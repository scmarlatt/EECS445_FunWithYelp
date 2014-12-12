import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
import nltk
import string
import nltk
import sys

def run():
	inputfile = open('nbvalues.txt')

	num_reviews = 4000
	num_features = 6
	num_test_reviews = 1000

	#get n by m for training
	#get n by m for testing
	train_x = np.zeros((num_reviews, num_features))
	train_t = np.zeros((num_reviews,1))
	test_x = np.zeros((num_test_reviews, num_features))
	test_t = np.zeros((num_test_reviews,1))

	for n, line in enumerate(inputfile):
		this_line = line.split()
		if n % 5 != 0:
			train_t[n] = this_line[0]
			for x in range(1,6):
				train_x[x] = this_line[x]
		else:
			test_t[n] = this_line[0]
			for x in range(1,6):
				test_x[x] = this_line[x]

	regr = linear_model.LinearRegression()
	regr.fit(train_x, train_t)

	predictions = regr.predict(test_x)
	rounded_predictions = [round(pred, 0) for pred in predictions]

	num_correct = 0
	value = 0
	for i in range(2000):
		temp = predictions[i]
		if temp > 5.0:
			temp = 5.0
		if temp < 1.0:
			temp = 1.0
		value += abs(temp - test_t[i][0])
		if rounded_predictions[i] == test_t[i][0]:
			num_correct += 1

	print value/2000.0 #avg error
	print num_correct/2000.0 #accuracy


if __name__ == "__main__":
	run()