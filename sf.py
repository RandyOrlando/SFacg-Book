# -*- coding: UTF-8 -*-

def sfnext(url):
    import re,urllib
    html=urllib.request.urlopen(url).read().decode("utf-8")
    xyz1 =re.search('class="btn normal">下一章</a>', html, flags=0).span()
    xyz1=xyz1[0]
    xyz=html[:xyz1]
    xyz=xyz[-40:]
    xyz2=re.search('=',xyz,flags=0).span()
    xyz2=xyz2[1]
    xyz=xyz[xyz2:]
    xyz=xyz[1:][:-2]
    xyz="http://book.sfacg.com"+xyz
    return xyz
def sflast(url):
    import re,urllib
    html=urllib.request.urlopen(urllib.request.Request(url)).read().decode("utf-8")
    syz1 = re.search('class="btn normal">上一章</a>', html, flags=0	).span()
    syz1=syz1[0]
    syz=html[:syz1]
    syz=syz[-200:]
    syz2=re.search('<a href=',syz,flags=0).span()
    syz2=syz2[1]
    syz=syz[syz2:]
    syz=syz[1:][:-2]
    syz="http://book.sfacg.com"+syz
    return syz
def sf (url,cookie):
    import re
    nv=re.search("Novel",url)
    vip=re.search("vip",url)
    if vip !=None:
        ret=sfvip(url,cookie)
    if nv !=None:
        ret=sfnv(url)
    return ret
def sfnv(url):
    import re
    from urllib import request
    html=request.urlopen(url).read().decode("utf-8")
    try:
        nr1 = re.search('<div class="article-hd">', html, flags=0).span()
        nr1 = nr1[1]
        nr = html[nr1:]

        nr2 = re.search('</div>', nr, flags=0).span()
        nr2 = nr2[0]
        nr = nr[:nr2]

        bt1 = re.search('<h1 class="article-title">', nr, flags=0).span()
        bt1 = bt1[1]
        bt = nr[bt1:]

        bt2 = re.search('</h1>', bt, flags=0).span()
        bt2 = bt2[0]
        bt = bt[:bt2]
        bt = "\n" + bt

        zz1 = re.search('作者', nr, flags=0).span()
        zz1 = zz1[1]
        zz = nr[zz1:]

        zz2 = re.search('</span>', zz, flags=0).span()
        zz2 = zz2[0]
        zz = zz[:zz2]

        zz = "\n作者" + zz

        gxsj1 = re.search('更新时间', nr, flags=0).span()
        gxsj1 = gxsj1[1]
        gxsj = nr[gxsj1:]

        gxsj2 = re.search('</span>', gxsj, flags=0).span()
        gxsj2 = gxsj2[0]
        gxsj = gxsj[:gxsj2]

        gxsj = "\n更新时间" + gxsj

        zs1 = re.search('字数', nr, flags=0).span()
        zs1 = zs1[1]
        zs = nr[zs1:]

        zs2 = re.search('</span>', zs, flags=0).span()
        zs2 = zs2[0]
        zs = zs[:zs2]

        zs = "\n字数" + zs
        a = re.search('<div class="article-content font16" id="ChapterBody" data-class="font16">', html, flags=0).span()
        b = a[-1]

        c = html[b:]
        ccc = re.search('<p>', c, flags=0).span()
        ccc = ccc[0]
        ccc = ccc - 7
        c = c[ccc:]

        d = re.search("</div>", c, flags=0).span()
        e = d[0]
        f = c[:e]

        bb = re.sub("</p>", "\n       ", f, count=0, flags=0)
        bb = re.sub("<p>", "", bb, count=0, flags=0)
        bb = re.sub("<br>", "", bb, count=0, flags=0)
        ret=bt+zz+gxsj+zs+"\n----------------------------------------\n"
        ret=ret+bb+"-------------------end---------------"
        return ret
    except:
        return "获取失败"
def sfvip(url,cookie):
    import urllib
    import re
    import requests
    import PIL,PIL.Image
    from requests.cookies import RequestsCookieJar
