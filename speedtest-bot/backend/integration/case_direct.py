import gradio as gr
from backend.integration.llm_adapter import get_moonshot_stream_response, get_zhipu_stream_response


def predict_with_llm(inputs, chat_history, llm, model, task_type):
    chat_history.append(inputs)
    ai_answer = []
    if(llm == "moonshot"):
        response = get_moonshot_stream_response(
            chat_history=chat_history, model=model, task_type=task_type)
    if (llm == "zhipu"):
        response = get_zhipu_stream_response(
            chat_history=chat_history, model=model, task_type=task_type)
    counter = 0
    for chunk in response:
        chunk_message = chunk.choices[0].delta
        if not chunk_message.content:
            continue
        ai_answer.append(chunk_message)
        message = ''.join([m.content for m in ai_answer])
        if counter == 0:
            chat_history.append(" ")
        else:
            chat_history[-1] = message
        chat = [(chat_history[i], chat_history[i + 1]) for i in range(0,
                                                                      len(chat_history) - 1, 2)]
        counter = counter + 1
        yield chat, chat_history


def clear_chat():
    return gr.update(value=''), [], []


def reset_textbox():
    return gr.update(value='')


title = """<h3 align="center">Call LLM API directly without langchain</h3>"""
with gr.Blocks(css="""#col_container {width: 1200px; margin-left: auto; margin-right: auto;}
                # chatbot {height: 1200px; overflow: auto;}""") as case_direct:
    gr.HTML(title)
    with gr.Row():
        llm_list = gr.Dropdown(label="LLM",
                               choices=["moonshot", "zhipu"], value="moonshot", interactive=True)
        model_list = gr.Dropdown(label="Model",
                                 choices=["moonshot-v1-8k","moonshot-v1-32k", "GLM-3-Turbo","GLM-4"], value="moonshot-v1-8k", interactive=True)
        task_list = gr.Dropdown(label="Task", choices=[
            "analysis_requirements", "write_test_case"], value="analysis_requirements", interactive=True)
    with gr.Column(elem_id="col_container"):
        chatbot = gr.Chatbot(elem_id='chatbot', label="ChatBot")
        inputs = gr.Textbox(label="Type an input and press Enter")
        state = gr.State([])
        with gr.Row():
            clear_button = gr.Button(value="Clear")
        with gr.Accordion("Parameters", open=False):
            top_p = gr.Slider(minimum=-0, maximum=1.0, value=0.95, step=0.05,
                              interactive=True, label="Top-p (nucleus sampling)",)
            temperature = gr.Slider(
                minimum=-0, maximum=5.0, value=0.5, step=0.1, interactive=True, label="Temperature",)
            top_k = gr.Slider(minimum=1, maximum=50, value=4,
                              step=1, interactive=True, label="Top-k",)

    inputs.submit(predict_with_llm, inputs=[
                  inputs, state, llm_list, model_list, task_list], outputs=[chatbot, state])
    inputs.submit(reset_textbox, [], [inputs])
    clear_button.click(clear_chat, outputs=[inputs, chatbot, state])
