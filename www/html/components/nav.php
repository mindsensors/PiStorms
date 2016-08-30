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
if (!isset($_SESSION['logged_in']) || !$_SESSION['logged_in']) {
    header('Location: ./login.php');
    exit();
}

$pg = basename($_SERVER['PHP_SELF']);
$act = 'class="active"';

?>
<aside class="main-sidebar">
    <section class="sidebar">
      <ul class="sidebar-menu">
        <li class="header">LINKS</li>
        <li <?php if($pg=="index.php"){echo $act;}?>><a href="./"><i class="fa fa-home"></i> <span>Home</span></a></li>
        <li <?php if($pg=="programs.php"){echo $act;}?>><a href="programs.php"><i class="fa fa-code"></i> <span>Programs</span></a></li>
        <li <?php if($pg=="pictures.php"){echo $act;}?>><a href="pictures.php"><i class="fa fa-image"></i> <span>Screenshots</span></a></li>
        <li <?php if($pg=="remote.php"){echo $act;}?>><a href="remote.php"><i class="fa fa-arrows"></i> <span>Remote Control</span></a></li>
        <li <?php if($pg=="log.php"){echo $act;}?>><a href="log.php"><i class="fa fa-file-text-o"></i> <span>Logs</span></a></li>
        <li <?php if($pg=="message.php"){echo $act;}?>><a href="message.php"><i class="fa fa-comment"></i> <span>Messages</span></a></li>
        <li class="header">HELP</li>
        <li><a href="http://www.mindsensors.com/blog" target="_blank"><i class="fa fa-book"></i> <span>Blog</span></a></li>
        <li><a href="http://www.mindsensors.com/forum" target="_blank"><i class="fa fa-users"></i> <span>Forum</span></a></li>
        <li><a href="#" data-toggle="modal" data-target="#questionFormModal"><i class="fa fa-bug"></i> <span>Submit a Bug</span></a></li>
      </ul>
    </section>
  </aside>