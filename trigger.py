import os
import boto3
import time
# Create an S3 client
endpoint = "http://192.168.217.128:8084"

access_key = 'US4LZ44BLIV7RAIC399X'
secret_key = 'WnFCbyNVE8pXxC2nI2ZmHSoomLbB4M2pbXKsryeb'

s3 = boto3.client(
        's3',
        endpoint_url=endpoint,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
        )
# s3 = boto3.client('s3')

processed_files = set()

bucket_name = 'my-new-bucket1'
# List objects in the S3 bucket
response = s3.list_objects_v2(Bucket=bucket_name)

counter = 0
# Check for new objects and invoke the function
for obj in response.get('Contents', []):
    key = obj['Key']
    if key not in processed_files:
        # Generate and execute the curl command for each new object
        # command = "echo '{{\"Records\":[{{\"s3\":{{\"object\":{{\"key\":\""+key+"\"}}}}}}]}}' | faas-cli invoke -f proj3.yml proj3"
        command = 'curl -X POST -d \'{"Records":[{"s3":{"object":{"key":"'+key+'"}}}]}\' http://localhost:8080/function/proj3'
        # print(command)
        print(f"\nRunning for {key}")
        os.system(command)

        time.sleep(5)

        # Mark the object as processed to avoid reprocessing
        processed_files.add(key)
        counter += 1

print(f"Number of files processed: {counter}")