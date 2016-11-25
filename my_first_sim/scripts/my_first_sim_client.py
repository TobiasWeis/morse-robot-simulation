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

try:
    from pymorse import Morse
except ImportError:
    print("you need first to install pymorse, the Python bindings for MORSE!")
    sys.exit(1)

lv = LaserVisualizer(180)

print("Use WASD to control the robot")

with Morse() as simu:

  motion = simu.robot.motion
  sick = simu.robot.sick
  pose = simu.robot.pose

  v = 0.0 # velocity
  w = -0.1 # angular velocity

  while True:
      '''
      key = input("WASD?")
      if key.lower() == "w":
          v += 0.1
      elif key.lower() == "s":
          v -= 0.1
      elif key.lower() == "a":
          w += 0.1
      elif key.lower() == "d":
          w -= 0.1
      else:
          continue
      '''

      # here, we call 'get' on the pose sensor: this is a blocking
      # call. Check pymorse documentation for alternatives, including
      # asynchronous stream subscription.
      print("The robot is currently at: %s" % pose.get())
      sickdata = sick.get_local_data().result()
      print(sickdata.keys())
      print(sickdata["range_list"])
      print(len(sickdata["range_list"]))
      lv.visualize(sickdata["range_list"])

      motion.publish({"v": v, "w": w})

      time.sleep(.1)
