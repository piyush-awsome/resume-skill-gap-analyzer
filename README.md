🔗 Live Demo
👉 https://resume-skill-gap-analyzer-avcsvuzp8jbpdeiuwdyyey.streamlit.app/

# Resume–Job Skill Gap Analyzer 🚀

A production-style AI application that analyzes how well a resume matches a given job description and highlights skill gaps using semantic similarity.

This project is designed to be **stable, explainable, and cloud-deployable**, making it suitable for real-world hiring and ATS-style use cases.

---

## 🔍 What This App Does

Users can:

- Upload a **resume (PDF)**
- Paste a **job description**
- Instantly get:
  - ✅ Overall match score (%)
  - 📊 Skill coverage
  - ✅ Matched skills
  - ❌ Missing skills
  - 🧠 Resume strength summary

---

## 🧠 How It Works (Technical Overview)

1. **Resume Parsing**

   - Extracts text from PDF using `pypdf`

2. **Text Preprocessing**

   - Cleans and normalizes resume and job description text

3. **Semantic Similarity**

   - Uses `sentence-transformers (all-MiniLM-L6-v2)`
   - Computes cosine similarity between resume and JD embeddings

4. **Skill Gap Analysis**

   - Extracts keywords from resume and JD
   - Compares them using set operations
   - Calculates skill coverage and missing skills

5. **Explainable Output**
   - No generative hallucinations
   - Fully deterministic and transparent logic

---

## 🏗️ Project Structure

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Sentence-Transformers**
- **NumPy**
- **Scikit-learn**
- **PyPDF**

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
python -m streamlit run app.py
```
