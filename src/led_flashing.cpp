#include "ros/ros.h"
#include "std_msgs/Bool.h"

int main(int argc, char **argv){
  ros::init(argc, argv, "led_flashing");
  ros::NodeHandle nh;
  ros::Publisher publisher = nh.advertise<std_msgs::Bool>("/publisher_tutorial/led_state", 1);
  ros::Rate sleep_time(1);

  bool state;
  std_msgs::Bool msg;

  while (ros::ok()){
    ROS_INFO("ON");
    state = true;
    msg.data = state;
    publisher.publish(msg);
    sleep_time.sleep();

    ROS_INFO("OFF");
    state = false;
    msg.data = state;
    publisher.publish(msg);
    sleep_time.sleep();
  }

  return 0;

}
