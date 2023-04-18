import pytest

from common import login

# 使用 icyfenix 作为整个测试的测试用户
# 这里把 token 作为 session 级别的 fixture，一次 pytest 运行中，只会执行一次 login，所有的测试用例共享这个 token
@pytest.fixture(scope="session")
def token():
    resp = login("icyfenix", "MFfTW3uNI4eqhwDkG7HP9p2mzEUu/r2")
    return resp["access_token"]
    
    

