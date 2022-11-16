#!/usr/bin/env python
from __future__ import print_function, unicode_literals
import os
import sys
# IPを設定
os.environ["ROS_MASTER_URI"] = "http://127.0.0.1:11311"
os.environ["ROS_IP"] = "127.0.0.1"

# roslibへのパスを通す
sys.path.append("../")

from custom_msgs.srv import *
import rospy
import yaml

def add(req):
    req = yaml.safe_load( req.data )
    sum = req["a"] + req["b"]
    return StringTriggerResponse( yaml.dump( {"sum": sum } ) )

def add_two_ints_server():
    rospy.init_node('servise_server')
    s = rospy.Service('add', StringTrigger, add)
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()
