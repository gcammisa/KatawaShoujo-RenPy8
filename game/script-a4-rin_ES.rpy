label es_R30:

window hide None

scene bg school_scienceroom
with locationchange

window show

play music music_normal fadein 3.0

"Llego a clase a tiempo, aunque no a tiempo para el desayuno."

"El salón de clases está bañado en la suave luz del sol."

"Esto significa que va a hacer un calor insoportable en la tarde. Sin embargo, por ahora, es agradable."

"Veo la animada discusión de Misha y Shizune sobre cualquier cosa, Hanako mirando fuera de la ventana del salón, Mutou tropezando al entrar cuatro minutos tarde y sin recordar qué se supone que debería enseñar hoy."

"No podría imaginar abandonar la escuela así como así, aun si es solo por unas semanas."

"Por otro lado, Rin parece no tener problema con la idea, o seguirla."

"Pero si lo piensas, de algún modo me vi envuelto en su aislamiento insensato, aun si terminamos lastimándonos el uno al otro."

"¿O acaso fue así? Tal vez solo yo fui lastimado."

scene bg school_scienceroom_ss
with shorttimeskip

"Me toma hasta bien entrada la tarde para darme cuenta de que hoy es lunes. El club de arte se reúne este día."

"No solo eso. Debido a los exámenes, esta será la última reunión del club antes de las vacaciones de verano."




label es_R30x:

"En realidad no tengo ningún propósito de ir…"

"Pero quiero hablar con el maestro."

scene bg school_hallway3
with locationchange

"Por tanto, termino holgazaneando como un tipo raro frente al salón de arte, esperando a que la reunión termine."

no "¡Eso es todo por el trimestre, muchachos!"

"Su voz suena con fuerza suficiente para ser escuchada a través de la puerta y con demasiado entusiasmo para ser genuina."

no "La siguiente reunión será después de las vacaciones de verano, el lunes de la primera semana del siguiente trimestre."

no "¡Espero volver a verlos a todos entonces!"

no "¡Que tengan buenas vacaciones!"

play ambient sfx_crowd_indoors fadein 1.0
stop music fadeout 4.0

show crowd
with charaenter

"Hay un coro de voces confuso como respuesta, y la puerta al salón se abre, dejando salir un flujo de estudiantes."

"Espero a que todos los demás se vayan, para poder hablar con Nomiya a solas. Casi es la hora de la cena, así que no tengo que esperar mucho."

stop ambient fadeout 2.0

scene bg school_classroomart_ss
with locationchange




label es_R30y:

"Sin Rin se siente como si no tuviera sentido ir ahí, pero quiero hablar con el maestro."

scene bg school_classroomart_ss
with locationskip

"La reunión en sí no es digna de mencionar, al igual que mi habilidad con la acuarela no es digna de mencionarse."

"Nomiya trata de alentarme y aconsejarme sin sonar demasiado condescendiente, pero no está haciendo un trabajo muy bueno en ello."

"Si nada más, unirme al club de arte me ha enseñado que me gusta el arte. Aunque sería agradable si pudiera realmente intentar hacer un poco de arte en el club."

"Después de que los frutos de la labor de todos han sido rejuntados en una pila ordenada sobre el escritorio del maestro, él aclara la garganta para dar un pequeño discurso."

show nomiya talk at center
with charaenter

no "¡Eso es todo por este trimestre, muchachos!"

"Su voz suena bastante fuerte y con demasiado entusiasmo para ser genuina."

show nomiya smile
with charachange

no "La siguiente reunión será después de las vacaciones, el lunes de la primera semana del siguiente trimestre."

no "¡Espero volver a ver a todos entonces!"

show nomiya veryhappy
with charachange

no "¡Que tengan buenas vacaciones!"

hide nomiya
with charaexit

stop music fadeout 4.0

"Todos le desean de vuelta unas buenas vacaciones mientras salen en fila por la puerta."

"Yo me quedo atrás, esperando hasta que los dos nos quedamos solos. Es casi la hora de la cena, así que no tengo que esperar mucho."


label es_R30z:

"Nomiya está viendo las pinturas, algunas de las cuales son bastante buenas, de hecho."

"Puede que Rin supere a todos los demás en el club de arte, pero no es la única con talento."

hi "Disculpe, maestro…"

play music music_happiness fadein 2.0

show nomiya smile at center
with charaenter

no "¿Hmm? ¿Qué sucede, Nakai?"

"Levanta sus cejas a modo de pregunta, sonriendo ampliamente."

hi "Es sobre Rin…"

show nomiya frown
with charachange

no "¿Oh? ¿Hay algo malo con Tezuka?"

hi "No, pero…"

"Dudo por una fracción de segundo, inseguro de cómo decir lo que quiero decir, dándole suficiente tiempo a Nomiya de empezar a parlotear por cuenta propia."

show nomiya smile
with charachange

no "La vi hace unos días cuando estaba pasando por la galería de Sae."

no "Ella dijo que tendría hechas una o dos pinturas más para la exhibición."

show nomiya talk
with charachange

no "Estaba muy complacido, ella es una chica que trabaja sorprendentemente duro. Siempre había creído que era un poco floja, haciendo lo que quisiera en lugar de sus tareas…"

"Él parece notar mi ansiedad y se percata de que está divagando, guardando silencio antes de terminar su idea."

show nomiya smile
with charachange

no "Ah, pero si tenías algo de qué hablar. ¿De qué se trata?"

hi "No lo sé… ella se siente desconectada de todo, como si no pudiera pensar en nada más que la exhibición."

show nomiya frown
with charachange

no "Bueno, ¿no es eso bueno? Está concentrada en sus pinturas, como debería ser."

hi "Sí, pero esto es diferente. Es como si estuviese obsesionada. Fui a verla, y…"

show nomiya serious
with charachange

no "¿La has estado molestando?"

"Me interrumpe antes de que pueda terminar lo que quería decir, súbitamente viéndose muy irritado."

hi "No… yo… no creo."

hi "Solo estoy preocupado porque ha dejado de venir a la escuela por completo. Ella se siente extraña, también."

hi "Más extraña de lo usual, por lo menos."

show nomiya stern
with charachange

no "¡Disparates! Esto es mucho más importante para ella que una inmunda clase de Matemáticas, o Física, o lo que sea."

no "Esta es la razón exacta del porqué esta escuela es tan flexible, para darle al estudiante toda oportunidad de realizarse a sí mismo."

show nomiya serious
with charachange

no "Tezuka es una pintora, así que debería pintar, ¿no? Y tener una exhibición. Eso es lo que los artistas hacen. A ella se le debería de permitir concentrarse en eso, no estas otras clases frívolas. Ella debería de ser alentada."

no "Si piensas en ello, es realmente bastante obvio."

"Sus contestaciones no son muy convincentes, pero estoy teniendo dificultades tratando de pensar en algún tipo de réplica."

"Mi resentido silencio es interpretado como consentimiento, y Nomiya vuelve a barajar la pila de tareas entregadas sobre su escritorio como si se tratara de un mazo de cartas."

show nomiya smile
with charachange

no "Tengo que decir, ya que estamos hablando de la exhibición de Tezuka…"

no "Estoy muy emocionado por ver cómo resultará."

show nomiya dreamy
with charachange

no "Ella sigue siendo tan joven, y aun así tiene una habilidad maravillosa, ¡y estilo!"

"Le habla al aire, para relajar el ambiente que se tornó tan negativo."

show nomiya talk
with charachange

no "¿Me imagino que asistirás?"

hi "Sí, supongo que sí."

show nomiya smile
with charachange

no "Bien, a la próxima nos veremos allá."

stop music fadeout 3.0

scene bg school_hallway3
with locationchange

"Considero eso como mi oportunidad de irme. Y la tomo, aunque no estoy contento de ello."

"Mi mensaje no llegó, por no decir más."


$ suppress_window_after_timeskip = True

scene black
with dissolve


label es_R31:

window hide None
nvl clear

scene bg school_scienceroom_bw
with locationchange

nvl show dissolve

play music music_night fadein 1.0

n "\n\n\n\n\n\n\n\n\nAl siguiente día, todas las oportunidades perdidas y cosas que debería de haber dicho me caen encima. No resta nada por hacer después de ello, además de lamentarse."

nvl clear
nvl hide dissolve

with shorttimeskip

nvl show dissolve

n "\n\n\n\n\n\n\n\n\nSegundo día. Empiezo a sentirme con ansias. Comienzo a dudar de mis dudas y se siente estúpido, especialmente porque no puedo pensar en nada más que en Rin."

nvl clear
nvl hide dissolve

with shorttimeskip

nvl show dissolve

n "\n\n\n\n\n\n\n\n\nTercer día, examen de japonés, {b}y{/b} examen de Historia Universal. Genial. Lo que más odio de ella es que puede hacerme sentir así de horrible aunque debiera de concentrarme en cosas completamente diferentes en este momento."

nvl clear
nvl hide dissolve

with shorttimeskip

nvl show dissolve

n "\n\n\n\n\n\n\n\n\nCuarto día. Examen de Matemáticas. Tenemos un examen de Matemáticas. Va como va. No me importa."

nvl clear
nvl hide dissolve

with shorttimeskip

nvl show dissolve


n "\n\n\n\n\n\n\n\n\nQuinto día. Nomiya me pregunta de nuevo si asistiré a la apertura de la exhibición. No puedo decirle que no aunque realmente quiera hacerlo. Simplemente no quiero discutir con él nada relacionado con Rin así que es mejor tomar el camino menos difícil."

nvl clear
nvl hide dissolve

stop music fadeout 2.0

scene bg school_dormhallway
show rin basic_absent at center
with shorttimeskip

window show

"En el sexto día, el día antes de la apertura de la exhibición, encuentro a Rin de pie en el pasillo frente a mi habitación cuando regreso a los dormitorios después de cenar."

play music music_rain fadein 6.0

hi "¿Qué estás haciendo aquí?"

"Mi voz suena más enojada de lo que quería. Estoy un poco decepcionado de no haber podido contenerme a mí mismo, pero no hay más remedio."

"Rin solo está ahí de pie, como si acabara de pararse por mera coincidencia donde no tiene nada que ver. La manera tan fría en que reacciona a todo me molesta."

"Esto no está bien. Han sido seis días, y el solo verla me hace arder. Ni siquiera ha abierto la boca todavía."

show rin basic_deadpan
with charachange

rin "Terminé de pintar."

hi "¿No deberías de estar en la galería? ¿Preparándote?"

show rin basic_awayabsent
with charachange

rin "Dijeron que no."

"Entonces supongo que la galerista hace esa parte, hacer enmarcar las pinturas, colgarlas en las paredes y demás."

hi "Así que, ¿por qué estás aquí?"

show rin basic_deadpannormal
with charachange

rin "Se me ocurrió."

"Este mismo patrón estúpido emerge de nuevo; yo haciéndole preguntas a las que ella contesta con algo que no responde nada, porque es la única manera en la que podemos conversar."

"Aparte de escuchar su balbuceo sobre cualquier cosa, que realmente no es una conversación."

"¿Es esto una representación teatral? ¿Acaso hay roles invisibles en los que sin darnos cuenta nos hemos convertido, dictando las reglas del juego cada vez que nos vemos, inevitablemente llevándonos a lastimarnos el uno al otro?"

"Sus respuestas indiferentes acompañadas por ese encogerse de hombros de manera todavía más indiferente me dejan confundido. Supongo que debería de estar contento de que las preparaciones para la exhibición están completas."

play sound sfx_dooropen

scene bg school_dormhisao
with locationchange

"Cuando entro a mi cuarto, escucho sus pisadas seguirme hacia dentro."

"No la invité a entrar. No le pediré que se vaya."

show rin basic_awayabsent:
    center
    alpha 0.0
    ease 0.5 ypos 1.15 alpha 1.0
    parallel:
        ease 0.3 center
    parallel:
        "rin basic_absent" with Dissolve(0.3, alpha=True)
with Pause(0.5)

stop music fadeout 6.0

"Reclama mi cama sin pedirme permiso, haciéndome desear que haya tenido el tiempo de tenderla antes de salir esta mañana, luego se pone de pie otra vez como si se hubiera sentado en brasas ardientes."

"Me medio recargo sobre el único rincón de mi escritorio que no está lleno de cosas amontonadas, para descansar mis piernas por lo menos un poco."

show rin basic_awayabsent:
    center
    alpha 1.0
with charachange

"Rin pasa unos momentos echando un vistazo con curiosidad por mi habitación. Hace que me dé cuenta de que nunca ha estado aquí antes."

"Por un momento, ella realmente parece estarse concentrando. Tratando de absorberlo todo. Este debe ser el ojo para el detalle que la hace una artista."

show rin basic_absent
with charachange

"Ya que la habitación es pequeña, ella pronto se queda sin cosas que ver, pero nada más ocurre, permitiendo al silencio incómodo apoderarse del ambiente."

"El humor es frío por no decir más, y ambos estamos en guardia, esperando a que el otro haga el primer movimiento."

"Por supuesto, Rin podría jugar este juego por siempre. Así que tengo que ser yo."

hi "Y bien…"

"Me doy por vencido porque ella nunca trataría de iniciar una conversación, y porque parece que ella quiere hacer algo, y quiero terminar con esto."

"¿Por qué estaría aquí si no es porque quiere hablar?"

"Yo no sé qué decir. Quiero estar enojado, pero no me atrevo a gritarle o algo parecido."

"Mi voz capta su atención, y ella también trata de buscar palabras que decir, pero parece que tampoco está del todo segura del porqué está aquí."

show rin basic_absent_close:
    center
    ypos 1.05
    easein 0.5 ypos 1.0
with characlose

"Y así, Rin simplemente toma unos cuantos pasos para cerrar la distancia entre nosotros y se para de puntillas para igualar la diferencia de altura."

window hide

show rin basic_lucid_superclose at center
with charachange

centered "“Fue una mala idea.”"

centered "“Quizás deberías olvidarlo, y yo lo haré también.”"

window show

"Es un reflejo, y casi como una idea tardía, las palabras “no,” “sí” y “tal vez” emergen al mismo tiempo dentro de mi mente."

"Mi mano se encuentra entre sus labios y mis labios, un muro que he levantado para protegerme de… algo."

"Su aliento se siente cálido en mis dedos. El aroma de su piel permanece en el aire, la sensación indescriptible y misteriosa que me captura lleva mis ojos a la profundidad de sus ojos."

show rin basic_surprised_close
with charachange

play music music_moonlight fadein 0.5

"La mirada en sus ojos es de sorpresa, inquisitiva en cuanto al porqué de la mano impertinente que previene sus insinuaciones."

"Sus ojos son realmente grandes y relucen con humedad, y contemplando directamente hacia los míos con una mirada suave a la que estoy teniendo dificultad para igualar."

"La boca a medio abrir de Rin la hace verse todavía más confundida, aunque el sensual arco formado por sus labios señale algo completamente diferente."

show rin basic_upset_close
with charachange

rin "Por favor."

show rin negative_angry_close
with charachange

rin "Te necesito."

"Las palabras desde su garganta son tan ásperas como un susurro destinado solo para mí, circunvalando su lengua y dientes sin darles oportunidad de interrumpir."

show rin negative_angry
with Dissolve(0.15)
with vpunch

"Me espabilan en un instante, y torpemente retrocedo para tener un poco más de distancia entre nosotros, raspándome dolorosamente contra el escritorio en el proceso."

"Tal vez sea su elección de palabras, tal vez el modo en que las dijo, pero algo en ellas me repele."

"Algo está mal, está horriblemente mal otra vez."

hi "¿Necesitarme para qué?"

"Todos los sentimientos desagradables brotan nuevamente, y siento mis latidos repentinamente acelerarse por lo menos diez veces."

show rin basic_absent
with charachange

"Los ojos de Rin pierden foco y retroceden mientras su cuerpo se relaja de su estado de tensión, y se para derecha de nuevo."

show rin basic_deadpanupset
with charachange

rin "No creo que haya estado pensando en algo. ¿Por qué dibujas patrones en el polvo sobre tu mesa de noche?"

show rin basic_awayabsent
with charachange

rin "Hay una palabra para ese tipo de cosas pero no la puedo recordar…"

"Su comentario casi me hace perder la concentración y echo un vistazo sobre su hombro a la mesita enseguida de mi cama, pero no puedo ver nada a esta distancia."

"¿Así que no me necesita para nada en especial?"

"Tan solo pasa que vino para acá porque pensó que estaría contento de verla después de que me apartara, sin aceptar quejas, por una semana."

"¿Motivos completamente altruistas?"

"¿Se le ocurrió?"

hi "Tonterías. Puedo responder por mí mismo."

hi "¿Para jugar con mi mente cuando te dé la gana, besar cuando te dé la gana, ignorar cuando te dé la gana, satisfacer tus caprichos cuando te dé la gana?"

hi "¿Es eso? ¿Para lo que me necesitas?"

"Mi voz suena muy enojada otra vez, incluso para mí mismo."

extend " Bien."

show rin basic_absent
with charachange

"Rin también entiende el ambiente finalmente y su expresión de curiosidad cambia inmediatamente a algo más atípico."

show rin negative_sad
with charachange

rin "No—"

"Ella lo deja en eso, sus ojos divagando alrededor sin descanso, buscando en el cuarto como si las palabras que intenta encontrar estuviesen escritas en el empapelado de mis paredes."

hi "¿Entonces qué?"

show rin negative_confused
with charachange

stop music fadeout 2.0

rin "Necesitaba pintar."

"Pintar."

"Claro. Eso es lo que hacen los artistas."

"Las palabras reverberan a través de mi ser, latiendo en mi sangre por sobre el silbido ensordecedor de mi ira."

play music music_tragic fadein 2.0

hi "¡No me vengas con eso, Rin! ¡No soy alguna maldita musa tuya, libre de ser abusada por el bien de la pintura!"

hi "No soy algún medio para lo que sea que tú aspires, ¡yo soy yo!"

hi "¿Y qué si no sé nada de mi futuro?"

hi "¡Hay cosas que quiero, y cosas que me importan! ¡Incluso yo puedo soñar con algo más que pesadillas!"

"Estoy gritando, pero estoy más allá del punto en el que me importan cosas como esa."

show rin negative_sad
with charachange

"Rin mira abajo hacia sus dedos y los mueve un poco con melancolía mientras recibe mi estallido sin decir nada para defenderse a sí misma."

"Solo hasta que yo termino ella intenta responder de algún modo."

show rin basic_sad
with charachange

rin "No puedo hacer nada más. O puedo hacer todo tipo de cosas, pero… no puedo… hacer."

show rin basic_upset
with charachange

rin "Es la única cosa que hago más o menos bien. La mayoría del tiempo."

"Lo entiendo completamente. El arte es primero, todo lo demás está en segundo lugar, o en el milésimo."

hi "¿Qué hay de mí? ¿No soy nada? Cuando estaba interesado en el arte, ¿acaso eso te hizo sentir como si yo fuese un poquito interesante, por un corto momento?"

hi "Dime. Realmente quiero saberlo. ¿Alguna vez pensaste en mi perspectiva, o acaso todo se trata de ti?"

"Las palabras se alzan como hiel en mi garganta."

show rin basic_surprised
with charachange

"Ella se ve alarmada. Y también completamente desconcertada, como si simplemente no comprendiera por qué estoy enojado."

"No puedo creer que ella sea tan estúpida."

show rin negative_sad
with charachange

rin "¿Yo no quise—?"

"Esta vez es Rin quien se interrumpe a sí misma a media palabra."

show rin basic_upset
with charachange

rin "¿No entiendes? No puedo."

hi "¿No puedes qué?"

hi "¡Nunca te explicas! ¿Cómo se supone que vaya a entender algo si nunca dices nada?"

hi "¿Por qué nunca hablas?"

hi "¡Di algo!"

"Pero no lo hace."

"Descargar mi ira sobre ella se siente agradable y sentirme satisfecho con ello se siente terrible, pero no puedo detenerme."

show rin negative_annoyed
with charachange

"No queriendo encontrar mi cólera de frente, Rin se vuelve para mirar fijamente fuera de mi ventana aunque no haya nada que ver allá."

"Lo peor de mi ira se ha ido, me callo ya que no puedo tomarme la molestia de continuar gritándole a la nuca de Rin, así que el silencio finalmente regresa."

"Trato de discernir algún indicio de su reacción a través de mi visión distorsionada por la adrenalina."

"Mi crítica no fue del mejor tipo, pero espero que Rin tenga una idea clara de que no puede simplemente ignorar todo lo demás cuando sea que le dé la gana."

"Odiaría que no fuese así. Ella nunca pero nunca escucha algo, el mundo a su alrededor jamás la altera."

"No esta vez, parece ser."

"Su cuerpo tiembla como si estuviese conteniendo el llanto, pero yo ya sé que Rin no está llorando."

"Su indiferencia me puso furioso. Ahora que se ha ido, me quedo sin palabras. Me pregunto…"

"¿Fui demasiado lejos?"

hi "Escucha, yo—"

show rin negative_angry
with charachange

rin "Vete."

rin "Vete, Hisao."

"Su voz suena tan diminuta y cansada cuando dice esto, pero escucho las palabras tan claras como el día."

"…"

"¿Qué más queda por decir?"

hi "Esta es mi habitación."

"El comentario, hueco y directo, es una conclusión apropiada para esta desagradable discusión convertida en un todavía más desagradable y desigual concurso de gritos."

show rin basic_lucid
with charachange

"Después de un momento para recobrar la calma Rin se da por vencida, puedo verlo por el modo en el que baja sus hombros, y camina hacia afuera."

hide rin
with charaexit

"Aunque ella deliberadamente vea en otra dirección, puedo ver que se muerde la comisura del labio tan fuerte que podría empezar a sangrar si no se detiene."

"Cuando hace su salida, me percato de que ella dejó la puerta abierta al entrar y mis gritos deben haber hecho eco por los pasillos del dormitorio."

"Suspiro. Ahora que se ha ido, me quedo solo con mi culpa."

"A medida que el golpeteo en mi pecho se tranquiliza poco a poco, la ansiedad lo reemplaza."

"De algún modo siento que nada de esto habría pasado de no ser por mí."

"No importa cuán exasperante, insoportable y abusiva sea Rin, ella no es la Rin que pensé que conocía."

"La Rin que esperaba que fuera Rin."

"…"

"¿Acaso fui yo quien causó todo esto al convencer a Rin de probar su suerte con la exhibición?"

"¿Soy directamente responsable de que Rin se convirtiera en lo que ha sido las últimas semanas?"

"No puedo pensar en alguna explicación para su extraño comportamiento, además de la exhibición y todas las cosas que vinieron junto con ella."

"Tal vez era el único camino que podría habernos unido, pero todo lo que hizo fue separarnos todavía más el uno del otro, y ahora más allá del alcance de cualquiera de los dos."

play sound sfx_impact2
with vpunch

"Golpeo con fuerza mi cabeza contra la pared."

play sound sfx_impact2
with vpunch

stop music fadeout 4.0

"Dos veces, para asegurarme de que duele."

scene black
with dissolve



label es_R32:

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_traffic fadein 0.5

scene bg gallery_ext
with locationchange

"Una jaqueca retumba contra mi nuca sin descanso cuando empujo para abrir la puerta a la 22a Esquina."

"Además de eso, estoy perfectamente tranquilo."

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")

window hide
nvl clear
nvl show dissolve

n "\n\nDespués de descargar sobre Rin todo el enojo que tenía reprimido, se sintió como si un gran peso se hubiese levantado de mi corazón."

n "La tensión que se había aferrado a mi mente durante las semanas anteriores se desvaneció sin dejar siquiera una sombra detrás."

n "En este estado cercano a la iluminación Zen me percato de que tal vez fue una mala idea gritarle de esa manera."

n "\nHablaba muy en serio pero, ¿qué bien hace explotar así? Ninguno."

n "Yo no soy así. Yo no le grito a la gente normalmente. No sé por qué lo hice ayer."

n "Así que me sigo sintiendo bastante culpable al respecto y sigo queriendo retractarme."

n "\n\nRin probablemente también está molesta. Aun más que mi propio comportamiento, su reacción me conmocionó."

nvl clear

n "\nSiempre había pensado en ella como alguien invariable, distante de sus alrededores así que ver que mis gritos la hayan molestado tanto se sintió… fuera de lugar."

n "\n¿Me pregunto si entiende cómo me siento?"

n "En el mundo de Rin todo parece ser tan absoluto y subjetivo… absolutamente subjetivo, como si ella fuese completamente incapaz de ver las cosas desde un punto de vista diferente al suyo."

n "Pero después de todo, ¿hay alguien capaz de hacerlo? Quizás el objetivismo y el altruismo son solo ilusiones para la gente que gusta de pensar en sí misma como compasiva."

n "Justo como el arte es una ilusión para la gente que piensa que la realidad es meramente un velo para algo más grandioso."

n "Aun cuando dejas de pensar que el mundo da vueltas alrededor de ti o comienzas a pensar en algo distinto al mítico común, tan solo estás dentro de otro común más grande del que no puedes escapar."

n "\nTal vez eso, a fin de cuentas, la hace como el resto de nosotros."

stop ambient fadeout 1.0

nvl clear
nvl hide dissolve

play sound sfx_storebell
$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 0.5

scene bg gallery_int
show crowd
with locationchange

window show

play music music_ease fadein 3.0

"Camino por la puerta para encontrarme con la galería llena de gente ilusionada."

"A pesar de las observaciones de Sae durante mis primeras visitas yo siempre pensé que era muy espaciosa, pero ahora que está así de llena de gente, definitivamente se ve pequeña."

show sae smile at center behind crowd
with charaenter

"Inmediatamente noto a Sae de pie en medio de una animada discusión, ocupada charlando con algún caballero mayor."


"Ella de hecho es bastante alta y se ve algo espectacular, así que sobresale de la multitud."

"Hay unas docenas de copas de vino colocadas sobre las mesas a lo largo de la pared del fondo, llenas de líquido color borgoña. Una vasta mayoría de los invitados bebe de sus copas."

"Los miembros de la alta sociedad y los conocedores de arte se mezclan con alegría intercambiando leves comentarios sobre el arte de Rin, el cual parece ser un objeto de interés secundario para la mayoría."

"Me siento distanciado, excluido del resto de la gente aquí."

"No puedo afirmar, incluso si exagerara, ser un camaleón social, así que esta situación es bastante inquietante."

"Ya que no me mezclo con la multitud en absoluto, solo finjo que lo hago, tratando de verme tan indiferente y seguro como puedo."

"Me pregunto cómo estará manejando Rin todo esto. Si fuera yo, estaría aterrado."

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene bg gallery_exhibition
show crowd
with locationchange

"Haciendo la ansiedad a un lado, trato de navegar con cuidado a través de la muchedumbre, robándole miradas a las pinturas enmarcadas ahora colgando sobre las paredes."

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

scene rin_exhibition_paintings
with locationchange

"La exhibición de Rin toma alrededor de la mitad del espacio en las paredes de la galería. Algunas de las pinturas me resultan menos familiares que otras, pero reconozco la mayoría de ellas."

"Algunas las he visto siendo creadas en las reuniones del club después de todo, o las recuerdo de las veces en las que Rin estaba escogiéndolas para su portafolio."

"Noto que un par de pinturas sin terminar están enmarcadas y en la pared, también. ¿Tal vez eso es lo que llaman arte fortuito?"

"Incluso los fracasos de Rin, si puedes llamarlos así, se han convertido en una pieza de exhibición de su habilidad. Bastante paradójico."

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene bg gallery_exhibition
show crowd
with locationchange

