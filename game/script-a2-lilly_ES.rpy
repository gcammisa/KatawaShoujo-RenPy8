label es_L1:

window hide None

scene black
with dissolve

play sound sfx_alarmclock

with Pause(2.0)

scene bg school_dormhisao
with openeye

window show

"Me despierto escuchando el estruendo molesto de mi reloj despertador, y sus brillantes números rojos iluminan mi rostro."

play music music_dreamy fadein 2.0

"Es el mismo reloj despertador que tenía en casa, uno de los pocos artefactos que quedan de mis días antes de venir a Yamaku. Esperaba que usarlo me ayudaría a aliviar mi transición a esta nueva vida."

"Sin embargo, no tengo tal suerte."

"Arrastrándome adormiladamente de la cama, limpio el sueño de mis ojos, y luego extiendo mi brazo hacia el escritorio. Abro un par de frascos de medicamentos esparcidos por él, y me trago en seco unas cuantas píldoras."

"Ya el proceso está comenzando a volverse automático, algo de lo que debería alegrarme, dado su propósito."

$ renpy.music.set_volume(0.5, 2.0, channel="music")

scene bg school_dormbathroom
with locationskip

"Sintiéndome mucho más despierto que antes, me dirijo al baño."

play ambient sfx_shower fadein 8.0

show steam
with charaenter

"Mientras la ducha se calienta, mi mente comienza a divagar al comenzar mi nueva rutina diaria una vez más."

"Los colores brillantes de los fuegos artificiales llenan mi mente, igual que las dos chicas con quienes pasé el tiempo observándolos. Se siente extraño estar tan conmovido por gente tan desconocida."

"Por otra parte, supongo que estas tampoco son circunstancias normales. Por lo menos tengo con quién hablar ahora, además de mi compañero vecino."

stop ambient fadeout 2.0

hide steam
with charaexit

"Con el tiempo que queda antes de las clases de hoy disminuyendo, comienzo a prepararme para salir."

$ renpy.music.set_volume(1.0, 3.0, channel="music")

scene bg school_scienceroom
with shorttimeskip

"Atravesando la puerta para entrar al salón, noto que he llegado un poco temprano. Veo unos cinco o seis estudiantes dando vueltas, la mayor parte de ellos luciendo como si prefirieran seguir en cama."

"En momentos como estos, agradezco ser una persona madrugadora. Dicho eso, dos estudiantes en particular se ven tan animadas como siempre."

hi "Hola Shizune, hola Misha."

show shizu behind_blank at tworight
show misha perky_smile at twoleft
with charaenter

"De pronto me doy cuenta de que mi saludo no será recibido por la primera, así que rápidamente lo continúo con una seña de mano. Ella no parece demasiado molesta."

"Ni tampoco interesada."

show shizu basic_normal
with charachange

shi "…"

show misha hips_grin
with charachange

mi "¡Hola, Hicchan~! ¿Te sientes bien?"

"Solamente puedo asumir que su saludo proviene de Shizune. A veces es difícil saber si está hablando como ella misma o como Shizune."

hi "Mejor que la mayoría de los demás, creo. Ustedes dos parecen alegres y animadas."

show misha sign_smile
with charachange

show misha perky_smile
show shizu basic_frown
with charachange

"Misha le interpreta a Shizune mientras hablo, obteniendo una respuesta un poco brusca, si los movimientos rápidos y agudos de sus brazos son alguna indicación."

"Considerando que ellas dos le dieron tanta importancia a los preparativos del festival, probablemente debería de haber elegido mis palabras más cuidadosamente."

show shizu behind_frown
with charachange

shi "¡…!"

show misha hips_grin
with charachange

mi "Ya que eres un estudiante nuevo, te hemos estado dando un respiro. Por favor no esperes que este tipo de evasión de tareas sea permitido en el futuro."

"Misha parece estar a punto de agregar su propio comentario, pero rápidamente vuelve a interpretar a Shizune mientras esta continúa, sin detenerse."

show shizu basic_frown
show misha sign_smile
with charachange

mi "Aunque tu contribución al puesto del grupo 3-2 es apreciada—"

"Eh. Esa noticia sí se difundió bastante rápido. Eso, o estas dos están al tanto de todo en la escuela."

show misha hips_frown
with charachange

mi "—preferiríamos que tus esfuerzos se enfocaran en la tarea que nos ocupa. Concretamente, tu propio grupo."

"Aunque odio admitirlo, tienen razón. Sin embargo, antes de poder responder, Shizune añade algo más, lo que saca una sonrisa de Misha."

show shizu behind_blank
with charachange

shi "…"

show misha perky_smile
with charachange

mi "¿Entonces disfrutaste del festival~?"

"Se acabó el sermón, creo."

hi "Sí, estuvo bien. ¿Ustedes dos lo disfrutaron?"

show shizu behind_smile
show misha hips_grin
with charachange

"Shizune asiente brevemente mientras que Misha sonríe y hace saltar su cabeza. La comparación, lado a lado, es graciosa."

"De reojo, noto que más estudiantes comienzan a escurrirse al salón. Una rápida mirada a mi reloj confirma que han llegado algunos minutos tarde."

show hanako emb_downtimid at offscreenright
with None

show misha hips_grin at left
show shizu behind_smile at Transform(xpos=0.48)
show hanako emb_downsmile at Transform(xpos=1.0, xanchor=0.7)
show bg school_scienceroom at bgleft
with charamove

"Miro hacia el asiento de Hanako y me doy cuenta de que ella ya está ahí, y está leyendo un libro tranquilamente. Me hace preguntarme cuánto tiempo lleva ahí sin que yo me diera cuenta."

show misha hips_grin:
    ease 1.0 xpos 0.2
show shizu behind_smile:
    ease 1.0 tworight
show hanako emb_downsmile:
    ease 1.0 offscreenright
show bg school_scienceroom:
    ease 1.0 center
with None

hide misha
hide shizu
hide hanako
with Dissolve(1.0)

"Con los pasos pesados que vienen del pasillo señalando la llegada de Mutou, nuestra plática termina y me siento al lado de Misha."

"Cuando la puerta se abre, él entra con un andar aletargado. Su postura es incluso peor que lo usual, y sus ojos apenas se mantienen abiertos. Supongo que la broma que les dije a Lilly y Hanako sobre el personal estuvo fuera de lugar."

play ambient sfx_paperruffling

"Todos abren sus libros mientras él llega a su escritorio, y la primera clase de la nueva semana comienza."

stop music fadeout 3.0
stop ambient fadeout 0.5

with shorttimeskip

play sound sfx_normalbell

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0

"Froto mis ojos cuando timbra la campana del almuerzo, contento con el descanso temporal del trabajo."

show lilly basic_smileclosed at offscreenleft
with None

show bg school_scienceroom at bgright
show lilly cane_smileclosed at Transform(xanchor=0.2)
with charamove

"No me sorprende para nada cuando miro hacia la puerta y veo a Lilly parada ahí, bastón en mano, esperando pacientemente a Hanako."

"Considerando su aprobación de mi petición de unírmeles ayer, decido pasar mi hora del almuerzo con ellas en lugar de comer solo."

show hanako emb_smile at Alphain(0.5), Slide(0.5,0.5,0.4,0.5,0.5)
with Pause(0.5)

hide hanako
hide lilly
with charaexit

"Hanako se mueve sorprendentemente rápido para recibir a su acompañante, y las dos entran al pasillo antes de que pueda alcanzarlas."

stop ambient fadeout 1.0

scene bg school_hallway3
show lilly back_listen at twoleft
show lillyprop back_cane at twoleft
show hanako emb_downsmile at tworight
with locationchange

show hanako def_shock
with vpunch

"Lilly voltea la cabeza ligeramente, registrando el sonido de pasos detrás de ella. Cuando Hanako lo nota y sigue su movimiento, casi salta de sorpresa."

show hanako defarms_strain
with charachange

ha "¿Hi… Hisao?"

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play music music_normal fadein 2.0

show hanako emb_blushtimid
with charachange

ha "Digo… em… hola, Hisao…"

hi "Hola. Disculpa si te asusté."

show lilly cane_smile
hide lillyprop
with charachange

"Lilly se da la vuelta para saludarme, su orientación ayudada por Hanako."

show lilly cane_smileclosed
with charachange

li "Buenas tardes, Hisao. ¿Nos acompañarás?"

hi "Si no es molestia. Realmente no hay mucho más que hacer."

show lilly cane_smile
with charachange

"Lilly asiente levemente, como para apartar en silencio cualquier idea de que podría causar problemas en lo más mínimo."

scene bg school_staircase2
with locationchange

with Pause(0.3)

scene bg school_hallway2
with locationchange

"Bajamos por una serie de escaleras y caminamos por el pasillo hacia el cuarto de siempre, nuestro paso un tanto más rápido gracias a que Lilly está usando a Hanako para orientarse, en lugar de su bastón y los barandales."

scene bg school_miyagi
with locationchange

"Como esperábamos, está vacío. Los sonidos de los otros clubes apenas se pueden oír mientras la luz entra al cuarto desde afuera."

"Registrando el cuarto, noto un par de caballetes vacíos apoyados contra una pared que no creo que estuvieran antes. El club de arte debe usar este cuarto como bodega adicional."

show hanako emb_smile
with charaenter

ha "¿Saco el juego de ajedrez?"

"La voz de Hanako parece menos tensa cuando está hablándole directamente a Lilly."

show hanako emb_smile at tworight
show bg school_miyagi at bgright
with charamove

show lilly cane_weaksmile at twoleft
with charaenter

li "Sí. Prepararé té mientras ordenas las piezas."

hi "Ah, puedo hacer eso por ti, si quieres."

show lilly cane_surprised
with charachange

with Pause(0.3)

show lilly cane_planned
with charachange

"Considera la oferta un momento antes de sonreír, confirmando que he tomado la decisión correcta. Su rostro es sorprendentemente fácil de leer."

show lilly cane_satisfied
with charachange

li "Muy bien. Gracias."

show lilly cane_satisfied:
    ease 0.5 ypos 1.3
    "lilly basic_cheerful" with Dissolve(0.5, alpha=True)
    ease 0.5 ypos 1.0
with Pause(1.0)

hide lilly
hide hanako
with charaexit

"Ella desliza su bastón replegado por la manilla de su bolso y lo apoya contra una de las patas de la mesa, antes de tomar asiento opuesta a Hanako."

"Mientras preparo el té para nosotros tres, puedo oír las pequeñas piezas de madera siendo colocadas en el tablero. Me pregunto qué tan buena será Lilly para el ajedrez, considerando sus circunstancias."

"Cuando por fin pongo las tazas humeantes de té sobre la mesa, Lilly y Hanako ya han movido sus primeras piezas mientras mordisquean emparedados y bolas de arroz de sus bolsas respectivas."

$ renpy.music.set_volume(0.5, 2.0, channel="music")

show chessboard:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"Noto que el tablero de ajedrez que están usando tiene huecos en medio de cada cuadrado y clavijas debajo de las piezas, y que cada cuadrado oscuro está levantado un poco."

"Ver los dedos de Lilly deslizarse sobre el tablero, trazando las posiciones de las piezas, me hace maravillarme un poco del simple ingenio del diseño. Debe de haber sido hecho específicamente para jugadores ciegos."

$ renpy.music.set_volume(1.0, 5.0, channel="music")

show chessboard:
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide chessboard
with None

hi "Aquí tienen."

scene bg tearoom_everyone_noon
show tearoom_hanae happy
show tearoom_lillye smileclosed
show tearoom_hisaoe hsmile
show tearoom_chess
with locationskip

"Hanako asiente ligeramente cuando pongo una taza en su lado del tablero. La mano de Lilly se extiende ligeramente, así que pongo su taza para que toque las puntas de sus dedos; un gesto que parece agradecer."

show tearoom_hisaoe outside
with charachange

"Por fin tomo asiento y doy sorbos a mi té en silencio mientras las dos juegan. Es interesante mirar el contraste de sus apariencias mientras se concentran."

show tearoom_hanae open
with charachange

"Hanako mira de cerca el tablero, su rostro demostrando concentración enfocada. Lilly, por otra parte, mantiene su rostro tranquilo y conserva su serena neutralidad."

"La voz suave de Lilly se dirige hacia nosotros dos mientras sigue jugando."

show tearoom_lillye smile
with charachange

li "¿Cómo les fue en las clases, ya que se ha acabado el festival?"

show tearoom_hanae shy
show tearoom_hisaoe hthink
with charachange

"Miro a Hanako para ver si responderá ella primero, pero veo que ella está haciendo lo mismo."

show tearoom_hisaoe sigh
with charachange

hi "No… muy bien. La mitad del grupo parecía estar dormitando, incluso el maestro. Sin mencionar que además hubo un examen."

show tearoom_hanae happy
with charachange

"Hanako concuerda con esto en voz baja."

show tearoom_lillye ara
with charachange

li "Puedo imaginarme que eso sea un tanto difícil para ti, siendo un estudiante de transferencia."

show tearoom_hisaoe lsmile
with charachange

hi "Bueno, creo que me fue bien. Aparte del impacto de tener una prueba tan pronto, ciencias probablemente es mi mejor materia."

show tearoom_hisaoe hsmile
with charachange

hi "¿Cómo te fue a ti, Hanako?"

show tearoom_hanae open
with charachange

ha "¿A mí? Ah… bien… Supongo…"

"Hanako es demasiado sincera como para ser capaz de mentir muy bien. Al menos eso es obvio."

show tearoom_lillye thinking
with charachange

"La sonrisa de Lilly cae muy levemente. Por su reacción, Hanako no debe ser lo bastante hábil en lo académico como para que le vaya bien sin preparación."

show tearoom_hisaoe lsmile
with charachange

hi "¿Cómo lo manejó tu grupo, Lilly?"

show tearoom_lillye giggle
with charachange

li "De hecho, nos fue sorprendentemente bien. Solo faltó un estudiante, así que fue mejor de lo que esperaba la maestra."

show tearoom_hanae shy
show tearoom_lillye smileclosed
with charachange

"Con el tema prácticamente agotado, las dos se concentran una vez más en su partida de ajedrez."

show tearoom_hisaoe relief
with charachange

"No puedo decir que alguna vez me haya gustado la idea del ajedrez como un deporte espectáculo, pero dada su naturaleza única, esta vez estoy cautivado viendo cómo se desarrolla el juego."

show tearoom_hisaoe outside
show tearoom_hanae sad
with shorttimeskip

"Mientras pasa el tiempo, ambas demuestran habilidad decente para jugar. Habiendo capturado dos peones más que Hanako, Lilly tiene la delantera, pero solo por un poco."

show tearoom_hanae open
show tearoom_hisaoe hunsure
with charachange

"… Hasta que Hanako hace una jugada extraña con su reina. Aprovechando este lapsus de juicio, Lilly captura la pieza con su caballo."

show tearoom_hanae shy
with charachange

"Sin dudarlo, Hanako mueve un peón para capturar la torre de Lilly en el lado opuesto del tablero, y lo promueve a reina."

show tearoom_lillye thinking
show tearoom_hisaoe lunsure
with charachange

"El rostro de Lilly flaquea mientras sus dedos se mueven sobre las piezas y se da cuenta de que acaba de caer en la trampa de Hanako. Es un tanto distractor el tener que trazar el tablero después de cada jugada, aunque sea por necesidad."

"A juzgar por la ausencia de reacción de Hanako, ella debe estar acostumbrada a esto. Ella y Lilly deben haber jugado al menos unas cuantas partidas entre ellas, después de todo."

ha "Jaque."

show tearoom_hisaoe hsmile
with charachange

hi "Eso no está para nada mal. Bien, Hanako."

show tearoom_hanae happy
with charachange

"El cumplido hace que su rostro florezca con un rubor sorprendido."

ha "G-gracias. Yo no… creí que fuera a funcionar."

show tearoom_hisaoe lsmile
with charachange

"Miro a Lilly, sus dedos recién acabando de trazar la posición de sus piezas restantes en un intento por sacar a su rey de este aprieto."

li "Creo que es jaque mate…"

show tearoom_hisaoe loops
with charachange

hi "¿Hmm?"

show tearoom_hisaoe relief
with charachange

"Echo otra mirada al tablero para confirmarlo."

"Efectivamente, su rey no tiene adónde escaparse sin verse amenazado por otra pieza. Mi pregunta de antes sobre cuál de las dos es mejor en esto acaba de ser respondida."

show tearoom_hisaoe sigh
with charachange

hi "Así es."

show tearoom_lillye weaksmile
with charachange

"Lilly suelta un ligero suspiro mientras Hanako sonríe. Por sus reacciones, esto parece un resultado bastante usual."

show tearoom_hisaoe lsmile
with charachange

hi "¿Cuánto tiempo llevan jugando?"

show tearoom_hisaoe hsmile
show tearoom_hanae sad

with charachange

ha "Desde… que era pequeña."

show tearoom_lillye smileclosed
show tearoom_hisaoe lsmile
with charachange

"Lilly asiente a la breve respuesta de Hanako."

show tearoom_lillye smile
with charachange

li "Hanako me enseñó a jugar poco después de conocerla. La puedo derrotar de vez en cuando… pero eso es una rareza. Tal parece que no tengo la mentalidad correcta para ello."

"Si Lilly vino a Yamaku al inicio de la preparatoria, y conoció a Hanako cuando se mudó a los dormitorios, eso significa que solamente ha jugado por un año."

"Después de ver el nivel de juego de Hanako, no me sorprende mucho que Lilly tenga problemas derrotándola."

show tearoom_hanae happy
show tearoom_hisaoe hthink
with charachange

ha "Pero… ella es mejor con los idiomas que yo, así que…"

show tearoom_lillye ara
show tearoom_hisaoe lthink
with charachange

"Lilly suelta una sonrisa apreciativa, si bien un tanto divertida, por la rápida inversión que Hanako hizo de su cumplido."

show tearoom_lillye weaksmile
with charachange

li "Bueno, así es."

stop music fadeout 3.0
play sound sfx_warningbell

"Para la sorpresa de todos, la campana suena de repente, anunciando el final de la hora del almuerzo."

show tearoom_lillye thinking
show tearoom_hisaoe loops
with charachange

li "Hmm, esa partida duró más de lo que pensé."

hi "Sí. Creo que es mejor que volvamos a clase."

show tearoom_hanae shy
show tearoom_lillye weaksmile
show tearoom_hisaoe thinkclosed
with charachange

"Hanako ya está guardando todo, así que tomo el bolso de Lilly y se lo ofrezco. Para mi sorpresa, ella lo recibe y asiente, pero luego lo coloca de vuelta en la mesa."

play music music_daily fadein 2.0

scene bg school_miyagi
show lilly basic_smileclosed at twoleft
show hanako basic_normal at tworight
with locationskip

li "Hisao, ¿puedo pedir algo?"

hi "Claro, adelante."

show lilly basic_smile at twoleft
with charachange

li "¿Te molestaría si yo palpara brevemente tu rostro?"

hi "Oh, eh… no, adelante. No me molesta."

"La pregunta me toma gravemente por sorpresa, pero ya que recupero mi compostura, parece lo bastante razonable. Hasta ahora Lilly no tiene ninguna idea de cómo me veo, y esta sería su única forma de descubrirlo."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

show ev lilly_touch_uni
with GenericWhiteout(0.5,0.1,3.0)

"Lilly levanta su mano derecha, la cual tomo con la mía y la guío a mi rostro antes de soltarla."

"El cuarto queda completamente en silencio mientras la mano de Lilly se mueve y recorre mis facciones, desde mi mentón, a mis mejillas, hasta todo lo demás."

"Esperaba que esto se sintiera mucho más inquietante de lo que se siente. Supongo que es debido a que la acción es por completo un asunto de practicidad, siendo funcionalmente igual que mirar el rostro de alguien."

"Su mano es suave, pero lo que me toma por sorpresa es el largo de sus dedos, sin mencionar lo seguros que son hasta los más ligeros de sus movimientos. No tengo duda de que su nivel de sensación táctil es mucho mejor que el mío."

"Su mano recorre brevemente mi cabello una vez antes de retirarse. Me imagino que cada centímetro de mi rostro ha sido guardada en su memoria. Y es ahora también que me doy cuenta de que Hanako ha estado observando en silencio todo el tiempo."

$ renpy.music.set_volume(1.0, 2.0, channel="music")

scene bg school_miyagi
show hanako basic_distant at tworight
show lilly basic_weaksmile_close at twoleft
with whiteout

li "Gracias por dejarme hacer eso, Hisao."

show lilly basic_smile_close at twoleft
with charachange

li "Y si debo añadir, creo que eres bastante apuesto."

"Me sonrojo un poco por su comentario, antes de levantar una ceja de forma inquisitiva."

hi "Pero si no puedes ver, ¿cómo…?"

show lilly basic_pout_close at twoleft
with charachange

li "Solo porque no pueda ver, no significa que no tenga mis preferencias."

show hanako emb_timid at tworight
with charachange

ha "Ahh, ya deberíamos irnos…"

hi "Cierto, tienes razón. Entonces creo que nos veremos luego, Lilly."

scene bg school_hallway2
show lilly basic_smile at twoleft
show hanako emb_smile at tworight
with locationskip

"Caminando por los pasillos de vuelta a nuestros propios salones, noto que Hanako parece más callada que antes, pero también más cómoda."

"Lilly, con su mano en el hombro de Hanako, también parece darse cuenta de su paso seguro, sonriendo mientras caminan."

"Si pudiera pasar el resto de mi tiempo en Yamaku de esta forma, no creo que sería tan malo. Todo lo que se necesita para estar alegre son pequeños intercambios de felicidad, después de todo."

scene bg school_scienceroom
with locationskip

play sound sfx_rumble

"Cuando llego a mi banco y dejo mi bolso junto a él, me doy cuenta de algo. O mejor dicho, mi estómago lo hace."

"Estuve tan ocupado con ellas dos, que se me olvidó comprar almuerzo…"

stop music fadeout 2.0

scene black
with dissolve



label es_L2:

scene bg school_dormhisao
with locationchange

"Sábado. Mi segundo día favorito de la semana."

"Esto se debe casi completamente al hecho de que es el segundo día con menos clases, ya que terminan al comienzo del almuerzo."

scene bg school_dormhallway
with locationchange

"Abro mi puerta con confianza, estando yo mismo más que confiado de ser capaz de disfrutar del buen clima y el periodo más corto de clases."

scene bg school_dormhallground
with locationchange

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_footsteps_hard

"Avanzo con confianza por el pasillo y bajo las escaleras que dan al vestíbulo de los dormitorios para varones."

$ renpy.music.set_volume(0.6, 4.0, channel="ambient")

"Miro con confianza detrás mío para ver a quién pertenecen los pasos que se acercan."

$ renpy.music.set_volume(1.0, 4.0, channel="ambient")

"Y… pierdo mi confianza en que este día sea agradable."

stop ambient
play music music_kenji fadein 0.5

show kenji happy:
    center
    xpos 0.4
    easein 0.5 xpos 0.5
with charaenter

ke "Oye hombre. ¿Qué va?"

hi "No mucho supongo, nada más esperando que llegue la tarde. ¿Tú?"

show kenji happy_close at center
with characlose

"Él rodea mis hombros caídos con su brazo demasiado cómodamente. Algo pasa."

show kenji neutral_close
with charachange

ke "Vayamos afuera, ¿te parece?"

hi "En eso estaba, antes de que me detuvieras."

show kenji tsun_close
with charachange

scene bg school_dormext_full
with locationchange

"Él no toma bien mi reacción a su teatralidad. Ignorándolo, camino hacia afuera y empiezo a bajar los peldaños."

"No le toma mucho tiempo alcanzarme otra vez. Me pregunto si quiere dinero, o vociferar sobre otra conspiración. Quizás ambas."

show kenji tsun:
    center
    xpos 0.6
    easein 0.5 xpos 0.5
with charaenter

ke "Tengo unas cuentas pendientes contigo."

hi "Ajá."

ke "Es con respecto a esa rubia. Tú sabes de quién hablo."

"Una conspiración, entonces. Por un momento considero fingir ignorancia, pero me doy cuenta de que esto acabará más rápido si simplemente dejo que lo suelte todo."

hi "¿Lilly? ¿La que está en tu grupo?"

show kenji rage at center
with vpunch

ke "¡¿Ya la llamas por su nombre?!"

"Él parece verdaderamente impactado por este desarrollo. ¿No esperaba que fuera capaz de responder?"

show kenji tsun
with charachange

"Recupera su compostura y tose en su puño. Dramáticamente, como todo lo que hace."

ke "Bueno, no importa eso. Estoy aquí para advertirte. Tú sabes. De hombre a hombre."

hi "¿Advertirme sobre qué? ¿Lilly?"

ke "Claro. Tú no la conoces, hombre."

