from backend.uitest.web_prompts import generate_webui_locator_prompt, generate_webui_step_function_prompt
from backend.base.init_model import init_model
import backend.config.configs as configs
from langchain_core.output_parsers import StrOutputParser

output_parser = StrOutputParser()

def write_locators_for_web_ui(test_tool, web_page,model_name=configs.DEFAUT_MODEL):
    llm = init_model(model_name=model_name)
    chain = generate_webui_locator_prompt | llm | output_parser
    locators  = chain.invoke({'test_tool': test_tool,'web_page': web_page})
    return locators


def write_step_function_for_web_ui(test_tool, locators, step_scenario,model_name=configs.DEFAUT_MODEL):
    llm = init_model(model_name=model_name)
    chain = generate_webui_step_function_prompt | llm | output_parser
    step_function_code= chain.invoke({'test_tool': test_tool,'page_locators': locators,'test_step_description':step_scenario})
    return step_function_code