"Ella no se deja ver por ninguna parte, lo cual es extraño porque aun si está repleto de gente, la galería {b}es{/b} bastante pequeña."


"Está bien, más o menos. No sé qué cara ponerle después de lo de ayer. Tal vez no debería ni haber venido."

"Pero se lo prometí a muchas personas, incluida Rin, que vendría, así que…"

"Maldición, suena como si hiciera las cosas que hago a causa de algún tipo de honorabilidad instintiva que me obliga, no porque fuera sensato (o no)."

scene bg gallery_int at right
show sae smile at center
show crowd at right
with locationchange

"Me escabullo más cerca de Sae para esperar por un descanso en la conversación y así también poder charlar con ella."

"Aunque su voz esté casi completamente sumergida debajo del ruido de fondo generalizado, escucho pedacitos de ella hablando sobre Rin."

sa "Sí, ella es una estudiante de preparatoria en una escuela local… aunque se graduará el siguiente año estoy segura de que varias escuelas de arte estarán interesadas en…"

sa "… Pensé que sería interesante tener una exhibición de alguien que todavía está en las fases iniciales de desarrollo…"

"Es tan extraño, es como si Rin fuese algún tipo de minicelebridad aunque esto no sea más que una apertura de una pequeña exhibición en una pequeña galería de arte en una pequeña ciudad."

sa "De hecho, hay un amigo mío de…"

play sound sfx_impact
with vpunch

mystery "¡Es Hisao!"

"Dejo de escuchar a escondidas al ser interrumpido por una voz familiar y una palmada familiar en la espalda. No necesito adivinar de quién viene, aun si no me doy vuelta."

hi "Hola Emi."

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

show emicas invis:
    center
    xpos 0.15
with None

show bg gallery_int at left
show sae invis:
    xpos 0.75
show crowd at left
show emicas happy at center
with dissolvecharamove

hide sae
with None

emi "¡Hola! ¿Eres como, un representante del club de arte o algo así? No veo a nadie más de la escuela aquí…"

hi "Ahh… No lo sé, en realidad. Supongo que lo soy si ese es el caso."

hi "¿Qué hay de ti?"

show emicas neutral
with charachange

emi "¿Qué hay de mí?"

hi "Ehh…"

show emicas angry_up
with charachange

emi "¿No pensaste que estaría interesada en el arte? ¿Es eso, Hisao?"

hi "No, eso no es lo que yo… bueno, tal vez un poco, si lo pones de esa manera."

hi "Quiero decir, aun si te juntas con Rin nunca te he escuchado hablar de arte con ella así que…"

show emicas awayfrown_up
with charachange

"Emi resopla y mira a su alrededor, viéndose descontenta."

show emicas closedsmile
with charachange

emi "Es verdad, no lo entiendo para nada, pero vino a mi competencia de atletismo así que solo pensé que es justo regresar el favor."

show emicas wink_close
with characlose

"Se inclina hacia mí, tratando de parecer confidente pero solo logrando verse conspirativa."

emi "¿Tú {b}entiendes{/b} el arte?"

hi "No. No lo entiendo."

hi "En absoluto."

show emicas closedsmile_close
with charachange

"El sacudir mi cabeza como énfasis extrae una risilla y un alegre meneo de cabeza de Emi."

show emicas happy_close
with charachange

emi "¡Yo tampoco!"

show emicas wink_close
with charachange

emi "Oye, ¡vamos a hablar con Rin! Apuesto a que todavía no has ido, porque yo tampoco he ido."

show emicas happy_up_close
with charachange

emi "¡Vamos!"

show nomiya invis behind emicas:
    center
    xpos 0.8
show rin invis:
    center
    xpos 1.1
with None


show bg gallery_int at center
show crowd at center
show emicas neutral_close:
    xpos 0.15
show nomiya smile:
    xpos 0.55
show rin basic_awayabsent:
    xpos 0.85
with dissolvecharamove

"Antes de que tenga una oportunidad de arrastrarme a la fuerza hacia Rin, Nomiya aparece detrás de ella con Rin a sus espaldas."

"Ella no está vestida para la ocasión, en su lugar optando por el uniforme escolar usual y cabello desarreglado."

"Quizás su apariencia natural es lo que queda mejor."

show emicas happy_close
with charachange

emi "¡Hola, maestro! ¡Qué tal, Rin!"

"Sin inmutarse, Emi saluda al maestro con alegría, ocasionando que él se tenga que dar vuelta y mirar hacia abajo confundido."

show nomiya frown
with charachange

no "¿Quién eres?"

show emicas frown_up_close
with charachange

emi "Soy Emi, de la escuela, grupo 3-4. ¿No me recuerda?"

"Se ve bastante asombrada ante la posibilidad de que pueda haber alguien que no la conoce."

show nomiya talk
with charachange

no "Oh, disculpa. Estás en el mismo grupo que Tezuka, ¿verdad?"

show emicas wink_close
with charachange

emi "¡Sí!"

show nomiya smile
with charachange

no "Tendrás que perdonarme, tengo problema recordando estudiantes que no cursan arte."

show emicas closedsmile_up_close
with charachange

emi "¡No hay problema, no hay problema!"

show emicas happy_close
with charachange

emi "¡Qué tal Rin!"

show rin basic_deadpan
with charachange

rin "Hola."

show emicas happy_up_close
with charachange

emi "¡Felicidades por tu cosa de arte supergenial! ¡Estoy segura de que serás un gran éxito!"

"Ella lanza sus manos al aire para un escandaloso énfasis, casi golpeándome en la cara."

show emicas wink_up_close
with charachange

emi "¡Y mira, Hisao también vino!"

show rin relaxed_nonchalant
with charachange

"Rin no me mira, tampoco me saluda."

hi "Felicidades, Rin."

"Ella sigue desviando su mirada, mirando fijamente a sus sandalias."

show emicas closedsmile_close
with charachange

"Inconsciente de la tensión entre nosotros e ignorante de lo sucedido ayer, Emi sigue parloteando sobre esto y aquello a una Rin indiferente."

"Supongo que está acostumbrada a no observar mucho en ella de cuando en cuando."

stop music fadeout 5.0
$ renpy.music.set_volume(1.0, 3.0, channel="ambient")



show sae invis behind rin:
    center
    xpos 1.25
with None

show bg gallery_int at right
show crowd at right
show emicas invis:
    xpos -0.35
show nomiya smile:
    xpos 0.25
show rin relaxed_nonchalant:
    xpos 0.55
show sae neutral:
    xpos 0.8
with dissolvecharamove

hide emicas
with None

"En poco tiempo, Nomiya y Sae se vuelven hacia Rin, presentándola."

"Esperando eso, capto el segundo de confusión cuando los invitados ven sus brazos."

show sae smile
with charachange

"Sae por suerte tiene eso en mente y brevemente explica nuestra escuela."

"Los rostros dudosos rápidamente cambian a curiosos."

"Hombre" "¿Te importaría decirnos algo sobre tu arte?"

"Hombre" "Pienso que el desarrollo es bastante fácil de notar, ¿qué piensas tú misma de las diferencias entre tus viejas y tus más recientes obras?"

"Hombre" "Es bastante raro para alguien tan joven incursionar en lo abstracto."

"Mujer" "¡Sería interesante ver cómo trabajas!"

"Hombre" "¡Oh, definitivamente! ¿Asumo que usas tus pies? Debe haber sido un gran problema aprenderlo, deberías de estar orgullosa."

show rin basic_surprised
with charachange

rin "Yo… ehhh…"

play music music_rain fadein 8.0

"Hombre" "¿Seguirás una carrera como artista después de la escuela?"

"Rin es bombardeada con tantas preguntas que no puede ni esperar a responderlas todas."

"Quizás eso sea para lo mejor, Rin tiende a decir tonterías más que ocasionalmente."

"Hombre" "Y bien, ¿de dónde obtienes tus ideas?"

show rin relaxed_boredom
with charachange

rin "Esa es la cuarta, quiero decir quinta peor…"

"Rin sigue tropezándose con sus palabras, viéndose más y más irritada por las ansiosas preguntas."

show rin negative_annoyed
with charachange

rin "Ah…"

"Todos esperan que diga algo, pero parece que el ratón le comió la lengua."

"Cada pregunta que se va amontonando solo se suma a su angustia."

show rin basic_sad
with charachange

"No puedo escuchar la pregunta que es la gota que derrama el proverbial vaso."

"Es como un motor que se para."

show rin basic_sad:
    1.2
    parallel:
        easeout 0.5 ypos 1.2
    parallel:
        "rin basic_lucid" with Dissolve(0.3, alpha=True)
with Pause(1.5)

stop ambient fadeout 7.0

scene ev rin_gallery:
    truecenter
    zoom 0.9 subpixel True
    easein 30.0 zoom 1.0
with Dissolve(0.2)
play sound sfx_pillow
with vpunch

"Rin simplemente se congela por un largo, largo segundo hasta que cae sobre sus rodillas, golpeando el suelo sin gracia como un saco de papas."

"Mujer" "¿Te encuentras bien?"

rin "No lo sé…"

no "¿Tezuka? ¿Qué sucede, mi niña?"

rin "No sé qué está mal…"

"Un terrible silencio cae sobre la gente reunida en torno a Rin."

"Todos están hechos piedra, sin saber cómo reaccionar a su súbito… ataque, o algo."

"Ella respira con jadeos profundos y temblorosos como si se le estuviera acabando el aire, mirando al frente con ojos vacíos."

play sound sfx_rustling
stop music fadeout 1.0

scene bg gallery_int at right
show crowd at right
show nomiya serious:
    center
    xpos 0.25
show rin negative_sad_close:
    center
    xpos 0.55 ypos 1.2
    ease 0.8 ypos 1.0
show sae scowl:
    center
    xpos 0.8
with locationchange


"Al ver que nadie hace nada, atravieso la muchedumbre a la fuerza para ir hacia Rin y la levanto del suelo, permitiendo que se recargue en mí para mantenerse en pie."

hi "¿Te gustaría un poco de aire fresco? Está bien, vamos hacia afuera un poco."


"Ni siquiera espero a que me responda antes de sujetarla del hombro y jalarla frente a Nomiya, Sae, Emi y los invitados con miradas estupefactas."

hi "Discúlpenos."

play sound sfx_storebell
$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_traffic fadein 1.0

scene bg gallery_ext
with locationchange

"La fría brisa de la noche me alcanza en el rostro en la puerta."

show rin negative_sad_close_ni at center
with charaenter

"Dejo ir a Rin y se recarga sobre la pared de piedra, intentando recuperar el aire."

hi "¿Te encuentras bien?"

show rin negative_confused_close_ni
with charachange

rin "No podía decir nada…"

"Rin sigue sin verme, así que aparto mi mirada."

play music music_dreamy fadein 4.0

"El alumbrado público y las señales de colores neón distorsionan mi visión en una mancha casi enceguecida, obligándome a mirar a otro lado."

"Por lo menos habla, aun si no está dirigiendo sus palabras hacia mí."

hi "¿Qué querías decir?"

"Tal vez ambos podemos imaginar que estamos hablando con un amigo invisible."

show rin basic_sad_close_ni
with charachange

rin "No lo sé."

show rin negative_sad_close_ni
with charachange

rin "Algo que significara algo."

"…"

"El silencio dura por un largo rato."

"No me siento cómodo estando a solas con Rin. No soy bueno imaginando que existen cosas que no lo hacen… o que no existen cosas que sí lo hacen."

hi "Deberíamos volver adentro."

hi "La gente que Sae invitó está ahí dentro, probablemente ellos quieran conocerte y hablar contigo."

hi "Tú sabes, hacerte preguntas y cosas así. Sobre esas pinturas para las que trabajaste tan duro."

show rin negative_angry_close_ni
with charachange

rin "No quiero que me hagan preguntas así. Nunca puedo decir las cosas correctas."

hi "¿Entonces qué quieres?"

"…"

show rin relaxed_doubt_close_ni
with charachange


label es_choiceR32:
menu:
    with menueffect
    rin "Que alguien no tuviera que hacerme preguntas."
    "¿No estás feliz de que la gente se interese en tus pinturas?":



        return m1
    "Pero si encontraras a alguien así, ¿entonces qué?":

        return m2

label es_R32a:

$ renpy.music.set_volume(0.2, 0.2, channel="ambient")

hi "¿Pero que no estás feliz de que la gente esté interesada en tus pinturas?"

hi "Quiero decir, ¿no es esa la razón de que hayas seguido adelante con la exhibición y todo eso?"

hi "Por supuesto que te harían preguntas, si pensaran que es interesante."

show rin negative_annoyed_close_ni
with charachange

rin "Es como si tuvieras dos amaneceres uno después del otro cuando quieres bañarte desnuda bajo la luz de la luna."

show rin negative_angry_close_ni
with charachange

rin "Agradable, pero…"

"… no es lo suficientemente bueno, completo la oración por ella aun si no entiendo su metáfora inapropiada."

hi "No lo comprendo."

hi "Deberías de tratar de estar más alegre. Es tu gran noche, después de todo."

hi "Todas estas personas están aquí para ver tus pinturas. Yo creo que es estupendo."

"Espero a que diga algo, ya sea a favor o en contra, pero Rin se sigue lamentando."

"No quiere responder preguntas, o explicarme qué es lo que está mal."

"Si ella tenía algo que decir, las palabras se quedan sin ser dichas."

"Las palabras que ella no puede decir."

"Me da un escalofrío el viento helado que sopla en las calles, y su aullido llena el silencio."

hi "Deberíamos volver adentro."

hi "Tienes a todos preocupados."

stop ambient fadeout 0.5
play sound sfx_storebell

scene bg gallery_int
show crowd
show nomiya talk at twoleft
show sae neutral at tworight
with locationchange

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0

no "¡Ah, ahí estás! ¿Te sientes mejor? Puede ponerse muy acalorado aquí adentro, un mareo puede tomarte desprevenido."

show nomiya veryhappy
with charachange

"Se ríe con descaro, casi es desagradable."

show nomiya talk
with charachange

no "Deberías de beber algo si te sientes débil, Tezuka."

show nomiya talk:
    center
    xpos 0.25
show sae neutral:
    center
    xpos 0.8
with charamove

show rin basic_lucid:
    center
    xpos 0.55
with charaenter

"Rin asiente débilmente, pero parece ser suficiente para convencer a Nomiya de que está bien."

"Empuja a Rin un poco hacia adelante para presentarla a la persona con la que él estaba conversando anteriormente."

show nomiya smile
with charachange

no "Y bien, de lo que estábamos hablando antes…"

"Hombre" "Ah sí, estoy muy emocionado por conocer…"

stop music fadeout 8.0

"Soy retirado de la conversación, y el ruido de fondo de docenas de otras discusiones llena mis oídos con un zumbido indistinto."

"Incluso Emi ha desaparecido en algún lugar."

"Estar de pie en medio de una multitud es una sensación sorprendentemente solitaria."

"No solo Rin, sino todos los demás parecen ser parte de algo de lo que yo no soy parte."

"Estoy feliz por ella, en verdad lo estoy, pero me hace sentir como si yo no hubiera logrado nada todavía."

"Rin es prueba viviente del potencial de un ser humano. Ella derrotó su discapacidad, incluso la hizo una fuerza."

stop ambient fadeout 4.0

"Ella debería de estar feliz."

"¿Cuál es mi potencial?"

"Rin logró llegar hasta acá, pero, ¿qué tan lejos puedo llegar yo?"

scene black
with dissolve


label es_R32b:

$ renpy.music.set_volume(0.2, 0.2, channel="ambient")

hi "Pero si encuentras a alguien así, ¿entonces qué?"


hi "¿En verdad piensas que sería alguna especie de cosa definitiva, amantes destinados y todos felices para siempre?"

show rin basic_absent_close_ni
with charachange

"Mi pregunta se encuentra con una mirada en blanco, la oscuridad en sus ojos impávida ante la amargura mal disimulada."

show rin negative_worried_close_ni
with charachange

rin "No, no pienso eso."

show rin negative_annoyed_close_ni
with charachange

rin "Pero por lo menos entonces no tendría que estar sola."

"Le susurra las palabras a las luces de la ciudad pero las escucho de igual modo."

show rin negative_sad_close_ni
with charachange

rin "No debería de haber hecho esto. No todavía."

hi "¿La exhibición?"

show rin basic_lucid_close_ni
with charachange

"Ella asiente y cierra los ojos, dejando salir el aire con tranquilidad como si probara que puede, y entonces continúa hablando consigo misma."

hi "¿Por qué? ¿Mala conjunción de los planetas?"

show rin basic_sad_close_ni
with charachange

rin "No, eso no. Revisé dos veces, y me levanté con el pie derecho, quiero decir izquierdo, e hice todo a la izquierda, quiero decir correcto."

show rin negative_sad_close_ni
with charachange

rin "Soy yo."

show rin negative_worried_close_ni
with charachange

rin "Yo estaba mal."

hide rin
with charaexit

"Ella se para derecha y se estira antes de pasar frente a mí y hacia la calle."

hi "Espera, ¿adónde vas?"

show rin basic_absent_ni
with charaenter

"Ella se detiene en seco y se da vuelta, mirándome con curiosidad."

show rin basic_awayabsent_ni
with charachange

rin "Escuela. Me voy."

hi "Qué… ¿Por qué?"

show rin basic_absent_ni
with charachange

rin "Porque quiero ser yo."

$ renpy.music.set_volume(0.4, 1.0, channel="ambient")

hide rin
with charaexit

"Rin se marcha, dejándome detrás completamente confundido."

hi "¡Rin!"

"Pero… algo que ella dijo en verdad me tocó, o quizás fue cómo lo dijo."

"Tal vez fue el hecho de que {b}ella{/b} lo dijera."

"Quiero decirle algo de vuelta, antes de que olvide este sentimiento de nuevo."

"Como si me cumpliera un deseo, Rin se detiene en seco. Ella no se da vuelta, solo sigue esperando a que yo diga lo que quiero decir aun si no tuve tiempo de pensar en qué…"

hi "Rin… escucha. Yo… Yo no creo que tengas que estar sola, aun si nunca conoces a alguien así."

"No sé si escuchó mis palabras, pero de cualquier modo, no reacciona de ninguna manera."

"Por última vez, ella comienza a caminar alejándose de la galería."

play sound sfx_storebell
stop ambient fadeout 0.5

scene bg gallery_int
show crowd at center
show nomiya frown at twoleft
show sae doubt at tworight
with locationchange

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0

no "¿Y bien? ¿Dónde está Tezuka?"

"Tan solo puedo sacudir la cabeza, pero ya que no parece ser una respuesta suficiente tengo que decir algo."

hi "Se escapó."

show nomiya stern
with charachange

no "¿Qué?"

"La espantosa comprensión se extiende por su rostro como un incendio."

show nomiya serious
with charachange

no "¡Esto es un fiasco! ¡Una catástrofe!"

no "¿En qué está pensando esa niña?, el evento más importante de su vida, ¿y simplemente corre?"

show nomiya stern
with charachange

no "¡Y tú! ¿Por qué no la detuviste? Voy a hacerte personalmente responsable…"

show sae neutral
with charachange

"Sae lo interrumpe, manteniendo sus manos en alto tranquilamente."

"Es bueno que ella interviniera; el maestro empezaba a recibir algunas miradas raras de los invitados cercanos."

show sae smile
with charachange

sa "Ya, ya, Shinichi. Ella probablemente solo tuvo pánico escénico. No la conozco tan bien como ustedes, pero sí tuve la impresión de que ella es un tanto peculiar."

sa "Este tipo de cosas suceden."

show sae neutral
with charachange

sa "Estará bien. Les explicaré que de pronto enfermó. Los invitados seguramente entenderán."

show nomiya frown
with charachange

no "Pero…"

show sae smile
with charachange

sa "Mira a tu alrededor, todos parecen bastante contentos con su vino gratis y charlas."

show nomiya serious
with charachange

no "¡Los invitados estarán bien, pero estamos perdiendo una oportunidad aquí! ¡Interconexiones, hacer contactos y conocidos!"

show emicas invis_close:
    center
    xpos -0.35
with None

show bg gallery_int at left
show crowd at left
show nomiya serious:
    xpos 0.5
show sae smile:
    xpos 0.9
show emicas frown_close:
    xpos 0.15
with dissolvecharamove

"Mientras los adultos siguen discutiendo sobre algo que no tiene remedio, Emi tira de mi manga para llamar mi atención."

"Ella tampoco se ve muy contenta."

show emicas awayfrown_close
with charachange

emi "Vamos."

hi "¿Adónde?"

show emicas frown_up_close
with charachange

emi "Vamos a encontrar a Rin y patearle el trasero."

hi "¿Qué?"

show emicas angry_close
with charachange

emi "No puedo creerlo, ¡es tan estúpida!"

emi "Esa Rin, ¿cómo puede hacer esto? Déjame decirte, ¡ella no tiene un cachito de sentido común en la cabeza!"

"Emi en serio está furiosa, solo le falta vapor alzándose de sus orejas."

"Supongo que entiendo a Emi, ella es de {b}ese{/b} tipo de personas."

"“Rendirse” nunca ha sido parte de su vocabulario, y tal vez siente como si no debiera de ser parte del vocabulario de nadie."

hi "Probablemente lo mejor es dejarla sola esta noche."

show emicas angry_up_close
with charachange

emi "¿Qué? ¿Eres un experto en Rin ahora?"

"Ella toma una posición firme y pone sus manos sobre sus caderas de modo confrontacional."

"Es como si quisiera pelearse conmigo también."

hi "No, no creo que eso siquiera sea posible en primer lugar."

hi "Es solo que no creo que patearle el trasero le haga algún bien."

show emicas frown_close
with charachange

"Mi melancólica observación sorpresivamente funciona, y Emi deja caer sus hombros un poco y suspira."

emi "Lo sé."

hi "¿En serio?"

stop music fadeout 2.0

show emicas awayfrown_close
with charachange

emi "La última vez que hice eso no cambió nada."

stop ambient fadeout 1.0

scene ev busride_ni
with locationskip

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")
play ambient sfx_businterior fadein 2.0

"El viaje de regreso a la escuela en un autobús vacío en medianoche es callado."

"Ambos nos quedamos viendo las luces brillantes pasar frente a la ventana sin decir una palabra."

stop ambient fadeout 1.0

scene bg school_dormext_full_ni
with locationskip

play music music_soothing fadein 0.5

"El campus nocturno está en silencio, iluminado solo por la pálida luna y postes de luz amarillos."

"Nos decimos buenas noches frente a mi dormitorio."

show emicas awayfrown_up_ni at center
with charaenter

"Emi aprieta sus puños por reflejo y me obliga a asegurarme de que no atacará a Rin en el momento en que la pierda de vista."

hi "¿Me prometes no ir a regañarla?"

show emicas angry_up_ni
with charachange

"Ella me ve, sus ojos ardiendo con ira que igualo con una mirada tan tranquilizadora como pueda."

"Solo es fácil enfrentar a una mujer enojada cuando no eres tú el blanco de su ira."

"Después de un minuto de la dispareja competencia de miradas, ella suspira y agita la cabeza, derrotada."

show emicas closedsmile_ni
with charachange

emi "Eres demasiado amable, Hisao."

show emicas weaksmile_ni
with charachange

emi "¿Sabías eso?"

"Los indicios de una sonrisa tiran de las comisuras de su boca mientras dice eso, y se ve mucho más relajada."

"Qué cambio de humor tan repentino."

"Tal vez no estaba tan enojada como parecía en un principio."

"Tal vez su humor cambia con facilidad."

hi "Si lo fuera, te hubiera dejado hacer lo que quisieras."

show emicas wink_ni
with charachange

emi "¿Eso significa que solo eres amable con Rin?"

"Ambos escondemos nuestra preocupación detrás de bromas vacías, pero por lo menos me pone de buen humor."

"Emi menea sus cejas con una sonrisa ligeramente burlona, tratando de hacerme reaccionar. No funcionará."

hi "No, solo significa que no soy amable solo contigo."

show emicas angry_up_ni
with charachange

emi "¡OYE!"

stop music fadeout 2.0

hi "Buenas noches, Emi."

scene black
with dissolve


label es_R33:

play music music_daily fadein 0.5

scene bg school_scienceroom
with locationchange

"El último día antes de las vacaciones de verano está terminando poco a poco."

"El examen final del trimestre es el de Ciencias y entonces estamos libres."

"El anhelo colectivo de la libertad es casi palpable en este salón de clases, aun si el tiempo es un poco nublado."

"Puede que llueva hoy, quién sabe."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene ev rin_doodle
with locationchange

"Ya he terminado el examen porque era bastante fácil, así que estoy garabateando con flojera en la parte de atrás de la hoja, esperando a que Mutou diga que se terminó el tiempo."

"También previene que Misha trate de mirar disimuladamente mis respuestas por sobre mi hombro."

"Puede que engañe al maestro distraído, pero puedo darme cuenta de que está tratando de ver."

"Supongo que es su mejor apuesta para pasar la prueba. Sin embargo no me hace sentir nada de piedad, así que solo la ignoro y miro a mi alrededor."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

scene bg school_scienceroom
with locationskip

"Es silencioso."

"Los únicos sonidos en el salón de clases son el callado barajar de hojas y la constante tos de Mutou."

"Hace que la percepción de mi entorno lentamente se desplace al fondo de mi consciencia, dándole espacio a otras cosas."






label es_R34:
scene bg school_scienceroom
with None

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\nVacaciones, ¿eh?"

n "Algunos se quedarán en la escuela aun durante las vacaciones, otros volverán con sus familias."

n "Yo no sé qué hacer. Debería ir a comprar un boleto de tren para mi viaje a casa, pero simplemente no me dan ganas de hacerlo."

n "Apuesto a que recibiré una llamada de casa otra vez. Mi mamá me molestará con cuándo voy a volver, y no voy a saber qué responder."

n "\nEsto realmente apesta. En el estado actual del asunto con Rin, se siente como si simplemente no me pueda largar de aquí y pretender que terminamos."

n "\nY ahora, ella tiene otros problemas suyos. Pensé que la apertura de la exhibición le daría un descanso, pero estaba muy equivocado."

n "\n\nEl enredo tan solo parece hacerse más grande."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

play sound sfx_doorknock

window show

"Un llamado fuerte a la puerta interrumpe el ánimo silencioso pero frenético de los últimos 15 minutos del examen."

show muto normal at center
with charaenter

$ renpy.music.set_volume(0.2, 0.0, channel="sound")

mu "Pase."

stop music fadeout 1.0
$ renpy.music.set_volume(1.0, 8.0, channel="sound")
play sound sfx_footsteps_hard

show bg school_scienceroom at bgleft
show muto normal at twoleft
with charamove

show nomiya serious at tworight
with charaenter

"La puerta que se abre revela al maestro de arte, quien entra con su chaqueta arremolinándose en torno a él como si estuviese en una ráfaga de viento."

"Le echa una mirada a Mutou, quien lo mira de vuelta."

play music music_tension

show muto irritated
show nomiya stern
with charachange

"El ceño se frunce simultáneamente en ambos rostros mientras los hombres se miden el uno al otro con sus miradas."

no "Discúlpeme, ¿podría llevarme al señor Nakai por un momento?"

mu "Discúlpeme a {b}mí{/b}, señor Nomiya, pero estamos en la mitad de un examen."

