from langchain.prompts.chat import (
    ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate)

ASK_QUESTION = """
You are a business analysis expert, review the following business requirement and identify any unclear questions. List all questions without providing answers,Only list questions.

business requirement:
```{requirement}```
"""

ask_question_human_message = HumanMessagePromptTemplate.from_template(
    ASK_QUESTION)
ask_question_prompt = ChatPromptTemplate.from_messages(
    [ask_question_human_message])

SUMMARY_REQUIREMENT = """
You are a business analysis expert, review below business requirement and question answer, Summarize and organize this requirement context,Do not miss any requirments rules.

business requirement
```{requirement}```

requirement question anwser:
```{answer}```
"""

summary_requirement_human_message = HumanMessagePromptTemplate.from_template(
    SUMMARY_REQUIREMENT)
summary_requirement_prompt = ChatPromptTemplate.from_messages(
    [summary_requirement_human_message])


WRITECASES = """
You are test case design expert, analysis below requirement and choose reasonable case design method to write test case base on requirements.

Requirement:
```{requirement}```

Optional test case design methods:
- Boundary Value Analysis
- Equivalence Partitioning
- Cause-Effect Graphing
- State Transition Testing
- Decision Table Testing
- Combinatorial Testing
- Error Guessing
- Random Testing

Write test cases table, table column include CASE NAME GIVEN/WHEN/THEN,provided test data in given column.
"""

write_case_human_message = HumanMessagePromptTemplate.from_template(WRITECASES)
write_case_prompt = ChatPromptTemplate.from_messages(
    [write_case_human_message])

refine_requirements = """
You are a requirements analysis expert. Analyze the raw requirement information below. If there are any unclear rules or details in the requirements, supplement and refine them based on your own knowledge. Finally, compile a new detailed requirements specification information.

raw_requirement
```{raw_requirement}```
"""
refine_requirement_human_message = HumanMessagePromptTemplate.from_template(
    refine_requirements)
refine_requirement_prompt = ChatPromptTemplate.from_messages(
    [refine_requirement_human_message])

correct_requirement = """
You are a requirements analysis expert, tasked with generating a detailed and complete requirements specification document based on user input.

User: Initially provides the raw requirements.
```{raw_requirement}```
You: Refine all detailed rules of the requirements based on the user's raw input. If there are still unclear areas in the user's raw input, supplement them automatically based on your own knowledge.
```{refined_requirement}```
User: Provides feedback on the newly generated requirements, indicating whether modifications are needed and specifying the exact points of modification.
```{user_feedback}```
You: Revise the newly generated requirements specification document based on the user's feedback."
"""

correct_requirement_human_message = HumanMessagePromptTemplate.from_template(
    correct_requirement)
correct_requirement_prompt = ChatPromptTemplate.from_messages(
    [correct_requirement_human_message])

summary_requirement_dialog = """
You are a requirement expert, the following dialog is aimed at the original requirement information, with some corrections and responses from the user. Combining the original requirements and the dialogue information, summarize and organize new, more detailed and accurate business requirements.

dialog:
```{dialog}```
"""

summary_requirement_dialog_human_message = HumanMessagePromptTemplate.from_template(
    summary_requirement_dialog)
summary_requirement_dialog_prompt = ChatPromptTemplate.from_messages(
    [summary_requirement_dialog_human_message])

correct_test_case = """
You are a test case writing expert, tasked with generating detailed and complete test cases based on user input.

User: Initially provides the raw requirements.
```{raw_requirement}```
You: Based on the user's raw requirements, select appropriate test case design methods to write test cases. Test cases are represented in a table format, consisting of four columns: case name, given, when, then.
```{test_case}```
User: Provides feedback on the generated test cases, indicating whether modifications are needed and specifying the exact points of modification.
```{user_feedback}```
You: Revise the test case table based on the user's feedback.
"""

correct_test_case_human_message = HumanMessagePromptTemplate.from_template(
    correct_test_case)
correct_test_case_prompt = ChatPromptTemplate.from_messages(
    [correct_test_case_human_message])

summary_test_case_dialog = """
You are a test case writing expert, the following dialog is aimed at writing test cases for the requirements. The user provides some corrections and responses. Combining the original test cases and the dialogue information, summarize and organize a new, more detailed and accurate test case list.

dialog:
```{dialog}```

Summary test cases table, table column include CASE NAME GIVEN/WHEN/THEN,provided test data in given column.
"""

summary_test_case_dialog_human_message = HumanMessagePromptTemplate.from_template(
    summary_test_case_dialog)
summary_test_case_dialog_prompt = ChatPromptTemplate.from_messages(
    [summary_test_case_dialog_human_message])

devide_requirement= """You are a business analysis expert, analysis below original requirements, then devide original requirement into {feature_number} features, every feature should have Independent Business Value, include  name and  details, details must include all business rules, validation, exception handling and so on.
Write  feature description and details which include as detail as possible. Every details must be greater than 1000 characters.

original requirements:
{original_requirements}
"""

devide_requirement_human_message= HumanMessagePromptTemplate.from_template(devide_requirement)
devide_requirement_prompt= ChatPromptTemplate.from_messages([devide_requirement_human_message])

write_ac= """
You are a test case expert, you review and analysis below business requirements,then write test case base on requirements. The test case should cover both negative and positive scenarios.Write test cases using the GIVEN/WHEN/THEN table format.

requirements:
{requirements}
"""
write_ac_human_message= HumanMessagePromptTemplate.from_template(write_ac)
write_ac_prompt=ChatPromptTemplate.from_messages([write_ac_human_message])


WRITECASES_Backup = """
You are test case design expert, write test case base on requirements, requirements will give api info and call api rules.

Requirements:
```{requirements}```

Test case design methods:
- Boundary Value Analysis
- Equivalence Partitioning
- Cause-Effect Graphing
- State Transition Testing
- Decision Table Testing
- Combinatorial Testing
- Error Guessing
- Random Testing

Few-shot:
Case Name:Call api successfully when otrModelYear is a calendar year
GIVEN
valid otrModelYear that cannot be matched to fsModelYears, and otrModelYear is a calendar year
WHEN
making the API call
THEN
the API should return the otrModelYear as the fsModelYear.api response as below
 {{
 "IsSuccessful": true,
 "Code": 200,
 "Data": [
   {{
     "otrModelYear": "1002",
     "otrChangeYear": null,
     "fsModelYear": 1002
   }}
 ],
 "Message": "Successful."
}}

Write reasonable test cases, Use following format:

Thought: You should always think the requirements and analyze which test case design methods should be used to design the test cases. After confirming the test case design methods, you should evaluate whether the test cases are sufficient and cover both negative and positive scenarios.
Question: the question to ask to clarify the requirement and test case design method
Answer: the answer I responded to the question
... (this Thought/Question/Answer can repeat at least 3 times, at most 10 times)
Thought: I know enough to write all test cases

Tasks: Write test cases using the CASE NAME GIVEN/WHEN/THEN format, following the few-shot example, provided test data value in test case and give expected api response for every test case.
"""
