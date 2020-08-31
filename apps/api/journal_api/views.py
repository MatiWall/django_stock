from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import views
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework import status

from django.apps import apps
# Create your views here.

from apps.journal.models import portfolio, Journal, JournalAction, JournalTargets
from .serializers import portfolioSerializer, journalSerializer, journalActionSerializer, journalTargetsSerializer
from .forms import JournalActionForm, JournalTargetForm

class portfolioView(viewsets.ModelViewSet):
    
    serializer_class = portfolioSerializer

    def get_queryset(self):
        return portfolio.objects.filter(user = self.request.user)


    def partial_update(self, request, pk=None):
        pass


class journalView(viewsets.ModelViewSet):
    
    serializer_class = journalSerializer

    def get_queryset(self):
        return Journal.objects.filter(user = self.request.user)








class journalActionView(viewsets.ModelViewSet):
    
    template_name = 'journal-api/generalForm.html'
    serializer_class = journalActionSerializer
    


    def get_queryset(self):
        
        journal = self.request.query_params.get('journal', None)
        return JournalAction.objects.filter(user = self.request.user, journal = journal)

    

    def create(self, request):
        data = request.data
        if data:
            
            serializer = journalActionSerializer(data = data)
            if serializer.is_valid():
                
                serializer.save(user = request.user, journal_id = request.query_params.get('journal'))
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            form = JournalActionForm()
            return render(request, self.template_name, {'form': form})


    def update(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        instance = JournalAction.objects.get(id = pk )
        data = request.data
        if data:
            
            serializer = journalActionSerializer(instance, data = data, partial = True)
            if serializer.is_valid():
                
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            form = JournalActionForm(instance = instance)
            return render(request, self.template_name, {'form': form})

    
    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        instance = JournalAction.objects.get(id = pk )
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class journalTargetView(viewsets.ModelViewSet):
    
    template_name = 'journal-api/generalForm.html'
    serializer_class = journalTargetsSerializer
    


    def get_queryset(self):
        
        journal = self.request.query_params.get('journal', None)
        return JournalTargets.objects.filter(user = self.request.user, journal = journal)

    

    def create(self, request):
        data = request.data
        if data:
            serializer = self.serializer_class(data = data)
            if serializer.is_valid():
                
                serializer.save(user = request.user, journal_id = request.query_params.get('journal'))
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            form = JournalTargetForm()
            return render(request, self.template_name, {'form': form})


    def update(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        instance = JournalTargets.objects.get(id = pk )
        data = request.data
        if data:
            
            serializer = journalTargetsSerializer(instance, data = data, partial = True)
            if serializer.is_valid():
                
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            form = JournalTargetForm(instance = instance)
            return render(request, self.template_name, {'form': form})

    
    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        instance = JournalTargets.objects.get(id = pk )
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class portfolioFormView(views.APIView):
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = 'journal-api/portfolioForm.html'


    def get(self, request):
        serializer = portfolioSerializer()

        return Response({'serializer' : serializer})

    def post(self, request):
      
        serializer = portfolioSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
        
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class journalFormView(views.APIView):
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = 'journal-api/journalForm.html'


    def get(self, request):
        serializer = journalSerializer(context={'request': request})

        return Response({'serializer' : serializer})

    def post(self, request):
        serializer = journalSerializer(data = request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user = request.user)
        
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