"Un ambiente frío súbitamente se propaga a media tarde de verano a medida que los dos hombres siguen observándose fijamente."

show nomiya serious
with charachange

no "Esto es urgente, y parece que Nakai ya ha terminado."

"Los dos voltean a verme, mirándome como un par de basiliscos tratando de petrificar un sabroso bocadillo."

"Es cierto que no he estado haciendo nada por un buen tiempo, así que Nomiya está en lo correcto, pero…"

show muto normal
with charachange

mu "Nakai, ¿te gustaría revisar tus respuestas una vez más?"

"Mutou habla con una extraña entonación, dándole peso a ciertas palabras como si tratara de mandar un mensaje."

"La presión de sus miradas me hace sacudir rápidamente la cabeza, lo cual es interpretado como una respuesta de algún tipo."

stop music fadeout 6.0

show muto irritated
with charachange

mu "Muy bien. Nakai, ve con el señor Nomiya, por favor."

mu "Llévate tu mochila y trae las hojas de tu examen a mi escritorio."

show muto smile
with charachange

mu "Que tengas felices vacaciones."

hi "Ahhh. Eh, igualmente, maestro."

"El mundo entero… bueno, al menos el grupo parece mantener el aliento solo para mí, suspendiendo el examen hasta que me ponga de pie, recoja mis cosas y camine fuera de la puerta."

"Puedo sentir las miradas sobre mi nuca. Mis compañeros de clase probablemente piensan que me castigarán o algo así, en el último día de escuela antes de las vacaciones de verano."

"No sé qué quiere el maestro de mí, pero puedo imaginar que posiblemente no es un castigo y también que posiblemente tiene algo que ver con Rin otra vez."

scene bg school_hallway3
with locationchange

play sound sfx_doorslam
with vpunch

"Nomiya no me lleva a ningún lugar, conformándose con el pasillo ya que está completamente abandonado."

show nomiya serious at center
with charaenter

play music music_pearly fadein 1.0

no "¿Sabes dónde está Tezuka?"

"Así que ella está tratando de evitar al maestro… como es de costumbre, probablemente."

"Me pregunto si se da cuenta de que no puede evitar enfrentarse con esto indefinidamente."

hi "No tengo idea."

hi "Quizás ya haya preguntado por ella en su grupo en la puerta de enseguida."

show nomiya stern
with charachange

no "¡Por supuesto que lo he hecho! He buscado en todos los rincones de esta maldita escuela y en el dormitorio de chicas."

no "Eres el último que la vio desde ayer y eres su amigo."

show nomiya serious
with charachange

no "Échame la mano. ¿Que no estás preocupado?"

"Lo estoy, pero no sé qué podría hacer."

"Rin hizo algo incomprensible anoche, incluso para ella."

"Se veía muy confundida."

hi "Tal vez solo quiere algo de tiempo para pensar. Tuve la sensación de que ella estaba dudando de tener esa exhibición."

"O algo así. Realmente no explicó qué era lo que ocurría."

show nomiya frown
with charachange

no "¿Dudando de qué?"

hi "No lo sé. Solo tuve esa sensación."

"Estoy siendo un poco deshonesto con el maestro, pero esto no es algo en lo que me debería de estar entrometiendo."

"Él vino hacia mí… sí, ¿por qué? Quizás piense que soy como alguien de confianza para Rin, pero no creo que pueda ayudar en este asunto."

show nomiya serious
with charachange

"El maestro resopla y se rasca la cabeza en confusión."

no "¿Qué pasa con esa niña? Esto no es como ella, siempre ha sido tan determinada."

"¿“Determinada”? Esa realmente no me parece una palabra con la cual describir a Rin."

"Para mí, ella siempre dio la sensación de ser obsesiva como mínimo."

hi "Eh, no quiero ser grosero, ¿pero no fue usted quien empujó a Rin en esa dirección en primer lugar?"

show nomiya dreamy
with charachange

no "Su meta es mi meta. Ese es el trabajo de un mentor."

hi "Supongo. Es solo que no sé si pintar puede hacerla feliz."

show nomiya stern
with charachange

no "Tú diciendo eso es bastante absurdo, Nakai."

"Repentinamente suena bastante furioso. ¿Dije algo estúpido?"

show nomiya serious
with charachange

no "Tú no entiendes, ¿verdad? No es una cuestión de felicidad. Por cada victoria hay un sacrificio por hacerse."

show nomiya stern
with charachange

no "No puedes tener algo a cambio de nada, pero acaso yo podría… ¿dejaría a esa chica desperdiciar su talento si tiene un momento de incertidumbre? ¡Nunca!"

no "Pintar es un trabajo como cualquier otro. Tezuka puede hacerlo parecer como un juego de niños para ti, pero ella trabaja duro cada día para hacer su arte."

no "Para ser extraordinario, uno tiene que hacer un esfuerzo extraordinario."

"Mientras más habla el maestro, más pienso que Rin no piensa de ese modo, aun si no tengo idea de cómo piensa ella."

show nomiya serious
with charachange

no "Puedo entender muy bien por qué sacrificaría sus vacaciones de verano y repondría las clases perdidas y los exámenes para tener una oportunidad de mostrar su arte."

no "Este es el camino que ella ha tomado, y seguirlo hasta el final, no es fácil."

no "Sé que es joven, y es difícil para ella al igual que lo es para todos los muchachos en esta escuela, pero eso no es excusa."

"Ya ha terminado."

hi "Pero—"

show nomiya smile
with charachange

no "¿Tienes algo tuyo como el arte es para Tezuka?"

hi "No…"

"Es cierto. Tan solo tengo vagas ideas sobre mi futuro, no hay una meta a la cual llegar, ni un sueño por tratar de alcanzar ciegamente."

"Me uní al club de arte en busca de algo en lo que podría estar interesado, para inspirarme."

"¿Encontré algo como eso?"

"Al final todo lo que encontré… fue a Rin."

hi "No, no tengo una pasión como esa."

show nomiya serious
with charachange

no "Entonces no puedes entender."

"Su llana declaración no permite argumento en contra."

hi "Pero… puede que ni ella misma entienda."

"Aun así, sigo discutiendo, por despecho si no es por algo más."

show nomiya stern
with charachange

no "¿Cómo podría no entenderlo? Ha estado trabajando tan duro por las últimas semanas que pospuso incluso venir a la escuela, eso sin mencionar asistir a clases. No digas ridiculeces."

"No pienso que esté diciendo ridiculeces, pero como no tengo modo de rebatir, Nomiya parece considerar esto como su victoria."

show nomiya smile
with charachange

no "Sea como sea, la apertura fue todo un éxito a pesar de que Tezuka apenas se haya mostrado."

no "Muchas personas estaban interesadas en su trabajo y una pieza incluso se vendió a un precio razonable."

hi "Bueno, eso está bien, ¿no es así?"

show nomiya veryhappy
with charachange

no "Sí, ¡son noticias fantásticas! Esperaba que Tezuka recobrara la cordura al escuchar sobre esto, pero…"

"Suspira y se quita los anteojos, limpiándolos con su chaqueta antes de ponérselos de vuelta sobre su nariz."

show nomiya smile
with charachange

no "De cualquier modo, debo marcharme. Está este desastre por arreglarse con Sae y todos los demás."

no "Si ves a Tezuka, por favor dile que venga a verme. De otro modo, que tengas felices vacaciones."

hi "Gracias…"

stop music fadeout 6.0
play sound sfx_footsteps_hard
$ renpy.music.set_volume(0.0, 4.0, channel="sound")

hide nomiya
with charaexit

"Después de que ha desaparecido a la vuelta de la esquina, reflexiono en dónde podría estar Rin realmente."

"Siento como si no tuviera solo uno, sino por lo menos media docena de estos “lugares secretos”."

"Sopeso entre el deseo de resolver este enredo y de dejarlo por la paz."

"El salón desocupado está a solo unos pasos de distancia."

"¿Qué hacer?"

"…"

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_dooropen

scene bg school_room34
with locationchange

"Cuando abro la puerta, solo me reciben las sombras del interior."

hi "Qué tal."



label es_R35:

scene bg school_scienceroom
with None

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\nVacaciones, ¿eh?"

n "Algunos se quedarán en la escuela aun durante las vacaciones, otros volverán con sus familias."

n "Probablemente debería de hacer el viaje de regreso a casa y reportarle a mis padres que estoy vivo y sano."

n "\nNo hay mucho que hacer en la escuela de todos modos, supongo."

n "El siguiente trimestre será estresante. Todos tendrán que pensar seriamente en qué hacer después de graduarse."

n "\n\nIncluyéndome a mí…"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

scene ev rin_doodle_all
with silentwhiteout

window show

"Una mirada a mis garabatos me convence de dejar de tratar de salvaguardarlos. Es un desastre de líneas sin vida, un desperdicio de papel si no fuese la parte de atrás de mi examen."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\n\nTal vez porque no me propuse dibujar algo en particular."

n "Tan solo quería matar un poco de tiempo, así que el dibujo se convirtió en exactamente lo que soy."

n "Sin una dirección adónde ir."

n "\n\nSería más fácil si tuviera algún talento especial, como Rin."

n "Lo tiene fácil."

n "Me pone un poco celoso."

n "Me da rabia que ella misma parece no poder estar contenta de ello."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

scene bg school_scienceroom
show muto smile at center
with locationskip

window show

mu "Yyyy… ¡tiempo!"

"El llamado de Mutou para el fin del examen extrae gemidos de descontento de la mitad del grupo."

"No los culpo, el examen era algo difícil."

"Mutou espera mucho de mi grupo, aun si no es para nada estricto. Supongo que le gustaría que todos nosotros fuésemos científicos."

show muto normal
with charachange

mu "Dejen sus lápices y entreguen sus hojas, por favor."

"El quejido más grande viene del banco a mi lado."

show misha invis_close:
    center
    xpos -0.2
    ypos 1.13
with None

show bg school_scienceroom at bgright
show muto normal at tworight
show misha perky_sad_close:
    xpos 0.15
with dissolvecharamove

"La desesperanza de Misha es casi tangible."

"La oscura aura de ilusiones perdidas emanando de su asiento me hace sentir simultáneamente miedo y compasión por ella."

show muto smile
with charachange

mu "Y bien, debería haber una sesión de aula antes de que estén libres, pero solo tengo unos anuncios que hacer así que esto debería de acabar rápido…"

"Sus anuncios nunca son importantes, así que solo lo escucho con un oído."

"Misha parece estar demasiado deprimida como para siquiera pretender prestar atención."

"Deja caer su cabeza contra el escritorio, viéndose afligida."

hi "Alégrate, Misha."

hi "¡Son vacaciones! No te preocupes por el examen."

show misha sign_smile_close
with charachange

mi "Gracias, Hicchan."

"Su mohín se convierte en una pequeña sonrisa, y una chispa de entusiasmo ilumina sus ojos."

show misha perky_smile_close
with charachange

mi "¿Qué vas a hacer en tus vacaciones de verano, Hicchan?"

show misha hips_smile_close
with charachange

mi "Yo voy a ir a la casa de Shicchan, ¡tienen esta mansión asombrosa y supergenial! ¡Estoy tan emocionada~!"

show misha hips_grin_close
with charachange

mi "¡Estoy segura de que serán las más mejores vacaciones de todas~!"

"Parece haber olvidado todo sobre su miseria en unos cuantos segundos y rebota de arriba a abajo en su asiento como si inflara su emoción."

hi "En realidad no tengo ningún plan, supongo…"

show misha sign_smile_close
with charachange

mi "¿Es en serio~? Tal vez deberías—"

show misha perky_confused_close
with charachange

"Un dedo golpeteando su hombro roba la atención de Misha en mí."

show muto irritated
with charachange

"Shizune apunta a Mutou, quien está mirándolas a las dos con expectación."

show misha sign_confused_close
with charachange

mi "¡Ups! Perdón, Shicchan, no me di cuenta de que el maestro ya había terminado, ejeje~."

"Ella aclara su garganta y toma aire con profundidad…"

show misha hips_grin_close:
    ypos 1.0
with dissolvecharamove

mi "¡De pie!"

"Me pongo de pie con todos los demás."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\nDesde que vine aquí, siempre me he preguntado algo."

n "¿Qué piensan los estudiantes en sillas de ruedas sobre esta tradición, siendo incapaces de seguirla “apropiadamente”?"

n "¿Es un tropiezo mantener esta tradición en un lugar que evita muchas otras por conveniencia?"

n "Aunque nunca le pregunté a nadie, durante estas cortas semanas aquí he llegado a la conclusión de que ellos definitivamente no se sienten insultados."

n "Ellos entienden."

n "Eso es lo que me gusta de esta escuela. Nadie es demasiado estirado sobre algo, todos son tan… considerados y comprensibles con los demás."

stop music fadeout 4.0

n "\n\nDesearía que el mundo entero fuera así."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

scene black
with locationchange

window show

mi "¡Reevereeenciaaa!"

scene bg school_dormhisao
with shorttimeskip

play sound sfx_paper
play music music_tranquil fadein 3.0

"Le doy vuelta a la página con lentitud, escuchando el crujir que el papel hace cuando mis dedos la sujetan."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\nMe siento inquieto."

n "Son las vacaciones de verano."

n "No hay clases, ni tareas, ni reuniones del club de arte. Solo tiempo libre para pasar como me dé la gana."

n "No se siente como nada."

n "Traté de animar a Misha, pero yo mismo no me siento muy animado."

n "Para ser honesto, el tiempo libre es intimidante. Me recuerda al hospital y los largos días sin sentido que tenían que ser llenados de algún modo."

n "La única diferencia es que allá estaba atado al ala del hospital, vigilado por enfermeras que parecían Cerberos."

n "Leer fue una buena solución en ese entonces, pero el pensar en pasar mis vacaciones de verano leyendo se siente… ñoño."

n "Eso no tiene nada que ver con el hecho de que estoy leyendo incluso ahora… Solo estoy matando el tiempo y tratando de vencer mi ansiedad."

n "Además, mi mente está en otros asuntos, estirándose en demasiadas direcciones como para encontrarle sentido a alguno de ellos."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

window show

"Por ende, el libro con el que he estado desde el martes va progresando l{w=0.3}e{w=0.3}n{w=0.3}t{w=0.3}o{w=0.3}."

"Se siente como si este libro me estuviese tomando más tiempo de leer que el que le tomó al autor escribirlo."

"Intento dejarlo por un rato, luego volver a leer un poco, empezar todo desde el principio, leer cada página dos veces."

"Nada funciona, tengo cero concentración."

"Llevándolo conmigo solo por si acaso, me dirijo hacia afuera para tomar un poco de aire fresco e inspiración en cuanto a qué hacer."

scene bg school_courtyard
with locationskip

"Me dirijo al patio, pasando frente a estudiantes que van al portón."

"Los más apresurados se van ya a sus casas, juzgando por las maletas que algunos arrastran consigo."

"Supongo que no importa cuán hospitalario sea Yamaku, el hogar sigue siendo el hogar. Aun así, escuché que algunos se quedarán durante las vacaciones."

"El patio es lo suficientemente grande como para que su centro esté sin sombra sin importar qué tan alto o bajo se encuentre el sol."

"Me detengo en la mitad y disfruto de la calidez."

"El brillo me hace entrecerrar los ojos cuando veo hacia el edificio principal."

"Parece ya estar abandonado por completo."

"Yuuko no estaba en el trabajo hoy, así que la siguiente vez que pueda sacar libros de la biblioteca es después de las vacaciones."

"Hay una biblioteca pública en alguna parte, estoy seguro, pero me siento demasiado aletargado como para averiguar dónde está."

scene bg school_lobby
with locationskip

"El vestíbulo está igualmente carente de vida así que tengo que conformarme con regresar a los dormitorios, terminando mi paseo antes de lo que esperaba."

"Por otro lado, no estaba muy seguro de qué estaba esperando en primer lugar."

scene bg school_girlsdormhall
with locationskip

"En un impulso del momento entro al dormitorio de chicas para ver si Rin o Emi están ahí."


"Ninguna está, así que regreso a mi propia habitación para estar en mi letargo."

window hide

scene bg school_dormhisao
with locationskip

$ renpy.music.set_volume(0.5, 1.0, channel="music")

nvl clear
nvl show dissolve

n "\n\nTengo que hablar a fondo con Rin."

n "Ella en verdad me molesta."

n "\n\nDesafiando el equivalente conceptual de la gravedad, ella se balancea sobre la delgada línea que zigzaguea entre la locura, lo incomprensible y la inestabilidad."

n "Rin me afecta también. Me reta en maneras que yo no sabía… o más correctamente, no esperaba que existieran."

n "\n\nHe comenzado a preguntarme si estos sentimientos son realmente amor, o si estaba engañándome a mí mismo."

n "Seguramente, ¿sería una locura considerar eso?"

nvl clear

n "\n\nPor el resto del día, Rin, el hospital, Yamaku y las vacaciones se arremolinan por mi cabeza."

n "\nNo puedo concentrarme ni en concentrarme."

n "\nLos pensamientos parecen ir y venir sin orden ni concierto, fragmentados en pedazos de cognición demasiado pequeños."

n "\nLevanto el libro y logro leer cien páginas, pero estoy seguro de que para mañana no tendré memoria de qué sucedió en la historia."

n "\nTrato de limpiar mi cuarto, pero incluso eso resulta ser demasiado molesto, consumiendo demasiado tiempo y requiriendo demasiada atención al detalle."

n "Usualmente es así. Cuando no tienes “nada que hacer”, no haces nada incluso si pudieras."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

scene bg school_dormhisao_blurred_ss
show phone mobile at center
with shorttimeskip

window show

"Como es de esperarse, mi mamá llama y termino prometiéndole que veré si puedo conseguir un boleto de tren para mañana, o de no poder, para el día siguiente."

window hide
nvl clear

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

$ renpy.music.set_volume(0.5, 1.0, channel="music")

nvl show dissolve

n "\n\nQuizás vaya mañana al centro de todos modos. Podría hacer un poco de compras o algo así."

n "No es que necesite algo, pero tal vez haya ventas de verano, y podría conseguir… algo."

stop music fadeout 10.0

n "\n\n…¿Por qué estoy tratando de forzarme a mí mismo?"

n "Antes, estaba conforme sin tener nada que hacer, aparte de patear la pelota de vez en cuando en el campo."

n "Ahora parece que no puedo calmarme en absoluto."

n "\n¿Acaso es porque he cambiado, o porque mi mundo ha cambiado?"

nvl hide dissolve
nvl clear

scene bg school_dormhisao_ni
with shorttimeskip

window show

"A las once, la oscuridad me manda a dormir."

window hide

show pills:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

window show

"Los frascos con medicamentos están acomodados de manera inocua sobre mi mesa de noche, para nada llamativos, más bien recordándome puntualmente la realidad."

"Es de noche…"
"Tengo que abrir tres frascos, extraer una grande de forma ovalada, dos pequeñas redondas y una grande y plana que tiene que ser cortada a la mitad, cerrar los frascos y pasar los medicamentos con un trago de fresca agua del grifo."

window hide

show pills:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide pills
with None

window show

"El agua tiene sabor metálico en mi lengua."

"La trago junto con las píldoras de todos modos y me dirijo al baño."

scene bg school_dormbathroom
with locationskip

"La tarea mecánica de cepillarme los dientes es apropiada para tratar de organizar mis pensamientos."

"Uno emerge de la masa, claramente levantándose sobre los demás."

window hide
nvl clear
nvl show dissolve

n "\n\n\n\n\n\n\n\n\nQuiero ver a Rin."

n "No puedo dejar que mi explosión de enojo sea lo último entre nosotros antes de las vacaciones."

nvl hide dissolve
nvl clear

scene bg school_dormhisao_ni
with locationskip

nvl show dissolve

n "\n\n\n\n\n\n\n\nTengo que verla, mañana."

n "El sueño vence mi mente confundida con más facilidad de la que debería."

nvl hide dissolve
nvl clear

$ suppress_window_before_timeskip = True

scene black
with shuteye


label es_R36:


$ renpy.music.set_volume(1.0, 0.0, channel="music")
$ renpy.music.set_volume(0.7, 0.0, channel="ambient")
play ambient sfx_rain fadein 1.0

scene bg misc_sky_rn
show rain normal
show hisaowindow
with locationchange

"Lluvia cae sobre mis vacaciones de verano como un incontable número de pequeños malos augurios."

"Por suerte no soy supersticioso, pero el mal tiempo me hace sentir apesadumbrado, también."

"Ha sido así desde la mañana y no se le ve el fin."

"Una impenetrable masa gris de nubes ensombrece el cielo tanto como ensombrece mi ánimo."

"En un arranque de despecho, terminé de limpiar esta mañana, pero después de que eso estuviese hecho me quedé mirando fuera de la ventana con esperanzas de que el tiempo clareara."

"El tamborileo incesante de las gotas de lluvia contra el tejado y el pavimento es hipnotizante, un zumbido como ruido de fondo en el cual perder tu mente."

"…"

"… …"

$ renpy.music.set_volume(0.4, 1.0, channel="ambient")

scene bg school_dormhisao_rn
with locationchange

"Esto no servirá, tengo que moverme."

"¿Debería empacar ahora o más tarde?"

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")

scene bg school_dormhallway
with locationchange

"Me decido por la segunda y me dirijo hacia afuera, haciendo una pausa breve frente a la puerta de Kenji para escuchar al extraño sonido de golpes sordos desde el otro lado de la puerta."

show rain normal behind bg
with None

"No me atrevo a tocar, por miedo de descubrir qué es lo que está haciendo."

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

show bg school_dormext_full_rn as bg2 behind rain
hide bg
with locationskip

"Enfrentándome a la lluvia desde debajo de un confiable paraguas, cruzo el espacio hacia el dormitorio de chicas."

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")

scene bg school_girlsdormhall
with locationskip

play sound sfx_doorknock2

"Llamar a la puerta de Rin no da respuesta, pero la puerta detrás de mí se abre en su lugar."

play sound sfx_dooropen

show emicas invis:
    center
    xpos 0.3
with None

show emicas happy at center
with dissolvecharamove

play music music_emi fadein 0.5

emi "¿Hisao? ¡Qué tal!"

show emicas awayfrown
with charachange

emi "Un tiempo terrible. Hasta me perdí mi trote matutino."

"Frunce el entrecejo, pero estaría contento si fuese ella. Los trotes matutinos de Emi son cualquier cosa menos relajados."

hi "Oh, qué tal, estaba—"

show emicas neutral
with charachange

emi "Si estás buscando a Rin, no creo que esté ahí."

hi "¿La has visto recientemente?"

show emicas grin_up
with charachange

emi "Sí, apenas esta mañana cuando la desperté."

"La mención de despertar hace a Emi bostezar como un gato, y me hace sentir tonto."

"Por supuesto que ha visto a Rin. Emi la despierta y la ayuda a vestirse en la mayoría de las mañanas, incluso hace sus almuerzos de vez en cuando."

"Ellas son como hermanas, aunque no parecen tener nada en común."


label es_R36a:

"¿Me pregunto quién será la hermana mayor? Probablemente Emi, contra toda posibilidad."

"Ella es bastante diligente, aun si da la impresión de ser alguien que sería toda una cabeza hueca."

"¿Por qué se siente tan extraño que ella sea tan solícita bajo esa sonrisa alegre suya?"



label es_R36x:

show emicas frown_up
with charachange

emi "Se fue a la galería hace algunas horas… oye, ¿estás escuchando?"

"Tal vez estoy haciendo una cara graciosa o algo así, ya que Emi ladea la cara con curiosidad, mirándome con sus ojos redondos e inquisitivos."

show emicas neutral
with charachange

emi "¿Hmm?"

"Su inocente rostro parece pedir mi atención."

hi "Sí, estoy escuchando."

show emicas weaksmile
with charachange

emi "¿Puedo hacerte una pregunta?"

hi "Sí, claro."

show emicas awayfrown
with charachange

"Ella frunce el ceño y se lame los labios como si se preparara para algo."

show emicas frown
with charachange

emi "¿Por qué te preocupas tanto por Rin?"

show emicas neutral
with charachange

emi "Digo, tú probablemente te juntas con ella más que yo, y nosotras incluso dormimos en la misma cama algunas veces hasta, bueno, recientemente."

hi "¿Hasta que te expulsó porque devastaste su cabello?"

show emicas blush
with charachange

"Un choque de horror ensancha los ojos de Emi por lo menos al doble, haciéndolos ver aún más como platillos que lo usual, mientras un saludable rubor se alza en sus mejillas y orejas."

show emicas angry_up
with charachange


emi "¡¿Te dijo?! Ohhh… Voy a estrangular a esa Rin o algo otro horrible…"


"Contengo mi risa, no sea que dirija su desdén hacia mí."

show emicas closedsmile
with charachange

"Emi se recupera rápidamente de su vergüenza y parece perdonar a Rin al mismo instante, poniendo su atención de vuelta sobre mí."

show emicas smile
with charachange

emi "De cualquier modo, ¿estás enamorado de ella o algo?"

"Oh oh. Esto realmente se siente como una hermana mayor interrogando a un pretendiente. Emi es un tanto entrometida, y no de una manera buena y alegre, si es que siquiera haya una para empezar."

"Ella haría una buena pareja con Misha, para ser honesto. Qué horror."

hi "Esa ya es tu segunda pregunta, así que no creo que tenga que responder."

"Trato de conjurar una fachada hecha de pura y cristalizada frialdad y carencia de implicación."

"Me pregunto si siquiera logro engañarme a mí mismo."

show emicas evil
with charachange

"Por lo menos Emi está meneando sus cejas con peligrosidad, con una desagradable sonrisa en sus labios."

emi "¿Es eso un sí?"

hi "No, no es un sí."

show emicas neutral
with charachange

"Obviamente insatisfecha con mi rechazo a responder su pregunta demasiado íntima, ella tiene la suficiente sensatez de retroceder."

show emicas wink
with charachange

"No la detiene de sacarme la lengua como un niño, y reír de nuevo."

show emicas closedsmile
with charachange

emi "Si esa es tu respuesta, no creo que tenga que hablar más contigo."

"Es fácil ver que ella en realidad no está enojada."

show emicas happy
with charachange

emi "Además, tengo que ir a empacar. Mi mamá estará preocupada si pierdo el autobús."

emi "¡Nos vemos!"

hi "Sí, hasta luego."

stop music fadeout 4.0

hide emicas
with charaexit

play sound sfx_doorclose

"Ella se retira a su habitación, dejándome solo en el pasillo."

"Lo que hay entre Rin y yo no es asunto suyo, ¿cierto?"

"Es por eso que terminé sin decirle nada a Emi sobre nuestra pelea. Rin tampoco debe de haber dicho algo."

"Supongo que… aun siendo amigas, hay cosas de las que no hablan."

"…"

"Y bien, si Rin está en la galería, tendré que ir hasta allá."

"Ahora que logré salir de mi habitación, supongo que no es tanta molestia ir al centro."

"Podría ir por un boleto, pero el tren de regreso a casa tendrá que esperar, al menos hasta mañana."

show rain normal behind bg
with None

"De ninguna manera voy a cargar equipaje a la estación de tren en esta lluvia, aun si no es mucho."

$ renpy.music.set_volume(1.0, 3.0, channel="ambient")

show bg city_street4_rn as bg2 behind rain
hide bg
with shorttimeskip

"La lluvia hace todos los contornos parecer muy inestables, como si se estuviesen desvaneciendo."

"El paisaje urbano se torna una colección sin forma de varios tonos borrosos de gris, en lugar de formas distintas de edificios y autos."

