#! /usr/bin/python

import glob
import os
import json
import io

DIR_TWEETS_TEXT = '../data/tweets-text'
EXT_TWEETS_TEXT = 'txt'

TOKEN_HANDLE = 'Handle'
TOKEN_TEXT = 'Text'

OUTPUT_DIR = '../data/tweets-12'
OUTPUT_FILE = 'tweets-12.json'

# find all data files
match = '/'.join([DIR_TWEETS_TEXT, '*.' + EXT_TWEETS_TEXT])
files = glob.glob(match)

# functions for parsing
def parseFile(text_list):
  data = [ ]
  current = None
  current_text = None
  current_author = None

  for line in text_list:
    line = line.strip()
    author_token = TOKEN_HANDLE + ':'
    text_token = TOKEN_TEXT + ':'

    if line.startswith(author_token):
      current = { }
      author = line.split(author_token)[1].strip()
      current['author'] = author

    elif line.startswith(text_token):
      text = line.split(TOKEN_TEXT + ':')[1].strip()
      current_text = text
      current['text'] = current_text
      data.append(current)

  # return the data
  return data

# iterate through files
data = [ ]
for path in files:
  file_data = [ ]
  with open(path) as f:
    text_list = f.readlines()
    file_data = parseFile(text_list)
    data += file_data
data_json = json.dumps(data, ensure_ascii = False)

# write data to file
output = '/'.join([OUTPUT_DIR, OUTPUT_FILE])
with open(output, 'w') as out:
  out.write(data_json)

