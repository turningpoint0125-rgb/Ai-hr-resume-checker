import streamlit as st
import pandas as pd

from utils.pdf_reader import extract_text
from ai.chains import analyze_resume
from components.sidebar import sidebar
from components.ranking import show_ranking

st.set_page_config(
    page_title="AI Recruitment Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

sidebar()

st.title("🤖 AI Recruitment Assistant")

jd_file = st.file_uploader(
    "Upload Job Description (PDF)",
    type="pdf"
)

resume_files = st.file_uploader(
    "Upload Resume(s)",
    type="pdf",
    accept_multiple_files=True
)

if st.button("Analyze Resume"):

    if jd_file is None:
        st.warning("Please upload Job Description.")
        st.stop()

    if not resume_files:
        st.warning("Please upload Resume(s).")
        st.stop()

    jd_text = extract_text(jd_file)

    with st.expander("📄 Job Description Preview"):
        st.text(jd_text[:3000])

    ranking = []

    progress = st.progress(0)
    total = len(resume_files)

    for i, resume in enumerate(resume_files):

        progress.progress((i + 1) / total)

        resume_text = extract_text(resume)

        with st.spinner(f"Analyzing {resume.name}..."):

            try:
                result = analyze_resume(
                    resume_text,
                    jd_text
                )

            except Exception as e:
                st.error(e)
                continue

        st.divider()

        with st.expander(f"👤 {resume.name}", expanded=True):

            st.subheader("Candidate Summary")
            st.info(result["summary"])

            score = result["score"]

            st.subheader("Match Score")

            if score >= 80:
                st.success(f"Excellent Match : {score}%")

            elif score >= 60:
                st.warning(f"Average Match : {score}%")

            else:
                st.error(f"Poor Match : {score}%")

            col1, col2 = st.columns(2)

            with col1:

                st.subheader("Matching Skills")

                for skill in result["matching_skills"]:
                    st.success(skill)

            with col2:

                st.subheader("Missing Skills")

                for skill in result["missing_skills"]:
                    st.error(skill)

            st.subheader("Extra Skills")

            for skill in result["extra_skills"]:
                st.write("✅", skill)

            st.subheader("Recommendation")

            if result["recommendation"] == "Hire":
                st.success(result["recommendation"])

            elif result["recommendation"] == "Interview":
                st.warning(result["recommendation"])

            else:
                st.error(result["recommendation"])

            st.write(result["justification"])

            st.subheader("Interview Questions")

            for q in result["interview_questions"]:
                st.write("•", q)

            with st.expander("Resume Preview"):
                st.text(resume_text[:3000])

        ranking.append({

            "Candidate": resume.name,

            "Score": score,

            "Recommendation": result["recommendation"]

        })

    show_ranking(ranking)

    if not ranking:
        st.warning("No candidates were successfully analyzed, so no statistics are available.")
        st.stop()

    comparison = pd.DataFrame(ranking)

    st.subheader("Dashboard Statistics")

    c1, c2, c3 = st.columns(3)

    c1.metric("Candidates", len(comparison))

    c2.metric("Average Score", round(comparison["Score"].mean(), 2))

    c3.metric("Highest Score", comparison["Score"].max())

    st.subheader("Candidate Score Chart")

    st.bar_chart(
        comparison.set_index("Candidate")["Score"]
    )

    csv = comparison.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇ Download Ranking CSV",
        csv,
        "candidate_ranking.csv",
        "text/csv"
    )

st.markdown("---")
st.caption("Developed using Streamlit + LangChain + Gemini AI")