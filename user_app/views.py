from django.shortcuts import render,redirect
# Create your views here.
def render_profile_page(request):
    if request.user.is_authenticated:
        return render(request,"user_app/user_profile_page.html")
    else:
        return redirect("login_user_page")
    
