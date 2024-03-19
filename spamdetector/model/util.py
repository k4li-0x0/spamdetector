from pathlib import Path
import joblib
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer


MODEL_PATH = Path('./model/model.joblib')
VECTORIZER_PATH = Path('./model/vectorizer.joblib')
vectorizer: CountVectorizer = joblib.load(VECTORIZER_PATH)
model: MultinomialNB = joblib.load(MODEL_PATH)

if __name__ == "__main__":
    while 1:
        try:
            transformedMessage = vectorizer.transform([input()])
            prediction = model.predict(transformedMessage)
            print(prediction)
        except Exception:
            pass
