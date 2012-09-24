#
# spec file for package YaNMa 
#
# Copyright (c) 2012 Alexander Naumov <alexander_naumov@opensuse.org>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name:           YaNMa
Version:
Release:
License:	GPLv2
Summary:	PySide NetworkManager applet
Url:		https://github.com/alexander-naumov/YaNMa
Group:		Network
Source:		%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
YaNMa - Yet another NetworkManager applet.
PyQt4/PySide study project.


%prep
%setup -q

%build
%install
ls -la
mkdir -p $RPM_BUILD_ROOT/usr/share/yanma

#%{_install} -d %(buildroot)/usr/share/yanma
mv *.py $RPM_BUILD_ROOT/usr/share/yanma

%clean
%{?buildroot:%__rm -rf "%{buildroot}"}

%post

%postun

%files
%defattr(-,root,root)
#%doc ChangeLog README COPYING
/usr/share/yanma/info.py
/usr/share/yanma/settings.py
/usr/share/yanma/yanma_tray.py

/usr/share/yanma/images/wireless.png
/usr/share/yanma/images/wired.png
/usr/share/yanma/images/settings.png
/usr/share/yanma/images/quit.png
/usr/share/yanma/images/applet_48x48.png


%changelog
* Fri Sep 21 2012 - alexander_naumov@opensuse.org
- first version
