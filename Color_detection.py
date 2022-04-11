import cv2 
import numpy as np
import pandas as pd
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i","--Image",required=True,help="Image Path")
#python Color_detection.py -i Image.jpg
args = vars(ap.parse_args())
img_path = args["Image"]
img = cv2.imread(img_path)
#diciton globle var
click = False
r = g = b = xpos = ypos = 0
#reading csv file
index = ["color","color_name","hex","R","G","B"]
csv =pd.read_csv("colors.csv",names=index,header=None)


def getColorrName(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R-int(csv.loc[i,"R"])) +abs(G-int(csv.loc[i,"G"])) + abs(B-int(csv.loc[i,"B"]))
        if d <= minimum:
            minimum = d 
            cname = csv.loc[i,"color_name"]
    return cname

def draw_function(event,x,y,flags,parmam):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos,click
        click = True 
        xpos = x
        ypos = y 
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)

cv2.namedWindow("image")
cv2.setMouseCallback("image",draw_function)

while(1):
    cv2.imshow("image",img)
    if click == True:
        cv2.rectangle(img,(20,20),(750,60),(b,g,r),-1)
        text = getColorrName(r,g,b) + " R = "+str(r) + " G = "+str(g) + " B = "+str(b)
        cv2.putText(img,text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
        if(r+g+b>= 600):
            cv2.putText(img,text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
        click = False
        
    if cv2.waitKey(20) & 0xFF == "q":
        break
cv2.destroyAllWindows()        
        
