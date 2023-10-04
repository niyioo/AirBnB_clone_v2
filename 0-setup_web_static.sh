#!/usr/bin/env bash
# This script sets up web servers for the deployment of web_static

# Install Nginx if not already installed
if ! dpkg -l | grep -q nginx; then
    apt-get update
    apt-get -y install nginx
fi

# Create necessary directories
mkdir -p /data/web_static/{releases/test,shared}
chown -R ubuntu:ubuntu /data/

# Create a fake HTML file for testing
echo "This is a test." | tee /data/web_static/releases/test/index.html

# Create or update the symbolic link
if [ -L /data/web_static/current ]; then
    rm /data/web_static/current
fi
ln -s /data/web_static/releases/test /data/web_static/current

# Update Nginx configuration with an alias
config_file="/etc/nginx/sites-available/default"
sed -i "/server_name _;/ a \\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}" "$config_file"

# Restart Nginx to apply the configuration
sudo service nginx restart
