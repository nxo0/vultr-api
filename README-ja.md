# Vultr-api

([English](README.md) / 日本語)

Vultr-api はVultrをPythonプログラムから操作するためのライブラリです。

## Install

```bash
$ pip install git+https://github.com/nxo0/vultr-api
```


## Example

現在使用しているインスタンス(サーバー)一覧を取得し、新しくインスタンスを作成する例です。

```python
import vultr_api

vultr = vultr_api

print(vultr.instance.vm_list())

try:
    vultr.instance.vm_create()
except Exception as e:
    print("インスタンスの作成に失敗しました。")
```

