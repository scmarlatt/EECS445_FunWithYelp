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
    if star == star_param and count_ones < num_bigrams:
      data = bigrams(word1, word2)
      bigram_data.append(data)
      count += 1

  return bigram_data

def build_features(prob_distribution, most_info_words, most_info_bigrams, review_string, most_common_words):
  words_one = parse_most_info('features_text/most_informative_1_to_5.txt', 1000, "1")
  words_five = parse_most_info('features_text/most_informative_1_to_5.txt', 1000, "5")
  bigrams_one = parse_bigrams('features_text/bigrams.txt', 1000, "1")
  bigrams_five = parse_bigrams('features_text/bigrams.txt', 1000, "5")
 
  one_word_count = 0
  five_word_count = 0
  one_bigram_count = 0
  five_bigram_count = 0
  review_words = review_string.split()
  
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
   
  



def main():
  parse_most_info('features_text/most_informative_1_to_5.txt', 20, 1)
  #parse_bigrams('bigrams.txt', 20)
if __name__ == "__main__":
  main()
