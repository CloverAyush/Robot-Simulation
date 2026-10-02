import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose2D
import math

class Robot(Node):
    def __init__(self):
        super().__init__('robot_simulator')
        #position and heading of the robot
        self.x = 0
        self.y = 0
        self.heading = math.pi/2

        #velocity and angular velocity
        self.vel = 0
        self.omega = 0

        self.cmd_subscriber= self.create_subscription(Twist, '/cmd_vel', self.cmd_vel_callback, 10)

        self.pose_publisher = self.create_publisher(Pose2D, '/pose', 10)

        self.timer= self.create_timer(0.1, self.update_state)

    def cmd_vel_callback(self, msg):
        self.vel= msg.linear.x
        self.omega= msg.angular.z
    
    def update_state(self):

        dt= 0.1 #time step for the sim

        #update the state of the robot

        self.x+= self.vel*math.cos(self.heading)*dt
        self.y+= self.vel*math.sin(self.heading)*dt
        self.heading+= self.omega*dt

        #publish the updated pose
        pose= Pose2D()
        pose.x= self.x
        pose.y= self.y
        pose.theta= self.heading
        self.pose_publisher.publish(pose)

def main(args=None):
    rclpy.init(args=args)

    robot = Robot()

    rclpy.spin(robot)

    robot.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()