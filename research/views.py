from django.shortcuts import render
from django.core.paginator import Paginator
# Create your views here.
from django.http import HttpResponse
from members.models import Member
from research.models import Areas, Centers, International
from news.models import Post
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def lab(request):
    members = Member.objects.all()
    context = {
        'members': members,
    }
    return render(request, 'research/laboratories.html', context)

@require_http_methods(["GET"])
def areas(request):
    areas = Areas.objects.translated('zh-hant').order_by('translations__date')
    context = {
        'areas': areas,
    }
    return render(request, 'research/areas.html', context)

@require_http_methods(["GET"])
def centers(request):
    info = Centers.objects.translated('zh-hant').order_by('translations__date')
    context = {
        'info': info,
    }
    return render(request, 'research/centers.html', context)

@require_http_methods(["GET"])
def international(request):
    info = International.objects.translated('zh-hant').order_by('translations__date')
    post = Post.objects.filter(type__name__contains="國際合作交流").distinct()
    paginator = Paginator(post, 10) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'info': info,
        'page_obj': page_obj,
    }
    return render(request, 'research/international.html', context)