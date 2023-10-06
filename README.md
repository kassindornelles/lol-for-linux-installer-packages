# lol-for-linux-installer-packages

## Arch Linux/Manjaro and Friends with multilib enabled:
Run "makepkg -si" in the PKGBUILD file folder and it will create the package and install it.

## Ubuntu/Pop_OS!/Mint with multiarch enabled:
Have `dpkg` installed if on Arch Linux

Run `createdeb.sh` to create a .deb file.

## Fedora 38
Have RPM-Tools installed and then run `build.rpm.sh` and then double click the .rpm file to install.
