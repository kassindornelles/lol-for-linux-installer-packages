#!/bin/bash
version=$(grep -oP '(?<=Version:\s{8})\S+' lol-for-linux-installer.spec)
url="https://github.com/kassindornelles/lol-for-linux-installer/archive/refs/tags/v.${version}.tar.gz"
curl -L -o "v.${version}.tar.gz" "$url"
mkdir -p SOURCES
mv "v.${version}.tar.gz" "SOURCES/"
rpmbuild -ba lol-for-linux-installer.spec
shopt -s extglob
rm -rf !(RPMS|lol-for-linux-installer.spec|build_rpm.sh)
cd RPMS
if [ -d "x86_64" ]; then
  mv x86_64/* ../
fi
cd ..
rm -rf RPMS

