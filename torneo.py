# torneo_scelta.py
import streamlit as st
import itertools
import pandas as pd

st.title("Torneo Siciliano")

# Squadre predefinite
squadre = ["bea", "gio", "luna", "mara"]
# Tutti contro tutti
partite = list(itertools.combinations(squadre, 2))

# Dizionario classifica
classifica = {s: {"Punti": 0, "Vinte": 0, "Pareggi": 0, "Perse": 0} for s in squadre}

# Mostra ogni partita e chiedi il risultato
st.subheader("Seleziona il risultato per ogni partita:")

for i, (s1, s2) in enumerate(partite):
    risultato = st.radio(
        f"{s1.upper()} vs {s2.upper()}",
        options=[s1, "Pareggio", s2],
        key=f"partita_{i}",
        horizontal=True,
    )

    # Aggiorna classifica
    if risultato == s1:
        classifica[s1]["Punti"] += 3
        classifica[s1]["Vinte"] += 1
        classifica[s2]["Perse"] += 1
    elif risultato == s2:
        classifica[s2]["Punti"] += 3
        classifica[s2]["Vinte"] += 1
        classifica[s1]["Perse"] += 1
    else:
        classifica[s1]["Punti"] += 1
        classifica[s2]["Punti"] += 1
        classifica[s1]["Pareggi"] += 1
        classifica[s2]["Pareggi"] += 1
st.markdown("---")
st.markdown("---")
# Mostra classifica
df = pd.DataFrame.from_dict(classifica, orient="index")
df = df.sort_values(by=["Punti", "Vinte"], ascending=False)

st.markdown("---")
st.markdown("---")
st.markdown("---")
st.markdown("---")
st.markdown("---")
st.markdown("---")
st.markdown("---")
st.markdown("---")
st.markdown("---")
st.markdown("---")
st.markdown("---")
st.markdown("---")
st.markdown("---")
st.markdown("---")
st.markdown("---")
st.markdown("---")
st.markdown("---")
st.markdown("---")
st.markdown("---")



st.subheader("🏆 Classifica finale")
st.dataframe(df.style.format(precision=0))
