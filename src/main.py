from config.envConfig import EnvConfig
from module.classifeirModel.infrastructure.classifeirRoutes import classifeirRoutes
from common.app.application import Application
from module.health.infrastructure.healthCheckRoute import healtCheckRoute

application = Application([classifeirRoutes, healtCheckRoute])

application.setup()
app = application.create_app()

if  __name__ == '__main__':
    app.run(port=EnvConfig.get_port(), host=EnvConfig.get_ip(), debug=True)