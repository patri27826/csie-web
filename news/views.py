from django.shortcuts import render

# Create your views here.
from .models import Post, Type, Status
from django.views import generic
from django.http import HttpResponse
import os
from django.db.models import Q
from django.views.decorators.http import require_http_methods
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

@require_http_methods(["POST"])
def index(request):
    """View function for home page of site."""
    posts = Post.objects.all()
    type = Type.objects.all()
    statu = Status.objects.all()

    context = {
        'posts':posts,
        'type':type,
        'statu':statu,
    }

    return render(request, 'news/index.html', context=context)

class globalsearch(generic.ListView):
    model = Post
    paginate_by = 10

    template_name = 'news/search.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context
    def get_queryset(self, **kwargs):
        keywords = self.request.GET.get('q')
        return Post.objects.filter(Q(title__icontains=keywords) | Q(content__icontains=keywords) | Q(date__icontains=keywords) | Q(type__name__icontains=keywords) | Q(title_en__icontains=keywords)).distinct()

class PostListView(generic.ListView):
    model = Post
    paginate_by = 10

class PostListView_1(generic.ListView):
    model = Post
    paginate_by = 10
    def get_queryset(self, **kwargs):
        return Post.objects.filter(type__name__contains="一般").distinct()

class PostListView_bachelorAdmission(generic.ListView):
    model = Post
    paginate_by = 10
    def get_queryset(self, **kwargs):
        return Post.objects.filter(type__name__contains="招生").filter(Q(type__name__contains="大學部") | Q(status__name__contains="大學部")).distinct()
class PostListView_masterAdmission(generic.ListView):
    model = Post
    paginate_by = 10
    def get_queryset(self, **kwargs):
        return Post.objects.filter(type__name__contains="招生").filter(Q(type__name__contains="研究所") | Q(type__name__contains="碩士") | Q(status__name__contains="碩士") | Q(type__name__contains="博士") | Q(status__name__contains="博士")).distinct()

class PostListView_3(generic.ListView):
    model = Post
    paginate_by = 10
    def get_queryset(self, **kwargs):
        return Post.objects.filter(type__name__contains="演講").distinct()
class PostListView_4(generic.ListView):
    model = Post
    paginate_by = 10
    def get_queryset(self, **kwargs):
        return Post.objects.filter(type__name__contains="獲獎").distinct()
class PostListView_5(generic.ListView):
    model = Post
    paginate_by = 10
    def get_queryset(self, **kwargs):
        return Post.objects.filter(type__name__contains="獎助學金").distinct()
class PostListView_6(generic.ListView):
    model = Post
    paginate_by = 10
    def get_queryset(self, **kwargs):
        return Post.objects.filter(type__name__contains="徵人").distinct()

class PostDetailView(generic.DetailView):
    model = Post
