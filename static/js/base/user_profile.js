$(document).ready(function(){
    user_profile_page_btn_handler()
})
function user_profile_page_btn_handler(){
    $(document).on("click","#user_profile_settings_btn",function(){
        console.log("Open logged in user profile page")
    })
}