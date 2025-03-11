import cv2
import numpy as np
import os
import handtracking as htm

brushThickness=15
eraserThickness=100

# Load header images
folderPath = "Header"
MyList = os.listdir(folderPath)
print(MyList)

overlayList = [cv2.imread(f'{folderPath}/{imPath}') for imPath in MyList]
print(len(overlayList))

header = overlayList[0]  
drawColor=(255,0,255)


# Initialize camera
cam = cv2.VideoCapture(0)
cam.set(3, 1280)  # Width
cam.set(4, 720)   # Height

# Initialize hand detector
detector = htm.handDetector(detectionCon=0.6)
x1,x2,y1,y2=0,0,0,0
xp,yp=0,0
imageCanvas=np.zeros((720,1280,3),np.uint8)

while True:
    # Capture frame
    success, img = cam.read()
    img = cv2.flip(img, 1)

    # Detect hands
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)[0]

    if len(lmList)>12:
        # Tip of index and middle finger
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

    # Detect which fingers are up
    fingers = detector.fingersUp()
    # print("Fingers Up:", fingers)  # Debugging Output

    if len(fingers)==5:
    # Selection Mode: Both index & middle fingers up
        if fingers[1] == 1 and fingers[2] == 1 and abs(x2 - x1) <= 50:
            xp,yp=0,0
            print("Selection mode")
            # print(lmList[8][1:])
            
            if y1 < 125:
                if 250 < x1 < 450:
                    header = overlayList[0]
                    drawColor = (255, 0, 255)
                elif 550 < x1 < 750:
                    header = overlayList[1]
                    drawColor = (255, 0, 0)
                elif 800 < x1 < 950:
                    header = overlayList[2]
                    drawColor = (0, 255, 0)
                elif 1050 < x1 < 1200:
                    header = overlayList[3]
                    drawColor = (0,0,0)
            cv2.rectangle(img, (x1, y1 - 30), (x2, y2 + 30),drawColor, cv2.FILLED)

        # Drawing Mode: Only index finger up
        if fingers[1] == 1 and fingers[2] == 0:
            cv2.circle(img, (x1, y1), 10, drawColor , cv2.FILLED)
            
            print("Drawing mode")
            # print(x1,x2,y1,y2)
                
            if xp==0 and yp ==0:
                xp,yp=x1,y1
            
            if drawColor==(0,0,0):
                cv2.line(img,(xp,yp),(x1,y1),drawColor,eraserThickness,cv2.FILLED)
                cv2.line(imageCanvas,(xp,yp),(x1,y1),drawColor,eraserThickness,cv2.FILLED)
            else:
                cv2.line(img,(xp,yp),(x1,y1),drawColor,brushThickness,cv2.FILLED)
                cv2.line(imageCanvas,(xp,yp),(x1,y1),drawColor,brushThickness,cv2.FILLED)

            xp , yp = x1, y1



    imgGray = cv2.cvtColor(imageCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv,cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img,imgInv)
    img = cv2.bitwise_or(img,imageCanvas)

    # Set the header image
    img[0:125, 0:1280] = header
    # img=cv2.addWeighted(img,0.5,imageCanvas,0.5,0)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    cv2.imshow("Image", img)
    # cv2.imshow("Canvas", imageCanvas)
    cv2.waitKey(1)
