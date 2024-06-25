from backend.apitest.mock_prompts import generate_mapping_file_prompt, generate_mapping_file_with_regex_prompt
from langchain_core.output_parsers import StrOutputParser
from backend.base.init_model import init_model
import backend.config.configs as configs

output_parser = StrOutputParser()

def write_mapping_file(mapping_rule, url, method, request, response,model_name=configs.DEFAUT_MODEL):
    llm=init_model(model_name=model_name)
    if mapping_rule.get("is_use_regex"):
        chain = generate_mapping_file_with_regex_prompt | llm | output_parser
    else:
        chain = generate_mapping_file_prompt | llm | output_parser
    is_map_cookie = mapping_rule.get("is_map_cookie")
    is_map_header = mapping_rule.get("is_map_header")
    mapping_file = chain.invoke({'is_map_cookie':is_map_cookie,'is_map_header':is_map_header,'api_url':url,'api_method':method,'api_request':request,'api_response':response})  
    return mapping_file
