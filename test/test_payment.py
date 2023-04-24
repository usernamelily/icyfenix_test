import requests
from common import BASE_URL, settlements, settlement_data


# 提交结算单，支付状态为待支付，然后取消订单
def test_settlement(token):
    #提交结算单
    new_settlement = settlements(token)
    
    #断言订单状态为待支付
    assert new_settlement["payState"] == "WAITING"
    
    #获取结算单id
    payid = new_settlement["payId"]
    
    #取消订单
    url = BASE_URL + "restful/pay/" + str(payid)
    query_param = {"state": "CANCEL"}
    headers = {"Authorization": "bearer " + token}
    resp = requests.patch(url, params=query_param, headers=headers)
    json = resp.json()
    
    #断言订单状态为取消
    assert resp.status_code ==200
    assert json["code"] == 0
    assert json['message'] == '操作已成功'
    

# 提交缺失收件人姓名的结算单
def test_settlement_faile(token):
    data = settlement_data()
    data["telephone"] = ""

    url = BASE_URL + "restful/settlements"
    headers = {"Authorization": "bearer " + token}
    resp = requests.post(url, headers=headers, json=data)
    json = resp.json()
    
    assert resp.status_code == 400 
    assert json["code"] == 1
    assert json["message"] == "结算单中缺少配送信息"
