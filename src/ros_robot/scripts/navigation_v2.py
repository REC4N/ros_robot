#!/usr/bin/env python
# ECE 5730 - Robotics


# Import libraries.
import rospy
import sys

from geometry_msgs.msg import Twist
from apriltag_ros.msg import AprilTagDetectionArray


def node():
    # Create Navigation node.
    rospy.init_node('navigation')
    # Define and initialize variables for motor control use.
    global keyboard_vx
    global keyboard_vtheta
    keyboard_vx = 0.0
    keyboard_vtheta = 0.0
    # Create publisher node for target velocity of motor control.
    publisher_ = rospy.Publisher('target_vel', Twist, queue_size=10)
    rospy.Subscriber('cmd_vel', Twist, keyboard_callback)
    rospy.Subscriber('tag_detections', AprilTagDetectionArray, apriltag_callback)
    rate = rospy.Rate(10)
    msg = Twist()
    while not rospy.is_shutdown():
        msg.linear.x = float(keyboard_vx)
        msg.angular.z = float(keyboard_vtheta)
        publisher_.publish(msg)
        #rospy.loginfo('(Vx: "%4.2f", Vtheta: "%2.2f")' % (msg.linear.x, msg.angular.z))
        rate.sleep()


def keyboard_callback(msg):
    """
    Assigns the recieved message from the keyboard into class variables.
    """
    global keyboard_vx
    global keyboard_vtheta
    keyboard_vx = msg.linear.x
    keyboard_vtheta = msg.angular.z

def apriltag_callback(msg):
    """
    Assigns the recieved message from the keyboard into class variables.
    """
    if len(msg.detections) != 0:
        #rospy.loginfo('April tag detected')
        rospy.loginfo(msg.detections)
        #if msg.detections.id.index(0) is not None:
        #    rospy.loginfo(msg.detections.pose)

def main(args=None):
    # Initialize rclpy
    # Navigation node.

    try:
        # Run Navigation node.
        node()
        
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()
