import os
from openai import OpenAI
from backend.integration.prompts import analysis_requirement_prompt, write_test_case_prompt
from zhipuai import ZhipuAI


def generate_message(initial_prompt, chat_history):
    prompt_list = []
    prompt_list.insert(0, {"role": "user", "content": initial_prompt})
    for i in range(0, len(chat_history)-1, 2):
        user_input = chat_history[i]
        assistant_response = chat_history[i + 1]
        prompt_list.append({"role": "user", "content": user_input})
        prompt_list.append(
            {"role": "assistant", "content": assistant_response})
    prompt_list.append({"role": "user", "content": chat_history[-1]})
    return prompt_list


def generate_requirement_analysis_message(chat_history):
    initial_prompt = "prompt=" + analysis_requirement_prompt
    return generate_message(initial_prompt=initial_prompt, chat_history=chat_history)


def generate_write_test_case_message(chat_history):
    initial_prompt = "prompt="+write_test_case_prompt
    return generate_message(initial_prompt=initial_prompt, chat_history=chat_history)


def generate_moonshot_message(chat_history, task_type):
    prompt_list = []
    if task_type == "analysis_requirements":
        prompt_list = generate_requirement_analysis_message(
            chat_history=chat_history)
    if task_type == "write_test_case":
        prompt_list = generate_write_test_case_message(
            chat_history=chat_history)
    prompt_list.insert(
        0, {"role": "system", "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一些涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"})
    return prompt_list


def generate_zhipu_message(chat_history, task_type):
    prompt_list = []
    if task_type == "analysis_requirements":
        prompt_list = generate_requirement_analysis_message(
            chat_history=chat_history)
    if task_type == "write_test_case":
        prompt_list = generate_write_test_case_message(
            chat_history=chat_history)
    return prompt_list


def get_moonshot_stream_response(chat_history, model, task_type):
    prompt_list = generate_moonshot_message(
        chat_history=chat_history, task_type=task_type)
    client = OpenAI(
        api_key=os.getenv("MOONSHOT_API_KEY"),
        base_url=os.getenv("MOONSHOT_BASE_URL")
    )
    response = client.chat.completions.create(
        model=model,
        messages=prompt_list,
        temperature=0.3,
        stream=True,
    )
    return response


def get_zhipu_stream_response(chat_history, model, task_type):
    prompt_list = generate_zhipu_message(
        chat_history=chat_history, task_type=task_type)
    client = ZhipuAI(api_key=os.getenv("ZHIPU_API_KEY"))
    response = client.chat.completions.create(
        model=model,
        messages=prompt_list,
        stream=True,
    )
    return response
