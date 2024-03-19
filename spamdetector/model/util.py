from pathlib import Path
from typing import Literal
import joblib
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.feature_extraction.text import CountVectorizer


BAYES_PATH = Path('./model/bayes.joblib')
SVC_PATH = Path('./model/svc.joblib')
VECTORIZER_PATH = Path('./model/vectorizer.joblib')
vectorizer: CountVectorizer = joblib.load(VECTORIZER_PATH)
bayes_model: MultinomialNB = joblib.load(BAYES_PATH)
svc_model: SVC = joblib.load(SVC_PATH)


def predict_bunch(
    messages: list[str], model: Literal['Bayes', 'SVC'] = 'Bayes'
) -> list[int]:
    transformedMessages = vectorizer.transform(messages)
    prediction = (bayes_model if model == 'Bayes' else svc_model).predict(
        transformedMessages
    )
    return prediction


def predict(message: str, model: Literal['Bayes', 'SVC'] = 'Bayes') -> int:
    return predict_bunch([message], model)[0]


if __name__ == "__main__":
    while 1:
        try:
            message = input('Message: ')
            print("Bayes: Spam!" if predict(message, 'Bayes') else "Bayes: Not spam")
            print("SVC: Spam!" if predict(message, 'SVC') else "SVC: Not spam")
        except KeyboardInterrupt:
            break
        except Exception:
            pass
