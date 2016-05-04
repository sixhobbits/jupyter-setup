#!/bin/sh
sudo apt-get update
sudo apt-get -y install python3-pip git python3-matplotlib python3-numpy

# Messes with Locale settings 
export LC_ALL="en_US.UTF-8"

sudo pip3 install -U pip
pip3 install jupyter --user


# Create certificate files
mkdir ~/.ssh
cd ~/.ssh
openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout notebook.key -out notebook.pem
