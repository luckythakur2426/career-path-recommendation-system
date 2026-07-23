import streamlit as st
from src.utils import load_data
from src.vectorizer import TextFeatureVectorizer
from src.recommender import RecommenderEngine
from src.knowledge_base import KNOWLEDGE_BASE

st.set_page_config(page_title="AI Career Recommender", layout="wide")

@st.cache_resource
def initialize_system():
    df = load_data('data/Raw dataset.xlsx')
    vec = TextFeatureVectorizer()
    vec.fit_transform(df)
    
    rec_engine = RecommenderEngine(df, vec)
    return rec_engine

rec_engine = initialize_system()

# Main Header
st.title("🎓 AI Career & Learning Path Recommendation System")
st.write("Dynamic Career Matching using TF-IDF Natural Language Processing & Cosine Similarity")
st.markdown("---")

# User Inputs
col_input1, col_input2 = st.columns(2)

with col_input1:
    user_skills_in = st.text_input("Enter Your Skills (comma-separated):", "Python, SQL")
    user_interest_in = st.selectbox("Select Primary Interest:", rec_engine.get_unique_interests())

with col_input2:
    user_cgpa_in = st.number_input("Enter Your CGPA:", min_value=0.0, max_value=10.0, value=8.0, step=0.1)
    career_options = ["Auto-Detect from Dataset"] + sorted(list(KNOWLEDGE_BASE.keys()))
    target_career_in = st.selectbox("Preferred Target Goal (Optional):", career_options)

# Recommendation Logic Execution
if st.button("Generate Recommendations 🚀"):
    res = rec_engine.predict_and_recommend(
        user_skills=user_skills_in,
        user_interest=user_interest_in,
        target_career_override=target_career_in
    )

    st.markdown("---")
    st.success(f"🎯 **Target Domain:** {res['predicted_career']} (Similarity Score: {res['match_score']}%)")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🔴 Recommended Skills to Learn (Skill Gap)")
        for skill in res['missing_skills']:
            st.write(f"- {skill}")

        st.subheader("🏆 Recommended Certifications")
        for cert in res['certifications']:
            st.write(f"- {cert}")

    with col2:
        st.subheader("📖 Recommended Courses (Coursera / Udemy / CampusX)")
        for course in res['courses']:
            st.write(f"- {course}")

        st.subheader("⚡ Recommended Projects")
        for project in res['projects']:
            st.write(f"- {project}")