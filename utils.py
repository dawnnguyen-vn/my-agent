from typing import List
from io import StringIO
import re
from markdown import Markdown
from langchain_core.documents import Document

def __unmark_element(element, stream=None):
    if stream is None:
        stream = StringIO()
    if element.text:
        stream.write(element.text)
    for sub in element:
        __unmark_element(sub, stream)
    if element.tail:
        stream.write(element.tail)
    return stream.getvalue()

def markdown_to_text(md_text: str) -> str:
    Markdown.output_formats["plain"] = __unmark_element
    __md = Markdown(output_format="plain")
    __md.stripTopLevelTags = False
    plain = __md.convert(md_text)
    plain = re.sub(r'\n+', '\n', plain)
    plain = re.sub('-', '', plain)
    plain = re.sub(':', '', plain)
    plain = re.sub(',', '', plain)
    plain = re.sub(r'\(', '', plain)
    plain = re.sub(r'\)', '', plain)
    plain = re.sub(r'\[', '', plain)
    plain = re.sub(r'\]', '', plain)
    return plain

def format_page_content(docs: List[Document]) -> List[Document]:
    for doc in docs:
        doc.page_content = markdown_to_text(doc.page_content)
    return docs