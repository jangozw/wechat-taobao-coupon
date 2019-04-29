#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tb_login
import requests
import urllib
from tbk_api import tbk_helper
from tbk_api.TbkMaterialOptional import TbkMaterialOptional
from tbk_api.TbkPwdCreate import TbkPwdCreate
import re


def get_new_pwd(pwd):
    coupon = parse_coupon(pwd)
    if not coupon:
        return '该商品没有推广优惠,您可以更换其它商品查询优惠~'
    key = tbk_helper.get_pwd_keyword(pwd)
    t = TbkMaterialOptional()
    trans = t.send(key).first_item()
    coupon['url'] = trans['url']
    p = TbkPwdCreate()
    new_pwd = p.send(coupon['pictUrl'], key, coupon['url']).get_pwd()
    share = new_pwd_str(coupon, key, new_pwd)
    return share


def new_pwd_str(coupon, title, new_pwd):
    str = "%s \n现价：%s元\n返利： %s元\n" %(title, coupon['zkPrice'], coupon['tkCommFee'])
    if coupon['couponInfo']:
        str = str + "优惠活动: %s\n" %(coupon['couponInfo'])
        if coupon['couponAmount']:
            str = str+"优惠金额：%s元\n" %(coupon['couponAmount'])
    str = str + "到手价: %s\n" % (coupon['zkPrice'] - coupon['couponAmount'] - coupon['tkCommFee'])
    str = str + "店铺: %s\n" % (coupon['nick'])
    str = str + "復|制这段描述 %s 后到👉淘♂寳♀👈 \n" % (new_pwd)
    str = str + "复制这个口令，尽快下单才能返现/:rose/:rose/:rose"
    return str


# 解析出优惠
def parse_coupon(tk_pwd):
    cookies = tb_login.get_cookies(False)
    keyword = tbk_helper.get_pwd_keyword(tk_pwd)
    coupon_info = get_coupon_detail(cookies, keyword)
    print("优惠信息如下: ", coupon_info)
    return coupon_info


def get_coupon_detail(cookies, keyword):
    q = urllib.parse.quote(keyword)
    url = "https://pub.alimama.com/items/search.json?q="+q
    json = requests.get(url, cookies=cookies).json()
    item = get_tbk_item(json)
    if not item:
        return ''
    return parse_coupon_info(item)


def get_tbk_item(json):
    k = 'data'
    if k in json:
        if len(json['data']['pageList']) == 1:
            return json['data']['pageList'][0]
    return False


def parse_coupon_info(item):
    info = {}
    # 商品地址
    info["auctionUrl"] = item["auctionUrl"]
    # 图片
    info["pictUrl"] = 'https:'+item["pictUrl"]
    # 售价
    info["zkPrice"] = item["zkPrice"]
    # 优惠券金额
    info["couponAmount"] = item["couponAmount"]
    # 店铺
    info["nick"] = item["nick"]
    # 原价格
    info["reservePrice"] = item["reservePrice"]
    # 佣金比率 0.33
    info["tkRate"] = item["tkRate"]
    # 佣金 元  23.21
    info["tkCommFee"] = item["tkCommFee"]
    # 满199元减10元
    info['couponInfo'] = item['couponInfo']
    # 优惠券有效 2019-04-26
    info['couponEffectiveStartTime'] = item['couponEffectiveStartTime']
    # 2019-04-27
    info['couponEffectiveEndTime'] = item['couponEffectiveEndTime']
    # 优惠券启用门槛的消费金额
    info['couponStartFee'] = item['couponStartFee']
    # 优惠券总数量
    info['couponTotalCount'] = item['couponTotalCount']
    # 优惠券剩余数量
    info['couponLeftCount'] = item['couponLeftCount']
    return info






if __name__ == '__main__':
    pwd = '【直营】Nike耐克 Tanjun 男子休闲运动鞋 812654 https://item.taobao.com/item.htm?ut_sk=1.WK1Ly22xn3MDAHR6GMQ8PRus_21380790_1556255070536.PanelQRCode.1&id=567270395710&sourceType=item&price=349&origin_price=499&suid=626F7BF4-3EE6-419A-A42C-950D054B7AB9&sm=5438ba'
    r = re.search(r'【(.*?)】', pwd)
    print(r.group(1))


    # print(tbk_helper.get_pwd_keyword(pwd))
    # print(get_new_pwd(pwd))








'''
{
auctionId: 567270395710
auctionTag: "130 385 587 907 1163 1478 1483 2049 2059 2178 2562 3394 3459 3974 4166 4491 4550 4555 6603 7046 8199 8454 11083 11339 11531 13186 17739 22977 28353 28802 37569 40897 49218 52737 66241 67521 68930 69249 70273 71682 82306 82369 83202 96257 101762 102017 102594 103489 103617 106625 107393 109954 110146 110401 111489 112001 112193 112386 112961 113473 115329 115905 116097 116865 119937 164930 177090 177154 194626 206082 237826 243906 247810 281666 287810 293442 297858 299138 299458 320514 331650 332610 348546 368386 368450 368770 368962 371074 100022093"
auctionUrl: "http://item.taobao.com/item.htm?id=567270395710"
biz30day: 607
couponActivityId: null
couponAmount: 10
couponEffectiveEndTime: "2019-04-26"
couponEffectiveStartTime: "2019-04-25"
couponInfo: "满199元减10元"
couponLeftCount: 16800
couponLink: ""
couponLinkTaoToken: ""
couponOriLink: null
couponShortLink: null
couponStartFee: 199
couponTotalCount: 30000
dayLeft: -18012
debugInfo: null
eventCreatorId: 0
eventRate: null
hasRecommended: null
hasSame: null
hasUmpBonus: null
includeDxjh: 0
isBizActivity: null
isTbPt: 0
leafCatId: 50012043
nick: "天猫国际官方直营"
pictUrl: "//img.alicdn.com/bao/uploaded/i3/2549841410/O1CN01CQGOyJ1MHoyNfz1d9_!!2549841410-0-sm.jpg"
reservePrice: 499
rlRate: 30.07
rootCatId: 50012029
rootCatScore: 0
rootCategoryName: null
sameItemPid: "-568184547"
sellerId: 2549841410
shopTitle: "天猫国际官方直营"
title: "【直营】<span class=H>Nike</span><span class=H>耐克</span> Tanjun 男子休闲<span class=H>运动鞋</span> 812654"
tk3rdRate: null
tkCommFee: 6.98
tkCommonFee: 6.98
tkCommonRate: 2
tkFinalCampaign: 10
tkFinalFee: null
tkFinalRate: null
tkMktStatus: null
tkRate: 2
tkSpecialCampaignIdRateMap: {}
tkTbPtCommFee: 0
tkTbPtEndTime: "1970-01-01 08:00:00"
tkTbPtGroupSize: 0
tkTbPtPrice: 0
tkTbPtStartTime: "1970-01-01 08:00:00"
totalFee: 805.41
totalNum: 190
umpBonus: null
userType: 1
userTypeName: null
zkPrice: 349
}
'''