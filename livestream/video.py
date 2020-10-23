import boto3
from authentication import configProperties

#This file takes in the folder from S3 and generates a pre-signed url with an argument
#where you can define the index of the file in the bucket.

def video_url(index, bucket):
    if index == None:
        print("File index is empty")
    elif bucket == None:
        print("Please specify a bucket name")
    else:

        #Call S3 Boto3 Client
        s3_client = boto3.client('s3',)

        #list bucket objects, specify the index and return the object URL.
        list_bucket_object = s3_client.list_objects(Bucket=bucket)

        object_properties = bucket_object.get('Contents')

        object_name = object_properties[index]['Key']

        object_url = s3_client.generate_presigned_url(
                ClientMethod='get_object',
                Params={
                    'Bucket':bucket,
                    'Key':object_name,
                    },
                ExpiresIn=3800,
            )
    return object_url
