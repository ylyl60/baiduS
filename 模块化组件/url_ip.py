# coding=UTF-8
import socket

class TS(object):
    def ts(self):
        test = www_ip('www.163.com')
        print test

#域名转IP程序模块（如果域名无IP信息，则返回 8.8.8.8）
#---------------------------------------------------
def www_ip(url_y):
    try:
        result = socket.getaddrinfo(url_y, None)
        return result[0][4][0]
    except:
        return '8.8.8.8'
#---------------------------------------------------

if __name__ == "__main__":
    tt = TS()
    tt.ts()
