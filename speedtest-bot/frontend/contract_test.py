import gradio as gr
from backend.apitest.base_api import get_server_list, get_api_url_by_server, get_api_request_response, get_api_details, get_method_list
from backend.apitest.contract_chains import write_contract_test


def gen_contract_test(tool, request, response, url, method):
    if not request or not response or not url or not method:
        return f'request or response or url or method must not be empty or None'
    return write_contract_test(test_tool=tool, request=request,
                               response=response, url=url, method=method)


api_method_list = ['GET', 'POST', 'DELETE', 'PUT']

with gr.Blocks() as contract_test:
    list = get_server_list()
    with gr.Row():
        tool_dropdown = gr.Dropdown(
            choices=["Pact-JS"], value="Pact-JS", label="Choose Tool")
        with gr.Group():
            refresh_server_button = gr.Button(
                value="Refresh Server", elem_classes="custom_button")
            server_dropdown = gr.Dropdown(choices=list, show_label=False)
        with gr.Group():
            refresh_url_button = gr.Button(
                value="Refresh URL", elem_classes="custom_button")
            api_url_dropdown = gr.Dropdown(show_label=False, choices=[])
        with gr.Group():
            refresh_method_button = gr.Button(
                value="Refresh Method", elem_classes="custom_button")
            method_list_dropdown = gr.Dropdown(
                show_label=False, choices=api_method_list)
    with gr.Row(equal_height=True):
        with gr.Column(scale=1):
            with gr.Group():
                get_apiInfo_button = gr.Button(
                    value="Show API Details", elem_classes="custom_button")
                api_request = gr.Json(label="Api Request")
                api_response = gr.Json(label="Api Response")
        with gr.Column(scale=1):
            with gr.Group():
                gen_contract_test_button = gr.Button(
                    value="Generate Contract Test", elem_classes="custom_button")
                code = gr.Code(show_label=False, lines=4,
                               language="javascript")

    def update_server_list():
        list = get_server_list()
        return gr.Dropdown(choices=list,interactive=True)

    def update_api_url_list(server_name):
        list = get_api_url_by_server(server_name)
        return gr.Dropdown(choices=list,interactive=True)

    server_dropdown.select(update_api_url_list, inputs=server_dropdown,
                           outputs=api_url_dropdown)
    refresh_server_button.click(update_server_list, outputs=server_dropdown)

    def update_api_url_list(server_name):
        list = get_api_url_by_server(server_name)
        return gr.Dropdown(choices=list,interactive=True)

    server_dropdown.select(update_api_url_list, inputs=server_dropdown,
                           outputs=api_url_dropdown)
    refresh_url_button.click(update_api_url_list, inputs=[
                             server_dropdown], outputs=api_url_dropdown)

    def update_method_list(server_name, api_url):
        list = get_method_list(server_name=server_name, api_url=api_url)
        return gr.Dropdown(choices=list,interactive=True)
    
    api_url_dropdown.select(update_method_list, inputs=[
                            server_dropdown, api_url_dropdown], outputs=[method_list_dropdown])
    refresh_method_button.click(update_method_list, inputs=[
                                server_dropdown, api_url_dropdown], outputs=[method_list_dropdown])
    get_apiInfo_button.click(get_api_details, inputs=[
        server_dropdown, api_url_dropdown, method_list_dropdown], outputs=[api_request, api_response])

    def generate_code(server_name, tool, api_url, method,):
        request_response = get_api_request_response(
            server_name, api_url, method)
        request = request_response['request']
        response = request_response['response']
        return gen_contract_test(tool, request, response, api_url, method)

    gen_contract_test_button.click(generate_code, inputs=[
        server_dropdown, tool_dropdown, api_url_dropdown, method_list_dropdown], outputs=[code])
