import streamlit as st


def render_system_status(context):

    st.markdown("## ❤️ Estado del Sistema")

    c1,c2,c3,c4 = st.columns(4)

    c1.metric(
        "Base de datos",
        "ONLINE"
    )

    c2.metric(
        "Motor IA",
        "READY"
    )

    c3.metric(
        "Scraper",
        "OK"
    )

    c4.metric(
        "Último sorteo",
        context.metrics["total_draws"]
    )
