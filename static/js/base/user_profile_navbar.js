$(document).ready(function(){
    user_profile_page_btn_handler()
    handle_logout_button()
})
function user_profile_page_btn_handler() {
    $(document).on("click", "#user_profile_settings_btn", function (e) {
        e.stopPropagation()
        $("#profile_dropdown_menu").toggleClass("hidden")
    })

    // Close dropdown if user clicks outside
    $(document).on("click", function () {
        $("#profile_dropdown_menu").addClass("hidden")
    })
}

function handle_logout_button() {
    $(document).on("click", "#logout_button", function () {
        // Optionally make logout request here
        window.location.href = "{% url 'logout_user_page' %}"
    })
}