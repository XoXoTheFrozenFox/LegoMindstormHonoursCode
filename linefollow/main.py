#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase


left_motor = Motor(Port.B)
right_motor = Motor(Port.C)


line_sensor = ColorSensor(Port.S2)

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)


BLACK = 9
WHITE = 85
threshold = 50


DRIVE_SPEED = 100
PROPORTIONAL_GAIN = 1.2

while True:
    deviation = line_sensor.reflection() - threshold
    turn_rate = PROPORTIONAL_GAIN * deviation
    robot.drive(DRIVE_SPEED, turn_rate)
wait(10)