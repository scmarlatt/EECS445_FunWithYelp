import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model, svm

def classify(train_x, train_t):

	svm_model = svm.SVC(kernel='rbf')
	svm_model.fit(train_x, train_t)
	return svm_model

def test_and_print_svm(test_x, test_t, svm):

	predictions = svm.predict(test_x)

	# rounded_predictions = [round(pred, 0) for pred in predictions]

	num_correct = 0
	value = 0
	for i in range(test_size):
		# temp = predictions[i]
		# if temp > 5.0:
		# 	temp = 5.0
		# if temp < 1.0:
		# 	temp = 1.0
		# value += abs(temp - test_t[i])
		if predictions[i] == test_t[i]:
			num_correct += 1

	# print value/test_size
	print "Accuracy: " + str(float(num_correct)/len(test_t)) #accuracy
