from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import Todoform
from .models import Task
from django.views.generic import ListView, DetailView, UpdateView, DeleteView


# Create your views here.
def task(request):
    obj=Task.objects.all()
    if request.method=='POST':
        label=request.POST.get('label', '')
        priority=request.POST.get('priority', '')
        tdate=request.POST.get('tdate', '')

        task=Task(label=label, priority=priority, tdate=tdate)
        task.save()

    return render(request, 'index.html', {'ta': obj})

class Tasklist(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'ta'

class Taskdetail(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'

class Taskupdate(UpdateView):
    model = Task
    template_name = 'updates.html'
    context_object_name = 'task'
    fields = ('label', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('updates', kwargs={'pk':self.object.id})

class Taskdelete(DeleteView):
    model = Task
    template_name = 'deleter.html'
    success_url = reverse_lazy('todoapp:homes')

def delete(request, tid):
    if request.method == 'POST':
        delet = Task.objects.get(id=tid)
        delet.delete()
        return redirect('/')
    return render(request, 'delete.html')

def updatetask(request, id):
    task=Task.objects.get(id=id)
    f=Todoform(request.POST or None, instance=task)

    if f.is_valid():
        f.save()
        return redirect('/')

    return render(request, 'update.html', {'t':task, 'f':f})


