import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose2D
from std_msgs.msg import Float32

class SensorNode(Node):
    def __init__(self):
        super().__init__('sensor_node')
 
        self.obstacle_x= 0.0
        self.obstacle_y= 5.0

        self.robot_x= 0.0
        self.robot_y= 0.0
   
        self.pose_subscriber= self.create_subscription(Pose2D, '/pose', self.pose_callback, 10)
        self.distance_publisher= self.create_publisher(Float32, '/distance', 10)

       

    def pose_callback(self, msg):
        self.robot_x= msg.x
        self.robot_y= msg.y
        self.calc_distance()

    def calc_distance(self):
        distance= ((self.robot_x- self.obstacle_x)**2 + (self.robot_y- self.obstacle_y)**2)**0.5
        
        distance_msg= Float32()
        distance_msg.data= distance
        self.distance_publisher.publish(distance_msg)

def main(args=None):
    rclpy.init(args=args)

    sensor = SensorNode()

    rclpy.spin(sensor)

    sensor.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()