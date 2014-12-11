import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
import nltk
import json
import string
import regex as re
import nltk
import sys

def build_sample_file(reviews_json):
    with open("../reviews_sample.json","w") as output:
        for r in reviews_json:
            output.write(r) 

def format_review(review, stopwords):
    review[0].replace(" not ", " not");
    review[0].replace(" no ", " no");
    review[0].replace(" didn't ", " didn't");
    review[0].replace(" can't ", " can't");
    remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
    return [[r for r in review[0].translate(remove_punctuation_map).lower().split() if r not in stopwords], review[1]]
  

def read_n_reviews(n, infile):
    stopwords = load_stop_words();
    with open(infile) as data:
        reviews_json = [next(data) for i in range(n)]
    reviews = [[json.loads(review)["text"], json.loads(review)["stars"]] for review in reviews_json]
    
    return [format_review(review, stopwords) for review in reviews]

#def format_word(word):
 #   for suffix in ["tion", "ing", "ed", "ious", "ed", "ies", "ive", "es", "s", "ment", "y", "ate", "able"]:
  #      if word.endswith(suffix):
   #         return word[:-len(suffix)]
    #return word

def load_stop_words():
    with open("stopwords.txt") as stopwords:
        return stopwords.read().splitlines()


def common_words():
    # Number of reviews to process
    num_reviews_to_process = 1000
    stopwords = load_stop_words()

    first_reviews = read_n_reviews(num_reviews_to_process, "../reviews_sample.json")

    for r in first_reviews:
        total_review_string += r[0]
    fdist = FreqDist(total_review_string)
    print "---------------Most Common Words --------------"
    print fdist.most_common(30)


def run():

	n = 1000
	m = 30
	load_stop_words()
	training_set = read_n_reviews(1000, "../reviews_sample.json")
	for i in training_set
		for j in range(0, m)
			text = training_set[0]
			for k in text
				if fdist.most_common(k)
					train_x[j] = 1
    #get n by m for training
    #get n by m for testing
    train_x = zeros((n,m))
    train_t = zeros((n,m))
    test_x = zeros((n,m))
    train_t = zeros((n,m))

    regr = linear_model.LinearRegression()
    regr.fit(train_x, train_t)



if __name__ == "__main__":
    run()