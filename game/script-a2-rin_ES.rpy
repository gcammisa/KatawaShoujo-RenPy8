label es_R1:






window hide None











scene bg school_scienceroom
with locationchange

with Pause(1.0)

play music music_normal fadein 6.0

window show

"Ya son las ocho y media, pero esta clase de la mañana aún no ha comenzado. Se supone que deberíamos haber tenido Física, pero el maestro no se ve por ningún lado."

"De haberlo sabido de antemano, también me hubiera quedado dormido."

play sound sfx_doorslam
with vpunch

"Repentinamente la puerta del salón se abre de un portazo y Mutou nos gruñe su saludo matutino desde la entrada."

show muto normal at center
with charaenter

mu "¡Buenos días a todos!"

"Parece que Mutou no ha dormido en absoluto."

"La barba de varios días, su cabello más despeinado de lo normal y la camisa de vestir manchada crean una impresión poco favorable."

"Supongo que se divirtió en el festival anoche, también."

show muto irritated
with charachange

mu "Disculpen la tardanza, me encontré con problemas inesperados. Usualmente no soy dado a festivales como este, pero espero que todos hayan pasado un buen rato."

mu "Después de todo, este tipo de eventos son importantes para todos ustedes, ya que les dan un corto respiro del trabajo escolar."

show muto normal
with charachange


"El grupo responde con diversos niveles de entusiasmo, y Mutou procede a pasar lista y a empezar la clase."

mu "Bien, entonces. El tema de hoy es la Física del fotón."

hide muto
with shorttimeskip

"En poco tiempo he descendido a un confortable estado similar al coma junto con el resto del grupo, dejando que los farragosos discursos de Mutou entren por un oído y salgan por el otro sin dejar rastro."

show muto normal at center
with charaenter

mu "Bien, ¿quién podría decirnos la solución a este problema?"


"Mutou ha escrito una ecuación bastante sencilla en el pizarrón. Trata desesperadamente de lograr que el grupo participe."

show muto irritated
with charachange

mu "¿Nadie? Vamos, muchachos. Nakai, ¿qué hay de ti?"

"Injustamente señalado y acorralado, le doy una respuesta. Esto hace que sus rasgos desaliñados se tuerzan en una jovial sonrisa que horrorizaría a niños pequeños."

show muto smile
with charachange

mu "¡Precisamente! ¡Buen trabajo, Nakai!"


"Me siento tanto perturbado como honrado por el hecho de que pueda recordar mi nombre tan solo una semana después de haber sido transferido."

"Por lo que he visto, Mutou tiene serios problemas para recordar los nombres de cualquier otra persona en el grupo, y casi todos ellos han estado aquí desde el primer año."

"El salón se asienta en un humor lóbrego, con los estudiantes y el maestro tratando de encarrilarse después del festival."

"Me imagino que la semana pasada debió de haber estado muy agitada para todos."

play sound sfx_normalbell

stop music fadeout 2.0

"Ni un minuto antes de tiempo, suena la campana para el almuerzo."

scene bg school_hallway3
with locationchange

play music music_running

mystery "¡ABRAN PASO! ¡ASUNTO IMPORTANTE!"

"Vuelvo la cabeza justo a tiempo para ver a otras personas dispersarse fuera del camino, mientras alguien se lanza desde el extremo lejano del corredor hacia las escaleras."


"Es demasiado tarde para darme cuenta de que estoy de pie en medio del corredor, directamente dentro de la trayectoria del proyectil humano que se aproxima."

"Trato de retroceder hacia la puerta. Desafortunadamente, la persona que corre hacia mí esquiva en la misma dirección."

"En la siguiente fracción de segundo, varias cosas me vienen a la mente en sucesión, aunque casi de manera simultánea."

"Primero, reconozco que la chica que se encuentra en rumbo de colisión contra mí es Emi."

"Segundo, advierto que de alguna forma se siente muy natural el ser embestido por Emi una vez más. Podría casi sentirme cómodo, de no ser por el reflexivo pánico y terror."

"Tercero, Emi parece estar cargando con una pila de papeles 30 centímetros de alto mientras corre por el pasillo."

play sound sfx_pillow
with vpunch

"Ella se estrella contra mí, pero por lo menos esta vez el impacto fue de un rozón con mi brazo."

show emi sad_depressed at center
with charamoveinbottom


emi "Aayyy… ¿Por qué me pasa esto siempre a mí?"




hi "Caray, me pregunto por qué. ¿Acaso podría tener algo que ver contigo corriendo por el pasillo como si te estuvieras quemando?"

show emi sad_shy
with charachange


"Ella gimotea arrepentida, viéndose como un cachorrito lastimado. El espectáculo me hace lamentar la respuesta brusca el mismo instante que emerge de mis labios."

show emi sad_pout
with charachange

emi "Pero… Estaba apurada."


hi "Puedo verlo."

emi "Lo siento."

hi "No te preocupes por eso."

show emi sad_shy
with charachange


"Emi se lamenta débilmente una última vez y se frota la frente como si quisiera expulsar el dolor mientras su mirada pasa por el piso del pasillo."


"El momento en que se percata de que su ordenada pila de papeles se ha esparcido por todo el piso en un gran desastre, deja escapar un grito de horror."

show emi basic_shock
with charachange

emi "¡Aah! ¡Las impresiones! Oh no oh no, ¿qué voy a hacer? El maestro me crucificará si se ensucian."

hi "Probablemente estén bien. Vamos a juntarlas, no será problema."


"Terminamos rápido de juntar los papeles, y Emi trata de organizar con las manos el montón desparramado de vuelta a la pila ordenada que era."

show emi basic_grin
with charachange

emi "¿Adónde vas?"

hi "A ningún lugar en particular, supongo. No quería quedarme solo con Mutou en el salón. Creo que tiene resaca."

show emi excited_happy
with charachange

emi "¿Ya almorzaste?"

hi "Todavía no, pero no tengo mucha hambre de cualquier modo."

show emi basic_confused
with charachange

"Ella me mira con incredulidad, como si dudara de mi cordura por haber dejado salir tal cosa de mi boca."

show emi excited_proud
with charachange

emi "¡Deberías de ir a la azotea! Le prometí a Rin que almorzaría con ella. Apuesto a que le gustaría la compañía."

"Oh, oh. Mis almuerzos con Rin han sido notablemente infructuosos."


"Sé adónde está yendo esta conversación y es difícil no dejarse llevar, así que no tengo más opción que cooperar."

hi "Está bien, iré a comprar un poco de pan o algo, primero."

show emi basic_closedgrin
with charachange



"Emi sonríe brillantemente antes de que yo diga algo más."

show emi basic_grin
with charachange

emi "No no, iré a entregar estas superrápido y luego iré a comprar el almuerzo para nosotros. Y para Rin también, por supuesto. ¿Qué tipo de pan te gusta?"


hi "Así está bien, en realidad no tienes que…"

show emi excited_proud
with charachange

emi "No te preocupes, está bien. Considéralo una disculpa. ¡Estaré de vuelta antes de que te des cuenta!"

hi "Eso es lo que me preocupa. No te metas en otro accidente."

"Emi comienza a caminar por el pasillo, pero como sigue hablando conmigo, no está viendo por dónde va."

show emi basic_closedhappy
with charachange

emi "¡No lo haré!"

hide emi
with charaexit

stop music fadeout 4.5

"Célebres últimas palabras. Ya está bajando al trote por las escaleras mientras me grita esa no muy tranquilizante promesa."

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 2.0

scene bg school_staircase1
with locationchange


"Suspirando en silencio, comienzo a andar con paso pesado tras su camino. Pero en lugar de tomar las escaleras para abajo, voy hacia arriba."

"La escalera a la azotea está sin iluminar e igual de sobrecogedora que antes."

play sound sfx_dooropen

"La puerta chirría débilmente en protesta mientras la empujo para abrirla."

play sound sfx_door_creak
$ renpy.music.set_volume(1.0, 0.5, channel="ambient")


scene bg school_roof
with Fade(0.5, 0.0, 2.0, color="#FFF")

"Rin está ahí también, como dijo Emi, por alguna razón acostada boca arriba al otro lado de la azotea cubierta de grava."

"Prediciendo algo innecesariamente extraño otra vez, camino hacia ella tan lento como sea posible."

scene ev rin_roof_boredom
with locationchange

rin "Hoooolaa."


"Suena muy somnolienta al decir eso, estirando la palabra con una voz arrastrada. A pesar de eso, sus ojos se encuentran bien abiertos."

show hisao rin_roof
with charaenter


"La miro hacia abajo, mi sombra cubriendo su cara."

hi "¿Qué estás haciendo?"

show ev rin_roof_doubt
with charachange

"Rin levanta una ceja."

show ev rin_roof_nonchalant
with charachange

rin "Pensé que tenías un problema con el corazón, no un problema de la vista."

"Ella responde, desafiando la razón de mi pregunta perfectamente válida sin siquiera inclinar la cabeza para verme."


"Los comentarios de sabelotodo de Rin son exasperantes. Lo peor de todo es que no sé si lo está haciendo a propósito o no."


hi "Muy bien. Entonces déjame reformularlo:"

hi "¿Por qué estás acostada en la azotea?"

show ev rin_roof_boredom
with charachange

"Se encoge de hombros con pereza y aspira con desdén."

rin "Estoy tratando de experimentar. Probablemente la gente no lo hace lo suficiente."

hi "¿Exactamente qué es lo que estás tratando de experimentar? Realmente no puedo notarlo, pero probablemente hay una razón para que la gente no haga… como sea."


"Está jugando conmigo de nuevo, respondiendo mi intento de charla con acertijos que no quiero resolver."

"Pero no la quiero ignorar, tampoco."

show ev rin_roof_nonchalant
with charachange

rin "Sí, pero la razón de eso es que todos están demasiado ocupados con sus vidas como para prestarle atención a las cosas realmente importantes."

hi "¿Como ver el cielo?"

show ev rin_roof_surprised
with charachange

"Aparta la vista del cielo y por fin me ve directamente. La penetrante profundidad de sus ojos una vez que los centra en algo es sorprendente."


rin "Sabes, si fueras una chica podría verte las pantaletas."


hi "Si fuera una chica, no estaría tan cerca de alguien que tratara de echarle un ojo a mis pantaletas. Tengo ese mínimo de sentido común."

show ev rin_roof_boredom
with charachange

rin "Yo tampoco lo haría, pero hay veces que no puede evitarse. Como ahora, por ejemplo."

show ev rin_roof_nonchalant
with charachange


rin "Aunque, a decir verdad, ni siquiera quiero verte las pantaletas."


rin "La ropa interior es el alma de una chica. No deberías husmear en el alma de alguien. Aun si no eres una chica."

hi "Como chico, supongo que puedo entender eso. Para nosotros, son algún tipo de objeto semimítico que no podemos comprender del todo."

show ev rin_roof_surprised
with charachange

rin "Sí, exactamente así es como también pienso yo. Qué coincidencia."

hi "En verdad lo es."

hi "Entonces, ¿tuviste Historia Universal en las clases de la mañana?"

show ev rin_roof_doubt
with charachange


rin "Falté a clases."

hi "¿Para hacer esto?"

show ev rin_roof_boredom
with charachange

rin "Bueno, en verdad no estoy haciendo lo que parece que estoy haciendo, o al menos creo que lo que estoy haciendo no parece lo que yo aparento, pero desde tu perspectiva…"

extend " probablemente…"


rin "Sí, falté a clases para hacer esto."

hi "Supongo que cualquiera que sea tu razón, es tan buena como cualquier otra."

hide hisao
with charaexit

play sound sfx_rustling

scene bg school_roof
with locationchange

"Cediendo a la sensación de cansancio en mis piernas, me siento en la azotea, enseguida de Rin."

"Las piedras no son la cama más comoda en el mundo, pero si ella puede soportarlo, entonces yo también debería poder hacerlo."

rin "¿Qué estás esperando?"

hi "¿Hmm?"

rin "Inténtalo."

stop music fadeout 2.0
$ renpy.music.set_volume(0.4, 3.0, channel="ambient")

"Inclino la cabeza hacia atrás para echar un vistazo hacia donde ella está viendo."

scene bg misc_sky at Fullpan(40.0)
with locationchange


"El cielo azul plateado, salpicado por rebaños de nubes de ovejas, llena por completo mi campo visual."

"Aunque bonito, la vista no es para nada especial, incluso si hay buen tiempo."


"Me encojo de hombros, haciendo mi mejor esfuerzo por imitar la forma indiferente que Rin parece haber desarrollado a la perfección, y me recuesto boca arriba."


"Las piedras se clavan en mi espalda a través de la delgada camisa cada vez que trato de moverme aunque sea un poco, obligándome a mantenerme tan quieto como sea posible."

"Trato de ignorar la incomodidad y a mí mismo, en su lugar me concentro en la inmensidad sobre nosotros."

"Muy en lo alto, las nubes de verano vuelan a la deriva por el domo del cielo."


"Ninguno de los dos tiene algo más que decir, y así el silencio cubre la azotea."

"Los ruidos apagados de estudiantes en la hora del almuerzo, cigarras en los árboles y el zumbar del tráfico más allá de la escuela resuenan agradablemente en algún lugar en el fondo."

hi "Escucha, lo pasé genial ayer."

rin "¿En serio?"

hi "Bueno, para ser honesto, no. Pero estuvo bien. Probablemente fue el tiempo más largo en el que he estado sentado en un solo lugar sin hacer nada, lo que es un poco impresionante."

"Trato de que suene tan convincente como sea posible."

rin "¿Es eso impresionante?"

hi "Creo que lo es. Usualmente soy demasiado inquieto como para hacer algo como eso."

rin "También creo que la pasé bien."

"Una nube pasa sobre nosotros, proyectando su sombra sobre la escuela."

"Un escalofrío me atraviesa por el súbito cambio de luz a sombra."


"Me doy cuenta de que el verano no está en su máximo apogeo todavía."

"La única medida del tiempo transcurrido es el lento paso de las nubes desplazándose hacia el pueblo."



"Algunos rayos dorados de luz de sol se filtran a través de los espacios, cegándome por un momento cada vez que llegan a mis ojos directamente."

"El azul del cielo parece tan inalcanzable."

"Esto me recuerda al tiempo que pasé en el hospital, donde todos los días estaba tremendamente aburrido."

"De algún modo, no era problema después de un tiempo. Aprendí a apreciar otras cosas además de ver televisión y chismear con gente que ni siquiera me agrada."

"Una sensación de tranquilidad generalizada se extiende desde mi vista hacia mis demás sentidos, finalmente llegando a mi cerebro."

"Un avión pasa volando, dejando dos delgadas estelas detrás como un par de líneas de tiza dibujadas en el cielo de un extremo al otro."

"Me pregunto hacia dónde se dirige."

"El estruendo apagado de sus motores llega hasta acá, a mis oídos, aunque puede apenas oírse sobre el barullo del patio."

stop ambient fadeout 8.0
$ renpy.music.set_volume(1.0, 10.0, channel="ambient")

rin "Es agradable."

hi "Es agradable, pero no puedo comprender por qué esto es más importante que ir a clases."

rin "¿Acaso no es bueno hacer algo que te gusta?"

rin "¿De vez en cuando?"

hi "Por supuesto, pero—"

stop sound

emi "¿Qué están haciendo?"

"Emi se nos ha escabullido sin que ninguno de los dos se diera cuenta y se encuentra a tan solo un paso de mí, sosteniendo entre sus brazos varios paquetes envueltos en plástico."

show emi excited_happy_close:
    xalign 0.5 yanchor 1.0 ypos 1.2
    easein 0.5 center
show bg misc_sky at right
with charaenter


"Ella se inclina hacia adelante y se asoma sobre mí, proyectando su sombra sobre mi rostro casi exactamente del mismo modo que yo lo hice con Rin antes."

"Me pregunto qué tan raro se ve esto, ambos tendidos sobre nuestras espaldas en la azotea."

hi "Eso es lo que también pregunté."


rin "Yo estaría más preocupada sobre qué es lo que tú estás haciendo. Si fuera tú, no me acercaría tanto a la gente que pudiera verme las pantaletas."

play sound sfx_pillow

show emi sad_angry_close
with vpunch

play music music_comedy fadein 0.5

emi "¡Rin!"

show emi sad_angry_close:
    easeout 0.5 ypos 1.2 alpha 0.0
with None

scene bg school_roof
with locationchange

show emi basic_hes:
    xalign 0.5 yanchor 1.0 ypos 1.1
    easein 0.5 center
with charaenter

"La voz de Emi se escandaliza, pero pronto da un paso atrás, presionando sus manos contra el frente de su falda tan abruptamente que los paquetes de pan con los que cargaba se caen."

"Rápidamente aparto la vista, y miro con enojo a Rin. Ella pretende no verme."

show emi basic_shock
with charachange

emi "Hisao no es así, ¿verdad?"

hi "Así es."

play sound sfx_rustling

show emi basic_shock:
    parallel:
        ease 0.5 ypos 1.17
    parallel:
        "emi basic_annoyed" with Dissolve(0.5, alpha=True)
    ease 0.5 ypos 1.0
with Pause(1.0)

"Emi le frunce el ceño a Rin y se agacha a recoger los paquetes."

play ambient sfx_rooftop fadein 8.0

show emi basic_grin_close
with characlose

show emi basic_grin_close:
    ypos 1.12
with charamove

"Ella los limpia de polvo y salta con agilidad alrededor mío hacia el otro lado de Rin, donde se sienta."

emi "Como sea, aquí está tu pan. Perdón por haberme tardado."

hi "Está bien. Gracias por invitarme."

"Me levanto a una posición de sentado y acepto con gratitud el pan que Emi está ofreciendo."

"Los tres vorazmente atacamos la sencilla comida. El pan está sorprendentemente pasable y sin problemas me llena el estómago."

show rin invis:
    yanchor 1.0 ypos 1.2 xanchor 0.5 xpos 1.0
with None

show emi basic_grin_close:
    xpos 0.3
show bg school_roof at bgleft
show rin basic_awayabsent_close:
    ease 1.0 ypos 1.07 xpos 0.9
with dissolvecharamove

"Con el rabillo del ojo sigo la habilidad con la que Rin maneja el pan entre sus pies."

show emi excited_proud_close
with charachange


emi "No te he visto en la pista desde hace unos días."

show rin basic_absent_close:
    ypos 1.07 xpos 0.9
with charachange

hi "Oh. Cierto, yo… pensé que empezar con esa rutina era demasiado pesado para mí."

show rin basic_awayabsent_close
show emi basic_hes_close
with charachange

emi "¿Así que has estado haciendo otra cosa?"

show rin basic_absent_close
with charachange

hi "He estado considerando mis opciones."

show emi basic_annoyed_close
with charachange

"Ella frunce el ceño pero no insiste más al respecto, por lo cual estoy agradecido."

"Emi parece ser muy testaruda y realmente no quisiera que me molestara sobre esto a diario. Ya tengo suficientes responsabilidades que soportar con Shizune y Misha."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

play sound sfx_warningbell
show rin basic_awayabsent_close
show emi basic_shock_close
with charachange

"Apenas terminamos el almuerzo antes de que las campanas suenen, llamándonos de vuelta a nuestros salones."

stop ambient fadeout 0.5
$ renpy.music.set_volume(1.0, 1.0, channel="music")

scene bg school_scienceroom
with locationskip

show misha sign_smile at center
with charaenter

mi "¡Hicchan!"

"Misha me saluda con la mano tan pronto como entro, y comienza a hablar antes de que siquiera haya cruzado el salón."

show misha hips_smile
with charachange

mi "¿Cómo estuvo tu festival? ¿Te divertiste?"

hi "Ehhh… todavía algo indeciso al respecto. Diría que “probablemente”."

hi "¿Por qué?"

show misha hips_grin
with charachange

mi "¡Guajaja~, solo preguntaba, solo preguntaba!"

"Sus ojos brillan de una manera que me dicen que ella no solo estaba preguntando. Sin embargo, no puedo ni imaginarme sus motivos."

hide misha
with charaexit


"Como la oportuna entrada del maestro de inglés nos impide hablar más de ello, Misha cambia al plan B."

window hide

show misha hips_grin_close at offscreenleft
with None

show misha perky_smile_close:
    xpos 0.1 xanchor 0.5
show bg school_scienceroom at left
with charamove

$ written_note(u"¡Estuve ahí todo el día con Shicchan! ¡Nos divertimos muchísimo!", text_args={"color":"#FF2AAA"})


$ written_note(u"¿No se suponía que estarían trabajando?")

show misha hips_grin_close
with charachange

$ written_note(u"¡No te preocupes! Todo salió muy bien.", text_args={"color":"#FF2AAA"})

window show


"No respondo a eso, y me deja a solas después de que Shizune exige su atención."

stop music fadeout 12.0

show misha invis at offscreenleft
with dissolvecharamove

hide misha
show bg school_scienceroom:
    subpixel True yalign 0.0
    ease 30.0 zoom 1.1
with None

"Mi propia atención, por otro lado, está dirigida hacia fuera de la ventana."

"Ahora que lo veo desde aquí, a través de la ventana y el follaje justo afuera, el cielo parece más pequeño."


"Distingo tan solo pequeños atisbos de azul; todo lo demás es un montón de ruido justo en medio de mi campo visual."


"¿Qué “experiencia” quería obtener Rin de mirar el cielo? De seguro lo ha hecho antes. Todos lo han hecho."


"No sirve de nada tratar de adivinar en lo que ella pensaba, pero si no lo hago, entonces no tengo excusa para no concentrarme en las palabras del maestro."

"Miro los garabatos que aparecen en el pizarrón, tratando de averiguar su significado con poco éxito."


"Inglés, definitivamente, no es mi materia favorita. Tenemos una fuerte aversión mutua."

stop music fadeout 2.0



label es_R2:

scene bg school_hallway3
with shorttimeskip

play music music_normal fadein 3.0
play sound sfx_normalbell

"La fuerte y caliente luz de la tarde invade el corredor, haciendo que el aire se sienta pesado y apacible."


"Mi cuerpo se siente agobiado por ello mientras lo arrastro dos puertas por el pasillo hacia el salón de arte."


"Tal vez esta sea parte de la razón por la que no me uní a ningún club antes: las tardes simplemente no son adecuadas para actividades."

scene ev rin_artclass1
with locationchange


"Llamo a la puerta del salón de arte y la abro. Una chica que posiblemente estaba haciendo algo importante con ese pliego de papel que está llevando, se da vuelta para evaluarme y sonríe con dulzura, si bien de manera un poco confundida."

show ev rin_artclass2
with charachange

"Estudiante" "¿Hola…?"

hi "Este es el club de arte, ¿no?"

"Estudiante" "Síp. ¿Interesado en unirte?"

hi "Sí. De hecho, puede que ya lo haya hecho, pero ya veremos."

show ev rin_artclass3
with charachange


"Le doy una sonrisa débil, y la suya aumenta de grado, haciéndome sentir menos nervioso."

"Estudiante" "¡Genial! Toma asiento, entonces. Empezaremos ya que el maestro llegue."

show ev rin_artclass4
with charachange

"Sin siquiera explorar el salón por un buen lugar, camino rápido hasta el fondo del salón y me siento en un lugar libre, apartado de todos los demás."

"Algunos otros miembros están descansando en sus asientos, esperando al maestro. Rin se sienta sola en un lugar cerca de la ventana, viendo hacia afuera."
"Ella es la única persona que conozco, aunque un tipo de mi salón con el que nunca me he llevado está aquí también."

"Nadie viene a saludarme —¿quizás las presentaciones son dejadas para después?— así que también me conformo con la observación silenciosa."


"Un chico tiene gafas de sol; una imagen inusual en los interiores, si no estuviéramos en Yamaku. Apuesto a que se trata del estudiante ciego del que Rin estaba hablando."

stop music fadeout 2.0
play sound sfx_footsteps_hard fadein 0.2

scene bg school_classroomart at left
with locationchange

"La espera prueba ser extremadamente corta."

stop sound
play music music_happiness fadein 2.0

show nomiya smile at center
with charaenter

"Nomiya camina tres largas zancadas para pararse detrás de su escritorio, luego da una sonrisa y un saludo extravagante."

show nomiya veryhappy
with charachange

no "¡Buenas tardes a todos!"

show nomiya talk
with charachange

no "Primero lo primero: Hisao es un nuevo miembro, así que todos llévense bien con él."

"Me guiña un ojo perturbadoramente."

"Los ocho miembros del club, incluyéndome a mí, respondemos su saludo con bastante menos entusiasmo. Aun así, la gente finalmente se endereza en sus asientos y comenzamos a prestar atención."

show nomiya smile
with charachange

no "Creo que algunos de ustedes todavía tienen proyectos en los que trabajar, así que por favor continúen en ellos, si así lo desean."

show nomiya talk
with charachange


no "Y para el resto, estaba pensando que este día podríamos bocetar algunos estudios."

show nomiya veryhappy
with charachange

no "¿Qué les parece?"

"Nadie responde, a excepción de algunos murmullos ininteligibles que Nomiya aparentemente interpreta como una aprobación unánime."

show nomiya talk
with charachange

no "¡Pues muy bien! Todos los que no están trabajando en otros proyectos, escojan un compañero y dibujen un boceto el uno del otro."

no "Deberían ser capaces de completarlo este día, pero si no, podemos continuar la próxima vez, o incluso hacerlo de nuevo si les resulta interesante."

show nomiya veryhappy
with charachange

no "Recuerden prestar atención a la iluminación y las sombras, ¡y hagan su mejor esfuerzo!"

"¿Parejas? Me siento bastante incómodo al respecto, ya que difícilmente conozco a alguien aquí. Ojalá alguien me pidiera ser su compañero."

hide nomiya
with charaexit


"Los alumnos se ponen de pie y mueven sus sillas para estar más juntos, pero nadie viene hacia mí."

"Pronto todos los demás tienen pareja. Amigos se juntan entre sí, pero yo quedo solo."

"Bueno, está Rin."

show bg school_classroomart at right
with charamove

"Ella está sentada en el rincón más lejano del salón, aún mirando hacia fuera de la ventana y aparentemente desinteresada en tomar parte en el ejercicio."

"Ya que ella es la única otra persona sin pareja, camino hacia su asiento."


"No puedo verle el rostro porque el cabello lo cubre en su mayoría, y no está viendo hacia mí."

hi "¿Rin?"

"La llamo en voz alta. No hay respuesta."


hi "Hola, ¿quieres ser mi compañera? Eres la única que conozco aquí."

show rin basic_absent at center
with charaenter

"Parece que finalmente reconoce mi presencia, girando su cabeza como un robot a la vez que mira quién le dirige la palabra."

"…"

"Rin no responde, y tampoco quiero repetir la pregunta. Estoy seguro de que la escuchó la primera vez."

"…"

"¿Por qué no dice nada? No puede ser un destino tan terrible tenerme de compañero, ¿o sí?"

"No me mira a la cara, y en su lugar se queda mirando directamente a mi pecho y estómago."

"…"

show rin basic_deadpan
with charachange

rin "Oh, está bien. ¿Por qué no?"

"…"


hi "Está bien. Muy bien. Genial. Iré por las cosas para nosotros."

hide rin
with charaexit

show bg school_classroomart at left
with charamove



"Viendo el equipo que Nomiya ha preparado para la reunión de hoy me confunde. En lugar de grafito o lápices, se supone que hagamos bocetos con tinta."

"Nunca he hecho algo así antes."

"El maestro, sin embargo, parece confiar en mis habilidades para adaptarme a este medio."

show nomiya veryhappy at center
with charaenter

no "¡Sencillo!"

show nomiya smile
with charachange

no "Primero haces el contorno en tinta. Dejas que se seque, y luego lo sombreas con tinta diluida. Esto se conoce como tinta china, funciona como las acuarelas."

show nomiya talk
with charachange

no "Si te sientes incómodo con eso, usa una pluma en lugar de un pincel para el contorno."

hi "Entendido."

hide nomiya
with charaexit

"Tomo papel, dos vasos con agua, una pluma para mí, un pincel para Rin y tinta para los dos, entonces regreso con Rin."

show bg school_classroomart at right
with charamove

show rin basic_absent_close:
    center
    ypos 1.1
with charaenter

"Alcanzándome una silla desocupada de cerca, me siento directamente opuesto a ella."

show rin negative_spaciness_close
with charachange

stop music fadeout 1.0

rin "¿Quieres que lo haga con mi pie o con la boca?"

hi "¿Qué dijiste?"

play music music_another fadein 2.0

show rin relaxed_surprised_close
with charachange



"Ella inclina la cabeza a un lado y sus cejas forman dos arcos interrogantes, como si ella no comprendiese que yo no entendiera la pregunta."

show rin basic_deadpan_close
with charachange

rin "No me molesta dibujar de cualquier manera. Aunque te verás mejor si lo hago con el pie."

hi "Con el pie, entonces, si da lo mismo para ti."

show rin basic_deadpannormal_close at center
with dissolvecharamove

"Asintiendo en respuesta, Rin se levanta de su asiento y se quita las sandalias."

show rin basic_awayabsent_close:
    center
    ypos 1.17
with dissolvecharamove

"En dos fluidos movimientos, ella levanta la hoja de papel y la deja caer en el suelo, luego toma el pincel entre los dedos antes de sentarse en el piso en una posición extraña con las piernas cruzadas."

"Aunque ya la he visto hacer todo con sus pies, desde comer hasta pintar, esta demostración de destreza es tan prodigiosa que simplemente me le quedo mirando, anonadado."

show rin negative_annoyed_close
with charachange


"Rin contempla su papel en blanco atentamente. La afilada punta de su pincel se cierne sobre el pliego con anticipación."

show rin basic_deadpancontemplation_close
with charachange

"Cuando levanta su cabeza para ver si estoy listo, rápidamente vuelvo mi rostro."

show rin basic_deadpan_close
with charachange

rin "Yo iré primero. Haz una pose."

hi "¿Qué tipo de pose?"

show rin basic_lucid_close
with charachange

rin "No importa. Ese es el punto. Tienes que hacer un boceto de la impresión que tienes, no decidir de antemano."

"Termino sentado en mi silla con las manos colgando lánguidamente entre las rodillas."

show rin basic_deadpanupset_close
with charachange

"La miro, y ella me mira por un momento antes de empezar."


"La mirada de Rin es penetrante pero imperturbable, como si estuviese tratando de absorber una parte de mí dentro de sí misma. Siento como si me estuviese encogiendo físicamente bajo la presión de su mirada."


"Tengo la sensación de que, por primera vez desde que nos conocimos, Rin está realmente mirándome, en lugar de en la dirección en la que estoy."

show rin negative_annoyed_close
with charachange

"Ella dibuja con confianza, trazos atrevidos con el delicado pincel, sin importarle las consecuencias potencialmente destructivas de una pincelada fuera de lugar."

show rin basic_absent_close at center
with dissolvecharamove

"Ya que está contenta con el contorno, se levanta para posar para mí, estirando su espalda y piernas."

show rin basic_awayabsent_close
with charachange


"Esta vez no me mira. En vez de eso, Rin deja a su mirada pasearse por el salón. Me siento aliviado, es más fácil observar a alguien cuando no te están viendo."

"Aun así, me resulta difícil hacer el dibujo."


"No tengo algún talento artístico especial, por lo que temo que mi retrato termine siendo algo deforme, en especial al ser comparado con la habilidad de mi compañera."

"No quiero avergonzarme demasiado en el primer intento."


"Rin tampoco está ayudando en el proceso."

show rin negative_annoyed_close
with charachange

"No se mantiene quieta por siquiera diez segundos, inclinando su cabeza de lado a lado para juzgar su dibujo, mordiéndose el labio inferior, viéndose insatisfecha y moviéndose constantemente como si estuviera parada sobre brasas ardientes."

show rin basic_awayabsent_close:
    center
    ypos 1.17
with dissolvecharamove

"Finalmente logro un avance en mi dibujo, y con mi contorno hecho, ambos comenzamos a entintar la luz y la sombra."

show rin basic_awayabsent_close:
    tworight
    ypos 1.17
show bg school_classroomart at center
with charamove

show nomiya smile behind rin at twoleft
with charaenter

"Nomiya va pasando y hace comentarios sobre los inicios de nuestros dibujos."

show nomiya veryhappy
with charachange

no "¡Muy bien! La figura de pie es más fácil de comprender para un principiante."

hi "Pero yo no escogí la pose…"

hide nomiya
with charaexit

"En confusión, lo miro a él y luego a Rin, pero el maestro ya se ha pasado a la siguiente pareja, y Rin parece indiferente."

show rin basic_awayabsent_close:
    center
    ypos 1.17
show bg school_classroomart at right
with charamove


"Al igual que cuando estaba pintando el mural, Rin se encuentra tan absorta en su trabajo que parece ser que nos ha dejado fuera a mí, al salón y al mismo mundo entero de su propia pequeña burbuja existencial."

"Cada tanto se inclina hacia atrás, aparentemente para tener algo de perspectiva. Algunas veces se inclina hacia adelante, acercándose hasta que su nariz casi toca el papel."

"Este estarse meciendo hacia adelante y hacia atrás se ve ridículo."

"Súbitamente, Rin demuestra no haberse sumido completamente en un mundo propio, y habla."

show rin negative_spaciness_close
with charachange

rin "¿Ya te estás divirtiendo?"

"No levanta su mirada del dibujo, lo cual es algo bueno. El rompimiento del silencio envía una descarga de sorpresa a través de mí, como si hubiese sido electrocutado."

hi "Yo… no lo sé, todavía. Es difícil decirlo."

show rin basic_awayabsent_close
with charachange

"No puedo escuchar cómo contesta a mi respuesta, porque parece que repentinamente está teniendo una conversación privada en voz baja con su dibujo."

"No entiendo cómo puede dibujar tan bien cuando tiene el periodo de atención de una mariposa."

"Como parece que perdió su interés, también voy de vuelta a trabajar en mi dibujo."

"Intento añadir textura al cabello de Rin para, de alguna manera, captar el modo en que la dorada luz de la tarde enciende su cabello despeinado en llamas y transferirlo a mi papel en tonos de negro y gris."

"Por alguna razón, esta pluma y frasco de tinta dan la impresión de ser herramientas tan pésimas e inadecuadas para la tarea."

