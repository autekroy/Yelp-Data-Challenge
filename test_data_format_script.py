import re
import json
from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol
import os.path
import shutil

# for testing category review
# json_path = "yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_business.json"

# test = []
# with open(json_path, "r") as business:
# 	count = 0
# 	for line in business:
# 		line_contents = json.loads(line)
# 		count += 1
# 		test.append(line_contents)
# 		if count == 10: # only store 10 review to see the data format
# 			break

# # check if there's a existing file
# for line in test:
# 	ID = line[u'business_id']
# 	filename = 'review_based_on_business_ID/' + ID + '.json'
# 	# print filename
# 	if os.path.isfile(filename): # this business id has review data
# 		for cat in line[u'categories']:
# 			folder_path = 'review_based_on_business_and_category/' + json.dumps(cat)[1:-1] #remove quotation mark
# 			# print folder_path
# 			if not os.path.exists(folder_path): # create category folder
# 				os.makedirs(folder_path)
# 			shutil.copyfile(filename, folder_path + '/' + ID + '.json')



# for testing split review based on business id
# json_path = "yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_review.json"

# test = []
# with open(json_path, "r") as review:
# 	count = 0
# 	for line in review:
# 		line_contents = json.loads(line)
# 		count += 1
# 		test.append(line_contents)
# 		if count == 10: # only store 10 review to see the data format
# 			break

# type(test) 		# list
# type(test[0])	# dictionary

# for review in test:
# 	ID = review[u'business_id']
# 	f = open('review_based_on_business_ID/' + ID +'.json', 'a')
# 	f.write(json.dumps(review) + '\n')
# 	f.close() # definitely this line! or it will missing last line in file

# # all business id
# with open(json_path, "r") as allReview:
# 	for line in allReview:
# 		review = json.loads(line)
# 		ID = review[u'business_id']
# 		f = open('review_based_on_business_ID/' + ID +'.json', 'a')
# 		f.write(json.dumps(review) + '\n')
# 		f.close() # definitely this line! or it will missing last line in file

