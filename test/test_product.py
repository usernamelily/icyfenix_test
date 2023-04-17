# 测试产品相关接口
import requests


# 获取仓库中所有的货物信息GET
def test_get_all_products():
    url = "http://81.70.57.108:8080/restful/products"
    resp = requests.get(url)
    resp.status_code = "200"
    json = resp.json()
    assert len(json) > 0


# 获取仓库中指定的货物信息GET
def test_get_product_by_id():
    url = "http://81.70.57.108:8080/restful/products/3"
    resp = requests.get(url)
    resp.status_code = "200"
    json = resp.json()
    assert json["id"] == 3


# 管理员更新产品信息PUT
def test_update_products():
    url = "http://81.70.57.108:8080/restful/products"
    data = {"id": 2, "title": "智慧的疆界", "price": "90"}
    headers = {
        "Authorization": "bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJpY3lmZW5peCIsInNjb3BlIjpbIkJST1dTRVIiXSwiZXhwIjoxNjgxNzM5NDQzLCJhdXRob3JpdGllcyI6WyJST0xFX1VTRVIiLCJST0xFX0FETUlOIl0sImp0aSI6ImZhNzdlMDAzLTg3YjYtNGNhMy05OWZiLTMxYWRkZTYwYWRiMyIsImNsaWVudF9pZCI6ImJvb2tzdG9yZV9mcm9udGVuZCIsInVzZXJuYW1lIjoiaWN5ZmVuaXgifQ.modJMoGYf4CRpSOLxniHIgZEjhHHav2TjC4nKvDw_mY"
    }
    resp = requests.put(url, headers=headers, json=data)
    json = resp.json()
    assert resp.status_code == 200


# 普通用户 更新产品信息PUT
def test_update_products_by_user():
    url = "http://81.70.57.108:8080/restful/products"
    data = {
        "id": 2,
        "title": "智慧的疆界",
        "price": "160",
        "rate": 9.1,
        "description": "<p>这是一部对人工智能充满敬畏之心的匠心之作，由《深入理解Java虚拟机》作者耗时一年完成，它将带你从奠基人物、历史事件、学术理论、研究成果、技术应用等5个维度全面读懂人工智能。</p> <p>\\n本书以时间为主线，用专业的知识、通俗的语言、巧妙的内容组织方式，详细讲解了人工智能这个学科的全貌、能解决什么问题、面临怎样的困难、尝试过哪些努力、取得过多少成绩、未来将向何方发展，尽可能消除人工智能的神秘感，把阳春白雪的人工智能从科学的殿堂推向公众面前。</p>",
        "cover": "/static/cover/ai.jpg",
        "detail": "/static/desc/ai.jpg",
    }
    headers = {
        "Authorization": "bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJsbCIsInNjb3BlIjpbIkJST1dTRVIiXSwiZXhwIjoxNjgxNzQzMTI1LCJhdXRob3JpdGllcyI6WyJST0xFX1VTRVIiXSwianRpIjoiNDEwYmUwMGYtNWIzZC00YjkxLWEyYmQtMTAxZjY1NTE1MWE4IiwiY2xpZW50X2lkIjoiYm9va3N0b3JlX2Zyb250ZW5kIiwidXNlcm5hbWUiOiJsbCJ9.YdAJFgLMShORZ-p9AxquxfErkmbaYvY51Nf29tm9VnA"
    }
    resp = requests.put(url, headers=headers, json=data)
    json = resp.json()
    assert resp.status_code == 403


