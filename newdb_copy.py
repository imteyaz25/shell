#!/usr/bin/python
import os
import sys
import time
from subprocess import PIPE, Popen

def cmdline(command):
   process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
   )
   return process.communicate()[0]

# Sync the db files first
#rsync -ravz -e 'ssh -i /home/tvemulti/.ssh/imt'  --exclude='on-demand' nbcutve.prod@web-5863.prod.hosting.acquia.com:/mnt/gfs/home/nbcutve/prod/backups/ .
#rsync -ravz -e 'ssh -i /home/tvemulti/.ssh/imt' nbcutve.prod@web-5863.prod.hosting.acquia.com:/mnt/gfs/home/nbcutve/prod/backups/on-demand/backup-2016-05* .
#backup-2016-05-02-08-08-bravo-29676543.sql


'''
Pass the argument as environemnt
'''

if(len(sys.argv)==0):
  print "Hello that is empty"
  exit()

ENV = sys.argv[1]

'''Overriding value for stage'''
if(ENV=='stage'):
   ENV = 'stg'

if(ENV=='prod'):
   ENV = ''

#sites = ['bravo','cnbc','eonline', 'esquire', 'mun2', 'nbcsports', 'nbcd','nbcnews','nbcuniverso', 'syfy', 'sprout', 'oxygen','telemundo', 'usa']
sites = ['mun2']

localtime = time.localtime(time.time())
timeString = time.strftime("%Y-%m-%d", localtime)
timeString ="2016-05-02"

for site in sites:
  print "******"+site+"*******"
#  cmd1  = "ls ../backups/prod-"+site+"*"+timeString+".sql"
  cmd1  = "ls ../backups/backup-"+timeString+"*"+site+"*"+".sql"
  db_filename = cmdline(cmd1)
  print db_filename
  cmd2 = "drush @nbcutve.prod -l nbcutve-"+site+"  sql-drop -y -v"
  cmd3 = "drush @nbcutve.prod -l nbcutve-"+site+" sqlc < "+db_filename
  print cmdline(cmd2)
  print cmd3
  print cmdline(cmd3)
