import json

def main():
	f = open('../yelp_academic_dataset_business.json','rb')

	for line in f
		rec = json.loads(line.strip())
		if rec["categories"] == "Restaurants" || rec["categories"] == "Food"
			print rec["business id"]


if __name__ == "__main__":
        main()
