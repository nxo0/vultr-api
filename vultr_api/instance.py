# -*- coding: utf-8 -*-
from . import logger

def vm_list(id):
    print("インスタンス一覧を表示します。")
    try:
        print("インスタンス一覧の表示に成功しました")
    except Exception as e:
        logger.err("インスタンスの表示に失敗しました")
        logger.err(e)