from flask import Blueprint

# from config import TEMPLATES_DIR, STATICFILES_DIR

admin = Blueprint('admin', __name__, 
                  )  # 创建一个蓝图对象，设置别名，模板文件地址，静态文件地址

from App.administrator import views  # 这里导入是为了在解释时，蓝图能加载到views文件中的路由数据