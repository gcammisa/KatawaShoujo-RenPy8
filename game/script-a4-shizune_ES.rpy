label es_S30:

window hide None

scene bg school_library
with locationchange

window show

play music music_happiness fadein 2.0

"Solo un día después, el fin de semana ya ha llegado. Dejo caer una pila pesada de libros sobre el escritorio de la bibliotecaria, sin querer golpearlos, pero pesan tanto que ocurre de todos modos."

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_impact

show yuuko panic_up:
    center
    ypos 1.2 alpha 0.0
    easein 0.25 ypos 1.0 alpha 1.0
with vpunch

show yuuko panic_up:
    center
    alpha 1.0
with None

"Yuuko salta de su silla con suficiente fuerza como para hacer caer sus anteojos. Ella apenas los sujeta."

show yuuko neutral_up
with charachange

yu "Oh, hola."

hi "Lo siento. Estoy aquí para devolver todos esos libros que debía entregar."

show yuuko worried_down
with charachange

yu "Eso es genial, pero desearía que los hubieras traído antes. No sería un problema si la biblioteca tuviera más copias de todo, pero no las tiene… y ellos actúan como si fuera mi culpa."

hi "¿“Ellos”?"

show yuuko panic_down
with charachange

yu "Otros estudiantes. Ellos pueden ser… em, bastante insistentes."

hi "Lo siento. Simplemente como que se me olvidó. Ha sido un par de días bastante duro."

show yuuko worried_down
with charachange

yu "Oh… Em, supongo que no quieres hablar de ello…"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\nDe manera sumisa, Yuuko se pone a la tarea de registrar todos los libros que he traído de vuelta como “devuelto”, tratándolos con extremo cuidado y precisión, como si ella fuera más una técnica antiexplosivos que una bibliotecaria."

n "Durante el último par de días, he estado pensando en algo que Misha dijo. Por supuesto, había pensado en todo lo que ella dijo, pero una cosa en particular sigue regresando. Ella habló de cómo no quería extrañar a las personas ni pensar en estar separada de ellas nunca más."

n "Cuando recordé esas palabras, me detuvieron en frío, como una bofetada brusca en la mejilla. En solo unos meses, nos estaremos graduando. Misha y Shizune eran casi inseparables, pero después de la graduación, puede que ellas nunca se vuelvan a ver. Me pregunto si ese pensamiento es lo que comenzó todo esto."

n "Si Misha tratara de hablar con Shizune sobre esto, probablemente Shizune no pensaría en ello en absoluto. Eso la entristecería, y por esa razón, ella intentaría ignorarlo. Para alguien como Shizune, quien es tan rápida en suprimir sus preocupaciones, sería fácil."

nvl clear

n "\n\nMisha resultó ser más sensible de lo que parecía. Eso la habría destrozado, aun más porque la reacción de Shizune podría resultar bastante fría. No sé si así es como Shizune lo manejaría, pero parece probable, y puedo entender por qué ella actuaría de esa manera."

n "También puedo entender por qué Misha estaría afligida por la idea de alejarse de alguien que es una parte tan importante de ella. Nunca había pensado en la graduación hasta ese momento."

n "Entonces comencé a pensar cosas como, “¿Realmente solo ha pasado menos de un año?”. Comencé a pensar en todas las personas que he conocido. No solo en Shizune y Misha, sino en todas los demás. Ellas son pensamientos afectuosos. Entonces, pensé en perderlas. De repente, pude entender las ansiedades de Misha."

n "\nSería bueno hablar con alguien al respecto."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear
window show

hi "En realidad, como que quiero hacerlo."

show yuuko worried_up
with charachange

yu "¿Con quién?"

"Puedo sentir una obvia matiz de aprensión en su voz."

hi "Contigo."

show yuuko neurotic_up
with charachange

yu "Ah… ¿En serio? ¿Estás seguro? ¿P-por qué yo?"

hi "Porque eres adulta."

show yuuko neurotic_down
with charachange


yu "¿Es eso? Ahhhh… eso es…"

"Apenada, ella se mueve un poco en su asiento, intentando ponerse cómoda en una manera que se ve muy incómoda. Supongo que eso significa que ella está bien con eso."

hi "¿Es difícil, ser adulto?"

show yuuko cry_down
with charachange

yu "Sí."

show yuuko panic_down
with charachange

yu "Pero no creo que yo sea tan vieja… Es sorprendente que los estudiantes ahora, c-como Shizune y tú, usen cosas como perfumes o colonia… Yo nunca lo hice. Aún no las uso…"

show yuuko worried_up
with charachange

yu "Em, por cierto, hoy no estás usando tu colonia de uva."

hi "Sí, no estaba funcionando para mí."

show yuuko worried_down
with charachange

yu "Oh, eso es bueno. Pensaba lo mismo… Lo siento."

"Se ve que Yuuko está genuinamente apenada, y siento una punzada de culpa. Sonrío, a pesar de mí mismo. Una pequeña mentira como esa puede regresar para morderme el trasero."

"Para Misha, intentar esconder cómo se sentía con el fin de poner una cara feliz para Shizune por tanto tiempo debió haber sido devastador."

hi "Alguien que conozco sacó el tema de que nos vamos a graduar, y me di cuenta de que nunca he pensado en ello antes."

hi "Me siento estúpido de que pudiera pasar tanto tiempo y nunca pensara en estas cosas. He conocido a muchas personas grandiosas, y nunca he pensado en cómo será graduarme y quizás nunca volverlas a ver."

show yuuko neutral_down
with charachange

yu "Aún hay maneras en las que podrías ponerte en contacto…"

hi "Sí, supongo. Me siento infantil. Sé que todos probablemente están pasando por lo mismo. Apuesto a que escuchas mucho este tipo de problemas."

show yuuko worried_down
with charachange

yu "N-no… No he estado trabajando aquí mucho tiempo…"

show yuuko worried_up
with charachange

yu "Me preocupaba por lo mismo cuando me gradué de la preparatoria. Em, aunque no estudié aquí. También extraño a mis amigos… y desearía haber mantenido un mejor contacto con ellos. Debí haberme esforzado más."

"Yuuko realmente no me está ayudando a sentir mejor, y se calla rápidamente cuando lo ve en mi rostro."

hi "No quiero mirar atrás y tener esos mismos remordimientos."

hi "Me pregunto si hasta Shizune piensa en ese tipo de cosas. Debido a lo que ella dice a veces, acerca de cómo ella no quiere vivir con remordimientos."

show yuuko panic_up
with charachange

yu "Vaya… Eso suena imposible, para mí…"

"Asiento con la cabeza, solo queriendo estar de acuerdo a medias."

show yuuko closedhappy_up
with charachange

yu "Aun así… También creo que es algo admirable… Algo valiente. ¿No lo crees?"

hi "“Valiente” es una nueva manera de decirlo."

show yuuko neutral_down
with charachange

"Yuuko mueve su cabeza insistentemente."

yu "Pero es cierto. Y también algo intimidante…"

hi "Rayos. No deberías estar intimidada por estudiantes de preparatoria."

show yuuko worried_up
with charachange

yu "Lo intentaré…"

hide yuuko
with charaexit

"Ella se da la vuelta para comenzar a doblar una nota adhesiva una y otra vez. Un comportamiento bastante ocioso para una estudiante universitaria, pero lo más importante, me pregunto si le dije algo equivocado."

"Al estar con Shizune por tanto tiempo, no puedo dejar de leer tanto como pueda en cada momento de silencio."

"Si Yuuko fuera el tipo de persona que no se intimidara por estudiantes de preparatoria, probablemente no sería tan fácil hablar con ella."

"Es demasiado fácil querer eliminar una cualidad negativa tuya. Cuando pienso en todas las personas que conozco, son esas cualidades las que más me gustan."

show yuuko worried_up at center
with charaenter

yu "Em…"

show yuuko smile_down
with charachange

yu "No creo que realmente me arrepienta. Pensé, mientras que pudiera recordar los buenos momentos, eso era suficiente."

show yuuko worried_down
with charachange

yu "No lo sé… Lo siento."

"Noto un par de estudiantes entrando a la biblioteca, y decido que mi tiempo se acabó."

hi "No, eso fue de ayuda."

hi "Siento que dos de mis amigas están peleando porque una de ellas se está tomando muy duro el hecho de que puede que no nos veamos de nuevo después de que nos graduemos."

hi "Y la otra probablemente está siendo estoica al respecto, lo cual solo lo empeora."

hi "No entiendo cómo se supone que maneje este tipo de situación. No parece ser el tipo de problema en donde tendré que terminar eligiendo un bando, pero podría resultar de esa manera, y entonces no tengo idea de lo que voy a hacer."

show yuuko neutral_down
with charachange

yu "Deberías decirles que no deberían pelear."

hi "Lo sé. Pelear es malo."

hi "No son Shizune y Misha, por cierto."

show yuuko worried_up
with charachange

yu "Bueno… Em, aunque realmente no estaba pensando en eso…"

"Qué vergonzoso. Aunque sabía que lo sería, todavía siento mis mejillas enrojecerse, e incluso así, aún dije algo tan transparente y abiertamente falso. Pero podría ser que a veces eso es lo correcto."

hi "¿Tienes algunos libros sobre personas que tienen que tomar decisiones difíciles?"

show yuuko happy_down
with charachange

yu "Tenemos muchos libros de autoayuda…"

"Es curioso que pueda encontrar eso sorprendente, porque no me habría sorprendido hace solo unos meses."

hi "Quise decir “sobre”, no “para”. No hay muchos, ¿cierto?"

show yuuko worried_down
with charachange

yu "Sí. Em, no muchos, quiero decir."

stop music fadeout 3.0

"Aunque me siento un poco inquieto al respecto, quiero hablar con Shizune. No entiendo por qué me siento nervioso por ello, y eso me disgusta un poco."

scene bg school_council
with locationskip

"Eso también me motiva a buscarla, justo en ese momento y lugar, aunque no tengo que buscar mucho. Ella está en el salón del consejo estudiantil, como siempre."

play music music_pearly fadein 5.0

show shizu behind_blank at center
with charaenter


"Preocupantemente, Misha no está con ella. Cuando Shizune me nota y levanta la mirada de su papeleo, lo primero que pregunto es dónde está ella."

show shizu basic_normal2
with charachange

ssh "No lo sé."

"Hay tanta incertidumbre en su respuesta que no puedo dejarla pasar así como así."

his "Ella está faltando mucho a la escuela."

show shizu adjust_happy
with charachange

ssh "¿Eres la policía de asistencia?"

his "Eso es muy extraño, viniendo de la presidenta del consejo estudiantil."

show shizu adjust_smug
with charachange

"Shizune esconde una risa detrás de una mano ahuecada, y comienzo a pensar que podría estar preocupándome por nada, pero entonces su risa lentamente se desvanece hacia una expresión más seria y pensativa."

show shizu basic_normal
with charachange

ssh "Tienes razón."

show shizu behind_blank
with charachange

ssh "Ayer,"

show shizu adjust_happy
with charachange

"Capto el indicio de una sonrisa cómplice en su rostro cuando ve mi pánico pobremente escondido ante la palabra. A pesar de sus mejores esfuerzos, ella no puede evitar estar satisfecha al provocar sorpresa en todos los demás, hasta el final."

"Incluso entonces, puedo ver que ella tiene preocupaciones más grandes debido a cómo su sonrisa desaparece rápidamente."

show shizu basic_angry
with charachange

ssh "… antes de que alguno de ustedes me notara, vi lo que estaban diciendo. No soy estúpida."

show shizu behind_frown
with charachange

ssh "Si no lo hubiera hecho, aún podía verlo en Misha cuando estábamos caminando de regreso. Incluso si no me lo hubiera contado todo más tarde. Ella no puso mucho problema por ello, pero de cualquier manera que lo veas, es mi culpa, ¿no es así?"

his "¿Qué te dijo?"

show shizu adjust_frown
with charachange

"Shizune se estremece ante la pregunta, aunque es claro que ha estado esperándola. Ella continúa con un gesto muy imponente."

show shizu basic_normal2
with charachange

ssh "Mucho."

show shizu adjust_frown
with charachange

ssh "Como, que puedo ser egoísta, y confusa. Me esfuerzo demasiado en traer gente a mi alrededor, y luego la alejo de mí."

show shizu basic_normal2
with charachange

ssh "No sabía lo que debía hacer. Pensé que ella tenía razón en mencionar todas esas cosas, así que simplemente estuve de acuerdo con ella, pero eso solo empeoró las cosas."

show shizu behind_sad
with charachange

ssh "No lo entiendo."


"Al ajustar sus anteojos, ella se ve muy cansada. Espero que no sea porque estuvo ocupada evitando a Misha, pero no puedo dejar de considerar la posibilidad, al ver a dónde va esta conversación."

show shizu adjust_smug
with charachange

ssh "Es cierto. Incluso con el consejo estudiantil siendo tan pequeño, y nosotros estando siempre inundados de trabajo, es mi culpa. Puede que hasta haya terminado apartando a mucha gente, y alejándola del consejo estudiantil, al actuar de esa manera."

"Shizune mueve un dedo pícaramente, reconociendo que “puede que” es una sutileza. Sin embargo, por la manera cansada como lo hace, es obvio que el humor es solo para tranquilizarme, y por tanto no es genuino."

show shizu basic_normal
with charachange

ssh "Como Lilly, por ejemplo. Ella fue la primera persona en unirse cuando comencé a intentar reclutar gente de nuevo después de que todos los demás se fueron, porque no pudieron soportarme, supongo."

show shizu adjust_happy
with charachange

ssh "Logramos preparar el último festival, y hasta manejamos un puesto juntas a último minuto."

show shizu behind_frown
with charachange


ssh "Pero no me agradaba porque yo pensaba que ella era egoísta, siempre retrasándonos para ayudar a una amiga suya o de otra, y dejándonos a Misha y a mí solas para arreglar las cosas relacionadas con toda la escuela por nuestra cuenta."

show shizu cross_angry
with charachange

ssh "Si había algún problema por el que ella estaba pasando, nos dejaba plantadas mientras entraba en pánico por ello, y no regresaba hasta que estuviera resuelto."

show shizu adjust_angry
with charachange

ssh "¡Ella se enfocaba en eso al cien por ciento, y estaba muy preocupada como para enfocarse en cualquier trabajo del consejo estudiantil!"

show shizu behind_frustrated
with charachange

ssh "Eso fue lo peor, para mí, que ella podía ser tan amable y aun así menospreciar a tanta gente. ¿Entonces por qué se unió al consejo estudiantil? Parecía tan corta de vista y egoísta, ¿no lo crees?"

show shizu basic_normal2
with charachange

ssh "Pero, en realidad soy yo la que es así."

show shizu adjust_frown
with charachange

ssh "Como dijo Misha, siempre intentando acercar a la gente y luego apartándola."

show shizu behind_sad
with charachange

ssh "Así es como la he tratado a ella, lo cual me hace una mala amiga. Y entonces parece que hice lo mismo contigo, así que supongo que también soy una mala novia, aunque Misha diga que bien podrías reemplazarla."

show shizu basic_normal2
with charachange

ssh "Estoy enojada por arruinar las cosas tanto como para que se salgan de las manos. Todo lo que quería era…"

stop music fadeout 3.0

"Ella hace una pausa para buscar las palabras correctas, juntando sus dedos en concentración."

show shizu behind_blank
with charachange

ssh "Hacer feliz a la gente, creo."

show shizu adjust_happy
with charachange

ssh "Aunque eso parezca una manera simple de decirlo."

"Mientras ella apoya su cabeza sobre su mano, su flequillo cae delicadamente frente a sus ojos, escondidos detrás de esos anteojos brillantes que reflejan solo un poquito de luz."

"Puede que esté mal pensar así, pero ahora mismo, ella parece especialmente bella. Como una persona más completa."

"Se siente que esta es mi primera oportunidad para responder a su efusión de emociones. ¿Reemplazar a Misha como intérprete de Shizune? Misha debe estar bromeando."

"Necesité de toda mi energía para seguir su ritmo justo ahora, con sus señas llenas de gestos que nunca he visto antes."

"Probablemente, son hábitos tomados de Misha, y desarrollados por los años que han estado juntas. Yo nunca podría reemplazar a alguien tan cercana a ella."


his "Me gustas porque me gustas, no porque me hayas hecho creer eso."

"A pesar de lo mucho que se esforzó, de todos modos. Sigo mirando a sus ojos, tan intensos como siempre. La primera vez que los vi, me parecieron un poco intimidantes. Como los ojos de un depredador. Eso no ha cambiado, lo que me tranquiliza."

show shizu basic_normal
with charachange

ssh "Aún quiero hacerlos felices a todos."

his "¿Empezando con Misha?"

play music music_shizune fadein 6.0

show shizu basic_frown
with charachange

"Shizune se ve un poco molesta de que yo insinúe que ella comenzaría con alguien más, y sonríe con confianza, como si la tristeza de una amiga fuera un oponente físico al que puede estrangular hasta la sumisión."

show shizu behind_frustrated
with charachange

ssh "Por supuesto; obviamente; naturalmente."


show shizu adjust_noglasses
with charachange

"Quitándose sus anteojos, ella se reclina en su silla y deja salir un suspiro. Es la primera vez que la he visto sin ellos, pero no consigo verla bien antes de que se los vuelva a poner."

show shizu behind_smile
with charachange

ssh "Pero estoy muy cansada para comenzar hoy. Lo primero mañana."

show shizu basic_normal
with charachange

ssh "¿Quieres ayudar?"

his "Sí."

show shizu adjust_happy
with charachange

ssh "Y… tengo otras cosas del consejo estudiantil con las que me podrías ayudar, mientras estás en eso."

"Aunque resulta que no hay muchas otras cosas."

stop music fadeout 2.0
$ suppress_window_after_timeskip = True

scene black
with dissolve




label es_S31:

window hide None

scene black
with dissolve

with Pause(2.0)

play sound sfx_doorknock

with Pause(2.0)

scene bg school_dormhisao
with openeye

window show

play sound sfx_doorknock

"No hay escuela hoy, así que esperaba poder dormir hasta tarde. Desafortunadamente, soy despertado por alguien que golpea despiadadamente en mi puerta a las ocho de la mañana."

"Al comienzo, creo que podría ser Kenji, pero cuando mis gritos de enojo no son respondidos, me doy cuenta de que es Shizune."

play sound sfx_dooropen

scene bg school_dormhallway
show shizu adjust_happy_close at center
with locationchange

play music music_another fadein 0.5

show shizu behind_blank at center
with charadistant

"Ella inmediatamente se aleja de la puerta cuando la abro, ocultando rápidamente algo detrás de su espalda. Un poco ominoso."

his "¿Qué es eso? ¿Es una sorpresa? En realidad no me gustan las sorpresas."

show shizu behind_frown
with charachange

"La expresión de disgusto en su rostro dice que ella quiere que yo deje de ser tan aguafiestas, pero está muy ocupada lidiando con lo que tiene detrás de su espalda como para decirlo en señas."

show shizu adjust_smug
with charachange

"Debe ser frustrante para ella, porque segundos más tarde, muestra el objeto, balanceándolo con orgullo, y también de una manera un poco peligrosa."

show shizu basic_happy
with charachange


ssh "Ta-rá. Una canasta de picnic. Podemos almorzar juntos, nosotros tres."

"En realidad no es una canasta, parece más una bolsa de plástico. Echando un rápido vistazo adentro, puedo ver que la mayoría de la comida también fue comprada en tiendas y no hecha en casa. Algunos objetos aún tienen puesta la etiqueta de precio."

"Pero hay una selección muy diversa aquí. Incluso una pequeña lata de caviar. Poco a poco me impresiono más con este almuerzo. Tomo una uva de allí y la meto en mi boca."

show shizu adjust_frown
with charachange

ssh "¡No hagas cosas como esa! Pasé toda la noche perfeccionando esta arma final."

show shizu adjust_frown:
    ease 0.5 ypos 1.2
    ease 0.5 center
with Pause(0.5)

play sound sfx_pillow

show shizu basic_normal:
    ypos 1.2
    ease 0.5 center
with charachange

"Shizune la pone en el suelo para liberar sus manos, y de inmediato comienza a darle golpecitos alegremente entre sus pies como un balón de futbol. Definitivamente eso no es lo que harías con cualquier cosa a la que llames un “arma final”."

show shizu adjust_happy at center
with charachange

ssh "Todo es parte de mi plan llamado “hacer que Misha deje de estar tan deprimida”. Estuve despierta toda la noche trabajando en él."

show shizu behind_smile
with charachange

ssh "Cuando intentamos ordenar la última vez, Misha escasamente comió algo, y lo usó como excusa para irse temprano. No dejaré que se escape tan fácilmente esta vez. La comida ya está aquí. Ella tendrá que sentarse y comer con nosotros."

show shizu basic_happy
with charachange

ssh "Es el señuelo perfecto. ¿No se ve irresistible? Intenté hacerlo yo misma, pero no sé cómo hacer que se vea todo elegante, así que terminé comprando todo. Aun así se ve delicioso, ¿no es así? Debería serlo."

"Ella está muy alegre hoy, animada por la idea de alegrar a Misha. Aunque es extraño verla tan feliz por eso, sé que ella ahora está tan insegura como lo estaba ayer."

"La única cosa que ha cambiado es que al verlo como otro desafío para ella misma, puede poner sus preocupaciones a un lado y lanzarse a ello imprudentemente."

"Ha funcionado bastante bien para Shizune hasta ahora. No me sorprendería si esa fuera la única manera en que ella sabe cómo vivir."

his "Pero es un poquito temprano…"

show shizu adjust_frown
with charachange

ssh "Ya son las ocho de la mañana, ¡es tarde! Hasta Misha se levanta a las ocho o nueve. Ella se acuesta a las 7:00 p.m., pero eso no es importante."

his "Es muy importante."

show shizu basic_normal_close
with characlose

"Shizune me ignora, amordazando mis manos al tomarlas ella misma en lugar de una refutación más adecuada. La manera como ella se detiene contra mí por más tiempo de lo esperado se siente muy reconfortante."

show shizu adjust_happy_close
with charachange

ssh "El punto es que ella está despierta ahora mismo, caminando por ahí. Vamos a encontrarla."

scene bg school_courtyard at bgleft
with locationskip

"Ella corre impacientemente hacia la puerta a toda velocidad, y su entusiasmo, mientras me lleva a rastras buscando a Misha, me hace sentir más como si estuviera siguiendo a un cazador en un safari que buscando a una amiga en común."

"No tenemos que buscar mucho. Incluso muy corto, su pelo rosado se destaca. El hecho de que ella solo esté deambulando por el campus al aire libre lo hace aún más fácil. Ahora yo estoy sonando como un cazador de safari."

show shizu adjust_happy_close at tworight
with charaenter

shi "¡…!"

hi "¡Misha!"

show mishashort hips_smile at twoleft behind shizu
with charaenter

mi "¿Eh~?"

hi "Estábamos buscándote."

show shizu behind_smile_close
with charachange

ssh "Es un buen día para un picnic, deberías acompañarnos. Incluso tenemos caviar; no es esturión, por supuesto, pero es muy delicioso."

show mishashort perky_confused
with charachange


mi "¿Caviar? ¿Estupor?"

"Aparentemente al encontrar molesto el tener que explicar todo en detalle con una sola mano, Shizune se da por vencida rápidamente."

show shizu adjust_frown_close
with charachange

ssh "Huevos de pescado."

show mishashort sign_confused
with charachange

mi "¿Qué?"

show shizu behind_smile_close
with charachange

ssh "Sabe bien."

show mishashort cross_smile
with charachange

mi "Lo siento, Shicchan, creo que pasaré por hoy."

show shizu basic_angry_close
with charachange

"Cuando Misha comienza a alejarse, Shizune me entrega la bolsa, necesitando que yo la tome para que sus manos puedan estar libres."

hide shizu
with None

show shizu basic_angry_close at tworight behind mishashort
with None

show mishashort cross_smile:
    ease 1.0 center
show bg school_courtyard:
    ease 1.0 center
show shizu basic_angry_close:
    ease 1.0 xpos 0.75
with Pause(0.5)
show shizu behind_blank:
    tworight
    xpos 0.725
    ease 0.5 xpos 0.75
with charadistant

show mishashort perky_confused at Position(xpos=0.35)
show shizu behind_blank at Position(xpos=0.65)
show bg school_courtyard at Position(xpos=0.43)
with dissolvecharamove


"Tan pronto sus manos están libres, corre a toda velocidad hacia Misha, deteniéndola."

show shizu adjust_happy
with charachange

ssh "Pero hice mucha comida."

show mishashort perky_sad
with charachange

mi "Lo siento, no tengo hambre en este momento."

show shizu behind_blank
with charachange

shi "…"

show shizu behind_frown
with charachange

ssh "¿Entonces cuándo vas a tener hambre?"

show mishashort hips_frown
with charachange

mi "Shicchan, eso es imposible saberlo~."

show shizu adjust_frown
with charachange

ssh "Puedes adivinar."

"La tensión entre ellas enfurece a Shizune, y está intentando lidiar con ella tratando de desgarrarla. Pero ese enfoque no va a funcionar."

"Había pensado, y esperado, que Misha se hubiera sobrepuesto, pero supongo que ella estaba muy herida por lo que pasó."


"En ese caso, eso realmente está fuera de las manos de cualquiera. Creo que Shizune podría entender eso, en algún nivel. Si no fuera así, ella no tendría ninguna duda en absoluto."

"Sin embargo, como ella no puede hablar, he aprendido a notar su vacilación. Es muy clara; ella bien podría estar gritando."

show mishashort sign_smile
with charachange

hide mishashort
with charaexit

stop music fadeout 5.0

"Misha mueve sus manos enfrente de ella, no queriendo continuar más con la discusión, y rápidamente se escabulle. Shizune se enfurece en silencio, reacia a dejarla ir pero sin tener manera de retenerla aquí."

"Mientras la espalda de Misha se hace más pequeña en la distancia, me pregunto a dónde se dirige. ¿Shizune se está preguntando lo mismo, mientras se muerde el labio en señal de frustración?"

"Quiero tocarla en el hombro para tranquilizarla, pero me detengo, sin saber si es lo correcto."

