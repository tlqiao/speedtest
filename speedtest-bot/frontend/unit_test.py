import gradio as gr
from backend.unittest.chains import write_unit_test


def gen_unit_test(test_tool, language, test_type, mock_tool, assert_tool, source_code):
    if not test_tool or not language or not mock_tool or not assert_tool or not source_code:
        return f'test tool or language or mock tool or assert tool or source code must not to be empty or None'
    return write_unit_test(test_tool=test_tool, language=language, test_type=test_type,
                           mock_tool=mock_tool, assert_tool=assert_tool, source_code=source_code)


with gr.Blocks() as unittest:
    with gr.Row():
        language_dropdown = gr.Dropdown(
            label="Language", choices=["Java", "Javascript"], value="Java")
        framework_dropdown = gr.Dropdown(label="Framework", choices=[
                                         "Junit5", "Junit4", "Jest"],value="Junit5")
        test_type_dropdown = gr.Dropdown(label="Test Type", choices=[
            "Unit Test", "Integration Test"],value="Unit Test")
        mock_tool_dropdown = gr.Dropdown(
            label="Mock Tool", choices=["Mockito"])
        assert_tool_dropdown = gr.Dropdown(
            label="Assert Tool", choices=["AssertJ"])
    with gr.Row():
        gen_unit_test_button = gr.Button(
            value="Generate Unit Test", elem_classes="custom_button")
    with gr.Row():
        source_code = gr.Code(language="javascript",
                              label="Source Code", lines=30)
        output_code = gr.Code(language="javascript",
                              label="Unit Test", lines=30)

    gen_unit_test_button.click(gen_unit_test, inputs=[
        framework_dropdown, language_dropdown, test_type_dropdown, mock_tool_dropdown, assert_tool_dropdown, source_code], outputs=[output_code])
