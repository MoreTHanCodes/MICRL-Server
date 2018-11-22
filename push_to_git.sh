#!/bin/sh

DATE=`/bin/date`
cd /home/micrl/MICRL_Homepage/MICRL-Server
echo '## Welcom to the Secret Homepage of MICRL!' > ./README.md
echo ${DATE} >> ./README.md
git add -A
git commit -a --allow-empty-message -m ''
git push -u origin master
