import os


def displayAvailableNetworks(interface):
    command = "netsh wlan show networks interface=\"" + interface + "\""
    os.system(command)


def createNewConnection(name, SSID, password, interface):
    config = """<?xml version=\"1.0\"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
	<name>""" + name + """</name>
	<SSIDConfig>
		<SSID>
			<name>""" + SSID + """</name>
		</SSID>
	</SSIDConfig>
	<connectionType>ESS</connectionType>
	<connectionMode>auto</connectionMode>
	<MSM>
		<security>
			<authEncryption>
				<authentication>WPA2PSK</authentication>
				<encryption>AES</encryption>
				<useOneX>false</useOneX>
			</authEncryption>
			<sharedKey>
				<keyType>passPhrase</keyType>
				<protected>false</protected>
				<keyMaterial>""" + password + """</keyMaterial>
			</sharedKey>
		</security>
	</MSM>
</WLANProfile>"""
    command = "netsh wlan add profile filename=\"" + name + ".xml\"" + " interface=\"" + interface + "\"" + " user=all"
    # command = "netsh wlan add profile filename=\"" + name + ".xml\"" + " interface='Wi-Fi 2' user=all"
    with open(name + ".xml", 'w') as file:
        file.write(config)
    os.system(command)


def connect(name, SSID, interface):
    command = "netsh wlan connect name=\"" + name + "\" ssid=\"" + SSID + "\" interface=\"" + interface + "\""
    os.system(command)


def DeleteNetworks(name):
    Delcommand = "netsh wlan delete profile name=\"" + name + "\""
    os.system(Delcommand)
