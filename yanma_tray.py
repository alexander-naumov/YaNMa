#!/usr/bin/env python

#   Copyright 2012-2013 Alexander Naumov <alexander_naumov@opensuse.org>

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

show_info =  "Interface\t" + info.name + "\n" \
	     "IP Addr\t"  + info.IP4 + "\n" \
		 "MAC Addr\t" + info.HwAddress + "\n" \
	     "Driver\t"   + info.driver


class TrayBase(QSystemTrayIcon):
	def __init__(self, parent=None):
		super(TrayBase,self).__init__(parent)
		
		self.settings = QSettings()
		self.updateCheck = self.settings.value("checkboxes/update").toBool();

		self.tray = QSystemTrayIcon(self)
		self.trayMenu = QMenu()
		self.tray.setToolTip(show_info)
		
		self.action_wired    = QAction(QIcon("images/wired.png"), info.name+u' '+info.IP4, self)
		self.action_wireless = QAction(QIcon("images/wireless.png"), u'Wireless Networks', self)
		self.action_settings = QAction(QIcon("images/settings.png"), u'Network Settings', self)
		self.action_quit     = QAction(QIcon("images/quit.png"), u'Quit', self)

		self.trayMenu.addAction(self.action_wired)
		self.trayMenu.addSeparator()
		self.trayMenu.addAction(self.action_wireless)
		self.trayMenu.addSeparator()
		self.trayMenu.addAction(self.action_settings)
		self.trayMenu.addAction(self.action_quit)

		self.connect(self.action_wired, SIGNAL("triggered()"), self.wired)
		self.connect(self.action_wireless, SIGNAL("triggered()"), self.wireless)
		self.connect(self.action_settings, SIGNAL("triggered()"), self.net_settings)
		self.connect(self.action_quit, SIGNAL("triggered()"), self.quit)
		
		self.trayIcon = QIcon("images/applet_48x48.png")
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
	app = QApplication(sys.argv)
	
	if(QSystemTrayIcon.isSystemTrayAvailable() != 1 ):
		message = QMessageBox(self)
		message.setText(u'Could not detect system tray')
		message.setIcon(QMessageBox.Warning)
		message.addButton("Quit", QMessageBox.RejectRole)
		message.exec_()
		response = message.clickedButton().text()
		
		if response == "Quit":
			sys.exit()

	else:
		print u"YaNMa starting..."
		settings = QSettings()
		settings.setValue("popupmessages", QVariant(QSystemTrayIcon.supportsMessages()));
	
		app.setQuitOnLastWindowClosed(0)
		myob = TrayBase()
			
	sys.exit(app.exec_())
