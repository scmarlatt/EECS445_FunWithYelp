import nltk
import nltk.classify
import sys

def get_adjectives(reviews):
	one_star = {}
	for review in reviews[1]:
		pos_assign = nltk.pos_tag(review)
		for assignment in pos_assign:
			if assignment[1]=='JJ':
				if assignment[0] in one_star:
					one_star[assignment[0]] += 1
				one_star[assignment[0]] = 1
	return one_star