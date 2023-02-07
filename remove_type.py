from news.models import Post, Type
from django.db.models import Q

p1 = Post.objects.filter(Q(type__name__contains="招生專區") & Q(type__name__contains="資訊所") & Q(title__contains='產業碩士'))
p2 = Post.objects.filter(Q(type__name__contains="招生專區") & Q(type__name__contains="資訊所") & Q(title__contains='甄選入學'))
p3 = Post.objects.filter(Q(type__name__contains="招生專區") & Q(type__name__contains="資訊所") & Q(title__contains='個人申請'))
p4 = Post.objects.filter(Q(type__name__contains="招生專區") & Q(type__name__contains="資訊所") & Q(title__contains='在職專班'))
# p5 = Post.objects.filter(Q(type__name__contains="招生專區") & Q(type__name__contains="資訊所") & Q(title__contains='特殊選才'))
# p6 = Post.objects.filter(Q(type__name__contains="招生專區") & Q(type__name__contains="資訊所") & Q(title__contains='人工智慧碩士學位學程'))
t1 = Type.objects.get(name='招生專區/資訊所')

for p in p1:
    post = Post.objects.get(id=p.id)
    post.type.remove(t1)
    post.save()

for p in p2:
    post = Post.objects.get(id=p.id)
    post.type.remove(t1)
    post.save()

for p in p3:
    post = Post.objects.get(id=p.id)
    post.type.remove(t1)
    post.save()

for p in p4:
    post = Post.objects.get(id=p.id)
    post.type.remove(t1)
    post.save()

# for p in p5:
#     post = Post.objects.get(id=p.id)
#     post.type.remove(t1)
#     post.save()

# for p in p6:
#     post = Post.objects.get(id=p.id)
#     post.type.remove(t1)
#     post.save()