import streamlit as st
import os

from parser import extract_text_from_pdf
from analyzer import calculate_match

st.set_page_config(page_title="Resume Skill Gap Analyzer")

st.title("📄 Resume–Job Skill Gap Analyzer")
st.write("Upload your resume and compare it with a job description")

uploaded_resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description", height=200)

if uploaded_resume and job_description:
    os.makedirs("data", exist_ok=True)
    resume_path = "data/resume.pdf"

    with open(resume_path, "wb") as f:
        f.write(uploaded_resume.read())

    with st.spinner("Analyzing resume..."):
        resume_text = extract_text_from_pdf(resume_path)

    with st.spinner("Comparing with job description..."):
        match_score, coverage, matched, missing = calculate_match(
            resume_text, job_description
        )

    st.subheader("📊 Match Score")
    st.progress(min(match_score / 100, 1.0))
    st.write(f"**Overall Match:** {match_score}%")
    st.write(f"**Skill Coverage:** {coverage}%")

    st.subheader("✅ Matched Skills")
    st.write(", ".join(matched) if matched else "No strong matches found")

    st.subheader("❌ Missing Skills")
    st.write(", ".join(missing) if missing else "No major skill gaps detected")

    st.subheader("🧠 Resume Strength Summary")
    if match_score >= 75:
        st.success("Strong alignment with job requirements")
    elif match_score >= 50:
        st.warning("Moderate alignment – some upskilling required")
    else:
        st.error("Low alignment – significant skill gaps found")
