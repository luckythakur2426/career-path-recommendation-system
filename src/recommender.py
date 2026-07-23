from sklearn.metrics.pairwise import cosine_similarity
from src.knowledge_base import KNOWLEDGE_BASE
from src.utils import clean_skill_string

class RecommenderEngine:
    def __init__(self, df, vectorizer_obj):
        self.df = df
        self.vectorizer = vectorizer_obj

    def get_unique_interests(self):
        return sorted(self.df['Interest'].unique().tolist())

    def predict_and_recommend(self, user_skills, user_interest, target_career_override=None):
        user_skill_list = clean_skill_string(user_skills)
        user_skill_set = set(s.lower() for s in user_skill_list)
        query = f"{user_skills} {user_interest}"

        # Calculate Cosine Similarity against Dataset
        user_vec = self.vectorizer.transform(query)
        similarity_scores = cosine_similarity(user_vec, self.vectorizer.matrix).flatten()
        best_match_idx = similarity_scores.argmax()
        predicted_career = self.df.iloc[best_match_idx]['Career']

        # Selected Target Career
        if target_career_override and target_career_override != "Auto-Detect from Dataset":
            target_career = target_career_override
        else:
            target_career = predicted_career

        career_info = KNOWLEDGE_BASE.get(target_career, KNOWLEDGE_BASE["Data Analyst"])

        # Skill Gap Calculation
        missing_skills = [
            skill for skill in career_info["required_skills"]
            if skill.lower() not in user_skill_set
        ]

        return {
            "predicted_career": target_career,
            "match_score": round(float(similarity_scores[best_match_idx]) * 100, 2),
            "missing_skills": missing_skills if missing_skills else ["You have all basic skills!"],
            "courses": career_info["courses"],
            "certifications": career_info["certifications"],
            "projects": career_info["projects"]
        }