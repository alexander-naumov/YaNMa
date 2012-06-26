#   Copyright 2011 Alexander Naumov <alexander_naumov@opensuse.org>

#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License Version 2 as
#   published by the Free Software Foundation.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

import sys, info
from PyQt4 import QtGui, QtCore

class NetworkSettings(QtGui.QWidget):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)

	        self.setGeometry(300, 300, 250, 150)
	        self.setWindowTitle('Network Settings')

		#self.mainWidget = QtGui.QWidget(self)

		label_interface = QtGui.QLabel(' Interface : '+ info.name, self)
		label_mac       = QtGui.QLabel(' MAC       : '+ info.HwAddress, self)
		label_ip        = QtGui.QLabel(' IP        : '+ info.IP4, self)
		label_driver    = QtGui.QLabel(' Driver    : '+ info.driver, self)

		configure = QtGui.QPushButton('Configure', self)
                quit      = QtGui.QPushButton('Ok',        self)
		
		self.connect(configure, QtCore.SIGNAL('clicked()'), QtGui.qApp, QtCore.SLOT('quit()'))		
		self.connect(quit,      QtCore.SIGNAL('clicked()'), QtGui.qApp, QtCore.SLOT('quit()'))
		
		hLayout = QtGui.QHBoxLayout()
		hLayout.addWidget(configure)
		hLayout.addWidget(quit)

		mainLayout = QtGui.QVBoxLayout()
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

