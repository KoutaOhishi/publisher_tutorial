#! /usr/bin/env python
# coding:utf-8
import sys
import time

import rospy
from std_msgs.msg import Bool, String

class DummyLED:
    def __init__(self):
        self.sub_bool = rospy.Subscriber("/publisher_tutorial/led_state", Bool, self.sub_bool_callback)
        self.sub_color = rospy.Subscriber("/publisher_tutorial/color", String, self.sub_color_callback)

        self.led_state = False
        self.color = "WHITE"

    def sub_bool_callback(self, msg):
        self.led_state = msg.data

    def sub_color_callback(self, msg):
        self.color = str(msg.data).upper()

    def console(self, color):
        if color == "BLACK":
            return "\033[30m" + "● ● ● ● ● 　" + "\033[0m"

        elif color == "RED":
            return "\033[31m" + "● ● ● ● ● 　" + "\033[0m"

        elif color == "GREEN":
            return "\033[32m" + "● ● ● ● ● 　" + "\033[0m"

        elif color == "YELLOW":
            return "\033[33m" + "● ● ● ● ● 　" + "\033[0m"

        elif color == "BLUE":
            return "\033[34m" + "● ● ● ● ● 　" + "\033[0m"

        elif color == "PURPLE":
            return "\033[35m" + "● ● ● ● ● 　" + "\033[0m"

        elif color == "CYAN":
            return "\033[36m" + "● ● ● ● ● 　" + "\033[0m"

        else: #WHITE
            return "\033[37m" + "● ● ● ● ● 　" + "\033[0m"

    def main(self):
        while not rospy.is_shutdown():
            try:
                if self.led_state == True:
                    sys.stdout.write("\r"+self.console(self.color))
                    sys.stdout.flush()
                    time.sleep(0.1)

                else:
                    sys.stdout.write("\r　   　 　　")
                    sys.stdout.flush()
                    time.sleep(0.1)

            except KeyboardInterrupt:
                break


if __name__ == "__main__":
    rospy.init_node("dummy_led")

    print "--- DummyLED ---"
    c = DummyLED()
    c.main()
    print "\n"
