from sklearn.feature_extraction.text import TfidfVectorizer

class TextFeatureVectorizer:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.matrix = None

    def fit_transform(self, df):
        """Combines Skills and Interest into a text vector feature."""
        text_data = df['Skills'].astype(str) + " " + df['Interest'].astype(str)
        self.matrix = self.vectorizer.fit_transform(text_data)
        return self.matrix

    def transform(self, query_text):
        """Transforms user input query into feature vector."""
        return self.vectorizer.transform([query_text])