from django.shortcuts import render, redirect
from .models import Task, TaskList
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from . import forms

# tasklists

@login_required(login_url= 'accounts:login')
def taskList_list(request):
    
    current_user = request.user
    generalTasks = Task.objects.filter(id_lista=None, author=current_user, completed=False)
    generalCompletedTasks = Task.objects.filter(id_lista=None, author=current_user, completed=True)
    taskLists = TaskList.objects.filter(author=current_user).order_by("fecha_limite")

    return render(request, 'tasks/taskList_list.html', {"taskLists": taskLists, "generalTasks": generalTasks, "generalCompletedTasks": generalCompletedTasks})

def taskList_favorite(request, id):
    taskList = TaskList.objects.get(id=id)
    if request.method == 'POST':
        if(taskList.favorito):
            taskList.favorito = False
        else:
            taskList.favorito = True
        taskList.save()
       
        print(taskList.favorito) 
        return JsonResponse({'message': 'Entrada marcada como favorita correctamente.'})
    
def taskList_delete(request, id):
    taskList = TaskList.objects.get(id=id)
    if request.method == 'DELETE':
        taskList.delete()
 
        return JsonResponse({'message': 'Entrada eliminada correctamente.'})
    
def taskList_details(request, id):
    
    taskList = TaskList.objects.get(id=id)
    
    tasks = Task.objects.filter(id_lista = taskList.id)
    return render(request, 'tasks/taskList_details.html', {'taskList': taskList, 'tasks': tasks})

@login_required(login_url= 'accounts:login')
def taskList_create(request):
    if request.method == 'POST':
        form = forms.CreateTaskList(request.POST, request.FILES)
        if form.is_valid():
            # save taskList to db
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
            return redirect('tasks:tl_list')
    else:
        form = forms.CreateTaskList()
    return render(request, 'tasks/taskList_create.html', {'form': form})

# tasks
@login_required(login_url= 'accounts:login')
def task_list(request):
    favoritos = request.GET.get("favoritos", False)
    current_user = request.user
    tasks = Task.objects.filter(author=current_user).order_by("fecha_limite")

    if favoritos:
        tasks = Task.objects.filter(author=current_user, is_favorite=True)
    else:
        tasks = Task.objects.filter(author=current_user)
    return render(request, 'tasks/task_list.html', {"tasks": tasks})

def task_favorite(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        if(task.favorito):
            task.favorito = False
        else:
            task.favorito = True
        task.save()
       
        print(task.favorito) 
        return JsonResponse({'message': 'Entrada marcada como favorita correctamente.'})
    
def task_delete(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'DELETE':
        task.delete()
 
        return JsonResponse({'message': 'Entrada eliminada correctamente.'})
    
def task_details(request, id):
    task = Task.objects.get(id=id)
    return render(request, 'tasks/task_details.html', {'task': task})

@login_required(login_url= 'accounts:login')
def task_create(request, tlid=None):
    author = request.user
    if request.method == 'POST':
        if (tlid):
            current_list_id = TaskList.objects.get(id=tlid)
            form = forms.CreateTask(request.POST, author=request.user, current_list_id=current_list_id)
        else:
            form = forms.CreateTask(request.POST, author=request.user)

        if form.is_valid():
            # save task to db
            instance = form.save(commit = False)
            instance.author = request.user
            
            instance.save()
            print('lista:', form.data['id_lista'])
            if(form.data['id_lista']==''):
                return redirect('tasks:tl_list')
            else:
                return redirect('tasks:tl_details', form.data['id_lista'])
            
            
    else:
        if (tlid):
            current_list_id = TaskList.objects.get( id=tlid)
            form = forms.CreateTask(author=request.user, current_list_id=current_list_id)
        else:
            form = forms.CreateTask(author=request.user)
        
    return render(request, 'tasks/task_create.html', {'form': form, 'tlid': tlid})

def task_completed(request):
    if request.method == 'POST' :
        task_id = request.POST.get('task_id')
        

        # Lógica para marcar la tarea como completada en la base de datos

        task = Task.objects.get(id=task_id)
        task.completed = True
        task.save()
        updated_status = "completada"
        response_data = {'titulo': task.titulo}
        return JsonResponse({'success': True, 'status': updated_status})
    else:
        return JsonResponse({'error': 'Invalid request'})