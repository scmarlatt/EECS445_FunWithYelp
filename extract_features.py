import json

import re
class pairs():
  def __init__(self, word, star):
    self.word = word
    self.star = star
class bigrams():
  def __init__(self, word1,word2, star):
    self.word1 = word1
    self.word2 = word2
    self.star = star

def parse_most_info(infile, num_words):
  count_ones = 0
  count_fives = 0
  word_data = []
  f = open(infile)
  for line in f:
    words =  re.sub(' +', ' ', line).split()
    word = words[0]
    star = words[3]
    if star == "1" and count_ones < num_words:
      data = pairs(word, star)
      word_data.append(data)
      count_ones += 1
    elif star == "5" and count_fives < num_words:
       data = pairs(word, star)
       word_data.append(data)
       count_fives +=1
  return  word_data

def parse_bigrams(infile, num_bigrams):
  f = open(infile)
  bigram_data = []
  count_ones = 0
  count_fives = 0
  for line in f:
    words =  re.sub(' +', ' ', line).split()
    word1 = words[0][3:-2]
    word2 = words[1][2:-2]
    star = words[4]
    if star == "1" and count_ones < num_bigrams:
      data = bigrams(word1, word2, star)
      bigram_data.append(data)
      count_ones += 1
    elif star == "5" and count_fives < num_bigrams:
      data = bigrams(word1, word2, star)
      bigram_data.append(data)
      count_fives += 1

  return bigram_data

def build_features(prob_distribution, most_info_words, most_info_bigrams, words_review, most_common_words):
  words = parse_most_info('features_text/most_informative_1_to_5.txt', 20)
  bigrams = parse_bigrams('features_text/bigrams.txt', 20)




def main():
  #parse_most_info('most_informative_1_to_5.txt'i, 20)
  #parse_bigrams('bigrams.txt', 20)
if __name__ == "__main__":
  main()
