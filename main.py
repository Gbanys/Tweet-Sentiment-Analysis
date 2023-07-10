from access_s3_storage import read_text_data_from_s3

aws_key = input("Please enter your aws access key: ")
aws_secret = input("Please enter your aws secret access key: ")

tweet_text_data_dataframe = read_text_data_from_s3(aws_key, aws_secret, file='train.csv')
print(tweet_text_data_dataframe)
