from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

WRITE_UNIT_TEST = """
Write unit tests using {test_tool} based on the provided source code in {language}. Utilize {mock_tool} to mock the object and {assert_tool} for assertions.

Source code:
```{source_code}```

Please follow these guidelines when writing the unit tests:

1.Perform an analysis of the code using Boundary Value Analysis and Equivalence Partitioning to determine which unit test cases should be added. Make sure to avoid repetition, redundancy, and omission.
2.If the source code is controller code, use Spring's @MockBean to mock the object. Otherwise, use @Mock and @InjectMock to mock the object.
3.If the source code is controller code, use Spring's @WebMvcTest to add unit tests for the controller code.
4.If {test_tool} is JUnit 5, utilize @ParameterizedTest and @ValueSource to write the unit tests.
"""

WRITE_INTEGRATION_TEST = """
Write integration tests using {test_tool} for the given {language} source code. Use {mock_tool} for mocking objects and {assert_tool} for assertions.

Source code:
```{source_code}```

In order to create the integration tests, follow the steps below:

1.Analyze the code using Boundary Value Analysis and Equivalence Partitioning to identify which integration test cases should be added. Ensure there is no repetition, redundancy, or omission in the test cases.
2.If the source code is a controller code, use the Spring @SpringBootTest annotation for testing.
3.If the source code is a repository code and the underlying database is MongoDB, use the Spring @DataMongoTest annotation to add integration tests for the source code.
4.If the source code is a repository code and JPA is used, use the Spring @DataJpaTest annotation to add integration tests for the source code.
5.If the source code calls a third-party API, use the @RestClientTest annotation to add integration tests for the source code.
6.If {test_tool} is JUnit 5, use the @ParameterizedTest and @ValueSource annotations to write unit tests.

few-shot of unit test:
```
@ParameterizedTest
@ValueSource(ints = {{1, 3, 5, -3, 15, Integer.MAX_VALUE}}) 
void isOdd_ShouldReturnTrueForOddNumbers(int number) {{
    assertTrue(Numbers.isOdd(number));
}}
```
Tasks: Write appropriate integration tests based on the above guidelines.
"""
template = "You are an {language} unit and integration test expert,wite unit test base on source code,only generate test code, do not generate any explanation info"
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = WRITE_UNIT_TEST
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
generate_unit_test_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt])

human_template = WRITE_INTEGRATION_TEST
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
generate_integration_test_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt])
