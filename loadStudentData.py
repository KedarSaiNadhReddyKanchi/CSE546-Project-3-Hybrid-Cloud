import boto3
import json
db_table = 'CSE546Project2StudentData'
db = boto3.resource('dynamodb')

with open('student_data.json') as f:
    data = json.load(f)

get_db_table = db.Table(db_table)

with get_db_table.batch_writer() as batch:
    for value in data:
        batch.put_item(Item=value)
        print("Inserted item")