import time

import twint
import nest_asyncio
import pandas as pd
import random
import schedule

def gettweets(username):
    c = twint.Config()
    c.Username = username
    c.Limit =  2000

    c.User_full = True
    c.Count = True
    c.Stats = True
    c.Pandas = True
    c.Store_pandas = True
    c.Hide_output = True
    c.Pandas_clean = True

    c.Store_csv = True
    c.Output = "tweets.csv"
    nest_asyncio.apply()
    twint.run.Search(c)
    return

def display_tweet():
    df = pd.read_csv("tweets.csv")
    tweets = df.tweet.to_list()
    print(random.choice(tweets))




gettweets(input("Enter Username"))
delay = int(input("Enter your time delay in seconds"))
while True:
    time.sleep(delay)
    display_tweet()






