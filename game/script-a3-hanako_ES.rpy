label es_H11:

scene bg school_miyagi_ss
show hanako basic_distant_close_ss at center
with locationchange

"El color de la habitación lentamente cambia del brillo de la tarde al anaranjado del crepúsculo. Un reloj pasa lentamente los segundos, contando en el fondo, en el límite de la audición."

"Pero no importa cuánto espere, el resultado no puede ser cambiado."

"La diminuta pieza de ajedrez en juego hace un ligero sonido contra el tablero."

show hanako basic_normal_close_ss
with charachange

"Como un resorte comprimido, Hanako hace su movimiento apenas momentos después del mío."

"Es embarazoso. En comparación a mis movimientos de cinco minutos, ella parece saber exactamente lo que quiere hacer."

show hanako basic_smile_close_ss
with charachange

play music music_tranquil fadein 3.0

ha "Mate."

hi "Otra vez… ¿Cuánto es con este? ¿3-2?"

show hanako cover_bashful_close_ss
with charachange

ha "E-empates no cuentan."

hi "Maldición. Te estás volviendo mejor en esto cada día."

"Eso, o se había estado conteniendo. Nunca habría imaginado algo como eso cuando le hablé por primera vez, pero en verdad tiene habilidad para este juego."

"El ajedrez parece haberse vuelto un pasatiempo popular para ambos; escondiéndonos en el cuarto de té, jugando uno o dos juegos después de clases."

"Desde aquí, los estudiantes afuera apenas pueden escucharse aglomerándose. Los ruidos cotidianos de abajo me recuerdan un poco a mi vida antes de Yamaku, aunque estoy ya bastante consciente de que es una vida a la que nunca volveré."

hi "¿Gustas jugar otra vez?"

show hanako basic_worry_close_ss
with charachange

ha "Te… tengo que terminar mi tarea…"

hi "Oh. Bueno, te veré mañana entonces."

show hanako basic_distant_close_ss
with charachange

ha "Pero… qué hay de esto…"

"Hanako señala el juego de té cerca del casi vacío tablero de ajedrez."

hi "No te preocupes por eso, yo me encargaré."

show hanako basic_normal_close_ss
with charachange

ha "Oh… está bien…"

show hanako basic_bashful_close_ss
with charachange

ha "N-nos vemos."

hi "Hasta luego."

hide hanako
with charaexit

"Hanako parte mientras comienzo a limpiar el área."

"Los ocasionales silbidos y porras del club de deportes afuera se vuelven menos frecuentes, alcanzando eventualmente el silencio."

"Una parte de mí aún quiere estar en alguna clase de equipo. Dado que jugué futbol y otros deportes antes de mi accidente, supongo que tan solo es normal sentir nostalgia sobre lo que ya no puedo hacer."

"Pero tengo otras razones para venir aquí tan seguido, y no me siento tan mal por perder esa parte de mí gracias a ellas. Lilly es ya una buena amiga, pero son los pequeños intercambios que tengo con Hanako lo que se siente especialmente bien."

"Las pequeñas victorias que siento cada día al ver más de lo que hay bajo su autoimpuesto caparazón. Ese es el porqué vengo aquí más que nada."

"Mientras estoy guardando tazas y salseras, escucho voces fuera de la puerta. Deteniéndome por un momento para escuchar, puedo darme cuenta de que son Hanako y Lilly, y decido ir afuera para investigar."

scene bg school_hallway2
show lilly basic_weaksmile at twoleft
show hanako emb_downtimid at tworight
with locationchange

li "¿Estás segura?"

ha "Estoy… segura…"

show hanako emb_timid
with charachange

ha "Ah, Hisao."

"Hanako voltea a verme con mirada de sorpresa al notar que me acerco. Lilly debe haberla encontrado justo cuando estaba por irse."

show lilly basic_smile
with charachange

li "Oh vaya, ¿Hisao está aquí también?"

hi "Buenas tardes, Lilly. ¿Qué pasa?"

show lilly basic_smileclosed
with charachange

li "Esperaba, ahora que he terminado por este día con mis tareas de representante de la clase, que podría contar con ambos para acompañarme para el té al Shanghái. Sería bueno disfrutar de un tiempo juntos fuera de la escuela, para variar."

hi "Yo estaría encantado. ¿Pero Hanako no tenía trabajo por hacer…?"

show hanako basic_smile
with charachange

ha "No… no es tanto…"

show lilly behind_cheerful
with charachange

li "Maravilloso. Parece ser que está decidido entonces."

stop music fadeout 2.0

scene bg suburb_shanghaiint at Fullpan(3.0, dir="left")
with shorttimeskip

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0

"Cruzo mis ojos a través del café mientras los tres entramos. Como es usual, a lo mucho solo hay un puñado de personas, y el nivel de ruido es un tranquilo murmullo de fondo."

scene bg suburb_shanghaiint at left
show hanako emb_emb:
    xpos 0.4 xanchor 0.5
show lilly cane_smileclosed at twoleft
with charaenter

play music music_dreamy fadein 6.0

"El apoyo que Lilly tiene en el brazo de Hanako permanece tal como ha estado durante todo el lento andar de bajada al pueblo, aunque es difícil decir por qué razón, si para guía de Lilly, o para proveer confianza a Hanako."

show lilly basic_smile
with charachange

"Por un momento, Lilly quita su brazo del de Hanako para retraer su bastón mientras Yuuko rápidamente vuela a donde estamos parados, pero poco después lo coloca nuevamente donde estaba."

show yuukoshang closedhappy_up at tworight
with charaenter

yu "¡Bienvenidos al Shanghái! ¿Puedo tomar su orden?"

show yuukoshang neutral_up at Transform(ypos=1.25)
with Dissolvemove(0.5)

show yuukoshang neutral_down at tworight
with dissolvecharamove

"Ella hace una profunda reverencia, poniéndola de buen humor su bien llevada y profesional introducción. Es un buen cambio de la norma para Yuuko."

show lilly basic_smileclosed
with charachange

li "Solo té, por favor. ¿Hanako, Hisao?"

hi "Yo una rebanada de tarta y un café."

show hanako basic_smile
with charachange

ha "Solo… t-té… por favor."

show yuukoshang smile_up
with charachange

yu "Viene enseguida. Por favor tomen asiento donde gusten, y estaré de vuelta pronto."

hide yuukoshang
with charaexit

"Yuuko da una pequeña sonrisa y asiente con la cabeza antes de arrastrarse al mostrador, y nosotros nos dirigimos a unos asientos vacíos cerca de la ventana a paso rápido."

hide hanako
hide lilly
with charaexit

show bg suburb_shanghaiint at right
with charamove_slow

show lilly basic_sleepy_close:
    twoleft
    easein 1.0 ypos 1.1
show hanako basic_smile_close:
    tworight
    easein 1.0 ypos 1.09
with charaenter

"Nos deslizamos a nuestros asientos, las chicas a un extremo, con el bastón de Lilly apoyado a un lado, y yo en el otro. Me doy cuenta de que Hanako no está haciendo algo que comúnmente hace."

"En lugar de mantener sus ojos fijos en el piso y esconderse tras su escolta ciega, ocupada intentando convencerse de que el mundo a su alrededor no existe, está apenas manteniendo sus ojos bajos y ayudando a Lilly a moverse."

hi "¿Estás bien, Lilly? Pareces cansada."

show lilly basic_weaksmile_close:
    twoleft
    ypos 1.1
with charachange

"Ella baja su cabeza un poco, luciendo algo apenada por haberlo dejado ver."

li "Las tareas de representante de la clase pueden ser muy desgastantes, considerando que muchas veces significa tratar con el consejo estudiantil."

show lilly basic_sleepy_close
with charachange

li "Muy desgastantes en verdad."

show hanako basic_normal_close:
    tworight
    ypos 1.09
with charachange

ha "¿Cómo… le va a los otros representantes?"

show lilly basic_reminisce_close
with charachange

li "Mejor que a mí, pero no mucho. Shizune es una persona exigente sin importar con quién esté tratando."

hi "No suena como si disfrutaras particularmente el trabajo. ¿Por qué lo haces en primer lugar, si es tan malo?"

show lilly basic_displeased_close
with charachange

li "Ser representante de la clase es agradable, y puedo manejar la responsabilidad lo suficientemente bien. Es solo que la gente involucrada es algunas veces…"

"Ella baja su voz, cortando sus palabras en el lugar oportuno. Es difícil imaginar a Lilly blasfemando, pero imagino que si alguien puede hacer que lo haga, sería Shizune."

show hanako cover_worry_close
with charachange

"Hanako parece languidecer un poco ante el calor de tal conflicto, pero antes de que pueda desviar un poco el tema, ella se levanta."

show hanako basic_worry_close at tworight
with dissolvecharamove

show lilly basic_surprised_close
with charachange

li "¿Hanako?"

show hanako defarms_strain_close
with charachange

ha "Yo… estaré de vuelta en un momento."

hide hanako
with charaexit

"Con eso, ella se va al sanitario. Supongo que esa es una forma de lidiar con la situación, si eso fue en verdad su motivación."

show bg suburb_shanghaiint at center
show lilly basic_concerned_close at Position(xpos=0.5)
with dissolvecharamove

"Lilly, como sea, parece un poco herida."

hi "No te preocupes por eso. No creo que hayas sido tú."

show lilly basic_oops_close
with charachange

li "Pero…"

hi "Creo que se ha vuelto más fuerte últimamente. Lo has visto tú misma… ¿cierto…?"

"Eso salió un poco mal. Afortunadamente Lilly no parece ofendida, y para estos momentos ya no debería en realidad estar tan asustado de pisar sobre esa mina a su alrededor."

show lilly basic_sleepy_close
with charachange

li "Posiblemente. Pero algunas veces… lo encuentro difícil de saber."

"El silencio reina por un momento antes de que dos tazas de té, una tarta, y una taza de café humeante aparezcan frente a nosotros."

show bg suburb_shanghaiint at right
show lilly basic_sleepy_close at Position(xpos=0.3)
with charamove

show yuukoshang closedhappy_down at tworight
with charaenter

"Noto que Yuuko toma especial cuidado en colocar la taza de té contra las puntas de los dedos de Lilly, permitiéndole saber dónde está."

show yuukoshang closedhappy_up
with charachange

yu "Aquí tienen."

hi "Gracias, Yuuko."

show lilly basic_weaksmile_close
with charachange

li "Muchas gracias."

hide yuukoshang
with charaexit

"Con una rápida y silenciosa reverencia, la mesera de gafas parte."

show bg suburb_shanghaiint at center
show lilly basic_weaksmile_close at Position(xpos=0.5)
with charamove

li "Ah, es cierto. Quería preguntarte algo, y ahora sería el momento apropiado de hacerlo."

hi "Soy todo oídos."

show lilly basic_smileclosed_close
with charachange

li "El cumpleaños de Hanako se acerca, y esperaba que me acompañaras para la compra de regalos en la ciudad este fin de semana."

"¿El cumpleaños de Hanako será pronto? Supongo que sería una buena oportunidad para animarla un poco."

"Como Yuuko, ella parece estar siempre tambaleándose en el límite entre el pánico y la depresión, y nunca la he visto disfrutar mucho de sí misma aparte de en nuestros juegos de ajedrez."

"Y dejando eso de lado, aprender mejor la distribución de la ciudad con un amigo haciéndome compañía suena como una buena forma de pasar el fin de semana."

hi "Seguro, estaría feliz de hacerlo. ¿Has hecho algún plan sobre lo que se hará para su cumpleaños? ¿Una fiesta o algo?"

show lilly basic_weaksmile_close
with charachange

li "Con Hanako siendo Hanako, tal vez una pequeña reunión sería—"

show lilly basic_listen_close
with charachange

"Lilly repentinamente se corta, lo que me deja preguntándome por qué mientras lleva su taza de té a sus labios y comienza a sorber."

"Después de unos segundos, noto a Hanako por encima de su hombro caminando hacia nosotros. El oído de Lilly debe ser muy bueno si fue el sonido de la puerta del sanitario abriéndose lo que la alertó."

show bg suburb_shanghaiint at bgleft
show lilly basic_listen_close at Position(xpos=0.3)
with charamove

show hanako basic_normal_close:
    tworight
    easein 1.0 ypos 1.09
with charaenter

"Hanako toma su asiento una vez más, y de inmediato bebe su té. Pronto estamos los tres tranquilamente comiendo y bebiendo mientras el sol se oculta."

"Es una buena forma de pasar lo que resta de la luz del día, y me hace apreciar los tranquilos y serenos alrededores de Yamaku. Creo que está comenzando a gustarme realmente aquí, con todo y tan aislado como podría ser."

stop ambient fadeout 2.0

scene bg suburb_shanghaiint at bgleft
show lilly basic_smileclosed_close:
    twoleft
    ypos 1.1
show hanako basic_smile_close:
    tworight
    ypos 1.09
with shorttimeskip

"Termino lo que queda de mi café y dejo la taza en la mesa mientras las chicas hablan entre ellas. El café aquí es un poco amargo para mi gusto, pero aún es bastante bueno. Mejor que lo que puedo hacer yo, en cualquier caso."

"La discusión de las chicas está principalmente centrada en sus respectivas preferencias de lectura, lo cual me da un poco de curiosidad sobre un tema relacionado."

hi "Oye Hanako, me estaba preguntando… además del ajedrez y la lectura, ¿tienes algún otro pasatiempo o cosas que te guste hacer?"

show hanako emb_timid_close
with charachange

"Ella se detiene de golpe, luciendo bastante sorprendida de que alguien pudiera estar interesado en tal pregunta sobre ella. Le toma un poco de tiempo formular una respuesta."

show hanako emb_downsmile_close
with charachange

ha "Em… supongo que… me gusta cantar un p-poco. Un poco las c-computadoras también, pero no… no las uso mucho en realidad."

"Cantar no es algo que esperaba escuchar. Es difícil imaginar su voz cantada, tomando en cuenta lo bajo que siempre habla."

show lilly basic_smile_close
with charachange

"Lilly, por otro lado, simplemente asiente. Ella ya debe saber todo esto, pues ya ha sido amiga de Hanako por un año más o menos."

show hanako cover_bashful_close
with charachange

ha "¿Q-qué hay… d-de…?"

hi "¿De mí?"

show hanako basic_bashful_close
with charachange

"Ella duda un poco antes de rápidamente agitar su cabeza de arriba a abajo. Es simplemente lógico que ella quiera saber sobre mis pasatiempos después de decirme los suyos."

hi "Está el ajedrez, obviamente, pero además… hmm…"

hi "Estaba el futbol también, aunque en realidad ya no puedo hacer eso. Leer, pasatiempo que agarré en el hospital… um…"

show hanako basic_normal_close
show lilly basic_sleepy_close
with charachange

"Esto es sorpresivamente difícil. Lilly y Hanako parecen un poco incómodas por la dirección que esto está tomando, y entre más lo pienso, más lo estoy yo también."

show lilly basic_weaksmile_close
with charachange

li "Parece que has adquirido varias cosas desde tu accidente."

"La sinceridad de Lilly está cubierta probablemente con el giro más positivo que alguien podría poner en lo que dije. Hanako, sin embargo, está en silencio."

"Si una situación se vuelve difícil, su reacción parece ser siempre replegarse a un silencio para prevenir que las cosas se pongan peor. Eso, o retirarse físicamente."

$ renpy.music.set_volume(0.2, 0.0, channel="sound")
play sound sfx_phone

show lilly basic_surprised_close
show hanako cover_worry_close
with charachange

"Un ligero timbre nos da una pausa. Mientras Lilly alcanza su bolsillo, se vuelve obvio que el sonido está viniendo de su teléfono."

show lilly basic_weaksmile_close
with charachange

li "Lo siento…"

show hanako basic_normal_close
with charachange

ha "E-está bien…"

show lilly invis_close at Position(ypos=1.0)
with dissolvecharamove

hide lilly
with None

"Lilly asiente rápidamente una vez antes de arrastrarse afuera de su asiento y tomar la llamada a una corta distancia, para evitar molestarnos a ambos."

hi "Debe sentirse bien ser popular."

show hanako cover_bashful_close
with charachange

"Hanako sonríe, pero no toma el anzuelo para continuar con la conversación."

$ renpy.music.set_volume(0.5, 2.0, channel="music")

scene black
with shuteye

"Termino reclinándome hacia atrás y cerrando mis ojos, relajándome lo mejor que puedo."

hi "Es lindo y tranquilo aquí. Me pregunto cómo sería haber crecido en algún lugar como este, en lugar de en la ciudad."

ha "¿Vi-vienes de la ciudad?"

"Parece que he encontrado algo de lo que quiere hablar."

$ renpy.music.set_volume(1.0, 2.0, channel="music")

scene bg suburb_shanghaiint at center
show hanako basic_smile_close:
    center
    ypos 1.09
with openeye

hi "Sí. Podría decirse que fui un niño de ciudad de pies a cabeza."

show hanako basic_worry_close
with charachange

ha "S-suena como que cambiaron m-muchas cosas…"

hi "Así es. Sin embargo aún no estoy seguro de qué sacar de todo esto. Es un poco un shock cultural, en más de una forma."

hi "Debes haber pasado por algo como esto cuando recién llegaste a Yamaku, ¿cierto? Imagino que la mayoría de los nuevos estudiantes lo hacen."

show hanako basic_distant_close
with charachange

ha "N-no realmente…"

"Hanako mira un poco hacia un lado, luciendo poco dispuesta a seguir. Inclino mi cabeza inquisitivamente, pero un par de segundos pasan sin una respuesta."

scene bg suburb_shanghaiint at bgright
show hanako basic_distant_close:
    tworight
    ypos 1.09
with charamove

show lilly back_pout at twoleft
with charaenter

stop music fadeout 8.0

li "¿Pero no podemos lidiar con eso el lunes? Apenas se han asentado las consecuencias de la última…"

show lilly back_listen
with charachange

li "Entiendo. Trataré de hablar con ella. Ya sabes cómo es cuando se ha cerrado a una idea."

li "Sí, gracias. Entonces te llamo después. Hasta luego."

show lilly basic_displeased
with charachange

"La conversación de Lilly termina con el chasquido de su teléfono cerrándose. Ella regresa a nuestra mesa, pero no toma su asiento."

hi "¿Debes irte?"

show lilly basic_concerned
with charachange

li "Por desgracia. El trabajo de representante de la clase llama otra vez."

show hanako cover_worry_close
with charachange

ha "P-puedo ir contigo."

show lilly basic_weaksmile
with charachange

li "Está bien, Hanako. Solo iré directo al consejo estudiantil. No hay necesidad de echar a perder una buena tarde por consideración a mí."

show lilly basic_smile
with charachange

li "Además, si me acompañaras en mi camino de regreso a la escuela, ¿quién haría compañía a nuestro pobre Hisao?"

show hanako basic_normal_close
with charachange

ha "Está bien…"

show lilly basic_weaksmile
with charachange

li "Puedo reunirme otra vez con ustedes para el té más tarde esta noche, si gustan. Bien podría necesitarlo."

show lilly cane_weaksmile
with charachange

"Consentimos con el plan, y Lilly se despide de ambos, tomando su bastón luego de que Hanako se lo pasa."

hide lilly
with charaexit

"A pesar de mi oferta de pagar la parte de Lilly, ella insiste en darnos su porción de la cuenta, y da las gracias a Yuuko mientras se retira."

play music music_dreamy fadein 4.0

show bg suburb_shanghaiint at center
show hanako basic_normal_close:
    center
    ypos 1.09
with charamove

"Y después… estamos solos. Podría ser bueno y todo dejarnos a Hanako y a mí solos para tener un tiempo juntos, pero eso casi siempre significa los dos sentados uno cerca del otro en silencio por un rato."

"Me pregunto cómo debo parecerle a Hanako."

"Nunca pensé en mí como una persona que da miedo, pero tener a alguien de mi misma edad actuando de esa forma a mi alrededor me hace extremadamente consciente de mí mismo, como si fuera mi culpa el que ella se sienta incómoda."

"Podría acostumbrarse más a la gente si dejara de estar tan enclaustrada en Yamaku."

"Pero por otro lado… cuando incluso la gente mucho más grande que ella reacciona tan fuertemente después de una sola mirada a su rostro, bien podría sentirse de la misma forma que yo ahora."

"Es un verdadero callejón sin salida. Si se queda en Yamaku, no se acostumbrará a socializar, pero si se va, cualquier intento que pudiera hacer podría serle lanzado de vuelta por la gente que no puede lidiar con sus cicatrices."

hi "¿Quieres ordenar algo más para no perder el ritmo? Aún no hemos tenido lo que podría llamar una cena, después de todo."

show hanako basic_smile_close
with charachange

"Hanako se anima y asiente vigorosamente, feliz de que saqué el tema por ella. Capto la atención de Yuuko, y diligentemente viene a tomar nuestra orden."

scene bg suburb_shanghaiint at bgright
show hanako basic_smile_close:
    tworight
    ypos 1.09
with charamove

show yuukoshang neutral_down at twoleft
with charaenter

yu "¿Gustan algo más?"

hi "Yo quiero solo un emparedado especial y un chocolate caliente. Ya es un poco tarde para café. ¿Hanako?"

show hanako cover_bashful_close
with charachange

ha "Y-yo… quiero lo mismo…"

hide yuukoshang
with charaexit

"Con un movimiento de cabeza y una reverencia, Yuuko gira sobre la punta del pie y regresa tras el mostrador, donde se ocupa en pescar el pan y condimentos y hacer trabajar la máquina para hacer nuestras bebidas."

show yuukoshang smile_up at twoleft
show hanako basic_bashful_close
with charaenter

"Ni una palabra es dicha entre nosotros hasta que Yuuko regresa. Ella sonríe y nos da nuestra comida y bebidas, antes de avanzar hacia un cliente que ha llamado su atención."

hide yuukoshang
with charaexit

show bg suburb_shanghaiint at center
show hanako basic_bashful_close:
    center
    ypos 1.09
with dissolvecharamove

"Doy por perdida la posibilidad de tener algo como una conversación con mi compañera y decido solo disfrutar mi comida, tan pequeña como pueda ser."

"Sabe bien, como la mayor parte de la comida aquí. Después de algunos bocados, noto que algo está faltando. Concretamente, el sonido de Hanako comiendo."

show hanako basic_distant_close
with charachange

"Mirando hacia ella otra vez, veo a Hanako un poco inquieta detrás de su emparedado intacto."

hi "¿No tienes hambre?"

show hanako cover_worry_close
with charachange

"Ella sacude su cabeza de lado a lado. Aun mientras lo hace, el apaño de cabello que mantiene sobre su lado derecho del rostro todavía hace su trabajo escondiéndolo casi enteramente."

ha "N-no es eso."

hi "Oh. Ya estaba listo para comerme tu parte también."

show hanako basic_worry_close
with charachange

ha "Lucías… p-preocupado. ¿S-sucede… algo m-malo?"

"Me agarra por sorpresa su idea de que soy yo el que luce en problemas, pero pensándolo mejor, probablemente está en lo cierto. Mi cara debe haber transmitido mis emociones sin que yo lo notara, y ella no es nada tonta; más bien lo opuesto."

hi "Somos amigos, ¿cierto?"

show hanako emb_downsad_close
with charachange

ha "Amigos…"

"Por el tono de su voz y postura contraída, parece como que he pisado otra mina más."

"Esta es otra razón del porqué interactuar con ella es difícil; las autoimpuestas barreras psicológicas que pone entre ella y los demás, incluidos yo y, muy probablemente, Lilly. Es una pena que—"

show hanako basic_bashful_close
with charachange

ha "C-creo que lo s-somos…"

"Me toma un poco con la guardia baja la respuesta tan directa de Hanako, y más porque estaba a punto de dar por perdida la posibilidad de obtener cualquier respuesta."

hi "Ya veo…"

show hanako basic_worry_close
with charachange

ha "¿E-estoy mal? P-perdón, y-yo…"

hi "No, es solo que… escuchar una confirmación tuya sobre eso es reconfortante."

hi "Para retomar lo que habías dicho antes: desde que llegué a Yamaku, he estado teniendo algunos problemas con el cómo debo relacionarme con otros."

"Me encuentro riendo un poco. Es sorpresivo el gran alivio que esto ha sido. Puedo sentir mi cara sonriendo mientras tomo mi taza de chocolate caliente y la llevo a mis labios."

hi "¡Ouch! Está caliente…"

show hanako emb_downsmile_close
with charachange

ha "E-esa es…"

show hanako emb_smile_close
with charachange

ha "Esa es la razón por la que aún no he comido. E-estaba esperando… a que mi bebida se enfriara primero."

hi "Supongo que entonces esperaré."

"Ambos compartimos una pequeña risa. La situación no es realmente tan graciosa, pero por alguna razón… se siente como si reír fuera la cosa más natural por hacer justo ahora."

"Supongo que ambos estábamos un poco nerviosos respecto al otro. Estaba tan ocupado pensando que Hanako era la que tenía algo mal, que le tocó a ella recordarme que yo también estaba incómodo."

"Pero sea como fuere… todavía se siente un poco bien. Un poco bien tener a alguien pensando en mí de ese modo, a su manera."

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
stop music fadeout 8.0

scene bg school_dormext_full_ni
with shorttimeskip

"Continuando con una larga y tranquila caminata cuesta arriba a la colina y a los terrenos escolares, los dos nos encontramos entre ambos dormitorios."

"Patrullas nocturnas regulares pasan entre los edificios de los dormitorios de hombres y mujeres, tanto por seguridad como para levantar rápidamente la alarma en caso de que cualquier problema médico surja."

"El guardia actualmente en turno nos asiente rápidamente con la cabeza mientras continúa con su camino."

show hanako emb_downtimid_ni at center
with charaenter

"Un fuerte bostezo escapa de la boca de Hanako antes de tener oportunidad de cubrirlo. Tengo pocas dudas de que ya está bastante cansada."

hi "Mejor me voy a mi cuarto, entonces. Te veo mañana, Hanako."

show hanako emb_smile_ni
with charachange

ha "B-buenas noches…"

hide hanako
with charaexit

"Nos separamos y comenzamos nuestros caminos separados, antes de detenerme y ver atrás."

show hanako basic_smile_ni
with charaenter

"Hanako está de pie, agitando su mano mientras sonríe. Sonrío y me despido igual, y después de unos segundos, se da la vuelta y sube las escaleras del edificio de su dormitorio, desapareciendo a través de la puerta."

hide hanako
with charaexit

"Estos pequeños momentos que compartimos entre nosotros son como un pequeño tesoro. Una cosa es segura; quiero proteger esa pequeña y delicada sonrisa que ella tan fugazmente viste alrededor de tan poca gente."

"Me pregunto sobre estos sentimientos que tengo cuando Hanako está cerca, y cuando logro hacer cosas por ella… no sé si serán la semilla de algo más allá de lo que compartimos ahora."

scene black
with dissolve



label es_H12:

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play music music_happiness fadein 2.0

scene bg school_track
with locationchange

"El sol de verano es algo para ser saboreado, pero cuando se combina con el limpio aire del campo, es aún mejor."

"Los miembros del club de atletismo están corriendo por todos lados en el campo frente a mí; algunos están jugando con un balón de futbol, otros están hablando, y unos pocos ríen mientras dos de ellos juegan luchas."

"Ninguno de ellos me presta atención mientras me siento solo en el pasto, bajo la sombra de un árbol particularmente alto. Es un agradable y pacífico momento después de un pesado día de trabajo de la escuela."

play ambient sfx_footsteps_soft fadein 4.0

"Jugaba futbol bastante seguido antes de mi ataque al corazón, así que pensé que sería bastante nostálgico verlos. Sin embargo, lo que estoy sintiendo ahora, es muy distinto de esa emoción."

stop ambient fadeout 0.3

show miki smile:
    center
    easein 1.0 ypos 1.12
with charaenter

"Escucho pasos acercándose detrás de mí, y giro a un lado para ver a una de mis compañeras de clase tomar asiento a mi lado. Me toma con la guardia baja, porque los dos no nos hemos hablado mucho antes, y no pensé que alguien me notaría aquí."

show miki grinclosed:
    center
    ypos 1.12
with charachange

mk "Qué hay."

hi "Hola. Miura, ¿no es así?"

show miki wink
with charachange

mk "Solo llámame Miki. Los nombres de pila son muy remilgados."

hi "Así lo haré, entonces."

show miki smile
with charachange

"Ambos volvemos a mirar hacia el campo donde los chicos están jugando. Parece que se están preparando para un segundo juego, con las personas dispersándose a sus posiciones y el balón siendo llevado al centro del campo."

"Ya preparados, el silbato es sonado para empezar el partido y con eso vuelven a su juego."

hi "¿No jugarás?"

show miki grinclosed
with charachange

mk "Nah, solo descansaré por un rato."

show miki wink
with charachange

mk "¿Qué hay de ti? Lucías como si quisieras jugar cuando estabas mirándonos hace rato."

"Así que alguien me notó después de todo."

hi "Es una historia un poco larga."

show miki grin
with charachange

"Su rostro me dice que he captado su interés."

hi "Estoy en Yamaku porque tengo un problema del corazón. En realidad ya no puedo jugar futbol."

show miki smile
with charachange

mk "Querías ser jugador de futbol, ¿o no?"

hi "No, en realidad solo lo hacía por diversión. Mis amigos lo jugaban, así que yo jugaba también."

hi "Cualquiera de esos chicos podría haber sido yo antes de mi accidente. Pero no siento tampoco como si tuviera algún interés real en volver. Es un poco difícil de explicar."

"Aún estoy en forma física decente de los días en que jugaba, incluso si mi fuerza ya me ha dejado en gran medida, y me llevé bien con los otros miembros del club."

"Cuando pienso en ello, debería sentirme bastante mal viendo a la gente jugar cuando ya no puedo hacerlo yo. Pero no es así. Tal vez es algo bueno; una señal de que ya lo he sobrellevado y estoy listo para volverme una nueva persona."

hi "Lo siento, como que estoy divagando."

show miki grinclosed
with charachange

mk "Está bien. De hecho estoy feliz de escuchar eso."

show miki smile
with charachange

mk "Suena como que realmente tienes las cosas bajo control. Algunas de las personas que recién vienen a Yamaku están hechas un desastre al principio."

hi "Así que ¿tú eres miembro del club de atletismo, entonces?"

show miki grin
with charachange

mk "Sip. He estado en él desde que llegué aquí."

hi "¿Supongo que no serás amiga de Emi? ¿Bajita, rápida corredora, sin piernas? No creo que haya muchos miembros femeninos de ese club."

show miki grinclosed
with charachange

mk "Jaja, Emi. Todos la conocen, ¿o no?"

show miki smile
with charachange

mk "Pero nah, tiendo a llevarme mejor con los hombres, así que Emi y yo no hablamos mucho en verdad. Como sea, ¿qué hay de ti?"

hi "Ah, bueno, en realidad no estoy en ningún club. Clubes reales, en todo caso."

show miki wink
with charachange

mk "Pero has estado pasando el rato con Hanako y esa amazona rubia, ¿cierto?"

"Amazona rubia… supongo que Lilly tiene la altura para entrar en esa descripción, si no es que más. Asiento como respuesta, sin remarcar nada acerca de las cosas."

show miki grinclosed
with charachange

mk "Entonces no te preocupes por eso. Mientras tengas algunos amigos, no necesitas unirte a un club."

"Un fuerte silbido desde el campo atrae nuestra atención. Uno de los jugadores está en el suelo, agarrando su pierna, y los otros detienen el juego para avanzar hacia él, dejando a Miki haciendo una mueca."

show miki serious
with charachange

mk "Ouch, eso parece doloroso. Ese chico tiene en verdad mala suerte."

"Mientras continúa viendo hacia el campo, no puedo evitar ser recordado de sus propias heridas."

"Su brazo izquierdo, terminando en un muñón en lugar de una mano, ha estado vendado durante todo el tiempo que he estado en Yamaku, y su herida no se ve tan nueva."

