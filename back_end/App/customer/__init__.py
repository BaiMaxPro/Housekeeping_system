from flask import Blueprint

# from config import TEMPLATES_DIR, STATICFILES_DIR

customer = Blueprint('customer', __name__, 
                  )  # 创建一个蓝图对象，设置别名，模板文件地址，静态文件地址

from App.customer import views