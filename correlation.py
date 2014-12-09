import json
from pprint import pprint
import plotly.plotly as py
from plotly.graph_objs import *



class pairs:
        def __init__(self):
                self.useful = 0
                self.length = 0
                self.stars = 0



def main():
        print 'hi'
        f = open('reviews_sample.json','rb')
        a = []
        for line in f:
                rec = json.loads(line.strip())
                s = pairs()
                s.useful = rec["votes"]["useful"]
                s.stars = rec["stars"]
                s.length = len(rec["text"])
                a.append(s)
        f.close()

        useful = []
        lengths = []
        stars = []
        for pair in a:
                useful.append(pair.useful)
                lengths.append(pair.length)
                stars.append(pair.stars)
        trace0 = Scatter(
                x= useful,
                y= lengths,
                z= stars,
                mode = 'markers'
        )
        data = Data([trace0])
        unique_url = py.plot(data, filename = 'test.png')





if __name__ == "__main__":
        main()


