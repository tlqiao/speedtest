from backend.apitest.contract_prompts import generate_contract_test_prompt
from langchain_core.output_parsers import StrOutputParser
from backend.base.init_model import init_model
import backend.config.configs as configs

output_parser = StrOutputParser()

def write_contract_test(test_tool, request, response, url, method,model_name=configs.DEFAUT_MODEL):
    llm = init_model(model_name=model_name)
    chain = generate_contract_test_prompt | llm | output_parser
    contract_test =chain.invoke({'test_tool':test_tool,'api_url':url,'api_method':method,'api_request':request,'api_response':response})
    return contract_test
