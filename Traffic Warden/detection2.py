# calling all the files
from ultralytics import YOLO
import cv2 as cv
#logical variables
accident=False
emergency=False 
deadtraffic =1
#  calling the pretrained and trained model
# pretrained
model0=YOLO("yolov8n.pt")
# emergency trainde
model1=YOLO("best1.pt")
# accident trained
model2=YOLO("best.pt")

# giving the souce file from where we have to take the video for processing
source=("gettyimages-476361046-612x612.jpg")

# configuring the result of the modules by  selecting the classes and 

#  function for manging pretrained model 

def pretrainde():
   result0=model0.predict(source,show=True,stream=True,verbose=False,classes=[1,2,3,5])
   name=model0.names
   for r in result0:
        for c in r.boxes.cls:
            if (name[int(c)]=='car' or name[int(c)]=="truck" or name[int(c)]=="bike"):
                count=count+1
   return count             
               
          
# function for managing the emergency vehicles in the yolo

def emergency():
    result1=model1.predict(source,show=False,stream=True,verbose=False,conf=0.20)
    name=model1.names
    for r in result1:
        for c in r.boxes.cls:
            if name[int(c)]=='fire_tuck':
                # print("Emergency")
                emergency=True
                return emergency
            

# function for managing the accident that occures at the sqiares

def accident():
    result2=model2.predict(source,show=False,stream=True,verbose=False,conf=0.20)
    name=model2.names
    for r in result2:
        for c in r.boxes.cls:
             if (name[int(c)]=="Accident"):
                accident=True
                return accident


cv.waitKey(0)              