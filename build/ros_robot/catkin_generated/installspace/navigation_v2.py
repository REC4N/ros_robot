#!/usr/bin/env python2
# ECE 5730 - Robotics

# navigation.py - Nav control node to send velocity to motor control node.

# Import libraries.
import rospy
import sys

from geometry_msgs.msg import Twist


def node():
    # Create Navigation node.
    rospy.init_node('navigation')
    # Define and initialize variables for motor control use.
    global keyboard_vx
    global keyboard_vtheta
    keyboard_vx = 0.0
    keyboard_vtheta = 0.0
    # Create publisher node for target velocity of motor control.
    #self.publisher_ = self.create_publisher(Twist, 'target_vel', 10)
    publisher_ = rospy.Publisher('target_vel', Twist, queue_size=10)
    # Send messages every 10 Hz
    rospy.Subscriber('cmd_vel', Twist, keyboard_callback)
    rate = rospy.Rate(10)
    msg = Twist()
    while not rospy.is_shutdown():
        msg.linear.x = float(keyboard_vx)
        msg.angular.z = float(keyboard_vtheta)
        publisher_.publish(msg)
        rospy.loginfo('(Vx: "%4.2f", Vtheta: "%2.2f")' % (msg.linear.x, msg.angular.z))
        rate.sleep()
    #timer_period = 0.1  # seconds 
    #self.timer = self.create_timer(timer_period, self.publish_motor_control)
    # Create subscriber node to a 'platform_vel' topic and expects a Twist message.
    #self.subscription_motor_control = self.create_subscription(
    #    Twist,
    #    'platform_vel',
    #    self.motor_control_callback,
    #    10)
    #self.subscription_motor_control  # prevent unused variable warning
    # Create subscriber node to a 'cmd_vel' topic and expects a Twist message.
    #self.subscription_keyboard = self.create_subscription(
    #    Twist,
    #    'cmd_vel',  # Topic of teleop_twist_keyboard node.
    #    self.keyboard_callback,
    #    10)
    #self.subscription_keyboard  # prevent unused variable warning


def keyboard_callback(msg):
    """
    Assigns the recieved message from the keyboard into class variables.
    """
    global keyboard_vx
    global keyboard_vtheta
    keyboard_vx = msg.linear.x
    keyboard_vtheta = msg.angular.z

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
