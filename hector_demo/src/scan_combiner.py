#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan


def callback(data):
    global min_angle, max_angle, heard, angles, start_angles, ranges, pub
    rospy.loginfo("I heard %s", data.header.seq)
    min_angle = min(min_angle, data.angle_min)
    max_angle = max(max_angle, data.angle_max)
    heard += 1
    print(heard)
    angles[data.angle_min] = len(data.ranges)
    if heard <= 10:
        print("waiting for 10 messages")
        total_length = sum(angles.values())
        start_angles = sorted(angles.keys())
        ranges = [0] * total_length
    else:
        print(angles)
        print(start_angles)
        i = start_angles.index(data.angle_min)
        print(i)
        ranges[i*250:len(data.ranges)+i*250] = data.ranges

        data.ranges = ranges
        data.angle_min = min_angle
        data.angle_max = max_angle
        data.intensities = []
        pub.publish(data)


if __name__ == "__main__":
    min_angle = 100
    max_angle = 0
    heard = 0
    angles = {}
    start_angles = []
    ranges = []
    pub = rospy.Publisher("scan_combined", LaserScan)

    rospy.init_node('node_name')
    i = 0
    rospy.Subscriber("scan", LaserScan, callback)
    rospy.spin()
