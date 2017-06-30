from picamera.array import PiRGBArray
from picamera import PiCamera
from PiStorms import PiStorms
import cv2
import sys,os
import imutils
import numpy as np
import argparse,time

import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)

psm = PiStorms()

class icontracker:
    training = {}
    version  = ''
    ## generate the images dictoneary and store it it memory
    ##each image is 200x200
    def __init__(self):
        self.training = self.get_training()
        self.version = '1.00'

    def get_training(self):
        path = currentdir
        training = {}
        files = os.listdir(path)
        files_png = [i for i in files if i.endswith('.png')]
        print "files_png: ", files_png
        #print len(files_png),'images found'
        for file in files_png  :
            imR = cv2.imread(currentdir+"/"+file)
            #width = imR.shape[0]
            #height = imR.shape[1]
            #r = 200.0 / height
            #dim = (200, int(imR.shape[0] * r))
            # perform the actual resizing of the image and show it
            #imR = self.preprocess(cv2.resize(imR, (100,100), interpolation =cv2.INTER_AREA))
            imR = self.preprocess(imR)
            training[file] = imR

        return training

    # Captures a single image from the camera and returns it in PIL format
    def get_image(self,camera):
        # read is the easiest way to get a full image out of a VideoCapture object.
        retval, im = camera.read()
        return im

    ###############################################################################
    # Image Matching
    ###############################################################################
    def preprocess(self,img):
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray,(5,5),5 )
        thresh = cv2.adaptiveThreshold(blur,255,1,1,11,1)
        return thresh

    def imgdiff(self,img1,img2):

        img1 = cv2.GaussianBlur(img1,(5,5),5)
        img2 = cv2.GaussianBlur(img2,(5,5),5)
        diff = cv2.absdiff(img1,img2)
        diff = cv2.GaussianBlur(diff,(5,5),5)
        flag, diff = cv2.threshold(diff, 200, 255, cv2.THRESH_BINARY)
        return np.sum(diff)

    def find_closest_card(self,training,img):
        features = preprocess(img)
        return sorted(training.values(), key=lambda x:imgdiff(x[1],features))[0][0]

    def findSquare( self,frame ):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (7, 7), 0)
        edged = cv2.Canny(blurred, 60, 60)
        # find contours in the edge map
        (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # loop over our contours to find hexagon
        cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:50]
        screenCnt = None
        for c in cnts:
            # approximate the contour
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.004 * peri, True)
            # if our approximated contour has four points, then
            # we can assume that we have found our squeare

            if len(approx) >= 4:
                screenCnt = approx
                x,y,w,h = cv2.boundingRect(c)
                cv2.drawContours(image, [approx], -1, (0, 0, 255), 1)
                #cv2.imshow("Screen", image)
                #create the mask and remove rest of the background
                mask = np.zeros(image.shape[:2], dtype = "uint8")
                cv2.drawContours(mask, [screenCnt], -1, 255, -1)
                masked = cv2.bitwise_and(image, image, mask = mask)
                #cv2.imshow("Masked",masked  )
                #crop the masked image to to be compared to referance image
                cropped = masked[y:y+h,x:x+w]
                #scale the image so it is fixed size as referance image
                cropped = cv2.resize(cropped, (200,200), interpolation =cv2.INTER_AREA)

                return cropped


    def locate_target( self,frame ):
        #find the square logo image from our image
        self.target = self.preprocess( self.findSquare(frame))
        #cv2.imshow('target',self.target)
        #cv2.waitKey(0)
        #print 'target', target.shape
        return self.target

    def identify_target( self,frame ):
        results = {}
        for file in self.training :
            results[file] = self.imgdiff(self.locate_target(frame),self.training[file])

        #x = min(results, key=results.get)
        #min(min(e) for e in E if e)
        x = min (((e) for e in results if e), key=results.get)
        return x


if __name__ == '__main__':

    icon = icontracker()
    print icon.training
    print icon.version
    #camera_port = 0
    # Now we can initialize the camera capture object with the cv2.VideoCapture class.
    # All it needs is the index to a camera port.
    #camera = cv2.VideoCapture(camera_port)

    try:
        camera = PiCamera()
    except:
         m = ["Icon Tracker", "Camera not enabled.", "Run raspi-config and enable camera"]
         psm.screen.askQuestion(m,["OK"])
         exit()
    #camera.resolution = (640, 480)
    #rawCapture = PiRGBArray(camera, size=(640, 480))
    camera.resolution = (320, 240)
    rawCapture = PiRGBArray(camera, size=(320, 240))
    #camera.resolution = (160, 120)
    #rawCapture = PiRGBArray(camera, size=(160, 120))
    camera.framerate = 30
    #Number of frames to throw away while the camera adjusts to light levels
    #ramp_frames = 30

    # Ramp the camera - these frames will be discarded and are only used to allow v4l2
    # to adjust light levels, if necessary
    '''
    for i in xrange(ramp_frames):
        temp = icon.get_image(camera)
    '''
    i =0
    lasttime = time.time()
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # grab the raw NumPy array representing the image, then initialize the timestamp
        # and occupied/unoccupied text

        i = i+1
        image = frame.array
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        print i
        #image = icon.get_image(camera)
        #cv2.imshow('captured image',image)
        #cv2.waitKey(0)

        '''
        #find the square logo image from our image
        target = icn.preprocess( icn.findSquare(image))
        cv2.imshow('target',target)
        cv2.waitKey(0)
        print 'target', target.shape

        results = {}
        for file in icn.training :
            results[file] = icn.imgdiff(target,icn.training[file])

        print min(results, key=results.get)
        '''
        img = icon.identify_target(image)
        print "identified: " , img

        psm.screen.termPrintAt(7, "count: " + str(i))
        psm.screen.termPrintAt(8, "identified: " + str(img))
        print 1000*(time.time() - lasttime)
        lasttime = time.time()
        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)
        if(psm.isKeyPressed()):
                psm.screen.clearScreen()
                psm.screen.termPrintAt(9, "Exiting to menu")
                time.sleep(0.5)
                quit()

        #cv2.waitKey(0)
    # You'll want to release the camera, otherwise you won't be able to create a new
    # capture object until your script exits
    #del(camera)
