import streamlit as st
import folium
from streamlit_folium import st_folium
from datetime import datetime

heure_actuelle = datetime.now().hour

# =========================================================
# CONFIGURATION PAGE
# =========================================================
st.set_page_config(
    page_title="Dakar JOJ 2026",
    page_icon="🇸🇳",
    layout="centered"
)

# =========================================================
# STYLE PREMIUM (DARK BLUE - JOJ DAKAR 2026)
# =========================================================
st.markdown("""
<style>

/* 🌌 BACKGROUND GLOBAL */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(180deg, #061a33 0%, #0b1f3a 50%, #050f1f 100%);
    color: white;
}

/* 📦 CONTENEUR PRINCIPAL */
.main {
    padding: 1.5rem;
}

/* 🏷️ TITRES */
h1, h2, h3 {
    color: #00d4ff !important;
    font-weight: 700;
}

/* 🧭 SIDEBAR PREMIUM */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #071428 0%, #0b223d 100%);
    border-right: 1px solid rgba(255,255,255,0.08);
}

[data-testid="stSidebar"] * {
    color: #e6f1ff !important;
}

/* 🔘 BOUTONS PREMIUM */
.stButton button {
    width: 100%;
    border-radius: 14px;
    background: linear-gradient(135deg, #00bfff, #0080ff);
    color: white;
    font-weight: 600;
    border: none;
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    transition: 0.2s ease-in-out;
}

.stButton button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(0,0,0,0.4);
}

/* ✍️ INPUTS (SEARCH / TEXT / FORM) */
input, textarea, .stTextInput input {
    background-color: #0b2a4a !important;
    color: white !important;
    border-radius: 12px !important;
    border: 1px solid rgba(0, 212, 255, 0.3) !important;
}

input::placeholder {
    color: rgba(255,255,255,0.5) !important;
}

input:focus {
    background-color: #0f355f !important;
    border: 1px solid #00d4ff !important;
    outline: none !important;
}

/* 📊 METRICS */
[data-testid="stMetric"] {
    background: rgba(255,255,255,0.05);
    padding: 12px;
    border-radius: 12px;
    border: 1px solid rgba(255,255,255,0.08);
}

/* 🧊 EXPANDERS */
.streamlit-expanderHeader {
    background: rgba(255,255,255,0.05);
    border-radius: 10px;
    color: #e6f1ff !important;
}

/* 📏 DIVIDERS */
hr {
    border-color: rgba(255,255,255,0.1);
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================
st.title("🇸🇳 Dakar 2026 — Teranga Mobile")
st.caption("Prototype de mobilité intelligente pour les JOJ 2026")

if heure_actuelle < 12:
    st.success("☀️ Bonjour et bienvenue !")
elif heure_actuelle < 18:
    st.success("🌤️ Bon après-midi !")
else:
    st.success("🌙 Bonne soirée !")

st.info(
    f"📅 {datetime.now().strftime('%d/%m/%Y')} | 🕒 {datetime.now().strftime('%H:%M')}"
)

# =========================================================
# SIDEBAR
# =========================================================
st.sidebar.image(
    "AYO.png",
    width=180
)

st.sidebar.success("🦁 Ayo vous accompagne")
st.sidebar.caption(
    "Mascotte officielle des JOJ Dakar 2026"
)

st.sidebar.success("🏅 Visiteur JOJ")
st.sidebar.info("Niveau : Explorateur")
st.sidebar.markdown("---")

st.sidebar.metric("Voyageurs", "45 000")
st.sidebar.metric("Billets", "250 000")
st.sidebar.metric("SOS", "18")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "📍 Navigation",
    [
        "🏠 Accueil & Trafic",
        "🗺️ Carte & Signalements",
        "🚨 Zone SOS",
        "🍽️ Restauration",
        "🚍 Itinéraire Intelligent",
        "🦁 Guide Teranga",
        "🌤️ Météo",
        "🎟️ Mes Billets"
    ]
)

# =========================================================
# PAGE 1 : ACCUEIL & TRAFIC
# =========================================================
if page == "🏠 Accueil & Trafic":
    st.header("🚦 État du Réseau")

    if heure_actuelle >= 22 or heure_actuelle < 5:
        etat_ter = "Fermé"
        icone_ter = "🔴"
    else:
        etat_ter = "Ouvert"
        icone_ter = "🟢"

    if heure_actuelle >= 21 or heure_actuelle < 5:
        etat_brt = "Fermé"
        icone_brt = "🔴"
    else:
        etat_brt = "Ouvert"
        icone_brt = "🟢"

    col1, col2 = st.columns(2)
    with col1:
        st.metric("🚆 TER", etat_ter, icone_ter)
    with col2:
        st.metric("🚌 BRT", etat_brt, icone_brt)

    st.caption(f"🕒 Heure actuelle : {datetime.now().strftime('%H:%M')}")
    st.divider()

    st.subheader("🕒 Horaires de fonctionnement")
    st.info("🚆 TER : 05h00 → 22h00")
    st.info("🚌 BRT : 05h00 → 21h00")
    st.divider()

    st.subheader("🚌 Lignes principales")
    st.success("TER Dakar ↔ Diamniadio : circulation normale")
    st.warning("BRT Guédiawaye ↔ Petersen : ralentissements légers")
    st.info("Navette JOJ Ligne A : service opérationnel")
    st.divider()

    st.subheader("👥 Affluence actuelle")
    if 6 <= heure_actuelle <= 9:
        st.warning("⚠️ Heure de pointe du matin")
        st.progress(90)
        niveau = "Très élevée"
    elif 17 <= heure_actuelle <= 20:
        st.error("🔴 Heure de pointe du soir")
        st.progress(100)
        niveau = "Maximum"
    elif 12 <= heure_actuelle <= 14:
        st.info("🟠 Affluence moyenne")
        st.progress(60)
        niveau = "Moyenne"
    else:
        st.success("🟢 Circulation fluide")
        st.progress(30)
        niveau = "Faible"

    st.metric("Niveau d'affluence", niveau)
    st.divider()

    st.subheader("🚍 Véhicules en circulation")
    if 17 <= heure_actuelle <= 20:
        nb_brt = 120
        nb_ter = 20
        message = "Renforcement spécial heure de pointe"
    elif 6 <= heure_actuelle <= 9:
        nb_brt = 100
        nb_ter = 18
        message = "Renforcement du service matinal"
    else:
        nb_brt = 70
        nb_ter = 15
        message = "Service normal"

    st.info(message)
    col1, col2 = st.columns(2)
    with col1:
        st.metric("🚌 BRT actifs", nb_brt)
    with col2:
        st.metric("🚆 TER actifs", nb_ter)
    st.divider()

    st.subheader("🔮 Prévision de trafic")
    if 16 <= heure_actuelle <= 18:
        st.warning("Forte augmentation du trafic prévue dans l'heure.")
    elif 20 <= heure_actuelle <= 21:
        st.success("Diminution progressive de l'affluence prévue.")
    else:
        st.info("Aucune perturbation majeure prévue.")
    st.divider()

    st.subheader("📢 Alertes Réseau")
    st.warning("Travaux prévus demain sur certaines lignes BRT.")
    st.info("Navettes JOJ renforcées pour les compétitions du soir.")
    st.divider()

    st.subheader("🏅 Statistiques du jour")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Voyageurs", "45 000")
    with col2:
        st.metric("Navettes JOJ", "180")
    with col3:
        st.metric("Incidents", "3")
    st.divider()

    st.subheader("😊 Satisfaction voyageurs")
    satisfaction = st.slider("Note moyenne", 1, 5, 4)
    st.success(f"Satisfaction moyenne : {satisfaction}/5")

# =========================================================
# PAGE 2 : CARTE & SIGNALEMENTS
# =========================================================
elif page == "🗺️ Carte & Signalements":
    st.header("🗺️ Carte des Transports")
    st.write("Visualisez les incidents, perturbations et zones importantes du réseau.")
    st.divider()

    st.subheader("🔎 Filtrer les événements")
    filtre = st.selectbox(
        "Type d'affichage",
        ["Tous", "Embouteillages", "Incidents", "TER", "BRT", "Navettes JOJ"]
    )

    coords_dakar = [14.7167, -17.4677]
    ma_carte = folium.Map(location=coords_dakar, zoom_start=12)

    if filtre in ["Tous", "Embouteillages"]:
        folium.Marker(
            [14.7450, -17.4520],
            popup="⚠️ Embouteillage important\n\nNiveau : Élevé\n\nTemps perdu estimé : 15 min",
            tooltip="🚗 Embouteillage",
            icon=folium.Icon(color="red")
        ).add_to(ma_carte)

    if filtre in ["Tous", "Incidents"]:
        folium.Marker(
            [14.7200, -17.4400],
            popup="🚧 Travaux en cours\n\nImpact : Moyen",
            tooltip="🚧 Travaux",
            icon=folium.Icon(color="orange")
        ).add_to(ma_carte)

    if filtre in ["Tous", "TER"]:
        folium.Marker(
            [14.7333, -17.4677],
            popup="🚆 Gare TER Dakar",
            tooltip="TER",
            icon=folium.Icon(color="green")
        ).add_to(ma_carte)

    if filtre in ["Tous", "BRT"]:
        folium.Marker(
            [14.7600, -17.4300],
            popup="🚌 Station BRT",
            tooltip="BRT",
            icon=folium.Icon(color="blue")
        ).add_to(ma_carte)

    if filtre in ["Tous", "Navettes JOJ"]:
        folium.Marker(
            [14.7645, -17.3660],
            popup="🏅 Navette JOJ",
            tooltip="JOJ",
            icon=folium.Icon(color="purple")
        ).add_to(ma_carte)

    st_folium(ma_carte, use_container_width=True, height=500)
    st.divider()

    st.subheader("📊 Situation actuelle")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Embouteillages", "4")
    with col2:
        st.metric("Incidents", "2")
    with col3:
        st.metric("Zones fluides", "12")
    st.divider()

    st.subheader("⚠️ Signaler une anomalie")
    with st.form("form_incident"):
        type_incident = st.selectbox(
            "Type de problème",
            ["Embouteillage", "Navette en panne", "Zone saturée", "Accident", "Travaux", "Autre"]
        )
        gravite = st.select_slider("Niveau de gravité", options=["Faible", "Moyenne", "Élevée"])
        description = st.text_area("Décrivez le problème")
        envoyer = st.form_submit_button("📤 Envoyer")

        if envoyer:
            if description.strip() == "":
                st.error("Veuillez ajouter une description.")
            else:
                st.success("Signalement envoyé avec succès ✅")
                st.info(f"Type : {type_incident}\n\nGravité : {gravite}\n\nDescription : {description}")
    st.divider()

    st.subheader("📜 Derniers signalements")
    st.warning("🚗 Embouteillage signalé à Liberté 6")
    st.info("🚧 Travaux signalés à Colobane")
    st.error("🚌 Navette JOJ en panne à Diamniadio")

# =========================================================
# PAGE 3 : SOS
# =========================================================
elif page == "🚨 Zone SOS":
    st.header("🚨 Zone SOS & Urgences")
    st.error("En cas d'urgence, contactez immédiatement les secours.")
    st.divider()

    st.subheader("📞 Numéros utiles")
    col1, col2 = st.columns(2)
    with col1:
        st.info("👮 Police")
        st.code("17")
        st.info("🚒 Pompiers")
        st.code("18")
    with col2:
        st.info("🚑 SAMU")
        st.code("1515")
        st.info("🆘 Urgence JOJ")
        st.code("+221 77 000 2026")
    st.divider()

    st.subheader("🚨 Déclencher une alerte SOS")
    type_urgence = st.selectbox(
        "Type d'urgence",
        ["Accident", "Malaise", "Agression", "Incendie", "Perte d'enfant", "Autre"]
    )
    niveau = st.select_slider("Niveau de priorité", options=["Faible", "Moyenne", "Élevée", "Critique"])
    localisation = st.text_input("📍 Localisation")
    details = st.text_area("📝 Décrivez rapidement la situation")
    envoyer_sos = st.button("🚨 Envoyer l'alerte SOS")

    if envoyer_sos:
        if localisation.strip() == "":
            st.error("Veuillez préciser le lieu.")
        else:
            st.success("Alerte SOS envoyée avec succès ✅")
            st.warning(f"🚨 Type : {type_urgence}\n\n📍 Localisation : {localisation}\n\n⚠️ Priorité : {niveau}\n\n📡 Les secours ont été notifiés.")
    st.divider()

    st.subheader("⏱️ Temps d'intervention estimé")
    if niveau == "Critique":
        temps = "3 min"
    elif niveau == "Élevée":
        temps = "5 min"
    elif niveau == "Moyenne":
        temps = "10 min"
    else:
        temps = "15 min"

    st.metric("Temps estimé", temps)
    st.divider()

    st.subheader("🏥 Postes de secours à proximité")
    st.success("🏥 Poste médical Stade Abdoulaye Wade")
    st.success("🏥 Centre médical Village Olympique")
    st.success("🏥 Infirmerie Piscine Olympique")
    st.divider()

    st.subheader("📡 Suivi de l'intervention")
    progression = st.slider("Avancement", 0, 100, 25)
    st.progress(progression)

    if progression < 30:
        st.info("Alerte reçue par le centre d'urgence.")
    elif progression < 70:
        st.warning("Une équipe est en route.")
    else:
        st.success("Les secours sont sur place.")
    st.divider()

    st.subheader("🛟 Conseils rapides")
    with st.expander("❤️ Malaise ou blessure"):
        st.write("• Mettre la personne en sécurité\n\n• Éviter les mouvements brusques\n\n• Appeler le SAMU")
    with st.expander("🔥 Incendie"):
        st.write("• Évacuer immédiatement\n\n• Ne pas utiliser les ascenseurs\n\n• Appeler les pompiers")
    with st.expander("👶 Enfant perdu"):
        st.write("• Prévenir les agents JOJ\n\n• Décrire les vêtements\n\n• Rester sur place")
    st.divider()

    st.subheader("📊 Activité du jour")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("SOS reçus", "18")
    with col2:
        st.metric("Interventions", "15")
    with col3:
        st.metric("Temps moyen", "6 min")

# =========================================================
# PAGE 4 : RESTAURATION
# =========================================================
elif page == "🍽️ Restauration":
    st.header("🍽️ Food Zones JOJ Dakar 2026")
    st.write("Découvrez les restaurants et espaces de restauration proches des sites olympiques.")
    st.divider()

    stade = st.selectbox(
        "🏟️ Choisir un site olympique",
        ["Stade Abdoulaye Wade", "Stade Léopold Sédar Senghor", "Piscine Olympique", "Village Olympique"]
    )
    st.divider()

    st.subheader("🇸🇳 Découvrir la cuisine sénégalaise")
    plats_senegalais = ["🍚 Thiéboudiène", "🍗 Yassa Poulet", "🥩 Mafé", "🐟 Thiou Bou Dienn", "🥟 Fataya", "🥤 Jus de Bissap"]
    for p in plats_senegalais:
        st.write(p)
    st.divider()

    st.subheader("🍴 Restaurants recommandés")
    if stade == "Stade Abdoulaye Wade":
        with st.container():
            st.success("🥘 Chez Lamine Grill")
            st.write("⭐ 4.7/5")
            st.write("📍 500 m du stade")
            st.write("⏳ Attente : 10 min")
        st.info("🍔 Fast Burger Diamniadio")
        st.warning("☕ Café Teranga Express")
    elif stade == "Stade Léopold Sédar Senghor":
        st.success("🍛 Dakar Saveurs")
        st.info("🍕 Pizza Rapido")
        st.warning("🥤 Olympic Food Corner")
    elif stade == "Piscine Olympique":
        st.success("🐟 Le Ndamli Seafood")
        st.info("🥗 Green Food Dakar")
        st.warning("☕ Café des Athlètes")
    elif stade == "Village Olympique":
        st.success("🍲 Teranga Buffet")
        st.info("🍗 Chicken Express")
        st.warning("🥪 Olympic Snack Zone")
    st.divider()

    st.subheader("🔎 Filtres")
    col1, col2 = st.columns(2)
    with col1:
        halal = st.checkbox("✅ Halal")
    with col2:
        wifi = st.checkbox("📶 Wi-Fi")

    budget = st.slider("💰 Budget moyen (FCFA)", 1000, 20000, 5000)
    st.info(f"Budget sélectionné : {budget} FCFA")
    st.divider()

    st.subheader("📋 Menu JOJ")
    menu = {"Thiéboudiène": 3500, "Yassa Poulet": 3000, "Mafé": 3000, "Fataya": 500, "Jus de Bissap": 1000}
    for nom_p, prix_p in menu.items():
        st.write(f"🍽️ {nom_p} — {prix_p} FCFA")
    st.divider()

    st.subheader("🛒 Commander un repas")
    plat_choisi = st.selectbox("Choisir un plat", list(menu.keys()))
    quantite = st.number_input("Quantité", 1, 10, 1)
    total = menu[plat_choisi] * quantite

    st.metric("💰 Total", f"{total} FCFA")
    if st.button("🛍️ Commander"):
        st.success(f"{quantite} x {plat_choisi} commandé(s) avec succès ✅")
    st.divider()

    st.subheader("🛵 Livraison JOJ")
    livraison = st.radio("Souhaitez-vous une livraison ?", ["Oui", "Non"])
    if livraison == "Oui":
        adresse = st.text_input("📍 Votre position")
        if adresse:
            st.success(f"Livraison disponible vers {adresse}")
    st.divider()

    st.subheader("📊 Occupation des restaurants")
    st.progress(40)
    st.caption("40% d'occupation actuellement")
    st.divider()

    st.subheader("⭐ Votre avis")
    note = st.slider("Donnez une note", 1, 5, 4)
    commentaire = st.text_area("Votre commentaire")
    if st.button("Envoyer l'avis"):
        st.success("Merci pour votre avis !")
    st.divider()

    st.subheader("🏅 Passeport Gastronomique")
    plats_testes = st.slider("Nombre de plats sénégalais goûtés", 0, 5, 0)
    if plats_testes >= 3:
        st.success("🏅 Badge Découverte de la Gastronomie Sénégalaise obtenu !")
    st.divider()

    st.subheader("🤖 Assistant Food")
    question_food = st.text_input("Que souhaitez-vous manger ?")
    if question_food:
        if "poisson" in question_food.lower():
            st.info("Nous vous recommandons le Thiéboudiène.")
        elif "poulet" in question_food.lower():
            st.info("Nous vous recommandons le Yassa Poulet.")
        else:
            st.info("Découvrez les spécialités sénégalaises proposées.")
    st.divider()

    st.subheader("🗺️ Carte des Food Zones")
    carte_food = folium.Map(location=[14.7167, -17.4677], zoom_start=12)
    folium.Marker([14.7645, -17.3660], popup="Chez Lamine Grill", tooltip="🥘 Cuisine Sénégalaise").add_to(carte_food)
    folium.Marker([14.7368, -17.4532], popup="Olympic Food Corner", tooltip="🍔 Fast Food").add_to(carte_food)
    folium.Marker([14.7510, -17.4725], popup="Café des Athlètes", tooltip="☕ Café").add_to(carte_food)
    st_folium(carte_food, use_container_width=True, height=400)

# =========================================================
# PAGE 5 : ITINERAIRE INTELLIGENT
# =========================================================
elif page == "🚍 Itinéraire Intelligent":
    st.header("🚍 Itinéraire Intelligent")
    st.write("Planifiez votre déplacement vers les sites des JOJ.")
    st.divider()

    depart = st.selectbox(
        "📍 Point de départ",
        ["Plateau", "Pikine", "Guédiawaye", "Parcelles Assainies", "Diamniadio", "Aéroport AIBD"]
    )
    destination = st.selectbox(
        "🎯 Destination",
        ["Stade Abdoulaye Wade", "Village Olympique", "Piscine Olympique", "Stade Léopold Sédar Senghor"]
    )
    transport = st.radio(
        "🚆 Moyen de transport préféré",
        ["Le plus rapide", "Le moins cher", "TER", "BRT", "Navette JOJ"]
    )
    st.divider()

    if st.button("🔍 Calculer l'itinéraire"):
        temps = 35
        cout = 1000
        st.success("Itinéraire trouvé ✅")
        st.info(f"🚆 TER jusqu'à Diamniadio\n\n🚌 Navette JOJ vers le site\n\n⏱ Temps estimé : {temps} min\n\n💰 Coût estimé : {cout} FCFA")
        st.progress(70)
    st.divider()

    st.subheader("📊 Comparaison des moyens de transport")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🚆 TER", "25 min")
    with col2:
        st.metric("🚌 BRT", "40 min")
    with col3:
        st.metric("🏅 Navette", "30 min")
    st.divider()

    st.subheader("🌱 Impact environnemental")
    mode = st.selectbox("Choisir un mode", ["TER", "BRT", "Navette JOJ"])
    if mode == "TER":
        emission = 1.2
    elif mode == "BRT":
        emission = 2.0
    else:
        emission = 1.5
    st.metric("CO₂ estimé", f"{emission} kg")
    st.divider()

    st.subheader("👥 Affluence prévue")
    if 17 <= heure_actuelle <= 20:
        st.error("Très forte affluence prévue.")
        st.progress(100)
    elif 6 <= heure_actuelle <= 9:
        st.warning("Affluence élevée.")
        st.progress(80)
    else:
        st.success("Affluence normale.")
        st.progress(40)
    st.divider()

    st.subheader("⭐ Trajets favoris")
    favoris = st.checkbox("Ajouter ce trajet aux favoris")
    if favoris:
        st.success("Trajet ajouté aux favoris ✅")
    st.divider()

    st.subheader("🕘 Historique récent")
    st.write("📍 Plateau → Stade Abdoulaye Wade")
    st.write("📍 Pikine → Village Olympique")
    st.write("📍 AIBD → Stade Léopold Sédar Senghor")

# =========================================================
# PAGE 6 : GUIDE TERANGA
# =========================================================
elif page == "🦁 Guide Teranga":
    st.header("🦁 Guide Teranga")
    st.subheader("📍 Lieux utiles")
    st.write("🏟️ Stade Abdoulaye Wade")
    st.write("🚆 Gare TER Dakar")
    st.write("🏊 Piscine Olympique")
    st.divider()

    st.subheader("🍽️ Conseils visiteurs")
    st.write("• Utiliser le TER aux heures de pointe")
    st.write("• Prévoir une bouteille d’eau")
    st.write("• Scanner les QR codes des navettes")
    st.write("• Respecter les consignes de sécurité")
    st.divider()

    st.subheader("🌍 Langues utiles")
    st.write("🇸🇳 Wolof")
    st.write("🇫🇷 Français")
    st.write("🇬🇧 English")

# =========================================================
# PAGE 7 : METEO
# =========================================================
elif page == "🌤️ Météo":
    st.header("🌤️ Météo JOJ Dakar 2026")
    st.write("Prévisions météo pour les visiteurs et les compétitions.")
    st.divider()

    st.subheader("☀️ Conditions actuelles")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🌡️ Température", "29°C")
    with col2:
        st.metric("💧 Humidité", "72%")
    with col3:
        st.metric("💨 Vent", "18 km/h")
    st.divider()

    st.subheader("📅 Prévisions des prochains jours")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("Lundi\n\n☀️ Ensoleillé\n\n30°C")
    with col2:
        st.info("Mardi\n\n⛅ Nuageux\n\n28°C")
    with col3:
        st.info("Mercredi\n\n🌦️ Averses\n\n27°C")
    st.divider()

    st.subheader("🧴 Conseils météo")
    st.success("🥤 Pensez à vous hydrater régulièrement.")
    st.info("🧢 Portez une casquette durant les compétitions extérieures.")
    st.warning("☀️ Évitez une exposition prolongée au soleil entre 12h et 15h.")
    st.divider()

    st.subheader("🚍 Impact sur les transports")
    st.success("Aucune perturbation météo prévue sur le TER et le BRT.")
    st.divider()

    st.subheader("🏟️ Conditions des sites sportifs")
    st.write("🏟️ Stade Abdoulaye Wade : Conditions excellentes")
    st.write("🏊 Piscine Olympique : Conditions excellentes")
    st.write("🏘️ Village Olympique : Conditions normales")

# =========================================================
# PAGE 8 : MES BILLETS
# =========================================================
elif page == "🎟️ Mes Billets":
    st.header("🎟️ Billetterie JOJ Dakar 2026")
    st.write("Consultez et gérez vos billets.")
    st.divider()

    nom = st.text_input("👤 Nom du visiteur")
    competition = st.selectbox(
        "🏅 Compétition",
        ["Athlétisme", "Natation", "Football", "Basket 3x3", "Handball"]
    )
    date_match = st.date_input("📅 Date de l'événement")
    nombre = st.number_input("🎫 Nombre de billets", 1, 10, 1)
    st.divider()

    prix = {"Athlétisme": 3000, "Natation": 2500, "Football": 5000, "Basket 3x3": 3500, "Handball": 3000}
    total = prix[competition] * nombre

    st.metric("💰 Prix total", f"{total} FCFA")
    st.divider()

    if st.button("🎟️ Générer mon billet"):
        st.success("Billet généré avec succès ✅")
        st.info(f"👤 Nom : {nom}\n\n🏅 Compétition : {competition}\n\n📅 Date : {date_match}\n\n🎫 Nombre de billets : {nombre}\n\n💰 Total payé : {total} FCFA")
        st.code(f"JOJ-{competition[:3].upper()}-{nombre}2026")
    st.divider()

    st.subheader("📱 Contrôle d'accès")
    st.success("QR Code prêt pour le contrôle à l'entrée.")
    st.progress(100)
    st.divider()

    st.subheader("📜 Historique des billets")
    st.write("🎫 Football - 15 août 2026")
    st.write("🎫 Athlétisme - 18 août 2026")
    st.write("🎫 Natation - 20 août 2026")
    st.divider()

    st.subheader("📊 Billetterie")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Billets vendus", "250 000")
    with col2:
        st.metric("Disponibilité", "78%")