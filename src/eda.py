class EDAEngine:
    def __init__(self, df):
        self.df = df

    def get_summary_stats(self):
        return {
            "total_records": len(self.df),
            "total_careers": self.df['Career'].nunique(),
            "total_interests": self.df['Interest'].nunique(),
            "avg_cgpa": round(float(self.df['CGPA'].mean()), 2)
        }

    def get_career_counts(self):
        return self.df['Career'].value_counts()

    def get_interest_counts(self):
        return self.df['Interest'].value_counts()