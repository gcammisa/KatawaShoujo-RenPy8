


label es_NOP1:
window hide None

scene black
with None

scene bg op_snowywoods
show snow
with Dissolve(2.0)

window show

play music music_serene fadein 2.0

"Una suave brisa hace que las ramas desnudas en lo alto repiquen como si fuesen campanillas de viento de madera."

"Este es un retiro popular para las parejas durante el verano. Los árboles de hoja caduca proveen un hermoso dosel verde, lejos de la vista de maestros y compañeros de clase."

"Pero ahora, a finales de invierno, se siente como si estuviera de pie bajo una pila de astillas."


"Soplo dentro de mis manos ahuecadas y las froto con fuerza para evitar que se entumezcan en este frío."

hi "¿Pues cuánto tiempo se supone que esté esperando aquí? Estoy seguro de que la nota decía 4:00 p. m."

"Ah sí… la nota… deslizada entre las páginas de mi libro de matemáticas mientras no miraba."

"En cuanto a clichés, soy más fan de “la carta en el casillero”, pero por lo menos esta manera muestra un poco de iniciativa."

"Mientras reflexiono el significado de la nota, la nevada se espesa gradualmente."

"Los copos de nieve, silenciosamente cayendo desde el cielo pintado de blanco, son la única señal del pasar del tiempo en este mundo paralizado."

"Su lento descenso en el bosque congelado hace parecer que el tiempo se ha ralentizado hasta casi detenerse."

play sound sfx_rustling

"El crujido de la nieve seca bajo los pies me da un sobresalto, interrumpiendo la tranquilidad. Alguien se me acerca por detrás."

mystery "Hola… ¿Hisao? ¿Viniste?"

"Una titubeante y apenas audible pregunta."

"Sin embargo, reconozco al instante a la dueña de esa delicada voz."

"Siento que mi corazón deja de latir."

"Es una voz que he escuchado cientos de veces, pero nunca como algo más que un curioso escuchando una conversación ajena."

"Volteo para darle la cara a esta voz, la voz de mis sueños, y mi corazón comienza a correr…"

window hide

$ ksgallery_unlock("evul other_iwanako")
scene ev other_iwanako_start
show snow
with GenericWhiteout(0.5,0.0,5.0)

window show

hi "¿Iwanako? Recibí una nota diciéndome que esperara aquí… ¿era tuya?"

"Maldita sea. Me pasé toda la tarde tratando de pensar en una buena línea y eso fue el resultado."

"Patético."

"Iwanako" "Ahh… sí. Le pedí a una amiga que te diera esa nota… Estoy tan contenta de que la hayas recibido."

"Una tímida y alegre sonrisa que me pone tan tenso que no podría mover un músculo, aunque lo intentara."

stop music fadeout 10.0

window hide

scene bg op_snowywoods
show snow
with GenericWhiteout(0.5,0.0,2.0)

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)

with Pause(0.7)

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)

window show

"Mi corazón está golpeándome el pecho, como si tratase de reventármelo para salir y reclamar a esta chica como suya."

window hide

scene ev other_iwanako
show snow
with GenericWhiteout(0.5,0.0,3.0)

window show

hi "Así que… ah… aquí estamos. En el frío…"

"Una vez más, el viento agita las ramas. El ruido cacofónico es música para mis oídos."


"Iwanako se estremece muy suavemente ante la ráfaga de viento."

"A medida que pasa, se reincorpora, como si la apoyara una nueva confianza."

"Su mirada se encuentra con la mía mientras perezosamente enrolla su largo y oscuro cabello alrededor de su dedo."

"Al mismo tiempo, el latido ansioso de mi corazón se hace más fuerte."

window hide

scene bg op_snowywoods
show snow
with GenericWhiteout(0.5,0.0,2.0)

window show

"Mi garganta se aprieta; dudo poder siquiera forzar una palabra, aun si lo intentara."

"Iwanako" "Ya ves…"

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.4)

window show

"Iwanako" "… quería saber…"

stop music fadeout 0.5

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

"Iwanako" "… si saldrías conmigo…"

"Me quedo de pie, inmóvil, con excepción del fuerte latido de mi corazón."

"Quiero decir algo como respuesta, pero mis cuerdas vocales se sienten como si hubieran sido estiradas más allá del punto de ruptura."

play music music_tragic fadein 0.5

"Iwanako" "… ¿Hisao?"

"Trato de masajear mi garganta, pero esto solo envía espinas de dolor cegador a lo largo de mis brazos."

"Iwanako" "¡¿Hisao?!"

window hide

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.8)

window show

"Mi cuerpo entero se congela, exceptuando mis ojos, que se disparan abiertos en terror."

window hide

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.8)

with Pause(0.15)

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.8)

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.8)

with Pause(0.05)

play sound sfx_heartstop
show heartattack alpha
with Dissolve (0.1)

stop music fadeout 0.3

show heartattack residual
with Dissolve (0.8)

window show

"Iwanako" "¡HISAO!"

"El latido en mi pecho repentinamente se detiene, y mis rodillas se debilitan."

window hide

show passoutOP1
with None

nvl show Dissolve(0.2)

n "\n\n\n\n\n\n\nEl mundo a mi alrededor —el dosel de ramas desnudas, el pálido cielo de invierno, Iwanako corriendo hacia mí— todo esto se desvanece en la oscuridad."

n "\nLo último que recuerdo antes de caer son los sonidos de Iwanako gritando pidiendo ayuda y el traqueteo incesante de las ramas en lo alto…"

nvl hide Dissolve(3.0)

nvl clear

with Pause (1.0)

scene black
with None


label es_NOP2:

window hide None

scene black
with None

centered "Han sido ya cuatro meses desde mi ataque al corazón." with dissolve

scene bg hosp_room
show sakura
show hospitalmask
with Dissolve (1.5)

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_rain fadein 4.0

nvl show dissolve

n "\n\nEn todo ese tiempo, es probable que pueda contar con una mano las veces que he salido de este cuarto de hospital sin supervisión."

n "Cuatro meses es un tiempo bastante largo cuando te dejan solo con tus pensamientos. Así que he tenido mucho tiempo para aceptar mi situación."

n "Arritmia."

n "Una palabra inusual. Una extranjera y alienígena. Una con la que no quieres estar en la misma habitación."

n "Una condición rara. Provoca que el corazón actúe de forma errática y ocasionalmente lata demasiado rápido. Puede ser fatal."

n "Aparentemente, la he tenido por un largo tiempo. Dijeron que fue un milagro que haya podido continuar por tanto tiempo sin que sucediera nada."

n "¿Es eso realmente un milagro? Creo que se suponía que me haría sentir mejor, con más apreciación por mi vida."

n "En realidad no hizo nada para levantarme el ánimo."

nvl clear

n "\n\n\n\n\nA mis padres, creo, les afectaron más las noticias que a mí. Ellos prácticamente tuvieron dos hemorragias, cada uno."

n "\nYo ya había tenido un día entero para digerirlo todo. Para ellos, todo fue nuevo. Estaban incluso preparados para vender la casa para poder pagar por una cura."

n "\n\nPor supuesto, no hay una cura."

nvl clear

n "Por el tardío descubrimiento de esta… condición, he tenido que quedarme en el hospital para recuperarme de los tratamientos."

n "Cuando recién fui admitido, se sentía como si fuese extrañado…"

n "Por alrededor de una semana, mi habitación en la sala del hospital se encontraba llena de flores, globos y cartas."

n "Pero las visitas pronto se redujeron, y todos los regalos de “recupérate pronto” comenzaron a disminuir hasta no quedar nada, poco después."

n "Me di cuenta de que la única razón por la que recibí tantas cartas y flores, fue porque enviarme su simpatía se había convertido en un proyecto de clase."

n "Quizás a algunos les preocupaba genuinamente, pero lo dudo. Incluso al principio apenas tenía visitas. Para el final del primer mes, solo mis padres venían a verme de forma regular."

