import requests

# 测试用户相关接口


# 拿到登录响应的token
def take_access_token():
    url = "http://81.70.57.108:8080/oauth/token?username=icyfenix&password=MFfTW3uNI4eqhwDkG7HP9p2mzEUu/r2&grant_type=password&client_id=bookstore_frontend&client_secret=bookstore_secret"
    resp = requests.get(url)
    json = resp.json()
    return json["access_token"]


access_token = take_access_token()


# 测试用户登录
def test_token():
    url = "http://81.70.57.108:8080/oauth/token?username=icyfenix&password=MFfTW3uNI4eqhwDkG7HP9p2mzEUu/r2&grant_type=password&client_id=bookstore_frontend&client_secret=bookstore_secret"
    resp = requests.get(url)
    json = resp.json()
    assert json["access_token"] != None


# 普通用户登录
def test_token_01():
    url = "http://81.70.57.108:8080/oauth/token?username=summer&password=p7US079zh3YgH8JB4V6/dot/aYLBmAm&grant_type=password&client_id=bookstore_frontend&client_secret=bookstore_secret"
    resp = requests.get(url)
    json = resp.json()
    assert json["access_token"] != None


# 根据用户名获取用户详情
def test_accounts():
    url = "http://81.70.57.108:8080/restful/accounts/icyfenix"
    headers = {"Authorization": "bearer " + access_token}
    resp = requests.get(url, headers=headers)
    resp.status_code = "200"
    json = resp.json()
    assert json["username"] == "icyfenix"


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


# 更新用户信息（普通用户只能更新自己的信息）
def test_update_user():
    url = "http://81.70.57.108:8080/restful/accounts"
    headers = {
        "Authorization": "bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJzdW1tZXIiLCJzY29wZSI6WyJCUk9XU0VSIl0sImV4cCI6MTY4MTc0OTUxOSwiYXV0aG9yaXRpZXMiOlsiUk9MRV9VU0VSIl0sImp0aSI6IjA5N2M2NTlkLTkwMzctNGM0NS1iNjhkLTkzOTI0OTE0ZGQ4NSIsImNsaWVudF9pZCI6ImJvb2tzdG9yZV9mcm9udGVuZCIsInVzZXJuYW1lIjoic3VtbWVyIn0.roXh2lmYzRzoxuesKAldG-S-viPisfXUE2MZ6fogwa0"
    }
    data = {
        "id": 7,
        "username": "ll",
        "name": "wang",
        "avatar": "https://www.gravatar.com/avatar/1563e833e42fb64b41eed34c9b66d723?d=mp",
        "telephone": "11111111111",
        "email": "wang234@qq.com",
        "location": "唐家湾港湾大道科技一路3号远光软件股份有限公司",
    }
    resp = requests.put(url, headers=headers, json=data)
    json = resp.json()
    assert resp.status_code == 200
