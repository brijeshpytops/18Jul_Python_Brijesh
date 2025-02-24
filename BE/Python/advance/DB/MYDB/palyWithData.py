from .dbConnection import cursor

def play_with_data():
    # sql = "select * from users"
    # sql = "select * from users where user_id < 10"
    # sql = "select * from users limit 10"
    # sql = "select * from users order by fullname"
    sql = "select * from users order by fullname desc"
    cursor.execute(sql)
    for d in cursor.fetchall():
        # print(d[1])
        print(d)