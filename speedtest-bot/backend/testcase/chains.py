from backend.testcase.prompts_en import ask_question_prompt, summary_requirement_prompt, write_case_prompt, summary_requirement_dialog_prompt, summary_test_case_dialog_prompt, correct_requirement_prompt, correct_test_case_prompt, refine_requirement_prompt,devide_requirement_prompt,write_ac_prompt
from backend.config.configs import DEFAUT_MODEL
from backend.base.init_model import init_model
from langchain_core.output_parsers import StrOutputParser

output_parser = StrOutputParser()
def ask_question_stream(requirement,model_name=DEFAUT_MODEL):
    llm = init_model(model_name=model_name)
    chain = ask_question_prompt | llm | output_parser
    return chain.stream({'requirement':requirement})


def summary_requirements_stream(requirement, question_answer,model_name=DEFAUT_MODEL):
    llm = init_model(model_name=model_name)
    chain = summary_requirement_prompt | llm | output_parser
    return chain.stream({'requirement': requirement,'answer': question_answer})


def write_case_stream(requirement,model_name=DEFAUT_MODEL):
    llm=init_model(model_name=model_name)
    chain = write_case_prompt | llm | output_parser
    return chain.stream({"requirement": requirement})

def write_case(requirement,model_name=DEFAUT_MODEL):
    llm=init_model(model_name=model_name)
    chain=write_case_prompt | llm | output_parser
    return chain.invoke({"requirement": requirement})


def refine_requirement_stream(raw_requirement,model_name=DEFAUT_MODEL):
    llm=init_model(model_name=model_name)
    chain = refine_requirement_prompt | llm | output_parser
    return chain.stream({"raw_requirement":raw_requirement})


def correct_requirement_stream(raw_requirement, refined_requirement, user_feedback,model_name=DEFAUT_MODEL):
    llm=init_model(model_name=model_name)
    chain=correct_requirement_prompt | llm | output_parser
    return chain.stream({"raw_requirement":raw_requirement,
                          "refined_requirement":refined_requirement, "user_feedback":user_feedback})


def correct_test_case_stream(raw_requirement, test_case, user_feedback,model_name=DEFAUT_MODEL):
    llm=init_model(model_name=model_name)
    chain=correct_test_case_prompt | llm |output_parser
    return chain.stream({"raw_requirement": raw_requirement,"test_case":test_case,"user_feedback":user_feedback})


def summary_requirement_dialog_stream(dialog_list,model_name=DEFAUT_MODEL):
    llm=init_model(model_name=model_name)
    chain=summary_requirement_dialog_prompt | llm | output_parser
    return chain.stream({"dialog":dialog_list})


def summary_test_case_dialog_stream(dialog_list,model_name=DEFAUT_MODEL):
    llm=init_model(model_name=model_name)
    chain=summary_test_case_dialog_prompt | llm | output_parser
    return chain.stream({"dialog": dialog_list})


def devide_requirments(original_requirements, feature_number, model_name=DEFAUT_MODEL):
  llm = init_model(model_name=model_name)
  chain = devide_requirement_prompt | llm | output_parser
  result = chain.invoke({"original_requirements": original_requirements,"feature_number":feature_number})
  features = result.split("Feature ")[1:]
  return features


def write_ac_stream(requirements, model_name=DEFAUT_MODEL):
    llm = init_model(model_name=model_name)
    chain = write_ac_prompt | llm | output_parser
    return chain.stream({"requirements": requirements})
