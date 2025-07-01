$(document).ready(function(){
    login_user_button_handler()
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
    fetch(URL,{
        method:"POST",
        headers:{
            "Accept":"application/json",
            "Content-type":"application/json",
            "X-CSRFToken":getCookie("csrftoken")
        },
        body:JSON.stringify(data)
    }).then(response=>response.json())
    .then(data=>{
        console.log("data ===> ",data)
        if(data.status_code === 200){

        }
        else{

        }
    })
}
// GATHER DATA AND SEND DATA TO THE BACK-END ENDS