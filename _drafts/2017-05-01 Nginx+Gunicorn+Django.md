---
layout: post
title: Nginx + Gunicorn + Django
---

{{page.title}}
===============

[Linode Tutorial](https://www.linode.com/docs/web-servers/nginx/how-to-configure-nginx/)
[Gunicorn](http://docs.gunicorn.org/en/stable/deploy.html)
[django using Gunicorn](https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/gunicorn/)


# Setup Gunicorn
[How To Set Up Django with Postgres, Nginx, and Gunicorn on Ubuntu 14.04 ](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-14-04#configure-nginx-to-proxy-pass-to-gunicorn)

[deploy gunicorn](http://docs.gunicorn.org/en/stable/deploy.html)

gunicorn.conf with upstart, [unkown service gunicorn](https://askubuntu.com/questions/30796/upstart-script-doesnt-start)
`sudo initctl list | grep your_job_name`
use `start/stop/restart gunicorn`
`/var/log/messages`

930 
#### /etc/init/gunicorn.conf

```sh
description "Gunicorn application server handling onedrivecloud"

start on runlevel [2345]
stop on runlevel [!2345]

respawn
#setuid ec2-user
#setgid www-data

script
    chdir /home/ec2-user/work/onedrivecloud

    exec gunicorn --workers 3 --bind unix:/home/ec2-user/work/onedrivecloud/onedrivecloud.sock onedrivecloud.wsgi:application
end script
```
start gunicorn by:
`sudo service gunicorn start`

check `/var/log/messages` for the error info there.

# Setup Nginx

**nginx.conf locations**:
    * /usr/local/nginx/conf
    * /etc/nginx
    * /usr/local/etc/nginx
```
# /etc/sysconfig/nginx
NGINX_CONF_FILE=/etc/nginx/nginx.conf
```

```
# /etc/nginx/nginx.conf
user nobody nobody;
pid /var/run/nginx.pid;
error_log /var/log/nginx/error.log;

events {
    worker_connections  1024;
    #accept_mutex: on;
}

http {
    include       mime.types;
    default_type  application/octet-stream;
    access_log /tmp/nginx.access.log combined;
    sendfile        on;
    tcp_nopush      on;
    tcp_nodelay         on;
    gzip  on;
    gzip_http_version 1.0;
    gzip_proxied any;
    #gzip_min_lenght 500;
    gzip_disable "MSIE [1-6]\.";
    gzip_types text/plain text/xml text/css
         text/comma-separated-values
         text/javascript application/x-javascript
         application/atom+xml;
    include /etc/nginx/sites-enabled/*.*;
}

```


```
# etc/nginx/sites-available/onedrivecloud
upstream onedrivecloud {
    server 127.0.0.1:8000 fail_timeout=0;
}

server {
    listen 80;
    server_name 52.78.25.118;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/ec2-user/onedrivecloud;
    }

    location / {
        # include proxy_params;
        proxy_pass http://unix:/home/ec2-user/onedrivecloud/onedrivecloud.sock;
    }
}

```
in `/etc/nginx/nginx.conf`, to add `include /etc/nginx/sites-enabled/*;`
in `sites-enabled/$$project, to define the server block.

[sample config in EC2](https://serverfault.com/questions/351559/nginx-without-server-name-and-using-only-static-ip-address) 

## changes log
 - open 80 port for everywhere in EC2  -> 502 Bad Gateway,
    `/var/log/nginx/error.log`
    `connect() to unix:/home/ec2-user/onedrivecloud/onedrivecloud.sock failed (13: Permission denied) while connecting to upstream`
     -> uncomment user in nginx.conf -> error remains

