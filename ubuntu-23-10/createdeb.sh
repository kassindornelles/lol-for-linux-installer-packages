#!/bin/bash

PKG_NAME="lol-for-linux-installer-ubuntu-23-10"
PKG_VER="2.6.5"
PKG_REL="1"

mkdir -p temp-directory/DEBIAN
mkdir -p temp-directory/usr/bin
mkdir -p temp-directory/usr/share/lol-for-linux-installer
mkdir -p temp-directory/usr/share/applications

curl -L -o temp-directory/source.tar.gz https://github.com/kassindornelles/lol-for-linux-installer/archive/refs/tags/v.$PKG_VER.tar.gz

tar -xzvf temp-directory/source.tar.gz -C temp-directory/
rm temp-directory/source.tar.gz

cp DEBIAN/control temp-directory/DEBIAN/control

cp temp-directory/lol-for-linux-installer-v.$PKG_VER/src/lolforlinuxinstaller.py temp-directory/usr/bin/lolforlinuxinstaller
cp temp-directory/lol-for-linux-installer-v.$PKG_VER/src/launch-script.py temp-directory/usr/share/lol-for-linux-installer/launch-script.py
cp temp-directory/lol-for-linux-installer-v.$PKG_VER/src/vulkan_layers.py temp-directory/usr/share/lol-for-linux-installer/vulkan_layers.py
cp temp-directory/lol-for-linux-installer-v.$PKG_VER/src/env_vars.json temp-directory/usr/share/lol-for-linux-installer/env_vars.json
cp temp-directory/lol-for-linux-installer-v.$PKG_VER/src/lolforlinuxinstaller.svg temp-directory/usr/share/lol-for-linux-installer/lolforlinuxinstaller.svg
cp temp-directory/lol-for-linux-installer-v.$PKG_VER/src/leagueinstaller_code.py temp-directory/usr/share/lol-for-linux-installer/leagueinstaller_code.py
cp temp-directory/lol-for-linux-installer-v.$PKG_VER/src/lolforlinuxinstaller.desktop temp-directory/usr/share/applications/lolforlinuxinstaller.desktop
cp temp-directory/lol-for-linux-installer-v.$PKG_VER/src/installer.ui temp-directory/usr/share/lol-for-linux-installer/installer.ui

dpkg-deb --build temp-directory

rm -rf temp-directory/lol-for-linux-installer-v.$PKG_VER
mv temp-directory.deb ../$PKG_NAME\_$PKG_VER-$PKG_REL\_amd64.deb
rm -rf temp-directory

