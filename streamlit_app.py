import streamlit as st


st.image("logo_petit_noir.png", width=150)

# CSS personnalisé
st.markdown(
    """
    <style>


    /* Masquer complètement le bandeau si nécessaire */
    header {
        visibility: hidden;
    }
    header > div {
        display: none;
    }



    /* Personnaliser les autres éléments si nécessaire */
    /* Applique le style pour centrer le texte globalement */
        .center-text {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100%;
            text-align: center;
            font-size: 20px;
        }

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap');
   

    </style>
    """,
    unsafe_allow_html=True
)

st.header("Calcule tes zones d'entrainement")

st.text("Tu peux calculer tes zones d'entrainement sur la base de ta fréquence cardique au repos et ta fréquence cardiaque maximale")

st.text("Réalise 6 minutes à intensité maximale en côte pour obtenir ta fréquence cardiaque maximale. Tu peux aussi prendre la FC max la plus élevée à ce jour")

st.text("Mesure ta fréquence cardiaque au repos le matin au réveil. Ou prends la FC la plus basse à ce jour")

st.text("Les zones d'entrainement sont basées sur la fréquence cardiaque de réserve. C'est la différentre entre ta FC max et ta FC de repos.")

st.text("La Fréquence cardiaque maximale est personelle et ne peut pas être estimée des formules générales telles que 220 - âge")


st.divider()

fc_max = st.number_input("Fréquence cardiaque maximale", min_value=0, max_value=300, value=0, step=1)
fc_rest = st.number_input("Fréquence cardiaque au repos", min_value=0, max_value=300, value=0, step=1)

st.divider()

zone1_max = fc_rest + 0.6 * (fc_max - fc_rest)
zone2_max = fc_rest + 0.7 * (fc_max - fc_rest)
zone3_max = fc_rest + 0.8 * (fc_max - fc_rest)
zone4_max = fc_rest + 0.9 * (fc_max - fc_rest)

st.subheader("Zones 1")
st.write(f"Zone 1: {0} - {zone1_max}")

st.subheader("Zones 2")
st.write(f"Zone 2: {zone1_max} - {zone2_max}")

st.subheader("Zones 3")
st.write(f"Zone 3: {zone2_max} - {zone3_max}")

st.subheader("Zones 4")
st.write(f"Zone 4: {zone3_max} - {zone4_max}")

st.subheader("Zones 5")
st.write(f"Zone 4: {zone4_max} - {fc_max}")




                            

    
   

    