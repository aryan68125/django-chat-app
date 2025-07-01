$(document).ready(function(){
    register_user_button_handler()
})
// REGISTER BUTTON LOGIC STARTS
function register_user_button_handler(){
    $(document).on("click","#register_user",function(){
        gather_data_register_user()
    })
}
// REGISTER BUTTON LOGIC ENDS

// REGISTER USER FORM VALIDATION STARTS
function validate_email(email){
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}
function validate_password(password){
    return password.length >= 8;
}
// REGISTER USER FORM VALIDATION ENDS

// VALIDATION ERROR UI LOGIC STARTS
function show_error_message(message,field_id){
    $('#' + field_id + '_error').text(message).show();
}
function hide_error_message(field_id){
    $('#' + field_id + '_error').empty();
    $('#' + field_id + '_error').hide();
}
// VALIDATION ERROR UI LOGIC ENDS

// GATHER DATA AND THEN SEND DATA TO BACK-END STARTS
function gather_data_register_user(){
    let email = $('#email').val()
    let password = $('#password').val()
    let data = {
        "email":email,
        "password":password
    }
    if(!validate_email(email)){
        show_error_message("Invalid email format","email");
    }
    else{
        hide_error_message("email");
    }
    if(!validate_password(password)){
        show_error_message("Invalid password. Password must be at least 8 characters long","password");
    }
    else{
        hide_error_message("password");
    }
    send_data_register_user(data);
}
function send_data_register_user(data){
    fetch(RegisterUser,{
        method:"POST",
        headers:{
            "Accept":"application/json",
            "Content-Type":"application/json",
            "X-CSRFToken":getCookie("csrftoken")
        },
        body:JSON.stringify(data)
    }).then(response=>response.json())
    .then(data=>{
        console.log(data);
        if(data.status_code === 201){
            success_alert(data.message,login_user_page)
        }
        else{
            error_alert(data.error)
        }
    })
}
// GATHER DATA AND THEN SEND DATA TO BACK-END ENDS