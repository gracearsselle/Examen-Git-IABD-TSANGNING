import gradio as gr


def hello(name: str) -> str:
    return f"Hello, {name}!"


demo = gr.Interface(
    fn=hello,
    inputs=gr.Textbox(label="Ton prenom"),
    outputs=gr.Textbox(label="Reponse"),
    title="Hello World - BUNEC MLOps",
)

demo.launch()
