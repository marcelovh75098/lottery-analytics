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

    # KPIs
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        info_card("Total Sorteos", context.metrics["total_draws"], "#2563EB")

    with c2:
        info_card("Estrategias", context.metrics["strategies"], "#10B981")

    with c3:
        info_card("Predicciones", context.metrics["predictions"], "#F59E0B")

    with c4:
        info_card("Estado", "Activo", "#8B5CF6")

    # Resumen
    section("Resumen Ejecutivo")

    st.dataframe(
        context.ranking,
        use_container_width=True
    )

    # ← AQUÍ VA EL BLOQUE

    section("📈 Analítica General")

    left, right = st.columns((2,1))

    with left:

        if hasattr(context,"frequency_df"):

            st.plotly_chart(
                frequency_chart(context.frequency_df),
                use_container_width=True
            )

    with right:

        if hasattr(context,"parity"):

            st.plotly_chart(
                parity_chart(context.parity),
                use_container_width=True
            )

    section("❤️ Estado")

    render_system_status(context)
from ui.charts import (
    frequency_chart,
    parity_chart
)

from ui.system_status import render_system_status

import plotly.express as px
import pandas as pd
