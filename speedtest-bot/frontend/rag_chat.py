import gradio as gr
from backend.rag.retriever import get_all_file_names, chat, delete_all_file
from backend.rag.loader import save_vector_document
import backend.config.configs as configs


with gr.Blocks() as rag_chat:
    with gr.Row():
        with gr.Column(scale=1):
            chatbot = gr.Chatbot(height=380)
            human_message_textbox = gr.Textbox(interactive=True)
            clear = gr.ClearButton([human_message_textbox, chatbot])
        with gr.Column(scale=1):
            with gr.Row():
                chat_model_dropdown = gr.Dropdown(label="Chat Model", choices=[
                                                  "gpt-3.5-turbo"], value="gpt-3.5-turbo", interactive=True)
                embedding_model_dropdown = gr.Dropdown(
                    label="Embedding Model", choices=["text-embedding-3-small"], value="text-embedding-3-small", interactive=True)
                doc_language_dropdown = gr.Dropdown(
                    label="Doc Language", choices=["English", "Chinese"], value="English")
                chunk_dropdownList = gr.Dropdown(choices=configs.CHUNK_SIZE_LIST,value=configs.DEFAULT_CHUNK_SIZE,label="chunk size",interactive=True)     
                overlap_dropdownList = gr.Dropdown(choices = configs.OVERLAP_SIZE_LIST,value=configs.DEFAULT_OVERLAP_SIZE,label="overlap size",interactive=True)   
            with gr.Row():
                output_text = gr.Text(label="Show Result")
            with gr.Row():
                upload_local_file_button = gr.UploadButton("Upload Local File")
                get_file_list_button = gr.Button(value="Get File List")
                delete_file_button = gr.Button(value="Delete ALL File")
            with gr.Row():
                file_list_checkboxGroup = gr.CheckboxGroup(
                    ["file1", "file2"], interactive=True, show_label=False, info="Choose File List")

        def get_file_list():
            file_list = get_all_file_names()
            return gr.CheckboxGroup(choices=file_list,interactive=True)
        get_file_list_button.click(
            get_file_list, outputs=file_list_checkboxGroup)
        delete_file_button.click(delete_all_file, outputs=output_text)
        human_message_textbox.submit(chat, inputs=[
            human_message_textbox, chatbot, chat_model_dropdown,file_list_checkboxGroup], outputs=[human_message_textbox, chatbot])
        upload_local_file_button.upload(save_vector_document, inputs=[
            upload_local_file_button, doc_language_dropdown, embedding_model_dropdown,chunk_dropdownList,overlap_dropdownList], outputs=output_text)
