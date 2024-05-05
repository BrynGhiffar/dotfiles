#!/bin/bash

# A script used to toggle internet connection on and off.
state=$(sudo iptables -S | grep 'INPUT -j DROP')
if [ -z "$state" ]
then
	sudo iptables -A INPUT -s 192.168.1.0/24 -j ACCEPT
	sudo iptables -A INPUT -i lo -j ACCEPT
	sudo iptables -A INPUT -j DROP
	sudo iptables -A OUTPUT -d 192.168.1.0/24 -j ACCEPT
	sudo iptables -A OUTPUT -o lo -j ACCEPT
	sudo iptables -A OUTPUT -j DROP	
  echo "Internet Disabled"
else
	sudo iptables -D INPUT -j DROP
	sudo iptables -D OUTPUT -j DROP
  echo "Internet Enabled"
fi
