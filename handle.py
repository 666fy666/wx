# -*- coding: utf-8 -*-
# filename: handle.py

import hashlib
import web
import receive
import time
import os
import requests
import json


class Handle(object):

    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)

    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "Fy12345678"

            list = [token, timestamp, nonce]
            list.sort()
            s = list[0] + list[1] + list[2]
            hashcode = hashlib.sha1(s.encode('utf-8')).hexdigest()
            print("handle/GET func: hashcode, signature: ", hashcode, signature)
            if hashcode == signature:
                return echostr
            else:
                return echostr
        except (Exception) as Argument:
            return Argument

    def POST(self):
        try:
            webData = web.data()
            print("Handle Post webdata is:\n", webData)
            # 打印消息体日志
            recMsg = receive.parse_xml(webData)

            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':

                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if str(recMsg.Content) == '体温':
                    f1 = open(r"C:\Users\Administrator\Desktop\sbtwtb\fy.txt", 'r', encoding='utf-8')
                    ms1 = ''' '''
                    while True:
                        line = f1.readline()
                        ms1 += line.strip() + '\n'
                        if not line:
                            break
                        print(ms1)
                    f1.close()

                    f2 = open(r"C:\Users\Administrator\Desktop\ymj\fy.txt", 'r', encoding='utf-8')
                    ms2 = ''' '''
                    while True:
                        line = f2.readline()
                        ms2 += line.strip() + '\n'
                        if not line:
                            break
                        print(ms2)
                    f2.close()

                    f3 = open(r"C:\Users\Administrator\Desktop\zty\fy.txt", 'r', encoding='utf-8')
                    ms3 = ''' '''
                    while True:
                        line = f3.readline()
                        ms3 += line.strip() + '\n'
                        if not line:
                            break
                        print(ms3)
                    f3.close()

                    content = str(ms1) + str(ms2) + str(ms3)
                    print('Reply message info:\n')
                    print('toUser =', toUser)
                    print('fromUser = ', fromUser)
                    print('content = ', content)
                    return self.render.reply_text(toUser, fromUser, int(time.time()), content)
                elif str(recMsg.Content) == '我爱你':
                    content = "我也爱你！！"
                    print('Reply message info:\n')
                    print('toUser =', toUser)
                    print('fromUser = ', fromUser)
                    print('content = ', content)
                    return self.render.reply_text(toUser, fromUser, int(time.time()), content)

                else:
                    def qingyunke(msg):
                        print("原话2>>", msg)
                        url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg={}'.format(msg)
                        print("原话3>>", msg)
                        html = requests.get(url)
                        a = html.json()["content"]
                        print("hh", str(a))
                        return html.json()["content"]

                    while True:
                        msg = str(recMsg.Content)
                        print("原话1>>", msg)
                        content = str(qingyunke(msg))
                        print("青云客>>", content)

                        print('Reply message info:\n')
                        print('toUser =', toUser)
                        print('fromUser = ', fromUser)
                        print('content = ', content)
                        return self.render.reply_text(toUser, fromUser, int(time.time()), content)
            else:
                print("不支持的消息类型：", recMsg.MsgType)
                return "success"
        except Exception as Argment:
            return Argment
