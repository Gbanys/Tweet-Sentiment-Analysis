import unittest
from text_preprocessing import (
    remove_hashtags, 
    remove_users, 
    remove_links, 
    remove_non_ascii_characters, 
    remove_stopwords, 
    remove_email_address, 
    remove_punctuation, 
    remove_digits,
    preprocess_text_data
)

class TestTextPreprocessing(unittest.TestCase):

    def test_remove_hashtag(self) -> None:
        sample_text = "This is a #samplehashtag text"
        result = remove_hashtags(sample_text)
        expected_result = 'This is a text'
        self.assertEqual(result, expected_result)

    def test_remove_users(self) -> None:
        sample_text='This is a @sampleuser text'
        result = remove_users(sample_text)
        expected_result = 'This is a text'
        self.assertEqual(result, expected_result)

    def test_remove_links(self) -> None:
        sample_text='This is a twitter picture url: http://twitpic.com/?????. This is a bitly url: http://bit.ly/?????.'
        result = remove_links(sample_text)
        expected_result = 'This is a twitter picture url: This is a bitly url:'
        self.assertEqual(result, expected_result)

    def test_remove_non_ascii_characters(self) -> None:
        sample_text='Characters such as α, β and γ come from the Greek alphabet'
        result = remove_non_ascii_characters(sample_text)
        expected_result = 'Characters such as ,  and  come from the Greek alphabet'
        self.assertEqual(result, expected_result)

    def test_remove_stopwords(self) -> None:
        sample_text='This is so exciting'
        result = remove_stopwords(sample_text)
        expected_result='This exciting'
        self.assertEqual(result, expected_result)

    def test_remove_email_address(self) -> None:
        sample_text='The email address is test@gmail.com'
        result = remove_email_address(sample_text)
        expected_result='The email address is'
        self.assertEqual(result, expected_result)

    def test_remove_punctuation(self) -> None:
        sample_text = 'testword1, testword2, testword3!!!!'
        result = remove_punctuation(sample_text)
        expected_result='testword1 testword2 testword3'
        self.assertEqual(result, expected_result)

    def test_remove_digits(self) -> None:
        sample_text = 'test123, test? 5678'
        result = remove_digits(sample_text)
        expected_result = 'test, test?'
        self.assertEqual(result, expected_result)

    def test_preprocess_text_data(self) -> None:
        sample_text = "Hugh Masekela pix online + Contern - T71 pix + review @ http://clada.lu -> coming up next Naturally7 Concert this evening"
        result = preprocess_text_data(sample_text)
        expected_result = 'hugh masekela pix online contern t pix review coming next naturally concert evening'
        self.assertEqual(result, expected_result)


unittest.main()