label es_H2:

scene bg school_miyagi
show hanako emb_downsmile_close
with None

play sound sfx_doorknock2

show hanako emb_timid_close
with charachange

"Mientras estamos acomodando las piezas, se escucha un ruido en la puerta."

play sound sfx_dooropen

show bg school_miyagi at bgright
show hanako emb_timid_close at tworight
with charamove

show lilly basic_smileclosed at twoleft
with charaenter

li "Buenas tardes."

play music music_lilly fadein 4.0

show hanako emb_emb_close
with charachange

ha "Lilly…"

hi "Oh, qué tal Lilly. ¿Has acabado?"

show lilly basic_smile at twoleft
with charachange

li "¿Ambos están aquí? Maravilloso. De alguna forma, nuestra maestra se las arregló para reunir alguna ayuda extra, así que pude irme. ¿Han estado aquí desde que te fuiste?"

hi "Prácticamente. Hemos estado jugando un poco de ajedrez."

show hanako emb_smile_close
with charachange

ha "¿Gu-gustas una taza de té?"

show lilly basic_weaksmile at twoleft
with charachange

li "De hecho, creo que podría ser una buena idea ir afuera por un rato…"

show hanako def_worry_close
with charachange

"El instantáneo cambio de ánimo en el rostro de Hanako muestra su oposición a este plan, incluso si ella no dice nada."

"Me siento extrañamente obligado a decir lo que está plenamente a la vista en su rostro, pero que Lilly no puede ver."

hi "Creo… creo que tal vez deberíamos quedarnos aquí…"

show lilly basic_surprised at twoleft
with charachange

li "¿En verdad? Está tan concurrido aquí que estaba pensando que deberíamos dejar la escuela e ir a la casa de té local."

show hanako emb_blushtimid_close
with charachange

ha "¿Quieres decir el Sh-Shanghái?"

show lilly basic_smileclosed
with charachange

li "Desde luego; con todos en el festival debe de estar prácticamente vacío."

hi "¿Casa de té?"

show lilly basic_weaksmile
with charachange

li "Oh, es cierto, probablemente no sabes de él."

show lilly basic_smile
with charachange

li "Hay una casa de té no lejos de aquí, a la cual vamos de vez en cuando."

hi "Suena bien. Hanako, ¿tú qué piensas?"

show hanako defarms_shock_close
with Dissolve(0.2)

show hanako def_worry_close
with charachange

"Hanako salta un poco al ser forzada a entrar en la conversación, pero al menos luce menos consternada que antes."

show hanako cover_bashful_close
with charachange

ha "Si… si es el Shanghái, creo que será agradable."

show lilly basic_planned
with charachange

li "Bueno entonces, está acordado. Pongámonos en camino."

show hanako basic_bashful
with charadistant

"Hanako y yo nos levantamos de la mesa y nuestro juego de ajedrez."

"Antes de que pueda hacer nada, Hanako ha arrojado las piezas dentro de un pequeño contenedor y colocado el tablero a un lado."

hi "Parece que ahora estamos listos. Por favor, ustedes primero."

stop music fadeout 8.0

scene bg school_hallway3
with locationchange

show hanako emb_smile at Transform(xanchor=0.5, xpos=0.58)
show lilly basic_smileclosed at Transform(xanchor=0.5, xpos=0.42)
with charaenter

"Hanako se mueve al lado de Lilly y nos aventuramos hacia los corredores de la escuela."

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")

play ambient sfx_crowd_outdoors fadein 1.0

scene bg school_gate_ss
with locationskip

"El par me conduce a través de una serie de puertas desconocidas, y salimos por un lado del edificio opuesto a los terrenos del festival."

"Aislado por la pesada piedra del edificio, el ruido de la multitud se ha desvanecido a un murmullo."

hi "Extraño; pensé que la mayoría de la gente estaría comenzando a irse para este momento…"

show hanako emb_downtimid_ss at Transform(xanchor=0.5, xpos=0.58)
show lilly basic_smile_ss at Transform(xanchor=0.5, xpos=0.42)
with charaenter

li "Probablemente están aquí para ver los fuegos artificiales."

hi "¿Fuegos artificiales?"

show lilly basic_weaksmile_ss
with charachange

li "Sí, aparentemente la escuela prepara todo un espectáculo. Mucha gente viene del pueblo solo para verlos."

"La decisión de Lilly de dejar los terrenos escolares parece tomar sentido ahora. Hanako probablemente tendría dificultades con todo el pueblo descendiendo a la escuela. O ascendiendo, según sea el caso."

stop ambient fadeout 7.0
play music music_tranquil fadein 3.0

scene bg school_road_ss
with locationchange

"Por segunda ocasión desde que arribé a Yamaku me encuentro bajando a pie por esta carretera con Lilly."

"Solo ahora que puedo apenas escuchar el incesante ruido del festival me doy cuenta de lo ruidoso que era. Puedo escuchar mis oídos sonando ligeramente en el silencioso aire de la tarde mientras se recuperan del asalto que durante el día sufrieron."

show hanako emb_emb_ss at Transform(xanchor=0.5, xpos=0.58)
show lilly basic_smileclosed_ss at Transform(xanchor=0.5, xpos=0.42)
with charaenter

"Hanako se pega a Lilly, pero aun así se las arregla para guiarla a través de la carretera. Eso, y evitar las ocasionales miradas de los peatones curiosos, parece debilitar completamente su constitución."

"Raramente levanta su atención del piso frente a ella, y raramente pronuncia una palabra."

"Lilly, por otro lado, mantiene su personalidad formal y propia tal como lo hace en la escuela. Es obvio que intencionadamente pone esfuerzo en su apariencia, en lugar de esconderla de la forma que Hanako hace."

"Es sorprendente lo diferentes que son en la forma que se desenvuelven fuera de los terrenos de Yamaku. Dicho lo anterior, es obvio que en ambos casos cambian visiblemente."

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

window hide

nvl clear

$ renpy.music.set_volume(0.5, 1.0, channel="music")

nvl show dissolve

n "\n\n\nDentro de Yamaku, todo mundo es “especial”, lo que niega la “especialidad” de ello."

n "Pero una vez que nos aventuramos fuera de los portones escolares, somos devueltos al estatus de “forasteros” y de etiquetas genéricas."

n "Especialmente cuando aún estamos en uniforme escolar. Es como estar colgando una señal alrededor de tu cuello desafiando a la gente a descubrir lo que está mal contigo."

n "Estoy sorprendido de que tantos estudiantes se lo dejen puesto. Por otro lado, con bastones y sillas de ruedas siendo comunes entre los estudiantes, supongo que no es realmente una gran liberación."

n "\n¿O tal vez soy el único que ve esto como un estigma? Tal vez te acostumbras a ello después de un tiempo, como cualquier otro uniforme escolar."

nvl hide dissolve

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear

scene bg suburb_shanghaiext_ss
with locationskip

window show

"La casa de té luce bastante estándar desde afuera; solo un edificio ordinario con típicas señales decorando la entrada."

"Luce como el tipo de lugar por el que pasarías de largo sin pensarlo, solo otro café genérico en un mar de miles."

"Si Hanako no hubiese conducido a Lilly hacia la entrada yo habría continuado por la carretera sin siquiera saber que existía."

play sound sfx_storebell

scene bg suburb_shanghaiint at Fullpan(5.0, dir="right")
with locationchange

stop music fadeout 6.0

"Dentro de la casa de té se adquiere una sensación más tradicional. Todo parece haber sido hecho del mismo trozo de madera, del mostrador y los bancos a las mesas con sillones de respaldo alto en las paredes."

"Pero la cualidad más llamativa del cuarto es la falta de vida. Creo que puedo escuchar vagamente algo burbujeando a lo lejos al fondo, pero fuera de eso el cuarto está en silencio."

"Sin ninguna dirección, simplemente esperamos cerca de la entrada, obedeciendo educadamente la señal de “Por favor espere a que le asignen mesa”."

hi "Eh, ¿está cerrado este lugar o algo?"

stop music
play sound sfx_impact2

show yuukoshang panic_up:
    xalign 0.5 yanchor 1.0 ypos 1.5 alpha 0.0
    easein 0.3 ypos 1.0 alpha 1.0
show bg suburb_shanghaiint at right
with vpunch

"El sonido de una silla cayendo hace eco por todo el cuarto vacío, y una cabeza se levanta con rapidez de debajo de una mesa."

play music music_comedy fadein 0.5

show yuukoshang neurotic_up:
    ypos 1.0 alpha 1.0
with charachange

yu "¡No estaba dormida y bienvenidos al Shanghái!"

"Yuuko, vestida en delantal color pastel y sosteniendo un menú, se apresura a recibirnos. Sus anteojos desalineados y cabello despeinado arrojan sospechas sobre su declaración previa."

"Pero fuese que estaba dormida o no, no es la primera pregunta que viene a mi mente."

hi "¿Trabajas aquí ahora? ¿Qué le pasó a la biblioteca?"

show yuukoshang smile_down
with charachange

yu "¿Qué? ¿Lilly? ¿Hisao?"

show yuukoshang neurotic_up
with charachange

yu "¡Bienvenidos al Shanghái!"

show yuukoshang noglasses_up at Transform(ypos=1.25)
with Dissolvemove(0.2)

play sound sfx_dropglasses

with Pause(0.3)

show yuukoshang noglasses_up at center
with charamove

"Yuuko, todavía despertándose, lanza una violenta reverencia, haciendo caer sus anteojos en el proceso."

yu "¿¡Ghieh!? Mis anteojos…"

"Mientras recojo sus gafas del piso, Lilly ofrece una explicación."

show yuukoshang noglasses_up at tworight
show bg suburb_shanghaiint at center
with charamove

show lilly basic_weaksmile at twoleft
with charaenter

li "Yuuko trabaja aquí medio tiempo al igual que en la biblioteca. Es una de las razones por las que nos gusta venir aquí."

show yuukoshang neurotic_up
with charachange

"Yuuko toma sus anteojos de mis manos, poniéndoselos temblorosamente otra vez."

yu "Sí… eso es cierto… gracias…"

show yuukoshang neutral_down
with charachange

yu "¿Gustan que les muestre su mesa?"

show yuukoshang worried_up
with charachange

yu "No hay nadie más aquí, así que pueden escoger su mesa y ordenar lo que quieran, pero tardará un poco porque tendré que hacerlo yo misma…"

show lilly basic_smile at twoleft
with charaenter

li "Está bien, Yuuko. Estará bien con solo una tetera de té negro y un plato de emparedados."

show yuukoshang happy_down
with charachange

yu "¡Bien! ¡Pasaré de inmediato a ello!"

hide yuukoshang
with charaexit

show lilly basic_smile at center
show bg suburb_shanghaiint at bgright
with charamove

"Yuuko sale rápidamente hacia atrás del café, dejándonos aún de pie en la entrada."

"Ella empuja parcialmente las puertas de vaivén antes de darse cuenta de que no nos ha asignado mesa."

yu "¡Lo siento! ¡Lo siento! Por favor, ¡siéntense donde quieran! ¡Estaré de vuelta de inmediato!"

stop music fadeout 3.0

hide lilly
with charaexit

show bg suburb_shanghaiint at bgleft
with charamove

"Siguiendo su consejo, conduzco a Lilly a la mesa más cercana mientras Hanako nos sigue."

show lilly basic_smileclosed:
    twoleft
    ease 1.0 ypos 1.2
show hanako basic_normal:
    tworight
    ease 1.0 ypos 1.17
with Dissolve(1.0)

"Mientras me siento al lado de Lilly, me doy cuenta de lo apropiado que este lugar es para Hanako."

"Las mesas con sillones de respaldo alto te separan totalmente del resto del cuarto, y no parece recibir muchos clientes."

"Toda la mueblería, de los cojines en las mesas a los frascos para condimentos, luce antigua pero no demasiado desgastada."

"Me pregunto si Lilly selecciona deliberadamente lugares como este para llevar a Hanako. Ella luce como el tipo de persona que recorrería grandes distancias para atender el predicamento único de Hanako."

play music music_another fadein 4.0

show lilly basic_weaksmile:
    ypos 1.2
with charachange

li "Así que, Hisao, no sabía que jugaras ajedrez…"

hi "Bueno, no muy bien, pero sé cómo jugar."

show lilly basic_smile
with charachange

li "Supongo que ahora la pregunta obvia sería… ¿quién ganó?"

"La sonrisa inocente de Lilly me hace dudar. Realmente no quiero que parezca como que me estoy jactando de mi victoria sobre Hanako."

show hanako cover_bashful:
    ypos 1.17
with charachange

ha "Hi-Hisao ganó."

hi "Sí… pero, eh, no por mucho…"

"Maldición. Decir eso en voz alta me hace sentir como que he hecho algo terrible."

show lilly basic_giggle
with charachange

li "Bien hecho, Hisao. Has logrado algo en lo que yo solo he fallado."

hi "Eh, gracias. No he jugado en años, así que se sintió bien jugar otra vez."

show hanako basic_smile
with charachange

ha "S… sí… así fue."

"Hanako juguetea con su cabello un poco y mira a otro lado mientras responde, pero una pequeña sonrisa emerge."

"Es una reacción un poco más extrema de lo que esperaba, pero aún algo lindo en esa forma de Hanako."

show hanako defarms_shock at Transform(xpos=0.8)
show lilly basic_surprised at Transform(xpos=0.2)
with Dissolvemove(0.5)

show yuukoshang worried_up at center
with charaenter

"Me toma con la guardia un poco baja, y solo el reingreso cataclísmico de Yuuko me sacude de regreso a la conversación."

hi "¿Está todo bien por allá, Yuuko? ¿Necesitas una mano?"

show yuukoshang neurotic_up
show hanako def_worry
with charachange

yu "Estoy bien estoy bien estoy bien. Tengo que hacer esto apropiadamente, es mi trabajo."

show yuukoshang worried_up
with charachange

"La concentración aparece en su rostro mientras observa la bandeja en sus manos, como si simplemente el mirar a su contenido lo fuera a mantener en su posición."

show yuukoshang worried_up at centertremble
with charachange

"Tristemente, esto no se muestra del todo efectivo; las tazas y platillos bailan lentamente sobre ella, resonando ocasionalmente al chocar unos con otros."

show yuukoshang worried_up at Transform(ypos=1.1)
with ease

show yuukoshang worried_up at center
with ease

"Con gran cuidado, Yuuko coloca la bandeja en la mesa con apenas el más sutil de los choques."

show yuukoshang happy_down
with charachange

yu "Ahí está, ¡viste!"

hi "Eh, ¿bien hecho?"

show lilly basic_weaksmile
with charachange

li "Gracias, Yuuko."

show yuukoshang neutral_down at Transform(ypos=1.2)
with Dissolvemove(0.2)

with Pause(0.2)

show yuukoshang neutral_down at center
with ease

"La cabeza de Yuuko se dispara hacia abajo en su distintiva reverencia antes de contestar."

show yuukoshang closedhappy_down
with charachange

yu "No ha sido nada."

show lilly basic_smile
with charachange

li "¿Te gustaría unírtenos? Hay algo más que me gustaría discutir sobre esa reciente orden, si es que puedo…"

"Ah, es cierto. Lilly y Yuuko estaban discutiendo sobre una pila de libros cuando hablé con Hanako por primera vez."

"Algo sobre Lilly ayudando con el braille…"

show yuukoshang neurotic_up
with charachange

yu "Ah… sí. No tuvimos la oportunidad de repasarlos a todos, ¿verdad?"

show yuukoshang neurotic_up at Transform(ypos=1.17)
with charamove

"Yuuko se sienta apresuradamente junto a Hanako."

"Aparentemente su dedicación a este trabajo solamente llega hasta donde llega su concentración; una vez que se rompe, de repente la pierde."

show yuukoshang smile_down
with charachange

yu "Estaré en la biblioteca mañana en la tarde si gustas intentar otra vez…"

show lilly basic_cheerful
with charachange

li "Eso suena perfecto, te veré ahí después de clases."

show hanako emb_timid
with charachange

ha "Ah… L-Lilly…"

show lilly basic_oops
with charachange

li "Oh querida, es cierto. Mañana es lunes, ¿cómo pude haberlo olvidado?"

"Estoy empezando a sentirme un poco al margen de la conversación. Aunque es algo de esperar; he estado aquí por apenas una semana, así que es imposible saber los horarios de todos."

show lilly basic_weaksmile
with charachange

li "Bueno, a lo mejor podemos llegar a algún otro arreglo."

show lilly basic_smile
with charachange

li "Yuuko, ¿estarás en la biblioteca más adelante en la semana?"

show yuukoshang worried_up
with charachange

yu "Hmm, tal vez, pero esto ya está con retraso…"

show hanako emb_downsad
with charachange

ha "Y hay al-algunas… cosas que n-necesito…"

show lilly basic_listen
with charachange

li "Esto podría ser un problema…"

"Lilly reflexiona por un segundo antes de descubrir la respuesta."

show lilly basic_planned
with charachange

