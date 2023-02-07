from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from education.models import CourseInfo, TextInfo
from news.models import Post, Type, Status
from django.db.models import Q
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def courseInfo(request):
    info = CourseInfo.objects.all()
    post = Post.objects.filter(type__name__contains="課程介紹").distinct().order_by('-is_pin', '-update_date', '-date')
    paginator = Paginator(post, 10) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'info': info,
        'page_obj': page_obj
    }
    return render(request, 'education/course_info.html', context)

@require_http_methods(["GET"])
def credits(request):
    info = TextInfo.objects.filter(Q(type__name__contains="課程及修業") & Q(type__name__contains='課程抵免'))
    post = Post.objects.filter((Q(type__name__contains="學生事務") | Q(type__name__contains="課程及修業")) & Q(type__name__contains="課程抵免")).distinct().order_by('-is_pin', '-update_date', '-date')
    paginator = Paginator(post, 10) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'info': info,
        'page_obj': page_obj,
    }
    return render(request, 'education/credits.html', context)

@require_http_methods(["GET"])
def bachelor(request):
    info1 = TextInfo.objects.filter(Q(type__name__contains="課程及修業") & Q(type__name__contains='大學部') & Q(type__name__contains='課程介紹'))
    info2 = TextInfo.objects.filter(Q(type__name__contains="課程及修業") & Q(type__name__contains='大學部') & Q(type__name__contains='修業規定'))
    info3 = TextInfo.objects.filter(Q(type__name__contains="課程及修業") & Q(type__name__contains='大學部') & Q(type__name__contains='專題展'))
    info4 = TextInfo.objects.filter(Q(type__name__contains="課程及修業") & Q(type__name__contains='大學部') & Q(type__name__contains='畢業規定'))
    post = Post.objects.filter((Q(type__name__contains="學生事務") | Q(type__name__contains="課程及修業")) & Q(type__name__contains="大學部")).distinct().order_by('-is_pin', '-update_date', '-date')
    paginator = Paginator(post, 10) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'info1': info1,
        'info2': info2,
        'info3': info3,
        'info4': info4,
        'page_obj': page_obj
    }
    return render(request, 'education/bachelor.html', context)

@require_http_methods(["GET"])
def bs(request):
    info1 = TextInfo.objects.filter(Q(type__name__contains="課程及修業") & Q(type__name__contains='普渡雙聯組') & Q(type__name__contains='課程介紹'))
    info2 = TextInfo.objects.filter(Q(type__name__contains="課程及修業") & Q(type__name__contains='普渡雙聯組') & Q(type__name__contains='修業規定'))
    info3 = TextInfo.objects.filter(Q(type__name__contains="課程及修業") & Q(type__name__contains='普渡雙聯組') & Q(type__name__contains='專題展'))
    info4 = TextInfo.objects.filter(Q(type__name__contains="課程及修業") & Q(type__name__contains='普渡雙聯組') & Q(type__name__contains='畢業規定'))
    post = Post.objects.filter((Q(type__name__contains="學生事務") | Q(type__name__contains="課程及修業")) & Q(type__name__contains="普渡雙聯組")).distinct().order_by('-is_pin', '-update_date', '-date')
    paginator = Paginator(post, 10) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'info1': info1,
        'info2': info2,
        'info3': info3,
        'info4': info4,
        'page_obj': page_obj
    }
    return render(request, 'education/bs.html', context)

@require_http_methods(["GET"])
def instCSIE(request):
    info1 = TextInfo.objects.filter(Q(type__name__contains="課程及修業") & Q(type__name__contains='資訊所') & Q(type__name__contains='課程介紹'))
    info2 = TextInfo.objects.filter(Q(type__name__contains="課程及修業") & Q(type__name__contains='資訊所') & Q(type__name__contains='修業規定'))
    info3 = TextInfo.objects.filter(Q(type__name__contains="課程及修業") & Q(type__name__contains='資訊所') & Q(type__name__contains='專題展'))
    info4 = TextInfo.objects.filter(Q(type__name__contains="課程及修業") & Q(type__name__contains='資訊所') & Q(type__name__contains='畢業規定'))
    post = Post.objects.filter((Q(type__name__contains="學生事務") | Q(type__name__contains="課程及修業")) & Q(type__name__contains="資訊所")).distinct().order_by('-is_pin', '-update_date', '-date')
    paginator = Paginator(post, 10) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'info1': info1,
        'info2': info2,
        'info3': info3,
        'info4': info4,
        'page_obj': page_obj
    }
    return render(request, 'education/instCSIE.html', context)

@require_http_methods(["GET"])
def imi(request):
    info1 = TextInfo.objects.filter(Q(type__name__contains="課程及修業") & Q(type__name__contains='醫資所') & Q(type__name__contains='課程介紹'))
    info2 = TextInfo.objects.filter(Q(type__name__contains="課程及修業") & Q(type__name__contains='醫資所') & Q(type__name__contains='修業規定'))
    info3 = TextInfo.objects.filter(Q(type__name__contains="課程及修業") & Q(type__name__contains='醫資所') & Q(type__name__contains='專題展'))
    info4 = TextInfo.objects.filter(Q(type__name__contains="課程及修業") & Q(type__name__contains='醫資所') & Q(type__name__contains='畢業規定'))
    post = Post.objects.filter((Q(type__name__contains="學生事務") | Q(type__name__contains="課程及修業")) & Q(type__name__contains="醫資所")).distinct().order_by('-is_pin', '-update_date', '-date')
    paginator = Paginator(post, 10) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'info1': info1,
        'info2': info2,
        'info3': info3,
        'info4': info4,
        'page_obj': page_obj
    }
    return render(request, 'education/imi.html', context)