n "Iwanako fue la última en dejar de venir."

n "Después de seis semanas, nunca volví a verla. Nunca tuvimos mucho de qué hablar cuando me visitaba, de cualquier manera."


n "Nunca más volvimos a tocar el tema que había entre nosotros aquel nevado día de invierno."

nvl clear

n "\n¿El hospital?"

n "No es realmente un lugar donde me gustaría vivir."

n "Los doctores y enfermeras se sienten tan impersonales y faltos de rostro."

n "Creo se debe a que se encuentran apresurados y tienen otro millón de pacientes esperándolos, pero me hace sentir incómodo."

n "Durante el primer mes, más o menos, le preguntaba al jefe de cardiología cada vez que lo veía por una estimación “grosso modo” de cuándo podría dejar este lugar."

n "Él nunca respondía algo de manera directa, en cambio me decía que esperara y viera si el tratamiento y cirugías habían funcionado."

n "\nAsí que, sin tener nada que hacer, observaba la cicatriz que aquellas cirugías habían dejado en mi pecho cambiar lentamente su apariencia a través del tiempo, pensando en ello como una especie de presagio."



n "Aún le pregunto al jefe de cardiología sobre cuándo podré irme, pero mis expectativas son ahora tan bajas que ya no me decepciono cuando él no contesta. El modo en que evade la respuesta muestra que hay por lo menos un poco de esperanza."

nvl clear

n "\n\n\n\nEn algún momento dejé de ver televisión. No sé por qué, solo lo hice."

n "Tal vez era el tipo equivocado de escapismo para mi situación."

n "\nEn lugar de eso, empecé a leer. Había una pequeña “biblioteca” en el hospital, aunque era más como un almacén para libros. Comencé a leer todo lo que había ahí, una pila pequeña a la vez. Después de consumirla, regresaba por más."

n "Descubrí que me gustaba la lectura, incluso pienso que me volví un poco adicto. Empecé a sentirme desnudo sin un libro en las manos."

n "\nPero me encantaban las historias."

nvl clear

n "\nEso fue lo que era mi vida."

n "\nSe volvió cada vez más difícil distinguir un día del otro, difiriendo únicamente en el libro que leía y el clima afuera. Se sentía como si el tiempo se desdibujara en algún tipo de masa gelatinosa en la que me encontraba atrapado, en lugar de moviéndome dentro de ella."


n "Una semana podía ir y venir sin que yo me diera cuenta realmente."

n "Algunas veces, me detenía al darme cuenta de que no sabía qué día de la semana era."

n "Pero otras veces, todo lo que me rodeaba colapsaba dolorosamente hacia mi consciencia, a través de la barrera de indiferencia que había erguido para mí."

n "Las páginas de mi libro comenzaban a cobrar filo y a arder, la pesadez en mi pecho se hacía tan difícil de soportar que debía dejar el libro de lado y solo recostarme por un rato, mirando al techo como si fuera a llorar."

n "Pero eso pasaba en raras ocasiones."

n "\nY no podía siquiera llorar."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve

nvl clear

window show

"Hoy el doctor entra y me da una gran sonrisa. Parece entusiasmado, pero no mucho. Es como si estuviera esforzándose por verse feliz por mí."

"Mis padres están aquí. Han sido algunos días desde que los vi por última vez. Incluso los dos parecen estar vestidos para la ocasión. ¿Acaso se supone que esto es alguna clase de evento especial? No es una fiesta."

"Hay un ritual que el jefe de cardiología tiene. Se toma su tiempo ordenando sus papeles, luego los pone a un lado como si quisiera enfatizar la inutilidad de lo que acaba de hacer."

"Entonces casualmente se sienta a la orilla de la cama a mi lado. Me ve a los ojos por un momento."

"Doctor" "Hola, Hisao. ¿Cómo estás hoy?"

"No le respondo, pero le devuelvo una pequeña sonrisa."

"Doctor" "Creo que puedes irte a casa; tu corazón es más fuerte ahora, y con un poco de precauciones, deberías de estar bien."

"Doctor" "Ya tenemos todos tus medicamentos en orden. Le daré la receta a tu padre."

"El doctor le da una hoja de papel a mi papá, cuya expresión se convierte en piedra mientras la lee rápidamente."

"Papá" "Son tantos…"

"La tomo de su mano y le echo un vistazo, sintiéndome entumido. ¿Cómo se supone que deba reaccionar a esto?"

$ renpy.music.set_volume(0.5, 2.0, channel="music")

scene white
with Dissolve(2.0)

show wallodrugs:
    xalign 0.0 subpixel True
    easein 25.0 xalign 1.0


"La absurdamente larga lista de medicamentos mirándome de vuelta desde el papel parece insuperable. Todos ellos entremezclándose en un mar de letras."

"Esto es una locura."

"Efectos secundarios, efectos adversos, contraindicaciones y dosis se encuentran listadas línea tras línea con fría precisión."

"Intento leerlas, pero es tan inútil."

"No puedo entender nada de esto. Solo intentarlo me hace sentir más enfermo."

"Todo esto… ¿por el resto de mi vida, todos los días?"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

scene bg hosp_room
show sakura
show hospitalmask
with fade

"Doctor" "Me temo que esto es lo mejor que podemos hacer en este momento."

"Doctor" "Sin embargo, nuevos medicamentos siempre están siendo desarrollados, así que no me sorprendería ver esa lista disminuir a través de los años."

"Años… ¿Qué clase de aliento es eso? Me hubiera sentido mejor si él no hubiera dicho nada en absoluto…"

"Doctor" "Además, he charlado con tus padres y creemos que sería lo mejor si no regresaras a tu antigua escuela."

"¿¡Qué!?"

"Papá" "Por favor, tranquilízate, Hisao. Escucha lo que el doctor tiene que decir…"

"¿Tranquilizarme? La forma en que lo dice me da a entender que sabía por completo que no me agradaría. ¿Seré acaso educado en casa?"

"Lo que sea que mi preocupación muestra, es ignorado."

"Doctor" "Todos entendemos que tu educación es primordial; sin embargo, no pienso que sea prudente que te encuentres sin supervisión."

"Doctor" "Al menos no hasta que nos aseguremos de que tu medicamento es adecuado."

"Doctor" "Así que, he hablado con tus padres acerca de una transferencia."

"Doctor" "Es una escuela llamada Academia Yamaku que se especializa en el trato con estudiantes discapacitados."

"¿Discapacitado? ¿Qué? Acaso soy…"

"Doctor" "Tiene personal de enfermería las 24 horas y está a solo unos minutos de un hospital general de gran prestigio. La mayoría de los estudiantes viven en el campus."

"Doctor" "Piénsalo como un tipo de internado. Está diseñado para dar a los estudiantes un cierto grado de independencia, mientras se mantiene ayuda cercana."

"¿Independencia? Es una escuela para muchachos discapacitados. No trate de ocultar ese hecho."

"Si fuese realmente “libre”, no habría personal de enfermería las 24 horas, y usted no haría del hospital cercano un gancho de venta."

"Papá" "Por supuesto, eso es solo si tú quieres ir. Pero… tu madre y yo no somos capaces de educarte en casa."

"Papá" "Fuimos allá y vimos el lugar hace un par de semanas; pienso que te gustaría."

"Parece que en verdad no tengo opción."

"Doctor" "Comparado con otros problemas cardiacos, gente con tu condición tiende a vivir vidas largas. Necesitarás un trabajo algún día y esta es una buena oportunidad para continuar tu educación."

"Esto no es una oportunidad, no la llame una oportunidad. No la llame una maldita oportunidad."



"Doctor" "Bueno, deberías estar entusiasmado por la oportunidad de volver a la escuela. Recuerdo que querías volver a ella, y si bien no es la misma…"

"Una escuela especial. Eso es…"

"Un insulto. Eso es lo que quiero decir. Es un paso atrás."


