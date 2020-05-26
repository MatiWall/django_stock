import re

from django.conf import settings
from django.http import redirect
 
class loginRequiredMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwrgs):
        assert hasattr(request, 'user')
        
