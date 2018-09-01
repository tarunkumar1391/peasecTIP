
$(function() {

$('[data-toggle="tooltip"]').tooltip();

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
    var values = $(this).val();
    $('#final_objref').val(values);
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


});