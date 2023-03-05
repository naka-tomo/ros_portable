#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import os
import sys
import rospy
import actionlib
from custom_msgs.msg import *
import yaml


def feedback(fb):
    seq = yaml.safe_load(fb.feedback)["sequence"]
    print("feedback:", seq)


def main():
    rospy.init_node("action_client")
    action_client = actionlib.SimpleActionClient("ros_tutorial_action", StringAction)
    action_client.wait_for_server()

    goal = StringActionGoal()
    goal.goal = yaml.dump({"order": 10})

    action_client.send_goal(goal, feedback_cb=feedback)
    action_client.wait_for_result()
    res = action_client.get_result()
    sequence = yaml.safe_load(res.result)["sequence"]
    print("result:", sequence)


if __name__ == "__main__":
    main()
