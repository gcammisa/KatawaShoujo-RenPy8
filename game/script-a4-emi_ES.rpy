label es_E28:

window hide None

scene black
with dissolve

with Pause(2.0)

play sound sfx_alarmclock

with Pause(3.0)

scene bg school_dormhisao
with openeye

play music music_dreamy fadein 4.0

window show

"El sonido de mi alarma no es una intrusión bienvenida en el sueño que he luchado por obtener. Dudo que haya estado verdaderamente dormido por más de una hora o dos."

"Demasiadas cosas en mente. ¿Tomé la decisión correcta, al dejar ayer la casa? ¿Conseguí que Emi se diera cuenta de lo irracional que ha sido?"

"¿Alguna vez conseguiré que deje de ser irracional? La mamá de Emi me dio una nueva perspectiva el otro día, pero aún no estoy seguro de que sea la perspectiva correcta."

"Ella también resultó lastimada ayer cuando me fui."

"Sé que parte de cualquier conversación tendrá que incluir una disculpa por eso. Sea o no lo correcto, la lastimé."

"Me apresuro en llegar a la pista, ansioso de hablar con Emi. Creo que sé lo que debo decir. Primero una disculpa por irme, y avanzar desde ahí."

scene bg school_track
with locationskip

"A menos, por supuesto, que Emi no venga."

"Lo que parece ser el caso, por cómo se ven las cosas. Han pasado unos quince minutos desde que llegué aquí, y no hay señales de ella."

"Ella nunca llega tarde, a menos que esté enferma, lo cual es poco probable. Puede que simplemente no quiera verme en este momento."

scene bg school_track_on
with locationchange

scene bg school_track_running
with locationchange

"Para apartar mi mente de lo que eso implica, comienzo con mi rutina de calentamiento y empiezo a correr por la pista."

"Despeja mi mente de manera maravillosa; durante la media hora que paso corriendo, no pienso en nada excepto en correr."

scene bg school_track_on
with locationchange

stop music fadeout 4.0

"Sin embargo, una vez que termino, y Emi todavía no se ha aparecido…"

"Me preocupa un poco. Con algo de suerte, el enfermero sabrá dónde se encuentra; o al menos podré ver cuál cree él que debería ser mi siguiente paso."

scene bg school_nurseoffice
show nurse grin at center
with locationskip

play music music_nurse fadein 0.5

nk "Así que, anoche no te fue muy bien, supongo."

hi "¿Eh? ¿Ya lo sabes?"

nk "Tengo mis fuentes, y no es como si fuera a pasar por alto la ausencia de tu compañera de carreras esta mañana, ¿no crees?"

hi "No, supongo que no."

show nurse neutral
with charachange

nk "Entonces, ¿qué pasó?"

hi "¿No lo sabes ya?"

show nurse fabulous
with charachange

nk "Tal vez, pero podría estar fingiendo. Quizá preferiría escuchar tu versión de la historia antes de dar algún consejo."

"Informo rápidamente al enfermero de los eventos de anoche, y él escucha todo sin cambiar de expresión una sola vez."

"Ninguna de las cosas que ocurrió parece sorprenderlo, aunque sí parece sorprendido cuando le cuento que no seguí a Emi."

show nurse grin
with charachange

nk "Elegiste hablar con su madre, ¿eh? Una buena decisión, aunque supongo que al final no te funcionó muy bien."

hi "Bueno no estoy seguro. Emi parecía arrepentida cuando me fui, o al menos lo parecía hasta que volvió a levantar sus defensas."

"El enfermero suspira y extiende sus manos en un gesto conciliador."

show nurse fabulous
with charachange

nk "Francamente, lo que me sorprende es que las haya bajado. Emi ha tenido mucha práctica en esa área. Probablemente no obtendrás nada más de ella."

hi "No te creo."

nk "¿Eso piensas? ¿Crees que te contará toda la historia?"

"Juraría que acabo de ver un leve destello en los ojos del enfermero. Su expresión es la misma, pero se inclina muy ligeramente hacia adelante."

hi "Pienso que ella se abrirá un poco más si no soy un idiota al preguntarle, sí."

"El enfermero responde con su enigmática sonrisa y se encoge de hombros ampliamente. Creo que está disfrutando demasiado de su rol."

show nurse grin
with charachange

nk "Ese es el verdadero truco, ¿no es así? ¿Estás seguro de que conoces la manera correcta de abordar el tema? Puedo garantizar que Emi se esforzará al máximo para pretender que anoche no pasó nada."

show nurse neutral
with charachange

nk "Será dolorosamente incómodo para los dos, pero también será mucho más seguro que intentar preguntarle por la historia completa de nuevo. Esta vez podría salir peor."

nk "¿Estás preparado para algo así?"

"Suena como un desafío, como si no creyera ni por un minuto que yo podría ser tan audaz. En realidad me siento un poco insultado por su falta de confianza en mí."

hi "¡Claro que estoy preparado para eso! ¡La amo!"

show nurse fabulous
with charachange

"Mi arrebato obtiene una ceja levantada como respuesta."

nk "Muy bien."

show nurse neutral
with charachange

nk "Buena suerte. Hazme saber cómo resulta todo."

"Aunque dice esto último con la misma sonrisita de siempre, en realidad creo que el enfermero quiere que tenga éxito."

stop music fadeout 3.0

scene bg school_nursehall
with locationchange

"Resisto el impulso de cargar directamente hacia la habitación de Emi para demostrar que el enfermero se equivoca. He ido antes sin un plan adecuado, y los resultados fueron menos que sobresalientes."

"Si voy a hacer esto, necesito pensar exactamente en qué voy a decir, y en cómo lo voy a decir. Algo para pensar en clases."

scene bg school_scienceroom
with shorttimeskip

"Efectivamente, para cuando empieza el almuerzo, creo que tengo una buena idea de qué decir. Puedo hacerlo."

play sound sfx_normalbell

scene bg school_staircase1
with locationskip

"Suena la campana, agarro mi almuerzo y subo las escaleras rápidamente, ansioso de ser el primero en llegar. Tendré que pedirle a Rin que se vaya, y tendré que—"

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 1.0
play sound sfx_door_creak

scene bg school_roof
show emi basic_hes at twoleft
show rin basic_absent at tworight
with silentwhiteout

emi "¡Hola, Hisao! ¡Perdón por no haber podido correr contigo esta mañana! ¡Me quedé dormida!"

"De alguna forma, tanto Emi como Rin han conseguido llegar a la azotea antes que yo."

hi "Oh, no hay problema. La última noche fue un poco… agotadora, supongo."

"La expresión de Emi no cambia en absoluto."

emi "¡Sí, perdón por eso! ¡Pero he tenido una mañana tan extraña después de eso!"

hi "Oh ah, ¿en serio?"

show emi basic_happy
with charachange

"Emi procede a charlar el resto del tiempo. Apenas consigo decir una palabra o dos de vez en cuando, y pronto termino intercalando palabras con ella en el tipo de diálogo de ida y vuelta que parece haber definido nuestra relación inicial."

"No voy a avanzar con este problema durante el almuerzo, claramente. Puedo respetar eso; Emi obviamente no quiere que Rin se vea envuelta en nuestras cosas por accidente, y eso está bien."

"No es que yo crea que Rin lo notaría, pero al menos puedo respetar ese tipo de lógica."

"Intento con una táctica distinta."

hi "Oye, Emi. ¿Qué harás hoy luego de clases? Estaba pensando que podríamos ir a algún lugar a cenar, o algo."

show emi sad_depressed
with charachange

