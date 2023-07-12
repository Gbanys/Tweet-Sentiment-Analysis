import pandas as pd
import boto3
import io

def read_text_data_from_s3(aws_key: str, aws_secret: str, file: str) -> pd.DataFrame:
    s3 = boto3.resource(
        service_name='s3',
        aws_access_key_id=aws_key,
        aws_secret_access_key=aws_secret
    ) 

    obj = s3.Bucket('gbanys').Object(f'tweet_text_data/{file}').get()

    text_data_df = pd.read_csv(io.BytesIO(obj['Body'].read()), encoding='unicode_escape')

    return text_data_df