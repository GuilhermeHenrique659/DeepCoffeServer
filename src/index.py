from module.classifeirModel.infrastructure.classifeirRoutes import classifeirRoutes
from common.app.application import Application

aplication = Application([classifeirRoutes])
aplication.run()