"Esas pobres almas forzadas a estar en el diluvio tratan de apresurarse tanto como les sea posible, compadeciéndose mutuamente por su miseria compartida."

show bg gallery_ext_rn as bg2
with locationchange

"Doy vuelta en la última esquina, la vigésima segunda por así decirlo, e inmediatamente me siento estúpido por divertirme con mi propio juego de palabras."

"La puerta me atrae con promesas de calor."

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")
play sound sfx_storebell
play music music_soothing fadein 0.5

scene bg gallery_int
with locationchange

"El agua de lluvia goteando de mi paraguas hace interesantes y casi artísticos patrones sobre el suelo."

"No estoy mojado, aparte de mis zapatos que dejan pequeños charcos detrás de mí, completando el arte en agua de lluvia."

show nomiya smile at twoleft
show sae neutral at tworight
with charaenter

"Nomiya también está aquí, charlando con Sae al fondo de la galería. Sin embargo, Rin no se encuentra en ningún lado."

"Quizás esté arriba."

"Aunque no hay clientes, lo cual es de esperarse, considerando los cubetazos de agua cayendo en el cuello de quienquiera que se atreva a enfrentar al clima en este día."

show sae smile
with charachange

sa "Bienvenido."

hi "Hola. Perdón por interrumpir…"

show nomiya talk
with charachange

no "Ah, buenas tardes Nakai."

show nomiya smile
with charachange

no "¿Viniste hasta acá para visitar?"

hi "Ah… no, creo que fue solo un impulso. Estaba por el vecindario, de compras, y decidí pasar por aquí."

"Mi reacción de reflejo es una mentira blanca, lo cual me sorprende."

"Tal vez solo no quiero decir que vine específicamente para ver a Rin, aun si eso debe de ser obvio."

show sae doubt
with charachange

sa "Vaya, escogiste un mal día para ir de compras. ¿Gustarías una taza de té para calentarte?"

hi "Gracias, estoy bien, en serio."

hi "Aunque el tiempo podría ser mejor. Lluvia en el primer día de vacaciones es un poco deprimente."

show nomiya veryhappy
show sae neutral
with charachange

no "¡Jajaja! Bueno, estoy seguro de que mejorará."

"Nomiya ofrece su afable carcajada, lindando en lo abrasivo."

hi "La lluvia no lo pone de malas, ¿maestro?"

show nomiya smile
with charachange

no "Bueno, yo también prefiero buen tiempo. De hecho estaba a punto de irme para reunirme con alguien, y preferiría no mojar mi chaqueta. Es bastante cara."

show nomiya talk
with charachange

no "¡Pero por supuesto que estoy de buen humor!"

show nomiya smile
with charachange

no "¿Qué pensaste de la exhibición? Fue maravillosa, ¿no es así?"

hi "Sí, fue muy elegante."

"Mi respuesta sin entusiasmo solo lo incentiva a que continúe, caminando por la galería mientras parlotea sobre la apertura."

"Habla todavía más y con más fuerza cuando se mueve. Es algo que noté en las reuniones del club, también."

show nomiya veryhappy
with charachange

no "Logramos hablar con mucha gente buena y hacer contactos valiosos."

show nomiya smile
with charachange

no "Incluso una de las pinturas de Tezuka se vendió, a un coleccionista de Osaka."

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")

show rin_exhibition_sold at center
with locationchange

"Sigo sus ojos hacia un espacio vacío en la pared. Ni siquiera puedo recordar cuál pintura estaba colgando en ese lugar."

"Bueno, se ha ido."

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")

hide rin_exhibition_sold
show nomiya talk
with charachange

no "Fue una suerte que se encontrara bien a pesar de ese mareo."

show nomiya smile
with charachange

no "Aunque se puso un poco callada, así que le dije que descansara bien. Por otro lado ella siempre ha sido bastante tímida."

"¿Tímida? Como sea, simplemente asiento junto con el maestro."

show nomiya talktongue
with charachange

no "La recepción fue bastante positiva en general. Quizás pueda conseguir que uno de mis amigos escriba un articulito en una revista para—"

sa "Shinichi, tu reunión. Estás haciendo esperar al señor Takahashi."

show nomiya serious
with charachange

"El comentario de Sae lo hace detenerse en seco y revisar su reloj."

"Nomiya frunce el entrecejo en disgusto ante la interrupción de su diatriba."

show nomiya smile
with charachange

no "Oh, cierto. Sí, bueno, me retiraré entonces. Nos vemos en septiembre, Nakai."

hi "Hasta luego."

hide nomiya
with charaexit

play sound sfx_storebell
stop music fadeout 4.0

"Guau. El maestro en verdad no se contiene cuando se trata de la carrera de artista en ciernes de Rin."

"Creo que se necesita mucho para tener éxito, pero supongo que su trabajo sería más fácil si Rin fuera más cooperativa."

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\nElla es demasiado indecisa aun si lo está haciendo bien. Como ese “mareo” de la noche anterior."

n "Simplemente le entró pánico o algo así, y no hice nada para ayudarla."

n "\nSuspiro."

n "Se siente como si la brecha entre Rin y yo solo se estuviese ensanchando."

n "Ella se convertirá en algo grandioso mientras yo me sigo sintiendo atascado, a pesar de prometerme a mí mismo tratar de hacer algo de mi vida."

n "Además de eso, tuvimos esa pelea y mientras más tiempo pase sin que hablemos, más difíciles serán de curar esas heridas."

n "Si es que eso es lo que queremos. Nunca descubrí qué sentía Rin, y ahora no estoy seguro de qué siento yo."

n "Desearía poder entenderla. Pero Rin es muy abierta a la interpretación."

n "No es que ella esté ocultando algo, simplemente parece desafiar mis intentos de comprender de qué está hablando en un día cualquiera."

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")
$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

show sae smile
with charachange

window show

sa "¿Algo en mente?"

"Me percato de que me he quedado ido en medio de la galería por quién sabe cuánto tiempo."

hi "Ahh… nada en especial…"

"Pretendo estudiar la pintura más cercana para distraerla."

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
play music music_another fadein 0.5

scene rin_exhibition_c:
    truecenter
    zoom 1.0 subpixel True
    ease 30.0 zoom 1.1
with locationchange

"La he visto antes."

"Los ya muy familiares trazos de color, torciéndose y fundiéndose unos con otros aparentemente al azar todavía logran sentirse como si hubiera algo sucediendo detrás de escena, por así decirlo."

"El estilo de Rin es tan parecido a ella. Abstracto, incomprensible, colorido."

"Misterioso."

"¿Me pregunto si para entender a un artista, uno debe entender el arte?"

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")

scene bg gallery_int
with locationchange

hi "Ahh… puede que tenga una pregunta."

show sae smile at center
with charaenter

sa "¿Oh?"

"Ella levanta la vista de la revista que estaba hojeando distraídamente, aparentemente encantada con mi muestra de interés sin especificar."

hi "¿Cómo interpreta el arte?"

show sae doubt
with charachange

sa "¿De qué hablas?"

"Sus cejas se levantan alto formando arcos inquisitivos, como si la pregunta fuese demasiado complicada como para siquiera empezar a responderla sin clarificación."

hi "Perdón si estoy preguntando algo estúpido."

hi "No creo que realmente entienda el arte como los profesionales lo hacen."

show sae smile
with charachange

sa "Oh, no hay truco para ello."

"Sae descarta mi pregunta con un simple pero eficiente giro de muñeca."

show sae neutral
with charachange

sa "Cada uno interpreta el arte como gusta, y la interpretación depende tanto de quien lo mira como de las intenciones del creador."

sa "Los “profesionales” tienen su propia manera, porque existe esta cosa llamada teoría del arte."

sa "Hay patrones en el arte, al igual que en todo, y asumimos que es posible sacar algunas conclusiones al observar esos patrones."

"Su voz es como la de una maestra, dando una lección y añadiendo énfasis en palabras al azar para mantener a los oyentes atentos."

show sae smile
with charachange

sa "Al final, supongo que no tiene mucho sentido."

"Ella cambia a meditar aparentemente para sí misma, murmurando lo suficientemente fuerte como para que yo la escuche claramente."

sa "Una buena pieza de arte te hará sentir algo y eso es todo."

sa "Los sentimientos cambian y ellos afectan el arte que creamos y el arte que vemos."

hi "Pero…"

show sae neutral
with charachange

sa "Te contaré una historia."

hi "¿Tiene que hacerlo? La última fue deprimente…"

sa "Es importante. Escucha…"

sa "Hace alrededor de cien años a un pintor poco conocido le llegó la noticia de que su amigo, un hombre llamado Casagemas, se había suicidado."


sa "Esto había sucedido cuando él estaba fuera y no había visto a su amigo por un tiempo."

sa "Así que obviamente se debe de haber sentido aún más conflictuado de lo que normalmente te sentirías después de escuchar tal cosa."

sa "Por cuatro años después de eso, nuestro personaje principal no hizo nada más que pinturas monocromáticas porque había sido afectado tan profundamente por esas noticias."

sa "Cualquier cosa que hiciera, siempre regresaba a ese color hasta que este se desaferró de él."

"Ella hace una ligera pausa para revisar si todavía le sigo la pista."

"Sí lo hago, en cierta medida, así que le doy la señal para la que viven los cuentacuentos."

hi "Así que…"

"Es difícil continuar de ahí, ya que parezco no poder descubrir la pregunta que ella quiere que descubra."

"Como un Sócrates sin madurar, ella pensó que había puesto todas las herramientas para la revelación frente a mí."

show sae doubt
with charachange

sa "¿Todavía no ves el punto?"

"Solo que su estudiante probó ser demasiado bobo para entenderlo."

show sae scowl
with charachange

"Ella se ve descontenta con mi torpeza."

sa "El periodo azul de Picasso es uno de los más afamados en la historia del arte, pero, ¿quién sabe qué sintió cuando trabajó en esas obras maestras?"

sa "¿Tristeza? ¿Anhelo? ¿Arrepentimiento?"

sa "Nadie puede decirlo."

sa "Si ahora ves una de sus pinturas del periodo azul, probablemente la interpretes de manera diferente a antes de que supieras de Casagemas, el amigo de Picasso."

show sae neutral
with charachange

sa "Experimentar el arte es siempre personal, solo interactivo por casualidad o circunstancia."

sa "Hay millones de explicaciones para cualquier obra de arte, pero puede ser que ninguna de ellas sea lo que el creador quería."

show sae smile
with charachange

sa "Ningún hombre es una isla, ¿lo sabes?"

"Asiento sin entender qué significa ese último comentario."

"Lo que dijo tenía sentido de otro modo, excepto por una cosa."

"Si el arte es comunicación como Rin dijo, pero todos hablan su propio idioma secreto como dijo Sae, ¿cómo puede alguien tener la esperanza de comunicarse?"

"Se siente tan vano e inútil."

"El arte en verdad no es algo para mí."

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")

scene bg gallery_exhibition
with locationchange

"Sae regresa a su revista, y yo doy una vuelta por la galería, tratando de ver lo que Rin ve en sus propias pinturas."

"Un ambiente relajante se apodera de la galería rodeada por la tormenta, las grandes ventanas haciendo al transparente aislamiento sentirse más cómodo."

play sound sfx_storebell
stop music fadeout 2.0

"Un tintineo de la campana interrumpe el ambiente tranquilo."

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")

scene bg gallery_int
with locationchange

show rin relaxed_nonchalant at center
with charaenter

"Rin abre la puerta al empujarla con el hombro y da un paso adentro."

"Casi había olvidado que ella era la razón por la que vine a la galería en primer lugar."

show rin relaxed_boredom
with charachange

rin "Creo que estoy lista—{w=0.3}{nw}"

show rin relaxed_surprised
with charachange

"Ella se detiene a media palabra, percatándose de mi presencia."


"El silencio absoluto dura exactamente un segundo y medio, no lo suficiente como para que Sae o yo abramos la boca, pero suficiente para que Rin reaccione."

show rin negative_annoyed
with charachange

rin "Iré a dar un paseo."

hide rin
with charaexit

play sound sfx_storebell

"Yendo de vuelta hacia afuera con un paso imprudente inusual para ella, Rin parece olvidar que sigue lloviendo."

show rain normal behind bg

"Sin realmente pensarlo demasiado, tomo mi paraguas y me apresuro tras de ella."

play sound sfx_storebell
$ renpy.music.set_volume(1.0, 2.0, channel="ambient")

hide bg
show bg city_street4_rn as bg2 behind rain
show rin negative_spaciness_close_rn
with locationskip

"Alcanzo a Rin a la vuelta de la esquina, abro el paraguas y lo levanto por sobre nosotros dos sin dejar de tener que casi correr para seguirle el paso."

"Ella no protesta que corra detrás ni que le dé refugio contra la lluvia, finalmente disminuye el paso para que pueda igualarlo sin un riesgo inmediato de que me esfuerce demasiado."

"Me tranquilizo del apuro, evaluando la situación."

"La última vez que sostuve mi paraguas para protegernos a los dos de la lluvia, no pensé demasiado en ello."

"Pero ahora, todas las cosas que pasaron desde entonces se han juntado en una bola helada alrededor de mi estómago."

"Estar cerca de ella me hace sentir incómodo, y siento cómo me pongo ligeramente nervioso."

"Es difícil sacarme las palabras de la boca, ya que súbitamente se siente muy, muy seca."

"Aun así, no es como si pudiera echarme para atrás."

hi "¿Por qué sigues corriendo?"

show rin negative_annoyed_close_rn
with charachange

rin "No quiero hablar contigo."

hi "Yo quiero hablar contigo."

show rin negative_confused_close_rn
with charachange

rin "Me duele cada vez que lo hago."

hi "Algunas veces no hay más remedio."

show rin negative_sad_close_rn
with charachange

rin "No quiero sentir dolor."

hi "Está bien. No tenemos que hablar."

show rin relaxed_doubt_close_rn
with charachange

rin "¿Qué deberíamos hacer?"

hi "Solo sigamos caminando."

show rin relaxed_surprised_close_rn
with charachange

rin "¿Solo caminar?"

hi "Solo caminar."

show rin basic_absent_close_rn
with charachange

rin "Está bien."


label es_R37:

play music music_dreamy fadein 2.0
$ renpy.music.set_volume(1.0, 2.0, channel="ambient")
$ renpy.music.play(sfx_rain, fadein=2.0, if_changed=True, channel="ambient")

play sound sfx_whiteout

scene white
with Dissolve(1.0)

show rain normal behind white
with None

hide white
show ev rin_rain_away_close behind rain at Fullpan(20.0,dir="up")
with Dissolve(1.0)

"Nuestras pisadas hacen “splish splash” en los charcos poco profundos formándose en las calles a medida que caminamos por la lluvia."

"Rin, ahora caminando a mi lado en su manera tranquila y relajada, no parece estar ni un poco molesta por el hecho de que se está mojando aun si no tiene que hacerlo."

"Ella está parcialmente fuera del refugio protector de mi paraguas, a pesar de este ser más grande de lo necesario para los dos."

"Es como si ni siquiera notara la lluvia mojando su blusa."

"…"

"El comportamiento de Rin siempre evoca imágenes mentales de meditativa calma, aun cuando ella pudiera tener un conflicto interior."

"Pero no creo que eso sea meditación. Eso es solo estarse empapando en la lluvia."

"También desearía estar más tranquilo."

"Me he involucrado demasiado con Rin como para mantener mi usual distanciamiento."

"Se siente como si me hubiese vuelto una de esas personas que se engañan a sí mismas pensando que son objetivas, tan solo para darse cuenta de que son de la peor clase de mentirosos."

"Ilusiones para engañarnos, ¿qué mejor manera de hacer que uno se sienta como una mejor persona?"

"Tal vez sea mejor perder esa ilusión."

show ev rin_rain_away_close at Position(yalign=0.0)
show ovl rin_rain_hisaotowards_close behind rain at Position(xalign=1.0, yalign=0.0)
with charachange

hi "Iré de regreso a casa por un tiempo así que pensé en venir a verte antes de eso."

"Podría haber pensado en un mejor inicio de conversación, pero Rin negándose activamente a hablar lo hace más difícil."

rin "Eso es bueno. Podría haber pensado que habías sido raptado de otro modo."

hi "No puedes continuar escapando de todo. Ni siquiera de mí tratando de hablar seriamente."

rin "Siempre hablo en serio. Además parezco estar corriendo muy lentamente en este momento."

rin "Tal vez deba tomar lecciones con Emi."

"Es inútil. Como hablar con una pared de ladrillo que al azar te dice tonterías sarcásticas de vuelta."

hi "Piensa en la apertura de tu exhibición. ¿Qué tal si te hubieses escapado?"

"Rin no responde a eso, tan solo sigue caminando. O corriendo lentamente, huyendo de mí hacia su silencio."

"Ella tiene la habilidad de estar sola en compañía, he notado."

show bg city_street3_rn behind rain
hide ev
hide ovl
with locationchange

"Caminamos por la calle, luego doblamos a la izquierda, y luego tres veces a la derecha, luego a la izquierda de nuevo."

"Es como aquella noche de hace algún tiempo, seguimos escogiendo direcciones al azar porque no importa adónde vamos."


"Todo lo que importa es caminar y el sonido de las gotas de lluvia tamborileando el paraguas."

"El agua fluye abajo desde los tejados de los edificios y hacia el drenaje pluvial en ríos anchos."

"Aunque trato de pasar sobre ellos, mis pies están mojándose a través de mis zapatos."

"Seguimos caminando en silencio que ruega por ser roto otra vez. Sin embargo, estoy seguro de que soy el único que se siente así."

hide bg
show ev rin_rain_away behind rain
show ovl rin_rain_hisaotowards at Position(xalign=1.0, yalign=0.0) behind rain
with locationchange

hi "¿Por qué tuviste la exhibición?"

"Rin solo se encoge hoscamente de hombros y mira en otra dirección. Me doy por vencido en este punto."

window hide

hide ovl
with charachange

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")
$ renpy.music.set_volume(0.5, 1.0, channel="music")

nvl clear
nvl show dissolve

n "\n\n\nNo tiene punto."

n "\n¿Qué es lo que ella quería lograr? Lo que dijo en la noche de la apertura me hizo sentir que había algo… algo especial que ella quería."

n "Para mí se sintió que Rin aspiraba hacia algo inalcanzable."

n "Se fijó la meta demasiado alta y dentro de su propia cabeza ella fracasó, sin importar cuánto le haya gustado su trabajo a la gente."

n "Es entendible carecer de realismo; a la mayoría de la gente le pasa, aun si no es en el nivel extremo al que Rin lo lleva."

n "\nPero no es razón para vivir en tu propio mundo privado que no acepta visitantes."

nvl clear

n "\n\n\nNo puedes doblar el mundo para que sea acorde a tu cosmología retorcida y megalómana donde todo funciona justo como tú quieres."

n "\nEso es lo que más me frustra de Rin."

n "\nElla quiere que el mundo viva bajo sus reglas, descartando todo lo que entre en conflicto con aquellas como irrelevante o innecesario."

n "No puedo creer que alguien en Yamaku podría no tener la más mínima percepción para entender que el mundo puede algunas veces ser muy injusto."

n "Estoy seguro de que ella no es la única que desea que algunas cosas fuesen diferentes, pero por lo menos podemos comprender los hechos como son."

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")
$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

hide ev
show bg city_street4_rn behind rain
show rin negative_spaciness_close_rn at center
with locationchange

window show

"Le echo una mirada de reojo a Rin, quien está mirando nuestra cubierta en forma de domo. Es un pobre reemplazo para el cielo verdadero con su austeridad monocromática."

"La lluvia solo sigue cayendo."

"Al igual que las nubes hoy, Rin realmente no da la sensación de querer ser observada."

"Se enfada al unísono con el cielo que ella ama tanto."

"No debería de haber venido. Su presencia únicamente me recuerda cuán enojado me puse a causa de exactamente estas razones, y cómo esas razones probablemente nunca podrán cambiar."

"Aun si quiero decir que lo siento, a pesar de que no quiero que nos separemos, no puedo obligarme a decir alguna de estas cosas."

show bg misc_sky_rn
hide rin
with locationchange

"Seguimos caminando por la calle empapada por la lluvia un paso a la vez."

"A menudo, cuando caminas junto con alguien más, tus pasos se sincronizan con los suyos como por algún extraño pacto subconsciente."

"He notado que los nuestros nunca lo hacen."

window hide

stop music fadeout 5.0
$ renpy.music.set_volume(0.3, 3.0, channel="ambient")

show bg misc_sky_rays
show rain light
with Dissolve(3.0)

window show

"El tiempo pasa, y los golpes contra el parche de tambor de mi paraguas se disipan a medida que las nubes sobre nosotros se dispersan poco a poco para revelar un azul cerúleo."

show rain light:
    alpha 1.0
    linear 5.0 alpha 0.0
with None

stop ambient fadeout 9.0

"Eventualmente la lluvia cede lo suficiente como para que cierre el paraguas, sacudiendo el exceso de agua antes de hacerlo."

"Mientras batallo con el mecanismo, Rin se detiene tan abruptamente que doy cinco pasos antes de darme cuenta de que ya no está conmigo."

"Parece que el estúpido paraguas se atascó."

play music music_innocence fadein 6.0

scene ev rin_trueend_normal:
    truecenter
    zoom 1.2 rotate -6 subpixel True
    easein 6.0 zoom 1.0 rotate 0
with locationchange

"Cuando me doy vuelta, la encuentro mirándome con un rostro impasible."

rin "Quería que alguien dijera “entiendo cómo te sientes”."

rin "¿No sería eso genial?"

"¿Es esa una respuesta a la pregunta de antes? No estoy seguro."

hi "Sí… pero, ¿por qué es tan importante?"

scene ev rin_trueend_sad:
    truecenter
    zoom 1.0 rotate 0 subpixel False
with locationchange

rin "Porque de otro modo… no sé si pueda soportar esto."

"Todavía estaba en medio de guardar mi paraguas así que solo respondo cualquier cosa para mantener la conversación andando, pero lo que dice ahora me congela la sangre."

scene ev rin_trueend_closed
with locationchange

rin "Si alguien dice una broma y se ríe, te ríes con ellos, ¿verdad? Porque la alegría duplicada es la alegría triplicada, ¿verdad?"


scene ev rin_trueend_smile
with locationchange

rin "Si alguien está lastimado y triste, lo reconfortas y lo abrazas, ¿verdad? Porque de esa manera—"

rin "…"

"Hace una pausa, su boca todavía a medio abrir, entonces recuerda cerrarla."

scene ev rin_trueend_normal
with locationchange

"Una penumbra se asienta en su rostro y simultáneamente en mi corazón."

rin "No sé por qué las palabras correctas nunca salen."

rin "No sé por qué puedo reír solo cuando yo me hago reír."

rin "No sé por qué todo se queda solo dentro de mí, aun cuando se siente como si fuese a estallar."

"Su llano e inexpresivo rostro no vacila siquiera cuando dice eso."

"Su usual voz inalterable tan solo se hace ligeramente más callada de lo normal."

rin "Pero, ¿quién… quién quisiera sentirse así?"

"Rin me mira e imagino la tristeza reflejándose desde sus ojos, sin importar si está realmente ahí o no."

rin "Yo no."

rin "No quiero sentirme así."

"Guardamos silencio por un corto momento después de eso."

"Rin porque dijo todo lo que tenía que decir de una vez, yo porque no tengo idea de cómo procesar lo que acaba de decir."

"No entiendo lo que Rin está diciendo. O sí lo entiendo, pero no quiero."

"Por primera vez estas dos cosas suceden, y tiene que ser simultáneo."

"La ironía no se me escapa."

hi "Yo… creo que todos quieren ser entendidos. Eso es universal."

hi "Pero… eso es imposible. No solo para mí, pero para todo mundo."

hi "Sae también lo dijo."

hi "Afectas a otras personas y eres afectada por ellas, pero al final, tú ves todo de la manera en la que solo tú puedes."

hi "Todas las personas… están solas. Tan solo nos utilizamos mutuamente para aliviar esa soledad."

"Me pregunto por qué lo dije de esa manera. Solo se sintió como si lo que dijo Sae fuera la verdad, como si siempre hubiera pensado de ese modo sin saberlo."

"Se siente como si ella hubiese articulado mis pensamientos en claras y simples palabras y en esa estúpida historia sobre Picasso."

scene ev rin_trueend_closed
with locationchange

"Rin deja caer la cabeza como una flor marchitándose, dejando que su flequillo caiga frente a sus ojos de modo que yo no pueda verlos."

rin "¿Por qué dices eso cuando me hiciste sentir algo más?"

rin "No es justo."

"La trémula voz que dice esas palabras no pertenece a Rin."

scene ev rin_trueend_sad
with locationchange

rin "Realmente pensé que tú podrías ser diferente. Que no tendría que estar sola."

"Es una amarga voz de desilusión, dicha a través de dientes apretados y un pecho tembloroso."

hi "Lo siento…"

rin "Si lo haces, ¿por qué dices algo injusto como eso?"

"Su tono demandante no invoca ningún sentimiento en particular en mí, además de tristeza que ha estado ahí desde ayer en la noche."

"Ella no me intimida en absoluto. Ya no más."

"Rin no es un genio prodigio, ni una impredecible chica con savantismo que podría desgarrar el lóbulo lógico del cerebro haciéndolo jirones cuando sea que abra su boca."

"Tan solo es una chica que pensé que amaba, una amada que quería ser mi amiga, una amiga que defraudé."

hi "Digo eso, porque decir otra cosa se sentiría como mentir."

scene ev rin_trueend_normal
with locationchange

rin "¿Por qué?"

"Las preguntas simples son las más difíciles. Tengo que cerrar los ojos para así poder concentrar mis pensamientos lo suficiente para responderle."

hi "No soy un artista. Nunca podré estar al mismo nivel que tú."

hi "Hay un mundo que solo tú puedes ver, y para ser parte de él tendría que convertirme en ti."

hi "Eso es algo que no puedo hacer, sin importar qué tanto desees que lo haga."

"Rin toma mi explicación sin mover una pestaña."

rin "Tampoco soy una artista de verdad."

rin "Yo solo pinto porque me hace sentir como si en realidad pudiera sentir algo."

scene ev rin_trueend_weaksmile
with locationchange

"Contiene el aliento por un momento antes de sacarlo en un largo flujo parecido a un suspiro."

scene ev rin_trueend_closed
with locationchange

rin "Es por eso que lo haré."

rin "Ya me he decidido. Lo haré. Si incluso Hisao lo dice, entonces eso es lo que haré."


hi "¿Hacer qué?"

"Rin, asustándose un poco, muestra que se ha revertido a hablar consigo misma otra vez, pero me alegro de que pueda hacerla volver a la realidad."

scene ev rin_trueend_normal
with locationchange

rin "El maestro y Sae han hablado con alguien que es una persona muy importante. Me dieron una beca para una gran escuela de arte en Tokyo."

rin "Dijo que me podía transferir allá y comenzar después de que termine el verano, si quería."

rin "En realidad no entiendo por qué—"

stop music fadeout 10.0

hi "Espera, ¿qué? ¿Por qué no lo dijiste?"

scene ev rin_trueend_smile
with locationchange

rin "Acabo de hacerlo. Eres el primero al que se lo digo porque acabo de decidirlo apenas."

"Mantiene su sangre fría, viéndose apenas ligeramente sorprendida de mi exclamación estupefacta."

