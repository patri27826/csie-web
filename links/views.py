from django.shortcuts import render

# Create your views here.
from links.models import Other, Alumni, TextInfo
from news.models import Post
from django.views.decorators.http import require_http_methods
from django.db.models import Q
from django.core.paginator import Paginator

@require_http_methods(["GET"])
def other(request):
    others = Other.objects.translated('zh-hant').order_by('translations__date')
    context = {
        'others': others,
    }
    return render(request, 'links/otherSystem.html', context)

@require_http_methods(["GET"])
def alumni(request):
    # alumni = Alumni.objects.translated('zh-hant').order_by('translations__date')
    post = Post.objects.filter(Q(type__name__contains="相關連結") & Q(type__name__contains="系友資訊")).distinct().order_by('-is_pin', '-update_date', '-date')
    paginator = Paginator(post, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        # 'alumni': alumni,
        'page_obj': page_obj,
    }
    return render(request, 'links/alumni.html', context)

@require_http_methods(["GET"])
def venue(request):
    info = TextInfo.objects.filter(Q(type__name__contains="場地租借"))
    post = Post.objects.filter(type__name__contains="場地租借").distinct()
    paginator = Paginator(post, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'info': info,
        'page_obj': page_obj,
    }
    return render(request, 'links/venue_hire.html', context)