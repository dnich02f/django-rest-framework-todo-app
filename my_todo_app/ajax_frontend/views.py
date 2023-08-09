from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
@login_required
def my_list(request):
    """
        This view will render the html, where the ajax calls will be made
    """
    return render(request, 'ajax_frontend/list.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get("login")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            if request.GET.get('next', False):
                print(request.GET)
                return redirect(request.GET['next'])
            else:
                return redirect('ajax_frontend:my_list')
        else:
            messages.add_message(request, messages.WARNING, 'Invalid login')
    return render(request, 'ajax_frontend/login.html', {})


def logout(request):
    auth_logout(request)
    return redirect('ajax_frontend:login')
