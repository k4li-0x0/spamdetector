import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt
import joblib
from pathlib import Path


df = pd.read_csv('./dataset/dataset.csv', index_col=0)
print(
    f"{(df['label'].value_counts(normalize=True)[1]*100.0):.2f}% of messages are spam"
)

X_train, X_test, y_train, y_test = train_test_split(
    df['message'], df['label'], test_size=0.2
)

vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train, y_train)

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
joblib.dump(vectorizer, './model/vectorizer.joblib')
joblib.dump(model, './model/model.joblib')

plt.show()
