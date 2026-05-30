import streamlit as st
import folium
import qrcode
import time
import pandas as pd
import math
from streamlit_folium import st_folium
from datetime import datetime
from PIL import Image

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
# 🎬 SPLASH SCREEN
# =========================================================

if "splash_done" not in st.session_state:

    placeholder = st.empty()

    with placeholder.container():

        st.markdown("""
        <style>
        .main { background-color: #0e1117; }
        </style>
        """, unsafe_allow_html=True)

        st.markdown("<br><br>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            try:
                st.image("accueil.png.jpeg", use_container_width=True)
            except Exception:
                st.markdown("🇸🇳", unsafe_allow_html=False)

        st.markdown("""
        <div style="text-align:center; padding:20px;">
            <h1 style="color:#00d4ff; font-size:55px; font-weight:bold; margin-bottom:10px;">
                🇸🇳 BIENVENUE AU SÉNÉGAL
            </h1>
            <h3 style="color:white; font-style:italic; margin-bottom:30px;">
                DALL LEEN AK DIAM CI SENEGAL
            </h3>
            <div style="background: linear-gradient(135deg,#00d4ff,#007cf0); padding:18px; border-radius:15px; color:white; font-size:20px; font-weight:bold; width:60%; margin:auto; box-shadow:0px 4px 15px rgba(0,0,0,0.3);">
                ⏳ Chargement de Teranga Mobile...
            </div>
        </div>
        """, unsafe_allow_html=True)

    time.sleep(3)
    st.session_state["splash_done"] = True
    placeholder.empty()

# =========================================================
# PAGE DE CONNEXION
# =========================================================

if "connecte" not in st.session_state:
    st.session_state["connecte"] = False

if not st.session_state["connecte"]:

    import base64

    # ======================================
    # FONCTION POUR L'IMAGE DE FOND
    # ======================================

    def get_base64_image(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()

    image_base64 = get_base64_image("mon_accueil.png")

    # ======================================
    # CSS ARRIERE-PLAN
    # ======================================

    st.markdown(
        f"""
        <style>

        .stApp {{
            background-image: url("data:image/jpeg;base64,{image_base64}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        .login-box {{
            background-color: rgba(0, 0, 0, 0.65);
            padding: 40px;
            border-radius: 20px;
            margin-top: 40px;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

    # ======================================
    # CONTENU PAGE CONNEXION
    # ======================================

    st.markdown(
        """
        <div class="login-box">

        <h1 style="
            text-align:center;
            color:#00d4ff;
            font-size:55px;
            font-weight:bold;
        ">
            🇸🇳 BIENVENUE AU SÉNÉGAL
        </h1>

        <h3 style="
            text-align:center;
            color:white;
            font-style:italic;
            margin-bottom:30px;
        ">
            DALL LEEN AK DIAM CI SENEGAL
        </h3>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("## 👤 Connexion utilisateur")

    nom = st.text_input("Nom")
    prenom = st.text_input("Prénom")

    langue = st.selectbox(
        "🌍 Choisissez une langue",
        ["Français", "English", "Español"]
    )

    if st.button("🔓 Accéder à Teranga Mobile"):

        if nom == "" or prenom == "":
            st.error("⚠️ Veuillez remplir tous les champs.")

        else:
            st.session_state["connecte"] = True
            st.session_state["nom"] = nom
            st.session_state["prenom"] = prenom
            st.session_state["langue"] = langue

            st.rerun()

# =========================================================
# APPLICATION PRINCIPALE
# =========================================================

else:

    st.success(f"Bienvenue {st.session_state['prenom']} {st.session_state['nom']} 👋")

    # HEADER
    st.markdown("""
    <div style="background: linear-gradient(135deg,#007cf0,#00dfd8); padding:25px; border-radius:18px; text-align:center; color:white; box-shadow:0px 4px 15px rgba(0,0,0,0.3);">
        <h1>🇸🇳 Dakar 2026 — Teranga Mobile</h1>
        <p style="font-size:20px;">Prototype de mobilité intelligente pour les JOJ 2026</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # MESSAGE SELON L'HEURE
    if heure_actuelle < 12:
        st.success("☀️ Bonjour et bienvenue !")
    elif heure_actuelle < 18:
        st.success("🌤️ Bon après-midi !")
    else:
        st.success("🌙 Bonne soirée !")

    st.markdown(f"""
    <div style="background-color:#1f2937; padding:15px; border-radius:12px; text-align:center; color:white; font-size:18px; margin-top:10px;">
        📅 {datetime.now().strftime('%d/%m/%Y')} &nbsp;&nbsp;&nbsp;&nbsp; 🕒 {datetime.now().strftime('%H:%M')}
    </div>
    """, unsafe_allow_html=True)

    # SIDEBAR
    st.sidebar.markdown("""
    <h2 style='text-align:center; color:#00d4ff;'>🦁 Ayo</h2>
    """, unsafe_allow_html=True)

    try:
        st.sidebar.image("AYO.png", width=200)
    except Exception:
        pass

    st.sidebar.success("Mascotte officielle des JOJ Dakar 2026")
    st.sidebar.markdown("---")
    st.sidebar.info("🏅 Visiteur JOJ")
    st.sidebar.success("Niveau : Explorateur")
    st.sidebar.markdown("---")

    page = st.sidebar.radio(
        "📍 Navigation",
        [
            "🏠 Accueil & Trafic",
            "🗺️ Carte & Signalements",
            "🚨 Zone SOS",
            "🍽️ Restauration",
            "🎟️ Mes Billets",
            "🦁 Guide Teranga"
        ]
    )

    # =========================================================
    # PAGE 1 : ACCUEIL & TRAFIC
    # =========================================================

    if page == "🏠 Accueil & Trafic":

        st.header("🚦 État du Réseau")

        etat_ter = "Fermé" if (heure_actuelle >= 22 or heure_actuelle < 5) else "Ouvert"
        icone_ter = "🔴" if etat_ter == "Fermé" else "🟢"

        etat_brt = "Fermé" if (heure_actuelle >= 21 or heure_actuelle < 5) else "Ouvert"
        icone_brt = "🔴" if etat_brt == "Fermé" else "🟢"

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
            nb_brt, nb_ter = 158, 27
            message = "Renforcement spécial heure de pointe"
        elif 6 <= heure_actuelle <= 9:
            nb_brt, nb_ter = 100, 18
            message = "Renforcement du service matinal"
        else:
            nb_brt, nb_ter = 70, 15
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

        st.subheader("😊 Satisfaction voyageurs")
        satisfaction = st.slider("Note moyenne", 1, 5, 4)
        st.success(f"Satisfaction moyenne : {satisfaction}/5")

       # =========================================================
    # PAGE 2 : CARTE & SIGNALEMENTS
    # =========================================================
    # =========================================================
    # PAGE 2 : CARTE & SIGNALEMENTS
    # =========================================================

    elif page == "🗺️ Carte & Signalements":

        st.header("🗺️ Carte & Signalements")

        st.info(
            "Consultez les perturbations, les sites JOJ et signalez un incident sur le réseau Dakar 2026."
        )

        st.divider()

        if "signalements" not in st.session_state:

            st.session_state.signalements = []

        if "trajet_trouve" not in st.session_state:

            st.session_state.trajet_trouve = False

        if "recommandations" not in st.session_state:

            st.session_state.recommandations = []

        if "distance" not in st.session_state:

            st.session_state.distance = 0

        if "conseil" not in st.session_state:

            st.session_state.conseil = ""

        if "depart" not in st.session_state:

            st.session_state.depart = ""

        if "arrivee" not in st.session_state:

            st.session_state.arrivee = ""

        # =====================================================
        # PLANIFICATEUR D'ITINERAIRE
        # =====================================================

        st.subheader("🧭 Planifier mon trajet")

        LIEUX = {

            "Stade Abdoulaye Wade (Diamniadio)": {
                "lat": 14.7645,
                "lon": -17.3660,
                "zone": "diamniadio"
            },

            "Dakar Arena (Diamniadio)": {
                "lat": 14.7285,
                "lon": -17.2733,
                "zone": "diamniadio"
            },

            "Complexe Iba Mar Diop (Dakar)": {
                "lat": 14.6937,
                "lon": -17.4441,
                "zone": "dakar"
            },

            "Saly Beach West (Saly)": {
                "lat": 14.3144,
                "lon": -16.9700,
                "zone": "saly"
            },

            "Gare TER Dakar (Petersen)": {
                "lat": 14.6920,
                "lon": -17.4460,
                "zone": "dakar"
            },

            "Gare TER Diamniadio": {
                "lat": 14.7305,
                "lon": -17.1987,
                "zone": "diamniadio"
            },

            "Aéroport AIBD": {
                "lat": 14.7367,
                "lon": -17.0902,
                "zone": "aibd"
            },

            "Plateau / Centre-ville Dakar": {
                "lat": 14.6937,
                "lon": -17.4441,
                "zone": "dakar"
            },

            "Guédiawaye": {
                "lat": 14.7800,
                "lon": -17.3950,
                "zone": "banlieue"
            },

            "Rufisque": {
                "lat": 14.7152,
                "lon": -17.2703,
                "zone": "rufisque"
            },
        }

        col1, col2 = st.columns(2)

        with col1:

            depart = st.selectbox(
                "📍 Point de départ",
                options=list(LIEUX.keys()),
                index=4
            )

        with col2:

            arrivee = st.selectbox(
                "🏁 Point d'arrivée",
                options=list(LIEUX.keys()),
                index=0
            )

        def haversine(lat1, lon1, lat2, lon2):

            R = 6371

            dlat = math.radians(lat2 - lat1)
            dlon = math.radians(lon2 - lon1)

            a = (
                math.sin(dlat / 2) ** 2
                + math.cos(math.radians(lat1))
                * math.cos(math.radians(lat2))
                * math.sin(dlon / 2) ** 2
            )

            return R * 2 * math.asin(math.sqrt(a))

        def recommander_transport(lieu_dep, lieu_arr, lieux):

            dep = lieux[lieu_dep]
            arr = lieux[lieu_arr]

            dist = haversine(
                dep["lat"],
                dep["lon"],
                arr["lat"],
                arr["lon"]
            )

            recommandations = []

            if lieu_dep == lieu_arr:

                return [], 0, ""

            recommandations.append({

                "moyen": "🚆 TER",
                "niveau": "Recommandé",
                "couleur": "success",
                "duree": "30 à 40 min",
                "prix": "1 500 FCFA",
                "details": (
                    "Le TER permet d'éviter les embouteillages "
                    "entre Dakar et Diamniadio."
                )
            })

            recommandations.append({

                "moyen": "🚌 BRT",
                "niveau": "Rapide",
                "couleur": "info",
                "duree": "20 à 35 min",
                "prix": "500 FCFA",
                "details": (
                    "Le BRT est conseillé pour les déplacements "
                    "dans Dakar et la banlieue."
                )
            })

            recommandations.append({

                "moyen": "🚕 Taxi / VTC",
                "niveau": "Alternatif",
                "couleur": "warning",
                "duree": "Variable",
                "prix": f"{int(dist * 300)} FCFA",
                "details": (
                    "Solution flexible mais plus lente "
                    "pendant les heures de pointe."
                )
            })

            conseil = (
                "✅ Privilégiez les transports publics "
                "pour éviter les ralentissements."
            )

            return recommandations, round(dist, 1), conseil

        if st.button(
            "🔍 Trouver le meilleur transport",
            type="primary"
        ):

            if depart == arrivee:

                st.error(
                    "⚠️ Le départ et l'arrivée sont identiques. Veuillez choisir deux lieux différents."
                )

            else:

                recommandations, distance, conseil = recommander_transport(
                    depart,
                    arrivee,
                    LIEUX
                )

                st.session_state.trajet_trouve = True

                st.session_state.recommandations = recommandations

                st.session_state.distance = distance

                st.session_state.conseil = conseil

                st.session_state.depart = depart

                st.session_state.arrivee = arrivee

        if st.session_state.trajet_trouve:

            st.success("✅ Itinéraire trouvé")

            st.markdown(
                f"**Trajet :** "
                f"{st.session_state.depart} "
                f"→ "
                f"{st.session_state.arrivee}"
                f"  |  "
                f"**Distance estimée :** "
                f"{st.session_state.distance} km"
            )

            st.info(
                st.session_state.conseil
            )

            st.markdown(
                "#### Moyens de transport disponibles"
            )

            for r in st.session_state.recommandations:

                badge = {
                    "success": "🟢",
                    "info": "🔵",
                    "warning": "🟠"
                }.get(r["couleur"], "⚪")

                niveau_couleur = {
                    "success": st.success,
                    "info": st.info,
                    "warning": st.warning
                }

                niveau_couleur[r["couleur"]](
                    f"{badge} **{r['moyen']}** — *{r['niveau']}*\n\n"
                    f"⏱ Durée : {r['duree']}  |  💰 Prix : {r['prix']}\n\n"
                    f"{r['details']}"
                )

        st.divider()

        # =====================================================
        # FILTRE CARTE
        # =====================================================

        st.subheader("🔎 Filtrer la carte")

        filtre = st.selectbox(
            "Choisir un affichage",
            [
                "Tous",
                "Sites JOJ",
                "TER",
                "BRT",
                "Navettes JOJ",
                "Perturbations"
            ]
        )

        st.divider()

        # =====================================================
        # CARTE INTERACTIVE
        # =====================================================

        st.subheader("📍 Carte interactive JOJ")

        carte = folium.Map(
            location=[14.7167, -17.4677],
            zoom_start=10
        )

        folium.Marker(
            [14.7645, -17.3660],
            popup="🏟️ Stade Abdoulaye Wade",
            tooltip="Stade Abdoulaye Wade",
            icon=folium.Icon(color="green")
        ).add_to(carte)

        folium.Marker(
            [14.7285, -17.2733],
            popup="🏟️ Dakar Arena",
            tooltip="Dakar Arena",
            icon=folium.Icon(color="blue")
        ).add_to(carte)

        folium.Marker(
            [14.6937, -17.4441],
            popup="🏟️ Complexe Iba Mar Diop",
            tooltip="Complexe Iba Mar Diop",
            icon=folium.Icon(color="red")
        ).add_to(carte)

        folium.Marker(
            [14.3144, -16.9700],
            popup="🏖️ Saly Beach West",
            tooltip="Saly Beach West",
            icon=folium.Icon(color="orange")
        ).add_to(carte)

        st_folium(
            carte,
            use_container_width=True,
            height=550
        )

        st.divider()

        # =====================================================
        # ALERTES TEMPS REEL
        # =====================================================

        st.subheader("📢 Alertes en temps réel")

        st.error(
            "🔴 Accident signalé sur la Corniche Ouest"
        )

        st.warning(
            "🟠 Trafic dense vers Dakar Arena"
        )

        st.info(
            "🔵 Navette JOJ Ligne B opérationnelle"
        )

        st.success(
            "🟢 TER Dakar ↔ Diamniadio fonctionne normalement"
        )

        st.divider()

        # =====================================================
        # NIVEAU GLOBAL DU TRAFIC
        # =====================================================

        st.subheader("📊 Niveau global du trafic")

        if 7 <= heure_actuelle <= 9:

            trafic = "Très dense"
            progression = 90

        elif 17 <= heure_actuelle <= 20:

            trafic = "Saturé"
            progression = 100

        elif 12 <= heure_actuelle <= 14:

            trafic = "Modéré"
            progression = 60

        else:

            trafic = "Fluide"
            progression = 30

        st.progress(progression)

        st.metric(
            "🚗 État du trafic",
            trafic
        )

        st.divider()

        # =====================================================
        # FORMULAIRE SIGNALEMENT
        # =====================================================

        st.subheader("⚠️ Signaler un incident")

        with st.form("signalement"):

            type_incident = st.selectbox(
                "Type d'incident",
                [
                    "Embouteillage",
                    "Accident",
                    "Retard navette",
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
                "📝 Décrire le problème"
            )

            envoyer = st.form_submit_button(
                "📤 Envoyer le signalement"
            )

            if envoyer:

                st.session_state.signalements.append({

                    "type": type_incident,
                    "gravite": gravite,
                    "description": description
                })

                st.success(
                    "Signalement envoyé avec succès ✅"
                )

        st.divider()

        # =====================================================
        # SIGNALEMENTS COMMUNAUTAIRES
        # =====================================================

        st.subheader("📡 Signalements communautaires")

        if st.session_state.signalements:

            for signalement in reversed(
                st.session_state.signalements
            ):

                if signalement["gravite"] == "Élevée":

                    st.error(
                        f"🚨 {signalement['type']} — "
                        f"{signalement['description']}"
                    )

                elif signalement["gravite"] == "Moyenne":

                    st.warning(
                        f"⚠️ {signalement['type']} — "
                        f"{signalement['description']}"
                    )

                else:

                    st.info(
                        f"ℹ️ {signalement['type']} — "
                        f"{signalement['description']}"
                    )

        else:

            st.success(
                "✅ Aucun incident signalé actuellement."
            )

        st.divider()

        # =====================================================
        # CONSEILS MOBILITE
        # =====================================================

        st.subheader("💡 Conseils mobilité")

        st.success(
            "🚆 Privilégiez le TER pendant les heures de pointe."
        )

        st.info(
            "🚌 Les navettes JOJ sont renforcées autour des sites sportifs."
        )

        st.warning(
            "⏰ Anticipez vos déplacements avant les compétitions majeures."
        )
        
    # =========================================================
    # PAGE 3 : ZONE SOS
    # =========================================================

    elif page == "🚨 Zone SOS":

        st.header("🚨 Zone SOS")
        st.error("En cas d'urgence, utilisez cette rubrique pour contacter les secours.")
        st.divider()

        if "alertes_sos" not in st.session_state:
            st.session_state.alertes_sos = []

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

        st.subheader("🚨 Déclencher une alerte SOS")

        type_urgence = st.selectbox(
            "⚠️ Type d'urgence",
            ["Accident de transport", "Malaise", "Agression", "Enfant perdu",
             "Navette en panne", "Incendie", "Embouteillage", "Route bloquée", "Voiture en panne", "Autre"]
        )

        niveau = st.select_slider(
            "🚦 Niveau de priorité",
            options=["Faible", "Moyenne", "Élevée", "Critique"]
        )

        localisation = st.selectbox(
            "📍 Localisation",
            ["Stade Abdoulaye Wade", "Dakar Arena", "Complexe Iba Mar Diop",
             "Saly", "Autoroute Dakar - Diamniadio", "Village Olympique", "Autre"]
        )

        details = st.text_area("📝 Décrivez brièvement la situation")

        if st.button("🚨 Envoyer l'alerte"):
            st.session_state.alertes_sos.append({
                "type": type_urgence, "priorite": niveau,
                "lieu": localisation, "details": details
            })
            st.success("✅ Alerte transmise avec succès.")
            st.warning(f"🚨 {type_urgence} — 📍 {localisation} — Priorité : {niveau}")

        st.divider()

        st.subheader("⏱️ Temps d'intervention estimé")
        temps_map = {"Critique": "3 min", "Élevée": "5 min", "Moyenne": "10 min", "Faible": "15 min"}
        st.metric("Temps estimé", temps_map[niveau])

        st.divider()
        st.subheader("📡 Alertes communautaires")

        if st.session_state.alertes_sos:
            for alerte in reversed(st.session_state.alertes_sos):
                if alerte["priorite"] == "Critique":
                    st.error(f"🚨 {alerte['type']} — 📍 {alerte['lieu']} — Priorité : {alerte['priorite']} — {alerte['details']}")
                elif alerte["priorite"] == "Élevée":
                    st.warning(f"⚠️ {alerte['type']} — 📍 {alerte['lieu']} — {alerte['details']}")
                else:
                    st.info(f"ℹ️ {alerte['type']} — 📍 {alerte['lieu']} — {alerte['details']}")
        else:
            st.success("✅ Aucun incident signalé actuellement.")

        st.divider()
        st.subheader("🏥 Centres d'assistance")
        st.success("🏥 Poste médical du Stade Abdoulaye Wade")
        st.success("🏥 Centre d'assistance Dakar Arena")
        st.success("🏥 Poste de secours de Saly")
        st.success("🏥 Unité mobile Teranga Mobile")

        st.divider()
        st.warning("🚑 Une équipe d'intervention est actuellement en route.")
        st.divider()

        st.subheader("🛟 Conseils pratiques")
        with st.expander("🚌 Incident de transport"):
            st.write("• Restez calme et éloignez-vous du danger\n• Prévenez immédiatement les agents Teranga Mobile\n• Attendez les secours dans une zone sécurisée")
        with st.expander("❤️ Malaise ou blessure"):
            st.write("• Mettre la personne à l'abri\n• Appeler rapidement le SAMU\n• Ne pas déplacer la victime inutilement")
        with st.expander("👶 Enfant perdu"):
            st.write("• Informer immédiatement les agents JOJ\n• Décrire précisément les vêtements\n• Rester au point de rencontre indiqué")
        with st.expander("🔥 Incendie"):
            st.write("• Quitter la zone immédiatement\n• Éviter les mouvements de foule\n• Appeler les sapeurs-pompiers")

    # =========================================================
    # PAGE 4 : RESTAURATION
    # =========================================================

    elif page == "🍽️ Restauration":

        st.header("🍽️ Food Zones JOJ Dakar 2026")
        st.write("Découvrez les restaurants et spécialités culinaires à proximité des sites des JOJ Dakar 2026.")
        st.divider()

        stade = st.selectbox(
            "🏟️ Choisir un site",
            ["Stade Abdoulaye Wade", "Dakar Arena", "Complexe Iba Mar Diop", "Saly"]
        )
        st.divider()

        st.subheader("🇸🇳 Gastronomie sénégalaise")
        plats_senegalais = [
            "🍚 Thiéboudiène", "🍗 Yassa Poulet", "🥩 Mafé",
            "🐟 Poisson braisé", "🥟 Fataya", "🥤 Jus de Bissap",
            "🌺 Jus de Bouye", "🥣 Couscous de Mil"
        ]
        for plat in plats_senegalais:
            st.write(plat)

        st.divider()
        st.subheader("🍴 Restaurants recommandés")

        restaurants = {
            "Stade Abdoulaye Wade": [
                ("🍚 Restaurant Teranga Diamniadio", "success", "⭐ 4.8/5 — 📍 À proximité du stade — ⏳ ~10 min"),
                ("🍔 Fast Food Arena", "info", "⭐ 4.2/5 — Burgers, sandwichs"),
                ("☕ Café des Supporters", "warning", "⭐ 4.0/5 — Boissons et en-cas"),
            ],
            "Dakar Arena": [
                ("🥘 Saveurs du Sénégal", "success", "⭐ 4.7/5 — Cuisine locale authentique"),
                ("🍕 Pizza Arena", "info", "⭐ 4.0/5 — Restauration rapide"),
                ("🥤 Olympic Food Corner", "warning", "⭐ 3.9/5 — Snacks et boissons"),
            ],
            "Complexe Iba Mar Diop": [
                ("🐟 La Terrasse Dakaroise", "success", "⭐ 4.6/5 — Poissons grillés, thiéboudiène"),
                ("🍗 Yassa Express", "info", "⭐ 4.1/5 — Yassa et grillades"),
                ("☕ Café Sportif", "warning", "⭐ 3.8/5 — Café et snacks"),
            ],
            "Saly": [
                ("🦐 Restaurant de la Plage", "success", "⭐ 4.9/5 — Fruits de mer frais"),
                ("🐟 Saly Seafood", "info", "⭐ 4.5/5 — Spécialités marines"),
                ("🥥 Tropical Café", "warning", "⭐ 4.2/5 — Jus tropicaux et snacks"),
            ],
        }

        for nom_resto, style, desc in restaurants[stade]:
            getattr(st, style)(f"{nom_resto} — {desc}")

        st.divider()
        st.subheader("📋 Menu JOJ")
        menu = {"Thiéboudiène": 3500, "Yassa Poulet": 3000, "Mafé": 3000, "Fataya": 500, "Jus de Bissap": 1000}
        for nom_plat, prix in menu.items():
            st.write(f"🍽️ {nom_plat} — {prix} FCFA")

        st.divider()
        st.subheader("💡 Conseil du jour")
        st.success("🍚 Ne quittez pas le Sénégal sans goûter au Thiéboudiène, plat emblématique classé au patrimoine culturel de l'UNESCO.")

        st.divider()
        st.subheader("⭐ Votre avis")
        note = st.slider("Donnez une note", 1, 5, 4)
        commentaire = st.text_area("Votre commentaire")
        if st.button("Envoyer l'avis"):
            st.success("Merci pour votre avis !")

        st.divider()
        st.subheader("🏅 Passeport Gastronomique")
        plats_testes = st.slider("Nombre de spécialités sénégalaises goûtées", 0, 5, 0)
        if plats_testes >= 3:
            st.success("🏅 Badge Découverte de la Gastronomie Sénégalaise obtenu !")

        st.divider()
        st.subheader("🤖 Assistant Food")
        question_food = st.text_input("Que souhaitez-vous manger ?")
        if question_food:
            if "poisson" in question_food.lower():
                st.info("🍚 Nous vous recommandons le Thiéboudiène.")
            elif "poulet" in question_food.lower():
                st.info("🍗 Nous vous recommandons le Yassa Poulet.")
            else:
                st.info("🇸🇳 Découvrez les spécialités culinaires sénégalaises proposées.")

    # =========================================================
    # PAGE 5 : MES BILLETS
    # =========================================================

    elif page == "🎟️ Mes Billets":

        st.header("📅 Calendrier Officiel des JOJ Dakar 2026")
        st.write("Découvrez le programme prévisionnel des compétitions des JOJ Dakar 2026.")
        st.success("📍 JOJ Dakar 2026 : du 31 octobre au 13 novembre 2026")
        st.divider()

        calendrier = {
            "31 oct - 3 nov": {"🚣 Aviron côtier": "Saly Beach West", "⚾ Baseball5": "Complexe Tour de l'Œuf"},
            "1 - 3 nov": {"🏉 Rugby à 7": "Complexe Iba Mar Diop", "🥋 Judo": "Dakar Arena", "🥋 Wushu": "Dakar Expo Center"},
            "1 - 5 nov": {"⚽ Futsal": "Iba Mar Diop / Dakar Arena", "🏸 Badminton": "Dakar Arena", "🏓 Tennis de table": "Dakar Expo Center"},
            "1 - 6 nov": {"🏊 Natation": "Complexe Tour de l'Œuf"},
            "3 - 6 nov": {"🐎 Équitation": "Complexe Équestre Diamniadio"},
            "4 - 5 nov": {"🛹 Skateboard": "Complexe Tour de l'Œuf"},
            "5 - 6 nov": {"🏊‍♂️ Triathlon": "Saly Beach West"},
            "5 - 11 nov": {"🤸 Gymnastique": "Dakar Expo Center"},
            "6 - 10 nov": {"🏹 Tir à l'arc": "Stade Abdoulaye Wade"},
            "7 - 8 nov": {"🤼 Lutte de plage": "Saly Beach West"},
            "7 - 12 nov": {"🥊 Boxe": "Dakar Expo Center"},
            "8 - 10 nov": {"🏃 Athlétisme": "Complexe Iba Mar Diop", "🚴 Cyclisme route": "Corniche Ouest"},
            "8 - 12 nov": {"🥋 Taekwondo": "Complexe Iba Mar Diop", "⛵ Voile": "Saly Beach West"},
            "8 - 13 nov": {"🤺 Escrime": "Dakar Expo Center"},
            "9 - 13 nov": {"🏐 Beach Handball": "Saly Beach West"},
            "12 - 13 nov": {"🕺 Breaking": "Complexe Tour de l'Œuf"},
        }

        st.subheader("🗓️ Programme des compétitions")
        for date_evt, sports in calendrier.items():
            with st.expander(f"📆 {date_evt}"):
                for sport, lieu_evt in sports.items():
                    st.write(f"**{sport}** — 📍 {lieu_evt}")

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
        st.info("🏅 Dakar 2026 sera la première édition des JOJ organisée en Afrique.")

        st.divider()

        # ---- BILLETTERIE ----
        st.header("🎟️ Mes Billets JOJ Dakar 2026")
        st.write("Consultez et générez vos billets sécurisés pour les compétitions.")

        st.warning("⚠️ Les tarifs officiels des billets n'ont pas encore été publiés par le comité d'organisation.")
        st.info("Les modalités de réservation et les tarifs seront communiqués prochainement.")

        st.divider()
        st.subheader("👤 Informations du spectateur")

        nom_billet = st.text_input("Nom complet", key="nom_billet")

        evenement = st.selectbox(
            "🏅 Choisir une compétition",
            ["🏉 Rugby à 7", "⚽ Futsal", "🏊 Natation", "🏃 Athlétisme",
             "🥋 Taekwondo", "🥊 Boxe", "🤸 Gymnastique", "🕺 Breaking"]
        )

        date_billet = st.selectbox(
            "📅 Date",
            ["1 Novembre 2026", "3 Novembre 2026", "5 Novembre 2026",
             "8 Novembre 2026", "10 Novembre 2026", "12 Novembre 2026"]
        )

        lieu_billet = st.selectbox(
            "📍 Site",
            ["Dakar Arena", "Complexe Iba Mar Diop", "Stade Abdoulaye Wade",
             "Saly Beach West", "Dakar Expo Center"]
        )

        st.divider()

        # --- LOGIQUE DE PAIEMENT ---
        # On initialise les états de paiement s'ils n'existent pas encore
        if "paiement_effectue" not in st.session_state:
            st.session_state["paiement_effectue"] = False

        # Si le paiement n'est pas encore fait, on affiche le module Wave / Orange Money
        if not st.session_state["paiement_effectue"]:
            st.subheader("💳 Étape obligatoire : Paiement du billet (1 000 FCFA)")
            
            mode_paiement = st.radio("Sélectionnez votre moyen de paiement :", ["Wave 🌊", "Orange Money 🍊"], horizontal=True)
            numero_tel = st.text_input("Entrez votre numéro de téléphone (9 chiffres)", key="num_pay", max_chars=9)
            
        if st.button("📱 Procéder au paiement"):
                if nom_billet == "":
                    st.error("⚠️ Veuillez d'abord remplir votre Nom complet plus haut avant de payer.")
                elif len(numero_tel) < 9 or not numero_tel.isdigit():
                    st.error("⚠️ Veuillez entrer un numéro de téléphone valide à 9 chiffres (ex: 77xxxxxxx).")
                else:
                    with st.spinner(f"Connexion avec {mode_paiement} en cours... Veuillez valider la notification sur votre téléphone."):
                        time.sleep(3) # Simule l'attente de validation USSD/Application
                    st.success(f"✅ Paiement de 1 000 FCFA réussi via {mode_paiement} ! Vous pouvez maintenant générer votre billet.")
                    st.session_state["paiement_effectue"] = True
                    st.rerun() # Rafraîchit la page pour débloquer le bouton du billet    

        if st.button("🎫 Générer mon billet"):

            if nom_billet == "":
                st.error("⚠️ Veuillez entrer votre nom complet.")
            else:
                billet_texte = f"JOJ Dakar 2026 | {nom_billet} | {evenement} | {date_billet} | {lieu_billet}"

                qr = qrcode.QRCode(version=1, box_size=10, border=5)
                qr.add_data(billet_texte)
                qr.make(fit=True)
                img_qr = qr.make_image(fill_color="black", back_color="white").convert("RGB")

                st.success("✅ Billet généré avec succès !")
                st.markdown("## 🎟️ Mon Billet JOJ Dakar 2026")

                col1, col2 = st.columns([2, 1])
                with col1:
                    st.write(f"👤 Nom : **{nom_billet}**")
                    st.write(f"🏅 Événement : **{evenement}**")
                    st.write(f"📅 Date : **{date_billet}**")
                    st.write(f"📍 Lieu : **{lieu_billet}**")
                with col2:
                    st.image(img_qr, caption="QR Code du billet", width=220)

                st.markdown("""
                <div style="background-color:#d1ecf1; padding:18px; border-radius:12px; font-size:20px; font-weight:bold; text-align:center; color:#0c5460; margin-top:15px;">
                    📱 Présentez ce QR code à l'entrée.
                </div>
                """, unsafe_allow_html=True)
                
                # --- REMPLACE LE BOUTON "ACHETER UN AUTRE BILLET" PAR CELUI-CI : ---
            if st.button("🔄 Acheter un autre billet"):
                st.session_state["paiement_effectue"] = False
        
        st.divider()
        st.markdown("""
        <div style="background: linear-gradient(135deg, #0c5460, #117a8b); padding:25px; border-radius:15px; color:white; box-shadow:0px 4px 12px rgba(0,0,0,0.2); margin-top:10px; text-align:center;">
            <h3>🎟️ Billetterie JOJ Dakar 2026</h3>
            <p style="font-size:16px; line-height:1.8;">
                Les données présentées sont à titre de démonstration.<br>
                Les tarifs officiels seront publiés prochainement par le comité d'organisation.
            </p>
            <p style="font-size:18px; font-weight:bold;">🇸🇳 Merci de votre confiance</p>
        </div>
        """, unsafe_allow_html=True)

    # =========================================================
    # PAGE 6 : GUIDE TERANGA
    # =========================================================

    elif page == "🦁 Guide Teranga":

        st.header("🦁 Guide Teranga")
        st.write("Bienvenue au pays de la Teranga ! Découvrez la culture, les traditions et les lieux incontournables du Sénégal.")
        st.divider()

        destination_guide = st.selectbox(
            "📍 Choisissez un site touristique",
            ["Île de Gorée", "Monument de la Renaissance Africaine", "Lac Rose",
             "Réserve de Bandia", "Mosquée de Touba", "Parc National du Niokolo-Koba"]
        )

        st.divider()

        sites_info = {
            "Île de Gorée": {
                "emoji": "⛴️",
                "img": "https://upload.wikimedia.org/wikipedia/commons/6/65/Goree_Island.jpg",
                "itineraire": "Taxi ou Bus → Port Autonome de Dakar → Ferry 20 min",
                "temps": "45 min à 1h",
                "decouvertes": ["Maison des Esclaves", "Plages historiques", "Rues coloniales", "Musées et galeries"],
                "conseil": "Privilégiez une visite le matin pour éviter la chaleur."
            },
            "Monument de la Renaissance Africaine": {
                "emoji": "🗿",
                "img": "https://upload.wikimedia.org/wikipedia/commons/0/0e/Monument_Renaissance_Africaine.jpg",
                "itineraire": "Taxi, Bus Dakar Dem Dikk ou VTC depuis Plateau / Almadies",
                "temps": "20 à 35 min",
                "decouvertes": ["Vue panoramique sur Dakar", "Musée intérieur", "Escaliers monumentaux"],
                "conseil": "Visitez en fin d'après-midi pour admirer le coucher du soleil."
            },
            "Lac Rose": {
                "emoji": "🌸",
                "img": "https://upload.wikimedia.org/wikipedia/commons/a/a3/Lac_Rose_Senegal.jpg",
                "itineraire": "Autoroute depuis Dakar → Rufisque → Kayar",
                "temps": "1h30",
                "decouvertes": ["Couleur rose du lac", "Extraction traditionnelle du sel", "Balades en quad", "Dunes et plage"],
                "conseil": "La couleur du lac est plus visible en saison sèche."
            },
            "Réserve de Bandia": {
                "emoji": "🦒",
                "img": "https://upload.wikimedia.org/wikipedia/commons/5/5d/Giraffes_Bandia.jpg",
                "itineraire": "Autoroute A1 depuis Dakar → direction Mbour",
                "temps": "1h15",
                "decouvertes": ["Girafes", "Rhinocéros", "Zèbres", "Safari en 4x4"],
                "conseil": "Réservez une visite guidée pour profiter pleinement du safari."
            },
            "Mosquée de Touba": {
                "emoji": "🕌",
                "img": "https://upload.wikimedia.org/wikipedia/commons/f/f7/Touba_Mosque.jpg",
                "itineraire": "Autoroute Ila Touba depuis Dakar",
                "temps": "3 heures",
                "decouvertes": ["Grande Mosquée", "Bibliothèque islamique", "Architecture religieuse"],
                "conseil": "Portez une tenue respectueuse pour visiter les lieux religieux."
            },
            "Parc National du Niokolo-Koba": {
                "emoji": "🌿",
                "img": "https://upload.wikimedia.org/wikipedia/commons/e/e3/Niokolo_Koba.jpg",
                "itineraire": "Avion ou voiture vers Tambacounda depuis Dakar",
                "temps": "8 à 10h par route",
                "decouvertes": ["Lions", "Antilopes", "Oiseaux rares", "Nature sauvage"],
                "conseil": "Prévoir plusieurs jours pour profiter pleinement du parc."
            },
        }

        site = sites_info[destination_guide]

        st.subheader(f"{site['emoji']} {destination_guide}")

        try:
            st.image(site["img"], use_container_width=True)
        except Exception:
            pass

        st.markdown(f"**🚍 Itinéraire :** {site['itineraire']}")
        st.markdown(f"**⏱ Temps estimé :** {site['temps']}")
        st.markdown("**⭐ À découvrir :**")
        for decouverte in site["decouvertes"]:
            st.write(f"  • {decouverte}")
        st.info(f"💡 **Conseil :** {site['conseil']}")

        st.divider()
        st.success("✅ Itinéraire généré avec succès.")
        st.divider()
        st.subheader("✅ Conseils visiteurs")
        conseils = [
            "Utiliser le TER pour rejoindre rapidement Diamniadio.",
            "Arriver au moins 1 heure avant le début des compétitions.",
            "Prévoir une bouteille d'eau réutilisable.",
            "Scanner les QR codes des navettes officielles JOJ.",
            "Respecter les consignes de sécurité sur les sites.",
            "Garder une pièce d'identité sur soi.",
        ]
        for conseil in conseils:
            st.write(f"• {conseil}")

        st.divider()
        st.subheader("🌍 Langues utiles")
        st.write("🇸🇳 Wolof : Bienvenue → 'Dalal ak jamm'")
        st.write("🇫🇷 Français : langue officielle")
        st.write("🇬🇧 English : Welcome")
        st.write("🇪🇸 Español : Bienvenido")

        st.divider()
        st.subheader("🎭 Culture sénégalaise")
        st.info("La Teranga est une valeur essentielle du Sénégal : hospitalité, respect et partage envers les visiteurs.")

        st.subheader("🍽️ Cuisine Sénégalaise")
        for plat in ["🍚 Thiéboudiène", "🍗 Yassa Poulet", "🥩 Mafé", "🥟 Fataya", "🥤 Jus de Bissap"]:
            st.write(plat)

        st.divider()
        st.subheader("🗣️ Quelques mots en Wolof")
        expressions = {
            "Bonjour": "Salaam Aleekum",
            "Merci": "Jërëjëf",
            "Comment ça va ?": "Nanga def ?",
            "Bienvenue": "Dalal ak jamm"
        }
        for fr, wo in expressions.items():
            st.write(f"🇫🇷 {fr} → 🇸🇳 {wo}")

        st.divider()
        st.subheader("🎯 Quiz Sénégal")
        reponse_quiz = st.radio(
            "Quel est le plat national du Sénégal ?",
            ["Pizza", "Thiéboudiène", "Hamburger"]
        )
        if st.button("Valider"):
            if reponse_quiz == "Thiéboudiène":
                st.success("Bonne réponse ! 🎉")
            else:
                st.error("Mauvaise réponse. C'est le Thiéboudiène !")

        st.divider()
        st.success("Merci de découvrir le Sénégal à travers ce guide Teranga ! Profitez pleinement des JOJ Dakar 2026.")

    # =========================================================
    # FOOTER
    # =========================================================

    st.divider()
    st.markdown("""
    <div style='text-align:center; color:gray;'>
        🇸🇳 Dakar JOJ 2026 — Teranga Mobile<br>
        Développé pour améliorer la mobilité, la sécurité et l'expérience des visiteurs.<br>
        Version 1.0
    </div>
    """, unsafe_allow_html=True)
