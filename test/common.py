import requests
import pytest

BASE_URL = "http://81.70.57.108:8080/"
DEFAULT_ACCOUNT = "icyfenix"
DEFAULT_PWD = "MFfTW3uNI4eqhwDkG7HP9p2mzEUu/r2"


# 登录
def login(username, password) -> dict:
    """
    获取 token
    """
    url = BASE_URL + "oauth/token"
    query_params = {
        "username": username,
        "password": password,
        "grant_type": "password",
        "client_id": "bookstore_frontend",
        "client_secret": "bookstore_secret",
    }
    resp = requests.post(url, params=query_params)
    return resp.json()


# 获取默认token
def get_default_test_user_token() -> str:
    resp = login(DEFAULT_ACCOUNT, DEFAULT_PWD)
    return resp["access_token"]


# 获取用户信息
def get_account(username):
    url = BASE_URL + "restful/accounts/" + username
    resp = requests.get(url)
    return resp.json()


# 创建新用户的数据
def new_account_data():
    return {
        "username": "test_user",
        "email": "1111111@qq.com",
        "password": "123456",
        "telephone": "11111111111",
        "name": "test"
    }


# 删除用户
def delete_account(token: str, name: str):
    url = BASE_URL + f"restful/accounts/{name}"
    headers = {"Authorization": "bearer " + token}
    resp = requests.delete(url=url, headers=headers)
    assert resp.status_code == 200, f"删除用户(name={name })失败"


# 通过id获取产品信息
def get_product(product_id: int):
    url = BASE_URL + f"restful/products/{product_id}"
    resp = requests.get(url)
    return resp.json()


# 创建新产品数据
def product_data():
    return {
        "title": "测试书籍",
        "price": 129,
        "rate": 9.6,
        "cover": "/static/cover/jvm3.jpg",
        "desc": "",
        "description": "测试书籍描述",
        "detail": "/static/desc/jvm3.jpg",
    }


# 创建产品
def create_product(token: str, product: dict) -> dict:
    url = BASE_URL + "restful/products"
    headers = {"Authorization": "bearer " + token}
    resp = requests.post(url=url, headers=headers, json=product)
    return resp.json()


# 删除产品
def delete_product(token: str, id: int):
    url = BASE_URL + f"restful/products/{id}"
    headers = {"Authorization": "bearer " + token}
    resp = requests.delete(url=url, headers=headers)
    assert resp.status_code == 200, f"删除产品(id={id})失败"


# 创建结算单数据
def settlement_data():
    return {
        "items": [{"amount": 1, "id": 1}],
        "purchase": {
            "name": "周志明",
            "telephone": "18888888888",
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


# 提交结算单
def settlements(token):
    url = BASE_URL + "restful/settlements"
    headers = {"Authorization": "bearer " + token}
    resp = requests.post(url=url, headers=headers, json=settlement_data())
    return resp.json()


if __name__ == "__main__":
    pass
    # login(DEFAULT_ACCOUNT, DEFAULT_PWD)
    # token = get_default_test_user_token()
    # product = {
    #     "id": 14,
    #     "title": "测试书籍",
    #     "price": 129.0,
    #     "rate": 9.6,
    #     "description": "测试书籍描述",
    #     "cover": "/static/cover/jvm3.jpg",
    #     "detail": "/static/desc/jvm3.jpg",
    #     "specifications": None,
    # }
    #
    # product = create_product(token, product)
    #
    # print(product)