label es_A31:

scene black
with None

scene bg school_scienceroom
with Dissolve(2.0)

play music music_normal fadein 3.0

"Los estudiantes entran a clase para la sesión de sábado por la mañana, todos y cada uno de ellos luciendo los ojos cansados de gente que ha trabajado por la noche."

"Quedando solo un día más para prepararse, supongo que no es de sorprender. Afortunadamente, solo tendremos que sufrir de clases hasta el receso del almuerzo, después el tiempo será todo nuestro."

show muto irritated at center
with charaenter

"Mutou entra tambaleándose a clase con un vaivén cansado. Supongo que los estudiantes no son los únicos que disfrutan sus noches de viernes."

"Sin decir palabra, garabatea algunos números de página y problemas en el pizarrón y se desploma en su escritorio."

"Es un comportamiento completamente extraño en él, pero parece que nadie va a decirle nada sobre ello."

play sound sfx_paperruffling

hide muto
with charaexit

stop sound fadeout 6.0

"En silencio, los estudiantes hojean sus cuadernos para empezar a trabajar. Sin deseos de romper esta tendencia, hago lo mismo."

"La fatiga ha hecho la clase antisocial; ni un murmullo es escuchado además del pasar de las hojas."

"Eso puede en parte atribuirse a los dos asientos vacíos a mi lado. Por alguna razón Misha y Shizune no están presentes; probablemente están con algún trabajo del consejo para el festival."

"Está muy tranquilo sin Misha presente."

"Me pregunto si ella nació siendo tan ruidosa como es, o si está “compensando” por la falta de voz de Shizune."

show muto normal at center
with charaenter

stop music fadeout 2.0

mu "Nakai, ¿podemos hablar un momento?"

"Estoy tan absorto pensando en Misha que ni siquiera noté que Mutou se acercaba a mi banco."

hi "Seguro… ¿sobre qué?"

mu "Probablemente sea mejor si hablamos fuera del salón…"

play sound sfx_dooropen

hide muto
with charaexit

"Algo sobre esto no suena muy bien, pero me levanto y lo sigo afuera, al pasillo."

play sound sfx_doorclose


label es_A31b:

scene bg school_hallway3
show muto normal at center
with locationchange



"Mutou está de pie en el pasillo, rascándose la cabeza mientras trata de dar con lo que quiere decir. Sin saber qué es lo que ocurre, espero en silencio."

mu "Escuché de parte del jefe de enfermeros de la escuela que tuviste un incidente el otro día."

"Ah. Así que es sobre aquello."

hi "Bueno, algo así, pero no es nada para preocuparse."

show muto irritated
with charachange

mu "Sí, sí lo es. Cualquier cosa que ponga en peligro tu salud es algo para preocuparse."

mu "Nosotros damos lo mejor para prepararte para tu vida aquí. Parte de lo cual implica saber tus límites, y cómo trabajar en torno a ellos."

mu "Sería negligente de mi parte si no hablara contigo sobre esto."

hi "Está bien, lo entiendo. Lo lamento."

"Mutou cierra sus ojos con frustración, y me doy cuenta de que probablemente no fue lo mejor que se podía decir."

mu "Algo me dice que no lo lamentas. Pretende tanto como quieras, pero esta no es una escuela normal."

mu "Mucha gente ha puesto demasiado tiempo, esfuerzo y dinero para asegurar que tú, y cada uno de los estudiantes aquí, puedan tener el mismo nivel de educación que sus iguales."

mu "Que abuses y rechaces nuestros consejos, especialmente los consejos médicos, es simplemente egoísta."

"No estoy completamente seguro de si es así como realmente se siente, o si es un acto que ha practicado varias veces para hacer a los estudiantes sentir remordimiento para que hagan “lo correcto”. Sea como sea, está funcionando."

hi "Entiendo. Todo esto es nuevo para mí, y me disculpo. Ahora conozco mis límites, y me apegaré a ellos."

show muto smile
with charachange

"Mutou parece alegrarse un poco, satisfecho de que su mensaje ha sido recibido."



label es_A31c:

scene bg school_hallway3
show muto normal at center
with locationchange



"Mutou está de pie en el pasillo, rascándose la cabeza mientras trata de dar con lo que quiere decir. Sin saber qué es lo que ocurre, espero en silencio."

mu "Así que, dime, ¿cómo van las cosas?"

hi "¿Cosas?"

"Esperaba que Mutou fuera un poco vago, pero esto es demasiado."

show muto irritated
with charachange

mu "Ya sabes. Cosas. Ahora ya has tenido una semana para acostumbrarte, así que ¿cómo van las cosas?"

hi "Eh, bien, supongo."

show muto normal
with charachange

mu "Ya veo. ¿Y cómo está tu… condición?"

"La pausa antes de “condición” pareció un poco innecesaria."

hi "No he tenido ningún problema hasta ahora."

show muto smile
with charachange

"Un gesto de alivio se muestra en el rostro de Mutou."

mu "Bien, eso es bueno. El enfermero de la escuela estaba un tanto preocupado de que pudieras estarte esforzando un poco de más."

mu "Me pidió que estuviera pendiente de ti cuando él no pudiera."

hi "Tiene sentido…"

show muto normal
with charachange

mu "Te quisiera pedir que no te desentiendas de nosotros con tanta ligereza. Por mucho que tratamos de darte el nivel de educación que tendrías en una escuela normal, tienes que comprender que tienes límites."

mu "Nuestro objetivo es asegurarnos de que sabes dónde están esos límites, y cómo maximizar tu potencial dentro de ellos. ¿Entiendes?"

hi "Supongo. Quiero decir, no planeo hacer nada estúpido."

show muto smile
with charachange

mu "Bueno, eso es un comienzo, supongo."





label es_A31d:

show muto normal
with charachange

play music music_normal fadein 3.0

mu "Bien entonces, a mi siguiente pregunta; ¿cómo encuentras tus estudios? Entiendo que estuviste indispuesto por un tiempo. No estamos muy avanzados, ¿o sí?"

hi "No lo creo. Traté de no quedarme atrás mientras estuve en el hospital, así que no ha sido muy difícil."

show muto irritated
with charachange

"Mutou toca su barbilla y levanta una ceja mientras absorbe esta información."

mu "¿Es eso…? Supongo que aún hay estudiantes en el mundo que se dan cuenta de la importancia del aprendizaje…"

"Yo no iría tan lejos, solo estaba tratando de mantenerme ocupado en mi pequeña prisión de soporte vital."

hi "Bueno, sí. No tienes que quedarte atrás con estas cosas, ¿o sí?"

show muto smile
with charachange

mu "Exactamente eso es. Un movimiento equivocado en este mundo y te dejan atrás, ¿correcto?"

hi "Emm, correcto. No desearía que eso pasara."

show muto normal
with charachange

mu "No, no lo desearías. Cada semana hay un nuevo descubrimiento científico. La mayoría no significa nada para los ignorantes, pero cualquiera de estos podría ser la llave a la Siguiente Gran Cosa."

hi "Lo tendré en mente…"

"Es obvio que la plática seria de Mutou ha acabado, y está de vuelta a su estándar, su enfoque ligeramente confuso de la vida."

"Creo, en retrospectiva, que lo prefiero de esta forma. Es ligeramente más predecible en su imprevisibilidad."

show muto smile
with charachange

mu "Bien entonces, creo que es todo lo que tenía que decir. Volvamos adentro, ¿de acuerdo?"

"Mi alivio con esa propuesta es insuperable."

hi "Seguro. Usted es el jefe, ¿o no?"

show muto normal
with charachange

"Mutou se detiene por un momento."

mu "No creo que alguno de mis estudiantes me haya dicho eso antes."

"Por un instante considero contestar a eso, pero algo en mi interior me llama a cerrar la boca y volver al salón."

play sound sfx_dooropen

scene bg school_scienceroom
with locationchange

stop music fadeout 5.0

"Unos pocos estudiantes brincan con el sonido de la puerta, tratando rápidamente de hacer como que trabajan en las preguntas del pizarrón."

play sound sfx_doorclose

"Algunos ni se molestan, sus cabezas desplomadas sobre sus bancos mientras duermen una siesta, pareciera que Mutou ni siquiera los nota."


"Él regresa a su escritorio y saca una revista científica de uno de los cajones. Creo que le llegué con eso."

"La clase regresa al casi-silencio que Mutou y yo dejamos antes de nuestra charla."

"Sentimientos mezclados de cansancio y anticipación rondan en la clase. Todos aquí esperan, ya sea una oportunidad de descansar, o la oportunidad de poner sus preparaciones de último minuto en marcha."


play sound sfx_normalbell
play music music_daily fadein 8.0

"El reloj en la pared lentamente hace pasar el tiempo restante de clase, hasta que finalmente la campana suena, terminando el tormento."

show muto normal at center
with charaenter

mu "Antes de que se vayan, quiero las respuestas de esos problemas para el lunes."

hide muto
with charaexit

"La clase suspira al unísono, lamentándose al instante de haber trabajado tan lento, pero aún conscientes de los demás problemas que tienen encima."

"El salón se vacía en un parpadeo dado que todos se precipitan para completar sus preparaciones de último minuto para el festival."

"Yo me quedo y trato de terminar rápidamente las preguntas para así no tener que preocuparme de esto por el resto del fin de semana, con el festival y todo mañana."

show bg school_scienceroom at bgleft
show hanako emb_downtimid at right
with charamoveinright

"Aparte de mí, Hanako es la única que queda, obviamente esperando a Lilly."

"Es extraño que Lilly haga todo el recorrido hasta nuestro salón para recogerla. Supongo que moverse por los alrededores es más complicado para ella que para Hanako."

"Pero no son mis asuntos, y naturalmente no pregunto sobre ello a Hanako."

"A pesar de la relativa proximidad de nuestros asientos, ninguno trata de iniciar una conversación sobre eso o sobre nada más, así que un silencio opresivo recae en el salón de clase."

"El tiempo pasa en silencio. Son probablemente solo 15 minutos o algo así pero se sienten como mucho más. Paso las hojas de mi cuaderno. Hanako pasa las hojas de la novela que está leyendo."

"La punta de mi lápiz se rompe sobre el papel justo cuando estaba por terminar un párrafo."

"El sonido de mi irritado suspiro y la subsecuente búsqueda de un sacapuntas se sienten como si estuvieran rompiendo la tranquilidad en el salón."

"Hanako mantiene sus ojos firmemente lejos de mi dirección."

"No pasa mucho tiempo antes de que se muestre la alta figura de Lilly en la entrada."

show lilly basic_smileclosed at offscreenleft
with None

show bg school_scienceroom at center
show hanako emb_downtimid at offscreenright
show lilly basic_smileclosed at left
with charamove

li "¿Hanako?"

show lilly basic_smileclosed at twoleft
show bg school_scienceroom at bgright
show hanako emb_downsmile at center
with charamove

"Su nombre es todo lo que se necesita para que Hanako salte de su banco y corra hacia Lilly."

hide lilly
with charaexit

show hanako emb_downsad
with charachange

show hanako emb_downsad at Slide(0.5,0.5,0.7,0.5,1.0,time_warp=_ease_out_time_warp)
with None

hide hanako
with charaexit

"Ellas hablan en voz baja por un momento, pero poco después Lilly se retira hacia el pasillo y Hanako vuelve desanimada al salón, tomando su asiento una vez más."


show hanako emb_downsad at offscreenright
with None

show bg school_scienceroom at bgleft
show hanako emb_downsad at right
with charamove

"Observo a Hanako de reojo por pura curiosidad ante la idea de que ambas estuvieran separadas."

"Por un par de minutos, ella no hace nada sino sentarse con su mano en la barbilla, mirando con desaliento al banco."

show hanako emb_downtimid at right
with charachange

"Sin embargo el aburrimiento evidentemente se vuelve demasiado para ella, su delgada figura alcanza su mochila y saca un pequeño libro."

"Ahora que lo pienso, ese no es el que le vi leer en la biblioteca. Ella debe ser una lectora bastante rápida para terminarlos a este ritmo."


label es_A31e:

hide hanako
with charaexit

stop music fadeout 4.0

"Después de unos diez minutos de revolverse sin descanso en su asiento y tratar de leer, Hanako cierra su libro y se va también."

"Como también lo hago yo, dado que el trabajo está ya terminado y no hay nada más que hacer en el salón."

scene bg school_dormhisao
with locationskip

"Sin sentirme realmente con energía, simplemente voy directo a mi habitación y leo por el resto del día."

$ suppress_window_after_timeskip = True

scene black
with Dissolve(3.0)




label es_A32:

scene bg school_scienceroom at bgleft
show hanako emb_downtimid at right
with None

hide hanako
with charaexit

stop music fadeout 4.0

"Después de unos 10 minutos de revolverse sin descanso en su asiento y tratar de leer, Hanako cierra su libro y se va también."

"Como también lo hago yo, dado que el trabajo está ya terminado y no hay nada más que hacer en el salón."

"Digo, no es que tenga nada que hacer en ningún otro lugar tampoco."

play music music_tranquil fadein 3.0

scene bg school_hallway3
show crowd
with locationchange

play ambient sfx_crowd_indoors fadein 0.3

"La escuela es como una colmena llena de actividad pero nadie me presta atención."

"Me paseo por los salones llenos de estudiantes haciendo desesperadamente esto y aquello, rondando de un lado a otro como pequeñas abejas obreras."

"No podrías imaginar que el día escolar ha terminado."

stop ambient fadeout 0.3

scene bg school_courtyard
show crowd
with locationskip

play ambient sfx_crowd_outdoors fadein 0.2

"Está un poco más tranquilo afuera, pero no mucho."

"La gente se apresura, a izquierda y derecha, avanzando tan rápido como pueden; ocupados y con energía."

"Yo siento lo contrario. El sol de mediodía parece estar absorbiendo todo el espíritu de mi cuerpo, haciendo que se sienta débil de arriba a abajo."

"Un aire cálido y suave fluye por dentro de mi camisa, sintiéndose como un cojín."

"Bostezo perezosamente, pensando en qué hacer."

"Dejaré mis libros en el dormitorio primero, y después… algo que aún no he decidido."

"Tal vez Kenji está en su habitación."

stop ambient fadeout 2.0

scene bg school_dormext_half
with locationchange

"En mi camino a los dormitorios distingo a Emi, corriendo a pesar de no tener sus extrañas piernas prostéticas de carrera puestas. La saludo y ella se patina hasta detenerse."

show emi basic_closedgrin at center
with charamoveinright

emi "¡Qué hay, Hisao!"

"Salpicaduras de pintura blanca y verde adornan su nariz y barbilla respectivamente, pero su sonrisa es amplia, tal como parece serlo siempre."

show emi excited_happy_close
with characlose

"Ella se acerca a mí, aumentando la sensación de que está examinándome."


emi "¿Qué haciendo?"

hi "Nada realmente. No tengo nada que hacer para el festival y todos los demás parecen estar haciendo algo importante."

show emi excited_laugh_close
with characlose

emi "¡Eso es perfecto! ¡Entonces puedes ayudarnos a mí y a Rin!"

hi "¿Con las preparaciones del festival? Eeeh, no estoy muy seguro de si sería de mucha ayuda."

show emi excited_proud_close
with characlose

emi "¡Está bien! ¡No soy de mucha ayuda tampoco!"

"Emi agarra mi muñeca y empieza a arrastrarme dentro de la escuela forzadamente."

scene bg school_lobby
show crowd
with locationskip

play ambient sfx_crowd_indoors fadein 0.3

"Incluso su velocidad al caminar es más como un trote, haciendo que me tropiece conmigo mismo tratando de mantener el ritmo."

scene bg school_staircase2
with locationchange

"Las escaleras detienen un poco a Emi. Tal vez es difícil ascender con sus piernas, o tal vez finalmente se ha quedado sin aliento."

stop music fadeout 7.0

scene bg school_hallway3
show crowd
with locationchange

"Regresamos al tercer piso y al pasillo de los estudiantes de último año, terminando en el lugar de donde había salido hace cinco minutos. Podría haber esperado aquí a Emi, si hubiera sabido."

hi "Así que tú… ¿Está Rin trabajando aún en ese mural?"

show emi basic_closedgrin at center
with charaenter

emi "¡Es correcto! Ella necesita todo tipo de pinturas y pinceles y cosas, así que vine a sacarlas del salón de arte."

hi "Y me necesitas para ayudar con eso."

show emi basic_grin
with charaenter

emi "Bueno… Rin me dijo que ya una vez le habías ayudado así que pensé que no te importaría hacerlo otra vez."

hi "Ya veo."

stop ambient fadeout 1.0

scene bg school_classroomart at bgright
with locationchange

play music music_another fadein 0.5

"Así que gracias a la extraña lógica de Emi, estoy aquí otra vez, juntando cosas del salón de arte para otra persona."

"La habitación está vacía aparte de nosotros y las solitarias partículas de polvo flotando en el aire. Emi avanza directamente a la pared trasera, sacando una pequeña y arrugada pieza de papel de su bolsillo."

"Mientras trata de encontrar sentido a los garabatos escritos, observo más atentamente los materiales que yacen aquí."

"Docenas de latas y botes de pintura están amontonados en los estantes en la forma más desorganizada."

"Algunos parece que fueron abandonados aquí hace décadas; reliquias de previas generaciones de miembros del club de arte."

"A un lado de los grandes montones de papel de dibujo cuidadosamente apilado, hay cajas llenas de pinceles de diferentes tamaños y crayones revueltos."

