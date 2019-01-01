$(function(){
    $(document).find('.btn_save').hide();
	$(document).find('.btn_cancel').hide();

	 $(document).find('.btn_save2').hide();
	$(document).find('.btn_cancel2').hide();

   /* Update and Delete kill chain data */

               //--->button > edit > start
	$(document).on('click', '.btn_edit', function(event)
	{
		event.preventDefault();
		var tbl_row = $(this).closest('tr');

		var row_id = tbl_row.attr('row_id');

		tbl_row.find('.btn_save').show();
		tbl_row.find('.btn_cancel').show();

		//hide edit & delete button
		tbl_row.find('.btn_edit').hide();
		tbl_row.find('.btn_delete').hide();

		//make the whole row editable
		tbl_row.find('.row_data')
		.attr('contenteditable', 'true')
		.attr('edit_type', 'button')
		.addClass('bg-light')
		.css('padding','3px')

		//--->add the original entry > start
		tbl_row.find('.row_data').each(function(index, val)
		{
			//this will help in case user decided to click on cancel button
			$(this).attr('original_entry', $(this).html());
		});
		//--->add the original entry > end

	});
	//--->button > edit > end

    //--->button > cancel > start
	$(document).on('click', '.btn_cancel', function(event)
	{
		event.preventDefault();

		var tbl_row = $(this).closest('tr');

		var row_id = tbl_row.attr('row_id');

		//hide save and cancel buttons
		tbl_row.find('.btn_save').hide();
		tbl_row.find('.btn_cancel').hide();

		//show edit & delete button
		tbl_row.find('.btn_edit').show();
		tbl_row.find('.btn_delete').show();

		//make the whole row editable
		tbl_row.find('.row_data')
		.attr('edit_type', 'click')
        .attr('contenteditable', 'false')
		.removeClass('bg-light')
		.css('padding','')

		tbl_row.find('.row_data').each(function(index, val)
		{
			$(this).html( $(this).attr('original_entry') );
		});
	});
	//--->button > cancel > end
    //--->save whole row entery > start
	$(document).on('click', '.btn_save', function(event)
	{
		event.preventDefault();
		var tbl_row = $(this).closest('tr');

		var row_id = tbl_row.attr('row_id');


		//hide save and cacel buttons
		tbl_row.find('.btn_save').hide();
		tbl_row.find('.btn_cancel').hide();

		//show edit & delete button
		tbl_row.find('.btn_edit').show();
		tbl_row.find('.btn_delete').show();


		//make the whole row editable
		tbl_row.find('.row_data')
		.attr('edit_type', 'click')
            .attr('contenteditable', 'false')
		.removeClass('bg-light')
		.css('padding','')

		//--->get row data > start
		var arr = {};
		tbl_row.find('.row_data').each(function(index, val)
		{
			var col_name = $(this).attr('col_name');
			var col_val  =  $(this).html();
			arr[col_name] = col_val;
		});
		$.extend(arr, {id:row_id});
		//--->get row data > end

		//use the "arr"	object for your ajax call

        //submit to db : ajax post
        var sendData = JSON.stringify(arr, null, 2)
         $.ajax({
            url: '/updatekillchaindata',
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

	//--->save whole row entery > end
    //--> Delete the entry from db : Delete function
                $(document).on('click', '.btn_delete', function(event){
                    event.preventDefault();
                    var tbl_row = $(this).closest('tr');

                    var row_id = tbl_row.attr('row_id');

                    //--->get row data > start
                    var arr = {};
                    tbl_row.find('.row_data').each(function(index, val)
                    {
                        var col_name = $(this).attr('col_name');
                        var col_val  =  $(this).html();
                        arr[col_name] = col_val;
                    });
                    $.extend(arr, {id:row_id});
                    //--->get row data > end
                    var sendData = JSON.stringify(arr, null, 2)
                     $.ajax({
                        url: '/deletekillchaindata',
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

    /* Update and Delete ext ref data */

               //--->button > edit > start
	$(document).on('click', '.btn_edit2', function(event)
	{
		event.preventDefault();
		var tbl_row = $(this).closest('tr');

		var row_id = tbl_row.attr('row_id');

		tbl_row.find('.btn_save2').show();
		tbl_row.find('.btn_cancel2').show();

		//hide edit & delete button
		tbl_row.find('.btn_edit2').hide();
		tbl_row.find('.btn_delete2').hide();

		//make the whole row editable
		tbl_row.find('.row_data2')
		.attr('contenteditable', 'true')
		.attr('edit_type', 'button')
		.addClass('bg-light')
		.css('padding','3px')

		//--->add the original entry > start
		tbl_row.find('.row_data2').each(function(index, val)
		{
			//this will help in case user decided to click on cancel button
			$(this).attr('original_entry', $(this).html());
		});
		//--->add the original entry > end

	});
	//--->button > edit > end

    //--->button > cancel > start
	$(document).on('click', '.btn_cancel2', function(event)
	{
		event.preventDefault();

		var tbl_row = $(this).closest('tr');

		var row_id = tbl_row.attr('row_id');

		//hide save and cancel buttons
		tbl_row.find('.btn_save2').hide();
		tbl_row.find('.btn_cancel2').hide();

		//show edit & delete button
		tbl_row.find('.btn_edit2').show();
		tbl_row.find('.btn_delete2').show();

		//make the whole row editable
		tbl_row.find('.row_data2')
		.attr('edit_type', 'click')
        .attr('contenteditable', 'false')
		.removeClass('bg-light')
		.css('padding','')

		tbl_row.find('.row_data2').each(function(index, val)
		{
			$(this).html( $(this).attr('original_entry') );
		});
	});
	//--->button > cancel > end
    //--->save whole row entery > start
	$(document).on('click', '.btn_save2', function(event)
	{
		event.preventDefault();
		var tbl_row = $(this).closest('tr');

		var row_id = tbl_row.attr('row_id2');


		//hide save and cacel buttons
		tbl_row.find('.btn_save2').hide();
		tbl_row.find('.btn_cancel2').hide();

		//show edit & delete button
		tbl_row.find('.btn_edit2').show();
		tbl_row.find('.btn_delete2').show();


		//make the whole row editable
		tbl_row.find('.row_data2')
		.attr('edit_type', 'click')
            .attr('contenteditable', 'false')
		.removeClass('bg-light')
		.css('padding','')

		//--->get row data > start
		var arr = {};
		tbl_row.find('.row_data2').each(function(index, val)
		{
			var col_name = $(this).attr('col_name');
			var col_val  =  $(this).html();
			arr[col_name] = col_val;
		});
		$.extend(arr, {id:row_id});
		//--->get row data > end

		//use the "arr"	object for your ajax call

        //submit to db : ajax post
        var sendData = JSON.stringify(arr, null, 2)
         $.ajax({
            url: '/updateextrefdata',
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

	//--->save whole row entery > end
    //--> Delete the entry from db : Delete function
    $(document).on('click', '.btn_delete2', function(event){
                    event.preventDefault();
                    var tbl_row = $(this).closest('tr');

                    var row_id = tbl_row.attr('row_id2');
					var obj_type = 'attack-pattern';
                    //--->get row data > start
                    var arr = {};
                    tbl_row.find('.row_data2').each(function(index, val)
                    {
                        var col_name = $(this).attr('col_name');
                        var col_val  =  $(this).html();
                        arr[col_name] = col_val;
                    });
                    $.extend(arr, {id:row_id});
                    $.extend(arr, {objtype:obj_type});
                    //--->get row data > end
                    var sendData = JSON.stringify(arr, null, 2)
                     $.ajax({
                        url: '/deleteextrefdata',
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