li "¿Me pregunto si podríamos conseguir la ayuda de alguien más, si se necesitara…?"

hi "Um, ¿Para hacer qué? Me perdí hace ya un rato…"

"Que se me haga voluntario para algo sin tener siquiera la más mínima idea de lo que está pasando en realidad no es lo mío."

"Y yo que pensé que finalmente había escapado de las ataduras del consejo estudiantil y sus repetidos intentos de reclutarme."

show lilly basic_smileclosed
with charachange

li "Oh, por supuesto. El otro día estaba ayudando a Yuuko a clasificar los nuevos libros de braille en la biblioteca."

show lilly basic_weaksmile
with charachange

li "Pero Hanako y yo usualmente vamos de compras los lunes por la tarde; está más tranquilo ese día que los fines de semana."

li "La semana pasada no pudimos ir porque estaba ocupada con el festival. Me las arreglé para escaparme después en la semana, pero Hanako no pudo hacerlo."

hi "Bueno, dado que no puedo leer braille, ¿asumo que te gustaría que fuera de compras con Hanako?"

show lilly basic_smile
show hanako emb_timid
with charachange

li "Correcto. Fuiste de gran ayuda para mí el otro día."

hi "Creo que puedo hacerlo. Hanako, ¿tú qué piensas?"

show hanako basic_smile
with charachange

ha "S-si no te molesta…"

hi "Claro que no. Todavía no estoy familiarizado con todas las tiendas en el área, así que suena como una buena idea."

show hanako basic_bashful
with charachange

ha "E-está bien."

show lilly basic_smileclosed
with charachange

li "Ahora que hemos acordado eso, ¿deberíamos tomar nuestro té?"

"Es ahora que me doy cuenta de que nuestro té ha estado esperando todo este tiempo, sin ponerse más caliente."

show yuukoshang panic_up
with charachange

yu "¡Es mi culpa! Déjame servirlo por ti…"

"Yuuko se extiende con manos temblorosas, pero la intercepto; no parece estar en buen estado para andar manejando líquidos calientes."

hi "Está bien, yo lo haré. Dado que tú ya hiciste el té y los emparedados, ya has cumplido con tu trabajo de mesera, ¿cierto?"

show yuukoshang neurotic_up
with charachange

yu "Yo… supongo."

"Yuuko se relaja un poco, pero aún observa ansiosamente mientras reparto la mezcla."

stop music fadeout 1.0
play ambient sfx_fireworks

show white
with Dissolve(0.1)

hide white
show fireshine
show hanako defarms_shock
show yuukoshang panic_up
show lilly basic_surprised
with charachange

"Cuando estoy a punto de morder el emparedado, un grave, y fuerte fragor puede ser escuchado, junto con un destello de luz desde afuera."

show lilly basic_weaksmile
show yuukoshang smile_down
show hanako emb_timid
with charachange

li "Ah, deduzco que el espectáculo ha comenzado."

hide fireshine
show bg misc_sky_ni as front
show fireworks
with locationchange

"Solo ahora que veo afuera, me doy cuenta de que el ocaso ha venido y se ha ido, dejándonos en la cumbre del crepúsculo."

"Estelas chispeantes se arquean al subir, listas para explotar en las florales siluetas de los fuegos artificiales."

hide fireworks
hide front
show fireshine
show yuukoshang happy_down
with locationchange

yu "¡Vamos a ver!"

show yuukoshang panic_up
with charachange

yu "Oh… perdón Lilly…"

show lilly basic_ara
with charachange

show hanako_fw behind bg:
    truecenter zoom 1.05 subpixel True
    ease 22.0 zoom 1.0
show ev hanako_shanghaiwindow behind hanako_fw:
    truecenter zoom 1.05 subpixel True
    ease 22.0 zoom 1.0
with None

li "Por favor, no se pierdan el espectáculo por consideración a mí. Por lo que he oído, este no es un mal lugar para verlo."

play music music_serene fadein 4.0

hide fireshine
hide bg
hide hanako
hide lilly
hide yuukoshang
with locationskip

"Con excepción de Lilly, nos apresuramos a la ventana de la pequeña casa de té para ver el espectáculo."

"Las luces estroboscópicas de colores juegan sobre los rostros sonrientes de Hanako y Yuuko, y por un segundo olvido mirar por la ventana."

"En este mundo totalmente nuevo, hay unas pocas cosas que no cambian."

"Creo que ese es el porqué la escuela hace tanto alboroto con esto del festival. Es una oportunidad de mostrar las similitudes entre todos."

stop ambient fadeout 3.0

hide hanako_fw
with Dissolve(1.0)

"El espectáculo se termina muy rápido; los fuegos artificiales son caros, incluso para las escuelas bien apadrinadas."

scene bg suburb_shanghaiint at bgright
with locationchange

"Antes de regresar a nuestro té y emparedados, Hanako gira hacia mí."

show hanako emb_downsmile_close
with charaenter

ha "Ah, g-gracias por lo de hoy."

show hanako emb_smile_close
with charachange

ha "… Y mañana."

hi "Está bien; no creo que yo hubiera podido enfrentar ese gentío tampoco."

hi "En días como este es más relajante pasar un tiempo alejado de todos, ¿no crees?"

show hanako basic_normal_close
with charachange

ha "S-sí."

hi "Como sea, ya hemos estado retrasando este té por demasiado tiempo, regresemos."

show hanako basic_bashful_close
with charachange

ha "S-seguro."

stop music fadeout 6.0

hide hanako
with charaexit

show bg suburb_shanghaiint at bgleft
with charamove

show lilly basic_smileclosed:
    yanchor 1.0 xanchor 0.5 ypos 1.2 xpos 0.2
show yuukoshang neutral_down:
    yanchor 1.0 xanchor 0.5 ypos 1.17 xpos 0.5
with locationchange

show hanako basic_smile:
    yanchor 1.0 xanchor 0.5 ypos 1.0 xpos 0.8
    easein 1.0 ypos 1.17
with charaenter

"Regresamos a la mesa y nuestra ligera comida."

show lilly basic_smile
with charachange

li "Eso sonó impresionante. Más grande que el último año."

show yuukoshang happy_down
with charachange

yu "Sí, ¡fue grandioso! No los había visto nunca preparar un espectáculo semejante."

yu "¡Se pone mejor cada año!"

show lilly basic_weaksmile
with charachange

li "Me temo, sin embargo, que durante ese tiempo, el té se ha enfriado."

show yuukoshang panic_up at center
with Dissolvemove(0.2)

play music music_ease fadein 0.5

yu "¡Oh no! ¡Déjenme hacer un poco más! ¡Esto es mi culpa!"

hi "Cálmate, Yuuko, no es culpa de nadie."

"Tomo un sorbo de mi taza, solo para probar mi punto."

hi "De todas maneras, este té no es tan malo frío. Es como un té helado."

show yuukoshang worried_up
with charachange

yu "¿En serio?"

hi "Sí, en serio. Si añades un poco de azúcar está bueno."

show yuukoshang neurotic_up
with charachange

yu "¿Estás seguro?"

hi "Lo digo en serio. Ahora ¿por qué no te sientas y terminamos esto juntos?"

show yuukoshang smile_down
with charachange

yu "E-está bien."

show yuukoshang smile_down at Transform(ypos=1.17)
with charamove

"Yuuko no parece convencida, pero se sienta de cualquier forma."

"Cuidadosamente mide unas cinco cucharaditas de azúcar y las añade a su té."

hi "Eh, dije un poco de azúcar…"

show yuukoshang neutral_down
with charachange

yu "Lo sé, pero me gusta mi té dulce de todas formas."

"Con curiosidad doy un vistazo dentro de su taza. Como esperaba, casi nada del azúcar se disuelve en el frío líquido."

"Ella la revuelve dos veces antes de levantarla y beber su contenido, con azúcar y todo, de un solo trago."

show yuukoshang happy_down
with charachange

yu "¡Tienes razón! ¡No sabe mal en absoluto!"

hi "Eh, bien…"

"Volteo a ver a Lilly y Hanako, quienes han terminado su comida mientras yo observaba la personalidad de Yuuko en acción."

"Sin deseos de retrasar a nadie, utilizo su táctica y termino lo que resta de mi té en un solo trago."

hi "Bien entonces, parece que todos hemos terminado."

show lilly basic_smile
with charachange

li "¿Debemos volver ahora o nos serviremos más?"

show yuukoshang neurotic_up
with charachange

"La expresión de Yuuko muestra claramente que esto no es una buena idea."

hi "Creo que sería mejor si volvemos ahora."

hi "Tenemos que regresar antes del toque de queda, después de todo."

show lilly basic_smileclosed
with charachange

li "Oh, ese es un buen punto."

show lilly basic_smile
with charachange

li "Te veré mañana, Yuuko."

show yuukoshang neutral_down
with charachange

yu "Estaré esperando por ello, Lilly. Hasta luego, todos."

stop music fadeout 9.0

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_cicadas fadein 0.5

scene bg suburb_shanghaiext_ni
with locationchange

"Hacemos nuestro camino hacia afuera de la pequeña casa de té y hacia la oscuridad de la noche."

$ renpy.music.set_volume(0.4, 1.0, channel="ambient")
scene bg suburb_roadcenter_ni
with locationchange

"Lilly y Hanako una vez más toman posiciones, pero bajo el cobijo de la oscuridad Hanako luce ligeramente menos estresada que cuando hizo el camino hacia aquí."

"Nos movemos contra el grupo ocasional de personas vaciando los terrenos escolares, pero Hanako parece guiarnos a lo largo de algunos pequeños senderos, evitando a la mayor parte de la multitud."

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene bg school_dormext_full_ni
with locationskip

"Fuera de los dormitorios, la escuela parece extrañamente tranquila al compararla con el ruido del día."

hi "Bueno, gracias a ambas por lo de hoy. Creo que aprendí mucho."

show hanako emb_timid_ni at Transform(xanchor=0.5, xpos=0.59)
show lilly basic_weaksmile_ni at Transform(xanchor=0.5, xpos=0.41)
with charaenter

li "No ha sido nada, pero me temo que en verdad debo irme. Hoy ha sido un largo día."

"Eso es cierto; Lilly pasó todo el día de hoy de pie, y puedo imaginar que caminar fuera de la escuela sería muy agotador para ella."

"Siento una punzada de culpa al recordar que fui probablemente el único en la escuela que se levantó alrededor de las diez el día de hoy."

hi "Desde luego."

hi "Bueno, las veré a ambas mañana. Buenas noches."

show lilly basic_cheerful_ni
with charachange

li "Buenas noches, Hisao."

show hanako basic_smile_ni
with charachange

ha "N-noches."

hide hanako
hide lilly
with charaexit

"Las chicas regresan a su dormitorio, y yo al mío."

"De hecho, ahora que lo considero, el día de hoy me ha fatigado también."

stop ambient fadeout 2.0

scene black
with dissolve



label es_H3:

window hide None

scene black
with dissolve

$ renpy.music.set_volume(0.0, 0.0, channel="ambient")
play sound sfx_alarmclock

with Pause(1.2)

play sound sfx_impact2

window show

"Mi alarma retumba en mis oídos, solo para ser silenciada velozmente por mi puño."

scene bg school_dormhisao
with openeye

"Mi cuerpo cambia a modo automático, llevando a mi inconsciente yo fuera de la cama y a ponerse el uniforme."

"Como siempre, mis frascos de píldoras esperan en mi escritorio pacientemente, aguardando a que las tome y elija mi dosis diaria de medicina; diecisiete píldoras al día."

scene bg school_scienceroom at bgright
with locationskip

"Antes de darme cuenta, estoy abriendo la puerta del grupo 3-3, feliz de ver que no soy el único que parece estar con un poco de resaca de la semana del festival."

"Cada uno de los rostros en el salón luce demacrado. Con el festival ya terminado, es como si el sueño de la vida de todos hubiera sido realizado."

"Sin nada más por lo que vivir, los estudiantes han confiado solo en sus instintos para guiarlos a clase."

"O tal vez simplemente estoy pensándolo demasiado."

"Lentamente tomo mi camino hacia mi asiento y solo entonces me doy cuenta del porqué el cuarto está tan tranquilo."

"Los asientos al lado mío están felizmente vacíos; la intérprete de sordos más escandalosa del mundo aún falta por llegar."

play sound sfx_doorslam
play music music_running

show misha hips_grin:
    yalign 1.0 xanchor 0.0 xpos 1.0
    easein 0.3 xanchor 1.0
with vpunch

"Justo cuando estoy por sentarme, la puerta se abre de golpe, revelando a una resplandeciente Misha; sus rizos balanceándose por la dramática entrada y sus brazos extendidos hacia el cielo."

show misha hips_laugh at right
with charachange

mi "¡Yu-juuu~! ¡Todo ha terminado!"

"Pareciera que no todos son afectados por la depresión postfestival."

"El resto de la clase la observa, obviamente pensando lo mismo que yo."

show misha sign_confused
with charachange

"Misha, aún inmóvil en la entrada con sus brazos todavía en el aire, observa nerviosamente alrededor."

"Es obvio que siente el terrible humor, pero no puede encontrar exactamente qué hacer."

show misha sign_confused at center
with ease_decel

"De repente, es arrojada bruscamente hacia adelante."

show misha perky_sad
with charachange

mi "¡Oye!"

show shizu invis behind misha:
    yalign 1.0 xanchor 0.5 xpos 1.0
with None

show misha perky_sad at twoleft
show bg school_scienceroom at center
show shizu adjust_happy at tworight
with dissolvecharamove

"Mientras tropieza dentro del salón, revela a Shizune, que tiene aún su brazo extendido por haber empujado a Misha."

show shizu basic_normal
with charachange

shi "…"

hi "Gracias por el entretenimiento, pero ¿no deberían las dos tomar sus asientos?"

show shizu behind_frown
with charachange

shi "…"

"Aún ligeramente apenada, le toma unos segundos a Misha darse cuenta de que tiene que traducir."

show misha sign_smile
with charachange

mi "¡Oh! ¡Cierto! Shicchan dice que no está muy contenta contigo por abandonarnos la semana pasada."

show misha cross_frown
with charachange

mi "¡Estábamos realmente ocupadas!"

hi "¿Ah, sí? ¿Qué hay de las cosas que ya había hecho por ustedes?"

show shizu cross_angry
with charachange

shi "…"

show misha hips_grin
with charachange

mi "Ella dice que eso solo cuenta para miembros del consejo. Dado que declinaste, ella no te debe nada."

show misha hips_grin_close
with characlose

"Misha se inclina acercándose más y susurra conspiratoriamente en mi oído."

mi "De hecho, creo que solo está un poco dolida de que no pasaste el día con ella."

show misha hips_smile_close
with charachange

mi "Pero está realmente agradecida por tu trabajo de la semana pasada."

show shizu behind_frustrated
with charachange

"Sintiendo que estamos hablando de ella, Shizune golpea ligeramente sus dedos en el banco hasta que Misha da la vuelta para verla."

show misha sign_smile
with charadistant

show shizu basic_angry
with charachange

show misha hips_grin
with charachange

show shizu adjust_blush
with charachange

"No puedo entender nada de las rápidas señas que están haciendo, pero por la expresión ligeramente apenada de Shizune, y la carcajada pobremente contenida de Misha, puedo suponerlo."

stop music fadeout 8.0

"Mientras este intercambio sucede, la puerta se abre una vez más, pero esta vez a un ritmo mucho más razonable."

show hanako invis at offscreenright
with None

show bg school_scienceroom at bgleft
show shizu basic_normal at Transform(xpos=0.42)
show misha hips_smile at Transform(xpos=0.18)
show hanako emb_downtimid at right
with dissolvecharamove

"Hanako entra silenciosamente al salón, y cierra la puerta tras ella."

show hanako emb_timid
with charachange

"Asomándose desde debajo de su cabello, rápidamente examina el salón de clases."

"Nuestros ojos se encuentran, y súbitamente se congela. Cierra sus ojos, respira hondo, y camina hacia mi banco."

show hanako cover_distant
with charachange

ha "Bu… buenos días Hisao."

hi "Buenos días Hanako. Llegas un poco tarde, ¿no?"

show hanako basic_normal
with charachange

ha "Yo… estaba hablando con Lilly."

show hanako basic_worry
with charachange

ha "S-sobre hoy."

hi "Ah, ¿entonces tienes su lista? Podemos irnos justo después de clases en ese caso."

show hanako emb_smile
with charachange

ha "C-claro."

hi "Estoy ansioso de ello."

"Hanako me muestra brevemente su apenada sonrisa y luego se apresura a su asiento."

scene bg school_scienceroom at bgright
with shorttimeskip

play music music_normal fadein 3.0

"Durante clases, se vuelve evidente que no son solo los estudiantes los que están un poco desanimados después del festival."

"Mutou simplemente nos da una lista de ejercicios del libro de texto y luego se sienta detrás de su escritorio."

"Por un momento olvido completamente el corto periodo de almuerzo, tal es la banalidad del día."

play sound sfx_normalbell