"Papá" "No es lo que piensas. Todos los estudiantes ahí son bastante activos, en su propio modo."

"Papá" "Está dirigida a estudiantes que todavía pueden moverse y aprender, pero solo necesitan un poco de ayuda… de alguna forma u otra."

"Doctor" "Tu padre está en lo correcto. Y muchos de los graduados de esa escuela han llegado a hacer cosas asombrosas. Una persona no tiene que ser frenada por su discapacidad."

"Doctor" "Uno de mis colegas en otro hospital es un graduado."

"No me importa. ¿Una persona no tiene que ser frenada por su discapacidad? Eso es lo que una discapacidad es."

"Realmente odio que algo tan importante haya sido decidido por mí. Pero ¿qué puedo hacer al respecto? Una vida “normal” es ahora imposible."

stop music fadeout 10.0

"Es gracioso, siempre había pensado que mi vida era un poco aburrida, pero ahora la extraño."

"Quiero protestar. Quiero culpar de esta falta de reacción al estado de shock, o fatiga. Podría fácilmente gritar algo en este momento; algo sobre cómo puedo regresar a la escuela en cualquier caso. Pero, no."

"No digo nada. El hecho es que ahora sé que es inútil."

"Veo alrededor de la habitación, sintiéndome muy cansado de todo esto. El hospital, los doctores, mi condición, todo. No veo nada que me pueda hacer sentir diferente."

"En realidad no hay ninguna opción. Esto lo sé, pero el pensar que iré a una escuela para discapacitados… ¿y cómo se supone que son esas? Por más que trate de verle el lado positivo, es muy difícil."



"Pero permítanme intentar."

"Un borrón y cuenta nueva no es algo malo."

"Eso es en todo lo que puedo pensar para salir de esto. Al menos todavía tengo algo; incluso si es una “escuela especial”, es algo. Es un nuevo inicio, y mi vida no ha terminado. Sería un error simplemente resignarme a pensar eso."

"Por lo menos, trataré de ver cómo será mi nueva vida."

window hide




label es_A1:

window hide None

scene bg school_gate
with Dissolve(3.0)

play music music_happiness

window show

"El portón se veía demasiado pomposo para lo que era."

"De hecho, los portones en general parecen tener esa característica, pero más este en especial."


"Ladrillos rojos, hierro forjado negro y yeso gris, ensamblado en un todo que no se sentía acogedor en lo más mínimo."

"Me preguntaba si se veía como un portón de escuela debería verse, pero realmente no pude decidir. Probablemente no."

"Por supuesto, no quería quedarme ahí pensando sobre el portón por demasiado tiempo, entonces entré por este con un ritmo enérgico que se sintió sorprendentemente bien."

"Avanzar se siente bien."

scene bg school_courtyard
with locationchange


"Así que camino hacia el edificio principal de la Academia Yamaku con este paso rápido. Me encuentro solo, ya que mis padres están llevando mis cosas a los dormitorios y se supone que hay alguien esperándome."

"Los jardines son increíblemente exuberantes, llenos de verde."

"No se siente como el tipo de campus que una escuela tendría, es más como un parque, con un camino limpio pasando por los árboles y el olor a césped recién podado y todas las demás cosas como en los parques."

"Palabras como “limpio” e “higiénico” aparecen en mi mente. Me hacen temblar."

"Me las quito de encima. Mantente con mente abierta ahora. Es tu nueva vida. Tienes que tomártelo tal y como venga."

"Eso es lo que me digo a mí mismo."

"Algunos edificios grandes se asoman sobre las copas frondosas de los árboles, demasiado grandes y demasiado numerosos para solo una escuela."


"Todo parece fuera de lugar; es diferente de lo que pensé que sabía de ellas."

"Es un valle misterioso. Aunque me hayan dicho que esta es mi nueva escuela, en el fondo no se siente como tal."

"Me pregunto si el sentimiento es real o causado por mis expectativas de una escuela para discapacitados."

"Hablando de eso, no veo a nadie más aquí. Es un poco desconcertante."

"Me hace desear que hubiera alguien más aquí para poder anclarme en algo tangible, en lugar de tener esta sensación de haber entrado en otra dimensión."

"Los árboles susurran con el viento, y los tonos verdes destellando a mi alrededor capturan mi atención."

"Me hace pensar sobre hospitales otra vez, el cómo dicen que las salas de operaciones están pintadas de verde porque el verde es un color tranquilizador."

"Entonces ¿por qué es que me siento tan ansioso, a pesar de toda esta vegetación?"

"…"

"Solo después de estar delante del presuntuoso edificio principal, me sorprendo a mí mismo al darme cuenta del porqué el portón me molestaba:"

"Era la última oportunidad que tenía de volver atrás, aunque no tuviera una vida a la cual regresar."

"Pero aun así, después de entrar, no había ninguna manera en absoluto de volver atrás."

"Sintiéndome nervioso y con este pensamiento en la mente, abro la puerta de entrada."

scene bg school_lobby
with locationchange

"Un hombre alto con mala postura me ve al entrar. Somos las únicas personas en el vestíbulo, así que es simplemente lógico."

show muto normal at center
with charaenter

mu_ "Usted debe ser… Ni… Na… ¿Niki?"

hi "Nakai."

show muto smile
with charachange

mu_ "Así que es usted. Excelente. Soy su maestro de cabecera y de ciencia. Mi nombre es Mutou."

mu "Bienvenido."

"Intercambiamos un apretón de manos que no es ni firme ni torpe, y mira su reloj."

show muto irritated
with charachange

mu "El jefe de enfermería pidió que fueras con él para una breve visita de chequeo, pero ya no hay tiempo para eso."

hi "Oh. ¿Debería ir más tarde?"

show muto normal
with charachange

mu "Sí, en la tarde puede que esté bien. Deberíamos irnos y presentarte al resto de la clase. Ya están esperándote."

"¿Esperándome? En verdad no me gusta ser el centro de atención, pero supongo que es inevitable en una situación como esta."

"De alguna manera, no saber qué es lo que me espera me hace sentir muy nervioso."

"Pensando en esto, casi dejo pasar lo que el maestro está diciendo."

label es_choiceA1:
menu:
    with menueffect
    mu "¿Quieres presentarte tú mismo a la clase?"
    "¿Por qué?":



        return m1
    "Seguro, por supuesto.":

        return m2

label es_A1a:

hi "¿Por qué? ¿Tengo que hacerlo?"

mu "Claro que no. Por eso es que pregunto."

hi "Cierto."

mu "Entonces vamos."



label es_A1b:

hi "Sí, claro. Quiero decir, ¿no es eso normal?"

mu "Por supuesto. Pero no a todos les agrada ser el centro de atención."

"Probablemente soy una de esas personas, pero creo que yo debería ser quien da la primera impresión de mí mismo."

hi "Cierto, pero no es ningún problema."

mu "Entonces vamos."



label es_A1c:

scene bg school_staircase2
with locationchange

"Mi corazón late con fuerza dentro de mi pecho y me mantiene pensando sobre mi condición mientras subo por las escaleras junto con el maestro."

scene bg school_hallway3
show muto normal at center
with locationchange


"La tercera puerta del corredor del tercer piso está marcada como el salón de clase 3-3."

play sound sfx_dooropen

"Mutou abre la puerta y entra."

show muto normal at Alphaout(0.5), Slide(0.5,0.5,0.4,0.5,0.5,_ease_out_time_warp)
with Pause (0.5)

hide muto
with None

mu "Buenos días a todos, discúlpenme por llegar tarde otra vez."

stop music fadeout 2.0

"Dudo por una fracción de segundo en la puerta, congelándome justo en ese lugar."





label es_A2:

scene bg school_hallway3
with None

"¡Ah, contrólate! Este es un gran paso, lo sé… Pero no tiene sentido preocuparse tanto por ello, al menos no tan pronto."

