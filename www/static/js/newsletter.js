$("#newsletter-form").on("submit", (event) => {
    event.preventDefault();
    var email = $("#newsletter_email").val()
    $.ajax({
        type: "POST",
        url: newsletterUrl,
        data: $("#newsletter-form").serialize(),
        success: (data) => {
            if (data['response'] == "OK") {
                $("#newsletter_email").val("");
                $("#newsletter-success").attr("hidden", false);
                setTimeout(() => {
                    $("#newsletter-success").attr("hidden", true);
                }, 20000);
            }
        },
    });
})