$("#contact-form").on("submit", (event) => {
    event.preventDefault();
    $.ajax({
        type: "POST",
        url: contactUrl,
        data: $("#contact-form").serialize(),
        success: (data) => {
            if (data['response'] == "OK") {
                $("#contact-form")[0].reset();
                $("#contact-success").attr("hidden", false);
                setTimeout(() => {
                    $("#contact-success").attr("hidden", true);
                }, 20000);
            }
        },
    });
})