scene ev hisao_class_start
with fade

play music music_normal fadein 0.5

"Sigo al maestro hacia dentro del salón y veo alrededor, parcialmente para no tener que encontrarme con las miradas curiosas de mis nuevos compañeros de clase."

"Es bastante espacioso; el techo es inusualmente alto y hay mucho espacio de sobra alrededor y entre cada escritorio."

"Una pared entera ocupada por pizarrones, además de ventanas altas y anticuadas únicamente lo hacen parecer más grande."

"Los bancos de los estudiantes son solo escritorios estándar de madera con un cajón debajo para libros y sillas de madera con armazón de metal. Simple y eficiente."

"Me detengo al frente del salón de clase y volteo a ver a los demás estudiantes. Todos parecen normales, como estudiantes en cualquier otra escuela. Pero entonces, ¿por qué estarían aquí?"

scene ev hisao_class_move
with None


"Probablemente son como yo y hay algo mal en ellos, solo que no se evidencia inmediatamente. Entonces, me doy cuenta de que a una de las chicas parece faltarle el pulgar de la mano derecha. Es un poco discordante."

"A pesar de la tendencia natural de escuchar cuando alguien habla de ti, dejo de oír al maestro a medio discurso mientras me presenta a la clase."

"Noto un destello de cabello oscuro y veo que alguien me mira. Una chica con cabello verdaderamente largo y lacio que llama mucho la atención. Cuando ve que la miro, se cubre la cara con las manos como si eso la hiciera invisible."

"Hay un chico con un bastón apoyándose contra los casilleros en la parte trasera del salón. Es raro ver a alguien tan joven con un bastón."

"Otra chica parece estar haciendo algunos movimientos extraños con las manos. ¿Lenguaje de señas? Ella mira por encima de la montura de sus anteojos, y luego regresa a lo que fuera que estaba haciendo."

"Es bastante linda. También lo es la chica con apariencia alegre de cabello rosado que se sienta a su lado. Es muy difícil pasarla por alto; no sé cómo es que no la noté desde el momento en que entré…"

mu "… por favor denle la bienvenida a nuestro más nuevo compañero de clase."

"Aplaude y también lo hacen todos los demás, excepto una chica en la primera fila que solo tiene una mano. Me avergüenzo un poco, pero lo oculto con una reverencia de agradecimiento por este aplauso que no merecía."


label es_A2a:

"Después del aplauso, hay un breve silencio que nadie parece querer ser el responsable de romper."


"El maestro pronto se da cuenta de que probablemente debería decir algo. Empieza con un ruido indescifrable, se calla al ir perdiendo su ímpetu, y entonces comienza a presentarme."

"Nadie parece muy interesado."

"Tal vez debería de haber dicho sí a eso de presentarme yo mismo."


"Quizás comprendiendo que en verdad no sabe nada de mí, acaba diciendo mal mi nombre una vez más, y me pide escribirlo en el pizarrón."

"Lo hago, y me vuelvo para ver a la clase, sintiéndome raro."


label es_A2b:

"Un silencio colectivo me dice que debería abrir la boca ahora."



hi "Bueno… soy Hisao Nakai."

"¿Y después de eso?"

hi "Mis pasatiempos son la lectura y el futbol. Espero llevarme bien con todos aunque sea un estudiante nuevo."

"¿Y después?"

"Estoy siendo tan aburrido. Esto es exactamente como cualquier otra presentación. Debería decir algo más. Algo más emocionante."

"Termino sin decir nada, y el maestro continúa a partir de ahí."


"Sin embargo, todo mundo parece estar satisfecho incluso con lo poco que dije. Algunas chicas se susurran entre sí, lanzando miradas hacia mí. Podría haber sido peor."

"…"


label es_A2c:

scene ev hisao_class_end
with None

"Escucho al maestro mientras sigue hablando sobre llevarse bien a la vez que paso la mirada por el salón de clase."


"Todos parecen escucharlo atentamente y cuando acaba, aplauden de nuevo, se siente como algo extraño de hacer."

"La chica en la primera fila aplaude esta vez, con su única mano contra la otra muñeca que termina en un muñón vendado."

"Me hace sentir un poco mal."

scene bg school_scienceroom at bgright
show muto normal at center
with fade

mu "Haremos algo de trabajo en grupo este día, así que eso te dará una oportunidad de hablar con todos. ¿Estás de acuerdo con eso?"

hi "Sí, por mí está bien."

show muto smile
with charachange


mu "Eso es bueno, puedes trabajar con Hakamichi. Es la representante del grupo."


mu "Ella puede explicarte cualquier cosa con la que puedas tener problemas. Y quién mejor para hacerlo, ¿no?"

hide muto
with charaexit

"¿Cómo podría saberlo?"

"El maestro reparte las tareas de hoy y anuncia que trabajaremos en grupos de tres."

"Me llega de golpe que no sé quién es Hakamichi. Lento. El maestro parece captar mi expresión de impotencia."

mu "Oh, cierto. Hakamichi está justo ahí, Shizune Hakamichi."

show misha perky_smile at center
with charaenter

"Al llamar su nombre, la linda chica de apariencia efervescente con brillante pelo rosado y ojos dorados me hace un gesto con su mano. Tomo asiento junto a ella, al lado de la ventana."

hi "Hola, supongo que tú eres Hakamichi, ¿no? Es un gusto conocerte."

stop music fadeout 1.0

show misha cross_laugh
with charachange

mi_shi "¡Jajaja~!"

"¿Qué? Su risa me toma por sorpresa."

show misha hips_grin
with charachange

mi_shi "¡También es un gusto conocerte!{w=0.5} ¡Pero~!"

mi_not_shi "¡También es un gusto conocerte! ¡Pero~!{fast}, yo no soy Hakamichi, ¡soy Misha! Ella es Hakamichi. ¡Shicchan~!"

play music music_shizune fadein 1.0

show misha hips_grin at twoleft
show bg school_scienceroom at center
with charamove

show shizu basic_normal at tworight
with charaenter


"Riendo, Misha apunta a la chica a su lado, a quien vi usando lenguaje de señas antes. Parece que ha estado mirándome todo este tiempo. Ella asiente con la cabeza una vez con indiferencia para mostrar que reconoce mi presencia… pero solo apenas."

"Ella tiene cabello corto pero cuidadosamente cepillado, un par de anteojos en forma de óvalo se balancean en la punta de una delicada nariz, y ojos azul oscuro que parecen alternar cada pocos segundos entre una mirada analítica y algo aburrida."

hi "Gusto en conocerte."

show shizu behind_blank
with charachange

shi "…"

show misha perky_smile
with charachange

show misha sign_smile
with charachange

show misha perky_smile
with charachange

"De inmediato voltea a ver a Misha, quien sonríe y hace un gesto rápido con las manos."

show shizu adjust_happy
with charachange

show shizu behind_smile
with charachange

"Hakamichi asiente y hace algunos gestos propios."

"Empiezo a preguntarme si el maestro estaba jugando conmigo, diciendo algo como “podrás hablar con la gente” y “quién mejor para explicarte las cosas”."

show misha hips_smile
with charachange

mi "Puedo ver que estás un poco confundido, ¿cierto?, ¿cierto? Pero, ¡entiendo por qué pensarías que yo soy Shicchan!"

mi "Shicchan es sorda, así que soy yo quien traduce las cosas de un lado a otro para ella."

show misha hips_grin
with charachange

mi "¡Soy como una intérprete~! ¡Ella dice que es un gusto conocerte, también!"

show shizu basic_normal2
with charachange

shi "…"

show misha perky_smile
with charachange

mi "Eres el nuevo estudiante, ¿no? Bueno, Shicchan, ¡claro que lo es! Si no lo fuera, habría estado ahí parado sin razón alguna, ¿cierto? ¡Cierto~!"



label es_A2d:

mi "Se ve como una persona muy interesante, ¿no es así~?"



