import streamlit as st

from core.bootstrap import initialize_system

from ui.sidebar import render_sidebar

from ui.pages.dashboard import render_dashboard
from ui.pages.analytics import render_analytics
from ui.pages.predictions import render_predictions
from ui.pages.strategies import render_strategies
from ui.pages.simulator import render_simulator
from ui.pages.settings import render_settings


def configure_page():

    st.set_page_config(
        page_title="Lottery Analytics V2",
        page_icon="🎯",
        layout="wide",
        initial_sidebar_state="expanded"
    )


def load_css():

    with open("assets/theme.css", encoding="utf8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


def main():

    configure_page()

    load_css()

    context = initialize_system()

    page = render_sidebar(context)

    if page == "Dashboard":

        render_dashboard(context)

    elif page == "Analítica":

        render_analytics(context)

    elif page == "Predicciones":

        render_predictions(context)

    elif page == "Estrategias":

        render_strategies(context)

    elif page == "Simulador":

        render_simulator(context)

    elif page == "Configuración":

        render_settings(context)


if __name__ == "__main__":

    main()
