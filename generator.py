import boto3
import json

s3_client = boto3.client("s3")


def create_presigned_post(bucket_name, object_name):
    return s3_client.generate_presigned_post(
        bucket_name, object_name, ExpiresIn=300
    ).get("url")


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))

    upload_url = create_presigned_post('TODO', 'test-file.txt')


    return {
        "statusCode": "200",
        "body": upload_url,
        "headers": {"Content-Type": "text/plain"},
    }

