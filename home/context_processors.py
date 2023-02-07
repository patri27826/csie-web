from django.conf import settings
from django.shortcuts import render

from home.models import Carousel, Image, Link, ITNews, homeInfo, homeImage, externalLink

def navlinks(request):
    """View function for home page of site."""
    carousels = Carousel.objects.all() 
    links = Link.objects.all()
    url = {
        '系所公告': 'posts',

        '系所介紹': 'info',
        '榮譽事蹟': 'Honor',
        '法規彙編': 'Regulation',
        '交通資訊': 'Visiting',
        '場地租借': 'Venue',

        '課程介紹': 'CourseInfo',
        '大學部': 'Bachelor',
        '碩博士': 'Master_PhD',
        '產業碩士專班': 'Industrial',
        '畢業生': 'Graduated',
        '文件下載': 'Documents',
        '國際合作交流': 'International',

        '大學部招生': 'BachelorAdmission',
        '碩士招生': 'MasterAdmission',
        '博士招生': 'PhDAdmission',

        '師資陣容': 'members',
        '系辦成員': 'office_members',

        '實驗室': 'Lab',
        '研究群': 'Areas',
        '研究中心': 'Centers',

        '其他服務系統': 'Other',
        '成功大學': 'NCKU',
        '電資學院': 'EECS',
        '系友資訊': 'Alumni',
    }
    
    # items = Navbar.objects.values_list('links', flat=True).distinct()
    # links = []

    # for item in items:
    #     if item in url:
    #         links.append((item,url[item]))   

    # links = []

    # if Navbar.objects.filter(links__name__contains="本系簡介"):
    #     links.append(("本系簡介",'info'))
    # if Navbar.objects.filter(links__name__contains="系所公告"):
    #     links.append(("系所公告",'posts'))
    # if Navbar.objects.filter(links__name__contains="師資陣容"):
    #     links.append(("師資陣容",'members'))
    
    # last_post = news.get_last_posts()

    context = {
        'carousels': carousels,
        'links': links,
    }
    # Render the HTML template index.html with the data in the context variable
    return context