"Ella gira para hablarme otra vez y me pesca mirando. Ambos nos sentamos en un incómodo silencio mientras ella toma su brazo vendado y lo sostiene sobre su regazo con su mano restante."

hi "P-perdón. Supongo que aún estoy un poco…"

show miki smile
with charachange

mk "Está bien. En verdad."

"Su tono es alegre, pero ninguno de los dos dice nada después de eso."

"Cada estudiante discapacitado aquí tiene su propia forma de tratar con sus problemas, y que algunos encuentren sus condiciones como incómodas es natural. Estoy incluido en ellos, después de todo."

"El chico herido del juego de futbol se las arregla para ponerse de pie con algo de ayuda, y termina dejando el campo cojeando con un brazo sobre el hombro de otra persona como apoyo."

"Probablemente solo le dio un tirón si aún puede arreglárselas para caminar."

"El silbato suena otra vez, y el juego continúa una vez más con un hombre menos en el campo."

show miki whistle
with charachange

mk "Pasando el rato con Hanako y aquella chica rubia… tienes una extraña compañía."

hi "¿Cómo es eso?"

show miki serious
with charachange

mk "Es solo que Hanako es como… no lo sé."

hi "¿Tímida?"

mk "No, no es realmente eso. Es solo… tiene problemas, yo creo. Realmente no puedo decirlo de algún buen modo."

show miki wink
with charachange

mk "Pero no es que piense que no es una buena persona. Es perfectamente buena."

show miki serious
with charachange

mk "Solo… difícil de tratar."

"Suena como que Miki, o al menos otras personas en el salón, han tratado de acercarse a Hanako en el pasado. Y no resultó muy bien."

"Creo que su juicio es más bien duro, tomando en cuenta que todos, no solo aquellos en Yamaku, tienen sus propios problemas."

"Por otro lado, no he conocido a Hanako por tanto tiempo, así que no me sorprendería si hubiera algunas cosas de las que no supiera."

hi "Solo lo tomo como es. Es una buena persona, y creo que eso debe ser todo lo que importa."

"Los ojos de Miki se estrechan un poco, y su sonrisa se extiende."

show miki grin
with charachange

mk "En verdad te gusta, ¿o no?"

label es_choiceH12:
menu:
    with menueffect
    "Ciertamente Miki no se anda con rodeos."
    "Admitirlo.":


        return m1
    "Negarlo.":

        return m2


label es_H12a:

hi "Para ser completamente honesto… sí, me gusta. Apreciaría si no se lo dices a nadie."

show miki wink
with charachange

mk "Oye, cielos, puedes confiar en mí. No hay problema por ese lado."

show miki grinclosed
with charachange

mk "Para ser honesta, creo que es algo lindo. Si quieres ir por ello, no dejes que yo te detenga."

hi "Gracias."

"Podrá decir eso, pero solo estaba hablando de Hanako teniendo “dilemas”. Aun así, quiero apegarme a las palabras que dije. Los problemas de Hanako no importan; me ocuparé de cualquier cosa que surja, porque quiero ayudarla."

"Si existe la mínima posibilidad de que pueda sacar a Hanako de su depresión y reclusión, entonces debo trabajar con dirección a ella, sin importar nada. Si necesita un príncipe, entonces seré ese príncipe."

"Mientras pienso en la posibilidad de una relación, puedo ver a Miki sonriéndome mientras observa mi rostro. Estoy sin duda sonrojándome, y mirar a otro lado solo la hace reír."


label es_H12b:

hi "No lo creo. Solo somos amigos."

show miki serious
with charachange

mk "Oh. Pensé que había descubierto algo bueno por un momento. Entiendo; los chicos y chicas no necesitan ser novios y novias, después de todo."

"Lo que dice es verdad, incluso si de verdad siento algo por Hanako. En este momento somos buenos amigos, y no quiero echar eso a perder, pero también quiero ser más que eso para ella. Es difícil."


label es_H12c:

"Miki emite una vibra diferente a las otras chicas. Hablarle se siente más como hablarle a un chico en lugar de una mujer. El que ella diga que prefiere la compañía masculina tampoco ayuda a disipar esa idea."

"Dar una mirada a mi reloj me muestra que el receso del almuerzo terminará en solo unos pocos minutos. Tiempo de comenzar el regreso a clase."

hi "El almuerzo está por terminar. ¿Quieres que volvamos?"

show miki smile
with charachange

mk "Sí, mejor vamos."

show miki smile at center
with charamove

"Me levanto del pasto y me sacudo, ofreciendo una mano a Miki para ayudarla a levantarse también. Ella la toma y con facilidad se levanta, mostrando los músculos moviéndose en sus tonificados brazos desnudos en el proceso."

hi "Ahora que lo pienso, ¿por qué no estás vistiendo la blusa normal de las chicas?"

show miki whistle
with charachange

mk "Eh, es demasiado caliente y restrictiva. El uniforme de los hombres es mejor, de todas formas."

"Ella agita sus brazos un poco para enfatizar su punto, que tiene el efecto secundario de mostrar una parte particular de su cuerpo que estaría especialmente restringida por la blusa."

scene bg school_gardens
with locationchange

"Ambos comenzamos a caminar de vuelta al edificio principal a través de los jardines, hablando mientras lo hacemos."

show miki smile at center
with charaenter

mk "Suena como que te estás adaptando bien. Eso es un alivio. Fue bastante sorpresivo recibir un estudiante de transferencia en este punto del año, considerando que los exámenes se están acercando."

hi "No me lo recuerdes…"

show miki grinclosed
with charachange

mk "Jaja, no te preocupes por ellos. Solo estudia todo un día antes y estarás bien."

hi "Eso no suena como un buen consejo."

show miki grin
with charachange

"Ella golpea un par de veces en mi hombro mientras sonríe. No creo que ella se tome la escuela muy en serio."

show miki wink
with charachange

mk "Luces como un tipo listo, y Mutou ya te ha echado el ojo. Le caes como anillo al dedo."

hi "Ahora a decidir si eso es algo bueno o malo."

hi "Aún no sé qué pensar de esta escuela. Ya he estado aquí unas cuantas semanas, pero aún me siento confundido a veces."

show miki smile
with charachange

mk "Te acostumbrarás, tan solo dale un poco de tiempo. Es solo una preparatoria, como cualquier otra."

"Ella lo hace sonar tan simple, pero nunca he pensado en ello de esa forma. Para mí, Yamaku simbolizó un cambio marcado en mi vida. Ya no era normal; era “diferente”, e iba a ser educado con otras personas “diferentes”."

"Y sin embargo, estoy caminando de vuelta a clase y hablando casualmente con una compañera durante el almuerzo, después de ver a otros jugar un juego de futbol. Todo perfectamente normal. Tal vez tiene razón."

"Tal vez solo debo ver a Hanako de la misma forma. Todos tienen sus propios problemas; esto es difícilmente algo único de Yamaku. Después de todo, es solo una preparatoria, como cualquier otra."

"Mientras continuamos hablando, me encuentro sonriendo. Miki y yo somos personas diferentes en casi todo, pero se siente bien el haber podido conocer un poco mejor a otro compañero de clase."

stop music fadeout 2.0

scene black
with dissolve



label es_H13:

play music music_daily fadein 2.0
$ renpy.music.set_volume(0.4, 0.0, channel="ambient")
play ambient sfx_parkambience fadein 2.0

scene bg misc_sky
with locationchange

"Una ligera brisa sopla el aroma de principios de verano por mi cabeza mientras espero a Lilly."

"Pequeñas nubes blancas se esparcen en el cielo, rompiendo la monotonía del azul."

li "¿Hisao? ¿Estás aquí?"

"La voz de Lilly baila en la brisa como si ambas fueran una misma cosa."

"Dejo de observar el cielo para examinar a Lilly."

$ renpy.music.set_volume(0.8, 1.0, channel="ambient")

scene bg school_gate
show lilly cane_surprised_cas at center
with locationchange

"Con un suéter sin hombros color durazno y falda hasta el tobillo color canela, además de dos sandalias canela, es un gusto verla."

hi "Sí, estoy por aquí, Lilly. Cerca del portón."

hi "¿Lograste escapar de Hanako?"

show lilly cane_weaksmile_cas
with charachange

li "Sí. No es inusual que yo salga durante los fines de semana, así que no creo que haya notado nada extraño."

show lilly cane_sleepy_cas
with charachange

li "Eso, y… ella tiene a alguien a quien ve."

"Lilly contrae sus labios, como si tal vez no debiera haber continuado. Yo lo encuentro un poco difícil de creer."

hi "¿Hanako está viendo a alguien? ¿En verdad?"

show lilly cane_weaksmile_cas
with charachange

li "No, es solo que… ella ve a un terapeuta de vez en cuando los fines de semana."

hi "Oh. Bueno. Eso tiene mucho sentido."

show lilly cane_reminisce_cas
with charachange

"Lilly frota su brazo incomodada, y después de una mirada a su preocupada expresión, rápidamente me muevo a cambiar el tema lejos de Hanako."

hi "Eeh…"

show lilly cane_surprised_cas
with charachange

li "¿Sí?"

hi "Solo me estaba preguntando… ¿puedes arreglártelas por ti misma en la ciudad?"

show lilly cane_listen_cas
with charachange

"Lilly suspira por mi consternación sobre el tema de su ceguera. Soy mi propio peor enemigo, algunas veces."

li "Puedo, sí. Aunque es más fácil cuando salgo con un amigo o mi hermana."

"Me pregunto cómo se lleva Lilly con su hermana. Siendo hijo único, es difícil imaginar cómo sería tener un hermano, así que eso me hace sentir un poco de envidia de ella."

hi "Muy bien. Bueno entonces, el autobús llega en unos minutos, así que probablemente debemos irnos."

show lilly cane_weaksmile_cas
with charachange

li "Cierto; es una larga espera si perdemos este."

stop music fadeout 6.0
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene bg school_road
with locationchange

"Con eso, partimos hacia la parada de autobús en la colina. Es solo una pequeña distancia del portón de la escuela, así que es muy conveniente."

hi "Es una buena vista desde aquí. Viniendo de la ciudad, realmente nunca llegué a ver un paisaje como este, y ni hablar de hacerlo diariamente."

show lilly cane_smile_cas at center
with charaenter

li "Esta área es linda para mí también. Es tranquila, y alejada de los ruidos y olores de la ciudad."

show lilly back_listen_cas
show lillyprop back_cane at center
with charachange

"La cabeza de Lilly se levanta animada con uno de sus característicos gestos personales, lo que significa que ha captado un sonido."

show lilly back_smile_cas
with charachange

li "Oh, aquí viene el autobús…"

"Observo la carretera para ver al autobús rodando cuesta arriba a la colina. Su oído es una herramienta bastante útil."

"Al autobús únicamente le toma un poco para alcanzar la parada, forzando su camino a lo alto de la carretera, y en menos de un minuto estamos en nuestro camino a la ciudad."

stop ambient fadeout 2.0

scene bg city_street1
with shorttimeskip

play music music_ease fadein 2.0
$ renpy.music.set_volume(0.4, 0.0, channel="ambient")
play ambient sfx_traffic fadein 2.0

"Caminando por la ciudad siento una distintiva nostalgia. Los olores, el tráfico, los edificios altos en todos lados… es bastante como mi ciudad nativa, excepto por los andadores elevados."

"Se siente un poco extraño; caminar por la ciudad tan casualmente como lo haría por el parque, pero con autos a toda velocidad pasando debajo de mí."

"Mientras estoy absorto reflexionando sobre la maravilla de ingeniería que es el andador elevado, recibo una sorpresa."

show lilly cane_smileclosed_cas_close:
    center
    xpos 0.4
    easein 1.0 xpos 0.5
with charaenter

"Me toma un momento darme cuenta de que Lilly ha abrazado mi brazo con el suyo, extendiendo su bastón frente a ella con la otra mano."

"Por un momento me da un sobresalto, pero me las arreglo para mantenerlo lo suficientemente oculto para que Lilly no lo note. Aunque no ha sido la primera vez que Lilly ha confiado en mí como guía, antes solo se había agarrado al puño de mi manga."

"Es lógico que sería más fácil para ella navegar en una abarrotada y compleja área como la ciudad mientras está unida de forma segura, pero estoy lejos de estar tan acostumbrado a este tipo de contacto como lo está Lilly."

"Finalmente dándome cuenta del creciente silencio entre nosotros mientras Lilly espera a que avance, rápidamente pongo mi cerebro en marcha."

hi "Sabes, fue toda una sorpresa el que a Hanako le guste cantar. ¿La has escuchado hacerlo alguna vez?"

show lilly cane_smile_cas_close at center
with charachange

li "De hecho sí. Hemos estado en sesiones de karaoke varias veces, junto con mi hermana. No puedo decir que me entusiasme mucho en la actividad, pero a las otras dos les gusta."

"Tal vez Hanako haciendo karaoke es más apropiado de lo que en un inicio pensé. Solo ella y aquellos a los que conoce, todos solos en un pequeño cuarto."

"Le proporcionaría una rara oportunidad de dejar su guardia baja, sin nadie más ahí para juzgarla."

hi "Tal vez sería bueno traerla a la ciudad para una fiesta karaoke de cumpleaños, si le gusta hacerlo."

show lilly cane_sleepy_cas_close
with charachange

li "Hmm. No estoy segura de que pudiera manejar muy bien la emoción."

"Me preparo a protestar, pero su cara muestra que aún está dándole vueltas a la proposición un poco más. Le toma un poco de tiempo llegar a una conclusión."

show lilly cane_weaksmile_cas_close
with charachange

li "Por otro lado, lo mejor que podemos hacer por Hanako en este punto es tratar de crear algunas placenteras memorias de cumpleaños. Tratarla continuamente como si fuera anormal no ayudará."

hi "Creo que tienes razón; si tiene algo que recordar aparte de pérdidas, tal vez ella cambiará."

"Si le compramos algo lindo que pudiera ver todos los días entonces tal vez ella lograría sacar de su mente el pasado y recordar que tiene amigos."

"Y en cualquier caso, pienso que Hanako puede manejar algo como esto. En el tiempo que he pasado a su lado, he aprendido que no es tan terriblemente frágil como en un inicio pensé que era."

hi "Así que, ¿partimos? No estoy realmente seguro acerca de la distribución de esta área."

show lilly cane_smileclosed_cas_close
with charachange

stop music fadeout 6.0

li "Muy bien. Me gustaría sugerir primero ir por algo para comer."

hi "Yo tampoco he comido, así que eso suena como un buen plan."

show lilly cane_cheerful_cas_close
with charachange

li "Asegúrate de elegir un buen lugar, Hisao."

"Me da una sonrisa en broma, una que me hace sonreír reflexivamente como respuesta aun si ella no puede ver eso."

hi "Me aseguraré por completo de que así sea, no te preocupes por eso."

stop ambient fadeout 1.0
play music music_another fadein 4.0
scene bg city_karaokeint
with locationskip

"Una vez adentro, ordeno dos rebanadas de tarta y tazas de té para acompañar y las llevo a nuestra mesa."

show lilly basic_smileclosed_cas_close:
    center
    ypos 1.1
with charaenter

"Había etiquetado este café como el tipo que le gustaría a Lilly; pequeño y tranquilo, pero bien cuidado y un tanto elegante. Juzgando por la delicada sonrisa que tiene, creo… que no sé si elegí bien."

"Es muy, muy raro no verla sonriendo, después de todo."

"No obstante, tomo asiento cerca de ella en una de las mesas de la esquina y coloco nuestros alimentos."

show lilly basic_planned_cas_close
with charachange

"Lilly delicadamente lleva su cabeza sobre la rebanada de tarta colocada frente a ella, tomando delicadamente el aroma."

show lilly basic_cheerful_cas_close
with charachange

li "Tarta de limón, ¿cierto? Gracias, Hisao."

hi "No hay problema. El té está justo a un lado de ella, así que ten cuidado de no derramarlo."

show lilly basic_weaksmile_cas_close
with charachange

"Ella asiente apreciativamente, pero a juzgar por la ligeramente débil sonrisa que tiene, la advertencia no era realmente necesaria. Supongo que el sonido debe haberle dado una pista de su posición."

"Ambos comenzamos a comer sin más preámbulos, permaneciendo en bastante silencio mientras lo hacemos. Lilly no es del tipo que aprecia las discusiones mientras come, y no puedo decir que eso me guste tampoco."

"Eventualmente ambos terminamos nuestros alimentos, y lo último de nuestras tazas de té les siguen al poco tiempo. Lilly es la primera en romper el silencio."

show lilly basic_smile_cas_close
with charachange

li "Eso fue muy bueno. Debo decir que has elegido bastante bien, Hisao."

hi "Esta es la primera vez que he podido echarle un vistazo a la ciudad, así que todo lo que pude hacer en realidad fue escoger un lugar que se viera bien."

hi "Uh… maldición. Lo lamento."

"Me siento realmente mal por traer inadvertidamente el tema de la vista en presencia de Lilly, pero no parece importarle mucho. Al contrario; parece casi divertida por mi torpe intento de disculparme."

show lilly basic_smileclosed_cas_close
with charachange

li "Eres considerado, Hisao, pero algunas veces temo que eso se lleva lo mejor de ti. No hay necesidad de cambiar tu modo de hablar en consideración a mí."

"Lilly es en verdad muy despreocupada al tratar sobre su condición. Aun así me apresuro a cambiar el tema, pues no puedo realmente decir que comparto su familiaridad con esa cuestión."

hi "¿Has vivido aquí por mucho tiempo? Parece como que conoces muy bien este lugar."

show lilly basic_planned_cas_close
with charachange

"Rápidamente agita su mano frente a su rostro para descartar esa noción."

show lilly basic_smile_cas_close
with charachange

li "Nada como eso. He asistido a Yamaku desde el comienzo de la preparatoria, pero no caminé mucho por la ciudad porque Akira, mi hermana, me recogía y me dejaba."

hi "Oh, cierto. Mencionaste no vivir en los dormitorios hasta hace poco."

"Es toda una sorpresa. Asumí que había estado viviendo aquí por lo menos desde que entró a Yamaku, lo que daría algunos años aquí."

show lilly basic_smileclosed_cas_close
with charachange

li "He vivido con mi familia la mayor parte de mi vida, después estuve únicamente con mi hermana. Con mi familia mudándose a Inverness hace tiempo, y Akira trabajando más horas, terminé teniendo que mudarme."

hi "¿Inverness? ¿No está eso en algún lugar de Escocia?"

show lilly basic_surprised_cas_close
with charachange

li "Oh, ¿no te lo dije? Actualmente mi familia vive en Escocia, el lugar de nacimiento de mi madre. Pero el lado de mi padre es principalmente japonés."

"Eh. La duda de por qué Lilly tiene esa apariencia cruzó por mi mente varias veces, pero nunca pensé en preguntar. Entonces eso responde aquello."

hi "Para ser honesto, nunca lo habría adivinado. Considerando que no tienes acento, ¿supongo que naciste aquí?"

show lilly basic_giggle_cas_close
with charachange

li "Acertaste. Aunque estoy agradecida con mi herencia, dado que sin ella no se me hubiera enseñado inglés a tan temprana edad."

show lilly basic_smile_cas_close
with charachange

li "¿Y qué hay de ti, Hisao?"

hi "¿Qué hay de mí?"

"Lo piensa por un momento. Probablemente debió haber pensado qué preguntar antes de cambiar el tema."

show lilly basic_weaksmile_cas_close
with charachange

li "Me voy a ir con… ¿cuáles son tus planes para el futuro?"

hi "Para ser honesto, no he pensado mucho en ello recientemente."

hi "Después de mi accidente y los subsecuentes meses en el hospital, disfrutar de mi vida aquí contigo y Hanako ha sido suficiente para mí."

"De hecho, no creo haber pensado para nada en un “futuro” desde hace ya algún tiempo. Casi parece fútil."

show lilly basic_sleepy_cas_close
with charachange

li "Este es tu último año de escuela. Después de esto, tendrás que valerte por ti mismo de una forma u otra."

hi "No es como si no lo supiera, solo no he pensado lo suficiente en ello…"

show lilly basic_weaksmile_cas_close
with charachange

"Ella abre su boca para continuar, pero en lugar de ello da un pequeño suspiro. Parece darse cuenta de que en realidad no sabe lo suficiente acerca de mi situación como para profundizar más en esto."

li "Bueno, todos tenemos nuestro propio ritmo. Solo espero que tomarás cualquier oportunidad que veas."

hi "… Entiendo. Pensaré en ello."

stop music fadeout 2.0

$ renpy.music.set_volume(0.4, 0.0, channel="ambient")
play ambient sfx_traffic fadein 2.0

scene bg city_street2
show lilly cane_smileclosed_cas_close
with shorttimeskip

"Mientras caminamos hacia afuera a la ciudad, Lilly me toma por el brazo una vez más."

show lilly cane_smile_cas_close
with charachange

li "Entonces, ¿se te ocurrieron algunas buenas ideas para regalos?"

hi "Para ser honesto, no. Nunca he sido muy bueno para escogerlos."

show lilly cane_weaksmile_cas_close
with charachange

li "Tan absurdo como suena, tal vez deberíamos solo… ¿ver por ahí?"

"Escuchar a Lilly pronunciar esas palabras me saca de balance por un momento."

hi "Eh… bien. ¿Cómo hacemos eso?"

show lilly cane_cheerful_cas_close
with charachange

li "Esa es exactamente la reacción que estaba esperando. Es simple; puedes ir viendo vitrinas y solo decirme lo que hay por ahí."

show lilly cane_smileclosed_cas_close
with charachange

li "Si algo interesante aparece, entonces podríamos empezar por ahí."

hi "Bien… aún no estoy muy seguro de esto, pero creeré en tu palabra."

show lilly cane_smile_cas_close
with charachange

li "Creo que nos las arreglaremos. Hanako, mi hermana, y yo nos las arreglamos bastante bien."

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")

scene bg city_street3
with locationskip

"Con la simple y bastante optimista declaración de Lilly, partimos hacia el distrito comercial de la ciudad y comienzo a describirle a Lilly todo lo que veo."

"Es difícil imaginar a Hanako yendo a ver vitrinas a las tiendas. No se ve como el tipo que le da mucho valor a la moda, ni la he visto hojeando revistas o cosas así. De hecho, creo que en realidad todo lo que la he visto hacer como pasatiempo es leer."

hi "Hay una tienda de utensilios domésticos adelante. Pero tal parece que son vajillas más que nada."

show lilly cane_sleepy_cas_close at center
with charaenter

li "No creo que ella tenga mucha necesidad de algo así, ¿y eso qué tipo de mensaje le enviaría?"

hi "Um… ¿“cocina más comida”? Eso no es tan mala idea, tal vez…"

show lilly cane_weaksmile_cas_close
with charachange

li "Algunas veces es mejor dejar las cosas en paz, Hisao."

"Una vez más, tengo la sensación de que las proezas de Hanako en la cocina no siempre son exitosas. Lilly debe haber tenido que ayudarla con eso algunas veces."

hi "Vamos a ver, la siguiente es una librería… esa parece una buena opción, ella siempre está leyendo."

show lilly cane_concerned_cas_close
with charachange

li "Sí, pero hay algunos problemas con los libros. No estoy muy segura de lo que ha y no ha leído."

hi "¿Qué tal una tarjeta de regalo entonces?"

show lilly cane_listen_cas_close
with charachange

li "No hay nada tan impersonal como darle a alguien una tarjeta de regalo. Es como decir “no sé lo suficiente sobre ti como para imaginar lo que te gustaría recibir”."

hi "Yo siempre lo pensé como el asegurarse de que recibirían lo que querían."

show lilly cane_displeased_cas_close
with charachange

li "El darle regalos a la gente debería mostrar el nivel de afecto que les tienes. Si no puedes decidir sobre un simple regalo para ellos, ¿entonces cuánto podrías pensar en ellos?"

hi "Cierto, cierto, sin tarjetas de regalos."

"Lilly parece exageradamente apasionada en esto, pero puedo ver su punto. Si vas a buscar algo para alguien, entonces debes poner al menos un poco de cerebro en ello."

"Si quiero buscar algo para Hanako que le recuerde de nosotros cada día, ¿entonces qué tan buena es una tarjeta de regalos?"

hi "En ese caso, ¿qué le diste a Hanako el año pasado?"

show lilly cane_smile_cas_close
with charachange

li "Una muñeca de porcelana. Pensé que si tuviera alguien a quién hablarle, podría ayudarla a aliviar el dolor."

show lilly cane_weaksmile_cas_close
with charachange

li "Una muñeca jamás va a criticarla, después de todo."

hi "¿Entonces debo buscar una tienda de regalos?"

show lilly cane_smileclosed_cas_close
with charachange

li "Si pudieras ser tan amable de estar atento a una, estaría muy agradecida."

hi "Suena bien para mí, aunque desearía que lo hubieras mencionado antes."

show lilly cane_cheerful_cas_close
with charachange

li "Pero si lo hubiera hecho, entonces no hubieras comenzado a pensar por ti mismo, ¿o sí?"

"Una vez más Lilly tiene un punto. Actualmente mi cerebro está analizando cada tienda que pasamos por opciones para regalo. Si Lilly hubiera mencionado una tienda de muñecas desde un inicio no hubiera pensado en nada más."

$ renpy.music.set_volume(0.4, 1.0, channel="ambient")

scene bg city_street4
with locationskip

"Deambulamos por las calles de la ciudad, pero parece ser que somos incapaces de encontrar cualquier cosa que se asemeje a una tienda de muñecas, o algo que pueda considerar un regalo digno."

"El simple acto de buscar está empezando a aclarar mi cabeza. Los eventos de la semana pasada están comenzando a desvanecerse, y estoy deseando darle a Hanako su regalo…"

"… si es que puedo encontrar alguno."

hi "Esto es inútil. Pensé que era seguro que podríamos encontrar algo en la ciudad. Y estoy seguro de que hemos caminado a través de esta calle al menos una vez antes."

show lilly cane_oops_cas_close at center
with charaenter

li "Eso suena como que estás casi dándote por vencido, Hisao."

hi "No lo estoy, pero es mucho más difícil de lo que pensé."

show lilly cane_smileclosed_cas_close
with charachange

li "Trata de no ser tan rígido con tus ideas. ¿Tal vez deberíamos de hecho entrar a algunas tiendas y ver por ahí?"

hi "Eso podría funcionar. Nunca he sido muy bueno con eso de ir viendo vitrinas."

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")

scene bg city_street3 at right
with locationskip

"Lilly y yo damos una vuelta por las calles de la ciudad una vez más, pero esta vez entrando en las tiendas que llaman nuestra atención. Al final, sin embargo, nada se muestra como especialmente apropiado."

"Los gustos de Hanako son muchas veces difíciles de identificar cuando mejor nos va, gracias a su naturaleza intensamente reservada, y aquellos gustos que sí sabemos son difíciles de acomodar."

show lilly cane_sleepy_cas_close at center
with charaenter

li "¿Podríamos tomar un descanso por un minuto? Estoy un poco exhausta."

show lilly cane_sleepy_cas_close:
    ypos 1.05
with charamove

show bg city_street3 at left
show lilly invis:
    xpos 0.8
    ypos 1.05
with dissolvecharamove

"Concuerdo con Lilly y la dejo descansar contra un barandal mientras voy por un par de bebidas de una máquina expendedora cercana."

"Después de caminar a la máquina expendedora y agarrar algo de limonada para mí, me encuentro un poco perdido. Sin saber realmente los gustos de Lilly, decido adivinar y agarro algo que parece un poco femenino, pero no demasiado extraño."

"Leche sabor fresa."

show bg city_street3 at right
show lilly cane_weaksmile_cas_close:
    center
    ypos 1.05
with dissolvecharamove

hi "Volví."

"Camino hacia ella y coloco el cartón dentro de sus manos extendidas, asegurándome de que lo ha agarrado antes de dejarlo ir."

show lilly cane_smile_cas_close
with charachange

"Ella siente sus contornos antes de abrirlo y tomar un muy titubeante sorbo, su sonrisa aprobatoria inmediata me dice que hice la elección correcta. Ambos descansamos y bebemos tranquilamente por unos minutos."

$ renpy.music.set_volume(0.2, 0.0, channel="sound")
play sound sfx_phone

show lilly cane_surprised_cas_close
with charachange

"Un ligero repique familiar comienza a sonar del lado de Lilly. Ella rápidamente se disculpa mientras su mano va hacia su bolso, sacando su teléfono celular."

show lilly cane_weaksmile_cas_close
with charachange

li "¿Te molesta si tomo esta llamada?"

hi "Está bien, no te preocupes."

show lilly back_listen_cas_close
show lillyprop back_cane_close:
    center
    ypos 1.05
with charachange

"Ella agradece inclinando su cabeza antes de dar la vuelta y abrir el teléfono, llevándolo al lado de su rostro mientras contesta la llamada. "

show lilly back_smile_cas_close
with charachange

"Por el tono de voz de Lilly, la persona al otro lado del teléfono es sin duda algún amigo o parecido. Me desconecto de su conversación rápidamente, pues los fragmentos que Lilly dice lo hacen sonar como poco más que un chisme."

"Sin nada más que hacer, me encuentro mirando a Lilly. Realmente es una linda chica, lo que difícilmente afectaría su popularidad en la escuela. Es interesante lo mucho que Hanako y Lilly contrastan entre ellas, tanto en personalidad como apariencia."

show lilly back_smileclosed_cas_close
with charachange

"Por unos minutos solo me recargo hacia atrás y bebo, mirándola. No mucho después, Lilly dice adiós a la persona con la que habla y cuelga, dejando su teléfono de vuelta en su bolso y recargándose en el barandal como antes."

hide lillyprop
show lilly cane_weaksmile_cas_close
with charachange

li "Lo siento, solo un amigo de la clase."

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_can_clatter

"Doy un último trago a mi lata antes de arrojarla en la basura. Poco después Lilly me da su envase para tirarlo, terminándolo relativamente rápido."

$ renpy.music.set_volume(0.1, 2.0, channel="ambient")

hi "Pareces tener muchos amigos."

show lilly cane_smile_cas_close
with charachange

li "¿Oh?"

"Lilly espera a que termine, captando su interés."

hi "Solo estaba pensando que tú y Hanako realmente contrastan mucho. Es difícil imaginar a Hanako haciendo muchas de las cosas que tú haces, o conociendo a la gente que tú conoces."

show lilly cane_giggle_cas_close
with charachange

li "Pareces pensar bastante en Hanako."

hi "No lo sé. Es solo… es misteriosa, supongo. Como que quiero conocer más sobre ella, lo cual no es fácil de decir."

show lilly cane_weaksmile_cas_close
with charachange

li "Casi suena como si estuvieras dudando de tu relación con ella."

hi "No creo que sea eso. Solo quiero hacer más por ella, siendo su amigo y eso. Ni siquiera sé realmente cómo me ve ella."

show lilly cane_smile_cas_close
with charachange

"Esta declaración parece interesarle algo a Lilly. Me pregunto si Hanako le ha dicho algo sobre mí a Lilly durante sus conversaciones."

show lilly cane_smileclosed_cas_close at center
with dissolvecharamove

"Estoy por preguntarle qué hay en su mente cuando ella se separa del barandal."

show lilly cane_cheerful_cas_close
with charachange

li "¿Deberíamos partir, entonces?"

"Su voz y expresión me muestran que está jugando conmigo. Lilly sabe endemoniadamente bien que me está dejando volando."

"Con un suspiro, me separo también del barandal y doy un vistazo rápido alrededor. Tenemos cosas que hacer, así que solo intentaré hacerla regresar a esto después."

"Aprisionada entre un puesto de revistas y un minisúper está una pequeña tienda. El letrero sobre la puerta dice “Antigüedades Otelo” en escritura decorativa inglesa."

"Sería fácil de pasar por alto si estuviéramos caminando por la calle, pero dado que estamos inmóviles y estoy observando alrededor deliberadamente, simplemente es notable."

