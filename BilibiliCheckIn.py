# -*- coding: utf8 -*-
import requests 
import json
import time
import re
from bs4 import BeautifulSoup

cookies = '你的cookie'
aid='883409884'
uid=re.match('(?<=DedeUserID=).*?(?=;)',cookies)
sid=re.match('(?<=sid=).*?(?=;)',cookies)
csrf=re.match('(?<=bili_jct=).*',cookies)

def pushinfo(info,specific):
    headers={   
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    'ContentType': 'text/html'
    }
    requests.session().get("https://sc.ftqq.com/你的server酱SCKEY.send?text=" + info + "&desp=" + specific,headers=headers)


def login():
    headers={   
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    'Cookie':cookies
    }
    response = requests.session().get('http://api.bilibili.com/x/space/myinfo',headers=headers)
    rejson = json.loads(response.text)
    code = rejson['code']
    msg = rejson['message']
    if code == 0:
        print('登录成功')
        return True
    else:
        print('登录失败：'+msg)
        return False

def get_user_info():
    headers = {
        'Cookie':cookies
    }
    response = requests.session().get('http://api.bilibili.com/x/space/myinfo?jsonp=jsonp',headers=headers)
    rejson = json.loads(response.text)
    code = rejson['code']
    msg = rejson['message']
    if code == 0:
        userInfo=['账号：'+str(rejson['data']['silence']),
        '硬币：'+str(rejson['data']['coins']),
        '经验：'+str(rejson['data']['level_exp']['current_exp'])+"/"+str(rejson['data']['level_exp']['next_exp']),
        '等级：'+str(rejson['data']['level']),
        '昵称：'+str(rejson['data']['name'])
        ]
        print(userInfo[0]) 
        print (userInfo[1])
        print(userInfo[2])
        #response['data']['face'] #头像
        print(userInfo[3])
        print(userInfo[4])
        return userInfo
    else:
        print("用户信息获取失败："+msg)
        return "用户信息获取失败："+msg

def do_sign():
    headers = {
        'Cookie':cookies
    }
    response = requests.session().get('https://api.live.bilibili.com/sign/doSign',headers=headers)
    rejson = json.loads(response.text)
    code = rejson['code']
    msg = rejson['message']

    if code == 0:
        print('直播签到成功！') 
        return True
    else:
        print("直播签到失败："+msg)
        return False

def watch():
        # aid = 稿件av号
        headers = {
            'Cookie':cookies
        }
        response = requests.session().get('http://api.bilibili.com/x/web-interface/view?aid='+str(aid),headers=headers)
        rejson = json.loads(response.text)
        code = rejson['code']
        #print(response.text)
        if code == 0:
            cid = rejson['data']['cid']
            duration = rejson['data']['duration']
        else:
            print('视频信息解析失败')
            return False
        payload = {
            'aid': aid,
            'cid': cid,
            'part': 1,
            'did': sid,
            'ftime': int(time.time()),
            'jsonp': "jsonp",
            'lv': None,
            'mid': uid,
            'csrf': csrf,
            'stime': int(time.time()),
        }
        response = requests.session().post('http://api.bilibili.com/x/report/click/h5',data=payload,headers=headers)
        rejson = json.loads(response.text)
        code = rejson['code']
        if code == 0:
            payload = {
                'aid': aid,
                'cid': cid,
                'jsonp': "jsonp",
                'mid': uid,
                'csrf': csrf,
                'played_time': 0,
                'pause': False,
                'realtime': duration,
                'dt': 7,
                'play_type': 1,
                'start_ts': int(time.time()),
            }
            response = requests.session().post('http://api.bilibili.com/x/report/web/heartbeat',data=payload,headers=headers)
            rejson = json.loads(response.text)
            code = rejson['code']
            if code == 0:
                time.sleep(5)
                payload['played_time'] = duration - 1
                payload['play_type'] = 0
                payload['start_ts'] = int(time.time())
                response = requests.session().post('http://api.bilibili.com/x/report/web/heartbeat',data=payload,headers=headers)
                rejson = json.loads(response.text)
                code = rejson['code']
                if code == 0:
                    print(f"av{aid}观看成功")
                    return True
        print(f"av{aid}观看失败 {response}")
        return False

def main(*args):
    if login():
        ui = get_user_info()
        desp='直播签到：'+str(do_sign())+'\n\n'+'观看视频：'+str(watch())+'\n\n'+ui[0]+'\n\n'+ui[1]+'\n\n'+ui[2]+'\n\n'+ui[3]+'\n\n'+ui[4]+'\n\n'
        pushinfo('哔哩哔哩签到成功',desp)
    else:
        pushinfo('哔哩哔哩签到失败','')

    

if __name__ == '__main__':
    main()