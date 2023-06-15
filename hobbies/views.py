from django.shortcuts import render, redirect
from .models import Hobbie
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
# def hobbie_list(request):
#     return render(request, 'hobbies/hobbie_list.html')

# Create your views here.
@login_required(login_url= 'accounts:login')
def hobbie_list(request):
    current_user = request.user;
    hobbies = Hobbie.objects.filter(author=current_user).order_by("fecha")
    return render(request, 'hobbies/hobbie_list.html', {"hobbies": hobbies})

def hobbie_details(request, id):
    # return HttpResponse(slug)
    hobbie = Hobbie.objects.get(id=id)
    return render(request, 'hobbies/hobbie_detail.html', {'hobbie': hobbie})

@login_required(login_url= 'accounts:login')
def hobbie_create(request):
    if request.method == 'POST':
        form = forms.CreateHobbie(request.POST, request.FILES)
        if form.is_valid():
            # save hobbie to db
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
            return redirect('hobbies:list')
    else:
        form = forms.CreateHobbie()
    return render(request, 'hobbies/hobbie_create.html', {'form': form})