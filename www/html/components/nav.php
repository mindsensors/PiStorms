<?php

if (!isset($_SESSION['logged_in']) || !$_SESSION['logged_in']) {
    header('Location: ./login.php');
}
?>
<aside class="main-sidebar">
    <section class="sidebar">
      <ul class="sidebar-menu">
        <li class="header">LINKS</li>
        <li><a href="./"><i class="fa fa-home"></i> <span>Home</span></a></li>
        <li><a href="#"><i class="fa fa-code"></i> <span>Programs</span></a></li>
        <li><a href="pictures.php"><i class="fa fa-image"></i> <span>Screenshots</span></a></li>
        <li><a href="remote.php"><i class="fa fa-arrows"></i> <span>Remote Control</span></a></li>
        <li><a href="log.php"><i class="fa fa-file-text-o"></i> <span>Logs</span></a></li>
        <li><a href="message.php"><i class="fa fa-comment"></i> <span>Messages</span></a></li>
        <li class="header">HELP</li>
        <li><a href="http://www.mindsensors.com/blog" target="_blank"><i class="fa fa-book"></i> <span>Documentation</span></a></li>
        <li><a href="http://www.mindsensors.com/forum" target="_blank"><i class="fa fa-rss"></i> <span>Forum</span></a></li>
      </ul>
    </section>
  </aside>