# encoding=utf8 
    jar=RequestsCookieJar()
    jar.set('.SFCommunity',cookie,domain="sfacg.com",path='/')
    aa={'UserAgent':'User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
    }
    try:
        request=requests.get(url,headers=aa,cookies=jar,timeout=5)
    except:
        #print  "超时"
        return "获取HTML超时"
    #print(request.text)
    html=request.text
    htmlxx=urllib.request.urlopen(url).read().decode("utf-8")

    #获取文章信息
    nr1 = re.search('<div class="article-hd">', htmlxx, flags=0).span()
    nr1 = nr1[1]
    nr = htmlxx[nr1:]

    nr2 = re.search('</div>', nr, flags=0).span()
    nr2 = nr2[0]
    nr = nr[:nr2]

    bt1 = re.search('<h1 class="article-title">', nr, flags=0).span()
    bt1 = bt1[1]
    bt = nr[bt1:]

    bt2 = re.search('</h1>', bt, flags=0).span()
    bt2 = bt2[0]
    bt = bt[:bt2]
    bt = "\n" + bt

    zz1 = re.search('作者', nr, flags=0).span()
    zz1 = zz1[1]
    zz = nr[zz1:]

    zz2 = re.search('</span>', zz, flags=0).span()
    zz2 = zz2[0]
    zz = zz[:zz2]

    zz = "\n作者" + zz

    gxsj1 = re.search('更新时间', nr, flags=0).span()
    gxsj1 = gxsj1[1]
    gxsj = nr[gxsj1:]

    gxsj2 = re.search('</span>', gxsj, flags=0).span()
    gxsj2 = gxsj2[0]
    gxsj = gxsj[:gxsj2]

    gxsj = "\n更新时间" + gxsj

    zs1 = re.search('字数', nr, flags=0).span()
    zs1 = zs1[1]
    zs = nr[zs1:]

    zs2 = re.search('</span>', zs, flags=0).span()
    zs2 = zs2[0]
    zs = zs[:zs2]

    zs = "\n字数" + zs

    xx=bt+ zz+ gxsj+ zs
    wjm=bt
    #获取正文图片
    if (re.search("<img id='vipImage' src='/ajax/ashx/common.ashx?",html)==None):
        print ("获取失败此为vip章节，请确定你是否已经订阅该章节或者cookie是否正确。")
        input ("回车退出...")
        exit()
        return "获取失败"
    u=re.search("<img id='vipImage' src='/ajax/ashx/common.ashx?",html).span()
    html=html[u[1]:]
    n=re.search("' />",html).span()
    html=html[:n[0]]
    picurl='http://book.sfacg.com/ajax/ashx/common.ashx'+html
    #os.system('mkdir ~/sf/')
    try:
        html_str = requests.get(picurl,headers=aa,cookies = jar,timeout=20).content
    except:
        #print "超时"
        return "获取图片超时"
    # 写入文件,采用二进制写入文件
    import os
    try:
        wjm=re.sub("\n", "", wjm, count=0, flags=0)
    except:
        ht=0
    wjj=os.path.exists('./sf')
    if wjj== False:
        os.makedirs("./sf") 
    with open("./sf/"+wjm+".gif",'wb') as f:
        f.write (html_str)
        im=PIL.Image.open("./sf/"+wjm+".gif")

    im.show()
    return xx

import ini
cookie=ini.cookie()
tj = "ww"
url=input ("请输入SF文章链接:")
"""
try:
    while tj != "q":
        if tj == "r":
            url=input ("请输入SF文章链接:")
        print(sf(url,cookie))
        tj = input("是否继续? 退出输入q,下一章输入n,上一章输入l,重输链接输入r 输入其他刷新:")
        if tj=="n":
            url=sfnext(url)
        if tj=="l":
            url=sflast(url)
    print ("\n当前url:"+url)
except:
    print ("\n当前url:"+url)
"""
while tj != "q":
    if tj == "r":
        url=input ("请输入SF文章链接:")
    print(sf(url,cookie))
    tj = input("是否继续? 退出输入q,下一章输入n,上一章输入l,重输链接输入r 输入其他刷新:")
    if tj=="n":
        url=sfnext(url)
    if tj=="l":
        url=sflast(url)
print ("\n当前url:"+url)

