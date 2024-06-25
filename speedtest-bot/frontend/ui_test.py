import gradio as gr
from backend.database.test_db_manage import TestDBManage
from backend.uitest.web_chains import write_locators_for_web_ui, write_step_function_for_web_ui
import backend.config.configs as configs
from backend.uitest.mobile_chains import write_locator_for_mobile_ui, write_step_function_for_mobile_ui



def get_server_list():
    with TestDBManage(configs.DB_NAME) as db_manager:
        servers = db_manager.get_all_server()
    server_list = [item['serverName'] for item in servers]
    return server_list


def get_page_list(server_name,type):
    with TestDBManage(configs.DB_NAME) as db_manager:
        if type == "Web UI Test":
         page_list = db_manager.get_web_pages_by_server(server_name)
        elif type== "Mobile UI Test": 
         page_list = db_manager.get_mobile_pages_by_server(server_name)  
    return page_list


def add_page(server_name, tool, page_name,platform,type):
    if not server_name or not page_name:
        return f'Server name or page name must not be empty or None'
    with TestDBManage(configs.DB_NAME) as db_manager:
        if type == "Web UI Test":
         db_manager.add_web_page(
            server_name=server_name, tool=tool, page_name=page_name)
        elif type== "Mobile UI Test":
         db_manager.add_mobile_page(
            server_name=server_name, tool=tool, platform=platform, page_name=page_name)
        return f'Add page successfully'


def save_locator(tool, server, page_name, locators,platform,type):
    if not server or not page_name or not locators:
        return f'Server name or page name or locators must not be empty or None'
    with TestDBManage(configs.DB_NAME) as db_manager:
      if type == "Web UI Test":
        db_manager.update_web_ui_locators(
            tool=tool, server_name=server, page_name=page_name, locators=locators)
      elif type== "Mobile UI Test":
        db_manager.update_mobile_ui_locators(
            server_name=server, page_name=page_name, tool=tool, platform=platform, locators=locators)
    return "Update Successfully"


def get_locators(tool, server, page_name,platform, type):
    if not server or not page_name:
        return f'Server name or page name must not be empty or None'
    with TestDBManage(configs.DB_NAME) as db_manager:
        if type == "Web UI Test":
         return db_manager.get_web_locators_by_page(
            tool=tool, server_name=server, page_name=page_name)
        elif type== "Mobile UI Test":
           return db_manager.get_mobile_locators_by_page(
            server_name=server, tool=tool, platform=platform, page_name=page_name)


def gen_locators(tool, page_content,platform,type):
    if not page_content:
        return f'Page content must not to be empty or None'
    if type == "Web UI Test":
     return write_locators_for_web_ui(tool, page_content)
    elif type == "Mobile UI Test":
     return write_locator_for_mobile_ui(client_tool=tool, platform=platform, layout=page_content)  


def gen_ui_test(tool, locators, steps,type,model_name):
    if not locators or not steps:
        return f'locators or ui steps must not be empty or None'
    if type == "Web UI Test":
      return write_step_function_for_web_ui(test_tool=tool, locators=locators, step_scenario=steps,model_name=model_name)
    elif type == "Mobile UI Test":
      return write_step_function_for_mobile_ui(client_tool=tool, locators=locators, step_scenario=steps,model_name=model_name)

