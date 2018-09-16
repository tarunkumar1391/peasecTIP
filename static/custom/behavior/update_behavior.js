$(function() {

    $("#success-alert1").hide();
    $("#error-alert1").hide();
     $("#success-alert2").hide();
    $("#error-alert2").hide();
     $("#success-alert3").hide();
    $("#error-alert3").hide();


    /* Update Attack pattern required info*/
    $('#update_behavior').click(function() {
        $.ajax({
            url: '/update_behavior',
            data: $('#update_behaviorform').serialize(),
            type: 'POST',
            success: function(response) {

                $( "#success-alert1" ).fadeIn( 300 ).delay( 2000 ).fadeOut( 400, function () {
                     window.location.reload();
                 } );
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

    /* Submit External References data*/
    $('#add_extref').click(function() {
        $.ajax({
            url: '/insertextref',
            data: $('#ext_refform').serialize(),
            type: 'POST',
            success: function(response) {
                 $( "#success-alert2" ).fadeIn( 300 ).delay( 2000 ).fadeOut( 400, function () {
                     window.location.reload();
                 } );

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

    /* choosing attribute value from dropdown or input */
    $('#enableInput').change(function() {
         $('#attr_val2').attr('disabled',!this.checked)
         $('#attr_val2').attr('required',this.checked)

         $('#attr_val1').attr('disabled',this.checked)
        $('#attr_val1').attr('required',!this.checked)

    });

// behavior - dropdowns

    var val1,val2;
$('#attr_key').change(function(){

    var key = $(this).val();
    $('#attr_val1').change(function () {
        var val1 = $(this).val();
        var result = key + ":" + val1 ;
        $('#attr_val_final').val(result);
    });
    $('#attr_val2').change(function () {
        var val2 = $(this).val();
        var result = key + ":" + val2 ;
        $('#attr_val_final').val(result);
    });


});

$('#name').change(function () {
    var value = $(this).val();
    $('#name_final').val(value);
});

$('#technique_refs').change(function () {
    var value = $(this).val();
    $('#tech_refs_final').val(value);
});

$('#action_refs').change(function () {
    var value = $(this).val();
    $('#action_refs_final').val(value);
});

 /* Enable URL function*/
    $('#enableURL').change(function() {
         $('#extUrl').attr('disabled',!this.checked)
         $('#extUrl').attr('required',this.checked)

         $('#hashType').attr('disabled',!this.checked)
        $('#hashType').attr('required',this.checked)

         $('#hashVal').attr('disabled',!this.checked)
        $('#hashVal').attr('required',this.checked)
    });





});





