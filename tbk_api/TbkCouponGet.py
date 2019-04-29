#!/usr/bin/python
# -*- coding: utf-8 -*-

from tbk_api.TbkApiBase import TbkApiBase


#
class TbkCouponGet(TbkApiBase):

    __method = 'taobao.tbk.coupon.get'

    def __init__(self):
        super().__init__()

    # 这个接口要 item_id && activity_id 或者 me
    def send(self, item_id):
        params = {
            'item_id': item_id,
            # 'me': 'nfr%2BYTo2k1PX18gaNN%2BIPkIG2PadNYbBnwEsv6mRavWieOoOE3L9OdmbDSSyHbGxBAXjHpLKvZbL1320ML%2BCF5FRtW7N7yJ056Lgym4X01A%3D',
            # 'activity_id': '120013_4',
            # 'me': 'm%3D2%26s%3DdDzST%2Fo8VYkcQipKwQzePOeEDrYVVa64r4ll3HtqqoxyINtkUhsv0H7Z070Y3F6KLJZNqUVQqB9blNv28sf27IA9Gsiz%2B3lb4af7NPVlxMTaoLZXOJDeBXkRn8DJEmnBSBaygToy7Xkd3mozMs0%2By%2FhHU8bwQCso%2FVJqtNeEg5ML8zORzELl0CyT%2BuB7rBaS8QMBQxovn5NxKmPmpIKZsA%3D%3D',
            # 'me': 'm%3D2%26s%3DaJPzjRqBeawcQipKwQzePOeEDrYVVa64r4ll3HtqqoxyINtkUhsv0Jn%2FTWc4oxB5VpTHHGZ%2BJu9blNv28sf27IA9Gsiz%2B3lb4af7NPVlxMTaoLZXOJDeBXkRn8DJEmnBSBaygToy7Xkd3mozMs0%2By%2FhHU8bwQCso%2FVJqtNeEg5ML8zORzELl0CyT%2BuB7rBaS8QMBQxovn5NxKmPmpIKZsA%3D%3D',
            'me': 'XDNbTazGFuscQipKwQzePOeEDrYVVa64r4ll3HtqqoxyINtkUhsv0Jn/TWc4oxB5IG6CNHxzbctblNv28sf27IA9Gsiz+3lb4af7NPVlxMTaoLZXOJDeBXkRn8DJEmnBSBaygToy7Xkd3mozMs0+y/hHU8bwQCso/VJqtNeEg5ML8zORzELl0CyT+uB7rBaS8QMBQxovn5NxKmPmpIKZsA==',
        }
        return self.request(self.__method, params)


if __name__ == '__main__':
    t = TbkCouponGet()
    t.send('588208387661')
