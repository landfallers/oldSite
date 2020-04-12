number=int(input())
#コードから角度変換
def rgb_h(r,g,b):
    if max(r,g,b)==r:
        h=60*(g-b)/(255)
    if max(r,g,b)==g:
        h=60*(b-r)/255+120
    if max(r,g,b)==b:
        h=60*(r-g)/255+240
    h=h%360
    return h
#角度からrgb
def h_rgb(h):
    h=h%360
    if 0<=h and 60>=h:
        r=255
        g=(h/60)*255
        b=0
    if 60<=h and 120>=h:
        r=((120-h)/60)*255
        g=255
        b=0
    if 120<=h and 180>=h:
        r=0
        g=255
        b=((h-120)/60)*255
    if 180<=h and 240>=h:
        r=0
        g=((240-h)/60)*255
        b=255
    if 240<=h and 300>=h:
        r=((h-240)/60)*255
        g=0
        b=255
    if 300<=h and 360>=h:
        r=255
        g=0
        b=((360-h)/60)*255
    r1,g1,b1=round(r),round(g),round(b)
    return r1,g1,b1
import numpy as np
import random
color_list=[[255,0,0],[255,255,0],[0,255,0],[0,255,255],[0,0,255],[255,0,255],[255,255,255]]
from decimal import *
getcontext().prec = 5000

def det_h(gou,gakuin):
    num=Decimal(gou**2-1).sqrt()
    h=str(num-int(num))
    gou=int(h[gou]+h[gou+1]+h[gou+2])%120
    h=rgb_h(color_list[gakuin][0],color_list[gakuin][1],color_list[gakuin][2])
    x1=np.random.normal(h,15)
    if x1<0:
        x1+=360
    if x1>360:
        x1-=360
    x2=x1+120+gou
    if x2<0:
        x2+=360
    if x2>360:
        x2-=360
    ans1=list(h_rgb(x1))
    ans2=list(h_rgb(x2))
    return ans1+ans2
import csv
with open("Book1.csv", encoding="utf-8") as f:
    table = list(csv.reader(f))
del table[0]
from jinja2 import Template, Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('side_article.html.j2')
rendered=[]
for i in range(126):
    row = table[i]
    print(row[4])
    cs=det_h(int(row[4]),int(row[6]))
    print(cs)
    data = {
    "url":"https://landfaller.com/pdf/"+row[4]+"/"+row[3],
    "img":"none",
    "gakuin":row[5],
    "gousu":row[4]+"号",
    "title":row[1],
    "name":row[2],
    "概要":row[0],
    "c1":cs[0]-40,
    "c2":cs[1]-40,
    "c3":cs[2]-40,
    "c4":cs[3]-40,
    "c5":cs[4]-40,
    "c6":cs[5]-40
    }
    if True:
        rendered.append(template.render(data))
        print(i)
list=[56, 17, 40, 123, 11, 44, 82, 114, 68, 102, 109, 96, 63, 73, 53, 69, 55, 9, 122, 108, 57, 119, 89, 66, 111, 87, 75, 21, 24, 117, 91, 4, 84, 92, 50, 90, 116, 14, 101, 39, 60, 32, 10, 93, 88, 52, 99, 42, 118, 27, 86, 65, 77, 97, 110, 54, 106, 64, 43, 80, 15, 100, 46, 103, 78, 5, 16, 1, 35, 38, 37, 104, 41, 23, 121, 113, 95, 29, 58, 76, 0, 98, 33, 61, 79, 26, 105, 74, 112, 107, 12, 30, 13, 48, 7, 49, 8, 70, 59, 94, 22, 20, 19, 62, 67, 115, 47, 72, 71, 25, 51, 34, 36, 31, 81, 120, 3, 85, 18, 83, 2, 28, 45, 125, 6, 124]
with open("side_article.html",  'w',encoding="utf-8") as f:
    for i in range(number,number+80):
        u=list[i%125]
        f.write(rendered[u])
        f.write("\n")
print(number)
