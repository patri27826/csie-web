from django.shortcuts import render

from home.models import Carousel, Image, Link, ITNews, homeInfo, homeImage, externalLink, Visit
from news.models import Post, Type, Status
from django.views import generic
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def homepage(request, template='path/to/template'):
    """View function for home page of site."""
    carousels = Carousel.objects.all()
    itNews = ITNews.objects.all()
    info = homeInfo.objects.all()
    images = homeImage.objects.all()
    externallinks = externalLink.objects.all()

    normal = Post.objects.filter(type__name__contains="一般").distinct()[:5]
    admission = Post.objects.filter(type__name__contains="招生").distinct()[:5]
    awards = Post.objects.filter(type__name__contains="獲獎").distinct()[:5]

    links = Link.objects.all()

    visit_model=Visit.objects.get(pk=1)
    visit_model.times+=1
    visit_model.save()
    # items = Navbar.objects.values_list('links', flat=True).distinct()
    # links = []

    # for item in items:
    #     if item in url:
    #         links.append((item,url[item]))

    # if Navbar.objects.filter(links__name__contains="系所介紹"):
    #     links.append(("系所介紹",'info'))
    # if Navbar.objects.filter(links__name__contains="系所公告"):
    #     links.append(("系所公告",'posts'))
    # if Navbar.objects.filter(links__name__contains="師資陣容"):
    #     links.append(("師資陣容",'members'))

    
    # last_post = news.get_last_posts()

    context = {
        'carousels': carousels,
        'links': links,
        # 'items': items,
        'itNews': itNews[:4],
        'normal':normal,
        'admission':admission,
        'awards':awards,
        'info':info,
        'images':images,
        'externallinks':externallinks,
        'num_visit':visit_model.times,
        # 'url':url,
    }
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'home/homepage.html', context)

    