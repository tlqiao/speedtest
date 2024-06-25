from langchain.prompts.chat import (
    ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate)

api_test_prompt = """
Write an API test using {language} and {test_tool}, following the provided few-shot example. The test should cover the following API context:
API Request: {request}
API Response: {response}
Parameterized Field: {parameterizedFields}
Parameterized Field Value: {parameterizedFieldValue}
API Header: {apiHeader}
Verify Response Fields: {verifyFields}

Additional Rules:
1.When calling any API,use callApiWithToken function which is customerized function.
2.Use Handlebars to manage the API request body. If the parameterized field and value of the request body are not null, generate a Handlebars template using the parameterized field and compile it with the parameterized value.
3.Set the API header to the provided api_header. If api_header is null, use the default header: "Content-Type": "application/json".
4.Extract the specified verify response fields from the API response. If verify response fields are null, verify that the API response code is 200.

callApiWithToken function:
The callApi function provided should be used to make API calls.The input parameter for the function is a JSON object, and within the JSON object, you can set the URL, method, body, and header, where the URL is a required field.

Few-shot example:
//api call code

import callApiWithToken from '../client.js';
import handlebars from "handlebars";

export async function getArticle() {{
    let option = {{
        method: "GET",
        url: '/api/get/articles'
    }}
    return await callApiWithToken(option)
}}

// case code
import getArticle from "../../api/example/articleApiCallExample.js";
describe('article test',() => {{
    it('it should get articles successfully',async() => {{
        const response = await getArticle();
        expect(response.statusCode).toBe(200)
    }})
}})
"""
template = """ You are api test expert, generate api test,do not output any explanation info, only output code  """
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_message = HumanMessagePromptTemplate.from_template(api_test_prompt)
generate_api_test_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message])

api_test_prompt_v2 = """
Write an API test using {language} and {test_tool}, following the provided few-shot example. The test should cover the following API context:
API Request: {request}
API Header: {api_header}

Additional Rules:
1.When calling any API,use callApiWithToken function which is customerized function.
2.Use Handlebars to manage the API request body. If the parameterized field and value of the request body are not null, generate a Handlebars template using the parameterized field and compile it with the parameterized value.
3.Set the API header to the provided api header. If api header is null, use the default header: "Content-Type": "application/json".
4.{test_context}

callApiWithToken function:
The callApi function provided should be used to make API calls.The input parameter for the function is a JSON object, and within the JSON object, you can set the URL, method, body, and header, where the URL is a required field.

Few-shot example:
//api call code

import callApiWithToken from '../client.js';
import handlebars from "handlebars";

export async function getArticle() {{
    let option = {{
        method: "GET",
        url: '/api/get/articles'
    }}
    return await callApiWithToken(option)
}}

// case code
import getArticle from "../../api/example/articleApiCallExample.js";
describe('article test',() => {{
    it('it should get articles successfully',async() => {{
        const response = await getArticle();
        expect(response.statusCode).toBe(200)
    }})
}})
"""

system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_message = HumanMessagePromptTemplate.from_template(api_test_prompt_v2)
generate_api_test_prompt_v2= ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message])
