import json
from nltk.stem.porter import *
from nltk.stem.snowball import SnowballStemmer

def main():
	punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
	f = open('reviews_10k.json', 'r')
	clean_review = ""
	q = open('stopwords.txt')
	stopwords = []
	restraunts = open('restaurant_ids.txt')
	ids = []
	for word in restraunts:
		ids.append(word)
	stemmer = SnowballStemmer("english")
	for word in stopwords:
		stopwords.append(word)

	for line in f:
		rec = json.loads(line.strip())
		r = rec["text"].lower()
		for char in r:
			if char not in punctuations:
				clean_review = clean_review + char

		arr = clean_review.split(" ")
		for i in range(0, len(arr)):
			if arr[i] in stopwords:
				arr[i] = ""
			else:
		 		arr[i] = stemmer.stem(arr[i])

		final = ' '.join(arr)

		if rec["votes"]["useful"] > 5 and (rec["business_id"] in ids):
			print final

if __name__ == "__main__":
  main()


