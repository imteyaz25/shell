class PersonsController < ApplicationController
	def index
		@persons = Person.all
	end
	def show
		@person = Person.find(params[:id])
	end
	def new
	end
	def create
		@person = Person.new(person_params)
		if @person.save
			redirect_to :action => 'index'
		else
			render :action => 'new'
		end
	end
	def edit
        @person = Person.find(params[:id])
	end

	def update
		@person = Person.find(params[:id])
		if @person.update(person_params)
			redirect_to :action => 'index'
		else
			render 'edit'
		end
	end

	def destroy
		@person = Person.find(params[:id])
		@person.destroy

        redirect_to :action => 'index'

	end

	private
	def person_params
      params.require(:person).permit(:name, :age)
	end

end
