#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16
from sensor_msgs.msg import Joy

def left_callback(data):
	temp_int = 255 * data.axes[1]
	pub_left.publish(temp_int)
	temp_int = 255 * data.axes[5]
	pub_right.publish(temp_int)

# support for two joysticks
# def right_callback(data):
#	temp_int = 255 * data.axes[1]
#	pub_left.publish(temp_int)

    # Intializes everything
def start():
	# publishing to "turtle1/cmd_vel" to control turtle1
	global pub_left
	global pub_right
	rospy.init_node('Joy2Test')
	pub_right = rospy.Publisher('rightWheel', Int16, queue_size=1)
	pub_left = rospy.Publisher('leftWheel', Int16, queue_size=1)
	# subscribed to joystick inputs on topic "joy"
	rospy.Subscriber("left_stick", Joy, left_callback)
	# starts the node
	rospy.spin()

if __name__ == '__main__':
	start()
    
