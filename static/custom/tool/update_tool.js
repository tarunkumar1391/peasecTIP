$(function() {

    $("#success-alert1").hide();
    $("#error-alert1").hide();
     $("#success-alert2").hide();
    $("#error-alert2").hide();



// indicator - labels dropdown
$('#tool_label').change(function(){
    var values = $(this).val();
    $('#tool_label_final').val(values);
});


    /* Update tool required info*/
    $('#update_tool').click(function() {
        $.ajax({
            url: '/update_tool',
            data: $('#update_toolform').serialize(),
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





