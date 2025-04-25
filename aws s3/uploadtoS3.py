import boto3
from botocore.exceptions import NoCredentialsError

# AWS credentials
aws_access_key_id = 'ASIASL7KN76GHENGPWVX'
aws_secret_access_key = '+4SIpV0PkgMFKcJZFuPXI+mIecbgZKnyop8Hgp8l'
aws_session_token = 'IQoJb3JpZ2luX2VjEJz//////////wEaCXVzLXdlc3QtMiJHMEUCIHHuEAQqoc/qhkKW1LmZEjVH83vS87Qw+dMxHGlGwnvKAiEAgldK0dow...'

# S3 configuration
bucket_name = 'tweet-project-sa'  
file_path = 'updated_jetblue_dataset.csv'  # Local file
s3_file_name = 'jetblue/processed/updated_jetblue_dataset.csv'  # Full S3 key (with folder path)

# Initialize S3 client
s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    aws_session_token=aws_session_token
)

# Upload file
try:
    s3.upload_file(file_path, bucket_name, s3_file_name)
    print(f"✅ Successfully uploaded {file_path} to s3://{bucket_name}/{s3_file_name}")
except FileNotFoundError:
    print("The file was not found.")
except NoCredentialsError:
    print("AWS credentials not available.")
except Exception as e:
    print(f"Upload failed: {e}")
