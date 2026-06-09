import streamlit as st

from database.db import (
    create_database,
    get_total_draws,
    insert_draw
)

from scrapers.baloto_scraper import obtener_ultimo_sorteo

# Crear base de datos al iniciar
create_database()

st.set_page_config(
    page_title="Lottery Analytics",
    page_icon="🎯",
    st.write("VERSION SCRAPER TEST V2"),
    layout="wide"
)

st.title("🎯 Lottery Analytics")

st.markdown("---")

# Botón de prueba del scraper
if st.button("Actualizar datos Baloto"):

    resultado = obtener_ultimo_sorteo()

    st.write(resultado)

total_draws = get_total_draws()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Sorteos Analizados",
        total_draws
    )

with col2:
    st.metric(
        "Números Calientes",
        "Pendiente"
    )

with col3:
    st.metric(
        "Predicción IA",
        "Próximamente"
    )

st.markdown("---")

st.success("Base de datos conectada correctamente")