"Emi se ve genuinamente arrepentida."

emi "¡Lo lamento, Hisao! ¡Le prometí al capitán del equipo que me quedaría luego de la práctica para ayudar a algunos chicos con sus formularios! Tendrá que ser en otra ocasión."

hi "Sí, seguro…"

window hide

scene black
show bg misc_sky at center
with locationchange

nvl clear
nvl show dissolve

n "Honestamente no estoy seguro de qué hacer ahora. Puede que tampoco sea una buena idea profundizar en el tema el día después."

n "Ella podría seguir enojada por eso y simplemente no lo demuestra. Además, no pasa nada si tiene deberes con el equipo de atletismo, ¿cierto?"

show bg misc_sky:
    linear 10.0 alpha 0.0
with None

n "Me digo a mí mismo alguna variación de este tema el día siguiente. Y luego el siguiente. Me levanto, corro con Emi (mientras lo hacemos ella se rehúsa a hablar de nada excepto de la carrera y de lo que estaba haciendo la noche anterior), luego sigue el almuerzo, durante el cual nos sentamos y charlamos hasta que suena la campana."

n "Sus nuevas responsabilidades efectivamente evitan que la vea fuera de la escuela. Tal vez, solo tal vez, estoy dejando que pase porque es más seguro de esta manera, justo como dijo el enfermero."

n "Excepto que aun siendo lo más seguro, me siento más y más desdichado. Emi ya no se ve bien cuando la veo; oscuros círculos se esconden bajo sus ojos, se ve más y más distraída, y no me atrevo a preguntarle qué anda mal, porque nunca parece el momento adecuado."

n "\nSoy absolutamente miserable."

stop ambient fadeout 2.0

nvl clear
nvl hide dissolve

$ suppress_window_before_timeskip = True

scene black
with dissolve



label es_E29:

scene bg school_staircase1
with locationchange

"Hora de otro almuerzo. Subo penosamente las escaleras a la azotea como un hombre condenado."

play ambient sfx_rooftop fadein 1.0

scene bg school_roof at bgleft
show rin basic_absent at center
with locationchange

"Rin está ahí arriba, pero Emi no. Inmediatamente me preocupa que algo le haya pasado. Tal vez la falta de sueño por fin la hizo colapsar, o algo peor."

"Se veía muy cansada luego de nuestra carrera en la mañana. Tal vez se quedó dormida y ni siquiera pudo ir a clases."

hi "Hola, Rin. ¿Dónde está Emi?"

show rin basic_deadpancontemplation
with charachange

"Como respuesta recibo una mirada bastante penetrante por parte de Rin, y algo que se aproxima a un ceño aparece en su rostro."

rin "¿Es esa información realmente importante?"

hi "Creo que sí. Usualmente está aquí contigo, ¿no?"

show rin basic_awayabsent
with charachange

rin "No lo sé. No tengo forma de estar segura."

hi "Puedo confirmar que ella, en efecto, generalmente está aquí contigo cuando subo."

show rin basic_deadpannormal
with charachange

rin "Bueno, ahora no. ¿Eso te preocupa?"

hi "Algo."

show rin basic_deadpancontemplation
with charachange

rin "Hm."

play sound sfx_door_creak
with Pause(0.5)

show emi invis:
    twoleft
    xpos 0.1
with None

show bg school_roof at center
show rin basic_deadpancontemplation at tworight
show emi basic_closedhappy at twoleft
with dissolvecharamove

"Eso parece terminar la conversación, y la cuestión se vuelve irrelevante de todos modos porque Emi sale por la puerta con su energía habitual."

show rin basic_deadpan
with charachange

rin "Hisao está algo preocupado por ti, Emi. No creo que él pueda decidirse, o tal vez es solo que yo no le creo, pero me parece que ahora me iré a un lugar menos incómodo."

hide rin
with charaexit

with Pause(0.5)

show bg school_roof at bgright
show emi basic_confused at center
with dissolvecharamove

"Estoy tan sorprendido por la repentina franqueza de Rin respecto a, bueno, lo que sea que apenas alcanzo a ver cómo desaparece por la puerta."

show emi basic_shock
with charachange

"Emi está igual de sorprendida, y un leve carmesí la colorea mientras me mira con la boca abierta. Se me ocurre que probablemente debería decir algo, aunque sea para romper el incómodo silencio que ha caído repentinamente."

hi "Es porque aún no estabas aquí. Estaba eh, preocupado por eso."

show emi basic_confused
with charachange

emi "¿Por qué?"

hi "Usualmente estás aquí, así que me preocupaba que algo malo te hubiera pasado."

show emi sad_grin
with charachange

emi "Esta no es la primera vez que llego tarde, sabes. ¿También te preocupaste todas esas veces?"

hi "Eh, en realidad no."

show emi basic_closedgrin
with charachange

"Esto parece divertir un poco a Emi. No sé por qué, pero eso me molesta un poco."

show emi basic_grin
with charachange

emi "¿Entonces por qué esta vez fue una excepción?"

"Tal vez sea el tono ligero y burlón de la pregunta, pero algo en su respuesta me apremia a ser honesto, aunque no puedo evitar responderle bruscamente."

play music music_innocence fadein 10.0

hi "Porque has estado preocupándome desde la cena en tu casa, por eso."

show emi basic_hes
with charachange

"Bueno. Ya lo dije. Y los ojos de Emi están muy abiertos, y se ve como si quisiera echar a correr, pero no lo hace."

show emi sad_shy
with charachange

emi "Ah. Todavía con eso, ya veo."

hi "Qué, ¿crees que simplemente debería olvidarme de eso? ¡Me echaste de tu casa! ¡Hemos pasado casi una semana pretendiendo que nunca pasó!"

show emi sad_annoyed
with charachange

emi "Tampoco te vi a ti sacando el tema a conversación, sabes."

hi "Lo sé, y lamento que ese haya sido el caso. Tenemos que hacer algo al respecto, o simplemente seguiremos siendo lo que sea que seamos en estos momentos."

hi "Me está matando mirarte en este momento, ¿sabías eso? Esas ojeras bajo tus ojos y esa mirada distraída en ellos, y no puedo evitar pensar que yo lo provoqué de alguna manera."

show emi sad_pout
with charachange

emi "No lo hiciste. Créeme."

hi "Bueno, tampoco he ayudado. Sigo presionándote para que me digas cosas que aún no estás lista para decirme; tal vez me equivoqué al intentar que tu madre me ayudara, pero he estado tan preocupado por ti que no sabía qué más hacer."

show emi sad_depressed
with charachange

emi "Bueno, ya no tienes que preocuparte más por mí, ¿de acuerdo? Creo que está muy claro que no somos el uno para el otro, así que tal vez deberíamos… parar."

"Tiene el rostro torcido mientras dice esto, como si no quisiera decirlo pero de todos modos se obligara a hacerlo."

hi "En realidad no quieres eso, ¿cierto? Caray, si apenas te atreves a decirlo. De todas formas, no evitará que siga preocupándome por ti. Me importas demasiado como para detenerme a voluntad."

hi "¿No quieres decirme qué anda mal? Muy bien, pero no cesaré en mis intentos de ayudarte, aunque eso solo signifique seguir a tu lado."

show emi sad_angry
with charachange

emi "¡Deja de decir eso!"

"Ahora ella está temblando, y cuando me mira puedo ver que está asustada y frustrada por un millón de cosas diferentes a la vez. Sacudo la cabeza lentamente y doy unos cuantos pasos en su dirección."