"Aturde los sentidos, y todos parecen sorprendidos cuando la campana señala el fin de las lecciones."

show shizu basic_normal at tworight
show misha perky_smile at twoleft
with charaenter

"Mientras estoy guardando mis cosas, Shizune y Misha me flanquean y atrapan."

show misha hips_grin
with charachange

mi "Y bien, Hicchan, aún no es demasiado tarde para unirse. Tenemos bastante papeleo postfestival por completar…"

hi "Eh, perdón Misha, yo… tengo planes…"

show hanako invis at offscreenright
with None

show bg school_scienceroom at center
show shizu basic_normal at Transform(xpos=0.42)
show misha hips_grin at Transform(xpos=0.18)
show hanako cover_distant at right
with dissolvecharamove

"Como detectando la indirecta, Hanako aparece detrás de mí, sosteniendo una pequeña bolsa, y tratando de evitar el contacto visual con el mundo exterior."

show misha cross_laugh
with charachange

"Misha abre los ojos de par en par, después rompe en carcajadas."

mi "¡GUAJAJA! Te mueves rápido, ¿no es así, Hicchan~? ¡No perturbaremos tu cita por más tiempo! ¡Guajajaja!"

show shizu behind_blank
with charachange

"Tras la vociferante Misha, veo a Shizune tomándole muy poco interés a la escena. Podría estar malinterpretándolo, pero creo que está ignorándome deliberadamente."

show hanako emb_downtimid_close
with characlose

"Siento un gentil jalón en mi playera, y volteo para ver los ojos de Hanako fijos firmemente en el piso."

show hanako emb_timid_close
with charachange

ha "Va… vamos…"

hi "Entiendo. Shizune, Misha, las veré después."

hi "Y aún no estoy interesado en el consejo."

show misha cross_grin
with charachange

mi "Aguafiestas."

stop music fadeout 2.0

hide misha
hide shizu
with charaexit

show bg school_scienceroom at bgleft
show hanako emb_timid_close at center
with charamove

"Misha y Shizune se retiran al pasillo, haciéndose señas felizmente entre ellas."

hi "¿Tienes todas tus cosas? Marchémonos."

play music music_soothing fadein 4.0

scene bg school_gate
with locationskip

"Ríos de estudiantes salen por los portones de la escuela y hacia la carretera al pueblo."

"Es un poco extraño. Es casi una escena de cualquier otra escuela, pero la ilusión se desvanece por la ocasional silla de ruedas o miembro faltante."

"Una cosa que noto es que nadie está solo."

scene bg school_road
with locationchange

show hanako emb_downsad_close at center
with charaenter

"Y, mientras Hanako y yo pasamos a través del portón, noto que ella acorta la distancia entre nosotros."

"No lo suficiente para ser considerado “cerca”, pero claramente no está en su usual posición “solo un poco lejos”."

"Supongo que no somos lo suficientemente familiares como para que ella se acerque tanto como lo hace con Lilly."

"Sin embargo, incluso aunque se ha movido un poco más cerca a mí físicamente, mentalmente parece haber viajado un kilómetro."

"Sus manos asidas fuertemente a las correas de cuero de su mochila al punto de blanquear sus nudillos, su cabeza gacha y su boca contraída fuertemente."

"Casi luce como si se le estuviera llevando a la oficina del director por primera vez."

"Trato de ahogar una risa por la idea, pero en vano."

show hanako emb_timid_close
with charachange

ha "¿Q-qué ocurre…?"

"Supongo que no tiene caso esconderlo…"

hi "Perdón. Por un segundo se vio como si estuvieras en problemas."

show hanako defarms_strain_close
with charachange

ha "¿Q-q-qué quieres decir?"

hi "Creo que necesitas relajarte un poco. No vamos a ir muy lejos, y solo hay estudiantes por aquí, ¿cierto?"

show hanako def_worry_close
with charachange

ha "Ci-cierto."

"Me molesta un poco ver a Hanako tan alterada."

hi "Y haces esto cada semana, ¿o no?"

show hanako basic_worry_close
with charachange

ha "S-sí. Con Lilly."

"Por supuesto. “Con Lilly”. Me pregunto si alguna vez ha dejado la escuela sin ella."

"No parece ser mucha a primera vista, pero la dependencia de Hanako en Lilly es absurdamente grande."

"Si ni siquiera puede manejar el salir de la escuela sin ella, ¿cómo se las habría podido arreglar para sobrevivir si no se hubieran conocido?"

"¿Habría encontrado alguien más a quién aferrarse? ¿Y qué es lo que la llevó a Lilly?"

"¿Fue por su ceguera, o tan solo fue Lilly lo suficientemente gentil como para darle una mano?"

"Me pregunto si cualquiera hubiera cubierto los requisitos."

hi "Bueno, yo estoy aquí. Además, no vamos a ir tan lejos. Habrá terminado antes de que te des cuenta."

show hanako emb_downsmile_close
with charachange

"Los nudillos de Hanako lentamente recobran su color mientras trata de esconder una pequeña sonrisa, pero ese esfuerzo parece evitar continuar la conversación."

"Viajamos, lado a lado, por el sinuoso camino de bajada hacia el pueblo. La multitud de estudiantes se dispersa mientras continuamos a través de la acera."

"Los estudiantes más rápidos se adelantan, y los de menor movilidad se quedan atrás, diseminándose la multitud a nada."

scene bg suburb_konbiniext
with locationskip

"Para cuando llegamos al minisúper estamos prácticamente solos."

scene bg suburb_konbiniint
with locationchange

"Usándome como escudo entre ella y el encargado, Hanako se mueve entre los estrechos pasillos, añadiendo una diversidad de artículos a su canasta."

"Pan, leche, té… ¿tomillo?"

"¿Qué clase de minisúper vende hierbas?"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

nvl clear

nvl show dissolve

n "\n\nPor otro lado, nada sobre este pueblo parece normal, lo cual podría no ser algo tan malo en retrospectiva."

n "Todo es tan diferente e incómodo; detenerse a pensar en tales cosas no es realmente una opción."

n "Cuando pienso en ello, me recuerda a Hanako."

n "No importa lo mucho que intentes, no puedes evitar sus cicatrices; aún interrumpen mi hilo de ideas cuando las veo."

n "Por mucho que trato de no admitirlo dentro mío, creo que estoy forzándome a ignorarlas."

n "No es que yo mismo esté libre de cicatrices. La irregular línea en mi esternón nunca se desvanecerá por completo."

n "Tan solo tengo el lujo de poder esconderla fácilmente."

n "\nPero, en cierta forma, nuestras cicatrices me recuerdan que todos estamos en este lugar por una razón."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

window show

"…"

"Hanako arroja un último artículo en su canasta y luego tímidamente la extiende hacia mí, junto con unos pocos billetes."

show hanako emb_downtimid_close at center
with charaenter

ha "P-p-podrías p-por favor…"

"Me toma un segundo entender lo que está tratando de decir."

hi "Oh, ¿quieres que yo pague por esto?"

show hanako emb_downsad_close
with charachange

"Ella asiente con la cabeza, pero no levanta la mirada."

"Supongo que esta tarea recae en Lilly en las situaciones normales."

hi "Seguro. Solo déjame agarrar un par de cosas…"

"Apresuradamente agarro unos pocos artículos esenciales para mí y luego me dirijo al mostrador con Hanako siguiéndome de cerca."

"El encargado asiente indiferentemente mientras escanea los artículos."

"Supongo que solo ignorarnos es una forma de lidiar con las anomalías de Yamaku; deben de recibir a muchos estudiantes aquí, siendo la tienda más cercana a la escuela."

"Cada miembro del personal debe de tener su propia forma de lidiar con nosotros. O tal vez no; tal vez soy el único que piensa dos veces sobre mis excepcionales compañeros de la escuela."

stop music fadeout 2.0

scene bg suburb_konbiniext_ss
with locationchange

"Completada nuestra transacción, Hanako y yo partimos de regreso a la calle."

scene bg school_road_ss
with locationskip

play music music_tranquil fadein 10.0

"La carretera está prácticamente abandonada para estos momentos. Los estudiantes que iban saliendo ya se han ido, y ninguno ha comenzado su retorno aún."

"Y, con solo la escuela por delante en la carretera, no parece haber nadie más por aquí."

show hanako def_worry_close_ss at center
with charaenter

"Ciertamente el vacío se refleja en Hanako; sus brazos a los lados llevando cada uno una bolsa, su cabeza ya no inclinada, y de vuelta a una posición vertical…"

"Es casi como si estuviera disfrutando esta caminata."

hi "Entonces, ¿por qué todas estas cosas extrañas? ¿Especias mezcladas? ¿Por qué necesitarías eso en la escuela?"

show hanako basic_normal_close_ss
with charachange

ha "Algunas… veces… m-me gusta hacer co-comida."

hi "Bueno, desde luego, a mí también, pero… ¿especias?"

hi "Eso es un poco más avanzado, ¿no lo crees?"

show hanako emb_blushing_close_ss
with charachange

ha "N-no realmente."

hi "Bueno, creo que está bien. Tendrás que enseñarme algún día."

show hanako emb_smile_close_ss
with charachange

ha "S-seguro."

"No parece muy segura de eso, pero remarcarlo no parece muy inteligente."

"Al menos, parece mucho más feliz de lo que estaba durante el camino de ida por esta carretera."

"Ese simple hecho me hace un poco feliz."

scene bg school_dormext_full_ss
with shorttimeskip

show hanako basic_normal_close_ss at center
with charaenter

"Afuera de los dormitorios de las chicas, Hanako y yo organizamos las bolsas de comestibles con nuestras respectivas compras."

"En comparación, mis cosas parecen ciertamente planas."

hi "Lo digo en serio, me estás poniendo en ridículo aquí…"

show hanako defarms_shock_close_ss
with charachange

ha "N-no yo no… yo solo…"

hi "Solo bromeo."

show hanako def_worry_close_ss
with charachange

hi "Tengo una pila de tarea que dejé pasar la semana pasada, así que debo irme ahora."

hi "¿Estarás bien llevando todo eso a tu cuarto?"

show hanako cover_bashful_close_ss
with charachange

ha "S-sí."

hi "¿Segura? Bien entonces. Te veré mañana."

show hanako basic_smile_close_ss
with charachange

ha "A-adiós."

hide hanako
with charaexit

stop music fadeout 7.0

"Nos separamos, y yo regreso a mi cuarto."

scene bg school_dormhisao_ss
with locationskip

"Pilas de papeles descansan sobre mi escritorio, suplicando ser terminadas. Con todo el alboroto de la semana pasada, apenas he tenido tiempo para ponerme al día."

"Traté de continuar con mis estudios mientras estuve en el hospital, pero algunas de estas cosas no las he visto antes, incluso allá en mi anterior escuela."

"Sin estar de ninguna forma preparado, retiro la tapa de una lata de bebida, y me pongo a trabajar."

scene black
with dissolve



label es_H4:

scene black
with None

play music music_daily fadein 6.0

scene bg school_dormhisao
with locationchange

"Los días comienzan a ser realmente calurosos."

"Esta mañana, me desperté cubierto en sudor."

"Para cuando el cuerpo estudiantil comienza a dejar sus dormitorios para el desayuno y tareas matutinas, el sol ha tomado un efecto completo; extrañamente, eso me levanta los ánimos."

"No son ni siquiera las ocho, y aun así siento que este día va a ser uno de esos placenteros, tranquilos, y cálidos."

"Si no estuviera en una escuela que considera cada ausencia a clases como señal de una situación de riesgo mortal, consideraría saltarme el día completo y solo relajarme en los jardines de la escuela."

"Sí, hoy será un día genuinamente relajado."

"Por un segundo, me detengo a medio estirar, y considero la advertencia del enfermero sobre ejercitarme. Tal vez debí continuar con esas carreras matutinas."

"Correr con alguien como Emi podría haber sido un poco demandante, pero si hubiera ido a mi propio ritmo…"

"Ah, ¿a quién engaño? No podría apegarme a algo como eso sin algún tipo de motivación."

"No es como si estuviera por ahí sentado todo el día. La caminata de ida y vuelta al minisúper cuenta como ejercicio, ¿cierto? Especialmente la caminata por la colina cuesta arriba…"

"Claro, no es la gran cosa. Comparado con los meses yaciendo en una cama de hospital estoy haciendo bastante ejercicio."

scene bg school_scienceroom
with shorttimeskip

"Parece que no estoy solo en mi apreciación del día."

"Casi todos los miembros de la clase están observando a través de la ventana y hacia el incitante cielo."

"Incluso a la inmutable Shizune parece faltarle su usual vigor para los trabajos escolares."

"Misha, tan descarada como nunca, se ha desabotonado los primeros botones de su playera y está abanicándose con su cuaderno."

"Debo haberme quedado viendo, pues ahora está sacando su lengua hacia mí."

"Aun así, no muestra señales de detener sus esfuerzos, ni está tratando de esconder el hecho."

play sound sfx_normalbell

"La campana del almuerzo parece tomar a todos por sorpresa, y la clase se vacía a un ritmo mucho más lento del usual."

"El calor parece estar absorbiendo la necesidad de apresurarse de todos."

stop music fadeout 8.0

"Bueno, casi todos."

show hanako emb_emb
with charaenter

ha "¿Hi… Hisao?"

hi "Qué tal Hanako, ¿qué puedo hacer hoy por ti?"

"Hanako tiene ya una bolsa de almuerzo en sus manos."

"No tengo que ser detective para saber hacia dónde va esto."

show hanako emb_smile
with charaenter

ha "Um… ¿gustas almorzar con nosotras otra vez?"

show hanako basic_bashful
with charaenter

ha "Yo… traje suficiente para todos…"

hi "Maravilloso. Pero no tienes que ser tan ceremoniosa con esto."

show hanako basic_normal
with charaenter

ha "Ah… está bien."

hi "¿Supongo que vamos al cuarto de té?"

show hanako cover_worry
with charaenter

ha "P… por favor."

show hanako basic_normal
with charaenter

ha "Lilly dijo que nos vería ahí, así que debemos… debemos…"

hi "¿Debemos?"

show hanako emb_smile at center
with charaenter

ha "… Debemos irnos juntos…"

hi "Suena como una buena idea. Este calor me ha dado mucha hambre."

"Hanako da un suspiro de alivio, y yo junto mis cosas."

scene bg school_miyagi
with locationskip

play music music_happiness fadein 1.0

"Como siempre, el aura del cuarto de té es refrescante, sintiéndose aislado del resto del mundo."

"Por otro lado, el usual alboroto de la escuela parece un poco apagado; más que nada por la pereza producida debido al agotamiento por calor."

"Hanako lentamente dispersa su comida en la mesa, enfocándose atentamente en cada pequeño movimiento, como tratando de mantener su mente lejos de otros pensamientos."

"No es mucho, pero puedo decir por su comportamiento que ha preparado todo con sumo cuidado."

hi "Supongo que Lilly aún no está aquí. ¿Deberíamos empezar sin ella?"

show hanako emb_timid:
    center
    ypos 1.17
with charaenter

ha "E-estará aquí pronto…"

show hanako emb_downtimid
with charachange

"Hanako lucha con la tapa del contenedor del arroz."

hi "A ver, déjame ayudarte con eso…"

"Tomo el contenedor de las manos de Hanako, y trato de forzar la tapa a que se abra."

"A pesar de mis esfuerzos, parece atascada."

hi "Déjame adivinar, ¿la pusiste mientras el arroz aún estaba caliente?"

show hanako emb_sad
with charachange

ha "S-sí. Tenía mucha prisa…"

"Coloco el contenedor en la mesa entre nosotros."

hi "Eso pensé. Parece que esto está atascado. Necesitaremos un poco de agua caliente para abrirlo."

hi "Pero eso podría ser un problema aquí. Terminaríamos con agua en todos lados."

li "Bueno, en ese caso, ¿qué tal si contribuyo a la comida de hoy?"

show lilly invis at left
with None

show hanako emb_smile:
    tworight
    ypos 1.17
show bg school_miyagi at bgright
show lilly basic_cheerful at twoleft
with dissolvecharamove

"En la puerta, Lilly sonríe mientras sostiene una bolsa surtida con varios bollos y rollos de pan. No puedo sino hacer lo mismo."

show lilly basic_smileclosed
with charachange

li "Dado que ambos tuvieron que hacer cambio de planes debido a mí, pensé en traer un pequeño detalle."

hi "Gracias, Lilly. A ver, déjame sostener eso por ti…"

show lilly basic_smileclosed at Transform(ypos=1.2)
with charamove

"Con un poco de orientación, el surtido de panes de Lilly se une al plato sin arroz de Hanako. Rápidamente hago un poco de té para completar la imagen."

hi "Bueno, ya deseo comenzar."

show hanako emb_downtimid
with charachange

"Mientras doy una mordida, noto a Hanako haciendo su mayor esfuerzo por parecer como si no estuviera mirando hacia mí."

"No es nada especial, aunque a decir verdad no puedo quejarme. Soy muy desidioso cuando se trata de cocinar para mí."

