import math
import matplotlib.pyplot as plt
import numpy as np

class CamVisualizer():
    def __init__(self):
        plt.ion()

    def visualize(self, image):
        fig = plt.figure(5)
        plt.cla()
        fig.clf()
        plt.imshow(image)
        plt.show()
        plt.pause(0.000001)



