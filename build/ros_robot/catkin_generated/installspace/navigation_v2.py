#!/usr/bin/env python2

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
    # Linear and angular distance from Apriltags
    diff_x = 0.0
    diff_z = 0.0
    # Create publisher node for target velocity of motor control.
    publisher_ = rospy.Publisher('target_vel', Twist, queue_size=10)
    # Create subsriber to teleop keyboard node (if necessary).
    rospy.Subscriber('cmd_vel', Twist, keyboard_callback)
    # Create subsriber to april tags detection node.
    rospy.Subscriber('tag_detections', AprilTagDetectionArray, apriltag_callback)
    # Uncomment following lines of code to use robot with keyboard.  
    #rate = rospy.Rate(10)
    #msg = Twist()
    #while not rospy.is_shutdown():
    #    msg.linear.x = float(keyboard_vx)
    #    msg.angular.z = float(keyboard_vtheta)
    #    publisher_.publish(msg)
    #    rospy.loginfo('(Vx: "%4.2f", Vtheta: "%2.2f")' % (msg.linear.x, msg.angular.z))
    #    rate.sleep()
    # Comment following lines of code to use robot with keyboard.  
    # Refresh at 10 Hz.
    rate = rospy.Rate(10)
    msg = Twist()
    while not rospy.is_shutdown():
        # Move robot near apriltag until it is at less than 1.0 meter and aligned with the tag.
        while diff_z > 1.0 or diff_x > 0.3 or diff_x < -0.3:
            # Check for linear distance between robot and apriltag.
            if diff_z > 1.0:
                msg.linear.x = float(-0.4)
            else:
                msg.linear.x = float(0)
            # Check for alignment between robot and apriltag.
            if diff_x < 0.2:
                msg.angular.z = float(1.5)
            elif diff_x > 0.2:
                msg.angular.z = float(-1.5)
            else:
                msg.angular.z = float(0)
            # Publish velocities to motor control node.
            publisher_.publish(msg)
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
    Function that executes when april tag is detected.
    """
    global diff_x 
    global diff_z 
    # Execute when there is an apriltag detected.
    if len(msg.detections) != 0:
        # Assign information of location of apriltag to global variables.
        diff_x = msg.detections[0].pose.pose.pose.position.x
        diff_z = msg.detections[0].pose.pose.pose.position.z
    else:
        diff_x = 0
        diff_z = 0

def main(args=None):
    try:
        # Run Navigation node.
        node()
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()
