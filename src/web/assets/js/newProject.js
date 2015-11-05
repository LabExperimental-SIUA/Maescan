var ready = function(){
    //$('#configuration-zoom').val(10);
    $('body').on("click","#new-project-create",function(){
        var p_name = $('#newproject-name').val();
        var p_description = $('#newproject-description').val();
        var zoom = $('#configuration-zoom').val();
        var p_language = $('#newproject-language').val();
        $.ajax({
            method: 'POST',
            url: '/project',
            data: {project_name: p_name, project_description: p_description, config:{zoom:zoom, language:p_language}}
        }).done(function() {
            window.location.href = '/scan';
            console.log("The project was successfully created.");
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