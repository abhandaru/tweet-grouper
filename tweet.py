class Tweet:

  def __init__(self, data):
    self.author = data['author']
    self.text = data['text']
    self.recipients = [ ]
    self.hashtags = [ ]
    self.words = [ ]
    # parse out the text
    tokens = self.text.split(' ')
    for token in tokens:
      if token.startswith('@'):
        self.recipients.append(token[1:])
      elif token.startswith('#'):
        self.hashtags.append(token[1:])
      else:
        self.words.append(token)

  def __str__(self):
    return str(self.author) + ': ' + self.text
