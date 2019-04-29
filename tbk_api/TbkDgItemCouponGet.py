#!/usr/bin/python
# -*- coding: utf-8 -*-

from tbk_api.TbkApiBase import TbkApiBase


#
class TbkDgItemCouponGet(TbkApiBase):

    __method = 'taobao.tbk.dg.item.coupon.get'

    def __init__(self):
        super().__init__()

    #
    def send(self, q):
        params = {
            'adzone_id': self.tbk_adzoneid,
            'q':    q,
        }
        return self.request(self.__method, params)


if __name__ == '__main__':
    q = 'ASICS亚瑟士2019春夏男跑鞋缓冲耐磨运动鞋EXCITE 6 1011A616-200'
    q = 'asics旗舰店 '+ q
    t = TbkDgItemCouponGet()
    t.send(q)
