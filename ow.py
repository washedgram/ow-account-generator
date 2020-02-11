# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 19:24:27 2020

@author: Yongyao SUN
"""

import requests
import json
import random
import time
import names
import string
from fake_useragent import UserAgent

def loadProxyUserPass(filename):
    proxyList = []
    with open(filename + '.txt') as f:
        file_content = f.read()
    file_rows = file_content.split('\n')
    for i in range(0, len(file_rows)):
        if ':' in file_rows[i]:
            tmp = file_rows[i]
            tmp = tmp.split(':')
            proxies = {'http': 'http://' + tmp[2] + ':' + tmp[3] + '@' + tmp[0] + ':' + tmp[1] + '/',
                       'https': 'http://' + tmp[2] + ':' + tmp[3] + '@' + tmp[0] + ':' + tmp[1] + '/'}
            proxyList.append(proxies)
    return proxyList 


def loadProxyIpAuth(filename):
    proxyList = []
    with open(filename + '.txt') as f:
        file_content = f.read()
    tmp = file_content.split('\n')
    for n in range(0, len(tmp)):
        if ':' in tmp[n]:
            temp = tmp[n]
            proxies = {'http': 'http://' + temp,  'https': 'http://' + temp}
            proxyList.append(proxies)
    return proxyList 

def regist(name,ran_num,domain,pw):
    email = str(name)+str(ran_num)+str(domain)
    email = email.replace(' ','')
    s =requests.session()
    ua = UserAgent()
    headers = {'authority':'www.off---white.com',
               'scheme':'https',
               'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
               'accept-encoding':'gzip, deflate, br',
               'accept-language':'zh-CN,zh;q=0.9,de;q=0.8',
               'cache-control':'max-age=0',
               'sec-fetch-mode': 'navigate',
               'sec-fetch-site': 'none',
               'sec-fetch-user': '?1',
               'upgrade-insecure-requests':'1',
               'user-agent':ua.random
               }
    try:
        if bool(proxyList) == True:
            s.proxies = random.choice(proxyList)
        r=s.get('https://www.off---white.com/en-de/',headers=headers,timeout=5)   
        headers_regist = {
                'authority': 'www.off---white.com',
                'method': 'POST',
                'path': '/en-de/api/account/register',
                'scheme': 'https',
                'accept': 'application/json, text/plain, */*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'zh-CN,zh;q=0.9,de;q=0.8',
                'content-type': 'application/json;charset=UTF-8',
                'origin': 'https://www.off---white.com',
                'referer': 'https://www.off---white.com/',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': ua.random,
                'x-newrelic-id': 'VQUCV1ZUGwIFVlBRDgcA'
        }
        data = {
                'name': name,
                'username': email,
                'email': email,
                'password': pw,
                'countryCode': "DE",
                'receiveNewsletters': 'false'
                }
        regist_api = 'https://www.off---white.com/en-de/api/account/register'
        r = s.post(regist_api,headers=headers_regist,data=json.dumps(data).encode("utf-8"),timeout=5)
        if r.status_code == 200:
            print(str(email)+' Successfully registed')
            acc = str(email)+':'+str(pw)
            file = open('ow_acc.txt', 'a')
            file.write(str(acc.replace('\'', '')))
            file.write("\n")
            file.close()
    except:
        print(str(email)+' failed')

def regist_real_email(email_reg,pw):
    s =requests.session()
    ua = UserAgent()
    headers = {'authority':'www.off---white.com',
               'scheme':'https',
               'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
               'accept-encoding':'gzip, deflate, br',
               'accept-language':'zh-CN,zh;q=0.9,de;q=0.8',
               'cache-control':'max-age=0',
               'sec-fetch-mode': 'navigate',
               'sec-fetch-site': 'none',
               'sec-fetch-user': '?1',
               'upgrade-insecure-requests':'1',
               'user-agent':ua.random
               }
    try:
        if bool(proxyList) == True:
            s.proxies = random.choice(proxyList)
        r=s.get('https://www.off---white.com/en-de/',headers=headers,timeout=5)   
        headers_regist = {
                'authority': 'www.off---white.com',
                'method': 'POST',
                'path': '/en-de/api/account/register',
                'scheme': 'https',
                'accept': 'application/json, text/plain, */*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'zh-CN,zh;q=0.9,de;q=0.8',
                'content-type': 'application/json;charset=UTF-8',
                'origin': 'https://www.off---white.com',
                'referer': 'https://www.off---white.com/',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': ua.random,
                'x-newrelic-id': 'VQUCV1ZUGwIFVlBRDgcA'
        }
        data = {
                'name': names.get_full_name(),
                'username': email_reg,
                'email': email_reg,
                'password': pw,
                'countryCode': "DE",
                'receiveNewsletters': 'false'
                }
        regist_api = 'https://www.off---white.com/en-de/api/account/register'
        r = s.post(regist_api,headers=headers_regist,data=json.dumps(data).encode("utf-8"),timeout=5)
        if r.status_code == 200:
            print(str(email_reg)+' Successfully registed')
            acc = str(email_reg)+':'+str(pw)
            file = open('ow_acc.txt', 'a')
            file.write(str(acc.replace('\'', '')))
            file.write("\n")
            file.close()
    except:
        print(str(email_reg)+' failed')

if __name__ == "__main__":
    proxyList = []
    proxyIndex = 0
    try:
        proxyList =  loadProxyUserPass('proxies')
    except:
        proxyList =  loadProxyIpAuth('proxies')

    totalproxies = len(proxyList)
    if int(totalproxies) == 0:
        print('Running localhost!')
    else:
        print('Loaded %s proxies!' % totalproxies)
    mode = int(input('Mode 1: catchall    Mode 2: real email  '))
    if mode == 1:            
        domain = input(" Catchall domain(with@) : ")
        entryCount = int(input("Amount : "))
        pw = input('Password: ')
        for i in range(entryCount):
            name = names.get_full_name()
            ran_num = ''.join(random.sample(string.digits, 6))
            regist(name,ran_num,domain,pw)
            time.sleep(3)
    elif mode == 2:
        with open('email.txt') as f:
            file_content = f.read()
        email = file_content.split('\n')
        for i in range(len(email)):
            pw = ''.join(random.sample(string.ascii_letters + string.digits, 10))
            email_reg = email[i]
            regist_real_email(email_reg,pw)
            time.sleep(3)