import csv
from news.models import Post, PostFile

with open('filename.csv', 'r', newline='') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        try:
            p = Post.objects.filter(title=row[0])[0]
            p.postfile_set.all().delete()
            print(f'刪除公告: {row[0]}')
        except:
            print(f'刪除錯誤！！{row}')

with open('filename.csv', 'r', newline='') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        try:
            p = Post.objects.filter(title=row[0])[0]
            if PostFile.objects.filter(file='post/files/'+row[1]).exists()==False:
                print(f'公告: {row[0]}\n檔案名稱: {row[1]}')
                PostFile.objects.create(post=p,file='post/files/'+row[1])
        except:
            print(f'錯誤！！{row}')
