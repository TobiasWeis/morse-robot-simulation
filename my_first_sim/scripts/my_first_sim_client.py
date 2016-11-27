#! /usr/bin/env python3
"""
Test client for the <my_first_sim> simulation environment.

This simple program shows how to control a robot from Python.

For real applications, you may want to rely on a full middleware,
like ROS (www.ros.org).
"""

import sys
import time
from laser_visualizer import *
from odo_visualizer import *
from mapper import *
from MyConfig import *

try:
    from pymorse import Morse
except ImportError:
    print("you need first to install pymorse, the Python bindings for MORSE!")
    sys.exit(1)


c = Config()
lv = LaserVisualizer(180)
ov = OdoVisualizer()
mapper = Mapper(c)

print("Use WASD to control the robot")

with Morse() as simu:

  motion = simu.robot.motion
  sick = simu.robot.sick
  pose = simu.robot.pose
  odo = simu.robot.odo

  v = 0.1 # velocity
  w = -0.1 # angular velocity

  # send commands to robot
  #motion.publish({"v": v, "w": w})

  while True:
      #print("The robot is currently at: %s" % pose.get())

      # odometry (assume it has already been integrated)
      ododata = odo.get_local_data().result()

      # laserscanner
      sickdata = sick.get_local_data().result()

      ov.add_values(ododata)

      lv.visualize(sickdata["range_list"])
      ov.visualize_integrated()

      # mapper
      mapper.integrate(ov.pos, lv.egopoints)
      mapper.visualize()
