#!/usr/bin/env python

#  Author: Angela Chapman
#  Date: 8/6/2014
#
#  This file contains code to accompany the Kaggle tutorial
#  "Deep learning goes to the movies".  The code in this file
#  is for Part 1 of the tutorial on Natural Language Processing.
#
# *************************************** #

import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from Word2VecUtility import Word2VecUtility
import pandas as pd
import numpy as np
from nltk.corpus import stopwords #for stop words

train = pd.read_csv('dataset/Restaurants_training_set.txt', header=0, delimiter="\t", quoting=3)
test = pd.read_csv('dataset/Restaurants_testing_set.txt', header=0, delimiter="\t", quoting=3 )

# print 'The first review id is:'
# print train["review_id"][0]
# print 'The first review is'
# print train["review"][0]
# print 'The first review star is'
# print train["stars"][0]

# print 'Download text data sets. If you already have NLTK datasets downloaded, just close the Python download window...'
# nltk.download()  # Download text data sets, including stop words

# # Initialize an empty list to hold the clean reviews
clean_train_reviews = []

# # Loop over each review
print "Cleaning and parsing the training set reviews...\n"

num_reviews = len(train["review"])
for i in xrange( 0, num_reviews):
    if( (i+1)%10000 == 0 ):
        print "Processing review %d out of %d" % ( i+1, num_reviews ) 
    clean_train_reviews.append(" ".join(Word2VecUtility.review_to_wordlist(train["review"][i], True)))


# ****** Create a bag of words from the training set
print "Creating the bag of words...\n"


# Initialize the "CountVectorizer" object, which is scikit-learn's
# bag of words tool.
vectorizer = CountVectorizer(analyzer = "word",   \
                         tokenizer = None,    \
                         preprocessor = None, \
                         stop_words = None,   \
                         max_features = 5000) # limit the most frequent 5000 words

# fit_transform() does two functions: First, it fits the model
# and learns the vocabulary; second, it transforms our training data
# into feature vectors. The input to fit_transform should be a list of
# strings.
train_data_features = vectorizer.fit_transform(clean_train_reviews)

# Numpy arrays are easy to work with, so convert the result to an
# array
train_data_features = train_data_features.toarray()
print 'The feature sizes is '
print train_data_features.shape

# ======== Take a look at the 5000 words ========
# vocab = vectorizer.get_feature_names()
# print vocab

# Sum up the counts of each vocabulary word
# dist = np.sum(train_data_features, axis=0)

# For each, print the vocabulary word and the number of times it 
# appears in the training set
# for tag, count in zip(vocab, dist):
    # print count, tag
# ==============================================

# ******* Train a random forest using the bag of words
print "\nTraining the random forest (this may take a while)..."


# Initialize a Random Forest classifier with 100 trees
forest = RandomForestClassifier(n_estimators = 100)

# Fit the forest to the training set, using the bag of words as features and the stars labels as answer
#
# This may take a few minutes to run
forest = forest.fit( train_data_features, train["stars"] )


# ********** Create an empty list and append the clean reviews one by one *******
clean_test_reviews = []
num_test_reviews = len(test["review"])

print "Cleaning and parsing the test set reviews...\n"
for i in xrange(0,num_test_reviews):
    if( (i+1) % 10000 == 0 ):
        print "Review %d of %d" % (i+1, num_test_reviews)    
    clean_test_reviews.append(" ".join(Word2VecUtility.review_to_wordlist(test["review"][i], True)))

# Get a bag of words for the test set, and convert to a numpy array
test_data_features = vectorizer.transform(clean_test_reviews)
test_data_features = test_data_features.toarray()

# Use the random forest to make sentiment label predictions
print "Predicting test labels...\n"
pred_results = forest.predict(test_data_features)

accuracy = Word2VecUtility.compare_prediction(pred_results, test['stars'])



# # Copy the results to a pandas dataframe with an "id" column and
# # a "sentiment" column
# output = pd.DataFrame( data={"id":test["id"], "sentiment":result} )

# # Use pandas to write the comma-separated output file
# output.to_csv(os.path.join(os.path.dirname(__file__), 'data', 'Bag_of_Words_model.csv'), index=False, quoting=3)
# print "Wrote results to Bag_of_Words_model.csv"