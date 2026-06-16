import gradio as gr


def hello(name: str) -> str:
    return f"Hello, {name}!"


demo = gr.Interface(
    fn=hello,
    inputs=gr.Textbox(label="Ton prénom"),
    outputs=gr.Textbox(label="Réponse"),
    title="Hello World - BUNEC MLOps",
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0")
