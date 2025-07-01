from django.shortcuts import render

# Create your views here.
def register_user_page(request):
    if not request.user.is_authenticated:
        return render(request,'auth_app/register_users.html')
    

    