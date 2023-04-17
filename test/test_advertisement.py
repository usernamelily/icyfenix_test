import requests


# 验证广告资源
def test_advertisements():
    url = "http://81.70.57.108:8080/restful/advertisements"
    resp = requests.get(url)
    resp.status_code = "200"
    json = resp.json()
    assert len(json) > 1
