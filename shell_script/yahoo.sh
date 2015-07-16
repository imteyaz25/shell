#!/bin/sh

file="purge_urls.txt";
host="http://mvpd-admin.nbcuni.com";
time=$(date +%F);
bal1="bal-6951";
bal2="bal-6952";

while read LINE
do
  string=${LINE#$host};
  #echo 'curl -X PURGE -H "X-Acquia-Purge:nbcutveadmin" --compress -H "Host: mvpd-admin.nbcuni.com" http://$1.prod.hosting.acquia.com$string'
  command='curl -X PURGE -H "X-Acquia-Purge:nbcutveadmin" --compress -H "Host: mvpd-admin.nbcuni.com" http://'$bal1'.prod.hosting.acquia.com'$string;
  $command >> purge_output_$time.txt;
  command='curl -X PURGE -H "X-Acquia-Purge:nbcutveadmin" --compress -H "Host: mvpd-admin.nbcuni.com" http://'$bal2'.prod.hosting.acquia.com'$string;
  $command >> purge_output_$time.txt;
done < $file
