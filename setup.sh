#!/bin/sh
sudo apt-get update
sudo apt-get -y install python3-pip git python3-matplotlib python3-numpy
sudo pip3 install -U pip
sudo pip3 install jupyter


# Create certificate files
mkdir ~/.ssh
cd ~/.ssh
openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout notebook.key -out notebook.pem
