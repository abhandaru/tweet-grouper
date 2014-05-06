class Label:

  RANK_CUTOFF = 100

  def __init__(self, title):
    self.title = title
    self.includes = [ ]
    self.excludes = [ ]
    self.exceptions = [ ]
    self.pos_ranks = [ ]
    self.neg_ranks = [ ]

  def __str__(self):
    return self.title + str(self.includes)

  def add_author(self, author):
    if self.excludes.count(author) > 0:
      self.excludes.remove(author)
    self.includes.append(author)

  def remove_author(self, author):
    if self.includes.count(author) > 0:
      self.includes.remove(author)
    self.excludes.append(author)

  def members(self, db, authors):
    print 'Similarity scores ...'
    scores = { }
    for author in authors:
      score = self.get_similarity(db, author)
      scores[author] = score
      print '  ', author.ljust(15), score

    # compile a list of candidates
    candidates = [ ]
    total = 0
    for author in authors:
      if not author in self.includes and not author in self.excludes:
        candidates.append(author)
        total += scores[author]

    # compute the average score
    avg = total / len(candidates)
    print 'Average score:', avg

    # include authors
    members = self.includes[:]
    for author in candidates:
      if author not in self.exceptions and scores[author] > avg:
        members.append(author)
    return members

  def train(self, db):
    self.pos_ranks = self.get_ranks(db, self.includes)
    self.neg_ranks = self.get_ranks(db, self.excludes)
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
        total += self.score_function(i, pos_index, test, self.pos_ranks[pos_index])
      if neg_index >= 0:
        total -= self.score_function(i, neg_index, test, self.neg_ranks[neg_index])
    return total

  def score_function(self, index1, index2, rank1, rank2):
    w1 = rank1[1]
    w2 = rank2[1]
    return 1.0 * (w1 + w2) / ((1 + index1) * (1 + index2))

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
    return items[:Label.RANK_CUTOFF]

  def get_counts(self, db, authors):
    counts = { }
    for author in authors:
      tweets = db.get_by_author(author)
      for tweet in tweets:
        for word in tweet.words:
          if not counts.get(word):
            counts[word] = 0
          counts[word] += 1
    # return the dictionary
    return counts
