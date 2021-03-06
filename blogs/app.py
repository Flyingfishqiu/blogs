from flask_script import Manager
from flask_migrate import MigrateCommand, Migrate
from info import create_app, db

app = create_app('dev')
Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)


if __name__ == '__main__':
    print(app.url_map)
    manager.run()
