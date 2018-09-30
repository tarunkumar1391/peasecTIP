$(function() {

    $("#success-alert1").hide();
    $("#error-alert1").hide();
     $("#success-alert2").hide();
    $("#error-alert2").hide();
     $("#success-alert3").hide();
    $("#error-alert3").hide();


    /* Update Attack pattern required info*/
    $('#update_attkpat').click(function() {
        $.ajax({
            url: '/update_attk_pattern',
            data: $('#update_attkpatternform').serialize(),
            type: 'POST',
            success: function(response) {

                $( "#success-alert1" ).fadeIn( 300 ).delay( 2000 ).fadeOut( 600, function () {

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

    /* Submit kill chain data*/
    $('#submit_kcph').click(function() {
        $.ajax({
            url: '/killchain',
            data: $('#killchain').serialize(),
            type: 'POST',
            success: function(response) {
                 $( "#success-alert2" ).fadeIn( 300 ).delay( 2000 ).fadeOut( 600, function () {

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

    /* Submit External References data*/
    $('#add_extref').click(function() {
        $.ajax({
            url: '/insertextref',
            data: $('#ext_refform').serialize(),
            type: 'POST',
            success: function(response) {
                 $( "#success-alert3" ).fadeIn( 300 ).delay( 2000 ).fadeOut( 600, function () {

                 } );
                console.log(response);
            },
            error: function(error) {
                $("#error-alert3").fadeTo(2000, 500).slideUp(500, function(){
               $("#error-alert3").slideUp(500);
                });
                console.log(error);
            }
        });

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


/* Updating url*/
    $('#extUrl').change(function(){
    var values = $(this).val();
    $('#extref_url_final').val(values);
});
/* Updating hash type*/
    $('#hashType').change(function(){
    var values = $(this).val();
    $('#hash_type_final').val(values);
});
/* Updating hash val*/
    $('#hashVal').change(function(){
    var values = $(this).val();
    $('#hash_value_final').val(values);
});

});





