### split reviews based on different business id
### create different reviews files named after by business id
### all reviews files in 'yelp_dataset_challenge_academic_dataset' folder

### create reviews based on category of different business ID
### all reviews (different category) will in the "review_based_on_business_and_category" folder

import re
import json
import os.path
import shutil

def read_and_write_file():
	"""Read in the json dataset file from 'yelp_academic_dataset_review.json' """
	json_path = "yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_review.json"

	with open(json_path, "r") as allReview:
		for line in allReview:
			review = json.loads(line)
			ID = review[u'business_id']
			f = open('review_based_on_business_ID/' + ID +'.json', 'a')
			f.write(json.dumps(review) + '\n')
			f.close() # definitely this line! or it will missing last line in file


def divide_review_on_category():

	json_path = "yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_business.json"
	
	with open(json_path, "r") as business:
		for line in business:
			line_contents = json.loads(line)
			ID = line_contents[u'business_id']
			filename = 'review_based_on_business_ID/' + ID + '.json'
			# print filename
			if os.path.isfile(filename): # this business id has review data
				for cat in line_contents[u'categories']:
					folder_path = 'review_based_on_business_and_category/' + json.dumps(cat)[1:-1] #remove quotation mark
					# print folder_path
					if not os.path.exists(folder_path): # create category folder
						os.makedirs(folder_path)
					shutil.copyfile(filename, folder_path + '/' + ID + '.json')



def main():
	read_and_write_file() # take within 3 miuntes
	divide_review_on_category() # take within minutes

if __name__ == "__main__":
  main()