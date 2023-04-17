# 修改订单状态 get payID
import requests


# 取消已支付订单 取消失败
def test_cancel_order_fail():
    url = "http://81.70.57.108:8080/restful/pay/4e341f3b-2217-408c-9e38-5ef30438edcc?state=CANCEL"
    resp = requests.patch(url)
    # assert resp.status_code ==


# 取消未支付订单 取消成功
def test_cancel_order_success():
    url = "http://81.70.57.108:8080/restful/pay/169b3d2b-458c-45fd-97c0-8c05461cd76f?state=CANCEL"
    resp = requests.patch(url)
    assert resp.status_code == 200
