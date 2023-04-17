# 结算
# 提交一张结算单，根据结算单中的物品，生成支付单

import requests


# 测试提交订单 合法信息
def test_settlement():
    url = "http://81.70.57.108:8080/restful/settlements"
    headers = {
        "Authorization": "bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJpY3lmZW5peCIsInNjb3BlIjpbIkJST1dTRVIiXSwiZXhwIjoxNjgxNzQzNTQxLCJhdXRob3JpdGllcyI6WyJST0xFX1VTRVIiLCJST0xFX0FETUlOIl0sImp0aSI6IjA0MDNiMGE4LTIwZDItNDhlOS1hMTAzLTMzOGI2YzZmNmI0OCIsImNsaWVudF9pZCI6ImJvb2tzdG9yZV9mcm9udGVuZCIsInVzZXJuYW1lIjoiaWN5ZmVuaXgifQ.o0pYXhfTKgCnMD1ZAjXwxIqTCVJD-QEtVFcFocuoTV0"
    }
    data = {
        "items": [{"amount": 1, "id": 3}],
        "purchase": {
            "name": "周志明",
            "telephone": "17834526737",
            "delivery": True,
            "address": {"province": "广东省", "city": "广州市", "area": "海珠区"},
            "location": "广东省  广州市 海珠区 唐家湾港湾大道科技一路3号远光软件股份有限公司",
            "pay": "wechat",
            "id": 1,
            "username": "icyfenix",
            "avatar": "https://www.gravatar.com/avatar/1563e833e42fb64b41eed34c9b66d723?d=mp",
            "email": "icyfenix@gmail.com",
        },
    }
    resp = requests.get(url, headers=headers, json=data)
    assert resp.status_code == 200


# 测试提交订单 非法法信息
def test_settlement():
    url = "http://81.70.57.108:8080/restful/settlements"
    headers = {
        "Authorization": "bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJpY3lmZW5peCIsInNjb3BlIjpbIkJST1dTRVIiXSwiZXhwIjoxNjgxNzQzNTQxLCJhdXRob3JpdGllcyI6WyJST0xFX1VTRVIiLCJST0xFX0FETUlOIl0sImp0aSI6IjA0MDNiMGE4LTIwZDItNDhlOS1hMTAzLTMzOGI2YzZmNmI0OCIsImNsaWVudF9pZCI6ImJvb2tzdG9yZV9mcm9udGVuZCIsInVzZXJuYW1lIjoiaWN5ZmVuaXgifQ.o0pYXhfTKgCnMD1ZAjXwxIqTCVJD-QEtVFcFocuoTV0"
    }
    data = {
        "items": [{"amount": 1, "id": 3}],
        "purchase": {
            "name": "",
            "telephone": "1783452673",
            "delivery": true,
            "address": {"province": "北京市", "city": "市", "area": "区"},
            "location": "北京市  市 区 广东省  广州市 海珠区 唐家湾港湾大道科技一路3号远光软件股份有限公司",
            "pay": "alipay",
            "id": 1,
            "username": "icyfenix",
            "avatar": "https://www.gravatar.com/avatar/1563e833e42fb64b41eed34c9b66d723?d=mp",
            "email": "icyfenix@gmail.com",
        },
    }
    resp = requests.get(url, headers=headers, json=data)
    json = resp.json()
    assert resp.status_code == 200
