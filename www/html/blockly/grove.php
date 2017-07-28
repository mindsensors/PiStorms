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

  <block type="Grove_Luminance_Sensor"></block>
  <sep gap="5"></sep>
  <block type="Grove_Luminance_Sensor__luminance"></block>

  <block type="Grove_Light_Sensor"></block>
  <sep gap="5"></sep>
  <block type="Grove_Light_Sensor__lightLevel"></block>

  <block type="Grove_Temperature_Sensor"></block>
  <sep gap="5"></sep>
  <block type="Grove_Temperature_Sensor__temperature"></block>
  <sep gap="5"></sep>
  <block type="Grove_Temperature_Sensor__CtoF"></block>

  <block type="Grove_UV_Sensor"></block>
  <sep gap="5"></sep>
  <block type="Grove_UV_Sensor__intensity"></block>
  <sep gap="5"></sep>
  <block type="Grove_UV_Sensor__UVindex"></block>

  <block type="Grove_Moisture_Sensor"></block>
  <sep gap="5"></sep>
  <block type="Grove_Moisture_Sensor__moistureLevel"></block>

  <block type="Grove_Sound_Sensor"></block>
  <sep gap="5"></sep>
  <block type="Grove_Sound_Sensor__soundIntensity"></block>

  <block type="Grove_Loudness_Sensor"></block>
  <sep gap="5"></sep>
  <block type="Grove_Loudness_Sensor__detectSound"></block>

  <block type="Grove_Air_Quality_Sensor"></block>
  <sep gap="5"></sep>
  <block type="Grove_Air_Quality_Sensor__airQuality"></block>
  <sep gap="5"></sep>
  <block type="Grove_Air_Quality_Sensor__qualitativeMeasurement"></block>
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
        this.setColour(20);
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
        this.setColour(20);
        this.setTooltip("");
        this.setHelpUrl("");
    },
    function(block) {
        var sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
        return [`${sensor}.motionDetected()`, Blockly.Python.ORDER_ATOMIC];
    }
);


makeBlock('Grove_Flame_Sensor',
    function() {
        this.appendDummyInput()
            .appendField("Grove flame sensor at")
            .appendField(new Blockly.FieldDropdown(allPorts), "port");
        this.setInputsInline(true);
        this.setOutput(true, "Grove_Flame_Sensor");
        this.setColour(40);
        this.setTooltip("");
        this.setHelpUrl("");
    },
    function(block) {
        var port = block.getFieldValue('port');
        Blockly.Python.definitions_.import_GroveDevices = "import GroveDevices";
        Blockly.Python.definitions_[`groveFlameSensor_${port}`] = `groveFlameSensor_${port} = GroveDevices.Grove_Flame_Sensor("${port}")`;
        return [`groveFlameSensor_${port}`, Blockly.Python.ORDER_ATOMIC];
    }
);


makeBlock('Grove_Flame_Sensor__fireDetected',
    function() {
        this.appendValueInput("sensor")
            .setCheck("Grove_Flame_Sensor")
            .appendField("does");
        this.appendDummyInput()
            .appendField("detect fire");
        this.setInputsInline(true);
        this.setOutput(true, "Boolean");
        this.setColour(40);
        this.setTooltip("");
        this.setHelpUrl("");
    },
    function(block) {
        var sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
        return [`${sensor}.fireDetected()`, Blockly.Python.ORDER_ATOMIC];
    }
);


makeBlock('Grove_Luminance_Sensor',
    function() {
        this.appendDummyInput()
            .appendField("Grove luminance sensor at")
            .appendField(new Blockly.FieldDropdown(analogPorts), "port");
        this.setInputsInline(true);
        this.setOutput(true, "Grove_Luminance_Sensor");
        this.setColour(60);
        this.setTooltip("");
        this.setHelpUrl("");
    },
    function(block) {
        var port = block.getFieldValue('port');
        Blockly.Python.definitions_.import_GroveDevices = "import GroveDevices";
        Blockly.Python.definitions_[`groveLuminanceSensor_${port}`] = `groveLuminanceSensor_${port} = GroveDevices.Grove_Luminance_Sensor("${port}")`;
        return [`groveLuminanceSensor_${port}`, Blockly.Python.ORDER_ATOMIC];
    }
);


