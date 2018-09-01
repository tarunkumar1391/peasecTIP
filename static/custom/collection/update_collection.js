$(function() {

    $("#success-alert1").hide();
    $("#error-alert1").hide();

/* Updating identity class and sectors*/
    $('#assoc_type').change(function(){
    var values = $(this).val();
    $('#assoc_type_final').val(values);
});



    /* Update Identity required info*/
    $('#update_collection').click(function() {
        $.ajax({
            url: '/update_collection',
            data: $('#update_collectionform').serialize(),
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


