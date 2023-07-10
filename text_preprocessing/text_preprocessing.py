import pandas as pd
import re
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer


def remove_hashtags(text: str) -> str:
  text_without_hashtag = " ".join(re.sub(r"#(\w+)", '', text).split())
  return text_without_hashtag


def remove_users(text: str) -> str:
    text_without_users = " ".join(re.sub('(@[A-Za-z]+[A-Za-z0-9-_]+)', '', text).split())
    return text_without_users


def remove_links(text: str) -> str:
    text = " ".join(re.sub(r'http\S+', '', text).split())
    text = " ".join(re.sub(r'bit.ly/\S+', '', text).split())
    text = text.strip('[link]')
    return text


def remove_non_ascii_characters(text: str) -> str:
    return "".join(char for char in text if ord(char)<128)


def transform_text_to_lower_case(text: str) -> str:
   return text.lower()


def remove_stopwords(text: str) -> str:
  english_stopwords = set(stopwords.words("english"))
  english_stopwords.update(('So','arnt','so'))
  text_without_stopwords = ' '.join([word for word in text.split() if word not in english_stopwords]) 
  return text_without_stopwords


def remove_email_address(text: str) -> str:
  email = re.compile(r'[\w\.-]+@[\w\.-]+')
  return " ".join(email.sub(r'',text).split())


def remove_punctuation(text: str) -> str:
  token = RegexpTokenizer(r'\w+')
  text = token.tokenize(text)
  text = " ".join(text)
  return text 


def remove_digits(text: str) -> str:
    pattern = r'[^a-zA-z.,!?/:;\"\'\s]' 
    return " ".join(re.sub(pattern, '', text).split())


def preprocess_text_data(text: str) -> str:
  text_preprocessing_functions = [
      remove_hashtags, 
      remove_users, 
      remove_links, 
      remove_non_ascii_characters,
      transform_text_to_lower_case,
      remove_stopwords, 
      remove_email_address,
      remove_punctuation,
      remove_digits
  ]
  for function in text_preprocessing_functions:
      text = function(text)

  return text
   
