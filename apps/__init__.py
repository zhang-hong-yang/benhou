"""
app的创建
建议以函数进行封装
"""
from flask import Flask


# 蓝图注册函数
def register_blueprint(app):
	from apps.cms import cms_bp
	app.register_blueprint(cms_bp)


def create_app():
	app = Flask(__name__)
	app.config.from_object('apps.private_conf')
	app.config.from_object('apps.public_conf')
	register_blueprint(app)
	return app
