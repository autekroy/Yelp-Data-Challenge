import re
import json
from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol


json_path = "yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_review.json"

test = []
with open(json_path, "r") as review:
	count = 0
	for line in review:
		line_contents = json.loads(line)
		count += 1
		test.append(line_contents)
		if count == 10: # only store 10 review to see the data format
			break

type(test) 		# list
type(test[0])	# dictionary

for review in test:
	ID = review[u'business_id']
	f = open('review_based_on_business_ID/' + ID +'.json', 'a')
	f.write(json.dumps(review) + '\n')
	f.close() # definitely this line! or it will missing last line in file

# all business id
with open(json_path, "r") as allReview:
	for line in allReview:
		review = json.loads(line)
		ID = review[u'business_id']
		f = open('review_based_on_business_ID/' + ID +'.json', 'a')
		f.write(json.dumps(review) + '\n')
		f.close() # definitely this line! or it will missing last line in file

