# ECE 5730 - Robotics
# navigation.py - Nav control node to send velocity to motor control node.

# Import libraries.
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class Navigation(Node):
    """
    Navigation node for robotic system.
    """

    def __init__(self):
        # Create Navigation node.
        super().__init__('navigation')
        # Define and initialize variables for motor control use.
        self.keyboard_vx = 0.0
        self.keyboard_vtheta = 0.0
        # Create publisher node for target velocity of motor control.
        self.publisher_ = self.create_publisher(Twist, 'target_vel', 10)
        # Send messages every 10 Hz
        timer_period = 0.1  # seconds 
        self.timer = self.create_timer(timer_period, self.publish_motor_control)
        # Create subscriber node to a 'platform_vel' topic and expects a Twist message.
        self.subscription_motor_control = self.create_subscription(
            Twist,
            'platform_vel',
            self.motor_control_callback,
            10)
        self.subscription_motor_control  # prevent unused variable warning
        # Create subscriber node to a 'cmd_vel' topic and expects a Twist message.
        self.subscription_keyboard = self.create_subscription(
            Twist,
            'cmd_vel',  # Topic of teleop_twist_keyboard node.
            self.keyboard_callback,
            10)
        self.subscription_keyboard  # prevent unused variable warning

    def publish_motor_control(self):
        # Publish a twist message.
        msg = Twist()
        msg.linear.x = float(self.keyboard_vx)
        msg.angular.z = float(self.keyboard_vtheta)
        self.publisher_.publish(msg)
        self.get_logger().info('(Vx: "%4.2f", Vtheta: "%2.2f")' % (msg.linear.x, msg.angular.z))

    def motor_control_callback(self, msg):
        """
        Recieves current platform velocity.
        """
        #self.get_logger().info('Arduino sent: Linear: "%.2f", Angular: "%.2f"' % (msg.linear.x, msg.angular.z))

    def keyboard_callback(self, msg):
        """
        Assigns the recieved message from the keyboard into class variables.
        """
        self.keyboard_vx = msg.linear.x
        self.keyboard_vtheta = msg.angular.z

def main(args=None):
    # Initialize rclpy
    rclpy.init(args=args)
    try:
        # Navigation node.
        navigation = Navigation()
        try:
            # Run Navigation node.
            rclpy.spin(navigation)
        except KeyboardInterrupt:
            pass
        finally:
            # Clean navigation node.
            navigation.destroy_node()
    finally:
        rclpy.shutdown()
        print("\nProgram closed successfully.")

if __name__ == '__main__':
    main()
