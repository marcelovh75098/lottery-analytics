import streamlit as st


def page_header(
    title: str,
    subtitle: str = ""
):

    st.markdown(
        f"""
        <div style="
            padding:22px;
            border-radius:18px;
            background:linear-gradient(135deg,#2563EB,#1D4ED8);
            margin-bottom:25px;
            box-shadow:0 10px 25px rgba(0,0,0,.35);
        ">

        <h1 style="
            color:white;
            margin:0;
        ">{title}</h1>

        <p style="
            color:#DBEAFE;
            margin-top:8px;
            font-size:16px;
        ">
        {subtitle}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


def info_card(
    title,
    value,
    color="#2563EB"
):

    st.markdown(
        f"""
        <div style="
            background:#1E293B;
            border-left:6px solid {color};
            border-radius:15px;
            padding:18px;
            margin-bottom:15px;
            box-shadow:0 8px 18px rgba(0,0,0,.25);
        ">

        <div style="
            color:#94A3B8;
            font-size:14px;
        ">
        {title}
        </div>

        <div style="
            color:white;
            font-size:34px;
            font-weight:bold;
        ">
        {value}
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


def section(title):

    st.markdown(
        f"""
        <h2 style="
        margin-top:35px;
        margin-bottom:18px;
        color:white;
        ">
        {title}
        </h2>
        """,
        unsafe_allow_html=True
    )


def success_box(message):

    st.markdown(
        f"""
        <div style="
        background:#052E16;
        border-left:5px solid #10B981;
        padding:18px;
        border-radius:12px;
        color:white;
        ">
        {message}
        </div>
        """,
        unsafe_allow_html=True
    )


def warning_box(message):

    st.markdown(
        f"""
        <div style="
        background:#451A03;
        border-left:5px solid #F59E0B;
        padding:18px;
        border-radius:12px;
        color:white;
        ">
        {message}
        </div>
        """,
        unsafe_allow_html=True
    )


def error_box(message):

    st.markdown(
        f"""
        <div style="
        background:#450A0A;
        border-left:5px solid #EF4444;
        padding:18px;
        border-radius:12px;
        color:white;
        ">
        {message}
        </div>
        """,
        unsafe_allow_html=True
    )
