# %%
import csv, re, shlex
from bs4 import BeautifulSoup

with open('data',"r",encoding="utf-8") as f:
    lines = f.readlines()
    # print(lines)

# %%
def splitString(str):
    i = -1
    isQ = False
    lstStr = []
    for s in str:
        if s != ',' and s != "\'":
            if i == -1 or i < len(lstStr):
                lstStr.append(s)
                i = len(lstStr)
            else:
                lstStr[i-1] = lstStr[i-1] + s
         
        elif s == ',' and isQ == False:
            lstStr.append('')
            i = len(lstStr)
             
        elif s == "\'" and isQ == False:
            isQ = True
            continue
         
        elif s == "\'" and isQ == True:
            isQ = False
            continue
         
        elif s == ',' and isQ == True:
            lstStr[i-1] = lstStr[i-1] + s
         
         
    return lstStr

def parse(str):
    soup = BeautifulSoup(x[4])
    titles = soup.find_all("p")
    content = ""
    for title in titles:
        content += title.getText()
        content += "\n"

    return content
# %%
with open('output_utf8.csv', 'w', newline='') as csvfile:
    for line in lines:
        if line[0] != 'I':
            line = line[1:-3] #去除(),
            x = splitString(line)
            # x[4] = parse(x[4])
            x[4] = "".join(x[4].split("\\r\\n"))
            x[6] = "".join(x[6].split("\\r\\n"))
            print(x[0],x[1],x[2],x[3],x[4],x[8])
            writer = csv.writer(csvfile)
            writer.writerow([x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8][1:],x[11]])

# %%
