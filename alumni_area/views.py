from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
import mimetypes
from django.db.models import Q
from django.views.decorators.http import require_http_methods

# Create your views here.
@require_http_methods(["GET"])
def index(request):
    """View function for home page of site."""
 
    return render(request, 'alumni_area/index.html')