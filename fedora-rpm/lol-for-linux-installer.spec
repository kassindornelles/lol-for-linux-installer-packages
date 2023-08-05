%define _topdir %(pwd)

Name:           lol-for-linux-installer
Version:        2.5.6
Release:        1%{?dist}
Summary:        League of Legends installer and manager for Linux
License:        GPL-3.0
URL:            https://github.com/kassindornelles/lol-for-linux-installer
Source0:        https://github.com/kassindornelles/lol-for-linux-installer/archive/refs/tags/v.%{version}.tar.gz

BuildRequires:  wget

Requires:       python3
Requires:       python3-psutil
Requires:       python3-PyQt5
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

# Define the package build process
%description
%{summary}

%prep
%autosetup -n lol-for-linux-installer-v.%{version}

%install
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/share/lol-for-linux-installer
mkdir -p %{buildroot}/usr/share/applications
install -m755 src/com.kassindornelles.lolforlinuxinstaller.py %{buildroot}/usr/bin/com.kassindornelles.lolforlinuxinstaller
install -m644 src/launch-script.py %{buildroot}/usr/share/lol-for-linux-installer/launch-script.py
install -m644 src/vulkan_layers.py %{buildroot}/usr/share/lol-for-linux-installer/vulkan_layers.py
install -m644 src/env_vars.json %{buildroot}/usr/share/lol-for-linux-installer/env_vars.json
install -m644 src/lol-for-linux-installer.svg %{buildroot}/usr/share/lol-for-linux-installer/lol-for-linux-installer.svg
install -m644 src/leagueinstaller_code.py %{buildroot}/usr/share/lol-for-linux-installer/leagueinstaller_code.py
install -m644 src/com.kassindornelles.lolforlinuxinstaller.desktop %{buildroot}/usr/share/applications/com.kassindornelles.lolforlinuxinstaller.desktop
cp src/installer.ui %{buildroot}/usr/share/lol-for-linux-installer/installer.ui

%files
%doc README.md
%license license.md
/usr/bin/com.kassindornelles.lolforlinuxinstaller
/usr/share/lol-for-linux-installer/
/usr/share/applications/

%changelog
* Fri Aug 04 2023 Kassin Dornelles <kassin.dornelles@gmail.com> - 2.5.6-1
- Initial release
