from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

WRITE_MOBILE_LOCATOR = """
Write mobile UI auto tests using {client_tool} and javascript for {platform} based on the mobile screen layout and given selectors. Generate the locator following few-shot format strictly, do not provide explanatory information.

identified element:
button,a link,input

selectors:
Accessibility ID Selector:
Example: const elem = await $('~my_accessibility_identifier')
For iOS: Use accessibilityIdentifier
For Android: Use android:contentDescription="@string/inspect"

Android UIAutomator Selector (Android Only):
Example: const element = await $(android=$new UiSelector().text("Cancel").className("android.widget.Button"))
Example: const element = await $('android=new UiSelector().resourceId("your_resource_id")')

iOS UIAutomation Locator Selector (iOS Only):
Example: const element = await $(ios=UIATarget.localTarget().frontMostApp().mainWindow().buttons()[0])

iOS XCUITest Predicate Strings and Class Chains Selector (iOS Only):
Example: const element = await $(-ios predicate string:type == 'XCUIElementTypeSwitch' && name CONTAINS 'Allow')
Example: const element = await $(-ios class chain:/XCUIElementTypeCell[name BEGINSWITH "D"]//XCUIElementTypeButton)

Class Name Selector:
For iOS: Use the full name of a UIAutomation class, starting with UIA-. Example: $('UIATextField')
For Android: Use the fully qualified name of a UI Automator class. Example: await $('android.widget.DatePicker')

Class Chain Selector:
For iOS: Example: const element = await $(-ios class chain:**/XCUIElementTypeTextField[name="username"])
For Android: Example: const element = await $('~parentClassName parentIndex=0 ~childClassName childIndex=1')

XPath Selector:
For iOS: Example: const element = await $('//XCUIElementTypeTextView[@name="textContent"]')
For Android: Example: const element = await $('//android.widget.TextView[@text="textContent"]')

Mobile Screen Layout:
```{layout}```

Few-shot:
locators = {{
    locatorName:locator,
    emailInput: $('input[formcontrolname="email"]'),
    passwordInput: $('input[formcontrolname="password"]'),
    signInButton: $('button[type="submit"]')
}}

Write reasonable mobile app UI locators using the provided selectors and guidelines:

1.Review the identified element and analyze the layout of the mobile screen,determine which elements should generate locator.
2.Review the provided selectors and choose the most suitable selector to locate each element, considering the platform (iOS, Android) and whether the selector is intended for iOS-only, Android-only, or both.
3.Review the Few-shot, gnerated locators following few-shot pattern strictly.
"""

template = "You are an mobile ui auto test expert,write reasonable locator base on mobile screen layout and given selector.Generate the locator following few-shot format strictly, do not write explanatory information"
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = WRITE_MOBILE_LOCATOR
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
mobileui_locator_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt])

WRITE_MOBILE_STEP_FUNCTION = """
Write a test function using {client_tool} based on the provided test step description and locators. Do not generate page locators on your own; use the provided ones. Generate the code directly and do not include explanatory information.
locators:
```{locators}```

test step description:
```{test_step_description}```

Few-shot-example of genrated function:
 async signIn() {{
        let user = require('./user.json');
        await locators.emailInput.setValue(user.username);
        await locators.passwordInput.setValue(user.password);
        await locators.signInButton.click();
    }}
"""
template = "You are an mobile ui auto test expert,write test step function with {client_tool} base on locators and test step description. Generate code directly, do not write explanatory information"
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = WRITE_MOBILE_STEP_FUNCTION
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
mobileui_step_function_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt])
