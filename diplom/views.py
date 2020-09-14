from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages


def login_page(request):
    if request.user.is_authenticated:
        return redirect('main')
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'),
                            password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.add_message(request, messages.INFO,
                                 'Упс! Не подошло. Попробуй ещё!')
            return render(request, 'pages/login.html', {})
    else:
        return render(request, 'pages/login.html', {})


def user_logout(request):
    logout(request)
    return redirect('main')
