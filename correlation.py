
mport json
from pprint import pprint
import plotly.plotly as py
from plotly.graph_objs import *



class pairs:
        def __init__(self):
                self.useful = 0
                self.length = 0



def main():
        print 'hi'
        f = open('reviews_sample.json','rb')
        a = []
        for line in f:
                rec = json.loads(line.strip())
                s = pairs()
                s.stars = rec["votes"]["useful"]
                s.length = len(rec["text"])
                a.append(s)
        f.close()

        useful = []
        lengths = []
        for pair in a:
                useful.append(pair.stars)
                lengths.append(pair.total)

        trace0 = Scatter(
                x= useful,
                y= lengths,
                mode = 'markers'
        )
        data = Data([trace0])
        unique_url = py.plot(data, filename = 'test.png')





if __name__ == "__main__":
        main()


