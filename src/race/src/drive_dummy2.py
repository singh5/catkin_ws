#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from race.msg import drive_param
from race.msg import pid_input

pub = rospy.Publisher('drive_parameters', drive_param, queue_size=1)

def callback(data):
	msg = drive_param()

	msg.velocity = 8
	msg.angle = 0
	pub.publish(msg)

if __name__ == '__main__':
	print("Dummy drive node started")
	rospy.init_node('drive_dummy', anonymous=True)
	rospy.Subscriber("scan", LaserScan, callback)
	rospy.spin()
