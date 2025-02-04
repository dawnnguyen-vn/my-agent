from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

embeddings = HuggingFaceEmbeddings(
    model_name='dangvantuan/vietnamese-document-embedding', model_kwargs={'trust_remote_code': True}
)

vector_store = Chroma(embedding_function=embeddings, persist_directory="./vector_database")
