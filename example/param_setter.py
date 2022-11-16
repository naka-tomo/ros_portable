#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import os
import sys
# IPを設定
os.environ["ROS_MASTER_URI"] = "http://127.0.0.1:11311"
os.environ["ROS_IP"] = "127.0.0.1"

# roslibへのパスを通す
sys.path.append("../")

import rospy

def main():
    global param
    rospy.init_node("param_setter")
    
    while not rospy.is_shutdown():
        param = input("input parameter ->")
        param = float(param)
        rospy.set_param( "/param_tutrial/param", param )
        
if __name__ == "__main__":
    main()
10