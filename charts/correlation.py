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
        colors = ['rgb(249,18,18)','rgb(18,18,247)','rgb(249, 249, 18)',
          'rgb(41,249,18)','rgb(241,18,249)']
        print 'hi'
        f = open('reviews_sample.json','rb')
        a = []
        for line in f:
                rec = json.loads(line.strip())
                s = pairs()
                s.useful = rec["votes"]["useful"]
                if s.useful == 0:
                        continue
                s.stars = rec["stars"]
                s.length = len(rec["text"])
                a.append(s)
        f.close()

        usefulOnes = []
        usefulTwos = []
        usefulThrees = []
        usefulFours = []
        usefulFives = []
        

        ones = []
        twos = []
        threes = []
        fours = []
        fives = []


        for pair in a:
                if pair.stars == 1:
                        usefulOnes.append(pair.useful)
                        ones.append(pair.length)
                elif pair.stars == 2:
                        usefulTwos.append(pair.useful)
                        twos.append(pair.length)
                elif pair.stars == 3:
                        usefulThrees.append(pair.useful)
                        threes.append(pair.length)
                elif pair.stars == 4:
                        usefulFours.append(pair.useful)
                        fours.append(pair.length)
                else:
                        usefulFives.append(pair.useful)
                        fives.append(pair.length)


        

        trace1 = Scatter(
                x= usefulOnes,
                y= ones,
                mode = 'markers',
                marker = Marker(
                        color=colors[0]
                )
        )
        trace2 = Scatter(
                x= usefulTwos,
                y= twos,
                mode = 'markers',
                marker = Marker(
                        color=colors[1]
                )
        )
        trace3 = Scatter(
                x= usefulThrees,
                y= threes,
                mode = 'markers',
                marker = Marker(
                        color=colors[2]
                )
        )
        trace4 = Scatter(
                x= usefulFours,
                y= fours,
                mode = 'markers',
                marker = Marker(
                        color=colors[3]
                )
        )
        trace5 = Scatter(
                x= usefulFives,
                y= fives,
                mode = 'markers',
                marker = Marker(
                        color=colors[4]
                )
        )
        data = Data([trace1, trace2, trace3, trace4, trace5])
        unique_url = py.plot(data, filename = 'test.png')





if __name__ == "__main__":
        main()


