# 🎯 Career Path Recommendation & Prediction System

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Streamlit-1.25%2B-FF4B4B.svg)](https://streamlit.io/)
[![Machine Learning](https://img.shields.io/badge/Scikit--Learn-1.2%2B-F7931E.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An end-to-end Machine Learning and Natural Language Processing (NLP) framework designed to bridge the gap between academic qualifications and industry expectations. The system provides real-time, personalized career track recommendations and predictive insights for engineering and computer science students by evaluating technical skill sets, academic performance (CGPA), domain preferences, and degree streams.

---

## 💡 Executive Summary & Problem Statement

Navigating career choices in modern software engineering and technology domains can be overwhelming due to rapidly shifting skill demands and complex job descriptions. Traditional career advice often relies on broad generalizations rather than empirical skill alignment.

This project solves that challenge by offering a two-pronged solution:
1. **Content-Based Skill Recommendation:** Evaluates candidate technical skills and domain interests against standardized role signatures using NLP techniques (TF-IDF vectorization and Cosine Similarity).
2. **Supervised Career Prediction:** Leverages supervised ensemble learning (Random Forest Classification) to predict suitable career tracks based on holistic profile features (Degree, Branch, CGPA, Work Mode, Age).

---

## 📌 Key System Features

- **Hybrid AI Architecture:** Combines content-based filtering (NLP) and supervised classification models for balanced predictions.
- **Interactive Web Interface:** High-performance Streamlit dashboard (`app.py`) for inputting user profiles and rendering instant career match percentages.
- **Comprehensive EDA Pipelines:** Notebooks containing data distribution plots, skill co-occurrence analyses, and model performance benchmarks.
- **Extensible Knowledge Base:** Configurable rules engine (`src/knowledge_base.py`) mapping technical skill aliases to primary job roles.

---

## 📁 Repository Directory Structure

```text
career-path-recommendation-system/
├── data/
│   └── Raw dataset.xlsx            # Primary dataset containing 10,000 student records
├── notebooks/
│   ├── Codes.ipynb                 # Initial exploratory analysis & data cleaning
│   └── EDA_and_Model_Testing.ipynb # Feature engineering, cross-validation & model evaluation
├── src/
│   ├── recommender.py              # Cosine Similarity recommendation engine logic
│   ├── vectorizer.py               # Text preprocessing and TF-IDF extraction pipeline
│   ├── knowledge_base.py           # Domain mapping rules & skill-to-role definitions
│   └── utils.py                    # Data validation, formatting, and helper scripts
├── app.py                          # Main Streamlit web application entry point
├── requirements.txt                # Dependency specifications
├── Report.docx                     # Detailed project design and technical report
└── Ppt.pptx                        # Presentation slide deck
