#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tb_login
import requests
import urllib
import re



def is_query_coupon_response_correct(json):
    check_key = "data"
    if check_key in json:
        return True
    return False


def get_title_by_product_share(d):
    r = re.match("【(.*?)】", d)
    if r:
        return r.group(1)
    else:
        return ''


# 从淘口令中提取商品关键字用于淘宝联盟精确搜索到此商品
'''
    tk_pwd = "【ASICS亚瑟士2019春夏男跑鞋缓冲耐磨运动鞋EXCITE 6 1011A616-200】https://m.tb.cn/h.e0JYzzj 点击链接，再选择浏览器咑閞；或復·制这段描述￥dPFgYZX6lNe￥后到👉淘♂寳♀👈"
    tk_pwd = '复制整段信息，打开👉手机天猫👈，即可查看此商品:【可省500元 vivo Z3手机vivoz3 z4限量版 vivoz3i z1 x9  vivox21 x21 vivox23 y93 voviz3手机官方网新品】(未安装App点这里：http://yukhj.com/s/opRgI?tm=b15ce5 )🔑喵口令🔑'
    tk_pwd = '【直营】Nike耐克 Tanjun 男子休闲运动鞋 812654 https://item.taobao.com/item.htm?ut_sk=1.WK1Ly22xn3MDAHR6GMQ8PRus_21380790_1556255070536.PanelQRCode.1&id=567270395710&sourceType=item&price=349&origin_price=499&suid=626F7BF4-3EE6-419A-A42C-950D054B7AB9&sm=5438ba'
    print(get_pwd_keyword(tk_pwd))
'''
def get_pwd_keyword(pwd):
    str = ''
    if re.match("复制整段信息", pwd):
        r = re.search(r"即可查看此商品:(.*?)\(未安装", pwd)
        if r:
            str = r.group(1)
            str = str.replace('【', '')
            str = str.replace('】', '')
    elif re.match("【直营】", pwd):
        r = re.search("(【直营】.*?)http", pwd)
        if r:
            str = r.group(1)
    elif re.match("【", pwd):
        r = re.search("【(.*?)】http", pwd)
        if r:
            str = r.group(1)
    return str


def is_tbk_pwd(text):
   k = get_pwd_keyword(text)
   if k:
       return True
   else:
       return False


def match_url(string):
    pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')  # 匹配模式
    url = re.findall(pattern, string)
    if url:
        return url[0]
    else:
        return ''

if __name__ == '__main__':
    tk_pwd = "【ASICS亚瑟士2019春夏男跑鞋缓冲耐磨运动鞋EXCITE 6 1011A616-200】https://m.tb.cn/h.e0JYzzj 点击链接，再选择浏览器咑閞；或復·制这段描述￥dPFgYZX6lNe￥后到👉淘♂寳♀👈"
    tk_pwd = '复制整段信息，打开👉手机天猫👈，即可查看此商品:【可省500元 vivo Z3手机vivoz3 z4限量版 vivoz3i z1 x9  vivox21 x21 vivox23 y93 voviz3手机官方网新品】(未安装App点这里：http://yukhj.com/s/opRgI?tm=b15ce5 )🔑喵口令🔑'
    tk_pwd = '【直营】Nike耐克 Tanjun 男子休闲运动鞋 812654 https://item.taobao.com/item.htm?ut_sk=1.WK1Ly22xn3MDAHR6GMQ8PRus_21380790_1556255070536.PanelQRCode.1&id=567270395710&sourceType=item&price=349&origin_price=499&suid=626F7BF4-3EE6-419A-A42C-950D054B7AB9&sm=5438ba'
    print(get_pwd_keyword(tk_pwd))