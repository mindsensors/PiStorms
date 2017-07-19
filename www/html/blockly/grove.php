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

<category name="Grove" colour="60">
  <block type="Grove_Button"></block>
  <sep gap="5"></sep>
  <block type="Grove_Button__isPressed"></block>

  <block type="Grove_PIR_Motion_Sensor"></block>
  <sep gap="5"></sep>
  <block type="Grove_PIR_Motion_Sensor__motionDetected"></block>

  <block type="Grove_Flame_Sensor"></block>
  <sep gap="5"></sep>
  <block type="Grove_Flame_Sensor__fireDetected"></block>
</category>



<script>
function makeBlock(identifier, parameters, generateCode) {
    Blockly.Blocks[identifier] = {init: parameters};
    Blockly.Python[identifier] = generateCode;
}


allPorts = ["BBA1","BBA2","BBA3","BBD1","BBD2","BAD2","BAD1","BAA3","BAA2","BAA1"].map(p=>[p,p]);
analogPorts = ["BBA1","BBA2","BBA3","BAA3","BAA2","BAA1"].map(p=>[p,p]);
digitalPorts = ["BBD1","BBD2","BAD2","BAD1"].map(p=>[p,p]); // for encoders


makeBlock('Grove_Button',
    function() {
        this.appendDummyInput()
            .appendField("Grove Touch sensor at")
            .appendField(new Blockly.FieldDropdown(allPorts), "port");
        this.setInputsInline(true);
        this.setOutput(true, "Grove_Button");
        this.setColour(0);
        this.setTooltip("");
        this.setHelpUrl("");
    },
    function(block) {
        var port = block.getFieldValue('port');
        Blockly.Python.definitions_.import_GroveDevices = "import GroveDevices";
        Blockly.Python.definitions_[`groveButton_${port}`] = `groveButton_${port} = GroveDevices.Grove_Button("${port}")`;
        return [`groveButton_${port}`, Blockly.Python.ORDER_ATOMIC];
    }
);


makeBlock('Grove_Button__isPressed',
    function() {
        this.appendValueInput("sensor")
            .setCheck("Grove_Button")
            .appendField("is");
        this.appendDummyInput()
            .appendField("pressed");
        this.setInputsInline(true);
        this.setOutput(true, "Boolean");
        this.setColour(0);
        this.setTooltip("");
        this.setHelpUrl("");
    },
    function(block) {
        var sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
        return [`${sensor}.isPressed()`, Blockly.Python.ATOMIC];
    }
);


makeBlock('Grove_PIR_Motion_Sensor',
    function() {
        this.appendDummyInput()
            .appendField("Grove PIR motion sensor at")
            .appendField(new Blockly.FieldDropdown(allPorts), "port");
        this.setInputsInline(true);
        this.setOutput(true, "Grove_PIR_Motion_Sensor");
        this.setColour(0);
        this.setTooltip("");
        this.setHelpUrl("");
    },
    function(block) {
        var port = block.getFieldValue('port');
        Blockly.Python.definitions_.import_GroveDevices = "import GroveDevices";
        Blockly.Python.definitions_[`groveMotionSensor_${port}`] = `groveMotionSensor_${port} = GroveDevices.Grove_PIR_Motion_Sensor("${port}")`;
        return [`groveMotionSensor_${port}`, Blockly.Python.ORDER_ATOMIC];
    }
);


makeBlock('Grove_PIR_Motion_Sensor__motionDetected',
    function() {
        this.appendValueInput("sensor")
            .setCheck("Grove_PIR_Motion_Sensor")
            .appendField("does");
        this.appendDummyInput()
            .appendField("detect motion");
        this.setInputsInline(true);
        this.setOutput(true, "Boolean");
        this.setColour(0);
        this.setTooltip("");
        this.setHelpUrl("");
    },
    function(block) {
        var sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
        return [`${sensor}.motionDetected()`, Blockly.Python.ORDER_ATOMIC];
    }
);
</script>

