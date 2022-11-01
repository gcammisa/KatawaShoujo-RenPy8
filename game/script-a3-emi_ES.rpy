label es_E16:

window hide None

scene bg school_scienceroom
with fade

nvl clear
nvl show dissolve

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_normal fadein 3.0

n "\n\n\nMi cabeza no para de dar vueltas durante la clase de Mutou."

n "Voy a salir a comer."

n "Con Emi."

n "Quien quiere ser mi novia, nada menos."

n "Una cita…"

n "Y luego me besó."

n "Ese beso. Sigo regresando a él, repitiéndolo una y otra vez en mi cabeza."

n "Todo sobre ese momento se sintió tan bien."

n "\nMi mente divaga, distraída con pensamientos de Emi."

$ renpy.music.set_volume(1.0, 2.0, channel="music")

nvl clear
nvl hide dissolve
window show

show muto normal
with charaenter

mu "¿Nakai? ¿Hola?"

"Al parecer me perdí en mis divagaciones."

hi "¿Eh? ¿Qué?"

show muto irritated
with charachange

mu "¡Dioses! ¡Has contraído algún tipo de amnesia!"

mu "¡Alguien llame al enfermero!"

"La clase ríe con las payasadas de Mutou."

hi "Perdón, señor."

show muto normal
with charachange

mu "Hmm, no pasará de nuevo y todo eso, ¿no?"

hi "Exacto."

"Mutou se anima considerablemente."

show muto smile
with charachange

mu "¡Bien! ¡Me alegra escucharlo!"

mu "No me gustaría tener a mi alumno estrella holgazaneando, después de todo."

hide muto
with charaexit

"Lo he estado haciendo bien, pero creo que difícilmente califico como alumno estrella."

"Estoy seguro de que este es el tipo de clase en la que todos lo hacen bien. Solo debes memorizar fórmulas."

"Fiel a mi palabra, me las arreglo para prestar atención durante el resto de la clase."

stop music fadeout 2.0

show muto normal
with shorttimeskip

play sound sfx_normalbell

mu "Nakai, ¿puedo hablar contigo?"

"Me pregunto si estoy en problemas por lo de antes."

hi "Eh, claro."

hi "¿Estoy en problemas?"

show muto irritated
with charachange

"Mutou se ve genuinamente confundido por un instante."

mu "¿Disculpa?"

"Él inclina la cabeza hacia un lado y piensa por un momento."

show muto smile
with charachange

mu "¡Oh, eso! No, no, no estás en problemas."

mu "Solo me gustaría preguntarte algo."

hi "¿Qué cosa?"

show muto normal
with charachange

mu "Nada terrible, solo me preguntaba cuáles son tus planes para después de la graduación."

play music music_another fadein 2.0

mu "¿Irás a la universidad?"

hi "Sí, supongo. En realidad no veo una razón para no ir."

mu "¿Has pensado en qué te gustaría estudiar?"

hi "No, no realmente. Pensaba que ya se me ocurriría algo una vez llegara allá."

show muto smile
with charachange

"Mutou se ríe."

mu "Tomando las cosas como vengan, ¿eh?"

mu "Estaría en contra de eso, pero así lo hice yo cuando fui a la universidad."

mu "Bueno, no realmente."

mu "Sabía que iría por alguna ciencia, solo que no estaba seguro de cuál."

mu "Terminé en física, pero igual podría haber terminado en astronomía o lo que fuese."

show muto irritated
with charachange

mu "La verdad es que primero fui por química, pero había toda clase de cosas…"

"Mutou se calla, y frunce el ceño levemente."

"Le toma un minuto recuperar su línea de pensamiento, y espero pacientemente a que continúe."

show muto normal
with charachange

mu "En fin, también avancé mucho en física, porque me interesaba, pero no estaba seguro de si era lo mío."

show muto smile
with charachange

mu "Así que regresé a química, y aquí estamos. ¿Sí?"

show muto smile
with charachange

"Él me sonríe con entusiasmo, como si esperara que yo confirme ese sí, que aquí es donde estamos."

"Por algún motivo tengo la sensación de que Mutou tenía un plan para esta conversación, pero mentiría si digo que lo puedo adivinar."

hi "Perdón, pero no te sigo."

"Mutou frunce el ceño y se rasca la barbilla por un momento, viéndose perplejo. Luego chasquea sus dedos como si hubiera recordado cuál era el punto de todo esto."

mu "¡Cierto! ¡Sí! ¡Tú!"

hi "¿Yo?"

mu "¡Sí! ¡Deberías considerar estudiar una de las ciencias!"

mu "Eres fantástico con ellas."

mu "A menos de que quieras irte por las matemáticas."

show muto irritated
with charachange

"Mutou pone cara de amargura."

mu "No soy un gran fanático de las matemáticas puras. Siempre me gustaron más los experimentos que las pruebas."

hi "¿Estás diciendo que debería de estudiar ciencias en la universidad?"

"Mutou parece desbalancearse por mi pregunta."

show muto normal
with charachange

mu "Bueno, algo así."

show muto smile
with charachange

mu "¡También podrías unirte al club de ciencia!"

mu "El problema es, en realidad no hay un club de ciencia."

mu "¡Pero podría haber uno!"

mu "¡Incluso podrías ser uno de los primeros miembros!"

mu "¡Un padre fundador!"

mu "Por supuesto, necesitarías encontrar otros miembros."

show muto normal
with charachange

mu "Bueno, solo si querías."

mu "Podríamos empezarlo solo nosotros dos."

mu "Y um."

show muto smile
with charachange

mu "Podría darte cosas para leer, y podríamos hablar de ellas."

mu "Eh, y también podría ayudarte con la preparación para la universidad y eso."

show muto irritated
with charachange

mu "¡Espera!"

"Mutou hurga en su maletín y me lanza un libro."

show muto smile
with charachange

mu "Lee eso."

mu "Si es interesante, entonces podríamos hablarlo."

"¿“Breve Historia del Tiempo”?"

"No sé si realmente quiero leerlo, pero Mutou parece muy emocionado por esto."

hi "¿De qué se trata?"

show muto normal
with charachange

mu "Tiempo. Espacio. Espacio-tiempo. Agujeros negros y demás."

mu "Y no es tan denso. Es solo para ver si ese tipo de cosas te son interesantes, tú entiendes."

mu "Pásate luego de clases, y podemos discutirlo, o puedo enseñarte a hacer explosivos en el laboratorio."

show muto smile
with charachange

"Él sacude una mano ante mi expresión de curiosidad."

mu "Bromeaba, lo siento."

mu "Aun así, ya te he mantenido aquí por un buen rato."

mu "Piensa en la ciencia como una trayectoria profesional, Nakai. Creo que lo disfrutarías."

hi "Eh, de acuerdo. Lo haré. Gracias por el libro."

stop music fadeout 14.0

scene bg school_hallway3
with locationchange

"Salgo del aula y miro hacia el reloj; una considerable porción de tiempo por matar hasta que Emi salga de la práctica."

"Supongo que ojearé este libro; probablemente también debería de bañarme."

"Bañarse antes de una cita es lo más adecuado, ¿verdad?"

"Me dirijo de vuelta a los dormitorios."

scene bg school_dormhisao
with locationskip

"De todas maneras, me pregunto en dónde se supone que me encuentre con Emi."

"Ella dijo “luego de la práctica”, pero no dijo dónde debía encontrarme con ella."

"Supongo que puedo pasar por la pista; probablemente sea lo mejor, de todos modos."

"Si ella necesita ducharse, podría esperarla en su habitación o algo."

"O en el corredor, supongo; eso también sería lo mejor."

"Tomo una ducha rápida, recordando tomar mi medicina una vez salgo."

"Ahora, a echarle un vistazo a este libro."

stop music

scene black
with dissolve


label es_E17:

scene black
with None

scene bg school_dormhisao
with vpunch

"Me despierto con un sobresalto."

"¡Mierda! ¿Qué hora es?"

"Un vistazo al reloj revela que he estado dormido por casi una hora."

hi "Gracias al cielo."

"La práctica de Emi debería de estar por terminar."

"Me pongo ropa casual y me dirijo a la pista."

scene bg school_track
with locationskip

"Por algún motivo tengo el presentimiento de que no vamos a hacer nada estrafalario para la cena."

"Emi no me da la impresión de ser una persona muy extravagante."

"Aun así, supongo que todavía tengo muchas cosas que aprender sobre Emi."

"A pesar de nuestra recién descubierta cercanía, todavía siento que no la conozco tan bien como debería."

"Oh bueno, tengo mucho tiempo para arreglar eso."

"Para ser honesto, espero con ansias conocerla más."

"Estoy tan atrapado por mis propios pensamientos que apenas registro que ya estoy en la pista."

"No veo a Emi por ningún lado."

"Ni siquiera veo señales del equipo de atletismo."

"Esto podría ser vergonzoso."

"Me doy vuelta para encaminarme hacia el dormitorio de las chicas cuando escucho a alguien."

emi "¡Oye, Hisao!"

play music music_emi fadein 1.0

show emicas smile at center
with charaenter

"Me doy vuelta para ver a Emi venir derechito hacia mí con una bolsa de gimnasia colgando del hombro."

"Ella se puso ropa definitivamente más casual; unos pantalones cortos y una blusa verde oliva."

"Sus prótesis para correr han sido reemplazadas por unas piernas de apariencia más realista que probablemente no engañan a nadie."

"A Emi no parece importarle eso, algo que me hace sonreír."

show emicas happy
with charachange

emi "¡Oye, viniste!"

show emicas closedsmile
with charachange

emi "Digo, pensé que lo harías, pero aun así…"

show emicas closedsmile_up_close
with characlose

"De repente me encuentro atrapado en un abrazo bastante afectuoso, y parece ser imposible para mí mantener lo que podría ser la mayor sonrisa del mundo fuera de mi rostro."

hi "Bueno, ¡claro que vine!"

hi "Estaría loco de no ser así, ¿cierto?"

"Emi reflexiona por un momento."

show emicas grin_up_close
with charachange

emi "Sabes, es cierto."

show emicas wink_up_close
with charachange

emi "Quiero decir, soy bastante asombrosa, después de todo."

"Me encojo de hombros en respuesta."

hi "Ya lo creo."

show emicas blush_up_close
with charachange

"Es un comentario desinteresado, por eso me sorprendo al ver que parece haber tomado a Emi por sorpresa."

show emicas smile_up_close
with charachange

"Ella se sonroja y me sonríe cálidamente antes de plantar un beso en mis labios."

"Ahora es mi turno de estar sorprendido."

show emicas grin
with charadistant

"Emi da un paso atrás, descansando su peso sobre sus talones, viéndose complacida consigo misma."

"Mi cerebro busca a tientas una respuesta adecuada."

hi "…"

hi "Debería de halagarte más a menudo."

show emicas happy_up
with vpunch

"Emi se ríe y me da un empujoncito juguetón."

show emicas closedsmile
with charachange

emi "Idiota."

show emicas weaksmile_up_close
with characlose

"Coloco un brazo alrededor de los hombros de Emi y me siento complacido cuando ella inmediatamente se inclina sobre mí como si fuera lo más natural del mundo."

hi "Entonces, ¿a dónde?"

show emicas awayfrown_up_close
with charachange

emi "La verdad no estoy segura."

show emicas neutral_up_close
with charachange

emi "Más bien, ¿a dónde va la gente a citas por estos lugares?"

"Esa es una muy buena pregunta."

hi "No tengo ni idea."

hi "¿Por qué no bajamos al Aura-Mart y buscamos algo para llevar?"

"El rostro de Emi se ilumina con esta idea."

show emicas happy_up_close
with charachange

emi "¡Un picnic!"

show emicas wink_up_close
with charachange

emi "Creo que tienes razón, Hisao."

scene bg school_gate
with locationskip

"Emi acomoda su brazo alrededor de mi cintura, y nos dirigimos hacia el portón de la entrada."

"No tengo ni la más mínima idea de qué debería hacer en esta situación, pero al menos Emi se ve igual de perdida."

scene bg suburb_roadcenter
with locationskip

"A pesar de la relajante sensación de estar con Emi, no puedo evitar sentirme un poco tenso."

"¿Qué tal si hago algo mal?"

"No me gustaría quedar como un completo imbécil."

scene bg suburb_konbiniext
with locationchange

"El viaje al Aura-Mart es acompañado por la plática de Emi sobre la práctica."

"Permanezco en silencio por la mayor parte, simplemente disfrutando de la calidez de estar cerca de Emi."

"Recibimos un par de miradas extrañas de los transeúntes, pero no me importa."

"Terminamos comprando algo de pan y fideos instantáneos, dándonos cuenta demasiado tarde de que en realidad no podemos cocinar estos últimos en el parque."

show emicas weaksmile
with charaenter

emi "Oh, bueno. Los haré para el almuerzo o algo así."

hi "Eso servirá."

stop music fadeout 2.0
$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_parkambience fadein 2.0

scene bg suburb_park
with locationskip

"Localizamos el parque luego de perdernos brevemente, algo por lo que culpo a Emi por completo."

"Ella, por supuesto, me culpa a mí."

show emicas smile:
    center
    easein 1.0 ypos 1.13
with charaenter

"Encontramos un lugar bajo un árbol y nos sentamos. Me recuesto contra el tronco, Emi se sienta frente a mí."

play music music_ease fadein 3.0

hi "Supongo que deberíamos de haber traído una sábana o algo para sentarnos, ¿eh?"

show emicas smile_up:
    ypos 1.13
with Dissolve(0.2)

show emicas smile
with charachange

"Emi se encoge de hombros."

show emicas closedsmile
with charachange

emi "No me importa."

hi "A mí tampoco."

show emicas grin_up
with charachange

"Emi me lanza un paquete de pan y empezamos a comer."

"Pan de curry. Interesante."

"Supongo que no estaba poniendo mucha atención a lo que agarré en la tienda."

show emicas wink_up
with charachange

emi "Oye, Hisao. Parece que tu pan está algo picante."

"Sacudo la cabeza, intentando en vano mantener una imagen de masculinidad."

hi "Nah, apenas si pica."

show emicas closedsmile_up
with charachange

emi "Ya veo, ya veo. Debe de ser por eso que tu cara se ha puesto tan roja."

hi "Sí, exacto. La falta de picante ha hecho que… se me suba la sangre a la cabeza."

hi "A causa de la decepción."

show emicas happy
with charachange

"Emi ríe y se traga el resto de su pan."

show emicas wink
with charachange

emi "Bueno, si no puedes con él, estaré encantada de quitártelo de las manos."

hi "Oye, solo porque devoraste el tuyo tan rápido no significa que te voy a dar el mío."

show emicas pout
with charachange

"Emi bromea haciendo muecas, provocando que casi me atragante con mi pan por la risa."

emi "Oh, ¡vamos, Hisao!"

show emicas awayfrown
with charachange


emi "¿No se supone que ahora debes asegurarte de que yo tenga suficiente comida?"

emi "¡Estamos saliendo, sabes!"

show emicas pout
with charachange

emi "Aunque…"

"De repente Emi se ve inquieta."

show emicas frown_up
with charachange

emi "No puedo decir que me sienta diferente."

hi "¿Hmm? ¿A qué te refieres con eso?"

show emicas awayfrown
with charachange

emi "¿Qué hace de esto una cita?"

emi "Es simplemente lo que habríamos hecho de todos modos, la verdad."

emi "Pero esto debería sentirse distinto porque antes cuando almorzábamos eramos amigos, y ahora estamos un nivel por encima de amigos."

hi "Suenas como Rin."

show emicas happy
with charachange

"La risa escapa, y Emi sonríe."

show emicas closedsmile_up
with charachange

emi "Bueno, puede que ella haya puesto el pensamiento en mi mente."

show emicas closedsmile
with charachange

emi "Hemos hablado de estas cosas antes."

hi "¿En serio? ¿De mí?"

show emicas grin
with charachange

emi "No realmente. Solo… cosas, en realidad."

show emicas neutral
with charachange

emi "Rin cree que el cambio de término de “amiga” a “novia” parece arbitrario la mayor parte del tiempo."

emi "Como si no hubiera diferencia entre los dos."

hi "Puedo pensar en al menos una, sabes."

hi "No sueles besar a tus amigos con tanta frecuencia."

show emicas blush
with charachange

"Por segunda vez en este día, Emi se sonroja ligeramente y suelta una risilla."

show emicas closedsmile
with charachange

emi "Creo que tienes razón."

hi "Exacto. Siempre tengo razón en cosas como esta."

show emicas weaksmile_up
with charachange

"Emi pone los ojos en blanco y se ríe."

emi "Supongo que eres bastante listo, ¿eh?"

"Asiento en acuerdo."

hi "Síp."

hi "Hasta Mutou piensa eso. Él cree que yo debería estudiar alguna ciencia luego de la graduación."

show emicas neutral
with charachange

"Emi levanta una ceja."

emi "Oh, ¿en serio?"

hi "Sí, pienso que podría hacer exactamente eso."

"En realidad, entre más considero la idea, más me llama la atención."

"Hago una nota mental para pensar más detenidamente en ello."

hi "Entonces, ¿qué piensas hacer luego de la graduación?"

hi "¿Aún piensas correr?"

show emicas awayfrown
with charachange

"Emi se encoge de hombros, casi viéndose un poco insegura."

show emicas frown
with charachange

emi "No lo sé. ¿Si soy lo suficientemente buena y encuentro un equipo, supongo?"

hi "¿Quieres decir que no estás segura?"

show emicas neutral
with charachange

emi "No he… pensado realmente en eso, para ser honesta."

hi "¿En serio?"

hi "Probablemente deberías, sabes. La graduación no está muy lejos."

show emicas awayfrown
with charachange

"Emi se retuerce un poco, nerviosa."

emi "Sí, bueno… está lo suficientemente lejos, ¿cierto?"

show emicas neutral
with charachange

emi "Además, tengo otras cosas en las que pensar."

show emicas grin_up_close
with vpunch

"Hay un travieso resplandor tras los ojos de Emi, y de repente me encuentro gloriosamente atrapado contra el árbol."

show emicas smile_up_close
with charachange

emi "Como asegurarme de que esta es una verdadera cita, ¿cierto?"

show emicas closedsmile_up_close
with charachange

emi "Quiero decir, si no nos besamos entonces no es para nada una cita, ¿cierto?"


hi "Supongo qu— mmmff." with vpunch

"Fresas y curry. No es la mejor combinación, pero no creo que importe."

show emicas grin
with charadistant

"Emi se sienta en mis piernas y sonríe de nuevo."

emi "Ahí. La ciencia lo aprobaría, ¿cierto?"

"Tengo la extrañísima imagen mental de Mutou asintiendo seriamente y haciendo una marca en alguna lista de verificación."

"No puedo evitar reírme de la idea."

show emicas neutral
with charachange

emi "Bueno lo admito, esta es la primera vez que veo un beso terminar en una carcajada."

emi "¿Debería de sentirme ofendida?"

hi "Jeje, no, no."

hi "Estoy seguro de que la ciencia lo aprueba."

show emicas happy_up
with charachange

"Emi me sonríe radiante, y cada vez me parece más difícil mantener a mi cerebro funcionando adecuadamente."

emi "¡Oh, bien!"

"Es en este momento cuando noto que Emi ha robado el resto de mi pan de curry mientras yo estaba ocupado por otro lado con imágenes de maestros sosteniendo portapapeles."

hi "¡Oye!"

show emicas blush
with charachange

"Emi intenta verse inocente, pero, considerando que acaba de atiborrarse los últimos pedazos de mi pan en la boca, no parece estar funcionando."

emi "¿Mmff? Ferdón, no fude refisftir."

hi "¡Ladrona!"

show emicas neutral
with charachange

"Un encogimiento de hombros de mi acompañante es todo lo que recibo como respuesta."

hi "¡Usaste tu encanto femenino en mí!"

"Igual no tenía tanta hambre, pero aun así siento que debo hacer el comentario."

show emicas pout
with charachange

"Emi parece confundida por la frase “encanto femenino”, pero la comprensión ilumina sus rasgos luego de unos momentos de reflexión."

show emicas angry_up
with charachange

emi "¡No tuvo nada que ver con eso!"

show emicas frown_up
with charachange

emi "¡Te estabas riendo! ¡Si usara mi encanto femenino no te reirías!"

"Supongo que no puedo rebatir eso."

hi "Eso no cambia tu robo."

show emicas happy
with charachange

"Emi se ríe de mi tono afligido y me da un golpecito juguetón."

show emicas closedsmile
with charachange

emi "Bien, puedes quedarte con los fideos instantáneos."

hi "¿Estás bromeando? ¡Esas cosas son horribles!"

hi "¡En todo caso, deberías comértelos como castigo!"

show emicas wink
with charachange

"Otra carcajada de la chica sentada en mis piernas."

"… Las cuales ya se han dormido."

show expression im.Composite((295,1200), (0,0), "sprites/emicas/emicas_wink.png") as emicas:
    xalign 0.5 yanchor 0.5 ypos 1.13 subpixel True
    easeout 0.8 rotate -90
with None

show expression im.Composite((295,1200), (0,0), "sprites/emicas/emicas_blush.png") as emicas:
    xalign 0.5 yanchor 0.5 ypos 1.13 subpixel True
    easeout 0.8 rotate -90

with Dissolve(0.2)
with Pause(0.6)

hide emicas
with vpunch

"Retuerzo una pierna intentando despertarla, lo que tiene el indeseado efecto de desbalancear a Emi, quien cae de lado con un asustado ¡“Ayy”!"

hi "¡Oops! Disculpa."

hi "Se me durmieron las piernas."

"Emi se queda en el suelo, riéndose infantilmente."

"Me levanto algo tembloroso, sintiendo los nervios de mis piernas regresar a la normalidad."

"Mis ojos vagan por el escenario hasta fijarse en la figura de Emi, que aún no se ha levantado."

scene ev emi_parkback:
    xalign 0.5 yalign 0.5 zoom 1.1 subpixel True
    ease 10.0 zoom 1.0
with locationchange

"Su cabello está extendido alrededor de su cabeza, sus brazos abiertos, y la risa borbotea en su boca."

"Todo sobre Emi parece estar condensado en esta imagen."

"Su energía, su espíritu, sus risas infantiles."

"La urgencia de acostarme en el césped con ella acelera rápidamente desde el fondo de mi mente hasta el primer plano de mis pensamientos, y realmente estoy convencido de que nada me gustaría más que hacer eso."

"Desafortunadamente el sol se ha ocultado, y probablemente sea tiempo de que regresemos a los dormitorios."

"Mientras Emi podría ser feliz quedándose aquí afuera toda la noche, no creo que yo tenga esa capacidad."

"Además, la tarea me espera."

"No tendría sentido empezar a considerar cosas como la universidad y luego aflojar el ritmo, ¿verdad?"

"Extiendo una mano para ayudar a Emi a levantarse."

hi "Probablemente deberíamos irnos."

show ev emi_parkback_frown
with charachange

"Emi pone una mueca de irritación."

emi "Tienes razón."

scene bg suburb_park
with locationchange

show emicas weaksmile_close:
    center
    ypos 1.2
    easein 0.5 ypos 1.0
with charaenter


"Ella toma mi mano extendida, y la traigo sobre sus pies y hacia un abrazo."

"Esta vez soy yo el que la beso, incapaz de resistir el tener a Emi contra mí."

hi "Sería una lástima irse, sabes."

show emicas closedsmile_close
with charachange

emi "Sí, lo sería."

show emicas grin_up_close
with charachange

emi "Pero si no volvemos pronto a la escuela, probablemente nos metamos en problemas."

"Emi me da un golpecito travieso en las costillas."

show emicas wink_up_close
with charachange

emi "Y tú necesitas hacer la tarea, estoy segura."

hi "Desgraciadamente, tienes toda la razón."

hide emicas
with charaexit

"Pongo mi brazo sobre sus hombros, y caminamos el trayecto de vuelta a la escuela, acompañados por ocasionales episodios de risa mientras nuestra conversación salta de un tema a otro."

"Todo desde correr, hasta la escuela, hasta la peculiar manera en la que huele uno de los empleados de la cafetería."

stop ambient fadeout 2.0

scene bg school_dormext_full
with locationskip

"Y así, muy repentinamente nos encontramos fuera del edificio del dormitorio de las chicas."

show emicas closedsmile at center
with charaenter

emi "Bueno, supongo que me voy, entonces."

hi "Supongo, ¿eh?"

show emicas grin_up
with charachange

"Emi me sonríe de nuevo con esa mirada traviesa."

emi "¿Serás capaz de sobrevivir sin mí?"

"Me río."

hi "Estoy seguro de que me las arreglaré."

show emicas pout_up
with charachange

emi "¡Qué horrible! ¿No se supone que digas algo como “estaré contando los segundos que estés lejos”?"

hi "Nah, no lo creo."

show emicas closedsmile_close
with characlose

show emicas weaksmile
with charadistant

"Emi me jala hacia un rápido beso de despedida y da un paso atrás, viéndose inesperadamente tímida."

emi "Gracias por la cena."

emi "Realmente me divertí."

show emicas closedsmile
with charadistant

emi "En serio, lo hice."

hi "Igual yo."

hi "Creo que tendremos que hacerlo de nuevo, en algún momento."

show emicas happy
with charadistant

"Emi se ríe de mi inexpresivo comentario y asiente."

emi "Te veo temprano mañana por la mañana, ¿verdad?"

show emicas wink
with charadistant

emi "Tienes que quemar ese pan, después de todo."

hi "Claro. A pesar de que tú te lo comiste casi todo."

show emicas smile_up
with charadistant

emi "Sí, a pesar de eso."

show emicas grin_up
with charadistant

emi "¡Te veo luego, Hisao!"

stop music fadeout 3.0

show emicas invis:
    xpos 0.6
with dissolvecharamove

hide emicas
with None

"Cuando Emi se da la vuelta para entrar, noto algo extraño."

"Algo tan extraño que estoy sorprendido de no haberlo notado antes."

"Ella cojea levemente, favoreciendo la pierna izquierda."

play music music_pearly fadein 8.0

hi "¡Oye, Emi!"

show emicas invis at tworight
with None

show bg school_dormext_full at bgleft
show emicas neutral at center
with dissolvecharamove

emi "¿Hmm?"

hi "¿Está bien tu pierna?"

show emicas awayfrown
with charachange

"Emi se ve confundida, o al menos finge confusión."

show emicas frown
with charachange

emi "¿De qué estás hablando?"

hi "Tu pierna derecha. Estás cojeando."

show emicas blush
with charachange

show emicas frown
with charachange

"Hay un brevísimo destello de preocupación en el rostro de Emi."

"O ella no quería que yo supiera, o creyó que no me daría cuenta… o, preferiría creer, simplemente no se había dado cuenta."

show emicas neutral_up
with charachange

emi "Oh, eso."

"Ella se encoge casualmente de hombros."

show emicas awayfrown
with charachange

emi "Debe de haberse desacomodado un poco durante el picnic."

show emicas wink
with charachange

emi "Ni idea de qué podría haberlo ocasionado, por supuesto."

"Retrocedo mis pensamientos hasta estar atrapado bajo el árbol."

hi "Oh."

hi "¡Deberías habérmelo dicho! Podríamos habernos detenido y arreglarlo, sabes."

"Emi sacude una mano despreocupadamente."

show emicas smile_up
with charachange

emi "Nah, no es para tanto."

show emicas weaksmile_up
with charachange

emi "No te preocupes por eso, ¿de acuerdo, Hisao?"

show emicas closedsmile_up
with charachange

emi "Está bien."





label es_choiceE17:
menu:
    with menueffect
    "¿Por qué tengo la sensación de que ella se está convenciendo a sí misma tanto como a mí?"
    "Presionar a Emi.":


        return m1
    "Dejarlo pasar.":

        return m2


label es_E17a:


hi "¿Estás absolutamente segura?"

hi "¿No quieres ajustarlo antes de empezar a subir las escaleras?"

hi "Podrías lastimarte si no lo haces, ¿cierto?"

show emicas awayfrown_up
with charachange

emi "Dije que estaba bien, Hisao."

show emicas frown
with charachange

emi "En serio, no te preocupes por eso."

show emicas weaksmile
with charachange

emi "Tengo algo de experiencia en estos asuntos, después de todo."

hi "Sí, supongo que sí."

"Emi sonríe tranquilizadoramente."

show emicas grin
with charachange

emi "Honestamente, Hisao, aprecio la preocupación pero realmente estoy bien."


label es_E17b:


"Bueno, ella probablemente está bien."

"Imagino que diría algo si hubiera un verdadero problema."

"Y con un demonio, probablemente se molestaría si continúo sacando el tema."


label es_E17x:

show emicas smile
with charachange

emi "Ahora en serio, necesito irme."

show emicas wink_up
with charachange

emi "¡Tus intentos de mantenerme aquí están condenados al fracaso!"

hi "Jeje, por supuesto."

hi "Solo prolongaba la despedida, supongo."

"Otra sonrisa ilumina el rostro de Emi."

show emicas happy_up
with charachange

emi "Buenas noches, Hisao."

hi "Buenas noches."

hide emicas
with charaexit

stop music fadeout 5.0

"Mientras ella entra cojeando, espero que realmente esté bien, a pesar de sus intentos de convencerme de que lo está."

"Creo que puedo llamar a esta una primera cita exitosa."

"Diablos, cualquier día que termine con Emi arrinconándome bajo un árbol para besarme no puede ser malo, ¿verdad?"

"Me dirijo de vuelta a mi habitación, agradezco mentalmente a los dioses que Kenji no me emboscó en el pasillo, y empiezo con mi tarea."

scene black
with dissolve




label es_E18:

scene bg school_dormhisao
with locationchange

play music music_night fadein 5.0

"La mañana llega demasiado temprano para mi gusto."

"Y no ayuda haber tenido problemas para dormir anoche."

"Simplemente había demasiadas cosas en las que pensar. Mi cerebro no quería descansar."

"En vez de eso, repetí lo de la azotea, el parque, y todo lo demás una y otra vez en mi mente."

"Hay una pequeña parte de mi mente que aún está paranoica con que todo esto ha sido alguna especie de broma."

"Que me encontraré con Emi en la pista, y ella actuará como si no hubiera pasado nada ayer."

"Empujando estos pensamientos hasta el fondo de mi mente, me pongo la ropa para correr y abro la puerta."

scene bg school_track
show emi basic_grin_gym at center
with locationskip

"Emi está esperándome con su sonrisa habitual."

show emi basic_annoyed_gym
with charachange

emi "¡Llegas tarde!"

show emi basic_closedgrin_gym
with charachange

emi "O al menos no llegaste temprano hoy."

show emi excited_hesitant_gym
with charachange

emi "¿Estás cansado o algo?"

"Me froto tristemente la parte trasera de la cabeza."

hi "Sí, algo así."

hi "Mucho en lo que pensar y todo eso."

show emi basic_closedgrin_gym
with charachange

"Emi se ríe con mi leve indirecta."

show emi basic_grin_gym
with charachange

emi "Sí, yo tampoco dormí muy bien."

show emi excited_proud_gym
with charachange

emi "La verdad me alegra que no hayas llegado temprano, porque yo tampoco lo hice."

"Me pregunto si lo mismo nos mantuvo despiertos."

"La imagen de su rostro lleno de lágrimas pasa por mi mente."

hi "¿Qué te mantuvo despierta?"

show emi sad_shy_gym
with charachange

"La expresión de Emi se tambalea, pero nota mi curiosidad con rapidez y fuerza una sonrisa."

show emi sad_grin_gym
with charachange

emi "Nada importante."

"Obviamente no está diciéndome algo."

"La pregunta es, ¿debería de presionarla?"

"Claramente algo la ha estado molestando desde hace un tiempo."

"Quiero ayudarla, pero, ¿parecería que solo soy un entrometido?"

"Aun así, debería de saber que me preocupo por ella."

hi "¿Estás segura?"

hi "Si algo te molesta, estoy aquí para ayudarte a resolverlo."

show emi basic_closedhappy_gym
with charachange

"Emi entonces se ríe, pero no es la risa de siempre. Tiene un tono que parece casi amargo."

show emi sad_grin_gym
with charachange

emi "¿Resolverlo?"

emi "No estoy segura de que pueda resolverse, Hisao."

"Una sonrisa casi siniestra cruza sus labios."

"Es como una sonrisa de resignación."

show emi sad_pout_gym
with charachange

emi "Y no creo que puedas ayudarme, de todas maneras."

"Eso duele."

"No quiero decirle que me duele, pero lo hace."

"¿No se da cuenta de que quiero estar ahí para ella cuando las cosas anden mal?"

hi "Bueno, no te presionaré con eso."

hi "Pero estoy aquí para ti si luego decides que te gustaría hablarlo."

hi "Podría ayudar."

show emi sad_shy_gym
with charachange


"Puedo ver el furioso debate tras los ojos de Emi."

"Parece que quiere contármelo, pero no está segura de si puede hacerlo o no."

hi "Oye, olvídate de ello por ahora, ¿de acuerdo?"

hi "Tenemos que correr."

"Con la mención de correr, algo que puede controlar, Emi regresa a ser la misma de siempre."

show emi basic_closedhappy_gym
with charachange

emi "¡Cierto!"

show emi basic_grin_gym
with charachange

emi "¡Apresúrate y estira, Hisao!"

show emi excited_proud_gym
with charachange

emi "¡Tenemos que empezar a movernos!"

play ambient sfx_emipacing

hide emi
with easeoutleft

stop ambient fadeout 3.0

