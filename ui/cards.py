import streamlit as st


def metric_cards(total_draws, strategies, best_strategy):

    c1,c2,c3=st.columns(3)

    with c1:

        st.metric(

            "Sorteos",

            total_draws

        )

    with c2:

        st.metric(

            "Estrategias",

            strategies

        )

    with c3:

        st.metric(

            "Mejor",

            best_strategy

        )


def elite_ticket(ticket):

    texto=" - ".join(

        map(str,ticket)

    )

    st.markdown(

        f"""

        <div class="ticket">

        🎯 ELITE TICKET

        <br><br>

        {texto}

        </div>

        """,

        unsafe_allow_html=True

    )