"Los olores a pintura, aguarrás y papel fresco flotan en el aire viciado, mezclándose en mi nariz para formar ese inconfundible aroma del arte."

show emi basic_closedgrin at offscreenright
with None

scene bg school_classroomart at bgleft
show emi basic_closedgrin at right
with charamove

"Emi revisa sus notas, comparándolas con las marcas en las varias latas de pintura, y me las pasa conforme va hallando las correctas."

show emi basic_grin
with charachange

"Ella estira su cuello para ver en el estante más alto, pero no parece ser suficiente."

show emi basic_annoyed
with charachange


"Sus ojos se mantienen por debajo del estante, no importa lo que haga. Emi se da por vencida y simplemente mira al estante arriba por un largo tiempo, como un niño en una tienda de juguetes, resoplando molesta."

show emi annoyedbounce
with None

"Después de un momento de creciente ira, ella empieza a saltar arriba y abajo, aparentemente tratando de leer rápido las etiquetas durante la fracción de segundo en que puede verlas, y captar lo que puede."

show emi basic_closedsweat at center
with charachange

"No es sorpresa que falle miserablemente, y casi se las arregla para echar abajo el estante completo."

"Ahora veo por qué el traerme aquí sería de utilidad."

hi "Vamos, déjame hacer eso. No puedes saltar tan alto, y no quiero que te lastimes intentándolo."

hi "Además, soy casi el doble de alto que tú."

show emi sad_angry
with charachange

emi "¡No lo eres!"

"Ella se da la vuelta, mirando con desdén, con las mejillas rojas y todo."

hi "Solo bromeo, solo bromeo. Como sea, buscaré ahí arriba, ¿está bien?"

show emi basic_annoyed
with charachange

"Ella me mira enojada una vez más, pero no logra replicar nada. Con un gruñido me da la espalda."

hide emi
with charaexit

"Así que comienzo a revolver el estante más alto buscando pintura mientras abajo, Emi se inclina para explorar lo que puede de los armarios."

"Sacudo negativamente la cabeza un poco, después de haber chequeado doblemente para asegurarme de que ella no me puede ver haciéndolo."


"Que Emi tenga un complejo sobre su estatura fue sorpresivo; de haberlo sabido no hubiera hecho bromas sobre eso."

"Ella parece despreocupada, pero supongo que todos tienen sus puntos débiles."

show emi basic_grin at center
with shorttimeskip

"Solo después de que tenemos casi todos los objetos juntos y extendidos en el escritorio como el botín de un cazador de tesoros, me doy cuenta de que no necesariamente fue lo de la estatura lo que la irritó."

"No le ha de gustar que le digan que no puede hacer algo. Como saltar."

"Pero la misma Emi parece que ya lo ha olvidado todo. Rápida para enojarse, rápida para perdonar… ¿es ella ese tipo de persona?"

"Al menos no parece que se haya tomado nada muy a pecho, dado que ella charla felizmente mientras tomamos el resto de los objetos y regresamos a donde está Rin."

scene bg school_courtyard
show crowd
with locationskip

play ambient sfx_crowd_outdoors fadein 0.2

"Caballerosamente llevo la mayor parte de los materiales mientras vamos con dirección a los dormitorios."

show emi basic_annoyed at center
with charaenter

emi "Rin está muy estresada con eso de terminar su pintura. Al final es su culpa; debió haber empezado antes."

hi "¿Lo logrará?"

show emi basic_closedgrin
with charachange

emi "Ni idea. Para mí se ve bien, pero con Rin, nunca sabes lo que está pasando."

show emi basic_annoyed
with charachange

emi "La encontré esta mañana tirada enfrente de los dormitorios en posición fetal. No había dormido en toda la noche. No puedo creer que las enfermeras nocturnas no la hayan encontrado."

show emi basic_grin
with charachange

emi "Y ahora está pintando otra vez como loca."

hi "Sí, he… notado que ella parece como un poco… trastornada. Por decirlo de alguna forma."

show emi basic_closedhappy
with charachange

"Emi ríe por mis palabras, así como también por mi, probablemente, muy obvia incomodidad."

show emi basic_happy
with charachange

emi "No me molesta. Ella es simplemente un poco extraña a veces."

"En eso estoy de acuerdo con ella. A diferencia de mí, Emi parece estar bien con la… lo que sea que se siente tan fuera de lugar en Rin."

"Aun así, ellas no se sienten tan cercanas como Misha y Shizune. Con ellas trabajando a veces como una sola entidad, es difícil decir dónde termina una y empieza la otra."

"Y todo a pesar de ser tan diferentes, tal como lo son Emi y Rin."

"Y Rin es la más diferente de todas, diferente de cualquiera que haya conocido jamás."

hi "Sí, supongo que ella es una persona muy… peculiar."

"Regreso a esa palabra otra vez, como si abarcara la personalidad de Rin por sí sola, pero realmente es solo un sustituto para una larga descripción de rarezas."

show emi basic_closedhappy
with charachange

"Emi ríe mientras me esfuerzo por encontrar una palabra descriptiva apropiada."

show emi basic_grin
with charachange

emi "Ella es simplemente extraña."

show emi excited_proud
with charachange

emi "¿Sabes?, más temprano, ella pasó media hora simplemente sentada en su caja."

emi "Y mirando sus pies."

show emi basic_closedhappy
with charachange

"Ella ríe otra vez en una forma que me hace pensar que no sabe bien lo que hay de gracioso en eso, simplemente lo es."

stop music fadeout 3.0

show emi basic_grin
with charachange

emi "Todo ese tiempo."

stop ambient fadeout 2.0

scene bg school_dormext_half
with locationskip

play music music_happiness fadein 2.0

"El área de trabajo es un desastre, pero el mural en sí ha ocupado aún más espacio en la pared desde la última vez que lo vi."

"Las desfiguradas formas humanas han sido casi enteramente coloreadas en tonos rojos, rosas y naranjas; cosas… extrañas e imaginarias llenando los espacios en medio."

"Luce… bien. No puedo pensar en ninguna palabra que describiría el trabajo consistente y comprensivamente así que me decido por un no-descriptivo “bien”."

"Pero honestamente, parece que el área alrededor de la pared se torna más desordenada con el mismo ritmo al cual el mural progresa."

"El piso está regado con docenas de latas de pintura, varios suministros de arte y botellas vacías de gaseosa."

show rin negative_spaciness at center
with charaenter

"Rin misma está en el centro de este caos, parada ahí luciendo muy cómoda como si ella fuera una parte natural de la escena."

"Su pantalón ha sido doblado hasta sus rodillas, exponiendo sus delgadas piernas que lucen un seco espectro de pinturas de guerra, similar al del rostro de Emi."

show emi basic_grin at offscreenleft
with None

show rin negative_spaciness at tworight
show bg school_dormext_half at bgright
show emi basic_grin at twoleft
with charamove

"Emi se me adelanta corriendo hacia Rin y salta con regocijo frente a ella."

show emi basic_closedhappy
with charachange

emi "¡Estoy de vuelta!"

show rin basic_awayabsent
with charachange

rin "Eso fue rápido. ¿Corriste por los pasillos otra vez?"

show emi excited_proud
with charachange

emi "Hisao me ayudó."

show emi basic_grin
with charachange

"Emi apunta victoriosamente hacia mí."

show rin basic_absent
with charachange


"Rin gira siguiendo el dedo de Emi con sus ojos, mirando hacia el lugar donde me ubico."

show rin basic_deadpannormal
with charachange

"Ella asiente distraídamente hacia mí. Parece que no ha dormido desde anoche: una inexpresiva y vidriosa mirada que está enfocada ligeramente fuera de donde estoy, y movimientos como en cámara lenta."

rin "Hola, Hisao. Gracias por tu ayuda."

hi "Ni lo menciones."

show rin basic_deadpan
with charachange

rin "Lo acabo de hacer."

hi "No importa."

hi "Parece que has progresado. Se ve bien, hasta donde puedo decir."

show rin basic_deadpannormal
with charachange

rin "Pero ahora das más mala suerte."

hi "Lo sé, pero estoy dispuesto a correr el riesgo."

show rin basic_deadpandelight
with charachange


rin "Eso es algo muy bonito para decir. Para mí, desde luego. No para ti."

show rin basic_awayabsent
with charachange

rin "Esto es el porqué los artistas siempre tienen mala suerte. Ellos tienen que ver constantemente sus pinturas sin terminar."

rin "Así que los artistas no pueden encontrar el romance, sus programas favoritos de TV son cancelados, o mueren jóvenes por una enfermedad no especificada. Es una profunda y misteriosa ley del universo."

show rin basic_lucid
with charachange

rin "A menos que sean ciegos."

"Ella considera esto por un rato, luciendo como si fuera a caer dormida."

show rin basic_absent
with charachange

rin "Está este chico."

show rin basic_deadpannormal
with charachange

rin "En el club de arte, ¿ves? Un chico ciego. Así que él no. Ve."

label es_A32a:

hi "Ya me lo habías dicho."

show emi basic_hes
with charachange

"Miro a un lado a Emi y ella me mira también en una forma que me dice que también ya ha escuchado esto antes."

"No obstante, ninguno de nosotros dice nada a Rin, así que ella continúa con su monótono soliloquio como un comediante sin gracia."

label es_A32b:

show rin basic_awayabsent
with charachange

rin "Él debería convertirse en un artista. Sin mala suerte, garantizado."

rin "¿No creen que sería una buena idea?"

show rin basic_lucid
with charachange

hi "¿Que solo las personas ciegas se convirtieran en artistas? No, no lo creo."

"…"

show rin basic_deadpan
with charachange

rin "Tal vez tengas razón."

show rin negative_spaciness
with charachange

"Abandonando este hilo de pensamientos, ella da vuelta otra vez para meditar su trabajo y empieza a murmurar una melodía, pero no puedo recordar el nombre de esta."

show emi basic_closedgrin
with charachange

"Emi ordena los suministros que trajimos y mueve algunas latas de pintura, tratando de traer algo de organización a la escena."

show rin basic_awayabsent
with charachange

rin "Emi, necesito la pintura azul Prusia."

show emi basic_confused
with charachange

emi "¿Cuál es el azul Prusia?…"

"Ella está observando impotentemente siete u ocho latas, cada una con una diferente tonalidad de azul."

show rin basic_deadpan
with charachange

rin "Es la que tiene pintura azul Prusia dentro."

show emi basic_annoyed
with charachange

emi "¡Cielos, Rin! ¡No estás ayudando para nada!"

"Miro alrededor también, a pesar de que no sé tampoco cómo luce el azul Prusia. Me pregunto qué azul tiene algo que ver con Prusia."

"… O qué es Prusia en primer lugar. El nombre me suena vagamente familiar, pero no puedo recordar."

"Aunque ninguno de los azules parece más prusiano que los otros, las pequeñas etiquetas impresas son suficientemente legibles para determinar que ninguno dice nada de que el contenido sea prusiano."

hi "No hay azul Prusia aquí."







label es_A33:

scene bg school_dormext_half at bgright
show rin basic_deadpan at tworight
show emi basic_annoyed at twoleft
with None

"Emi suspira."

show emi basic_closedsweat
with charachange

emi "Supongo que tengo que regresar y conseguir un poco."

show emi basic_grin
with charachange

emi "Pero prometí ayudar con el proyecto de nuestra clase, así que estaré de vuelta un poco tarde. ¿Podrás arreglártelas sin él por unas horas?"

show rin basic_deadpannormal
with charachange

"Rin asiente con la cabeza y así, Emi se va."

stop music fadeout 2.0

hide emi
with charaexit

show rin basic_deadpannormal at center
show bg school_dormext_half at center
with charamove

"Yo me quedo porque me gusta ver a Rin pintar, y porque no tengo nada mejor que hacer."

"Me siento en una caja y tomo el libro del día de mi mochila. Es una historia de tres chicos bebiendo cerveza por dos semanas completas sin hacer mucho más."

play music music_pearly fadein 2.0

hide rin
with charaexit

"Rin se mueve del lugar que necesitaba el azul y empieza a trabajar lentamente en otro."

"Sus pies trabajan con el pincel firmemente sobre la pared de yeso. Capas de pintura sobre capas de pintura. El mural lentamente gana más forma."

"Doy la vuelta a las páginas tranquilamente. En este capítulo ellos beben cerveza en la casa del amigo del protagonista. En los previos era en el propio departamento del protagonista."

"No es el tipo de libro interesante, un pedazo de la vida imaginaria de alguien que me hace preguntar el porqué tenía que ser escrita."

"De hecho ¿por qué? La razón por la cual hacer algo creativo… es algo incomprensible."

"Como el porqué Rin pinta. Parece como que Rin y Emi son iguales, yendo firmemente contra sus destinos como si fuera por simple despecho."

"Rin incluso dijo algo como eso. “Haz algo que no puedes simplemente porque puedes”."

"¿Eso es a lo que se refería? ¿Es esa su razón? Podría ser la de Emi, ella parece una persona un tanto testaruda."

"Rin no da ese tipo de aire. Pensándolo bien, ella no da ningún tipo de aire, o tal vez da un tipo diferente cada vez que hablo con ella."

"¿Por qué ella dijo lo que dijo? ¿Por qué ella o cualquiera pinta, o dibuja, o esculpe, o escribe?"

"Nunca he tenido mucho de impulsos creativos así que no creo poder entender realmente sobre ello."

"Me hace sentir hueco por dentro."

"Qué pensamiento tan terrible. Tampoco puedo decidir si eso es verdad o no."

"¿Estoy conforme siendo de esta forma? No puedo negar que siento un poco de envidia por Rin, pero no puedo realmente considerarlo un defecto de ningún tipo."

"Yo soy yo y ella es ella."

"Aun así, necesito encontrar algo. Algo que pudiera… hacerme sentir un poco menos perdido, en lugar de simplemente ahogarme en estos libros como hice en el hospital."

"No puedo hacer nada más que sentirme desorientado; la nueva escuela, nueva forma de vida y la gente a mi alrededor contribuyen con esta sensación."

"Estoy dando lo mejor de mí para encajar en los círculos sociales existentes, y la mayoría de la gente que he conocido ha sido realmente buena."

"Aún se siente, sin embargo, como que soy un forastero; como si no perteneciera aquí."

stop music fadeout 2.0

"Me saco el sentimiento de encima, dándome cuenta de que estoy divagando. No he ni dado la vuelta a una sola página del libro, ni hecho nada por Rin."

"Ella está tratando de vaciar pintura de una gran lata usando solo sus pies, sin molestarse en pedírmelo. O tal vez lo pidió, y no lo escuché."

"Como sea, se ve muy inestable."

scene bg mural_part
show rin basic_awayabsent_close at tworight
with locationchange

play music music_soothing fadein 0.5

"Rápidamente salto a ayudarla, pues parece como que está a punto de derramar el contenido completo de la lata por todo el pavimento."

"Tomo la lata de sus pies y vacío un poco en el recipiente."

show rin basic_absent_close
with charachange

"Ella no dice nada, y tampoco lo hago yo. Percibo un resplandor de sus ojos, mirándome silenciosamente por debajo de su despeinado flequillo."

"Es una expresión indescifrable, un perfecto rostro neutral, mezclado con un toque de algo como una ligera sorpresa."

"Me pregunto qué estará pensando. Tal vez se está preguntando qué estoy pensando. Tal vez nada."

hi "¿Cuánto por tus pensamientos?"

show rin basic_deadpan_close
with charachange

rin "¿Traes dinero contigo?"

hi "No lo creo."

show rin basic_deadpancontemplation_close
with charachange

rin "Entonces no creo que lo diré. No estoy pensando nada tampoco, así que estás de suerte. Excepto que ahora lo acabo de hacer."

"Ella frunce el ceño, mostrándose muy insatisfecha."

rin "Es difícil no pensar en nada. Pero es importante."

"Estoy a punto de preguntar por qué es importante cuando un tipo de edad camina hacia nosotros, con la apariencia de que tiene asuntos con Rin."

scene bg school_dormext_half at bgright
show nomiya smile at center
with locationchange

no_ "Buenas tardes. ¿Cómo vas?"

show nomiya smile at twoleft
show bg school_dormext_half at center
with charamove

show rin basic_awayabsent at tworight
with charaenter

rin "Puedo hacerlo."

"Rin no aparta sus ojos de la pared y responde tan naturalmente que solo puedo asumir que ellos se conocen."

"No he visto a este hombre antes, así que naturalmente me pregunto quién podrá ser. ¿Tal vez un maestro?"

"Su cabello se ha desteñido a un gris plateado, tanto que parece hecho artificialmente. Espero que ese no sea el caso."

"Pequeños anteojos redondos se sostienen en su nariz, pero parece que está constantemente mirando por encima de los lentes, en lugar de a través de ellos."

"Él está estudiando el mural atentamente sobre los susodichos anteojos."

show nomiya talk
with charachange

no_ "Bien, bien."

no_ "¡Qué composición tan audaz tienes aquí!"

"Se mueve para inspeccionar el mural más de cerca, hablando consigo mismo en una forma que vuelve obvio que quiere que escuchemos también."

show nomiya veryhappy
with charachange

no_ "Muy bien, realmente muy bien…"

"Realmente no sé qué sacar de eso pero Rin parece no preocuparse mucho. Ella está mirando alrededor de su espacio de trabajo, los varios recipientes de diferentes tonos esparcidos por todo el lugar."

show rin basic_deadpan
with charachange

rin "Hisao."

hi "¿Hmm?"

show rin basic_deadpannormal
with charachange

rin "Un poco más de este."