"No porque se vea frágil, vulnerable o triste. Es lo contrario. Después de un rato, su expresión no ocultaba ninguna emoción en absoluto. Solo contemplación. De repente, ella se da la vuelta."

play music music_dreamy fadein 4.0

show shizu basic_angry at center
show bg school_courtyard at right
with dissolvecharamove

ssh "Ahora toda esta comida se va a desperdiciar."

his "Sí."

show shizu behind_sad
with charachange

ssh "Eso me pone furiosa."

"Aunque es obvio que Shizune está más herida que furiosa. La bolsa que cuelga de mi mano se siente como si estuviera llena de plomo."

show shizu behind_blank
with charachange

$ doublespeak(ssh, his, "Vamos a una cita.", "Vamos a usarla, entonces.")

show shizu adjust_blush
with charachange

shi "…"

show shizu basic_normal
with charachange

ssh "¿A dónde quieres ir?"

his "No lo sé."

show shizu behind_blank
with charachange

ssh "La azotea."

show shizu adjust_happy
with charachange

ssh "Es mi lugar favorito."

"Una sonrisa irónica aparece en su rostro, desapareciendo casi con la misma rapidez."

play ambient sfx_rooftop fadein 1.0

scene bg school_roof
show shizu behind_frown_close at center
with shorttimeskip

"En la azotea, inmediatamente destapo el caviar, ignorando una mirada burlona de Shizune todo el tiempo. Termino dejándolo en el suelo de inmediato."


his "¿Dónde están las tostadas de caviar?"

show shizu basic_normal2_close
with charachange

ssh "No hice ninguna. Como te lo dije, compré todo."

his "Pero no hay tostadas de caviar…"

show shizu adjust_frown_close
with charachange

ssh "¿Por qué eso es importante? De todos modos, no venden las tostadas de caviar solas. Eso sería estúpido."

his "Apuesto a que sí."

show shizu behind_blank_close
with charachange

ssh "Tal vez en tiendas para los excepcionalmente perezosos, pero no aquí. ¿Por qué no usas un nacho?"

his "Un nacho no es lo mismo."

show shizu basic_frown_close
with charachange

ssh "Ambos son triángulos. Deja de ser una princesa. No sabía que había una manera correcta de comer caviar, es la primera vez que oigo sobre eso."

his "No es lo mismo en absoluto."

show shizu adjust_smug_close
with charachange

"No puedo ser decadente de esta manera. Y de todos modos, ¿cómo puede no saberlo? Ella vive en una mansión enorme. Shizune, mientras tanto, aprovecha la oportunidad para sacar media lata en un solo nacho."

his "¡Oye!"

"Estoy seguro de que ni siquiera sabe bien así."

show shizu behind_smile_close
with charachange

shi "…"

"Hay mucha comida aquí para dos personas."

"Como no podemos comunicarnos entre nosotros mientras comemos, Shizune y yo tenemos mucho tiempo para sentarnos en silencio y pensar en el hecho de que Misha, la persona por la que ella hizo todo esto, no está aquí."

show shizu basic_angry_close
with charachange

ssh "Es molesto que ella no esté aquí. Ni siquiera puedo disfrutar mi comida así."

"Miro fijamente el vaso desechable a su lado, todavía medio lleno de jugo."

his "Pensé que no querías que toda esta comida se echara a perder."

show shizu adjust_frown_close
with charachange

ssh "También quería que Misha estuviera aquí. Ese era el objetivo. No pude lograr lo que quería, así que no sabe bien."

show shizu behind_blank_close
with charachange

ssh "Deberías comértela. Come más."

his "Pero quiero las cosas fritas. Te las sigues comiendo todas, aunque dices que no saben bien."

show shizu basic_normal_close
with charachange

ssh "Las cosas fritas siempre son deliciosas. Siempre hay una excepción para ellas."

his "Engordarás."

his "Creo que estás siendo muy agresiva."

show shizu behind_blank_close
with charachange

ssh "Es como te dije ayer, solo estoy tratando de animarla."

his "Sí, pero parece más como si estuvieras planeando una campaña militar."

show shizu basic_normal2_close
with charachange

ssh "Solo estoy tratando de tomarlo en serio."

show shizu behind_sad_close
with charachange

ssh "… Y esta es la única manera en que sé cómo hacerlo en serio."

show shizu basic_normal2_close
with charachange


ssh "Me siento tan impotente. Lo odio. Ni siquiera puedo gritarle, aunque quiero hacerlo. Gritar es para ocasiones serias, ¿cierto?"

his "Sí."

show shizu adjust_frown_close
with charachange

ssh "Tú deberías gritarle a Misha por mí. Puedes decirle que quiero que ella deje de estar tan deprimida. Incluso si se siente triste y sola, no es razón para estar melancólica por siempre."

his "¿Por qué no lo haces tú?"

show shizu basic_frown_close
with charachange

ssh "Ya lo hice."

show shizu behind_blank_close
with charachange

ssh "Durante un juego de dados."

show shizu basic_happy_close
with charachange

ssh "De Siete, para ser exacta. ¡Gané! ¡Cinco veces!"

"Solo ellas dos se enorgullecerían tanto de ganar juegos de completo azar."

show shizu adjust_frown_close
with charachange

ssh "Entonces, traté de hablar con ella, pero obviamente no salió tan bien."

his "Bueno, yo también. Traté y fallé."

show shizu basic_normal2_close
with charachange

ssh "Pero mi meta siempre ha sido mejorar en todo."

his "Sí, tu deseo de estar siempre adelante es realmente extraordinario."

show shizu behind_frustrated_close
with charachange

ssh "Pero también fallé…"

show shizu basic_normal2_close
with charachange

ssh "Es por eso que quiero tu ayuda."

show shizu behind_sad_close
with charachange

ssh "Ya no entiendo qué se supone que debo hacer."


"Para alguien como Shizune, quien ha interactuado con el mundo únicamente midiendo fuerzas con cada obstáculo en su camino, el entendimiento solo llega hasta allí."

$ renpy.music.set_volume(0.5, 2.0, channel="music")
$ renpy.music.set_volume(0.5, 2.0, channel="ambient")

window hide

scene bg misc_sky at Fullpan(30.0)
with locationchange

nvl clear
nvl show dissolve

n "\n\nQuiero decirle a ella que no tiene que preocuparse. Que ella es grandiosa animando a la gente, porque ella logró animarme en mi primera semana aquí."

n "En retrospectiva, debo haberme visto casi como un idiota, al estar tan amargado desde el momento en que llegué aquí. Aunque no creo que estuviera siendo poco razonable."

n "Aun teniendo meses para digerirlo, descubrir que tienes un defecto cardiaco como yo lo hice es algo difícil de lidiar. Además de eso, había tenido mucho menos tiempo para reflexionar sobre ser trasladado de repente a Yamaku."

n "\n\nPasar el festival con Shizune realmente me ayudó a salir de la rutina. Estaba feliz, lo suficiente para olvidar que todo el tiempo se había sentido como si ella me estuviera manipulando. Ahora entiendo que yo me había permitido ser manipulado."

nvl clear

n "\n\nAunque sentí como si estuviera en el fondo del mundo, todavía quería tener una vida normal de nuevo, estoy seguro, porque disfruto lo que tengo ahora. Creo que debe ser lo mismo para todos. Incluida Misha. Todos quieren a alguien allí para que los levanten y los saquen de su autocompasión."

n "Es solo que Misha siempre quiso que Shizune fuera esa persona, pero como no pueden estar juntas, creo que Misha siente que no puede aceptar la mano de Shizune. Y eso frustra a Shizune. Pero si ella pudo animar a un extraño como yo, entonces morirá intentándolo con Misha."

n "\nTambién puedo verlo en sus ojos. Aunque ella intenta tratarlo como cualquier otro problema en su vida, Shizune no puede hacer eso con la depresión de Misha. Sus procesos de pensamiento son completamente diferentes, en cierta forma más cuidadosos, en cierta forma más imprudentes y frenéticos. Ella se preocupa mucho más por eso."

nvl clear

n "\n\n\n\n\nTermino sin decir nada. En parte porque estar sentado junto a ella de esta manera, solo nosotros dos, es lo bastante placentero en sí que no quiero interrumpir el momento con una pregunta."

n "\n\nY en parte por una razón más cobarde. He comenzado a pensar que no lo eran, pero no sé si las acciones de ella en ese día podrían no haber sido una idea de último momento, o ni siquiera una casualidad, solo un conjunto de coincidencias. No sé si eso cambie algo, pero me siento incómodo pensando en ello."

$ renpy.music.set_volume(1.0, 2.0, channel="music")
$ renpy.music.set_volume(1.0, 2.0, channel="ambient")

nvl hide dissolve
nvl clear

scene bg school_roof
with locationchange

window show

stop music fadeout 5.0

"La valla detrás de mí tiembla un poco, y me giro para ver que es porque Shizune se ha quedado dormida apoyándose contra ella. Considerando que estuvo despierta toda la noche, no es de extrañar."

"¿De dónde viene toda esa motivación? No solo con respecto a Misha. Soy cínico, así que es difícil para mí aceptar que alguien puede ser tan fuerte."

"Mi primer pensamiento fue que quizás es porque ella se odia a sí misma. Es muy plausible."

"Apoyándome contra ella, me siento triste al saber que ese podría ser el caso. Pero podría ser que somos parecidos en que ambos queremos ser mejores personas."

stop ambient fadeout 2.0

scene black
with dissolve

$ suppress_window_after_timeskip = True



label es_S32:

window hide None

scene black
with dissolve

scene bg school_dormhisao
with openeye

window show

play music music_daily fadein 8.0

"Parece que comí demasiado ayer, porque desperté en la mañana sintiéndome con suficientes náuseas como para que sea un problema."

"Pero realmente no puedo posponer mi visita al pueblo para ir de compras. Así que a pesar de querer darme la vuelta y pasar el rato durmiendo, me obligo a levantarme y a vestirme."

scene bg suburb_roadcenter
with locationskip

"En algún punto entre comprar pasta de dientes y algunos otros alimentos, me termino yendo del lugar. Entonces, me siento hambriento. Después de parar para desayunar, me doy cuenta de cuánto tiempo ha pasado."

"No había esperado estar fuera por tanto tiempo. Ni siquiera estoy seguro de si me molesté en cerrar mi puerta con seguro. Realmente debería regresar."

scene bg school_dormhallway
show hideaki bored at center
with locationskip

"Cuando regreso a los dormitorios, desde la entrada veo a Hideaki parado enfrente de mi habitación."

"Se me ocurren pocas cosas más inesperadas, y no puedo dejar de pensar que podría tener un ataque cardiaco solo por la sorpresa. Afortunadamente, eso no pasa."

show hideaki normal
with charachange

"Tan pronto me ve, me saluda de manera distante, como acostumbra. Soy un poco lento en responderle, así que repite el saludo sin vacilar."

show hideaki triangle
with charachange

hh "Hola."

show hideaki normal
with charachange

hh "¿Ocurre algo?"

hi "Solo estoy sorprendido de verte aquí."

"No tan sorprendido como podría haber estado, ya que es imposible confundirlo con alguien más. Reconocería esa ropa extraña en cualquier parte. Ahora que lo pienso, realmente me he rodeado con personas de aspecto peculiar últimamente."

show hideaki confused
with charachange

"La cabeza de Hideaki cae ligeramente a un lado, muy fácilmente."

hh "¿Por qué? ¿Es raro ver que la familia de alguien venga a visitarlos?"

hi "Bueno… en realidad, sí."

show hideaki surprise_up
with charachange

show hideaki bored
with charachange

"Así que Hideaki no es un robot después de todo. De hecho, es casi como si hubiera sido tomado por sorpresa por el hecho de que incluso él puede ser tomado por sorpresa, pero se recupera rápidamente."

"Sin embargo, en ese breve momento, se ve su edad. Ese lado incómodo suyo parece el más honesto, y no me molestaría ver más de eso."

"Pero no tanto como para esforzarme en fisgonearlo. Solo Shizune sería tan entusiasta. Que mis pensamientos lleguen tan lejos es prueba de que ella se está pegando en mí."

hi "Pensaría que tendrías una razón, eso es todo."

show hideaki triangle
with charachange

hh "Hay una."

hi "¿Ves? En fin, podemos hablar mientras vamos a buscarla. Es por eso que estás aquí, ¿cierto?"

show hideaki normal_up
with charachange

hh "Shizune está en el salón del consejo estudiantil. Estaba buscándote a ti. Podríamos irnos de viaje pronto, un viaje familiar. ¿Crees que ella quisiera venir con nosotros?"

hi "Sí, no lo sé. Ella como que ha estado en pie de guerra últimamente, con muchas cosas. Y una vez que ella está concentrada en algo, no lo abandonará… Supongo que tú sabrías eso."

show hideaki closed_up
with charachange

hh "Mm."

scene bg school_courtyard
with locationskip

"Hideaki se ve mucho más cómodo caminando por el lugar que yo durante mi primera semana."

hi "Entonces, ¿esta no es tu primera vez aquí?"

"Simplemente lo suelto allí. Por supuesto, ignorar completamente el entorno podría ser algo de familia. Eso explicaría por qué Hideaki parece tan distante de Shizune. Tengo la sensación de que hay más de ello que solo su sordera."

show hideaki bored at center
with charaenter

hh "No, pero esta es la primera vez que pude caminar tanto por el lugar. Es un poco raro aquí. Me encontré con una persona que me dijo que las mujeres no son permitidas en las habitaciones."

show hideaki disapproves
with charachange

hh "Después de que le dije que no soy mujer, él me dijo que yo era engañoso, y luego me acusó de ser un asesino."

show hideaki normal
with charachange

hh "Me advirtió que él no solo era invencible, sino lo bastante fuerte como para probablemente destruir el edificio de un puñetazo, o para al menos derribar el cuadro colgado en el pasillo. Por cierto, ese cuadro en realidad está atornillado a la pared."

hi "Sí, es el tipo que vive al otro lado del pasillo enfrente de mí. Es un buen tipo."

show hideaki triangle
with charachange

hh "Ya veo. Ah, dejaste la puerta abierta. Estaba sin seguro cuando vine aquí."

"Estoy un poco molesto de que Hideaki sepa eso. La única manera en que pudo saberlo es si él hubiera abierto la puerta. Pero la sensación pasa."

hi "No importa."

hi "No tengo nada para esconder, o para que me roben."

show hideaki happy_up
with charachange

hh "Tu balón de futbol es muy bueno."

hi "Esa es una de las cosas que no importan."

show hideaki serious
with charachange

hh "Si eres futbolista, un balón de futbol es muy importante."

"Supongo que lo es. El pensamiento me hace sonreír."

show bg school_lobby
show hideaki closed_up at center
with locationskip


hh "Estoy aquí porque mi padre compró un teléfono nuevo, y quería hacérselo saber a Shizune, en caso de que ella necesite llamarlo. Pensé que tú también deberías saberlo, ya que eres su novio, ¿no es así?"

hi "Sí…"

hi "¿… Por qué?"

show hideaki bored
with charachange

hh "Por si acaso hay algún problema, o ella necesita algo."

"Eso no es lo que quise decir, pero no lo corregiré."

hi "Incluso si así fuera, ella probablemente no llamaría."

show hideaki triangle
with charachange

hh "Así es ella."

hi "Bueno, si lo sabes… ¿Pero venir hasta aquí para eso? Él podría haberla informado por correo electrónico."

show hideaki closed_up
with charachange

hh "A él no le gusta usar el correo electrónico."

hi "Eso es tan anticuado. No me digas que aún hace negocios por correo regular, o algo así."

stop music fadeout 3.0

"Silencio. Ahora es mi turno de sentirme incómodo. ¿Hideaki lo está tomando literalmente, o sí di en el blanco?"

"No. Estoy seguro de que en realidad se reduce a que él sí quiere ver a su hija y permanecer en contacto con ella. Al final, siguen siendo familia, después de todo. A pesar de que juegan a estar atacándose entre ellos."

scene bg school_council
show jigoro smug at tworight
show shizu basic_normal2 at twoleft
with locationskip

play music music_happiness fadein 2.0

"La puerta del salón del consejo estudiantil está abierta, y Hideaki y yo sorprendemos a Jigoro vociferando. Él nos ve, pero decide que no vale la pena parar sus divagaciones hacia Shizune. Esto está sacudiendo mucho mi fe en mi suposición anterior."

show jigoro angry
with charachange

hx "Cuando yo estaba en el consejo estudiantil, nuestro salón era más pequeño. También era más frío. Como trabajar en una cámara frigorífica. No como ustedes, niños mimados. Qué desperdicio. Sentados aquí en su salón gigante, sin hacer nada."

show shizu behind_frown
with charachange

shi "…"

hx "¿No son solo ustedes tres? Eso hace que tener tantos escritorios solo parezca una muestra innecesaria de una decadencia sin sentido. Horroroso. Deben usar los escritorios que necesitan, y ni uno más. Es parte de mi código."

"Puede que sea extraño de mi parte pensar así, pero… escuchar solo la mitad de una conversación es bastante extraño. Además, vaya código aquel."

"Ahora que he llegado, él cambia el tema, y comienza a hablar de la razón por la que está aquí."

show jigoro neutral
with charachange

hx "Hideaki y yo nos vamos de viaje."

show shizu basic_normal2
with charachange

shi "…"

show jigoro angry
with charachange

hx "¿Qué estás haciendo? ¿Todos los que usan lenguaje de señas murmuran mientras lo hacen?"

hi "No, pero solo soy amateur. Me ayuda a pensar. Es como la fuerza de la costumbre."

hx "Solo un amateur… increíble… Bien."

"Él se vuelve a dirigir a Shizune justo a tiempo para verla mover la cabeza de un lado a otro."

show jigoro neutral
with charachange

hx "¿Estás segura de que no vendrás con nosotros?"

show shizu adjust_frown
with charachange

"Ella repite el gesto."

show jigoro angry
with charachange

hx "Bien."

show jigoro neutral
with charachange

hx "¿Puedes decirle que me llame si necesita algo?"

hi "Sí."

hi "Pero realmente creo que enviarle un correo electrónico habría sido más fácil."

show jigoro angry
with charachange

hx "No voy a leer correos electrónicos en mi teléfono. Si ella no quiere hablar, puede llamar a Hideaki. Supongo que si me van a contactar, tú tendrías que llamarme, o esa otra chica tendría que llamarme… Hmf. En realidad, los tres pueden llamar a Hideaki."

hide jigoro
with charaexit

stop music fadeout 3.0

"Y con eso, él rápidamente se da la vuelta y se va, con Hideaki siguiéndolo. Un largo viaje, para algo que tardó cinco minutos."

"Ninguno de ellos puede expresar muy bien sus sentimientos. En el caso de Shizune, tengo que cuestionar si ella lo haría si pudiera. Explica mucho, pero ella no parece infeliz con este arreglo. Aun así, me pregunto si podría estarlo."

play sound sfx_doorclose
with Pause(1.0)
show shizu basic_normal at center
show bg school_council at bgright
with dissolvecharamove

play music music_normal fadein 3.0

"Cuando la puerta se cierra detrás de ellos, dejándonos solos a Shizune y a mí, ella deja salir un profundo suspiro que parece hacer eco en el silencio del salón."

show shizu behind_frown
with charachange

ssh "Es totalmente ridículo pedirme que vaya de viaje. El momento no podría ser peor, primero, coincide con las elecciones del consejo estudiantil. Segundo, ni siquiera he animado a Misha."

ssh "Si consideras eso, es molesto incluso tener algo más en qué pensar."

his "Sí, pero podrías estar demasiado enfocada en todas esas cosas en este momento."

show shizu adjust_frown
with charachange

"Shizune ajusta sus anteojos bruscamente."

show shizu behind_frown
with charachange

ssh "Completamente, cien por ciento correcto. En el momento en que decidí que iba a animar a Misha, todo lo demás pasó a un segundo plano, supongo."

his "Creo que tu papá podría preocuparse por ti más de lo que aparenta."

show shizu basic_normal
with charachange

ssh "Lo sé."

his "Entonces, podría ser una buena idea—"

show shizu adjust_frown
with charachange

ssh "No."

"Y de nuevo, más firmemente, como si fuera para los dos."

show shizu cross_angry
with charachange

ssh "No."

show shizu basic_frown
with charachange

ssh "Después de llegar tan lejos, no puedo tomar un descanso. Unas vacaciones serían discordantes. Sería como despertar en una vida diferente. Ayer fue como mis vacaciones. Así que ahora tenemos que ir con todo."

show shizu behind_blank
with charachange

ssh "Lo siento, pero así es como soy."