hi "No está mal, ¿supongo que esto está hecho con las cosas que compraste ayer?"

show hanako emb_blushtimid
with charachange

ha "S-sí."

"Los ojos de Hanako me gritan, rogando por algún tipo de retroalimentación."

hi "Bueno, claramente valió la pena. Gracias, Hanako."

show hanako cover_bashful
with charachange

ha "Yo… quería mostrarte esto… después de lo de ayer…"

hi "Está bien. Solo estaba un poco sorprendido con las cosas que estabas comprando."

show lilly basic_weaksmile
with charachange

li "Hanako ha gustado siempre de experimentar cuando se trata de comida. Creo que es buena… la mayoría… de las veces."

"Mientras por un lado la sonrisa de Lilly no tiembla, el ligero cambio en su tono me dice que las cosas no han ido muy bien en el pasado."

"Y no es como si Hanako tuviera mucha gente para probar su cocina…"

stop music fadeout 7.0

"Un momento… ¿estaba Lilly esperando a que yo fuera primero? Ella no empezó a comer hasta después de que dije que todo estaba bien…"

"Su descarada sonrisa me dice que esta fue una acción deliberada. Tendré que tratar de idear cómo devolvérsela en el futuro, para pagar por esto."

hi "Bueno, está rica, y es todo lo que cuenta, ¿cierto?"

show hanako basic_smile
with charachange

ha "Ci-cierto."

show lilly basic_smileclosed
with charachange

"Lilly, satisfecha de no ser la primera en servir de prueba a la creación de Hanako, comienza a consumir la comida frente a ella."

"Me encuentro ensimismado mientras veo sus palillos tocar gentilmente el plato, sus puntas picando y trazando para rápidamente determinar la posición de la comida mientras diestramente la recoge."

"Uno podría pensar que es una niña jugando con su comida si no fuera por la situación, pero lo hace con tanto cuidado y ligereza que es obvio que simplemente este es el modo en el que come este tipo de alimentos."

"No queriendo perdérmelo, comienzo a comer también."

show hanako emb_downsmile
with charachange

"Hanako toma una actitud diferente, esperando hasta que Lilly y yo tengamos las manos libres antes de tomar su parte rápidamente."

show hanako emb_smile
with shorttimeskip

play music music_dreamy fadein 4.0

"En poco tiempo los contenedores están limpios, salvo por el aún cerrado contenedor de arroz."

show lilly basic_smile
with charachange

li "Gracias Hanako, estoy satisfecha."

show hanako basic_smile
with charachange

ha "N-no… gracias a ti por el pan…"

hi "Sí, habría sido un desastre de no ser por eso."

show lilly basic_planned
with charachange

li "No ha sido nada."

show lilly basic_weaksmile
with charachange

li "Pero ahora, tengo que regresar. Es bastante fácil llegar tarde después de comer aquí."

hi "Sí, veo a lo que te refieres. Creo que nosotros limpiaremos aquí y luego partiremos."

show lilly basic_smileclosed at twoleft
with dissolvecharamove

li "Bueno entonces, buen día."

hide lilly
with charaexit

show hanako basic_smile:
    center
    ypos 1.17
show bg school_miyagi at center
with charamove

"Lilly se va, su bastón golpeando el piso a través del tranquilo pasillo."

"Hanako y yo rápidamente empacamos nuestras cosas y permanecemos sentados, esperando la campana."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene bg misc_sky at Fullpan(20.0)
with locationchange

"Juntos, observamos hacia afuera de la ventana y hacia el azul cielo sin fin."

play sound sfx_warningbell

"Si no fuera por el repique de las campanas, hubiera jurado que el tiempo se había detenido."

"El impulso de saltarme la clase se levanta en mis entrañas."

"Lanzo una mirada a Hanako quien no muestra tampoco señales de moverse."

ha "No… aún no…"

$ renpy.music.set_volume(1.0, 3.0, channel="music")

scene bg school_miyagi
show hanako basic_smile:
    center
    ypos 1.17
with shorttimeskipsilent

"El intervalo entre las campanas de aviso y el final del almuerzo pasa en un abrir y cerrar de ojos."

hi "En verdad tenemos que irnos… la gente se espantará y comenzará una búsqueda de rescate si nos saltamos…"

show hanako basic_distant
with charachange

"Hanako suspira."

show hanako basic_normal
with charachange

ha "Tienes razón."

show hanako basic_normal at center
with charamove

"Lentamente, se pone de pie, y yo la imito."

scene bg school_staircase2
with locationskip

"Silenciosamente, tomamos nuestro camino por las escaleras hacia arriba al tercer piso y después a nuestro salón."

scene bg school_hallway3
with locationchange

play sound sfx_dooropen

"En la entrada, tomo la iniciativa y abro la puerta por delante de Hanako, inclinando mi cabeza a modo de disculpa por adelantado."

scene bg school_scienceroom at center
with locationchange

stop music fadeout 5.0

hi "Lo lamento, llegamos tarde maestro."

play sound sfx_doorclose

"Soy recibido no por palabras severas, ni por una enfadada instrucción de tomar mi asiento, sino simplemente por el silencio creado por los más o menos quince estudiantes tratando de no reír."

"Mutou, siempre lento, aún falta por llegar. De todas maneras, el hecho de que Hanako y yo hemos llegado juntos es visiblemente obvio."

show misha hips_grin at center
with charaenter

mi "Pff… pffua…"

"Eso lo vuelve unos catorce estudiantes tratando, y un estudiante fallando."

play music music_comedy

show misha cross_laugh
with charachange

mi "¡Pft-guajajaja! ¡Los amantes vuelven~!"

show misha hips_laugh
with charachange

mi "¡GUAJAJAJA~!"

hi "Sí, gracias. Ahora puedes tranquilizarte."

hide misha
show hanako invis_close:
    center
    xpos 1.0
with charaexit

show bg school_scienceroom at bgleft
show hanako emb_downsad_close:
    xpos 0.8
with dissolvecharamove

"Paso a través de la puerta, y me doy cuenta de que Hanako está firmemente presionada contra mi espalda, escondiendo su persona del resto de la clase."

show hanako invis_close:
    xpos 0.7
with dissolvecharamove

"Conforme mis pasos se acercan a mi banco, ella eventualmente se aparta de mí y camina rígidamente al suyo. El esfuerzo por bloquear mentalmente la presencia de todos está claramente escrito en su rostro."

scene bg school_scienceroom at bgright
with charamove

"Rápidamente revisando la puerta por cualquier señal de arribo del maestro, hago un viaje al banco de Hanako y susurro en su oído."

hi "No te preocupes por Misha, ella siempre es así. Disfruté del día de hoy. No te preocupes, ¿está bien?"

"Hanako asiente con la cabeza tras sus brazos plegados, pero aún no muestra su rostro."

play sound sfx_dooropen

show muto invis at tworight
with None

show muto normal at center
show bg school_scienceroom at center
with dissolvecharamove

"Deseo quedarme y consolarla un poco más, pero Mutou elige este preciso momento para entrar al salón, a mitad de su explicación, como si hubiera empezado en el pasillo."

show muto smile at center
with charaenter

mu "… lo que, por supuesto, es directamente proporcional a la carga pero inversamente proporcional al cuadrado de la distancia…"

hide muto
with charaexit

play sound sfx_doorclose

"Está tan absorto en su discurso que ni siquiera me nota deslizándome de vuelta a mi asiento desde el banco de Hanako."

"Mientras la arenga de Mutou divaga, Misha se inclina hacia mí."

show misha invis at offscreenleft
with None

show misha perky_smile_close:
    xanchor 0.5 xpos 0.16
with dissolvecharamove

mi "El maestro podrá no haber notado tu tardanza, pero yo sí."

"Eso es bastante obvio por el espectáculo que montaste."

show misha hips_grin_close
with charachange

mi "He recibido instrucciones de dejar que te salgas con la tuya por hoy, pero solo con una condición."

hi "¿Oh? ¿Y cuál sería?"

show misha sign_smile_close
with charachange

mi "¡Tienes que ayudarnos esta tarde~!"

"Estiro mi cuello para ver sobre el hombro de Misha."

"Shizune está convenientemente evitando el contacto visual conmigo."

hi "Bien. Solo por hoy."

hi "Ya les he dicho que no me uniré al consejo, ¿recuerdas?"

show misha hips_grin_close
with charachange

mi "¡Desde luego! Hacer eso sería considerado… um, considerado…"

show misha perky_confused_close
with charachange

"Ella voltea a su cuaderno, obviamente buscando su posición en el guión."

show misha hips_grin_close
with charachange

mi "… Bajo presión y por tanto iría contra el reglamento."

hi "Qué extraño en ti ser ahora considerada sobre el reglamento."

show misha sign_smile_close
with charachange

mi "¡Las cosas deben hacerse conforme al libro!"

show misha perky_smile_close
with charachange

mi "Es solo que el libro no ha sido escrito para todas las situaciones, así que hay veces en que puede ser ignorado."

hi "Y aun así, ambas se preguntan por qué nadie quiere estar en el consejo estudiantil…"

stop music fadeout 3.0

show misha hips_frown_close
with charachange

with Pause(0.3)

show misha invis at offscreenleft
with dissolvecharamove

hide misha
with None

"Después de sacar su lengua hacia mí, Misha regresa a su cuaderno, y ambos luchamos por superar los desafíos a través de la segunda mitad del día escolar."

with shorttimeskip

play sound sfx_normalbell

show shizu invis_close at offscreenright
show misha invis_close at offscreenleft
with None

show misha hips_smile_close at twoleft
show shizu behind_blank_close at tworight
with Dissolvemove(0.5, time_warp=_ease_in_time_warp)

"Antes de siquiera poder levantarme, Misha y Shizune han puesto sus manos en mis hombros."

hi "Oigan, dije que ayudaría, rayos…"

play music music_shizune fadein 1.0

show misha hips_grin_close
with charachange

mi "Esto es solo un seguro, Hisao, ¡seguro~!"

show hanako invis behind shizu at offscreenright
with None

show misha hips_smile_close at Transform(xpos=0.17)
show shizu behind_blank_close at Transform(xpos=0.5)
show bg school_scienceroom at bgleft
show hanako emb_timid:
    xanchor 0.5 xpos 0.9
with dissolvecharamove

ha "¿Hi-Hisao?"

"Hanako tímidamente trata de dejar el salón rodeándonos y repentinamente me doy cuenta de que esta podría ser mi única oportunidad de escapar."

hi "Oh, oye Hanako. ¿Qué pasa?"

show shizu basic_angry_close
with charachange

shi "…"

show misha hips_frown_close
with charachange

mi "Oye, ¿qué te hace pensar que tienes tiempo de platicar?"

hi "Oh relájense, esto no tomará mucho… perdón Hanako, ¿decías?"

show hanako emb_downtimid
with charachange

ha "Yo… iba a la biblioteca, y… y pensé…"

"Los pulgares de Hanako danzan entre ellos y sus ojos revolotean por todo el lugar, mirando a todos lados menos a nosotros."

show misha sign_smile_close
with charachange

mi "Lo lamento Hanako, pero Hisao tiene que venir con nosotras. Tiene trabajo que hacer."

show shizu behind_smile_close
with charachange

shi "…"

show misha hips_grin_close
with charachange

mi "¡Oh! Pero puedes ayudar también si lo deseas."

show hanako cover_worry
with charachange

ha "Em…"

label es_choiceH4:
menu:
    with menueffect
    mi "Entonces, ¿qué dices, Hisao?"
    "¿Tú qué dices, Hanako?":


        return m1
    "Ya he hecho suficiente trabajo para el consejo.":

        return m2


label es_H5_1:


scene bg school_scienceroom at bgleft
show hanako cover_worry:
    xanchor 0.5 xpos 0.9
show shizu behind_smile_close at Transform(xanchor=0.5, xpos=0.5)
show misha hips_grin_close at Transform(xanchor=0.5, xpos=0.17)
with None

hi "¿Qué dices, Hanako? Si todos ayudamos no deberíamos tardar mucho en realidad."

show hanako emb_timid
with charachange

"La agitación de Hanako contesta mi pregunta antes de que ella pueda siquiera formar las palabras."

show hanako emb_downtimid
with charachange

ha "Yo… en verdad tengo que irme…"

"Bueno, eso era de esperarse. Parece ser que somos solo yo y las chicas del consejo otra vez."

"Es más fácil resignarme a otra tarde de trabajo en la pequeña oficina del consejo."

hi "Te alcanzo después, ¿está bien?"

show hanako emb_smile
with charachange

ha "E-está bien."

stop music fadeout 3.0

show misha hips_grin_close at twoleft
show shizu behind_smile_close at tworight
show hanako invis at offscreenright
show bg school_scienceroom at center
with dissolvecharamove

show misha hips_smile_close at twoleft
hide hanako
with charachange

mi "¡Bien! Ahora que las despedidas han terminado, ¡es tiempo de trabajar!"

scene bg school_hallway3
with locationchange

"Misha y Shizune me meten por la fuerza a la oficina del consejo estudiantil, sin soltar mis hombros ni un momento."

"Me siento un poco mal por dejar plantada a Hanako así, pero si este es el precio por quitarle de encima a Misha, que así sea."

scene bg school_council
with locationchange

hi "Y entonces, ¿en qué estamos metidos hoy?"

show misha sign_smile at center
with charaenter

play music music_ease fadein 8.0

mi "¡Informar!"

hi "¿Eh? ¿No se supone que eso se hace después de que sucedió algo?"

show misha hips_grin
with charachange

mi "¡Sip! Debemos cotejar toda la información del festival para que Shicchan pueda dar el informe a los maestros."

show misha hips_grin at twoleft
show bg school_council at bgleft
with charamove

show shizu adjust_happy at tworight
with charaenter

"Shizune deja caer una gran pila de papeleo en el escritorio frente a mí, y sonríe con precisión."

show misha hips_smile
with charachange

mi "Necesitas dividir esos en dos pilas."

show misha sign_smile
with charachange

mi "Una para cosas financieras, como recibos."

mi "Una para retroalimentación, una para retroalimentación positiva, tal vez una para cosas que parezcan como que podrían ser un problema el próximo año, una para problemas que probablemente no podrán ser resueltos…"

hi "Esas son un poco más de dos pilas…"

show misha perky_confused
with charachange

mi "¿Eh? Oh, cierto. Sí, pensé que serían solo dos pilas. Mi error."

hi "Bien. Mientras estoy haciendo esto, ¿qué estarán haciendo ustedes dos?"

show misha hips_grin
show shizu adjust_smug
with charachange

mi "Bueno, perdimos el desayuno porque estábamos recolectando todos estos reportes, ¡así que iremos por algo de comer!"

"Y por qué no los organizaron mientras los estaban recolectando…"

"Por suerte mi mecanismo de autodefensa me golpea y evita que abra la boca y que pueda empeorar más la situación."

show misha perky_confused
with charachange

mi "¡¿Eh?!"

show misha perky_sad
with charachange

mi "¿Cómo es eso justo?"

show shizu behind_blank
with charachange

shi "…"

"Me estaba enojando tanto por la injusta distribución del trabajo que no noté que Shizune había continuado haciendo señas."

"Si no fuera por el arrebato de Misha, probablemente no lo habría notado para nada."

show shizu adjust_smug
with charachange

show shizu basic_normal
with charachange

show shizu behind_blank
with charachange

"Shizune parece estar dando una cadena ciertamente larga de órdenes a Misha, y ninguna de ellas parece agradable."

show misha sign_sad
with charachange

show misha perky_sad
with charachange

show misha perky_sad at Transform(ypos=1.15)
with charamove

"Llegando a una conclusión, Misha devuelve rápidamente unas señas a Shizune, y después se sienta en el escritorio a mi lado."

show shizu adjust_happy
with charachange

hide shizu
with charaexit

show misha perky_sad at Transform(xpos=0.5)
show bg school_council at center
with charamove

"Shizune agita la mano hacia nosotros antes de desaparecer por la puerta."

hi "¿Qué fue todo eso?"

show misha perky_confused
with charachange

mi "Shicchan estaba preocupada de que lo hicieras todo mal a menos que fueras supervisado."

show misha perky_sad
with charachange

mi "Y dado que ella no puede decirte cómo estás arruinando las cosas, me ha hecho quedarme. Oooooh… qué desastre, ¡yo quería ir con Shicchan!"

show misha cross_smile
with charachange

mi "¡Pero nos traerá algo de comida~!"

show misha cross_grin
with charachange

mi "¡Eso es muy bueno!"

"La frivolidad de Misha está fuera de este mundo. Del ánimo por los suelos a la cima del mundo por unas calorías."

"Es difícil imaginar cómo alguien podría operar a ese nivel."

hi "Bueno, podría haber sido peor."

hi "¿Entonces qué se supone que haremos?"

show misha sign_smile
with charachange

mi "Cotejar."

hi "Eso lo entendí."

show misha hips_smile
with charachange

mi "Bueno, empecemos por hacer pilas. Ya resolveremos después lo que cada pila significa."

