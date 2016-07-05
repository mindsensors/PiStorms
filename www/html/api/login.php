<?php
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
# June-2016 Roman       Initial development.
#
include "./config.php";

$pass_in = $_POST["pass"];

$nf = false;
$file = fopen("/var/tmp/web/web_passcode.txt", "r") or $nf = true;
if (!$nf) {
    $pass = fread($file,filesize("/var/tmp/web/web_passcode.txt"));
    fclose($file);
    if (isset($pass_in) && $pass === $pass_in) {
        $_SESSION["logged_in"] = true;
        die("1");
    } else {
        $_SESSION["logged_in"] = false;
        die("2");
    }
} else {
    $_SESSION["logged_in"] = true;
    die("3");
}
