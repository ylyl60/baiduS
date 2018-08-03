# coding=UTF-8
import requests

class TS(object):
    def ts(self):
        test = ip_address('123.56.30.223')
        print test

#ip转换运营地址（使用了阿里的公共API，本程序可获取，国家、省份、城市、运营商）
#---------------------------------------------------
def ip_address(ip_y):
    ipapi = 'http://ip.taobao.com/service/getIpInfo.php?ip=' + ip_y
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}
    html_y= requests.get(ipapi, headers=headers)
    address = html_y.text.replace('"','')
    country = address.split(',')[2].split(':')[1]
    region = address.split(',')[4].split(':')[1]
    city = address.split(',')[5].split(':')[1]
    isp = address.split(',')[7].split(':')[1]
    try:
        return  country + '_' + region + '_' + city + '_' + isp
    except:
        return 0
#---------------------------------------------------

if __name__ == "__main__":
    tt = TS()
    tt.ts()
