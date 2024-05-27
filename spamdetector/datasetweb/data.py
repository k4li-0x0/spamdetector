import pandas as pd
from pathlib import Path
from sqlite3 import connect


dataset_path = Path('dataset/messages.csv')
database_path = Path('dataset/messages_labeled.db')
dump_path = Path('dataset/messages_labeled.csv')
if not dataset_path.exists():
    raise FileNotFoundError('Dataset not found')

db_init_required = True if not database_path.exists() else False


df = pd.read_csv(dataset_path)
original_df = df.copy(True)
con = connect(database_path)


if db_init_required:
    with con:
        cur = con.cursor()
        cur.execute(
            "CREATE TABLE labels (id INTEGER PRIMARY KEY, message_id INTEGER, label INTEGER)"
        )
        con.commit()
else:
    with con:
        cur = con.cursor()
        cur.execute("DELETE FROM labels")
        con.commit()


def get_message():
    return df.sample(1).to_dict(orient='records')[0]


def set_label(id, label):
    global df
    with con:
        df = df.drop(df[df['id'] == id].index)
        cur = con.cursor()
        cur.execute(
            "INSERT INTO labels (message_id, label) VALUES (?, ?)",
            (
                id,
                label,
            ),
        )
        con.commit()


def dump_all():
    with con:
        cur = con.cursor()
        result = []

        cur.execute("SELECT message_id, label FROM labels")
        labels = cur.fetchall()
        for label_row in labels:
            index = label_row[0]
            label = label_row[1]
            message_text = original_df.loc[index, 'message']

            result.append(
                (
                    message_text,
                    label,
                )
            )

        pd.DataFrame(result, columns=['message', 'label']).to_csv(dump_path)
