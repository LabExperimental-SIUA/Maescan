var ready = function(){

    $('body').on("click","#new-project-create",function(){
        var p_name = $('#newproject-name').val();
        var p_description = $('#newproject-description').val();
        var zoom = $('#configuration-zoom').val();
        var p_language = $('#newproject-language').val();
        $("#loading-cams").css("display", "block");
        $.ajax({
            method: 'POST',
            url: '/project',
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            data: JSON.stringify({postData: {project_name: p_name, project_description: p_description, config:{zoom:zoom, language:p_language}}})
        }).done(function(data) {
            if(data.status == 1){
                window.location.href = '/scan';
                $("#loading-cams").css("display", "none");
                console.log("The project was successfully created.");
            }else{
                $("#loading-cams").css("display", "none");
                $('#camera-error').modal('show');
            }
        });
    });

    $('body').on("click","#new-book-config-apply",function(){
        $('#configuration-modal').modal('hide');
    });

    $('body').on("click","#new-book-config-cancel",function(){
        $('#configuration-zoom').val(10);
    });


};

$(document).on('page:load', ready);
$(document).ready(ready);