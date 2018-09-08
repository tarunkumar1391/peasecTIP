$(function() {

    $("#success-alert1").hide();
    $("#error-alert1").hide();


    /* Update Relationship required info*/
    $('#update_relationship').click(function() {
        $.ajax({
            url: '/update_relationship',
            data: $('#update_relationshipform').serialize(),
            type: 'POST',
            success: function(response) {

                $( "#success-alert1" ).fadeIn( 300 ).delay( 2000 ).fadeOut( 400, function () {
                     window.location.reload();
                 } );
                console.log(response);
            },
            error: function(error) {
                $( "#error-alert1" ).fadeIn( 300 ).delay( 2000 ).fadeOut( 400, function () {
                     window.location.reload();
                 } );
                console.log(error);
            }
        });

    });








});





