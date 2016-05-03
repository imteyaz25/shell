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
  print "******"+site+"*******"
  #print "/var/www/html/tvemult"+ENV+"/docroot/sites/nbcutve-"+site+"/"
  cmd1 = '/var/www/html/tvemulti'+ENV+'/docroot/sites/nbcutve-'+site+'/'
  cmd = cmd1
  print cmd1
  os.system("cd ~")
  os.chdir(cmd)
  os.system("drush cc all")
  os.system("drush fra -y")
  os.system("drush rr")
  os.system("drush -y vset cron_safe_threshold 0")
  os.system("cd ~")
