import json
import string
import regex as re
from nltk import *

def build_sample_file(reviews_json):
    with open("reviews_sample.json","w") as output:
        for r in reviews_json:
            output.write(r) 

def read_n_reviews(n, infile):
    with open(infile) as data:
        reviews_json = [next(data) for i in range(n)]
    reviews = [[json.loads(review)["text"], json.loads(review)["stars"]] for review in reviews_json]
    
    # Remove punctuation
    remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
    reviews_without_punctutation = [[review[0].translate(remove_punctuation_map), review[1]] for review in reviews]
    
    return reviews_without_punctutation

def format_word(word):
    for suffix in ["tion", "ing", "ed", "ious", "ed", "ies", "ive", "es", "s", "ment", "y", "ate", "able"]:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word

def load_stop_words():
    with open("stopwords.txt") as stopwords:
        return stopwords.read().splitlines()


def run():

    # Number of reviews to process
    num_reviews_to_process = 20000
    #------------------------------

    stopwords = load_stop_words()

    first_reviews = read_n_reviews(num_reviews_to_process, "yelp_academic_dataset_review.json")
    reviews_by_stars = {
      1:[],
      2:[],
      3:[],
      4:[],
      5:[]
    }

    for r in first_reviews:
        reviews_by_stars[r[1]].extend([format_word(word) for word in r[0].lower().split() if word not in stopwords])
    for key in reviews_by_stars:
      fdist = FreqDist(reviews_by_stars[key])
      print "---------------Most Common " + str(key) + " Star Words --------------"
      print fdist.most_common(100)

if __name__ == "__main__":
    run()
