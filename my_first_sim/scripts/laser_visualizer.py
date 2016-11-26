import math
import matplotlib.pyplot as plt
import numpy as np

class LaserVisualizer():
    def __init__(self, degs, steps=1, lrange=30):
        self.degs = degs
        self.steps = steps
        self.lrange = lrange
        self.egopoints = []

        plt.ion()

    def visualize(self, points):
        fig = plt.figure(0)
        plt.cla()
        fig.clf()
        
        self.egopoints = []
        for i,p in enumerate(points):
            if p < 30.0:
                # calculate the angle of the measurement
                curr_deg = math.radians(-self.degs/2. + i*self.steps)

                # rotate and display
                x = 0*math.cos(curr_deg) - p*math.sin(curr_deg)
                y = p*math.cos(curr_deg) + 0*math.sin(curr_deg)
                self.egopoints.append([x,y])

        ps = np.array(self.egopoints)
        plt.scatter(ps[:,0], ps[:,1])

        plt.axes().set_aspect('equal', 'datalim')

        plt.xlim((-31,31))
        plt.ylim((-1,31))
        plt.show()
        plt.pause(0.000001)



