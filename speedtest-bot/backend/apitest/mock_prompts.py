from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

WRITE_MAPPING_FILE = """
Create a WireMock mapping file that follows the provided rules based on the given API details:

API_URL: {api_url}
API_METHOD: {api_method}
API_REQUEST_BODY: {api_request}
API RESPONSE:{api_response}
IS_MATCH_COOKIE: {is_map_cookie}
IS_MATCH_HEADER: {is_map_header}

Rules:
1.If the API URL contains query parameters, use "matches" and "doesNotMatch" rules to match the API query parameters in the mapping file. If there are no query parameters, the mapping file should not include any query parameter match.
2.If the API request body is not null, use the "equalToJson" rule to match the API request body in the mapping file.
3.If the "IS_MATCH_COOKIE" value is true, use the "cookies contains" rule to match the cookie in the mapping file. If "IS_MATCH_COOKIE" is false, the mapping file should not include any cookie match.
4.If the "IS_MATCH_HEADER" value is true, use the "Content-Type" header with "equalTo" and "caseInsensitive" rules to match the API header in the mapping file. If "IS_MATCH_HEADER" is false, the mapping file should not include any header match.

Please write the WireMock mapping file according to the provided API details and rules mentioned above.
"""


WRITE_MAPPING_FILE_WITH_REGEX = """
Create a WireMock mapping file based on the provided API details and rules. The mapping file should adhere to the following specifications:

API details:
API_URL: {api_url}
API_METHOD: {api_method}
API_REQUEST_BODY: {api_request}
API RESPONSE:{api_response}
IS_MATCH_COOKIE: {is_map_cookie}
IS_MATCH_HEADER: {is_map_header}

rules:
1.Analyze the API URL from the API details. If there are query parameters, use the "matches" and "doesNotMatch" rules to match the API query parameters when generating the WireMock mapping file. If there are no query parameters, the mapping file should not include query parameter matches.
2.Analyze the API request body from the API details. If the request body is not null, use the "matchesJsonPath" rule to match the API request body when generating the WireMock mapping file.
3.Analyze the "IS_MATCH_COOKIE" value from the API details. If "IS_MATCH_COOKIE" is true, use the "cookies contains xxxx" rule to match the cookie when generating the WireMock mapping file. If "IS_MATCH_COOKIE" is false, the mapping file should not include cookie matches.
4.Analyze the "IS_MATCH_HEADER" value from the API details. If "IS_MATCH_HEADER" is true, use the "Content-Type equalTo" rule (with the option to set "caseInsensitive" as true/false) to match the API header when generating the WireMock mapping file. If "IS_MATCH_HEADER" is false, the mapping file should not include header matches.
"""
template = "You are an wiremock expert,write wiremock mapping file, return it with json format, only generate mapping file, do not generate any explanation info"
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = WRITE_MAPPING_FILE
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
generate_mapping_file_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt])

human_template = WRITE_MAPPING_FILE_WITH_REGEX
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
generate_mapping_file_with_regex_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt])
