init -2 python:



    init_language("es")

    displayDict["es"].styleoverrides = {"font": mainfont,
                                        "language": "western",
                                        "line_spacing": 0}

    displayDict["es"].timeformat = "%b %d, %H:%M"

    displayDict["es"].sayfont = mainfont

    displayDict["es"].quote_outer_open = u"“"
    displayDict["es"].quote_outer_close = u"”"
    displayDict["es"].quote_inner_open = u"‘"
    displayDict["es"].quote_inner_close = u"’"

    displayDict["es"].activeLanguage = u"Español Internacional"
    displayDict["es"].allLanguages = {}
    displayDict["es"].allLanguages["es"] = displayDict["es"].activeLanguage
    displayDict["es"].allLanguages["en"] = u"Inglés"
    displayDict["es"].allLanguages["de"] = u"Alemán"
    displayDict["es"].allLanguages["it"] = "Italiano"
    displayDict["es"].allLanguages["fr"] = u"Francés"
    displayDict["es"].allLanguages["jp"] = u"Japonés"

    displayDict["es"].act_term = u"Acto"
    displayDict["es"].window_name = u"Katawa Shoujo"

    displayDict["es"].main_menu_start = u"Inicio"
    displayDict["es"].main_menu_load = u"Cargar"
    displayDict["es"].main_menu_extra = u"Extras"
    displayDict["es"].main_menu_config = u"Opciones"
    displayDict["es"].main_menu_quit = u"Salir"

    displayDict["es"].game_menu_return = u"Regresar"
    displayDict["es"].game_menu_show = u"Mostrar imagen"
    displayDict["es"].game_menu_history = u"Historial"
    displayDict["es"].game_menu_skip = u"Avance rápido"
    displayDict["es"].game_menu_auto = u"Modo auto"
    displayDict["es"].game_menu_config = u"Opciones"
    displayDict["es"].game_menu_save = u"Guardar"
    displayDict["es"].game_menu_load = u"Cargar"
    displayDict["es"].game_menu_main = u"Menú principal"
    displayDict["es"].game_menu_quit = u"Salir"
    displayDict["es"].game_menu_current_scene = u"Escena actual"
    displayDict["es"].game_menu_current_music = u"Pista de música actual"
    displayDict["es"].game_menu_replay_indicator = u"Repetir"

    displayDict["es"].return_button_text = u"Volver"

    displayDict["es"].hdisabled_label = u"Deshabilitar contenido adulto"
    displayDict["es"].config_page_caption = u"Opciones"
    displayDict["es"].config_fullscreen_label = u'Modo pantalla completa'
    displayDict["es"].config_transitions_label = u'Deshabilitar transiciones'
    displayDict["es"].config_skip_unseen_label = u'Saltar texto no leído'
    displayDict["es"].config_skip_after_choice_label = u'Seguir saltando después de decidir'
    displayDict["es"].config_textspeed_label = u'Velocidad del texto'
    displayDict["es"].config_afmspeed_label = u'Demora del modo auto'
    displayDict["es"].config_musicvol_label = u"Volumen de música"
    displayDict["es"].config_musicvol_jukebox_label = u"Vol."
    displayDict["es"].config_sfxvol_label = u"Volumen SFX"
    displayDict["es"].config_sfxtest_label = u"Probar"
    displayDict["es"].config_gamepad_label = u"Mapeo del control de mando…"

    displayDict["es"].config_language_sel = u"Selección de idioma…"
    displayDict["es"].config_language_caption = u"Opciones > Selección de idioma"
    displayDict["es"].config_language_restart_note = u"Nota: Cambiar el idioma mientras una sesión esté en curso regresará el juego al último nodo del guión."

    displayDict["es"].gamepad_caption = u"Opciones  > Mapeo del control de mando"
    displayDict["es"].gamepad_key_na = u"Sin asignar"
    displayDict["es"].gamepad_request_key = u"Presiona el botón que quieras asignar a “%s”.\nHaz clic con el ratón o el botón select para borrar el mapeo."

    displayDict["es"].yesno_yes = u"Sí"
    displayDict["es"].yesno_no = u"No"
    displayDict["es"].yesno_okay = u"Continuar"
    displayDict["es"].yesno_savesuccess = u"Progreso guardado con éxito."
    displayDict["es"].yesno_quit = u"¿Está seguro de querer\nsalir de Katawa Shoujo?"
    displayDict["es"].yesno_return_to_main = u"¿Está seguro de querer\nregresar al menú principal?"
    displayDict["es"].save_page_caption = u"Guardar"
    displayDict["es"].new_save_button = u"Crear nuevo estado"
    displayDict["es"].load_page_caption = u"Cargar"
    displayDict["es"].yesno_load_in_game = u"¿Está seguro de querer\ndesechar su progreso?"
    displayDict["es"].yesno_save_overwrite = u"¿Está seguro de querer\nsobrescribir su estado?"
    displayDict["es"].yesno_delete_savegame = u"¿Está seguro de querer\nborrar este estado?"
    displayDict["es"].play_time_label = u"Tiempo de juego"
    displayDict["es"].show_manual_saves = u"Manual"
    displayDict["es"].show_auto_saves = u"Auto"

    displayDict["es"].text_history_caption = u"Historial del texto"

    displayDict["es"].extra_menu_caption = "Extras"
    displayDict["es"].extra_music_button_label = "Rocola"
    displayDict["es"].extra_gallery_button_label = u"Galería"
    displayDict["es"].extra_scene_button_label = "Biblioteca"
    displayDict["es"].extra_omake_button_label = "Omake"
    displayDict["es"].extra_opening_button_label = "Cine"
    displayDict["es"].commentary_label = "Habilitar comentario"

    displayDict["es"].video_page_caption = "Extras > Cine"


    displayDict["es"].music_page_caption = "Extras > Rocola"
    displayDict["es"].music_stop_button_text = "Parar"
    displayDict["es"].music_now_playing = "Reproduciendo"

    displayDict["es"].gallery_page_caption = u"Extras > Galería"
    displayDict["es"].gallery_onelocked = u"Una imagen más no desbloqueada."
    displayDict["es"].gallery_manylocked = u"%d imágenes más no desbloqueadas."
    displayDict["es"].gallery_singlelocked = "Imagen %d de %d no desbloqueada."
    displayDict["es"].gallery_num_page_prefix = u"Página"
    displayDict["es"].gallery_num_page_error = u"No hay imágenes para mostrar"

    displayDict["es"].scene_page_caption = "Extras > Biblioteca"
    displayDict["es"].scene_completion_label = "Completado: %s%%"
    displayDict["es"].scene_playthrough_label = u"Usar flujo de repetición (recomendado)"
    displayDict["es"].scene_launch_path = u"¿Desea empezar\nel camino entero?"

    displayDict["es"].joy_left = u"Izquierda"
    displayDict["es"].joy_right = u"Derecha"
    displayDict["es"].joy_up = u"Arriba"
    displayDict["es"].joy_down = u"Abajo"
    displayDict["es"].joy_dismiss = u"Seleccionar/Avanzar"
    displayDict["es"].joy_rollback = u"Historial del texto"
    displayDict["es"].joy_holdskip = u"Mantener presionado para saltar"
    displayDict["es"].joy_toggleskip = u"Avance rápido"
    displayDict["es"].joy_hide = u"Mostrar imagen"
    displayDict["es"].joy_menu = u"Mostrar menú"



    displayDict["es"].name_hi = "Hisao"

    displayDict["es"].name_ha = "Hanako"
    displayDict["es"].name_emi = "Emi"
    displayDict["es"].name_rin = "Rin"
    displayDict["es"].name_li = "Lilly"
    displayDict["es"].name_shi = "Shizune"
    displayDict["es"].name_mi = "Misha"

    displayDict["es"].name_ke = "Kenji"
    displayDict["es"].name_mu = "Mutou"
    displayDict["es"].name_nk = "Enfermero"
    displayDict["es"].name_no = "Nomiya"
    displayDict["es"].name_yu = "Yuuko"
    displayDict["es"].name_sa = "Sae"
    displayDict["es"].name_aki = "Akira"
    displayDict["es"].name_hh = "Hideaki"
    displayDict["es"].name_hx = "Jigoro"
    displayDict["es"].name_emm = "Meiko"
    displayDict["es"].name_sk = "Tendero"
    displayDict["es"].name_mk = "Miki"

    displayDict["es"].name_mystery = u"¿¿??"

    displayDict["es"].name_ha_ = u"Chica de cabello púrpura"
    displayDict["es"].name_emi_ = "Chica de coletas"
    displayDict["es"].name_rin_ = u"Chica extraña"
    displayDict["es"].name_li_ = "Chica de cabello ondulado"
    displayDict["es"].name_mi_ = u"Chica risueña"
    displayDict["es"].name_ke_ = u"Compañero de anteojos"
    displayDict["es"].name_mu_ = "Hombre alto"
    displayDict["es"].name_yu_ = "Bibliotecaria"
    displayDict["es"].name_no_ = "Hombre de cabello plateado"
    displayDict["es"].name_sa_ = u"Galerista"
    displayDict["es"].name_aki_ = "Persona bien vestida"
    displayDict["es"].name_nk_ = "Hombre sonriente"
    displayDict["es"].name_hh_ = "Chica delgada"
    displayDict["es"].name_emm_ = "Mujer con trenza"
    displayDict["es"].name_hx_ = "Hombre enorme"

    displayDict["es"].videos = (("Apertura", "video/base_op_1.mp4"),
                                ("Emi", "video/base_tc_act2_emi.mp4"),
                                ("Hanako", "video/base_tc_act2_hanako.mp4"),
                                ("Lilly", "video/base_tc_act2_lilly.mp4"),
                                ("Rin", "video/base_tc_act2_rin.mp4"),
                                ("Shizune", "base_video/tc_act2_shizune.mp4"),
                               )

    if (renpy.ios):
        displayDict["es"].videos = (("Apertura", "video/ios_op_1.mp4"),
                                    ("Emi", "video/ios_tc_act2_emi.mp4"),
                                    ("Hanako", "video/ios_tc_act2_hanako.mp4"),
                                    ("Lilly", "video/ios_tc_act2_lilly.mp4"),
                                    ("Rin", "video/ios_tc_act2_rin.mp4"),
                                    ("Shizune", "video/ios_tc_act2_shizune.mp4"),
                                )





    displayDict["es"].s_scenes = ((u"Prólogo", rp_actmark, rp_actmark, ("Act 1","Prologue")),
                                    ("Congelado", "NOP1", u"En un día frío y nevado, los sueños de Hisao estaban a punto de hacerse realidad, sólo para ser interrumpidos por un repentino ataque cardiaco.", ("Act 1","Prologue")),
                                    ("Haz de Hisao", "NOP2", u"Le hablan a Hisao de la Academia Yamaku, donde probablemente pasará el resto de sus días de preparatoria.", ("Act 1","Prologue")),
                                    ("Acto 1: Esperanza de Vida", rp_actmark, rp_actmark, "Act 1"),
                                    (u"Comenzar es Fácil", "A1", "Hisao entra a la Academia Yamaku por primera vez, y conoce a su maestro de cabecera, Mutou.", "Act 1"),
                                    ("Entrada, Escenario a la Izquierda", "A2", u"Presentaciones al grupo, y un encuentro con la representante de grupo y su intérprete.", "Act 1"),
                                    (u"En la Enfermería", "A3", u"Misha y Shizune le muestran la cafetería a Hisao, tras lo cual va a ver al enfermero.", "Act 1"),
                                    (u"Habitación de Nadie", "A4", u"Hisao se muda a su nueva habitación, conociendo a Kenji, su compañero de pasillo, en el proceso.", "Act 1"),
                                    ("Charla", "A5", "Shizune y Misha le dicen a Hisao sobre el festival que se acerca y lo invitan a almorzar.", "Act 1"),
                                    ("El que No Arriesga, No Gana", "A6", "Shizune y Hisao combaten por el mundo en una partida de Risk.", "Act 1"),
                                    ("Seudoteteras", "A7", u"Buscando la biblioteca, Hisao se pierde y se encuentra con Lilly en un salón en desuso.", "Act 1"),
                                    ("Biblioteca Compartida", "A8", "Finalmente encontrando el camino a la biblioteca, Hisao se encuentra con Hanako y la espanta.", "Act 1"),
                                    (u"Extraño y Surrealista", "A9", "Kenji revela los oscuros secretos de Yamaku.", "Act 1"),
                                    (u"Teoría de la Evolución del Almuerzo", "A10", "Shizune y Misha fastidian a Hisao para que se una al consejo estudiantil antes de discutir sobre el almuerzo.", "Act 1"),
                                    ("Impacto Imprevisto", "A11_1", "Camino a almorzar junto con Misha y Shizune, Hisao choca con Emi en el pasillo.", "Act 1"),
                                    ("Adorable Encontronazo", "A11_2", "Hisao choca con una alborotada Emi en su camino a almorzar con Hanako y Lilly.", "Act 1"),
                                    (u"Desviación Más Adelante", "A12", u"Shizune y Misha llevan a Hisao a su casa de té favorita, el Shanghái.", "Act 1"),
                                    ("Sorbo (Parte 1)", "A13", "Hisao tiene un tranquilo almuerzo con Lilly y Hanako.", "Act 1"), 
                                    (u"Forma Carácter", "A15", "Mutou intenta tener una charla seria con Hisao, pero Misha interrumpe y pone a Hisao a trabajar.", "Act 1"),
                                    ("Un Almuerzo Privado", "A16", u"Hisao, en busca de suministros, se topa con una extraña chica en el salón de arte.", "Act 1"),
                                    ("Emboscada", "A17", "Mientras ayudaba a Rin cargando un poco de pintura, Hisao es interrogado por el enfermero.", "Act 1"),
                                    ("El Otro Verde", "A18", "Hisao mira a Rin pintar su mural.", "Act 1"),
                                    ("La Chica Corredora", "A19", "Al intentar hacer algo de ejercicio matutino, Hisao se encuentra con Emi en la pista de atletismo.", "Act 1"),
                                    (u"Jabón", "A20", "Kenji le tiende una emboscada a Hisao en la regadera en un intento de conseguir algo de dinero.", "Act 1"),
                                    (u"Guerra Fría", "A21", "Shizune y Lilly se enfrentan por solicitudes presupuestales.", "Act 1"),
                                    ("Prueba de Competencia", "A22", "Shizune y Misha asaltan a Hisao en un intento de hacer que se una al consejo estudiantil.", "Act 1"),
                                    ("Horizonte de Eventos", "A22_2", "Shizune y Misha asaltan a Hisao en un intento de hacer que se una al consejo estudiantil.", "Act 1"),
                                    (u"Por Encima y Más Allá", "A23_1", u"Hisao recibe una cátedra sobre los nobles deberes de un consejo estudiantil.", "Act 1"),
                                    ("Cosas que Puedes Hacer", "A23_2", u"Después de escapar de las garras de Shizune y Misha, Hisao le ayuda de nuevo a Rin.", "Act 1"),
                                    (u"Colorear con Números", "A24", "Hanako y Hisao le echan una mano al grupo de Lilly al ayudar voluntariamente a construir sus puestos.", "Act 1"),
                                    ("Ejercicio", "A25", u"En otra temprana mañana Hisao corre por la pista con Emi.", "Act 1"),
                                    ("Sombrero Invisible", "A26", u"Kenji le da a Hisao unos consejos de veterano acerca de cómo socializar.", "Act 1"),
                                    ("Ventaja de Campo Propio", "A26_1", u"Shizune y Misha secuestran a Hisao mientras salía de su habitación para ir a clase.", "Act 1"),
                                    (u"Sin Recuperación", "A27", False, "Act 1"), 
                                    (u"Lenta Recuperación", "A27_1", u"Recuperándose de sus palpitaciones del corazón, Hisao eventualmente llega a clase.", "Act 1"),
                                    (u"Sin Recuperación", "A27_2", u"Hisao lucha para llegar a clase después de su secuestro por el consejo estudiantil.", "Act 1"),
                                    ("El Almuerzo No Es Gratis", "A28", u"Hisao es escoltado al salón del consejo estudiantil para su primer día oficial ahí.", "Act 1"),
                                    ("Pie y Boca", "A29", "Emi arrastra a Hisao al tejado para almorzar con Rin.", "Act 1"),
                                    ("Cuidado Donde Pisas", "A30", u"Hisao y Lilly van de compras, encontrándose con una muy confundida Rin en el camino de regreso.", "Act 1"),
                                    ("Apoyo", "A31", u"Hisao tiene su primera lección del sábado, con todo y una plática con Mutou.", "Act 1"),
                                    (u"En Estética", "A32", u"Emi encuentra a Hisao holgazaneando después de clases y lo recluta para ayudarle a Rin una vez más.", "Act 1"),
                                    ("Dolor Creativo", "A33", "Hisao conoce al maestro de arte, Nomiya, mientras Rin pinta su mural.", "Act 1"),
                                    ("Ejercicio Saludable", "A34", "Emi y Hisao discuten la importancia de estar en forma.", "Act 1"),
                                    ("Sorbo (Parte 2)", "A35", "En un intento de matar el tiempo, Hisao va a dar una vuelta por la escuela.", "Act 1"),
                                    ("Enshanghaiado", "A36", u"Té, pastel y competencias con Shizune y Misha en el Shanghái.", "Act 1"),
                                    ("Silencioso", "A37", "Hanako y Hisao leen libros antes del festival.", "Act 1"),
                                    (u"No Entre en Pánico", "A38", u"Después de despertar el día del festival, Hisao es recibido por un desvariante Kenji.", "Act 1"),
                                    (u"¡Es Carnaval!", "A39", u"Emi atrapa a Hisao comiendo comida frita y lo hace acompañarla como castigo.", "Act 1"),
                                    ("Nc5xb3", "A42", "Incapaz de ayudar a Lilly en su puesto, Hisao busca a Hanako en el festival.", "Act 1"),
                                    ("Movimiento", "H2", u"Lilly termina sus deberes e invita a Hanako y a Hisao a una taza de té en el Shanghái.", "Act 1"), 
                                    ("Promesa de tiempo", "A41", u"Después de una difícil mañana en su puesto, Hisao lleva a Lilly para encontrar a Hanako.", "Act 1"),
                                    ("Nubes en mi Cabeza", "A40", u"Hisao le hace compañía a Rin y a su ahora terminado mural.", "Act 1"),
                                    ("Lanzando Pelotas", "A44", u"Fiel a su palabra, Hisao pasa el día con Shizune y Misha.", "Act 1"),
                                    ("Tocando Fondo", "A43", "Kenji y Hisao comparten un picnic de machos en la azotea en lugar de ir al festival.", "Act 1"),
                                    ("Acto 2: Forma", rp_actmark, rp_actmark, ("Act 2","Emi")),
                                    ("Carrera Matutina", "E3", "La primera de muchas carreras matutinas de Hisao con Emi.", ("Act 2","Emi")),
                                    ("Nubes, Viajes en el Tiempo, y Usted", "E4", "Otro almuerzo en la azotea con Emi y Rin. Emi extrae de Hisao una promesa de ir a verla en la competencia de atletismo.", ("Act 2","Emi")),
                                    (u"¡Preguntas que Necesitan Respuesta!", "E5", u"Una charla entre Emi y Hisao. Hisao le hace un par de preguntas más a Emi acerca de su relación con Rin.", ("Act 2","Emi")),
                                    ("La Segunda Vez es la Peor", "E6", "La segunda carrera matutina. Hisao es casi arrastrado gritando y pateando por la pista.", ("Act 2","Emi")),
                                    (u"Una Manzana al Día", "E7", "Hisao va a visitar al enfermero junto con Emi y se encuentra con que los dos se han conocido desde hace tiempo.", ("Act 2","Emi")),
                                    ("Competencia de Atletismo", "E8", u"El día de la competencia de atletismo. Otra faceta de la personalidad de Emi es revelada.", ("Act 2","Emi")),
                                    (u"Tómate Esa Medicina Ya", "E9", u"Hisao menciona un dolor en su pecho durante una visita al enfermero y recibe una lección.", ("Act 2","Emi")),
                                    (u"Piratería en los Altos Mares", "E10", u"Hisao discute de su futuro como pirata con Emi en la azotea, después una carta de Iwanako arruina su día.", ("Act 2","Emi")),
                                    (u"Últimas Palabras Célebres", "E11", "Emi y Rin llevan a Hisao de picnic, pronto arruinado por la lluvia.", ("Act 2","Emi")),
                                    (u"Siguiéndole la Pista a las Ausencias", "E12", u"Hisao va a la pista como es usual, pero Emi no está.", ("Act 2","Emi")),
                                    ("Visitando", "E13", "Una visita a una Emi enferma, la cual pronto cambia a algo completamente distinto.", ("Act 2","Emi")),
                                    (u"La Primera Mañana del Día Siguiente", "E14", u"Hisao rememora la última noche y decide hacer algo por Emi.", ("Act 2","Emi")),
                                    ("El (Verdadero) Comienzo", "E15", "Otra hora del almuerzo en la azotea, sin Rin.", ("Act 2","Emi")),
                                    ("Acto 3: Perspectiva", rp_actmark, rp_actmark, ("Act 3","Emi")),
                                    (u"Ezto Ezz… Scienca", "E16", u"Mutou jala a Hisao a una corta discusión acerca de su futuro.", ("Act 3","Emi")),
                                    ("Definiciones", "E17", u"Emi y Hisao intentan otro picnic, esta vez sin intervención alguna de la Madre Naturaleza.", ("Act 3","Emi")),
                                    ("Roca Invisible", "E18", u"De vuelta en la pista en la mañana, con todo como es habitual… o eso parece.", ("Act 3","Emi")),
                                    ("Almuerzo y Ciencia", "E19", "Hisao visita de nuevo a Mutou para hablar de su futuro en las ciencias.", ("Act 3","Emi")),
                                    ("Arriba, Abajo, y Arriba Otra Vez", "E20", u"Una frenética llamada de Emi lleva a Hisao a su habitación, donde dos sorpresas lo esperan.", ("Act 3","Emi")),
                                    ("Espacio de Almacenaje", "E21", "Emi persuade a Hisao de entrar al cobertizo de la pista.", ("Act 3","Emi")),
                                    ("Planes Posescuela", "E22", u"Emi tiene una plática seria con Hisao acerca de los exámenes próximos.", ("Act 3","Emi")),
                                    ("Desapegada", "E23", u"Hisao medita melancólicamente acerca de su relación con Emi.", ("Act 3","Emi")), 
                                    ("Dolor Fantasma", "E24", u"El intento de Hisao de mostrarle a Emi su preocupación no sale tan bien como lo esperaba.", ("Act 3","Emi")),
                                    ("El Debate Expresa Duda", "E25", u"Hisao está confundido por el comportamiento de Emi y por una invitación a su casa.", ("Act 3","Emi")),
                                    (u"Adivina Quién Viene… No Importa", "E26", "Cena con la familia Ibarazaki.", ("Act 3","Emi")),
                                    (u"Repetición Instantánea", "E27", u"Las cosas finalmente llegan a un punto crítico en la pista.", ("Act 3","Emi")),
                                    ("Acto 4: Movimiento", rp_actmark, rp_actmark, ("Act 4","Emi")),
                                    ("Abanicar y Fallar", "E28", "Hisao se pregunta si Emi lo evade intencionalmente.", ("Act 4","Emi")),
                                    (u"Tirada de Salvación", "E29", u"Las cosas finalmente llegan a un punto crítico en la azotea.", ("Act 4","Emi")),
                                    ("Susurros del Pasado", "E30", u"Hisao, Emi y su mamá van a visitar una tumba.", ("Act 4","Emi")),
                                    ("Hurra por los Calcetines", "E31", "Sexo, drogas, pero no rock and roll.", ("Act 4","Emi")),
                                    ("Dientes Limpios", "E32", "Hisao despierta y se encuentra a Emi durmiendo a su lado.", ("Act 4","Emi")),
                                    ("Acto 2: Las Escondidas", rp_actmark, rp_actmark, ("Act 2","Hanako")),
                                    ("Al Pueblo, Al Pueblo", "H3", u"Un viaje de compras al minisúper con Hanako.", ("Act 2","Hanako")),
                                    (u"Hojas De Té", "H4", "Hanako invita a Hisao a almorzar con ella y Lilly.", ("Act 2","Hanako")),
                                    ("Confesionario De Oficina", "H5_1", u"Hisao y Misha discuten la situación de Hanako.", ("Act 2","Hanako")),
                                    ("Ajedrez y Toboganes", "H5_2", "Hisao deja plantado al consejo estudiantil para leer con Hanako.", ("Act 2","Hanako")),
                                    (u"Levántate y Brilla", "H6", u"Una invitación de Lilly a una fiesta de té a altas horas.", ("Act 2","Hanako")),
                                    ("Sombrerero Loco", "H7", u"Hanako, Hisao y Lilly se reúnen para una fiesta de té en la habitación de Lilly.", ("Act 2","Hanako")),
                                    ("Poco Cambio", "H8", u"Kenji es forzado a pagar su préstamo.", ("Act 2","Hanako")),
                                    ("Ausentismo", "H9", "Hisao y Lilly discuten la asistencia de Hanako a la escuela.", ("Act 2","Hanako")),
                                    ("Intercambio Equivalente", "H10", u"A cambio de aprender sobre su corazón, Hanako revela parte de su pasado a Hisao.", ("Act 2","Hanako")),
                                    ("Acto 3: Enroque", rp_actmark, rp_actmark, ("Act 3","Hanako")),
                                    (u"Invitación", "H11", u"Lilly encuentra a Hisao limpiando el cuarto de té y le habla sobre el cumpleaños de Hanako.", ("Act 3","Hanako")),
                                    ("Encuentro Turbio", "H12", "Una charla inesperada con Miki mientras rememora el pasado.", ("Act 3","Hanako")),
                                    (u"Antigüedades y Tarta", "H13", "Lilly y Hisao van de compras por un regalo a la ciudad.", ("Act 3","Hanako")),
                                    ("Cayendo", "H14", u"Hanako tiene un ataque de pánico durante la clase.", ("Act 3","Hanako")),
                                    ("Andando Con Cuidado", "H15", "Lilly tiene malas noticias que discutir con Hisao y Hanako.", ("Act 3","Hanako")),
                                    (u"Aproximándose", "H16", u"Hisao se acerca a una retraída Hanako.", ("Act 3","Hanako")),
                                    (u"Un Año Más", "H17", u"Se une a nuestro trío un invitado inesperado mientras celebran la fiesta de cumpleaños de Hanako.", ("Act 3","Hanako")),
                                    ("Un Pedazo De Papel", "H18", u"Hisao disfruta su primera resaca antes de recibir una carta problemática.", ("Act 3","Hanako")),
                                    (u"Sólidas y Rayadas", "H19", u"Una charla de corazón a corazón durante un juego de billar.", ("Act 3","Hanako")),
                                    ("Comienzo Del Fin", "H20", "La partida de Lilly a su viaje.", ("Act 3","Hanako")),
                                    ("Acto 4: Cicatrices", rp_actmark, rp_actmark, ("Act 4","Hanako")),
                                    ("Absentismo Escolar", "H21", u"Almuerzo con el consejo estudiantil y preocupación sobre Hanako encerrándose.", ("Act 4","Hanako")),
                                    ("Presencia Remota", "H22", u"Hisao llama a Lilly para pedir consejo después de que Hanako se aisla por otro día.", ("Act 4","Hanako")),
                                    ("Paso En Falso", "H23", u"Hisao trata de sacar a Hanako de su habitación, con resultados inesperados.", ("Act 4","Hanako")),
                                    (u"Cortar Pétalos", "H24", u"Hisao encuentra su relación con Hanako terminada prematuramente.", ("Act 4","Hanako")),
                                    (u"La Melodía Continúa", "H25", "Hanako regresa a clase, para alivio de Hisao.", ("Act 4","Hanako")),
                                    (u"Aplicación en el Shanghái", "H26", u"Buscando evitar distracciones, Hisao trata de estudiar en el Shanghái.", ("Act 4","Hanako")),
                                    ("Su Pasado", "H27", u"En un intento de acercarse más a Hanako, Hisao comparte parte de su pasado con ella.", ("Act 4","Hanako")),
                                    ("Encuentro Citadino", "H28", "Ambos comparten una cita en la ciudad.", ("Act 4","Hanako")),
                                    ("Contacto Susurrado", "H29", "Hisao y Hanako pasan la noche juntos.", ("Act 4","Hanako")),
                                    ("Futuro Indeterminado", "H30", "Los eventos de la noche previa pesan bastante en Hisao.", ("Act 4","Hanako")),
                                    ("Edad Adulta", "H31", u"El final de dos niños, el comienzo de dos adultos.", ("Act 4","Hanako")),
                                    ("Acto 2: Pasado", rp_actmark, rp_actmark, ("Act 2","Lilly")),
                                    ("Earl Grey", "L1", u"Hisao comparte el primero de muchos almuerzos con Hanako y Lilly mientras se recupera del día anterior.", ("Act 2","Lilly")),
                                    ("Una Libra Esterlina", "L2", u"Interrogado por Kenji acerca de la nacionalidad de Lilly, Hisao decide investigar y encuentra muchas más cosas.", ("Act 2","Lilly")),
                                    ("Presentes y Presencia", "L3", u"Durante la búsqueda por el regalo para Hanako, Lilly y Hisao se encuentran a Akira y a su primo.", ("Act 2","Lilly")),
                                    ("Objeto para Beber No Identificado", "L4", u"El trío celebra el cumpleaños de Hanako y es interrumpido por una hermana.", ("Act 2","Lilly")),
                                    (u"El Día Después", "L5", "Hisao y Lilly despiertan e intentan recuperarse de los eventos de la noche anterior.", ("Act 2","Lilly")),
                                    ("Breve Historia del Tomillo", "L6", "Hisao y Lilly van a comprar comida.", ("Act 2","Lilly")),
                                    (u"Pequeña Ala", "L7", u"Mientras comparten el almuerzo en la azotea, la situación toma un giro desafortunado.", ("Act 2","Lilly")),
                                    ("Bon Voyage", "L8", "Se despiden de Lilly y Akira cuando ellas se van de viaje para visitar a su familia en Escocia.", ("Act 2","Lilly")),
                                    ("Acto 3: Presente", rp_actmark, rp_actmark, ("Act 3","Lilly")),
                                    (u"Día a Día", "L9", u"Hisao deja pasar ociosamente un día sin Lilly al tener una plática con Mutou acerca de Yamaku.", ("Act 3","Lilly")),
                                    ("Discordia Menor", "L10", "Hisao almuerza con Kenji, luego le entrega unas notas a una alarmantemente silenciosa Hanako.", ("Act 3","Lilly")),
                                    ("Disonancia", "L11", u"Con Hanako encerrada en sí misma por completo, Hisao le ofrece lo poco de ayuda que puede antes de llamar a Lilly.", ("Act 3","Lilly")),
                                    ("Un Mundo Aparte", "L12", u"La mente tranquila de Hisao comienza a preguntarse acerca de su relación con Lilly.", ("Act 3","Lilly")),
                                    (u"Renovación", "L13", u"Hisao, Hanako, y Hideaki les dan la bienvenida a Akira y a Lilly después de su regreso de Escocia.", ("Act 3","Lilly")),
                                    (u"Estadía Norteña", "L14", u"El trío comienza sus vacaciones en Hokkaido.", ("Act 3","Lilly")),
                                    ("Preludio", "L15", "Una caminata matutina comienza una cadena de eventos.", ("Act 3","Lilly")),
                                    ("Crescendo", "L16", "Los verdaderos sentimientos de Lilly son dichos en el dorado interminable de los campos de trigo." , ("Act 3","Lilly")),
                                    ("Diminuendo", "L17", "Nuestra pareja comparte su primera noche juntos.", ("Act 3","Lilly")),
                                    ("Panorama Gris", "L18", u"Confinados en una casa de verano, Lilly y Hisao son forzados a aceptar su relación.", ("Act 3","Lilly")),
                                    ("Rapsodia en Azul", "L19", u"Un baño durante el que Hisao reflexiona sobre dónde están él y Lilly en la vida, hasta que alguien se le une.", ("Act 3","Lilly")),
                                    (u"El Presente Momentáneo", "L20", "Al viajar de vuelta a Yamaku, Hisao y Lilly charlan entre ellos.", ("Act 3","Lilly")),
                                    ("Acto 4: Futuro", rp_actmark, rp_actmark, ("Act 4","Lilly")),
                                    ("Pasos Lentos Antes de un Vals", "L21", "De vuelta en la escuela, lo sucedido en Hokkaido viene al frente.", ("Act 4","Lilly")),
                                    ("Ropas de Dormir y Trajes", "L22", u"Asentándose de nuevo en la vida diaria. Akira se le une al trío durante una de sus fiestas de té.", ("Act 4","Lilly")),
                                    ("Procedimiento Correcto", "L23", "Hisao y Lilly arreglan una cita antes de que Akira llegue.", ("Act 4","Lilly")),
                                    (u"Un Día Fuera", "L24", "Hisao y Lilly van a su primera cita y averiguan acerca de sus pasados.", ("Act 4","Lilly")),
                                    (u"Un Ensueño de Mañana", "L25", "Hisao y Lilly discuten sobre sus ambiciones para el futuro.", ("Act 4","Lilly")),
                                    (u"Apagón", "L26", u"El trío reflexiona acerca de las vacaciones próximas antes de que Hisao experimente la visión como la de Lilly.", ("Act 4","Lilly")),
                                    ("Contexto", "L27", "Hisao recibe una llamada de Akira y los dos hablan acerca de su hermana.", ("Act 4","Lilly")),
                                    ("Un Futuro Lejano", "L28", u"Lilly le revela a Hisao la oferta de su familia de unírseles en Escocia.", ("Act 4","Lilly")),
                                    ("Despedida", "L29", u"Despedidas de Akira y Lilly la noche anterior de que dejen Japón.", ("Act 4","Lilly")),
                                    ("Falsa Cadencia", "L30", u"Hisao se apresura para confrontar a Lilly, percatándose de su conflicto.", ("Act 4","Lilly")),
                                    ("Debajo de un Sensiblero Cielo", "L31", "Caminando por el ala del hospital, Hisao lucha por aceptar su vida.", ("Act 4","Lilly")),
                                    ("Debajo de un Brillante Cielo", "L32", u"Lilly se reúne con Hisao y los dos comienzan de nuevo su vida juntos.", ("Act 4","Lilly")),
                                    (u"¡Hacia Adelante, con Entusiasmo!", "L33", "Lilly y Hisao se despiden de Akira.", ("Act 4","Lilly")),
                                    (u"Acto 2: Desconexión", rp_actmark, rp_actmark, ("Act 2","Rin")),
                                    (u"Un Campo de Visión Más Amplio", "R1", "Hisao pasa la hora del almuerzo con Rin viendo las nubes en la azotea.", ("Act 2","Rin")),
                                    ("Estudios en Escala de Grises", "R2", u"Rin y Hisao dibujan retratos el uno del otro en su primera reunión en el club de arte.", ("Act 2","Rin")),
                                    ("Intersticial", "R3", "Kenji le presta a Hisao un libro “procurado” de la biblioteca.", ("Act 2","Rin")),
                                    (u"Autoevaluación", "R4", "Misha y Shizune pescan a Hisao garabateando meditabundo durante la clase.", ("Act 2","Rin")),
                                    ("La Sonrisa de Hisao", "R5", u"Rin le habla a Hisao de sus expresiones de alegría, o falta de ellas.", ("Act 2","Rin")),
                                    ("Cosas que te Gustan", "R6", "Breves reflexiones con Yuuko sobre libros y Yamaku.", ("Act 2","Rin")),
                                    (u"Público Meta", "R7", u"El día de la competencia de atletismo. Facetas de Emi y personalidades de Rin son reveladas.", ("Act 2","Rin")),
                                    ("La Eternidad En Una Hora", "R8", u"Nomiya incita a la discusión del arte durante una reunión del club.", ("Act 2","Rin")),
                                    ("Bajo el Agua y un Arce con Nombre", "R9", "Rin lleva a Hisao al bosque, donde reflexionan sobre su futuro inmediato.", ("Act 2","Rin")),
                                    ("El Arrepentimiento de Iwanako", "R10", "Llega una carta de Iwanako.", ("Act 2","Rin")),
                                    ("En Su Propia Imagen", "R11", u"Hisao empuja a Rin a tener su propia exhibición de arte.", ("Act 2","Rin")),
                                    (u"Pastel de Lógica del Paraguas", "R12", u"Les llueve encima a Emi, Hisao y Rin y buscan refugio en el Shanghái.", ("Act 2","Rin")),
                                    (u"Seis Metros Más Cerca del Cielo", "R13", "Rin y Hisao NO almuerzan en la azotea, debido a una distintiva falta de Emi.", ("Act 2","Rin")),
                                    (u"Indecisión", "R14", "Emi se cura de su resfriado, mientras que Rin pesca el suyo.", ("Act 2","Rin")),
                                    (u"Interferencia de Señales", "R15", u"Hisao va a visitar a Rin en su habitación.", ("Act 2","Rin")),
                                    (u"Dientes de León", "R16", "Se llega a conclusiones en la cima de una colina.", ("Act 2","Rin")),
                                    ("Acto 3: Distancia", rp_actmark, rp_actmark, ("Act 3","Rin")),
                                    ("22a Esquina", "R17", u"El equipo del club de arte revisa la galería para la futura exhibición de Rin.", ("Act 3","Rin")),
                                    ("El Aroma de la Luz", "R18", u"Hisao se topa con una durmiente Rin en el salón de arte.", ("Act 3","Rin")),
                                    ("Cosas a las Que No Puedes Renunciar", "R19", "Emi y Hisao discuten la personalidad de Rin.", ("Act 3","Rin")),
                                    (u"¡BADAAN!", "R20", u"Los pensamientos de Yuuko sobre la motivación.", ("Act 3","Rin")),
                                    ("Anteojos Color de Rosa", "R21", "Nomiya habla en detalle sobre el arte como carrera.", ("Act 3","Rin")),
                                    ("El Borde del Mundo", "R22", u"Hisao se le confiesa a Rin y es rechazado. ¿O no?", ("Act 3","Rin")),
                                    ("El contexto de Rin", "R23", u"Una incómoda y silenciosa tarde en el taller.", ("Act 3","Rin")),
                                    (u"Tiempo Después", "R23_2", u"Las preparaciones para la exhibición se asientan en una extraña rutina.", ("Act 3","Rin")),
                                    (u"Autodestrucción", "R24", "Rin experimenta fumando un cigarrillo para obtener una mirada fresca de la creatividad.", ("Act 3","Rin")),
                                    ("Escapismo Inverso", "R25", "Hisao lleva a Rin a un paseo por las calles nocturnas.", ("Act 3","Rin")),
                                    ("Sin Fronteras", "R26", u"Sae y Nomiya le dan a Hisao un poco de información de la vida de los artistas.", ("Act 3","Rin")),
                                    ("Delirio", "R27", "Hisao sorprende a una desesperada Rin en el taller.", ("Act 3","Rin")),
                                    ("Cosas que Odias", "R28", u"Desagradables consecuencias de una noche increíble.", ("Act 3","Rin")),
                                    ("Fragmentos de Ira", "R29", u"La tensa relación entre los dos estalla.", ("Act 3","Rin")),
                                    (u"Acto 4: Sueño", rp_actmark, rp_actmark, ("Act 4","Rin")),
                                    ("Ilusiones para la Gente", "R30", u"Hisao habla de sus recelos con Nomiya, con poco éxito.", ("Act 4","Rin")),
                                    (u"Hastío", "R31", "La paciencia de Hisao llega a su fin.", ("Act 4","Rin")),
                                    ("La Escena", "R32", u"Reunión con Rin en la apertura de su exhibición.", ("Act 4","Rin")), 
                                    ("Longitud de Onda", "R35", u"Hisao deja pasar el tiempo letárgicamente en el último día de exámenes.", ("Act 4","Rin")),
                                    ("Periodo Azul", "R36", u"Un día lluvioso, la 22a Esquina, y una breve historia de Picasso.", ("Act 4","Rin")),
                                    (u"El Mundo Que Solo Tú Puedes Ver", "R37", u"Rin y Hisao parten después de la lluvia.", ("Act 4","Rin")),
                                    ("Gloria Desesperada", "R34", u"Un frenético Nomiya cuestiona a Hisao sobre el paradero de Rin.", ("Act 4","Rin")), 
                                    (u"Problemas de la Lógica Autorreferencial", "R38", "Hisao encuentra a Rin en su escondite, y la convence de reconciliarse con Nomiya.", ("Act 4","Rin")),
                                    ("Midiendo Sombras", "R39", "La disculpa de Rin al maestro de arte no es bien recibida.", ("Act 4","Rin")),
                                    (u"Raison d'être", "R40", "Hisao reconforta a una alterada Rin.", ("Act 4","Rin")),
                                    ("Sin Respirar, Sin un Sonido", "R41", u"En el primer día de las vacaciones de verano, Rin viene a la habitación de Hisao.", ("Act 4","Rin")),
                                    ("Prueba de Existencia", "R42", u"Todo confluye en la cima de aquella colina cubierta de dientes de león.", ("Act 4","Rin")),
                                    ("Acto 2: Aprendiendo a Leer", rp_actmark, rp_actmark, ("Act 2","Shizune")),
                                    ("Pasando Mensajes", "S8", u"Shizune y Hisao exploran métodos de comunicación.", ("Act 2","Shizune")),
                                    ("Habla con la Mano", "S9", "Hisao comienza a estudiar un nuevo idioma, y una tutora aparece.", ("Act 2","Shizune")),
                                    (u"Teléfono Descompuesto", "S10", "Kenji logra forzar a Hisao a que le haga un favor, pero Hisao se mete en problemas en muchos sentidos.", ("Act 2","Shizune")),
                                    (u"Teoría de Juegos Avanzada", "S11", u"RISK ya no es suficiente para saciar el hambre de Shizune. Lo que es peor, una nueva oponente hace su aparición.", ("Act 2","Shizune")),
                                    ("Pan, Tijeras y Papel", "S12", u"Una tarde tranquila se vuelve dramática cuando de repente un pedazo de pan se convierte en un objeto de gran interés.", ("Act 2","Shizune")),
                                    (u"Interacción", "S13", u"Shizune y Hisao encuentran una conexión.", ("Act 2","Shizune")),
                                    (u"Entrar en Acción", "S14", "Hisao tiene que mediar entre Lilly y Shizune, pero afortunadamente las cosas salen bien al final.", ("Act 2","Shizune")),
                                    ("Pasado Imperfectivo", "S15", u"El consejo estudiantil rememora sobre los años anteriores mientras se relaja en el Shanghái.", ("Act 2","Shizune")),
                                    ("Cuando las Estrellas se Abrazan", "S16", u"¡Finalmente es hora de Tanabata!", ("Act 2","Shizune")),
                                    (u"Acto 3: Prestidigitación", rp_actmark, rp_actmark, ("Act 3","Shizune")),
                                    (u"Retroalimentación de Fuerza", "S17", u"Hisao descubre que Shizune va a visitar a su familia, y se las arregla para acompañarla.", ("Act 3","Shizune")),
                                    ("Naciones Unidas", "S18", "El viaje a la casa de Shizune, conocer a su hermano menor, y un repentino concurso de pesca.", ("Act 3","Shizune")),
                                    (u"Distinción Uso-Mención", "S19", u"Hideaki intenta entretener a Hisao por un día, teniendo poco éxito.", ("Act 3","Shizune")),
                                    ("Trama Familiar", "S20", u"Nuestro trío conoce al padre de Shizune e inmediatamente echa a correr.", ("Act 3","Shizune")),
                                    (u"Ventana Pangramática", "S21", u"Una solicitud de Hideaki para aprender lenguaje de señas inesperadamente se convierte en una competencia de gritos con Jigoro.", ("Act 3","Shizune")),
                                    (u"Más Cerca", "S22", "Shizune y Hisao se unen por primera vez.", ("Act 3","Shizune")),
                                    (u"Confrontación", "S23", u"Jigoro menosprecia al consejo estudiantil y Hisao se alza ante el desafío.", ("Act 3","Shizune")),
                                    ("El Ancla", "S24", u"De vuelta a Yamaku. Una carta de Iwanako da pie a una larga discusión de Kenji sobre los puntos más sutiles de las novias.", ("Act 3","Shizune")),
                                    ("Hoja de Ruta", "S25", "El consejo estudiantil se preocupa por su reemplazo, y Hisao de alguna manera termina invitando a Misha a un parfait.", ("Act 3","Shizune")), 
                                    (u"Triángulo Agudo", "S26", "Una tarde de trabajo con Shizune le muestra a Hisao que algo anda mal entre las chicas.", ("Act 3","Shizune")),
                                    ("Dewey Diezmado", "S27", u"Yuuko consigue que Hisao cuide la biblioteca por ella. La llegada de Kenji hace que el intento tenga un relativo éxito.", ("Act 3","Shizune")),
                                    ("Labios Sellados", "S28", u"Misha visita a Hisao en su habitación, y las cosas van en una dirección inesperada.", ("Act 3","Shizune")),
                                    ("Mirando a un Lado", "S29_1", u"Hisao encuentra a una deprimida Misha en el techo. Él termina juntándola con Shizune.", ("Act 3","Shizune")),
                                    ("Mirando Adelante", "S29_2", "Hisao encuentra a una deprimida Misha en el techo. Shizune se les une y pone a todo el consejo de vuelta a trabajar.", ("Act 3","Shizune")),
                                    ("Acto 4: A Mi Otro Yo", rp_actmark, rp_actmark, ("Act 4","Shizune")),
                                    ("Gran Estrategia", "S30", "Shizune le confiesa a Hisao algunas de sus metas y fracasos.", ("Act 4","Shizune")),
                                    (u"Por Un Dígito", "S31", "Un intento fallido de animar a Misha se convierte en una cita improvisada para Hisao y Shizune.", ("Act 4","Shizune")),
                                    (u"Invasión", "S32", "Jigoro y Hideaki le hacen a Shizune una visita inesperada y de alguna manera desagradable.", ("Act 4","Shizune")),
                                    ("Parfait", "S33", "Hisao y Shizune siguen a Misha. Hisao finalmente logra arrinconarla y discutir las cosas apropiadamente.", ("Act 4","Shizune")),
                                    ("Tiempo Presente", "S38", "Hisao se encuentra con Lilly en el almuerzo, y los dos hablan de Shizune.", ("Act 4","Shizune")), 
                                    ("Espiral", "S39", "Evasivas, obstrucciones, y una emboscada nocturna de Kenji.", ("Act 4","Shizune")),
                                    ("Terminal", "S40", u"Una charla con Shizune temprano en la mañana en la silenciosa escuela.", ("Act 4","Shizune")),
                                    ("La Cumbre", "S34", u"Kenji y Shizune se encuentran en la habitación de Hisao. Milagrosamente, nada explota.", ("Act 4","Shizune")), 
                                    (u"Sucesión", "S35", "El actual consejo estudiantil prepara a sus sucesores antes de participar en “actividades extracurriculares”.", ("Act 4","Shizune")),
                                    (u"Misión Furtiva", "S36", u"La muestra de determinación de Misha anima a Shizune a poner su mira en cosas más grandes.", ("Act 4","Shizune")),
                                    ("Infinito", "S37", u"Nuestro trío renueva su amistad, con su inminente graduación aproximándose.", ("Act 4","Shizune")),
                                    )



    displayDict["es"].creditstring = u"""{image=ui/flourish_left.png} {b}Escrito por{/b} {image=ui/flourish_right.png}
Anonymous22
Aura
cpl_crud
Suriko
TheHivemind

{image=ui/flourish_left.png} {b}Edición{/b} {image=ui/flourish_right.png}
Kagami
Losstarot
Silentcook

{image=ui/flourish_left.png} {b}Música{/b} {image=ui/flourish_right.png}
Blue123
NicolArmarfi

{image=ui/flourish_left.png} {b}Arte{/b} {image=ui/flourish_right.png}
gebyy-terar
Kamifish
moekki
pimmy
raemz
Raide

{image=ui/flourish_left.png} {b}Arte Adicional{/b} {image=ui/flourish_right.png}
climatic
Doomfest
yujovi

{image=ui/flourish_left.png} {b}Animación FMV{/b} {image=ui/flourish_right.png}
Mike Inel

{image=ui/flourish_left.png} {b}Dirección{/b} {image=ui/flourish_right.png}
delta
Raide
yujovi

{image=ui/flourish_left.png} {b}Ingeniería{/b} {image=ui/flourish_right.png}
delta

{image=ui/flourish_left.png} {b}Producción{/b} {image=ui/flourish_right.png}
cpl_crud
Suriko


{image=ui/flourish_left.png} {b}Agradecimientos{/b} {image=ui/flourish_right.png}
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

{image=ui/flourish_left.png} {b}Agradecimientos Especiales{/b} {image=ui/flourish_right.png}
hir
PyTom
RAITA
replicated


{image=ui/flourish_center.png}


{image=ui/flourish_left.png} {b}Traducción al español latinoamericano{/b} {image=ui/flourish_right.png}
abscess - Rin, Acto 1
forseti - Hanako, Acto 1
Carlithium - Shizune
Alkhaz - Emi
MrA, Brooke - Lilly
rockprogrelatino - Corrección
promolic1 - Corrección
wolf224 - Control de calidad
Shocku - Control de calidad
lead - Control de calidad

{image=ui/flourish_left.png} {b}Agradecimientos{/b} {image=ui/flourish_right.png}
Aoiichi
ClexSipsoxard
coldacid
DuaneMoody
Fink
Juno
Kuranyll
Lawls
Naba
Pato
Shiz
SilverWings
Vbro
Zahlman"""


    displayDict["es"].drugs_wordlist  =  ["Disopiramida",
                        "Warfarina",
                        "Diltiazem",
                        "Felodipina",
                        "Propranolol",
                        "Penbutolol",
                        "Carteolol",
                        "Procainamida",
                        "Heparina",
                        u"Fenitoína",
                        "Verapamilo",
                        "Quinidina",
                        "Flecainida",
                        u"5mg/día",
                        u"400mg/día",
                        u"15ml/día",
                        u"100mg/día",
                        "10ml/48hrs",
                        u"10ml/día",
                        "200mg/12hrs",
                        "50mg/12hrs",
                        "500mg/48hrs",
                        "125mg/12hrs",
                        u"25ml/día",
                        "pesadillas",
                        u"disminución de la concentración",
                        "bradicardia",
                        u"depresión clínica",
                        "insomnio",
                        u"disfunción eréctil",
                        u"visión anormal",
                        "insuficiencia cardiaca",
                        u"náusea",
                        "mareo",
                        "alucinaciones",
                        "broncoespasmo",
                        "disnea",
                        "fatiga",
                        u"hipotensión",
                        "bloqueo cardiaco",
                        u"extremidades frías",
                        "diarrea",
                        "paro cardiaco",
                        u"fibrilación ventricular",
                        "ataxia",
                        "asma"]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
