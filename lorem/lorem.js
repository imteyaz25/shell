(function ($) {
  Drupal.behaviors.lorem = {
    attach: function (context, settings) {
      // Your Javascript code goes here

      $('#edit-button', context).click(function () {
        i=0;
        j=0;
        output="";
        text = $('#edit-lorem-text').val();
        rows = $('#edit-rows').val();
        cols = $('#edit-column').val();
        for(i=0;i<rows;i++){
  	      for(j=0;j<cols;j++)
  		    output +=text+" ";
  	      output +="<br/>";
        }

        $('#edit-message').html(output);
        return false;
      });
 
    }
  };
}(jQuery));