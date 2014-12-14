import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model, svm

def regression(train_x, train_t):

	svm_reg_model = svm.SVR(kernel='rbf')
	svm_reg_model.fit(train_x, train_t)
	return svm_reg_model

def test_and_print_svm_regression(test_x, test_t, svm):

	test_size = len(test_t) 

	predictions = svm.predict(test_x)

	rounded_predictions = [round(pred, 0) for pred in predictions]

	num_correct = 0
	value = 0
	for i in range(test_size):
		temp = rounded_predictions[i]
		if temp > 5.0:
			temp = 5.0
		if temp < 1.0:
			temp = 1.0
		value += abs(temp - test_t[i])
		if rounded_predictions[i] == test_t[i]:
			num_correct += 1

	# print value/test_size #avg error
	print "Average  Error: " + str(value/test_size) #avg error
	print "Accuracy: " + str(float(num_correct)/test_size) #accuracy
