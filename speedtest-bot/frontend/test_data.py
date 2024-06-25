import gradio as gr
from backend.testdata.chains import generate_csv_data, generate_sql, generate_code_from_sql
from backend.testdata.import_table import get_table_schema,import_mysql_tables,get_all_database,get_all_tables,add_database

global_fields = []
global_tables = []

def import_table_schema(db_type,db_name,file):
     if not db_type or not db_name:
          return f'must choose DB Type and DB Name'
     import_mysql_tables(file_path=file.name)
     return "import sql schema file successfully"
     
def clear_tables():
    global global_tables
    global_tables = []
    return ""


def choose_tables(name):
    global_tables.append(name)


def show_tables(name):
    choose_tables(name)
    return ", ".join(global_tables)


def add_field(name, type, range):
    field = {}
    field["name"] = name
    field["type"] = type
    field["range"] = range
    global_fields.append(field)


def clear_fields():
    global global_fields
    global_fields = []
    return ""


def show_fields(name, type, range):
    add_field(name, type, range)
    name_list = []
    for item in global_fields:
        name_list.append(item.get("name"))
    return ", ".join(name_list)


def parse_prompt_fields():
    res = ""
    for item in global_fields:
        if item.get("range") is not None:
            str = item.get("name") + "  " + item.get("type") + \
                " range is " + item.get("range")
        else:
            str = item.get("name") + "  " + item.get("type")
        res = res + str + ','
    return res


def gen_data(data_rows):
    if not global_fields or not data_rows:
        return f'line of data and fields must not to be empty or None'
    field_info = parse_prompt_fields()
    return generate_csv_data(field_info, data_rows=data_rows)


def import_table_schema(db_type,db_name,file):
    if not db_name or not db_type:
        return f'must choose DB Type and DB Name'
    rs =import_mysql_tables(db_type=db_type,db_name=db_name,file_path=file.name)
    return rs


def get_table_schema_info(db_name, tables):
    if not db_name:
         return f'must choose db name'
    if not tables:
        return f'must choose at least one table'
    table_list = [item.strip() for item in tables.split(',')]
    rs =get_table_schema(db_name=db_name,table_list=table_list)
    return rs
    
def add_database_name(db_name):
     if not db_name:
          return f'must choose db name'
     add_database(db_name=db_name)
     return "add db name successfully"


def gen_sql(db_name,tables, user_request):
    if not db_name:
         return f"must choose db name"
    if not tables or not user_request:
        return f"Must choose at least one table and input SQL query natural language"
    table_schem_info=get_table_schema_info(db_name,tables)
    return generate_sql(sql_tables=table_schem_info, user_request=user_request)


def gen_code_base_sql(language, client_tool, sql, user_request):
    if not sql or not user_request or not language or not client_tool:
        return f"Language,client tool, sql must not to be empty"
    return generate_code_from_sql(language=language, client_tool=client_tool, sql=sql, user_request=user_request)


