import database

print "hello world!"
db = database.Database()

# inputs
labels = [ ]

tweets = db.get_by_author('Harvard', 5)
for tweet in tweets:
  print tweet
  print tweet.hashtags, tweet.recipients
  print

