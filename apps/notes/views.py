from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect

from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
from django.db import connection

from django.custom_utils.utils import cleanFormData, dictFetchAll


from .forms import taskForm
from .models import task, stickyNote, treeItem

import json
# Create your views here.


class home(TemplateView):
    template_name = 'notes/tasks.html'

    def get(self, request):
        form = taskForm()
        query = 'SELECT * FROM notes_task where user_id = %s'
        #tasks = task.objects.raw( query, [request.user.id])
        tasks = task.objects.filter(user = request.user)
    
        return render(request, self.template_name, {'form': form, 'tasks' : tasks, 'genres': treeItem.objects.all()})


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



def saveStickyNotes(request):
    
    if request.method == 'POST' and request.is_ajax():
        data = json.loads(request.body) 
        print(data)
        with connection.cursor() as cursor:
            query = '''
                INSERT INTO notes_stickyNote (notes, user_id) VALUES (%s, %s)
                ON CONFLICT (user_id) DO UPDATE   
                SET notes = excluded.notes
            '''
            cursor.execute(query, [json.dumps(data), request.user.id])
        
        return HttpResponse('')



def getStickyNotes(request):
    
    if request.method == 'GET' and request.is_ajax():

        with connection.cursor() as cursor:
            query = '''
                SELECT notes FROM notes_stickyNote WHERE user_id = %s
            '''
            cursor.execute(query, [request.user.id])
            notes = cursor.fetchall()
            print(notes)
            #notes = dictFetchAll(cursor)
        
    
    return JsonResponse({'data' : notes[0][0]})