hi "Bien…"

show misha perky_smile
with charachange

"Empezamos a separar todos los papeles en pilas incrementalmente complejas."

"Al inicio son solo simples categorías; financieras, retroalimentación, reportes de incidentes…"

"Después se dividen en buenos y malos reportes, y aún más, hasta que empieza a parecer como si solo hubiéramos tirado los papeles en el escritorio."

hi "Esto es inútil."

show misha perky_confused
with charachange

mi "¿Eh? ¿Por qué? Estamos haciendo lo que se nos dijo, ¿cierto?"

hi "Sí, pero parece como si solo estuviéramos haciendo un desastre."

show misha hips_grin
with charachange

mi "No, creo que ya tenemos hecho bastante. Shicchan podrá resolver lo demás a partir de aquí."

show misha cross_grin
with charachange

mi "Así que creo que entonces podemos detenernos aquí."

"Es casi como si el sentido común de Misha hubiera dejado el cuarto con Shizune."

"Aun así, no tiene caso discutir."

show misha sign_smile
with charachange

mi "De todas formas…"

show misha cross_smile
with charachange

mi "¿Qué hay entre tú y Hanako?"

hi "¿Qué hay?"

show misha hips_smile
with charachange

mi "Estabas pasando el rato con ella hoy, ¿o no~?"

show misha hips_grin
with charachange

mi "¿Ha habido alguna chispa? ¿Algún chisme que me estés ocultando~?"

hi "Si te hablo de mis propias circunstancias, no sería un chisme, ¿o sí?"

show misha perky_confused
with charachange

mi "Supongo que no…"

hi "Solo somos amigos, supongo."

hi "¿Por qué estás tan interesada? Pensé que a Shizune y a ti no les agradaba…"

show misha cross_frown
with charachange

mi "No es eso en realidad. Ya sabes que Shicchan y Lilly no se llevan bien."

mi "Y dado que en realidad no puedes alejar a Hanako de Lilly, no hablamos mucho con ella."

show misha sign_smile
with charachange

mi "Pero eso no significa que no pueda preocuparme por ella."

hi "¿Y hay algo de qué preocuparse?"

show misha perky_sad
with charachange

mi "Bueno, ella nunca pasa el rato con nadie más, ¿cierto? ¡No es bueno, Hicchan!"

"Si Shizune y Lilly no se llevan bien porque “sus personalidades son diferentes” entonces odio pensar cómo se llevarían Misha y Hanako…"

show misha perky_confused
with charachange

mi "Quiero decir, de una forma u otra, aquí todos estamos en el mismo bote, ¿cierto~?"

hi "Bueno, supongo."

show misha sign_smile
with charachange

mi "Esta vez, cuando se fue en mitad de la clase, Shicchan fue con el maestro y preguntó qué es lo que se iba a hacer al respecto."

show misha sign_confused
with charachange

mi "Él dijo que cada estudiante aquí tiene necesidades especiales, y que Shicchan no debería preocuparse por ello."

show misha perky_confused
with charachange

mi "Hanako nunca hace ningún trabajo grupal; ella simplemente sale corriendo."

mi "¿No es eso suficiente para preocuparse?"

hi "Supongo que tienes razón. Ella todavía dice con trabajo algunas palabras cuando hablamos."

show misha perky_sad
with charachange

mi "Bueno, eso es más de lo que he logrado hacer. Shicchan y yo tratamos cuando ella empezó, pero se asustó y corrió."

"Considero decirle a Misha que exactamente lo mismo sucedió conmigo, pero parece atrapada en sus pensamientos."

"Escuchar a Misha sin la influencia de Shizune es… interesante."

show misha cross_frown
with charachange

mi "Creo que necesita darse cuenta de que a la gente aquí no le importa cómo se ve, y que puede confiar en nosotros."

show misha cross_smile
with charachange

mi "Si lo hiciera, me sentiría mucho mejor por ella."

"Creo que este es el tiempo más largo que he visto a Misha sin hacer señas."

"Cuando está con Shizune, está constantemente agitando sus manos por todos lados, explicando el mundo a Shizune."

"Esa cantidad de esfuerzo probablemente pone bajo presión incluso a una mente ágil."

"Y enfrentémoslo; Misha no es la mente más brillante del mundo."

hi "Bueno, la vigilaré por ti."

hi "Pero probablemente deberías disculparte por lo de antes. No creo que Hanako esté hecha para ese tipo de bromas."

show misha perky_confused
with charachange

mi "¿Oh? ¡Oh~!"

show misha perky_sad
with charachange

mi "No me di cuenta. Perdón."

hi "No me lo digas a mí, solo menciónaselo a ella."

show misha perky_smile
with charachange

mi "Está bien. Será lo primero mañana, hablaré con ella."

hi "Bien."

play sound sfx_doorslam
with vpunch

"Una cacofonía de la puerta anuncia el regreso de Shizune."

"Supongo que no puede en realidad saber cuánto ruido está haciendo."

show misha hips_grin
with charachange

mi "¡Oh, Shicchan! ¡Estás de vuelta!"

show shizu invis at Transform(xanchor=0.5, xpos=1.0)
with None

show misha hips_grin at Transform(xpos=0.3)
show shizu behind_blank at tworight
show bg school_council at bgleft
with dissolvecharamove

"Shizune aparece, completamente cargada con bienes del minisúper."

show shizu basic_normal2
with charachange

shi "…"

show misha sign_smile
with charachange

mi "Hubo algún excedente del festival. Dado que este es oficialmente un asunto del festival, he derrochado un poco."

show misha hips_grin
with charachange

mi "Buena idea Shicchan, diez puntos."

hi "¿Realmente está eso permitido?"

show shizu cross_angry
with charachange

shi "…"

show misha cross_frown
with charachange

mi "Para alguien que se rehúsa a unírsenos, pareces tomar un interés no saludable en las políticas de este consejo."

show misha cross_grin
show shizu adjust_smug at tworight
with charachange

mi "Debo castigar tu insolencia racionando tu porción del festín."

hi "Bien, bien, entiendo."

show misha perky_smile
show shizu adjust_happy at Transform(ypos=1.15)
with dissolvecharamove

"Misha desliza las múltiples pilas de papeles a un lado para hacer campo para la avalancha de comida que Shizune está extendiendo."

"Mientras observo mi duro pero errado trabajo desperdiciarse, me doy cuenta de que no es sorprendente que estas dos necesiten ayuda."

"La comida del minisúper no es muy buena, pero al menos es llenadora."

show shizu behind_smile
with charachange

shi "…"

show misha sign_smile
with charachange

mi "Gracias por ayudar hoy. La mayoría de las veces solo completamos los reportes para el personal."

show misha perky_smile
with charachange

mi "Este año podremos al menos completar algunos apartados relevantes en el informe."

hi "¿Están seguras de que esta no es una organización corrupta?"

show misha hips_grin
with charachange

mi "Para nada, para nada. Vamos conforme al libro. No es nuestra culpa si el libro no es lo suficientemente específico."

hi "Pensé que esa era la definición de corrupción…"

show misha hips_smile
with charachange

mi "¡Piensas demasiado~!"

hi "¿Saben qué? Probablemente tengan razón."

hi "De cualquier modo, tengo que irme…"

hi "… Eso es, si tengo permiso para retirarme."

show shizu adjust_smug
with charachange

shi "…"

show misha hips_grin
with charachange

mi "Tu trabajo ha sido considerado suficiente. Puedes irte."

hi "Bien, gracias."

hi "Sabes, si remarcaras el lado de “comida gratis” sobre el de “carga de trabajo sin fin”, probablemente terminarías con más reclutas."

stop music fadeout 6.0

show misha sign_smile
with charachange

show shizu behind_blank
with charachange

mi "Tal vez sea un buen punto."

hi "Bueno, piénsalo."

hi "Y piensa sobre lo que hablamos… no tienes que decirle a Shizune si no quieres."

show misha perky_confused
with charachange

mi "¿Qué? Oh, cierto. Trataré de verla mañana."

show misha perky_smile
with charachange

mi "Buenas noches, Hicchan."

hi "Buenas noches Misha, Shizune."

scene black
with dissolve


label es_H5_2:

scene bg school_scienceroom at bgleft
show hanako cover_worry:
    xanchor 0.5 xpos 0.9
show shizu behind_smile_close at Transform(xanchor=0.5, xpos=0.5)
show misha hips_grin_close at Transform(xanchor=0.5, xpos=0.17)
with None

hi "Oye, Shizune. Sé que dije que ayudaría, pero olvidé que ya había hecho planes. Además, la semana pasada ayudé con más de lo que me tocaba, ¿o no?"

hi "Prometo que se los compensaré en alguna otra ocasión."

show misha sign_confused_close
with charachange

show shizu basic_frown_close
with charachange

show misha perky_smile_close
with charachange

show shizu behind_blank_close
with charachange

"Shizune y Misha me liberan y tienen una larga, intensa, y silenciosa conversación."

show misha sign_smile_close
with charachange

mi "Bueno, ese es un buen punto. Para ser honesta, solo íbamos a gastar el resto del presupuesto en pasteles."

show misha cross_laugh_close
with charachange

mi "Así que, si no estás ahí, será mejor. Más pastel para nosotras. ¡Guajajaja~!"

stop music fadeout 6.0

show shizu invis at offscreenleft
with dissolvecharamove

show misha invis at offscreenleft
with dissolvecharamove

hide shizu
hide misha
with None

"Shizune da un giro de 180 grados y camina hacia la puerta, y Misha sale saltando tras ella."

hi "Bueno, eso fue mucho más fácil de lo que pensé que iba a ser. La semana pasada esas dos fueron como sabuesos. O guardias de prisión."

hi "O tal vez guardias de prisión engendrados por sabuesos…"

"No puedo creer lo que acabo de pensar, por no mencionar que lo dije en voz alta. Creo que necesito alejarme de Kenji."

hi "… No importa. Como sea, ¿nos vamos a la biblioteca?"

show hanako basic_smile
with charachange

ha "S-seguro."

play ambient sfx_crowd_indoors fadein 0.5

scene bg school_hallway3
show crowd
with locationchange

"Hanako me sigue a través de los aún concurridos pasillos a la biblioteca, usándome como escudo."

stop ambient fadeout 0.5
play music music_happiness fadein 2.0

scene bg school_library
show hanako invis at offscreenright
show yuuko neutral_down at center
with locationchange

show hanako basic_worry at tworight
with dissolvecharamove

"Tan pronto como hemos atravesado la puerta, Hanako huye hacia el mostrador, donde Yuuko está apilando libros."

show hanako emb_emb
with charachange

"Antes de poder alcanzarla, Hanako le ha susurrado algo."

show yuuko neurotic_up
with charachange

yu "Um, lo encontrarás en la sección de no ficción, pero no sé dónde exactamente. Si gustas puedo buscarlo…"

show hanako emb_downsad
with charachange

ha "N-no importa."

hi "Oye Yuuko, ¿de qué se trata todo esto?"

show yuuko neutral_down
with charachange

yu "Oh, Hisao… Hanako solo estaba buscando un libro sobre…"

show hanako emb_blushing
with charachange

ha "N-nada…"

hi "¿Un libro sobre nada? ¿En la sección de no ficción?"

show hanako def_strain
with charachange

ha "Yo… solo estaba…"

show yuuko neurotic_up
with charachange

"Lanzo una mirada a Yuuko. Parece como si estuviera por explotar por la presión de mantener en secreto la petición de Hanako."

hi "Yuuko, ¿qué…?"

show yuuko happy_down
with charachange

yu "¡Ajedrez! ¡Está buscando un libro de ajedrez!"

"Hago una nota mental de nunca confiar a Yuuko ninguna información importante."

show hanako defarms_shock
with charachange

ha "Y-Yuuko…"

show yuuko panic_up
with charachange

yu "Lo siento Hanako… solo se me salió…"

hi "Bueno, ha dejado de ser un secreto. Vamos, te echaré una mano. En verdad necesito pulir mis habilidades también."

show hanako def_worry
with charachange

ha "E… está bien."

hide yuuko
with charaexit

show hanako def_worry at center
show bg school_library at bgleft
with charamove

"Yuuko desaparece tras el mostrador avergonzada mientras Hanako y yo partimos hacia las profundidades de la sección de no ficción."

"Sé que se supone que hay un sistema para categorizar estos libros, pero no veo cómo podría alguien descifrarlo sin perder la mitad de su vida investigándolo."

"Probablemente esa es la razón por la que todas las bibliotecarias que conozco son neuróticas."



"Cerca del final del pasillo, entre un libro de trucos mágicos y un libro de juegos para niños, aparece un solo libro titulado “Tácticas de Ajedrez para Campeones”."

show hanako basic_bashful
with charachange

"Antes de que yo pueda estirar la mano, Hanako tiene el libro en sus manos, apresándolo contra su pecho."

hi "Bueno, supongo que es tuyo entonces. ¿No te molestaría si lo tomo prestado cuando lo termines?"

show hanako cover_worry
with charachange

ha "S-seguro. Solo no… no he jugado en realidad contra nadie más que L-Lilly antes, así que pensé…"

"Maldición. No es como si estuviera tratando de vencer a Hanako deliberadamente ni nada, pero parece haberlo tomado muy a pecho."

"Aunque claro, al menos esto significa que quiere jugar conmigo otra vez. Eso es bueno, ¿cierto?"

hi "Ja, bueno no es como si fuera un maestro ni nada; solo jugué un poco antes…"

"Súbitamente me doy cuenta de que no le he dicho a Hanako sobre mi condición. Vacilo por un segundo, decidiendo cubrir mis pasos. Esa es una conversación para otro día."

hi "… Antes de venir aquí."

stop music fadeout 6.0

show hanako cover_distant
with charachange



ha "¿Estás… estás bien?"

hi "Sí, solo estaba recordando algo…"

"Cuando pienso sobre ello, no debería tener miedo de hablarle a Hanako de mi condición y el tiempo en el hospital. Juzgando por sus cicatrices, ella probablemente pasó una buena cantidad de tiempo en una cama de hospital."

"Pero, por alguna razón, no puedo decirlo. Al menos no hoy, y sin antelación."

"Ansioso por interrumpir la conversación, tomo un libro del estante."



"Es un libro sobre las montañas rusas más veloces del mundo…"

"… Publicado en 1982. Bueno, no muy actualizado, pero debe ser por lo menos interesante."

hi "Bueno, ahora ambos conseguimos un libro, ¿deberíamos sentarnos?"

show hanako cover_bashful
with charachange

"Hanako parece aceptar mi treta, y nos dirigimos al rincón de lectura al fondo de la biblioteca."

hide hanako
with charaexit

"Ninguno de nosotros dice una palabra; simplemente abrimos nuestros libros y comenzamos a leer."

"Trato de leer mi libro, pero parece ser que en 1982 las montañas rusas no eran ni por asomo tan largas como las construidas en las décadas siguientes."

"La mayoría de las listadas están hechas de madera. Algo sobre ello no me parece muy seguro."

"Si voy a montarme en algo potencialmente peligroso, quiero que esté hecho de acero, o algún tipo de aleación de la era espacial que diga en letras grandes algo como “Titanio” y “Rutenio”."

"Rápidamente pierdo el interés, y mis ojos divagan por el área de lectura y descansan en Hanako."

show ev hana_library_read_std:
    truecenter zoom 1.0 subpixel True
    easein 20.0 zoom 1.05
with locationskip

"Hanako parece absorta en su libro, hojeando hacia adelante y atrás apresuradamente, como confirmando lo que acaba de leer."

"Me pregunto si de hecho eso es efectivo, o si solamente está sobrecargándose."

"Inconscientemente ella retira su cabello de su rostro, revelando temporalmente su piel cicatrizada."

"Aún no estoy seguro del protocolo aquí. ¿Es correcto preguntarle sobre sus cicatrices? ¿O su pasado? ¿Cuánto tiempo estuvo en el hospital? ¿Aún visita al doctor?"

"Todas estas parecen las preguntas que le harías a alguien que se acaba de transferir a tu escuela, traducidas al lenguaje local."

"Pero, a la fecha, nadie me ha preguntado directamente ninguna de ellas. Bueno, excepto Rin, pero no creo que deba usarla como guía para comportamiento social correcto."

"Por el momento, solo mantendré mi boca cerrada. Si alguien quiere que sepas algo, entonces te lo dirá. Tratar de forzar el tema podría llevar a Hanako a cerrarse otra vez."

scene bg school_library_ss
show yuuko worried_up_ss at center
with shorttimeskip

yu "Um… perdón por interrumpir, pero ya tengo que cerrar la biblioteca."

play music music_tranquil fadein 3.0

hi "¿Tan pronto?"

"Reviso mi reloj. De alguna forma, mientras me perdía en mis pensamientos, casi dos horas han pasado."

show yuuko smile_down_ss
with charachange

yu "¿Quieren registrar esos libros para llevar? Puedo hacerlo en la salida…"

show hanako invis:
    xpos 0.9 xanchor 0.5 ypos 1.17 yanchor 1.0
