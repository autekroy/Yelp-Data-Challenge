import json
import os.path


# os.listdir() will get you files and directories that's in a directory.



# save all reviews from only one business id
count = 0
def all_reviews_from_business(json_path):
	with open(json_path, "r") as review:
		for line in review:
			line_contents = json.loads(line)
			f = open('all_review_based_on_category/Restaurants_review.txt', 'a')
			f.write(json.dumps(line_contents[u'text'])[1:-1].replace('\n', ' ') + ' ')
			f.close()

			if count >= 20:
				break

def main():
	review_path = "review_based_on_business_and_category/Restaurants/4bEjOyTaDG24SY5TxsaUNQ.json"
	all_reviews_from_business(review_path)

if __name__ == "__main__":
	main()