import nltk
import nltk.classify
import sys


def find_bigrams(review):
	return zip(review, review[1:])

def read_star_reviews(infile, n):
	with open(infile) as review_input:
		return [next(review_input).split() for i in range(n)]

def build_test_set(reviews, num_train):
	test_set = {1:[], 2:[], 3:[], 4:[], 5:[]}
	for i in [1,2,3,4,5]:
		test_set[i].extend([{word: True for word in review} for review in reviews[i][num_train:]])
		# test_set[i].extend([{word: True for word in qfind_bigrams(review)} for review in reviews[i][num_train:]])
	return test_set

def print_accuracies(classifier, test_set):
	for i in [1,2,3,4,5]:
		data = classifier.classify_many(test_set[i])
		print str(i) + " Star"
		print "------------"
		print "Accuracy -> " + str(data.count(i)/float(len(test_set[i])))
		print "Average result rating -> " + str(sum([int(d) for d in data])/float(len(data)))
		print "\n"

def output_prob_dist(classifier, test_set, outfile):
	with open(outfile, 'w') as probs_output:
		for i in [1,2,3,4,5]:
			data = classifier.prob_classify_many(test_set[i])
			for probs in data:
				probs_output.write(str(i))
				for r in [1,2,3,4,5]:
					probs_output.write(" " + str(probs.prob(r)))
				probs_output.write("\n")
				


def naive_bayes():
	reviews = {}

	num_each_review = 13000
	num_train = 12000

	reviews[1] = read_star_reviews("star_texts/one_stars.txt", num_each_review)
	reviews[2] = read_star_reviews("star_texts/two_stars.txt", num_each_review)
	reviews[3] = read_star_reviews("star_texts/three_stars.txt", num_each_review)
	reviews[4] = read_star_reviews("star_texts/four_stars.txt", num_each_review)
	reviews[5] = read_star_reviews("star_texts/five_stars.txt", num_each_review)

	train_set = []
	for i in [1,2,3,4,5]:
		train_set.extend([({word: True for word in review}, i) for review in reviews[i][:num_train]])
		# train_set.extend([({word: True for word in find_bigrams(review)}, i) for review in reviews[i][:num_train]])

	test_set = build_test_set(reviews, num_train)

	classifier = nltk.classify.NaiveBayesClassifier.train(train_set)
	print classifier.show_most_informative_features(100)
	# print_accuracies(classifier, test_set)
	output_prob_dist(classifier, test_set, "nbtrain.txt")
	return classifier


def run():
	classifier = naive_bayes()
	while True:
		review = raw_input('Enter Review: ').split()
		if review:
			features = {}
			for r in review:
				features[r] = True
			probs = classifier.prob_classify(features)
			for i in [1,2,3,4,5]:
				print str(i) + " Star Probability: " + str(probs.prob(i))
			print "-----------------"


if __name__ == "__main__":
	run()