"Eso es más o menos cierto. Solo las conozco a ella y a Hanako desde hace menos de dos semanas, e incluso así solamente hemos platicado superficialmente sobre la escuela mientras pasamos el almuerzo."

hi "Estoy bastante seguro de que tú tampoco."

ke "Ese no es el punto. Tú eres el que está pasando cantidades excesivas de tiempo con ella."

"Me angustia que alguien como Kenji, quien probablemente esté tan desinformado como se pueda estar, sepa sobre un hecho tan trivial como con quién elijo tener una amistad."

"Por otra parte… Soy un estudiante de transferencia, y ella no solo es la representante de su clase, sino también una rubia alta."

"Quizás debería apreciar este sermón como una advertencia de que la fábrica de rumores también existe en esta escuela, y que estoy inmerso firmemente dentro de ella."

hi "Es solo el almuerzo. Nada especial."

show kenji neutral
with charachange

ke "Mira, hombre, bajo el puente. ¿Ves este puente? Tú estás bajo él. Un hombre tiene que hacer lo que un hombre tiene que hacer para obtener información."

show kenji tsun
with charachange

ke "Solo quiero asegurarme de que no acabes demasiado debajo del puente."

hi "Me estás perdiendo, Kenji."

show kenji happy
with charachange

ke "Está bien, muchas personas se pierden. Es por eso que estoy aquí para ayudar."

scene bg school_gardens
show kenji neutral
with locationskip

ke "Solo ten cuidado con ella, ¿vale? Ella parece inofensiva por el exterior, pero he escuchado mierda. Mierda grave."

show kenji tsun
with charachange

ke "Conoces al consejo estudiantil, ¿cierto?"

"Parece estremecerse involuntariamente al decir esas palabras. Tenerlos a él y a Shizune juntos en un cuarto es un ejercicio mental entretenido. Me pregunto si se conocerán."

hi "Claro, Shizune y Misha están en mi grupo. Aunque creo que evadí ser reclutado."

show kenji happy
with charachange

ke "Buen hombre. Buen hombre."

show kenji tsun
with charachange

ke "¿Pero y esta rubia? Ella estaba ahí. En el consejo estudiantil. Justo. En. Ello."

hi "Ya veo. ¿Y?"

ke "Y ahora ella no está ahí."

stop music fadeout 3.0

hi "…"

ke "En serio, piénsalo. Algo habrá pasado."

"Dejo de caminar por un momento, pensando más detenidamente de lo que debería en la idea."

"Eso explicaría la pelea que ellas tuvieron, al menos en parte. Espera, no, en realidad no. Hasta abandonar el consejo estudiantil requeriría un catalizador."

"En fin, no explica mucho en absoluto. Aparte del hecho de que su riña tiene ya un tiempo."

hi "Supongo que tienes razón. Aunque no veo cómo eso realmente me afecta a mí."

show kenji neutral
with charachange

ke "Bueno, ahora contesta esta. Lilly es extranjera, obviamente."

hi "Obviamente."

ke "Ahora bien, ¿qué nacionalidad tiene?"

"Abro mi boca para dar una respuesta, pero me doy cuenta de que no tengo ninguna. De hecho, no he pensado mucho en el tema."

"Dado que no tiene acento y actúa perfectamente como japonesa, supongo que nunca me ha parecido realmente importante. Aunque ahora que lo menciona, siento algo de curiosidad."

hi "Para serte sincero, no lo sé. ¿Quizás inglesa? A ellos les gusta el té."

"Probablemente no debería recurrir a estereotipos, pero esa es la única pista que tengo."

show kenji happy
with charachange

play music music_kenji fadein 1.0

ke "No estás pensando. Por suerte, me tienes aquí para pensar por ti."

hi "Caray, gracias."

"Él ignora la gracia sin problemas."

show kenji neutral
with charachange

ke "Ahora respóndeme esto: ¿Quién tiene muchísimo poder social, es asquerosamente rica —tú sabes que las rubias son todas ricas, ¿cierto?— tiene una larga historia de disputas y solía pertenecer a una organización más grande?"

hi "¿La Santa Iglesia Católica Romana?"

show kenji tsun
with charachange

ke "… Bueno, sí, está esa."

show kenji neutral
with charachange

ke "Pero también está la Mafia. Vamos. Rica, extranjera, no hay forma de que no tenga conexiones con ellos."

"Tengo motivos para dudar de la lógica de sus deducciones, pero él no parece estar listo para detenerse."

scene bg school_hallway3
show kenji neutral
with locationskip

ke "¿Entonces sabes de dónde creo que es?"

hi "¿Italia?"

show kenji tsun
with charachange

ke "La Italia continental es de poca monta, hombre. Ella tiene que ser de Sicilia. Todos esos mafiosos vienen de ahí."

show kenji happy
with charachange

ke "Espera, no, Rusia. Maldición, esto podría ser malo. La Mafia ahí es algo serio, hombre; Ex-KGB por todas partes, paramilitares, contrabando en serio, y—"

hi "Espera, espera, detente, tan solo cálmate un segundo. ¿A qué estás tratando de llegar con esto?"

show kenji neutral
with charachange

ke "No sabes qué es lo que hará, hombre. No me interpondré en tu camino —los agentes no operamos así— pero simplemente quiero que tengas cuidado."

show kenji tsun
with charachange

ke "Cuando llegue el momento, necesitaremos toda la ayuda que haya. No quiero perderte, camarada."

"Bueno, por lo menos se preocupa por mí. Algo así."

stop music fadeout 4.0

show kenji tsun:
    center
    easeout 0.5 xpos 0.6 alpha 0.0
with None

"Me despido de él mientras vamos hacia nuestras respectivas clases, pero no estoy seguro de que vea el gesto."

scene bg school_scienceroom
with shorttimeskip

play ambient sfx_crowd_indoors fadein 2.0

"Apilando mis libros en mi bolso, veo brevemente los libros de la biblioteca que pedí prestados la semana pasada. A lo mejor los devuelvo, ya que me tardé solo dos días en terminarlos."

"Por un momento, considero invitar a Hanako a la biblioteca, pero ella ya se ha ido. De todas formas probablemente sea mejor para mis estudios si estoy solo."

"Estirándome brevemente y despidiéndome con un gesto de un par de compañeros que me responden de la misma forma, me abro paso para salir del salón."

stop ambient fadeout 1.0

scene bg school_library
with locationskip

"Cuando abro mi mochila y arrojo los libros por el buzón de devoluciones en el mostrador frontal, noto a una persona extraña detrás del escritorio. Vieja y canosa, ella debe de ser el reemplazo de Yuuko cuando le toca trabajar en el café."

"Comienzo a buscar una mesa disponible, una tarea un poco difícil dado que, a pesar de no haber muchos estudiantes por aquí, todos están sentados en sus propias mesas."

"Noto una mata de cabello conocido, y camino hacia una que está cerca de la sección de braille."

show lilly basic_smileclosed
with charaenter

"Es difícil distinguir si Lilly se está concentrando mucho o no, su expresión relajada manteniéndose perfectamente quieta mientras sus dedos recorren las páginas repletas de puntos del libro."

hi "Hola. ¿Te importa si me siento aquí?"

show lilly basic_surprised
with charachange

li "¿Hmm? Oh, no me importa en absoluto…"

"Sus palabras van apagándose, evidentemente aún concentrada en sus asuntos."

play music music_lilly fadein 10.0

show lilly basic_smile
with charachange

li "Ah, Hisao."

show lilly basic_smileclosed
with charachange

"Ella saluda asintiendo mientras yo me siento opuesto a ella en la mesa, tomo un libro de química de mi mochila y rápidamente salto al capítulo que estamos viendo en clase."

"Por un rato, nos sentamos ahí y leemos, cada uno a su manera."

"Sin embargo, verla me recuerda a lo que dijo Kenji esta mañana. Eso y el hecho de que yo nunca antes había visto a alguien leer en braille me hacen seguir lanzando miradas hacia ella."

"Me siento un poco culpable al respecto, dado que ella no tiene forma de darse cuenta de lo que estoy haciendo, así que decido simplemente preguntarle al respecto."

"Su lineaje no es exactamente un secreto de estado, después de todo, y hay otra cosa que acabo de notar por sus movimientos."

hi "Oye, Lilly, ¿te importa si te hago una pregunta?"

show lilly basic_smile
with charachange

li "Para nada. ¿Pasa algo?"

hi "Solo me preguntaba… eres por lo menos en parte extranjera, ¿cierto?"

show lilly basic_giggle
with charachange

"Ella suelta una risita antes de bajar su libro."

show lilly basic_cheerful
with charachange

li "Siempre me ha divertido lo aprensiva que es la gente con respecto a eso. Akira mencionó antes cuán diferentes ella y yo somos del resto."

show lilly basic_smile
with charachange

li "Los detalles son un poco complicados, pero soy mitad japonesa, mitad escocesa."

"… ¿Escocesa? Esa no fue exactamente mi primera suposición. Me cuesta un poco no soltarlo en voz alta."

"Intento conjurar imágenes del lugar en mi mente. Creo que en lo que respecta al Reino Unido, Escocia no es un mal lugar para vivir… pero en realidad no estoy seguro."

"Mi primera suposición de Inglaterra estaba sorprendentemente acercada, al menos geográficamente. Aunque eso deja otra pregunta."

hi "Pero tú no tienes acento…"

show lilly basic_weaksmile
with charachange

li "Ahí es donde comienzan los detalles. Nací y fui criada en Japón, a pesar de que mi madre fuera extranjera."

hi "Ah, lo entiendo."

"Un momento, si ella se mudó a los dormitorios solamente porque Akira comenzó a trabajar más horas…"

hi "¿Entonces no viven cerca de la escuela?"

show lilly basic_reminisce
with charachange

"Ella suelta un ligero suspiro, como si no esperara que siguiera más allá. ¿Su franqueza anterior era nada más que una fachada?"

li "No… exactamente. Ha pasado mucho tiempo desde que nos vimos."

"Siento que no conozco la historia completa, pero en realidad no quiero inmiscuirme excesivamente en su situación. Su cambio de actitud demuestra que se siente un poco incómoda al respecto."

hi "Entonces… ¿hablas mucho inglés? Para serte honesto no sé mucho sobre Escocia, pero al menos sé que ese es el idioma principal allá."

"Se tarda un momento en recuperar su compostura, apreciando el cambio de tema."

show lilly basic_smileclosed
with charachange

li "Así es. Mi familia usaba principalmente japonés en casa cuando era joven, pero se aseguraron de que Akira y yo conociéramos nuestro lado escocés también."

show lilly basic_smile
with charachange

li "Domino el idioma, pero también estoy estudiándolo en la escuela. Para mantener mis habilidades y para tener los requisitos en papel, principalmente."

hi "¿Entonces eres bilingüe? Eso es bastante impresionante."

show lilly basic_weaksmile
with charachange

li "Yo no diría tanto. Tener padres que puedan hablar el idioma es una gran ventaja, y los libros en inglés de braille no son tan difíciles de comprar o importar. Con la ayuda de Yuuko, al menos."

show lilly basic_smileclosed
with charachange

li "De todas maneras aquí hay una demanda relativamente alta de maestros locales de inglés, lo que también me sirve como motivación para aprender."

"¿Demanda de maestros de inglés? Por un momento, me pregunto por qué mencionó esto."

hi "¿Planeas ser maestra de inglés?"

show lilly basic_cheerful
with charachange

"Ella asiente de manera entusiasta."

"Debe ser bueno, tener un futuro tan definido en mente. Nunca he pensado mucho en el mío, así que siento un poco de envidia."

hi "Hmm…"

show lilly basic_smile
with charachange

li "¿Qué pasó?"

hi "Es solo… Puedo verte fácilmente como maestra. Te queda bien."

show lilly basic_emb
with charachange

"Por un momento, ella queda sin palabras. Baja su rostro un poco y suelta una risita nerviosa, algo que nunca la he visto hacer antes."

"Con el rol de Lilly como representante de clase y su naturaleza confiable, la docencia parece ser el campo de trabajo apropiado para su personalidad."

hi "Lo siento, quizás dije algo de más. De todas formas, es la verdad."

show lilly basic_weaksmile
with charachange

"Moviendo su mano frente a su rostro como si no tuviera importancia, se recupera rápidamente."

li "No es eso, es solo que… solo una persona me ha dicho eso antes."

stop music fadeout 8.0

"Un silencio breve e incómodo sigue a la discusión. Sin darme cuenta, terminé llegando de nuevo a un tema problemático."

"Debería intentar animarla un poco. Fui yo quien la puso melancólica, después de todo."

hi "¿Quieres ir a almorzar a la cafetería después de esto?"

"Podría animarla un poco, o al menos distraer su mente de su aparentemente complicada situación familiar."

show lilly basic_planned
with charachange

"A juzgar por su sonrisa, parece haber tenido el efecto deseado."

show lilly basic_ara
with charachange

li "Agradezco el gesto, pero la comida ahí…"

"Vaya cambio en la dirección de la conversación. Aunque tiene razón, la comida ahí no es la mejor."

hi "¿Quizás el Shanghái? Podríamos preguntarle a Hanako si quiere venir también."

show lilly basic_surprised
with charachange

li "Ah…"

hi "¿Qué pasó?"

show lilly basic_weaksmile
with charachange

li "Casi se me olvidó, hasta que me lo recordaste. El cumpleaños de Hanako viene pronto, y mañana pensaba ir de compras en la ciudad para buscarle un regalo."

hi "Si eso es una invitación, me encantaría acompañarte."

"La oportunidad de poder acostumbrarme más al trazado de la ciudad probablemente sea útil. Apenas he puesto un pie ese lugar, así que por mi cuenta estaría irremediablemente perdido."

show lilly basic_smile
with charachange

"Ella asiente, señalando que acepta felizmente este plan para el domingo."

"Eventualmente seguimos con nuestros libros, aunque antes de comenzar a leer otra vez doy un último vistazo hacia a ella."

"Quizás he estado pensando demasiado en mi propia situación. Después de todo, aquí todos deben de tener sus propias circunstancias únicas."

"La oportunidad de salir y despejar mi cabeza probablemente me haga bien."

scene black
with dissolve



label es_L3:

play ambient sfx_traffic fadein 10.0

scene black
with None

scene bg city_street1 at Fullpan(16.0, "left")
with locationchange

"Aburrido de estar parado en un lugar y mirar la televisión en la vitrina de una tienda, me aparto de la vulgar pantalla sin mucho esfuerzo."

"Después de vivir en Yamaku, la ciudad parece un mundo completamente distinto."

"Nadie corre por los pasillos. Uno se debe de comportar de forma tranquila y ordenada en todo momento en los salones. Los estudiantes deben salir de los cuartos luego de verificar en ambas direcciones si se aproxima alguien."

"Los ascensores están reservados para los alumnos con dificultades de movimiento. Una sola fila en las escaleras."

"Comparado con esos estándares tan estrictos, casi de regimiento, la galería comercial de la ciudad bien podría ser un país extraño."

"Aunque la escuela puede tener su parte de barullo durante el festival, el mundo exterior es muy diferente."

"Es extraño. Habiendo vivido en una ciudad metropolitana antes de mi accidente, esto debería sentirse más natural de lo que Yamaku y el pueblo circundante podrían."

"Sin embargo, se siente extraño, de algún modo. Las pasarelas elevadas y edificios, cada uno adornado con carteleras más altas que tres personas, no hacen mucho para distraerme de las reacciones de la multitud circundante."

$ renpy.music.set_volume(0.7, 0.5, channel="ambient")

show lilly cane_smileclosed_cas_close:
    center
    xpos 0.2
    easein 1.0 twoleft
show bg city_street1 at left
with Dissolve(1.0)

"Lilly mantiene una mano sobre mi hombro, la otra sosteniendo su bastón que golpetea el suelo con la regularidad de un metrónomo. Cuando la miro, veo que esa sonrisa neutral suya aún permanece."

"Habiéndola visto solamente en su uniforme escolar, no la habría reconocido cuando estaba sentada en una banca esperándome, si no fuera por su bastón apoyado contra la banca y su cabello distintivo."

"No puedo distinguir si la están mirando de reojo debido a su altura, su apariencia de extranjera, su evidente ceguera, o las tres. Ninguna de esas haría la situación menos incómoda de lo que es."

show lilly cane_smile_cas_close
with charachange

li "¿Tienes alguna idea de dónde buscar primero, Hisao?"

"Su voz suave me hace perder el hilo de lo que pensaba."

"No puedo imaginarme que ella no logre notar la atención que está consiguiendo, pero parece permanecer impávida. Tengo la sensación de que ella es del tipo que disfruta caminar afuera, así que puede que a estas alturas ya esté acostumbrada."

hi "No en realidad. Es mi primera vez en esta ciudad, así que no tengo idea de dónde ir."

show lilly cane_listen_cas_close
with charachange

"Ella frunce el ceño pensativa, planeando una ruta que podamos tomar. Y, ahora que lo pienso, una manera de comunicarla."

"Algo que he notado en el tiempo que he estado con ella es cómo, cuando ella se encuentra abstraída en sus pensamientos, carece de casi cualquier forma de lenguaje corporal para demostrarlo."

"Su expresión cambia, pero no hay ningún rastro de movimiento. Aunque ella parece en general no tener mucho en lo que respecta a gestos físicos dramáticos, así que he asumido que es parte de su naturaleza reservada."

show lilly cane_weaksmile_cas_close
with charachange

li "¿Hay una tienda grande de artículos electrónicos cerca de aquí?"

"Miro rápidamente alrededor, encontrando principalmente tiendas de ropa. Después de unos cuantos segundos noto una tienda con un letrero azul brillante algo lejos que satisface su descripción."

hi "Síp, está un poco más adelante. ¿Vamos hacia allá?"

show lilly cane_smile_cas_close
with charachange

"Por suerte, es justo la información que ella necesitaba. Al asentir ella, comenzamos a caminar y nos dirigimos hacia el destino desconocido de Lilly, guiados por puntos de referencia."

stop ambient fadeout 2.0

scene ev icecream
with shorttimeskip

play music music_happiness fadein 2.0

"Dueño del negocio" "Aquí tienen. Uno de vainilla, uno de chocolate."

scene bg city_street2 at center
with locationchange

"Entrego el dinero sobre el mostrador y llevo los conos al barandal en el que se encuentra sentada Lilly."

"No puedo creer que la haya dejado engañarme así. Ella no solo me condujo a un puesto de helados, sino también me hizo comprarle uno. Por lo menos me dio el dinero para el suyo."

show lilly cane_smileclosed_cas at Transform(xanchor=0.5, xpos=0.2, ypos=0.2, yanchor=0.0)
with charaenter

"Como suponía, ella está ahí esperando pacientemente donde la dejé. Supongo que estaba planeando hacer del día un evento en lugar de un simple viaje de compras."

show lilly cane_smileclosed_cas:
    ease 1.0 xpos 0.5 xanchor 0.5 ypos 0.15
show bg city_street2:
    ease 1.0 left
with None

show lilly basic_satisfied_cas_close:
    xanchor 0.5 xpos 0.2 ypos 0.2 yanchor 0.0
    ease 1.0 xpos 0.5 xanchor 0.5 ypos 0.15
show bg city_street2:
    ease 1.0 left
with Dissolve(1.0)

"La llamo y lentamente coloco el cono de vainilla en sus manos extendidas, teniendo cuidado de asegurarme de que lo haya tomado firmemente antes de soltarlo."

"Por lo menos sus gustos son bastante normales. Me preocupaba que pidiera algún sabor raro cuando me preguntó."

hi "Aquí está el cambio."

show lilly basic_smileclosed_cas_close at Transform(xalign=0.5, ypos=0.15)
with charachange

li "Está bien, quédatelo."

"Estoy por quejarme, pero me doy cuenta de la inutilidad de hacer eso por tan poca cantidad. Guardo la moneda en mi bolsillo, complementando mi escasa mesada aunque sea por poco."

show lilly basic_smileclosed_cas_close
with charachange

"Lilly no parece querer levantarse, así que me siento junto a ella y comienzo a comerme mi propio helado."

hi "El clima de verano es agradable. Con algo de suerte seguirá así por un tiempo."

show lilly basic_weaksmile_cas_close
with charachange

li "¿Tú también? Estoy empezando a pensar que soy la única persona que prefiere el invierno."

"Contemplo su afirmación un largo rato."

hi "Sí, puede que sí."

show lilly basic_pout_cas_close
with charachange

"Logro la reacción deseada. Ella es linda cuando hace pucheros."

hi "Aun así, en realidad no puedo imaginarme qué hay de bueno en el invierno. No puedes salir sin abrigarte, y te congelas de todas formas."

show lilly basic_reminisce_cas_close
with charachange

li "Antes vivía más al norte, donde había mucha nieve en qué jugar, así que es un tanto nostálgico. Tampoco me gusta mucho el calor."

hi "Al menos puedes usar una falda, así que no te quejes por eso."

show lilly basic_giggle_cas_close
with charachange

"Ella suelta una risita divertida mientras ambos seguimos terminando nuestros conos de helado ya derretidos."

play ambient sfx_crowd_outdoors fadein 2.0

hide lilly
show crowd at left
with shorttimeskip

"Me siento ociosamente y miro la multitud pasar mientras comemos, escuchando fragmentos de conversación."

show lilly basic_satisfied_cas_close at Transform(xalign=0.5, ypos=0.15)
with charaenter

"Mirando a Lilly, puedo verla lamiendo diligentemente su helado desde la punta hacia abajo, felizmente inconsciente del hecho de que se ha comenzado a derretir."

hi "Se está derritiendo."

show lilly basic_surprised_cas_close
with charachange

li "¿Dónde?"

hi "Um… ¿un poco más abajo?"

show lilly basic_listen_cas_close
with charachange

"Ella baja su boca de la parte superior del cono, pero no tiene idea de dónde exactamente está goteando el helado. Lo que sigue es un juego de guiarla a la izquierda y a la derecha hasta que finalmente lo encuentra."

"Para cualquier espectador, debe parecer totalmente extraño, una chica con sus ojos cerrados girando su cono una y otra vez mientras el chico a su lado da instrucciones."

"Quizás una variante extraña de los juegos infantiles con los ojos vendados."

show lilly basic_smileclosed_cas_close
with shorttimeskip

"Al fin terminamos nuestros helados, y dejamos pasar el tiempo conversando casualmente."

stop music fadeout 3.0

show lilly back_listen_cas_close
with charachange

"En medio de una oración, Lilly levanta su cabeza en su forma típica. Es una señal inconfundible de que algo ha llamado su atención."

show lilly back_smileclosed_cas_close
with charachange

li "Ah…"

hi "¿Qué pasó?"

show lilly back_smile_cas_close
with charachange

li "¿Akira está por allá? Creo que la escuché."

show lilly back_smile_cas_close at Transform(xpos=0.25)
show crowd:
    bgright
    xpos 0.55
show bg city_street2:
    bgright
    xpos 0.55
with dissolvecharamove




"Levanto una ceja mientras miro en la dirección en la que ella apunta, algo dudoso de su habilidad de distinguir la voz solitaria de Akira entre el barullo."

show akira basic_boo behind crowd:
    tworight
    xpos 0.78 ypos 1.13
with charaenter

"Pero en efecto, se puede ver una chica rubia vestida de traje a través de los pequeños huecos entre las personas caminando en cualquier dirección."

"Levanto una mano y la agito, intentando llamar su atención."

hi "¡Satou! ¡Oye, Satou!"

show akira basic_smile
with charachange

"Ella se detiene completamente y mira hacia mí, evidentemente notando mis llamados. Al mismo tiempo, noto que alguien está caminando junto a ella."

"No logro ver bien quién es la persona desconocida, pero ya ambos han empezado a caminar hacia nosotros."

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")
play music music_ease fadein 4.0

show akira basic_smile:
    ease 1.0 ypos 1.0 alpha 0.0
with None

show akira basic_smile as akira2 behind lilly:
    tworight
    xpos 0.78 ypos 1.13 alpha 0.0
    ease 1.0 ypos 1.0 alpha 1.0
with Pause(1.0)

hide akira
with None

show lilly back_smile_cas_close at Transform(yalign=1.0)
with charamove

"Cuando se acercan, Lilly y yo nos paramos y nos sacudimos el polvo."

show lilly back_giggle_cas_close
with charachange

li "¿Akira?"

hide akira2
show akira basic_laugh behind lilly:
    tworight
    xpos 0.78 ypos 1.0
with charachange

aki "Buenas, ustedes dos."

show lilly back_giggle_cas_close at Transform(xpos=0.1)
show akira basic_smile at Transform(xanchor=0.5, xpos=0.6)
show crowd at center
show bg city_street2 at center
with dissolvecharamove

show hideaki bored at right behind akira
with charaenter

