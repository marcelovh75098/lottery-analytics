import streamlit as st


def render_kpis(total_draws, total_strategies, best_strategy):

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "📚 Sorteos",
            f"{total_draws:,}"
        )

    with c2:

        st.metric(
            "🧠 Estrategias",
            total_strategies
        )

    with c3:

        st.metric(
            "🏆 Mejor estrategia",
            best_strategy
        )
