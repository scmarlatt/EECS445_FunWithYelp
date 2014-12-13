import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model, svm

def lin_reg(train_x, train_t):

	regr = linear_model.LinearRegression()
	regr.fit(train_x, train_t)
	return regr

def test_and_print_regression(test_x, test_t, regr):

	test_size = test_t.shape[0]

	predictions = regr.predict(test_x)

	rounded_predictions = [round(pred, 0) for pred in predictions]

	num_correct = 0
	value = 0
	for i in range(test_size):
		temp = predictions[i]
		if temp > 5.0:
			temp = 5.0
		if temp < 1.0:
			temp = 1.0
		value += abs(temp - test_t[i])
		if rounded_predictions[i] == test_t[i]:
			num_correct += 1

	print value/test_size #avg error
	print num_correct/test_size #accuracy