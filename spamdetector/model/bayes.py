from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt
import joblib
from pathlib import Path
from vectorizer import *

print('Starting model fitting...')
model = MultinomialNB()
model.fit(X_train, y_train)

print('Checking results...')
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)


table = plt.table(
    colLabels=['Accuracy', 'Precision', 'Recall', 'F1-score'],
    rowLabels=['Bayes'],
    loc='center',
    cellLoc='center',
    colWidths=[0.2, 0.2, 0.2, 0.2],
    rowLoc='center',
    colLoc='center',
    edges='open',
    cellText=[[accuracy, precision, recall, f1]],
)

Path('./model').mkdir(exist_ok=True)
if not VECTORIZER_PATH.exists():
    joblib.dump(vectorizer, './model/vectorizer.joblib')
joblib.dump(model, './model/bayes.joblib')

plt.show()
