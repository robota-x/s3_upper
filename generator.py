import boto3
import json

s3_client = boto3.client("s3")


def create_presigned_url(bucket_name, object_name):
    return s3_client.generate_presigned_url(
        ClientMethod="put_object",
        Params={"Bucket": bucket_name, "Key": object_name},
        ExpiresIn=300,
    )


def lambda_handler(event, context):
    try:
        object_name = event["queryStringParameters"]["filename"]
        bucket_name = event["queryStringParameters"]["bucketname"]
    except KeyError:
        return {
            "isBase64Encoded": False,
            "statusCode": "200",
            "body": "missing query param!",
            "headers": {"Content-Type": "text/plain"},
        }

    return {
        "isBase64Encoded": False,
        "statusCode": "200",
        "body": create_presigned_url(bucket_name, object_name),
        "headers": {"Content-Type": "text/plain"},
    }
