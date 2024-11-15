from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from item.models import Category, Item


from .forms import SignupForm, LoginForm

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })



def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })


def user_login(request):
    

    if request.method == 'POST':
        form = LoginForm(request, data = request.POST) #login form needs extra request para

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('core:index')  # Replace with your home page URL
    else:
        form = LoginForm()

    return render(request, 'core/login.html', {
        'form': form
    })

def user_logout(request):
    logout(request)
    return redirect('core:index')