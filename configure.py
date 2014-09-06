#!/usr/bin/env python

#   Copyright 2011-2014 Alexander Naumov <alexander_naumov@opensuse.org>

#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License Version 2 as
#   published by the Free Software Foundation.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

import dbus, sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class InterfaceConfiguration(QDialog):
	def __init__(self, iface, state, parent=None):
		super(InterfaceConfiguration, self).__init__(parent)

		self.setGeometry(700, 700, 450, 250)
		self.setWindowTitle('Interface Configuration')
		self.setWindowIcon(QIcon('/usr/share/icons/oxygen/64x64/categories/preferences-system.png'))

		for i in iface:
			print i, iface[i]


		label_state     = QLabel(' State ')
		label_interface = QLabel(' Interface ')
		#label_type      = QLabel(' Type\t\t' + str(info.data['DeviceType']), self)
		label_ip        = QLabel(' IP ')
		label_dhcp4conf = QLabel(' Dhcp4Config ')
		#label_gateway  = QLabel(' Gateway\t\t' + info.gateway, self)
		#label_conf     = QLabel(' IpInterface\t\t' + iface['IpInterface'], self)
		label_mac       = QLabel(' MAC ')
		label_driver    = QLabel(' Driver ')
		#label_cap 		= QLabel('Capabilities')

		value_State         = QLabel(state)
		value_Interface		= QLabel(iface['Interface'])
		value_Ip4Address	= QLineEdit(iface['Ip4Address'])
		value_Dhcp4Config	= QLabel(iface['Dhcp4Config']) 
		value_HwAddress		= QLabel(iface['HwAddress'])
		value_Driver		= QLabel(iface['Driver'])
		#value_Capabilities	= QLabel(iface['Capabilities'])

		quit = QPushButton('Ok', self)
		self.connect(quit, SIGNAL('clicked()'), self.accept)

		mainLayout = QVBoxLayout()

		hLayout_State = QHBoxLayout()
		hLayout_State.addWidget(label_state)
		hLayout_State.addWidget(value_State)

		hLayout_Interface = QHBoxLayout()
		hLayout_Interface.addWidget(label_interface)
		hLayout_Interface.addWidget(value_Interface)

		hLayout_IP = QHBoxLayout()
		hLayout_IP.addWidget(label_ip)
		hLayout_IP.addWidget(value_Ip4Address)

		hLayout_Dhcp = QHBoxLayout()
		hLayout_Dhcp.addWidget(label_dhcp4conf)
		hLayout_Dhcp.addWidget(value_Dhcp4Config)

		hLayout_MAC = QHBoxLayout()
		hLayout_MAC.addWidget(label_mac)
		hLayout_MAC.addWidget(value_HwAddress)

		hLayout_Driver = QHBoxLayout()
		hLayout_Driver.addWidget(label_driver)
		hLayout_Driver.addWidget(value_Driver)

		#hLayout_Capabilities = QHBoxLayout()
		#hLayout_Capabilities.addWidget(label_cap)
		#hLayout_Capabilities.addWidget(value_Capabilities)

		mainLayout.addLayout(hLayout_State)
		mainLayout.addLayout(hLayout_Interface)
		mainLayout.addLayout(hLayout_IP)
		mainLayout.addLayout(hLayout_Dhcp)
		mainLayout.addLayout(hLayout_MAC)
		mainLayout.addLayout(hLayout_Driver)
		#mainLayout.addLayout(hLayout_Capabilities)
		
		mainLayout.addWidget(quit)
		self.setLayout(mainLayout)

#conf = InterfaceConfiguration()
