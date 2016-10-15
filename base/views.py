from django.shortcuts import render
from auther.forms import UserRegistrationForm
from auther.forms import UserLoginForm


def home(request):
    registration_form = UserRegistrationForm()
    login_form = UserLoginForm()
    context = {
        'registration_form': registration_form,
        'login_form': login_form,
    }
    return render(request, "base/home.html", context)


def base_files(request, filename):
    location = "base/" + filename
    return render(request, location, {}, content_type="text/plain")
