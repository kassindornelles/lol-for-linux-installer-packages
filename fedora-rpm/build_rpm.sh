#!/bin/bash

# Get the version number from the spec file
version=$(grep -oP '(?<=Version:\s{8})\S+' lol-for-linux-installer.spec)

# Download the source file from GitHub
url="https://github.com/kassindornelles/lol-for-linux-installer/archive/refs/tags/v.${version}.tar.gz"
curl -L -o "v.${version}.tar.gz" "$url"

# Create a SOURCES directory in the current directory if it doesn't exist
mkdir -p SOURCES

# Move the source file to the SOURCES directory in the current directory
mv "v.${version}.tar.gz" "SOURCES/"

# Run the RPM build command
rpmbuild -ba lol-for-linux-installer.spec

# Delete all folders in the current directory that aren't named "RPMS" and exclude the spec file and the bash script
shopt -s extglob
rm -rf !(RPMS|lol-for-linux-installer.spec|build_rpm.sh)

# Go to the RPMS folder
cd RPMS

# Check if there's an "x86_64" subfolder
if [ -d "x86_64" ]; then
  # Move all files inside the "x86_64" subfolder to the initial directory
  mv x86_64/* ../
fi

# Delete the RPMS folder
cd ..
rm -rf RPMS

