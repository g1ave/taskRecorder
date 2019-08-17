from taskRecorder import create_app
from flask_script import Manager

if __name__ == '__main__':
    app = create_app()
    manager = Manager(app)
    manager.run()
