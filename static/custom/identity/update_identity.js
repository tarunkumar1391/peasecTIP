$(function() {

    $("#success-alert1").hide();
    $("#error-alert1").hide();

/* Updating identity class and sectors*/
    $('#id_class').change(function(){
    var values = $(this).val();
    $('#id_class_final').val(values);
});

    $('#sectors').change(function(){
    var values = $(this).val();
    $('#sectors_final').val(values);
});


    /* Update Identity required info*/
    $('#update_identity').click(function() {
        $.ajax({
            url: '/update_identity',
            data: $('#update_identityform').serialize(),
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


