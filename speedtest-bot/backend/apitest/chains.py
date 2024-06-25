import openai
import os
from langchain.chains import LLMChain
from langchain_openai.chat_models import ChatOpenAI
from backend.apitest.prompts import generate_api_test_prompt,generate_api_test_prompt_v2
from langchain_core.output_parsers import StrOutputParser
import backend.config.configs as configs
from backend.base.init_model import init_model

openai.api_key = os.environ.get("OPENAI_API_KEY")
model_name = "gpt-3.5-turbo"
output_parser = StrOutputParser()

def generate_api_test_code(language, test_tool, request, response, parameterizedFields, parameterizedFieldValue, verifyFields, apiHeader,model_name=configs.DEFAUT_MODEL):
    llm = init_model(model_name=model_name)
    chain = generate_api_test_prompt | llm | output_parser
    api_test_code = chain.invoke({'language':language,'test_tool': test_tool, 'request':request,'response':response,'parameterizedFields':parameterizedFields,'parameterizedFieldValue':parameterizedFieldValue,'verifyFields':verifyFields,'apiHeader':apiHeader})
    return api_test_code

def generate_api_test_code_v2(language, test_tool, request,api_header,test_context,model_name=configs.DEFAUT_MODEL):
    llm = init_model(model_name=model_name)
    chain = generate_api_test_prompt_v2 | llm | output_parser
    api_test_code = chain.invoke({'language':language,'test_tool': test_tool, 'request':request,'api_header':api_header,'test_context':test_context})
    return api_test_code
