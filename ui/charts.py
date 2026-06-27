import plotly.express as px
import pandas as pd


def frequency_chart(df):

    fig = px.bar(
        df,
        x="numero",
        y="frecuencia",
        text="frecuencia"
    )

    fig.update_layout(
        template="plotly_dark",
        height=420,
        margin=dict(l=10, r=10, t=30, b=10),
        paper_bgcolor="#0F172A",
        plot_bgcolor="#0F172A"
    )

    return fig


def hot_numbers_chart(df):

    fig = px.scatter(
        df,
        x="numero",
        y="score",
        size="score",
        color="score",
        template="plotly_dark",
        height=420
    )

    fig.update_layout(
        paper_bgcolor="#0F172A",
        plot_bgcolor="#0F172A"
    )

    return fig


def parity_chart(data):

    fig = px.pie(
        names=["Pares","Impares"],
        values=data,
        hole=.65
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0F172A"
    )

    return fig
