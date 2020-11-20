# -*- coding: utf8 -*-
import requests 
from bs4 import BeautifulSoup

def pushinfo(info,specific):
    headers={   
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    'ContentType': 'text/html'
    }
    requests.session().get("https://sc.ftqq.com/你的server酱SCKEY.send?text=" + info + "&desp=" + specific,headers=headers)


def main(*args):
    headers={
        'Cookie': "htVD_2132_client_token=0C9A52205AD670E5C1FEEEC315F90A5D; htVD_2132_connect_is_bind=1; htVD_2132_connect_uin=0C9A52205AD670E5C1FEEEC315F90A5D; htVD_2132_sid=0; htVD_2132_nofavfid=1; htVD_2132_smile=1D1; htVD_2132_ignore_rate=1; htVD_2132_connect_login=1; htVD_2132_lastvisit=1604930985; htVD_2132_client_created=1604936469; htVD_2132_atarget=1; KF4=NajPLO; htVD_2132_home_readfeed=1605359783; htVD_2132_ttask=236785%7C20201120; htVD_2132_lastviewtime=236785%7C1605845715; htVD_2132_visitedfid=8D74D24D16D4; htVD_2132_st_t=236785%7C1605879083%7Cdec55cea4aa8412ffe170d201d055b68; htVD_2132_forum_lastvisit=D_2_1603979533D_10_1604418358D_16_1604824108D_24_1605019942D_4_1605628506D_8_1605879083; htVD_2132_noticonf=236785D1D3_3_1; htVD_2132_ulastactivity=1605879083%7C0; htVD_2132_checkpm=1; htVD_2132_lastcheckfeed=236785%7C1605879085; htVD_2132_checkfollow=1; htVD_2132_noticeTitle=1; Hm_lvt_46d556462595ed05e05f009cdafff31a=1605845721,1605853882,1605870674,1605879100; Hm_lpvt_46d556462595ed05e05f009cdafff31a=1605879100; htVD_2132_lastact=1605879087%09plugin.php%09",
        'ContentType':'text/html;charset=gbk'
    }
    requests.session().get('https://www.52pojie.cn/home.php?mod=task&do=apply&id=2',headers=headers)
    a=requests.session().get('https://www.52pojie.cn/home.php?mod=task&do=draw&id=2',headers=headers)
    b=BeautifulSoup(a.text,'html.parser')          
    c=b.find('div',id='messagetext').find('p').text

    if "您需要先登录才能继续本操作"  in c: 
        pushinfo("Cookie失效", c)
    elif "恭喜"  in c:
        pushinfo("吾爱破解签到成功",c)
    else:
        pushinfo("吾爱破解签到失败",c)
    print(c)


if __name__ == '__main__':
    main()
