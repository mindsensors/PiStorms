<?php
session_start();

/*
$nf = false;
$software_v = "Unknown";
$file = fopen("/home/pi/PiStorms/.version", "r") or $nf = true;
if (!$nf) {
    $software_v = fread($file,filesize("/home/pi/PiStorms/.version"));
    fclose($file);
}
*/
$versions = '{"update": "both"}';
$file = fopen("/var/tmp/ps_versions.json", "r") or $nf = true;
if (!$nf) {
    $versions = fread($file,filesize("/var/tmp/ps_versions.json"));
    fclose($file);
}
$updates = json_decode($versions, true)["update"];
$uptodate = '<span class="pull-right badge bg-green">Up-to-date</span>';
$needsupdate = '<span class="pull-right badge bg-red">Needs Update!</span>';