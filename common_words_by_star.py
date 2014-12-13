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
