from access_s3_storage import read_text_data_from_s3
from machine_learning_workflow.train_and_evaluate_ml_model import train_and_evaluate_naive_bayes_classifier
from text_preprocessing.text_preprocessing import preprocess_text_data

import logging

logging.basicConfig(level=logging.INFO)

aws_key = input("Please enter your aws access key: ")
aws_secret = input("Please enter your aws secret access key: ")

train_text_dataframe = read_text_data_from_s3(aws_key, aws_secret, file='train.csv')
train_text_dataframe = train_text_dataframe.dropna(subset=['text'])
train_text_dataframe['preprocessed_text'] = train_text_dataframe['text'].apply(preprocess_text_data)

test_text_dataframe = read_text_data_from_s3(aws_key, aws_secret, file='test.csv')
test_text_dataframe = test_text_dataframe.dropna(subset=['text'])
test_text_dataframe['preprocessed_text'] = test_text_dataframe['text'].apply(preprocess_text_data)

naive_bayes_model = train_and_evaluate_naive_bayes_classifier(train_text_dataframe, test_text_dataframe)
