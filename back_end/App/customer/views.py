from App.customer import customer  # 获取蓝图

from App.customer.models import *  # 获取数据库模型对象和SQLAlchemy对象db，注意不可使用App模块中的db

@customer.route('/')  # 设置路由
def customer():  # 执行的方法
    return 'This Page Is Customer'