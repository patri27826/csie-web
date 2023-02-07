from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from news.models import Post
from admission.models import TextInfo, Bachelor_AdmissionInfo, Master_PhD_AdmissionInfo
from django.db.models import Q
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator

@require_http_methods(["GET"])
def adm_senior(request):
    info = TextInfo.objects.filter(Q(type__name__contains="高中生"))
    post = Post.objects.filter(Q(type__name__contains="招生專區") & Q(type__name__contains="高中生")).distinct().order_by('-is_pin', '-update_date', '-date')
    paginator = Paginator(post, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'info': info,
        'page_obj': page_obj,
    }
    return render(request, 'admission/adm_senior.html', context)

@require_http_methods(["GET"])
def adm_bachelor(request):

    info = TextInfo.objects.filter(Q(type__name__contains="大學部"))
    post = Post.objects.filter(Q(type__name__contains="招生專區") & Q(type__name__contains="大學部")).distinct().order_by('-is_pin', '-update_date', '-date')
    paginator = Paginator(post, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'info': info,
        'page_obj': page_obj,
    }
    return render(request, 'admission/adm_bachelor.html', context)

@require_http_methods(["GET"])
def adm_bs(request):

    info = TextInfo.objects.filter(Q(type__name__contains="普渡雙聯組"))
    post = Post.objects.filter(Q(type__name__contains="招生專區") & Q(type__name__contains="普渡雙聯組")).distinct().order_by('-is_pin', '-update_date', '-date')
    paginator = Paginator(post, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'info': info,
        'page_obj': page_obj,
    }
    return render(request, 'admission/adm_bs.html', context)

@require_http_methods(["GET"])
def adm_talent(request):

    info = TextInfo.objects.filter(Q(type__name__contains="特殊選才"))
    post = Post.objects.filter(Q(type__name__contains="招生專區") & Q(type__name__contains="特殊選才")).distinct().order_by('-is_pin', '-update_date', '-date')
    paginator = Paginator(post, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'info': info,
        'page_obj': page_obj,
    }
    return render(request, 'admission/adm_talent.html', context)

@require_http_methods(["GET"])
def adm_CSIE(request):

    info = TextInfo.objects.filter(Q(type__name__contains="資訊所"))
    post = Post.objects.filter(Q(type__name__contains="招生專區") & Q(type__name__contains="資訊所")).distinct().order_by('-is_pin', '-update_date', '-date')
    paginator = Paginator(post, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'info': info,
        'page_obj': page_obj,
    }
    return render(request, 'admission/adm_CSIE.html', context)

@require_http_methods(["GET"])
def adm_imi(request):

    info = TextInfo.objects.filter(Q(type__name__contains="醫資所"))
    post = Post.objects.filter(Q(type__name__contains="招生專區") & Q(type__name__contains="醫資所")).distinct().order_by('-is_pin', '-update_date', '-date')
    paginator = Paginator(post, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'info': info,
        'page_obj': page_obj,
    }
    return render(request, 'admission/adm_imi.html', context)

@require_http_methods(["GET"])
def adm_ai(request):

    info = TextInfo.objects.filter(Q(type__name__contains="AI學程"))
    post = Post.objects.filter(Q(type__name__contains="招生專區") & Q(type__name__contains="AI學程")).distinct().order_by('-is_pin', '-update_date', '-date')
    paginator = Paginator(post, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'info': info,
        'page_obj': page_obj,
    }
    return render(request, 'admission/adm_ai.html', context)

@require_http_methods(["GET"])
def adm_industrial(request):

    info = TextInfo.objects.filter(Q(type__name__contains="產碩專班"))
    post = Post.objects.filter(Q(type__name__contains="招生專區") & Q(type__name__contains="產碩專班")).distinct().order_by('-is_pin', '-update_date', '-date')
    paginator = Paginator(post, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'info': info,
        'page_obj': page_obj,
    }
    return render(request, 'admission/adm_industrial.html', context)

@require_http_methods(["GET"])
def adm_inService(request):

    info = TextInfo.objects.filter(Q(type__name__contains="在職專班"))
    post = Post.objects.filter(Q(type__name__contains="招生專區") & Q(type__name__contains="在職專班")).distinct().order_by('-is_pin', '-update_date', '-date')
    paginator = Paginator(post, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'info': info,
        'page_obj': page_obj,
    }
    return render(request, 'admission/adm_inService.html', context)