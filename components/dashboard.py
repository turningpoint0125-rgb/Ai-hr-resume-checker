import streamlit as st

from components.uploader import show_uploaded_files
from utils.pdf_reader import extract_text
from utils.text_cleaner import clean_text

from ai.summary_chain import generate_summary
from ai.skill_match_chain import skill_match
from ai.score_chain import match_score


def dashboard(jd_file, resume_files):

    st.header("Resume Screening Dashboard")

    show_uploaded_files(jd_file, resume_files)

    st.markdown("---")

    if st.button("Analyze Resume"):

        if jd_file is None:
            st.error("Please upload Job Description")
            return

        if not resume_files:
            st.error("Please upload Resume")
            return

        jd_text = clean_text(extract_text(jd_file))

        for resume in resume_files:

            resume_text = clean_text(extract_text(resume))

            st.subheader(resume.name)

            summary = generate_summary(resume_text)
            st.write(summary)

            st.subheader("Skill Match")
            st.write(skill_match(resume_text, jd_text))

            st.subheader("Match Score")
            st.metric("Score", match_score(resume_text, jd_text))

            st.markdown("---")stra