$ renpy.music.set_volume(0.3, 6.0, channel="ambient")

hi "Dime, Lilly… esa muñeca que le diste a Hanako; ¿era nueva?"

show lilly cane_smile_cas_close
with charachange

li "Bueno, sí, pero no estoy muy segura de lo que quieres decir."

hi "Creo que he encontrado nuestra tienda. Está cruzando la calle."

show lilly cane_surprised_cas_close
with charachange

li "¿Oh? ¿Qué es? ¿Algún tipo de juguetería?"

hi "Es una tienda de antigüedades. Creo que será probablemente nuestra mejor apuesta."

show lilly cane_satisfied_cas_close
with charachange

li "¿En verdad? Ni siquiera sabía que teníamos una de esas cerca de aquí."

hi "Yo tampoco, se me pasó la primera vez que anduvimos por aquí. Está bastante bien escondida."

show lilly cane_smileclosed_cas_close
with charachange

li "Bien entonces, no puede hacer mal revisar."

"Inspirado por este nuevo hallazgo, rápidamente nos sacudimos y nos dirigimos a la tienda, la mano de Lilly dirigiéndose a mi codo para guiarse."

stop ambient fadeout 0.5

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_storebell
play music music_soothing fadein 0.5
$ renpy.music.set_volume(1.0, 4.0, channel="ambient")

scene bg city_othello at right
with locationchange

"La tienda tiene un extraño y almizclado aroma. La disposición es más como un garage que como una tienda; las cosas están esparcidas por todo el piso sin ninguna apariencia inmediata de orden."

show shopkeep neutral at center
with charaenter

"El encargado nos da una mirada casi aburrida a través de sus particularmente pequeños ojos."

"Su rostro luce fastidiado y cansado, y su forma de vestir es distintivamente anacrónica. Nos da un cortés asentimiento de bienvenida antes de volver a su libro."

hide shopkeep
with charaexit

"Lilly se agarra fuertemente a mi brazo, y me encuentro dividiendo mis esfuerzos entre asegurarme de que no se nos pase por alto un regalo potencial para Hanako y que Lilly no tropiece inadvertidamente con algo."

show bg city_othello at center
with charamove_slow

"La tarea es bastante difícil dada la arbitraria forma en que la tienda está acomodada, y las muchas cosas sobresaliendo de los anaqueles o los muebles en los que están."

"Sin embargo, eventualmente llegamos sin contratiempos a un viejo escritorio cubierto de muñecas y osos de peluche."

hi "Creo que este es el lugar correcto. Aquí hay prácticamente cualquier tipo de muñeca que podrías imaginar."

show lilly cane_smileclosed_cas_close at center
with charaenter

li "Eso debe hacer la elección mucho más fácil. ¿Podrías por favor elegir una por mí, Hisao?"

"Tenía la idea de que terminaríamos en esto. Dibujo a Hanako en mi mente, y trato de imaginar cuál de las muñecas frente a mí le quedaría mejor."

"Mis ojos se pasean entre la colección; cada una es tan exquisita como la anterior. La cantidad de estilos en sí misma es alucinante, pero eventualmente una capta mi atención."

hi "Aquí, ¿qué tal esta?"



"Tomo una pequeña muñeca de porcelana que luce al menos un poco asequible. Ataviada en un vestido verde de la era Victoriana con un pequeño sombrero café descansando sobre su rubio cabello, luce un poco como Lilly."

show lilly cane_listen_cas_close
with charachange



"Gentilmente se la paso a Lilly, quien delicadamente siente cada fracción del objeto mientras mantiene una mirada de ligera concentración."

show lilly cane_smile_cas_close
with charachange

li "Ciertamente se siente hermosa. ¿En tu opinión, crees que le sentará bien a Hanako?"

hi "Creo que lo hará; luciría bien en su habitación."

show lilly cane_smileclosed_cas_close
with charachange

li "En ese caso, confiaré en tu juicio. ¿Le darás algo también, o este deberá ser un regalo compartido?"

hi "Hmm, no estoy seguro. Creo que debería darle algo también, pero no creo que darle otra muñeca sea una gran idea. Tal vez…"

"Dejo mi voz apagarse mientras busco alrededor de la tienda. Descansando en un escritorio no lejos de nosotros está una caja decorativa que capta mi atención."

hi "Espera aquí, creo que he encontrado algo…"

show lilly cane_ara_cas_close
with charachange

li "Vaya vaya, eso fue rápido."



"Cautelosamente camino a través de la cristalería y tomo la caja. Los costados de madera están cubiertos en tallados representando antiguas batallas alrededor de un castillo."

"La parte de arriba, sin embargo, luce demasiado familiar. Cuadros alternados de madera barnizada en blanco y negro están ordenados en la tapa."

sk "Ese es un objeto realmente bueno. Es un juego de ajedrez del extranjero."



show bg city_othello at bgleft
show lilly cane_smileclosed_cas_close at twoleft
with dissolvecharamove

show shopkeep neutral at tworight
with charaenter

"La súbita aparición del dueño de la tienda me sobresalta un poco; en realidad no lo vi acercarse."

"Supongo que está tratando de ayudarnos porque realmente no lucimos como si supiéramos lo que buscamos… O por otro lado, tal vez quiere echarnos un ojo porque sospecha que podríamos hurtar la tienda."

hi "Estoy… buscando un regalo para una amiga."

show shopkeep happy
with charachange

sk "Ya veo. En ese caso, este juego de ajedrez sería una elección perfecta."

"Súbitamente me doy cuenta de algo. Este es un juego muy bonito, pero esta es una tienda de antigüedades. No son bien conocidas por sus precios baratos."

hi "¿Qué tan viejo es esto?"

show shopkeep neutral
with charachange

sk "Esta es una reproducción. Mi mejor estimación es de hace unos cinco años."

hi "Ya veo. ¿Cuánto vale?"

show shopkeep thinking
with charachange

"Lo piensa un poco antes de decirme, lo cual es ligeramente desconcertante."

show shopkeep neutral
with charachange

sk "Te dejaré llevártelo hoy por 7 000 yenes."

"Me muestro un poco reacio; no estaba esperando gastar tanto, pero esto sí luce perfecto. Por otra parte, tal vez eso es testimonio de lo bien que midió la cantidad que me haría pagar."

hi "¿No podrían ser 5 000?"

show shopkeep thinking
with charachange

sk "5 500, no menos."

hi "Vendido. Oh, también quisiéramos llevar esa muñeca…"

show shopkeep neutral
with charachange

"El dueño de la tienda mira sobre mi hombro, enfocándose en Lilly y la muñeca en sus manos. Sus ojos se estrechan, y visiblemente toma un momento para poner en marcha sus engranajes mentales."

"En el proceso, su sonrisa se pierde ligeramente."

sk "Ah…"

"Supongo que eso significa que no todo en esta tienda es una reproducción."

show shopkeep thinking
with charachange

sk "¿Está completamente segura de que desea esa muñeca, señorita?"

show lilly cane_smile_cas_close
with charachange

li "Confío en el juicio de mi amigo."

show shopkeep surprised
with charachange

sk "Ya veo… oh, no quise ofender…"

show lilly cane_smileclosed_cas_close
with charachange

li "No lo hizo. Si pudiera por favor envolverla por mí, sería apreciable."

show shopkeep neutral
with charachange

sk "Sí, desde luego, pero cuesta 20 000 yenes…"

"Lilly alcanza su bolso y muestra cuatro billetes de 5 000 yenes nuevos."

show lilly cane_cheerful_cas_close
with charachange

li "Aquí tiene, 20 000 yenes."

show shopkeep thinking
with charachange

"El encargado obedientemente los toma junto con la muñeca, y procede hacia el mostrador. Tomo el brazo de Lilly para guiarla ahí."

hi "¿Estás segura de esto?"

show lilly cane_smileclosed_cas_close
with charachange

li "Está bien; yo… tengo el dinero que necesito. Como dije, confío en tu juicio."

"Me siento un poco culpable por dos frentes; primero porque Lilly acaba de gastar mucho dinero en mi recomendación, y segundo porque tengo el presentimiento de que el valor de mi regalo no es lo suficientemente alto."

"No obstante, Lilly en verdad parece un poco incómoda siempre que se menciona el dinero…"

show shopkeep neutral
with charachange

"Le paso al encargado mi regalo y el dinero cuando es el momento. Él pone el dinero en la registradora antes de ocuparse en envolver la muñeca y repetir el proceso con el tablero de ajedrez."

"Eventualmente, él termina de envolverlos y nos da a ambos nuestros regalos."

show shopkeep happy
with charachange

sk "Por favor vayan con cuidado, y vuelvan otra vez."

hi "Gracias."

show lilly cane_smile_cas_close
with charachange

li "Cierto, muchísimas gracias."

"El dueño de la tienda nos da una reverencia profunda mientras partimos."

stop music fadeout 6.0
$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_traffic fadein 1.0

scene bg city_street3
with locationchange

show lilly cane_weaksmile_cas_close at center
with charaenter

li "Bueno, eso nos tomó todo el día, pero al final encontramos algo."

hi "Eso hicimos."

"Ahora que los presentes están envueltos, me estoy sintiendo un poco impaciente por dárselos a Hanako. Es una reacción común al comprar regalos; querer ver la reacción del que lo recibe al descubrir lo que es."

"Y parte de mí quiere regresar a Hanako, solo para confirmar su condición con mis propios ojos."

hi "¿Entonces deberíamos volver?"

show lilly cane_smile_cas_close
with charachange

li "Hagámoslo. Hemos caminado bastante hoy, así que no me molestaría tomar un descanso de vuelta en los dormitorios."

"Lilly está en lo cierto. Ahora que la necesidad de encontrar una tienda ha terminado, mis piernas están sintiéndose un tanto cansadas."

hi "Bueno, entonces regresemos a la escuela. Ya deseo descansar un poco también."

"Lilly extiende su brazo, y enlazo el mío con el de ella. Juntos, tomamos nuestro camino de vuelta a los dormitorios."

stop ambient fadeout 2.0

scene black
with dissolve



label es_H14:

play music music_pearly fadein 5.0

scene bg school_scienceroom at right
with locationchange

"Mutou nos lee ecuaciones y fórmulas una por una, en su usual tono sin entusiasmo, directamente del libro."

"Es posible que esté entusiasmado por lo que nos enseña; algunas veces puede mostrar una incómoda chispa de pasión por ello, como si estuviera empezando a meterse en el material."

"Sin embargo, la mayoría de los días, son como este."

"Lo que estamos cubriendo es algo simple, así que encuentro incrementalmente difícil mantener mi concentración en él. No pasa mucho antes de que mis piernas comiencen a doler otra vez, lo cual lo vuelve aún más difícil."

"Casi estoy comenzando a lamentar el haber caminado por la ciudad ayer con Lilly."

"Desde que dejé el hospital, he hecho muy poco esfuerzo físico. Caminar a y desde la tienda de la esquina local apenas cuenta."

"A pesar de los intentos de Emi cuando recién llegué a Yamaku, me he dado mayormente por vencido de la idea de regresar a mi antiguo nivel de estado físico."

"Tengo pocas dudas de que ese es el porqué caminar por la ciudad por tantas horas me ha hecho sentir adolorido. Es deprimente, y me recuerda una cosa más que no puedo hacer desde mi ataque al corazón. Me hace sentir patético."

show muto normal at twoleft
with charaenter

mu "¿Ahora… Ikezawa?"

show hanako defarms_shock at tworight
with vpunch

"Es extraño para Mutou el hacerle a Hanako una pregunta, pero no es algo que nunca se vea. Ella rápidamente salta en pie, un poco sobresaltada, e inmediatamente fija sus ojos en él."

"Ella sabe que Mutou haciéndola participar es raro, así que todos los ojos en el salón estarán sobre ella. De esta forma, ella no corre el riesgo de hacer contacto visual con nadie más."

show hanako def_worry
with charachange

ha "¿S-sí?"

mu "En este ejemplo particular de reacción redox, la reacción de combustión del metano produce de hecho un producto más que no está listado. ¿Ese producto es…?"

show hanako emb_downtimid
with charachange

"Incluso aunque es una pregunta sencilla, ella tímidamente espera un poco antes de contestar, mordiendo ligeramente su labio inferior como para mantener la concentración."

show hanako emb_timid
with charachange

ha "Em… ¿c-calor?"

show muto smile
with charachange

mu "Bien hecho. Esta es una reacción exotérmica, con la reacción dando más calor del que se pone en ella."

show hanako invis:
    ypos 1.1
with dissolvecharamove

hide hanako
with None

"Recibiendo un gesto de afirmación de Mutou, Hanako toma su asiento una vez más y da un suspiro de alivio."

"Un vacilante comienzo, pero es algo."

"Será bueno salir con ella para su cumpleaños, algún lugar diferente del usual aislamiento de su habitación y el cuarto de té. Con el progreso que ha hecho hasta ahora, no creo que vaya a haber mucho problema con el ir a la ciudad."

show muto smile at center
show bg school_scienceroom at center
with charamove

mu "Bien entonces. Por lo que resta de esta clase me gustaría que trabajaran en grupos de tres o cuatro en los problemas del capítulo 12. Estaré aquí si me necesitan."

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 8.0

show muto invis:
    ypos 1.1
with dissolvecharamove

hide muto
with None

"Mutou se sienta tras su escritorio, saca unas hojas sueltas de una carpeta y comienza a trabajar en una especie de papeleo suyo. Pensé que se esperaba que los maestros hicieran esa clase de cosas después de clase, no durante ella."

show shizu invis_close:
    tworight
    xpos 0.8
show misha invis_close:
    twoleft
    xpos 0.2
with None

show shizu behind_blank_close at tworight
show misha hips_smile_close at twoleft
with dissolvecharamove

"A pesar de ello, miro a mi derecha para elegir a alguien con quién formar un grupo. Dadas las dos sonrientes caras rondando cerca de mí, creo que no voy a tener mucha voz en ese asunto."

hi "Supongo que tenemos un grupo entonces."

show misha hips_grin_close
with charachange

mi "¡Hicchan~! ¿Quieres que trabajemos juntos? ¡Bien, bien~! ¡Eso es grandioso! ¡Hacía ya tanto tiempo~!"

show shizu behind_blank_close:
    ypos 1.09
show misha hips_smile_close:
    ypos 1.09
with dissolvecharamove

"La clase comienza el proceso de arrastrar ruidosamente los bancos por el lugar, con Shizune haciendo lo mismo mientras pone el suyo delante del mío."

"Es un poco afortunada de no poder escuchar el alboroto del salón, el cual es lo suficientemente fuerte para causar algo de incomodidad."

"A decir verdad, trabajar con Shizune y Misha dará probablemente buenos resultados, Shizune y yo somos bastante buenos en este tema, y Misha… tiene letra muy linda."

show hanako silhouette behind shizu at center
with charaenter

"Mientras veo a Misha, noto una figura alta tras ella. La sombra capta la atención de Misha también que gira para ver de frente al observador de cabello oscuro."

show shizu behind_blank_close at Position(xpos=0.8)
show misha perky_smile_close at Position(xpos=0.2)
show hanako basic_worry
with dissolvecharamove

mi "¡Buenas tardes, Hanako~!"

show hanako emb_timid
with charachange

ha "Um… hola…"

"Shizune finalmente nota a Hanako, después de levantar la vista y seguir la mirada de Misha y mía. De forma rápida, ella golpetea a Misha en el hombro para llamar su atención antes de comenzar a hacer señas."

show shizu adjust_happy_close
with charachange

shi "…"

show misha sign_smile_close
with charachange

mi "Shicchan dice, ¡si estás buscando un grupo, puedes unirte al nuestro~!"

show hanako emb_downsmile
with charachange

"Hanako baja la mirada y se sonroja un poco por la oferta. De toda la gente en la clase, Hanako está más familiarizada con nosotros tres, así que es razonable que vendría a nosotros primero."

"Por otra parte, ella viniendo a un grupo con la intención de unirse es algo que aparentemente muy rara vez hizo antes."

hide hanako
with charaexit

show shizu behind_smile_close:
    tworight
    ypos 1.09
show misha hips_smile_close:
    twoleft
    ypos 1.09
with dissolvecharamove

"Ella se va momentáneamente para jalar su banco, y Shizune y Misha dan la vuelta hacia mí tan pronto como ella da la espalda."

show shizu adjust_happy_close
with charachange

shi "…"

show misha perky_smile_close
with charachange

mi "¡Supongo que jugaremos otra vez, Hicchan~! Ya casi nunca juegas con nosotras…"

hi "¿Me pregunto por qué? Ustedes dos parecen tener siempre un motivo escondido."

show shizu basic_frown_close
with charachange

shi "…"

show misha hips_frown_close
with charachange

mi "Eso dolió, Hicchan… ¡Casi podría pensar que estabas insultándome~!"

show misha hips_grin_close
with charachange

mi "¡Pero~! Es Hicchan, ¡así que sé que estás bromeando!"

hi "Tan buen sentido del humor al respecto; sería terrible si alguien fuera a tomar ventaja de tu buena naturaleza. Como hacerte ayudarles con su trabajo."

show shizu adjust_smug_close
with charachange

shi "…"

show misha cross_laugh_close
with charachange

mi "¡Guajaja~!"

"Shizune luce emocionada por un segundo, un poco sorprendida de que estoy dispuesto a retarla, pero cuando ve a Hanako volviendo, ella se repliega con una sonrisa. Supongo que los juegos mentales han terminado temprano hoy."

show hanako invis_close behind shizu at center
with None

show shizu behind_blank_close at Position(xpos=0.85)
show misha perky_smile_close at Position(xpos=0.15)
show hanako emb_downtimid_close at Position(ypos=1.09)
with dissolvecharamove

"Hanako cuidadosamente coloca su banco frente al de Misha. Con sus ojos fijos abajo, y me quedo preguntándome por qué hasta que veo alrededor de la clase."

"La mayoría están ocupados preparando sus equipos, pero unos pocos le están lanzando miradas curiosas. En este punto, es difícil decir si hasta ahí es donde termina su interés en ella, o si están hablando de ella también."

"Es extraño. Nadie presta atención cuando Hanako escapa del salón para evitar el trabajo en grupo, pero ahora que está haciendo un esfuerzo se le quedan viendo como si hubiera hecho algo malo."

"Todos nos movemos para acomodarnos, extendemos nuestros cuadernos y hojas de trabajo alrededor de la superficie más grande creada por nuestros escritorios unidos. No pasa mucho antes de que toda la clase empiece a trabajar."

show misha sign_smile_close
with charachange

mi "¡Hola, Hanako~! Es bueno trabajar finalmente contigo~."

show hanako basic_distant_close
with charachange

ha "S-sí."

show shizu adjust_smug_close
with charachange

shi "…"

show misha hips_grin_close
with charachange

mi "¿Eres la razón por la que Hicchan ha estado evitándonos últimamente~? Shicchan dice que es un poco rudo, pero si Hicchan quería pasar tiempo con una linda chica, ¡es entendible~!"

show hanako cover_worry_close
with charachange

ha "Y-yo no c-creo que sea así…"

"Hanako comienza a agitarse, no acostumbrada a este tipo de atención."

"Creo que para este momento una persona ordinaria dejaría la conversación, pero Misha es como la antítesis de Hanako. Parte de ello incluye ser ciega a las señales sociales ordinarias, mientras Hanako es excesivamente sensitiva a ellas."

"Por ello, Misha continúa disparando las preguntas, demasiado rápido como para que yo logre interceder y guiar la discusión a algo más agradable."

stop music fadeout 7.0

show misha hips_smile_close
with charachange

mi "¿En verdad~? ¡Entonces~! ¿Él no estaba pasando el rato contigo ayer?"

show hanako emb_downsad_close
with charachange

ha "N… no…"

"Ya puedo sentir mi coartada haciéndose pedazos. Lilly no quería que supiera que estuvimos fuera comprándole regalos, ni hablar de que planeábamos su fiesta de cumpleaños. No sería bueno para ella que lo descubriera."

hi "Bueno estaba… haciendo algo más. Ya sabes cómo es…"

show shizu behind_blank_close
with charachange

shi "…"

show misha sign_smile_close
with charachange

mi "¿En verdad~? ¡Me pregunto qué era tan importante como para que Hicchan nos mandara a volar así~! Si no era para pasar tiempo con Hanako, ¿entonces qué podría ser~? Es realmente interesante…"

"Ahora esto está comenzando a sentirse como un interrogatorio. Estoy sorprendido por cómo Misha es capaz de ejercer tal sensación de presión sin en realidad intentarlo."

show hanako defarms_strain_close
with charachange

ha "¿E… estuviste con L-Lilly?"

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")

"De la nada, Hanako se las arregla para tropezar con la respuesta. Puede ser terriblemente tranquila y tímida, pero es muy intuitiva."

hi "¿Q-qué te hace decir eso?"

show hanako emb_sad_close
with charachange

ha "A-ayer Lilly dijo algo s-similar."

show shizu basic_happy_close at Position(xpos=0.8)
with charachange

shi "…"

show misha hips_smile_close
with charachange

mi "¡Sospechoso~! ¡Hicchan~! ¡Exijo que te expliques!"

hi "Oigan, ¿no deberíamos estar haciendo un trabajo?"

show misha cross_smile_close
with charachange

mi "¡Pero~! Es tan misterioso… ¡Incluso Hanako quiere saber~!"

"Volteo a ver a Hanako. Es verdad; por la expresión en su cara, es obvio que quiere saber también, y creo que hemos pasado el punto en el que me podría escapar de tener que dar una explicación."

"Le pido disculpas a Lilly en mi mente. Ella realmente quería mantenerlo en secreto, pero parece que eso ya no es posible."

"Siento una ola de emociones encontradas, tan revueltas que no puedo identificarlas fácilmente, pero chocan en mi cabeza mientras trato de calmarme y hablar."

hi "Está bien, se los diré. Fui a la ciudad con Lilly, pero no fue lo que piensan."

hi "Lilly y yo estuvimos… eh… para el cumpleaños de Hanako… nosotros estuvimos…"

"El secreto se ha destapado. Pero parece que Hanako lo está tomando un poco mejor de como pensé que lo haría."

show misha perky_confused_close
show shizu adjust_blush_close at Position(xpos=0.85)
show hanako emb_downtimid_close
with charachange

"Un corto silencio pasa por nuestro pequeño grupo mientras Shizune y Misha se ven la una a la otra avergonzadamente. Puedo decir que ellas no esperaban que su juego se tornara en algo así."

"Misha voltea hacia Hanako para disculparse, después se detiene. Hanako está viendo al centro de su banco y apenas moviéndose, con una llorosa expresión en su rostro. Supongo que estaba mal sobre ella tomándolo bien."

show misha perky_sad_close
with charachange

mi "¿Hanako? Lo lamento…"

"Hay una pausa de unos segundos, pero Hanako eleva y sacude su cabeza."

show hanako emb_timid_close
with charachange

ha "Está… bien…"

"Su expresión se ve extraña, como si estuviera muy cansada. Eso no parece natural, pero no es nada alarmante. Realmente nadie quiere continuar con la conversación actual, así que abrimos nuestros cuadernos y comenzamos nuestro trabajo en grupo."

play music music_rain fadein 12.0
$ renpy.music.set_volume(0.5, 5.0, channel="ambient")

show shizu basic_normal2_close at Position(xpos=0.8)
with charachange

"Esto es muy tonto. Aunque las ecuaciones que se supone trabajaremos en equipo tomarán un tiempo, la mayor parte de eso va a ser aburridamente mecánico."

"Tampoco ayuda que aunque eso no fue tan malo como podría haber sido, ha dejado una atmósfera incómoda entre nosotros. Aun así, nos las arreglamos."

"La cara de Shizune revela que ella tiene casi las mismas expectativas de nuestro trabajo que yo, y ambos comenzamos nuestros resultados grupales."

show misha perky_confused_close
with charachange

"Misha, por otro lado, está estrujando sus labios y tratando muy visiblemente de encontrarle pies o cabeza a lo que estamos haciendo."

"Hanako está observando en silencio, absorbiendo lo que escribimos y lo que digo. Usualmente tiene esta misma expresión cuando el maestro habla."

"Es una pena que su asistencia sea tan inconstante."

"Con la forma en que capta información, pienso que lo haría bastante bien en clase, si en verdad siguiera las lecciones regularmente. Me pregunto si este podría ser el porqué Shizune parece presionarla tanto."

show misha perky_smile_close
with charachange

mi "¿Oye, Hanako, tú entiendes esto~?"

"Misha ve a Hanako, pero sospecho que su esperanza es más encontrar un camarada en la ignorancia que ayuda genuina."

show hanako emb_downtimid_close
with charachange

ha "Yo-yo… em… n-no realmente… s-supongo…"

"Soy sorprendido por la forma tan tensa en que responde, pero se tranquiliza otra vez. Ella exhala, y la forma en que la parte de arriba de su cuerpo y su cabeza bajan me recuerda a un balón desinflándose."

hi "¿Estás bien? Podría repasar esto si quieres."

"Hanako sacude su cabeza ligeramente, pero una vez más, no pienso que necesite explicaciones extra a pesar de lo que dijo."

"Misha rápidamente interviene, completamente ajena a eso, y termino yendo lentamente a través de uno de nuestros resultados, paso a paso."

"Momentos como este me recuerdan que este tipo de trabajo podría no ser mecánico para todos, sino que se siente así para mí por mi entendimiento del tema. Es un sentimiento satisfactorio."

"Mientras Misha convierte su puño cerrado en una mano abierta de entendimiento, descubro otra buena sensación. Mi explicación le llegó a ella, y se las arregla para hacer la siguiente ecuación ella misma con guía mínima."

"A lo largo de todo esto, Hanako está inusualmente inmóvil."

"Normalmente es muy tranquila, pero uno aún puede verla con sus ojos vagando periódicamente por la extensión del salón frente a ella, o revolviendo ansiosamente sus manos de alguna forma, o moviendo sus hombros periódicamente."

"Justo ahora, estos pequeños movimientos que me he acostumbrado a ver están todos ausentes. Alguien sin moverse en absoluto es definitivamente extraño. Incluso Misha puede darse cuenta de que hay algo mal."

show misha perky_confused_close
with charachange

mi "¿Hanako? ¿Estás segura de que estás bien?"

ha "S-sí…"

hi "¿Estás segura?"

show hanako emb_downsad_close
with charachange

ha "Estoy bien."

"Un poco más fuerte esta vez, pero ella gira al decirlo. Solo me hace dudar más de su respuesta, no obstante, al mismo tiempo puedo decir que ella no quiere hablar más de ello."

"Ya habiendo tenido hoy una conversación muy incómoda de la cual aún no estoy totalmente recuperado, tampoco quiero presionar más el tema."

"Volvemos a nuestras rutinas, debatiendo sobre nuestras respuestas siempre que hay alguna duda, pero conforme el tiempo avanza noto que Hanako no está hablando para nada. Es frustrante; había tenido mucho progreso."

"Me hace enojar un poco con Shizune y Misha deshaciendo la sorpresa que Lilly quería mantener tan en secreto. Sé que es mi culpa también. Tal vez podría haberlo mantenido oculto de alguna forma."

show shizu behind_frustrated_close at Position(xpos=0.85)
with charachange

"Shizune ha notado el silencio de Hanako también, y también se está poniendo nerviosa. Puedo verlo en su cara. Es extraño que incluso aunque es sorda, Shizune ha percibido la inusual inmovilidad de Hanako antes que Misha."

show shizu adjust_frown_close
with charachange

shi "…"

show misha sign_smile_close
with charachange

mi "Hanako, estás demasiado tranquila~. ¡Tienes que contribuir también~!"

mi "Algún día podríamos trabajar en un proyecto más grande, como uno tan grande que valga la pena celebrarlo después, como con helado o tarta. ¡Si actúas de esa forma, no te llevaremos con nosotros~!"

"Puedo notar que están tratando de molestarla para que salga de su caparazón, pero no creo que ese tipo de acercamiento vaya a funcionar en Hanako. Solo la hará sentir peor."

hi "Chicas, no bromeen así."

show shizu behind_smile_close
with charachange

shi "…"

show misha hips_smile_close
with charachange

mi "¡Hicchan, todo es en buen plan~! Shicchan dice que bromea con todos, de todas formas."

show misha perky_smile_close
show shizu behind_blank_close
with charachange

"Sin embargo, sí se detienen, Misha alejándose del problema haciéndome una pregunta otra vez. Al ver lo difícil que es el problema en el que está trabajando, no sé si fue un escape hábil o pura coincidencia."

"Nos toma más del tiempo necesario, porque Shizune se mantiene en desacuerdo conmigo mientras trato de explicar a Misha, y Misha es rápida en creerle a ella antes que a mí. Tan rápida, de hecho, que se olvida de traducir lo que Shizune está diciendo."

hi "Oigan, el reloj está avanzando. Deberíamos acelerar un poco."

stop music fadeout 4.0

show misha perky_confused_close
with charachange

mi "¡Hicchan~! Suenas un poco como Shicchan así…"

hi "¿Solo porque vi mi reloj? Rayos, ¿es eso en verdad todo lo que se necesita? ¿Administro el tiempo y de repente soy el presidente del consejo estudiantil?"

stop ambient fadeout 4.0

$ ksgallery_unlock("evul hanako_breakdown_down")
scene evbg hanako_breakdown:
    truecenter
    1.0
    zoom 1.05 subpixel True
    easein 8.0 zoom 1.0
show evfg hanako_breakdown_down:
    truecenter
    1.0
    zoom 1.1 subpixel True
    easein 8.0 zoom 1.0
with silentwhiteout

play music music_tragic fadein 8.0

"Volteo hacia el banco de Hanako para ver cómo le está yendo, y me congelo. Nuestros papeles están cubiertos de ecuaciones, pero el de Hanako está solo a mitad del camino. Parece que no ha escrito nada en los últimos veinte minutos."

"Cuando me doy cuenta de ello, quiero patearme a mí mismo por lo tonto que he sido."

"Debí haber sabido que alguien tan frágil como Hanako no iba simplemente a dejar pasar tan fácil lo que sucedió, pero he estado demasiado ansioso por moverme de una incómoda situación como para darme cuenta."

"Ella ha estado lentamente apagándose por la última media hora, y no he tenido idea. Su pluma aún está en su mano, pero no le da vueltas lentamente como usualmente lo hace. No hay ni un vago movimiento en Hanako."

$ ksgallery_unlock("evul hanako_breakdown_up")
scene evbg hanako_breakdown:
    truecenter
    1.0
    zoom 1.0 subpixel False
show evfg hanako_breakdown_up:
    truecenter
    zoom 1.0 subpixel False
with charachange

"Solo el hecho de que trata de alejarse poco a poco cuando nos siente a Shizune, Misha y a mí viéndola me dice que aún está consciente. Miramos a otro lado, y al menos en mi caso, en parte por vergüenza de que se haya llegado a este punto."

"Aunque por fuera casi se ha paralizado por completo, sé que por dentro es una historia completamente diferente."

"¿Qué tipo de cosas podría estar pensando mientras trata más y más fuertemente de encogerse en sí misma, como si al hacerlo pudiera de alguna forma desaparecer?"

"Todos están viéndola ahora, lanzando furtivas miradas mientras le dan los toques finales a sus trabajos."

"Misha intenta preguntarle qué sucede, pero eso solo hace el problema peor. Si no estuviera congelada en su asiento, probablemente correría fuera del cuarto justo ahora."

$ ksgallery_unlock("evul hanako_breakdown_closed")
show evfg hanako_breakdown_closed
with charachange

"Las preguntas de Misha son lo suficientemente fuertes para ser escuchadas a través de todo el salón, y por un segundo estoy listo para reprimirla, porque ya puedo imaginar cuán peor está haciendo sentir a Hanako."

"Desde luego, si llegara a hacer eso, solo haría la situación peor."

"Había creído que Hanako se había vuelto más fuerte, y así ha sido, pero no lo suficiente, y estaba demasiado entusiasmado para creerlo."

