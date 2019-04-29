import itchat, time
from itchat.content import *
from tbk_api import tbk_helper
import tb_login
import tbk_coupon


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    # msg.user.send('%s: %s' % (msg.type, msg.text))
    if tbk_helper.is_tbk_pwd(msg.text):
        new_pwd = tbk_coupon.get_new_pwd(msg.text)
        msg.user.send(new_pwd)
    else:
        #@890623e56794841cdb267eb9f928fa2df940750e770ee579893ea198bacc8e71 (danel)
        #msg.user.send('I love you whatever you say, my darling')
        return


'''
@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg.download(msg.fileName)
    typeSymbol = {
        PICTURE: 'img',
        VIDEO: 'vid', }.get(msg.type, 'fil')
    return '@%s@%s' % (typeSymbol, msg.fileName)


@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send('Nice to meet you!')


@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg.isAt:
        msg.user.send(u'@%s\u2005I received: %s' % (
            msg.actualNickName, msg.text))


'''


def main():
    tb_login.get_cookies(False)
    itchat.auto_login(True)
    itchat.run(True)
