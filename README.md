# 🎯 Career Path Recommendation & Prediction System

An end-to-end Machine Learning and NLP-based application that recommends optimal career roles and predicts potential job pathways for students based on their technical skills, academic performance, field of study, and personal preferences.

---

## 📌 Features

- **Personalized Recommendation:** Utilizes Content-Based Filtering with TF-IDF Vectorization and Cosine Similarity to align candidate skill sets with industry roles.
- **Predictive Modeling:** Employs Supervised Machine Learning (e.g., Random Forest Classifier) to predict suitable career tracks based on academic metrics (CGPA, Education level, Branch) and work preferences.
- **Interactive Web Interface:** Built with Streamlit (`app.py`) for seamless profile input and real-time visualization of career suggestions.
- **Data-Driven Insights:** Comprehensive Exploratory Data Analysis (EDA) uncovering key relationships between academic branch, CGPA, technical skills, and target roles.

---

## 📁 Repository Structure

```text
├── data/                    # Dataset directory
│   └── Raw dataset.xlsx     # Dataset containing 10,000 student records
├── notebooks/               # Jupyter Notebooks for experimentation
│   ├── Codes.ipynb          # Exploratory Data Analysis & initial logic
│   └── EDA_and_Model_Testing.ipynb # Feature engineering & model evaluations
├── src/                     # Source modules for core functional logic
│   ├── recommender.py       # Recommendation engine (Cosine Similarity)
│   ├── vectorizer.py        # TF-IDF text feature extraction
│   ├── knowledge_base.py    # Career & domain mapping rules
│   └── utils.py             # Data processing & helper utilities
├── app.py                   # Streamlit web application entry point
├── requirements.txt         # Project dependencies
├── Report.docx              # Project documentation report
└── Ppt.pptx                 # Project presentation deck