$ renpy.music.set_volume(0.5, 2.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\nRecuerdo lo que dijo Yuuko, que encontraba a Shizune valiente, de cierta manera. Creo que entiendo lo que quiso decir, y tengo que reconocerlo. Aunque también podría ser llamado imprudencia, e insensatez, y obstinación sin sentido, supongo que también podrías llamarlo “valentía”."


n "Sin embargo, puedo ver que hay un defecto fundamental en el pensamiento de Shizune que no había notado hasta ahora."

n "\nEstoy seguro de que Shizune ha reflexionado por más tiempo, y más arduamente de lo que yo podría, acerca de dónde metió la pata para crear una situación tan mala entre ella y Misha. Sin embargo, como es típico de ella, no se permitiría darle espera e inmediatamente se dispondría a arreglar el problema."

n "Esto ignora completamente una gran parte del problema: Misha en sí. Pasar de una introspección crítica a presentar a Misha como parte de una meta causa que la persona sea ignorada. Shizune ha “dicho” mucho en los últimos días, pero nada sobre cómo se siente Misha."

nvl clear

n "\nLa manera de pensar de Shizune es anormal. Pocas personas normales rechazarían a un amigo, y luego esperarían que las cosas vuelvan a ser como antes tan fácilmente. Shizune lo hace, porque ella ve la vida como, si tuviera que decirlo de una manera simple, algo que puede ser segmentado y compartimentado."

n "Misha, como todos los demás, la ve como toda una experiencia. Un viaje largo y continuo, donde un momento de angustia puede seguirte para siempre."

n "Para Shizune, un suceso es un suceso, y pocos de ellos se cruzan. La vida está compartimentada alrededor de triunfos, fracasos y decisiones, donde cada uno de ellos se presenta como su propia historia. Es por eso que la idea de unas vacaciones es discordante para ella. Es por eso que ella solo puede apreciar las emociones inmediatas de la gente."

n "En realidad, es exactamente como pensaría alguien obsesionado con vivir el momento."

n "Igualmente, Shizune puede ver a Misha como una amiga, pero dudo que ella alguna vez haya pensado en Misha como algo más hasta hace poco. O que se haya preguntado algo sobre ella. “Misha es Misha” sería suficiente para ella, aunque para Misha debe ser increíblemente agobiante."

nvl clear

n "\nShizune es solo Shizune para ella misma. Es probable que ella ni siquiera piense en las consecuencias de sus acciones a largo plazo, siempre y cuando animen la vida de los demás. Pero para Misha, estoy seguro de que eso la hacía parecer casi heroica. Como Yuuko admirando su valentía, e incluso yo mismo."

n "Y los pensamientos de Shizune sobre ese sentimiento son que fue bueno poder tocar la vida de alguien. Pero termina ahí. Es fácil cautivar; mucho más difícil cultivar. A lo siguiente. El pensar en la vida en términos de acontecimientos casi completamente aislados también tiene una tendencia a aislar a una persona."

n "Aunque ella está intentando remediarlo ahora, el punto queda: simplemente no hay manera de que Shizune pudiera haber evitado lastimar a Misha. Su inversión emocional en Shizune fue algo a lo que Shizune no podía responder, así que no lo hizo. Combinado con su personalidad, era inevitable."

n "Ellas dos me han contado todo eso, principalmente en fragmentos, durante los últimos dos meses que las he conocido."

n "\nEn medio de considerar sus diferencias, una idea comienza a tomar forma en mi mente."

$ renpy.music.set_volume(1.0, 2.0, channel="music")

nvl hide dissolve
nvl clear
window show

his "¿Estás trabajando en tu plan ahora mismo? ¿En este instante?"

his "Tu plan de animar a Misha."

show shizu basic_happy
with charachange

ssh "Por supuesto. Estaba pensando en él en todo el tiempo que me estaban gritando."

show shizu adjust_happy
with charachange

"Moviendo rápidamente sus anteojos sobre el caballete de su nariz con un aire extrañamente triunfante, ella tamborilea su dedo contra su sien."

show shizu behind_smile
with charachange


ssh "¡Es multitasking!"

stop music fadeout 4.0

"¿En serio? ¿No es más bien que eres capaz de concentrarte en algo así porque no puedes oír? Bueno, como sea. Cuando le pregunto qué piensa del mío, resulta que ambos hemos llegado a una idea similar."

scene black
with dissolve



label es_S33:

scene bg school_scienceroom at bgleft
with locationchange

play music music_pearly fadein 5.0

"Aunque me hace sentir algo intranquilo, ya que estamos hablando de un ser humano, el primer paso es arrinconar a Misha."

"Aunque para mí la situación se parece mucho a algo sacado de un drama policial, hemos llegado a esto porque hablarle normalmente está resultando ser casi imposible."

"Pero sí tenemos clases juntos. Incluso la primera clase del día."

show shizu invis:
    center
    xpos 0.75
show mishashort invis_close:
    center
    xpos 0.15
with None

show shizu behind_blank at tworight
show mishashort perky_confused_close at twoleft
show bg school_scienceroom at center
with dissolvecharamove

"Aunque toma un tiempo para que el anuncio llegue, en el instante en que escucho que hoy vamos a trabajar en grupos, Shizune y yo intentamos asegurarnos de que Misha esté en el nuestro."

hi "Sabes, creo que Mutou asigna una cantidad sospechosamente grande de trabajo en grupo y autoestudio, ¿no te parece?"

show mishashort perky_smile_close
with charachange

mi "Hm~, pero es fácil, así que está bien, ¿cierto~?"

hi "¿Sí? Sin embargo, hay otras cosas en las que he estado pensando últimamente, que podrían no estar bien."

"Misha asiente después de cada frase, y después las ignora todas."

show mishashort sign_confused_close
with charachange

mi "Pensé en ello, y~… ¡no trabajo lo suficiente cuando trabajo contigo y con Shicchan! Así que, voy a esforzarme más hoy. ¡Entonces~!, no me distraigas, Hicchan~. Tengo que estar concentrada~."

show shizu behind_frustrated
with charachange

"Esa fue una evasión irritantemente transparente. Shizune tampoco se ve muy feliz, ya que Misha no se molestó en hacer señas de nada de eso, optando por darle vueltas a un bolígrafo en sus manos."

"Por la manera temblorosa como lo hacía, estoy seguro de que fue para no hacer señas de nada inadvertidamente."

"Por la manera como se ve Misha, distraída e intranquila, dudo que sea porque quiera mantener al margen a Shizune por alguna razón maliciosa. Aunque, obviamente todavía es una manera de distanciarse de Shizune."

hi "Shizune quiere hablar contigo."

show mishashort perky_sad_close
with charachange

mi "…"

show mishashort perky_confused_close
with charachange

mi "¿No puede esperar hasta más tarde, Hicchan?"

show shizu basic_angry
with charachange

ssh "No."

hi "¿Por qué no ahora?"

show mishashort sign_confused_close
with charachange

mi "Estamos en medio de la clase~…"

"Ahora está girando un bolígrafo en cada mano. Estoy comenzando a pensar que sus señas se han convertido en una especie de tic nervioso para ella. Este no es un buen reemplazo, aunque la vista de su doble empuñadura es bastante impresionante."

hi "Entonces después de clase."

scene bg school_scienceroom at bgleft
with shorttimeskip

"Después de clase, no pierdo un segundo en volver a sacar el tema."

show shizu invis:
    center
    xpos 0.75
show mishashort invis_close:
    center
    xpos 0.15
with None

show shizu behind_frown at tworight
show mishashort perky_sad_close at twoleft
show bg school_scienceroom at center
with dissolvecharamove

"Mientras todos salen en fila del salón de clase, dejándonos a los tres solos, Misha da miradas cada vez más largas en todas las direcciones excepto hacia adelante."

hi "¿Quieres ir a comer algo?"

show mishashort hips_frown_close
with charachange

mi "¿Por qué tú y Shicchan me siguen preguntando si quiero comer algo~? ¿~Hicchan?"

hi "Porque todos vamos a la cafetería, y no hemos comido juntos en mucho tiempo. Así que, ¿por qué no?"

show mishashort perky_confused_close
with charachange


mi "¿Esto tiene que ver con el consejo estudiantil?"

show shizu behind_blank
with charachange

shi "…"

show mishashort perky_sad_close
with charachange

"Tomando la falta de respuesta de Shizune como una confesión, Misha suspira."

show mishashort hips_frown_close
with charachange

mi "Shicchan, ¿eso es en todo lo que piensas?"

stop music fadeout 5.0

hide mishashort
with charaexit

"Antes de que Shizune pueda responder, ella se va. Tengo que decir que no me quedé sintiéndome con mucha confianza después de lo que acabó de ocurrir."

show shizu behind_blank at center
show bg school_scienceroom at bgleft
with charamove

"Ninguno de nosotros estaba esperando que esto fuera sobre ruedas, pero habría sido bueno."

show shizu adjust_frown
with charachange

"Leyendo mi mente, Shizune enrolla un dedo alrededor de sus anteojos por un momento antes de hacer señas."

show shizu basic_angry
with charachange

ssh "Sé lo que estás pensando, pero no, no es que crea que ahora debamos darle algo de espacio. Te dije que no me daría por vencida tan fácilmente."

his "Sí, bueno, ahora estoy comenzando a preguntarme si no es demasiado pronto."

show shizu behind_frown
with charachange

ssh "¿Te estás echando para atrás?"

show shizu adjust_frown
with charachange

ssh "Bueno, yo no lo haré. Eso sería abandonarla."

show shizu behind_blank
with charachange

ssh "Hay una delgada línea entre ayudar a alguien y sofocarlo. Pero solo quiero que Misha se calme y deje de actuar tan extraña."

show shizu basic_normal
with charachange

ssh "Sé que puede hacerlo. Aunque ella quiera intentarlo, la gente no cambia de la noche a la mañana. Si pudieran, el mundo sería un lugar más sencillo."

his "Bueno, tú ganas."

his "Entonces supongo que esta es la parte en donde nos separamos y la buscamos."

"Aunque yo soy el único que realmente se supone que va a encontrarla."

show shizu adjust_happy
with charachange

play music music_tranquil fadein 3.0

ssh "Si me encuentro con ella primero, te llamaré a tu celular."

"Sonriendo, Shizune saca su celular y lo enciende para prepararse. Noto que tiene un número extremadamente alto de mensajes sin leer, y al ver su expresión, ella también lo nota. Al darle vueltas con la correa un par de veces, ella hace una mueca."

show shizu behind_frown
with charachange

ssh "No me gusta usar esta cosa."

show shizu basic_angry
with charachange

ssh "¿Por qué no puedo chasquear mis dedos?"

his "¿Y luego qué? No soy un perro. Y ese sonido no viaja tan lejos como una señal de teléfono."

show shizu behind_smile
with charachange

his "Te estás divirtiendo mucho con esto, ¿no es así?"

"Negando con la cabeza de lado a lado, ella continúa."

show shizu adjust_happy
with charachange

ssh "Es obvio a dónde irá. No puedes buscarla en el campus de la escuela, ella querría ir tan lejos como pueda."

show shizu behind_blank
with charachange

ssh "¿Revisar la tienda de té? Por lo general está vacía a esta hora; a Misha le encanta ir allí si tiene ganas de saltar clases, y le encantan los parfaits que tienen allí."

"“Realmente sabes mucho de ella”. Pero ella lo pensaría demasiado, y lo convertiría en algo que parecería mucho más ambiguo de lo que realmente es, así que mejor elijo asentir con la cabeza e irme, hasta que la siento agarrarse de mi manga."

show shizu basic_normal_close
with characlose

hi "¿Qué?"

"Lo digo instintivamente, olvidando que ella no puede oírme."

show shizu behind_smile_close
with charachange

ssh "Se siente bien ya no tener que hacerlo todo por mi cuenta, porque puedo confiar en ti. Estoy muy feliz."

"Me alegra oír eso. No puedo pensar en una manera de responder, y termino asintiendo con la cabeza de nuevo."

play ambient sfx_crowd_indoors fadein 2.0

scene bg school_lobby
show mishashort perky_confused:
    center
    xpos 0.6
    ypos 1.05
show crowd
with locationskip


"Saliendo del lugar, vislumbro un poco de cabello rosado detrás de la cabeza de otra chica, y mientras me dirijo hacia allí, me doy cuenta de que ese no es el camino que tomas si quieres salir de la escuela."

"Es el camino al salón del consejo estudiantil. Si yo quisiera evitar a Shizune, no iría allí."

"Entonces es extraño que Misha estuviese yendo en esa dirección. Quizás quiere aclarar las cosas con Shizune."

"En cuyo caso, tengo que preguntarme si sería una mala idea dejar que las cosas se desarrollen naturalmente después de todo, especialmente si parece que van en una buena dirección."

show mishashort invis as mishafront:
    center
    xpos 0.6
    ypos 1.05
with None

show mishashort invis at center
show mishashort hips_smile as mishafront at center
with Dissolvemove(0.7)

hide mishashort
hide mishafront
with None

show mishashort hips_smile at center
with None

"De repente, Misha se detiene y se da la vuelta, tomándome por sorpresa."

show mishashort hips_grin
with charachange

mi "¡Sorpresa~, Hicchan~! ¿Estabas buscándome? ¡Tenía un presentimiento~!"

"Iba a decir “Oye, te estaba buscando”, pero supongo que eso no es bueno ahora."

show mishashort hips_grin:
    easeout 0.7 xpos 1.0 alpha 0.0
with Pause(0.7)

"Ella ni siquiera ha terminado su frase cuando pasa por mi lado, dirigiéndose a la salida. Tengo que admitir que Misha es exasperantemente más astuta de lo que había esperado. También es sorprendentemente rápida."

stop ambient fadeout 2.0

scene bg school_courtyard
with locationskip

"Aunque es más actividad física de la que creo que debería hacer, consigo alcanzarla a medio camino de la puerta."

hi "Realmente estás siendo la mujer más grosera del mundo en este momento."

hi "¿Puedes dejar de tratar de huir por un segundo? Quiero hablar contigo."

show mishashort cross_smile at center
with charaenter

"Misha da media vuelta, viéndose ligeramente entretenida, y levanta su mano como diciéndome que continúe. Pero ahora que tengo su atención, es difícil pensar en algo apropiado para decir."

hi "¿A dónde vas ahora?"

show mishashort sign_smile
with charachange

mi "Al Shanghái~."

hi "¿Entonces puedo ir contigo?"

show mishashort perky_confused
with charachange

"Esperar a que ella responda se siente como una eternidad. Es casi como si pudiera escuchar mi reloj de pulsera contando uno a uno los segundos."

show mishashort hips_smile
with charachange

mi "Está bien, Hicchan."

stop music fadeout 3.0

"Tengo la sensación de que ella solo aceptó porque no quiere discutir más hoy."

scene bg suburb_shanghaiint
show mishashort perky_smile:
    center
    ypos 1.02
with shorttimeskip

with Pause(0.2)

play sound sfx_storebell
show mishashort perky_confused:
    ease 0.1 ypos 1.0
    ease 0.2 ypos 1.02
with Pause(0.3)

"Cuando llegamos allí, una pareja entra después de nosotros, haciendo que Misha salte ligeramente por el ruido."

show mishashort perky_smile_close at Position(ypos=1.1)
with dissolvecharamove

"Al ver que no es Shizune, se relaja de nuevo, sonriendo casi como siempre para pedirle un parfait a Yuuko, y se mete en la casilla más cercana."

hi "Saliste corriendo muy rápido. Por lo menos pudiste haber esperado para ver qué iba a decir."

show mishashort hips_frown_close
with charachange

"La reacción enojada de Misha me dice que podría ser que ella tenía miedo de lo que Shizune podría decir."

mi "¿Por qué ustedes dos están haciendo esto, Hicchan?"

hi "Porque Shizune aún quiere ser tu amiga. Supongo que para ella es un poco como lanzar un misil nuclear desde un submarino, necesitas dos llaves para hacerlo."

show mishashort perky_confused_close
with charachange

mi "…"

hi "¿Pero qué más puede hacer?"

"Ella ya no está haciendo señas automáticamente de lo que escucha o dice, y estoy seguro de que esa es la razón por la que Shizune ha estado teniendo tantos problemas con ella."

hi "Si ella tratara de hablar de ello, tú no escucharías."

show mishashort perky_sad_close
with charachange

play music music_night fadein 6.0

"La expresión culpable de Misha me dice que di en el blanco."

hi "¿Realmente odias tanto a Shizune?"

show mishashort sign_confused_close
with charachange

mi "No, Hicchan. Te lo dije."

show mishashort perky_confused_close
with charachange

"Ella responde sin inmutarse siquiera, jugando ociosamente con una cuchara."

hi "Sí, lo sé."

hi "Estoy seguro de que ella también lo sabe, pero me pregunto si podría ser más fácil si lo hicieras."

hi "La única cosa en la que realmente ha pensado durante la última semana es en cómo hacerte feliz. Ya que Shizune todavía te tiene mucho cariño. Aunque ayer, ella pensó que quizás sería más fácil para ti si tú la odiaras."

hi "Puesto que no le has dicho que la odias, Shizune piensa que ambas pueden seguir siendo amigas. Ella es así, solo piensa en extremos."

"Su parfait se está comenzando a derretir, los ingredientes se unen en pequeños ríos que me recuerdan a las raíces que crecen de un árbol siendo mostrado a través de fotografías a intervalos de tiempo."

show mishashort cross_frown_close
with charachange

mi "Eso es estúpido. Shicchan no es tan estúpida, Hicchan. No seas ridículo~."

hi "No tiene nada que ver con la inteligencia. Las personas inteligentes pueden hacer cosas estúpidas. Y de todos modos, ¿no es cierto?"

hi "Estaba aterrado la semana pasada cuando hablamos, pero al final, estaba aliviado porque parecía que las cosas podrían regresar a la normalidad."

hi "No esperaba que ustedes dos tuvieran una discusión justo después."

show mishashort perky_confused_close
with charachange

mi "No fue una discusión, Hicchan. Solo fui yo gritándole a ella."

"He notado que la voz de Misha en realidad nunca cambia de tono, solo de volumen. Es tan baja por la culpa que me cuesta creer que vino de ella."

hi "De cualquier manera, estaba feliz, porque pensé que tú y ella aún podían ser amigas. Ya que ella te necesita."

show mishashort sign_confused_close
with charachange

mi "Hm~. No, ella no me necesita, Hicchan."

hi "¿Y? ¿Cómo sabes eso? Hay muchas cosas que Shizune no…"

"¿Vocaliza? ¿Dice? ¿Conversa? Temo que si digo algo indebido, arruinará el ambiente. Por fin logro tener una conversación con ella y no quiero arruinarla. Me pregunto si esta es la primera vez que ella ha tenido una conversación honesta conmigo."

hi "Solo porque ella no te lo dijo no significa que no te quiere."

show mishashort hips_frown_close
with charachange

mi "Eso no tiene sentido…"

hi "Claro que sí. De lo contrario, ella respondería a eso."

show mishashort hips_grin_close
with charachange

mi "Guajaja~."

hi "¿No lo crees? Ella discute con todo el mundo, entonces ¿por qué no contigo? Obviamente, porque tú eres su amiga, y ella te valora. Y Shizune también está dolida."

hi "Es solo que ella es terrible mostrando sus sentimientos. Y por lo general, también lo hace de la manera equivocada. Pero todavía le agradas."

show mishashort perky_confused_close
with charachange

mi "Hicchan, ¿recuerdas cuando dije que no quería odiar a Shicchan, ni molestarla? La verdad es que~, terminé haciendo las dos cosas. Ahora es como si hubiera, como, una incomodidad entre nosotras. Es difícil de explicar."

hi "Ustedes dos son muy tercas. Estabas hablando acerca de cómo no querías distanciarte de Shizune, pero después vas a dejar que eso suceda."

hi "Y Shizune es igual de mala. Ella quiere ser tu amiga, pero te respeta demasiado como para ser tan agresiva como lo sería con cualquier otro."

"Y estoy seguro de que Misha interpreta el espacio que le da Shizune como falta de cariño."

show mishashort perky_sad_close
with charachange

mi "Ya lo arruiné, Hicchan. Sucederá de nuevo~, estoy segura. Cuando lo pienso de esa manera, no sé qué se supone que haga."

mi "Se siente como si de cualquier manera, voy a terminar empeorando las cosas. Entonces, podría ser mejor si no hiciera nada, ¿cierto~?"

hi "No seas ridícula. ¿Por qué se te ocurriría pensar eso en primer lugar? Sé más positiva."

"Quería decir, “Debería ser fácil para ti”, pero eso sería atrevido."

show mishashort hips_smile_close
with charachange

mi "Hicchan~, nunca supe que fueras tan optimista. Nunca me lo esperé."

hi "…"

show mishashort perky_smile_close
with charachange

mi "Siempre actúas tan sombrío cuando intento sorprenderte."

hi "No, esto es algo reciente. En serio. Es que ahora odio cuando la gente se da por vencida fácilmente."

show mishashort cross_grin_close
with charachange

mi "Jaja~."

show mishashort perky_smile_close
with charachange

mi "“Ahora”, ¿eh~…?"

hi "Me da rabia cuando la gente se da por vencida. Solía pensar que darse por vencido era más o menos como huir, ya que así es como la gente siempre lo describe, pero ahora que lo pienso, por lo general es más como tirar algo."

hi "Cuando huyes de algo, puedes pensar que eso todavía está ahí. De manera que, yo estaba en el hospital, y no solo quería huir de mis problemas, sino que no quería volver a pensar en ellos nunca más."

"Misha come una cucharada de su helado viscoso y gris. ¿Acaba de recordar que estaba allí ahora, o podría ser que a ella le gusta así?"

hi "En fin, mi punto es que no puedes hacer eso. La gente es demasiado sentimental como para desechar sus recuerdos de esa manera."

hi "Es imposible. Shizune no puede pensar de la vida en otra cosa que no sea ganar o perder; ¿no crees que ella desearía no tener que recordar las partes en donde pierde?"

hi "Sin embargo, no puedes elegir. Eso es como querer vivir en una burbuja. La peor parte es que, tu forma de pensar es tan inútil. Te está haciendo tan pesimista que le temes a todo."

stop music fadeout 4.0

hi "Vamos."

"Tomo su mano mientras llamo a Yuuko con la otra para pagar nuestra comida."

show mishashort sign_confused_close
with charachange

mi "¿A dónde vamos ahora?"

hi "De regreso a la escuela antes de que termine el almuerzo, pero quiero mirar unos lugares antes de eso."

scene bg school_gate:
    right
    subpixel True
    linear 30 left
with locationskip

play music music_comfort

"Aunque comienzo a sentirme cansado, incluso después de hacer lo que podría describirse aproximadamente como un trote rápido en el mejor de los casos, Misha y yo finalmente llegamos al portón de la escuela con algo más de diez minutos de sobra."

hi "Sabes, en realidad ni siquiera quería venir a esta escuela. No tuve elección. Cuando llegué a este portón, estoy seguro de que una parte de mí estaba pensando, “Qué lugar tan deprimente”."


hi "Sin embargo, no se ve deprimente en absoluto. Bueno, todavía pensaba que tenía todo planeado. Me sentí prácticamente como otra persona."

hi "Si pudiera, regresaría y me diría a mí mismo que deje de pensar que puede dar todo por perdido en un instante, y de actuar como si su vida ya hubiera terminado, y de pensar que nunca podrá divertirse de nuevo."

scene bg school_gardens:
    right
    subpixel True
    linear 30 left
with locationskip

"En el campus de la escuela todavía hay unas cuantas personas. Es la hora del almuerzo, así que es típico."

hi "Aquí es donde Shizune y tú me tuvieron ayudándoles a armar dos festivales. Fue mucho trabajo duro. Yo pensaba, “No tengo tiempo para esto”."

hi "Pero cuando miro hacia atrás, no hice tanto. Tampoco tenía nada mejor que hacer. Habría pasado el tiempo solo."

scene bg school_scienceroom:
    right
    subpixel True
    linear 30 left
with locationskip

"Después la llevo a nuestro salón de clase, que está vacío excepto por Mutou que intenta comer un emparedado antes de continuar las clases."

hi "Cada vez que pensaba en alguna de ustedes, deseaba que me dejaran en paz. Ya fuera aquí, o…"

scene bg school_lobby
with locationskip

"Dejando a Mutou con su almuerzo, nos dirigimos a la máquina expendedora cercana, y tomo una gaseosa mientras aún tengo cinco minutos para beberla."

"He pasado un periodo para el almuerzo completo con Misha; más tiempo del que Shizune y yo hemos logrado hablar con ella en días."

hi "… siguiéndome a la cafetería, o intentando arrinconarme después de la mitad de mis clases."

hi "Nunca me di cuenta de que solo hablamos como cuatro veces. En realidad todo estaba en mi cabeza. Apenas me di cuenta de ello ahora."

show mishashort hips_smile at center
with charaenter

mi "Recuerdo eso, Hicchan. Pero~, también sé dónde están todos estos lugares."

hi "Espera, déjame terminar mi visita guiada. Porque se nos está acabando el tiempo. Por cierto, ¿quieres una gaseosa?"

scene bg school_staircase2
with locationchange

"Abriéndonos paso hacia las escaleras, me alegra ya no tener que tomarla más de la mano."

hi "Te mareas en las escaleras, ¿cierto?"

show mishashort perky_sad_close at twoleft
with charaenter

mi "Sí~."

hi "Entonces, supongo que aquí estaremos bien."

show mishashort perky_sad_close:
    ease 1.0 ypos 1.2
with Pause(1.0)

"Me apoyo contra la pared mientras que Misha se sienta en los escalones, frente a mí."

hi "¿Alguna vez extrañas a las personas con las que fuiste a la escuela primaria, o a la secundaria?"

show mishashort perky_confused_close
with charachange

mi "No."

"Eso fue rápido. Ni siquiera tuvo que pensarlo. Me encuentro encogiéndome reflexivamente."

hi "Yo tenía más amigos en mi vieja escuela, pero ya no hablo más con ellos. Se siente casi como si hubiera sido en otra vida. Lo cual es triste, en realidad."

hi "A veces quiero hablar con ellos de nuevo, pero sé que no puedo. Estoy asustado, y avergonzado, cosas así. Están demasiado lejos para ir a verlos. Entonces pienso en llamarlos, pero no me sé la mayoría de sus números."

hi "Y me fui con una nota amarga. Así que, ¿por qué ellos querrían volver a verme?"

hi "Se siente como si debiera olvidarme de eso, pero igual aún pienso en ello y me arrepiento de no haberme esforzado más para permanecer en contacto, de alguna manera."

hi "Y empiezo a pensar que quizás sentirme como si debiera olvidarme de eso está mal. Sería un insulto a todas esas personas con las que me divertí y un desperdicio de todos los buenos momentos."

hi "Como dije antes, incluso si también hay algunos malos momentos, está bien si puedes revivirlos como recuerdos felices."

hi "Pero ni siquiera pensé en eso entonces. Así que fue como si despertara un día y me diera cuenta de que no tenía amigos. Me permití perder a todos mis amigos, y se sintió horrible. Realmente odiaría si Shizune y tú terminaran igual. Eso es todo."

show mishashort perky_sad_close
with charachange

mi "“Eso es todo~”."

hi "Me entristece pensar que harás lo mismo y apartarás a tu amiga. Especialmente porque no estás muy lejos de Shizune; quiero decir, hasta viven en el mismo dormitorio."

mi "Amiga, hm~…"

show mishashort perky_confused_close
with charachange

mi "¿No eres mi amigo también, Hicchan?"

hi "Sí."


hi "A pesar de que te dormiste durante ellos, los fuegos artificiales fueron muy bonitos en ese entonces, en el festival."

hi "La primera vez que veo fuegos artificiales como esos. Y la primera vez que realmente veo el cielo desde hace tiempo. Y, en realidad tampoco había mirado las estrellas antes de eso."

"Sin embargo, había hojeado un libro sobre ellas mientras estaba en el hospital, y aprendí mucho."

"Como que las estrellas no solo están ardiendo, son más como una constante cadena de explosiones, tan lejos que algunas de las estrellas que estaría viendo se habrían extinguido hace ya miles de años."

"Es que su luz solo estaría llegando a la Tierra en ese momento. Vi una maqueta que comparaba el tamaño del planeta con nuestro sol, y luego con otros soles. Japón ni siquiera era visible en la pequeña Tierra de ese libro."

hi "¿Sabes de lo que nunca me había dado cuenta?"

show mishashort perky_smile_close
with charachange

"Ella me mira con expectación."

hi "Son increíblemente brillantes."

show mishashort hips_grin_close
with charachange

mi "Ajajaja~."

hi "Es cierto."

show mishashort perky_confused_close
with charachange

mi "¿Por qué estás haciendo esto, Hicchan?"

hi "¿Haciendo qué?"

show mishashort cross_frown_close
with charachange

mi "No soy estúpida."

hi "No lo sé. Por un montón de motivos. ¿Porque eres la amiga de Shizune? ¿Y me agradaba lo unidas que eran?"

hi "Y quizás estoy tratando de decirte que todos tenemos nuestros bajones, pero darte por vencido es estúpido. En fin, parece que vale la pena."

show mishashort sign_smile_close
with charachange

mi "¿Ese es el único motivo?"

hi "Y porque eres mi amiga."

show mishashort hips_smile_close
with charachange

mi "¿Eso es todo?"

hi "¿No puedo hacer algo sin motivo?"

show mishashort hips_grin_close
with charachange

mi "Guajaja~. Puedes, puedes~, pero~, quiero saber."

hi "Bueno, ¿qué más quieres escuchar?"

play sound sfx_warningbell
stop music fadeout 3.0

"La campana suena antes de que Misha pueda responder, así que en vez de eso ella termina riendo."

scene black
with dissolve




label es_S34:

scene black
with dissolve

"Veo menos a Misha en los siguientes días. Pero no me preocupo, porque cuando la veo, cada vez se parece un poco más a la Misha de siempre."


"Una vez que está suficientemente claro que no tengo que temer a que sean mis fantasías las que influyen en mis percepciones, me comienzo a relajar de nuevo."

window hide

with Pause(1.0)

scene bg school_dormhisao
with openeye

window show

"El domingo despierto muy temprano y sintiéndome enfermo. Anoche también me fui a dormir muy temprano. Algo también anda mal con mis cortinas, y no cierran por completo."

"Debido a eso, ni siquiera puedo intentar volver a dormir. El sol me golpea en los ojos todo el tiempo. También estoy seguro de que probablemente por eso desperté tan temprano esta mañana."

play sound sfx_doorknock

"Estar así de enfermo y cansado es una tormenta perfecta de frustración. Casi me alegro cuando golpean a la puerta."

scene bg school_dormhallway
show kenji neutral at center
with locationchange

play music music_kenji fadein 0.5

"Es una persona conocida con una manzana casi completamente comida en su mano. Dando un último bocado, él intenta lanzarla a mi bote de basura y falla por completo, y se rompe en pedazos contra la pared a dos metros de altura."


"Para ser justos, la mayoría de los pedazos después sí caen en el bote de basura, pero estoy seguro de que nadie es tan descarado para tener la intención de hacer eso a propósito."

show kenji happy
with charachange

ke "¡Un lanzamiento perfecto!"

show kenji neutral
with charachange

ke "¿Qué hay, compañero de habitación?"

hi "No soy tu compañero de habitación, no vivimos en el mismo lugar."

show kenji tsun
with charachange

ke "No importa."

hi "Sí importa, por lo menos deberías saber la diferencia entre vivir en el mismo edificio y vivir en la misma habitación."

show kenji neutral
with charachange

ke "Necesito usar tu habitación."

hi "¿Para qué?"

"Lo arruiné, debí haber dicho “de ninguna manera”."

show kenji tsun
with charachange

ke "El consejo estudiantil sigue trayendo mi correo, aunque les pedí que lo echaran en mi casillero o algo así."

ke "Pero siguen echándolo bajo mi puerta, traen mi correo sin que me dé cuenta, así que hoy, estaré al acecho para atraparlas en el acto… como un detective, o un cazador de safari."

show kenji neutral
with charachange

ke "Necesito esperar en tu habitación por hoy y mirar por la pequeña mirilla o no podré atraparlas en el acto. Y quizás mañana, también."

show kenji happy
with charachange

ke "Será genial, pediremos pizza, los dos días. ¿O deberíamos pedir pizza solo un día, y algo más el otro? ¿Pero qué? ¿Y cuál día es el día de la pizza?"

hi "Hoy no. Nunca. Sabes, estoy en el consejo estudiantil. ¿Por qué no me preguntaste acerca de esto?"

"Si lo hubiera hecho, habría podido averiguar muy fácilmente y no tendría a Kenji en mi habitación. Todos ganamos, excepto que supongo que de esta manera él podría quitarme una pizza. Comienzo a pensar que quizás esa era la intención de Kenji."

"Pero… No, lo dudo. No hay manera de que él pudiera planear algo tan elaborado."

show kenji tsun
with charachange

ke "¿Tú sabes?"

hi "¿Cuándo traen el correo? Bueno, no. Ellas por lo general me entregan mi correo cuando voy al consejo estudiantil."

hi "El punto es que podría averiguarlo preguntándoles. Entonces lo sabría y podría decírtelo. Así es como la gente averigua las cosas, preguntando."

show kenji neutral
with charachange

ke "No los cavernícolas. Oh sí, no tienes una respuesta para eso, ¿verdad? Jaque mate."

hi "… Usa tu propia mirilla."

show kenji tsun
with charachange

ke "¿Qué pasa si me ven?"


hi "No pueden, así funcionan las mirillas. Es como un vidrio unidireccional."

show kenji happy
with charachange

ke "¿En serio? Bueno… De ninguna manera. Ellas esperarán que yo esté en mi habitación, de todos modos. Sentirán mi presencia y sabrán que estoy allí. Nunca esperarían que estuviera en la habitación de enfrente."

hi "Voy a ir al salón del consejo estudiantil y traeré tu correo por ti, ahora mismo."

show kenji tsun
with charachange

ke "Entonces supongo que no puedo dejarte ir."

hi "Eso es una tontería. ¿Y si tengo que ir al baño?"

show kenji neutral
with charachange

ke "Tus juegos no funcionarán conmigo."

scene bg school_dormhisao
with locationchange

"Me siento en mi escritorio y comienzo a hacer mi tarea del fin de semana."

hi "Sabes, con el tiempo vas a tener que irte, así que no puedes quedarte aquí para siempre, ni retenerme aquí para siempre. Quiero decir, esta es mi habitación para empezar."

show kenji neutral at tworight
with charaenter

ke "Sí, no creo que pueda. ¿A qué hora suele llegar el correo?"

hi "Ahora."

show kenji tsun
with charachange

ke "¿Por qué las mujeres son tan lentas?"

hi "Por cierto, ¿por qué te importa tanto el correo? ¿Estás esperando algo?"

show kenji neutral
with charachange

ke "Siempre estoy esperando algo… Pero no hoy."

hi "¿Quieres que ellas envíen algo? ¿Por lo menos envías correo?"

show kenji tsun
with charachange

ke "¡No! Así es como te atrapan. No he usado el correo desde que tenía ocho años. Envié una carta a Lego pidiéndoles que hicieran Legos de Dragon Ball."

show kenji happy
with charachange

ke "Dijeron que no podían conseguir los derechos y me dieron unos cupones. Valió totalmente la pena, pero después de eso me aseguré de pasar desapercibido."

show kenji neutral
with charachange

ke "Tú no usas el correo, ¿verdad?"

hi "Le escribí a mis padres la semana pasada."

show kenji tsun
with charachange

ke "¡Pero así es como te atrapan!"


hi "Sí, debí haberlo sabido. Quizás por eso me pusieron ese microchip el otro día."

show kenji neutral
with charachange

ke "Entonces… los rumores eran ciertos."

"Me gustaría saber de qué fábrica de rumores sacó eso."

hi "Estaba bromeando. Es una broma."

show kenji tsun
with charachange

ke "¿Una broma? Maldición. ¿Tú haciéndome bromas? Supongo que así es como se siente… que te hagan bromas. Nunca pensé que esto me pasaría. Esto es un asunto serio. Hombre, creo que no estás apreciando lo profundo de mi dilema."

ke "Es un trabajo en muchos actos. Actos complicados, con muchos jugadores. Es muy difícil, ¿bueno?"

ke "Después de que acabe voy a comerme un pescado entero, para celebrarlo. Aaaah, mierda. Pero quería una pizza. Todavía quiero pizza. ¿Puedo pedir pescado en la pizza? ¿Hacen eso ahora?"

hi "Tú vas a pagarla. Todavía no me has devuelto el dinero que te presté, y de todos modos no tengo hambre en este momento."

show kenji neutral
with charachange

ke "¿No estás de humor para pizza? Eso no es posible, hijo."

show kenji tsun
with charachange


ke "Tiene que ser pizza, de todos modos. Estoy en la etapa de la pizza de mi vida. Antes estaba en la etapa del helado, pero mi novia se seguía comiendo toda la fresa de mi napolitano. Probablemente también te pasará a ti."

"Es difícil saber si él habla en serio la mitad del tiempo; solo puedo ver su expresión cuando no tiene su nariz pegada en mi puerta."

hi "Lo dudo. Oye, sabes que sí tengo novia, ¿verdad? Y no es Iwanako. De hecho, es la presidenta del consejo estudiantil."

show kenji neutral
with charachange

ke "Ya lo sabía."

hi "¿Qué? ¿En serio?"

show kenji happy
with charachange

ke "Tengo mis fuentes."

show kenji tsun
with charachange

ke "En fin… Entonces me di cuenta de que había engordado por todo ese helado. Fue un duro despertar. Como dormir en una playa y ser golpeado por una ola que destruye tu castillo de arena."

show kenji neutral
with charachange

ke "Comencé a correr. Tenía que perder los kilos. Pero quizás… en realidad estaba huyendo de mí mismo."

play sound sfx_doorknock
stop music
show kenji rage:
    tworight
    ease 0.3 twoleft
with vpunch

"Un golpeteo repentino y continuo hace que él salte hacia atrás, lo bastante lejos para golpear la pared que estaba muy detrás de él. Aprovecho la oportunidad para acercarme a la puerta y abrirla."

play sound sfx_dooropen

scene bg school_dormhallway
show shizu behind_blank
with locationchange

ssh "Buenos días. ¿Qué tal?"

ke "Escuché que si le echas sal a la puerta no pueden entrar sin ser invitadas."

play music music_comedy fadein 4.0

scene bg school_dormhisao
show kenji neutral at center
with whip_left

hi "No voy a echar sal en mi puerta."

show kenji happy
with charachange

ke "Pero… lo estás considerando. Bien."

scene bg school_dormhallway
show shizu behind_blank
with whip_right

hi "Buenos días. ¿Estás aquí para traer el correo?"

show shizu adjust_happy
with charachange

"Asintiendo con su cabeza, Shizune agita un par de sobres entre nuestros rostros. Los tomo de sus manos, liberándolas para conversar."

show shizu basic_normal2
with charachange

ssh "¿Cómo supiste, cómo supiste?"

hi "Estabas escondiéndolo detrás de ti de una manera muy obvia."

ke "¿Escondiendo qué?"

scene bg school_dormhisao
show kenji tsun at center
with whip_left

hi "El correo."

scene bg school_dormhallway
show shizu basic_normal2
with whip_right

with Pause(0.2)

show shizu adjust_smug
with charachange

ssh "Está bien, no me estaba esforzando mucho en esconderlo en primer lugar."


hi "Eso no es propio de ti. Eres el tipo de persona que piensa que “Cualquier cosa que vale la pena es digna de esfuerzo”."

ke "¿Las chicas tomando iniciativa? ¿Y qué hay de mí? He estado usando esa frase por años. ¿Dónde está mi desfile, amigo?"

ke "Escupo oro literario y ustedes, mujeres, se lo roban y lo gastan como un vestido de verano al dos por uno. Todas son como el Picard de mi Kirk. O hasta podrían ser Janeway."

show shizu behind_frown
with charachange

ssh "No todo el tiempo. ¿Te estás burlando de mí?"

show shizu adjust_happy
with charachange

"Finalmente notando a Kenji, ella lo saluda con un gesto de su mano."

scene bg school_dormhisao
show kenji tsun at center
with whip_left

hi "Oye, Kenji, la presidenta del consejo estudiantil te está saludando."

show kenji neutral
with charachange

ke "Hola."

scene bg school_dormhallway
show shizu behind_blank at center
with whip_right

ssh "Preséntame. No tengo idea de lo que está diciendo, pero parecía confiado."

"Oh sí, nadie es mejor en decir ese tipo de cosas confiadamente."

hi "Ya lo hice. Hasta te presenté por tu título. Él es Kenji, es el chico que vive al otro lado del pasillo. Su habitación está justo detrás de ti. En fin, ¿tienes su correo también?"

show shizu adjust_happy
with charachange

ssh "Solo estoy trayendo tu correo porque estaba allí. ¡Tengo acceso temprano! Es cuestión de ubicación. Considéralo como un beneficio de estar en el consejo estudiantil."

"Eso no suena muy justo. Ella se toma muchas libertades con su posición. Al menos son pequeñas."


label es_S34a:

ssh "Nunca logré entrar a tu habitación antes. Es interesante."


label es_S34b:

ssh "Esta es la primera vez que realmente he podido ver tu habitación."

"Es una flagrante mentira, o ella lo habría dicho en señas mucho más rápido. Estoy seguro de que Shizune recuerda que no es la primera vez."


label es_S34c:

show shizu basic_frown
with charachange

ssh "¿Por qué él puede ver tu habitación y yo no? ¿Es una cosa de chicos?"

hi "No es un club secreto ser un chico."

ke "Debería serlo. Con anillos. Anillos con emblemas gigantescos. ¡Y oro!"

show shizu adjust_smug
with charachange

ssh "¿Estás seguro? ¿Estás realmente seguro? Siempre pensé que había una hermandad secreta de hombres."

ke "¿Por qué me está ignorando? Déjame contarle sobre el club de chicos. Además, ¿qué pasa con esas señales con la mano? ¿Está intentando embrujarme o algo así?"

scene bg school_dormhisao
show kenji tsun at center
with whip_left


hi "No, no te metas en esto. Tendré que traducir todo lo que le dices a ella, y no estoy seguro de poder manejarlo. Y ella probablemente lo malinterpretaría, y luego probablemente malinterpretarías la respuesta, y tendré que traducir lo que recules."

show kenji happy
with charachange


ke "¿Recular? ¿Por qué yo recularía? Me gusta mi culo."

scene bg school_dormhallway
show shizu behind_frustrated at center
with whip_right

ssh "¿Qué está diciendo?"

hi "Dice que no va a recular."

show shizu basic_normal
with charachange

ssh "¿Recular qué? Si ni siquiera he comenzado a desafiarlo."

"No me gusta la manera como puso eso. Entonces, parece que ella quiere hacerlo. ¿Pero en qué? No importa, ya que no terminaría bien."

hi "No busques peleas donde no las hay."

show shizu adjust_frown
with charachange

ssh "Nunca he conocido a tus amigos. ¿Por qué no puedo? Parece que él está… siendo apasionado."

"Supongo que con su forma de moverse frenéticamente, sería estúpido esperar que Shizune piense lo contrario. De todos modos, será mejor que cambie el tema."

"No es que probablemente funcione con ella, pero estoy seguro de que tiene que haber venido aquí por una razón, además de solo dejar mi correo."

"Si fuera algo tan simple, ella ni siquiera se habría molestado en golpear."

hi "No viniste aquí solo para darme mi correo ni para hablar con mis amigos, ¿cierto?"

play sound sfx_snap

"Shizune chasquea sus dedos fingiendo frustración. Es tan intimidantemente fuerte como siempre."

show shizu basic_normal
with charachange

ssh "Tienes razón."

show shizu behind_smile
with charachange

ssh "Vamos de nuevo a algún lugar."

hi "¿Ya tienes algún lugar en mente?"

show shizu adjust_smug
with charachange

ssh "Tienes razón otra vez. Vamos al lugar de siempre."


"Ella saca rápidamente de afuera del marco de la puerta, una bolsa de recipientes cuidadosamente envueltos. Supongo que están llenos de comida, y esta vez, no parece comprada en una tienda. Dejándola entre sus pies, ella continúa."

show shizu behind_smile
with charachange

$ doublespeak (ke, ssh, u"¿Eso es para mí?", u"Esta era la verdadera sorpresa. ¿Ves?")

show shizu adjust_smug
with charachange


ssh "Debo tener algo sobre todos los demás al final."

"Estoy de acuerdo, en la forma en que la gente normalmente lo está cuando alguien hace una declaración enfrente de ellos que dice más de lo que quisieron decir."

show kenji invis:
    center
    xpos 0.0
with None

show shizu behind_smile at tworight
show kenji tsun at twoleft
show bg school_dormhallway at bgright
with dissolvecharamove

ke "Pues, bien, si los dos van a ignorarme, me voy de aquí. Qué crueles. ¡Lo lamentarán!"

stop music fadeout 2.0

hide kenji
with charaexit

scene ev shizu_roof at shizu_roof_in
with shorttimeskip

play ambient sfx_rooftop fadein 1.0
play music music_soothing fadein 0.5

"Poco tiempo después, nos encontramos en la azotea de la escuela."

"¿Normalmente está desierta a esta hora, en un bonito día como este, un fin de semana? No, por supuesto que no. Solo puedo pensar que es debido a Shizune. No es que sacar a todos de una azotea requiera algo más que poner un cartel en la puerta."

"Los recipientes de plástico vacíos en los que Shizune había empacado nuestra comida se encuentran a mi lado. Fue otra comida tranquila, ya que sostener los palillos nos impide hablar mucho entre nosotros."

"Si bien no está soplando tan fuerte como para ser un problema, el viento es un poco fuerte hoy."

"Sopla la bolsa suelta de plástico de debajo de los recipientes vacíos, así que se mueve de un lado a otro por un momento antes de rodar sobre mis piernas y quedar atrapada en la punta del zapato de Shizune."

show ev shizu_roof_towardsangry at shizu_roof_in
with charachange

"Inmediatamente, la agarra y comienza a hacer señas, sin verse contenta de que me esté riendo de ella, aunque ella misma está tratando de no soltar una risa. Sin embargo, con la bolsa en medio, al final tiene que sentarse sobre ella para continuar."

ssh "Muy gracioso."

show ev shizu_roof_towardsnormal at shizu_roof_in
with charachange

ssh "¿Cómo estuvo?"

show ev shizu_roof2_towardsnormal at shizu_roof_in
with charachange

his "¿La comida? Tenía un sabor familiar."

show ev shizu_roof2_towardsangry at shizu_roof_in
with charachange

ssh "Significa que estuvo mala."

show ev shizu_roof_towardsangry at shizu_roof_in
with charachange

his "No, no. Recuerdo haber comido esta misma comida antes, cuando tú la hiciste."

"No exactamente la misma. El camarón frito era nuevo."

ssh "Es la única cosa que sé hacer, pero debería haber mejorado."

his "¿Cuántas veces la has hecho antes?"

show ev shizu_roof_towardsnormal at shizu_roof_in
with charachange

ssh "Esta es la segunda vez."

his "¿Que haces esta comida en particular?"

show ev shizu_roof at shizu_roof_in
with charachange

ssh "Que cocino."

show ev shizu_roof_smile at shizu_roof_in
with charachange

ssh "La próxima vez, te toca intentarlo."

show ev shizu_roof_towardsangry at shizu_roof_in
with charachange

"La manera como ella sigue tirando de la esquina de la bolsa me está molestando. Creo que sé por qué lo está haciendo."

show ev shizu_roof2_towardsangry at shizu_roof_in
with charachange

his "¿Realmente te está molestando tanto?"

show ev shizu_roof2_towardsnormal at shizu_roof_in
with charachange

ssh "Quiero empacarlos apropiadamente."

show ev shizu_roof_towardsnormal at shizu_roof_in
with charachange

his "Está bien, yo los guardaré."


"Cuando los recojo, me doy cuenta de que ella debió haber traído mucha comida para poder llenar todos estos recipientes. Ni siquiera comí mucho. Shizune debe tener un buen metabolismo para poder atiborrarse todo eso."

stop music fadeout 1.0
play sound sfx_impact

scene black
with vpunch

"Aunque solo he estado de pie por un segundo, es suficiente tiempo para tropezarme estúpidamente con mis propios pies. Apenas logrando amortiguar mi caída, termino cayendo sobre mis codos y rodillas justo al lado del regazo de Shizune."

scene bg school_roof
with locationchange

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack
with Dissolve (0.7)

"Mientras me vuelvo a levantar, con mi mano agarrando cautelosamente mi pecho, en todo lo que puedo pensar es en el dolor en mis rodillas y en cómo esa caída podría haberme matado. Siento náuseas."

"Shizune amablemente me da un empujón en mi hombro para ayudarme a erguirme, aunque la noto mirándome de manera extraña. Desafortunadamente, hasta un pequeño empujón es suficiente para tomarme por sorpresa."

show shizu basic_normal2_close:
    center
    ypos 1.1
with charaenter

ssh "¿Estás bien?"

"Asiento con la cabeza, pero no volvemos a sentarnos al lado del otro. Naturalmente, estar solo con Shizune va a involucrar mucho silencio, pero solo comienzo a notarlo ahora. La típica señal de incomodidad. De nuevo, ella es la que rompe el hielo."

show shizu behind_smile_close
with charachange

ssh "Estaba esperando que intentaras algo sucio."

hi "…"

show shizu behind_sad_close
with charachange


"Y ahora el ambiente vuelve a ser incómodo."

his "¿Cómo está Misha?"

show shizu basic_normal_close
with charachange

play music music_twinkle fadein 6.0

ssh "Misha parece más feliz ahora, de vuelta a ser la de siempre. Pensé que esta sería una buena manera de celebrar, y de agradecerte por ayudarla."

"Su mano tropieza un poco en la última palabra."

his "Piensas demasiado como una empresaria."

show shizu behind_blank_close
with charachange

ssh "No puedo evitarlo, así es como me han enseñado a hacer las cosas."

show shizu adjust_happy_close
with charachange

ssh "Estoy feliz de que preguntes por Misha. Sería más preciso decir “de vuelta a ser la verdadera Misha”. Ella solo volvería a ser la de siempre para ti."

show shizu basic_normal_close
with charachange

ssh "La Misha que conoces es completamente diferente de la que yo pienso, cuando pienso en la primera vez que nos vimos. Aunque creo que se ve mejor animada y sonriendo, así no es como ella normalmente es."

show shizu behind_blank_close
with charachange

ssh "Me pregunto si es cierto en tu caso, ¿también?"

"No respondo."

his "Bueno, si Misha está feliz, entonces no importa, si resultó al final. Tu plan funcionó."

his "La conocías tan bien como dijiste. Sabías todo lo que ella diría. Pero si tu idea era que yo hablara por ti, ¿eso no me convierte en tu marioneta? Entonces, no hice nada."

show shizu cross_angry_close
with charachange

ssh "No es cierto. Fue tu idea primero."

show shizu basic_frown_close
with charachange

ssh "Yo estaba equivocada. Tengo una manera de ver las cosas que es muy errada, ahora que lo he pensado. Estoy segura de que lo sabes. A veces, trato todo como una competencia entre yo y todos los demás. Incluso cuando no tiene sentido hacerlo."

"¿A veces?"

show shizu behind_blank_close
with charachange

ssh "Sé muy bien lo fácil que es ignorar a alguien si solo puede comunicarse contigo por señas. Debí haber pedido ayuda. Pero estaba tan segura de que podía hacerlo por mi cuenta. En realidad, fue algo valiente lo que hiciste. Aunque no te llevarás el mérito."

show shizu basic_normal_close
with charachange

ssh "Aparte de eso, realmente te has vuelto un poco admirable últimamente."

"Es extraño que ella me felicite aunque su expresión facial no haya cambiado en lo más mínimo."

show shizu adjust_frown_close
with charachange

ssh "¡Pero!"

show shizu basic_happy_close
with charachange

ssh "“La gente no cambia tan fácilmente”. Según tú. ¿Estoy en lo cierto?"

"Ella hace un guiño, claramente disfrutándolo mucho."

his "¿Misha te cuenta todo?"

show shizu behind_blank_close
with charachange

ssh "Casi todo."

his "Supongo que vas a decirme que estoy equivocado en eso, ¿no es así?"

show shizu basic_normal2_close
with charachange

ssh "Sí y no."

show shizu adjust_frown_close
with charachange

ssh "Yo fui la que le dijo eso a Misha, antes que cualquiera. Pero ella lo llevó muy lejos, y cambió el significado. No es fácil, pero ella actúa como si eso lo hiciera imposible."

show shizu basic_normal_close
with charachange

ssh "Es posible, si vas poco a poco. Estoy pensando en tratar de ser menos competitiva."

his "Pero pensé que lo disfrutabas."

show shizu behind_smile_close
with charachange

ssh "Quizás solo un poco. Es por eso que usé específicamente el “menos”."

"Ella se apoya contra la valla. Tengo cosas que quiero decirle, pero de alguna manera, no parece el momento adecuado para ello. Es una sensación que tengo. Puedo notar que ella todavía no ha terminado."

show shizu basic_normal2_close
with charachange

ssh "Mucha gente cree que me esfuerzo demasiado."

show shizu adjust_happy_close
with charachange

ssh "Bueno… Siempre he pensado que trato de esforzarme lo suficiente."



"El sonido que la valla hace cuando se presiona contra ella, y el delicado tintineo de los botones de su manga raspándose contra los enlaces, son extrañamente relajantes."

"También lo es la brisa que se levanta suavemente detrás de mí. Puedo escuchar a la gente debajo de nosotros."

show shizu basic_normal_close
with charachange

"Los ojos de Shizune se lanzan hacia abajo, y me pregunto si ella todavía piensa en lo que se podría estar perdiendo. La manera llamativa en que ella suele chasquear sus dedos prueba que tiene un entendimiento de cómo otras personas perciben el sonido."

show shizu invis_close at center
with dissolvecharamove

hide shizu
with None

"Debe ser raro, poder entenderlo tanto, pero no poder experimentarlo tú mismo. Ella comienza a caminar despacio alrededor del perímetro de la azotea, aún raspando sus botones contra la valla. No es rítmico en absoluto, aunque no por falta de esfuerzo."

show shizu invis_close at twoleft
with None

show shizu basic_normal_close at center
with dissolvecharamove

"Como que me distraigo con mis pensamientos mientras lo hace, y soy violentamente sacado de ellos cuando ella le da la vuelta completa y me da un golpecito en el hombro."

show shizu behind_blank_close
with charachange

ssh "¿Recuerdas de qué estábamos hablando?"

his "¿Cuándo? ¿Ahora? Por supuesto, acabó de suceder."

show shizu basic_angry_close
with charachange

ssh "Han pasado casi diez minutos."

show shizu adjust_frown_close
with charachange

ssh "Cuando te vi por primera vez, parecías como si estuvieras muy apegado a la idea de sentir lástima por ti mismo."

"Eso duele, aunque sea cierto."

show shizu behind_smile_close
with charachange

ssh "Lo siento, lo siento."

show shizu basic_normal_close
with charachange

ssh "Me hizo querer animarte a primera vista. Aunque tenía miedo de que fuera para nada. No podía dejar de pensar que sería difícil cambiar tu parecer."

show shizu behind_smile_close
with charachange

ssh "Pero cambiaste. Pensé que era muy sorprendente, y también que podrías ser un poco fácil de influenciar. Aun así, estaba sorprendida. Me hizo reconsiderar muchas cosas. Como… que quizás todo valía la pena al final."

his "¿Todo?"

show shizu adjust_happy_close
with charachange

stop music fadeout 4.0

ssh "—Es por eso que me gustas."

his "Ya veo."

"Es bueno saberlo finalmente."

stop ambient fadeout 2.0

scene black
with dissolve



label es_S35:

scene bg school_council_ss at right
show mishashort hips_smile_close_ss at closeleft
show shizu behind_blank_close_ss at closeright
with locationchange

play music music_ease

hi "… Y recuerden, tienen que tomarse este trabajo en serio. Muchas personas piensan que simplemente pueden holgazanear, y que no es importante. Esa es una manera peligrosa de pensar."

show mishashort cross_frown_close_ss
with charachange

mi "Sin duda~. ¡No se le puede tomar demasiado en serio~! Si no están siempre pensando en grande, pensando en positivo, y si muestran alguna señal de debilidad, la gente comenzará a pensar que son incompetentes, ¿saben~?"

show mishashort sign_confused_close_ss
with charachange

mi "Y pronto no podrán hacer nada porque su poder va a ser delegado poco a poco a otras personas, y ustedes se quedarán sin nada. Eso es lo que pasó la última vez~."

show mishashort hips_grin_close_ss
with charachange

mi "¡Entonces~! Recuerden~, puede parecer un trabajo fácil, pero pueden ocurrir muchas matanzas en este salón. Ajaja~. Y~, fuera de él. ¡También lidiar con el personal de la escuela!"

mi "Incluso tratar de obtener un reporte de presupuesto de una representante de clase puede ser una lucha a muerte~, a veces."

hi "… Sí. Es matar o morir. No hay amigos en las fosas y no tomas prisioneros. ¿… Están seguras de esto? ¿Está bien?"

show shizu basic_angry_close_ss
with charachange

ssh "Ustedes no parecen lo bastante emocionados, tengo que asegurarme de que esto se está comunicando apropiadamente. ¡Una vez más, con sentimiento!"

show aoi_keiko:
    yalign 1.0 xanchor 0.5 xpos 0.0 alpha 0.0
with None

play sound sfx_flash

show bg school_council_ss at left
show mishashort invis_close at Position(xpos=1.1)
show shizu invis_close at Position(xpos=1.6)
show aoi_keiko:
    center
    alpha 1.0
with Dissolvemove(0.5)

"Shizune retuerce sus manos como un maestro para enfatizar, intimidando visiblemente a las dos chicas de pie en posición de firmes delante de nosotros."

"Y pensar que todo esto comenzó porque una de las dos preguntó si ella no se estaba tomando su trabajo demasiado en serio."

ssh "¿¡Entienden!?"

hi "¿Entienden? Finjan que lo estoy gritando."

"Aoi" "¡Está bien, está bien! ¡Aaaaah! Este consejo estudiantil es muy raro."

"Keiko" "Sí, señor."


hi "¿“Señor”? De todas maneras, ¿a quién le están hablando?"

play sound sfx_flash

show bg school_council_ss at right
show mishashort hips_smile_close_ss at closeleft
show shizu adjust_frown_close_ss at closeright
show aoi_keiko:
    yalign 1.0 xanchor 0.5 xpos 0.0 alpha 0.0
with Dissolvemove(0.5)

ssh "¡No es raro! Tienen que pensar en él como un trabajo. Si quieren, piensen en él como si les estuvieran pagando con el derecho de usar esta gran oficina."

play sound sfx_flash

show bg school_council_ss at left
show mishashort invis_close at Position(xpos=1.1)
show shizu invis_close at Position(xpos=1.6)
show aoi_keiko:
    center
    alpha 1.0
with Dissolvemove(0.5)


hi "¿Quieren otro sermón?"

"Aoi" "Noooo…"

ssh "Pueden irse ahora."

stop music fadeout 5.0

scene bg school_council_ss
show mishashort perky_smile_ss:
    twoleft
    ypos 1.1
with shorttimeskip

"Como si nada, la orientación del consejo estudiantil de una hora de duración termina."

"Personalmente, pensé que duró cincuenta minutos más de la cuenta, y también me pareció gracioso que incluyera un recorrido por la escuela a la que todos hemos estado yendo por un tiempo, pero supongo que no dolió."

"Espero que Shizune regrese a su silla, ya que ha estado muy inquieta todo el día, pero no lo hace. Ella continúa caminando sin descanso por el salón."

show shizu invis:
    center
    xpos 1.0
with None

play music music_shizune fadein 1.0

show shizu adjust_frown_ss at tworight
with dissolvecharamove

ssh "¡Todavía tienen un largo camino por recorrer! Ahora mismo, son una burla."

show mishashort sign_confused_ss:
    twoleft
    ypos 1.1
with charachange

mi "¿Eh?"

hi "¿Qué?"

show shizu behind_frustrated_ss
with charachange

ssh "¿Creen que pueden ser el nuevo consejo estudiantil? Están tan desenfocadas. Realmente puedes ver la falta de experiencia. Este fue nuestro mejor año hasta ahora; no creo que tengan lo que se necesita para ser nuestro acto siguiente."

show shizu basic_frown_ss
with charachange

ssh "Y sé que hay más personas además de esas dos chicas. ¿Dónde están? Son como la secuela enormemente publicitada y de alto presupuesto pero mediocre y fuertemente criticada del éxito inesperado y aclamado de bajo presupuesto."

show mishashort perky_confused_ss
show shizu behind_blank_ss:
    ypos 1.1
with dissolvecharamove

"Eventualmente, ella por fin se detiene y se sienta."

hi "¿Vas a extrañarlo?"

show shizu basic_normal_ss
with charachange

ssh "Obviamente."

show mishashort perky_sad_ss
with charachange

mi "Hm~… Yo también estaría más feliz si no tuviera que irme."

show mishashort hips_smile_ss
with charachange

mi "Me gusta estar en el consejo estudiantil, aunque también pueda ser agotador."

hi "Sí, sin duda es agotador."

show mishashort hips_grin_ss
with charachange

mi "Solo porque Shicchan siempre está intentando hacer más de lo que debe~."

show shizu adjust_frown_ss
with charachange



ssh "Olvidas que si yo hiciera lo mínimo, no haríamos nada en todo el año excepto repartir folletos, recoger encuestas y planear las próximas elecciones del consejo estudiantil y así el próximo consejo estudiantil pueda pasar otro año sin hacer nada."

show shizu behind_frown_ss
with charachange

ssh "¿Pedirme que deje que eso ocurra? No sean ridículos. En un consejo estudiantil como ese, ni siquiera habría poder alguno con qué jugar."

show shizu adjust_happy_ss
with charachange

ssh "Solo estoy feliz de que aunque claramente necesito exigirles más, esas dos no están mal. Aún les falta, pero el nuevo consejo estudiantil debería estar en buenas manos."

hi "¿Cómo lo sabes?"

show shizu behind_smile_ss
with charachange

ssh "Después del festival, me preguntaron si podíamos también hacer un evento de Halloween, como una casa embrujada o algo por el estilo. También tenían un montón de otras ideas."

show shizu adjust_smug_ss
with charachange

ssh "Por supuesto, mi respuesta fue “no”. Hice que Misha les dijera que lo hicieran ellas mismas, si lo querían tanto. Por alguna razón, estaban enojadas."

show mishashort cross_laugh_ss
with charachange

mi "Ajaja~."

hi "Por supuesto que estarían enojadas si les dijeras eso."

"Y Misha entregando el mensaje no ayudaría."

show mishashort cross_smile_ss
show shizu behind_blank_ss
with charachange

ssh "Yo también estaba enojada."

show shizu basic_frown_ss
with charachange

ssh "De repente, quieren tanto. Si querían una casa embrujada, o un café estilo tradicional, o un viaje a la playa, o cualquier otra cosa cliché, ¿por qué no intentaron organizarla antes? Era como si se estuvieran aprovechando de mí."

show shizu behind_frown_ss
with charachange

ssh "Trabajé duro para organizar esos festivales, y a cambio vinieron a mí con “Eso estuvo bien, pero ¿puedes hacer esto ahora? ¿Qué tal hacer esto? Eso es lo que realmente quiero”."

show mishashort sign_smile_ss
with charachange

mi "Pero Shicchan estaba equivocada~."

show shizu basic_happy_ss
with charachange

ssh "Correcto. Ellas querían unirse al consejo estudiantil para así poder hacerlo posible. Las hice sentir celosas y las animé. Eso también puede ser una especie de motivación."

show shizu adjust_happy_ss
with charachange

ssh "El deseo de hacer algo grande se extiende, aunque sea para demostrármelo. Sin embargo, decidieron aceptar mi desafío."

show shizu behind_blank_ss
with charachange

ssh "Estoy impresionada. Bueno, por ahora. Tendría que ver cómo se desarrolla por un poco más de tiempo para saberlo con seguridad."

play sound sfx_snap

show shizu adjust_happy_ss
show mishashort perky_confused_ss:
    ease 0.1 ypos 1.05
    ease 0.1 ypos 1.1
with vpunch

"Ella chasquea sus dedos repentinamente, lo cual hace que Misha casi salte de su silla. Interesante, supongo que es imposible acostumbrarse."

show shizu basic_happy_ss
with charachange

ssh "¡Es cierto! Íbamos a hacer una fiesta para celebrar el paso de las riendas al nuevo consejo estudiantil, ¿no es así? ¿Por qué no la hacemos ahora? O por lo menos planeémosla ahora, y la hacemos mañana."

hi "Pero ni siquiera están a cargo todavía. De hecho, eso es lo primero que les dijiste: “No están a cargo todavía”. Parece prematuro."

show shizu adjust_frown_ss
with charachange

shi "…"

show shizu behind_blank_ss
with charachange

ssh "Misha, ¿tú qué piensas?"

show mishashort hips_smile_ss
with charachange

mi "Hmmm~, estoy de acuerdo, es demasiado pronto. Además~, no creo que pudiera ir de todos modos. ¡Lo siento~! De hecho, iba a irme ahora mismo."

ssh "¿Por qué no?"

show mishashort hips_grin_ss
with charachange

mi "¡Sin~ comentarios~!"

show shizu adjust_frown_ss
with charachange

ssh "Vamos, dime."

show mishashort perky_confused_ss
with charachange

mi "Bueno… ¡está bien~!"


"Bien por no ceder ante la presión, Misha."

show mishashort sign_confused_ss
with charachange

mi "Pensé en ello, y~… ¡Aunque no quisiera ir, diría que sí~! Por lo general~. Es el tipo de persona que soy. Realmente debería dejar de hacer eso, y este es un buen lugar para empezar, creo."

show mishashort perky_sad_ss
with charachange

mi "Si es una celebración para decir adiós, yo no la quiero. Sería muy triste~. Quiero hacer algo más en su lugar. Y después de todo, Hicchan, tú y Shicchan todavía estarán aquí mañana. No parece correcto."

show mishashort hips_grin_ss
with charachange

mi "Además, ¡tengo otras cosas de la escuela que tengo que hacer hoy~! No puedo dejarlas así como así."

show shizu adjust_frown_ss
with charachange

ssh "Podemos posponerla."

show mishashort hips_frown_ss
with charachange

mi "No. ¡Nada de despedidas prematuras~!"

"Ella se ve muy firme cuando dice esto."

hi "Pero, ¿no te vas a ir ahora?"

show mishashort hips_grin_ss
with charachange

mi "¿Hm~? ¡Oh, es cierto~! ¡Guajaja~!"

show mishashort perky_smile_ss at twoleft
with Dissolvemove(0.7)

show mishashort sign_smile_ss
with charachange

mi "Muy bien, además de ahora, nada de despedidas demasiado prematuras, ¿de acuerdo?"

show shizu behind_blank_ss
with charachange

ssh "Entendido."

show mishashort hips_grin_ss
with charachange

mi "¡Muy bien, hasta luego~!"

stop music fadeout 4.0

hide mishashort
with charaexit

show bg school_council_ss:
    subpixel True
    center
    parallel:
        "bg school_council_ni" with Dissolve(5.0)
    parallel:
        ease 5.0 bgleft
show shizu behind_blank_ss:
    subpixel True
    parallel:
        "shizu behind_blank" with Dissolve(5.0, alpha=True)
    parallel:
        ease 5.0 xpos 0.5
with None

"Con eso, Shizune y yo quedamos solos en el salón del consejo estudiantil."

play music music_dreamy fadein 4.0

with Pause(2.0)

"La puesta de sol cambia lentamente a noche mientras estamos sentados en silencio, ambos buscando algo que decir."

show bg school_council_ni at bgleft
show shizu adjust_frown:
    center
    subpixel False ypos 1.1
with Dissolvemove(0.5)

ssh "¿Realmente sería tan malo?"

his "Sí. No lo pensé de esa manera, pero Misha tiene razón. Las fiestas fijan un estado de ánimo, y sería uno triste. Una fiesta triste no suena muy divertida."

show shizu basic_angry
with charachange

ssh "¿Por qué sería triste?"

"¿Es una pregunta capciosa? Estoy seguro de ello. Los ojos de Shizune penetran en los míos, esperando mi respuesta con una mirada indiferente y analítica que no he visto en un tiempo, pero que de todos modos se siente familiar."

"Considero mi respuesta cuidadosamente, pero también lo que significa para ella preguntarme."

"Podría ser que Shizune la encuentre deprimente también. O podría ser que ella no entiende por qué alguien la encontraría deprimente. Ambas son igualmente plausibles."

his "Tuve un pensamiento de que cuando te gradúas, es todo. Va a ser el fin del consejo estudiantil. Estaba preguntándome si tenías la misma idea."

show shizu behind_frown
with charachange

ssh "No seas estúpido. Lo espero con ansias. Ya no seré más una estudiante, así que las expectativas van a ser completamente diferentes. Las expectativas de la gente en mí, y mis expectativas sobre todo lo demás. ¡Parece emocionante!"

show shizu adjust_frown
with charachange

ssh "En cuanto al consejo estudiantil, debería estar en manos suficientemente capaces. No tengo nada de qué estar triste."

his "No creo que estés siendo honesta. Te veías molesta por tener que dejar el consejo estudiantil hace unas semanas. Tampoco era por dejarlo a un montón de novatos, era sobre tener que dejar de hacer trabajo del consejo estudiantil en absoluto."

show shizu behind_smile
with charachange

"Inesperadamente, Shizune sonríe."

his "Así que no estás en desacuerdo."

his "Entonces no tiene sentido. ¿Por qué querrías hacer una fiesta para eso?"

show shizu basic_normal
with charachange

ssh "Estoy tratando de superarlo. Además… Las celebraciones de despedida son muy importantes. La gente dice que el primer paso es el más importante, pero seguir hasta el final y terminar limpiamente es igual de importante, ¿cierto?"

his "Supongo que eso es cierto."

show shizu adjust_smug
with charachange


ssh "En fin, no lo considero una despedida. Pero aun así es un evento. Todavía tienes que pasar por las acciones apropiadas."

show shizu behind_blank
with charachange

stop music fadeout 4.0

ssh "¿No vas a hacerlo?"

his "¿No voy a hacer qué?"

show shizu basic_normal
with charachange

ssh "Besarme, por supuesto."

his "¿Esas son “las acciones apropiadas”?"

show shizu behind_blank
with charachange

ssh "Sería normal, ¿no? Lo más natural del mundo."

"Es hora de actuar con decisión. Si no lo hago, estoy seguro de que mi corazón explotará."

show shizu adjust_blush_close
with charachange


"La beso inmediatamente, tan rápido que ni siquiera tengo tiempo de disfrutarlo. A pesar de que estaba preparada para ello, Shizune se sonroja profundamente. Siento un calor similar aumentando en mi cuello y en mis mejillas."

play music music_one fadein 4.0

scene evh shizu_undressing_clothed_stare
with whiteout

"Me acerco por otro beso, pero cuando lo hago, ella se mueve hacia atrás al mismo tiempo y pícaramente salta sobre el gabinete detrás de ella. Solos, en el silencio total del salón, solo nos miramos el uno al otro por un momento."

show evh shizu_undressing_clothed_kiss
with charachange

"Esta vez, la beso más profundamente. Sus labios se sienten ligeros y secos, y se abren un poquito. Solo soy capaz de apreciar la sensación por un momento antes de que Shizune empiece a devolverme el beso con fuerza."

"Su flequillo roza contra mis párpados cerrados mientras me dejo hundir más profundamente en el beso. Puedo sentir la forma de su cuerpo a través de su ropa, lo cual solo me hace sujetar con más fuerza a Shizune."

show evh shizu_undressing_clothed_blush
with charachange

"Se necesita un poco de esfuerzo para que los dos nos separemos del otro. Ambos estamos sonrojados, por el beso y por los pensamientos de lo que está por venir, y estoy lejos de ser el único que está respirando un poco fuerte."

"Mientras Shizune comienza a quitarme la corbata, yo empiezo a desabrochar su blusa. Me lleva un rato saber cómo hacerlo. Realmente nunca había pensado antes cómo funcionan las blusas de nuestra escuela."

"La blusa de Shizune le queda un poco estrecha, y sus brazos se atascan por un momento debido a ello."

"Me encuentro quitándosela lentamente, aunque con la manera en que ella está intentando moverse para quitársela al mismo tiempo, no es fácil. La vista es un poco cómica."

play sound sfx_rustling

show evh shizu_undressing_unclothed_closed
with charachange

"Una vez los brazos de Shizune están libres, ella se libra de su camisa, su falda cae a sus rodillas siguiéndola después de que la desengancha y se desprende de sus piernas. Lo único que la cubre ahora son su sostén y sus pantaletas."

"Su figura es voluptuosa y firme, y el color saludable de su piel contrasta con el negro de su ropa interior. Es una vista maravillosa, especialmente contra el fondo de la luz de la luna a través de la ventana."

show evh shizu_undressing_unclothed_blush
with charachange

"Ella mira mi pecho y se encarga de los botones de mi camisa uno por uno. El proceso se ralentiza enormemente por mis manos moviéndose hacia arriba y hacia abajo por sus muslos. Es un poco divertido jugar con ella así."

show evh shizu_undressing_unclothed_kiss
with charachange

"Con el tiempo, finalmente, mi camisa cae al suelo. Shizune me sorprende al acercarme rápidamente para un beso profundo sin previo aviso, pero rápidamente devuelvo el gesto."

show evh shizu_undressing_unclothed_talk
with charachange

ssh "¿Por qué eres más atrevido hoy que en la azotea?"

ssh "¿O que en tu habitación?"

"Intento pensar en una buena respuesta, pero no es fácil. ¿Cómo sería capaz de responder a eso aunque pudiera? No hay manera de hacerlo, a menos que fuera a decir que la burocracia realmente me pone de humor."

"Habiéndose deshecho de mi camisa, Shizune pasa a mi cinturón, y decido ayudarla a desabrocharlo en lugar de responder a su pregunta. No creo que sería de mucho bien a estas alturas."

scene bg school_council_ni
with locationchange

"No es difícil de quitar, y cae al suelo con un tintineo metálico. Me acerco por otro beso y comienzo a deslizar mi mano por su lado hacia arriba, pero ella de repente se tambalea hacia adelante, haciéndome tropezar hacia atrás."

"El borde rígido de la mesa detrás de mí era lo más alejado de mi mente, hasta que lo siento clavarse en mi espalda baja. Ni siquiera había notado que estaba allí. Me hace agarrar a Shizune con más fuerza mientras caemos sobre la superficie de la mesa."

label es_S35h:

show evh shizu_pushdown
with charachange

"Contengo un suspiro mientras Shizune se sostiene victoriosamente sobre mí. Ella ha ganado otra vez."

"Estoy distraído hasta que el sostén de Shizune cae sobre mí, como si hubiera caído del cielo. Termino riéndome, a pesar de lo mucho que me esfuerzo para no hacerlo, y es lo bastante contagioso como para que Shizune comience a reír también."

"Liberados de su sostén, sus senos son más grandes de lo que había pensado, aunque ya eran visiblemente grandes a través de su camisa. Ella levanta su sostén con sus dedos y lo aparta rápidamente mientras mis manos se mueven por su cuerpo."

"Sentada a horcajadas sobre mí con sus rodillas sobre la mesa, Shizune se quita su ropa interior, con mis manos moviéndose inconscientemente de sus caderas para ayudarla."

"Echo un vistazo a mi reloj. Solo han pasado unos minutos, pero pareció mucho más tiempo."

"Ella se mueve con cuidado hacia abajo, más y más cerca hasta que nuestros pechos desnudos se tocan, sus senos se sienten extraños contra la cicatriz sobre mi corazón."

window hide

show evh shizu_straddle_open
with whiteout

with Pause(7.0)

window show

"Cuando Shizune se incorpora, me siento resbalándome adentro, lentamente envuelto por sus partes mientras sus senos se levantan de mi torso. Un ataque en dos frentes, intento fríamente considerar la situación. Típico de ella."

show evh shizu_straddle_tease
with charachange

ssh "Debería detenerme ahora, y dejarte hirviendo en tu lujuria."

"Ella dice, mientras comienza a rozarse contra mí, haciéndome parpadear ante el repentino placer. Muy gracioso, Shizune. Pronto pierdo la noción de mis pensamientos."

show evh shizu_straddle_closed
with charachange

shi "… Sss."

"Shizune se muerde los labios para impedir que su voz salga. Una voz no deseada. Esto es lo más que he escuchado de ella, y se sonroja una vez se da cuenta de que la dejó escapar."

"Para ocultarlo, Shizune se impulsa contra mí con más fuerza, causando que me sacuda contra ella, empujando mi erección más profundo en ella."

"Empujo mis caderas hacia ella ante la sensación repentina de movimiento, y Shizune lucha contra mí, intentando sujetarme hacia abajo de nuevo cuando logro sacar mis brazos de debajo de mí."

show evh shizu_straddle_smile
with charachange

"En ese momento, sus caderas empujan de vuelta con mucha más fuerza en respuesta."

"El sonido de los gemidos suaves y refrenados de Shizune, y la vista de sus generosos senos moviéndose arriba y abajo cada vez que sus caderas caen contra las mías, se hacen más excitantes con el tiempo en la quietud del salón del consejo estudiantil."

shi "Mmff…"

shi "… Nn…"

"Casi no puedo soportarlo más. Las sensaciones placenteras que brotan entre mis piernas, multiplicadas por la presión del peso de Shizune encima de mí, hacen que sea difícil pensar. Mis caderas comienzan a moverse solas."

"Las manos de Shizune empujan las mías hacia abajo sobre la mesa. Cada movimiento suyo es una especie de empujón."

"La mesa debajo de nosotros se sacude bajo nuestro peso combinado. Dudo que se derrumbe, pero el ruido es realmente impresionante."

show evh shizu_straddle_come
with charachange

"No es que Shizune lo note. Su ritmo se vuelve más rápido, hasta se siente como si ella podría empujarme a través de la mesa con lo enérgica que está siendo. Sin previo aviso, sus movimientos llegan a un crescendo final."

scene bg school_council_ni
with locationchange
with vpunch

"De repente, ella se detiene, casi cayendo sobre mí con tanta velocidad, que si no se recuperaba, probablemente nos habría dejado inconscientes. La peor situación posible, si alguien llega a entrar mientras estuviéramos noqueados."

"Estoy sorprendido, pero no lo suficiente para olvidar que ambos estamos desnudos y la repentina y dolorosa interrupción que acaba de suceder."

"¿Por qué tuvo que pasar esto? ¿Fue intencional, dejarme hirviendo en mi propia lujuria? Shizune deja salir su respiración con vergüenza, dándose cuenta de ello al mismo tiempo que yo."

show shizu behind_blank_nak
with charaenter

ssh "Lo siento, me tropecé, o me resbalé, o algo así."

his "Estuve pensando, ¿la puerta está sin seguro?"

hide shizu
with charaexit

"Ella rápidamente se baja de la mesa y corre para revisar, y le pone seguro, lo quita, y lo vuelve a poner, tirando del picaporte solo para estar segura. Cuando finalmente está segura, ella hace un movimiento fuera de lugar con sus manos."

show shizu behind_smile_nak
with charaenter

ssh "¡A salvo!"

his "Me alegra que puedas tomarte las cosas tan a la ligera."

show shizu behind_frown_nak
with charachange

ssh "No lo hice a propósito. ¿Por qué no tomas la iniciativa, entonces?"

show shizu behind_smilelow_nak
with charachange

ssh "Vamos."

hide shizu
with charaexit

"Agarro a Shizune por los hombros y en cambio intento ponerla sobre la mesa. Su frente se arruga en disgusto cuando el borde de la mesa la toca en la espalda, tal como ocurrió conmigo. Ella opta por ayudarse a subirse sobre la misma."

scene evh shizu_table_smile
with dissolve

"Esta también es la primera vez que he visto a Shizune acostada y desnuda. Los contornos de su clavícula y sus senos son hermosos, y mis ojos los siguen hacia abajo hasta sus caderas bien formadas. Una figura delicada de reloj de arena."

"Paso mis manos a lo largo de la curva de su cuerpo, desde sus hombros hacia abajo."


"Lentamente me inserto en Shizune hasta el tope. Una calidez y una estrechez intensas me rodean inmediatamente, y comienzo a moverme en ella para continuar donde nos quedamos antes."

"Su cuerpo se siente tan caliente contra mi piel, cada vez que nuestras caderas se juntan con cada empujón, y en los lugares donde nos estamos sujetando el uno al otro. Siento que me quemaré con su calor corporal."

"Encima de eso, me siento más sensible ahora que antes, y me encuentro empujando a Shizune más fuerte para compensarlo."

scene evh shizu_table_normal
with charachange


"Mi mano se desliza alrededor de la curva de su muslo y con cuidado la provoco con mi mano también, casi perdiendo mi equilibrio cuando reacciona con fuerza, moviéndose bruscamente hacia arriba y hacia mi ingle y casi empujándonos a los dos al suelo."

"Moviendo mis manos hacia arriba, agarro sus prominentes senos y los acaricio como siempre he querido. Se sienten incluso más grandes de lo que parecen, y rebosan mis manos, suaves y perfectamente formados."

"Ella se retuerce debajo de mí mientras muevo mis dedos sobre sus pezones, y retuerce sus brazos alrededor de los míos en su lugar, sujetando mis dedos y acercándome más. Se siente como si estuviera luchando con ella; la llave es ineludible."

"Desde la primera vez que nuestras manos se encontraron, supongo que estábamos conectados."

"Ya sea con ella llevándome de un evento del consejo estudiantil a otro, o tomados de la mano como amantes, creo que ha sido igual, la confianza que se percibe en la manera en que ella sujeta mi mano."

"Sus manos se retuercen sobre la superficie de la mesa, y agarrándose a ella, engancha sus piernas alrededor de mi espalda, juntándonos más cerca, conectándonos aún más a fondo y atrapándome dentro de ella."

show evh shizu_table_comeopen
with charachange


"Sus paredes internas son tan calientes y apretadas, y con ella empujando contra mí, la fricción solo aumenta, enviándome más allá de mis límites."

show evh shizu_table_comeclosed
with whiteout

stop music fadeout 4.0

"Muy pronto, la sensación termina. Todo lo que puedo hacer después es permanecer dentro de ella con mis manos sujetando la mesa, por falta de energía y porque sus piernas todavía están encerrándome. Por parte de Shizune, ella sonríe casi soñando."

"La vista me hace sonreír también. Sus piernas caen lentamente, permitiéndome retirarme."

label es_S35x:

scene bg school_council_ni
with locationchange

"Exhausto, me reclino contra un escritorio e intento recuperar mi aliento antes de vestirme de nuevo."

"Noto un latido sordo y caliente en mi pecho mientras abotono mi camisa hacia arriba. Le pone un mal regusto a todo lo que acaba de pasar."

show shizu behind_smile_nak
with charaenter

ssh "Fue un golpe de suerte que Misha no pudiera estar aquí, ¿cierto?"

his "Estás de un humor inusualmente bromista hoy."

his "Me pregunto qué tenía que hacer."

show shizu behind_blank_nak
with charachange

"Shizune traza el aire perezosamente con un dedo y señala la puerta."

ssh "Ve a verlo por ti mismo."

his "¿Por qué no me lo dices?"

show shizu behind_smile_nak
with charachange

ssh "Es más interesante si lo ves por ti mismo. Ver para creer."

his "Claro. Ingenioso. Tal vez lo haga. ¿Qué hay de ti, vas a quedarte aquí todo el día? Se está haciendo tarde."

show shizu behind_blank_nak
with charachange

ssh "Se siente como mi último día como presidenta del consejo estudiantil, así que tal vez dormiré aquí esta noche. Podría ser la última oportunidad que tenga para dormir en mi escritorio, como después de un largo día tratando de cumplir un plazo."

his "Eso es raro."

his "Yo dormiré en mi cama."

ssh "Dormir sentado es una habilidad. Una muy útil."

his "Claro."

scene bg school_lobby_ni
with locationchange

"Por un momento después de salir del salón, de hecho sí considero ver lo que Misha está haciendo, solo porque Shizune lo hizo sonar tan secreto, como si ella estuviera construyendo una máquina del tiempo o algo así. Pero al final decido no hacerlo."




label es_S36:

scene bg school_courtyard_ni
with locationskip

"El aire de la noche es agradable en esta época del año. Es refrescante y un poco húmedo, pero no tan frío como para que sea incómodo estar afuera por un momento. También es lo bastante tarde para que el patio esté prácticamente desierto."

"Después de que Shizune y yo nos despedimos el uno al otro, me disponía a regresar a mi habitación en los dormitorios. Sin embargo, ni siquiera hice todo el recorrido, antes de distraerme."

"No parece una mala idea ir a ver lo que Misha está haciendo. No tengo nada mejor que hacer. No hay tarea. No hay nada que valga la pena leer. Encima de eso, simplemente quiero saber."

scene bg school_lobby_ni
with locationchange

"Esta no es la primera vez que estoy en el edificio principal después de hora, pero por lo general, es cuando estoy saliendo del lugar con Shizune y Misha después de un largo día en el consejo estudiantil. No entrando solo."

"El ambiente es tranquilo, una palabra que normalmente no usaría para describir estos pasillos. Es un poco escalofriante. Una luz comienza a parpadear adelante. Esto parece un momento de una película de terror esperando por ocurrir."

play sound sfx_rustling
with vpunch

"Al sentir una mano sobre mi hombro, me pongo tenso reflexivamente."

"No es Misha, o de lo contrario habría manos tapando mis ojos y un cantarín “adivina quién” acompañándolas. Entonces, ¿quién es? Espero que no sea Kenji, o al menos que sea alguien que conozca, o esto tomará un giro hacia lo raro."

show shizu invis_close at tworight
with None

show shizu behind_blank_close_ni at center
with dissolvecharamove

play music music_happiness fadein 4.0

"Quienquiera que sea rápidamente se aparece delante de mí. Es Shizune."

hi "¿Qué estás haciendo aquí?"

"Estoy tan aliviado que olvido decirlo en señas."

show shizu adjust_frown_close_ni
with charachange

"Shizune pone un dedo en sus labios. Supongo que aunque no puede oír, ella tiene alguna idea de lo que es el volumen, y puede notar por mi expresión que estaba hablando en voz alta. Y aparentemente, ser ruidoso no es algo bueno ahora mismo."

"Pero entonces, ¿por qué Misha es su intérprete?"

his "Ah, muy gracioso. ¿Por qué estás aquí?"

show shizu basic_normal_close_ni
with charachange

ssh "Estaba esperando a que vinieras a ver. Sabía que te aparecerías. Aunque te tomó un rato."

his "¿Estuviste esperando aquí?"

show shizu behind_blank_close_ni
with charachange

ssh "Sí, pero eso no es importante. Tenemos que ser sigilosos, si no queremos que Misha nos detecte. Dime si no estoy siendo lo bastante sigilosa, ¿bueno?"

show shizu basic_normal_close_ni
with charachange

"Con eso, Shizune comienza a andar de puntillas lentamente por el medio del pasillo. Le doy una palmadita en el hombro para llamar su atención."

his "Eso no es sigiloso."

his "¿Por qué tenemos que ser sigilosos?"

show shizu behind_frustrated_close_ni
with charachange

"Ella se niega a responder, probablemente porque hacer señas y caminar sigilosamente al mismo tiempo no parece fácil."

scene bg school_hallway3_ni
with locationskip

"Antes de que lo sepa, estamos en frente de nuestro salón de clase."

stop music fadeout 0.5
play sound sfx_snap
with vpunch

"De repente, un sonido como el chasquido de un látigo atraviesa el aire, seguido por una conocida expresión de frustración."

"Estoy seguro de que un sonido como ese no es bueno para mi corazón. Sin mencionar que todo suena casi un millón de veces más fuerte con lo silencioso que es. Viene del interior del salón, y me acerco sigilosamente a Shizune para mirar adentro."

scene ev misha_nightclass:
    center
    xpos 0.4
show ovl misha_nightclass_aperture at left
with silentwhiteout

play music music_comedy fadein 0.5

mu "¿Puedes dejar de tirar tu lápiz, por favor? ¿Cómo puedes incluso lanzar un lápiz tan ruidosamente?"

ssh "Se ve muy nervioso."

"Vaya eufemismo. Simpatizo con Mutou. Pude escuchar el bolígrafo de Misha romper la barrera del sonido incluso a través de una pared y una gruesa puerta de un salón. Probablemente le reventó los tímpanos y dejó una marca en la pared."

show ev misha_nightclass:
    ease 1.0 xpos 0.23 xanchor 0.0
show ovl misha_nightclass_aperture:
    ease 1.0 right
with None

mi "No lo estoy tirando~, cuando me pongo nerviosa, me gusta darle vueltas, pero~, entonces olvido que lo estoy sujetando, y—"

mu "No importa, en cualquier caso, no debería haber lápices revoloteando. Ya tengo suficiente de eso durante las horas regulares de la escuela, no lo necesito después de hora."

mi "¡C-claro~! Lo siento."

mu "Como sea, solo deja de tirar, o soltar, o dejar caer cosas, por favor. Los maestros también tienen trabajo."

scene bg school_hallway3_ni
show shizu behind_blank_close_ni at center
with locationchange

"Noto que Shizune está mirando la misma escena que yo. Mutou está gritando a todo pulmón, y Misha está siendo Misha."

"Puedo escucharlos razonablemente bien a través de la puerta. Pero Shizune obviamente no puede escuchar absolutamente nada. Entonces, me pregunto cómo es mirar esto para ella."

"Ella debe saber, ya que entiende lo bastante bien como para que quiera que yo lo vea también, pero tengo que preguntarme si alguna vez ella se siente como si se perdiera de algo, debiendo esforzarse mucho más para entender lo que está observando."

show shizu basic_normal_close_ni
with charachange

ssh "Parece que ella está tomando lecciones suplementarias. ¿No es así?"

his "Sí."

"Le respondo, a pesar de saber que la pregunta es completamente retórica."

show shizu behind_smile_close_ni
with charachange

ssh "Misha me dijo que quiere mucho ser maestra de lenguaje de señas en el futuro. Si puede obtener una recomendación, puede estudiar en el extranjero para ello. Es por eso que está trabajando tan duro. Sus calificaciones siempre fueron algo bajas."

his "Ahora me siento culpable. Ni siquiera he pensado en lo que voy a hacer todavía."

show shizu adjust_smug_close_ni
with charachange

ssh "¡Tampoco yo!"

"La manera animada en que lo dice en señas es muy impropia de ella, y es obviamente falsa."

show shizu basic_normal2_close_ni
with charachange

ssh "Vámonos de aquí, no queremos que nos vean. Sería un problema si nos sorprenden aquí parados como idiotas."

his "¿Adónde? ¿Al salón del consejo estudiantil?"

show shizu adjust_happy_close_ni
with charachange

stop music fadeout 3.0

show shizu invis_close at tworight
with dissolvecharamove

"Negando con la cabeza, ella entra silenciosamente al salón de clase al otro lado del pasillo."

scene bg school_room34_ni
with locationchange

his "Gran escondite."

show shizu behind_blank_ni at center
with charaenter

ssh "Estás inusualmente sarcástico, últimamente. Con la puerta cerrada es uno bueno. De todos modos, ¿no fue interesante?"

his "Sí, pero no estoy muy sorprendido."

play sound sfx_doorclose


show shizu adjust_smug_ni at Position(ypos=1.1)
with dissolvecharamove

"Cierro la puerta detrás de nosotros, haciendo que Shizune se ría silenciosamente mientras se mueve hacia una silla. Por un segundo, me deprime. Quiero oír su risa real."

show shizu behind_smile_ni
with charachange

play music music_innocence fadein 10.0

ssh "Yo lo estaba. He estado menospreciando a Misha. No pensé que ella tuviera una meta en absoluto. Pero resulta que yo estaba equivocada. Hice una suposición descuidada. Pensé que Misha estaba tan falta de metas como yo. Fui estúpida. Perdí."

show shizu basic_normal_close_ni
with charachange

"Shizune hace una pausa para hacer sonar sus nudillos, luego dobla sus manos una sobre la otra, y se inclina hacia adelante en su silla."

"En el silencio anormal del edificio, puedo oír a Mutou gritarle a Misha otra vez incluso a través de un pasillo y dos puertas."

"Los ojos de Shizune están fijos en los míos, sin parpadear detrás de los cristales resplandecientes de sus anteojos, observando mi reacción a sus palabras."

"Esto es una prueba. Su opinión de la gente rara vez está formada en cómo responden a las preguntas; es el cómo responden a las declaraciones lo que cuenta."

"En retrospectiva, tiene sentido. La incapacidad de Shizune de hablar, además de solo su personalidad en general, significa que cualquier cosa que ella “diga” es un gran compromiso de su parte. Todo."

"Por esa razón, a veces dudo que ella diga algo sin intenciones ocultas detrás de ello."

"Eso suena increíblemente paranoico. Hasta Kenji pensaría eso. Por desgracia, estoy tan inmerso pensando en ello que olvido darle una respuesta. Ella lo toma como si no hubiese una. Había un límite de tiempo invisible en esta prueba, más corto de lo usual."

show shizu adjust_smug_close_ni
with charachange

ssh "Justo como lo pensé."

his "¿Qué quieres decir?"

show shizu behind_blank_close_ni
with charachange

ssh "¿No estás de acuerdo?"

his "No realmente, no es eso. No lo entiendo."

show shizu basic_normal2_close_ni
with charachange

ssh "Quiero forzar mi voluntad en la gente."

"Qué gusto ver su sinceridad."

show shizu behind_frown_close_ni
with charachange

ssh "No me veas de esa manera rara. No es que esa fuera siempre mi intención."

show shizu basic_normal_close_ni
with charachange

ssh "Al comienzo, solo estaba aburrida. Quería ver la pasión de alguien por algo. Entonces podría intentar vencerlo. Quería poner a prueba su capacidad o sus convicciones."

show shizu adjust_frown_close_ni
with charachange

ssh "Pero fue imposible, nadie tiene ninguna pasión por nada en esta escuela. Solo quieren guardársela para ellos mismos."

show shizu behind_frustrated_close_ni
with charachange

ssh "No puedo creerlo. Es muy aburrido de esa manera. Pensé que no había manera de que estas personas monótonas pudieran ser reales. Va más allá de no querer causar problemas."

show shizu adjust_angry_close_ni
with charachange

ssh "Tenían que tener algunos intereses. Tenían que estar escondiendo algo. Quería exponerlo, y revelarlo, y sacarlo."

show shizu behind_blank_close_ni
with charachange

ssh "Una de las maneras más exitosas de hacer que la gente se abra a ti, y animarlos, es abrirte con una historia sobre ti mismo. Y luego tú los motivas cuidadosamente para que te cuenten algo sobre ellos mismos."

show shizu adjust_happy_close_ni
with charachange

ssh "Es como dar y recibir, pero con un elemento de manipulación, lo cual lo hace interesante."

show shizu behind_blank_close_ni
with charachange

ssh "Yo no puedo hacer eso. Si intento hacer que Misha hable sobre mí, por mí, me hace parecer arrogante. El mensaje tiene que pasar por un mensajero. Estoy de pie junto a Misha, diciéndole que le cuente a alguien sobre mí."

show shizu adjust_frown_close_ni
with charachange

ssh "No tienes que ser capaz de leer lenguaje de señas para ver eso. Si yo estuviera obligada a aguantar eso, también pensaría que yo era arrogante."

show shizu basic_angry_close_ni
with charachange

ssh "Estaba frustrada; no podía encontrar una manera de tener una conversación con alguien que no fuera Misha. Nadie se abría hacia mí."

show shizu behind_frown_close_ni
with charachange

ssh "Llegué a la conclusión de que no puedo hacer que la gente confíe en mí, o crea en mí. Solo puedo esperar crear cosas, y mostrarlas a las personas, y esperar que las haga felices."

ssh "O podría ser más enérgica y esperar que al final eso se le pegue a alguien."

"Supongo que ese sería yo. Se siente vagamente deprimente."

show shizu basic_normal_close_ni
with charachange

ssh "En algún momento, creo que comencé a ignorar a Misha, o a verla como menos que una persona, o algo así. La di por segura, creo que sería la mejor manera de ponerlo. Era como si ella fuera simplemente una extensión de mí misma."

show shizu behind_sad_close_ni
with charachange

ssh "Olvidé que todo el tiempo, Misha estaba allí, abriéndose a mí, y dando un ciento por ciento todos los días."

show shizu basic_angry_close_ni at center
with Dissolvemove(0.7)

ssh "No logré ver lo que estaba buscando, porque estaba a plena vista. Qué estúpido de mí. En realidad sí me volví arrogante. Es por eso que he perdido. Soy más corta de vista de lo que era en ese entonces. Fui al revés."

"Ella ahora está caminando de un lado a otro, casi taciturna, pero todavía llena de tanta energía que no puede soportar dejar de moverse."

"Si hicieras que sujetara dos cables, estoy seguro de que Shizune podría encender una bombilla. Es extraño que yo pudiera tener un pensamiento tan desenfadado mientras ella está siendo tan seria."

show shizu adjust_frown_close_ni
with charachange

ssh "Y a pesar de eso, Misha me dice que yo soy su inspiración. ¿No es ridículo? No soy el tipo de persona que pueda inspirar a otros."

show shizu behind_blank_close_ni
with charachange

ssh "Incluso si una persona que te inspira tiene defectos, puede ser aceptable. He pensado en esto. Hasta hay una hipocresía aceptable."

show shizu basic_normal2_close_ni
with charachange

ssh "Por ejemplo… Si tu héroe fuera atleta, pero tiene una conducta poco deportiva, aún podría ser respetado por su habilidad atlética, incluso si tuviera fallas como persona."

play sound sfx_snap
show shizu adjust_angry_close_ni
with charachange

ssh "Sin embargo,"

"Ella chasquea sus dedos bruscamente. Suenan como un trueno en el salón vacío, y Shizune se toma unos segundos para estirarlos. Ahora que lo pienso, esta es la ocasión en la que más ha hablado en señas."

show shizu cross_angry_close_ni
with charachange

ssh "Si alguien como yo no tiene metas, sería completamente inaceptable. Sería la peor clase de hipocresía. Y los hipócritas no merecen responsabilidades sobre nada, ni siquiera pueden manejarse a sí mismos."

"Qué increíblemente pesimista. Me enoja pensar en ello."

"Me odiaba a mí mismo hace unos meses. Así debe ser la manera como yo miraba a los demás."

"Y, curiosamente, fueron Shizune y Misha las que me convencieron de parar. Sin ellas estoy seguro de que las cosas serían muy diferentes, y no para mejor."

"Últimamente, siento como si repartiéramos nuestras miserias tanto como estamos apoyados por los demás, pero creo que eso simplemente es de esperarse al tener amigos y estar cerca de alguien."

his "Eres la líder de todos modos."

show shizu behind_frown_close_ni
with charachange

ssh "Eso es simplemente porque nadie más quiere serlo."

his "Pero eso significa que todavía lo eres, ya que las personas están poniendo su confianza en ti de todas maneras. De hecho, ¿eso no lo hace más importante?"


his "De cualquier manera, tú eres la líder, tú eres la figura de inspiración o como sea que quieras llamarlo. Eres responsable por lo que domesticas."

his "Leí eso en un libro en algún lugar."

show shizu basic_normal_close_ni
with charachange

ssh "Eso es inteligente."

"Shizune solo parece mostrar lo que siente en su rostro cuando quiere, pero no creo que esté siendo sarcástica."

show shizu adjust_frown_close_ni
with charachange

ssh "Pero yo no quiero “domesticar” a nadie."

his "Entonces ser la líder y ser admirada. Es lo mismo."

show shizu behind_frustrated_close_ni
with charachange

ssh "Nunca quise ser la líder, simplemente terminó así."

his "Eso no lo creo, todo lo que haces es tratar de agarrar más y más responsabilidad."

show shizu adjust_frown_close_ni
with charachange

ssh "Espera, espera. No iba a decirte que no lo disfruto. No me importa ser la líder, pero no me molesta. No me importa ser la mejor, pero no me molesta. Aunque tienes razón, acerca de mí queriendo responsabilidad."

show shizu basic_happy_close_ni
with charachange

ssh "Por supuesto que quiero más responsabilidad. Tener responsabilidades me hace sentir viva. Es por eso que me uní al consejo estudiantil: si no hay presión, simplemente no puedo soportarlo."

show shizu behind_blank_close_ni
with charachange

ssh "Aun así, ahora soy la líder. Siempre pensé que ser la líder significaba que das órdenes, pero en realidad es más."

show shizu adjust_frown_close_ni
with charachange

ssh "Se trata de tener una meta. Si no tengo una meta, entonces es inútil. La gente solo estaría siguiéndome para mi propio disfrute. Eso sería egoísta."

"Es un punto de vista extrañamente moral para una persona que parece amar tanto ser mejor que los demás."

show shizu basic_normal2_close_ni
with charachange

"Apoyando su barbilla sobre sus dedos entrecruzados, Shizune se ve cautivadoramente infantil mientras piensa seriamente en su problema. La expresión en su rostro es un poco cómica, porque es muy obvia, y por lo tanto, muy impropia de ella."

his "Eso viene con el trabajo. Creo que tendrías que ser una líder. No estarías satisfecha con ninguna otra cosa, te aburrirías."

show shizu basic_frown_close_ni
with charachange

"Shizune no responde, pero por su expresión molesta, creo que adiviné correctamente."

his "He estado pensando que yo también necesito algo de dirección."

show shizu adjust_happy_close_ni
with charachange

ssh "¿Te dijeron que es importante contribuir a la sociedad?"

"Qué respuesta tan inusual. Es tan inesperada que no sé cómo responder. Y también me molesta, aunque no sé por qué. Posiblemente porque no parece algo que viniera de ella."

"Así que comienzo a pensar que no es para nada el pensamiento de Shizune. Me pregunto quién le dijo eso. Bueno, probablemente fue su papá. Pero es posible que a ella se le ocurriera por su cuenta. Si es así, ¿sería porque ella no puede oír?"

his "¿Por qué dices eso?"

show shizu behind_blank_close_ni
with charachange

ssh "Porque sí."

his "Yo no lo creo."

his "Pero supongo que está bien."

show shizu basic_normal_close_ni
with charachange

ssh "Ya veo."

show shizu adjust_frown_close_ni
with charachange

ssh "No sé si sea lo mismo para mí. Lo odio."

"Creo que todos quieren un propósito. Rememorando, tiene sentido que Shizune no tenga uno. De lo contrario toda esa energía habría sido dirigida a algo."

"Ya que Shizune no tenía hacia dónde canalizarla, la lanzó en todas las direcciones. Me recuerda a un cable eléctrico caído sacudiéndose en una tormenta: furioso e incandescente, pero sin rumbo y peligroso. Tal como Shizune."

"Quiero decir que es por eso que ella siente la necesidad de convertir todo en una competencia, pero… probablemente así es ella. Tener una meta para enviar esa energía es solo el próximo nivel."

show shizu behind_blank_close_ni
with charachange

ssh "¿Qué tal esto? Podría entrar en los negocios. Mi familia está bien conectada, así que no debería ser muy difícil… Eso resulta ser algo poco ético y nepotista, ¿no es así?"

his "Un poco."

show shizu adjust_frown_close_ni
with charachange

ssh "Pero no buscaré el trabajo fácil. Trabajaré duro, hasta que esté en la mismísima cima."

ssh "Cuando tenga tanto dinero como sea posible, tanto que será como si yo no supiera qué hacer con él, pasaré al siguiente nivel. Después de sentarme sobre él por un tiempo, por supuesto, como un dragón en un cuento de hadas."

his "¿Quieres ser…?"

show shizu basic_happy_close_ni
with charachange

ssh "¡Una filántropa!"

hi "…"

show shizu adjust_smug_close_ni
with charachange

ssh "Tch tch. ¿Qué estabas pensando? ¿Que quiero ser una avara?"

show shizu behind_blank_close_ni
with charachange

ssh "Bueno, es cierto, eso es parte del plan. Pero no me subestimes ni pares allí."

stop music fadeout 8.0

"Shizune todavía se ve intranquila. Por supuesto; incluso si ella pareciera resolver su problema rápidamente, nadie puede superar sus ansiedades con tanta rapidez. Nadie puede resolver sus problemas tan fácilmente."

"Lo importante es que parece como si ella estuviera decidida a intentarlo. Todavía es difícil saber si ese impulso suyo viene de un lugar bueno o malo."

"Pero ahora tiene algo a qué aferrarse. Genuinamente puedo creer que lo tiene. Estoy feliz por ella. Y al mismo tiempo, me siento un poco frío. Yo soy el único que está atrasado. Ahora, yo soy el único sin una meta."

$ suppress_window_after_timeskip = True

scene black
with dissolve



label es_S37:

window hide None
nvl clear

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_daily fadein 0.5

scene bg school_dormhisao_bw
with dissolve

nvl show dissolve

n "\n\n\n\n\n\n\n\n\nNo ha habido más interrupciones desde esa semana."

nvl clear

n "\nPor supuesto, eso es lo que pensé la semana antes de esa. Y la claridad repentina y renovada de Shizune y Misha me ha dejado sintiéndome un poco perdido y envidioso. Pensé que no había manera de que pudiera descansar tranquilo en ese momento."

n "Pero afortunadamente, nada salió de mis preocupaciones. Entonces antes de darme cuenta, había suficiente para ocuparse en la escuela que incluso pude sacármelas de mi mente. Y aun así, todo estaba bien."

n "Estaba equivocado. Había visto las vulnerabilidades cuidadosamente escondidas de Shizune y Misha; pero todavía eran fuertes."

n "Ahora, nos vamos a graduar pronto. Me he sentido tan cómodo aquí que eso como que me agarró desprevenido. Cuando eso ocurrió, me sentí triste y no quería pensar en ello. Así que no lo hice. No hasta hace poco."

n "Hace como una semana, comencé a hacer una lista de personas de las que pensé que debería despedirme antes de la graduación. La primera regla que preparé por mi cuenta fue que no trataría de escribirlas en ningún tipo de orden especial, como del menos importante al más importante."

n "De alguna manera, terminó así de todos modos, aunque también terminó siendo una lista más corta de lo que esperaba que fuera. Kenji está en algún lugar en el medio."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

scene bg school_dormhisao
show kenji neutral at center
with locationchange

window show

ke "Dijeron que con el tiempo tendría que graduarme. Bueno, se los demostré. He vivido aquí sin pagar renta por más tiempo que el suficiente. Si tienes en cuenta el aumento del costo de la tierra, creo que podrías decir que gané al final."

show kenji happy
with charachange

ke "No, ¿sabes qué? Sí gané. La historia me reconocerá como el vencedor."

hi "¿El vencedor de qué?"

ke "Me las arreglé para permanecer fuera de la vista, y colarme a través de las grietas. Vencí al sistema."

hi "Si lo pones de esa manera, suena como si hubieras huido del sistema."

ke "A veces, correr es la forma más grande de victoria; como en los Juegos Olímpicos."

"Estoy muy cansado de discutir con él. ¿A quién engaña? Todos saben que el lanzamiento de peso es el mejor deporte olímpico, en cualquier caso."

hi "Entonces, básicamente lo que estás diciendo es que, ¿no la extrañarás?"

show kenji neutral
with charachange

ke "¿Extrañar qué?"

hi "La escuela, tonto."

show kenji tsun
with charachange

ke "No. Te lo dije, este lugar está demasiado lleno de feministas. Ya es imposible de salvar. Pero al menos podré irme antes de que alcance la masa crítica. Solo regresaré, años después, cuando construyan una estatua para honrarme."


hi "¿Aquí hacen esa reunión diez años más tarde?"

show kenji neutral
with charachange

ke "¿Cómo voy a saberlo? Probablemente. En fin, tengo que empezar a empacar ahora. Cuídate, hombre."

hi "Debiste haber empacado hace una semana, como lo hice yo."

"No es que tuviera mucho que empacar."

show kenji tsun
with charachange

ke "Así no son las cosas. Se supone que hagas todo a última hora. Los hombres son mejores haciendo todo a última hora, la última hora puede tener más productividad que, digamos, toda la semana anterior. Así es como jugamos limpio con esa mierda."

show kenji neutral
with charachange

ke "Pffff, nunca vas a entender nuestras costumbres varoniles."

hi "Tú también cuídate."

show kenji happy
with charachange

show kenji invis at right
with dissolvecharamove

play sound sfx_doorslam

hide kenji
with vpunch

"Con un saludo, él corre hacia atrás a través de la puerta, cerrándola de un golpe detrás de él con tanta fuerza que probablemente todo el dormitorio escuchó. He notado que mucha gente cierra las puertas de un golpe aquí. Tal vez sea algo local."

"“Que me cuide”. Es la primera vez que le oí decir eso. Normalmente termina nuestras conversaciones con algo como “Nos vemos” o “Te pagaré luego, hombre”. Bueno, a veces él era un poco molesto, pero lo extrañaré. Lo tacho de mi lista mentalmente."

"La lista es muy corta ahora, y una vez más descarto la noción de completarla en cualquier tipo de orden. Como dije, nunca tuve esa intención."

scene bg school_dormhallway
with locationchange

"Entonces, salgo a buscar a Shizune y Misha. Solo puedo pensar en un lugar en donde podrían estar. El salón del consejo estudiantil, por supuesto."

play ambient sfx_crowd_indoors fadein 2.0

scene bg school_lobby
show crowd
with locationskip

"Al doblar en la esquina, casi me choco con un pequeño grupo de estudiantes. Por un segundo, un sentimiento amargo aparece rápidamente en mí, ya que por lo que sé, eso podría haber sido fatal."

"Es el nuevo consejo estudiantil. No son muchos, pero son mucho más que tres. Lo cual es bueno, ya que significa que hay suficientes como para que cada uno de ellos tenga su propio título."

"Habría sido genial si pudiera haber tenido una pequeña placa de escritorio con mi nombre y mi título en ella. No creo que la hagan ahora, o si alguna vez la hicieron, desafortunadamente."

"El nuevo consejo estudiantil me rodea mientras estoy pensando. Si alguien estuviera mirando esto desde lejos, sería una vista bastante siniestra."

"Quizás han venido para finalmente vengarse de mí por llamarlos “el nuevo consejo estudiantil” todas esas veces. Solo estaba traduciendo a Shizune, pero supongo que debí haber sido menos perezoso y más discreto. No me arrepiento de nada."

"Me encuentro recibiendo las gracias por “todo lo que he hecho”."

"Me están dando las gracias. Esto debería hacerme feliz, considerando lo mucho que pensaba para mí mismo que estar en el consejo estudiantil era un trabajo completamente ingrato. Sí me hace feliz, pero no puedo disfrutarlo por completo."

$ renpy.music.set_volume(0.5, 1.0, channel="music")
$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

window hide
nvl clear
nvl show dissolve

n "\n\nMe pregunto cómo habrían resultado las cosas si nuestro consejo estudiantil hubiera sido tan grande como el que está listo para reemplazarnos."

n "Aunque solo tienen otros dos o tres miembros, es suficiente como para que ellos hayan establecido roles. No como nosotros, donde Shizune parecía ser la presidenta, pero eso era todo."

n "El nuevo consejo agradeciéndome me da una sensación extraña. Es como regresar a casa y ver que un árbol que cuidaste años atrás ha crecido. Pero siento como si no hubiera cuidado de ese árbol lo suficiente. Me pregunto qué más podría haber hecho."

n "Probablemente enfurecería a Shizune que yo me sintiera distante de lo que hice en el consejo estudiantil de esta manera, o que insinuara que no hice lo suficiente, pero es cierto. Solo la estaba siguiendo a ella."

n "\nEntonces, de alguna manera, también siento que estoy viendo el mismo árbol desde la distancia. Como si lo estuviera viendo desde la ventana de un tren mientras pasa."

$ renpy.music.set_volume(1.0, 1.0, channel="music")
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")
stop music fadeout 4.0

nvl hide dissolve
nvl clear
window show

"Me dejé enredar en estos pensamientos por mucho tiempo. Cuando me recupero, me doy cuenta de que todavía estoy de pie allí, rodeado por el nuevo consejo estudiantil."

"Hago la única cosa que puedo hacer, y me disculpo por distraerme. Luego, les devuelvo las gracias."

stop ambient fadeout 0.5

scene bg school_council
with locationchange

play music music_normal fadein 3.0

"Cuando se retiran, entro al salón del consejo estudiantil, el cual se ve mucho más desordenado, pero parece haber ganado un computador."



"Tiene sentido; recuerdo escuchar a una de las chicas con la tabla sujetapapeles hablar sobre sus planes de usar un computador para hacer todo el aburrido ingreso de datos que hace Shizune más tolerable."

"Aunque no puedo recordar cuál dijo eso. Aoi parece ser la más ambiciosa, pero por otra parte, Keiko parece más seria. Bueno, eso no importa ahora."

"No estoy solo en el salón, pero en vez de encontrar aquí a Shizune como esperaba, solo es Misha. Está sentada sobre el escritorio de Shizune, como la misma Shizune lo hace a menudo, balanceando sus piernas hacia atrás y adelante."

show mishashort invis:
    center
    ypos 1.2
with None

show mishashort hips_grin at center
with Dissolvemove(0.5)

"Cuando nuestras miradas se cruzan, ella se baja e inexplicablemente posa como un superhéroe."

mi "¡Hola, Hicchan~! ¡Estoy sorprendida de verte aquí~!"

hi "¿Qué estás haciendo?"

show mishashort cross_smile
with charachange

mi "Tú primero~."

hi "Estaba buscando a Shizune."

show mishashort cross_grin
with charachange

mi "¡Yo también~! ¡Pensé que ella estaría aquí, pero encontré a Hicchan en su lugar~!"

hi "Vaya, gracias."

show mishashort sign_smile
with charachange

mi "¡Guajaja! Bueno~, esto es bueno. En serio, en serio~. Quería hablar contigo, de todos modos~."

hi "¿Sobre qué?"

"Me tomo el tiempo para mirar un poco más alrededor del salón. Veo un hornillo. Realmente se están dando la buena vida."

show mishashort perky_sad
with charachange

mi "Quería decir que lo siento~, por supuesto~, por todos los problemas que les causé a ti y a Shicchan."

hi "No los llames “problemas”."

show mishashort sign_confused
with charachange

mi "Cierto~, cierto~."

hi "No te disculpes con Shizune."

show mishashort hips_smile
with charachange

mi "Ajaja~. Cierto~, cierto~. Pero esa no es la razón por la que estoy aquí, Hicchan. No iba a disculparme con Shicchan. Ya que estás aquí, quiero hacerte una pregunta."

show mishashort perky_confused
with charachange

mi "Hicchan, ¿qué crees que se necesitaría para que Shicchan sea feliz?"

hi "La dominación del mundo, obviamente."

show mishashort cross_laugh
with charachange

mi "¡Guajaja~!"

show mishashort hips_smile
with charachange

mi "Aunque estás bromeando, Hicchan~… No, incluso si pudiera, eso no haría feliz a Shicchan. Solo por un ratito."

show mishashort sign_smile
with charachange

mi "Hicchan, ¿alguna vez has escuchado de los artistas que rompen sus pinturas tan pronto las terminan? ¡Personas como esas realmente existen en el mundo, ¿sabes~?!"

show mishashort perky_smile
with charachange

mi "Lo recordé todo de repente. Es como Shicchan, ahora que lo pienso. Cuando Shicchan establece un reto para ella misma y lo completa, actúa como si sus habilidades ya no tuvieran significado alguno."

show mishashort perky_confused
with charachange

mi "Me pregunto~, ¿es porque ella no puede crear algo permanente?"

show mishashort perky_sad
with charachange

mi "Es como esos artistas, y cómo ellos quieren crear una obra de arte para dejar atrás~, una muy grande~, pero no pueden hacerlo. Es muy obvio cuando lo recuerdo~, pero~, no lo vi antes."

mi "Ahora, tengo miedo. Me pregunto si Shicchan alguna vez será feliz."

hi "No, no lo creo. No sobre ella alguna vez siendo feliz. Creo que estás equivocada. Shizune en realidad es feliz más a menudo de lo que había pensado."

hi "Creo que en realidad es algo sorprendente. Por lo general, las personas no piensan en ese tipo de cosas hasta que llegan a la mediana edad o están muriendo. Entonces piensan “Quiero dejar algo atrás” o “Quiero ser recordado”."

"Como yo."

"Solo que yo me adelanté un poco. Mi vida era corta, y parecía aún más corta después de mi ataque al corazón."

"No pensaba en lo que estaba dejando atrás, porque muy rápidamente pensé que no había casi nada que estuviera dejando atrás. Así que todo lo que quedaba para mí era hervir en mi propia amargura."

hi "Shizune ya quiere dejar su marca en alguna parte. Pero ella quiere hacerlo ayudando a la gente. Es por eso que las celebraciones son tan importantes para ella. Hasta quiere ser filántropa."

hi "Creo que es la mejor manera de vivir, perdurar por lo que das a los demás. Incluso si es por una razón egoísta, también está bien."

hi "Shizune ya es feliz, porque si algo sale bien, siempre estará alguien más para verlo y recordarlo. Eso es lo que la hace feliz."

"Misha suspira, con sus brazos rígidos a los lados, y sus manos tamborileando suavemente el aire."

show mishashort sign_sad
with charachange

mi "Antes, todavía pensaba… em~… que podría hacer feliz a Shizune; y que estaba en un buen lugar para hacerlo antes. Ya que yo era su intérprete, siempre podía estar con ella. Tal vez…"

show mishashort perky_confused
with charachange

mi "Y~, pensé que lo haría llegando a ser como… la sombra de Shicchan."

show mishashort perky_sad
with charachange

mi "Seguí intentándolo incluso cuando me rechazó. Se sentía como si estuviera atascada y no pudiera hacer nada más que mirar la espalda de Shicchan haciéndose más pequeña mientras seguía su camino. Estaba asustada, aunque debí haberlo aceptado."

mi "Es difícil. Tal vez podría, al menos, haber entendido a Shicchan~."

show mishashort cross_smile
with charachange

mi "Pero parece que yo estaba completamente equivocada después de todo~… Ni siquiera supe eso, ni pensé en ello… Shicchan lo llamaría una completa pérdida."

show mishashort cross_frown
with charachange

mi "Bueno~, terminé. Eso es todo, Hicchan~. ¡Pero~! Ya que tú eres el que mejor conoce a Shicchan, no puedes hacerla llorar. ¡O me enojaré~!"

show mishashort hips_smile
with charachange

mi "Voy a ir al extranjero después de esto. ¡Incluso tengo cartas de recomendación, o no creo que pudiera ir normalmente~! ¿Tal vez estudiaré y me convertiré en maestra de lenguaje de señas allá? ¡Quién sabe~!"

show mishashort hips_grin
with charachange

mi "¡Eso significa~! Que tienes que cuidar de Shicchan, ¿de acuerdo?"

stop music fadeout 8.0

"La sonrisa de Misha es tan honesta como siempre, pero ella obviamente ha cambiado. La mirada en sus ojos es la de una chica mucho más atenta. Parece ser cierto que las adversidades construyen sabiduría. Me recuerda a la mirada en los ojos de Shizune."

"Me pregunto en lo que podría haber pasado Shizune para haberse convertido en lo que es. Puedo tratar de adivinar. O tal vez ella siempre fue así. Tengo más deseos de verla, y le sugiero a Misha que deberíamos buscarla juntos."

"Por supuesto, es solo una excusa para pasar más tiempo con una amiga. Es extraño que no haya pasado mucho desde la última vez que salimos juntos, los tres, en el lapso de un día rutinario del consejo estudiantil. Sin embargo, parece que fue hace mucho."

"Pensar en el futuro puede poner ese tipo de lente sobre el pasado."

"Hablando de lentes…"

scene bg school_courtyard at bgleft
show yuuko neutral_up at center
with locationskip

play music music_ease fadein 8.0

"Afuera, Yuuko anda por allí, jugueteando con una cámara pequeña y de aspecto moderno en sus manos. Sería imperceptible si no fuera lo bastante metálica como para reflejar la luz del sol. Misha la llama a gritos. Pensé que buscábamos a Shizune."

show yuuko neutral_up at tworight
show bg school_courtyard at center
with charamove

show mishashort hips_grin at twoleft
with charaenter

mi "¡Hola~ hola~!"

show mishashort cross_smile
with charachange

mi "¿Qué estás haciendo~?"

show yuuko closedhappy_down
with charachange

yu "Solo estoy tomando fotos de todos."

show mishashort hips_grin
with charachange

mi "¡Eso es obvio~!"

"Qué incómodo. Misha, nunca olvidaré cómo me enseñaste que alguien puede guardar tantos secretos, y aun así tener una enorme falta de tacto."

hi "¿Dónde está mi foto?"

show yuuko worried_up
with charachange

yu "¿Q-quieres una copia? No… no lo sé. Bueno… Solo si prometen mantenerlo en secreto, o de lo contrario todos querrán una también."

show mishashort cross_smile
with charachange

mi "¡Eso me pasó en la escuela primaria, solo que fue con dulces~!"

show yuuko smile_up
with charachange

yu "Muy bien… Entonces les tomaré una foto a ustedes…"

hi "Ah, espera, no estoy listo. Solo estaba bromeando."

show mishashort sign_smile
with charachange


mi "¡Hicchan, haz un signo de la paz~!"

hi "No voy a hacer eso."

play sound sfx_camera
with cameraflash

"El flash de la cámara se activa, cegándome."

show mishashort perky_confused
show yuuko worried_down
with charachange

"Yuuko se protege detrás de ella, dejando salir un gemido de frustración. No se supone que enciendas el flash al aire libre."

show yuuko invis at right
with dissolvecharamove

"Ella comienza a disculparse innecesariamente, y luego se escabulle silenciosamente."

hi "Ah, espera."

show yuuko worried_up at tworight
with dissolvecharamove

yu "¿Sí?"

show mishashort sign_smile
with charachange

mi "¿Has visto a Shicchan por aquí~?"

show yuuko neutral_up
with charachange

yu "Sí… Enfrente del portón."

hi "Gracias."

"Apenas puedo decirlo antes de tener que comenzar a seguir a Misha."

play ambient sfx_crowd_outdoors fadein 3.0

scene bg school_gate
show crowd at center
show shizu behind_blank at center
with locationskip

"Afortunadamente, no por mucho tiempo. El portón está apenas a un minuto a pie desde aquí, aunque incluso eso a veces puede ser agotador para mí. Vemos a Shizune con el consejo estudiantil; probablemente le están agradeciendo también."

$ renpy.music.set_volume(0.3, 1.0, channel="ambient")

show shizu adjust_frown
with charachange

hide crowd
with charaexit

"Tan pronto ella nos ve, los ahuyenta. Lo cual es muy fácil, ya que dudo que alguno de ellos pueda entender o usar lenguaje de señas, así que no están muy tristes por irse."

"Lo que a su vez me hace preguntarme por qué le darían las gracias sin alguien que pueda hacerlo, pero es la intención lo que cuenta."

show mishashort invis at twoleft behind shizu
with None

show mishashort hips_grin:
    xpos 0.36
show shizu adjust_blush
with Dissolvemove(0.4)

show bg school_gate at bgright
show mishashort perky_smile at twoleft
show shizu behind_smile at tworight
with dissolvecharamove

"Misha inmediatamente abraza a Shizune, y luego se apoya contra el portón, al lado de ella. Yo, por otra parte, decido quedarme atrás un momento, y dejarlas hablar. Después de todo, Misha quería hablar con Shizune todo este tiempo. Puedo esperar."

show bg school_gate at right
show shizu invis:
    xpos 0.4
show mishashort invis:
    xpos 0.0
with dissolvecharamove

"Incluso me doy la vuelta, para no “espiar” su conversación."

"Termino perdiendo la noción del tiempo."

"Cuando miro mi reloj, ya han pasado diez minutos. Me pregunto si terminaron, y me doy la vuelta para encontrarlas detrás de mí."

show bg school_gate at bgright
show mishashort perky_smile at twoleft
show shizu behind_blank at tworight
with dissolvecharamove

ssh "¿En qué estás pensando?"

hi "En cosas filosóficas aburridas de las que no quiero hablar. No te preocupes, no estoy pensando demasiado en ello."

show shizu adjust_smug
with charachange

ssh "Bien. Volverte filosófico en un momento como este sería lo peor que podrías hacer."

hi "Sí. Solo quiero quedarme aquí por un momento. Es relajante."

show mishashort hips_grin
with charachange

mi "¡Guajaja~! Fue~ una semana ocupada."

hi "No realmente, no para mí."

$ renpy.music.set_volume(0.5, 1.0, channel="music")
$ renpy.music.set_volume(0.1, 1.0, channel="ambient")

window hide
nvl clear
nvl show dissolve

n "\n\n\n\nSé que ellas debieron haber estado ocupadas. Pero creo que sé lo que quiero hacer ahora, y cuando lo descubrí, no me sentí particularmente entusiasmado, o ansioso."

n "Es lo contrario. Me siento en paz por primera vez en mucho tiempo, y quiero disfrutar ese sentimiento un poco más."

n "\nCreo que quiero enseñar aquí."

n "\nTan pronto pensé esto, un camino largo y serpenteante apareció en mi mente. Un camino incierto, que me trae de vuelta aquí."

nvl clear

n "\n\n\n\nMe pregunto si podré en el futuro conocer a alguien como yo. Alguien lleno de amargura."

n "Quiero hablarle a esa persona, ya que no puedo hablar conmigo mismo. Quiero decirle que la vida es muy corta; algo que no pudieron decirme, sino mostrarme. Quiero hacerlo sin lástima."

n "Si hubieran sentido lástima por mí, estoy seguro de que solo habría muerto un poco más. Cuando pienso en esa primera semana, todavía pienso en lo bien que transcurrió. Tan bien que solo podría ser llamada el resultado de la amabilidad. Siento que quiero mostrarle a los demás la misma amabilidad."

n "\nY también quiero seguir persiguiendo a Shizune."

$ renpy.music.set_volume(1.0, 1.0, channel="music")
$ renpy.music.set_volume(0.3, 1.0, channel="ambient")

nvl hide dissolve
nvl clear

show mishashort perky_smile
with charachange

window show

mi "¿Qué quería el nuevo consejo estudiantil, Shicchan~?"

"Es difícil soñar despierto cuando tienes que lidiar con la voz de Misha."

hi "No sabía que tenían a alguien que supiera lenguaje de señas."

show shizu behind_smile
with charachange

ssh "No lo tienen. Creo que lo más probable es que solo haya sido una despedida, así que lo aprecio, aunque no pudiera decírselo a ellos."

show shizu basic_normal
with charachange

ssh "¿Cómo supieron ustedes que yo estaba aquí?"

hi "¿Se supone que es un secreto? En fin, se lo preguntamos a Yuuko. ¿Ella también te tomó una foto a ti?"

show shizu behind_blank
with charachange

ssh "Sí, sin preguntarme primero. Pero ya que es raro que Yuuko haga algo sin pensarlo, lo pasaré por alto."

play sound sfx_snap
show shizu basic_sparkle
with charachange

"Ella chasquea sus dedos, más porque creo que le gusta, que por el descubrimiento de una idea."

show shizu behind_smile
with charachange

ssh "Deberíamos tomarnos una foto de los tres."

show shizu adjust_happy
with charachange

ssh "Todavía no nos hemos tomado una foto del consejo estudiantil. Ahora es la oportunidad perfecta."

show shizu basic_normal
with charachange

ssh "Pero, si tengo que mirar esa foto dentro de un año, no quiero que nosotros estemos mirando de frente a la cámara."

mi "¿Hm~? ¿Qué significa eso, Shicchan?"

show shizu adjust_frown
with charachange

ssh "Se supone que las fotografías capturan el momento, ¿no es así? Sin duda. No son retratos. Simplemente estar allí parados sería tan rígido. Ni siquiera capturaría cómo me siento."

show shizu behind_smile
with charachange

ssh "Siento que nos veremos de nuevo. Entonces, esta no es una ocasión para tomar una foto tan seria. Debería ser una foto que diga “hasta luego”; no es gran cosa. Debería ser algo más… festivo."

hi "Oh, vaya."

show shizu basic_happy
with charachange


ssh "Como esto. Síganme."

show shizu adjust_smug
with charachange

show shizu behind_smile
with charachange

"Shizune posa como un mosquetero, tan rápidamente que estoy seguro de que hasta ella sabe que es tonto."

show mishashort cross_laugh
with charachange

mi "¡Ajajaja~!"

hi "¿Realmente tenemos que hacer… una pose tan cursi?"

show shizu adjust_happy
with charachange

ssh "No puedo pensar en una pose mejor. ¡Misha, ve a buscar a Yuuko!"

show mishashort sign_smile
with charachange


mi "A mí tampoco me gusta esta pose, pero creo que es algo bonita~."

hi "Eso ni siquiera tiene sentido."

show mishashort invis:
    xpos 0.0
with dissolvecharamove

"Ella ya se ha ido, y regresa arrastrando a Yuuko detrás de ella."

show yuuko invis:
    center
    xpos -0.2
with None

show bg school_gate at left
show shizu behind_smile_close:
    xpos 0.83
show mishashort hips_grin at center
show yuuko neutral_up at left
with dissolvecharamove

"El flash está apagado. Un LED rojo parpadea tres veces sobre él después de que el dedo de Yuuko presiona el botón. Shizune nos mira a los dos para asegurarse de que estemos preparados. Sincronizamos relojes. Saltamos."

play sound sfx_camera
$ renpy.music.set_volume(0.0, 0.5, channel="ambient")

scene ev shizu_goodend
with cameraflashlong

ssh "Apuesto que quedó excelente."

ssh "Muy bien, …"

mi "¡Ahora, tomemos una con Yuuko, también~!"

yu "N-no, por favor…"

hi "Eso no es necesario."

"Yo también quiero una copia de esta foto."

show ev shizu_goodend_pan
with None

"Probablemente moriré más joven que la persona promedio. Mi vida podría apagarse inesperadamente en cualquier momento. Así que no tengo tiempo que perder. Quiero vivir tanto como pueda. También quiero ver sonreír a los demás con lo que he hecho."

"Vivir indirectamente a través de la felicidad de los demás no parece tan malo. Sentir alegría a través de la felicidad de otra persona no parece algo tan malo. Es la manera más fácil que se me ocurre para prolongar mi propia vida, y darle distinción."

"Quizás este es el significado que Shizune ha encontrado para sí misma, aunque es solo mi teoría. Las personas a menudo se encuentran solas en sus vidas, y sin dirección."

"Sin embargo, las personas pueden refugiarse en momentos de felicidad. Pueden marcar la vida de una persona como paradas en un mapa de trenes. O como marcaciones de memoria sobre un largo camino."

"Esos momentos individuales, pensándolo mejor, pueden darle satisfacción a la vida de una persona. Cada amigo, cada festival, cada reunión alegre, y cada despedida alegre."

"Quiero ser capaz de preguntarle un día a Shizune si tengo razón. Quiero pasar el tiempo que tengo con ella. Finalmente, quiero hacer sonreír a Shizune para sí misma."

$ renpy.music.set_volume(0.3, 1.0, channel="ambient")

scene bg school_gate at left

show mishashort perky_smile at twoleft 
show shizu behind_smile_close at tworight 


with locationchange

hi "Te amo."

"Hago una pausa, preguntándome si ella me mirará, confundida, y preguntará por qué diría eso de la nada. No lo hace."

hi "¿Hacen esa reunión aquí?"

show shizu adjust_happy_close
with charachange

ssh "Por supuesto que sí."

show mishashort sign_smile
with charachange

mi "¡Un miembro del consejo estudiantil debería saber eso~!"

show shizu behind_smile_close
with charachange


ssh "Pero más pronto que esa, ¿de acuerdo?"

show shizu adjust_happy_close
with charachange

ssh "Los dos."

show mishashort hips_grin
with charachange

mi "¡Claro~!"

hi "Sí."

show shizu basic_happy_close
with charachange

ssh "¡Yuuko! ¡Tú también haz la pose!"

show shizu adjust_happy_close
with charachange

ssh "Después, podemos ir a tomar té."

"Shizune se ríe, como si no le importara nada en el mundo, la risa de Misha uniéndose con la de ella tan fácilmente como si fuera la suya propia. Nos veremos de nuevo."

stop ambient fadeout 2.0
stop music fadeout 2.0







label es_S38:

play music music_pearly

scene bg school_scienceroom
with locationchange

"Al día siguiente, Misha está de vuelta en la clase, aunque todavía se ve bastante taciturna. No es que estuviera esperando que se sintiera mejor por arte de magia; eso sería pedir lo imposible considerando lo que pasó."

"Esta vez es Shizune la que no está. Al comienzo, casi me hace reír que de repente cuando una está en clase, la otra no. Pero cuando lo pienso, no hay nada gracioso en absoluto sobre eso. De hecho, me es difícil concentrarme en mi trabajo por eso."

"Podría ser que ella está enferma. O simplemente podría estar saltando clases. También podría ser algo más serio, y estoy tentado en preguntarle a Misha si sabe, pero termino sin hacer nada."

"No me arrepiento de intervenir ayer, temeroso de que Misha hiciera algo impulsivo."

play sound sfx_normalbell

"Pero ahora siento que debería darle algo de espacio. Finalmente, suena la campana, y Misha se levanta para almorzar junto con todos los demás. Decido almorzar hoy en un salón vacío… Pero no en este."

scene bg school_hallway3
with locationchange

"Desafortunadamente, muchos otros estudiantes parecen tener la misma idea, así que no hay muchos salones vacíos para todos. Finalmente, cuando estoy a punto de renunciar a la idea, encuentro un salón oscuro al final del pasillo."

scene bg school_miyagi
show lilly back_surprise:
    center
    ypos 1.15
with locationchange

"Sin embargo, al encender la luz, descubro que este tampoco está vacío. La cabeza de Lilly gira hacia mí, lo cual me asusta antes de que me dé cuenta de que ella probablemente me escuchó mover el interruptor de la luz."

show lilly basic_listen
with charachange

li "Hola."

hi "Hola, Lilly. No pensé que alguien más estuviera aquí."

show lilly basic_weaksmile
with charachange

li "¿Eres tú, Hisao?"

hi "Sí, pero probablemente ya lo sabías."

"Me doy la vuelta para irme, lo cual rápidamente lleva a Lilly a hablar más fuerte."

show lilly basic_smile
with charachange

li "No tienes que irte tan rápido. Ambos podemos almorzar en el mismo salón. De hecho, preferiría comer con alguien más."

"Estoy a punto de preguntarle cómo sabía que yo estaba aquí para almorzar, pero decido no hacerlo. Es solo simple sentido común, y no quiero parecer demasiado fácil de impresionar."

show lilly basic_smile_close:
    center
    ypos 1.1
with characlose

"Tomo asiento en el banco frente a Lilly, después de darle la vuelta para estar de cara a ella. He escuchado que nuestras mentes se llenan de mucho de lo que vemos basándonos en cómo recordamos verlo anteriormente, o en nuestras expectativas."

"Principalmente por eficiencia, para así no tener que procesar todo lo que ves de forma individual."

"Lilly nunca parece detenerse a cuestionar ningún ruido. Entonces, me pregunto, ¿es porque su mente está llenándose de contexto en cada momento? ¿O a ella no le importa y solo acepta las cosas como vengan?"

"Sobre su escritorio solo hay unas galletas y un termo de té. Ella debe ser de las personas que prefieren un almuerzo ligero. Doy un mordisco a mi emparedado. Algunos de los ingredientes se desparraman por la parte de atrás."

show lilly basic_ara_close
with charachange

li "No hemos hablado en mucho tiempo, estoy sorprendida de que todavía recuerdes mi nombre."

hi "¿Mmfffmm?"

show lilly basic_smileclosed_close
with charachange

li "Debes estar muy ocupado en el consejo estudiantil."

hi "Es diferente cada semana. Algunas semanas son bastante lentas, en otras semanas considero tomar un día por enfermedad."

"Espera, Lilly, necesito un segundo para recuperar mi aliento por tragarme ese emparedado."

show lilly basic_smile_close
with charachange

li "¿Y cómo ha estado últimamente?"

hi "Impredecible."

play sound sfx_snap

show lilly basic_oops_close
with vpunch

"Chasqueo mis dedos, lo cual, por su expresión facial, le molesta mucho."

show lilly basic_reminisce_close
with charachange

li "Creo que has estado saliendo demasiado con esas dos."

hi "Supongo que es uno de los distintivos de Shizune. Personalmente, me gusta."

show lilly basic_displeased_close
with charachange

li "Yo lo ignoro."

"Su tono no cambia ni en lo más mínimo, pero obviamente el estado de ánimo de Lilly ha caído."


hi "No parece que sea fácil hacerlo. He estado tratando de entender cómo ella puede hacerlo sonar tan fuerte, pero creo que me estoy dañando los nudillos."

show lilly behind_displeased_close
with charachange

li "Aunque fuera lo suficientemente fuerte para romper las ventanas, lo ignoraría. No soy una foca entrenada; yo tengo ese lujo."

hi "¿Todavía sigues enojada por eso?"

"Hago la pregunta tan cuidadosa y diplomáticamente como sea posible, aunque al final solo estoy preguntando para satisfacer mi curiosidad."

show lilly basic_weaksmile_close
with charachange

li "No, por supuesto que no, aunque no me agrada Shizune."

show lilly basic_reminisce_close
with charachange

li "Estuvimos juntas en el consejo estudiantil por un tiempo breve."

hi "Eso oí."

show lilly basic_sleepy_close
with charachange

li "Desearía que tú no hubieras sido tan rápido en unirte."

show lilly basic_listen_close
with charachange

li "No me gusta la manera como Shizune dirige el consejo estudiantil. ¿Sabías que ahuyentó a la mayoría de los antiguos miembros? Es por eso que creo que ella trata de rodearse de personas que no se opondrán a ella."

show lilly basic_reminisce_close
with charachange

li "Y no lo hacen. Es como una burbuja de dependencia."

"Estoy seguro de que Shizune es consciente de lo que Lilly está diciendo. Después de todo, puedo recordarla negando específicamente eso un par de veces, lo cual siempre había pensado que era extraño."

"Dicen que cuanto más específica es una negación, más probable es que las acusaciones sean ciertas. En este caso, creo que estaría en desacuerdo. Shizune es la única persona sobre la cual su opinión podría llamarse menos que objetiva."

hi "¿Le dijiste eso?"

show lilly basic_displeased_close
with charachange

li "Muy a menudo."

"Lilly se detiene para despacharse lo último de su té. Me estoy demorando en terminarme mi propio almuerzo y aprovecho la pausa para comer tanto como sea posible."

show lilly basic_sleepy_close
with charachange

li "Todos sus amigos están relacionados con el consejo estudiantil, como Misha."

li "Escuché que las cosas están delicadas entre ella y Misha. ¿Tuvieron una pelea?"

hi "No realmente."

show lilly basic_surprised_close
with charachange

li "¿De veras?"

show lilly basic_reminisce_close
with charachange

li "Sea como sea, no sirve de nada tratar de forzarlas a que se reconcilien."

li "Intentar siempre confrontar todo sin ambages es lo que Shizune haría, pero eso no funciona en el mundo real. En algún momento, eso es solo ser terco, no es valentía ni buenas intenciones."

hi "Eso es un poco general, ¿no lo crees?"

show lilly basic_smileclosed_close
with charachange

li "Hm, supongo."

show lilly basic_weaksmile_close
with charachange


li "¿Qué crees que es lo mejor para acompañar el té? ¿Galletas o bizcochos? Me gustan ambos, de diferentes maneras. No podría elegir."

show lilly basic_displeased_close
with charachange

li "No me gusta la gente que constantemente me obliga a tomar partido o que quieran convertir todo en un concurso."

li "Cuando me uní al consejo estudiantil, pensé que solo sería ayudar a que todo funcionara sin problemas y darle una mano a los demás, como ser la representante de la clase."

show lilly basic_reminisce_close
with charachange

li "En vez de eso, cada día consistía en tener a Shizune pisoteando por doquier, usando a Misha como un megáfono, para hablar de cómo teníamos que superar al último consejo estudiantil, y crear más y más eventos, y hacerlos cada vez más grandes."

hi "Pero entonces ustedes dos básicamente querían lo mismo. Todo eso hace que las cosas sean emocionantes."

hi "No lo entendía mucho al principio, pero no es un proyecto para el ego. A la gente le gustan los fuegos artificiales y las casetas de soba, las manzanas de caramelo y los días de disfraces, o lo que sea."

hi "Entre más cosas haga el consejo estudiantil, más responsabilidad nos da la escuela. Eso significa trabajo extra, pero en cierto modo, también significa más libertad."


hi "Tienes la fuerza de hacer cosas como organizar un gran festival, y ellos pensarán que eres lo bastante capaz de manejar la situación en lugar de rechazarlo inmediatamente."

hi "En fin, también quiero eso, ahora. Tiene su parte de trabajo inútil, pero hay momentos que hacen que valga la pena cuando todo toma forma. Me da algo que hacer. Si solo tuviera que ir a la escuela día tras día, creo que explotaría."

show lilly basic_weaksmile_close
with charachange

li "Creo que Yamaku es mucho más llevadera que otras escuelas."

"Pero Yamaku no es otras escuelas."

"Comienzo a caer en otra mentalidad familiar. En cierto modo, es casi demasiado llevadera."

"Y si yo fuera una persona diferente estoy seguro de que encontraría agobiante lo llevadera que es, aunque en cualquier otra escuela, tal simplicidad solo sería el flujo normal de la vida."

"Pero aquí, esa falta de eventos sería acentuada. Se sentiría diferente, porque no soy una persona normal, después de todo."

"Lo recordaría cada vez que escuche la sangre latiendo en mis sienes. Me sentiría controlado y débil, y mi amargura solo crecería."

hi "Sí, claro."

hi "El punto es que, creo que ahora entiendo de qué se trata todo esto. Realmente le estás haciendo pasar un muy mal rato a Shizune."

show lilly basic_sleepy_close
with charachange

li "Eso podría ser cierto, pero a la hora de tratar con otras personas, ella no lo hace muy bien."

"Desafortunadamente, eso es un poco más difícil de discutir."

show lilly basic_smile_close
with charachange

li "¿Tienes la hora? Me gusta ir a clase diez minutos antes de la campana."

hi "Entonces estás justo a tiempo si vas ahora."

show lilly invis_close at center
with dissolvecharamove

stop music fadeout 4.0

"Disculpándose, Lilly se va, y me siento escuchando el cliqueo de su bastón contra el piso desvaneciéndose entre los murmullos de otros estudiantes que están conversando en los otros salones y en el pasillo."

"Me siento exhausto, y olvido por completo que quería hablar con Shizune."

scene black
with dissolve




label es_S39:

scene bg school_hallway3
with locationchange

"Después de clases al día siguiente, inmediatamente me dirijo al salón del consejo estudiantil para hablar con Shizune."

"Aunque ella está en la clase, tratar de interrumpirla y tener una conversación con ella cerca de la puerta o en el pasillo podría ser un poco obstructivo."

scene bg school_lobby
with locationchange

"Será mejor tratar de reunirme con ella en el salón del consejo estudiantil. Me tomo mi tiempo en ir allí, tomando un jugo de la máquina expendedora en el camino."

"También repaso en mi cabeza lo que quiero decirle. No es nada demasiado importante, solo algunas preguntas sobre los próximos eventos."

scene bg school_council
with locationchange

play music music_rain fadein 8.0

"La puerta está sin seguro cuando llego."

"Creería que el salón también estaba vacío, si no pudiera ver la mochila de Shizune encaramada en su escritorio, con la parte superior de su cabeza asomándose desde detrás de ella. Parece como si ella se hubiera construido un pequeño fuerte."

show shizu basic_normal at center
with charaenter

"Shizune me saluda con la mano desde detrás de su mochila, antes de levantarla con un dedo y apartarla a un lado."

"Pero después de eso, ella inmediatamente regresa a golpetear su bolígrafo contra el escritorio y a mirar una lista como si contuviera el significado de la vida misma en ella."

show shizu adjust_frown
with charachange

ssh "¿Qué necesitas?"

his "Quería ver si había algo en lo que pudiera ayudar. Como todo eso de allí, ¿qué son esas?"

"Señalo el montón mediano de carpetas a su lado, pero ella mueve su mano con desdén."

show shizu behind_blank
with charachange

ssh "Puedo encargarme de eso yo misma."

his "¿Entonces qué hay de las elecciones?"

his "Además, ¿dónde está Misha?"

show shizu behind_sad
with charachange

shi "…"

show shizu basic_normal2
with charachange

ssh "Están yendo bien. Y le dije a Misha que iba a encargarme de todo yo misma."

his "¿Por qué?"

"Shizune gira lentamente un bolígrafo en su mano, colocándolo entre cada uno de sus dedos, como una aguja a través de un trozo de tela."

show shizu behind_blank
with charachange

ssh "Por nada."

his "¿En serio?"

show shizu adjust_frown
with charachange

ssh "Por nada."

"Ella hace las señas de nuevo para enfatizar, para cerrar la noción de que haya algo más detrás de ello. Pero lo hay, ya que definitivamente ella no está actuando normalmente."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\n\n\n“¿Y por qué la ley del hielo?” es la frase que de inmediato viene a mi mente, a pesar de que no es el momento para chistes. Pero sí describe lo que siento. No podemos comunicarnos normalmente, así que aprecio los pocos momentos en los que podemos. Ser rechazado así duele."

n "Es obvio que sean cuales sean sus razones, va a ser prácticamente imposible hablar con Shizune hoy. Más allá de simplemente ser terca, ella parece estar deprimida, pero con la manera en que ya estaba yendo nuestra conversación, no me veo siendo capaz de averiguar por qué está deprimida."

n "\nDe alguna manera, eso solamente me hace querer averiguar más. Y eso significa que tengo que preguntarle a Misha. El problema es que no sé realmente adónde va Misha en su tiempo libre."

$ renpy.music.set_volume(1.0, 1.0, channel="music")
stop music fadeout 3.0

nvl hide dissolve
nvl clear

scene bg school_lobby
with shorttimeskip

window show

"Después de preguntarle a mucha más gente de la que debería si han visto a una chica con pelo rosado brillante por ahí, y de recibir más respuestas negativas de las que esperaba, finalmente encuentro a una pareja que la ha visto."

scene bg school_cafeteria
show mishashort perky_smile at center
with locationchange

play music music_moonlight fadein 8.0

"Para cuando llego a la cafetería, donde aparentemente Misha ha estado todo este tiempo, he caminado por toda la escuela dos veces, y estoy muy cansado. Me doy cuenta de que pasé cerca de ella antes, y de que no la vi detrás de una columna."

hi "¿Por qué tú eres mejor encontrándome que yo encontrándote?"

show mishashort hips_smile
with charachange

mi "¿Me estabas buscando, Hicchan?"

show mishashort hips_grin
with charachange

mi "Hm~… ¿Quién sabe~? Creo que es solo una coincidencia."

hi "Sabes, la idea principal de las coincidencias es que no son consistentes."

show mishashort cross_laugh
with charachange

mi "Jajaja~."

hi "¿Estás almorzando tan tarde?"

show mishashort sign_smile
with charachange

mi "No pude comer a la hora del almuerzo, ¡así que sí~! Pero~, no demasiado, para así poder cenar."

show mishashort perky_smile
with charachange

mi "¿Querías hablar conmigo sobre algo, Hicchan?"

"No pierdo el tiempo."

hi "Sí. La razón por la que estoy aquí… ¿Notaste que Shizune ha estado algo malhumorada hoy?"

show mishashort perky_confused
with charachange

mi "Quería preguntarte lo mismo, Hicchan~."

show mishashort perky_sad
with charachange

mi "Bueno~, excepto que, ella ya ha estado así por un par de días."

hi "Ya veo."

show mishashort sign_confused
with charachange

mi "Hicchan, ¿crees que es por algo que hice? ¿Crees que hice enojar a Shicchan, como la última vez?"

hi "No. De todos modos, ella parece estar más enojada conmigo."

"No estoy mintiendo, de veras que no. Desafortunadamente, mis intentos de asegurarle eso no parecen andar muy bien. A su propia manera, Misha también es bastante terca."

scene bg school_dormhisao_ss
with locationskip

"Al final, regreso a mi habitación. Los últimos días no han sido nada más que una experiencia continuamente frustrante, y me dejaron agotado. Me siento tan cansado que decido tomar una siesta, esperando quizás resolver las cosas mientras duermo."

stop music fadeout 3.0

window hide

scene black
with shuteye

with Pause(1.0)
with shorttimeskip
with Pause(1.0)

scene bg school_dormhisao_ni
with openeye

window show

play music music_night fadein 1.0

"Cuando despierto, me siento más descansado, pero todavía sin claridad. La única cosa que ha cambiado es que está oscuro afuera."

"Al abrir un poco la ventana, puedo notar que el clima todavía es algo agradable. Después de tragarme en seco mis pastillas de la noche, tomo una pequeña caminata a las máquinas expendedoras."

scene bg school_lobby_ni
with locationskip

"Se les agotó todo lo que normalmente compraría, así que aplasto mi mano contra los botones hasta que algo sale."

scene bg school_courtyard_ni
with locationchange

"Las luces están apagadas en el edificio principal, incluyendo el salón del consejo estudiantil. Solo es una observación casual."

play sound sfx_rustling


"Mientras estoy pensando, escucho un crujido detrás de mí. He visto esa película antes, y ese es un sonido muy siniestro de escuchar, a solas en la noche."

show kenji happy_ni at center
with charaenter

"Afortunadamente, solo es Kenji, y se aparta de los arbustos con un estado de ánimo inusualmente alegre."

ke "Hola."

hi "¿Pero qué demonios? ¿Acaso te acercas sigilosamente a las personas de noche y les dices “hola” de manera casual y frecuente?"

show kenji neutral_ni
with charachange

ke "No, eso sería raro. Sabía que eras tú. Tengo una visión nocturna extremadamente buena. Quizás es porque soy sobrehumano."

hi "Entonces, ¿qué estás haciendo aquí?"

show kenji tsun_ni
with charachange

ke "Podría preguntarte lo mismo. ¿Qué estás haciendo TÚ aquí?"

"Considero decirle la verdad, pero rápidamente decido no hacerlo. Me tomaría mucho tiempo explicarlo."

hi "Aullándole a la luna."

show kenji neutral_ni
with charachange

ke "Yo también lo hago, a veces. Aunque la luna no salió esta noche."

"Casi ni lo oigo, sintiéndome un poco resentido por la interrupción."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\nLe mentí entre dientes a Shizune al decirle que nada estaba mal. O, para ser más exactos, mentí entre manos. Y en ese mismo momento, estaba teniendo una conversación completamente diferente con Misha."

n "Esa conversación, comprensiblemente, pudo molestar a Shizune. Pero no había manera de que ella pudiera haberla escuchado. Hasta las manos de Misha, que por lo general hacen señas de todo lo que piensa, estaban completamente quietas. Aunque no lo estuvieran, estaba parado frente a ella, bloqueándola de la vista de Shizune."

n "La única manera en la que Shizune podría escuchar esa conversación sería si ella pudiera leer los labios. Prácticamente la primera cosa que pregunté cuando comencé con lenguaje de señas fue sobre la lectura de labios, por curiosidad. No es fácil, ni es perfecto… así que nunca lo había considerado hasta ahora."

n "\nTendría sentido, y el espacio para malentendidos al leer los labios no ayudaría."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear
window show

ke "… Así que me di cuenta de que podría usar el manto de la oscuridad para comprar leche."

ke "Por lo general, solo salgo cuando llueve o cuando puedo cubrirme en un mar de ciclistas, o turistas. Esto es mucho más consistente… Pero estoy gastanto mucho dinero en leche."

show kenji happy_ni
with charachange

ke "Pareces algo deprimido o aislado o algo así. No pienses demasiado, ¡un hombre tiene que estar siempre en acción! Puedes pensar en cosas todo el día, pero la mejor manera de cambiar la situación es haciendo algo."

ke "Hago cosas sin pensar, todo el tiempo. Por eso en la secundaria me llamaban “causa muchos problemas”. Pensé que era genial, sonaba como un nombre hindú."

hi "Realmente no estoy de humor."

show kenji neutral_ni
with charachange

ke "¿Teniendo un mal día?"

hi "Sí, no lo sé. Estoy algo distraído en este momento."

stop music fadeout 7.0

hide kenji
with dissolve

"Tan distraído que, hasta que él se va, no me doy cuenta de que su consejo fue en realidad uno muy bueno. Creo que Shizune me habría dado la misma sugerencia. Para entonces, es muy tarde para agradecerle educadamente."

"Ya respondí en el tono más grosero posible. Me siento como un idiota."

"Al mirar atrás, en estos últimos días me he arrepentido de cada acción que he hecho. Lo peor es que no me he tomado el tiempo para meditar sobre ellas, y al hacerlo, aprender de ellas. Esto únicamente lleva a… ha llevado a, más arrepentimientos."

scene black
with dissolve



label es_S40:

play music music_dreamy fadein 2.0

scene bg school_dormhisao
with locationchange

play sound sfx_doorknock2

"A la mañana siguiente, cuando me estoy vistiendo, escucho que golpean a mi puerta. Poniéndome rápidamente el resto de mi ropa, la abro, sin llegar a detenerme a pensar en quién podría estar detrás de ella."

scene bg school_dormhallway
show shizu basic_normal
with locationchange

"Resulta ser Shizune."

show shizu behind_blank
with charachange

ssh "Misha me dijo que estabas buscándome."

"Estoy un poco dolido por no recibir ni siquiera un “buenos días”, pero no es gran cosa."

his "Así es."

show shizu basic_normal2
with charachange

ssh "Pero me encontraste ayer."

"Los dedos de Shizune trazan una grieta en la pared. Parece que está haciendo su mejor esfuerzo por verse distante."

show shizu adjust_smug
with charachange

ssh "Bueno, no lo hice fácil, ¿verdad?"

his "Está bien."

show shizu behind_blank
with charachange

ssh "Es por eso que estoy aquí. Podemos hablar hoy. Aunque… como que quiero ir a otro lugar."

his "¿Qué hay de la clase?"

show shizu adjust_smug
with charachange

ssh "Está bien, está bien."

show shizu basic_normal2
with charachange

ssh "¿Qué tal si damos un paseo por la escuela? Todo el lugar excepto el edificio principal va a estar desierto. La campana de la primera hora debería estar sonando ahora mismo."

"Echo un vistazo rápido a mi reloj y veo que ella tiene razón."

his "Bien."

stop music fadeout 6.0

show shizu basic_angry
with charachange

shi "…"

his "¿Hay algún problema?"

show shizu behind_blank
with charachange

ssh "¿Por qué crees que hay algún problema?"

his "Porque obviamente estás molesta. Lo acabo de notar."

his "Eso es de lo que quería hablar contigo."

show shizu basic_normal2
with charachange

"Shizune hace crujir rápidamente sus nudillos mientras le hablo en señas."

show shizu behind_blank
with charachange

ssh "Aparentemente, soy más fácil de leer de lo que había pensado. Estaba esforzándome en ocultarlo. ¿Puedes saber lo que estoy pensando ahora mismo?"

hide shizu
with charaexit

"No respondo, y Shizune se dirige hacia la puerta, con bastante lentitud para que yo note que quiere que la siga."


"Sus manos están dobladas en su espalda, la cual está arqueada contra ellas como si estuviera a punto de inclinarse hacia atrás en cualquier momento."

scene bg school_courtyard
with locationchange

"Afuera, veo que Shizune tiene razón. La escuela está completamente desierta. Aunque no es la primera vez que veo la escuela así, es algo espeluznante."

scene bg school_backexit at right
with locationchange

"Shizune actúa casi como si yo no estuviera allí, echando un vistazo a una máquina expendedora y tomando un camino lento y tortuoso hasta que terminamos detrás del edificio principal."

show shizu invis_close at tworight
with None

show shizu basic_normal_close:
    ypos 1.05
with dissolvecharamove

"Finalmente, ella se apoya contra la pared y me mira, pero siento como si hubiera olvidado cómo iniciar una conversación."

play music music_sadness fadein 8.0

show shizu behind_blank_close
with charachange

ssh "Hay un dicho. “No sabes lo mucho que lo has arruinado hasta que lo arruinas”."

his "¿Quién dice eso?"

show shizu basic_normal2_close
with charachange

ssh "Supongo que soy yo."

show shizu basic_angry_close
with charachange

"Reconsiderando el hilo de sus ideas, ella agita sus manos en frustración."

show shizu behind_blank_close
with charachange

ssh "Bueno, voy a decirlo de otra manera."

show shizu basic_normal_close
with charachange

ssh "Cuando era más joven, tuvimos que hacer carteles para el Día de la Tierra en la escuela. Había otra chica en mi clase a la que todos consideraban la mejor artista."

show shizu behind_blank_close
with charachange

ssh "No era porque ella podía dibujar mejor que todos los demás, era por lo mucho que ella podía hacer caber en una sola imagen."

show shizu adjust_frown_close
with charachange

ssh "Quería ser mejor que ella, así que hice innumerables carteles hasta que terminé con el mejor posible. Tenía que ser la mejor y tener el más grande. Al final, a todos les gustó más mi cartel, incluso al maestro."

show shizu basic_normal_close
with charachange

ssh "Una semana después, no tenía importancia. Lo tiré a la basura."

show shizu behind_blank_close
with charachange

ssh "Creo que te conté algo parecido antes."

his "Sí."

show shizu basic_angry_close
with charachange

ssh "Cuando siento que he terminado, desearía poder hacer borrón y cuenta nueva. Ya sea si tengo éxito o no. Hice pasar a Misha por muchas cosas, e incluso te arrastré a ellas."

show shizu adjust_frown_close
with charachange

ssh "Y cada punto en donde podría haber resuelto esta tonta situación, o donde podría haber evitado que ocurriera en primer lugar, sigue regresando a mí."

show shizu behind_sad_close
with charachange

ssh "Es la peor sensación. Especialmente cuando siento que no he hecho nada bien y que todo lo he hecho mal. Como recientemente. Es el peor tipo de fracaso. Me siento como un fracaso en todos los niveles."

show shizu basic_normal2_close
with charachange

ssh "Desearía poder borrar todo lo que he hecho y estar sola, ya que todo lo que he hecho es causarle problemas a Misha por dos años. Y aprovecharme de ti por un año por razones egoístas."

his "Está bien."

show shizu adjust_frown_close
with charachange

ssh "No, no está bien. No lo entiendes. Estaba pensando en ello; todo lo que hago se siente como si tuviera que vencer a alguien más. Incluso, a todos los demás. Si así es como es, ¿entonces cuáles son mis relaciones con la gente? Se sienten casi igual."

"Puedo ver a dónde va esto."

show shizu behind_sad_close
with charachange

ssh "El punto es que he fastidiado a tanta gente por ser egoísta, y ahora quiero estar lejos de los demás por un tiempo."

his "¿Incluso de mí?"

"Hay una pausa."

show shizu basic_normal_close
with charachange

ssh "Sí."

"Seguida por una pausa aún más larga, esta vez mía."

his "Ya veo."

his "Es la cosa más egoísta que podrías hacer."

his "Solo eres tú tomando otra decisión por ti misma."

show shizu basic_normal2_close
with charachange

shi "…"

"Por un minuto, parece que está considerando la mejor manera de responder, pero al final, ella simplemente asiente con la cabeza. La cual, creo, es la mejor manera de responder de todos modos."

"Es muy propio de ella, hablar con rodeos incluso ahora, pero al final sin excusas."


"Todas mis emociones hierven dentro de mí. Veo una caldera enfrente de mí, con el agua borboteando dentro de ella, tan cerca que puedo tocarla y sentir el calor irradiando de ella."

"Me alegro por la distracción, porque sé que no hay recurso ni negociación posible."

show shizu adjust_frown_close
with charachange

ssh "Me dijiste que todo estaba bien, pero no era cierto, ¿verdad?"

show shizu behind_sad_close
with charachange


ssh "Entonces no puedo creerlo nunca más."

hi "Muy bien."

show bg school_backexit at center
show shizu invis_close:
    xpos 0.85
with dissolvecharamove

"Sin siquiera molestarme en decirlo en señas, me pongo de pie. Mis manos están en mis bolsillos, tocando mi dinero suelto. El aire de la mañana se siente frío contra mi rostro."

scene ev shizu_badend:
    xalign 0.0 yalign 0.5 zoom 1.1 subpixel True
    acdc_warp 10.0 zoom 1.0
with locationchange

"Cuando vuelvo a mirarla, ella parece muy solitaria. Me recuerda a mí mismo. He hecho esa expresión antes. Tal vez está en mi rostro ahora mismo. Se siente como si la imagen de una chica tan solitaria se grabará en mi mente para siempre."

"Cada momento en donde podría haber evitado esto, o en donde podría haber resuelto el problema, regresa a mí. Me hace sonreír de alguna manera sin diversión."

stop music fadeout 4.0

window hide

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
