$(document).ready(function(){
    verify_account()
})
function verify_account(){
    if(verification_uid && verification_token){
        let data = {
            uid:verification_uid,
            token:verification_token
        }
        fetch(
            RegisterUser,
            {
                method:'PUT',
                headers:{
                    "Accept":"application/json",
                    "Content-Type":"application/json",
                    "X-CSRFToken":getCookie("csrftoken")
                },
                body:JSON.stringify(data)
            }
        ).then(response=>response.json())
        .then(data=>{
            console.log(data)
            setTimeout(() => {
                $("#verification_message").empty();
                if (data.status_code === 200) {
                    $("#verification_message").append("Your account is now active!");
                    setTimeout(() => {
                        window.location.href = login_page_url;
                    }, 2000);
                } else {
                    $("#verification_message").append(data.error);
                }
            }, 2000)
        })
    }
}