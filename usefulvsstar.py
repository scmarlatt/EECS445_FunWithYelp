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
        colors = ['rgb(254,229,217)','rgb(252,174,145)','rgb(251, 106, 74)',
          'rgb(222,45,38)','rgb(165,15,21)']
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
        star = []

        for pair in a:
            useful.append(s.useful)
            star.append(s.star)
        
        trace1 = Scatter(
            x= useful,
            y= star,
            mode = 'markers'
        )

        data = Data([trace1])
        unique_url = py.plot(data, filename = 'test1.png')

            





if __name__ == "__main__":
        main()