with gr.Blocks() as ui_test:
    server_list = get_server_list()
    with gr.Row():
        type_dropdown=gr.Dropdown(choices=["Web UI Test","Mobile UI Test"], value="Web UI Test", label="Type", interactive=True)
        tool_dropdown = gr.Dropdown(
            choices=["Cypress", "Playwright","Appium webdriver"], value="Cypress", label="Tool",interactive=True)
        platform_dropdown= gr.Dropdown(choices=["Android","IOS"], value="Android", label="Platform", interactive=True)
        model_dropdown = gr.Dropdown(choices=configs.SUPPORT_MODEL_LIST,value=configs.DEFAUT_MODEL,label="LLM",interactive=True)
        with gr.Group():
            refresh_server_button = gr.Button(
                value="Refresh Server", elem_classes="custom_button")
            server_dropdown = gr.Dropdown(
                choices=server_list, show_label=False, interactive=True)
        with gr.Group():
            refresh_page_button = gr.Button(
                value="Refresh Page", elem_classes="custom_button")
            page_list_dropdown = gr.Dropdown(choices=["page1"],
                                             show_label=False, interactive=True)
        with gr.Group():
            add_page_button = gr.Button(
                value="Add Page", elem_classes="custom_button")
            page_name_textbox = gr.Textbox(
                placeholder="Input page name", show_label=False)
    with gr.Row(equal_height=True):
        with gr.Column(scale=1):
            page_conent_textbox = gr.TextArea(
                label="Page Content", lines=16, max_lines=16, placeholder="Input page xml file in here when generate lactors")
        with gr.Column(scale=1):
            with gr.Group():
                with gr.Row():
                    show_locator_button = gr.Button(
                        value="Show Locator", elem_classes="custom_button")
                    gen_locator_button = gr.Button(
                        value="Gen Locator", elem_classes="custom_button")
                    save_locator_button = gr.Button(
                        value="Save Locator", elem_classes="custom_button")
                with gr.Row():
                    locators_textbox = gr.TextArea(
                        show_label=False, placeholder="Show locators or output in here", lines=15, max_lines=15)
    with gr.Row():
          gen_ui_code_button = gr.Button(
            value="Gen UI Code", elem_classes="custom_button")
    with gr.Row():
        ui_step_textbox = gr.Textbox(
            label="Input UI Steps", placeholder="Scenario step like this \n Sign-up function\n Input username \n Input email \n Input password \n Click sign up button",  lines=15)
        output_ui_code = gr.Code(
            label="UI Test Code", language="javascript", lines=23)
    def update_tool_dropdown(type):
       if type == "Web UI Test":
         return tool_dropdown.update(value="Cypress")
       elif type == "Mobile UI Test":
          return tool_dropdown.update(value="Appium webdriver")
       
    type_dropdown.select(update_tool_dropdown,inputs=[type_dropdown],outputs=[tool_dropdown])

    def update_server_list_dropdown():
        newList = get_server_list()
        return gr.Dropdown(choices=newList,interactive=True)
    
    refresh_server_button.click(update_server_list_dropdown,
                                outputs=server_dropdown)

    def update_page_list_dropdown(server_name,type):
        newList = get_page_list(server_name,type)
        return gr.Dropdown(choices=newList,interactive=True)

    server_dropdown.select(update_page_list_dropdown, inputs=[server_dropdown,type_dropdown],
                           outputs=page_list_dropdown)

    refresh_page_button.click(update_page_list_dropdown, inputs=[
        server_dropdown,type_dropdown], outputs=page_list_dropdown)

    add_page_button.click(
        add_page, inputs=[server_dropdown, tool_dropdown, page_name_textbox,platform_dropdown,type_dropdown], outputs=locators_textbox)

    gen_locator_button.click(gen_locators,
                             inputs=[tool_dropdown, page_conent_textbox,platform_dropdown,type_dropdown], outputs=locators_textbox)
    save_locator_button.click(save_locator, inputs=[
                              tool_dropdown, server_dropdown, page_list_dropdown, locators_textbox,platform_dropdown,type_dropdown], outputs=[locators_textbox])
    show_locator_button.click(get_locators, inputs=[
                              tool_dropdown, server_dropdown, page_list_dropdown,platform_dropdown,type_dropdown], outputs=[locators_textbox])
    gen_ui_code_button.click(
        gen_ui_test, inputs=[tool_dropdown, locators_textbox, ui_step_textbox,type_dropdown,model_dropdown], outputs=output_ui_code)
