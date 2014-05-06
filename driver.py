import database
from label import Label

print 'Running driver ...'
db = database.Database()

# authors
following = db.get_authors()

# set up a label
label = Label('schools')
label.add_author('Yale')
label.add_author('CarnegieMellon')
# label.add_author('Harvard')
# label.add_author('facebook')
# label.add_author('Yale')
# label.add_author('UWaterloo')
# label.add_author('espn')
# label.remove_author('facebook')
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
