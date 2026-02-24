import streamlit as st
import pandas as pd
import numpy as np
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ----------------------------
# Text Cleaning Function
# ----------------------------

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text

# ----------------------------
# Streamlit UI
# ----------------------------

st.title("AI Resume Screening & Ranking System")

st.write("Enter required skills and paste resume to check match score.")

# HR inputs required skills
hr_input = st.text_input("Enter Required Skills (comma separated)")

if hr_input:
    hr_keywords = [word.strip().lower() for word in hr_input.split(",")]
    job_description = " ".join(hr_keywords)

    # Resume input
    resume_text = st.text_area("Paste Resume Content Here")

    if resume_text:

        cleaned_resume = clean_text(resume_text)
        cleaned_job = clean_text(job_description)

        # ----------------------------
        # Keyword Matching Score
        # ----------------------------

        def keyword_match_score(text):
            count = 0
            for word in hr_keywords:
                if word in text:
                    count += 1
            return (count / len(hr_keywords)) * 100

        match_score = keyword_match_score(cleaned_resume)

        # ----------------------------
        # TF-IDF + Cosine Similarity
        # ----------------------------

        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform([cleaned_job, cleaned_resume])

        similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0] * 100

        # ----------------------------
        # Final Score (Weighted)
        # ----------------------------

        final_score = (0.6 * match_score) + (0.4 * similarity_score)

        # Decision Rule
        if final_score >= 50:
            decision = "Selected for Next Round"
        else:
            decision = "Not Selected"

        # ----------------------------
        # Display Results
        # ----------------------------

        st.subheader("Results")

        st.write("Keyword Match Percentage:", round(match_score, 2))
        st.write("Similarity Score:", round(similarity_score, 2))
        st.write("Final Score:", round(final_score, 2))
        st.success(decision)