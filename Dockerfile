FROM python:3.10.16-bookworm

RUN curl -fsSL https://ollama.com/install.sh | sh

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

RUN nohup bash -c "ollama serve &" && sleep 3 && ollama pull qwen2.5:0.5b

COPY ./entrypoint.sh .

RUN chmod +x entrypoint.sh

COPY ./main.py .

ENTRYPOINT [ "sh", "entrypoint.sh" ]