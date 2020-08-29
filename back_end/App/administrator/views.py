from App.administrator import admin  # 获取蓝图

from App.administrator.models import *  # 获取数据库模型对象和SQLAlchemy对象db，注意不可使用App模块中的db

@admin.route('/')  # 设置路由
def admin():  # 执行的方法
    return 'This Page Is Admin'