from langchain.chains import LLMChain

from ai.llm import llm

from prompts.summary_prompt import summary_prompt

summary_chain = LLMChain(

    llm=llm,

    prompt=summary_prompt

)


def generate_summary(resume_text):

    return summary_chain.run(

        resume=resume_text

    )