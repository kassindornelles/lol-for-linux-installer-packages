%define _topdir %(pwd)

Name:           lol-for-linux-installer
Version:        2.6.5
Release:        1%{?dist}
Summary:        League of Legends installer and manager for Linux
License:        GPL-3.0
URL:            https://github.com/kassindornelles/lol-for-linux-installer
Source0:        https://github.com/kassindornelles/lol-for-linux-installer/archive/refs/tags/v.%{version}.tar.gz

BuildRequires:  wget

Requires:       python3
Requires:       python3-psutil
Requires:       python3-PyQt5
Requires:       python3-pip
Requires:       python3-cffi
Requires:       /usr/bin/wine
Requires:       python3-requests
Requires:       qt5-qtbase
Requires:       tar
Requires:       gnutls
Requires:       openldap-compat
Requires:       libpng
Requires:       mesa-libGL
Requires:       libgphoto2
Requires:       wine


# Define the package build process
%description
%{summary}

%prep
%autosetup -n lol-for-linux-installer-v.%{version}

%install
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/share/lol-for-linux-installer
mkdir -p %{buildroot}/usr/share/applications
install -m755 src/lolforlinuxinstaller.py %{buildroot}/usr/bin/lolforlinuxinstaller
install -m644 src/launch-script.py %{buildroot}/usr/share/lol-for-linux-installer/launch-script.py
install -m644 src/vulkan_layers.py %{buildroot}/usr/share/lol-for-linux-installer/vulkan_layers.py
install -m644 src/env_vars.json %{buildroot}/usr/share/lol-for-linux-installer/env_vars.json
install -m644 src/lolforlinuxinstaller.svg %{buildroot}/usr/share/lol-for-linux-installer/lolforlinuxinstaller.svg
install -m644 src/leagueinstaller_code.py %{buildroot}/usr/share/lol-for-linux-installer/leagueinstaller_code.py
install -m644 src/lolforlinuxinstaller.desktop %{buildroot}/usr/share/applications/lolforlinuxinstaller.desktop
cp src/installer.ui %{buildroot}/usr/share/lol-for-linux-installer/installer.ui

%files
%doc README.md
%license license.md
/usr/bin/lolforlinuxinstaller
/usr/share/lol-for-linux-installer/
/usr/share/applications/

%changelog
* Tue Dec 30 2023 Kassin Dornelles <kassin.dornelles@gmail.com> - 2.6.5-1
- Initial release
