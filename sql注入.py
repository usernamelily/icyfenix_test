def query_user_by_id(id: int):
    sql = f"select * from user where id = {id};"
    print(f"execute sql: {sql}")


def deleted_goods_by_id(id: int):
    sql = f"delete goods where id = {id};"
    print(f"execute sql: {sql}")


if __name__ == "__main__":
    deleted_goods_by_id("1; drop table goods")
