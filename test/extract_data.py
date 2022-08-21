import unittest
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join('scripts')))
from extract_dataframe import read_json
from extract_dataframe import TweetDfExtractor
_, tweet_list = read_json("data/Economic_Twitter_Data.zip")

columns = ['created_at', 'source', 'original_text', 'clean_text', 'sentiment', 'polarity', 'subjectivity', 'lang', 'favorite_count', 'retweet_count',
           'original_author', 'screen_count', 'followers_count', 'friends_count', 'possibly_sensitive', 'hashtags', 'user_mentions', 'place']


class TestTweetDfExtractor(unittest.TestCase):
    def setUp(self) -> pd.DataFrame:
        self.df = TweetDfExtractor(tweet_list[:2])

    def test_find_statuses_count(self):
        self.assertEqual(self.df.find_statuses_count(), [40, 40])

    def test_retweet_text(self):
        retweet = ["""Irre: Annalena Baerbock sagt, es bricht ihr das Herz, dass man nicht bedingungslos schwere Waffen liefert.
Mir bric… https://t.co/1dSS6HdHBE""", """Merkel schaffte es in 1 Jahr 1 Million "Flüchtlinge" durchzufüttern, jedoch nicht nach 16 Jahren 1 Million Rentner aus der Armut zu holen."""]
        self.assertEqual(self.df.find_retweet_text(), retweet)

    def test_find_created_time(self):
        created_at = ['Fri Apr 22 22:20:18 +0000 2022',
                      'Fri Apr 22 22:19:16 +0000 2022']
        self.assertEqual(self.df.find_created_time(), created_at)

    def test_find_source(self):
        source = ['<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>',
                  '<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>']
        self.assertEqual(self.df.find_source(), source)

    def test_find_screen_name(self):
        name = ['McMc74078966', 'McMc74078966']
        self.assertEqual(self.df.find_screen_name(), name)

    def test_find_followers_count(self):
        f_count = [70860, 526]
        self.assertEqual(self.df.find_followers_count(), f_count)

    def test_find_friends_count(self):
        friends_count = [12, 12]
        self.assertEqual(self.df.find_friends_count(), friends_count)

    def test_find_is_sensitive(self):
        self.assertEqual(self.df.is_sensitive(), [
                         None, None])

    def test_find_favourite_count(self):
        self.assertEqual(self.df.find_favourite_count(),
                         [2356, 1985])

    def test_find_retweet_count(self):
        self.assertEqual(self.df.find_retweet_count(), [355, 505])

    def test_find_hashtags(self):
        hashtags = [None, None]
        self.assertEqual(self.df.find_hashtags(), hashtags)

    def test_find_user_mentions(self):
        user_mentions = ['nikitheblogger', 'sagt_mit']
        self.assertEqual(self.df.find_mentions(), user_mentions)

    def test_find_lang(self):
        self.assertEqual(self.df.find_lang(), ['de', 'de'])

    def test_find_location(self):
        self.assertEqual(self.df.find_location(), [
                         '', ''])


if __name__ == '__main__':
    unittest.main()