"Los minutos pasan, pero el dibujo no se ve mágicamente más como Rin que como se veía antes. Su voz me despierta de mi desgracia."

show rin basic_deadpannormal_close
with charachange

rin "¿Qué tal ahora?"

hi "¿Disculpa?"

show rin basic_deadpan_close
with charachange

rin "¿Ya te estás divirtiendo?"

hi "¿Por qué sigues preguntando eso?"

show rin basic_deadpancontemplation_close
with charachange

rin "Porque es un club, ¿o no? Los clubes se supone que deben ser divertidos. Te uniste para divertirte. ¿Te estás divirtiendo?"

hi "¿Es importante que me esté divirtiendo?"

show rin basic_deadpanupset_close
with charachange

rin "… Sí."

hi "… Está bien, me estoy divirtiendo."

show rin basic_lucid_close
with charachange

rin "Bien."

"Me pregunto si dije eso solo para complacerla, o si realmente quise decirlo. Realmente no puedo decidir cuál fue."

"Sin embargo, no lo odio. Puedo decir eso honestamente. Es lo suficientemente bueno por ahora."

stop music fadeout 2.0

scene bg school_classroomart at right
with shorttimeskip

"A medida que el tiempo asignado para terminar los estudios transcurre con rapidez, trato desesperadamente de mejorar mi horrible dibujo, pero no parece hacerlo."

"Quiero empezar de nuevo desde cero, pero ¿cuál sería el punto? Tampoco hay tiempo para eso."

play music music_daily fadein 2.0


no "Bien, muchachos, ¡eso es todo por hoy! Por favor dejen sus dibujos sobre mi escritorio, ¡y los veré a todos el próximo lunes!"

show ovl rinbyhisao:
    center
    ypos 1.5 alpha 0.0
    easein 1.0 ypos 1.0 alpha 1.0
with Pause(1.0)

"Le echo un vistazo a mi retrato. No se ve exactamente como Rin. Supongo que podría decirse que la retrata, pero eso tal vez sería un poco generoso."

"La nariz y la quijada se ven horrendas, y el sombreado es terrible. Claro, es mi primer intento de dibujar con tinta, pero sigue estando muy mal."

rin "Eso no está mal."

show rin basic_deadpanamused_close behind ovl at center
with None

show ovl rinbyhisao:
    easeout 1.0 ypos 1.5 alpha 0.0
with Pause(1.0)

hide ovl
with None

"Se escabulló detrás de mí mientras estaba perdido en mis pensamientos."


hi "Maldición. Tenía la esperanza de poder dárselo al maestro a escondidas sin que lo vieras."

show rin basic_surprised_close
with charachange

rin "¿Por qué?"

hi "No estoy realmente contento con esto. Quisiera poder dibujar mejor."

show rin basic_deadpannormal_close
with charachange

rin "Tan solo necesitas un poco de práctica. ¿Podrías llevarle mi dibujo al maestro, también?"


"Curioso por saber cómo quedó el dibujo, le echo una mirada. Por la manera en la que Rin estaba dibujando, parecía que estaba realmente concentrada."

show ovl hisaobyrin:
    center
    ypos 1.5 alpha 0.0
    easein 1.0 ypos 1.0 alpha 1.0
with Pause(1.0)


"Es excelente. De algún modo los trazos aparentemente arbitrarios se unen para formar una imagen de mi rostro, desde la forma de mi barbilla, al cabello alborotado, a la expresión un tanto pesimista."

label es_choiceR2:
menu:
    with menueffect
    "Su dibujo es sorprendente."
    "¡Eres impresionante!":


        return m1
    "Quisiera ser tan bueno como tú.":

        return m2

label es_R2a:

hi "Guau, eres impresionante."

rin "No es tan impresionante."

rin "Pero gracias."

label es_R2b:


hi "Guau, desearía ser así de bueno. Me avergüenzo un poco de mí mismo."

rin "¿No tendrías que ser yo para ser tan bueno como yo? No creo que quisieras ser yo."

hi "No, supongo que no. Tal vez tan solo algún tipo de aproximación."

label es_R2c:

show ovl hisaobyrin:
    yalign 0.0 subpixel True
    easein 20.0 zoom 1.1
with None

"Le doy una mirada más de cerca a su trabajo. Todavía reluce con la tinta secándose lentamente."

hi "Sabes, me veo algo malhumorado."

rin "Te ves un poco malhumorado. Quiero decir, estoy de acuerdo; pero también es cierto del otro modo. Como este tú, no el tú que yo hice."

hi "¿En serio?"

rin "Eso creo, al menos."


"Su simple afirmación súbitamente me da una sensación sumamente embarazosa. Siento que necesito un espejo ahora mismo, para confirmar o desmentir lo que dice Rin. Es una sensación desagradable."

"Tal vez es solo ella. Espero que sea solo ella y que no me vea como ese dibujo para todos."

"Es un buen dibujo, pero de alguna manera me viene una sensación muy opresiva de este."

show rin basic_absent_close
with None

show ovl hisaobyrin:
    easeout 1.0 ypos 1.5 alpha 0.0
with Pause(1.0)

hide ovl
with None

hi "Ya veo. De cualquier modo, se ve muy bien. En verdad eres impresionante."

show rin basic_deadpandelight_close
with charachange

rin "Gracias. Me alegro de poderte haber dibujado. Eres una persona interesante."

hi "Tú también eres una persona interesante, pero eso no me ayudó mucho."

"Mi autodesprecio hoy no tiene límites, pero Rin lo ignora todo. Sabía que nunca me podría comparar, pero ver la diferencia con mis propios ojos es bastante humillante."

show rin basic_awayabsent_close
with charachange

rin "Sabes, traté de hacer que te vieras como si pensaras mucho, ya que pensaste mucho."

show rin basic_deadpanamused_close
with charachange

rin "Y sí, puede que haya exagerado la expresión de “estoy harto de la vida”, pero los cínicos son así, ¿no?"


"Quiero replicar con algo cortante, pero Nomiya no me da tiempo de pensar al momento que nos conduce a la puerta."

show rin basic_deadpanamused_close at tworight
show bg school_classroomart at center
with charamove

show nomiya talk behind rin at twoleft
with charaenter

no "¡Apresúrense, ustedes dos!"

"Mientras estábamos charlando, el resto del club se ha marchado."

hide rin
with charaexit

"Rápidamente tomo mis dibujos y los llevo al escritorio del maestro antes de darme prisa detrás de Rin, quien ya ha salido del salón."

stop music fadeout 4.0



label es_R3:

scene bg school_hallway3
with locationchange

"No se encuentra en el pasillo, para mi sorpresa. Me pregunto adónde habrá logrado correr en tan solo unos pocos segundos. Hubiera sido agradable platicar más."

"Bueno, no es que tuviera mucho que decir, excepto tal vez vengarme por llamarme cínico."

"Es sorprendentemente tarde. Ya me acostumbré a que la escuela termine en el mismo tiempo todos los días, así que puedo sentir las horas extras en mi cabeza. Y en mi estómago."

"Los gruñidos de mi estómago me recuerdan que estoy absolutamente famélico. Tengo tanta hambre que me atrevería a tratar de comer cualquier cosa que el personal de la cafetería considere como comestible."

scene bg school_cafeteria
with locationskip

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 1.0


"Incluso al ver las delicias de hoy, trozos misteriosos fritos, mi férrea determinación no se desvanece. Me trago la cena sin saborearla en lo más mínimo, lo cual es probablemente lo mejor."

"No tengo mucha tarea por hacer, pero la poca que tengo no se hará por sí sola, así que camino hacia los dormitorios."

stop ambient fadeout 0.5
scene bg school_dormhallway
with locationskip

$ renpy.music.set_volume(0.0, 2.0, channel="ambient")
play sound sfx_doorknock2

"Preparándome para la calma después de la tarea, llamo a la puerta de Kenji."

"Responde desde el otro lado, aunque no puedo entender lo que dijo. Trato de abrir la puerta, pero está cerrada con llave."

show kenji neutral at Slide(0.2,0.5,0.3,0.5,1.0)
with charaenter


"Unos segundos más tarde, se oye el ruido de cerrojos y la puerta se abre."


hi "Hola. Oye, ¿podrías prestarme un libro? La biblioteca ya estaba cerrada cuando salí de la reunión del club."

show kenji tsun
with charachange


"Él entrecierra los ojos más de lo común, y sus cejas se estremecen con nerviosismo."

play music music_kenji fadein 2.0



ke "¿Club? Viejo, eso es peligroso. Adoctrinamiento, pensamiento de grupo, lavado de cerebros, hay de todo."


ke "Los clubes escolares siembran las semillas de la conspiración. ¿Sabes cuántas sociedades secretas han crecido a partir de clubes escolares?"

ke "Ten cuidado y no te metas mucho en eso. Podrías no regresar."

hi "Está bien, Kenji. Entonces, ¿qué hay del libro?"

show kenji neutral
with charachange

ke "Eh, seguro, pero los regresas y no eches a perder ninguno de mis libros. Sin bebidas, ni manchas de comida, ni fluidos corporales, ¿capisce?"

hi "Seguro. Gracias."

show kenji invis:
    xpos 0.2
with dissolvecharamove

"En lugar de dejarme entrar, se aleja de la puerta, cerrándola de nuevo."

show kenji neutral at Slide(0.2,0.5,0.3,0.5,1.0)
with charachange

"Unos segundos más tarde, regresa con una pila de tres libros gruesos y me los entrega."

"Al abrir el que está hasta arriba, me saluda un emblema familiar estampado en la página de derechos de autor."

hi "Eh, ¿tus libros? Estos son de la biblioteca de la escuela."

show kenji happy
with charachange

ke "Ahora son míos."

hi "¿Los robaste?"

show kenji tsun
with charachange


ke "¿Hombre, de qué estás hablando? He estado liberándolos del opresivo movimiento feminista que controla la biblioteca."

hi "Por favor di que el “opresivo movimiento feminista” no se refiere a esa pobre bibliotecaria, Yuuko. Ella no podría ni oprimir una toalla húmeda."

show kenji invis:
    xpos 0.2
with dissolvecharamove

hide kenji
with None

stop music fadeout 3.0

"Kenji se da la vuelta, balbuceando algo que no puedo entender, y cierra la puerta detrás de sí."

scene bg school_dormbathroom
with locationchange

play ambient sfx_shower fadein 1.0

"Antes de ir a mi habitación, entro al baño. Al lavarme las manos, la reflexión del espejo sobre el lavabo capta mi atención."

$ ksgallery_unlock("ev hisao_mirror_800")
scene ev hisao_mirror:
    zoom 1.0 xalign 0.5 yalign 0.5 subpixel True
    ease 20.0 zoom 0.8
with locationchange

"Trato de buscar el mal humor que Rin vio en mí, pero es el Hisao usual que me mira de vuelta dentro del espejo."

"Intento decirme a mí mismo que así es como siempre me he visto, pero me doy cuenta de que no recuerdo cómo me veía hace medio año."

stop ambient fadeout 6.0

$ suppress_window_after_timeskip = True

scene black
with Dissolve(2.0)







label es_R4:

window hide None

scene black with dissolve

scene bg school_dormhisao
with openeye

window show

"Despierto empapado en sudor, como si hubiera corrido medio maratón mientras dormía."

play music music_pearly fadein 5.0


"Qué raro, no recuerdo haber dormido mal. Me atraviesa un sentimiento de inquietud, no quisiera que a mi corazón le pasara algo sin poder darme cuenta de ello."

"Aun así, aparte de este extraño agotamiento justo antes de despertar, me siento muy bien."

"Mi boca se siente como una lija y no tengo nada para beber, así que tengo que ir hasta el baño para tomar mis medicamentos. Siguiendo un impulso, decido ducharme ya que estoy en eso."

scene bg school_dormbathroom
show steam
with locationskip

play ambient sfx_shower fadein 1.0

"Mientras estoy en la ducha, decido que esto cuenta como ejercicio matutino, si lo compenso apropiadamente con una agradable caminata de media hora después de clases."


"No quisiera correr el riesgo de sufrir posibles complicaciones por ir a correr ahora, obviamente. Además, Emi nunca sabrá, y creo que está perdiendo la fe en mí, de cualquier modo."

"Caminar sería agradable, de todas formas, solo para conocer el lugar."

"Hay un gran bosque en las colinas detrás de la escuela, o podría ir al minisúper."

hide steam
with charaexit
stop ambient fadeout 1.0



"Mientras seco la humedad en mi piel, decido ir por mi uniforme."

"Rápidamente abotono mi camisa y me subo el pantalón antes de salir."

scene bg school_courtyard
with locationskip


"Normalmente, en esta época del año, estaría esperando ansiosamente las vacaciones de verano. Como he estado aquí poco más de una semana, realmente no tengo ese tipo de sentimientos."

"Todavía estoy saboreando la vida escolar y, considerando el abrupto y complicado giro que mi vida ha tomado, no he tenido el tiempo de preocuparme por liberarme de ella."

"Además, ya que lleguen las vacaciones, me serán una grata sorpresa si no las estoy esperando. Especialmente con los exámenes finales que se avecinan."

"Por lo menos no tengo que ponerme al día con el estudio. Mi esmero por fin ha dado frutos."

"Me abro camino a través de los chicos reunidos en la puerta y me desplomo en mi asiento."

stop music fadeout 2.0

scene bg school_scienceroom
with locationskip

"Desde el rabillo del ojo puedo ver a Shizune y a Misha suspender su conversación inevitablemente animada, y voltear casi al mismo tiempo en mi dirección."

"Claramente quieren algo de mí, puedo notarlo por la manera en la que Shizune sonríe. Es demasiado amplia para ser sincera y demasiado calculada para ser espontánea."

show shizu behind_smile at tworight
show misha perky_smile at twoleft
with charaenter

play music music_normal fadein 2.0

mi "¡Buenos días~!"

"Su saludo está hecho de un cien por ciento de alegría y energía desbordante."

hi "Buenas."

"Fracaso al tratar de poner alguna de estas en mi respuesta."

show misha perky_confused
with charachange

mi "No te ves con muchas energías."

hi "No es sorpresa, tampoco me siento con muchas energías. Creo que no dormí bien, pero no estoy seguro."

show misha hips_grin_close
with vpunch

"Me da una palmada en la espalda y sonríe."

show misha hips_smile_close
with charachange

mi "¡Anímate un poco! ¡Es un día grandioso~!"

show shizu basic_normal2
with charachange


"Me encuentro con la mirada de Shizune. Tiene una extraña y concentrada expresión en el rostro, pero frunce el ceño un poco con el contacto visual directo y mira hacia otro lado."

show shizu adjust_happy
with charachange

"Por un momento pienso que Shizune alcanza a ver mis preocupaciones, de algún modo, y está pensando en cómo responder. Pero entonces endereza sus anteojos rápidamente, y con eso, su expresión."

show shizu basic_happy
with charachange

shi "…"

show misha sign_smile_close
with charachange



mi "De cualquier modo, nos estábamos preguntando si sigues interesado en aquella posición en el consejo estudiantil, porque te haremos una oferta que no puedes rechazar~."

hi "Espera, ¿qué? No estaba realmente interesado en primer lugar. Estás poniendo palabras en mi boca."

show shizu adjust_smug
with charachange

shi "…"

mi "No es así. Pero, ¿no sería agradable pasar el rato con nosotras todos los días mientras también le eres de utilidad a tu escuela?"

hi "Bueno, a decir verdad, yo… como que ya me uní a un club. Así que, de hecho, sería un poco pesado para mí también unirme al consejo estudiantil."

hi "Incluso si quisiera. Lo cual no es así, como dije."

show shizu behind_blank
with charachange

shi "…"

show misha cross_smile_close
with charachange

mi "¿En serio? ¿Cuál club es, Hicchan~?"

hi "El club de arte."

show shizu cross_angry
with charachange

shi "…"

"Los ojos de Shizune destellan de una manera siniestra mientras me mira con el ceño fruncido."
"Con cómo me mira, estaré esperando que el club de arte pierda sus fondos antes de que termine la hora del almuerzo, o que el maestro de arte desaparezca de la faz de la Tierra de manera misteriosa."

hide shizu
hide misha
with charaexit

"Antes de que ella alcance a comentar, el maestro finalmente entra al salón, quitándome a Shizune y a Misha de encima y mandando a todos a hurgar en sus mochilas por sus libros y plumas."

"Sí me uní al club de arte, pero la primera reunión no aumentó mi confianza, realmente. En realidad no estoy seguro de para qué lo estoy haciendo."

"Desearía poder dibujar como Rin, pero no sé lo que haría si pudiera. ¿Para qué fines usaría tal habilidad? Realmente no lo sé."

$ renpy.music.set_volume(0.5,  1.0, channel="music")

show ev hisaobird_0:
    center
    alpha 0.0 ypos 1.5
    easein 0.5 alpha 1.0 ypos 1.0
with Pause(0.5)


"Ignorando la voz con capacidades inductoras de sueño del maestro, abro mi cuaderno en una página en blanco y presiono la punta del lápiz, tan aguda como una aguja, sobre esta."

"¿Qué dibujaré?"

"En verdad no puedo pensar en nada bueno que dibujar."

show ev hisaobird_1:
    center
    alpha 1.0
with charachange


"En lo que dudo y levanto la mano, una tímida marca negra que queda en el papel anteriormente en blanco parece desagradable."

"Parezco no poder siquiera obtener la línea inicial, mucho menos empezar. Es casi una sensación física de ser retenido. De un modo irritante, me recuerda a mi intento fallido de trotar con Emi."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

show ev hisaobird_1:
    center
    easeout 0.5 alpha 0.0 ypos 1.5
show bg school_scienceroom:
    yalign 0.0
    ease 20.0 zoom 1.1
with Pause(0.5)

hide ev
with None

"Miro por la ventana con desesperación. Justo entonces, un pajarito alza el vuelo desde uno de los cerezos que crecen por doquier en el campus de la escuela."



"En realidad no pude verlo con claridad, y no es como si pudiera diferenciar un diminuto pájaro de otro. Pero lo elijo como mi tema de estudio, de cualquier modo."

$ renpy.music.set_volume(0.5,  1.0, channel="music")

show ev hisaobird_1:
    center
    alpha 0.0 ypos 1.5
    easein 0.5 alpha 1.0 ypos 1.0
with Pause(0.5)

show ev hisaobird_2:
    center
    alpha 1.0
with charachange

"Evocando la imagen de un pájaro con el ojo de mi mente, regreso mi mirada de vuelta a mi cuaderno y deliberadamente dibujo una gruesa línea a través de la hoja para comenzar."

"Parece estarse burlando de mí, ya que no puedo seguir de inmediato. De cualquier modo, es un comienzo. Comenzar es bueno."

show ev hisaobird_3
with charachange

"Poco a poco dibujo la imagen sobre la hoja del cuaderno, la imagen en mi mente se vuelve más clara a medida que el dibujo toma forma."

show ev hisaobird_4
with charachange


"En verdad no es nada, tan solo ese pájaro cualquiera y sin nombre sobre el papel, pero eso no es importante."

show ev hisaobird_5
with charachange

"Mi vacilación se desvanece hacia el fondo junto con la voz del maestro mientras continúo con mi lucha. Las plumas forman un patrón simple en mi mente, pero en el papel es un desastre de demasiadas líneas toscas a pesar de mi mejor esfuerzo."

show ev hisaobird_6
with charachange


"Me doy cuenta de que en realidad no sé cómo es que un ala de pájaro debería de verse, aun si trato de pensar en ello. Incluso dejo el lápiz y cierro los ojos por un momento, tratando de trazar su figura en mi mente."

show ev hisaobird_7
with charachange

"Que me lo tome tan en serio de manera tan repentina me hace sentir un poco frustrado."

show ev hisaobird_8
with charachange


"La clase de arte en la secundaria era la clase “fácil” entre materias agotadoras como matemáticas o japonés. Pero está este otro lado del arte, el que ves cuando no estás solamente haciéndote el tonto."

show ev hisaobird_9
with charachange

"Es algo casi completamente diferente."

stop music fadeout 0.5

mi "¿Hicchan?"

show bg school_scienceroom behind ev:
    center
    zoom 1.0
show shizu behind_blank_close behind ev at closeright
show misha cross_smile_close behind ev at closeleft
with None

show ev hisaobird_9:
    center
    easeout 0.5 alpha 0.0 ypos 1.5
with Pause(0.5)

hide ev
with None

"Volteo hacia arriba para ver a dos chicas mirándome."

$ renpy.music.set_volume(1.0,  0.0, channel="music")
play music music_comedy fadein 1.0

"Misha y Shizune han traído sus sillas hasta mi banco y están ahora de pie a mis lados, viendo mi dibujo."

hi "¿Cuánto tiempo han estado ahí?"

show misha hips_grin_close
with charachange

mi "Creo que necesitas más práctica."

show shizu basic_normal_close
with charachange


"Shizune traza algunas señas con gravedad en el aire entre ella y Misha."

show misha sign_smile_close
with charachange

mi "Shicchan está de acuerdo."

"Rin dijo exactamente lo mismo ayer, pero ¿por qué sonó menos condescendiente?"

hi "No deberían de juzgar antes de que haya acabado."

hi "Además, ¿qué no saben que es de mala suerte ver una pieza de trabajo sin acabar?"

show misha cross_laugh_close
with charachange

"Misha rompe en una risa exuberante."

show misha hips_grin_close
with charachange

mi "¿Qué? ¡No seas tonto~! Eso no puede ser verdad."

hi "Como sea."

show shizu adjust_frown_close
with charachange

"El ceño de Shizune se frunce peligrosamente, y los movimientos de sus manos se vuelven abruptos, como el cortar de un cuchillo."

show shizu behind_frown_close
with charachange

shi "…"

show misha hips_frown_close
with charachange

mi "Deberías aprender a tomar mejor las críticas constructivas."

hi "Lo haría si ustedes sí ofrecieran alguna."

"Sé que me estoy poniendo demasiado a la defensiva y que Shizune está tomando partido de ello, pero no puedo evitarlo."

hi "¿Qué están haciendo ustedes dos aquí, a todo esto?"

show shizu basic_frown_close
with charachange

shi "…"


"Misha menea su dedo de modo reprensivo frente a mi nariz."

show misha sign_smile_close
with charachange

mi "Tch, tch, Hicchan. ¿Qué acaso no estabas escuchando al maestro?"

show shizu behind_blank_close
with charachange

shi "…"

show misha hips_smile_close
with charachange

mi "Tenemos un trabajo en grupo, ahora."

"Asiento desalentado, y dejo que tomen las riendas."

show misha hips_grin_close
with charachange

mi "Así que, ¿qué piensas de la lección de hoy?"

hi "No gran cosa… No escuché ni una sola palabra de ella."

show misha hips_frown_close
with charachange

"Misha se da una palmada en la frente y sacude la cabeza teatralmente."

mi "¿Cómo le vamos a hacer contigo, Hicchan?"


"Afortunadamente, Shizune y Misha juntas son más eficaces que tres o cuatro personas normales, así que puedo holgazanear en la mayor parte del ejercicio."

"Hago mi mejor esfuerzo para ofrecer por lo menos un poco de ayuda, pero termino siendo prácticamente inútil."

stop music fadeout 2.0

scene bg school_scienceroom
with shorttimeskip

play sound sfx_normalbell

"El maestro nos mantiene en el salón cinco minutos después de que sonara la campana para el almuerzo, pero eventualmente nos deja salir."

"Rápidamente meto mis libros en mi mochila mientras Shizune y Misha cargan sus sillas de vuelta a sus lugares."


"El intento fracasado de dibujar un pájaro termina arrugado y embutido en mi bolsillo a la vez que me apresuro a salir."

stop music fadeout 2.0

scene black
with dissolve




label es_R5:

scene black
with locationchange

"Después de esa clase en la mañana, y durante toda la semana, sigo topándome con Rin."

window hide

scene bg school_hallway3
show crowd
show rin basic_absent at center
with delayblinds

play ambient sfx_crowd_indoors fadein 2.0

window show

rin "Hola."

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

window hide
nvl clear
nvl show dissolve

play music music_daily fadein 2.0

n "\n\nEsto es un tanto natural, ya que nuestros salones son contiguos. Pero en lugar de solo cruzar nuestros caminos en el pasillo, como la gente normalmente lo hace, parece que nosotros hacemos una pausa al vernos el uno al otro."

n "Invariablemente terminamos charlando un poco, o tan solo pasando juntos el rato, en silencio."


n "Creo que me estoy acostumbrando a estar en silencio en compañía de Rin, ya que ha dejado de sentirse tan incómodo como antes. Yo soy, por naturaleza, un poco introvertido al igual que ella, así que encajamos bien."

n "Creo que, de hecho, es una anomalía que alguien en esta escuela sea tan callado. A la mayor parte de la gente aquí parece que le encanta socializar."

n "\nEs algo de lo que ya me había percatado, incluso si no he estado aquí por mucho tiempo: La gente aquí habla mucho, y lo hace todo el tiempo."

nvl clear

n "\n\nEs un caso raro cuando veo a alguien sentarse solo, únicamente mirando al vacío o algo similar. Obviamente aquí también hay gente así; esa chica Hanako y yo, tan solo para nombrar dos de mi propio grupo. Pero en general, son la minoría."

n "En cualquier caso, tampoco llamaría exactamente lo que Rin y yo hacemos “socializar”, pero es algo, por lo menos."

n "Estas ocurrencias por sí mismas no me molestan, pero el hecho de que lleguen a ocurrir lo hace."


n "Dudaría en afirmar que algo nos une, pero ciertamente actuamos como si así fuera."

n "\n\nSin embargo, esta sensación de una incipiente amistad es completamente destrozada cada vez que Rin abre la boca."

nvl hide dissolve
nvl clear
window show

stop music fadeout 0.5
stop ambient fadeout 0.5

show rin basic_deadpannormal_close
with characlose

rin "¿Puedo escuchar latir tu corazón?"

play music music_rin fadein 0.5
$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 4.0

"Ella dice esto, u otra cosa igual de escandalosa, y tengo que librarme de cualquier tontería que su mente ha elucubrado durante la clase anterior de alguna materia en la que ella no está interesada."

"Parece que Rin le tomó interés a mi condición del corazón, como algún tipo de extensión de su interés en las discapacidades más extrañas que la gente aquí tiene, y en las consecuencias de dichas aflicciones."

"Al estar parado frente a ella por un segundo de más, viéndome tan desconcertado como me siento, ella concluye que es necesario aclarar aún más su petición."

show rin basic_deadpan_close
with charachange

rin "Sé que puedo, pero quiero decir, ¿me dejas?"

hi "¿Por qué?"

show rin relaxed_doubt_close
with charachange

rin "¿Necesito una razón? Suelo ser muy mala con las razones."


hi "No necesariamente, pero si quieres hacerlo, probablemente sí tengas una razón."

show rin basic_deadpanamused_close
with charachange

rin "Eso es algo ingenioso. Eres más inteligente de lo que pareces."

hi "Además, preferiría que no lo hicieras. Pienso que este tipo de cosas deberían de ser privadas."

show rin basic_deadpandelight_close
with charachange

rin "Privadas. Entendido."

hi "Aunque puedo decirte algo, si esto te divierte; estoy bastante seguro de que así será. Mi corazón sí suena muy raro. A causa de… tú sabes, la condición."

hi "Y lo oigo. Todo el tiempo."

show rin negative_spaciness_close
with charachange

rin "Así que estás paranoico."

"Eso no es una pregunta, es una afirmación."

hi "No, no estoy paranoico. Los doctores dijeron que la atención anormal al latido del corazón es un síntoma común de mi… condición."

show rin basic_deadpannormal_close
with charachange

rin "Así que, para ti, es normal ser paranoico."

"Eso tampoco es una pregunta."

hi "Uno también podría decir que el que yo me encuentre así no es normal, en primer lugar, pero qué más da."

hi "La paranoia me sienta bien."

show rin basic_lucid_close
with charachange


rin "No creo que sea algo que realmente pueda sentar bien en alguien o en alguna parte."

show rin basic_deadpan_close
with charachange

rin "Sabes, comí una naranja como desayuno hoy."

hi "¿Qué tal estaba?"

"Me siento ligeramente orgulloso de mí mismo, por haber logrado seguir el súbito cambio de tema de Rin."

show rin basic_amused_close
with charachange

rin "Excelente. No recuerdo cuándo fue la última vez que comí una naranja. Porque es molesto pelar una."

show rin basic_delight_close
with charachange

rin "Está en la lista de cosas que quiero aprender a hacer apropiadamente."

hi "¿Cómo fue que comiste una, entonces?"

show rin basic_deadpanamused_close
with charachange

rin "Emi tenía unas, así que peló una para mí."

hi "Bien por ti."

show rin relaxed_nonchalant_close
with charachange

stop music fadeout 6.0

"Rin estira la espalda, bosteza, y no dice nada más."

"Me lanza una mirada desde el rabillo del ojo mientras ve gente pasar, pero no podría decir por qué."

"Me doy cuenta, sin embargo, que esta es la primera vez que he hablado de manera natural sobre mi condición con alguien. De cierto modo."

stop ambient fadeout 4.0

"Un grupo de muchachos nos pasa caminando hacia el salón de clase de Rin, pero ella no les presta ninguna atención. Ellos tampoco le prestan ninguna a ella. Mi mente divaga, alentada por el silencio."

window hide
nvl clear
nvl show dissolve

$ renpy.music.set_volume(0.5,  0.0, channel="music")
play music music_pearly fadein 1.0

n "\n\n\nQuizás debería haberle permitido escuchar mi corazón. No es como si importara. Nada realmente importa tanto, al final de cuentas."


n "Comienzo a sentirme deprimido sin razón, de nuevo. Es como una oleada de la nada, oprimiendo mi consciencia, sumergiéndome bajo el agua."

n "Siento un suspiro salir de mi boca, y giro apartándome de Rin, pretendiendo leer un cartel sobre la pared. Es un anuncio para el festival escolar, promocionando un evento de casi una semana atrás."

n "La diferencia entre Rin y yo es que es más probable que yo esté muerto que vivo antes de cumplir treinta, mientras que ella no puede comer naranjas sin ayuda."

n "\n\nNo puedo decidir quién de nosotros la lleva peor."




nvl hide dissolve
nvl clear

scene black
with delayblinds

nvl show dissolve

n "\n\n\nTrato de captar el paso del tiempo, pero lo encuentro difícil. Todavía sigo acostumbrado al ritmo del hospital, donde trivialidades como el día de la semana o la hora realmente no importaban."

n "Todo era lo mismo, sin importar qué."

n "Redescubrir el significado del tiempo es una experiencia extrañamente desorientadora, y me encuentro a mí mismo disfrutando de poder categorizar eventos de este modo."

show ev watch_black:
    center
    alpha 0.0
    linear 1.0 alpha 1.0

n "La relevancia del andar de un reloj es sorprendentemente grata, y decido empezar a llevar un reloj analógico de pulsera, algo que no solía hacer antes."



n "\nCuando finalmente le pregunto a Rin sobre algo que me ha estado molestando durante toda la semana, ya es la hora del almuerzo."

$ renpy.music.set_volume(1.0, 2.0, channel="music")

nvl clear
nvl hide dissolve

scene bg watchhallway_blur
show ev watch_worn:
    xalign 0.5 yalign 0.5
with locationchange

window show

"La hora es entre las 11:06 y las 11:07, ya que mi reloj no tiene una manecilla para mostrar los segundos. Es del tipo tradicional con extensibles de piel negros y carcasa de titanio."

"No se ve llamativo, pero un reloj de pulsera no tiene que serlo."

show ev watch_worn:
    easeout 0.5 ypos 1.0 alpha 0.0
with None

show bg school_hallway3
show crowd behind ev
show rin basic_awayabsent at center behind ev
show ev watch_worn:
    easeout 0.5 ypos 1.0 alpha 0.0
with locationchange

hide ev
with None

play ambient sfx_crowd_indoors fadein 2.0

hi "Oye."

show rin basic_absent
with charachange

hi "¿Recuerdas ese dibujo que hiciste de mí? ¿Que dijiste que me veía malhumorado y lúgubre o algo así?"

hi "Quisiera saber a qué te referías con eso."

show rin negative_spaciness
with charachange

"Me da una mirada extraña e inclina la cabeza algunos grados a la izquierda, pero no dice nada por un rato."

rin "Bueno, verás…"

show rin basic_deadpanupset
with charachange

stop ambient fadeout 2.0
stop music fadeout 2.0

rin "Nos hemos conocido por dos semanas y no te he visto sonreír ni una sola vez."


"Su sorprendente observación me hace dar una pausa."

window hide
nvl clear
nvl show dissolve

n "\n\n\n¿Acaso he dejado de sonreír?"

n "\nTengo que tomar lo que dice como la verdad. Ella no tiene razón para mentir."

n "Algo sobre cómo lo dice me molesta. Le frunzo el ceño a Rin, luego trato de corregir mi expresión para parecer menos deprimido."

n "No he estado en el humor más alegre durante los últimos meses, más o menos, esto es cierto."


n "¿Se nota tanto que alguien como Rin puede darse cuenta de ello, después de tan poco tiempo de conocernos?"

n "¿Debería de sonreírle más a Rin? Quizás ella pueda apreciarlo, ya que ella misma tiene un rostro tan neutral casi todo el tiempo."

n "\n¿En verdad he dejado de sonreír?"

nvl hide dissolve
nvl clear
window show

play ambient sfx_crowd_indoors fadein 2.0

hi "Ya veo."

hi "¿Debería de sonreír más?"

show rin relaxed_nonchalant
with charachange


rin "No me molesta de cualquier manera. Sé cómo eres; no puedes evitar ser Hisao, de todos modos."

hi "Pero, ¿te molesta?"

show rin basic_absent
with charachange

rin "Tan solo lo noté, eso es todo."

show emi excited_smile:
    tworight
    xpos -0.5
with None

show rin basic_absent at tworight
show crowd at bgright
show bg school_hallway3 at bgright
show emi excited_smile at twoleft
with charamove

play music music_emi fadein 0.2


"Emi salta por el pasillo, da un brinco para detenerse en seco cuando nos alcanza, y le da una leve palmada en el hombro a Rin."

