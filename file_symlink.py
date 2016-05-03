#!/usr/bin/python
import os
import sys

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

sites = ['bravo', 'cnbc', 'eonline', 'esquire', 'mun2', 'nbcsports', 'nbcd','nbcnews','nbcuniverso', 'syfy', 'sprout', 'telemundo', 'usa']

for site in sites:
  cmd1 =  "sudo ln -s /mnt/gfs/files/tve"+site+ENV+"/sites/files-private /var/www/html/tvemulti"+ENV+"/docroot/sites/nbcutve-"+site+"/files-private"
  cmd2 =  "sudo ln -s /mnt/gfs/files/tve"+site+ENV+"/sites/files /var/www/html/tvemulti"+ENV+"/docroot/sites/nbcutve-"+site+"/files"
  os.system(cmd1)
  os.system(cmd2)
