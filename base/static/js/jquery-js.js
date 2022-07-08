$(document).ready(function() {
    $("#join-event").click(function(e) {
        e.preventDefault();
        // var product_name = $(this).closest('.product-info').find('.prod-name').val();

        var event_id = $(this).closest('#event-box').find('#event').val();
        var user_id = $(this).closest('#event-box').find('#user').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: 'POST',
            url: '/add-event/',
            data: {
                'event_id': event_id,
                'user-id': user_id,
                csrfmiddlewaretoken: token,
            },
            success: function(response) {
                location.reload(true);
                console.log("Heloo")
                    //window.location.reload(true);
            }
        });
    });

});

$(document).ready(function() {
    $("#revoke-event").click(function(e) {
        // alert("Do you want to delete?")
        e.preventDefault();

        // var product_name = $(this).closest('.product-info').find('.prod-name').val();

        var event_id = $(this).closest('#event-box').find('#event').val();
        var user_id = $(this).closest('#event-box').find('#user').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: 'POST',
            url: '/revoke-event/',
            data: {
                'event_id': event_id,
                'user-id': user_id,
                csrfmiddlewaretoken: token,
            },
            success: function(response) {
                location.reload(true);
                //window.location.reload(true);
            }
        });
    });

});

$(document).ready(function() {
    $("#send").click(function(e) {
        e.preventDefault();
        var message = $(this).closest('#message-box').find('#message').val();
        var user_id = $(this).closest('#message-box').find('#user_id').val();
        var event_id = $(this).closest('#message-box').find('#event_id').val();

        var token = $('input[name=csrfmiddlewaretoken]').val();

        if (message) {
            $.fn.postData()
        } else {
            alert('Type message')
        }
        $.fn.postData = function() {
            $.ajax({
                method: 'POST',
                url: '/send-message/',
                data: {
                    'message': message,
                    'user_id': user_id,
                    'event_id': event_id,
                    csrfmiddlewaretoken: token,
                },
                success: function(response) {
                    location.reload(true);
                    // console.log("Sending...")
                    //window.location.reload(true);
                }
            });
        };
    });
});
$(document).ready(function() {
    $(".delete").click(function(e) {
        e.preventDefault();
        var msg_id = $(this).closest('.msg').find('#msg_id').val();
        var user_id = $(this).closest('.msg').find('#user_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: 'POST',
            url: '/delete-message/',
            data: {
                'msg_id': msg_id,
                'user_id': user_id,
                csrfmiddlewaretoken: token,
            },
            success: function(response) {
                location.reload(true);
            }
        });
    });
});