"Ella asiente hacia mí, un gesto que respondo rápidamente. Mi mirada se vuelve hacia la joven chica junto a ella, y nuestros ojos se encuentran. Al mismo instante, Akira deja caer su mano sobre su cabeza, un movimiento que no parece perturbarla."

show hideaki normal
with charachange

hh "No creo que nos conozcamos. Soy Hideaki. Encantado de conocerte, Hisao."

"¿Nombre de hombre, eh? Creo que acabo de evitar meter la pata. Él hace una reverencia, un tanto refrenado por la mano de Akira sobre su cabeza."

show lilly basic_smileclosed_cas_close at Transform(xpos=0.18)
with charachange

li "Oh, ¿Hideaki también está aquí? ¿Todo bien?"

show hideaki thinking
with charachange

hh "Akira ha estado cuidando bien de mí, gracias."

show akira basic_laugh
show hideaki sad
with charachange

"Akira sonríe como para aseverar el punto y frota fuerte la cabeza del niño, arrastrándola en un movimiento circular. Su rostro sombrío durante esto es un poco gracioso."

show akira basic_smile
with charachange

aki "El tío volvió a salir de negocios, así que por hoy nada más lo traje a la ciudad."

show akira basic_boo
with charachange

aki "Hubiera preferido pasar el día en una cita con mi novio, pero…"

show hideaki closed_up
with charachange

"Hideaki tose para intentar redirigir los pensamientos de Akira."

"Pero, cuando lo hace, encuentro que los míos divagan. ¿Son parientes? Y más aún, ¿primos? Supongo que eso explica por qué se está haciendo cargo de él, de todos modos."

hi "Ahora que lo pienso, Hideaki, ¿cómo sabías mi nombre?"

show hideaki serious
with charachange

hh "Akira me lo dijo. Por ser estudiante de Yamaku, ¿supongo que tienes alguna discapacidad?"

hi "No todos en Yamaku son discapacitados…"

"Lo cual solo aprendí hace algunos días. Les agradezco en silencio a Shizune y a Misha por su torrente de información sobre cómo funciona la escuela."

"Gracias a ellas, descubrí que ya que la escuela acepta a prácticamente cualquier persona que sufra de discapacidades no mentales, tampoco discrimina a personas sanas."

"Sin embargo, parece improbable que muchas personas de buena salud se matriculen ahí. Aunque el estándar de educación es bastante alto, está extremadamente apartado y muy enfocado en ayudar a los estudiantes discapacitados."

show hideaki angry_up
with charachange

hh "Estás evadiendo la pregunta."

"Maldición, es agudo."

"De todas formas, antes de que pueda decir otra palabra, él decide intentar adivinar por él mismo."

show hideaki evil
with charachange

hh "Si fuera a adivinarlo yo… ¿tu corazón?"

$ renpy.music.set_volume(0.5, 0.5, channel="music")
$ renpy.music.set_volume(0.0, 0.5, channel="ambient")

show akira basic_lost
show lilly basic_listen_cas_close
with charachange

"Akira me observa moderadamente curiosa, su interés también avivado. Esa ciertamente fue una suposición afortunada."

hi "¿Cómo lograste…?"

$ renpy.music.set_volume(1.0, 10.0, channel="music")
$ renpy.music.set_volume(0.5, 10.0, channel="ambient")

show hideaki thinking
with charachange

hh "No te faltan extremidades ni tienes deformaciones, así que descarto las discapacidades externas."

show hideaki serious
with charachange

hh "Considerando la ausencia de gestos extraños, es improbable que tengas alguna discapacidad mental."

show lilly basic_planned_cas_close
with charachange

li "Pero Yamaku no acepta estudiantes con discapacidades mentales."

show hideaki bored
with charachange

hh "Lo sé."

show hideaki serious_up
with charachange

hh "Dejando eso a un lado, la única posibilidad que queda es que sea una discapacidad interna."

show hideaki happy
with charachange

hh "No sabía cuál podría ser, así que adiviné. Correctamente, resultó ser. Y tu reacción confirmó mi suposición."

show akira basic_smile
with charachange

"Más que un tanto perplejo, miro a Akira. Ella sonríe y se encoge de hombros, obviamente disfrutando la deducción de su compañero."

"Es agudo, sí, pero poco compasivo también. Lógico, pero carente de tacto. Su actitud me recuerda a Shizune, de cierta forma, y también su apariencia."

show hideaki disapproves
with charachange

hh "¿Puedo preguntarte por qué me estás observando así? No creo que sea un espécimen tan inusual."

"¿Acaso no se da cuenta de lo inusual que se ve? Podría pasar por alto las polainas y la ropa como solo una coincidencia, pero la cinta en su cabello de verdad es demasiado."

"Aunque esto es totalmente irrelevante."

hi "Lo siento. Es solo que me recuerdas a alguien."

play sound sfx_impact

show akira basic_boo
show hideaki surprise_up
with vpunch

"Akira le da un codazo fuerte."

show akira basic_laugh
with charachange

aki "Te dije que no eras tan distinto a ella."

show hideaki closed_up
with charachange

"Él tose, tapándose la boca con la mano, intentando mantener una postura derecha y seria."

hh "Entonces veo que ya conoces a mi hermana. Quizás mi nombre completo pueda ayudarte."

show hideaki serious
with charachange

hh "Soy Hideaki Hakamichi. Probablemente piensas en mi hermana, Shizune Hakamichi."

"Oh, así que es el hermano de Shizune."

"Espera, si Hideaki es el hijo del tío de Akira, y Shizune es su hermana, entonces eso significa que los padres de Lilly y Shizune son hermanos. Por lo tanto…"

hi "¿Lilly y Shizune son primas?"

show lilly basic_concerned_cas_close
show akira basic_smile
with charachange

"Lilly refunfuña de una forma inusitadamente descontrolada. La reacción se gana una sonrisa divertida de parte de su hermana."

"La enemistad entre ellas dos acaba de tomar un nuevo significado. Había pensado que era simplemente cosa de la dificultad de comunicación entre las dos, pero una riña familiar complica las cosas mucho más."

show akira basic_laugh
with charachange

aki "Puedes escoger a tus amigos, pero no puedes escoger a tu familia."

show akira basic_boo
with charachange

"Ella se encoge de hombros sin mucho ánimo. Parece no darle tanta importancia al conflicto entre ellas dos como yo."

show akira basic_smile
with charachange

aki "Bueno, así es como es. De todas formas, ¿en qué andan ustedes dos en este agradable día?"

show lilly basic_smileclosed_cas_close
with charachange

li "Buscamos un regalo de cumpleaños para Hanako. Pronto va a llegar el día, así que esta es la última oportunidad que tendremos antes de que vuelvan a comenzar las clases durante la semana."

stop music fadeout 7.0

show akira basic_lost
with charachange

"Akira pone una cara extraña, como si Lilly acabara de decir que el cielo no es azul y las nubes no son blancas."

aki "¿Su cumpleaños no es el diez del próximo mes?"

show lilly basic_surprised_cas_close
with charachange

li "Sí… ¿Por qué? ¿Pasa algo malo?"

show akira basic_resigned
with charachange

"El rostro de Akira parece colapsar. Es una expresión completamente inapropiada para alguien tan escandalosa y terca."

aki "¿Los viejos aún no te han llamado?"

show lilly basic_oops_cas_close
show hideaki confused
with charachange

"Mientras Lilly niega con la cabeza sin tener idea, miro a Hideaki para ver si él sabe algo de esto. Un simple encogimiento de hombros es su única respuesta."

show akira basic_boo
with charachange

"Por un momento, Akira parece pensar en qué hacer antes de volver a sonreír. El hecho de que pueda ocultar sus emociones tan rápida y efectivamente es inquietante."

show akira basic_smile
with charachange

aki "Oye Peque, lo siento, pero ¿podrías quedarte con Hisao por un ratito?"

$ renpy.music.set_volume(0.7, 2.0, channel="ambient")

show hideaki normal
with charachange

show lilly basic_oops_cas_close:
    parallel:
        easeout 1.0 xpos -0.5
    parallel:
        linear 0.7 alpha 0.0
show akira basic_smile:
    parallel:
        easeout 1.0 xanchor 1.0 xpos 0.0
    parallel:
        linear 0.7 alpha 0.0
show hideaki normal:
    ease 1.0 center
show bg city_street2:
    ease 1.0 right
show crowd:
    ease 1.0 right
with Pause(1.0)

hide lilly
hide akira
with None

"Él asiente y se despide, Akira colocando un brazo sobre el hombro de Lilly mientras la guía lejos de nuestro campo auditivo."

"Y así, estoy solo con el “Peque”."

hi "Entonces… buen clima, ¿no crees?"

show hideaki thinking at center
with charachange

hh "Así parece."

"…"

hi "Creo que nos abandonaron."

show hideaki serious
with charachange

hh "Efectivamente."

"Qué intento más absurdo de cháchara. No tengo idea de cómo hablar con este tipo, y sus respuestas robóticas no están ayudando. Se me viene a la mente que es como hablar con una pared."

show hideaki triangle
with charachange

"Sin decir otra palabra, él comienza a mecerse sobre sus pies en un obvio gesto de aburrimiento con esta conversación. De verdad es como un niño pequeño, a pesar de su actitud seria."

"Sospechando que la conversación se ha acabado, decido hacer lo que vine a hacer en primer lugar."

hi "Voy a ir a buscar un regalo de cumpleaños. ¿Vienes?"

show hideaki normal
with charachange

hh "No hay mucho más que hacer."

stop ambient fadeout 0.5

scene bg city_street3
with shorttimeskip

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_traffic fadein 2.0

"En un rato, llegamos a una pequeña tienda junto a un almacén."

"Por una vez las vitrinas no están llenas de artículos electrónicos y juegos de computadora, sino de muñecas, osos de peluche y toda clase de curiosidades de madera."

hi "¿Antigüedades… Otelo?"

"¿Una tienda de antigüedades? Bueno, si hay algo en esta ciudad que le sentaría a Hanako, supongo que estaría aquí."

"Extiendo mi mano hacia el picaporte antiguo, pero la retiro en el último instante cuando me doy cuenta de que mi compañero se ha separado."

hi "¿No vienes?"

show hideaki triangle at center
with charaenter

hh "Me quedaré en el puesto de periódicos por un rato. No te preocupes."

"Su voz deja tajantemente en claro que no tiene ningún interés en lo que hay en la tienda, y que no se siente obligado a seguirme."

hide hideaki
with charaexit

"Cuando se marcha sin decir más, yo empujo la gruesa puerta de madera y entro a la tienda, una campana sonando sobre mí."

stop ambient fadeout 0.5
play sound sfx_storebell

scene bg city_othello at Fullpan(10.0, dir="left")
with locationskip

play music music_soothing fadein 0.5

"El olor mohoso de libros viejos y estanterías de madera es distintivamente anacrónico."

"Miro hacia el mostrador junto a la puerta. El hombre canoso tras él está sentado ahí en silencio, leyendo un libro desgastado. Ciertamente concuerda con el aspecto del lugar."

"Pasando lentamente por los pasillos, la persona que se me viene a la mente cada vez que inspecciono una manualidad o curiosidad importada no es Hanako."

"Agachándome, examino un antiguo escritorio de roble dentro de la vitrina de la tienda."

"Al menos treinta muñecas, todas de distintos tamaños y manufactura. La única similitud entre ellas son los largos vestidos victorianos que usan."

"Doy vuelta a la etiqueta de una de las que parece llegarme hasta la cintura."

"… No está en mi rango de precios. Para nada."

"Hago lo mismo con cada una de ellas, deprimiéndome más y más a medida que se vuelven más y más pequeñas."

"Eso es, hasta que llego a la más pequeña de todas. Puedo costearla, apenas, pero es de buena calidad y tiene cabello largo y cobrizo, y un pequeño vestido azul."

"Decido que es el tipo de regalo que Hanako apreciaría. Bonito, y para nada chillón."

"Después de tomarla con cuidado, decido seguir mirando por la tienda. No estoy seguro si es porque me gusta la atmósfera o por mera curiosidad."

stop music fadeout 2.0

show bg city_othello at left
with None

"Dando un vistazo a la vuelta de la esquina antes de pasar al siguiente pasillo, veo que los estantes en este están llenos de juguetes de madera; desde autos de juguete hasta autómatas intrincados."

show musicbox closed:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"Escondido detrás de una línea de cascanueces, noto una pequeña y sencilla caja de madera. Se siente sorprendentemente ligera cuando la recojo con mi mano libre."

show musicbox open:
    ypos 0.5 alpha 1.0
with charachange

play music music_musicbox

"La tapa solamente requiere un pequeño movimiento para abrirse, y el pequeño cilindro de metal adentro comienza a rotar de inmediato."

"Por largo rato, me quedo simplemente detenido ahí escuchando la melodía que cabe en la palma de una mano."

"Mientras toca, tomo la pequeña etiqueta entre mis dedos y la levanto hasta mi rostro, leyendo con dificultad la minúscula letra cursiva."

"Es asequible… más o menos."

show musicbox closed
with charachange

play sound sfx_switch
stop music

show musicbox closed:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide musicbox
with None

"Con una pequeña mueca, cierro la tapa y me dirijo al mostrador con la muñeca y la caja de música en mano."

show shopkeep surprised at center
with charaenter

"Cuando dejo los dos objetos sobre el mostrador, el hombre tras él se sienta derecho y los examina. No esconde muy bien su sorpresa de que alguien de mi edad los compre."

show shopkeep thinking
with charachange

"Es doloroso, pero entrego dinero para pagar los dos y salgo de la tienda con una pequeña bolsa opaca en mano."

play ambient sfx_traffic fadein 0.5

scene bg city_street3
show hideaki serious at center
with locationchange

"Que Hideaki esté ahí me toma por sorpresa."

hi "Oh… hola. Pensé que estarías en el puesto de periódicos."

show hideaki bored
with charachange

hh "Akira me llamó. Nos está esperando en la fuente junto con Lilly."

"Al menos eso resuelve el problema de intentar encontrarlas otra vez."

$ renpy.music.set_volume(0.4, 0.5, channel="ambient")

scene bg city_street2
with locationskip

"Nos dirigimos de vuelta a la fuente. La postura y presentación de Hideaki, a pesar de su apariencia, hacen un extraño contraste mientras caminamos."

show lilly cane_reminisce_cas at twoleft
show akira basic_boo at tworight
with charaenter

"Lilly y Akira están ahí de pie esperándonos, sus expresiones difíciles de leer."

show akira basic_smile at tworight
with charachange

aki "Oye. ¿Listo para irte, Peque?"

show bg city_street2 at bgleft
show lilly cane_reminisce_cas at left
show akira basic_smile at Transform(xpos=0.55)
with charamove

show hideaki happy at right
with charaenter

"El humor de Hideaki parece mejorar cuando se reúne con ella."

show hideaki happy_up
with charachange

aki "Nos vemos Lilly, Hisao. Díganle a Hanako que le deseo un feliz cumpleaños."

hi "Se lo diremos. Adiós."

show lilly cane_weaksmile_cas
with charachange

li "Hasta luego, Akira."

hide akira
hide hideaki
show lilly cane_reminisce_cas
with charaexit

show lilly cane_reminisce_cas at center
show bg city_street2 at bgright
with charamove

"Y con eso, los dos desaparecen entre el tumulto de la multitud de atardecer."

"Girando hacia Lilly, noto que carga una pequeña bolsa. Ahora entiendo por qué su disposición se siente diferente de antes; si bien Lilly es de las que muestran sus emociones a flor de piel, ahora su expresión y tono son confusos y difíciles de leer."

"Es más que un poco desalentador, pero dado el esfuerzo que está poniendo en ocultar sus emociones, dudo que quiera ser acorralada con el porqué se siente así."

hi "¿Ya le compraste un regalo a Hanako?"

show lilly cane_weaksmile_cas
with charachange

li "Sí. ¿Lo has hecho tú?"

hi "Claro."

show lilly cane_sleepy_cas
with charachange

li "¿Entonces regresamos a la parada de autobús?"

hi "De acuerdo. Debería pasar un autobús de regreso a Yamaku pronto."

"Y con eso, comenzamos a caminar."

$ renpy.music.set_volume(0.7, 0.5, channel="ambient")

scene bg city_street1
show lilly cane_concerned_cas_close at twoleft
with locationskip

"Se siente extraño comparado con antes. La mano de Lilly en mi antebrazo se siente inusualmente tensa, y el ambiente en general se siente extraordinariamente incómodo."

"El silencio continúa por un largo rato. De verdad no me gusta verla así."

show lilly cane_sleepy_cas_close
with charachange

li "La fiesta de cumpleaños de Hanako va a tener que celebrarse antes. ¿Te parece bien que sea el cuatro?"

"De todas formas no tengo ninguna otra posible obligación, así que asiento en reflejo. Solo después recuerdo que hacer eso no tiene sentido, y rápidamente respondo eso con habla."

"Ella intenta recuperar la compostura, una tarea que parece casi lastimera en lo claro que es ver lo distantes que están sus pensamientos."

show lilly cane_weaksmile_cas_close
with charachange

li "Lo siento, Hisao. Dijiste que el autobús pasaría pronto, ¿correcto?"

hi "Así es."

"Pero ahora que ella dice eso, tengo una idea."

hi "De hecho, ¿tienes algo que hacer más tarde?"

show lilly cane_oops_cas_close
with charachange

li "Yo… no lo creo. ¿Por qué lo preguntas?"

hi "Este es el momento en que normalmente tomaría tu mano y te arrancaría hacia alguna parte, pero aun sin eso, tendrás que confiar en mí. ¿De acuerdo?"

show lilly cane_surprised_cas_close
with charachange

"Tomo de su mano y la conduzco cuidadosamente, su rostro distante reemplazado por uno de moderada sorpresa y curiosidad."

stop ambient fadeout 2.0

scene bg city_karaokeint
with shorttimeskip

$ renpy.music.set_volume(1.0, 10.0, channel="ambient")
play music music_another fadein 2.0

"Cuando la camarera coloca la taza de té y la taza de café que ordené sobre la mesa, le agradezco antes de que se retire."

"A decir verdad, en realidad tuve suerte de haber encontrado este café. En realidad no sabía adónde iba, y simplemente estaba buscando cualquier café que pareciera relativamente agradable."

"Habiendo logrado recuperarse un poco, Lilly bebe vacilantemente de su taza mientras yo bebo un largo trago del café frente a mí."

"Como esperaba, su rostro se ilumina cuando se da cuenta de cuál sabor es."

show lilly basic_weaksmile_cas_close at Transform(xalign=0.5, ypos=0.15, yanchor=0.0)
with charaenter

li "¡Ah… esto está maravilloso!"

show lilly basic_surprised_cas_close
with charachange

li "Hisao, ¿cómo supiste que este era…?"

"Pedí té negro de vainilla francés, poniendo mis esperanzas en que sería su sabor favorito, o al menos uno que le gustara. Si bien en verdad no sé mucho de té, sonaba como uno que ella podría apreciar."

"… A partir del hecho de que le gustara el helado de vainilla. Un conocedor de té definitivamente no soy."

hi "Fue una suposición afortunada. De verdad te gusta el té, ¿no es así?"

show lilly basic_smileclosed_cas_close
with charachange

"Ella baja su taza y asiente un poco, con esa sonrisita familiar agradecidamente posada en su rostro una vez más."

show lilly basic_smile_cas_close
with charachange

li "Beber té es… relajante, creo."

hi "Con la cantidad que bebes, ¿estás segura de que no eres adicta a ello? La adicción a la cafeína es algo bastante común hoy en día."

show lilly basic_giggle_cas_close
with charachange

li "¿Alguna vez dije que no lo fuera?"

"Ella suelta una risita y dejo caer mi cabeza. Todos tenemos nuestros vicios, supongo, y hay cosas peores a las que ser adicto."

hi "Té negro de vainilla francés, ¿eh? Tendré que recordar eso."

show lilly basic_smileclosed_cas_close
with charachange

"Por un rato, ambos bebemos en silencio. Es reconfortante tener a alguien como ella cerca en un lugar nuevo como este, aun si es solo nosotros dos sentados en silencio."

"Comienzo a preguntarme si el sentimiento es el mismo para ella, cuando de repente ella baja su taza."

show lilly basic_emb_cas_close
with charachange

li "Hisao, ¿te molesta si te pregunto algo un tanto extraño?"

hi "Eso depende de la pregunta, supongo."

show lilly basic_weaksmile_cas_close
with charachange

li "Me preguntaba… cuál será tu color favorito. Después de todo, todos tienen uno."

"Casi respondo antes de darme cuenta de por qué la pregunta aparentemente banal es de hecho bastante extraña."

hi "¿Mi color favorito? Pero…"

show lilly basic_pout_cas_close
with charachange

"Ella hace un puchero, queriendo que responda de todas formas. Si bien la respuesta parece inevitablemente desperdiciada con ella, no hay nada de malo en dársela."

hi "Siempre he sentido algo por el verde. Diría que es mi favorito."

show lilly basic_satisfied_cas_close
with charachange

li "¿Verde, entonces? ¿En qué cosas piensas cuando contemplas ese color?"

hi "Supongo que… praderas y árboles en verano. También en el ejército, por el camuflaje."

show lilly basic_planned_cas_close
with charachange

li "A los hombres siempre parece gustarles lo militar."

show lilly basic_smile_cas_close
with charachange

li "Pero… eso suena como un color bonito. Un color muy bonito."

"Ella asiente un poco, como aprobando mi elección. Considerando lo extraño que el concepto de color es para su mente, calificarlo por asociación parece bastante razonable."

hi "Si todos tienen un color favorito, entonces ¿cuál es el tuyo?"

show lilly basic_smileclosed_cas_close
with charachange

li "Blanco. Me han dicho que es el color de la nieve, y del helado."

hi "No eres mejor que yo, entonces, si solo te gusta ese color por una comida favorita. Aunque creo que el blanco también es bonito."

hi "Y hablando de colores, oscurecerá pronto. Déjame ayudarte a levantarte."

show lilly basic_smile_cas_close
with charachange

show lilly basic_smile_cas_close at center
with charamove

"Lilly ofrece su mano, la cual tomo con la mía para ayudarla a impulsarse de su asiento en la mesa. Su suavidad comparada con la mía me toma por sorpresa, ya que en realidad no estoy muy acostumbrado al contacto tan casual."

"Sin embargo, no parece preocuparle a ella para nada. Aunque parece obvio por qué, se siente como si tan solo fuera otro aspecto refinado más de ella."

"Cuando su mano se mueve hacia su bolsillo, la interrumpo en el acto."

hi "No te preocupes, yo pagaré esto."

show lilly basic_cheerful_cas_close at center
with charachange

li "Oh. Gracias, Hisao."

"Ella sonríe con sinceridad ante el gesto, una recompensa mucho mayor que la de sus palabras."

stop music fadeout 2.0

scene bg suburb_roadcenter_ni
with shorttimeskip

$ renpy.music.set_volume(0.2, 0.5, channel="ambient")
play ambient sfx_cicadas fadein 0.5

"Ya cuando nos bajamos del autobús, está bien oscuro afuera."

$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

scene bg school_road_ni
with locationskip

"Nos dirigimos colina arriba en silencio, ambos actuando un tanto incómodos, probablemente debido a los acontecimientos del día."

"Aunque aún me preocupa la actitud retraída de Lilly después de encontrarnos con su hermana, el hecho de que lograra animarla aunque fuera un poco se siente como una victoria personal."

"Pero… se siente como si el aire entre nosotros hubiera cambiado. Quizás es solo un poco, pero es algo de lo que creo que ninguno de los dos se había dado cuenta antes."

show lilly cane_weaksmile_cas_ni at center
with charaenter

li "Eso fue… una cita, ¿o no?"

"Lo fue. Eso no se nos escapa a ninguno de los dos, siendo la respuesta a esa pregunta tan evidente que llega a ser retórica."

"Por lo incómodo que sea, no creo que este sentimiento sea malo. De hecho, todo lo contrario. No sé qué es, ciertamente no puedo estar seguro, pero se siente como algo más que amistad."

"¿Entendimiento? ¿Simpatía? Buscar palabras que lo describan adecuadamente es difícil. De todas formas…"

hi "¿Te gustaría hacer esto alguna otra vez, Lilly? ¿Sin tener que comprar regalos?"

show lilly cane_emb_cas_ni
with charachange

"La vacilante pregunta es respondida con la misma expresión que Lilly tenía antes. Su blanco rostro hace que el rubor de sus mejillas sea un poco más notorio y su cara, aunque aún dirigida hacia la calle delante de ella, baja. Solo un poco."

show lilly cane_cheerful_cas_ni
with charachange

li "… De acuerdo."

stop ambient fadeout 2.0

scene black
with dissolve




label es_L4:

scene bg school_girlsdormhall
with locationchange

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

"Camino por el pasillo de los dormitorios de chicas, mochila en mano."