show emi basic_happy
with charachange

emi "¿Lista para el almuerzo?"

show rin basic_deadpanupset
with charachange


rin "Depende de lo que sea el almuerzo de hoy. ¿Recuerdas ese estofado en marzo? Nunca más, eso."

show emi basic_closedgrin
with charachange

emi "Vamos de todos modos. ¡Muero de hambre!"

hide emi
hide rin
with charaexit

"Cuando están a punto de partir, Emi se da la vuelta hacia mí; aparentemente como si fuese una idea de último momento, y me sonríe de una forma encantadora."

show emi sad_grin at center
with charaenter

emi "Por cierto, Hisao…"


"El tono de su voz es demasiado dulce y suave como para ser sincero. Puedo sentir la trampa a punto de cerrarse en mí a causa de esta endiablada fanática de la salud en miniatura."

"Sé qué es lo que ella está a punto de decir incluso antes de que continúe, porque he estado tratando de evitarla toda la semana."

show emi excited_proud
with charachange

emi "Todavía no te he visto en la pista toda esta semana."

hi "Tal vez he estado ahí cuando tú no estás."

show emi sad_annoyed
with charachange

emi "Eso es imposible. Estoy ahí todo el tiempo."

hi "Pero duermes y vas a clases."

show emi basic_annoyed
with charachange

emi "Hago esas cosas a la misma hora que tú."

hi "Sí, lo sé, lo sé. Es solo que… no he podido animarme."

hi "No me delates con el enfermero, ¿de acuerdo?"

hi "Correr simplemente no es lo mío, y no se me ha ocurrido una buena alternativa."

show emi excited_happy
with charachange

emi "¿Por qué no vienes a la competencia de atletismo este fin de semana? Tal vez llegues a inspirarte."

hi "¿Competencia de atletismo?"

show emi basic_happy
with charachange

emi "¡Sí! Gente de algunas otras escuelas viene para acá para un poco de acción atlética amistosa. Es el domingo por la tarde."

"No puedo pensar en una razón para no ir."

hi "Seguro. Vendré a animarte. ¿Supongo que correrás?"

show emi excited_proud
with charachange

emi "¡Por supuesto! ¡Tendrás la oportunidad de verme vencerlos a todos!"

show emi basic_grin
with charachange

emi "¡Pero nos vemos luego! Si no tengo algo para comer, moriré."

hi "Nos vemos luego."

hide emi
with charaexit

stop music fadeout 3.0

hi "Hasta luego, Rin. Prometo que sonreiré la próxima vez."

"Llamo su nombre, casi como una idea de último momento. Después me siento avergonzado por ello, y me pregunto por qué siquiera dije algo."

stop ambient fadeout 1.0

scene ev hisao_mirror_800
with shorttimeskip

"Esa noche, cuando confirmo doblemente que Kenji no vendrá a irrumpir en el baño, miro en el espejo y le sonrío a mi reflexión."

"El yo en el espejo que me sonríe en el baño se ve terriblemente falso."

scene black
with dissolve




label es_R6:

play music music_happiness fadein 2.0

scene bg school_library
with locationchange

"Después de haber acabado los libros que Kenji me prestó en tan solo unas cuantas noches, voy de vuelta a la biblioteca, considerándola una alternativa más segura para obtener mi dosis de lectura."

"Regreso los libros que él había robado mientras estoy en eso, para el deleite de Yuuko. Sin embargo, no le digo de dónde los saqué."

show yuuko happy_down at center
with charaenter

yu "Guau, tú sí que lees mucho, ¿no?"


hi "Bueno, supongo que sí."

hi "Quiero decir, sí. Incluso yo pienso que es raro. Creo que podría tener un problema de lectura. Quizás sea un adicto."

show yuuko panic_up
with charachange

yu "No no, no lo quise decir de esa manera. No es raro en lo más mínimo, y ser adicto a la lectura es mucho mejor que ser adicto a… a otra cosa."

hi "Sí, lo sé. Era una broma."


"Le sonrío de un modo tranquilizador y dejo los libros sobre el mostrador para que Yuuko los registre. Me siento cansado, así que me acomodo en la silla desocupada frente a su escritorio."

show yuuko neutral_up
with charachange

"Mientras Yuuko revisa la modesta pila de material de lectura que encontré, dejo que mi vista se pasee por la biblioteca."

hide yuuko
with charaexit

"En las mesas, un par de chicas están charlando en voz baja en lugar de trabajar en sus tareas."

"La chica de cabello corto se da cuenta de que estoy viendo en su dirección y me saluda con la mano. Cuando levanto la mía, se miran la una a la otra y ríen al unísono."

"No estoy seguro de cómo debería de sentirme al respecto, así que decido que es algo bueno. La que me saludó tiene un horrible caso de epilepsia."

"La vi teniendo un ataque hace unos días. Fue una de las cosas más perturbadoras y aterradoras que he visto en mucho tiempo."

"Sin embargo, ahí está ella, platicando sobre lo que sea, como si no tuviera una sola preocupación en el mundo."

hi "Sabes, esta escuela en verdad es algo más."

show yuuko panic_up
with charaenter

"Yuuko levanta la mirada de los libros que estaba revisando, un poco sorprendida. Se acomoda los anteojos y pone una confundida y nerviosa sonrisa."

show yuuko smile_down
with charachange

yu "¿A qué te refieres?"

hi "Realmente no sé cómo explicarlo. Es solo que todos son tan… activos, o… ¿cómo debería decirlo?"

hi "No es solo lo del festival, creo, aun si no he estado aquí tanto tiempo, pero es todo."

hi "La gente habla más, trabaja más duro y simplemente… son… más que en cualquier otra escuela que haya visto antes."



"Estoy batallando para encontrar palabras, pero se siente como si estuviera hablando con honestidad."

label es_choiceR6:
menu:
    with menueffect
    hi "Esta escuela se siente tan viva."
    "Es refrescante.":


        return m1
    "Me hace sentir como si estuviera atorado.":

        return m2

label es_R6a:

hi "Claro, también había gente así en mi antigua escuela, pero no tanta. Y se siente más intenso, de algún modo."

hi "Creo que, si tuviera que especificar en una sola cosa, los estudiantes aquí realmente aprecian ir a la escuela."

label es_R6b:

hi "Siento que necesito comenzar a andar en alguna dirección, también. Así es como esta escuela me hace sentir."

label es_R6c:

show yuuko worried_up
with charachange

yu "No creo que eso sea algo malo."

hi "Sí, yo tampoco."

"De repente me doy cuenta de que, de la nada, le he estado parloteando mis pensamientos a Yuuko. Ella es una persona un poco nerviosa, así que temo poder haber causado una mala impresión."

"Ella me mira con lo que espero sea curiosidad en lugar de horror, así que concluyo que se encuentra bien."

hi "Disculpa por hablar de pronto sobre cosas raras como esta. No quise causarte problemas."

show yuuko smile_down
with charachange

yu "Oh no, no es problema. Me alegra escuchar si te sientes con ganas de hablar."

show yuuko neutral_down
with charachange

yu "Me hace sentir un poco fiable, también."



"Yuuko sonríe con dulzura, y de una forma un poco irónica con ello. Respondo con una agradecida sonrisa de mi cuenta."

"En lo que ella empuja la ordenada pila de libros por el mostrador, me pongo de pie y los recojo en mis brazos."

show yuuko closedhappy_up
with charachange

yu "Aquí están."

hi "Gracias."

show yuuko neutral_up
with charachange

yu "Supongo que nos veremos otra vez. Por favor, ven cuando gustes."

"La amabilidad de Yuuko es reconfortante."

hi "Puedes contar con ello. Nos vemos después."

stop music fadeout 2.0

scene black
with dissolve


label es_R7:

scene bg school_courtyard
show crowd
with locationchange
play ambient sfx_crowd_outdoors fadein 7.0

"La mañana de la competencia de atletismo me recibe con una resplandeciente luz de sol desde un cielo azul cristal."

"Mientras camino tranquilamente hacia la pista, decido que esto es una buena señal. De qué, no estoy seguro; este evento no es tan emocionante para mí como parece serlo para una gran parte del cuerpo estudiantil."

"Me interesa mucho menos ver deportes que participar en ellos, pero animar a Emi es una buena causa."

"No espero que esta sea algún tipo de experiencia asombrosa y espectacular, pero no puede hacer daño. Probablemente estaría pasando el tiempo leyendo encerrado en mi habitación, de otro modo."

scene bg school_track
show crowd
show rin basic_absent at center
with locationchange

"Cuando me acerco a las gradas, veo a Rin emerger de la muchedumbre justo antes de que ella me vea."

show rin basic_deadpannormal
with charachange

rin "Viniste."

hi "Por supuesto, dije que lo haría, ¿no es cierto?"

show rin basic_deadpanamused
with charachange

rin "Eso no necesariamente implica que cumplirías tu palabra."

show rin basic_awayabsent
with charachange

rin "Muchas personas dicen cosas y no lo toman en serio."

hi "Bueno, yo no."

play music music_soothing fadein 0.5

show rin negative_spaciness
with charachange

"Rin se encoge de hombros. Al parecer aburrida por nuestra conversación, se da vuelta y se dirige de nuevo hacia las gradas."

hi "Así que, ¿estás emocionada por esto?"

show rin basic_deadpan
with charachange

rin "No realmente."

hi "Yo tampoco."

show rin basic_absent
with charachange

rin "Entonces, ¿por qué viniste?"

hi "¿Por qué viniste tú?"

"Ella no responde, así que decido tampoco responder."


"Subimos a las gradas, y Rin señala hacia arriba con la cabeza."

show rin negative_spaciness at center
with charaenter

rin "Allá arriba."

show rin basic_deadpancontemplation
with charachange

"Rin dirige el camino y pronto nos sentamos en una banca casi vacía."

$ renpy.music.set_volume(0.3, 3.0, channel="ambient")

show rin basic_deadpancontemplation at tworight
show bg school_track at bgright
show crowd:
    linear 1.0 alpha 0.0
with charamove

hide crowd
show meiko smile at twoleft
with charaenter

"Hay una señora sentada junto a Rin —la madre de alguien, supongo."

"Lleva el cabello bastante largo recogido en una trenza. Al ver a Rin, ella le da una sonrisa extrañamente familiar."

show meiko happy
with charachange


emm_ "Vaya, esta es una sorpresa."

show meiko wink
with charachange

emm_ "Pensé que ibas por un bocadillo, no por un chico."

hi "¿Eh?"

show rin basic_surprised
with charachange

rin "¿Este no está bien?"

show meiko happy
show rin basic_awayabsent
with charachange

"La mujer se ríe de Rin y sacude la cabeza, aparentemente incapaz de encontrar una réplica para ello. Conozco ese sentimiento."

show meiko smile
with charachange

emm_ "Bueno, supongo que siempre has sido alguien que sale por algo y trae otra cosa."

emm_ "¡Pero qué descortés soy! No me he presentado."

emm_ "Soy Meiko Ibarazaki. Estoy segura de que si conoces a esta chica, por lo menos te has encontrado con mi hija, también."

show meiko happy
with charachange

emm "Encantada de conocerte."

"Bueno, eso lo explica todo. Ella es como una Emi más alta, mayor y maternal."

"Aparte de que su cabello es más oscuro que el de su hija, realmente no hay duda del parecido."

show rin basic_absent
show meiko smile
with charachange

hi "Disculpe, soy Hisao. Hisao Nakai. Gusto en conocerla."

show rin basic_lucid
with charachange

rin "Soy Rin Tezuka."

show meiko happy
show rin basic_awayabsent
with charachange

"La señora Ibarazaki ríe una vez más —ella en verdad se parece a su hija— y entonces se reclina un poco en su asiento y alza una ceja."

$ renpy.music.set_volume(0.0, 0.5, channel="ambient")

show meiko serious
with charachange

stop music fadeout 1.0

emm "Así que, ya que todos nos conocemos, ¿cuánto tiempo hace que tú y Rin han estado saliendo?"

"Mi respuesta consiste en silencio en lo que mi cerebro repentinamente se pone en marcha. Pero justo antes de que pueda balbucear una apresurada explicación, la madre de Emi rompe en carcajadas de nuevo."

play music music_soothing fadein 0.5
$ renpy.music.set_volume(0.3, 0.5, channel="ambient")

show meiko happy
with charachange


emm "¡Ja! Eres de los que se sonrojan, ¿no es así?"

"No sé si hay alguna manera de conservar mi dignidad en esta situación, así que me conformo con responder entre dientes."

show meiko smile
show rin basic_absent
with charachange

hi "No estamos—"

show meiko happy
show rin basic_awayabsent
with charachange

emm "Lo sé, pero es divertido verte retorcer."

show meiko wink
with charachange

emm "Lo siento. Perdona las diversiones de una mujer mayor."


"Ella ríe otra vez para sí misma."

"¿Mujer mayor?"

"Ella para nada se ve tan vieja, a mi parecer."

show rin basic_absent
with charachange

hi "Supongo que lo puedo dejar pasar."

show meiko happy
show rin basic_awayabsent
with charachange

emm "Qué amable de tu parte."

stop music fadeout 6.0

show rin basic_deadpan
with charachange

rin "Está empezando."

stop ambient fadeout 2.0

scene ev emitrack_blocks at Fullpan(12.0, dir="left", time_warp=_ease_in_time_warp)
with locationskip

"Dirijo mi atención a la pista, donde se preparan para el primer sprint."


"Parece ser la carrera de los 400 metros."

"Mis ojos examinan a las corredoras antes de encontrar a Emi."

scene ev emitrack_blocks_close
with flash

"Está sonriendo, con una mirada casi arrogante en su rostro."

show insert startpistol at right
with easeinright

"El juez de salida levanta su pistola."

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")

play sound sfx_startpistol
play ambient sfx_emisprinting

scene ev emitrack_running at Fullpan(1.0, dir="left", time_warp=_ease_in_time_warp)
with silentflash

"Emi sale disparada de los tacos de salida, desapareciendo de la línea de inicio en un instante."

"Es sorprendente. Incluso cuando las demás velocistas convergen en los carriles más cercanos a la línea interna, Emi acelera hacia el frente del grupo."

"Para el momento en que llega a la curva final, algunas de las otras corredoras la han alcanzado."

"Pero ella arranca con velocidad una última vez y las deja por lo menos medio segundo atrás."

scene ev emitrack_finish
with locationchange

stop ambient fadeout 1.0
play sound sfx_crowd_cheer

"La señora Ibarazaki exclama y grita de alegría, aplaudiendo frenéticamente, y básicamente viéndose como cualquier otro padre animando a su hijo."


"Emi rebota de la pista, viéndose satisfecha consigo misma."

play music music_daily fadein 2.0

scene bg school_track at bgright
show meiko happy at twoleft
show rin basic_deadpandelight at tworight
with locationchange

"Animo junto con todos los demás."

"La anunciadora (quien suena sospechosamente similar a Misha) alegremente da los resultados."

show meiko smile
show rin basic_awayabsent
with charachange

emm "Creo que se ha vuelto más rápida desde la última vez."

show rin basic_absent
with charachange

hi "Eso fue increíble."

show meiko happy
show rin basic_awayabsent
with charachange

"La señora Ibarazaki sonríe con orgullo."

emm "Emi es una corredora tremenda."

show meiko smile
with charachange

"Nos quedamos en silencio mientras el próximo evento se prepara para comenzar."

"Estoy sorprendido al ver a Emi caminando hacia la pista de nuevo."

show rin basic_absent
with charachange

hi "Esperen, ¿que no acaba de correr?"

"La madre de Emi asiente."

show rin basic_awayabsent
with charachange

emm "Sí, pero ella corre en diferentes eventos para el equipo. Especialmente los sprints."

show meiko happy
with charachange


emm "Es correr un montón, pero Emi puede arreglárselas."

"Por como se ven las cosas, está en lo correcto."

"Emi no parece estar cansada, como si no hubiera corrido en el evento anterior."

"De no ser por el sudor visible en su camiseta, nunca lo sabrías."

show rin basic_absent
with charachange

hi "¿Cuál evento es este?"

show meiko smile
show rin basic_awayabsent
with charachange

emm "Es la carrera de los 200 metros."

emm "Ella estará en esta, la de 100 metros y los relevos."

show rin basic_absent
with charachange

hi "Ya veo."

show rin negative_spaciness
with charachange

play sound sfx_startpistol
play ambient sfx_emisprinting

"Una vez más suena la pistola, y una vez más Emi despega de los tacos de salida."

"El sonido de un golpeteo saca mi atención de la carrera."

"Es el pie de Rin."

"Parece completamente absorta en la carrera."

show meiko happy
with charachange

stop ambient fadeout 1.0
play sound sfx_crowd_cheer

"La madre de Emi echa porras otra vez, y supongo que la carrera terminó."

"No me parece que los sprints tomen mucho tiempo para acabarse."

hi "Tu pie."

show rin relaxed_surprised
show meiko smile
with charachange

rin "¿Hmm?"

hi "Tu pie estaba golpeando las gradas."

show rin basic_deadpan
with charachange

rin "Oh."

hi "Parece que esto te gusta mucho. Estoy sorprendido; pensé que dijiste que esto no sería emocionante."

show rin relaxed_nonchalant
with charachange

rin "Hmm, supongo que tienes razón."

rin "No es tan interesante."

show rin basic_deadpannormal
with charachange

rin "Pero estoy viendo a Emi, no al deporte."

hi "No entiendo."

show rin basic_lucid
with charachange

rin "Emi es su más Emi cuando corre."

rin "No puedes ver a Emi en su más Emi muy seguido."

show rin basic_deadpanamused
with charachange

rin "Pero aquí, puedes. ¿Ves?"

"Dirige mi atención hacia la pista una vez más, donde la carrera de los 100 metros está a punto de comenzar."

stop music fadeout 6.0
stop sound fadeout 2.0

scene ev emitrack_blocks_close
with locationskip

"Miro a Emi de cerca."

"A medida que se sube a los tacos de salida, todo su cuerpo parece relajarse, pero es un relajamiento falso."

"Puedo ver que en realidad ella es como un resorte."

scene ev emitrack_blocks_close_grin
with locationchange

"Cuando el juez de salida le dice a todos que se alisten, mueve su cabeza hacia arriba de golpe y sus ojos se entrecierran un poco."

"Su boca se curva hacia arriba en lo que podría ser una sonrisa y podría ser un gruñido."

play sound sfx_startpistol
play ambient sfx_emisprinting

scene ev emi_run_face_zoomin
with locationskip

"Cuando la pistola se dispara, es como si hubiese sido liberada de una jaula, como si siempre estuviese moviéndose con esta rapidez deslumbrante, pero no pudiéramos verlo hasta que la pistola de salida disipase la ilusión de inmovilidad."

stop ambient fadeout 1.0
play sound sfx_crowd_cheer

"Tan pronto cruzó la línea de meta, la mirada feroz fue reemplazada por su sonrisa normal."

"El general vencedor regresando a su granja."

hi "Asombroso."

hi "Ella es realmente asombrosa. Nunca he visto a nadie moverse así de rápido."

scene bg school_track at bgright
show meiko smile at twoleft
show rin basic_deadpanamused at tworight
with locationchange

emm "Bueno, no me mires a mí, soy demasiado relajada como para correr así de rápido."

stop sound fadeout 9.0

show meiko worry
show rin basic_awayabsent
with charachange

emm "No, creo que el coraje de Emi viene todo del lado de su padre."

"A la mención del padre de Emi, la señora Ibarazaki se ve melancólica, casi triste."


emm "Él hizo que se interesara en el atletismo, ¿sabes?"

show rin basic_absent
with charachange

hi "Ah, ¿en serio? No lo sabía."

"Lo dejo en eso y no digo nada por un corto momento. Tengo la sensación de que esto es algo personal de lo que no debería preguntar."

play sound sfx_cellphone

"Un timbrado súbitamente emana del bolsillo de la señora Ibarazaki. Alcanzándolo, ella saca un teléfono celular y lo mira."

show meiko serious
show rin basic_awayabsent
with charachange


emm "… ¿En serio, mensajes de texto?"

emm "¿Pues cuántos años tiene? ¿dieciséis?"

hi "¿Hmm?"

show meiko smile
with charachange

emm "Oh, nada."

show meiko wink
with charachange

emm "Tengo que ir a encontrarme con un amigo mío."

show meiko happy
with charachange

emm "¿Le dirías a Emi que estoy muy orgullosa de ella y que la llamaré más tarde en la noche?"

show rin basic_absent
with charachange

hi "Por supuesto."

hide meiko
with charaexit

show rin basic_absent at center
show bg school_track at center
with charamove

show rin basic_awayabsent
with shorttimeskip

play music music_tranquil fadein 2.0

"Mientras espero que la carrera de relevos arranque, le echo una mirada a Rin. Parece desinteresada en sus alrededores, incluyéndome a mí."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\n\n\nEse comentario que hizo antes todavía lo tengo en mente."

n "“Emi es su más Emi cuando corre”."

n "Sí tiene sentido, ya que me pongo a pensarlo. Ya que la vi correr, puedo creer que Emi da su mayor esfuerzo en la pista."

n "Los deportes son más que un pasatiempo, o incluso una competencia, para ella. Son un aspecto definitorio de su vida."

n "¿Qué hay de Rin, entonces? ¿Acaso ella siente lo mismo por el arte? Considerando la persistencia que mostró antes del festival, podría creerlo con facilidad."


n "¿Vi a Rin en su “más Rin” cuando estaba pintando el mural?"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear
window show

"Los relevos están por empezar, pero no veo a Emi por ninguna parte."

hi "Pensé que Emi correría en los relevos."

show rin basic_deadpan
with charachange


rin "Ella es el ancla."

show rin basic_deadpannormal
with charachange

rin "Así que no correrá por un rato, todavía."

hi "Ah."

show rin basic_deadpandelight
with charachange

rin "¿Lo viste?"

hi "¿Eh?"

rin "Emi en su más Emi."

hi "Tal vez."

show rin basic_deadpanupset
with charachange

rin "Hmm. Quizás esta vez."

play sound sfx_startpistol


"La carrera comienza, y le echo porras a las compañeras de equipo de Emi cuando pasan la estafeta."

play ambient sfx_emisprinting

scene ev emitrack_running:
    truecenter zoom 1.0 subpixel True
    ease 20.0 zoom 1.05 xalign 0.0 yalign 0.0
with locationskip

"Finalmente, veo a Emi hacer el sprint en la pista para tomar el último pase."

"Una vez más estoy sorprendido por cuán grácil se ve cuando corre."

"Es realmente hermoso."

"La mirada de determinación y audacia en su rostro solo enriquece la imagen."

"Emi en su más Emi, supongo."

stop ambient fadeout 1.0
play sound sfx_crowd_cheer

show ev emitrack_finish
with locationskip


"Emi atraviesa volando la línea de meta con un gran salto, apenas por delante de las corredoras cercanas, pero aún en primero."

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

scene bg school_track
show rin negative_worried at center
with locationskip

show rin basic_absent
with charachange

rin "Bueno, bajemos."

rin "Tenemos que coronar a la vencedora."

show rin basic_deadpanamused
with charachange

rin "Ve si puedes encontrar una ramita de laurel."

hi "Eso no va a ser fácil."

show rin basic_deadpannormal
with charachange

"Rin se encoge de hombros."

show rin basic_deadpan
with charachange

rin "Al menos lo intentamos."

stop music fadeout 5.0
stop sound fadeout 5.0
play ambient sfx_crowd_outdoors fadein 2.0

scene bg school_track_on
show crowd
show rin basic_awayabsent at center
with locationskip

"Emi está rodeada por sus compañeras, todas ellas felicitándola por la carrera."

"Rin parece estar esperando a que Emi se percate de que ella ya ha llegado."

"No parece ser su estilo el llamar la atención hacia sí misma. O mostrar sus emociones más allá de encogerse de hombros."

"Al ser más impaciente que Rin, alzo la mano y llamo la atención de Emi. Ella ve hacia arriba y nos sonríe con alegría."

show bg school_track_on at bgright
show crowd at bgright
show rin basic_awayabsent at tworight
with charamove

play music music_emi fadein 1.0

show emi basic_closedhappy_gym at twoleft
with charaenter

emi "¡Qué tal, te apareciste!"

show rin basic_deadpanupset
with charachange

rin "Te hubiéramos traído una corona de laureles, pero Hisao no encontró ninguna."

show emi basic_grin_gym
with charachange

hi "Tú tampoco."

show rin basic_deadpan
with charachange

rin "No era mi trabajo buscar."

hi "¿Cuándo asignamos los trabajos?"

show rin basic_deadpannormal
with charachange

rin "Cuando dije “Ve si puedes encontrar una ramita de laurel”."

show rin basic_deadpandelight
with charachange

rin "Trata de seguir el ritmo."

"Me encojo de hombros. Creo que Rin me lo está contagiando."

hi "Parece que es mi culpa después de todo, Emi."

show emi basic_closedhappy_gym
show rin basic_awayabsent
with charachange

"Emi se ríe de Rin y de mí."

show emi basic_happy_gym
with charachange

emi "Está bien, estoy segura de que me lo compensarán de alguna manera."

show rin basic_absent
with charachange

hi "Ah, claro."

show rin basic_awayabsent
show emi excited_amused_gym
with charachange


emi "¡Bien! Así que, ¿cómo me vi?"

show rin basic_absent
with charachange

hi "Muy impresionante."

show emi basic_closedgrin_gym
with charachange

"Emi parece complacida con esta valoración."

"No menciono cuán todavía más impresionante es su desempeño dada su falta de piernas. Me imagino que ya lo sabe."

"Además, parece que le restaría mérito a su esfuerzo, de algún modo."

show emi basic_grin_gym
show rin basic_awayabsent
with charachange

emi "¡Estupendo saberlo! Me preocupaba haberme visto un poco lenta en los relevos, pero supongo que lo hice bien, ¿eh?"

show emi basic_closedgrin_gym
with charachange

"Emi ríe y entonces parece recordar algo."

show emi basic_happy_gym
with charachange

emi "Oh, antes de que lo olvide…"

emi "¡Rin y yo vamos a hacer algo el próximo domingo como festejo después de la competencia!"

show emi excited_proud_gym
with charachange

emi "¡Deberías venir!"

show emi sad_grin_gym
with charachange

emi "Normalmente lo hacemos un día después, pero ya que hoy es domingo, tengo tareas y clases y todas esas cosas de las que encargarme."

show rin basic_absent
with charachange

hi "Oh seguro, me encantaría."

show rin basic_awayabsent
show emi excited_laugh_gym
with charachange

emi "¡Genial! ¡Es una promesa, entonces!"

show rin basic_absent
with charachange

hi "Oh, cierto. Tu mamá quería decirte que está orgullosa de ti."

hi "Te llamará más tarde en la noche."

show emi basic_happy_gym
show rin basic_awayabsent
with charachange

emi "¡Pensé que la había visto en las gradas!"

show emi basic_closedhappy_gym
with charachange

emi "¡Me alegra que haya podido venir!"

"Compañero" "¡Oye, Emi! ¡Te vas a perder la ceremonia de premiación!"

show emi basic_shock_gym
with charachange

emi "¡Oh sí, gracias!"

show emi basic_grin_gym
with charadistant

"Ella se vuelve hacia Rin y hacia mí."

emi "No tienen que quedarse para esta parte. Dura una eternidad."

show emi excited_proud_gym
with charachange

emi "Además, deberías ponerte a hacer tu tarea ahora si no quieres estar despierto hasta tarde, Hisao."

play sound sfx_emipacing

hide emi
with easeoutleft

stop sound fadeout 2.0

show bg school_track_on at center
show crowd at center
show rin basic_awayabsent at center
with charamove

stop music fadeout 5.0

"Emi va saltando hacia sus compañeras, dejándonos solos a Rin y a mí."

"Ni uno de los dos tiene el mínimo interés en la ceremonia de entrega de medallas, así que nos retiramos silenciosamente y regresamos al campus."

$ renpy.music.set_volume(0.3, 2.0, channel="ambient")

scene bg school_courtyard
show crowd
show rin relaxed_nonchalant at center
with locationskip

"Rin bosteza sin siquiera tratar de contenerse y arrastra sus pies sin descanso."


"Me siento incómodo, pero en menor medida que si estuviera con alguien más. Aun así, me quedo pensando sin saber qué es lo que debería decir."

hi "Emi estuvo genial, ¿no es así?"

show rin basic_deadpannormal
with charachange

rin "Estuvo genial. Le tengo mucha envidia."

hi "¿Por qué?"

show rin basic_awayabsent
with charachange

rin "Como dije, ¿no crees que es grandioso poder ser realmente tú mismo?"

"Eso suena extraño, viniendo de Rin."

hi "No creo que tú, de entre todas las personas, deberías de tener problemas con encontrar una manera de cómo expresarte."

hi "¿Acaso no tienes tus pinturas?"

show rin basic_absent
with charachange

stop ambient fadeout 1.0

"Ella voltea a verme. Por primera vez veo en sus ojos esta extraña y vacía expresión que creo debe ser única de ella."

rin "No, verás, el problema es que realmente no estoy segura de quién soy."

stop ambient fadeout 1.0
scene black
with dissolve


label es_R8:


$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
scene bg school_classroomart at right
with locationchange

"La reunión de hoy del club de arte se encuentra en espera actualmente, mientras todos esperan a que aparezca Nomiya. Me tomo este tiempo para tratar de explicar mi teoría sobre Yamaku a Rin."

"He tratado de comprender exactamente qué es lo que, para mí, se siente tan especial en esta escuela; ese concepto que, sin éxito, intenté explicarle a Yuuko el otro día."

"Todavía es difícil, pero la competencia de atletismo y el tiempo que he pasado observando a mis compañeros de clase, han ayudado a que mis ideas maduren un poco."

show rin basic_absent_close at center
with charaenter

hi "¿Te has dado cuenta de que la gente habla todo el tiempo?"

hi "En realidad no puedo explicarlo, pero…"

"Una vez más, mientras trato de explicar mis observaciones, lucho para encontrar las palabras."

"El cuerpo estudiantil se encuentra fuertemente separado en grupos, y tan solo ahora comienzo a encontrarles sentido al intrincado agrupamiento y redes de popularidad."
"Y aun así, la sensación de ser parte de un grupo es más fuerte aquí que la que recuerdo en mi antigua escuela."

hi "Estoy tratando de decir que esta escuela no es como las otras escuelas. O al menos los estudiantes no lo son, incluso después de descartar lo obvio."

hi "… ¿Sabes de lo que estoy hablando?"

show rin basic_deadpan_close
with charachange

rin "No sé de qué estás hablando."

hi "Oh, bueno… pues, como sea."


"Quiero seguir con la discusión, pero para entonces Nomiya entra al salón."

hide rin
with charaexit

show bg school_classroomart at left
with charamove

show nomiya smile at center
with charaenter

play music music_happiness fadein 2.0

"El maestro se limpia el sudor de la frente con un pañuelo y respira con bastante dificultad. Rápidamente le echa una mirada al salón y se serena un poco."

show nomiya veryhappy
with charachange

no "Hola, hola; disculpas por llegar tarde."

show nomiya talk
with charachange

no "¿Están todos presentes? ¡Bien!"

no "Debo confesar, realmente no he planeado nada para hoy porque he estado extremadamente ocupado, últimamente. Pero estoy seguro de que se nos puede ocurrir algo entretenido."

show nomiya frown
with charachange


no "¿Alguien tiene alguna sugerencia? Estaba pensando que podríamos tener un círculo de discusión, ya que no hemos tenido uno desde hace tiempo. Por lo menos yo encontré el último magníficamente agradable."

"Hay algunos murmullos por aquí y por allá, pero nadie levanta la voz a favor o en contra de Nomiya."

show nomiya talk
with charachange

no "Podríamos profundizar en varios movimientos artísticos. ¿O tiene alguien un tema interesante en mente?"


no "Vamos, pónganlo al frente. No importa si es tonto o extraño, ¡siempre podemos hacerlo algo interesante!"

"Nadie parece ser lo suficientemente valeroso como para hacer tal sugerencia."

"Ya que el silencio se rehúsa a romperse, alzo mi mano al aire."

show nomiya smile
with charachange

no "¿Ajá? Nuestro amigo más reciente parece tener algo en mente. ¡Habla, hijo, habla!"

hi "Ah, bueno… No sé los demás, pero siempre me he preguntado por qué existe el arte, en primer lugar."

stop music fadeout 2.0


"Mi voz se apaga. El silencio se asienta en el salón y nadie le hace seguimiento a mi tímida sugerencia."

"Entonces, el maestro revienta a carcajadas."

show nomiya veryhappy
with charachange

no "¡Jojojo, excelente!"


no "Muy bueno, en verdad muy bueno. Empezando y te vas a lo grande, ¿eh?"

no "¡Fabuloso!"


"Riendo, mueve unos papeles de lugar en su escritorio por unos momentos. Cuando termina, parece haber tomado algún tipo de decisión."

show nomiya smile
with charachange

no "Muy bien. Vayamos con eso y veamos adónde nos lleva, ¿de acuerdo?"

show nomiya talktongue
with charachange


no "Oh Dios, incluso un vejestorio como yo se emociona cuando tan delicioso entusiasmo está presente. Oh por dios."

show nomiya smile
with charachange

no "Déjenme organizar mis ideas por un momento, para que pueda pensar en un buen punto de inicio para todos."

"Por alguna razón el maestro parece estar, casi literalmente, brillando de la emoción. Garabatea algunas cosas en una hoja de papel suelta, y entonces limpia sus anteojos con el pañuelo."

show nomiya dreamy
with charachange



"Hace una pose, entonces se detiene para una pausa artística excesivamente dramática que dura lo que se siente como medio minuto."

"Todo está tan callado que podría escuchar caer un alfiler."

show nomiya talk
with charachange

play music music_another fadein 0.5

no "Primero, pensemos en algunas preguntas que queremos contestadas, como “¿Qué es el arte?” y “¿Por qué existe el arte?”."

show nomiya smile
with charachange

no "¿Alguien tiene alguna pregunta que pueda estar relacionada?"