hi "¿Sabes qué me dijo tu mamá? Me dijo que tú nunca pedirías ayuda, porque sabes que eres lo suficientemente fuerte como para superar cualquier cosa sola, pero esa no es toda la historia, ¿verdad?"

show emi basic_hes
with vpunch

"Sus ojos se agrandan, y da un paso hacia atrás. Continúo, porque creo que por fin lo he entendido. Algo me dice que no tendré otra oportunidad. Ya lo he pospuesto por demasiado tiempo."

hi "No hace daño que haya alguien ayudándote, a menos de que, en primer lugar, te preocupe necesitar ayuda. Estás asustada, ¿no es así? Por culpa de…"

"Me detengo, porque no estoy seguro de lo que le pasó al padre de Emi, y no quiero saltar a conclusiones."

hi "Bueno, no importa por qué, pero está bien estar asustada."
hi "Has estado huyendo de eso y de mí por mucho tiempo, aun cuando sabes que eventualmente tendrás que darte la vuelta y enfrentar tu miedo, y yo voy a estar ahí para ayudarte cuando lo hagas."

hi "No voy a parar, porque no creo que quieras eso. Puedes entender ese tipo de determinación, ¿verdad?"

"Puedo ver que he logrado impactarla, pero rápidamente vuelve a enfadarse para tratar de alejarme."

show emi sad_angry
with charachange

emi "¿De vuelta sobre tu blanco corcel, Hisao? ¿Debes ayudar a la pobre lisiada a enfrentar sus problemas emocionales? ¿Qué sabes de mí y de las cosas que ya he tenido que enfrentar?"

show emi sad_grit
with charachange

emi "¿Crees que dos meses aprendiendo a caminar de nuevo fueron divertidos? Pero lo hice, y luego de hacerlo tuve que…"

"Por un momento parece que ella va a decir algo más, pero se interrumpe a medio camino."

hi "Y luego de todo eso, ¿no crees que puedes superar tu miedo? Emi, no puedo ni imaginar las cosas por las que has pasado, pero haberlo hecho y seguir siendo la clase de chica que eres, bueno, me hace pensar que eres aun más fuerte de lo que crees."

hi "Así que no voy a ayudarte porque crea que necesitas ser rescatada. No quiero ser un caballero rescatando a la damisela en peligro, pero incluso los caballeros se ayudaban los unos a los otros, sabes. Quiero ayudarte, aun sabiendo que puedes hacerlo sola."

show emi sad_depressed
with charachange

"Por un momento parece que Emi va a desmoronarse por completo, pero no lo hace. Las lágrimas recorren su rostro, pero me mira fijamente."

emi "¿Por qué te esfuerzas tanto en ayudarme?"

hi "Diría que es porque te debo una por ayudarme cuando nos conocimos, pero esa no sería la verdad. La verdad es que solo quiero que seas feliz, porque te amo."

stop music fadeout 4.0

"¿Ya había dicho eso alguna vez? Hemos estado en una relación, y ha sido muy evidente que la amo, ¿pero alguna vez pronuncié las palabras?"

show emi sad_shyblush
with charachange

emi "¿Qué dijiste?"

"Lo digo de nuevo, saboreando la sensación de poder decirlo, de ser capaz de decirlo y de querer decirlo. Emi parece aturdida."

hi "Dije que te amo, Emi. Te amo. Solo a ti, y eso hace que quiera estar a tu lado, sin importar lo que debas atravesar."

play music music_serene fadein 0.5

show emi excited_sad_close
with vpunch

"Luego me encuentro atrapado en un feroz abrazo, mientras Emi empieza a sollozar contra mi pecho."

emi "¡Lo siento! Lo siento tanto por todo pero estoy muy asustada, Hisao, asustada de perderte y también te amo pero no puedo perderte y yo solo… ¡Lo siento tanto!"

show emi sad_shy
with charadistant

"La sujeto en silencio, tranquilizándola hasta que se calma. Ella retrocede, algo más serena."

emi "¿Vendrás conmigo mañana? ¿De vuelta a mi casa? Hay algunas cosas que debo mostrarte, si voy a hacer esto."

hi "Claro. Tal vez esta vez podremos regresar juntos, en vez de separados."

show emi sad_grin
with charachange

"Emi sonríe, con un repentino destello de alegría que parece más genuino que cualquier otra cosa que haya visto durante esta semana."

emi "Sí, tal vez."

play sound sfx_warningbell

"Suena la campanada del almuerzo, y maldigo el mal gusto del universo."

hi "¿Estás libre esta noche? Podemos hablar más tarde, ¿cierto?"

"Emi sacude la cabeza."

show emi sad_depressed
with charachange

emi "Perdona, Hisao, pero aún estoy ayudando al equipo de atletismo. Además, creo que no sería bueno que habláramos esta noche. Estaré demasiado cansada para pensar con claridad, y quiero ser capaz de contarte todo sin arruinarlo."

show emi sad_shy
with charachange

emi "Puedes esperar, ¿verdad?"

"Incluso en estos momentos, hay cierto miedo en su voz. Sonrío y coloco una mano sobre su hombro."

hi "De acuerdo. Estaré esperando."

show emi excited_amused_close
with characlose

"Emi me da un beso rápido antes de dirigirse hacia las escaleras."

show emi sad_grin
with charadistant

emi "Gracias, Hisao. Te veo mañana en la mañana."

hi "No faltaría por nada."

hide emi
with charaexit

$ renpy.music.set_volume(1.0, 2.0, channel="ambient")
stop ambient fadeout 2.0

scene bg school_staircase1
with locationchange

"Me dirijo a las escaleras con la sensación de sus labios sobre los míos, súbitamente consciente de lo mucho que extrañaba esa sensación. Tendré que recordar agradecerle a Rin por habernos hecho hablar el uno con el otro."

"Aunque es posible que no se dé cuenta de lo que ha hecho. Aun así, de no ser por ella dudo que hubiera sido capaz de volver a confrontar a Emi."

"Supongo que necesitaba más ayuda de la que creía. Mañana, sin embargo, tendré que enfrentar solo lo que sea que Emi esté elaborando."

"Estaré a la altura del desafío. Espero."

stop music fadeout 2.0

scene black
with dissolve

$ suppress_window_after_timeskip = True



label es_E30:

window hide None

scene black
with dissolve

with Pause(2.0)

play sound sfx_alarmclock

with Pause(3.0)

scene bg school_dormhisao
with openeye

window show

"El sol de la mañana se ve brillante a través de mi ventana abierta, y al sonido de mi alarma no le toma mucho levantarme."

"Dormí sorprendentemente bien anoche, seguro por saber que al menos tengo otra oportunidad con Emi."

"Si puedo evitar hacer algo estúpido, tal vez averiguaré qué ha estado molestándola."

"Tengo algunas conjeturas, pero nada concreto. E indudablemente nada que le vaya a decir a ella; antes preferiría que ella misma me lo diga."



label es_E30a:

"Aunque no puedo evitar recordar la advertencia del enfermero de que podría no gustarme lo que ella tiene que decir. ¿Realmente necesito tanto saberlo?"

"¿Qué tal si es algo horrible y hace que ella me repugne? ¿De verdad puedo decir que estoy preparado para afrontar cualquier cosa que ella tenga que decir, sin importar lo que sea?"

"Emi dijo que quiere contármelo “sin arruinarlo”. ¿A qué diablos se refería con eso? ¿Qué podría arruinar?"

"Supongo que no sirve de mucho preocuparse por eso, a fin de cuentas. Hoy lo averiguaré. De repente se me ocurre que debo correr esta mañana sin importar qué, para despejar mi mente, por lo menos."



label es_E30b:

