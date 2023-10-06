#!/bin/bash

cd archlinux
makepkg

cd ../fedora-rpm
./build_rpm.sh

cd ../ubuntu-LTS
./createdeb.sh

cd ..

echo "done"

