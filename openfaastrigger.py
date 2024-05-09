import subprocess
import time
import boto3
import json
import requests

#AWS S3 CONFIGURATION
bucket_name = "cc-input-546"
region= "us-east-1"

# OpenFaaS Configuration
openfaas_gateway = "http://192.168.49.2:31112"  # Update with your OpenFaaS gateway URL
openfaas_function = "app1"  # Update with your OpenFaaS function name

def poll_s3_bucket():
    s3 = boto3.resource('s3', region_name=region)
    bucket = s3.Bucket(bucket_name)

    for obj in bucket.objects.all():
        # Process the object or perform other actions
        print(f"Processing S3 Object: {obj.key}")

        # Invoke OpenFaaS function with HTTP request
        invoke_openfaas_function(obj.key)

def invoke_openfaas_function(s3_object_key):
    openfaas_url = f"{openfaas_gateway}/function/{openfaas_function}"
    print("open faas url formed in the code is :- " , openfaas_url)
    headers = {"Content-Type": "application/json"}
    # Assuming your OpenFaaS function expects JSON payload, adjust accordingly
    payload = {
        "s3_object_key": s3_object_key
    }
    print(" we get the payload object key")
    print(s3_object_key)
    # Invoke OpenFaaS function using curl
    #subprocess.run(["curl", "-X", "POST", openfaas_url, "-d", json.dumps(payload), "-H", f"{headers}"])

    # Construct the curl command
    curl_command = f'curl -X POST -d \'{payload}\' {openfaas_url} '
    result = subprocess.run(curl_command, shell=True)
    print("the result returned from the handler.py file when executed")
    print(result)
    if result.returncode == 0:
        print(f"Function invoked successfully. Output: {result.stdout}")
    else:
        print(f"Error invoking function. Return code: {result.returncode}, Error: {result.stderr}")

    #try:
     #   response = requests.post(openfaas_url , json=payload)
      #  print("the status code for response is " , response.status_code)
    #except Exception as e:
     #   print (f"Error invoking the open faas function : {e}")

if __name__ == "__main__":
    a = 1
    while a == 1:
        poll_s3_bucket()
        a = a + 1
        #time.sleep(60)  # Adjust the polling interval as needed