"Es ridículo qué tan fácil puede decir algo que te cambia tanto la vida."

"No puedo creerlo. Después de lo que pasó en febrero, ya he tenido suficiente por este año."

"Aun si las cosas andan mal en este momento, no quiero que todo cambie."

hi "Pero, ¿qué hay de Yamaku? ¿No te quieres graduar con todos?"

"Mi súplica no provoca emoción."

rin "¿Todos quiénes?"

hi "¡Emi, yo, todos!"

"Siento mi pulso elevarse alarmantemente, y mi respiración se hace rápida y poco profunda."

"No quiero que esto ocurra."

rin "Su vida no es la mía."

rin "Tú acabas de decir que todos están solos."

hi "No quise decirlo de ese modo—"

rin "Tú siempre decías que tendrías que aprovechar el día y comenzar a vivir tu vida."

rin "También yo tengo que vivir mi vida."

"Rin está torciendo mis palabras para justificar el huir de nuevo. Me hace enojar."

"Su tranquilidad, firmeza y seriedad al anunciar esto es inaceptable."

"¡Como si cambiar tu vida es algo que puedas hacer en un capricho de un momento! ¡No!"

hi "¿Cómo puedes decir eso? ¿Por qué ni siquiera tratas de pertenecer?"

"La acusación desesperada no tiene efecto. Se siente como si una vez más me encontrara sin armas, que no puedo llegar a ella sin importar qué trate."

"Rin es tan frustrantemente absoluta en su propio juicio que podría hacerme odiarla si no la amara, aunque ya no sé de qué forma me siento."

scene ev rin_trueend_normal
with locationchange

rin "Tal vez soy ese tipo de persona. Del tipo que pertenece solo a sí misma."

hi "No aceptaré eso."

"A sus indiferentes ojos no parece importarles si acepto su decisión o no."

"…"


"La pausa me permite tranquilizarme, para encontrar mis sensibilidades."

"Mientras lo hago, las nubes de lluvia que se retiran revelan un sol poniéndose que todavía tiene tiempo de brillar sus últimos cálidos rayos antes de terminar el día."

"Un mosaico de luz y sombra se propaga sobre los muros de los edificios, en la calle y la valla que rodea al parque al otro lado de la calle."

"La sombra de Rin es lo suficientemente larga para alcanzar mis pies."

"Es como una de esas películas del viejo oeste, con dos vaqueros mirándose fijamente el uno al otro, listos para desenfundar sus pistolas contra el otro."

"Aquel que se acobarde comerá plomo."

"Me doy cuenta de que yo tendría la desventaja porque el sol está detrás de Rin, lastimándome los ojos."

scene ev rin_trueend_sad
with locationchange

rin "¿Me odias?"

"Ella desenfunda primero y no tengo respuesta."

hi "No lo sé."

"¿Acaso perdí?"

hi "Aun si lo hiciera, ¿qué importancia tendría?"

"Batallo para encontrar palabras, palabras que podrían rescatar esto. No encuentro ninguna."

hi "Eres mi amiga, prometiste eso. No soy de la clase de tipos que olvidan las promesas."

hi "Creo que eso es lo más importante. Podríamos tratar de—"

scene ev rin_trueend_normal
with locationchange

rin "No lo digas."

scene ev rin_trueend_hug
with locationchange

play music music_friendship fadein 4.0

"Prediciendo lo que iba a decir, Rin se arroja a mis brazos, presionando su cuerpo contra el mío."

"La siento pararse de puntillas para igualar mi altura y acurrucarse más cerca."

"El aroma de su cabello es aquel de lluvia y solvente de pintura. Su cuerpo se siente tan frío como siempre. Su aliento contra mi cuello es tan caliente como siempre."

"Es gracioso cómo todos ellos se sienten tan familiares aun si Rin, como un todo, no."

scene ev rin_trueend_hugclosed
with locationchange

rin "¿Estás seguro de que no puedes odiarme?"

"Rin susurra en mi oído tan cerca que puedo sentir el movimiento de sus labios en el lóbulo de mi oreja."

"Es provocativo y burlón. Si esto fuera una situación de algún otro tipo estoy seguro de que me haría cosquillas de manera seductora y me reiría nerviosamente aunque sea un hombre."

rin "Sería más fácil si lo hicieras."

hi "No sé. Es bastante difícil cuando me estás abrazando así."

scene ev rin_trueend_sad
with locationchange

"Me pregunto si es por mi voz taciturna, pero ella da un paso hacia atrás, viendo con melancolía a sus cortos brazos."

"Desearía que ella no hubiese hecho eso."

rin "No puedo abrazar a nadie, Hisao."

rin "Soy una persona así de mala."

scene ev rin_trueend_normal
with locationchange

rin "Es por eso que tengo que irme."

"Me desarma por completo con tres simples oraciones, dejándome incapaz de discutir más."

"Y ya que no puedo, Rin es libre de continuar como desee, balanceándose de un pie al otro antes de hacerlo."

scene ev rin_trueend_smile
with locationchange

rin "Aprenderé a abrazar a la gente a mi propia manera."

rin "Estoy segura de que puedo convertirme en una artista verdadera."

rin "Pero si lo hago… Puede que ya no sea capaz de ser yo."

"La insinuación de una sonrisa sobre sus labios es una traición, una falsa señal de confianza en un futuro que incluso Rin no puede prever."

"Quisiera interpretarlo como una señal de esperanza, pero sé que no puedo."

"Rin solo continúa sonriendo esa extraña y forzada sonrisa suya."

rin "Es por eso que… por favor olvídate de mí, y yo también me olvidaré de ti."

rin "Estoy segura de—{w=0.5}{nw}"

scene ev rin_trueend_sad
with locationchange

"Rin se ahoga a la mitad de decir algo que nunca llegaré a escuchar."

"No creo que hubiera querido oírlo de cualquier modo."

"Esto no es justo."

"Rin no está bromeando. Rin siempre habla en serio. Pero no puedo aceptarlo, no puedo."

"¿Olvidarme de ti? ¿Cómo podría…?"

"Eso es lo que quisiera decir. Pero no sé cómo continuaría. No se me ocurre nada bueno que decir, así que tengo que retarla."

hi "¿Cómo puedes decir tal cosa?"

scene ev rin_trueend_normal
with locationchange

"Rin levanta los ojos para encontrarse con los míos, son serios y profundos, una imagen perfecta del territorio sin explorar que siempre pensé que eran."

"Incluso ahora, no puedo leer sus emociones a partir de esos iris imperturbables de jade que nunca pudieron reflejar lo que veían."

rin "Es fácil. Después de todo, soy buena olvidando cosas."

"…"

"Su falta de justicia me hace un nudo en la garganta, pero logro pronunciar la pregunta ardiendo en mi mente."

hi "Así que, ¿esto es todo? ¿Esto es el adiós?"

"…"

"Rin siguió viéndome gentilmente, sin responder mi pregunta."

"De sus ojos pude ver que ella ni siquiera necesitaba decir algo."

"No había más palabras para nosotros."

stop music fadeout 12.0

scene ev rin_trueend_gone
with locationchange

"Se dio la vuelta y caminó sin mirar atrás."

"Todo a mi alrededor, el mundo siguió cambiando, poco a poco, pero yo me quedé de pie ahí."

scene ev rin_trueend_gone:
    "ev rin_trueend_gone_ni" with Dissolve(10.0)
with None

"El sol cayó debajo del horizonte, proyectando largas y delgadas sombras por la calle."

"En la menguante luz, la espalda distante de Rin parece haber sido de un sueño lejano."

"La brecha entre nosotros creció lentamente."

"Las ondas en los charcos que pisó se expandieron hasta llegar a los límites de su pequeña existencia y desaparecieron sin dejar rastro."


"Sus palabras se quedaron congeladas en lo más profundo de mi corazón."

window hide


label es_R38:


scene bg school_room34
with None

show rin negative_spaciness
with charaenter

play music music_drama fadein 6.0

"Ella está de pie en medio del salón iluminado por el sol, asomándose a través de la separación entre las cortinas hacia el patio."

"Como muchas veces antes, no se asusta ni salta, solo espera tranquilamente a que yo haga el primer movimiento."

"Es como si ella estuviese tratando de convertirse en una parte permanente de los muebles."

hi "El maestro te está buscando."

"Una mirada en blanco sobre su hombro es todo lo que obtengo, acompañada de una cara críptica e inexpresiva."

rin "¿Tú también me estás buscando?"

hi "Nah, ya te encontré, ¿o no?"

rin "¿Lo hiciste?"

show rin negative_annoyed
with charachange

"Ella frunce el ceño, viéndose tan confundida que me hace dudar de si la pregunta fue hecha en serio."

"Tal vez lo fue."

hi "¿Estás ahora hablando metafóricamente?"

show rin negative_spaciness
with charachange

rin "¿Quieres decir como las anguilas, cuevas y oscuras noches tormentosas?"

show rin negative_sad
with charachange

rin "Soy mala hablando de ese modo."

"…"

play sound sfx_doorclose

"El saludo terminado abruptamente me da la oportunidad de cerrar la puerta detrás de mí y sentarme en la mesa de un banco cubierto de polvo."

show rin basic_absent
with charachange

"Rin se queda de pie, pero por lo menos se da la vuelta."

"Pero pronto deseo que no lo hubiera hecho, su mirada anticipativa es tan opresiva."

"Este es su lugar y yo soy un intruso, aunque uno tolerado. A pesar de ello, ella sigue esperando a que diga algo."

"Si solo supiera qué."

"…"

"El silencio iluminado por el sol me presiona hacia las decisiones."

"Vine aquí sin realmente pensar qué haría, aparte de entregar el corto mensaje de Nomiya en el caso de que Rin estuviera aquí."

"Sí estaba, y ahora no sé qué más quiero decir… ¿qué más debería decir?"

"Considero mis dos opciones por un momento."

"Que Rin esté preocupada también me preocupa. Es una revelación sorprendente, casi tan grande como lo fue el percatarse de que ella en verdad está preocupada."

"Nada que yo pueda hacer podría ayudar, y quizás también sea parcialmente culpable de eso."

"¿Acaso eso significa que debería simplemente lavarme las manos de ella?"

"No lo creo."

hi "Y bien… ¿qué está mal?"

"…"

show rin relaxed_nonchalant
with charachange

rin "Nada."

"Comienza a apartarse de nuevo, como si tratase de salirse físicamente de una conversación que no quiere tener."

hi "Rin, deja de intentar evadirme o me iré."

show rin relaxed_boredom
with charachange

rin "Está bien."

hi "¿Quieres que me vaya?"

show rin relaxed_doubt
with charachange

rin "¿Sigues enojado?"

"Nos tomó —¿o fue solo a mí?— diez segundos hundir la conversación hasta esto."

"Desearía que pudiéramos borrar el pasado, o en su defecto, olvidar todo de este."

"He deseado eso más de una vez en los últimos meses."

hi "Dejemos eso de lado por el momento, ¿está bien?"

show rin basic_absent
with charachange

rin "Si tú lo dices."

hi "Lo digo. Así que… ¿qué ocurre?"

hi "Sae y Nomiya no estaban muy contentos con que simplemente te escaparas ayer."

hi "Los dejaste en un gran aprieto, y supongo que el maestro quiere algún tipo de explicación."

hi "Parecía que básicamente hubieses tirado todo por lo que habías trabajado. Y no entiendo por qué."

show rin basic_deadpanupset
with charachange

rin "¿Cometí un error?"

"Mi reprimenda y su respuesta llana van tan en contra de las expectativas usuales y las interacciones presupuestas que bien podría ser otra persona hablando."

"Ninguno de los dos es como solía ser, esta sensación rígida y estrecha que tengo cada vez que veo a Rin actualmente parece ser reflejada en su comportamiento."

"Odio las cosas que van irreparablemente mal. Desde febrero las he odiado."

"¿Qué puedo decir?"

"Su pregunta es seguida por una mirada imperiosa e inquisitiva que me hace suspirar y fruncir el entrecejo."

"Las conversaciones que nadie quiere tener son las peores."

hi "No lo sé. Quiero decir, no es el fin del mundo pero probablemente fue bastante estúpido."

show rin relaxed_nonchalant
with charachange

"Ella responde con un suspiro suyo, aunque el de ella no es ni cercanamente tan pesado como el mío."

show rin relaxed_sleepy
with charachange

rin "Es solo que no podía hacerlo."

hi "Pero… ¿Por qué? ¿Qué ocurre?"

show rin negative_annoyed
with charachange

"Una pausa, un ceño fruncido, una voz callada."

rin "Déjalo ser, Hisao."

rin "No creo que pueda realmente explicarlo de un modo que tenga sentido."

"Sí, Rin tampoco quiere tener esta conversación. Eso puede ser lo mejor."

"Pero qué raro de ella, admitir que incluso ella tiene algún tipo de límites."

"Siempre pensé que Rin era completamente ignorante de su tendencia a distraerse, tanto que sin darse cuenta ofusca todo lo que dice."

"…"

hi "Nunca explicas {b}nada{/b} de un modo que tenga sentido."

show rin basic_absent
with charachange

rin "Nadie más me lo había pedido."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "Supongo que así es como es."

n "Pero yo siempre quise entenderte, encontrar quién eres."

n "Todavía quiero hacerlo, ¿no lo ves?"

n "…"

n "Sé que no."

n "Pero yo sí."

n "¿Es por eso que continúo con esto? Te duele tanto como me duele a mí. Es poco probable que le sea útil a alguno."

n "Hicimos y dijimos cosas que no pueden deshacerse."

n "Es como si… tú y yo estando cerca uno del otro solo nos lastimara a los dos, pero aun así seguimos intentándolo deliberadamente."

n "¿No es eso tonto?"

n "Incluso ahora, puedo ver cómo te fuerzas a responder aun si no me debes nada."

n "Aun si es difícil hablar de cosas como esta."

n "¿Por qué?"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear
window show

hi "¿Por qué es que pintas?"

show rin basic_awayabsent
with charachange

rin "Yo… porque no sé qué más podría hacer."

rin "Es como esta sensación de que no hay opción, que es la única posibilidad."

show rin basic_sad
with charachange

rin "Como cuando solo quedan paletas de sandía en la tienda pero necesitas comer una paleta."

"Dejando de lado su mala metáfora, realmente no respondió nada. Si es posible, esto tiene todavía menos sentido que no saber."

hi "Pero… si no quieres pintar…"

show rin negative_spaciness
with charachange

rin "No así. Tú tuviste que venir a esta escuela aun si probablemente no querías tener un ataque al corazón."

show rin negative_annoyed
with charachange

"Hace una pausa, frunce el ceño como si algo en lo que dijo no le hubiera gustado."

show rin basic_lucid
with charachange

rin "Al menos creo que no quisieras."

"Su seguimiento cuidadoso es acompañado por otra pausa más corta y otro gesto parecido más pequeño."

show rin basic_deadpanupset
with charachange

rin "¿Te gustaría tener un ataque cardiaco?"

hi "No, no me gustaría y no quise tenerlo."

show rin basic_deadpansurprised
with charachange

rin "Pero te está yendo bien, ¿o no? ¿O todavía estás triste por eso?"

"La pregunta de Rin hace que me percate de que realmente no he pensado en mi enfermedad por semanas."

"Aparte de tragarme mis medicinas cada día no ha habido necesidad de preocuparme de mi corazón roto, por lo que simplemente estoy agradecido, realmente."

"Conocer gente nueva, una escuela nueva, un pueblo nuevo… una vida nueva, todo ello me ha cautivado y hecho al pasado desvanecerse."

hi "No… je, supongo que ni siquiera yo puedo vivir en el pasado indefinidamente."

show rin basic_awayabsent
with charachange

rin "¿Ves? Incluso la sandía realmente no sabe mala si tienes que comerla."

"Su cierre semiabsurdo parece ponerle fin al tema en la mente de Rin, así que yo solo asiento en insegura confirmación."

"…"

"…"

"Hay dos tipos de silencios: los incómodos que quieres romper, y los cómodos que no te molestan."

"Los del primer tipo son malos, porque hacen que tus pensamientos vayan mal. Como los míos en este momento."

"Mirar a Rin me hace sentir mal."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\nNo quiero sentirme así."

n "Mirar a Rin me hace sentir… exhausto. En verdad hice mi mejor esfuerzo, ella trató de… no tengo idea."

n "Pero terminamos así, y ella terminó arruinando la apertura de su exhibición."

n "Parece que estamos en un callejón sin salida."

n "No hay dirección para continuar."

n "Me acerqué a ella ayer, pensando que sería la última vez."

n "Se marchó."

n "“Quiero ser yo”."

n "¿Qué diablos significa eso? Si alguien lo es, Rin en definitiva es ella misma."

n "Me siento un poco aliviado de no ser el culpable, pero en mi mente esto todavía me molesta."

n "¿Por qué escapó? No tenía sentido ayer. No tiene sentido hoy."

n "Las cosas que dijo se sienten como si debieran de tenerlo pero simplemente no lo tienen, para mí."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear
window show

hi "Sabes, sobre esa cosa que acabas de decir…"

show rin basic_absent
with charachange

rin "¿Cuál de ellas?"

hi "Ehh… pintar… Sae me dijo algo así antes… que un artista verdadero no pinta porque quiere, sino porque {b}debe{/b}."

hi "Y he estado pensando en lo que ella dijo. ¿Por qué los artistas {b}deben{/b} pintar?"

"Mi pregunta probablemente es bastante estúpida. Por lo menos Rin me mira de la manera inexpresiva que parece decir eso."

show rin basic_deadpannormal
with charachange

rin "No lo sé. ¿Soy una artista?"

hi "Bueno, pintas cosas y también tienes una exhibición. Diría que calificas."

show rin basic_deadpancontemplation
with charachange

rin "Creo que todavía no lo sé, pero está bien."

"La pausa reflexiva que sigue parece durar media eternidad."

"A diferencia de la mayoría de las personas, Rin no le da sabor a sus pausas pensativas por medio de lenguaje corporal o al decir “como” o “ehhh” o nada."

"He notado que puede que prefiera su modo."
"El modo usual incluso me molesta, como si las personas estuviesen tan infatuadas con el sonido de su voz que simplemente tuvieran que seguir haciendo ruido aun cuando solo están pensando en lo siguiente que podrían decir."

"Rin simplemente… se detiene por completo mientras piensa. Es desconcertante, porque reaccionar a gente que se queda ida es siempre difícil, pero se siente menos repelente."

show rin basic_lucid
with charachange

rin "Creo que quiero a alguien que vea qué hay dentro de mí. No de la manera que los doctores o asesinos en serie lo hacen."

show rin basic_absent
with charachange

rin "Del modo que no me haga sentir sola."

show rin relaxed_boredom
with charachange

rin "Esto es lo que llamas metafórico, sabes."

hi "Por favor no me des una lección sobre cosas evidentes."

show rin basic_deadpansurprised
with charachange

rin "No es evidente que esto sea evidente."

hi "Entonces, ¿le presentas una pintura a alguien y esperas que él mágicamente capte un destello de tu alma?"

show rin negative_angry
with charachange

rin "No es así. Es solo un poquito como eso pero no realmente. ¿Que no entiendes?"

hi "Entiendo… y no entiendo."

hi "Sabes, me siento un poco desesperanzado cada vez que haces esa pregunta."

show rin basic_absent
with charachange

rin "¿Qué pregunta?"

hi "Sobre si te entiendo o no."

"Ella parece casi sorprendida ante mi clarificación."

show rin basic_lucid
with charachange

rin "Oh, en realidad no es una pregunta. Es una de ese tipo que no tienes que responder."

hi "Retórica."

show rin basic_absent
with charachange

rin "Sí, esa es la palabra, una pregunta que no es una pregunta es una pregunta retórica. Qué lindo."

rin "Eso me recuerda, en realidad no tiene sentido. ¿Qué tipo de pregunta es una que no es pregunta?"

hi "Una retórica."

rin "¿Qué tipo de respuesta es una respuesta que no responde nada?"

hi "¿Es esa una pregunta retórica?"

show rin basic_deadpanupset
with charachange

rin "No eres gracioso."

show rin basic_awayabsent
with charachange

rin "Pero si no te gusta, ¿quisieras que mejor dijera algo diferente?"

show rin basic_lucid
with charachange

rin "Aunque no tengo ninguna buena. ¿Qué tal… “Tus pantalones se están quemando”?"

show rin basic_absent
with charachange

rin "Esto puede ser nuestro lenguaje secreto."


"La verdadera bobería de Rin, hecha el doble de ridículo por el hecho de que sé que ella está hablando completamente en serio, me saca de mi ritmo como siempre lo hace."


"Es como un mecanismo de seguridad para prevenir que me convierta en uno de esos tipos angustiados, impidiéndome mantener los pies en la tierra donde deberían de estar."

"Me hace sonreír confusamente, pero solo en mi interior."

"A pesar de que las comisuras de mi boca no se dibujen en una sonrisa, estoy impresionado por la facilidad con la que rompe cualquier intento de ser demasiado serio."

"¿Podría ella (si se lo propusiera) olvidar e ignorar las cosas que le molestan, cosas que la angustian?"

"¿Podría ella (si se lo propusiera) ser libre de cualquiera que sea la carga que ser ella significa?"

"¿O soy yo el único que se siente agobiado por ser yo mismo?"

hi "No gracias."

hi "Pero igual, las veces en las que siento que coincido contigo son bastante raras."

hi "Se siente como… si hubiera esta brecha y algunas veces tú simplemente vas al otro lado, y yo no… tengo ningún modo de alcanzarte desde donde estoy."

hi "Es como si estuvieras en lugares completamente diferentes, algunas veces."

hi "Aunque estés justo aquí."

"Es cierto."

"Hay una discontinuidad insuperable, un muro de cristal imaginario que no permite que haya comprensión."

"Puede que exista tal brecha entre cualquier par de personas, pero con Rin se siente más tangible."

"Rin no reacciona a mis pensamientos, ni a los que dije en voz alta ni a los que no dije."

hi "Es aun peor con el arte."

hi "No soy muy bueno con el arte, lo admito."

hi "Me uní al club de arte porque pensé que podría ser interesante."

hi "Y supongo que lo es. Me gusta el arte, me gusta tu arte también, pero al igual que contigo, no puedo comprenderlo."

hi "Y estoy bastante seguro de que nadie puede realmente."

show rin relaxed_doubt
with charachange

"Esto parece preocuparla ligeramente."

rin "¿Tú crees eso?"

hi "Sí. Supongo que el arte debe de ser interpretado, no entendido. Así es como lo pondría."

show rin relaxed_sleepy
with charachange

rin "Ese es un pensamiento triste."

hi "Supongo que podría sentirse como uno."

hi "¿Hace que te sientas triste por ti misma?"

show rin basic_lucid
with charachange

"Rin piensa en esto por un momento, y luego agita su cabeza con sorprendente vehemencia."

show rin basic_deadpannormal
with charachange

"Lo primero en lo que fija su mirada después de ello soy yo."

"Estas dos cosas me hacen sentir alegre y aliviado."

hi "Eso es bueno, ¿o no? De cualquier modo, deberías de ir a hablar con el maestro y disculparte apropiadamente."

hi "Creo que estaba preocupado por ti."

hi "¿Puedes hacer eso?"

show rin basic_absent
with charachange

"Esta vez ella asiente con la cabeza."

stop music fadeout 4.0

"Solo que no es igual de vehemente."


label es_R39:

scene bg school_hallway3
with locationchange


"El pasillo se encuentra vacío. Es casi intimidante."

"La “oficina” de Nomiya es el salón de arte al otro extremo del pasillo del tercer piso."

show rin basic_absent at center
with charaenter

"Nuestras pisadas hacen eco perturbadoramente. El ambiente es diferente al de una tarde normal. Se siente como si la escuela supiera que nadie vendrá de vuelta por un mes, también."

"La puerta está abierta, pero no es muy atrayente."

hi "Yo… eh, esperaré afuera."

show rin relaxed_nonchalant
with charachange

with Pause(0.2)

show rin invis at tworight
with dissolvecharamove

hide rin
with None

"Asintiendo de manera apenas notable, Rin da pasos sin detenerse y, naturalmente, sin llamar a la puerta."

"Tal vez ese es el porqué pasan unos segundos antes de que escuche la voz del maestro desde adentro."

no "¡Ahí estás!"

rin "Hola."

"Surge un conflicto: ¿Debería quedarme aquí o irme a algún otro lugar?"

"No estoy seguro si siquiera quiero escucharlos a escondidas."

"…"

show bg school_hallway3 at right
with charamove

"Los modales pierden ante la curiosidad, y entonces me quedo lo suficientemente cerca como para escucharlos."

"Sus voces hacen eco en el pasillo, pero no importa."

"No hay nadie alrededor, salvo por mí."

play music music_tragic fadein 8.0

no "Querida niña, ¿en qué estabas pensando, marchándote de esa manera en la gran noche?"

rin "No podía decir nada."

"Comparado con el tono de regaño de Nomiya, Rin suena terriblemente callada y retraída."

"Sus palabras parecen ahogarse bajo las de él."

no "Tengo que decir que estoy muy decepcionado de ti, Tezuka."

rin "No fue para nada bueno."

no "Olvida todas las cosas que hice por ti, pero, ¿qué hay de Sae? ¿Qué hay de todos los invitados que querían conocerte?"

rin "No había nadie. Incluso Hisao…"

no "Nos has avergonzado tanto, Tezuka."

no "La reputación es lo que cuenta, ¿seguramente sabes eso?"

rin "Está bien. No la necesito."

no "¡“No necesitas”! ¿Tú qué crees que sabes?"

"Las respuestas de Rin solo parecen agitar más al maestro, su voz se levanta con cada oración."

no "El camino de un artista está lleno de espinas, ¡te diré eso! ¡Lleno de espinas!"

no "¡Tienes que ver el panorama total! ¡Habrá tiempos malos y tiempos buenos!"

rin "Las cosas son como son. Estará bien aun—"

no "Puede que ahora pienses que es tan, pero tan maravilloso y fácil, ¿pero qué tan lejos habrías llegado sin mí?"

no "¡No estaré siempre ahí para ti!"

no "Cuando estés tendida en el suelo de tu minúsculo departamento, tu renta tres semanas retrasada, tu mente en blanco por la cuarta semana seguida, entonces desearás haber escuchado al viejo Nomiya un poco más."

no "¡Cuando sigas midiendo cómo la sombra de tu silla se hace más larga durante la primavera porque eso es todo lo que te permite tu apatía, tal vez entonces sea cuando empezará a importarte tu carrera!"

rin "Eso no importa."

no "Tu determinación no es suficiente."

rin "No soy una persona determinada."

no "No eres una persona determinada…"

play sound sfx_impact2
with vpunch

no "Entonces dime, por qué… por qué… ¿POR QUÉ FUE QUE PASAMOS POR TODO ESTE PROBLEMA SI TODO ASCIENDE A LA MIERDA DE UN MOSQUITO?"

"Por Dios, el maestro perdió la cabeza."

"Que él le grite a Rin me hace sentir culpa por ser un espectador. Si hubiese ido con ella, quizás no se hubiese enojado tanto."

"Si no la hubiese dejado ir, él no se hubiese enojado en primer lugar."

"Todavía podría ir y salvarla… no creo que pueda."

"Yo fui igual. También le grité a Rin, y me siento todavía más avergonzado de ello."

"Me sentí justificado de descargar mi ira en su cara solo porque… solo porque sentí que era su culpa que me sintiera tan frustrado."

