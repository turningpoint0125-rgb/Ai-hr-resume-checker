from langchain.chains import LLMChain

from ai.llm import llm
from prompts.skill_prompt import skill_prompt

skill_chain = LLMChain(
    llm=llm,
    prompt=skill_prompt
)

def skill_match(resume_text, jd_text):

    response = skill_chain.run(

        resume=resume_text,

        jd=jd_text

    )

    return response