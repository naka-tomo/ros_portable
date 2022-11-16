#!/usr/bin/env python
from __future__ import print_function, unicode_literals

import os
import sys
# IPを設定
os.environ["ROS_MASTER_URI"] = "http://127.0.0.1:11311"
os.environ["ROS_IP"] = "127.0.0.1"

# roslibへのパスを通す
sys.path.append("../")

import rospy
from std_msgs.msg import String

def main():
    rospy.init_node('talker', anonymous=True)

    pub = rospy.Publisher('chatter', String, queue_size=10)
    r = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        str = "hello world %s"%rospy.get_time()
        print(str)
        pub.publish(str)
        r.sleep()

if __name__ == '__main__':
    main()
