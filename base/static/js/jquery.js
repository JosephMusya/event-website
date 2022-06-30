// $(document).ready(function() {
//     var details = $(this).closest('.myBody').find('.details').text()
//     // console.log(details)
//     var details50 = details.subs(0, 50);
//     $('.details').html(details50 + '...')
// })

$(document).ready(function() {
    $("#join-event").click(function(e) {
        // alert("Do you want to delete?")
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