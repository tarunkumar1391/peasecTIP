$(function(){


    /* Update and Delete observable references*/


    //--->save whole row entery > start
	$(document).on('click', '.btn_view', function(event)
	{
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
		$.extend(arr, {objtype:"collection"});

		//--->get row data > end

		//use the "arr"	object for your ajax call
        if (arr['obs_type'] == "artifact"){
            //submit to db : ajax post
        var sendData = JSON.stringify(arr, null, 2)
         $.ajax({
            url: '/fetch_artifact',
            data: sendData,
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            success: function(response) {
                $('#sno').text(response.id);
                $('#mime_type').text(response.mime_type);
                $('#payload_bin').text(response.payload_bin);
                $('#url').text(response.hash_type);
                $('#hash_val').text(response.hash_value);
            },
            error: function(error) {

                console.log(error);
            }
        });
        }
        if (arr['obs_type'] == "autonomous-system"){
                //submit to db : ajax post
        var sendData = JSON.stringify(arr, null, 2)
         $.ajax({
            url: '/fetch_autonomoussystem',
            data: sendData,
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            success: function(response) {
                console.log(response);
                $('#sno').text(response.id);
                $('#number').text(response.number);
                $('#name').text(response.name);
                $('#rir').text(response.rir);

            },
            error: function(error) {

                console.log(error);
            }
        });
        }
        if (arr['obs_type'] == "directory"){
                //submit to db : ajax post
        var sendData = JSON.stringify(arr, null, 2)
         $.ajax({
            url: '/fetch_directory',
            data: sendData,
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            success: function(response) {
                $('#sno').text(response.id);
                $('#path').text(response.path);
                $('#path_enc').text(response.path_enc);
                $('#created').text(response.created);
                $('#modified').text(response.modified);
                $('#accessed').text(response.accessed);
                $('#contains_refs').text(response.contains_refs);

            },
            error: function(error) {

                console.log(error);
            }
        });
        }
        if (arr['obs_type'] == "domain-name"){
                //submit to db : ajax post
        var sendData = JSON.stringify(arr, null, 2)
         $.ajax({
            url: '/fetch_domainname',
            data: sendData,
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            success: function(response) {
                $('#sno').text(response.id);
                $('#value').text(response.value);
                $('#resolves_to_refs').text(response.resolves_to_refs);

            },
            error: function(error) {

                console.log(error);
            }
        });
        }
        if (arr['obs_type'] == "email-addr"){
                //submit to db : ajax post
        var sendData = JSON.stringify(arr, null, 2)
         $.ajax({
            url: '/fetch_emailaddr',
            data: sendData,
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            success: function(response) {
                $('#sno').text(response.id);
                $('#value').text(response.value);
                $('#display_name').text(response.display_name);
                $('#belongs_to_ref').text(response.belongs_to_ref);

            },
            error: function(error) {

                console.log(error);
            }
        });
        }
        if (arr['obs_type'] == "email-message"){
                //submit to db : ajax post
        var sendData = JSON.stringify(arr, null, 2)
         $.ajax({
            url: '/fetch_emailaddr',
            data: sendData,
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            success: function(response) {
                $('#sno').text(response.id);
                $('#is_multipart').text(response.is_multipart);
                $('#date').text(response.date);
                $('#content_type').text(response.content_type);
                $('#from_ref').text(response.from_ref);
                $('#sender_ref').text(response.sender_ref);
                $('#to_refs').text(response.to_refs);
                $('#cc_refs').text(response.cc_refs);
                $('#bcc_refs').text(response.bcc_refs);
                $('#subject').text(response.subject);
                $('#received_lines').text(response.received_lines);
                $('#additional_header_fields').text(response.additional_header_fields);
                $('#body').text(response.body);
                $('#raw_email_ref').text(response.raw_email_ref);

            },
            error: function(error) {

                console.log(error);
            }
        });
        }
        if (arr['obs_type'] == "file"){
                //submit to db : ajax post
        var sendData = JSON.stringify(arr, null, 2)
         $.ajax({
            url: '/fetch_file',
            data: sendData,
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            success: function(response) {
                $('#sno').text(response.id);
                $('#extensions').text(response.extension);
                $('#hashes').text(response.hashes);
                $('#size').text(response.size);
                $('#name').text(response.name);
                $('#name_enc').text(response.name_enc);
                $('#magic_number_hex').text(response.magic_number_hex);
                $('#mime_type').text(response.mime_type);
                $('#created').text(response.created);
                $('#modified').text(response.modified);
                $('#accessed').text(response.accessed);
                $('#parent_directory_ref').text(response.parent_directory_ref);
                $('#is_encrypted').text(response.is_encrypted);
                $('#encryption_algorithm').text(response.encryption_algorithm);
                $('#decryption_key').text(response.decryption_key);
                $('#content_ref').text(response.content_ref);

            },
            error: function(error) {

                console.log(error);
            }
        });
        }
        if (arr['obs_type'] == "ipv4-addr"){
                //submit to db : ajax post
        var sendData = JSON.stringify(arr, null, 2)
         $.ajax({
            url: '/fetch_ipv4',
            data: sendData,
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            success: function(response) {
                $('#sno').text(response.id);
                $('#value').text(response.value);
                $('#resolves_to_refs').text(response.resolves_to_refs);
                $('#belongs_to_refs').text(response.belongs_to_refs);

            },
            error: function(error) {

                console.log(error);
            }
        });
        }
        if (arr['obs_type'] == "ipv6-addr"){
                //submit to db : ajax post
        var sendData = JSON.stringify(arr, null, 2)
         $.ajax({
            url: '/fetch_ipv6',
            data: sendData,
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            success: function(response) {
                $('#sno').text(response.id);
                $('#value').text(response.value);
                $('#resolves_to_refs').text(response.resolves_to_refs);
                $('#belongs_to_refs').text(response.belongs_to_refs);

            },
            error: function(error) {

                console.log(error);
            }
        });
        }
        if (arr['obs_type'] == "mac-addr"){
                //submit to db : ajax post
        var sendData = JSON.stringify(arr, null, 2)
         $.ajax({
            url: '/fetch_mac',
            data: sendData,
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            success: function(response) {
                $('#sno').text(response.id);
                $('#value').text(response.value);

            },
            error: function(error) {

                console.log(error);
            }
        });
        }
        if (arr['obs_type'] == "network-traffic"){
                //submit to db : ajax post
        var sendData = JSON.stringify(arr, null, 2)
         $.ajax({
            url: '/fetch_networktraffic',
            data: sendData,
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            success: function(response) {
                $('#sno').text(response.id);
                $('#extensions').text(response.extensions);
                $('#start').text(response.start);
                $('#end').text(response.end);
                $('#is_active').text(response.is_active);
                $('#src_ref').text(response.src_ref);
                $('#dst_ref').text(response.dst_ref);
                $('#src_port').text(response.src_port);
                $('#dst_port').text(response.dst_port);
                $('#protocols').text(response.protocols);
                $('#src_byte_count').text(response.src_byte_count);
                $('#dst_byte_count').text(response.dst_byte_count);
                $('#src_packets').text(response.src_packets);
                $('#dst_packets').text(response.dst_packets);
                $('#ipfix').text(response.ipfix);
                $('#src_payload_ref').text(response.src_payload_ref);
                $('#dst_payload_ref').text(response.dst_payload_ref);
                $('#encapsulated_refs').text(response.encapsulated_refs);
                $('#encapsulated_by_ref').text(response.encapsulated_by_ref);

            },
            error: function(error) {

                console.log(error);
            }
        });
        }
        if (arr['obs_type'] == "process"){
                //submit to db : ajax post
        var sendData = JSON.stringify(arr, null, 2)
         $.ajax({
            url: '/fetch_process',
            data: sendData,
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            success: function(response) {
                $('#sno').text(response.id);
                $('#extensions').text(response.extensions);
                $('#is_hidden').text(response.is_hidden);
                $('#pid').text(response.pid);
                $('#name').text(response.name);
                $('#created').text(response.created);
                $('#cwd').text(response.cwd);
                $('#arguments').text(response.arguments);
                $('#command_line').text(response.command_line);
                $('#environment_variables').text(response.environment_variables);
                $('#opened_connection_refs').text(response.opened_connection_refs);
                $('#creator_user_ref').text(response.creator_user_ref);
                $('#binary_ref').text(response.binary_ref);
                $('#parent_ref').text(response.parent_ref);
                $('#child_refs').text(response.child_refs);
            },
            error: function(error) {

                console.log(error);
            }
        });
        }
        if (arr['obs_type'] == "software"){
                //submit to db : ajax post
        var sendData = JSON.stringify(arr, null, 2)
         $.ajax({
            url: '/fetch_software',
            data: sendData,
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            success: function(response) {
                $('#sno').text(response.id);
                $('#name').text(response.name);
                $('#cpe').text(response.cpe);
                $('#languages').text(response.languages);
                $('#vendor').text(response.vendor);
                $('#version').text(response.version);

            },
            error: function(error) {

                console.log(error);
            }
        });
        }
        if (arr['obs_type'] == "url"){
                //submit to db : ajax post
        var sendData = JSON.stringify(arr, null, 2)
         $.ajax({
            url: '/fetch_url',
            data: sendData,
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            success: function(response) {
                $('#sno').text(response.id);
                $('#value').text(response.value);

            },
            error: function(error) {

                console.log(error);
            }
        });
        }
        if (arr['obs_type'] == "user-account"){
                //submit to db : ajax post
        var sendData = JSON.stringify(arr, null, 2)
         $.ajax({
            url: '/fetch_useracc',
            data: sendData,
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            success: function(response) {
                $('#sno').text(response.id);
                $('#extensions').text(response.extensions);
                $('#user_id').text(response.user_id);
                $('#account_login').text(response.account_login);
                $('#account_type').text(response.account_type);
                $('#display_name').text(response.display_name);
                $('#is_service_account').text(response.is_service_account);
                $('#is_privileged').text(response.is_privileged);
                $('#can_escalate_privs').text(response.can_escalate_privs);
                $('#is_disabled').text(response.is_disabled);
                $('#account_created').text(response.account_created);
                $('#account_expires').text(response.account_expires);
                $('#password_last_changed').text(response.password_last_changed);
                $('#account_first_login').text(response.account_first_login);
                $('#account_last_login').text(response.account_last_login);

            },
            error: function(error) {

                console.log(error);
            }
        });
        }
        if (arr['obs_type'] == "windows-registry-key"){
                //submit to db : ajax post
        var sendData = JSON.stringify(arr, null, 2)
         $.ajax({
            url: '/fetch_winregkey',
            data: sendData,
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            success: function(response) {
                $('#sno').text(response.id);
                $('#key').text(response.key);
                $('#modified').text(response.modified);
                $('#creator_user_ref').text(response.creator_user_ref);
                $('#number_of_subkeys').text(response.number_of_subkeys);
            },
            error: function(error) {

                console.log(error);
            }
        });
        }
        if (arr['obs_type'] == "x509-certificate"){
                //submit to db : ajax post
        var sendData = JSON.stringify(arr, null, 2)
         $.ajax({
            url: '/fetch_x509',
            data: sendData,
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: 'json',
            success: function(response) {
                $('#sno').text(response.id);
                $('#is_self_signed').text(response.is_self_signed);
                $('#hash_type').text(response.hash_type);
                $('#hash_value').text(response.hash_value);
                $('#version').text(response.version);
                $('#serial_number').text(response.serial_number);
                $('#signature_algorithm').text(response.signature_algorithm);
                $('#issuer').text(response.issuer);
                $('#validity_not_before').text(response.validity_not_before);
                $('#validity_not_after').text(response.validity_not_after);
                $('#subject').text(response.subject);
                $('#subject_public_key_algorithm').text(response.subject_public_key_algorithm);
                $('#subject_public_key_modulus').text(response.subject_public_key_modulus);
                $('#subject_public_key_exponent').text(response.subject_public_key_exponent);


            },
            error: function(error) {

                console.log(error);
            }
        });
        }

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
                   $.extend(arr, {objtype:"collection"});
                    //--->get row data > end
            if (arr['obs_type'] == "artifact"){
            //submit to db : ajax post
            var sendData = JSON.stringify(arr, null, 2);
                     $.ajax({
                        url: '/delete_artifact',
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
                }
            if (arr['obs_type'] == "autonomous-system"){
                ///submit to db : ajax post
            var sendData = JSON.stringify(arr, null, 2);
                     $.ajax({
                        url: '/delete_autonomoussystem',
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
        }
            if (arr['obs_type'] == "directory"){
           ///submit to db : ajax post
            var sendData = JSON.stringify(arr, null, 2);
                     $.ajax({
                        url: '/delete_directory',
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
            }
            if (arr['obs_type'] == "domain-name"){
                   ///submit to db : ajax post
            var sendData = JSON.stringify(arr, null, 2);
                     $.ajax({
                        url: '/delete_domainname',
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
            }
            if (arr['obs_type'] == "email-addr"){
                  ///submit to db : ajax post
            var sendData = JSON.stringify(arr, null, 2);
                     $.ajax({
                        url: '/delete_emailaddr',
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
            }
            if (arr['obs_type'] == "email-message"){
                  ///submit to db : ajax post
            var sendData = JSON.stringify(arr, null, 2);
                     $.ajax({
                        url: '/delete_emailmsg',
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
            }
            if (arr['obs_type'] == "file"){
                  ///submit to db : ajax post
            var sendData = JSON.stringify(arr, null, 2);
                     $.ajax({
                        url: '/delete_file',
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
            }
            if (arr['obs_type'] == "ipv4-addr"){
                  ///submit to db : ajax post
            var sendData = JSON.stringify(arr, null, 2);
                     $.ajax({
                        url: '/delete_ipv4',
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
            }
            if (arr['obs_type'] == "ipv6-addr"){
                  ///submit to db : ajax post
            var sendData = JSON.stringify(arr, null, 2);
                     $.ajax({
                        url: '/delete_ipv6',
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
            }
            if (arr['obs_type'] == "mac-addr"){
                  ///submit to db : ajax post
            var sendData = JSON.stringify(arr, null, 2);
                     $.ajax({
                        url: '/delete_mac',
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
            }
            if (arr['obs_type'] == "network-traffic"){
                  ///submit to db : ajax post
            var sendData = JSON.stringify(arr, null, 2);
                     $.ajax({
                        url: '/delete_networktraffic',
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
            }
            if (arr['obs_type'] == "process"){
                  ///submit to db : ajax post
            var sendData = JSON.stringify(arr, null, 2);
                     $.ajax({
                        url: '/delete_process',
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
            }
            if (arr['obs_type'] == "software"){
                  ///submit to db : ajax post
            var sendData = JSON.stringify(arr, null, 2);
                     $.ajax({
                        url: '/delete_software',
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
            }
            if (arr['obs_type'] == "url"){
                  ///submit to db : ajax post
            var sendData = JSON.stringify(arr, null, 2);
                     $.ajax({
                        url: '/delete_url',
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
            }
            if (arr['obs_type'] == "user-account"){
                  ///submit to db : ajax post
            var sendData = JSON.stringify(arr, null, 2);
                     $.ajax({
                        url: '/delete_useracc',
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
            }
            if (arr['obs_type'] == "windows-registry-key"){
                  ///submit to db : ajax post
            var sendData = JSON.stringify(arr, null, 2);
                     $.ajax({
                        url: '/delete_winregkey',
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
            }
            if (arr['obs_type'] == "x509-certificate"){
                  ///submit to db : ajax post
            var sendData = JSON.stringify(arr, null, 2);
                     $.ajax({
                        url: '/delete_x509',
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
            }



    });

});