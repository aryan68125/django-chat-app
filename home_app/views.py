from django.shortcuts import render,redirect

# Create your views here.
def render_home_page(request):
    if request.user.is_authenticated:
        return render(request, "home_app/home_page.html")
    else:
        return redirect("login_user_page")