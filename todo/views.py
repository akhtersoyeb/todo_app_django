from django.shortcuts import render

from .models import Category, Task

def index(request):
    category_list = Category.objects.all()
    task_list = Task.objects.all()
    
    context = {
        "category_list": category_list,
        "task_list": task_list
    }
    return render(request, 'todo/index.html', context)
