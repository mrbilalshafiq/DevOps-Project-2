#!/bin/bash

# install ansible, python 3 & pip
sudo apt update && sudo apt upgrade -y
sudo apt install -y ansible python3 python3-pip awscli
# install awscli and boto3 dependencies
pip3 install --user --upgrade boto3 awscli
echo 'PATH=$PATH:~/.local/bin' >> ~/.bashrc
source ~/.bashrc