scene bg school_track
show emi basic_grin_gym at center
with locationskip

"Emi está esperándome como prometió, viéndose algo demacrada, pero aparte de eso alegre y animada. Mucho más que cualquier día anterior de esta semana."

show emi excited_proud_gym
with charachange

emi "¡Hisao! ¡Llegas tarde!"

"Sacudo mi mano con desdén."

hi "¡Tonterías! Es solo que tú llegaste temprano."

play music music_emi fadein 2.0

show emi basic_closedgrin_gym
with charachange

"Emi me sonríe, y se siente como si por fin hubiéramos regresado a donde deberíamos estar."

"Excepto que ahora Emi, y no solo yo, quiere dar un paso al frente. Aunque una parte de mí está preocupada de que ella dé marcha atrás en el último instante."

show emi basic_grin_gym
with charachange

emi "¡Date prisa y estírate, Hisao! ¡No quiero perder el autobús!"

hi "¿El autobús?"

show emi sad_grin_gym
with charachange



label es_E30c:

emi "Sí, el autobús. Quiero mostrarte algo, y no quiero llegar tarde."

hi "Oh, de acuerdo."

"Intento no sonreír de oreja a oreja. Me alegra más de lo que puedo describir que Emi quiera salir luego de la carrera, pero su promesa de mostrarme algo me tiene aún más intrigado."

"¿Era esto lo que ella tenía que pensar? Me pregunto qué estará planeando hacer."



label es_E30d:

emi "Dije que quería que vinieras de nuevo a mi casa, ¿recuerdas? Y le prometí a mi mamá que estaríamos allá a tiempo para almorzar, ¡así que quería darme prisa!"

hi "Madrugando, ¿eh?"

show emi basic_closedgrin_gym
with charachange

emi "Es más por el beneficio de mi mamá que por ninguna otra cosa."

hi "Ah, bueno, está bien."

"Intento sin éxito adivinar lo que Emi ha planeado, un poco antes de darme cuenta de que no me importa tanto."



label es_E30e:

show emi basic_concentrate_gym
with charachange

play sound sfx_gymbounce

show emi gymconcentratebounce
with None

"Realizo rápidamente mi rutina de calentamiento mientras Emi salta de un pie a otro con impaciencia. Realmente parece que quiere empezar lo antes posible."

scene bg school_track_running
with shorttimeskip

"La carrera termina tan rápido que apenas puedo creer que no haya caído muerto luego. Emi establece un ritmo abrasador y yo, en mi insensatez, lo sigo."

scene bg school_track_on
with Dissolve(2.0)

show emi basic_grin_gym at center
with charaenter

"Bueno, hasta el último par de vueltas. Tuve que reducir el ritmo por si acaso. Pero no me importa, y Emi está esperando pacientemente por mí cuando termino. Tan pacientemente como puede."

show emi basic_closedgrin_gym_close
with vpunch

emi "¿Terminaste? ¡Bien! ¡Vamos!"

stop music fadeout 2.0

scene bg school_nursehall
with locationskip

"Agarrando mi brazo, prácticamente me arrastra hasta la oficina del enfermero."

play music music_nurse fadein 0.5

show nurse neutral:
    twoleft
    xpos 0.2
    easein 0.5 twoleft
with charaenter

nk "Pareces apresurada, Emi. ¿Intentas tomar el primer autobús?"

show emi basic_grin_gym at tworight
with charaenter

emi "Sí, le dije a mi mamá que estaría allá para el almuerzo."

show nurse grin at twoleft
with charachange

nk "Bien, me encargaré de ti primero, entonces."

show emi basic_confused_gym
with charachange

emi "¡Pero Hisao también tiene que venir conmigo!"

show nurse fabulous
with charachange

"El enfermero alza una ceja cuando escucha esto y nos mira a los dos inquisitivamente."

nk "¿De verdad? Hoy, ¿eh?"

show emi sad_grin_gym
with charachange

"Emi asiente la cabeza a modo de respuesta, seguida de una sonrisa sorpresivamente tímida."

show nurse grin
with charachange

nk "Muy bien, entonces hagamos esto rápido."

hide nurse
hide emi
with charaexit

"Emi entra en la oficina del enfermero, y yo espero afuera pacientemente a que termine, preguntándome por qué el enfermero se veía sorprendido por lo que Emi dijo."

"Siento como si no entendiera una broma o la importancia de este día. Más allá del hecho de que evidentemente es importante de una manera u otra, por supuesto."

scene bg school_nurseoffice
with shorttimeskip

"Cumpliendo su palabra, el enfermero termina con Emi sorprendentemente rápido, y yo tomo su lugar luego de prometer que nos encontraremos en el portón principal. El enfermero toma mi pulso, escuchando por un rato."

show nurse fabulous at center
with charaenter

nk "Tus latidos son más rápidos que de costumbre. Te has estado exigiendo, ¿verdad?"

hi "Bueno, Emi parecía tener prisa en acabar la carrera, así que…"

show nurse neutral
with charachange

nk "Hm, no me sorprende. Hoy es muy importante para ella, sabes."

hi "Sospechaba que ese podría ser el caso, pero no tengo idea de por qué habría de serlo."

show nurse fabulous
with charachange

nk "¿Ella no te lo ha dicho? Interesante."

hi "Entonces, tú tampoco vas a contármelo."

show nurse grin
with charachange

nk "No, no lo haré. Sospecho que Emi tiene su propio plan para explicártelo hoy, y no quiero entrometerme con eso. Lo averiguarás dentro de poco, ¿así que cuál es la prisa?"

show nurse neutral
with charachange

nk "Ahora, con respecto a tu corazón, yo me lo tomaría con calma el resto del día. Nada de carreras espontáneas o algo como eso, ¿entendido?"

hi "Entendido. Además ella no tendrá puestas sus piernas para correr, ¿cierto?"

show nurse grin
with charachange

nk "No, pero si crees que algo como eso va a detenerla…"

hi "Buen punto."

show nurse neutral
with charachange

nk "No creo que sea un problema precisamente hoy, pero aun así."

"Si intenta tranquilizarme, está haciendo un pésimo trabajo. Rápidamente empiezo a preocuparme más y más por lo que podría pasar este día, como súbitamente enterarme de que Emi está en un culto o algo así."

"Al mismo tiempo, si hoy es tan importante y Emi me quiere ahí con ella, entonces tal vez realmente quiera acercarse más a mí. Tal vez esta sea la respuesta a todos los acertijos, a las noches sin dormir y los súbitos cambios de humor."

stop music fadeout 1.0

scene bg school_dormhisao
with locationskip

"De cualquier manera, apenas recuerdo agradecerle al enfermero antes de salir corriendo tan rápido como me atrevo a mi habitación para ducharme y ponerme alguna ropa que se vea decente."
"Si hoy es tan importante como parece, debería vestirme apropiadamente."

scene bg school_gate
show emicas grin at center
with locationskip

play music music_dreamy fadein 2.0

"Emi, por supuesto, me demuestra que estoy equivocado tan pronto llego al portón, llevando la camiseta y los pantalones cortos de siempre. Así que al menos sé que no es un asunto terriblemente formal, sea lo que sea."

show emicas smile
with charachange

emi "Llegas temprano, Hisao."

hi "No tan temprano como tú. Ansiosa, ¿no?"

show emicas wink_up
with charachange

"Emi me saca la lengua con picardía."

show emicas closedsmile
with charachange

"La parada del autobús no está muy concurrida a esta hora, lo que parece complacer a Emi, y terminamos relajándonos un poco mientras esperamos."
"Nos sentamos en silencio por un rato, pero puedo notar que Emi se está armando de valor para decir algo."

