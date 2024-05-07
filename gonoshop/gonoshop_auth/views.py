from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import authenticate, login, logout

from gonoshop_auth.models import User
from .forms import UserRegistrationForm
from .forms import UserLoginForm


# Create your views here.
def login_view(request: HttpRequest) -> HttpResponse:
    tipo = 'login'
    form = UserLoginForm()

    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['email'], password=cd['password'])

            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('home:index')
                else:
                    return HttpResponse('Su cuenta esta suspendida')

    context = {
        'tipo': tipo,
        'form': form
    }
    return render(request, 'gonoshop_auth/authentication/template.html', context)


def register_view(request: HttpRequest) -> HttpResponse:
    tipo = "register"
    form = UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            cd: dict = form.cleaned_data
            user: User = form.save(commit=False)
            user.set_password(cd.get('password'))
            user.save()

            auth_result = authenticate(username=user.email, password=cd.get('password'))
            print(auth_result)
            if auth_result and auth_result.is_active:
                login(request, auth_result)
                return redirect('home:index')

    context = {
        'tipo': tipo,
        'form': form
    }
    return render(request, 'gonoshop_auth/authentication/template.html', context)


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('home:index')
