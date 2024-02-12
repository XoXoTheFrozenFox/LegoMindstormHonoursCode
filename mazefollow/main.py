#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
ev3.speaker.beep()

# Initialize the motors.
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)


#initializing the touch sencor
touch_sensor = TouchSensor(Port.S3)
wall_sensor = TouchSensor(Port.S4)

#sensors
color_sensor = ColorSensor(Port.S1)
ultrasonic_sensor = UltrasonicSensor(Port.S2)

#global variables

#cheking if hit a wall

DRIVE_SPEED = 120

turn_amount = 97.35


# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=108.25)

#creating the functions for the maze Finder madness

#waiting function fr button press
def waitTouch():
    flag_touch = True
    while flag_touch:
        if (touch_sensor.pressed()):
            flag_touch = False


#to turn robot right if a wall is hit
def hitWall():
    if (wall_sensor.pressed()):
        robot.straight(-15)

        #fine tune here
        robot.turn(96)


       # hit_flag = True
        #x = 0

        #while hit_flag:
        #    if (wall_sensor.pressed()):
         #       hit_flag = False
          #  robot.straight(150)
           # x = x + 15
     #       if (x >= 135):
      #          hit_flag = False

        return False
    else:
        return True


#to turn robot left when a gap is seen
def turnLeft():
    wall_distance = ultrasonic_sensor.distance()
    if (wall_distance > 235) and (wall_distance < 2500) :

        #wait to ensure moves past begining of gap
        robot.straight(126)
        robot.turn(turn_amount * -1)
        robot.straight(135)
        return False
    else:

        #might have to add follow wall to here
        return True


#to follow wall at certain distance
def followWall():

    #problem with following wall, as it turns the wall relative to ultrasonic sensor increases in distance
    robotDist = ultrasonic_sensor.distance()


    if (robotDist > 72) and (robotDist < 2100):
        return -17
    elif (robotDist > 2100) or (robotDist < 62):
        return 17
    else :
        return 0


def correctPos():
    turnChecking()


#turn in both ways, then choose the distrance that is clostest to the wall(meaning it should be parrellel then) 
#turn both ways and get minimum value
def turnChecking():
    # Setting initial minimum distance to a large value
    temp_min = 2550
    # Variable to keep track of the total angle turned
    temp_angle = 0

    # Loop to test different turning angles
    for x in range(360):
        # Turn the robot by one degree
        robot.turn(-1)  # Adjust the direction of rotation to turn left

        # Read the distance from the ultrasonic sensor
        actual_dist = ultrasonic_sensor.distance()

        # Update the minimum distance and total angle if a shorter distance is found
        if actual_dist < temp_min:
            temp_min = actual_dist
            temp_angle = x

    # Turn the robot to the angle with the minimum distance
    robot.turn(temp_angle)


#to drive robot foward
def drive():
    left_flag = turnLeft()
    wall_flag = hitWall()
    if (left_flag and wall_flag):

        #global for turning
        robot.drive(100, followWall())



#correct the posistion of the robot
#find out an idea of accuratly resseting robot position for consistency

#correctPos()

#main program here
waitTouch()

#correctPos()

end_flag = True

while end_flag:
    if (color_sensor.color() == Color.RED):
        wait(1000)
        end_flag = False
    drive()