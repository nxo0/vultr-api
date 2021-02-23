# -*- coding: utf-8 -*-
from . import logger
import urllib.request
import json


def vm_list(api_key):
    if type(api_key) is str:
        req = urllib.request.Request('https://api.vultr.com/v2/instances')
        req.add_header('Authorization', f'Bearer {api_key}')
        with urllib.request.urlopen(req) as res:
            res = res.read().decode('utf-8')
            return res
    else:
        logger.err("[vultr-api] APIキーはString型で指定してください。")


def vm_create(api_key, region, plan, label, os_id, user_data, backups):
    url = "https://api.vultr.com/v2/instances"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type:": "application/json"
    }
    data = {
        "region": region,
        "plan": plan,
        "label": label,
        "os_id": os_id,
        "user_data": user_data,
        "backups": backups
    }
    req = urllib.request.Request(url, json.dumps(data).encode(), headers)
    with urllib.request.urlopen(req) as res:
        res = res.read()
        return res