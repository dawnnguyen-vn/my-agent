from flask import Flask, Response
from ollama import chat

app = Flask(__name__)


@app.route("/chat")
def hello_world():
    def generate():
        stream = chat(
            model='qwen2.5:0.5b',
            messages=[
                {'role': 'user', 'content': 'Ai là người thông minh nhất?'}],
            stream=True,
        )
        for chunk in stream:
            if chunk.done is not True:
                yield (chunk.message.content)

    return Response(generate(), content_type="text/plain; charset=utf-8")