hi "Dame un segundo."

"Vierto una mezcla 50-50 de dos pinturas en el recipiente para crear más del mismo tono rosa pálido que Rin estaba usando para rellenar la forma de la cara de un hombre."

"Rin me observa haciéndolo, lo cual me pone nervioso de alguna forma. Su rostro es tan modesto que se siente como que ella solo está esperando que haga algo mal."

"El hombre gira para reconocerme también, luciendo sorprendido como si apenas hubiera notado mi presencia."

"… Tal vez lo hizo."

show nomiya talk
with charachange

no_ "Vaya, qué tal. ¿Quién podría ser usted?"

hi "Ah, soy un estudiante transferido a la clase 3-3. Hisao Nakai. Un gusto en conocerlo."

show nomiya frown
with charachange

no_ "La clase de Mutou, ¿eh? Bueno, ¡no consideraré eso en tu contra!"

play sound sfx_birdstakeoff

show nomiya veryhappy
with vpunch

"Él se ríe muy fuerte. Odiosamente fuerte. Unas cuantas aves pequeñas levantan vuelo de un árbol cercano."

show nomiya talk
with charachange

no_ "Soy Shinichi Nomiya, el maestro de arte."

"Así que este es el maestro de arte. En retrospectiva, creo que debí suponerlo. Incluso se ve como uno, en lo que a primeras impresiones se refiere."

show nomiya smile
with charachange

no "¿Cómo es que terminaste asistiendo a mi protegida?"


label es_choiceA33:
menu:
    with menueffect
    "Desearía saberlo…"
    "Solo terminé aquí con ella, creo.":


        return m1
    "Estoy interesado en el club de arte.":

        return m2


label es_A33a:

hi "Supongo que estoy un poco interesado en el club de arte."


"Lo dejo salir, un tanto inadvertidamente."

show nomiya talk
with charachange

no "¿Qué quieres decir?"

hi "Nada… específico."

hi "Me pregunto si podría ir en algún momento. Incluso si es solo para observar o algo."

hi "He estado pensando que debo unirme a algún club o algo, así que…"

"No es de ninguna forma un movimiento premeditado, sino que una vaga sensación de determinación ha estado creciendo dentro de mí esta semana pasada."

"Quiero hacer algo. Quiero pertenecer a algún lugar."

"Podría ser el club de arte, a pesar de mis limitaciones."

"El maestro parece complacido."

show nomiya veryhappy
with charachange

no "¿Oh? ¿Quieres unirte? Bueno, siempre damos la bienvenida a nuevas personas, desde luego."

no "Las reuniones de club son bastante normales. Estudiamos varios aspectos de las bellas artes y también las probamos con nuestras propias manos."

show nomiya frown
with charachange

no "O pies."

"Él tose avergonzadamente, pero a Rin parece no importarle. Siento un poco de consuelo por el hecho de que no soy el único con dificultades de vocabulario en esta escuela."

"Nomiya sale de su paso en falso revisando teatralmente el tiempo en su enorme y brillante reloj de bolsillo, y golpea su frente aún más teatralmente."

show nomiya veryhappy
with charachange

no "Realmente me debo ir ahora, pero si tienes preguntas, estoy seguro de que Tezuka las puede aclarar."

"De alguna forma, mencionar “aclarar” y Rin en la misma oración no se siente bien. Como sea, no digo mucho al maestro, pues parece que tiene prisa."

show nomiya smile
with charachange

no "Tezuka, estoy complacido de ver que este pequeño proyecto está marchando tan bien."

show nomiya talk
with charachange

no "Solo me detuve para recordarte que no te escapes mañana. He invitado a cierta gente al festival por ti, y estoy seguro de que a ellos les gustaría conocerte también."

show nomiya smile
with charachange

no "Espero verte el lunes entonces, Nakai."

stop music fadeout 6.0

hide nomiya
with charaexit

show rin basic_deadpannormal at center
show bg school_dormext_half at bgleft
with charamove

"El maestro se retira, y nos quedamos solos otra vez. Rin está aún pintando como si nada notable hubiera sucedido. Dado que de hecho nada pasó, me quedo preguntándome qué demonios sucede conmigo."

"El arte y yo no hemos trabajado bien juntos en el pasado, al menos a juzgar por las calificaciones que solía tener en la secundaria."

"Tal vez un club será diferente de una clase obligatoria. ¿Quién sabe?"

"Trato de encontrar algo significativo para preguntar sobre ello, pero sin resultados."

"Solo iré a una reunión del club y veré cómo resulta todo."

hi "¿Así que él invitó a algunas personas mañana solo para que vean tu pintura?"

show rin basic_absent
with charachange

rin "Él tiene a mucha gente de arte como amigos. A ellos les gusta hablar sobre arte."

show rin basic_awayabsent
with charachange

rin "Creo que quiere que hable sobre arte con ellos."

hi "De alguna forma, tengo la sensación de que no estás muy entusiasmada sobre ello."

"Rin se encoge de hombros evasivamente, pero aun así da una impresión de disgusto general a la idea de tener que discutir su pintura, o cualquier pintura, con otras personas."

show rin basic_deadpan
with charachange

play music music_rin fadein 5.0

rin "En realidad no me gusta hablar de arte. Ya es una forma de hablar sin hablar, ¿así que por qué molestarse en hablar sobre ello?"

hi "Puedo entender eso."

show rin basic_deadpannormal
with charachange

rin "Es como estar aburrido y hablar sobre estar aburrido, porque estás aburrido."

hi "No te estoy entendiendo."

show rin negative_spaciness
with charachange

rin "¿Has hablado alguna vez sobre estar aburrido? No tiene sentido y no es muy emocionante. Todo lo que puedes decir en realidad es “Estoy tan aburrido”. Una vez pasé una semana intentando pensar en algo valioso para decir sobre el aburrimiento."

rin "Fue la semana más aburrida que he tenido jamás."

hi "Pero eso le queda muy bien, ¿no lo crees?"

show rin basic_deadpan
with charachange

"Rin me mira, el tipo de mirada lacónica que parece que no significa nada, pero que sí."

hi "Como sea… no lo sé, supongo que solo raramente puedo pensar en algo que decir sobre el arte."

hi "Quiero decir, como este que estás haciendo ahora. No tengo idea de qué pensar sobre ello, excepto que se ve bien. ¿Sobre qué es esta pintura?"


show rin basic_deadpannormal
with charachange

rin "No es sobre nada en absoluto."

"…"

show rin basic_deadpandelight
with charachange

rin "Eso es lo que me gustaría decir. Así que lo dije."

show rin basic_deadpannormal
with charachange

rin "Pero eso fue una pequeña mentira. Lo dije de todas maneras porque como que me gustaría que fuera verdad."

rin "El maestro quiso que hiciera esto, pero no tuve ninguna idea. Traté de tener algunas, pero no pasó nada."

show rin negative_spaciness
with charachange

rin "Así que ahora esta es una pintura sin ninguna idea."

hi "Pero… ¿qué estás pintando, entonces?"

show rin basic_absent
with charachange

rin "Ni idea."

show rin basic_delight
with charachange

rin "Ahora que lo pienso, creo que le llamaré a esto “Ni idea”."

show rin negative_worried
with charachange

rin "Ah, ya empecé a pensar otra vez. Esto es malo."

show rin basic_absent
with Dissolve(0.15)

show rin negative_worried
with Dissolve(0.1)

show rin negative_worried
with Dissolve(0.05)

show rin basic_absent
with Dissolve(0.05)

show rin negative_worried
with Dissolve(0.05)

show rin basic_absent
with Dissolve(0.05)

show rin negative_worried
with Dissolve(0.05)

show rin basic_absent
with Dissolve(0.05)

show rin negative_worried
with Dissolve(0.1)

show rin basic_absent
with Dissolve(0.15)

show rin negative_worried
with Dissolve(0.5)

"Ella sacude su cabeza vigorosamente por un rato, tratando de sacar “el pensar” fuera de su cabeza. Aquel cabello rojo ámbar vuela descontroladamente por doquier."

show rin basic_deadpannormal
with charachange

rin "Esto es el porqué tenía a Emi ayudándome. Ella facilita no pensar en nada."


rin "Ya sabes, cómo ella solo habla habla habla sobre nada por horas. Es como si su cabeza estuviera hecha de gelatina de espuma de baño con aroma a goma de mascar."

show rin basic_deadpandelight
with charachange

rin "Tú eres más o menos lo mismo, pero no realmente. Es de mucha ayuda si te quedas aquí."

stop music fadeout 5.0

"No estoy seguro de si eso es un cumplido o no. Probablemente no es ninguno de los dos; con Rin siendo la persona tan sobradamente neutral que es."

hi "Así que ¿hay algo específico que te gustaría que hiciera para hacerte no pensar?"

show rin basic_deadpan
with charachange

rin "Solo sé."

hide rin
with charaexit

"Así que sin saber qué debería hacer, solo me siento en una caja vacía a verla continuar con la pintura, dando la vuelta ociosamente a las páginas del libro sobre beber cerveza."

play music music_dreamy fadein 1.0

scene bg mural_part
show rin negative_spaciness_close at tworight
with locationchange

"Rin tiene una expresión serena en su rostro, sus ojos verde oscuro escondiendo detrás de ellos lo que pueda estar pensando. No, espera, supuestamente no está pensando en nada, ¿cierto?"

"Silenciosamente canturrea una melodía, interrumpiéndola de vez en cuando con amables peticiones por más pintura u otro tipo de brocha."

"Su concentración es admirable, a pesar de que parece estar privada del sueño y bajo presión para terminar el trabajo."

"Centímetro a centímetro la pintura gana más forma, detalles siendo añadidos sobre detalles, colores entrelazándose entre ellos, llenando los espacios vacíos, creciendo uno sobre otro."

"Me encuentro pensando sobre inspiración y motivación para crear arte, otra vez."

"¿Dónde obtiene uno ideas? No surgen de la nada, y no creo que haya musas que mágicamente inyectan un poco de inspiración en tu cabeza."

"Las ideas tienen un origen y un propósito."

"Entre más pienso sobre ello, más convencido estoy de que Rin está mintiendo sobre su mural, o al menos está tergiversando la verdad. Tal vez ella misma no se dé cuenta."

"No puedes hacer nada creativo sin tener una idea de qué es lo que vas a crear. Eso iría contra la definición."

"Cada trazo debe decidirse ser dibujado. Incluso si es hecho al azar, entonces eso, también, es una decisión consciente."

"Así que sus pinturas, incluso esta, deben basarse en tener algún objetivo deliberado o una idea de qué pintar."

"Si la idea de Rin es no tener idea, tal como dijo, ¿eso cuenta como tener una idea?"

"¿Una paradoja lógica? Eso parece ser el modus operandi de Rin para la mayoría de sus interacciones, así que no me sorprendería si ni siquiera ha notado esto ella misma."

"Me pregunto si debería decirlo, pero no estoy seguro de querer participar en un argumento de lógica con esta chica."

"Uno de nosotros probablemente terminaría haciendo cortocircuito con bastante rapidez, así que descarto la idea."

show rin basic_awayabsent_close
with charachange

show rin negative_spaciness_close
with charachange

"Rin se está retorciendo y arrastrando los pies, inquieta."

show rin negative_annoyed_close
with charachange

show rin negative_spaciness_close
with charachange

"Incluso su usual semblante en blanco se descompone ocasionalmente en expresiones bastante difíciles de interpretar, de ese tipo que uno simplemente no revela por accidente."

show rin negative_annoyed_close
with charachange

hi "¿Todo bien?"

rin "Sí. No."

rin "Mi espalda empezó a doler otra vez."

rin "Esta pintura es demasiado grande, después de todo, y es difícil pintar en esta posición."

hi "¿Quieres tomar un descanso?"

show rin basic_deadpanupset_close
with charachange

rin "Después de que termine esta parte."

show rin negative_annoyed_close
with charachange

"Desde luego, ella no toma un descanso, y no traigo de vuelta el tema otra vez porque eso sería completa y absolutamente inútil."

scene bg school_dormext_half_ss
with locationchange

"Rin continúa su trabajo y me quedo con ella: me gusta verla pintar, y ahora voy a ser un miembro del mismo club en el que ella está."

stop music fadeout 4.0
$ renpy.music.set_volume(0.5,0.0, "ambient")
play ambient sfx_cicadas fadein 3.0

scene bg school_dormext_full_ni
with Dissolve(3.0)

"Cuando declara el mural terminado, es ya tan oscuro que no tengo idea de cómo puede notarlo."

"No hay celebración, ni un sentido general de un trabajo bien hecho, solo un cansado y lacónico “Ya acabé” y luego ambos vamos a dormir."


stop ambient fadeout 3.0

$ suppress_window_after_timeskip = True

scene black
with Dissolve(3.0)


label es_A33b:

hi "Me sigo preguntando eso mismo. La falta de algo mejor que hacer, probablemente."

show nomiya veryhappy
with charachange

"Él deja salir una carcajada, luego revisa su reloj."

show nomiya smile
with charachange

no "Realmente me debo ir ahora. Tezuka, estoy complacido de ver que este pequeño proyecto está marchando tan bien."

show nomiya talk
with charachange

no "Solo me detuve para recordarte que no te escapes mañana. He invitado a cierta gente al festival por ti, y estoy seguro de que a ellos les gustaría conocerte también."

show nomiya smile
with charachange

no "Además, la reunión del club del lunes se suspende, dado que voy a estar fuera del pueblo. Supongo que pueden hacer algo entre ustedes, si quieren."

hide nomiya
with charaexit

stop music fadeout 4.0

show rin basic_deadpannormal at center
show bg school_dormext_half at bgleft
with charamove

"Él se va, dándose vuelta con extravagancia, después alejándose caminando tan dramáticamente como es posible caminar."

"Qué maestro tan extraño."

hi "Me voy también. Te veo luego, Rin."

"Levantando la mano, doy vuelta para subir las escaleras a los dormitorios."

"Tal vez, si puedo terminar de leer estos libros hoy, el día de mañana entero estará libre para el festival."

$ suppress_window_after_timeskip = True

scene black
with Dissolve(3.0)




label es_A34:

scene bg school_dormext_half at bgright
show rin basic_deadpan at tworight
show emi basic_annoyed at twoleft
with None

stop music fadeout 6.0

show emi basic_closedgrin
with charachange

emi "Necesitamos ir por más, entonces."

"Abro mi boca para decir que de hecho, no somos necesarios los dos para tan simple tarea como encontrar otro bote de azul Prusia, pero Emi ya ha agarrado mi brazo y comenzado a arrastrarme."

hide emi
with charaexit

"Agito la mano hacia Rin, quien no parece haber notado que los dos nos estamos yendo."

play ambient sfx_crowd_outdoors fadein 0.5

scene bg school_courtyard
show crowd
with locationskip

"Bueno, lo notará cuando vaya por el azul Prusia y se encuentre con que aún no está ahí."

scene bg school_lobby
show crowd
with locationskip

play ambient sfx_crowd_indoors fadein 0.5

"Tal vez."

scene bg school_staircase2
with locationskip

"…"

scene bg school_hallway3
show crowd
with locationskip

"Probablemente no, de hecho."

stop ambient fadeout 2.0

scene bg school_classroomart
with locationskip

"Mientras estoy ocupado pensando en lo extraña que es Rin, Emi ha estado arrastrándome de regreso al salón de arte."

"Siento que estoy comenzando a quedarme sin aliento."

hi "¿Cuál es la prisa?"

show emi basic_confused at center
with charaenter

emi "¿Eh?"

"Emi está dándome una mirada inquisitiva, como si estuviera tratando de descifrar algo."

hi "Es solo que pareces estar con prisa."

hi "No creo poder seguir el ritmo."

"La comprensión nace en su rostro."

play music music_emi fadein 0.3

show emi excited_proud
with charachange

emi "No estás sin aliento, ¿o sí?"

"Hay casi una acusación juguetona en su tono."

"Estoy tentado a negarlo, pero entonces me doy cuenta de que he estado respirando pesadamente desde que nos detuvimos."

"Supongo que es un tanto obvio."

hi "Un poco. No todos pueden estar en forma, ¿sabes?"

hi "De todo ha de haber, ¿cierto?"

show emi basic_annoyed
with charachange

"Emi frunce el ceño. No es particularmente un buen fruncimiento."

hi "Eh, eso es…"

hi "¿Debo… ponerme en forma?"

"No es que aún no haya decidido tratar eso."

"Después de esa agitación en la pista me doy cuenta de que hay una necesidad real de obtener algún tipo de hábito de correr."

"Estaba, después de todo, sintiéndome muy bien hasta que tuve mi falsa alarma."

"Bueno, de hecho no lo estaba. Pero fue… ¿divertido?"

"Mientras tanto, mi comentario parece ayudar a Emi a llegar a algún tipo de decisión."

show emi basic_closedgrin
with charachange

emi "Bueno, eso es todo entonces."

stop music fadeout 1.0

show emi basic_annoyed
with charachange

"Ella me da una mirada seria."

emi "Te me unirás."

"…"

hi "Disculpa, ¿qué has dicho?"

show emi basic_grin
with charachange

emi "Por las mañanas."

emi "Tú y yo somos ahora compañeros de carreras."

show emi basic_closedhappy
with charachange

emi "Ya tengo una rutina bien planeada. De hecho…"

play sound sfx_paper

"Ella muestra una arrugada hoja de papel."

show emi excited_amused
with charachange

emi "La tengo justo aquí conmigo."

play music music_running

