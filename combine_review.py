import json
import os.path
import sys

# os.listdir() will get you files and directories that's in a directory.
def create_train_test_set(category):
	category_path = "review_based_on_business_and_category/" + category
	if not os.path.isdir(category_path):
		print "There's no such category name. Please try again."
		exit(1)

	review_files = os.listdir(category_path)
	print 'How many reviews in category ' + category + ': ' + str(len(os.listdir(category_path)))

	if not os.path.exists('dataset/'): # the dataset folder
		os.makedirs('dataset/')

	f = open('dataset/' + category + '_training_set.txt', 'w')
	f.write("review_id\treview\tstars\n")
	f.close()

	f = open('dataset/' + category + '_testing_set.txt', 'w')
	f.write("review_id\treview\tstars\n")
	f.close()

	# For every business in the category, we split them into training and testing dataset
	# for i in xrangelen(os.listdir(category_path)):
	for i in xrange(3000):
		business_path = 'review_based_on_business_and_category/' + category + '/' + review_files[i]
		if i % 2:
			all_reviews_from_one_business(category, business_path, 'training_set')
		else:
			all_reviews_from_one_business(category, business_path, 'testing_set')


# save all reviews from only one business id and save them into files
def all_reviews_from_one_business(category, json_path, dataset_type):
	count = 0
	with open(json_path, "r") as review:
		f = open('dataset/' + category + '_' + dataset_type + '.txt', 'a')
		for line in review:
			line_contents = json.loads(line)
			# print str(json.dumps(line_contents[u'stars']))
			f.write(json.dumps(line_contents[u'review_id'])[1:-1])
			f.write('\t')
			f.write(json.dumps(line_contents[u'text'])[1:-1].replace('\n', ' '))
			f.write('\t')
			f.write(json.dumps(line_contents[u'stars']))
			f.write('\n')

			count += 1
			# if count >= 20:
			# 	break
		f.close()

	# print count

def main():
	# review_path = "review_based_on_business_and_category/Restaurants/4bEjOyTaDG24SY5TxsaUNQ.json"
	# all_reviews_from_one_business(review_path)
	if len(sys.argv) < 2:
		print "You have to give a category! (Ex: Restaurants)"
		exit(1)

	create_train_test_set(sys.argv[1])

if __name__ == "__main__":
	main()