label es_A2e:

"Misha me ve con una expresión rara, después continúa."

mi "No sabemos mucho de él, pero tal vez nos enteraremos más tarde."

"Tal vez debería haberme presentado yo mismo después de todo. Cualquier cosa hubiera dado una mejor primera impresión que el parloteo del maestro, mientras se equivocaba con mi nombre."



label es_A2f:

mi "Sabíamos que iba a haber un nuevo estudiante, pero no sabíamos que estarías aquí este día. ¡Tan pronto! Hicchan, ¿verdad?"

"¿Hicchan… ?"

show misha hips_grin
with charachange

mi "¡Síp~! Te queda, ¿no?"


"¿Lo dije en voz alta? Es un tanto sorprendente. Nunca me ha gustado ese apodo."

hi "En verdad no veo cómo."

show misha cross_grin
with charachange

mi "¡Sí queda~! ¡Eres justo como te imaginé!"

show shizu adjust_smug
with charachange

shi "…"

show misha cross_laugh
show shizu adjust_happy
with charachange

mi "¡Jajajaja~! ¡Sí, te ves justo como un Hicchan!"

hi "Me pregunto por qué es que todos parecen pensar así…"

shi "…"


"Hakamichi golpetea sus dedos sobre el escritorio para llamar la atención de Misha. Ambas gesticulan de un lado a otro entre ellas con emoción, sus manos demasiado rápidas para poderlas seguir."

show shizu adjust_happy
with charachange

show misha sign_smile
with charachange

show shizu behind_smile
with charachange

show misha perky_confused
with charachange

"Misha luce un poco abrumada."

show misha hips_grin
with charachange

mi "¡Ajaja~! Ehh, ¡perdón por eso!"

show misha hips_smile
with charachange



mi "Shicchan quiere que sepas que ella es la representante del grupo, así que si hay algo que necesites saber, puedes sentirte con la libertad de preguntarle."

show shizu behind_blank
with charachange

shi "…"

show misha sign_smile
with charachange

mi "¿Te ha gustado la escuela hasta ahora? Podemos mostrarte un poco los alrededores si no has tenido tiempo de andar por ahí y…{w=0.5}{nw}"

show misha perky_smile:
    "misha perky_confused" with Dissolve(0.5, alpha=True)
with None


extend " ¿familiarizarte?{w=0.5}{nw}"

show misha perky_confused:
    "misha perky_smile" with Dissolve(0.5, alpha=True)
with None

extend " ¡Con el lugar!"

"Misha tropieza un poco con la palabra complicada, haciéndola sobresalir en su traducción, de otro modo, fluida."

hi "Gracias, eso es muy amable de su parte. Seguro, prácticamente vine directo a clase hoy."

show shizu behind_frown
with charachange

shi "…"

show misha hips_laugh
with charachange

mi "¡Jajaja~!"

show misha hips_smile
with charachange

mi "¡Eso no está bien! Siempre deberías tratar de aprender lo más que puedas acerca del lugar adonde vas antes de ir allá. ¡No solo con la escuela~!"

show misha hips_grin
with charachange

mi "¡Siempre! ¡Incluso si es un viaje a la tienda! ¿En serio, Shicchan? ¡Jajaja~!"

show misha perky_smile
show shizu behind_smile
with charachange

"¿Aprender acerca de adónde vas? Creo que no me molesté en hacerlo, o simplemente no me importaba lo suficiente como para hacer eso."


"No esperaba esto con ansias, aunque yo mismo me comprometí a ir con la corriente sin muchas ganas, pero en fin."

"No digo nada, y Misha dice algo en señas que termina con ella encogiéndose de hombros. ¿Qué fue eso? Parece que era sobre mí."


"Siento que quiero desplomarme sobre el asiento. Ambas sonríen, pero ese encogimiento de hombros me golpeó de forma inesperadamente profunda."

show misha perky_sad
with charachange

mi "Te ves triste, ¿estás bien?"

show shizu basic_normal
with charachange

shi "…"

show misha perky_smile
with charachange

mi "¡Por favor, no lo tomes a mal~! ¡Odio cuando las personas tienen miedo de hacer preguntas! ¡Así es como la gente aprende, preguntando~!"

mi "Pedir ayuda es perfectamente normal, ¡tanto como necesitar ayuda! ¡Deja de verte como si acabaras de reprobar un examen!"

show misha cross_laugh
with charachange

mi "¡Guajajaja~!"

hi "De acuerdo."

show shizu adjust_happy
with charachange

shi "…"

show misha perky_smile
with charachange

mi "Ah, y otra cosa, ¡no tienes que llamar a Shicchan de forma tan formal, como “Hakamichi” o “representante del grupo” todo el tiempo! ¡Solo llámala Shicchan~!"

stop music fadeout 0.5

show shizu adjust_blush
with charachange

shi "…"

show misha hips_smile
with charachange

mi "¡Ajaja~! Bueno, puede que eso sea demasiado casual. Tal vez “Shizune” sería más apropiado."

show shizu basic_normal2
with charachange

shi "…"

show misha hips_grin
with charachange

play music music_shizune fadein 5.0

mi "¡Síp, síp~! ¡“Shizune” está bien!"

hi "Je. Está bien, eso sería bastante más fácil para mí."

"Me siento mucho más tranquilo. Ambas parecen amigables, así que me siento como un idiota por haber estado tan preocupado antes. Especialmente por Shizune, quien supuse sería toda seriedad y trabajo."


"Bueno, ella todavía me da esa idea. Solo que un poco menos, supongo."

show shizu behind_frown
with charachange

shi "¡…!"

show misha perky_confused
with charachange

mi "¿Eh? ¡Oh, cierto, no hemos ni tocado el trabajo! Deberíamos empezar ahora, o Shicchan se enojará."

hi "La tarea también es un poco larga, así que deberíamos empezar ahora, si queremos terminar antes del final de la clase."

show misha hips_laugh
with charachange

mi "¡Guajaja~! ¡Eso también!"

show shizu basic_frown
with charachange

shi "…"

"Shizune nos mira con dureza e impaciencia. No necesito saber lenguaje de señas para entender eso."

hi "Está bien, está bien. Entiendo el mensaje."

show shizu basic_normal
with charachange

shi "…"

show misha perky_smile
with charachange

mi "Después de clase, podemos pasear por los jardines juntos. ¡Hoy es un bonito día! ¿De acuerdo~?"

"A decir verdad la tarea es muy difícil de realizar, combinando aspectos de ser tanto complicada como innecesariamente larga."

stop music fadeout 6.0

scene bg school_scienceroom
with shorttimeskip

"Aun así, la terminamos unos minutos antes que el resto del salón, a pesar de nuestro inicio tardío. Shizune y Misha son realmente capaces."

"Sin embargo, son bastante diferentes. La representante del grupo es tan tranquila y profesional como se ve, mientras que Misha es mucho más juguetona y candorosa. Sin mencionar que se distrae con facilidad."

"Siendo honesto, ellas hicieron la mayor parte del trabajo. Me siento culpable por ello."

play sound sfx_normalbell

"La torre del reloj suena, señalando el final del período. Tiempo para el almuerzo."

scene bg school_hallway3
with locationchange

"Sin saber qué otra cosa hacer, sigo a Misha, quien me llama con señas para que vaya al corredor y baje las escaleras."




label es_A3:

scene bg school_staircase2
with locationchange

"Descendemos aún más abajo del vestíbulo donde me encontré con Mutou, hasta la planta baja."

play ambient sfx_crowd_indoors fadein 6.0

scene bg school_cafeteria
with locationchange

"Al igual que todo en esta escuela, la cafetería parece demasiado espaciosa y extrañamente moderna, contrastando con el exterior clásico."

"Sus grandes ventanales dan al patio, hacia el portón principal."

show misha hips_grin
with charachange

play music music_ease

mi "¡Es la cafetería~!"