"El chico de gafas abre la boca casi de inmediato. Su voz es suave y baja, y tengo dificultad para entender lo que dice."

"Chico de gafas" "¿Qué define a un artista?"

"Después de él, surge otra pregunta."

"Estudiante" "Si lleno una caja de cartón con agua y lo llamo arte, ¿es arte?"

show nomiya veryhappy
with charachange

"Todos se ríen de eso, incluso el maestro."

no "¡Genial! ¡Todo esto es maravilloso!"

show nomiya talk
with charachange

no "Permítanme empezar por decir que esto no es un caso claro en absoluto, y como tal, no les daré ninguna respuesta. Solo voy a hablar de mi propia perspectiva."

no "Los eruditos han discutido sobre este tipo de preguntas desde tiempos inmemorables, y nunca se ha llegado realmente a un consenso aplicable ampliamente."

show nomiya smile
with charachange

no "Hay, sin embargo, algunas cualidades en las que la mayoría tiende a estar de acuerdo. Con suerte, todos ustedes también las deberían encontrar aceptables."

show nomiya dreamy
with charachange

no "En pocas palabras, el arte se define a sí mismo. Este simplemente no puede ser contenido en una definición externa, ya que los límites del arte se expanden y se contraen por fuerzas internas."

show nomiya serious
with charachange

no "Todos los días, alguien en algún lugar sale con algo completamente escandaloso que desafía todas y cada una de las preconcepciones."

show nomiya frown
with charachange

no "La idea central de esto es que, en lugar del lado racional de la mente, el arte atrae a la intuición, al instinto, a lo primitivo. Encontrarían muy difícil de explicar el porqué, exactamente, es que gustan de un estilo o pieza en particular, ¿no?"

"No espera una respuesta antes de continuar."

show nomiya veryhappy
with charachange

no "Este es exactamente el porqué."

show nomiya frown
with charachange

no "Entonces, el arte es este tipo de cosa salvaje e incontrolable que merodea en algún profundo lugar de nuestro subconsciente. Ahora, ¿por qué existe?"

"Nomiya aparentemente espera que alguien salga con una suposición, pero nadie se atreve a interrumpir su inspirado discurso. Él continúa."

show nomiya dreamy
with charachange

no "¡Era una pregunta capciosa! Verán, el arte también se valida a sí mismo."

show nomiya talk
with charachange

no "En general, uno podría decir que el arte no existe para ningún otro fin que sí mismo. Es algo que existe únicamente para dejar una marca en la historia."

show nomiya serious
with charachange

no "Es la oposición de un mortal en contra del rostro de la oscuridad, como se dijo una vez antes. El arte es verdaderamente la prueba de nuestra existencia."
no "Todos ustedes deberían saber que la cultura humana y la civilización están estrechamente ligadas a la existencia del arte."

show nomiya frown
with charachange


no "Entonces, ¿qué hay de los artistas? ¿Qué impulsa a un hombre a dedicar su vida a algo tan voluble y misterioso que incluso desafía la definición?"

show nomiya serious
with charachange

no "Hay tantas respuestas para esto como hay artistas, pero si tuviera que ponerlo en palabras… un artista no hace arte porque puede, sino porque debe."

"Nomiya hace una pausa, y su mirada pasa por sobre la audiencia, sus ojos ardiendo con pasión."

show nomiya frown
with charachange

no "Es obvio que el arte toca la misma alma de todos y cada ser humano en algún u otro modo. Así que, si se les diera la oportunidad de conectarse con sus semejantes en un modo tan fundamental, ¿cómo podrían no hacerlo?"

show nomiya talk
with charachange

no "Hay un poema al que le tengo mucho cariño, y ahora les recitaré la parte más conocida. Siento que, personalmente para mí, de todas las cosas posibles, captura mejor la esencia de lo que significa ser artista."

stop music fadeout 2.5

"Nomiya se recarga sobre el escritorio mientras aclara la garganta, preparándose."

"Mirando a algún lugar lejano, pronuncia las palabras en el pesado aire de la tarde con su suave voz de bajo."

show nomiya dreamy
with charachange

play music music_one fadein 0.5

no "Ver a un Mundo en un Grano de Arena"

extend "\nY a un Cielo en una Flor Silvestre,"

no "Sujetar el Infinito en la palma de tu mano"

extend "\nY la Eternidad en una hora."






"Hay un solemne e increíblemente incómodo silencio después de que termina de recitar el corto fragmento. Nadie se atreve a decir una palabra."

"Nomiya aclara su garganta de nuevo."

show nomiya talk
with charachange

no "El ser artista es ver el mundo en un grano de arena."

show nomiya dreamy
with charachange

no "Verán, hijos míos, sin el arte, no habría mucho por el cual vivir en este mundo. Es algo sumamente profundo."

"Claramente está conmovido por esta idea. Casi espero ver una lágrima solitaria caer por su áspera mejilla, pero nunca sucede."

show rin invis at offscreenright
with None

show nomiya invis at twoleft
show bg school_classroomart at bgleft
show rin basic_awayabsent_close:
    xpos 0.9 xanchor 0.5
with dissolvecharamove

hide nomiya
with None

"Me volteo hacia Rin y le susurro."

hi "¿Y cómo es esto un círculo de discusión?"

"Se encoge de hombros desinteresadamente a modo de respuesta."

show rin basic_deadpan_close
with charachange

rin "Los anteriores fueron lo mismo."

"Hay que reconocer que Nomiya sí trata de poner un poco de debate en marcha, pero el club parece reacio en obedecer."

"Me siento un poco culpable por abrir mi boca. Tal vez nos hubiéramos librado de esto."

stop music fadeout 1.5

show rin basic_awayabsent_close
with shorttimeskip

play music music_normal fadein 2.0

"A medida que la reunión llega a su fin, me doy cuenta de que no he tocado nada de pinturas o plumas este día, y me siento un poco decepcionado."

show nomiya smile at twoleft
with charaenter


"Nomiya emerge repentinamente a nuestro lado. Parece todavía estar encendido por el discurso que dio."

"Su colonia huele a almizcle y a sacarina a la vez, dándome un dolor de cabeza al instante, aun si no soy sensible a los perfumes. Está viendo a Rin como un lobo hambriento."

show nomiya talk
with charachange

no "Tezuka, ¿recuerdas a la señora Saionji, quien nos visitó en el festival?"

show rin basic_deadpannormal_close
with charachange

rin "Eso creo."

show nomiya veryhappy
with charachange

no "Voy a decirte algo impresionante."

show nomiya smile
with charachange

no "El asunto es, ella es una galerista muy conocida por aquí. Resulta ser que podría lograr que ella considere tener algo de tu trabajo en exhibición."

"Él termina la oración con un gesto dramático. Parece ser que está esperando que Rin muestre algún tipo de reacción de alegría y sorpresa a tales noticias tan grandes, pero ella tan solo lo mira inexpresivamente."

show nomiya veryhappy
with charachange



no "Magnífico, ¿no es así? Esta podría ser una verdadera oportunidad para que podamos avanzar, mi niña."

show rin basic_surprised_close
with charachange

rin "Pero…"

show nomiya frown
with charachange

no "Ya ya, sé lo que vas a decir. Sí, no sería un asunto tan simple, pero creo que esta es una oportunidad absolutamente fantástica."



no "¡Francamente, no me sorprendería en absoluto si incluso lográramos hacerlo en grande! ¡Este podría ser el primer paso! Y luego, cuando haya corrido la voz, ¡les damos con todo lo que tenemos! ¿Verdad, Nakai?"

hi "Eh, sí, suena bastante genial. Si le gustan ese tipo de cosas."

show nomiya veryhappy
with charachange

no "¿Ves? Definitivamente no deberíamos dejar esta pasar, ¿no es cierto?"

show rin negative_confused_close
with charachange

rin "Realmente yo… no."

stop music fadeout 7.0

"Rin parece estar preocupada por alguna razón. No puedo entender por qué. Lo que está diciendo Nomiya en verdad suena como algo posiblemente grandioso."

"Sin embargo ella se ve muy triste y confundida. Nunca la había visto así."

show nomiya talk
with charachange

no "Así que, ¿qué opinas?"

"Rin mira hacia el rostro brillante del maestro, luego de vuelta hacia abajo, a su escritorio."

show rin negative_worried_close
with charachange

rin "Pensaré al respecto."


"Nomiya finalmente es tomado por sorpresa por la falta del superlativo placer de Rin. Entonces él le sonríe ampliamente y con gentileza le da unas palmaditas en la cabeza."

show nomiya smile
with charachange

no "Buena chica."

hide rin
hide nomiya
with charaexit

"La reunión del club finalmente se acaba, y mientras recojo mis cosas perezosamente y ayudo en la limpieza, comienzo a sentirme exhausto por alguna razón. No hay mucho que hacer, sin embargo, así que termina rápido."





label es_R9:

scene bg school_staircase2
show rin negative_spaciness_close at tworight
with locationskip

"Alcanzo a Rin, quien dejó el salón hace solo un momento, así que estamos bajando por las escaleras hasta la planta baja, mientras trato de repasar el apasionado discurso de Nomiya sobre el arte, y Rin parece estar perdida en sus pensamientos."

"No es un estado inusual para ella, eso lo he aprendido, pero algo sobre su expresión me hace sentir intranquilo."


hi "Lo que pagaría por saber en qué piensas."

show rin basic_deadpancontemplation_close
with charachange

rin "Te costaría un ojo de la cara."

hi "Tan solo estás sobrevaluando tus pensamientos."

show rin basic_lucid_close
with charachange

rin "No podría venderlos, de todas formas. Todavía no estoy segura de en qué estoy pensando. Eso sería fraude, también; como robarle un dulce a un bebé."

hi "Eso es hurto, no fraude."

show rin basic_deadpanupset_close
with charachange

rin "Tengo que pensar en lo que pienso."

hi "¿Es esto sobre lo que dijo el maestro? ¿Poner tu trabajo en exhibición y todo eso?"

scene bg school_lobby
with locationchange

"Ella no responde, pero se detiene en seco cuando llegamos al vestíbulo."

"Somos las únicas personas alrededor, así que está muy silencioso. Unas pisadas hacen eco desde algunos pisos arriba mientras alguien se apresura yendo por las escaleras."

show rin negative_annoyed at center
with charaenter

rin "Creo que voy a ir a algún otro lugar."

"Creo que se encuentra realmente afligida."

hi "¿Quieres compañía?"

hi "No puedo prometer mucha ayuda para pensar, pero no es como si tuviera mucho más que hacer, y se supone que tengo que hacer un poco de ejercicio ligero."

show rin basic_absent
with charachange

rin "Si gustas."

play ambient sfx_parkambience fadein 20.0

scene bg school_backexit
with locationskip


"Rin me lleva hacia afuera, al muro detrás de los dormitorios. Hay un pequeño portón ahí, hecho del mismo hierro forjado que el portón principal. Lleva al lóbrego parque enarbolado detrás de la escuela."

"El portón está oxidado, como si no fuese usado a menudo. Sin embargo, se encuentra abierto, así que pasamos por este. No les está prohibido a los estudiantes dejar el campus, pero de algún modo me siento un poco nervioso."

scene bg school_forest1
with locationchange

"Un camino conduce hacia más adentro del bosque. Altos arces y zelkovas susurran en el aire y sus follajes crean parches de aire frío que permanecen en los lugares donde caen las sombras."

"El bosque huele fuertemente a tierra. Casi siento frío, aun si el día de pleno verano es tan caliente como siempre."

"Rin camina arduamente hacia el frente como una sonámbula, con paso seguro pero sin un destino aparente en mente. Sus pensamientos parecen estar en otra parte. Sigo algunos pasos detrás, tomando más cuidado de ver dónde pisan mis pies."


"El camino sigue el terreno cuesta arriba en un ángulo bajo, de vez en cuando desviándose ligeramente cuesta abajo antes de subir de nuevo."
"Los enmudecidos troncos marrones y grises forman filas en ambos lados del camino, salpicado de helechos y otra maleza."

scene bg school_forest2
with locationchange

"Después de un rato comienzo a preocuparme. El camino sigue siendo amplio y claro, así que no hay posibilidad de perderse, pero no parece que tengamos algún destino en particular."

"No hay nada de malo con vagar sin rumbo un poco, pero no quiero ir tan lejos y terminar demasiado cansado para caminar de regreso."

scene bg school_forestclearing
with locationchange

"Comienzo a sentir que me falta un poco el aire y mis piernas se sienten pesadas. Quiero detenerme y tomar la oportunidad de recuperar mi aliento y descansar las piernas, pero Rin sigue andando."

hi "¿Adónde estamos yendo? ¿O estamos yendo adonde sea?"

show rin basic_deadpan at center
with charaenter

rin "Árbol de la Preocupación."

hi "Ya veo."

hi "Entonces, ¿exactamente, qué es el Árbol de la Preocupación?"

show rin negative_spaciness
with charachange

rin "Es solo un árbol. Como este."

"Ella se detiene delante de un arce particularmente grande que puede o no ser el Árbol de la Preocupación. Sus exuberantes hojas verdes se mecen ligeramente en la brisa que sopla a través del pequeño claro al que entramos."

hi "Me lo imaginé."

show rin basic_deadpanupset
with charachange

rin "Hay gente que cree que debes venir aquí para regodearte en la miseria, si eres miserable, es solo que por “gente” me refiero a mí, y el árbol en realidad no tiene algún nombre."

hi "Así que… si eres miserable, ¿hablas con un árbol sobre ello?"

show rin basic_deadpan
with charachange

rin "No. ¿Por qué? No puedes hablar con los árboles. ¿Qué crees que soy?, ¿una loca?"

hi "No… No lo dije con esa intención."

show rin basic_lucid
with charachange

rin "¿O tal vez tú hablas con los árboles? Lo siento, no quise decir que estabas loco. Aun si probablemente lo estés, si hablas con los árboles."

show rin negative_confused
with charachange

rin "No lo recomendaría, en cualquier caso. La gente pensará que eres una persona rara."

hi "No, yo… solo olvídalo."

"Ella parece un poco confundida, por lo cual no la culpo en absoluto. Ella inclina un poco la cabeza hacia un lado, mientras su expresión se funde de vuelta a la usual."

show rin basic_absent
with charachange

rin "Está bien. Soy buena para olvidar cosas."


hi "Entonces, ¿por qué estamos aquí? ¿Te sientes miserable?"

"No puedo leer la expresión que hace. Odio qué tan malo soy para interpretar el estado de ánimo de Rin."

show rin negative_worried
with charachange



"Ella no responde de inmediato, como si ella misma no estuviera segura de su propio estado. La mirada perdida cambia a una expresión de dificultad a medida que ella se mueve con inquietud."

show rin basic_deadpancontemplation
with charachange

"Finalmente, llegando a una conclusión, Rin se encoge de hombros. Ese gesto ha llegado a disgustarme seriamente. No significa nada."

show rin basic_deadpanupset
with charachange

rin "Tal vez. Es solo que me siento un poco como si me estuviera hundiendo bajo el agua. No sé qué debería hacer."

show rin negative_confused
with charachange


rin "No sé adónde debería de ir, eso es todo. Quizás no es algo tan grande, pero pensé que caminar podría ayudar. Algo así como, si voy a algún lugar sabría hacia dónde voy. No sé si en verdad lo hizo."

show rin negative_worried
with charachange

rin "Realmente habría tenido sentido si hubiese ayudado a decidir adónde ir."

hi "Así que, ¿no quieres tratar de tener una exhibición? O mejor dicho, ¿no sabes si quieres? ¿No puedes decidirte?"


"Rin no dice nada por un rato, ordenando sus pensamientos en silencio. Este se rompe por el canto de los pájaros desde alguna parte en las copas de los árboles, seguido por el susurro de las hojas cuando los pájaros alzan el vuelo."

show rin basic_awayabsent
with charachange

rin "Tal vez. No estoy segura de si pueda tener algo como eso. Hasta ahora solo he pintado para mí misma."

show rin basic_absent
with charachange

rin "No creo que podría tener mis cosas en exhibición de la manera que soy ahora. Este yo no podría hacerlo."

"Sus razones suenan como una débil excusa. Frunzo mi ceño de mi modo característico, pero ella no lo nota."

hi "No lo entiendo. El maestro ciertamente piensa que podrías. No creo que lo sugeriría, de lo contrario. Suena como si estuviera pidiéndole favores a sus amigos, también."

show rin relaxed_nonchalant
with charachange

rin "Lo sé. Él ha hecho realmente mucho por mí. Pero esto podría ser demasiado."

show rin negative_confused
with charachange

rin "Convertirme en alguien que pueda hacerlo podría ser muy difícil. Tal vez no podría hacerlo en absoluto. Él no puede hacerlo por mí y si lo dejo intentar, yo solo me hundiría más y más."

"Rin está de pie frente al gran arce y me da la espalda. Quiero cerrar esos pocos pasos de distancia entre nosotros y… no lo sé. Mi enfado se ha ido repentinamente, y comienzo a sentir simpatía por ella."

hi "Sé exactamente cómo te sientes."

hi "Bueno, tal vez no, pero aun así."

hi "Creo que no me he sentido como si estuviera verdaderamente en control de mi propia vida durante todo este año. Simplemente yendo con la corriente, indefenso."

hi "Como venir aquí, a esta escuela. En realidad yo no la escogí por mí mismo. Y ciertamente yo no escogí este momento de mi vida para saber que tengo… esta condición."


"Todavía no puedo decir casualmente y en voz alta esa palabra."

hi "Es como… sí, es exactamente como estar bajo el agua. Como si no pudiera respirar."

show rin basic_sad
with charachange

"Rin se vuelve hacia mí una vez más, una expresión triste en su rostro."

rin "¿Es por eso que te ves tan triste todo el tiempo? No quiero verme triste como tú. ¿Me veo yo para ti como tú te ves para mí?"

hi "No me veo triste todo el tiempo."

hi "Es solo que… no sé qué debería de estar sintiendo. Qué tipo de cara debería de hacer."

show rin basic_upset
with charachange

rin "Yo tampoco. ¿Me veo triste ahora?"

hi "No realmente. Te ves como siempre, creo."

show rin negative_sad
with charachange

rin "Pero me estoy hundiendo."

show rin negative_worried
with charachange

rin "Debería tratar de flotar. Arriba, como un patito de hule. Cuac cuac, todo amarillo y espeluznante."

"Tengo que pensar por unos segundos en qué dirección debería seguir en esta conversación, entonces me doy cuenta de que no importa."

hi "¿Piensas que los patitos de hule son espeluznantes?"

show rin basic_surprised
with charachange

rin "¿Tú no? Yo creo que se ven muy espeluznantes. Todo lo que tiene ojos pero no está vivo es muy perturbador. Como patitos de hule y reflexiones en el espejo."

show rin basic_surprised:
    ease 0.5 ypos 1.2 alpha 0.0
with Pause(0.5)

hide rin
with None
play sound sfx_rustling


"Se deja caer debajo de los árboles, reclinándose sobre el arce que ella nombró el Árbol de la Preocupación. Después de preguntarme qué hacer por un minuto, también me siento a casi un metro de ella."

play sound sfx_rustling
$ renpy.music.set_volume(0.5, 2.0, channel="ambient")

scene bg worrytree:
    xalign 0.5 yalign 1.0 subpixel True
    acdc_warp 30.0 yalign 0.0
with whiteout

"El bosque nos envuelve con su abrazo, y su quietud cae sobre nosotros dos."

"Nos sentamos ahí sin hablar por un largo rato. Puedo literalmente sentir el paso del tiempo."


"Parches de luz de sol salpican el pequeño claro en un patrón que duplica el dosel de los arces. Uno de ellos cae directamente sobre mí, calentándome hasta los huesos."

"Me pregunto qué podría hacer para mí mismo, y tal vez para Rin. Por ahora solo continúo viéndola desde esta distancia."

"Algunas veces estira el cuello hasta atrás, tanto que parece casi doloroso, y mira los pequeños parches de cielo visible más allá del follaje del Árbol de la Preocupación."

"Algunas veces simplemente mira con ojos vacíos hacia enfrente, como si viera algo apenas más allá de su alcance. Sigue susurrándose a sí misma, pero tan bajo que no puedo oírla, aun si estoy sentado justo a su lado."

"Tan solo veo sus labios moverse, como si estuviera a la mitad de un sueño distante."

"Me doy cuenta de que, en este momento, ya no siento más nada de esa intensa soledad que siento en la noche, justo antes de quedarme dormido."

"Puede que sea más como Rin de lo que pensé."


"Puedo ya sea rendirme y quedarme sumergido bajo el peso de toda la basura en mi vida, o tratar de cambiarme a mí mismo en algo mejor."

"Su decisión es diferente, y sin embargo la misma."

"Y a diferencia de ella, tengo por seguro que no puedo quedarme así para siempre."

label es_choiceR9:

menu:
    with menueffect
    "Tengo que cambiar."
    "Quiero ser más como Rin.":


        return m1
    "Quiero ser más como Emi.":

        return m2

label es_R9a:


$ renpy.music.set_volume(0.5, 0.5, channel="ambient")
"Rin probablemente podría hacerlo. Aun si parece que duda de sí misma, yo no tengo dudas sobre su fuerza."

"Ella podría hacerlo, incluso si no puede."

label es_R9b:

$ renpy.music.set_volume(0.5, 0.5, channel="ambient")
"Emi probablemente lo ha hecho. Es tan alegre y enérgica, una chica corredora sin piernas."

"Si alguien ha “derrotado” una discapacidad, debe de ser ella."

label es_R9c:

"Me hace sentir un poco mejor, también, y me recuesto sobre el árbol, respirando profundamente como si fuera la primera vez en un largo tiempo."

show bg worrytree_ss:
    yalign 1.0
with shorttimeskip

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

"Nos quedamos así en el pequeño claro hasta que el ángulo del sol cambia y las frías sombras se profundizan. Ya sin estar caliente donde nos sentamos, dejamos el bosque, regresando por el mismo camino que tomamos de entrada."

scene bg school_forest2_ss
show rin negative_spaciness_ss at center
with locationchange

"No parece que Rin haya llegado a una decisión."

hi "Me pregunto si fue mala idea haberte acompañado."

show rin basic_absent_ss
with charachange

rin "Está bien. No me molesta. Estoy segura de que a los árboles y a la tierra y a las piedras tampoco les molesta. ¿A ti te molestó?"

hi "No, para nada. Creo que también me ayudó."

$ renpy.music.set_volume(0.4, 1.0, channel="ambient")
scene bg school_forest1_ni
with locationskip

"Mientras caminamos de vuelta a los dormitorios, el cielo cambia a un profundo azul de ultramar. Las primeras estrellas del verano titilan suavemente a través de aberturas en el follaje, apenas visibles como diminutas luciérnagas."

"He llegado a estar muy consciente de la presencia de Rin."

window hide
nvl clear
nvl show dissolve

stop ambient fadeout 2.0

n "\n\n\n\nNo he pensado mucho en chicas desde que las cosas se vinieron abajo con Iwanako."

n "Esta es casi la misma situación que entonces, pero para ser honesto no creo que realmente cuente para mucho. No con Rin."

n "Aun así… se siente bien caminar junto a ella, incluso si no es nada más que esto."

n "Al principio, creo que Rin me inquietaba bastante con su comportamiento impredecible. Pero recientemente siento que no he tenido que mantenerme alerta tanto."

n "He logrado dejarme ir un poco. Eso me hace sentir satisfecho, a pesar de que, en última instancia, creo que es más gracias a Rin que a mí mismo."

n "Ella parece estar desinteresada en un enorme número de cosas, pero algo en ella hace que me esfuerce más de lo que normalmente lo haría."

nvl clear


n "\n\n\nNo es que quiera impresionarla; creo que verdaderamente impresionar a Rin requeriría un esfuerzo casi sobrehumano tan solo por cómo es ella. En lugar de eso, es porque está este implacable sentimiento dentro de mí diciéndome que no debería defraudarla."


n "Es realmente extraño. Me pregunto por qué empecé a pensar así. Ni siquiera sé qué tipo de expectativas tiene sobre casi nada."



n "Así que, ¿cómo podría defraudarla? Rin tiene este aire de modestia a su alrededor, y ella realmente no habla sobre cosas muy seguido. Incluso la confesión de hoy sobre su desconfianza en sí misma me tomó un poco con la guardia baja."

n "Siento como si quisiera hablar más con ella."

n "De pronto me doy cuenta de que Rin es, básicamente, la única persona con la que he hablado últimamente, aparte de lo que sea que tenga que soportar de Shizune, Misha o Kenji. Me siento un poco deprimido."

nvl clear
nvl hide dissolve

scene bg school_dormext_full_ni at bgright
with locationskip

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_cicadas fadein 1.0

window show


"Frente a los dormitorios, como si hubiese sido invocado por mis oscuros pensamientos, nos topamos con el mismísimo Kenji."

show kenji tsun_ni at center
with charaenter

"Se siente muy extraño verlo afuera, respirando aire fresco del exterior. Por lo menos ya es de noche; casi espero que Kenji se desintegre después de ser expuesto directamente al sol."

"Kenji también se ve muy inseguro, parado ahí viéndose como si estuviera esperando algo, pero sin saber él mismo qué podría ser."

hi "Qué tal, Kenji. ¿Qué estás haciendo?"

show kenji tsun_ni at twoleft
show bg school_dormext_full_ni at center
with charamove

show rin basic_awayabsent_ni at tworight
with charaenter

rin "Hola."

stop ambient fadeout 0.2

show kenji rage_ni
with charachange
with vpunch

ke "¿Quién eres tú?"

play music music_tension

show rin basic_absent_ni
with charachange

hi "Soy yo, Hisao. Ahh… ¿no sé si conoces a Tezuka del grupo 3-4?"

show kenji tsun_ni
with charachange

"Por su rostro puedo ver que no solo no conoce a Rin, él tampoco puede verla desde esta corta distancia."

show kenji happy_ni
show rin basic_awayabsent_ni
with charachange

stop music fadeout 0.5

ke "Oh, ¿qué hay, viejos?"

play music music_kenji
play ambient sfx_cicadas fadein 6.0


"Kenji lanza su mano entusiásticamente hacia adelante, casi directamente al estómago de Rin."

show rin negative_spaciness_ni
with charachange

"Rin mira la mano extendida de Kenji, confundida, hasta que él aclara la garganta y retrae su mano."

show kenji neutral_ni
with charachange



"Eso es algo casi fascinante que logra hacer con ineptitud social. No es que yo sea el hombre más afable del planeta, pero no creo que alguna vez vaya a ser capaz de siquiera aproximarme al nivel de Kenji."

"Creo que respeto a Kenji un poquito más."

show rin basic_absent_ni
with charachange

hi "Así que, ¿estás esperando a alguien?"

show kenji tsun_close_ni
with characlose

"Él se me acerca y baja su voz a un agitado susurro. Veo sus músculos faciales retorcerse."

ke "Vamos hombre, sabes que no puedo hablar de cosas en público. Ellas podrían estar escuchando."

ke "Voy a tener que ir a recoger algunas cosas en algún lugar, y no quiero a esas entrometidas arpías del consejo estudiantil metiéndose en mis asuntos."

ke "Además, no confío en tu amigo. Nada personal. ¿Estás seguro de que es digno de confianza?"

"Brevemente considero decirle a Kenji del sexo de Rin, pero como podría terminar mal para uno o ambos, decido lo contrario."

hi "Sí, estoy seguro."

show kenji neutral_ni
show rin basic_awayabsent_ni
with charadistant

"Se voltea hacia Rin e inmediatamente tengo la sensación de que debo evitar que hablen entre ellos por cualquier medio necesario. Sin embargo, es poco lo que puedo hacer ahora, aparte de recurrir a la violencia física."

show kenji happy_ni
with charachange


ke "En ese caso, ¿estarías interesado en saber acerca de la peor amenaza para el hombre desde que inventaron el vegetarianismo?"

"Suena como un vendedor de aspiradoras."

show rin basic_deadpan_ni
with charachange

rin "Pensé que era el domingo."

show kenji neutral_ni
show rin basic_awayabsent_ni
with charachange

ke "Veo que no estás enterado. Sí hombre, estoy hablando de las vacas devoradoras de hombres. Muy pocos saben lo que sé, así que no estoy sorprendido."

show kenji happy_ni
with charachange

ke "No podemos hablar aquí, pero si quieres un folleto, ven a mi habitación después del toque de queda en los lunes o miércoles."

"Repentinamente se lleva la mano a su bolsillo y saca un bolígrafo y lo que parece ser un recibo de minisúper."


"Kenji garabatea con furia sobre el trozo de papel y luego lo empuja hacia donde Rin."

show kenji neutral_ni
with charachange

ke "Aquí está la contraseña. Memorízala y luego erradica cualquier rastro de este documento. Cómetelo, quémalo, disuélvelo en ácido, lo que sea."

"Tomo el recibo de la mano de Kenji, ya que Rin es incapaz de hacerlo, y le echo un ojo. Definitivamente es un recibo, aparentemente para dos bolas de arroz y cinco cajas de cerillos. Espero que no esté planeando incendiar algo."

"Del otro lado está escrita solo una palabra."

window hide

$ written_note(u"PANQUECITODEMIEL")

show rin basic_absent_ni
with charachange

window show

"Se lo muestro a Rin también, pero no muestra reacción alguna."

show rin basic_awayabsent_ni
with charachange

rin "Gracias."

show kenji tsun_ni
with charachange

ke "Oye, Hisao. ¿Sigues en ese club? ¿El club de las artes oscuras?"

show rin basic_absent_ni
with charachange

hi "De bellas artes. Como sea, sí, de hecho tuvimos una reunión justamente hoy."

show rin basic_awayabsent_ni
show kenji neutral_ni
with charachange


ke "¿Todavía sigues cuerdo? ¿Ningún turbio truco mental por ahí? Nada personal hombre, pero tengo que estar en control de todos los asuntos."

show kenji tsun_ni
with charachange

ke "No me deben atrapar con los pantalones abajo. Hablando de eso, realmente deberías de tomarte una ducha en un rato. Hay que respetar ese espacio personal. Nada personal."

"Kenji mira alrededor como si hubiese escuchado algo y luego se endereza la chaqueta."

show kenji neutral_ni
with charachange

ke "Bueno, me tengo que largar antes de que sea demasiado tarde. Nos vemos, viejos. Buena suerte."

hide kenji
with charaexit

show bg school_dormext_full_ni at bgleft
show rin basic_deadpanupset_ni at center
with dissolvecharamove
stop music fadeout 4.0

"Kenji arranca deprisa hacia el portón principal. Rin lo ve marcharse con el ceño fruncido."

"Ambos vemos en silencio la figura de Kenji disminuirse."

show rin basic_deadpancontemplation_ni
with charachange

rin "¿Qué le pasa?"

hi "Técnicamente hablando, creo que es legalmente ciego."

show rin basic_deadpansurprised_ni
with charachange

rin "Oh. Ya veo."

stop ambient fadeout 2.0

scene black
with dissolve




label es_R10:

scene ev hisao_letter_closed
with locationchange


"Puedo notar de inmediato por el sobre que no se trata de asuntos oficiales de ningún tipo. Alguien me envió una carta escrita a mano en papel, a la antigua."

"En todo caso, ¿quién se molesta en hacer algo como eso en estos días? Sin embargo, tan improbable como suene la posibilidad de recibir una, definitivamente hay una carta sobre mi escritorio."

scene bg school_dormhisao
with locationchange

"Las clases por el día se han terminado. Aún sintiéndome bastante lleno por el gran almuerzo que inesperadamente comí en la cafetería, regresé a mi dormitorio, planeando terminar mi tarea y quizás saltarme la cena, o por lo menos comer ligero."

"Siento que necesito comer menos de lo que solía. Tal vez no uso tanta energía, ahora que no hago mucho además de leer."

"De cualquier modo, la carta en mi escritorio naturalmente ha captado mi interés."

scene ev hisao_letter_closed:
    xalign 0.5 yalign 0.5 zoom 1.1 subpixel True
    acdc_warp 10.0 zoom 1.0
with locationchange

"Es lo primero que me llega por correo aquí en Yamaku, así que se sentiría especial incluso si no fuera algo tan raro como una carta escrita a mano."

"Lo que me causa más inquietud es el nombre del remitente, pulcramente escrito en el reverso del sobre."

"Iwanako."

"No tengo idea de por qué me escribiría. No he estado en contacto con nadie de mi antigua escuela desde que me transfirieron, e Iwanako es la última persona que esperaría que quisiera escribirme una carta."

window hide
nvl clear
nvl show dissolve

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_rain fadein 4.0

n "\n\n\nLa última vez que vi a Iwanako fue terriblemente incómodo; hasta vergonzoso. Vino a mi cuarto de hospital, me peló una manzana por cortesía y luego prácticamente nos sentamos en silencio por media hora."

n "Ella dijo “adiós” y no me vio a los ojos cuando cerró la puerta."

n "Puede que haya sido un fin natural a la serie de visitas que probablemente fueron bastante dolorosas para ambos."

n "Cada vez que me visitaba en el hospital, quería hablar con ella pero algo siempre me lo impedía. Cada vez que no hablaba, hacía que fuera más difícil en la siguiente ocasión."

n "Iwanako siempre tuvo este aura de fragilidad en torno a ella, como si fuera a romperse en pedazos ante la perturbación más pequeña. Inicialmente pienso que podría haber sido esa delicadeza la que me atrajo de ella, pero después de lo que sucedió en ese entonces, se sentía como si realmente se hubiera roto."

nvl clear

n "\n\n\n\n\nSe veía tan triste que no quería decir nada que pudiera molestarla, y nunca pude encontrar las palabras correctas que decir."

n "Le dije que no era su culpa, ella asintió y realmente creo que ella entendió que, si no hubiera sido eso, entonces tarde o temprano algo más hubiera hecho fallar a mi corazón."

n "Sin embargo, ella se veía tan irremediablemente triste cada vez que abría esa puerta y entraba a mi cuarto."

n "Así que nunca logré decir las cosas que quería decir. Al final, eso puede haberla lastimado aún más."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

scene ev hisao_letter_open
with locationchange

window show

"Con cuidado, abro el sobre y saco la carta doblada del interior."

window hide



