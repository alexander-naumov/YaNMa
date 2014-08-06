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

		label_interface = QLabel(' Interface\t'+ info.data['Interface'], self)
#		label_type      = QLabel(' Type\t\t' + str(info.data['DeviceType']), self)
		#label_state     = QLabel(' State\t\t' + str(info.state), self)
		label_ip        = QLabel(' IP\t\t'+ info.IP4, self)
		##label_gateway	= QLabel(' Gateway\t\t' + info.gateway, self)
		label_mac       = QLabel(' MAC\t\t'+ info.data['HwAddress'], self)
		label_driver    = QLabel(' Driver\t\t'+ info.data['Driver'], self)
		#label_addr		= QLabel(' Addr\t\t' + info.addr_dotted, self)


		configure = QPushButton('Configure', self)
		quit      = QPushButton('Ok',        self)
		
		self.connect(configure, SIGNAL('clicked()'), self.accept)
		self.connect(quit,      SIGNAL('clicked()'), self.accept)
		
		hLayout = QHBoxLayout()
		hLayout.addWidget(configure)
		hLayout.addWidget(quit)

		mainLayout = QVBoxLayout()
		#mainLayout.addWidget(label_type)
		#mainLayout.addWidget(label_state)
		mainLayout.addWidget(label_interface)
		mainLayout.addWidget(label_ip)
		mainLayout.addWidget(label_mac)
		mainLayout.addWidget(label_driver)
		##mainLayout.addWidget(label_addr)
		mainLayout.addLayout(hLayout)

		self.setLayout(mainLayout)

#app = QtGui.QApplication(sys.argv)
ns = NetworkSettings()
#qb.show()
#sys.exit(app.exec_())

