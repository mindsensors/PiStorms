#!/usr/bin/env python

from PiStorms import PiStorms
import MsDevices
import time

doExit = False
psm = PiStorms()

buttons = [[255,5,'blob'],
[255,45,'movie'],
[255,85,'c-mov'],
[255,125,'face'],
[255,205,'pict'],
[5,205,'qrcode'],
[70,205,'line'],
[135,205,'eye']
]

mode = 1

func = None

def doMovie(doInit):
    global func
    #func = doMovie
    if (doInit == True):
        psm.screen.termPrintAt(5, "doMovie init")
        cam.command(77)
        psm.screen.termPrintAt(6, "doMovie sleep(6)")
        time.sleep(6)
        func(True)

    psm.screen.termPrintAt(6, "doMovie loop - pass")
    pass


def doContinuousMovie(doInit):
    global func
    func = doContinuousMovie
    if (doInit == True):
        psm.screen.termPrintAt(5, "Cont-Movie init")
        cam.command(82)

    psm.screen.termPrintAt(6, "Cont-Movie loop sleep(2)")
    time.sleep(2)
    pass

def doQRCode(doInit):
    global func
    func = doQRCode
    if (doInit == True):
        psm.screen.termPrintAt(5, "qrcode tracking")
        cam.command(81)
        time.sleep(3)

    psm.screen.termPrintAt(6, "QRCode seen:")
    qrcode = cam.readString(0x42, 8)
    print "QRCode: " + str(qrcode)
    psm.screen.termPrintAt(7, qrcode)
    pass

def doPicture(doInit):
    global func
    if (doInit == True):
        psm.screen.termPrintAt(5, "doPicture init")
        cam.command(80)
        psm.screen.termPrintAt(6, "doPicture sleep(3)")
        time.sleep(3)
        func(True)

    psm.screen.termPrintAt(6, "doPicture loop - pass")
    pass

def doFace(doInit):
    global func
    func = doFace
    if (doInit == True):
        psm.screen.termPrintAt(5, "doFace init")
        cam.command(70)

    psm.screen.termPrintAt(6, "doFace loop")
    num = cam.getNumberObjects()
    if (num != None):
        #str = "blob count: %d" % num
        #psm.screen.termPrintAt(8, str)
        for i in range(num):
            blob = cam.getBlobs(i+1)
            if ( blob != 0):
                str = "Face: %d, %d, %d, %d, %d" % (blob.color, blob.left, blob.top, blob.right, blob.bottom)
                psm.screen.termPrintAt(7, str)
                drawBox(blob.left+5,blob.top+5,blob.right+5,blob.bottom+5)
            #if<
        #for<
    pass

def doEye(doInit):
    global func
    func = doLine
    if (doInit == True):
        psm.screen.termPrintAt(5, "doEye init")
        cam.command(76)  # object

    psm.screen.termPrintAt(6, "doEye loop")
    num = cam.getNumberObjects()
    if (num != None):
        #str = "blob count: %d" % num
        #psm.screen.termPrintAt(8, str)
        for i in range(num):
            blob = cam.getBlobs(i+1)
            if ( blob != 0):
                str = "Line: %d, %d, %d, %d, %d" % (blob.color, blob.left, blob.top, blob.right, blob.bottom)
                psm.screen.termPrintAt(7, str)
                drawBox(blob.left+5,blob.top+5,blob.right+5,blob.bottom+5)
            #if<
        #for<

def doLine(doInit):
    global func
    func = doLine
    if (doInit == True):
        psm.screen.termPrintAt(5, "doLine init")
        cam.command(76)  # object

    psm.screen.termPrintAt(6, "doLine loop")
    num = cam.getNumberObjects()
    if (num != None):
        #str = "blob count: %d" % num
        #psm.screen.termPrintAt(8, str)
        for i in range(num):
            blob = cam.getBlobs(i+1)
            if ( blob != 0):
                str = "Line: %d, %d, %d, %d, %d" % (blob.color, blob.left, blob.top, blob.right, blob.bottom)
                psm.screen.termPrintAt(7, str)
                drawBox(blob.left+5,blob.top+5,blob.right+5,blob.bottom+5)
            #if<
        #for<

def doBlob(doInit):
    global func
    func = doBlob
    if (doInit == True):
        psm.screen.termPrintAt(5, "doBlob init")
        cam.command(79)  # object

    psm.screen.termPrintAt(6, "doBlob loop")
    num = cam.getNumberObjects()
    if (num != None):
        #str = "blob count: %d" % num
        #psm.screen.termPrintAt(8, str)
        for i in range(num):
            blob = cam.getBlobs(i+1)
            if ( blob != 0):
                str = "blob: %d, %d, %d, %d, %d" % (blob.color, blob.left, blob.top, blob.right, blob.bottom)
                psm.screen.termPrintAt(7, str)
                drawBox(blob.left+5,blob.top+5,blob.right+5,blob.bottom+5)
            #if<
        #for<


def drawBox(x1,y1,x2,y2):
    print "box %d,%d,%d,%d"%(x1,y1,x2,y2)
    psm.screen.drawLine(x1,y1,x2,y1)
    psm.screen.drawLine(x1,y2,x2,y2)
    psm.screen.drawLine(x1,y1,x1,y2)
    psm.screen.drawLine(x2,y1,x2,y2)

def drawButtons():
    for bb in buttons:
        print bb
        psm.screen.drawButton(bb[0],bb[1],width=60,height=35,text=bb[2],display=False)

def checkButtonPress():
    for bb in buttons:
        if (psm.screen.checkButton(bb[0], bb[1],width=60,height=35) == True):
            return bb[2]

    return ""

cam = MsDevices.NXTCam5(psm.BAS1)
func = doBlob

while(not doExit):

    drawButtons()
    id = cam.GetDeviceId()
    pos = id.find('\0')
    psm.screen.termPrintAt(6, "Device ID: " + id[:pos])

    #cam.command(79)  # object
    time.sleep(1)
    psm.screen.clearScreen()
    drawButtons()

    if( psm.isKeyPressed() == True) or ( psm.screen.checkButton(0,0,30,30)):
        psm.screen.clearScreen()
        psm.screen.termPrintAt(8, "Exiting to menu")
        doExit = True

    btn = checkButtonPress()
    if ( btn != "" ):
        psm.screen.clearScreen()
        if ( btn == 'blob'):
            psm.screen.termPrintAt(4, "blob pressed")
            doBlob(True)
        if ( btn == 'face'):
            psm.screen.termPrintAt(4, "face pressed")
            doFace(True)
        if ( btn == 'movie'):
            psm.screen.termPrintAt(4, "movie pressed")
            doMovie(True)
        if ( btn == 'c-mov'):
            psm.screen.termPrintAt(4, "c-mov pressed")
            doContinuousMovie(True)
        if ( btn == 'eye'):
            psm.screen.termPrintAt(4, "eye pressed")
            doEye(True)
        if ( btn == 'pict'):
            psm.screen.termPrintAt(4, "pict pressed")
            doPicture(True)
        if ( btn == 'qrcode'):
            psm.screen.termPrintAt(4, "qrcode pressed")
            doQRCode(True)
        if ( btn == 'line'):
            psm.screen.termPrintAt(4, "line pressed")
            doLine(True)

    func(False)

    time.sleep(0.4)

