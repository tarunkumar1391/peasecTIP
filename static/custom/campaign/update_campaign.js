$(function() {

    $("#success-alert1").hide();
    $("#error-alert1").hide();



    /* Update campaign required info*/
    $('#update_campaign').click(function() {
        $.ajax({
            url: '/update_campaign',
            data: $('#update_campaignform').serialize(),
            type: 'POST',
            success: function(response) {

                $("#success-alert1").fadeTo(2000, 500).slideUp(500, function(){
               $("#success-alert1").slideUp(500);
                });
                console.log(response);
            },
            error: function(error) {
                $("#error-alert1").fadeTo(2000, 500).slideUp(500, function(){
               $("#error-alert1").slideUp(500);
                });
                console.log(error);
            }
        });

    });









});