"No tengo nada que decir, así que permanezco sentado esperando a que ella hable. No toma demasiado tiempo."

show emicas awayfrown
with charachange

emi "Y bien, estoy segura de que sientes curiosidad por saber Por qué el enfermero se extrañó tanto de que te trajera conmigo hoy…"

hi "Un poco, sí, pero si no estás lista para contármelo—"

show emicas blush_close
with characlose

"Emi detiene mi oración poniendo un dedo sobre mis labios."

show emicas frown_close
with charachange

emi "No me tientes, Hisao. Quiero decirte esto, es solo que no estoy segura de cómo hacerlo bien. No quiero seguir evitándolo o aplazándolo, solo quiero ser capaz de decirlo."

hi "Entonces dilo."

show emicas neutral_close
with charachange

emi "Sabes que no va a ser así de fácil para mí, Hisao."

hi "Entonces hazlo como en las carreras. Calienta con algo pequeño y fácil, y avanza desde ahí. Pero no lo hagas demasiado rápido, ¿de acuerdo? Soy un hombre paciente, puedo esperarte."

show emicas awayfrown_close
with charachange

"Emi parece considerar mis palabras, sopesándolas con lo que probablemente es un deseo de acabar con esto de una vez. Lo admito, por más que le diga a Emi que se tome su tiempo, tampoco me molestaría que me lo dijera de una vez."

"Pero de alguna manera sé que Emi probablemente necesita más tiempo del que el viaje en autobús nos va a dar para decirlo todo, sea lo que sea."

show emicas frown_close
with charachange

emi "Sí, tal vez tienes razón. Además puede que la parada del autobús no sea el mejor lugar para esto. Pero solo para asegurarme de cumplir mi palabra, al menos diré esto:"

show emicas awayfrown_close
with charachange

"Ella respira hondo, exhala, y después de unos instantes dice en voz baja,"

show emicas weaksmile_close
with charachange

stop music fadeout 1.0

emi "Hoy vamos a ver a mi papá."

"Las palabras flotan en el aire, y puedo ver que Emi teme que mi respuesta sea entrar en pánico y desaparecer. Algo que una parte de mí quiere hacer."

"Pero sería estúpido de mi parte retroceder, o abandonar repentinamente la promesa que hice de estar ahí para Emi cuando me necesitase."

"El enfermero se extrañó mucho de que ella me llevara. Ella nunca lleva a nadie más, o al menos apostaría a que nunca lo ha hecho hasta hoy."

"El día parece adquirir aún más importancia. ¿Cuánto le ha costado a Emi llegar tan lejos?"

play music music_dreamy fadein 5.0

hi "Ah."

"¿Y por qué es esa la mejor respuesta que se me ocurrió?"

show emicas neutral_close
with charachange

emi "Sí."

hi "Yo eh, no sé qué debería decir."

emi "Nada, creo. Solo prométeme que vendrás conmigo."

hi "¡Por supuesto! Sabes que lo haré."

show emicas weaksmile_close
with charachange

"Emi sonríe débilmente, viéndose un poco aliviada."

emi "Bien. En ese caso, será mejor que nos pongamos en marcha."

"El autobús llega poco después de que ella termina la oración."

scene bg city_street4
with shorttimeskip

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_traffic fadein 2.0

"Difusos recuerdos de mi primer viaje hasta aquí me vienen a la mente cuando me bajo del autobús pero, por desgracia, son demasiado difusos para servir de algo."

"No tengo problemas en admitir que no recuerdo muy bien cómo llegar a la casa de Emi, así que la dejo ir primero."

$ renpy.music.set_volume(1.0, 8.0, channel="ambient")
stop ambient fadeout 1.0

scene bg emi_houseext
with locationskip

"Ella parece satisfecha caminando en silencio, y yo no tengo idea de qué decir, así que los dos llegamos a su casa sin decir nada desde que nos bajamos del autobús."

show meiko smile:
    tworight
    xpos 0.8
    easein 0.5 tworight
with charaenter

"La madre de Emi abre la puerta y no parece sorprendida de verme ahí junto a su hija. Imagino que Emi llamó a su madre con anticipación para avisarle del cambio de planes."

show meiko happy at tworight
with charachange

emm "¡Emi, Hisao, llegan justo a tiempo! El almuerzo está casi listo."

show emicas happy at twoleft
with charaenter

emi "¡Genial! Temía que nos estuviéramos retrasando."

hi "Con lo rápido que ibas esta mañana, no creo que esa fuera una posibilidad."

show meiko serious
with charachange

emm "En serio espero que ella no fuera una molestia, Hisao. Tiende a volverse un poco paranoica cuando hay comida de por medio."

hi "No me había dado cuenta."

show emicas pout_up
with charachange

"Con esto me gano un golpe en el brazo de parte de Emi, quien a pesar de la seriedad de nuestra conversación en el autobús y el casi melancólico silencio de nuestra caminata, se ha vuelto más alegre de nuevo."

"Probablemente para evitar que su madre se preocupe por lo que sea que ella planea decirme después."

scene bg emi_dining
with shorttimeskip

"La Sra. Ibarazaki nos indica que pasemos y en poco tiempo estamos alrededor de la mesa devorando el almuerzo."
"No me había dado cuenta de lo hambriento que estaba hasta que llegué aquí, pero por alguna razón parece que estoy comiendo tanto como Emi."

show meiko happy at tworight
show emicas closedsmile at twoleft
with charaenter

emm "Cielos, qué bueno que hice tanto. ¡Están actuando como si no hubieran comido por días!"

hi "Me salté el desayuno esta mañana."

show emicas grin
with charachange

emi "Yo también."

show meiko smile
with charachange

emm "¿Tenían que tomar el autobús, supongo?"

show emicas wink_up
with charachange

emi "Eso y que supuse que harías tanta comida que no importaría si me saltaba el desayuno."

show meiko wink
with charachange

emm "Bien, es bueno saber que soy predecible."

show emicas grin_up
with charachange

"Emi asiente con entusiasmo, y la conversación decae de nuevo mientras prácticamente limpiamos la mesa de cualquier cosa comestible. Es un testimonio a la ingente cantidad de comida disponible que no terminemos con todo."

show emicas grin
show meiko smile
with shorttimeskip

"Me recuesto en mi silla con un suspiro y agradezco a la Sra. Ibarazaki por la comida."

show meiko happy
with charachange

emm "Me alegra que te gustara, Hisao. Ahora, ¿te dijo Emi adónde vamos?"

hi "Sí, algo así. ¿Está lejos de aquí?"

show emicas closedsmile
with charachange

emi "En realidad no, pero conduciremos hasta allá para ahorrar tiempo. Cierran algo temprano."

"Asiento con la cabeza en acuerdo y me levanto, listo para irme."

hi "Muy bien, ¿nos vamos?"

hide meiko
with charaexit

show bg emi_dining at bgright
show emicas awayfrown at center
with dissolvecharamove

"La Sra. Ibarazaki asiente y sale de la sala para recoger sus llaves. Emi, noto, ha empezado a ponerse nerviosa."

hi "¿Lo pensaste mejor?"

show emicas weaksmile
with charachange

"Emi me sonríe con firmeza y se encoge de hombros. Se ha quedado callada de nuevo, lo que probablemente significa que tengo razón y ella está empezando a arrepentirse de haberme traído."

"No es que la culpe; ha hecho tan buen trabajo manteniéndome a oscuras que dudo que sea fácil abrirse de repente. Honestamente, me preocupa que se esté obligando."

