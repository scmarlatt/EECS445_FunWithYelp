import json
import string
import regex as re
import nltk
import nltk.classify
import sys

def build_sample_file(reviews_json):
    with open("reviews_sample.json","w") as output:
        for r in reviews_json:
            output.write(r) 

def format_review(review, stopwords):
    review[0].replace(" not ", " not");
    review[0].replace(" no ", " no");
    review[0].replace(" didn't ", " didn't");
    review[0].replace(" can't ", " can't");
    remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
    return [[r for r in review[0].translate(remove_punctuation_map).lower().split() if r not in stopwords], review[1]]
  

def read_n_reviews(n, infile):
    stopwords = load_stop_words();
    with open(infile) as data:
        reviews_json = [next(data) for i in range(n)]
    reviews = [[json.loads(review)["text"], json.loads(review)["stars"]] for review in reviews_json]
    
    return [format_review(review, stopwords) for review in reviews]

def format_word(word):
    for suffix in ["tion", "ing", "ed", "ious", "ed", "ies", "ive", "es", "s", "ment", "y", "ate", "able"]:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word

def load_stop_words():
    with open("stopwords.txt") as stopwords:
        return stopwords.read().splitlines()


def common_words_by_stars():
    # Number of reviews to process
    num_reviews_to_process = 200000
    stopwords = load_stop_words()

    first_reviews = read_n_reviews(num_reviews_to_process, "yelp_academic_dataset_review.json")
    train_reviews_by_star = {
      1:[],
      2:[],
      3:[],
      4:[],
      5:[]
    }

    for r in first_reviews:
        train_reviews_by_star[r[1]].extend(r[0])
    for key in train_reviews_by_star:
        fdist = FreqDist(train_reviews_by_star[key])
        print "---------------Most Common " + str(key) + " Star Words --------------"
        print fdist.most_common(100)

def naive_bayes():
    # Number of reviews to process
    num_reviews_to_process = 5555 
    #------------------------------

    first_reviews = read_n_reviews(num_reviews_to_process, "yelp_academic_dataset_review.json")
    train_reviews_by_star = {1:[], 2:[], 3:[], 4:[], 5:[]}
    test_reviews_by_star = {1:[], 2:[], 3:[], 4:[], 5:[]}


    for idx, r in enumerate(first_reviews):
        if idx % 10 == 0:
          test_reviews_by_star[r[1]].append(r[0])
        else:
          train_reviews_by_star[r[1]].append(r[0])


    #-----Implementing Naive Bayes--------
    train_set = []
    for rating, reviews in train_reviews_by_star.iteritems():
      for r in reviews:
         features = {} 
         for word in r:
             features[word] = True
         train_set.append((features, str(rating)))
    
    test_set = {1:[], 2:[], 3:[], 4:[], 5:[]}
    for rating, reviews in test_reviews_by_star.iteritems():
      for r in reviews:
         features = {} 
         for word in r:
             features[word] = True
         test_set[rating].append((features))
    
    classifier = nltk.classify.NaiveBayesClassifier.train(train_set)
    print classifier.show_most_informative_features(200)

    for i in range(1,6):
      data = classifier.classify_many(test_set[i])
      print str(i) + " Star"
      print "------------"
      print "Accuracy -> " + str(data.count(str(i))/float(len(test_set[i])))
      print "Average result rating -> " + str(sum([int(d) for d in data])/float(len(data)))
      print "\n"

    return classifier

def run():
    classifier = naive_bayes()
    while True:
      review  = sys.stdin.read(1)
      if review:
        features = {}
        for r in review.split():
          features[r] = True
        print classifier.classify(features)


if __name__ == "__main__":
    run()
