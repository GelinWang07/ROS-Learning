 #!/usr/bin/env python
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
import rospy
import math 



class GoalPublisher(object):


    def __init__(self,goalx,goaly,color,id):
        """ Initialize the goal publisher node."""

        self._point_pub = rospy.Publisher('/visualization_marker_array', MarkerArray,queue_size=1)
        self.goalx = goalx
        self.goaly = goaly
        self.color = color
        self.id = id
        
        markerArray = MarkerArray()
        marker = Marker()
        if(color[1]==1.0):
            rate = rospy.Rate(0.2)
            rate.sleep()
        for i in range(len(goalx)):
            marker.header.frame_id = "/odom"
            marker.type = marker.SPHERE
            marker.action = marker.ADD
            marker.scale.x = 0.2
            marker.scale.y = 0.2
            marker.scale.z = 0.2
            marker.color.a = 1.0
            marker.color.r = color[0]
            marker.color.g = color[1]
            marker.color.b = color[2]
            marker.pose.orientation.w = 1.0
            marker.pose.position.x = goalx[i]
            marker.pose.position.y = goaly[i]
            marker.pose.position.z = 0
        
            markerArray.markers.append(marker)
 
            # Renumber the marker IDs
            #id = 0
            for m in markerArray.markers:
                m.id = self.id[i]
 
            # Publish the MarkerArray
            self._point_pub.publish(markerArray)
            rospy.sleep(0.01) 
        
