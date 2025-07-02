$(document).ready(function(){
    upload_profile_picture()
    add_or_update_user_profile_data()
    get_profile_data()
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

// GET DATA FROM THE BACK-END FOR THE UPDATE PROFILE DATA STARTS
function get_profile_data(){
    fetch(
        ProcessUserProfileData,{
            method:'GET',
            headers:{
                "X-CSRFtoken":getCookie("csrftoken"),
            }
        }
    ).then(response=>response.json())
    .then(data=>{
        if(data.status_code === 200){
            console.log(data.data)
            $("#user_name_profile_page").val(data.data.name)
            $("#user_phonenumber_profile_page").val(data.data.mobile_number)
            if (data.data.profile_picture_url){
                $("#profile_photo_preview").attr("src", data.data.profile_picture_url)
            }
        }
        else{
            error_alert(data.error)
        }
    })
}
// GET DATA FROM THE BACK-END FOR THE UPDATE PROFILE DATA ENDS