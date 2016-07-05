<?php
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