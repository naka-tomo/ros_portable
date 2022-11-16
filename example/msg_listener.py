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

def callback(data):
    print( data.data )
    
def main():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", String, callback)
    rospy.spin()
        
if __name__ == '__main__':
    main()
