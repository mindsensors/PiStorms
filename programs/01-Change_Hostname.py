#!/usr/bin/env python
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
    subprocess.call("sudo sed -i 's/^127\.0\.1\.1.*$/127\.0\.1\.1       \"%s\"/' /etc/hosts" % hostname, shell=True)
    subprocess.call("echo \"%s\" | sudo tee /etc/hostname > /dev/null" % hostname, shell=True)
    return subprocess.call("sudo /etc/init.d/hostname.sh", shell=True) == 0
    
while psm.screen.askYesOrNoQuestion(["Change Hostname", "Would you like to set the system hostname?"], wrapText=True):
    userInput = keyboard.getInput()
    hostname = userInput['response']
    if hostname == '' or not userInput['submitted']:
        continue
    if setHostname(hostname):
        psm.screen.showMessage(["Success!", "Your hostname was successfully changed to %s." % hostname], wrapText=True)
        # TODO: restart browser to reflect new hostname
        break
    else:
        psm.screen.showMessage(["Failure", "Unable to set hostname."], wrapText=True)
# Please use only lower-case or capital letters. You may also use a period or dash between any pair of letters.

