import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model, svm

def classify(train_x, train_t):

	svm_model = svm.SVC(kernel='rbf')
	svm_model.fit(train_x, train_t)
	return svm_model

def test_and_print_svm(test_x, test_t, svm):

	predictions = svm.predict(test_x)
	test_size = len(test_t)

	num_correct = 0
	value = 0
	for i in range(test_size):
		if predictions[i] == test_t[i]:
			num_correct += 1

	# print value/test_size
	print "Accuracy: " + str(float(num_correct)/test_size) #accuracy
