#モジュールの準備
import csv
import re
data=[]
 
#################################################################
#########################htmlファイルを開く#######################
#################################################################
#各研究室タグのhtml
html_path = 'base.html'
s = open(html_path)
html=s.read()

#先頭部分のhtml
start_html_path = 'start_of_base.html'
h_s = open(start_html_path)
start_html=h_s.read()

#終わり部分のhtml
end_html_path = 'end_of_base.html'
h_e = open(end_html_path)
end_html=h_e.read()
 
#出力するファイルを開く
#ここでは出力先のtxtファイルはtest.html
out_path = 'test.html'
out = open(out_path,'w')
 
#csvファイルを開く
#ここでは読み込むcsvファイルはsample.txt
data_path='test_list.csv'
f=open(data_path, encoding="utf-8")
reader = csv.reader(f)

######################################################################
################必要な部分だけを切り取ったdataリストを作る##############
######################################################################
for row in reader:
    if row[0] == "":
        break
    data.append(row[0:6])
data[0][0]=str(92)
######################################################################
##############################出力開始#################################
######################################################################
gousu=-1
item_num=2

#先頭部分のhtmlを出力
print(start_html,file=out)

for test in data:
    if gousu != test[0]:
        if int(test[0]) in [90,80,70,60,50,40,30,20,10]:
            print('</ul>',file=out)
            print('</div>', file=out)
            print('<div class="tab-pane fade" id="item'+str(item_num)+'" role="tabpanel" aria-labelledby="item'+str(item_num)+'-tab">', file=out)
            print('<ul class="tlist">',file=out)
            item_num += 1

        gousu = test[0]
        print("<h5>"+str(gousu)+"号</h5>", file=out)
    
    text=html
    text_mod = text.replace("title",test[4])
    text_mod = text_mod.replace("教授名",test[3])
    text_mod = text_mod.replace("パス",test[2])
    text_mod = text_mod.replace("号数",test[0])
    print(text_mod, file=out)

#最後の部分のhtmlを出力
print(end_html,file=out)