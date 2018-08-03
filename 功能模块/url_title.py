# coding=UTF-8
import requests
from lxml import etree  www.dbsec.cn# 必须加上这个组件，否则会错误

class TS(object):
    def ts(self):
        test = url_title('')
        print test

#通过域名获取网站title信息，如果访问失败则返回"网站失效"
#---------------------------------------------------
def url_title(url_y):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}
        html = requests.get('http://' + url_y, headers=headers)
        html.encoding = "utf-8"
        page = etree.HTML(html.text)
        title = page.xpath('/html/head/title/text()')
        title = title[0].strip()
        return title
    except:
        return '网站失效！'
#---------------------------------------------------

if __name__ == "__main__":
    tt = TS()
    tt.ts()
