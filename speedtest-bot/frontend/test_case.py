import gradio as gr
from backend.rag.retriever import  get_all_file_names, delete_all_file, query_question
from backend.rag.loader import save_vector_document
from backend.testcase.chains import ask_question_stream, summary_requirements_stream, write_case_stream, summary_requirement_dialog_stream, summary_test_case_dialog_stream, correct_requirement_stream, correct_test_case_stream, refine_requirement_stream
import backend.config.configs as configs

def summary_chat(task_type, chat_history,model_name):
    chat_history.append("Following content is summarized by AI")
    if task_type.lower() == "requirement clarification":
        response = summary_requirement_dialog_stream(dialog_list=chat_history,model_name=model_name)
    if task_type.lower() == "write case":
        response = summary_test_case_dialog_stream(dialog_list=chat_history,model_name=model_name)
    ai_answer = []
    counter = 0
    for chunk in response:
        if not chunk:
            continue
        ai_answer.append(chunk)
        message = ''.join([m for m in ai_answer])
        if counter == 0:
            chat_history.append(" ")
        else:
            chat_history[-1] = message
        chat = [(chat_history[i], chat_history[i + 1]) for i in range(0,
                                                                      len(chat_history) - 1, 2)]
        counter = counter + 1
        yield "",chat, chat_history     

     
def chat(task_type, user_input, chat_history,model_name):
    chat_history.append(user_input)
    if task_type.lower() == "requirement clarification":
        if len(chat_history) == 1:
            response=refine_requirement_stream(raw_requirement=user_input,model_name=model_name)
        if len(chat_history) >= 3:
         raw_requirement = chat_history[0]
         refined_requirement = chat_history[-2]
         user_feedback = chat_history[-1]
         response = correct_requirement_stream(raw_requirement=raw_requirement,refined_requirement=refined_requirement, user_feedback=user_feedback,model_name=model_name)   
    if task_type.lower() == "write case":
       if len(chat_history) == 1:
           response = write_case_stream(requirement=user_input,model_name=model_name)
       if len(chat_history) >= 3:
           raw_requirement = chat_history[0]
           test_case = chat_history[-2]
           user_feedback = chat_history[-1]
           response = correct_test_case_stream(raw_requirement=raw_requirement,
                                   test_case=test_case, user_feedback=user_feedback,model_name=model_name)
    ai_answer = []
    counter = 0
    for chunk in response:
        if not chunk:
            continue
        ai_answer.append(chunk)
        message = ''.join([m for m in ai_answer])
        if counter == 0:
            chat_history.append(" ")
        else:
            chat_history[-1] = message
        chat = [(chat_history[i], chat_history[i + 1]) for i in range(0,
                                                                      len(chat_history) - 1, 2)]
        counter = counter + 1
        yield "",chat, chat_history       

def task_stream_process(task_type, input,output, model_name,file_list):
    task_functions = {
        "Ask Question": lambda:ask_question_stream(requirement=input,model_name=model_name),
        "Query Question": lambda:query_question(question=output,model_name=model_name,file_name_list=file_list),
        "Summary Requirement": lambda:summary_requirements_stream(requirement=input,question_answer=output,model_name=model_name),
        "Write Case": lambda:write_case_stream(requirement=output,model_name=model_name)
    }
    if task_type in task_functions:
        response = task_functions[task_type]()
    else:
        raise ValueError("Unsupported task type:", task_type)      
    ai_answer = []
    for chunk in response:
        if not chunk:
            continue
        ai_answer.append(chunk)
        message = ''.join([m for m in ai_answer])  
        yield message   

def clear_chat():
    return gr.update(value=''), [], []


