import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

class Position():
    def __init__(self, x,y,a):
        self.x = x
        self.y = y
        self.a = a

class OdoVisualizer():
    def __init__(self):
        values = [
                'x',
                'y',
                'z',
                'yaw',
                'pitch',
                'roll',
                'timestamp'
                ]

        self.pos = Position(0.0, 0.0, 0.0)

        self.valuelist = {}
        for v in values:
            self.valuelist[v] = []

        plt.ion()

    def add_values(self,odo):
        self.pos.x = odo['x']
        self.pos.y = odo['y']
        self.pos.a = odo['yaw'] - math.pi/2.

    def visualize_integrated(self):
        fig = plt.figure(2)
        #plt.cla()
        #fig.clf()
        cmap = matplotlib.cm.get_cmap('hsv')
        rgba = cmap((self.pos.a/(2.*math.pi) % 1.))

        plt.plot(self.pos.x, self.pos.y, 'o', c=rgba) #, color="%f" % (self.pos.a /(math.pi*2.)))

        # arrow visualization
        al = 0.1

        # rotate unity vec (arrowhead)
        ahx = self.pos.x - al*math.sin(self.pos.a)
        ahy = self.pos.y + al*math.cos(self.pos.a)

        plt.arrow(self.pos.x,  #x1
                  self.pos.y,  # y1
                  ahx-self.pos.x, # x2 - x1
                  ahy-self.pos.y, # y2 - y1
                  width=0.005, head_width=0.05, head_length=0.05,
                  color=rgba)

        plt.axes().set_aspect('equal', 'datalim')
        #plt.title("x: %.2f, y: %.2f, a: %.2f" % (self.pos.x, self.pos.y, self.pos.a))
        plt.show()
        plt.pause(0.0000001)