$ written_note("Querido Hisao,\n\n¿Cómo estás? Espero que estés bien y feliz en tu nueva escuela. Todos aquí te extrañan. Casi todo nuestro grupo de segundo año fue colocado junto en el grupo 3-1 para el último año, así que hemos estado bastante cómodos desde el principio. Estoy segura de que habrías sido asignado a este, también.")

$ written_note("Los ánimos entre los de tercer año parecen ser de muchas ansias por los exámenes finales, aun estando tan lejos. Los maestros nos fastidian por ello todo el tiempo, incluso el viejo señor Tachibana quien es, por cierto, nuestro maestro de cabecera este año. ¿Podrías creerlo? Estaba segura de que se retiraría después de nuestro segundo año, pero aquí está, dándonos lata a todos para que estudiemos para los exámenes.\n")


$ written_note("Creo que cosas como esa son la principal razón de que los ánimos entre los de tercero sean de tanto nerviosismo. Debo admitir que de algún modo también estoy perdiendo confianza en mí misma, a pesar de que siempre me ha ido razonablemente bien en los exámenes.\n\n\n\n\n")

$ written_note("Es tan extraño pensar que ya estamos en el último año, ¿no es así? El tiempo realmente ha pasado volando. Me pregunto adónde fue. Los nuevos de primer año parecen tan jóvenes y de algún modo tan inocentes. No dejo de preguntarme si yo era como ellos en mi primer año. He estado sintiéndome así de nostálgica durante todo el primer trimestre.\n\n\n")

show ev hisao_letter_open:
    "ev hisao_letter_open_2" with locationchange
with None
$ ksgallery_unlock("ev hisao_letter_open_2")

$ written_note("Hay otras cosas que quiero decir. Te estoy escribiendo porque sentí que hay cosas que debería haber dicho después del incidente en aquel invierno. Realmente me arrepiento de no haber sido capaz de decirlas en persona, y no tengo excusa para ello.\n\n\n\n\n")

$ written_note("La verdad es, las veces que te visité en el hospital hicieron que me preocupara por ti. No estoy hablando de tu salud. Parecías haberte distanciado y desanimado más. Era natural después de que ocurriera algo como eso, estoy segura, pero de alguna manera tuve la sensación de que habías renunciado a algo en ese entonces. ¿La felicidad, tal vez?\n")

$ written_note("Quería por algún medio expresar mis sentimientos, pero las palabras correctas no venían a mí. No podía decir algo para consolarte. Realmente siento no poder haberte apoyado cuando más lo necesitabas, aunque me gustes tanto. Por lo menos ahora, finalmente, puedo ser más honesta.\n\n\n\n")


$ written_note("Si pudiera volver a aquellos días silenciosos en febrero y marzo, te diría que no renunciaras a ti mismo. Eso es lo que diría. Quizás no te hubieses alejado tanto si tan sólo hubiera dicho algo. Espero que hayas podido recuperarte por tu cuenta.\n\n\n\n")

$ written_note("Ahora que la distancia entre nosotros es también física, se siente también más definitiva, de algún modo. Me pregunto si nos encontraremos de nuevo. ¿Tal vez sea mejor si no? Aun así, si te gustaría mantener correspondencia conmigo, por supuesto que puedes escribirme de vuelta. Me agradaría mucho escuchar sobre tu nueva escuela y cómo te está yendo. Te deseo todo lo mejor.\n\nAtentamente, Iwanako")

window show

"Tras terminar de leer la carta, la doblo como estaba y la pongo sobre mi escritorio."

"No sé qué pensar de esto. Me siento vacío y confundido."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\n¿Por qué ahora, después de todo este tiempo?"

n "Tan solo ayer decidí que no puedo permitirme quedarme así, que trataría de ponerme en control de mi propia vida. Leer esta carta únicamente me recuerda lo que podría haber sido."

n "Por supuesto que deseo no haber tenido que estar aquí. Me gustaría estar en el mismo grupo de Iwanako, de nuevo. Tal vez podríamos hablar todos los días ahora e ir a citas."


n "\nMi vida no fue por ese camino."

n "En verdad no necesitaba ser recordado de esto. Iwanako necesitaba escribir esta carta por su propio bien y estoy contento por ella de que haya podido hacerlo, pero habría sido mejor si no la hubiera leído."


n "\nDesde luego, ella está en lo correcto. Pensé en lo mismo el día de ayer. Caí en un agujero de depresión y ahora tengo que escalar para salir."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

scene bg school_dormhisao
with locationchange

window show

"Arranco una hoja de mi cuaderno, y después de un momento de pensar en cómo estructurar mis palabras, le escribo una corta respuesta a Iwanako."

"Encuentro difícil serle realmente honesto, pero por lo menos intento parecer un poco convincente. No le escribo sobre Yamaku en absoluto."


"Dudo que me escriba de nuevo, pero no me siento para nada triste por ello. Doblo mi carta y, ya que no tengo un sobre, la coloco enseguida de la de Iwanako. Se la mandaré después."

"Luego me acuesto en mi cama, mirando al monótono techo gris."

"Un pájaro canta fuera de mi ventana y una repentina ráfaga de viento agita mis cortinas. La tarde de verano se siente inmóvil, como si el tiempo se hubiese detenido por un breve momento."

"Pienso en todas las cosas que he perdido y nunca recuperaré."

stop music fadeout 2.0

scene black
with dissolve

$ suppress_window_after_timeskip = True




label es_R11:

window hide None

play music music_night

scene bg misc_sky at Fullpan(60.0)
with locationchange

nvl clear
nvl show dissolve

n "Así pasan los lánguidos días de mitad de junio."

n "Mando mi carta a Iwanako, y no recibo respuesta."

n "Habiendo decidido deshacerme de mi viejo yo, comienzo a observar a mis compañeros más de cerca de lo que lo hacía antes, con esperanza de entender cómo otra gente enfrenta sus propios problemas."

n "Empiezo a ver cosas que no veía antes, y eso hace que me pregunte si he estado equivocado dos veces."


n "Superficialmente, todos son anormales y sin embargo son tan sorprendentemente normales que me impactó al principio. Admiré la forma en que mis nuevos compañeros pusieron de cabeza mis prejuicios así como así, simplemente siendo ellos mismos."

n "Ahora que me he acostumbrado, comienzo a darme cuenta de otros tipos de tonos en la gente que me rodea cada día."

n "\nSe encuentra esta suave y adormecida tristeza a mi alrededor."

n "Puedo ver el esfuerzo que todos tienen que hacer solo para pasar el día, y cómo pesa sobre sus hombros, así como pesa en los míos."


nvl clear
n "Incluso la más brillante sonrisa está tenuemente apagada, todo estallido de enojo apenas disminuido. Es sutil, pero definitivamente está ahí."



n "Trato de pensar en lo que significa, en qué puedo aprender de otros. Me pregunto si, muy hacia sus adentros, todos están tan perdidos como yo. ¿Hay acaso aunque sea una persona aquí que verdaderamente haya encontrado la paz? Empiezo a tener dudas de mí mismo una vez más."


n "No puedo decidir si estas personas son felices, infelices, o si solo han aprendido a sobrellevarlo y ahora viven en un limbo insensible como lo hice yo toda la primavera."


n "Escapo de estos sentimientos hacia las altísimas pilas de libros que llevo a mi habitación desde el santuario de Yuuko. Después de darme cuenta de que esto solo me deprimirá aun más, comienzo a ir al salón del club de arte más seguido, usualmente cada vez que puedo."

n "\nRin también parece pasar más tiempo ahí dentro que en su propio salón."

n "Con frecuencia la he visto bambolearse hacia la puerta en el extremo de nuestro corredor. Esa puerta de madera y el salón detrás de esta, el olor de pintura y papel, para ella parecen significar más que el resto del mundo combinado."

nvl clear

n "Ella dice que tiene permiso especial para usar el salón, lo cual no dudo para nada. No creo que Nomiya le negaría algo a Rin."



n "\n\nÉl parece consentirla como un tío a su sobrina favorita."




n "El objeto de su cariño, no obstante, no tiene favoritos. Ella dice que aprecia mucho al maestro por dar un paso extra por su bien, pero incluso cuando dice eso, su expresión es la misma de siempre."

n "Es como si estuviese hablando acerca de una roca con particularmente nada en especial que vio el otro día. Realmente no puedo comprender su relación."

n "Rin parece no dejar que nadie se acerque. No creo que siquiera Emi pueda decir que haya cruzado ese espacio que parece separar a Rin del resto del mundo."

n "\n\nNo lo entiendo. Ella parece tan indiferente, sin embargo tan apasionada al mismo tiempo."

play sound sfx_normalbell

n "En algún lugar, las campanas de la escuela dan el último llamado del día."

stop music fadeout 5.0

nvl hide dissolve
nvl clear

scene bg school_classroomart
with locationchange

window show

"Me percato de que me he quedado ido por quién sabe cuánto tiempo. Aturdido, me siento más derecho, tratando de llamar la atención tan poco como sea posible."

"Los olores acres del aceite de linaza y aguarrás se mezclan en mis fosas nasales cuando tomo aire con profundidad. Me siento somnoliento y mareado."

"Ya es tarde y algunos de los miembros del club se fueron temprano, así que somos solo yo, Rin, el maestro, y otras dos chicas que también están a punto de marcharse."

play music music_soothing fadein 4.0

scene ev rin_painting_base
with locationchange

"Rin está sentada a mi derecha, lentamente trabajando en una pintura mientras yo paso el tiempo. No creo que se dé cuenta de que la he estado viendo todo este tiempo."

scene ev rin_painting_foot:
    xalign 0.5 yalign 0.0 subpixel True
    ease 7.0 yalign 1.0
with locationchange

"Con un ágil movimiento de su delicado tobillo, ella moja el pincel en la pintura carmesí y lo presiona ligeramente sobre el lienzo. Una mancha se extiende, como si la brocha estuviera sangrando."

"Su progreso se ha vuelto muy lento. Para ahora he aprendido que esto es peligroso para su técnica, ya que no se le debe permitir a la pintura secarse antes de que ella haya terminado."


"Se me viene a la mente que literalmente estoy viendo pintura secarse. Y sin embargo, de algún modo, no me estoy aburriendo a pesar de haberme perdido en mis pensamientos hace poco."

window hide

$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene ev rin_painting_base
with locationchange

nvl clear
nvl show dissolve

n "\n\nLa mayor parte del tiempo, el club de arte es muy relajado y de forma libre. Aparte de las veces en las que Nomiya se emociona mucho por alguna técnica o estilo que nos quiere enseñar, todos son libres de seguir sus propios intereses."

n "Carente de uno, sigo dando vueltas sin rumbo. Pruebo esto y aquello, pero nada realmente me deja una impresión profunda, eso sin mencionar que no parezco tener una habilidad especial para alguna cosa."

n "Bueno, me felicitaron por tratar de trabajar con acuarelas, y me sentí muy bien por ello, pero eso es todo."

n "Supongo que es de esperarse. Me uní al club de arte más que nada por un capricho, después de todo."


n "Estoy pensando en que tal vez debería renunciar al club, si es que será así de inútil. Pero no hay nada realmente malo con que sea así y no puedo decir precisamente que me encuentre descontento."

n "\nInsatisfecho quizás, pero solo me puedo culpar a mí mismo por ello."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

scene bg school_classroomart
with locationchange

window show


"Cuando el par de chicas salen del salón del club con un alegre “hasta luego”, Nomiya se levanta de su escritorio. Su silla sale lanzada hacia atrás con un fuerte chirrido que rompe la armonía de esta silenciosa tarde."

"Le da dos golpecitos a un montón de hojas que tiene en las manos contra la superficie de su escritorio para enderezarlas, luego estira su espalda."

show nomiya smile
with charaenter

no "Tengo una reunión de maestros a la cual atender, así que no puedo quedarme. Tendré que hacer algo de papeleo, así que si quieren quedarse podemos hablar entonces. Discúlpenme."

"Hay dos personas aquí, pero en realidad solo está hablando con uno de nosotros."


"Nomiya invierte horas extra de su tiempo aconsejando a Rin después de que el horario oficial del club haya pasado, y apuesto a que le gustaría discutir un poco más su plan de poner el arte de Rin en una galería."

scene ev rin_painting_base
with locationchange

rin "Está bien. Creo que probablemente estaré aquí, pero no es gran cosa si no estoy. En verdad no tengo mucho que hacer ahora."

"Rin responde sin mover sus ojos de la obra en curso. El tono de su voz no es del tipo cortés que se espera cuando se habla con un maestro, ni su usual monótono."

no "¿Así que no tengo que mandar un equipo de búsqueda si no estás aquí?"


rin "Sí, no gracias, no me gusta estar en un equipo. Podemos hablar después."

scene bg school_classroomart
show nomiya veryhappy
with locationchange

no "Buena chica."

hide nomiya
with charaexit

stop music fadeout 6.0

"Sonriendo, el maestro recoge el resto de sus papeles y se dirige a la puerta. Miro el reloj sobre esta y luego a mi reloj de pulsera para corroborar."

"Tienen tres minutos de diferencia, y de cualquier modo la reunión del club se ha terminado ya."

"Rin parece decidida a quedarse aquí a trabajar en su cuadro mientras espera al maestro."

"No puedo imaginarme cómo sería su tiempo a solas."

"¿Realmente discutirían algo? Rin es siempre tan parca en lo que dice, y cuando realmente dice algo es difícil de entender de lo que está hablando."

"Quizás Nomiya simplemente habla sin parar como lo hace en las reuniones del club, dejando que Rin absorba lo que quiera de su fuente infinita de conocimiento del arte, como un girasol girando su cara hacia el brillante sol."

scene ev rin_painting_base
with locationchange

hi "¿Te importa si me quedo? Yo eh… pensé en tal vez probar otra vez con acuarelas."

"Pronuncio esa excusa un poco por accidente, avergonzándome. Rin no aparta la mirada de su pintura."

rin "Está bien."

scene bg school_classroomart
with locationchange


"Me muevo de mi silla, luego voy por una taza de agua, pinceles, colores y algo de papel. El sonido de mis pisadas invade el quieto aire de la tarde."


"Antes de empezar, trato de recordar lo que nos dijo el maestro, una importante filosofía sobre el medio: trabajar con acuarelas significa más trabajar con agua que con color."
"Trato de mantener eso en mente, y mojo mi diminuto pincel de marta en la taza de agua."

"Estoy mezclando amarillo y azul, intentando capturar las copas de los árboles iluminadas por el sol fuera de la ventana. El sol está bajo, así que los amarillos son más pronunciados y todo se ve más oscuro."

"Todavía no puedo conectar bien lo que veo con lo que mi mano hace con las pinturas, pero es un intento pasable para mi nivel."


"Después de un rato comienzo a perder mi concentración y hago el papel a un lado, decidiendo mejor ver a Rin trabajar por un momento."

"Ese corto momento se extiende primero en un largo rato, luego en un muy largo rato."

play music music_dreamy fadein 1.0

scene ev rin_painting_base
with locationchange


"Rin pinta, todo su ser completamente concentrado en el pincel entre sus finos dedos y la pintura que cobra vida un trazo a la vez."

"Ella se ve tan decidida y sin embargo relajada a la vez, moviendo el pincel sin esfuerzo, nunca titubeando. Los colores se encuentran y se separan, se mezclan y se cubren los unos a los otros sobre el lienzo, doblegándose a su silenciosa voluntad."

"No sé nada sobre composición, estructura o nada de esas cosas, pero realmente me gustan las pinturas de Rin. Me gusta cómo se ve cuando pinta."

"Como es usual, el silencio entre nosotros me obliga a hablar en lugar de simplemente esperar a que ella se abra. Puede que ella termine sin decir nada en absoluto."

hi "¿Te molesta si hablamos?"

scene ev rin_painting_reply
with locationchange

rin "No me molesta."

hi "Quería preguntarte un poco más sobre por qué te pones tan rara con eso que el maestro quiere arreglar por ti."

"Rin toma un tubo de pintura y lo aprieta entre los dedos sobre una paleta casi con tanta facilidad como la de alguien con pulgares oponibles. Retomando el pincel de nuevo, ella responde."

scene ev rin_painting_concerned
with locationchange

rin "Muchas cosas. Y algunas no-cosas. Descosas. No creo que esa sea una palabra."

hi "¿Quieres hablar de ello?"


"Trato de alcanzarla con torpeza, ignorando la embarazosa sensación de la impericia."
"Rin mantiene su concentración en la obra, untando más y más pintura sobre el lienzo, sus labios formando una línea perfectamente recta a medida que se concentra en el trabajo."

scene ev rin_painting_base
with locationchange

rin "No realmente."

scene ev rin_painting_reply
with locationchange

rin "Hablar es difícil. Quiero decir, no es difícil, estoy hablando incluso ahora. Pero decir las cosas correctas me es muy difícil."

scene ev rin_painting_concerned
with locationchange

rin "Sin importar qué, solo no puedo decir las cosas que quiero."

hi "Eso suena extraño."

scene ev rin_painting_base
with locationchange

rin "Es verdad. Digo todo tipo de cosas que realmente no quiero decir todo el tiempo. Y algunas veces olvido palabras y entonces uso las palabras equivocadas. Incluso invento nuevas palabras para cosas que ya las tienen. Eso es lo peor."

rin "Me pongo muy nerviosa y todo sale hecho un desastre y ni siquiera yo entiendo realmente qué quiero decir."

scene ev rin_painting_concerned
with locationchange

rin "Creo que hay algo mal conmigo que lo hace así. ¿Recuerdas cuando te dije que solo puedo pensar en cuatro cosas a la vez?"

"Asiento sin decir una palabra."

scene ev rin_painting_reply
with locationchange

rin "En realidad no son cuatro. Quiero decir, sí son cuatro, pero todo lo demás también está ahí, algo así como en el fondo. Como estar en un parque de diversiones y en un panal de abejas al mismo tiempo. Pero ese no es el punto."

rin "Solía hacerlo mejor. Como seis o siete cosas. Eso creo, al menos. Siento que me estoy haciendo más tonta."

hi "Pienso que todos tienen momentos en los que se sienten como si no pudieran decir lo correcto."

scene ev rin_painting_base
with locationchange

rin "Pero está ahí todo el tiempo. Más fuerte y más profundo. Sí, más profundo es una buena frase. Me gusta esa frase. Más profundo."

rin "Es esa sensación de estar bajo el agua. Tal vez sea solo el arte."

scene ev rin_painting_reply
with locationchange

rin "Mientras más pinto, más son las palabras que olvido. Quizás llegue un momento en el que olvide cómo hablar por completo."


rin "Se siente como si lentamente estuviera olvidándolo todo. ¿Recuerdas lo que pensabas de las cosas hace tres o cuatro años?"

rin "Yo no."

"Sigue una larga pausa, durante la cual el tiempo parece doblarse sobre sí mismo, casi atándose a sí mismo en un nudo. No creo haber escuchado nunca antes a Rin hablar de algo con tanta seriedad por tanto tiempo."

scene ev rin_painting_concerned
with locationchange


rin "Es como si estuviera desapareciendo de la tierra."

scene ev rin_painting_faceconcerned:
    xalign 0.5 yalign 0.5 zoom 1.0 subpixel True
    easein 10.0 zoom 1.05
with locationchange

"El pie de Rin ha terminado su trabajo sobre el lienzo y ella se queda mirando su pintura, inmóvil, como si contemplara algún horizonte lejano."


"La luz del sol brilla brevemente en el rincón de sus ojos de ónice. Algo flota hacia la superficie del ser de Rin y ella deja salir un largo suspiro."

scene bg school_classroomart
show rin basic_lucid_close:
    tworight
    ypos 1.1
    0.2
    "rin basic_awayabsent_close" with Dissolve(0.3, alpha=True)
with locationchange

stop music fadeout 0.3

"Entonces parpadea y se ha ido."

show rin basic_absent_close
with charachange

rin "Las pinturas permanecen. Cuando veo mis viejas cosas, recuerdo lo que estaba pensando cuando las hice."

show rin basic_lucid_close
with charachange

rin "Me hacen sentir como si pudiera estar con todos los yos pasados cuando era una yo diferente."

show rin basic_awayabsent_close
with charachange

rin "Supongo que son la prueba de mi existencia."

"Ella usa las mismas palabras que Nomiya utilizó cuando nos habló sobre la naturaleza del arte. No pensé que Rin estuviese prestando nada de atención, en ese entonces."
"Me pregunto si estaba escuchando, o si había escuchado el mismo discurso apasionado de Nomiya anteriormente."

"Sea como sea, me siento abrumado."

hi "Vaya que eres complicada. Yo hubiera escogido escribir un diario."

show rin basic_absent_close
with charachange

show rin basic_awayabsent_close
with charachange


"Sus ojos revolotean en dirección mía y luego de vuelta a la pintura, pero ella ya no recoge el pincel."

play music music_rin fadein 0.5

rin "Esa es una idea grandiosa. ¿Por qué nunca pensé en eso antes?"

hi "¿Estás siendo sarcástica?"

show rin basic_deadpan_close
with charachange

rin "¿Qué es sarcasmo?"


"No le presto atención a su broma, si es que la es."

show rin basic_awayabsent_close
with charachange

"Justo en ese momento, Nomiya regresa de su reunión. Nos saluda de una manera bastante melodramática, ligeramente sorprendido de verme aquí junto con su estudiante predilecta."
"Caminando con paso ostensible hacia su escritorio, deja caer sus papeles en este."

"Toma un pañuelo y limpia sus anteojos con un cuidado increíblemente minucioso antes de caminar hacia nosotros."

"Antes de que esté al alcance del oído, Rin me dice algo en una voz rápida y baja."

stop music fadeout 0.5

show rin basic_absent_close
with charachange

rin "El cambio es lo más escalofriante en el mundo para mí."

show rin basic_upset_close
with charachange

rin "Y en verdad no sé si quiero cambiar en una persona que pudiera hacer lo que el maestro quiere que haga. No sé si pudiera aun si lo quisiera."

show nomiya talk behind rin at twoleft
with charaenter

no "¡Hola de nuevo!"

$ doublespeak(hi,rin,"Hola.")

show nomiya smile
with charachange

play music music_pearly fadein 5.0

no "¿Qué sucede?"

"Él sonríe con un poco de timidez, viéndonos a los dos con interés desinhibido."

hi "Ah, nada. Solo estábamos hablando sobre esa cosa con su conocida y la galería. Para el trabajo de Rin. Más o menos."

show nomiya veryhappy
with charachange


no "¿Ajá? ¿Alguna decisión?"

"Miro a Rin, quien trata de arreglar la expresión de molestia sobre su rostro en algo más."
































label es_choiceR11aaa:
menu:
    with menueffect
    hi "En cualquier caso, no creo que tenga mucho más que decir, aparte de que deberías intentarlo."
    "Creo que serías un gran éxito.":


        return m1
    "Porque sería emocionante.":

        return m4
    "Titubear de esta manera no es para nada típico de ti.":

        return m5


label es_choiceR11baa:
menu:
    with menueffect
    hi "En cualquier caso, no creo que tenga mucho más que decir, aparte de que deberías intentarlo."
    "Estarías desperdiciando tus talentos de otro modo.":


        return m2
    "Porque sería emocionante.":

        return m4
    "Titubear de esta manera no es para nada típico de ti.":

        return m5


label es_choiceR11aba:
menu:
    with menueffect
    hi "En cualquier caso, no creo que tenga mucho más que decir, aparte de que deberías intentarlo."
    "Creo que serías un gran éxito.":


        return m1
    "No tendrás una oportunidad como esta otra vez.":

        return m3
    "Titubear de esta manera no es para nada típico de ti.":

        return m5


label es_choiceR11aab:
menu:
    with menueffect
    hi "En cualquier caso, no creo que tenga mucho más que decir, aparte de que deberías intentarlo."
    "Creo que serías un gran éxito.":


        return m1
    "Porque sería emocionante.":

        return m4
    "Deberías apuntar alto.":

        return m6


label es_choiceR11abb:
menu:
    with menueffect
    hi "En cualquier caso, no creo que tenga mucho más que decir, aparte de que deberías intentarlo."
    "Creo que serías un gran éxito.":


        return m1
    "No tendrás una oportunidad como esta otra vez.":

        return m3
    "Deberías apuntar alto.":

        return m6


label es_choiceR11bab:
menu:
    with menueffect
    hi "En cualquier caso, no creo que tenga mucho más que decir, aparte de que deberías intentarlo."
    "Estarías desperdiciando tus talentos de otro modo.":


        return m2
    "Porque sería emocionante.":

        return m4
    "Deberías apuntar alto.":

        return m6


label es_choiceR11bba:
menu:
    with menueffect
    hi "En cualquier caso, no creo que tenga mucho más que decir, aparte de que deberías intentarlo."
    "Estarías desperdiciando tus talentos de otro modo.":


        return m2
    "No tendrás una oportunidad como esta otra vez.":

        return m3
    "Titubear de esta manera no es para nada típico de ti.":

        return m5


label es_choiceR11bbb:
menu:
    with menueffect
    hi "En cualquier caso, no creo que tenga mucho más que decir, aparte de que deberías intentarlo."
    "Estarías desperdiciando tus talentos de otro modo.":


        return m2
    "No tendrás una oportunidad como esta otra vez.":

        return m3
    "Deberías apuntar alto.":

        return m6





label es_R11a:


hi "Creo que serías superpopular. Quiero decir, tus pinturas son realmente sorprendentes."

hi "Y pintas con los pies; eso también es bastante fantástico. Apuesto a que la gente estará asombrada."

show rin basic_deadpanupset_close
with charachange

rin "No es gran cosa. Pintaría con las manos si las tuviera."

hi "Oh… lo siento. Disculpa, no quise decirlo así."

show rin negative_confused_close
with charachange

"Rin me da la espalda, viendo su pintura melancólicamente. Quisiera retractarme de lo que dije si eso fue lo que la hizo tener esa cara."

rin "Entiendo."


label es_R11b:


hi "Estarías dejando que tu talento se fuese a la basura si no lo haces."

show rin basic_surprised_close
with charachange

rin "¿Irse adónde?"

hi "A la basura. Pienso que sería un desperdicio para otras personas no ver estas cosas."

"Trato de presionarla un poco, para extraer algún tipo de decisión de ella, pero Nomiya elige intervenir."

show nomiya smile
show rin basic_awayabsent_close
with charachange

no "Oh, no es tan malo."

show nomiya talk
with charachange

no "Coincido en que es importante aprovechar las oportunidades, pero Tezuka tiene tan solo dieciocho. Ella tendrá tiempo y sus habilidades madurarán."

show nomiya veryhappy
with charachange

no "Dicho eso, hay muchas ventajas en darse a conocer a una edad temprana, de ser posible."

show rin basic_absent_close
with charachange

hi "Sí, pero…"


label es_R11c:


hi "Quiero decir, el maestro posiblemente esté en lo correcto. No vas a tener una oportunidad como esta de nuevo."

hi "La gente no tiene muchas oportunidades en la vida, y no deberías de desperdiciar ninguna de ellas, aun si tienes dudas."

show rin basic_absent_close
with charachange

"Rin se queda mirándome con indiferencia. Es como si mis palabras no tuviesen sentido en absoluto para ella."



label es_R11d:


hi "¿No piensas que sería emocionante? Yo estaría eufórico con algo como esto."

show nomiya talk
with charachange

no "Jajaja, yo también. Pero esto es sobre cosas como tu carrera y tu futuro, en lugar de una aventura juvenil. Sin embargo no tiene nada de malo el disfrutarlo."

"Nomiya reprende suavemente mi emoción, pero no voy a dejar que el tema se me vaya."

hi "En serio, la vida cotidiana es tan aburrida, siempre haces lo mismo todos los días, de la misma manera. Esto sería algo diferente."



label es_R11e:


hi "Esto no es típico de ti. Tú me dijiste que la gente debería de hacer cosas que no pueden hacer, solo porque pueden."


hi "Y ahora tú misma estás vacilando ante algo tan importante."



label es_R11f:


hi "Realmente pienso que deberías de apuntar más alto. Deberías tomar la oportunidad."

hi "Aun si fracasas rotundamente, por lo menos lo intentaste. Valdría la pena solo por eso."

"Nomiya traga aire y luego lo deja salir después de una pausa, como si quisiera agregar algo, pero logra contenerse. Rin finalmente me responde."

show rin basic_surprised_close
with charachange


rin "¿Crees que así no soy lo suficientemente buena?"

hi "No. Creo que te estás subestimando si piensas de ese modo. Es cobardía."


label es_R11g:


show rin basic_deadpanupset_close
show nomiya smile
with charachange


"Rin me mira distraída, sin decir nada. No tengo ni idea de si mis palabras tuvieron algún efecto en ella."

hi "Simplemente no lo entiendo. Cualquier otra persona estaría brincando de la emoción."

hi "¿Qué importancia tiene hacer tu mejor esfuerzo y estar en este club de arte, si no haces nada con tu talento?"

hi "Te lo digo, voy a estar muy enojado contigo si renuncias a esto."

"Mi voz se levanta aún más alto. No sé qué es lo que me hace decir esto. Es como si alguna fuerza fuera de mi control se hubiese apoderado de mí, pero realmente estoy enojado."

"Imágenes de una carta escrita en un lindo papel destellan en mi mente, imágenes de los rostros enmascarados de mis padres, mis doctores, imágenes del tiempo que he desperdiciado."
"Estas se mezclan con mis sentimientos sobre Rin como un torrente de hierro fundido."

show rin basic_deadpanupset_close at tworight
with charamove

"Quiero continuar, pero Rin repentinamente se pone de pie."

rin "Está bien."

rin "Me voy."

hide rin
with charaexit

"Ella trota hacia afuera del salón sin que nadie diga nada. La miro irse, todavía furioso, aunque con la voz de la razón en mi interior preguntándose si también la hice enojar."

show nomiya veryhappy at center
show bg school_classroomart at bgright
with dissolvecharamove

"El maestro deja salir una avergonzada, pero extraordinariamente fuerte risa."

show nomiya frown
with charachange

no "Te preocupas mucho por ella, ¿no?"



label es_R11h:


show rin basic_deadpanupset_close
show nomiya smile
with charachange

rin "No creo que quiera hablar de esto."

rin "Me voy."

show rin basic_deadpanupset_close at tworight
with charamove

hide rin
with charaexit

"Rin se pone de pie y trota hacia afuera del salón sin que nadie diga nada más."

show nomiya smile at center
show bg school_classroomart at bgright
with charamove

hi "Lo siento. Creo que la hice enojar."

show nomiya veryhappy
with charachange

no "Jajaja, no te preocupes por eso. Ella estará bien, estoy seguro. Hablaré con ella más tarde."



label es_R11i:


show nomiya smile
with charachange

no "Ya ya, mi niño. Es una gran decisión y aunque también quisiera que Tezuka fuera más decidida, necesita tiempo para reflexionar sobre ello."

show nomiya frown
with charachange

no "¿Por qué no la dejamos elegir? Tienes buenas intenciones, pero al final todo se reduce a sus sentimientos."

show nomiya veryhappy
with charachange

no "¿Alguna opinión del tema, Tezuka? Has estado callada toda la tarde."

"Ambos vemos a Rin, quien no devuelve ninguna de nuestras miradas."

show rin basic_lucid_close
with charachange

rin "No. Creo que me voy."

show nomiya talk
with charachange

no "¿Te vas? Qué lástima. Prométeme que me darás algún tipo de respuesta en más o menos una semana, ¿está bien?"

show rin basic_deadpanupset_close
with charachange

rin "Está bien."

show nomiya smile
with charachange

no "Buena chica."

show rin basic_deadpanupset_close at tworight
with charamove

hide rin
with charaexit

"Rin se pone de pie y trota hacia afuera del salón sin que nadie diga nada más."

show nomiya smile at center
show bg school_classroomart at bgright
with charamove


label es_R11j:


"Nomiya me mira por encima de sus rosados anteojos circulares, sonriendo con simpatía."

show nomiya talk
with charachange

no "¿Te has hecho amigo de ella, entonces, Nakai?"

hi "Ah… bueno, algo por el estilo, supongo. Depende de cómo se le vea. Para ser honesto, realmente no estoy seguro."

"Es más como si Rin y yo solo tendiéramos a pasar el rato alrededor uno del otro de modo irregular, hablando o no sobre algo que a menudo parece una retorcida burla de la filosofía, en lugar de una charla cotidiana y normal que “amigos” tendrían."

show nomiya frown
with charachange

no "Bueno, eso está muy bien, ¿no es así? Eres un estudiante nuevo y deberíamos estar impulsando la integración al cuerpo estudiantil y esas cosas."
no "No puedo recordar todas las palabras de moda que escupen en la facultad y en las reuniones de la Fundación Yamaku, pero así son las cosas."

show nomiya veryhappy
with charachange

no "Tezuka tampoco es la persona más social por estos lados."

hi "Sí, eso es cierto, definitivamente."

show nomiya smile
with charachange

no "Entonces, ¿ha hablado ella de mi sugerencia contigo?"

hi "Oh, no, no realmente. Creo que ha sido más yo presionándola para que decida algo. Quizás no debería haberlo hecho."

show nomiya talk
with charachange

no "No, estoy seguro de que está bien. Soy demasiado blando con ella, aun si no debiera. En verdad no sé cómo tratar con Tezuka, ella es tan independiente y obstinada."

show nomiya talktongue
with charachange

no "Me pregunto si así es como todo viejo maestro de arte, que tuvo en sus manos a un joven y temperamental prodigio, se sintió."

show nomiya smile
with charachange

"Ríe un poco hacia sus adentros con ironía, volteando a ver la obra más reciente que Rin dejó secándose en el caballete. Ella partió tan abruptamente que hace preguntarme si la considera finalmente terminada."

show nomiya talk
with charachange

no "Y bien, veamos la pintura entonces."

"Se inclina hacia la pintura, mirando el lienzo."

show nomiya frown_close
with characlose

no "Te atrae, ¿no es así?"

show nomiya dreamy
with charadistant



"Nomiya endereza la espalda, en el rostro una expresión soñadora, nostálgica. No le respondo, ya que parece tomar como un hecho el que esté de acuerdo."

show nomiya talk
with charachange



