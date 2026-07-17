from langchain.prompts import PromptTemplate

skill_prompt = PromptTemplate(

    input_variables=["resume", "jd"],

    template="""
You are an expert HR recruiter.

Compare the following Resume with the Job Description.

Return the output in this format only.

Matching Skills:
- skill1
- skill2

Missing Skills:
- skill1
- skill2

Extra Skills:
- skill1
- skill2

Resume:
{resume}

Job Description:
{jd}
"""
)