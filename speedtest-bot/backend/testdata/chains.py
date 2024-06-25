import openai
import os
from langchain.chains import LLMChain
from langchain_openai.chat_models import ChatOpenAI
from backend.testdata.prompts import chat_prompt, sql_chat_prompt, code_chat_prompt
from langchain_core.output_parsers import StrOutputParser
import backend.config.configs as configs
from backend.base.init_model import init_model

out_parser = StrOutputParser()

openai.api_key = os.environ.get("OPENAI_API_KEY")


def generate_csv_data(fields, data_rows,model_name=configs.DEFAUT_MODEL):
    llm = init_model(model_name=model_name)
    chain  = chat_prompt | llm | out_parser
    data = chain.invoke({'fields':fields,'data_rows':data_rows})
    return data


def generate_sql(sql_tables, user_request,model_name=configs.DEFAUT_MODEL):
    llm = init_model(model_name=model_name)
    chain = sql_chat_prompt | llm |out_parser
    data = chain.invoke({'sql_tables':sql_tables,'user_request':user_request})
    return data


def generate_code_from_sql(language, client_tool, sql, user_request,model_name=configs.DEFAUT_MODEL):
    llm = init_model(model_name=model_name)
    chain = code_chat_prompt | llm | out_parser
    data = chain.invoke({'language':language,'client_tool':client_tool,'sql':sql,'user_request':user_request})
    return data