no "Algunas veces me quedo aquí después de tarde solamente para ver las pinturas de Tezuka. Ella es simplemente una prodigio verdadera, y en una edad tan joven."
no "Me dan escalofríos solo de pensar en qué podría convertirse con unos cuantos años más de refinamiento."

show nomiya frown
with charachange

no "Tú preguntaste qué hace a un artista, ¿recuerdas? Es esto. Ellos toman un pedazo del mundo y lo remodelan a su propia imagen. Metafóricamente, claro."

show nomiya dreamy
with charachange

no "Verla hace que te preguntes cómo se ve el mundo a través de sus ojos. Es algo maravilloso, ser joven y tan apasionado, el momento más extraordinario de tu vida. Harías bien en recordarlo, Nakai."

hi "Sí, señor."

show nomiya veryhappy
with charachange

no "Es tan tonto."

show nomiya frown
with charachange

no "La gente siempre le pregunta a los artistas “¿De dónde sacas tus ideas?” como si las ideas fueran algo en venta en el mercado por unas monedas."

show nomiya serious
with charachange

no "No puedes explicar la inspiración. Para la gente como Tezuka, es como respirar. Es un instinto."

no "He conocido tal vez uno o dos con el mismo tipo de potencial en bruto. Pero ninguna cantidad de potencial llegará a nada si uno no trabaja para realizarlo."

no "Es práctica, técnica, habilidad. Dibuja por una hora todos los días por unos cuantos años e incluso el caso más perdido se convierte en un artista aceptable."

show nomiya talk
with charachange

no "Tezuka no es brillante porque nació con talento natural para esta clase de cosas. Ella es brillante porque trabaja más duro que los demás, desde que aprendió a sostener una pluma, seguramente."

show nomiya veryhappy
with charachange

no "Todo eso con los pies, nada menos. Absolutamente fenomenal."

"El silencio finalmente aterriza en el salón del club mientras Nomiya se deja atraer de vuelta hacia la pintura de Rin, murmurando suavemente una aprobación hacia el todavía húmedo lienzo."

hi "¿Qué tipo de cosas pinta usted?"

show nomiya smile
with charachange

"Como si despertara de un ensueño, me mira sorprendido de que le hable."

show nomiya talk
with charachange

no "Oh, no lo hago. Ya no más."

show nomiya smile
with charachange

no "Me convertí en maestro de arte solo después de que mi carrera en ese campo llegara a su fin. Ahora tan solo paso conocimiento a la siguiente generación."

"La manera en la que Nomiya responde es curiosa, a la vez dando y reteniendo información. Tengo ganas de preguntar más, pero él habla antes de que tenga la oportunidad."

show nomiya veryhappy
with charachange

no "Deberías de irte ya, mi niño. Es casi la hora de la cena, ¿no es así?"

hi "Sí, señor. Que tenga buenas noches."

show nomiya smile
with charachange

no "Tú también."

scene bg school_hallway3
with locationchange

stop music fadeout 2.0

"Rápidamente recojo mis cosas y salgo hacia el pasillo desierto, dejando al maestro a solas con sus pensamientos."

"El fin de semana llegará pronto. Es sorprendente cuán rápido el tiempo vuela aquí."

"Le prometí a Emi que me le uniría para la celebración de su triunfo en la competencia de atletismo la semana pasada. Eso debería de ser un montón de diversión."

scene black
with dissolve



label es_R12:


$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_daily fadein 3.0

scene bg school_courtyard_rn
with locationchange

hi "¿Estás segura de que quieres ir?"

"El tiempo que ha sido maravilloso por todo junio finalmente ha dado un giro para lo peor. Las nubes plomizas colgando sobre el pueblo se ven preocupantes y el cielo se siente pesado y estancado, justo como antes de llover."

"El pronóstico dijo que hay una probabilidad del 60%% de que llueva esta tarde. Quizás esto marque el inicio de la temporada de lluvia."

show emi basic_grin_rn at center
with charaenter

emi "¡Claro que estoy segura! ¡He estado esperando esto toda la semana!"

"Emi había planeado un picnic en algún parque cercano, con bocadillos en abundancia comprados en el minisúper, pero con el tiempo así de gris, parece riesgoso."

show emi basic_annoyed_rn
with charachange

emi "Le había pedido a otras personas que vinieran, pero no quisieron ir por el tiempo. ¡Tenemos que demostrar que estaban equivocados!"

hi "¿Cómo equivocados?"

show emi excited_smile_rn
with charachange

emi "Tú sabes, así como cuando siempre llueve cuando piensas que no va a llover, y luego piensas que lloverá, ¿no es así? Iremos sin importar qué, ¡así que es una situación donde ganamos o ganamos!"

show emi basic_closedhappy_rn
with charachange


emi "No he comido dulces por semanas a causa de las prácticas para la competencia de atletismo. Pero ahora puedo derrochar todo lo que me dé la gana. ¡Nada me va a detener ahora!"

hi "Pensé que en verdad te importaba lo de un estilo de vida saludable y esas cosas."

show emi excited_proud_rn
with charachange

emi "Ojojo, Hisao, entiendes tan poco. ¡No hay una sola chica en este planeta a la que no le gusten los dulces!"

show emi excited_proud_rn at twoleft
show bg school_courtyard_rn at bgleft
with charamove

show rin basic_deadpan_rn at tworight
with charaenter

rin "A mí no me gustan los dulces."

show emi excited_joy_rn
show rin basic_awayabsent_rn
with charachange

emi "Ella no cuenta. En fin, ¿está claro?"

show rin basic_absent_rn
with charachange

hi "Completamente. Iremos y comeremos dulces hasta llenarnos."

show emi basic_closedgrin_rn
show rin basic_awayabsent_rn
with charachange


emi "Por supuesto que lo haremos, ¡carajo!"

show emi excited_laugh_rn
with charachange

emi "Tendré que bajarlo después pero vale tanto la pena."

"Emi parece estar extremadamente resuelta a esto. Ella está verdaderamente entusiasmada, llena de energía como siempre, pero algo parece ser especial el día de hoy."


"Parece que apenas puede evitar saltar de arriba a abajo, dondequiera que esté."

show emi excited_joy_rn
with charachange

emi "¡Vamos!"

hide emi
hide rin
with charaexit

"Sujeto el mango de madera del paraguas que traje y comienzo a seguir a las dos chicas, que parecen no tener problemas con dejarme atrás si sigo soñando despierto."

"Mi paraguas es realmente suntuoso, del tipo que está hecho a la antigua con mango curvado y punta de metal en el extremo. Solía pertenecer a mi abuelo. Parece una antigüedad, pero está en muy buenas condiciones. Casi como nuevo."

"Es bastante grande, también. Recuerdo cómo mi abuelo, mi abuela y yo cabíamos cómodamente bajo él cuando una tormenta nos alcanzó en un paseo por la tarde hace años, cuando tenía alrededor de nueve o diez años."

"Mis dos abuelos ya se han ido, pero todavía tengo el paraguas para mantenerme seco cuando llueve."

scene bg school_road_rn
with locationskip

"Caminamos por la calle que lleva de la escuela al minisúper, las nubes arrojando su sombra sobre nosotros. El tiempo parece estar empeorando y estoy muy seguro de que acabo de sentir una gota de lluvia en mi cabeza."

hi "¿Qué acaso no pensaron en traer paraguas? En serio parece que va a llover."

show rin basic_deadpancontemplation_rn at tworight
show emi basic_grin_rn at twoleft
with charaenter

"Rin mira sus mangas colgar y se encoge de hombros."

show emi basic_closedgrin_rn
show rin basic_awayabsent_rn
with charachange

emi "No tengo uno. Además, un poco de lluvia no nos matará."

"Ella saca el pecho, viéndose muy confiada en ello."

show emi basic_happy_rn
with charachange

emi "¡No estamos hechos de azúcar!"

show rin basic_absent_rn
with charachange

hi "Pensé que eso era exactamente de lo que estaban hechas las chicas, sobre todo considerando con lo que planeas atiborrarte hoy."

show emi sad_annoyed_rn
with charachange

"Ella simplemente saca la lengua como respuesta."

hide emi
hide rin
with charaexit

"El camino de la escuela al distrito comercial no es largo, pero tampoco es muy corto. Es todo cuesta abajo así que nos movemos con facilidad, pero el tiempo se extiende, no obstante."

"La distancia está justo en ese punto, en esa región gris donde no esperas que el viaje termine pronto, pero tampoco te preparas para una larga caminata."

"Por tanto, el viaje es ligeramente demasiado largo como para quedarse callados todo el tiempo con comodidad, aunque a las chicas parece no molestarles."

"Rin camina tranquilamente por delante, aparentemente perdida en sus pensamientos. Estoy un poco preocupado de empezar una conversación, ya que la última vez no terminó muy bien para ninguno de los dos."

"No he intercambiado una sola palabra con ella desde entonces."

"Emi, por otra parte, está demasiado contenta con tan solo caminar."


"Ella parece estar literalmente brincando un poco en cada paso, o saltando sobre grietas, o balanceándose en el borde de la acera."
"Cada tanto, comenta sobre algo a lo cual Rin responde de un modo que suena automático y sin sentido, haciendo reír un poco a Emi."

$ renpy.music.set_volume(0.1, 0.0, channel="ambient")
play ambient sfx_rain fadein 5.0

scene bg suburb_roadcenter_rn
with locationchange

"A medida que llegamos al pie de la colina, las primeras gotas de lluvia comienzan a caer. Siento una caer sobre mi cabeza, luego dos más caen en mi nariz en una rápida sucesión."

play sound sfx_thunder
stop music

$ renpy.music.set_volume(0.2, 0.5, channel="ambient")
$ renpy.music.set_volume(1.0, 4.0, channel="music")
show rain light
with dissolve

"Ya no es una ni dos nubes de lluvia. El cielo entero se ha tornado un gris lúgubre, nubes henchidas se arremolinan justo sobre nosotros."

show emi sad_pout_rn behind rain at center
with charaenter

emi "Oh, rayos. Supongo que no vamos a tener un picnic, después de todo."

hi "¿Qué dices?"

show emi sad_pout_rn at twoleft
show bg suburb_roadcenter_rn at bgleft
with charamove

show rin negative_spaciness_rn behind rain at tworight
with charaenter

rin "Tal vez podríamos tener un picnic de lluvia. Un picnic en la lluvia."

show emi basic_annoyed_rn
with charachange

emi "No, solo terminaríamos pescando un resfriado y a mí no me gusta mojarme o que se mojen mis bocadillos."

show rin relaxed_nonchalant_rn
with charachange

rin "A mí me gusta. Aunque no lo de los bocadillos."

$ renpy.music.set_volume(0.5, 4.0, channel="ambient")

show emi basic_concentrate_rn
show rain medium
with charachange
play sound sfx_rustling

"Emi considera nuestra situación problemática por un momento mientras yo abro mi paraguas y lo levanto, tratando de sostenerlo de modo que los tres estemos cubiertos."

show emi basic_happy_rn
with charachange

emi "Oye Hisao, ¿ya has ido al Shanghái?"

show rin basic_absent_rn
with charachange


label es_R12a:

hi "Es un café en algún lugar de por aquí, ¿cierto? He escuchado de él."


label es_R12b:

hi "Sí, nuestra presidenta de grupo me llevó ahí en mi primera semana."


label es_R12c:

show rin basic_awayabsent_rn
show emi basic_grin_rn
with charachange

emi "Es un lugar agradable. Vamos allá y esperemos a que pase la lluvia. Si es solo una llovizna rápida, podemos todavía ir de picnic, y si se pone peor, simplemente pediremos pastel ahí."

show rin basic_absent_rn
with charachange

hide emi
with charaexit

hide rin
with charaexit

"Ni Rin ni yo tenemos mejores ideas, así que con Emi tomando la delantera, comenzamos a caminar con prisa por una calle aledaña."

$ renpy.music.set_volume(1.0, 6.0, channel="ambient")

scene bg suburb_shanghaiext_rn
show rain normal
with locationchange

"El café está a tan solo unas cuadras más adelante, pero incluso con el paraguas, no podemos evitar mojarnos un poco. La lluvia sigue cayendo más y más fuerte."

"Gotas de lluvia dejan pequeñas manchas negras en la calle de asfalto, las cuales luego se combinan en parches más grandes, como arte puntillista siendo creado frente a mis ojos en cuestión de segundos."


"Está lloviendo a raudales. El agua tamborilea en los capós de los autos estacionados a los lados de la calle y ya fluyen pequeños arroyos por las aceras."

"La luz amarilla brillando a través del agua de lluvia corriendo por las ventanas se ve muy cálida y tentadora."

play sound sfx_storebell
stop ambient fadeout 0.5
play music music_jazz fadein 2.0

scene bg suburb_shanghaiint at left
with locationchange

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0

"Sacudo el exceso de agua del paraguas y me dirijo hacia adentro con ellas, siguiendo a Emi a una mesa vacía en el rincón más apartado del pequeño café."

$ renpy.music.set_volume(0.7, 2.0, channel="ambient")

"El lugar está casi lleno; aparentemente otra gente ha tenido la misma idea que Emi, y ahora estamos todos juntos varados en este pequeño y acogedor lugar."

scene bg suburb_shanghaiint at Fullpan(5.0)
with None

"Pilares de madera barnizada y pantallas de papel se mezclan con mesas y sillas de estilo parisino en una armonía discordante, un contraste de lo viejo y lo nuevo."

"Jazz ligero suena con suavidad de fondo, sin embargo es ahogado casi por completo por el murmullo de los clientes."


label es_R12d:

"Solo hay una mesera sirviéndole a la casa llena, frenéticamente deslizándose de una mesa a otra y tratando de mantener el ritmo con todo. Para mi sorpresa, creo que la reconozco."

"La veo llevar una bandeja con tazas de té y pastelillos a otra mesa ocupada por estudiantes de Yamaku, luego tomar una orden de una pareja de mediana edad sentada frente a nosotros, antes de finalmente voltearse para servirnos a nosotros."

hi "¿Yuuko?"

show yuukoshang neurotic_up at Slide(0.6,0.5,0.5,0.5,0.5)
show bg suburb_shanghaiint at right
with charaenter

"Ahora que está cerca y frente a mí, veo que realmente es ella; la bibliotecaria de medio tiempo en Yamaku, con vestimenta de mesera. Es un atuendo muy lindo, y se ha recogido el cabello en chongos para combinar."

show yuukoshang worried_up at center
with charachange

"Es una imagen completamente diferente de su estilo tímido y simple en su otro trabajo. Yuuko parpadea un par de veces viéndose confundida, entonces recuerda que estaba a punto de decir algo."

show yuukoshang panic_down
with charachange

yu "Ehh… ah, bienvenidos al Shanghái."

hi "¿Así que trabajas aquí también? Pensé que eras estudiante universitaria o algo así."

show yuukoshang neurotic_down
with charachange

yu "Ehh, sí, eso también. Es un trabajo de medio tiempo como puedes ver, ejeje. Es domingo, así que no hay clases."

show yuukoshang neutral_down
with charachange


yu "Es algo bueno, además, ya que este día ha estado tan atareado que desearía tener otro par de manos. Bien, bueno, tengo un poco de prisa como pueden ver. ¿Qué puedo traerles este día?"

label es_R12e:

"Me doy cuenta de que Yuuko está trabajando hoy, pero parece que está sirviéndole a la casa llena ella sola, frenéticamente deslizándose de una mesa a otra y tratando de mantener el ritmo con todo."

"La veo llevar una bandeja con tazas de té y pastelillos a otras mesas ocupadas por estudiantes de Yamaku, luego tomar una orden de una pareja de mediana edad sentada frente a nosotros antes de finalmente voltearse para servirnos a nosotros."

hi "Hola, Yuuko."

show yuukoshang neurotic_up at Slide(0.6,0.5,0.5,0.5,0.5)
with charaenter

yu "Ahh… eh, bienvenidos al Shanghái. "

hi "Parece que estás ocupada."

show yuukoshang neurotic_down at center
with charachange

yu "Ajaja, Estoy hasta el cuello. Desearía tener otro par de manos."

show yuukoshang neutral_down
with charachange


yu "¿Qué puedo hacer por ustedes el día de hoy?"

label es_R12f:

show emi excited_joy at Slide(-0.1,0.0,0.0,0.0,0.5)
show rin basic_awayabsent at Slide(1.05,1.0,0.95,1.0,0.5)
with charaenter

stop music fadeout 1.0
$ renpy.music.set_volume(0.4, 2.0, channel="ambient")

"Emi no duda ni un segundo. Sus ojos brillan como aquellos de un niño en una dulcería."

play music music_comedy fadein 1.0
show emi excited_amused at left
with charachange

emi "¡Té para todos! ¡Y pastel para mí!"

show yuukoshang smile_up
with charachange

"Yuuko trata de mantener la apariencia formal y profesional tanto como sea posible, sonriéndole alegremente a mi hambrienta compañera."

show yuukoshang smile_down
with charachange

yu "Ahh… sí, este día tenemos una selección de pastelillo de fresa, pastel en capas de frambuesa o tarta de limón con merengue."

show emi basic_happy
with charachange

emi "Fresa… ¡no, limón! ¡No, de hecho escojo los dos!"

"Ella me mira desafiantemente."


hi "Ehh… Ordenaré la tarta, solamente."

show rin basic_deadpan at Position(xalign=1.0, xpos=0.95)
with charachange

rin "Nada."

show emi basic_annoyed
with charachange

"Emi le hace una cara a Rin como si hubiese mordido un limón. Ella está claramente descontenta con Rin por no unirse."

emi "Oh vamos, Rin. Eso es de muy mala educación."

show rin relaxed_boredom
with charachange

rin "Nada, gracias."

show emi basic_confused
with charachange

emi "¡No, no, tontita! Quise decir que deberías de pedir algo también."

show rin negative_spaciness
with charachange

rin "Tomaré una pajilla, entonces. Mis pies están todos mojados."

show yuukoshang worried_up
with charachange

yu "¿Disculpa?"

show rin basic_awayabsent
with charachange

rin "Del tipo que es para beber. Una, por favor."

show yuukoshang worried_down
with charachange

"Yuuko obviamente no sabe qué pensar sobre esto. Así que juega con su pluma y papel por un momento, viéndose como si estuviera a punto de llorar, antes de decidir que hemos terminado de ordenar."

show yuukoshang neurotic_up
with charachange

yu "¡Muchas gracias!"

show yuukoshang neurotic_down at Transform(ypos=1.25)
with Dissolvemove(0.2)

with Pause(0.3)

show yuukoshang neurotic_down at center
with charamove

hide yuukoshang
with charaexit

show emi basic_grin at twoleft
show rin basic_awayabsent at tworight
with dissolvecharamove

$ renpy.music.set_volume(0.7, 2.0, channel="ambient")

"Ella hace una reverencia y se inclina un poco de más y corre deprisa a la seguridad detrás del mostrador."

"Después de que termina ese calvario, tengo oportunidad para relajarme y darle una mejor mirada a los alrededores."

"Casi todas las mesas están ocupadas por gente feliz de estar fuera de la lluvia, bebiendo agradecidos su té mientras esperan a secarse."

"Fragmentos de quejas sobre el mal tiempo o discusiones acerca de tareas recientes, llegan a mis oídos desde mesas cercanas. Una se sobrepone a la otra, pero todas son cubiertas por el sonido de la lluvia cayendo."

show emi basic_grin at left
show rin basic_awayabsent at Position(xpos=0.95, xalign=1.0)
with charamove

show yuukoshang smile_up at center
with charaenter

$ renpy.music.set_volume(0.4, 2.0, channel="ambient")

"Después de un rato Yuuko regresa a nuestra mesa, cargando una bandeja con una tetera enorme, tres tazas, una rebanada de pastel y dos rebanadas de tarta."

show yuukoshang neurotic_up at centertremble
with charachange

with Pause(0.5)

show yuukoshang smile_down at Transform(ypos=1.25)
with Dissolvemove(0.2)
play sound sfx_pillow

with Pause(0.3)

show yuukoshang smile_down at center
with charamove

hide yuukoshang
with charaexit

show emi basic_grin at twoleft
show rin basic_awayabsent at tworight
with dissolvecharamove

$ renpy.music.set_volume(0.7, 2.0, channel="ambient")

"Ella azota la bandeja en nuestra diminuta mesa con un repiqueteo, casi mandando la tetera a punto de voltearse sobre el regazo de Rin."
"Apenas nos recuperamos antes de que ella haga otra reverencia y se marche, apresurándose a servir a los demás clientes."

"Emi ha estado ojeando muy hambrienta su pastel de fresa todo este tiempo, pero de algún modo logró contenerse hasta que Yuuko estuviera fuera de vista."

show emi excited_smile
with charachange

"Ella ataca con gran deleite, mientras yo me conformo con servirle té a todos y colocar la pajilla en la taza de Rin."

show rin basic_deadpansurprised
with charachange

"Rin mira el modo en el que el té se arremolina dando vueltas y vueltas en su taza de porcelana blanca con sus ojos a medio cerrar, casi como si estuviera siendo hipnotizada."

show shangpai:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"Tomo mi tenedor y le echo un ojo a la comida frente a mí. La tarta parece estar hecha a la perfección, una gruesa capa de merengue encima de espesa crema de limón."

"Después de darle la primera mordida, hago una pausa, saboreando la combinación de ácidos cítricos y merengue suave y azucarado. Es bastante bueno, aunque demasiado dulce para mí."

show emi excited_joy
show rin basic_deadpannormal
with None

show shangpai:
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide shangpai

emi "Effta mu güeno."

"Habla con la boca llena de pastel, ya a la mitad de su rebanada a pesar de que no es precisamente pequeña."

show emi basic_grin
with charachange

emi "Quiero probar un poco de eso."

play sound sfx_slide2

show emi excited_happy_close
show rin basic_absent
with characlose

show emi basic_closedgrin
show rin basic_awayabsent
with charachange

"Antes de que pueda responder, ella arremete contra mi deliciosa tarta, toma un pedazo con su tenedor y escapa con él."

show emi basic_closedhappy
with charachange

emi "Este está muy bueno."

hi "¿Qué estás haciendo? ¡Tienes una rebanada propia!"

show emi excited_proud
with charachange

emi "Sí, pero si empezaba con ese antes de terminar el pastel, sería de mala educación, ¿no lo crees?"

"Su insolencia es indignante, pero el caballero en mí no permite represalias."

show emi basic_grin
with charachange

"La miro con enojo y ella responde sacando la lengua traviesamente. Emi está más hiperactiva este día que de costumbre, pero no me molesta. Es bueno para ella que descargue sus energías."

"Tomo otro sorbo del té en mi taza. Está rico y caliente, aun si usualmente no me interesa mucho el té, y el ambiente en el café es bastante relajante."

"No me molesta pasar el resto de la tarde aquí, incluso después de que Emi ordena su segunda rebanada de pastel de fresa, y Rin pasa la mayoría del tiempo mirando fijamente la lluvia caer de los cielos."

show rain normal behind bg
with None

"Incluso Yuuko pone los ojos en blanco con el tercer pedazo de pastel, que desaparece en el estómago sin fondo de Emi tan rápido como los dos anteriores."

$ renpy.music.set_volume(1.0, 2.0, channel="ambient")
play ambient sfx_rain fadein 1.0

show bg suburb_shanghaiext_rn as bg2 behind rain
hide bg
hide rin
hide emi
with shorttimeskip


show bg suburb_shanghaiext_rn behind rain
hide bg2
with None

"Pese al paso del tiempo, todavía sigue lloviendo afuera cuando salimos del Shanghái, aunque parece estar amainando un poco."


hi "Lástima que tuvo que lloverle a tu fiesta."

show rin basic_awayabsent_rn behind rain at center
with charaenter

rin "¿No se suponía que íbamos a ir de picnic?"

show rin basic_awayabsent_rn at tworight
show bg suburb_shanghaiext_rn at bgright
with charamove

show emi basic_closedgrin_rn behind rain at twoleft
with charaenter

"Emi no parece muy desconsolada por este giro de eventos."

emi "¡Nah está bien! Nos la pasamos bien, ¿o no? Me siento llenísima de energías."

show emi basic_grin_rn
with charachange

emi "Ya ni siquiera está lloviendo tan fuerte. Como que tengo ganas de correr a la escuela para deshacerme de esta energía y bajar un poco de ese pastel."

"Estira los brazos y arquea la espalda como un gato. Después de girar sus hombros un par de veces, ella sonríe con alegría."

show emi sad_grin_rn
with charachange


emi "Vaya, aunque no puedo correr bien con estas piernas, especialmente cuesta arriba. Quisiera haber traído las otras."

"Ese concepto suena raro, dicho tan casualmente. Pero supongo que para Emi, el cambiar de piernas es un poco como para alguien más cambiar de zapatos."

show emi excited_proud_rn
with charachange

emi "Tal vez si camino muy rápido, eso será un poco como correr. Creo que haré eso."

show rin basic_absent_rn
with charachange

hi "Aunque no podré mantenerte el ritmo yendo cuesta arriba, en verdad estoy en mala forma. Además, te mojarás sin un paraguas."

show emi basic_grin_rn
show rin basic_awayabsent_rn
with charachange

emi "Ya apenas y es una llovizna. Unas cuantas gotas no me harán daño. Creo que iré a la pista después de que cambie de piernas, también."

"Emi salta fuera de la protección de mi paraguas y va hacia adelante con un paso rápido. De pronto parece recordar algo a medida que se detiene y se da vuelta."

show emi excited_smile_rn
with charachange

emi "¡Nos vemos mañana!"

show emi excited_proud_rn
with charachange

emi "¡Ven a almorzar con nosotras en la azotea! ¡Llevaré comida para tres!"

show emi invis at offscreenleft
show rin basic_absent_rn at center
show bg suburb_shanghaiext_rn at center
with dissolvecharamove

hide emi
with None

stop music fadeout 5.0


"Quedamos Rin y yo para verla despedirse con la mano y marcharse dando brincos otra vez. Pronto, ella desaparece a la vuelta de una esquina. Nunca entenderé por qué Emi está perpetuamente en tanto apuro para llegar a alguna parte."

hi "Así que, ¿quisieras que te acompañe de vuelta a la escuela, para que por lo menos una de ustedes no se moje?"

show rin basic_deadpan_rn
with charachange

rin "Si estás feliz con eso."

"Parece que ninguno de nosotros quiere mantener con vida el ambiente tenso de la discusión de hace unos días en el salón de arte, lo que me hace sentir aliviado. No quiero guardar rencores y estoy feliz de que Rin se sienta de la misma manera."

"Y así se decide que estamos conformes con la compañía del otro por ahora, y comenzamos a caminar en la misma dirección que Emi, aunque con un paso considerablemente más relajado."

hide rin
hide bg
show ev rin_rain_away_close behind rain:
    xalign 0.5 yalign 1.0 subpixel True
    acdc_warp 20.0 yalign 0.0
with whiteout
$ renpy.music.set_volume(0.7, 4.0, channel="ambient")

"Me le acerco un poco más a Rin, aun si el paraguas es lo suficientemente grande para resguardarnos a los dos. Puedo sentir su calidez cercana ofrecer un contraste con el frío de este tiempo lluvioso."


"Las gotas que golpean el paraguas hacen un sonido distintivo, tocando una melodía staccato de lluvia para nadie en especial."






"Me doy cuenta de que no he estado fuera en el agua en lo que se siente como una eternidad. Inhalo, apreciando el aroma de lluvia, sintiendo el clima con todos mis sentidos."

"El mundo se funde en una mancha dentro del aguacero."

"Los colores del cielo se han oscurecido de gris a un azul renegrido, con tonalidades de rojo añadidas a la mezcla de la luz del sol que se refleja en las nubes. El cielo bajo se ve bonito, como si pudiera extender la mano y tocarlo."

$ renpy.music.set_volume(0.5, 4.0, channel="ambient")

rin "¿Te he dicho cuánto me gusta la lluvia? Es como pintar. Me hace sentir conectada."

"Casi haciéndole eco a mis pensamientos, Rin deja salir uno de los suyos. Se escapa de su boca, circulando alrededor nuestro con suavidad."

rin "Todo se ve tan blando, como si los contornos de las cosas apenas desaparecieran. Me gusta eso."

rin "Es como si la lluvia me abrazara."

"Su voz suena diferente de lo usual; más gentil ahora, y suave. Me pregunto si es solo a causa de la lluvia, o a causa del estado de ánimo que la lluvia le trajo a la silenciosa chica artista."

show ev rin_rain_away_close behind rain at Position(xalign=0.5, yalign=0.0)
show ovl rin_rain_hisaotowards_close behind rain at Position(xalign=1.0, yalign=0.0)
with charachange

"También siento ese estado de ánimo en mí, acentuado por sus palabras."

hi "Sí. También me gustan los tiempos lluviosos. Es agradable, de vez en cuando."


hi "Me pregunto qué tiene de especial la lluvia."

show ev rin_rain_towards_close at Position(xalign=0.5, yalign=0.0)
hide ovl
with charachange

rin "Todo."

show ev rin_rain_towards:
    xalign 0.5 yalign 0.5 zoom 1.05 subpixel True
    ease 5.0 zoom 1.0
with locationchange

$ renpy.music.set_volume(0.35, 6.0, channel="ambient")

"Un silencio le sigue a esta declaración, ya que no permite continuación alguna. Decido dirigir el camino de la charla un poco."

hi "Pero sabes, si te gusta la sensación de estar conectada, ¿cuál es el problema con mostrar tus pinturas a los demás?"

hi "¿Acaso no quieres estar conectada con otras personas?"

show ev rin_rain_away at Position(zoom=1.0)
show ovl rin_rain_hisaotowards behind rain at Position(xalign=1.0, yalign=0.0)
with charachange

rin "No es lo mismo. Estás comparando manzanas y calamares."

"Traje a colación el tema que Rin quiere evitar, y eso la hace cerrarse de nuevo."
"La pregunta queda flotando entre nosotros por el resto del viaje de vuelta a la escuela, y no puedo evitar preguntarme qué rayos podría haber dicho para verdaderamente poder alcanzar a Rin."

"¿Acaso siente que le hace falta una identidad?"

"Ella tiene una personalidad fuerte, pero si fuese presionado para dar mayor explicación, no estoy seguro de que pudiera describirlo con exactitud."
"Se siente como una persona que estuviera en conflicto constante consigo misma. Nunca sé qué esperar cuando hablo con ella."

"Me pregunto cómo es que ella misma siente esa desconexión."

"Si Rin se está preguntando a sí misma cada día “¿Quién soy?”, y pinta obsesivamente imágenes para definirse a sí misma día tras día, ¿qué pensará ella de ese estilo de vida?"

hide ovl
with charachange

"La ironía es, que esa es exactamente la misma pregunta que me he estado haciendo a mí mismo los últimos cuatro o cinco meses. Para mí fue miserable. Tan solo puedo asumir que ese es el estado natural de ser para esta chica."

hide ev
show bg school_dormext_full_rn behind rain
show rin basic_awayabsent_close_rn behind rain at center
with shorttimeskip

$ renpy.music.set_volume(0.7, 1.0, channel="ambient")

"Cuando nos detenemos frente a los dormitorios Rin se vuelve para verme, como si percibiera mis pensamientos a lo lejos. Su mirada viaja vacía más allá de mi hombro hacia la lluvia sin forma."

"Sus ojos oscuros parecen absorber la luz ambiental hacia sí mismos, como un espejo invertido."

"Esa mirada vacía no deja salir nada. Si quiero comprender qué está ocurriendo detrás de esos ojos, tengo que entenderlo por mi cuenta."

"Rin abre su boca, luego la cierra sin decir nada. El silencio dura por unos momentos más antes de que tome un paso hacia la puerta del edificio de los dormitorios."

show rin basic_absent_rn
with charadistant

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

rin "Nos vemos mañana."

stop ambient fadeout 0.5

scene black
with dissolve





label es_R13:

scene bg school_dormhisao
with dissolve

"La mañana siguiente, como cada segundo lunes en la mañana hasta que él diga lo contrario, tengo una cita con el enfermero."


"Me permiten faltar a parte de la primera de mis clases matutinas, y tampoco siento nada de pena por faltar al resto."

"En vez de estar agradecido porque puedo perderme Historia Universal, siento pavor cuando pienso en estas citas."

scene bg school_dormbathroom
show steam
with locationchange

play ambient sfx_shower fadein 0.5


"Me despierto a la hora normal, de cualquier modo; y tomo una ducha en el baño que comparto con Kenji, arreglando mi cabello despeinado por la almohada."

"Me visto rápidamente y pongo mi ropa sucia en el cesto."

stop ambient fadeout 0.5
hide steam
scene bg school_dormhisao
with locationchange

"Guardo las cosas para el día de escuela. Tengo toda mi tarea hecha, como es usual, así que tengo un poco de tiempo libre ahora."


"No tiene sentido ir a la clase por 20 minutos antes de que tenga que ir a la oficina del enfermero, así que me acuesto en la cama y leo un libro hasta que es hora de irse."

scene black
with dissolve
scene bg school_nurseoffice
with locationskip

play sound sfx_doorknock2

"La puerta que da a la oficina del enfermero está abierta, lo que es inusual. Entro llamando a la puerta para anunciar mi llegada. Mirando por encima de la pantalla de su computadora, me hace señas para que tome asiento con un saludo amistoso."

"Vapor se desprende de una taza muy caliente de café en su escritorio. Probablemente no es su primera de este día."

play music music_nurse fadein 0.5
$ renpy.music.set_volume(1.0, 4.0, channel="ambient")

show nurse neutral at center
with charaenter

nk "¿Qué tal te sientes en esta maravillosa mañana, Hisao?"

hi "Estoy bien, creo. Estaba haciendo frío ayer a causa de la lluvia así que me desperté sintiéndome un poco mareado."

show nurse fabulous
with charachange

nk "Tú también, ¿eh? Bastantes muchachos fueron alcanzados sin paraguas, así que hemos pasado el tiempo repartiendo mascarillas y curando resfríos. Hmm… muy bien, hoy es día de exámenes. Dame tu brazo."

show nurse neutral_close
with characlose

