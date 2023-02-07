# %%
from news.models import Post, Status, Type
from django.db.models import Q

type_old = {'1':'本系簡介/榮譽事蹟', 
        '2':'本系簡介/法規彙編', 
        '3':'本系簡介/場地租借', 
        '11':'學生事務/課程介紹', 
        '12':'學生事務/碩博士', 
        '13':'學生事務/大學部', 
        '14':'學生事務/畢業生', 
        '15':'', 
        '16':'學生事務/文件下載', 
        '17':'學生事務/國際合作交流', 
        '18':'學生事務/高中生', 
        '21':'工程認證 / 問卷系統', 
        '999':'一般資訊', 
        '998':'招生資訊', 
        '997':'演講資訊', 
        '996':'獲獎資訊', 
        '995':'獎助學金', 
        '994':'徵人資訊'}
type_new = ['簡介/榮譽事蹟',
            '簡介/法規彙編/大學部','簡介/法規彙編/研究所','簡介/法規彙編/教師',
            '簡介/法規彙編/課務','簡介/法規彙編/其他','簡介/法規彙編/獎學金',
            '學術研究/國際合作交流',
            '課程及修業/課程抵免','課程及修業/大學部','課程及修業/普渡雙聯組','課程及修業/資訊所',
            '課程及修業/醫資所','課程及修業/AI學程','課程及修業/產碩專班','課程及修業/在職專班',
            '學生事務/檔案下載/大學部','學生事務/檔案下載/研究所','學生事務/檔案下載/畢業生',
            '學生事務/檔案下載/教務','學生事務/檔案下載/其他',
            '招生專區/高中生','招生專區/大學部','招生專區/普渡雙聯組','招生專區/特殊選才','招生專區/資訊所',
            '招生專區/醫資所','招生專區/AI學程','招生專區/產碩專班','招生專區/在職專班',
            '公告/一般','公告/大學部招生','公告/研究所招生','公告/演講及活動','公告/獲獎','公告/獎助學金','公告/徵人',
            '相關連結/場地租借']

for value in type_new:
    if Type.objects.filter(name=value).exists() == False:
        Type.objects.create(name=value)
        print("create Type object: "+value)
# %%
posts = Post.objects.filter(type__name='本系簡介/榮譽事蹟')
for post in posts:
    post.type.add(Type.objects.get(name = '簡介/榮譽事蹟'))
# %%
posts = Post.objects.filter(Q(type__name='本系簡介/法規彙編') & (Q(title__contains='大學部')|Q(status__name__contains='大學部')))
for post in posts:
    post.type.add(Type.objects.get(name = '簡介/法規彙編/大學部'))
# %%
posts = Post.objects.filter(Q(type__name='本系簡介/法規彙編') & (Q(title__contains='研究')|Q(status__name__contains='碩士')))
for post in posts:
    post.type.add(Type.objects.get(name = '簡介/法規彙編/研究所'))
# %%
posts = Post.objects.filter(Q(type__name='本系簡介/法規彙編') & (Q(title__contains='博士')|Q(status__name__contains='博士')))
for post in posts:
    post.type.add(Type.objects.get(name = '簡介/法規彙編/研究所'))
# %%
posts = Post.objects.filter(Q(title__contains='抵免'))
for post in posts:
    post.type.add(Type.objects.get(name = '課程及修業/課程抵免'))
# %%
posts = Post.objects.filter(Q(type__name='學生事務/大學部'))
for post in posts:
    post.type.add(Type.objects.get(name = '課程及修業/大學部'))
# %%
posts = Post.objects.filter(Q(type__name='學生事務/碩博士') & (Q(title__contains='博士') | Q(title__contains='資訊工程') | Q(title__contains='資訊所')))
for post in posts:
    post.type.add(Type.objects.get(name = '課程及修業/資訊所'))
# %%
posts = Post.objects.filter(Q(type__name='學生事務/碩博士') & (Q(title__contains='醫學資訊') | Q(title__contains='醫資')))
for post in posts:
    post.type.add(Type.objects.get(name = '課程及修業/醫資所'))
# %%
posts = Post.objects.filter(Q(type__name='學生事務/碩博士') & (Q(title__contains='人工智慧科技碩士學位')))
for post in posts:
    post.type.add(Type.objects.get(name = '課程及修業/AI學程'))
