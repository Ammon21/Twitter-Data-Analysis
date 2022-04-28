import pandas as pd
import re

#Debugged by Ammon on April 25th 2022

class Clean_Tweets:
    """
    The PEP8 Standard AMAZING!!!
    """
    def __init__(self, df:pd.DataFrame):
        self.df = df
        print('Automation in Action...!!!')
        
        
    def fill_missing(self, df: pd.DataFrame, column: str, value):
        """
        fill null values of a specific column with the provided value
        """

        df[column] = df[column].fillna(value)

        return df      
        
    def drop_unwanted_column(self, df:pd.DataFrame)->pd.DataFrame:
        """
        remove rows that has column names. This error originated from
        the data collection stage.  
        """
        unwanted_rows = df[df['retweet_count'] == 'retweet_count' ].index
        df.drop(unwanted_rows , inplace=True)
        df = df[df['polarity'] != 'polarity']
        
        return df
    def drop_duplicate(self, df:pd.DataFrame)->pd.DataFrame:
        """
        drop duplicate rows
        """
        #code to drop duplicates with the same entry on all columns
               
        df.drop_duplicates()
        
      
   
    def convert_to_datetime(self, df:pd.DataFrame)->pd.DataFrame:
        """
        convert column to datetime
        """
        #changing the column to date format using todatetime() func
        
        df['created_at'] = pd.to_datetime(df['created_at'])
        
         
        
        return df
    
    def convert_to_numbers(self, df:pd.DataFrame)->pd.DataFrame:
        """
        convert columns like polarity, subjectivity, retweet_count
        favorite_count etc to numbers
        """
        #changing the column to numbers format using tonumeric() func
        
        df['polarity'] = pd.to_numeric(df['polarity'])
        df['subjectivity'] = pd.to_numeric(df['subjectivity'])
        df['retweet_count'] = pd.to_numeric(df['retweet_count'])
        df['favorite_count'] = pd.to_numeric(df['favorite_count'])
        
        return df
    
    def remove_non_english_tweets(self, df:pd.DataFrame)->pd.DataFrame:
        """
        remove non english tweets from lang
        """
        
        df = df.drop(df[df['language'] != 'en'].index)
        
        return df
        
    def extract_device_name(self, source: str):
        """
        returns device name from source text
        """
        res = re.split('<|>', source)[2].strip()
        return res    
        
       