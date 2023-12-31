# SPDX-FileCopyrightText: 2023 Haruki Matsushita
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

def cb(msg):
    global node
    node.get_logger().info("Answer: %d" % (msg.data * msg.data * 12 + 34))

rclpy.init()
node = Node("listener")
pub = node.create_subscription(Int16, "countup", cb, 10)
rclpy.spin(node)
