#!/bin/bash

# Enable ssh password authentication
sed -i 's/^PasswordAuthentication .*/PasswordAuthentication yes/' /etc/ssh/sshd_config
sed -i 's/^PermitRootLogin .*/PermitRootLogin yes/' /etc/ssh/sshd_config
systemctl reload sshd

# Config NameServers
echo "\ndns-nameservers 8.8.8.8 8.8.4.4" >> /etc/network/interface

# Install Consul
curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add
sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
sudo apt-get update && sudo apt-get install consul

# Run Consul agent
mkdir -p /etc/console/data
consul agent -client 172.16.16.20 -bind 172.16.16.20 -data-dir /etc/console/data > /dev/null &

# Set Root password
echo "[TASK 2] Set root password"
echo -e "admin\nadmin" | passwd root >/dev/null 2>&1


