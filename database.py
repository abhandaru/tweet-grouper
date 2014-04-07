import io
import json
import tweet

class Database:

  DATA_PATH = 'data/tweets-9/tweets-9.json'

  def __init__(self):
    self.tweets = [ ]

    path = Database.DATA_PATH
    with open(path) as data:
      tweets_data = json.load(data)
      for tweet_data in tweets_data:
        t = tweet.Tweet(tweet_data)
        self.tweets.append(t)

  def get_by_author(self, author):
    results = [ ]
    for tweet in self.tweets:
      if tweet.author == author:
        results.append(tweet)
    return results