makeBlock('Grove_Luminance_Sensor__luminance',
    function() {
        this.appendValueInput("sensor")
            .setCheck("Grove_Luminance_Sensor")
            .appendField("luminance of");
        this.setInputsInline(true);
        this.setOutput(true, "Number");
        this.setColour(60);
        this.setTooltip("");
        this.setHelpUrl("");
    },
    function(block) {
        var sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
        return [`${sensor}.luminance()`, Blockly.Python.ATOMIC];
    }
);


makeBlock('Grove_Light_Sensor',
    function() {
        this.appendDummyInput()
            .appendField("Grove light sensor at")
            .appendField(new Blockly.FieldDropdown(analogPorts), "port");
        this.setInputsInline(true);
        this.setOutput(true, "Grove_Light_Sensor");
        this.setColour(80);
        this.setTooltip("");
        this.setHelpUrl("");
    },
    function(block) {
        var port = block.getFieldValue('port');
        Blockly.Python.definitions_.import_GroveDevices = "import GroveDevices";
        Blockly.Python.definitions_[`groveLightSensor_${port}`] = `groveLightSensor_${port} = GroveDevices.Grove_Light_Sensor("${port}")`;
        return [`groveLightSensor_${port}`, Blockly.Python.ORDER_ATOMIC];
    }
);


makeBlock('Grove_Light_Sensor__lightLevel',
    function() {
        this.appendValueInput("sensor")
            .setCheck("Grove_Light_Sensor")
            .appendField("light level of");
        this.setInputsInline(true);
        this.setOutput(true, "Number");
        this.setColour(80);
        this.setTooltip("");
        this.setHelpUrl("");
    },
    function(block) {
        var sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
        return [`${sensor}.lightLevel()`, Blockly.Python.ATOMIC];
    }
);


makeBlock('Grove_Temperature_Sensor',
    function() {
        this.appendDummyInput()
            .appendField("Grove temperature sensor at")
            .appendField(new Blockly.FieldDropdown(analogPorts), "port");
        this.setInputsInline(true);
        this.setOutput(true, "Grove_Temperature_Sensor");
        this.setColour(100);
        this.setTooltip("");
        this.setHelpUrl("");
    },
    function(block) {
        var port = block.getFieldValue('port');
        Blockly.Python.definitions_.import_GroveDevices = "import GroveDevices";
        Blockly.Python.definitions_[`groveTemperatureSensor_${port}`] = `groveTemperatureSensor_${port} = GroveDevices.Grove_Temperature_Sensor("${port}")`;
        return [`groveTemperatureSensor_${port}`, Blockly.Python.ORDER_ATOMIC];
    }
);


makeBlock('Grove_Temperature_Sensor__temperature',
    function() {
        this.appendValueInput("sensor")
            .setCheck("Grove_Temperature_Sensor")
            .appendField("detected temperature of");
        this.setInputsInline(true);
        this.setOutput(true, "Number");
        this.setColour(100);
        this.setTooltip("");
        this.setHelpUrl("");
    },
    function(block) {
        var sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
        return [`${sensor}.temperature()`, Blockly.Python.ATOMIC];
    }
);


makeBlock('Grove_Temperature_Sensor__CtoF',
    function() {
        this.appendValueInput("celsius")
            .setCheck("Number")
            .appendField("Farenheit conversion of")
        this.appendDummyInput()
            .appendField("Celsius")
        this.setInputsInline(true);
        this.setOutput(true, "Number");
        this.setColour(100);
        this.setTooltip("");
        this.setHelpUrl("");
    },
    function(block) {
        Blockly.Python.definitions_.import_GroveDevices = "import GroveDevices";
        var celsius = Blockly.Python.valueToCode(block, 'celsius', Blockly.Python.ORDER_ATOMIC);
        return [`GroveDevices.Grove_Temperature_Sensor.CtoF(${celsius})`, Blockly.Python.ATOMIC];

    }
);


