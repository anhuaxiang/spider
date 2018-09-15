# -*- coding:utf-8 -*-
import pymysql
import jieba
import csv
import emote
import sys
reload(sys)
sys.setdefaultencoding('utf8')
datas=[]
comment=[]
date=[]
feel=[]
ments=[]
config={'host':'127.0.0.1',
    'port':3306,
    'user':'root',
    'password':'1122334455',
    'database':'bdtb',
    'charset':'utf8'
}
con=pymysql.connect(**config)
cur=con.cursor()
cur.execute('use bdtb;')
with open('bdtb_searchresult_before.csv') as f:
    reader=csv.reader(f)
    for line in reader:
        data1=(line[0],line[2],line[4],line[6],u'贴吧')
        datas.append(data1)
try:
    cur.executemany("insert IGNORE into topic (t_id,t_title,t_url,t_reply,t_bbs) values(%s,%s,%s,%s,%s)",datas)
    con.commit()
except Exception as err:
    print(err)

with open("bdtb_commen_before.csv") as file:
    reader=csv.reader(file)
    for line in reader:
        comment.append(line[4].decode('utf-8'))
        data=(line[0],line[1],line[3],line[5])
        date.append(data)
for i in comment:
    if not i:
        i=str(1)
    feel1=emote.analysis(i)
    feel.append((feel1['good'],feel1['anger'],feel1['surprise'],feel1['sorrow'],feel1['fear'],feel1['evil'],feel1['happy']))
k=len(comment)
for i in range(0,k):
    ments.append(date[i]+feel[i])
with open ('beifen.csv','ab+') as beifengfile:
    write=csv.writer(beifengfile)
    for en in ments:
        write.writerow([en[0],en[1],en[2],en[3],en[4],en[5],en[6],en[7],en[8],en[9],en[10]])
try:
    cur.executemany("insert IGNORE into reply (r_t_id,r_id,r_p_id,r_time,r_good,r_angry,r_shock,r_dole,r_fear,r_evil,r_happy) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",ments)
    con.commit()
except Exception as err:
    print(err)
cur.close()
con.close()