"Tomo la hoja de papel y le doy una pasada rápida."

"Tiempos, fechas y vueltas, todo dispuesto."

"Un lento incremento de solo unas pocas vueltas al día a…"

"Por Dios, ¿espera tenerme corriendo maratones?"

"¿Y dónde encontró el tiempo para armar todo esto?"

"¿Y cuánto tiempo ha estado planeando esto, de cualquier modo?"

hi "¿Has estado planeando esto?"

show emi sad_shy
with charachange

emi "Un poco."

show emi sad_grin
with charachange

emi "¡Pero en realidad es idea del enfermero!"

show emi basic_closedgrin
with charachange

emi "¡Él me dijo que te vigilara para asegurarse de que te ejercitaras tal como te dijo que lo hicieras!"



label es_A34a:

"¿Una vasta conspiración?"

"Tal vez Kenji está conectado a algo aquí…"

hi "Esto parece demasiado para solo “mantenerme vigilado”."

show emi sad_grin
with charachange

emi "Bueno, para ser honesta he estado tratando de encontrar un compañero de carreras en las mañanas desde hace ya un tiempo."

"¡Por Dios, Kenji! ¡Si solo pudieras ver el esquema revelándose!"

hi "¿Para qué necesitas a un compañero, de cualquier forma?"

show emi basic_annoyed
with charachange

emi "Es más fácil mantener un plan de entrenamiento si no eres el único haciéndolo."

emi "¿No es obvio?"

emi "Tienes menos probabilidades de abandonar si alguien más está contando contigo para estar ahí, ¿cierto?"

hi "Ya veo. Y esto no solo te mantendrá corriendo, sino además asegurará que yo me mantenga corriendo también."

hi "Lo que quiere decir que estaré obedeciendo al enfermero…"

show emi excited_proud
with charachange

emi "¡… y te estaré vigilando justo como él lo pidió!"

show emi basic_closedgrin
with charachange

emi "Captas rápido, Hisao."

hi "¿Y si me niego?"

"No tengo intenciones de negarme, por supuesto."

"Pero tengo que poner al menos una resistencia simbólica a ese plan tan magistralmente ejecutado."

show emi basic_grin
with charachange

emi "Bueno, si te rehúsas tendría que hacer pucheros."

emi "Y tendrías que vivir con ser el tipo que hizo a Emi Ibarazaki hacer pucheros."

show emi basic_closedgrin
with charachange

emi "No quieres eso en tu conciencia, ¿o sí?"

show emi sad_depressed
with charachange

"Como para demostrarlo, Emi empieza a hacer pucheros."

"Es la más adorable, y desgarradora cosa que jamás he visto."

hi "¡Muy bien! ¡Lo haré!"

hi "Solo… ¡no hagas eso!"

hi "¡Siento como si acabara de golpear a un cachorro!"

show emi basic_closedgrin
with charachange

emi "Así que está decidido, ¿cierto?"

emi "¿Tú vas a ser mi compañero de carreras?"

emi "¿Vas a seguir el plan de entrenamiento?"

emi "¿Y el plan alimenticio?"

hi "¿Plan alimenticio?"

show emi basic_grin
with charachange

emi "Sí, ¡el plan alimenticio!"

show emi excited_proud
with charachange

emi "Tienes que comer sanamente si vas a ponerte en forma, ¡¿sabes?!"

"Examino la rutina de entrenamiento más atentamente."

hi "No veo un plan alimenticio aquí."

show emi basic_shock
with charachange

emi "¡Oh cierto! ¡Olvidé darte eso!"

play sound sfx_paper

show emi excited_amused
with charachange

"Otra hoja arrugada de papel es expuesta y entregada."

"Es un poco menos detallada."

show emi excited_happy
with charachange

emi "Tuve al enfermero ayudándome a hacerla."

"La cantidad de dedicación que el enfermero tiene para mantenerme con buena salud es bastante abrumadora."

"No conozco muchos enfermeros de escuela que pondrían a una de sus estudiantes a espiarme, mucho menos que ayudarían a hacer un plan alimenticio."

"Una vez más, supongo que no estoy en una escuela normal."

"Y tal vez no es algo tan malo."

"Y una vez más, este plan alimenticio parece simplemente eliminar todo lo que será ofrecido en el festival mañana."

"Hmm."

hi "Así que ¿cuándo empezamos a correr?"

show emi basic_grin
with charachange

emi "Después del festival."

hi "¿Justo después? ¿Qué tal si he tenido algo de comer ahí? Podría agarrar un dolor de estómago, ¿sabes?"

show emi basic_annoyed
with charachange

emi "Quise decir al día siguiente del festival."

hi "Ya lo sabía."

"¿No había algo que se supone deberíamos estar haciendo?"

hi "¡Oh! Supongo que debemos conseguir esa pintura para Rin, ¿eh?"

show emi basic_shock
with charachange

emi "¡Oh no! ¡Se me olvidó!"

stop music fadeout 8.0

scene bg school_dormext_half_ss
with shorttimeskip

"Para cuando conseguimos la pintura y volvemos al mural, Rin ya se ha alejado sin rumbo."

"Oh bueno."

"Emi y yo decidimos separarnos ahí, dejando la pintura en el suelo."

"Rin la encontrará. Cuando sea que regrese, de todos modos."

scene bg school_dormhisao
with locationskip

"El festival es mañana. En realidad estoy un poco emocionado sobre eso."

"Al mismo tiempo, la semana me ha dejado muy cansado, así que leo un poco y después voy a la cama."

$ suppress_window_after_timeskip = True

scene black
with Dissolve(3.0)


label es_A34b:



stop music fadeout 1.0

"Maldición, ¿por qué toda esta gente insiste en meterse en mis asuntos? Supongo que el enfermero tiene permiso, incluso obligación pero…"

hi "¿Sabes?, no creo que eso sería una buena idea."

hi "Este es mi problema, realmente no quiero hacer a nadie parte de él."

hi "Tengo que resolverlo por mí mismo."

show emi sad_depressed
with charachange

emi "¿Estás enojado por lo de ayer?"

"Ella está haciendo pucheros, mirando distante como un cachorro herido. No podría estar enojado ahora, incluso si quisiera."

hi "No, no es eso. En todo caso, fue mi culpa."

"Me apoyo contra la pared, apartando la mirada de Emi."

hi "Yo solo… no lo sé, se siente como una mala idea."




label es_A35:

scene bg school_scienceroom at bgleft
show hanako emb_downtimid at right
with None

"Pero ¿por qué Lilly la dejaría a su suerte? Parece estar un poco fuera de lo común, por la reacción de Hanako."

"…"

"… Ah, es cierto. Creo que Lilly mencionó algo sobre ir al pueblo hoy antes de que Rin se topara con nosotros."

"La idea sobre esa caminata me hace mirar afuera."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene bg misc_sky at Fullpan(15.0)
with locationchange

"El sol brillante y las esporádicas personas deambulando y disfrutando la tarde me hacen anhelar salir de la escuela, o al menos hacer algo además de sentarme aquí."

"Cediendo a uno de mis peores vicios, la postergación, decido que historia es una asignatura mejor estudiada un domingo. O un lunes. O en cualquier otro día menos este."

"Doy un gruñido mientras me levanto de mi asiento, debatiendo brevemente entre ir o no a pasar el rato con Kenji."

"No me parece del tipo “disfrutando el buen clima afuera con otros”, en verdad. Creo que me reuniré después con él."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

scene bg school_scienceroom at bgleft
with Dissolve(1.5)

"Cambiando planes, brevemente considero la idea de hablar con Hanako, pero para cuando veo su asiento, está vacío. Debe de haberse ido a la biblioteca."



label es_choiceA35:
menu:
    with menueffect
    "Debe de haber algo para matar el tiempo…"
    "Ir a caminar al pueblo.":


        return m1
    "Ir a la biblioteca.":

        return m2

label es_A35a:

"Seguir a Hanako a la biblioteca parece un poco intrusivo. Hubo una razón por la que dejó el salón, después de todo."

"Y aparte de eso, quiero encontrarme con Lilly. Al menos, me gustaría agradecerle por hacerse cargo de mí a pesar de sus otros, obviamente agotadores, deberes."

"Creo que iré a caminar por el pueblo. Con un poco de suerte, debería ser capaz de hallar a Lilly. El ejercicio me hará algún bien también."

play music music_tranquil fadein 3.0

scene bg school_courtyard
with locationskip

"Caminando a través del patio de la escuela al portón, doy un pequeño saludo con la cabeza a unos compañeros de clase, el gesto es devuelto amablemente."

"Inclusive desde aquí, los gritos de los miembros del club deportivo pueden ser escuchados. Por el volumen del ruido, la pista debe estar abarrotada justo ahora."

"Recuerdo lo que dijo Lilly ayer sobre haber sido arrojado justo en medio de atareados momentos para la escuela."

"Mientras trato de orientarme y ponerme al corriente con los estudios que he perdido, todos los demás están haciendo actividades normales de escuela. La sensación de ser un forastero aún no se ha disipado. Al menos no todavía."

"Bueno, supongo que no todo es malo."

"Esta es una escuela privada, y eso es fácil notarlo cuando se camina en los exteriores."
"No solo los terrenos escolares son enormes, sino también los edificios mismos están inmaculados y un tanto alejados de los bloques de concreto que se encuentran a montones en las escuelas públicas."

"También está el hecho de que hay un sentido mucho más fuerte de comunidad aquí, o al menos una atmósfera más amistosa. En mi antigua escuela, era generalmente aceptado que la gente se mantuviera en su pequeña pandilla y hasta ahí."

scene bg school_gate
with locationchange

"Eventualmente alcanzo el portón, y comienzo a caminar por la carretera y hacia el pueblo."

scene bg suburb_roadcenter
with shorttimeskip

"Bueno, eso fue muy productivo."

"Habiendo visto una buena porción del pueblo, inclusive las casas en las colinas en las afueras, decido dar una caminata por el parque antes de regresar."

"Al vivir en la ciudad toda mi vida, la ausencia total de hombres de negocios elegantemente vestidos y chicas vestidas a la moda me parece increíblemente inusual."

"Todo lo que hay para ver aquí son la extraña persona anciana arrastrando los pies por la acera y una variedad de parejas de mujeres de mediana edad ocupadas hablando fuera de las pequeñas tiendas."

stop music fadeout 8.0

"Sin embargo, andar a lo largo del camino hacia el parque rápidamente me distrae de ellos, haciéndome notar que tal vez me he presionado más allá de lo que debería para ver tanto como me fuese posible."

"Mientras comienzo a respirar con dificultad y mi pecho se aprieta más y más, abandono la posibilidad de seguir adelante."

play ambient sfx_parkambience fadein 1.0

scene bg suburb_park
with locationskip

"Después de una mirada rápida alrededor del parque mientras entro, tomo asiento en una tambaleante banca vieja que noto cerca de un par de máquinas expendedoras."

"Por unos minutos al fin me siento con mi cabeza gacha, forzándome a respirar profundamente. Me siento más como un viejo que como un adolescente que debería estar en la plenitud de su vida."

"La estancia en el hospital, la cirugía y la medicación deben estar pasándome factura. Maldita sea."

"Eventualmente, mi respiración regresa a la normalidad y los músculos en mi pecho se relajan, no sin una justa cantidad de alivio. Supongo que esto significa el fin de mi pequeño descanso, en cualquier caso."

stop ambient fadeout 1.0

scene bg suburb_shanghaiext
with locationchange

"Hay un café en la esquina de más lejos, así que me detendré ahí para saciar mi sed antes de volver."

play sound sfx_storebell

scene bg suburb_shanghaiint at bgright
with locationchange

play music music_dreamy fadein 2.0

"Una campanilla sobre la puerta señala mi llegada a un mostrador vacío."

"Por unos instantes me quedo de pie esperando, de vez en cuando mis ojos merodean de un extremo del mostrador al otro buscando por una campanilla de servicio."

show yuukoshang neutral_down at center
with charaenter

"Eventualmente una puerta un poco atrás del mostrador abre, la persona emergiendo de ella me toma por completa sorpresa."

hi "Yu… ¿Yuuko?"

hi "Hola, no tenía idea de que trabajaras aquí."

"En verdad no tengo ni idea de cómo dirigirme a ella tampoco, dado que ella es técnicamente personal de la escuela al igual que, aparentemente, una mesera."

show yuukoshang neurotic_up
with charachange

yu "Ah, sí, eh…"

"Ella rápidamente avanza hacia el mostrador, antes de lanzar la mitad superior de su cuerpo hacia el suelo en una exagerada reverencia."

show yuukoshang closedhappy_down
with charachange

yu "¡Bienvenido al Shanghái! ¿Puedo tomar su orden?"

"Directo al grano, según veo."

hi "No lo sé… bueno, ¿un poco de café, por favor?"

show yuukoshang neutral_down
with charachange

yu "Sí, desde luego. Lo haré de inmediato y se lo traeré cuando esté listo."

hi "Ah, gracias."

"La formalidad de Yuuko me toma desprevenido. Ella parece tomar su trabajo muy seriamente."

hide yuukoshang
with charaexit

"Obedeciendo sus instrucciones, me doy vuelta y rápidamente veo alrededor por una mesa libre. Considerando que el café parece estar vacío, esta es una tarea fácil de completar."

show bg suburb_shanghaiint at bgleft
with charamove

"Mientras camino hacia una mesa adyacente a la ventana, descubro un destello de amarillo entre uno de los divisores de las mesas."

show lilly basic_smileclosed at twoleft
show akira basic_lost at tworight
with charaenter

"Desde luego, no más de una mirada es necesaria para asegurar que es una cierta Satou en la mesa. Dicho esto, no reconozco a la figura trajeada del otro lado de la mesa en donde ella está."

"Rubia, de piel clara y solo un poco más chica, él… ¿ella? Creo que ella, debe de ser un familiar."

"Puesto que las dos están prácticamente calladas mientras la figura trajeada toma un trago de su taza de café, decido saludar a Lilly. Una parte de mi venida aquí fue para encontrarla, después de todo."

hi "Hola, Lilly."

show lilly basic_smile
with charachange

li "… ¿Hisao?"

hi "Sí. Es bueno verte otra vez."

show akira basic_smile
with charachange

"La chica trajeada mira hacia arriba, notando mi uniforme con una sonrisa relajada."

aki_ "¿Se conocen?"

hi "Eso… supongo."

"Es la mejor aproximación a nuestra relación que puedo pensar."

show lilly basic_smileclosed
with charachange

li "Hmm… ¿Gustas tomar asiento?"

"Ella dice esto al aire a un lado mío, pero el mensaje es suficientemente claro y tomo asiento a su lado."

show lilly basic_weaksmile
with charachange

li "Supongo que algunas presentaciones serían prudentes."

show lilly basic_smile
with charachange

li "Hisao, ella es Akira Satou, mi hermana mayor. Akira, él es Hisao Nakai, otro estudiante de Yamaku."


"Parece que mi suposición fue correcta. La recién introducida Akira da un asentimiento, el cual yo regreso."

"Lo que no regreso, sin embargo, es la casi analítica mirada con la que ella me observa de arriba a abajo."

show lilly basic_smile at left
show akira basic_smile at right
with charamove

show yuukoshang neutral_down at center
with charaenter

"Mientras lo hace, Yuuko camina hacia la mesa y cuidadosamente coloca el café en la mesa antes de dar una reverencia y retirarse."

hide yuukoshang
with charaexit

show lilly basic_smile at twoleft
show akira basic_smile at tworight
with charamove

"Acercando gentilmente mi mano a un lado de la taza, me doy cuenta de que ya está a buena temperatura para beber. Después de dar un sorbo, el sabor termina siendo tan bueno como la temperatura."

"Yuuko parece ser mucho mejor en esto que en ser bibliotecaria."


"Tomo un buen y largo trago antes de relajarme en el asiento."

"Toma apenas unos segundos para que el examen de Akira llegue al final. Aparentemente aburriéndose rápidamente con la actividad, ella voltea hacia su hermana."

show akira basic_boo
with charachange

aki "Así que, ¿cómo está la escuela últimamente?"

"Parece que Akira está completamente despreocupada con que alguien que no conoce del todo esté escuchando todo lo que dicen."

"No es que me moleste. Dejándolas con su charla, me recargo y continúo bebiendo el café complacientemente aromático."

show lilly basic_smileclosed
show akira basic_smile
with shorttimeskip

aki "Suena como que está muy ocupado para ti, entonces."

show lilly basic_smile
with charachange

li "Al menos ya no estoy cocinando más tus comidas después de la escuela."

"Mientras hablan, lentamente me doy cuenta de que soy completamente incapaz de medir las emociones de Lilly a través de sus ojos; tal como haría con cualquier otra persona."

"Se vuelve ligeramente inquietante mientras me enfoco subconscientemente en ese hecho."

show akira basic_lost
with charachange

aki "Vaya, qué frialdad. ¿No estabas cocinando solo para ti de cualquier forma? Solo recibí sobras siempre."

show lilly basic_displeased
with charachange

li "Ese no es el punto… ¿Estás arreglándotelas para alimentarte, al menos?"

show akira basic_resigned
with charachange

aki "Puedo cocinar sin volarme a mí misma, ¿sabes?"

show akira basic_annoyed
with charachange

aki "Más o menos."

show lilly basic_listen
with charachange

li "Eso es…"

show akira basic_laugh
with charachange

aki "¡Jajaja! Está bien, está bien. Necesitaba aprender algún día de cualquier modo."

show lilly basic_listen at left
show akira basic_laugh at right
with charamove

