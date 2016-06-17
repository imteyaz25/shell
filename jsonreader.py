#!/usr/bin/python
import os
import sys
import json
import urllib2


sites = {
'tveott':{'dev':'dev','stage':'dev','uat':'dev','prod':'prod'},
'mvpdadmin':{'dev':'dev','stage':'dev','prod':'prod'},
'nbc':{'dev':'dev', 'editdev':'editdev', 'stage':'stage', 'editstage':'editstage','acc':'acc','editacc':'editacc','prod':'prod','edit':'edit'},
'tsjf':{'dev':'dev', 'editdev':'editdev', 'stage':'stage', 'editstage':'editstage','acc':'acc','editacc':'editacc','prod':'prod','edit':'edit'}
}

fo = open("custom_aliases", "w+")

for site in sites:
  for env in sites[site]:
    servers = []
    try:
      url = "https://dashboardapi.nbcuext.com/v3/search/deploy/"+site+sites[site][env]+"@"
      response = urllib2.urlopen(url)
      data = json.loads(response.read())
      for boxes in data :
        #print data[boxes]['dns']
        servers.append(data[boxes]['dns'])
      i=1
      skip = False
      if(len(servers)>1):
        skip = True

      for server in servers:
        #alias drush='DRUSH_PHP=/usr/bin/php /usr/local/share/Drush/drush.php'
        cmd = "alias "+site+"."+env+"="+"'"+"ssh "+site+"."+env+"@"+server+"'"
        if(skip):
          cmd = "alias "+site+"."+env+str(i)+"="+"'"+"ssh "+site+"."+env+"@"+server+"'"
          i =  i + 1
        print cmd
        fo.write(cmd)
        fo.write('\n')
    except OSError as err:
      print("OS error: {0}".format(err))

fo.close()
os.system('source ~/.bash_profile')
