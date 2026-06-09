import streamlit as st

from scrapers.baloto_scraper import obtener_ultimo_sorteo
from database.db import insert_draw, get_total_draws

st.set_page_config(
    page_title="Lottery Analytics",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Lottery Analytics")

st.markdown("---")

# 📊 Estadística básica
total = get_total_draws()
st.metric("Sorteos guardados", total)

st.markdown("## 🔄 Actualizar datos Baloto")

if st.button("Actualizar datos Baloto"):

    resultado = obtener_ultimo_sorteo()

    if resultado:

        insert_draw(
            resultado["fecha"],
            resultado["n1"],
            resultado["n2"],
            resultado["n3"],
            resultado["n4"],
            resultado["n5"],
            resultado["superbalota"]
        )

        st.success("✅ Sorteo guardado correctamente")

        st.json(resultado)

    else:
        st.error("❌ No se pudo obtener el sorteo")

st.markdown("---")
st.subheader("📈 Sorteos Analizados")

st.info("Próximo paso: análisis de números calientes y predicción IA")
