$(function() {

    // intrusion set - resource level dropdown
$('#res_level').change(function(){
    var values = $(this).val();
    $('#res_level_final').val(values);
});



// intrusion set - primary motivation dropdown
$('#prim_motiv').change(function(){
    var values = $(this).val();
    $('#prim_motiv_final').val(values);
});

// intrusion set - secondary motivation dropdown
$('#secondary_motiv').change(function(){
    var values = $(this).val();
    $('#sec_motiv_final').val(values);
});

// intrusion set - first seen
$('#first_seen').change(function(){
    var values = $(this).val();
    $('#first_seen_final').val(values);
});
// intrusion set - last seen
$('#last_seen').change(function(){
    var values = $(this).val();
    $('#last_seen_final').val(values);
});



    $("#success-alert1").hide();
    $("#error-alert1").hide();



    /* Update Intrusion set required info*/
    $('#update_intrusionset').click(function() {
        $.ajax({
            url: '/update_intrusionset',
            data: $('#update_intrusionsetform').serialize(),
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


