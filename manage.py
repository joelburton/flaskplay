import os

from flask.ext.script import Manager, Server

from flaskplay import create_app

# default to dev config
env = os.environ.get('FLASK_MODE', 'dev')
app = create_app('flaskplay.config.%sConfig' % env.capitalize())

manager = Manager(app)

manager.add_command("server", Server())


@manager.shell
def make_shell_context():
    return dict()


if __name__ == '__main__':
    manager.run()


