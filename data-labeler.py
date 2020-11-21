import os
import numpy as np
import cv2
from tqdm import tqdm
from PIL import Image 
import matplotlib.pylab as plt
import time as t


print("""
      _       _             _       _          _           
     | |     | |           | |     | |        | |          
   __| | __ _| |_ __ _     | | __ _| |__   ___| | ___ _ __ 
  / _` |/ _` | __/ _` |    | |/ _` | '_ \ / _ \ |/ _ \ '__|
 | (_| | (_| | || (_| |    | | (_| | |_) |  __/ |  __/ |   
  \__,_|\__,_|\__\__,_|    |_|\__,_|_.__/ \___|_|\___|_|   
                                                         """)

#----------------------------------------------------------------------
# Paths

dirname = os.path.dirname(__file__)
out = 'labeled_data/'
path = 'raw_data/'
yolo_path = 'yolo/'


#-----------------------------------------------------------------------
# Loading Yolo
try:
    net = cv2.dnn.readNet(yolo_path + "yolov3.weights",yolo_path + "yolov3.cfg")
    classes = []
    with open(yolo_path + "coco.names" ,"r") as f:
        classes = [line.strip() for line in f.readlines()]
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0] - 1 ] for i in net.getUnconnectedOutLayers()]
    print("Yolo loaded succesfuly")
except:
    print("=> Exception happened while loading yolo please check your 'yolo_path' variable")

#-----------------------------------------------------------------------
# Creat folders according to the classes
try:
    for i in range(len(classes)):
        os.mkdir(out + str(classes[i]))
except OSError:
        print("files already exist or permission denied")
#------------------------------------------------------------------------
# labels the data
def label_data(path):
    for image_path in tqdm(os.listdir(path)):
        image_path = f'raw_data/{image_path}'
        print(image_path)
        img  = cv2.imread(image_path)
        
        height, width, channels = img.shape


        # Dedecting objects 
        blob = cv2.dnn.blobFromImage(img,1/255,(416,416),(0,0,0),True,crop=False)

        class_ids = []
        confidences = []
        boxes = []
        for b in blob:
            for n, img_blob in enumerate(b):
                pass
        
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
                crop_img = img[y:y+h, x:x+w]
                try:
                    cv2.imwrite(f"labeled_data/{label}/{np.random.random()}.jpg",crop_img)
                except:
                    pass

def main():
    label_data(path)

main()