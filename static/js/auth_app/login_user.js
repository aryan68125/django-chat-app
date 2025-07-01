$(document).ready(function(){
    login_user_button_handler()
    redirect_to_register_page_handler()
    redirect_to_forgot_password_page_handler()
})

// LOGIN USER BUTTON HANDLER STARTS
function login_user_button_handler(){
    $(document).on("click","#login_user",function(){
        gather_login_data()
    })
}
// LOGIN USER BUTTON HANDLER ENDS

// GATHER DATA AND SEND DATA TO THE BACK-END STARTS
function gather_login_data(){
    let email = $("#email_login").val()
    let password = $("#password_login").val()
    let data = {
        "email":email,
        "password":password
    }
    send_login_data(data)
}
function send_login_data(data){
    console.log("incoming login data ===> ",data)
    fetch(LoginUser,{
        method:"POST",
        headers:{
            "Accept":"application/json",
            "Content-type":"application/json",
            "X-CSRFToken":getCookie("csrftoken")
        },
        body:JSON.stringify(data)
    }).then(response=>response.json())
    .then(data=>{
        console.log("login response data ===> ",data)
        if(data.status_code === 200){
            success_alert(data.message,render_home_page)
        }
        else{
            error_alert(data.error)
        }
    })
}
// GATHER DATA AND SEND DATA TO THE BACK-END ENDS


// REDIRECTION LOGIC STARTS
function redirect_to_register_page_handler(){
    $(document).on("click","#redirect_to_register_page",function(){
        window.location.href = register_user_page
    })
} 
function redirect_to_forgot_password_page_handler(){
    $(document).on("click","#redirect_to_register_page",function(){
        // window.location.href = register_user_page
    })
}
// REDIRECTION LOGIC ENDS 