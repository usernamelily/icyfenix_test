# 测试产品相关接口
from typing import List

import requests
from common import BASE_URL
from common import get_product, create_product, login


# 获取仓库中所有的货物信息GET
def test_get_all_products():
    url = BASE_URL + "restful/products"

    resp = requests.get(url)
    json = resp.json()

    assert resp.status_code == 200
    assert len(json) > 0


# 获取已经存在的产品  
def test_get_product_by_existing_id(get_new_product):
    id = get_new_product["id"]
    url = BASE_URL + f"restful/products/{id}"

    resp = requests.get(url)
    json = resp.json()

    assert resp.status_code == 200
    assert json["title"] == "测试书籍"


# 获取不存在的产品  ：id = 100000
def test_get_product_by_non_existing_id():
    url = BASE_URL + "restful/products/10000"

    resp = requests.get(url)
    text = resp.text

    assert resp.status_code == 204, "产品不存在，HTTP 状态码应该等于 204"
    assert text == ""


# 更新一个已存在的产品成功
def test_update_existing_product(token, get_new_product):
    # 更新产品信息
    url = BASE_URL + "restful/products"
    headers = {"Authorization": "bearer " + token}
    get_new_product["price"] = 90
    resp = requests.put(url, headers=headers, json=get_new_product)

    # 获取更新后的产品信息
    id = get_new_product['id']
    product_after_update = get_product(id)

    # 验证
    assert resp.status_code == 200
    assert product_after_update["price"] == get_new_product["price"], "响应 200，但是没有更新成功"

# 更新一个已存在的产品失败，将产品价格修改为-10，
def test_update_existing_product_fail(token, get_new_product):
    # 更新产品信息
    url = BASE_URL + "restful/products"
    headers = {"Authorization": "bearer " + token}
    get_new_product["price"] = -10
    resp = requests.put(url, headers=headers, json=get_new_product)
    json = resp.json()

    # 验证
    assert resp.status_code == 400
    assert json["message"] == "商品价格最低为零"


# 创建一个产品，给定合法信息post
def test_create_product_success(token: str, data: dict, to_be_deleted_product_ids: List[int]):
    url = BASE_URL + "restful/products"
    headers = {"Authorization": "bearer " + token}

    resp = requests.post(url, headers=headers, json=data)
    json = resp.json()

    assert resp.status_code == 200
    assert json['id'] > 0
    assert json["title"] == data["title"]
    to_be_deleted_product_ids.append(json['id'])



# 创建一个产品，给定非法信息（商品名词为空）
def test_add_new_product_fail(token, data):
    url = BASE_URL + "restful/products"
    headers = {"Authorization": "bearer " + token}
    data = {
        "title": "",
    }

    resp = requests.post(url, headers=headers, json=data)
    json = resp.json()

    assert json["code"] == 1


# 删除一个存在的产品DELETE
def test_del_existing_product(token, get_new_product_id):
    url =  BASE_URL + f"restful/products/{get_new_product_id}"
    headers = {"Authorization": "bearer " + token}
    resp = requests.delete(url, headers=headers)
    assert resp.status_code == 200
    json = resp.json()
    
    #断言
    assert json["code"] == 0


# 删除一个不存在的产品
def test_del_non_existing_product(token):
    url = BASE_URL + "restful/products/10000"
    headers = {"Authorization": "bearer " + token}

    resp = requests.delete(url, headers=headers)
    json = resp.json()

    assert json["code"] == 1


# 根据已存在产品id查询库存GET
def test_get_stockpile_by_existing_id(token):
    url = BASE_URL + "restful/products/stockpile/2"
    headers = {"Authorization": "bearer " + token}

    resp = requests.get(url, headers=headers)
    json = resp.json()
    assert resp.status_code == 200
    assert json['amount'] >= 0

# 根据不存在产品id查询库存GET
def test_get_stockpile_by_non_existing_id(token):
    url = BASE_URL + "restful/products/stockpile/10000"
    headers = {"Authorization": "bearer " + token}

    resp = requests.get(url, headers=headers)
    json = resp.json()
    assert resp.status_code == 500
    assert json['code'] == 1
    
# 根据产品id修改库存成功, amount >= 0
def test_update_current_stockpile_success(token):
    url = BASE_URL + "restful/products/stockpile/2"
    headers = {"Authorization": "bearer " + token}
    params = {
        "amount": 10
    }

    resp = requests.patch(url, params=params, headers=headers)
    json = resp.json()
    assert resp.status_code == 200
    assert json['code'] == 0
    
#根据产品id修改库存失败，amount <0 
def test_update_fault_stockpile_fail(token):
    url = BASE_URL + "restful/products/stockpile/2"
    headers = {"Authorization": "bearer " + token}
    params = {
        "amount": -10
    }

    resp = requests.patch(url, params=params, headers=headers)
    json = resp.json()
    assert resp.status_code == 500
    assert json['code'] == 1

    