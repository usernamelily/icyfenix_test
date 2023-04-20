from typing import List

import pytest

from common import login, product_data, delete_product,create_product, get_default_test_user_token


# 使用 icyfenix 作为整个测试的测试用户
# 这里把 token 作为 session 级别的 fixture，一次 pytest 运行中，只会执行一次 login，所有的测试用例共享这个 token
@pytest.fixture(scope="session")
def token():
    resp = login("icyfenix", "MFfTW3uNI4eqhwDkG7HP9p2mzEUu/r2")
    return resp["access_token"]


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