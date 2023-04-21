from typing import List
from common import BASE_URL
import requests

import pytest

from common import login, product_data, delete_product,create_product, get_default_test_user_token, new_account_data, delete_account


# 使用 icyfenix 作为整个测试的测试用户
# 这里把 token 作为 session 级别的 fixture，一次 pytest 运行中，只会执行一次 login，所有的测试用例共享这个 token
@pytest.fixture(scope="session")
def token():
    resp = login("icyfenix", "MFfTW3uNI4eqhwDkG7HP9p2mzEUu/r2")
    return resp["access_token"]

#新建用户的数据
@pytest.fixture()
def account_data():
    new_data = new_account_data()
    return new_data

#创建一个新用户
@pytest.fixture(scope='function')
def create_account(token, account_data):
    url = BASE_URL + "restful/accounts"
    headers = {"Authorization": "bearer " + token}
    resp = requests.post(url, headers=headers, json=account_data)
    
    yield
    
    delete_account(token, 'test_user')

#删除用户
@pytest.fixture(scope='function')
def deleted_account_by_names(token):
    pass
    
    yield

    delete_account(token, 'test_user')


# 新建产品的数据
@pytest.fixture()
def data():
    new_data = product_data()
    return new_data

#存放新建产品的id，测试结束后通过id消除新建的产品
@pytest.fixture(scope='function')
def to_be_deleted_product_ids(token) -> List[int]:
    ids = []
    
    yield ids

    for _id in ids:
        delete_product(token, _id)

#获取一个新产品id
@pytest.fixture(scope='function')
def get_new_product_id(token, data):
    new_product = create_product(token, data)   
    return new_product['id']

#新建一个产品，并返回产品所以信息
@pytest.fixture(scope='function')
def get_new_product(token, data):
    product = create_product(token, data) 
    id = product['id']
    
    yield product
    
    delete_product(token, id)