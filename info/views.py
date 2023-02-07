from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Info, TextInfo, Visiting
from news.models import Post, Type, Status
from django.db.models import Q
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator

@require_http_methods(["GET"])
def index(request):
    return render(request, 'info/index.html')

from django.views import generic

class InfoListView(generic.ListView):
    model = Info
    # def get_queryset(self) :
    #     return Info.objects.translated('zh-hant').order_by('translations__title')

@require_http_methods(["GET"])
def directions(request):
    info = TextInfo.objects.filter(Q(type__name__contains="教育目標"))

    context = {
        'info': info,
    }
    return render(request, 'info/directions.html', context)

@require_http_methods(["GET"])
def honor(request):
    info = TextInfo.objects.filter(Q(type__name__contains="榮譽事蹟"))
    post = Post.objects.filter(type__name__contains="榮譽事蹟").distinct()
    paginator = Paginator(post, 10) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'info': info,
        'page_obj': page_obj,
    }
    return render(request, 'info/honor.html', context)

@require_http_methods(["GET"])
def regulation(request):
    info1 = TextInfo.objects.filter(Q(type__name__contains="法規彙編") & Q(type__name__contains='大學部'))
    info2 = TextInfo.objects.filter(Q(type__name__contains="法規彙編") & Q(type__name__contains='研究所'))
    info3 = TextInfo.objects.filter(Q(type__name__contains="法規彙編") & Q(type__name__contains='教師'))
    info4 = TextInfo.objects.filter(Q(type__name__contains="法規彙編") & Q(type__name__contains='課務'))
    info5 = TextInfo.objects.filter(Q(type__name__contains="法規彙編") & Q(type__name__contains='其他'))
    info6 = TextInfo.objects.filter(Q(type__name__contains="法規彙編") & Q(type__name__contains='獎學金'))
    post1 = Post.objects.filter(Q(type__name__contains="法規彙編") & (Q(type__name__contains='大學部') | Q(status__name__contains='大學部'))).distinct()
    post2 = Post.objects.filter(Q(type__name__contains="法規彙編") & (Q(type__name__contains='研究所') | Q(status__name__contains='碩士') | Q(status__name__contains='博士'))).distinct()
    post3 = Post.objects.filter(Q(type__name__contains="法規彙編") & Q(type__name__contains='教師')).distinct()
    post4 = Post.objects.filter(Q(type__name__contains="法規彙編") & Q(type__name__contains='課務')).distinct()
    post5 = Post.objects.filter(Q(type__name__contains="法規彙編") & Q(type__name__contains='其他')).distinct()
    post6 = Post.objects.filter(Q(type__name__contains="法規彙編") & Q(type__name__contains='獎學金')).distinct()
    context = {
        'info1': info1,
        'info2': info2,
        'info3': info3,
        'info4': info4,
        'info5': info5,
        'info6': info6,
        'post1': post1,
        'post2': post2,
        'post3': post3,
        'post4': post4,
        'post5': post5,
        'post6': post6,
    }
    return render(request, 'info/regulation.html', context)

@require_http_methods(["GET"])
def visiting(request):

    info = Visiting.objects.translated('zh-hant').order_by('translations__date')
    context = {
        'info': info,
    }
    return render(request, 'info/visiting.html', context)

@require_http_methods(["GET"])
def equipment(request):
    info = TextInfo.objects.filter(Q(type__name__contains="設備介紹"))
    
    context = {
        'info': info,
    }
    return render(request, 'info/equipment.html', context)