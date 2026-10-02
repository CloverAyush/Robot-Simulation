import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32

class DecisionNode(Node):
    def __init__(self):
        super().__init__('decision_node')

        self.decision_publisher= self.create_publisher(Twist, '/cmd_vel', 10)

        self.distance_subscriber= self.create_subscription(Float32, '/distance', self.distance_callback, 10)

    def distance_callback(self, msg):
        distance= msg.data
        self.make_decision(distance)

    def make_decision(self, distance):
        cmd_msg= Twist()

        if distance < 1.0:
            cmd_msg.linear.x = 0.5
            cmd_msg.angular.z = 1.0
        else:
            cmd_msg.linear.x= 1.0
            cmd_msg.angular.z= 0.0

        self.decision_publisher.publish(cmd_msg)

def main(args=None):
    rclpy.init(args=args)

    decision = DecisionNode()

    rclpy.spin(decision)

    decision.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()