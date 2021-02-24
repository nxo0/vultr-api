# -*- coding: utf-8 -*-
from . import logger
import urllib.request
import json


def vm_list(api_key):
    try:
        if type(api_key) is str:
            req = urllib.request.Request('https://api.vultr.com/v2/instances')
            req.add_header('Authorization', f'Bearer {api_key}')
            with urllib.request.urlopen(req) as res:
                res = res.read().decode('utf-8')
                return res
        else:
            logger.err("[vultr-api] APIキーはString型で指定してください。")
    except Exception as e:
        logger.err(e)


def vm_create(api_key, region, plan, label, os_id, user_data, backups):
    try:
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
    except Exception as e:
        logger.err(e)


def vm_get(api_key, instance_id):
    try:
        if type(api_key) is str:
            req = urllib.request.Request(f'https://api.vultr.com/v2/instances/{instance_id}')
            req.add_header('Authorization', f'Bearer {api_key}')
            with urllib.request.urlopen(req) as res:
                res = res.read().decode('utf-8')
                return res
        else:
            logger.err("[vultr-api] APIキーはString型で指定してください。")
    except Exception as e:
        logger.err(e)


def vm_update(api_key, instance_id, label, tag, upgrade_plan):
    try:
        url = f"https://api.vultr.com/v2/instances/{instance_id}"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type:": "application/json"
        }
        data = {
            "label": label,
            "upgrade_plan": upgrade_plan,
            "tag": tag
        }
        req = urllib.request.Request(url, json.dumps(data).encode(), headers, method='PATCH')
        with urllib.request.urlopen(req) as res:
            res = res.read()
            return res
    except Exception as e:
        logger.err(e)