with gr.Blocks() as test_data:
    db_list = get_all_database()
    default_db=db_list[0] if db_list else "no db"
    with gr.Accordion("Gen SQL", open=False):
        with gr.Row():
            db_type_dropdown=gr.Dropdown(label="DB Type",choices=['mysql','postsql'],value="mysql",interactive=True)
            db_dropdown = gr.Dropdown(
                        label="DB Name", choices=db_list,value=default_db, interactive=True)
            table_dropdown = gr.Dropdown(
                        label="Table Name", choices=["table1","table2"], interactive=True)
            language_dropdown = gr.Dropdown(
                    label="Language", choices=["javascript", "python"],interactive=True)
            client_tool_dropdown = gr.Dropdown(
                    label="DB Client Tool", choices=["mysql", "node-postgres", "mssql", "oracledb"],interactive=True)
            with gr.Group():
                 add_db_button=gr.Button(value="Add DBName",elem_classes="custom_button")
                 db_name_text=gr.Textbox(show_label=False)
        with gr.Row():
            refresh_db_button=gr.Button(value="Refresh DB",elem_classes="custom_button")
            import_table_button=gr.UploadButton("Import Table",elem_classes="custom_button")
            choose_table_button = gr.Button(
                    value="Choose Table", elem_classes="custom_button")
            clear_table_button = gr.Button(
                    value="Clear Table", elem_classes="custom_button")
            get_table_schema_button=gr.Button(value="Review Table",elem_classes="custom_button")
            gen_sql_button = gr.Button(
                    value="Gen SQL", elem_classes="custom_button")
            gen_code_button = gr.Button(
                    value="Gen SQL Code", elem_classes="custom_button")
        with gr.Row():
                sql_natural_language_textbox = gr.Textbox(
                    show_label=False, placeholder="Input nanuarl sql language like below\nWrite a SQL query which computes the average total order value for all orders on 2023-04-01.", lines=5, max_lines=5)
                sql_textbox = gr.Textbox(
                    show_label=False, placeholder="Show choosed table and generated sql in here", lines=5, max_lines=5)
        with gr.Row():
                output_text = gr.TextArea(
                    placeholder="Show code and output in here", show_label=False, show_copy_button=True, lines=15, max_lines=15)
    with gr.Accordion("Gen CSV DATA", open=False):        
        with gr.Row():
                clear_fields()
                field_name_textbox = gr.Textbox(label="Field Name")
                field_type_dropdown = gr.Dropdown(label="Field Type", choices=[
                    "string", "number", "boolean", "enum", "date-time"], interactive=True)
                field_range_textbox = gr.Textbox(
                    label="Field Range", placeholder="Optional, Like 10-20", lines=1, max_lines=1)
                lines_textbox = gr.Textbox(label="lines of data")
                add_fields_button = gr.Button(value="Add Fields",
                                              elem_classes="custom_button", min_width=2)
                clear_fields_button = gr.Button(
                    value="Clear Fields", elem_classes="custom_button")
                gen_data_button = gr.Button(
                    value="Gen CSV Data", elem_classes="custom_button")
        with gr.Row():
                show_data_textbox = gr.TextArea(
                    label="Show CSV Data", show_copy_button=True, lines=20, max_lines=20)

        def refresh_database():
            list = get_all_database()
            return gr.Dropdown(choices=list, interactive=True)

        def refresh_table(db_name):
            list = get_all_tables(db_name=db_name)
            return gr.Dropdown(choices=list,interactive=True)
        
        refresh_db_button.click(refresh_database,outputs=[db_dropdown])
        db_dropdown.change(refresh_table, inputs=[
                           db_dropdown], outputs=table_dropdown)
        add_db_button.click(add_database_name,inputs=[db_name_text],outputs=[output_text])
        choose_table_button.click(
            show_tables, inputs=[table_dropdown], outputs=[sql_textbox])
        import_table_button.upload(import_table_schema,inputs=[db_type_dropdown,db_dropdown,import_table_button],outputs=[output_text])
        clear_table_button.click(clear_tables, outputs=[sql_textbox])
        get_table_schema_button.click(get_table_schema_info,inputs=[db_dropdown,sql_textbox],outputs=[output_text])
        gen_sql_button.click(gen_sql, inputs=[
                             db_dropdown,sql_textbox, sql_natural_language_textbox], outputs=[output_text])
        gen_code_button.click(gen_code_base_sql, inputs=[
                              language_dropdown, client_tool_dropdown, sql_textbox, sql_natural_language_textbox], outputs=[output_text])

        def clear_field_type():
            return gr.Dropdown(value="",interactive=True)

        def clear_field_name():
            return gr.Textbox(value="")

        def clear_field_rang():
            return gr.Textbox(value="")

        def add_data_fields(name, type, range):
            return show_fields(name, type, range), clear_field_name(), clear_field_type(), clear_field_rang()
        add_fields_button.click(add_data_fields, inputs=[
            field_name_textbox, field_type_dropdown, field_range_textbox], outputs=[show_data_textbox, field_name_textbox, field_type_dropdown, field_range_textbox])
        clear_fields_button.click(clear_fields, outputs=show_data_textbox)
        gen_data_button.click(
            gen_data, inputs=[lines_textbox], outputs=show_data_textbox)
