def read_star_reviews(infile, n):
	with open(infile) as review_input:
		return [next(review_input).split() for i in range(n)]				

def read(num_each_review):
	reviews = {}
	reviews[1] = read_star_reviews("star_texts/one_stars.txt", num_each_review)
	reviews[2] = read_star_reviews("star_texts/two_stars.txt", num_each_review)
	reviews[3] = read_star_reviews("star_texts/three_stars.txt", num_each_review)
	reviews[4] = read_star_reviews("star_texts/four_stars.txt", num_each_review)
	reviews[5] = read_star_reviews("star_texts/five_stars.txt", num_each_review)

	return reviews