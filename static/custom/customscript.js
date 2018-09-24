
$(function() {





$('[data-toggle="tooltip"]').tooltip();

$('[data-toggle="popover"]').popover({html:true});



// identity - dropdowns
$('#select_sector').change(function(){
    var values = $(this).val();
    $('#selectors').val(values);
});

// indicator - dropdown
$('#select_label').change(function(){
    var values = $(this).val();
    $('#label_final').val(values);
});

// intrusion set - dropdowns
$('#secondary_motiv').change(function(){
    var values = $(this).val();
    $('#secondary_motiv_final').val(values);
});

// malware - dropdowns
$('#labels').change(function(){
    var values = $(this).val();
    $('#labels_final').val(values);
});

// report - dropdowns
$('#reportlabels').change(function(){
     var values = $(this).val();
    $('#final_label').val(values);
});
// report - dropdowns
$('#obj_ref').change(function(){
    finalresult = [];
    //var id = JSON.stringify($(this).find(":selected").attr('objid'));
    //var type = JSON.stringify($(this).find(":selected").attr('objtype'));
    var option = $(this).find('option:selected');
    option.each(function () {

        var id = $(this).attr('objid');
        var type = $(this).attr('objtype');
        item = {};
        item["objid"] = id;
        item["objtype"] = type;
        finalresult.push(item);

    })



    //var result =  id+ ':'+ type;
   // var values = $(this).val();
    $('#final_objref').val(JSON.stringify(finalresult));

});

// tool - dropdowns
$('#tool_label').change(function(){
    var values = $(this).val();
    $('#tool_label_final').val(values);
});

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
$('#sec_motiv').change(function(){
    var values = $(this).val();
    $('#ta_sec_motiv_final').val(values);
});
// threat-actor - dropdowns
$('#per_motiv').change(function(){
    var values = $(this).val();
    $('#ta_per_motiv_final').val(values);
});
// malware-family - multiple select
    $('#familylabels').change(function(){
    var values = $(this).val();
    $('#familylabels_final').val(values);
});
// malware-instance - multiple select
    $('#malinstancelabels').change(function(){
    var values = $(this).val();
    $('#malinstancelabels_final').val(values);
});
    $('#osexecenv').change(function(){
    var values = $(this).val();
    $('#osexecenv_final').val(values);
});
    $('#archexec_env').change(function(){
    var values = $(this).val();
    $('#archexec_env_final').val(values);
});
    $('#os_feat').change(function(){
    var values = $(this).val();
    $('#os_feat_final').val(values);
});

// script for relationship object

    $("#success-alert1").hide();
    $("#error-alert1").hide();
    $("#success-alert2").hide();
    $("#error-alert2").hide();
    $("#success-alert3").hide();
    $("#error-alert3").hide();
var relationships =  [{
 	"attack-pattern": [{
 		"targets": [{
 			"1": "vulnerability",
 			"2": "Identity"
 		}],
 		"uses": [{
 			"1": "malware",
 			"2": "tool"
 		}]
 	}],
 	"campaign": [{
 		"attributed-to": [{
 			"1": "intrusion-set",
 			"2": "threat-actor"
 		}],
 		"targets": [{
 			"1": "identity",
 			"2": "vulnerability"
 		}],
 		"uses": [{
 			"1": "attack-pattern",
 			"2": "malware",
 			"3": "tool"

 		}]

 	}],
 	"indicator": [{
 		"indicates": [{
 			"1": "attack-pattern",
 			"2": "campaign",
 			"3": "intrusion-set",
 			"4": "malware",
 			"5": "threat-actor",
 			"6": "tool"
 		}]

 	}],
 	"intrusion-set": [{
 		"attributed-to": [{
 			"1": "threat-actor"
 		}],
 		"targets": [{
 			"1": "identity",
 			"2": "vulnerability"
 		}],
 		"uses": [{
 			"1": "attack-pattern",
 			"2": "malware",
 			"3": "tool"
 		}]
 	}],
 	"malware": [{
 		"targets": [{
 			"1": "identity",
 			"2": "vulnerability"
 		}],
 		"uses": [{
 			"1": "tool"
 		}],
 		"variant-of": [{
 			"1": "malware"
 		}]
 	}],
 	"threat-actor": [{
 		"attributed-to": [{
 			"1": "identity"
 		}],
 		"impersonates": [{
 			"1": "identity"
 		}],
 		"targets": [{
 			"1": "identity",
 			"2": "vulnerability"
 		}],
 		"uses": [{
 			"1": "attack-pattern",
 			"2": "malware",
 			"3": "tool"
 		}]
 	}],
 	"tool": [{
 		"targets": [{
 			"1": "identity",
 			"2": "vulnerability"
 		}]

 	}]

 }];
var src_type = $('#source_type');
var relationship_type = $('#relationshipType');
var target_type = $('#target_type');
var src_type_value, relationship_type_value;
src_type.change(function(){
    src_type_value = $(this).val();
    // attack-pattern
    if(src_type_value == "attack-pattern"){
        relationship_type.children('option:not(:first)').remove();
        relationship_type.append('<option value="targets">targets</option>');
        relationship_type.append('<option value="uses">uses</option>');
    }
    // campaign
    if(src_type_value == "campaign"){
        relationship_type.children('option:not(:first)').remove();
        relationship_type.append('<option value="attributed-to">attributed-to</option>');
        relationship_type.append('<option value="targets">targets</option>');
        relationship_type.append('<option value="uses">uses</option>');
    }
    // Indicator
    if(src_type_value == "indicator"){
        relationship_type.children('option:not(:first)').remove();
        relationship_type.append('<option value="indicates">indicates</option>');
    }
    // intrusion-set
    if(src_type_value == "intrusion-set"){
        relationship_type.children('option:not(:first)').remove();
        relationship_type.append('<option value="attributed-to">attributed-to</option>');
        relationship_type.append('<option value="targets">targets</option>');
        relationship_type.append('<option value="uses">uses</option>');
    }
    // malware
    if(src_type_value == "malware"){
        relationship_type.children('option:not(:first)').remove();
        relationship_type.append('<option value="targets">targets</option>');
        relationship_type.append('<option value="uses">uses</option>');
        relationship_type.append('<option value="variant-of">variant-of</option>');
    }
    // threat-actor
    if(src_type_value == "threat-actor"){
        relationship_type.children('option:not(:first)').remove();
        relationship_type.append('<option value="attributed-to">attributed-to</option>');
        relationship_type.append('<option value="impersonates">impersonates</option>');
        relationship_type.append('<option value="targets">targets</option>');
        relationship_type.append('<option value="uses">uses</option>');
    }
    // tool
    if(src_type_value == "tool"){
        relationship_type.children('option:not(:first)').remove();
        relationship_type.append('<option value="targets">targets</option>');
    }
    // behavior
    if(src_type_value == "behavior"){
        relationship_type.children('option:not(:first)').remove();
        relationship_type.append('<option value="dependent-on">dependent-on</option>');
        relationship_type.append('<option value="discovered-by">discovered-by</option>');
    }
    // Malware action
    if(src_type_value == "malware-action"){
        relationship_type.children('option:not(:first)').remove();
        relationship_type.append('<option value="dependent-on">dependent-on</option>');
        relationship_type.append('<option value="discovered-by">discovered-by</option>');
    }
    // Malware family
    if(src_type_value == "malware-family"){
        relationship_type.children('option:not(:first)').remove();
        relationship_type.append('<option value="dropped-by">dropped-by</option>');
        relationship_type.append('<option value="derived-from">derived-from</option>');
    }
    // Malware instance
    if(src_type_value == "malware-instance"){
        relationship_type.children('option:not(:first)').remove();
        relationship_type.append('<option value="ancestor-of">ancestor-of</option>');
        relationship_type.append('<option value="downloaded-by">downloaded-by</option>');
        relationship_type.append('<option value="dropped-by">dropped-by</option>');
        relationship_type.append('<option value="derived-from ">derived-from</option>');
        relationship_type.append('<option value="extracted-from">extracted-from</option>');
        relationship_type.append('<option value="has-distance ">has-distance</option>');
        relationship_type.append('<option value="installed-by">installed-by</option>');
        relationship_type.append('<option value="variant-of">variant-of</option>');
    }
});
relationship_type.change(function(){
    relationship_type_value = $(this).val();
    // attack pattern - targets, uses
    if(src_type_value == "attack-pattern" && relationship_type_value == "targets"){
        target_type.children('option:not(:first)').remove();
        target_type.append('<option value="vulnerability">vulnerability</option>');
        target_type.append('<option value="identity">identity</option>');
    }
    if(src_type_value== "attack-pattern" && relationship_type_value == "uses"){
        target_type.children('option:not(:first)').remove();
        $('#target_type').append('<option value="malware">malware</option>');
        $('#target_type').append('<option value="tool">tool</option>');
    }
    // campaign - attributed-to, targets, uses
    if(src_type_value == "campaign" && relationship_type_value == "attributed-to"){
        target_type.children('option:not(:first)').remove();
        target_type.append('<option value="intrusion-set">intrusion-set</option>');
        target_type.append('<option value="threat-actor">threat-actor</option>');
    }
    if(src_type_value == "campaign" && relationship_type_value == "targets"){
        target_type.children('option:not(:first)').remove();
        target_type.append('<option value="identity">identity</option>');
        target_type.append('<option value="vulnerability">vulnerability</option>');
    }
    if(src_type_value == "campaign" && relationship_type_value == "uses"){
        target_type.children('option:not(:first)').remove();
        target_type.append('<option value="attack-pattern">attack-pattern</option>');
        target_type.append('<option value="malware">malware</option>');
        target_type.append('<option value="tool">tool</option>');
    }
    // Indicator - indicates
    if(src_type_value == "indicator" && relationship_type_value == "indicates"){
        target_type.children('option:not(:first)').remove();
        target_type.append('<option value="attack-pattern">attack-pattern</option>');
        target_type.append('<option value="campaign">campaign</option>');
        target_type.append('<option value="intrusion-set">intrusion-set</option>');
        target_type.append('<option value="malware">malware</option>');
        target_type.append('<option value="threat-actor">threat-actor</option>');
        target_type.append('<option value="tool">tool</option>');
    }
    // intrusion-set  - attributed-to, targets, uses
    if(src_type_value == "intrusion-set" && relationship_type_value == "attributed-to"){
        target_type.children('option:not(:first)').remove();
        target_type.append('<option value="threat-actor">threat-actor</option>');
    }
    if(src_type_value == "intrusion-set" && relationship_type_value == "targets"){
        target_type.children('option:not(:first)').remove();
        target_type.append('<option value="identity">identity</option>');
        target_type.append('<option value="vulnerability">vulnerability</option>');
    }
    if(src_type_value == "intrusion-set" && relationship_type_value == "uses"){
        target_type.children('option:not(:first)').remove();
        target_type.append('<option value="attack-pattern">attack-pattern</option>');
        target_type.append('<option value="malware">malware</option>');
        target_type.append('<option value="tool">tool</option>');
    }
    // malware  -  targets, uses, variant-of
    if(src_type_value == "malware" && relationship_type_value == "targets"){
        target_type.children('option:not(:first)').remove();
        target_type.append('<option value="identity">identity</option>');
        target_type.append('<option value="vulnerability">vulnerability</option>');
    }
    if(src_type_value == "malware" && relationship_type_value == "uses"){
        target_type.children('option:not(:first)').remove();
        target_type.append('<option value="tool">tool</option>');
    }
    if(src_type_value == "malware" && relationship_type_value == "variant-of"){
        target_type.children('option:not(:first)').remove();
        target_type.append('<option value="malware">malware</option>');
    }
    // threat-actor  - attributed-to , impersonates,  targets, uses
    if(src_type_value == "threat-actor" && relationship_type_value == "attributed-to"){
        target_type.children('option:not(:first)').remove();
        target_type.append('<option value="identity">identity</option>');
    }
    if(src_type_value == "threat-actor" && relationship_type_value == "impersonates"){
        target_type.children('option:not(:first)').remove();
        target_type.append('<option value="identity">identity</option>');
    }
    if(src_type_value == "threat-actor" && relationship_type_value == "targets"){
        target_type.children('option:not(:first)').remove();
        target_type.append('<option value="identity">identity</option>');
        target_type.append('<option value="vulnerability">vulnerability</option>');
    }
    if(src_type_value == "threat-actor" && relationship_type_value == "uses"){
        target_type.children('option:not(:first)').remove();
        target_type.append('<option value="attack-pattern">attack-pattern</option>');
        target_type.append('<option value="malware">malware</option>');
        target_type.append('<option value="tool">tool</option>');
    }
    // tool - targets
    if(src_type_value == "tool" && relationship_type_value == "targets"){
        target_type.children('option:not(:first)').remove();
        target_type.append('<option value="identity">identity</option>');
        target_type.append('<option value="vulnerability">vulnerability</option>');
    }
    // Behavior - targets
    if(src_type_value == "behavior" && relationship_type_value == "dependent-on"){
        target_type.children('option:not(:first)').remove();
        target_type.append('<option value="behavior">behavior</option>');
    }
    if(src_type_value == "behavior" && relationship_type_value == "discovered-by"){
        target_type.children('option:not(:first)').remove();
        target_type.append('<option value="software">software</option>');
    }
    // Malware action - targets
    if(src_type_value == "malware-action" && relationship_type_value == "dependent-on"){
        target_type.children('option:not(:first)').remove();
        target_type.append('<option value="malware-action">malware-action</option>');
    }
    if(src_type_value == "malware-action" && relationship_type_value == "discovered-by"){
        target_type.children('option:not(:first)').remove();
        target_type.append('<option value="software">software</option>');
    }
    // Malware family - targets
    if(src_type_value == "malware-family" && relationship_type_value == "dropped-by"){
        target_type.children('option:not(:first)').remove();
        target_type.append('<option value="malware-family">malware-family</option>');
    }
    if(src_type_value == "malware-family" && relationship_type_value == "derived-from"){
        target_type.children('option:not(:first)').remove();
        target_type.append('<option value="malware-family">malware-family</option>');
    }
    // Malware instance - targets
    if(src_type_value == "malware-instance" && relationship_type_value == "ancestor-of"){
        target_type.children('option:not(:first)').remove();
        target_type.append('<option value="malware-family">malware-instance</option>');
    }
    if(src_type_value == "malware-instance" && relationship_type_value == "downloaded-by"){
        target_type.children('option:not(:first)').remove();
        target_type.append('<option value="malware-family">malware-family</option>');
        target_type.append('<option value="malware-instance">malware-instance</option>');
    }
    if(src_type_value == "malware-instance" && relationship_type_value == "dropped-by"){
        target_type.children('option:not(:first)').remove();
        target_type.append('<option value="malware-family">malware-family</option>');
        target_type.append('<option value="malware-instance">malware-instance</option>');
    }
    if(src_type_value == "malware-instance" && relationship_type_value == "derived-from"){
        target_type.children('option:not(:first)').remove();
        target_type.append('<option value="malware-family">malware-family</option>');
        target_type.append('<option value="malware-instance">malware-instance</option>');
    }
    if(src_type_value == "malware-instance" && relationship_type_value == "extracted-from"){
        target_type.children('option:not(:first)').remove();
        target_type.append('<option value="malware-instance">malware-instance</option>');
    }
    if(src_type_value == "malware-instance" && relationship_type_value == "has-distance"){
        target_type.children('option:not(:first)').remove();
        target_type.append('<option value="malware-instance">malware-instance</option>');
    }
    if(src_type_value == "malware-instance" && relationship_type_value == "installed-by"){
        target_type.children('option:not(:first)').remove();
        target_type.append('<option value="malware-family">malware-family</option>');
        target_type.append('<option value="malware-instance">malware-instance</option>');
    }
    if(src_type_value == "malware-instance" && relationship_type_value == "variant-of"){
        target_type.children('option:not(:first)').remove();
        target_type.append('<option value="malware-family">malware-family</option>');
        target_type.append('<option value="malware-instance">malware-instance</option>');
    }
});

/* create relationship object*/
    $('#create_relationship').click(function() {
        $.ajax({
            url: '/create_relationship',
            data: $('#relationshipform').serialize(),
            type: 'POST',
            success: function(response) {

             //   $("#success-alert1").fadeTo(2000, 500).slideUp(500, function(){
             //  $("#success-alert1").slideUp(500);
            //    });
                $( "#success-alert1" ).fadeIn( 300 ).delay( 2000 ).fadeOut( 400, function () {
                     window.location.reload();
                 } );
                console.log(response);
            },
            error: function(error) {
                $( "#error-alert1" ).fadeIn( 300 ).delay( 1500 ).fadeOut( 400 );
                console.log(error);

            }
        });

    });

 /* view STIX content */
    $(document).on('click','#view_content',(function() {
        var tbl_row = $(this).closest('tr');
		var row_id = tbl_row.attr('row_id');
        type = tbl_row.find('#stix_type').text();
        stixid = tbl_row.find('#stix_id').text();
        arr = {};
        arr['type']=type;
        arr['stixid']=stixid;
        var sendData = JSON.stringify(arr, null, 2)
        $.ajax({
            url: '/view_stixcontent',
            data: sendData,
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            success: function(response) {
               // $.getJSON("view_stixcontent", function (data) {
                 //   $('#display_publishedcontent').html(data);
                  //  console.log(data);
                //})
                var result = JSON.stringify(response, null,"\t")
                $('#display_publishedcontent').addClass('alert-success').removeClass('alert-danger').text(result);
                console.log(response);
            },
            error: function(error) {
                var result = JSON.stringify(error.responseText, null,"\t")
                $('#display_publishedcontent').addClass('alert-danger').removeClass('alert-success').text(result);
                console.log(error);

            }
        });

    }));

    /* view MAEC content */
    $(document).on('click','#view_maec_content',(function() {
        var tbl_row = $(this).closest('tr');
		var row_id = tbl_row.attr('row_id');
        type = tbl_row.find('#maec_type').text();
        maecid = tbl_row.find('#maec_id').text();
        arr = {};
        arr['type']=type;
        arr['maecid']=maecid;
        var sendData = JSON.stringify(arr, null, 2)
        $.ajax({
            url: '/view_maeccontent',
            data: sendData,
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            success: function(response) {
               // $.getJSON("view_stixcontent", function (data) {
                 //   $('#display_publishedcontent').html(data);
                  //  console.log(data);
                //})
                var result = JSON.stringify(response, null,"\t")
                $('#display_publishedmaeccontent').addClass('alert-success').removeClass('alert-danger').text(result);
                console.log(response);
            },
            error: function(error) {
                var result = JSON.stringify(error.responseText, null,"\t")
                $('#display_publishedmaeccontent').addClass('alert-danger').removeClass('alert-success').text(result);
                console.log(error);

            }
        });

    }));
    /* bundle drop down */
$('#bundle').change(function(){
    finalresult = [];
    //var id = JSON.stringify($(this).find(":selected").attr('objid'));
    //var type = JSON.stringify($(this).find(":selected").attr('objtype'));
    var option = $(this).find('option:selected');
    option.each(function () {

        var id = $(this).attr('reftype');
        var stixid = $(this).attr('refstix');
        item = {};
        item["reftype"] = id;
        item["refstix"] = stixid;
        finalresult.push(item);

    });
    $('#final_bundle').val(JSON.stringify(finalresult));

});
/* create bundle object*/
    $('#create_bundle').click(function() {
        $.ajax({
            url: '/create_bundle',
            data: $('#bundleform').serialize(),
            type: 'POST',
            success: function(response) {

             //   $("#success-alert1").fadeTo(2000, 500).slideUp(500, function(){
             //  $("#success-alert1").slideUp(500);
            //    });
                $( "#success-alert2" ).fadeIn( 300 ).delay( 2000 ).fadeOut( 400, function () {
                     window.location.reload();
                 } );
                console.log(response);
            },
            error: function(error) {
                $( "#error-alert2" ).fadeIn( 300 ).delay( 1500 ).fadeOut( 400 );
                console.log(error);

            }
        });

    });
     /* package drop down */
$('#package').change(function(){
    finalresult = [];
    //var id = JSON.stringify($(this).find(":selected").attr('objid'));
    //var type = JSON.stringify($(this).find(":selected").attr('objtype'));
    var option = $(this).find('option:selected');
    option.each(function () {

        var type = $(this).attr('reftype');
        var maecid = $(this).attr('refmaec');
        item = {};
        item["reftype"] = type;
        item["refmaec"] = maecid;
        finalresult.push(item);

    });
    $('#final_package').val(JSON.stringify(finalresult));
 });

    /* create package object*/
    $('#create_package').click(function() {
        $.ajax({
            url: '/create_package',
            data: $('#packageform').serialize(),
            type: 'POST',
            success: function(response) {

             //   $("#success-alert1").fadeTo(2000, 500).slideUp(500, function(){
             //  $("#success-alert1").slideUp(500);
            //    });
                $( "#success-alert3" ).fadeIn( 300 ).delay( 2000 ).fadeOut( 400, function () {
                     window.location.reload();
                 } );
                console.log(response);
            },
            error: function(error) {
                $( "#error-alert3" ).fadeIn( 300 ).delay( 1500 ).fadeOut( 400 );
                console.log(error);

            }
        });

    });

    /* view Bundle content */
    $(document).on('click','#view_bundledata',(function() {
        var tbl_row = $(this).closest('tr');
		var row_id = tbl_row.attr('row_id');
        bundleid = tbl_row.find('#bundle_id').text();
        arr = {};
        arr['type']="bundle";
        arr['bundleid']=bundleid;
        var sendData = JSON.stringify(arr, null, 2)
        $.ajax({
            url: '/view_bundle',
            data: sendData,
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            success: function(response) {
               // $.getJSON("view_stixcontent", function (data) {
                 //   $('#display_publishedcontent').html(data);
                  //  console.log(data);
                //})
                var result = JSON.stringify(response, null,"\t")
                $('#display_bundlecontent').addClass('alert-success').removeClass('alert-danger').text(response);
                console.log(result);
            },
            error: function(error) {
                var result = JSON.stringify(error.responseText, null,"\t")
                $('#display_bundlecontent').addClass('alert-danger').removeClass('alert-success').text(result);
                console.log(error);

            }
        });

    }));

     /* view package content */
    $(document).on('click','#view_packagedata',(function() {
        var tbl_row = $(this).closest('tr');
		var row_id = tbl_row.attr('row_id');
        packageid = tbl_row.find('#package_id').text();
        arr = {};
        arr['type']="package";
        arr['packageid']=packageid;
        var sendData = JSON.stringify(arr, null, 2)
        $.ajax({
            url: '/view_package',
            data: sendData,
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            success: function(response) {
               // $.getJSON("view_stixcontent", function (data) {
                 //   $('#display_publishedcontent').html(data);
                  //  console.log(data);
                //})
                var result = JSON.stringify(response, null,"\t")
                $('#display_packagecontent').addClass('alert-success').removeClass('alert-danger').text(response);
                console.log(result);
            },
            error: function(error) {
                var result = JSON.stringify(error.responseText, null,"\t")
                $('#display_packagecontent').addClass('alert-danger').removeClass('alert-success').text(result);
                console.log(error);

            }
        });

    }));

    /* fetch bundle data */
    $(document).on('change','#bundle_dropdown',(function() {


        bundleid = $(this).val();
        arr = {};
        arr['type']="bundle";
        arr['bundleid']= bundleid;
        var sendData = JSON.stringify(arr, null, 2)
        $.ajax({
            url: '/view_bundle',
            data: sendData,
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            success: function(response) {
               // $.getJSON("view_stixcontent", function (data) {
                 //   $('#display_publishedcontent').html(data);
                  //  console.log(data);
                //})
                var result = JSON.stringify(response, null,"\t")
                $('#paste-area').addClass('alert-success').removeClass('alert-danger').text(response);

            },
            error: function(error) {
                var result = JSON.stringify(error.responseText, null,"\t")
                $('#paste-area').addClass('alert-danger').removeClass('alert-success').text(result);
                console.log(error);

            }
        });

    }));
    /* reset bundle form data */
    $('#bundleform_reset').click(function() {
        $('#bundle_dropdown').val(0);
        $('#paste-area').text('').removeClass('alert-success').removeClass('alert-danger');


    });

});