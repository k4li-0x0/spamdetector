import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('./dataset/dataset.csv', index_col=0)
print(
    f"{(df['label'].value_counts(normalize=True)[1]*100.0):.2f}% of messages are spam"
)

X_train, X_test, y_train, y_test = train_test_split(
    df['message'], df['label'], test_size=0.2
)