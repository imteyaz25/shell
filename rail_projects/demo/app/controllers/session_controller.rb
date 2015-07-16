class SessionController < ApplicationController
  def login
  end

  def auth
  	user = User.authenticate(params[:username], params[:password])
  	if user
  		session[:user_name] = user
  		redirect_to root_path, :notice => "Logged in!"
  	else
  		redirect_to action: 'login', :notice => "Login failed!"
  	end

  end

  def logout
  	session[:user_name] = nil
    redirect_to root_path, :notice => "Logged out!"
  end

end