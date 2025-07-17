for i, (s1, s2) in enumerate(partite):
    # Mappa opzioni visuali → valori interni
    opzioni = {
        "🤙🏼": None,
        s1: s1,
        "PAREGGIO": "pareggio",
        s2: s2
    }

    scelta = st.radio(
        f"{s1.upper()} vs {s2.upper()}",
        options=list(opzioni.keys()),
        index=0,  # di default "🤙🏼"
        key=f"partita_{i}",
        horizontal=True,
    )

    risultato = opzioni[scelta]

    # Solo se è stata fatta una scelta valida
    if risultato == s1:
        classifica[s1]["PUNTI"] += 3
        classifica[s1]["Vittorie"] += 1
        classifica[s2]["Sconfitte"] += 1
    elif risultato == s2:
        classifica[s2]["PUNTI"] += 3
        classifica[s2]["Vittorie"] += 1
        classifica[s1]["Sconfitte"] += 1
    elif risultato == "pareggio":
        classifica[s1]["PUNTI"] += 1
        classifica[s2]["PUNTI"] += 1
        classifica[s1]["Pareggi"] += 1
        classifica[s2]["Pareggi"] += 1

    # Aggiungi linea divisoria dopo ogni partita
    st.markdown("---")
