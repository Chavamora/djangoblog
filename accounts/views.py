from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from tasks.models import Task
from dairy.models import Dairy_Entry
from hobbies.models import Hobbie

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            #log the user in
            return redirect('accounts:homepage')
    elif request.method == 'GET':
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log the user in
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else: 
                return redirect('accounts:homepage')
            
    elif request.method == 'GET':
        form = AuthenticationForm()
    return render(request,'accounts/login.html', {'form': form} )

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    
@login_required(login_url= 'accounts:login')
def homepage_view (request):
    current_user = request.user
    hobbies = Hobbie.objects.filter(author=current_user)
    tasks = Task.objects.filter(author=current_user)
    dairy_entries = Dairy_Entry.objects.filter(author=current_user)
    return render(request, 'accounts/userhomepage.html', {
        'hobbies': hobbies,
        'tasks': tasks,
        'dairy_entries': dairy_entries,
        })

@login_required(login_url= 'accounts:login')
def profile_view (request):
    return render(request, 'accounts/profile.html', {'user': request.user})

