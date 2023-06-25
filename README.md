# lol-for-linux-installer-pkgbuild
PKGBUILD for lol-for-linux-installer

## Arch Linux/Manjaro and Friends with multilib enabled:
With the main PKGBUILD file in a folder on arch/manjaro and friends you just need to run "makepkg -si" and it will build and install

## Ubuntu/Pop_OS!/Mint with multiarch enabled:
Install `makedeb` and run "makedeb -si" inside the ubuntu-makedeb folder to compile and install

## Fedora 38
Run `rpmbuild -bb lol-for-linux-installer.spec`and then double click the .rpm file to install