show yuukoshang neurotic_up at center
with charaenter

yu "Ah, ¿Lilly?"

show lilly basic_smile
show akira basic_boo
with charachange

"Todos los presentes somos momentáneamente distraídos por Yuuko, quien coloca una taza de té en la mesa para Lilly."

hide yuukoshang
with charaexit

show lilly basic_smile at twoleft
show akira basic_boo at tworight
with charamove

"Tomando un momento para mirar su reloj, Akira se levanta de su asiento y me da un asentimiento rápido."

show akira basic_smile
with charachange

aki "Bueno, mejor me voy. Fue bueno hablar contigo, Lilly."

show lilly basic_oops
with charachange

li "Akira, ¿tienes que…?"

"Lilly luce genuinamente triste con su hermana dejándonos repentinamente. En verdad parece como que ella podría tener una idea equivocada."

show akira basic_resigned
with charachange

aki "Lo siento, necesito volver al trabajo. Ellos estarán sobre mi cuello otra vez si no regreso rápidamente."

"Tan informal… El aspecto aseado y arreglado de Akira le daría a cualquiera la impresión errónea de ella."

show lilly basic_concerned
with charachange

li "Adiós, Akira…"

show akira basic_smile
with charachange

aki "Vamos, no pongas esa cara tan triste. Estaré de vuelta pronto otra vez. Nos vemos."

hide akira
with charaexit

"Con eso, ella sale tranquilamente del Shanghái con su mano en alto."

"Lilly aún luce bastante deprimida, así que trato de hacer una pequeña plática en un esfuerzo por alejar su mente de eso."

show lilly basic_concerned at center
show bg suburb_shanghaiint at center
with charamove

hi "Ella parece agradable."

show lilly basic_displeased
with charachange

li "Solíamos vivir juntas, pero ahora que vivo en la escuela difícilmente podemos vernos."

"A pesar de que Lilly ha sido bastante afable, aún no sé realmente mucho sobre ella. En retrospectiva, es sorprendente lo mucho que ella ha extraído de mí, en verdad."

hi "¿Solían vivir juntas? ¿Era en algún lugar por aquí?"

li "Era bastante alejado al sur, así que el viaje a Yamaku era relativamente largo."

show lilly basic_reminisce
with charachange

li "Con sus horas de trabajo aumentando y Yamaku estando tan lejos, no hubo otra opción más que mudarme a los dormitorios."

"Bueno, eso explica su plática sobre cocinar. Evidentemente recuperando su compostura, ella se anima un poco… al menos, en parte."

show lilly basic_weaksmile
with charachange

li "¿Deduzco que estás más descansado ahora?"

hi "¿Disculpa?"

show lilly basic_smileclosed
with charachange

li "Suenas menos exhausto que al inicio cuando entraste aquí."

"Para lograr captar mi respiración así… debe tener muy buen oído."

hi "Seguro. Terminé caminando por todo el pueblo, a pesar de haber planeado solo tomar una corta caminata hacia aquí."

"Recordando mi sed por la caminata, me inclino hacia adelante para tomar un sorbo."

play sound sfx_teacup

"Sin más rodeos, Lilly empieza a tomar su taza de té de fuerte olor."

"Creo que mejor me voy regresando a Yamaku. Hay apenas tiempo como para entretenerme estudiando, y quiero dormir bien por la noche antes del festival."

stop music fadeout 4.0

"Levantándome de mi asiento, tomo la taza con restos de café de la mesa."

show lilly basic_surprised
with charachange

li "¿Te vas?"

hi "Sí. ¿Vas a regresar también? Se está volviendo un poco tarde."

"Por un momento ella se detiene, antes de elevar su cabeza sobre la taza de té como si estuviera mirándome."

play music music_lilly fadein 3.0

show lilly basic_smile
with charachange

li "Yuuko, ¿podríamos tener una taza más de café?"

yu "Muy bien, ¡la traeré de inmediato!"

hi "Eso no es… sutil."

show lilly basic_giggle
with charachange

"Ella da una corta risa a mi franca evaluación de su maniobra. Es sorpresivamente infantil y despreocupada, dada su, de otra forma, tranquila apariencia."

"Al final, sin embargo, tengo pocas razones para negarme. Para ser honesto difícilmente puedo decir no, tomando en consideración todas las cosas."

"Dando un fingido suspiro, tomo asiento frente a ella."

hi "¿Quieres compañía, entonces?"

show lilly basic_cheerful
with charachange

li "Hmm… diría que es más que me estaba preguntando…"

"Veo que está en modo inquisitivo, otra vez. Ella en verdad parece estar inusualmente interesada en mí, o al menos curiosa."

show lilly basic_smile
with charachange

li "¿Tienes hermanos?"

"No exactamente una inesperada tangente."

hi "No, hijo único. Para ser honesto, la idea de tener a alguien tan cercano me hace sentir un poco de envidia."

show lilly basic_smileclosed
with charachange

li "Interesante…"

"Elevo una ceja, lo cual por supuesto pasa sin ser visto. El corto silencio comunica la pregunta lo suficientemente bien."

show lilly basic_smile
with charachange

li "Es solo que otros han dicho lo mismo antes."

li "Es un tema complicado para tratar de pensar objetivamente, tomando en cuenta que yo siempre he tenido a alguien así."

"Puedo entender la mayor parte de lo que Lilly quiere decir, tomando en cuenta que sería difícil colocarse fuera de una situación en la que han estado toda su vida."

"Ella y su hermana deben tener una relación muy cercana."

"Esforzándose por interrumpirnos lo menos posible, Yuuko diligentemente se acerca y coloca una taza en la mesa."

"Lilly le agradece mientras vuelvo a sentarme, asimilando a esta desconcertante chica frente a mí."

"A pesar de parecer siempre en guardia y en control de sí misma cuando habla a otros, ella tiene una curiosidad casi infantil acerca de otras personas."

"Dicho eso, aquellos raros momentos en que ella parece bajar su guardia ligeramente son los más clarificadores sobre su forma de pensar."

"Extendiéndome por mi bebida, me doy cuenta de algo que probablemente debí haber notado antes."

"… Creo que estoy comenzando a sentir algo de curiosidad por ella."

stop music fadeout 2.0

scene bg school_gate_ni
with shorttimeskip

play ambient sfx_cicadas fadein 0.5

"A pesar de ir a buen ritmo, es ya de noche para cuando alcanzo los largos portones de hierro frente a la escuela."

"Si bien es bueno tener bastante tiempo para deambular por los alrededores por el hecho de vivir justo al lado de la escuela, no puedo evitar sino sentir que solo unos pocos estudiantes se toman realmente la oportunidad."

scene bg school_courtyard_ni
with locationchange

"Comparado al número de estudiantes que veo proliferando alrededor del campus durante el tiempo libre, es sorpresivamente raro ver a alguien por el pueblo."

"Dado el gran número de comodidades e instalaciones que la escuela ofrece, muchos de ellos podrían simplemente no ver punto alguno en aventurarse afuera, y mucho menos personas tales como Hanako y Kenji."

"Me hace preguntarme si estudiantes como Shizune, Misha y Lilly son las excepciones para esta escuela, en lugar de la norma."

stop ambient fadeout 1.0
scene bg school_dormhallway
with locationskip

"Mientras deambulo de vuelta a mi dormitorio, continúo comparando mi vieja escuela con Yamaku. Mientras lo hago, comienzo a estar sorprendido de que logré estar tan acostumbrado a todo lo que me ha sucedido."

$ suppress_window_after_timeskip = True

scene black
with Dissolve(3.0)




label es_A36:

window hide None

scene black
with dissolve

play sound sfx_doorknock

scene bg school_dormhisao
with openeye

window show

"Cinco minutos después de las 8, unos golpes increíblemente fuertes me sacuden de mi sueño. Vienen de fuera de mi puerta."

scene bg school_dormhallway
show shizu behind_blank at tworight
show misha hips_smile at twoleft
with locationchange

play music music_comedy fadein 0.3

"Rápidamente, abro la puerta para ver a Shizune y Misha paradas una al lado de la otra. Ambas parecen un poco desgastadas, aunque es más visible en Misha."

hi "¿Cuál de ustedes dos tocó?"

"Interrogo, haciendo eco a la pregunta que debe estar en la mente de todos en el edificio completo."

show misha hips_grin
with charachange

mi "Ajajaja, ¡eso no es importante, Hicchan!"

"Ella rápidamente la desestima sin siquiera pestañear."

show misha hips_smile
with charachange

mi "¿Oh? ¿Aún estás en tu pijama, Hicchan? ¿Entonces tú no te levantas a las ocho?"

"Noto que su cabello está mojado. Sus rizos están apenas manteniendo su forma."

hi "No, pensé que dormiría hasta un poco tarde pues es fin de semana y todo eso, y he estado seriamente privado del sueño esta semana."

"Me pregunto si no notó el veneno en mis palabras."

show shizu basic_normal2
with charachange

shi "…"

show misha hips_grin
with charachange

mi "¡Entonces es algo bueno que te hayamos venido a despertar!"

show shizu adjust_happy
with charachange

shi "…"

show misha sign_smile
with charachange

mi "Como sea, Hicchan, supongo que te gustaría saber por qué estamos aquí, ¿o no?"

"No es difícil de suponer, pero desearía que ella no dijera las palabras que va a decir a continuación."

show misha perky_smile
with charachange

mi "¿Te gustaría saltarte la clase e ir a algún buen lugar con nosotras?"

hi "¿Cómo dices?"

show misha hips_smile
with charachange

mi "¿Te gustaría saltarte la clase para hacer algo divertido?"

"Estaba seguro de que me forzarían a ayudarles otra vez con algún trabajo forzado."

hi "¿En serio?"

show misha hips_grin
with charachange

"Misha sonríe y asiente con entusiasmo."

"Me gusta este nuevo acercamiento que están tomando, aunque estoy un tanto sorprendido de que hayan sugerido saltarse la clase, inclusive si solo tenemos la mitad del día dado que es sábado."

hi "¿No están ustedes dos preocupadas por faltar constantemente a clase?"

show shizu behind_smile
with charachange

shi "…"

show misha perky_smile
with charachange

mi "Bueno, ¡no parece ser un problema! Hicchan, esta escuela es prácticamente un punto muerto cada vez que este momento llega."

show misha hips_smile
with charachange

mi "Es sábado también~. ¿No quieres hacer algo divertido?"

"Estoy asombrado por lo poco que parecen preocuparse."

show shizu adjust_smug
with charachange

shi "…"

show misha perky_smile
with charachange

mi "No es que te estemos presionando para darnos tu compañía, ¡pero pensamos que podría gustarte pasar el rato!"

show shizu behind_blank
with charachange

shi "…"

show misha hips_smile
with charachange

mi "Así que… ¿te gustaría unírtenos? Vamos, ¡tendrás mucha más diversión que solo sentándote aquí con tu cabeza en tu escritorio~!"

"Supongo que no me estaré perdiendo nada importante; ni seré echado de menos."

hi "Está bien, entonces, no creo que me estaría perdiendo de mucho. ¿Qué tienen en mente?"

"Mis ojos se entrecierran con sospecha mientras un pensamiento cruza por mi mente."

hi "Esperen… esto no es solo un tipo de truco para ponerme a hacer más trabajo del consejo estudiantil, ¿cierto?"

show shizu basic_angry
with charachange

shi "…"

show misha perky_confused
with charachange

mi "No, ¡desde luego que no!"

show misha hips_frown
with charachange

mi "Y es una cosa muy fea simplemente asumir cosas de esa forma, Hicchan."

show shizu behind_frown
with charachange

shi "…"

show misha hips_smile
with charachange

mi "… Y además, ahora estás en el consejo estudiantil, ¿recuerdas?"

show misha hips_grin
with charachange

mi "Si quisiéramos que hicieras algo por nosotras, ¡no tendríamos que engañarte~!"

show misha hips_laugh
with charachange

mi "¡Jajaja!"

show misha hips_smile
with charachange

"Esta es una forma de coacción que es nueva para mí. Solo dos chicas lindas podrían llevarla a cabo."

stop music fadeout 3.0

"Me permito relajarme un poco. Tal vez estoy siendo demasiado paranoico; parece que ellas podrían realmente solo querer pasar el rato."

"Aun así…"

hi "¿Sin trucos?"

play music music_shizune fadein 4.0

show shizu basic_angry
with charachange

shi "…"

show misha hips_grin
with charachange

mi "¡Sin trucos! ¡Deja de ser tan paranoico!"

hi "Bueno, si tú lo dices."

"De repente, me doy cuenta de que aún estoy vistiendo pijama."

hi "Me pregunto si me dejarían vestirme primero."

show shizu adjust_smug
with charachange

shi "…"

show misha hips_smile
with charachange

mi "¿Eh? ¿Por qué, Hicchan? ¡Te ves bien!"

hi "Aun así preferiría vestir algo más."

play sound sfx_doorclose

scene bg school_dormhisao
with locationchange

"Cierro la puerta antes de que ella tenga una oportunidad para contestar y rápidamente me pongo mi uniforme."

play sound sfx_dooropen

scene bg school_dormhallway
show misha perky_smile at twoleft
show shizu basic_normal at tworight
with locationchange

"Al volver al pasillo, veo que Shizune y Misha están metidas en una animada discusión."

"Me pregunto si la gente discutiendo en señas alguna vez pica accidentalmente al otro en los ojos."

show shizu behind_frown_close
with characlose

"Mientras considero esto, Shizune me toca en el hombro impacientemente."

shi "…"

show misha hips_smile
with charachange

mi "Entonces, ¡estamos planeando bajar al pueblo! ¿Recuerdas esa tienda de té en la que estuvimos el miércoles?"

hi "¿Tienda de té?"

show shizu behind_frustrated_close
with characlose

shi "…"

show misha perky_confused
with charachange

mi "¿No recuerdas?"

hi "Oh, quieres decir ese café."

show misha hips_smile
with charachange

mi "¡Tienda de té! Se llama el Shanghái. China es el lugar de nacimiento del té, ¿sabes? ¡Vamos, Hicchan! ¡Inclusive yo invitaré hoy!"

show misha hips_grin
with charachange

mi "Ah… yo no, yo no, ¡quiero decir Shicchan! ¡Ajaja~!"

hi "No lo sé…"

show misha sign_smile
with charachange

mi "Es bueno, ¡es realmente relajante! Es como… mitad café, mitad restaurante, mitad sofisticado, mitad… biblioteca…"

"¿Qué?"

hi "Esas son muchas mitades."

"Pero Misha parece no notar eso."

show misha hips_smile
with charachange

mi "¡Así que~! Vamos, ¡no es muy común que tengamos tanto tiempo libre!"

show shizu adjust_smug_close
with charachange

shi "…"

show misha hips_grin
with charachange

mi "Sin embargo, si estás ocupado, ¡no tienes que venir! ¡No es como que tu presencia sea absoluta, absolutamente requerida!"

show misha cross_laugh
with charachange

mi "¡Jajajaja!"

show misha cross_grin
with charachange

"No he visto psicología inversa tan pobremente disfrazada en mi vida. Me siento algo cansado hoy, y mis maestros en mis clases podrían querer saber dónde estoy. Tal vez."

"Por otro lado, no he realmente recorrido el pueblo desde que llegué aquí, así que esta es una buena razón para ir allá."

"Además, estaría bien algo de comer. Si Shizune invita, aún mejor; estoy totalmente en bancarrota."

hi "Está bien, vamos. Yo las sigo."

show misha hips_smile
show shizu behind_smile_close
with charachange

mi "¡Genial~!"

stop music fadeout 2.0

scene bg suburb_shanghaiint
with shorttimeskip

"Llegamos a la tienda de té con una caminata de quince minutos. Parece que somos los únicos clientes por aquí."

play music music_another fadein 2.0

show shizu behind_blank at tworight
show misha perky_smile at twoleft
with charaenter

hi "¿Siempre está así de tranquilo en las mañanas?"

"Y con eso, quiero decir que si está siempre así de vacío."

show shizu basic_normal
with charachange

shi "…"

show misha perky_confused
with charachange

mi "No, esto es un poco raro. Oye, pero no es algo malo, ¿cierto?"

hi "Estás en lo cierto."

scene ev shizu_shanghai
with locationchange

"Tomamos asiento en una larga y cuadrada mesa de madera, y me doy cuenta de que no sé qué sirven en este lugar. Solo me fui con lo que Yuuko recomendó la última vez."

hi "Oigan, ¿hay un menú o algo?"

scene ev shizu_shanghai_normallaugh
with charachange

mi "¡Nop!"

"Esa fue una extraña cantidad de entusiasmo."

scene ev shizu_shanghai_smirklaugh
with charachange

shi "…"

scene ev shizu_shanghai_smirknormal
with charachange

mi "Así que, Hicchan, ¿has decidido qué es lo que ordenarás?"

scene bg suburb_shanghaiint at Fullpan(8.0)
with locationchange

"Miro alrededor de la tienda y no puedo ver nada que se asemeje a un menú."

"No entiendo, ¿qué pasa con este lugar? ¿Qué es lo que da?"

"¿Es esta alguna especie de tienda secreta? ¿Puedes normalmente entrar aquí solo con un saludo secreto? ¿Alguna especie de guiño y un asentimiento?"

"¿Necesitas que alguien interceda por ti? ¿Un juramento de sangre? Maldición, no hubo nada como esto la última vez."

scene ev shizu_shanghai
with locationchange

hi "No lo sé, la última vez ¿creo que solo tuve café? ¿Qué es lo que sirven aquí?"

