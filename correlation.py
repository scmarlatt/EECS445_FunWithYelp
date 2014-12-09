
import json
from pprint import pprint
import plotly.plotly as py
from plotly.graph_objs import *



class pairs:
        def __init__(self):
                self.stars = 0
                self.useful = 0

def main():
        print 'hi'
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

        trace0 = Scatter(
                x= stars,
                y= useful,
		mode = 'markers'
        )
        data = Data([trace0])
        unique_url = py.plot(data, filename = 'test.png')





if __name__ == "__main__":
        main()