"Ella sale disparada, mucho más rápido de lo que estoy acostumbrado."

scene bg school_track_on
with locationchange

scene bg school_track_running
with Dissolve(2.0)

"Aun así, intento mantener su ritmo, probando tercamente mis límites."

"Eso me deja una sensación de libertad, como si mi corazón ya no importara más."


"Me dan ganas de reír, lleno de la sensación de moverme afuera de lo que una vez llamé mis límites."

"Las advertencias del enfermero de no pasarme de la raya hacen eco en mi cabeza, y yo las ignoro."

"Esta sensación que tengo, esta disposición a arriesgar un ataque cardiaco por algo tan trivial como una carrera matutina, se siente atípico de mí."

"Pero, ¿lo es?"

"O más bien, ¿debería de serlo?"

"Tengo un corazón débil, claro."

"Uno que nunca será capaz de tener la velocidad ni la resistencia que tiene el de Emi."

"Pero probablemente yo no sería capaz de llegar a ser tan bueno aun teniendo un corazón saludable."

stop music fadeout 6.0

"Mientras cruzamos el último recodo, siento mis piernas gritando en protesta, pero, por primera vez, las ignoro."

"Acelero para terminar con un sprint, casi alcanzando a Emi."

"Eso nunca iba a pasar, por supuesto."

"Aun así, me siento sorprendentemente bien."

"Oh, claro, siento como si mis piernas estuvieran a punto de prenderse fuego, y estoy teniendo problemas para mantenerme derecho."

"Pero ha habido una especie de cambio hoy."

"Y es todo gracias a la chica sonriendo en la línea de meta, esperando por mí."

scene bg school_track_on
show emi basic_grin_gym at center
with locationchange

play music music_emi fadein 1.0

hi "Eso se sintió un poco más rápido de lo habitual."

"Mi comentario es recibido con una sonrisa y un encogimiento de hombros."

show emi excited_proud_gym
with charachange

emi "No puedo dejar que pienses que voy a ser blanda contigo, ¿no?"

show emi basic_closedgrin_gym
with charachange

emi "Pero te las arreglaste para superarlo sin problemas."

hi "Bueno, no podría haberlo hecho sin ti."

show emi basic_confused_gym_close
with characlose

"Todavía sintiendo el éxtasis de la carrera y motivado por una oleada de gratitud, atrapo a Emi en un abrazo."

hi "Gracias."

hi "En serio, no lo digo por decirlo."

hi "Estoy en deuda contigo."

show emi basic_hes_gym_close
with charachange

"Emi parece agitada por mis palabras, retorciéndose con incomodidad."

emi "No seas tonto, Hisao."

show emi basic_grin_gym_close
with charachange

emi "Alguien tenía que arrastrarte hasta acá afuera, ¿verdad?"

show emi basic_closedgrin_gym_close
with charachange

emi "Y no es como si tú no estuvieras haciendo nada por mí, ¿cierto?"

show emi basic_grin_gym_close
with charachange

emi "Necesitaba un compañero para correr, ¿recuerdas?"

show emi basic_shock_gym_close
with charachange

"Sacudo la cabeza, todavía sin ninguna intención de dejar ir a Emi, quien deja de retorcerse y se limita a mirarme desde abajo con un rubor que se intensifica rápidamente y que casi parece impropio de ella."

hi "No, eso no es verdad."

hi "Querías un compañero para correr, pero no necesitabas uno."

hi "Si no me hubiera presentado el día después del festival, aún seguirías corriendo, ¿cierto?"

hi "Pero no funciona al revés."

hi "Solo conseguí hacerlo unas pocas veces antes del festival."

hi "Y sin ti, probablemente no habría conseguido hacer nada después de eso."

show emi basic_closedgrin_gym_close
with charachange

"Emi me sonríe y me clava un dedo en el pecho."

show emi excited_proud_gym_close
with charachange

emi "Eres bastante perezoso, Hisao."

hi "¡Oye, yo te estaba halagando!"

show emi sad_grin_gym_close
with charachange

emi "Bueno… de nada, supongo."

hi "Te lo recompensaré de algún modo."

show emi basic_hes_gym_close
with charachange

emi "Oh, uh, bueno…"

show emi basic_closedgrin_gym_close
with charachange

emi "Sabes, eso no es necesario."

show emi basic_happyblush_gym_close
with charachange

emi "Digo, me gustas un poco, Hisao."

show emi sad_grin_gym_close
with charachange

emi "Y poder correr contigo en las mañanas no es exactamente un mal trato para mí, así que…"

"Para alguien que recibe tantas alabanzas, ella no parece acostumbrada a la gratitud."

"No puedo pensar en nada más que decir, así que nos quedamos en silencio."

"Me vuelvo consciente de la respiración de Emi, de la humedad de su ropa, y de su olor."

"Viniendo de alguien más, apestaría."

"Viniendo de Emi, se ajusta a ella de una forma única."

"Su piel está fría, cubierta de sudor, y una brisa le provoca escalofríos."

show emi excited_amused_gym_close
with charachange

"Casi sin pensarlo, me inclino y me encuentro con la boca de Emi que ya se ha movido para encontrarse con la mía."

"Sus labios son suaves, y ella ronronea felizmente mientras nos besamos, enviando vibraciones de su boca a la mía."

"Hay una alarmante exactitud en este momento. Encajamos el uno con el otro a la perfección."

show emi basic_grin_gym_close
with charachange

"El beso termina, y finalmente dejo caer mis brazos a mis costados."

show emi basic_closedgrin_gym_close
with charachange

"Emi está sonriéndome cálidamente, y suelta una risita de nuevo."

show emi basic_closedhappy_gym
with charadistant

emi "Vamos, Hisao, será mejor que veamos al enfermero."

stop music fadeout 1.0

"Entonces ocurre."

show emi basic_closedhappy_gym:
    ease 0.25 ypos 1.05
    ease 0.25 ypos 1.0
with None

show emi excited_sad_gym:
    ease 0.25 ypos 1.05
    ease 0.25 ypos 1.0
with Dissolve(0.25)

"Cuando ella se da vuelta para caminar, suelta un pequeño quejido y tropieza hacia adelante."

hi "¡Emi!"

play music music_rain fadein 2.0

show emi excited_sad_gym_close
with characlose

"Salto hacia adelante para estabilizarla y noto con algo de preocupación que está favoreciendo a la misma pierna de ayer."

hi "Tu pierna…"

show emi basic_hes_gym
with charadistant

"Emi parece ser presa del pánico y me empuja para alejarse."

emi "¡Está bien!"

"Mi expresión debe verse dolida, porque se apresura en disculparse."

show emi basic_shock_gym
with charachange

emi "¡Perdón! ¡Perdón!"

emi "¡No quise empujarte así!"

show emi basic_closedsweat_gym
with charachange

emi "Solo estaba…"

"Ella tartamudea buscando algo que decir."

show emi sad_depressed_gym
with charachange

emi "No es nada, en serio."

hi "Oye, no te preocupes por eso."

"Ella está muy agitada, decido hacer de lado todo el asunto."

"Pero ahora hay una sensación gélida en el fondo de mi estómago que no se irá."

"Intenté acercarme y ayudarla, pero ella me empujó lejos."

"Sonriendo, entierro esos pensamientos en el fondo de mi mente y me concentro en Emi."

hi "Es solo que no quiero que te lastimes, nada más."

show emi sad_pout_gym
with charachange

emi "No tienes que preocuparte por mí, en serio."

show emi sad_grin_gym
with charachange

emi "¡Estoy bien!"

"Sí, tú dices eso, pero no te creo."


label es_E18a:


"¿Por qué no me dices qué anda mal?"

"Es como si la ofendieran mis intentos de ayudarla."

"¿Qué se supone que haga entonces?"


label es_E18b:


"A pesar de eso sigo preocupándome por ti, y no haber dicho nada ayer solo me hace sentir culpable por lo de hoy."

"Al menos debería haber preguntado."

"¿Habría reaccionado ella del mismo modo anoche?"

"Supongo que ya nunca lo sabré."


label es_E18x:

stop music fadeout 2.0

scene bg school_nursehall
with locationskip

"Aún estoy intentando superar lo que ocurrió en la pista cuando llegamos frente a la oficina del enfermero."

"Emi levanta su mano para tocar, vacila y se vuelve hacia mí con una sonrisa de culpabilidad."

show emi sad_grin_gym:
    yalign 1.0 xanchor 0.5 xpos 0.47
    easein 0.5 center
with charaenter

emi "Oye, ¿me puedes hacer un favor?"

hi "Claro."

show emi excited_proud_gym at center
with charachange

emi "¿Puedes decirle al enfermero que lo veré más tarde?"

show emi basic_grin_gym
with charachange

emi "Acabo de recordar que tengo algunas… cosas de las que encargarme antes de clases."

show emi sad_grin_gym
with charachange

emi "Así que realmente necesito apresurarme."

show emi sad_shyblush_gym
with charachange

"La miro fijamente, y ella se inquieta bajo mi mirada."

"Sí, claramente está evitando al enfermero."

"Esa pierna suya…"

"Bueno, como sea. Dije que ayudaría, y así lo haré."

"Pero me aseguraré completamente de que vea al enfermero antes de que termine el día."

hi "Sí, de acuerdo. Le haré saber."

show emi excited_smile_gym
with charachange

"Emi se ve como si yo acabara de darle un poni para Navidad."

show emi excited_joy_gym
with charachange

emi "¡Muchísimas gracias!"

show emi excited_amused_gym
with charachange

emi "¡Eres el mejor, Hisao!"

show emi excited_amused_gym_close
with characlose

"Soy recompensado por mi complicidad en su mentira con un beso que hace que todo valga la pena, o eso me digo a mí mismo."

hide emi
with charaexit

"Mientras Emi sale del edificio, esforzándose por no evidenciar su cojera, toco la puerta de la oficina."

nk "Ah, Hisao. Entra."

play music music_nurse fadein 1.0

scene bg school_nurseoffice
show nurse neutral at center
with locationchange

nk "No veo a Emi contigo."

show nurse fabulous
with charachange

nk "No está enferma de nuevo, ¿o sí?"

"Por el tono de su voz, no creo que el enfermero esté esperando que yo diga “Sí, lo está”."

hi "Eh, ella dijo que olvidó hacer algo, entonces tuvo que irse, pero te verá más tarde."

show nurse concern
with charachange

"El enfermero suelta un suspiro de exasperación."

nk "En serio, esa chica…"

hi "¿Hmm?"

show nurse neutral
with charachange

nk "Me ha estado evitando."

nk "Ayer entró y salió de aquí sin siquiera quitarse sus prótesis. Y ahora esto."

"Bueno, al menos no soy el único al que Emi no quiere tener preocupado."

"Eso es… reconfortante, supongo."

"Aun así, siento que debería decir algo sobre su pierna. Dije que mentiría por ella, pero realmente necesita ver al enfermero."

hi "Ahora que lo mencionas, hoy estaba cojeando bastante."

hi "Y anoche también."

show nurse concern
with charachange

"Los ojos del enfermero se entrecierran con la palabra “anoche”."

nk "¿Y exactamente qué estaban haciendo ustedes dos anoche?"

hi "Estábamos eh, en una cita."

show nurse fabulous
with charachange

"El enfermero alza las cejas como si estuviera sorprendido."

nk "¿En serio? Interesante."

hi "¿Huh?"

show nurse neutral
with charachange

nk "Oh, nada."

"Su mirada se torna pensativa, y luego me sonríe."

show nurse grin
with charachange

nk "No crees que puedes usar algo de ese encanto de novio para hacer que ella venga a verme hoy, ¿o sí?"

hi "¡Claro!"

hi "Estaba pensando hacer eso de todos modos."

hi "Creo que está realmente lastimada y solo pretende no estarlo."

show nurse neutral
with charachange

nk "Hmm, sí. Ella hace eso."

nk "Teme que yo le ponga un alto a las carreras."

hi "¿Lo harías?"

show nurse concern
with charachange

nk "No me gusta, pero si es lo suficientemente malo como para que ella haya estado cojeando, bueno…"

nk "Supongo que tendré que ver cuál es el problema antes de hacer esa llamada."

hi "Ya veo."

"¿Emi sin permiso para correr? Que el cielo nos libre."

"No sé si ella podría seguir funcionando sin correr."

"Con razón es renuente a admitir que algo anda mal."

hi "Bueno, me aseguraré de que te vea."

show nurse neutral
with charachange

nk "Bien. Oh, y antes de que lo olvide…"

show nurse grin
with charachange

"Me sonríe de nuevo de una manera que se siente levemente amenazadora."

nk "No olvides que sé cuáles medicinas estás tomando."

show nurse neutral
with charachange

nk "Sé cuidadoso cuando estés con Emi, ¿entendido?"

"Guau. También se ve serio."

hi "Entendido."

hi "No lastimar a Emi. Ni lo soñaría."

show nurse grin
with charachange

nk "¡Grandioso!"

show nurse fabulous
with charachange


nk "No me gustaría ver que te pasaras."

hi "¿Huh?"

show nurse grin
with charachange

nk "Pasarte, en el sentido de “pasarte a mejor vida”."

show nurse concern
with charachange

"Él frunce el ceño por un instante, insatisfecho."

nk "Sonaba mejor en mi cabeza…"

show nurse neutral
with charachange

nk "Bueno, en fin."

show nurse grin
with charachange

nk "¡Vete de aquí antes de que pierdas tu primera clase!"

nk "Tienes cosas que hacer, estoy seguro. ¡Fuera!"

stop music fadeout 6.0

"Mientras me voy, noto cómo el enfermero saca su teléfono y marca un número."

show nurse concern
with charachange

nk "Meiko, tu hija me está dando dolores de cabeza otra vez…"

"Mejor me dirijo de vuelta a mi habitación, o en serio llegaré tarde."

"Oye, ¿no se supone que él tenía que revisar mi ritmo cardiaco?"



label es_E19:

scene bg school_scienceroom
with shorttimeskip

play sound sfx_normalbell

"Suena la campanada del almuerzo, y salgo del estupor en el cual caí durante las clases de la mañana."

"La falta de sueño de anoche, sumada al acelerado ritmo de la carrera de esta mañana, me ha dejado algo exhausto."

