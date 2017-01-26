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
# Date           Author          Comments
# August 2016    Roman Bohuk     Initial Authoring 
# October 2016   Seth Tenembaum  Add showMessage 
# January 2017   Roman Bohuk     Add support for SumoEyes, LineLeader, LightSensorArray

*/
?>
<xml id="toolbox" style="display: none">
    <category name="Logic" colour="210">
      <block type="controls_if"></block>
      <block type="logic_compare"></block>
      <block type="logic_operation"></block>
      <block type="logic_negate"></block>
      <block type="logic_boolean"></block>
      <block type="logic_null"></block>
      <block type="logic_ternary"></block>
    </category>
    <category name="Loops" colour="120">
      <block type="controls_repeat_ext">
        <value name="TIMES">
          <shadow type="math_number">
            <field name="NUM">10</field>
          </shadow>
        </value>
      </block>
      <block type="controls_whileUntil"></block>
      <block type="controls_for">
        <value name="FROM">
          <shadow type="math_number">
            <field name="NUM">1</field>
          </shadow>
        </value>
        <value name="TO">
          <shadow type="math_number">
            <field name="NUM">10</field>
          </shadow>
        </value>
        <value name="BY">
          <shadow type="math_number">
            <field name="NUM">1</field>
          </shadow>
        </value>
      </block>
      <block type="controls_forEach"></block>
      <block type="controls_flow_statements"></block>
    </category>
    <category name="Math" colour="230">
      <block type="math_number"></block>
      <block type="math_arithmetic">
        <value name="A">
          <shadow type="math_number">
            <field name="NUM">1</field>
          </shadow>
        </value>
        <value name="B">
          <shadow type="math_number">
            <field name="NUM">1</field>
          </shadow>
        </value>
      </block>
      <block type="math_single">
        <value name="NUM">
          <shadow type="math_number">
            <field name="NUM">9</field>
          </shadow>
        </value>
      </block>
      <block type="math_trig">
        <value name="NUM">
          <shadow type="math_number">
            <field name="NUM">45</field>
          </shadow>
        </value>
      </block>
      <block type="math_constant"></block>
      <block type="math_number_property">
        <value name="NUMBER_TO_CHECK">
          <shadow type="math_number">
            <field name="NUM">0</field>
          </shadow>
        </value>
      </block>
      <block type="math_change">
        <value name="DELTA">
          <shadow type="math_number">
            <field name="NUM">1</field>
          </shadow>
        </value>
      </block>
      <block type="math_round">
        <value name="NUM">
          <shadow type="math_number">
            <field name="NUM">3.1</field>
          </shadow>
        </value>
      </block>
      <block type="math_on_list"></block>
      <block type="math_modulo">
        <value name="DIVIDEND">
          <shadow type="math_number">
            <field name="NUM">64</field>
          </shadow>
        </value>
        <value name="DIVISOR">
          <shadow type="math_number">
            <field name="NUM">10</field>
          </shadow>
        </value>
      </block>
      <block type="math_constrain">
        <value name="VALUE">
          <shadow type="math_number">
            <field name="NUM">50</field>
          </shadow>
        </value>
        <value name="LOW">
          <shadow type="math_number">
            <field name="NUM">1</field>
          </shadow>
        </value>
        <value name="HIGH">
          <shadow type="math_number">
            <field name="NUM">100</field>
          </shadow>
        </value>
      </block>
      <block type="math_random_int">
        <value name="FROM">
          <shadow type="math_number">
            <field name="NUM">1</field>
          </shadow>
        </value>
        <value name="TO">
          <shadow type="math_number">
            <field name="NUM">100</field>
          </shadow>
        </value>
      </block>
      <block type="math_random_float"></block>
    </category>
    <category name="Text" colour="160">
      <block type="text"></block>
      <block type="text_join"></block>
      <block type="text_append">
        <value name="TEXT">
          <shadow type="text"></shadow>
        </value>
      </block>
      <block type="text_length">
        <value name="VALUE">
          <shadow type="text">
            <field name="TEXT">abc</field>
          </shadow>
        </value>
      </block>
      <block type="text_isEmpty">
        <value name="VALUE">
          <shadow type="text">
            <field name="TEXT"></field>
          </shadow>
        </value>
      </block>
      <block type="text_indexOf">
        <value name="VALUE">
          <block type="variables_get">
            <field name="VAR">text</field>
          </block>
        </value>
        <value name="FIND">
          <shadow type="text">
            <field name="TEXT">abc</field>
          </shadow>
        </value>
      </block>
      <block type="text_charAt">
        <value name="VALUE">
          <block type="variables_get">
            <field name="VAR">text</field>
          </block>
        </value>
      </block>
      <block type="text_getSubstring">
        <value name="STRING">
          <block type="variables_get">
            <field name="VAR">text</field>
          </block>
        </value>
      </block>
      <block type="text_changeCase">
        <value name="TEXT">
          <shadow type="text">
            <field name="TEXT">abc</field>
          </shadow>
        </value>
      </block>
      <block type="text_trim">
        <value name="TEXT">
          <shadow type="text">
            <field name="TEXT">abc</field>
          </shadow>
        </value>
      </block>
      <block type="text_print">
        <value name="TEXT">
          <shadow type="text">
            <field name="TEXT">abc</field>
          </shadow>
        </value>
      </block>
      <block type="text_prompt_ext">
        <value name="TEXT">
          <shadow type="text">
            <field name="TEXT">abc</field>
          </shadow>
        </value>
      </block>
    </category>
    <category name="Lists" colour="260">
      <block type="lists_create_with">
        <mutation items="0"></mutation>
      </block>
      <block type="lists_create_with"></block>
      <block type="lists_repeat">
        <value name="NUM">
          <shadow type="math_number">
            <field name="NUM">5</field>
          </shadow>
        </value>
      </block>
      <block type="lists_length"></block>
      <block type="lists_isEmpty"></block>
      <block type="lists_indexOf">
        <value name="VALUE">
          <block type="variables_get">
            <field name="VAR">list</field>
          </block>
        </value>
      </block>
      <block type="lists_getIndex">
        <value name="VALUE">
          <block type="variables_get">
            <field name="VAR">list</field>
          </block>
        </value>
      </block>
      <block type="lists_setIndex">
        <value name="LIST">
          <block type="variables_get">
            <field name="VAR">list</field>
          </block>
        </value>
      </block>
      <block type="lists_getSublist">
        <value name="LIST">
          <block type="variables_get">
            <field name="VAR">list</field>
          </block>
        </value>
      </block>
      <block type="lists_split">
        <value name="DELIM">
          <shadow type="text">
            <field name="TEXT">,</field>
          </shadow>
        </value>
      </block>
      <block type="lists_sort"></block>
    </category>
    <category name="Color" colour="20">
      <block type="colour_picker"></block>
      <block type="colour_random"></block>
      <block type="colour_rgb">
        <value name="RED">
          <shadow type="math_number">
            <field name="NUM">100</field>
          </shadow>
        </value>
        <value name="GREEN">
          <shadow type="math_number">
            <field name="NUM">50</field>
          </shadow>
        </value>
        <value name="BLUE">
          <shadow type="math_number">
            <field name="NUM">0</field>
          </shadow>
        </value>
      </block>
      <block type="colour_blend">
        <value name="COLOUR1">
          <shadow type="colour_picker">
            <field name="COLOUR">#ff0000</field>
          </shadow>
        </value>
        <value name="COLOUR2">
          <shadow type="colour_picker">
            <field name="COLOUR">#3333ff</field>
          </shadow>
        </value>
        <value name="RATIO">
          <shadow type="math_number">
            <field name="NUM">0.5</field>
          </shadow>
        </value>
      </block>
    </category>
    <sep></sep>
    
    <category name="Custom Vars" colour="330" custom="VARIABLE"></category>
    <category name="Functions" colour="290" custom="PROCEDURE"></category>
    <sep></sep>
    
    <category name="Motors" colour="240">
      <block type="motors_setspeed">
        <value name="SPEED">
          <shadow type="math_number">
            <field name="NUM">50</field>
          </shadow>
        </value>
      </block>
      <block type="motors_getposition"></block>
      <block type="motors_resetposition"></block>
      <block type="motors_brake"></block>
      <block type="motors_float"></block>
      <block type="motors_hold"></block>
      <block type="motors_syncspeed">
        <value name="SPEED">
          <shadow type="math_number">
            <field name="NUM">50</field>
          </shadow>
        </value>
      </block>
      <block type="motors_syncfloat"></block>
      <block type="motors_syncbrake"></block>
      <block type="motors_runsecs">
        <value name="SPEED">
          <shadow type="math_number">
            <field name="NUM">50</field>
          </shadow>
        </value>
        <value name="TIME">
          <shadow type="math_number">
            <field name="NUM">3</field>
          </shadow>
        </value>
      </block>
      <block type="motors_rundegrees">
        <value name="SPEED">
          <shadow type="math_number">
            <field name="NUM">50</field>
          </shadow>
        </value>
        <value name="DEG">
          <shadow type="math_number">
            <field name="NUM">180</field>
          </shadow>
        </value>
      </block>
      <block type="motors_isbusy"></block>
      <block type="motors_isstalled"></block>
      <block type="motors_isoverloaded"></block>
      <block type="motors_waituntilnotbusy"></block>
      <block type="motors_setparams">
        <value name="Kp_tacho">
          <shadow type="math_number">
            <field name="NUM">6</field>
          </shadow>
        </value>
        <value name="Ki_tacho">
          <shadow type="math_number">
            <field name="NUM">0</field>
          </shadow>
        </value>
        <value name="Kd_tacho">
          <shadow type="math_number">
            <field name="NUM">0</field>
          </shadow>
        </value>
        <value name="Kp_speed">
          <shadow type="math_number">
            <field name="NUM">1</field>
          </shadow>
        </value>
        <value name="Ki_speed">
          <shadow type="math_number">
            <field name="NUM">0</field>
          </shadow>
        </value>
        <value name="Kd_speed">
          <shadow type="math_number">
            <field name="NUM">0</field>
          </shadow>
        </value>
        <value name="passcount">
          <shadow type="math_number">
            <field name="NUM">10</field>
          </shadow>
        </value>
        <value name="tolerance">
          <shadow type="math_number">
            <field name="NUM">5</field>
          </shadow>
        </value>
      </block>
    </category>

    <category name="Sensors" colour="60">
      <block type="sensors_nxttouch"></block>
      <sep gap="5"></sep>
      <block type="sensors_ev3touch"></block>
      <sep gap="5"></sep>
      <block type="sensors_istouchpressed"></block>
      <sep gap="5"></sep>
      <block type="sensors_gettouchbumpcount"></block>
      <sep gap="5"></sep>
      <block type="sensors_resettouchbumpcount"></block>
      <sep gap="20"></sep>
      <block type="sensors_nxtlight"></block>
      <sep gap="5"></sep>
      <block type="sensors_nxtlightgetvalue"></block>
      <sep gap="5"></sep>
      <block type="sensors_nxtlightsetmode"></block>
      <sep gap="20"></sep>
      <block type="sensors_nxtcolor"></block>
      <sep gap="5"></sep>
      <block type="sensors_nxtcolorgetcolor"></block>
      <sep gap="5"></sep>
      <block type="sensors_nxtcolorsetmode"></block>
      <sep gap="20"></sep>
      <block type="sensors_ev3color"></block>
      <sep gap="5"></sep>
      <block type="sensors_ev3colorgetvalue"></block>
      <sep gap="5"></sep>
      <block type="sensors_ev3colorsetmode"></block>
      <sep gap="20"></sep>
      <block type="sensors_ev3gyro"></block>
      <sep gap="5"></sep>
      <block type="sensors_ev3gyrogetvalue"></block>
      <sep gap="5"></sep>
      <block type="sensors_ev3gyrosetmode"></block>
      <sep gap="20"></sep>
      <block type="sensors_ev3ultrasonic"></block>
      <sep gap="5"></sep>
      <block type="sensors_ev3ultrasonicgetvalue"></block>
      <sep gap="5"></sep>
      <block type="sensors_ev3ultrasonicdetect"></block>
      <sep gap="5"></sep>
      <block type="sensors_ev3ultrasonicsetmode"></block>
      <sep gap="20"></sep>
      <block type="sensors_ev3infrared"></block>
      <sep gap="5"></sep>
      <block type="sensors_ev3infraredgetproximity">
        <value name="channel">
          <shadow type="math_number">
            <field name="NUM">1</field>
          </shadow>
        </value>
      </block>
      <sep gap="5"></sep>
      <block type="sensors_ev3infraredchannelheading">
        <value name="channel">
          <shadow type="math_number">
            <field name="NUM">1</field>
          </shadow>
        </value>
      </block>
      <sep gap="5"></sep>
      <block type="sensors_ev3infraredchannelproximity">
        <value name="channel">
          <shadow type="math_number">
            <field name="NUM">1</field>
          </shadow>
        </value>
      </block>
      <sep gap="5"></sep>
      <block type="sensors_ev3infraredgetremote">
        <value name="channel">
          <shadow type="math_number">
            <field name="NUM">1</field>
          </shadow>
        </value>
      </block>
      <sep gap="5"></sep>
      <block type="sensors_ev3infraredsetmode"></block>
      <sep gap="20"></sep>
      <block type="sensors_absoluteimu"></block>
      <sep gap="5"></sep>
      <block type="sensors_absoluteimugettilt"></block>
      <sep gap="5"></sep>
      <block type="sensors_absoluteimugetacceleration"></block>
      <sep gap="5"></sep>
      <block type="sensors_absoluteimugetmagnetometer"></block>
      <sep gap="5"></sep>
      <block type="sensors_absoluteimugetgyro"></block>
      <sep gap="5"></sep>
      <block type="sensors_absoluteimugetheading"></block>
      <sep gap="5"></sep>
      <block type="sensors_absoluteimusetaccel"></block>
      <sep gap="5"></sep>
      <block type="sensors_absoluteimustartcmpscal"></block>
      <sep gap="5"></sep>
      <block type="sensors_absoluteimustopcmpscal"></block>
      <block type="sensors_sumoeyes"></block>
      <sep gap="5"></sep>
      <block type="sensors_sumoeyesgetvalue"></block>
      <sep gap="5"></sep>
      <block type="sensors_sumoeyessetmode"></block>
      <sep gap="20"></sep>
      <block type="sensors_lineleader"></block>
      <sep gap="5"></sep>
      <block type="sensors_lineleadergetsteering"></block>
      <sep gap="5"></sep>
      <block type="sensors_lineleadergetaverage"></block>
      <sep gap="5"></sep>
      <block type="sensors_lineleadergetresult"></block>
      <sep gap="5"></sep>
      <block type="sensors_lineleadergetrawcalibrated"></block>
      <sep gap="20"></sep>
      <block type="sensors_lsa"></block>
      <sep gap="5"></sep>
      <block type="sensors_lsagetrawcalibrated"></block>
      <sep gap="20"></sep>
    </category>

    <category name="Screen" colour="300">
      <block type="screen_drawrect">
        <value name="x">
          <shadow type="math_number">
            <field name="NUM">10</field>
          </shadow>
        </value>
        <value name="y">
          <shadow type="math_number">
            <field name="NUM">10</field>
          </shadow>
        </value>
        <value name="width">
          <shadow type="math_number">
            <field name="NUM">50</field>
          </shadow>
        </value>
        <value name="height">
          <shadow type="math_number">
            <field name="NUM">50</field>
          </shadow>
        </value>
      </block>
      <block type="screen_drawcircle">
        <value name="x">
          <shadow type="math_number">
            <field name="NUM">10</field>
          </shadow>
        </value>
        <value name="y">
          <shadow type="math_number">
            <field name="NUM">10</field>
          </shadow>
        </value>
        <value name="radius">
          <shadow type="math_number">
            <field name="NUM">25</field>
          </shadow>
        </value>
      </block>
      <block type="screen_drawautotxt">
        <value name="x">
          <shadow type="math_number">
            <field name="NUM">10</field>
          </shadow>
        </value>
        <value name="y">
          <shadow type="math_number">
            <field name="NUM">10</field>
          </shadow>
        </value>
        <value name="size">
          <shadow type="math_number">
            <field name="NUM">20</field>
          </shadow>
        </value>
        <value name="str">
          <shadow type="text">
            <field name="TEXT">Hello World</field>
          </shadow>
        </value>
      </block>
      <block type="screen_drawroundedrect">
        <value name="x">
          <shadow type="math_number">
            <field name="NUM">10</field>
          </shadow>
        </value>
        <value name="y">
          <shadow type="math_number">
            <field name="NUM">10</field>
          </shadow>
        </value>
        <value name="width">
          <shadow type="math_number">
            <field name="NUM">50</field>
          </shadow>
        </value>
        <value name="height">
          <shadow type="math_number">
            <field name="NUM">50</field>
          </shadow>
        </value>
        <value name="radius">
          <shadow type="math_number">
            <field name="NUM">5</field>
          </shadow>
        </value>
      </block>
      <block type="screen_drawbmp">
        <value name="x">
          <shadow type="math_number">
            <field name="NUM">30</field>
          </shadow>
        </value>
        <value name="y">
          <shadow type="math_number">
            <field name="NUM">0</field>
          </shadow>
        </value>
        <value name="width">
          <shadow type="math_number">
            <field name="NUM">240</field>
          </shadow>
        </value>
        <value name="height">
          <shadow type="math_number">
            <field name="NUM">240</field>
          </shadow>
        </value>
        <value name="location">
          <shadow type="text">
            <field name="TEXT">/usr/local/mindsensors/images/Pane1.png</field>
          </shadow>
        </value>
      </block>
      <block type="screen_drawbutton">
        <value name="x">
          <shadow type="math_number">
            <field name="NUM">10</field>
          </shadow>
        </value>
        <value name="y">
          <shadow type="math_number">
            <field name="NUM">10</field>
          </shadow>
        </value>
        <value name="width">
          <shadow type="math_number">
            <field name="NUM">50</field>
          </shadow>
        </value>
        <value name="height">
          <shadow type="math_number">
            <field name="NUM">30</field>
          </shadow>
        </value>
        <value name="text">
          <shadow type="text">
            <field name="TEXT">OK</field>
          </shadow>
        </value>
      </block>
      <block type="screen_checkbutton">
        <value name="x">
          <shadow type="math_number">
            <field name="NUM">10</field>
          </shadow>
        </value>
        <value name="y">
          <shadow type="math_number">
            <field name="NUM">10</field>
          </shadow>
        </value>
        <value name="width">
          <shadow type="math_number">
            <field name="NUM">50</field>
          </shadow>
        </value>
        <value name="height">
          <shadow type="math_number">
            <field name="NUM">30</field>
          </shadow>
        </value>
      </block>
      <block type="screen_drawtitle">
        <value name="TEXT">
          <shadow type="text">
            <field name="TEXT">Hello World</field>
          </shadow>
        </value>
      </block>
      <block type="screen_istouched"></block>
      <block type="screen_gettouchcoord"></block>
      <block type="screen_rotate"></block>
      <block type="screen_getwidthheight"></block>
      <block type="screen_clear"></block>
      <block type="screen_askyesnoquestion">
        <value name="text">
          <shadow type="text">
            <field name="TEXT">Continue?</field>
          </shadow>
        </value>
      </block>
      <block type="screen_showmessage">
        <value name="text">
          <shadow type="text">
            <field name="TEXT">You win!</field>
          </shadow>
        </value>
      </block>
      <block type="screen_refresh">
        <value name="line">
          <shadow type="math_number">
            <field name="NUM">1</field>
          </shadow>
        </value>
      </block>
      <block type="terminal_gotoline">
        <value name="line">
          <shadow type="math_number">
            <field name="NUM">1</field>
          </shadow>
        </value>
      </block>
      <block type="terminal_print">
        <value name="text">
          <shadow type="text">
            <field name="TEXT">Hello World</field>
          </shadow>
        </value>
      </block>
      <block type="terminal_println">
        <value name="text">
          <shadow type="text">
            <field name="TEXT">Hello World</field>
          </shadow>
        </value>
      </block>
      <block type="terminal_replacelastline">
        <value name="text">
          <shadow type="text">
            <field name="TEXT">Hello World</field>
          </shadow>
        </value>
      </block>
      <block type="terminal_printatline">
        <value name="text">
          <shadow type="text">
            <field name="TEXT">Hello World</field>
          </shadow>
        </value>
        <value name="line">
          <shadow type="math_number">
            <field name="NUM">1</field>
          </shadow>
        </value>
      </block>
      <block type="terminal_refreshline">
        <value name="line">
          <shadow type="math_number">
            <field name="NUM">1</field>
          </shadow>
        </value>
      </block>
    </category>
    
    <category name="LED" colour="140">
      <block type="led_control"></block>
    </category>
    
    <category name="Buttons" colour="200">
      <block type="system_keypressed"></block>
      <block type="system_getkeypresscount"></block>
      <block type="system_resetkeypresscount"></block>
    </category>
        
    <category name="System" colour="5">
      <block type="system_print">
        <value name="TEXT">
          <shadow type="text">
            <field name="TEXT">Hello World</field>
          </shadow>
        </value>
      </block>
      <block type="system_sleep">
        <value name="TIME">
          <shadow type="math_number">
            <field name="NUM">3</field>
          </shadow>
        </value>
      </block>
      <block type="system_exit"></block>
      <block type="variable_pistorms"></block>
      <block type="system_shutdown"></block>
      <block type="system_getbattery"></block>
      <block type="system_getfirmware"></block>
      <block type="system_getvendor"></block>
      <block type="system_getdeviceid"></block>
    </category>
  </xml>