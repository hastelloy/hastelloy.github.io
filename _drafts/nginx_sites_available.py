server {
        listen 80;
        server_name 52.78.25.118;

       location = /favicon.ico { 
           access_log off; 
            log_not_found off; 
        }
        
        location /static/ {
            root /home/ec2-user/onedrivecloud;
        }

        location / {
            # include proxy_params;
            proxy_pass http://unix:/home/ec2-user/onedrivecloud/onedrivecloud.sock;
        }
    }