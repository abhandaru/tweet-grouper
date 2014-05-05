class Label:

  def __init__(self, title):
  	self.title = title
  	self.authors = []

  def __str__(self):
  	labelString = self.title + ': ' 
  	for author in self.authors:
  		labelString = labelString + author + ' '
  	return labelString

  def add_author(self, author):
  	self.authors.append(author)

  def remove_author(self, author):
  	self.authors.remove(author)

  def train(self, db):
  	




