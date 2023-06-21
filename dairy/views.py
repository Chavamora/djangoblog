from django.shortcuts import render, redirect
from .models import Dairy_Entry
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
# def dairy_entry_list(request):
#     return render(request, 'dairy/dairy_entry_list.html')

# Create your views here.
@login_required(login_url= 'accounts:login')
def dairy_entry_list(request):
    current_user = request.user
    dairy = Dairy_Entry.objects.filter(author=current_user).order_by("fecha")
    return render(request, 'dairy/dairy_entry_list.html', {"dairy": dairy})

def dairy_entry_details(request, id):
    # return HttpResponse(slug)
    dairy_entry = Dairy_Entry.objects.get(id=id)
    return render(request, 'dairy/dairy_entry_detail.html', {'dairy_entry': dairy_entry})

@login_required(login_url= 'accounts:login')
def dairy_entry_create(request):
    if request.method == 'POST':
        form = forms.CreateDairy_Entry(request.POST, request.FILES)
        if form.is_valid():
            # save dairy_entry to db
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
            return redirect('dairy:list')
    else:
        form = forms.CreateDairy_Entry()
    return render(request, 'dairy/dairy_entry_create.html', {'form': form})