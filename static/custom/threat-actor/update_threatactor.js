$(function() {

      $("#success-alert1").hide();
    $("#error-alert1").hide();
     $("#success-alert2").hide();
    $("#error-alert2").hide();


     // threat-actor - dropdowns
$('#ta_labels').change(function(){
    var values = $(this).val();
    $('#ta_label_final').val(values);
});
// threat-actor - dropdowns
$('#ta_roles').change(function(){
    var values = $(this).val();
    $('#ta_role_final').val(values);
});



// threat-actor - dropdowns
$('#sophistication').change(function(){
    var values = $(this).val();
    $('#ta_sophistication_final').val(values);
});
// threat-actor - dropdowns
$('#res_level').change(function(){
    var values = $(this).val();
    $('#ta_res_level_final').val(values);
});
// threat-actor - dropdowns
$('#prim_motiv').change(function(){
    var values = $(this).val();
    $('#ta_prim_motiv_final').val(values);
});

// threat-actor - dropdowns
$('#per_motiv').change(function(){
    var values = $(this).val();
    $('#ta_per_motiv_final').val(values);
});

 /* Update malware required info*/
    $('#update_threatactor').click(function() {
        $.ajax({
            url: '/update_threatactor',
            data: $('#update_threatactorform').serialize(),
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



// threat-actor - dropdowns
$('#sec_motiv').change(function(){
    var values = $(this).val();
    $('#ta_sec_motiv_final').val(values);
});
// threat-actor - dropdowns
$('#per_motiv').change(function(){
    var values = $(this).val();
    $('#ta_per_motiv_final').val(values);
});



});