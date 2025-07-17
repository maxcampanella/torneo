# torneo_scelta.py
import streamlit as st
import itertools
import pandas as pd

st.title("LA BRISCOLA SICILIANA")

# Squadre predefinite
squadre = ["MAX", "SERGIO", "LEO", "GIANNI", "PASSE", "COMPA", "TONY", "CHRI"]

# Tutti contro tutti
partite = list(itertools.combinations(squadre, 2))

# Dizionario classifica
classifica = {s: {"PUNTI": 0, "Vittorie": 0, "Pareggi": 0, "Sconfitte": 0} for s in squadre}

# Mostra ogni partita e chiedi il risultato
st.subheader("viva la democrazia")

for i, (s1, s2) in enumerate(partite):
    risultato = st.radio(
        f"{s1.upper()} vs {s2.upper()}",
        options=["🤙🏼", s1, "PAREGGIO", s2],
        index=0,  # di default seleziona "?"
        key=f"partita_{i}",
        horizontal=True,
    )

    # Solo se è stata fatta una scelta valida
    if risultato == s1:
        classifica[s1]["PUNTI"] += 3
        classifica[s1]["Vittorie"] += 1
        classifica[s2]["Sconfitte"] += 1
    elif risultato == s2:
        classifica[s2]["PUNTI"] += 3
        classifica[s2]["Vittorie"] += 1
        classifica[s1]["Sconfitte"] += 1
    elif risultato == "Pareggio":
        classifica[s1]["PUNTI"] += 1
        classifica[s2]["PUNTI"] += 1
        classifica[s1]["Pareggi"] += 1
        classifica[s2]["Pareggi"] += 1
    # Se "?" → non aggiorniamo nulla

# Mostra classifica solo se almeno una partita è stata giocata
df = pd.DataFrame.from_dict(classifica, orient="index")
df = df.sort_values(by=["PUNTI", "Vittorie"], ascending=False)

# Spazio visivo
st.markdown("---")
for _ in range(20):
    st.markdown("&nbsp;", unsafe_allow_html=True)

st.subheader("🏆 Classifica finale")
st.dataframe(df.style.format(precision=0))
