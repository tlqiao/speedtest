from flask import Flask
from backend.apitest.apitest_server import apitest_blueprint
from backend.uitest.uitest_server import uitest_blueprint
from backend.testcase.testcase_server import testcase_blueprint
from flask_cors import CORS
from  backend.config import configs

app = Flask(__name__)

app.register_blueprint(apitest_blueprint, url_prefix='/')
app.register_blueprint(uitest_blueprint,url_prefix='/')
app.register_blueprint(testcase_blueprint,url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True,port=configs.BACKEND_SEVER_PORT)