scene ev shizu_shanghai_smirknormal
with charachange

shi "…"

scene ev shizu_shanghai_smirklaugh
with charachange

mi "¡Té!"

hi "Ah, bueno, eso es…"

hi "No tan solo té, ¿cierto? ¿No solo té? Hay otras cosas también, ¿cierto?"

scene ev shizu_shanghai_normallaugh
with charachange

shi "…"

scene ev shizu_shanghai
with locationchange

mi "¡Ciertamente~!"

hi "¿Ciertamente? ¿Como qué? No hay menús aquí. ¿Dónde están los menús?"

"Están jugando otra broma conmigo. No hay forma de salir de esto; todo lo que puedo hacer es prepararme para la inevitable e inminente burla."

"Casi quiero caminar fuera de la tienda, pero ya estoy acomodado aquí."

"Sería impropio salir ahora; las reglas tácitas de buena conducta social bloquean mi salida como una pared de fuego."

"Decido jugar a lo seguro. Ordenaré lo que ellas ordenen, si es lo suficiente y aceptablemente varonil."

hi "¿Por qué no ordenan ustedes dos antes? Las damas primero."

scene ev shizu_shanghai_smirknormal
with charachange

shi "…"

mi "Bien jugado, Hicchan, pero~ ¡ya hemos ordenado!"

hi "¿Cómo es eso posible? ¿Cuándo? ¿Cómo? ¿De quién?"

mi "Somos regulares, ¡venimos aquí tan seguido que ya no tenemos que hacer eso!"

scene ev shizu_shanghai
with charachange

shi "…"

mi "Bueno, creo que has tenido suficiente. Estamos sentadas sobre los menús, ¡por supuesto~!"

scene ev shizu_shanghai_normallaugh
with charachange

mi "¡Jajaja!"

"Veo hacia las otras mesas. No hay menús en ninguna de ellas. Eso quiere decir que deben mantenerlos en una gran pila cerca de la puerta o algo así. Vaya cosa para sentarse, y qué velocidad para agarrarlos tan rápido."

hi "Bueno, como sea. ¿Puedo tener uno, entonces?"

scene ev shizu_shanghai_smirklaugh
with charachange

shi "…"

scene ev shizu_shanghai_smirknormal
with charachange

mi "Puedes tomar uno si quieres, pero no eres el tipo de persona que haría algo ¿la-sci-vo?, ¿no es eso cierto?"

"Les digo que solo me gustaría un poco de café y pongo mi cabeza en la fría tabla de la mesa."

scene ev shizu_shanghai_borednormal
with charachange

shi "…"

scene ev shizu_shanghai_boredlaugh
with charachange

mi "¿Café? Este es un establecimiento de muy alta clase, ¿y tú vas a ordenar café?"

"Puedo notar que están metiéndose conmigo otra vez."

hi "En ese caso, tendré lo que sea que ustedes vayan a tener."

scene ev shizu_shanghai_smirklaugh
with charachange

shi "…"

scene ev shizu_shanghai_smirknormal
with charachange

mi "Hicchan, Shicchan va a beber un té especial que solo crece en áreas remotas de la India."

mi "El té es aún hecho a mano por una tribu de fabricantes de té quienes han pasado los métodos a través de su familia por generaciones."

mi "Ellos deben vadear a través de aguas infestadas de lagartos para obtener las hojas una vez al año. En cada viaje, algunos no logran volver vivos."

"No puedo beber eso, me sentiría demasiado culpable."

hi "Entonces tendré lo que tú vas a tener."

scene ev shizu_shanghai_smirklaugh
with charachange

mi "Yo no sé lo que voy a beber."

"¿Cómo?"

hi "Bien, entonces quiero el té por el que ha muerto gente."

hi "No, olvídenlo. Tendré café."

hi "Si este es un establecimiento de muy alta clase, entonces deben tener un café de muy alta clase, ¿cierto?… Nadie murió por él, ¿cierto?"

scene ev shizu_shanghai
with charachange

"La respuesta perfecta, no hay forma en que puedan ponerse contra ella. Shizune se encoge de hombros, como para decir “bien jugado”."

"Ellas aún no han contestado mi segunda pregunta."

scene bg suburb_shanghaiint
with locationchange

show yuukoshang neutral_down at center
with charaenter

"Misha llama por Yuuko, quien trae nuestras bebidas y un sencillo e increíblemente diminuto pastelillo amarillo con un pequeño tenedor negro de plástico clavado en él para cada uno de nosotros."

hide yuukoshang
with charaexit

"Me como mi pastelillo de una mordida, asombrado de cómo es probablemente la cosa menos llenadora que he comido jamás."

show shizu behind_blank at Slide(0.2,0.5,0.3,0.5,1.0)
show misha perky_smile_close at Slide(0.8,0.5,0.7,0.5,1.0)
with Dissolve(1.0)

stop music fadeout 3.0

mi "Hicchan, ¿no tienes planes para mañana?"

"Misha toma un trago de su té, algo que suena sospechosamente de alta clase incluso a pesar de que luce como un té ordinario."

"Ella bebe con bastante indiferencia considerando lo caliente que está. El opuesto exacto de Shizune o Lilly."

"¿Planes? Eso suena amenazador."

play music music_running fadein 8.0

hi "¿Planes? Sí."

hi "Sí, estoy increíblemente ocupado mañana. De hecho, tengo tanto que hacer que no tendré nada de tiempo libre en absoluto."

hi "Eso es… absolutamente nada de nada. Y todo lo que tengo que hacer es extremadamente importante. Muy, muy importante."

show misha hips_grin_close at tworight
with charachange

"Misha ríe, claramente no se lo está creyendo, y después le indica todo a Shizune, quien asiente con la cabeza lenta y deliberadamente mientras luce muy seria."

show shizu basic_normal_close at twoleft
with characlose

"De repente, ella se inclina al frente, mirando analíticamente a mi rostro como un detector de mentiras humano, esperando por la menor revelación para delatarme."

"Después de al menos un minuto de esto, ella regresa atrás a su asiento y toma un sorbo de té."

show shizu behind_blank
with charadistant

shi "…"

show misha perky_smile_close
with charachange

mi "Está bien, Hicchan, si estás tan ocupado. Nosotras no tenemos nada que hacer mañana, ¡así que pensamos que tal vez querrías pasar el rato con nosotras en el festival!"

show misha sign_smile_close
with charachange

mi "Eres nuevo aquí, de cualquier modo, ¿cierto? ¿Cierto? Así que~ pensamos que te mostraríamos los alrededores y tendríamos un poco de diversión juntos, pero si estás tan ocupado, ¡nosotras lo entendemos!"

show shizu adjust_happy
with charachange

shi "…"

mi "Oh bueno, ¡oh bueno!"

show misha cross_grin_close
show shizu basic_normal2
with charachange

"Ambas se encogen de hombros en perfecta sincronía, como si lo hubieran ensayado."

show misha cross_laugh_close
with charachange

mi "¡Ajajajajaja~!"

show misha cross_grin_close
with charachange

mi "Hicchan, eres muy paranoico."

show shizu adjust_smug
with charachange

shi "…"

show misha cross_smile_close
with charachange

mi "… Y de cualquier forma nunca me vencerás, ¿así que por qué molestarse en entusiasmarse tanto sobre ello?"

show misha cross_laugh_close
with charachange

mi "¡Jaja! ¡Guau, Shicchan~!"

hi "¿Vencerte? ¿De qué estás hablando?"

"¿Está hablando de la coacción? Nunca me di cuenta de que esto era solo un juego para ella. Pensé que era el único que veía esto como una competencia."

show shizu basic_happy
with charachange

shi "…"

show misha hips_grin_close
with charachange

mi "¡Ya lo sabes~! ¿… Eh? ¿Lo sabes, Hicchan? Porque yo no."

show shizu adjust_smug
with charachange

shi "…"

show misha hips_smile_close
with charachange

mi "¡No puedes superarme! —Ah, bueno, Hicchan, no yo…"

show shizu basic_sparkle
with charachange

shi "…"

show misha perky_confused_close
with charachange

mi "¿Qué? De qué estás hablando, Shicchan…"

"Puedo ver a Shizune sonriendo con astucia, retándome a entrar a esta batalla de voluntad e ingenio con ella."

"Cuando se le orilla al borde de la desesperación, un hombre no tiene otra opción más que hundirse, o aferrarse a los fugaces mechones de esperanza, pelear con todo su poder contra la inevitabilidad de su destino y luchar contra lo imposible."

"Para que, incluso si falla, al menos lo haga sabiendo que se batió noblemente…"

"… O algo así."

hi "Bueno, ya lo veremos. No me subestimes."

show shizu behind_blank
with charachange

shi "…"

show misha perky_smile_close
with charachange

mi "¿No tienes que seguir hasta el final para cumplir con eso, Hicchan?"

hi "Ah, bueno, podría estar de suerte. No pases por alto esa posibilidad."

show shizu adjust_smug
with charachange

shi "…"

show misha cross_grin_close
with charachange

mi "No lo estarás~."

hi "¡Lo estaré! Espera—"

show shizu basic_happy
with charachange

shi "…"

show misha cross_smile_close
with charachange

mi "¡Vamos a apostar entonces!"

hi "No me interesa competir."

"Eso es una completa mentira."

hi "Espera, ¿a qué te refieres exactamente?"

show misha cross_laugh_close
with charachange

mi "Está bien si no lo sabes, ¡yo tampoco sé! ¡Guajajaja!"

show shizu basic_normal2
with charachange

shi "…"

show misha perky_smile_close
with charachange

mi "¡Está decidido entonces! Está bien, ¡está bien!"

hi "¿Qué? ¿No escucharon lo que acabo de decir?"

show shizu adjust_happy
with charachange

shi "…"

show misha sign_smile_close
with charachange


mi "¡Ahora todo lo que falta es lo que se apostará! Lo que el ganador gana, o, aún más interesante, ¡lo que el perdedor pierde!"

hi "¡Oigan!"

"Es un juego muy peligroso el que estoy jugando. Shizune en sí misma es una chica muy peligrosa, si solo puede pensar en términos de ganar o perder."


"Si ve cada momento en que hablamos como una especie de batalla de voluntades, no creo que pueda soportarlo."

"Ese tipo de cosas vuelve a la gente loca. Es demasiado maquiavélica; antes de esto asumí que era solo un tanto estoica."

"Pero no importa, estoy interesado. En retrospectiva, me doy cuenta de que simplemente la reté a lo que es esencialmente un duelo sin reglas que no terminará hasta que uno de nosotros… ¿qué?"

"Supongo que eso es todo. Eso es tan vago. ¿Cuáles son las condiciones de victoria o derrota? ¿La primera persona que se sienta estúpida pierde?"

hi "No lo sé, nunca he tenido que pensar en nada como esto antes."

show misha hips_smile_close
with charachange

mi "¿Nunca?"

hi "Nunca."

show misha perky_confused_close
with charachange

mi "¿Así que nunca has apostado, Hicchan?"

hi "Estoy sorprendido de que ustedes dos lo hayan hecho."

show shizu behind_blank
with charachange

shi "…"

show misha hips_grin_close
with charachange

mi "Oh, vamos… ¡Es solo por diversión, de cualquier modo! ¡Entre amigos~!"

show misha sign_smile_close
with charachange

mi "¡Es sobre causar humillación, sufrimiento, y desesperación absoluta! ¿No es ese el punto?"

"Shizune coloca un dedo en su sien pensativamente."

show shizu adjust_happy
with charachange

shi "¡…!"

show misha hips_smile_close
with charachange

mi "Hmm… Ah, qué tal esto, Hicchan: Si tú pierdes, tendrás que ir un día a la escuela sin pantalones puestos."

hi "¿Están locas?"

"Aunque en comparación con lo que temía que diría, eso es muy suave."

hi "¿No podemos simplemente apostar dinero, como gente normal?"

show shizu basic_sparkle
with charachange

shi "…"

show misha hips_grin_close
with charachange

mi "¡No es como si tú pudieras alcanzar mi apuesta si lo hiciéramos~! Ahora, ¡es tu turno!… ¡Pero nada pervertido! ¿Entendido?"

show misha hips_laugh_close
with charachange

mi "¡Jajaja!"

hi "Creo que necesito más tiempo."

"Esto va a tenerme constantemente al límite por semanas."

show misha hips_grin_close
with charachange

mi "¡Bien~! Vamos, ustedes dos se deben apresurar, ¡sus bebidas se están enfriando!"

show shizu basic_happy
with charachange

"Rápidamente termino el resto de mi café mientras Shizune hace lo mismo, observándome con una feroz mirada de competencia en sus ojos."

"Parece un desperdicio que ella esté tragando algo por lo que alguien podría haber muerto para su disfrute."

show misha sign_smile_close
with charachange

mi "Hicchan, ¿estás seguro de que no quieres pasar el rato mañana? Mucha gente está buscando hacerlo; no querrás perdértelo."

"Le balbuceo algo ininteligible."

show misha perky_confused_close
with charachange


mi "No te entiendo realmen…"

"Es tiempo de pensar. La bebida de Shizune es más pequeña, pero yo puedo consumir la mía más rápido."

"Si Shizune termina su bebida primero, ella tal vez se escape de pagar, dejándome para que yo pague la cuenta, incluso si ella dijo que las bebidas irían por su cuenta."

"Como no tengo dinero conmigo, sería humillado, y por tanto esto podría ser considerado una derrota."

"Si termino primero, las reglas de caballerosidad me harían ver como un idiota, dado que tendría que escapar de esta casa de té, dejándola pagar por todo. Eso podría ser considerado también una derrota. Ella usaría eso."

"En el caso de un empate, ella podría intentar correr a la puerta, y probablemente yo haría lo mismo. Esto podría llevar a una colisión en la puerta, lo cual sería humillante, pero no demasiado… y Misha se quedaría a pagar la cuenta."

"Esto es realmente infantil. Estoy un poco decepcionado de Shizune, y de mí."

show misha perky_smile_close
with charachange

mi "Bueno, Hicchan, sería muy bueno si pudiéramos todos celebrar lo bien que hemos armado todo para el festival dando una mirada a nuestra obra…"

"Misha parece inconsciente del hecho de que una épica batalla de voluntades está desarrollándose frente a ella. Asiento lentamente con la cabeza y termino lo último de mi café."

hi "Bueno, he terminado de disfrutar mi bebida. Supongo que es tiempo de que me vaya. Y me iré ahora. Tranquilamente."

show shizu adjust_happy
with charachange

shi "…"

show misha perky_confused_close
with charachange

mi "¿Tú también, Shicchan?"

mi "¿Por qué están los dos actuando tan raro?"

scene bg suburb_shanghaiext
with locationchange

"Rápidamente salgo por la puerta y Shizune me sigue. Misha va a tener que pagar la cuenta."

scene bg suburb_roadcenter
with locationchange

"Lo siento, Misha."

show shizu behind_smile at center
with charaenter

"Alcanzándome, Shizune rápidamente empuja sus anteojos hacia arriba y presiona una nota contra mi mano."

window hide

$ written_note("Si tú pierdes, tendrás que pasar el rato con nosotras mañana.")

window show

hi "¿Así que crees que puedes ganar hoy? Eso es un tanto engreído, Shizune."

"Olvido por un segundo que ella no puede oírme. Asiento con la cabeza."

"Justo ahora, luce mucho más linda de lo que usualmente es, sonriendo tiernamente con un atisbo de confianza mostrándose a través de esta."

"Shizune luce enérgica y despreocupada, aunque podría solo ser la cafeína."

show shizu adjust_happy
with charachange

"Ella guiña un ojo, y extiende su mano para un apretón de manos. Me pregunto si hay un timbre ahí y planea darme un toque, pero eso no luce como algo que ella haría, así que acepto."

"Con un apretón, ella presiona otra nota en mi mano. Momentáneamente pienso que es un timbre y me pregunto si el toque podría matarme."

hide shizu
with charaexit

"Shizune sonríe y luego escapa."

window hide

$ written_note("Probablemente no sabes cómo volver a la escuela desde aquí.\n\nHabrá trabajo esperándote cuando lo hagas. Te veo entonces~")

window show

"Aplasto la nota en mi mano dramáticamente, pero nadie está ahí para verlo, y eso me pone triste."

"Me pregunto si es demasiado tarde para volver a la tienda y preguntar a Misha por indicaciones."

"Sin embargo, le di muchas dificultades por no saber el camino hacia aquí, así que no puedo permitirle que se aproveche de mí por no saber el camino de regreso."

"Y si le pregunto, Shizune podría verlo como una victoria. No, no es necesario."

stop music fadeout 3.0

"La escuela está en la cima de una maldita colina, ¿qué tan difícil de hallar podría ser?"

"Puedo ser ligeramente malo para ubicarme, pero estoy seguro de que incluso yo puedo hacer esto."

scene bg school_courtyard
with shorttimeskip

play music music_happiness

"Cerca de una hora y media después, recorro el largo camino pavimentado del portón al edificio principal."

scene bg school_lobby
show shizu behind_blank at tworight
show misha hips_grin at twoleft
with locationchange

mi "¡Jajaa! Justo la persona que estábamos esperando. Así que lograste llegar aquí eventualmente, Hicchan, ¡bien! ¡Ahora es tiempo para trabajar trabajar~!"

"Misha y Shizune habían preparado una emboscada para mí en el vestíbulo principal de la planta baja y caminé directo a ella. Debí haber rodeado la escuela como lo había planeado originalmente, pero pensé que estaba sobreactuando y siendo tonto."

