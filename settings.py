#   Copyright 2012-20132-2013 Alexander Naumov <alexander_naumov@opensuse.org>

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
		
		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('Network Settings')

		label_interface = QLabel(' Interface : \t'+ info.name, self)
		label_mac       = QLabel(' MAC       : \t'+ info.HwAddress, self)
		label_ip        = QLabel(' IP        : \t'+ info.IP4, self)
		label_driver    = QLabel(' Driver    : \t'+ info.driver, self)

		configure = QPushButton('Configure', self)
		quit      = QPushButton('Ok',        self)
		
		self.connect(configure, SIGNAL('clicked()'), self.accept)
		self.connect(quit,      SIGNAL('clicked()'), self.accept)
		
		hLayout = QHBoxLayout()
		hLayout.addWidget(configure)
		hLayout.addWidget(quit)

		mainLayout = QVBoxLayout()
		mainLayout.addWidget(label_interface)
		mainLayout.addWidget(label_mac)
		mainLayout.addWidget(label_ip)
		mainLayout.addWidget(label_driver)
		mainLayout.addLayout(hLayout)

		self.setLayout(mainLayout)

#app = QtGui.QApplication(sys.argv)
ns = NetworkSettings()
#qb.show()
#sys.exit(app.exec_())

