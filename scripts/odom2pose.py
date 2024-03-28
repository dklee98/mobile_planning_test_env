#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped

class OdometryConverter:
    def __init__(self):
        # Create a ROS subscriber to receive odometry messages
        self.sub = rospy.Subscriber("/agent/odom", Odometry, self.callback)
        # Create a ROS publisher to publish pose stamped messages
        self.pub = rospy.Publisher("/agent/posestamped", PoseStamped, queue_size=1)
    
    def callback(self, msg):
        # Create a geometry_msgs/PoseStamped message
        pose_stamped_msg = PoseStamped()
        # Set the header field of the pose stamped message to the header field of the odometry message
        pose_stamped_msg.header = msg.header
        # Set the pose field of the pose stamped message to the pose field of the odometry message
        pose_stamped_msg.pose = msg.pose.pose
        
        # Publish the geometry_msgs/PoseStamped message
        self.pub.publish(pose_stamped_msg)

if __name__ == '__main__':
    # Initialize the ROS node
    rospy.init_node("odometry_converter")
    # Create an OdometryConverter object
    oc = OdometryConverter()
    # Keep the node running until it is shutdown
    rospy.spin()
