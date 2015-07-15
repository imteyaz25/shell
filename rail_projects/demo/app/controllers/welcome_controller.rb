class WelcomeController < ApplicationController
  def index
  end
  def yahoo
    begin

      #require 'rubygems'
      require 'net/ssh'
      #require 'net/ssh-getway'
      #ssh nbcutveadmin.prod@web-13028.prod.hosting.acquia.com
      @HOST = "web-13028.prod.hosting.acquia.com"
      @USER = "nbcutveadmin.prod"
      @PASS = ""
      Net::SSH.start( @HOST, @USER, :password => @PASS ) do|ssh|
       @output = ssh.exec!('cd /var/www/html && ls -ltr')
       #open('log.txt', 'w') do |f|
       #  f.puts(output)
       #end
       #puts output
      end
    rescue Exception => e
      puts e.message
      puts e.backtrace.inspect
    end
  end
end