"Su entusiasta afirmación sobre lo obvio hace que la gente alrededor voltee a vernos, pero eso no parece importarle a Misha, así que procedemos a la fila."

hide misha
with charaexit

"Hay una lista considerablemente larga de opciones en el menú, lo que parece genial, hasta que me doy cuenta de que muchas de ellas son para dar cabida a aquellos estudiantes que necesitan dietas especiales."

"Pero qué lindo. Hasta casi se siente como si estuviera de vuelta en el hospital, comiendo porciones medidas con precisión científica para cumplir las necesidades de los pacientes."

"Escojo algo al azar y sigo a Shizune a una mesa, sentándome frente a ella."

show misha hips_frown at twoleft
show shizu basic_normal at tworight
with charaenter

"Mientras indiferentemente mordisqueo la comida que preferiría no comer, Misha me da un codazo en el costado para llamar mi atención y apunta a Shizune."

show misha perky_smile
show shizu basic_frown
with charachange

shi "…"

"No entiendo las señas, así que el significado me elude."

"¿Tal vez mirar a la persona con quien “hablas” es correcto y educado?"

show misha hips_smile
show shizu behind_blank
with charachange

mi "¿Quieres saber algo?"

hi "¿Qué?"

show misha hips_grin
with charachange

mi "¡Sobre cualquier cosa! ¡Somos tus guías, así que deberías preguntar si hay algo~!"

label es_choiceA3:
menu:
    with menueffect
    hi "Hmm, me pregunto…"
    "Preguntar sobre la biblioteca.":


        return m1
    "Preguntar sobre la sordera de Shizune.":

        return m2
    "Creo que ya sé todo lo que tengo que saber.":

        return m3

label es_A3a:

hi "Oh, sí. ¿Hay una biblioteca en la escuela? Últimamente me ha dado por leer mucho, así que me gustaría ir a verla."

"Misha hace el tipo de gesto que deja claro que ella no considera a la lectura como un pasatiempo sano, pero entonces recupera su sonrisa de nuevo."

mi "¡Sí la hay~! ¡Está en el segundo piso, te la podemos mostrar alguna vez!"

hi "Gracias."

"Regreso a mi comida mientras las chicas hablan entre ellas."



label es_A3b:

"Shizune me intriga, y siento que quiero preguntar algo acerca de ella."

"Pero en realidad no puedo preguntar sobre algo tan personal, ¿o sí?"

"Hmm…"

"No se me ocurre otra cosa más sobre qué preguntar, así que simplemente me concentro en mi comida mientras las chicas hablan entre ellas."



label es_A3c:

hi "No se me ocurre nada, en verdad."

show misha sign_smile
with charachange

mi "¡Ooh! Eso significa que hemos sido buenas guías, ¿o no?, ¿o no~?"

"…"

hi "Eeh… si tú lo dices."

show misha hips_grin
with charachange

show shizu behind_smile
with charachange

"Misha definitivamente sonríe con energía, y también lo hace Shizune después de una rápida traducción."



"Sacudo la cabeza a causa de su entusiasmo un tanto exagerado, y cambio mi atención hacia la comida."



label es_A3d:

"Misha y Shizune gesticulan de un lado a otro entre ellas muy animadamente, arrojándome miradas, pero Misha se abstiene de traducir."

"Quizás estén hablando de cosas secretas de chicas o algo así."

"…"

stop music fadeout 3.0
$ renpy.music.set_volume(1.0, .5, channel="ambient")
stop ambient fadeout 3.0

"Rápidamente me percato de que una conversación en señas no es suficiente para llenar un silencio."

scene bg school_scienceroom
with shorttimeskip

play music music_daily fadein 0.5

"Llegamos temprano al salón de clases, pero no somos los primeros."

show hanako emb_downtimid at Transform(xanchor=0.8, xpos=1.0)
with charaenter

"Esa chica de cabello oscuro que vi antes se encuentra desplomada sobre su escritorio en la última fila."

show hanako defarms_shock
with vpunch

show hanako defarms_shock at Transform(xanchor=0.6, xpos=1.0)
with charamove

"Ella salta un poco cuando Misha entra estrepitosamente al salón con la elegancia de un rinoceronte."

"Se encoge más dentro de su asiento. Puedo sentir su tensión desde acá, como si lentamente se estuviera convirtiendo en piedra solo por nuestra presencia."

"Misha y Shizune, o bien no lo notan o no les importa, ya que caminan directamente delante de ella hacia sus asientos y comienzan a conversar."

show hanako defarms_shock at offscreenright
with charamove

hide hanako
with None

"Me quedo pensando en ella, incluso cuando el salón se llena lentamente con otros estudiantes y finalmente, el maestro."

"Entrar en el ritmo escolar se siente extraño; es como si mi cerebro recordara cómo se hace esto, pero mi cuerpo no."

"Hacia el final de la clase empiezo a bostezar y a contar los minutos restantes."

"No debería estar así de cansado en mi primer día de clases."

"Tal vez sea el largo tiempo pasado en el hospital el que me ha hecho así. Incluso me siento físicamente débil y sin vida."

scene bg school_scienceroom
with shorttimeskip

play sound sfx_normalbell

"En poco tiempo, suena la campanada final."

"La escuela ha terminado por este día, finalmente."

"A mi lado, Misha y Shizune tienen una corta conversación. Después de un momento de deliberación, Misha se vuelve hacia mí."

show shizu behind_blank at tworight
show misha perky_smile at twoleft
with charaenter

shi "…"

mi "Desafortunadamente no podemos quedarnos y mostrarte el lugar por hoy, Hicchan. Debemos darnos prisa, ya que hay mucho trabajo por hacer."

show shizu basic_normal2
with charachange

shi "…"

mi "Encontrarás tu camino por aquí, de eso estoy segura."

hi "¡Ah, espera! El maestro dijo que debía ver al enfermero. ¿Adónde tengo que ir?"

show shizu behind_smile
show misha hips_grin
with charachange

mi "¿En serio? ¡Al menos podemos mostrarte eso~!"

mi "Vamos, la enfermería tiene su propio edificio, así que tenemos que salir."

hide shizu
hide misha
with charaexit

scene bg school_hallway3
with locationchange

"Nos unimos al flujo de estudiantes bajando las escaleras y yendo hacia afuera, con las chicas indicando otros salones de niveles avanzados en el mismo corredor que el nuestro."

scene bg school_courtyard
with locationskip

"Cuando llegamos al exterior, las chicas se dirigen al edificio más pequeño justo a un lado de la escuela."

"Está construido con el mismo estilo, así que realmente parece ser una parte del edificio principal."

show shizu behind_smile at tworight
show misha perky_smile at twoleft
with charaenter

shi "…"

mi "Este es el edificio auxiliar. Hay un montón de cosas oficiales e importantes adentro, como la oficina de la Fundación Yamaku y todas las oficinas de enfermería. ¡Incluso tienen una piscina!"

hi "¿Cómo es eso oficial?"

show shizu behind_frustrated
with charachange

shi "…"

show misha hips_grin
with charachange

mi "¡No seas tonto, Hicchan! Es para terapia física, por supuesto."

show misha sign_smile
with charachange

mi "De cualquier forma, todas las instalaciones para el personal de enfermería se encuentran también aquí. La oficina del jefe de enfermería está en el primer piso."

show misha hips_smile
show shizu behind_smile
with charachange

mi "Estarás bien de ahora en adelante, ¿cierto~? ¡Nos retiramos entonces! ¡Hasta mañana!"

hi "Sí, gracias. Nos vemos."

stop music fadeout 5.0

hide shizu
hide misha
with charaexit

"¿Todo un edificio para cosas que realmente no tienen nada que ver con educación?"

"Supongo que es necesario para un lugar como este."

scene bg school_nursehall
with locationchange

"Camino hacia adentro, con la esperanza de que esto en verdad sea solo una visita rápida como dijo el maestro."

