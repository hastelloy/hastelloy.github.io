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


gunicorn.conf with upstart, [unkown service gunicorn](https://askubuntu.com/questions/30796/upstart-script-doesnt-start)
`sudo initctl list | grep your_job_name`
use `start/stop/restart gunicorn`
`/var/log/messages`

```sh
  description "Gunicorn application server handling myproject"

  start on runlevel [2345]
  stop on runlevel [!2345]

  respawn
  # this will fail with  init: /etc/init/gunicorn.conf:7: Unknown stanza
  # setuid user
  # setgid www-data
  chdir /home/user/myproject

  exec myprojectenv/bin/gunicorn --workers 3 --bind unix:/home/user/myproject/myproject.sock myproject.wsgi:application
```

# Setup Nginx
in `/etc/nginx/nginx.conf`, to add `include /etc/nginx/site-enabled/*;`
in `site-enabled/$$project, to define the server block.

[sample config in EC2](https://serverfault.com/questions/351559/nginx-without-server-name-and-using-only-static-ip-address) 

