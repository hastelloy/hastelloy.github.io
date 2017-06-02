---
layout: post
title: Shadowsocks in EC2
categories: [VPN, EC2]
tags: [AWS, Python, VPN, EC2]
fullview: false
comments: true
description: Setup Shadowsocks in AWS EC2..
---


[Git source](https://github.com/ziggear/shadowsocks)

/etc/shadowsocks.json
```
{
    "server":"ec2_private_ip",
    "server_port":8388,
    "local_address": "127.0.0.1",
    "local_port":1080,
    "password":"mypassword",
    "timeout":300,
    "method":"aes-256-cfb",
    "fast_open": false
}
```

To run in the foreground:
    ```ssserver -c /etc/shadowsocks.json```
To run in the background:
    ```ssserver -c /etc/shadowsocks.json -d start```
    ```ssserver -c /etc/shadowsocks.json -d stop```