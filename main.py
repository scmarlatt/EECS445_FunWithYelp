import read_reviews
# import general_regression
# import naive_bayes
# import extract_features
# import common_words_by_star
# import numpy as np
# import svm_classify
# import svm_regression
import adjectives
import verbs

def main():


 
    reviews = read_reviews.read(100)
    # reviews[1] is a list of all 15000 rfone star reviews
    
    adjectives.write_adjectives(reviews)
    verbs.write_verbs(reviews)   

    #  	print "Getting common words"
	# star_mcw_lists = common_words_by_star.get_common_words(reviews, 50)
	# # star_mcw_list[1] is a list of most common 1 star words

	# print "Training naive bayes classifier"
	# nb_num_train = 4000
	# nb_classifier = naive_bayes.create_classifier(reviews, nb_num_train)	

	# print "Parsing most informative words and bigrams"
	# words_one = extract_features.parse_most_info('features_text/most_informative_1_to_5.txt', 1000, "1")
	# words_five = extract_features.parse_most_info('features_text/most_informative_1_to_5.txt', 1000, "5")
	# bigrams_one = extract_features.parse_bigrams('features_text/bigrams.txt', 1000, "1")
	# bigrams_five = extract_features.parse_bigrams('features_text/bigrams.txt', 1000, "5")

	# print "Creating feature vectors"
	# train_features = []
	# train_targets = []
	# test_features = []
	# test_targets = []
	# for i in [1,2,3,4,5]:
	# 	for review in reviews[i][:4000]:
	# 		train_features.append(extract_features.build_features(nb_classifier, review, star_mcw_lists[i], words_one, words_five, bigrams_one, bigrams_five))
	# 		train_targets.append(i)
	# 	for review in reviews[i][4000:]:
	# 		test_features.append(extract_features.build_features(nb_classifier, review, star_mcw_lists[i], words_one, words_five, bigrams_one, bigrams_five))
	# 		test_targets.append(i)

	# train_x = np.array(train_features)
	# train_t = np.array(train_targets)
	# test_x = np.array(test_features)
	# test_t = np.array(test_targets)

	# #print nb_classifier.show_most_informative_features(100)
	# #nb_test = naive_bayes.build_test_set(reviews, nb_num_train)
	# #naive_bayes.print_accuracies(nb_classifier, nb_test)

 #  # to find the pdist for a review
 #  #   probs =  nb_classifier.prob_classify(review)
 #  #   one_star_probability = probs.prob(1)

	# #load into feature matrix

	# print "Running linear regression training"
	# regr = general_regression.lin_reg(train_x, train_t)

	# print "Testing regression"
	# general_regression.test_and_print_regression(test_x, test_t, regr)

	# print "Running SVM classifier"
	# svm_model = svm_classify.classify(train_x, train_t)

	# print "Testing SVM classifier"
	# svm_classify.test_and_print_svm(test_x, test_t, svm_model)

	# print "Running SVM regression"
	# svm_reg_model = svm_regression.regression(train_x, train_t)

	# print "Testing SVM regression"
	# svm_regression.test_and_print_svm_regression(test_x, test_t, svm_reg_model)



if __name__ == "__main__":
	main()
