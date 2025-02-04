from langchain_community.document_loaders import DirectoryLoader, TextLoader
from utils import format_page_content
from vector_store import vector_store

text_loader_kwargs = {"autodetect_encoding": True}
loader = DirectoryLoader("./data", glob="*.md", loader_cls=TextLoader, loader_kwargs=text_loader_kwargs)
raw_docs = loader.load()
docs = format_page_content(raw_docs)
vector_store.add_documents(docs)
print("Success!")