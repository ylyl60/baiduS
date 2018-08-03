# coding=UTF-8
import requests
from lxml import etree
import sys
import urllib
import socket
reload(sys)
sys.setdefaultencoding('utf-8')

class BDC(object):
    def getURL(self):
        for n in range(30):
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}
            #url = 'https://www.baidu.com/s?wd=%E5%9C%A8%E7%BA%BF%E6%95%99%E8%82%B2&rsv_spt=1&rsv_iqid=0xcb306ff3000119a2&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=11&rsv_sug1=8&rsv_sug7=100'
            keyword = '在线教育 平台'
            url = 'https://www.baidu.com/s?wd='+urllib.quote(keyword)+'&pn=' + str(n) + '0'
            #print(url)
            html = requests.get(url,headers=headers)
            #print(html.status_code)
            #print(html.text)
            datas = etree.HTML(html.text)
            dat = datas.xpath('//div[@class="f13"]/a/text()')
            #print(dat)
            with open('baidu.txt', 'a') as fp:
                for i in dat:
                    if(i!=u'\u767e\u5ea6\u5feb\u7167'):
                        o = i.lstrip('https://')
                        b = o.split('/',1)[0]
                        c = www_ip(b)
                        d = ip_address(c)
                        if (c != '8.8.8.8'):
                            e = url_title(b)
                        else:
                            e = '网站失效'
                        #print b+'-----'+c+'-----'+d+'-----'+e
                        fp.write(b+'------'+c+'-----'+d+'-----'+e)
                        #print(i)
                        fp.write("\n")
                fp.close()
        #print("-------")

def www_ip(name):  #域名转IP
    try:
        result = socket.getaddrinfo(name, None)
        return result[0][4][0]
    except:
        return '8.8.8.8'

def ip_address(name1):
    #print name1
    ipapi = 'http://ip.taobao.com/service/getIpInfo.php?ip=' + name1
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}
    html = requests.get(ipapi, headers=headers)
    address = html.text.replace('"','')
    country = address.split(',')[2].split(':')[1]
    region = address.split(',')[4].split(':')[1]
    city = address.split(',')[5].split(':')[1]
    isp = address.split(',')[7].split(':')[1]
    try:
        #print country + '_' + region + '_' + city + '_' + isp
        return  country + '_' + region + '_' + city + '_' + isp
    except:
        return 0

def url_title(name2):
    url = name2
    #print url
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}
    try:
        html = requests.get('http://' + url, headers=headers)
        html.encoding = "utf-8"
        page = etree.HTML(html.text)
        title = page.xpath('/html/head/title/text()')
        title = title[0].strip()
        #print title
        return title
    except:
        return '网站失效！'

if __name__ == "__main__":
    bdc = BDC()
    bdc.getURL()