"Yo no tenía más justificación que el maestro."

"…"

"Un terrible silencio se asienta en el pasillo."

"Rin no tiene nada que decirle a Nomiya."

"Ya sea que se le han acabado las respuestas o que sepa que discutir solo lo enojaría más, nadie lo sabe."

"El maestro tampoco tiene nada más que decir, parece ser, o tal vez solo se le acabó el aire."

"Por un momento, me imagino a los dos solo mirándose mutuamente, uno rojo lleno de cólera, la otra llena de… sí, ¿de qué?"

"No puedo saber cómo se siente Rin, no antes, ni ahora."

"El maestro parece esperar que Rin diga algo también, pero ya que no lo hace, él finalmente continúa en una voz más callada pero no menos enojada."

no "¿Qué valor tiene hacer tanto trabajo si el resultado es… nada?"

"Aun así, Rin no dirá nada."

no "Lo lamento. No debería de haberme alterado tanto."

"No suena apenado en absoluto. Más bien, su tono es frío y severo, como si estuviese escupiendo las palabras fuera de su boca."

no "Parece que estaba esperando demasiado de ti. No eres una artista, después de todo."

"Sí, no se siente para nada apenado."

show nomiya serious:
    tworight
    alpha 0.0
    parallel:
        linear 1.0 center
    parallel:
        linear 0.4 alpha 1.0
        0.2
        linear 0.4 alpha 0.0
with Pause(1.0)

stop music fadeout 4.0

"Él sale disparado del salón y baja por las escaleras sin darse cuenta de mí."

"Después de que se ha ido, me asomo con cuidado dentro del salón."

scene bg school_nomiya at right
show rin basic_awayabsent at center
with locationchange

"Rin se queda parada ahí, frente al escritorio del maestro."

show rin negative_spaciness
with charachange

rin "No podía decir que lo sentía."

"Lo dice al húmedo aire del salón de clases, no a mí."

"Pero ya que el salón no le responde, tendré que hacerlo yo."

hi "Eso no fue justo de su parte… Estaba enojado, pero de todos modos…"

"No puedo decidir en cómo terminar la oración. Desdeñar al maestro se siente como desdeñar mi propio comportamiento de hace dos días."

"Estúpido, pero correcto en retrospectiva."

show rin negative_spaciness_close
with characlose

"Rin no responderá, quedándose petrificada donde yace, así que camino hacia ella."

"Ella defendió su postura. De cierto modo. No esperaba eso."

"No puedo determinar si es impropio o no, pero de cualquier manera, ella lo hizo."

"Contra mí nunca lo hizo."

"Creo que desearía que lo hubiese hecho, tal vez no me sentiría así de mal."

"Últimamente en verdad parece como si estuviese deseando todo tipo de cosas."

hi "¿Rin?"

show rin negative_annoyed_close
with charachange

rin "Vete."


label es_R40:

scene bg school_nomiya at right
show rin negative_annoyed_close at center
with None

play music music_sadness fadein 6.0

hi "¿Por qué… qué estás diciendo?"

show rin negative_angry_close
with charachange

rin "Tú también estás enojado conmigo, ¿verdad?"

rin "Pensé que eras mi amigo. Pensé que él lo era, también."

"Su voz es diferente a la que he escuchado, es amarga, aguda como agujas y ella sigue mirando fijamente a sus dedos."

hi "No creo que sea sobre eso."

hi "Él quería que fueras algo que no eres. Y…"

show rin basic_surprised_close
with charachange

"Tomo aire profundamente y finalmente atrapo sus ojos con los míos, fijando nuestras miradas."

hi "… Lo siento. También quería que fuéramos algo más… más que amigos."

hi "Tal vez es por eso que no pude contenerme y me sentí tan frustrado, al igual que el maestro."

show rin relaxed_doubt_close
with charachange

rin "¿Más qué? No hay más de mí que yo, eso es todo lo que soy. No lo entiendo."

"Bueno… la respuesta debería ser obvia, ¿no?"

"Me recuerdo a mí mismo, pensando en el propósito de la amistad. Aguantar de todo y de nada, estar ahí para tu amigo."

"¿Fracasé como amigo, pensando que podría ser un peldaño para algo diferente?"

"Tal vez a causa de esos pensamientos, no logré aguantar esas cosas y mantenerme."

"Tan intolerable como es y lo fue Rin, no debería de haberme permitido concentrarme en eso, especialmente cuando comencé a sentirme del modo que me sentí por ella."

"Así que, ¿fracasé?"

"Es lo que sus ojos parecen preguntar."

"…"

hi "Lo siento, Rin."

hi "Puede que no sea capaz de ser tu amigo."

hi "No creo que algún día pueda ser un buen amigo para ti."

"Digo estas cosas porque son la verdad, no porque a uno de nosotros le agradaría escucharlas."

"Pero son algo que debe ser dicho."

"La finalidad de mis palabras crea un silencio retumbante, ¿pues qué podría alguno de nosotros añadir a ello?"

"…"

show rin negative_confused_close
with charachange

rin "¿Por qué? ¿Por qué pasa todo esto?"

show rin negative_sad_close
with charachange

rin "La gente hace cosas que yo no pido y no quiero y todos siguen enojándose conmigo, ya no tengo idea de qué es lo que está sucediendo y no puedo dejar de sentir que quiero escaparme de todo…"

show rin basic_lucid_close
with charachange


"Cierra los ojos, apretándolos, y deja salir su aliento desde lo más profundo con calma."

show rin basic_upset_close
with charachange

"Cuando los párpados abren, todo lo que puedo ver es desesperación verde oscuro."

rin "{b}¡No tengo idea de qué hay de malo en mí!{/b}"

"Su arrebato frenético me deja estupefacto por un momento, y por un instante simplemente nos miramos el rostro el uno al otro."

"Ver sus ojos confundidos desesperadamente tratando de buscar respuestas en los míos solo me hace sentir triste, porque sé que no tengo ninguna."

hi "Yo tampoco lo sé."

hi "Pero, sabes, tú misma dijiste que las cosas no están bien o mal."

hi "Simplemente son."

hi "O las aceptas, trabajas en cambiarlas o te rindes."

hi "No es que yo te odie, o que el maestro Nomiya lo haga."

hi "Es solo que… creo que soy del tipo de persona que se rinde cuando siente que ya no puede más."

hi "Y aun si lo odias, así… así es… como son las cosas."

"Estoy diciendo cosas muy crueles pero no puedo detenerme, las palabras siguen rodando de mi lengua con lenta y dura certeza."

show rin basic_surprised_close
with charachange

"Puedo verlas golpear a Rin casi como golpes físicos."

"A medida que la humedad se junta en las orillas de sus ojos, estos siguen bien abiertos con la impresión del rechazo."

show rin basic_crying_close
with charachange

"A medida que las lágrimas comienzan a deslizarse por sus pálidas mejillas, ella no las detiene."

"A medida que caen en el piso una a una, ella se queda inmóvil, mirándome con ojos llenos de vacía incredulidad."

rin "…"

"Pero la realidad nos alcanza."

show rin negative_crying_superclose
with vpunch

"Rin se desploma hacia adelante como si se estuviese desinflando, y hunde su cara en mi camisa lo más profundo que puede."

"Rin es pesada y ligera como una pluma cuando sostengo su peso."

"Ella realmente no solloza o grita, solo se inclina en mí, dejando que su lágrimas quemen a través de mi camisa hacia la piel debajo."

"Y se lo permito, llevando mi mano alrededor de su hombro en un torpe abrazo que no hace nada para consolarla."

"Puedo sentir las vertebras de Rin en las yemas de mis dedos, como duros y dentados recordatorios de cuán mal se encuentran las cosas."

"Sus delgados hombros temblando en mi palma son un espectáculo digno de dar pena, y la angustia de ser parte de la causa de la tristeza de Rin sigue desgarrando mi corazón."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\n\n\nHacer llorar a una chica es lo más despreciable que puede hacerse."

n "\nIncluso a Rin. Especialmente a Rin."

n "\nDetrás de ese velo de indiferencia, Rin es solo un ser humano, también."

n "Igual de confundido, asustado y perdido como el resto de nosotros."

n "La mayor parte del tiempo parece que no hay razón ni propósito de lo que Rin hace y dice, pero por única vez, creo que realmente entiendo cómo se siente ella."

n "\n\nPero ninguna palabra puede expresarlo, y ninguna palabra puede mejorarlo."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear

show bg school_nomiya:
    "bg school_nomiya_ss" with Dissolve(8.0)
show rin negative_crying_superclose:
    "rin negative_crying_superclose_ss" with Dissolve(8.0, alpha=True)
with None

stop music fadeout 5.0

n "\n\n\n\n\nY así nos quedamos sin palabras, esperando en silencio a que sus lágrimas se acaben."

n "El tiempo pasa agonizantemente lento, incluso las letárgicas motas de polvo flotando en el aire parecen detenerse por completo."

n "El obligatorio reloj de pared hace tic-tac distractoramente sobre la puerta."

n "Decido no contar los segundos, porque los haría sentir más largos."

n "\n\n…"

play music music_serene fadein 9.0

nvl hide dissolve
nvl clear

show rin basic_crying_superclose_ss
with charachange

window show

"Finalmente Rin se mueve un poco y, aún ahogándose a sí misma en mi pecho, murmura sobre mi camisa."

rin "Déjame estar aquí por un tiempo."

show rin negative_crying_superclose_ss
with charachange

rin "Por favor, Hisao."

rin "Solo dame un poco de tiempo."

"Un tranquilizador diluvio se propaga por mi consciencia, el conocimiento de que aunque estar aquí para Rin es todo lo que puedo hacer por ella, eso es todo lo que ella quiere en este momento, aun después de todo lo que hemos pasado."

hi "Claro."

"Y así se queda allí."

"Pero aun así no puedo obligarme a acercarla más hacia mí para poder abrazarla apropiadamente."

"Es porque hacerlo solo me haría sentir tan triste que no sé si podría soportarlo."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\nLa idea de que probablemente nunca seamos realmente capaces de convertirnos en lo que queremos ser para el otro se cristaliza en mi mente como una iluminación tan dura como diamante."

n "Una punzada atraviesa mi corazón como un choque eléctrico."

n "Es doloroso."

n "Esta claridad… lastima."

n "¿Qué podemos ser para el otro? ¿Qué significado tiene el que nos aferremos desesperadamente el uno al otro aunque parezca ser inútil?"

n "¿Qué debería decirle a Rin? ¿Cómo hacerla sentir mejor?"

n "No sé ninguna de esas cosas, y tengo miedo de que saberlas únicamente lastimaría más."

n "A la fuerza, empujo todo ello fuera de mi mente porque no quiero estar pensando en verdades dolorosas."

n "Mis pensamientos se tranquilizan pronto, la tristeza se dispersa hasta que todo lo que queda somos Rin y yo y la tierna sensación de su calidez y suavidad en mi pecho."

nvl clear

n "\n\n¿Cuándo fue que me enamoré de ella?"

n "No puedo recordarlo, pero estoy seguro de que fue mucho antes de sentir el cálido toque de sus labios sobre los míos, en la tarde color naranja cuando ella estaba enferma de gripe y yo fui a verla por razones poco claras."

n "Su actitud despreocupada, el aire de alteridad a su alrededor, todas las cosas que hacen de Rin ella misma… aquellas cosas me capturaron con fuerza irresistible."

n "La manera en la que ella podía tomar todas y cada una de las cosas dándole solo el valor que ella misma le otorgaba, valorando todas las cosas justamente y sin prejuicio, viendo el mundo como ella quería."

n "Esto es algo que yo nunca podría hacer, y Rin probablemente fue más una musa para mí que cualquier otra cosa jamás lo fue para ella."

n "Ella me parecía tan libre, verdaderamente un espíritu libre. Mientras que yo, preocupándome constantemente de todo, parecía tan inhibido que era casi vergonzoso."

n "Tal vez es por eso que me aferré con tanta fuerza de Rin, tratando de entrar en su mundo que era tan diferente de mi propia vida sombría."

nvl clear

n "\n\nAntes de que me diera cuenta de ello, esa fuerza irresistible me había jalado peligrosamente cerca de ella, pero resultó ser demasiado ajeno a mí."

n "Y me había olvidado de Newton, de entre todas las cosas."

n "La fuerza gravitacional es inversamente proporcional al cuadrado de la distancia entre los objetos."

n "Así que si dos personas sienten algo por la otra…"

n "Je."

n "Aunque los sentimientos no son gobernados por las constantes universales, no puedo evitar pensar que por algún tiempo ya he sido un satélite del planeta intensamente brillante de Rin."

n "\nPlaneta Rin."

n "\nEl pensamiento casi me hace reír, ella en verdad parece ser de otro planeta algunas veces, menos la piel verde y posiblemente algunos tentáculos."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

show rin negative_sad_close_ss
with charadistant

window show

"Quizás a causa de mi risa contenida, Rin se aparta y la dejo ir, sintiendo el frío cuando su calor se ha ido, y un poco de vergüenza por dejar a mis pensamientos correr sin control de esa manera."

"Le doy crédito de ello a Rin siendo una mala influencia para mí, a la vez que me siento contento de que ella no puede leer los pensamientos en realidad."

"Las lágrimas amargas de Rin se han secado, y ella se ve un poco más como sí misma de nuevo."

show rin basic_sad_close_ss
with charachange

"Aunque el aspecto perdido en sus ojos sigue ahí. Su mirada se pasea alrededor sin descansar antes de detenerse en mí."

rin "¿Qué acaba de pasar?"

rin "¿Puedes decirme?"

hi "¿Qué? ¿De qué hablas?"

show rin basic_upset_close_ss
with charachange

rin "Lloré."

"Dice eso dudándolo, como si no creyera en sí misma."

hi "Sí…"

"…"

"Sigue mirándome, como si suplicara por orientación para que no tuviera que sentirse tan perdida."

"…"

show rin basic_sad_close_ss
with charachange

rin "¿Por qué?"

hi "Estabas triste."

hi "¿Es eso lo que querías que dijera? Pero, ¿no es eso obvio?"

show rin negative_confused_close_ss
with charachange

rin "No lo sé. Se siente raro llorar."

hi "¿Qué? No lo creo. Quiero decir, todo mundo lo hace. Es nor—"

"Me muerdo la lengua antes de terminar mi argumento sobre la normalidad."

"Las normas no aplican a la persona con la que estoy hablando."

show rin negative_worried_close_ss
with charachange

rin "Siempre se sintió tan mal, diferente de lo que hay dentro de mí. Como si no pudiera saber qué es lo que siento."

rin "Así que empecé a pensar que tal vez no sé qué es lo que siento. Tal vez soy yo quien está mal—"

rin "Pensé ese tipo de cosas."

show rin negative_sad_close_ss
with charachange

rin "Pensé… que pintar era suficiente porque se sentía como si al menos hiciera eso bien."

rin "Que todo lo que hay dentro de mí pudiera convertirse en una imagen si realmente me esforzaba. Y sí podía."

rin "Pero ya no se siente como si fuera suficiente. Porque si nadie más puede verlo, seguiré estando sola."

show rin basic_absent_close_ss
with charachange

rin "¿Estuvo mal intentar? Todos se enojaron mucho conmigo por eso."

stop music fadeout 6.0

"Rara vez he escuchado antes a Rin decir tanto de una sola vez."

"Una vez que termina, simplemente se calla, viéndose tan neutral que es difícil creer que acabara de decir lo que dijo."

"No sé qué pensar."

"…"

"Rin estaba desesperada por que alguien viera sus pinturas, y de algún modo viera a través de ellas dentro de su alma, que entendiera sus sentimientos…"

"¿Porque… ella sintió que no podía expresarlos de alguna otra manera?"

"¿Cómo puede alguien decir si eso está bien o mal?"

"¿Podría ser que durante todo este tiempo ella ha estado tratando de alcanzarme como yo he estado tratando de alcanzarla a ella?"

"…"

"Me siento en un banco para pensar, y para descansar mis piernas que nos mantuvieron a los dos de pie por un largo rato."

play music music_innocence fadein 12.0

hi "Sabes, cuando leo un libro o veo un cielo estrellado o lo que sea, algunas veces también yo siento algo… profundo, como un… rayos, no sé cómo describirlo."

hi "Pero el instante que trato de ponerlo en palabras siento que pierdo algo, no se siente igual de real, igual de verdadero que como se sentía dentro de mi cabeza."

hi "Se siente un poco falso. Maldición, incluso lo que acabo de decir se sintió falso."

"Le ofrezco una sonrisa que se supone ser entre graciosa y autocrítica, pero Rin no reacciona."

hi "De cualquier modo…"

hi "Puede ser que nadie puede jamás expresar sus verdaderos sentimientos de manera que otros entiendan."

hi "La realidad no tiene oportunidad de compararse con lo que alguien tiene dentro de su cabeza."

hi "Nada puede igualarlo. Ni siquiera tus pinturas, excepto tal vez para ti."

hi "Pero supongo que tú no puedes mantener todo dentro, entonces explotarías realmente."

hi "Lo que estoy tratando de decir es… no creo que esté mal expresar tus sentimientos, aun si usas la pintura como tu conducto."

hi "Tú simplemente no puedes esperar que la gente te comprenda mejor que si lo hubieras hecho de cualquier otra forma."

hi "De hecho, no puedes esperar que la gente te comprenda en absoluto."

hi "Es porque todo es tan subjetivo. Tú ves el mundo de tu manera, pero es diferente del de todos los demás."

show rin basic_sad_close_ss
with charachange

rin "¿Pero no es eso terrible?"

hi "Supongo que lo es, de cierto modo."

"…"

show rin relaxed_doubt_close_ss
with charachange

"Ella frunce el ceño, viéndose probablemente tan afligida como puede. Que no es mucho, pero suficiente para que yo entienda que Rin no se encuentra especialmente contenta."

rin "Creo que me puede hacer sentir triste, después de todo."

hi "Sí. Lo sé."

hi "Desearía poder hacer algo para remediarlo."

"No creo que suene amargado, aunque lo esté, un poco."

"Este es mi problema. No puedo ser lo que Rin quiere para sí. Y por la misma razón, ella tampoco puede hacer lo mismo por mí."

"…"

show rin negative_worried_close_ss
with charachange

"Ella hace una cara complicada, cuidadosamente tratando de escoger las palabras que quiere decir."

"Así que Rin tiene momentos en los que le es difícil decir algo, también."

show rin basic_sad_close_ss
with charachange

rin "No hay más remedio, creo."

show rin basic_absent_close_ss
with charachange

rin "… Pero… si tú dices eso…"

show rin basic_awayabsent_close_ss
with charachange

rin "Me hace sentir un poco mejor."

"…"

"Es gracioso cómo cosas aparentemente irrelevantes son las más significativas en momentos como este."

"Como la voz de Rin que suena tan tan baja, apenas audible cuando dice algo."

"Y cómo incluso su corto flequillo puede cubrir sus ojos cuando mira hacia abajo."

show rin basic_blush_close_ss
with charachange

"Y cómo no puede cubrir el color rojo creciendo en sus mejillas hasta la punta de sus orejas."

"Se convierten en un tono de rojo muy interesante."

"Un silencio ensordecedor le sigue."

"Es muy incómodo, como si hubiese visto algo que no debería de haber visto, aun si no fue a propósito."

"No sé qué decir, pero sigo sintiéndome como si debería saberlo."

"Ella tampoco sabe."

"De cualquier modo, se siente como si no hubiera un impulso que perder aun si nos quedáramos en silencio."

"Como si tuviésemos alguna conexión rara sin palabras que seguiría de igual manera."

show rin relaxed_nonchalant_close_ss
with charachange

"Rin sigue balanceándose de una pierna a otra sin parar, viendo a todos lados del salón excepto a mí."

"Ella es quien finalmente acaba con el momento."

show rin basic_deadpan_close_ss
with charachange

rin "¿Podemos irnos? No quiero estar aquí."

hi "Oh, sí, por supuesto. ¿Adónde?"

"Mi respuesta cubre mi nerviosismo igual de mal como su pregunta cubre el de ella."

show rin relaxed_sleepy_close_ss
with charachange

rin "Tú puedes ir adonde gustes. Yo quiero dormir. No he dormido en realidad por algunos días."

show rin basic_lucid_close_ss
with charachange

rin "Se siente como si hubiera una bandada de mariposas azul claro dentro de mi cabeza. Hace difícil pensar apropiadamente."

show rin basic_deadpannormal_close_ss
with charachange

rin "Del tipo que piensas que es demasiado azul para realmente existir, como las pantaletas de Emi esta mañana."

show rin negative_spaciness_close_ss
with Dissolve(0.1)

show rin basic_absent_close_ss
with Dissolve(0.1)

show rin negative_spaciness_close_ss
with Dissolve(0.05)

show rin basic_absent_close_ss
with Dissolve(0.05)

show rin negative_spaciness_close_ss
with Dissolve(0.05)

show rin basic_absent_close_ss
with Dissolve(0.05)

show rin negative_spaciness_close_ss
with Dissolve(0.1)

show rin basic_deadpannormal_close_ss
with Dissolve(0.2)

"Ella sacude la cabeza, y casi espero que un par de morfos color azul ultramar salten de sus orejas."

show rin basic_deadpanamused_close_ss
with charachange
"Una pequeña sonrisa tira hacia arriba las comisuras de sus labios."

rin "Eso me recuerda. El azul, no las pantaletas."

show rin basic_deadpandelight_close_ss
with charachange

rin "La palabra para una bandada de mariposas es enjambre. La busqué."

"Eso hace que mis cejas se alcen formando un arco inquisitivo."

hi "¿Por qué no la usas, entonces?"

show rin basic_absent_close_ss
with charachange

rin "Me gusta más la otra palabra."

"¿Entonces para qué buscarla en primer lugar?"

hi "Entonces deberías de usarla, ¿no?"

show rin basic_awayabsent_close_ss
with charachange

"Ella asiente y guarda silencio, su mirada escapando de la mía hacia un lado, atraída por el naranja oscuro de la luz refractándose por las ventanas."

"Nos quedamos así por un momento: yo silenciosamente viéndola a ella viendo silenciosamente por la ventana."

hi "Oye… ¿ya te encuentras bien?"

show rin basic_absent_close_ss
with charachange

"Me echa un vistazo desde el rabillo del ojo, viéndose melancólica de nuevo. El reflejo de la luz del sol no delata más de sus sentimientos internos."

rin "Necesitaré pensar en eso."

"Quiero continuar con esta conversación, aferrándome a ese pequeño indicio de esperanza que finalmente ha revelado que existe."

show rin basic_awayabsent_close_ss
with charachange

"Pero Rin está viendo fuera de la ventana tan distraídamente que sé que no me responderá de ningún modo que tenga sentido."

"Es como algún tipo de mecanismo de defensa suyo, para evitar ser sensata."

"Su mente es como una mariposa en sí misma, siempre revoloteando por algún lugar cuando sea que es provocada."

"Justo cuando pensé que podía ver detrás de su velo, ella salta fuera de mi alcance de nuevo."

"Tal vez simplemente es así como es Rin."

"Tal vez eso es algo que debería solo de aceptar para obtener un poco de paz interior."

hi "Está bien."

hi "Te acompañaré a los dormitorios, entonces."

show rin basic_absent_close_ss
with charachange

rin "Gracias."

show rin basic_lucid_close_ss
with charachange

rin "En verdad."

stop music fadeout 12.0

scene bg school_hallway3
with locationchange

"Los pasillos vacíos de la escuela, carentes de sus estudiantes se sienten muy solitarios."

"Menos de una hora después de que comenzaran las vacaciones de verano, el edificio parecía desierto, y todo lo que se entromete con la quietud son nuestros pasos."

"El cambio es súbito, pero muestra cómo el edificio es tan solo un cascarón vacío, muerto sin sus estudiantes y maestros."

"Es como si la escuela se hubiera convertido en un mundo privado solo para nosotros dos, un lugar desolado lleno de silencio y polvo de tiza."

scene bg school_staircase2_ss
show rin relaxed_sleepy_close_ss at twoleft
with locationchange

rin "Creo que tengo que cambiar."

"Ella dice eso de la nada mientras bajamos por las escaleras desde el tercer piso, todavía logrando sentirse como si estuviese reflejando lo que estaba pensando apenas antes."

hi "Eso es lo que la gente debe hacer, algunas veces."

window hide
nvl clear
nvl show dissolve

n "\n\n\n\n\n\n\n\nEso es lo último que nos decimos el uno al otro ese día, aun si habría tanto de qué hablar."

n "E incluso esas palabras se ahogan en el silencio que lo abarca todo, desapareciendo en el aire enrarecido como si nunca hubiesen sido dichas."

nvl clear
nvl hide dissolve

$ suppress_window_before_timeskip = True

scene black
with dissolve



label es_R41:

play music music_dreamy fadein 2.0

scene bg school_dormhisao_rn
with charachange

$ renpy.music.set_volume(0.4, 0.0, channel="ambient")
play ambient sfx_rain fadein 1.0

"El primer día de las vacaciones de verano es una decepción."

"Me desperté. El agua bajó desde el cielo plomizo en proporciones bíblicas."

"Era optimista en ese momento."

"Una llovizna rápida, pensé. Torrentes de lluvia por unos minutos, después se va."

show rain normal behind bg
with None

"No hay tal suerte."

$ renpy.music.set_volume(0.7, 1.0, channel="ambient")

hide bg
show bg misc_sky_rn as bg2 behind rain
show hisaowindow
with locationchange

"El agua de lluvia cae a raudales sin cansancio desde el cielo azul grisáceo fuera, corriendo por el vidrio de mi ventana en pequeños ríos y riachuelos, juntándose para formar estanques en miniatura en las aceras."

"Igual que lo ha estado haciendo por las últimas dos horas y media."

$ renpy.music.set_volume(0.4, 1.0, channel="ambient")

scene bg school_dormhisao_rn
with charachange

"Así que he estado entre limpiar sin ganas y leer sin ganas un libro, empacando mis cosas a ratos cuando me aburro de las primeras dos."

"El clima arrastra mis ánimos por los suelos, haciendo más difícil el hacer algo apropiadamente."

play sound sfx_impact2

"Algo chocando contra mi puerta me saca de mi apatía."

"Espero que no sea Kenji y su loca línea de bolos bajo techo."

"…"

"No escucho más sonidos del corredor hasta que camino hacia la puerta y la abro."

play sound sfx_dooropen
$ renpy.music.set_volume(0.2, 1.0, channel="ambient")
stop music fadeout 2.0

scene bg school_dormhallway
show rin basic_absent
with locationchange

"Rin."

"Desearía que verla evocara algo más de emoción en mí, pero para empezar, estoy demasiado sorprendido de que ella haya venido a verme y para continuar, está empapada."

"La blusa de su uniforme está mojada y ella está de pie sobre un charco hecho por ella misma."

"Gotas de agua resbalan por su corto flequillo y se deslizan por su nariz hasta caer desde la punta."

"Una.{w=0.7} Por.{w=0.7} Una."

hi "Ahh… hola."

hi "¿Cómo te sientes?"

show rin basic_deadpannormal
with charachange

rin "Medio normal."

play music music_rin fadein 2.0

"Dejando de lado la relativa cuestionabilidad de su expresión, ella sí que no se ve muy bien."

hi "Estás toda mojada."

show rin basic_absent
with charachange

rin "Es porque vengo de afuera. ¿Sabes eso?"

hi "¿Por qué estarías afuera? Está lloviendo a cántaros, por si no lo has notado."

