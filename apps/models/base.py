from contextlib import contextmanager

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy


class SQLAlchemy(_SQLAlchemy):
	"""
	继承SQLALchemy,使用上下文管理器,保存commit出错回滚
	"""

	@contextmanager
	def auto_commit(self):
		try:
			yield
			self.session.commit()
		except Exception as e:
			self.session.rollback()
			raise e


db = SQLAlchemy()


class Base(db.Model):
	__abstract__ = True
	id = db.Column(db.Integer, primary_key=True)
	status = db.Column(db.Integer, default=1)

	# 定义从attrs字典结构中，赋值表字段名称
	def set_attrs(self, attrs):
		for k, v in attrs.items():
			if hasattr(self, k) and k != 'id':
				setattr(self, k, v)

	def __getitem__(self, item):
		if hasattr(self, item):
			return getattr(self, item)
