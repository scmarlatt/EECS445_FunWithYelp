import json
import string
import regex as re
import nltk
import nltk.classify

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


def common_words_by_stars():
    # Number of reviews to process
    num_reviews_to_process = 200000
    #------------------------------

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
        train_reviews_by_star[r[1]].extend([word for word in r[0].lower().split() if word not in stopwords])
    for key in train_reviews_by_star:
        fdist = FreqDist(train_reviews_by_star[key])
        print "---------------Most Common " + str(key) + " Star Words --------------"
        print fdist.most_common(100)

def naive_bayes():
    # Number of reviews to process
    num_reviews_to_process = 10000 
    #------------------------------

    stopwords = load_stop_words()

    first_reviews = read_n_reviews(num_reviews_to_process, "yelp_academic_dataset_review.json")
    train_reviews_by_star = {1:[], 2:[], 3:[], 4:[], 5:[]}
    test_reviews_by_star = {1:[], 2:[], 3:[], 4:[], 5:[]}


    for idx, r in enumerate(first_reviews):
        if idx % 5 == 0:
          test_reviews_by_star[r[1]].append([word for word in r[0].lower().split() if word not in stopwords])
        else:
          train_reviews_by_star[r[1]].append([word for word in r[0].lower().split() if word not in stopwords])


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
      print classifier.classify_many(test_set[i]).count(str(i))/float(len(test_set[i]))

def run():
    naive_bayes()

if __name__ == "__main__":
    run()