# 创建新的产品POST  (操作结果，库存没有多一本书，而是将第一本书的位置替换掉了)
def test_add_new_product():
    url = "http://81.70.57.108:8080/restful/products"
    headers = {
        "Authorization": "bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJpY3lmZW5peCIsInNjb3BlIjpbIkJST1dTRVIiXSwiZXhwIjoxNjgxNzQzNTQxLCJhdXRob3JpdGllcyI6WyJST0xFX1VTRVIiLCJST0xFX0FETUlOIl0sImp0aSI6IjA0MDNiMGE4LTIwZDItNDhlOS1hMTAzLTMzOGI2YzZmNmI0OCIsImNsaWVudF9pZCI6ImJvb2tzdG9yZV9mcm9udGVuZCIsInVzZXJuYW1lIjoiaWN5ZmVuaXgifQ.o0pYXhfTKgCnMD1ZAjXwxIqTCVJD-QEtVFcFocuoTV0"
    }
    data = {
        "id": 1,
        "title": "凤凰架构测试指南",
        "price": "48",
        "rate": "8.2",
        "description": "<p>这是一部从工作原理和工程实践两个维度深入剖析JVM的著作，是计算机领域公认的经典，繁体版在台湾也颇受欢迎。  自2011年上市以来，前两个版本累计印刷36次，销量超过30万册，两家主要网络书店的评论近90000条，内容上近乎零差评，是原创计算机图书领域不可逾越的丰碑，第3版在第2版的基础上做了重大修订，内容更丰富、实战性更强：根据新版JDK对内容进行了全方位的修订和升级，围绕新技术和生产实践新增逾10万字，包含近50%的全新内容，并对第2版中含糊、瑕疵和错误内容进行了修正。  全书一共13章，分为五大部分：  第一部分（第1章）走近Java  系统介绍了Java的技术体系、发展历程、虚拟机家族，以及动手编译JDK，了解这部分内容能对学习JVM提供良好的指引。  第二部分（第2~5章）自动内存管理  详细讲解了Java的内存区域与内存溢出、垃圾收集器与内存分配策略、虚拟机性能监控与故障排除等与自动内存管理相关的内容，以及10余个经典的性能优化案例和优化方法；  第三部分（第6~9章）虚拟机执行子系统  深入分析了虚拟机执行子系统，包括类文件结构、虚拟机类加载机制、虚拟机字节码执行引擎，以及多个类加载及其执行子系统的实战案例；  第四部分（第10~11章）程序编译与代码优化  详细讲解了程序的前、后端编译与优化，包括前端的易用性优化措施，如泛型、主动装箱拆箱、条件编译等的内容的深入分析；以及后端的性能优化措施，如虚拟机的热点探测方法、HotSpot 的即时编译器、提前编译器，以及各种常见的编译期优化技术；  第五部分（第12~13章）高效并发  主要讲解了Java实现高并发的原理，包括Java的内存模型、线程与协程，以及线程安全和锁优化。  全书以实战为导向，通过大量与实际生产环境相结合的案例分析和展示了解决各种Java技术难题的方案和技巧。</p>",
        "cover": "/static/cover/jvm3.jpg",
        "detail": "/static/desc/jvm3.jpg",
        "specifications": [
            {"id": 3, "item": "ISBN", "value": "9787111641247", "productId": 1},
            {"id": 8, "item": "出版年", "value": "2019-12", "productId": 1},
            {"id": 9, "item": "装帧", "value": "平装", "productId": 1},
            {"id": 2, "item": "副标题", "value": "JVM高级特性与最佳实践", "productId": 1},
            {"id": 4, "item": "书名", "value": "深入理解Java虚拟机（第3版）", "productId": 1},
            {"id": 6, "item": "丛书", "value": "华章原创精品", "productId": 1},
            {"item": "页数", "value": "4", "productId": 1},
            {"item": "作者", "value": "Lily", "productId": 1},
            {"item": "出版社", "value": "佛珠奥出版社", "productId": 1},
        ],
    }
    resp = requests.put(url, headers=headers, json=data)
    json = resp.json()
    assert resp.status_code == 200


# 删除产品DELETE
def test_del_product():
    url = "http://81.70.57.108:8080/restful/products/1"
    headers = {
        "Authorization": "bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJpY3lmZW5peCIsInNjb3BlIjpbIkJST1dTRVIiXSwiZXhwIjoxNjgxNzQzNTQxLCJhdXRob3JpdGllcyI6WyJST0xFX1VTRVIiLCJST0xFX0FETUlOIl0sImp0aSI6IjA0MDNiMGE4LTIwZDItNDhlOS1hMTAzLTMzOGI2YzZmNmI0OCIsImNsaWVudF9pZCI6ImJvb2tzdG9yZV9mcm9udGVuZCIsInVzZXJuYW1lIjoiaWN5ZmVuaXgifQ.o0pYXhfTKgCnMD1ZAjXwxIqTCVJD-QEtVFcFocuoTV0"
    }
    resp = requests.delete(url, headers=headers)
    json = resp.json()
    assert resp.status_code == 200


# 根据产品查询库存GET
def test_get_stockpile_by_id():
    url = "http://81.70.57.108:8080/restful/products/stockpile/1"
    headers = {
        "Authorization": "bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJpY3lmZW5peCIsInNjb3BlIjpbIkJST1dTRVIiXSwiZXhwIjoxNjgxNzQzNTQxLCJhdXRob3JpdGllcyI6WyJST0xFX1VTRVIiLCJST0xFX0FETUlOIl0sImp0aSI6IjA0MDNiMGE4LTIwZDItNDhlOS1hMTAzLTMzOGI2YzZmNmI0OCIsImNsaWVudF9pZCI6ImJvb2tzdG9yZV9mcm9udGVuZCIsInVzZXJuYW1lIjoiaWN5ZmVuaXgifQ.o0pYXhfTKgCnMD1ZAjXwxIqTCVJD-QEtVFcFocuoTV0"
    }
    resp = requests.get(url, headers=headers)
    json = resp.json()
    assert resp.status_code == 200
