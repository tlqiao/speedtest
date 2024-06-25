from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

WRITE_WEB_LOCATOR = """
Write a reasonable locator with {test_tool} for identified element based on the web page body. 

identified element:
button,a link,input

locator method:
cy.get(selector)
cy.get(selector).contains(content)
cy.get(selector).eq(index)
cy.get(selector).filter(selector)
cy.get(selector).find(selector)
cy.get(selector).first()
cy.get(selector).first(selector)
cy.get(selector).last()
cy.get(selector).last(selector)
cy.get(selector).next(selector)
cy.get(selector).parent()
cy.get(selector).parent(selector)
cy.get(selector).slibings()
cy.get(selector).slibings(selector)
cy.get(selector).shadow()
cy.get(selector).shadow(shadow)

web page body:
web_page is xml format file as following
```{web_page}```

few-shot:
locators = {{
locatorName: locator
commentInput: cy.get('app-article-page form textarea')
submitButton: cy.get('app-article-page form button')
aboutLink : cy.get('.nav').contains('About'),
}}
Write reasonable web app UI locators for identified element using the provided selectors and guidelines:

1.Review the identified element and analyze the layout of the web page,determine which elements should generate locator.
2.Review the provided selectors and choose the most suitable selector to locate identified element
3.Use above locator method,do not make up other locator method.
4.Review the Few-shot, gnerated locators following few-shot pattern strictly.
"""
template = "You are an ui auto test expert,write reasonable locator with {test_tool} base on web page body.Generate the locator following few-shot format strictly, do not generate any explanation"
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = WRITE_WEB_LOCATOR
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
generate_webui_locator_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt])

WRITE_WEB_STEP_FUNCTION = """
Write a test step function using {test_tool} based on the provided test step description. 
Use the provided page locators and do not generate page locators yourself.
Use one function to wrap it.

```{page_locators}```

```{test_step_description}```

few-shot:
function addComment(commentContent){{
   locators.commentInput.type(commentContent);
   locators.submitButton.click();
}}

function shouldAddCommentSuccessfully(commentContent) {{
    locators.commentLabel.should('contain',commentContent)
}}
module.exports={{
   addComment:addComment,
   shouldAddCommentSuccessfully:shouldAddCommentSuccessfully
}};
"""
template = "You are an ui auto test expert,write test step function with {test_tool} base on page locators and test step description. Only Wrap one function,Generate code directly, do not write explanatory information"
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = WRITE_WEB_STEP_FUNCTION
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
generate_webui_step_function_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt])
