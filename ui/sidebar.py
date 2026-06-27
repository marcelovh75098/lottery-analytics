import streamlit as st


MENU = {

    "Dashboard":"📊",

    "Analítica":"📈",

    "Predicciones":"🎯",

    "Estrategias":"🧠",

    "Simulador":"🧪",

    "Configuración":"⚙️"

}


def render_sidebar(context):

    with st.sidebar:

        st.image("assets/logo.png", width=90)

        st.title("Lottery Analytics")

        st.caption("Versión 2")

        st.divider()

        option = st.radio(

            "",

            list(MENU.keys()),

            format_func=lambda x:f"{MENU[x]}  {x}"

        )

        st.divider()

        st.metric(

            "Sorteos",

            context.metrics["total_draws"]

        )

        st.metric(

            "Estrategias",

            context.metrics["strategies"]

        )

        st.metric(

            "Predicciones",

            context.metrics["predictions"]

        )

        st.divider()

        st.caption("© Lottery Analytics")

    return option
