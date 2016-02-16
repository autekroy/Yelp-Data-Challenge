#!/usr/bin/env python

import re # use regular expression to remove non-alphabet
import nltk #for stop words

import pandas as pd
import numpy as np

from nltk.corpus import stopwords


class Word2VecUtility(object):
    """Word2VecUtility is a utility class for processing raw text into segments for further learning"""

    @staticmethod
    def review_to_wordlist( review, remove_stopwords=False ):
        # Function to convert a document to a sequence of words,
        # optionally removing stop words.  Returns a list of words.
        #
        # 1. Remove non-alphabets
        review_text = re.sub("[^a-zA-Z]"," ", review)
        #
        # 2. Convert words to lower case and split them
        words = review_text.lower().split()
        #
        # 3. Optionally remove stop words (false by default)
        if remove_stopwords:
            stops = set(stopwords.words("english"))
            words = [w for w in words if not w in stops]

        return(words)

    # Define a function to split a review into parsed sentences
    @staticmethod
    def review_to_sentences( review, tokenizer, remove_stopwords=False ):
        # Function to split a review into parsed sentences. Returns a
        # list of sentences, where each sentence is a list of words
        #
        # 1. Use the NLTK tokenizer to split the paragraph into sentences
        raw_sentences = tokenizer.tokenize(review.decode('utf8').strip())
        #
        # 2. Loop over each sentence
        sentences = []
        for raw_sentence in raw_sentences:
            # If a sentence is empty, skip it
            if len(raw_sentence) > 0:
                # Otherwise, call review_to_wordlist to get a list of words
                sentences.append( KaggleWord2VecUtility.review_to_wordlist( raw_sentence, \
                  remove_stopwords ))
        #
        # Return the list of sentences (each sentence is a list of words,
        # so this returns a list of lists
        return sentences

    @staticmethod
    def compare_prediction(pred, answer, evaluation = "accuracy"):
        from sklearn.metrics import mean_squared_error
        if len(pred) != len(answer):
            print "the size of prediction are not matched! "
            exit(1)
        
        num_pred = len(pred)
        true_positive = 0        
        for i in xrange(num_pred):
            if pred[i] == answer[i]:
                true_positive += 1
        
        accuracy = float(true_positive)/num_pred
        RMSE = mean_squared_error(answer, pred)**0.5
        
        print '%d out of %d is correct!' % (true_positive, num_pred)
        print 'Accuracy is ', accuracy
        print 'RMSE is ', RMSE
        
        if evaluation == "accuracy":
            return accuracy
        elif evaluation == 'RMSE':
            return RMSE