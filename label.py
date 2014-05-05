class Label:

  def __init__(self, title):
    self.title = title
    self.authors = [ ]
    self.excludes = [ ]

  def __str__(self):
    return self.title + str(self.authors)

  def add_author(self, author):
    self.authors.append(author)

  def remove_author(self, author):
    self.authors.remove(author)
    self.excludes.append(author)

  def train(self, db):

    return True
