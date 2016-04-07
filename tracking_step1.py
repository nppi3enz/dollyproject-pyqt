# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import imutils

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (480, 320)
#camera.ISO = 100
#camera.brightness = 65
#camera.contrast = 50
camera.exposure_mode = 'fixedfps'
#camera.framerate = 32
camera.rotation = 180
rawCapture = PiRGBArray(camera, size=(480, 320))

min_area = 500000

fgbg = cv2.createBackgroundSubtractorMOG2()
#fgbg.setShadowThreshold(200)

# allow the camera to warmup
time.sleep(0.1)

firstFrame = None

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array
    image = imutils.resize(image, width=480)
    text = "Unoccupied"

    # show the frame
    cv2.imshow("Original", image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    cv2.imshow('bgSubtractor',gray)

    if firstFrame is None:
        firstFrame = gray

    frameDelta = cv2.absdiff(firstFrame, gray)
    thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

    thresh = cv2.dilate(thresh, None, iterations=2)
    (_, cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    max_area = 0
    for c in cnts:
        print ("Area: "+str(cv2.contourArea(c)))
        if cv2.contourArea(c) > 5000 and cv2.contourArea(c) < min_area and cv2.contourArea(c) > max_area:
            max_area = cv2.contourArea(c)
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            text = "Occupied"

    #qcv2.putText(frame, "Room Status: {}".format(text),(10, 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.imshow("Security Feed", image)
    cv2.imshow("Thresh", thresh)
    cv2.imshow("Frame Delta", frameDelta)

    key = cv2.waitKey(1) & 0xFF

    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break


cv2.imwrite("result.jpg", fgmask)

#output = fgmask.copy()
#output, contours, hierarchy = cv2.findContours(output, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#cv2.drawContours(output,contours,-1,(0,255,0),3)
#cv2.imshow("Detect", output)

cv2.waitKey(0)
cv2.destroyAllWindows()
