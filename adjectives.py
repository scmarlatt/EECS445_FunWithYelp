import nltk
import nltk.classify
import sys

def get_adjectives(reviews):
	one_star = {}
	for review in reviews[1]:
                try:
                    pos_assign = nltk.pos_tag(review)
                except:
                    continue
                for assignment in pos_assign:
			if assignment[1]=='JJ':
				if assignment[0] in one_star:
				    one_star[assignment[0]] += 1
                                else:
                                    one_star[assignment[0]] = 1
	return one_star