"Adentro hay una muñeca, puesta con cuidado sobre una caja pequeña. He estado cargando la caja ahí desde hace un tiempo, aún sin estar seguro de qué hacer con ella."

"Toda esta situación, ahora que lo pienso, es extraña."

"Aunque he sabido sobre la fiesta de cumpleaños de Hanako desde hace un tiempo, no tenía idea de exactamente dónde sería la celebración hasta que encontré una nota en el cuarto de té vacío más temprano hoy."

"La sostengo y la vuelvo a leer, corroborando las instrucciones. La sencilla letra negra es bastante legible a pesar de la ceguera de Lilly, claramente gracias a considerable esfuerzo y cuidado."

window hide

$ written_note(u"Hisao,\n\nLa fiesta va a ser en mi cuarto. Por favor ven a las seis a la habitación 225 en el dormitorio de chicas.\nDisculpa por notificarte de esta manera, pero me han tocado deberes como representante de clase.\n\n- Lilly Satou", text_args={"color":"#000000"})

window show

"Sin estar convencido, sigo caminando por el pasillo hasta que llego al dormitorio de Lilly. Por un segundo dudo, pero eventualmente golpeo tres veces la puerta."

play sound sfx_doorknock2
with Pause(0.5)

"Se escucha un breve y amortiguado intercambio de palabras desde el otro lado. Escuchando detenidamente, puedo identificar las voces de Lilly y Hanako."

"Cuando terminan, Lilly llama."

li "¿Será Hisao?"

hi "Síp. Encontré la nota que me dejaste."

li "Puedes entrar, la puerta está abierta."

"Feliz de haber encontrado el cuarto correcto, bajo la manilla y entro."

play sound sfx_dooropen

"Cuando la puerta se abre, mi saludo para ellas es arrebatado de mi boca."

window hide

play music music_one fadein 10.0

scene ev lilly_bedroom:
    truecenter
    zoom 1.1 subpixel True
    ease 15.0 zoom 1.0
with GenericWhiteout(0.5,0.1,4.0)

window show

"Lilly está sentada en una mesa baja en el centro del cuarto vestida en ropa de dormir, mientras que al otro lado está sentada Hanako con un camisón. Estando vestido solo con mi uniforme escolar normal, me siento muy fuera de lugar."

"Doy un rápido vistazo a la encantadora imagen de ellas dos, mis ojos apartándose de las largas, delgadas y blancas piernas de Lilly solo con un poco de renuencia."

hi "Ho-hola. Yo… creo que traje todo lo que hacía falta."

scene ev lilly_bedroom_large:
    xpos -130 ypos -400 subpixel True
    acdc_warp 12.0 ypos -800
with flash

"Ella sonríe y asiente. Me pregunto si está siquiera consciente de la agradable imagen que entrega. La delgada seda azul oscuro de su ropa de dormir en verdad le asienta, acentuando tanto sus ojos como sus curvas."

"Su aspecto de anoche, esa apariencia indecisa y casi avergonzada, se ve totalmente reemplazada por su naturaleza coqueta. Es bueno ver que haya recuperado su confianza, aunque no puedo evitar recordar cómo se veía en ese momento."

scene ev lilly_bedroom_large:
    xpos -830 ypos -200 subpixel True
    acdc_warp 12.0 ypos 0
with flash

"Miro a Hanako, quien está nerviosamente sentada opuesta a ella con su vestido. No es de sorprender que vista algo tan conservador, aunque definitivamente se ve linda."

hi "Hola, Hanako. Feliz cumpleaños."

ha "Ah… g-gracias."

"Ella está inusualmente asustadiza, a pesar del hecho de que hayamos llegado a llevarnos bastante bien durante las semanas que nos hemos conocido. Esta es una situación bastante inusual, supongo."

scene ev lilly_bedroom
with flash

li "Puedes tomar asiento si quieres, Hisao. Les serviré algo de té a los dos."

hi "Claro."

$ renpy.music.set_volume(0.8, 2.0, channel="music")

scene bg school_dormlilly
with locationchange

"Lilly toma la humeante tetera roja del costado de la mesa y suavemente vierte su contenido en nuestras tazas mientras yo tomo asiento junto a ellas, dejando mi mochila apoyada contra una pared cercana."

"Ya con mis sentidos de vuelta y mis hormonas un tanto más calmadas, me doy cuenta de que esta es la primera vez que he estado en el cuarto de Lilly."

"Lo primero que noto es el aroma ambiental, solo un poco distinto del mío… probablemente un dejo de perfume, o esmalte de uñas. Podría ser cualquier cosa de chica, en realidad."

"Otra cosa es la naturaleza simple del cuarto, hablando visualmente. Paredes beige, un armario elegante aunque sin adornos, la ausencia de pósteres o colgantes en las paredes. Es claramente utilitaria, algo que debería haber anticipado dada su ceguera."

"La única cosa que de verdad parece fuera de lo común son varias pilas de libros en el suelo, cada una alzándose a una altura aproximadamente desde la rodilla hasta la cadera."
"Algunos de ellos tienen títulos impresos, otros están completamente en blanco salvo por los puntos de braille."

"El hecho de que aquellos con títulos impresos estén todos en inglés es interesante, aunque no del todo inesperado. Después de todo, ella había mencionado que sus padres les formaron a ella y a Akira el idioma."

hi "Tu cuarto se ve bien, Lilly."

show hanagown distant:
    center
    ypos 1.15
with charaenter

"Oigo un gracias desde un costado de mi hombro. Volviendo la vista a Hanako, veo que su mirada está fija en su regazo y sus manos aferran nerviosamente su vestido."

"Ahora noto por qué. Con esta ropa puesta, la extensión de sus cicatrices es mucho más visible; alcanzando su cuello y bajando por su hombro derecho, cubriéndolo."

"Dado que esto es una fiesta para ella, en realidad no parece que esté disfrutando la experiencia ahora que yo estoy aquí."

hi "¿Entonces cuántos años cumples? ¿Dieciocho?"

show hanagown worry
with charachange

"Su expresión de sorpresa, para nada disminuida por su absoluta falta de habilidad para esconder sus emociones, muestra que estaba intentando desconectarse mentalmente. Esto es de verdad bastante incómodo."

ha "S-sí."

hi "El lado positivo es que solo quedan dos años más para que puedas beber. ¿Y quién es mayor? ¿Tú o Lilly?"

show hanagown normal
with charachange

ha "Lilly. Su cumpleaños fue en… f-febrero. ¿Qué hay del… tuyo?"

hi "Antes este año, así que ya pasó."

"No menciono que la fecha pasó mientras estaba atrapado en el hospital. Eso fue… un punto particularmente bajo de la experiencia."

show hanagown distant
with charachange

show hanagown distant:
    tworight
    ypos 1.15
show bg school_dormlilly at bgright
with charamove

show lilly basic_smileclosed_paj:
    twoleft
    ypos 1.2
with charaenter

play sound sfx_teacup

"La conversación con ella se agota tan rápido como lo esperaba. No pasa mucho tiempo para que Lilly acabe de preparar nuestras bebidas, dejando las tres tazas frente a nosotros."

"Tomo la mía, notando inmediatamente un aroma y sabor mucho más fuertes que el té que tomábamos antes."

hi "Eh, sabe distinto del té que bebemos en la escuela."

show lilly basic_smile_paj
with charachange

li "Es de una variedad distinta, no del tipo que bebemos allá. ¿Alguna vez has probado la Naranja de Jaipur antes?"

hi "No… que yo recuerde. Después de todo, usualmente bebo café, como cuando estábamos en la ciudad. Aunque este está bueno."

show hanagown normal
with charachange

"Mientras nos acomodamos y damos un sorbo, Hanako parece relajarse más, o por lo menos está un poco menos tensa por mi presencia."

"Todos terminamos nuestras tazas más o menos al mismo tiempo, Hanako no pudiendo esconder en absoluto su anticipación por el pastel que está a un costado, rogando ser comido."

stop music fadeout 4.0

"Ahora que lo pienso, yo mismo me siento emocionado. Aunque primero lo primero."

hi "¿Lilly?"

show lilly basic_planned_paj
with charachange

li "Sí, ahora está bien."

"Sabiendo ambos exactamente lo que el otro quiere decir, me inclino hacia un lado y hurgo en mi mochila buscando la muñeca que le compré a Hanako mientras que Lilly se levanta y alcanza su regalo."

"Escondiendo nuestros regalos en nuestras manos, ambos los presentamos al mismo tiempo sobre la mesa."

show lilly basic_cheerful_paj
show hanagown normal_blush
with charachange

$ doublespeak (li, hi, u"¡Feliz Cumpleaños!")

"Hanako se queda sentada en silencio mirándolos durante largos segundos, debido a semejante sorpresa."

"Mi pequeña muñeca de madera, repleta con vestido de la era victoriana y un pequeño sombrero, yace junto a un oso de peluche esponjoso y color café claro de parte de Lilly."

show hanagown distant
with charachange

"Ella agarra el borde de su vestido mientras se mueve para hablar, sin apartar sus ojos de los modestos obsequios."

show hanagown distant_blush
with charachange

ha "G… gracias… Lilly y… Hisao…"

play music music_serene fadein 6.0

scene unlock_ev lilly_hanako_hug_end
show black
show ev lilly_hanako_hug:
    xalign 0.5 yalign 1.0 alpha 0.0 subpixel True
    parallel:
        linear 5.0 alpha 1.0
    parallel:
        easein 15.0 yanchor 0.0 ypos -0.15

with locationskip

"Su voz comienza a flaquear, y Lilly se inclina hacia adelante, cubriéndola en un suave abrazo."

"Ver a Hanako abrazando tan fuerte a Lilly es conmovedor, tanto que siento que no podría borrar la sonrisa de mi rostro, aun si quisiera."

"Mientras Lilly apoya su rostro ligeramente en la cabeza de Hanako, habla tan bajo y suavemente que apenas la escucho."

li "Feliz cumpleaños, Hanako."

hi "Feliz cumpleaños."

"Hanako asiente ligeramente, abrazando a Lilly durante un tiempo antes de soltarse y frotarse un ojo."

"Supongo que para Hanako simplemente tener a alguien, quien sea, que esté ahí y la ame debe de ser especial. El hecho de que Lilly y yo ahora podamos compartir ese rol para ella es algo que creo que siempre agradeceré."

scene ev hanako_presents1
with locationskip

"Hanako toma suavemente la muñeca y el oso de peluche, sosteniendo ambos junto a su pecho mientras sonríe afectuosamente."

"Por un largo rato, los tres simplemente estamos sentados felizmente en silencio. La calma no es interrumpida hasta que la dulce voz de Lilly nos indica."

li "¿Nos servimos del pastel, entonces?"

scene bg school_dormlilly
show lilly basic_smile_paj:
    twoleft
    ypos 1.2
show hanagown smile:
    tworight
    ypos 1.15
with locationskip

"Su propuesta es respondida con dos miradas de anticipación no escondida."

hi "Yo no me quejo."

ha "De acuerdo."

stop music fadeout 2.0

scene bg school_dormlilly
show lilly basic_smileclosed_paj:
    twoleft
    ypos 1.2
show hanagown normal:
    tworight
    ypos 1.15
with shorttimeskip

hi "Uf, eso estuvo bueno."

play music music_dreamy fadein 4.0

"Me reclino hacia atrás, satisfecho, y tanto Lilly como Hanako parecen tan satisfechas con la comida como yo. Requirió algo de esfuerzo, pero logramos acabar el pastel de una sola vez."

show hanagown normal_blush
with charachange

ha "No creo que me quede espacio en el estómago."

show lilly basic_weaksmile_paj
with charachange

li "Creo que la próxima vez compraré un pastel más pequeño."

show hanagown smile
with charachange

"Hanako y yo nos reímos, pero no puedo evitar notar que, llegado este momento el próximo año, ya nos habremos graduado de Yamaku."

"Ese hecho es algo deprimente, ya que por fin siento como si mi vida comenzara a volver a tener cierto orden."

"Mirando ociosamente el pulcro y ordenado cuarto de Lilly, sus libros me llaman la atención otra vez."

"Puede ser un tanto impulsivo, pero la curiosidad me vence. Además, de todas formas no creo que le moleste."

hi "Oye Lilly, ¿te molesta si miro uno de tus libros?"

show lilly basic_smile_paj
with charachange

li "Eres bienvenido a hacerlo, Hisao."

show lilly basic_planned_paj
with charachange

li "Dicho eso, si puedes sobrepasar dos barreras idiomáticas estaré bastante impresionada."

hi "¿Dos? Braille y… oh cierto, inglés."

show lilly basic_smile_paj
with charachange

"Ella asiente."

hi "Sabía que estudiabas inglés, pero aún me sorprende que seas tan hábil en ello."

show lilly basic_giggle_paj
with charachange

li "Uno podría decir que es la forma perfecta de evitar que la gente tome prestada mi colección."

"Ella dice esto en broma, pero me siento un poco desilusionado. Tener todos estos libros a mi alrededor sin tener forma de leerlos se siente como una gran tentación."

"Hanako se ríe en silencio mientras alcanzo la pila más cercana, tomando el libro superior con solo una inspección general. “Death on the Nile”, en grandes letras sobre la cubierta, es el único texto impreso visible."

$ renpy.music.set_volume(0.5, 0.5, channel="music")
play sound sfx_paper
show ev braille at Fullpan(10.0, dir="right")
with locationskip

"Me siento por un rato con el libro abierto sobre mi regazo mientras Lilly y Hanako platican."

"Por mucho que intente sentir los puntos de braille impresos en cada página, parecen mezclarse entre ellos y volverse indistintos."

"Pensé que esto sería mucho más fácil de lo que es en realidad. Aunque con algo de práctica, podría imaginarme a alguien con mejor sentido del tacto que yo logrando leer a una velocidad bastante rápida."

$ renpy.music.set_volume(1.0, 0.5, channel="music")

scene bg school_dormlilly
show lilly basic_smileclosed_paj:
    twoleft
    ypos 1.2
show hanagown normal:
    tworight
    ypos 1.15
with locationskip

"Notando un silencio que probablemente haya comenzado antes, levanto la mirada desde las páginas punteadas para ver a Lilly sonriendo mientras Hanako bebe otra taza de té."

hi "¿Pasa algo?"

show lilly basic_smile_paj
with charachange

li "Todo lo contrario, tu curiosidad es bastante llamativa."

"Me siento enormemente satisfecho por el elogio, aunque puedo sentir mis mejillas calentarse un poco."

hi "Gracias, pero no sé cómo más podría actuar."

show lilly basic_weaksmile_paj
with charachange

li "Para serte honesta, no estaba muy segura de cómo nos veías, ya que eras un estudiante de transferencia nuevo de otra escuela."

stop music fadeout 12.0

show lilly basic_reminisce_paj
with charachange

li "Si nos hubieras tenido lástima, me habría sentido bastante ofendida."

show hanagown distant
with charachange

"Hay cierta agudeza en la voz de Lilly, una que yo posiblemente identificaría como orgullo. Mirando de reojo a Hanako, ella parece aún más contenida de lo usual, mirando hacia Lilly en lugar de a mí."

hi "No te preocupes por eso. Considerando la posición en la cual me encuentro, quizás yo sea la última persona que debería sentir lástima por otros."

hi "Las primeras interacciones que tuve con mis padres después de mi ataque cardiaco… No querría que nadie viera ese tipo de expresión."

show lilly basic_oops_paj
show hanagown distant_blush
with charachange

"Paro de hablar, pero no lo bastante pronto. Ambas chicas parecen desalentadas, Lilly en particular."

show lilly basic_emb_paj
show hanagown worry
with charachange

li "Lo… siento. No debí haberlo llevado tan lejos…"

show lilly basic_listen_paj
with charachange

$ renpy.music.set_volume(0.5, 0.0, channel="sound")
play sound sfx_doorknock2

"Por algunos instantes reina un silencio incómodo, que afortunadamente termina cuando la cabeza de Lilly se levanta en un gesto que he llegado a reconocer fácilmente."

hi "¿Oyes algo?"

show lilly basic_surprised_paj
with charachange

li "La puerta…"

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_dooropen

show lilly basic_surprised_paj:
    left
    ypos 1.2
show hanagown distant_blush at Transform(xpos=0.4)
show bg school_dormlilly at bgleft
with charamove

"Todos miramos hacia ella, confiando en los sentidos de Lilly. En efecto, la manilla de la puerta se agita y da la vuelta, un destello de amarillo y negro colándose por ella."

show akira basic_laugh at right
with easeinright

play music music_running

show lilly basic_listen_paj
show hanagown worry
with vpunch

aki "¡Akira Satou presentándose! ¡Feliz cumpleaños, Hanako!"

show hanagown worry_blush
with charachange

ha "Ah… gracias…"

show akira basic_smile at Transform(ypos=1.15, xpos=0.8, xanchor=0.5)
with dissolvecharamove

"Akira toma asiento en la mesa mientras deja su larga bolsa junto a ella. Tiene ese aire estrepitoso propio de ella, al hacer de su entrada un espectáculo."

show hanagown distant
with charachange

"Hanako agarra el borde de su vestido para calmarse, pero no parece muy agitada ya cuando se acomoda. Supongo que debe haber conocido a Akira antes, lo que no me sorprende dado lo cercanas que son Akira y Lilly."

"A Akira no parece que le afecten en absoluto las cicatrices de Hanako, a pesar de lo que resaltan, pero tampoco se contiene en su forma de actuar a pesar de la naturaleza tímida de Hanako."

show lilly basic_weaksmile_paj
with charachange

li "Pensé que habías dicho que tenías que trabajar, Akira. ¿Lograste conseguir un tiempo libre?"

show akira basic_boo:
    ypos 1.15
with charachange

aki "Eh, algo así. Me siento mal por abandonar a los chicos haciendo tiempo extra, así que debo volver pronto."

show akira basic_smile
with charachange

aki "Pero también me sentía mal por no venir a tu fiesta de cumpleaños para esta pequeña chica linda, así que por ahora, aquí estoy."

show hanagown smile
with charachange

"Ella sonríe ampliamente a Hanako, quien enrojece completamente mientras baja sus ojos hacia su regazo. Su boca parece ensancharse y contraerse una y otra vez, como si intentara reprimir una sonrisa por la vergüenza."

"Es un poco extraño cómo su reacción parece ser más inmediata y enérgica que cuando siente vergüenza por cómo se ve. Todo lo que logra responder es un diminuto asentimiento, sin lograr en mayor medida esconder su agradecimiento."

"Supongo que poca gente le da atención positiva. Me hace respetar lo bien que Akira la trata, haciéndola tan feliz, comparado con lo poco que pude hacer yo."

show akira basic_laugh
with charachange

aki "Entonces, antes de irme…"

play sound sfx_rustling

"Ella alcanza la bolsa junto a su lado y ostentosamente muestra su contenido."

show wine:
    yalign 0.5 xanchor 0.0 xpos 1.0 alpha 0.0
    easein 1.0 alpha 1.0 xanchor 1.0
with Pause(1.0)

"Salen dos grandes botellas de vidrio, ambas con extensos nombres franceses en sus etiquetas."

show hanagown normal
with charachange

"La expresión de Hanako es una mezcla extraña de sorpresa y curiosidad, y sospecho que la mía no es distinta. Lilly, al no ver las acciones, está inconsciente de lo que está sucediendo."

show hanagown normal_blush
with charachange

ha "Akira… esto no es…"

show lilly basic_surprised_paj
with charachange

li "¿Qué es?"

hi "Vino. Uno tinto, uno blanco."

show lilly basic_pout_paj
with charachange

li "¡A-Akira! ¡Eso es…!"

show akira basic_smile
with None

show wine:
    easeout 1.0 alpha 0.0 xanchor 0.0
with Pause(1.0)

hide wine
with None

aki "Relájate, relájate, no es como si Shizune estuviera aquí para regañarte."

hi "Lilly tiene razón, eso no está precisamente permitido en el campus."

hi "… O en cualquier parte, en realidad. Aún nos falta para tener la edad legal para beber, ¿recuerdas?"

show akira basic_laugh
with charachange

aki "Fuertes palabras para quien prácticamente está babeando mientras examina una botella."

"Ahí sí me ha ganado. Siento interés genuino en probar algo, aunque sea solo un poco. Aunque Hanako no haya tocado ninguna botella, su expresión me dice que también está lejos de oponerse a la idea."

show lilly basic_displeased_paj
with charachange

"Lilly frota su frente, rindiéndose en la pelea que sabe que Akira ganaría simplemente por no importarle lo suficiente esas ridículas “reglas” y “regulaciones”."

show lilly basic_displeased_paj
with charachange

li "Tan solo no digas ni una palabra de esto a nadie en la escuela, por favor. Te lo ruego."

show akira basic_smile
with charachange

aki "No soy estúpida, no te preocupes."

show akira basic_boo
with charachange

aki "Dicho eso, ya tengo que volver al trabajo pronto."

show lilly basic_oops_paj
with charachange

li "¿Tan pronto? Pero si acabas de llegar…"

show akira basic_resigned
with charachange

aki "Lo lamento, Lilly. De todas formas, es bueno volver a verlas a ustedes dos, y a ti Hisao."

hi "Hasta luego, entonces."

ha "Um… a-adiós… Akira…"

show akira basic_resigned at Transform(yalign=1.0)
with charamove

hide akira
with charaexit

"Ella se levanta con un gruñido y se retira campante del cuarto, dejándonos solos con los dos objetos en la mesa."

show lilly basic_oops_paj:
    twoleft
    ypos 1.2
show hanagown normal_blush:
    tworight
    ypos 1.15
show bg school_dormlilly at center
with charamove

hi "… Interesante."

show lilly basic_arablush_paj
show hanagown normal
with charachange

"Lilly suelta una risita nerviosa por las gracias de su hermana mientras que Hanako toma una botella de vino."

show hanagown distant_blush
with charachange

ha "Entonces…"

hi "¿Qué opinas, Lilly?"

show lilly basic_weaksmile_paj
with charachange

"Ella pone su codo sobre la mesa y presiona el caballete de su nariz, pensando detenidamente las cosas. No parece ser muy capaz de contener a su hermana."

show lilly basic_smile_paj
with charachange

stop music fadeout 3.0

li "Bueno… ya está aquí. Bien podríamos servirnos un poco."

"Tan pronto como lo dice doy una rápida mirada por el cuarto, buscando vasos."

scene bg school_dormlilly_ni
with shorttimeskip

play music music_night fadein 0.5

"Un pequeño gruñido sobre mí me recuerda que Lilly se retiró a descansar en su cama un rato hace algunos minutos."

"Agotado de energía casi por completo, logro pararme y arrastrar mi cuerpo hacia un costado de la cama, sentándome y apoyando mi espalda contra esta."

show bg school_dormlilly_ni as ovl1:
    xalign 0.5 alpha 0.4 yalign 0.5 zoom 1.0
    ease 1.0 xalign 0.55 alpha 0.5 rotate 1 zoom 1.05
    ease 1.0 xalign 0.5 yalign 0.5 alpha 0.0 rotate 0 zoom 1.0

show bg school_dormlilly_ni as ovl2:
    xalign 0.5 alpha 0.4 yalign 0.5 zoom 1.0
    ease 1.0 xalign 0.45 alpha 0.5 rotate -1 zoom 1.05
    ease 1.0 xalign 0.5 yalign 0.5 alpha 0.0 rotate 0 zoom 1.0

hi "Dios mío."

show lilly basic_listen_paj_ni:
    center
    ypos 1.2
with charaenter

li "Eugh…"

"El gruñido de Lilly suena apagado."

hi "¿Demasiada bebida?"

show lilly basic_concerned_paj_ni
with charachange

li "Me duele la cabeza."

hi "Claro, demasiada bebida."

"Descanso mi cabeza y miro ociosamente el techo. Vaya desastre absoluto."

"Como idiotas verdaderos, bebimos toda la noche un vaso tras otro. Hanako simplemente se cayó a un lado, dormida, y es un milagro que no me sienta tan enfermo como Lilly."

show lilly basic_sad_paj_ni
with charachange

li "¿Oye, Hisao? Lo siento por lo de hoy. Yo… no creí que pasaría esto."

hi "Está bien, Lilly. Honestamente, me divertí mucho hoy."

show lilly basic_weaksmile_paj_ni
with charachange

li "¿En serio?"


hi "Mmm. Creo que Hanako también. No, ciertamente ella también."

show lilly basic_reminisce_paj_ni
with charachange

"Hay un breve silencio, y luego otro gruñido resuena de Lilly que yace de espaldas."

hi "¿Estás bien?"

show lilly basic_weaksmile_paj_ni
with charachange

li "Es como dices, solo bebí demasiado. ¿Qué hora es?"

hi "¿La hora? Eh, son…"

"Miro rápidamente mi reloj, sus números apenas inteligibles en la penumbra."