@require_http_methods(["GET"])
def ai(request):
    info1 = TextInfo.objects.filter(Q(type__name__contains="課程及修業") & Q(type__name__contains='AI學程') & Q(type__name__contains='課程介紹'))
    info2 = TextInfo.objects.filter(Q(type__name__contains="課程及修業") & Q(type__name__contains='AI學程') & Q(type__name__contains='修業規定'))
    info3 = TextInfo.objects.filter(Q(type__name__contains="課程及修業") & Q(type__name__contains='AI學程') & Q(type__name__contains='專題展'))
    info4 = TextInfo.objects.filter(Q(type__name__contains="課程及修業") & Q(type__name__contains='AI學程') & Q(type__name__contains='畢業規定'))
    post = Post.objects.filter((Q(type__name__contains="學生事務") | Q(type__name__contains="課程及修業")) & Q(type__name__contains="AI學程")).distinct().order_by('-is_pin', '-update_date', '-date')
    paginator = Paginator(post, 10) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'info1': info1,
        'info2': info2,
        'info3': info3,
        'info4': info4,
        'page_obj': page_obj
    }
    return render(request, 'education/ai.html', context)

@require_http_methods(["GET"])
def industrial(request):
    info1 = TextInfo.objects.filter(Q(type__name__contains="課程及修業") & Q(type__name__contains='產碩專班') & Q(type__name__contains='課程介紹'))
    info2 = TextInfo.objects.filter(Q(type__name__contains="課程及修業") & Q(type__name__contains='產碩專班') & Q(type__name__contains='修業規定'))
    info3 = TextInfo.objects.filter(Q(type__name__contains="課程及修業") & Q(type__name__contains='產碩專班') & Q(type__name__contains='專題展'))
    info4 = TextInfo.objects.filter(Q(type__name__contains="課程及修業") & Q(type__name__contains='產碩專班') & Q(type__name__contains='畢業規定'))
    post = Post.objects.filter((Q(type__name__contains="學生事務") | Q(type__name__contains="課程及修業")) & Q(type__name__contains="產碩專班")).distinct().order_by('-is_pin', '-update_date', '-date')
    paginator = Paginator(post, 10) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'info1': info1,
        'info2': info2,
        'info3': info3,
        'info4': info4,
        'page_obj': page_obj
    }
    return render(request, 'education/industrial.html', context)

@require_http_methods(["GET"])
def inService(request):
    info1 = TextInfo.objects.filter(Q(type__name__contains="課程及修業") & Q(type__name__contains='在職專班') & Q(type__name__contains='課程介紹'))
    info2 = TextInfo.objects.filter(Q(type__name__contains="課程及修業") & Q(type__name__contains='在職專班') & Q(type__name__contains='修業規定'))
    info3 = TextInfo.objects.filter(Q(type__name__contains="課程及修業") & Q(type__name__contains='在職專班') & Q(type__name__contains='專題展'))
    info4 = TextInfo.objects.filter(Q(type__name__contains="課程及修業") & Q(type__name__contains='在職專班') & Q(type__name__contains='畢業規定'))
    post = Post.objects.filter((Q(type__name__contains="學生事務") | Q(type__name__contains="課程及修業")) & Q(type__name__contains="在職專班")).distinct().order_by('-is_pin', '-update_date', '-date')
    paginator = Paginator(post, 10) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'info1': info1,
        'info2': info2,
        'info3': info3,
        'info4': info4,
        'page_obj': page_obj
    }
    return render(request, 'education/inService.html', context)

@require_http_methods(["GET"])
def documents(request):
    info1 = TextInfo.objects.filter(Q(type__name__contains="檔案下載") & Q(type__name__contains='大學部'))
    info2 = TextInfo.objects.filter(Q(type__name__contains="檔案下載") & Q(type__name__contains='研究所'))
    info3 = TextInfo.objects.filter(Q(type__name__contains="檔案下載") & Q(type__name__contains='畢業生'))
    info4 = TextInfo.objects.filter(Q(type__name__contains="檔案下載") & Q(type__name__contains='教務'))
    info5 = TextInfo.objects.filter(Q(type__name__contains="檔案下載") & Q(type__name__contains='其他'))
    post1 = Post.objects.filter(Q(type__name__contains="檔案下載") & Q(type__name__contains='大學部')).distinct().order_by('-is_pin', '-update_date', '-date')
    post2 = Post.objects.filter(Q(type__name__contains="檔案下載") & Q(type__name__contains='研究所')).distinct().order_by('-is_pin', '-update_date', '-date')
    post3 = Post.objects.filter(Q(type__name__contains="檔案下載") & Q(type__name__contains='畢業生')).distinct().order_by('-is_pin', '-update_date', '-date')
    post4 = Post.objects.filter(Q(type__name__contains="檔案下載") & Q(type__name__contains='教務')).distinct().order_by('-is_pin', '-update_date', '-date')
    post5 = Post.objects.filter(Q(type__name__contains="檔案下載") & Q(type__name__contains='其他')).distinct().order_by('-is_pin', '-update_date', '-date')

    context = {
        'info1': info1,
        'info2': info2,
        'info3': info3,
        'info4': info4,
        'info5': info5,
        'post1': post1,
        'post2': post2,
        'post3': post3,
        'post4': post4,
        'post5': post5,
    }
    return render(request, 'education/documents.html', context)
