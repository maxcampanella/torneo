import streamlit as st
import itertools
import pandas as pd
import random

st.title("LA BRISCOLA SICILIANA")

# Squadre predefinite
squadre = ["MAX", "SERGIO", "LEO", "GIANNI", "PASSE", "COMPA", "TONY", "CHRI"]
"""
squadre = [
    "zocchi", "barchi", "mattiuz", "abruscato", "campanella", "dessilani",
    "chiesa", "muccino", "mancuso", "balzano", "iacometti", "saronne", "cesti",
    "comolla", "tagliabue", "santeusanio", "pezzotta", "panella", "mari", "codini",
    "repossi", "maggiora", "maggiori", "marghe_tipa_gio", "peroni", "tomova",
    "olmo", "putrino", "minniti", "crush_culo", "beltrame", "invernizzi",
    "divittorio", "fant", "pero", "delsignore", "rana"
]
"""
# Mischia le partite solo una volta
if "partite" not in st.session_state:
    partite = list(itertools.combinations(squadre, 2))
    random.shuffle(partite)
    st.session_state.partite = partite
else:
    partite = st.session_state.partite

# Dizionario classifica
classifica = {s: {"Punti": 0, "Vittorie": 0, "Pareggi": 0, "Sconfitte": 0} for s in squadre}

# Mostra ogni partita e chiedi il risultato
for i, (s1, s2) in enumerate(partite):
    opzioni = {
        "🤙🏼": None,
        s1: s1,
        "PAREGGIO": "PAREGGIO",
        s2: s2
    }

    scelta = st.radio(
        f"{s1.upper()} vs {s2.upper()}",
        options=list(opzioni.keys()),
        index=0,
        key=f"partita_{i}",
        horizontal=True,
    )

    risultato = opzioni[scelta]

    if risultato == s1:
        classifica[s1]["Punti"] += 3
        classifica[s1]["Vittorie"] += 1
        classifica[s2]["Sconfitte"] += 1
    elif risultato == s2:
        classifica[s2]["Punti"] += 3
        classifica[s2]["Vittorie"] += 1
        classifica[s1]["Sconfitte"] += 1
    elif risultato == "PAREGGIO":
        classifica[s1]["Punti"] += 1
        classifica[s2]["Punti"] += 1
        classifica[s1]["Pareggi"] += 1
        classifica[s2]["Pareggi"] += 1

    st.markdown("---")

# Classifica finale
df = pd.DataFrame.from_dict(classifica, orient="index")
df = df.sort_values(by=["Punti", "Vittorie"], ascending=False)

for _ in range(20):
    st.markdown("&nbsp;", unsafe_allow_html=True)

st.subheader("🏆 Classifica finale")
st.dataframe(df.style.format(precision=0))
