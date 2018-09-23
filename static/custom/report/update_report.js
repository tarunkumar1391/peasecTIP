$(function() {


      $("#success-alert1").hide();
    $("#error-alert1").hide();
     $("#success-alert2").hide();
    $("#error-alert2").hide();

 /* Update malware required info*/
    $('#update_report').click(function() {
        $.ajax({
            url: '/update_report',
            data: $('#update_reportform').serialize(),
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

// report - dropdowns
$('#reportlabels').change(function(){
    var values = $(this).val();
    $('#final_label').val(values);
});
// report - dropdowns
$('#published').change(function(){
    var values = $(this).val();
    $('#new_published_final').val(values);
});


});