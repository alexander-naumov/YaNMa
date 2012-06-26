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

import dbus
import binascii

bus = dbus.SystemBus()

nm = bus.get_object("org.freedesktop.NetworkManager", "/org/freedesktop/NetworkManager/Devices/0")
prop_iface = dbus.Interface(nm, "org.freedesktop.DBus.Properties")

name          = prop_iface.Get("org.freedesktop.NetworkManager.Device", "Interface")
driver        = prop_iface.Get("org.freedesktop.NetworkManager.Device", "Driver")
IpInterface   = prop_iface.Get("org.freedesktop.NetworkManager.Device", "IpInterface")
Capabilities  = prop_iface.Get("org.freedesktop.NetworkManager.Device", "Capabilities")
Ip4Address    = prop_iface.Get("org.freedesktop.NetworkManager.Device", "Ip4Address")
State         = prop_iface.Get("org.freedesktop.NetworkManager.Device", "State")
Ip4Config     = prop_iface.Get("org.freedesktop.NetworkManager.Device", "Ip4Config")
Dhcp4Config   = prop_iface.Get("org.freedesktop.NetworkManager.Device", "Dhcp4Config")
Ip6Config     = prop_iface.Get("org.freedesktop.NetworkManager.Device", "Ip6Config")
Managed       = prop_iface.Get("org.freedesktop.NetworkManager.Device", "Managed")
DeviceType    = prop_iface.Get("org.freedesktop.NetworkManager.Device", "DeviceType")

#PermHwAddress = prop_iface.Get("org.freedesktop.NetworkManager.Device.Wired", "PermHwAddress")
HwAddress     = prop_iface.Get("org.freedesktop.NetworkManager.Device.Wired", "HwAddress")


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


#print IP4Addr(Ip4Address)
IP4 = str(IP4Addr(Ip4Address))

