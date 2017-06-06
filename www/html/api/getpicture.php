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

$pic = $_GET["image"];

$basepath = '/var/tmp/ps_images/';
$realBase = realpath($basepath);

$userpath = $basepath . $pic;
$realUserPath = realpath($userpath);

$scanned_directory = array_diff(scandir("/var/tmp/ps_images"), array('..', '.'));

if ($realUserPath === false || strpos($realUserPath, $realBase) !== 0 || !in_array($pic, $scanned_directory)) {
    die("nope");
} else {
    $type = 'image/png';
    header('Content-Type:'.$type);
    header('Content-Length: ' . filesize($userpath));
    readfile($userpath);
}

?>