"Extiendo mi brazo izquierdo hacia él, manteniendo mi rostro inexpresivo. El enfermero ata un torniquete de caucho alrededor de mi bíceps con un ya practicado movimiento, y rápidamente sigue con sus asuntos."

"No creo que a nadie realmente le guste que le claven agujas, pero por lo menos superé mi desagrado por ellas. Tuve que hacerlo. Ahora apenas y me estremezco al momento de la verdad."

"Una vez hecho eso, un chequeo de la presión sanguínea le sigue, luego son listas de control y cuestionarios por los que pasar. El enfermero asiente y garabatea mis respuestas a las preguntas a la vez que las doy."

show nurse grin_close
with charachange

nk "Muy bien. Vamos a escuchar, entonces."

show nurse neutral_close
with charachange
play sound sfx_rustling

"Desabotono mi camisa y la pongo con cuidado en el respaldo de la silla en la que estaba sentado, mientras él se pone su estetoscopio."

"Me sé de memoria el orden de los lugares donde va a escuchar mis pulmones y los latidos del corazón. Ajusto mi respiración para que sea regular y profunda sin que siquiera me digan. Ya se ha convertido en una rutina para ambos."

"Es gracioso, este es prácticamente el único momento en la vida de uno cuando realmente te concentras en respirar y nada más. Eso siempre lo he encontrado divertido."

"El enfermero levanta el estetoscopio tan frío como el acero de mi pecho y lo coloca unos centímetros más abajo, escuchando de nuevo. El contacto del metal me hace retroceder por reflejo, aun si lo estaba esperando."

show nurse concern_close
with charachange

"El enfermero frunce el ceño, pero no puedo discernir si es porque no está contento, o si está tratando de notar algo específico entre la compleja multitud de irregularidades en mis latidos."

hi "¿Hay algo mal?"


nk "Por favor no hables."

"Me callo y me pongo más ansioso. El enfermero es agradable, pero no puedo evitar que me desagraden estas revisiones obligatorias. Me pregunto si voy a terminar odiando todas las citas médicas de ahora en adelante, a causa de estas."

show nurse concern
with charadistant

"Él finalmente levanta la placa circular metálica de mi pecho, permitiéndome hablar otra vez."

show nurse grin
with charachange

nk "Todo parece estar bien. ¿Te estás sintiendo bien?"

hi "Supongo. Estuve fuera cuando estaba lloviendo, y sí, realmente me sentí un poco mal en esta mañana. Tal vez pesqué un resfriado."

show nurse fabulous
with charachange

nk "¿Estuviste con Emi? También ella se resfrió. Mi gente le dijo que se quedara en cama por un día o dos."

hi "¿En serio? Digo, estuve con ella, pero no sabía que se había enfermado."

"Supongo que fue una tontería después de todo, que ella saliera bajo la lluvia así."

show nurse neutral
with charachange

nk "Sí. Bueno, pongamos eso de lado. Todo parece estar en orden contigo, pero recuerda ser cuidadoso."

hi "Claro. En verdad no quiero volver al hospital."


"Él reconoce algo en mi voz —tal vez terror reprimido, no lo sé— y me echa un vistazo por encima de unos papeles que estaba viendo."

show nurse fabulous
with charachange

nk "Oye, no te preocupes. En esta etapa, tomaría un enorme vuelco en tu condición para rehospitalizarte."

"Realmente no me tranquiliza, pero quejarme de ello con él no haría alguna diferencia. Me retiro sin decir nada."

stop music fadeout 7.0

scene bg school_nursehall
with locationchange

"Caminando por el corredor del edificio auxiliar al edificio principal de la escuela, me encuentro una joven enfermera viniendo del otro lado. Me sonríe cuando pasamos uno al lado del otro."

scene bg school_lobby
with locationchange