"Ahora, ella está aterrada, sola en medio del salón, y no hay nada que yo pueda hacer sin atraer más atención hacia ella."

"Es exasperante. Misha está preocupada, e incluso Shizune está mordiendo su labio."

"Ninguno de nosotros sabe cómo lidiar con esta situación, así que decido llamar a Mutou. Su juicio será probablemente mejor que el nuestro."

"Volteo y me las arreglo para captar su atención, indicándole silenciosamente que se acerque. Quiero hacer tan poco alboroto de esto como sea posible, dado que si hay algo que podría volver esto peor, es más atención enfocándose en ella."

"Sé que Hanako puede ver a todos mirando a nuestro grupo. Específicamente a ella. Porque saben que si hay algún problema, tiene que ser ella."

"Todos la conocen, y es la primera sobre la que la mente de cualquiera saltaría. Su reputación de faltar a clases la ha marcado como una persona inusual, aun en la inusual Yamaku."

"Quién sabe cuántas veces se le han quedado viendo antes. Tal vez es porque ha visto al grupo mirándola muchas veces que ella tiene el miedo que tiene a sus miradas."

"El tiempo que le toma a Mutou caminar hasta nuestro lugar debe ser como una eternidad para Hanako, y ella luce como si estuviera por caer."

scene bg school_scienceroom
show shizu behind_blank_close:
    tworight
    xpos 0.85 ypos 1.09
show misha perky_sad_close:
    twoleft
    xpos 0.15 ypos 1.09
show hanako emb_downtimid_close:
    center
    ypos 1.09
show muto irritated behind shizu at tworight
with dissolve

"Mutou tranquilamente comienza a preguntarnos qué sucede, antes de notarlo por sí mismo al ver a Hanako."

show misha perky_sad_close
with charachange

mi "¿La… la hicimos enojar…?"

show muto normal
with charachange

mu "No te preocupes."

"Mutou se inclina después de calmar a Misha y observa atentamente la cara de Hanako."

show muto smile
with charachange

mu "Hola, Ikezawa. ¿Puedo ayudarte en algo?"

"Su voz es muy baja y gentil. Todos están actuando muy diferente alrededor de Hanako ahora que la clase entera ha notado que sucede algo malo con ella."

show muto smile_close
with characlose

"Hanako no responde, así que Mutou descansa gentilmente una mano en su hombro."

show hanako emb_downsad_close at centertremble_sit
with charachange

"Ella comienza a temblar con el contacto, pero ni siquiera levanta la mirada. Hanako continúa viendo las ecuaciones en su banco, con una visión tan enfocada que dudo que las esté viendo."

"Está peor que antes. Recuerdo que no hace una hora atrás, ella podía hablarle casi normalmente."

show muto irritated
show hanako emb_downsad_close:
    center
    ypos 1.09
with charadistant

"Mutou hace una pequeña mueca mientras se levanta otra vez, y ahora que su expresión ha cambiado, puedo ver que tampoco está muy sereno con lo que pasó."

show muto normal
with charachange

"Él toma aire para calmarse antes de hablar en una voz muy tranquila. Estoy impresionado por lo rápido que toma el control de la situación."

mu "¿Eso es todo? ¿No sucede nada, entonces?"

play ambient sfx_crowd_indoors fadein 8.0

"Mutou parece no decirle eso a nadie en particular. Como sea, sus palabras suenan lo suficientemente convincentes como para que la mayoría de las personas que estaban viendo hacia Hanako se volteen, volviendo a su trabajo."

"Él da una mirada rápida a izquierda y derecha. Varias personas en los bancos alrededor aún están viéndonos con curiosidad, pero fuera de eso, parece que hemos escapado de atraer mucha atención."

show muto smile
with charachange

"Mutou me nota haciendo lo mismo que él y sonríe un poco, en su forma forzada usual."

mu "Creo, por el bien de Ikezawa, que sería bueno sacarla rápido a algún lugar lejos de los demás."

mu "Nakai, Hakamichi; ¿podrían por favor sacar a Ikezawa del salón? Mantendré a todos en sus lugares, así que por favor no se preocupen por nada más que por ella, ¿está bien?"

show misha sign_confused_close
show shizu behind_blank_close
with charachange

"Él voltea hacia Misha para decirle que interprete sus palabras para Shizune, pero ella ya está terminando su traducción para cuando lo hace. Es notable el poco esfuerzo mental que necesita para hacer señas, pues por lo demás aún luce un poco aturdida."

show muto invis
show misha perky_confused_close
show shizu behind_blank_close:
    xpos 0.85
    ypos 1.0
with dissolvecharamove

hide muto
hide shizu
with None

show shizu behind_blank_close behind hanako:
    tworight
    xpos 0.85
    ypos 1.0
with None

"Asintiendo, Shizune y yo nos movemos a cada lado de Hanako."

"Mutou da unos pasos atrás para darnos algo de espacio, y le habla a los bancos detrás de nosotros pues algunas personas ahí han comenzado a murmurar entre ellos sobre lo que está pasando."

show hanako emb_downsad_close at center
with charamove

"Nos vemos el uno al otro antes de agacharnos al unísono, pasar cada uno un brazo alrededor de nuestros hombros y levantarnos."

show hanako emb_downsad_close:
    twoleft
    xpos 0.35
show shizu behind_blank_close at tworight
show bg school_scienceroom at bgleft
show misha invis_close at Position (xpos=-0.1)
with dissolvecharamove

"Ambos comenzamos a caminar, a paso lento para asegurarnos de no lastimarla inadvertidamente."

"Por mucho que tratamos de hacer parecer esto normal, estoy bastante seguro de que habría muchas más miradas sobre nosotros de no ser por la distracción de Mutou."

"Eventualmente, por fortuna, alcanzamos la puerta y pasamos a través de ella."

stop ambient fadeout 0.5

scene bg school_hallway3
with locationchange

"No hay nadie afuera, así que caminamos a través del pasillo. No parece como si se estuviera calmando más de como estaba en el salón. Finalmente, le pregunto si quiere sentarse."

show shizu adjust_happy_close at tworight
show hanako emb_downsad_close:
    twoleft
    xpos 0.35
with charaenter

"Por un rato, simplemente permanecemos en el lugar y esperamos a que diga algo. Shizune tentativamente frota un poco el hombro de Hanako, pero no hay respuesta."

show shizu behind_smile_close
with charachange

"Eventualmente, ella sacude un poco su cabeza cuando Shizune intenta otra vez. Ambos estamos viéndola, así que lo captamos inmediatamente."

show shizu adjust_happy_close
show hanako emb_sad_close
with charachange

"La mano de Shizune pasa a descansar en el hombro de Hanako conforme despierta, su rostro elevándose hacia dos muy preocupadas y ansiosas personas viéndola."

"Ella nos mira en silencio por un rato."

"Al principio estoy preocupado de que podría perder el control o hacer algo extremo, pero esos miedos se muestran infundados mientras su expresión cambia lentamente de un estado casi blanco y sin vida a una retraída timidez más normal."

show hanako emb_downtimid_close
with charachange

"Sin decir palabra ella baja su cabeza, sus ojos moviéndose evasivamente a un lado. Luce incómoda, casi avergonzada."

"Quiero decir algo, lo que sea, para ayudarla. Pero no puedo. No sé realmente lo que pasó, o siquiera qué lo causó. Me siento impotente, y avergonzado de mí mismo por no ser de utilidad."

show shizu basic_normal2_close
with charachange

"Shizune suspira antes de verme a mí. Incluso sin palabras, creo poder saber lo que está preguntando."

hi "Llevaré a Hanako con el enfermero. ¿No tienes problemas con ello?"

"Trato de comunicar mis intenciones a través de gestos con las manos, pero siento que no logro llegar a ella muy bien."

show shizu behind_frustrated_close
with charachange

"Shizune hace una cara triste como respuesta a mis gesticulaciones, confirmando mi impresión."

show shizu adjust_frown_close
with charachange

"Ella apunta su dedo en el aire decisivamente, primero hacia mí, luego a Hanako, y luego hacia las escaleras. Ella espera a que yo asienta antes de señalarse a sí misma, luego señalar la puerta del salón."

"Tengo la sensación de que Shizune es mucho mejor en esto que yo."

show shizu behind_blank_close
with charachange

"Asiento, dado que su plan es el mismo que el mío después de todo. Shizune se prepara para partir, pero solo se va después de ver a Hanako por algo de tiempo."

hide shizu
with dissolve

hi "¿No te molesta si te llevo a la oficina del enfermero?"

stop music fadeout 4.0

"Hanako no dice nada ni asiente, sino que se levanta por sí misma en lugar de eso, y cuando comienzo a caminar me sigue obedientemente. He leído acerca de gente en estado catatónico antes, pero creo que esta es la primera vez que veo a alguien así."

"Luce extremadamente cansada. Después de todo lo que pasó, no es una sorpresa."

stop music fadeout 1.0
scene bg school_nurseoffice
with locationskip

"Después de que Hanako se quita silenciosamente sus zapatos y se recuesta en la cama de la enfermería, el enfermero y yo nos retiramos."

play music music_hanako fadein 0.3

"Él cierra la cortina detrás de nosotros. Ambos tomamos asiento, y lenta y minuciosamente cuento todo lo que sucedió, con bastante detalle."

"Quiero entender lo que pasó, y el enfermero tiene tan buenas posibilidades como cualquiera de saber."

show nurse concern at center
with charaenter

"Él asiente a lo largo de mi explicación, su rostro luciendo preocupado cuando termino."

nk "Debe haber sido muy problemático para ti haber visto todo esto."

hi "Estaría mintiendo si dijera que no. Entiendo que se quedó pasmada, pero realmente no comprendo nada del porqué sucedió o por qué ella actúa de esta forma."

"Él asiente, pero su rostro está nublado."

hi "¿No lo sabe tampoco?"

nk "Bueno… sí y no. Es complicado."

nk "Asumo que en algún momento has escuchado acerca del concepto de la confidencialidad de un paciente."

nk "Esto es un poco como un campo minado en ese sentido. Lo diré sin rodeos; este es un asunto entre Ikezawa, yo, y su terapeuta."

"Me muevo para protestar, pero lo pienso mejor. Quiero negar lo que dice, pero si pienso esto racionalmente, lo que dice tiene perfecto sentido."

hi "Entiendo."

show nurse neutral
with charachange

nk "Bien, bien. Desearía poder ayudarte más, pero pienso que lo que Ikezawa necesita justo ahora no es alguien espiando en su pasado o sus emociones. Solo necesita a alguien que esté ahí para ella."

nk "Necesita un amigo."

show nurse fabulous
with charachange

nk "En lo que a esto respecta, creo que has hecho bien en traerla aquí. Suena como que tus amigos y tú lidiaron bien con la situación, también."

show nurse grin
with charachange

nk "Te daría una paleta o una estampita como recompensa, pero tal vez estás un poco viejo para ambas."

"Él da una sonrisa arrogante, obviamente tratando lo mejor que puede de animar el ambiente. Realmente no estoy de humor como para reír, pero logra sacarme una sonrisa."

hi "Gracias. Em, ¿le molesta si me quedo aquí con Hanako?"

show nurse neutral
with charachange

nk "Aprecio esa idea, pero creo que lo mejor sería dejarla descansar por ahora."

nk "Se le dejará volver a su dormitorio esta tarde, así que podrías visitarla entonces."

"Concuerdo con él antes de levantarme. Se siente como si todo lo que puedo hacer siempre es humildemente concordar con lo que él dice, pero fue lo mismo con los doctores del hospital también."

stop music fadeout 3.0

scene bg school_nursehall
with locationchange

"La caminata de vuelta al salón es larga, con mi mente sintiéndose pesada bajo el peso de tantas cosas pasando al mismo tiempo."

scene bg school_scienceroom
with locationskip

play music music_dreamy fadein 2.0
$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0

"Incluso mientras entro de nuevo al salón, estoy pensando en Hanako."

"Mi estómago se siente como si se estuviera haciendo nudos mientras pienso en cómo lidiar con ella. Todavía no sé lo que voy a decir cuando la vea otra vez."

"Afortunadamente, el grupo no me presta mucha atención. Hay un par de miradas cuestionadoras, pero en general no muchas personas parecen estar conscientes de lo que sucedió."

"Mutou eleva sus cejas para llamar mi atención cuando paso por su escritorio."

show muto normal at center
with charaenter

mu "Nakai… supongo que Ikezawa está en la enfermería ahora."

hi "Sí. La llevé allí, y el enfermero dijo que la debía dejar descansar."

"Mutou asiente, asegurándome que hice lo correcto. Él rasca su barbilla por un segundo antes de levantarse de su escritorio."

show muto smile
with charachange

mu "Todos, quiero que continúen con su ejercicio. Nakai, te veré en el pasillo, por favor."

"Su discurso es tranquilo, pero en general no parece estar actuando muy diferente de como usualmente lo hace. Siendo maestro, tal vez eso es de esperarse."

stop ambient fadeout 1.0
scene bg school_hallway3
with locationchange

"Mientras salimos al pasillo, lo noto dando una rápida mirada a izquierda y derecha para revisar si hay algún estudiante molestando por ahí."

"El pasillo está casi en silencio, pero no puedo pensar en nada excepto en esperar a que Mutou hable."

show muto smile at center
with charaenter

mu "Nakai, ¿cuál piensas que es el propósito de esta escuela?"

hi "Emm… ¿atender las necesidades de los estudiantes discapacitados?"

show muto normal
with charachange

"Mutou rasca su cabeza mientras la sacude."

mu "No. Si hubiéramos querido hacer eso habríamos construido una nueva escuela desde cero. Un piso. Pizarrones parlantes. Esa clase de cosas."

mu "Mira alrededor, Nakai. Esta escuela es sobre darle a todos ustedes un futuro que les habría sido negado en educación regular."

hi "¿Eh?"

mu "Piénsalo de esta forma. Si quisiéramos que se graduaran y fueran derecho a un hospital, ¿crees que pondríamos tanto empeño en esto?"

"La franqueza de la declaración de Mutou me aturde temporalmente, haciendo que me olvide de la situación inmediata."

hi "No…"

mu "Es cierto. Queremos que todos ustedes se vayan de aquí como miembros útiles de la sociedad."

hi "No… no estoy muy seguro de estar entendiendo…"

show muto smile
with charachange

mu "Tengo grandes esperanzas en ti, Nakai. Eres posiblemente el primer estudiante que he tenido que entiende mis clases."

"Eso no es algo que un maestro debería estar admitiendo tan libremente."

mu "Bien podrías fácilmente tomar tus estudios de ciencia en la universidad. ¿Has considerado eso?"

hi "No puedo decir que lo he hecho."

mu "Bueno, ¿qué has considerado? Para tu futuro, quiero decir…"

hi "Yo… no puedo decir que haya pensado mucho en mi futuro."

"Por un momento recuerdo claramente a Lilly cuestionándome sobre el mismo tema."

"Han sido solo poco más de cinco meses desde que estuve en el suelo jadeando por falta de aire. Es demasiado pronto para estar pensando en el futuro, y además, los problemas de Hanako parecen mucho mayores en este momento."

show muto irritated
with charachange

"Mutou da un suspiro de desaprobación antes de continuar."

show muto normal
with charachange

mu "Piensa en este lugar como una oportunidad. Aquí tú tienes facilidades ilimitadas, buenos maestros, más el bonus añadido del enfermero y su personal."

mu "No debes estar haciendo nada más que pensar en tu futuro."

hi "Eh… cierto."

"Mientras levanto mi cabeza para encontrarme con su mirada, un pensamiento viene a mí; es casi como si Mutou hubiera hecho totalmente a un lado el problema actual."

hi "Perdón, pero ¿por qué nadie del personal parece preocuparse cuando Hanako se salta la clase?"

hi "Lo he observado viéndola caminar fuera de la clase más de una vez. ¿No debería al menos decir algo?"

show muto smile
with charachange

mu "Bueno, Nakai, no es realmente tan simple. Cada estudiante aquí tiene necesidades especiales; si no fuera por eso entonces no tendríamos una escuela aquí."

mu "Por ejemplo, no te mantendría en clase si tuvieras problemas para respirar, ¿o sí?"

hi "Pero eso no es…"

"Mutou me corta antes de poder siquiera pensar en terminar mi oración."

show muto normal
with charachange

mu "El caso de Ikezawa es bastante como eso. Pero en lugar de RCP o un marcapasos, lo que ella necesita es tiempo y espacio."

mu "La facultad advirtió esto desde el día en que ella arribó, por tanto cada vez que siente la necesidad de irse, le permitimos hacerlo."

show muto smile
with charachange

mu "E incluso si no es una alumna estrella, parece aprobar todos sus exámenes, así que no le ha afectado su habilidad para estudiar. ¿No es eso suficiente?"

"Abro mi boca para protestar, pero no puedo encontrar falla en su argumento. Mientras que su condición sí parece en un principio ser totalmente psicológica, sus peores efectos han sucedido en su psique."

"Sin embargo, aún no me agrada. ¿No está él únicamente pasando la responsabilidad por su problema? Sin duda ella no puede andar de esa forma por toda su vida."

show muto normal
with charachange

mu "Entiendo que puede que no estés acostumbrado aún a este tipo de cosas. Ha sido un gran cambio para ti. Dicho lo anterior, es menos de un año antes de la graduación."

mu "Tal vez no te acostumbrarás a esta escuela. Si mantienes tu cabeza abajo, estoy seguro de que lo harás lo suficientemente bien en tus exámenes."

"Asiento aturdido, más para simplemente hacer saber que estoy escuchando que en señal de acuerdo. Tenía la sensación de que me estaba acostumbrando a esta escuela, pero se siente como si solo se me hubiese sido lanzada de vuelta en la cara."

hi "Pero… ¿qué hay de Hanako?"

mu "Creo… bueno, espero, que lo hará lo suficientemente bien como para hacer lo que ella quiera."

mu "Qué es eso, no lo sé. No todos los estudiantes dejan la escuela con una idea de qué es lo que quieren hacer, desafortunadamente."

"Se toma el cuidado de enfatizar la última palabra, como si no estuviera ya lo suficientemente claro, y me da un momento para darle vueltas a sus palabras."

show muto smile
with charachange

mu "Hoy ha sido un día problemático para ti, y en verdad dudo que podrías concentrarte mucho de cualquier forma después de todo lo que sucedió, así que te permitiré tomarte el resto del día libre."

mu "Tus calificaciones han sido buenas en esta clase hasta ahora, lo que me hace pensar que no tendrás ningún problema en alcanzarnos en lo que hemos estado haciendo."

"Me da una pequeña sonrisa junto con su elogio, como para compensar por la seriedad de su sermón antes de esto."

mu "Ve, junta tus cosas y te veré mañana."

hi "Bien. Gracias."

stop music fadeout 5.0

hide muto
with charaexit

"Su indirecto discurso dejó mis pensamientos dispersos. Aún no logro acercarme a entender qué puedo hacer para ayudar a Hanako, si es que hay algo, y mi mente está todavía más confundida luego de lo que Mutou dijo."

"También estoy aún molesto por el hecho de que Hanako fue ayudada por lo menos igual por Shizune, su enemiga por asociación, que por mí, pero no sé si eso es solo bravuconería de macho o preocupación genuina."

scene bg school_scienceroom
with locationchange

"Mientras junto las cosas de Hanako y las mías del salón, continúo intentando ordenar mis sentimientos."

"Quiero decir que la entiendo, y que estoy ahí para ella… pero mientras podría haber dicho eso apenas ayer, no puedo decirlo ahora."

"Desearía que pudiera."




label es_H15:

scene bg school_dormhisao_ss
with shorttimeskip

play music music_night fadein 1.0

"Yazgo en mi cama, tratando de juntar mis pensamientos."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

nvl clear
window hide
nvl show dissolve

n "\n\nDespués del ataque de pánico de Hanako, me he encontrado revalorando la relación que compartimos, y lo que sé de ella."

n "Tuve un momento lo suficientemente difícil lidiando con cuatro meses en el hospital. Una mirada a sus cicatrices me dice que ella estuvo en uno por más tiempo que yo."

n "Sea como fuere, prácticamente no sé nada de su pasado. Me ha dicho acerca de la casa en llamas, pero solo de la forma más básica."

n "¿Y qué hay de su familia? Aún no le he preguntado a Lilly sobre ellos; no ha habido una buena oportunidad de hablarlo."

n "No sé dónde creció, o cómo era su escuela anterior. Ni de sus amigos anteriores, sus deseos y ambiciones. Ni siquiera sus gustos en música, comida y películas… todas las pequeñas cosas sobre las que yo sabía de todos mis viejos amigos."

n "\n\n¿Qué es lo que he estado haciendo, en todo este tiempo en el que he estado con ella y Lilly?"

$ renpy.music.set_volume(1.0, 1.0, channel="music")
$ renpy.music.set_volume(0.1, 0.0, channel="sound")
play sound sfx_normalbell

nvl clear
nvl hide dissolve
window show

"En la distancia, escucho las campanas señalando el final de las clases. Con un poco de suerte, Lilly pronto se dará cuenta de que ni Hanako ni yo estamos por ahí, y regresará a los dormitorios."

$ renpy.music.set_volume(0.5, 0.0, channel="sound")
stop music fadeout 0.5
play sound sfx_phone

"Mi teléfono móvil empieza a sonar, cortando mis pensamientos pronto. Me sorprende un poco, pues casi nunca he sido llamado desde que vine a Yamaku."

scene bg school_dormhisao_blurred_ss
show phone mobile:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with locationchange
with Pause (0.5)

hi "Hola, Hisao Nakai al habla…"

li "Oh, Hisao, qué bueno que te encuentro. No estabas en ninguno de nuestros lugares usuales, así que pensé que esta sería la forma más rápida de contactarte."

"Probablemente debí imaginar que sería Lilly, dado que ella es una de las pocas personas a las que les he dado mi número. Incluso a través del teléfono, su voz suena ligeramente nerviosa."

hi "Yo… Hanako y yo dejamos la clase temprano. Ella tuvo una especie de ataque de pánico…"

"La línea se torna en silencio. Si no fuera por la estática de fondo, habría pensado que Lilly me había colgado."

li "Entiendo. ¿Podrías venir a mi cuarto? Quisiera hablar contigo."

hi "Seguro. Yo… apreciaría la oportunidad de tener un poco de charla, de hecho."

li "Bien… bien. También… tengo algunas malas noticias. Pienso que debemos discutir esto en persona."

"Es difícil captar la seriedad de la situación por el tono de voz de Lilly. Suena tan calmada todo el tiempo, pero eso podría ser algo bueno o malo, dependiendo de la situación."

hi "Está bien, estaré ahí de inmediato."

show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with None

scene bg school_dormhisao_ss
show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with locationchange
with Pause (0.5)

hide phone
with None

"Junto las cosas de la escuela de Hanako de mi banco y me dirijo a la habitación de Lilly."

scene bg school_girlsdormhall
with locationskip

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_doorknock2

"Golpeo mis nudillos en su puerta, y al poco tiempo ella me invita a pasar."

play music music_drama fadein 4.0

scene bg school_dormlilly
show lilly basic_sleepy:
    center
    ypos 1.17
with locationchange

"Lilly se sienta en su mesa dentro de su cuarto, luciendo algo desgastada; supongo que es por las malas noticias."

"Siguiendo su gesto de invitación, me siento frente a ella y dejo las cosas de Hanako en la mesa."

show lilly basic_weaksmile
with charachange

li "Bueno, no hay razón para que ninguno espere. ¿Te importaría hablar primero, Hisao? ¿Qué sucedió hoy?"

"Mi recuerdo del incidente está ya comenzando a disolverse, pero se lo explico lo mejor que puedo a Lilly."

"La invitación a Hanako para trabajar con el equipo, Shizune y Misha preguntando, nuestra incursión a la ciudad descubierta, y el subsecuente ataque de pánico."

"Añado la reacción de Shizune casi como algo adicional, pero Lilly parece recibir un poco de consuelo al escucharlo."

"Supongo que las rivales no se vuelven rivales por nada. Debe haber algo de historia ahí, pero ahora no es el momento de explorarla."

show lilly basic_concerned
with charachange

li "Ya veo. Había dicho que sus sesiones con el terapeuta estaban ayudando, pero tenía mis dudas. Es una pena."

show lilly basic_reminisce
with charachange

li "Su cumpleaños ha causado problemas antes, pero había esperado que mejoraría contigo a su alrededor, y la terapia más intensa."

show lilly basic_oops
with charachange

li "¿Dónde está Hanako ahora?"

hi "La última vez que la vi estaba en la enfermería. Supongo que para esta hora ya ha vuelto a su cuarto."

show lilly basic_sleepy
with charachange

li "No estaba en la biblioteca o el cuarto de té cuando revisé, así que solo puedo asumir eso también."

hi "También dijiste que tenías algunas malas noticias… ¿Qué sucede? ¿Tienen que ver con Hanako?"

"Lilly cambia su posición; la forma del cuerpo de decir que ella está buscando las palabras correctas."

show lilly basic_concerned
with charachange

li "Mi tía ha caído gravemente enferma. Me temo que tendré que volver a Escocia a visitarla, y para pasar algún tiempo con mi familia."

hi "¿Qué? ¿Está ella bien? ¿Cuándo te vas?"

show lilly basic_reminisce
with charachange

li "No estoy del todo segura de exactamente cómo se encuentra en este momento, pero lo último que escuché es que estaba estable. Me iré el sábado; es el vuelo más cercano que pude conseguir."

"“Estable”. Ese es el código para “necesita quedarse en el hospital”."

"He estado “estable” lo suficiente como para saber eso, y para saber que no necesariamente significa que alguien está en buenas condiciones, sino meramente en un punto muerto."

"En el lado bueno, “estable” es mucho mejor que “condición crítica”. Al menos no está al borde de la muerte."

hi "Estable… eso es un alivio."

show lilly basic_sad
with charachange

li "Sí, pero esto significa que no estaré aquí para el cumpleaños de Hanako."

show lilly basic_concerned
with charachange

li "Te lo quería decir ahora para que pudiéramos pensar en algo antes de decirle a Hanako, pero después de los eventos de hoy, no estoy siquiera segura si habría algún problema si simplemente cancelamos la fiesta."

hi "Yo… no creo que esa sea una buena idea. Hanako ya sabe que estamos planeando una fiesta; echarse para atrás en eso parece lo peor que se puede hacer."

hi "Además, tenemos que hacer algo por tu partida, ¿cierto?"

show lilly basic_weaksmile
with charachange

li "Lo haces sonar como si no fuera a regresar. Si todo sale bien, solo debería estar fuera por una semana, aunque posiblemente sean dos."

hi "Eso es un alivio, al menos."

show lilly basic_oops
with charachange

li "Con eso en mente, ¿qué sugieres entonces?"

hi "Dadas las circunstancias, no creo que el karaoke sea realmente apropiado. No te estás yendo por las mejores razones, así que divertirse mucho se sentiría mal."

hi "¿Qué hiciste para su cumpleaños el año pasado?"

show lilly basic_reminisce
with charachange

li "El año pasado… literalmente no pude sacarla de su habitación. Cerró con seguro la puerta."

li "Todo lo que pude hacer fue dejar comida afuera para ella, asegurándome de que al menos estaba comiendo bien."

"Esto es tal vez lo más deprimida que he visto y escuchado a Lilly actuar. Me siento mal por ella, dado lo derrotada que debe sentirse por no poder ayudar a su amiga más cercana."

hi "¿Tal vez sería mejor dejar caer la fiesta antes de que te vayas, entonces?"

show lilly basic_weaksmile
with charachange

li "Eso suena como que sería la opción más sencilla."

hi "Pienso que al menos deberíamos decirle a Hanako, sobre ambos, tu viaje y su fiesta. Tengo sus cosas de la clase también."

show lilly basic_smile at center
with dissolvecharamove

li "Ese es un buen punto. ¿Deberíamos ir y visitarla ahora?"

hi "Creo… creo que eso sería una buena idea."

"Parte de mí está muriendo por ver a Hanako. La última vez que la vi lucía como una muerta andando, y estas últimas horas me han destrozado solo pensando en ello."

stop music fadeout 4.0

scene bg school_girlsdormhall
with locationchange

"Tranquilamente nos levantamos y salimos de la habitación de Lilly. La de Hanako está a un lado en el mismo corredor."

play sound sfx_doorknock2

"Tocar gentilmente no nos da respuesta, pero la puerta prueba estar sin seguro. Lilly se detiene por un momento cuando la perilla se mueve inesperadamente bajo su mano, antes de abrir la puerta."

play music music_moonlight fadein 0.5

scene bg school_dormhanako_ni at Fullpan(8.0)
with locationchange

"El cuarto de Hanako es inesperadamente vacío y monótono. No hay decoraciones en las paredes desnudas, una plana manta azul oscuro, y solo unos pocos libros, papeles, y objetos puramente utilitarios en los estantes."

"Incluso sus cobijas son monocromáticas. El cuarto entero se siente tan apagado como el carácter de Hanako."

scene ev hanako_cry_closed
with whiteout

"Hanako yace acurrucada en su cama. Puede que no esté llorando en este momento, pero sus ojos están fuertemente cerrados para no hacerlo, y los caminos dejados por sus lágrimas aún se muestran en sus enrojecidas mejillas."

"Silenciosamente entro y coloco la mochila en su escritorio, temeroso de sobresaltarla demasiado."

li "Hola, Hanako. Hisao me contó acerca de lo que pasó hoy… ¿estás bien?"

show ev hanako_cry_away
with charachange

"Los ojos de Hanako se abren, pero solo un poco."

ha "Estoy… estoy bien…"

show ev hanako_cry_open
with charachange

"Ella inclina su cabeza ligeramente para verme, notando mi mueca antes de poder ocultarla."

ha "P-perdón… p-por p-preocuparlos."

show ev hanako_cry_closed
with charachange

ha "E-en verdad… estoy b-bien ahora…"

"Realmente no luce ni suena bien, aunque al menos luce más calmada de lo que estaba antes. Aún parece como si el más ligero suspiro pudiera romperla emocionalmente."

hi "Lo dije antes, ¿cierto? No necesitas lamentarte por esto."

li "Hisao está en lo cierto. Nosotros… yo… no debí ocultarte algo como una celebración de cumpleaños."

"Veo a Hanako estremecerse con la palabra. Lilly reacciona en el silencio que sigue, y se agacha al nivel de Hanako."

li "Soy la única que debería sentirlo, Hanako."

show ev hanako_cry_away
with charachange

"Los ojos de Hanako se abren para mirar a Lilly. Ella ve a Lilly por un tiempo, asimilando su rostro con esos oscuros, y analíticos ojos de ella."

play sound sfx_rustling

scene bg school_dormhanako_ni
show hanako emb_downsad_ni:
    center
    ypos 1.3
    easein 1.0 ypos 1.15
with locationchange

"Lilly debe haber hecho la impresión correcta en ella, pues Hanako se recupera lo suficiente para levantarse de la cama y pasar a sentarse a su lado. Hanako se preocupa de muchas cosas, pero molestar a otros está por delante de ellas."

show bg school_dormhanako_ni at bgright
show hanako emb_downsad_ni:
    xpos 0.6
    ypos 1.15
with charamove

show lilly invis:
    twoleft
    xpos 0.4
with None

show lilly basic_weaksmile_ni at Position(ypos=1.17)
with dissolvecharamove

"Al escuchar el movimiento de Hanako, Lilly se mueve adelante y tienta la orilla de la cama, eventualmente tomando asiento junto a ella y tomando la mano izquierda de Hanako entre las suyas."

"El sentimiento de estar fuera de lugar cuando las dos están juntas ha disminuido en el tiempo que nos hemos conocido, pero aún está ahí ocasionalmente. Este es uno de esos momentos, creo."

hi "Lilly, si quieres que me vaya…"

show hanako emb_sad_ni
with charachange

ha "Yo no… quiero eso…"

show lilly basic_surprised_ni
with charachange

