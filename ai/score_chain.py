from langchain.chains import LLMChain

from ai.llm import llm
from prompts.score_prompt import score_prompt

score_chain = LLMChain(
    llm=llm,
    prompt=score_prompt
)

def match_score(resume_text, jd_text):

    score = score_chain.run(

        resume=resume_text,

        jd=jd_text

    )

    return score