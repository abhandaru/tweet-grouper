import database
from label import Label

print "hello world!"
db = database.Database()

# set up a label
label = Label('sports')
label.add_author('NBA')
# label.add_author('nyjets')
label.train(db)
print label

# tweets = db.get_by_author('Harvard', 5)
# for tweet in tweets:
#   print tweet
#   print tweet.hashtags, tweet.recipients
#   print

