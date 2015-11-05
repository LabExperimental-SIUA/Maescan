
$(document).ready(function(){

   $('body').on('click', '.photo' ,function(){
        var src = $(this).attr('src');
        var img = '<img src="' + src + '" class="img-responsive"/>';

        $('#photo-modal').on('shown.bs.modal', function(){
            $('#photo-modal .modal-body').html(img);
        });
        $('#photo-modal').on('hidden.bs.modal', function(){
            $('#photo-modal .modal-body').html('');
        });
       $('#photo-modal').modal();
   });

   $('body').on('click', '.capture-btn' ,function(){
        $.ajax({
            method: 'post',
            url: '/photo'
        }).done(function(response) {
            console.log(response);
            $('#photo1').attr( "src", "data:image/jpg;base64," + response.photo1.content);
            $('#photo2').attr( "src", "data:image/jpg;base64," + response.photo2.content);
        });
   });

    $('body').on('click', '#process-btn', function() {
        $.ajax({
            method: 'get',
            url: '/photo'
        }).done(function(response) {
            console.log(response);
            $('#photo1').attr( "src", "data:image/jpg;base64," + response.photo1.content);
            $('#photo2').attr( "src", "data:image/jpg;base64," + response.photo2.content);
        });
    });

})