hi "Cerca de medianoche."

show lilly basic_concerned_paj_ni
with charachange

li "Entonces el toque de queda está en efecto."

hi "Sí, supuse eso. Tendremos que dormir todos aquí esta noche."

"Tan pronto digo eso, oigo las sábanas moviéndose mientras Lilly comienza a sentarse."

show lilly basic_oops_paj_ni
with charachange

li "Hanako…"

hi "Ah, no, vuelve a dormir, no intentes levantarte."

show lilly basic_displeased_paj_ni
with charachange

li "Hisao, tengo que…"

hi "Tú estás en peor condición que yo bajo cualquier punto de vista. Descansa."

show lilly basic_oops_paj_ni
with charachange

li "Pero qué hay de…"

hi "Yo tomaré algunas mantas extras y las pondré sobre ella, no te preocupes."

hide lilly
with charaexit

"Mientras doy un profundo bostezo y me levanto para sacarlas, la oigo tenderse con un suave golpe."

li "Gracias, Hisao."

hi "No hay problema, es lo menos que puedo hacer. Te ves bastante tomada, de verdad."

li "No tan… tomada… solo un poco… agotada."

"Ella comienza a hacer pucheros, sus palabras empezando a ser distorsionadas, arrastrándose a medida que el alcohol toma efecto otra vez. Tomo un par de las mantas enrolladas del pie de su cama."

"Caminando silenciosamente hacia Hanako, extiendo con cuidado las mantas sobre su tranquila figura dormida, asegurándome de no despertarla."

"Aunque el denso hedor del alcohol proveniente de su aliento me hace dudar que se despierte sin importar lo que haga."

"Me levanto y evalúo la habitación una sola vez más."

stop music fadeout 4.0

"Dos chicas, ambas muy ebrias, y un chico pasando la noche con ellas en los dormitorios para estudiantes femeninas. Vaya escándalo sería si esto se supiera."

"Cuando me muevo para sentarme de nuevo a un costado de la cama, miro de reojo por última vez a Lilly."

"Su figura desparramada y despeinada yace descansando pacíficamente, apenas tumbada hacia un lado."

"Me agacho para observar mejor."

play music music_comfort

scene ev lilly_sleeping:
    truecenter zoom 1.05 subpixel True
    acdc_warp 20.0 zoom 1.0
with locationchange

"Su piel blanca se entremezcla con la almohada blanca de la cama, una expresión de serenidad durmiente en su rostro."

"Usualmente parece tan confiada y asertiva, siempre presente y preocupada por Hanako. Ahora, sin embargo, parece dolorosamente delicada."

"Vuelvo a pensar en los regalos de Hanako."

"Pensé que sería una bonita ocasión para ella, pero para nada esperaba que fuera tan emotivo."

"Un cumpleaños tras otro, año tras año."

"Solo ella y Lilly, completamente solas."

"… Supongo que no fueron solo los regalos lo que le gustó."

scene bg school_dormlilly_ni
with locationchange

"Resignándome a un sueño incómodo, me siento a un costado de la cama una vez más y descanso mis brazos cansados junto a mí."

li "Oye, Hisao."

"La voz de Lilly es tan baja que apenas logro escucharla. Ella debe estar a punto de quedarse dormida."

scene ev lilly_sleeping:
with locationchange

hi "¿Sí?"

scene ev lilly_sleeping_smile
with charachange

li "Gracias."

hi "¿Gracias? ¿Por qué?"

li "Por estar aquí."

hi "… Está bien."

scene bg school_dormlilly_ni
with locationchange

"Cuando escucho una respiración profunda, es obvio que Lilly se ha dormido."

"Ya cuando cierro mis ojos, no toma mucho para que el sueño me venza a mí también."

stop music fadeout 2.0

window hide

scene black
with shuteye



label es_L5:

window hide None

scene black
with Pause(4.0)

stop music

window show

mystery "¿Hisao?"

mystery "¿Hisao, estás…?"

"La suave, apenas audible voz que queda en mis oídos lentamente me despierta. Desearía poder ser despertado así más a menudo."

"Con un murmullo, lentamente abro mis…"

scene bg school_dormlilly
show lilly superclose
with openeye_shock

show lilly superclose_shock
with Dissolve(0.2)

$ doublespeak(hi, li, u"¡Guah!", u"¡Ah!")

play sound sfx_impact2

show lilly superclose_ouch
with vpunch

show lilly basic_concerned_paj:
    xalign 0.5 yanchor 1.0 ypos 1.2
    ease 0.4 ypos 1.4
with Dissolve(0.2)

"Tomado por sorpresa ante el rostro flotando con curiosidad a meros milímetros del mío, hago que nuestras cabezas choquen con un golpe seco."
"El impacto de nuestras frentes hace que ambos caigamos hacia atrás y exclamemos de dolor, Lilly sonando más como un juguete chillón que una persona."

hi "Ay, ay, ay."

play music music_happiness fadein 6.0

"Lentamente froto mi frente con una mano, apoyándome con la otra. Lilly yace a metro y medio más allá haciendo exactamente lo mismo, su rostro obviamente adolorido."

hi "Ah… lo siento. Tu rostro estaba algo cerca y actué en reflejo. ¿Estás bien?"

show lilly basic_concerned_paj:
    ease 1.0 ypos 1.2
with Pause(0.5)

li "Mi cabeza…"

"Parece que de hecho no está bien. Ahora que lo pienso, dudo que sea solamente el impacto lo que le está causando a su cabeza tanto dolor."

hi "¿Resaca? Bebiste una buena cantidad anoche."

show lilly basic_sad_paj:
    ypos 1.2
with charachange

"Ella asiente en silencio, confirmándolo mientras yo me levanto."

show lilly basic_concerned_paj:
    ease 1.0 ypos 1.0
with Pause(0.5)

"Le ofrezco una mano, y la ayudo a ponerse de pie. Mirando detrás de ella, veo que Hanako aún sigue profundamente dormida."

show lilly basic_reminisce_paj at center
with charachange

li "No es justo… Bebí la misma cantidad que tú…"

hi "Eso es distinto a lo que yo recuerdo. Y de todas formas, las chicas tienen menos tolerancia que los hombres."

show lilly basic_displeased_paj
with charachange

li "Eso no ayuda."

hi "Bien, te traigo un vaso de agua. Solo ten cuidado de no tropezar con Hanako."

hide lilly
with charaexit

"Froto mis ojos para sacarme el sueño, al menos en parte, mientras camino hacia el otro lado del cuarto. Cuidar a alguien con resaca no es como me gustaría pasar una mañana."

"Solo toma unos cuantos segundos llenar el vaso, el agua clara reflejando el rayo de luz que logra filtrarse por las delgadas cortinas."

"Parece que Lilly se ha sentado al costado de la cama. Camino hacia ella mientras me cuido de pasar sobre la serena y durmiente Hanako, y coloco el vaso entre sus manos extendidas."

show lilly basic_weaksmile_paj_close:
    center
    ypos 1.2
with charaenter

li "Gracias."

hi "No hay problema."

stop music fadeout 12.0

"Tomo asiento junto a ella, la blanda cama siendo sorprendentemente elástica."

"Ella bebe lenta y metódicamente. Pasa un largo silencio en el que solo se escucha la suave respiración de Hanako."

show lilly basic_reminisce_paj_close
with charachange

"Con un grado de culpa, miro el rostro de Lilly e intento leer su expresión. Tiene el ceño fruncido, y parece estar sumida en sus pensamientos."

show lilly basic_emb_paj_close
with charachange

"Por un momento dudo, pero eventualmente coloco una mano en su hombro en un intento de tranquilizarla. Aunque no esperaba que se estremeciera tan notoriamente con eso."

hi "Ah, lo siento. No era mi intención—"

show lilly basic_sad_paj_close
with charachange

"Lilly rápidamente niega con la cabeza, de una forma un tanto más violenta que lo usual para ella."

"Ella respira profundamente para calmarse antes de dejar caer su cabeza."

show lilly basic_weaksmile_paj_close
with charachange

li "Me imagino que me veo terrible ahora mismo…"

"Me muevo para protestar, pero rápidamente me doy cuenta de que sería inútil hacerlo. Dicho eso, quiero que ella se exprese más."

hi "Si quieres hablar de algo, estoy aquí."

show lilly basic_displeased_paj_close
with charachange

"Lilly resopla con autocrítica, como burlándose de sus propias emociones."

show lilly basic_reminisce_paj_close
with charachange

li "Solo que… ahora mismo están pasando muchas cosas."

show lilly basic_sad_paj_close
with charachange

li "Lo siento por estar tan extraña últimamente, especialmente cuando estábamos en la ciudad. Incluso ahora estoy un poco confundida con respecto a todo."

hi "Créeme, sé cómo se siente."

show lilly basic_weaksmile_paj_close
with charachange

"Ella sonríe melancólicamente, descansando una mejilla en el dorso de sus dedos."

li "Somos una pareja de jóvenes necios destrozados, ¿no es así?"

hi "Vamos, no digas eso. Cuando llegue la graduación, ya volveremos al mundo real."

"¿El mundo real? A veces me sorprendo a mí mismo por la forma en que pienso las cosas. Supongo que la sensación aislada y extraña de Yamaku y el pueblo circundante comparada al mundo exterior aún no se ha vuelto natural."

"Quizás nunca lo haga. Es extraño, en retrospectiva; estar aislado de la sociedad de esta forma no se siente tan mal como probablemente debería. Con una sonrisa irónica en su rostro, Lilly parece compartir la misma sensación de diversión por la idea."

"Aunque eventualmente, su sonrisa desaparece."

show lilly basic_displeased_paj_close
with charachange

li "Me iré a Escocia por una semana o dos, pronto."

hi "¿Es por eso que tuvimos que cambiar la fecha de la fiesta de cumpleaños de Hanako?"

"Ella asiente afirmativamente."

hi "Pero verás a tu familia de nuevo, por lo menos. ¿No estás emocionada por eso?"

show lilly basic_concerned_paj_close
with charachange

li "No he visto a mi familia en seis años. Ya ni siquiera sé cómo actuar cuando estoy con ellos."

"Espera… ¿qué? Mi boca queda abierta mientras intento procesar lo que dijo."

play music music_moonlight fadein 6.0

"Si tiene dieciocho, eso significa que nada más tenía doce años cuando ellos se fueron. Podré haber visto muy poco a mis padres, ya que ambos trabajaban muchas horas, pero eso es…"

"Me siento completamente inútil mientras intento encontrar alguna manera de responderle."

hi "Eso es… pero, ¿por qué?"

show lilly basic_reminisce_paj_close
with charachange

li "¿Por qué se fueron, o por qué nos están invitando a Akira y a mí de vuelta?"

hi "Ambas, supongo."

show lilly basic_sleepy_paj_close
with charachange

li "El negocio de mi padre tiene su oficina central en Escocia, y se abrió un puesto ejecutivo para él allá. Al final, tuvo que mudarse permanentemente."

li "Mi madre lo acompañó, pero Akira y yo permanecimos en Japón por el bien del trabajo de Akira en la sucursal japonesa de la compañía de mi padre, y de mi educación."

show lilly basic_concerned_paj_close
with charachange

li "Con respecto a lo último… una de mis tías está gravemente enferma."

hi "Ah. Lo… lamento."

show lilly basic_weaksmile_paj_close
with charachange

li "No lo hagas. La verdad es que se siente extraño. Estamos siendo llamadas allá por ella, y sin embargo apenas nos hemos visto antes. Ni siquiera puedo recordar cómo suena su voz."

"Igualmente extraña es la falta total de antipatía que siente hacia su familia por hacer tal cosa. No puedo evitar sentirme un tanto movido."

"Dicho eso, su expresión melancólica simplemente está escondiendo sus emociones. Verla así es deprimente."

stop music fadeout 5.0

"Sabiendo lo que tengo que hacer, me levanto de la cama. Lilly nota los movimientos de la cama, su cabeza levantándose y su mano extendiéndose hacia un lado para sentir el lugar donde me sentaba."

show lilly basic_oops_paj_close
with charachange

li "¿Hisao…?"

play sound sfx_rustling

"Camino hacia mi mochila, que aún está apoyada contra la pared. Desabrochando la lengüeta frontal y sacando la bolsa opaca de adentro, tomo la pequeña y sencilla caja con mis manos."

hi "Extiende tus manos, Lilly."

show lilly basic_surprised_paj_close
with charachange

"Ella por un momento parece sorprendida, pero eventualmente acepta."

show lilly basic_surprised_paj_close:
    ease 1.0 xpos 0.4
show bg school_dormlilly:
    center
    ease 1.0 xpos 0.4
with Pause (1.0)

show musicbox closed behind lilly:
    alpha 0.0  zoom 0.5  xanchor 0.0 xpos 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.6 alpha 1.0
show boxstrip behind lilly:
    alpha 0.0  zoom 0.5  xanchor 1.0 xpos 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.6 alpha 1.0
with Pause (1.0)

"Me divierte su expresión de curiosidad cuando coloco la caja musical en sus palmas abiertas, su típica forma delicada de manejarla haciéndolo parecer como si fuera lo bastante frágil para romperse si se respirara sobre ella."

stop music fadeout 2.0

"Ella la pone frente a su cara sin decir nada, sus dedos delgados palpando sus contornos y patrones."

"Eventualmente sus dedos encuentran la línea ahuecada entre la tapa y el cuerpo de la caja, y su pulgar abre la tapa sin hacer esfuerzo."

show musicbox open:
    xpos 0.5 ypos 0.6 alpha 1.0
with charachange

play music music_musicbox

"Me siento en la cama a su lado, observando su rostro atentamente en silencio."

"Ella está sentada completamente en silencio mientras escucha la pequeñísima melodía metálica, su boca apenas abierta."

show musicbox closed
show lilly basic_smileclosed_paj_close:
    xpos 0.4
with charachange

play sound sfx_switch
stop music

show musicbox closed:
    ease 1.0 ypos 0.7 alpha 0.0
show boxstrip:
    ease 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

show lilly basic_smileclosed_paj_close:
    ease 1.0 xpos 0.5
show bg school_dormlilly:
    ease 1.0 center
with Pause (1.0)

hide musicbox
hide boxstrip

"Pasa un largo tiempo antes de que vuelva a cerrar la tapa con un pequeño chasquido, bajando el telón de la interpretación en miniatura sonando en sus manos."

"La sonrisa en su rostro, amable y melancólica, señala que tomé la decisión correcta."

hi "Piénsalo como un regalo de despedida por tu viaje a Escocia."

show lilly basic_smile_paj_close:
    xpos 0.5
with charachange

li "Lo haré…"

play sound sfx_rustling

show lilly basic_smile_paj_close:
    twoleft
    ypos 1.2
show bg school_dormlilly at bgleft
with charamove

"Del suelo frente a nosotros se oye un movimiento inquieto, el sonido habiendo despertado a Hanako."

show hanagown distant:
    tworight
    ypos 1.3
    easein 1.0 ypos 1.1
with Dissolve(1.0)

"Ella sale con aspecto aturdido de las mantas que tendí encima de ella, limpiándose los ojos para despertarse."

hi "Veo que por fin te despertaste."

show hanagown normal:
    ypos 1.1
with charachange

ha "¿Hmm? ¿Qué?"

show lilly basic_planned_paj_close
with charachange

"Hanako mira la habitación con sus ojos solamente medio abiertos, su mente muy distante de estar tan despierta como su cuerpo. Su aturdimiento nos hace reírnos entre dientes."

show lilly basic_planned_paj_close:
    ease 1.0 twoleft
with Pause(1.0)

show lilly basic_planned_paj at twoleft
with charadistant

"Mientras Lilly se levanta de la cama para atender a Hanako, doy una última mirada al cuarto."

hi "Creo que ya debo marcharme, entonces. Surgirán preguntas si me ven salir de los dormitorios de chicas por la mañana."

show lilly basic_smile_paj
with charachange

li "Adiós, Hisao."

show hanagown smile
with charachange

ha "Oh… adiós."

"Me levanto y camino hacia la puerta, tomando mi mochila un poco más ligera en el camino."

scene bg school_girlsdormhall
with locationchange

"Sin embargo, después de salir del cuarto y entrar al pasillo, oigo los pasos de Lilly detrás de mí."

hi "¿Hmm? ¿Qué pasó?"

show lilly basic_smileclosed_paj_close:
    yalign 1.0 xpos 0.3 xanchor 0.5
    easein 1.0 xpos 0.5
with Dissolve(1.0)

"Sin decir nada, ella se me acerca a largos pasos. Me congelo al sentir su mano deslizarse hasta mi mejilla, como si cada nervio recibiera la sensación de sus dedos y su palma sobre ellos."

play music music_romance

"Inmediatamente después, su rostro lentamente se acerca al mío, un toque momentáneo de sus labios rozando mi otra mejilla."

"Por un momento, todo parece detenerse. Llevo distraídamente mis dedos hasta mi mejilla, como para intentar recapturar aquella sensación efímera."

hi "Lilly…"

show lilly basic_smile_paj_close at center
with charachange

li "Ese es mi gracias, Hisao."

hi "¿Gracias…?"

show lilly basic_cheerful_paj_close
with charachange

li "Por tu regalo. Que tengas buen día en la escuela."

show lilly basic_cheerful_paj_close:
    easeout 1.0 xpos 0.3 alpha 0.0
with Pause(1.0)

hide lilly
with None

"Y con eso, desaparece tras la puerta y la cierra lentamente, las voces amortiguadas de ella y de Hanako aún audibles, justo como anoche."

"…"

"… Creo que sería difícil no tener un buen día, después de eso."

show bg school_courtyard
with locationskip

"Me alejo con cierto brinco en mis pasos. Creo que hubo algunas personas que me miraron de reojo al salir del edificio de los dormitorios de chicas, pero encuentro difícil preocuparme por eso."

stop music fadeout 2.0

scene black
with dissolve



label es_L6i:

scene black
with None

mi "Hicchan~."

hi "Vete."

mi "Hicchan~."

hi "Déjame solo."

mi "Vamos, Hicchan~."

hi "Hmph, déjame dormir."

"Después de dos noches de no haber podido dormir en absoluto, lo último que quiero es ser despertado cuando al fin logro hacerlo."

"Puede que sea el último periodo de clases, y que use un libro de texto como almohada, pero en este punto acepto cualquier tipo de sueño que haya."

mi "¡Mira Hicchan, hasta Shicchan quiere que te levantes~!"

"No me importa lo que quiera Shizune, déjenme solo."

mi "Cielos, Hicchan, simplemente tendré que despertar…"

"Espera, ¿Misha va a…?"

mi "… te…"

"¡Esto será malo!"

play music music_running

scene bg school_scienceroom
show misha hips_grin_close at center
with vpunch

hi "¡ESTOY DESPIERTO!, ¡ESTOY DESPIERTO! NO TIENES… que…"

"Puedo sentir mi rostro adoptando un fuerte rubor escarlata."

"Los estudiantes aún en clase están sentados completamente derechos y mirando al necio gritón que estaba durmiendo hace solo algunos momentos."

hi "… Maldición."

play sound sfx_impact2
with vpunch

"Dejo caer mi cabeza directamente sobre la mesa con un notorio golpe."

show misha cross_laugh_close
with charachange

mi "¡Guajajajajaja~!"

"La risa descontrolada típica de Misha resuena por el salón."

show shizu invis behind misha:
    center
    xpos 0.95
with None

show misha hips_grin_close at twoleft
show shizu adjust_happy at tworight
show bg school_scienceroom at bgleft
with dissolvecharamove

"Cuando giro mis afligidos ojos hacia la Shizune anteojuda a su lado, ella ajusta sus lentes, tratando desesperadamente de mantener una expresión de desaprobación seria."

"Estrechando mis ojos, puedo ver la sonrisa mal oculta que se dibuja por su rostro."

hi "¿Y tú también, Shizune?"

show shizu behind_blank
with Dissolve(0.3)

"Shizune mira hacia otro lado rápidamente mientras cruza sus brazos con firmeza, apenas al límite de mantener su control."

show misha cross_laugh_close
with charachange

mi "¡Guajajajajajaja~!"

"La risa de Misha se duplica en volumen cuando mira a Shizune. Lo único que puedo hacer es arrastrar mi mano sobre mi rostro resignándome."

hi "Ustedes dos…"

show misha sign_smile_close
with charachange

mi "¿Quién era el que dormía en clase, Hicchan~?"

hi "Sí, sí, era yo."

show misha hips_frown_close
with charachange

mi "La pobre Shicchan tenía un ataque intentando despertarte. ¿Verdad?"

show shizu basic_angry
with charachange

"Vuelvo mis ojos hacia la intratable Shizune, quien con un solo resoplido de confirmación vuelve a apartar la mirada con sus brazos cruzados."

hi "¿Por qué Shizune intentaba despertarme?"

show misha hips_smile_close
with charachange

mi "Shicchan quería darte las guías que el maestro substituto nos pasó mientras Hicchan estaba dormido."

hi "¿Guías?"

play sound sfx_paper
show shizu behind_frown_close
show misha hips_frown_close
show blanknote at truecenter
with vpunch

"De pronto encuentro dos hojas de papel arrojadas frente a mi rostro."

show blanknote at Transform(xpos=0.3)
with charamove

"Siguiendo la mano que las sostiene, veo la figura aún enfadada mirándome frunciendo el ceño de forma marcada. Supongo que de verdad soy yo el que está mal aquí."

hi "… Ah. Em, lo siento por eso."

stop music fadeout 8.0

"No funciona. Su rostro irritado aún persiste. Junto mis manos y agacho bruscamente mi cabeza como señal de disculpa."

hi "Lo siento mucho, mucho."

show shizu behind_frustrated_close
with charachange

show blanknote:
    easeout 0.5 ypos 0.8 alpha 0.0
with Pause(0.5)

hide blanknote
with None

"Ella resopla y simplemente deja caer los papeles sobre el banco."

hi "Maldición."

show shizu adjust_angry_close
show misha sign_smile_close
with charachange

"Miro sobre mis manos para ver a Shizune y a Misha haciéndose señas frenéticamente entre ellas, una expresión de frustración en el rostro de Shizune."

show shizu basic_angry_close
with charachange

shi "¡…!"

"Parece menos un diálogo y más una ataque interrumpido por miradas laterales hacia mí. Decir que es inquietante es quedarse corto."

hi "Em…"

show shizu behind_frown_close
show misha hips_frown_close
with Dissolve(0.3)

"Las dos de pronto dejan de hacer señas y me miran al mismo tiempo, ambas con exactamente la misma expresión de desaprobación. En un único movimiento fluido, las manos de Misha de pronto se extienden muy por sobre mí y bajan disparadas."

scene black
with None

play sound sfx_impact2
play music music_running

"Antes de poder siquiera esperar reaccionar, mi cabeza queda rebotando como una caja sorpresa." with vpunch

"Rápidamente pongo mis manos en mi cabeza, más por reflejo que por dolor verdadero."

hi "¡Au! ¿¡Por qué fue eso!?"

scene bg school_scienceroom at bgleft
show shizu adjust_smug_close at tworight
show misha hips_grin_close at twoleft
with openeye

"Abro los ojos para verlas a las dos sonriéndose entre sí mientras intercambian pulgares arriba entusiasmadamente."

show misha hips_smile_close
show shizu behind_smile_close
with charachange

mi "¡Shicchan dice que ahora te perdona, Hicchan~!"

hi "¿Podrías perdonarme con un poco menos de fuerza la próxima vez?"

show misha cross_laugh_close
with charachange

mi "¡Guajajajaja~!"

"Las miro sin mostrar expresión en el rostro. Misha y Shizune: uno, Hisao: nada."

show shizu adjust_happy_close
with charachange

shi "…"

show misha hips_grin_close
with charachange

mi "¡Oh, Shicchan también dice que deberías revisar tu correo de estudiante más a menudo~!"

show letter_insert:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"Ella saca un sobre amarillo brillante y me lo entrega con una sonrisa exuberante."

"Qué extraño. ¿Quién podría haberme escrito una carta? Aunque ahora no es el momento y definitivamente no es el lugar para enterarme."

show letter_insert:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide letter_insert
with None

"Desistiendo de la siesta que me fue arrebatada tan cruelmente, froto mi frente y lentamente me levanto, poniendo las hojas y el sobre en mi mochila antes de tirarla sobre mi hombro."

show misha cross_laugh at Transform(yalign=1.0, xanchor=0.5, xpos=0.355)
show shizu behind_smile at Transform(yalign=1.0, xanchor=0.5, xpos=0.615)
with charadistant

"Doy un paso hacia atrás y me muevo para retirarme con una pequeña reverencia, mientras Misha sostiene sus costados por la risa y Shizune responde asintiendo con una despedida cortante."

stop music fadeout 3.0
play ambient sfx_crowd_indoors fadein 0.5

