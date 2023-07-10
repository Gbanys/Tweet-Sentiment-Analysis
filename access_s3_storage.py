import pandas as pd

def read_text_data_from_s3(aws_key: str, aws_secret: str, file: str) -> pd.DataFrame:
    tweet_text_dataframe = pd.read_csv(
        f"s3://gbanys/tweet_text_data/{file}",
        storage_options={
            "key": aws_key,
            "secret": aws_secret,
        },
        encoding='unicode_escape'
    )
    return tweet_text_dataframe