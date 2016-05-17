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



sites = ['bravo', 'cnbc', 'eonline', 'esquire', 'mun2', 'nbcsports', 'nbcd','nbcnews','nbcuniverso', 'syfy', 'sprout', 'oxygen','telemundo', 'usa']

for site in sites:
  print "******"+site+"*******"
  cmd = "rsync -ravz -e "+"'"+"ssh -i /home/tvemulti/.ssh/imt"+"'"+"  nbcutve.prod@web-5863.prod.hosting.acquia.com:/mnt/gfs/nbcutve/sites/nbcutve-"+site+"/files/ /mnt/gfs/files/tve"+site+"/sites/files/"
  print cmd
  os.system(cmd)