"Misha está ondeando una gruesa pila de papeles impresos en mi dirección, burlándose de mí."

show misha perky_smile
with charachange

mi "¡Como que necesitamos tu ayuda~!"

hi "¿Como que?"

show misha hips_grin
with charachange

mi "¡Necesitamos tu ayuda~!"

show shizu cross_angry
with charachange

shi "…"

show misha sign_smile
with charachange

mi "¡Nos ayudarás!"

"Misha habla con su usual manera juguetona y despreocupada, pero aun así puedo oír la intimidante y dura severidad de Shizune tras ella."

hi "Eso suena como una orden."

mi "¿En serio? ¿Lo es?"

show shizu behind_frown
with charachange

shi "…"

show misha perky_confused
with charachange

mi "¿Eh? ¿Lo es?"

show misha hips_laugh
with charachange

mi "Ah, lo siento, Hicchan, ¡supongo que lo es! ¡Jajajaja!"

"No suena muy sentida a pesar de todo."

show misha hips_grin
with charachange

mi "Pensé que teníamos casi todo hecho hasta ahora, pero resulta que tenemos todas estas señales para fijar a los paneles."

show shizu adjust_angry
with charachange

shi "…"

show misha sign_smile
with charachange

mi "¡Más manos hacen ligero el trabajo!"

show misha hips_laugh
with charachange

mi "¡Y todos ganan! ¡Jajajajaja!"

show shizu basic_angry
with charachange

shi "…"

show misha hips_smile
with charachange

mi "Esto es tu deber, después de todo, como miembro del consejo estudiantil. Del cual tú eres parte."

mi "Como un miembro."

mi "Del consejo estudiantil."

show misha hips_laugh
with charachange

mi "¡Ajajaja~!"

show shizu behind_blank
with charachange

shi "…"

show misha perky_smile
with charachange

mi "Es una tarea simple, así que quitarla del camino de una vez sería bueno. No es tanto trabajo. ¡Una pequeñez, en verdad!"

show shizu basic_normal2
with charachange

shi "…"

mi "¡Y realmente apreciamos tu ayuda!"

mi "¡Realmente, realmente la apreciamos!"

show misha hips_grin
with charachange

mi "Además, ¡es tiempo de pagarnos por haberte tratado tan bien!"


hi "¡Así que la tienda de té fue una trampa después de todo! ¡Timadoras sinvergüenzas!"

show shizu behind_blank
with charachange

shi "…"

show misha cross_smile
with charachange

mi "No digas eso, fue un evento no relacionado. ¡Queríamos celebrar tu unión al consejo!"

"Pero ¿por qué mencionó eso, entonces?"

hi "Pero—{w=0.3}{nw}"

show shizu cross_rage
with charachange

shi "¡…!"

show misha hips_grin
with characlose

mi "¡Sin peros! ¡Vas a venir con nosotras!"

show misha hips_grin at offscreenleft
show shizu cross_rage at offscreenright
with ease

show misha cross_smile_close at closeleft
show shizu cross_angry_close at closeright
with ease

"No logro siquiera terminar mi oración dado que me agarran por los brazos y tratan de jalarme hacia su oficina."

show misha cross_laugh_close
with charachange

"Misha ríe graciosamente mientras Shizune intercambia maliciosas miradas a mis espaldas."

show shizu basic_angry_close
with charachange

shi "¡…!"

mi "¡Ah, no creo que tengas elección en esto, Hicchan! ¡Jajajaja!"

show misha hips_grin at twoleft
show shizu basic_angry at tworight
with charadistant

mi "Hay dos de nosotras, ¡así que ni siquiera intentes escapar! ¡No nos tomes a la ligera!"

show shizu behind_frown
with charachange

shi "¡…!"

mi "Hicchan, ¡es tu deber ayudarnos, de cualquier modo! ¡Como miembro del consejo estudiantil!"

hi "Está bien, ¡está bien! ¿Cómo pude olvidarlo?"

hi "Pero, en serio, ¿no hay otra gente que pueda ayudarles?"

show misha perky_confused
with charachange

mi "¿Como quién, Hicchan?"

mi "No te molestó ayudarnos ayer…"

hi "¡Ayer no es hoy!"

hi "¡Y cualquiera que no sea yo!"

hi "¿Por qué no tienen a nadie más en el consejo?"

show shizu cross_wut
with charachange

shi "¡…!"

show misha cross_laugh
with charachange

mi "¡Eso es lo que nos gustaría saber!… Aja… ¡Ajajajajaja!"

"La carcajada de Misha explota a través del pasillo. Ella no nota para nada la mueca en mi cara. Es cierto, son solo ellas dos después de todo, ¿no?"

hi "Oh, está bien. Les ayudaré."

show misha hips_grin
with charachange

"Misha pasa su lengua sobre sus dientes, luciendo bastante complacida."

mi "¡Ese es mi Hicchan! ¡Sabía que podíamos confiar en ti~!"

show shizu behind_smile
with charachange

shi "¡…!"

mi "Tan predecible~."

stop music fadeout 2.0

scene bg school_council
with locationskip

"Cuando llegamos a la habitación del consejo estudiantil, mi quijada se desploma. El número de señales, paneles, y postes de señalización es una locura."

"Están apilados por todo el lugar como materiales de construcción en una zona de obras, algo que permití a Shizune y Misha saber justo en el acto."

hi "¡Hay tantos postes de señalización aquí que probablemente podrías construir una segunda pared alrededor de la escuela con ellos!"

play music music_ease fadein 4.0

show shizu behind_blank at tworight
show misha perky_smile at twoleft
with charaenter

mi "¡Jajaja~! ¿En verdad? Bueno, hay muchísimos de ellos, así que tal vez…"

show shizu basic_angry
with charachange

shi "¡…!"

show misha perky_confused
with charachange

mi "¿Eh? ¿No?"

mi "¿Cómo sabes eso, Shicchan?"

show shizu behind_frown
with charachange

shi "¡…!"

mi "¿En serio?"

hi "No me digas, ¡¿en verdad ella lo consideró?!"

show misha hips_grin
show shizu adjust_smug
with charachange

"Shizune duda, luego presiona sus anteojos hacia arriba un poco mientras Misha deja salir una risa que suena a mucha incomodidad."

"Así que lo ha considerado."

show shizu basic_normal2
with charachange

shi "¡…!"

mi "¡Ajaja! Eso es… ¡irrelevante, Hicchan! ¿Puedes comenzar con eso de hacer las señales, por favor?"

hi "Está bien, está bien."

hi "Sin embargo, me siento un tanto engañado. ¿Pensé que ustedes dijeron que no sería tanto trabajo?"

show shizu behind_blank
with charachange

shi "¡…!"

show misha hips_smile
with charachange

mi "Ah, bueno, Shicchan quiso decir que no sería tanto trabajo para nosotras."

show shizu basic_normal
with charachange

shi "¡…!"

mi "Alguien tiene que supervisarte mientras haces esto, ya sabes, para asegurar que lo estás haciendo bien. Y esas personas seremos nosotras."

hi "¿Entonces qué es lo que ustedes dos harán?"

show misha cross_laugh
show shizu basic_happy
with charachange

mi "¡Mirarte! ¡Jajajaja~!"

show shizu adjust_happy
with charachange

shi "¡…!"

show misha perky_smile
with charachange

mi "No, eso fue solo una broma, Hicchan. Ayudaremos también, desde luego. El consejo estudiantil en teoría realmente debería tener mucha más gente."

show misha perky_sad
with charachange

mi "Este es solo un mal año. Menos gente de la usual, incluso a pesar de que no habíamos tenido mucha el año anterior."




mi "Y entonces simplemente tenemos mucho más trabajo que antes, también."

show shizu behind_smile
with charachange

shi "¡…!"

show misha perky_smile
with charachange

mi "Además, a Shicchan le gusta trabajar contigo. ¡Y a mí también!"

mi "Hemos completado mucho más de lo que normalmente podemos, ¿sabes?"

stop music fadeout 7.0

"Puedo aceptar eso. Últimamente, ellas han estado luciendo fatigadas cada vez que las veo."

"El trabajo del consejo estudiantil es aparentemente algo de “24 horas al día”, y por lo que he visto aquí, solo están ellas dos. Bueno, supongo que conmigo son tres."

"Deben trabajar casi sin parar. Me pregunto cuánto tiempo pasan trabajando en esta habitación, cuando no las veo."

"Incluso he sorprendido a Misha tomando siestas algunas veces sin Shizune a su lado. Por sí misma, Shizune debe estar trabajando 60 horas semanales haciendo sus deberes del consejo estudiantil, sumadas a sus clases regulares."

scene bg school_council_ss
with shorttimeskip

play music music_tranquil fadein 3.0

"Dos horas pasan, y estiro la mano por una tachuela solo para encontrar que la caja está vacía. Shizune la toma antes de que yo pueda decir nada."

show shizu adjust_happy_ss at tworight
show misha perky_smile_ss at twoleft
with charaenter

"Ella sonríe, lanzándola expertamente en un bote de basura junto con otra caja vacía de tachuelas."

show shizu behind_smile_ss
with charachange

shi "¡…!"

show misha hips_grin_ss
with charachange

mi "¿Entonces se te acabaron también, Hicchan? No te preocupes, Shicchan dice que irá por más."

show misha hips_laugh_ss
with charachange

mi "¡Jajajaja!"

show misha hips_grin_ss
with charachange


mi "También nos acabamos una caja, pero yo y Shizune decidimos esperar hasta que tú necesitaras una nueva caja también."

"Algo sobre eso me parece extraño."

hi "Esperen, ¿los dos nos quedamos sin tachuelas justo ahora? Guau, qué extraña coincidencia, ¿eh?"

show misha perky_smile_ss
with charachange

mi "Ah, bueno, de hecho, Hicchan, nos las terminamos hace veinte minutos, y solo había una caja más de tachuelas, las que te dimos a ti."

mi "Y estabas avanzando con ellas muy rápido, ¡así que~! ¡pensamos que deberíamos esperar hasta que ambos no tuviéramos más tachuelas antes de ir por más!"

show misha sign_smile_ss
with charachange

mi "Entonces, Shicchan podría ir por más cajas de tachuelas para todos nosotros al mismo tiempo. Ya sabes, ¡por eficiencia~!"

show shizu basic_normal2_ss
with charachange

"Shizune asiente con la cabeza, preparándose para salir por la puerta."

hi "Esperen un segundo, ¿entonces qué hicieron ustedes dos en los últimos 20 minutos?"

show shizu adjust_happy_ss
with charachange

shi "¡…!"

show misha hips_grin_ss
with charachange

mi "¡Ajaja~! ¡Nada, por supuesto! ¿Qué podíamos hacer? ¡No teníamos tachuelas, Hicchan!"

show shizu behind_smile_ss
show misha cross_grin_ss
with charachange

"Shizune y Misha intercambian miradas de complicidad antes de darme un perfectamente sincronizado e increíblemente exagerado encogimiento de hombros simultáneo."

hi "Ya veo. Así que decidieron tomarse un descanso. Ingenioso."

show shizu adjust_smug_ss
with charachange

shi "¡…!"

show misha hips_grin_ss
with charachange

mi "Oh, sabemos que fue ingenioso."

hi "¿De quién fue la idea?"

show misha hips_smile_ss
show shizu adjust_happy_ss
with charachange

mi "De nosotras dos, por supuesto, ¡por supuesto!"

show misha cross_laugh_ss
with charachange

mi "¡Ajajaja~! Bueno, Hicchan, todo fue idea de Shicchan."

show shizu behind_smile_ss
with charachange

hide shizu
with charaexit

stop music fadeout 3.0

"Volteo inmediatamente a Shizune, quien me da un brusco saludo desde lejos y una sonrisa sorpresivamente alegre antes de desvanecerse rápidamente hacia fuera de la puerta."

show misha cross_grin_ss at twoleft
with charachange

show misha cross_grin_ss at center
show bg school_council_ss at bgright
with charamove

"Bueno, ¿¡entonces por qué no dijeron simplemente que querían tomar un descanso!?"

"Solía pensar que Shizune y Misha eran polos opuestos. Misha siempre luce tan enérgica y juguetona, como cualquier otra chica. Shizune, por otro lado, siempre lucía distante. Agresivamente manipuladora y vagamente atemorizante, pero distante."

"Hubo momentos en que pensé que ella no tenía sentido del humor. Así tan linda como era, casi nunca la había visto sonreír. Sin mencionar todas las otras cosas."

"La mirada analítica, la expresión permanentemente estoica, e incluso su caligrafía; tan mecánicamente precisa que todo lo que escribe parece a máquina."

"Pero Shizune y Misha realmente no son tan diferentes como pensé."

hi "Estoy un poco sorprendido."

play music music_shizune fadein 5.0

show misha perky_confused_ss
with charachange

mi "¿Por qué?"

hi "Shizune. No sabía que a ella le gustaba bromear de esa manera."

"Lo que quiero decir es, no sabía que ella podía actuar tan femenina. Fue de hecho muy lindo."

show misha perky_smile_ss
with charachange

mi "Te sorprendería, Hicchan."

hi "Bueno, tampoco sabía que tú y ella fueran tan cercanas, la primera vez que las vi."

"Siempre he tenido curiosidad por cómo es que estas dos se conocieron."

hi "¿Ustedes dos se conocen desde hace mucho o algo así?"

hi "¿Amigas desde niñas?"

hi "¿Vecinas de al lado?"

show misha perky_sad_ss
with charachange

mi "Jaja… Lo siento, Hicchan, no es nada como eso, aunque sería mucho más lindo de esa forma."

show misha perky_smile_ss
with charachange

mi "Cuando vine a esta escuela, ellos solo me pusieron al lado de Shicchan, y ella lucía como una persona muy seria."

show misha sign_smile_ss
with charachange

mi "Y pensé, “¡Voy a estar pasando el resto del año al lado de esta persona, tal vez!”."

mi "“¡Así que sería bueno si pudiéramos ser amigas! Pero~, me pregunto si le gustaré”."

show misha hips_grin_ss
with charachange

mi "Y aprendí que ella era sorda. ¿Sabes, Hicchan?, ¡la primera vez simplemente pensé que ella estaba ignorándome~!"

show misha hips_smile_ss
with charachange

mi "Pero, afortunadamente, sabía un poco de lenguaje de señas, y nos hicimos amigas."

"Quiero saber dónde es que Misha aprendió cómo hacer señas, pero supongo que eso es algo para otra ocasión."

show misha perky_smile_ss
with charachange

mi "Ahora, supongo que siempre estamos juntas. Es bueno, siempre he querido a alguien que me escuche, ¡y pienso que a Shicchan le gusta tener a alguien con quien hablar! Así que, todos ganan."

hi "Je. Eso es bueno."

show misha hips_grin_ss
with charachange

mi "¿Eso es todo? Luces decepcionado, Hicchan, ¿qué es lo que esperabas?"

show misha hips_laugh_ss
with charachange

mi "¡Ajajajajaja!"

show misha hips_grin_ss
with charachange

mi "¿Sabes, Hicchan? No creo que Shicchan y yo te hayamos agradecido apropiadamente."

hi "¿Por qué?"

show misha perky_smile_ss
with charachange

mi "Unirte al consejo estudiantil. ¡Has sido una verdadera ayuda para nosotras, Hicchan! ¡Creo que tendremos mucho más tiempo para dormir ahora~!"

hi "Bueno, me alegra haber ayudado, si eso ayuda a una joven mujer a dormir por la noche."

show misha hips_smile_ss
with charachange

mi "Eso es una forma interesante de decirlo, Hicchan."

mi "Shicchan realmente aprecia el que nos estés ayudando también."

show misha hips_smile_ss at twoleft
show bg school_council_ss at center
with charamove

show shizu behind_frustrated_ss at tworight
with charaenter

"En ese momento, Shizune vuelve a la habitación, luciendo ligeramente molesta y sorbiendo desenvueltamente de una caja de jugo."

show shizu adjust_happy_ss
with charachange

shi "…"

play sound sfx_dropstuff

"Ella tira dos cajas de tachuelas en el piso con una sonrisa forzada."

show shizu basic_normal2_ss
with charachange

shi "¡…!"

show misha sign_smile_ss
with charachange

mi "Ah, Shicchan."

play sound sfx_crunchydeath

show shizu behind_frown_ss
show misha sign_confused_ss
with charachange

"Misha abre su boca para hablar, pero entonces rápidamente la cierra pues Shizune repentinamente aplasta su caja de jugo con un crujir parecido al sonido de huesos rompiéndose."

show shizu basic_angry_ss
with charachange

shi "¡…!"

show shizu adjust_angry_ss
with charachange

shi "…"

show shizu behind_frown_ss
with charachange

shi "¡…!"

"Puedo decir que cada severo y tembloroso gesto de manos es más como un insulto."

hi "¿Qué está diciendo?"

show misha perky_confused_ss
with charachange

mi "Fue algo muy difícil de captar…"

show shizu basic_angry_ss
with charachange

shi "¡…!"

show misha sign_confused_ss
with charachange

mi "Creo que eso es un eufemismo, Shicchan…"

"Shizune se calma un poco, enderezando sus anteojos y cepillando ligeramente su flequillo hacia atrás con un dedo."

show shizu adjust_happy_ss
with charachange

shi "…"

show misha perky_smile_ss
with charachange

mi "¿No fue realmente un gran problema en retrospectiva? ¡Eso es muy prevenido de tu parte!"

show misha hips_smile_ss
with charachange

