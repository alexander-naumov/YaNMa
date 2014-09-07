#   Copyright (C) 2012-2014 Alexander Naumov <alexander_naumov@opensuse.org>

#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License Version 2 as
#   published by the Free Software Foundation.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

import sys, info, configure
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class NetworkSettings(QDialog):
	def __init__(self, parent=None):
		super(NetworkSettings, self).__init__(parent)
		
		dic_state = {				# https://developer.gnome.org/NetworkManager/unstable/spec.html#type-NM_DEVICE_STATE
				0  : "UNKNOWN",		# The device is in an unknown state.
				10 : "UNMANAGED",	# The device is recognized but not managed by NetworkManager.
				20 : "Unavailable", # The device cannot be used (carrier off, rfkill, etc).
				30 : "Disconnected",# The device is not connected.
				40 : "PREPARE",		# The device is preparing to connect.
				50 : "CONFIG",		# The device is being configured.
				60 : "NEED_AUTH",	# The device is awaiting secrets necessary to continue connection.
				70 : "IP_CONFIG",	# The IP settings of the device are being requested and configured.
				80 : "CHECK",		# The device's IP connectivity ability is being determined.
				90 : "SECONDARIES", # The device is waiting for secondary connections to be activated.
				100: "Activated",	# The device is active.
				110: "DEACTIVATING",# The device's network connection is being torn down.
				120: "FAILED"}		# The device is in a failure state following an attempt to activate it.

		dic_type = {				# https://developer.gnome.org/NetworkManager/unstable/spec.html#type-NM_DEVICE_TYPE
				0  : "UNKNOWN",		# The device type is unknown.
				1  : "Ethernet",	# The device is wired Ethernet device.
				2  : "Wireless",	# The device is an 802.11 WiFi device.
				5  : "Bluetooth",	# The device is Bluetooth device that provides PAN or DUN capabilities.
				6  : "OLPC_MESH",	# The device is an OLPC mesh networking device.
				7  : "WIMAX",		# The device is an 802.16e Mobile WiMAX device.
				8  : "Modem",		# The device is a modem supporting one or more of analog telephone,
									#  CDMA/EVDO, GSM/UMTS/HSPA, or LTE standards to access a cellular or wireline data network.
				9  : "INFINIBAND",	# The device is an IP-capable InfiniBand interface.
				10 : "BOND",		# The device is a bond master interface.
				11 : "VLAN",		# The device is a VLAN interface.
				12 : "ADSL",		# The device is an ADSL device supporting PPPoE and PPPoATM protocols.
				13 : "BRIDGE"}		# The device is a bridge interface.


		self.setGeometry(400, 500, 250, 150)
		self.setWindowTitle('Network Settings')
		self.setWindowIcon(QIcon('/usr/share/icons/oxygen/64x64/categories/applications-science.png'))
		mainLayout = QVBoxLayout()

		for iface in info.interfaces:
			dev_type = dic_type[int(iface['DeviceType'])]
			dev_state = dic_state[int(iface['State'])]


			label_interface = QLabel(' Interface\t'+ iface['Interface'])
			#label_type      = QLabel(' Type\t\t' + str(dev_type))
			label_state		= QLabel(' State\t\t' + str(dev_state))
			label_ip        = QLabel(' IP\t\t'+ iface['Ip4Address'])
			#label_gateway	= QLabel(' Gateway\t\t' + info.gateway)
			#label_conf		= QLabel(' IpInterface\t\t' + iface['IpInterface'])
			label_mac       = QLabel(' MAC' + '\t\t'+ iface['HwAddress'])
			label_driver    = QLabel(' Driver\t\t'+ iface['Driver'])
			#label_addr		= QLabel(' Addr\t\t' + info.addr_dotted)

			vLayoutInfo = QVBoxLayout()
			#vLayoutInfo.addWidget(label_type)
			vLayoutInfo.addWidget(label_interface)
			vLayoutInfo.addWidget(label_state)
			#vLayout.addWidget(label_conf)
			vLayoutInfo.addWidget(label_ip)
			vLayoutInfo.addWidget(label_mac)
			vLayoutInfo.addWidget(label_driver)

			vLayoutIface = QVBoxLayout()

			image = QLabel(" ")
			if dev_type == "Ethernet":
				if dev_state == "Activated":
					image.setPixmap(QPixmap.fromImage(QImage('/usr/share/icons/oxygen/64x64/devices/network-wired-activated.png')))
				else:
					image.setPixmap(QPixmap.fromImage(QImage('/usr/share/icons/oxygen/64x64/devices/network-wired.png')))
				
			elif dev_type == "Wireless": 
				if dev_state == "Activated":
					image.setPixmap(QPixmap.fromImage(QImage('/usr/share/icons/oxygen/64x64/devices/network-wireless.png')))
				else:
					image.setPixmap(QPixmap.fromImage(QImage('/usr/share/icons/oxygen/64x64/devices/network-wireless-disconnected.png')))
			
			#elif IfaceType == 5:	# BT: The device is Bluetooth device that provides PAN or DUN capabilities.

			elif dev_type == "Modem":
				image.setPixmap(QPixmap.fromImage(QImage('/usr/share/icons/oxygen/64x64/devices/modem.png')))	

			#elif IfaceType == 9:	# INFINIBAND : The device is an IP-capable InfiniBand interface. 
			#elif IfaceType == 11:	# VLAN: The device is a VLAN interface.
			#elif IfaceType == 12:	# ADSL: The device is an ADSL device supporting PPPoE and PPPoATM protocols.
			#elif IfaceType == 13:	# BRIDGE: The device is a bridge interface.
			else:
				print "The device type is unknown :(", dev_type

			configure = QPushButton('Configure', self)
			configure.setIcon(QIcon('/usr/share/icons/oxygen/64x64/actions/configure.png'))

			self.connect(configure, SIGNAL('clicked()'), lambda x=iface, y=dev_state, z=dev_type: self.config(x, y, z))

			vLayoutIface.addWidget(image)
			vLayoutIface.addWidget(configure)

			hLayoutIface = QHBoxLayout()
			hLayoutIface.addLayout(vLayoutInfo)
			hLayoutIface.addLayout(vLayoutIface)

			group = QGroupBox()
			group.setLayout(hLayoutIface)
			mainLayout.addWidget(group)

		quit = QPushButton('Ok', self)
		quit.setIcon(QIcon('/usr/share/icons/default.kde4/48x48/actions/dialog-ok-apply.png'))
		self.connect(quit, SIGNAL('clicked()'), self.accept)
	
		hLayout = QHBoxLayout()
		hLayout.addLayout(hLayoutIface)
		hLayout.addWidget(quit)

		mainLayout.addLayout(hLayout)

		self.setLayout(mainLayout)

	def config(self, iface, dev_state, dev_type):
		print dev_state
		import configure
		conf = configure.InterfaceConfiguration(iface, dev_state, dev_type, self)
		conf.exec_()

ns = NetworkSettings()

