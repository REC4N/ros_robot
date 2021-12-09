#!/usr/bin/env python2
#import rclpy
import rospy
#from rclpy.node import Node
import serial
import sys

from std_msgs.msg import String
from geometry_msgs.msg import Twist

g_node = None
g_ser = None
l = 0.267

def sub_callback(msg):
    global g_node
    global g_ser
    global l
    r = l/2
    # Adding conversion between vx and encoder counts.
    encoder_x = int(msg.linear.x / (4 * 0.02040816 * 0.0508 * 2 * 3.14))
    linear_left, linear_right = convert_angular_to_linear(msg.angular.z, r)
    encoder_linear_left = int(linear_left / (4 * 0.02040816 * 0.0508 * 2 * 3.14))
    encoder_linear_right = int(linear_right / (4 * 0.02040816 * 0.0508 * 2 * 3.14))
    vel_left = encoder_x + encoder_linear_left
    vel_right = encoder_x + encoder_linear_right
    #g_node.get_logger().info('I heard "%f"'%msg.linear.x)
    #g_ser.write("{:d},{:d}\n".format(int(msg.linear.x), int(msg.linear.x)).encode())
    g_ser.write("{:d},{:d}\n".format(int(vel_left), int(vel_right)).encode())
    #g_ser.write("{:d},{:d}\n".format(int(msg.linear.x), int(msg.angular.z)).encode())

def convert_angular_to_linear(angular_velocity, r):
    angular_vel = abs(angular_velocity) 
    if angular_velocity < 0:
        linear_left = r * angular_vel
        linear_right = - r * angular_vel
    elif angular_velocity > 0:
        linear_left = -r * angular_vel
        linear_right = r * angular_vel
    else:
        linear_left = 0
        linear_right = 0
    return (linear_left, linear_right)

def main(args=None):
    global g_node
    global g_ser
    #rclpy.init(args=args)
    rospy.init_node('arduino')
    #g_node = rclpy.create_node('arduino_publisher')

    #publisher = g_node.create_publisher(Twist, 'platform_vel', 1)
    publisher = rospy.Publisher('platform_vel', Twist, queue_size=10)
    #subscriber = g_node.create_subscription(Twist, 'target_vel', sub_callback, 1)
    #rospy.Subscriber('target_vel', Twist, sub_callback)
    rospy.Subscriber('target_vel', Twist, sub_callback)

    msg = Twist()

    i = 0
    g_ser=serial.Serial('/dev/ttyACM0', 115200, timeout=1)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        line=g_ser.readline(100)
        #rclpy.spin_once(g_node, timeout_sec=0)
        vals=line.decode().split(',')
        if(len(vals) != 5):
            #print("Got ",len(vals)," vals from ",line)
            continue
        #print("Got ",len(vals)," vals from ",line)
        #msg.linear.x= float(vals[0])
        msg.linear.x= float(vals[0]) * 4 * 0.02040816 * 0.0508 * 2 * 3.14
        msg.angular.z= float(vals[1])
        #g_node.get_logger().info('Serial Rx: %s'%str(line))
        publisher.publish(msg)
        rate.sleep()

    #node.destroy_node()
    #rclpy.shutdown()

if __name__ == '__main__':
    main()
