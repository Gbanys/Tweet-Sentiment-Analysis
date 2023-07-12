from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

import pandas as pd
import logging

def train_and_evaluate_naive_bayes_classifier(
        train_text_dataframe: pd.DataFrame, 
        test_text_dataframe: pd.DataFrame
) -> MultinomialNB:

    X_train = train_text_dataframe['preprocessed_text'] 
    y_train = train_text_dataframe['sentiment']

    count_vect = CountVectorizer()
    X_train_counts = count_vect.fit_transform(X_train)

    tfidf_transformer = TfidfTransformer()
    X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

    naive_bayes_model = MultinomialNB().fit(X_train_tfidf, y_train)

    logging.info("Naive bayes classifier trained successfully")

    X_test = test_text_dataframe['preprocessed_text']
    y_test = test_text_dataframe['sentiment']

    X_test_counts = count_vect.transform(X_test)
    X_test_tfidf = tfidf_transformer.transform(X_test_counts)

    test_score = naive_bayes_model.score(X_test_tfidf, y_test)

    logging.info(f'Model evaluated with test score {test_score}')

    return naive_bayes_model