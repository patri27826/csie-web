from news.models import Post, Status

# all = Post.objects.all()
# for p in all:
#     post = Post.objects.get(id=p.id)
#     post.update_date = post.date
#     post.save()

all = Post.objects.filter(date__lte="2022-10-14")
normal = Status.objects.get(name = "一般")
important = Status.objects.get(name = "重要")

for p in all:
    post = Post.objects.get(id=p.id)
    if post.status == important:
        post.status = normal
    elif post.status == normal:
        post.status = important
        
    post.save()