#!/usr/bin/python
# -*- coding: utf-8 -*-

from tbk_api.TbkApiBase import TbkApiBase


#
class XXX(TbkApiBase):

    __method = ''

    def __init__(self):
        super().__init__()

    #
    def send(self):
        params = {

        }
        return self.request(self.__method, params)


if __name__ == '__main__':
    pass