class Label:

  def __init__(self, title):
    self.title = title
    self.includes = [ ]
    self.excludes = [ ]

  def __str__(self):
    return self.title + str(self.includes)

  def add_author(self, author):
    self.includes.append(author)

  def remove_author(self, author):
    self.includes.remove(author)
    self.excludes.append(author)

  def train(self, db):
    includes_ranks = self.get_ranks(db, self.includes)
    excludes_ranks = self.get_ranks(db, self.excludes)

    for tup in includes_ranks[:20]:
      print tup[1], tup[0]
    return True

  def get_ranks(self, db, authors):
    counts = self.get_counts(db, authors)
    items = counts.items()
    items.sort(key = lambda el: el[1], reverse=True)
    return items


  def get_counts(self, db, authors):
    counts = { }
    for author in authors:
      tweets = db.get_by_author(author, 200)
      for tweet in tweets:
        for word in tweet.words:
          if not counts.get(word):
            counts[word] = 0
          counts[word] += 1
    # return the dictionary
    return counts
