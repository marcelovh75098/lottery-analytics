import streamlit as st
from database.db import get_total_draws

st.set_page_config(
    page_title="Lottery Analytics",
    page_icon="🎯",
    layout="wide"
)

total_draws = get_total_draws()

st.title("🎯 Lottery Analytics")

st.markdown("---")

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
st.markdown("---")

st.subheader("Administración")

if st.button("Actualizar datos Baloto"):
    st.info("Función de actualización en construcción")
