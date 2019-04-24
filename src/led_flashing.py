#! /usr/bin/env python
# coding:utf-8

import rospy
import time
from std_msgs.msg import Bool

if __name__ == "__main__":
    rospy.init_node("led_flashing", anonymous=True)
    publisher = rospy.Publisher("/publisher_tutorial/led_on", Bool, queue_size=1)

    while not rospy.is_shutdown():
        try:
            publisher.publish(True)
            time.sleep(1)

            publisher.publish(False)
            time.sleep(1)

        except KeyboardInterrupt: #Ctrl+cが入力された
            print "Ctrl+c"
            break
