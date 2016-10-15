from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect


# Create your views here.
def create_account(request):
    username = request.POST.get('email')
    password = request.POST.get('password')
    user = User.objects.create_user(username=username, password=password)
    user.save()
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            raise Http404("El usuario no esta activo")
    else:
        raise Http404("El usuario o la contraseña son incorrectos")


def log_user_in(request):
    username = request.POST['email']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            raise Http404("El usuario no esta activo")
    else:
        raise Http404("El usuario o la contraseña son incorrectos")


def log_user_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
