import pycurl
import json
import requests
from io import BytesIO

onENDPOINT = 'http://192.168.0.139/SystemON'        #{"SystemON":"x"} "on" "off"
dataOn = {'SystemON':'on'}

zoneENDPOINT = 'http://192.168.0.139/ZoneCommand' 
zoneCommand = {         #x - is zone number y - is: "open" - to open the zone "close" - to close
    'ZoneCommand':{
      'ZoneNo':'5',
      'Command':'open'
    }
}

SettingsENDPOINT = 'http://192.168.0.139/SystemSettings'
Statuszone14ENDPOINT = 'http://192.168.0.139/Zones1_4'
Statuszone58ENDPOINT = 'http://192.168.0.139/Zones5_8'


#buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, zoneENDPOINT)
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, json.dumps(zoneCommand))
#c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()
#body = buffer.getvalue()
#print(body)

rx = requests.get(SettingsENDPOINT)    #gets general system info excluding zone info
#print(rx.text)

loaded_json = json.loads(rx.text)   #format AC response into new line for each parameter
for x in loaded_json:
	print("%s: %s" % (x, loaded_json[x]))

class sysInfo(object):
    def __init__(self, data):
        self.__dict__ = json.loads(rx.text)

acInfo = sysInfo(rx.text)

SystemOn = acInfo.SysOn
SetPoint = acInfo.Setpoint
FanSpeed = acInfo.SysFan

print(SetPoint)

print("Zone Info:")
rx14 = requests.get(Statuszone14ENDPOINT)
zone14Json = rx14.text
rx58 = requests.get(Statuszone58ENDPOINT)
zone58Json = rx58.text
#print(zone58Json)

# parse zonelist:
z14 = json.loads(zone14Json) # the result is a Python dictionary:
z58 = json.loads(zone58Json) # the result is a Python dictionary:

#print("Zone 1 Info:")
#print(len(z14))
#print(z14[0])

zone = []

for entry in z14:             #zone 1 - 4
    info = entry['Name']
    mode = entry['Mode']
    zone.append(entry['Mode'])
    print(info + ":" + mode)


for entry in z58:            #zone 1 - 4
    info = entry['Name']
    mode = entry['Mode']
    zone.append(entry['Mode'])
    print(info + ":" + mode)

#print(zone)
print(zone[1])

#acInfo = sysInfo(rx14.text)

#zone1Name = acInfo.Name
#zone1Mode = acInfo.Mode

#print(zone1Mode)