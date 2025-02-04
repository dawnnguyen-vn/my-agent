from flask import Flask, Response, request, render_template
from ollama import chat
from vector_store import vector_store

app = Flask(__name__)

@app.route('/chat', methods=['GET'])
def get_chat_page():
    return render_template('index.html')

@app.route('/chat', methods = ['POST'])
def chat_with_agent():
    params = request.json

    user_message = params['message']

    retrieval = retrieval_rag(user_message).page_content
    context = f"Context: {retrieval}"

    content = f"Content: {user_message}"

    prompt = context + content

    def generate():
        stream = chat(
            model='llama3.2:1b',
            messages=[
                {'role': 'user', 'content': prompt}],
            stream=True,
        )
        for chunk in stream:
            if chunk.done is not True:
                yield (chunk.message.content)

    return Response(generate(), content_type="text/plain; charset=utf-8")


def retrieval_rag(search_content: str):
    results = vector_store.similarity_search(search_content, k=1)
    return results[0]