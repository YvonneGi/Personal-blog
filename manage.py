from app import create_app
from flask_script import Manager,Server
from app import create_app,db
from app.models import User,Post, Comment, Subscription
from flask_migrate import Migrate, MigrateCommand

#Creating app instance
app = create_app('development')
# app = create_app('production')

#Manager Commands
manager = Manager(app)
migrate = Migrate(app,db)

#Manager Functionalities
manager.add_command('server', Server)
manager.add_command('db',MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Writer = Writer, Post = Post, Comment = Comment, Subscription = Subscription )

#Testing Settings
@manager.command
def test():
    """Run unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,Writer = writer, Blog = Blog, Comment = Comment )

if __name__ == '__main__':
    manager.run()
