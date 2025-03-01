import traceback

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


def user_login(request):
    if request.method == "POST":
        response = {k: v[0] for k,v in dict(request.POST).items()}

        user = authenticate(username=response['email'], password=response['password'])

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, "E-mail or password incorrect.")

    return render(request,'core/login.html')


def user_logout(request):
    logout(request)
    return redirect('/login/')


@csrf_exempt
def sign_up(request):
    if request.method == 'POST':
        response = {k: v[0] for k, v in dict(request.POST).items()}

        try:
            check_if_username_exists = User.objects.filter(username=response['username'], is_active=True)
            check_if_email_exists = User.objects.filter(email=response['email'], is_active=True)

            if not check_if_username_exists and not check_if_email_exists:
                new_user = User.objects.create_user(
                    username=response['username'],
                    email=response['email'],
                    password=response['password'],
                )
                new_user.first_name = response['first_name']
                new_user.last_name = response['last_name']
                new_user.save()

                auth_user = authenticate(username=new_user.username, password=response['password'])

                if auth_user is not None:
                    return redirect("/login/")

                messages.error(request, "An error occurred. Please try again.")
            else:
                messages.error(request, f"{'Email' if check_if_email_exists else 'Username'} already exists. Please "
                                        f"try another.")
        except Exception as e:
            print(e)
            print(traceback.format_exc())

    return render(request, 'core/signup.html')
