from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import CSVLoader
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_community.document_loaders import UnstructuredHTMLLoader
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import JSONLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from backend.rag.text_spliter.chinese_recursive_text_splitter import ChineseRecursiveTextSplitter
from langchain.memory import ConversationSummaryMemory
from langchain.chains.retrieval_qa.base import RetrievalQA
import os
import shutil
from backend.database.test_db_manage import TestDBManage
from backend.config import configs

file_type_loader = {
    "txt": TextLoader,
    "pdf": PyPDFLoader,
    "html": UnstructuredHTMLLoader,
    "markdown": UnstructuredMarkdownLoader,
    "csv": CSVLoader,
    "json": JSONLoader
}


def _create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        try:
            os.makedirs(folder_path)
            print(f"Folder created: {folder_path}")
        except OSError as e:
            print(f"Error creating folder {folder_path}: {e}")
    else:
        print(f"Folder already exists: {folder_path}")

def _save_document_info(file_name):
    persist_path = configs.RAG_PERSIST_PATH
    dest_file_path = persist_path + "/source_file/"
    vector_path = persist_path + "/vector/"
    with TestDBManage("speedtest") as db_manager:
        db_manager.add_persist_path(persist_path=persist_path)
        db_manager.add_document_info(dest_file_path=dest_file_path, file_name=file_name, vector_path=vector_path, persist_path=persist_path)
    return f" Save document in database successfully"   


def _get_file_info(file):
    file_path = file.name
    folder_path = os.path.dirname(file_path)
    file_type = os.path.splitext(file_path)[1][1:]
    file_name = os.path.basename(file_path)
    file = {
        "folder_path": folder_path,
        "type": file_type,
        "name": file_name
    }
    return file


def _load_save_file(file, persist_path):
    file_info = _get_file_info(file)
    file_type = file_info["type"]
    loader_cls = file_type_loader[file_type]
    save_file_path = persist_path + '/source_file/'
    _create_folder_if_not_exists(save_file_path)
    copy_target_path = save_file_path + file_info["name"]
    shutil.copyfile(file.name, copy_target_path)
    loader= TextLoader(copy_target_path)
    docs = loader.load()
    _save_document_info(file_info["name"])
    return docs


def _split_document(docs, language,chunk_size,chunk_overlap):
    if language == "Chinese":
        document_splitter = ChineseRecursiveTextSplitter
    else:
        document_splitter = RecursiveCharacterTextSplitter
    splitter = document_splitter(
        keep_separator=True,
        is_separator_regex=True,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    splits = splitter.split_documents(docs)
    return splits


def save_vector_document(file, language, ebedding_model,chunk_size,chunk_overlap):
    persist_path = configs.RAG_PERSIST_PATH
    vector_path = persist_path + '/vector/'
    docs = _load_save_file(file=file, persist_path=persist_path)
    splited_text = _split_document(docs=docs, language=language,chunk_size=chunk_size,chunk_overlap=chunk_overlap)
    _create_folder_if_not_exists(vector_path)
    vectorstore = Chroma.from_documents(
        documents=splited_text, persist_directory=vector_path, embedding=OpenAIEmbeddings(model=ebedding_model))
    vectorstore.persist()
    vectorstore = None
    return "Save document vector successfully"