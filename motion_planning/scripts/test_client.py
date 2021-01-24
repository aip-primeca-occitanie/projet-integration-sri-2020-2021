#! /usr/bin/env python

import rospy, actionlib
from motion_planning.msg import PickUpPoseAction, PickUpPoseGoal

def test_client_client():
    client = actionlib.SimpleActionClient('pick', PickUpPoseAction)
    client.wait_for_server()

    # Creates a goal to send to the action server.
    goal = PickUpPoseGoal()
    goal.object_pose.header.frame_id = 'base_footprint'
    goal.object_pose.pose.position.x = 0.531774938258
    goal.object_pose.pose.position.y = -0.0489538018672
    goal.object_pose.pose.position.z = 0.859598292586
    goal.object_pose.pose.orientation.x = 0
    goal.object_pose.pose.orientation.y = 0
    goal.object_pose.pose.orientation.z = 0
    goal.object_pose.pose.orientation.w = 1.0

    # Sends the goal to the action server.
    client.send_goal(goal)

if __name__ == '__main__':
    rospy.init_node('test_client')
    rospy.loginfo("qmkdfjqmk")
    rospy.sleep(3)
    test_client_client()