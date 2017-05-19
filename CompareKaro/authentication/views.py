from django.shortcuts import render,redirect

from authentication.forms import UserForm
from authentication.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy,reverse
import datetime
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail


# Create your views here.


def create_profile(request):
    if(request.method == 'POST'):
        user_form = UserForm(request.POST)
        if(user_form.is_valid()):
            userid = user_form.cleaned_data["username"]
            first_name = user_form.cleaned_data["first_name"]
            last_name = user_form.cleaned_data["last_name"]
            email = user_form.cleaned_data["email"]
            password = user_form.cleaned_data["password"]

            user = User.objects.create_user(
                username = userid,
                email = email,
                password = password,
                first_name = first_name,
                last_name = last_name
            )
            user.is_active = True
            user.save()

            user = authenticate(username = userid, password = password)
            login(request, user)

            return redirect(reverse('index'))
    else:
        user_form = UserForm()
    return render(request,'authentication/registration/register.html',
        {'user_form' : user_form})

def log_out(request):
    if(request.user.is_authenticated):
        logout(request)
    return render(request, 'core/index.html')

def log_in(request):
    if(request.user.is_authenticated):
        return redirect(reverse('index'))
    else:
        if(request.method == 'POST'):
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect(reverse('index'))
        else:
            return render(request,'authentication/login.html')