makeBlock('Grove_UV_Sensor',
    function() {
        this.appendDummyInput()
            .appendField("Grove UV sensor at")
            .appendField(new Blockly.FieldDropdown(analogPorts), "port");
        this.setInputsInline(true);
        this.setOutput(true, "Grove_UV_Sensor");
        this.setColour(120);
        this.setTooltip("");
        this.setHelpUrl("");
    },
    function(block) {
        var port = block.getFieldValue('port');
        Blockly.Python.definitions_.import_GroveDevices = "import GroveDevices";
        Blockly.Python.definitions_[`groveUVSensor_${port}`] = `groveUVSensor_${port} = GroveDevices.Grove_UV_Sensor("${port}")`;
        return [`groveUVSensor_${port}`, Blockly.Python.ORDER_ATOMIC];
    }
);


makeBlock('Grove_UV_Sensor__intensity',
    function() {
        this.appendValueInput("sensor")
            .setCheck("Grove_UV_Sensor")
            .appendField("measured intensity of");
        this.setInputsInline(true);
        this.setOutput(true, "Number");
        this.setColour(120);
        this.setTooltip("");
        this.setHelpUrl("");
    },
    function(block) {
        var sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
        return [`${sensor}.intensity()`, Blockly.Python.ATOMIC];
    }
);


makeBlock('Grove_UV_Sensor__UVindex',
    function() {
        this.appendValueInput("sensor")
            .setCheck("Grove_UV_Sensor")
            .appendField("UV index of");
        this.setInputsInline(true);
        this.setOutput(true, "Number");
        this.setColour(120);
        this.setTooltip("");
        this.setHelpUrl("");
    },
    function(block) {
        var sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
        return [`${sensor}.UVindex()`, Blockly.Python.ATOMIC];
    }
);


makeBlock('Grove_Moisture_Sensor',
    function() {
        this.appendDummyInput()
            .appendField("Grove moisture sensor at")
            .appendField(new Blockly.FieldDropdown(analogPorts), "port");
        this.setInputsInline(true);
        this.setOutput(true, "Grove_Moisture_Sensor");
        this.setColour(140);
        this.setTooltip("");
        this.setHelpUrl("");
    },
    function(block) {
        var port = block.getFieldValue('port');
        Blockly.Python.definitions_.import_GroveDevices = "import GroveDevices";
        Blockly.Python.definitions_[`groveMoistureSensor_${port}`] = `groveMoistureSensor_${port} = GroveDevices.Grove_Moisture_Sensor("${port}")`;
        return [`groveMoistureSensor_${port}`, Blockly.Python.ORDER_ATOMIC];
    }
);


makeBlock('Grove_Moisture_Sensor__moistureLevel',
    function() {
        this.appendValueInput("sensor")
            .setCheck("Grove_Moisture_Sensor")
            .appendField("moisture level of");
        this.setInputsInline(true);
        this.setOutput(true, "Number");
        this.setColour(140);
        this.setTooltip("");
        this.setHelpUrl("");
    },
    function(block) {
        var sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
        return [`${sensor}.moistureLevel()`, Blockly.Python.ATOMIC];
    }
);


makeBlock('Grove_Sound_Sensor',
    function() {
        this.appendDummyInput()
            .appendField("Grove sound sensor at")
            .appendField(new Blockly.FieldDropdown(analogPorts), "port");
        this.setInputsInline(true);
        this.setOutput(true, "Grove_Sound_Sensor");
        this.setColour(160);
        this.setTooltip("");
        this.setHelpUrl("");
    },
    function(block) {
        var port = block.getFieldValue('port');
        Blockly.Python.definitions_.import_GroveDevices = "import GroveDevices";
        Blockly.Python.definitions_[`groveSoundSensor_${port}`] = `groveSoundSensor_${port} = GroveDevices.Grove_Sound_Sensor("${port}")`;
        return [`groveSoundSensor_${port}`, Blockly.Python.ORDER_ATOMIC];
    }
);


