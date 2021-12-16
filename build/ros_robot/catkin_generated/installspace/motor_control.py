#!/usr/bin/env python2

#Import modules.
import rospy
import serial
import sys
from std_msgs.msg import String
from geometry_msgs.msg import Twist

g_node = None
g_ser = None
l = 0.267

def sub_callback(msg):
    """
    Callback function to obtain target velocity for arduino.

    Parameters:
    -------------
    msg : Twist

    Returns:
    -------------
    None

    """
    global g_node
    global g_ser
    global l
    # Convert linear (m/s) and angular velocity (rad/s) to encoder information.
    r = l/2
    encoder_x = int(msg.linear.x / (4 * 0.02040816 * 0.0508 * 2 * 3.14))
    linear_left, linear_right = convert_angular_to_linear(msg.angular.z, r)
    encoder_linear_left = int(linear_left / (4 * 0.02040816 * 0.0508 * 2 * 3.14))
    encoder_linear_right = int(linear_right / (4 * 0.02040816 * 0.0508 * 2 * 3.14))
    # Add linear and angular velocities to obtain velocity of each wheel.
    vel_left = encoder_x + encoder_linear_left
    vel_right = encoder_x + encoder_linear_right
    # Send velocity information to arduino.
    g_ser.write("{:d},{:d}\n".format(int(vel_left), int(vel_right)).encode())

def convert_angular_to_linear(angular_velocity, r):
    """
    Convert angular velocity of the whole robot to its equivalent linear 
    velocity on both wheels of robot.

    Parameters:
    -------------
    angular_velocity : `int`
    r : `int`

    Returns:
    -------------
    Tuple containing speed on left and right wheels.

    """
    # Obtain magnitude of angular speed.
    angular_vel = abs(angular_velocity) 
    # Given sign of angular velocity, rotate to the right or left.
    if angular_velocity < 0:
        linear_left = r * angular_vel
        linear_right = - r * angular_vel
    elif angular_velocity > 0:
        linear_left = -r * angular_vel
        linear_right = r * angular_vel
    else:
        # IF angular velocity is zero, the speed of both wheels is also zero.
        linear_left = 0
        linear_right = 0
    return (linear_left, linear_right)

def main(args=None):
    global g_node
    global g_ser
    # Start the arduino node.
    rospy.init_node('arduino')
    # Create publisher that sends the desired velocity to the arduino through
    # the serial port.
    publisher = rospy.Publisher('platform_vel', Twist, queue_size=10)
    # Create subsriber that listens for the target velocity given by the navigation node.
    rospy.Subscriber('target_vel', Twist, sub_callback)
    msg = Twist()
    i = 0
    # Open serial port to communicate with arduino.
    g_ser=serial.Serial('/dev/ttyACM0', 115200, timeout=1)
    # Information will be sent at 10 Hz.
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        # Check that we are receiving the correct information from the arduino.
        line=g_ser.readline(100)
        vals=line.decode().split(',')
        if(len(vals) != 5):
            continue
        # Prepare data to be published. 
        msg.linear.x= float(vals[0]) * 4 * 0.02040816 * 0.0508 * 2 * 3.14
        msg.angular.z= float(vals[1])
        publisher.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    main()