show rin basic_deadpancontemplation
with charachange

rin "No lo he notado. Aunque está lloviendo bastante fuerte. Estaba dando un paseo."

hi "¿Es esto a lo que llamas “regodearse en la autocompasión”?"

show rin basic_deadpanupset
with charachange

rin "¿Crees que doy pena?"

hi "No, quise decir que tú piensas eso."

show rin basic_awayabsent
with charachange

rin "No lo hago, y la lluvia no es algo triste."

show rin basic_absent
with charachange

rin "¿Acaso nunca caminas en la lluvia?"

hi "Sí, pero solo con el equipo apropiado, como un paraguas."

show rin basic_lucid
with charachange

rin "Solo necesitas imaginar que tienes un paraguas azul con rayas blancas."

hi "Puede que sea difícil cuando hay lluvia cayendo sobre mi cabeza."

show rin basic_deadpannormal
with charachange

rin "Solo imagina con más fuerza."

"…"

"Sí, definitivamente ha vuelto a la normalidad."

"Esos comentarios semisarcásticos y desconsiderados que realmente me hacen enojar aunque ella no lo haya querido, esa mirada ida y vacante que siempre espera recibir más de lo que da."

"Es tan… como ella."

show rin basic_deadpan
with charachange

rin "Puede que necesite entrar. Necesito un poco de ayuda con esta agua y prendas que llevo."

"Mi cerebro pronto resuelve la ecuación, y tropiezo con mis palabras, una clara muestra de contraste a la invitación despreocupada de Rin."

hi "Pero, Emi…"

show rin basic_lucid
with charachange

"Rin sacude la cabeza con vehemencia, haciendo que gotas de agua se esparzan por todas partes."

rin "Se fue."

show rin basic_awayabsent
with charachange

rin "Además ella solo se preocuparía y armaría un alboroto hasta que ya no pudiera preocuparse o alborotarse más, lo que siempre toma un tiempo fastidiosamente largo."

show rin basic_absent
show rain normal behind bg
with charachange

rin "Es de hecho más largo de lo que quiero escucharla quejarse, y pensé que probablemente tú no eres del tipo que hace un escándalo."





$ renpy.music.set_volume(0.4, 1.0, channel="ambient")

hide bg
show rin invis_close at center
show bg misc_sky_rn as bg2 behind rain
show hisaowindow behind rin
with locationchange

show rin relaxed_nonchalant_close_rn:
    ypos 1.1
with Dissolvemove(0.5)

stop music fadeout 8.0
play sound sfx_rustling

"Se deja caer sobre mi escritorio con un sonido húmedo."

"Su ropa empapada moja mi escritorio y todo lo demás pero a ella no le importa."

"…"

hi "Está bien, está bien. Te ayudaré."

hi "Tengo una toalla en algún lugar. ¿Quieres ropa seca? ¿Está bien un uniforme? Soy más alto que tú, pero…"

show rin basic_lucid_close_rn
with charachange

rin "Todo está bien."

show bg school_dormhisao_rn
with locationchange

"Buscando un poco encuentro un uniforme fresco y una toalla suave en las profundidades de mi armario."

hide bg
with locationchange

"Con la toalla en una mano y el uniforme en la otra, me doy vuelta hacia Rin otra vez, inseguro del siguiente paso."

"Hay algo mal conmigo, un tipo normal simplemente—{w=1.0}{nw}"

show rin basic_absent_close_rn
with charachange

rin "Deja de preocuparte. No es problema."

"Probablemente pudo ver justo a través de mi rostro titubeante."

"Como si fuese completamente transparente para ella."

"Hago a mi ansiedad a un lado y me concentro en los ocho botones alineados en su blusa, justo como en mi camisa."

"Solo el primer botón es un obstáculo, y después de terminar con él desabotono los demás con manos un poco menos temblorosas."

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")
play music music_heart fadein 0.5

scene ev rin_wet_pan_down:
    center
    yalign 1.0 subpixel True
    easein 20.0 yalign 0.0
with whiteout

"Arrojando a un lado la blusa empapada, revelo el pálido cuerpo superior de Rin, envuelto únicamente en un sostén azul claro lo cual me recuerda al instante que ella dijo era su color favorito."

"Trato de no pensar demasiado en… cosas, pero es difícil no ver su cuerpo con lo que solo puedo considerar como sentimientos encontrados."

"No sé qué pensar de esto, así que solo la miro. Rin se ve… quebradiza."

"Es como un cascarón, algo frágil manteniéndose apenas unido."

"Sus costillas, cada una de ellas visible bajo su pálida piel, se mueven de arriba a abajo al ritmo de su respiración."

"Rin siempre me pareció como alguien muy delgada, pero ahora me doy cuenta de que el maníaco periodo creativo antes de la apertura de la exhibición pudo haber causado que perdiera peso."

"¿Comió apropiadamente y suficiente? Definitivamente no y probablemente no."

"Este feo y sin embargo hermoso mínimo de un cuerpo humano que le pertenece a alguien que me importa es una contradicción de la estética misma, extrañamente propio de ella."

"Mis ojos siguen su clavícula hacia su hombro y abajo por el brazo hasta su abrupto final."

"No, es menos que el mínimo, pienso con una pasajera sensación de tristeza y un poco de culpa por pensar de esa manera."

scene ev rin_wet_arms:
    center
    xalign 0.0 subpixel True
    linear 20.0 xalign 1.0
with flash

"Sus brazos, degenerados hasta casi nada más que hueso y piel debido a la falta de uso, se ven muy cortos ahora que las largas mangas de su uniforme no los cubren:"

"La falta de cualquier reacción negativa de mi parte me hace pensar que, de hecho, me he acostumbrado bastante a las varias anomalías físicas de mis compañeros."




"Siempre me pregunté por qué Rin mantiene las mangas de sus blusas largas, solo atándolas en un nudo simple donde estaría el codo."

"Parece poco práctico, pero por otro lado ella no es exactamente el pináculo de la practicidad."

"Tal vez le guste, tal vez es de algún modo importante para ella. Tal vez no hay ningún significado profundo en ello."

"Siento ganas de preguntar, y casi lo hago, pero el estado miserable de Rin requiere una atención de más alta prioridad."

scene ev rin_wet_face_down:
    center
    yalign 0.0
with flash

"También ha dejado de hablar, después de que se nos acabaran los ásperos saludos."

"Supongo que no hay necesidad de charlar, entonces."

scene ev rin_wet_towel_down
with charachange

"Recojo la toalla de la cama y la envuelvo alrededor de su cabeza, arrugándola toda alrededor de su cabello hasta que la mayoría del agua, con esperanza, sea absorbida por la tela."

scene ev rin_wet_towel_up
with charachange

"Se asoma para verme por debajo de la toalla, mirándome con ojos impasibles."

"Parece que quiere decir algo sin decirlo."

"Es ese tipo de mirada."

"Pero no puedo leer qué es en lo que está pensando en su cara, así que simplemente sigo batallando con la toalla alrededor de sus hombros y cabello."

"El silencio es opresivo, aterrorizante."

"La comunicación entre nosotros súbitamente ha sido reducida a los movimientos de mis manos y de la toalla, y de Rin meciendo su cuerpo hacia enfrente y atrás."

"Mi respiración entrecortada y la suya silenciosa, tratando de encontrar algún ritmo en común que simplemente no hay."

"Creo que puedo escuchar sus latidos, o tal vez son solo los míos duplicados."

"Cuando hago a un lado un solitario mechón de cabello de su oreja, Rin súbitamente presiona su mejilla contra el dorso de mi mano."

"El contacto es eléctrico, una descarga de corriente se dispara dentro de mí."

scene ev rin_wet_towel_touch
with charachange

"Ya sea que busca consuelo, calor o simplemente mi tacto, no podría saberlo, pero no puedo evitar tocarla de vuelta, acariciar su suave mejilla con mi mano."

"Y con ojos cerrados, ella me besa, en los dedos, contando los nudillos con sus labios…"

"Me siento triste más allá de mis capacidades expresivas."

"Aquí estamos, un chico y una chica, ambos enamorados o algo similar a ello el uno del otro, o tal vez no… sin embargo…"

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\nAlgo está roto, puedo sentirlo dentro de mí y dentro de Rin; en el modo en que nuestras miradas apenas se rozan entre ellas, rehuyendo del contacto; en su postura cerrada y tímida y en mi modo de tocarla como si fuese una muñeca de porcelana, asustado de romper su delicada forma."

n "En cómo estamos más cerca de lo que hemos estado, y aun así no me siento feliz. Es como ayer."

n "¿Cuándo fue que la ternura y el desamparo se convirtieron en una misma palabra, y las muestras de afecto comenzaron a invocar únicamente anhelo…? ¿Cómo… por qué fue que terminamos así?"

n "“No, no respondas eso”, me gustaría decirme a mí mismo, pero pelear con la omnisciencia de la consciencia de uno mismo es un caso perdido."

n "Igualmente, estoy aquí, y Rin está aquí, y se siente como si ella podría ser capaz de resolver cualesquiera que sean sus problemas."

n "Y si ella puede, ¿por qué no podría yo? ¿Por qué no podríamos nosotros?"

n "Se siente como si dar ese paso sea demasiado, demasiado difícil, demasiado inseguro."

n "Así que, por ahora, todo lo que puedo hacer es secarla para que no pesque un resfriado de nuevo."

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")
$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

scene ev rin_wet_face_up
with charachange

window show

"Le cepillo la cabeza con las manos, tratando de acomodar el cabello que se rehúsa a ser acomodado aun estando mojado."

"Un par de oscuros ojos vidriosos siguen todos mis movimientos."

hi "¿Los pantalones también?"

scene ev rin_wet_face_down
with charachange

"Ella asiente como respuesta, recargándose hacia atrás y abriendo las piernas, con un gesto grotescamente seductor que provoca a un desagradable sentimiento trepar por mi espina de arriba a abajo como una mala premonición."

"Sin embargo, no es suficiente para contenerme, mientras el silencio comienza a hacerme sentir separado de mí mismo."

"Me muevo automáticamente, sin siquiera pensarlo aun si debería; debería hablar con ella de esto, o por lo menos de algo."

"El silencio es un encanto, un pacto que nos ha atado a este mundo privado hecho del sordo sonido de la lluvia y el suave sentir de su piel en mis dedos."

"El botón de sus pantalones está abrochado firmemente, pero se abre con sorprendente facilidad."

"Quitárselos es difícil, principalmente porque se está sentando en ellos, sin intención de levantarse para facilitar mi tarea."

scene unlock_evh rin_h2_pan_surprise
show evh rin_h2_pan_surprise:
    xalign 0.5 yalign 0.0
with whiteout

"Me arrodillo incómoda y estimuladoramente entre sus piernas para poder secar rápido sus pies, recordando que son tan importantes para ella como las manos son para mí."

"A medida que la voy secando con la toalla de sus tobillos hacia arriba, Rin roza mi mejilla con su muslo y me da un golpecito en la espalda baja con su talón para hacer que me acerque más."

"Volteo hacia arriba para encontrarme con su mirada silenciosa que estaba esperando a que volteara."

"Esa mirada modesta y a la espera parece decir que el siguiente paso depende de mí."

"…"

"Brevemente rozo el interior de su muslo con mi mano."

show unlock_evh rin_h2_pan_away
show evh rin_h2_pan_away
with charachange

"El toque la hace dar un grito ahogado, como si estuviese tratando de contener su aliento."

"¿Qué tal si hago esto, entonces?"

show unlock_evh rin_h2_pan_closed
show evh rin_h2_pan_closed
with charachange

"El pequeño beso que coloco en su muslo es suficiente para hacer que Rin pierda su compostura, que cierre los ojos, que chille de manera casi inaudible."

"… ¿Es eso lo que tú también quieres? ¿Estaría bien? ¿El dar ese paso?"

show evh rin_h2_pan_closed:
    subpixel True
    acdc_warp 8.0 yalign 1.0
with None

"… ¿Qué tal si…? ¿Tal vez si…?"

"Pensamientos nebulosos flotan en algún lugar en el interior de mi mente dispersa."

"De algún modo, toda esta situación hace que pensar sea muy difícil, como si mi cabeza estuviese colmada de relleno de algodón."

"Pero así está bien. Parece que pensar no es algo que necesitemos en este momento."

label es_R41h:
show evh rin_h2_nopan_closed:
    yalign 1.0
with Dissolvemove(0.5)

$ renpy.music.play(music_heart, fadein=0.5, if_changed=True)

"Por la gracia de una cantidad mucho menor de tela, quitarle las pantaletas a Rin es considerablemente más fácil que sus pantalones."



"Desaparecen más allá de mi campo visual, deslizándose hacia algún lugar bajo sus piernas."

"Parece que hice un trabajo deficiente con la toalla, ya que las piernas de Rin siguen húmedas a causa del agua."

"Bueno, como sea."

show evh rin_h2_hisao_closed
with charachange

"Guiado por el instinto más que por el raciocinio, me acerco más y saboreo el distinto tipo de humedad."

"Ella responde a mí, a los lentos movimientos de mi lengua sobre su piel, a mis besos sobre su carne."

"Sus músculos se tensan y relajan al ritmo, como si lo que estuviese haciendo fuese incómodo."

"Escuchar a Rin tratar de no hacer ruido cuando la chupo es… irreal."

"Toda esta mañana ha sido tan irreal, como la intangibilidad surrealista de un sueño en el despertar."

"No puedo creer que esté haciendo esto, a ella, ahora. Pero me dejo llevar por la corriente."

"Además, el punto de no regreso fue hace miles de kilómetros."

"Me muevo alrededor, tratando de hacerle cosas, de encontrar los lugares donde yacen sus debilidades, provocarla, volverla loca de placer porque quiero, quiero hacerle esto a ella."

"Pero no chilla, no se retuerce, tal vez porque no puedo hacer enloquecer a Rin más de lo que ya está, sin importar qué haga."

"Su aliento pesado e irregular mezclado con gemidos ininteligibles son los de una lunática, pero no los causo yo."

"Yo únicamente los hago salir de ella."

"Ella se humedece más y más, y yo bebo de ella, sintiendo el calor creciendo dentro de mí."

"Trato de alcanzar sus lugares más profundos, de sentir todo lo que pueda de ella de esta manera."

"Cada acción mía se encuentra con una reacción diferente, pero todas ellas son a causa de lujuria pura."

show evh rin_h2_hisao_closed:
    subpixel True
    acdc_warp 16.0 yalign 0.0
with None

"Rin está perdida en el deseo, dispuesta a permitir que cualquier cosa le suceda si lo hago en este momento."

"Ella llega más y más cerca del momento de descarga, pero el camino a ello es una pendiente ascendente de demencia."

"Aun así, ella va hacia allá."

"Los músculos no se relajan entre las olas de espasmos extasiados."

"Rin solo se tensa cada vez más, contrayéndose tanto que debe ser físicamente doloroso, pero no me detengo."

"Sigo haciéndolo, y sé que ella también lo quiere, ella quiere desesperadamente que le haga esto."

"Una pierna me rodea el hombro y me lleva más cerca, tan cerca que pienso que voy a ahogarme."

"Continúo porque es la única posibilidad."

stop music fadeout 8.0
stop ambient fadeout 12.0

"Al momento en que presiono ese botón que la hace jadear tratando de respirar, tensando su pierna de un tirón sobre mi espalda, perdiendo la cabeza en la sensación…"
"… en ese preciso momento parezco olvidar todo lo que debía ser, todo lo que debería de ser."

"Todo lo que sé es que ella vino aquí y… creo que había una toalla en algún momento, también."

"Nada de eso importa, todo lo que importa es esto, lo que tenemos ahora."

"Su orgasmo se dispara también a través de mí, excitándome de un modo completamente nuevo."

"Me hace sentir ansioso, nervioso. Molesto."

show evh rin_h2_hisao_away:
    yalign 0.0
with Dissolvemove(0.5)

"A medida que relaja su cuerpo, trato de besarla ahí abajo otra vez, pero la asusta, haciéndola brincar."

show evh rin_h2_hisao_surprise
with charachange

rin "No… Hisao… Suficiente."

rin "Ven aquí."

scene bg school_dormhisao_rn
with locationchange

"Me pongo de pie para remover la última prenda que lleva Rin."

"Ella se recarga sobre mí para recuperar su aliento, haciéndome cosquillas con el aire caliente exhalado dentro de mi camisa."

"Ciegamente estiro el brazo atrás de su espalda para tratar de buscar a tientas debajo de sus omóplatos, para encontrar el mecanismo que abrocha el sostén."

"Se abre más fácil de lo que pensé, cayendo en alguna parte del suelo."

play music music_romance fadein 10.0

scene ev rin_pair_base_clothes
show rp_hisao normal at truecenter
show rp_rin normal at truecenter
with whiteout

"Su piel desnuda sobre mí es una sensación tan maravillosa que quiero tener más de ella, y lo hago, abrazándola."

"El cabello de Rin huele a lluvia, y me doy cuenta de que ya no oigo el sonido del agua cayendo."

"Es algo que me hace volver en mí. El cojín que nos envolvía en nuestra propia realidad se ha ido, y me percato más claramente de qué es lo que está sucediendo."

show rp_hisao frown
with charachange

hi "Sabes, esto realmente no es algo que los amigos deberían de estar haciendo."

"Le susurro, una vez más notando cómo algunas veces una cosa simple como hablar puede ser tan difícil."

show rp_rin talk
with charachange

rin "¿Dejarás de ser mi amigo?"



"Eso no fue lo que quería decir, pero su tono serio y las capas de connotaciones detrás de la pregunta de Rin me hacen dar una pausa."

show rp_hisao smile
with charachange

hi "Nah."

show rp_rin smile
with charachange

rin "Yo… creo que podría estar bien. Aun si lo hicieras."

"La abrazo y le sonrío a su cabello, entendiendo perfectamente a Rin por primera vez."

show rp_rin frown
with charachange

rin "Estás mojado."

"Los remanentes de agua sobre su piel se han absorbido en mi camisa."

"De algún modo, aun sus observaciones de lo obvio me hacen sonreír en este momento."

show rp_hisao normal
with charachange

hi "Tienes razón. Lo estoy. Pero eso es tu culpa."

show rp_rin normal
with charachange

rin "Quiero verte."

play sound sfx_rustling

scene ev rin_pair_base
with charachange

"Obedezco, dando un paso atrás para desabotonar mi camisa, mucho más rápido que cuando lo hice con los botones de Rin."

"Una repentina sensación de prisa me arremete, incentivándome a que me apure."

"Cada segundo que no estoy tocando a Rin es un desperdicio, una oportunidad perdida."

"La hebilla de mi cinto prueba ser un obstáculo a pesar de mi habilidad de abrirlo en un abrir y cerrar de ojos en circunstancias normales."

show rp_rin closed
with charachange

"Mientras titubeo con este, no me doy cuenta de que Rin lleva su pie entre nosotros hasta que comienza a trazar mi pecho con su dedo."

show rp_hisao frown
with charachange

"Miro abajo para ver qué es a lo que está viendo…"

hi "Mi corazón…"

"Retrocedo por reflejo, cubriendo el tejido cicatricial en medio de mi pecho."

"Las marcas superficiales que la cirugía que le siguió a mi ataque cardiaco dejó sobre mi cuerpo ya han sanado pero… bueno, no es un espectáculo especialmente bonito aunque no es que sea excesivamente repulsivo."

"Es apenas notable, pero ella definitivamente tiene un ojo para el detalle. ¿Es por esto que dijo que quería verme?"

"Me había medio olvidado de esto a causa de todo este desastre con Rin, pero ahora todo lo desagradable conectado a mi condición surge a la vez, corriendo por mi mente como una inundación repentina."

"Y por Dios todas las historias sobre tipos viejos teniendo ataques al corazón cuando tienen sexo, que tal si…"

show rp_rin talk
with charachange

rin "Hisao."

"…"

"Percatándome de que podría haber arruinado el ambiente, tropiezo para explicarme."

show rp_hisao normal
with charachange

hi "Ah… disculpa, es solo que…"

show rp_rin smile
with charachange

rin "Déjame tocarte."

"Sus ojos son sensuales, seduciéndome al sentarse ahí desnuda sin un rastro de vergüenza. Nunca pensé que Rin podría verse así."

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\nSí, sé que esto no es como debería de ser."

n "Aun si Rin está justo aquí, aun si no debería de haber más preguntas, ni obstáculos, ni esta exasperante sensación de que algo está constantemente mal…"

n "El mismo sentimiento que aprisionó a mi corazón ayer hace su aparición."

n "Estamos juntos. De una manera que es difícil de definir, elude descripción tan obstinadamente como evade el cambio."

n "\n¿Podría estar bien una relación como esta? ¿Podríamos algún día cambiar para acercarnos más?"

n "Aunque permaneciéramos juntos durante toda la eternidad, podríamos nunca encontrar nuestro entendimiento mutuo."

n "Pero no hay tal cosa como la eternidad. Esto puede significar que no estaremos juntos por siempre."

n "Si no son nuestras diferencias, entonces el pasar del tiempo nos apartará con fuerza irresistible."

nvl clear

n "\n\nRin es una criatura del momento, de caprichos e impulsos."

n "\nYo no soy así para nada."

n "\nEste es un hecho que puedo entender muy claramente."

n "Si no es por otra razón, por esta misma debería de aferrarme a este momento. Aun si es el único momento que tendremos, no debería permitirme arruinarlo."

n "Aunque no pueda escapar de mí mismo. Rin tampoco puede, ahora lo sé."

n "\nAmbos tenemos cosas que no podemos dejar ir, cosas en las que no podemos no pensar."

n "Sentimientos que no podemos no sentir."

n "Pero ella se permite desearme sin ningún impedimento. Aquí y ahora."

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")
$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

show rp_hisao frown
with charachange

window show

hi "Lo siento, sabes…"

show rp_rin closed
with charachange

rin "Hisao, realmente tienes que dejar de preocuparte."

"Rin me interrumpe antes de que pueda decir más, lo que es bueno porque no sé qué podría haber dicho."

"Su voz, carente de su usual lejanía, me regaña con suavidad, sin filo."

show rp_rin smile
with charachange

rin "Realmente tienes que aprender a dejar las cosas ir."

"Ella me analiza con tranquilidad, casi de manera calculadora."

"Me pregunto cómo me veo a través de sus ojos."

"Maldición. Son tan verdes que casi lastiman."

"Siempre me han encantado tanto sus ojos, esos misteriosos y cautivadores ojos que siempre se encontraban demasiado inquietos para su propio bien."

"Pero también siempre me sentí intimidado por ellos."

"Sí. Rin es intimidante, en más de una manera y especialmente ahora."

"Ella se encuentra terriblemente lúcida, la piel de gallina delata que tiene frío, o está asustada también."

"Sea como sea, me armo de valor y doy un paso de vuelta hacia Rin, abrazándola para sentirla en mis brazos y para disipar mis dudas."

"Mirar sus gentiles y amorosos ojos parece derretir esas dudas como la última nevada de invierno."

scene evh rin_h_closed
with whiteout

"Ella presiona su cabeza contra mi hombro, buscando un lugar donde descansar, recargándose sobre mí como yo me recargo en ella."

rin "Déjalas ir."

"Sí."

scene evh rin_h_left
with charachange

rin "Deberías de olvidarte de cosas como el futuro y el pasado, no es como si pudieras cambiar ese tipo de cosas."

"Quería decirle algo, pero he perdido mi voz así que tan solo le murmuro algo ininteligible."

rin "Deberías tan solo estar conmigo ahora."

"Quizás entendió lo que quería decir aunque no lo dijera."

rin "Ven aquí."

hi "Estoy aquí."

scene evh rin_h_normal
with charachange

rin "Acércate más."

"Mi cuerpo entero solo piensa en cosas positivas ahora así que lo hago, abrazándola más fuertemente."

scene evh rin_h_right
with charachange

rin "Más cerca."

"Presiono la parte inferior de mi cuerpo sobre ella."

"Ella se tensa un poco. Solo un poco."

scene evh rin_h_closed_close
with characlose

rin "Más cerca."

"Su última súplica es más como una plegaria."

"Solo hay una manera de estar más cerca que esto."

"Con mi mano alcanzo entre nosotros y me guío a mí mismo, hundiéndome dentro de ella."

scene evh rin_h_strain_close
with charachange

"Cada músculo en el cuerpo de Rin se tensa al mismo tiempo."

scene evh rin_h_strain
with charadistant

"Ella no dice nada, ni hace un gesto de dolor, así que empujo más profundamente, finalmente moviéndome hacia afuera."

"Y otra vez. Y ella se mueve conmigo."

"Nuestros movimientos se funden en una hilera continua hacia enfrente y atrás, adentro y afuera."

"Todas las sensaciones se hacen más agudas, amplificadas diez veces."

"Mi cerebro desistió de interpretar toda esta estimulación hace una eternidad, y ahora me quedo sin más opción que sentir todo esto con mi cuerpo entero."

"Es también lo mismo para Rin, lo sé. Puedo verlo. Puedo sentirlo."

"Ella respira con intensidad de adentro hacia afuera, perdiendo toda compostura y gracia, respira cálidamente sobre mi hombro."

"En medio de aquellas frágiles aspiraciones, ella algunas veces me besa con ternura, como si no estuviese segura de cómo hacerlo apropiadamente."

"Pero no hay vacilación."

"Desesperadamente aferrándose a mí, llevándome más cerca para que yo pueda llenarla por completo, se mueve sobre y alrededor de mí, por lo que es difícil decir dónde me detengo yo y ella empieza."

"Lo llevamos con calma, terriblemente despacio, como si tuviésemos todo el tiempo del mundo aunque tengamos solo este momento y nada más allá de este."

"Esa sensación es—{w=0.7}{nw}"

scene evh rin_h_normal_close
with characlose

rin "Espera…"

"Dejo de moverme, ligeramente alarmado."

"Tal vez duela, o…"

scene evh rin_h_right_close
with charachange

"Me mira de un modo en el que realmente no puedo ni empezar a interpretar."

rin "¿Es esto?"

hi "… ¿Eh?"

rin "Dijiste que no tenía que estar sola."

scene evh rin_h_left_close
with charachange

"Sus ojos están llenos de una inocente y aturdida confusión que me hace reír un poco y acariciarle la nuca."

hi "Sí. Esto es a lo que me refería."

hi "Que tengas a alguien al que puedas acudir cuando te empapes bajo la lluvia."

hi "Significa que no estás sola."

hi "Si es que hay una persona así para ti."

scene evh rin_h_closed_close
with charachange

"Ella responde con un beso, recordándome que hemos dejado de movernos sin razón alguna."

"Así que comenzamos nuevamente, casi al mismo tiempo, cada quien reflejando el ritmo del otro."

"Me muevo más rápido, más rápido hacia afuera y hacia adentro, mi sudor se mezcla con el suyo, reluciendo en nuestra piel compartida como diamantes y perlas."

scene evh rin_h_strain:
    truecenter
    zoom 1.2 subpixel True
    easein 20.0 zoom 1.0
with charadistant

"Ella se mueve más rápido, restregándose sobre mí en las convulsiones de nuestro deseo."

"El olor intoxicante de su lujuria, el sentimiento que conecta nuestros cuerpos que hace a la mente desvanecerse, la sensación de todo pensamiento racional siendo drenado de mi mente."

"Todos ellos queman mi consciencia justo como la irresistible sensación en mi cuerpo quema mis instintos."

"A medida que esos sentimientos crecen, Rin no da señales de detenerse."

