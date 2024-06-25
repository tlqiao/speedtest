from backend.unittest.prompts import generate_unit_test_prompt, generate_integration_test_prompt
import backend.config.configs as configs
from backend.base.init_model import init_model
from langchain_core.output_parsers import StrOutputParser

output_parser = StrOutputParser()

def write_unit_test(test_tool, language, mock_tool, test_type, assert_tool, source_code,model_name):
    llm = init_model(model_name=model_name)
    chain = generate_unit_test_prompt | llm | output_parser
    if test_type == "unit_test":
        chain = generate_unit_test_prompt | llm | output_parser
    else:
        chain = generate_integration_test_prompt | llm | output_parser
    unit_test = chain.invoke({'test_tool':test_tool,'language':language,'mock_tool':mock_tool,'assert_tool':assert_tool,'source_code':source_code})
    return unit_test
