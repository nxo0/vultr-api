# -*- coding: utf-8 -*-
from . import logger
import urllib.request

def vm_list(api_key):
    req = urllib.request.Request('https://api.vultr.com/v2/instances')
    req.add_header('Authorization', f'Bearer {api_key}')
    with urllib.request.urlopen(req) as res:
        res = res.read().decode('utf-8')
        print(res)

def vm_create():
    print("インスタンスを作成しました")