"Ella curva sus pies detrás de mi espalda baja, forzándome a conducirme más adentro de ella tan profundo como sea físicamente posible, cada milímetro enviando olas a través de mi espina."

"Mi mente se pone en blanco cuando el mundo hace erupción en un destello blanco de brillo enceguecedor."

stop music fadeout 2.0
stop ambient fadeout 2.0

window hide

scene white
with Dissolve(2.0)

$ suppress_window_after_timeskip = True

with Pause(4.0)


label es_R42:

window hide None

scene white
with None

$ renpy.music.set_volume(0.1, 0.0, channel="music")
play music music_timeskip fadein 4.0

centered_b "Presente{fast}" with Dissolve(4.0)

nb "El “presente” es un concepto breve e impreciso en el mejor de los casos.\n"

extend "¿El momento entre el pasado y el futuro?\n"

extend "Eso en verdad no significa nada.\n"

extend "Pensar demasiado en algo que no tiene sentido es una pérdida de tiempo.\n"

extend "Es por eso que vivir a través del presente es la mejor opción.\n"

extend "Además, para nosotros que no podemos prever el futuro y quienes olvidamos el pasado con demasiada facilidad, el presente es en verdad la única prueba de nuestra existencia.\n"

extend "Aunque la existencia seguirá adelante aun si te olvidas de ella por un tiempo, es bueno aprovechar el día por lo menos una vez cada tanto.\n"


centered_alive "De ese modo… puedes confirmar que estás, de hecho…"


show alivetext "De ese modo… puedes confirmar que estás, de hecho…"
with None


show alivetext "De ese modo… puedes confirmar que estás, de hecho… vivo."
with Dissolve(3.0)

$ renpy.pause()

stop music fadeout 4.0

scene bg school_dormhisao
with Dissolve(4.0)

window show Dissolve(2.0)

$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_dreamy fadein 4.0

"Estoy bastante seguro de que la chica que está de pie ahí medio desnuda, mirando por fuera de la ventana de mi habitación, tiene un mejor entendimiento del “presente” que yo."

"En cuanto a mí… bueno, en este momento estoy un poco confundido a causa de mi estado actual, ya que debería de tratar de encontrar mi camisa y no mirarle el trasero a Rin."

"Pero simplemente no puedo dejar de verla."

scene bg misc_sky
show hisaowindow
show rinpan relaxed_nonchalant_close at center
with locationchange

"Ella se encuentra tan cerca del cristal que su nariz probablemente va a dejar una marca."

"Al menos su aliento lo hace, cuando se condensa en el cristal de la ventana enfriado por la lluvia antes de rápidamente desaparecer de nuevo."

"El que me mueva por la habitación para vestirme no saca a Rin de su contemplación, lo cual está bien, en serio. No me molesta el silencio tanto como solía hacerlo."

"Tan solo después de que casi termino de abotonarme mi camisa Rin dice algo, aun sin darse vuelta para verme."

show rinpan relaxed_boredom_close
with charachange

rin "Vamos a alguna parte."

hi "¿Adónde?"

"Únicamente puedo asumir que me está invitando a mí y no al alféizar, pero es una suposición justa."

show rinpan basic_lucid_close
with charachange

rin "Yo sé."

hi "¿Qué?"

show rinpan basic_deadpan_close
with charachange

rin "Ayúdame a vestirme."

show rinpan basic_awayabsent_close
with charachange

rin "Creo que hoy es el día."

show rinpan basic_deadpanupset_close
with charachange

rin "Vamos, ropa."

"Ropa, ropa… qué tono tan impaciente."

"Me agacho para recoger su sostén del suelo donde había caído, desechado en la prisa de desvestirse y olvidado ahí."

"Colgándolo entre mis dedos como un pescado muerto, la misma vacilación que me sujetó cuando estaba desvistiendo a Rin vuelve a treparse dentro de mi cabeza."

"¿Es la intimidad realmente algo tan difícil de manejar para mí?"

show rinpan basic_deadpancontemplation_close
with charachange

rin "Vamos, me lo quitaste sin mayor problema. Esto es lo mismo pero al revés. Es como hablar al revés."

show rinpan basic_deadpan_close
with charachange

rin "Licáf se orep, licífid ecerap."

"Perplejo por su repentina y prodigiosa muestra de capacidad de procesamiento mental, olvido tratar de revertirle sus galimatías."

"Estoy bastante seguro de que no podría cambiarme a hablar al revés con esa fluidez aun con algo de práctica."

hi "Ahh, ¿podrías repetir eso?"

show rinpan basic_lucid_close
with charachange

rin "Licáf se orep, licífid ecerap."

"…"

hi "Entendido. Bien, lo intentaré."

"Rin tenía razón, el mecanismo de cerrado es bastante simple, y logro meter correctamente los ganchitos de plástico en el tercer intento."

hi "Ya está."

show rinpan basic_deadpandelight_close
with charachange

rin "Olratsuja euq seneit aroha."

hi "¿Qué? Por favor deja eso, no hablo enrevesado."

show rinpan basic_lucid_close
with charachange

"Ella sacude su cabeza como si necesitara alejar la manera de pensar inversa con un gesto físico."

"Conozco algunas personas que podrían beneficiarse de ese tipo de habilidad."

show rinpan relaxed_nonchalant_close
with charachange

rin "Me atoré. Ahora tienes que ajustarlo."

hi "¿Ajustar?"

show rinpan basic_deadpan_close
with charachange

rin "Eso es lo que dije."

hi "No, pregunté qué es lo que quisiste decir."

show rinpan basic_lucid_close
with charachange

rin "Tú sabes, para que ellos estén… bien."

"Oh. ¿Bien, dices?"

"…"

"Como no tengo idea de cuándo sus senos suponen estar “bien”, termino moviéndole el pecho por un buen rato sin realmente lograr algo."

"No es que me queje, pero Rin lo hace."

show rinpan basic_deadpanupset_close
with charachange

rin "Emi es mejor que tú en esto."

"Su tono impaciente me hace enojar, aunque en verdad no puedo discutir. Rin de pronto parece tener mucha prisa."

hi "Sí bueno discúlpame, ¿podría eso ser porque ella es una {b}chica{/b} y pueden entenderse, de hecho?"

show rinpan basic_deadpanamused_close
with charachange

rin "No lo creo, ella tiene casi tanto busto como tú."

"…"

stop music fadeout 5.0

hide rinpan
show rin basic_absent_close
with shorttimeskip

"Con su sostén y senos finalmente “bien” como deberían de estar, el resto de su ropa es considerablemente más fácil de poner."

hide rin
with charaexit

"Rin se lanza hacia la puerta aunque su blusa ni siquiera esté abotonada por completo todavía."

"Quedándome con pocas opciones, corro tras ella."

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_soothing fadein 2.0
play ambient sfx_parkambience fadein 0.5

scene bg school_gardens
with locationskip

"Tan pronto como me percato de que nos dirigimos a la entrada lateral que lleva al bosque, creo saber adónde es que Rin quería ir, aunque no podría decir el porqué querría ella ir allá."

"Por otro lado, realmente no puedo asumir que mis suposiciones podrían estar cerca cuando se trata de Rin, ni siquiera para una definición bastante generosa de “correcto”."

$ renpy.music.set_volume(0.6, 0.5, channel="ambient")
$ renpy.music.set_volume(0.8, 0.5, channel="music")

scene bg school_forest1
with locationskip

"El bosque detrás de los muros huele a lluvia, las últimas gotas todavía están cayendo de los arbustos húmedos hacia la tierra a pesar de que la lluvia se haya ido por un rato ya."

"Paseamos con un paso desapresurado que Rin marca, dándome tiempo de apreciar el ambiente tranquilizador."

"Creo que puedo escuchar a Rin decirle hola a por lo menos tres diferentes árboles al pasar caminando frente a ellos, pero lo ignoro, al igual que lo hacen los árboles."

"Me lleva a un camino lateral estrecho que lleva a las colinas, como había supuesto."

scene bg worrytree:
    truecenter
    yalign 1.0
with locationchange

"Me asomo por las copas de los árboles tratando de encontrar un arcoíris, pero parece no haber uno."

"Es el clima perfecto para los arcoíris. El sol brilla bajo, y la lluvia acabó hace poco."

"Bueno, como sea."

$ renpy.music.set_volume(0.7, 0.5, channel="ambient")
$ renpy.music.set_volume(0.6, 0.5, channel="music")

scene bg school_forest2
with locationchange

"Bajo los ojos de las copas de los árboles para ver la delgada espalda de la chica que está trepando la colina lentamente, sin perder su equilibrio."

"Algunos pasos del camino frente a mí, pero aún dentro de mi alcance."

"No creo que algún día pueda alcanzar a un arcoíris, pero alcanzar a Rin… parece menos imposible de lo que solía parecer."

$ renpy.music.set_volume(1.0, 0.5, channel="ambient")
$ renpy.music.set_volume(0.4, 0.5, channel="music")

scene bg school_hilltop_border_summer
with locationchange

"El cielo despejado que nos recibe desde lo alto del prado se ve vasto y hermoso."

"Un fuerte viento se lleva el rebaño de nubes de lluvia lejos de la ciudad, al otro lado de las montañas a la distancia."

"La vista es bonita, pero…"

"…"

stop music fadeout 6.0

show dandelionsbg thin
show dandelionsfg thin
with None

"Una mota de blanco vuela por la orilla de mi visión periférica, pero cuando me giro para ver, ya se ha ido."

"Otra le sigue, luego una tercera."

"Antes de darme cuenta, docenas de casi invisibles motitas peludas blancas vuelan alrededor de nosotros."

show rin basic_delight behind dandelionsfg at center
with charaenter

rin "Mira, las flores."

"Ah. Ya lo veo."

$ renpy.music.set_volume(1.5, 0.5, channel="ambient")
$ renpy.music.set_volume(1.0, 0.0, channel="music")

scene bg school_hilltop_summer
show dandelionsbg dense
show dandelionsfg dense
with locationchange

play music music_comfort fadein 0.5

"El mar de dientes de león que cubría la cima de la colina en nuestra última visita ha cambiado con el paso de los días."

"Donde antes había amarillo brillante, ahora hay blanco esponjoso."

"Algunas de las flores ya han perdido sus semillas, pero muchas todavía siguen esperando una ráfaga de viento adecuada."

"Hoy esas ráfagas no escasean, de vez en cuando sacuden el pasto por completo, y de pronto el aire está repleto de semillas de dientes de león."

"Una a una, las semillas se separan de las flores y son llevadas lejos."

"Un evento común, pero uno que parece fascinar a Rin por alguna razón."

$ renpy.music.set_volume(1.0, 0.5, channel="ambient")

show rin negative_spaciness behind dandelionsfg at center
with charaenter

"Ella gira la cabeza de lado a lado, maravillándose ante el cambio sucediendo a todo su alrededor a medida que las semillas vuelan lejos."

"También las miro, siguiendo las motas blancas flotando con el viento hacia el horizonte, e imagino que puedo verlas aun después de que desaparecen de mi vista."

"…"

show rin basic_awayabsent
with charachange

rin "Hisao."

hi "¿Qué pasa?"

show rin basic_absent
with charachange

rin "¿Me amas?"

"Me pongo alerta de inmediato, para encontrarme con su repentinamente muy serio rostro que ya no está mirando solo a las flores."

"Qué pregunta tan difícil, hecha así como así, de la nada."

"Aun así, su brusquedad me fuerza a dar una respuesta rápido."

hi "No lo sé. Tal vez sí."

"Tal vez demasiado rápido."

show rin basic_deadpannormal
with charachange

rin "¿Qué significa eso?"

hi "… No lo sé."

show rin basic_lucid
with charachange

"Rin suspira, tal vez triste con mi respuesta vaga. Yo también lo estaría."

show rin relaxed_nonchalant
with charachange

rin "Yo tampoco."

show rin relaxed_boredom
with charachange

rin "No creo que sepa mucho sobre el amor."

hi "…"

hi "… Está bien, ¿no?"

show rin basic_lucid
with charachange

"“¿Cómo podría saberlo?”, el cómo se encoge de hombros parece decir eso, titubeando en dar una respuesta más firme."

"Ella guarda silencio por solo un segundo de más, pero aun así ese segundo no es lo suficientemente largo para que yo piense más allá…"

show rin basic_absent
with charachange

rin "Te amo."

"Esas dos palabras me vuelven piedra como un conejo mirando dentro de los faros de un auto, pero no soy un conejo y tan solo estoy mirando dentro de los ojos de Rin que parecen muy, muy impasibles."
"Demasiado para lo que acaba de dejar salir de su boca."

show rin basic_deadpanupset
with charachange

"Sin embargo Rin se ve bastante seria, hasta que saca la lengua, frunce el ceño un poco y me confunde todavía más de lo que lo hicieron sus palabras."

"¿Por qué se ve ligeramente triste?"

"Fue una confesión de sus sentimientos más profundos. ¿Una prueba para ver cómo reaccionaría yo? ¿Una prueba de cómo reaccionaría ella?"

show rin basic_awayabsent
with charachange

rin "Sabe raro."

hi "… ¿Sabe?"

show rin basic_lucid
with charachange

rin "Sí. Muy raro."

"Ella se ríe, tal vez nerviosamente o así quiero pensarlo, pero se detiene a la mitad cuando se da cuenta de cuán raro suena."

show rin negative_spaciness
with charachange

rin "Como si… No sé qué, yo… no creo que haya una palabra para esto."

"Rin sigue hablando como si no hubiera significado detrás de sus palabras, palabras constantes y descuidadas caen de la misma lengua que formó las más importantes."

show rin negative_worried
with charachange

rin "Una palabra para… ahhh…"

"Excepto."

show rin negative_annoyed
with charachange

rin "… es como…"

"Que ella no puede."

show rin basic_deadpanupset
with charachange

rin "…"

"Encontrar las palabras."

show rin basic_sad
with charachange

rin "…"

"Rin tan solo sigue mirándome, tropezándose con sus palabras como si su cerebro se hubiera detenido súbitamente por completo."

"Se ve terriblemente confundida, justo como me siento en este momento mientras espero a que ella se explique."

"Pero no lo hace, solo parpadea unas cuantas veces, el aleteo de sus largas pestañas captura mi atención porque de otro modo ella parece estar petrificada."

"Hasta que me doy cuenta de que ellas estaban peleando contra ello."

show rin basic_crying
with charachange

"Son esas lágrimas extrañas otra vez, no asociadas con la tristeza o la felicidad, ni patéticos sollozos ni risa de alegría."

"Solo lágrimas, espontáneas y sin advertencia, como en aquella ocasión en su salón de clase."

rin "Ah."

"Solo unas cuantas de ellas, no lo suficiente para armar un alboroto, así que Rin no se mueve para ocultarlas aun después de darse cuenta de ellas."

"Rin llora, viéndose como si no tuviera idea de por qué, y de algún modo una gran ansiedad crece dentro de mi pecho cuando miro en sus ojos llorosos que me miran de vuelta."

"También me petrifica, la impresión de la incomprensibilidad de esta situación."

"Simplemente yo ya no sé qué es lo que está sucediendo."

hi "¿Rin? ¿Qué ocurre?"

rin "Yo…"

show rin negative_crying
with charachange

"Ella agita la cabeza en su confusión, batallando para sacar las palabras de su boca."


show rin basic_crying
with charachange

rin "Lo siento…"

rin "Puede que te tenga un poco de miedo."

"Las palabras son masculladas lentamente, con una vocecita que es tan incrédula de lo que está diciendo como lo soy yo."

hi "¿Qué? ¿Por qué?"

show rin basic_sad
with charachange

rin "No lo sé. Solo decir eso me hizo sentir así."

show rin basic_absent
with charachange

rin "La gente llora cuando está asustada, ¿verdad?"

show rin basic_awayabsent
with charachange

rin "¿Ves? Yo lo puedo hacer también."

"Desvía su mirada ahora, deliberadamente para no verme. Me desconcierta, al menos tanto como lo que está diciendo."

show rin negative_annoyed
with charachange


rin "Yo… algunas veces, contigo, quiero escapar tanto pero no puedo moverme, es como si mis piernas se convirtieran en panna cotta de limón y mi corazón se siente como si fuera a estallar y…"

show rin negative_sad
with charachange

"Deja caer sus hombros melancólicamente."

rin "¿Alguna vez te pasó algo como esto?"

"… Recuerdo el cielo plomizo sobre el bosque congelado y el sonido de las ramas desnudas golpeándose unas con otras."

"Es como una memoria de otra vida."

hi "Sí. Una vez."

hi "Mi corazón también me dolía mucho entonces."

show rin basic_surprised
with charachange

rin "Pero pensé que tu cosa no era contagiosa."

"Sacudo mi cabeza y una diminuta, ligeramente forzada sonrisa surge en mis labios."

"El otro mal de mi corazón bien podría ser contagioso y no me importaría ni un poco."

hi "¿De qué tienes miedo? Nunca pensé que daba miedo."

show rin negative_confused
with charachange

"Rin sacude la cabeza con desesperación, como si supiera que la maraña dentro de su mente no podría desenredarse con solo eso."

rin "Tú me haces sentir que debería ser alguien más que yo."

show rin negative_sad
with charachange

rin "Es algo que da miedo."

show rin negative_worried
with charachange

rin "Pasa cuando eres bueno conmigo. Como ayer."

rin "Nunca sé qué hacer en momentos como ese. Es difícil."

"Su voz, apenas audible, susurra una admisión de algo que es demasiado vergonzoso de siquiera pensar, eso sin mencionar decirla en voz alta."

"Rin nunca ha sido del tipo que se avergüenza así que sí lo pronuncia en voz alta, aunque con timidez como por instinto."

show rin basic_upset
with charachange

rin "Pero quiero hacer algo. Pero no sé si este yo pueda."

"Por un momento, simplemente nos miramos el uno al otro como si esperáramos a que el otro diga algo."

"…"

hide rin
show rin basic_upset_close as rin2
with characlose

hi "Eres tan estúpida."

hide rin2
show rin relaxed_surprised_superclose at center
with characlose

"Los labios de Rin saben salados y asustados contra los míos."

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack
with Dissolve (0.4)

window show

"Al tomarla en un abrazo, siento mi corazón golpeando en mi pecho dolorosamente."

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack
with Dissolve (0.4)

$ renpy.music.set_volume(0.5, 1.0, channel="music")
$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

nvl clear
nvl show dissolve

n "\n\nAunque estoy feliz de que ella pueda decir cosas como esa, me hacen sentir triste después de todo."

n "El entusiasmo de Rin, su pasión, su fuerza. Todas esas cosas tan queridas para mí son las que no quiero cambiar."

n "¿Cómo debería tratarlas? ¿Adónde es que se dirigen? ¿Es ese futuro irrevocablemente diferente al mío?"

n "Esa ansiedad nunca disminuirá la presión en mi corazón, pero creo que podría aprender a vivir con ella."

n "Lentamente, el dolor dentro de mi corazón se apaga, y se asienta en el mismo ritmo que el de Rin."

n "\n\nLo escuchamos por un rato."

n "…"

$ renpy.music.set_volume(1.0, 1.0, channel="music")
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")
stop music fadeout 8.0

nvl hide dissolve
nvl clear

hide rin2
show rin basic_blush_close behind dandelionsfg at center
with charadistant

window show

"Después de que nuestros labios se separan, toma un tiempo para que alguno de los dos se percate de que ya podemos decir algo."

"…"

show rin basic_sad_close
with charachange

rin "¿Ves?"

show rin relaxed_doubt_close
with charachange

rin "Eres una persona muy amable, aun cuando no lo eres."

rin "Es lo más aterrador de todo."

show rin relaxed_sleepy_close
with charachange

rin "Creo… que todo a lo que le tenía miedo era a tu amabilidad."

"…"

hi "¿Eso es malo? ¿Aun si tienes miedo?"

show rin basic_lucid_close
with charachange

"Ella piensa en ello por un rato, frunciendo su ceño como si esto fuese algún tipo de problema difícil de Matemáticas."

show rin basic_deadpanamused_close
with charachange


rin "No. No hay problema con ello. Está bien, si es contigo."

"Como un peso que se levanta de mi pecho, sus palabras me alegran el corazón, llenándolo con… no lo sé, ¿felicidad?"

"¿Qué más podría ser?"

"Esta vez mi sonrisa es verdadera."

hide rin
show rin basic_deadpanamused as rin2 behind dandelionsfg
with charadistant

"Rin da un paso atrás, todavía sonriéndome con gentileza como yo a ella."

show dandelion full:
    alpha 0.0 xalign 0.5 yanchor 1.0 ypos 1.2 subpixel True
    easein 1.0 ypos 1.0 alpha 1.0
with None
show dandelionbg behind dandelion
show dandelions_blurbg behind dandelion
show dandelions_blurfg behind dandelion
hide dandelionsfg
hide dandelionsbg
with Dissolve(1.0)

hide rin2
show rin basic_deadpanamused behind dandelionbg
with None

"Mientras limpia su rostro en su hombro, recojo un diente de león entero, redondo y esponjoso y lo llevo a mis labios apretados."

show dandelion gone
with Dissolve(1.0)

"Pfff…"

"Se esparcen por el viento que los levanta y los lleva a un nuevo hogar."

"Y pensar que, tan solo hace unas cuantas semanas, eran tan diferentes."

"Esto es cambio."

"…"

show dandelion gone:
    easeout 1.0 alpha 0.0 yanchor 1.0 ypos 1.2
with None

hide dandelionbg
hide dandelions_blurbg
hide dandelions_blurfg
show dandelionsbg dense behind rin
show dandelionsfg dense
with Dissolve(1.0)

hi "Oye, entonces las flores se transformaron en lo que debían convertirse, como lo dijiste la última vez."

hi "¿Qué hay de ti? ¿Te convertiste en una artista verdadera? ¿O no, porque te escapaste?"

show rin basic_deadpancontemplation
with charachange

"Hace una pausa por un momento para reflexionar sobre mi pregunta."

show rin relaxed_nonchalant
with charachange

"… y se encoge de hombros."

"Casi me hace reír."

"La despreocupada soltura de su gesto es algo adorable, una señal de cómo Rin puede, real y verdaderamente, sin restricciones de algún tipo, deshacerse del peso entero del mundo sobre sus hombros, si ella así lo quiere."

"Ella es, de toda manera posible y probablemente algunas imposibles… libre."

"Y creo que podría amarla por ello."

show rin basic_absent
with charachange

rin "No creo que importe."

show rin basic_deadpandelight
with charachange

rin "Solo veamos las nubes este día."

play music music_twinkle fadein 2.0

scene ev rin_goodend_1
show evbg rin_goodend_base:
    center
    subpixel True xalign 0.0
    1.0
    easein 20.0 xalign 1.0
show dandelionsbg dense
show rin goodend_1:
    center
    subpixel True xalign -0.5
    1.0
    easein 20.0 xalign 1.0
show dandelionsfg dense
show evfg rin_goodend:
    center
    subpixel True xalign -1.0
    1.0
    easein 20.0 xalign 1.0
with whiteout

"Ella toma dos pasos para escalar una gran roca para poder levantarse tan alto como es posible aquí, y se para de puntillas."

"Cuando tratas de alcanzar las nubes, cada centímetro cuenta."

hi "Seguro, veamos las nubes. Es bueno hacer algo que realmente quieres, de vez en cuando."

rin "Sí. Puede que tengas la razón."

"Miro hacia arriba al cielo azul abriéndose a lo alto sobre nosotros."

"Es un vasto y profundo cerúleo que se extiende hasta llenar mi campo visual entero y más allá."

"Aun así Rin se queda sobre su roca, asomándose por el horizonte distante donde las nubes de lluvia flotan alejándose de nosotros."

rin "He decidido algo."

"Esa voz de ensueño suya, hablada al viento que la lleva a mis oídos, le hace falta determinación en el tono pero está llena de sentido."

rin "Está bien ser yo después de todo."

$ renpy.music.set_volume(0.5, 1.0, channel="music")
$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

window hide
nvl clear
nvl show dissolve

n "\n\n\n¿Está bien? Sus decisiones siempre parecen ser bastante… únicas."


n "Bueno, supongo que es una epifanía importante."

n "Llegar a un acuerdo con uno mismo, aceptarte a ti mismo, estar bien con quién eres."

n "Una simple resolución del corazón que para algunas personas es excesivamente difícil, si no es que imposible."

n "Me doy cuenta bien de que podría yo también ser de ese tipo de personas."

n "También Rin… "

n "Tal vez no seamos tan diferentes después de todo."

n "Quizás para aceptar a alguien más, primero debes aceptarte a ti mismo."

n "Tal vez ese sea un paso necesario, el cual no tomamos hasta ahora."

$ renpy.music.set_volume(1.0, 1.0, channel="music")
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

nvl hide dissolve
nvl clear
window show

"Viéndola de pie sobre esa roca, yo creo que ella puede encontrar lo que sea que esté buscando."

"Y yo también."

show ev rin_goodend_1b
show evbg rin_goodend_base:
    subpixel False xalign 1.0
show rin goodend_1b:
    subpixel False xalign 1.0
show evfg rin_goodend:
    subpixel False xalign 1.0
with charachange

"El viento atrapa su cabello y ropa, y Rin abre sus cortos brazos en un abrazo que es tan pero tan diminuto, pero tan amplio como ella puede hacerlo."

"Por un momento parece que ella misma podría levantar el vuelo, y tengo que detenerme para no sujetar su hombro, para no arrastrarla de vuelta hacia mí."

"Pero esta imagen es algo que tan solo puedo mirar, es algo para que yo recuerde."

"Las mangas de Rin aletean libremente en el viento, su cabello alborotado incontrolablemente por este, su piel tocada por el sol poniente."

"Su forma elegante que he llegado a adorar se estremece en el frío viento que lleva las pequeñas motas blancas frente a ella, cada una el inicio de una nueva flor."

"Todo ello está grabado dentro de mi corazón."

"Como aquellas diminutas semillas esparcidas por el viento, estoy seguro de que Rin también puede tomar su lugar en este mundo sin la necesidad de crear el suyo propio dentro de este."

"Tal vez ella lo crea también, y estando de pie tan cerca del cielo como es posible, ella le da al mundo un gran abrazo."

"Para mí parece como si el mundo entero realmente pudiera caber ahí, entre esos pequeños brazos suyos, dentro de su abrazo que lo cubre todo."

show ev rin_goodend_2
show rin goodend_2
with charachange

rin "¿Hisao?"

"Ella me mira del mismo modo con el que llama mi nombre, con descuido por encima de su hombro con un extraño tono de felicidad en su voz y en sus ojos."

show evbg rin_goodend_base:
    subpixel True yalign 0.0
    acdc_warp 12.0 zoom 1.15
show rin goodend_2_hires:
    subpixel True yalign 0.0 xalign 1.0 zoom 0.769
    acdc_warp 12.0 zoom 1.0
    subpixel False
show evfg rin_goodend:
    subpixel True yalign 0.0
    acdc_warp 12.0 zoom 1.45
with None

"Miro dentro de aquellos misteriosos y oscuros ojos que centellean desde debajo de su cabello cobrizo."

"Aunque estoy demasiado lejos de ella para verlo, estoy seguro de que reflejan mi imagen."

hi "¿Qué sucede?"

rin "¿Cuál es la palabra para cuando sientes dentro de tu corazón que todo en el mundo está bien?"

stop music fadeout 4.0
stop ambient fadeout 4.0

window hide

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
