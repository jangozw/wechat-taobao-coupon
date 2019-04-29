#!/usr/bin/python
# -*- coding: utf-8 -*-

from tbk_api.TbkApiBase import TbkApiBase


#创建淘口令
class TbkPwdCreate(TbkApiBase):

    __method = 'taobao.tbk.tpwd.create'
    __result = {}
    def __init__(self):
        super().__init__()
    
    def send(self, logo, text, url):
        params = {
            "logo": logo,
            "text": text,
            "url": url
        }
        self.__result = self.request(self.__method, params)
        return self

    def get_pwd(self):
        try:
            return self.__result['data']['model']
        except Exception as e:
            print(e)
            return False

if __name__ == '__main__':
    logo = 'https://gss3.bdstatic.com/7Po3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D268%3Bg%3D0/sign=666fb0075266d0167e19992eaf10b33a/5243fbf2b2119313efcacc7a65380cd790238d6a.jpg'
    text = "测试文案商品描述"
    url = 'https://uland.taobao.com/'
    url = 'https://www.baidu.com/'
    url = 'https://s.click.taobao.com/t?e=m%3D2%26s%3Dog2exO6auxMcQipKwQzePOeEDrYVVa64r4ll3HtqqoxyINtkUhsv0GRq2oU4IM000yZ75MLd%2B9tblNv28sf27IA9Gsiz%2B3lb4af7NPVlxMTaoLZXOJDeBXkRn8DJEmnBSBaygToy7Xkd3mozMs0%2By%2FhHU8bwQCso%2FVJqtNeEg5ML8zORzELl0CyT%2BuB7rBaS8QMBQxovn5NxKmPmpIKZsA%3D%3D&scm=null&pvid=100_11.14.170.4_32340_6361556245471219758&app_pvid=59590_11.23.122.156_405_1556245471215&ptl=floorId:2836;pvid:100_11.14.170.4_32340_6361556245471219758;app_pvid:59590_11.23.122.156_405_1556245471215&xId=PSp1cuqUrLIUYelY24Jk5JeaT65yW3QcRfpe5txrDSL7KRP3cEsX3KGoURZLVAKcfF3qEnGxPtIYZnAYgLdL2i&union_lens=lensId:0b177a9c_0bb7_16a5775600f_e63b'
    t = TbkPwdCreate()
    t.send(logo, text, url)
