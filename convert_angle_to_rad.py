#!/usr/bin/env

# convert the joint angles of the robot from degrees to radians

import numpy as np
import csv

data = np.genfromtxt('new_perception_positions.csv', delimiter=',')
data_radians = data * np.pi / 180
np.savefromtxt('new_perception_positions_radians.csv', data_radians, delimiter=',')
