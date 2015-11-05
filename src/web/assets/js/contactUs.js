$(function(){
    $("#send-mail-btn").click(function(){
        var senderName = $("#form-user-name").val();
        var senderEmail = $("#form-user-email").val();
        var message = $("#form-user-message").val();

        $.ajax({
            method: "GET",
            url: "/mail",
            data: { name: senderName, email: senderEmail, message: message}
        }).done(function() {
            $("#form-user-name").val("");
            $("#form-user-email").val("");
            $("#form-user-message").val("");
            $("#sent_success").removeClass("hidden");
        }).fail(function() {
            alert("Todo mal");
        });

    });
});
