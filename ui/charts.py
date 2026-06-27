import pandas as pd
import plotly.express as px
import streamlit as st


def ranking_chart(ranking):
    """
    Muestra el Top 20 del ranking global.
    """

    df = pd.DataFrame(ranking[:20])

    fig = px.bar(
        df,
        x="number",
        y="score",
        text="score",
        title="🏆 Top 20 Ranking Global",
        labels={
            "number": "Número",
            "score": "Score"
        }
    )

    fig.update_traces(
        texttemplate="%{text:.2f}",
        textposition="outside"
    )

    fig.update_layout(
        height=550,
        xaxis_title="Número",
        yaxis_title="Score",
        showlegend=False
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


def historical_table(ranking):

    df = pd.DataFrame(ranking)

    st.dataframe(

        df,

        use_container_width=True,

        hide_index=True

    )


def top10_cards(ranking):

    st.subheader("⭐ Top 10 Números")

    cols = st.columns(5)

    for i in range(10):

        with cols[i % 5]:

            st.metric(

                f"#{i+1}",

                ranking[i]["number"],

                f'{ranking[i]["score"]:.2f}'

            )
