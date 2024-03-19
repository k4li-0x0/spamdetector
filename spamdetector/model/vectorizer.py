from pathlib import Path
from dataset import X_test, X_train, y_test, y_train
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib


VECTORIZER_PATH = Path('./model/vectorizer.joblib')
vectorizer = None
if VECTORIZER_PATH.exists():
    print('Loading vectorizer...')
    vectorizer = joblib.load(VECTORIZER_PATH)
    X_train = vectorizer.transform(X_train)
else:
    print('Starting vectorizer fitting...')
    vectorizer = TfidfVectorizer(max_features=1500)
    X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)
