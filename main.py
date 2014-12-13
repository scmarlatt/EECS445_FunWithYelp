import general_regression
import read_reviews
import naive_bayes

def main():

	reviews = read_reviews.read(10000)



	nb_num_train = 9000
	nb_classifier = naive_bayes.create_classifier(reviews, nb_num_train)	
	#print nb_classifier.show_most_informative_features(100)
	nb_test = naive_bayes.build_test_set(reviews, nb_num_train)
	naive_bayes.print_accuracies(nb_classifier, nb_test)


	#load into feature matrix

	#regr = general_regression.lin_reg(train_x, train_t)

	#general_regression.test_and_print_regression(test_x, test_t, regr)


if __name__ == "__main__":
	main()