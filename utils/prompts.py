PROMPT = """
You are an Expert HR Recruitment AI.

Compare the Resume with the Job Description.

Return ONLY valid JSON.

{{
    "summary":"Short candidate summary",
    "matching_skills":[
        "Python",
        "SQL"
    ],
    "missing_skills":[
        "Docker",
        "AWS"
    ],
    "extra_skills":[
        "Power BI"
    ],
    "score":90,
    "recommendation":"Hire",
    "justification":"Candidate matches most required skills.",
    "interview_questions":[
        "Explain OOP.",
        "What is TensorFlow?",
        "Difference between CNN and RNN?",
        "Tell me about yourself.",
        "Why should we hire you?"
    ]
}}

Job Description

{jd}

Resume

{resume}
"""