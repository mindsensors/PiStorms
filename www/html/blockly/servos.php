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

<category name="Servos" colour="240">
  <block type="servo_setpulse">
    <value name="PULSE">
      <shadow type="math_number">
      <field name="NUM">1500</field>
    </shadow>
  </block>
</category>



<script>
Blockly.Blocks['servo_setpulse'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("set pulse of servo")
        .appendField(new Blockly.FieldDropdown([["BAS1","BAS1"], ["BAS2","BAS2"], ["BAS3","BAS3"], ["BBS1","BBS1"], ["BBS2","BBS2"], ["BBS3","BBS3"]]), "servo_selector");
    this.appendValueInput("PULSE")
        .setCheck("Number")
        .appendField("to");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(240);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['servo_setpulse'] = function(block) {
  var dropdown_servo_selector = block.getFieldValue('servo_selector');
  var value_pulse = Blockly.Python.valueToCode(block, 'PULSE', Blockly.Python.ORDER_ATOMIC);
  //Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  //Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.'+ dropdown_servo_selector + '.setSpeed(' + value_pulse + ')\n';
  return code;
};
</script>
