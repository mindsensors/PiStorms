#!/usr/bin/env python3
#
# Copyright (c) 2017 mindsensors.com
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
# Learn more product option visit us @  http://www.mindsensors.com/
#
# History:
# Date          Author          Comments
# June 2017     Seth Tenembaum  Initial Authoring

from PiStorms import PiStorms
from TouchScreenInput import TouchScreenInput
import subprocess

psm = PiStorms()
keyboard = TouchScreenInput(psm.screen)

def setHostname(hostname):
    
    subprocess.call("sudo sed -i 's/^127\.0\.1\.1.*$/127\.0\.1\.1       %s/' /etc/hosts" % hostname, shell=True)
    subprocess.call("echo \"%s\" | sudo tee /etc/hostname > /dev/null" % hostname, shell=True)
    return  subprocess.call("sudo /etc/init.d/hostname.sh %s"% hostname, shell=True) == 0

message = ["Change Hostname",
           "Would you like to set the system hostname?",
           "If so, please use only lower-case or capital letters." # no comma so string joins with following line
           "You may also use a period or dash between any pair of letters."]
while psm.screen.askYesOrNoQuestion(message, wrapText=True):
    userInput = keyboard.getInput()
    hostname = userInput['response']
    if hostname == '' or not userInput['submitted']:
        continue
    if setHostname(hostname):
        psm.screen.showMessage(["Success!", 'Your hostname was successfully changed to "%s".' % hostname], wrapText=True)
        # restart browser to reflect new hostname (shown as a cyan title at the top of the screen)
        subprocess.call("sudo /etc/init.d/MSBrowser.sh restart", shell=True)
        break
    else:
        psm.screen.showMessage(["Failure", 'Unable to set hostname to "%s".' % hostname], wrapText=True)
