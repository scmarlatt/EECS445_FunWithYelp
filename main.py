import general_regression
import read_reviews
import naive_bayes
import extract_features
def main():


 
	reviews = read_reviews.read(15000)
  # reviews[1] is a list of all 15000 rfone star reviews


	nb_num_train = 8000
	nb_classifier = naive_bayes.create_classifier(reviews, nb_num_train)	
	print nb_classifier.show_most_informative_features(100)
	nb_test = naive_bayes.build_test_set(reviews, nb_num_train)
	naive_bayes.print_accuracies(nb_classifier, nb_test)

  # to find the pdist for a review
  #   probs =  nb_classifier.prob_classify(review)
  #   one_star_probability = probs.prob(1)

	#load into feature matrix

	#regr =ression.lin_reg(train_x, train_t)

	#general_regression.test_and_print_regression(test_x, test_t, regr)


if __name__ == "__main__":
	main()
