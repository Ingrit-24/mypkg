import rclpy
from rclpy.node import Node
from person_msgs.srv import Query #使う型を変更
  
rclpy.init()
node = Node("talker")


def cb(request, response):
    if request.name == "コピペマン":
        response.age = 19 
    else:
        response.age = 530000

    return response 
 
def main():
    srv = node.create_service(Query, "query", cb) #サービスの作成                     
    rclpy.spin(node)
