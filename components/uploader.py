import streamlit as st

def show_uploaded_files(jd_file, resume_files):

    st.subheader("Uploaded Files")

    if jd_file:
        st.success("Job Description Uploaded Successfully")
        st.write(f"📄 {jd_file.name}")

    if resume_files:

        st.success(f"{len(resume_files)} Resume(s) Uploaded")

        for resume in resume_files:
            st.write(f"📄 {resume.name}")