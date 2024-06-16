import streamlit as st # type: ignore

# Initialiser les états de session si ce n'est pas déjà fait
if 'Accueil' not in st.session_state:
    st.session_state.Accueil = True
if 'modifiable' not in st.session_state:
    st.session_state.modifiable = False
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'Accueil'
if 'emplacement_geo' not in st.session_state:
    st.session_state.emplacement_geo = "Amiens"
if 'foyer' not in st.session_state:
    st.session_state.foyer ="4"
if 'adulte' not in st.session_state:
    st.session_state.adulte ="2"
if 'enfant' not in st.session_state:
    st.session_state.enfant ="2"

# Sidebar pour la navigation
with st.sidebar:
    gauche, droite = st.columns(2)

    with gauche:
        image = st.image("Assets/download.png", width=75)
        voir_plus = st.button('Voir plus', key='voir_plus')

    with droite:
        retour = st.button('RobinAI', key='retour')

    st.header('Consommation par zone', divider=True)
    sdb = st.button('Salle de Bain', key='sdb')
    cuisine = st.button('Cuisine', key='cuisine')
    autres = st.button('Autres', key='autres')
    st.header("Idée pour réduire la consommation", divider=True)
    catalogue = st.button('Catalogue', key='catalogue')

# Gérer la navigation entre les pages
if retour:
    st.session_state.current_page = 'Accueil'

if voir_plus:
    st.session_state.current_page = 'Modifier'

if sdb:
    st.session_state.current_page = 'Salle de Bain'

if cuisine:
    st.session_state.current_page = 'Cuisine'

if autres:
    st.session_state.current_page = 'Autres'

if catalogue:
    st.session_state.current_page = 'Catalogue'

# Afficher le contenu de la page en fonction de la page courante
if st.session_state.current_page == 'Accueil':
    _, milieu, _ = st.columns(3)
    with milieu:
        st.image('Assets/LOGO_RobinAI.png', width=225)
    st.header("RobinAI : votre assistant consommation", divider=True)
    st.subheader("Prévision de la consommation ")

    st.image('Assets/prevision.png')
    st.subheader("Consommation mensuelle d'eau ")

    st.image("Assets/graph_variation.png")
    st.image("Assets/camembert_simple.png")


elif st.session_state.current_page == 'Modifier':
    # La case à cocher contrôle directement l'état `modifiable`
    check = st.checkbox('Modifier', value=st.session_state.modifiable)

    # Mettre à jour l'état modifiable en fonction de la case à cocher
    if check != st.session_state.modifiable:
        st.session_state.modifiable = check

    # Afficher le champ de texte avec l'état d'activation basé sur l'état de modification
    st.session_state.emplacement_geo = st.text_area('Emplacement Géographique (Ville)', value=st.session_state.emplacement_geo, disabled=not st.session_state.modifiable)
    st.session_state.foyer = st.text_area('Nombre dans le foyer', value=st.session_state.foyer, disabled=not st.session_state.modifiable)
    st.session_state.adulte = st.text_area('Adulte(s)', value=st.session_state.adulte, disabled=not st.session_state.modifiable)
    st.session_state.enfant = st.text_area('Enfant(s)', value=st.session_state.enfant, disabled=not st.session_state.modifiable)


elif st.session_state.current_page == 'Salle de Bain':
    st.header("Consommation d'eau dans la salle de bain", divider=True)
    st.image("Assets/coso_mensuelle_douche.png")

elif st.session_state.current_page == 'Cuisine':
    st.header("Consommation d'eau dans la cuisine", divider=True)
    st.image("Assets/conso_mensuelle_cuisine.png")

elif st.session_state.current_page == 'Autres':
    st.header("Autres consommation d'eau", divider=True)
    st.image("Assets/conso_autre_mensuelle.png")
    st.write("- Besoin vitaux (hydratation)\n - Faire la cuisine (laver les aliments, bouillir des pâtes...)")

elif st.session_state.current_page == 'Catalogue':
    gauche, droite = st.columns(2, gap='large')

    with gauche:
        st.write('Pommeau de douche')
        st.video("Assets/Pommeau.mp4", format="video/mp4", start_time=0, loop=True, autoplay=True, muted=True)
        st.write("Le pommeau de douche HYDRAO Aloe est un dispositif éco-responsable qui aide à réduire la consommation d'eau.\
                  Il utilise des LED colorées pour indiquer en temps réel la quantité d'eau utilisée,\
                  favorisant ainsi une gestion économe. Facile à installer, il s'adapte à la plupart des douches standard\
                  et ne nécessite pas de piles, l'énergie étant générée par le flux de l'eau.")

        st.link_button(label='Cliquer pour en savoir plus', url='https://www.hydrao.com/fr/store/pommeau-aloe')

    with droite:
        st.write('Tête thermostatique')
        st.video("Assets/tete_thermos.mp4", format="video/mp4", start_time=0, loop=True, autoplay=True, muted=True)
        st.write("Description:\n\n La tête thermostatique Zigbee/WiFi ETH600 de SEDEA\
                 permet de contrôler à distance la température de vos radiateurs via l'application SEDEA Home ou Tuya.\
                 Elle offre des fonctionnalités avancées telles que la programmation horaire.\
                 Elle s'adapte à différentes vannes grâce aux adaptateurs inclus. Idéale pour automatiser et économiser l'énergie dans votre maison. ")

        st.link_button(label='Cliquer pour en savoir plus', url='https://www.leroymerlin.fr/produits/chauffage-et-ventilation/radiateur/radiateur-a-eau-chaude/accessoires-de-radiateur-eau-chaude/thermostat-et-tete-thermostatique-connecte/tete-thermostatique-zigbee-wifi-eth600-sedea-89969432.html')