scene bg school_hallway3
show crowd
with locationchange

"Me uno al flujo de estudiantes saliendo por la puerta abierta, y doy la vuelta hacia el pasillo."

$ renpy.music.set_volume(0.7, 0.5, channel="ambient")

show hanako emb_downtimid at center
with charaenter

"… Para encontrarme cara a cara con Hanako."

hi "Guah. Eh, hola Hanako."

show hanako emb_timid
with charachange

ha "Buenas tardes… Hisao."

show hanako emb_downtimid
with charachange

"Ambos quedamos en silencio mientras estudiantes parlanchines pasan a nuestro alrededor. Ella se mueve inquieta constantemente, sus ojos atraídos por su particularmente común calzado."

"Tomo el caballete de mi nariz con mis dedos mientras pestañeo con fuerza en un intento de hacer que las cosas se vean más claras. Apenas me estoy manteniendo despierto tal como estoy."

hi "Hanako, quieres decir algo. ¿Qué es?"

show hanako emb_blushing
with charachange

ha "A-ah… Quería… darte esto…"

hi "¿Hmm?"

show hanako basic_worry
with charachange

"Ella extiende un pequeño trozo rectangular de papel. Vuelvo a parpadear para poder distinguir el texto a través de mis ojos apenas abiertos, lentamente comenzando a distinguir lo que está escrito."

window hide

$ written_note(u"\nHuevos x2\nPan x1\nCereal integral x1\nTomillo x1\n")

window show

play music music_happiness fadein 0.5

hi "… ¿Una lista de compras?"

"Subo la mirada, levantando una ceja."

show hanako emb_timid
with charachange

ha "Usualmente voy de compras con Lilly pero no puedo ir ahora, entonces…"

hi "¿Quieres que haga un recado por ti?"

show hanako defarms_shock
with charachange

ha "¡E-está bien si no quieres hacerlo! Solo pensé que, quizás, em…"

"Está entrando en pánico. Suspiro. Otra batalla perdida, aunque esta vez fue una rendición poco peleada."

"Sonrío, cansado, y apoyo una mano sobre su cabeza para tranquilizarla."

hi "Está bien, iba a ir de todas formas. ¿Solo lo de esta lista?"

show hanako def_worry
with charachange

"Ella asiente y luego hace una reverencia pronunciada, dos veces, como para dejar perfectamente en clara su gratitud."

show hanako cover_distant
with charachange

ha "Í-íbamos a reunirnos fuera del portón de la escuela a las seis… gracias, iba a ir yo, pero necesito estudiar para el examen de mañana."

hi "¿Examen? Ah, cierto, ciencias. ¿Cómo te está yendo con eso?"

show hanako cover_bashful
with charachange

"Ella se anima solo un poquito."

show hanako basic_bashful
with charachange

ha "Le he estado… dedicando más tiempo que antes. Creo que estaré… bien."

hi "Buen trabajo, entonces."

show hanako basic_smile
with charachange

"Ella también comienza a sonreír, y mucho más honestamente que yo."

"Tengo plena confianza en que puede irme bien sin estudiar extra, pero el hecho de que ella le esté poniendo esfuerzo en lugar de solo leer en la biblioteca es alentador."

hi "Compraré tus cosas y las llevaré a tu dormitorio en la tarde. Nos vemos."

stop music fadeout 3.0
$ renpy.music.set_volume(1.0, 3.0, channel="ambient")

hide hanako
with charaexit

"Despidiéndonos con las manos, nos separamos."

"Iré a hacer mi tarea antes de encontrarme con Lilly. Debería ser capaz de encargarme de ello a tiempo."

stop ambient fadeout 1.0

scene bg school_gate_ss
with shorttimeskip

play music music_soothing fadein 2.0

"Luchar contra un problema de matemáticas particularmente complicado me ha atrasado un poco en mi encuentro con Lilly."

"Solo un par de minutos, pero suficiente para hacerme caminar cautelosamente en el patio hacia el portón de la escuela."

scene bg school_road_ss
with locationchange

"Giro a la derecha y voy hacia el pequeño pueblo ahí abajo, dejando unos estudiantes girando hacia el otro lado para ir a la estación de autobuses."

"Pongo mi mano derecha en mi bolsillo mientras camino bajo la luz anaranjada del atardecer."

"Afortunadamente el calor sofocante del verano ha comenzado a disminuir, dando paso a una agradable brisa fresca."

show lilly back_listen_ss at center
show lillyprop back_cane_ss at center
with charaenter

"Cuando estiro mis manos sobre mi cabeza, una figura familiar toma forma, un bastón en su mano derecha."

hi "Ah, Lilly."

show lilly cane_listen_ss
hide lillyprop
with charachange

"Ella se detiene y da la vuelta, girando su cabeza un poco para intentar distinguir de dónde exactamente vino la voz."

hi "Qué tal. Soy yo."

"Rápidamente la alcanzo, llegando a su costado e igualando su lento paso mientras continuamos caminando."

show lilly cane_smile_ss
with charachange

li "Buenas tardes, Hisao."

hi "Hola."

scene bg misc_sky_ss at Fullpan(10.0, dir="right")
with locationchange

"Alzo la mirada al cielo."

"Un matiz distinto de naranja decolora las nubes, bañando el sendero con su luz. Largas sombras de los árboles caen, cruzando el ancho camino que baja la colina."

scene bg school_road_ss
show lilly cane_smileclosed_ss
with charachange

li "Entonces Hisao, ¿qué te trae por aquí?"

hi "Solo iba al pueblo a comprar algunos comestibles. Hanako me mandó."

show lilly cane_surprised_ss
with charachange

li "¿Hanako te mandó?"

hi "Sí, dijo que necesitaba estudiar para el examen de mañana. Yo iba a venir de todas formas, así que solo compraré sus cosas también."

"Queda sobreentendido que Lilly de verdad necesita algo de ayuda para conseguir la comida, pero es un hecho obvio que ninguno de los dos necesita mencionar."

show lilly cane_weaksmile_ss
with charachange

li "Es bueno saber que está estudiando para ello."

hi "Pensé lo mismo cuando me pidió que viniera contigo."

hide lilly
with charaexit

"Seguimos bajando por la calle, el sonido conocido de su bastón haciendo eco en el aire mientras caminamos. Excepto por el auto ocasional y las hojas susurrando en las ramas, hay un silencio maravilloso."

"Gracias a Dios que por fin puedo relajarme por primera vez hoy."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene evbg lilly_sunsetwalk:
    truecenter subpixel True zoom 0.9
    acdc_warp 20.0 zoom 1.0
show evfg lilly_sunsetwalk:
    truecenter subpixel True zoom 0.85
    acdc_warp 20.0 zoom 1.0
with locationskip

"Miro de reojo a Lilly."

"A ese rostro de porcelana suyo nunca parece faltarle ese aire de confianza relajada. Supongo que lo mismo podría decirse también de su personalidad."

"Mientras camina en silencio, su rostro dirigido hacia la calle frente a ella, yo miro hacia adelante y disfruto del aire fresco soplando sobre mi cara."

"Este es probablemente el momento más tranquilo que he tenido desde el giro repentino que mi vida tomó hace poco."

"Tenerlo mientras camino a comprar comestibles. Qué vida más rara."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

scene bg school_road_ss
with locationskip

"Siento el papel arrugado rozando contra mi mano en mi bolsillo, y lo saco para revisar su contenido."

hi "Veamos… huevos, pan, cereal, tomillo, lechuga, jamón laminado…"

show lilly cane_weaksmile_ss
with charaenter

li "Eso suena como bastante para llevar junto con lo tuyo."

hi "Cierto. ¿Cuánto come esta chica de todas formas?"

"Mi mente de pronto cae en cuenta de que sí, de hecho hay una persona junto a mí."

hi "E-espera, quiero decir…"

show lilly cane_giggle_ss
with charachange

"Ella se ríe de todo corazón."

show lilly cane_planned_ss
with charachange

li "Vaya vaya, Hisao."

"Sus risitas acentúan sus palabras, aunque no está poniendo mucho esfuerzo para reprimirlas."

show lilly cane_satisfied_ss
with charachange

li "Bastante directo hoy, ¿no es así?"

hi "Sí, tienes razón. De todas formas, es mucha comida."

show lilly cane_smileclosed_ss
with charachange

li "Suelo ir de compras con Hanako, así que sé lo que compra. Siempre es lo mismo todas las semanas."

hi "Eh. ¿Cocina bien?"

show lilly cane_weaksmile_ss
with charachange

"Ella se ríe nerviosamente."

li "Usualmente soy yo quien termina cocinando. Solía hacerlo por Akira, así que no hay problema en hacerlo por Hanako también."

hi "¿Puedes cocinar? Pero…"

show lilly cane_cheerful_ss
with charachange

"Un breve tarareo con un ritmo divertido emana de mi lado."

"Me pregunto si el hecho de que ella parezca divertida por mis comentarios tan a menudo es en verdad genuino, o si es simplemente por querer hacerme sentir más cómodo al referirme a su ceguera."

show lilly cane_smileclosed_ss
with charachange

li "Hay formas de lidiar con ello. Algunos platos son más difíciles de cocinar que otros por no poder ver lo que estoy haciendo, pero usualmente solo me toma un poco más de tiempo."
li "Los dedos también sirven como herramientas de medida bastante útiles, por ejemplo."

"Tiene sentido, pero tendría que ser bastante cuidadosa de no lastimarse a sí misma. Me pregunto cuántas veces habrá ocurrido eso, dado que parece que ha cocinado sola posiblemente durante años mientras Akira trabajaba y sus padres no estaban."

"Con eso, la conversación se acaba."

"Comparado con los silencios incómodos de Hanako, Lilly parece sinceramente contenta con decir lo que piensa y permanecer callada cuando no hay nada que decir."

"El camino escurridizo bajo mis pies está bañado por un brillo anaranjado, de vez en cuando una hoja caída crujiendo bajo los pies mientras caminamos. Suelto un bostezo, mi falta de sueño volviendo a atormentarme."

show lilly cane_smile_ss
with charachange

li "¿No dormiste mucho anoche?"

hi "No he podido dormir nada de nada estas últimas dos noches. Probablemente insomnio."

stop music fadeout 8.0

show lilly cane_oops_ss
with charachange

"El rostro de Lilly de pronto parece preocupado. Se siente como una derrota personal cada vez que ella se preocupa por mi bienestar, aunque sí es agradable saber que alguien se preocupa."

li "¿Tienes insomnio? ¿No irás al enfermero por eso?"

hi "Nah, no hace falta. Ha pasado antes unas cuantas veces. Mis medicamentos fastidian mi sueño de vez en cuando."

show lilly cane_concerned_ss
with charachange

li "… Ah. Lo… lamento."

hi "Vamos, no es tu culpa. Por lo menos no debería tener problemas para dormirme esta noche."

show lilly cane_sleepy_ss
with charachange

li "Me preocupas a veces."

hi "¿Te… preocupo?"

"Extiendo mi brazo y me rasco la nuca. Quiero en parte tratar esto."

hi "Oye, Lilly…"

show lilly cane_smile_ss
with charachange

li "¿Hmm?"

hi "No quiero sonar raro, pero… por favor intenta olvidarte de mi problema cardiaco."

show lilly cane_oops_ss
with charachange

"Ella parece un tanto confusa. No puedo culparla."

hi "Creo que lo que quiero decir es… solo que no me trates diferente por eso."

show lilly cane_emb_ss
with charachange

"Ella hace una pequeña reverencia con su cabeza, sus blancas mejillas sonrojándose casi imperceptiblemente."

li "Es natural preocuparse de quienes te rodean…"

hi "Bueno, de todas formas es agradable saber que hay alguien así en el mundo."

show lilly cane_smileclosed_ss
with charachange

"Puede ser algo vergonzoso decirlo, pero es la verdad. Lilly da un respiro para recuperar la compostura y logra adoptar una amable sonrisa, aunque sus mejillas siguen rojas."

"La caminata colina abajo que queda hasta la tienda transcurre en silencio."

scene bg suburb_konbiniint
with shorttimeskip

play music music_daily fadein 4.0

"Cajera" "¡Bienvenidos!"

hi "Supongo que tomaré mis cosas primero y las de Hanako en la segunda ronda."

show lilly cane_smileclosed at center
with charaenter

"Tomo dos canastas desgastadas rojas de una pila junto a la entrada y le paso una a Lilly."

show lilly cane_smileclosed at Transform(ypos=800)
with charamove

show lilly basic_smileclosed at Transform(ypos=800)
with charachange

show lilly basic_smileclosed at center
with charamove

"Justo como antes, ella la pone en el suelo y desliza su bastón retraído entre las manillas del canasto antes de volver a agarrarla con su mano derecha."

$ renpy.music.set_volume(0.5, 0.5, channel="music")

show lilly basic_smileclosed at Slide(0.5,0.5,0.3,0.5,1.0, time_warp=_ease_time_warp)
with None

show lilly basic_smileclosed_close at Slide(0.5,0.5,0.3,0.5,1.0, time_warp=_ease_time_warp)
with Dissolve(1.0)

"Cuando ella toma mi brazo con el suyo, me sorprende lo rápido que este tipo de contacto casual se ha vuelto natural. Más que nada por necesidad, me imagino."

show lilly basic_smile_close at twoleft
with charachange

li "¿Comenzamos?"

$ renpy.music.set_volume(1.0, 2.0, channel="music")

hi "Claro."

"Mientras recorremos la tienda, ninguna de las otras personas pasando por los pasillos parece prestarnos nada de atención. Es agradable, comparado con las miradas y susurros en la ciudad."

show lilly basic_smileclosed_close
with charachange

"Cuando llegamos a cada pasillo, rápidamente repaso con Lilly lo que ella necesita y lo tomo junto con lo que yo quiero, colocando los objetos en nuestras canastas respectivas."

"Se siente extraño, que uno dependa tanto de otra persona para algo tan básico como ir de compras. Hanako sería prácticamente una necesidad para que ella tome lo que quiere, después de todo."

hi "Bueno, ya prácticamente he terminado con lo mío y lo de Hanako. ¿Necesitas algo más, Lilly?"

show lilly basic_smile_close
with charachange

li "No, eso sería todo."

hi "Entonces nos marchamos."

"Curiosamente, hay una fila como de un kilómetro. Considerando que la tienda solo es lo bastante grande para necesitar un mostrador, parece que esto se tardará."

hi "Maldición."

show lilly basic_surprised_close
with charachange

"Lilly pone una expresión de curiosidad, incapaz de ver el motivo de mi queja."

hi "La fila es muy larga. Parece que tendremos que esperar."

show lilly basic_weaksmile_close
with charachange

li "Qué raro."

"Compartiendo el mismo sentido de resignación, a regañadientes tomamos lugar al final de la fila."

$ renpy.music.set_volume(0.5, 10.0, channel="music")

"Una persona termina, la fila avanza. Otra persona termina, la fila avanza."

"Para cuando finalmente llegamos al comienzo de la fila, estoy tan cerca de dormirme que Lilly tiene que palmearme suavemente en la espalda para que avance."

show lilly basic_oops_close
with charachange

li "¡Hisao… Hisao!"

$ renpy.music.set_volume(1.0, 0.3, channel="music")

hi "¿Hmm? Ah, lo siento."

show lilly basic_displeased_close
with charachange

"Ella suspira consternada mientras avanzo, dejando la mercadería de Hanako y la mía en bolsas separadas."

"Cajera" "¡Gracias, por favor vuelvan pronto!"

stop music fadeout 5.0

scene bg suburb_konbiniext_ni
show lilly basic_smileclosed_ni
with locationskip

"Ya cuando salimos de la tienda, Lilly está sosteniendo una sola bolsa mientras yo lucho con llevar cuatro, ambas manos verdaderamente llenas. Es mucho trabajo, pero afortunadamente los objetos en ellas no pesan mucho."

"Aun sin mirar hacia el cielo, es obvio que ha pasado una cantidad sorprendente de tiempo; el camino afuera está a oscuras e iluminado por los faroles."

show lilly cane_smile_ni
with charachange

"Una vez que Lilly saca su bastón, andamos hacia los dormitorios por donde vinimos, abandonando el brillo cálido y acogedor de la tienda."

scene bg school_road_ni
with locationskip

play music music_dreamy fadein 8.0

"A pesar de que el camino está vacío, las bolsas llenas compensan la falta de ruido, chirriando y golpeteando entre ellas."

show lilly cane_ara_ni
with charaenter

li "Vaya vaya, Hisao, es bueno saber que estás alimentándote bien."

hi "¡Soy un chico en crecimiento después de todo, necesito comer todo lo que pueda!"

show lilly cane_weaksmile_ni
with charachange

li "Hmm… debe ser agradable, ser hombre."

hi "¿Q-qué?"

"Aparentemente sin notarlo, o ignorando, mi sorpresa ante el comentario completamente inesperado, ella continúa sin pausa."

show lilly cane_smile_ni
with charachange

li "Tu peso en realidad no te preocupa cuando comes, la mayor parte del tiempo."

hi "Entiendo lo que quieres decir. Las mujeres tienden a preocuparse de cosas como esas más que nosotros, supongo."

show lilly cane_smileclosed_ni
with charachange

li "Exactamente. Me da un poco de envidia, para serte honesta."

hi "Bueno, no es como si pudiéramos ignorarlo completamente."

"Asintiendo afirmativamente, seguimos caminando."

hi "Oh, es cierto."

show lilly cane_smile_ni
with charachange

li "¿Qué pasó?"

hi "Hanako mencionó que tu cumpleaños fue antes este año. ¿Hiciste algo especial?"

show lilly cane_listen_ni
with charachange

"Ella se toma una larga pausa, reflexionando por unos cuantos segundos mientras recuerda el evento."

show lilly cane_weaksmile_ni
with charachange

li "No, en realidad. Hanako y yo solo tuvimos una pequeña fiesta durante la noche después de las clases."

hi "Se supone que tu cumpleaños debe ser un acontecimiento importante, sabes."

"Suena como una forma bastante solitaria de pasar un cumpleaños, solo ella y Hanako pasando la noche juntas."

"Para mí los cumpleaños siempre se han sentido como acontecimientos familiares. Eran ocasiones donde, a pesar de sus trabajos de tiempo completo, mis padres hacían el esfuerzo de estar ahí por el día o al menos para una fiesta de antemano."

"Me recuerda de cuando Lilly mencionó que no ha visto a su familia desde hace tanto tiempo, e incluso terminó mudándose lejos de la casa de Akira después."

"Pero supongo que es lo mismo en situaciones tan comunes como estas. Considerando su incapacidad para leer los envoltorios, tan solo comprar comestibles sería una molestia sin alguien más a su alrededor."

"En fin, ella solamente nos tiene a mí y a Hanako, y a Akira cuando no está trabajando."

"Sea como sea, ella aún parece tener muchos más amigos distantes entre los estudiantes, sin mencionar gente como Yuuko."

"Parece ser decisión propia que haya tal separación entre aquellos que son cercanos a ella, y aquellos con los que simplemente socializa."

"Me impresiona un poco ver lo mucho que Lilly parece haber asentado su vida y que esta vaya tal como ella quiere."

"Y sin embargo Hanako está ahí por ella para celebrar su cumpleaños, y yo estoy aquí ayudándola con sus compras. Es una simbiosis medio extraña, supongo."

show lilly cane_oops_ni
with charachange

li "¿Estás bien, Hisao?"

hi "¿Disculpa?"

li "Parecías haberte quedado en silencio, eso es todo."

hi "Ah, lo siento. Solo estaba pensando."

show lilly cane_smileclosed_ni
with charachange

li "¿Oh?"

label es_choiceL6_1:
menu:
    with menueffect
    "Ah, ahora he incitado su curiosidad. Aunque se siente tal vez demasiado personal hablar de ello…"
    "Evitar el tema.":


        return m1
    "Decir la verdad.":

        return m2

label es_L6a:


hi "Solo pensaba en algunas de las cosas que han pasado. No te preocupes."

stop music fadeout 2.0

show lilly cane_listen_close_ni
with characlose

li "¿Hmm?"

"Ella se inclina aún más hacia mí, forzándome a moverme a un costado."

hi "Vamos, ¿tú nunca haces eso también?"

show lilly cane_cheerful_close_ni
with charadistant

li "Lo haces sonar como si ocultaras algo…"

play music music_lilly fadein 4.0

"Erk. ¿Por qué esta chica tiene que ser tan perceptiva?"

"Aunque, mirando de reojo su rostro, ella tiene una sonrisa juguetona y linda."

"Ella está… ¿jugando conmigo? Aun así, preferiría no continuar este tema con ella."

hi "Ya te dije, no es nada."

show lilly cane_displeased_close_ni
with charachange

"Lilly frunce el ceño en desaprobación."

li "¿Oh no?"

hi "Así es."

show lilly cane_surprised_close_ni
with charachange

li "No sabes mentir, Hisao."

hi "Es cierto, pero es por eso que no estoy mintiendo. Soy una persona muy confiable."

show lilly cane_weaksmile_close_ni
with charachange

li "Me imagino que sí. Aunque creo que puedo perdonarte esta vez nada más."

hi "¿Perdonarme? ¿Por qué, exactamente?"

show lilly cane_giggle_close_ni
with charachange

with Pause(0.2)

show lilly cane_smile_ni
with charadistant

"Ella se ríe un poco antes de seguir caminando en silencio. ¿En qué estará pensando?"

stop music fadeout 4.0

"Alzo la mirada al oscuro cielo mientras dejo caer mis hombros."

"Pienso que esto es algo que debo arreglar por mí mismo, en lugar de confiar en ella para todo."

label es_L6b:


hi "Es solo que… Estaba pensando en cómo pareces tener todo tan ordenado, incluso con Hanako contando contigo. Puedo admitir que hasta yo conté contigo un poco cuando llegué."

hi "Creo que es una buena cualidad para tener."

"Me doy vuelta hacia Lilly, observando su reacción."

stop music fadeout 2.0

show lilly cane_listen_close_ni
with characlose

"Ella se está forzando a mirar hacia adelante y está frunciendo el ceño bastante. Su rostro se ve un tanto extraño, como si intentara encontrar las palabras correctas."

hi "… ¿Lilly?"

show lilly cane_weaksmile_close_ni
with charachange

li "Te lo agradecería, pero… asumir que yo no cuento con la presencia de otros es demasiado. Te equivocarías si pensaras que Hanako depende de mí sin recibir nada a cambio."

"Parece que le cuesta admitir esto, a pesar de que sea mayormente lo que yo ya pensaba."

"Si ella ha intentado tanto mantener su independencia, como cualquiera en su posición, con o sin visión, quizás para ella es difícil hablar de sus propias necesidades."

"De repente me doy cuenta de una omisión en lo que ella dice. Decido mencionarla, principalmente como broma, para evitar que las cosas se pongan muy personales."

hi "¿Oh? ¿Y qué hay de mí?"

play music music_lilly fadein 2.0

show lilly cane_smile_ni
with charadistant

"Ella de pronto corre delante de mí y se da la vuelta, bloqueándome el paso."

show lilly behind_cheerful_ni
with charachange

"Con una sonrisa, ella junta sus manos mientras se inclina hacia adelante."

li "Tú eres diferente."

show lilly back_giggle_ni
show lillyprop back_cane_ni
with charachange

"Y con eso, ella se da la vuelta y continúa caminando enfrente de mí, con una energía renovada en su andar."

"Todo lo que puedo hacer es levantar una ceja y darle una sonrisa deslumbrada. No creo que haya visto este lado juguetón y coqueto de ella antes."

"Entonces… Soy “diferente”. Es difícil distinguir el contexto exacto, pero conociéndola, esta ambigüedad es intencional."

"Nuestra relación ha estado cambiando, por lo menos simplemente porque he comenzado a valerme por mí mismo más y he comenzado a sentir más curiosidad por la situación de quienes me rodean."

"Con respecto al porqué… probablemente una mezcla de curiosidad personal, y un deseo de intentar aprender cómo lidiar con mi situación."

"Sin embargo, estoy menos seguro de Lilly. Es por eso que su declaración, tan similar a mis propios sentimientos hacia ella, baja tanto mi guardia."

"Viéndola avanzar calle arriba, su bastón golpeando de izquierda a derecha, decido zanjar el tema después, y simplemente sonrío. Este lado de ella es agradable, y no quiero olvidarlo."

stop music fadeout 2.0

label es_L6c:


scene bg school_girlsdormhall
with shorttimeskip

play music music_normal fadein 4.0

"Eventualmente llegamos a los dormitorios de chicas, ambos brazos adoloridos por el peso de dos conjuntos de mercadería."

hi "Hah… al fin hemos llegado. Uf."

show lilly invis:
    right
    xpos 0.95
with None

show lilly cane_smileclosed at right
with dissolvecharamove

