import general_regression
import read_reviews


def main():

	reviews = read_reviews.read(10000)

	#load into feature matrix

	#regr = general_regression.lin_reg(train_x, train_t)

	#general_regression.test_and_print_regression(test_x, test_t, regr)


if __name__ == "__main__":
	main()