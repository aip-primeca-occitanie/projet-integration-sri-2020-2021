#!/usr/bin/env python
# license removed for brevity

import rospy
import sys

# Brings in the SimpleActionClient
import actionlib
# Brings in the .action file and messages used by the move base action
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Pose, PoseStamped, Point, Quaternion, PoseWithCovarianceStamped
from move_to_goal import movebase_client

flag = False

def callback(msg, args):
  current_pose = args
  global flag
  flag = True
  current_pose = msg
  # rospy.loginfo("I heard %s", msg.pose.pose.position.x)

def check_pose(pose_goal, current_pose):
  rospy.Subscriber('/robot_pose', PoseWithCovarianceStamped, callback, (current_pose))

  print(flag)

  current_pose_x = current_pose.pose.pose.position.x
  current_pose_y = current_pose.pose.pose.position.y

  pose_goal_x = pose_goal.pose.position.x
  pose_goal_y = pose_goal.pose.position.y
  if(flag == True):
    print(current_pose_x >= pose_goal_x + 0.05)
    while((current_pose_x >= pose_goal_x + 0.05 or current_pose_x <= pose_goal_x - 0.05) or (current_pose_y >= pose_goal_y + 0.05 or current_pose_y <= pose_goal_y - 0.05)):
      print("hi") 
      print(current_pose)

      point = Point(0.0, 0.0, 0)
      quaternion = Quaternion(0.0, 0.0, 0.0, 0.77)
      frame= "map"

      if(current_pose_x >= pose_goal_x + 0.05):
        rospy.loginfo("La position en X du robot est incorrecte.")
        point.x = -0.05
      elif(current_pose_x <= pose_goal_x - 0.05):
        rospy.loginfo("La position en X du robot est incorrecte.")   
        point.x = 0.05

      if(current_pose_y >= pose_goal_y + 0.05):
        rospy.loginfo("La position en Y du robot est incorrecte.")
        point.y = -0.05
      elif(current_pose_y <= pose_goal_y - 0.05):
        rospy.loginfo("La position en Y du robot est incorrecte.")
        point.y = 0.05  
      
      movebase_client(point, quaternion, frame)
    return flag
  return flag




# If the python node is executed as main process (sourced directly)
if __name__ == '__main__':
  # Initializes a rospy node to let the SimpleActionClient publish and subscribe
  rospy.init_node('check_pose')


  point = Point(1, 1.0, 0)
  quaternion = Quaternion(0.0, 0.0, 0.0, 0.77)
  frame= "map"
  pose = PoseStamped()
  pose.pose.position = point
  pose.pose.orientation = quaternion
  pose.header.frame_id = frame
  pose.header.stamp = rospy.Time.now()

  a = 0

  current_pose = PoseWithCovarianceStamped()
  while(flag == False):
    a = check_pose(pose, current_pose)
  print("end")
