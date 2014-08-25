#   Copyright 2012-2014 Alexander Naumov <alexander_naumov@opensuse.org>

#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License Version 2 as
#   published by the Free Software Foundation.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

import sys, info
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class NetworkSettings(QDialog):
	def __init__(self, parent=None):
		super(NetworkSettings, self).__init__(parent)
		
		self.setGeometry(400, 500, 250, 150)
		self.setWindowTitle('Network Settings')
		mainLayout = QVBoxLayout()

		#configure = QPushButton('Configure', self)
		quit      = QPushButton('Ok',        self)
				        
		#self.connect(configure, SIGNAL('clicked()'), self.accept)
		self.connect(quit,      SIGNAL('clicked()'), self.accept)

		for iface in info.interfaces:
			#print iface
			label_interface = QLabel(' Interface\t'+ iface['Interface'], self)
			label_type      = QLabel(' Type\t\t' + str(info.data['DeviceType']), self)
			label_state		= QLabel(' State\t\t' + str(info.data['State']), self)
			label_ip        = QLabel(' IP\t\t'+ iface['Ip4Address'], self)
			#label_gateway	= QLabel(' Gateway\t\t' + info.gateway, self)
			#label_conf		= QLabel(' IpInterface\t\t' + iface['IpInterface'], self)
			label_mac       = QLabel(' MAC\t\t'+ iface['HwAddress'], self)
			label_driver    = QLabel(' Driver\t\t'+ iface['Driver'], self)
			#label_addr		= QLabel(' Addr\t\t' + info.addr_dotted, self)

			vLayoutInfo = QVBoxLayout()
			vLayoutInfo.addWidget(label_interface)
			vLayoutInfo.addWidget(label_type)
			vLayoutInfo.addWidget(label_state)
			#vLayout.addWidget(label_conf)
			vLayoutInfo.addWidget(label_ip)
			vLayoutInfo.addWidget(label_mac)
			vLayoutInfo.addWidget(label_driver)

			vLayoutIface = QVBoxLayout()

			image_label = QLabel(" ")
			image_label.setPixmap(QPixmap.fromImage(QImage('/usr/share/icons/oxygen/64x64/devices/network-wired-activated.png')))

			configure = QPushButton('Configure', self)
			self.connect(configure, SIGNAL('clicked()'), self.accept)

			vLayoutIface.addWidget(image_label)
			vLayoutIface.addWidget(configure)

			hLayoutIface = QHBoxLayout()
			hLayoutIface.addLayout(vLayoutInfo)
			hLayoutIface.addLayout(vLayoutIface)

			group = QGroupBox()
			group.setLayout(hLayoutIface)
			mainLayout.addWidget(group)


		#configure = QPushButton('Configure', self)
		#quit      = QPushButton('Ok',        self)
		
		#self.connect(configure, SIGNAL('clicked()'), self.accept)
		#self.connect(quit,      SIGNAL('clicked()'), self.accept)
		
		hLayout = QHBoxLayout()
		hLayout.addLayout(hLayoutIface)
		hLayout.addWidget(quit)

		mainLayout.addLayout(hLayout)

		self.setLayout(mainLayout)

ns = NetworkSettings()

