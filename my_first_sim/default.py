#! /usr/bin/env morseexec

""" Basic MORSE simulation scene for <my_first_sim> environment

Feel free to edit this template as you like!
"""

from morse.builder import *
from morse.sensors.laserscanner import *
from my_first_sim.builder.robots import Mycar

#robot = Morsy()
#robot = ATRV()
robot = Mycar()
robot.translate(0.0, 0.0, 0.0)
robot.rotate(0.0, 0.0, 0.0)
robot.add_default_interface('socket')


# set 'fastmode' to True to switch to wireframe mode
env = Environment('indoors-1/boxes_tobi', fastmode = False)
env.set_camera_location([-18.0, -6.7, 10.8])
env.set_camera_rotation([1.09, 0, -1.14])


