import io
import json
import tweet

class Database:

  DATA_PATH = 'data/tweets-12/tweets-12.json'

  def __init__(self):
    self.tweets = [ ]
    self.authors = { }
    # Read in the file.
    path = Database.DATA_PATH
    with open(path) as data:
      tweets_data = json.load(data)
      for tweet_data in tweets_data:
        t = tweet.Tweet(tweet_data)
        a = t.author
        if not self.authors.get(a):
          self.authors[a] = [ ]
        self.authors[a].append(t)
        self.tweets.append(t)


  def get_authors(self):
    return self.authors.keys()

  def get_by_author(self, author, limit=None):
    results = self.authors[author]
    return results[:limit]
