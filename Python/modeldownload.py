import boto3
import botocore

BUCKET_NAME = '' # replace with your bucket name
KEY = '' # replace with your object key

s3 = boto3.resource('s3')

try:
    print('Downloading')
    s3.Bucket(BUCKET_NAME).download_file(KEY, 'efficientnetb6_notop.h5')
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise