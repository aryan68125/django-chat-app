from django.shortcuts import render,redirect
from common_app.common_messages import ErrorMessages
from django.http import HttpResponseBadRequest
# Create your views here.
def register_user_page(request):
    if not request.user.is_authenticated:
        return render(request,"auth_app/register_users.html")
    else:
        return redirect("render_home_page")
    
def verify_account_page(request,uid=None,token=None):
    if not request.user.is_authenticated:
        if not uid or not token:
            context = {"error":ErrorMessages["ACCOUNT_VERIFICATION_LINK_ERROR"].value}
            return render(request,"common_error_page/error_page.html",context)
        # save the uid and token in the sessions
        context = {
            "verification_uid": uid,
            "verification_token": token
        }
        return render(request,"auth_app/verify_account_page.html",context)
    else:
        return redirect("render_home_page")
    
def login_user_page(request):
    if not request.user.is_authenticated:
        return render(request,"auth_app/login_users.html")
    else:
        return redirect("render_home_page")
    