"Lilly y yo estamos sorprendidos por Hanako armándose de coraje. Un medio murmurado “Bien” es todo lo que puedo darle como respuesta, y tomo su silla del escritorio para sentarme."

show lilly basic_concerned_ni
with charachange

li "Hanako, me temo que tengo algunas malas noticias."

"Así que Lilly revelará las noticias ahora. Con Hanako habiendo afirmado nuestra relación tan claramente, tal vez Lilly pensó que el momento era bueno, o al menos, tan bueno como podrá ser."

show lilly basic_sad_ni
with charachange

li "Mi tía se ha enfermado, así que necesito regresar con mi familia por un tiempo."

show hanako cover_worry_ni
with charachange

"La preocupación reemplaza la expresión de remordimiento de Hanako."

ha "Tu… familia… Quieres decir en Escocia, ¿cierto?"

show lilly basic_reminisce_ni
with charachange

li "Eso es cierto. Akira y yo estaremos partiendo el sábado."

show hanako defarms_strain_ni
with charachange

ha "E-entonces ¿te vas?"

show lilly basic_weaksmile_ni
with charachange

li "No me iré por mucho tiempo. Probablemente una semana o dos. Estaré de regreso antes de que te des cuenta, además Hisao estará aquí, ¿cierto?"

hi "Eso es cierto, no voy a ir a ningún lado."

show hanako basic_worry_ni
with charachange

"Hanako parece recibir poco consuelo de esto, pero al menos se las arregla para convocar una resolución de algún lugar dentro suyo."

ha "¿E-estará bien tu tía?"

show lilly basic_reminisce_ni
with charachange

li "No estoy segura."

"El silencio cae. Es deprimente que lo que realmente saca a Hanako de su estancamiento es el infortunio de otro."

"Decido dejar salir el otro asunto que nos trajo aquí, para alejar al menos en parte el tétrico sentimiento impregnando el cuarto."

hi "Como sea, estábamos pensando que sería una buena idea tener una fiesta de despedida para Lilly, y podría servir también como… bueno…"

"Me corto antes de mencionar su cumpleaños, dado que eso parece ser un gatillo para emociones muy fuertes dentro de ella."

"Lilly le da a Hanako un gentil apretón."

show lilly basic_weaksmile_ni
with charachange

li "¿Está bien por ti, Hanako? No será nada espléndido ni exagerado, solo algo pequeño en mi cuarto."

show hanako def_worry_ni
with charachange

ha "¿E-entonces solo en la escuela? ¿Solo nosotros?"

show lilly basic_smileclosed_ni
with charachange

li "Es correcto, solo nosotros tres. Si gustas, puedo pedirle a Akira que venga también."

show hanako basic_normal_ni
with charachange

ha "Está… bien. ¿S-solo te vas por una semana?"

show lilly basic_smile_ni
with charachange

li "Una semana o dos, sí. Te prometo que no tomará más tiempo."

show hanako cover_distant_ni
with charachange

ha "B-bien…"

"La mayoría de la gente estaría enojada al escuchar que un miembro de la familia de un amigo se ha enfermado y feliz por lo de tener una fiesta, pero con Hanako parece que ambos eventos están en el mismo nivel."

hi "Todo bien entonces. Parece que necesitas un descanso, Hanako, así que lo mejor sería tal vez que todos regresemos a nuestras habitaciones por ahora."

show lilly basic_weaksmile_ni
with charachange

li "Sabes que si alguna vez quieres algo, siempre puedes hablar conmigo o Hisao, ¿verdad?"

"La voz de Lilly es meditabunda, un borde inusual para alguien tan segura en sí misma como ella."

show hanako basic_bashful_ni
with charachange

ha "Yo… entiendo. Gracias, Lilly, Hisao."

show lilly basic_smileclosed_ni at Position(ypos=1.0)
with dissolvecharamove

li "Bueno entonces, buenas noches, Hanako."

show hanako basic_normal_ni
with charachange

ha "Noches…"

stop music fadeout 4.0

scene bg school_girlsdormhall
with locationchange

"Dejo salir un largo suspiro después de que la puerta se cierra tras nosotros. Se siente un poco como que he estado muy profundo bajo el agua, y solo ahora he podido subir por aire."

show lilly basic_concerned at center
with charaenter

"A Lilly no parece estarle yendo bien tampoco. Luce pálida y demacrada."

hi "¿Estás bien?"

li "Solo estoy un poco cansada. Ha estado… ajetreado últimamente."

hi "¿Has dormido siquiera? “Un poco cansada” luce como que lo estás subestimando, por cómo te ves."

show lilly basic_sleepy
with charachange

li "Creo que me las arreglé para obtener un par de horas de sueño antes de clase. Estaré bien."

"Me siento mal por presionar a Lilly justo ahora. Creo que ambos estamos bastante cansados por todo lo que ha pasado."

hi "Creo que debes descansar un poco. Ha sido un largo día, y permanecer despierta no es bueno para tu complexión."

show lilly basic_weaksmile
with charachange

li "Gracias por tu preocupación, Hisao. Buenas noches, entonces."

hi "Está bien. Buenas noches, Lilly."

hide lilly
with charaexit

"Dejo a Lilly en el corredor mientras abre la puerta a su habitación, y comienzo a caminar hacia la mía."

scene ev hanako_cry_closed_fb
show noiseoverlay
with flash

"Mientras camino a través del tranquilo corredor, no puedo sacar esa imagen de Hanako de mi cabeza. Acurrucada y digna de compasión, yaciendo indefensa con lágrimas en sus mejillas."

"Empecé a pensar que ella solo era una persona normal, acaso extremadamente tímida, pero sus problemas van mucho más allá."

"Tratar de llevar nuestra relación a más de lo que compartimos ahora, cuando es tan frágil y vulnerable, no estaría bien. No necesito ser más que su amigo para poder protegerla, para intentar evitar que nada como esto suceda otra vez."

"La posibilidad de mis sentimientos yendo más allá de eso… no importa más. Hanako es valiosa para mí, y ese es el porqué no puedo aprovecharme de ella."

"Pero incluso así… aún está esa espinita que siento cuando pienso de esa forma."

scene bg school_girlsdormhall
with flash

"Por ahora, necesito dormir. Mañana, espero, será un mejor día."

scene black
with dissolve



label es_H16:

scene bg school_scienceroom
with locationchange

"Hanako es más perceptible en su ausencia que cuando está en el lugar."

"Siento que su escritorio vacío me está llamando. Me encuentro mirando sobre mi hombro sin descanso, esperando estar alucinando y que Hanako aparezca mágicamente."

"Ella se asegura de ser una presencia tan pequeña como es posible cuando asiste a clase, y aunque había estado mejorando recientemente, el hecho nunca cambió."

"Nadie le presta nada de atención jamás, y ahora que no está aquí, no notan su ausencia. Es como si nunca hubiera existido."

"Lilly sí dijo que el saltarse clases no era algo inusual en ella antes de que la conociera, pero aún es muy molesto."

play sound sfx_normalbell

"Las campanas anunciando el fin de la escuela me hacen saltar de mi asiento. Es solo ahora que noto que Misha me está pinchando a un lado con su lapicero para llamar mi atención."

show shizu invis:
    center
    xpos 0.4
show misha invis_close:
    center
    xpos 0.1
with None

show bg school_scienceroom at bgright
show misha sign_smile_close at Position(xpos=0.2)
show shizu behind_blank at center
with dissolvecharamove

play music music_normal fadein 3.0

mi "Hola… ¿hay alguien ahí~?"

hi "Oye, detente."

show misha hips_grin_close
with charachange

mi "¡Ah! ¡Ahí está! ¡Bienvenido de vuelta a la Tierra, Hicchan~!"

hi "¿De qué estás hablando?"

show misha hips_smile_close
with charachange

mi "Sigues soñando despierto; estaba empezando a creer que tratabas de comunicarte con alienígenas."

"Realmente no dormí mucho anoche, así que no dudo de las palabras de Misha. No estoy seguro si fue por los efectos secundarios de las medicinas, el ataque de pánico de ayer de Hanako, mi preocupación general por ella, o las tres juntas."

"Bostezo cansado antes de descansar mi barbilla en mi palma, al recordar lo mal que dormí."

show misha perky_confused_close
with charachange

mi "Oye, ¿en verdad estás bien? El día de ayer también me puso algo nerviosa…"

hi "Sí… sí, supongo. Aunque, quería hablar con Hanako otra vez."

show misha perky_smile_close
with charachange

mi "¿La viste anoche?"

hi "Sí, Lilly y yo le hablamos."

hi "Um, esto podría sonar un poco raro, pero ¿podrías decirle a Shizune “gracias”? De parte de ambos, yo… y Lilly."

"Sé que Lilly técnicamente no agradeció a Shizune, pero puedo decir por su reacción de anoche que es lo que quería. Al menos, así es como se ve en mi cabeza."

show shizu adjust_blush
with charachange

show shizu cross_angry
with charachange

shi "…"

show misha sign_confused_close
with charachange

mi "Eh… creo que lo que Shicchan está tratando de decir es “no fue nada”."

"Las furiosas señas y las mejillas sonrojadas de Shizune me hacen saber que lo que dijo fue completamente diferente. Su descarada expresión nerviosa es lo suficientemente divertida como para hacerme reír."

show misha perky_confused_close
with charachange

mi "¿Qué es tan gracioso, Hicchan~? ¿Fue algo que dijimos?"

hi "No, no, no es eso. Simplemente estaba pensando en lo linda que Shizune puede ser a veces."

show misha cross_laugh_close
with charachange

mi "¡Guajajaja~! ¡Estás en lo cierto~! ¡Shicchan es realmente linda cuando trata de no serlo!"

"Noto que Misha decide no traducir su respuesta a Shizune. Tal vez la cólera de Shizune es suficiente contraataque para cualquier cantidad de “linda”."

show shizu adjust_frown
with charachange

"No obstante eso, Shizune rápidamente se tranquiliza y hace unas señas más a Misha."

show shizu behind_smile
with charachange

shi "…"

show misha perky_smile_close
with charachange

mi "¿Oh~? Está bien… Hicchan, Shicchan quiere que vengas y cenes con nosotras."

hi "Cena, ¿eh?"

"Desviando mi mirada de ellas un poco, por miedo a ser persuadido por sus suplicantes sonrisas, empiezo a reflexionar."

"La invitación ciertamente es tentadora. Una cena fuera con lindas chicas no es algo malo, después de todo. La idea de Hanako encerrada en su cuarto, sin embargo, continúa bailando en mi cabeza."

hi "Lo siento, tendré que pasar."

show misha perky_sad_close
with charachange

mi "Oooh…"

show shizu behind_frown
with charachange

"Misha no traduce mi respuesta, pero Shizune la capta fácilmente y hace una mueca de decepción."

show shizu basic_normal2
with charachange

"Ella mueve sus brazos, presumiblemente empezando alguna forma de protesta o coacción, pero se detiene y golpetea el hombro de Misha dos veces."

"Una vez que Misha le da a Shizune su atención, la única declaración que tiene sobre el asunto es un encogimiento de hombros."

show misha perky_confused_close
with charachange

mi "Oh bueno. Es tu elección, Hicchan."

hi "Les prometo que me uniré a ustedes en otra ocasión, si eso ayuda."

show misha perky_smile_close
show shizu behind_blank
with charachange

"Misha se anima con esto, pero Shizune no comparte su reacción. Con un movimiento rápido de su cabeza para señalar a Misha que siga su camino, Shizune simplemente eleva su mano para silenciosamente decirme adiós."

hide misha
hide shizu
with charaexit

stop music fadeout 3.0

"Mientras las dos se dirigen hacia la puerta, regreso el gesto hasta que están fuera de vista."

"No pensé que estarían tan decepcionadas, y me hace sentir un poco mal por abandonarlas. Aun así, tengo cosas que hacer."

scene bg school_girlsdormhall at right
with shorttimeskip

"El dormitorio de chicas está especialmente ruidoso hoy, con varias chicas jugando juegos escandalosamente y viendo televisión en la habitación común en el primer piso."

"Puedo escuchar sus voces aun ahora, estando de pie frente a la puerta de Hanako."

"Es un contraste extraño con el vacío del piso en el que está. Las voces de abajo hacen que el vacío se sienta aún más solitario."

"Tenía esperanzas de que Hanako estaría en clase hoy, especialmente después de la charla conmigo y Lilly la otra noche, pero siento que no debería echárselo en cara."

"Fue un episodio bastante malo, y haberlo experimentado de primera mano debió haber sido peor."

scene bg school_dormhanako_ni
show hanagown worry_close:
    center
    xpos 0.39
show expression Solid("#00000022")
show hanako_door_base at right
show hanako_door_door at left
with locationchange

play sound sfx_doorknock2

"Al no saber en qué estado está, tomo un pequeño suspiro antes de dar unos pequeños golpes claros en su puerta café."

"Todo lo que puedo hacer es pararme y esperar, haciendo lo mejor posible por no sentirme ansioso."

"Conforme los segundos pasan, empiezo a pensar que podría estar dormida y no me escuchó tocar. Pero la manija de la puerta cruje un poco antes de que pueda levantar mi mano para tocar otra vez."

play sound sfx_dooropen

show hanako_door_door:
    xpos -0.05
with charamove

"La puerta apenas se abre, un ojo aparece por el hueco apenas del tamaño suficiente para mirar a través de este. Estoy seguro de que esta chica instalaría una mirilla en su dormitorio, tan solo si tal cosa estuviera permitida."

"Solo permanezco de pie y le sonrío. No creo que las palabras ayudarían realmente aquí, después de todo."

"El acto es devuelto en forma parecida, con Hanako sin decir palabra mirándome. El hueco no es lo suficientemente ancho para ver su expresión, y solo puedo suponer lo que está pensando."

"El tiempo pasa mientras nos vemos el uno al otro, siendo el único sonido la alegría sin dueño del piso de abajo."

hide hanagown
with charaexit

"No estoy seguro de cuánto toma, pero eventualmente el ojo se retira. Permanezco preguntándome si me dejará entrar o si se encerrará, hasta que la puerta lentamente comienza a abrirse crujiendo."

play sound sfx_door_creak

show hanako_door_door:
    easeout 1.0 xpos -0.2
show hanako_door_base:
    easeout 1.0 xpos 1.1
show bg school_dormhanako_ni:
    center
    easeout 1.0 xpos 0.55
with None

scene bg school_dormhanako
show hanagown normal at center
with silentwhiteout

play music music_comfort

"Ahora que tengo una vista completa de ella y la cama detrás de ella, la primera cosa que noto es que Hanako está algo húmeda. Se bañó recientemente, lo cual se hace más obvio por el aroma de champú flotando hacia mí."

"La mirada en su rostro parece de curiosidad, como si no estuviera segura de qué pensar de mí. Aun así, no estoy realmente seguro de qué es lo que está pensando."

"Se siente como si se hubiera ido por mucho tiempo, y habiendo regresado ahora, ninguno de los dos sabemos qué decir al otro."

show hanagown distant
with charachange

"Hanako se da cuenta de que está mirándome, ella dirige sus ojos a otro lado incómodamente antes de girar a un lado y ver a sus pies."

"Decido tomarlo como una invitación y paso a su lado hacia dentro del cuarto, cerrando la puerta tras de mí mientras lo hago."

"Puedo ver sus manos jugueteando en los pliegues de su camisón extragrande que cuelgan de sus hombros. Trato de concentrarme en lo que quiero decir, pero su aroma confunde mis sentidos."

"Para mi sorpresa, no soy yo, sino Hanako la que rompe el silencio."

show hanagown normal
with charachange

ha "¿Por qué…?"

hi "Porque… eh…"

"… ¿Por qué vine aquí?"

"Estaba preocupado por Hanako, así que vine a su habitación. Me dejó entrar, como había esperado, y luego… ¿qué? ¿Qué planeaba hacer? ¿Qué planeaba decir?"

"Por qué no pensé en todo esto antes de venir aquí…"

"Quiero recompensarla por lo que creo que siento que yo causé, al menos parcialmente. Quiero intentar eliminar la distancia que siento entre nosotros desde entonces, y verla feliz."

"¿Cómo puedo hacer eso cuando no sé ni el principio sobre ella?"

"Me pregunto… me pregunto si es así como Iwanako se sintió cuando me vio yaciendo en esa estéril y azul pastel cama de hospital."

hi "Yo eh… yo… em…"

"Un profundo suspiro calma mis nervios un poco y acaba con mi tartamudeo."

"No creo que me haya sentido así de nervioso junto a alguien antes. Cuando estoy así, no creo poder mentir. Incluso si pudiera obligarme a hacerlo, Hanako vería a través de ello al instante."

hi "No lo sé. Solo… quería verte, creo."

show hanagown smile
with charachange

"Sus dedos dejan de moverse, dándome una pequeña sorpresa. Mirando hacia su cara, ella me da una dulce sonrisa y asiente con la cabeza. ¿Esa fue una respuesta satisfactoria para ella?"

ha "Em… ya que estás aquí…"

show hanagown distant_blush
with charachange

ha "Me gustaría… jugar una partida de ajedrez contigo…"

"Casi agacho mi cabeza sin poder creer que todo lo que quiere hacer, después de torturarme tanto, es jugar un juego. Sin embargo, al mirar su cara, una cautelosa sonrisa se ha asentado en ella, me doy cuenta de que esto es más que eso."

"Ella podría no haberse molestado en contestar la puerta. Podría haberse encerrado tan pronto como vio mi cara. Podría haberme pedido que me fuera."

"Podría haberme rechazado en muchos puntos, pero no lo hizo. Ahora, con este rostro calmado, quiere que juguemos el mismo juego que jugamos cuando realmente pasamos tiempo juntos por primera vez."

"Un sentimiento de alivio me invade."

"Todo estará bien. Hanako me ha dejado entrar a su mundo. Mientras podamos estar juntos de esta forma, pienso que todo estará bien."

hi "Sería un placer."

stop music fadeout 2.0

scene black
with dissolve



label es_H17:

scene bg school_girlsdormhall
with locationchange

"El día de la fiesta de Hanako está finalmente aquí."

"Para ser honesto, espero con ansias ver a Hanako y Lilly en sus pijamas otra vez."

"El camisón de Hanako se ha plantado en mí como algo que luce más bien lindo, aunque algo conservador, y los shorts de Lilly y la parte de arriba de seda son una combinación encantadora."

"Pero el evento está manchado un poco con el recuerdo de la reacción de Hanako a este."

"Aún no entiendo realmente lo que sucedió, solo pudiendo suponer vagamente las posibles razones de ello, pero no creo que encontrar la respuesta vaya a ser tan directo como preguntarle a ella."

play sound sfx_doorknock2

"Con eso en mente, toco en la puerta enseguida de la de Hanako."

li "¿Eres tú, Hisao?"

hi "Sí, soy yo."

"Puedo escuchar el sonido de unas pisadas viniendo a la puerta, seguido del sonido del seguro abriéndose. No creo haber visto antes la puerta de Lilly cerrada con seguro, y me hace sentir sospecha."


"Una vez que se abre la puerta, la vista es… un poco fría para una fiesta de cumpleaños."

play music music_ease fadein 1.0

scene ev lilly_bedroom
with locationchange

"Hanako regresa a su asiento en la mesa con una rápida sonrisa y un asentimiento de cabeza, dejándome cerrar y, asumiendo que ellas la querían de esa forma, asegurar la puerta."

"Mientras lo hago, me doy cuenta de que la escena frente a mí es aquella de una fiesta de té de la tarde, justo como cualquier otra entre las dos. De alguna forma, creo que no debería sorprenderme."

scene ev lilly_bedroom_large:
    ypos 0 xpos -860
with locationchange

"Para mi alivio, Hanako luce relativamente tranquila. Su ruptura en clase probablemente le ha hecho bien, dándole tiempo para relajarse un poco."

scene bg school_dormlilly
show lilly basic_smileclosed_paj:
    twoleft
    ypos 1.2
show hanagown distant:
    tworight
    ypos 1.17
with locationchange

"Tomo asiento entre las dos en la mesa baja en el centro de la habitación de Lilly, la tetera de colores brillantes despidiendo vapor entre nosotros."

"Una bolsa grande color café cerca del lado de Lilly atrapa mi atención. Secretamente trato de lanzar una mirada dentro un par de veces, pero no puedo obtener una buena vista desde aquí."

"Viendo a Hanako, parece que tiene tanta curiosidad acerca de ella como yo."

hi "Oye, ¿Lilly?"

"Lilly termina la taza que llevó a sus labios antes de devolverla a la mesa y darme su atención."

show lilly basic_smile_paj
with charachange

li "¿Sí?"

hi "Solo me estaba preguntando sobre esa bolsa café…"

"Se detiene por un momento, luego da una ligera sonrisa pícara."

show lilly basic_cheerful_paj
with charachange

li "Ese sería el regalo de Akira. Desafortunadamente, ella dijo que estaba trabajando y no podría unírsenos."

"Lilly se inclina y siente el objeto dentro antes de levantar su brazo."

"Levanto una ceja dado que dos objetos, no uno, salen de la bolsa. Los cuellos de las botellas son sujetados por Lilly a cada lado de su dedo medio. Así que este es el porqué ella tenía la puerta cerrada."

show wine:
    yalign 0.5 xanchor 0.0 xpos 1.0 alpha 0.0
    easein 1.0 alpha 1.0 xanchor 1.0
with Pause(1.0)

ha "Vino…"

"Hay dos pequeños golpes secos cuando las dos botellas son llevadas a descansar en la mesa; una roja, una blanca. Quiero creer que es falso, vino sin alcohol, pero si lo fuera, no habría ninguna necesidad de ser tan prudente."

hi "¿Alcohol? ¿En serio? ¿Estás segura de que esta es una buena idea?"

show lilly basic_smileclosed_paj
with charachange

"Lilly sonríe cortésmente y suelta una risilla. No estoy muy convencido de que ella lo esté."

li "Este sería el regalo de mi hermana. Sé que es un poco cuestionable, pero un poco no debe hacer daño."

"Si Lilly tuviera un serio problema con ello, no pienso que hubiera estado de acuerdo tan fácilmente. Dejando eso de lado, tenía a Akira encasillada como del tipo serio y responsable, tal vez como una Lilly grande, pero parece que estaba mal."

"Ni siquiera podemos tomar legalmente aún."

hi "Bueno, en ese caso no me quejaré. No se ven mal, tampoco."

"No soy conocedor, pero al menos las botellas se ven bien. Aparte de un clandestino vaso de vino o dos de parte de mi padre en las cenas familiares, no he bebido el suficiente para saber qué es qué."

show hanagown smile
with None

show wine:
    easeout 1.0 alpha 0.0 xanchor 0.0
with Pause(1.0)

hide wine
with None

"Eso, y no puedo realmente decir que soy un puritano. A decir por la expresión de Hanako, ella está pensando lo mismo, y es su cumpleaños de cualquier forma."

show lilly basic_smile_paj
with charachange

li "¿Debería abrir una?"

hi "Seguro. Tomaré un poco—{w=0.3}{nw}"

$ renpy.music.set_volume(0.5, 0.5, channel="music")
$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_doorknock2

show lilly basic_displeased_paj
show hanagown worry
with vpunch

"Mi corazón se detiene cuando escucho tres golpes secos viniendo de la puerta de Lilly. La cabeza de Hanako se sacude de un lado a otro, y los ojos de Lilly se cierran mientras escucha atentamente. Ninguno de nosotros quiere ser agarrado por esto."

show lilly basic_oops_paj
with charachange

li "¿Quién es?"

mystery "¡Déjame entrar, tengo frío!"

show lilly basic_weaksmile_paj
with charachange

$ renpy.music.set_volume(1.0, 6.0, channel="music")

"Lilly deja salir un resignado suspiro antes de indicarle a Hanako que abra la puerta."

show hanagown invis at tworight
with dissolvecharamove

hide hanagown
with None

"Ella obedientemente se levanta y hace ruido con su camisón antes de moverse, aparentemente sin estar segura aún de quién es, pero confiando lo suficiente en Lilly para hacer lo que pide."

"Solo puedo ver una figura rubia, de traje negro hacerse visible sobre el hombro de Hanako mientras abre la puerta."

mystery "Feliz cumpleaños, Hanako."

ha "G-gracias… Akira…"

"Hanako hace una pequeña reverencia mientras juguetea con sus dedos frente a ella. Así que esta es la elusiva hermana de Lilly."

show bg school_dormlilly at bgleft
show lilly basic_weaksmile_paj:
    left
    ypos 1.2
with charamove

show hanagown invis at center
show akira invis at right
with None

show hanagown normal at Position(ypos=1.17)
show akira basic_smile:
    right
    xpos 0.95
with dissolvecharamove

"Akira sigue a Hanako a la mesa después de cerrar la puerta tras de ella, dándome mucho tiempo para tomar una buena vista de ella."

"Parece ser más o menos de la misma estatura de Hanako, y tiene pelo corto que está un tanto agresivamente cortado. Eso, añadido a sus modestos pechos, traje masculino y voz profunda, le da un efecto algo andrógino."

show akira basic_ending at Position(ypos=1.18)
with dissolvecharamove

"Sin más preámbulos, se deja caer al lado de la mesa frente a mí."

show lilly basic_smile_paj
with charachange

li "Es bueno tener tu compañía después de todo, Akira. ¿Tu trabajo te dejó salir?"

show akira basic_boo
with charachange

aki "Sí. Tengo que regresar ahí en un rato, pero me las arreglé para tener suficiente tiempo libre para manejar hasta acá."

show akira basic_smile
with charachange

aki "Así que… este sería Hisao, ¿entonces?"

"Una sonrisa con confianza es lanzada en mi dirección, así que asiento cortésmente en respuesta. Considerando que simplemente se lanzó directo a usar mi nombre, es mucho más informal de lo que su apariencia podría sugerir."

"Esperen, si ya sabe quién soy, eso debe significar que Lilly ha hablado de mí con ella. Me pregunto qué habrá dicho."

show lilly basic_smileclosed_paj
with charachange

li "Perdón por no presentarlos, Hisao. Esta es Akira Satou, mi hermana mayor."

hi "Ya veo. Gusto en conocerte."

show akira basic_ending
show hanagown worry:
    0.1
    ease 0.1 ypos 1.15
    ease 0.1 ypos 1.17
with Dissolve(0.1)

"La persona en cuestión aplaude sus manos sonoramente, haciendo a Hanako saltar un poco."

show akira basic_lost
with charachange


"Akira nota esto, y luce inquieta por una fracción de segundo antes de volver a sus zancadas."

show akira basic_smile
with charachange

"Solo ahora me doy cuenta de que Akira no le ha prestado atención excesiva a las cicatrices de Hanako. Esta también luce cómoda, si no exactamente relajada cerca de Akira."

show akira basic_laugh
with charachange

aki "Bien entonces, ¿asumo que los regalos lograron pasar? No hay razón para esperar, considerando que Hisao y la chica del cumpleaños parecen estar bastante ansiosos."

show lilly basic_cheerful_paj
with charachange

"Lilly da una risilla mientras incómodamente volteo a otro lado, un poco apenado por el hecho de que no pude ocultar mi interés."

"Sin embargo los ojos de Hanako me están diciendo que quiere probar el vino junto conmigo, así que me decido por una mirada de indiferencia pobremente fingida."

show lilly basic_smile_paj
show akira basic_smile
show hanagown distant
with charachange


"Akira se las arregla para descorchar la primera botella con poco esfuerzo, y Hanako va por unas copas antes de que yo pueda servir las cuatro hasta llenarlas de vino blanco."

"Escuché por ahí que el vino blanco tiene menos alcohol que el vino tinto, así que pienso que sería mejor empezar con ese."

hi "Por Hanako, y el viaje de Lilly."

show lilly basic_giggle_paj
show akira basic_laugh
with charachange

$ doublespeak (li, aki, u"¡Salud!")

show hanagown smile
with charachange

ha "S-salud…"

show lilly basic_smileclosed_paj
show akira basic_smile
with charachange

"Después de la tradicional elevación de los vasos todos tomamos sorbos del pálido líquido amarillo. No es nada como aquellas cosas que probé con mis padres, con el sabor a frutas casi escondiendo por completo el sabor del alcohol."

"Tal vez así es como el vino verdadero se supone que sepa. Por otro lado, es posible que Akira solo haya escogido un vino que se amoldaría a nuestros gustos, dado que ninguno de nosotros está acostumbrado al alcohol aún."

"O al menos, espero que ninguno de nosotros lo esté."

hi "Esto no es tan malo. Estaba esperando algo más… fuerte."

show akira basic_ending
with charachange

aki "Si no te ha gustado, tengo unas cuantas variedades más de las que podría haber escogido."

hi "Suena como que sabes de lo que hablas cuando se trata de vinos."

show akira basic_smile
with charachange

aki "Solo un poco; soy más una persona de cervezas."

show akira basic_laugh
with charachange

aki "Sin embargo, tengo entendido perfectamente eso de beber."

"Como para probar su punto, ella rellena su copa antes de llevarla a sus labios y echar su cabeza hacia atrás."

stop music fadeout 6.0

show akira basic_smile
show hanagown normal
with charachange

"Hanako y yo observamos silenciosos mientras la copa completa desaparece por la garganta de Akira. No puedo decidir si estar impresionado o desanimado, pero ciertamente no tengo ninguna urgencia en imitar el acto."

show lilly basic_displeased_paj
with charachange

"Lilly hace una ligera mueca a los alardes de su hermana. Sin embargo, noto que está sorbiendo de su copa mientras lo hace."

show lilly basic_weaksmile_paj
with charachange

li "Como sea, ahora que el regalo de Akira se ha abierto y probado, ¿deberíamos proceder a los nuestros?"

show hanagown worry
with charachange

ha "¿Re-regalos?"

play music music_twinkle fadein 6.0

show lilly basic_smile_paj
with charachange

li "Es correcto, tenemos tus regalos. Es tu cumpleaños, después de todo."

show lilly basic_smileclosed_paj
with charachange

li "Este es de mi parte."

"Lilly saca la muñeca cuidadosamente envuelta de debajo de la mesa y se la pasa a Hanako."

"Hanako maneja el regalo como si fuera cristalería, girándolo cuidadosamente para remover la cinta que ata el envoltorio. Eventualmente el papel cae de la muñeca, revelando el verde esmeralda del vestido de esta."

show hanagown normal_blush
with charachange

ha "Es… hermosa."

"No estoy seguro de qué reacción esperaba de Hanako. La casi total falta de muñecas en su cuarto me hacía pensar que no se interesaba por ellas, pero la mirada en sus ojos es algo diferente."

"Ella gira la muñeca con la misma delicadeza que le dio al envoltorio, como si esperara que se fuera a deshacer en sus manos."

show lilly basic_weaksmile_paj
with charachange

li "Estoy feliz de que te gustara. Hisao la eligió, para ser honesta."

"Hanako repentinamente recuerda que no está sola en la habitación, y cambia su concentración de la muñeca."

show hanagown smile
with charachange

ha "S-sí, me gusta. G-gracias, Lilly y Hi-Hisao."

hi "De hecho, te traje algo más…"

"Alcanzo mi mochila y saco el juego de ajedrez envuelto."

hi "Aquí lo tienes. Feliz cumpleaños."

show hanagown normal
with charachange

"Hanako cuidadosamente coloca la muñeca de Lilly a su lado y abre mi regalo con el mismo cuidado que mostró con el de Lilly."



"Pronto, el patrón de cuadros del tablero es visible, y Hanako gentilmente pasa sus dedos a través de las superficies talladas."

show hanagown normal_blush
with charachange

ha "¡Oh!"

"Casi por accidente ella abre el seguro de la tapa, asustándose a sí misma en el proceso. La abre y saca una de las piezas grises."

"Luce tan absorta en las piezas de ajedrez como lo estuvo con la muñeca antes."

hi "Son de coral. Coral natural, sin teñir. O así estoy informado."

show hanagown smile
with charachange

ha "Gracias, Hisao…"

