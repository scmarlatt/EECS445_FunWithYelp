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


def run():
    default_stopwords = ["a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "aren't", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "can't", "cannot", "could", "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't", "down", "during", "each", "few", "for", "from", "further", "had", "hadn't", "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't", "it", "it's", "its", "itself", "let's", "me", "more", "most", "mustn't", "my", "myself", "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other", "ought", "our", "ours    ourselves", "out", "over", "own", "same", "shan't", "she", "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", "we'd", "we'll", "we're", "we've", "were", "weren't", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "won't", "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves"]
    custom_stopwords = []
    stopwords = default_stopwords + custom_stopwords

    first_reviews = read_n_reviews(20000, "yelp_academic_dataset_review.json")
    reviews_by_stars = {
      1:[],
      2:[],
      3:[],
      4:[],
      5:[]
    }


    concat_text = []
    for r in first_reviews:
        reviews_by_stars[r[1]].extend([format_word(word) for word in r[0].lower().split() if word not in stopwords])

    # print "---------------ConcatText--------------"
    # print concat_text
    for key in reviews_by_stars:
      fdist = FreqDist(reviews_by_stars[key])
      print "---------------Most Common " + str(key) + " Star Words --------------"
      print fdist.most_common(100)



if __name__ == "__main__":
    run()
