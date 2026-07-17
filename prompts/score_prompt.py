from langchain.prompts import PromptTemplate

score_prompt = PromptTemplate(

    input_variables=["resume", "jd"],

    template="""
You are an HR recruiter.

Compare the Resume with the Job Description.

Give only one overall match score.

Return only the percentage.

Resume

{resume}

Job Description

{jd}
"""
)