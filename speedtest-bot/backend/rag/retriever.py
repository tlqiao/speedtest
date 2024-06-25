from langchain_community.vectorstores.chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationSummaryMemory
from langchain.chains.retrieval_qa.base import RetrievalQA
import os
import shutil
from backend.database.test_db_manage import TestDBManage
from backend.config import configs

def get_all_file_paths():
    with TestDBManage("speedtest") as db_manager:
        paths = db_manager.get_all_file_path()
    return paths


def get_all_file_names():
    persist_path = configs.RAG_PERSIST_PATH
    with TestDBManage("speedtest") as db_manager:
        names = db_manager.get_all_file_name(persist_path=persist_path)
    return names

def delete_all_file():
    persist_path = configs.RAG_PERSIST_PATH
    try:
        shutil.rmtree(persist_path)
        print(f"Folder '{persist_path}' deleted successfully.")
    except OSError as e:
        print(f"Error: {persist_path} : {e.strerror}")
    with TestDBManage("speedtest") as db_manager:
        db_manager.clear_data(collection_name="document_info")
    return "Delete All files succssfully"


def query_question(question, model_name, file_name_list):
    persist_path = configs.RAG_PERSIST_PATH
    vector_persist_path = persist_path+'/vector/'
    vectorDB = Chroma(persist_directory=vector_persist_path,
                      embedding_function=OpenAIEmbeddings())
    llm = ChatOpenAI(model_name=model_name,
                     temperature=0.5, verbose=True)
    new_file_name_list = [persist_path +"/source_file/" + filename for filename in file_name_list]
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm, retriever=vectorDB.as_retriever(search_kwargs={"k":1,"filter": {"source":{"$in": new_file_name_list}}}))
    answer = qa_chain({"query": question})["result"]
    return answer


def chat(question, chat_history, chat_model,file_name_list):
    persist_path = configs.RAG_PERSIST_PATH
    vector_persist_path = persist_path+'/vector/'
    vectorDB = Chroma(persist_directory=vector_persist_path,
                      embedding_function=OpenAIEmbeddings())
    llm = ChatOpenAI(model_name=chat_model,
                     temperature=0.5, verbose=True)
    new_file_name_list = [persist_path +"/source_file/" + filename for filename in file_name_list]
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vectorDB.as_retriever(search_kwargs={"k": 1,"filter":{"source":{"$in": new_file_name_list}}})
                                           )
    bot_message = qa_chain({"query": question})["result"]
    chat_history.append((question, bot_message))
    return "", chat_history