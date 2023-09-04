from common.app.application import Application
from common.model.model import predict, index
aplication = Application()
aplication.get_app().add_url_rule('/predict', None, predict, methods= ['POST'])
aplication.get_app().add_url_rule('/', None, index)

aplication.run()