from flask_script import Manager

from apps import create_app

# 先创建app
app = create_app()

# 再用manager进行接管
manager = Manager(app=app)

if __name__ == '__main__':
    print(app.url_map)
    manager.run()
