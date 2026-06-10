import pandas as pd
from database.db import insert_draw, init_db


def load_seed():

    init_db()

    df = pd.read_csv("data/baloto_seed.csv")

    inserted = 0

    for _, row in df.iterrows():

        insert_draw(
            row["draw_date"],
            int(row["n1"]),
            int(row["n2"]),
            int(row["n3"]),
            int(row["n4"]),
            int(row["n5"]),
            int(row["superbalota"])
        )

        inserted += 1

    return inserted
