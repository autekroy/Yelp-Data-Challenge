###### Test script for functions in 

import re
import json
import os.path
import shutil
import logging, gensim, bz2
from vaderSentiment.vaderSentiment import sentiment as vaderSentiment # for Sentiment


# test sentimental analysis
json_path = "review_based_on_business_and_category/Restaurants/4bEjOyTaDG24SY5TxsaUNQ.json"

count = 0
reviewLine = []
with open(json_path, "r") as review:
	for line in review:
		line_contents = json.loads(line)
		line_contents = json.dumps(line_contents[u'text'])[1:-1].replace('\n', ' ')
		reviewLine.append(line_contents)
		vaderSentiment(line_contents)
		# if count >= 2:
			# break

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
id2word = gensim.corpora.Dictionary.load_from_text('all_review_based_on_category/Restaurants_review.txt')

# json_path = "review_based_on_business_and_category/Restaurants/4bEjOyTaDG24SY5TxsaUNQ.json"

# all_review = []
# with open('all_review_based_on_category/Restaurants_review.txt', 'r') as review:
# 	for line in review:
# 		all_review.append(line[:-1]) # ignore the skip line symbol ('\n')
# 		