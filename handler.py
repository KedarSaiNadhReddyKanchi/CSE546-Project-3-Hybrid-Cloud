from fileinput import filename
from boto3 import client as boto3_client
import face_recognition
import pickle
import urllib.parse
import boto3
import botocore
import os
import json
import csv
from decimal import Decimal
from boto3.dynamodb.conditions import Attr

print('Loading function')

s3 = boto3.client('s3')

dir_video =  '/tmp' + "/video/"

dir_image = '/tmp' + "/images/"




s3 = boto3.client('s3')
dynamoDB = boto3.resource('dynamodb')

table_name = 'CSE546Project2StudentData'
table = dynamoDB.Table(table_name)
path_encode = '/home/app/encoding'
s3_input_bucket = 'cc-input-546'
s3_output_bucket = 'cc-output-546'

os.makedirs(dir_video, exist_ok=True)
os.makedirs(dir_image, exist_ok=True)


def image_processing(path_image):

    file_image = face_recognition.load_image_file(path_image)
    encode_image_file = face_recognition.face_encodings(file_image)[0]

    with open(path_encode, 'rb') as f: 
        get_data = pickle.load(f)
        get_name = get_data['name']
        get_encoding = get_data['encoding']

    data_compare = face_recognition.compare_faces(get_encoding, encode_image_file)
    for value in data_compare:
        if value:
            index = data_compare.index(value)
            print(get_name[index])
            return (get_name[index])


def dynamodb_result(get_name):
        try:
            db_response = table.scan(FilterExpression=Attr('name').eq(get_name))
            get_item = db_response.get('Items', [])
            if get_item:
                print("Match Found")
                return get_item[0] 
        except Exception as e:
            print(f"An error occurred while querying the table: {e}")
        return None

def face_recognition_handler(ret):	
    print("Received event: " + ret)

    event_bucket = s3_input_bucket
    event_object_key = ret.s3_object_key

    try : 
        
        try:
            s3_response = s3.get_object(Bucket=event_bucket, Key=event_object_key)
            s3_data = s3_response['Body'].read()
            with open(dir_video + event_object_key, 'wb') as f:
                f.write(s3_data)
            s3.delete_object(Bucket=event_bucket, Key=event_object_key)
        except Exception as e:
            print(f'Error while downloading video from S3: {e}')

        try:
            os.system(f"ffmpeg -i {dir_video + event_object_key} -r 1 {dir_image}image-%3d.jpeg")
            print("Images extracted successfully")
        except Exception as e:
            print(f'Error while extracting images: {e}')
    
        get_name = image_processing(dir_image+ "image-002.jpeg")

        result = dynamodb_result(get_name)

        print("creating csv file")
    
        file_name = event_object_key + result["name"] + ".csv"
        file_path = '/tmp/' + event_object_key + file_name
        with open(file_path, 'w') as csvfile: 
            file_write = csv.writer(csvfile, delimiter=',',
                                quoting=csv.QUOTE_MINIMAL)               
            file_write.writerow(['Name','Major','Year'])
            file_write.writerow([result['name'], result['major'], result['year']])

        print("upload file started")
        s3.upload_file(
                        Bucket = s3_output_bucket,
                        Filename = file_path,
                        Key = file_name
                    )  
        print("upload file completed")      
        os.remove(file_path)  

    except Exception as e :
        print(e)
        raise e
    
def handle(ret):
    face_recognition_handler(ret)