with gr.Blocks() as test_case:
    with gr.Row():
         task_dropdownList = gr.Dropdown(choices=[
                                                "Requirement Clarification", "Write Case"], value="Requirement Clarification",interactive=True, show_label=False)
         chat_model_dropdownList=gr.Dropdown(choices=configs.SUPPORT_MODEL_LIST,value=configs.DEFAUT_MODEL,show_label=False,interactive=True)
         language_dropdownList=gr.Dropdown(choices=['English','Chinese'],value='English',interactive=True,show_label=False)
    with gr.Row():
                chatbot = gr.Chatbot(height=300)
                state = gr.State([])
    with gr.Row():
                human_message_textbox = gr.Textbox(interactive=True,label="User Input")
    with gr.Row():
                clear_button = gr.ClearButton([human_message_textbox, chatbot])
                finish_button = gr.Button(value="Summary")
    with gr.Row():
      with gr.Accordion("Requirement Analysis by RAG", open=False):
        with gr.Row():
             with gr.Column(scale=1):
               with gr.Row():
                 model_dropdown= gr.Dropdown(choices=configs.SUPPORT_MODEL_LIST,value=configs.DEFAUT_MODEL,show_label=False,interactive=True)
                 language_dropdown=gr.Dropdown(choices=['English'],value='English',show_label=False,interactive=True)
                 run_task_button = gr.Button(value="Run Task")
               with gr.Row():
                  task_type_radio_list=gr.Radio(["Ask Question","Query Question","Summary Requirement","Write Case"],show_label=False)   
               with gr.Row():
                 input_textbox = gr.TextArea( lines=10, max_lines=10,placeholder="Input original requirement in here",show_label=False)
               with gr.Row():
                 output_textbox = gr.TextArea(lines=10, max_lines=10,placeholder="Choose file if run 'Query Question' task",show_label=False)
             with gr.Column(scale=1):
                with gr.Row():
                        title = """<h3 align="center">Upload and Search file</h3>"""
                        gr.HTML(title)
                with gr.Row():        
                        ebedding_model_dropdownList = gr.Dropdown(
                            choices=configs.SUPPORT_EMBDDING_MODEL_LIST, value=configs.DEFAULT_EMBEDDING_MODEL, label="embedding model", interactive=True)
                        chunk_dropdownList = gr.Dropdown(choices=configs.CHUNK_SIZE_LIST,value=configs.DEFAULT_CHUNK_SIZE,label="chunk size",interactive=True)     
                        overlap_dropdownList = gr.Dropdown(choices = configs.OVERLAP_SIZE_LIST,value=configs.DEFAULT_OVERLAP_SIZE,label="overlap size",interactive=True)   
                with gr.Row():
                        upload_local_file_button = gr.UploadButton(
                            "Upload")
                        get_file_list_button = gr.Button(value="Choose")
                        delete_file_button = gr.Button(value="Delete")
                with gr.Row():
                        file_list_checkboxGroup = gr.CheckboxGroup(
                            ["file1", "file2"], interactive=True, show_label=False, info="Choose File List")
                with gr.Row():
                        result_textbox = gr.Textbox(placeholder="show result in here",show_label=False)        

        def get_file_list():
            file_list = get_all_file_names()
            return gr.CheckboxGroup(choices=file_list,interactive=True)
        get_file_list_button.click(
            get_file_list, outputs=file_list_checkboxGroup)
        delete_file_button.click(delete_all_file, outputs=output_textbox)
        run_task_button.click(task_stream_process, inputs=[task_type_radio_list,
                                  input_textbox,output_textbox,chat_model_dropdownList,file_list_checkboxGroup], outputs=[output_textbox])
        upload_local_file_button.upload(save_vector_document, inputs=[
            upload_local_file_button, language_dropdown, ebedding_model_dropdownList,chunk_dropdownList,overlap_dropdownList], outputs=result_textbox)
        human_message_textbox.submit(chat, inputs=[task_dropdownList,human_message_textbox, state,chat_model_dropdownList], outputs=[human_message_textbox, chatbot, state])
        finish_button.click(summary_chat, inputs=[
                            task_dropdownList, state,chat_model_dropdownList], outputs=[human_message_textbox, chatbot, state])
        clear_button.click(clear_chat, outputs=[
                           human_message_textbox, chatbot, state])
