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

<category name="LED_GRX" colour="140">
  <block type="led_control"></block>
</category>

<script>
Blockly.Blocks['led_control'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("turn LED")
        .appendField(new Blockly.FieldDropdown([["1", "1"], ["2", "2"]]), "led_selector");
    this.appendDummyInput()
        .appendField("to color")
        .appendField(new Blockly.FieldColour("#ff0000"), "COLOR");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(140);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['led_control'] = function(block) {
  var dropdown_led_selector = block.getFieldValue('led_selector');
  var colour_color = block.getFieldValue('COLOR');
  Blockly.Python.definitions_.import_PiStorms_GRX = "from PiStorms_GRX import PiStorms_GRX";
  Blockly.Python.definitions_.grx_PiStorms_GRX = "grx = PiStorms_GRX()";
  var rgb = hexToRgb(colour_color);
  var code = 'grx.led(' + dropdown_led_selector + ', ' + rgb.r + ', ' + rgb.g + ', ' + rgb.b + ')\n';
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
