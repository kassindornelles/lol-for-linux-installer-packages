#!/bin/bash

mkdir -p packages

echo "BUILDING FOR ARCH LINUX"
cd archlinux
makepkg
echo "BUILDING FOR FEDORA"
cd ../fedora-rpm
./build_rpm.sh
echo "BUILDING FOR UBUNTU LTS"
cd ../ubuntu-LTS
./createdeb.sh
echo "BUILDING FOR UBUNTU 23.10"
cd ../ubuntu-23-10
./createdeb.sh

cd ..
echo "MOVING FILES TO PACKAGES FOLDER"
mv archlinux/*.pkg.tar.zst packages/
mv *.deb packages/
mv fedora-rpm/*.rpm packages/

echo "done"


