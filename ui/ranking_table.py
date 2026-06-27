import pandas as pd
import streamlit as st


def render_ranking(ranking):

    st.subheader("🏆 Ranking Global")

    df = pd.DataFrame(ranking)

    df = df.rename(columns={

        "number": "Número",

        "score": "Score",

        "historical_count": "Histórico",

        "recent30": "30",

        "recent100": "100",

        "recent200": "200",

        "last_seen": "Última aparición"

    })

    st.dataframe(

        df,

        use_container_width=True,

        hide_index=True

    )
