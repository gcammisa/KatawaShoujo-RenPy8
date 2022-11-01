init -2 python:

    init_language("fr")

    displayDict["fr"].styleoverrides = {"font": mainfont,
                                        "language": "western",
                                        "line_spacing": 0}

    displayDict["fr"].timeformat = "%d/%m/%y %H:%M"

    displayDict["fr"].sayfont = mainfont

    displayDict["fr"].quote_outer_open = u"“"
    displayDict["fr"].quote_outer_close = u"”"
    displayDict["fr"].quote_inner_open = u"‘"
    displayDict["fr"].quote_inner_close = u"’"

    displayDict["fr"].activeLanguage = u"Français"
    displayDict["fr"].allLanguages = {}
    displayDict["fr"].allLanguages["fr"] = displayDict["fr"].activeLanguage
    displayDict["fr"].allLanguages["en"] = "Anglais"
    displayDict["fr"].allLanguages["de"] = "Allemand"
    displayDict["fr"].allLanguages["es"] = "Espagnol"
    displayDict["fr"].allLanguages["it"] = "Italien"
    displayDict["fr"].allLanguages["jp"] = "Japonais"

    displayDict["fr"].act_term = u"Acte"
    displayDict["fr"].window_name = u"Katawa Shoujo"

    displayDict["fr"].main_menu_start = u"Démarrer"
    displayDict["fr"].main_menu_load = u"Charger"
    displayDict["fr"].main_menu_extra = u"Extras"
    displayDict["fr"].main_menu_config = u"Options"
    displayDict["fr"].main_menu_quit = u"Quitter"

    displayDict["fr"].game_menu_return = u"Retour"
    displayDict["fr"].game_menu_show = u"Cacher le texte"
    displayDict["fr"].game_menu_history = u"Historique"
    displayDict["fr"].game_menu_skip = u"Avance rapide"
    displayDict["fr"].game_menu_auto = u"Mode auto"
    displayDict["fr"].game_menu_config = u"Options"
    displayDict["fr"].game_menu_save = u"Sauvegarder"
    displayDict["fr"].game_menu_load = u"Charger"
    displayDict["fr"].game_menu_main = u"Menu principal"
    displayDict["fr"].game_menu_quit = u"Quitter"
    displayDict["fr"].game_menu_current_scene = u"Scène actuelle"
    displayDict["fr"].game_menu_current_music = u"Musique actuelle"
    displayDict["fr"].game_menu_replay_indicator = u"Relecture"

    displayDict["fr"].return_button_text = u"Retour"

    displayDict["fr"].hdisabled_label = u"Désactiver contenu pour adultes"
    displayDict["fr"].config_page_caption = u"Options"
    displayDict["fr"].config_fullscreen_label = u'Mode plein écran'
    displayDict["fr"].config_transitions_label = u'Désactiver les transitions'
    displayDict["fr"].config_skip_unseen_label = u'Sauter les textes non lus'
    displayDict["fr"].config_skip_after_choice_label = u"Garder avance rapide après les choix"
    displayDict["fr"].config_textspeed_label = u'Vitesse de lecture'
    displayDict["fr"].config_afmspeed_label = u'Délai mode automatique'
    displayDict["fr"].config_musicvol_label = u"Volume de la musique"
    displayDict["fr"].config_musicvol_jukebox_label = u"Vol."
    displayDict["fr"].config_sfxvol_label = u"Volume effets"
    displayDict["fr"].config_sfxtest_label = u"Test"
    displayDict["fr"].config_gamepad_label = u"Configuration de la manette…"

    displayDict["fr"].config_language_sel = u"Choix de la langue…"
    displayDict["fr"].config_language_caption = u"Options > Choix de la langue"
    displayDict["fr"].config_language_restart_note = u"Note : Changer de langue pendant la partie fera retourner le jeu en début de la dernière scène."

    displayDict["fr"].gamepad_caption = u"Options > Configuration de la manette"
    displayDict["fr"].gamepad_key_na = u"Non assigné"
    displayDict["fr"].gamepad_request_key = u"Pressez la touche que vous voulez assigner “%s” to.\nCliquez sur la souris ou pressez une touche pour effacer l'attribution actuelle."

    displayDict["fr"].yesno_yes = u"Oui"
    displayDict["fr"].yesno_no = u"Non"
    displayDict["fr"].yesno_okay = u"Continuer"
    displayDict["fr"].yesno_savesuccess = u"Progression sauvegardée avec succès."
    displayDict["fr"].yesno_quit = u"Êtes-vous sûr de vouloir quitter Katawa Shoujo ?"
    displayDict["fr"].yesno_return_to_main = u"Êtes-vous sûr de vouloir retourner au menu principal ?"
    displayDict["fr"].save_page_caption = u"Sauvegarder"
    displayDict["fr"].new_save_button = u"Créer une nouvelle sauvegarde"
    displayDict["fr"].load_page_caption = u"Charger"
    displayDict["fr"].yesno_load_in_game = u"Êtes-vous sûr de vouloir effacer votre progression ?"
    displayDict["fr"].yesno_save_overwrite = u"Voulez-vous vraiment écraser cette sauvegarde ?"
    displayDict["fr"].yesno_delete_savegame = u"Voulez-vous vraiment supprimer cette sauvegarde ?"
    displayDict["fr"].play_time_label = u"Temps de jeu"
    displayDict["fr"].show_manual_saves = u"Manuel"
    displayDict["fr"].show_auto_saves = u"Auto"

    displayDict["fr"].text_history_caption = u"Historique du texte"

    displayDict["fr"].extra_menu_caption = "Extras"
    displayDict["fr"].extra_music_button_label = "Juke-box"
    displayDict["fr"].extra_gallery_button_label = "Galerie"
    displayDict["fr"].extra_scene_button_label = "Bibliothèque"
    displayDict["fr"].extra_omake_button_label = "Omake"
    displayDict["fr"].extra_opening_button_label = "Cinéma"
    displayDict["fr"].commentary_label = "Activer les commentaires"

    displayDict["fr"].video_page_caption = "Extras > Cinéma"


    displayDict["fr"].music_page_caption = "Extras > Juke-box"
    displayDict["fr"].music_stop_button_text = "Stop"
    displayDict["fr"].music_now_playing = "Actuellement"

    displayDict["fr"].gallery_page_caption = "Extras > Galerie"
    displayDict["fr"].gallery_onelocked = "Une image restante non débloquée."
    displayDict["fr"].gallery_manylocked = "%d images restantes non débloquées."
    displayDict["fr"].gallery_singlelocked = "Images %d à %d non débloquées."
    displayDict["fr"].gallery_num_page_prefix = "Page"
    displayDict["fr"].gallery_num_page_error = "Aucune image à afficher"

    displayDict["fr"].scene_page_caption = "Extras > Bibliothèque"
    displayDict["fr"].scene_completion_label = "Complétion: %s%%"
    displayDict["fr"].scene_playthrough_label = "Utiliser la vitesse de rediffusion"
    displayDict["fr"].scene_launch_path = "Souhaitez-vous refaire\nla route entière ?"

    displayDict["fr"].joy_left = "Gauche"
    displayDict["fr"].joy_right = "Droite"
    displayDict["fr"].joy_up = "Haut"
    displayDict["fr"].joy_down = "Bas"
    displayDict["fr"].joy_dismiss = "Choix/Avancer"
    displayDict["fr"].joy_rollback = "Historique du texte"
    displayDict["fr"].joy_holdskip = "Rester en avance rapide"
    displayDict["fr"].joy_toggleskip = "Avance rapide"
    displayDict["fr"].joy_hide = "Montrer image"
    displayDict["fr"].joy_menu = "Montrer menu"



    displayDict["fr"].name_hi = "Hisao"

    displayDict["fr"].name_ha = "Hanako"
    displayDict["fr"].name_emi = "Emi"
    displayDict["fr"].name_rin = "Rin"
    displayDict["fr"].name_li = "Lilly"
    displayDict["fr"].name_shi = "Shizune"
    displayDict["fr"].name_mi = "Misha"

    displayDict["fr"].name_ke = "Kenji"
    displayDict["fr"].name_mu = "Mutou"
    displayDict["fr"].name_nk = "Infirmier"
    displayDict["fr"].name_no = "Nomiya"
    displayDict["fr"].name_yu = "Yuuko"
    displayDict["fr"].name_sa = "Sae"
    displayDict["fr"].name_aki = "Akira"
    displayDict["fr"].name_hh = "Hideaki"
    displayDict["fr"].name_hx = "Jigoro"
    displayDict["fr"].name_emm = "Meiko"
    displayDict["fr"].name_sk = "Gérant"
    displayDict["fr"].name_mk = "Miki"

    displayDict["fr"].name_mystery = "???"

    displayDict["fr"].name_ha_ = "Fille aux cheveux violets"
    displayDict["fr"].name_emi_ = "Fille aux couettes"
    displayDict["fr"].name_rin_ = "Fille étrange"
    displayDict["fr"].name_li_ = "Fille aux cheveux ondulés"
    displayDict["fr"].name_mi_ = "Fille riant"
    displayDict["fr"].name_ke_ = "Voisin binoclard"
    displayDict["fr"].name_mu_ = "Homme grand"
    displayDict["fr"].name_yu_ = "Bibliothécaire"
    displayDict["fr"].name_no_ = "Homme aux cheveux gris"
    displayDict["fr"].name_sa_ = "Galeriste"
    displayDict["fr"].name_aki_ = "Personne bien habillée"
    displayDict["fr"].name_nk_ = "Homme souriant"
    displayDict["fr"].name_hh_ = "Fille mince"
    displayDict["fr"].name_emm_ = "Femme avec tresses"
    displayDict["fr"].name_hx_ = "Grand homme"

    displayDict["fr"].videos = (("Opening", "video/base_op_1.mp4"),
                                ("Emi", "video/base_tc_act2_emi.mp4"),
                                ("Hanako", "video/base_tc_act2_hanako.mp4"),
                                ("Lilly", "video/base_tc_act2_lilly.mp4"),
                                ("Rin", "video/base_tc_act2_rin.mp4"),
                                ("Shizune", "video/base_tc_act2_shizune.mp4"),
                               )

    if (renpy.ios):
        displayDict["fr"].videos = (("Opening", "video/ios_op_1.mp4"),
                                    ("Emi", "video/ios_tc_act2_emi.mp4"),
                                    ("Hanako", "video/ios_tc_act2_hanako.mp4"),
                                    ("Lilly", "video/ios_tc_act2_lilly.mp4"),
                                    ("Rin", "video/ios_tc_act2_rin.mp4"),
                                    ("Shizune", "video/ios_tc_act2_shizune.mp4"),
                                )



    displayDict["fr"].s_scenes = (("Prologue", rp_actmark, rp_actmark, ("Act 1","Prologue")),
                                    (u"Dans le Froid", "NOP1", "Par une froide journée d'hiver, les rêves d'Hisao étaient sur le point de se réaliser, mais sont interrompus par une crise cardiaque.", ("Act 1","Prologue")),
                                    (u"Le Paquet d'Hisao", "NOP2", "Hisao entend parler de l'Académie Yamaku, où il sera probablement envoyé pour le reste de sa scolarité.", ("Act 1","Prologue")),
                                    (u"Acte 1: Espérance de Vie", rp_actmark, rp_actmark, "Act 1"),
                                    (u"L'effet du Portail", "A1", "Hisao met le pied dans l'Académie Yamaku pour la première fois, et rencontre son professeur principal, Mutou.", "Act 1"),
                                    (u"L'Entrée sur Scène", "A2", "Présentation à la classe, et rencontre avec la déléguée et son interprète.", "Act 1"),
                                    (u"Dans l'Infirmerie", "A3", "Misha et Shizune montrent la cafétéria à Hisao, après qu'il soit allé voir l'infirmier.", "Act 1"),
                                    (u"La Chambre de Personne", "A4", "Hisao emménage dans sa nouvelle chambre, rencontrant Kenji, son voisin de couloir par la même occasion.", "Act 1"),
                                    (u"Papotage", "A5", "Shizune et Misha parlent à Hisao du festival qui approche et l'invitent à déjeuner.", "Act 1"),
                                    (u"Risk vs Récompense", "A6", "Shizune et Hisao s'affrontent pour la conquête du monde à Risk.", "Act 1"),
                                    (u"Pseudo Salon de Thé", "A7", "Cherchant la bibliothèque, Hisao se perd et trouve Lilly dans une classe abandonnée.", "Act 1"),
                                    (u"Bibliothèque Partagée", "A8", "Trouvant finalement son chemin vers la bibliothèque, Hisao rencontre et effraie Hanako.", "Act 1"),
                                    (u"Bizarre et Surréel", "A9", "Kenji révèle les sombres secrets de Yamaku.", "Act 1"),
                                    (u"La Théorie de l'Évolution du Déjeuner", "A10", "Shizune et Misha font pression sur Hisao pour qu'il rejoigne le Conseil des Étudiants avant de discuter du déjeuner.", "Act 1"),
                                    (u"Rencontre Rapide", "A11_1", "Sur le chemin pour aller déjeuner avec Misha et Shizune, Hisao entre en collision avec Emi dans le couloir.", "Act 1"),
                                    (u"Mignonne Rencontre", "A11_2", "Hisao entre en collision avec une Emi déchaînée en route pour aller manger avec Hanako et Lilly.", "Act 1"),
                                    (u"Détour En Vue", "A12", "Shizune et Misha emmènent Hisao à leur salon de thé favori, le Shanghai.", "Act 1"),
                                    (u"Siroter (partie 1)", "A13", "Hisao passe un déjeuner paisible avec Lilly et Hanako.", "Act 1"), 
                                    (u"Ça Forme le Caractère", "A15", "Mutou essaye d'avoir une conversation sérieuse avec Hisao, mais Misha les interrompt et met Hisao au travail.", "Act 1"),
                                    (u"Un Déjeuner Privé", "A16", "Cherchant du matériel, Hisao rencontre une étrange fille dans la salle d'art.", "Act 1"),
                                    (u"Interception", "A17", "Pendant qu'il aide Rin à porter de la peinture, Hisao est questionné par l'infirmier.", "Act 1"),
                                    (u"L'Autre Vert", "A18", "Hisao regarde Rin peindre son mur.", "Act 1"),
                                    (u"La Fille qui Court", "A19", "Alors qu'il essaye de faire des exercices matinaux, Hisao rencontre Emi sur la piste de course.", "Act 1"),
                                    (u"Savon", "A20", "Kenji tend une embuscade à Hisao dans la douche dans l'intention d'avoir de l'argent.", "Act 1"),
                                    (u"Guerre Froide", "A21", "Shizune et Lilly font face aux requêtes budgétaires.", "Act 1"),
                                    (u"Preuve de Compétence", "A22", "Shizune et Misha attaquent Hisao dans l'intention de lui faire rejoindre le Conseil des Étudiants.", "Act 1"),
                                    (u"Événement à l'Horizon", "A22_2", "Shizune et Misha attaquent Hisao dans l'intention de lui faire rejoindre le Conseil des Étudiants.", "Act 1"),
                                    (u"Au-dessus et Au-delà", "A23_1", "Hisao a droit à un discours sur les nobles devoirs du Conseil des Étudiants.", "Act 1"),
                                    (u"Choses que Tu Peux Faire", "A23_2", "Après avoir échappé aux griffes de Shizune et Misha, Hisao aide encore Rin.", "Act 1"),
                                    (u"Peindre par Nombres", "A24", "Hanako et Hisao donnent un coup de main à la classe de Lilly pour monter leur stand.", "Act 1"),
                                    (u"Exercice", "A25", "Un autre matin où Hisao et Emi courent ensemble.", "Act 1"),
                                    (u"Chapeau Invisible", "A26", "Kenji donne à Hisao quelques conseils pour socialiser.", "Act 1"),
                                    (u"L'Avantage du Terrain", "A26_1", "Shizune et Misha interceptent Hisao pendant qu'il sort de sa chambre.", "Act 1"),
                                    (u"Aucune Récupération", "A27", False, "Act 1"), 
                                    (u"Récupération Lente", "A27_1", "Récupérant de son faux battement, Hisao retourne finalement en classe.", "Act 1"),
                                    (u"Aucune Récupération", "A27_2", "Hisao lutte en classe après son enrôlement par le Conseil des Étudiants.", "Act 1"),
                                    (u"Rien N'est Gratuit", "A28", "Hisao est escorté dans la salle du Conseil des Étudiants pour son premier jour officiel.", "Act 1"),
                                    (u"Pied et Bouche", "A29", "Emi emmène Hisao sur le toit pour déjeuner avec Rin.", "Act 1"),
                                    (u"Surveille Tes Pas", "A30", "Hisao et Lilly vont faire les courses, rencontrant une Rin très confuse sur le chemin du retour.", "Act 1"),
                                    (u"Support", "A31", "Hisao a son premier cours du samedi, complété par une discussion avec Mutou.", "Act 1"),
                                    (u"Une Esthétique", "A32", "Emi trouve Hisao en train d'errer après les cours et lui demande de l'aider avec Rin encore une fois.", "Act 1"),
                                    (u"Douleur Créative", "A33", "Hisao rencontre le professeur d'art, Nomiya, pendant que Rin peint son mur.", "Act 1"),
                                    (u"Un Bon Exercice", "A34", "Emi et Hisao discutent de l'importance d'être en bonne santé.", "Act 1"),
                                    (u"Siroter (Partie 2)", "A35", "Dans le but de passer le temps, Hisao va faire une balade autour de l'école.", "Act 1"),
                                    (u"Shanghaïsé", "A36", "Thé, cake et compétition avec Shizune et Misha au Shanghai.", "Act 1"),
                                    (u"Silence", "A37", "Hanako et Hisao lisent des livres pour le festival.", "Act 1"),
                                    (u"Ne Panique Pas", "A38", "Après s'être réveillé le jour du festival, Hisao a droit a une rodomontade de la part de Kenji.", "Act 1"),
                                    (u"C'est Carnaval !", "A39", "Emi attrape Hisao en train de manger de la nourriture frite et le force à lui tenir compagnie en punition.", "Act 1"),
                                    (u"Nc5xb3", "A42", "Incapable d'aider Lilly à son stand, Hisao cherche Hanako dans le festival.", "Act 1"),
                                    (u"Mouvement", "H2", "Lilly finit ses devoirs de déléguée et emmene Hanako et Hisao au Shanghai.", "Act 1"), 
                                    (u"Promesse de Temps", "A41", "Après une matinée à son stand, Hisao aide Lilly à trouver Hanako.", "Act 1"),
                                    (u"Nuages dans Ma Tête", "A40", "Hisao tient compagnie à Rin et à son mur maintenant fini.", "Act 1"),
                                    (u"Jeté de Balles", "A44", "Fidèle à sa promesse, Hisao passe la journée avec Shizune et Misha.", "Act 1"),
                                    (u"La Fin Profonde", "A43", "Kenji et Hisao partagent un pique-nique viril sur le toit au lieu d'aller au festival.", "Act 1"),
                                    (u"Acte 2 : Forme", rp_actmark, rp_actmark, ("Act 2","Emi")),
                                    (u"Course Matinale", "E3", "La premiere course d'une longue série avec Emi.", ("Act 2","Emi")),
                                    (u"Nuages, Voyage dans le Temps, et toi", "E4", "Un autre déjeuner sur le toit avec Emi et Rin. Emi extirpe une promesse de la part d'Hisao pour sa venue à la rencontre d'athlétisme.", ("Acte 2","Emi")),
                                    (u"Questions qui ont Besoin de Réponses !", "E5", "Discussion entre Emi et Hisao. Hisao pose quelques questions à Emi sur sa relation avec Rin.", ("Act 2","Emi")),
                                    (u"C'est Pire la Seconde Fois", "E6", "La seconde matinée de courses. Hisao est presque tiré par les cheveux autour de la piste.", ("Act 2","Emi")),
                                    (u"Une Pomme un Jour", "E7", "Hisao rend une visite à l'infirmier avec Emi, découvrant qu'ils se connaissent depuis un moment.", ("Act 2","Emi")),
                                    (u"Rencontre d'Athlétisme", "E8", "Le jour de la rencontre. Une autre facette de la personnalité d'Emi est révélée.", ("Act 2","Emi")),
                                    (u"Prends tes Médicaments Maintenant", "E9", "Hisao mentionne une douleur à la poitrine durant une visite à l'infirmier et se fait disputer.", ("Act 2","Emi")),
                                    (u"Pirates de Haute Mer", "E10", "Hisao discute de son avenir avec un accent de pirate sur le toit avec Emi, puis une lettre d'Iwanako gâche la journée.", ("Act 2","Emi")),
                                    (u"Fameux Derniers Mots", "E11", "Emi et Rin emmènent Hisao pour un pique-nique, qui se retrouve gâché par la pluie.", ("Act 2","Emi")),
                                    (u"Absence de Piste", "E12", "Hisao va à la piste comme d'habitude, mais Emi est absente.", ("Act 2","Emi")),
                                    (u"Visite", "E13", "Une visite à Emi qui est alitée mais qui se change rapidement en quelque chose de complètement différent.", ("Act 2","Emi")),
                                    (u"Le Premier Matin d'Après", "E14", "Hisao se rappelle la soirée de la veille, décidant de faire quelque chose pour aider Emi.", ("Act 2","Emi")),
                                    (u"Le (Vrai) Commencement", "E15", "Un autre déjeuner sur le toit, sans Rin.", ("Act 2","Emi")),
                                    (u"Acte 3 : Perspective", rp_actmark, rp_actmark, ("Act 3","Emi")),
                                    (u"Eet Ees… Scienca", "E16", "Mutou discute brièvement avec Hisao à propos de son avenir.", ("Act 3","Emi")),
                                    (u"Définitions", "E17", "Emi et Hisao essayant de faire un autre pique-nique, sans intervention de mère nature cette fois.", ("Act 3","Emi")),
                                    (u"Pierre Invisible", "E18", "Retour à la piste le matin, pareil que d'habitude... ou pas.", ("Act 3","Emi")),
                                    (u"Déjeuner et Science", "E19", "Hisao reparle avec Mutou à propos de son avenir dans les sciences.", ("Act 3","Emi")),
                                    (u"Haut, Bas, et de Nouveau Haut", "E20", "Un appel urgent d'Emi amène Hisao jusqu'à sa chambre, où deux surprises l'attendent.", ("Act 3","Emi")),
                                    (u"La Réserve", "E21", "Emi embusque Hisao dans le local d'athlétisme.", ("Act 3","Emi")),
                                    (u"Plans Apres l'École", "E22", "Emi a une discussion sérieuse avec Hisao à propos des examens à venir.", ("Act 3","Emi")),
                                    (u"Détachée", "E23", "Hisao broie du noir à propos de sa relation avec Emi.", ("Act 3","Emi")), 
                                    (u"Douleur Fantôme", "E24", "La tentative d'Hisao de montrer son inquiétude ne se passe pas du tout comme prévu.", ("Act 3","Emi")),
                                    (u"Doute Express", "E25", "Hisao est troublé par le comportement d'Emi et par l'invitation à sa maison.", ("Act 3","Emi")),
                                    (u"Devine Qui Vient… Peu Importe", "E26", "Dîner à la maison Ibarazaki.", ("Act 3","Emi")),
                                    (u"Relecture Instantanée", "E27", "Les choses arrivent à leur terme à la piste d'athlétisme.", ("Act 3","Emi")),
                                    (u"Acte 4 : Mouvement", rp_actmark, rp_actmark, ("Act 4","Emi")),
                                    (u"Un Geste et un Loupé", "E28", "Hisao se demande si Emi l'évite volontairement.", ("Act 4","Emi")),
                                    (u"Rattraper la Balle", "E29", "Les choses arrivent à leur terme sur le toit.", ("Act 4","Emi")),
                                    (u"Murmures du Passé", "E30", "Hisao, Emi et sa mère vont au cimetière.", ("Act 4","Emi")),
                                    (u"Vive les Chaussettes", "E31", "Sexe, drogues, mais pas rock'n'roll.", ("Act 4","Emi")),
                                    (u"Dents Propres", "E32", "Hisao se réveille, découvrant Emi dormant à côté de lui.", ("Act 4","Emi")),
                                    (u"Act 2 : Cache-Cache", rp_actmark, rp_actmark, ("Act 2","Hanako")),
                                    (u"En Ville, En Ville", "H3", "En chemin jusqu'à la supérette avec Hanako.", ("Act 2","Hanako")),
                                    (u"Feuilles de Thé", "H4", "Hanako invite Hisao à aller déjeuner avec elle et Lilly.", ("Act 2","Hanako")),
                                    (u"Confession au Bureau", "H5_1", "Hisao et Misha parlent de Hanako.", ("Act 2","Hanako")),
                                    (u"Échecs et glissades", "H5_2", "Hisao abandonne le Conseil des Étudiants pour lire avec Hanako.", ("Act 2","Hanako")),
                                    (u"Lève-Toi et Marche", "H6", "Une invitation de Lilly à boire le thé après les cours.", ("Act 2","Hanako")),
                                    (u"Chapelier Fou", "H7", "Hanako, Hisao et Lilly se rencontrent pour boire le thé dans la chambre de Lilly.", ("Act 2","Hanako")),
                                    (u"Petit Changement", "H8", "Kenji est forcé à payer ses dettes.", ("Act 2","Hanako")),
                                    (u"Absentéisme", "H9", "Hisao et Lilly discutent du taux de présence de Hanako.", ("Act 2","Hanako")),
                                    (u"Échange Équivalent", "H10", "Sachant pour le cœur de Hisao, Hanako révèle une partie de son passé en retour.", ("Act 2","Hanako")),
                                    (u"Act 3 : Roque", rp_actmark, rp_actmark, ("Act 3","Hanako")),
                                    (u"Invitation", "H11", "Lilly trouve Hisao en train de nettoyer la Salle du Thé et lui parle de l'anniversaire de Hanako.", ("Act 3","Hanako")),
                                    (u"Rencontre Ombragée", "H12", "Une discussion imprévue avec Miki arrive pendant qu'Hisao se remémore le passé.", ("Act 3","Hanako")),
                                    (u"Antiquités et Tarte", "H13", "Lilly et Hisao vont acheter un cadeau en ville.", ("Act 3","Hanako")),
                                    (u"Chute", "H14", "Hanako a une crise de panique durant les cours.", ("Act 3","Hanako")),
                                    (u"Avancée Lente", "H15", "Lilly a des mauvaises nouvelles à annoncer à Hisao et Hanako.", ("Act 3","Hanako")),
                                    (u"Atteinte", "H16", "Hisao essaye d'atteindre une Hanako recluse.", ("Act 3","Hanako")),
                                    (u"Une Année de Plus", "H17", "Notre trio est rejoint par un invité inattendu alors qu'ils célèbrent l'anniversaire de Hanako.", ("Act 3","Hanako")),
                                    (u"Un Morceau de Papier", "H18", "Hisao apprécie sa première gueule de bois, puis reçoit une lettre troublante.", ("Act 3","Hanako")),
                                    (u"Bribes et Morceaux", "H19", "Cœur à cœur durant une partie de billard.", ("Act 3","Hanako")),
                                    (u"Début de la Fin", "H20", "Le départ de Lilly.", ("Act 3","Hanako")),
                                    (u"Acte 4 : Cicatrices", rp_actmark, rp_actmark, ("Act 4","Hanako")),
                                    (u"Absence", "H21", "Déjeuner avec le Conseil des Étudiants et inquiétudes à propos de Hanako qui se renferme.", ("Act 4","Hanako")),
                                    (u"Présence Lointaine", "H22", "Hisao téléphone à Lilly pour avoir des conseils au sujet de Hanako qui est restée enfermée un jour de plus.", ("Act 4","Hanako")),
                                    (u"Faux Pas", "H23", "Hisao essaye de faire sortir Hanako de sa chambre, avec des résultats étonnants.", ("Act 4","Hanako")),
                                    (u"Pétales Arrachées", "H24", "Hisao trouve sa future relation avec Hanako terminée prématurément.", ("Act 4","Hanako")),
                                    (u"Mélodie Continue", "H25", "Hanako retourne en classe, ce qui rassure Hisao.", ("Act 4","Hanako")),
                                    (u"Études au Shanghai", "H26", "Essayant d'éviter les distractions, Hisao essaye d'étudier au Shanghai.", ("Act 4","Hanako")),
                                    (u"Son passé", "H27", "Dans une tentative de se rapprocher de Hanako, Hisao partage un peu de son passé avec elle.", ("Act 4","Hanako")),
                                    (u"Rendez-Vous en Ville", "H28", "Ils vont ensemble se balader dans la métropole.", ("Act 4","Hanako")),
                                    (u"Un Toucher Timide", "H29", "Hisao et Hanako passent la nuit ensemble.", ("Act 4","Hanako")),
                                    (u"Futur Indéterminé", "H30", "Les événements de la nuit précédente pèsent lourdement sur Hisao.", ("Act 4","Hanako")),
                                    (u"La voie d'un adulte", "H31", "La fin de deux enfants, le début de deux adultes.", ("Act 4","Hanako")),
                                    (u"Acte 2 : Passé", rp_actmark, rp_actmark, ("Act 2","Lilly")),
                                    (u"Earl Grey", "L1", "Hisao partage le premier de nombreux déjeuners avec Hanako et Lilly, récupérant du jour précédent.", ("Act 2","Lilly")),
                                    (u"Une Livre Sterling", "L2", "Questionné par Kenji sur la nationalité de Lilly, Hisao décide de mener son enquête et découvre quelque chose d'intéressant.", ("Act 2","Lilly")),
                                    (u"Présents et Présence", "L3", "Pendant qu'ils sont sortis chercher un cadeau pour Hanako, Lilly et Hisao rencontrent Akira et son cousin.", ("Act 2","Lilly")),
                                    (u"Objet Buvant Non Identifié", "L4", "Le trio fait une fête d'anniversaire pour Hanako, interrompu par l'apparition surprise d'un membre de la famille.", ("Act 2","Lilly")),
                                    (u"Le Jour d'Après", "L5", "Hisao et Lilly se réveillent et essayent de récupérer des événements de la veille.", ("Act 2","Lilly")),
                                    (u"Une Brève Histoire de Thym", "L6", "Hisao et Lilly vont faire des courses.", ("Act 2","Lilly")),
                                    (u"Petite Aile", "L7", "Un déjeuner sur le toit prend un tour malheureux.", ("Act 2","Lilly")),
                                    (u"Good Trip", "L8", "Lilly et Akira font leurs au revoir alors qu'ils partent en voyage pour voir leur famille en Écosse.", ("Act 2","Lilly")),
                                    (u"Acte 3 : Présent", rp_actmark, rp_actmark, ("Act 3","Lilly")),
                                    (u"Jour par Jour", "L9", "Hisao passe un jour sans Lilly, discutant avec Mutou de Yamaku.", ("Act 3","Lilly")),
                                    (u"Discorde Mineure", "L10", "Hisao a un déjeuner avec Kenji, puis donne des photocopies à une Hanako bien trop silencieuse.", ("Act 3","Lilly")),
                                    (u"Dissonance", "L11", "Avec Hanako s'isolant complètement, Hisao offre le peu d'aide qu'il peut avant d'appeler Lilly.", ("Act 3","Lilly")),
                                    (u"Un Monde de Distance", "L12", "Hisao maintenant rassuré commence à se poser des questions sur la relation entre Lilly et lui.", ("Act 3","Lilly")),
                                    (u"Renouveau", "L13", "Hisao, Hanako et Hideaki accueillent Akira et Lilly après leur retour d'Écosse.", ("Act 3","Lilly")),
                                    (u"Séjour au Nord", "L14", "Le trio commence son voyage à Hokkaido.", ("Act 3","Lilly")),
                                    (u"Prélude", "L15", "Une marche matinale qui n'est que le début d'une chaîne d'événements.", ("Act 3","Lilly")),
                                    (u"Crescendo", "L16", "Les vrais sentiments de Lilly sont étalés devant l'or infini des champs de blé." , ("Act 3","Lilly")),
                                    (u"Diminuendo", "L17", "Notre couple partage leur première nuit ensemble.", ("Act 3","Lilly")),
                                    (u"Perspective Grisée", "L18", "Confinés dans la maison d'été, Lilly et Hisao sont forcés de mettre un mot sur leur relation.", ("Act 3","Lilly")),
                                    (u"Rhapsodie en Bleu", "L19", "Hisao se baignant pense à où en sont Lilly et lui dans la vie, avant d'être rejoint par quelqu'un.", ("Act 3","Lilly")),
                                    (u"Acte 4 : Futur", rp_actmark, rp_actmark, ("Act 4","Lilly")),
                                    (u"Le Présent Momentané", "L20", "Retournant à Yamaku, Hisao et Lilly discutent.", ("Act 4","Lilly")),
                                    (u"Petits Pas avant la Danse", "L21", "De retour à l'école, les événements de Hokkaido reviennent en mémoire.", ("Act 4","Lilly")),
                                    (u"Pyjamas et Costumes", "L22", "Retour à la vie quotidienne. Akira rejoint le trio durant un thé.", ("Act 4","Lilly")),
                                    (u"Procédure Correcte", "L23", "Hisao et Lilly arrangent un rendez-vous, avant qu'Akira ne passe.", ("Act 4","Lilly")),
                                    (u"Être et savoir", "L24", "Hisao et Lilly patagent leur premier rendez-vous, découvrant un peu du passé de chacun.", ("Act 4","Lilly")),
                                    (u"Une Rêverie Matinale", "L25", "Hisao et Lilly discutent de leurs ambitions pour l'avenir.", ("Act 4","Lilly")),
                                    (u"Black-Out", "L26", "Le trio pense aux vacances à venir, avant que Hisao expérimente la vue comme Lilly.", ("Act 4","Lilly")),
                                    (u"Contexte", "L27", "Hisao se fait appeler par Akira et ils discutent tous deux de sa sœur.", ("Act 4","Lilly")),
                                    (u"Un Futur Lointain", "L28", "Lilly révèle l'offre de sa famille de les rejoindre en Écosse.", ("Act 4","Lilly")),
                                    (u"Au Revoir", "L29", "Au revoir à Akira et Lilly le soir avant de quitter le Japon.", ("Act 4","Lilly")),
                                    (u"Fausse Cadence", "L30", "Hisao se précipite pour se confronter à Lilly, réalisant ses doutes.", ("Act 4","Lilly")),
                                    (u"Sous un Ciel Gris", "L31", "Se réveillant dans un hôpital, Hisao lutte pour mettre au point sa vie.", ("Act 4","Lilly")),
                                    (u"Sous un Ciel Clair", "L32", "Lilly rejoint Hisao, et ils commencent tous deux leur nouvelle vie ensemble.", ("Act 4","Lilly")),
                                    (u"En avant, avec foi !", "L33", "Lilly et Hisao disent au revoir à Akira.", ("Act 4","Lilly")),
                                    (u"Act 2 : Déconnecté", rp_actmark, rp_actmark, ("Act 2","Rin")),
                                    (u"Un Plus Grand Champ de Vision", "R1", "Hisao passe sa pause déjeuner sur le toit avec Rin à regarder les nuages.", ("Act 2","Rin")),
                                    (u"Études de Niveaux de Gris", "R2", "Rin et Hisao dessinent chacun le portrait de l'autre durant sa première réunion du club.", ("Act 2","Rin")),
                                    (u"Instersticiel", "R3", "Kenji prête un livre “emprunté” à Hisao.", ("Act 2","Rin")),
                                    (u"Études Personnelles", "R4", "Misha et Shizune surprennent Hisao en train de dessiner sur son cahier durant les cours.", ("Act 2","Rin")),
                                    (u"Le sourire de Hisao", "R5", "Rin parle à Hisao de ses expressions joyeuses, ou plutôt du manque de celles-ci.", ("Act 2","Rin")),
                                    (u"Choses que Tu Aimes", "R6", "Brève rêverie avec Yuuko à propos de livres et Yamaku.", ("Act 2","Rin")),
                                    (u"Audience Ciblée", "R7", "Le jour de la rencontre d'athlétisme. Des facettes de la personnalité d'Emi et de Rin sont révélées.", ("Act 2","Rin")),
                                    (u"L'Éternité En une Heure", "R8", "Nomiya incite à la discussion sur l'art durant une réunion du club.", ("Act 2","Rin")),
                                    (u"Sous l'Eau et un Érable avec un Nom", "R9", "Rin mène Hisao dans les bois, où ils pensent à leur avenir proche.", ("Act 2","Rin")),
                                    (u"Le Regret d'Iwanako", "R10", "Une lettre d'Iwanako arrive.", ("Act 2","Rin")),
                                    (u"À Sa Propre Image", "R11", "Hisao pousse Rin à avoir sa propre exposition d'art.", ("Act 2","Rin")),
                                    (u"Le Gâteau de la Logique du Parapluie", "R12", "Emi, Hisao et Rin sont sous la pluie et cherchent un refuge au Shanghai.", ("Act 2","Rin")),
                                    (u"Six Mètres Plus Proche du Paradis", "R13", "Rin et Hisao ne mangent PAS un déjeuner sur le toit, à cause de l'absence d'Emi", ("Act 2","Rin")),
                                    (u"Indécis", "R14", "Emi récupère de son rhume et Rin se l'approprie.", ("Act 2","Rin")),
                                    (u"Interférences dans le Signal", "R15", "Hisao va dans la chambre de Rin pour lui rendre visite", ("Act 2","Rin")),
                                    (u"Pissenlit", "R16", "Des conclusions se font en haut d'une colline.", ("Act 2","Rin")),
                                    (u"Acte 3 : Distance", rp_actmark, rp_actmark, ("Act 3","Rin")),
                                    (u"22nd Corner", "R17", "L'équipe du club d'art va voir la galerie pour la future exposition de Rin.", ("Act 3","Rin")),
                                    (u"L'Odeur de la Lumière", "R18", "Hisao surprend Rin à dormir dans la salle d'art.", ("Act 3","Rin")),
                                    (u"Choses qu'on ne Peut Pas Abandonner", "R19", "Emi et Hisao discutent de la personnalité de Rin.", ("Act 3","Rin")),
                                    (u"KABOUUM !", "R20", "Les pensées de Yuuko sur la motivation.", ("Act 3","Rin")),
                                    (u"Lunettes Teintées Roses", "R21", "Nomiya parle sans s'arrêter de l'art en tant que carrière.", ("Act 3","Rin")),
                                    (u"Le Bout du Monde", "R22", "Hisao fait sa déclaration à Rin et se fait rejeter. Vraiment ?", ("Act 3","Rin")),
                                    (u"Le Contexte de Rin", "R23", "Un après-midi gênant et silencieux dans l'atelier.", ("Act 3","Rin")),
                                    (u"Avance Rapide", "R23_2", "Les préparations de l'exposition s'arrangent dans une étrange routine.", ("Act 3","Rin")),
                                    (u"Auto-Destruction", "R24", "Rin expérimente la cigarette pour avoir un œil neuf sur la créativité.", ("Act 3","Rin")),
                                    (u"Echappatoire Inverse", "R25", "Hisao emmène Rin dans une balade dans les rues la nuit.", ("Act 3","Rin")),
                                    (u"Sans Limite", "R26", "Sae et Nomiya donnent une vision sur la vie des artistes.", ("Act 3","Rin")),
                                    (u"Delirium", "R27", "Hisao surprend une Rin desespérée dans l'atelier.", ("Act 3","Rin")),
                                    (u"Choses que Tu Détestes", "R28", "Réflexions désagreables d'une nuit incroyable.", ("Act 3","Rin")),
                                    (u"Tesson de Colère", "R29", "La relation épuisée entre les deux éclate.", ("Act 3","Rin")),
                                    (u"Acte 4 : Rêve", rp_actmark, rp_actmark, ("Act 4","Rin")),
                                    (u"Illusions pour les Gens", "R30", "Hisao parle de ses doutes à Nomiya, sans effet.", ("Act 4","Rin")),
                                    (u"Désabusé", "R31", "La patience d'Hisao arrive à sa fin.", ("Act 4","Rin")),
                                    (u"La Scène", "R32", "Rencontre avec Rin à l'ouverture de l'exposition.", ("Act 4","Rin")), 
                                    (u"Longueur D'Onde", "R35", "Léthargique, Hisao attend que le temps passe durant le dernier jour des examens.", ("Act 4","Rin")),
                                    (u"Période Bleue", "R36", "Un jour de pluie, le 22nd Corner, et une brève histoire sur Picasso.", ("Act 4","Rin")),
                                    (u"Le Monde Que Seul Toi Peux Voir", "R37", "Rin et Hisao se séparent après la pluie.", ("Act 4","Rin")),
                                    (u"Gloire Desespérée", "R34", "Un Nomiya énervé interroge Hisao sur Rin.", ("Act 4","Rin")), 
                                    (u"Problème de Logique Autocentrée", "R38", "Hisao trouve Rin à sa cachette habituelle, et la convainc d'aller parler avec Nomiya.", ("Act 4","Rin")),
                                    (u"Mesurer les Ombres", "R39", "L'excuse de Rin au professeur d'art n'est pas bien reçue.", ("Act 4","Rin")),
                                    (u"Raison d'Être", "R40", "Hisao réconforte une Rin malheureuse.", ("Act 4","Rin")),
                                    (u"Sans Respirer, Sans un Son", "R41", "Le premier jour des vacances d'été, Rin vient dans la chambre de Hisao.", ("Act 4","Rin")),
                                    (u"Preuve d'Existence", "R42", "Tout prend forme sur la colline couverte de pissenlits.", ("Act 4","Rin")),
                                    (u"Acte 2 : Apprendre à Lire", rp_actmark, rp_actmark, ("Act 2","Shizune")),
                                    (u"Message Passant", "S8", "Shizune et Hisao explorent diverses méthodes de communication.", ("Act 2","Shizune")),
                                    (u"Parler à la Main", "S9", "Hisao commence à étudier un nouveau langage et un tuteur apparaît.", ("Act 2","Shizune")),
                                    (u"Murmures Chinois", "S10", "Kenji réussit à forcer Hisao à lui rendre service, mais Hisao se retrouve confrontés à de nombreux soucis.", ("Act 2","Shizune")),
                                    (u"Théorie du Jeu Avancé", "S11", "RISK n'est pas suffisant pour satisfaire l'appétit de Shizune. Encore pire, un nouvel adversaire fait son apparition.", ("Act 2","Shizune")),
                                    (u"Pain, Papier, Ciseaux", "S12", "Un après-midi flemmard devient chaotique alors qu'un simple sandwich devient un objet d'intérêt général.", ("Act 2","Shizune")),
                                    (u"Interface", "S13", "Shizune et Hisao trouvent une connexion.", ("Act 2","Shizune")),
                                    (u"Sauter dans l'Action", "S14", "Hisao doit faire le médiateur entre Lilly et Shizune, mais heureusement les choses se résolvent en fin de compte.", ("Act 2","Shizune")),
                                    (u"Passé Inaccompli", "S15", "Le Conseil des Étudiants se rappelle des années passées tout en se relaxant au Shanghai.", ("Act 2","Shizune")),
                                    (u"Quand les Étoiles se Croisent", "S16", "C'est enfin le moment de Tanabata !", ("Act 2","Shizune")),
                                    (u"Acte 3 : Tour de Passe-passe", rp_actmark, rp_actmark, ("Act 3","Shizune")),
                                    (u"Retour Forcé", "S17", "Hisao découvre que Shizune va rendre visite à sa famille, et s'arrange pour faire partie du voyage.", ("Act 3","Shizune")),
                                    (u"Nations Unies", "S18", "Le voyage jusqu'à la maison de Shizune, la rencontre avec son petit frère et un concours soudain de pêche", ("Act 3","Shizune")),
                                    (u"Avec Mention Distinction", "S19", "Hideaki essaye d'occuper Hisao pendant une journée avec peu de succès.", ("Act 3","Shizune")),
                                    (u"Complot Familial", "S20", "Notre trio rencontre le père de Shizune et bat presque immédiatement en retraite.", ("Act 3","Shizune")),
                                    (u"Fenêtre Pangrammatique", "S21", "Une requête de Hideaki pour apprendre le langage des signes se change improbablement en un concours de cris avec Jigoro.", ("Act 3","Shizune")),
                                    (u"Plus Proche", "S22", "Shizune et Hisao se réunissent pour la première fois.", ("Act 3","Shizune")),
                                    (u"Confrontation", "S23", "Jigoro dénigre le Conseil des Étudiants et Hisao relève le challenge.", ("Act 3","Shizune")),
                                    (u"L'Ancre", "S24", "De retour à Yamaku. Une lettre de Iwanako déclenche une longue discussion avec Kenji sur les petites copines.", ("Act 3","Shizune")),
                                    (u"Feuille de Route", "S25", "Le Conseil des Étudiants s'inquiète de sa succession, et Hisao finit d'une certaine facon par payer un parfait à Misha.", ("Act 3","Shizune")), 
                                    (u"Triangle Isocèle", "S26", "Un après-midi de travail avec Shizune montre à Hisao qu'il y a quelque chose qui ne va pas entre les deux filles.", ("Act 3","Shizune")),
                                    (u"Les Yeux Vides", "S27", "Yuuko demande à Hisao de surveiller la bibliothèque pour elle. L'arrivée de Kenji rend les choses difficiles.", ("Act 3","Shizune")),
                                    (u"La Langue Liée", "S28", "Misha rend visite à Hisao dans sa chambre, et les choses prennent une tournure étonnante.", ("Act 3","Shizune")),
                                    (u"Regarder de Côté", "S29_1", "Hisao rencontre une Misha déprimée sur le toit. Il finit par réunir Misha et Shizune.", ("Act 3","Shizune")),
                                    (u"Regarder Devant", "S29_2", "Hisao rencontre une Misha déprimée sur le toit. Shizune les rejoint et remet le conseil entier au travail.", ("Act 3","Shizune")),
                                    (u"Acte 4 : À Mon Autre Moi", rp_actmark, rp_actmark, ("Act 4","Shizune")),
                                    (u"Grand Strategy", "S30", "Shizune confesse à Hisao certains de ses buts et de ses échecs.", ("Act 4","Shizune")),
                                    (u"Sauf Pour Une", "S31", "Une tentative ratée de réconforter Misha se transforme en un rendez-vous impromptu entre Hisao et Shizune.", ("Act 4","Shizune")),
                                    (u"Invasion", "S32", "Jigoro et Hideaki rendent une visite quelque peu désagréable à Shizune.", ("Act 4","Shizune")),
                                    (u"Parfait", "S33", "Hisao et Shizune cherchent Misha. Hisao arrive finalement à l'attraper et à discuter correctement.", ("Act 4","Shizune")),
                                    (u"Tension Présente", "S38", "Hisao croise Lilly au déjeuner et ils discutent de Shizune.", ("Act 4","Shizune")), 
                                    (u"Spirale", "S39", "Poursuite, obstruction et embuscade de Kenji la nuit.", ("Act 4","Shizune")),
                                    (u"Terminal", "S40", "Une discussion tôt dans la matinée avec Shizune dans l'école.", ("Act 4","Shizune")),
                                    (u"Le Sommet", "S34", "Kenji et Shizune se rencontrent dans la chambre de Hisao. Miraculeusement, rien n'explose.", ("Act 4","Shizune")), 
                                    (u"Succession", "S35", "Le Conseil des Étudiants actuel peaufine sa succession avant d'engager des “activités extrascolaires”.", ("Act 4","Shizune")),
                                    (u"Mission d'Infiltration", "S36", "La détermination de Misha encourage Shizune à viser plus haut.", ("Act 4","Shizune")),
                                    (u"Infinité", "S37", "Notre trio renouvelle leur amitié, avec l'année arrivant à sa fin.", ("Act 4","Shizune")),
                                    )



    displayDict["fr"].creditstring = u"""{image=ui/flourish_left.png} {b}Écrivains{/b} {image=ui/flourish_right.png}
Anonymous22
Aura
cpl_crud
Suriko
TheHivemind

{image=ui/flourish_left.png} {b}Éditeurs{/b} {image=ui/flourish_right.png}
Kagami
Losstarot
Silentcook

{image=ui/flourish_left.png} {b}Musiques{/b} {image=ui/flourish_right.png}
Blue123
NicolArmarfi

{image=ui/flourish_left.png} {b}Dessinateurs{/b} {image=ui/flourish_right.png}
gebyy-terar
Kamifish
moekki
pimmy
raemz
Raide

{image=ui/flourish_left.png} {b}Dessinateurs Additionnels{/b} {image=ui/flourish_right.png}
climatic
Doomfest
yujovi

{image=ui/flourish_left.png} {b}FMV Animation{/b} {image=ui/flourish_right.png}
Mike Inel

{image=ui/flourish_left.png} {b}Direction{/b} {image=ui/flourish_right.png}
delta
Raide
yujovi

{image=ui/flourish_left.png} {b}Programmation{/b} {image=ui/flourish_right.png}
delta

{image=ui/flourish_left.png} {b}Producteurs{/b} {image=ui/flourish_right.png}
cpl_crud
Suriko


{image=ui/flourish_center.png}


{image=ui/flourish_left.png} {b}Édition Française{/b} {image=ui/flourish_right.png}
Kawa Soft

{image=ui/flourish_left.png} {b}Traduction{/b} {image=ui/flourish_right.png}
Jisa

{image=ui/flourish_left.png} {b}Correction{/b} {image=ui/flourish_right.png}
Saya Akya
Wyrine
Thibaud
Enzan
Fairy
Toto
Animus

{image=ui/flourish_left.png} {b}Moteur{/b} {image=ui/flourish_right.png}
Mop


{image=ui/flourish_center.png}


{image=ui/flourish_left.png} {b}Remerciements{/b} {image=ui/flourish_right.png}
Ambi07
abscess
Anonymous
Celiest
ContinualNaba
Dark_Mercury
DuaneMoody
Fink
frumplstlskn
Ismuth
Japesland
Juno
kekekeke
konflikti
Magaran
Mirage_GSM
OverCoat
Peorth
Petaru
silentkyon
skim
stirfriedweasel
Syureria
TcDohl
tottori
VCR

{image=ui/flourish_left.png} {b}Remerciements Particuliers{/b} {image=ui/flourish_right.png}
hir
PyTom
RAITA
replicated"""


    displayDict["fr"].drugs_wordlist  =  ["Disopyramide",
                        u"Warfarine",
                        u"Diltiazem",
                        u"Félodipine",
                        u"Propanolol",
                        u"Penbutolol",
                        u"Cartéolol",
                        u"Procaïnamide",
                        u"Héparine",
                        u"Phénytoïne",
                        u"Vérapamil",
                        u"Quinidine",
                        u"Flécaïnide",
                        u"5mg/jour",
                        u"400mg/jour",
                        u"15ml/jour",
                        u"100mg/jour",
                        u"10ml/48h",
                        u"10ml/jour",
                        u"200mg/12h",
                        u"50mg/12h",
                        u"500mg/48h",
                        u"125mg/12h",
                        u"25ml/jour",
                        u"cauchemars",
                        u"diminution de la concentration",
                        u"bradycardie",
                        u"dépression clinique",
                        u"insomnie",
                        u"dysfonction érectile",
                        u"vision anormale",
                        u"insuffisance cardiaque",
                        u"nausées",
                        u"étourdissements",
                        u"hallucinations",
                        u"bronchospasme",
                        u"dyspnée",
                        u"fatigue",
                        u"hypotension",
                        u"bloc cardiaque",
                        u"extrémités froides",
                        u"diarrhée",
                        u"arrêt cardiaque",
                        u"fibrillation ventriculaire",
                        u"ataxie",
                        u"asthme"]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
