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
# mindsensors.com invests time and resources providing this open source code,
# please support mindsensors.com  by purchasing products from mindsensors.com!
# To learn more product options, visit us @  http://www.mindsensors.com/
#
# History:
# Date      Author      Comments
# 01/01/16   Deepak     Initial development.
#
from ws4py.client.threadedclient import WebSocketClient
import json, time, socket
import os,sys,inspect,fcntl,struct

def my_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("1.255.255.255",0))
    my_ip = s.getsockname()[0]
    s.close()
    return my_ip

# filter function, drop empty lines as well as our own ip address.
def fff(xxx):
    global my_ip
    if ( xxx == "" ):
        return False
    if ( xxx == my_ip ):
        return False
    return True

def find_swarm_neighbors():
    global my_ip
    my_ip = my_ip_address()
    cmd_str = "sudo -u pi nmap -p 9000 " + my_ip + "/24" + " -oG /tmp/scout.out > /dev/null "
    output = os.system( cmd_str )
    cmd_str = "grep \"9000\/open\" /tmp/scout.out | cut -d\" \" -f2 > /tmp/peer_ips"
    output = os.system( cmd_str )
    f = open("/tmp/peer_ips", 'r')
    lines = f.read().split('\n')
    print lines
    return filter(fff, lines)


my_ip = ""
class SwarmClient(WebSocketClient):
    isRegistered = False
    handler = None
    receivedAck = False
    peerTable = {}
    def __init__(self, handler, server=None, deviceid=None):
        my_ip = my_ip_address()
        #my_name = socket.getfqdn(my_ip)
        my_name = my_ip
        self.userid = my_name
        if ( deviceid == None):
            self.deviceid = my_name
        else:
            self.deviceid = deviceid
        self.devicekey = my_name
        self.handler = handler
        if ( server == None ):
            server = "ws://"+my_ip+":9000/"
        WebSocketClient.__init__(self, server, protocols=['http-only', 'chat'])
        self.connect()
        #time.sleep(0.01)
        # wait here until we get an ack from server
        while ( self.receivedAck == False ):
            pass

    def Send(self, m_type, msg_array):
        msg_array['type'] = m_type
        self.send(json.dumps(msg_array))

    def SendMessage(self, value):
        msg_array = {}
        msg_array['message'] = value
        self.Send('message', msg_array)

    def SendMessageToPeer(self, user, message, deviceid=None):
        msg_array = {}
        msg_array['user'] = user
        if ( deviceid == None):
            msg_array['device'] = user
        else:
            msg_array['device'] = deviceid
        msg_array['message'] = message

        # if the user is in peerTable, use the old connection,
        # else, create new connection and save it for future use.
        if (user in self.peerTable):
            ws2 = self.peerTable[user]
        else:
            svr = "ws://"+user+":9000/"
            ws2 = SwarmClient(self.tempHandler, svr)
            self.peerTable[user] = ws2

        ws2.Send('peermessage', msg_array)
        #ws2.close()

    def tempHandler(self, msg_array):
        if ('type' in msg_array) and (msg_array['type'] == 'peermessage'):
            print ("> Peer says: {0}".format(msg_array['message']))
        else:
            print ("> System Message: {0}".format(msg_array['message']))


    def opened(self):
        # right after establishing connection,
        # send our credentials to register in server's table.
        msg_array = {}
        msg_array['userid'] = self.userid
        msg_array['deviceid'] = self.deviceid
        msg_array['devicekey'] = self.devicekey
        self.Send('credentials', msg_array)

    def closed(self, code, reason=None):
        print ("Closed down {0} {1}".format(code, reason))

    def received_message(self, m):
        data = json.loads(str(m))
        self.receivedAck = True
        if ('type' in data) and (data['type'] == 'register'):
            if ( data['status'] == "successful"):
                self.isRegistered = True
            elif ( data['status'] == "failed"):
                self.isRegistered = False
        else:
            self.handler(data)

if __name__ == '__main__':
    def myHandler(message):
        print ("**myHandler** received: {0}".format(message))

    try:
        print ("creating SwarmClient")
        ws = SwarmClient(myHandler, 'ws://127.0.0.1:9000/')
        if not ( ws.isRegistered ):
            print ("registration failed")
            exit()

        ws.SendMessage("second message")
        ws.SendMessage("third message")
        #ws.run_forever()
        while True:
            pass
    except KeyboardInterrupt:
        ws.close()
