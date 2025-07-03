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
    $(document).on("click", "#logout_button_nav_bar", function () {
        // Optionally make logout request here
        fetch(
            LogoutUser,
            {
                method:'POST',
                headers:{
                    "X-CSRFToken":getCookie("csrftoken"),
                    "Accept":"application/json",
                }
            }
        ).then(response=>response.json())
        .then(data=>{
            if(data.status_code===200){
                success_alert(data.message,login_user_page)
            }
            else{
                error_alert(data.error)
            }
        })
    })
}