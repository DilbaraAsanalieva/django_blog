from django.contrib.auth import authenticate,logout, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def register_view(request):
    if request.method == "POST":
        data = request.POST
        first_name = data["first_name"]
        last_name = data["last_name"]
        username = data["username"]
        email = data["email"]
        password = data["password1"]
        password2 = data["password2"]
        if password2 != password:
            return render(request, 'signup.html')
        if not username:
            return render(request, 'signup.html')
        user = User.objects.create_user(
            username=username, password=password, first_name=first_name, last_name=last_name, email=email)
        return HttpResponse("Регистрация успешна прошла!")
    return render(request, 'signup.html')


def login_view(request):
    if request.method == "POST":
        data = request.POST
        user = authenticate(username=data["username"], password=data["password"])
        if user:
            login(request, user)
            return HttpResponse("Почуму так часто проподаешь?!")
        else:
            return render(request, "login.html")
    if request.method == "GET":
        return render(request, "login.html")

def logout_view(request):
    logout(request)
    return HttpResponse("Ты опять проподаешь!:(")