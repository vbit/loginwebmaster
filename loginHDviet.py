# -*- coding: UTF-8 -*-

import hashlib
import os
import re
import urllib,urllib2
import cookielib

username = 'bitav90@gmail.com'
passText = 'wiyeuem'
p = hashlib.md5(passText)
password = p.hexdigest()

print password


def check_login(source,username):
    
    logged_in_string = 'Bi Bi'

    if re.search(logged_in_string,source,re.IGNORECASE):
        return True
    else:
        return False


def doLogin(cookiepath, username, password):

    if not os.path.isfile(cookiepath):
        cookiepath = os.path.join(cookiepath,'cookiesHDviet.lwp')
        
    try:
        os.remove(cookiepath)
    except:
        pass

    if username and password:

        login_url = 'http://movies.hdviet.com/dang-nhap.html'

        header_string = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'

        cookie_string = 'movie_autoplay=; loc={%\22province%22:24%\2C%\22zone%22:2%\2C%\22country%22:%\22vn%\22%\2C%\22ip%22:%22123.25.30.143%22}; popupNotice=false; vnhd_sessionhash=ckkpb1fo6hff3sg668sc2r9k90; __utma=34337085.1017517156.1399277707.1399277707.1399277707.1; __utmb=34337085.47.10.1399277707; __utmc=34337085; __utmz=34337085.1399277707.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%\20provided)'

        login_data = urllib.urlencode({'username':username, 'password':password, 'textcaptcha':'30789af317ff123448571b5a0140ce36'})

        req = urllib2.Request(login_url, login_data)
        req.add_header('User-Agent',header_string)
        req.add_header('Cookie',cookie_string)

        cj = cookielib.LWPCookieJar()

        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

        response = opener.open(req)
        source = response.read()
        
        response.close()

        login = check_login(source,username)

        if login == True:
            cj.save(cookiepath)

        return login
    
    else:
        return False

if __name__ == "__main__":
    if username is '' or password is '':
        print 'YOU HAVE NOT SET THE USERNAME OR PASSWORD!'
    else:
        logged_in = doLogin(os.getcwd(),username,password)
        print 'LOGGED IN:',logged_in
