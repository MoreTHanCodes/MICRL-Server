#!/bin/sh

# NEW_IP = '/sbin/ifconfig -a | grep inet | grep -v 127.0.0.1 | grep -v inet6 | grep 175.159 | awk '{print $2}' | tr -d "addr:"'
NEW_IP = '/sbin/ifconfig -a | grep inet | grep -v 127.0.0.1 | grep -v inet6 | grep 175.159'
cd /home/micrl/MICRL_Homepage/MICRL-Server
echo '## Welcom to the Secret Homepage of MICRL!' > ./README.md
echo ${NEW_IP} >> ./README.md
git add -A
git commit -a --allow-empty-message -m ''
git push -u origin master