"Pero mientras esperábamos por el autobús dijo que no se suponía que le diera una oportunidad de arrepentirse, y ya que prometí ir con ella, supongo que no tengo muchas opciones."
"No puedo darle la espalda a mi promesa, y ella no puede dársela a la suya."

"Solamente espero que ambos estemos a la altura del desafío."

show bg emi_dining at center
show emicas weaksmile at twoleft
with charamove

show meiko happy at tworight
with charaenter

emm "¡Nos vamos!"

"La madre de Emi pasa como un huracán por la sala, nos recoge a ambos, y sale por la puerta con paso enérgico. Ahora sé de dónde lo sacó su hija."

stop music fadeout 4.0

scene bg city_graveyard
with shorttimeskip

"El auto se detiene frente al portón del cementerio, y siento cómo Emi se tensa a mi lado. Me acerco y le doy un apretón consolador en la mano, lo que causa que se relaje un poco."

"La madre de Emi no nos sigue, explicando que prefiere visitar la tumba sola. Emi pasa por el portón y mira hacia atrás, como para asegurarse de que sigo ahí. Caminamos hacia el cementerio."

"No me siento cómodo en los cementerios. Lápidas pueblan el suelo, cada una funcionando como un recordatorio de que alguien solía estar vivo pero ya no."

"¿Cuántos murieron jóvenes? ¿Cuántos eran de mi edad? ¿Cuándo acabaré teniendo mi propia marca? ¿Cuánto tiempo me queda?"

"El concepto de no despertar, no ver a Emi de nuevo, no es uno feliz. Me asusta, y estoy a punto de darme la vuelta y salir de ahí en ese mismo instante."

"No quiero ir junto a la gente muerta, no quiero ver sus tumbas y pensar en quiénes eran o quiénes podrían haber sido si solo hubieran tenido más tiempo."

"Luego miro a la chica junto a mí, y mi determinación regresa. Emi da zancadas deliberadas camino abajo, ojos claros, marcando un ritmo casi de trote. Cuanto antes lleguemos mejor, sospecho que eso es lo que ella piensa."

show emicas weaksmile at center
with charaenter

emi "Llegamos."

scene black
show ev emi_grave:
    truecenter
    subpixel True zoom 0.95
    easein 10.0 zoom 1.0
with whiteout

$ renpy.music.set_volume(0.4, 0.0, channel="music")
play music music_friendship fadein 1.0

"Una lápida, totalmente común y corriente en todo excepto en el nombre grabado en ella. El césped ha crecido alrededor de su base."

"Los ojos de Emi están clavados en la piedra."

scene bg city_graveyard
show emicas neutral at center
with locationchange

$ renpy.music.set_volume(1.0, 20.0, channel="music")

"Luego de unos instantes ella se da vuelta, viéndose sorprendentemente calmada, pero solemne."

show emicas awayfrown
with charachange

emi "El rosado no es mi color favorito."

hi "Eh, ¿qué?"

show emicas frown
with charachange

emi "Estoy calentando."

hi "Ah."

show emicas neutral
with charachange

emi "La gente tiende a pensar que el rosado es mi color favorito. Creo que es porque me gustan las fresas, y aunque sean rojas simplemente asumen que el rosado es el color adecuado para las fresas."

emi "Y que es mi color favorito. Pero no lo es."
emi "Soy demasiado amable como para decirle a nadie lo contrario, claro, y no es del tipo de cosas por las que valga la pena preocuparse, pero apostaría a que incluso tú pensaste que el rosado era mi color favorito."

show emicas weaksmile_up
with charachange

emi "Azul. Ese es mi color favorito. Mi mamá y mi papá son los únicos que saben eso, y ahora tú también."

hi "Gracias por contármelo, creo."

show emicas closedsmile
with charachange

emi "De nada."

"Hay una pausa mientras ella considera qué decir después, tomando una rápida bocanada de aire."

show emicas neutral
with charachange

emi "No podría cantar ni aunque mi vida dependiera de ello. Puedo tararear, pero la verdad cantar una canción es algo que nunca he sido capaz de hacer. No me importa, porque de todos modos no soy fanática del karaoke."

hi "Bueno, eso elimina una posible idea para una cita."

show emicas frown
with charachange

emi "Toda la gente cree que soy una persona realmente amistosa y popular, pero tengo solo unos pocos amigos cercanos. Probablemente porque les oculto todo, pero creo que también es porque detesto la idea de perder a un amigo cercano."

show emicas awayfrown
with charachange

emi "No hay muchas personas por las que valga la pena tomar el riesgo."

show emicas frown
with charachange

emi "Soy terrible con las despedidas."

emi "A veces pienso que solo corro porque es lo que solía hacer con mi padre."

show emicas neutral
with charachange

emi "No eres mi primer novio. Salí bastante tiempo con un chico durante mi segundo año en Yamaku, pero al final rompimos, porque no quería acercarme más a él. Él no podía vivir con esa distancia entre nosotros."

"La velocidad a la que habla aumenta levemente, como si quisiera llegar rápido a la línea final."

show emicas weaksmile
with charachange

emi "En realidad soy un año mayor que tú. Todos creen que soy más joven porque soy baja, pero tuve que saltarme un año de escuela por mi accidente."

show emicas neutral
with charachange

emi "Al inicio, cuando me sacaron de entre los escombros, creyeron que estaba paralizada. Ya había perdido mis piernas, pero temían que ni siquiera podría usar lo que quedó de ellas."

emi "Luego de la cirujía, era claro que se habían equivocado en su diagnóstico inicial. No podía sentir mis piernas por el shock. Parálisis a corto plazo debido al otro trauma que había experimentado."

emi "Mi recuperación fue una de las más rápidas que hayan visto, o eso me dijeron. Nunca averigué si era en serio o si le decían eso a todos los pacientes que intentaban aprender a caminar de nuevo."

show emicas awayfrown
with charachange

emi "Yo…"

"Ella se detiene, preparándose para un último esfuerzo."

show emicas sad
with charachange

emi "Hace ocho años, perdí mis piernas. Y también perdí a mi padre."

emi "Él murió camino al hospital. Ni siquiera pude ir a su tumba hasta dos meses después, y no pude asistir a su funeral."

hi "Lo lamento tanto."

show emicas neutral
with charachange

emi "No lo hagas. Eso es lo que todos dicen, que lo lamentan. Detesto escuchar eso. Como si alguien hubiera podido hacer algo para cambiar lo que pasó."

show emicas frown
with charachange

emi "¿Sabes qué es lo mejor que me han dicho? “Esas cosas pasan”. Ni siquiera recuerdo quién lo dijo, pero supongo que no tenía nada mejor que decir."

show emicas sad
with charachange

emi "Pero es verdad, ¿sabes? Esas cosas pasan, y no hay nada que puedas hacer al respecto. No siempre son planeadas, no siempre son malas, y no siempre son buenas, pero pasan."

emi "Así que tomé la decisión de que viviría sin preocuparme por el futuro. Y para asegurarme de no tener que volver a decir adiós, decidí que ya no dejaría que la gente se acercara a mí."

emi "Después de todo, me los podrían arrebatar en cualquier momento. ¿Y sabes qué?"

"Ella se ríe, con cierta amargura."

show emicas sad_up_close
with characlose

"Sus ojos empiezan a inundarse de lágrimas, y doy un paso adelante para abrazarla pero ella levanta una mano para detenerme."

emi "No he terminado."

"Respira profundamente, y continúa."

show emicas sad_close
with characlose