$ renpy.music.set_volume(0.1, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 0.5

"El vestíbulo está vacío de gente. No es de sorprenderse, ya que todavía hay clases. Escucho sonidos ahogados de discusiones que vienen de atrás de las puertas de los salones del primer piso."

"Le echo una mirada a mi reloj. Tendría que apresurarme para llegar a mi salón a tiempo, y no me siento con ganas de ir a clase de todos modos, así que decido subir a la azotea y tener un descanso extralargo para comer."

"Emi prometió que traería algo para mí hoy, pero si está enferma eso posiblemente no va a suceder. No tengo hambre de todas formas, así que da igual."

play ambient sfx_rooftop fadein 0.5
$ renpy.music.set_volume(0.3, 0.5, channel="ambient")

scene bg school_staircase1
with locationchange

"Subir por las escaleras empinadas es extrañamente liberador, casi como perder peso. Siento satisfacción de que no me agota tanto como lo hizo la primera vez que vine aquí."

"Empujo para abrir la puerta chirriante en la cima y entro a la luz del sol."

play sound sfx_door_creak
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")
scene bg school_roof
with Fade(0.5, 0.1, 2.0, color="#FFF")

"La valla metálica proporciona una grandiosa vista a las copas de los árboles, hasta llegar a las más lejanas siluetas grises del centro del pueblo."

scene bg misc_sky:
    left
    subpixel True
    linear 40.0 right
with locationchange

"El clima lúgubre de ayer es solo una memoria ahora. El cielo azul plateado parece estar al alcance de la mano."

"Olvido por un momento que estoy de mal humor. La calidez del sol me empapa hasta los huesos, en su lugar haciéndome sentir somnoliento y perezoso."

scene bg school_roof
with shorttimeskip
play sound sfx_normalbell

"Las campanas suenan para la hora del almuerzo, dándome un sobresalto de vuelta a la realidad."

"Poco después, el patio debajo de mí cobra vida. Estudiantes salen en masa de las puertas del primer piso, con la intención de disfrutar del almuerzo en el patio y de los frondosos jardines en este clima perfecto."

"Cuando escucho la puerta que da a las escaleras abrirse, no me molesto en voltear para ver quién es."


"La intrusa comienza a venir hacia mí con pasos irregulares. La grava con la que está cubierta la azotea tañe y cruje debajo de sus pisadas."

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

scene bg misc_sky
with locationchange

"Los pasos se detienen a una corta distancia de mí, seguidos de un silencio. Miro hacia arriba, al brillante ojo del sol, absorbiendo su calor con todo mi cuerpo."

rin "¿Qué estás haciendo?"

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene bg school_roof
show rin basic_absent
with locationchange


"Me giro por cortesía ante sus primeras palabras, para contemplar la figura esbelta y desmañada de Rin Tezuka. Ella también se ve bastante como sí misma este día."
"Su cabello está quizás un poco más despeinado que de costumbre, como si se acabara de levantar de la cama."

"Ella está de pie, apoyando su peso sobre uno de sus pies, viéndome con ligera curiosidad como si fuese algo en el escaparate de una tienda."

hi "No sé. Perdiéndome en mis pensamientos, supongo."

hi "¿Qué hay de ti?"

show rin basic_deadpan
with charachange

rin "Emi prometió comida. Generalmente comemos aquí."

hi "Me temo que estarás decepcionada. Escuché que Emi se resfrió."

show rin relaxed_nonchalant
with charachange

rin "Oh. Supongo que eso tiene sentido. No estaba en el salón."

hi "Sin embargo, no es tan común pescar resfriados en junio. ¿Sí crees que haya ido a la pista a correr, como dijo? La lluvia simplemente continuó."

show rin basic_deadpanupset
with charachange

rin "Probablemente."

hi "¿En la lluvia?"

rin "En la lluvia."

"Eso suena un poco exagerado solo para mantener el régimen de entrenamiento. Aunque Emi es una cabeza dura, así que puedo imaginarla corriendo en el aguacero solo porque “tenía que hacerlo”."

hi "Bueno, eso es obviamente un exceso. Tal vez sea también la razón de que haya pescado ese resfriado."

hi "Pero supongo que eso es un poco genial."

show rin relaxed_boredom
with charachange

rin "Hablando de eso, tampoco me estoy sintiendo muy bien. Creo…"

stop ambient

show rin relaxed_sleepy
with vpunch

rin "¡ACHÚ!"

play music music_another fadein 4.0

"Rin estornuda bastante fuerte, siendo incapaz de impedirlo a tiempo. Ella estira su cuello hacia abajo para limpiarse la nariz en su hombro, así que; decidiendo que eso sería muy poco femenino, saco un pañuelo y lo acerco a su nariz."

show rin relaxed_sleepy_close
with characlose

hi "Ten. Salud."

show rin relaxed_doubt_close
with charachange

rin "Gdacias."

"Ella se suena la nariz y la froto suavemente con el pañuelo, limpiándola."

"Su nariz es realmente linda. Extrañamente es posible que sea la parte más femenina del rostro de Rin. Creo que me estoy sonrojando un poco, pero Rin no se da cuenta."

show rin basic_lucid_close
with charachange

rin "Gracias. Creo que está por darme algo, también. Como estaba diciendo."

hi "Espero que no."

show rin basic_awayabsent_close
with charachange


"Rin no parece estar muy molesta por lo de la comida, así que; a pesar de la falta del almuerzo provisto por Emi, nos quedamos en la azotea. Ella se acerca y se queda de pie a mi lado, junto a la valla, viendo la misma abstracta distancia que yo."

"Nadie parece venir acá a interrumpir esta tranquilidad, tampoco. Está callado y pacífico."

stop music fadeout 2.0
play ambient sfx_rooftop fadein 3.0

scene bg school_roof
with shorttimeskip

"¿Qué hace uno en la hora del almuerzo si no es que comer?"

"Resulta ser que, entre nosotros dos, no sabemos realmente. Por fortuna, pasar el tiempo es una actividad que se maneja a sí misma bastante bien."

"Aun si no hay conversación para llenar el silencio entre los segundos que pasan, sin actividades sin sentido como mirar las nubes con las cuales pasar los minutos entre el ahora y entonces, el tiempo sigue su marcha sin descanso."

"Sigo viendo la hora en mi reloj, luego decido que es tonto hacer eso. En su lugar, trato de aguantar tanto como sea posible antes de que lo vuelva a ver. Tal vez pueda aguantar por seis o siete minutos."

show rin basic_awayabsent_close at center
with charaenter

"Rin permanece en silencio, mirando la extensión celeste sobre nosotros sin hacer nada."

"Me pregunto por qué, en la mayoría de las veces, no hablamos mucho. Ella dijo que no le gusta hablar a causa de sus percibidas dificultades para expresarse a sí misma de manera apropiada."

"En cuanto a mí, creo que solo terminé cayendo en el hábito en el hospital, donde pasé un largo tiempo sin realmente hablar con alguien."

"La mayor parte del tiempo me siento cómodo con este ambiente silencioso. E incluso cuando tengo la sensación de que tengo que romperlo, siempre es tan difícil pensar en algo del qué hablar cuando se trata de Rin."


"Ella y yo estamos en frecuencias tan diferentes que no parece haber nada en terreno común."

hi "¿Qué es lo que te gusta tanto del cielo?"

show rin basic_deadpannormal_close
with charachange

"Ella se gira hacia mí, sus ojos oscuros y serios."

show rin basic_deadpan_close
with charachange


rin "El cielo es lo único que es perfecto."

show rin basic_awayabsent_close
with charachange

rin "Eso lo sé. Podrías decir que soy una experta en cielo si quisieras. Y lo soy aun si no quisieras. Una experta en cielo."


rin "Siempre es diferente, pero siempre es perfecto también cuando es diferente."

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

scene bg misc_sky at Fullpan (8.0)
with locationchange

"Sigo su vista hacia la ilimitada extensión azul, pensando en sus palabras."

hi "¿Alguna vez has querido ser algo diferente?"

rin "No sería tan malo ser el cielo."

hi "No, quiero decir, alguien diferente. Ir a una escuela normal como todos los demás, sin tener que preocuparte de las cosas…"

rin "¿Qué cosas?"

"Trato de encontrar las palabras correctas por un momento, pero no puedo lograr formar una oración con la que estaría cómodo al momento de usarla."

hi "Caray, realmente no puedo decirlo en voz alta."

rin "Intenta. No soy muy buena leyendo mentes."

stop ambient fadeout 0.5
scene bg school_roof
show rin basic_awayabsent_close
with locationchange

hi "¿No has querido no ser discapacitada?"

"Ella piensa en esto y luego sacude la cabeza, frunciendo el ceño."

show rin negative_annoyed_close
with charachange

rin "Esa es una pregunta difícil. No sé qué decir."

hi "Está bien si no dices nada."

hi "Por alguna razón, simplemente estoy tan insatisfecho con quién soy en este momento, que constantemente pienso en cosas como esa. Es muy difícil de admitir, pero así es."

"Honestamente, me siento aliviado al decírselo a alguien finalmente, incluso si solo es Rin."

show rin negative_confused_close
with charachange

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play music music_serene fadein 8.0

rin "Creo que quiero ser diferente, algunas veces. He estado tratando de cambiarme a mí misma últimamente, pero me asusta un poco, como caminar hacia atrás con los ojos cerrados."

show rin negative_worried_close
with charachange

rin "La parte difícil es saber adónde los dedos de tus pies no están apuntando. Quiero decir, direcciones."

show rin basic_sad_close
with charachange

rin "Aun si no hago nada, nunca permanecería igual."

show rin negative_spaciness_close
with charachange

rin "Es como mis viejas pinturas. Son diferentes de lo que pinto ahora, porque soy diferente, pero siguen siendo mis pinturas así que hay algo igual. Eso es realmente extraño."

show rin basic_lucid_close
with charachange

rin "Soy diferente cada día, pero sigo siendo yo cada día. Entonces, ¿quién soy?"

hi "¿Es eso un acertijo?"

show rin basic_deadpanupset_close
with charachange


rin "Si quieres que lo sea. Aunque no sé cuál es la respuesta correcta, así que tú tienes que pensar en una."

hi "Bueno, es el cielo, ¿no es así? Usando esa definición tuya de ahorita."

show rin basic_surprised_close
with charachange

"En verdad logro sorprenderla con eso. Quizá ya se había olvidado de ello."

show rin basic_deadpansurprised_close
with charachange

rin "¡Es cierto! Pero estaba pensando en mí misma cuando dije eso. Muy extraño."

show rin basic_lucid_close
with charachange

rin "¿Podría ser que realmente yo soy el cielo?"

hi "No creo que eso sea posible. Tu lógica está un poco equivocada en alguna parte."

show rin basic_awayabsent_close
with charachange

"Ella mira hacia abajo y se calla, puedo ver que rápidamente está repasando la deducción mentalmente, y se pone descontenta con el resultado al que finalmente llega."

show rin basic_deadpanupset_close
with charachange

rin "Sí, quizás no sea el cielo. Tendría sentido, la tengo difícil para saber qué tipo de persona soy."

hi "No eres la única."

show rin negative_spaciness_close
with charachange

rin "Es como si mi mente estuviera en algún otro lugar que el resto de mí."

hi "Debajo del agua."

show rin basic_awayabsent_close
with charachange

rin "Sí, me pregunto cómo llegó ahí."


"No tengo respuesta, así que un breve silencio cae entre nosotros. Paso a mirar de vuelta al cielo sobre nosotros."

$ renpy.music.set_volume(0.5, 2.0, channel="music")

window hide

scene bg misc_sky
with locationchange

nvl clear
nvl show dissolve

n "\n\nLa última vez que verdaderamente le presté tanta atención al cielo fue… supongo que debió haber sido en el hospital. Podía ver solo una delgada franja del cielo desde mi ventana en mi cuarto. Si caminaba hacia las ventanas y presionaba mi cara contra el vidrio frío, la franja se hacía más grande, pero no mucho."


n "Ese cielo me hizo sentir triste y solitario, un recuerdo del mundo en el otro lado. Me pregunto si también hay otro mundo más allá del cielo que vemos desde aquí, sobre la azotea de la escuela."

n "No puedo dejar de comparar la vida en Yamaku con mi hospitalización, pero en verdad debería. Ya no estoy allá."

n "El estrecho cielo de mi ventana en mi cuarto de hospital, las caras de los doctores, las caras de mis padres. Las paredes blanquecinas por todas partes. La carta de Iwanako, haciéndole eco a las palabras que nunca dijo. Son cosas del pasado, ahora."

n "Desearía poder olvidar todo hasta este momento y que el tiempo se detuviera por completo. Estaríamos únicamente yo, Rin, y el cielo, un descanso para almorzar eterno en esta azotea. Perfecto, inmutable e interminable."

$ renpy.music.set_volume(1.0, 2.0, channel="music")

nvl clear
nvl hide dissolve

window show

hi "No estoy seguro de si me gusta o si odio esta escuela."

rin "Podría haber ido a una escuela normal si hubiera querido, pero elegí venir aquí."

scene bg school_roof
show rin relaxed_nonchalant_close at center
with locationchange

hi "¿Por qué?"

show rin relaxed_doubt_close
with charachange

rin "Solo decidí que vendría. Casi como gelatina de melón o de ciruela."

hi "¿Piensas que fue una buena idea?"

hi "Quiero decir, hay un montón de cosas buenas sobre esta escuela, pero pienso que también hay algunas cosas malas."

show rin basic_lucid_close
with charachange

rin "Lo sé."

show rin basic_awayabsent_close
with charachange

rin "Yo colecciono gente, porque son interesantes. La gente aquí es realmente sorprendente. La mayoría. Pero no todos."

show rin negative_angry_close
with charachange

rin "Algunas personas no pueden soportarlo. Sufren demasiado. A veces se ponen muy mal, sabes. Sufren."

show rin basic_deadpanupset_close
with charachange

rin "¿Me pregunto si tú también eres así? Espero que no. No me gustan cosas así."


hi "Oye, no soy tu estudio de caso. Y no me voy a rendir y morirme ni nada de eso."

hi "De cualquier modo, quise decir que este lugar está demasiado alejado del mundo real."

show rin basic_surprised_close
with charachange

rin "¿Qué es el mundo real?"

hi "Todo lo que está allá afuera. Gente real, con vidas diarias normales que encajan entre ellas como un rompecabezas."

show rin relaxed_surprised_close
with charachange

rin "¿Tú no piensas que somos así? ¿Gente real?"

hi "Tal vez no lo somos. Bueno, no, sí lo somos. Solo quise decir que se siente como si fuéramos las piezas sobrantes."

show rin negative_annoyed_close
with charachange

"Rin piensa por un momento, sus ojos con forma de almendra se entrecierran a la vez que muerde su labio ligeramente, como un niño."

show rin basic_deadpansurprised_close
with charachange

rin "¿Es difícil ser discapacitado?"

"Su pregunta se gana una risa reseca de mi parte."

hi "Tú dime. Tú has estado en este asunto mucho más tiempo que yo."

show rin negative_annoyed_close
with charachange

"Ella piensa en eso por otro momento."

show rin basic_deadpancontemplation_close
with charachange

rin "En verdad no me siento tan discapacitada. Digo, hago casi todo de un modo diferente, pero no es tan difícil. Siempre puedo practicar."

show rin basic_deadpandelight_close
with charachange

rin "He comenzado a practicar cosas de comida este año. Creo que quisiera aprender a cocinar en una cocina real algún día."

hi "Eso es admirable, pero no creo que sea solo un estado mental."

show rin basic_lucid_close
with charachange

rin "Tal vez no para ti."


"No tengo un buen contraargumento para eso, así que concedo al quedarme callado. La situación me está confundiendo más y más."

"Yo sé qué es lo que quiero, pero no sé cómo conseguirlo. Rin parece creer que únicamente con voluntad puede transformarse a sí misma a la forma que necesita ser, pero no puede decidir entre si quiere ser un ave o una mariposa."

show rin basic_awayabsent_close
with charachange

rin "Creo que, después de todo, realmente tampoco estoy tan contenta con quien soy, pero eso no significa que me arrepiento de quién soy."

show rin relaxed_nonchalant_close
with charachange

stop music fadeout 0.5

rin "Eso es lo que está mal contigo, Hisao."

play sound sfx_rustling

scene bg school_roof_blurred
show rin basic_lucid_superclose at center
with characlose


"Apenas comienzo a procesar esa muy contundente afirmación antes de que Rin me abrace de pronto."

hi "¿Qué estás haciendo?"

"Nunca he sido abrazado por una chica sin brazos antes. Para ser honesto, realmente no se siente físicamente como un abrazo."
"La extraña manera en la que ella presiona su cuerpo contra el mío y la falta de brazos que me rodeen lo hace sentir como si se haya caído sobre mí."

"Pero la calidez de un abrazo verdadero sigue ahí, y así es como lo reconozco por lo que es."

show rin basic_deadpannormal_superclose
with charachange

play music music_comfort fadein 9.0

rin "Te estoy abrazando, Hisao."

hi "Lo sé, pero…"

show rin relaxed_doubt_superclose
with charachange

rin "¿Está mal? Pensé que esto era lo que se suponía que tenía que hacer."

show rin relaxed_sleepy_superclose
with charachange

rin "Realmente no estoy acostumbrada a este tipo de cosas. La primera vez que Emi me abrazó me sorprendí y la pateé en el estómago. Puedo patear muy fuerte así que ella no me ha estado abrazando demasiado después de eso."

hi "No está mal. Es solo que, no, soy solo yo… es un poco difícil para mí, de momento. Parezco no poder reaccionar de la manera apropiada ante nada."

show rin relaxed_surprised_superclose
with charachange

rin "¿En serio? ¿Así que es difícil ser discapacitado después de todo?"

"Supongo que me tiene acorralado. No tengo la energía para empezar a discutir en contra de eso, pero siento que tengo que sacarme algo."

hi "Bueno, yo… no, no es difícil. Creo que soy solo yo pensando de más."

hi "En verdad desearía no sentirme tan mal por mí mismo todo el tiempo."

"Me pregunto si siempre fui así de frágil o si me volví de este modo después del incidente. Nada había sacudido realmente mi mundo así antes, así que no hay manera de decirlo."

show rin basic_lucid_superclose
with charachange


"Rin presiona su mejilla sobre mí con fuerza. Puedo sentir el calor de su cuerpo cerca del mío."

"Su temperatura corporal se siente muy alta, como si hubiese absorbido la luz del sol dentro de sí misma y estuviera ahora compartiéndola conmigo. O quizás sea un estado natural para ella."


"Es lo más reconfortante que he sentido en un muy largo tiempo."

show rin basic_deadpan_superclose
with charachange

rin "Guau, tu corazón de verdad suena realmente extraño. Es como una orquesta de percusión ebria."

hi "Por favor no digas cosas como esa. Me hacen sentir muy incómodo."

"Me río de su comentario de todas formas, en un intento de aliviar la tensión. Suena un poco forzado."


hi "Vaya, siento que sea todo un desastre."

show rin basic_deadpannormal_superclose
with charachange

rin "Está bien. Es la mejor parte de ti."

hi "Oír eso no me hace sentir contento."

scene bg school_roof
show rin basic_deadpannormal_close at center
with charadistant

"Ella rompe el abrazo y se sienta. Un incómodo silencio cae sobre nosotros como una sábana; yo sintiéndome avergonzado de mí mismo y Rin tratando de arreglar su expresión a algo que a ella le agrade."

$ renpy.music.set_volume(0.5, 2.0, channel="music")

scene bg misc_sky
with locationchange

"Una última vez, miro hacia arriba."

hi "Esta azotea es realmente genial. Es como si estuviera un poco más cerca del cielo."

rin "Conozco un lugar mejor, pero no podemos ir en la hora del almuerzo. Puedo llevarte allá algún día, si quieres."

play sound sfx_warningbell

"Suenan las campanas para el inicio de las clases vespertinas y Rin se pone de pie para dirigirse hacia abajo. No me apresuro a alcanzarla, decido quedarme aquí arriba por tan solo un rato más."

$ renpy.music.set_volume(1.0, 2.0, channel="music")

scene bg school_roof
show rin basic_awayabsent at center
with locationchange

hi "Gracias por el abrazo."

show rin basic_lucid
with charachange

rin "Gracias por no patearme."

hide rin
with charaexit

"Después de que Rin se marcha, finalmente dejo correr las lágrimas por mis mejillas y lloro por mi condición por primera y única vez en mi vida."

"Luego me deshago de esa persona hueca acostada en la cama de hospital, para siempre."

stop music fadeout 2.0
scene black
with dissolve





label es_R14:

scene bg school_scienceroom
with locationchange

"Dos días después, me siento menos miserable. Incluso tomo una larga, vigorosa y saludable caminata como recomendó el enfermero, algo que había evitado y evadido con todo tipo de excusas anteriormente."

"Me siento más activo en clase también, para el deleite de nuestro maestro de ciencia/cabecera, el señor Mutou, con respuestas correctas y prontas."

"El descanso de este momento entre las dos clases de la mañana es demasiado corto para cualquier tipo de actividad significativa, pero demasiado largo para solo pasárselo sentado en el salón sin hacer nada."

play ambient sfx_crowd_indoors fadein 0.5

scene bg school_hallway3
show crowd
with locationchange

"Salir al pasillo no es por mucho mejor, pero flexionar mis músculos agarrotados es un mejor uso del tiempo que dejar que se agarroten más al quedarme sentado."

"La puerta al salón de clases contiguo se abre y los estudiantes del 3-4 emergen para llenar el ya semiatestado pasillo. Parece ser que su maestro los mantuvo dentro algunos minutos extra."

"Emi está entre ellos. Ella se percata de que la noté, lo cual casi me hace apartar la vista de reflejo."

play music music_emi fadein 0.5

show emi basic_closedgrin at center
with charaenter

"Sin embargo, no lo hago, y Emi me sonríe mientras felizmente salta hacia mí, pasando a los demás estudiantes."

"Emi se ve bastante enérgica, sin mostrar signo alguno de enfermedad. Parece que se recuperó del resfriado."

show emi basic_happy
with charachange

emi "¡Hola! ¡Buenos días!"


hi "Qué bueno que estés de vuelta. ¿Te sientes mejor?"

"Ella se ve bien para mí, pero aun así me siento obligado a preguntar."

show emi excited_laugh
with charachange

emi "¡Gracias! Y sí, me siento mejor. Solo era un resfriado, nada serio."

"Emi ríe con confianza, como para enfatizar su condición. Me pregunto por un momento qué se consideraría como serio según Emi."

"Aunque ella parece impaciente por dejar el tema de lado."

show emi excited_happy
with charachange

hi "¿Adónde vas?"

show emi basic_closedgrin
with charachange

emi "A la habitación de Rin para ver si ya está despierta."

hi "¿Oh? ¿Faltó a las clases de la mañana?"

show emi sad_grin
with charachange

"Una tímida sonrisa emerge en el rostro de Emi y se pone un poco nerviosa."

emi "Ehh… no exactamente. Parece que pescó el mismo resfriado que yo."

hi "Lo lamento mucho. Bueno, estuvo fuera en la lluvia el domingo con nosotros, después de todo. La vi el lunes y también se estaba sintiendo un poco mal entonces."

show emi basic_grin
with charachange

emi "Sí. Como sea, le pediré al enfermero un poco de medicina contra el resfriado para dársela si no se recupera pronto."

stop music fadeout 3.0

hide emi
with charaexit

"Ella se retira al dormitorio de chicas. Quiero ir con ella para desearle a Rin que se mejore. Quiero decirle que ahora yo también estoy mejor, pero no se siente apropiado."

"Un sentimiento sin especificar desvía mis pensamientos. De algún modo no puedo armarme de valor para ir allá. ¿Es esto por lo que Iwanako pasó cuando trató de decirme lo que sentía?"

stop ambient fadeout 2.0

scene black
with dissolve



label es_R15:

scene bg school_girlsdormhall
with locationchange

"Aunque me siento con más energía, todavía estoy dudando de ir para allá y hablar con Rin."

"No es sino hasta dos días después, el viernes, que finalmente reúno el valor suficiente para entrar al dormitorio de las chicas. Le pregunto a la primera persona que me encuentro adentro cómo llegar a la habitación de Rin."



play sound sfx_doorknock2


"Llamo a la puerta sin distintivos de Rin y espero."

$ renpy.music.set_volume(0.5, 0.0, channel="sound")
play sound sfx_rustling
$ renpy.music.set_volume(1.0, 10.0, channel="sound")

"Después de algunos segundos de silencio, oigo algo crujir dentro de la habitación. Comienzo a preguntarme si quizás debería haberle traído algo, como una lata de café caliente o algunas naranjas."
"Podría haberlas pelado por ella. Bueno, demasiado tarde."

"La puerta se abre sin hacer ruido —ya estaba sin seguro— y me encuentro mirando a Rin, quien me mira de vuelta."

"Parece que acaba de levantarse de la cama, con su cabello todo desarreglado."

show rinpan basic_deadpanamused at Slide(1.05,1.0,1.0,1.0,0.5)
with charaenter

"… y apenas vestida."

"…"

show rinpan basic_amused at right
with charachange

rin "Hooolaaaa."

play music music_rin fadein 0.5

"Hay una extraña sonrisa de apariencia estúpida en la cara de Rin. No estoy precisamente seguro por qué."

"Rin sonríe tan pocas veces que esta parece estar fuera de lugar todo el tiempo. Especialmente ahora, dado su estado parcialmente desvestido. Dicho estado me hace sentir extremadamente conflictuado sobre si esta fue o no una buena idea."

"Sus mejillas están ruborizadas, contrastando con el aspecto pálido y lechoso de una persona que no sale lo suficiente al sol. Su frente parece sudorosa, como si pudiera tener fiebre."

hi "Ah, hola."

show rinpan basic_absent
with charachange

"¿Ahora qué? No planeé nada más allá de esto, y Rin me está mirando otra vez con esos ojos de que está esperando algo de mí."

"Hay algo de esta situación que me da un presentimiento muy extraño. Sus ojos están aún más vacíos que de costumbre y ella parece tener dificultad para centrarlos en cualquier cosa."

"La falta de ropa es perturbadora, pero ya que ella misma parece no estar molesta, ¿por qué debería de estarlo yo?"

"No dejo de decirme eso a mí mismo."

hi "Ehh, pensé en visitarte ya que no has estado en el club de arte… y quería hablar contigo y desearte que te recuperes."

"Rin no muestra señal alguna de reconocer lo que acabo de decir, haciendo que me pregunte si de verdad entendió mis palabras, o si siquiera las escuchó."

"Tal vez es la fiebre lo que la hace estar atontada; ella podría haber estado durmiendo antes de que yo viniera."

show rinpan basic_deadpan
with charachange

rin "Está bien."

show rinpan basic_deadpan:
    easeout 0.5 alpha 0.0 xpos 1.05
with Pause(0.5)

hide rinpan
with None

"Ella se da media vuelta y se aleja de la puerta, caminando de regreso a la pequeña habitación. Desde la entrada puedo verla caminar hacia su cama y medio caerse, medio sentarse en el desordenado montón de sábanas."

"La puerta abierta parece ser más un obstáculo, en mi mente, del que lo era la puerta cerrada; pero como Rin no dice nada más, paso a través de esta y hacia su habitación."

scene bg school_dormrin
with locationchange

"Rin está en su cama recargándose contra la pared, dejando la única silla en la habitación para mí."

"Ella guarda silencio después de que me siento, así que, ¿puede que ella haya querido invitarme pero simplemente olvidó decirlo en voz alta? Una invitación implícita, por así decirlo."

show rinpan basic_deadpanamused at twoleft
with charaenter

rin "Muy emocionante. Nadie me había visitado antes."

"El quebranto del silencio lleva mi atención de la habitación a su residente, quien de momento parece estar en medio de un proceso mental muy profundo."









show rinpan basic_awayabsent
with charachange

rin "A decir verdad, eso no fue cierto. Sobre visitar. Pero Emi no cuenta aunque visite."

show rinpan basic_deadpan
with charachange

rin "Ella siempre me consiente demasiado. Creo que se está divirtiendo de más."

show rinpan basic_absent
with charachange

rin "Creo que he olvidado cómo ponerme un sostén yo sola."

"Ella mira a sus pechos, mareada."

show rinpan basic_surprised
with charachange

rin "La cual probablemente sea la razón de que no tenga uno puesto, ahora que lo pienso."

"No he podido evitar notar que la blusa de Rin también está desabotonada, pero trato de mantener mis ojos estrictamente puestos en los de ella."

"Es bastante evidente que ella no es una persona muy consciente de su cuerpo. Mi propio cuerpo, sin embargo, es bastante consciente del de ella en estos momentos."

show rinpan relaxed_sleepy
with charachange

rin "¡Ella vino a despertarme a las siete y media hoy!"

show rinpan relaxed_doubt
with charachange

rin "¿Puedes imaginarlo?"

"Ella hace una pausa por un momento y mira mi rostro estupefacto."

show rinpan basic_lucid
with charachange

rin "Pensándolo bien, probablemente puedas. No es como ese pez arcoíris invertido que traté de imaginar antes. Eso fue difícil."

hi "Bueno, sí, esa parece una hora bastante normal para despertarse, si quieres ir a clases en la mañana."

"Intento sonar lo más razonable que sea posible para contrarrestar el enojo irrazonable de Rin."

show rinpan basic_deadpanupset
with charachange

rin "Le dije que se fuera al diablo."

show rinpan relaxed_nonchalant
with charachange

rin "Ella me dio estos medicamentos y me dijo que me los tomara."

"Sigo sus ojos a la mesita de noche y luego al frasco de píldoras sobre esta."

show pills:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"Lo levanto y le doy vuelta para ver la etiqueta y así ver qué tipo de medicamento trajo Emi."

"Ingrediente activo… ¿codeína?"

show pills:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide pills
with None

hi "¿Te tomaste todas estas?"

show rinpan relaxed_surprised
with charachange

rin "No. Sí. He estado comiéndome algunas porque hay tantas. Parecen hacer esta cosa no tan mala."

show rinpan relaxed_sleepy
with charachange

rin "De hecho… creo que me estoy sintiendo muy bien."

"Su cabeza le cuelga de lado a lado, haciéndola parecer como si estuviera tratando de estirar los músculos del cuello o posiblemente desmayándose."

"¿Tomó varias de estas píldoras? ¿Puede ser eso seguro? Debe de tener cuando menos algunos efectos secundarios… los cuales me temo estoy presenciando en estos momentos."

show rinpan basic_deadpanupset
with charachange

rin "Me estoy sintiendo muy bien… estoy bien… solo con que alguien me quite este zumbido de la cabeza. No puedo pensar bien."

"La expresión molesta regresa al rostro de Rin."

show rinpan basic_upset
with charachange


rin "Es como muchos de esos insectos… o un insecto muy grande."

show rinpan basic_awayabsent
with charachange

rin "Con muchas alas. Muchos colores y todo."

show rinpan basic_absent
with charachange

rin "¿Cuál es la palabra para esos?"

show rinpan basic_deadpanamused
with charachange

rin "Oh, no importa. Ya la recordé. Es mariposas."

"Ella le sonríe levemente a su última observación. La corta pausa en su monólogo no es lo suficientemente larga como para que me atreva a decir algo que pudiera potencialmente, aunque improbable, rescatar esta discusión."

show rinpan basic_amused
with charachange

rin "Amo las mariposas. Son los mejores animales."

show rinpan basic_awayabsent
with charachange

rin "¿Viste alguna en tu camino para acá?"

show rinpan basic_deadpansurprised
with charachange

rin "Hisao."

"Ella pronuncia mi nombre sin darse cuenta, posiblemente para poner en claro que ahora se está dirigiendo a mí, en lugar de solo decir lo primero que se le viene a la mente a quienquiera que pueda estar escuchando."

"Esta extraña situación me ha dejado sin habla más o menos desde el momento en que Rin abrió la boca al principio. Ahora que ella misma parece no tener nada más que agregar, el silencio llena la pequeña habitación."

"Me hace echar un vistazo alrededor de nuevo, en un intento de encontrar algo de qué hablar."

"La habitación de Rin es tan pequeña como la mía. La gran ventana, que ocupa casi toda la pared más alejada de la puerta, abre al este justo como la mía."

"Se ve muy normal, lo cual me parece extraño. Esperaba algo más… diferente."

"Aproximadamente una docena de pinturas —la mayoría en el característico estilo abstracto de Rin— y algunos carteles de arte ocupan casi todo el espacio disponible en las paredes, pero esa es la única diferencia real entre su habitación y la mía."


"No es que sea precisamente ascética, pero tampoco se ve como lo que esperaría de la habitación de una chica."

"Un débil aroma a arte… de pintura y papel, flota en el aire. Es el mismo olor que tiene el salón de arte."

"Rin no está muy preocupada con ser ordenada, parece ser; todo lo que le pertenece parece estar puesto en varios montones alrededor de su habitación."

hi "Tu habitación se ve bien."

"Es una frase vacía que uno usa para llenar el espacio vacío en conversaciones, pero mi ingenio me está fallando bastante en este momento."

show rinpan relaxed_nonchalant
with charachange

rin "Sí. ¿Quieres que te muestre los lugares?"

"Ella mira hacia abajo, a su blusa a medio abrir, con curiosidad; sin querer haciéndome seguir su vista hacia sus pechos."

show rinpan relaxed_sleepy
with charachange

rin "Oh… creo que ya lo hice."

"Eso no lo puedo negar, sin importar lo mucho que intente actuar con propiedad."

show rinpan basic_absent
with charachange

rin "Es muy lindo que hayas venido a verme."

show rinpan basic_deadpancontemplation
with charachange


rin "Me hace sentir muy… ¿cuál es la palabra?… tú sabes, esa sobre cosas y demás."

show rinpan basic_lucid
with charachange

rin "Como sea, viniste."

"Los desvaríos de Rin me hacen recordar que de hecho vine aquí por una razón."

hi "Oye, sobre lo que hablamos el lunes. En la azotea, ¿recuerdas?"

stop music fadeout 4.0

show rinpan relaxed_surprised
with charachange

rin "¿Hmmm?"

"Rin no parece estar muy atenta en estos momentos, no es que normalmente lo sea. Sigo adelante y me lo saco del pecho, de cualquier manera."

hi "Solo quería decirte que seré mejor de ahora en adelante, supongo."

hi "Odio ser patético, así que decidí que no lo seré, ya no más."

hi "Creo que… eso es todo."

show rinpan relaxed_sleepy
with charachange

rin "Está bien. ¿No es eso bueno?"


"Las palabras borrosas fluyen fuera de sus labios con lentitud y sin control."

show rinpan relaxed_nonchalant
with charachange

rin "Estoy feliz por ti, creo. Eso es lo que creo."

show rinpan basic_deadpannormal
with charachange


rin "No deberías de verte tan triste todo el tiempo. Digo, verse triste está bien si no estás triste, pero te ves triste como si estuvieras triste."

show rinpan basic_deadpan
with charachange

rin "Eso no está bien."

show rinpan basic_awayabsent
with charachange

play music music_rin fadein 0.5

rin "¿Vas a ir a algún campo de entrenamiento donde hacen hombres de los niños? ¿O meditación en la cima de las montañas?"

hi "No, no lo creo."

show rinpan basic_absent
with charachange

rin "Oh. Supongo que eso también está bien."

"Las oraciones salen de su boca, y probablemente de su mente, una a la vez con pequeñas pausas entre cada una de ellas, haciendo sus galimatías difíciles de entender."

show rinpan relaxed_doubt
with charachange

rin "Solo pensé que parecía una buena idea. Tal vez no lo es."

"Rin termina con una línea más, pudiendo decir la última palabra por encima de sí misma, una impresionante demostración de lo que solo puedo describir como boxeo de sombra mental."


hi "Mientras estoy avergonzándome a mí mismo, vale más decirte que siento haberte dicho esas estupideces la semana pasada."

hi "Es asunto tuyo decidir qué es lo que vas a hacer."

show rinpan basic_absent
with charachange

"Ella parece no detectar mis palabras al principio, pero entonces la comprensión se enciende en sus ojos y mueve su cabeza de lado a lado de un modo que podría interpretarse de cualquier manera."

show rinpan basic_deadpancontemplation
with charachange

rin "Está bien."

show rinpan basic_lucid
with charachange

rin "Posiblemente yo también dije estupideces."

rin "Es solo que a veces es un poco difícil mantener mis pensamientos como me gustan."

show rinpan relaxed_nonchalant
with charachange

rin "No son muy derechos, al menos la mayoría del tiempo."

rin "No es que quiera tenerlos derechos… solo quisiera que por lo menos tuvieran alguna forma."

rin "Redondo también es bueno. Pero necesito más definición."

show rinpan relaxed_boredom
with charachange

rin "Mis pensamientos son muy desordenados."

show rinpan relaxed_sleepy
with charachange

rin "Desordenados."

show rinpan invis:
    ypos 1.1
with dissolvecharamove

play sound sfx_pillow

scene ev rin_high_frown
with locationchange





"Ella repite la palabra melancólicamente, luego se deja caer sobre su cama y acomoda su cabeza sobre la almohada, cerrando los ojos."

rin "Suficiente. Cansada. Deberías irte. Voy a dormir otra vez."

scene ev rin_high_oneeye
with locationchange

"Ella abre uno de sus ojos para mirarme."




rin "¿Eras tú a quien le gustaba ver chicas durmiendo? ¿O alguien más?"

rin "Tal vez había muchos de esos."

scene ev rin_high_frown
with locationchange

rin "No puedo recordar."




rin "Puedes quedarte si quieres."

hi "No no, me iré. Tengo que… hacer tarea, de todos modos."

stop music fadeout 2.0




scene bg school_dormrin
with locationchange

"Me levanto de la silla y doy un paso hacia la puerta."

rin "Espera."

"Su petición me detiene en seco, no es como si hubiera tenido la intención de salir corriendo de inmediato."

scene ev rin_high_grin
with locationchange






"Miro por sobre mi hombro a la chica recostada sobre su cama, de nuevo con la sonrisa más extraña en sus facciones."

"Ella debería de sonreír más seguido."

rin "Puedo llevarte a la puerta."

scene ev rin_high_grinwide
with locationchange




rin "Es lo menos que un caballero puede hacer."




scene ev rin_high_smile
with locationchange

"Rin se ríe como una niña pequeña, haciendo que esté más que absolutamente seguro de que hoy tomó demasiado del medicamento para su resfriado."

rin "Siempre había querido decir eso."

scene bg school_dormrin
with locationchange

show rinpan invis:
    twoleft
    ypos 1.1
with None

show rinpan basic_deadpandelight at twoleft
with dissolvecharamove

"Poco a poco y con dificultad, Rin primero se sienta otra vez, luego se pone de pie con aún más dificultad y con aún mayor lentitud."

"Como si fueran guiados por alguna automatización masculina, mis ojos instantáneamente bajan a la curva de sus muslos y las pantaletas a rayas, al punto tal que mis modales me fuerzan a levantar la mirada de vuelta al nivel de los ojos de Rin."


"Está casi poniéndose demasiado difícil de hacer."

"Rin está de pie, pero apenas. Parece que tiene problemas manteniendo su, generalmente decente, equilibrio de nuevo; probablemente un efecto secundario de la medicina."

show rinpan basic_deadpandelight:
    ease 1.0 center
with None

show rinpan basic_deadpandelight_close:
    twoleft
    ease 1.0 center
with Dissolve(1.0)

"Ella da un inestable paso hacia mí, luego uno más pequeño al darse cuenta de que no es una buena idea el tratar de dar pasos grandes."

"Siento mis músculos tensarse mientras me preparo para atrapar a Rin si se cae."

play music music_twinkle fadein 3.0

scene ev rin_kiss:
    center
    yalign 0.0 zoom 4.0 subpixel True
    easein 0.4 zoom 1.05
    easein 5.0 zoom 1.0
with flash

"Ella se las arregla para dar dos pasos más antes de caer sobre mí. Para mi sorpresa, ni su impulso hacia abajo ni nuestra ligera diferencia de altura son capaces de evitar que Rin presione sus labios con forma de corazón directamente sobre los míos."

"A la vez que nuestros labios se separan, después de un confuso momento de nada más que el sabor de… Rin, miro abajo hacia ella, tratando de encontrar alguna explicación para este desconcertante acontecimiento."

$ renpy.music.set_volume(0.7, 2.0, channel="music")

scene bg school_dormrin
show rinpan basic_deadpandelight_close at center
with locationchange

"La eufórica sonrisa de un desquiciado se acrecienta sobre los labios de Rin otra vez y—"

show rinpan relaxed_sleepy_close
with charachange

rin "Me pregunto si recordaré esto mañana."


"Me encuentro completamente indeciso en cómo responder."

show rinpan relaxed_sleepy_close:
    ease 1.0 twoleft
with None

show rinpan relaxed_sleepy:
    center
    ease 1.0 twoleft
with Dissolve(1.0)

"Rin da un paso hacia atrás, separando su cuerpo del mío, y haciendo que me percate hasta ahora de que estuviesen conectados, para empezar."

show rinpan invis:
    ypos 1.1
with dissolvecharamove

play sound sfx_pillow


"El segundo paso es de hecho una caída hacia atrás, afortunadamente directa hacia su cama."


"El suave y sordo ruido que hace el delgado cuerpo de Rin contra el colchón rompe el silencio."

scene ev rin_high_open
with locationchange

"Me muevo rápidamente hacia ella para ver si se lastimó, solo para encontrarme con el pacífico rostro del sueño."

"Rin duerme."

"Está acostada en diagonal sobre la cama, de algún modo arreglándoselas para quedarse dormida mientras estaba de pie, y caer de modo que no se haya lastimado a sí misma."

"Un golpe de suerte."

scene ev rin_high_sleep
with locationchange

"Arropo a Rin, cubriéndola con las sábanas lo mejor que puedo."

"Ella se siente muy ligera, incluso si no soy tan fuerte."

show ev rin_high_sleep:
    subpixel True xalign 1.0 yalign 0.0
    ease 10.0 zoom 1.1
with None

"Me levanto para verla, el rostro ovalado, las pestañas oscuras cerradas sobre las mejillas febriles, el esbelto cuerpo cubierto con las pálidas sábanas."

"Rin duerme."

"Un conflicto. No. Conflictos, plural, se arremolinan en mi interior. Pienso en llamarle a algún enfermero para que la mantenga vigilada, pero decido en contra de eso. Después de tomar una última mirada a su rostro apacible, decido que ella estará bien."

"Aunque sí me echo las píldoras que quedan al bolsillo."

stop music fadeout 5.0

scene bg school_girlsdormhall
with locationchange

"Salgo de la habitación, y cierro la puerta detrás de mí sin hacer ruido."

"Exhalo con profundidad, hasta ahora advirtiendo que había contenido la respiración por buena parte de un minuto. Tomándome un momento para relajarme, trato de tranquilizar mi corazón, el cual corre como una liebre."

$ suppress_window_after_timeskip = True

scene black
with dissolve




label es_R16:

window hide None

scene black
with dissolve

play music music_pearly fadein 1.0

scene bg school_dormhisao
with openeye

window show

"Tuve problemas para dormir aquella noche, así que a la mañana siguiente me encuentro excepcionalmente adormilado."
"Momentáneamente considero faltar a clases, pero me recuerdo a mí mismo que se supone ahora sería una persona más fuerte."

scene bg school_courtyard
with locationskip

"Me levanto como un buen chico y me pongo el uniforme, luego me dirijo al edificio principal sin desayunar."

scene bg school_scienceroom
with locationskip


"Me siento en mi lugar en el salón 3-3, saludando con la mano a Misha y a Shizune como lo hago cada mañana, y dejo que el día me envuelva."

with shorttimeskip

"Las clases de la tarde son siempre más largas que las de la mañana. Esto es verdad sin importar si lo cuento por minutos o por el número de garabatos dibujados en mi cuaderno."


"Hoy estoy especialmente distraído, por seguir pensando en Rin."

$ renpy.music.set_volume(0.5, 0.5, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\n\n\n\n¿Logré decirle apropiadamente que quiero mejorar? ¿Entendió ella alguna palabra de lo que estaba diciendo?"

n "Pienso en el beso que compartimos y lo que significa. Ella estaba tan fuera de sí, que tal vez no signifique nada. Pero nos hemos estado acercando, últimamente. ¿Qué significa eso?"

n "\n\n\nPienso más y más en Rin hoy en día. Me pregunto si ella piensa en mí."

$ renpy.music.set_volume(1.0, 4.0, channel="music")
play sound sfx_normalbell
nvl clear
nvl hide dissolve
window show

"El sonar de las campanas me toma por sorpresa, y entonces me hace notar que no he estado prestando nada de atención durante la segunda mitad de la clase."

"Veo la diversidad de dibujos que van de arriba a abajo por los márgenes de mi cuaderno, lo único que hice en la última hora."

"Sintiéndome ligeramente decepcionado de mí mismo, guardo mis cosas y me dirijo al pasillo."

stop sound fadeout 0.5
$ renpy.music.set_volume(0.0, 1.0, channel="music")
scene bg school_hallway3
show rin basic_absent at center
with locationchange

"Rin está de pie justamente fuera de la puerta, su presencia deteniéndome en seco tan pronto como la veo."

"Su postura es relajada como siempre, pero súbitamente siento como si acabara de comerme una palanca. Estoy teniendo dificultades para verla a los ojos."

"Ella parece no tener ningún problema al verme, pero esos ojos oscuros me están haciendo sentir nervioso sin motivo."

"Es difícil verla directamente, así que aparto mi mirada un poco."

"No sé qué es lo que uno debería de decir en este tipo de situación."

"Por otra parte, rara vez sé qué decirle a Rin en cualquier situación dada."

$ renpy.music.set_volume(1.0, 8.0, channel="music")

hi "Ehh… hola."

show rin basic_deadpan
with charachange

rin "Hola."

"Trato de deshacerme de la sensación de incomodidad en mi voz e invoco un modo más natural de hablar. De repente me preocupa dónde debería de poner las manos; de alguna forma se siente como si estuvieran estorbando."


hi "¿Cómo te sientes? Estabas muy rara ayer."

show rin basic_awayabsent
with charachange

rin "Estoy bien. ¿A qué te refieres con ayer?"

hi "¿No lo recuerdas?"

show rin relaxed_disgust
with charachange

"Ella inclina su cabeza a un lado como un pájaro, viéndose un poco confundida."

rin "¿Recordar qué? Tengo una memoria muy mala."

hi "Sobre lo de ayer."

show rin relaxed_surprised
with charachange

rin "¿Qué hay de ayer?"

hi "Vine a verte y…"

show rin relaxed_nonchalant
with charachange

rin "No recuerdo que sucediera ese tipo de cosa."

"¿En verdad no lo recuerda? No sé si esto es algo bueno o algo malo, pero me siento desanimado de igual manera."

show rin basic_lucid
with charachange

rin "Aunque recuerdo que prometí mostrarte un lugar. ¿Eso pasó en verdad?"

show rin basic_awayabsent
with charachange

rin "Tal vez solo pienso que lo recuerdo y la verdad es que no."

hi "No, eso también fue real."

show rin basic_absent
with charachange

rin "Está bien. ¿Quieres ir?"

hi "¿Ahora?"

show rin basic_deadpannormal
with charachange

rin "Sí."

hi "Bueno, claro, ¿por qué no? ¿Está lejos?"

show rin basic_deadpan
with charachange

rin "No lo está."

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
$ renpy.music.set_volume(0.8, 0.5, channel="music")
play ambient sfx_parkambience fadein 0.5

scene bg school_courtyard
with locationskip

"Caminamos juntos escaleras abajo y luego hacia afuera. El usual día de verano, cigarras zumbando y todo, nos saluda. Hace mucho calor, y sin el aire acondicionado que brinda el salón, comienzo a sudar de inmediato."

scene bg school_gardens
with locationchange

"Caminamos por el sendero arbolado que lleva a los dormitorios."

"Los cerezos brindan sombra mientras la luz del sol parpadea a través de agujeros en el follaje. La luz crea un caótico patrón de sombras moteadas con partes brillantes donde los rayos tocan el pavimento."

"Los ojos de Rin merodean en todas direcciones excepto hacia mí. Tengo la sensación de que es intencional."

$ renpy.music.set_volume(0.7, 0.5, channel="ambient")
$ renpy.music.set_volume(0.6, 0.5, channel="music")

scene bg school_forest1
with locationskip


"Ella me lleva a la puerta trasera una vez más, nos conduce a través de esta y hacia el interior del bosque más adelante."
"Al igual que antes, la temperatura que va bajando y los drásticamente reducidos niveles de luz, hacen que se sienta como si el bosque nos estuviera tragando directo a su vientre cavernoso."

scene bg school_forest2
with locationchange

"Nos dirigimos cuesta arriba por el mismo camino de la vez pasada, serpenteando alrededor de los árboles y peñascos, raíces y rocas, más allá de la maleza silvestre."
"Los pájaros cantan en algún lugar en el bosque, solistas en el silbido de la música de fondo en las copas de los árboles."

scene bg school_forestclearing
with locationchange

"Vamos más allá del pequeño claro con el gran arce que ahora es llamado el Árbol de la Preocupación. El ascenso se complica, luego se vuelve a facilitar de nuevo."

scene bg school_forest2
with locationchange

"Tengo que detenerme algunas veces para recuperar el aliento, luego me apresuro tras de Rin, quien no se detiene a esperarme."

"Pronto estoy sin aliento de nuevo."

$ renpy.music.set_volume(1.0, 0.5, channel="ambient")
$ renpy.music.set_volume(0.4, 0.5, channel="music")

scene bg school_hilltop_border
with locationchange

"De modo inesperado, los árboles terminan y salimos del bosque. El límite de la arboleda es marcado y abrupto, como si una línea hubiese sido dibujada para señalarlo."

"La colina continúa su ascenso un poco más allá, pero de aquí a la cima se encuentra un prado rocoso, parches de hierba y pequeños arbustos que parecen crecer directamente de la roca."

$ renpy.music.set_volume(1.5, 0.5, channel="ambient")
stop music fadeout 2.0
$ renpy.music.set_volume(1.0, 10.0, channel="music")

scene bg school_hilltop_spring at Fullpan(15.0)
with locationchange

"Pronto alcanzamos el punto más alto, con el bosque detrás de nosotros y la vista abriéndose en todas direcciones frente a nuestros ojos."

"La ciudad yace muy abajo y lejana, perezosamente deleitándose en el silencioso ánimo de la tarde."

"Puedes ver bastante lejos desde aquí, y la vista panorámica es hermosa. Me pregunto qué tan alto estamos."

"Respiro el aire fresco y siento el latir de mi corazón bajar lentamente. Creo que pude haberme exagerado un poco; un pulso más alto es peligroso para mí. Aunque ahora me estoy sintiendo bien."

"El viento comienza a soplar con fuerza, despeinándome y haciendo que se mezan los árboles debajo de nosotros. Causa que las hierbas ondulen como olas a medida que la brisa corre por la cima."

"El sol brilla desde los cielos abiertos sobre nosotros, y algunas nubes pasando para ensombrecerlo. Lo que era un doloroso ardor antes ahora es una suave calidez."

"Le doy una buena mirada a mis alrededores. La cima es bonita del modo en el que la naturaleza a menudo lo es, armonía sin planificar que se encuentra en el arreglo natural de las cosas."

"El rasgo más distintivo es la abundancia de pequeñas flores amarillas. Se encuentran literalmente en todas partes de este prado. No puedo evitar comentar sobre ello."

hi "Guau. Cuántas flores."

show bg school_hilltop_spring at right
show rin basic_absent at center
with charaenter


rin "Sí. ¿Conoces las de este tipo? Volarán algún día."

hi "Sí. Dientes de león."

show rin basic_awayabsent
with charachange

rin "No hay muchas de ellas en la escuela, porque cortan el césped muy seguido. Nadie corta el césped aquí."

"Las flores de aspecto frágil pronto se tornarán blancas y afelpadas como el algodón, y el viento se llevará sus semillas."

$ renpy.music.set_volume(1.0, 0.5, channel="ambient")

scene ev dandelion:
    yalign 0.5 xalign 0.5 zoom 0.8 subpixel True
    ease 20.0 zoom 0.9
with locationchange

"Me agacho para ver a una diminuta flor amarilla, silenciosamente disfrutando de la luz del sol. No hay ni rastro de blanco todavía, así que aún está esperando a que su tiempo se haya consumado."

"Paso mis dedos sobre los delicados pétalos amarillos, siento la suave textura en las yemas. Se siente nostálgico, de algún modo. Oigo a Rin acercarse por atrás y me pongo de pie para verla de frente."

stop ambient fadeout 3.0

scene bg school_hilltop_spring at left
show rin basic_sad at center
with locationchange

"Tiene una rara mirada en su rostro."

hi "¿Tienes algo en mente?"

show rin basic_upset
with charachange

rin "No lo sé. Es solo…"

play music music_rin fadein 0.5

rinbabble "Te ves tan triste todo el tiempo y te molestas tan fácilmente y eso hace que me confunda y realmente no recuerdo mucho de lo de ayer excepto que tú viniste a mi habitación y podría ser por eso por causa mía así que si es causa mía creo que sé por qué, es porque a la gente en realidad no le gusta hablar conmigo y tú podrías ser igual y eso sería triste conozco a esas personas y estoy hablando de otro aparte de Emi siempre dice que soy rara y que hablo de cosas raras así que pensé que trataría de no decir cosas raras pero eso solo me hace pensar más y nuevo y raro y colorido esa no fue una buena palabra pero tal vez entiendas de todas formas y cosas extrañas así que si quiero decir algo en verdad no sé cómo y entonces las palabras no son las mismas que los pensamientos porque algo anda mal cuando sale pero no es como si los pensamientos sean lo que debería de estar diciendo es más como la idea del pensamiento o el sentimiento de la idea o la idea del sentimiento pero tampoco es alguno de ellos porque no hay ninguna palabra para ello a menos que invente una nueva lo cual no es muy útil así que he estado pensando si hacer cosas es mejor que decirlas así que quizás porque ayer tomé esas píldoras y me estaba sintiendo un poco rara podría haber hecho algo que no debería además ni siquiera sé si sería mejor si tan solo podría decir el pensamiento no hay telepatía que sea telepatía real o sí creo que sería terrible y útil a la vez pero en este momento no me molestaría porque malentender es tan fácil pero entender no lo es y pensé—"

stop music
play sound sfx_pillow
with vpunch


"Sujeto su hombro y aprieto con fuerza para hacerla parar. No tengo la capacidad para procesar todo eso de una sola vez."

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

show rin basic_surprised
with charachange

"Rin se calla al instante."

hi "Respira."

hi "No estoy molesto. ¿Por qué lo estaría? Solo estoy un poco confundido, pero está bien."

"Me pregunto si estaba haciendo una cara que a ella no le agrada, otra vez. Supongo que he estado pensando en el día de ayer todo el tiempo. Quizás me veía raro. Ojalá tuviera un espejo conmigo a todas horas."

hi "No hay necesidad de decirlo todo de una vez. Te escucharé, aun si hablas más lento."

show rin basic_deadpanupset
with charachange

rin "Solo salió. Disculpa. Ya estoy bien. Es solo que quería decir algo. No quise decir todo eso."

play music music_innocence fadein 10.0

show rin negative_worried
with charachange

rin "Es raro, ¿verdad?"

"Me mira con una expresión sorprendentemente tímida, una que no había visto antes. No puedo evitar reír un poco."

hi "Sí, es raro."

hi "Tú eres una persona bastante rara, pero no hay nada de malo en ello."

hi "Gracias por preocuparte por mí, pero me pondré mejor. Te lo dije ayer, pero supongo que tampoco recuerdas eso."

show rin relaxed_nonchalant
with charachange

rin "No lo recuerdo. Me pregunto qué más olvidé. Espero que nada importante como mi propio nombre. Eso sería terrible."

hi "Bueno, me besaste."

show rin relaxed_surprised
with charachange

rin "¿Lo hice?"

hi "Sí, lo hiciste. En los labios."


"Trato de sonar con tanta naturalidad como me es posible, pero me preocupa que me esté sonrojando de nuevo."

show rin relaxed_doubt
with charachange

rin "¿Me pateaste?"

hi "¡No! ¿Por qué haría eso?"

show rin basic_deadpancontemplation
with charachange

rin "Entonces, todo está bien, ¿verdad? Está bien, ¿no? No olvidé mi nombre."

hi "Sí, está bien."

"Quisiera ser más afable para que pudiera pensar en una frase mejor a esa, pero nada se me viene a la mente. Es algo bueno que Rin tenga más que decir. Me hace sentir aliviado, de algún modo."

show rin negative_confused
with charachange

rin "Creo que debería decir lo siento. En verdad soy mala con la gente."

show rin negative_spaciness
with charachange

rin "Algunas cosas son difíciles de entender, como las medusas. ¿Tú entiendes a las medusas?"

hi "Ah… Creo que no."

show rin negative_sad
with charachange

rin "La gente es como las medusas para mí. No entiendo."

"Ahora es su turno de hacer una cara que realmente no me gusta ver."

show rin basic_sad
with charachange

label es_choiceR16:

menu:
    with menueffect
    rin "Realmente nunca he tenido amigos."
    "¿Qué hay de mí?":


        return m1
    "¿Qué hay de Emi?":

        return m2

label es_R16a:


hi "Nah. Yo soy tu amigo, por ejemplo."

hi "Quiero decir, piénsalo. Ya hablamos mucho el uno con el otro, e incluso nos hemos enfadado el uno con el otro y luego perdonado por ello."

hi "Eso es lo que llaman amistad."

label es_R16b:

hi "¿Qué hay de Emi?"

show rin basic_surprised
with charachange

"Ella hace una pausa por un momento, como si tener que considerar la posibilidad le haya venido de sorpresa."

show rin basic_awayabsent
with charachange

rin "Emi… me cuida. En realidad no sé por qué."

show rin negative_annoyed
with charachange

rin "Pero no puedo realmente hablar con ella, no de esa manera. Es como si su cabeza estuviese hecha de espuma de jabón y malvaviscos. O tal vez sea solo yo. Pero me agrada."

hi "Ella es muy agradable, ¿no es así?"

show rin basic_absent
with charachange

rin "Sí."

hi "Yo también quiero ser tu amigo."

hi "Te escucharé si quieres hablar. Si no, entonces puedo solo sentarme en silencio a tu lado."

hi "Y quiero decirte sobre lo que pienso, también. Esto va en ambas direcciones."

hi "Definitivamente deberíamos ser amigos."

label es_R16c:

show rin basic_deadpanamused
with charachange

rin "Es realmente lindo de tu parte, decir eso."

show rin basic_awayabsent
with charachange

rin "Siempre he podido decirle todo a los lápices y pinturas y papel. Son mis mejores amigos."

show rin basic_lucid
with charachange

rin "Es más difícil con la gente. Tengo que usar palabras, eso es difícil para mí."

hi "Sí, lo sé, me lo dijiste. Sobre cómo olvidas."

show rin basic_absent
with charachange

"Rin asiente sin decir más y me atrevo a intentar mostrarle una pequeña pero alentadora sonrisa. Espero hacerla adecuadamente. Ella no responde de ninguna manera."

"Me siento muy feliz. La distancia que Rin pone entre ella y todos los demás me ha hecho sentir muy inquieto desde que la conocí. Si nos hacemos verdaderos amigos, estoy seguro de que podría entenderla más."

"Estoy seguro de que, de este modo, podemos cerrar esa brecha en la comprensión entre nosotros."

show rin basic_awayabsent
with charachange


"Mis pensamientos no se transmiten a Rin. Ella parece perdida sumida en los suyos, errante en un mar de flores amarillas envolviendo la cima de la colina cubierta de hierba. Es igual de bueno."

$ renpy.music.set_volume(0.4, 2.0, channel="music")
play ambient sfx_parkambience fadein 7.0

scene bg school_hilltop_spring_ss at left
with shorttimeskip

"El tiempo pasa, la brisa hace a la hierba más alta mecerse gentilmente al compás del viento. Rin tararea una cancioncilla a sí misma en una voz tan baja que no puedo decir qué es, si es que es algo."

"Una ráfaga más fuerte pasa sobre la cima de la colina, y el sonido de los árboles en el viento ahoga la canción."

"Veo mi reloj, más por hábito que por cualquier otra razón. Son las 4:30 en este momento, en esta tarde de sábado."

show rin basic_awayabsent_ss at center
with charaenter

"Rin mira hacia el horizonte distante con esa rara mirada vacía suya, como si no estuviese viendo nada en absoluto. Sus pupilas son oscuras y silenciosas como un par de estanques profundos e inmóviles."

$ renpy.music.set_volume(0.7, 6.0, channel="music")

label es_R16d:

hi "Creo que voy a renunciar al club de arte. Me di cuenta de ello cuando tuvimos esa discusión la semana pasada."

hi "Fue algo bueno que lo probara, pero simplemente no es para mí, ¿sabes? Me divertí más llegando a conocerte que de verdad haciendo cosas de arte."

hi "Pero quiero seguir siendo tu amigo. ¿Te parece bien?"

show rin basic_deadpan_ss
with charachange

rin "Seguro. Se estaba poniendo muy espeluznante contigo mirándome todo el tiempo, de todos modos."

"Su comentario hace que me ponga nervioso de inmediato, pero me las arreglo para responder."

hi "Discúlpame por eso."

show rin basic_deadpandelight_ss
with charachange

rin "Está bien, estoy acostumbrada. No eres la primera persona a quien le gusta verme pintar."

show rin basic_absent_ss
with charachange

rin "¿Vas a hacer alguna otra cosa?"

hi "No lo sé. Probablemente no."

label es_R16e:

show rin relaxed_doubt_ss
with charachange

rin "Te vas a poner mejor, ¿verdad?"

hi "Claro."

show rin relaxed_nonchalant_ss
with charachange

rin "Yo también, sabes. Voy a hablar con esa amiga del maestro y pedirle que ponga mis cosas en su lugar y trabajaré duro para tener todo eso listo."

show rin basic_lucid_ss
with charachange

rin "Acabo de decidirlo, sabes. Pero creo que lo sabía desde el principio."

show rin basic_deadpannormal_ss
with charachange

rin "He tenido esta sensación por un largo tiempo ya, que voy a cambiar. Incluso si lo odio y no lo quiero, incluso si lo quisiera, cambiaría."

show rin basic_deadpanupset_ss
with charachange

rin "Como si no fuera suficiente con cómo soy ahora. Creo que esto podría ser una buena manera de hacerlo porque es como una línea recta."

show rin basic_deadpancontemplation_ss
with charachange

rin "Como si todo lo que he aprendido en mi vida hasta ahora fuera solo para esto. Es solo arte, y es lo único que conozco de verdad. Sé lo que voy a hacer, así que está bien. No tengo nada de miedo."

show rin basic_deadpansurprised_ss
with charachange

rin "Me siento como siempre me siento. ¿Es eso raro?"

hi "No. De ninguna manera."

stop ambient fadeout 2.0
$ renpy.music.set_volume(1.4, 4.0, channel="music")

window hide

scene black
with shuteye

window show

"Cierro los ojos, y cedo a la irresistible sensación que ha estado creciendo dentro de mí durante toda la semana."

"Floto hacia lo alto, hacia la superficie de mi propia vida."

"La presión de estar bajo el agua disminuye lentamente, y la sensación de ingravidez se hace más fuerte."

"Rompo la superficie del agua, levanto la cabeza hacia el sol e inhalo con profundidad, respirando aire fresco como si fuera la primera vez en un largo, largo tiempo."

scene bg school_hilltop_spring_ss at left
show rin basic_deadpandelight_close_ss at center
with openeye

"Mis pulmones se llenan de oxígeno, y abro los ojos para ver el rostro tranquilo y decidido de Rin."

stop music fadeout 10.0
$ renpy.music.set_volume(1.0, 2.0, channel="music")

scene bg school_hilltop_border_ss
with shorttimeskip

"Caminamos por la ladera con cuidado y con lentitud para evitar caernos, Rin al frente y yo unos pasos atrás."

"Rin sin duda puede hacerlo. Incluso si no puede, logrará salir adelante."

"Estoy seguro de que podré mantener la cabeza fuera del agua, también, de ahora en adelante."

"El sol se oculta tras nuestras espaldas, encendiendo el mundo en llamas con su brillo naranja."

"Sigo mirando la espalda de la chica pelirroja descendiendo por el camino unos pasos por delante de mí."

"Si es solo este tanto… esta distancia entre nosotros está sin duda dentro de mi alcance."

window hide

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
