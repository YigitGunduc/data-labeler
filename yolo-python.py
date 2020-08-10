"""
Created on July 18 2020
@author: Yigit GUNDUC
"""

import numpy as np
import cv2
import matplotlib.pylab as plt
import time as t

path = "PATH"

# Loading Yolo
net = cv2.dnn.readNet(path + "yolov3.weights",path + "yolov3.cfg")
classes = []
with open(path + "coco.names" ,"r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1 ] for i in net.getUnconnectedOutLayers()]

# Loading image
#img = cv2.imread("C:/Users/gunduc/Desktop/projepy/street.jpg")
cap = cv2.VideoCapture("Video PATH")

while True:
    _, img = cap.read()
    height, width, channels = img.shape


    # Dedecting objects 
    blob = cv2.dnn.blobFromImage(img,1/255,(416,416),(0,0,0),True,crop=False)

    class_ids = []
    confidences = []
    boxes = []
    for b in blob:
        for n, img_blob in enumerate(b):
            cv2.imshow(str(n),img_blob)
    
    net.setInput(blob)
    outs = net.forward(output_layers)
  
    # Showing info on the screen
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                # Object dedected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                
                # Rectangle Coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)


    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    font = cv2.FONT_HERSHEY_SIMPLEX
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            cv2.rectangle(img, (x, y), (x + w, y + h), (0,255,0), 2)
            cv2.rectangle(img, (x, y), (x +50, y - 20), (255,0,255), cv2.FILLED)
            cv2.putText(img, label, (x, y-5), font, 0.5, (0, 0, 0), 2)


   
    # Showing image
    cv2.imshow("car",img)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    t.sleep(10)
VideoOutPut.releas()
cap.release()
cv2.destroyAllWindows()
