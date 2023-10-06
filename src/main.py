from config.envConfig import EnvConfig
from module.classifeirModel.infrastructure.classifeirRoutes import classifeirRoutes
from common.app.application import Application

application = Application([classifeirRoutes])

application.setup()
app = application.create_app()
app.run(port=EnvConfig.get_port(), host=EnvConfig.get_ip())