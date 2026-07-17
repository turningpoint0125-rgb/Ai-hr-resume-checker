from langchain.prompts import PromptTemplate

summary_prompt = PromptTemplate(

    input_variables=["resume"],

    template="""

You are an HR Recruitment Assistant.

Read the resume carefully.

Extract only the following information.

Candidate Summary

Education

Years of Experience

Technical Skills

Projects

Certifications

Achievements

Return only clean text.

Resume

{resume}

"""

)