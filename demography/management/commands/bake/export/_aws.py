import boto3
from demography.conf import settings


def get_bucket():
    session = boto3.session.Session(
        region_name=settings.AWS_REGION,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
    )
    s3 = session.resource('s3')
    return s3.Bucket(settings.AWS_S3_BUCKET)
