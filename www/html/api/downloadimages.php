<?php
include "config.php";

if (!isset($_SESSION['logged_in']) || !$_SESSION['logged_in']) {
    die();
}

$zip = new ZipArchive;
$download = 'screenshots_export.zip';
$zip->open($download, ZipArchive::CREATE);
foreach (glob("/var/tmp/ps_images/*") as $file) {
    $zip->addFile($file);
}
$zip->close();
header('Content-Type: application/zip');
header("Content-Disposition: attachment; filename = $download");
header('Content-Length: ' . filesize($download));
//header("Location: $download");
?>