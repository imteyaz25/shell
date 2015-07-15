#!/usr/bin/env ruby
require 'rubygems'
require 'net/ssh'
#ssh nbcutveadmin.prod@web-13028.prod.hosting.acquia.com
HOST = 'web-13028.prod.hosting.acquia.com'
USER = 'nbcutveadmin.prod'
PASS = ''

Net::SSH.start( HOST, USER, :password => PASS ) do|ssh|
  output = ssh.exec!('cd /var/www/html && ls')
  puts output
end
