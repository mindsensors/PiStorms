<?php
include "config.php";

if (!isset($_SESSION['logged_in']) || !$_SESSION['logged_in']) {
    die();
}

$scanned_directory = scandir("/var/tmp/ps_images");
sort($scanned_directory);
$scanned_directory = array_reverse($scanned_directory);

for ($i = 0; $i < sizeof($scanned_directory); $i++) {
                    if (strlen($scanned_directory[$i]) > 4) {
                        echo "<div class=\"col-xs-12 col-sm-6 col-md-4 col-lg-3\">\n    <div class=\"text-center\">\n       <img src=\"./api/getpicture.php?image=$scanned_directory[$i]\" alt=\"$scanned_directory[$i]\" style=\"max-height:200px;max-width:100%;\"/><p style=\"margin-top:5px\"><b>$scanned_directory[$i]</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style=\"white-space: nowrap;\"><i class=\"fa fa-download\"></i>&nbsp;&nbsp;<a href=\"./api/getpicture.php?image=$scanned_directory[$i]\" download=\"$scanned_directory[$i]\">Download</a></span></p></div></div>\n";
                    }
                }
?>