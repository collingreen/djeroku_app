from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

from tasks import fake_task
from models import TaskInfo


# public pages
def index(request):
    return render(request, 'djeroku_app/index.html')

def fivehundrederror(request):
    raise Exception('you asked for it')

def fivehundred(request):
    return render(request, '500.html')

def fourohfour(request):
    return render(request, '404.html')

def hello(request):
    name = 'name' in request.POST and request.POST['name'] or None
    email = 'email' in request.POST and request.POST['email'] or None
    return render(
            request,
            'djeroku_app/hello.html',
            {
                'name': name,
                'email': email
            }
        )

# admin pages

@staff_member_required
def count_tasks(request):
    return render(
            request,
            'djeroku_app/tasks.html',
            {
                'task_count': TaskInfo.objects.count(),
                'pending': TaskInfo.objects.filter(finished=False).count(),
            }
        )

@staff_member_required
def create_tasks(request):
    fake_task.apply_async()
    return render(
            request,
            'djeroku_app/tasks.html',
            {
                'created': True,
                'pending': TaskInfo.objects.filter(finished=False).count(),
                'task_count': TaskInfo.objects.count()
            }
        )
