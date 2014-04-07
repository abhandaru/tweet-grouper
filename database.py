import io
import json

class Database:

  DATA_PATH = 'data/tweets-9/tweets-9.json'

  def __init__(self):
    path = Database.DATA_PATH
    with open(path) as data:
      self.tweets = json.load(data)

  def get_by_author(self, author):
    results = [ ]
    for tweet in self.tweets:
      if tweet['author'] == author:
        results.append(tweet)
    return results
