$(() => {
    $("#create").on("click", function () { 
        $('#one input, #one button, #remember-log').css("animation", "create 1s forwards");
        $('.via, .account').css({
            display: "none"
        });
        $(".account, .account a").css("cursor", "default");
        $("#two").css("animation", "created 1s forwards");
        $('body').scrollTop(0);
    });
    $("#back").on("click", function () { 
        $("#two").css("animation", "createback 1s reverse");
        setTimeout(() => {
            $('.via, .account').css({
                display: "inline"
            });
        }, 700);
        $(".account").css("cursor", "initial");
        $(".account a").css("cursor", "pointer");
        $('#one input, #one button, #remember-log').css("animation", "createdback 1s forwards");
    });
    $(document).on('change', '#image', function() {
        var fileName = $(this).val().split('\\').pop();
        $('label[for="image"]').attr('data-content', fileName);
    });
    $('input[name="sign-submit"]').on("click", function (e) {
        if ($('input[name="sign-password"]').val() !== $('input[name="sign-confirm"]').val()) {
            alert("password not matching");
            e.preventDefault();
        }
    });
});
