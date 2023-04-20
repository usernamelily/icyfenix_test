import requests

from common import BASE_URL
from common import login
from common import get_account

# 测试用户相关接口


# 登陆
def test_auth():
    resp = login("icyfenix", "MFfTW3uNI4eqhwDkG7HP9p2mzEUu/r2")

    assert resp["access_token"] != None, "登陆失败"


# 获取用户信息，用户已存在
def test_get_account_with_existing_username():
    url = BASE_URL + "restful/accounts/icyfenix"

    resp = requests.get(url)
    json = resp.json()

    resp.status_code = "200"
    assert json["username"] == "icyfenix"


# 获取用户信息，用户不存在
def test_get_account_with_non_existing_username():
    url = BASE_URL + "restful/accounts/icyfenix_00001"

    resp = requests.get(url)
    text = resp.text

    assert resp.status_code == 204, "用户不存在，HTTP 状态码应该等于 204"
    assert text == ""


# 创建新的用户
# 成功
def test_add_new_user_success():
    url = "http://81.70.57.108:8080/restful/accounts"
    data = {
        "username": "sum",
        "email": "1162162162@qq.com",
        "password": "78910",
        "telephone": "17676207620",
        "name": "hao",
    }
    resp = requests.post(url, json=data)
    resp.status_code = "200"
    json = resp.json()
    assert json["message"] == "操作已成功"


# 创建用户失败 用户名称重复
def test_add_new_user_failure():
    url = "http://81.70.57.108:8080/restful/accounts"
    data = {
        "username": "sum",
        "email": "1112162162@qq.com",
        "password": "789101",
        "telephone": "16676207620",
        "name": "ho",
    }
    resp = requests.post(url, json=data)
    json = resp.json()
    resp.status_code = "400"
    assert json["message"] == "用户名称、邮箱、手机号码均不允许与现存用户重复"


# 更新自己的用户信息
def test_update_self(token):
    # 获取用户信息
    account = get_account("icyfenix")

    # 更新用户信息
    url = BASE_URL + "restful/accounts"
    headers = {"Authorization": "bearer " + token}
    account["name"] = "usernamelily"
    resp = requests.put(url, json=account, headers=headers)

    # 获取更新后的用户信息
    update_after_account = get_account("icyfenix")

    # 验证
    assert resp.status_code == 200, "更新用户信息失败"
    assert update_after_account["name"] == account["name"], "响应 200，但是没有更新用户名字"


# 更新其他用户的信息
def test_update_other_user(token):
    url = BASE_URL + "restful/accounts"
    headers = {"Authorization": "bearer " + token}
    account = {
        "id": 4,
        "username": "hh",
        "name": "huahua",
        "avatar": "https://www.gravatar.com/avatar/1563e833e42fb64b41eed34c9b66d723?d=mp",
        "telephone": "18888887772",
        "email": "icyfenix@gmail.com",
        "location": "唐家湾港湾大道科技一路3号远光软件股份有限公司",
    }

    resp = requests.put(url, json=account, headers=headers)

    assert resp.status_code == 400
    content = resp.json()
    assert "不是当前登陆用户" in content["message"]