with None

show hanako basic_worry_ss:
    xpos 0.7
show bg school_library_ss at bgleft
show yuuko smile_down_ss at twoleft
with dissolvecharamove

ha "P-por favor."

hi "Ya he terminado. Dejaré este libro en el camino. No era tan interesante como pensé en un inicio."

show hanako emb_timid_ss at tworight
with dissolvecharamove

"Hanako marca su posición con un pedazo de papel y se levanta. Las chicas se dirigen al mostrador y yo regreso mi libro a lo que creo que es el estante correcto."

show yuuko neurotic_up_ss
with charachange

"Yuuko escanea el libro de Hanako con presición practicada, aun así se las arregla para fallar."

show yuuko neutral_down_ss
with charachange

yu "Oh… ahí tienes. La tercera es la vencida. Dado que este es un libro de no ficción, solo puedes tenerlo por una semana."

show hanako basic_smile_ss
with charachange

ha "E-está bien."

scene bg school_hallway2
with locationchange

"Yuuko apaga la computadora de la biblioteca y nos conduce hacia la puerta."

show yuuko panic_up at twoleft
show hanako def_worry at tworight
with charaenter

yu "¡Argh! ¡No pensé que ya fuera tan tarde…!"

hi "Pero tú fuiste la que nos dijo que ya tenía que cerrar…"

show yuuko worried_up
with charachange

yu "Sí pero, lo sé pero, ¡eso fue antes de que viera la hora!"

show yuuko neurotic_up
with charachange

yu "Los veré después."

hide yuuko
with easeoutleft

"Yuuko se apresura por el pasillo, su bolso de mano arrastrándose tras ella como una ridícula serpentina."

show hanako def_worry at center
show bg school_hallway2 at bgleft
with dissolvecharamove

hi "Supongo que todas las bibliotecarias son en verdad neuróticas."

show hanako emb_timid
with charachange

ha "¿Eh?"

hi "Ah, no importa. solo estaba pensando que nunca he conocido a una bibliotecaria que pudiera organizar su tiempo, sin importar lo buenas que fueran con sus libros."

show hanako basic_smile
with charachange

ha "Oh… sé a lo que te refieres…"

"Hanako sonríe divertida. No lo dije en forma de broma, pero debí haberle recordado a alguna otra bibliotecaria… o algo…"

show hanako cover_worry
with charachange

ha "Tengo… tengo que regresar."

hi "Sí, yo también. No me di cuenta de que era así de tarde. Gracias por dejarme pasar el rato contigo."

show hanako basic_bashful
with charachange

ha "N-no hay problema."

hi "Como sea, ahora voy camino a mi dormitorio, entonces ¿te importa si me voy contigo?"

show hanako emb_blushing
with charachange

ha "E-está bien."

hide hanako
with charaexit

"Hanako sale delante de mí, y necesito trotar un poco para alcanzar su lado."

scene bg school_dormext_full_ss
with locationchange

show hanako def_worry_ss at center
with charaenter

"Caminamos a través de los jardines, llegando eventualmente frente a los edificios de los dormitorios."

hi "Vaya, caminas bastante rápido. Solía jugar en un club de futbol, y te las arreglas para dejarme atrás."

stop music fadeout 6.0

show hanako emb_downsmile_ss at center
with charaenter

"En cierta forma me arrepiento de decir eso. Tiene menos que ver con su paso que con el hecho de que mi estado ha empeorado significativamente mi condición."

"La reacción de Hanako es extraña. Esperaba un torpe intento por reducir su velocidad al caminar, pero solo se ruboriza mientras mira sus pies y sonríe."

"El silencio flota en el aire entre nosotros. Eso sucede frecuentemente con Hanako, pero se siente ligeramente diferente de lo usual esta vez. Después de unos segundos, trato de romper el silencio."

hi "Aquí estamos. ¿Te veo en clase mañana?"

show hanako emb_smile_ss
with charachange

ha "S-seguro."

hide hanako
with charaexit

"Hanako agita su mano en una corta despedida antes de atravesar las puertas de los dormitorios. Me quedo de pie y las observo por un rato, antes de tomar mi camino hacia mi propio dormitorio."

scene black
with dissolve



label es_H6:

scene bg school_dormhisao
with locationchange

"Pájaros chirriando."

"Normalmente este sería un buen momento para reflexionar sobre la belleza de la naturaleza."

"Pero son las 6 a. m."

play sound sfx_pillow

scene black
with Dissolve(0.2)

"Cubriendo mi cabeza con la almohada, azoto mi cara contra el colchón, esperando que el impacto me mande instantáneamente de vuelta a dormir."

"Inútil."

"Me sacudo y doy la vuelta, pero el sueño simplemente no vuelve a mí."

play music music_daily fadein 10.0

scene bg school_dormhisao
with locationchange

"Está bien naturaleza, tú ganas. ¿Ves? Ya me estoy levantando…"

"La falta de sueño pesa sobre mi cabeza, y solo hay un remedio para esto; un buen y abundante desayuno."

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 0.5

scene bg school_cafeteria
with locationchange

"Sería bueno ser la primera persona aquí."

"Ser el primero en meter la cuchara en una pila caliente de comida, sentarme donde desee…"

"Hubiera sido bueno."

"Pero incluso mi excepcionalmente matinal comienzo me ha puesto por detrás de los estudiantes más diligentes."

"Supongo que hay unas pocas personas que tienen comienzos tempraneros aquí, por una razón u otra."

"Un grupo de estudiantes en ropa deportiva se amontona en una mesa, discutiendo ávidamente planes de juego al mismo tiempo que tragan grandes bocados de comida."

"Esparcido por el pasillo se encuentra un número de estudiantes con ojos somnolientos, probablemente sufriendo de mi mismo mal —pájaros ruidosos."

"Y, por supuesto, están las personas que de hecho disfrutan levantarse a esta hora, los que llevan sus mochilas rellenas con libros de texto y tareas completadas."

"Es difícil no despreciar a gente como esa, y aún más cuando uno mismo está cansado."

"Descubro un rostro familiar entre la pequeña multitud, me dirijo hacia la mesa más cercana."

"Lilly se sienta solitaria, sintiendo delicadamente su camino a través de un pequeño plato de huevos con su tenedor."

"Es casi una pena interrumpirla a ella y sus acompasados movimientos."

"Me pregunto si es así como una persona ciega se desconecta. Desplazándose simplemente en movimientos predeterminados aprendidos a través de los años, tal como una persona con vista comería mientras lee un periódico."

hi "Buenos días, Lilly. No esperaba que estuvieras aquí tan temprano."

show lilly basic_surprised:
    center
    ypos 1.2
with charaenter

li "Oh, Hisao, me asustaste. No sabía que desayunabas tan temprano."

hi "No lo hago. Esta es una excepción a la regla. Preferiría por mucho andar tarde para la escuela que temprano para el desayuno."

show lilly basic_weaksmile
with charachange

"Lilly da un pequeño suspiro a mi admitida tardanza mientras comienzo a comer mi desayuno."

"No le toma demasiado para volver a su previo mordisqueo mecánico."

"Cada pequeño movimiento carece de energía. Supongo que esto es similar a dejar a tus ojos vagar mientras realizas algún quehacer cualquiera."

"Pero después de algunas repeticiones del ciclo encontrar comida/comer comida, Lilly coloca en la mesa su tenedor y toca sus labios con una servilleta."

stop music fadeout 6.0
stop ambient fadeout 6.0

show lilly basic_concerned
with charachange

li "Hisao, ¿te importa si te hago una pregunta?"

"Maldición. Todo lo que quiero es un poco de comida y unas cuatro horas de sueño. Y nadie dice “puedo hacerte una pregunta” por una pregunta simple."

hi "Seguro."

show lilly basic_listen
with charachange

li "¿Piensas en Hanako como una amiga?"

"Eh, esta parece una pregunta capciosa."

hi "Yo… creo. ¿Por qué lo preguntas?"

show lilly basic_weaksmile
with charachange

li "Por nada."

show lilly basic_displeased
with charachange

play music music_serene fadein 8.0

li "Pero sí tengo otra pregunta. ¿Por qué es que piensas en ella como una amiga?"

"Esto está por encima de mi nivel. ¿Qué es lo que espera de mí?"

hi "No estoy seguro en realidad. Supongo que es porque ella es un poco diferente en la manera en la que trata con la gente…"

show lilly basic_reminisce
with charachange

li "Hmm. Desde que la conozco, no se ha conectado en realidad con nadie."

show lilly basic_concerned
with charachange

li "No parece interesada en otras personas, y creo que las personas se asustan un poco con su apariencia."

hi "¿En verdad? Pensé que ese tipo de cosas eran, bueno, frenadas aquí. Discriminación y eso."

show lilly basic_listen
with charachange

li "Hmm, si tuviera que ponerlo de algún modo…"

"Ella frunce las cejas pensando, un movimiento que me pone un poco ansioso sobre lo que podrá estar sacando de su mente."

show lilly basic_weaksmile
with charachange

li "Diría que eres un poco ingenuo."

"¿Ingenuo? Estaría siendo insultado de no ser por la sonrisa ligeramente cínica en su rostro."

hi "Ya veo…"

show lilly basic_reminisce
with charachange

li "Aunque Yamaku da una sensación más fuerte de comunidad comparada con otras escuelas, está lejos de estar libre de conflictos."

show lilly basic_displeased
with charachange

li "Las reglas no pueden eliminar la naturaleza humana después de todo, solo suprimirla."

"De hecho, eso es algo que he notado."

"Solo pequeñas cosas, por ejemplo el cómo ciertas personas y grupillos se evitan los unos a los otros en los pasillos. No es diferente de mi vieja escuela, en verdad."

"Inclusive Lilly y Shizune pueden ser consideradas rivales encarnizadas, aun a pesar de que ambas parecen aceptar a las personas imparcialmente."

"Bueno, al menos la Mishaneada Shizune lo hace; quién sabe lo que en realidad sucederá con sus dedos y tras sus anteojos."

hi "Supongo que tienes razón. Pero cuando recién llegué aquí, todo fue un poco como un shock."

hi "Me mantuve cometiendo errores, o al menos pensando que había estado cometiendo errores. Como cuando nos conocimos, y te dije “ya veo”."

hi "No sabía si eso era considerado maleducado o algo, así que solo traté de llevarlo al fondo de mi mente. Tratar a las personas diferente de alguna forma y ese tipo de cosas."

hi "Así que no lo hice. Me dije a mí mismo que Hanako y tú y todos los demás eran simplemente normales, y traté de ignorar lo obvio."

hi "Le hablé a Hanako como si fuera cualquier otra persona, y entonces nos hicimos amigos."

hi "O al menos, así es como creo que sucedió."

hi "Pero ya sabes, me siento culpable solo de decir algo así en voz alta. Como si tomara un esfuerzo extra pensar en Hanako, o en ti, o en cualquiera aquí como personas normales. No creo que eso sea correcto."

show lilly basic_smileclosed
with charachange

li "Hisao, creo que eres ingenuo, pero también creo que eres una buena persona. Creo que es uno de tus mejores rasgos."

hi "Yo… supongo… que puedo tomar eso como un cumplido…"

show lilly basic_smile
with charachange

li "Dime, ¿estás libre esta noche?"

hi "Si no cuentas la tarea, entonces estoy tan libre como el viento."

show lilly basic_cheerful
with charachange

li "En ese caso, ¿te importaría unirte a mí y Hanako para el té?"

hi "Em, en realidad no tengo mucho dinero por el momento, así que salir no es realmente…"

show lilly basic_smile
with charachange

li "Oh, no quise decir salir a algún lado. Simplemente aquí, esta noche."

hi "¿Pueden acceder a los salones en la noche aquí?"

show lilly basic_giggle
with charachange

li "No, no es lo que quise decir. Hanako y yo frecuentemente usamos mi habitación como cuarto para fiestas de té. Por favor siéntete libre de pasar después del atardecer."

hi "Seguro, no veo problema en ello. ¿Cuál es el número de tu habitación?"

show lilly basic_smileclosed
with charachange

li "225; Habitación 25 en el segundo piso."

hi "Está bien, seguro."

show lilly basic_weaksmile
with charachange

li "Bien entonces, mejor me retiro. Tengo tareas de representante de la clase por atender, después de todo."

show lilly basic_cheerful at center
with dissolvecharamove

li "Hasta esta tarde, Hisao."

hi "Sí, te veo después."

hide lilly
with charaexit

stop music fadeout 8.0

"Un momento… ¿acabo de ser invitado al cuarto de una chica por la noche? ¿Eso está siquiera permitido?"

"Hay un toque de queda aquí, pero nunca escuché nada de reglas sobre visitantes en los dormitorios."

"Aun así, esto es suficiente para hacer a mi cerebro privado de sueño saltar despierto."

"Añade a eso un desayuno frío y tienes un tremendo despabilante."

scene bg school_scienceroom
with locationskip

"Acudo a clases de mala gana, aún un poco alborotado ante la probabilidad de romper las reglas."

"Me siento un poco como un niño planeando escabullirse por su ventana en la noche."

"Bueno, tal vez eso es ir un poco lejos, pero cuando comparas una invitación a una fiesta con más o menos seis horas de sermones, sé cuál es la ganadora."

"Misha y Shizune tampoco hacen mucho por liberarme de mi aburrimiento. Por primera vez, parecen de hecho determinadas a completar los trabajos de Mutou."

scene bg school_scienceroom_ss
with shorttimeskip

play sound sfx_normalbell

"Sin embargo, el día eventualmente llega al cierre."

scene bg school_dormhisao_ss
with locationskip

"Me apresuro a volver a mi habitación para lavarme y cepillar mi cabello. Por suerte no me topo con Kenji."

scene bg school_dormext_full_ss
with locationchange

"Al poco tiempo estoy dejando los dormitorios de chicos."



label es_H7:

scene bg school_girlsdormhall
with locationskip

play sound sfx_doorknock2

"Nerviosamente doy unos golpecitos en la puerta marcada 225, revisando mi reloj una vez más."

li "¿Eres tú, Hisao? La puerta está abierta, puedes entrar."

"La voz de Lilly juguetea a través de la puerta y tranquiliza mis nervios."

"Esta es la primera vez que he sido invitado a la habitación de una chica después de anochecer."

"A pesar de que sé que no hay motivos encubiertos tras esta invitación, no hace que mi mente pare de viajar a salvajes posibilidades."

"Un chico. Dos chicas. En un dormitorio. Con un juego de té."

"Cuando lo pongo así, suena un poco arriesgado."

"Dando un pequeño suspiro para estabilizarme, cautelosamente pongo mi mano en la manija y abro la puerta, estirando mi cabeza para ver dentro."

play sound sfx_dooropen

window hide

scene white
with dissolve

with Pause(0.1)

play music music_one fadein 10.0

scene ev lilly_bedroom:
    truecenter
    zoom 1.1 subpixel True
    ease 15.0 zoom 1.0
with Dissolve(4.0)

window show

"La puerta se abre por completo y obtengo mi primer vistazo de la habitación de Lilly."

"Su amueblado parece casi antiguo, pero las paredes desnudas y superficies planas están apenas decoradas. En el centro del cuarto descansa una mesa baja, donde veo un juego de té en espera."

"Parece que todo en esta habitación tiene su lugar, posiblemente exceptuando las muchas pilas de libros amontonadas contra la pared."

"Mi sentido de la vista no es el único estimulado; el tenue aroma de algo puede captarse en el aire. Esmalte de uñas, perfume, maquillaje… es difícil de describir de otra forma sino “de chicas”."

"Mis ojos terminan su rápida examinación del cuarto, antes de regresar a su posición hacia las chicas."

scene ev lilly_bedroom_large:
    xpos -130 ypos -400 subpixel True
    acdc_warp 4.0 ypos -600
with flash

"Lilly se sienta junto a la pequeña mesa, vistiendo una pijama de azul bastante oscuro. Pijama azul oscuro con shorts que muestran mucho de sus atractivas piernas pálidas."

show ev lilly_bedroom_large:
    ease 1.0 ypos -300 xpos -830
    acdc_warp 12.0 ypos 0 xpos -830
with None

"Opuesta a ella, Hanako descansa adornada en un conservador camisón rosa claro."

"Sus manos están fijas firmemente entre sus piernas, sus hombros hacia adelante, y su cabeza gacha, como tratando de esconderse en la pijama."

"Sería fácil para ella hacerlo; parece ser grande por dos tallas para ella."

"Pliegues de franela caen de su cuerpo, haciéndola ver como una niña jugando vestida con la ropa de sus padres."

"Ella mira hacia arriba para confirmar mi identidad, y el principio de una ligera sonrisa se desliza en su rostro, antes de desvanecerse tan rápido que no puedo estar seguro de que haya estado ahí."

show ev lilly_bedroom_large:
    ease 1.0 xpos -130 ypos -400
with None

li "No hay razón para que te quedes parado en el pasillo, Hisao."

scene bg school_dormlilly
show lilly basic_smile_paj:
    twoleft
    ypos 1.2
