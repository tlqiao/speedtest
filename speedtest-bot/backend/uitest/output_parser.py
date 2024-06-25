import json
import re

def extract_locator_for_cypress(input_string):
    key_value_pattern1 = re.compile(r'(\w+):\s*(cy\.(?:get|contains)\(.*?\))')
    key_value_pattern2 = re.compile(r'(\w+):\s*\"(cy\.(?:get|contains)\(.*?\))\"')

    matches = key_value_pattern1.findall(input_string)
    if matches == []:
       matches =  key_value_pattern2.findall(input_string)   
    result = {match[0]: match[1] for match in matches}
    result_json = json.dumps(result, indent=2)

    return result_json