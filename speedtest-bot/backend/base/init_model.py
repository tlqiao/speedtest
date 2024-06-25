import openai
import os
from langchain_openai.chat_models import ChatOpenAI
from langchain_community.chat_models.moonshot import MoonshotChat
from langchain_community.chat_models import ChatZhipuAI
from langchain_community.chat_models import ChatBaichuan

def _init_chat_openai(model_name):
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    return ChatOpenAI(model=model_name)

def _init_chat_baichuan(model_name):
    baichuan_api_key = os.environ.get("BAICHUAN_API_KEY")
    return ChatBaichuan(baichuan_api_key=baichuan_api_key)

def _init_chat_zhipuai(model_name):
    zhipuai_api_key = os.environ.get("ZHIPU_API_KEY")
    return ChatZhipuAI(
        api_key=zhipuai_api_key,
        model=model_name,
        temperature=0.5,
    )

def _init_moonshot_chat(model_name):
    moonshot_api_key = os.environ.get("MOONSHOT_API_KEY")
    return MoonshotChat(model=model_name)

def init_model(model_name):
    model_initializers = {
        "gpt": _init_chat_openai,
        "Baichuan2": _init_chat_baichuan,
        "GLM": _init_chat_zhipuai,
        "moonshot": _init_moonshot_chat
    }

    prefix = model_name.split("-")[0]
    if prefix in model_initializers:
        llm= model_initializers[prefix](model_name)
        return llm
    else:
        raise ValueError("Unsupported model name:", model_name)