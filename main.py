import general_regression
import read_reviews
import naive_bayes
import extract_features
import common_words_by_star

def main():


 
	reviews = read_reviews.read(1000)
  # reviews[1] is a list of all 15000 rfone star reviews

	star_mcw_lists = common_words_by_star.get_common_words(reviews, 50)
	# star_mcw_list[1] is a list of most common 1 star words

	nb_num_train = 500
	nb_classifier = naive_bayes.create_classifier(reviews, nb_num_train)	
	
	words_one = extract_features.parse_most_info('features_text/most_informative_1_to_5.txt', 1000, "1")
	words_five = extract_features.parse_most_info('features_text/most_informative_1_to_5.txt', 1000, "5")
	bigrams_one = extract_features.parse_bigrams('features_text/bigrams.txt', 1000, "1")
	bigrams_five = extract_features.parse_bigrams('features_text/bigrams.txt', 1000, "5")

	features = []
	for i in [1,2,3,4,5]:
		for review in reviews[i]:
			features.append(extract_features.build_features(nb_classifier, review, star_mcw_lists[i], words_one, words_five, bigrams_one, bigrams_five))

	print features[0]



	#print nb_classifier.show_most_informative_features(100)
	#nb_test = naive_bayes.build_test_set(reviews, nb_num_train)
	#naive_bayes.print_accuracies(nb_classifier, nb_test)

  # to find the pdist for a review
  #   probs =  nb_classifier.prob_classify(review)
  #   one_star_probability = probs.prob(1)

	#load into feature matrix

	#regr =ression.lin_reg(train_x, train_t)

	#general_regression.test_and_print_regression(test_x, test_t, regr)


if __name__ == "__main__":
	main()
