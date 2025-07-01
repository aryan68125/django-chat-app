$(document).ready(function(){
    add_or_update_profile_picture_data_in_profile_page_handler()
})

// ADD OR UPDATE PROFILE PICTURE DATA IN THE FORM STARTS
function add_or_update_profile_picture_data_in_profile_page_handler(){
    $(document).on("click","#select_profile_photo",function(){
        console.log("Select profile photo button clicked!")
        $("#profile_photo_input").click()
    })

    // Preview selected image
    $("#profile_photo_input").on("change",function(){
        const file = this.files[0]
        if(file){
            const reader = new FileReader()
            reader.onload = function(e){
                $("#profile_photo_preview").attr("src",e.target.result)
            }
            reader.readAsDataURL(file)
        }
    })
}
// ADD OR UPDATE PROFILE PICTURE DATA IN THE FORM ENDS