$ renpy.music.set_volume(0.15, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 1.0

scene bg school_staircase1
with locationskip

"A pesar de eso, estoy saltándome los escalones que van hacia la azotea."

"Ahora hay un entusiasmante suspenso, además del placer que tienes al comer con tus amigos."

play sound sfx_door_creak
$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

scene bg school_roof
with locationchange

"Cierto, Emi y Rin aún son mis amigas, pero Emi se ha vuelto más que eso."

"Rin está de vuelta en su lugar habitual en la azotea, casi como si nunca se hubiera ausentado."

scene ev rin_roof_boredom
show hisao rin_roof
with locationchange

hi "¿Supongo que te sientes mejor?"

show ev rin_roof_surprised
with charachange

"Una ceja levantada es mi recompensa por hablar."

rin "¿Mejor que cuándo?"

play music music_rin fadein 6.0

hi "Eh, mejor de lo que te sentías ayer."

show ev rin_roof_nonchalant
with charachange

"Rin le dedica a mi pregunta algo de seria reflexión."

rin "No estoy segura."

rin "Creo que pude haberme sentido bastante bien durante una parte de ayer, pero todo está borroso."

hi "¿Demasiada medicina para la gripe?"

show ev rin_roof_doubt
with charachange

rin "Bueno, estaba dormida. Y eso por lo general es bueno."

show ev rin_roof_boredom
with charachange

rin "Pero no puedo recordar cómo se siente estar dormida, porque no soy consciente de ello."

rin "Es un verdadero problema."

show ev rin_roof_nonchalant
with charachange

rin "Por otra parte, si supiera qué tan bien se sintió podría no volver a dormir más."

rin "Pero de esta forma sigo intentándolo, entonces supongo que así es como evito estar demasiado cansada."

hi "¿Un misterio eterno para mantenerte durmiendo por las noches?"

show ev rin_roof_boredom
with charachange

rin "Tal vez misterio es la palabra incorrecta. Intangibilidad podría ser la manera adecuada para describirlo."

hi "Ya veo."

"No, no lo hago, en absoluto. No tengo ni idea de lo que está hablando, pero está bien, dado que rara vez lo hago."

show ev rin_roof_doubt
with charachange

rin "¿Tú recuerdas cómo se siente dormir?"

rin "Ayer por ejemplo, ¿recuerdas cómo te sentías ayer al dormir?"

hi "Bueno, en realidad ayer no pude dormir mucho."

show ev rin_roof_nonchalant
with charachange

rin "Hmm."

rin "Tal vez es porque recuerdas inconscientemente."

hi "De hecho, creo que estaba preocupado por Emi."

show ev rin_roof_surprised
with charachange

rin "¿Acaso Emi no se preocupa lo suficiente por sí misma?"

"No había considerado eso, pero me detiene por un momento."

hi "Cierto, pero si ella necesitara ayuda, ¿la pediría?"

show ev rin_roof_doubt
with charachange

"Rin frunce el ceño, y yo levanto una ceja. ¿Recibiré una respuesta apropiada?"

rin "Probablemente no. ¿Hay algo por lo que ella debería estar pidiendo ayuda?"

hi "Su pierna, para empezar."

"Esto parece captar el interés de Rin."

show ev rin_roof_disgust
with charachange

rin "¿Pierna?"

hi "Está herida, pero no verá al enfermero por eso."

"Rin sacude la cabeza en desaprobación."

show ev rin_roof_doubt
with charachange

rin "Debes hacer que vaya."

show ev rin_roof_nonchalant
with charachange

rin "Como ella me hace ir a clases. Por su propio bien."

rin "O podría perder sus piernas de nuevo, y eso es demasiado raro."

rin "Perder cosas dos veces."

show ev rin_roof_doubt
with charachange

rin "Especialmente si no las encuentras antes, para empezar."

rin "A menos de que las prótesis sean lo mismo que encontrar algo."

show ev rin_roof_nonchalant
with charachange

rin "Pero esa es una pérdida diferente, ¿verdad?"

hi "Creo."

show ev rin_roof_boredom
with charachange

rin "Hmm. Me pregunto…"

stop music fadeout 0.5

show emi rin_roof
with charaenter

emi "¿Qué cosa?"

scene bg school_roof
show emi basic_grin at center
with locationchange

"Emi parece haberse escabullido hasta nosotros, aunque Rin no parece especialmente sorprendida. Lo que en sí mismo es poco sorprendente, supongo."

show bg school_roof at bgleft
show emi basic_grin at twoleft
with charamove

show rin basic_deadpannormal:
    tworight
    ypos 1.25
    easein 0.5 ypos 1.2
with charaenter

"Rin se las arregla para ponerse de pie con bastante pericia, empujando la parte superior del cuerpo hacia adelante y utilizando el impulso para enderezarse."

show rin basic_absent:
    ypos 1.2
with charachange

hi "Tu pierna. ¿Cómo está?"

show emi sad_annoyed
show rin basic_awayabsent
with charachange

"Eso me gana un ceño fruncido y una breve mirada feroz."

emi "Está bien, creo."

show emi sad_shy
with charachange

emi "No vale la pena preocuparse por eso."

show rin basic_absent
with charachange

hi "Díselo al enfermero."

hi "Insiste en que lo visites, sabes."

show emi sad_pout
show rin basic_awayabsent
with charachange

"Emi hace pucheros como si yo acabara de decirle que está castigada."

emi "Él se preocupa demasiado."

show emi basic_grin
with charachange

emi "No es gran cosa, solo un poco de inflamación."

"Intento resistir poner los ojos en blanco por la exasperación."

show rin basic_absent
with charachange

hi "Si no es nada, entonces no deberías tener ningún problema en ir a verlo, ¿cierto?"

show emi basic_annoyed
show rin basic_awayabsent
with charachange

"Emi entrecierra los ojos con sospecha."

emi "¿Él te metió en esto?"

show rin basic_absent
with charachange

hi "Bueno, tal vez. Un poco."

hi "Pero ese no es el punto. Te habría recordado que fueras a verlo de todos modos."

hi "Sería horrible ver cómo estando realmente herida no haces nada al respecto."

hi "Eso lo haría peor, y realmente no quiero verte herida, ¿sabes?"

hi "Llámame loco, pero creo que prefiero verte sana y feliz."

show emi sad_grin
show rin basic_awayabsent
with charachange

"Con cada línea, el ceño de Emi se desvanece un poco, hasta que eventualmente está sonriendo, aunque con algo de timidez."

play music music_daily fadein 4.0

emi "Bueno, si lo vas a poner así, entonces supongo que tendré que verlo."

show emi excited_proud
with charachange

emi "O continuarás preocupándote, y entonces será un cuento de nunca acabar, ¿no?"

show rin basic_absent
with charachange

hi "Correcto. Seguiré insistiendo, y eso podría arruinar nuestras citas."



hi "“¿Cómo está la comida, Hisao?” “Habla con el enfermero, Emi”."

hi "“¿Cómo estuvo tu día, Hisao?” “Habla con el enfermero, Emi”."

hi "“Hisao, creo que estoy lista para que m—” “{b}Habla con el enfermero, Emi{/b}”."

hi "¿Ves? No funciona muy bien."

show emi basic_closedhappy
show rin basic_awayabsent
with charachange

"Emi se ríe infantilmente con mi chillona interpretación de su propia voz y me da un empujón cariñoso."

show emi excited_amused
with vpunch

emi "Mi voz no es tan aguda, idiota."

show rin basic_deadpan
show emi excited_circle
with charachange

rin "Yo creo que fue bastante acertada."

with Pause(3.0)

"Emi y yo observamos a Rin por unos instantes antes de echarme a reír."

show emi sad_annoyed
show rin basic_awayabsent
with charachange

"Emi cruza sus brazos y resopla, fingiendo estar ofendida."

show emi sad_angry
with charachange

emi "Los dos son unos idiotas."

show rin basic_absent
with charachange

hi "Tales calumnias viles provenientes de ti, joven dama."

hi "Estoy sorprendido de que me llames, entre todas las personas, un idiota."

hi "Honestamente, simplemente… no sé qué pensar."

show emi basic_annoyed
show rin basic_awayabsent
with charachange

"Emi me saca la lengua."

emi "Imbécil."

show emi basic_grin
with charachange

emi "Entonces, Rin, ¿qué tal el club de arte estos días?"

show rin basic_surprised
with charachange

"Rin, viéndose tan sorprendida como yo por este repentino cambio de tema, se toma un minuto para pensar antes de responder."

show rin basic_lucid
with charachange

rin "Creo que está bien."

show rin basic_deadpancontemplation
with charachange

rin "Aunque Nomiya sigue diciéndome que trabaje más duro."

show rin relaxed_nonchalant
with charachange

rin "Pero no creo que entienda mis métodos."

show emi sad_annoyed
with charachange

emi "Él siempre me ha parecido algo escalofriante."

show rin basic_lucid
with charachange

"Rin sopesa esta declaración por un instante."

show rin basic_awayabsent
with charachange

rin "Nunca lo noté."

show rin basic_deadpancontemplation
with charachange

rin "Pero no le presto mucha atención la mayor parte de los días, así que tal vez sea eso."

hi "¿Qué tan seguido se encuentran?"

show emi basic_closedgrin
with charachange

emi "¿Piensas unirte, Hisao?"

show rin basic_absent
with charachange

hi "¿Qué? Nah, ya he decidido unirme a un club."

show emi excited_happy
show rin basic_awayabsent
with charachange

emi "¿En serio? ¿Cuál?"

show rin basic_absent
with charachange

hi "Bueno, no es realmente un club, para ser honesto…"

show emi excited_proud
show rin basic_awayabsent
with charachange

emi "Oh, ¿te uniste al club del té?"

show rin basic_absent
with charachange

hi "No, yo, eh… me uní al club de ciencia… creo."

show emi basic_confused
show rin basic_awayabsent
with charachange

"Emi se ve muy confundida."

emi "¿Tenemos un club de ciencia?"

show rin basic_absent
with charachange

hi "Eh, no realmente. Solo soy yo."

show emi basic_closedhappy
show rin basic_awayabsent
with charachange

emi "Hisao, eso no es un club. Eso es sentarte en tu habitación a leer libros."

hi "No, quiero decir, solo somos Mutou y yo."

hi "Soy el único estudiante hasta este momento."

show emi basic_confused
show rin basic_lucid
with charachange

emi "¿Mutou? ¿En serio?"

"La asalta un pensamiento."

show emi basic_happy
with charachange

emi "Oh, ¿de eso estabas hablando ayer? ¿Tu reunión con Mutou?"

hi "Sí, esa fue nuestra primera reunión, supongo."

show emi basic_closedgrin
with charachange

"Emi suelta una risita."

show emi basic_grin
with charachange

emi "Nerd."

hi "Oye, no puedo evitar ser listo."

show emi excited_proud
with charachange

emi "Sabes, podría haber usado tu ayuda hace unos años."

emi "Deberías de haber sufrido tu ataque al corazón más joven, Hisao."

"Me río, y luego me doy cuenta de que es probablemente una de las muy raras ocasiones en las que me he reído de mi ataque cardiaco."

hi "En retrospectiva…"

show emi sad_grin
with charachange

emi "Sí…"

play sound sfx_warningbell

"El sonido de la campana finaliza nuestra conversación."

hi "Hmm, creo que mejor nos vamos."

show emi basic_grin
with charachange

emi "Sí, supongo que sí."

show emi excited_amused:
    xpos 0.45
with dissolvecharamove

emi "Vamos, Rin, tú también."

show rin basic_surprised
with vpunch

"Al parecer Rin ha empezado a dormitar, así que Emi le da un sonoro golpe."

show rin basic_deadpanupset
with charachange

rin "Casi lo tenía."

show emi basic_closedgrin
with charachange

emi "Perdona, pero tienes que ir a clases."

show rin relaxed_nonchalant at tworight
with dissolvecharamove

rin "No opino lo mismo, pero tal vez si duermo en clases lo conseguiré."

show rin relaxed_boredom
with charachange

rin "Cambiar de lugar a veces es útil para esa clase de cosas."

"Ni Emi ni yo nos preocupamos en preguntar qué cosas son."

stop music fadeout 3.0
stop ambient fadeout 2.0
scene bg school_hallway3
with locationskip

"Cuando llegamos a mi aula, Emi me da un beso rápido y se va por el pasillo, Rin remolcada detrás."

show shizu behind_blank:
    tworight
    xpos 0.8
    easein 0.5 tworight
show misha perky_smile:
    twoleft
    xpos 0.2
    easein 0.5 twoleft
with charaenter

"Me vuelvo para entrar al aula, y me encuentro con el dúo de Shizune y Misha."

play music music_shizune fadein 1.0

show shizu adjust_happy
with charachange

shi "…"

"Misha parece estar luchando una batalla perdida para evitar romper en un ataque de risa mientras traduce el último arranque de Shizune."

show misha hips_grin
with charachange

mi "Aun si estamos encantadas, y hasta emocionadas, de ver lo bien que te las has arreglado para hacer nuevos amigos y forjar relaciones —y con semejante lindura también, Hicchan~…"

"Creo que la última parte fue probablemente Misha."

show shizu basic_normal
with charachange

shi "…"

show misha hips_frown
with charachange

mi "No obstante, nos sentimos obligadas a recordarte amablemente que por la sección ocho del código de conducta establecido en el manual del estudiante:"
mi "Las muestras públicas de afecto están estrictamente prohibidas —¿en serio? Eso es decepcionante, Shicchan."

show shizu adjust_smug
with charachange

shi "…"

show misha sign_smile
with charachange

mi "En este caso, sin embargo, la ignorancia de la ley puede ser tu excusa, ya que nos sentimos clementes…"

show shizu behind_smile
with charachange

shi "…"

show misha hips_smile
with charachange

mi "… Y el papeleo requerido para castigarlos a ambos solo se sumaría al ya colosal volúmen de trabajo que nos confronta, a los únicos miembros del consejo estudiantil, además, ¡ustedes dos son adorables juntos~!"

show shizu adjust_happy
with charachange

shi "…"

show misha hips_grin
with charachange

mi "Por consiguiente considera esto una advertencia formal, y por favor abstente de tales exhibiciones en el futuro. ¡Por lo menos cuando Shizune pueda verte, Hicchan~!"

"Todo este asunto es tan patentemente ridículo que no puedo evitar responder de la misma manera pomposa."

hi "Bueno, yo, por mi parte, me siento ilustrado."

hi "Me disculpo profusamente por mis imprudentes acciones y me esforzaré en contener mis instintivos impulsos que, me temo, me empujan hacia tan inapropiadas exhibiciones públicas de afección."

hi "Ni por asomo se me ocurriría agobiar a un consejo estudiantil que ya está sobrecargado de trabajo con tan insignificantes asuntos, y haré todo lo posible para facilitar sus vidas en este tema de ahora en adelante."

hi "Al menos cuando Shizune esté mirando."

"Esta última línea la acompaño con un guiño a Misha, quien finalmente pierde el control de su risa."

show misha cross_laugh
with charachange

mi "¡Guajaja~!"

show misha cross_grin
with charachange

mi "¡Bien dicho, Hicchan~!"

"Mientras me río entre dientes, entramos al aula."

stop music fadeout 2.0
scene bg school_scienceroom
with shorttimeskip

"La clase transcurre sin pormenores, y luego de que suena la campanada final, me encuentro de nuevo a solas con Mutou."

show muto smile at center
with charaenter

mu "Entonces, parece que estamos listos para la segunda reunión del club de ciencia."

play music music_another fadein 2.0
show muto normal
with charachange

mu "¿O es la primera? Qué piensas, ¿deberíamos de contar lo de ayer como una reunión?"

hi "Bueno, formamos el club ayer, ¿no es verdad?"

hi "Eso parece asunto del club, entonces sin duda podemos llamarla una reunión."

show muto smile
with charachange

"Mutou sonríe de forma torpe y rebuscada, como es típico de él. Me pregunto si los músculos de su cara no tienen la forma correcta como para dejarlo sonreír con naturalidad."

mu "Creo que realmente tienes un don para esto. Procesos de pensamiento lógico, eso es."

hi "¿Supongo?"

show muto normal
with charachange

mu "Un científico responde con autoridad, Hisao. La respuesta aquí es “Sí, lo hago”."

mu "Cuando el mundo quiere saber cómo funciona algo, les decimos. Incluso si todo lo que tenemos es una hipótesis decente."

show muto smile
with charachange

mu "Pero aun así debemos sonar seguros, porque somos las autoridades en el tema, ¿cierto?"

"Él se ríe entre dientes, acompañando a su incómodo chiste con su incómoda sonrisa. Hago todo lo posible por no hacer alguna mueca, pero creo que no estoy teniendo mucho éxito."

show muto normal
with charachange

mu "Eso es completamente falso, por supuesto."

mu "Sabemos mucho, claro, pero nadie es un experto en cómo funciona el mundo, aunque solo sea porque nadie puede estar seguro. Sin certeza, no hay expertos."

mu "Pero nos gusta pretender, a veces."

hi "Hay algunas cosas de las que podemos estar seguros, ¿cierto?"

mu "Sí… pero no."

mu "Sabemos que la gravedad está ahí, por ejemplo."

"Para ilustrar, Mutou levanta un lápiz y lo suelta."

mu "¿Ves? Aún está ahí. Pero es bueno revisar de vez en cuando."

mu "Es por eso que todavía verás investigadores curioseando con la gravedad."

show muto smile
with charachange

mu "Estamos bastante seguros de cómo funciona, pero siempre existe la posibilidad de que algo no sea como creemos que es."

mu "Así que revisamos, y revisamos, y revisamos. Eso es ciencia en pocas palabras, Hisao."

"Todo este tiempo he estado escuchando con cierto embelesamiento. Mutou parece estar realmente apasionado con estas cosas… creo. A veces es difícil decirlo."

"Cómo funciona el mundo…"

"Cómo funcionan los humanos."

"Cómo funciona el universo."

"Todas estas preguntas sin respuesta aún."

"Y, dependiendo de lo que decida, quizá hasta podría encontrar una manera de arreglar mi corazón. Con esto dicho, no creo que esa sea una verdadera prioridad para mí."

"Además, cuando empezamos a discutir el libro que me dio ayer, me encuentro más y más interesado en eso que en mi condición cardiaca."

show muto normal
with shorttimeskip

"Antes de darnos cuenta, ha pasado una hora."

mu "Bueno, terminaremos esta reunión por ahora, ¿de acuerdo?"

mu "Tendremos otra reunión… mañana, o eh… pasado mañana."

"Considera esto por un momento."

mu "Mejor pasado mañana. Tengo que poner un montón de notas."

hi "De acuerdo. Te veré entonces."

scene bg school_hallway3
with locationchange

stop music fadeout 5.0

"Mientras salgo del aula, me doy cuenta de que en realidad no tengo nada que hacer esta noche."

"Emi y yo no tenemos planes, así que…"

"Supongo que iré a la biblioteca. La verdad, es mejor que hacer la tarea en mi habitación."

scene black
with locationskip_in



label es_E20:

play music music_happiness fadein 2.0
scene bg school_library
with locationskip_out

"La biblioteca siempre parece más fresca que el resto del edificio."

"Probablemente para evitar que los libros se dañen por exceso de humedad y calor."

"Los libros son objetos robustos, pero requiere un pequeño esfuerzo mantenerlos en buen estado."

"Tengo varios libros que están tan gastados que las páginas apenas se sostienen del lomo."

"Parece imposible que todavía sean utilizables, pero si los manejas con cuidado…"

"Camino hacia el escritorio principal, donde veo a Yuuko ocupada con esto y aquello."

show yuuko neutral_up at center
with charaenter

"Me sonríe cuando entro y saluda con la mano."

show yuuko closedhappy_down
with charachange

yu "Hola, Hisao."

show yuuko happy_down
with charachange

yu "¡Es bueno verte de nuevo! ¿Qué estás buscando esta vez?"

hi "Nada en particular, supongo. Simplemente no quería regresar a mi habitación, es todo."

show yuuko neutral_down
with charachange

"Yuuko asiente."

show yuuko smile_up
with charachange

yu "Bueno, si estás desocupado, ¿tal vez podrías ayudarme a buscar algo?"

hi "Claro, ¿qué necesitas?"

stop music fadeout 5.0

show yuuko worried_up
with charachange

"Yuuko se lleva un dedo a los labios y mira alrededor furtivamente."

"Parece estar buscando espías."

yu "Acércate."

show yuuko worried_up_close
with characlose

"Doy unos pasos inseguros hacia adelante sintiéndome distintivamente nervioso."

"Yuuko baja su voz hasta un susurro confidencial."

show yuuko neutral_up_close
with charachange

yu "Estoy siguiéndole la pista al Gato Ladrón de Yamaku."

play music music_tension fadein 0.5

hi "¿Al qué?"

show yuuko panic_up_close
with charachange

yu "¡Shh! ¡Las paredes oyen, Hisao!"

yu "O podrían hacerlo."

show yuuko worried_down_close
with charachange

yu "¡Pero escucha! Esos libros perdidos, ¿los recuerdas?"

hi "Eh, ¿sí?"

show yuuko worried_up_close
with charachange

yu "Bueno, ¡no se perdieron! ¡Se los robaron!"

yu "¡Estoy convencida de ello!"

hi "Recuerdo que decías algo por el estilo antes, ¿pero cómo lo sabes?"

"Yuuko se acerca más y, si es posible, susurra más bajo."

show yuuko closedhappy_down_close
with charachange

yu "¡Porque encontré uno de sus escondites!"

hi "¿Que hiciste qué?"

"Yuuko se ve triunfante."

show yuuko happy_up_close
with charachange

yu "¡Encontré uno de sus escondites! ¡Estaba bajo uno de los escalones en el dormitorio de los chicos!"

yu "Tres libros que había estado buscando, ¡todos allí!"

show yuuko closedhappy_up_close
with charachange

yu "Sospechaba de un ladrón antes, ¡pero esto lo prueba!"

hi "¿Entonces tomaste los libros?"

show yuuko panic_up_close
with charachange

"Yuuko se ve como si yo acabara de sugerirle que camine desnuda."

yu "¿Estás loco?"

show yuuko worried_down_close
with charachange

yu "¡No puede saber que estoy tras él! ¡Podría escabullirse y evadir la captura!"

hi "A… já. Entonces, ¿para qué necesitas mi ayuda?"

"Yuuko lanza otra mirada hacia la biblioteca y se aproxima más."

show yuuko neutral_down_close
with charachange

yu "Tienes que espiar por mí."

hi "¿Espiar?"

yu "Sí, cuando estés en los dormitorios, ya sabes."

show yuuko closedhappy_down_close
with charachange

yu "Vigila cualquier actividad sospechosa."

"De todas formas, ¿qué constituye “sospechosa”?"

"Quiero decir, Kenji es un tipo bastante sospechoso, pero apostaría a que apenas asiste a clases, mucho menos entraría a hurtadillas a la biblioteca para robar libros."

"Aun así, ¿qué daño haría decir que sí? Al menos me sacaría de esta extraña conversación."

hi "Seguro, puedo hacer eso. Sin problema."

show yuuko closedhappy_down
with charadistant

"Yuuko se endereza y aplaude felizmente."

yu "¡Genial!"

show yuuko worried_down
with charachange

yu "Ahora, rápido, ¡habla de alguna otra cosa en caso de que alguien entre!"

stop music fadeout 2.0

show yuuko happy_down
with charachange

yu "¿Cómo te ha estado tratando la escuela?"

hi "Eh, bastante bien, en realidad."

hi "He estado corriendo por las mañanas con—"

show yuuko closedhappy_up
with charachange

yu "Emi Ibarazaki, ¿correcto?"

play music music_comedy fadein 2.0

hi "Uh, sí."

hi "¿Cómo sabes?"

show yuuko smile_down
with charachange

yu "Los atendí en la casa de té, ¿recuerdas?"

show yuuko closedhappy_down
with charachange

yu "Deduje que si ibas a correr con alguien, sería probablemente con ella."

"Se ve complacida consigo misma."

hi "Impresionante."

hi "De todas formas, sí. Hemos estado corriendo por las mañanas."

hi "Y eh, en algún momento empezamos a salir."

show yuuko closedhappy_up
with charachange

"Yuuko aplaude con emoción."

yu "¿En serio? ¡Eso es grandioso!"

yu "¡Apuesto a que ustedes dos se ven genial juntos!"

show yuuko neutral_down
with charachange

yu "Me encanta ver cómo las personas se encuentras las unas a las otras así, ¿sabes?"

yu "Incluso aquella vez cuando entraste en el Shanghái pensé, “me pregunto si ese chico terminará con alguna de esas chicas”."

hi "… ¿En serio?"

"Yuuko no parece notar mi tono de extrañeza y asiente afirmativamente."

show yuuko closedhappy_down
with charachange

yu "¡Síp! Estaba segura de que acabarías con una de ellas, sabes."

show yuuko neutral_down
with charachange

yu "Tengo buen ojo para este tipo de cosas."

show yuuko worried_down
with charachange

yu "Claro…"

"Su expresión decae ligeramente."

yu "No soy tan buena cuando se trata de mí misma."

hi "Oh, estoy seguro de que eso no es cierto."

show yuuko neutral_down
with charachange

yu "Sí, es cierto."

yu "Una vez conocí a un chico…"

show yuuko smile_down
with charachange

yu "Nos llevábamos realmente bien, pero resulta que era más joven que yo."

show yuuko neutral_up
with charachange

yu "Y eso era un poco raro, pero no terriblemente raro."

yu "Lo más raro es que un día desapareció, y no lo he visto desde entonces."

hi "Oh. Eso sí parece raro."

show yuuko worried_up
with charachange

yu "¿Verdad?"

show yuuko neurotic_down
with charachange

yu "Espero que no haya sido algo que yo hice…"

"Me siento obligado a tranquilizarla."

hi "Estoy seguro de que no lo fue."

stop music fadeout 4.0

$ renpy.music.set_volume(0.5, 0.0, channel="sound")
play sound sfx_phone
show yuuko panic_up
with vpunch

"Mi intención es calmarla un poco más, pero ambos saltamos de sorpresa por el repentino zumbido proveniente de mi bolsillo."

show yuuko worried_down
with charachange

"Yuuko suspira para calmarse mientras yo saco el teléfono de mi bolsillo. Me siento un poco avergonzado por haber causado el suceso indirectamente."

scene bg school_library_yuuko_blurred
show phone mobile:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with locationchange
with Pause (0.5)

hi "¿Emi? ¿Qué pasa?"

emi "Oh, gracias a Dios, no había llamado a tu número antes así que no sabía si funcionaría o si no contestarías y no podía—"

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play music music_pearly fadein 2.0

hi "Guau, Emi, tranquilízate."

hi "¿Qué sucede?"

"Hay una pausa al otro lado de la línea, durante la cual puedo escuchar a Emi tratando de controlar su respiración para calmarse."

"Algo la ha agitado terriblemente, y está empezando a agitarme a mí."

emi "Podrías solo…"

emi "¿Podrías pasarte por acá?"

emi "Algo así como, ¿ya? ¿O en un ratito?"

emi "En serio, en serio necesito hablar contigo."

"Hay un tono de súplica en su última oración que no creo haber escuchado nunca en ella."

hi "Claro, estaré allí enseguida."

hi "Quédate tranquila, ¿de acuerdo?"

"En mi creciente estado de agitación aparentemente he empezado a decir cosas que no tienen mucho sentido."

emi "De acuerdo. Estaré bien."

hi "Te veo pronto."

show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with None

scene bg school_library
show yuuko worried_down at center
show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with locationchange
with Pause (0.5)

hide phone
with None

with charaexit

"Presiono el botón para finalizar la llamada antes de deslizar el teléfono de vuelta en mi bolsillo, me disculpo con Yuuko por correr, y salgo corriendo."

scene bg school_girlsdormhall
with locationskip

"Tal vez en algún punto me habría detenido a pensar en la hora, o en qué tan sospechoso se vería un chico entrando al dormitorio de las chicas a esta hora."

"Excepto que justo ahora solo me preocupa ir con Emi y averiguar qué anda mal y cómo puedo ayudarla."

play sound sfx_doorknock2

"Toco la puerta y soy recibido con un suave “Entra”."

scene bg school_dormemi at left
with locationchange

"Algo está bastante mal cuando observo la escena frente a mí."

"Emi está ahí, sí."

"Pero está en silla de ruedas."

"Y sus piernas no están. Miro por la habitación y las veo en una esquina, parecen haber sido arrojadas allí."

show emiwheel weaksmile at center
with charaenter

"Emi reacciona cuando entro con una sonrisa torcida que se ve tanto complacida de verme como completamente, absolutamente descorazonada."

emi "Hola, Hisao."

"Parece que ha estado llorando, pero si lo hacía, ya se detuvo."

"Noto que estoy algo agitado, habiendo saltado escalones de dos en dos para llegar aquí."

"Sin embargo, mi corazón no parece preocuparse por la tensión. Archivo este agradable hecho para considerarlo más tarde."

"Como para cuando no esté mirando estupefacto a mi novia en silla de ruedas."

"Dándose cuenta de que aún no he respondido a su saludo, mi cerebro se enciende bruscamente."

hi "¿Emi? ¿Qué sucedió?"

show emiwheel pout
with charachange

emi "Supongo que debería haberte escuchado, Hisao."

show emiwheel sad
with charachange

emi "Mi pierna tiene una infección desagradable. No me permitirán correr por lo menos durante un par de semanas."

"Suelta una risa amarga que no debería provenir de ella."

show emiwheel frown
with charachange

emi "Je, ni siquiera puedo caminar."

emi "Podía haber usado una muleta y conservar una de mis piernas, pero no veo el punto."

show emiwheel awayfrown
with charachange

emi "¿Por qué cojear? No puedes correr con una pierna."

show emiwheel pout
with charachange

emi "Al menos de esta forma puedo, no sé, rodar más rápido o algo."

hi "S-sí, eso es bueno, ¿cierto?"

"Mi torpe intento de ver el lado bueno parece ser apreciado, pero no efectivo."

"Emi se encoge de hombros de nuevo."

show emiwheel awayfrown
with charachange

emi "Es solo… una molestia."

show emiwheel frown
with charachange

emi "Digo, ahora ni siquiera podemos comer en el techo. No tiene acceso para sillas de ruedas."

hi "Sí, pero eso no es gran cosa, ¿cierto?"

hi "Quiero decir, aún podemos comer juntos, y eso es lo que importa."

show emiwheel weaksmile
with charachange

"Esa sonrisa torcida de nuevo. Duele mirarla."

emi "Supongo que sí."

show emiwheel frown
with charachange

emi "Pero como dije, es una molestia."

show emiwheel awayfrown
with charachange

emi "Digo, no he usado una silla de ruedas en…"

stop music fadeout 10.0

"Lo piensa por un momento."

show emiwheel pout
with charachange

emi "¿Siete años quizá? En fin, algo así."

emi "Un largo tiempo."

show emiwheel weaksmile
with charachange

emi "Me temo que he perdido algo de práctica."

hi "Bueno, afortunadamente solo es temporal, ¿cierto?"

"Emi asiente."

show emiwheel neutral
with charachange

emi "Oh, sí, por supuesto."

emi "No es como si las hubiera perdido permanentemente."

show emiwheel awayfrown
with charachange

emi "Pero igual es un dolor de cabeza."

"Asiento comprensivamente."

"No hay mucho más que pueda hacer, después de todo."

"¿Qué voy a hacer? ¿Decir “te lo dije”?"

"Aunque {b}sí{/b} le dije que debían revisarle esa pierna."

"Pero cuando me di cuenta, ya era demasiado tarde."

hi "¿Necesitas ayuda con algo?"

hi "Eh, digo, ¿puedo ayudar con algo?"

show emiwheel closedsmile
with charachange

"Emi sacude la cabeza y vuelve un poco de su sonrisa habitual."

emi "Nah, me las puedo arreglar sola."

show emiwheel grin
with charachange

emi "Aunque si quieres ayudarme a alcanzar mi cama, me ahorrarías la molestia de rodar hasta allá por mí misma."

"Me sonrojo, a mi pesar."

"Emi suelta una risita."

play music music_heart fadein 0.5

show emiwheel wink
with charachange

emi "Eres un mojigato, Hisao."

hi "¡No lo soy! Solo que no me gustaría aprovecharme de una joven dama como tú."

hi "No es caballeroso."

hide emiwheel
with charaexit

show bg school_dormemi at right
with charamove

"Empujo la silla hasta la cama, alzo a Emi con facilidad y la dejo allí. Ella se acomoda con rapidez y se sienta en el borde."

show emi basic_grin:
    center
    ypos 1.0
    easein 0.5 ypos 1.1
with charaenter

"La verdad es que ella es un poco más pesada de lo que parece. Sería grosero de mi parte observar esto en voz alta, por supuesto."

hi "Vaya, eres bastante pesada."

play sound sfx_pillow
show comic vfx2
show emi excited_amused:
    center
    ypos 1.1
with hpunch

with Pause(0.5)

show comic vfx2:
    truecenter
    easeout 0.5 yanchor 0.3 alpha 0.0
with Pause(0.5)

"Emi me golpea con una almohada."

show emi basic_closedgrin
with charachange

emi "Idiota."

hi "Nada más lo decía, es todo."

hi "Debe ser por correr tanto."

show emi sad_shy
with charachange

"Al mencionar las carreras la sonrisa de Emi se tambalea un poco."

show emi sad_pout
with charachange

emi "Je, bueno, supongo que no tendré que preocuparme por eso durante un tiempo, ¿eh?"

show emi sad_grin
with charachange

emi "Tal vez pierda algo de peso."

hi "Eso es lo que haces para perder peso, ¿cierto? ¿Cesar la actividad física?"


show emi basic_closedgrin
with charachange

emi "Estoy segura de que eso es lo que recomendaría el enfermero."

hi "Hablando de eso, ¿aún irás por las mañanas?"

hi "No me gustaría correr so—"

show emi sad_depressed
with charachange

emi "Ah, mierda…"

"La repentina interjección de Emi, más un murmullo inquieto que algo muy profano, me obliga a mirarla, sorprendido."

"Ella está inclinada hacia adelante, intentando ocultar el hecho de que está llorando cubriéndose los ojos con una mano."

"Por supuesto, los suaves sollozos hacen que sea bastante evidente que está llorando."

hi "Oye, lo siento."

hi "Olvida todo lo que dije, ¿de acuerdo?"

show emi sad_depressed_close at center
with characlose

"Con cautela, coloco una mano a su alrededor y la atraigo más hacia mí."

"No puedo pensar en nada más que hacer o decir. ¿Cómo consuelas a alguien que acaba de perder sus piernas de nuevo?"

show emi sad_pout_close
with charachange

"Emi me atrapa en un abrazo y se queda así por un rato."

hi "Perdona."

hi "Creo que soy bastante malo consolándote."

emi "No digas eso."

emi "Estoy bien, en serio."

"Su voz resulta ligeramente amortiguada por mi pecho. Le doy unas palmaditas en la cabeza para animarla."

hi "Ese es el espíritu, ¿cierto?"

hi "Saldrás de esto sin problemas, lo sé."

hi "Además, estoy aquí para ayudarte, ¿recuerdas?"

show emi sad_shy_close
with charachange

"Emi levanta su cabeza y me mira con los ojos llenos de lágrimas."

show emi sad_grin_close
with charachange

emi "¿Puedes hacerlo? ¿En serio puedes hacerlo?"

"Ella está sonriendo torcidamente, y algo brilla en su mirada."

"No puedo saber si está bromeando o no."

hi "Claro. Digo, la verdad eres un poco pesada, pero—{w=0.5}{nw}"

play sound sfx_impact

show emi excited_amused_close
with vpunch

extend " ¡mmff!"

"Mi ocurrencia es interrumpida por la súbita presión de los labios de Emi sobre los míos. Me toma desprevenido, y soy recompensado golpeando mi cabeza contra la pared detrás de su cama."

hi "Ay."

show emi basic_hes
with charadistant

"Emi retrocede, tratando de verse preocupada en vez de como si estuviera a punto de reír."

emi "¿Estás bien?"

show emi excited_proud
with charachange

emi "¡Perdón!"

"Me froto la cabeza apesadumbradamente y le sonrío de vuelta."

hi "Me tomaste desprevenido."

hi "¿Se va a volver costumbre? ¿Shizune y Misha van a pasar más tiempo regañándome?"

"A la mención del dúo, Emi suelta una risita."

show emi basic_closedgrin
with charachange

emi "En serio, esas dos…"

show emi basic_grin
with charachange

emi "Si no supiera la razón, no entendería en absoluto por qué ella anda con alguien tan mandona."

hi "¿De cuál de las dos hablamos?"

show emi basic_closedhappy
with charachange

emi "Sabes exactamente de cuál, Hisao. Misha difícilmente es mandona."

hi "Entonces, ¿cuál es la razón?"

show emi basic_confused
with charachange

emi "¿Huh?"

hi "La razón por la que Misha anda con Shizune."

show emi basic_closedgrin
with charachange

"Emi evita mi pregunta con una sonrisa."

emi "Ni idea."

hi "Ya veo."

show emi basic_grin
with charachange

emi "De todos modos, pareces estar olvidando la pregunta original, ¿no?"

hi "Oh, sí, creo que sí."

hi "No te molestaría darle al chico un pequeño aviso, ¿no crees?"

hi "De otra manera podría terminar con una conmoción."

"Enfatizo el punto frotándome la parte trasera de la cabeza."

show emi excited_amused
with charachange

"Emi suelta una risita malvada."

emi "Podrías usar casco."

show emi excited_proud
with charachange

emi "Algunos chicos de aquí lo hacen, sabes."

stop music fadeout 1.0

hi "¡O podría cobrar venganza!"

play sound sfx_pillow

show emi excited_circle
with vpunch

"Agarro una almohada de atrás y golpeo a Emi en la cabeza."

show expression im.Composite((295,1200), (0,0), "sprites/emi/emi_excited_circle.png") as emi:
    xalign 0.5 yanchor 0.5 ypos 1.0 subpixel True
    easeout 0.8 ypos 1.25 rotate -90
with None

show expression im.Composite((295,1200), (0,0), "sprites/emi/emi_excited_sad.png") as emi:
    xalign 0.5 yanchor 0.5 ypos 1.0 subpixel True
    easeout 0.8 ypos 1.25 rotate -90

with Dissolve(0.5)
with Pause(0.3)

play sound sfx_impact

hide emi
with vpunch

"Emi cae de la cama y aterriza en el suelo con un golpe."

show emi sad_pout:
    center
    ypos 1.2
    ease 1.0 ypos 1.0
with Dissolve(1.0)

"Sus brazos reaparecen rápidamente en la cama, y se las arregla para subir de nuevo."

"Realmente tiene una cantidad sorprendente de fuerza en ese pequeño cuerpo."

"Su cara está vuelta hacia abajo, mirando hacia el lado opuesto, lo que me hace pensar que podría haberla lastimado accidentalmente."

hi "¿Emi? ¿Estás bien?"

hi "No te golpeaste la—{w=0.3}{nw}"

show emi excited_smile_close
with vpunch

"Una mano sale disparada y agarra el cuello de mi camisa. Ella me acerca con un fuerte tirón, ahora su rostro está apenas a un centímetro del mío mientras sonríe descaradamente."

hi "¿Emi…?"

show emi excited_smile_close:
    subpixel True
    linear 0.1 ypos 1.7 zoom 2.0
with None

scene white
with Dissolve(0.1)

play sound sfx_impact

scene black
with Dissolve(0.75)

"Ella me da un brusco cabezazo, y nuestras frentes producen un ruido bastante fuerte."

scene bg school_dormemi at right
show emi basic_closedgrin at center
with openeye

"Me siento y froto mi adolorida cabeza mientras Emi sonríe victoriosa."

show emi basic_grin
with charachange

emi "¿Qué tal {b}eso{/b} como venganza?"

play music music_running

hi "¡No es justo!"

hi "¡No puedes vengarte de alguien que se está vengando!"

"Para alguien que no tiene gran parte de sus piernas, Emi es sorprendentemente ágil."

show emi basic_grin:
    center
    parallel:
        "emi basic_closedgrin" with Dissolve(0.2, alpha=True)
    parallel:
        easeout 0.5 xpos 0.3 alpha 0.0
with Pause(0.5)

hide emi
with None

"Me deslizo hasta su posición, pero ella rueda hábilmente y acierta un golpe con su almohada."

"Claro, las probabilidades están en su contra. Yo puedo ponerme en pie, para empezar."

scene black
with vpunch

"¡Auch!"

window hide

show evh emi_grinding_victorytall:
    xalign 0.5 yalign 1.0 subpixel True
    easein 12.0 yalign 0.0

with Dissolve(1.0)

with Pause(6.0)

window show

"Supongo que no puedo, después de todo. Emi parece haberme tirado abajo eficazmente, y ahora está sentada a horcajadas sobre mí mientras yo estoy de espaldas al suelo. Ni siquiera estoy seguro de cómo lo consiguió."

emi "¡Yo gano!"

"Sus ojos brillan traviesamente. He sido completamente derrotado por una chica que es de una fracción de mi tamaño, sin más."

"Por otra parte, ser el perdedor no parece tan malo. Emi posicionada sobre mi cintura no es algo que yo, o mi cuerpo, podamos ignorar fácilmente."

scene bg school_dormemi
with locationchange

"Abro mi boca para hablar, pero Emi baja su cabeza rápidamente antes de que yo pueda pronunciar media palabra. No opongo resistencia mientras ella presiona su boca contra la mía, tampoco es que quiera hacerlo."

"Esto es… diferente, de algún modo."

"Ella se detiene, mordisquea mi labio inferior, y continúa con su abrazo. Su lengua se apresura a explorar el interior de mi boca. Puedo sentir un calor extendiéndose a través de mi cuerpo mientras mi corazón comienza a latir más rápido."

"Mi mente empieza a enturbiarse, y me vuelvo vagamente consciente de mi mano viajando hacia la blusa de Emi. Emi suspira cuando alcanzo un pecho, luego hay una risita, y luego—"

scene evh emi_grinding_victory
with locationchange

"Miro hacia arriba, hacia una Emi sonriente."

emi "Te lo dije. Ahora esa es mi segunda victoria."

hi "¿Qué? Eso no cuenta; usaste tus encantos femeninos."

show evh emi_grinding_wink
with charachange

emi "“En el amor y la guerra todo se vale”, ¿no?"

emi "Ja, ¡hasta te estás sonrojando! No sabía que eras de los que se sonrojan, Hisao."

hi "Tú también te estabas sonrojando, sabes. Probablemente debido a tus actos indecentes."

"Incluso yo debo admitir que es una estupidez decirle esto a una mujer que está a horcajadas sobre mí y ha estado, hasta hace unos instantes, jugando a explorar nuestras gargantas."

show evh emi_grinding_grin
with charachange

emi "Una indecente, ¿yo?"

emi "Pues bien, veamos quién se sonroja primero, ¿de acuerdo?"

"No estoy seguro de si el tono de su voz me aterroriza o me provoca, pero esa pregunta se vuelve irrelevante con rapidez."

label es_E20h:

show evh emi_grinding_half_undress
with charachange

show evh emi_grinding_half_grin
with charachange

"En un movimiento de facilidad practicada, ella se quita su blusa y la arroja despreocupadamente a un lado. Su sujetador y falda la siguen rápidamente al suelo."

emi "¡Ja!"

"Resisto la urgencia de sonrojarme. Es una tarea sumamente difícil."

hi "Poco a poco, ¿no?"

show evh emi_grinding_off_yawn
with charachange

"Mi camisa sigue el ejemplo, no sin algo de dificultad gracias a mi posición. Emi finge un bostezo."

emi "Tendrás que hacer algo más que e—"

show evh emi_grinding_off_closesurprise
with charachange
stop music fadeout 3.0

emi "¡Ah…!"

"Mis manos acarician suavemente la piel desnuda de Emi, provocándole un escalofrío. Parece ser que mis manos actúan por sí mismas, de nuevo. Si nuestra posición me lo permitiera, probablemente terminaría de desnudarla."

"Empiezo a decir algo acerca de cómo Emi ha comenzado a sonrojarse, pero los dos estamos aproximándonos con rapidez a los límites de algo que apenas nos está conteniendo."
"Nuestra conversación se detiene por completo, y siento cómo mis brazos pierden energía."

play music music_one fadein 0.5

"Ninguno de los dos, sin embargo, está preparado para esta súbita y nueva sensación."

show evh emi_grinding_off_closearoused
with charachange

"Un indescriptible calor recorre mi cuerpo, viniendo tanto de mí como, al parecer, de Emi."

"Con una mano en mi pecho para estabilizarse, y otra sosteniendo la mía para asegurarse de que no puedo abrirme paso por su cuerpo de nuevo, ella se ve bastante complacida consigo misma."

show evh emi_grinding_off_aroused
with charachange

"Y entonces, luego de un momento de duda, se mueve."

"Y se mueve de nuevo."

"Y de nuevo."

"Mientras se mueve, su respiración sube y baja. Mi respiración también se está volviendo más rápida y entrecortada."

"El cuerpo de Emi tiembla y se estremece contra el mío, y puedo sentir cómo ella empieza a perder el balance. Debe de ser más difícil para ella mantenerse estable porque no tiene piernas."

show evh emi_grinding_off_closesurprise
with charachange

"La estabilizo lo mejor que puedo, posicionando mis manos sobre su trasero. Es firme y tenso."

"Tiene sentido, considerando lo mucho que corre. El poder latente en esos músculos hace que se flexionen cuando ella responde a mi contacto."

"Lo que fallo a tener en cuenta es que mi intento de estabilizarla hace que ella se deslice un poco hacia adelante y, bueno… Se siente increíble."

show evh emi_grinding_off_arousedclosed
with charachange

"Su ropa interior se desliza fácilmente contra mis pantalones, y no nos toma mucho tiempo establecer un ritmo."

"Pero Emi se niega a seguirlo, yendo ahora rápido, ahora lento, ahora deteniéndose por lo que se siente como una eternidad. No estoy seguro de si lo hace por jugar conmigo, o si lo hace para sentirse mejor, pero no podría importarme menos."

"El calor entre nosotros está creciendo en intensidad, y no puedo retener un suspiro. El sonido solo parece provocar a Emi."

"Empiezo a remarcar sus movimientos con los míos, lo que causa que sus modestos pechos reboten con mis movimientos. Su respiración empieza a acelerar mientras continuamos, con mi propia respiración acelerando del mismo modo."

"Con los ojos cerrados, aprieta sus labios con expectación. Me las arreglo para levantarme por unos instantes. Nuestras bocas buscándose la una a la otra, su pecho deslizándose contra el mío mientras nuestro sudor se mezcla."

"Cuando me acuesto de nuevo, mis pantalones están empapados con sudor. Me los quitaría si eso no significase detener lo que estamos haciendo."

"Y no quiero detener lo que estamos haciendo, detener esta presión cada vez mayor, este cosquilleo en lo recóndito de mi cerebro."

"Emi está deslizándose más y más rápido, respirando pesadamente, con su voz aparentemente incapaz de expresar lo que está sintiendo. Su cuerpo, por otro lado, está haciendo un buen trabajo."

show evh emi_grinding_off_come
with charachange

"De repente, ella cambia un poco sus movimientos mientras mi respiración se enreda en mi garganta, terminando en una estocada desesperada que me envía sobre los límites hacia una sensación arrasadora que no sabía que existía."

scene white
with Dissolve(3.0)

"Mi mente se vacía, se llena de ruido blanco, y sucumbo a la sensación del clímax. Por unos segundos, todo lo demás en el mundo colapsa excepto por esta increíble sensación de Emi y yo, juntos."

show evh emi_grinding_off_end
with Dissolve(1.0)

"Y luego… termina. El ruido blanco se aclara, y me quedo mirando hacia los ojos de la chica encima de mí."

"Por unos minutos, ninguno de los dos habla. El sonido de nuestra respiración llena el lugar, nuestros pechos agitados por la experiencia."

"Eventualmente ella, de mala gana, se mueve de encima y se sienta contra la pared. Me uno a ella."

label es_E20x:

scene bg school_dormemi at right
with locationchange

show eminude smile_close
with charachange

emi "Entonces… ¿me sonrojé?"

hi "No me fijé."

hi "¿Y yo?"

show eminude neutral_close
with charachange

"Emi se encoge de hombros, todavía respirando pesadamente."

show eminude weaksmile_close
with charachange

emi "Tampoco me fijé."

hi "Bueno, tal vez deberíamos—"

play sound sfx_dooropen

stop music fadeout 0.3

show rin basic_deadpan behind eminude:
    center
    xpos 1.0 xanchor 0.0 alpha 0.0 subpixel True
    easein 0.5 right alpha 1.0
show eminude blush_close
with vpunch

rin "Necesito usar tu ventana."

"Mi primera reacción es esconderme, pero luego me doy cuenta de que todavía estoy totalmente exhausto y sentado junto a una Emi con los pechos al aire, así que no hay escapatoria."

show rin basic_awayabsent:
    right alpha 1.0
with charachange

show rin basic_absent
with charachange

show rin basic_awayabsent
with charachange

"Los ojos de Rin pasan sobre Emi, sobre mí, y se fijan en la ventana."

show rin basic_deadpannormal
with charachange

rin "Había una nube."

play music music_comedy fadein 0.5

show eminude neutral_close
with charachange

emi "¿Una nube?"

show rin basic_lucid
with charachange

"Rin asiente."

show rin relaxed_nonchalant
with charachange

rin "La estaba observando desde mi ventana, pero no se quedó en mi ventana."

show rin negative_spaciness
with charachange

rin "Así que necesito usar tu ventana."

show eminude closedsmile_close
with charachange

"Emi se retuerce un poco, obligándome a toser para ocultar mi propia risa."

emi "¿Cuánto tiempo necesitas la ventana?"

emi "Estamos eh."

show eminude wink_close
with charachange

emi "Ocupados."

"Esta vez no puedo contener mi risa."

show rin negative_annoyed
with dissolvecharamove

"Rin nos ignora a los dos y observa por la ventana."

show rin basic_deadpanupset
with charachange

"Ella deja caer los hombros de golpe, y se ve decepcionada."

rin "Hmm."

rin "Cambió a otra cosa."

rin "Decepcionante."

show eminude grin_close
with charachange

"Emi está teniendo problemas para mantener una cara seria."

emi "Lamento escucharlo, Rin."

show eminude pout_close
with charachange

emi "¿Podríamos tener algo de privacidad ahora, por favor?"

show rin relaxed_nonchalant
with charachange

with Pause(0.2)

show rin relaxed_nonchalant:
    easeout 1.0 xpos 1.0 alpha 0.0 xanchor 0.0 subpixel True
with Pause(1.0)

play sound sfx_doorclose

hide rin
with None

"Rin se encoge de hombros, como si dijera ¿“puedes”? y arrastra sus pies a través de la puerta, cerrándola tras ella."

show eminude happy_close
with charachange

"Ambos soltamos una estridente carcajada, incapaces de lidiar con la extrañamente sincronizada visita de Rin de otra manera."

"Luego de que se detienen nuestras carcajadas, miro a Emi. Somos un completo desastre."

stop music fadeout 5.0

hi "Entonces."

show eminude neutral_close
with charachange

"Emi alza una ceja."

emi "¿Entonces?"

hi "¿Otra vez?"

show eminude wink_close
with charachange

"Emi suelta una carcajada, y luego asiente."

show eminude grin_close
with charachange

emi "Probablemente deberíamos de quitarnos la ropa esta vez."

$ suppress_window_after_timeskip = True

scene black
with dissolve


label es_E21:

window hide None

play sound sfx_alarmclock

with Pause(2.0)

scene bg school_dormhisao
with openeye

window show

"El resplandor del sol atraviesa mi ventana poco después de que mi alarma arruina el silencio de la mañana."

play music music_dreamy fadein 6.0

"Me siento adolorido."

"Los eventos de la noche anterior invaden de repente mi conciencia, y termino sonrojándome."

"Fue una noche memorable, y explica perfectamente el dolor en la parte baja de mi espalda."

"Caminar de regreso, según recuerdo, fue bastante tenso."

"Mis pantalones terminaron… empapados, los lavé en la ducha antes de regresar a mi habitación."

"Pero aún había una mancha considerablemente visible en el frente."

"Por fortuna para mí, Kenji fue la única persona con quien me encontré mientras regresaba."

"Y él no notó nada."

"Bueno, aparte de mi presencia en su vecinidad general."

"Claro que él me preguntó qué tal estuvo la noche, y si aprendí algo importante o no."

"Ni siquiera sé si abrí la boca para contestar; estaba demasiado cansado para que me importara."

"Y esta mañana, admito que me siento bastante desgastado."

"A pesar de todo, Emi prometió encontrarse conmigo en la pista, y no me gustaría defraudarla."

scene bg school_track
show emiwheel weaksmile at center
with locationskip

"Cuando llego, de verdad está esperándome."

"Esforzándose por verse animada, a pesar del hecho de estar en silla de ruedas."

"La saludo y empiezo a estirar."

hi "Llegaste temprano."

show emiwheel frown
with charachange

"Emi frunce el ceño y sacude la cabeza."

show emiwheel angry
with charachange

emi "Ridículo."

emi "{b}Tú{/b} llegaste tarde."

show emiwheel grin
with charachange

emi "¿Te quedaste dormido, Hisao?"

show emiwheel wink
with charachange

emi "¿Todo machacado?"

"Bueno, al menos ya se ve más como la misma de siempre."

"Y como era de esperarse, ella no parece muy cohibida al mencionar nuestras… actividades previas."

hi "Oye, tienes suerte de que haya podido venir hoy."

hi "Con toda esa actividad cardiovascular de anoche, casi llegué a pensar que tendría que ver al enfermero luego."

show emiwheel wink
with charachange

"Emi suelta una risotada, después su rostro se llena repentinamente de preocupación."

show emiwheel blush
with charachange

stop music fadeout 8.0

emi "Oye, eso no es…"

emi "Quiero decir, tú no…"

hi "Adelante, dilo."

show emiwheel awayfrown
with charachange

emi "Es solo que sería difícil de explicar si tú hubieras tenido un episodio mientras nosotros…"

hi "Oh."

hi "{b}Oh.{/b}"

"Ahora que ella lo menciona, de verdad es una preocupación legítima."

"Honestamente no pensé en eso anoche, por supuesto, estaba ocupado con otros asuntos más urgentes."

hi "Bueno, no creo que nada de lo que, eh, {b}hagamos{/b} vaya a ser una tensión mayor que estas carreras matutinas, y me las arreglo bien con esas, así que…"

show emiwheel frown
with charachange

"Emi considera esto."

show emiwheel evil
with charachange

"Un brillo travieso aparece en sus ojos."

play music music_emi fadein 2.0

emi "Digamos…"

hi "¿Hmm?"

show emiwheel grin
with charachange

"La luz se esfuma, y Emi me sonríe con tristeza."

"No puedo evitar sentir una vaga sospecha."

show emiwheel happy
with charachange

emi "Parece que olvidé un par de guantes."

hi "¿Para qué necesitas guantes?"

show emiwheel smile
with charachange

"Emi señala la silla sobre la cual está sentada."

emi "¡Para esto, por supuesto!"

show emiwheel wink
with charachange

emi "Bueno, no hacen falta para moverse normalmente por los alrededores, pero quiero sacarle buen provecho y ejercitarme."

show emiwheel grin
with charachange

emi "Y para ir así de rápido, debes usar guantes si no quieres terminar con llagas."

hi "Entonces qué, ¿te estás acobardando? ¿Tengo que hacerlo solo?"

show emiwheel awayfrown
with charachange

"Emi piensa por unos instantes, o pretende pensar."

show emiwheel closedsmile
with charachange

emi "Hmm… si mal no recuerdo, hay uno o dos pares que no se usan en el almacén de atletismo."

"Así que de verdad quiere hacerlo."


"¿Pero con el uniforme normal de la escuela? Pensé que usaría el uniforme de gimnasia para algo como esto."

hi "Espera, ¿qué están haciendo allí?"

show emiwheel frown
with charachange

"Emi me mira de soslayo."

emi "¿En serio? ¿No se te ocurre una razón por la cual un almacén lleno de suministros de atletismo en una escuela de discapacitados tendría guantes para carreras?"

"Bueno, si lo pone de esa manera, supongo que tiene perfecto sentido."

hi "Oye, todavía estoy acostumbrándome a este lugar. Dame un respiro, ¿no?"

show emiwheel grin
with charachange

emi "Supongo que puedo dejarlo pasar esta vez."

show emiwheel wink
with charachange

emi "Ahora vamos, voy a necesitar tu ayuda."

"No imagino para qué, pero, por otra parte, tampoco sabía por qué hay guantes para carreras en el almacén, así que no quiero presionar más el asunto."

scene bg school_sportsstoreext
with locationchange

"Emi dirige el camino hasta el almacén con suficiente facilidad, aunque puedo escuchar cómo se queja en voz baja."

"La verdad es que es algo tierno."

"Me adelanto un poco para alcanzar la puerta primero. Abrirla será más fácil para mí que para ella."

play sound sfx_door_creak

show emiwheel neutral:
    center
    xpos 0.4
    easein 0.5 xpos 0.5
with charaenter


"La puerta se abre, y Emi comienza a empujar su silla hacia adentro, solo para detenerse repentinamente en la entrada."

"Parece que el peldaño es un poquito más alto de lo que ella puede subir por sí misma."

show emiwheel awayfrown:
with charachange

show emiwheel awayfrown:
    center
    ease 0.4 xpos 0.45
    easeout 0.2 xpos 0.5
    ease 0.4 xpos 0.45
    easeout 0.2 xpos 0.5
    ease 0.4 xpos 0.45
    easeout 0.2 xpos 0.5
    ease 0.4 xpos 0.45
    ease 0.2 xpos 0.5
with Pause(1.0)

"Lo intenta unas cuantas veces, sin éxito, antes de fruncir el ceño y lanzar una mirada al objeto infractor."

show emiwheel angry at center
with charaenter

emi "Estúpida silla de ruedas."

show emiwheel frown
with charachange

emi "Hisao, ¿me podrías echar una mano con esto?"

hi "Claro, no hay problema."

scene bg school_sportsstoreroom
with locationchange

"Es suficientemente sencillo para mí empujar a Emi sobre el peldaño de la puerta, sacudiéndola un poco."

show emiwheel blush_close_ni at center
with charaenter

emi "¡Oye, con cuidado!"

hi "¡Oops! Perdón."

"Es en este momento cuando fallo en darme cuenta de mi dirección y estrello la silla de Emi contra una estera."

play sound sfx_impact

show expression im.Composite((425,1200), (0,0), night("sprites/emiwheel/close/emiwheel_blush_close.png")) as emiwheel:
    xalign 0.5 yanchor 0.5 ypos 1.0 subpixel True
    easeout 0.5 ypos 1.4 rotate 70

with vpunch

hide emiwheel
with None

"Ella suelta un grito de sorpresa y se desploma fuera de su silla."

"Hay un momento de silencio mientras miro con horror lo que hice, y Emi me mira a mí."

emi "Hisao…"

hi "¿Sí?"

emi "Prométeme que nunca trabajarás en un hospital."

hi "¡Lo lamento! ¡No quise hacerlo!"

"Emi suelta una risita, y alza una mano."

emi "¿Serías tan amable de ayudarme a regresar a mi silla, Hisao?"

show emi basic_closedgrin_close_ni:
    center
    ypos 1.2
    easein 0.5 ypos 1.0
with charaenter

"Mientras me agacho para ayudarla, ella sonríe triunfante y me jala hacia un beso que rápidamente provoca que nos olvidemos de regresarla a su silla."

play sound sfx_door_creak

"De hecho, cuando me muevo a una posición más cómoda, confieso que la silla rueda a través de la puerta, la cual se cierra de golpe tras su paso."

play sound sfx_rustling

hide emi
show eminude smile_close_ni at center
with charachange

"Bueno, al menos ahora tenemos privacidad, y eso es bueno porque mis manos trabajan con velocidad para remover la camiseta y la falda de Emi."

"Me asusta descubrir que ella olvidó ponerse su sujetador hoy. ¿Acaso planeó esto?"

show eminude blush_close_ni
with charachange

"Sus brazos se acomodan bajo los míos y reposan en mis hombros mientras yo trazo un camino de besos en su cuello, deteniéndome para dedicarle especial atención a cierto punto que descubrí ayer, donde el cuello se encuentra con el hombro."

emi "T-te has vuelto bastante bueno en es-¡ah!"

hi "Me esfuerzo."

show eminude frown_close_ni
with charachange

"Emi empuja mi pecho, con insistencia, y retrocedo con una expresión de perplejidad."

emi "Tengo que confesar algo, Hisao."

hi "¿Oh?"

"Habiendo retrocedido, decido concentrar mi atención en sus pechos."

show eminude blush_close_ni
with vpunch

"Mientras trata de hablar, intercala sus palabras con risitas que me parecen increíblemente adorables."

show eminude wink_close_ni
with charachange

emi "En re-aja ja ja-realidad ¡G-guau! No uso guantes."

"Mi respuesta es más bien un balbuceo dirigido a su pecho en vez de a su cara."

hi "Debí haberlo sabido…"

"Las palabras dejan de ser relevantes rápidamente."

show eminude closedsmile_close_ni
with vpunch

"Los movimientos de Emi son frenéticos, como si hubiera estado conteniendo algo desde que nos encontramos esta mañana, y ahora pudiera dejarlo salir."

"Su agresividad casi me toma desprevenido, sintiendo cómo casi arranca mi camisa, la forma en la que parece luchar por estar en la posición dominante."

"Por mi parte, confieso que también soy atraído por su actitud, defendiéndome, girando y luchando incluso mientras acaricio sus pechos, incluso cuando sus dedos se clavan en mis hombros, y olvido dónde estamos."

show eminude blush_ni
with vpunch

"Tanto así que giro fuera de la estera y caigo sobre algo pequeño y bastante duro."

hi "¡Au!"

show eminude weaksmile_ni
with charachange

"Emi, aún sonrojada y respirando pesadamente, me vuelve a ver y rompe en carcajadas."

emi "Lo siento, lo siento. ¿Estás bien?"

hi "Sí, creo. Aunque no estoy seguro sobre qué caí…"

"Reviso bajo mi espalda y saco el objeto culpable, inspeccionándolo de cerca."

stop music fadeout 0.2

"“Lubricante personal. Sabor a limón”."

"Espera, ¿qué?"

play music music_running

show eminude happy_ni
with charachange

"Emi lanza una mirada y empieza, si es posible, a reír con más fuerza."

hi "Por alguna razón, creo que esto… no tiene nada que ver con atletismo."

show eminude closedsmile_ni
with charachange

emi "Oh, vaya, ¡yo sé de quién es eso!"

hi "¿Qué?"

show eminude wink_ni
with charachange

emi "¡Es del capitán del equipo!"

"Ah, mi viejo némesis. O algo así."

hi "¿Cómo sabes que es de él?"

show eminude awayfrown_ni
with charachange

"Al parecer hice una pregunta tonta, o al menos eso piensa Emi."

show eminude frown_ni
with charachange

emi "Porque fue él quien me dijo que el almacén de atletismo era un buen lugar para… ¿cómo los llamó él?"

show eminude pout_ni
with charachange

emi "“Encuentros clandestinos”."

hi "¿Oh? ¿Te invitó a alguno o algo así?"

show eminude happy_ni
with charachange

"Emi suelta otra carcajada."

"Confieso que la imagen de una Emi desnuda riéndose es extrañamente hermosa."

"Siento un afán por terminar la conversación y continuar con lo que estábamos haciendo, a pesar de mi pregunta capciosa."

show eminude closedsmile_ni
with charachange

emi "Hisao, el capitán del equipo es gay."

"Huh."

hi "¿En serio? Y yo al inicio pensé que ustedes dos eran pareja."

show eminude awayfrown_ni
with charachange

emi "Bueno… en realidad me gustaba cuando me uní al equipo, pero él no estaba interesado."

show eminude frown_ni
with charachange

emi "Obviamente."

show eminude neutral_ni
with charachange

emi "Pero somos buenos amigos, supongo."

show eminude grin_ni
with charachange

emi "Digo, él me contó todo esto, ya sabes."

hi "Me cuesta preguntarlo,"

"de verdad, me cuesta. Pero lo pregunto de todos modos."

hi "Pero, aun así, ¿para qué necesita el eh… lubricante?"

hi "Quiero decir, él no… eh…"

"¿Cómo diablos se las arregla Emi para no sonrojarse?"

show eminude wink_ni
with charachange

emi "Obviamente lo usa para eso, ya sabes."

show eminude evil_ni
with charachange

emi "Anal."

"Intento suprimir una risilla."

"Fracaso."

show eminude happy_ni
with charachange

"Emi también está riéndose entre dientes."

hi "¿Y él te {b}cuenta{/b} todas estas cosas?"

show eminude awayfrown_ni
with charachange

"Emi se encoge de hombros."

show eminude neutral_ni
with charachange

emi "Sí, claro."

stop music fadeout 10.0

show eminude closedsmile_ni
with charachange

emi "Es algo entusiasta con todo este asunto."

emi "Dice que es una sensación insuperable."

hi "Ah… ajá."

"El aire en el almacén se siente cargado con algún tipo de horrible curiosidad."

hi "Interesante."

hi "Supongo que tendré que creer lo que dice."

show eminude neutral_ni
with charachange

emi "Bueno…"

"Los pájaros de afuera dejan de silbar."

"El viento se detiene."

"En algún lugar, un hombre está bebiendo una taza de café. Se detiene con la taza en sus labios."

show eminude neutral_ni
with charachange

emi "Tal vez…"

extend " podríamos…"

show eminude blush_ni
with charachange

emi "Intentarlo."

play music music_one fadein 5.0

"Repentinamente y sin previo aviso mi mandíbula se suelta y pega en el suelo."

hi "¿Q-qué?"

"Emi por fin se está sonrojando, frotándose la parte trasera de la cabeza avergonzadamente."

show eminude pout_ni
with charachange

emi "Bueno, es solo que realmente no… podemos hacer lo que hicimos anoche, ¿sabes?"

emi "Sería un poco… no sería seguro, ¿sabes?"

show eminude weaksmile_ni
with charachange

emi "Digo, anoche no fue exactamente una buena idea."

show eminude closedsmile_ni
with charachange

emi "Así que ya sabes, podríamos intentarlo para ver…"

hi "¿Si es igual de bueno?"

show eminude weaksmile_ni
with charachange

emi "Bueno eh, sí. Básicamente."

hi "Huh."

label es_E21h:

scene evh emi_shed_base1
show emi emi_shed_grin
show hisao emi_shed_neutral
show evh_l emi_shed_up
show evh_r emi_shed_down
with shorttimeskip

emi "¡Con cuidado!"

hi "¿Estás segura de esto?"

"Estoy posicionado detrás de Emi, quien está mirando hacia atrás sobre su hombro, viéndose algo nerviosa."

"Bueno, obviamente una vez que decidimos continuar con esta idea teníamos que recuperar el estado de ánimo."

"Una vez lo logramos, vaciamos la botella de lubricante y…"

"Aquí estamos."

show emi emi_shed_hesitant
with charachange

emi "Sí, ¡estoy segura! Apresúrate, antes de que me calme y lo piense mejor."

"La respiración de Emi aún está algo agitada, y su respuesta es casi impaciente."

"Es de esperarse, supongo. Estábamos tan cerca, y esto está retrasando las cosas."

"Creo que los dos nos volvimos temporalmente locos."

"Al menos pretenderé que eso es lo que pasa de ahora en adelante."

"Me esfuerzo en no pensar en los detalles de lo que estoy a punto de hacer."

"No hay forma de que esto vaya a ser limpio."

show evh emi_shed_base2
show hisao emi_shed_closed
with charachange

"Tomando una bocanada de aire que es tanto para mí como para ella, entro despacio."

"Hay mucha resistencia, y es como si nuestros cuerpos no estuvieran dispuestos a seguir adelante."

show emi emi_shed_shock
with hpunch

"Todo el cuerpo de Emi se tensa, y como en este momento solo estoy parcialmente dentro, se siente sorprendentemente bien, quizá un poco raro."

"Emi, por el otro lado, se ve incómoda."

"Su expresión es casi cómica."

show hisao emi_shed_neutral
with charachange

hi "¿Debería de parar?"

"La respiración de Emi se atasca en su garganta, y parece que le toma un poco más del tiempo necesario formular una respuesta."

show emi emi_shed_closed
with charachange

emi "N-no, sigue. Simplemente se siente raro."

"Suelta una risita."

"No puedo culparla. A mí me sorprende haber podido formar una oración."

show hisao emi_shed_closed
with charachange

"Es… caliente."

"Se siente extremadamente raro."

"El lubricante reluce de forma poco natural."

"Me hace sentir incómodo."

"Continúo trabajando mi camino dentro de ella, avanzando despacio y escuchando atentamente su respiración."

show evh emi_shed_base3
show emi emi_shed_hesitant
with charachange

"Llego a mi límite y me detengo. Emi mira hacia atrás, mordiéndose el labio inferior."

emi "¿Intentarás moverte? ¿O solo nos vamos a quedar así sintiéndonos como idiotas?"

show hisao emi_shed_neutral
with charachange

hi "No, solo quería darte un momento para que te ajustes."

"Esto no tiene ningún sentido."

"¿Cómo fue que se nos ocurrió intentar esto?"

show emi emi_shed_grin
with charachange

emi "No creo que haya forma de ajustarse a esto, Hisao."

show emi emi_shed_hesitant
with charachange

emi "Intenta moverte. ¿Tal vez se sienta mejor?"

"Ella suena poco segura, pero claramente no está dispuesta a admitir la derrota ahora que llegamos tan lejos."

show emi emi_shed_closed
with charachange

"Empiezo un movimiento lento que parece funcionar para ambos, ya que ella cierra los ojos en un intento de concentrarse en esta nueva sensación."

"Mientras empiezo a encontrar el ritmo, empiezo a sentir esa familiar sensación de caída que experimenté ayer."

show hisao emi_shed_closed
with charachange

"Cierro mis ojos e intento perderme en la sensación, solo que…"

"Algo no está bien."

"Emi no está haciendo ningún ruido."

"Ayer aprendí con rapidez que Emi no es precisamente silenciosa cuando está disfrutando."

show hisao emi_shed_neutral
with charachange

"Cuando abro los ojos, veo que Emi intenta adaptarse, pero simplemente no parece estar funcionando para ella."

"Tiene los ojos cerrados, y está mordiéndose el labio, pero parece ser más por tolerancia que por placer."

"Una mirada que dice algo así como “bueno, esto fue un fracaso, pero tal vez termine pronto”."

"Vaya situación en la que me metí."

"En realidad, no quiero parar."

"Pero al mismo tiempo, no parece estar funcionando para Emi, y si lo hace, lo hace mucho más lento que para mí."

"Me siento mal. Quiero que Emi también disfrute de esto."

show evh_r emi_shed_up
show emi emi_shed_shock
with charachange

"Estiro un brazo para acariciar el pecho de Emi, lo que hace que se sobresalte."

show hisao emi_shed_sweat
with charachange

"Esto provoca que ella se tense a mi alrededor considerablemente, provocando una oleada de placer que me ciega."

show evh emi_shed_base4
show hisao emi_shed_neutral
show emi emi_shed_closed
show evh_l emi_shed_down
with charachange

"Mi suspiro parece provocar a Emi, pero su sonrisa se convierte rápidamente en un suspiro cuando casualmente muevo mi otra mano hacia abajo y empiezo a acariciar con gentileza el suave parche de vello entre sus piernas."

"El movimiento de mis propias caderas aumenta mientras las caricias de mi mano traen de vuelta los suspiros y gemidos a los que estoy acostumbrado."

show hisao emi_shed_sweat
with charachange

"Me concentro solo en las sensaciones de mis manos, una resbalosa y deslizándose, la otra sobre piel suave y sensible, escalofríos en su piel, temblores y sudor, mientras su propio clímax creciente provoca que se tense, hasta que por fin ya no puedo—"

"Yanopuedomás."

show hisao emi_shed_closed
with charachange

"OhDioslosientoEmivoyahacerlo."

"Doy una estocada final, mis dedos se tensan sobre los pezones de Emi, me sumerjo entre sus piernas."

window hide

play sound sfx_flash
with SilentWhiteout(0.1,0.0,0.1)
play sound sfx_flash
with SilentWhiteout(0.1,0.0,0.4)
with GenericWhiteout(0.5,1.0,4.0)

window show

"La espalda de Emi sufre un espasmo y ella se arquea, un agudo grito de niña rebota en las paredes, y siento la oleada de mi propio clímax aniquilando las demás sensaciones de mi cuerpo."

show evh_l emi_shed_up
show evh_r emi_shed_down
with charachange

"Los brazos de Emi ceden y ella se va de bruces, separándonos con considerable violencia y tirando de algo muy preciado para mí en el proceso."

label es_E21x:

play sound sfx_impact

scene bg school_sportsstoreroom
with vpunch

"El repentino cambio de placer a dolor hace que pierda el equilibrio y caiga sobre Emi."

stop music fadeout 2.0

emi "¡Au!"

hi "Au."

"Rápidamente me quito de encima y me pongo en pie, respirando pesadamente e intentando ignorar el dolor de mi entrepierna."

"Emi se queja un poco mientras gira. Agarra unos cuantos pañuelos que teníamos a mano, y se limpia antes de ponerse la ropa interior y recostarse incómodamente contra una pared."

"Aún respirando pesadamente, decido sentarme contra la pared junto a ella. El frío concreto tocando mi sudorosa espalda es una sensación bienvenida."

show eminude sad_close_ni at center
with charaenter

emi "¡Al final {b}dolió{/b}!"

hi "Sí, yo eh…"

hi "Probablemente no fue una buena idea."

"Emi se retuerce para intentar sentarse junto a mí sin sentir mucho dolor. A juzgar por sus muecas; no funciona muy bien."

show eminude pout_close_ni
with charachange

emi "Sí, voy a tener que hablar con el capitán."

show eminude angry_close_ni
with charachange

emi "Obviamente estaba mintiendo."

play music music_ease

"La profunda y absoluta ridiculez de la situación me golpea de repente, y empiezo a reír."

show eminude happy_close_ni
with charachange

"Emi sacude la cabeza y empieza a reír conmigo."

show eminude grin_close_ni
with charachange

emi "Oye, Hisao."

hi "¿Sí?"

show eminude pout_close_ni
with charachange

emi "Nunca vamos a hacer esto de nuevo, ¿verdad?"

hi "Sí, creo que aquí mi curiosidad ya está satisfecha."

"Emi asiente, complacida."

show eminude closedsmile_close_ni
with charachange

emi "Bien."

show eminude smile_close_ni
with charachange

emi "Creo que tal vez deberíamos apegarnos a lo básico, ¿no?"

show eminude blush_close_ni
with charachange

emi "De todas formas casi todo esto es nuevo para mí."

hi "¿A qué te refieres con “casi todo”?"

show eminude grin_close_ni
with charachange

"Emi sonríe malvadamente."

show eminude closedsmile_close_ni
with charachange

emi "Nunca lo diré."

"Un pensamiento desagradable cruza mi mente."

"Aún más desagradable es la idea de tener que preguntárselo a Emi."

"Aunque, después de lo que acabamos de hacer, debería de ser pan comido."

hi "Oye, ¿hay algún lavabo?"

hi "Me gustaría quizás, eh."

hi "Lavarme un poco."

show eminude blush_close_ni
with charachange

"Emi abre la boca de par en par."

emi "¿En el {b}lavabo{/b}?"

hi "Bueno, en realidad no hay otro lugar para hacerlo, ¿no?"

hi "Y eh… Quiero evitar un olor."

hi "Que el enfermero podría notar."

"Esta es la conversación más incómoda que he tenido nunca."

show eminude closedsmile_close_ni
with charachange

emi "Tienes razón."

show eminude grin_close_ni
with charachange

emi "Sí, hay uno eh… Está en la pared de atrás."

show eminude smile_close_ni
with charachange

emi "Puede que también haya jabón."

hi "Gracias."

hide eminude
with charaexit

"De hecho, sí hay un pequeño jabón para manos, que es mejor que nada."

"Aunque no hay ninguna toalla. Supongo que me secaré tarde o temprano."

show eminude grin_ni at center
with charaenter

emi "¿Todo listo?"

hi "Sí, eso servirá por ahora. No es como si no fuera a tomar una ducha luego de que veamos al enfermero."

show eminude weaksmile_ni
with charachange

emi "Me alegra escucharlo."

show eminude wink_ni
with charachange

emi "Ahora ayúdame a encontrar mi ropa. La arrojaste en algún lugar."

hi "¡Oye, tú tampoco te contuviste! ¿Cómo se supone que explique este agujero en mi camisa?"

show eminude closedsmile_ni
with charachange

emi "Jeje, perdona. Me emocioné un poco."

scene bg school_sportsstoreroom
with shorttimeskip

"Toma algo de tiempo, pero al fin estamos más o menos vestidos."

"Hay un frenético instante en el cual ninguno de los dos sabe dónde está la silla de ruedas de Emi, pero recuerdo el momento en que cruzó la puerta y voy al rescate."

show emiwheel neutral_close_ni at center
with charaenter

emi "Ahora ten más cuidado cuando cruces la puerta, ¿de acuerdo?"

show emiwheel awayfrown_close_ni
with charachange

emi "Los golpes no son mis amigos en estos momentos."

hi "Lamento tanto que hayamos intentado esto."

show emiwheel grin_close_ni
with charachange

"Emi se encoge de hombros y sonríe."

show emiwheel wink_close_ni
with charachange

emi "Bueno, valía la pena intentarlo, ¿no?"

show emiwheel closedsmile_close_ni
with charachange

emi "Y de cualquier forma, fue un buen ejercicio, ¿no?"

"No puedo negarlo."

scene bg school_nursehall
with shorttimeskip

"Mientras subimos hacia la oficina del enfermero, noto que Emi sigue retorciéndose incómodamente en su silla."

show emiwheel awayfrown
with charachange

emi "Dios, esto se siente raro."

show emiwheel neutral
with charachange

emi "Por suerte estoy en una silla de ruedas, Hisao."

hi "¿Por qué lo dices?"

show emiwheel weaksmile
with charachange

emi "Porque ahora no tendré que explicarle al enfermero por qué estoy caminando raro."

hi "Oh."

hi "Nunca volveremos a hacer esto."

scene bg school_nurseoffice
show nurse fabulous at center
with locationchange

"El enfermero es lo suficientemente amable como para no mencionar las marcas que Emi me dejó en los hombros."

"Tampoco dice una sola palabra sobre el constante cambio de posiciones de Emi en su silla de ruedas."

"O no lo notó, o no quería notarlo."

"De todos modos, tendré que asegurarme de que no echó cianuro en mis medicinas por algún tiempo."

"Solo para estar seguro."

stop music fadeout 4.0
scene bg school_dormhisao
with locationskip

"Me ducho por más tiempo del usual, solo para asegurarme de que estoy limpio de nuestro pequeño “experimento”, y luego colapso en mi cama."

"Las clases empiezan en veinte minutos, así que probablemente pueda permitirme una siesta."

scene black
with shuteye




label es_E22:

scene black
with dissolve

with Pause(5.0)

play sound sfx_doorknock

"Toc toc."

"¿Quién es?"

play sound sfx_doorknock

"Toc toc."

"Así no es como sigue la broma."

play sound sfx_doorknock

"Toc toc."

"¡Ya dije quién es!"

"Más importante, ¿qué hora es?"

"Aún más importante, ¿qué día…?"

scene bg school_dormhisao
with openeyefast

"Repentinamente soy catapultado a la vigilia tanto porque no han dejado de tocar la puerta como porque ya está atardeciendo."

"En un día de escuela."

"Ahora completamente despierto, puedo recordar por qué estaba tomando una siesta."

"Mejor no le doy esa excusa a Mutou."

"“Perdón por no estar en clases, estaba experimentando sexualmente con mi novia y me dejó agotado”."

"Sí, eso funcionaría muy bien."

play sound sfx_doorknock

"Me pregunto cuánto tiempo más durará este ruido."

"Supongo que tengo que abrir la puerta."

play sound sfx_dooropen

scene bg school_dormhallway
show kenji tsun at center
with locationchange

"Por algún extraño motivo no me sorprende ver a Kenji del otro lado."

"Aunque parece que Kenji está sorprendido de verme a mí."

ke "¿Qué diablos estás haciendo aquí, hombre?"

play music music_kenji fadein 0.5

hi "Bueno, estaba durmiendo."

show kenji neutral
with charachange

"Kenji asiente comprensivo."

show kenji happy
with charachange

ke "Noqueado. Ya veo."

show kenji tsun
with charachange

ke "Te dije que fueras cuidadoso con esa chica Ibarazaki, hombre."

ke "Esta es la clase de cosas que pasan cuando no eres precavido."

"Él hace un intento de mirar la parte trasera de mi cabeza."

show kenji neutral
with charachange

ke "¿Te golpeó con algo?"

ke "¿O fue una droga?"

hi "Deja de intentar tocarme."

with flash

"Kenji saca una linterna eléctrica y la apunta hacia mis ojos."

ke "¿Tienes una conmoción?"

hi "¡No me noquearon!"

show kenji happy
with charachange

ke "Puede que simplemente no lo recuerdes."

"Esta conversación no va a terminar nunca."

hi "No, solo tuve una mañana agotadora y me dormí."

show kenji tsun
with charachange

ke "Lo que sea, hombre."

ke "Si quieres negarlo todo, supongo que no puedo detenerte."

ke "Pero tienes que tener cuidado con esa chica, hombre. No es segura."

hi "¿Qué?"

show kenji rage
with charachange

ke "No es seguro estar cerca de ella; ¡es una de sus agentes más siniestras!"

ke "Si no tienes cuidado, ¡nadie sabe lo que podría pasar!"

ke "¡Ella ha derribado a hombres más fuertes que tú, sabes!"

hi "¿De qué diablos estás hablando?"

hi "Ella no es una agente de nada, y no me noqueó, ¿de acuerdo?"

hi "Y también dudo que haya derribado nada."

show kenji tsun
with charachange

"Kenji se ve casi ofendido."

"No tengo idea por qué."

ke "¿No me crees?"

ke "Qué frío, hombre. Qué frío."

ke "Solo intento ayudarte. Eso es lo que hacen los amigos, sabes."

"¿Somos amigos? No tenía idea."

"Por otro lado, me pregunto si Kenji siquiera sabe lo que implica ser amigo de alguien."

"Siento algo de lástima por él, ahí parado frente a mí."

"Tal vez él de verdad cree que está ayudándome."

hi "Lo sé, lo sé."

hi "Lamento eso. Gracias por la advertencia."

"Le tiendo mi mano en señal de paz."

show kenji neutral_close
with characlose

"Kenji la estrecha cautelosamente, como si mi mano pudiera estar en llamas."

"Hay un incómodo silencio por unos segundos hasta que Kenji recuerda que aún está estrechándome la mano."

show kenji happy_close
with charachange

ke "De todas formas, necesito un favor."

hi "¿Qué tipo de favor? No me queda dinero…"

ke "Sí te queda. Tienes dinero guardado en la gaveta de tu escritorio bajo un cuaderno negro. Para emergencias."

hi "¿Registraste mi habitación?"

show kenji neutral_close
with charachange

ke "Eso no importa."

ke "De todas formas, no necesito dinero."

"Adopta un tono muy serio."

show kenji tsun_close
with charachange

ke "Estoy a punto de embarcarme en una operación importante."

ke "Hará volar la conspiración por los aires si estoy en lo correcto."

ke "Pero es peligroso, así que necesito que hagas algo por mí en caso de que no regrese."

hi "Uh, claro hombre. Lo que sea."

"¿Qué demonios planea hacer?"

"¿Debería avisarle a alguien sobre esto?"

show kenji neutral_close
with charachange

ke "Si desaparezco, espera tres días y luego envía mi diario a las noticias."

ke "Está escondido en mi habitación bajo el fondo falso de una de las gavetas de mi escritorio."

hi "¿Cómo entro en tu habitación? No tengo llave."

show kenji tsun_close
with charachange

"Kenji me mira como si estuviera loco."

ke "Fuerza la cerradura. Sabes hacer eso, ¿no?"

ke "¡Es una habilidad importante que debes aprender a temprana edad!"

hi "Eh, sí, claro que sé hacerlo."

hi "Me aseguraré de eh, hacerlo por ti. Si desapareces."

"No creo que quiera leer el diario de Kenji."

"De todos modos, Kenji parece bastante feliz de que haya accedido a hacer esto por él."

show kenji happy_close
with charachange

ke "Genial, hombre. Genial."

ke "Te veré luego, tengo cosas que hacer."

stop music fadeout 5.0

show kenji happy_close:
    easeout 0.5 xpos 0.7 alpha 0.0
with Pause(0.5)

hide kenji
with None

"Y se va, caminando rápidamente por el pasillo."

"Lo hizo parecer tan concluyente."

"Espero no tener que cumplir sus deseos finales."

scene bg school_dormhisao
with locationchange

play sound sfx_doorclose

"Sacudiendo mi cabeza, cierro la puerta y camino de vuelta a mi cama."

"Supongo que debería ir a clases, aunque sea para no perderme la segunda mitad del día."

"Pero ya es tan tarde y no he ido a ninguna clase hoy…"

"Y quería leer más de ese libro de Hawking que Mutou me prestó…"

"Estoy seguro de que él entenderá."

with shorttimeskip

play sound sfx_hammer

"Toc toc."

"Esta vez el ruido aparta bruscamente mi atención del libro."

"Una experiencia no muy distinta a ser despertado."

hi "¿Quién es?"

emi "¡Yo! ¿No estás alegre?"

play music music_emi fadein 4.0

"La voz se amortigua a través de la puerta, pero sin duda es de Emi."

play sound sfx_dooropen

scene bg school_dormhallway
show emiwheel smile at center
with locationchange

"Brinco y abro la puerta, sonriendo ampliamente."

hi "¡Hola! ¡Me alegra verte de nuevo!"

show emiwheel grin
with charachange

"Emi me devuelve la sonrisa, mirándome desde su silla de ruedas."

show emiwheel closedsmile
with charachange

emi "Sí, me hubieras visto más temprano, pero el condenado elevador no estaba funcionando."

show emiwheel pout
with charachange

emi "Tuve que esperar a que lo arreglaran."

show emiwheel awayfrown
with charachange

emi "Pensarías que lo mantienen en mejor estado, pero nooo…"


"Me río entre dientes por su expresión de enfado y la invito a pasar."

scene bg school_dormhisao
with locationchange

"Ella entra rodando con facilidad, y salta a la cama con mi ayuda."

show emi basic_closedgrin:
    center
    ypos 1.0
    easein 0.5 ypos 1.1
with charaenter

emi "Listo. Mucho más cómoda que esa estúpida silla."

show emi basic_grin:
    ypos 1.1
with charachange

"Flota cierta satisfacción en el aire, y por un minuto simplemente nos miramos el uno al otro."

"Es hasta ahora que noto los círculos bajo los ojos de Emi."

"No son oscuros, pero definitivamente no estaban allí antes."

"Antes de que pueda preguntar por ellos, Emi me clava una mirada traviesa."

show emi excited_happy
with charachange

emi "Entonces, no pude evitar notar que no fuiste hoy a almorzar."

emi "De hecho, no creo que te haya visto en ningún lado."

show emi excited_proud
with charachange

emi "¿Qué ocurrió, ehhh?"

hi "Me quedé dormido."

hi "En realidad no me desperté hasta el mediodía, y eso solo porque Kenji me despertó."

show emi excited_amused
with charachange

emi "¿Por qué estabas tan cansado, eh?"

hi "El arduo ejercicio de esta mañana. Un poco incómodo, también."

show emi basic_closedhappy
with charachange

"Emi tose, medio riéndose, medio ocultando su incomodidad."

show emi basic_happy
with charachange

emi "Recuérdame no hacer eso de nuevo."

hi "No hay problema. Tampoco fue exactamente agradable para mí, para ser honesto."

hi "Solo tendremos que evitarlo de ahora en adelante."

hi "¿Aún estás eh, adolorida?"

show emi basic_confused
with charachange

"Emi me mira con incredulidad."

hi "¿Qué? ¡Lo pregunto en serio!"

show emi sad_grin
with charachange

emi "De todas las preguntas que jamás pensé recibir, esa es una de ellas."

hi "Bueno, nunca pensé que la preguntaría, así que estamos a mano."

show emi basic_closedhappy
with charachange

"Emi se ríe con eso."

emi "Supongo, ¿eh?"

stop music fadeout 5.0

show emi sad_shy
with charachange

emi "Bueno, ya que preguntaste, sí. Aún estoy adolorida."

show emi sad_pout
with charachange

emi "Nunca haremos eso de nuevo."

hi "No voy a discutir eso."

"Se le escapa un bostezo, y alzo una ceja."

hi "¿Cansada?"

show emi sad_grin
with charachange

"Emi asiente adormecida."

play music music_serene fadein 8.0

show emi sad_depressed
with charachange

emi "No he dormido bien."

"¿No ha dormido bien?"

"Puedo saber que ella tampoco quería decirme esto, porque da un pequeño salto como si acabara de sorprenderla mintiendo y se apresura en añadir,"

show emi basic_closedgrin
with charachange

emi "Aunque no es gran cosa."

hi "¿Cuál es el problema?"

show emi basic_grin
with charachange

"Emi se encoge de hombros y se niega a explicar."

hi "¿Estresada por los exámenes?"

"Se encoge de hombros de nuevo, pero luego de una pausa, asiente vacilante."

show emi sad_shy
with charachange

emi "Eh, sí, supongo."

emi "La verdad, es por eso que pasé."

"Ella empieza a verse más y más miserable."

"No como para que se note, por supuesto; pero sus ojos están fijos en su regazo, ella está inquieta y su voz es cautelosa."

show emi sad_pout
with charachange

emi "Nosotros eh, debemos dejar de pasar tanto tiempo juntos."

hi "¿Eh? ¿Por qué?"

"Emi inhala profundamente, como si hubiera estado practicando esto."

show emi sad_shy
with charachange

emi "Porque es demasiado divertido estar contigo."

emi "Y no puedo concentrarme cuando estás cerca."

emi "Con los exámenes acercándose, simplemente… no puedo tener esa distracción."

show emi sad_depressed
with charachange

emi "De otra forma, me temo que mis notas serían terribles."

hi "Podría ayudarte a estudiar…"

show emi sad_grin
with charachange

"Ella me sonríe, visiblemente triste con la situación."

emi "Me encantaría si pudieras hacerlo, pero en realidad no estudiaríamos, ¿cierto?"

show emi sad_shy
with charachange

emi "Quiero decir, incluso ahora estoy intentando tener una conversación contigo pero creo que solo quiero, eh…"

show emi sad_shyblush
with charachange

emi "No conversar."

hi "Ah."

hi "Abrumada por mi vigorosa masculinidad. Entiendo."

show emi basic_grin
with charachange

"Eso me consigue una sonrisa, al menos."

"Emi sacude la cabeza."

show emi basic_closedgrin
with charachange

emi "Idiota. Eres tan presumido."

hi "Bueno, soy sumamente irresistible."

show emi sad_shyblush
with charachange

emi "Eh, más o menos. Supongo."

show emi sad_grin
with charachange

emi "Así que esa es la situación, Hisao."

emi "Me divierto demasiado contigo, y si quiero llegar preparada a los exámenes, necesito estar sola."

hi "Oye, está bien."

"Realmente parece haberla estado preocupando."

"Además, es solo por un par de semanas. Y aún nos veremos el uno al otro en las mañanas, y en el almuerzo."

hi "Podemos vernos en la escuela, no hay problema."

hi "Y luego de los exámenes, iremos a una cita para celebrar que hayan terminado, ¿de acuerdo?"

show emi basic_closedgrin
with charachange

"Emi sonríe, complacida por esta propuesta."

show emi basic_happy
with charachange

emi "¡Sí, claro! ¡Suena genial!"

show emi excited_amused_close at center
with characlose

"Y como para señalar el final de la conversación, se inclina y me besa."

"No nos pasamos el resto de la noche preocupándonos por los exámenes."

stop music fadeout 2.0

scene black
with dissolve



label es_E23:

window hide None

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_night fadein 4.0

scene bg school_library_bw
with locationchange

nvl clear
nvl show dissolve

n "\n\nEs extraño lo fácil que es para Emi y para mí no vernos luego de clases."

n "De hecho, me atrevería a decir que es ligeramente inquietante."

n "Tan fácil como nos hemos juntado, parece que nos separamos sin muchos problemas."

n "Bueno, supongo que eso no es totalmente cierto."

n "Los dos hemos estado bastante desanimados desde esa última noche juntos."

n "Y podemos vernos todas las mañanas para nuestras carreras (y solo para nuestras carreras, debería añadir)."

n "También en el almuerzo. Especialmente disfruto almorzar con ella."

n "Tenemos tiempo de sobra para hablar de todo fuera de la escuela, dado que las carreras matutinas se han vuelto más serias."

n "Creo que es porque Emi quiere reponer lo de nuestra tontería en el almacén."

n "Pero no importa cuánto bromeemos durante el almuerzo, no puedo evitar sentirme un poco preocupado por ella."

nvl clear

n "\n\nElla se ve distraída más a menudo, y la he observado inquieta y nerviosa más de una vez."

n "Nunca pensé que ella fuera alguien que se preocupa tan profundamente por los exámenes, pero realmente parecen estar haciendo mella en Emi."

n "Y eso que ni siquiera han empezado."

n "Este es solo el calentamiento, la bocanada de aire antes de zambullirse."

n "Mañana, el verdadero reto comienza."

n "O los verdaderos exámenes, como sea."

n "En cuanto a mí, no me siento así de preocupado por los exámenes."

n "No estoy seguro de por qué. Quiero decir, son muy importantes; mis notas aquí determinarán mis posibilidades de entrar en una buena universidad."

n "Diablos, si soy demasiado arrogante ahora, podría echar a perder toda mi trayectoria académica."

n "Pero ya empezados, estoy seguro de que saldré victorioso."

nvl clear

n "\n\n\n\n\n\nMutou cree que tengo dominado el examen de ciencias, por lo menos."

n "O como él dice, “La última cosa que debería darte problemas es mi examen, Hisao. Está muy por debajo de tus habilidades”."

n "Por otro lado, es Mutou quien me está diciendo esto."

n "Sus alabanzas hacia mí conllevan la disimulada implicación de que cualquier cosa proveniente de mí que sea menos que perfecta sería una decepción, lo que ha provocado que me preocupe más de lo que debería por el examen."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

scene bg school_library
with locationchange

window show

"Es por esa razón que me encuentro en la biblioteca después de clases, escudriñando el libro."

"Cosas bastante fáciles de repasar; algunas fórmulas de velocidad, unas cuantas de fricción…"

"Un paseo por el parque comparado con mi temido examen de Inglés. Nunca fui bueno con los idiomas…"

"Mientras hojeo a través de mis notas una vez más, mi mente empieza a vagar."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\n\nLuego de que estos exámenes terminen, las cosas deberían ser más sencillas."

n "Pronto nos graduaremos."

n "Luego iré a la universidad, espero."

n "Recuerdo mi fallido intento de averiguar lo que Emi planea hacer luego de la preparatoria."

n "Hmm, ella evitó el tema con destreza, si mal no recuerdo."

n "Demonios, parece que cada vez que presiono demasiado, ella baila alrededor del tema."

n "O me distrae… de otras maneras."

n "Como unos días atrás durante el almuerzo, cuando Rin no estaba…"

n "Jeje."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide None
window show None

stop music fadeout 0.2

show yuuko happy_up
with vpunch

yu "¡Lo conseguí!"

"Soy expulsado de mi ensueño por el grito triunfante de Yuuko."

hi "¡Ah!"

show yuuko panic_up
with charachange

"Yuuko se ve mortificada por mi repentino sobresalto."

play music music_happiness fadein 2.0

yu "¡Ay, Dios!"

show yuuko panic_down
with charachange

yu "¡Lo lamento tanto! Acabo de… y realmente no iba… y es solo que—"

"Mientras tartamudea, me muevo para calmarla rápidamente antes de que se agite demasiado."

hi "Guau, oye."

"Mis palabras parecen inefectivas."

"Yuuko continúa convirtiéndose en un completo frenesí."

show yuuko panic_up
with charachange

yu "Y es una biblioteca y yo no debería—"

hi "Tranquila, solo cálmate."

show yuuko cry_down
with charachange

yu "Y realmente estoy dando un mal ejemplo, y ahora me despedirán porque no puedo hacer nada bien—"

hi "¡YUUKO!" with vpunch

show yuuko worried_up
with charachange

"Gritar parece funcionar, aunque atraigo la ira de varias personas que estudiaban en la biblioteca."

"Yuuko se pone alerta de inmediato, como un soldado que acaba de escuchar al capitán gritar una orden."

show yuuko neurotic_up
with charachange

yu "¡Lo siento! ¡Lo siento!"

hi "Cálmate, está bien."

hi "Simplemente me asustaste un poco, y es solo porque estaba soñando despierto en vez de estudiar."

hi "Así que en realidad hiciste que volviera a mis deberes."

"Esta es una completa mentira. Pero parece funcionar."

show yuuko worried_down
with charachange

"Yuuko respira profundamente y parece calmarse un poco."

"Aunque sigue moviéndose alrededor con una energía nerviosa que me parece terriblemente familiar."

hi "En fin, ¿qué fue lo que te puso tan emocionada?"

show yuuko neutral_up_close
with characlose

yu "¡El Gato Ladrón de Yamaku!"

"Hay que reconocerlo, Yuuko consigue transmitir su intensa emoción en un susurro."

show yuuko closedhappy_up_close
with charachange

yu "¡Creo que sé quién es!"

show yuuko happy_down_close
with charachange

yu "¡Recibí un soplo anónimo de su identidad!"

yu "¡Así que espié un poco, y creo que el informante tenía razón!"

hi "¿Oh, en serio? ¿Y quién era este eh, ladrón?"

show yuuko worried_down_close
with charachange

"Yuuko cierra la boca, sacudiendo la cabeza con decisión."

yu "Nop, no te puedo decir eso."

hi "¿Por qué no?"

show yuuko worried_up_close
with charachange

yu "Es entre el ladrón y yo."

yu "No puedo arriesgarme a que le adviertas que estoy siguiéndole la pista."

yu "Él podría revelar sus cartas antes de tiempo y darse a la fuga."

yu "Y eso me dejaría sin delincuente."

"¿Cuándo empezó Yuuko a hablar como una detective curtida?"

hi "¡No le advertiría! ¿Por qué habría de importarme?"

show yuuko neutral_down
with charadistant

yu "Si tienes que preguntar eso, entonces no necesitas saberlo."

hi "Eso no tiene ningún sentido, pero de acuerdo."

hi "Felicidades, ¿supongo?"

show yuuko closedhappy_down
with charachange

yu "¡Gracias!"

show yuuko worried_up
with charachange

yu "Eh, ¿por qué?"

hi "Por eh, ¿el asunto del gato ladrón?"

show yuuko smile_down
with charachange

"Yuuko asiente y sonríe agradecidamente."

yu "¡Entonces! ¿Estudiando para los exámenes?"

hi "Bueno, ese era el plan. Aunque no estoy teniendo mucha suerte."

show yuuko worried_down
with charachange

yu "¿En serio? ¿Es porque no puedes encontrar un libro?"

show yuuko panic_up
with charachange

yu "¡Lo siento mucho!"

yu "¡He querido limpiar las estanterías desde hace semanas, pero sigo distrayéndome!"

yu "¡Lo lamento tanto!"

hi "Guau, espera."

hi "No es eso. Tengo mi libro justo aquí."

"Para demostrar mi punto y con suerte tranquilizar a Yuuko, le muestro el libro frente a mí."

hi "Mi mente no logra concentrarse, es todo."

show yuuko worried_up
with charachange

yu "¿Es por el ruido que hay aquí?"

yu "Estoy intentando ser más estricta con los niveles de ruido, pero no consigo gritarle a la gente…"

show yuuko worried_down
with charachange

yu "Quiero decir, ¿no son sus vidas lo suficientemente difíciles sin que yo esté imponiéndoles mi autoridad?"

hi "No, tampoco es el nivel de ruido, lo prometo."

hi "Solo estoy…"

"Diablos, no lo sé."

"Preocupado por Emi."

"Preocupado por nosotros."

"Preocupado por lo que pasará luego de que nos graduemos."

hi "Emi ha estado algo rara, últimamente."

show yuuko worried_up
with charachange

yu "¿A qué te refieres?"

hi "Bueno, ¿sabes que ahora estamos saliendo?"

hi "Solo que no sé si realmente somos, ya sabes…"

hi "Una pareja. O al menos no sé si somos más que amigos."

"Aunque los amigos normalmente no hacen las cosas que nosotros hacemos."

"Físicamente somos una pareja."

"Hacemos lo que hace una pareja, al menos."

hi "Es como si cada vez que intento saber más de ella, o sobre lo que ella quiere hacer con su vida, ella esquiva la pregunta."

hi "Como el otro día, estaba hablando con ella durante el almuerzo sobre unas universidades que busqué."

hi "Y le pregunté, “¿has buscado alguna escuela últimamente?”."

hi "Ella se encoge de hombros como respuesta, dice que no, y cuando le pregunto por qué no, dice que no piensa tan a futuro."

hi "Le pregunté por qué tenía esa política, y ella…"

"De repente me doy cuenta de lo que estoy a punto de empezar a describir, y sabiamente decido cerrar la boca."

show yuuko neutral_up
with charachange

yu "¿Ella qué?"

hi "Eh, ella cambió el tema."

hi "No quería hablar de eso."

show yuuko neutral_down
with charachange

yu "¿Tal vez es un tema incómodo para ella?"

yu "O simplemente cree que no hace falta explicarlo."

hi "Sí, pero no es solo eso."

hi "Cada vez que intento averiguar qué ha estado molestándola, también cambia el tema."

hi "Es como si ella estuviera conmigo, pero no estuviera acercándose a mí."

"Ahora que lo dije en voz alta, me siento peor."

"Yuuko digiere esta información."

show yuuko worried_down
with charachange

yu "Sabes, me parece que tú eres más serio sobre esto que ella."

"Casi puedo sentir mi estómago doblarse en un nudo."

"Tiene razón."

"Eso es exactamente lo que parece."

hi "¿Pero es realmente eso lo que pasa? Quiero decir…"

show yuuko panic_up
with charachange

yu "¡Perdona! ¡Solo estoy diciendo tonterías!"

yu "¡No deberías aceptar mis consejos, apenas me conoces!"

show yuuko cry_down
with charachange

yu "¡Solo soy la bibliotecaria, y soy soltera así que puedes imaginarte que no sé de lo que estoy hablando!"

hi "No, creo…"

hi "Creo que tienes razón."

"Por más que duela simplemente considerarlo."

"Yuuko parece intentar desesperadamente encontrar una manera de disminuir un poco el impacto."

show yuuko neutral_down
with charachange

yu "Eh, mira."

show yuuko smile_down
with charachange

yu "Probablemente me equivoco, pero si quieres estar seguro de lo obviamente equivocada que estoy, ¿quizá deberías simplemente hablar con ella?"

yu "Consigue algo de tiempo a solas y pregúntale."

show yuuko closedhappy_down
with charachange

yu "¡Y tampoco la dejes cambiar de tema!"

hi "Sí, tal vez debería hacer eso."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\nO tal vez debería simplemente disfrutar de lo que tengo."

n "Nos divertimos saliendo, después de todo."

n "Y las carreras son agradables, y las otras actividades son agradables, y hablar con ella es agradable…"

n "¿Realmente necesito acercarme más a ella? Lo que tengo ahora es bastante bueno."

n "Pero eso es tonto."

n "Quiero acercarme más a ella."

n "Quiero ser capaz de ayudarla con lo que sea que esté molestándola."

n "Pero… tal vez debería esperar a que los exámenes terminen."

n "Quizá ella se anime una vez que se le pase el estrés."

n "Si lo hace, entonces no necesito preocuparme más por eso."

n "Pero si no lo hace, bueno."

n "Cruzaré ese puente cuando lo tenga ante mí."

$ renpy.music.set_volume(1.0, 2.0, channel="music")

nvl hide dissolve
nvl clear
window show

stop music fadeout 5.0

"Agradezco a Yuuko por su consejo y me encamino de regreso a mi habitación."

scene bg school_hallway2
with locationchange

"Tal vez allí podré concentrarme más en mis estudios."

scene black
with dissolve



label es_E24:

scene bg school_hallway3
with locationskip
play music music_tranquil fadein 3.0

"Salgo del aula luego de terminar mi examen final y suelto un suspiro de alivio."

"Como esperaba, los exámenes no estuvieron tan mal. Me las arreglé para pasar todos con facilidad excepto el final de Inglés."

"E incluso ese estuvo aceptable."

"Me pregunto cómo le fue a Emi."

"Más aún, cómo está; se veía terrible durante el almuerzo de hoy."

"Quiero decir, estaba bastante feliz de librarse de la silla de ruedas, pero estaba muy exhausta."

"Algo ha estado desgastándola, y estoy empezando a dudar que fueran solo los exámenes."

"Aunque, ¿debería confrontarla por eso?"

"Mi meditación es interrumpida por un toque en el hombro."

show muto smile at center
with charaenter

mu "Oye, Hisao."

label es_choiceE24:
menu:
    with menueffect
    mu "¿Tienes un minuto?"
    "Supongo que dispongo de algunos minutos.":


        return m1
    "No, ando ocupado con otras cosas.":

        return m2

label es_E24a:





hi "Sí, tengo algo de tiempo. No tengo ningún lugar importante en el que estar ni nada de eso."

show muto normal
with charachange

"Mutou alza una ceja como si cuestionara mis palabras, luego me señala que entre de nuevo en el aula."

hide muto
with charaexit

scene bg school_scienceroom
with locationchange

show muto normal at center
with charaenter

mu "Quería que me dieras tu opinión, de ser posible."

mu "Sé que este curso no estaba precisamente a tu nivel…"

hi "No se preocupe por eso. Las actividades del club de ciencias lo compensaron con creces."

show muto smile
with charachange

mu "Hmm, ¿eso crees?"

show muto normal
with charachange

mu "Bueno, de hecho de eso quería hablarte."

mu "¿Crees que fue una actividad que valió la pena? Solo para mi propia referencia."

hi "Bueno, sí, fue una buena manera de avanzar más de lo que hacíamos en clases. Definitivamente valió la pena."

show muto smile
with charachange

"Mutou se ve complacido con mi respuesta."

mu "¡Eso es genial! Exactamente la clase de respuesta que esperaba."

mu "Sabes, Hisao, me alegra que hayas venido aquí. Siempre es bueno tener a un estudiante al que realmente le guste la materia que enseñas."

mu "De cierta forma, hace que sea más tolerable tratar con el resto de los estudiantes."

mu "También eres un chico brillante. Esto es para ti como el agua para un pato, o algún otro símil semejante."

hi "Eh, gracias."

hi "Usted fue de gran ayuda. Especialmente con las cosas de la universidad."

show muto normal
with charachange

mu "Otra cosa más, Hisao."

mu "Un pequeño consejo, de un científico a otro."

hi "¿Qué pasa?"

mu "¿Qué hace un científico?"

hi "Observa el mundo a su alrededor."

show muto smile
with charachange

mu "Exactamente. Bien."

show muto normal
with charachange

mu "Una pregunta sencilla, pero una que mucha gente no parece capaz de responder. Esa es la esencia de un científico, Hisao."

mu "Nosotros observamos qué hay allí, e intentamos entenderlo."

mu "¿Pero qué pasa si hay algo que no puedes entender?"

mu "¿Qué hace un científico si no puede observar algo?"

mu "¿Cómo, por ejemplo, podemos hablar sobre quarks cuando nadie realmente ha visto uno? ¿O de agujeros negros cuando observarlos directamente es imposible?"

hi "Bueno, el instrumental científico es bastante avanzado…"

show muto irritated
with charachange

"Mutou aparta mi respuesta con irritación."

mu "No, eso no tiene nada que ver."

mu "Esas son herramientas, yo intento darte una filosofía."

show muto normal
with charachange

mu "Piensa. Si no puedes observar algo directamente, ¿entonces cómo puedes observarlo?"

hi "Eh, ¿suponiendo?"

mu "¿Cómo? ¿Cómo supondrías el movimiento de un quark? ¿En qué se basa tu suposición?"

"Por supuesto."

"Debería haberlo pensado antes."

hi "Las cosas que afecta."

show muto smile
with charachange


"Mutou aplaude y exclama con emoción."

mu "Sí, exactamente. Bien."

mu "Recuerda eso, Hisao."

show muto normal
with charachange

mu "Si no puedes examinar algo directamente, es porque lo estás mirando mal."

mu "Tienes que mirarlo de otra manera si quieres descubrir la verdad. Y si te elude, entonces mira lo que deja atrás."

mu "Esa es la esencia de ser un científico. Nunca dejamos de buscar la respuesta. Nunca des nada por sentado."

mu "Observa, experimenta, y observa un poco más."

mu "Hay muchas cosas ahí afuera que no tienen sentido, Hisao. Nuestro trabajo es hacer que tengan sentido."

mu "Al menos espero que hayas aprendido eso aquí."

hi "Creo que puedo recordar eso."

show muto smile
with charachange

"Mutou sonríe, satisfecho."

mu "Bien. Ahora ve a disfrutar de tu tiempo libre. Te lo has ganado."

stop music fadeout 8.0

scene bg school_hallway3
with locationchange

"Abandono el aula sintiéndome un poco confundido."

"¿A qué se debió eso?"

"Aunque…"

"¿Estaré pensando en este asunto de Emi de la manera incorrecta?"

"Si ella no me va a decir nada, ¿entonces puedo hacerlo de otra manera?"



label es_E24b:

hi "De hecho, tengo algo que hacer…"

show muto normal
with charachange

mu "¿Ah sí? Oh, bueno."

mu "Quería que me dieras tu opinión del club de ciencia. Pero podemos hacer eso luego, supongo."

mu "Disfruta de tu descanso, ¿me oyes?"

hi "Gracias, lo haré."

"Realmente me gustaría charlar con Mutou, pero tengo otras cosas en la cabeza."

"Específicamente, qué hacer con Emi."

"¿Realmente puedo confrontarla?"



label es_E24c:

scene bg school_dormhisao
with locationskip

"La pregunta sigue dando vueltas en mi cabeza incluso después de haber llegado a mi habitación."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\n¿Qué tal si eso la molesta?"

n "Además, ¿qué tal si no es nada?"

n "Si voy y me niego a irme hasta que ella me diga qué anda mal o algo así, ¿no estaría siendo un pesado?"

n "No quiero empezar una pelea o algo similar por algo como esto."

n "Tal vez debería olvidarme del asunto y ver cómo está ella mañana antes de hacer algo."

n "¿Sería muy malo dejarlo pasar?"

n "No es como si no disfrutáramos de nuestra mutua compañía."

n "Pero aunque suene raro, realmente quiero… ayudarla."

n "Ni siquiera sé con qué o si al menos hay algo con lo que ella necesite ayuda."

n "Pero quiero hacerlo."

$ renpy.music.set_volume(1.0, 2.0, channel="music")

play sound sfx_doorknock

stop music fadeout 2.0

nvl clear
nvl hide dissolve

window show

"De repente, me despabila un golpe en la puerta."

play sound sfx_dooropen

scene bg school_dormhallway
show kenji neutral at center
with locationchange

"Abro para ver a Kenji."

hi "Oh, eres tú."

play music music_kenji

show kenji tsun
with charachange

ke "¿Soy yo? ¿Eso es todo?"

ke "Si tuvieras una idea de las cosas por las que he pasado, lo que he hecho, estarías más feliz de verme, hombre."

ke "Quiero decir, fue una mierda épica de esas en las que puede-que-no-vuelvas-a-verme-jamás."

ke "Y tú aquí simplemente actuando como si yo hubiera ido a la tienda por algo de leche."

show kenji happy
with charachange

ke "Eres un hombre frío, Hisao. Realmente respeto eso."

hi "Eh, gracias, supongo."

show kenji neutral
with charachange

ke "Es inteligente jugar a lo seguro, sabes. No mostrar ninguna emoción."

ke "Mantén tus cartas cerca de tu pecho."

ke "A menos que sea tiempo de revelar tus cartas, o que tengas malas cartas."

ke "Entonces deberías retroceder y recoger tus ganancias."

show kenji happy
with charachange

ke "¿Entiendes?"

hi "Sí, tiene perfecto sentido."

hi "¿Supongo que la eh, misión terminó bien?"

show kenji tsun
with charachange

ke "Guau, qué entrometido de tu parte, ¿no crees?"

ke "¡No puedes simplemente andar diciendo eso! ¡Las cosas están en una etapa delicada!"

ke "Un paso en falso, y, ¡BUM! ¡La invasión tiene éxito!"

hi "¿Pensé que ibas a volar la conspiración por los aires?"

ke "Es más grande de lo que pensé; necesito actualizar mis datos."

ke "Y probablemente cambiar algunas de las marionetas."

show kenji happy
with charachange

ke "¿Quieres ayudar? Tengo un poco de whiskey de… un lugar."

ke "Puedes informarme de todo lo que haya revelado tu investigación."

hi "Eh, mejor no. Se supone que eh… me vea con ella hoy."

hi "Debo hacer eso. No puedo levantar sospechas."

show kenji neutral
with charachange

"Kenji asiente en señal de aprobación."

ke "¿Sigues manteniéndolas cerca de tu pecho, eh? Está bien, hombre, respeto eso."

ke "Buena suerte."

hi "Eh, gracias."

hide kenji
with charaexit

stop music fadeout 4.0

"Voy a pretender, por el bien de mi propia cordura, que él me está deseando suerte en mi conversación con Emi."

"Y si lo miro de otra manera, toda esa analogía de las cartas de la que él estaba hablando sirve aquí."

"Hora de ponerlas todas sobre la mesa."

"O, más bien, de ver si puedo lograr que Emi lo haga."

"Con algo que se aproxima a la resolución, me dirijo a la habitación de Emi."

scene bg school_girlsdormhall
with locationskip

play sound sfx_doorknock2

"Subo por las escaleras que llevan a su habitación y toco en su puerta."

emi "¿Q-quién está ahí?"

play music music_drama fadein 8.0

"Huh. Eso es extraño. Su voz suena un poco ahogada."

hi "Hola, soy yo. Pensé en pasar por aquí."

emi "¿Hisao?"

emi "¡Entra!"

"Estiro la mano para abrir la puerta, solo para encontrarme con que está cerrada con llave."

"Más y más curioso."

hi "Eh, tu puerta está cerrada con llave."

emi "Oh, sí, perdona. Dame un minuto."

show emi basic_grin:
    tworight
    xpos 0.8
    easein 0.5 tworight
with charaenter

"Pasados unos instantes, Emi abre la puerta, sonriendo."

emi "Perdona, tenía que ponerme las piernas. Estaba tomando una siesta."

"A pesar de su sonrisa, hay algo que definitivamente no encaja."

"Los ojos de Emi están levemente enrojecidos, y parece que ha estado llorando."

hi "Oh, no importa."

hi "Eh, ¿estás bien?"

show emi sad_shy at tworight
with charachange

emi "¿Huh? ¡Sí, estoy bien!"

hi "Es solo que te ves como si hubieras estado llorando…"

"Oh, seguro, Hisao. Ese es un excelente comienzo."

show emi sad_grin at tworight
with charachange

emi "¿Qué? Nah, estoy bien. Solo estoy feliz de verte."

scene ev emi_firstkiss
with flash

"Ella puntúa esto con un largo beso que continúa mientras la puerta se cierra de golpe detrás de nosotros."

"Sé lo que ella quiere hacer ahora, y a la vez estoy dolorosamente consciente de lo mucho que yo también quiero hacerlo, pero…"

scene bg school_dormemi at left
show emi excited_amused_close at center
with locationchange

"Rompo el beso con un impulso de autocontrol que casi me mata."

hi "Oye, espera."

show emi basic_confused_close
with charachange

"Emi frunce el ceño por la confusión."

emi "¿Eh? ¿Esperar qué?"

hi "Tenemos que hablar."

show emi sad_grin_close
with charachange

emi "¿No se supone que esa es mi línea?"

show emi sad_shy_close
with charachange

emi "¿Y que nunca es algo bueno?"

"Ella tiene razón."

"Usualmente es lo que inicia una separación."

"O el preludio de una pelea."

hi "Tal vez pueda ser algo bueno esta vez."

hi "Eh, eso espero, de todas maneras."

show emi sad_shyblush_close
with charachange

emi "Ah… ajá."

show emi basic_grin_close
with charachange

emi "¿Podríamos al menos sentarnos en la cama? Es mi primer día de vuelta sobre estas cosas, y todavía estoy reajustándolas."

show emi basic_closedgrin_close
with charachange

emi "Además el enfermero dijo que debería tratar de usarlas menos, ya que las carreras ponen más tensión sobre ellas."

hi "No puedo decir que no a eso."

"Es una trampa, ambos lo sabemos, y ambos lo pasamos por alto."

"Por otra parte, es terriblemente difícil enojarse mientras estás en la cama con el objetivo de tus afecciones, así que tal vez también está esa motivación."

hide emi
with charaexit

show bg school_dormemi at right
with charamove

show emi basic_grin_close:
    center
    ypos 1.0
    easein 0.5 ypos 1.1
with charaenter

"Acomodo las piernas de Emi junto a la cama y me siento a su lado, colocando un brazo sobre sus hombros."

"En silencio, simplemente disfrutamos poder estar en esta posición de nuevo por unos cuantos minutos."

"Luego, por supuesto, debo arruinarlo abriendo la boca."

hi "Mira, yo sé que… que no has estado pasándola muy bien últimamente."

hi "Y quiero ayudarte."

hi "Pensé que eran solo los exámenes haciendo mella en ti, pero ahora vengo a tu habitación y has estado llorando, y eso me mata."

hi "Pero no puedo hacer nada si tú no me hablas de ello."

show emi basic_closedgrin_close:
    ypos 1.1
with charachange

emi "Ya te dije, estoy bien."

hi "No, no lo estás. Es obvio que algo te está consumiendo."

hi "Puedes decirme, lo sabes."

"Hay un levísimo aumento en la tensión de la voz de Emi."

show emi sad_shy_close
with charachange

emi "¿Por qué no es suficiente que diga que estoy bien?"

show emi sad_annoyed_close
with charachange

emi "Estás preocupado, lo entiendo. Está bien."

emi "Pero me siento bien, y no es nada por lo que debas preocuparte."

hi "No dormir y distraerse más que Rin no me parece “sentirse bien”."

hi "Yo solo… Quiero ayudar."

emi "Ah-eh."

hi "Sí, no me gusta verte así."

hi "Quiero que seas feliz, ¿sabes?"

show emi basic_annoyed_close
with charachange

"Tengo la sensación de que eso salió mal, porque Emi me clava una mirada gélida."

emi "¿Entonces quieres arreglarme, Hisao?"

"Ahora definitivamente se está enojando."

show emi sad_grit_close
with charachange

emi "¿Quieres irrumpir con tu blanco corcel y salvar el día?"

emi "¿Detener las pesadillas, el dolor de los miembros fantasma?"

show emi sad_angry_close
with charachange

emi "¿Restaurar lo que se ha perdido?"

show emi sad_depressed_close
with charachange

"Su voz se atora en su garganta, y las lágrimas empiezan a rodar."

emi "Bueno {b}no puedes{/b}."

show emi sad_pout_close
with charachange

emi "Nadie puede."

emi "Nadie lo hará."

"Estoy tan impactado por su repentino ataque verbal que permanezco callado."

"Ninguno de los dos dice nada por un rato."

"Estoy sorprendido de que Emi me abrace más fuerte en vez de empujarme."

"Luego de un profundo respiro, ella empieza a hablar de nuevo."

show emi sad_shy_close
with charachange

emi "Mira, lo lamento."

show emi sad_depressed_close
with charachange

emi "Yo solo… tengo estas pesadillas."

emi "Sobre el accidente."

"Ah. El accidente. Debí haberlo sabido."

"Se llevó sus piernas, después de todo, pero nunca viene al tema, por supuesto."

show emi sad_pout_close
with charachange

emi "Y usualmente me las arreglo bien con ellas, porque puedo correr."

emi "Correr despeja mi mente como ninguna otra cosa."

emi "No tengo que preocuparme por nada cuando estoy corriendo."

emi "Solo me concentro en respirar, en el ritmo de las cosas."

emi "Es más fácil de esa manera. La vida es más fácil de esa manera."

show emi sad_shy_close
with charachange

emi "Solo seguir moviéndose hacia adelante, ¿sabes? Nada más importa, solo vencer la siguiente curva."

emi "Y luego está la siguiente curva, y la siguiente, y la siguiente, hasta que no pueda seguir más, o pensar más, o hacer nada más que bajar la velocidad y caminar hasta que pueda recuperar el aliento de nuevo."

emi "Luego de algo como eso, nada más importa."

show emi basic_annoyed_close
with charachange

emi "Pero he estado atorada en esa maldita silla de ruedas por demasiado tiempo. Así que, ningún escape."

show emi sad_shy_close
with charachange

emi "Hoy simplemente se desbordó un poco."

hi "Podrías haberme hablado de eso, sabes."

hi "No tenías que pasarlo sola."

show emi sad_grin_close
with charachange

"Emi sonríe tristemente, como si intentara explicarle a un niño que todos los fuegos queman."

emi "Sí, tenía que hacerlo. Y lo haré."

hi "¿Pero por qué?"

hi "¿Por qué tienes que seguir atravesando esto sola?"

hi "¿Por qué no puedes confiar en mí lo suficiente como para dejarme ayudarte?"

"Esa sonrisa de nuevo."

show emi excited_amused_close
with charachange

show emi sad_grin_close
with charachange

"Emi se inclina sobre mí y me besa en la mejilla, un gesto casi maternal."

"Ella deja su boca cerca de mi oreja, mientras me confiesa una cosa."

show emi sad_shy_close
with charachange

emi "Porque sí, Hisao."

emi "Todo lo que tenía ya fue arrancado de mí una vez."

show emi sad_depressed_close
with charachange

emi "No sé qué haría si sucediera de nuevo."

"Ella se detiene, como insegura de si debería continuar o no."

"Puedo sentir una agitación violenta en mis entrañas."

"Ella continúa."

show emi sad_shy_close
with charachange

emi "Así que no puedo depender de ti."

emi "O del enfermero."

emi "O de nadie más."

show emi sad_pout_close
with charachange

emi "Solo yo."

emi "Así es como debe ser."

"Habiendo dado este corto discurso, ella mira hacia abajo y cubre su boca con la palma de su mano."

"La conversación está claramente finalizada. Busco algo que decir, pero no puedo pensar en nada."

hi "Yo…"

hi "Tal vez debería irme, por ahora."

hi "Tengo… cosas."

"Emi ni siquiera mira hacia arriba."

"Ella suena cansada, o aliviada."

"No puedo decir cuál."

emi "De acuerdo, Hisao."

emi "Ve a ocuparte de esas cosas."

emi "Te veré mañana."

hide emi
with charaexit

with Pause(0.2)

show bg school_dormemi at left
with charamove

"Bajo de la cama y me dirijo a la puerta, deteniéndome bajo su umbral."

hi "Oye, Emi…"

show emi sad_shy at tworight
with charaenter

emi "¿Sí?"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\nQuiero decir mil cosas."

n "Aunque estoy demasiado confundido como para decir ninguna."

n "Luego de escucharla admitir que nunca me dejará acercarme, siento como si {b}mi{/b} mundo hubiera sido arrancado de mí."

n "¿Qué pasó en ese accidente?"

n "Sé que perdió sus piernas, pero eso nunca parece haberla molestado."

n "¿Qué pasó allí?"

n "¿Qué asusta tanto a una chica como para que no acepte ayuda de nadie, ni siquiera de alguien que ama?"

n "No lo sé."

n "\nPero quiero saberlo."

n "Tengo tantas ganas de saberlo que no poder recibir esa respuesta se siente como un cuchillo en mis tripas."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve
window show

emi "¿Hisao?"

emi "¿Ibas a decir algo?"

"Aún estoy bajo el umbral de la puerta."

hi "… Nada."

hi "Olvídalo."

scene bg school_girlsdormhall
with locationchange

play sound sfx_doorclose
stop music fadeout 6.0

"Y estoy cerrando la puerta."

"Y caminando por el pasillo."

"Bajando las escaleras."

scene bg school_dormext_full_ni
with locationskip

"Saliendo por la puerta."

"Hacia la oscuridad."

scene bg school_dormhisao_ni
with locationskip

play music music_night fadein 1.0

"De algún modo deambulo de regreso a mi propia habitación. Mi cerebro moviéndose a un kilómetro por minuto, yendo rápidamente a ningún lugar."

window hide
nvl clear
nvl show dissolve

n "\n\nNo se me ocurre cómo lidiar con esto."

n "Pensé que seguir adelante era algo bueno."

n "Habitar menos en un pasado que no puedo cambiar. Vivir en el presente y ver hacia el futuro."

n "\n\nLuego de este… asunto con Emi, ya no estoy tan seguro."

n "Ella decía la verdad. Es más fácil ver hacia la siguiente curva, ignorando el camino transcurrido."

n "Sin preocuparse por el oponente que se quedó atrás. Sin fijarse en los espectadores en el banquillo."

n "Y también, desafortunadamente, sin tiempo para ayudar a los compañeros rezagados."

nvl clear
nvl hide dissolve
window show

"Me tiro en la cama, mirando hacia una esquina de mi techo como si las respuestas que quiero estuvieran escritas allí."

"No tengo esa suerte, por supuesto."

window hide
nvl clear
nvl show dissolve

n "\n\n\n\n\nElla está literalmente huyendo de algo, ¿pero no he estado haciendo yo lo mismo, dando lo mejor de mí para olvidar mi hospitalización?"

n "Estoy mejorando, pero mi salud no se va a arreglar mágicamente."

n "\nEmi debe arreglárselas con dos piernas en vez de un corazón, pero esas tampoco se van a arreglar mágicamente."

n "\nTal vez esto es lo más arreglados que podamos llegar a estar."

nvl clear
nvl hide dissolve
window show

"La habitación se oscurece más y más, hasta que realmente no puedo decir si sigo viendo hacia una esquina."



label es_E25:

scene bg school_dormhisao
with shorttimeskip

"La mañana llega demasiado temprano, encima de una noche sin dormir."

"¿Es así como Emi ha estado pasando sus noches?"

"Mirando hacia la pared, o al techo. Intentando dejar de pensar en lo que sea que piensa."

"Ella, en mi caso."

"Esa sensación de presión en mis entrañas aún está ahí."

window hide
nvl clear
nvl show dissolve

n "\n\n“No puedo depender de ti”."

n "\nPalabras dichas tan casualmente."

n "Es casi como si estuviera bromeando conmigo, o regañándome por sugerir que la Tierra es plana."

n "\n“Así es como debe ser”."

n "\nLa forma en que debe ser apesta."

n "Me siento tan miserable que estoy a punto de decidir saltarme la carrera."

n "Aunque eso sería estúpido. No es algo que haga solo por verla a ella."

n "Claro, esa era la razón original, pero ahora es algo más."

nvl clear

n "\n\n\n\nHe empezado a disfrutar de la carrera misma."

n "Hay peores maneras de poner a circular la sangre, de cualquier modo."

n "Nunca pensé que lo diría después de la primera semana, pero—"

n "\nMe siento mucho mejor después de una carrera, como si sin importar qué otra cosa haga hoy, al menos habré hecho eso."

n "También me despierta. La misma Emi dijo que correr siempre despeja su mente. Tal vez me ayude a despejar la mía."

n "\nEso espero."

nvl clear
nvl hide dissolve

scene bg school_track
with locationskip

window show

"La mañana está fresca y despejada, un poco húmeda, tal vez. El verano haciendo acto de presencia, o eso parece."

"Emi ya está estirando cuando llego, y me saluda con una sonrisa y un gesto."

show emi basic_closedgrin_gym at center
with charaenter

emi "¡Hola, Hisao!"

"El verla así de feliz es como una patada en los huevos."

"¿Cómo puede estar tan alegre después de lo de ayer?"

show emi excited_amused_gym_close
with characlose

"Apenas si consigo saludar y me sorprende recibir un abrazo."

show emi sad_shy_gym_close
with charachange

emi "Oye, sobre lo de anoche."

"Aquí viene."

stop music fadeout 1.0

show emi basic_grin_gym_close
with charachange

emi "Quería decir gracias."

show emi excited_happy_gym_close
with charachange

emi "En realidad logré dormir por primera vez en un tiempo, y creo que fue por nuestra conversación."

show emi basic_closedgrin_gym_close
with charachange

emi "Así que, gracias."

play music music_rain fadein 4.0

"¿Cómo pudo dormir mejor luego de nuestra charla?"

"Ella básicamente me dijo que no se acercaría más a mí."

"¿Y eso le permitió dormir mejor?"

"Perdóname, ¿pero qué demonios?"

"O Emi no nota mi desconcierto o elige no hacerlo."

"Con ella ya no puedo saberlo."

hi "Oh, no pasa nada. Me alegra que haya ayudado."

"El veneno que amenaza con inundar mi voz está controlado por ahora, pero creo que mejor empiezo a correr ya, antes de que haga algo estúpido."

scene bg school_track_on
with locationchange

"Emi se ve igual de dispuesta a empezar, y en poco tiempo estamos corriendo por la pista."

"Puedo notar que está más relajada."

scene ev emi_run_face:
    truecenter
    zoom 1.0 subpixel True
    acdc_warp 20.0 zoom 1.1
with flash

"Su forma de correr ha regresado a los movimientos más agraciados que recuerdo cuando la vi por primera vez."

"Es un marcado contraste con la forma casi brutal en la que había estado lanzándose a la pista estos últimos días."

"Nuestra conversación realmente parece haberla ayudado."

"Una lástima que no pudiera ayudarme a mí."

"Me acoplo al ritmo de la carrera, recordando cuando no podía permitirme pensar en nada más que en mantener mi respiración estable y mis piernas moviéndose."

"Supongo que esos días ya terminaron."

"Al menos por las primeras dos vueltas."

scene bg school_track_running
with Dissolve(2.0)

"Molesto por el poco éxito que estoy teniendo en despejar mi mente, aumento el ritmo."

"Ah, ahí está la sensación de ardor en mis piernas."

"La respiración furiosa en mi pecho, el embate de mi corazón. Con el cual aún debo ser cuidadoso."

"Pero parece ser que se ha vuelto más fuerte; puedo sentirlo bombeando sangre a través de mis venas."

"El sonido reverbera en mis oídos, pero en vez de entrar en pánico como lo hice aquel día en la nieve, me lleno de júbilo."

"¡Sí, está funcionando! Mi corazón, esa falla fatal que me trajo aquí, ha mejorado."

"Ahora soy capaz de seguir adelante, y quizá algún día seré capaz de dejar de preocuparme tanto."

"Ahora mismo, no importa que no tenga ni idea de qué hacer conmigo y con Emi."

"Todo lo que importa es que mis brazos y piernas continúan funcionando al unísono."

"Nada más."

show bg school_track_on
with locationchange

"Cuando llego al tramo final, me recuerdo a mí mismo que correr realmente ayuda, aunque no tanto como esperaba."

"Sí me siento mejor, y mientras camino unas cuantas vueltas para enfriarme, empiezo a recordar la noche anterior de una forma menos emocional."

"Emi quiere que yo me mantenga distante."

"Yo no podría hacer eso."

"Tiene que haber una forma de evitar esto, algún tipo de terreno neutral al que pueda llegar."

"Aunque no estoy seguro de cuál es ese terreno neutral."

"Diablos, casi me sentía optimista."

show emi excited_joy_gym at center
with charaenter

emi "¡Buena carrera, Hisao! ¡Realmente has mejorado!"

"Buena carrera. Eso es todo lo que puedo esperar por ahora, ¿no es verdad?"

"Felicidades, Hisao. Eres patético."

"Debo cambiar mi actitud."

hi "Bueno, ya sabes. Soy sumamente asombroso."

"Y aun así sigo diciendo cosas que no quiero decir."

"De un momento a otro seré tan bueno ocultando mis problemas como Emi."

show emi basic_closedgrin_gym
with charachange

emi "Me gusta pensar que lo eres."

"¿Por qué me dice eso? ¿Decir algo como eso con un cariño tan real en su voz que hace brincar a mi corazón?"

"No lo dice en serio. No puede."

"Debo estar haciendo un peor trabajo del que esperaba, porque Emi me mira con atención."

show emi basic_confused_gym
with charachange

emi "Oye, ¿te sientes bien?"

show emi basic_hes_gym
with charachange

emi "Tal vez deberíamos ver al enfermero, ¿eh?"

hi "Sí, no me gustaría desmayarme junto a ti."

"Emi se ve algo sorprendida por mi tono amargo."

show emi basic_shock_gym
with charachange

emi "¡No digas cosas como esas!"

show emi sad_shy_gym
with charachange

emi "Ya lo hiciste una vez antes, sabes."

"¿Por qué actúa tan cariñosa?"

"En realidad no le importa, pensé que ella había dejado eso claro."

"Pero a pesar de todo termino disculpándome, aun cuando no debería hacerlo. Aun cuando ella probablemente esté fingiendo."

hi "Perdona, jeje."

hi "Vamos, veamos al enfermero."

"No consigo calmarme en todo este rato."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\n\n\nCada vez que se siente como si ya hubiera superado lo que pasó anoche, Emi hace o dice algo que demuestra cariño, y regreso al principio de nuevo."

n "La imagen de ella terminando esa conversación me persigue."

n "Fue como el último giro de la cuchilla que me despojó de cualquier esperanza de que Emi y yo pudiéramos ser algo más de lo que somos."

n "¿Y qué somos en este momento? Poco más que amigos que casualmente tienen sexo."

n "Y de verdad, no es como si no disfrutara el tiempo que paso con ella. Yo mismo dije eso el otro día."

n "Estuve muy cerca de no sacar el tema a conversación con ella, iba a seguirle la corriente y dejarlo pasar, ¿no es verdad?"

stop music fadeout 2.0

nvl clear
nvl hide dissolve

scene bg school_nursehall
with shorttimeskip

window show

"Con esta carrera en mi cabeza, me encuentro enfrente de la oficina del enfermero, todavía meditando mientras él revisa a Emi."

"Emi sale saltando por la puerta, me da un beso, y sale disparada a tomar una ducha, supongo."

"Mientras tanto, el enfermero me hace señas para que entre en su oficina para hacerme la revisión habitual."

$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_nurse fadein 0.5

scene bg school_nurseoffice
show nurse neutral at center
with locationchange

nk "¿Algún problema hoy?"

hi "Nah. Incluso me esforcé un poco más que de costumbre, y parece que pude arreglármelas."

show nurse grin
with charachange

nk "Eso es arriesgado y poco característico viniendo de ti, Hisao."

nk "Has estado saliendo demasiado con Emi. Ella te lo ha contagiado, y no necesariamente de buena manera."

"A la mención del nombre de Emi, no puedo evitar fruncir el ceño con amargura a pesar de mis esfuerzos para controlarlo."

show nurse fabulous
with charachange

nk "Vaya, vaya. Eso es nuevo, ¿no crees?"

show nurse neutral
with charachange

nk "La última vez que me fijé, tu respuesta usual al nombre de Emi era una sonrisa, no un ceño."

show nurse concern
with charachange

nk "¿Exactamente qué pasó entre ustedes dos? Porque Emi no parece afectada por eso, sea lo que sea."

show nurse neutral
with charachange

nk "Ella se ve más relajada de lo que la he visto en semanas, lo que es inusual para esta época del año."

hi "¿A qué te refieres con eso?"

show nurse fabulous
with charachange

nk "¿Con qué?"

hi "“Para esta época del año”. Sigo intentando descubrir qué ha estado molestándola, pero ella se calla como un muerto cuando abordo el tema."

hi "Y anoche, ella dijo—"

show nurse neutral
with charachange

nk "Déjame adivinar. ¿No te lo dirá, porque dice que no puede confiar en ti?"

nk "Y ahora estás angustiado, porque pensaste que ustedes dos eran mucho más de lo que ella cree, ¿cierto?"

hi "Eh, más o menos."

hi "¿Cómo diablos lo supiste?"

show nurse grin
with charachange

nk "Hisao, soy el enfermero. Es mi trabajo saber estas cosas."

show nurse neutral
with charachange

nk "Además, he conocido a Emi por suficiente tiempo como para saber que intentaría hacer algo así; así es ella."

"Él dice esto con un tono medio cariñoso, medio frustrado que se vería más apropiado si tuviera un cigarrillo colgando de sus labios."

"A como están las cosas, parece dispuesto a conformarse con un bolígrafo."

show nurse fabulous
with charachange

label es_choiceE25:
menu:
    with menueffect
    nk "Mira, ¿te molesta si te doy un consejo?"
    "Claro, ¿por qué no?":


        return m1
    "No, este es mi problema.":

        return m2


label es_E25a:





"¿Qué fue lo que dijo Mutou ayer?"

"¿Si no puedes observar el objeto, observa lo que hay a su alrededor?"

"Vale la pena intentarlo."

"El enfermero conoce a Emi mejor que yo, estoy seguro."

hi "Claro, acepto sugerencias."

hi "Honestamente, estoy algo perdido."

hi "No tengo idea de cómo hacer frente a esto."

show nurse grin
with charachange

nk "Nunca lo habría adivinado."

"Sonríe cuando dice esto. Creo que está bromeando."

show nurse neutral
with charachange

nk "Mira, el asunto es: Emi es… terca."

show nurse grin
with charachange

nk "Deberías saber eso a estas alturas, si no entonces eres muy poco observador, pero te daré el beneficio de la duda esta vez."

hi "Estoy muy agradecido."

show nurse neutral
with charachange

nk "De todas formas, si ella decidió que no quiere hablar sobre lo que pasó, entonces ella no va a hablar sobre lo que pasó."

nk "¿Ha dicho algo de qué la ha estado molestando? ¿Aunque sea una pista?"

hi "Bueno, ella dijo que ha estado teniendo pesadillas sobre el accidente…"

show nurse fabulous
with charachange

nk "¿En serio? Entonces estás progresando. Eso es bueno."

show nurse neutral
with charachange

nk "Bueno, supongo que puedo decirte esto sin violar mi estricta política de cero interferencias cuando se trata de Emi tomando decisiones estúpidas."

show nurse concern
with charachange

nk "El aniversario de su accidente será pronto."

nk "Ella se deprime por estas fechas, porque fue un evento muy traumático, considerando lo que ha perdido."

hi "Esa es otra cosa. Ella se comportó como si hubiera perdido más que solo sus piernas. ¿Qué ocurrió?"

show nurse fabulous
with charachange

nk "¡Guau! Nop, no me meteré en eso. Tendrás que preguntárselo a alguien más, porque esa es la caja de Pandora y no pienso abrirla."

show nurse neutral
with charachange

nk "Si Emi quiere que lo sepas, te lo dirá a su debido tiempo."

nk "Solo debes ser paciente, eso es todo."

hi "¿Por qué estás ayudándome con todo esto?"

show nurse grin
with charachange

nk "Porque eres bueno para ella. Ella confía en ti, aunque no lo creas."

nk "Y en estos momentos eres el que tiene mayores posibilidades en toda la escuela de ayudarla a atravesar esta época del año."

show nurse neutral
with charachange

nk "Ella no aceptará mi ayuda, pero puede que acepte la tuya si no lo arruinas."

show nurse fabulous
with charachange

nk "Así que no lo arruines, ¿entendido?"



label es_E25b:

"¿Un consejo? ¿Sobre qué? No creo que haya nada que yo pueda hacer respecto a esto."

hi "En realidad no. No creo que haya algo que puedas decir que me sea de ayuda."

show nurse neutral
with charachange

nk "Nunca se sabe, Hisao."

hi "No, creo que tengo una idea bastante clara."

hi "Emi solo está siendo testaruda con algunas cosas, y está molestándome, pero lo superaré."

hi "No te preocupes por nosotros."

show nurse concern
with charachange

"El enfermero no parece creerme, pero se encoge de hombros."

nk "Hazlo a tu manera, muchacho."



label es_E25c:

$ renpy.music.set_volume(0.3, 0.0, channel="sound")
play sound sfx_hammer

"Abro la boca para responder pero un golpeteo en la puerta me interrumpe."

emi "Oigan, ¿aún siguen aquí?"

show nurse grin
with charachange

nk "Solo un minuto, Emi."

nk "Danos un segundo para ponernos los pantalones de nuevo."

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_doorslam

show emi invis:
    tworight
    xpos 1.0
with None

show bg school_nurseoffice at bgleft
show nurse grin at twoleft
show emi basic_annoyed_gym at tworight
with dissolvecharamove

"La puerta se abre de golpe y Emi lanza una mirada gélida al enfermero."

emi "Imbécil."

show nurse fabulous
with charachange

nk "No quería hacerte ilusiones."

hi "Oigan, ¿pueden… dejarme fuera de esto?"

hi "Como sea, ¿qué ocurre, Emi? ¿Olvidaste algo?"

"Intento adoptar un tono más alegre con ella."

"No hace falta preocuparla. Dos pueden jugar al juego de “todo está bien”."

show emi sad_grin_gym at tworight
with charachange

emi "En realidad olvidé preguntarte algo."

hi "¿Oh? ¿Qué pasa?"

show emi basic_happy_gym
with charachange

emi "¿Quieres venir de viaje conmigo a mi casa?"

show emi basic_closedgrin_gym
with charachange

emi "Mi mamá está haciendo la cena, y pensé que tal vez querías acompañarnos."

show nurse grin
with charachange

nk "Bueno, por supuesto que acepto."

show emi basic_closedgrin_gym:
    parallel:
        "emi excited_proud_gym" with Dissolve(0.2, alpha=True)
    parallel:
        ease 0.2 xpos 0.6
        ease 0.2 tworight
with Pause(0.5)

"Emi golpea al enfermero en el brazo juguetonamente."

emi "No tú, idiota. Fuiste la semana pasada."

show emi sad_grin_gym at tworight
with charachange

emi "Le hablaba a Hisao."

show nurse neutral
with charachange

nk "¿Oh? ¡Qué interesante! ¡Conocer a los padres!"

hi "Me encantaría ir, Emi. Gracias."

show nurse fabulous
with charachange

"El enfermero alza una ceja, pero no dice nada."

emi "¡Genial! ¡Estaré en mi habitación, pasa luego de bañarte y ponerte algo limpio y tomaremos el autobús!"

hi "Suena bien. ¡Te veré en un rato!"

stop music fadeout 2.0

show emi excited_amused_gym_close
with characlose

"Esta vez soy yo el que se inclina para darle un beso rápido antes de salir disparado hacia mi habitación."

scene bg school_dormhisao
with locationskip

"Vaya novedad más interesante."

"Quizá nos estamos volviendo más íntimos después de todo."

"Quizá Emi al fin esté lista para ablandarse un poco."

"O quizá solo esté siendo amable, y una cena gratuita parece una buena forma de disculparse por lo de ayer."

"Genial. Ahora no puedo decidir si estar emocionado, nervioso, o deprimido."

"Me decido por una combinación de las tres y me meto en la ducha."

scene black
with dissolve

$ suppress_window_after_timeskip = True



label es_E26:

window hide None

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_businterior fadein 2.0

scene ev busride
with locationchange

nvl clear
nvl show dissolve

n "\n\n\nNo creo que me guste andar en autobuses."

n "En realidad, me siento muy cómodo diciendo eso con total certeza."

n "Se balancean mucho, y huelen raro, y puedes sentir cada hueco en la carretera."

n "Realmente no me apasiona mucho esto."

n "\nAdemás las piernas de Emi siguen haciendo un sonido metálico que atrae la atención de todas las demás personas en el autobús."

n "Otra vez lleva pantalones cortos, y medias largas extendidas hasta sus prótesis para que estas no se vean tan obviamente falsas de nuevo."

n "Pero eso no detiene las dos o tres miradas extrañas cada vez que sus piernas chocan con un audible chasquido."

nvl clear

n "\n\n\nMe muevo nerviosamente en mi asiento, y Emi alza una ceja inquisitivamente."

n "A ella no parecen importarle las miradas, eso o ni siquiera nota que la gente está mirando."

n "Estoy seguro de que ya ha tenido suficientes miradas extrañas antes. Luego de cierto tiempo, dudo que siga notándolas."

n "\n\nNo es como si me lo fuera a decir si le preguntara."

n "Otro cosa que sé con certeza es que no solo estoy incómodo por el autobús."

n "Al parecer no puedo aceptar el hecho de que Emi parece estar intentando acercarse a mí mientras al mismo tiempo me empuja lejos."

nvl clear



label es_E26a:

n "\n\n\nEl enfermero dijo que ella confiaba en mí, aunque no lo pareciera."

n "Pero no estoy seguro de poder confiar en el enfermero."

n "Él es protector con Emi, igual a como yo soy protector con Emi, y si alguien me preguntara sobre ella probablemente diría algo que la hiciera verse bien."

n "\nAsí que él podría estar haciendo eso mismo."

n "\nAun así, había algo con la forma en la que se veía genuinamente sorprendido de que Emi me invitara…"

n "Tal vez la conversación de anoche ayudó más de lo que creía, pero aún estoy preocupado."


label es_E26b:

stop ambient fadeout 12.0

nvl clear

n "\n\n\nConocer a los padres es algo importante, ¿verdad?"

n "No es como si no hubiera conocido ya a la madre de Emi, pero eso solo fue un encuentro casual."

n "Ahora será como el novio de Emi, con todo lo que eso implica."

n "Puedo sentir mi corazón retumbar en mi pecho, un eco de aquella tarde cubierta de copos de nieve, la cual se siente como si hubiera sido hace tanto tiempo que bien podría haber ocurrido completamente en otra vida."

n "Solo que en ese entonces no sabía qué ocurría; tampoco tenía medicamentos para prevenir que las cosas se salieran de control."

n "He progresado mucho en términos de salud física, y por segunda vez hoy, siento como si ahora fuera capaz de vivir normalmente, o al menos lo más normalmente posible."

n "\nAhora, si tan solo pudiera manejar mi relación tan bien como he manejado mi corazón, estaría en muy buena forma."

stop ambient fadeout 1.5

window hide None

nvl clear
nvl hide dissolve

scene bg city_street4
show emicas smile_close at center
with shorttimeskip

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_traffic fadein 2.0

window show

emi "Bueno, llegamos."

play music music_soothing fadein 2.0

"Emi toma mi mano tan pronto nos bajamos del autobús. Ella empieza a caminar casi de inmediato."

show emicas wink_up_close
with charachange

emi "Vamos, faltan unas cuantas cuadras más hasta mi casa."

hi "¿Qué? Oh, de acuerdo."

scene bg city_alley
with locationchange

stop ambient fadeout 12.0

"Sigo a Emi calle abajo, observando su paso seguro."

"Lleva un ritmo algo rápido para una simple caminata."

"Supongo que está ansiosa por llegar."

hi "Así que, ¿tu mamá hace este tipo de cosas con regularidad?"

show emicas neutral_close at center
with charaenter

emi "Nah, no muy seguido. Mamá nunca ha sido una gran anfitriona."

hi "¿Ah sí?"

show emicas awayfrown_close
with charachange

emi "Sí, era mi papá el que siempre le decía que invitara a otras personas."

"Esta espontánea y repentina referencia a su padre me toma desprevenido."

"Y por la mirada en el rostro de Emi, no estoy seguro de que ella quisiera mencionarlo. Creo que solo la he escuchado hablar de él una vez."

"Todo lo que recuerdo es que la mamá de Emi me dijo que él ya no estaba."

hi "¿Oh? ¿Tu mamá prefiere la soledad?"

show emicas happy_up_close
with charachange

"Emi se ríe, ya sea por el alivio de que no le preguntara por su padre o porque de verdad le parece gracioso lo que dije."

emi "¡Para nada! Es por ella que soy una persona tan animada, sabes."

show emicas closedsmile_close
with charachange

emi "Simplemente prefiere ser una invitada a una anfitriona; es menos estresante de esa manera, o eso dice ella."

hi "Evidentemente nunca ha tenido que reunirse con la madre de su novia para la cena."

"Emi suelta una risita y habla con un tono provocador."

show emicas wink_close
with charachange

emi "¿Nervioso, Hisao?"

show emicas smile_close
with charachange

emi "¡No deberías, sabes! ¡No es la gran cosa! ¡Es solo una cena en mi casa, eso es todo!"

hi "Sí, ¿pero alguna vez trajiste un novio a tu casa antes?"

"Confieso que parte de mí anhela escuchar la respuesta a esto."

"Conozco muy poco de las relaciones pasadas de Emi, ni siquiera sé si hubo relaciones pasadas."

show emicas awayfrown_close
with charachange

emi "No, supongo que no."

show emicas frown_close
with charachange

emi "Oye, tal vez esto sí sea la gran cosa después de todo…"

hi "Oh, genial, ahora me siento el doble de nervioso."

"Aunque para ser sincero, estoy muy feliz de escuchar que soy el primero."

"Tal vez tengamos algo especial después de todo."

stop ambient
stop music fadeout 10.0

scene bg emi_houseext
with locationchange

play sound sfx_hammer

"Envalentonado por este pensamiento, me las he arreglado para tranquilizarme considerablemente para el momento en que Emi toca en la puerta principal."

show emicas grin_up at center
with charaenter

emi "¡Hola, mamá, abre! ¡Estamos aquí!"

show bg emi_houseext at bgleft
show emicas grin_up at twoleft
with charamove

show meiko smile at tworight
with charaenter

"La puerta se abre, y aparece la Sra. Ibarazaki sonriéndole a su hija. La sonrisa sigue siendo sorprendentemente similar a la de Emi."

"Nunca me acostumbraré a eso."

show meiko wink
with charachange

emm "Sabes, la gente normalmente espera unos minutos antes de empezar a gritar a la puerta."

show emicas pout_up
with charachange

emi "Y la mayoría de las madres dicen hola a sus hijas en vez de empezar a regañarlas inmediatamente."

show meiko happy
with charachange

emm "Ah, claro. Bienvenida a casa, cariño. Te he extrañado."

play music music_another fadein 0.5

scene bg emi_kitchen
with locationchange

"Un cariñoso abrazo después estamos adentro, y no es hasta entonces cuando la mamá de Emi parece recordar que estoy aquí."

show meiko smile at center
with charaenter

emm "Y hola a ti también, Hisao. ¿Cómo estás?"

hi "Bastante bien, gracias. Es bueno no tener que preocuparse por la escuela por un rato."

show meiko happy
with charachange

emm "Ah, sí, ya terminaron los exámenes, ¿cierto? Debe de ser un gran alivio para ustedes dos."

hi "Sin duda me quita un peso de encima, eso es seguro."

show bg emi_kitchen at bgright
show meiko happy at tworight
with charamove

show emicas happy at twoleft
with charaenter

emi "¡A mí también! Creo que anoche dormí bien por primera vez en semanas solo del alivio."

"Si estas noticias fueron una sorpresa para la madre de Emi, ella no lo demuestra. Aun así, su respuesta deja escapar una nota de interés."

show meiko smile
with charachange

emm "¿Es cierto eso? Me alegra mucho escucharlo, Emi. Sabes que me preocupo cuando tú te pones tan nerviosa por… bueno, los exámenes."

"Sin duda la madre de Emi sabe algo que yo no, o más bien, no sabe que Emi me contó sobre las pesadillas."

"Es interesante, poder observar cómo la Sra. Ibarazaki cubre a Emi. Ese instinto protector que se asegura de que yo no sepa más de lo que Emi está dispuesta a decirme."


label es_E26e:

"Supongo que Emi tiene más cosas en común con los quarks de lo que jamás imaginé."

"Se mueve con rapidez, imposible de entender si se observa directamente, y aun así tiene un efecto en todo el que se encuentra con ella."


label es_E26f:

"¿Me pregunto si la Sra. Ibarazaki averiguará que sé lo de las pesadillas, o simplemente está manteniendo todo en secreto para todo el mundo?"

show emicas weaksmile
with charachange

emi "Sí, este año no ha sido tan malo como en el pasado; Hisao me ayudó a mantenerme concentrada."

"Vamos, sé que eso no es verdad. ¡Ella incluso cortó nuestro contacto fuera de las horas de escuela durante la semana de exámenes!"

"Pero… ella me veía durante el día. Y me contó más de una vez que las carreras matutinas eran lo único que esperaba con ansias durante los exámenes, así que tal vez no sea una completa mentira."

"De cualquier manera, escuchar que haber estado ahí ayudó aunque sea un poco hace que me sienta un poquito mejor."

"La madre de Emi alza una ceja ante esto. O no le cree a Emi, o está tan sorprendida como yo."

show meiko happy
with charachange

emm "Bueno, entonces parece que es algo bueno que ustedes dos se hayan vuelto tan íntimos."

show meiko smile
with charachange

emm "Te diría que cuidaras bien de mi hija, Hisao, pero parece que ya estás haciendo eso."

show emicas closedsmile
with charachange

"Emi sonríe por esto y parece enorgullecerse de que yo me las haya arreglado para congraciarme con su madre tan fácilmente."

hi "En realidad, diría que su hija es la que ha cuidado de mí. Ella me ha puesto a funcionar."

hi "Probablemente he estado más activo que nunca desde que la conocí, incluso antes…"

"En realidad nunca había pensado mucho en eso, tampoco había apreciado el humor que encerraba."

"Yo no era muy activo antes del ataque cardiaco. Los juegos casuales de futbol no cuentan ya que no eran muy comunes."

"Y ya que sé con certeza que tengo un corazón débil, {b}ahora{/b} corro todos los días, tentando mi suerte con la ayuda de mi medicina."

"Me río entre dientes, y luego me doy cuenta de que nunca terminé mi oración."

hi "Bueno, antes de que tuviera mi ataque cardiaco y terminara en esta escuela."

"Lo digo tan casualmente. Hubo un tiempo en el que debía pensarlo dos veces para hablar sobre lo que estaba mal conmigo."

"¿Pero ahora? Ahora parece tonto preocuparse, especialmente en compañía de Emi y de su madre."

"Si Emi puede ser desdeñosa con su discapacidad, entonces yo también."

"Rememoro la competencia de atletismo, cuando Emi se autoproclamó la más rápida sin piernas."

"La realidad de su evidente pérdida nunca ha parecido molestarla, al menos no en público."

"Estar atrapada en la silla de ruedas la frustraba, lo sé. Pero incluso eso fue algo que manejó por sí misma, a pesar de mis esfuerzos de lo contrario."

show meiko happy
with charachange

emm "Emi tiene una manera de sacar el lado más activo de las personas. Nunca entendí del todo cómo lo hace."

"Esos ojos de cachorrito que hace, para empezar."

show meiko smile
with charachange

emm "No me sorprende que se las arreglara para meterte en una rutina de ejercicio."

emm "Si Rin no fuera tan testaruda como ella, estoy segura de que Emi también la habría sacado a correr contigo."

show emicas happy
with charachange

emi "¡Oh, eso me recuerda! Rin manda saludos."

scene bg emi_dining
with locationchange

"Floto a la deriva hasta los bordes de la conversación mientras nos movemos hacia el comedor para cenar."

"Huele delicioso aquí, y la magnitud de lo que la mamá de Emi ha producido es impresionante."

show meiko smile at tworight
show emicas happy_up at twoleft
with charaenter

emi "¡Guau, has hecho suficiente comida para alimentar a un ejército!"

show meiko happy
with charachange

emm "¿Es demasiado? Bueno, puedes llevarte algunas sobras cuando te vayas."

hi "¡Suena genial! Hay un límite en cuánta comida de cafetería puedo soportar. Algo hecho en casa sería un cambio bienvenido."

show emicas smile
with charachange

emi "Lo que él dijo. Gracias, mamá."

"La comida sabe tan bien como huele, y hay una pausa en la conversación mientras todos comemos."

"Emi asalta su plato con el entusiasmo usual, y debo admitir que yo también lo estoy haciendo a un ritmo considerablemente rápido."

show meiko wink
with charachange

emm "Así que, Hisao, he escuchado que tú y mi hija se han vuelto bastante íntimos, ¿eh?"

"La urgencia de decir algo como “No realmente” es tan fuerte que abro mi boca para decirlo, pero luego recupero el control."

"Somos íntimos, eso no se puede negar. Quiero decir, Emi me trajo aquí, ¿no?"

"Afortunadamente, tanto Emi como su madre parecen ver mi reacción como una señal de que me tomaron por sorpresa en vez de que iba a decir algo cruel."

hi "Jeje, supongo que sí. Yo culpo a las carreras matutinas."

show emicas pout_up
with charachange

emi "Haces que suene como algo malo, Hisao."

show meiko smile
with charachange

emm "Bueno, personalmente me siento aliviada."

hi "¿Y eso por qué?"

show meiko worry
with charachange

emm "Emi siempre ha sido una chica popular, pero nunca hizo amigos íntimos."

"Esto es una noticia para mí. Siempre he visto a Emi charlando con sus compañeros en los pasillos."

"Y sin duda todo el equipo de atletismo parece adorarla, pero es cierto que ella elige aislarse durante los almuerzos con Rin y conmigo."

"No es exactamente el tipo de actitud que esperas de una chica popular, después de todo. Por otra parte, he experimentado su renuencia a acercarse a los demás en carne propia, así que no puedo decir que esté sorprendido."

show meiko serious
with charachange

emm "Empezaba a tener mis dudas."

show emicas awayfrown_up
with charachange

"Emi gira los ojos al techo y refunfuña algo que no consigo entender."

stop music fadeout 1.0

hi "¿Huh?"

show emicas neutral_up
with charachange

emi "¿Qué?"

hi "¿Qué es eso que acabas de decir?"

show emicas blush
with charachange

emi "Nada."

show meiko happy
with charachange

"La Sra. Ibarazaki se atraganta con su bebida por la risa."

play music music_comedy fadein 0.5

emm "Has estado saliendo con el enfermero por demasiado tiempo, Emi."

emm "Tendré que hablar con él respecto a corromper a mi hija."

hi "Por algún motivo creo que eso no sería muy efectivo."

show emicas evil
with charachange

emi "De todas formas aprendí casi todo de ti. No del enfermero."

show meiko smile
with charachange

emm "No la escuches, Hisao. Es mentirosa de nacimiento."

show emicas awayfrown
with charachange

emi "Mph. Sí, claro."

hi "Oh, no sé, Emi. Creo que tu madre tiene razón."

show emicas angry_up
with charachange

emi "¿Qué? ¡Traidor! ¡Se supone que estés de mi parte en esto!"

hi "Sí, pero mentiste sobre tu pierna luego de la compe—{w=0.3}{nw}"

with vpunch

extend " ¡au!"

"Una patada en la espinilla dada por un inconfundible pie de plástico me interrumpe, pero no antes de que la Sra. Ibarazaki alce una ceja."

show meiko serious
with charachange

emm "¿Qué pasa con tu pierna?"

show emicas awayfrown
with charachange

emi "No fue gran cosa, es todo… Solo estuve, eh, ensilladeruedasporuntiempo."

"Las últimas palabras balbuceadas son descifradas rápidamente por la madre de Emi —sospecho que tiene experiencia con este tipo de cosas— y un ceño de preocupación aparece en su rostro."

show meiko worry
with charachange

emm "Así que por eso él seguía evitando mis llamadas…"

emm "Oh, Emi… Sé cuánto detestas estar en silla de ruedas."

emm "¡No me extraña que hayas estado de tan mal humor últimamente!"

show emicas frown
with charachange

hi "Sí, ella es mucho más feliz de pie, por así decirlo."

show meiko serious
show emicas awayfrown
with charachange

emm "¡Bueno, por supuesto! Pasó suficiente tiempo en silla de ruedas justo después del accidente."

show emicas frown
with charachange

hi "¿No le pusieron prótesis de inmediato?"

show meiko worry
show emicas awayfrown
with charachange

emm "No, ella debía terminar de sanarse antes de que la dejaran empezar la terapia por la que tienes que pasar para ajustar esas cosas."

emm "Especialmente porque ella quería correr con ellas."

show emicas frown
with charachange

hi "No tenía ni idea."

show emicas weaksmile_up
with charachange

emi "Sí, apestó. Oh, ¿viste el mural de Rin en el festival?"

"La repentina interrupción de Emi provoca que note muy tarde que ella ha estado nerviosa todo este rato, mientras su madre y yo hablábamos."

"Debería de haberme dado cuenta por su nerviosismo cuando se trata de hablar del accidente. Incluso cerca de su madre."

show meiko serious
with charachange

emm "No, no pude llegar al festival, ¿recuerdas?"

show meiko happy
with charachange

emm "Aunque logré echarle una ojeada durante tu competencia de atletismo. Me pareció bastante extraño."

show emicas closedsmile
with charachange

emi "Creo que es más o menos lo que ella quería. Habló mucho acerca de hacerlo como un sueño. O de intentar hacerlo como un sueño."

show meiko smile
with charachange

emm "El arte de Rin es una de esas cosas que no creo llegar a comprender nunca."

show emicas wink
with charachange

emi "No me sorprende. No creo que Rin espere ser comprendida."

show emicas grin
with charachange

emi "Ella me dijo una vez que el arte le permite a la gente entender cosas que no entendería de otra manera, pero al mismo tiempo ella no cree que realmente funcione de esa manera."

"Estoy sorprendido de que Emi haya hablado de esto con Rin tan exhaustivamente como para incluso tener la opinión de esta última, considerando cómo es."

"Aunque no esperaría que Rin pudiera decir, si estuviera dispuesta, lo mismo sobre la opinión de Emi."

"A menos, por supuesto, de que Emi esté manteniéndome todo oculto a propósito; lo cual es probable, pero desagradable de pensar."

"Me dejo llevar por esta desagradable línea de pensamientos por un rato, perdiendo la noción de la conversación."

show meiko serious
with charachange

emm "Oye, Emi, quería preguntarte…"

show emicas neutral
with charachange

emi "¿Huh?"

show meiko worry
with charachange

emm "¿Visitarás a tu padre este año?"

stop music fadeout 3.0


"Por la forma en la que lo dice, pensarías que la madre de Emi hablaba sobre el clima. Por la forma en que Emi reacciona, claramente no es del clima de lo que están hablando."

show emicas awayfrown
with charachange

"Ella se estremece, un leve tirón de la cabeza hacia atrás como si acabara de ser abofeteada."

show emicas sad
with charachange

emi "¿Podemos hablar de esto luego?"

"Su voz suena frágil, tensa. Parece como si la pregunta la hubiera conmocionado severamente."

"Parece que la Sra. Ibarazaki no calculó bien qué tan íntimos somos Emi y yo."

"Algunas cosas, al parecer, es mejor no conversarlas cuando yo estoy cerca. Su padre es una de esas cosas."

"El accidente que se llevó sus piernas probablemente es otra de esas cosas, si su reacción a la conversación entre su madre y yo es un indicio."

"A la madre de Emi no le toma mucho tiempo darse cuenta de que metió la pata."

show meiko happy
with charachange

emm "Claro que sí, cariño. Perdón por sacar el tema, solo quería preguntar para poder hacer planes—"

show emicas neutral
with charachange

emi "Está bien. No te preocupes."

"Emi se revuelve nerviosa, como si se avergonzara de su propia reacción. Confieso que su reacción es desconcertante."

"¡Si ella mencionó a su padre hoy mismo, más temprano! ¡Incluso hace unas pocas horas atrás!"

"¿Por qué la simple pregunta de cuándo visitará a su padre podría causar una reacción tan fuerte?"

"A menos de que cualquier serenidad que ella diga haber alcanzado gracias a nuestra conversación de anoche se haya evaporado repentinamente."

"O no ayudó tanto como ella pensó. O dijo."

show emicas weaksmile
with charachange

emi "Yo eh, regreso en un minuto. Debo ir al baño."

hide emicas
with charaexit

show bg emi_dining at bgleft
show meiko smile at center
with dissolvecharamove

"Emi se levanta y deja la mesa repentinamente, dejándonos a la Sra. Ibarazaki y a mí solos."

"Estoy algo confundido. ¿Debería seguirla, o debería quedarme aquí?"

"Es obvio que la partida de Emi no fue por el llamado de la naturaleza. Algo la está molestando, y tengo que saber qué es."



label es_choiceE26:
menu:
    with menueffect
    "¿Qué debería hacer?"
    "Seguirla.":


        return m1
    "Hablar con su madre.":

        return m2

label es_E26c:



"La única forma de averiguarlo es ir directamente a la fuente. Y la fuente está pretendiendo que tiene que usar el inodoro en estos momentos."

scene bg emi_kitchen
with locationchange

"Me excuso cortésmente de la mesa y me dirijo hacia allá, solo para ver a Emi no en el baño, sino en la cocina, junto a la sala de estar."

show emicas sad
with charaenter

"Emi dejó la puerta abierta, y cuando me acerco puedo ver que está agarrándose de la mesa en un intento de recobrar la compostura, un esfuerzo que falla tan pronto abro la boca."

hi "No parece que el llamado de la naturaleza fuera tan urgente."

show emicas angry
with charachange

"Emi salta y me lanza una mirada."

show emicas angry_up
with charachange

emi "¿Qué haces aquí? No vine aquí para estar con otra gente."

hi "Solo quería ayudarte. Te veías bastante agitada."

show emicas awayfrown
with charachange

emi "Dije que no pasaba nada, ¿no es verdad? Además, pensé que habíamos acordado que no podías ayudarme."

hi "No, acordamos que eres testaruda."

show emicas angry
with charachange

emi "Mira quién habla. El chico que me siguió."

hi "¡Es diferente! Quiero ayudarte con… lo que sea."

show emicas awayfrown
with charachange

emi "Qué chistoso, porque {b}yo{/b} solo quiero que me dejes sola."

hi "¿Pero por qué? ¿Por qué no puedes confiar en mí?"

show emicas frown
with charachange

emi "Ya hablamos de esto, Hisao. Tengo que lidiar con estas cosas yo sola."

hi "¡No aceptaré eso! ¡Necesitas mi ayuda, simplemente no la aceptas!"

"Mi elección de palabras parece haber fallado un poco."

show emicas angry
with charachange

emi "¿Necesito? ¿Yo {b}necesito{/b} tu ayuda?"

play music music_tragic fadein 0.5

show emicas angry_up
with charachange

emi "Bueno, qué bien que nos hayamos conocido, ¿no? Porque supongo que de otra manera yo simplemente sería un ser humano defectuoso, ¿no es verdad?"

emi "No, es una completa bendición que Hisao llegara a salvar el día, ¿no? Porque Dios sabe que no puedo ayudarme a mí misma, ¿cierto?"

emi "Solo soy la pobre chica sin piernas y con problemas emocionales, ¿cierto?"

hi "Emi, sabes que no creo eso—"

show emicas angry
with charachange

emi "¿En serio? Porque si pensaras otra cosa no creo que estuvieras aquí, diciendo que necesito tu ayuda."

emi "He llegado bastante lejos en la vida como un ser humano normal sin ti."

hi "Entonces qué, ¿nada de lo que hicimos fue importante? ¿Solo soy el chico que sale contigo?"

show emicas awayfrown
with charachange

emi "Eres mi novio, Hisao, no mi salvador."

hi "Pues no, eso es obvio. Ni siquiera considerarías que puedo ser de ayuda para ti, ¿verdad?"

hi "Solo vas a acumular todo dentro y esperarás a que una carrera resuelva tus problemas, o vendrás a visitarme y perderemos el tiempo hasta que te sientas mejor."

hi "Eso no es ser un ser humano saludable, Emi. Eso no es lo que una relación significa."

show emicas frown
with charachange

emi "Bueno, es lo que significa para mí en estos momentos, Hisao."

show emicas sad
with charachange

emi "Desearía—"

"Pero entonces ella parece reconsiderar sus palabras. Un atisbo de dolor, de duda en su rostro. Por un momento creo que está a punto de llorar."

show emicas frown
with charachange

"Pero ese momento pasa, y ahora ha recobrado su compostura de nuevo. Fuera lo que fuera, ese deseo permanecerá en silencio."

emi "Mira, es solo que… no puedo hacer esto ahora."

hi "Qué, ¿tener una conversación seria? ¿Ser abierta? ¿Ser honesta? ¿Preocuparte por alguien más aparte de ti misma y tus problemas?"

show emicas angry_up
with charachange

emi "¿Qué sabes de mis problemas? ¡Nada! No sabes por lo que he pasado, así que no pretendas que sí."

hi "Sé que tienes pesadillas, sé que tu padre ya no está. ¿Qué le ocurrió?"

show emicas sad_up
with charachange

"La cabeza de Emi se mueve hacia atrás como si acabara de abofetearla. Ese tono frágil ha regresado a su voz."

show emicas sad
with charachange

emi "Suficiente."

"Esto es estúpido. Toda esta conversación solo ha sido Emi evadiéndome de distintas maneras."

hi "Qué, ¿ni siquiera responderás esa pregunta? Bien, guárdate tus secretos. En lo que a mí respecta puedes enterrarlos en una tumba."

show emicas blush
with charachange

"Emi abre más los ojos, conmocionada. Cuando habla de nuevo, es con una voz grave, peligrosa."

show emicas grit
with charachange

emi "Sal de mi casa, Hisao."

"El súbito cambio de tono en su voz me saca instantáneamente de mi enojo autojustificado y provoca que me de cuenta, con creciente horror, de lo que acabo de decir."

hi "Emi, no quise—"

stop music fadeout 2.0

show emicas angry
with charachange

emi "Dije que te {b}vayas{/b}, Hisao."

emi "Dile a mi madre que cocinó una maravillosa cena pero que olvidaste un compromiso importante, y sal de mi casa."

"Ella está estremeciéndose ahora, temblando con ira, o con tristeza, o con determinación. Su voz aún es grave, controlada. Casi como un gruñido."

"Alzo una mano para colocarla en su hombro, para disculparme por ir demasiado lejos, pero ella se aleja de mi contacto."

show emicas angry_up
with charachange

emi "Vete."

show bg emi_dining at bgleft
show meiko serious at center
with locationchange

"¿Qué puedo hacer? Camino fuera de la cocina y voy a la sala de estar, le doy mis disculpas a la Sra. Ibarazaki, y me acompaño a mí mismo hasta la salida."

$ suppress_window_after_timeskip = True

scene black
with dissolve





label es_E26d:

"Hay un silencio incómodo en la mesa por un rato luego de que Emi se va apresuradamente. No se me ocurre nada que decir."

show meiko serious
with charachange

"La madre de Emi suspira, rompiendo el silencio."

play music music_moonlight fadein 5.0

emm "Me disculpo por eso, Hisao. A veces olvido que Emi es delicada con ciertos temas."

emm "Y también estaba hablando del asunto de la silla de ruedas…"

hi "¿Debería seguirla?"

show meiko worry
with charachange

emm "¡Cielos, no! No dejó la mesa para continuar con la conversación, sabes."

hi "Pero si está alterada, ¿no debería ayudarla alguien?"

show meiko serious
with charachange

emm "Si fuera alguien más, diría que sí. Pero mi hija es testaruda como una mula, y si quiere estar sola es mejor dejarla sola."

emm "De otra forma ella podría decir algo de lo que se arrepentiría, lo que provocaría que tú digas algo de lo que te arrepentirías, y preferiría que la cena no termine contigo o con ustedes dos saliendo de la casa como un huracán."

show meiko happy
with charachange

emm "Si eso llegara a pasar, entonces yo sería una pésima anfitriona, ¿no crees? Ya hoy me comporté como idiota una vez."

hi "No pasa nada, yo no debería haber dicho lo de la silla de ruedas, aparentemente."

show meiko serious
with charachange

"La Sra. Ibarazaki frunce el ceño, claramente más preocupada por la omisión de Emi de lo que aparentaba."

emm "Desearía que no hiciera eso. Solo hace que me preocupe más, sabes."

hi "¿Hace esto con regularidad?"

show meiko smile
with charachange

emm "¿Qué, huir al baño? No, supongo que no. ¿Lo de ocultarle heridas a su madre? Bueno, eso es más común."

emm "Cada vez que la atrapo mintiendo de esa forma, ella me asegura que la única razón por la que no me lo dijo es porque no era gran cosa."

hi "Si sirve de consuelo, estoy seguro de que la única razón por la que yo lo sabía es porque la veía todos los días."

show meiko happy
with charachange

"Esto provoca una risita seca del otro lado de la mesa. La Sra. Ibarazaki suspira, con algo de tristeza."

show meiko smile
with charachange

emm "Aún indecisa de acercarse a la gente, ¿eh? Aún tengo esperanzas de que superará eso."

emm "Es gracioso, la verdad. Ella se recuperó tan bien del accidente de tantas maneras…"

show meiko serious
with charachange

emm "Supongo que algunas cosas nunca desaparecen por completo."

"Por lo que parece, todo este asunto también sigue preocupándole."

"Aunque ella parece algo más dispuesta a hablar del accidente sin Emi cerca."

hi "Eh, tengo una pregunta, si no hay problema."

show meiko smile
with charachange

emm "¿Oh?"

hi "¿Qué otra cosa perdió Emi en ese accidente? El enfermero dijo que ella se pone así cerca del aniversario, y ella no me lo va a decir…"

show meiko happy
with charachange

emm "Y pensaste que yo te lo aclararía todo, ¿hmm?"

hi "Eh, sí. Con suerte."

show meiko serious
with charachange

emm "Bueno, hay un problema con esa petición, sabes."

hi "Déjame adivinar: ¿le prometiste a Emi que no le dirías nada a nadie que ella no quisiera que supiera, y tú no sabes si ella quiere que yo sepa."

emm "Algo así. Le prometí a Emi que sería ella quien le contaría a la gente la historia completa."

hi "¿Pero no es eso importante? Quiero decir, claramente ha tenido un gran impacto en ella si sigue actuando así tanto tiempo después del accidente."

show meiko worry
with charachange

emm "Eso es verdad. Sí tuvo un efecto a largo plazo en ella. Hay unas cuantas cosas que posiblemente nunca superará."

"Por un momento la Sra. Ibarazaki se ve muy entristecida, como si una vieja herida estuviera molestándola."

emm "Supongo que hay algunas cosas que yo tampoco podré superar…"

show meiko happy
with charachange

"Otra risita seca, y con una sacudida de la cabeza la madre de Emi destierra esas memorias."

show meiko smile
with charachange

emm "Mira, hay algo que es imprescindible que entiendas sobre la forma en que Emi piensa respecto al accidente."

hi "¿Qué?"

emm "No fue gran cosa."

stop music fadeout 1.0

"De algún modo me las arreglo para evitar que mi mandíbula caiga al suelo por la sorpresa, pero requiere algo de esfuerzo."

"Tiene que ser la cosa más ridícula que he escuchado."

hi "¿Perdona?"

play music music_sadness fadein 3.0

show meiko serious
with charachange

emm "Bien, tal vez no sea así de sencillo, pero es un resumen bastante preciso. Emi cree que el accidente no la definió, y que todo lo que perdió ese día tampoco la definió."

emm "Ella no es “esa chica que perdió sus piernas”, ella es “La Más Rápida sin Piernas”. Su optimismo y energía salieron ilesos de esa colisión, en lo que a ella respecta."

hi "Pero aun así va más allá de eso, ¿no es verdad? Quiero decir, anoche me dijo que se negaba a depender de mí porque eso haría que perderme resulte demasiado doloroso."

show meiko smile
with charachange

emm "No realmente. Dijiste que ella no te va a decir nada del accidente, aunque ya antes le habías preguntado sobre eso."

emm "La razón por la que ella no habla de eso cuando le preguntas es porque para ella no es algo que realmente debas saber. Aun si no estuviera aterrorizada de acercarse a los demás, seguiría sin hablar de eso."

hi "¿Ella teme acercarse a mí?"

show meiko happy
with charachange

emm "Oh, cielos, sí. Gracias a lo de haber salido viva del accidente, ella ha adquirido el desagradable conocimiento de lo rápido que todo puede acabar."

show meiko smile
with charachange

emm "Así que no dejará que las personas se acerquen mucho a ella, e indudablemente resentiría cualquier implicación de que no puede manejar esto sola."

hi "Pero no creo que {b}pueda{/b}."

show meiko serious
with charachange

emm "¿Ah, no? ¿Estás seguro de haber estado saliendo con mi hija y no con alguien más? Créeme, Hisao, ella puede manejarlo sola."

hi "Pero ella tiene pesadillas, y no puede dormir bien, y—"

show meiko smile
with charachange

emm "Y ella hace esto todos los años. Dime, si ella no fuera capaz de superarlo por sí sola, ¿realmente crees que seguiría viva? Se habría suicidado, o algo igual de melodramático."

hi "Entonces, qué, ¿no debería intentar ayudarle?"

show meiko serious
with charachange

emm "¡No dije eso! Detesto ver a mi hija así, y saber que ella puede confiar en alguien más me ayudaría a relajarme."

emm "Sencillamente debes entender que aceptar ayuda va en contra de la forma en que Emi piensa sobre sí misma y en la forma en que cree que el mundo funciona."

emm "Si aún quieres ofrecerle ayuda, supongo que es tu elección. Honestamente, me gustaría que lo hicieras, pero sería tonto no advertirte que no va a ser fácil."

show meiko smile
with charachange

emm "Solo debes ser paciente con ella. Ya eres más cercano a ella que cualquier otra persona que haya conocido en Yamaku."

hi "Bueno, la verdad no se siente como si fuéramos muy cercanos."

show bg emi_dining at center
show meiko serious at tworight
with dissolvecharamove

show emicas evil at twoleft
with charaenter

stop music fadeout 0.3

emi "Bien, eso hace que esta parte sea más fácil."

"La voz de Emi casi me provoca un infarto."

hi "¡Guau! No te escuché volver, Emi."

show emicas angry
with charachange

emi "Qué conveniente."

hi "Espera, ¿escuchabas a escondidas?"

show emicas angry_up
with charachange

emi "Nop. De casualidad regresé en el momento oportuno, supongo."

show meiko worry
with charachange

emm "Emi, Hisao solo estaba—"

"Emi alza un dedo, interrumpiendo a su madre."

show emicas grit
with charachange

emi "¿A punto de salir de la casa? Sí, lo sé."

"Ahora Emi está temblando de ira, viéndose vagamente traicionada."

emm "Emi, no seas ridícula, solo estábamos—"

show emicas angry_up
with charachange

emi "¡Lo {b}prometiste{/b}!"

play music music_rain fadein 0.5

"El dolor impreso en esas últimas palabras es casi demasiado para mí. La idea de que puedo lastimarla tanto es como una patada en la entrepierna."

"La madre de Emi se ve igual de dolida por el pensamiento."

emm "¡Y mantuve esa promesa! Solo escucha, no hay razón para que andes sacando gente de la casa."

"La madre de Emi parece tanto enojada por el arrebato de su hija como avergonzada de que yo esté viéndolo todo."

"Solo hay una verdadera solución para este problema, creo."

hi "Está bien. Me iré."

emm "Vamos, vamos, eso parece algo innecesario…"


hi "No se preocupe por eso. Gracias por la cena, Sra. Ibarazaki, y por el consejo."

show meiko serious
with charachange

emm "Fue un placer, Hisao. Lamento que no llegáramos hasta el postre."

hi "No pasa nada. De igual forma tengo que vigilar lo que como."

hi "Buenas noches, Emi, Sra. Ibarazaki."

"La formalidad de nuestra conversación, sumada al hecho de que estoy alistándome para irme, parece sacar a Emi de su enojo."

show emicas frown
with charachange

emi "No, espera. Lo siento, he estado tan… y luego de anoche pensé… No tienes que irte, retiro lo dicho, no pasa nada—"

"No puedo evitar sonreír ligeramente. Apenas puede articular su disculpa, y realmente me gustaría quedarme…"

"Pero no creo que pueda, no en este momento. Necesito pensar en lo que su madre dijo, y en lo que voy a hacer respecto a nosotros."

"Tampoco quiero arriesgarme a enojar accidentalmente a Emi de nuevo, con su estado actual."

hi "No, será mejor que me vaya. Te ves bastante conmocionada, y, bueno, solo terminaría intentando ayudarte de nuevo. Sé que preferirías que no lo hiciera, así que en vez de eso me iré."

show emicas sad
with charachange

emi "Pero—"

hi "Oye, no es ningún problema. No quieres un caballero en su blanco corcel, ¿cierto? Solo prométeme una cosa, ¿de acuerdo?"

show emicas frown
with charachange

emi "¿Qué?"

hi "No te enojes con tu mamá, ¿de acuerdo? Solo me estaba dando unos consejos, eso es todo."

show emicas sad
with charachange

"Emi asiente, vacilante, como si esta simple idea fuera su único apoyo en este momento. Está terriblemente desequilibrada, pero ahora mismo no puedo hacer nada al respecto."

emi "Bien."

hi "Te veo mañana, ¿está bien? Carrera por la mañana. ¡No lo olvides!"

"Puedo ver que lastimé a Emi cuando decidí irme. Pero no hay nada que pueda hacer por ella tal y como están las cosas, y sé que es demasiado terca como para admitir que me quiere aquí."

"Veo varias emociones cruzar el rostro de Emi mientras intenta procesar todo lo que acaba de suceder."

show emicas weaksmile
with charachange

"Poco después aparece esa mirada tranquila de nuevo, como anoche, y esa voz que se esfuerza tanto por sonar despreocupada."

emi "Claro, Hisao. Te veo luego."

"Ninguno de los dos está dispuesto a admitir emoción alguna en este momento, y me está costando mucho mantener mi fachada, así que me doy vuelta y salgo por la puerta."

stop music fadeout 7.0

scene bg emi_houseext
with locationskip

"La cierro lentamente detrás de mí, deteniéndome por un momento mientras se cierra por completo, con mi mano sobre la perilla."

"¿Tomé la decisión correcta hace unos instantes? ¿Debería haberme quedado para intentar resolver las cosas?"

"No, decido. No así, frente a su madre. A pesar de todo, preferiría mantener a la madre de Emi aislada de todo ese enfado que surgió anoche."

"Aunque ella probablemente ya esté acostumbrada, un instinto protector quiere que yo mantenga intacta la imagen de Emi como una chica alegre."

"Con un sobresalto, me doy cuenta de que mi mano aún reposa sobre la perilla. La aparto de ahí, la meto en mi bolsillo, y camino por la calle que se oscurece lentamente."

scene bg school_dormhisao
with shorttimeskip

play music music_pearly fadein 1.0

"Dejo escapar un largo suspiro."

"La espera hasta mañana por la mañana no será fácil."

"En todo caso, debo pensar en lo que le diré a Emi. Debo disculparme, y debo hacerme entender de algún modo."

"Por ese motivo, he estado pensando en algo durante la mayor parte del camino de regreso a mi habitación."

"La carta de disculpa de Iwanako."

"Estaba tan preocupado por mi nueva vida cuando la recibí que ni siquiera me preocupé en leerla por completo."

"Ahora que estoy en una posición similar, mi curiosidad se ha reavivado. ¿Qué quería decirme con tantas ganas?"

"Cuanto menos, leer sus pensamientos podría ayudarme a organizar los míos."

"Recuerdo haberla tirado lejos. Diablos, ¿adónde arrojé esa cosa?"

"Reviso debajo de mi escritorio. No me sirve de nada, así que busco en lugares más difíciles de alcanzar."

"…"

"Bueno, al menos ahora sé adónde fue ese calcetín perdido."

"Aunque todavía ninguna carta."

"Es cuando intento barrer con mi mano debajo de la mesita de noche que siento algo arrugado, prensado entre la mesita y la pared."

"Gruñendo un poco por el esfuerzo, alcanzo mi objetivo y me las arreglo para rápidamente arrastrarla hasta la luz."

"Bingo."

play sound sfx_paper

scene ev hisao_letter_open_2
with locationchange

"Me siento frente a mi escritorio y desenvuelvo el arrugado papel. Un chasquido enciende la lámpara de mesa."

"Saltándome los cumplidos vacíos, busco el punto donde dejé de leer. Ah, aquí está."

window hide

$ written_note("Hay otras cosas que quiero decir. Te estoy escribiendo porque sentí que hay cosas que debería haber dicho después del incidente en aquel invierno. Realmente me arrepiento de no haber sido capaz de decirlas en persona, y no tengo excusa para ello.\n\n\n\n\n")

$ written_note("La verdad es, las veces que te visité en el hospital hicieron que me preocupara por ti. No estoy hablando de tu salud. Parecías haberte distanciado y desanimado más. Era natural después de que ocurriera algo como eso, estoy segura, pero de alguna manera tuve la sensación de que habías renunciado a algo en ese entonces. ¿La felicidad, tal vez?\n")

window show

"Renunciar a la felicidad…"

"Esto suena incómodamente familiar."

window hide

$ written_note("Quería por algún medio expresar mis sentimientos, pero las palabras correctas no venían a mí. No podía decir algo para consolarte. Realmente siento no poder haberte apoyado cuando más lo necesitabas, aunque me gustes tanto. Por lo menos ahora, finalmente, puedo ser más honesta.\n\n\n\n")

$ written_note("Si pudiera volver a aquellos días silenciosos en febrero y marzo, te diría que no renunciaras a ti mismo. Eso es lo que diría. Quizás no te hubieses alejado tanto si tan sólo hubiera dicho algo. Espero que hayas podido recuperarte por tu cuenta.\n\n\n\n")

$ written_note("Ahora que la distancia entre nosotros es también física, se siente también más definitiva, de algún modo. Me pregunto si nos encontraremos de nuevo. ¿Tal vez sea mejor si no? Aun así, si te gustaría mantener correspondencia conmigo, por supuesto que puedes escribirme de vuelta. Me agradaría mucho escuchar sobre tu nueva escuela y cómo te está yendo. Te deseo todo lo mejor.\n\nAtentamente, Iwanako")

window show

"Luego de leer la carta la aliso con cuidado y la pongo a un lado en el escritorio."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\n\nGracias, Iwanako. Quería responder “sí” a tu pregunta en ese nevado día de invierno, pero nunca pude hacerlo."

n "Para cuando nos encontramos de nuevo, era demasiado tarde."

n "O eso pensé. ¿Qué habría pasado si me hubiera comportado de otra manera, en ese lúgubre y estéril cuarto de hospital?"

n "Lo lamento. No tiene sentido preguntárselo ahora, pero tampoco tiene sentido tratar de olvidarlo."

n "Soy quien soy por todo lo que me ha pasado y por todo lo que espero que me pase. Presente, futuro y pasado."

stop music fadeout 2.0

n "\n\nY creo que el pasado acaba de enseñarme una importante lección."

$ renpy.music.set_volume(1.0, 2.0, channel="music")

nvl clear
nvl hide dissolve






label es_E27:

window hide None

scene black
with dissolve

play sound sfx_alarmclock

with Pause(2.0)

scene bg school_dormhisao
with openeye

window show

"Suena el despertador y me doy la vuelta, apagándolo. Mis ojos se abren adormilados para observar el techo."

play music music_night fadein 1.0

window hide
nvl clear
nvl show dissolve

n "\n\n¿Qué voy a hacer? ¿Salgo de la cama, voy a la pista, y pretendo que no ha pasado nada?"

n "¿Emi estará pensando en ir? Después de los eventos de anoche, lo dudo."

n "Aun suponiendo que lo hiciera, ¿qué haría yo entonces? ¿Evitar esta pelea solo para incurrir en la misma rutina la próxima vez que algo la esté molestando?"

n "Sé que anoche hablé apresuradamente, especialmente al tratar de influenciarla usando a su padre."

n "¿Pero de verdad algo de lo que dije estuvo fuera de lugar? Ella no me dejará acercarme, nunca, y tendrá que sufrir sola."

n "Nada de lo que haga, nada de lo que diga va a cambiar eso. Ella no cambiará, y ya ha decidido mantener una distancia prudente de mí."

n "\n¿En serio puedo resignarme a ir allá y verla, sabiendo que nunca voy a pasar de donde estoy en estos momentos?"

nvl clear
nvl hide dissolve

scene black
with shuteye

window show

"No, decido. Realmente no puedo. Hoy no. Me doy la vuelta y sigo durmiendo."

"Probablemente ella no estará allí, de todas formas."

scene bg school_cafeteria
with shorttimeskip

"Una conversación mental similar se repite cuando es hora de ir a almorzar, y como en la cafetería, solo."

"No quiero verla; con solo pensarlo me siento enfermo."

scene bg school_track_ni
with shorttimeskip

"Esa noche, salgo a correr; estoy solo por primera vez desde que Emi se enfermó luego de la competencia de atletismo."

"Me salto la visita al enfermero, en caso de que pregunte por Emi."

"Tampoco quiero hablar de ella."

scene bg school_hallway3
with shorttimeskip

"El día siguiente, hago lo mismo. Apagar la alarma. Quedarme en la cama. Comer solo, correr solo."

"Para aprovechar el tiempo que usualmente pasaría con Emi, empiezo a leer más."

"Funciona sorprendentemente bien, hasta que termino escondiéndome en unos lavabos porque la veo caminando por el pasillo durante el receso."

"Si me vio, no lo demuestra, aunque supongo que ella nunca demuestra nada."

"Ciertamente no a las chicas de su clase que observo hablándole alegremente."

"O a sus queridos compañeros de atletismo."

"Especialmente no a mí."

"Apagar la alarma. Quedarme en la cama."

scene bg school_scienceroom
show muto normal at center
with shorttimeskip

"Mutou y yo tenemos una larga charla sobre la posibilidad de que la teoría de las cuerdas sea plausible. Yo no lo creo, la verdad."

"Más de cuatro dimensiones, lo puedo aceptar. ¿Pero un montón de cuerdas vibrando a un nivel subatómico? Eso es pedir demasiado."

"Y parece que no soy el único que piensa de esta manera. Al parecer ya no es una teoría tan sólida como antes."

"Mutou dice que es solo porque nadie ha encontrado todavía la forma correcta de observar los datos."

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_rooftop

scene bg school_roof
with shorttimeskip

"Comer solo."

"La azotea está desierta hoy. Por un instante me pregunto dónde están Emi y Rin, pero me sacudo la pregunta de encima. Lo importante es que no están aquí, así que no tendré que hablarles."

"Ya que no tengo a nadie con quien hablar, traigo un libro conmigo para leer."

"El clima está mejor, tal vez un poco caliente."

"Espero que esté más fresco por la noche; una serena brisa parece respaldar mi teoría."

stop ambient fadeout 2.0

scene bg school_track_on_ni
with shorttimeskip

"Correr solo."

"Está, de hecho, más fresco en la pista. No hay señal de Emi, la cual es exactamente la razón por la que voy."

"Estiro y empiezo mi carrera habitual, esforzándome en ignorar la ausencia de una compañera frente a mí."

"Encontrándome con mis pensamientos flotando hasta esa risa juvenil, incorregible sonrisa, esos grandes y amistosos ojos, su cuerpo increíblemente tonificado—"

scene bg school_track_running_ni
with Dissolve(1.0)

"Aumento el ritmo para aclarar mi cabeza. Acortando la distancia entre las curvas y yo, encuentro la velocidad que me hace pensar solo en mis piernas y en cuánto arden."

"Miro mi reloj mientras atravieso la última curva, notando que mi tiempo ha mejorado."

show bg school_track_on_ni
with Dissolve(2.0)

"Mi corazón parece estar algo nervioso esta noche, así que me permito unas cuantas vueltas más de enfriamiento solo para estar seguro."

"No hay razón para alertar al enfermero por esto. Estaré bien. Un pensamiento muy similar a los de Emi para mí, lo admito."

"Tengo que tener esperanzas de que eventualmente dejaré de pensar tanto en ella."

scene bg school_dormhisao
with shorttimeskip

"Termino otro libro antes de irme a dormir esa noche. Tendré que pasar por la biblioteca mañana."

play sound sfx_switch

show bg school_dormhisao_ni
with Dissolve(0.2)

with Pause(0.5)

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
stop music fadeout 3.5

scene black
with shuteye

window hide

with Pause(2.0)
play sound sfx_alarmclock
scene bg school_dormhisao
with openeye

window show

"No sé por qué todavía mantengo la alarma tan temprano, pero igual me despierta la siguiente mañana. La apago otra vez y me vuelvo a dormir."

scene bg school_scienceroom
show misha perky_smile at center
with shorttimeskip

play music music_pearly fadein 1.0

"Esa tarde, mientras me preparo para ir a la cafetería para otro solitario almuerzo (tengo un nuevo libro sobre un par de timadores en la antigua Persia que estoy emocionado por leer) soy repentinamente arrinconado por Misha y…"

"Huh. Supongo que solo Misha."

show misha hips_smile
with charachange

mi "¿Vas a comer solo de nuevo, Hicchan~?"

show misha sign_smile
with charachange

mi "¡Nos dimos cuenta, sabes~!"

hi "¿Nos?"

show misha hips_grin
with charachange

mi "¡Ajá! ¡Shicchan y yo notamos que has estado pasando más tiempo solo!"

show misha hips_smile
with charachange

mi "¡Ella quería que yo averiguara por qué, así que le dije que te preguntaría!"

hi "Me sorprende que no me lo preguntara ella."

show misha perky_smile
with charachange

mi "Lo habría hecho, pero quería adelantar un poco unos documentos. ¡Hay muchos de ellos ya que estamos acercándonos al final del trimestre, sabes~!"

hi "De todas formas, ¿por qué el repentino interés en mi bienestar?"

show misha sign_smile
with charachange

mi "Ah, Shicchan dijo “¡Es deber del consejo no perder de vista la salud emocional de sus estudiantes! ¡Permitir que un cons-constitutivo caiga en una espiral de depresión sin revisión alguna sería un fracaso imperdonable en los deberes del consejo!”."

hi "Bueno, eso es fácil, entonces. No estoy deprimido."

show misha perky_confused
with charachange

mi "¡Pero estás comiendo solo, y nadie te ha visto junto a Emi! Algo pasó, ¿verdad, Hicchan~?"

"La voz de Misha adquiere un tono ligeramente más severo, aunque de alguna manera mantiene el familiar canturreo al final de sus oraciones."



label es_choiceE27:
menu:
    with menueffect
    "Aprieto los labios, inseguro de cómo responder."
    "Restarle importancia al problema.":


        return m1
    "Ceder y contarle a Misha.":

        return m2







label es_E27a:
"No estoy seguro de que me agrade la idea de contarle cosas privadas al consejo estudiantil."

hi "Nada grave."

show misha cross_frown
with charachange

mi "Hicchan, ¡mentir es algo terrible~!"

"Ella no se lo cree."

"De acuerdo, le diré algo, pero no mucho."

hi "Tuvimos un desacuerdo y aún no lo hemos resuelto."

show misha perky_confused
with charachange

mi "¿Oh? ¿Por qué no?"

hi "Porque, mira, no necesito hablar de esto, ¿bien?"

hi "No es la gran cosa, ¿de acuerdo? Estoy bien."

show misha perky_sad
with charachange

mi "¿Y Emi? ¿Ella también está bien, Hicchan?"

stop music fadeout 4.0

"La voz de Misha adopta un tono decididamente serio. Esto es ridículo."

hi "No lo sé, ¿de acuerdo? No he preguntado. Las cosas están complicadas ahora mismo."

show misha hips_frown
with charachange

mi "¿Qué clase de hombre eres? ¿Las cosas se ponen un poco difíciles y decides esconderte de ellas?"

play music music_rain fadein 4.0

"La repentina réplica de Misha me toma totalmente desprevenido."

show misha cross_frown
with charachange

mi "¡Shicchan llamaría a eso un acto cobarde, y tendría toda la razón!"

mi "¡Ustedes dos eran cercanos! ¡Eran felices juntos! ¿Y solo vas a tirarte al suelo y morir sin dar pelea?"

mi "¡Deberías estar dispuesto a pelear por tu novia, Hisao!"

"Parece que Misha está canalizando a Shizune en estos momentos. No me sorprendería descubrir que Shizune le dio un guión a seguir basado en mi respuesta."

"Misha señala la puerta del aula con un brazo imperativo."

show misha sign_smile
with charachange

mi "¡Ahora sal del aula y repara las cosas!"

hi "Um, aún tenemos las clases de la tarde…"

"Esto no parece disuadir a Misha."

show misha hips_smile
with charachange

mi "¡Entonces luego de clases! ¡Será mejor que lo hagas, Hicchan! ¡Es importante que no dejes las cosas así!"

hi "¿Por qué?"

show misha cross_frown
with charachange

"Misha me mira como uno miraría los excrementos de un animal."

mi "¿Acaso ella no te importaba, Hisao? Eso es lo importante, ¿no crees?"

"Huh. Ella tiene razón."

"Me importaba… Me importa."

"¿No es verdad?"

hi "De acuerdo. La veré luego de clases."

show misha hips_grin
with charachange

mi "¡Genial~! ¡En ese caso le haré saber a Shicchan que estás bien~!"

"Regresa el canturreo. Supongo que eso significa que Misha ya no está enojada conmigo."

hide misha
with charaexit

"Ella se despide y desaparece por el pasillo, y yo me como mi almuerzo."

scene bg school_scienceroom
with shorttimeskip

"Mientras las clases de la tarde se acercan a su final, me preparo para lo que se aproxima."

"Debo ver a Emi; Misha tenía razón al menos en eso. Dejar nuestro problema sin resolver no sirve."

"Como mínimo, necesito disculparme por lo que dije."

"Considero ir a su habitación para verla, pero probablemente todavía está en la pista."

scene bg school_courtyard
with locationskip

"Las escaleras de la salida del edificio principal y del camino a la pista me hacen sentir como un hombre condenado."

"Tengo la horrible y trepidante sensación en las entrañas de que todo esto va a salir terriblemente mal, que no voy a lograr nada."

"Excepto tal vez incrustar el último clavo en el ataúd de lo que fuera que Emi y yo teníamos."

stop music fadeout 2.0

scene bg school_track
with locationskip

"Ahí está ella, justo como esperaba, dando vueltas por la pista luego de que todos los demás se han ido a bañar o a cenar."

"No la saludo, ni siquiera doy muestras de estar aquí. Solo me siento en las gradas y la veo recorrer la pista."

show emi basic_confused_gym:
    center
    xpos 0.6
    easein 0.5 xpos 0.5
with charaenter

"Le toma unas cuantas vueltas alrededor de la pista notar mi presencia, luego de hacerlo patina hasta detenerse, los ojos muy abiertos por la sorpresa."

show emi basic_annoyed_gym at center
with charachange

show emi basic_grin_gym
with charachange

"La sorpresa es rápidamente enmascarada por enojo, que a su vez se desvanece bajo la máscara que ya sé que es impenetrable."

emi "¿Qué estás haciendo aquí?"

"No es exactamente la reacción que esperaba, pero a estas alturas no tengo mucho de dónde escoger."

hi "Quería disculparme por lo que dije el otro día."

show emi basic_confused_gym
with charachange

emi "¿El otro día?"

show emi basic_closedgrin_gym
with charachange

"Ella se ríe, una brusca exclamación de incredulidad."

play music music_sadness fadein 0.5

show emi basic_grin_gym
with charachange

emi "Ha pasado casi una semana, Hisao."

hi "Sí, bueno… más vale tarde que nunca, ¿cierto?"

show emi sad_annoyed_gym
with charachange

"Emi se cruza de brazos y me mira fríamente, como si me evaluara. Finalmente, asiente."

show emi sad_grin_gym
with charachange

emi "Mmpf. Supongo que tienes razón. Agua pasada, entonces. Te perdono."

show emi basic_grin_gym
with charachange

emi "¿Eso es todo?"

show emi basic_grin_gym:
    easeout 0.5 xpos 0.3 alpha 0.0
with Pause(0.5)

hide emi
with None

"Su pregunta casi impaciente me toma tan desprevenido que ya está a medio camino de la pista antes de que se me ocurra gritarle."

hi "¡No, espera!"

show emi basic_annoyed_gym:
    center
    xpos 0.4
    easein 0.5 xpos 0.5
with charaenter

"Emi se detiene, da vuelta, y camina de regreso a mí, respirando un poco fuerte y viéndose molesta por mi interrupción."

emi "¿Qué?"

"Bien, necesito hacer esto bien, de alguna manera. Debo conocer el suelo bajo mis pies, tal vez remendar un poco las cosas."

hi "¿Podrías al menos sentarte?"

show emi sad_annoyed_gym at center
with charachange

emi "Creo que estamos bien hablando aquí."

hi "De acuerdo, seguro. Mira, sobre nosotros…"

"Hago una pausa, tratando de pensar en una buena manera de expresar lo que estoy a punto de decir."

"Pero antes de que inicie una apasionada súplica para que me dé otra oportunidad, Emi ya ha hablado."

show emi sad_shy_gym
with charachange

emi "No hay más nosotros, Hisao."

hi "¿Por qué no?"

show emi sad_pout_gym
with charachange

emi "Simplemente no somos el uno para el otro."

"Ella pronuncia esta atroz sentencia sin siquiera mirarme a los ojos."

hi "¡No te creo! ¡Nos va muy bien juntos!"

show emi basic_annoyed_gym
with charachange

emi "Lo dice el chico que está disculpándose por haber sido expulsado de mi casa la semana pasada."

hi "¡Fue una pelea! ¡Dije algo total e increíblemente estúpido y me disculpé por eso!"

show emi sad_angry_gym
with charachange

emi "¿Y cúantas veces habíamos discutido el problema que empezó la pelea? ¿Cuántas veces tuve que decirte que había un límite establecido que no iba a cruzar, y cuántas veces seguiste intentando cruzarlo?"

hi "¡Porque tu límite era estúpido!"

show emi sad_annoyed_gym
with charachange

"Emi pone los ojos en blanco, cruza los brazos sobre su pecho, y ladea la cabeza hacia un lado."

emi "¿Estás viendo esto, Hisao? ¡Es por esto que no somos el uno para el otro!"

"Su voz se suaviza un poco, y se acerca para acariciarme la mejilla."

show emi sad_grin_gym_close
with characlose

emi "Eres un buen chico, pero lo nuestro no funcionará."

"Con una horrible sensación de perder el equilibrio, me doy cuenta de que ella ha estado practicando esto. Quizá todos los días desde que salí de su casa."

"Incluso la caricia en la mejilla parece ensayada, como algo salido de una película."

"Nunca pensó en darme otra oportunidad."

"Qué diablos, ella probablemente habría estado de acuerdo con nunca volver a verme."

hi "¿Así que eso es todo? ¿Nada más qué decir además de “Caray, fue divertido mientras duró, pero hasta nunca”?"

show emi basic_closedgrin_gym_close
with charachange

"La verdad, esto parece divertir a Emi más de lo que yo quería. Ella suelta una risita mórbida."

emi "Así es como he vivido mi vida, Hisao. Ya deberías saber eso."

show emi sad_grin_gym_close
with charachange

emi "Y fue divertido."

"Una sonrisa triste. Ella se estremece ligeramente, y la sonrisa se desvanece."

show emi sad_shy_gym_close
with charachange

emi "Pero ya se acabó. Es lo mejor."

"Quiero pegar un alarido, gritarle a ella. Hacerla entrar en razón, que esto es estúpido, todo el acto. Que solo tiene miedo de mí, miedo de lo que significa ser cercano a alguien."

"Quiero decirle que la amo y que no puedo simplemente renunciar a ella así nada más."

"Excepto… que no tiene sentido. Ella ya decidió. Hemos terminado."

hi "De acuerdo."

show emi sad_grin_gym_close
with charachange

"Emi asiente, satisfecha. Quiero pegarle a algo."

emi "Bien."

show emi basic_grin_gym_close
with charachange

"Ella se anima con una falsa jovialidad."

emi "Te veo luego, Hisao."

hi "No lo harás. Ni siquiera lo intentarás."

show emi basic_grin_gym_close:
    easeout 0.5 xpos 0.3 alpha 0.0
with Pause(0.5)

hide emi
with None

"Ella se encoge de hombros, como si dijera “Como quieras”, y me da la espalda una vez más, acelerando rápidamente por la curva de la pista."

"Me siento entumecido. Esto es todo. El final del camino para nosotros, lo que sea que haya sido. La conclusión, al fin."

"Emi da otra vuelta a la pista sin lanzarme una segunda mirada. Ella está corriendo mucho más rápido ahora, y no puedo evitar recordar nuestra primera carrera juntos."

"Corrí para alcanzarte, para tratar de probar que no era tan débil como yo sabía que era. Pero terminó muy mal para mí, ¿verdad?"

"Y ahora, de nuevo estás corriendo demasiado rápido para mí, y de nuevo tengo la elección de correr detrás de ti."

"Pero no lo haré. No esta vez. Nunca me dejarías alcanzarte."

stop music fadeout 6.0

scene bg school_dormhisao
with shorttimeskip

"Ni siquiera noto cuando estoy alejándome de la pista, o entrando en mi cuarto, o sacando un libro de mi mochila para leer."

"Justo antes de dormir, vuelvo a configurar la alarma. Emi y yo tuvimos nuestro último encuentro."

scene black
with shuteye

"No volvemos a hablar luego de eso."





label es_E27b:


"Bueno, supongo que no hace daño que otra persona conozca mi problema. Y con un demonio, puede que Misha incluso me ofrezca un consejo."

hi "Tuvimos una pelea en su casa."

hi "Yo sigo intentando acercarme a ella, y ella no me dejará acercarme, y…"

hi "Y dije algo estúpido, y ella me echó."

show misha perky_sad
with charachange

mi "¿Has hablado con ella desde entonces?"

"Misha se ve genuinamente preocupada. Estoy sorprendido, casi como si estuviera esperando que ella dejara el tema de lado luego de averiguar cuál era el problema."

"Me sorprende aún más lo rápido que empiezo a confesarle mis problemas."

hi "No, no lo he hecho. Simplemente no me atrevo a verla después de eso."

hi "Actué como un completo idiota, y de todos modos es probable que ahora ella me odie. Especialmente porque no la he visto desde entonces."

show misha sign_smile
with charachange

mi "Eres bastante lento, Hicchan."

stop music fadeout 4.0

"Eso no suena como un consejo."

hi "¿Huh?"

show misha hips_frown
with charachange

"Misha pone los brazos sobre sus caderas e inicia un discurso que sonaría más plausible viniendo de Shizune."

mi "¡La solución a tu problema es simple! ¡Debes ir a disculparte con ella! ¡Dejar las cosas así solo lo empeorará todo!"

mi "¡No puedes saber si te odia a menos de que te lo diga! ¡De otro modo, no hay evidencia de que lo que temes sea verdad!"

mi "Y si Emi realmente te importa, ¿no deberías estar más preocupado por cómo le está afectando todo esto a ella?"

play music music_innocence fadein 1.0

"Con un súbito sobresalto, me doy cuenta de que tiene razón. He seguido despertándome más temprano con esa alarma porque parte de mí quería encontrarse con Emi en la pista para nuestras carreras."

"He seguido corriendo, porque sé que Emi se preocuparía por mí si yo no me mantuviera saludable."

"Ayer cuando fui a la azotea, tenía ciertas esperanzas de que ella estuviera allá arriba, y me sentí decepcionado cuando no fue así."

hi "Soy un idiota."

show misha hips_grin
with charachange

mi "¡Un poco, Hicchan~!"

show misha sign_smile
with charachange

mi "¡Entonces~! Ve a disculparte con ella lo más pronto posible, ¿de acuerdo~?"

"Abro la boca para decirle que lo haré ahora mismo, pero suena la campanada del almuerzo y caigo en la cuenta de que aún tengo que asistir a las clases de la tarde."

hi "La iré a ver, será lo primero que haga cuando terminen las clases. Lo prometo."

hi "Y eh, gracias por los consejos, supongo."

show misha hips_grin
with charachange

"Misha me sonríe resplandeciente, como si fuera una niña que acaba de aprenderse el abecedario."

mi "¡Bien! ¡En ese caso le haré saber a Shicchan que estás bien~!"

hi "Eh, sí. Tú haz eso."

hide misha
with charaexit

"Con un gesto de la mano (e ignorando por completo el hecho de que la gente ha empezado a regresar poco a poco al aula, en vez de salir de ella), Misha abandona el aula."

"Supongo que ella y Shizune tienen asuntos del consejo estudiantil de nuevo."

scene bg school_scienceroom
with shorttimeskip

"Mientras la tarde se arrastra, me encuentro impaciente por que acaben las lecciones. Necesito ver a Emi ahora."

"Debo arreglar las cosas. Incluso si ahora Emi me odia, debo por lo menos disculparme."

"Realmente se lo debo."

"¿Debería verla en su habitación? No, me decido, atrasaría demasiado las cosas. Si conozco a Emi, entonces puedo encontrarla en la pista."

"Aun así no tengo ni idea de qué decir una vez llegue allí, pero me consuelo sabiendo que Emi probablemente tampoco tenga un plan para algo como esto."

"Tendré que improvisar. Deja de estar nervioso, y solo ve a la pista. Averigua el resto cuando estés allí."

scene bg school_track
with shorttimeskip

"La pista aparece frente a mí, y otra descarga de nervios me golpea las entrañas. Resisto el impulso de dar media vuelta e irme, y en vez de eso noto con satisfacción que tenía razón y Emi aún está corriendo."

"No doy muestras de estar aquí de inmediato; en vez de eso me siento en las gradas y la veo correr, recordando viejos encuentros."

show emi basic_confused_gym:
    center
    xpos 0.6
    easein 0.5 xpos 0.5
with charaenter

"Luego de unas cuantas vueltas alrededor de la pista, Emi nota mi presencia y patina hasta detenerse, una expresión de sorpresa que rápidamente se torna una de enfado."

show emi basic_annoyed_gym at center
with charachange

emi "¿Qué estás haciendo aquí?"

"No es exactamente la reacción que esperaba, pero a estas alturas no tengo mucho de dónde escoger."

hi "Quería disculparme por lo que dije el otro día."

show emi basic_confused_gym
with charachange

emi "¿El otro día?"

show emi basic_closedgrin_gym
with charachange

"Ella se ríe, una brusca exclamación de incredulidad."

show emi basic_grin_gym
with charachange

emi "Ha pasado casi una semana, Hisao."

hi "Sí, bueno… más vale tarde que nunca, ¿cierto?"

show emi sad_annoyed_gym
with charachange

"Emi se cruza de brazos y me mira fríamente, como si me evaluara. Finalmente, asiente."

show emi sad_grin_gym
with charachange

emi "Mmpf. Supongo que tienes razón. Agua pasada, entonces. Te perdono."

show emi basic_grin_gym
with charachange

emi "¿Eso es todo?"

show emi basic_grin_gym:
    easeout 0.5 xpos 0.3 alpha 0.0
with Pause(0.5)

hide emi
with None

"Su pregunta casi impaciente me toma tan desprevenido que ya está a medio camino de la pista antes de que se me ocurra gritarle."

hi "¡No, espera!"

scene bg school_track_on
with locationchange

"Ella no parece haberme escuchado —o no quiere escucharme— así que empiezo la persecución, ignorando por completo el hecho de que no estoy vestido para eso."

scene bg school_track_running
with Dissolve(2.0)

"Me duelen los pies, y el cuello de mi camisa se siente como un nudo alrededor de mi garganta, pero aun así la persigo, porque si no lo hago perderé mi oportunidad."

"Emi aún no ha acelerado en serio, la cual probablemente sea la única razón por la que puedo alcanzarla, acercarme y tocarla en el hombro justo antes de que mis piernas no aguanten correr más en zapatos de vestir y den trompicones hasta detenerse."

scene bg school_track_on
with Dissolve(2.0)

"Sorprendentemente (¿afortunadamente?) parece haber valido la pena correr tanto. Me quedo sin aliento, sí, pero al menos mi corazón no intenta abrirse camino fuera de mi caja torácica."

show emi basic_confused_gym_close at center
with charaenter

"El toque en el hombro ha detenido a Emi, e incluso cuando hay un destello de preocupación mientras me mira recuperando el aliento, parece que ella también tiene una buena idea de lo que soy capaz."

"La preocupación no le dura mucho."

show emi basic_annoyed_gym_close
with charachange

emi "¿Qué?"

"Ella se ve tan irritada de que yo aún esté ahí que casi pierdo mi valor, pero ya lo he perdido suficientes veces."

hi "Necesito explicarme. El porqué no puedo dejar que las cosas se queden así."

show emi sad_annoyed_gym_close
with charachange

"Emi recoge los brazos y hace rebotar una de sus prótesis en el suelo en una aproximación a dar golpecitos de impaciencia con el pie. Aún tan enojada, y yo tan nervioso, sigue viéndose hermosa."

emi "De acuerdo, Hisao. Explica."

hi "El asunto es, sé que eres muy sensible acerca del accidente y acerca de tu papá."

"Puedo ver el rostro de Emi crisparse a la mención de las dos cosas que nos han estado alejando sin parar, o que al menos me hicieron sentir a mí que nos estábamos alejando."

hi "Pero creo que es por eso que quiero saber de ellos."

hi "Porque puedo ver cuánto te lastiman, y quiero estar ahí para consolarte."

hi "Me hace miserable, verte falta de sueño y deprimida, y no pretendas que no lo estás, porque yo lo sé, ¿de acuerdo?"

hi "Solo recuerdo esa noche cuando te dormiste conmigo y tuviste esa pesadilla, y que estabas feliz de tenerme allí cuando despertaste."

hi "Quiero ser capaz de estar allí para ti de esa manera siempre que tú necesites que sea así."

show emi sad_depressed_gym_close
with charachange

"El rostro severo se quiebra, levemente. Emi me interrumpe antes de que pueda proseguir."

emi "Solo… detente ahí. No podemos seguir viéndonos, ¿de acuerdo?"

show emi sad_pout_gym_close
with charachange

"Ahora ella está precipitándose, viendo hacia todos lados menos hacia mí. Me sorprende que no eche a correr, ella sabe que no puedo alcanzarla…"

emi "No somos… no somos el uno para el otro."

hi "Eso no es verdad, y lo sabes."

show emi sad_shy_gym_close
with charachange

emi "No, es verdad. Eres demasiado—"

hi "Lo sé. Sé que he sido insistente con conocer tu pasado."

hi "Si aún no puedes decírmelo, entonces al menos déjame estar allí aunque no conozca la razón."

hi "No pasa nada, lo prometo. No te preguntaré por qué necesitas consuelo, solo te lo daré sin pedir nada a cambio."

show emi sad_depressed_gym_close
with charachange

"Emi está sacudiendo la cabeza, y las lágrimas parecen estar amenazando los bordes de sus ojos."

emi "¡Deja de decir eso!"

hi "¿Por qué? ¿Porque tienes miedo de aceptar la oferta?"

show emi sad_pout_gym_close
with charachange

emi "¡No tengo miedo!"

"No logro evitar el tono paternal en mi voz cuando respondo."

hi "Sí, sí tienes. Tú misma me lo dijiste, ¿recuerdas? No tiene nada de malo, lo digo en serio."

hi "Sin embargo, me parece que si alguien se las arreglara para salir vivo de ese accidente y seguir siendo tan alegre y enérgico como tú, tendría la suficiente determinación como para enfrentar ese miedo."

show emi sad_angry_gym_close
with charachange

emi "¿Determinación? ¿Qué sabes tú de determinación?"

hi "Sé que hay una chica tan determinada a cuidar de un completo extraño que robaría su comida durante un festival."

hi "Sé que hay una chica tan determinada a ayudarme con mis propios problemas que planearía una dieta y un plan de ejercicio completos, y que no solo los planearía, sino que los seguiría conmigo, aun cuando no pudiera correr."

hi "Tan determinada a mantenerme a una distancia prudente que se expondría a sufrir emocionalmente si ella pensaba que eso era lo correcto."

hi "Aunque, hay una cosa para la que esta chica tan determinada no tenía un plan, y es que yo podría sentir el mismo tipo de determinación a evitar que ella resultara lastimada."

hi "Me enamoré de ti, y me niego a permitir que todo eso desaparezca porque tienes miedo de perderme."

show emi excited_sad_gym_close
with charachange

"Cualquier poquito de control que Emi todavía mantenía a estas alturas se quiebra, y de repente me encuentro envuelto por su abrazo mientras ella llora."

emi "¿Por qué estás haciendo esto? ¿Por qué no me puedes dejar sola?"

show ev emi_forehead
with dissolve

"La acerco a mí y planto un beso en su coronilla."

hi "Lo lamento, Emi. Tú me ayudaste cuando llegué por primera vez, así que ahora tengo que ayudarte. Es lo más justo."

emi "No tienes remedio, ¿lo sabías?"

"Ella hipa y tiembla un poco."

hi "Qué chistoso, podría decir lo mismo de ti."

emi "¿Puedes hacer algo por mí, Hisao?"

hi "Lo que sea."

scene bg school_track_on
show emi sad_shy_gym_close at center
with charachange

emi "¿Podrías irte, ahora?"

"Se siente como si acabara de clavarme un cuchillo en el pecho."

hi "¿Irme?"

show emi sad_pout_gym_close
with charachange

emi "Necesito… necesito pensar, ¿de acuerdo?"

emi "Es solo que aún no puedo contártelo todo. Aún estoy asustada, y cuando estás cerca, no puedo pensar con claridad."

emi "Pero hazme otro favor."

hi "¿Cuál?"

show emi sad_grin_gym_close
with charachange

emi "Que vengas a nuestra carrera de mañana."

"Sonrío, sintiéndome mejor de lo que me he sentido en toda la semana."

hi "Claro. No me la perdería por nada del mundo."

show emi sad_grin_gym
with charadistant

"Emi retrocede lentamente, casi a regañadientes. Sorbe un poco por la nariz y luego me sonríe, una verdadera sonrisa que ilumina toda la pista, eclipsando a la menguante luz del anochecer."

show emi basic_grin_gym
with charachange

emi "Te veo mañana, Hisao."

hi "De acuerdo."

show emi excited_amused_gym_close
with characlose

show emi basic_grin_gym
with charadistant

"Ella se acerca de repente, me da un suave beso en los labios, y retrocede tímidamente."

show emi basic_grin_gym:
    easeout 0.5 xpos 0.3 alpha 0.0
with Pause(0.5)

hide emi
with None

"Girando sobre los talones, se va a correr de nuevo, y sé que nuestra conversación ha llegado a su fin."

"Siento un cosquilleo en los labios por el calor de ese breve beso y el recuerdo de otros, más extensos."

"Me dirijo de vuelta a mi habitación casi brincando."

"Mañana cuando suene la alarma, me levantaré."

stop music fadeout 2.0

window hide

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
