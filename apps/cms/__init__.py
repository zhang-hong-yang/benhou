from flask import Blueprint

"""
cms : 蓝图的名字空间,不同的蓝图,相同的endpoint名，不会出现命名冲突的问题
__name__指明了该蓝图下的静态文件和模板文件的查找根路径
"""
cms_bp = Blueprint('cms', __name__, url_prefix='/cms')

# 导入蓝图管理的视图
from . import auth_view

