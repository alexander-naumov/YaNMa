#   Copyright 2012-2014 Alexander Naumov <alexander_naumov@opensuse.org>

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
		
		dic_state = {
				0  : "UNKNOWN",
				10 : "UNMANAGED",
				20 : "UNAVAILABLE",
				30 : "DISCONNECTED",
				40 : "PREPARE",
				50 : "CONFIG",
				60 : "NEED_AUTH",
				70 : "IP_CONFIG",
				100: "ACTIVATED",
				110: "DEACTIVATING",
				120: "FAILED"}

		self.setGeometry(400, 500, 250, 150)
		self.setWindowTitle('Network Settings')
		self.setWindowIcon(QIcon('/usr/share/icons/oxygen/64x64/categories/applications-science.png'))
		mainLayout = QVBoxLayout()

		for iface in info.interfaces:
			IfaceState = int(iface['State'])        #https://developer.gnome.org/NetworkManager/unstable/spec.html#type-NM_DEVICE_STATE

			label_interface = QLabel(' Interface\t'+ iface['Interface'], self)
			#label_type      = QLabel(' Type\t\t' + str(info.data['DeviceType']), self)
			label_state		= QLabel(' State\t\t' + str(dic_state[IfaceState]), self)
			label_ip        = QLabel(' IP\t\t'+ iface['Ip4Address'], self)
			#label_gateway	= QLabel(' Gateway\t\t' + info.gateway, self)
			#label_conf		= QLabel(' IpInterface\t\t' + iface['IpInterface'], self)
			label_mac       = QLabel(' MAC\t\t'+ iface['HwAddress'], self)
			label_driver    = QLabel(' Driver\t\t'+ iface['Driver'], self)
			#label_addr		= QLabel(' Addr\t\t' + info.addr_dotted, self)

			vLayoutInfo = QVBoxLayout()
			vLayoutInfo.addWidget(label_interface)
			#vLayoutInfo.addWidget(label_type)
			vLayoutInfo.addWidget(label_state)
			#vLayout.addWidget(label_conf)
			vLayoutInfo.addWidget(label_ip)
			vLayoutInfo.addWidget(label_mac)
			vLayoutInfo.addWidget(label_driver)

			vLayoutIface = QVBoxLayout()

			image_label = QLabel(" ")
			IfaceType = int(iface['DeviceType'])	#https://developer.gnome.org/NetworkManager/unstable/spec.html#type-NM_DEVICE_TYPE

			if IfaceType == 1:
				if IfaceState == 20: 
					image_label.setPixmap(QPixmap.fromImage(QImage('/usr/share/icons/oxygen/64x64/devices/network-wired.png')))
				elif IfaceState == 100:
					image_label.setPixmap(QPixmap.fromImage(QImage('/usr/share/icons/oxygen/64x64/devices/network-wired-activated.png')))
				
			elif IfaceType == 2: 
				if IfaceState == 20 or IfaceState == 30:
					image_label.setPixmap(QPixmap.fromImage(QImage('/usr/share/icons/oxygen/64x64/devices/network-wireless-disconnected.png')))
				elif IfaceState == 100:
					image_label.setPixmap(QPixmap.fromImage(QImage('/usr/share/icons/oxygen/64x64/devices/network-wireless.png')))
			
			#elif IfaceType == 5:	# BT: The device is Bluetooth device that provides PAN or DUN capabilities.
			#elif IfaceType == 8:	# MODEM: The device is a modem supporting one or more of analog telephone, CDMA/EVDO, GSM/UMTS/HSPA,
									# or LTE standards to access a cellular or wireline data network.
			#elif IfaceType == 9:	# INFINIBAND : The device is an IP-capable InfiniBand interface. 
			#elif IfaceType == 11:	# VLAN: The device is a VLAN interface.
			#elif IfaceType == 12:	# ADSL: The device is an ADSL device supporting PPPoE and PPPoATM protocols.
			#elif IfaceType == 13:	# BRIDGE: The device is a bridge interface.
			else:
				print "The device type is unknown :(", IfaceType

			configure = QPushButton('Configure', self)
			configure.setIcon(QIcon('/usr/share/icons/oxygen/64x64/actions/configure.png'))
			self.connect(configure, SIGNAL('clicked()'), lambda x=iface, state=str(dic_state[IfaceState]): self.config(x, state))

			vLayoutIface.addWidget(image_label)
			vLayoutIface.addWidget(configure)

			hLayoutIface = QHBoxLayout()
			hLayoutIface.addLayout(vLayoutInfo)
			hLayoutIface.addLayout(vLayoutIface)

			group = QGroupBox()
			group.setLayout(hLayoutIface)
			mainLayout.addWidget(group)

		quit = QPushButton('Ok', self)
		self.connect(quit, SIGNAL('clicked()'), self.accept)
	
		hLayout = QHBoxLayout()
		hLayout.addLayout(hLayoutIface)
		hLayout.addWidget(quit)

		mainLayout.addLayout(hLayout)

		self.setLayout(mainLayout)

	def config(self, iface, state):
		print state
		import configure
		conf = configure.InterfaceConfiguration(iface, state, self)
		conf.exec_()

ns = NetworkSettings()

