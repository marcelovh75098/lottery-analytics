import streamlit as st


def load_theme():

    st.markdown(
        """
        <style>

        .main{
            background:#0f172a;
        }

        .block-container{
            padding-top:2rem;
            padding-bottom:2rem;
            max-width:1600px;
        }

        h1,h2,h3{
            color:white;
        }

        div[data-testid="metric-container"]{

            background:#1e293b;

            border-radius:15px;

            padding:18px;

            border:1px solid #334155;

            box-shadow:0px 2px 10px rgba(0,0,0,.30);
        }

        div[data-testid="stMetricValue"]{

            color:#38bdf8;

            font-size:34px;

        }

        div[data-testid="stMetricLabel"]{

            color:#cbd5e1;

        }

        .small-card{

            background:#1e293b;

            padding:18px;

            border-radius:15px;

            border:1px solid #334155;

            margin-bottom:15px;

        }

        .ticket{

            background:#0369a1;

            padding:20px;

            border-radius:15px;

            text-align:center;

            font-size:26px;

            color:white;

            font-weight:bold;

        }

        .rank{

            background:#111827;

            border-left:6px solid #38bdf8;

            padding:15px;

            margin-bottom:8px;

            border-radius:10px;

            color:white;

        }

        </style>
        """,
        unsafe_allow_html=True
    )
