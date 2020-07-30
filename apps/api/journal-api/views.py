from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import views
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework import status
# Create your views here.

from apps.journal.models import portfolio, journal
from .serializers import portfolioSerializer, journalSerializer


class portfolioView(viewsets.ModelViewSet):
    
    serializer_class = portfolioSerializer

    def get_queryset(self):
        return portfolio.objects.filter(user = self.request.user)


    def partial_update(self, request, pk=None):
        
        pass


class journalView(viewsets.ModelViewSet):
    
    serializer_class = journalSerializer

    def get_queryset(self):
        return journal.objects.filter(user = self.request.user)







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
        print('ran')
        print(request.data)
        serializer = journalSerializer(data = request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user = request.user)
        
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





