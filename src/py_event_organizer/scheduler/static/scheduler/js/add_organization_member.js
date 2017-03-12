/**
 * Created by matt.larsen on 3/8/2017.
 */

/** referenced from https://simpleisbetterthancomplex.com/tutorial/2016/11/15/how-to-implement-a-crud-using-ajax-and-json.html **/

/* context_data refers to JSON object given through the organization_members.html template*/
$(function() {


    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function() {
                $("#modal-member").modal("show");
            },
            success: function(data){
                $("#modal-member .modal-content").html(data.html_form);
            }
        });
    };

    var saveForm = function () {
        var form = $(this);
        // debugger;
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data){
                if(data.form_is_valid){
                    $("#memberships_table tbody").html(data.html_member_list);
                    $("#modal-member").modal("hide");
                }
                else {
                    $("#modal-member .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };

    //add member to organization
    $(".js-add-member").click(loadForm);
    $("#modal-member").on("submit", ".js-add-member-form", saveForm);

});



