import streamlit as st
import folium
from streamlit_folium import st_folium
from datetime import datetime
import time
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
# 1. LES IMPORTATIONS (Tout en haut)
# =========================================================
import streamlit as st
import folium
from streamlit_folium import st_folium
from datetime import datetime
import time # <-- Super important pour les 3 secondes !

heure_actuelle = datetime.now().hour

# =========================================================
# 2. LA CONFIGURATION DE LA PAGE (Juste après)
# =========================================================
st.set_page_config(
    page_title="Dakar JOJ 2026",
    page_icon="🇸🇳",
    layout="centered"
)

# =========================================================
# 3. 🎬 L'ÉCRAN D'ACCUEIL (SPLASH SCREEN) <-- C'EST ICI !
# =========================================================
if "splash_done" not in st.session_state:
    placeholder = st.empty()
    
    with placeholder.container():
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        col_space1, col_img, col_space2 = st.columns([1, 2, 1])
        
        with col_img:
            # Remplace par le nom de ton fichier image ou ton lien URL
            st.image(
                "mon_accueil.png",
                use_container_width=True
            )
        
        st.markdown("""
            <div style="text-align: center; margin-top: 20px;">
                <h2 style="color: #00d4ff; font-weight: 700;">
                    BIENVENUE AU SENEGAL
                </h2>
                <p style="color: #e6f1ff; font-size: 1.2rem; font-style: italic;">
                    Dall len ak diam ci senegal
                </p>
                <div style="color: rgba(255,255,255,0.4); font-size: 0.9rem; margin-top: 30px;">
                    Chargement en cours... ⏳
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    time.sleep(3) # Temps d'attente (3 secondes)
    st.session_state["splash_done"] = True
    placeholder.empty()

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

st.sidebar.success("📍 Localisation")

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "📍 Navigation",
    [
        "🏠 Accueil & Trafic",
        "🗺️ Carte & Signalements",
        "🚨 Zone SOS",
        "🍽️ Restauration",
        "🚍 Itinéraire Intelligent",
        "🎟️ Mes Billets",
        "🤖 Assistant Teranga",
        "🇸🇳 Découvrir le Sénégal",
        "🦁 Guide Teranga"
    ]
)
# =========================================================
# PAGE 1 : ACCUEIL & TRAFIC
# =========================================================
if page == "🏠 Accueil & Trafic":

    st.header("🚦 État du Réseau")

    # =====================================
    # ETAT TER ET BRT
    # =====================================

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

    st.caption(
        f"🕒 Heure actuelle : {datetime.now().strftime('%H:%M')}"
    )

    st.divider()

    # =====================================
    # HORAIRES OFFICIELS
    # =====================================

    st.subheader("🕒 Horaires de fonctionnement")

    st.info("🚆 TER : 05h00 → 22h00")
    st.info("🚌 BRT : 05h00 → 21h00")

    st.divider()

    # =====================================
    # LIGNES PRINCIPALES
    # =====================================

    st.subheader("🚌 Lignes principales")

    st.success(
        "TER Dakar ↔ Diamniadio : circulation normale"
    )

    st.warning(
        "BRT Guédiawaye ↔ Petersen : ralentissements légers"
    )

    st.info(
        "Navette JOJ Ligne A : service opérationnel"
    )

    st.divider()

    # =====================================
    # AFFLUENCE
    # =====================================

    st.subheader("👥 Affluence actuelle")

    if 6 <= heure_actuelle <= 9:

        st.warning(
            "⚠️ Heure de pointe du matin"
        )

        st.progress(90)

        niveau = "Très élevée"

    elif 17 <= heure_actuelle <= 20:

        st.error(
            "🔴 Heure de pointe du soir"
        )

        st.progress(100)

        niveau = "Maximum"

    elif 12 <= heure_actuelle <= 14:

        st.info(
            "🟠 Affluence moyenne"
        )

        st.progress(60)

        niveau = "Moyenne"

    else:

        st.success(
            "🟢 Circulation fluide"
        )

        st.progress(30)

        niveau = "Faible"

    st.metric(
        "Niveau d'affluence",
        niveau
    )

    st.divider()

    # =====================================
    # FLOTTE ACTIVE
    # =====================================

    st.subheader("🚍 Véhicules en circulation")

    if 17 <= heure_actuelle <= 20:

        nb_brt = 158
        nb_ter = 27

        message = (
            "Renforcement spécial heure de pointe"
        )

    elif 6 <= heure_actuelle <= 9:

        nb_brt = 100
        nb_ter = 18

        message = (
            "Renforcement du service matinal"
        )

    else:

        nb_brt = 70
        nb_ter = 15

        message = (
            "Service normal"
        )

    st.info(message)

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "🚌 BRT actifs",
            nb_brt
        )

    with col2:
        st.metric(
            "🚆 TER actifs",
            nb_ter
        )

    st.divider()

    # =====================================
    # PREVISIONS
    # =====================================

    st.subheader("🔮 Prévision de trafic")

    if 16 <= heure_actuelle <= 18:

        st.warning(
            "Forte augmentation du trafic prévue dans l'heure."
        )

    elif 20 <= heure_actuelle <= 21:

        st.success(
            "Diminution progressive de l'affluence prévue."
        )

    else:

        st.info(
            "Aucune perturbation majeure prévue."
        )

    st.divider()
    # =====================================
    # SATISFACTION
    # =====================================

    st.subheader("😊 Satisfaction voyageurs")

    satisfaction = st.slider(
        "Note moyenne",
        1,
        5,
        4
    )

    st.success(
        f"Satisfaction moyenne : {satisfaction}/5"
    )

# =========================================================
# PAGE 2 : CARTE & SIGNALEMENTS
# =========================================================
elif page == "🗺️ Carte & Signalements":

    st.header("🗺️ Carte Intelligente Teranga Mobile")

    st.write(
        "Consultez les sites des JOJ, les lignes TER et BRT, les navettes officielles ainsi que les perturbations du trafic en temps réel."
    )

    # ==========================
    # FILTRES
    # ==========================

    st.subheader("🔎 Filtrer l'affichage")

    filtre = st.selectbox(
        "Type d'affichage",
        [
            "Tous",
            "Sites JOJ",
            "TER",
            "BRT",
            "Navettes JOJ",
            "Perturbations"
        ]
    )

    # ==========================
    # CARTE
    # ==========================

    ma_carte = folium.Map(
        location=[14.7167, -17.4677],
        zoom_start=10
    )

    # ==========================
    # SITES JOJ
    # ==========================

    if filtre in ["Tous", "Sites JOJ"]:

        folium.Marker(
            [14.7305, -17.1987],
            popup="""
🏟️ Stade Abdoulaye Wade

Site principal des JOJ Dakar 2026
""",
            tooltip="Stade Abdoulaye Wade",
            icon=folium.Icon(color="red")
        ).add_to(ma_carte)

        folium.Marker(
            [14.6935, -17.4548],
            popup="""
🏉 Complexe Iba Mar Diop

Compétitions sportives
""",
            tooltip="Complexe Iba Mar Diop",
            icon=folium.Icon(color="purple")
        ).add_to(ma_carte)

        folium.Marker(
            [14.4436, -17.0047],
            popup="""
🏖️ Saly

Zone touristique et animations JOJ
""",
            tooltip="Saly",
            icon=folium.Icon(color="orange")
        ).add_to(ma_carte)

    # ==========================
    # TER DAKAR - DIAMNIADIO
    # ==========================

    if filtre in ["Tous", "TER"]:

        ter_points = [
            [14.6937, -17.4441],  # Dakar
            [14.7045, -17.4380],  # Colobane
            [14.7340, -17.3950],  # Hann
            [14.7640, -17.3400],  # Pikine
            [14.7600, -17.2800],  # Rufisque
            [14.7305, -17.1987]   # Diamniadio
        ]

        folium.PolyLine(
            ter_points,
            color="green",
            weight=5,
            tooltip="Ligne TER Dakar - Diamniadio"
        ).add_to(ma_carte)

        folium.Marker(
            [14.6937, -17.4441],
            popup="🚆 Gare TER Dakar",
            icon=folium.Icon(color="green")
        ).add_to(ma_carte)

        folium.Marker(
            [14.7305, -17.1987],
            popup="🚆 Gare TER Diamniadio",
            icon=folium.Icon(color="green")
        ).add_to(ma_carte)

    # ==========================
    # BRT
    # ==========================

    if filtre in ["Tous", "BRT"]:

        brt_points = [
            [14.6920, -17.4460],  # Petersen
            [14.7150, -17.4300],
            [14.7450, -17.4100],
            [14.7800, -17.3950]   # Guédiawaye
        ]

        folium.PolyLine(
            brt_points,
            color="blue",
            weight=5,
            tooltip="Ligne BRT Petersen - Guédiawaye"
        ).add_to(ma_carte)

        folium.Marker(
            [14.6920, -17.4460],
            popup="🚌 Terminus BRT Petersen",
            icon=folium.Icon(color="blue")
        ).add_to(ma_carte)

        folium.Marker(
            [14.7800, -17.3950],
            popup="🚌 Terminus BRT Guédiawaye",
            icon=folium.Icon(color="blue")
        ).add_to(ma_carte)

    # ==========================
    # NAVETTES JOJ
    # ==========================

    if filtre in ["Tous", "Navettes JOJ"]:

        folium.Marker(
            [14.7100, -17.3500],
            popup="""
🚌 Navette JOJ

Trajet :
Dakar ➜ Stade Abdoulaye Wade
""",
            tooltip="Navette JOJ",
            icon=folium.Icon(color="cadetblue")
        ).add_to(ma_carte)

        folium.Marker(
            [14.5800, -17.1200],
            popup="""
🚌 Navette JOJ

Trajet :
Diamniadio ➜ Saly
""",
            tooltip="Navette JOJ",
            icon=folium.Icon(color="cadetblue")
        ).add_to(ma_carte)

    # ==========================
    # PERTURBATIONS
    # ==========================

    if filtre in ["Tous", "Perturbations"]:

        folium.Marker(
            [14.7050, -17.3650],
            popup="""
⚠️ Embouteillage

Autoroute Dakar - Diamniadio

Retard estimé : 20 min
""",
            tooltip="Embouteillage",
            icon=folium.Icon(color="darkred")
        ).add_to(ma_carte)

        folium.Marker(
            [14.7250, -17.2600],
            popup="""
🚧 Travaux

Accès ralenti vers le Stade Abdoulaye Wade
""",
            tooltip="Travaux",
            icon=folium.Icon(color="orange")
        ).add_to(ma_carte)

    st_folium(
        ma_carte,
        use_container_width=True,
        height=550
    )

    st.divider()
    # ==========================
    # SIGNALEMENT
    # ==========================

    st.subheader("⚠️ Signaler un problème")

    with st.form("form_incident"):

        type_incident = st.selectbox(
            "Type de problème",
            [
                "Embouteillage",
                "Retard de navette",
                "Accident",
                "Travaux",
                "Route fermée",
                "Autre"
            ]
        )

        gravite = st.select_slider(
            "Niveau de gravité",
            options=[
                "Faible",
                "Moyenne",
                "Élevée"
            ]
        )

        description = st.text_area(
            "Décrivez le problème"
        )

        envoyer = st.form_submit_button(
            "📤 Envoyer"
        )

        if envoyer:

            if description.strip() == "":

                st.error(
                    "Veuillez ajouter une description."
                )

            else:

                st.success(
                    "Signalement envoyé avec succès ✅"
                )

                st.info(f"""
Type : {type_incident}

Gravité : {gravite}

Description : {description}
""")

    st.divider()

    # ==========================
    # HISTORIQUE
    # ==========================

    st.subheader("📜 Dernières alertes")

    st.warning(
        "🚗 Ralentissement sur l'autoroute Dakar - Diamniadio."
    )

    st.info(
        "🚌 Retard de 10 minutes des navettes JOJ."
    )

    st.error(
        "🚧 Travaux à proximité du Stade Abdoulaye Wade."
    )

    st.success(
        "✅ Trafic fluide sur la ligne TER Dakar - Diamniadio."
    ) 
#==========================================================
# PAGE 3 : ZONE SOS
#==========================================================
elif page == "🚨 Assistance & SOS":

    st.header("🚨 Assistance & Urgences")

    st.error(
        "En cas d'urgence, utilisez cette rubrique pour contacter les secours et signaler rapidement un incident."
    )

    st.divider()

    # =====================================
    # CONTACTS D'URGENCE
    # =====================================

    st.subheader("📞 Contacts d'urgence")

    col1, col2 = st.columns(2)

    with col1:

        st.info("🚔 Police Secours")
        st.code("17")

        st.info("🚒 Sapeurs-Pompiers")
        st.code("18")

    with col2:

        st.info("🚑 SAMU National")
        st.code("1515")

        st.info("🏅 Assistance JOJ")
        st.code("Agents présents sur tous les sites")

    st.divider()

    # =====================================
    # ALERTE SOS
    # =====================================

    st.subheader("🚨 Déclencher une alerte SOS")

    type_urgence = st.selectbox(
        "Type d'urgence",
        [
            "Accident de transport",
            "Malaise",
            "Agression",
            "Enfant perdu",
            "Navette en panne",
            "Incendie",
            "Autre"
        ]
    )

    niveau = st.select_slider(
        "Niveau de priorité",
        options=[
            "Faible",
            "Moyenne",
            "Élevée",
            "Critique"
        ]
    )

    localisation = st.selectbox(
        "📍 Localisation",
        [
            "Stade Abdoulaye Wade",
            "Dakar Arena",
            "Complexe Iba Mar Diop",
            "Saly",
            "Autoroute Dakar - Diamniadio",
            "Autre"
        ]
    )

    details = st.text_area(
        "📝 Décrivez brièvement la situation"
    )

    envoyer_sos = st.button(
        "🚨 Envoyer l'alerte"
    )

    if envoyer_sos:

        st.success(
            "Alerte transmise avec succès ✅"
        )

        st.warning(f"""
🚨 Type : {type_urgence}

📍 Lieu : {localisation}

⚠️ Priorité : {niveau}

📡 Les équipes d'assistance ont été notifiées.
""")

    st.divider()

    # =====================================
    # TEMPS D'INTERVENTION
    # =====================================

    st.subheader("⏱️ Temps d'intervention estimé")

    if niveau == "Critique":
        temps = "3 min"

    elif niveau == "Élevée":
        temps = "5 min"

    elif niveau == "Moyenne":
        temps = "10 min"

    else:
        temps = "15 min"

    st.metric(
        "Temps estimé",
        temps
    )

    st.divider()

    # =====================================
    # CENTRES D'ASSISTANCE
    # =====================================

    st.subheader("🏥 Centres d'assistance")

    st.success(
        "🏥 Poste médical du Stade Abdoulaye Wade (Diamniadio)"
    )

    st.success(
        "🏥 Centre d'assistance Dakar Arena"
    )

    st.success(
        "🏥 Poste de secours de Saly"
    )

    st.success(
        "🏥 Unité mobile Teranga Mobile"
    )

    st.divider()

    # =====================================
    # SUIVI D'INTERVENTION
    # =====================================

    st.subheader("📡 Suivi de l'intervention")

    progression = 75

    st.progress(progression)

    st.warning(
        "🚑 Une équipe d'intervention est actuellement en route."
    )

    st.divider()

    # =====================================
    # CONSEILS DE SÉCURITÉ
    # =====================================

    st.subheader("🛟 Conseils pratiques")

    with st.expander("🚌 Incident de transport"):

        st.write("""
• Restez calme et éloignez-vous du danger

• Prévenez immédiatement les agents Teranga Mobile

• Attendez les secours dans une zone sécurisée
""")

    with st.expander("❤️ Malaise ou blessure"):

        st.write("""
• Mettre la personne à l'abri

• Appeler rapidement le SAMU

• Ne pas déplacer la victime inutilement
""")

    with st.expander("👶 Enfant perdu"):

        st.write("""
• Informer immédiatement les agents JOJ

• Décrire précisément les vêtements

• Rester au point de rencontre indiqué
""")

    with st.expander("🔥 Incendie"):

        st.write("""
• Quitter la zone immédiatement

• Éviter les mouvements de foule

• Appeler les sapeurs-pompiers
""")

    st.divider()

# =========================================================
# PAGE 4 : RESTAURATION
# =========================================================
elif page == "🍽️ Restauration":

    st.header("🍽️ Food Zones JOJ Dakar 2026")

    st.write(
        "Découvrez les restaurants, spécialités culinaires et espaces de restauration situés à proximité des sites des Jeux Olympiques de la Jeunesse Dakar 2026."
    )

    st.divider()

    # =====================================
    # CHOIX DU SITE
    # =====================================

    stade = st.selectbox(
        "🏟️ Choisir un site",
        [
            "Stade Abdoulaye Wade",
            "Dakar Arena",
            "Complexe Iba Mar Diop",
            "Saly"
        ]
    )

    st.divider()

    # =====================================
    # GASTRONOMIE SÉNÉGALAISE
    # =====================================

    st.subheader("🇸🇳 Découvrir la gastronomie sénégalaise")

    plats_senegalais = [
        "🍚 Thiéboudiène",
        "🍗 Yassa Poulet",
        "🥩 Mafé",
        "🐟 Poisson braisé",
        "🥟 Fataya",
        "🥤 Jus de Bissap",
        "🌺 Jus de Bouye",
        "🥣 Couscous de Mil"
    ]

    for plat in plats_senegalais:
        st.write(plat)

    st.divider()

    # =====================================
    # RESTAURANTS RECOMMANDÉS
    # =====================================

    st.subheader("🍴 Restaurants recommandés")

    if stade == "Stade Abdoulaye Wade":

        st.success("🍚 Restaurant Teranga Diamniadio")
        st.write("⭐ 4.8/5")
        st.write("📍 À proximité du stade")
        st.write("⏳ Temps d'attente moyen : 10 min")

        st.info("🍔 Fast Food Arena")
        st.warning("☕ Café des Supporters")

    elif stade == "Dakar Arena":

        st.success("🥘 Saveurs du Sénégal")
        st.info("🍕 Pizza Arena")
        st.warning("🥤 Olympic Food Corner")

    elif stade == "Complexe Iba Mar Diop":

        st.success("🐟 La Terrasse Dakaroise")
        st.info("🍗 Yassa Express")
        st.warning("☕ Café Sportif")

    elif stade == "Saly":

        st.success("🦐 Restaurant de la Plage")
        st.info("🐟 Saly Seafood")
        st.warning("🥥 Tropical Café")

    st.divider()
    # =====================================
    # MENU JOJ
    # =====================================

    st.subheader("📋 Menu JOJ")

    menu = {
        "Thiéboudiène": 3500,
        "Yassa Poulet": 3000,
        "Mafé": 3000,
        "Fataya": 500,
        "Jus de Bissap": 1000
    }

    for nom, prix in menu.items():
        st.write(f"🍽️ {nom} — {prix} FCFA")

    st.divider()
    # =====================================
    # CONSEIL DU JOUR
    # =====================================

    st.subheader("💡 Conseil du jour")

    st.success(
        "🍚 Ne quittez pas le Sénégal sans goûter au Thiéboudiène, plat emblématique classé au patrimoine culturel de l’UNESCO."
    )

    st.divider()

    # =====================================
    # AVIS CLIENTS
    # =====================================

    st.subheader("⭐ Votre avis")

    note = st.slider(
        "Donnez une note",
        1,
        5,
        4
    )

    commentaire = st.text_area(
        "Votre commentaire"
    )

    if st.button("Envoyer l'avis"):
        st.success("Merci pour votre avis !")

    st.divider()

    # =====================================
    # PASSEPORT GASTRONOMIQUE
    # =====================================

    st.subheader("🏅 Passeport Gastronomique")

    plats_testes = st.slider(
        "Nombre de spécialités sénégalaises goûtées",
        0,
        5,
        0
    )

    if plats_testes >= 3:

        st.success(
            "🏅 Badge Découverte de la Gastronomie Sénégalaise obtenu !"
        )

    st.divider()

    # =====================================
    # ASSISTANT FOOD
    # =====================================

    st.subheader("🤖 Assistant Food")

    question_food = st.text_input(
        "Que souhaitez-vous manger ?"
    )

    if question_food:

        if "poisson" in question_food.lower():

            st.info(
                "🍚 Nous vous recommandons le Thiéboudiène."
            )

        elif "poulet" in question_food.lower():

            st.info(
                "🍗 Nous vous recommandons le Yassa Poulet."
            )

        else:

            st.info(
                "🇸🇳 Découvrez les spécialités culinaires sénégalaises proposées."
            )

    st.divider()
#==========================================================
# PAGE 5 : Itineraire Intelligent
#==========================================================
elif page == "🚍 Itinéraire Intelligent":

    st.header("🚍 Itinéraire Intelligent")

    st.write(
        "Planifiez votre déplacement vers les sites officiels des JOJ Dakar 2026."
    )

    st.divider()

    # ==========================
    # CHOIX TRAJET
    # ==========================

    depart = st.selectbox(
        "📍 Point de départ",
        [
            "Plateau",
            "Pikine",
            "Guédiawaye",
            "Parcelles Assainies",
            "Diamniadio",
            "Aéroport AIBD"
        ]
    )

    destination = st.selectbox(
        "🎯 Destination",
        [
            "Stade Me Abdoulaye Wade",
            "Dakar Arena",
            "Dakar Expo Center (CICAD)",
            "Complexe Tour de l’Œuf",
            "Stade Iba Mar Diop",
            "Saly Beach West"
        ]
    )

    transport = st.radio(
        "🚆 Moyen de transport préféré",
        [
            "Le plus rapide",
            "Le moins cher",
            "TER",
            "BRT",
            "Navette JOJ"
        ]
    )

    st.divider()

    # ==========================
    # CALCUL ITINÉRAIRE
    # ==========================

    if st.button("🔍 Calculer l'itinéraire"):

        if destination == "Stade Me Abdoulaye Wade":
            trajet = "🚆 TER jusqu'à Diamniadio puis marche"
            temps = 30
            cout = 1000

        elif destination == "Dakar Arena":
            trajet = "🚆bus ou Taxi"
            temps = 35
            cout = 1000

        elif destination == "Dakar Expo Center (CICAD)":
            trajet = "🚆 TER puis navette JOJ"
            temps = 35
            cout = 1200

        elif destination == "Complexe Tour de l’Œuf":
            trajet = "🚌 BRT"
            temps = 20
            cout = 500

        elif destination == "Stade Iba Mar Diop":
            trajet = "🚌 BRT"
            temps = 15
            cout = 500

        else:  # Saly Beach West
            trajet = "🏅 Navette JOJ spéciale"
            temps = 60
            cout = 2500

        st.success("Itinéraire trouvé ✅")

        st.info(f"""
📍 Départ : {depart}

🎯 Destination : {destination}

🚍 Trajet recommandé : {trajet}

⏱ Temps estimé : {temps} min

💰 Coût estimé : {cout} FCFA
""")

        st.progress(min(temps, 100))

    st.divider()
    # ==========================
    # FAVORIS
    # ==========================

    st.subheader("⭐ Trajets favoris")

    favoris = st.checkbox(
        "Ajouter ce trajet aux favoris"
    )

    if favoris:

        st.success(
            "Trajet ajouté aux favoris ✅"
        )

    st.divider()

    # ==========================
    # HISTORIQUE
    # ==========================

    st.subheader("🕘 Historique récent")

    st.write(
        "📍 Plateau → Stade Me Abdoulaye Wade"
    )

    st.write(
        "📍 Pikine → Dakar Arena"
    )

    st.write(
        "📍 Aéroport AIBD → Dakar Expo Center (CICAD)"
    ) 
# =========================================================
# PAGE 6 : Mes billets
#==========================================================
elif page == "🎟️ Mes Billets":
    # =========================================================
    #calendrier des joj 
    #=========================================================  
    st.header("📅 Calendrier des JOJ Dakar 2026")

    st.write(
        "Retrouvez les principales compétitions des Jeux Olympiques de la Jeunesse Dakar 2026."
    )

    st.success(
        "📍 JOJ Dakar 2026 : du 31 octobre au 13 novembre 2026"
    )

    st.divider()

    st.subheader("🗓️ Programme des compétitions")

    calendrier = {
        "1 - 4 novembre": {
            "🏉 Rugby à 7": "Complexe Iba Mar Diop - Dakar"
        },

        "1 - 5 novembre": {
            "⚽ Futsal": "Complexe Iba Mar Diop - Dakar"
        },

        "1 - 6 novembre": {
            "🏊 Natation": "Dakar"
        },

        "8 - 10 novembre": {
            "🏃 Athlétisme": "Complexe Iba Mar Diop - Dakar"
        },

        "10 - 12 novembre": {
            "🥋 Taekwondo": "Dakar Expo Center - Diamniadio"
        }
    }

    for date, epreuves in calendrier.items():

        with st.expander(f"📆 {date}"):

            for discipline, lieu in epreuves.items():

                st.write(f"**{discipline}**")
                st.write(f"📍 {lieu}")
                st.write("---")

    st.divider()

    st.subheader("🏙️ Villes hôtes")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("📍 Dakar")

    with col2:
        st.info("📍 Diamniadio")

    with col3:
        st.info("📍 Saly")

    st.divider()

    st.subheader("📊 Compte à rebours")

    st.metric(
        "Durée des Jeux",
        "14 jours"
    )

    st.metric(
        "Villes hôtes",
        "3"
    )

    st.metric(
        "Sports officiels",
        "25"
    )

    st.divider()

    st.subheader("ℹ️ Informations")

    st.info(
        "Les compétitions se dérouleront dans plusieurs sites emblématiques de Dakar, Diamniadio et Saly."
    )
    st.header("🎟️ Billetterie JOJ Dakar 2026")

    st.write(
        "Consultez et gérez vos billets pour les événements des Jeux Olympiques de la Jeunesse Dakar 2026."
    )

    st.warning(
        "⚠️ Les tarifs officiels des billets n'ont pas encore été publiés par le comité d'organisation des JOJ Dakar 2026."
    )

    st.divider()

    # ==========================
    # INFORMATIONS VISITEUR
    # ==========================

    nom = st.text_input(
        "👤 Nom du visiteur"
    )

    competition = st.selectbox(
        "🏅 Événement",
        [
            "Cérémonie d'ouverture - Stade Léopold Sédar Senghor",
            "Tournoi de Football - Dakar Arena",
            "Basketball 3x3 - Place du Souvenir Africain",
            "Natation - Piscine Olympique Nationale",
            "Forum de la Jeunesse - CICAD",
            "Athlétisme - Stade Me Abdoulaye Wade",
            "Esports et Innovation - Parc des Expositions",
            "Festival Culturel Teranga - Place du Souvenir Africain",
            "Sports de plage - Saly Beach",
            "Voile - Port de Saly",
            "Journée du Tourisme - Village Artisanal",
            "Cérémonie de clôture - Stade Me Abdoulaye Wade"
        ]
    )

    date_evenement = st.date_input(
        "📅 Date de l'événement"
    )

    nombre = st.number_input(
        "🎫 Nombre de billets",
        min_value=1,
        max_value=10,
        value=1
    )

    st.divider()

    # ==========================
    # TARIFICATION
    # ==========================

    st.subheader("💰 Informations tarifaires")

    st.info(
        """
Les tarifs officiels des billets des JOJ Dakar 2026
ne sont pas encore disponibles.

Les informations tarifaires seront ajoutées
dès leur publication officielle.
"""
    )

    st.divider()

    # ==========================
    # GÉNÉRATION DU BILLET
    # ==========================

    if st.button("🎟️ Générer mon billet"):

        if nom.strip() == "":

            st.error(
                "Veuillez saisir votre nom."
            )

        else:

            st.success(
                "Billet généré avec succès ✅"
            )

            code_billet = (
                f"DAKAR2026-"
                f"{competition[:4].upper()}-"
                f"{date_evenement.strftime('%d%m')}"
            )

            st.info(f"""
👤 Nom : {nom}

🏅 Événement : {competition}

📅 Date : {date_evenement}

🎫 Nombre de billets : {nombre}

💰 Tarif : En attente de publication officielle

🎟️ Référence : {code_billet}
""")

            st.code(code_billet)

    st.divider()

    # ==========================
    # CONTRÔLE D'ACCÈS
    # ==========================

    st.subheader("📱 Contrôle d'accès")

    st.success(
        "QR Code simulé prêt pour le contrôle à l'entrée."
    )

    st.progress(100)

    st.divider()

    # ==========================
    # HISTORIQUE
    # ==========================

    st.subheader("📜 Historique des billets")

    st.write(
        "🎫 Tournoi de Football - Dakar Arena - 2 novembre 2026"
    )

    st.write(
        "🎫 Athlétisme - Stade Me Abdoulaye Wade - 8 novembre 2026"
    )

    st.write(
        "🎫 Festival Culturel Teranga - 10 novembre 2026"
    )

    st.divider()

    # ==========================
    # INFORMATIONS BILLETTERIE
    # ==========================

    st.subheader("ℹ️ Informations billetterie")

    st.info(
        """
Les données de billetterie présentées dans cette application
sont fournies à titre de démonstration.

Les modalités de réservation, les tarifs officiels
et les disponibilités seront communiqués par le comité
d'organisation des JOJ Dakar 2026.
"""
    )
#==========================================================
# PAGE 7 : Assistant Teranga
#==========================================================
elif page == "🤖 Assistant Teranga":

    st.header("🤖 Assistant Teranga")

    st.write(
        "Posez vos questions sur les transports, la restauration ou les JOJ."
    )

    st.divider()

    question = st.text_input(
        "💬 Votre question"
    )

    if question:

        question = question.lower()

        if "ter" in question:

            st.success("""
🚆 TER

Service actif de 05h00 à 22h00.

Liaison principale :
Dakar ↔ Diamniadio.
""")

        elif "brt" in question:

            st.success("""
🚌 BRT

Service actif de 05h00 à 21h00.

Des renforts sont déployés aux heures de pointe.
""")


        elif "stade" in question:

            st.info("""
🏟️ Stade Abdoulaye Wade

Site principal des JOJ Dakar 2026.
""")

        elif "bonjour" in question:

            st.success(
                "👋 Bonjour et bienvenue aux JOJ Dakar 2026 !"
            )

        else:

            st.warning(
                "Je n'ai pas trouvé de réponse précise. Essayez une question sur le TER, le BRT, les restaurants ou les urgences."
            )

    st.divider()

    # =====================================
    # QUESTIONS RAPIDES
    # =====================================

    st.subheader("⚡ Questions fréquentes")

    faq = st.selectbox(
        "Choisissez une question",
        [
            "Comment aller au Stade Abdoulaye Wade ?",
            "Quels sont les horaires du TER ?",
            "Où manger près du Village Olympique ?",
            "Comment contacter les secours ?"
        ]
    )

    if st.button("Afficher la réponse"):

        if faq == "Comment aller au Stade Abdoulaye Wade ?":

            st.info("""
🚆 TER jusqu'à Diamniadio

🚌 Navette JOJ jusqu'au stade
""")

        elif faq == "Quels sont les horaires du TER ?":

            st.info("""
🚆 TER

05h00 → 22h00
""")

        elif faq == "Où manger près du Village Olympique ?":

            st.info("""
🍽️ Teranga Buffet

🍗 Chicken Express

🥪 Olympic Snack Zone
""")

        elif faq == "Comment contacter les secours ?":

            st.error("""
🚑 SAMU : 1515

🚒 Pompiers : 18

👮 Police : 17
""")

    st.divider()
    # =====================================
    # LANGUES
    # =====================================

    st.subheader("🌍 Langue")

    langue = st.selectbox(
        "Choisir une langue",
        [
            "🇫🇷 Français",
            "🇬🇧 English",
            "🇸🇳 Wolof"
        ]
    )

    st.success(
        f"Langue sélectionnée : {langue}"
    )
#=========================================================
# PAGE 8 : SN DECOUVRIR LE SÉNÉGAL
#=========================================================

elif page == "🇸🇳 Découvrir le Sénégal":

    st.header("🇸🇳 Découvrir le Sénégal")

    st.write(
        "Bienvenue au pays de la Teranga ! Découvrez la culture, les traditions et les lieux incontournables du Sénégal durant les JOJ Dakar 2026."
    )

    st.divider()

    # =====================================
    # SITES TOURISTIQUES
    # =====================================

    st.subheader("📍 Sites incontournables")

    site = st.selectbox(
        "Choisir un site",
        [
            "Île de Gorée",
            "Monument de la Renaissance Africaine",
            "Lac Rose",
            "Réserve de Bandia",
            "Delta du Saloum"
        ]
    )

    if site == "Île de Gorée":
        st.info(
            "🏝️ Site historique classé au patrimoine mondial de l'UNESCO. Symbole de mémoire et de paix."
        )

    elif site == "Monument de la Renaissance Africaine":
        st.info(
            "🗿 Monument emblématique de Dakar offrant une vue panoramique sur la ville."
        )

    elif site == "Lac Rose":
        st.info(
            "🌸 Anciennement célèbre pour sa couleur rosée et ses paysages uniques."
        )

    elif site == "Réserve de Bandia":
        st.info(
            "🦒 Réserve naturelle où l'on peut observer girafes, zèbres, antilopes et rhinocéros."
        )

    elif site == "Delta du Saloum":
        st.info(
            "🌊 Réserve de biosphère classée à l'UNESCO, réputée pour sa biodiversité."
        )

    st.divider()
elif page == "🦁 Guide Teranga":

    st.header("🦁 Guide Teranga")

    st.write(
        "Découvrez les informations essentielles pour profiter pleinement des JOJ Dakar 2026."
    )

    st.divider()

    # ==========================
    # LIEUX UTILES
    # ==========================

    st.subheader("📍 Lieux utiles")

    st.write("🏟️ Stade Me Abdoulaye Wade (Diamniadio)")
    st.write("🏀 Dakar Arena (Diamniadio)")
    st.write("🏛️ Centre International de Conférences Abdou Diouf (CICAD)")
    st.write("🚆 Gare TER de Dakar")
    st.write("✈️ Aéroport International Blaise Diagne (AIBD)")
    st.write("🏖️ Saly Beach West")

    st.divider()

    # ==========================
    # CONSEILS VISITEURS
    # ==========================

    st.subheader("🍽️ Conseils visiteurs")

    st.write("• Utiliser le TER pour rejoindre rapidement Diamniadio.")
    st.write("• Arriver au moins 1 heure avant le début des compétitions.")
    st.write("• Prévoir une bouteille d'eau réutilisable.")
    st.write("• Scanner les QR codes des navettes officielles JOJ.")
    st.write("• Respecter les consignes de sécurité sur les sites.")
    st.write("• Garder une pièce d'identité sur soi.")

    st.divider()

    # ==========================
    # LANGUES UTILES
    # ==========================

    st.subheader("🌍 Langues utiles")

    st.write("🇸🇳 Wolof : Bienvenue → 'Dalal ak jamm'")
    st.write("🇫🇷 Français : langue officielle")
    st.write("🇬🇧 English : Welcome")
    st.write("🇪🇸 Español : Bienvenido")

    st.divider()
    # ==========================
    # CULTURE SÉNÉGALAISE
    # ==========================

    st.subheader("🎭 Culture sénégalaise")

    st.info(
        "La Teranga est une valeur essentielle du Sénégal. "
        "Elle représente l'hospitalité, le respect et le partage envers les visiteurs."
    )
    # =====================================
    # GASTRONOMIE
    # =====================================

    st.subheader("🍽️ Cuisine Sénégalaise")

    plats = [
        "🍚 Thiéboudiène",
        "🍗 Yassa Poulet",
        "🥩 Mafé",
        "🥟 Fataya",
        "🥤 Jus de Bissap"
    ]

    for plat in plats:
        st.write(plat)

    st.divider()

    # =====================================
    # WOLOF
    # =====================================

    st.subheader("🗣️ Quelques mots en Wolof")

    expressions = {
        "Bonjour": "Salaam Aleekum",
        "Merci": "Jërëjëf",
        "Comment ça va ?": "Nanga def ?",
        "Bienvenue": "Dalal ak jamm"
    }

    for francais, wolof in expressions.items():
        st.write(f"🇫🇷 {francais} → 🇸🇳 {wolof}")

    st.divider()

    # =====================================
    # CULTURE
    # =====================================

    st.subheader("🎶 Culture Sénégalaise")

    st.success("🥁 Musique traditionnelle et moderne")
    st.success("💃 Danses traditionnelles")
    st.success("🎨 Artisanat local")
    st.success("🤝 Hospitalité légendaire : la Teranga")

    st.divider()

    # =====================================
    # INFORMATIONS PAYS
    # =====================================

    st.subheader("📊 Le Sénégal en chiffres")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Population", "18 M")

    with col2:
        st.metric("Capitale", "Dakar")

    with col3:
        st.metric("Langue officielle", "Français")

    st.divider()

    # =====================================
    # QUIZ
    # =====================================

    st.subheader("🎯 Quiz Sénégal")

    reponse = st.radio(
        "Quel est le plat national du Sénégal ?",
        [
            "Pizza",
            "Thiéboudiène",
            "Hamburger"
        ]
    )

    if st.button("Valider"):

        if reponse == "Thiéboudiène":
            st.success("Bonne réponse ! 🎉")
        else:
            st.error("Mauvaise réponse.")
#==========================================================
# PAGE 9: GUIDE TERANGA
#==========================================================
elif page == "🦁 Guide Teranga":

    st.header("🦁 Guide Teranga")

    st.write(
        "Votre compagnon officiel pour découvrir Dakar et profiter pleinement des JOJ 2026."
    )

    st.divider()

    # =====================================
    # SITES JOJ
    # =====================================

    st.subheader("🏟️ Sites JOJ")

    st.write("🏟️ Stade Abdoulaye Wade")
    st.write("🏊 Piscine Olympique")
    st.write("🏘️ Village Olympique")
    st.write("🚆 Gare TER Dakar")

    st.divider()

    # =====================================
    # CONSEILS MOBILITE
    # =====================================

    st.subheader("🚍 Conseils de déplacement")

    st.success(
        "Utilisez le TER pour rejoindre rapidement Diamniadio."
    )

    st.info(
        "Privilégiez les navettes JOJ aux heures de pointe."
    )

    st.warning(
        "Arrivez au moins 30 minutes avant les compétitions."
    )

    st.divider()

    # =====================================
    # INFORMATIONS PRATIQUES
    # =====================================

    st.subheader("💵 Informations utiles")

    col1, col2 = st.columns(2)

    with col1:
        st.write("💰 Monnaie : FCFA")
        st.write("🕒 Fuseau horaire : GMT")

    with col2:
        st.write("📞 Indicatif : +221")
        st.write("🗣️ Langue officielle : Français")

    st.divider()

    # =====================================
    # CONTACTS UTILES
    # =====================================

    st.subheader("📞 Contacts d'urgence")

    col1, col2 = st.columns(2)

    with col1:

        st.info("👮 Police")
        st.code("17")

        st.info("🚒 Pompiers")
        st.code("18")

    with col2:

        st.info("🚑 SAMU")
        st.code("1515")

        st.info("🆘 Assistance JOJ")
        st.code("+221 77 000 2026")

    st.divider()

    # =====================================
    # MINI TRADUCTEUR WOLOF
    # =====================================

    st.subheader("🗣️ Expressions utiles")

    mot = st.selectbox(
        "Choisissez une expression",
        [
            "Bonjour",
            "Merci",
            "Bienvenue",
            "Comment ça va ?",
            "Au revoir"
        ]
    )

    traductions = {

        "Bonjour": "Salaam Aleekum",

        "Merci": "Jërëjëf",

        "Bienvenue": "Dalal ak jamm",

        "Comment ça va ?": "Nanga def ?",

        "Au revoir": "Ba beneen yoon"
    }

    st.success(
        f"🇸🇳 {traductions[mot]}"
    )

    st.divider()

    # =====================================
    # CONSEILS VISITEURS
    # =====================================

    st.subheader("🌍 Conseils visiteurs")

    st.write("🥤 Hydratez-vous régulièrement.")

    st.write("☀️ Portez une casquette lors des compétitions extérieures.")

    st.write("📱 Gardez votre billet électronique à portée de main.")

    st.write("🚌 Vérifiez les horaires du TER et du BRT avant vos déplacements.")

    st.write("🤝 Respectez les consignes des bénévoles et des agents JOJ.")

    st.divider()

    # =====================================
    # CULTURE SENEGALAISE
    # =====================================

    st.subheader("🇸🇳 La Teranga Sénégalaise")

    st.info("""
La Teranga est une valeur fondamentale du Sénégal.

Elle représente l'accueil, le partage,
la solidarité et l'hospitalité envers les visiteurs.
""")

    st.divider()

    # =====================================
    # BADGES VISITEURS
    # =====================================

    st.subheader("🏅 Badges obtenus")

    st.success("🏅 Badge Mobilité")

    st.success("🏅 Badge Découverte")

    st.success("🏅 Badge Teranga")

    st.divider()

    # =====================================
    # MESSAGE FINAL
    # =====================================

    st.success(
        "🇸🇳 Toute l'équipe Dakar 2026 vous souhaite un excellent séjour au Sénégal !"
    )
st.divider()

st.markdown("""
<div style='text-align:center;'>

🇸🇳 Dakar JOJ 2026 — Teranga Mobile

Développé pour améliorer la mobilité, la sécurité et l'expérience des visiteurs.

Version 1.0

</div>
""", unsafe_allow_html=True)
