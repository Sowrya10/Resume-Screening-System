Hiring & Recruitment System using Machine Learning
Project Overview
This project is a Machine Learning-based Resume Screening Application that automates the hiring process by ranking resumes based on job-specific keywords provided by HR.
The system uses Natural Language Processing (NLP) and Random Forest Classification Algorithm to evaluate and rank candidates efficiently, reducing manual screening effort.
Hiring & Recruitment System using Machine Learning

Problem Statement
Manual resume screening is:
Time-consuming
Prone to human bias
Inefficient for large volumes of applications

This system automates resume filtering by:
Matching resumes with HR-defined keywords
Calculating match percentage
Ranking candidates automatically

Features
Resume upload functionality
NLP-based text preprocessing
Keyword matching system
Match percentage calculation
Resume ranking system
Random Forest classification model
Simple UI built using Streamlit

Technologies Used
Python
Natural Language Processing (NLP)
Scikit-learn
Random Forest Algorithm
Pandas & NumPy
Streamlit (Frontend UI)

How It Works (Step-by-Step)
1️⃣ Resume Upload
Candidates upload their resumes in text format.
2️⃣ HR Inputs Required Skills
HR provides required keywords (e.g., Java, SQL, Machine Learning, etc.)
3️⃣ Text Preprocessing (NLP)
Convert text to lowercase
Remove stopwords
Remove punctuation
Tokenization
Feature Extraction
Convert resume text into numerical features using vectorization (TF-IDF or CountVectorizer).
5️⃣ Keyword Matching
System checks presence of HR keywords in resume.
Calculates match percentage.
6️⃣ Classification using Random Forest
Model predicts whether resume is suitable or not.
Output: 0 (Not Suitable) / 1 (Suitable)
7️⃣ Ranking
Resumes are ranked based on:
Match Percentage
Model Prediction

Output Example
| Candidate | Match % | Prediction | Rank |
| --------- | ------- | ---------- | ---- |
| Resume 1  | 85%     | 1          | 1    |
| Resume 2  | 65%     | 1          | 2    |
| Resume 3  | 30%     | 0          | 3    |

Project Structure
Hiring-Recruitment-ML/
│
├── app.py
├── requirements.txt
└── README.md

How to run the project
Step 1: Install Dependencies
pip install -r requirements.txt
Step 2: Run streamlit app
streamlit run app.py
Step 3: Open the browser link shown and upload resumes.

Benefits
Reduces HR workload
Speeds up hiring process
Improves candidate shortlisting accuracy
Scalable for large organizations

Future Enhancements
Resume PDF parsing
Deep Learning-based resume analysis
Skill scoring with weightage
ATS integration
Cloud deployment (AWS)

Author
Sowrya
