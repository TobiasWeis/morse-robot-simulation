# morse-robot-simulation
This repo contains a MORSE robot simulation project.

To run it with morse:
morse import my_first_sim
morse run my_first_sim

I adapted it to feature a laserscanner as well as client-code to read and visualize measurements:

![Simulation and LaserScanner visualization](second_sim.gif)

In the current state of the code, I included my own 3d-car-model,
as well as visualization scripts on the client-side to visualize live and integrated laser-data,
the camera image, as well as the odometry of the robot.

![Simulation, camera image and laser](screenshot_w_laser.png)

Please find more detailed informations here: http://blog.tobias-weis.de/simulating-robots-with-morse/
