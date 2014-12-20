import read_reviews
import general_regression
import naive_bayes
import extract_features
import common_words_by_star
import numpy as np
import svm_classify
import svm_regression
import adjectives
import verbs
import string
from sklearn import tree

def main():

    reviews = read_reviews.read_useful(1700)
    # reviews[1] is a list of all 15000 rfone star reviews

    print "Getting common words"
    star_mcw_lists = common_words_by_star.get_common_words(reviews, 500)
    # star_mcw_list[1] is a list of most common 1 star words

    # print "Getting common adjectives"
    mc_adj_list = adjectives.get_mc_adj("POS/adj_list1.txt", "POS/adj_list2.txt", "POS/adj_list3.txt", "POS/adj_list4.txt", "POS/adj_list5.txt", 15)   
    mc_vb_list = verbs.get_mc_vb("POS/verb_list1.txt", "POS/verb_list2.txt", "POS/verb_list3.txt", "POS/verb_list4.txt", "POS/verb_list5.txt", 15)
    #print mc_adj_list
    #print mc_vb_list

    print "Training naive bayes classifier"
    nb_num_train = 1500
    nb_classifier = naive_bayes.create_classifier(reviews, nb_num_train)
    #nb_classifier.show_most_informative_features(1000)


    print "Parsing most informative words and bigrams"
    words_one = extract_features.parse_most_info('features_text/most_informative_words_useful.txt', 500, "1")
    words_five = extract_features.parse_most_info('features_text/most_informative_words_useful.txt', 500, "5")
    bigrams_one = extract_features.parse_bigrams('features_text/most_informative_bigrams_useful.txt', 1000, "1")
    bigrams_five = extract_features.parse_bigrams('features_text/most_informative_bigrams_useful.txt', 1000, "5")

    print "Creating feature vectors"
    train_features = []
    train_targets = []
    test_features = []
    test_targets = []
    for i in [1,2,3,4,5]:
        for review in reviews[i][:1500]:
          train_features.append(extract_features.build_features(nb_classifier, review, star_mcw_lists, words_one, words_five, bigrams_one, bigrams_five, mc_adj_list, mc_vb_list))
          train_targets.append(i)
        for review in reviews[i][1500:1700]:
          test_features.append(extract_features.build_features(nb_classifier, review, star_mcw_lists, words_one, words_five, bigrams_one, bigrams_five, mc_adj_list, mc_vb_list))
          test_targets.append(i)


    train_x = np.array(train_features)
    train_t = np.array(train_targets)
    test_x = np.array(test_features)
    test_t = np.array(test_targets)

    print "Running linear regression training"
    regr = general_regression.lin_reg(train_x, train_t)

    print "Testing regression"
    general_regression.test_and_print_regression(test_x, test_t, regr)

    print "Running SVM classifier"
    svm_model = svm_classify.classify(train_x, train_t)

    print "Testing SVM classifier"
    svm_classify.test_and_print_svm(test_x, test_t, svm_model)

    print "Running SVM regression"
    svm_reg_model = svm_regression.regression(train_x, train_t)

    print "Testing SVM regression"
    svm_regression.test_and_print_svm_regression(test_x, test_t, svm_reg_model)
    
    print "Running Decision Tree"
    clf = tree.DecisionTreeClassifier()
    decision_tree_model = clf.fit(train_x, train_t)
    general_regression.test_and_print_regression(test_x, test_t, decision_tree_model)


    stopwords = []
    with open("features_text/stopwords.txt") as s:
        for line in s:
            stopwords.append(s)

    while True:
        review = raw_input('Enter Review: ')
        if review:
            r = unicode(review.lower())
            r = r.replace("couldn't ", "not")
            r = r.replace("wouldn't ", "not")
            r = r.replace("aren't ", "not")
            r = r.replace("can't ", "not")
            r = r.replace("didn't ", "not")
            r = r.replace("doesn't ", "not")
            r = r.replace("don't ", "not")
            r = r.replace("hadn't ", "not")
            r = r.replace("hasn't ", "not")
            r = r.replace("haven't ", "not")
            r = r.replace("isn't ", "not")
            r = r.replace("mustn't ", "not")
            r = r.replace("shouldn't ", "not")
            r = r.replace("won't ", "not")
            r = r.replace("not ", "not")
            r = r.replace("couldnt ", "not")
            r = r.replace("wouldnt ", "not")
            r = r.replace("arent ", "not")
            r = r.replace("cant ", "not")
            r = r.replace("didnt ", "not")
            r = r.replace("doesnt ", "not")
            r = r.replace("dont ", "not")
            r = r.replace("hadnt ", "not")
            r = r.replace("hasnt ", "not")
            r = r.replace("havent ", "not")
            r = r.replace("isnt ", "not")
            r = r.replace("mustnt ", "not")
            r = r.replace("shouldnt ", "not")
            r = r.replace("wont ", "not")
      
            
            remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)     
            review = r.translate(remove_punctuation_map)
            review = [r for r in review.split() if r not in stopwords]
            features = {}
    
            print "---------------------------"   
            print "Naive Bayes Probabilities"
            for r in review:
              features[r] = True
            probs = nb_classifier.prob_classify(features)
            for i in [1,2,3,4,5]:
              print str(i) + " Star Probability: " + str(probs.prob(i))
            
            featureVector = np.array([extract_features.build_features(nb_classifier, review, star_mcw_lists, words_one, words_five, bigrams_one, bigrams_five, mc_adj_list, mc_vb_list)])
            print "---------------------------"
            print "Linear Regression"             
            print regr.predict(featureVector)[0]            
            print "---------------------------"
            print "SVM Classification"
            print svm_model.predict(featureVector)[0]
            print "---------------------------"
            print "SVM Regression"
            print svm_reg_model.predict(featureVector)[0]
            print "---------------------------"
            print "Decision Tree"
            print decision_tree_model.predict(featureVector)[0]
            print "---------------------------"
            print "\n\n"


if __name__ == "__main__":
    main()
