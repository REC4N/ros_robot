#!/usr/bin/env python2
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
    global diff_x 
    global diff_z 
    keyboard_vx = 0.0
    keyboard_vtheta = 0.0
    diff_x = 0.0
    diff_z = 0.0
    # Create publisher node for target velocity of motor control.
    publisher_ = rospy.Publisher('target_vel', Twist, queue_size=10)
    rospy.Subscriber('cmd_vel', Twist, keyboard_callback)
    rospy.Subscriber('tag_detections', AprilTagDetectionArray, apriltag_callback)
    """  
    rate = rospy.Rate(10)
    msg = Twist()
    while not rospy.is_shutdown():
        msg.linear.x = float(keyboard_vx)
        msg.angular.z = float(keyboard_vtheta)
        publisher_.publish(msg)
        rospy.loginfo('(Vx: "%4.2f", Vtheta: "%2.2f")' % (msg.linear.x, msg.angular.z))
        rate.sleep()
    """ 
    rate = rospy.Rate(10)
    msg = Twist()
    while not rospy.is_shutdown():
        while diff_z > 1.0 or diff_x > 0.2 or diff_x < -0.2:
            if diff_z > 1.0:
                msg.linear.x = float(-0.2)
            else:
                msg.linear.x = float(0)
            if diff_x < 0.2:
                msg.angular.z = float(-1.3)
            elif diff_x > 0.2:
                msg.angular.z = float(1.3)
            else:
                msg.angular.z = float(0)
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
    global diff_x 
    global diff_z 
    # Execute when there is an apriltag detected.
    if len(msg.detections) != 0:
        rospy.loginfo(msg.detections[0].pose.pose.pose.position.z)
        diff_x = msg.detections[0].pose.pose.pose.position.x
        diff_z = msg.detections[0].pose.pose.pose.position.z
    else:
        diff_x = 0
        diff_z = 0

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
