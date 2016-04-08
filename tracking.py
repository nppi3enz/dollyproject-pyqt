#---------- VERSION 3-------------
# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import imutils
import numpy as np

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (480, 320)
#camera.ISO = 100
#camera.brightness = 65
#camera.contrast = 50
camera.exposure_mode = 'fixedfps'
#camera.framerate = 32
camera.rotation = 90
rawCapture = PiRGBArray(camera, size=(480, 320))

min_area = 500000

fgbg = cv2.createBackgroundSubtractorMOG2()
# allow the camera to warmup
time.sleep(0.1)

firstFrame = None
mode = 1
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    if mode == 1:
        textMode = "Object Detection"
        # grab the raw NumPy array representing the image, then initialize the timestamp
        # and occupied/unoccupied text
        image = frame.array
        image = imutils.resize(image, width=480)
        text = "Not Ready"
        fgmask = fgbg.apply(image)
        # show the frame
        #cv2.imshow("Original", image)
        cv2.imshow("Mask", fgmask)

        thresh = fgmask.copy()
        (_, cnts, _) = cv2.findContours(thresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        for c in cnts:
            #print ("Area: "+str(cv2.contourArea(c)))
            if cv2.contourArea(c) > 10000:
                max_area = cv2.contourArea(c)
                (x, y, w, h) = cv2.boundingRect(c)
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                text = "Ready"
                selectX = x
                selectY = y
                selectWidth = w
                selectHeight = h

        key = cv2.waitKey(1) & 0xFF
        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            print("NEXT")
            mode = 2
            #break
    elif mode == 2:
        textMode = "Object Tracking"
        image = frame.array

        # setup initial location of window
        r,h,c,w = 250,90,400,125  # simply hardcoded the values
        #c,r,w,h = selectX, selectY, selectWidth, selectHeight
        track_window = (c,r,w,h)

        # set up the ROI for tracking
        roi = image[r:r+h, c:c+w]
        hsv_roi =  cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
        roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
        cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)

        # Setup the termination criteria, either 10 iteration or move by atleast 1 pt
        term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )

        while(1):
            #ret ,frame = cap.read()
            image = frame.array

            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)

            # apply meanshift to get the new location
            ret, track_window = cv2.CamShift(dst, track_window, term_crit)

            # Draw it on image
            pts = cv2.boxPoints(ret)
            pts = np.int0(pts)
            img2 = cv2.polylines(image,[pts],True, 255,2)
            cv2.imshow('img2',img2)

        key = cv2.waitKey(1) & 0xFF
        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break

    cv2.putText(image, "Mode: {}".format(textMode),(10, 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
    cv2.putText(image, "Status: {}".format(text),(10, 40),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
    cv2.putText(image, "("+str(selectX)+" , "+str(selectY)+") Width: "+str(selectWidth)+" Height: "+str(selectHeight),(10, 300),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
    cv2.imshow("Object Detection", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
