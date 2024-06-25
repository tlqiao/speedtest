### speedtest是一系列工具的组合，这些工具主要是利用LLM提升测试任务效率

- **speedtest-bot：** speedtest工具的核心，以接口方式提供各种AI辅助测试能力，同时，有简单的UI界面，UI界面使用gradio构建
- **speedtest-autotest-plugin：** 用于编写apitest和uitest的一款vscode 插件
- **speedtest-locator-plugin：** 浏览器插件，调用speedtest-bot的接口，基于页面内容生成ui test的locators
