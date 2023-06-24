# Maintainer: Kassin Dornelles <kassin.dornelles@gmail.com>
Name: lol-for-linux-installer
Version: 2.5.1
Release: 1%{?dist}
Summary: League of Legends installer and manager for Linux
License: GPL-3.0
URL: https://github.com/kassindornelles/lol-for-linux-installer
Source0: https://github.com/kassindornelles/lol-for-linux-installer/archive/refs/tags/v.%{version}.tar.gz
BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-psutil
BuildRequires: python3-pyqt5
BuildRequires: python3-cffi
BuildRequires: wine
BuildRequires: python3-requests
BuildRequires: python3-pyqt5-qtwebkit
BuildRequires: tar
BuildRequires: gnutls-devel
BuildRequires: gnutls-devel.i686
BuildRequires: openldap-devel
BuildRequires: openldap-devel.i686
BuildRequires: libpng-devel
BuildRequires: libpng-devel.i686
BuildRequires: gphoto2-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: pulseaudio-libs-devel.i686

Requires: python3
Requires: python3-psutil
Requires: python3-pyqt5
Requires: python3-cffi
Requires: wine
Requires: python3-requests
Requires: python3-pyqt5-qtwebkit
Requires: tar
Requires: libgnutls30
Requires: libgnutls30.i686
Requires: libldap-2.5-0
Requires: libldap-2.5-0.i686
Requires: libpng16-16
Requires: libpng16-16.i686
Requires: gphoto2
Requires: libpulse0
Requires: libpulse0.i686

%description
League of Legends installer and manager for Linux.

%prep
%autosetup -p1

%build
# No build step required

%install
%py3_install

%files
%license LICENSE
%doc README.md
%{_bindir}/lol-for-linux-installer
%{_datadir}/lol-for-linux-installer
%{_datadir}/applications/lol-for-linux-installer.desktop

%changelog
* Thu Jun 24 2023 Kassin Dornelles <kassin.dornelles@gmail.com> - 2.5.1-1
- Initial RPM release
