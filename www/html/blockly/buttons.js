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


var buttons = `
<category name="Buttons" colour="200">
  <block type="system_keypressed"></block>
  <block type="system_getkeypresscount"></block>
  <block type="system_resetkeypresscount"></block>
  <block type="system_waitforkeypress"></block>
  <block type="system_untilkeypress"></block>
</category>
`;


Blockly.Blocks['system_keypressed'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("check if GO button is pressed");
    this.setInputsInline(true);
    this.setOutput(true, "Boolean");
    this.setColour(200);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['system_keypressed'] = function(block) {
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'bool(psm.isKeyPressed())';
  return [code, Blockly.Python.ORDER_ATOMIC];
};


Blockly.Blocks['system_getkeypresscount'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("get key press count");
    this.setInputsInline(true);
    this.setOutput(true, "Number");
    this.setColour(200);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['system_getkeypresscount'] = function(block) {
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.getKeyPressCount()';
  return [code, Blockly.Python.ORDER_ATOMIC];
};


Blockly.Blocks['system_resetkeypresscount'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("reset key press count");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(200);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['system_resetkeypresscount'] = function(block) {
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.resetKeyPressCount()\n';
  return code;
};


Blockly.Blocks['system_waitforkeypress'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("wait for key press");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(200);
    this.setTooltip('Pause until the GO button is pressed');
    this.setHelpUrl('');
  }
};
Blockly.Python['system_waitforkeypress'] = function(block) {
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.waitForKeyPress()\n';
  return code;
};


Blockly.Blocks['system_untilkeypress'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("repeat until key press");
    this.appendStatementInput("func")
        .setCheck(null);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(120);
    this.setTooltip('Repeat until the GO button is pressed');
    this.setHelpUrl('');
  }
};
Blockly.Python['system_untilkeypress'] = function(block) {
  var func = Blockly.Python.statementToCode(block, 'func');
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.untilKeyPress()\n';
  var anon = Blockly.Python.FUNCTION_NAME_PLACEHOLDER_.slice(1,-1);
  code = `def ${anon}():\n${func}psm.untilKeyPress(${anon})\n`;
  return code;
};
