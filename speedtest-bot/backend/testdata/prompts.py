from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate, HumanMessagePromptTemplate,
)

CSVDATA = """
You are a  data creater, create csv format data base on field name,field type, field range.Below are fields and type. csv data lines is {data_rows}.
```{fields}```
"""
template = "You are a data creater,generate csv format data base on fields and type.Only generate test case, do not generate any explanation"
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = CSVDATA
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
chat_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt])


GENSQL = """
Your task is write sql base on given sql tables and request
```{sql_tables}```

```{user_request}```
"""
sql_tempalte = "You are a sql expert, write sql base on given sql tables and user request, Only generate sql, do not generate any explanation"


sql_system_message_prompt = SystemMessagePromptTemplate.from_template(template)
sql_human_template = GENSQL
sql_human_message_prompt = HumanMessagePromptTemplate.from_template(
    sql_human_template)
sql_chat_prompt = ChatPromptTemplate.from_messages(
    [sql_system_message_prompt, sql_human_message_prompt])

GENCODE = """"
Your task is write code with {language} and {client_tool} base on below given table sql and user_request
```{sql}```

```{user_request}```
"""
code_sql_tempalte = "Wire code to get the data base on given sql , Only generate sql, do not generate any explanation"

code_system_message_prompt = SystemMessagePromptTemplate.from_template(
    code_sql_tempalte)
code_human_template = GENCODE
code_human_message_prompt = HumanMessagePromptTemplate.from_template(
    code_human_template)
code_chat_prompt = ChatPromptTemplate.from_messages(
    [code_system_message_prompt, code_human_message_prompt])
