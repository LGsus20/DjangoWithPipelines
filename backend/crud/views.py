from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import User

# Create your views here.
def home(request):
    return render(request, "home.html")

def users(request):
    items = User.objects.all()
    return render(request, "users.html", {"users": items})

def create_view(request):
    return render(request, "create_user.html")

def create_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if username and email and password:
            User.objects.create(username=username, 
                                email=email,
                                password=password)
            return redirect("Users")
    return render(request, "create_user.html")

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        user.delete()
        return redirect("Users")
    return render(request, "delete_confirmation.html", {"user": user})