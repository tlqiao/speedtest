from frontend.api_test import api_test
from frontend.ui_test import ui_test
from frontend.contract_test import contract_test
from frontend.mock_server import mock_server
from frontend.unit_test import unittest
from frontend.about import about
from frontend.test_data import test_data
from backend.integration.case_direct import case_direct
from frontend.test_case import test_case
from frontend.rag_chat import rag_chat
import gradio as gr
from static.custom_css import custom_css
from backend.config import configs


app = gr.TabbedInterface(interface_list=[about,test_case, case_direct, unittest, api_test, contract_test, ui_test, mock_server, test_data,rag_chat], tab_names=[
                         "About", "Test Case", "Case", "Unit Test", "API Test", "Contract Test", "UI Test", "Mock Server", "Test Data","RAG Demo"], theme=gr.themes.Default(
    primary_hue="green"), title="SpeedTest Bot", css=custom_css)
app.queue().launch(server_port=configs.FRONTEND_SEVER_PORT,debug=True)