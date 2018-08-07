$(function() {

    $('#submit_kcph').click(function() {
        $.ajax({
            url: '/killchain',
            data: $('#killchain').serialize(),
            type: 'POST',
            success: function(response) {

                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });

    });

    /* Enable URL function*/





});