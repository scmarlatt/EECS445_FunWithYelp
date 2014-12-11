import json
from pprint import pprint

def main():
  f = open('../yelp_academic_dataset_business.json','r')

  for line in f:
    rec = json.loads(line.strip())
    if "Restaurants" in rec["categories"] or "Food" in rec["categories"]:
      print rec["business_id"]

if __name__ == "__main__":
  main()
