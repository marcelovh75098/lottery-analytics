import streamlit as st


def render_status(boot, update, draws):

    st.subheader("Estado del motor")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.success("Base inicializada")

        st.write(boot)

    with c2:

        st.info("Actualización")

        st.write(update)

    with c3:

        st.success("Sorteos")

        st.metric(
            "Total",
            draws
        )