emi "¡Funcionó bastante bien! Hasta que te conocí y vi que intentabas ajustarte al lugar, así que pensé en ayudarte y después eras tan agradable y no pude evitarlo, yo solo…"

$ ksgallery_unlock("evul emi_cry_down")
show ev emi_cry_down at slow_out_tf
with whiteout

"Ahora las lágrimas fluyen, y esta vez ella acepta el abrazo. El resto de la oración es balbuceada contra mi pecho."

emi "Intenté no enamorarme de ti, pero lo hice. Y luego intenté mantenerte a cierta distancia, como hice con mi primer novio, pero no pude. Pero he estado tan asustada, porque no quiero perderte y aun así podría hacerlo—"

hi "Oye, aún estoy aquí, ¿cierto? Y tal vez no sea para siempre, ¿pero no crees que será divertido mientras dure?"
hi "Puede que ninguno de los dos sobreviva este día, el autobús podría chocar o algo, pero mientras sepa que he estado contigo, no creo que importe."

"Me golpea un pensamiento súbito, y no puedo evitar reírme. Mi condición me tenía tan asustado de morir que aproveché de inmediato la oportunidad que me presentaba Emi para mejorar mis esperanzas de vida."

"Pero sin Emi, ¿habría tenido alguna motivación para seguir corriendo? Me percato de que Emi es la razón por la que quiero correr cada día, para así pasar todo el tiempo que puedo con ella. Emi me mira, confundida."

hi "Viviremos hasta que dejemos de hacerlo. Y cuando dejemos de vivir podremos saber que al menos pasamos tiempo juntos, y no lo cambiaría por nada. Porque te amo, Emi, y en este momento eso es suficiente para mí."

scene bg city_graveyard
show emicas weaksmile_close at center
with locationchange

"Emi sonríe a través de sus lágrimas, y da un paso atrás."

emi "Sabes, es gracioso."

hi "¿Qué cosa?"

show emicas closedsmile_close
with charachange

emi "Pensé que la mejor manera de vivir en el momento era hacerlo sola. Pero ahora, creo que tampoco lo cambiaría por nada. Me alegra haberte conocido, Hisao."

hi "Bueno, esas cosas pasan."

"Emi y yo nos quedamos frente a la tumba por un rato, mientras Emi presenta sus respetos a su padre. Cuando está lista para marcharse, salimos del cementerio juntos."

stop music fadeout 15.0





label es_E31:

scene bg school_gate_ss
with shorttimeskip

"La madre de Emi nos conduce de regreso a Yamaku. El viaje de vuelta es muy silencioso."

show emicas neutral_close_ss
with charaenter

"Nos despedimos mientras el auto se aleja, y miro hacia abajo a la chica que se apoya en mi brazo."

hi "¿Cómo te sientes?"

show emicas awayfrown_close_ss
with charachange

"Emi se encoge de hombros evasivamente."

show emicas frown_close_ss
with charachange

emi "Estaré bien. Vamos, en marcha."

scene bg school_dormext_full_ss
with locationskip

"Nos detenemos frente a los dormitorios de chicas y me doy vuelta hacia Emi, listo para despedirme."

show emicas weaksmile_close_ss
with charaenter

emi "¿Por qué no entras por un rato?"

hi "De acuerdo."

scene bg school_girlsdormhall_ss
with locationskip

"La caminata hasta su habitación transcurre en silencio. No estoy seguro de por qué pensé que nos despediríamos en la puerta."

"Supongo que simplemente asumí que ella quería estar sola."

"Su madre, el enfermero, diablos, todos los que sabían la importancia de este día parecían creer que era mejor dejarla sola."

"Pero Emi me llevó al cementerio con ella. Me contó la historia de todo lo que pasó el día que perdió sus piernas."

"Ella me quería ahí. No ignoro la importancia de eso."

play sound sfx_dooropen

"Emi abre la puerta y entra a su habitación, sin molestarse en invitarme a entrar, sosteniendo la puerta para mí, expectante."

scene bg school_dormemi_ss at left
with locationskip

play sound sfx_doorclose

"Entro, y la puerta se cierra detrás de mí."

show emicas weaksmile_close_ss
with charaenter

emi "Oye, ¿puedo pedirte un favor?"

hi "Claro. No te garantizo que vaya a hacerlo, pero…"

show emicas closedsmile_close_ss
with charachange

"Emi suelta una risita y me atrae hacia un beso que empieza suavemente pero se convierte en algo casi desesperado."

show emicas smile_close_ss
with charachange

emi "¿Quédate conmigo? ¿Por favor?"

"Su voz ha descendido hasta un murmullo, la pregunta apenas es audible sobre el sonido de mi propia respiración."

"Hay algo en la forma en que lo pide, la vacilación, la voz suave, que me hace creer que ella no se refiere a esta noche."

"No, se refiere exactamente a lo que dijo. “Quédate conmigo”. No “esta noche” o “siempre”, porque los dos sabemos que no hay tal cosa como siempre."

"No hay límite de tiempo en su petición, solo la petición."

"El favor."

"¿Puedo hacerlo?"

"¿Puedo quedarme con ella?"

hi "Claro."

play music music_comfort fadein 4.0

show bg school_dormemi_ss at right
show emicas closedsmile_close_ss
with dissolvecharamove

"Nos abrazamos de nuevo, Emi guiándome hacia la cama, caminamos hacia atrás con cuidado hasta que se sienta en la orilla."

label es_E31h:

hide emicas
show eminude smile_close_ss
with charachange

"A estas alturas ya me quitó la camisa, igual a como yo ya levanté la suya sobre su cabeza, incluyendo el sostén. Sus pantaloncillos desaparecen igual de rápido."

"Ella remueve sus piernas con soltura y me jala hacia el costado de la cama junto a ella, mi mano rodeando su suave hombro."

hide eminude
with charachange

"Fijo mi mirada en su rostro, bajando por su cuello, siguiendo la línea donde se forman sus senos antes de bajar mi cabeza, plantando besos en su pecho, escuchando su respiración irregular mientras su mano se desliza más y más bajo mi pecho."

"Mientras avanzo de regreso a su cuello, puedo sentir sus manos trabajando en mi faja, ahora peleándose un poco con la hebilla, ahora desabotonando, ahora bajando la cremallera, hasta que mis pantalones caen al suelo."

"Sus pantaletas están notablemente oscurecida en el lugar correcto, demostrando que mi ayuda previa produjeron resultados."

"Doy un paso atrás con rapidez y me deshago de mis bóxers, y me acerco de nuevo mientras Emi alcanza una gaveta de su mesita de noche, agarrando un paquetito de aluminio."

"Lo abre de un rápido tirón con los dientes y se agacha para aplicar la protección, lo que, como siempre, provoca que yo suelte un pequeño suspiro."

"Su expresión cambia de repente cuando me mira bien."

show eminude evil_close_ss
with charaenter

emi "Espera un segundo… ¿Todavía llevas tus calcetines?"

"Me detengo, miro hacia abajo. Aparentemente, sí."

hi "Eh, sí. ¿Acaso importa?"

show eminude frown_close_ss
with charachange

emi "Quítatelos, es raro si todavía los tienes puestos."

hi "Sabes, tú también tienes los calcetines puestos."

show eminude closedsmile_close_ss
with charachange

emi "Sí, pero no tengo puestas las piernas. Así que no cuenta."

"Incapaz de negar su lógica e impaciente por terminar con la conversación, me apresuro para remover los objetos infractores."

"Estoy tan ansioso por regresar con Emi que prácticamente salto sobre ella, empujándola hacia abajo juguetonamente."

