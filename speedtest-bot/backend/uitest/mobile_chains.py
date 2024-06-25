from backend.base.init_model import init_model
import backend.config.configs as configs
from langchain_core.output_parsers import StrOutputParser

from backend.uitest.mobile_prompts import mobileui_locator_prompt, mobileui_step_function_prompt

output_parser = StrOutputParser()

def write_locator_for_mobile_ui(client_tool, platform, layout,model_name=configs.DEFAUT_MODEL):
    llm = init_model(model_name=model_name)
    chain = mobileui_locator_prompt | llm | output_parser
    locators  = chain.invoke({'client_tool': client_tool,'platform': platform,'layout':layout})
    return locators


def write_step_function_for_mobile_ui(client_tool, locators, step_scenario,model_name=configs.DEFAUT_MODEL):
    llm = init_model(model_name=model_name)
    chain = mobileui_step_function_prompt | llm | output_parser
    step_function_code  = chain.invoke({'client_tool': client_tool,'locators': locators,'test_step_description':step_scenario})
    return step_function_code
