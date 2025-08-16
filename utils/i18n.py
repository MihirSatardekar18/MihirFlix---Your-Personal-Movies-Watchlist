# utils/i18n.py

_current_lang = "en"
_listeners = []

_translations = {
    "en": {
        "home": "Home", "watchlist": "Watchlist", "add_movie": "Add Movie", "profile": "Profile",
        "about": "About", "contact": "Contact", "stats": "Stats", "welcome": "Welcome",
        "tagline": "MihirFlix — Premium, colorful, and smooth.",
        "filter_by_genre": "Filter by Genre", "select_genre": "Select Genre", "clear": "Clear",
        "no_movies_genre": "No movies found in this genre.", "watchlist_title": "Watchlist",
        "empty_watchlist": "Your watchlist is empty.", "profile_settings": "Profile Settings",
        "upload_change_picture": "Upload / Change Picture", "full_name": "Full Name",
        "username": "Username", "email": "Email", "phone": "Phone Number", "dob": "Date of Birth",
        "gender": "Gender", "language_preference": "Language Preference", "theme": "Theme",
        "privacy": "Privacy", "notifications": "Notifications", "public": "Public", "private": "Private",
        "save_update_profile": "Save / Update Profile", "change_password": "Change Password",
        "linked_accounts": "Linked Accounts", "recently_watched": "Recently Watched",
        "view_my_stats": "View My Stats", "delete_account": "Delete Account", "logout": "Log Out",
        "profile_saved": "Your profile has been updated successfully.", "choose_genre": "Choose Genre",
        "apply": "Apply", "cancel": "Cancel", "all": "All",
    },
    "hi": {
        "home": "होम","watchlist":"वॉचलिस्ट","add_movie":"मूवी जोड़ें","profile":"प्रोफ़ाइल","about":"अबाउट",
        "contact":"संपर्क","stats":"स्टैट्स","welcome":"स्वागत है",
        "tagline":"MihirFlix — प्रीमियम, रंगीन और स्मूद।","filter_by_genre":"श्रेणी से फ़िल्टर करें",
        "select_genre":"श्रेणी चुनें","clear":"हटाएं","no_movies_genre":"इस श्रेणी में कोई फ़िल्म नहीं मिली।",
        "watchlist_title":"वॉचलिस्ट","empty_watchlist":"आपकी वॉचलिस्ट खाली है।","profile_settings":"प्रोफ़ाइल सेटिंग्स",
        "upload_change_picture":"तस्वीर अपलोड / बदलें","full_name":"पूरा नाम","username":"यूज़रनेम","email":"ईमेल",
        "phone":"फ़ोन नंबर","dob":"जन्म तिथि","gender":"लिंग","language_preference":"भाषा चयन","theme":"थीम",
        "privacy":"गोपनीयता","notifications":"सूचनाएँ","public":"सार्वजनिक","private":"निजी",
        "save_update_profile":"प्रोफ़ाइल सेव / अपडेट करें","change_password":"पासवर्ड बदलें",
        "linked_accounts":"लिंक्ड अकाउंट्स","recently_watched":"हाल ही में देखी गई",
        "view_my_stats":"मेरे स्टैट्स देखें","delete_account":"अकाउंट हटाएँ","logout":"लॉग आउट",
        "profile_saved":"आपकी प्रोफ़ाइल अपडेट हो गई है।","choose_genre":"श्रेणी चुनें","apply":"लागू करें",
        "cancel":"रद्द करें","all":"सभी",
    },
    "mr": {
        "home":"मुख्यपृष्ठ","watchlist":"वॉचलिस्ट","add_movie":"चित्रपट जोडा","profile":"प्रोफाइल","about":"माहिती",
        "contact":"संपर्क","stats":"आकडेवारी","welcome":"स्वागत",
        "tagline":"MihirFlix — प्रीमियम, रंगीत आणि स्मूद.","filter_by_genre":"प्रकारानुसार फिल्टर",
        "select_genre":"प्रकार निवडा","clear":"काढा","no_movies_genre":"या प्रकारात कोणतेही चित्रपट आढळले नाहीत.",
        "watchlist_title":"वॉचलिस्ट","empty_watchlist":"तुमची वॉचलिस्ट रिकामी आहे.",
        "profile_settings":"प्रोफाइल सेटिंग्स","upload_change_picture":"चित्र अपलोड / बदला","full_name":"पूर्ण नाव",
        "username":"वापरकर्ता नाव","email":"ईमेल","phone":"फोन नंबर","dob":"जन्मतारीख","gender":"लिंग",
        "language_preference":"भाषा निवडा","theme":"थीम","privacy":"गोपनीयता","notifications":"सूचना",
        "public":"सार्वजनिक","private":"खाजगी","save_update_profile":"प्रोफाइल सेव / अद्यतनित करा",
        "change_password":"पासवर्ड बदला","linked_accounts":"लिंक्ड अकाउंट्स","recently_watched":"अलीकडे पाहिलेले",
        "view_my_stats":"माझे आकडे पाहा","delete_account":"खाते हटवा","logout":"लॉग आऊट",
        "profile_saved":"तुमची प्रोफाइल अद्यतनित झाली आहे.","choose_genre":"प्रकार निवडा","apply":"लागू करा",
        "cancel":"रद्द करा","all":"सर्व",
    },
    "fr": {
        "home":"Accueil","watchlist":"Liste de lecture","add_movie":"Ajouter un film","profile":"Profil","about":"À propos",
        "contact":"Contact","stats":"Statistiques","welcome":"Bienvenue",
        "tagline":"MihirFlix — Premium, coloré et fluide.","filter_by_genre":"Filtrer par genre",
        "select_genre":"Sélectionner un genre","clear":"Effacer","no_movies_genre":"Aucun film trouvé dans ce genre.",
        "watchlist_title":"Liste de lecture","empty_watchlist":"Votre liste de lecture est vide.",
        "profile_settings":"Paramètres du profil","upload_change_picture":"Télécharger / Changer l'image",
        "full_name":"Nom complet","username":"Nom d'utilisateur","email":"Email","phone":"Numéro de téléphone",
        "dob":"Date de naissance","gender":"Genre","language_preference":"Préférence de langue","theme":"Thème",
        "privacy":"Confidentialité","notifications":"Notifications","public":"Public","private":"Privé",
        "save_update_profile":"Enregistrer / Mettre à jour","change_password":"Changer le mot de passe",
        "linked_accounts":"Comptes liés","recently_watched":"Récemment regardé","view_my_stats":"Voir mes stats",
        "delete_account":"Supprimer le compte","logout":"Déconnexion","profile_saved":"Votre profil a été mis à jour.",
        "choose_genre":"Choisir un genre","apply":"Appliquer","cancel":"Annuler","all":"Tout",
    },
    "es": {
        "home":"Inicio","watchlist":"Lista de seguimiento","add_movie":"Agregar película","profile":"Perfil","about":"Acerca de",
        "contact":"Contacto","stats":"Estadísticas","welcome":"Bienvenido",
        "tagline":"MihirFlix — Premium, colorido y fluido.","filter_by_genre":"Filtrar por género",
        "select_genre":"Seleccionar género","clear":"Limpiar","no_movies_genre":"No se encontraron películas en este género.",
        "watchlist_title":"Lista de seguimiento","empty_watchlist":"Tu lista está vacía.",
        "profile_settings":"Configuración de perfil","upload_change_picture":"Subir / Cambiar imagen",
        "full_name":"Nombre completo","username":"Nombre de usuario","email":"Correo electrónico",
        "phone":"Número de teléfono","dob":"Fecha de nacimiento","gender":"Género",
        "language_preference":"Preferencia de idioma","theme":"Tema","privacy":"Privacidad",
        "notifications":"Notificaciones","public":"Público","private":"Privado",
        "save_update_profile":"Guardar / Actualizar perfil","change_password":"Cambiar contraseña",
        "linked_accounts":"Cuentas vinculadas","recently_watched":"Visto recientemente",
        "view_my_stats":"Ver mis estadísticas","delete_account":"Eliminar cuenta","logout":"Cerrar sesión",
        "profile_saved":"Tu perfil se ha actualizado correctamente.","choose_genre":"Elegir género",
        "apply":"Aplicar","cancel":"Cancelar","all":"Todos",
    },
    "de": {
        "home":"Startseite","watchlist":"Beobachtungsliste","add_movie":"Film hinzufügen","profile":"Profil","about":"Über uns",
        "contact":"Kontakt","stats":"Statistiken","welcome":"Willkommen",
        "tagline":"MihirFlix — Premium, farbenfroh und flüssig.","filter_by_genre":"Nach Genre filtern",
        "select_genre":"Genre auswählen","clear":"Löschen","no_movies_genre":"Keine Filme in diesem Genre gefunden.",
        "watchlist_title":"Beobachtungsliste","empty_watchlist":"Deine Beobachtungsliste ist leer.",
        "profile_settings":"Profileinstellungen","upload_change_picture":"Bild hochladen / ändern",
        "full_name":"Vollständiger Name","username":"Benutzername","email":"E-Mail","phone":"Telefonnummer",
        "dob":"Geburtsdatum","gender":"Geschlecht","language_preference":"Sprachpräferenz","theme":"Theme",
        "privacy":"Datenschutz","notifications":"Benachrichtigungen","public":"Öffentlich","private":"Privat",
        "save_update_profile":"Profil speichern / aktualisieren","change_password":"Passwort ändern",
        "linked_accounts":"Verknüpfte Konten","recently_watched":"Kürzlich angesehen",
        "view_my_stats":"Meine Statistiken anzeigen","delete_account":"Konto löschen","logout":"Abmelden",
        "profile_saved":"Dein Profil wurde aktualisiert.","choose_genre":"Genre wählen",
        "apply":"Anwenden","cancel":"Abbrechen","all":"Alle",
    },
    "it": {
        "home":"Home","watchlist":"Lista dei preferiti","add_movie":"Aggiungi film","profile":"Profilo","about":"Informazioni",
        "contact":"Contatti","stats":"Statistiche","welcome":"Benvenuto",
        "tagline":"MihirFlix — Premium, colorato e fluido.","filter_by_genre":"Filtra per genere",
        "select_genre":"Seleziona genere","clear":"Pulisci","no_movies_genre":"Nessun film trovato in questo genere.",
        "watchlist_title":"Lista dei preferiti","empty_watchlist":"La tua lista è vuota.",
        "profile_settings":"Impostazioni profilo","upload_change_picture":"Carica / Cambia immagine",
        "full_name":"Nome completo","username":"Nome utente","email":"Email","phone":"Numero di telefono",
        "dob":"Data di nascita","gender":"Genere","language_preference":"Preferenza lingua","theme":"Tema",
        "privacy":"Privacy","notifications":"Notifiche","public":"Pubblico","private":"Privato",
        "save_update_profile":"Salva / Aggiorna profilo","change_password":"Cambia password",
        "linked_accounts":"Account collegati","recently_watched":"Visti di recente",
        "view_my_stats":"Vedi le mie statistiche","delete_account":"Elimina account","logout":"Esci",
        "profile_saved":"Profilo aggiornato correttamente.","choose_genre":"Scegli genere",
        "apply":"Applica","cancel":"Annulla","all":"Tutti",
    },
    "bn": {
        "home":"হোম","watchlist":"ওয়াচলিস্ট","add_movie":"মুভি যোগ করুন","profile":"প্রোফাইল","about":"সম্পর্কে",
        "contact":"যোগাযোগ","stats":"পরিসংখ্যান","welcome":"স্বাগতম",
        "tagline":"MihirFlix — প্রিমিয়াম, বর্ণিল এবং স্মুথ।","filter_by_genre":"ধরন অনুযায়ী ফিল্টার",
        "select_genre":"ধরন নির্বাচন করুন","clear":"মুছুন","no_movies_genre":"এই ধরনে কোনো মুভি পাওয়া যায়নি।",
        "watchlist_title":"ওয়াচলিস্ট","empty_watchlist":"আপনার ওয়াচলিস্ট খালি।",
        "profile_settings":"প্রোফাইল সেটিংস","upload_change_picture":"ছবি আপলোড / পরিবর্তন",
        "full_name":"পূর্ণ নাম","username":"ইউজারনেম","email":"ইমেল","phone":"ফোন নম্বর",
        "dob":"জন্মতারিখ","gender":"লিঙ্গ","language_preference":"ভাষার পছন্দ","theme":"থিম",
        "privacy":"গোপনীয়তা","notifications":"নোটিফিকেশন","public":"পাবলিক","private":"প্রাইভেট",
        "save_update_profile":"সেভ / প্রোফাইল আপডেট","change_password":"পাসওয়ার্ড পরিবর্তন",
        "linked_accounts":"লিঙ্কড অ্যাকাউন্ট","recently_watched":"সাম্প্রতিক দেখা",
        "view_my_stats":"আমার পরিসংখ্যান দেখুন","delete_account":"অ্যাকাউন্ট মুছে ফেলুন","logout":"লগ আউট",
        "profile_saved":"আপনার প্রোফাইল আপডেট হয়েছে।","choose_genre":"ধরন নির্বাচন করুন",
        "apply":"প্রয়োগ","cancel":"বাতিল","all":"সব",
    },
    "ta": {
        "home":"முகப்பு","watchlist":"வாட்ச் பட்டியல்","add_movie":"படத்தை சேர்க்க","profile":"சுயவிபரம்","about":"எங்களை பற்றி",
        "contact":"தொடர்பு","stats":"புள்ளிவிவரம்","welcome":"வரவேற்கிறோம்",
        "tagline":"MihirFlix — உயர்தரம், வண்ணமயம், மென்மையானது.","filter_by_genre":"வகையால் வடிகட்டவும்",
        "select_genre":"வகையைத் தேர்ந்தெடு","clear":"அழி","no_movies_genre":"இந்த வகையில் படங்கள் இல்லை.",
        "watchlist_title":"வாட்ச் பட்டியல்","empty_watchlist":"உங்கள் வாட்ச் பட்டியல் காலியாக உள்ளது.",
        "profile_settings":"சுயவிபர அமைப்புகள்","upload_change_picture":"படத்தை பதிவேற்று / மாற்று",
        "full_name":"முழுப் பெயர்","username":"பயனர்பெயர்","email":"மின்னஞ்சல்","phone":"தொலைபேசி எண்",
        "dob":"பிறந்த தேதி","gender":"பாலினம்","language_preference":"மொழி விருப்பம்","theme":"தீம்",
        "privacy":"தனியுரிமை","notifications":"அறிவிப்புகள்","public":"பொது","private":"தனியார்",
        "save_update_profile":"சேமி / சுயவிபரத்தை புதுப்பி","change_password":"கடவுச்சொல்லை மாற்று",
        "linked_accounts":"இணைக்கப்பட்ட கணக்குகள்","recently_watched":"சமீபத்தில் பார்த்தவை",
        "view_my_stats":"என் புள்ளிவிவரங்கள்","delete_account":"கணக்கை நீக்கு","logout":"லாக்அவுட்",
        "profile_saved":"உங்கள் சுயவிபரம் புதுப்பிக்கப்பட்டது.","choose_genre":"வகையைத் தேர்ந்தெடு",
        "apply":"விண்ணப்பி","cancel":"ரத்து செய்","all":"அனைத்தும்",
    },
    "te": {
        "home":"హోమ్","watchlist":"వాచ్‌లిస్ట్","add_movie":"సినిమా జోడించు","profile":"ప్రొఫైల్","about":"గురించి",
        "contact":"సంప్రదించండి","stats":"గణాంకాలు","welcome":"స్వాగతం",
        "tagline":"MihirFlix — ప్రీమియం, రంగులమయం, సాఫ్ట్.","filter_by_genre":"జానర్ ద్వారా ఫిల్టర్ చేయండి",
        "select_genre":"జానర్ ఎంచుకోండి","clear":"క్లియర్","no_movies_genre":"ఈ జానర్‌లో సినిమాలు లేవు.",
        "watchlist_title":"వాచ్‌లిస్ట్","empty_watchlist":"మీ వాచ్‌లిస్ట్ ఖాళీగా ఉంది.",
        "profile_settings":"ప్రొఫైల్ సెట్టింగులు","upload_change_picture":"చిత్రం అప్‌లోడ్ / మార్చు",
        "full_name":"పూర్తి పేరు","username":"వాడుకరిపేరు","email":"ఇమెయిల్","phone":"ఫోన్ నంబర్",
        "dob":"పుట్టిన తేది","gender":"లింగం","language_preference":"భాష ప్రాధాన్యం","theme":"థీమ్",
        "privacy":"గోప్యత","notifications":"నోటిఫికేషన్లు","public":"పబ్లిక్","private":"ప్రైవేట్",
        "save_update_profile":"సేవ్ / ప్రొఫైల్ అప్‌డేట్","change_password":"పాస్‌వర్డ్ మార్చు",
        "linked_accounts":"లింక్ చేసిన ఖాతాలు","recently_watched":"ఇటీవల చూసినవి",
        "view_my_stats":"నా గణాంకాలు","delete_account":"ఖాతాను తొలగించు","logout":"లాగ్ అవుట్",
        "profile_saved":"మీ ప్రొఫైల్ అప్‌డేట్ అయింది.","choose_genre":"జానర్ ఎంచుకోండి",
        "apply":"వర్తించు","cancel":"రద్దు","all":"అన్నీ",
    },
}

def t(key: str, default=None) -> str:
    return (
        _translations.get(_current_lang, {}).get(key)
        or _translations["en"].get(key)
        or (default if default is not None else key)
    )

def set_language(code: str):
    global _current_lang
    if code in _translations and code != _current_lang:
        _current_lang = code
        for cb in list(_listeners):
            try:
                cb(_current_lang)
            except Exception:
                pass

def get_language() -> str:
    return _current_lang

def on_language_change(callback):
    if callback not in _listeners:
        _listeners.append(callback)

def remove_language_listener(callback):
    if callback in _listeners:
        _listeners.remove(callback)
