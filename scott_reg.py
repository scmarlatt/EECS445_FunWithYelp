import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
import nltk
import json
import string
import nltk
import sys



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
	total_review_list_5 = []
	total_review_list_4 = []
	total_review_list_3 = []
	total_review_list_2 = []
	total_review_list_1 = []

	first_reviews = read_n_reviews(num_reviews_to_process, "reviews_sample.json")

	for review in first_reviews:
		for word in review[0]:
			if review[1] == 5:
				total_review_list_5.append(word)
			elif review[1] == 4:
				total_review_list_4.append(word)
			elif review[1] == 3:
				total_review_list_3.append(word)
			elif review[1] == 2:
				total_review_list_2.append(word)
			else:
				total_review_list_1.append(word)
	fdist5 = nltk.FreqDist(total_review_list_5)
	fdist4 = nltk.FreqDist(total_review_list_4)
	fdist3 = nltk.FreqDist(total_review_list_3)
	fdist2 = nltk.FreqDist(total_review_list_2)
	fdist1 = nltk.FreqDist(total_review_list_1)
	most_common_words_list = []
	most_common_words_list.append(fdist1.most_common(99))
	most_common_words_list.append(fdist2.most_common(99))
	most_common_words_list.append(fdist3.most_common(99))
	most_common_words_list.append(fdist4.most_common(99))
	most_common_words_list.append(fdist5.most_common(99))


	return most_common_words_list


def run():

	num_reviews = 600
	num_features = 6
	num_test_reviews = 400

	#get n by m for training
	#get n by m for testing
	train_x = np.zeros((num_reviews, num_features))
	train_t = np.zeros((num_reviews,1))
	test_x = np.zeros((num_test_reviews, num_features))
	test_t = np.zeros((num_test_reviews,1))

	all_reviews = read_n_reviews(1000, "reviews_sample.json")
	training_set = all_reviews[0:600]
	testing_set = all_reviews[600:1000]
	most_common_words = common_words()
	#print most_common_words
	#iterate over most common words
	for n, review in enumerate(training_set):
		train_t[n] = review[1]
		for num_stars in range(5):
			for m, pair in enumerate(most_common_words[num_stars]):
				word = pair[0]
				for k in review[0]:
					if word == k:
						train_x[n][num_stars + 1] += 1

	for n, review in enumerate(testing_set):
		test_t[n] = review[1]
		for num_stars in range(5):
			for m, pair in enumerate(most_common_words[num_stars]):
				word = pair[0]
				for k in review[0]:
					if word == k:
						test_x[n][num_stars + 1] += 1




	regr = linear_model.LinearRegression()
	regr.fit(train_x, train_t)

	predictions = regr.predict(test_x)

	#print predictions
	rounded_predictions = [round(pred, 0) for pred in predictions]

	#print rounded_predictions
	num_correct = 0
	for i in range(400):
		#value = abs(rounded_predictions[i]  test_t[i][0])
		if rounded_predictions[i] == test_t[i][0]:
			num_correct += 1

	print num_correct/400.0


if __name__ == "__main__":
	run()