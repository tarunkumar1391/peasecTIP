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
                $('#sno_artifact').text(response.id);
                $('#mime_type_artifact').text(response.mime_type);
                $('#payload_bin_artifact').text(response.payload_bin);
                $('#url_artifact').text(response.hash_type);
                $('#hash_val_artifact').text(response.hash_value);
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
                $('#sno_as').text(response.id);
                $('#number_as').text(response.number);
                $('#name_as').text(response.name);
                $('#rir_as').text(response.rir);

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
                $('#sno_dir').text(response.id);
                $('#path_dir').text(response.path);
                $('#path_enc_dir').text(response.path_enc);
                $('#created_dir').text(response.created);
                $('#modified_dir').text(response.modified);
                $('#accessed_dir').text(response.accessed);
                $('#contains_refs_dir').text(response.contains_refs);

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
                $('#sno_dn').text(response.id);
                $('#value_dn').text(response.value);
                $('#resolves_to_refs_dn').text(response.resolves_to_refs);

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
                $('#sno_emaddr').text(response.id);
                $('#value_emaddr').text(response.value);
                $('#display_name_emaddr').text(response.display_name);
                $('#belongs_to_ref_emaddr').text(response.belongs_to_ref);

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
                $('#sno_emmsg').text(response.id);
                $('#is_multipart_emmsg').text(response.is_multipart);
                $('#date_emmsg').text(response.date);
                $('#content_type_emmsg').text(response.content_type);
                $('#from_ref_emmsg').text(response.from_ref);
                $('#sender_ref_emmsg').text(response.sender_ref);
                $('#to_refs_emmsg').text(response.to_refs);
                $('#cc_refs_emmsg').text(response.cc_refs);
                $('#bcc_refs_emmsg').text(response.bcc_refs);
                $('#subject_emmsg').text(response.subject);
                $('#received_lines_emmsg').text(response.received_lines);
                $('#additional_header_fields_emmsg').text(response.additional_header_fields);
                $('#body_emmsg').text(response.body);
                $('#raw_email_ref_emmsg').text(response.raw_email_ref);

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
                $('#sno_file').text(response.id);
                $('#extensions_file').text(response.extension);
                $('#hashes_file').text(response.hashes);
                $('#size_file').text(response.size);
                $('#name_file').text(response.name);
                $('#name_enc_file').text(response.name_enc);
                $('#magic_number_hex_file').text(response.magic_number_hex);
                $('#mime_type_file').text(response.mime_type);
                $('#created_file').text(response.created);
                $('#modified_file').text(response.modified);
                $('#accessed_file').text(response.accessed);
                $('#parent_directory_ref_file').text(response.parent_directory_ref);
                $('#is_encrypted_file').text(response.is_encrypted);
                $('#encryption_algorithm_file').text(response.encryption_algorithm);
                $('#decryption_key_file').text(response.decryption_key);
                $('#content_ref_file').text(response.content_ref);

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
                $('#sno_ipv4').text(response.id);
                $('#value_ipv4').text(response.value);
                $('#resolves_to_refs_ipv4').text(response.resolves_to_refs);
                $('#belongs_to_refs_ipv4').text(response.belongs_to_refs);

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
                $('#sno_ipv6').text(response.id);
                $('#value_ipv6').text(response.value);
                $('#resolves_to_refs_ipv6').text(response.resolves_to_refs);
                $('#belongs_to_refs_ipv6').text(response.belongs_to_refs);

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
                $('#sno_mac').text(response.id);
                $('#value_mac').text(response.value);

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
                $('#sno_nettraffic').text(response.id);
                $('#extensions_nettraffic').text(response.extensions);
                $('#start_nettraffic').text(response.start);
                $('#end_nettraffic').text(response.end);
                $('#is_active_nettraffic').text(response.is_active);
                $('#src_ref_nettraffic').text(response.src_ref);
                $('#dst_ref_nettraffic').text(response.dst_ref);
                $('#src_port_nettraffic').text(response.src_port);
                $('#dst_port_nettraffic').text(response.dst_port);
                $('#protocols_nettraffic').text(response.protocols);
                $('#src_byte_count_nettraffic').text(response.src_byte_count);
                $('#dst_byte_count_nettraffic').text(response.dst_byte_count);
                $('#src_packets_nettraffic').text(response.src_packets);
                $('#dst_packets_nettraffic').text(response.dst_packets);
                $('#ipfix_nettraffic').text(response.ipfix);
                $('#src_payload_ref_nettraffic').text(response.src_payload_ref);
                $('#dst_payload_ref_nettraffic').text(response.dst_payload_ref);
                $('#encapsulated_refs_nettraffic').text(response.encapsulated_refs);
                $('#encapsulated_by_ref_nettraffic').text(response.encapsulated_by_ref);

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
                $('#sno_process').text(response.id);
                $('#extensions_process').text(response.extensions);
                $('#is_hidden_process').text(response.is_hidden);
                $('#pid_process').text(response.pid);
                $('#name_process').text(response.name);
                $('#created_process').text(response.created);
                $('#cwd_process').text(response.cwd);
                $('#arguments_process').text(response.arguments);
                $('#command_line_process').text(response.command_line);
                $('#environment_variables_process').text(response.environment_variables);
                $('#opened_connection_refs_process').text(response.opened_connection_refs);
                $('#creator_user_ref_process').text(response.creator_user_ref);
                $('#binary_ref_process').text(response.binary_ref);
                $('#parent_ref_process').text(response.parent_ref);
                $('#child_refs_process').text(response.child_refs);
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
                $('#sno_software').text(response.id);
                $('#name_software').text(response.name);
                $('#cpe_software').text(response.cpe);
                $('#languages_software').text(response.languages);
                $('#vendor_software').text(response.vendor);
                $('#version_software').text(response.version);

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
                $('#sno_url').text(response.id);
                $('#value_url').text(response.value);

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
                $('#sno_useracc').text(response.id);
                $('#extensions_useracc').text(response.extensions);
                $('#user_id_useracc').text(response.user_id);
                $('#account_login_useracc').text(response.account_login);
                $('#account_type_useracc').text(response.account_type);
                $('#display_name_useracc').text(response.display_name);
                $('#is_service_account_useracc').text(response.is_service_account);
                $('#is_privileged_useracc').text(response.is_privileged);
                $('#can_escalate_privs_useracc').text(response.can_escalate_privs);
                $('#is_disabled_useracc').text(response.is_disabled);
                $('#account_created_useracc').text(response.account_created);
                $('#account_expires_useracc').text(response.account_expires);
                $('#password_last_changed_useracc').text(response.password_last_changed);
                $('#account_first_login_useracc').text(response.account_first_login);
                $('#account_last_login_useracc').text(response.account_last_login);

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
                $('#sno_winreg').text(response.id);
                $('#key_winreg').text(response.key);
                $('#modified_winreg').text(response.modified);
                $('#creator_user_ref_winreg').text(response.creator_user_ref);
                $('#number_of_subkeys_winreg').text(response.number_of_subkeys);
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
                $('#sno_x509').text(response.id);
                $('#is_self_signed_x509').text(response.is_self_signed);
                $('#hash_type_x509').text(response.hash_type);
                $('#hash_value_x509').text(response.hash_value);
                $('#version_x509').text(response.version);
                $('#serial_number_x509').text(response.serial_number);
                $('#signature_algorithm_x509').text(response.signature_algorithm);
                $('#issuer_x509').text(response.issuer);
                $('#validity_not_before_x509').text(response.validity_not_before);
                $('#validity_not_after_x509').text(response.validity_not_after);
                $('#subject_x509').text(response.subject);
                $('#subject_public_key_algorithm_x509').text(response.subject_public_key_algorithm);
                $('#subject_public_key_modulus_x509').text(response.subject_public_key_modulus);
                $('#subject_public_key_exponent_x509').text(response.subject_public_key_exponent);


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