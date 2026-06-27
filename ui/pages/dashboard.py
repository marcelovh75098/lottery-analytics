import streamlit as st

from ui.components import (
    page_header,
    info_card,
    section
)


def render_dashboard(context):

    page_header(
        "🎯 Lottery Analytics",
        "Centro de Analítica Inteligente"
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        info_card(
            "Total Sorteos",
            context.metrics["total_draws"],
            "#2563EB"
        )

    with c2:

        info_card(
            "Estrategias",
            context.metrics["strategies"],
            "#10B981"
        )

    with c3:

        info_card(
            "Predicciones",
            context.metrics["predictions"],
            "#F59E0B"
        )

    with c4:

        info_card(
            "Estado",
            "Activo",
            "#8B5CF6"
        )

    section("Estado General")

    st.info(
        "Lottery Analytics está funcionando correctamente."
    )

    section("Resumen Ejecutivo")

    st.dataframe(
        context.ranking,
        use_container_width=True
    )