show hanagown distant:
    tworight
    ypos 1.17
with locationchange

play sound sfx_doorclose
stop music fadeout 10.0

"Doy un paso hacia dentro de la habitación, cerrando la puerta tras de mí."

show lilly basic_weaksmile_paj
with charachange

li "Vaya vaya, me temo que esta es en verdad una habitación pequeña para los tres. ¿Gustas tomar asiento?"

"Lentamente camino a la mesa y me siento, tratando tanto como puedo de no alterar nada en el camino."

"Igualmente no puedo evitar lanzar una rápida mirada a la parte de arriba de Lilly mientras me siento."

"Ser privado de la vista sería un destino terrible."

show lilly basic_smileclosed_paj
with charachange

li "Bueno ahora, ¿qué tal un poco de té? Hanako, ¿podrías por favor servir?"

show hanagown normal_blush
with charachange

ha "S… seguro. Hi… sao… gus…"

show hanagown distant_blush
with charachange

ha "… Gustas…"

show hanagown worry_blush
with charachange

ha "… Gustas un…"

hi "Me encantaría un poco de té. ¿Necesitas una mano?"

show hanagown normal_blush
with charachange

ha "N… no, estoy bien…"

show hanagown smile
with charachange

ha "Gracias…"

play music music_dreamy fadein 2.0

show lilly basic_giggle_paj
with charachange

"Lilly encuentra difícil resistirse a sonreír por el nerviosismo de su compañera, algo por lo que no puedo culparla."

show hanagown distant
with charachange

hi "¿Día agotador?"

show hanagown smile
with charachange

ha "S… sí."

show lilly basic_smileclosed_paj
with charachange

"Me relajo en mi lugar, opuesto al armario."

"A mi izquierda una Lilly cubierta de azul y a mi derecha se sienta la rosada Hanako."

show teaset:
    xalign 0.5 yanchor 0.5 ypos 0.6 alpha 1.0
    easein 0.5 ypos 0.5
with charaenter

"El juego de té en la mesa luce bonito al igual que práctico; pintado de rojo con un adorno floral."

"Se ve extraño comparado con los planos pero generalmente sofisticados muebles de Lilly, lo que me lleva a pensar que tal vez Hanako lo eligió."

"Hay un ligero “ding” cuando Hanako golpea accidentalmente la tetera con una taza mientras está sirviendo."

show hanagown worry
show lilly basic_displeased_paj
with None

show teaset:
    easeout 0.5 alpha 0.0 ypos 0.6
with Pause(0.5)

hide teaset
with None

"Ella aspira bruscamente; debe estar en verdad nerviosa, pues no es el tipo de cosa por la que cualquiera se preocuparía."

show hanagown worry_blush
with charachange

"Hanako se estremece por su error."

show lilly basic_weaksmile_paj
with charachange

li "Está bien, Hanako. No hay por qué estar nerviosa."

show hanagown normal
with charachange

"Hanako parece encontrar un poco de confianza en las tranquilizadoras y suaves palabras de Lilly y hábilmente sirve las siguientes dos tazas."

show hanagown normal_blush
with charachange

ha "Aquí tienen, Hisao… Lilly."

"Hanako cuidadosamente coloca una taza y un platito frente a mí y Lilly. Podría acostumbrarme a un servicio como este."

show lilly basic_smile_paj
with charachange

li "Gracias, Hanako."

hi "Sí, gracias."

show hanagown smile
with charachange

ha "No hay problema."

show lilly basic_smileclosed_paj
with charachange

"Lilly busca su taza, y luego de encontrarla, sorbe delicadamente."

"Hago lo mismo. Este té sabe un poco mejor que el té que tomamos usualmente en la escuela."

hi "Está bueno, es muy diferente de cualquier té que haya probado antes…"

show lilly basic_ara_paj
show hanagown normal_blush
with charachange

li "Parece que elegiste el correcto, Hanako."

show lilly basic_smileclosed_paj
with charachange

li "Has hecho bien, incluso si fue un movimiento atrevido."

show hanagown smile
with charachange

"La sonrisa de Hanako regresa, redoblada."

"Incluso con su rostro lastimado, a su tímida sonrisa no se le podría llamar sino “linda”."

show hanagown distant_blush
with charachange

ha "Me alegra que te gustara…"

"Hanako, finalmente comenzando a relajarse, sorbe de su taza."


label es_H7a:

$ renpy.music.set_volume(0.5, 1.0, channel="music")
window hide
nvl clear
nvl show dissolve

n "Vuelvo a pensar en mi charla con Misha el otro día."

n "¿Es el comportamiento de Hanako algo por lo cual preocuparse, o solo es tímida?"

n "Y por otro lado estuvo lo de Lilly esta mañana."

n "La preocupación de ambas parecía ser genuina, y ambas conocen la situación mejor que yo."

n "Pero, en verdad, ¿yo cómo podría ayudar?"

n "No soy cirujano plástico, así que en realidad no puedo ayudar con su apariencia. Ni soy psicólogo para poder hacerla más sociable."

n "Así que ¿qué demonios quieren Lilly y Misha que haga?"

n "Es frustrante. Hanako y yo nos estamos volviendo amigos rápidamente por decisión mutua, y debido a esto, es como si todos quisieran que solucione todos sus problemas."

n "Y no tengo idea de cómo hacer eso."

n "Nadie puede curar mi corazón, ni los ojos de Lilly, ni a nadie de los que están aquí, en esta escuela."

n "Como sea, no veo problema en hacerme un mejor amigo de Hanako. Ahora que estoy empezando a agradarle creo que me gusta pasar el rato con ella."

$ renpy.music.set_volume(1.0, 1.0, channel="music")
nvl clear
nvl hide dissolve
window show



label es_H7b:


$ renpy.music.set_volume(0.5, 1.0, channel="music")
window hide
nvl clear
nvl show dissolve

n "\n\n\n\nAlgo sobre todo esto me hace pensar en la pregunta de Lilly en el desayuno."

n "¿Por qué soy amigo de Hanako?"

n "Lilly parece genuinamente preocupada por el bienestar de Hanako, pero no es como si yo pudiera hacer algo para salvarla."

n "Hasta donde puedo ver, sus cicatrices no la limitan físicamente, y todos los que he conocido parecen haber superado sus discapacidades hasta cierto punto."

n "No tengo ningún motivo oculto para pasar el rato con Hanako, solo compartimos intereses similares."

n "\n¿No es eso suficiente?"

$ renpy.music.set_volume(1.0, 1.0, channel="music")
nvl clear
nvl hide dissolve
window show




label es_H7c:

show lilly basic_smile_paj
with charachange

li "Así que, Hisao, ¿estás disfrutando el momento?"

"Las palabras de Lilly me sacan de mis ensoñaciones, y tomo un segundo para reconsiderar el lugar en el que estoy."

"Estoy en un cuarto con dos chicas en ropa de dormir. Esto es algo para disfrutarse."

hi "Desde luego, es relajante. Casi como si ya no estuviera en la escuela. ¿Hacen esto a menudo?"

show lilly basic_weaksmile_paj
with charachange

li "Bastante seguido, pero no tanto como tomar el té en el edificio escolar."

"Considerando que hacen eso casi a diario, esto no es una gran sorpresa."

"Al moverme para tomar otro sorbo de mi taza de té, la encuentro tristemente vacía."

hi "Eso fue delicioso. Gracias Hanako, Lilly."

show hanagown smile
with charachange

ha "No ha sido nada."

show lilly basic_smile_paj
with charachange

li "Sí, ha sido un placer Hisao. Es bueno tener una tercera persona aquí."

hi "Bueno, en cualquier ocasión que necesiten llenar esa posición, estoy siempre disponible. Siempre."

"Uno debe asegurarse de darse a entender en estas circunstancias."

stop music fadeout 8.0
show lilly basic_sleepy_paj
with charachange

"Lilly deja salir un bostezo, que inconscientemente esconde con su mano."

show lilly basic_weaksmile_paj
with charachange

li "Disculpen, creo que estoy un poco cansada."

show hanagown distant
with charachange

ha "Creo que todos estamos un poco cansados…"

show lilly basic_ara_paj
with charachange

li "Vaya vaya, qué perspicaz estás hoy, Hanako."

show lilly basic_weaksmile_paj
with charachange

li "En verdad deberíamos ir a la cama; todos tenemos clase mañana."

hi "Sí… me tengo que ir."

show lilly basic_smile_paj
with charachange

li "Gracias por tu presencia, Hisao."

show hanagown normal
with charachange

ha "Gra… gracias. ¿Vendrás otra vez?"

hi "Ni un ejército podría detenerme."

show lilly basic_cheerful_paj
with charachange

li "Estoy impresionada por tu determinación, Hisao."

hi "De cualquier modo, tienes razón. Lo mejor es que nos vayamos."

"Me levanto, y camino hacia la puerta."

show hanagown normal at tworight
with dissolvecharamove

"Hanako cautelosamente se pone de pie tras de mí."

"Me detengo y volteo a verla."

hi "¿Te vienes conmigo?"

play music music_comedy fadein 0.5

show hanagown normal_blush
with charachange

"Instantáneamente Hanako se sonroja por completo."

show hanagown distant_blush
with charachange

ha "No… yo… no… este cuarto… no es…"

hi "Está bien, solo bromeaba."

show hanagown smile
with charachange

ha "Oh… bien… buenas noches…"

show lilly basic_smileclosed_paj
with charachange

li "Buenas noches, Hanako. Buenas noches, Hisao."

hi "Buenas noches a ambas."

"Y con eso, nuestra fiesta de té termina."

scene bg school_girlsdormhall
with locationchange

"Aún no estoy seguro de qué es lo que Lilly quiere que haga por Hanako, pero no quiero defraudarla."

"Espero hasta que la puerta se ha cerrado tras nosotros antes de voltear hacia Hanako."

show hanagown distant_blush
with charaenter

hi "Oye, Hanako, sabes, no tienes que estar nerviosa en mi compañía ni nada."

hi "Quiero decir, somos amigos, ¿cierto?"

show hanagown normal_blush
with charachange

ha "Ci-cierto. Somos… amigos."

hi "Si alguna vez quieres pasar el rato o lo que sea, házmelo saber. Aún necesitamos tener esa revancha de ajedrez, ¿recuerdas?"

show hanagown distant
with charachange

ha "S-seguro…"

show hanagown normal
with charaenter

ha "P-pero no creo que ganes…"

hi "No sería divertido si fuera fácil."

show hanagown smile
with charachange

"Hanako parece dar una risa muda, pero podría fácilmente haber solo exhalado."

ha "B-buenas noches Hisao…"

show hanagown invis at tworight
with Dissolvemove(0.5, time_warp=_ease_out_time_warp)

hide hanako
with None

stop music fadeout 5.0

"Con eso, Hanako rápidamente se retira a su cuarto, localizado enseguida del de Lilly."

"Comienzo a caminar de vuelta a mi dormitorio, pero el simple acto de caminar parece mermar mi energía."

scene bg school_dormhisao
with locationskip

"Apenas logro llegar a mi habitación antes de ser golpeado por una ola de agotamiento."

play sound sfx_switch

scene bg school_dormhisao_ni
with Dissolve(0.2)

"Aviento mis zapatos, caigo en la cama y me duermo tan pronto como mi cabeza golpea la almohada."

scene black
with dissolve


label es_H8:

scene bg school_dormhallway
with locationchange

"Cierro mi puerta, listo para otro día de clases."

show kenji invis at twoleft
with None

show kenji neutral_close at center
with Dissolvemove(0.5, time_warp=_ease_in_time_warp)

ke "¿Dormiste bien?"

play music music_kenji fadein 0.5

"La llegada súbita de Kenji me hace saltar, y evito por poco que choquen nuestras cabezas."

"Sé que tiene vista pobre, pero ya sabe quién soy. ¿Aún tiene que pararse así de cerca?"

show kenji neutral
with charadistant

hi "Oh. Sí. Como un bebé."

show kenji tsun
with charachange

ke "Maldición, ¿por qué la gente dice eso? ¿Alguna vez has escuchado a un bebé dormir?"

ke "Gritan. Toda la noche. Cada noche. Los bebés no duermen bien, nunca."

"Bueno, ahí va mi estado tranquilo. Tengo que recordar nunca usar figuras retóricas con Kenji."

hi "Está bien, entiendo tu punto. Era una figura retórica."

show kenji neutral
with charachange

ke "Sí, seguro, lo que sea. ¿Dónde estuviste anoche? Tenía que pedirte un favor pero no andabas por aquí."

"Por una fracción de segundo considero decirle a Kenji la verdad; que estaba pasando el tiempo con Hanako y Lilly."

"Por suerte, esa fracción de segundo pasa tan rápido como vino."

hi "Solo andaba fuera. Revisando la zona y eso. Ya sabes, reconocimiento."

show kenji happy
with charachange

ke "Bien, hombre, bien. Sabía que eras del tipo que planea con antelación…"

hi "Como sea, ¿cuál era ese favor que querías?"

show kenji neutral
with charachange

ke "Iba a ir por algo de comida para llevar, pero necesitaba cambio."

hi "Espera, ¿qué? ¡Te di dinero la semana pasada y aún no me has pagado!"

show kenji tsun
with charachange

ke "Tsch, y yo que estaba empezando a pensar que eras buena onda."

"Kenji busca un poco en sus bolsillos y saca su cartera."

"Mientras cuenta los 400 yen que me debe, puedo ver claramente al menos dos billetes de 10 000 yen."

hi "Oye, ¿qué demonios? ¿Por qué estás pidiendo prestado dinero cuando tienes tanto efectivo?"

"Kenji sisea un poco, dándose cuenta de que lo han descubierto."

ke "Deja mis asuntos, hombre. Es de mala suerte dividir un billete grande por cualquier cosa de menos de la mitad de su valor. Es la regla del magnate."

ke "La cena de anoche me costará siete años de mala suerte. ¡Siete años!"

show kenji happy
with charachange

ke "¿No crees que eso es causa suficiente para ayudar a alguien? Obtendría una sentencia más corta si simplemente robara esas cosas."

"Mi sentido común me grita para que le diga algo, pero por suerte me contengo."

"Discutir algo como esto con Kenji únicamente llevará a mayores y más complicadas discusiones."

hi "Sí, supongo que tienes razón. ¿Tal vez deberías planear estas cosas un poco mejor?"

show kenji neutral
with charachange

ke "Sí hombre, lo sé. Pero he tenido muchas cosas que hacer, es difícil. Y ya no estás nunca por aquí, así que estoy solo."

ke "Se supone que somos hermanos en hermandad, ¿recuerdas?"

hi "Sí sí, te entiendo. Conspiración global y eso. Mantendré mis oídos alertas."

show kenji neutral_close
with charachange

"Kenji se acerca lo suficiente a mí como para recibir claramente el tufo de su aliento con tintes de ajo."

show kenji tsun_close
with charachange

ke "Mejor que así sea, hombre. Ya estás pasando menos tiempo aquí. Esa es la primera cosa que hacen."

ke "Tratarán de dividirnos. Divide y vencerás. Sun Tzu dijo eso."

hi "Entendido. Ahora, tengo que irme. Tengo clase. ¿Vienes?"

show kenji neutral_close
with charachange

ke "Nah, estoy cansado. Estuve despierto toda la noche únicamente para asegurarme de que nada fuera a suceder después de dividir ese billete."

hi "Tan racional como siempre, ya veo."

show kenji tsun_close
with charachange

ke "Lo que sea. Buenas noches."

stop music fadeout 3.0

show kenji invis at twoleft
with Dissolvemove(0.5, time_warp=_ease_out_time_warp)

"Kenji se escabulle de vuelta a su habitación, y lo escucho poniendo sus seguros mientras camino por el pasillo."



label es_H9:

scene bg school_dormhallway
with None

scene bg school_scienceroom
show muto smile at center
with shorttimeskip

play music music_daily fadein 4.0

mu "… Ese es el porqué algunas personas no pueden enrollar su lengua, o el porqué su segundo dedo del pie es más largo que su dedo gordo."

"Mutou nos lanza una gran sonrisa, obviamente orgulloso de su explicación de los genes recesivos."

"Como sea, no importa lo impresionado que él esté por la ciencia que define quién eres, el salón de clase parece estar reducido a un estupor."

"¿Por qué es que una mala explicación puede hacer incluso a la cosa más interesante parecer inútil?"

show muto irritated
with charachange

"Puedo ver a Mutou desalentarse al darse cuenta de que nada de lo que ha dicho en la última media hora se ha impregnado."

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 4.0

"Conversaciones en voz baja comienzan a romper el silencio, y como una avalancha, el nivel de ruido en el grupo comienza a elevarse."

show muto normal
with charachange

"Derrotado, Mutou establece algunas preguntas del libro de texto y se prepara a limpiar el pizarrón."

hide muto
with charaexit

"Casi como si lo esperara, Hanako guarda sus cosas y se va tan pronto como las personas comienzan a hablar y reír entre ellas."

