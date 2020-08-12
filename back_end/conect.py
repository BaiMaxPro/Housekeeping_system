import pymysql.cursors



connection = pymysql.connect( 
    host='home.chenxy.tech:3306', 
    port=3306, 
    user='root', 
    passwd='xdu2020', 
    database='housekeeping',
    charset='utf8'
    )