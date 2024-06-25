from backend.apitest.mock_chains import write_mapping_file
import gradio as gr
from backend.apitest.base_api import get_api_details, get_api_request_response, get_server_list, get_api_url_by_server, get_method_list
api_methods = ["GET", "POST", "PUT", "DELETE"]


def parse_mapping_rule(choose_rule):
    result = {}
    result["is_map_header"] = "Map Header" in choose_rule
    result["is_map_cookie"] = "Map Cookie" in choose_rule
    result["is_use_regex"] = "Regex Mapping" in choose_rule
    return result


def write_mock_mapping_file(rules, url, method, request, response):
    if not url or not method or not response:
        return f'url or method or response must not be empty or None'
    rule_list = parse_mapping_rule(rules)
    return write_mapping_file(mapping_rule=rule_list, url=url,
                              method=method, request=request, response=response)


with gr.Blocks() as mock_server:
    list = get_server_list()
    with gr.Row(equal_height=True):
        with gr.Column(scale=3):
            with gr.Row():
                tool_dropdown = gr.Dropdown(
                    choices=["WireMock"], label="Tool",value="WireMock")
                with gr.Group():
                    refresh_server_button = gr.Button(
                        value="Refresh Server", elem_classes="custom_button")
                    server_dropdown = gr.Dropdown(
                        choices=list,  interactive=True, show_label=False)
                with gr.Group():
                    refresh_url_button = gr.Button(
                        value="Refresh URL", elem_classes="custom_button")
                    api_url_dropdown = gr.Dropdown(
                        choices=["/api/demo"], show_label=False)
                with gr.Group():
                    refresh_method_button = gr.Button(
                        value="Refresh Method", elem_classes="custom_button")
                    method_list_dropdown = gr.Dropdown(
                        choices=api_methods, show_label=False)
        with gr.Column(scale=1):
            mapping_rule_checkbox = gr.CheckboxGroup(
                ["Header", "Cookie", "Regex"], label="Mapping Rule")
    with gr.Row():
        with gr.Column(scale=1):
            with gr.Group():
                get_apiInfo_button = gr.Button(
                    value="Show API Details", elem_classes="custom_button")
                api_request = gr.Json(
                    label="Api Request")
                api_response = gr.Json(
                    label="Api Response")
        with gr.Column(scale=1):
            with gr.Group():
                gen_mapping_file_button = gr.Button(
                    value="Gen Mapping File", elem_classes="custom_button")
                code = gr.Code(label="Mock Mapping File",
                               language="javascript", lines=10)

    def update_server_list():
        list = get_server_list()
        return gr.Dropdown(choices=list,interactive=True)
    
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

    def generate_mock_file(server_name, api_url, method, mapping_rule):
        request_response = get_api_request_response(
            server_name, api_url, method)
        request = request_response['request']
        response = request_response['response']
        return write_mock_mapping_file(mapping_rule, api_url, method, request, response)

    gen_mapping_file_button.click(generate_mock_file, inputs=[
        server_dropdown, api_url_dropdown, method_list_dropdown, mapping_rule_checkbox], outputs=[code])
