# iZone-Python3-Hassbian
Home Assistant Custom Component for iZone AC Controller

Before you use this repositry... checkout this one (https://github.com/Swamp-Ig/izone_custom_component) which is made by someone that actually knows how to use Python! Unforunately it didnt work for me becuase I am using Hassbian which is running on Python 3.5. I think to Penny uses Home Assistant as a docker container running Python 3.6 or higher which was a bit beyond me.


So this is a work in progress and pretty rudimentary but functional version and it is working for me. I have some things on the To Do list that I will highlight first.

ToDo:
- Clean up sending function. Currently is sends Fan speed, operation mode, temperateure and on / off every time you change one of these parameters. Realistically it should just change the parameter that has been modified.
- pass the values into a single function to tidy up the code.
- Update HomeAssistant values based on information from the controller each time data is sent so if you mannually update the temp on the controller HA also gets that same value.
- Update HomeAssistant values each time the iZones broadcasts the current values.
- Get Google Home to see the current value and be able to control the AC via HA.


How to use:
Download all files to your Home Assistnat Config directory. If you have not already got one put a custom_components folder in your homeassistant directory. Inside that you will put my files so it will look like this: homeassistant/custom_components/climate/panasonic.py

Then add this to your configuration.yaml:

```climate:
  - platform: panasonic
    name: Panasonic
    host: 'IP_ADDRESS'
    mac: 'MAC_ADDRESS'
    min_temp: 16
    max_temp: 30
    target_temp: 23
    temp_sensor: sensor.aeotec_zw100_multisensor_6_temperature
    default_operation: idle
    default_fan_mode: medium
    customize:
      operations:
        - idle
        - auto
        - vent
        - dry
        - cool
        - heat
      fan_modes:
        - low
        - medium
        - high
        - auto ```
