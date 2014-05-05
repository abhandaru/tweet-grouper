class Label:

  def __init__(self, title):
    self.title = title
    self.includes = [ ]
    self.excludes = [ ]
    self.pos_ranks = [ ]
    self.neg_ranks = [ ]

  def __str__(self):
    return self.title + str(self.includes)

  def add_author(self, author):
    self.includes.append(author)

  def remove_author(self, author):
    if self.includes.count(author) > 0:
      self.includes.remove(author)
    self.excludes.append(author)

  def contains(self, author):
    # trivial cases for membership
    if author in self.includes:
      return True
    if author in self.excludes:
      return False
    # common case: compute similarity score
    # TODO: Figure out cut-off
    score = self.get_similarity(db, author)
    return False

  def train(self, db):
    self.pos_ranks = self.get_ranks(db, self.includes)
    self.neg_ranks = self.get_ranks(db, self.excludes)
    for tup in self.pos_ranks[:20]:
      print tup[1], tup[0]
    return True

  #
  # Private helper methods
  #

  def get_similarity(self, db, author):
    total = 0
    ranks = self.get_ranks(db, [author])
    for i in xrange(len(ranks)):
      test = ranks[i]
      pos_index = self.index(self.pos_ranks, test)
      neg_index = self.index(self.neg_ranks, test)
      if pos_index >= 0:
        total += self.score_function(i, pos_index, self.pos_ranks[pos_index][1])
      if neg_index >= 0:
        total -= self.score_function(i, neg_index, self.neg_ranks[neg_index][1])
    return total

  def score_function(self, index1, index2, weight):
    return 1.0 * weight / ((1 + index1) * (1 + index2))

  def index(self, ranks, test):
    for i in xrange(len(ranks)):
      rank = ranks[i]
      if rank[0] == test[0]:
        return i
    return -1

  def get_ranks(self, db, authors):
    counts = self.get_counts(db, authors)
    items = counts.items()
    items.sort(key=lambda el: el[1], reverse=True)
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
