class Tweet:

  # Exclude common words in the English language.
  WORD_FILTER = [
    'the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'i', 'it',
    'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at', 'rt', 'w/',
    '&', 'is', 'we', 'an', 'this', 'but', 'his', 'by', 'from', 'they', 'say',
    'her', 'she', 'or', 'will', 'my', 'all', 'would', 'there', 'their', 'what',
    'so', 'if', 'who', 'get', 'which', 'me', 'are', 'our', 'your', 'here',
    'has', 'how'
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
      # trim off extraneous characters
      token = token.strip('.:()<>-').lower()
      # make sure we have a non-empty string
      if not token:
        continue
      # is the word in our exclusion set?
      if token in Tweet.WORD_FILTER:
        continue
      # is the token just a number?
      if token.isnumeric():
        continue
      # identify special tokens
      if token.startswith('@'):
        self.recipients.append(token[1:])
      elif token.startswith('#'):
        self.hashtags.append(token[1:])
      else:
        self.words.append(token)

  def __str__(self):
    return str(self.author) + ': ' + self.text
