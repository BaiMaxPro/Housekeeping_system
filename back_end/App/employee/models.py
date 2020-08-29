from App.employee import employee  # 获取蓝图

from App.employee.models import *  # 获取数据库模型对象和SQLAlchemy对象db，注意不可使用App模块中的db

@employee.route('/')  # 设置路由
def employee():  # 执行的方法
    return 'This Page Is Employee'