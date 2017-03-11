/**
 * Created by matt.larsen on 3/8/2017.
 */

/** referenced from https://simpleisbetterthancomplex.com/tutorial/2016/11/15/how-to-implement-a-crud-using-ajax-and-json.html **/

/* context_data refers to JSON object given through the organization_members.html template*/
$(function() {
    $(".js-add-member").click(function () {
        $.ajax({
            url: '/scheduler/organization/' + context_data.organization_id + '/add_member',
            type: 'get',
            dataType: 'json',
            beforeSend: function() {
                $("#modal-member").modal("show");
            },
            success: function(data){
                $("#modal-member .modal-content").html(data.html_form);
            }
        });
    });
});