"En una puerta blanca a la izquierda hay una cruz verde con la leyenda “Jefe de Enfermería” y una placa con un nombre."

play sound sfx_doorknock2

"Una voz desde el interior responde cuando llamo a la puerta casi de inmediato, pero no puedo entenderla del todo."


"Sonaba un poco como una invitación a abrir la puerta, así que me permito seguir más adentro."

play sound sfx_dooropen

scene bg school_nurseoffice
with locationchange

"El lugar no es grande y huele extraño, pero un hombre de aspecto amable se da la vuelta sobre su silla de oficina para verme entrar."

"Su escritorio está limpio y ordenado, pero el cesto debajo de la mesa se desborda con utensilios médicos usados, y hay por lo menos una docena de anillos de tazas de café manchando el escritorio."

play music music_nurse fadein 0.5

show nurse neutral at center
with charaenter

nk_ "Hola, qué tal. ¿Qué puedo hacer hoy por ti?"

"Tiene aspecto juvenil y algunas facciones fuertes, pero los hoyuelos en sus mejillas borran esa impresión cuando sonríe."

hi "Ehh, ¿es usted el enfermero?"

show nurse grin
with charachange

"Sonríe como una persona que ha escuchado esta misma pregunta cientos de veces."

nk_ "Pues sí, sí lo soy. Lo dice ahí mismo en la puerta, ¿no?"

nk_ "Puedes llamarme por mi nombre o solo “el enfermero” como todos los demás."

"Por supuesto. Me quito la confusión de encima, dándome cuenta de que probablemente debería tomar su mano extendida.{w} Su apretón de manos es bastante firme y amigable."

hi "Claro… ehh, soy un estudiante nuevo y mi maestro de cabecera me dijo que viniera a verlo. Mi nombre es Hisao Nakai."

play sound sfx_snap

"Sus ojos se iluminan con revelación y chasquea los dedos."

show nurse fabulous
with charachange

nk "Ah, eres ESE Nakai. Justamente estaba leyendo tu archivo esta mañana."

nk "Algún tipo de arritmia crónica y deficiencia del músculo cardiaco congénita relacionada, ¿cierto?"

"Señala que me siente en un sillón vacío frente a su escritorio."

hi "Eh, sí."

show nurse neutral
with charachange

nk "Bien. Bueno, probablemente ya has sido informado acerca de la escuela lo suficiente, así que voy a pasar rápido por eso."

nk "Tenemos todo tipo de instalaciones disponibles, principalmente terapia física y demás."

nk "Siempre hay alguien de mi personal alrededor, incluso de noche, así que nunca dudes en llamarnos si hay un problema."

"El famoso personal de enfermería las veinticuatro horas del día."

hi "Guau, esto es como un hospital."

nk "Bueno, no exactamente. Por ejemplo, aquí no hacemos cirugías de cerebro."

"Su broma se siente tan fuera de lugar que me quedo pensando en por qué es que la dijo."

hi "Sí… es solo que se siente raro tener tanto personal médico en una escuela."

nk "Te acostumbrarás."

"No estoy tan seguro de eso, pero no dejo que el enfermero lo sepa."

nk "Ahora, solo déjame encontrar tu archivo otra vez…"

"Mientras él busca algo desde su computadora y cambia pilas de papeles de un lugar a otro, dejo que mi mirada ande por la oficina."

"Es el epítome de genérico, quisiera decir."

"Paredes y techo de color beige, piso con laminado de color gris oscuro, y todo el equipo que esperarías en una enfermería escolar."

"Incluso los ridículos carteles educativos cuelgan de las cuatro paredes, recordándome que debo comer apropiadamente — tres veces al día y de todos los grupos alimenticios."

show nurse grin
with charachange

"Sonriendo, el enfermero saca un grueso archivo de un montón de archivos igualmente gruesos, y lo abre."

nk "Entonces, ya tienes medicamentos para la arritmia, solo recuerda tomar las pastillas cada mañana y noche o no será de mucha ayuda."

show nurse fabulous
with charachange

nk "Aparte de eso… ¿haces algún deporte? Cosas fuertes como… no lo sé, ¿boxeo?"

"Se sonríe por su propia broma, pero yo no."

hi "Eh, bueno. Jugaba futbol ocasionalmente con algunos compañeros de clase."

nk "Muy bien, me temo tendré que recomendarte que te abstengas de hacer eso. Al menos por el momento."

hi "Oh."

"Mi falta de reacción lo hace levantar una ceja, pero en serio, no me molesta mucho que me prohíban patear una pelota por todas partes."

"Supongo que nunca lo hice por una ardiente pasión por el deporte. Únicamente para tener algo que hacer."

nk "Cualquier tipo de contusión podría ser muy peligrosa para tu corazón y arriesgarse a otro ataque no es una buena idea."

nk "¿Fue el anterior causado por un golpe súbito a la región pectoral? No hay mención de la causa en tus papeles."

hi "Ehh… no exactamente."

show nurse concern
with charachange

"Evado la pregunta en forma aceptable, y me mira por encima de sus papeles, con una expresión más seria en su cara."

nk "Sin embargo, necesitas mantener tu cuerpo saludable así que algo de ejercicio te haría bien."

nk "Como dije, tenemos terapia física y demás cosas disponibles, pero no pienso que realmente necesites medidas tan fuertes."

nk "Simplemente haz un poco de ejercicio ligero de manera regular."

nk "Caminatas a paso rápido o incluso trote ligero, saltar la cuerda, ese tipo de cosas. ¿Natación, tal vez? Tenemos una piscina aquí."

hi "Sí, me han dicho."

show nurse neutral
with charachange

nk "¿Te han dicho? Muy bien."

nk "En cualquier caso, y estoy seguro de que esto ya te lo han dicho antes, solo debes tener cuidado de no esforzarte demasiado."

"Mueve su dedo para enfatizar el punto. No hay necesidad en verdad, esto lo he escuchado mil veces ya."

show nurse concern
with charachange

nk "Absolutamente ningún riesgo innecesario. Cuídate a ti mismo."

hi "Está bien."

"Revisa mis papeles una vez más y los deja sobre el escritorio, obviamente satisfecho."

show nurse neutral
with charachange

nk "Bien. Eso es todo, entonces. Ven a verme si alguna vez necesitas algo."

scene bg school_nursehall
with locationchange

stop music fadeout 2.0

"Soy escoltado hacia afuera antes de darme cuenta. Una visita rápida, en verdad."




label es_A4:

scene bg school_courtyard
with locationchange

play music music_pearly fadein 4.0

"Termino de pie frente a los edificios principal y auxiliar, aunque ante mis ojos, los dos aún parecen ser uno."

"Es la primera vez que me detengo a mirar a los demás estudiantes, así que veo gente salir de la escuela, yendo hacia el portón o a los dormitorios."

"Todos parecen saber adónde van."

"Y yo sigo pensando que la mayoría de ellos no se ven tan especiales por ser estudiantes en una escuela especial. Por otro lado, tampoco yo."

"¿Acaso eso me hace uno de ellos?{w} ¿Uno de nosotros?"

"…"

"También yo debería irme a alguna parte, como prevención para no perderme."

"Es casi tiempo de la cena, pero me siento cansado en lugar de hambriento."

"El cansancio solo aumenta a medida que camino con dificultad hacia los dormitorios, que se encuentran un poco alejados del edificio principal."

scene bg school_gardens
with locationchange

"Hay una especie de jardín entre la escuela y los dormitorios; arbustos, flores y el dominante aroma de césped recién cortado que llena el ambiente."

"Mi mente cansada cae en la cuenta de que el aroma parece novedoso porque no he estado fuera por tanto tiempo."

scene bg school_dormext_start at bgleft
with locationchange

"El edificio del dormitorio es grande, hecho de ladrillo rojo. Como los otros, se siente demasiado pomposo para lo que es; así que sigo adelante, entrando al edificio."

