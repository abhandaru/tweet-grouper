import database

print "hello world!"
db = database.Database()

tweets = db.get_by_author('elonmusk')
print tweets
