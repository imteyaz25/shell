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

if(ENV=='prod'):
   ENV = ''



sites = ['bravo','cnbc','eonline', 'esquire', 'mun2', 'nbcsports', 'nbcd','nbcnews','nbcuniverso', 'syfy', 'sprout', 'oxygen','telemundo', 'usa']

for site in sites:
  print "******"+site+"*******"
  docroot = '/var/www/html/tvemulti'+ENV+'/docroot'
  url = "http://tve"+site+ENV+'.apps.nbcuni.com'
  drush = "drush --root="+docroot+"  --uri="+url
  print drush
  os.system("cd ~")
  cmd1 = drush +" cc all"
  cmd2 = drush +" fra -y"
  cmd3 = drush +" rr"
  cmd4 = drush +" -y vset cron_safe_threshold 0"
  cmd5 = drush +" sqlq "+"'select * from apachesolr_environment'"
  cmd6 = drush +" sqlq "+"'delete from apachesolr_environment'"
  cmd7 = drush +" dis acquia_agent acquia_search acquia_spi -y"
  #cmd8 = drush +" cron"
  os.system(cmd1)
  os.system(cmd2)
  os.system(cmd3)
  os.system(cmd4)
  os.system(cmd5)
  os.system(cmd6)
  os.system(cmd7)
 # os.system(cmd8)
