$(function() {

    $("#success-alert1").hide();
    $("#error-alert1").hide();
    $("#success-alert2").hide();
    $("#error-alert2").hide();
    $("#success-alert3").hide();
    $("#error-alert3").hide();

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

/* Enable entity refs or observable refs */
    $('input[name=ref_check]').change(function () {
        var result = $('input[name=ref_check]:checked').val();
   console.log(result);
   if (result == 'entity'){
       $('#disp_entrefs').addClass("show_refs").removeAttr("style");

   } else {
       $('#disp_entrefs').removeClass("show_refs").css({"display":"none"});
   }

   if(result == 'observable') {
       $('#disp_obsrefs').addClass("show_refs").removeAttr("style");
   }else {
       $('#disp_obsrefs').removeClass("show_refs").css({"display":"none"});
   }

    });

 /* Input obj references show/hide*/
    $('#input_objref_type').change(function(){
            $('.input_objects').hide();
            $('#input_' + $(this).val()).show();
        });

/* entity refs*/
    $('#ent_refs').change(function(){
    var values = $(this).val();
    $('#ent_refs_final').val(values);
});

 /* Update collection*/
    $('#entity_refs_add').click(function() {

        $.ajax({
            url: '/update_collection_entityrefs',
            data: $('#entity_refsform').serialize(),
            type: 'POST',
            success: function(response) {

                $("#success-alert2").fadeTo(2000, 500).slideUp(500, function(){
               $("#success-alert2").slideUp(500);
               window.location.reload();
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

    /* observable refs */
     /* Artifact*/
    $('#submit_input_artifact').click(function() {


        $.ajax({
            url: '/insert_artifact',
            data: $('#input_artifact').serialize(),
            type: 'POST',
            success: function(response) {

             $("#success-alert3").fadeTo(2000, 500).slideUp(500, function(){
               $("#success-alert3").slideUp(500);
               $('#input_artifact').trigger("reset");
                console.log(response);
                });



            },
            error: function(error) {
                $( "#error-alert3" ).fadeIn( 300 ).delay( 1500 ).fadeOut( 400 );
                console.log(error);
            }
        });

        /* update the observable refs flag */
       var dataArray = $('#input_artifact').serializeArray();
        var len = dataArray.length;
        dataObj = {};

        for (var i=0; i<len; i++) {
            dataObj[dataArray[i].name] = dataArray[i].value;
        }


        //submit to db : ajax post
        var sendData = JSON.stringify(dataObj, null, 2)
        $.ajax({
            url: '/update_collection_observablerefs',
            data: sendData,
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            success: function(response) {
                    window.location.reload();
                console.log(response);

            },
            error: function(error) {

                console.log(error);
            }
        });

    });
    /* Artifact - Enable URL function*/
    $('#enableURL').change(function() {
         $('#extUrl').attr('readonly',!this.checked)
         $('#extUrl').attr('required',this.checked).val('')

         $('#hashType').attr('readonly',!this.checked)
        $('#hashType').attr('required',this.checked)

         $('#hashVal').attr('readonly',!this.checked)
        $('#hashVal').attr('required',this.checked).val('')

        $('#payload').attr('readonly',this.checked).val('')
    });

    /* Autonomous system*/
    $('#submit_input_as').click(function() {
        $.ajax({
            url: '/insert_autonomoussystem',
            data: $('#input_autonomous-system').serialize(),
            type: 'POST',
            success: function(response) {

            $("#success-alert3").fadeTo(2000, 500).slideUp(500, function(){
               $("#success-alert3").slideUp(500);
               $('#input_autonomous-system').trigger("reset");
                console.log(response);
                });
            },
            error: function(error) {
                $( "#error-alert3" ).fadeIn( 300 ).delay( 1500 ).fadeOut( 400 );
                console.log(error);
            }
        });
        /* update the observable refs flag */
       var dataArray = $('#input_autonomous-system').serializeArray();
        var len = dataArray.length;
        dataObj = {};

        for (var i=0; i<len; i++) {
            dataObj[dataArray[i].name] = dataArray[i].value;
        }


        //submit to db : ajax post
        var sendData = JSON.stringify(dataObj, null, 2)
        $.ajax({
            url: '/update_collection_observablerefs',
            data: sendData,
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            success: function(response) {
                    window.location.reload();
                console.log(response);

            },
            error: function(error) {

                console.log(error);
            }
        });

    });

    /* Directory*/
    $('#submit_input_dir').click(function() {
        $.ajax({
            url: '/insert_directory',
            data: $('#input_directory').serialize(),
            type: 'POST',
            success: function(response) {

             $("#success-alert3").fadeTo(2000, 500).slideUp(500, function(){
               $("#success-alert3").slideUp(500);
               $('#input_directory').trigger("reset");
                console.log(response);
                });
            },
            error: function(error) {
                $( "#error-alert3" ).fadeIn( 300 ).delay( 1500 ).fadeOut( 400 );
                console.log(error);
            }
        });
        /* update the observable refs flag */
       var dataArray = $('#input_directory').serializeArray();
        var len = dataArray.length;
        dataObj = {};

        for (var i=0; i<len; i++) {
            dataObj[dataArray[i].name] = dataArray[i].value;
        }


        //submit to db : ajax post
        var sendData = JSON.stringify(dataObj, null, 2)
        $.ajax({
            url: '/update_collection_observablerefs',
            data: sendData,
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            success: function(response) {
                    window.location.reload();
                console.log(response);

            },
            error: function(error) {

                console.log(error);
            }
        });

    });

    /* Domain-name*/
    $('#submit_input_domainname').click(function() {
        $.ajax({
            url: '/insert_domainname',
            data: $('#input_domain-name').serialize(),
            type: 'POST',
            success: function(response) {

             $("#success-alert3").fadeTo(2000, 500).slideUp(500, function(){
               $("#success-alert3").slideUp(500);
               $('#input_domain-name').trigger("reset");
                console.log(response);
                });
            },
            error: function(error) {
                $( "#error-alert3" ).fadeIn( 300 ).delay( 1500 ).fadeOut( 400 );
                console.log(error);
            }
        });
        /* update the observable refs flag */
       var dataArray = $('#input_domain-name').serializeArray();
        var len = dataArray.length;
        dataObj = {};

        for (var i=0; i<len; i++) {
            dataObj[dataArray[i].name] = dataArray[i].value;
        }


        //submit to db : ajax post
        var sendData = JSON.stringify(dataObj, null, 2)
        $.ajax({
            url: '/update_collection_observablerefs',
            data: sendData,
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            success: function(response) {
                    window.location.reload();
                console.log(response);

            },
            error: function(error) {

                console.log(error);
            }
        });

    });

    /* Email-addr*/
    $('#submit_input_emailaddr').click(function() {
        $.ajax({
            url: '/insert_emailaddr',
            data: $('#input_email-addr').serialize(),
            type: 'POST',
            success: function(response) {

            $("#success-alert3").fadeTo(2000, 500).slideUp(500, function(){
               $("#success-alert3").slideUp(500);
               $('#input_email-addr').trigger("reset");
                console.log(response);
                });
            },
            error: function(error) {
                $( "#error-alert3" ).fadeIn( 300 ).delay( 1500 ).fadeOut( 400 );
                console.log(error);
            }
        });
        /* update the observable refs flag */
       var dataArray = $('#input_email-addr').serializeArray();
        var len = dataArray.length;
        dataObj = {};

        for (var i=0; i<len; i++) {
            dataObj[dataArray[i].name] = dataArray[i].value;
        }


        //submit to db : ajax post
        var sendData = JSON.stringify(dataObj, null, 2)
        $.ajax({
            url: '/update_collection_observablerefs',
            data: sendData,
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            success: function(response) {
                    window.location.reload();
                console.log(response);

            },
            error: function(error) {

                console.log(error);
            }
        });

    });

    /* Email-message*/
    $('#submit_emailmsg').click(function() {
        $.ajax({
            url: '/insert_emailmsg',
            data: $('#input_email-message').serialize(),
            type: 'POST',
            success: function(response) {

             $("#success-alert3").fadeTo(2000, 500).slideUp(500, function(){
               $("#success-alert3").slideUp(500);
               $('#input_email-message').trigger("reset");
                console.log(response);
                });
            },
            error: function(error) {
                $( "#error-alert3" ).fadeIn( 300 ).delay( 1500 ).fadeOut( 400 );
                console.log(error);
            }
        });
        /* update the observable refs flag */
       var dataArray = $('#input_email-message').serializeArray();
        var len = dataArray.length;
        dataObj = {};

        for (var i=0; i<len; i++) {
            dataObj[dataArray[i].name] = dataArray[i].value;
        }


        //submit to db : ajax post
        var sendData = JSON.stringify(dataObj, null, 2)
        $.ajax({
            url: '/update_collection_observablerefs',
            data: sendData,
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            success: function(response) {
                    window.location.reload();
                console.log(response);

            },
            error: function(error) {

                console.log(error);
            }
        });

    });
    $('#is_multipart_check').change(function () {
        var val = $(this).val();
        if (val == 'true'){
            $('#emmsg_body').attr('disabled','true')
            $('#emmsg_bodyfinal').val('None')
        } else {
            $('#emmsg_bodyfinal').val('')
            $('#emmsg_body').removeAttr('disabled')

        }
    });
    $('#emmsg_body').keyup(function () {
        var val = $(this).val();
        $('#emmsg_bodyfinal').val(val);


    });
    $('#to_refs').change(function () {
        var value = $(this).val();
        $('#to_refs_final').val(value);
    });
    $('#cc_refs').change(function () {
        var value = $(this).val();
        $('#cc_refs_final').val(value);
    });
    $('#bcc_refs').change(function () {
        var value = $(this).val();
        $('#bcc_refs_final').val(value);
    });

    /* file */
    $('#submit_file').click(function() {
        $.ajax({
            url: '/insert_file',
            data: $('#input_file').serialize(),
            type: 'POST',
            success: function(response) {

             $("#success-alert3").fadeTo(2000, 500).slideUp(500, function(){
               $("#success-alert3").slideUp(500);
               $('#input_file').trigger("reset");
                console.log(response);
                });
            },
            error: function(error) {
                $( "#error-alert3" ).fadeIn( 300 ).delay( 1500 ).fadeOut( 400 );
                console.log(error);
            }
        });
        /* update the observable refs flag */
       var dataArray = $('#input_file').serializeArray();
        var len = dataArray.length;
        dataObj = {};

        for (var i=0; i<len; i++) {
            dataObj[dataArray[i].name] = dataArray[i].value;
        }


        //submit to db : ajax post
        var sendData = JSON.stringify(dataObj, null, 2)
        $.ajax({
            url: '/update_collection_observablerefs',
            data: sendData,
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            success: function(response) {
                    window.location.reload();
                console.log(response);

            },
            error: function(error) {

                console.log(error);
            }
        });

    });
    $('#ext_key').change(function(){

    var key = $(this).val();
    $('#ext_val').keyup(function () {
        var val1 = $(this).val();
        var result = key +":" + val1;
        $('#ext_final_val').val(result);
    });
});
    $('#hash_type').change(function(){

    var key = $(this).val();
    $('#hash_val').keyup(function () {
        var val1 = $(this).val();
        var result = key +":" + val1;
        $('#hashes_final').val(result);
    });
});
    $('#con_ref').change(function () {
        var value = $(this).val();
        $('#con_ref_final').val(value);
    });
    $('#is_enc').change(function () {
        var val = $(this).val();
        if (val == 'false'){
            $('#enc_algo').attr('disabled','true')
            $('#enc_algo_final').val('None')
        } else {
            $('#enc_algo_final').val('')
            $('#enc_algo').removeAttr('disabled')

        }
    });
    $('#enc_algo').change(function () {
        var value = $(this).val();
        $('#enc_algo_final').val(value);
    });

    /* ipv4 */
    $('#submit_ipv4').click(function() {
        $.ajax({
            url: '/insert_ipv4',
            data: $('#input_ipv4-addr').serialize(),
            type: 'POST',
            success: function(response) {

             $("#success-alert3").fadeTo(2000, 500).slideUp(500, function(){
               $("#success-alert3").slideUp(500);
               $('#input_ipv4-addr').trigger("reset");
                console.log(response);
                });
            },
            error: function(error) {
                $( "#error-alert3" ).fadeIn( 300 ).delay( 1500 ).fadeOut( 400 );
                console.log(error);
            }
        });
        /* update the observable refs flag */
       var dataArray = $('#input_ipv4-addr').serializeArray();
        var len = dataArray.length;
        dataObj = {};

        for (var i=0; i<len; i++) {
            dataObj[dataArray[i].name] = dataArray[i].value;
        }


        //submit to db : ajax post
        var sendData = JSON.stringify(dataObj, null, 2)
        $.ajax({
            url: '/update_collection_observablerefs',
            data: sendData,
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            success: function(response) {
                    window.location.reload();
                console.log(response);

            },
            error: function(error) {

                console.log(error);
            }
        });

    });
    $('#res_to_refs').change(function () {
        var value = $(this).val();
        $('#res_to_refs_final').val(value);
    });
    $('#belongs_to_refs').change(function () {
        var value = $(this).val();
        $('#belongs_to_refs_final').val(value);
    });

    /* ipv6 */
    $('#submit_ipv6').click(function() {
        $.ajax({
            url: '/insert_ipv6',
            data: $('#input_ipv6-addr').serialize(),
            type: 'POST',
            success: function(response) {

            $("#success-alert3").fadeTo(2000, 500).slideUp(500, function(){
               $("#success-alert3").slideUp(500);
               $('#nput_ipv6-addr').trigger("reset");
                console.log(response);
                });
            },
            error: function(error) {
                $( "#error-alert3" ).fadeIn( 300 ).delay( 1500 ).fadeOut( 400 );
                console.log(error);
            }
        });
        /* update the observable refs flag */
       var dataArray = $('#input_ipv6-addr').serializeArray();
        var len = dataArray.length;
        dataObj = {};

        for (var i=0; i<len; i++) {
            dataObj[dataArray[i].name] = dataArray[i].value;
        }


        //submit to db : ajax post
        var sendData = JSON.stringify(dataObj, null, 2)
        $.ajax({
            url: '/update_collection_observablerefs',
            data: sendData,
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            success: function(response) {
                    window.location.reload();
                console.log(response);

            },
            error: function(error) {

                console.log(error);
            }
        });

    });
    $('#res_to_refs_v6').change(function () {
        var value = $(this).val();
        $('#res_to_refs_v6_final').val(value);
    });
    $('#belongs_to_refs_v6').change(function () {
        var value = $(this).val();
        $('#belongs_to_refs_v6_final').val(value);
    });

    /* mac */
    $('#submit_mac').click(function() {
        $.ajax({
            url: '/insert_mac',
            data: $('#input_mac-addr').serialize(),
            type: 'POST',
            success: function(response) {

            $("#success-alert3").fadeTo(2000, 500).slideUp(500, function(){
               $("#success-alert3").slideUp(500);
               $('#input_mac-addr').trigger("reset");
                console.log(response);
                });
            },
            error: function(error) {
                $( "#error-alert3" ).fadeIn( 300 ).delay( 1500 ).fadeOut( 400 );
                console.log(error);
            }
        });
        /* update the observable refs flag */
       var dataArray = $('#input_mac-addr').serializeArray();
        var len = dataArray.length;
        dataObj = {};

        for (var i=0; i<len; i++) {
            dataObj[dataArray[i].name] = dataArray[i].value;
        }


        //submit to db : ajax post
        var sendData = JSON.stringify(dataObj, null, 2)
        $.ajax({
            url: '/update_collection_observablerefs',
            data: sendData,
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            success: function(response) {
                    window.location.reload();
                console.log(response);

            },
            error: function(error) {

                console.log(error);
            }
        });

    });

    /* network-traffic */
    $('#nt_ext_key').change(function(){
        var key = $(this).val();
        $('#nt_ext_value').keyup(function () {
            var val1 = $(this).val();
            var result = key +":" + val1;
            $('#ext_dict_final').val(result);
        });
    });
    $('#src_ref').change(function () {
        var value = $(this).val();
        $('#src_ref_final').val(value);
    });
    $('#dst_ref').change(function () {
        var value = $(this).val();
        $('#dst_ref_final').val(value);
    });
    $('#src_payload_ref').change(function () {
        var value = $(this).val();
        $('#src_payload_ref_final').val(value);
    });
    $('#encapsulates_ref').change(function () {
        var value = $(this).val();
        $('#encapsulates_ref_final').val(value);
    });
    $('#encapsulatedby_ref').change(function () {
        var value = $(this).val();
        $('#encapsulatedby_ref_final').val(value);
    });
    $('#submit_nettraffic').click(function() {
        $.ajax({
            url: '/insert_networktraffic',
            data: $('#input_network-traffic').serialize(),
            type: 'POST',
            success: function(response) {

             $("#success-alert3").fadeTo(2000, 500).slideUp(500, function(){
               $("#success-alert3").slideUp(500);
               $('#input_network-traffic').trigger("reset");
                console.log(response);
                });
            },
            error: function(error) {
                $( "#error-alert3" ).fadeIn( 300 ).delay( 1500 ).fadeOut( 400 );
                console.log(error);
            }
        });
        /* update the observable refs flag */
       var dataArray = $('#input_network-traffic').serializeArray();
        var len = dataArray.length;
        dataObj = {};

        for (var i=0; i<len; i++) {
            dataObj[dataArray[i].name] = dataArray[i].value;
        }


        //submit to db : ajax post
        var sendData = JSON.stringify(dataObj, null, 2)
        $.ajax({
            url: '/update_collection_observablerefs',
            data: sendData,
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            success: function(response) {
                    window.location.reload();
                console.log(response);

            },
            error: function(error) {

                console.log(error);
            }
        });

    });

    /* process */
    $('#proc_ext_key').change(function(){
        var key = $(this).val();
        $('#proc_ext_value').keyup(function () {
            var val1 = $(this).val();
            var result = key +":" + val1;
            $('#ext_dict').val(result);
        });
    });
    $('#opened_conn_refs').change(function () {
        var value = $(this).val();
        $('#opened_conn_refs_final').val(value);
    });
    $('#child_refs').change(function () {
        var value = $(this).val();
        $('#child_refs_final').val(value);
    });
    $('#submit_process').click(function() {
        $.ajax({
            url: '/insert_process',
            data: $('#input_process').serialize(),
            type: 'POST',
            success: function(response) {

             $("#success-alert3").fadeTo(2000, 500).slideUp(500, function(){
               $("#success-alert3").slideUp(500);
               $('#input_process').trigger("reset");
                console.log(response);
                });
            },
            error: function(error) {
                $( "#error-alert3" ).fadeIn( 300 ).delay( 1500 ).fadeOut( 400 );
                console.log(error);
            }
        });
        /* update the observable refs flag */
       var dataArray = $('#input_process').serializeArray();
        var len = dataArray.length;
        dataObj = {};

        for (var i=0; i<len; i++) {
            dataObj[dataArray[i].name] = dataArray[i].value;
        }


        //submit to db : ajax post
        var sendData = JSON.stringify(dataObj, null, 2)
        $.ajax({
            url: '/update_collection_observablerefs',
            data: sendData,
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            success: function(response) {
                    window.location.reload();
                console.log(response);

            },
            error: function(error) {

                console.log(error);
            }
        });

    });

    /* software */
    $('#submit_software').click(function() {
        $.ajax({
            url: '/insert_software',
            data: $('#input_software').serialize(),
            type: 'POST',
            success: function(response) {

             $("#success-alert3").fadeTo(2000, 500).slideUp(500, function(){
               $("#success-alert3").slideUp(500);
               $('#input_software').trigger("reset");
                console.log(response);
                });
            },
            error: function(error) {
                $( "#error-alert3" ).fadeIn( 300 ).delay( 1500 ).fadeOut( 400 );
                console.log(error);
            }
        });
        /* update the observable refs flag */
       var dataArray = $('#input_software').serializeArray();
        var len = dataArray.length;
        dataObj = {};

        for (var i=0; i<len; i++) {
            dataObj[dataArray[i].name] = dataArray[i].value;
        }


        //submit to db : ajax post
        var sendData = JSON.stringify(dataObj, null, 2)
        $.ajax({
            url: '/update_collection_observablerefs',
            data: sendData,
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            success: function(response) {
                    window.location.reload();
                console.log(response);

            },
            error: function(error) {

                console.log(error);
            }
        });

    });

    /* url */
    $('#submit_url').click(function() {
        $.ajax({
            url: '/insert_url',
            data: $('#input_url').serialize(),
            type: 'POST',
            success: function(response) {

            $("#success-alert3").fadeTo(2000, 500).slideUp(500, function(){
               $("#success-alert3").slideUp(500);
               $('#input_url').trigger("reset");
                console.log(response);
                });
            },
            error: function(error) {
                $( "#error-alert3" ).fadeIn( 300 ).delay( 1500 ).fadeOut( 400 );
                console.log(error);
            }
        });
        /* update the observable refs flag */
       var dataArray = $('#input_url').serializeArray();
        var len = dataArray.length;
        dataObj = {};

        for (var i=0; i<len; i++) {
            dataObj[dataArray[i].name] = dataArray[i].value;
        }


        //submit to db : ajax post
        var sendData = JSON.stringify(dataObj, null, 2)
        $.ajax({
            url: '/update_collection_observablerefs',
            data: sendData,
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            success: function(response) {
                    window.location.reload();
                console.log(response);

            },
            error: function(error) {

                console.log(error);
            }
        });

    });

    /* user-account */
    $('#submit_useracc').click(function() {
        $.ajax({
            url: '/insert_useracc',
            data: $('#input_user-account').serialize(),
            type: 'POST',
            success: function(response) {

             $("#success-alert3").fadeTo(2000, 500).slideUp(500, function(){
               $("#success-alert3").slideUp(500);
               $('#input_user-account').trigger("reset");
                console.log(response);
                });
            },
            error: function(error) {
                $( "#error-alert3" ).fadeIn( 300 ).delay( 1500 ).fadeOut( 400 );
                console.log(error);
            }
        });
        /* update the observable refs flag */
       var dataArray = $('#input_user-account').serializeArray();
        var len = dataArray.length;
        dataObj = {};

        for (var i=0; i<len; i++) {
            dataObj[dataArray[i].name] = dataArray[i].value;
        }


        //submit to db : ajax post
        var sendData = JSON.stringify(dataObj, null, 2)
        $.ajax({
            url: '/update_collection_observablerefs',
            data: sendData,
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            success: function(response) {
                    window.location.reload();
                console.log(response);

            },
            error: function(error) {

                console.log(error);
            }
        });

    });
    $('#ua_ext_key').change(function(){
        var key = $(this).val();
        $('#ua_ext_value').keyup(function () {
            var val1 = $(this).val();
            var result = key +":" + val1;
            $('#ua_ext_dict').val(result);
        });
    });

     /* windows-registry key */
    $('#submit_winregkey').click(function() {
        $.ajax({
            url: '/insert_winregkey',
            data: $('#input_windows-registry-key').serialize(),
            type: 'POST',
            success: function(response) {

            $("#success-alert3").fadeTo(2000, 500).slideUp(500, function(){
               $("#success-alert3").slideUp(500);
               $('#input_windows-registry-key').trigger("reset");
                console.log(response);
                });
            },
            error: function(error) {
                $( "#error-alert3" ).fadeIn( 300 ).delay( 1500 ).fadeOut( 400 );
                console.log(error);
            }
        });
        /* update the observable refs flag */
       var dataArray = $('#input_windows-registry-key').serializeArray();
        var len = dataArray.length;
        dataObj = {};

        for (var i=0; i<len; i++) {
            dataObj[dataArray[i].name] = dataArray[i].value;
        }


        //submit to db : ajax post
        var sendData = JSON.stringify(dataObj, null, 2)
        $.ajax({
            url: '/update_collection_observablerefs',
            data: sendData,
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            success: function(response) {
                    window.location.reload();
                console.log(response);

            },
            error: function(error) {

                console.log(error);
            }
        });

    });

    /* x509 certificate */
    $('#submit_x509').click(function() {
        $.ajax({
            url: '/insert_x509',
            data: $('#input_x509-certificate').serialize(),
            type: 'POST',
            success: function(response) {

             $("#success-alert3").fadeTo(2000, 500).slideUp(500, function(){
               $("#success-alert3").slideUp(500);
               $('#input_x509-certificate').trigger("reset");
                console.log(response);
                });
            },
            error: function(error) {
                $( "#error-alert3" ).fadeIn( 300 ).delay( 1500 ).fadeOut( 400 );
                console.log(error);
            }
        });
        /* update the observable refs flag */
       var dataArray = $('#input_x509-certificate').serializeArray();
        var len = dataArray.length;
        dataObj = {};

        for (var i=0; i<len; i++) {
            dataObj[dataArray[i].name] = dataArray[i].value;
        }


        //submit to db : ajax post
        var sendData = JSON.stringify(dataObj, null, 2)
        $.ajax({
            url: '/update_collection_observablerefs',
            data: sendData,
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            success: function(response) {
                    window.location.reload();
                console.log(response);

            },
            error: function(error) {

                console.log(error);
            }
        });

    });


});


