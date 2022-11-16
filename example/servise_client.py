#!/usr/bin/env python
from __future__ import print_function, unicode_literals
import os
import sys
# IPを設定
os.environ["ROS_MASTER_URI"] = "http://127.0.0.1:11311"
os.environ["ROS_IP"] = "127.0.0.1"

# roslibへのパスを通す
sys.path.append("../")

import sys
import rospy
from custom_msgs.srv import *
import yaml

def main():
    x = int(sys.argv[1])
    y = int(sys.argv[2])

    rospy.init_node('srvise_client' )
    rospy.wait_for_service('add')
    add = rospy.ServiceProxy('add', StringTrigger)
    request = yaml.dump({"a":x, "b":y})
    result = add( request ).result
    sum = yaml.safe_load(result)["sum"]
    print( x, y, sum )


if __name__ == "__main__":
    main()


 
