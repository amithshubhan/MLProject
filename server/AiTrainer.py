import cv2
import numpy as np
import time
from flask import Flask, render_template, Response
from sqlalchemy import between
import PoseModule as pm
cap = cv2.VideoCapture(0)
detector = pm.poseDetector()
count = 0
dir = 0
pTime = 0
bar = 0
angle1=0
angle2=0
left_tilt = 0
while True:
    success, img = cap.read()
    img = cv2.resize(img, (1460, 800))
    # img = cv2.imread("AiTrainer/test.jpg")
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)
    # print(lmList)
    if len(lmList) != 0:
        # Right Arm
        angle1 = detector.findAngle(img, 12, 14, 16)
        #Left Arm
        angle2 = detector.findAngle(img, 11, 13, 15)

        if(angle1<170 or angle2<170 ):
            left_tilt=1

        else:
            left_tilt=0

      

       

        if left_tilt:
            
            if angle1<angle2:
                per1 = np.interp(angle1, (50, 150), (100, 0))
                #per2 = np.interp(angle1, (210, 310), (0, 100))
                bar = np.interp(angle1, (50, 150), (100, 650))

                # print(angle, per)
                # Check for the dumbbell curls
                color = (255, 0, 255)
                if per1 == 100 :
                    color = (0, 255, 0)
                    if dir == 0:
                        count += 0.5
                        dir = 1
                        
                    
                    
                elif per1 == 0 :
                    color = (0, 255, 0)
                    if dir == 1:
                        count += 0.5
                        dir = 0
                        

                #print(count)
                # Draw Bar
                cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
                cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
                cv2.putText(img, f'{int(per1)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4,
                            color, 4)
                # Draw Curl Count
                cv2.rectangle(img, (0, 450), (250, 720), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15,
                            (255, 0, 0), 25)

        
            else:
                
                per2 = np.interp(angle2, (50, 150), (100, 0))
                bar = np.interp(angle2, (50, 150), (100, 650))
                #per2 = np.interp(angle2, (210, 310), (0, 100))
                # print(angle, per)
                # Check for the dumbbell curls
                color = (255, 0, 255)
                if per2 == 100 :
                    color = (0, 255, 0)
                    if dir == 0 :
                        count += 0.5
                        dir = 1
                    
                elif per2 == 0:
                    color = (0, 255, 0)
                    if dir == 1:
                        count += 0.5
                        dir = 0
                    
                #print(count)
                # Draw Bar
                cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
                cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
                cv2.putText(img, f'{int(per2)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4,
                            color, 4)
                # Draw Curl Count
                cv2.rectangle(img, (0, 450), (150, 720), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15,
                            (255, 0, 0), 25)

        else:
            if angle1>angle2:
                per1 = np.interp(angle1, (210, 310), (0,100))
                #per2 = np.interp(angle1, (210, 310), (0, 100))
                bar = np.interp(angle1, (210, 310), (650,100))
                # print(angle, per)
                # Check for the dumbbell curls
                color = (255, 0, 255)
                if per1 == 100 :
                    color = (0, 255, 0)
                    if dir == 0:
                        count += 0.5
                        dir = 1
                        
                    
                    
                elif per1 == 0 :
                    color = (0, 255, 0)
                    if dir == 1:
                        count += 0.5
                        dir = 0
                        
                #print(count)
                # Draw Bar
                cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
                cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
                cv2.putText(img, f'{int(per1)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4,
                            color, 4)
                # Draw Curl Count
                cv2.rectangle(img, (0, 450), (250, 720), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15,
                            (255, 0, 0), 25)
            else:
    
                per2 = np.interp(angle2, (210, 310), (0,100))
                bar = np.interp(angle2, (210, 310), ( 650,100))
                #per2 = np.interp(angle2, (210, 310), (0, 100))
                # print(angle, per)
                # Check for the dumbbell curls
                color = (255, 0, 255)
                if per2 == 100 :
                    color = (0, 255, 0)
                    if dir == 0 :
                        count += 0.5
                        dir = 1
                    
                elif per2 == 0:
                    color = (0, 255, 0)
                    if dir == 1:
                        count += 0.5
                        dir = 0
                    
                #print(count)
                # Draw Bar
                cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
                cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
                cv2.putText(img, f'{int(per2)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4,
                            color, 4)
                # Draw Curl Count
                cv2.rectangle(img, (0, 450), (150, 720), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15,
                            (255, 0, 0), 25)

    else:
        count=0
        # Draw Curl Count
        cv2.rectangle(img, (0, 450), (150, 720), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15,
            (255, 0, 0), 25)
    print(angle1," ",angle2)   
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5,
                (255, 0, 0), 5)
    cv2.imshow("Image", img)
    cv2.waitKey(1)