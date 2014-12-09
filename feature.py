import json
from pprint import pprint

class pairs:
	def __init__(self):
		self.rating = 0
		self.review = 0

class user_data:
	def __init__(self):
		self.rating = 0
		self.review = 0

def main():
	f = open('reviews_sample.json', 'rb')
	reviews_stars = []
	num_review = 0;
	users = []
	for line in f:
		rec = json.loads(line.strip())
		s = pairs()
		s.rating = rec["stars"]
		s.review = rec["text"]
		u = user_data()
		num_review = num_review+1
		reviews_stars.append(s);
	f.close()

	for pair in reviews_stars:
		#print pair.rating
		#print pair.review

	for user in users


if __name__ == "__main__":
  main()
