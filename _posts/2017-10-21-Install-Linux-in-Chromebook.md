---
layout: post
title: Install Linux in Chromebook Asus C300M
categories: [Chromebook]
tags: [Chromebook, Asus, Ubuntu, Fedora, GalliumOS]
fullview: false
comments: true
description: Install Linux in Chromebook Asus C300M
---


##System Recover

When you see this error message: __"Chrome OS is missing or damaged"__

Use [Chromebook Recovery Utility](https://chrome.google.com/webstore/detail/chromebook-recovery-utili/jndclpdbaamdhonoechobihbbiimdgai?hl=en) to create a recovery USB flash driver

___Note___: 

* VPN might be needed to access the Chrome extension to start the utility
* VPN could be disconnected during download of the recovery files
* __Important__: Try another USB flash driver if it cannot be recognized as a ChromeOS recovery media. 


##Flash custom firmware

Flash the firmware with the shell script from [John Lewis](http://johnlewis.ie)

___Note___:

* No need to activate your Google account in ChromeOS, simply use guest user.
* `Ctrl+Shift+T` to open Crosh and shell to run the shell script  

___Important___: to enable Legacy and USB boot, 
```
sudo crossystem dev_boot_usb=1
sudo crossystem dev_boot_legacy=1
```

Ctrl + D - Develop mode
Ctrl + L - Legacy mode
Ctrl + U - Boot with USB

##Install Linux System

####Create Linux live usb disk:

* [etcher](https://etcher.io/)
* [linux live usb](http://www.linuxliveusb.com/en/download)

####OS
* [GalliumOS](https://galliumos.org/)
* [Fedora](https://getfedora.org/)
* [Ubuntu](https://www.ubuntu.com/)

___Add something for GalliumOS___
GalliumOS 2.1, ubuntu 16.4
```
uname -a

Linux GOS 4.8.17-galliumos #1 SMP PREEMPT galliumos4 
Thu Feb 23 02:27:28 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
```

* Install pinyin
```
sudo apt-get install fcitx
sudo apt-get install sougoupinyin
```

* Install Chinese font
```
sudo apt-get install fonts-wqy-zenhei
```

* L2TP/IPSec client
```
sudo apt-get install xl2tpd network-manager-l2tp network-manager-l2tp-gnome
```
install `strongswan` and `network-manager-strongswan` will add L2TP configuration, but something wrong with pre-shared key (seems PSK cann't be set)