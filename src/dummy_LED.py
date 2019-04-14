#! /usr/bin/env python
# coding:utf-8
import sys
import time

import rospy
from std_msgs.msg import Bool, String

class DummyLED:
    def __init__(self):
        self.sub_bool = rospy.Subscriber("/publisher_tutorial/led_on", Bool, self.sub_bool_callback)
        self.sub_led_color = rospy.Subscriber("/publisher_tutorial/led_color", String, self.sub_led_color_callback)

        self.led_on = True
        self.led_color = "RED"

    def sub_bool_callback(self, msg):
        self.led_on = msg.data

    def sub_led_color_callback(self, msg):
        self.led_color = str(msg.data).upper()

    def console(self, led_color):
        if led_color == "BLACK":
            return "\033[30m" + "● ● ● ● ● 　" + "\033[0m"

        elif led_color == "RED":
            return "\033[31m" + "● ● ● ● ● 　" + "\033[0m"

        elif led_color == "GREEN":
            return "\033[32m" + "● ● ● ● ● 　" + "\033[0m"

        elif led_color == "YELLOW":
            return "\033[33m" + "● ● ● ● ● 　" + "\033[0m"

        elif led_color == "BLUE":
            return "\033[34m" + "● ● ● ● ● 　" + "\033[0m"

        elif led_color == "PURPLE":
            return "\033[35m" + "● ● ● ● ● 　" + "\033[0m"

        elif led_color == "CYAN":
            return "\033[36m" + "● ● ● ● ● 　" + "\033[0m"

        else: #WHITE
            return "\033[37m" + "● ● ● ● ● 　" + "\033[0m"

    def main(self):
        while not rospy.is_shutdown():
            try:
                if self.led_on == True:
                    sys.stdout.write("\r"+self.console(self.led_color))
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
