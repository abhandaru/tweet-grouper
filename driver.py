import database
from label import Label

print "hello world!"
db = database.Database()

# authors
authors = [
  'elonmusk', 'espn', 'Harvard', 'nyjets', 'SportsCenter', 'NBA',
  'Stanford', 'UWaterloo', 'Yale'
]

# set up a label
label = Label('sports')
label.add_author('nyjets')
label.remove_author('UWaterloo')
label.train(db)
print label

# compute scores for each author
scores = [ ]
for author in authors:
  scores.append((author, label.get_similarity(db, author)))
scores.sort(key=lambda el: el[1], reverse=True)

# print out scores in order
for score in scores:
  print score[0], '\t', score[1]


