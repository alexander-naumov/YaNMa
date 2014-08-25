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
import binascii

class IP4Addr(object):
	def __init__(self, int32):
		self.a = int32
	def __str__(self):
		ret = []
		i32 = self.a
		for i in range(4):
			ret.append("%d" % (i32 % 256))
			i32 /= 256
		return ".".join(ret)


bus = dbus.SystemBus()

try:
	nm = bus.get_object("org.freedesktop.NetworkManager", "/org/freedesktop/NetworkManager")
except:
	print "NetworkManager is not running..."
	sys.exit()

prop_iface = dbus.Interface(nm, "org.freedesktop.DBus.Properties")
i = prop_iface.GetAll('org.freedesktop.NetworkManager')

print i['ActiveConnections'][0]
print i['Connectivity']

nm1 = bus.get_object("org.freedesktop.NetworkManager", i['ActiveConnections'][0])
prop_iface1 = dbus.Interface(nm, "org.freedesktop.NetworkManager")

interfaces = []
for dev in prop_iface1.GetDevices():
	dev_proxy = bus.get_object("org.freedesktop.NetworkManager", dev)
	prop_iface = dbus.Interface(dev_proxy, "org.freedesktop.DBus.Properties")

	interface = prop_iface.Get("org.freedesktop.NetworkManager.Device", "Interface")

	data = {}
	data['Interface'] 	= interface
	data['Driver'] 		= prop_iface.Get("org.freedesktop.NetworkManager.Device", "Driver")
	data['IpInterface']	= prop_iface.Get("org.freedesktop.NetworkManager.Device", "IpInterface")
	data['Capabilities']= prop_iface.Get("org.freedesktop.NetworkManager.Device", "Capabilities")

	data['Ip4Address']  = prop_iface.Get("org.freedesktop.NetworkManager.Device", "Ip4Address")
	data['Ip4Address']  = str(IP4Addr(data['Ip4Address']))

	data['State']		= prop_iface.Get("org.freedesktop.NetworkManager.Device", "State")
	data['Ip4Config']	= prop_iface.Get("org.freedesktop.NetworkManager.Device", "Ip4Config")
	data['Dhcp4Config'] = prop_iface.Get("org.freedesktop.NetworkManager.Device", "Dhcp4Config")
	data['Ip6Config']	= prop_iface.Get("org.freedesktop.NetworkManager.Device", "Ip6Config")
	data['Managed']		= prop_iface.Get("org.freedesktop.NetworkManager.Device", "Managed")
	data['DeviceType']	= prop_iface.Get("org.freedesktop.NetworkManager.Device", "DeviceType")

	try:
		data['HwAddress']	= prop_iface.Get("org.freedesktop.NetworkManager.Device.Wired", "HwAddress")
	except:
		data['HwAddress']   = prop_iface.Get("org.freedesktop.NetworkManager.Device.Wireless", "HwAddress")

	interfaces.append(data)

for i in interfaces:
	print i