mi "Está bien entonces, ¡supongo que ambos debemos volver al trabajo, Hicchan!"

stop music fadeout 4.0

hi "Seguro, por qué no."

scene bg school_council_ni
with shorttimeskip

"Para cuando hemos terminado con las señales, ya está oscureciendo afuera."

"No había esperado que algo como esto tomara tanto tiempo. Pero una vez más, si fuera tan fácil, dudo que Shizune y Misha hubieran pedido mi ayuda."

play music music_dreamy fadein 2.0

show shizu basic_normal at tworight
show misha perky_smile at twoleft
with charaenter

"Shizune cae en una silla cercana, tronando sus nudillos sistemáticamente y dejando salir un mudo bostezo."

show shizu behind_blank
with charachange

shi "…"

show misha sign_smile
with charachange

mi "¡Es todo por hoy, supongo! Eso es algo bueno, Shicchan, también estoy muy cansada."

hi "Eso tomó más de lo esperado."

show shizu behind_frustrated
with charachange

shi "…"

show misha hips_grin
with charachange

mi "¿Estás de acuerdo? Jajaja, ¡nosotras tampoco esperábamos que tomara tanto tiempo! ¡No salió conforme al plan!"

show misha perky_sad
with charachange

mi "Oooh, tengo tanta hambre. Me acabo de dar cuenta de que no he comido en todo el día."

"Ahora que lo pienso, no he comido nada desde que me levanté esta mañana, pero justo ahora estoy casi demasiado cansado como para pensar en comida."

hi "Creo que ya dejaron de servir la cena."

show misha perky_confused
with charachange

mi "¡Esto no puede estar pasando! Hicchan, ¿puedes pensar en alguna forma en que podríamos… obtener comida?"

hi "¿Obtener comida?"

"No me gusta el tono de su voz."

show shizu adjust_happy
with charachange

shi "…"

show misha hips_grin
with charachange

mi "¿Por qué no ordenarla? Oh, es cierto, creo que yo podría hacerlo."

hi "¿Ordenar? ¿De dónde?"

mi "¡Del pueblo, por supuesto!"

hi "No sabía que hacían envíos a la escuela. Bueno, ¿qué es lo que pedirán?"

show misha hips_smile
with charachange

mi "¡Tal vez un poco de comida china!"

hi "Dado que ustedes lo van a hacer, ¿puedo aprovechar y pedir también? Yo también tengo mucha hambre."

show misha hips_laugh
with charachange

mi "¡Ajajaja~! Hicchan, ¡debiste haberlo dicho desde un inicio!"

show shizu basic_normal2
with charachange

shi "…"

show misha hips_grin
with charachange

mi "¿Qué dices? ¿Tú invitas? ¡Eso es genial! ¡Es genial!"

show shizu behind_blank
with charachange

shi "…"

show misha cross_laugh
with charachange

mi "Guajaja, eso es verdad, ¡si no fuera por ti, no estaríamos tan tarde aquí, Shicchan!"

show misha cross_grin
with charachange

"Misha rápidamente agarra un menú de un cajón tras ella y empieza a marcar el número lenta y cuidadosamente, como si estuviera acostumbrada a equivocarse."

mi "¿Qué quieres, Hicchan?"

hi "Bueno, creo que solo pediré unas croquetas."

show shizu behind_smile
with charachange

"Levanto mi mano en un gesto de agradecimiento a Shizune, quien responde con una muy ligera sonrisa de medio segundo."

show misha cross_laugh
with charachange

mi "¡¡Ajajajajaja~!! Hicchan, Shicchan pagará todo esta noche, todo está de su parte, ¡así que puedes darte el lujo de derrochar un poco!"

hi "Un arroz frito con camarón también, entonces."

show misha cross_grin
with charachange

mi "Está bien, ¡está bien! ¿y tú, Shicchan?"

show shizu basic_normal2
with charachange

shi "…"

show misha hips_smile
with charachange

mi "¿Un omelette chino? Muy bien, entonces."

hi "Oye, Misha, ¿eso realmente significa “omelette”? ¿Puedo ver eso otra vez?"

show misha hips_grin
with charachange

mi "¡Seguro! ¡Jaja! Así, así…"

show misha sign_smile
with charachange

show misha perky_smile
with charachange

show misha hips_grin
with charachange

mi "Y esto es lo que ordenaste: ¡Croquetas!"

show misha perky_smile
with charachange

show misha sign_smile
with charachange

show misha hips_smile
with charachange

mi "¡Arroz frito con camarón!"

show misha hips_grin
with charachange

mi "Yo voy a tener sopa y sofrito, eso lo dices así…"

show misha sign_smile
with charachange

show misha perky_smile
with charachange

mi "Y esto es cuánto cuesta todo: ¡3685 yenes!"

show misha perky_smile:
    "misha cross_laugh" with Dissolve(0.5, alpha=True)
with None

extend " ¡Guajajajaja~!"

hi "Bueno, no sé en cuántas situaciones necesitaré recordar ese número exacto…"

mi "¡Ajajajaja! ¡Bien~! Ordenaré ahora, a menos que alguno quiera algo más. ¿Sin objeciones? ¡Bueno bueno, entonces!"

scene bg school_council_ni
show shizu behind_frustrated at tworight
show misha hips_smile at twoleft
with shorttimeskip

"Shizune impacientemente gira un par de palillos entre sus dedos mientras esperamos a que la comida llegue."

hi "Oye, ¿de dónde sacaste esos?"

show misha hips_grin
with charachange

mi "Esta no es la primera vez que ordenamos, Hicchan, y por alguna razón siempre nos dan una tonelada de palillos, incluso cuando les decimos que solo somos dos personas."

hi "¿Y ustedes dos han coleccionado un montón de ellos de muchas largas noches comiendo comida para llevar en la oficina?"

show misha cross_laugh
with charachange

mi "¡Eso es, exactamente! ¡Jajajajajaja!"

show shizu basic_angry
with charachange

shi "…"

show misha perky_confused
with charachange

mi "¿Estoy exagerándolo?"

show shizu behind_blank
with charachange

shi "…"

show misha hips_grin
with charachange

mi "¡Jaja! ¡Eso es cierto, Shicchan! Oye, Hicchan, ¿sabías que una vez que coleccionemos cien pares de palillos por ordenar comida, seremos capaces de apoderarnos del universo?"

hi "Solía pensar eso también, cuando era pequeño."

show misha perky_smile
with charachange

mi "Hicchan, ¿eres bueno para partirlos por la mitad? Nunca puedo hacerlo bien, así que encontré la pequeña pila de palillos que Shicchan había guardado y practiqué con al menos veinte de ellos."

show misha hips_grin
with charachange

mi "¡Ella estaba realmente molesta por eso!"

show shizu adjust_blush
with charachange

shi "¡…!"

"Dejo salir una risa mientras Shizune se pone claramente roja de indignación. No sabía que ella tuviera un lado tan infantil."

stop music fadeout 5.0

scene bg school_council_ni
with shorttimeskip


"Cuando la comida llega, comienzo a comer con apetito, bebiendo una de las pequeñas latas de gaseosa que Shizune trajo para nosotros de las máquinas expendedoras en el pasillo."

"Agradeciendo a ambas por la comida, me dirijo a los dormitorios, listo para prepararme para la noche."

scene bg school_dormhallway
with locationskip

"Los dormitorios están tenebrosamente silenciosos excepto por los sonidos de televisiones portátiles y radios murmurando ininteligiblemente detrás de las delgadas paredes."

$ renpy.music.set_volume(0.1,0.0, "ambient")
play ambient sfx_cicadas fadein 4.0

scene bg school_dormhisao_ni
with locationchange


"Es tranquilo aquí por la noche, y muy pacífico. Puedo escuchar a los grillos cantando fuera de mi ventana, y de hecho ver estrellas cuando miro arriba."

"Cansado, trato de quedarme dormido tan pronto como puedo, solo sintiéndome ligeramente despojado de mi sábado."

stop ambient fadeout 2.0

$ suppress_window_after_timeskip = True

scene black
with shuteye






label es_A37:






scene bg school_scienceroom at bgleft
with None

"La biblioteca parece tan buen lugar como cualquier otro para ir. Hanako lucía como si hubiese sido tomada con la guardia muy baja por Lilly yéndose, así que tal vez quiera alguien para hablar."

"Colgando mi mochila sobre mi hombro, salgo del salón de clases."

stop music fadeout 4.0

scene bg school_hallway2
with locationchange

"Camino por el pasillo hacia la biblioteca, pasando una multitud de puertas cerradas."

"A través de cada una el sonido de furiosos ensayos puede ser oído. Música rock retumba de una puerta, casi tan fuerte como un concierto."

"Supongo que esa es una de las ventajas de una escuela privada; hay de hecho suficientes cuartos para estar en un momento como este."

"Y cuando pienso en ello, los patios y edificios de la escuela son mantenidos en una muy buena condición. Eso no puede ser muy barato."

"He oído que este lugar tiene algunos benefactores muy serios."

scene bg school_library
with locationchange

play music music_happiness fadein 1.0

"Las paredes de la biblioteca solo aíslan parcialmente el ruido de las preparaciones del festival, pero esos son los únicos sonidos que pueden ser escuchados."

"Ni un alma se mueve aquí, con todos aparentemente disfrutando el clima afuera o trabajando en eventos del festival."

"Yuuko tampoco está aquí. Tal vez no trabaja los sábados."



"Tranquilamente camino a través de la biblioteca, ahora lo suficientemente familiarizado con su distribución. Me dirijo a la parte trasera, donde está la pequeña esquina privada de Hanako."

"Paso mi mano a través de los lomos de los libros en mi camino hacia allá, sintiendo la textura individual de cada uno mientras doy un vistazo a través de los títulos."

"Solía hacer esto todo el tiempo en la biblioteca del hospital. Algunas cosas nunca cambian, supongo."

"Como el aroma de una biblioteca. No importa cuánto cuidado te tomes, el papel de los libros siempre se va a degradar con el tiempo."

"Probablemente, no importa a cuál biblioteca vayas, en cualquier parte del mundo, debe tener el mismo aroma mohoso."

"Encuentro algo que parece lo suficientemente ligero para leerse sin pensar mucho, después busco a Hanako en el área de lectura."

scene ev hana_library_read_std
with locationchange

"Una vez más, ella está sentada en un puf con su espalda hacia un librero. Leyendo el mismo libro que había tenido en el salón de clase, ella está lentamente pasando a través de las páginas."

play sound sfx_pillow

show ev hana_library_std
with locationchange

"A diferencia de la última vez que la vi aquí, silenciosamente tomo asiento en un puf. El ruido es suficiente para captar su atención, pero no para espantarla."

"Esta delicada rutina que debe ser seguida cada vez que trato de hablarle se siente como un juego de cacería."

hi "¿Es ese el mismo libro de antes?"

ha "S-sí… Ya casi he terminado…"

hi "Qué bien."

"Me pregunto si debería…"

hi "¿Te molesta si lo tomo prestado cuando termines?"

"Mi boca es más rápida que mi mente, al parecer."

ha "S-seguro… t-tal vez no te guste pero…"

hi "Estoy seguro de que no puede ser tan malo. Después de todo, te has entretenido con él, ¿o no?"

ha "S-supongo."

scene bg school_library
with locationchange

"Me acomodo en mi puf y comienzo a leer mi propio libro que había estado sepultado en mi mochila."

"Es una novela ligera sobre piratas. Para ser honesto he estado pasando por encima de las palabras, habiendo escogido el libro simplemente porque pertenece a un género diferente al que usualmente leo."

"Encontrando difícil reunir suficiente entusiasmo para terminar el libro, y notando que inadvertidamente he distraído a Hanako un poco, decido intentar hacer conversación."

hi "Entonces, ¿veo que Lilly se fue sin ti?"

show hanako emb_downtimid at center
with charaenter

show hanako basic_worry
with charachange


"Ella asiente con la cabeza antes de apartar sus ojos de su libro. Debe de haber estado muy metida en él después de todo."

ha "Lilly dijo que tenía que ir y… ver a alguien…"

hi "¿Oh?"

show hanako basic_normal
with charachange

ha "A-Akira. Su hermana…"

hi "¿Hermana? No la he escuchado hablar sobre su familia…"

show hanako cover_distant
with charachange

ha "Ella… ella y Akira solían vivir juntas."

hi "Creí que todos los estudiantes vivían en los dormitorios…"

show hanako cover_worry
with charachange

ha "E-ellos… digo, nosotros… no tenemos que hacerlo."

hi "Pero es más fácil, ¿cierto? Quiero decir, hay comida aquí y estás cerca de la escuela… No creo nunca haber llegado a clase a tiempo tan seguido en mi vida."

show hanako cover_smile
with charachange

"Su mal escondida sonrisa resulta ser bastante gratificante."

"En el fondo sé que tengo algo de tarea en la cual ponerme al corriente, pero es bastante reconfortante aquí. Nadie puede encontrarme y forzarme a trabajar en su proyecto favorito, tampoco."

"Sin embargo, ahora que estoy pensando sobre el festival, otra pregunta surge…"


hi "Oye, Hanako, ¿qué vas a hacer en el festival?"

stop music fadeout 0.2

show hanako def_shock
with charachange

"Por un segundo creo que Hanako está por lanzar su libro al aire por el shock."

ha "¿D-disculpa…?"

hi "Solo preguntaba qué vas a hacer en el festival mañana. ¿Tienes planes?"

show hanako def_worry
with charachange

ha "Yo… no lo sé."

"Hanako responde en la forma en que lo hace la gente cuando no quieren que hagas más preguntas. Supongo que grandes multitudes y música fuerte no son su “estilo”."

hi "Oh, está bien."

"Cambia el tema, cambia el tema…"

play music music_happiness fadein 4.0

hi "Así que, ¿cómo es la hermana de Lilly?"

show hanako basic_normal
with charachange

ha "Ella… ella es buena. Es muy parecida a Lilly, pero viste… de negocios…"

hi "¿De negocios?"

show hanako basic_distant
with charachange

ha "Ella… ella siempre lleva puesto un traje…"

hi "Ah, ya veo. ¿Y eso la hace menos bonita de alguna forma?"

show hanako emb_emb
with charachange

"Hanako sacude su cabeza avergonzadamente."

ha "N-no… solo… diferente."

"Lo admitiré, esto me ha intrigado. Escuchar a Hanako hablar de alguien más además de Lilly para empezar, y de hacer cumplidos sobre ello también…"

"Pero mientras trato de imaginar a esta misteriosa hermana, todo en lo que puedo pensar es en Lilly en traje. Y no puedo imaginar eso como no atractivo. Para nada."

hi "Bueno, algún día tendrás que presentarme con ella."

show hanako basic_bashful
with charachange

ha "B-bueno."

"Nuestra corta conversación termina tan abruptamente como empezó, y ambos regresamos a nuestras novelas."

stop music fadeout 4.0

scene bg school_library_ss
with shorttimeskip

"El paso del tiempo solo es marcado por el gradual movimiento de la línea de luz proyectada a través de la ventana."

"Lentamente, los ruidos de los varios ensayos en el edificio se disuelven y mueren mientras los estudiantes comienzan a sentirse hambrientos y cansados."


"Solo pensar en eso hace que mi estómago empiece a retorcerse sobre sí mismo. Creo que es tiempo de volver."

hi "¿Crees que Lilly haya regresado para estos momentos? Creo que tal vez me iré a mi dormitorio. Estoy muy cansado de esta semana."

"Y ni una palabra de eso es mentira. Cambiarme a una nueva escuela mientras se prepara para un evento de gran magnitud ha sido agotador, por decir lo menos."

"Puedo sentirme cabeceando mientras leo mi libro."

show hanako basic_smile_ss at center
with charaenter

ha "E-está bien. Yo… yo tal vez estaré aquí un poco más."

"Mirando al libro de Hanako, puedo ver que ella está a solo unas pocas páginas de completarlo."


"Por un momento considero pasar el rato hasta que termine, pero una vez más mi estómago gruñe, emitiendo un sonido gorgoteante."

hi "Seguro. Bueno, me voy a ir a los dormitorios antes de que oscurezca. Te veré después, ¿está bien?"

show hanako basic_bashful_ss
with charachange

ha "B-bien. Nos vemos, Hisao."

hi "Hasta luego."

show hanako defarms_worry_ss
with charachange

ha "¿H-Hisao?"

hi "¿Hmm?"

show hanako emb_smile_ss
with charachange

ha "G-gracias. P-por pasar el rato conmigo."

play music music_dreamy fadein 2.0

"Puedo ver lo difícil que fue para ella dejar salir esa simple oración de su boca. Me deja suspenso por un momento."


"Así que. Hay alguien más en esta escuela que está aún más sola que yo."
"Tal vez solitario es una palabra equivocada, no he andado corto de compañía por esta primera semana, pero aun así me las he arreglado para sentirme de alguna forma solo y separado."

"Tal vez solitaria es una palabra equivocada para Hanako también, tiene a Lilly después de todo, ¿o no?"

"Me doy cuenta de que he estado parado ahí por mucho tiempo sin responder, y logro una sonrisa perfecta y no muy exagerada."

hi "De nada."

hi "Buenas noches, Hanako."

show hanako emb_downsmile_ss
with charachange

ha "N-noches."

scene bg school_hallway2
with locationchange

"La dejo terminar su libro y vuelvo a los dormitorios y a la promesa de comida…"

stop music fadeout 3.0

$ suppress_window_after_timeskip = True

scene black
with Dissolve(3.0)

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
