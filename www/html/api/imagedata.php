<?php
/*
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
# Date         Author          Comments
# July 2016    Roman Bohuk     Initial Authoring 
# May 2017     Seth Tenembaum  Remove login requirement
*/
include "config.php";

$scanned_directory = scandir("/var/tmp/ps_images");
sort($scanned_directory);
$scanned_directory = array_reverse($scanned_directory);

for ($i = 0; $i < sizeof($scanned_directory); $i++) {
                    if (strlen($scanned_directory[$i]) > 4) {
                        echo "<div class=\"col-xs-12 col-sm-6 col-md-4 col-lg-3\">\n    <div class=\"text-center\">\n       <img src=\"./api/getpicture.php?image=$scanned_directory[$i]\" alt=\"$scanned_directory[$i]\" style=\"max-height:200px;max-width:100%;\"/><p style=\"margin-top:5px\"><b>$scanned_directory[$i]</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style=\"white-space: nowrap;\"><i class=\"fa fa-download\"></i>&nbsp;&nbsp;<a href=\"./api/getpicture.php?image=$scanned_directory[$i]\" download=\"$scanned_directory[$i]\">Download</a></span></p></div></div>\n";
                    }
                }
?>
