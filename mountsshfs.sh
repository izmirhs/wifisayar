#!/bin/bash
rm /mnt/mekansshfs/*
sshfs -o 'IdentityFile=~/.ssh/id_rsa' -o nonempty xxx@xxxx:/srv/izmirhs.org/mekan /mnt/mekansshfs/
/usr/bin/python /home/pi/mekanapp/mekan1.py
