# -*- coding: UTF-8 -*-


import os
import re
import urllib,urllib2
import cookielib

username = 'luka.bimbim'
password = 'abc123'

def check_login(source,username):
    
    logged_in_string = 'luka.bimbim'

    if re.search(logged_in_string,source,re.IGNORECASE):
        return True
    else:
        return False


def doLogin(cookiepath, username, password):

    if not os.path.isfile(cookiepath):
        cookiepath = os.path.join(cookiepath,'cookiesHanel.lwp')
        
    try:
        os.remove(cookiepath)
    except:
        pass

    if username and password:

        login_url = 'http://haneltv.vn/user'

        header_string = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'

        login_data = urllib.urlencode({'name':username, 'pass':password, 'form_build_id':'form-u6fxxNxRp8S8PvR7IfIycB5nQ4cY-R4SULyQ8KhQqqY', 'form_id':'user_login', 'op':'Đăng nhập'})

        req = urllib2.Request(login_url, login_data)
        req.add_header('User-Agent',header_string)

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
