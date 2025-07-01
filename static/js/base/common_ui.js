function success_alert(message,redirection_url = false) {
    Swal.fire({
                position: "center",
                icon: "success",
                title: message,
                showConfirmButton: false,
                timer: 1500
            }).then(()=>{
                if (redirection_url){
                    window.location.href = redirection_url
                }
            })
}

function error_alert(error_message) {
    Swal.fire({
        icon: "error",
        text: error_message,
    });
}