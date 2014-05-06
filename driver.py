import database
from label import Label

print 'Running driver ...'
db = database.Database()

# authors
following = [
  'elonmusk', 'espn', 'Harvard', 'nyjets', 'SportsCenter', 'NBA',
  'Stanford', 'UWaterloo', 'Yale'
]

# set up a label
label = Label('sports')
label.add_author('Stanford')
# label.add_author('espn')
# label.remove_author('elonmusk')
label.train(db)

# print out some information about the label
print 'Label: ', label
for el in label.pos_ranks[:20]:
  print '  ', el[1], el[0]

# see which authors are chosen for membership
members = label.members(db, following)
print 'Members:'
for m in members:
  print '  ', m