# %%
posts = Post.objects.filter(Q(type__name='學生事務/碩博士') & (Q(title__contains='產業碩士') | Q(title__contains='產碩')))
for post in posts:
    post.type.add(Type.objects.get(name = '課程及修業/產碩專班'))
# %%
posts = Post.objects.filter(Q(type__name='學生事務/文件下載') & (Q(title__contains='大學部')|Q(status__name__contains='大學部')))
for post in posts:
    post.type.add(Type.objects.get(name = '學生事務/檔案下載/大學部'))
# %%
posts = Post.objects.filter(Q(type__name='學生事務/文件下載') & (Q(title__contains='研究所')|Q(status__name__contains='碩士')|Q(status__name__contains='博士')))
for post in posts:
    post.type.add(Type.objects.get(name = '學生事務/檔案下載/研究所'))
# %%
posts = Post.objects.filter(Q(type__name='學生事務/文件下載') & (Q(title__contains='教務')))
for post in posts:
    post.type.add(Type.objects.get(name = '學生事務/檔案下載/教務'))
# %%
posts = Post.objects.filter(Q(type__name='學生事務/文件下載') & (Q(title__contains='經費核銷')))
for post in posts:
    post.type.add(Type.objects.get(name = '學生事務/檔案下載/其他'))
# %%
posts = Post.objects.filter(Q(type__name='學生事務/高中生'))
for post in posts:
    post.type.add(Type.objects.get(name = '招生專區/高中生'))
# %%
posts = Post.objects.filter(Q(type__name='招生資訊')& (Q(title__contains='大學部')|Q(status__name__contains='大學部')))
for post in posts:
    post.type.add(Type.objects.get(name = '招生專區/大學部'))
# %%
posts = Post.objects.filter(Q(type__name='招生資訊')& (Q(title__contains='普渡')))
for post in posts:
    post.type.add(Type.objects.get(name = '招生專區/普渡雙聯組'))
# %%
posts = Post.objects.filter(Q(type__name='招生資訊')& (Q(title__contains='特殊選才')))
for post in posts:
    post.type.add(Type.objects.get(name = '招生專區/特殊選才'))
# %%
posts = Post.objects.filter(Q(type__name='招生資訊')& (Q(title__contains='資訊所')|Q(title__contains='資工所')|Q(title__contains='資訊工程所')|Q(status__name__contains='博士')|~Q(title__contains='多媒體')))
for post in posts:
    post.type.add(Type.objects.get(name = '招生專區/資訊所'))
# %%
posts = Post.objects.filter(Q(type__name='招生資訊')& (Q(title__contains='醫資所')|Q(title__contains='醫學資訊')))
for post in posts:
    post.type.add(Type.objects.get(name = '招生專區/醫資所'))
# %%
posts = Post.objects.filter(Q(type__name='招生資訊')& (Q(title__contains='AI學程')|Q(title__contains='人工智慧科技碩士學位')))
for post in posts:
    post.type.add(Type.objects.get(name = '招生專區/AI學程'))
# %%
posts = Post.objects.filter(Q(type__name='招生資訊')& (Q(title__contains='產碩')|Q(title__contains='產業碩士')))
for post in posts:
    post.type.add(Type.objects.get(name = '招生專區/產碩專班'))
# %%
posts = Post.objects.filter(Q(type__name='招生資訊')& (Q(title__contains='在職')))
for post in posts:
    post.type.add(Type.objects.get(name = '招生專區/在職專班'))
# %%
posts = Post.objects.filter(Q(type__name='學生事務/國際合作交流'))
for post in posts:
    post.type.add(Type.objects.get(name = '學術研究/國際合作交流'))
# %%
posts = Post.objects.filter(Q(type__name='一般資訊'))
for post in posts:
    post.type.add(Type.objects.get(name = '公告/一般'))
# %%
posts = Post.objects.filter(Q(type__name='演講資訊'))
for post in posts:
    post.type.add(Type.objects.get(name = '公告/演講及活動'))
# %%
posts = Post.objects.filter(Q(type__name='獲獎資訊'))
for post in posts:
    post.type.add(Type.objects.get(name = '公告/獲獎'))
# %%
posts = Post.objects.filter(Q(type__name='獎助學金'))
for post in posts:
    post.type.add(Type.objects.get(name = '公告/獎助學金'))
# %%
posts = Post.objects.filter(Q(type__name='徵人資訊'))
for post in posts:
    post.type.add(Type.objects.get(name = '公告/徵人'))