"El shock inicial de ver a alguien escapar de clase tan descaradamente ha comenzado a disiparse, pero no evita que me ponga a pensar."

"¿Se va porque no quiere que la gente le hable? ¿O solo es la idea de la gente a su alrededor rompiendo su paz?"

play sound sfx_normalbell
$ renpy.music.set_volume(1.0, 4.0, channel="ambient")

"Antes de poder pensar en ello más detenidamente, la campana del almuerzo suena. Me pregunto si solo estaba tomando la oportunidad de irse antes."

"El usual clamor de estudiantes intercambiando libros para el almuerzo reverbera en el lugar, y mientras Misha está distraída, agarro mi almuerzo y me dirijo a la puerta."

stop ambient fadeout 1.0

scene bg school_miyagi
show lilly basic_smileclosed:
    center
    ypos 1.2
with locationskip

"Lilly ya ha tomado asiento en el cuarto de té, preparando su almuerzo sola."

hi "Entonces, ¿Hanako no está aquí?"

show lilly basic_smile
with charachange

li "Oh, Hisao, ¿cómo estás? Me temo que no me he encontrado con Hanako desde esta mañana."

"Es cierto, Hanako y Lilly viven una al lado de la otra."

"De alguna forma creo que sus conversaciones son ligeramente más normales que las divagaciones de Kenji."

hi "Qué extraño. Se fue de la clase temprano, así que me imaginé que habría venido aquí."

show lilly basic_displeased
with charachange

li "Entonces continúa yéndose de la clase temprano…"

hi "¿Eh? Sí, la he visto hacerlo algunas veces."

show lilly basic_sad
with charachange

stop music fadeout 7.0

"Lilly inclina su cabeza un poco, y el tono de su voz es notablemente triste. Es demasiado nostálgico para alguien que está acostumbrado a escuchar malas noticias."

li "Estaba tan segura de que dejaría de hacer eso una vez que ustedes dos se hicieran amigos."

show lilly basic_weaksmile
with charachange

li "Todos tienen su propio ritmo, supongo."

hi "Bueno, me estaba preguntando eso hoy. ¿Exactamente por qué se va?"

show lilly basic_reminisce
with charachange

li "Ni yo estoy del todo segura. Personalmente creo que es porque no quiere que se le ponga en una situación donde tenga que responderle a alguien."

"Me viene un recuerdo momentáneo de mi primer encuentro con ella, cuando pensé que lucía como un animal acorralado. Tal vez no estaba lejos de la verdad."

hi "Pero parece estar bien con la idea de hablar contigo, y conmigo… un poco…"

show lilly basic_displeased
with charachange

li "Es un poco más complejo que eso. Imagino que la primera cosa que la mayoría de las personas le pregunta es sobre sus cicatrices, y lo que sucedió."

li "En raras ocasiones habla de eso conmigo, pero puedo decir que no le gusta recordar lo que sea que sucedió entonces."

show lilly basic_reminisce
with charachange

li "Dejar la clase y escapar de las discusiones es su ataque preventivo, si lo quieres ver así."

hi "Eh… ¿entonces cómo explica eso el que me haya hablado?"

show lilly basic_weaksmile
with charachange

li "Tú mismo lo dijiste ayer en el desayuno; trataste de ignorar sus cicatrices. Una vez que vio que no le preguntarías sobre eso, se abrió contigo."

hi "Hrm, supongo que tienes razón. Tal vez. No lo sé. La conoces mejor que yo, así que creeré en tus palabras."

play music music_normal fadein 3.0

show lilly basic_giggle
with charachange

li "No me preocuparía de eso. Estoy segura de que la llegarás a conocer tan bien como yo muy pronto."

show lilly basic_smileclosed
with charachange

li "Le doy la bienvenida a la esperanza de que ella tenga un nuevo amigo, y ustedes dos tienen tantos intereses similares…"

hi "Bueno, difícilmente cuento la lectura como un trabajo de equipo. Pero es bueno tener compañía."

show lilly basic_smile
with charachange

li "Ese es mi punto. En el fondo Hanako aún es una persona común. Ella también quiere compañía en ocasiones como esa."

hi "Oh, ya veo. Creo. Para ser honesto, ustedes dos aún me confunden un poco."

show lilly basic_smileclosed
with charachange

li "Eso es natural, Hisao. Solo nos hemos conocido por poco tiempo; no es razonable esperar entendernos, de la misma forma que no podemos entenderte."

show lilly basic_weaksmile
with charachange

li "Pero eso es la mitad de la diversión de hacerse amigos, ¿cierto?"

hi "Sí, sí lo es."

show lilly basic_giggle
with charachange

li "Aunque… supongo que está el problema de ser del género opuesto. Hombres y mujeres parecen confundirse los unos a los otros con frecuencia."

"Ella dice eso con una ligera risilla, encontrando diversión en los pequeños detalles extraños de la vida."

show lilly basic_cheerful
with charachange

li "Espero que no te moleste, pero empezaré a comer."

hi "No, adelante, creo que comeré algo también. Tengo unos libros que quiero devolver a la biblioteca antes de que las clases empiecen, así que mejor me apresuro."

show lilly basic_smileclosed
with charachange

li "Probablemente ahí encontrarás también a Hanako. Si la ves, ¿puedes decirle que pase a mi habitación más tarde en la noche? Me gustaría hablar con ella."

hi "¿No vienes?"

show lilly basic_weaksmile
with charachange

li "Desafortunadamente al rato tengo reunión de representantes de clase, así que me iré tan pronto como termine mi almuerzo."

hi "Bien entonces, si no la veo en la biblioteca se lo diré en clase. Estoy seguro de que volverá después del almuerzo."

"Guardamos silencio mientras comemos, y tomo un segundo para reflexionar sobre nuestra conversación."

"Siempre había pensado que la timidez de Hanako era simplemente por ser consciente de sus propias cicatrices."

"Pero eso es una forma muy superficial de verla."

"Justo cuando pensé que al fin podía ver a través de la niebla de Lilly y Hanako, me doy cuenta de que estoy más perdido que cuando empecé."

"Lilly rápidamente termina su almuerzo, plenamente consciente de su reunión. No la culpo."

"Seguramente Shizune estará ahí, y dudo que quiera darle la satisfacción de otra discusión."

show lilly basic_smile
with charachange

li "Debo irme. ¿Misma hora mañana?"

hi "Misma hora, mismo canal. Mejor me voy también; no quiero arriesgarme a llegar tarde."

show lilly cane_smileclosed
with charachange

show lilly cane_smileclosed at center
with charamove

stop music fadeout 4.0

"Lilly sonríe gentilmente, coge su bastón y camina hacia el pasillo."



label es_H10:

scene bg school_hallway2
with locationchange

"Doy la espalda a Lilly al ir en dirección opuesta. Por alguna razón espero que no vaya a meterse en otra pelea con Shizune."

"Por mucho que me agrade Lilly, Shizune y Misha han sido de gran apoyo al ayudarme a ajustarme, incluso si la mitad de nuestras conversaciones son intentos de reclutamiento apenas disimulados."

"Por otra parte, apenas las conozco un poco. Tal vez previamente fueron líderes de algún tipo de sociedad secreta, pero el amor entre ellas las hizo salir…"

"Hombre, necesito dejar de leer ficción barata. Está pudriendo mi cerebro. Eso o me tengo que alejar de Kenji y su mala influencia."

"Es triste que ya no pueda diferenciar entre ambas cosas."

scene bg school_library at right
with locationskip

play music music_happiness fadein 2.0

"Deslizo mis libros por la rampa de devoluciones y caen con un placentero golpe sordo."

play sound sfx_impact2

show yuuko panic_up
with vpunch

"De cualquier modo, Yuuko, no parece tan impresionada como yo."

yu "¡Hi-Hisao! ¡Me asustaste!"

hi "Perdón, pensé que ya estarías acostumbrada a eso. ¿O es el índice de alfabetización tan bajo aquí que nadie pide prestados libros?"

show yuuko worried_up
with charachange

yu "¿Eh? No, creo que todos pueden leer bien aquí…"

hi "Sí… no importa."

"Hay algunas batallas que nunca puedes ganar. Tratar de explicar chistes es una de ellas. Mi papá me enseñó eso del modo difícil."

hi "Dime, Yuuko, ¿has visto a Hanako por aquí? Dejó la clase temprano pero no estaba en su escondite usual."

show yuuko closedhappy_down
with charachange

yu "Creo que la vi escabullirse aquí antes del almuerzo…"

show yuuko panic_up
with charachange

yu "¡Oh! ¡Pero se supone que no debo decirle eso a nadie!"

hi "Te acabo de decir que yo la vi irse, no hay necesidad de que te estreses…"

show yuuko smile_down
with charachange

yu "Oh… desde luego. Ella está probablemente en la parte de atrás."

hi "Gracias. ¿Has recibido algunos libros nuevos recientemente?"

show yuuko worried_up
with charachange

yu "No, lo lamento. Pero te lo haré saber cuando así sea."

hi "Está bien."

"Si hay algo que sé sobre las bibliotecarias, de medio tiempo o como sea, es que aprecian a la gente que toma interés genuino en su trabajo."

hide yuuko
with charaexit

show bg school_library at Fullpan(10.0, dir="left")
with None

"Avanzo por el ahora familiar camino al rincón de lectura de Hanako, eligiendo algunos títulos en el recorrido."

"Algunas veces es difícil descubrir algún libro que me interesará entre los estantes. El nombre de un autor y títulos de dos palabras no dicen mucho en un mar de palabras similares."

"Por esa razón, algunas veces releo libros que leí en el pasado. Mejor apostar al favorito que al nuevo corredor."

"Un título desconocido de un autor familiar se asoma entre los lomos de sus vecinos, así que lo retiro del estante."

"Al menos no voy a repasar material viejo."

scene ev hana_library_read_std
with locationskip

"Como esperaba, Hanako está sentada en su puf, concentrada profundamente en una copia de “Baila Baila Baila”."

hi "Hola Hanako. ¿Cómo estás?"

"Lucho contra la necesidad de preguntar el porqué se fue temprano. Si las sospechas de Lilly son correctas, entonces preguntar sobre ello podría tener el efecto opuesto."

"Mejor dejarlo por el momento. Algunas veces la mejor forma de sacar una respuesta de alguien es nunca hacer la pregunta."

show ev hana_library_smile_std
with charachange

ha "Hola, Hi-Hisao. Estoy bien."

"Hay algo extraño aquí, y después de unos segundos, me doy cuenta de lo que es. Hanako está sonriendo."

"Luce como si estuviera feliz de verme. Es un buen cambio de la usual e instintiva reacción de miedo, y es algo que espero ver más conforme nos vamos conociendo mejor."

hi "Qué bueno escuchar eso. ¿Qué tal está el libro? He oído que es una pasada."

ha "Es bueno… creo."

ha "A-apenas lo he empezado, así que e-en realidad no sé."

hi "Desde luego. Hazme saber qué tal está; tal vez lo tomaré prestado una vez que termines."

ha "S-seguro."

"Restan unos quince minutos del almuerzo. No suficiente para meterse en un libro, pero bastante para estar por ahí sin hacer nada."

show ev hana_library_read_std
with charachange

"Y Hanako ya ha regresado a su lectura, así que dudo obtener mucha conversación de ella."

"Oh bueno, mejor me pondré cómodo."

play sound sfx_pillow

"Me desplomo en un puf y abro mi libro."

"El familiar estilo del autor salta desde la primera línea. Conforme las oraciones se tornan en párrafos, comienzo a relajarme un poco."

stop music fadeout 8.0

"Pero no importa cómo lo intente, parezco no poder meterme en la atmósfera del libro."

"Esto es en parte por la falta de tiempo, pero el factor de mayor distracción es Hanako."

show ev hana_library_std
with charachange

show ev hana_library_read_std
with charachange

"Más o menos cada diez segundos ella mira por encima de su libro, pero cuando nuestras miradas se cruzan rápidamente se esconde tras las pastas."

"Supongo que sí quería hablar sobre algo después de todo."

scene bg school_library
with locationskip

hi "¿Qué sucede? Luces como un perro de las praderas en alerta."

show hanako emb_blushing:
    center
    ypos 1.17
with charaenter

ha "E… nada."

hi "Te lo he dicho antes, “nada” significa “algo” cuando lo dices así."

show hanako cover_worry
with charachange

"Hanako se encorva un poco en su puf, esperando que cambiando de posición encontrará las palabras que está buscando."

show hanako emb_downsad
with charachange

ha "Yo… estuve en un accidente."

hi "¿Accidente? ¿Justo ahora? ¿Estás bien?"

show hanako emb_sad
with charachange

"Hanako sacude su cabeza, fluyendo su cabello alrededor de sus hombros en mechones de amatista en un fondo de pálida y oscura carne."

show hanako emb_downsad
with charachange

ha "N-no. Cuando era m-más chica."

play music music_hanako

"Súbitamente caigo en la cuenta de lo que está hablando."

ha "Cuando yo… cuando yo era…"

hi "Está bien Hanako, no tienes que decirme nada si no quieres…"

"Una vez más sacude su cabeza."

show hanako emb_sad
with charachange

ha "N-no. Quiero… tengo que decirte."

scene ev hanako_crayon1:
    truecenter zoom 1.0 subpixel True
    linear 20.0 zoom 1.05
with locationskip

ha "Cuando era pequeña… estuve en un incendio."

ha "M-mi casa s-se quemó, y por poco… por poco no salí."

show ev hanako_crayon2:
    linear 8.0 zoom 1.05
with charachange

ha "D-después de eso… estaba sola…"

scene bg school_library
show hanako emb_downsad_close:
    center
    ypos 1.1
with locationskip

"Los ojos de Hanako brillan en la tenue luz de la biblioteca, y me acerco para tomar su mano."

hi "Está bien, Hanako. No tienes que seguir."

show hanako emb_sad_close
with charachange

ha "P-pero… tengo que…"

hi "¿Por qué? ¿A qué se debe esto?"

show hanako cover_distant_close
with charachange

ha "A-anoche Lilly me d-dijo sobre tu corazón…"

show hanako cover_worry_close
with charachange

ha "Y no… no p-pensé que fuera j-justo."

hi "¿Justo?"

show hanako emb_blushing_close
with charachange

ha "Que yo s-supiera sobre ti p-pero tú no supieras sobre mí…"

"Aprieto la mano de Hanako un poco."

hi "No seas tontita. Pero sí, tengo una condición del corazón."

"Me inclino un poco hacia Hanako."

hi "Lo que no le dije a Lilly es que tuve mi primer ataque cuando una chica se me declaró."

"Sonrío un poco para romper la tensión."

show hanako cover_worry_close
with charachange

ha "¿E-en verdad?"

hi "En verdad. Aunque no he escuchado de ella en un rato, así que supongo que todo ha terminado."

"Sé que ha terminado. No hay otra forma de interpretar lo que sucedió la última vez que la vi. De alguna forma, no haber escuchado otra vez de ella me ha ayudado a moverme de ese periodo de mi vida."

hi "Así que ahora, ambos sabemos un poco más de cada uno. Pero no tienes que hablar sobre algunas cosas si no quieres."

"De hecho, me siento un poco mal incluso de pensar en todo ese accidente. Casi puedo oler el desinfectante de hospital quemando dentro de mis orificios nasales."

"Imagino que Hanako está pasando por lo mismo en este momento."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\nCuando estaba en el hospital fui a la sala de quemados una vez, solo una. Estaba aburrido, así que fui a caminar a través de todas las salas."

n "Fui a oncología y pensé que podría hacerlo, pero cuando llegué a la sala de quemados di la vuelta y volví a mi cama."

n "Pensar que Hanako podría haber pasado meses en un lugar como ese, sin oler nada más que piel muerta, fuerte desinfectante y aire esterilizado."

n "Los casos realmente malos se mantenían en cabinas aisladas en las que no pudieran entrar objetos externos. Eso habría significado quedarse sin lectura."

n "\nMe habría vuelto loco si no hubiera tenido mis libros en el hospital."

n "Y ella dijo que estaba sola…"

n "¿Sus padres murieron? Tendré que preguntar a Lilly sobre ello. Puedo imaginarme diciendo algo estúpido sin intención."

stop music fadeout 2.0

nvl clear
nvl hide dissolve

show hanako emb_timid_close
with charachange

window show

ha "G-gracias, Hisao."

show hanako emb_downtimid_close
with charachange

ha "No… no le he dicho a nadie sobre esto."

hi "Para ser honesto, tampoco le he dicho a mucha gente sobre mi… circunstancia."

show hanako cover_smile_close
with charachange

ha "E-entonces no le diré a n-nadie tampoco."

hi "Hecho."

play sound sfx_warningbell

"Cambio mi agarre de la mano de Hanako a un apretón de manos mientras las campanas de aviso repican a través de la ventana."

hi "Bien entonces, mejor nos vamos de vuelta a clase, ¿eh?"

show hanako basic_bashful_close
with charachange

ha "S-seguro."
$ renpy.music.set_volume(1.0, 0.0, channel="music")

window hide

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
