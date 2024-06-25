from flask import jsonify,request,Blueprint
from flask_cors import CORS
from backend.testcase.chains import write_case
import backend.config.configs as configs

testcase_blueprint = Blueprint('testcase_blueprint', __name__)
CORS(testcase_blueprint)

@testcase_blueprint.route('/testcase/genTestCase',methods=['POST'])
def generateTestCase():
    data = request.json
    requirments = data.get('requirements', 'login')
    model_name=data.get('model',configs.DEFAUT_MODEL)
    testcase=write_case(requirements=requirments,model_name=model_name)
    return jsonify({'testcase':testcase})