class Tweet:

  def __init__(self, data):
    self.author = data['author']
    self.text = data['text']

  def __str__(self):
    return str(self.author) + ': ' + self.text
