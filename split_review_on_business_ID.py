### split reviews based on different business id
### create different reviews files named after by business id
### all reviews files in 'yelp_dataset_challenge_academic_dataset' folder

import re
import json

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


def main():
	read_and_write_file()

if __name__ == "__main__":
  main()