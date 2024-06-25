from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

WRITE_CONTRACT_TEST = """
Create a consumer contract test using {test_tool}, utilizing the provided API details.
 Your task is to analyze the API request body and response and determine the appropriate match rule to be used. 
 Only use the match rules listed in the "MATCH RULES" section. Assume that the contract file will be uploaded to a Pact Broker.

API Details:
API URL: {api_url}
API METHOD: {api_method}
API REQUEST BODY: {api_request}
API RESPONSE:{api_response}

MATCH RULES:
like
eachLike
atLeastOneLike
atLeastLike
atMostLike
boolean
integer
decimal	
number
string
timestamp
time
date
includes
"""
template = "You are an contract test expert,wite contract test with {test_tool}. Do not output any explanation info, only output code"
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = WRITE_CONTRACT_TEST
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
generate_contract_test_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt])