hi "No hay problema. Es tu cumpleaños, después de todo."

show hanagown distant
with charachange

ha "Eso es cierto… mi cumpleaños…"

"Una vez más la reacción de Hanako parece un poco extraña, pero cuidadosamente cierra la tapa del tablero."

show akira basic_lost
with charachange




"Noto que la sonrisa de Akira está comenzando a verse muy tensa. Me pregunto si sabrá algo de lo que pasó en clase, dado que parece andar de puntillas cerca de Hanako."

hi "Tendré que jugar contigo otra vez en alguna ocasión."

show hanagown smile
with charachange


ha "Me… aseguraré de jugar contigo antes…"


show ev hanako_presents2:
    truecenter
    subpixel True zoom 1.1
    acdc_warp 10.0 zoom 1.0
with whiteout

"Ella toma la muñeca que recibió de parte de Lilly y la sostiene hacia su pecho junto con el pequeño tablero de ajedrez, poniendo la pieza encima."

"El acto parece tranquilizarla un poco, y nosotros simplemente nos sentamos en silencio por un rato."

"Creo que es una de las pocas veces que la he visto genuinamente feliz, acunando la amistad de dos personas en su pecho tan fuertemente como puede."

show akira basic_boo
show lilly basic_smile_paj
with None

hide ev
with locationchange

ha "Gracias, Lilly. Gracias, Hisao."

show hanagown worry_blush
with charachange

"En el proceso de agradecernos, Hanako deja caer la pieza de ajedrez y hurga un poco en su prisa por recuperarla."

show hanagown distant
with charachange

"Una vez que la encuentra, Hanako deja el juego de ajedrez y nerviosamente traga su vino. Es como si el mundo real repentinamente hubiera regresado a su conciencia, y su escape más rápido de él estuviese en la copa."

hi "Oye, tranquila, no debes tomar tan rápido…"

show lilly basic_weaksmile_paj
with charachange

li "Es una fiesta, Hisao…"

"A pesar de decir esto, hay un ligero tono de preocupación en su voz. Eventualmente accediendo, Lilly procede a seguir el ejemplo de Hanako, aunque no tan ávidamente."

"Ella parece estar tomando pequeños sorbos de su vaso y dejando el vino asentarse en su lengua antes de tragarlo. Decido que este es probablemente el mejor enfoque y hago lo mismo."

hi "Dado que esta es una especie de fiesta de despedida para ti también, espero que disfrutes el viaje al menos un poco, Lilly. Espero que tu tía se mejore."

show hanagown worry
with charachange


ha "T-también espero que esté bien, Lilly…"

show lilly basic_surprised_paj
with charachange

"Lilly y yo quedamos un poco desconcertados por el fervor de Hanako en desearle bien a Lilly, a pesar de su propia situación familiar. Estoy un poco impresionado."

show lilly basic_weaksmile_paj
with charachange

li "Vaya, vaya, gracias a ambos. Me aseguraré de hacerle llegar sus pensamientos a mi familia cuando los vea."

show akira basic_smile
with charachange

aki "Todo estará bien al final, Lilly. No te preocupes por eso."


"Dado que el ambiente en la habitación se ha vuelto notablemente más taciturno, decido intentar hacer que las cosas sigan por otro rumbo."

hi "Bien entonces, ¿deberíamos empezar con el pastel?"

show hanagown normal
show lilly basic_smileclosed_paj
show akira basic_ending
with charachange

"Mi proposición tentativa tiene el efecto deseado, iluminándose todos considerablemente."

show hanagown normal_blush
with charachange

ha "S-sí, por favor…"

show lilly basic_surprised_paj
with charachange

li "¿Pastel? No sabía que hubiera algún pastel…"

hi "Tomé uno antes de venir, junto con algunos bocadillos."

show lilly basic_giggle_paj
with charachange

li "Bien hecho, Hisao. Al menos uno de nosotros recordó traer uno."

"Todos parecen agradecer la distracción, así que saco el pastel de mi mochila y comienzo a cortarlo."

"Mezclar vino y pastel de chocolate no es algo que pienso que resultará bien, pero a ninguno de nosotros parece importarle. La conversación es temporalmente suspendida mientras comenzamos a comer."

"No estaba muy confiado en un inicio sobre esta idea; después del ataque de pánico de Hanako esperaba lo peor de esta noche, pero pienso que la idea de Lilly de darle buenos recuerdos de su cumpleaños está funcionando."

"Eso, y también tenerlo compartido con su fiesta de despedida."

"Por la reacción de Hanako a sus regalos, puedo decir que ella estuvo realmente agradecida."

show lilly basic_smileclosed_paj
show akira basic_smile
show hanagown drunknormal
with shorttimeskip

"Hanako trata de servirse otra copa de vino, pero termina derramando un poco en la mesa. Hasta ahora ha tomado un par, así que considerando que nunca ha bebido alcohol antes, no es sorpresa que se esté sintiendo un poco mareada."

show hanagown drunksad
with charachange

ha "P-perdón Lilly… no fue mi intención hacer un desastre… yo…"

hi "No te preocupes, yo me ocupo…"

$ ksgallery_unlock("unlock_ev lilly_hanako_hug_end")
show ev lilly_hanako_hug:
    xalign 0.5 yalign 1.0 subpixel True
    easein 12.0 yanchor 0.0 ypos -0.15
with whiteout

"Lilly se acerca por un lado y gentilmente toma a la alterada Hanako en sus brazos, dándome un descanso."

li "Está bien, Hanako. Solo estoy feliz de que estés aquí."

"Hanako solo da un ligero asentimiento como respuesta. Es apropiado, supongo, que Lilly sea la que la apoye de esta forma. No tengo idea de cómo sería Hanako si no lo hiciera."

"Ver a las dos de esta forma me hace apreciar el hecho de que estoy al tanto de un momento tan íntimo. Incluso Akira no puede sino sonreír ante la visión."

"Nunca hubiera pensado que me las arreglaría para encontrar nuevos amigos tan rápido, y estoy aún más agradecido de que de todas las personas, ellas dos sean con las que hice amistad."

stop music fadeout 3.0

show lilly basic_cheerful_paj:
    xpos 0.02
    ease 1.0 xpos 0.0
show hanagown drunksmile:
    xpos 0.48
    ease 1.0 xpos 0.5
with None

hide ev
with locationchange

"Ellas lentamente se separan una de la otra, Hanako recuperándose un tanto mientras rápidamente vuelvo a mi tarea."

"Encuentro una toalla junto con el juego de té de Lilly y comienzo a limpiar lo derramado. Sin embargo, para cuando he terminado, Hanako y Lilly se las han arreglado para descorchar la otra botella y han llenado sus copas."

show akira basic_ending
with charachange

aki "Parece que están disfrutando el vino, entonces. Solo no se alboroten con él después de esto, si no les importa."

"Todos asentimos obedientemente y lo acordamos, pero su recordatorio se siente un poco tonto dado que ella es la que está proporcionando a menores de edad el alcohol."

play music music_comedy fadein 0.5

show lilly basic_cheerfulblush_paj at Position(xpos=0.0)
show hanagown drunkgiggle at Position(xpos=0.5)
show akira basic_boo
with shorttimeskip

"La segunda copa de vino se acaba mucho más rápido que la primera, y antes de que alguno de nosotros lo note, la segunda botella está vacía."

"Aunque Akira está ayudándonos a terminarlas, Hanako parece estar casi igualándola en la cantidad que ha bebido."

"Siento que mi cabeza está dando algunas vueltas, pero pienso que me las he arreglado para medir mi propia tolerancia sorprendentemente bien."

"Hanako sonríe despreocupadamente, jugando con el pelo de su muñeca. Creo que es una apuesta bastante segura decir que ella… no se ha moderado tan bien como yo."

"No creo que haya sido la intención de Hanako el ponerse así de borracha, pero parece que el alcohol la golpeó de repente. Tiene un cuerpo bastante delgado, algo que tampoco le podría ayudar a manejar bien su borrachera."

"Lilly acuna su copa, recorriendo un dedo a través del borde. Sus mejillas están rosadas, pero se las está arreglando para evitar lucir extremadamente borracha. Akira está, un tanto de esperar, casi nada afectada."

"Aunque su sonrisa podría ser un poco más ancha que antes. Tal vez."

show hanagown drunkgiggle:
    ease 0.1 ypos 1.15
    ease 0.1 ypos 1.17
with None

show hanagown drunkpout
with charachange

"Hanako repentinamente hipa y accidentalmente tira la muñeca."

show hanagown drunksad
with charachange

ha "Creo… que mejor me voy a la cama. G-gracias, Hisao, gracias Lilly y Aaaakiraaaa."

"Ella pronuncia el nombre de Akira con dificultades, evitando por poco romper en carcajadas. Está completamente borracha, y no logro decidir si sentirme mal o no por lo entretenido que estoy del estado en que se encuentra."

"Es realmente extraño verla actuar tan libremente. Una pena que es solo con la ayuda del alcohol."

show akira basic_ending at Position(ypos=1.0)
with dissolvecharamove

aki "Ven, déjame darte una mano."

"Akira comienza a levantarse para ayudar a Hanako, pero es detenida cuando Lilly tose fuertemente."

show lilly basic_planned_paj
with charachange

li "Hisao, ¿podrías por favor?"

show akira basic_lost
with charachange

"Akira luce un poco sorprendida, y tengo que admitir que lo estoy también. No me molesta la petición de ninguna forma, y menos cuando es dicha con tal sonrisa… simplemente viene más bien inesperadamente."

hi "Se-seguro. No hay problema."

hide hanagown
with None

show hanagown drunksad:
    center
    ypos 1.17
with None

show hanagown drunkgiggle_close at Position(ypos=1.0)
show akira basic_smile
with dissolvecharamove

stop music fadeout 4.0

"Recojo el juego de ajedrez y ayudo a Hanako a levantarse."

"Sí me siento un poco responsable por ella considerando que, además de Akira, soy probablemente la persona más sobria en la habitación. Ella abriga la muñeca en una mano y me ofrece la otra."



show hanagown drunkgiggle_close:
    parallel:
        ease 0.5 xpos 0.45
        ease 1.5 xpos 0.55
        ease 0.5 center
    parallel:
        1.5
        "hanagown drunkgiggle_close_ni" with Dissolve(1.0, alpha=True)
show bg school_dormlilly:
    ease 1.0 xpos 0.45
show akira basic_smile:
    ease 1.0 xpos 1.0 alpha 0.0
show lilly basic_planned_paj:
    ease 1.0 xpos 0.05 alpha 0.0
with None

show bg school_girlsdormhall:
    center
    xpos 0.6
    ease 2.5 xpos 0.4
with Dissolve(1.0)

hide akira
hide lilly
with Pause(0.5)

show bg school_dormhanako_ni:
    center
    xpos 0.45
    ease 1.0 center
with Dissolve(1.0)

"Tropezamos hasta la puerta, hacia el corredor, y a dentro de la habitación de Hanako, con esta chocando conmigo varias veces en el camino."

play sound sfx_switch

scene bg school_dormhanako
show hanagown drunkgiggle_close at center
with Dissolve(0.2)

"Dentro del cuarto, prendo la luz mientras Hanako torna su atención hacia un estante en su tocador. Una elegante muñeca está descansando en él, viendo hacia la desnuda habitación."

show hanagown drunksmile_close
with charachange

ha "Ahí estás… estarás segura aquí…"

show ev hanako_dolls
with locationchange

"Hanako cautelosamente coloca la muñeca junto a la otra y acomoda su vestido."

"Descansan en silencio, cabello y ropas perfectamente arreglados. Justo como la tetera en la habitación de Lilly, producen un contraste distinto a los aburridos blancos y grises que impregnan la habitación."



show hanagown drunksmile_close:
    ease 0.25 ypos 1.05
    ease 1.0 ypos 1.0
with None

hide ev
show hanagown drunkdistant:
    ease 0.25 ypos 1.05
    ease 1.0 ypos 1.0
with charadistant

"Satisfecha de que sus muñecas, sus dos únicas posesiones reales, están a salvo, Hanako da un paso atrás y se queda en pie, tambaleándose severamente. Doy un paso adelante para atraparla si se necesita, pero ella recupera su balance sin mi ayuda."

"Por un momento, ambos estamos de pie en silencio mientras Hanako mira abajo hacia el armario."

show hanagown drunkdistant:
    ease 1.0 xpos 0.48
    ease 1.0 xpos 0.5
    repeat
with Pause(0.5)


"Después de un minuto o dos ella comienza a balancearse un poco de lado a lado. Es bastante desconcertante."

hi "¿Vas… a estar bien?"

show hanagown drunksmile at center
with dissolvecharamove

"Hanako levanta su cabeza, y voltea a verme como si acabara de recordar que estoy en la habitación también."

show hanagown drunksmile_close:
    ease 1.0 ypos 1.05
with vpunch

stop music fadeout 0.3
play sound sfx_pillow

"Lo que es inesperado es que ella da dos pasos hacia mí y enrolla sus brazos alrededor de mi cuerpo, con su cabeza yendo a descansar contra mi pecho."

play music music_heart fadein 0.5


"Puedo sentir mi corazón latiendo mientras todos mis sentidos se sienten como si estuvieran volviendo a la vida otra vez después de su entorpecimiento por los tragos anteriores."

"El olor del vino en su aliento, sentir sus dedos a través de mi ropa, el aroma de su pelo bajo mi barbilla…"

"Mis manos permanecen estiradas frente a mí, sin atreverme a tocarla. La tentación de abrazarla está ahí, estrecharla, decirle que todo estará bien… pero esto se siente mal. Realmente, realmente mal."

hi "Hanako…"

show hanagown drunknormal_close at Position(ypos=1.05)
with charachange

ha "Pero quiero quedaaaarme contigo y Lillyyyy."

"El balbuceo de Hanako me recuerda un poco a Misha. Ella probablemente no estaría contenta de escuchar eso."

hi "Sabes que no puedo. Tú eres una chica y yo un chico, después de todo, y Lilly necesita dormir."

show hanagown drunkpout_close
with charachange

"Ella da un gemido de decepción. Es tan extraño para ella actuar tan directamente."

hi "No te preocupes, te veré mañana, ¿está bien?"

"Decido descansar una mano en su cabeza para tranquilizarla, decidiendo que esto es lo más lejos que me permitiré ir en términos de contacto físico con ella mientras está en este estado."

"La cabeza de Hanako se acurruca contra mi pecho. Me hace sentir mucho más incómodo con la situación, y sus brazos se aprietan alrededor de mi espalda, rápidamente decido echarme atrás."

"Descanso mis manos sobre sus hombros y le doy un firme pero gentil empujón. Su agarre se aprieta un poco cuando lo hago, pero eventualmente se interrumpe."

show hanagown drunkworry_close
with charachange

ha "No quiero que te vayas…"

hi "Hanako, por favor. Akira y Lilly comenzarán a pensar cosas raras si me tomo demasiado tiempo aquí."

"También es totalmente verdad. Realmente no quiero tomar ningún riesgo, y me siento muy incómodo en este momento."

"No debo tratar de leer nada del modo en que está actuando en este momento."

"Leí que además de que el alcohol disminuye tus inhibiciones, la gente puede reaccionar a la borrachera de muchas formas diferentes que no necesariamente se reflejan con la realidad."

"E incluso sin eso, hay muchas formas de interpretar lo que está diciendo. Mientras ella esté segura, trataré de salirme de su habitación tan pronto como sea posible."

show hanagown drunkworry_close:
    ease 0.1 ypos 1.03
    ease 0.1 ypos 1.05
with Pause(0.2)

"Hanako hipa otra vez, luciendo en verdad desastrosa mientras está en pie y se muestra abatida en el centro de la habitación."

"Su personalidad cambió mientras bebió más y más, y ahora, completamente sola en su habitación conmigo, su previo ánimo parece haberla dejado. ¿Solamente estaba actuando de forma optimista para asegurarse de que no nos preocupáramos?"

"Incluso si lo estaba haciendo… ¿qué podría hacer por ella, dado que yo hago exactamente lo mismo con respecto a mi propia condición?"

show hanagown drunkworry_close:
    ease 1.0 ypos 1.1 alpha 0.0
with Pause(1.0)

hide hanagown
with None

"Distanciándome de mis pensamientos, eventualmente me las arreglo para acorralar a Hanako en su cama, aunque sus intentos de domar a las salvajes sábanas en esta terminan por lograr poco."

hi "Perdón por lo de esta noche, Hanako. Sé que probablemente no recordarás nada de esto, pero… feliz cumpleaños. Lamento no haber podido hacer más por ti."

"Ella levanta la mirada hacia mí por un momento. No tengo idea de si lo que dije de hecho llegó a ella, pero cualquier oportunidad de preguntar se pierde cuando sus ojos se cierran tranquilamente."

play sound sfx_switch

scene bg school_dormhanako_ni
with Dissolve(0.2)

"Suspiro aliviado antes de silenciosamente alejarme de ella y dejarla en su habitación, apagando la luz mientras me voy."

stop music fadeout 4.0

scene bg school_girlsdormhall
with locationchange

"Dudo un poco antes de abrir la puerta de la habitación de Lilly otra vez, rápidamente ensayando lo que debo decir si soy cuestionado sobre Hanako. Después de unos segundos, aún no puedo pensar en nada."

scene bg school_dormlilly
show lilly basic_smileclosed_paj:
    twoleft
    ypos 1.2
show akira basic_smile:
    tworight
    ypos 1.18
with locationchange

"Abro la puerta y me aseguro de cerrarla tras de mí, por miedo a que algún estudiante que pase alcance a darle una mirada al vino, antes de darle mi atención a las dos chicas en la mesa baja."

"Akira está sonriendo casualmente, tal como lo está Lilly. Agradezco el cambio del ambiente de la habitación de Hanako."

show lilly basic_smile_paj
with charachange

li "¿Eres tú, Hisao?"

hi "Sí. Puse a Hanako en su cama; está durmiendo ahora."

show lilly basic_weaksmile_paj
with charachange

li "Eso es bueno. Tengo que admitir que no pensé que ella tomaría tanto."

show akira basic_lost
with charachange

aki "Oye, está bien. Está segura y metida en su cama ahora. Con la forma en la que ella es…"

"Ella va apagando su voz apenadamente, aunque Lilly y yo difícilmente protestaríamos. Para alguien tan ansiosa y temerosa, beber le daría una salida fácil de esos constantes sentimientos."

play music music_night fadein 4.0

"Desearía poder hacer más por ella. Me siento inútil."

"Viendo a Lilly, pienso otra vez en lo que me pregunté en la ciudad. Mi relación con ella es la de un amigo, y solo se ha sentido de esa forma, pero ahora creo que sé por qué."

"Lilly ha estado ahí para ambos, Hanako y yo, desde que la conocí, pero ella es así con todos, tratando de hacer lo mejor para hacerlos sentir mejor."

"Con eso en mente, ¿cuál es entonces el lazo entre Hanako y yo?"

"Después de rescatar nuestra relación luego del ataque de pánico que inadvertidamente inicié durante la clase, siento que estamos de vuelta a ser amigos, pero ella está en mi mente más y más."

"No puedo decir que veo a alguna otra chica de la misma forma, pero tal vez es solo una reacción normal hacia alguien que actúa así."

hi "Oye, ¿Akira?"

show akira basic_boo
with charachange

show akira basic_smile
with charachange

"Ella bosteza antes de mirarme. Se está haciendo bastante tarde."

hi "Sabes lo que pasó con Hanako, ¿no?"

show akira basic_resigned
with charachange

aki "Sí. Lilly me dijo."

show akira basic_boo
with charachange

aki "Negocié con bastante ahínco un descanso para poder venir acá y ayudar a hacer su cumpleaños un poco más animado. Nos llevamos bastante bien."

"Es sorpresivo escuchar eso de alguien tan extrovertida como ella, pero si Hanako llegó a conocerla a través de Lilly, tal vez tuvo el tiempo de acostumbrarse a Akira."

show akira basic_smile at tworight
with dissolvecharamove

aki "Y hablando de eso, mejor me voy. Ya voy a llegar un poco tarde con la hora que es."

show lilly basic_oops_paj
with charachange

li "Pero ya es tan tarde…"

show akira basic_boo
with charachange

aki "Lo siento. Nos aventaron un montón de trabajo, así que son horas extras."

show akira invis:
    xpos 0.8
with dissolvecharamove

"Ella se levanta con un gruñido y pasa junto a mí hacia la puerta. Justo antes de irse, gira hacia nosotros."

show akira basic_lost:
    tworight
with dissolvecharamove

aki "¿No te has olvidado de la hora del vuelo y todo el resto?"

show lilly basic_smileclosed_paj
with charachange

li "No te preocupes, tengo todo listo. Es solo cuestión de empacar cuando se acerque el momento de partir."

show akira basic_ending
with charachange

aki "Buena chica. Entonces los veré después chicos."

show akira invis:
    xpos 0.8
with dissolvecharamove

hide akira
with None

"Y con eso, desaparece a través de la puerta con su mano elevada en despedida."

show lilly basic_smileclosed_paj at Position(xpos=0.5)
show bg school_dormlilly at bgright
with charamove


hi "Tu hermana es… algo, bien."

show lilly basic_giggle_paj
with charachange

"Probablemente debí haber pensado ese comentario antes de decirlo. A pesar de ello, Lilly parece bastante divertida por mi apreciación."

hi "¿Estás bien después de todo lo que tomaste? ¿No estás borracha y solo lo estás ocultando bien?"

show lilly basic_smileclosed_paj
with charachange

li "Te aseguro que estoy bastante bien. Puedo moderarme. Tú también pareces ser bastante dueño de ti mismo, si debo decirlo."

hi "Sí, bueno, supongo que tu moderación se aplica a mí también."

"Titubeando un poco, tomo asiento en la mesa frente a Lilly. Quiero decir esto directamente, al menos para asentar mis propios pensamientos."

hi "He querido preguntar esto, pero me tomó un tiempo decidirme…"

hi "¿Tienes alguna idea de qué es lo que disparó ese ataque de pánico? Pienso que fue algo relacionado con su cumpleaños, pero ahora ya no sé."

hi "Incluso Akira estuvo siendo realmente cuidadosa cerca de ella, así que asumo que lo sabe también."

show lilly basic_reminisce_paj
with charachange

"La sonrisa de Lilly se va, la felicidad de la fiesta de cumpleaños ahora ha terminado en verdad."

li "Para ser honesta, yo misma no estoy de ninguna forma segura de los detalles."

li "Hanako te dijo que estuvo en un incendio casero. No me dijo más que eso, después de habernos conocido y pasado mucho tiempo juntas."

show lilly basic_concerned_paj
with charachange

li "Aparte de eso… simplemente no me dijo nada nunca."

hi "Nunca te dijo…"

show lilly basic_sad_paj
with charachange

li "Asumiendo lo peor, ¿qué es lo que ella tiene que recordar? ¿Una vida de aislamiento y además posiblemente la muerte de su familia? ¿Tal vez yendo tan lejos como para culpar a su existencia de sus muertes?"

"Incluso pensar en lo poco que sé sobre el pasado de Hanako es desolador. Haber tenido que vivir a través de todo eso, y vivir con esos recuerdos, debe ser definitivamente peor."

"Lilly luce similarmente deprimida, pero puedo verla recuperar al menos un poco de su compostura ante mis ojos."

"Tengo el presentimiento de que ambos estamos hablando más francamente de lo que de otra forma haríamos gracias al vino, pero se siente como si hablar de esto fuera algo bueno de todas maneras."

hi "Me siento un tanto impotente sobre ello. Cuando se le pone de esa forma, ¿qué podría hacer yo por ella?"

show lilly basic_sleepy_paj
with charachange

li "No estoy del todo segura de que deba decirte esto, pero Hanako me dijo que la visitaste al día siguiente después de que fuimos a ver cómo estaba."

show lilly basic_weaksmile_paj
with charachange

li "Debo admitir que no predije que ella daría tal paso tan rápido después de lo que pasó, ni esperaba que tú lo hicieras. Creo que fue un buen gesto de tu parte."

hi "No fue mucho, en verdad."

hi "Es solo que… en momentos como este, algunas veces pienso que sería mejor si no tuviéramos que dejar nunca Yamaku, o al menos este pueblo. Las cosas son mucho más fáciles sin otros alrededor."

"No esperaba que Lilly luciera tan preocupada por lo que dije, y por un rato luce perdida en pensamientos."

show lilly basic_oops_paj
with charachange

"Se mueve para hablar, pero se detiene tan pronto como lo hace, y vuelve a pensar. Es un poco desconcertante."

show lilly basic_reminisce_paj
with charachange

li "Pienso…"

show lilly basic_smile_paj
with charachange

li "Dime, ¿tienes algo planeado para la noche del viernes?"

hi "¿Noche del viernes? No…"

hi "¿No es tu vuelo a Escocia al día siguiente? No pienso que sería una buena idea que te fatigaras incluso antes de llegar allá."

show lilly basic_weaksmile_paj
with charachange

li "Estaré bien, no necesitas preocuparte por mí. Haría esto mañana en la noche, pero imagino que Hanako se estará sintiendo algo mal por un rato."


"La idea de cómo estará mañana me hace hacer una mueca. Tal vez debemos agradecer que no terminó simplemente vomitando por tomar tanto teniendo tan poca resistencia."

hi "Bueno, voy a poder asistir a lo que sea que estás planeando. ¿Qué es?"

show lilly basic_smileclosed_paj
with charachange

li "Nada inusual, te lo aseguro. Solo una pequeña excursión."

show lilly basic_cheerful_paj
with charachange

li "Y será mejor que te vayas, Hisao. No pienso que vaya a pasar mucho antes de que el toque de queda llegue."

"Oh rayos, el toque de queda. Lo había olvidado por completo."

"Veo al reloj junto a la cama de Lilly, pero parece ser alguna cosa extraña sin números. Lo que supongo que tiene sentido, dada la condición de Lilly."

"No queriendo arriesgarme a una arrogante patrulla de seguridad dándome una reprimenda, me levanto y decido ir a mi dormitorio como ella dice."

hi "Bueno entonces. Supongo que las veré a ti y a Hanako mañana, asumiendo que las dos se las arreglen para levantarse en la mañana."

show lilly basic_smileclosed_paj
with charachange

li "Gracias por tu interés, Hisao. Hasta entonces."

scene bg school_girlsdormhall
with locationchange

"Con eso, tomo mi camino hacia su puerta y hacia el corredor."

"Espero que su idea vaya a ser buena."

stop music fadeout 2.0

scene black
with dissolve



label es_H18:

scene black
with dissolve

play sound sfx_doorknock

"El martillar de un puño contra la puerta se siente como un clavo siendo machacado dentro de mi cabeza."

"Una, dos, tres veces, dejo salir un largo y molesto suspiro y lo soporto mientras presiono mis párpados cerrados, esperando fervientemente por que quien quiera que sea solo se vaya."

"Me siento terriblemente mal. Mi cara se siente como si estuviera fuera de lugar, mis brazos pesados, y me siento muy mareado. Ha sido así desde que me desperté hace una hora, y no puedo invocar la energía para salir de la cama."

"Así que… esto es lo que llaman una cruda."

"Me pregunto si este es el mejor tratamiento para adolescentes que quieren desesperadamente tratar la bebida como una forma de sentirse adultos. Considerando lo poco placentero que esto es, no es algo que quisiera repetir."

play sound sfx_doorknock

"Una serie de golpes llama otra vez, reverberando alrededor de la pequeña habitación. Desearía que simplemente se dieran ya por vencidos; no tengo intenciones de salir de la cama por ellos."

"Los segundos pasan, tornándose en minutos. Dado que no hay más golpeteos viniendo de la puerta, quienquiera que fuera se ha ido. Gracias a Dios."

play music music_dreamy fadein 2.0

scene bg school_dormhisao
with openeye

"Mirando mi reloj, el momento en que realmente debo pensar en cambiarme y alistarme para la clase se acerca. Aunque no creo poder lograrlo."

"Odio saltarme clases, pero no creo que vaya a poder hacer mucho en este punto. Puedo decir que estoy hecho un desastre sin la necesidad de mirarme en el espejo para confirmarlo."

scene bg school_hallway3
with shorttimeskip

"Las prisas de la mañana me están dando suficiente tiempo para pararme fuera del salón de clases por un rato sin lucir demasiado sospechoso. Espero que Mutou no haga ninguna pregunta incómoda sobre el porqué no asistí a la escuela ayer."

"Estaba enfermo, eso es verdad, solo son las razones de ello lo que tengo que ocultar."

"Confiado en que puedo arreglármelas con una omisión táctica de ciertas verdades, entro a zancadas al salón de clases haciendo lo mejor por parecer normal."

scene bg school_scienceroom
with locationchange

"El instante en que abro la puerta y doy un solo paso dentro, puedo sentir una docena de ojos mirándome. No hay forma en que esté imaginando esto; ni siquiera están haciendo un intento por ocultarlo."

show hanako emb_emb:
    tworight
    ypos 1.15
with charaenter

show hanako emb_downtimid
with charachange

"Mis ojos barren rápidamente el salón, y descubro a Hanako. Hacemos contacto visual momentáneamente, antes de que ella voltee al piso y vea fuertemente a su escritorio."

"¿Acaso soltó su lengua? A Mutou podría no importarle como maestro, pero menores de edad consumiendo alcohol en el campus no es exactamente algo que sería tomado a la ligera."

"Volteo a verlo con algo de inquietud."

show muto normal at twoleft
with charaenter

mu "¿Te sientes mejor hoy?"

hi "Sí. Gracias."

"Me indica que tome mi asiento, mis piernas se sienten como palillos mientras me llevan allá."

scene bg school_scienceroom at bgleft
with shorttimeskip

stop music fadeout 2.0
play sound sfx_normalbell

"Tan pronto como la campana del almuerzo suena, me dirijo hacia el escritorio de Hanako para preguntarle qué está pasando."

hi "Hanako… ¿tú dijiste…?"

show hanako emb_emb:
    center
    ypos 1.15
with charaenter

"Ella voltea hacia arriba a verme y sacude su cabeza. Eso es un gran alivio."

show hanako emb_downtimid
with charachange

ha "Es solo…"

hi "¿Solo…?"

mi "Bueno qué tal, Hicchan. ¡Es bueno verte otra vez hoy~!"

show bg school_scienceroom at bgright
show hanako emb_downtimid:
    right
    ypos 1.15
with dissolvecharamove

show shizu basic_sparkle at center
show misha perky_smile at twoleft
with charaenter

play music music_happiness fadein 2.0

"Hago una mueca y giro hacia la inconfundible voz viniendo de atrás de mí. Ese fue un tono de voz demasiado optimista como para sentirse cómodo, incluso para Misha."

"La feliz sonrisa de Misha no es nada fuera de lo usual. La de Shizune, sin embargo, es una muy mala señal. La que está haciendo se ha grabado en mi cerebro como su sonrisa de “te tengo en la palma de mi mano”."

hi "Hola Shizune, Misha. Tú eh… te ves feliz de verme."

show shizu adjust_smug
with charachange

shi "¿…?"

show misha hips_grin
with charachange

mi "¿No te sentías bien ayer, Hicchan~?"

hi "No. Pero ya me siento mejor, al menos."

show shizu behind_smile
with charachange

shi "…"

show misha cross_smile
with charachange

mi "Es bueno saberlo, Hicchan."

"¿Por qué tengo la sensación de que Shizune me está llevando a una trampa?"

hi "Suenas como si no estuvieras siendo completamente honesta."

show shizu adjust_happy
with charachange

shi "…"

show misha hips_smile
with charachange

mi "Oh no, Hicchan, estamos genuinamente encantadas de que ya estás mejor~."

show shizu basic_happy
with charachange

shi "…"

"Shizune está definitivamente desbordándose de felicidad. Solo hay una razón por la que podría estar así. Oh no."

show misha perky_smile
with charachange

mi "De hecho, estuvimos algo preocupadas por ti. Después de todo…"

