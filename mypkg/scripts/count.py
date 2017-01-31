#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

def Fibonacci(i):
    if i<= 2:
        return 1
    else:
        return Fibonacci(i-1)+Fibonacci(i-2)

if __name__=='__main__':
    rospy.init_node('count')
    pub = rospy.Publisher('count_up', Int32, queue_size=1)
    rate = rospy.Rate(1)
    n = 0
    i = 0
    while not rospy. is_shutdown():
        i += 1
        n = Fibonacci(i)
        pub.publish(n)
        rate.sleep()
