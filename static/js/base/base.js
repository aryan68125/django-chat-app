$(document).ready(function(){
    open_side_bar_menu_handler()
})
function open_side_bar_menu_handler(){
    $(document).on("click","#open_sidebar_menu",function(){
        console.log("Open side bar menu!")
    })
}