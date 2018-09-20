import requests
import re
from PIL import Image
from lxml import etree

cookie = {}
cookie_str = 'SINAGLOBAL=4642793730418.606.1532785072941; UOR=,,timi.qq.com; _s_tentry=-; Apache=8793788839015.575.1537176532013; ULV=1537176532955:7:5:2:8793788839015.575.1537176532013:1537081246956; login_sid_t=f39a6494cc7b8e7945b2c2946f938f90; cross_origin_proto=SSL; YF-Ugrow-G0=9642b0b34b4c0d569ed7a372f8823a8e; YF-V5-G0=c998e7c570da2f8537944063e27af755; wb_view_log=1536*8641.25; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWvxusCz7ky-S.UiHje9fF95JpX5K2hUgL.Fo-ceo2Neh.0S0n2dJLoIEXLxK-LBo5L12qLxKnLBo2L1hqLxKnLBo2L1hqLxK-LB-BLBKqLxK.L1K-LB.qt; ALF=1568724812; SSOLoginState=1537188812; SCF=AhizZKkJEtkKlchDpJnhUTezK__1xPPwKIiVvyO1S4_0XDNUuBS2JG9oGdvQb0YaMv5aIIhvZXriPfA5NyGNmkg.; SUB=_2A252m9OdDeRhGeNI6VMW8CfPzDSIHXVV0UJVrDV8PUNbmtBeLUHykW9NSIH50iWCjfpeQB145nO2zytXfdsrAGwy; SUHB=04Wu0DPVk7XkxQ; un=18301605620; wvr=6; YF-Page-G0=3d55e26bde550ac7b0d32a2ad7d6fa53; wb_view_log_5621709378=1536*8641.25'
for line in cookie_str.split(';'):
    name, value = line.strip().split('=', 1)
cookie[name] = value
headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Host': 'weibo.com',
    'Origin': 'https://weibo.com/login',
    'Referer': 'https://weibo.com/',
}
s = requests.session()
result = s.get('https://weibo.com/', headers=headers, cookies=cookie)
result = requests.get('https://weibo.com/', headers=headers, cookies=cookie)
print(result)
result.encoding = 'utf-8'
print(result.text)