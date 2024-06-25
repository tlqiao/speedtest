from flask import jsonify,request,Blueprint
from backend.uitest.mobile_chains import write_locator_for_mobile_ui,write_step_function_for_mobile_ui
from backend.uitest.web_chains import write_locators_for_web_ui,write_step_function_for_web_ui
from flask_cors import CORS
from backend.uitest.output_parser import extract_locator_for_cypress

uitest_blueprint = Blueprint('uitest_blueprint', __name__)
CORS(uitest_blueprint)

@uitest_blueprint.route('/uitest/genWebLocator',methods=['POST'])
def genWebLocators():
    data = request.json
    test_tool = data.get('testTool', 'Cypress')
    web_page=data.get('webPage',"<>demo page</>")
    result=write_locators_for_web_ui(test_tool=test_tool,web_page=web_page)
    web_locators = extract_locator_for_cypress(result)
    return jsonify({'locators':web_locators})

@uitest_blueprint.route('/uitest/genWebStepFunction',methods=['POST'])
def genWebStepFunction():
    data=request.json
    test_tool=data.get('testTool',"Cypress")
    locators=data.get('locators',"locators={}")
    step_scenarios = data.get('scenarios',"login")
    step_function_code=write_step_function_for_web_ui(test_tool=test_tool,locators=locators,step_scenario=step_scenarios)
    return jsonify({'code':step_function_code})

@uitest_blueprint.route('/mobiletest/genMobileLocator',methods=['POST'])
def genMobileLocators():
    data = request.json
    client_tool = data.get('testTool', 'webdriverio')
    platform=data.get('platform','Android')
    layout=data.get('layout',"<>demo page</>")
    locators=write_locator_for_mobile_ui(client_tool=client_tool,platform=platform,layout=layout)
    return jsonify({'locators':locators})

@uitest_blueprint.route('/mobiletest/genMobileStepFunction',methods=['POST'])
def genMobileStepFunction():
    data=request.json
    client_tool=data.get('testTool','webdriverio')
    locators=data.get('locators',"locators={}")
    step_scenarios = data.get('scenarios',"login")
    step_function_code=write_step_function_for_mobile_ui(client_tool=client_tool,locators=locators,step_scenario=step_scenarios)
    return jsonify({'code':step_function_code})



