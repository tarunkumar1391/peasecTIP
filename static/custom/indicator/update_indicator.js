$(function() {

    $("#success-alert1").hide();
    $("#error-alert1").hide();
     $("#success-alert2").hide();
    $("#error-alert2").hide();

// indicator - timestamps
$('#new_validfrom').change(function(){
    var values = $(this).val();
    $('#new_validfrom_final').val(values);
});
// indicator - timestamps
$('#new_validuntill').change(function(){
    var values = $(this).val();
    $('#new_validuntill_final').val(values);
});

// indicator - labels dropdown
$('#select_label').change(function(){
    var values = $(this).val();
    $('#label_final').val(values);
});


    /* Update indicator required info*/
    $('#update_indicator').click(function() {
        $.ajax({
            url: '/update_indicator',
            data: $('#update_indicatorform').serialize(),
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

    /* Submit kill chain data*/
    $('#submit_kcph').click(function() {
        $.ajax({
            url: '/killchain',
            data: $('#killchain').serialize(),
            type: 'POST',
            success: function(response) {
                 $("#success-alert2").fadeTo(2000, 500).slideUp(500, function(){
               $("#success-alert2").slideUp(500);
                });
                console.log(response);
            },
            error: function(error) {
                $("#error-alert2").fadeTo(2000, 500).slideUp(500, function(){
               $("#error-alert2").slideUp(500);
                });
                console.log(error);
            }
        });

    });





});





