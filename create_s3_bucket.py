import boto3

def create_s3_bucket():
    s3_client = boto3.client('s3')

    bucket_name = 'my-s3-bucket'
    s3_client.create_bucket(Bucket=bucket_name)

    print(f"S3 bucket '{bucket_name}' created successfully.")
