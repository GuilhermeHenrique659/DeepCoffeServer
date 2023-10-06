from module.classifeirModel.infrastructure.classifeirRoutes import classifeirRoutes
from common.app.application import Application

application = Application([classifeirRoutes])

def create_app():
    application.setup()
    app = application.create_app()
    app.run()
    return app