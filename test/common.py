import requests

BASE_URL = "http://81.70.57.108:8080/"

def login(username, password) -> str:
    """
    获取 token
    """
    url = BASE_URL + "oauth/token"
    query_params = {
        "username": username,
        "password": password,
        "grant_type": "password",
        "client_id": "bookstore_frontend",
        "client_secret": "bookstore_secret"
    }
    resp = requests.post(url, params=query_params)
    return resp.json()


# 获取用户信息
def get_account(username):
    url = BASE_URL + "restful/accounts/" + username
    resp = requests.get(url)
    return resp.json()

if __name__ == "__main__":
    # print(login("icyfenix", "MFfTW3uNI4eqhwDkG7HP9p2mzEUu/r2"))
    print(get_account("icyfenix"))