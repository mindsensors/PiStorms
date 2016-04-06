#!/usr/bin/env python
#
# Copyright (c) 2016 mindsensors.com
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.    See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
#mindsensors.com invests time and resources providing this open source code, 
#please support mindsensors.com  by purchasing products from mindsensors.com!
#Learn more product option visit us @  http://www.mindsensors.com/
#
# History:
# Date      Author      Comments
# 01/01/16   Deepak     Initial development.
#
import json, time, os, sys, inspect, thread
from ws4py.client.threadedclient import WebSocketClient
from swarmclient import *
from PiStorms import PiStorms

#
# message sender 
#
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
psm = PiStorms()
doExit = False
bmpw = 60
old_x = 110
old_y = 80

psm.screen.clearScreen()
if __name__ == '__main__':
    #
    # this callback handler handles the messages
    # received from the swarm server.
    #
    def myHandler(msg_array):
        global old_x
        global old_y
        #
        # this is where you would do something with
        # the message received from peer.
        #
        if ('type' in msg_array) and (msg_array['type'] == 'peermessage'):
            print "Peer says: ", msg_array['message']
            msg =  json.loads(str(msg_array['message']))
            if (msg['action'] == "move"):
                smiley_x = msg['x']
                smiley_y = msg['y']
                psm.screen.fillBmp(old_x, old_y, bmpw, bmpw, path = currentdir+'/'+"black-square.png")
                psm.screen.fillBmp(smiley_x, smiley_y, bmpw, bmpw, path = currentdir+'/'+"smiley.png")
                old_x = smiley_x
                old_y = smiley_y
        else:
            print "System Message: ", msg_array['message']

    psm.screen.drawAutoText("Searching Swarm neighbors ...", 15, 218, fill=(255, 255, 255), size = 18) 
    nbrs_list = find_swarm_neighbors()
    if ( len(nbrs_list) == 0 ):
        m = ["Swarm-Demo", "A swarm requires at least two PiStorms", "robots.",
                           "Get another PiStorms robot to add to", "your swarm."]
        psm.screen.askQuestion(m,["OK"])

    psm.screen.clearScreen()
    psm.screen.fillBmp(old_x, old_y, bmpw, bmpw, path = currentdir+'/'+"smiley.png")
    peers = len(nbrs_list)
    psm.screen.drawAutoText( str(peers) + " neighbor(s) found", 15, 200, fill=(255, 255, 255), size = 18) 
    psm.screen.drawAutoText("Press Go to Exit", 15, 218, fill=(255, 255, 255), size = 18) 
    #
    # register with the swarm server
    # Function parameters:
    # SwarmClient(messageHandler, <optional server>)
    #
    print "creating SwarmClient " 
    try:
        ws = SwarmClient(myHandler)
        #
        #
        if not ( ws.isRegistered ):
            print "registration failed"
            m = ["Swarm-Demo", "Swarm server registration failed."]
            psm.screen.askQuestion(m,["OK"])
            exit()

        old_tsx = 0
        old_tsy = 0
        while doExit == False:
            if ( psm.screen.isTouched() ):
                tsx = psm.screen.TS_X()
                tsy = psm.screen.TS_Y()
                tsx_delta = abs(tsx - old_tsx)
                tsy_delta = abs(tsy - old_tsy)
                # ignore small movements
                if ((tsx != 0 and tsy != 0) and (tsx_delta > 8 or tsy_delta > 8)):
                    old_tsx = tsx
                    old_tsy = tsy
                    #print "at: tsx: " + str(tsx) + " tsy: " + str(tsy)
                    # center the image where user touched.
                    image_x = psm.screen.TS_To_ImageCoords_X(tsx,tsy) - 20
                    image_y = psm.screen.TS_To_ImageCoords_Y(tsx,tsy) - 20
                    #print "touched at: x: " + str(image_x) + " y: " + str(image_y)

                    #for each nbr in the list send message of new coordinates {x,y}
                    m_array = {}
                    m_array['action'] = "move"
                    m_array['x'] = image_x
                    m_array['y'] = image_y
                    for neighbor in nbrs_list:
                        ws.SendMessageToPeer(neighbor, json.dumps(m_array))
                    psm.screen.fillBmp(old_x, old_y, bmpw, bmpw, path = currentdir+'/'+"black-square.png")
                    psm.screen.fillBmp(image_x, image_y, bmpw, bmpw, path = currentdir+'/'+"smiley.png")
                    old_x = image_x
                    old_y = image_y
                        

            if(psm.isKeyPressed() == True): # if the GO button is pressed
                psm.screen.clearScreen()
                psm.screen.termPrintln("")
                psm.screen.termPrintln("Exiting to menu")
                #time.sleep(0.2) 
                doExit = True 
            pass

    except KeyboardInterrupt:
        ws.close()