scene evh emi_miss_closed
with whiteout

"Las risitas y movimientos de Emi terminan rápidamente, reemplazados por un suspiro de alegría mientras entro en ella. Respirando profundamente mientras saborea la sensación, ella extiende los brazos para agarrarse a las sábanas."

"Siento su respiración en mi oído cuando comienzo a moverme. Me susurra palabras de aliento, mordisquea mi cuello y ahora mi boca."

"Mis caderas golpean el borde del colchón, sacudiendo la cama. Una parte de mi cerebro se pregunta brevemente si debería intentar ser más silencioso antes de sucumbir a las oleadas de placer que recorren mi columna."

scene evh emi_miss_open
with charachange

"El estómago de Emi se tensa mientras ella se acerca al límite, y mientras nuestros cuerpos empiezan a brillar con sudor, el tiempo comienza a volverse difuso."

"El sonido de mi propia respiración se mezcla con los jadeos de Emi, y me preparo para un embate final antes de rendirme a la precipitada oleada de placer."

"El cuerpo de Emi se estremece, y ella gime, sus dedos clavándose en mi espalda mientras yo también pierdo el control."

"Mi espalda se contrae mientras me dejo llevar, sintiendo espasmos en mi cuerpo por el orgasmo."

label es_E31x:

scene bg school_dormemi_ss at right
with shorttimeskip

"Colapso junto a Emi, quien casi de inmediato se acurruca junto a mí, sonriendo."

"Mentalmente, me siento agradecido de que Emi mantenga sus uñas cortas, de no ser así podría haberme sacado sangre."

"Me siento por un instante mientras me deshago del condón usado y me acuesto de nuevo junto a Emi, quien a su vez se está encargando de limpiarse a sí misma."

"Por un rato permanecemos en silencio, saboreando la sensación de estar juntos."

"Emi es la primera en hablar."

show eminude smile_close_ss
with charaenter

emi "Oye, Hisao."

hi "¿Hmm?"

show eminude closedsmile_close_ss
with charachange

emi "Gracias por venir hoy conmigo."

"Sonrío y planto un beso en su cabeza."

show eminude blush_close_ss
with charachange

hi "Por supuesto. El placer es mío."

show eminude closedsmile_close_ss
with charachange

"Emi se acurruca aún más cerca, y puedo sentir su respiración aflojándose mientras empieza a quedarse dormida."

"Justo cuando está por dormirse, se despierta lo suficiente como para murmurar una oración."

emi "Te amo, Hisao."

"Y luego se apaga como una bombilla, dejándome con la sensación de estar en la cima del mundo."

"Atraigo a la durmiente Emi lo más cerca posible, coloco las sábanas sobre nosotros para evitar el frío, y me quedo dormido más feliz que nunca."

stop music fadeout 2.0

$ suppress_window_after_timeskip = True

scene black
with dissolve



label es_E32:

window hide None

scene black
with dissolve

scene bg school_dormemi
with openeye

window show

"La luz de la mañana parece penetrar más profundamente en el cuarto de Emi que en el mío."

"Esto provoca que me despierte más temprano de lo que lo habría hecho si hubiera regresado a mi habitación anoche, como había sido nuestra rutina anterior."

"No me di cuenta hasta esta mañana, pero esta es la primera vez que realmente pasamos una noche juntos."

play music music_twinkle fadein 1.0

"Un leve movimiento proveniente de la figura aún dormida de mi acompañante me hace mirar hacia el lado."

"Con el cabello extendido por su cara, Emi continúa durmiendo acurrucada tranquilamente a mi lado."

"Es un poco raro verla sin sus características coletas, pero es una vista a la que podría acostumbrarme."

"El limitado tamaño de estas camas la obliga a acurrucarse, pero estoy seguro de que lo habría hecho de todas formas."

"Las sábanas casi cubren su cabeza, y sonrío cuando una hebra errante de cabello provoca un leve tic en su nariz."

"Incapaz de contenerme, la atraigo un poco más cerca, un movimiento que ella parece considerar una buena idea."

"Su calmada respiración desata una serie de escalofríos en mi pecho, pero no me importa."

"Ya no estoy cansado, pero no siento la necesidad de moverme de mi posición actual."

"El cálido cuerpo de Emi reposando junto al mío es demasiado agradable como para moverme."

"Dirijo mi mirada al techo y considero cómo es que llegamos a este punto. Hemos sido cercanos por un tiempo, pero no así de cercanos."

"Parece como si hubiera sido ayer que ella chocó contra mí en el pasillo y luego de disculparse decidió interesarse en mi bienestar."

"Pero eso se convirtió en algo más, algo que al menos yo no esperaba."

"Una cosa es cierta: ya que encontré a Emi, intentaré con todas mis fuerzas no perderla."

"Mis reflexiones matutinas son interrumpidas por más movimientos de Emi."

"Abre los ojos de golpe, y se ve brevemente confundida por mi presencia en su cama y por sus vestiduras, que son inexistentes."

scene ev emi_ending_smile
with whiteout

"Luego sonríe alegremente y se sienta, mirándome desde arriba."

emi "Buenos días, Hisao."

hi "Hola. ¿Dormiste bien?"

emi "Sí. Sí, lo hice. Día agotador el de ayer, ¿sabes?"

"Rememoro el viaje de ayer al cementerio."

hi "Sí. Me alegra escuchar que dormiste bien."

emi "¿Cómo dormiste tú?"

hi "Bastante bien, aunque tú seguías adueñándote de las sábanas…"

"Con esto me gano un golpe y una mueca con la lengua. Suelto una risita, y Emi ríe infantilmente, y nos quedamos en silencio por un rato."

"Me empapo en la sensación de lo bien que se siente todo esto, despertar junto a Emi, apretujados en una cama para una persona."

"Es algo a lo que podría acostumbrarme."

emi "Oye, Hisao…"

hi "¿Hmm?"

emi "Gracias por quedarte."

hi "No pasa nada. Me ahorró la caminata de regreso, ¿cierto?"

scene ev emi_ending_serious
with charachange

"Esto consigue otra risita, pero la expresión de Emi se vuelve seria de nuevo."

emi "No, de verdad. Yo seguía intentando empujarte lejos, porque pensaba que era lo correcto, y tú permaneciste aquí a través de todo."

emi "No te he facilitado ninguna de estas cosas, pero tú aguantaste sin importar qué."

emi "Así que de verdad, lo digo en serio. Gracias."

scene ev emi_ending_smile
with charachange

"Ella puntúa esto dándome un beso, retrocediendo y mirándome con una expresión de afecto."

"Me acerco y hago círculos en su cabello, sonriendo mientras tanto. Soy estúpidamente afortunado, creo."
"Haber pasado por tanto después de mi ataque cardiaco y de alguna manera haber encontrado a esta chica no es poco menos que un milagro."

hi "No tienes que agradecerme, Emi."

"No podía soportar la idea de dejarte ir."

hi "Incluso seguiré estando aquí, si quieres."

emi "Eso me gustaría."

"Eso lo decide, entonces. No sé por cuánto tiempo seguirá funcionando mi corazón, y en realidad ni siquiera sé qué haré cuando acabe este año, aparte de ir a la universidad."

"Siempre y cuando Emi esté ahí, creo que estaré bien. He conseguido ayudarla, y ella consiguió ayudarme. Si seguimos haciendo eso, estaremos bien, creo."

emi "Y bien, Hisao."

hi "¿Hmm?"

scene ev emi_ending_glad
with charachange

emi "¿Qué quieres hacer hoy?"

window hide

stop music fadeout 3.0

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
