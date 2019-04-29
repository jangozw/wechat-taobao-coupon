#!/usr/bin/python
# -*- coding: utf-8 -*-

from tbk_api.TbkApiBase import TbkApiBase


#
class TbkMaterialOptional(TbkApiBase):

    __method = 'taobao.tbk.dg.material.optional'
    __result = {}

    def __init__(self):
        super().__init__()

    #
    def send(self, product_keyword):
        params = {
            'q': product_keyword,
            'adzone_id': self.tbk_adzoneid,
        }
        self.__result = self.request(self.__method, params)
        return self

    def first_item(self):
        try:
            item = self.__result['result_list']['map_data'][0]
            coupon = {
                'num_iid': item['num_iid'],
                'title': item['title'],
                'shop_title': item['shop_title'],
                'url': 'https:'+item['url'],
                'pict_url': item['pict_url'],
                'white_image': item['white_image'],
                'reserve_price': item['reserve_price'],
                'zk_final_price': item['zk_final_price'],
                'volume': item['volume'],
                'coupon_info': item['coupon_info'],
                'provcity': item['provcity'],
            }
            return coupon
        except Exception as e:
            print(e)


if __name__ == '__main__':
    k = 'ASICS亚瑟士2019春夏男跑鞋缓冲耐磨运动鞋EXCITE 6 1011A616-200'
    k = '【直营】Nike耐克 Tanjun 男子休闲运动鞋 812654'
    t = TbkMaterialOptional()
    r = t.send(k).first_item()
    print(r['url'])
    # https://s.click.taobao.com/t?e=

    #
    # &scm=null&pvid=100_11.178.150.43_14608_5291556250044126415&app_pvid=59590_11.10.253.204_2238_1556250044120&ptl=floorId:2836;pvid:100_11.178.150.43_14608_5291556250044126415;app_pvid:59590_11.10.253.204_2238_1556250044120&xId=dGbVyjIqGtT7NRnTGbssA6tEmWU4rt9ekTnEY7IlY39zlhXFsBWF5vsn7mo98uFPFhgaEK6CPNrM91UGw26eps&union_lens=lensId:0b0afdcc_0c7b_16a57bb2700_48d0