show misha sign_smile
with charachange

mi "Tú, Hanako y Lilly se ausentaron todos de clase el mismo día."

"Sí, nos atrapó. Tan a la perfección que todo lo que puedo hacer es suspirar derrotado."

hi "Supongo que tienes tus propias teorías sobre esto. ¿Podrías solo, digamos… no decirle a nadie?"

show misha cross_smile
with charachange

mi "Es un poco tarde para eso, Hicchan~."

"Supongo que tiene razón, considerando las miradas que recibí mientras entraba a clase. Aun así, las cosas solo parecen estar al nivel de vaga sospecha en lugar de claras acusaciones, así que probablemente estaremos bien."

show hanako emb_downsad
with charachange

"El rostro de Hanako se hunde un poco más. Tal atención es problemática para mí, ya digamos para ella. Por las reacciones de Shizune y Misha, creo que han notado esto también."

show shizu basic_angry
with charachange

shi "…"

show misha hips_frown
with charachange

mi "¡La única razón por la que estamos haciéndote pasar tan duro momento es porque nos ignoraste ayer en la mañana~!"

"¿Ayer en la mañana? Me toma un momento recordar lo que pasó entonces, dada la neblina inducida por el terrible estado general en el que estaba en ese momento."

hi "Oh, cierto, los toquidos. ¿Esas fueron ustedes dos?"

show shizu behind_frown
with charachange

shi "…"

show misha cross_frown
with charachange

mi "Las mismas, y nos dejaste ahí por años después de que habíamos hecho el esfuerzo de ir a tu dormitorio temprano en la mañana."

hi "Lo lamento, tenía un… ¿problema con náuseas? Un problema con náuseas."

"No se la están creyendo. No puedo culparlas."

show shizu behind_frustrated
with charachange

"La cabeza de Shizune cae en resignación antes de alcanzar su bolsillo."

"Algo blanco y amarillo puede verse sobresaliendo un poco, y cuando lo saca, termina siendo un sobre con decoraciones muy alegres."

show letter_insert:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"Dado que ella lo apunta hacia mí, lo tomo como corresponde."

mi "¡Esto es lo que estábamos tratando de darte con tanto empeño, Hicchan! No revisas tu…"

stop music fadeout 5.0

"Dejo de sintonizar el sonido de la voz de Misha mientras mis ojos registran lo que está escrito en el sobre."

stop music fadeout 0.3

hi "Iwanako…"

"Me quedo viendo el sobre por un momento, antes de recordar que hay gente a mi alrededor."

show misha cross_smile
show shizu behind_blank
show hanako emb_timid
with None

show letter_insert:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide letter_insert
with None

"Hay un muy extraño, y algo invasivo sentimiento en sus expresiones. Como que quiero estar solo justo ahora."

show hanako emb_sad
with charachange

ha "¿Iwanako…?"

hi "No es nada. Gracias por traerme esto, las dos."

show misha hips_grin
with charachange

mi "Debo pensar que así es, después de todo lo que pasamos para dártela~."

show misha hips_frown
with charachange


"Doy un paso atrás y digo adiós. Misha incluso hace un puchero teatralmente mientras salgo por la puerta, pero Shizune y Hanako permanecen visiblemente curiosas sobre mi reacción. Espero que no me vayan a preguntar sobre esto después."

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_parkambience fadein 2.0

scene bg school_gardens2
with locationskip

play music music_serene fadein 2.0

"El pequeño jardín es, como siempre, una sensación muy placentera. Unas de las más visibles señales de lo bien financiada que está esta escuela, además de su gran tamaño, son la expansión y condición de sus terrenos."

"Un buen número de estudiantes puede verse comiendo el almuerzo, hablando, y jugando en el vivo césped verde."

"Nunca había tenido una vista así en mi ciudad natal. En excursiones, tal vez, pero ciertamente nunca en la escuela o ningún lugar cerca de donde vivía."

"Incluso la banca en la que me siento para leer está caliente gracias al sol de verano, recordándome por qué no he vestido la chaqueta de la escuela ni una vez."

show letter_open_insert:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"Considerando esto, los girasoles y salpicaduras de amarillo vibrante adornando el papel son bastante apropiados para este tiempo. Si solo las palabras escritas en él lo fueran también."

"Aquí estaba, pensando que me las había arreglado para terminar con ella, cuando esta problemática cosa aparece."

"Su escritura luce a lo mucho vagamente familiar, y solo ahora que la veo otra vez recuerdo que ella solía escribir bastante con pluma rosa. Siempre fue muy femenina, a falta de un mejor término."

"Pero también era algo frágil. Nunca supe si me gustaba este aspecto de ella o no, aunque con la llegada de esta carta, esa pregunta parece haberse vuelto bastante insignificante."

"La carta comienza con no mucho más que una actualización del estado de las cosas pasando en su vida. Mi viejo grupo tuvo un buen inicio en el ciclo escolar, muchos están ansiosos por los exámenes que vendrán en el futuro, etcétera."

play sound sfx_paper

hide letter_open_insert
show letter_open_insert_2
with charachange

"Pero termina en una muy personal, aunque corta, nota. Se siente un poco como que escribió la mayor parte de la carta solo para tratar de suavizar el golpe del final."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

$ written_note("Quería por algún medio expresar mis sentimientos, pero las palabras correctas no venían a mí. No podía decir algo para consolarte. Realmente siento no poder haberte apoyado cuando más lo necesitabas, aunque me gustes tanto. Por lo menos ahora, finalmente, puedo ser más honesta.\n\n\n\n")

$ written_note("Si pudiera volver a aquellos días silenciosos en febrero y marzo, te diría que no renunciaras a ti mismo. Eso es lo que diría. Quizás no te hubieses alejado tanto si tan sólo hubiera dicho algo. Espero que hayas podido recuperarte por tu cuenta.\n\n\n\n")

$ written_note("Ahora que la distancia entre nosotros es también física, se siente también más definitiva, de algún modo. Me pregunto si nos encontraremos de nuevo. ¿Tal vez sea mejor si no? Aun así, si te gustaría mantener correspondencia conmigo, por supuesto que puedes escribirme de vuelta. Me agradaría mucho escuchar sobre tu nueva escuela y cómo te está yendo. Te deseo todo lo mejor.\n\nAtentamente, Iwanako")

window show

$ renpy.music.set_volume(1.0, 1.0, channel="music")

"Y así, eso es eso. Nuestra relación ha terminado. Bonito, limpio, y ordenado, sin ambigüedades."

"No me había hecho ilusiones de que podría volver a empezar otra vez. La última vez que me visitó, ninguno de nosotros dijo nada, excepto por aquella palabra que dijo mientras se iba por última vez. “Adiós”."

"Sea como fuere… esto se siente más como un final. La cúspide en un experimento que ambos intentamos, y en el que fallamos."

show letter_open_insert_2:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide letter_open_insert_2
with None

"Un fuerte grito aleja mis ojos de la carta. Solo son unos estudiantes peleándose, con uno de los maestros cercanos aproximándose a hablar con ellos."

mystery "¿Estás bien?"

show yuuko neutral_down at center
with charaenter

"Una voz vacilante viene de mi lado. Por un momento asumo que es Hanako, pero de hecho es Yuuko."

hi "Oh, hola Yuuko. Pensé que estarías en la biblioteca."

show yuuko closedhappy_up
with charachange

"Ella da una sonrisa alegre, una que se adapta bastante a la atmósfera, y agita la envoltura vacía de un paquete en su mano. Debe tener a alguien más cubriéndola mientras fue por algo de comer."

"Me recuerda que no he comido nada aún. Pero no tengo hambre, y saltarme una comida no hará daño."

show yuuko smile_up
with charachange

yu "¿No te molesta si me siento aquí?"

hi "Seguro, adelante."

show yuuko neutral_down at Position(ypos=1.15)
with dissolvecharamove

"Rápidamente deslizo la carta de vuelta a su sobre, deslizando este dentro de mi mochila apoyada contra el lado de la banca mientras Yuuko toma asiento. Ella tira la envoltura en un bote junto a nosotros."

"Sin mucho más que hacer, me reclino y disfruto lo que puedo del sol, silenciosamente reflexionando sobre la carta."


"El suntuoso césped, el claro cielo azul… todo luce tan diferente de como lo hacía entonces. Incluso los alrededores de la escuela, desde la colina y el bosque a su alrededor, son completamente opuestos al escenario urbano que recuerdo."

"Tal vez así es como se siente estar nostálgico. Por otro lado, no es una sensación completamente mala; la percepción del área alrededor de Yamaku, aunque diferente, es también buena. Creo que me podría acostumbrar a ella."

show yuuko smile_down
with charachange

yu "¿Oye, Hisao?"

hi "¿Sí?"

show yuuko worried_down
with charachange

yu "No contestaste mi pregunta antes. No iba a decir nada, pero aún luces preocupado."

show yuuko panic_up
with charachange

yu "Aunque si no quieres decir nada, está bien, no me molesta en absoluto. Em, p-perdón por preguntar algo extraño como eso…"

hi "No importa."

hi "Es solo… recibí una carta de alguien que conocí antes de que viniera a Yamaku. Me hizo pensar en algunas cosas."

hi "Pensé que me las había arreglado para sobrellevar la mayoría de los problemas que mi accidente causó, pero ahora no estoy realmente seguro. Como que deseo nunca haberla visto."

show yuuko worried_up
with charachange

yu "No creo que eso sea bueno, Hisao."

show yuuko neutral_down
with charachange

yu "Cuando mi novio me dejó, lo hizo muy repentinamente, y nunca me dejó saber por qué. Al inicio estuve muy deprimida al respecto, pero decidí perdonarlo."

hi "¿Lo perdonaste? ¿No podría él al menos haber hablado apropiadamente contigo sobre ello?"

yu "Él siempre fue una de esas personas que encuentran difícil acercarse a otros."

yu "Al final, decidí que me enamoré de él por una razón. Él fue una buena persona, y creo que si yo hubiera estado en su posición, probablemente hubiera encontrado igual de difícil tratar de hablarle."

hi "No… veo realmente la conexión con la carta que recibí."

show yuuko worried_up
with charachange

yu "Quiero decir que… em, cómo debería decirlo…"

yu "Debe haber sido muy difícil para esa persona enviar esa carta, y si lo hizo, creo que debió haber pensado mucho acerca de qué escribir exactamente."

"Iwanako logró escribir esta carta y llevar a un final a nuestra relación; algo que nunca logré hacer yo."

"Mientras que yo estoy aquí, tratando de proteger a Hanako lo mejor que puedo, especialmente con Lilly yéndose por un tiempo, y ni siquiera soy capaz de lidiar con mis propios problemas."

show yuuko neutral_down
with charachange

yu "¿Eso tiene sentido?"

"Ella ha tomado mi falta de respuesta y cejas fruncidas como duda. Realmente lee mucho los rostros, justo como otra cierta persona."

hi "Sí, eso tiene sentido."

hi "La carta fue solo una especie de shock, en verdad."

hi "Creo que traté de engañarme a mí mismo pensando que mi vida reinició cuando vine a Yamaku, pero ahora estoy repentinamente consciente de que no fue así. Estoy un poco perdido sobre cómo sobrellevar estos sentimientos."

show yuuko worried_down
with charachange

yu "Creo que eso es algo con lo que realmente no puedo ayudarte. Lo siento."

hi "Está bien. Creo que el poder hablar contigo me ayudó a acomodar las cosas un poco mejor en mi cabeza, así que gracias de todas formas."

show yuuko closedhappy_down
with charachange

"Ella asiente y sonríe dulcemente. Yuuko es una buena chica, así que es una pena que ella se ponga tan nerviosa tan seguido."

play sound sfx_warningbell

show yuuko panic_up
with vpunch

"La campana de la escuela sonando nos sobresalta a los dos."

yu "Ah, ¡se suponía que estaría de vuelta antes de la campana!"

hi "Uups…"

show yuuko worried_up at center
with Dissolvemove(0.3)

"Ella salta fuera de la banca y casi sale corriendo sin decir nada más, pero gira sobre su talón cuando recuerda que hace apenas un momento estaba hablando conmigo."

show yuuko neutral_up
with charachange

yu "Te veo después, Hisao. Anímate, ¿está bien?"

hi "Trataré. Gracias, Yuuko."

stop music fadeout 9.0

hide yuuko
with charaexit

"Con una reverencia rápida, Yuuko parte y comienza su carrera a la biblioteca."

"Su vuelo capta los ojos curiosos de los pocos estudiantes pasando, quienes están caminando pesadamente y sin entusiasmo de vuelta a sus clases después de la diversión."

"Levantándome de mala gana de la banca, me sacudo y me uno a ellos."

"Incluso mientras camino a través de los jardines de vuelta al edificio principal, la idea de la carta en mi mochila no se aparta mucho de mi mente."

stop ambient fadeout 2.0
stop music fadeout 2.0

scene black
with dissolve



label es_H19:

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_traffic fadein 1.0

scene bg city_street2_ni
with locationchange

"La sensación de caminar a través de las calles es de muy profunda nostalgia. Mientras que Yamaku podría ser lo contrario de donde viví en el pasado, la ciudad por la noche es increíblemente familiar."

"Mis ojos se están moviendo constantemente de las luminosas pantallas electrónicas brillando alto en el cielo nocturno, a las lámparas de la calle penetrando la oscuridad con su luz"

"Y a los hombres de negocios disfrutando de sí mismos después del trabajo y hablando afanosamente en la cita con sus parejas."

"Incluso aunque no quisiera, no puedo evitar adentrarme en cada aspecto de la ciudad."

show akira basic_boo_ni:
    center
    xpos 0.59
show lilly cane_smileclosed_cas_ni:
    center
    xpos 0.41
with charaenter

"Lilly está caminando a mi izquierda con su bastón balanceándose de aquí hacia allá, agarrándose del brazo de su hermana mientras habla con ella."

"Comparado a viajar en taxi o autobús, ser llevado por Akira en su más bien agradable auto fue una experiencia mucho más disfrutable."

show hanako invis_close:
    center
    xpos 1.0
with None

scene bg city_street2_ni at bgleft
show akira basic_boo_ni:
    center
    xpos 0.39
show lilly cane_smileclosed_cas_ni:
    center
    xpos 0.21
show hanako basic_distant_cas_close_ni at tworight
with dissolvecharamove

"Aunque tal vez no para la persona a mi lado."

"Mientras que Lilly estaba acostumbrada a la forma de manejar de su hermana, y a mí como que me gustó un poco la emoción, Hanako estuvo agarrándose muy fuertemente de la puerta durante la mayor parte del viaje."

show hanako basic_smile_cas_close_ni
with charachange

ha "T-todo luce tan b-bonito por la noche…"

show hanako emb_downtimid_cas_close_ni
with charachange

"Hanako rápidamente mira hacia abajo otra vez cuando accidentalmente capta la mirada de alguien."

hi "Sí, así es."

"Mi respuesta no está muy pensada, dado que estoy distraído por tantos pensamientos que encuentro difícil seguir con la charla."

"Una de esas distracciones, además de los lugares de interés de la ciudad, es cómo luce Hanako."

"Esta es la primera vez que la he visto en algo más que su uniforme o su pijama. Me hizo detenerme por un momento cuando vi por primera vez su ropa, al encontrarnos en el portón de la escuela."

"Considerando lo mucho que baja su cabeza cuando la gente camina cerca de nosotros, imagino que la boina que viste es más que un accesorio de moda."

"Aunque inicialmente tenía desconfianza del plan de Lilly de llevarnos a la ciudad, cuando cayó la noche se hizo obvio que ella había pensado en esto. No mucha gente le ha prestado tanta atención a Hanako."

hi "Así que… estamos en la ciudad. ¿Alguna idea de qué hacer?"

show akira basic_smile_ni
with charachange

"Akira lanza una sonrisa. Algo me dice que ella es la que va a tomar esta decisión en particular, incluso si su hermana pudo haber propuesto la salida en primer lugar."

show akira basic_ending_ni
with charachange

aki "Ya lo verás. Solo síguenos."

"Asiento, y trato lo mejor posible de reprimir mi mueca. Después de lo que pasó durante la fiesta de cumpleaños de Hanako, no confío tanto en el juicio de Akira."

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
$ renpy.music.set_volume(0.1, 0.0, channel="music")
play music music_jazz fadein 14.0

scene bg city_street3_ni
with locationchange

"Continuamos caminando, y noto que estamos pasando más y más cafés, restaurantes, y otros establecimientos de comida."

"De vez en cuando un hombre borracho en traje sale de un bar, usualmente siendo ayudado por otro, pero la mayor parte de los clientes alrededor de esta área de la ciudad lucen jóvenes y a la moda."

"Diferentes tipos de música vienen y van mientras pasamos por cada negocio."

"La discordancia creada por el sonido encimado debería ser irritante, pero me recuerda tan fuertemente a los momentos que pasé en la ciudad con mis viejos amigos que no me molesta."

"Hanako y yo hemos empezado a distanciarnos un poco de Lilly y Akira. Pero eso termina cuando escucho un ligero golpe sordo de alguien atrás de mí."

show hanako defarms_shock_cas_ni
with vpunch

ha "¡P-p-perdón…!"

"Para el momento en que ella se endereza de su reverencia de disculpa, el hombre de negocios de mediana edad con el que tropezó está caminando lejos después de murmurar una poco entusiasta disculpa."

show hanako emb_downtimid_cas_ni
with charachange

"Hanako luce un poco desanimada por la experiencia, y mientras avanza rápidamente para emparejarse a mi paso, noto su cabeza bajando una vez más. Probablemente chocó con él porque estaba viendo al piso y no adonde estaba yendo."

show hanako emb_timid_cas_close_ni
with charachange

"Me acerco a su lado un poco y pongo una mano en su hombro más alejado, acercándola."

ha "¿Hisao?"

hi "Está bien. Puedes caminar más cerca de mí si quieres."

show hanako emb_smile_cas_close_ni
with charachange

"Hanako duda, pero eventualmente asiente con aprobación."

stop ambient fadeout 1.0
$ renpy.music.set_volume(0.5, 10.0, channel="music")

scene bg city_karaokeext_ni
show crowd_ni
show akira basic_smile_ni:
    center
    xpos 0.39
show lilly cane_listen_cas_ni:
    center
    xpos 0.21
show hanako basic_smile_cas_close_ni at tworight
with locationskip

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_crowd_outdoors fadein 2.0

"Después de un par de veces en que pensé que habíamos llegado al destino de Akira, alcanzamos nuestro objetivo. Para este momento estamos bajo los andadores elevados y más allá de los lugares más estridentes e intensamente iluminados."

"Estoy un poco sorprendido. La edad promedio de aquellos a nuestro alrededor es distintivamente mayor, y el olor de humo de cigarrillo es bastante denso."

"Sin embargo el área está lejos de ser miserable, y es un poco divertido ver la reacción de Lilly al olor del humo."

"Aunque enmascarada por los cuchicheos de aquellos a nuestro alrededor, puede escucharse música de jazz emanando de adentro. Mirando arriba al débilmente iluminado letrero, se vuelve obvio por qué."

hi "Un club de jazz. Debo admitir, esto no es lo que esperaba."

show lilly cane_giggle_cas_ni
with charachange

"Lilly da un bufido divertida y una sonrisa."

show lilly cane_smileclosed_cas_ni
with charachange

li "De alguna forma siento que debí haberlo sabido, Akira."

"Mientras hablamos afuera, noto más y más extrañas miradas de reojo dirigidas hacia nuestra posición. La gente se descubre viéndonos y se voltea incómodamente, pero eso solo lo hace más obvio."

"Había notado esto ocasionalmente cuando estábamos caminando, pero es más marcado ahora."

"Nunca había experimentado nada como esto en mi vida. Un chico adolescente normal japonés, solo un poco más alto de lo normal, no es el tipo que atraería atención sin hacer un poco de esfuerzo."

show akira basic_laugh_ni
with charachange

aki "Oigan, vamos. Solo porque son adolescentes, no significa que no puedan tener gusto. ¿Cierto?"

hi "Bueno… realmente no me molesta la música, si eso es lo que quieres decir."

show hanako cover_bashful_cas_close_ni
with charachange

ha "Tampoco… m-me… molesta…"

"Ella solo se las está arreglando para forzar a las palabras a salir. Contrasta bastante a cuando estamos solos en Yamaku, y me decepciona un poco que ella esté tan nerviosa por lo que se supone que es pasar un buen rato en la ciudad."

"Es difícil leer el rostro de Hanako pues se mantiene mirando abajo. No es de sorprender si no viene mucho a la ciudad por esto, y me vuelve un poco agradecido de que mis propias cicatrices son fácilmente ocultadas."

"Lilly tiene una forma similar de atraer las miradas de la gente, pero la razón de ello es claramente diferente. Difícilmente luce como nativa, y lo mismo puede decirse de su hermana. Eso es mucho más visible que su ceguera, desde lejos."

"Tal vez no puede ver esto por sí misma, pero tengo pocas dudas de que no pueda escuchar las extrañas frases susurradas por la gente que piensa que está fuera de su rango de escucha."

"Sea como fuere, ella no parece mostrar ninguna señal de molestia o placer por la atención."

hide akira
hide lilly
with charaexit

"Pero Akira está aún tan segura de sí misma como siempre. Lanzando una sonrisa, entra a grandes pasos con Lilly a su lado y los dos seguimos tras de ellas."

stop ambient fadeout 1.0
$ renpy.music.set_volume(1.0, 10.0, channel="music")

scene bg city_clubint:
    center
    xpos 0.6
show crowd
with locationchange

