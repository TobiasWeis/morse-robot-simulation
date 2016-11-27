from morse.builder import *
from my_first_sim.builder.robots.MyConfig import *

class Mycar(GroundRobot):
    """
    A template robot model for MyCar, with a motion controller and a pose sensor.
    """
    def __init__(self, name = None, debug = True):
       # MyCar.blend is located in the data/robots directory
        GroundRobot.__init__(self, 'my_first_sim/robots/MyCar.blend', name)
        self.properties(classpath = "my_first_sim.robots.MyCar.Mycar")

        self.c = Config()
        print(self.c.laser_offset)

        ###################################
        # Actuators
        ###################################


        # (v,w) motion controller
        # Check here the other available actuators:
        # http://www.openrobots.org/morse/doc/stable/components_library.html#actuators
        self.motion = MotionVW()
        self.append(self.motion)

        # Optionally allow to move the robot with the keyboard
        if debug:
            keyboard = Keyboard()
            keyboard.properties(ControlType = 'Position')
            self.append(keyboard)

        ###################################
        # Sensors
        ###################################

        self.pose = Pose()
        self.append(self.pose)

        # odometry, integrated (means we assume that our position has already been calculated)
        self.odo = Odometry()
        self.odo.level("integrated")
        self.odo.add_interface('socket')
        self.append(self.odo)

        # laser scanner
        self.sick = Sick()
        self.sick.translate(self.c.laser_offset[0], self.c.laser_offset[1], self.c.laser_offset[2])
        self.sick.rotate(0., 0., 0.)
        self.sick.add_interface('socket')
        self.append(self.sick)

        # camera
        self.cam = VideoCamera()
        self.cam.translate(self.c.cam_offset[0], self.c.cam_offset[1], self.c.cam_offset[2])
        self.cam.rotate(0., 0., 0.)
        self.cam.properties(cam_width=self.c.cam_width, cam_height=self.c.cam_height)
        #self.cam.add_interface('socket')
        self.cam.add_stream('socket')
        self.append(self.cam)


