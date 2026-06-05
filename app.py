import streamlit as st

st.set_page_config(
    page_title="Lottery Analytics",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Lottery Analytics")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Sorteos Analizados",
        value="0"
    )

with col2:
    st.metric(
        label="Números Calientes",
        value="Pendiente"
    )

with col3:
    st.metric(
        label="Predicción IA",
        value="Próximamente"
    )

st.markdown("---")

st.subheader("Bienvenido")

st.write("""
Esta plataforma analizará automáticamente:

- Resultados históricos de Baloto
- Frecuencia de números
- Números calientes y fríos
- Retrasos
- Ciclos
- Simulación Monte Carlo
- Predicciones con Machine Learning (XGBoost)
""")

st.success("Sistema inicial funcionando correctamente 🚀")