$ renpy.music.set_volume(0.8, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 1.0

"Esperaba que mis ojos necesitaran ajustarse a la luz de adentro, pero no está mucho más iluminado que afuera."

"La música que escuchamos está más clara ahora, mezclada con los sonidos de copas moviéndose en las mesas y el mostrador, y las roncas pláticas de los clientes."

"Mirar a mi derecha revela la fuente de la música, un grupo de jazz tocando unas mesas más allá."

"Los clientes parecen ser en su mayoría hombres, y aunque hay un puñado de mujeres, nadie parece de menos de treinta. Además de nosotros, por supuesto."

"Se siente un poco como si nos hubiéramos topado con los años veinte, y la atmósfera es bastante agradable. Si no estoy completamente cómodo es únicamente por mi edad, pero si fuera más viejo, probablemente me sentiría en casa."

show hanako basic_smile_cas_close at tworight
with charaenter

"Hanako luce un poco más relajada ahora, probablemente debido a que nadie la está viendo. Todos están hablando entre ellos, bebiendo, o mirando a la banda."

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

show akira basic_smile behind crowd:
    center
    easein 1.0 ypos 1.06
hide crowd
with Dissolve(1.0)

"Akira toma asiento casualmente en el mostrador sin siquiera mirar alrededor. Probablemente ya ha venido aquí antes."

show lilly basic_smileclosed_cas:
    twoleft
    xpos 0.25
    easein 1.0 ypos 1.1
with Dissolve(1.0)

"Lilly retrae su bastón, sintiendo el banquillo y la orilla del mostrador antes de tomar asiento junto a su hermana. El barman toma un pequeño descanso puliendo una copa para mirar a Lilly, antes de dejarla y aproximarse."

"Barman" "Buenas noches, chicas. ¿Qué les vamos a servir?"

show akira basic_ending:
    center
    ypos 1.06
with charachange

aki "Solo un whisky escocés, gracias. ¿Lilly?"

show lilly basic_cheerful_cas:
    twoleft
    xpos 0.25 ypos 1.1
with charachange

li "¿Podría darme una copa de cham—{w=0.5}{nw}"

show lilly basic_surprised_cas
show akira basic_boo
with vpunch

"Un codo en traje negro golpea su lado bruscamente."

show lilly basic_weaksmile_cas
with charachange

li "Jugo de naranja, por favor."

"Barman" "No hay problema, viene ahora mismo."

"El barman comienza a servir las bebidas. Un par de segundos pasan antes de que Akira recuerde repentinamente que Hanako y yo estamos de hecho aquí, y gire hacia nosotros."

show akira basic_smile
with charachange

aki "¿Ustedes dos quieren algo, o solo van a pararse ahí?"

"Hanako parece estarse poniendo un poco inquieta. No importa dónde nos vayamos a sentar, va a haber gente justo a su lado, y no creo que ella luzca convincentemente mayor de veinte, a diferencia de Lilly."

show bg city_clubint:
    xpos 0.4
show akira basic_smile:
    xpos 0.3
show lilly basic_weaksmile_cas:
    xpos 0.05
show hanako basic_smile_cas_close:
    xpos 0.5
with charamove

"Viendo alrededor, hay una sección de juegos a nuestra derecha. Un par de mesas de billar pueden verse en la esquina, y nadie las está usando tampoco."

"Volteo a ver a Hanako, a punto de preguntarle si quiere jugar, pero ya está viendo anhelantemente en la misma dirección. Tal vez dice algo el que podamos arreglárnoslas con tan pocas palabras hoy en día."

hi "Vamos a ir a jugar billar por allá."

show akira basic_boo
with charachange

"Akira se reclina para ver atrás de mí, antes de encogerse de hombros y reacomodarse otra vez."

show lilly basic_giggle_cas
with charachange

li "Parece que tendrás que soportar solo conmigo como compañía. Qué desafortunada."

show akira basic_smile
with charachange

aki "Diviértanse ustedes dos."

$ renpy.music.set_volume(0.8, 1.0, channel="music")
stop ambient fadeout 14.0

hide hanako
with charaexit

"Damos la vuelta y partimos hacia la abandonada esquina, con Hanako tomando la delantera."

"La posibilidad de un agradable y tranquilo juego lejos de todos la hace caminar notablemente más rápido. Sus ojos se mantienen firmemente fijos en su premio."

scene bg city_clubpool
with locationchange

"La mesa es de tamaño completo y bien iluminada a pesar de la oscuridad adyacente, gracias a las brillantes luces sobre nuestras cabezas. Una enorme pintura de… algo… cubre la pared."

"No hay mucha gente apiñándose en esta esquina del club, y puedo ver a Hanako poniéndose menos tensa como resultado."

show hanako basic_smile_cas at center
with charaenter

ha "¿Tú… sabes cómo jugar?"

hi "No soy experto, pero sí, lo sé."

show hanako basic_bashful_cas
with charachange

ha "Entonces em… ¿ocho bolas?"

hi "Seguro."

hide hanako
with charaexit

"Hanako agarra la tiza y dos tacos de un juego que está contra una de las paredes, mientras yo junto las bolas de las canastillas de la mesa y agarro el triángulo de un estante debajo."

"Ella pacientemente espera mientras preparo la mesa."
"Después de introducir la última bola en el triángulo y hacer algunos últimos ajustes, termino teniendo que pelear con mis urgencias perfeccionistas de alinear la fila de bolas de abajo exactamente perpendicular con las orillas."


"Con las bolas acomodadas y listas para jugar, doy un paso atrás y tomo mi taco del brazo estirado de Hanako. Llevo a cabo una rápida inspección de la punta antes de estar satisfecho de que está en buena condición."

hi "Entonces ¿has jugado antes?"

show hanako cover_bashful_cas
with charaenter

ha "Una vez… o dos. Yo solo como que… conozco las reglas."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

"El aire entre nosotros se siente un poco incómodo. Ella aún está muy nerviosa; entendible, dado que estamos en público."

"Eventualmente el silencio se vuelve demasiado incluso para Hanako, y comienza a tartamudear en voz baja."

$ renpy.music.set_volume(0.8, 1.0, channel="music")

show hanako basic_worry_cas
with charachange

ha "¿Qui-quién… em-empieza?"

"Pienso por un momento antes de alcanzar mi bolsillo y agarrar una moneda."

hi "Yo tomo cara, tú cruz."

"Después de una afirmación de Hanako con la cabeza, lanzo la moneda al aire, la atrapo, y la volteo en el dorso de mi mano izquierda."

hi "Parece que eres tú la que iniciará."

$ ksgallery_unlock("ev hanako_billiards_distant")
scene ev hanako_billiards_break
with locationchange

"Hanako asiente otra vez, antes de tomar su posición al final de la mesa."

"Ella usualmente no es tan callada a mi alrededor, pero no estoy del todo seguro si es por la pequeñez de información sobre su pasado que se le escapó hace unos momentos."

scene bg city_clubpool
with flash

play sound sfx_billiards_break

"El taco regresa en un gesto practicado antes de golpear de lleno en el centro de la bola blanca con un ruido sordo. La bola blanca patina a través de la suave extensión verde antes de estrellarse en las cuidadosamente acomodadas bolas al otro lado."

"Las bolas ruedan a través de la mesa con velocidad. El golpe inicial fue bueno, con las bolas siendo bien distribuidas alrededor de la mesa. Mis ojos ya están revoloteando de una a otra para elegir los candidatos más fáciles para meter."

play sound sfx_billiards

"Hanako se retira de los lados y hago mi tiro."

show hanako basic_smile_cas at center
with charaenter

ha "Bien hecho."

"Es solo después de que Hanako dice esto que me doy cuenta de que la bola a la que le estaba apuntando fue metida."

"Volteo a verla y noto una pequeña sonrisa en su cara. Es bueno el cómo jugar juegos parece relajarla un poco."

hi "Supongo que soy las rayadas, entonces."

show hanako cover_distant_cas
with charachange

"Doy un paso atrás y la dejo dar su siguiente tiro, pero ella no avanza a la mesa. En lugar de eso, ve hacia abajo y frota su brazo."

"Para estos momentos ya puedo identificar esto como uno de sus gestos que significan que quiere decir algo, pero no es lo suficientemente segura de sí misma para decirlo."

hi "¿Qué sucede?"

show hanako cover_bashful_cas
with charachange

ha "Es solo… tenías una… l-linda sonrisa. ¿Te gusta… jugar esto?"

"Suspiro y me reclino contra la mesa."

hi "Me gusta jugar, sí. Aunque creo que estaba sonriendo porque es realmente nostálgico."

show hanako def_worry_cas
with charachange

"Hanako inclina su cabeza con aire de duda."

hi "Mis amigos y yo solíamos jugar billar bastante seguido en los centros de juegos cerca de donde viví, y en la noche también."

show hanako basic_worry_cas
with charachange

ha "T-tus padres no…"

hi "Mis papás trabajaban, así que no les importaba que no estuviera en casa. También me mantenía entre los mejores con el trabajo de la escuela muy fácilmente, así que había mucho tiempo para hacer otras cosas al anochecer."

show hanako basic_distant_cas
with charachange

"Nuestra conversación termina, con Hanako tímidamente sacando lo mejor de sí. En respuesta, me alejo de la mesa y la dejo tomar su turno en tirar."


scene ev hanako_billiards_smile
with locationchange

"No hay muchas lisas en posición sencilla, así que Hanako se inclina y se lleva un rato en alinearse adecuadamente."

scene ev hanako_billiards_smile_close:
    truecenter
    zoom 1.0 subpixel True
    easein 6.0 zoom 0.8
with flash

"La expresión de Hanako es la misma que cuando jugamos ajedrez; relajada pero con concentración."

"Los atletas algunas veces hablan sobre meterse en una zona donde nada innecesario entra en sus mentes, y me pregunto si eso es algo que ella puede hacer."

"Su postura es buena. Mejor que la mía, eso es seguro. Está muy cerca a un modo de juego de libros de texto, mientras que yo tiendo a contorsionarme a la posición que siento es la más natural para el tiro que estoy dando."

scene ev hanako_billiards_serious
with locationchange

"Ella alinea el taco. Este regresa, y ella hace un par de movimientos de práctica para asegurarse de que está alineado correctamente."

"Hanako se toma el juego muy en serio. Es el único pasatiempo real que sé que tiene, además de leer. Se siente bien poder compartir este tipo de experiencia con ella."

scene bg city_clubpool
with flash

play sound sfx_billiards

"Ella da el tiro después de cuidadosa consideración, y la bola blanca se acerca a la bola posicionada en un ángulo ligeramente incómodo cerca de la esquina."

"La cuidadosa preparación de Hanako rinde frutos cuando la bola blanca golpea y manda a la otra bola rodando hacia la canastilla de la esquina."

"Por un momento parece que se detendrá en la orilla del hoyo, pero eventualmente se inclina solo lo suficiente para caer dentro."

hi "Hombre, ese fue un tiro difícil. Si puedes sacar eso, no creo tener muchas esperanzas."

show hanako emb_emb_cas at center
with charaenter

ha "No soy… t-tan buena…"

hi "Aunque no es solo el disparo; incluso cuando te alineaste lucías realmente seria. Eres así con el ajedrez también."

show hanako emb_downsmile_cas
with charachange

"El elogio la altera un poco. Ella acomoda el taco contra la mesa y se queda de pie, girando hacia mí."

ha "Solo… me gusta ese tipo de cosas…"

"Sus ojos están jugueteando y girando con fuerza."

show hanako emb_downtimid_cas
with charachange

ha "Cuando estaba en el orfanato… yo solo… m-me mantuve haciendo las cosas que me gustaban… antes."

ha "Si j-jugaba juegos con los otros, e-eso era suficiente para los ayudantes así, así que…"

"Nunca lo pensé de esa forma. El personal en el orfanato querría naturalmente que todos socializaran al menos un poco."

hi "Si está bien que pregunte… ¿cómo fue para ti el orfanato?"

show hanako emb_sad_cas
with charachange

ha "¿P-por qué quieres saber?"

"He tocado una cuerda sensible, pero el hecho de que respondió muestra que hay al menos una oportunidad de que conteste a mi pregunta. Antes ella seguramente se habría solo alejado de esta sin decir palabra."

show hanako emb_blushing_cas
with charachange

ha "Te… diré, pero…"

hi "¿Pero…?"

show hanako cover_worry_cas
with charachange

ha "¿Podrías… d-decirme quién es… I-Iwa… n-nako?"

$ renpy.music.set_volume(0.2, 1.0, channel="music")

hi "¿Iwanako…? Oh, la carta."

"Me pregunto por cuánto ha estado esperando la oportunidad correcta para preguntarme esto. Estoy sorprendido, pero no vacilo. Compartir información es naturalmente una cuestión de dar y recibir."

$ renpy.music.set_volume(1.0, 8.0, channel="music")
$ renpy.music.set_volume(0.4, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 8.0

hi "Es… alguien que solía gustarme."

show hanako basic_normal_cas
with charachange

"Su nerviosismo descendió, al menos por el tiempo que le tomó preguntar. Su curiosidad está sacando lo mejor de ella, y me siento un poco incómodo de ser interrogado sobre esto, sobre todas las cosas."

"No hay forma en que podría sacar mis sentimientos sobre Iwanako aquí. Ni siquiera yo mismo sé qué sentimientos tengo con relación a ella, incluso después de hablar con Yuuko más temprano, y quiero evitar el tema cerca de Hanako."

show hanako def_worry_cas
with charachange

"Hanako no luce muy satisfecha con el incómodo final de la discusión, pero lo piensa mejor acerca de continuarlo. Solo se las estaba arreglando para preguntármelo en primer lugar, sin saber que no querría hablar sobre ello."

"Me muevo para finalmente hacer mi tiro. La falta de charla entre nosotros se llena con las pláticas de otros clientes y la banda al otro lado del club."

hide hanako
with charaexit

"Descubriendo un disparo que no luce tan difícil, intento hacerlo."

play sound sfx_billiards

"La bola blanca golpea a la bola, y la trayectoria es más o menos correcta, pero le di mucha fuerza. Esta rasguña la esquina del hoyo y se mueve a un lado, apenas rodeando la tronera."

"Aprieto mis dientes un poco. Era bastante bueno en este juego, y es frustrante haberme deteriorado tanto."

"Doy un paso atrás y dejo a Hanako tomar su turno, lanzando una mirada hacia donde Lilly y Akira están sentadas. Están hablando afanosamente entre ellas."

scene ev hanako_billiards_serious
with locationchange

"Volteo hacia Hanako mientras ella tira. Con la misma cara de antes, se alinea y empuja fuertemente el taco."

scene bg city_clubpool
with flash

play sound sfx_billiards

"Tal como antes, ella mete la bola a la que estaba apuntando. Aunque se introduce en la tronera de un lado más limpiamente que la anterior. Parece que está metiéndose más en el ritmo del juego."

hi "Muy bien hecho."

"Ella duda por un momento, y comienza a dirigirse a mí sin voltear su cabeza."

scene ev hanako_billiards_smile_med
with locationchange

ha "El orfanato… era agradable. Se sentía un poco como se siente Yamaku… y el personal era m-muy atento."

show ev hanako_billiards_distant_med
with charachange

ha "Pero m-mientras los años pasaban, me di cuenta de algo. Yo era d-diferente."

"Se siente extraño escucharla hablar tan francamente de sí misma. Ella está audiblemente forzando las palabras a salir. Me recuerda a cuando ella insistió en decirme sobre el incendio."

"Hanako debe sentir que tiene que decirme tales cosas, si estoy dispuesto a decirle sobre mi propio pasado."

"Su agarre en el taco se aprieta mientras continúa hablando."

$ ksgallery_unlock("ev hanako_billiards_timid")
show ev hanako_billiards_timid_med
with charachange

ha "La m-mayoría de los niños ahí estaban en adopción, tal como yo lo estaba. Pero a diferencia de mí… ellos gradualmente se fueron, u-uno por uno. Para cuando fui a Yamaku, yo estaba… entre los niños más grandes ahí."

ha "Por un tiempo, a-ayudé con algunos de los n-niños más jóvenes, p-pero eventualmente…"

scene bg city_clubpool
with locationchange

"Coloco una mano en su hombro. Está forzándose en estos momentos."

hi "Está bien."

show hanako emb_blushtimid_cas_close at center
with charaenter

"Parece un poco sorprendida por un momento, pero entonces asiente dejando su taco y girando hacia mí."

show hanako basic_worry_cas_close
with charachange

ha "¿Realmente… crees eso?"

hi "Sí, lo creo. Incluso mientras Lilly esté fuera, estaré alrededor para protegerte, ¿cierto?"

show hanako basic_normal_cas_close
with charachange

"Hanako me mira por un largo rato, me toma un poco con la guardia baja."

"Su expresión de antes no ha cambiado, aún luciendo un tanto llorosa, y los silencios entre nosotros no son inusuales. Pienso que el hecho de que está manteniendo un contacto visual tan prolongado es lo que hace que esto se sienta un poco raro."

"Se siente como si estuviera juzgándome. Es un sentimiento muy extraño y algo incómodo."

hi "¿Hanako…?"

show hanako cover_smile_cas_close
with charachange

ha "E-entiendo. Gracias."

"Ella sonríe y voltea a otro lado un poco, pero se siente forzado. Hanako no es muy buena fingiendo emociones, y esta no es la excepción."

hide hanako
with charaexit

"Me muevo a la mesa y tomo mi turno para intentar distraerme, pero no parece funcionar. ¿Ella piensa que no estoy dispuesto a la tarea de ayudarla? ¿Está decepcionada de mí?"

"Tal vez estoy pensándolo demasiado. Aunque sus silencios son aceptados para este momento como un hecho de la vida, algunas veces desearía que hablara más."

play sound sfx_billiards

"Con un golpe sordo, envío la esfera blanca a correr a través de la mesa hacia mi objetivo."

show hanako def_strain_cas at center
with charachange

ha "Ah…"

"Hanako ve lo que está pasando tal como yo. La bola golpea duro, y la bola rayada que intentaba meter girando hacia la bola ocho."

"Con seguridad, mientras Hanako y yo observamos y mordemos nuestros labios, estas conectan y la bola ocho rueda lentamente hacia la tronera de la esquina."

show hanako basic_smile_cas
with charachange

"Todo lo que puedo hacer es suspirar. Pero parece que Hanako está sonriendo otra vez, así que tal vez no fue un desperdicio."

hi "Ese fue un tiro terrible, tú ganas. Parece que me estoy oxidando bastante después de todo este tiempo."

hide hanako
with charaexit

"Hanako se inclina y comienza a meter las bolas restantes en las troneras más cercanas. Casi pregunto si podríamos jugar otro juego, pero una mirada rápida a mi reloj confirma que se está haciendo bastante tarde."

"Lilly y Akira parecen estar aún tomando en el mostrador. Parece que tendremos que arrastrarlas fuera."

ha "Em, Hisao…"

scene ev hanako_billiards_distant
with locationchange

"Giro hacia Hanako, quien aún está en la mesa de billar disparando a las bolas. Su voz suena diferente de antes."

scene ev hanako_billiards_smile
with charachange

ha "Estoy… aquí para ti también…"

stop ambient fadeout 2.0

hi "Ah…"

"Repentinamente me encuentro sonrojándome. Es simplemente natural que ella respondiera de esta forma, dado lo que dije antes, pero aún es un shock escucharla."

scene ev hanako_billiards_smile_close:
    xalign 0.0 yalign 0.0 zoom 0.8 subpixel True
    acdc_warp 20.0 zoom 1.0
with locationchange

"¿Cuál es mi relación con esta chica, realmente? Quiero protegerla, hacerla feliz… No estoy muy seguro de que sea algo como amor, pero tampoco creo que estos sean el mismo tipo de sentimientos que tengo por Lilly."

"Siento pena por ella, el que haya pasado por tanto en su vida. Sus padres murieron en un incendio casero, y ella vivió en un orfanato por gran parte de su niñez… ni siquiera puedo imaginar ese tipo de vida."

"Pero siento que hay poco que pueda hacer por ella, especialmente ahora que Lilly se va a su país."

stop music fadeout 10.0

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_traffic fadein 4.0

scene bg city_karaokeext
show akira basic_boo_ni:
    center
    xpos 0.39
show lilly cane_smileclosed_cas_ni:
    center
    xpos 0.21
show hanako basic_normal_cas_close_ni at tworight
with locationskip

"Hanako y yo terminamos acomodando la mesa y los tacos, y recogemos a Lilly y Akira en nuestro camino afuera del club."

"Se siente como si algo hubiera cambiado entre Hanako y yo. No puedo decir lo que es, pero Hanako está actuando diferente ahora. Siento que estamos más apartados, si algo puedo decir."

show akira basic_smile_ni
with charachange

aki "¿Así que, se divirtieron?"

show hanako emb_smile_cas_close_ni
with charachange

"Hanako y yo asentimos. El juego fue bueno, y ambos aprendimos más sobre cada uno, así que es una respuesta honesta."

show lilly cane_sleepy_cas_ni
with charachange

"Lilly parece estar distraída."

hi "¿Preocupada por el viaje, Lilly?"

"Ella se detiene antes de suspirar y sonreír débilmente."

show lilly cane_weaksmile_cas_ni
with charachange

li "Un poco. Significa bastante."

show akira basic_laugh_ni
show lilly cane_surprised_cas_ni
with vpunch

"Su comentario se gana una palmada en el hombro de su hermana. Hanako sonríe también."

show hanako basic_smile_cas_close_ni
with charachange

ha "Estarás bien, Lilly. Espero que puedas disfrutar tu tiempo allá."

show lilly cane_smile_cas_ni
with charachange

li "Gracias, Hanako. Trataré. Será lindo estar de vuelta con mi familia, después de todo, no importa lo corto que el tiempo pueda ser."

"Con eso, los cuatro comenzamos a caminar al estacionamiento donde el auto de Akira está. Continuamos hablando entre nosotros, pero más que nada charlas triviales."

stop ambient fadeout 2.0
stop music fadeout 2.0

scene black
with dissolve



label es_H20:

play music music_daily fadein 2.0

scene bg school_girlsdormhall
show lilly basic_smile_cas at twoleft
show hanako basic_normal_cas at tworight
with locationchange

hi "Bien entonces. ¿Tomarás el autobús, Lilly?"

show lilly basic_smileclosed_cas
with charachange

"Lilly hace una seña hacia una maleta grande que está junto a ella."

show lilly basic_weaksmile_cas
with charachange

li "Tendré que llevar esta conmigo, así que he llamado un taxi. Nos verá en los portones de la escuela en unos cinco minutos."

hi "Ah, ya veo."

show lilly basic_sleepy_cas:
    ypos 1.1
with dissolvecharamove

"Lilly se agacha y siente la agarradera de su maleta. Su peso le causa algunas dificultades, así que rápidamente le ofrezco llevarla yo mismo."

show lilly basic_smileclosed_cas at twoleft
with dissolvecharamove

li "Eso es demasiado amable de tu parte, Hisao."

"Ella no repara en aceptarlo, y termino tomándola. No es lo que llamaría ligera, pero no es exactamente pesada, tampoco. No creo que vaya a tener muchos problemas llevándola."

show lilly basic_weaksmile_cas
with charachange

li "Bueno, gracias entonces. Aunque debemos apresurarnos, si el taxi se va entonces tomará un tiempo llamar uno nuevo. ¿Estás lista, Hanako?"

show hanako cover_worry_cas at tworight
with charachange

ha "S-sí. Vamos."

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_parkambience fadein 2.0

scene bg school_gate at bgright
with locationskip

"Nos apresuramos al portón tan rápido como podemos, solo para encontrarnos con que el taxi aún no ha llegado."

hi "Bueno, nada como un poco de ejercicio en la mañana. El enfermero me dijo que debería estar haciendo eso."

show lilly basic_weaksmile_cas at center
with charaenter

li "Creo que probablemente él tenía otras cosas en mente, Hisao. Y probablemente más regularmente. ¿Pretendes estar ayudando a la gente con su equipaje todos los días?"

hi "Supongo que no. Como sea, parece que tendremos que esperar un poco. ¿Cuánto hay que esperar antes de llamarlos otra vez?"

show lilly basic_smileclosed_cas
with charachange

li "Diría que otros diez minutos, pero nunca me han decepcionado antes. Probablemente solo hay un poco de tráfico."

hi "Bien."

hi "Entonces ¿qué tan largo es el viaje a Escocia?"

show lilly basic_smile_cas
with charachange

li "Unas dieciséis horas, si recuerdo bien. Es un poco difícil decirlo con el cambio de husos horarios."

show bg school_gate at center
show lilly basic_smile_cas at twoleft
with charamove

show hanako defarms_worry_cas at tworight
with charaenter

ha "Tan largo…"

"Es ahora que me doy cuenta de que Hanako ha estado inusualmente quieta, incluso para ella. No maneja bien el estrés, así que luce realmente tensa."

hi "Sí, no puedo imaginar estar en un avión por tanto tiempo."

"Solo he viajado en unas cortas vacaciones familiares al norte, así que es realmente difícil de imaginar. Si Hanako pasó mucha de su niñez en un orfanato, probablemente viajó muy poco, ya no se diga volar."

show lilly basic_weaksmile_cas
with charachange

li "No es tan malo. Pasaré la mayor parte de él durmiendo o practicando mi inglés. Difícilmente lo uso aquí así que necesito refamiliarizarme con él un poco."

show hanako cover_worry_cas
with charachange

ha "¿T-tu acento… será un problema?"

show lilly basic_smile_cas
with charachange

li "No me preocuparía mucho sobre ello. Podría ser un problema al inicio, pero debería estar bien una vez que me acostumbre."

show hanako basic_worry_cas at Position(ypos=1.14)
show lilly basic_smileclosed_cas at Position(ypos=1.17)
with dissolvecharamove

"Todos pasamos a sentarnos en la pequeña banca junto al portón de la escuela en silencio."

"Extrañamente, incluso aunque sé que Lilly está yéndose lejos, no puedo pensar en nada qué decirle. Lilly es una persona confiable, así que podría ser porque no es en quien estoy pensando más."

show hanako emb_downsad_cas
with charachange

"Lilly podría no ser capaz de verlo, pero Hanako está mordiéndose las uñas nerviosamente. Me muevo para hablarle, pero puedo escuchar un motor esforzándose en subir la colina antes de tener la oportunidad."

hi "Ah, creo que el taxi está en camino…"

show lilly basic_cheerful_cas
with charachange

li "Bien localizado Hisao, apenas lo escuché también."

"Una pequeña oleada de orgullo me invade. Haber notado algo al mismo tiempo que Lilly debe significar que me he vuelto más consciente de mis alrededores."


"Como sea, no tendremos que llamar a la compañía de taxis, ni preocuparnos de perder el vuelo de Lilly."

show hanako basic_worry_cas at tworight
show lilly basic_smileclosed_cas at twoleft
with dissolvecharamove

"Una vez que el taxi se detiene donde estamos parados, el conductor baja una ventanilla y se asoma. Después de confirmar que, sí, Lilly es la misma Lilly Satou que contrató el viaje, arreglamos su equipaje."

hide lilly
with charaexit

"El conductor abre la cajuela del taxi y toma el equipaje de Lilly, Lilly sube al asiento trasero mientras él lo coloca en la cajuela y la cierra."

"Después de volver a su asiento y cerrar las puertas, él espera a que demos nuestras despedidas."

show hanako emb_downtimid_cas
with charachange

ha "Que tengas un buen viaje, Lilly."

hi "Cuídate."

"Hanako luce entendiblemente deprimida, y eso es bastante obvio incluso en su voz."

li "Por supuesto que lo haré. Estaré de vuelta pronto, no te preocupes. Habrá aún otra persona aquí para ti, ¿o no, Hisao?"

hi "Sí, seguro."

show hanako emb_blushtimid_cas_close
with characlose

"Giro y sonrío a Hanako, poniendo mi mano en su hombro."

show hanako emb_downtimid_cas_close
with charachange

"Ella solo logra mantener el contacto visual conmigo por un par de segundos, sus mejillas rojas todo el tiempo, antes de mirar otra vez a Lilly."

hi "Nos vemos, Lilly."

show hanako basic_worry_cas_close
with charachange

ha "¡Adiós!"

stop music fadeout 6.0

"Lilly nos da sus despedidas a ambos con una justa cantidad de renuencia. Sin más dilación, el conductor enciende el motor una vez más y comienzan su viaje cuesta abajo, y hacia el aeropuerto."

"Ambos nos quedamos de pie en los portones por un largo rato incluso después de que han desaparecido de la vista, sin saber qué hacer realmente."

show bg school_gate at bgleft
show hanako basic_worry_cas_close at center
with charamove

hi "Así que, ¿qué quieres hacer?"

show hanako def_worry_cas_close
with charachange

ha "Yo… no lo sé."

label es_choiceH20:
menu:
    with menueffect
    "¿Quieres ir a la ciudad?":

        return m1
    "¿Qué tal si decimos que está bien por hoy?":

        return m2



label es_H20_1:

scene bg school_gate at bgleft
show hanako def_worry_cas_close at center
with None

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")

"La parada de autobús, de pie a las puertas de la escuela se siente como un sentinela mudo, pone ideas extrañas en mi mente."

hi "¿Quieres que vayamos a la ciudad y busquemos una librería o algo? Tenemos el resto del día libre."

"Es una apuesta grande, dado que a Hanako no le gusta ir a la ciudad. Cuento que hayamos logrado llevarla allá cuando estaba tan oscuro como un pequeño milagro, pero quiero pasar genuinamente más tiempo con ella."

"Como sea, lo más probable es que se negará y volverá a…"

show hanako basic_smile_cas_close
with charachange

ha "Está bien."

hi "¿En serio?"

show hanako basic_bashful_cas_close
with charachange

ha "E-en serio. Vamos."

"No puedo entender por qué Hanako ha decidido estar de acuerdo conmigo, pero no tengo intención de pedirle que cambie de opinión."

stop ambient fadeout 2.0

scene bg city_street2
show crowd
with shorttimeskip

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_crowd_outdoors fadein 2.0

"Saliendo del autobús, inmediatamente noto que mucha gente está a nuestro alrededor. En retrospectiva, debería haber sido obvio; es claro que muchas personas estarán en el centro en una tarde de sábado."

show hanako emb_downtimid_cas_close at center
with charaenter

"Hanako se repliega cerca a mi lado, y puedo sentir su mano agarrando mi brazo fuertemente. Su cuerpo se sostiene contra el mío y su cabeza está inclinada tan abajo que su boina esconde la mayor parte de sus cicatrices."

hi "Así que eh, ¿a dónde deberíamos ir? ¿Una librería?"

"El regalo de Hanako y mis otros gastos necesarios generales han prácticamente agotado mi presupuesto, pero debería poder costearme unos pocos libros. Son algo por lo que trato de reservar algunos fondos de todas maneras."

"Por un segundo pienso que Hanako no me escuchó, pero entonces veo a mi lado y la noto asintiendo casi imperceptiblemente."

show hanako emb_smile_cas_close
with charachange

ha "E-está bien. ¿Co-conoces alguna?"

hi "De hecho, sí. Pasamos algunas cuando Lilly y yo estuvimos buscando tus regalos…"

show hanako emb_downsad_cas_close
with charachange

"La expresión de Hanako se empaña una fracción de segundo. Tengo que recordar dejar de aludir a su cumpleaños."

show hanako emb_timid_cas_close
with charachange

ha "Ustedes dos… ¿se tomaron mucho tiempo?"

"O tal vez juzgué mal la situación."

hi "Queríamos asegurarnos de que consiguiéramos el regalo correcto, después de todo."

show hanako emb_smile_cas_close
with charachange

"Hanako sonríe y se sonroja un poco. Es un pequeño tesoro cuando lo hace."

hi "Como sea, debe haber una librería justo adelante, ¿quieres darle un vistazo?"

show hanako basic_bashful_cas_close
with charachange

ha "S-seguro."

scene bg city_street1
show crowd
with locationchange

"Las multitudes comienzan a formarse mientras nos dirigimos a la librería a lo largo de los andadores elevados. Hanako sujeta también su otro brazo a mí, haciendo nuestro progreso un poco más lento."

"Mientras caminamos, el sonido del tráfico me hace pensar en una posible distracción para ella."

hi "Me estaba preguntando, Hanako… ¿todavía no has pensado sobre cuándo vas a aprender a manejar?"

show hanako cover_worry_cas_close
with charachange

ha "¿M-manejar?"

hi "Sí. Eres afortunada, en cierta forma; no hay muchos estudiantes en Yamaku a los que se les permita manejar."

"No es el mejor tema de conversación, pero quiero intentar distraer a Hanako de la situación. Justo ahora está bastante nerviosa en verdad."

"Por otro lado, todo lo que he hecho es hacerla sentir incómoda, dado que ella probablemente nunca había pensado en ello. Deseo no haber dicho nada."

stop ambient fadeout 0.5

scene bg city_street3 at left
with locationchange

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_traffic fadein 1.0

"No pasa mucho antes de que estemos ante una de las librerías que Lilly y yo pasamos durante nuestra búsqueda."

hi "¿Qué clase de librería digna de sí misma cierra los sábados?"

show hanako def_worry_cas_close at center
with charaenter

ha "Las librerías… ya no hacen mucho dinero, debido a Internet. ¿Tal vez solo tuvieron que cerrar los fines de semana?"

"Ella parece saber mucho sobre tecnología. Supongo que es una ocupación que se prestaría bien para alguien que disfruta la soledad."

hi "Eh, supongo que eso tiene sentido… es más fácil encontrar libros en línea. Como sea, parece que esta idea murió. ¿Algo más que te gustaría hacer?"

show hanako emb_smile_cas_close
with charachange

ha "S-si no… no es molestia… ¿podrías mostrarme dónde compraron mi regalo?"

hi "Seguro, no hay problema. No es lejos de aquí."

hide hanako
with charaexit

show bg city_street3 at right
with charamove_slow

"Doy la vuelta en dirección a la tienda, solo medio seguro de su localización exacta. No quiero una repetición de la última vez; pasar la mitad del día caminando por ahí sin dirección."

hi "Aquí estamos, Antigüedades Otelo."

show hanako basic_normal_cas_close at center
with charaenter

ha "E-es pequeña."

hi "Bueno, sí. Nos tomó a Lilly y a mí un tiempo encontrarla."

show hanako basic_distant_cas_close
with charachange

ha "¿Podemos entrar?"

hi "No veo por qué no; está abierta."

stop ambient fadeout 0.5
play sound sfx_storebell
play music music_soothing fadein 0.5

scene bg city_othello
with locationchange

"Hanako empuja la puerta y entra antes que yo. Una vez más, la tienda está vacía salvo por el dueño de la tienda."

show shopkeep neutral at center
with charaenter

"Su rostro cambia un poco cuando me ve."

sk "Oh, no estás aquí por una devolución, ¿o sí? Espera, esa no es la chica que traías contigo la última vez…"

hi "Em, no, no estamos aquí para devolver nada. Solo andábamos en la ciudad y queríamos echar otro vistazo aquí."

show shopkeep thinking
with charachange

"El dueño de la tienda considera esto por un largo rato. Supongo que no está acostumbrado a que los estudiantes de preparatoria vengan a su tienda de forma regular."

show shopkeep happy
with charachange

sk "¿Podría ser esta la amiga a quien le compraste los regalos?"

hi "Eso es. Eran regalos para ella."

show shopkeep happy at twoleft
show bg city_othello at bgleft
with charamove

show hanako defarms_strain_cas_close at tworight
with charaenter

"El dueño de la tienda gira hacia Hanako, quien se congela en su lugar como un venado atrapado en las luces."

show shopkeep surprised
with charachange

"Él se mueve para dirigirse a ella, pero se detiene antes de hacerlo, luciendo un poco desconcertado."

show shopkeep thinking
with charachange

"Él se da cuenta de que se ha quedado mirando y voltea a un lado, dirigiéndose a nosotros indirectamente. Su expresión es incómoda y tensa, lo mismo que el resto de su cuerpo."

"Quiero estar enfadado con él, pero sé perfectamente bien que tuve la misma reacción instintiva cuando la vi por primera vez. Primero sorpresa, luego curiosidad, luego una incómoda mirada a otro lado mientras lidiaba con lo que había visto."

show hanako emb_downsad_cas_close
with charachange

"Hanako parece menos temerosa que antes… pero pienso que el sentimiento que está emitiendo ahora es peor. No es ira, ni molestia. Si es algo, es de disculpa."

show shopkeep neutral
with charachange

sk "Es afortunada, joven señorita. De tener amigos que se preocupan por usted tanto como lo hacen."

show hanako emb_downtimid_cas_close
with charachange

ha "G-gracias…"

"Si no hubiera pasado tanto tiempo con Hanako no me habría dado cuenta siquiera de que había dicho algo. Por otro lado, también el murmullo del dueño de la tienda apenas fue claro, gracias en parte a no estar dirigido hacia nosotros."

hide hanako
with charaexit

show bg city_othello at left
show shopkeep invis:
    xpos 0.6 alpha 0.0
with dissolvecharamove

"Hanako arremete adentro de la tienda, mirando maravillada los variados artículos en exhibición. Ella encuentra la sección de muñecas, y pasa lentos minutos estudiando cada una de ellas."

"Es un lado de Hanako al que he sido presentado apenas. Estuve asombrado cuando Lilly me dijo que le gustaban las muñecas, y aún más de encontrar su “colección” descansando en el tocador."

show hanako basic_normal_cas_close at center
with charaenter

"Ella luce un poco mejor ahora que está distraída y sin el dueño de la tienda a la vista, pero aún estoy un poco desconcertado por toda la experiencia."

"Puedo tener mis propios problemas, pero nunca he tenido a extraños reaccionando a mí de esa forma, como si fuera algo completamente extraño a ellos."

show hanako basic_smile_cas_close
with charachange

ha "Esta es una tienda agradable."

hi "Sí, no es lo que esperaba. ¿Quieres comprar algo?"

show hanako cover_worry_cas_close
with charachange

ha "N-no traje nada de dinero."

hi "Bueno, siempre podemos venir otra vez."

"Ahora que sé dónde encontrarla, quiero decir."

show hanako cover_bashful_cas_close
with charachange

ha "¿P-podemos?"

hi "Desde luego. Podemos venir tan seguido como quieras."

show hanako basic_bashful_cas_close
with charachange

ha "G-gracias."

hi "No necesitas agradecerme; casi olvidé dónde estaba este lugar."

"Realmente no pienso que ninguno de los dos crea completamente en lo que estamos diciendo, más bien, estamos solo repitiendo lo que pensamos que deberíamos decir."

show hanako emb_smile_cas_close
with charachange

ha "¿P-podemos volver a la escuela ahora?"

hi "Seguro. Vamos."

stop music fadeout 5.0
play ambient sfx_traffic fadein 2.0

scene bg city_street3 at right
with locationchange

"Mientras nos vamos hacia la parada de autobús, veo al dueño de la tienda dando una ojeada a través de la cortina en la parte de atrás de la tienda."

"No estoy realmente seguro de lo que dice esa mirada que le lanza a ella. Se siente un poco extraño, y el hecho de que Hanako no lo vio es un alivio y un poco frustrante."

stop ambient fadeout 2.0

scene bg school_dormext_full
with shorttimeskip

"Hanako y yo nos detenemos una vez que alcanzamos el área de concreto entre los edificios de los dormitorios. Hubo escasamente unas palabras entre nosotros en el camino de regreso de la ciudad."

show hanako basic_bashful_cas at center
with charaenter

ha "Bueno entonces, nos vemos."

hi "¿Quieres tomar un poco de té o algo? ¿Qué tal un juego?"

show hanako emb_emb_cas
with charachange

"Hanako sacude su cabeza apenadamente."

ha "Estoy… cansada. ¿Tal vez después? Tengo tarea…"

"Suena un poco deprimida. Hanako obviamente quiere hacer más, pero supongo que debe tener un poco de trabajo de la escuela para ponerse al corriente; se ha perdido algunos días de clase."

hi "Ah, tarea. Gracias por recordarme; tengo un montón por hacer también. Supongo que te veré mañana."

show hanako basic_smile_cas
with charachange

ha "Nos vemos, Hisao."

hide hanako
with charaexit

"Antes de que pueda decir adiós, Hanako ha dado la vuelta y comenzado a caminar hacia la entrada del edificio de los dormitorios de las mujeres."

"Veo por un rato la puerta por la que desaparece, antes de partir hacia mi propio dormitorio."

"Hoy fue un día agotador."

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")



label es_H20_2:

scene bg school_gate at bgleft
show hanako def_worry_cas_close at center
with None

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")

hi "No sé tú, pero creo que trataré de tomar una siesta. Mi cabeza me está matando."

show hanako basic_distant_cas_close
with charachange

"Juzgando por el alivio instantáneo de Hanako, solo puedo asumir que supuse correctamente. No creo que quiera salir de paseo."

hide hanako
with charaexit

"Sin decir palabra, ella gira y se dirige de vuelta al portón de la escuela."

scene bg school_dormext_full
with locationskip

"Caminamos de vuelta a los dormitorios juntos, deteniéndonos embarazosamente en el punto en que necesitamos separarnos."

show hanako cover_distant_cas at center
with charaenter

ha "Bueno entonces, a-adiós."

hi "¿Quieres tomar un poco de té o algo? ¿Qué tal un juego?"

show hanako emb_timid_cas
with charachange

"Hanako sacude su cabeza apenadamente."

show hanako emb_downtimid_cas
with charachange

ha "Estoy… cansada. ¿Tal vez después? Tengo tarea…"

"Supongo que debe tener un poco de trabajo de la escuela para ponerse al corriente; se ha perdido algunos días de clase, después de todo."

hi "Ah, tarea. Gracias por recordarme; tengo un montón por hacer también. Supongo que te veré mañana."

show hanako emb_downsmile_cas
with charachange

ha "Nos vemos, Hisao."

hide hanako
with charaexit

"Antes de que pueda decir adiós, Hanako ha dado la vuelta y comenzado a caminar hacia la entrada del edificio de los dormitorios de las mujeres."

"Veo por un rato la puerta por la que desaparece, antes de partir hacia mi propio dormitorio."

"Mañana será un mejor día."

stop ambient fadeout 1.0
$ renpy.music.set_volume(1.0, 2.0, channel="ambient")

window hide

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
