from django.shortcuts import render,redirect

# Create your views here.
def register_user_page(request):
    if not request.user.is_authenticated:
        return render(request,"auth_app/register_users.html")
    else:
        return redirect("render_home_page")
    
def login_user_page(request):
    if not request.user.is_authenticated:
        return render(request,"auth_app/login_users.html")
    else:
        return redirect("render_home_page")
    