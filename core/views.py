from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def frontpage(request):
    return render(request, 'core/frontpage.html')

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            
            return redirect('frontpage')

    else:
        form = UserCreationForm()
        context = {
            'form': form
        }
    return render(request, 'core/signup.html', context)

def log_out(request):
    if request.method == "GET":
        logout(request)
        return redirect('frontpage')