scene bg school_dormhallground
with locationchange

"Toma más tiempo del necesario pescar la llave que me dieron de mi bolsillo."

hi "Habitación uno-uno-nueve…"

"A pesar del exterior ornamentado, el interior del dormitorio se ve considerablemente nuevo, funcional, y aburrido."

"Al igual que el edificio principal, los pasillos y las puertas son amplios para darle cabida a sillas de ruedas."

"Asomo mi cabeza por una esquina de la puerta a la sala común."

"Dentro hay algunos estudiantes viendo televisión."

"Uno asiente la cabeza y da un “hola” rápido antes de regresar a ver la televisión."

"Parece que únicamente las chicas son sociables por aquí. Supongo que eso está perfectamente bien para mí."

"Subo las escaleras al piso superior."

scene bg school_dormhallway
with locationchange

"Aquí, pasillos angostos se ramifican del corredor principal."

"Cada uno de estos pasillos menores parece tener un inodoro y una ducha, así como cuatro habitaciones."

"Como a mitad del pasillo, alcanzo a ver la habitación 119."

"Las placas con los nombres en las habitaciones adyacentes a la mía están en blanco. Creo que solo hay dos de nosotros aquí."

play sound sfx_doorknock2
stop music fadeout 3.0

"Una luz brilla por debajo de la puerta de la habitación 117, así que toco la puerta ligeramente."

hi "Hola, ¿hay alguien en casa?"

"Desde dentro, escucho unos movimientos, luego el ruido de muchas más cerraduras de las que pensé que estas puertas tenían. Después de un momento la puerta se abre con un rechinido."

show kenji tsun at Slide(0.4,0.5,0.5,0.5,0.5)
with charaenter

play music music_kenji fadein 0.5

"Un chico con anteojos se encuentra de pie en la puerta. Me mira con mucha atención a través de sus lentes extremadamente gruesos."

ke_ "¿Quién es?"

"¿Ciego? No, al menos no del todo, ¿por qué tendría anteojos si lo fuera?"

show kenji tsun_close at center
with characlose

"Se inclina más hacia mí hasta que nuestras narices están por tocarse. Su aliento apesta a ajo."

hi "Hisao Nakai… Me estoy mudando a la habitación de al lado. Pensé que debería presentarme…"

show kenji happy
with charadistant

"Su rostro se ilumina en súbita comprensión, parándose derecho y disparando su mano al frente en un saludo sonriente, casi directo a mi diafragma."

ke_ "Oh, ¿qué hay, viejo? Me llamo Kenji."

hi "Ah, qué tal."

"Tomo la mano sudorosa de Kenji y la aprieto, todavía un poco sacudido por el repentino cambio de actitud y vehemente bienvenida."

ke "Había unas personas de aspecto sospechoso entrando y saliendo de tu habitación antes."

hi "Posiblemente eran mis padres."

show kenji tsun
with charachange

ke "¿Tus padres? ¿Seguro? Porque podrían haber sido otros tipos, también. No puedes juzgar un libro por su portada."

"Su proverbio fuera de lugar se queda colgando entre nosotros incómodamente mientras intento pensar en alguna forma de responder."

hi "Yo diría que las probabilidades son lo suficientemente altas."

"Se estremece y hace algunos gestos exagerados con las manos."

show kenji neutral
with charachange

ke "Eres un hombre valiente, Hisao."

show kenji tsun
with charachange

ke "Yo, no creo que podría confiar en la probabilidad."

ke "En el único en quien confío es en mí mismo."

hi "¿Acaso eso significa que no debería conocerte?"

"Él piensa por un momento en esto."

show kenji neutral
with charachange

ke "Una sabia decisión."

show kenji happy
with charachange

ke "Maldición, eres más listo de lo que te ves."

ke "Probablemente."

ke "¿Cómo te ves? Espero que no muy listo."

show kenji neutral_close
with characlose

"Entrecierra sus ojos y se inclina hacia mí de nuevo, pero me inclino hacia atrás para evadirlo."

show kenji tsun
with charadistant

ke "No tiene importancia, en lo absoluto."

hide kenji
with charaexit

stop music fadeout 3.0

"Con esto, se da vuelta, torpemente busca por un momento el picaporte,{w=0.3}{nw}"

play sound sfx_doorslam

extend " y cierra la puerta detrás de él."

"Deslizo la llave en la cerradura de la puerta marcada 119."

scene bg school_dormhisao_ss
with locationchange

play music music_night fadein 1.0

"Oscuras paredes beige, sábanas blancas, un escritorio hecho de algún tipo de madera ligera. Feas cortinas."

"Es la habitación de nadie; impersonal, como era mi habitación en el hospital."

"Mis bolsas todavía están al pie de mi cama, viéndose mucho más vacías que en esta mañana."

"El guardarropa se encuentra abierto, repleto de mi ropa."

"Además, parece que hay varios uniformes escolares colgando ahí."

"Hay una nota fijada en la manga de una de las camisas."

window hide

$ written_note("Qué tal Hicchan. Hemos desempacado tus cosas, y hecho tu cama.\nEllos dijeron que si estos no te quedan, entonces fueras a la oficina mañana.\nSi tienes cualquier problema, siempre puedes llamarnos.\n\nCon cariño, Papá y Mamá.")

window show

"Bueno, por lo menos no tengo que preocuparme por desempacar."

"De cierta forma esperaba poder hacerlo, entonces habría algo qué hacer."

"Todavía es muy temprano."

"Pongo la nota sobre el escritorio y me recuesto en la cama, sintiéndome exhausto."


"Quedarme acostado así hace que me den ganas de leer algo, pero no tengo nada conmigo."

"Me pregunto si el hospital me condicionó para querer leer cuando no tengo nada que hacer."

"El inquietante impulso tan solo sigue creciendo hasta que tengo que ponerme de pie."

"Tal vez es estrés o algo parecido."

"Estaba muy nervioso antes de venir aquí y durante todo el día también. Aún lo estoy, creo."

"Rayos, debo distraerme de alguna manera, así no seré tan raro todo el tiempo."

"Mañana iré a sacar algunos libros de la biblioteca."

"Sí, eso es lo que haré."

"Pero por ahora…"

show pills:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"Los frascos de medicamentos, cuidadosamente ordenados sobre la mesa de noche, atrapan mi atención."

"Tomo uno y lo agito solo para escuchar su contenido, y entonces leo la etiqueta pegada al frasco."

window hide

show pills:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide pills
with None

$ written_note("Hisao Nakai\n\nDos tabletas diarias para mantenerte vivo.", quiet=True)

window show

"Realmente no dice eso, pero bien podría hacerlo."

"Es un poco retorcido, tener tu vida dependiendo de químicos como estos. Lo resiento un poco, pero, ¿qué elección tengo?"

"Con un suspiro, comienzo mi ritual diario de tomar el número correcto de pastillas de cada frasco, siendo cuidadoso de revisar las dosis correctas."

"…"

"Me recuesto de nuevo, con una sensación de vacío e incertidumbre, entonces me mantengo viendo el techo, desconocido y en blanco, por un largo tiempo."

stop music fadeout 8.0

scene bg school_dormhisao_ni
with Dissolve(3.0)

"No comienza a parecer ni un poco más familiar, aun después de que cayera la oscuridad y largas sombras se dibujaran a través de mis paredes como si fuesen dedos."

"Las sábanas se sienten un poco más confortables, cálidas como un nido en contra del frío que pasa por temperatura ambiente en este lugar."

"Pronto el matiz más claro de oscuridad que es el techo, se ve como cualquier otro techo durante la noche, y se convierte en lo único que reconozco."

"La noche me llama a dormir, y siento el frío de lo desconocido y el temor arrastrándose por mi espalda una vez más."

"Sigo a la deriva, alejándome cada vez más del mundo que conocí."

$ suppress_window_after_timeskip = True

scene black
with shuteye


return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
