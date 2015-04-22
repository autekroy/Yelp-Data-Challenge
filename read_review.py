import json
import os.path



# save all reviews from only one business id
def all_reviews_from_business(json_path):
	with open(json_path, "r") as review:
		for line in review:
			line_contents = json.loads(line)
			f = open('all_review_based_on_category/Restaurants_review.txt', 'a')
			f.write(json.dumps(line_contents[u'text'])[1:-1] + '\n')
			f.close()


def main():
	review_path = "review_based_on_business_and_category/Restaurants/4bEjOyTaDG24SY5TxsaUNQ.json"
	all_reviews_from_business(review_path)

if __name__ == "__main__":
	main()