#!/usr/bin/env python
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
import actionlib
from custom_msgs.msg import *
import yaml

action_server = None

def callback( goal ):
    print(goal.goal)
    order = yaml.safe_load(goal.goal)["order"] 
    r = rospy.Rate(1)
    sequence = [0, 1]
    
    for i in range(1, order+1):
        if action_server.is_preempt_requested():
            print("stop")
            break
        
        sequence.append( sequence[i]+sequence[i-1] )
        action_server.publish_feedback( StringFeedback(yaml.dump({"sequence":sequence})) )

        print(sequence)
        r.sleep()

    action_server.set_succeeded( StringResult(yaml.dump({"sequence":sequence})) )        


def main():
    global action_server
    rospy.init_node("action_server")
    action_server = actionlib.SimpleActionServer("ros_tutorial_action", StringAction, execute_cb=callback, auto_start=False)
    action_server.start()
    rospy.spin() 
    
    
if __name__ == "__main__":
    main()
 
