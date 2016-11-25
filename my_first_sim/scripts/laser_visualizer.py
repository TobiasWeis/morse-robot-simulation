import math
import matplotlib.pyplot as plt

class LaserVisualizer():
    def __init__(self, degs, steps=1, lrange=30):
        self.degs = degs
        self.steps = steps
        self.lrange = lrange
        plt.ion()

    def visualize(self, points):
        fig = plt.figure(0)
        plt.cla()
        fig.clf()
        
        for i,p in enumerate(points):
            # calculate the angle of the measurement
            curr_deg = math.radians(-self.degs/2. + i*self.steps)

            # rotate and display
            x = 0*math.cos(curr_deg) - p*math.sin(curr_deg)
            y = p*math.cos(curr_deg) + 0*math.sin(curr_deg)
            plt.plot(x,y,'ko')

        plt.xlim((-31,31))
        plt.ylim((-1,31))
        plt.show()
        plt.pause(0.001)



