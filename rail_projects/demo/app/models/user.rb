class User < ActiveRecord::Base

	def self.authenticate(user_name, password)
      user = find(:first, :conditions => [ "username = ? AND password = ?", user_name, password ])
    end
end