"Me agacho para limpiar mi frente con la parte de atrás de mi mano. Lilly se detiene frente a su puerta y baja su bolsa, buscando la llave en su bolsillo."

show lilly cane_smile
with charachange

li "Gracias, Hisao. De verdad agradezco tu ayuda."

hi "Ah, no es la gran cosa."

show lilly cane_smileclosed
with charachange

li "Podrá no ser la gran cosa para ti, pero… definitivamente es algo para mí."

show lilly invis:
    right
    xpos 1.05
with dissolvecharamove

play sound sfx_doorclose

hide lilly
with None

"Y con eso, ella cruza la puerta, cerrándola detrás de ella."

"Pestañeo. Eso no fue más que un agradecimiento sincero, pero no puedo evitar sentir algo distinto con respecto a ello."

"De todas formas, tengo algo más que hacer antes de poder reflexionar tranquilamente sobre eso."

scene bg school_dormhanako_ni
show hanako emb_timid_close:
    center
    xpos 0.45
show hanako_door_base at right
show hanako_door_door at left
with locationchange

play sound sfx_doorknock2

"Doy la vuelta hacia el cuarto de Hanako y procedo a golpear dos veces en rápida sucesión, las bolsas en mi mano crujiendo juntas."

play sound sfx_dooropen

show hanako_door_door:
    xpos -0.05
with charamove

"Después de unos segundos, la puerta se abre lentamente. Si uno no mirara de cerca, sería entendible pensar que no se había movido en absoluto."

"Giro mi cabeza hacia el lado para intentar mirar a través de la rendija diminuta entre la puerta y el marco."

hi "Oye Hanako, tengo tus cosas."

show hanako basic_normal_close at Position(xpos=0.4)
with charachange

ha "¡Ah!"

show hanako_door_door:
    xpos -0.3
show bg school_dormhanako
with dissolvecharamove

"Con eso, ella abre la puerta completamente, haciendo su cuarto visible por sobre sus hombros. Escasamente decorado, probablemente sea incluso más común que mi propio cuarto."

"Extiendo mi brazo derecho, ambas bolsas casi tirándolo de vuelta hacia abajo con su peso."

show hanako emb_smile_close
with charachange

ha "G-gracias, Hisao."

show hanako emb_downtimid_close
with charachange

ha "Disculpa por hacerte… cargarlas todo el camino."

hi "Está bien, no te preocupes. Solo no me hagas hacerlo todos los días, ¿de acuerdo?"

show hanako basic_normal_close
with charachange

"Le paso las bolsas mientras le doy una risita entre dientes. Después del traspaso inicial de peso, ella logra cargarlas fácilmente."

hi "Entonces me marcho. Buenas noches, Hanako."

show hanako cover_bashful_close
with charachange

ha "Buenas noches. Em, n-nos vemos en clases… mañana…"

show hanako_door_door at left
with charamove

play sound sfx_doorclose

"Con una reverencia marcada y sus comestibles aún en ambas manos, ella da un paso atrás y cierra la puerta."

stop music fadeout 5.0

scene bg school_dormext_full_ni
with locationskip

"Regresando a mi propio dormitorio, coloco una bolsa en mi otra mano para balancearlas."

"Incluso ahora que hago esto, no puedo sacarme la sonrisa alegre de Lilly de mi mente. Cuando la conocí, habría sido casi imposible imaginármela así."

"En efecto, se siente como si nos hubiéramos vuelto más cercanos en las últimas semanas desde que conocí por primera vez a ella y a Hanako."

"El tiempo que paso con ella cada día. Los pequeños intercambios de felicidad que compartimos. Aquellos pequeños momentos de alegría a medida que me acerco a ella."

"Aún no estoy seguro, pero no creo que estos sean simplemente sentimientos normales de amistad."

scene bg school_dormhisao
with locationskip

"Una vez que regreso a mi cuarto, guardo lo que compré y comienzo a prepararme para la noche."

show letter_insert:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"Reemplazo los libros de texto en mi mochila por los que necesitaré mañana, sacando en el proceso el sobre amarillo que Misha me dio antes."

"Me distraje tanto con una cosa tras otra que no pude verla antes. ¿Me pregunto quién podría haberme escrito?"

"El nombre prolijamente adornando al reverso del sobre me detiene por completo. Ha pasado tanto tiempo desde que vi su letra, que no hay muchas posibilidades de que pudiera identificarla como suya de otra forma."

"“Iwanako”."

"¿Por qué… me podrá haber escrito? No puedo pensar en ningún buen motivo para hacer esto."

"Casi no abro la carta, pero eso no tiene mucho sentido. Si simplemente la dejara estar, su simple existencia me roería hasta que hiciera algo al respecto."

scene ev hisao_letter_open
with shorttimeskip

play music music_rain fadein 6.0

"Bajo la mirada al papel en mi escritorio, su brillante y veraniega decoración radiando alegremente hacia mí."

"Las letras están en rosado, desentonando fuertemente con el borde amarillo girasol de la tarjeta. La caligrafía es ordenada, los caracteres habiendo sido escritos con consideración y con una cantidad inusual de cuidado."

"Apenas le había prestado a la carta atención cuando me la dieron, pero ahora no puedo sacar su contenido de mi mente."

window hide
nvl clear
nvl show dissolve

n "\n\n\nAunque me gustaría decir que no sé por qué ella usó un método tan anticuado de comunicación, considerando que una llamada telefónica o un e-mail habría sido mucho más rápido y fácil, la respuesta se siente lo bastante obvia dado el contenido."

n "Una carta deja una distancia cómoda entre el remitente y el destinatario. A diferencia de un teléfono, no se requiere ninguna conversación, y a diferencia de un e-mail, hay menos expectativa de una respuesta inmediata."

n "\nAfirmaciones como “los ánimos entre los de tercer año parecen ser de muchas ansias por los exámenes finales”, y “es tan extraño pensar que ya estamos en el último año, ¿no es así?” son nada más que cháchara. Cháchara que podría haberse conseguido simplemente respondiendo a cualquiera de los mensajes que le envié cuando estaba en el hospital."

n "El final, sin embargo, es el motivo verdadero por el que envió esto. Las últimas líneas, añadidas casi como si fuera una idea de último momento."

nvl clear
nvl hide dissolve

play sound sfx_paper

scene ev hisao_letter_open_2
with locationchange

nvl show dissolve

n "\n\n\n\n\n\n\n“Me pregunto si nos encontraremos de nuevo. ¿Tal vez sea mejor si no?”"

n "Es una afirmación que debería doler. Siempre he escuchado que el terminar es cosa seria, pero se siente como si esto fuera simplemente una reafirmación de algo que ambos ya sabíamos."

n "Es el texto que lo antecede, no más que cháchara, lo que me hace sentir más inquieto. No puedo entender por qué, sin importar lo mucho que me siente aquí y mire a este trozo brillante y veraniego de papel."

nvl clear

n "\n\n\n\n\n\n\n\n“Si te gustaría mantener correspondencia conmigo, por supuesto que puedes escribirme de vuelta”."

n "Es claramente obvio que este no es el tipo de carta que uno respondería. Al final, esta carta no es más que una simple abdicación de responsabilidad; una afirmación final para asegurarse a sí misma de que nuestra relación se ha acabado."

stop music fadeout 3.0

nvl hide dissolve
nvl clear

scene bg school_dormhisao
with locationchange

window show

"Dicho eso, no tengo mayor dificultad para aplastar la carta y su sobre como bola y arrojarlos al basurero, librándome de su existencia."

"Me voy a la cama con sentimientos mezclados, privado de una tarde agradable por esta intrusa del pasado."

"Irónicamente, tardo un largo rato en lograr dormirme."

scene black
with dissolve

$ suppress_window_after_timeskip = True

label es_L7:

window hide None

scene black
with dissolve

nvl show dissolve

n "\n\n\n\nSudo copiosamente, esperando el momento aterrador."

$ renpy.music.set_volume(0.7, 0.0, channel="music")
play music music_tension fadein 6.0

n "Cada clic del reloj tensa mis músculos aún más, cada minuto que pasa poniéndome más pelos de punta."

n "Viene por mí, puedo sentirlo."

play sound sfx_slide

n "\n\n{image=vfx/reddash.png}{color=#FF0000}{b}La muerte.{/b}{/color}"

n "\n\nMuerte con la forma de una hoja de papel."

$ renpy.music.set_volume(1.0, 0.5, channel="music")

nvl clear
nvl hide dissolve

scene bg school_scienceroom at bgright
with locationchange

window show

"Recibo la pequeña pila de papeles del estudiante frente a mí y la paso hacia atrás después de sacar la hoja superior."

"Mirando la parte superior derecha de la página, veo mis miedos concretados dentro del pequeño círculo rojo."

stop music
play sound sfx_thunder
with vpunch

"Cuarenta y tres."

"Dejo caer mi cabeza y suspiro resignado. Maldiciendo por lo bajo, puedo sentir el aura de un sentimiento similar saliendo del grupo entero. Es extraño, pero ese hecho alivia mi ánimo una cantidad minúscula."

"A la miseria le agrada tener compañía, supongo."

"Cuando el maestro abre su boca, el cuarto entero se afirma ante el inevitable asalto…"

play music music_normal fadein 1.0

play sound sfx_normalbell

"… Solo para ser salvado en el último minuto."

"Rápidamente nos movemos a tomar nuestros bolsos y marcharnos a almorzar cuanto antes, pero el maestro suelta un ataque de despedida."

"Maestro" "Discutiremos los resultados del examen del grupo durante la próxima sesión. No creo que haga falta decir que será bastante larga la discusión."

"Un quejido colectivo suena por el grupo, ahora reducido a salir arrastrando los pies con desánimo."

scene bg school_hallway3 at bgright
with locationchange

"Coloco la hoja de papel en mi bolso mientras camino por el pasillo, arrugándolo en el proceso. Es suficiente que una carta tan problemática haya terminado en mi escritorio ayer, y ahora esto."

hi "Odio el inglés…"

stop music fadeout 0.7

mystery "¡HI—{w=0.3}SA—{w=0.3}O!"

"Una voz severa femenina me llama ásperamente por la espalda."

play music music_tension

"Me detengo, mi rostro volviéndose como piedra. Es como si pudiera sentir mi cerebro desconectándose de mi cuerpo."

"Mis ojos lentamente se mueven a la derecha, intentando vislumbrar el rastro de la voz incorpórea."

stop music fadeout 0.3

"… ¿Nada?"

"Mi rostro comienza a caer a medida que pasa el tiempo, y decido arriesgarme a girar la cabeza. Muy lentamente, la giro hacia—"

play sound sfx_impact

hi "¡GYAAAAH!" with vpunch

"Salto por los aires y suelto mi mochila, gritando de sorpresa."

"Cuando me recupero y recobro la compostura, me doy vuelta para ver… Debería haberlo sabido."

hi "Emi."

play music music_running

show emi excited_proud at center
with charaenter

emi "Te atrapé, Hisao."

"Ella está ahí parada con una sonrisa traviesa en su rostro, sus manos enfrente de ella con sus dedos apuntando hacia dentro. Ella fue la que pinchó mis costillas con sus dedos."

"La miro con una mueca, frotando mi cabello con frustración."

hi "Esa no es forma de saludar a alguien, sabes."

show emi sad_pout
with charachange

emi "No tienes sentido del humor."

hi "Dejé mi sentido del humor en mi clase de inglés. Quéjate con el maestro si quieres que me lo devuelvan."

show emi sad_shy
with charachange

"Ella pone sus mejores ojos de cachorrito mientras hace pucheros. Lilly ha logrado aumentar mi resistencia a esta táctica, pero la estatura baja de Emi le añade suficiente al efecto como para hacerme ceder."

hi "Entonces, ¿cómo van las cosas? Hace tiempo que no te veo."

show emi basic_closedgrin
with charachange

emi "Lo de siempre, lo de siempre. Corro tan rápido que nadie quiere acompañarme en mis corridas matutinas."

show emi basic_annoyed
with charachange

emi "Es una verdadera molestia."

"Su modestia nunca deja de divertirme."

show emi basic_grin
with charachange

emi "Aunque…"

"Uh oh."

show emi sad_shy
with charachange

emi "Sabes lo que estoy pensando, ¿verdad Hisao?"

"Mostrar mis emociones a flor de piel es uno de mis peores hábitos. Ella me ha leído por completo."

"Afortunadamente, veo a alguien acercándose que me permitirá escaparme."

hi "Oh, hola Hanako."

show emi sad_shy at twoleft
show bg school_hallway3 at center
with charamove

show hanako emb_downtimid at tworight
with charaenter

"Le doy un saludo de bienvenida con la mano, e intento todo lo posible parecer como si no hubiera notado la cara melodramática de Emi. Ella me saluda de vuelta."

show hanako emb_smile
with charachange

ha "Ho-hola, Hisao… Emi."

show emi basic_closedgrin
with charachange

emi "Hola, Hanako."

hi "Iré contigo y Lilly en un segundo."

hi "De hecho, hablando de compañía a la hora del almuerzo, es extraño verte sin Rin, Emi."

show emi basic_shock
show hanako defarms_shock
with vpunch

emi "¡Ah! ¡Rin!"

stop music fadeout 3.0

hide emi
with easeoutleft

"Sin decir más, ella se olvida de nosotros y sale disparada por el pasillo. Debe haberse olvidado de que la estaba esperando."

"Hanako y yo nos quedamos sin hablar, solo capaces de estar de pie inútiles y observar esta esfera de energía aparentemente sin límites salir corriendo."

play music music_running

show emi basic_closedgrin at left
with easeinleft

emi "Oh, cierto, Hisao…"

"Ella de pronto se detiene antes de desaparecer en la esquina que da a la escalera hacia la azotea, girando para encarar nuestros rostros perplejos."

show emi excited_proud
with charachange

emi "Yo también odio el inglés."

stop music fadeout 4.0

hide emi
with easeoutleft

"Y con eso, desaparece."

"Todo lo que puedo hacer es dejar caer mi cabeza y soltar un largo suspiro, habiendo quedado por completo en el polvo."

show hanako basic_smile
with charachange

"Cuando escucho una breve risita detrás de mí, me doy la vuelta para ver a Hanako sonriendo hacia la esquina por la que mi atacante dobló."

play music music_daily fadein 4.0

show hanako basic_smile at center
show bg school_hallway3 at bgleft
with charamove

"Agarro del suelo la mochila que dejé caer y rápidamente le sacudo el polvo."

hi "Buenas. ¿Ocupada?"

show hanako def_worry
with charachange

ha "¿A ti… no te gusta el inglés?"

hi "¿Hmm? Oh, eh, no. Tuve prueba de eso hace poco, y Emi me pilló deprimido por los resultados."

show hanako emb_downsad
with charachange

ha "Ah, lo siento…"

"Ella aparta la mirada, la culpa marcada en su rostro. Un observador casual pensaría que ella acaba sin querer de recordarme de un pariente muerto."

hi "Vamos, no es tu culpa. ¿Cómo te va con ello?"

show hanako emb_sad
with charachange

"Ella levanta la mirada, aunque sigue evitando mis ojos."

show hanako basic_worry
with charachange

ha "Bien… supongo."

"Sigue un silencio incómodo. Parecen demasiado comunes alrededor de Hanako."

show hanako basic_bashful
with charachange

ha "Oh, Lilly preguntó si… te gustaría acompañarnos a almorzar en la azotea."

"Supongo que no tengo precisamente algún compromiso urgente que atender."

hi "Claro, iré enseguida."

show hanako cover_distant
with charachange

ha "Em, yo… iré en este momento a buscar mi almuerzo a la cafetería… entonces."

hi "Adelante. No necesitas mi permiso para irte, sabes."

show hanako basic_smile
with charachange

ha "E-está bien. Yo… me marcho entonces."

hide hanako
with charaexit

stop music fadeout 5.0

"Ella da una respuesta nerviosa, asiente ligeramente y rápidamente se dirige hacia la cafetería."

play ambient sfx_crowd_indoors fadein 2.0

show crowd:
    bgleft
    alpha 0.0
    parallel:
        ease 1.0 center
    parallel:
        linear 2.0 alpha 1.0
with None

show bg school_hallway3 at center
with dissolvecharamove

"Supongo que debe haber olvidado traer su almuerzo hoy. Mientras camino por el pasillo, más y más estudiantes comienzan a salir de los salones y pasarme, dirigiéndose en la misma dirección que Hanako."

"Cuando logro llegar hasta las escaleras, tengo que abrirme camino a empujones a través de una multitud conversadora de estudiantes."

stop ambient fadeout 0.5

scene bg school_staircase1
with locationchange

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_rooftop

"Finalmente logro cruzar lo último de la multitud y doblar por las escaleras, dejando mis hombros caer de alivio y disminuyendo mi paso antes de abrir la puerta hacia la azotea."

play sound sfx_door_creak
$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

scene bg school_roof
show white
with locationchange

hi "¡Ah, maldición!"

"Momentáneamente aparto la mirada, cegado por el severo sol de verano."

show white:
    alpha 1.0
    linear 10.0 alpha 0.0

show lilly basic_smile behind white:
    left
    ypos 1.2
show emi basic_grin behind white:
    center
    ypos 1.15
show rin basic_absent behind white:
    right
    ypos 1.17
with charaenter

mystery "¿Hmm?"

play music music_soothing fadein 8.0

"A medida que recupero poco a poco mi vista, los alrededores al fin comienzan a tomar forma."

"Lilly, Emi y Rin están sentadas juntas en la azotea, las copas de los árboles del bosque que rodea Yamaku visibles más allá de la reja alrededor de ellas, como para enmarcar el cuadro."

show emi basic_closedgrin
with charachange

emi "¡Ah, Hisao!"

show lilly basic_smileclosed
show rin basic_deadpannormal
with charachange

"Lilly y Rin asienten rápidamente en reconocimiento y lentamente como saludo respectivamente."


"Comienzo a caminar hacia el trío bastante disparejo, y no puedo evitar maravillarme de la velocidad con la que Emi devora la segunda mitad de su plátano."

hi "Hola. Qué extraño verlas a las tres juntas de esta forma."

show lilly basic_weaksmile
with charachange

li "Parece ser un día bastante lleno de coincidencias; Emi y Rin decidieron comer en la azotea tal como Hanako y yo."

show emi basic_annoyed
with charachange

emi "¡Lo robaron! ¡Este lugar era nuestro!"

hi "Cálmate, no se puede robar un lugar en la escuela."

"Me dejo caer al lado de Lilly, nosotros cuatro formando un semicírculo."

show rin basic_deadpanupset
with charachange

rin "Creo que ella tiene razón."

hi "¿Tú también?"

show rin basic_deadpan
with charachange

rin "La mariposa es su cómplice."

hi "La mari…"

"Al mirar alrededor, en efecto, una pequeña mariposa amarilla revolotea por mi campo de visión."

hi "Entonces dime, ¿cómo ayudó esta mariposa a Lilly a “robar” este lugar?"

show rin basic_lucid
with charachange

rin "Escuchó nuestra conversación y le dijo."

"Debí saber que no podía esperar un razonamiento sensible de parte de Rin. De todas formas, supongo que no haría daño seguir el juego."

hi "¿Me estás diciendo que ella puede hablar con las mariposas?"

show rin basic_awayabsent
with charachange

rin "Hay gente que puede hablar con los caballos, llamados encantadores de caballos."

show rin basic_deadpanamused
with charachange

rin "Lilly debe de ser encantadora de mariposas."

"Escondo mi cabeza entre mis manos mientras Emi se pone en contra de su extraña compañera. No parece compartir el sentido del humor de Rin."

show emi basic_confused
with charachange

emi "Los encantadores no funcionan así."

"Emi y Rin continúan con su charla mientas me doy vuelta hacia Lilly, quien está ocupada acabando con su pequeña lonchera de curry y arroz."

hi "¿Entonces qué les trajo por aquí, de todos modos?"

show lilly basic_smile
with charachange

li "Un poco de aire fresco de vez en cuando no hace daño."

show emi basic_shock
with charachange

emi "¡Ah!"

"Emi pone fin a sus vanos intentos por presentarle a Rin el concepto de lógica."

show emi sad_annoyed
with charachange

emi "¡Nosotras vinimos por eso también!"

"Algo me dice que la idea fue solo de ella, y que Rin solo se vio arrastrada hasta aquí por capricho de Emi. Por otra parte, probablemente pueda decirse lo mismo de Lilly y Hanako."

show lilly basic_weaksmile
with charachange

li "Vamos, vamos. Podemos compartir."

$ renpy.music.set_volume(0.001, 1.0, channel="music")

play sound sfx_door_creak


show lilly basic_surprised
show emi basic_hes
show rin basic_awayabsent
with charachange

"El chillido de la puerta de la azotea se escucha tan pronto como ella dice esas palabras. Quedamos por un momento en silencio ya que nuestra atención se enfoca en la figura que emerge de ella."

show lilly basic_surprised:
    xanchor 0.5 xpos 0.4
show emi basic_hes:
    xpos 0.68
show rin basic_awayabsent:
    xpos 1.08
show bg school_roof at bgright
hide white
with charamove

show hanako basic_distant:
    xanchor 1.0 xpos 0.0 yalign 1.0
    easein 3.0 xanchor 0.0 xpos -0.06
    ease 1.0 ypos 1.17
with None

"Hanako camina lentamente hacia nosotros, sus ojos fijos en el suelo, lamentando en silencio la atención que está atrayendo. Se tensa, apenas un poco, cuando sus ojos se cruzan con los de Rin."

"No puedo evitar levantar una ceja mientras ella camina hacia nosotros y se sienta a mi lado, haciendo todo lo posible para evitar mirar hacia arriba, incluso cuando trae el pan de la cafetería a su boca."

show rin basic_absent
show emi basic_grin
show hanako basic_normal:
    xanchor 0.0 xpos -0.06 ypos 1.17
with charachange

hi "¿Y cómo se conocen tú y Emi, de todas formas?"

$ renpy.music.set_volume(1.0, 8.0, channel="music")

show lilly basic_smileclosed
show rin basic_awayabsent
with charachange

li "Emi es algo conocida por la escuela debido a su habilidad atlética. Ella es el miembro más rápido del equipo de atletismo por un buen margen, incluso superando a Miki Miura en la última competencia de atletismo la semana pasada."

"Miki Miura… ah, la chica bronceada que se sienta al frente en mi grupo. Considerando su altura y su cuerpo tonificado, ser capaz de vencerla es un logro bastante grande."

show emi excited_amused
with charachange

"Mirando hacia Emi, es bastante claro que ella está bien consciente de este hecho, y sonríe orgullosamente."

show emi excited_happy
with charachange

emi "Entonces, Hisao. ¿De cuánto fue tu puntaje en inglés?"

"Uf."

show rin basic_absent
with charachange

hi "Sin comentarios."

show emi basic_annoyed
show rin basic_awayabsent
with charachange

emi "Buu~."

"Ella infla sus mejillas y pone cara de berrinche, pero no le toma mucho tiempo volver a animarse."

show emi excited_proud
with charachange

emi "Bueno, si te digo el mío, tú tienes que decirme el tuyo. ¿Trato?"

stop music fadeout 4.0

show rin basic_absent
with charachange

hi "De acuerdo, de acuerdo."

show emi basic_closedhappy
show rin basic_awayabsent
with charachange

emi "Bien, a la cuenta de tres, ambos diremos nuestros resultados."

show emi excited_joy
with charachange

emi "Uno…{w=1.0} Dos…{w=1.0} ¡Tres!{w=1.0}{nw}"

show emi basic_closedgrin
with charachange

$ doublespeak (hi, emi, "…", u"¡Treinta y dos!")

"Sonrío de forma pícara."

play music music_comedy

show hanako cover_smile
show lilly basic_cheerful
show rin basic_amused
show emi excited_sad
with charachange
with vpunch
play sound sfx_impact

emi "¡Ah! ¡Malo! ¡Malo, malo, malo, malo!"

show rin basic_absent
with charachange

hi "Tú lo dijiste, no yo. De todas formas, el hecho de que hayas logrado tener un puntaje aún más bajo que el mío es asombroso."

show emi sad_grit
show rin basic_awayabsent
with charachange

emi "¡Grr~!"

"Ella se ve y suena como un terrier pequeño gruñéndole a un intruso. No puedo decir que sea lo más amenazante que he visto."

show lilly basic_displeased
show hanako basic_normal
with charachange

li "De todas formas, obtener más de treinta y dos no es algo de lo que se pueda presumir, y mucho menos sacar menos de eso. En cualquier materia."

show rin basic_absent
with charachange

hi "Sí, Lilly."

show rin basic_awayabsent
show emi sad_shy
with charachange

emi "Lo siento, Lilly."

show lilly basic_smile
with charachange

li "Podría ayudarte con tu inglés, si quieres. Sería un placer el—"

show emi basic_closedgrin
with charachange

