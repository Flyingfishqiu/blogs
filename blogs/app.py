from info import create_app, db
from flask_script import Manager
from flask_migrate import MigrateCommand, Migrate


Migrate(create_app('development'), db)
manager = Manager(create_app('development'))
manager.add_command("db", MigrateCommand)


if __name__ == '__main__':
    manager.run()
