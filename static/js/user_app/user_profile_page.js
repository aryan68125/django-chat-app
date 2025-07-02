$(document).ready(function(){
    upload_profile_picture()
    add_or_update_user_profile_data()
})

// ADD OR UPDATE PROFILE PICTURE DATA IN THE FORM STARTS
function upload_profile_picture(){
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

// ADD OR UPDATE USER PROFILE DATA IN THE FORM STARTS
function add_or_update_user_profile_data(){
    $(document).on("click","#update_profile_button",function(){
        // Prepare data to send
        let user_name_profile_page = $("#user_name_profile_page").val()
        let user_phonenumber_profile_page = $("#user_phonenumber_profile_page").val()
        let file = $("#profile_photo_input")[0].files[0]
        let formData = new FormData()
        formData.append("name",user_name_profile_page);
        formData.append("phonenumber",user_phonenumber_profile_page);
        if (file){
            formData.append("profile_photo",file);
        }
        // send the prepared data to the server
        fetch(
            ProcessUserProfileData,
            {
                method:'POST',
                headers:{
                    "X-CSRFToken":getCookie("csrftoken"),
                },
                body:formData
            }
        ).then(response=>response.json())
        .then(data=>{
            console.log(data)
            if(data.status_code === 200){
                success_alert(data.message,window.location.href)
            }
            else{
                error_alert(data.error)
            }
        })

    })
}
// ADD OR UPDATE USER PROFILE DATA IN THE FORM ENDS