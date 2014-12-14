import json

import re
class pairs():
  def __init__(self, word, star):
    self.word = word
    self.star = star
class bigrams():
  def __init__(self, word1,word2):
    self.word1 = word1
    self.word2 = word2

def parse_most_info(infile, num_words, star_param):
  count = 0
  word_data = []
  f = open(infile)
  for line in f:
    words =  re.sub(' +', ' ', line).split()
    word = words[0]
    star = words[3]
    if star == star_param  and count < num_words:
      word_data.append(word)
      count += 1 
  return  word_data

def parse_bigrams(infile, num_bigrams, star_param):
  f = open(infile)
  bigram_data = []
  count = 0
  for line in f:
    words =  re.sub(' +', ' ', line).split()
    word1 = words[0][3:-2]
    word2 = words[1][2:-2]
    star = words[4]
    if star == star_param and count < num_bigrams:
      data = bigrams(word1, word2)
      bigram_data.append(data)
      count += 1

  return bigram_data

def build_features(naive_classifier, review_words, most_common_words, words_one, words_five, bigrams_one, bigrams_five):

  # Feature vector format: [count_most_info_one_words, count_most_info_five_words, 
  #                         count_one_bigrams, count_five_bigrams, 
  #                         prob_one, prob_two, prob_three, prob_four, prob_five, 
  #                         count_common_one_words, count_common_two_words, count_common_three_words, 
  #                         count_common_four_words, count_common_five_words]
 
  one_word_count = 0
  five_word_count = 0
  one_bigram_count = 0
  five_bigram_count = 0

  total_ones_prob = 65911.0 / 780502
  total_twos_prob = 75818.0 / 780502
  total_threes_prob = 121182.0 / 780502
  total_fours_prob = 254632.0 / 780502
  total_fives_prob = 262959.0 / 780502

  feature_matrix = []
   
  for i in range(0, len(review_words)):
    word = review_words[i]
    if word in words_one:
      one_word_count += 1
    elif word in words_five:
      five_word_count += 1

    if i == len(review_words) - 1:
      break
  
    next_word = review_words[i+1]
    for elt in bigrams_one:
      if (elt.word1 == word and elt.word2 == next_word) or (elt.word1 == next_word and elt.word2 == word):
        one_bigram_count += 1
        break
    for elt in bigrams_five:
      if (elt.word1 == word and elt.word2 == next_word) or (elt.word1 == next_word and elt.word2 == word):
        five_bigram_count += 1
        break
   
  # Add info about most informative words and bigrams
  feature_matrix.append(float(one_word_count))
  feature_matrix.append(float(five_word_count))
  feature_matrix.append(float(one_bigram_count))
  feature_matrix.append(float(five_bigram_count))
  
  # Add info about probabilites
  probs = naive_classifier.prob_classify({word: True for word in review_words}) 

  feature_matrix.append(probs.prob(1) * total_ones_prob)
  feature_matrix.append(probs.prob(2) * total_twos_prob)
  feature_matrix.append(probs.prob(3) * total_threes_prob)
  feature_matrix.append(probs.prob(4) * total_fours_prob)
  feature_matrix.append(probs.prob(5) * total_fives_prob)
  
  feature_matrix.append(probs.prob(1))
  feature_matrix.append(probs.prob(2))
  feature_matrix.append(probs.prob(3))
  feature_matrix.append(probs.prob(4))
  feature_matrix.append(probs.prob(5))

  one_word_count = 0
  two_word_count = 0
  three_word_count = 0
  four_word_count = 0
  five_word_count = 0
  for word in review_words:
    if word in most_common_words[1]:
      one_word_count += 1
    if word in most_common_words[2]:
      two_word_count += 1
    if word in most_common_words[3]:
      three_word_count += 1
    if word in most_common_words[4]:
      four_word_count += 1
    if word in most_common_words[5]:
      five_word_count += 1

  feature_matrix.append(float(one_word_count))
  feature_matrix.append(float(two_word_count))
  feature_matrix.append(float(three_word_count))
  feature_matrix.append(float(four_word_count))
  feature_matrix.append(float(five_word_count))
  feature_matrix.append(len(review_words))
  
  return feature_matrix



