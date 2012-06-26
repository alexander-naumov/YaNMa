#!/usr/bin/env python

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
from PyQt4 import Qt, QtCore, QtGui

from PyQt4 import *

show_info =  "Interface\t" + info.name + "\n" \
	     "IP Addr\t" + info.IP4 + "\n" \
             "MAC Addr\t" + info.HwAddress + "\n" \
	     "Driver\t" + info.driver


class TrayBase(QtGui.QWidget):
	def __init__(self, *args):
		apply(QtGui.QWidget.__init__,(self, ) + args)
		
		self.settings = QtCore.QSettings()
		self.updateCheck = self.settings.value("checkboxes/update").toBool();

		self.tray = QtGui.QSystemTrayIcon(self)
		self.trayMenu = QtGui.QMenu()
		self.tray.setToolTip(show_info)
		
		#self.action_wired = QtGui.QAction(QtGui.QIcon("images/wired.png"), u'Wired Networks', self)
		self.action_wired = QtGui.QAction(QtGui.QIcon("images/wired.png"), info.name+u' '+info.IP4, self)
		self.action_wireless = QtGui.QAction(QtGui.QIcon("images/wireless.png"), u'Wireless Networks', self)
		self.action_settings = QtGui.QAction(QtGui.QIcon("images/settings.png"), u'Network Settings', self)
		self.action_quit = QtGui.QAction(QtGui.QIcon("images/quit.png"), u'Quit', self)

		self.trayMenu.addAction(self.action_wired)
		self.trayMenu.addSeparator()
		self.trayMenu.addAction(self.action_wireless)
		self.trayMenu.addSeparator()
		self.trayMenu.addAction(self.action_settings)
		self.trayMenu.addAction(self.action_quit)

		self.connect(self.action_wired, QtCore.SIGNAL("triggered()"), self.wired)
		self.connect(self.action_wireless, QtCore.SIGNAL("triggered()"), self.wireless)
		self.connect(self.action_settings, QtCore.SIGNAL("triggered()"), self.net_settings)
		self.connect(self.action_quit, QtCore.SIGNAL("triggered()"), self.quit)
		
		self.trayIcon = QtGui.QIcon("images/applet_48x48.png")
		self.tray.setContextMenu(self.trayMenu)
		self.tray.setIcon(self.trayIcon)
		
		self.tray.show()
		
	def wired(self):
		pass

	def wireless(self):
		pass

	def net_settings(self):
		import settings 
		settings.ns.show()

	def quit(self):
		print u"Quit"
		sys.exit()

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	
	if( QtGui.QSystemTrayIcon.isSystemTrayAvailable() != 1 ):
		message = QtGui.QMessageBox(self)
		message.setText(u'Could not detect system tray')
		message.setIcon(QtGui.QMessageBox.Warning)
		message.addButton("Quit", QtGui.QMessageBox.RejectRole)
		message.exec_()
		response = message.clickedButton().text()
		
		if response == "Quit":
			sys.exit()

	else:
		print u"YaNMa starting..."
		settings = QtCore.QSettings()
		settings.setValue("popupmessages", QtCore.QVariant(QtGui.QSystemTrayIcon.supportsMessages()));
	
		app.setQuitOnLastWindowClosed(0)
		myob = TrayBase()
			
	sys.exit(app.exec_())
