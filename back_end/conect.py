import pymysql.cursors
from flask import Flask 
from flask import request

server = Flask(__name__)

connection = pymysql.connect( 
    host='home.chenxy.tech', 
    port=3306, 
    user='root', 
    passwd='xdu2020', 
    database='housekeeping',
    charset='utf8'
    )

cursor=connection.cursor()

def my_db(sql_text):
    res = cursor.execute(sql_text)
    
    return res

@server.route('/')
def helle():
    return 'Hello, you set up this service successfully'

@server.route('/add_customer',methods=['post'])
def add_customer(tel, passwd):
    tel = request.valuse.get('tel')
    passwd = request.valuse.get('passwd')
    # test
    # tel = '123'
    # passwd = '123'

    if tel and passwd:
        find_sql = 'selsct * from login where username = "%s":'%tel
        if my_db(find_sql):
            res = {'msg':'this tel number has been used', 'msg_code':201}
        else:
            insert_sql= 'insert into login (name,passwd,role) values ("%s","%s",0)' %(tel,passwd)
            my_db(insert_sql)
            res = {'msg':' successfully','msg_code':0}
    else:
        res = {'msg':'NULL','msg_code':101}
    return res




if __name__ =='__main__':
    server.run()