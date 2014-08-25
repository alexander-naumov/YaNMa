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
	def __init__(self, parent=None):
		super(InterfaceConfiguration, self).__init__(parent)

		self.setGeometry(700, 700, 450, 250)
		self.setWindowTitle('Interface Configuration')


conf = InterfaceConfiguration()
