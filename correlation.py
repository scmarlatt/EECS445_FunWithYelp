import json
from pprint import pprint
import plotly.plotly as py
from plotly.graph_objs import *




# def read_reviews(filename):
# 	reviews = open(filename)
# 	data = json.load(reviews)
# 	pprint(data)
# 	#return data 
class pairs:
	def __init__(self):
		self.stars = 0
		self.useful = 0

def main():
	f = open('reviews_sample.json','rb')
	a = []
	for line in f:
		rec = json.loads(line.strip())
		s = pairs()
		s.stars = rec["stars"]
		s.useful = rec["votes"]["useful"]
		a.append(s)
	f.close()

	stars = []
	useful = []
	for pair in a:
		stars.append(pair.stars)
		useful.append(pair.useful)
	# plt.plot(stars,useful , 'ro')
	# plt.axis([0,5,0,20])
	# plt.savefig('test.png')

	trace0 = Scatter(
    x= stars,
    y= useful
	)
	#print str(trace0)
	data = Data([trace0])

	unique_url = py.plot(data, filename = 'test.png')
	print unique_url
	





if __name__ == "__main__":
  main()


