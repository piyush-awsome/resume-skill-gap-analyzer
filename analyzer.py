import re
import numpy as np
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text


def extract_keywords(text):
    words = set(re.findall(r"\b[a-z]{3,}\b", text))
    return words


def calculate_match(resume_text, jd_text):
    resume_text = clean_text(resume_text)
    jd_text = clean_text(jd_text)

    resume_emb = model.encode(resume_text, convert_to_tensor=True)
    jd_emb = model.encode(jd_text, convert_to_tensor=True)

    similarity = util.cos_sim(resume_emb, jd_emb).item()
    match_score = round(similarity * 100, 2)

    resume_skills = extract_keywords(resume_text)
    jd_skills = extract_keywords(jd_text)

    matched = sorted(list(resume_skills & jd_skills))
    missing = sorted(list(jd_skills - resume_skills))

    coverage = round((len(matched) / max(len(jd_skills), 1)) * 100, 2)

    return match_score, coverage, matched[:20], missing[:20]