makeBlock('Grove_Sound_Sensor__soundIntensity',
    function() {
        this.appendValueInput("sensor")
            .setCheck("Grove_Sound_Sensor")
            .appendField("measured sound intensity of");
        this.setInputsInline(true);
        this.setOutput(true, "Number");
        this.setColour(160);
        this.setTooltip("");
        this.setHelpUrl("");
    },
    function(block) {
        var sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
        return [`${sensor}.soundIntensity()`, Blockly.Python.ATOMIC];
    }
);


makeBlock('Grove_Loudness_Sensor',
    function() {
        this.appendDummyInput()
            .appendField("Grove loudness sensor at")
            .appendField(new Blockly.FieldDropdown(analogPorts), "port");
        this.setInputsInline(true);
        this.setOutput(true, "Grove_Loudness_Sensor");
        this.setColour(180);
        this.setTooltip("");
        this.setHelpUrl("");
    },
    function(block) {
        var port = block.getFieldValue('port');
        Blockly.Python.definitions_.import_GroveDevices = "import GroveDevices";
        Blockly.Python.definitions_[`groveLoudnesSensor_${port}`] = `groveLoudnessSensor_${port} = GroveDevices.Grove_Loudness_Sensor("${port}")`;
        return [`groveLoudnessSensor_${port}`, Blockly.Python.ORDER_ATOMIC];
    }
);


makeBlock('Grove_Loudness_Sensor__detectSound',
    function() {
        this.appendValueInput("sensor")
            .setCheck("Grove_Loudness_Sensor")
            .appendField("detect sound of");
        this.setInputsInline(true);
        this.setOutput(true, "Number");
        this.setColour(180);
        this.setTooltip("");
        this.setHelpUrl("");
    },
    function(block) {
        var sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
        return [`${sensor}.detectSound()`, Blockly.Python.ATOMIC];
    }
);


makeBlock('Grove_Air_Quality_Sensor',
    function() {
        this.appendDummyInput()
            .appendField("Grove air quality sensor at")
            .appendField(new Blockly.FieldDropdown(analogPorts), "port");
        this.setInputsInline(true);
        this.setOutput(true, "Grove_Air_Quality_Sensor");
        this.setColour(200);
        this.setTooltip("");
        this.setHelpUrl("");
    },
    function(block) {
        var port = block.getFieldValue('port');
        Blockly.Python.definitions_.import_GroveDevices = "import GroveDevices";
        Blockly.Python.definitions_[`groveAirQualitySensor_${port}`] = `groveAirQualitySensor_${port} = GroveDevices.Grove_Air_Quality_Sensor("${port}")`;
        return [`groveAirQualitySensor_${port}`, Blockly.Python.ORDER_ATOMIC];
    }
);


makeBlock('Grove_Air_Quality_Sensor__airQuality',
    function() {
        this.appendValueInput("sensor")
            .setCheck("Grove_Air_Quality_Sensor")
            .appendField("measured air quality of");
        this.setInputsInline(true);
        this.setOutput(true, "Number");
        this.setColour(200);
        this.setTooltip("");
        this.setHelpUrl("");
    },
    function(block) {
        var sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
        return [`${sensor}.airQuality()`, Blockly.Python.ATOMIC];
    }
);


makeBlock('Grove_Air_Quality_Sensor__qualitativeMeasurement',
    function() {
        this.appendValueInput("sensor")
            .setCheck("Grove_Air_Quality_Sensor")
            .appendField("air quality description from");
        this.setInputsInline(true);
        this.setOutput(true, "Number");
        this.setColour(200);
        this.setTooltip("");
        this.setHelpUrl("");
    },
    function(block) {
        var sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
        return [`${sensor}.airQuality()`, Blockly.Python.ATOMIC];
    }
);
</script>
