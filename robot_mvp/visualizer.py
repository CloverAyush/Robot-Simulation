import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose2D
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist


class Visualizer(Node):
    def __init__(self):
        super().__init__('visualizer')

        self.x = 0.0
        self.y = 0.0
        self.heading = 0.0
        self.distance = 0.0
        self.speed = 0.0
        self.turn_rate = 0.0

        self.create_subscription(
            Pose2D,
            '/pose',
            self.pose_callback,
            10
        )

        self.create_subscription(
            Float32,
            '/distance',
            self.distance_callback,
            10
        )

        self.create_subscription(
            Twist,
            '/cmd_vel',
            self.cmd_callback,
            10
        )

        self.timer = self.create_timer(1.0, self.display)

    def pose_callback(self, msg):
        self.x = msg.x
        self.y = msg.y
        self.heading = msg.theta

    def distance_callback(self, msg):
        self.distance = msg.data

    def cmd_callback(self, msg):
        self.speed = msg.linear.x
        self.turn_rate = msg.angular.z

    def display(self):
       if self.speed >0  and  self.turn_rate == 0:
        action = "MOVING FORWARD"
       elif self.turn_rate > 0 and self.speed >= 0:
        action = "TURNING and MOVING"
       else:
        action = "STOPPED"

       self.get_logger().info(
        f"ROBOT | "
        f"Position=({self.x:.2f}, {self.y:.2f}) m | "
        f"Distance={self.distance:.2f} m | "
        f"Speed={self.speed:.2f} m/s | "
        f"Turn={self.turn_rate:.2f} rad/s | "
        f"Action={action}"
    )

def main(args=None):
    rclpy.init(args=args)

    node = Visualizer()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()