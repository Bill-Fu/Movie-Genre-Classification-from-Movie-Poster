import subprocess
import os

subprocess.call(["cd", "/home/ubuntu/notebooks/darknet/darknet"])
result = subprocess.check_output(["/home/ubuntu/notebooks/darknet/darknet", 
                                  "detect", 
                                  "/home/ubuntu/notebooks/darknet/cfg/yolo.cfg", 
                                  "/home/ubuntu/notebooks/darknet/yolo.weights", 
                                  "/home/ubuntu/notebooks/darknet/data/horses.jpg"])

print(result)
