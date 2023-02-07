# %%
#coding=UTF-8
import pandas as pd
from datetime import datetime
from news.models import Post, Status, Type
import pytz

taipei_timezone = pytz.timezone('Asia/Taipei')

df=pd.read_excel("output.xlsx")
df = df.reset_index()
df = df[:]

type_d = {'1':'本系簡介/榮譽事蹟', 
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
state_d = {'1':'一般', '2':'重要', '3':'博士', 
            '5':'大學部', '6':'碩士', '7':'碩士'}
# %%

for values in type_d:
    if Type.objects.filter(name=type_d[values]).exists() == False:
        Type.objects.create(name=type_d[values])
        print("create Type object: "+type_d[values])

for values in state_d:
    if Status.objects.filter(name=state_d[values]).exists() == False:
        Status.objects.create(name=state_d[values])
        print("create Status object: "+type_d[values])

# %%
for index, row in df.iterrows():
    print(type_d[str(row['type'])])
    print(state_d[str(row['state'])])
    print(row['title'][1:])
    print(row['content'][1:])
    # print(datetime.strptime(row['date'], ' %Y-%m-%d %H:%M:%S'))
    print(row['date'].to_pydatetime())
    date = taipei_timezone.localize(row['date'].to_pydatetime())
    temp = Post(title=row['title'][1:], content=row['content'], 
                title_en=row['title_en'][1:], content_en=row['content_en'], 
                status=Status.objects.get(name = state_d[str(row['state'])]), 
                date=date, link  =row['link'])
    temp.save()
    temp.type.add(Type.objects.get(name = type_d[str(row['type'])]))
    
# %%
