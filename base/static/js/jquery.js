// $(document).ready(function() {
//     var details = $(this).closest('.myBody').find('.details').text()
//     // console.log(details)
//     var details50 = details.subs(0, 50);
//     $('.details').html(details50 + '...')
// })

// $(document).ready(function() {
//     $("#delete").click(function(e) {
//         // alert("Do you want to delete?")
//         e.preventDefault();

//         // var product_name = $(this).closest('.product-info').find('.prod-name').val();

//         var message_id = $(this).closest('.msg').find('.message_id').val();
//         var message_user = $(this).closest('.msg').find('.message_user').val();
//         var token = $('input[name=csrfmiddlewaretoken]').val();

//         $.ajax({
//             method: 'POST',
//             url: 'delete-msg/',
//             data: {
//                 'message_id': message_id,
//                 'message_user': message_user,
//                 csrfmiddlewaretoken: token,
//             },
//             success: function(response) {
//                 location.reload(true);
//                 //window.location.reload(true);
//             }
//         });
//     });

// });