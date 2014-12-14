import json
from nltk.stem.porter import *
from nltk.stem.snowball import SnowballStemmer
import codecs
import string

def main():
  f = open('useful_reviews.json', 'r')
  clean_review = ""
  q = open('features_text/stopwords.txt')
  stopwords = []
  restaurants = open('features_text/restaurant_ids.txt')
  ids = []
  one_stars = codecs.open('useful_reviews/one_stars.txt', "w", "utf-8")
  two_stars = codecs.open('useful_reviews/two_stars.txt', "w", "utf-8")
  three_stars = codecs.open('useful_reviews/three_stars.txt', "w", "utf-8")
  four_stars = codecs.open('useful_reviews/four_stars.txt', "w", "utf-8")
  five_stars = codecs.open('useful_reviews/five_stars.txt', "w", "utf-8")
  not_words = ["couldn t", "wouldn t", "aren t", "can t", "didn t", "doesn t", "don t", "hadn t", "hasn t", "haven t", "isnt t", "musn t", "shouldn t", "won t"]
  for word in restaurants:
    ids.append(word.rstrip())
  stemmer = SnowballStemmer("english")
  for word in q:
    stopwords.append(word.rstrip())
  for line in f:
    rec = json.loads(line.strip())
    if (rec["business_id"] in ids):
      r = unicode(rec["text"].lower())
      remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
      r2 = r.translate(remove_punctuation_map)
      arr = r2.split(" ")
      for i in range(0, len(arr)):
        if arr[i] in stopwords:
          arr[i] = ""
        elif arr[i] in not_words:
          arr[i] = "not"
        else:
         #  arr[i] = stemmer.stem(arr[i])
           continue
      final = ' '.join(arr)
      final = final.replace('\n', ' ')
      final = ' '.join(final.split())
      if rec["stars"] == 1:
        one_stars.write(final + '\n')
      elif rec["stars"] == 2:
        two_stars.write(final + '\n')
      elif rec["stars"] == 3:
        three_stars.write(final + '\n')      
      elif rec["stars"] == 4:
        four_stars.write(final + '\n')
      elif rec["stars"] == 5:
        five_stars.write(final + '\n')

if __name__ == "__main__":
  main()


