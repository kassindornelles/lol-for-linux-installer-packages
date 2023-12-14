# lol-for-linux-installer-packages

## Building on Arch Linux for Arch, Ubuntu LTS and Fedora at once
- You need a Arch Linux install or virtual machine
- Install `rpm-tools` and `dpkg` from Arch repos
- run `automated-build.sh` in a terminal and it will generate the packages for all 3 distros

The packages will be in the "Packages" folder in the same directory as the .sh script


### Arch Linux/Manjaro and Friends with multilib enabled:
Run `makepkg -si` in the `PKGBUILD` file folder and it will create the package and install it.

### Ubuntu/Pop_OS!/Mint with multiarch enabled:
Have `dpkg` installed if on Arch Linux

Run `createdeb.sh` to create a .deb file, double click the .deb file to install.

### Fedora
Have `rpm-tools` installed if on Arch Linux

Run `build.rpm.sh` and then double click the .rpm file to install.
