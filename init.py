import json
import string
import regex as re
import nltk
import nltk.classify
import sys


def find_ngrams(input_list, n):
  return zip(*[input_list[i:] for i in range(n)])

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
    reviewWords = [r for r in review[0].translate(remove_punctuation_map).lower().split() if r not in stopwords]
    reviewBigrams = find_ngrams(reviewWords, 2)
    return [review[1], reviewWords, reviewBigrams]



def read_n_reviews(n, infile):
    stopwords = load_stop_words();
    with open(infile) as data:
        reviews_json = []
        for i in range(100000):
          next(data)
        for i in range(n):
          reviews_json.append(next(data))
          for i in range(10):
            next(data)
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
    num_reviews_to_process = 4000
    #------------------------------

    first_reviews = read_n_reviews(num_reviews_to_process, "yelp_academic_dataset_review.json")

    train_reviews_by_star_counts = {1:0, 2:0, 3:0, 4:0, 5:0}
    test_reviews_by_star = {1:[], 2:[], 3:[], 4:[], 5:[]}

    train_set = []
    test_set = {1:[], 2:[], 3:[], 4:[], 5:[]}

    for idx, r in enumerate(first_reviews):
      if idx % 10 == 0:
        features = {} 
        for word in r[1]:
           features[word] = True
        for bigram in r[2]:
            features[bigram] = True  
        test_set[r[0]].append(features)
      else:
        if(train_reviews_by_star_counts[r[0]] < 600):
          train_reviews_by_star_counts[r[0]] += 1
          features = {} 
          for word in r[1]:
            features[word] = True
          for bigram in r[2]:
            features[bigram] = True      
          train_set.append((features, str(r[0])))


    #-----Implementing Naive Bayes--------
    
    classifier = nltk.classify.NaiveBayesClassifier.train(train_set)
    print classifier.show_most_informative_features(100)
    
    # ranges = {
    #     1:[0, .05],
    #     2:[.05, .4],
    #     3:[.4, .65],
    #     4:[.65, .95],
    #     5:[.95, 1],
    # }
    # predictions = {1:[], 2:[], 3:[], 4:[], 5:[]}
    # for rating in [1,2,3,4,5]:
    #   pdata = classifier.prob_classify_many(test_set[rating])
    #   for pdist in pdata:
    #     prob = pdist.prob('5')
    #     for k in [1,2,3,4,5]:
    #       if ranges[k][0] <= prob < ranges[k][1]:
    #         predictions[rating].append(k)
    #         break;
    #   print "Accuracy -> " + str(predictions[rating].count(rating)/float(len(test_set[rating])))
    #   print "Average result rating -> " + str(sum([int(d) for d in predictions[rating]])/float(len(predictions[rating])))


    for i in [1,2,3,4,5]:
      data = classifier.classify_many(test_set[i])
      print str(i) + " Star"
      print "------------"
      print "Accuracy -> " + str(data.count(str(i))/float(len(test_set[i])))
      print "Average result rating -> " + str(sum([int(d) for d in data])/float(len(data)))
      print "\n"

    return classifier

def run():
    classifier = naive_bayes()
    # while True:
    #   review  = sys.stdin.read(1)
    #   if review:
    #     features = {}
    #     for r in review.split():
    #       features[r] = True
    #     print classifier.classify(features)


if __name__ == "__main__":
    run()
