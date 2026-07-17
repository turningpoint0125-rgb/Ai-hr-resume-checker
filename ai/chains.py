from langchain_core.prompts import PromptTemplate
from ai.llm import llm
from utils.prompts import PROMPT
from utils.parser import parse_output

prompt = PromptTemplate(
    input_variables=["resume", "jd"],
    template=PROMPT
)

chain = prompt | llm

def _content_to_text(content):
    """
    Newer Gemini models (3.x) can return response.content as a list of
    content parts instead of a plain string. Normalize either shape
    into a single string so downstream parsing always works.
    """
    if isinstance(content, str):
        return content

    if isinstance(content, list):
        parts = []
        for part in content:
            if isinstance(part, str):
                parts.append(part)
            elif isinstance(part, dict):
                parts.append(part.get("text", ""))
        return "".join(parts)

    return str(content)


def analyze_resume(resume_text, jd_text):

    response = chain.invoke({
        "resume": resume_text,
        "jd": jd_text
    })

    text = _content_to_text(response.content)

    return parse_output(text)