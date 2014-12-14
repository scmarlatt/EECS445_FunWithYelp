import nltk

def get_common_words(reviews, num_words):
	# reviews[1] is a list of 1 star reviews...
	# Number of reviews to process

	words_in_reviews = {}
	for i in [1,2,3,4,5]:
		words_in_reviews[i] = [word for review in reviews[i] for word in review]

	fdists = {}
	for i in [1,2,3,4,5]:
		fdists[i] = nltk.FreqDist(words_in_reviews[i])
	
	most_common_words_lists = {}
	for i in [1,2,3,4,5]:
		most_common_words_lists[i] = fdists[i].most_common(num_words)

	return most_common_words_lists


def get_nb_probs(textfile):
	for n, line in enumerate(textfile):
		this_line = line.split()
		if n % 5 != 0:
			train_t[n] = this_line[0]
			train_t[train_count] = this_line[0]
			train_count += 1
			for x in range(1,6):
				train_x[x] = this_line[x]
		else:
			test_t[n] = this_line[0]
			test_t[n / 5] = this_line[0]
			for x in range(1,6):
				test_x[x] = this_line[x]