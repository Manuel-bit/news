from flask_script import Manager,Server
from app import create_app

app = create_app('production')

manager = Manager(app)
manager.add_command('server',Server)

if __name__ == '__main__':
  manager.run()