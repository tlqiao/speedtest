from flask import jsonify,request,Blueprint
from backend.apitest.chains import generate_api_test_code_v2
from backend.apitest.base_api import get_server_list, get_api_url_by_server, get_api_details
from flask_cors import CORS

apitest_blueprint = Blueprint('apitest_blueprint', __name__)
CORS(apitest_blueprint)
@apitest_blueprint.route('/apitest/genApiTestCode',methods=['POST'])
def generateApiTestCode():
    data = request.json
    language = data.get('language', 'javascript')
    test_tool = data.get('test_tool', 'jest' if language in ['javascript', 'js'] else 'pytest')
    if 'request' not in data:
     return  jsonify({'error': 'Missing api request field'}), 400     
    api_header = data.get('api_header', {"Content-Type": "application/json"})
    test_context=data.get('test_context',  'write api test')
    code = generate_api_test_code_v2(language=language,request=request,test_tool=test_tool,api_header=api_header,test_context=test_context)
    return jsonify({'code':code})

@apitest_blueprint.route('/apitest/getServerList',methods=['GET'])
def getServerList():
    server_List=get_server_list()
    return jsonify({'server_List': server_List})

@apitest_blueprint.route('/apitest/getApiUrlList',methods=['GET'])
def getApiUrlList():
    server_name = request.args.get('server_name')
    if not server_name:
        return jsonify({'error': 'Query parameter "server_name" is missing'}), 400
    apiUrlList=get_api_url_by_server(server_name=server_name)
    result = {'apiUrlList': apiUrlList}
    return jsonify(result)

@apitest_blueprint.route('/apitest/getApiReqRes',methods=["GET"])
def getApiReqRes():
    server_name=request.args.get('server_name')
    api_url=request.args.get('api_url')
    method=request.args.get('method')
    if not server_name or not api_url or not method:
        return jsonify({'error':'Query parameter is missing'}),400
    req,res=get_api_details(server_name=server_name,api_url=api_url,method=method)
    return jsonify({'apiReq':req,'apiRes':res})