emi "No, no, está bien. Pero aprecio el gesto. De verdad."

show lilly basic_reminisce
show hanako basic_smile
show rin basic_deadpanamused
with charachange

"Lilly se ve un poco decepcionada, sus esperanzas de entregar su conocimiento desvanecidas. A juzgar por la risa mal oculta del resto de nosotros, ni ella ni Emi parecen haber obtenido mucha lástima."

stop music fadeout 0.5
$ renpy.music.set_volume(0.0, 4.0, channel="ambient")

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)

window show

"Sin embargo, mientras me siento riendo felizmente, de pronto siento mi voz interrumpida al contraerse mi pecho."

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)

window show

"Me siento en silencio unos cuantos segundos, toda mi concentración enfocada en mi pulso. Es solo un dolor ligero, pero se siente que está aumentando."

play music music_tragic fadein 0.5

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

with Pause(0.7)

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

window show

"Respira profundo… respira profundo…"

window hide

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

window show

"Alzo la mirada hacia arriba e intento mantener por lo menos parte de mi atención en mis alrededores, para ver a Emi de pronto paralizándose cuando nota de reojo la expresión de dolor en mi rostro."

show emi basic_hes
with charachange

emi "Oye, Hisao… ¿estás bien?"

show hanako def_worry
show lilly basic_surprised
show rin basic_deadpanupset
with charachange

hi "Sí, estoy… bien…"

window hide

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

window show

"Vuelvo a mirar hacia abajo y redoblo mis esfuerzos para intentar mantenerme tranquilo, apretando mis puños para intentar calmar el dolor."

window hide

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

with Pause (0.7)

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

stop music fadeout 4.0

window show

"Toma un poco de tiempo, pero el dolor, afortunadamente, comienza a desvanecerse."

$ renpy.music.set_volume(0.5, 4.0, channel="ambient")

"Cuando vuelvo a levantar la mirada, solo hay silencio y expresiones pensativas a la vista. Supongo que mejor me explico."

play music music_rain fadein 10.0

hi "Arritmia. Estoy bien, es… solamente un pálpito cardiaco."

show lilly basic_listen
with charachange

li "¿Estás seguro? ¿Deberíamos traer al enfermero?"

show hanako def_worry:
    ypos 1.0
with ease

"Respondiendo a la señal, Hanako rápidamente se levanta y comienza a correr hacia la puerta."

hi "Hanako, detente. Lilly, estoy bien."

show rin basic_deadpan
with charachange

rin "Pareces un tomate mojado y arrugado."

hi "¿Eh?"

"Al poner mi mano en mi frente, puedo sentir las gotas de sudor reunidas y las limpio con mi puño."

hi "Gracias. Ya les dije, estoy bien. Solo soy un poco… frágil, supongo."

show hanako basic_worry
with charachange

show hanako basic_worry:
    ypos 1.17
with charamove

show emi sad_shy
show rin basic_deadpanupset
show lilly basic_sleepy
with charachange

"Todo el ambiente ha cambiado de uno festivo a uno de rostros abatidos, siendo la situación demasiado incómoda como para que alguien sepa exactamente cómo reaccionar."

"Y por supuesto, todo esto gracias a mí. Tan solo tenía que suceder ahora, junto a ellas."

stop music fadeout 8.0

show lilly basic_weaksmile
with charachange

li "¿Oh, Emi?"

show emi basic_hes
show rin basic_awayabsent
with charachange

emi "¿Hmm?"

"Ella levanta la mirada, con una caja de jugo a medio camino de su boca."

show lilly basic_smileclosed
with charachange

li "No les he dicho de mi puntaje aún, ¿o sí?"

show emi basic_annoyed
with charachange

emi "Sí, bueno. Eres medio extranjera, así que tu puntaje no cuenta de todas formas."

"Levantando una ceja, me doy vuelta inquisitivamente hacia Lilly."

show rin basic_absent
with charachange

hi "¿Cuál fue tu resultado en el examen, de todas formas?"

show lilly basic_cheerful

"Ella sonríe de forma pícara."

show rin basic_awayabsent
show lilly basic_planned
with charachange

li "Ciento por ciento. Puntaje perfecto."

play music music_lilly fadein 0.5

"No puede ser. Todo lo que puedo hacer es quedar asombrado con la boca abierta."

"Considerando que esos exámenes son una locura incluso para un hablante nativo, solo puedo imaginarme que ella llegó a memorizarse parte del diccionario. Un don para la memorización por repetición, quizás."

show rin basic_absent
with charachange

hi "Eso es…"

show rin basic_awayabsent
show emi sad_pout
with charachange

emi "¡Ves! Solo alguien mitad extranjero podría haber obtenido un puntaje tan bueno."

show rin basic_absent
with charachange

hi "“Ves”…"

show rin basic_awayabsent
show emi basic_closedsweat
with charachange

emi "Em…"

show lilly basic_giggle
show hanako basic_smile
with charachange

"Lilly y yo nos reímos a expensas de Emi, su reacción idéntica a la mía cuando pisé por primera vez esa pequeña mina. Aunque la ascendencia extranjera de Lilly sí plantea un punto."

show rin basic_absent
with charachange

hi "Ah, es cierto. Mañana te marchas a Escocia, ¿verdad?"

show rin basic_awayabsent
show lilly basic_smile
with charachange

li "Eso es correcto. Emi escuchó algunos rumores al respecto; parece que la noticia se está propagando rápidamente, considerando que solo se lo dije a un amigo de mi clase hace un par de días."

show emi sad_grin
with charachange

emi "Debe ser agradable cruzar la mitad del mundo para vacaciones."

show emi excited_happy
with charachange

emi "Oye, ¿podrías comprarme algo cuando estés allá?"

show rin basic_absent
with charachange

hi "Vamos, no te contengas."

show lilly basic_giggle
with charachange

"Lilly suelta una risita animada, evidentemente esperando la franqueza de Emi."

"El resto del almuerzo sigue tal como antes, el buen ambiente de antes de mi fibrilación auricular afortunadamente regresando por completo."

stop music fadeout 8.0

scene bg school_roof
show lilly basic_smileclosed:
    center
    ypos 1.2
with shorttimeskip

"Cuando todos se marchan en fila con las respectivas despedidas, solo quedamos Lilly y yo."

hi "¿Oye, Lilly?"

"Ella guarda lo último de sus cosas en su mochila y cierra los broches, antes de levantar un poco su cabeza."

show lilly basic_smile
with charachange

li "¿Hmm?"

hi "Em… gracias por romper el silencio antes. Yo quería hacerlo, pero en realidad no sabía cómo."

"Aunque me gustaría sonar menos taciturno con respecto a todo, entre la carta de ayer, haber metido tanto la pata en el examen, y ahora mi corazón, se me hace realmente difícil."

show lilly basic_weaksmile
with charachange

"Ella pone una sonrisa indulgente y asiente. Espero que no lo haya notado, pero conociéndola, es improbable que no lo haya hecho."

li "Emi es fuerte, pero solo una humana. Nos preocupamos por ti, Hisao."

hi "Un momento, ¿por qué se preocuparían por mí?"

$ renpy.music.set_volume(0.5, 2.0, channel="ambient")

show lilly basic_displeased
with charachange

"Su rostro sonriente colapsa, volviéndose incómodamente serio."

li "Hisao, no somos ignorantes de tu situación."

li "A dif…"

show lilly basic_concerned
with charachange

"Ella de pronto se detiene, dudando de si debería decir lo que quiere decir. Sonrío débilmente y pongo mi mano en su hombro."

play music music_twinkle fadein 10.0

hi "No lo hagas. Ya es suficiente con que yo me preocupe por ello. No quiero que todas ustedes lleven mi carga."

show lilly basic_oops
with charachange

li "Pero…"

hi "Si todas ustedes se preocupan por ello, yo tengo que preocuparme por su preocupación. Si… eso tiene sentido."

hi "Estoy bien, ¿de acuerdo?"

show lilly basic_reminisce
with charachange

"Por un momento ella parece estar perdida en sus pensamientos, considerando cuidadosamente cómo reaccionar."

show lilly basic_weaksmile
with charachange

li "Hisao, ¿tienes algún papel que te sobre de los envoltorios de tu comida?"

hi "¿Creo… que sí? Déjame ver."

play sound sfx_rustling

"Escarbo en mi mochila buscando las sobras de mi almuerzo, eventualmente encontrando un cuadrado de papel del envoltorio de mi emparedado."

"Con mis cejas levantadas y mi expresión bastante inquisitiva, suavemente coloco el cuadrado en las manos de Lilly. Sin decir nada, ella pone sus dedos a su alrededor para sentir sus bordes."

show lilly basic_smile
with charachange

li "Esto debería ser lo bastante grande…"

"Ambos sentados en la azotea, los minutos que quedan para las clases pasando, ella procede a poner el objeto en el suelo y comienza su trabajo en serio."

show lilly basic_smileclosed
with charachange

"Envuelto en el silencio, miro sus dedos moverse por el pequeño cuadrado con destreza absoluta. Un pequeño doblez aquí, uno más grande allí, sus dedos mantienen un ritmo lento pero seguro."

"Alzando mi mirada, su expresión es serena y plácida. El hecho de que su rostro apunte muy por sobre el papel frente a ella hace el ver su trabajo mucho más curioso."

"Sus hombros caen un poco después de terminar un doblez final, aparentemente concluido su trabajo. Solo cuando sostiene el objeto entre sus manos me doy cuenta de lo que es."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene white
with dissolve

with Pause(0.1)

scene ev lilly_crane:
    truecenter
    zoom 1.1 subpixel True
    ease 15.0 zoom 1.0
with Dissolve(4.0)

"Una pequeña grulla de papel."

"Marrón claro debido al envoltorio utilizado, el resultado se ve bastante delicado y preciso."

hi "¿Puedes hacer origami?"

li "Aprendí sola cómo hacerlo cuando era menor. Ha mejorado un poco mi destreza."

hi "Ya veo…"

"Un tanto perplejo, saco con cuidado la pequeña ave de sus blancas manos ahuecadas como si pudiera romperse por el más mínimo aliento. Parece estar doblado bastante bien, y mantiene su forma fácilmente."

$ renpy.music.set_volume(1.0, 2.0, channel="music")

scene bg school_roof
show lilly cane_smile at center
with locationskip

"Ambos tomamos nuestras mochilas y nos encaminamos a la puerta, Lilly extendiendo su bastón mientras tanto."

stop ambient fadeout 2.0

scene bg school_hallway3
with locationskip

"Sostengo la obra de Lilly ante mi rostro para seguir inspeccionándola mientras caminamos por el pasillo, su mano recorriendo los pasamanos plateados para orientarse."

"Si ella se enseñó a sí misma el origami para mejorar su destreza, con el uso de su mano significando tanto para ella dada su condición… ah, entonces es eso."

"Sonrío cuando me doy cuenta del significado del ave."

"“Todos aquí tenemos que encontrar nuestra propia manera de tratar con sus condiciones. No estás solo aquí cuando tienes problemas”."

hi "Gracias, Lilly. Agradezco esto."

show lilly cane_cheerful
with charaenter

"Ella sonríe dulcemente y asiente, sin usar palabras cuando no son necesarias, como siempre."

show lilly cane_smileclosed
with charachange

li "Todo lo que pido es que te cuides a ti mismo, Hisao."

hi "No te preocupes, lo haré."

show lilly cane_smile
with charachange

li "¿Me lo prometes?"

hi "Lo prometo."

hide lilly
with charaexit

stop music fadeout 7.0

"Y con eso, nos separamos."

"A decir verdad, no sé qué es lo que me molesta más, el hecho de que me pueda morir en cualquier momento, o el hecho de que todos lo sepan."

"Supongo que aceptaré cada día como venga. Como el obsequio inesperado en mi mano me recuerda, no estoy solo aquí. A pesar de que yo pueda ser así, no estoy solo."

"Si se preocupan, si quien sea se preocupa, sonreiré."

"Sonreiré tanto que todas sus preocupaciones desaparecerán."

scene black
with dissolve



label es_L8:

scene black
with dissolve

play sound sfx_normalbell

scene bg school_scienceroom
show muto normal at center
with locationchange

"Al momento que suena la campana, un suspiro de alivio colectivo escapa de todos."

play music music_happiness fadein 2.0

"Gran parte de la mañana ha sido ocupada por una lección monótona sobre estequiometría, un tema completamente inadecuado al calor insoportable que se cuela al salón."

hide muto
with charaexit

"Sabiendo que intentar enseñar algo más sería una labor inútil, Mutou se rinde y comienza a acomodar los materiales de estudio de su escritorio por hoy."

$ renpy.music.set_volume(0.7, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 0.5

show hanako basic_normal at center
with charaenter

"Cuando la plática banal comienza a sonar en el salón, noto que Hanako se ha levantado y que viene hacia mi banco. Ella ha estado mucho menos retraída últimamente, algo que me da un cierto grado de satisfacción."

show hanako basic_smile
with charachange

ha "Hola, Hisao."

hi "Hola. ¿Entonces, quieres ir a buscar a Lilly? Ya va a ser la hora en la que debería partir si quiere alcanzar el vuelo."

show hanako cover_worry
with charachange

ha "Em… sobre eso…"

show hanako basic_worry
with charachange

ha "Ella dijo que podría demorarse un poco por sus compañeros."

"Supongo que eso tiene sentido. Su grupo usualmente sale un poco antes que el nuestro, así que Lilly normalmente ya habría llegado a nuestro salón."

hi "Bueno, no importa. Podemos esperar fuera de su salón para variar, ¿cierto?"

show hanako emb_smile
with charachange

"Ella suelta una risita antes de asentir, los dos tomando nuestras cosas y encaminándonos al salón del grupo 3-2."

stop ambient fadeout 1.0

scene bg school_hallway3
with locationchange

"Cuando llegamos a nuestro destino, me detengo, entretenido por la escena que veo adentro."

"Una de las chicas más bajitas del grupo le da un abrazo con entusiasmo a Lilly y su cabeza apenas alcanza el mentón de Lilly."
"Sus otros amigos, de los cuales hay varios, están reunidos también alrededor de ella. Lilly simplemente sonríe amablemente y contesta el abrazo."

"Supongo que Lilly debe ser bastante popular. Comparada con la dura pero justa dictadura de Shizune en el 3-3, Lilly parece más como una figura materna para el 3-2, ni qué hablar de su altura y apariencia."

"El porte marcadamente frío de Kenji mientras guarda sus cosas en su asiento en la esquina de atrás del salón era de esperarse. Él sin lugar a dudas está lejos de ser un fan del alboroto por la despedida de Lilly."

"Miro hacia el lado y veo que Hanako sigue mi mirada, y decido al fin entrar al cuarto."

$ renpy.music.set_volume(0.7, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 0.5

scene bg school_room32
show crowd at center
show lilly basic_surprised at center
with locationchange

hi "Buenas, Lilly. Solo somos Hanako y yo."

show lilly basic_surprised at twoleft
show crowd at bgleft
show bg school_room32 at bgleft
with dissolvecharamove

show hanako emb_downtimid at tworight
with charaenter

"Hanako se retrae notablemente cuando se expone al barullo que hay alrededor de Lilly. Por mucho que lo intente, dudo que alguna vez supere por completo su ansiedad social."

show hanako emb_emb at tworight
with charaenter

ha "Hola…"

"Lilly logra identificar nuestra posición bastante bien, su compañera apartándose de ella sin decir palabra. Una expresión de ligera exasperación está marcada en el rostro de Lilly, aunque no puedo decir que la culpe."

show lilly basic_smileclosed
with charachange

li "Hola Hisao, Hanako. ¿Queda tiempo antes de que el vuelo salga?"

"Le doy una rápida mirada a mi reloj. Tomando en cuenta el viaje al aeropuerto, quedan diez minutos, quizás quince, permitiendo margen para cualquier imprevisto."

hi "Claro, aún tenemos unos cuantos minutos libres. Aún no me preocuparía de perderlo."

"Compañera" "Ah, ¿esta es Hanako?"

"Oh oh. Creo que sin darnos cuenta nos hemos visto envueltos en la red social de Lilly."

"La chica probablemente es parte de la facción legalmente ciega del grupo al igual que Kenji, dados sus anteojos casi como ventanas. Su cabello corto y cortado toscamente le da una apariencia que encaja con su expresión nerviosa."

show hanako def_shock
with charachange

ha "Ho-hola… em…"

"Ella toma la mano de Hanako y la agita hacia arriba y hacia abajo de forma entusiasta. De verdad no entiendo cómo las chicas pueden ser tan sociales con alguien a quien solo conocen como la amiga de una amiga."

"Mientras Hanako intercambia saludos nerviosos, miro por el cuarto buscando a mi pequeño y demasiado abrigado vecino de cuarto. Por más que lo intento, parece que se ha escapado del salón sin que nadie lo notara."

"Por un momento intento pensar en posibles proyecciones laborales que podrían beneficiarse de su única habilidad, antes de enfocar mi mente en asuntos más pertinentes."

show lilly basic_smile
show hanako cover_distant
with charachange

"Lilly parece satisfecha, si bien un poco cauta, por el entusiasmo que Hanako generó de pronto en aquellos alrededor de ella. No lo puede ver, pero Hanako tiene mucho menos pánico por la situación de lo que había anticipado."

"Pasando con dificultad por el grupo de compañeros, eventualmente logro llegar a ella."

hi "No te preocupes, Hanako está bien."

show lilly basic_weaksmile
with charachange

li "Gracias. Pensé que quizás se sentiría abrumada por ellos."

"Compañera" "¡No te preocupes, seremos amables!"

show lilly basic_concerned
with charachange

"Ambos hacemos una mueca al unísono. La sonrisa nerviosa de Hanako permanece pegada en su rostro cuando otro par de chicas se acerca a saludarla."

"Es un poco asombroso que hasta hace un mes atrás ella no habría sido capaz de manejar una situación como esta. Hasta cuando la conocí, nosotros dos completamente solos, ella salió corriendo de la biblioteca."

hi "Entonces, ¿tienes todo lo que necesitas?"

show lilly basic_smile
with charachange

li "Está todo empacado. Solo tengo que volver a mi cuarto a recogerlo en el camino, y Hanako y yo necesitamos cambiarnos."

hi "Supongo que será mejor que partamos, entonces. ¿Hanako?"

show hanako cover_bashful
with charachange

"La cabeza de Hanako se levanta hacia nosotros de golpe, su rostro indudablemente agradecido por la oportunidad de escaparse del pequeño grupo reunido a su alrededor."

show hanako basic_bashful
with charachange

stop music fadeout 2.0

ha "¡V-voy!"

stop ambient fadeout 0.5

scene bg hosp_ext
with shorttimeskip

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 1.0
play music music_tranquil fadein 3.0

"El largo viaje en taxi hasta el aeropuerto es sorprendentemente agradable, a pesar de que los tres estemos algo apretados juntos para caber en el pequeño asiento trasero. Por otra parte, quizás “pesar” no es la palabra apropiada."

"Lilly paga la tarifa al conductor cuando nos bajamos, los ojos de Hanako revolotean de izquierda a derecha. Afortunadamente no hay mucha gente por los alrededores, la mayoría de ellos estando dentro del edificio central en lugar de rondar por afuera."

show akira basic_boo at tworight
show hideaki bored:
    yalign 1.0 xanchor 0.5 xpos 0.9
with charaenter

"No es difícil divisar a Akira y a Hideaki, apoyados contra una reja mientras hablan para pasar el rato. Una gran maleta negra, con ruedas y manilla, también está apoyada contra la reja junto a ellos."

show hideaki surprise_up
with charachange

"Hideaki es el primero en vernos, señalándonos a Akira, quien nos saluda con demasiado entusiasmo."

show akira basic_laugh
with charachange

aki "¡Oigan! ¡Oi~gan!"

"Tomo la maleta de Lilly por ella al ir a encontrarnos con ambos, ganándome un gesto de apreciación."

show akira basic_smile
show hideaki normal
with charachange

aki "Tengo todas mis cosas aquí, ¿tienes las tuyas? ¿El boleto también?"

show lilly basic_smileclosed_cas at twoleft
with charaenter

li "No te preocupes, lo tengo todo. ¿Tú?"

show akira basic_laugh
with charachange

aki "Síp. Preparada para partir."

show hideaki evil
with charachange

hh "No sin contratiempos en el camino, debo añadir."

play sound sfx_impact

show akira basic_kill
show hideaki ohshit
with vpunch

"El comentario insidioso hace que su cabeza se vea arrastrada por una mano muy firmemente agarrada."

show akira basic_boo
show hideaki sad
with charachange

aki "Jaja cierto, como que se me olvidó que estaba en el bolsillo de mis pantalones. Pantalones que dejé en la lavadora…"

show lilly basic_concerned_cas
with charachange

li "Oh no…"

show akira basic_laugh
with charachange

aki "No te preocupes, no te preocupes. ¿Sabías que ahora puedes imprimir los boletos si los compras en línea? Es realmente genial."

show hideaki bored
with charachange

"La expresión de dolor de Hideaki dice que esta no fue una solución rápidamente encontrada. Podría haber sido peor, supongo."

show lilly basic_weaksmile_cas
with charachange

li "Entonces es mejor que partamos. El embarque debe estar listo."

show akira basic_lost
with charachange

stop music fadeout 2.0

aki "Sí, tienes razón."

"Hay cierto tono de melancolía en sus voces. Sin decir nada de los que quedan atrás, volver a ver a su familia después de todos estos años debe ser algo importante para ellas."

show hanako emb_sad_cas at center
with charaenter

play music music_serene fadein 4.0

ha "Lilly…"

"Hanako rodea a Lilly en un suave abrazo de despedida, el cual es cálidamente contestado. Lilly y yo compartimos un breve abrazo después, diciendo cada uno sus despedidas."

"Junto a nosotros, Hideaki y Akira se sueltan de un breve abrazo y unas pocas palabras entre ellos. Probablemente se vería bastante agradable si no fuera por la diferencia de altura casi cómica entre los dos."

show lilly basic_smile_cas
show akira basic_smile
show hanako emb_downtimid_cas
show hideaki normal
with charachange

"Lilly toma el brazo de su hermana ya que todo lo que hace falta decir en despedidas se ha dicho, las dos entrando por las enormes puertas de vidrio."

show lilly back_smileclosed_cas
with charachange

li "¡Adiós Hisao, Hanako!"

show akira basic_laugh
with charachange

aki "¡Nos vemos! ¡No hagas nada estúpido, Peque!"

hide lilly
hide akira
with charaexit

"Nos despedimos con los brazos hasta que finalmente desaparecen de nuestra vista entre la multitud en movimiento adentro."

"Y luego… estamos solos."

hi "Bueno… eso es todo."

show hideaki bored
with charachange

"Me doy vuelta y veo que Hideaki ya ha comenzado a marcharse."

hi "Nos vemos."

show hideaki bored_up
with charachange

show hideaki invis:
    xpos 1.0
with dissolvecharamove

hide hideaki
with None

"Él alza una mano al aire, de una manera que esperaría de Akira. Al final, solo quedamos Hanako y yo parados afuera."

show hanako emb_timid_cas
with charachange

"Pongo mi mano sobre su hombro. Ella distraídamente mira hacia las puertas frontales del edificio, como si fuera a ver un último destello de cualquiera de las dos antes de que desaparezcan."

hi "No te preocupes, el tiempo pasará rápido."

show hanako basic_normal_cas
with charachange

"Ella vacila un momento, pero eventualmente asiente."

"Con el calor sofocante del sol estival cayendo sobre nosotros, nos encaminamos hacia la parada de autobús cercana."

hide hanako
with charaexit

"Es extraño, de verdad. Justo cuando había comenzado a ver a Lilly de forma diferente, ella se va en lo que se siente casi como una peregrinación al pasado."

"Aunque, de cierto modo, eso es justo lo que yo he estado haciendo desde que llegué a Yamaku."

"Por mucho que reflexione con respecto a todo lo que me ha pasado, en realidad estoy lejos de ser único. Todos tenemos nuestras propias circunstancias y caminos para llegar a donde estamos ahora."

"Y sin embargo, aún no puedo entender cómo debería proceder. Mi vida podrá haber sido prácticamente reiniciada, y aún no puedo encontrar nada que llene satisfactoriamente el hueco que todavía siento en mi interior."

"Quizás el hecho de que se vaya Lilly sea algo bueno para mí. Sin ella para apoyarme, necesitaré hacer más por mi cuenta. También tendré que estar ahí para Hanako."

"Se siente extraño que todo esté cambiando tan rápidamente después de esos meses en el hospital que parecían existir tan separados de la realidad, pero eso es el mayor motivo para mantenerme enfocado."

"No puedo dejar pasar ninguna oportunidad en mi intento de reconstruir mi vida."

stop music fadeout 3.0
stop ambient fadeout 3.0

window hide

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
