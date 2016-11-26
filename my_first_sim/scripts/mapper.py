import math
import matplotlib.pyplot as plt
import numpy as np

class Mapper():
    def __init__(self):
        self.mappoints = []
        plt.ion()

    def integrate(self, pos, egopoints):
        # we know our current pose from the odometry,
        # so we just translate and rotate the sick-data to build a map

        # first, discard all measurements that are max-dist

        for c in egopoints:
            tx = c[0]  # compensate for laserscanner relative to robot center 
            ty = c[1] + 0.6 
            ta = pos.a

            x = tx * math.cos(ta) - ty * math.sin(ta)
            y = ty * math.cos(ta) + tx * math.sin(ta)

            x += pos.x
            y += pos.y

            self.mappoints.append([x,y])

    def visualize(self):
        fig = plt.figure(3)
        plt.cla()
        fig.clf()
        
        ps = np.array(self.mappoints)
        plt.scatter(ps[:,0], ps[:,1], alpha=0.1)

        plt.axes().set_aspect('equal', 'datalim')

        plt.show()
        plt.pause(0.000001)



