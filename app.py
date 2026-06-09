import streamlit as st

from database.db import (
    create_database,
    get_total_draws,
    insert_draw,
    get_all_draws
)

from scrapers.baloto_scraper import (
    obtener_ultimo_sorteo
)

create_database()

st.set_page_config(
    page_title="Lottery Analytics",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Lottery Analytics")

st.markdown("---")

if st.button("Actualizar datos Baloto"):

    resultado = obtener_ultimo_sorteo()

    if "error" in resultado:

        st.error(resultado["error"])

    else:

        guardado = insert_draw(
            resultado["fecha"],
            int(resultado["n1"]),
            int(resultado["n2"]),
            int(resultado["n3"]),
            int(resultado["n4"]),
            int(resultado["n5"]),
            int(resultado["superbalota"])
        )

        st.json(resultado)

        if guardado:
            st.success(
                "✅ Sorteo guardado correctamente"
            )
        else:
            st.warning(
                "⚠️ El sorteo ya existe en la base de datos o ocurrió un error"
            )

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

st.subheader("📋 Histórico de Sorteos")

draws = get_all_draws()

if len(draws) > 0:

    st.dataframe(
        draws,
        use_container_width=True
    )

else:

    st.info(
        "No hay sorteos almacenados todavía."
    )

st.markdown("---")

st.success(
    "Base de datos conectada correctamente"
)
