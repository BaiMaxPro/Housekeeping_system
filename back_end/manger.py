from flask_script import Manager

from App import create_app
from App.administrator import admin
from App.customer import customer
from App.employee import employee

app = create_app()  # 创建app

app.register_blueprint(admin, url_prefix='/admin')  # 注册蓝图
app.register_blueprint(customer, url_prefix='/customer')  # 注册蓝图
app.register_blueprint(employee, url_prefix='/employee')  # 注册蓝图

manager = Manager(app)  # 通过app创建manager对象

if __name__ == '__mian__':
    manager.run()  # 运行服务器