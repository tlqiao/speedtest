import gradio as gr

with gr.Blocks() as about:
    gr.Markdown(
        """
# SpeedTest Bot, which utilizes GenAI, serves as an accelerator for software testing tasks.

**Benefits:**

* Enhanced efficiency in writing test cases

* Improved efficiency in writing automated test code

* Increased efficiency in building test data

* Enhanced efficiency in isolating dependencies

**More:**

Here's a [demo](https://www.bilibili.com/video/BV1zC4y1i7VG/) to demonstrate how to use SpeedTest Bot for improving testing efficiency

        """, elem_id="custom_markdown"
    )
