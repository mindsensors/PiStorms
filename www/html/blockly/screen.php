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
# July 2017      Seth Tenembaum  Split into multiple files
*/
?>

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



<script>
Blockly.Blocks['screen_drawrect'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("draw rectangle");
    this.appendValueInput("x")
        .setCheck("Number")
        .appendField("X");
    this.appendValueInput("y")
        .setCheck("Number")
        .appendField("Y");
    this.appendValueInput("width")
        .setCheck("Number")
        .appendField("Width");
    this.appendValueInput("height")
        .setCheck("Number")
        .appendField("Height");
    this.appendDummyInput()
        .appendField("Filled with ")
        .appendField(new Blockly.FieldColour("#ff0000"), "COLOR")
        .appendField(" color");
    this.appendDummyInput()
        .appendField("Display on completion")
        .appendField(new Blockly.FieldCheckbox("TRUE"), "DISPLAY");
    this.setInputsInline(false);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(300);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['screen_drawrect'] = function(block) {
  var value_x = Blockly.Python.valueToCode(block, 'x', Blockly.Python.ORDER_ATOMIC);
  var value_y = Blockly.Python.valueToCode(block, 'y', Blockly.Python.ORDER_ATOMIC);
  var value_width = Blockly.Python.valueToCode(block, 'width', Blockly.Python.ORDER_ATOMIC);
  var value_height = Blockly.Python.valueToCode(block, 'height', Blockly.Python.ORDER_ATOMIC);
  var colour_color = block.getFieldValue('COLOR');
  var checkbox_display = block.getFieldValue('DISPLAY') == 'TRUE' ? 'True' : 'False';
  var rgb = hexToRgb(colour_color);
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.screen.fillRect(' + value_x + ', ' + value_y + ', ' + value_width + ', ' + value_height + ', (' + rgb.r + ', ' + rgb.g + ', ' + rgb.b + '), display = ' + checkbox_display + ')\n';
  return code;
};


Blockly.Blocks['screen_drawcircle'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("draw circle");
    this.appendValueInput("x")
        .setCheck("Number")
        .appendField("X");
    this.appendValueInput("y")
        .setCheck("Number")
        .appendField("Y");
    this.appendValueInput("radius")
        .setCheck("Number")
        .appendField("Width");
    this.appendDummyInput()
        .appendField("Filled with ")
        .appendField(new Blockly.FieldColour("#ff0000"), "COLOR")
        .appendField(" color");
    this.appendDummyInput()
        .appendField("Display on completion")
        .appendField(new Blockly.FieldCheckbox("TRUE"), "DISPLAY");
    this.setInputsInline(false);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(300);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['screen_drawcircle'] = function(block) {
  var value_x = Blockly.Python.valueToCode(block, 'x', Blockly.Python.ORDER_ATOMIC);
  var value_y = Blockly.Python.valueToCode(block, 'y', Blockly.Python.ORDER_ATOMIC);
  var value_radius = Blockly.Python.valueToCode(block, 'radius', Blockly.Python.ORDER_ATOMIC);
  var colour_color = block.getFieldValue('COLOR');
  var checkbox_display = block.getFieldValue('DISPLAY') == 'TRUE' ? 'True' : 'False';
  var rgb = hexToRgb(colour_color);
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.screen.fillCircle(' + value_x + ', ' + value_y + ', ' + value_radius + ', (' + rgb.r + ', ' + rgb.g + ', ' + rgb.b + '), display = ' + checkbox_display + ')\n';
  return code;
};


Blockly.Blocks['screen_drawautotxt'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("draw text");
    this.appendValueInput("str")
        .setCheck("String")
        .appendField("Text");
    this.appendValueInput("x")
        .setCheck("Number")
        .appendField("X");
    this.appendValueInput("y")
        .setCheck("Number")
        .appendField("Y");
    this.appendValueInput("size")
        .setCheck("Number")
        .appendField("Size");
    this.appendDummyInput()
        .appendField("Fileld with ")
        .appendField(new Blockly.FieldColour("#ff0000"), "COLOR")
        .appendField(" color");
    this.appendDummyInput()
        .appendField("Display on completion")
        .appendField(new Blockly.FieldCheckbox("TRUE"), "DISPLAY");
    this.setInputsInline(false);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(300);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['screen_drawautotxt'] = function(block) {
  var value_str = Blockly.Python.valueToCode(block, 'str', Blockly.Python.ORDER_ATOMIC);
  var value_x = Blockly.Python.valueToCode(block, 'x', Blockly.Python.ORDER_ATOMIC);
  var value_y = Blockly.Python.valueToCode(block, 'y', Blockly.Python.ORDER_ATOMIC);
  var colour_color = block.getFieldValue('COLOR');
  var value_size = Blockly.Python.valueToCode(block, 'size', Blockly.Python.ORDER_ATOMIC);
  var checkbox_display = block.getFieldValue('DISPLAY') == 'TRUE' ? 'True' : 'False';
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var rgb = hexToRgb(colour_color);
  var code = 'psm.screen.drawAutoText(' + value_str + ', ' + value_x + ', ' + value_y + ', fill = (' + rgb.r + ', ' + rgb.g + ', ' + rgb.b + '), size = ' + value_size +  ', display = ' + checkbox_display + ')\n';
  return code;
};


Blockly.Blocks['screen_drawroundedrect'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("draw rounded rectangle");
    this.appendValueInput("x")
        .setCheck("Number")
        .appendField("X");
    this.appendValueInput("y")
        .setCheck("Number")
        .appendField("Y");
    this.appendValueInput("width")
        .setCheck("Number")
        .appendField("Width");
    this.appendValueInput("height")
        .setCheck("Number")
        .appendField("Height");
    this.appendValueInput("radius")
        .setCheck("Number")
        .appendField("Radius");
    this.appendDummyInput()
        .appendField("Filled with ")
        .appendField(new Blockly.FieldColour("#ff0000"), "COLOR")
        .appendField(" color");
    this.appendDummyInput()
        .appendField("Display on completion")
        .appendField(new Blockly.FieldCheckbox("TRUE"), "DISPLAY");
    this.setInputsInline(false);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(300);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['screen_drawroundedrect'] = function(block) {
  var value_x = Blockly.Python.valueToCode(block, 'x', Blockly.Python.ORDER_ATOMIC);
  var value_y = Blockly.Python.valueToCode(block, 'y', Blockly.Python.ORDER_ATOMIC);
  var value_width = Blockly.Python.valueToCode(block, 'width', Blockly.Python.ORDER_ATOMIC);
  var value_height = Blockly.Python.valueToCode(block, 'height', Blockly.Python.ORDER_ATOMIC);
  var value_radius = Blockly.Python.valueToCode(block, 'radius', Blockly.Python.ORDER_ATOMIC);
  var colour_color = block.getFieldValue('COLOR');
  var checkbox_display = block.getFieldValue('DISPLAY') == 'TRUE' ? 'True' : 'False';
  var rgb = hexToRgb(colour_color);
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.screen.fillRoundRect(' + value_x + ', ' + value_y + ', ' + value_width + ', ' + value_height + ', ' + value_radius + ', (' + rgb.r + ', ' + rgb.g + ', ' + rgb.b + '), ' + checkbox_display + ')\n';
  return code;
};


Blockly.Blocks['screen_drawbmp'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("draw image from file");
    this.appendValueInput("x")
        .setCheck("Number")
        .appendField("X");
    this.appendValueInput("y")
        .setCheck("Number")
        .appendField("Y");
    this.appendValueInput("width")
        .setCheck("Number")
        .appendField("Width");
    this.appendValueInput("height")
        .setCheck("Number")
        .appendField("Height");
    this.appendValueInput("location")
        .setCheck("String")
        .appendField("Path to image");
    this.appendDummyInput()
        .appendField("Display on completion")
        .appendField(new Blockly.FieldCheckbox("TRUE"), "DISPLAY");
    this.setInputsInline(false);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(300);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['screen_drawbmp'] = function(block) {
  var value_x = Blockly.Python.valueToCode(block, 'x', Blockly.Python.ORDER_ATOMIC);
  var value_y = Blockly.Python.valueToCode(block, 'y', Blockly.Python.ORDER_ATOMIC);
  var value_width = Blockly.Python.valueToCode(block, 'width', Blockly.Python.ORDER_ATOMIC);
  var value_height = Blockly.Python.valueToCode(block, 'height', Blockly.Python.ORDER_ATOMIC);
  var value_location = Blockly.Python.valueToCode(block, 'location', Blockly.Python.ORDER_ATOMIC);
  var checkbox_display = block.getFieldValue('DISPLAY') == 'TRUE' ? 'True' : 'False';
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.screen.fillBmp(' + value_x + ', ' + value_y + ', ' + value_width + ', ' + value_height + ', path = ' + value_location + ', display = ' + checkbox_display + ')\n';
  return code;
};


Blockly.Blocks['screen_drawbutton'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("draw button");
    this.appendValueInput("x")
        .setCheck("Number")
        .appendField("X");
    this.appendValueInput("y")
        .setCheck("Number")
        .appendField("Y");
    this.appendValueInput("width")
        .setCheck("Number")
        .appendField("Width");
    this.appendValueInput("height")
        .setCheck("Number")
        .appendField("Height");
    this.appendValueInput("text")
        .setCheck("String")
        .appendField("Text");
    this.appendDummyInput()
        .appendField("Display on completion")
        .appendField(new Blockly.FieldCheckbox("TRUE"), "DISPLAY");
    this.setInputsInline(false);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(300);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['screen_drawbutton'] = function(block) {
  var value_x = Blockly.Python.valueToCode(block, 'x', Blockly.Python.ORDER_ATOMIC);
  var value_y = Blockly.Python.valueToCode(block, 'y', Blockly.Python.ORDER_ATOMIC);
  var value_width = Blockly.Python.valueToCode(block, 'width', Blockly.Python.ORDER_ATOMIC);
  var value_height = Blockly.Python.valueToCode(block, 'height', Blockly.Python.ORDER_ATOMIC);
  var value_location = Blockly.Python.valueToCode(block, 'text', Blockly.Python.ORDER_ATOMIC);
  var checkbox_display = block.getFieldValue('DISPLAY') == 'TRUE' ? 'True' : 'False';
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.screen.drawButton(' + value_x + ', ' + value_y + ', ' + value_width + ', ' + value_height + ', text = ' + value_location + ', display = ' + checkbox_display + ', align="xcenter")\n';
  return code;
};


Blockly.Blocks['screen_checkbutton'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("check button");
    this.appendValueInput("x")
        .setCheck("Number")
        .appendField("X");
    this.appendValueInput("y")
        .setCheck("Number")
        .appendField("Y");
    this.appendValueInput("width")
        .setCheck("Number")
        .appendField("Width");
    this.appendValueInput("height")
        .setCheck("Number")
        .appendField("Height");
    this.setInputsInline(false);
    this.setOutput(true, "Boolean");
    this.setColour(300);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['screen_checkbutton'] = function(block) {
  var value_x = Blockly.Python.valueToCode(block, 'x', Blockly.Python.ORDER_ATOMIC);
  var value_y = Blockly.Python.valueToCode(block, 'y', Blockly.Python.ORDER_ATOMIC);
  var value_width = Blockly.Python.valueToCode(block, 'width', Blockly.Python.ORDER_ATOMIC);
  var value_height = Blockly.Python.valueToCode(block, 'height', Blockly.Python.ORDER_ATOMIC);
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.screen.checkButton(' + value_x + ', ' + value_y + ', ' + value_width + ', ' + value_height + ')';
  return [code, Blockly.Python.ORDER_ATOMIC];
};


Blockly.Blocks['screen_drawtitle'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("display title");
    this.appendValueInput("TEXT")
        .setCheck("String")
        .appendField("Text");
    this.appendDummyInput()
        .appendField("Display on completion")
        .appendField(new Blockly.FieldCheckbox("TRUE"), "DISPLAY");
    this.setInputsInline(false);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(300);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['screen_drawtitle'] = function(block) {
  var value = Blockly.Python.valueToCode(block, 'TEXT', Blockly.Python.ORDER_ATOMIC);
  var checkbox_display = block.getFieldValue('DISPLAY') == 'TRUE' ? 'True' : 'False';
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.screen.drawDisplay(' + value + ', ' + checkbox_display + ')\n';
  return code;
};


Blockly.Blocks['screen_istouched'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("is touched");
    this.setInputsInline(true);
    this.setOutput(true, "Boolean");
    this.setColour(300);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['screen_istouched'] = function(block) {
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  code = "psm.screen.isTouched()";
  return [code, Blockly.Python.ORDER_ATOMIC];
};


Blockly.Blocks['screen_gettouchcoord'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("get")
        .appendField(new Blockly.FieldDropdown([["X", "X"], ["Y", "Y"]]), "mode_selector")
        .appendField("coordinate of touchscreen press");
    this.setInputsInline(true);
    this.setOutput(true, "Number");
    this.setColour(300);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['screen_gettouchcoord'] = function(block) {
  var dropdown_mode_selector = block.getFieldValue('mode_selector');
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  code = "psm.screen.TS_" + dropdown_mode_selector + "()";
  return [code, Blockly.Python.ORDER_ATOMIC];
};


Blockly.Blocks['screen_rotate'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("rotate screen")
        .appendField(new Blockly.FieldDropdown([["left", "Left"], ["right", "Right"]]), "mode_selector")
    this.setInputsInline(false);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(300);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['screen_rotate'] = function(block) {
  var dropdown_mode_selector = block.getFieldValue('mode_selector');
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  code = "psm.screen.rotate" + dropdown_mode_selector + "()\n";
  return code;
};


Blockly.Blocks['screen_getwidthheight'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("get")
        .appendField(new Blockly.FieldDropdown([["width", "Width"], ["height", "Height"]]), "mode_selector")
        .appendField("of the screen");
    this.setInputsInline(true);
    this.setOutput(true, "Number");
    this.setColour(300);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['screen_getwidthheight'] = function(block) {
  var dropdown_mode_selector = block.getFieldValue('mode_selector');
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  code = "psm.screen.screen" + dropdown_mode_selector + "()";
  return [code, Blockly.Python.ORDER_ATOMIC];
};


Blockly.Blocks['screen_clear'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("clear the screen");
    this.appendDummyInput()
        .appendField("Display on completion")
        .appendField(new Blockly.FieldCheckbox("TRUE"), "DISPLAY");
    this.setInputsInline(false);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(300);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['screen_clear'] = function(block) {
  var checkbox_display = block.getFieldValue('DISPLAY') == 'TRUE' ? 'True' : 'False';
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.screen.clearScreen(' + checkbox_display + ')\n';
  return code;
};


Blockly.Blocks['screen_askyesnoquestion'] = {
  init: function() {
    this.appendValueInput("text")
        .setCheck("String")
        .appendField("ask a yes/no question");
    this.setInputsInline(true);
    this.setOutput(true, "Boolean");
    this.setColour(300);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['screen_askyesnoquestion'] = function(block) {
  var value_text = Blockly.Python.valueToCode(block, 'text', Blockly.Python.ORDER_ATOMIC);
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.screen.askYesOrNoQuestion([' + value_text + '])';
  return [code, Blockly.Python.ORDER_ATOMIC];
};


Blockly.Blocks['screen_showmessage'] = {
  init: function() {
    this.appendValueInput("text")
        .setCheck("String")
        .appendField("show message");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(300);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['screen_showmessage'] = function(block) {
  var value_text = Blockly.Python.valueToCode(block, 'text', Blockly.Python.ORDER_ATOMIC);
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.screen.showMessage([' + value_text + '])\n';
  return code;
};


Blockly.Blocks['screen_refresh'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("refresh the screen")
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(300);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['screen_refresh'] = function(block) {
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.screen.refresh()\n';
  return code;
};


Blockly.Blocks['terminal_gotoline'] = {
  init: function() {
    this.appendValueInput("line")
        .setCheck("Number")
        .appendField("go to line");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(200);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['terminal_gotoline'] = function(block) {
  var value_line = Blockly.Python.valueToCode(block, 'line', Blockly.Python.ORDER_ATOMIC);
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.screen.termGotoLine(' + value_line + ')\n';
  return code;
};


Blockly.Blocks['terminal_print'] = {
  init: function() {
    this.appendValueInput("text")
        .appendField("print");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(200);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['terminal_print'] = function(block) {
  var value_text = Blockly.Python.valueToCode(block, 'text', Blockly.Python.ORDER_ATOMIC);
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.screen.termPrint(' + value_text + ')\n';
  return code;
};


Blockly.Blocks['terminal_println'] = {
  init: function() {
    this.appendValueInput("text")
        .appendField("print");
    this.appendDummyInput()
        .appendField("with newline");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(200);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['terminal_println'] = function(block) {
  var value_text = Blockly.Python.valueToCode(block, 'text', Blockly.Python.ORDER_ATOMIC);
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.screen.termPrintln(' + value_text + ')\n';
  return code;
};


Blockly.Blocks['terminal_replacelastline'] = {
  init: function() {
    this.appendValueInput("text")
        .appendField("replace last line with");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(200);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['terminal_replacelastline'] = function(block) {
  var value_text = Blockly.Python.valueToCode(block, 'text', Blockly.Python.ORDER_ATOMIC);
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.screen.termReplaceLastLine(' + value_text + ')\n';
  return code;
};


Blockly.Blocks['terminal_printatline'] = {
  init: function() {
    this.appendValueInput("text")
        .appendField("print");
    this.appendValueInput("line")
        .setCheck("Number")
        .appendField("at line");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(200);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['terminal_printatline'] = function(block) {
  var value_text = Blockly.Python.valueToCode(block, 'text', Blockly.Python.ORDER_ATOMIC);
  var value_line = Blockly.Python.valueToCode(block, 'line', Blockly.Python.ORDER_ATOMIC);
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.screen.termPrintAt(' + value_line + ', ' + value_text + ')\n';
  return code;
};


Blockly.Blocks['terminal_refreshline'] = {
  init: function() {
    this.appendValueInput("line")
        .setCheck("Number")
        .appendField("refresh line");
    this.appendDummyInput()
        .appendField("and ")
        .appendField(new Blockly.FieldCheckbox("TRUE"), "display")
        .appendField(" display");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(200);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['terminal_refreshline'] = function(block) {
  var value_line = Blockly.Python.valueToCode(block, 'line', Blockly.Python.ORDER_ATOMIC);
  var checkbox_display = block.getFieldValue('display') == 'TRUE';
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.screen.refreshLine(' + value_line + ', ' + checkbox_display + ')\n';
  return code;
};



function hexToRgb(hex) {
    var shorthandRegex = /^#?([a-f\d])([a-f\d])([a-f\d])$/i;
    hex = hex.replace(shorthandRegex, function(m, r, g, b) {
        return r + r + g + g + b + b;
    });
    var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return result ? {
        r: parseInt(result[1], 16),
        g: parseInt(result[2], 16),
        b: parseInt(result[3], 16)
    } : null;
}
</script>
