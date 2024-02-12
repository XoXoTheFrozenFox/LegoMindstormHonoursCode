#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
line_sensor = ColorSensor(Port.S4)
color_sensor = ColorSensor(Port.S1)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
B = 6
W = 69
threshold = (3+ 41) / 2
DRIVE_SPEED = 150
PROPORTIONAL_GAIN = 2.0

while True:
    deviation = line_sensor.reflection() - threshold
    turn_rate = PROPORTIONAL_GAIN * deviation
    robot.drive(DRIVE_SPEED, turn_rate)
    
    if color_sensor.color()==Color.BLACK:
        robot.drive (100, -100) 
        wait(600) 
    robot.drive(DRIVE_SPEED, turn_rate)

    if color_sensor.color()==Color.RED:
        if color_sensor.color()==Color.BLUE:
            robot.drive (100,180)
            wait(1000)
            robot.straight(300)
            robot.drive(100,180)
            wait(1000)
            robot.drive(DRIVE_SPEED, turn_rate)
            wait(15000)

    if color_sensor.color()==Color.RED:
        if color_sensor.color()==Color.GREEN:
            robot.stop()
            
    if color_sensor.color()==Color.GREEN:
        robot.drive(100,180)
        wait(1000)
    robot.drive(DRIVE_SPEED, turn_rate)
