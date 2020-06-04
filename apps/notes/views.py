from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect

from django.http import JsonResponse
from django.forms.models import model_to_dict

from django.custom_utils.utils import cleanFormData


from .forms import taskForm
from .models import task

import json
# Create your views here.


class home(TemplateView):
    template_name = 'notes/tasks.html'

    def get(self, request):
        form = taskForm()
        query = 'SELECT * FROM notes_task where user_id = %s'
        #tasks = task.objects.raw( query, [request.user.id])
        tasks = task.objects.filter(user = request.user)
    
        return render(request, self.template_name, {'form': form, 'tasks' : tasks})


    def post(self, request):
        
        
        data = cleanFormData(json.loads(request.body))
        form = taskForm(data = data)

        if form.is_valid():
            new_task = form.save(commit = False)
            new_task.user = request.user
            new_task.save()
            return JsonResponse({'tasks' : model_to_dict(new_task)})
        return JsonResponse({'tasks' : 'error'})




def taskCompleted(request):
    
    if request.is_ajax() and request.method == 'POST':
        completedTask = task.objects.get(id = json.loads(request.body))
        completedTask.delete()
    return JsonResponse({'task' : 'deleted'}, status = 200)