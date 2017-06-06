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
*/
session_start();

$versions = '{"update": "loading"}';

$versions = file_get_contents("/var/tmp/ps_versions.json", FILE_USE_INCLUDE_PATH);
/*$file = fopen("/var/tmp/ps_versions.json", "r") or $nf = true;
if (!$nf) {
    $versions = fread($file,filesize("/var/tmp/ps_versions.json"));
    fclose($file);
}
*/
if (!isset($versions) || !$versions) {
    $versions = '{"update": "loading"}';
}

$updates = json_decode($versions, true)["update"];
$uptodate = '<span class="pull-right badge bg-green">Up-to-date</span>';
$needsupdate = '<span id="needs-update-tooltip" class="pull-right badge bg-red">Needs Update!&nbsp;&nbsp;<i data-toggle="tooltip" class="fa fa-question-circle" title="Please go to the mindsensors.com blog to see firmware and sofware update instructions, or click here to go to the GitHub page" aria-hidden="true"></i></span>';
