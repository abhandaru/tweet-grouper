class Tweet:

  # Exclude common words in the English language.
  WORD_FILTER = [
    'the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I', 'it',
    'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at', 'RT', 'w/',
    '&'
  ]

  def __init__(self, data):
    self.author = data['author']
    self.text = data['text']
    self.recipients = [ ]
    self.hashtags = [ ]
    self.words = [ ]
    # parse out the text
    tokens = self.text.split(' ')
    for token in tokens:
      token = token.strip('.:')
      # make sure we have a non-empty string
      if not token:
        continue
      # trim out special characters
      if token.startswith('@'):
        self.recipients.append(token[1:])
      elif token.startswith('#'):
        self.hashtags.append(token[1:])
      elif not token.isnumeric() and token not in Tweet.WORD_FILTER:
        self.words.append(token)

  def __str__(self):
    return str(self.author) + ': ' + self.text
