<?php
include "config.php";

if (!isset($_SESSION['logged_in']) || !$_SESSION['logged_in']) {
    die();
}

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