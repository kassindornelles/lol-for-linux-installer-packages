Name:           lol-for-linux-installer
Version:        2.5.2
Release:        1%{?dist}
Summary:        League of Legends installer and manager for Linux
License:        GPL-3.0
URL:            https://github.com/kassindornelles/lol-for-linux-installer
Source0:        https://github.com/kassindornelles/lol-for-linux-installer/archive/refs/tags/v.%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-psutil
BuildRequires:  python3-PyQt5
BuildRequires:  python3-cffi
BuildRequires:  wine
BuildRequires:  python3-requests
BuildRequires:  qt5-qtbase-devel
BuildRequires:  tar
BuildRequires:  gnutls
BuildRequires:  openldap-compat
BuildRequires:  libpng
BuildRequires:  mesa-libGL-devel
BuildRequires:  libgphoto2-devel
BuildRequires:  python3-setuptools

Requires:       python3
Requires:       python3-psutil
Requires:       python3-PyQt5
Requires:       python3-cffi
Requires:       wine
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

install -m755 src/lol-for-linux-installer.py %{buildroot}/usr/bin/lol-for-linux-installer
install -m644 src/launch-script.py %{buildroot}/usr/share/lol-for-linux-installer/launch-script.py
install -m644 src/vulkan_layers.py %{buildroot}/usr/share/lol-for-linux-installer/vulkan_layers.py
install -m644 src/env_vars.json %{buildroot}/usr/share/lol-for-linux-installer/env_vars.json
install -m644 src/lol-for-linux-installer.png %{buildroot}/usr/share/lol-for-linux-installer/lol-for-linux-installer.png
install -m644 src/leagueinstaller_code.py %{buildroot}/usr/share/lol-for-linux-installer/leagueinstaller_code.py
install -m644 src/lol-for-linux-installer.desktop %{buildroot}/usr/share/applications/lol-for-linux-installer.desktop
cp src/installer.ui %{buildroot}/usr/share/lol-for-linux-installer/installer.ui

%files
%doc README.md
%license license.md
/usr/bin/lol-for-linux-installer
/usr/share/lol-for-linux-installer/
/usr/share/applications/

%changelog
* Sun Jun 25 2023 Kassin Dornelles <kassin.dornelles@gmail.com> - 2.5.1-1
- Initial release


