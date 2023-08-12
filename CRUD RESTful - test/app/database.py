import mysql.connector

def ConnectorMysql():
    mydb = mysql.connector.connect(
            host="mydb",
            user="admin",
            password="db4test$",
            database="simple_api"
    )
    return mydb

def get_all_user():
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM users;"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    arr = []
    if len(myresult) > 0: 
        for x in myresult:
            user = {
                "uid" : x[0],
                "name" : x[1],
                "age" : int(x[2])
            }
            arr.append(user)
    return arr

def get_user(_id):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM users WHERE uid='{}'; ".format(_id)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    if len(myresult) > 0: 
        for x in myresult:
            arr = {
                "uid" : x[0],
                "name" : x[1],
                "age" : int(x[2])
                }
    return arr

def insert_user(name, age):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "INSERT INTO users (name, age) VALUES (%s ,%s)"
    val = (name, age)
    mycursor.execute(sql,val)
    arr = {"uid" : mycursor.getlastrowid()}
    mydb.commit()
    mycursor.close()
    mydb.close()
    return arr
    

def update_user(_id, name, age):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "UPDATE users SET  name=%s , age=%s WHERE uid=%s"
    val = (name, age, _id)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()
    mydb.close()


def delete_user(_id):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "DELETE FROM users WHERE uid={}".format(_id)
    mycursor.execute(sql)
    mydb.commit()
    mycursor.close()
    mydb.close()