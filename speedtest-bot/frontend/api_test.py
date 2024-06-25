import gradio as gr
from backend.apitest.chains import generate_api_test_code
import json
from backend.apitest.base_api import get_server_list, get_api_url_by_server, get_api_request_response, get_api_details, get_method_list
from backend.apitest.import_api import add_api_url,add_server,manual_import_apiInfo,import_swagger_file
import backend.config.configs as configs


def parse_json_to_list(json_obj, parent_key='', separator='.'):
    parsed_list = []
    if isinstance(json_obj, dict):
        for key, value in json_obj.items():
            new_key = f"{parent_key}{separator}{key}" if parent_key else key
            parsed_list += parse_json_to_list(value, new_key, separator)
    elif isinstance(json_obj, list):
        for idx, item in enumerate(json_obj):
            new_key = f"{parent_key}[{idx}]"
            parsed_list += parse_json_to_list(item, new_key, separator)
    else:
        parsed_list.append(parent_key)
    return parsed_list


def generate_code(server_name, api_url, method, language, test_tool, parameterizedFields, value, verifyFields, model_name, apiHeader="contentType:application/json"):
    if not server_name or not api_url or not method or not language or not test_tool:
        return "server name or api url or method or language or test tool must not to be empty or None"
    request_response = get_api_request_response(
        server_name, api_url, method)
    request = request_response['request']
    response = request_response['response']
    return generate_api_test_code(language, test_tool, request, response, parameterizedFields, value, verifyFields, apiHeader,model_name=model_name)

with gr.Blocks() as api_test:
    server_list = get_server_list()
    with gr.Row():
        language_dropdown = gr.Dropdown(
            choices=["Javascript"], label="Language")
        test_tool_dropdown = gr.Dropdown(
            choices=["Jest"], label="Framework")
        model_dropdown = gr.Dropdown(choices=configs.SUPPORT_MODEL_LIST,value=configs.DEFAUT_MODEL,label='LLM',interactive=True)
        with gr.Group():
            refresh_server_button = gr.Button(
                value="Refresh Server", elem_classes="custom_button")
            server_dropdown = gr.Dropdown(
                choices=server_list, show_label=False, interactive=True)
        with gr.Group():
            refresh_url_button = gr.Button(
                value="Refresh URL", elem_classes="custom_button")
            api_url_dropdown = gr.Dropdown(
                choices=[], show_label=False, interactive=True)
        with gr.Group():
            refresh_method_button = gr.Button(
                value="Refresh Method", elem_classes="custom_button")
            method_list_dropdown = gr.Dropdown(
                choices=["GET", "POST", "DELETE", "PUT"], show_label=False)
    with gr.Row():
      with gr.Accordion("API Test", open=True):
        with gr.Row():
         with gr.Column(scale=1):
            with gr.Group():
                get_apiInfo_button = gr.Button(
                    value="Show API Details", elem_classes="custom_button")
                api_request = gr.JSON(
                    label="Api Request")
                api_response = gr.JSON(
                    label="Api Response")
         with gr.Column(scale=1):
            with gr.Group():
                choose_req_fields_button = gr.Button(
                    value="Get Parameterized Fields", elem_classes="custom_button")
                request_checkboxGroup = gr.CheckboxGroup(
                    ["req1", "req2"], interactive=True, show_label=False, info="Choose parameterized fields")
                parameterized_value = gr.TextArea(label="Input parameterized value", lines=3,
                                                  placeholder="Input parameterized value, if no value, will use default value")
         with gr.Column(scale=1):
            with gr.Group():
                choose_res_fields_button = gr.Button(
                    value="Get Verified fields", elem_classes="custom_button")
                response_checkboxGroup = gr.CheckboxGroup(choices=["res1", "res2"], interactive=True,
                                                          show_label=False, info="Choose verified response fields")
                header_input = gr.TextArea(
                    label="Input user-defined headers", lines=3, placeholder="Default header is {content-type:application/json}\nInput header if there is customerized header")
        with gr.Row():
          with gr.Group():
            generate_api_test_button = gr.Button(
                value="Generate API Test", elem_classes="custom_button")
            code = gr.Code(label="API Test Code", language="javascript")
    with gr.Row():        
      with gr.Accordion("Import API", open=False): 
         with gr.Row():       
           with gr.Group():
             add_api_url_button = gr.Button(
                value="Add Api Url", elem_classes="custom_button")
             api_url_textbox = gr.Textbox(
                placeholder="Input url,choose server,method to add", show_label=False)
           with gr.Group():
             add_server_button = gr.Button(
                value="Add Server", elem_classes="custom_button")
             server_textbox = gr.Textbox(
                placeholder="Input server name to add server", show_label=False)
           upload_button = gr.UploadButton(
                "Upload Swagger File", file_types=["json"], elem_classes="custom_button") 
         with gr.Row():
            output_text = gr.Textbox(
                placeholder="show import swagger file result in here", lines=1, show_label=False)
         with gr.Row():  
            manual_import_button = gr.Button(
                    value="Manual Import API Info", elem_classes="custom_button")
         with gr.Row():        
                manual_request_textbox = gr.Textbox(
                    label="API Request", lines=10, max_lines=10)
                manual_response_textbox = gr.Textbox(
                    label="API Response", lines=10, max_lines=10)
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

    def update_req_checkboxGroup(server_name, api_url, method):
        request_response = get_api_request_response(
            server_name, api_url, method)
        list = parse_json_to_list(json.loads(request_response["request"]))
        return gr.CheckboxGroup(choices=list,interactive=True)

    def update_res_checkboxGroup(server_name, api_url, method):
        request_response = get_api_request_response(
            server_name, api_url, method)
        list = parse_json_to_list(json.loads(request_response["response"]))
        return gr.CheckboxGroup(choices=list, interactive=True)

    choose_req_fields_button.click(update_req_checkboxGroup, inputs=[server_dropdown,
                                                                     api_url_dropdown, method_list_dropdown], outputs=[request_checkboxGroup])

    choose_res_fields_button.click(update_res_checkboxGroup, inputs=[server_dropdown,
                                                                     api_url_dropdown, method_list_dropdown], outputs=[response_checkboxGroup])

    generate_api_test_button.click(generate_code, inputs=[
        server_dropdown, api_url_dropdown, method_list_dropdown, language_dropdown, test_tool_dropdown, request_checkboxGroup, parameterized_value, response_checkboxGroup,model_dropdown, header_input], outputs=[code])
    
    add_api_url_button.click(add_api_url, inputs=[
                             server_dropdown, api_url_textbox, method_list_dropdown], outputs=[output_text])

    add_server_button.click(
        add_server, inputs=[server_textbox], outputs=output_text)
    upload_button.upload(import_swagger_file, [server_dropdown, upload_button],
                         outputs=output_text)

    manual_import_button.click(manual_import_apiInfo, inputs=[server_dropdown, api_url_dropdown,
                                                              method_list_dropdown, manual_request_textbox, manual_response_textbox], outputs=output_text)
