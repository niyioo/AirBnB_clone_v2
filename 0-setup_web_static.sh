#!/usr/bin/env bash
# This script sets up web servers for the deployment of web_static

sudo apt-get update
apt-get -y install nginx
sudo mkdir -p /data/web_static/{releases/test,shared}
sudo chown -R ubuntu:ubuntu /data/
echo "This is a test." | tee /data/web_static/releases/test/index.html
sudo ln -s /data/web_static/releases/test /data/web_static/current
config_file="/etc/nginx/sites-available/default"
sed -i "/server_name _;/ a \\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}" "$config_file"
sudo service nginx restart
