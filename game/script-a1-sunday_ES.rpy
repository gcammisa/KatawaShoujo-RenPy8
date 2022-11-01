label es_A38:


window hide None

scene black
with dissolve

scene bg school_dormhisao
with openeye

play music music_daily fadein 4.0

window show

"El día siguiente, me despierto sintiéndome un poco mareado. Ya casi es medio día."

$ renpy.music.set_volume(1.0,0.0, "ambient")
"Dormir hasta tarde está bien, dado que es domingo y no hay clases."

"Pero no es un domingo cualquiera, sino el día del festival también."

"Desde mi ventana puedo ver ya a algunas personas en la caseta de soba arrojando fideos dentro de platos para la gente con antojo de comida de baja calidad."

"Me trago un puñado de mis medicinas matutinas y reflexiono sobre cómo pasar el día."

"Habrá unos pocos exámenes la semana que viene, pero no los considero tan ominosos como los otros, así que no estoy tan preocupado por ellos como probablemente debiera estarlo."

"Sin obligaciones urgentes relativas a la educación, debería estar libre para pasar el día en el festival como desee."

scene bg school_dormhallway
with locationchange

"Terminando mi rutina matutina, salgo al pasillo, con la intención de pasear y encontrar algo para comer."

"Pasando por su puerta, decido ver qué es lo que Kenji tiene planeado para hoy por simple impulso."

"Tengo curiosidad sobre si tiene planes, dado que todos están haciendo algo."

"Por otra parte, puedo imaginármelo construyendo un refugio a prueba de ruido en su cuarto."

"O posiblemente algo como un fuerte, con todo y una señal de “No Se Admite A Las Chicas”."

"… y con el “Las Chicas” tachado y “Nadie” garabateado crudamente bajo eso."

stop music fadeout 2.0

play sound sfx_doorknock2

"Tocando en su puerta la cual está por suerte libre de cualquier tipo de señal, escucho una vez más el inquietante chasquido de al menos diez seguros siendo retirados. La puerta abre apenas una rendija."

show kenji neutral at Slide(0.0,0.3,0.0,0.2,0.5)
with Dissolve(.5)

ke "¿Quién es?"

hi "Se supone que debes preguntar eso antes de abrir la puerta."

show kenji neutral at center
show bg school_dormhallway at bgright
with charamove

play music music_kenji fadein 1.0

ke "Oh, eres tú. Maldición, es temprano."

hi "No es realmente tan temprano."

show kenji happy
with charachange

ke "¿Qué sucede, hombre?"

hi "Nada, iba a preguntarte qué vas a hacer hoy."

hi "La mitad de la escuela ya está afuera."

show kenji rage
with charachange

ke "¿Afuera? ¿Por qué?"

hi "¿Qué?"

ke "¿Qué de qué? ¿Hoy es un día especial? ¿Por qué están allá? ¿Quiénes son?"

show kenji tsun
with charachange

ke "Los puedo escuchar. Es fuerte… no me digas… ¿Ha comenzado la invasión?"

"De repente luce más alarmado."

show kenji neutral
with charachange

ke "¿Qué día es, hombre?"

hi "Seguro, supongo que no puedes ver las grandes casetas de madera afuera, y la gente vendiendo cosas…"

ke "¿De qué demonios estás hablando? Tengo mis cortinas cerradas todo el tiempo para frustrar a los francotiradores."

hi "Ehh, es el festival. Sabes eso… ¿Cierto?"

show kenji tsun
with charachange

ke "Oh mierda, ¿eso es hoy? Ah, maldición. Ah… Maldición. Maldita sea."

ke "No puedo creer que lo olvidé, no tengo mi fuerte terminado aún. Esto es malo."

ke "Este va a ser un muy mal día… Es bueno que me hayas dicho esto, hombre. Este va a ser un mal día."

hi "¿Por qué?"

show kenji neutral
with charachange

ke "Oh hombre, estarán por todos lados. La gente. Fuera de mi ventana. ¡Socializando!"

"Kenji frota sus sienes nerviosamente, luciendo de pronto muy enfermo."

show kenji tsun
with charachange

ke "Estará tan ruidoso como el infierno. Maldición, y yo que iba a ir afuera hoy, pero ahora está arruinado, todo está arruinado."

ke "Esto es horrible. Esto apesta. ¡Esto apesta!"

ke "Qué demonios, esto realmente apesta. Ahora no puedo ir a ningún lado. No hay ningún lugar al cual correr."

"Kenji parece nervioso. Podrías incluso decir que está perdiendo absolutamente el control."

show kenji neutral
with charachange

ke "No puedo creer esto. Así que eso es lo que hoy era."

ke "Maldición, y no pude siquiera prepararme para eso."

show kenji tsun
with charachange

ke "No pude ni siquiera fortificarme y ahora está aquí y no puedo hacer nada. Debiste decirme esto antes, chico. Quiero decir, al menos, lo sé, pero… ¡Pude haberlo sabido antes! Imagina lo que podría haber conseguido…"

hi "Lo siento. Pensé que sabías."

hi "¿Así que supongo que no vas a hacer nada hoy?"

hi "Incluso el clima es bueno. Ayer estuvo muy ventoso, así que pensé que hoy estaría frío. Sin embargo no lo está, así que no hay razón para solo permanecer dentro. Sin duda, deberías echarle un ojo al festival."

"Kenji gruñe y cubre su rostro con sus manos."

ke "Agh, no, ¡no! No puedo hacerlo. Me comerán vivo allá afuera, lo sé."

"Eso tiene que ser una broma, pero lo dijo con tal expresión de seriedad. Relativamente seria."

show kenji happy
with charachange

ke "¿Qué es lo que vas a hacer? Debemos pasar el rato aquí, puedes ayudarme a construir mi fuerte. Aún podríamos lograrlo a tiempo si trabajamos juntos."



label es_A38a:


hi "Voy a tener que pasar el rato con el consejo estudiantil, ya que perdí una apuesta."

"Me doy cuenta de que no acordamos el cuándo y dónde. Solo esperaré por ellas en lugar de arriesgarme a no encontrarnos en el caos afuera. Deben estar ocupadas corriendo y organizando cosas, de cualquier modo."

"Es gracioso. Habría asumido que el precio de perder contra Shizune en su estúpido juego sería mucho más severo. Esto es solo un pretexto para pasar el tiempo con ella. En ese caso, supongo que ella solo quiere que me divierta."

"Aun si ella no puede llegar y dejar en claro sus intenciones, podrían ser buenas intenciones después de todo, y pienso que está empezando a agradarme más."

hi "Podría pasar por alto el ir, pero sería un desperdicio. Y además quiero ir. Quiero decir, sabes, el día de hoy luce muy apasionante. Más que nada, será interesante."

show kenji tsun
with charachange

stop music fadeout 1.0

ke "¿El consejo estudiantil? ¿Qué? ¿Eso aún existe?"

ke "¿No es eso como, dos tipos?"

hi "Son ambas chicas."

play music music_tension

show kenji rage
with charachange

ke "¿En serio? ¿Son lindas? Maldición, no, espera… ¿son lindas?"

ke "¡No! ¡No importa! Escuché que la presidenta del consejo estudiantil está demente… que quien quiera que sea nunca habla y solo da órdenes a través de lacayos."

show kenji tsun
with charachange

ke "Mierda, son lo mismo en todas las escuelas… Suena como una perra despiadada. Perras en todos lados."

ke "Si son dos chicas, te sobrepasan en número de dos a uno. Eso es una situación peligrosa, chico. Quién sabe lo que pueda pasar."

ke "Maldición, el consejo estudiantil es solo dos mujeres, pero tienen demasiado poder."

ke "Deben ser detenidas."

ke "Puedo verlas, conspirando formas de forzar sus planes feministas. No puedo confiar en una administración como esa."

ke "Esto no es bueno. ¡No es bueno!"

show kenji rage
with charachange

ke "Maldición. ¡Mierda! ¡Maldición!"



label es_A38b:


hi "No lo sé. Estoy bastante hambriento así que pensé en ir por algo de comida primero y después pasearme por las atracciones."

hi "Tu proyecto de clase lucía muy bien, y eché una mano con él así que quiero al menos ver ese y hablar con Lilly supongo."

hi "Hablando de eso, ¿no tienes alguna obligación con el proyecto?"

show kenji rage
with charachange

ke "¿Estás mal de la cabeza?"

ke "Esa tipa ciega no se trae nada bueno entre manos; lo puedo sentir en mi bazo, hombre. Su presencia es como una sombra oscura que está en el camino de mi gran visión."

ke "Como se espera de la gente ciega."

hi "Qué."

hi "Además, yo pensé que tú también estabas…"

show kenji neutral
with charachange

"Él levanta su mano para interrumpirme."

ke "Solo legalmente."

ke "Metafóricamente, puedo ver más allá de lo que cualquier hombre antes que yo ha visto."

"Kenji mira estoicamente hacia la metafórica distancia para enfatizar su declaración, adelantando su barbilla confiadamente para parecer más masculino. De hecho es solo la pared del corredor dos metros más lejos pero da igual."

show kenji tsun
with charachange

ke "Puedo ver el futuro de la raza humana, y es uno oscuro a menos que la amenaza de las mujeres sea sofocada."

ke "Están por todos lados."



label es_A38c:


hi "Bueno, me uní al club de arte así que supongo que iré con ellos."

show kenji rage
with charachange

ke "¿Hiciste qué?"

hi "Me uní al club de arte."

show kenji tsun
with charachange

ke "Hombre, esa fue una mala jugada. Realmente mala. No sabes el tipo de chicas que hay en el club de arte. Bellezas perturbadas y angustiadas que te arrancan el corazón y se lo comen crudo."

"Bueno, conozco a una miembro del club de arte, y realmente no veo a Rin volviéndose repentinamente una asesina psicópata."

hi "Eso parece improbable."

ke "No digas eso. No te engañes a ti mismo. No tienes ni idea de a lo que te estás enfrentando aquí, hombre. Son el peor tipo."

show kenji neutral
with charachange

ke "Ellas te arrastran dentro con esta mierda seudointelectual y cuando menos te lo esperas, ¡BAM!"

hi "¿Bam qué?"

"Kenji parece ligeramente anonadado por mi escepticismo, pero no menos zafado."

show kenji tsun
with charachange

ke "No importa."

ke "Anda con cuidado hombre, anda con cuidado."



label es_A38d:


hi "Me pregunto… Tengo un poco de hambre, pero hice este trato de que trataría de cuidar mejor de mí mismo. Ser más saludable, ya sabes."

hi "No sé si debo evitar completamente el takoyaki, o dirigirme directo a él."

show kenji tsun
with charachange

ke "¿Trato? Suena ominoso. Así que ¿qué estarás obteniendo a cambio?"

hi "¿Nada, supongo? No es ese tipo de trato."

hi "¿Conoces a Emi, de nuestra generación? Acordamos algo como de cuidarnos las espaldas entre nosotros y…"

show kenji rage
with charachange

ke "¡Aieeeeeeee!"

"El agudo grito y la expresión de abyecto terror en el rostro de Kenji hielan mi sangre. Es como si le hubiera dicho a un sacerdote católico que le vendí mi alma al diablo."

ke "¡Ella! Le vendiste tu alma al diablo, ¿y no obtuviste nada a cambio?"

ke "¿Qué demonios sucede contigo, hombre?"

ke "¿Sabes con quién te estás enfrentando?"

ke "Ella es un peligro para la salud pública. ¿Sabes a cuánta gente manda al hospital mensualmente con sus cuidadosamente colocadas tacleadas voladoras?"

show kenji tsun
with charachange

ke "¡Es una de ellas! Una jugadora clave en la vasta conspiración que apunta por la completa sumisión de todo lo varonil."

ke "No puedo creer lo que estoy escuchando. Confié en tu juicio, hombre. Pensé que éramos hermanos."

ke "Tienes que cancelar antes de que sea demasiado tarde."

ke "Este festival también; es solo una de sus estratagemas."



label es_A38e:

"Él manosea su bufanda nerviosamente, más y más rápido como si estuviera tratando de iniciar un fuego, después lentamente empieza a calmarse una vez que el ataque de pánico termina su curso."

show kenji neutral
with charachange

ke "Voy a tener que encontrar algún lugar para esconderme, un refugio seguro. Y después dejarme a mí mismo inconsciente para no tener que experimentar este horrible día."

ke "Tengo la cosa perfecta para eso. Ahora debo prepararme."

show kenji tsun
with charachange

ke "No vayas al festival."

hi "Está bien."

show kenji neutral
with charachange

ke "Hasta luego, amigo."

stop music fadeout 2.0

hide kenji
with charaexit

"La puerta lentamente se cierra con un chirrido suave y no sé cómo sentirme sobre lo que Kenji acaba de decir."




label es_A44:

show bg school_dormhallway at bgright
with None

"Considero qué es lo que quiero hacer con Shizune y Misha. Decidiendo que es mejor estar extrapreparado, me escabullo a mi habitación para proveer mi cartera con dinero."

scene bg school_dormhisao
with locationchange

"Me pregunto si tendrán ese juego donde tratas de atrapar peces de colores en una red de papel."

"Parece ser mucho más fácil de lo que lo hacen ver. Por otra parte, si llegara a atrapar un pez de colores, no tendría una razón real para quedármelo."

"¿Qué voy a hacer con un pez en mi diminuta habitación? ¿Cocinarlo?"

"Podría dárselo a Shizune o Misha, pero eso podría ser sobrepasar los límites."

"Es un problema real. Ambas son lindas, pero no creo que tenga una oportunidad con ninguna de ellas. A pesar de todo, le doy vueltas a la idea de hacerlo. Me imagino cómo podrían reaccionar si les diera un regalo esta noche, como un pez o una muñeca."

"Misha probablemente se reiría como siempre hace. Shizune podría golpearlo lejos de mi mano."

"Tal vez no es tan buena idea después de todo."

"Está bien, creo que estoy listo."

with shorttimeskip

"Un largo rato después, decido que esto podría ser otra prueba para ponerme nervioso ideada por Shizune. Incluso si no lo es, está empezando a hacerse algo tarde."

"Decido ir afuera y buscarlas, a pesar de que no sé dónde podría revisar. Podrían ser realmente difíciles de encontrar hoy."

scene bg school_dormhallway
show shizu behind_blank_close at center
with locationchange

"Tan pronto como doy un paso afuera, casi choco con Shizune."

hi "Hola, Shizune. ¿Dónde está Misha?"

show shizu behind_frustrated_close
with locationchange

"Trato de decirlo con señas lo mejor que puedo, pero en verdad solo estoy inventando. Tengo que pedirle a Misha que me enseñe algo de esto."

mi "¡Aquí!"

play music music_comedy

show shizu behind_frustrated_close at Slide(0.5,0.5,0.7,0.5,1.0, time_warp=_ease_time_warp)
with None

show misha hips_grin behind shizu at Slide(0.5,0.5,0.3,0.5,1.0)
show shizu behind_frustrated_close at Slide(0.5,0.5,0.7,0.5,1.0,time_warp=_ease_time_warp)
with Dissolve(0.7)

"Misha se aparece de detrás de Shizune, sonriendo ampliamente."

mi "Solo venimos para asegurarnos de que vendrás con nosotras al festival."

show shizu basic_angry_close at tworight
with charachange

shi "…"

show misha sign_smile at twoleft
with charachange

mi "¡No renuncies a tu promesa~!"

hi "¿Promesa? No creo haber prometido nada."

show shizu cross_angry_close
with charachange

shi "…"

show misha hips_frown
with charachange

mi "¡Deja de tratar de salir de esta!"

show misha perky_sad
with charachange

mi "Vamos, Hicchan, ¡será divertido! Necesitas esto, de todas maneras, ¡o te volverás un bueno para nada!"

show misha perky_smile
with charachange

mi "No quieres convertirte en una de esas personas que solo permanecen en su cuarto todo el día, siendo paranoicas, ¿o sí?"

"Me encuentro lanzando una mirada sobre sus hombros hacia la puerta de la habitación de Kenji frente a la mía."

"Espero que no haya escuchado eso, pero creo que Misha quiere lo contrario."

hi "No, desde luego que no. Solo estaba bromeando un poco, y estaba a punto de irme de todas formas. Ustedes dos no tenían por qué venir aquí."

show misha cross_laugh
with charachange

mi "¿En verdad? ¡Ajajaja! ¡Shicchan estaba preocupada de que intentaras salirte de esta de alguna forma!"

show misha hips_grin
with charachange

mi "¡Te necesitamos, Hicchan~!"

hi "¿Eh?"

"Creo que mi corazón acaba de detenerse por un momento."

show misha perky_smile
with charachange

mi "No tengo el tino para tirar las muñecas de sus bases en el juego ese… y Shicchan se rehúsa a lanzar cosas."

hi "Oh."

"Shizune me mira, notando inmediatamente mi decepción. Ella descruza sus brazos y ajusta sus anteojos."

show shizu adjust_happy_close
with charachange

shi "…"

mi "¿A qué pensaste que nos referíamos? Me rehúso a lanzar cualquier cosa."

show misha perky_confused
with charachange

mi "¿Por qué, Shicchan? Eso es raro…"

show misha perky_smile
with charachange

mi "Bueno, como sea, Hicchan, has lanzado una pelota antes, cierto~, ¿cierto~? ¡Así que! ¡Tienes que venir con nosotras!"

"Estoy sorprendido por su lógica. No sé si están bromeando o no."

hi "Je, me sentiría ofendido si no supiera que están bromeando."

hi "Están bromeando, ¿cierto?"

show shizu behind_frown_close
with charachange

shi "…"

mi "¡Es lo que es, Hicchan~! ¡Es lo que es lo que es lo que es lo que es!"

hi "Bueno, eso es reconfortante."

show shizu basic_normal2_close
with charachange

shi "…"

show misha hips_smile_close at closeleft
with characlose

mi "Vente, ¡vamos! La banda de sordos se está preparando fuera de tu ventana."

"Misha agarra mi mano y trata de jalarme hacia afuera de la puerta, pero es claro que no está tratando del todo."

hide shizu
with None

show shizu basic_normal2_close behind misha at tworight
with None

show shizu adjust_blush_close
with charachange

stop music fadeout 3.0

"Shizune nos mira a ambos, sonrojándose ligeramente y jugueteando con sus anteojos impacientemente."

"No estoy acostumbrado a esta clase de contacto casual, pero no tengo nada contra él. ¿Cómo podría negarme?"

play ambient sfx_crowd_outdoors fadein 1.0

scene bg school_courtyard
show crowd
with locationskip

play music music_running

"Aún hay luz afuera, pero el Sol se está preparando para ponerse detrás de los árboles."

"Pareciera que la mitad de la escuela está allá afuera, y puedo incluso ver a algunos miembros de la facultad apartándose a un lado, sirviéndose un poco de ponche."

"Están por vaciar el recipiente completo, para consternación de la chica trabajando en el puesto."

"Hay algunos adivinos hablando despreocupadamente con sus amigos, mientras otros ya han empezado a lanzar horóscopos a cualquiera que camine a su alcance."

"Creo que ese tipo de táctica es un poco demasiado agresiva, pero demuestra que están metidos en eso. Te renueva el ver eso, pero no sé si lograré acostumbrarme a ello."

show shizu basic_normal2 at tworight
show misha perky_smile at twoleft
with charaenter

shi "…"

show misha sign_smile
with charachange

mi "Bueno, debemos conseguir algo de comer. ¿Con hambre, Hicchan?"

"Ahora que lo pienso, no he comido en todo el día."

hi "En realidad no quiero comer fideos fritos."

show misha hips_grin
with charachange

mi "No te preocupes, ¡hay otras comidas fritas!"

hi "¿Hay alguna comida que no esté frita?"

show shizu adjust_smug
with charachange

shi "…"

mi "Dulces. ¡La comida chatarra es la esencia de las celebraciones!"

show misha cross_laugh
with charachange

mi "¡Guajajajaja!"

show shizu behind_smile
with charachange

shi "…"

show misha hips_grin
with charachange

mi "Vamos, yo —quiero decir, Shicchan— ¡te invitará una cosa~!"

mi "¿Una?"

show shizu adjust_smug
with charachange

shi "¡…!"

show misha sign_smile
with charachange

mi "¡Solo una~! ¡Solo para que puedas acumular energía para tu brazo lanzador!"

show misha perky_smile
with charachange

mi "Ah, pero parece que no todas las casetas han terminado de armarse, así que podrías no lograr obtener lo que quieres."

"Doy una mirada alrededor, sorprendido por el número de puestos. Es increíble, este festival parece más grande que los que de hecho se podrían ver en los pueblos."

"A pesar de lo que Misha dijo, parece que la mitad de la escuela ya está celebrando."

"Resuenan en el aire las charlas animadas de al menos la mitad del cuerpo estudiantil."

"Puedo oler comida cocinándose, y eso solo me está provocando más hambre a cada segundo."

show shizu behind_frustrated
with charachange

shi "…"

show misha perky_confused
with charachange

mi "Vamos, Hicchan, ¡la comida ya está desapareciendo rápido! Si quieres takoyaki, ¡necesitamos movernos ahora!"

show misha hips_grin
with charachange

mi "¡Me agradaría un poco de takoyaki~! Vamos, ¡comamos eso!"

hi "Está bien, no he tenido takoyaki en mucho tiempo. Me uno."

hide shizu
with charaexit

hide misha
with charaexit

"Shizune parte antes de que Misha pueda traducir eso a ella, caminando enérgicamente hacia el puesto de takoyaki mientras Misha y yo tratamos de alcanzarla."

scene bg school_stalls1
with locationchange

"Misha se ríe mientras brinca hacia Shizune, quien pide tres órdenes de takoyaki levantando tres dedos."

"Nunca lo noté antes, pero para alguien que está obsesionada con té de primera clase, es un poco raro que Shizune esté también tan metida en la comida rápida."

"Recibo el plato de takoyaki que me entrega y me pregunto si debería comenzar a comer. Se ve extremadamente caliente."

"Puedo ver el humo saliendo de ahí y el aceite burbujeando en la superficie."

show misha hips_smile at Slide(0.2,0.5,0.3,0.5,1.0)
show shizu behind_blank at Slide(0.8,0.5,0.7,0.5,1.0)
with Dissolve(1.0)

"Shizune y Misha me miran, como esperando a que coma antes de que ellas puedan empezar."

"No puedo echarme para atrás, así que clavo uno en el diminuto tenedor sobresaliendo despreocupadamente de la esquina del plato."

show misha hips_grin at twoleft
show shizu basic_normal at tworight
with charachange

stop music fadeout 12.0

"Sin embargo, antes de que pueda siquiera ponerlo en mi boca, Shizune y Misha comienzan a comer ansiosamente, Shizune dando rápidos pero delicados bocados a su takoyaki mientras Misha come con deleite como un niño pequeño."

"Creo que al final del día, ambas son solo chicas como cualquier otro estudiante aquí."

"Esto es agradable. No creo haber tenido una oportunidad como esta en un largo tiempo para solo pasar el rato con otras personas y disfrutar de su compañía."

"Incluso antes de venir aquí, he estado pasando por un año muy ocupado. Tan ocupado que ni siquiera me había dado cuenta de lo que me estaba perdiendo hasta ahora."

"Aquí, me siento en paz."

"Esta es una atmósfera relajante. No sabía que este tipo de festivales aún existían."

show misha perky_confused
with charachange

mi "¿Eh? Hicchan, ¿no te vas a comer tu comida?"

hi "No, sí me la comeré."

show shizu adjust_smug
with charachange

shi "…"

show misha sign_smile
with charachange

mi "Espero que no estés acobardándote solo porque está demasiado caliente."

hi "No es eso."

"Incluso sus burlas están comenzando a volverse encantadoras."

$ renpy.music.set_volume(0.6, 2.0, "ambient")

scene bg school_stalls1_ss
with shorttimeskip

play music music_tranquil fadein 1.0

"Como rápido antes de que mi comida pueda enfriarse, pensando que las tenues linternas de papel encendidas resplandeciendo cálidamente contra el atardecer hacen de esta una vista hermosa."

show shizu behind_smile_close_ss at center
with charaenter

"Antes de que pueda terminar mi último bocado de takoyaki, Shizune se para frente a mí, permaneciendo perfectamente derecha con sus brazos rígidamente detrás de su espalda."

"Puedo ver que está dando lo mejor de sí por verse tan seria como sea posible, pero ni siquiera ella puede esconder su buen humor, dado que hay una ligera sonrisa en su rostro."

show bg school_stalls1_ss at bgright
show shizu behind_smile_close_ss at closeright
with charamove

show misha cross_laugh_ss at twoleft
with charaenter

mi "¡Ajajaja~! Vamos, Hicchan, ¡vamos a jugar algunos juegos!"

hi "¿Han terminado de armarlos?"

show shizu adjust_happy_close_ss
with charachange

shi "…"

show misha cross_grin_ss
with charachange

mi "No, pero no importa, ¡no importa~! Vamos, Hicchan, ¡antes de que se llene de gente!"

show misha hips_grin_close_ss at closeleft
with characlose

"Misha pone su mano en mi hombro y se ríe muy fuertemente."

show misha perky_smile_close_ss
with characlose

mi "¡Vamos! ¡Vamos! Los premios lucen de verdad grandiosos este año, de verdad ¡de verdad~! ¿No te gustaría ganar algunos premios para dos lindas chicas como nosotras?"

"Misha lanza su mejor mirada “linda”, que es ciertamente bastante linda. Miro a Shizune, esperando que haga lo mismo, pero solo me mira como si estuviera loco."

show shizu cross_wut_close_ss
with charachange

shi "…"

show misha hips_grin_close_ss
with characlose

mi "Misha, ¡deja de hacer eso!"

show misha perky_confused_close_ss
with charachange

mi "Espera… Yo soy Misha…"

show shizu basic_normal2_close_ss
with charachange

shi "…"

show misha sign_smile_close_ss
with charachange

mi "Hicchan, apresúrate, ¡has estado sosteniendo ese pedazo de takoyaki como por mil años!"

show misha cross_laugh_close_ss
with charachange

mi "¡Jajajajaja!"

show misha cross_smile_close_ss
with charachange

hi "Me gusta saborear todo lo que como. Incluso esto."

show shizu basic_sparkle_close_ss
with charachange

show shizu adjust_smug_close_ss
with charachange

"Sin advertencia, Shizune roba el takoyaki de mi mano y se lo echa a la boca rápidamente con una sonrisa."

"Sucede tan rápido que no hay forma en que pudiera haberla detenido."

show misha cross_laugh_close_ss
show shizu behind_smile_close_ss
with charachange

"Antes de poder siquiera entender del todo lo que acaba de pasar, Misha rompe en carcajadas, y Shizune me sonríe, probablemente lo más cercano que la he visto a llegar a reír."

show shizu adjust_happy_close_ss
with charachange

shi "¡…!"

mi "Bueno, ¡esto resuelve eso~! ¡Guajaja! ¡Jajajaja!"

stop music fadeout 6.0

"Shizune toma mi mano derecha, y Misha toma mi izquierda."

show shizu behind_smile_close_ss
with charachange

shi "…"

show misha hips_grin_close_ss
with charachange

mi "¡Vendrás con nosotras! Hay mucho que hacer esta noche, ¡deberías esforzarte más en disfrutarlo!"

show misha cross_laugh_close_ss
with charachange

mi "¡Jajajaja~!"

$ renpy.music.set_volume(1.0,2.0, "ambient")

scene bg school_courtyard_ss
show crowd_ss
with shorttimeskip

play music music_ease fadein 6.0

"Corriendo a través de una ya considerable muchedumbre, jugamos juego tras juego, de lanzamiento de aros, a whack-a-mole, y juegos sobre los que nunca he escuchado."

"Raramente ganamos, pero es divertido a pesar de todo."

hi "Oye, ¿tienen ese juego de agarrar peces de colores aquí?"

show shizu behind_smile_ss at tworight
show misha hips_smile_ss at twoleft
with charaenter

shi "…"

mi "¡Desde luego! ¡No sabía que te gustara ese juego, Hicchan!"

hi "Bueno, siempre he querido intentarlo. No parece muy difícil."

show misha hips_grin_ss
with charachange

mi "¿Estás seguro de eso, Hicchan~?"

show misha cross_laugh_ss
with charachange

mi "¡Guajajaja~! ¡Está bien, está bien! ¡Ya veremos! ¡Debe estar por aquí en algún lado!"

show shizu basic_normal_ss
with charachange

shi "…"

show misha perky_smile_ss
with charachange

mi "Pero, ¿dónde vas a tener a tu pez? ¿Tienes un recipiente para él?"

hi "Bueno, no…"

show misha hips_grin_ss
with charachange

mi "¡Tal vez se lo comerá!"

show shizu adjust_smug_ss
with charachange

shi "…"

show misha cross_laugh_ss
with charachange

mi "¡Jajajajajaja! ¡¡Ajajajajajaja!!"

show misha cross_grin_ss
with charachange

mi "Está bien, Hicchan, si ganamos algún pez, ¡te lo daremos a ti!"

hi "Oh, ¿en serio? ¿Otro juego? Bien, entonces."

show shizu basic_happy_ss
with charachange

"Shizune me empuja animadamente hacia la caseta, tratando de ocultar su entusiasmo en sus ojos."

scene bg school_stalls2_ss at bgright
with locationchange

"Afortunadamente, ninguna de las dos consigue atrapar ni un solo pez, aunque yo no lo hago mejor."

show bg school_stalls2_ss at bgleft
with charamove

$ renpy.music.set_volume(0.6,2.0, "ambient")
"No puedo evitar sino reír mientras inmediatamente después ellas comienzan a jalarme hacia un particularmente largo y colorido puesto que ayudé a construir."

"Recuerdo este; había sido un verdadero martirio hacerlo."

"El encargado de la caseta, un tipo de aspecto común con cabello teñido de café, rompe su letargo cuando nos ve caminando hacia él. Noto dos cosas:"

"Primero, es uno de esos juegos donde lanzas una bola a una pirámide de botes opacos y tratas de tirar tantos como sea posible."

"Cuatro bolas por 50 yenes, eso es muy bueno."

"Segundo, hay instrucciones de cómo jugar en braille. Casi quiero decir algo, y ver si Shizune y Misha lo ven también."

"O no lo ven, o no lo encuentran extraño del todo."

"Operador de caseta" "¡Hey! ¡Es bueno verte, Hakamichi! Muchas gracias por tu ayuda con esta caseta. ¿Divirtiéndote?"

"Shizune da un vistazo hacia Misha, quien traduce todo para ella en un santiamén, y luego sonríe al operador."

show shizu behind_smile_ss at Slide(0.8,0.5,0.7,0.5,1.0)
show misha perky_smile_ss at Slide(0.2,0.5,0.3,0.5,1.0)
with Dissolve(1.0)

shi "…"

show misha hips_grin_ss at twoleft
with charachange

mi "¡Jaja~! No fue nada, nada de nada, ¡en verdad~! Sin duda, esto es grandioso, ¡creo que el mejor festival que hemos armado hasta ahora!"

show misha perky_smile_ss
with charachange

mi "Shiraki, nos gustaría jugar esto, está bien, ¿cierto?"

show misha hips_grin_ss
with charachange

mi "Desde luego~, sería realmente grandioso si simplemente le dieras a tus lindas y trabajadoras incansables representantes del consejo estudiantil un premio, ¡por todas las horas que ponemos de nosotras para hacer todo esto posible!"

"Shiraki" "Jajaja, jaja… No."

"Si Shiraki tiene algo, son huevos."

hi "Oye, yo construí este puesto, y además fue un trabajo extenuante. Desperdicié dos horas de mi vida, creo que merezco al menos una ronda gratis."

show misha hips_frown_ss
with charachange

mi "¡Y yo!"

show shizu basic_angry_ss at tworight
with charachange

shi "…"

mi "¡Yo también!"

show misha perky_confused_ss
with charachange

mi "Ah…"

"Después de dudarlo un poco, eventualmente cede, y nos da cuatro bolas a cada uno con un encogimiento de hombros."

show misha hips_grin_ss
show shizu behind_blank_ss
with charachange

"Escasamente un segundo después, Shizune y Misha sueltan sus bolas frente a mí."

hi "¿Y ahora qué?"

hi "No me digan que después de hacer tal escándalo por esto, ¿ustedes ni siquiera van a jugar?"

hi "No después de la forma en que nos unimos contra Shiraki."

"Shiraki" "Sí…"

show shizu basic_frown_ss
with charachange

shi "…"

show misha sign_smile_ss
with charachange

mi "¡Tú mantente fuera de esto, por favor~!"

show shizu adjust_happy_ss
with charachange

"Shizune gira hacia mí y comienza a sacudir su mano despectivamente. Misha parece dividida entre traducir para ella y consolar al operador de la caseta."

show shizu adjust_smug_ss
with charachange

shi "¡…!"

show misha hips_grin_ss
with charachange

mi "¡Ajajaja! Hicchan, ¿dónde está tu sentido de caballerosidad? Además, yo… Shicchan, ¡tiene una política contra lanzar bolas!"

show misha hips_smile_ss
with charachange

mi "Ah, lo siento, Hicchan. No sé si mi puntería es tan buena, tampoco. Sin embargo, tú debes de ser muy bueno en estas cosas, cierto, ¿cierto? ¡No debe ser un problema para ti!"

stop music fadeout 3.0

"Esto luce lo suficientemente simple. Los botes ni siquiera están tan lejos, el único desafío es que estas son bolas ultralivianas."

play sound sfx_impact

"Lanzo una a los botes con fuerza, y esta rebota sin ceremonias."

show shizu behind_blank_ss
show misha perky_confused_ss
with charachange

hi "¿Qué demonios?"

"Shiraki" "Ah, sí, no es tan fácil como parece. Hay agua dentro de los botes. Secreto de oficio."

show misha hips_frown_ss
with charachange

mi "¡Eso no es muy justo!"

hi "Esto debe ser el porqué son cuatro bolas por 50 yenes. Qué astuto."

show shizu basic_angry_ss
with charachange

shi "…"

show misha hips_smile_ss
with charachange

mi "Vamos, Hicchan, ¡puedes tirarlas! ¡Tienes once oportunidades más! ¡Ve!"

hi "Tal vez ustedes deberían hacerlo."

hi "¿Shizune? ¿Quieres intentar?"

show shizu behind_blank_ss
with charachange

"Shizune sacude su cabeza enfáticamente de lado a lado."

"Me río, esto es de hecho muy divertido."

play sound sfx_impact
play music music_soothing fadein 3.0

"Posicionándome, lanzo otra bola a la pirámide de botes y logro hacerlos moverse solo un poco."

show shizu basic_normal_ss
show misha perky_smile_ss
with charachange

"Ambas, Shizune y Misha están lanzando miradas de anhelo a un muñeco con forma de gato."

"Después de todo, no son tan diferentes."

"Algunas veces me pregunto si Shizune sonaría como Misha si pudiera hablar."

"No, no son tan parecidas."

play sound sfx_impact

"Lanzo otra bola, dándome cuenta de que es en realidad bastante simple. Si puedo golpear dos botes en la columna inferior al mismo tiempo, es una victoria fácil."

"Una pequeña multitud está ya comenzando a formarse, así que de verdad hay presión sobre mí. Nueve tiros más."

play sound sfx_dropstuff

"Preparándome como un pitcher de béisbol, lanzo tan fuerte como puedo y los botes se vienen abajo."

show shizu behind_blank_ss
show misha cross_laugh_ss
with charachange

show stuffedcat:
    alpha 0.0 yalign 0.5 xanchor 0.5 xpos 0.6 subpixel True
    easein 1.0 xpos 0.5 alpha 1.0
with Pause (1.0)

"Triunfantemente, pido mi femenino premio muñeco-gato y Misha ríe a carcajadas como si fuera ella la que lo ganó."

"Shizune me mira con su expresión vacía usual. Está claro que ella quiere el muñeco también."

show stuffedcat:
    easeout 1.0 xpos 0.4 alpha 0.0
with Pause (1.0)

hide stuffedcat
with None

show shizu basic_normal2_ss
with charachange

shi "…"

show misha hips_grin_ss
with charachange

mi "Hicchan, ¡felicidades~! ¿Qué vas a hacer con ese muñeco?"

"No hay respuesta correcta. Tengo que negociar cuidadosamente."



hi "Yo… no lo sé."

mi "Bueeeeeno~ lo tomaré, si no lo quieres…"

show shizu adjust_smug_ss
with charachange

shi "…"

show misha cross_grin_ss
with charachange

mi "A menos que quieras quedártelo para ti, Hicchan. No sabía que te gustaran los muñecos. Qué delicado."

hi "No me gustan. No tengo uso para esto."

show misha cross_smile_ss
with charachange

mi "¿Puedo tenerlo yo, entonces?"

show shizu behind_blank_ss
with charachange

shi "…"

"Sus ojos están perforando en mi alma."

"Esta es una decisión que no quiero hacer. Giro otra vez hacia la caseta."

hi "Oye, ¿tienes otro más de estos muñecos?"

"Shiraki" "De hecho, sí, solo uno más."

hi "Está bien, prepara todo otra vez, quiero intentar sacar ese también."

"Aún tengo ocho intentos."

play sound sfx_pillow

"Tan pronto como el juego está preparado otra vez, lanzo tan fuerte como puedo una vez más, pero fallo."

show misha hips_grin_ss
with charachange

mi "¡Jajaja! ¿Tratando de ganar otro? ¿Tomando el camino fácil, Hicchan?"

hi "Si es tan fácil, podrías intentar."

mi "¡No gracias~!"

show misha perky_smile_ss
with charachange

mi "Dime, Hicchan, ¿puedes al menos soltar el muñeco mientras lanzas las bolas?"

hi "No."

show shizu adjust_smug_ss
with charachange

shi "…"

mi "Solo queda una más, ¡más te vale lograrlo! Si fallas, ¡te mataré~!"

show shizu behind_smile_ss
with charachange

shi "…"

mi "Pero, ¡qué forma tan mañosa de zafarte de darme el muñeco! Y por mí, ¡me refiero a mí~!"

show shizu adjust_happy_ss
with charachange

shi "¡!"

show misha cross_laugh_ss
with charachange

mi "¡Ajajajaja~! ¡Solo bromeo!"

"Puedo ver que Misha no planeaba ningún daño con eso, y Shizune parece disfrutar su broma, sonriendo por ella, pero un momento después luce un poco deprimida."

"Decido darle el muñeco, al menos mientras estoy tratando de ganar el otro. Es un tanto difícil apuntar sosteniendo un gato gigante."

show shizu behind_smile_ss
show misha perky_smile_ss
with charachange

shi "…"

mi "Gracias, Hicchan. ¡Shicchan luce feliz, Hicchan~! Pero, vas a ganar uno para mí también, ¿cierto?"

hi "Es lo que estoy tratando de hacer, ¿o no?"

stop music fadeout 5.0

show shizu behind_smile_ss at Slide(0.7,0.5,0.8,0.5,1.0, time_warp=_ease_out_time_warp)
show misha perky_smile_ss at Slide(0.3,0.5,0.2,0.5,1.0, time_warp=_ease_out_time_warp)
with None

hide shizu
hide misha
with Dissolve(1.0)

play sound sfx_pillow

"Lanzo de nuevo, pero mi puntería está demasiado mal esta vez."

"Mi brazo se siente algo pesado también, como si la sangre no estuviera fluyendo apropiadamente hacia él."

"Me regaño mentalmente, pensando en que es patético que me haya podido cansar con algo como eso."

"Después me doy cuenta de que tal vez sea por mi corazón. Si lo es, entonces no sé qué pensar."

play sound sfx_impact

"Es deprimente que incluso algo tan pequeño como esto sea suficiente para hacerme darme cuenta de mi propia mortalidad."

"Supongo que no habrá nunca un momento en que pueda olvidarme de ello."

"Incluso hoy, cuando pensé que podría solo disfrutar de mí mismo, en esta hermosa noche y en este hermoso lugar, no puedo escapar a la razón por la cual estoy aquí."

"Nunca me he sentido tan en paz en mi vida, en este lugar que no es como ninguno en el que haya estado."

play sound sfx_pillow
play music music_sadness fadein 2.0

"Es difícil ahora evitar pensar lo impensable:"

"Que tal vez haya sido mandado aquí a morir."

"Estos pocos días pasados han sido algunos de los mejores de mi vida. La primera vez en un largo tiempo en que me he sentido verdaderamente vivo."

"Pero al final, soy alguien que se encuentra siendo recordado a cada momento que si sube muchas escaleras o lanza una bola demasiado fuerte podría morir en cualquier segundo."

play sound sfx_pillow

"Siempre estaré limitado por esto."

"Me siento deprimido por eso, y también enojado. Al final, me preocupo por mi vida, y la disfruto, y ahora es más efímera de lo que nunca ha sido."

"Me pregunto qué es lo que finalmente me liquidará. Podría ser cualquier cosa, si soy así de débil y patético: una mala caída, un golpe al pecho, una pelota de béisbol perdida."

"Ahora he perdido mi voluntad para mantenerme jugando este juego, pero me mantengo jugando de cualquier forma."

stop music
$ renpy.music.set_volume(0.0,0.0, "ambient")
play sound sfx_heartfast

show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)

"De repente, siento una sensación fugaz de dolor en mi pecho. Viene y se va instantáneamente, pero es suficiente para hacerme tropezar solo un poco."

$ renpy.music.set_volume(0.4,10.0, "ambient")

show shizu adjust_blush_close_ss at Slide(0.8,0.5,0.7,0.5,0.5)
show misha perky_confused_close_ss at Slide(0.2,0.5,0.3,0.5,0.5)
with Dissolve(0.5)

"Shizune salta hacia atrás, sobresaltada. Se acerca, mirándome con preocupación. Misha pone su mano en mi hombro."

play music music_pearly

mi "Oye, Hicchan, ¿estás bien?"

hi "Sí, no pasa nada. Realmente no me siento muy bien en este momento. Creo que estoy enfermo. No creo que pueda seguir."

show misha hips_frown_close_ss at twoleft
with charachange

"Misha frunce el ceño."

mi "No te presiones. Si estás tan enfermo, solo te pondrás más enfermo."

show shizu basic_normal2_close_ss at tworight
with charachange

shi "…"

show misha hips_smile_close_ss
with charachange

mi "Mira, el festival apenas va empezando, y hemos estado jugando juegos por un rato. Podemos tomar un pequeño descanso si estás cansado."

show misha sign_smile_close_ss
with charachange

mi "Buena idea, Shicchan, ¡me estoy sintiendo un poco cansada también! ¡Creo que todos estamos un poco desgastados, corriendo por toda la escuela, Hicchan!"

"Asiento con la cabeza. No parecen notar nada inusual. Eso es bueno."

scene bg school_courtyard_ni
show crowd_ni
with shorttimeskip

$ renpy.music.set_volume(1.0,2.0, "ambient")

"Caminamos a través del mar de gente, con Misha animosamente apuntando a las caras de todos los que conoce. Shizune sostiene el gato de peluche en sus brazos, acunándolo sin darse cuenta. Parece que se están divirtiendo."

"De repente, siento un golpe de culpa."

"Por mi mala salud, todos tuvimos que detenernos."

show shizu behind_smile_ni at tworight
show misha perky_smile_ni at twoleft
with charaenter

shi "…"

mi "Hicchan, ambas tenemos un poco de hambre. ¿Qué hay de ti?"

hi "No tengo tanta hambre como podría tener, pero sí quiero algo de comer."

show misha hips_smile_ni
with charachange

mi "¡Eso es más que suficiente, Hicchan~! Así que, ¿qué debemos conseguir para comer?"

hi "En realidad no me importa."

show shizu adjust_happy_ni
with charachange

shi "…"

show misha hips_grin_ni
with charachange

mi "¡Ah! ¿Qué tal emparedados, entonces? ¡Y también necesitaremos algo para beber! ¡Misha conseguirá todo!"

show misha perky_confused_ni
with charachange

mi "¿Qué?"

show shizu behind_smile_ni
with charachange

"Shizune me mira y sonríe, y me doy cuenta de que ella podría estar tratando de levantarme el ánimo con una broma. Me río."

show shizu adjust_happy_ni
with charachange

shi "…"

show misha perky_smile_ni
with charachange

mi "Hicchan, está llenándose un tanto de gente, así que tal vez no podremos comer aquí. También está poniéndose un tanto ruidoso."

show misha sign_smile_ni
with charachange

mi "Tal vez debamos ir a comer arriba en la azotea."

hi "Por mí está bien. Podría ser una buena vista, y podría haber un poco de brisa."

show misha hips_grin_ni
with charachange

mi "¡Entonces está bien! Supongo que debo ir a conseguir la comida y las bebidas ahora… ¡Así que los veré después~!"

hide misha
with charaexit

stop music fadeout 6.0

"Misha agita torpemente su mano y luego sale corriendo."

"Antes, no noté cómo lucen las lámparas de papel iluminando la oscura noche, pero ahora que puedo verlo, es realmente una vista asombrosa."

"Luciérnagas flotan en lo alto, su suave resplandor haciendo parecer como si estuvieran nevando luces en el cielo nocturno."

"Este tipo de cosas serían imposibles de ver en la ciudad."

show shizu adjust_happy_ni at Slide(0.7,0.5,0.5,0.5,0.5,time_warp=_ease_time_warp)
with None

show shizu cross_angry_close_ni at Slide(0.7,0.5,0.5,0.5,0.5,time_warp=_ease_time_warp)
with Dissolve(0.5)

"Shizune tira de mi manga impacientemente y cruza sus brazos, frunciendo el ceño como para mostrar disgusto hacia mí por distraerme."

show shizu basic_angry_close_ni at center
with charachange

shi "…"

hi "Sabes, no sé cómo leer lenguaje de señas."

show shizu behind_frown_close_ni
with charachange

shi "…"

"Ahora que lo pienso, ¿no es un tanto estúpido de mi parte el haber dicho eso a una persona sorda? No podría haber escuchado."

show shizu behind_blank_close_ni
with charachange

"Me encojo de hombros, esperando mostrarle que no entiendo. Shizune sacude su cabeza y lo rechaza con una sacudida de su mano."

"Tal vez debo sacar el tiempo para pedirle a Misha algunas lecciones de lenguaje de señas."

$ renpy.music.set_volume(0.3, 1.0, "ambient")

scene bg school_roof_ni
with locationskip

"Al subir a la azotea, me encuentro asombrado otra vez ante el enorme tamaño de esta escuela. Los terrenos son tan extensos que no puedo creer que no me haya dado cuenta antes."

"Mientras avanzo a través de la azotea, caminando detrás de Shizune, no puedo evitar sino sobrecogerme por las estrellas brillando en el cielo."

show shizu behind_smile_close_ni at center
with charaenter

"Shizune y yo nos sentamos en una banca. Ella parece estar de buen humor pues sonríe suavemente mientras una brisa sopla a través de su cabello."

"Miramos hacia abajo al festival, el cual parece un mar de linternas ámbar brillando y abanicos de papel agitándose atestado de personas, algunas de ellas vestidas festivamente en yukatas."

"De hecho, la mayoría de las chicas parecen estar vistiendo yukatas. Me pregunto por qué Shizune y Misha no se arreglaron así hoy."

"Las dos lucirían bien en yukata. Brevemente pienso sobre los tipos que vestirían."

"Shizune iría probablemente con algo tradicional. Sin embargo, lo de Misha es un poco más difícil de adivinar."

"Misha llega, sin aliento por correr hacia nosotros, tratando de evitar que se caiga la comida que lleva en sus brazos."

"Acomodando todo en el piso, ella se deja caer hacia atrás."

show shizu behind_smile_close_ni at tworight
show bg school_roof_ni at bgright
with charamove

show misha hips_grin_ni behind shizu at twoleft
with charaenter

mi "¡Ajajajajajajajajaja~! ¡Eso tomó un rato! Vamos, ustedes dos no me dijeron lo que querían, así que traje un poco de ponche de arroz, unos emparedados, ¡y un poco de dulce también! ¡Un poco de todo!"

hi "Eso es genial. Pues a comer."

"Misha da una mordida a un pequeño emparedado triangular."

show misha hips_smile_ni
with charachange

mi "Entonces, Hicchan, ¿qué piensas del festival? Es agradable, ¿no?"

hi "Seguro."

show shizu adjust_happy_close_ni
with charachange

shi "…"

mi "Las estrellas se ven bien hoy. Este no podría haber sido un día más perfecto."

play music music_serene fadein 5.0
$ renpy.music.set_volume(0.1, 2.0, "ambient")

scene black
show bg misc_sky_ni at Fullpan(30.0)
with locationchange

"El sonido de la gente hablando bajo nosotros es como una suave música junto con los cantos de los grillos a la distancia."

"Tomo un sorbo de la lata de ponche y miro a Misha, quien parece como que está durmiendo confortablemente con su espalda extendida y una lata medio llena de jugo de manzana balanceada en su estómago."

"Shizune se sienta con las piernas recogidas hacia sí, meciéndose adelante y atrás lentamente como un impaciente niño mientras mira hacia el cielo."

"Ambas son bastante lindas. Observo alrededor y puedo ver muchos estudiantes agarrados de las manos con sus novias o novios."

"No muy lejos de nosotros en este techo, hay parejas mirando hacia arriba a las estrellas o hacia abajo a las luces del festival, agarradas de las manos."

"Una parte de mí quiere eso."

"Mirando a Shizune y Misha, me pregunto si debería pedirle a una de las dos salir algún día. Me pregunto si valdría el riesgo."

"Las manecillas doradas moviéndose a través de la cara del delicado reloj en la muñeca de Shizune captan mi atención, y veo que se está volviendo un tanto tarde. Pero las festividades están aún en todo su esplendor."

"Shizune está aún sosteniendo el gato de peluche que gané por la pata. Ella me nota mirándolo."

shi "¿…?"

"Indiferentemente, me lo ofrece. Sonrío, queriendo preguntarle qué haría yo con él, pero ella no podría entenderme."

"Sacudo mi cabeza y trato lo mejor que puedo de decirle que se lo quede, esperando que lo entienda."

"Mientras miro hacia la escuela, puedo ver ante mí a muchas personas, todas las cuales están felices y animadas."

"Mirarlas me hace sentir contento."

"Esto realmente fue algo especial. Hoy valió la pena."

"Pero aún no puedo sacarme de encima los sentimientos de culpa y melancolía de antes, se mantienen aferrados a mí, y no puedo dejarlos ir."

"Shizune me hace algunas señas, y no puedo entenderla. No importa lo que diga, no podrá escucharme."

hi "No puedo entenderte, Shizune."

hi "Bueno, como sea. Me pregunto si ambos nos consideramos culpables por esto. De cualquier modo, pido perdón por no poder entenderte."

hi "¿Sabes?, estoy casi, casi feliz de que trataste de obligarme a venir aquí. Sin embargo, si intento salir contigo, puede que tenga que pensar más acerca de ese lado tuyo."

hi "No, de hecho… estoy feliz. Hoy fue agradable."

hi "Serías más linda si sonrieras más, tienes una bonita sonrisa."

stop music fadeout 5.0

show shizu behind_frustrated_close_ni at center
show bg misc_sky_ni at right
with charaenter

"Frustrada, ella se levanta, los brazos atrás de su espalda, luciendo autoritaria y segura contra el fondo de estrellas."

stop ambient fadeout 2.0

show shizu out_serious_close_ni
with charachange

"De repente, Shizune lanza sus brazos hacia el cielo abierto, dando la impresión de que lo agarrara entre sus manos."

"Es como si me estuviera diciendo que observe a todo frente a mí:"

show shizu epictransition
show cityscape zoom behind shizu
show hill enter behind shizu

"La escuela, bañada con el brillo del festival e iluminada con las coloridas yukatas, el techo iluminado por luciérnagas, el cielo tan vasto que impone ese sentimiento de admiración sobre ti."

"¿Qué es lo que quiere? Lentamente me doy cuenta con el tiempo. Este hermoso escenario ante mí es prueba de que hay cosas lo suficientemente maravillosas como para que el arruinarlas con un mal humor sea imperdonable."

"Y puedo sentir el peso de la personalidad de Shizune acentuando la idea."

hi "Gracias, supongo."

hide shizu
show hill pairtouch at center
with charachange

"Miro a otro lado, pero entonces Shizune me agarra por el hombro, su reloj rozando contra mi mejilla."

"Con su mano izquierda, ella apunta al cielo."

play ambient sfx_fireworks fadein 1.0

show fireworks behind hill
with None
show fw_screen behind fireworks
with Dissolve(5.0)

"Con tenues estallidos, los fuegos artificiales comienzan a explotar en el cielo, cada uno esparciendo un baño de brillantes colores que lentamente se disuelven en la oscuridad."

"No puedo ni siquiera recordar del todo la última vez que vi fuegos artificiales, mucho menos una exhibición tan grande. Sin mencionar que al parecer están siendo lanzados desde la escuela; es casi imposible de creer."

"Las luces en el cielo se mezclan con una segunda salva desde el pueblo de abajo, y parecen cronometrados para complementarse entre sí como dos partes en un dueto."

"Continúan por tal vez quince minutos más, y luego se detienen."

"Shizune se da cuenta de que su mano está aún sobre mi hombro y la retira cuidadosamente, luciendo un poco incómoda."

stop ambient fadeout 5.0
hide fireworks
hide fw_screen
show hill pairnotouch
with Dissolve(5.0)

"Recuperando su compostura, sonríe, con las manos en las caderas y el pecho henchido."

"Es en estos momentos en los que ella luce más como una chica adolescente normal. Llena de energía, feliz, y despreocupada."

"Me mantengo pensativo mientras como con Shizune, ambos mirando en silencio a las multitudes abajo dispersándose gradualmente."

"Ella se sienta inclinada ligeramente hacia adelante, su barbilla descansando suavemente en sus manos y una apariencia satisfecha en su rostro con solo una pizca de melancolía."

"En todo momento aún sosteniendo gentilmente el gato de peluche."

"Comienzo a sentirme cansado y le digo que las veré a ella y Misha mañana, sin siquiera darme cuenta de que no puede escucharme, y luego comienzo a caminar de vuelta a los dormitorios."

"Me siento cálido y vivo, incluso en este frío aire nocturno."

stop music fadeout 4.0

"La imagen de Shizune de pie enérgica ante las estrellas, negándome mi autocompasión, no se escapa de mi mente fácilmente."

"Si… si solo toma un momento para que exista el amor, creo que me podría estar enamorando de ella."

"Solo un poquito."

window hide




label es_A39:

show bg school_dormhallway at bgright
with None

"Es un poco inquietante, y ahora comienzo a sentirme inseguro."

"¿Debería molestarme en ir?"

"Tengo un libro que he querido leer."

"Algo acerca de un servicio de correos clandestino que puede o no existir."

"Es corto, también. Podría tenerlo terminado en un día."

"¿Pero sería esa una buena manera de pasar mi tiempo?"

"Bueno, sí. Definitivamente lo sería."

"Pero supongo que probablemente sería una mejor idea ir afuera."

"Ver el festival."

"Tratar de integrarme con todas las demás atracciones secundarias."

"Honestamente, por lo menos debería hacer un intento de mantener la personalidad algo afable que he tenido esta última semana."

"Tal vez ir a comer algo, me sugiere el estómago."

"Ya es casi la hora del almuerzo… Podría al menos conseguir algo en uno de los puestos de afuera."

play music music_soothing fadein 1.0
play ambient sfx_crowd_outdoors fadein 1.0

scene bg school_courtyard
show crowd
with locationskip

"Pronto estoy afuera, rodeado por varios estudiantes y gente que pueden o no ser sus padres."

"Cada tanto alcanzo a ver a alguien que claramente vino del pueblo simplemente por la promesa de un festival."

"Son fáciles de identificar."

"Aquellos que no pueden parar de mirar, y detrás de sus ojos puede verse que están pensando “Bien, ¿y qué hay de malo con {b}este{/b} de aquí?”."

"Casi me dan ganas de gritarles."

"Pero al mismo tiempo, ¿acaso puedo negar que he estado haciendo lo mismo toda la semana?"

"Una oleada de algo semejante a la repugnancia me cubre por completo; una sensación de culpa por mi propia intolerancia."

"…"

$ renpy.music.set_volume(0.6,2.0, "ambient")

scene bg school_stalls1
with locationchange

"Pongo esos pensamientos de lado, concentrándome en las punzadas de hambre que queman mis tripas como un incendio arrasador."

"El aroma de algo frito me lleva a la tierra prometida, donde puedo conseguir algo para almorzar."

stop music fadeout 0.6

"Estoy apenas pidiendo mi orden cuando una voz fuerte me interrumpe."

show emi basic_annoyed at Slide(0.7,0.5,0.5,0.5,0.5)
with charaenter

emi "Oye, ¿qué demonios estás haciendo?"

play music music_comedy fadein 0.5

hi "Comprando desay— eh, ah, almuerzo."

show emi sad_annoyed at center
with charachange

emi "¿Desayuno?"

show emi sad_angry
with charachange

emi "¿Quieres decir que te acabas de levantar?"

hi "Eh…"

"Súbitamente dormir por toda la mañana se siente como un crimen."

hi "No, quise decir almuerzo… en serio."

"No se la está creyendo."

hi "¿Desalmuerzo?"

show emi basic_annoyed_close
with characlose

emi "¡Eso no es un desayuno saludable en lo absoluto!"

"Me arranca la comida de mis manos y me lanza una mirada feroz."

"¿Qué demonios está haciendo esta chica?"

hi "¡Oye, ese es mi desayuno!"

show emi sad_annoyed_close
with charachange

emi "¿Qué pasó con eso de que es tu almuerzo?"

hi "Eso es mi… ¡como sea, es mi comida!"

"Emi pone sus manos en sus caderas y comienza a darme una perorata."

show emi basic_annoyed_close
with charachange

emi "¿En verdad olvidaste ya tu plan alimenticio?"

emi "¡Necesitas ser más consciente de tu salud, Hisao!"

show emi sad_angry_close
with charachange

emi "¿Qué hay de tu corazón?"

hi "¡Mi corazón está bien tal y como está! La mayor parte."

"Lo único que logro es que como respuesta ella ponga los ojos en blanco."

show emi basic_annoyed_close
with charachange

emi "Lo dudo."

show emi basic_closedgrin_close
with charachange

emi "No estarías aquí si así fuera, ¿o sí?"

"La chica tiene razón, claro está."

"Pero no pienso concedérsela."

hi "¡No es un corazón tan malo!"

hi "¡Ciertamente puede soportar un poco de grasa cada tanto!"

"Sí, claro. Y también soportó perfectamente un poco de trote."

show emi basic_annoyed_close
with charachange

"Emi no parece convencida."

"No es de sorprenderse, ya que ni siquiera he logrado convencerme a mí mismo."

emi "Quizás, ¡pero no si siempre te quedas dormido todo el día!"

"Una mirada taimada le atraviesa el rostro."

show emi basic_grin_close
with charachange

emi "Por supuesto, si hubieses estado siguiendo una rutina desde el principio no estarías en esta situación…"

stop music fadeout 6.0

hi "¡Oye, he tenido una semana bastante ajetreada! ¿Sabes?"

hi "Por ejemplo, ¡casi me muero! Y luego hubo un montón de estar conociendo gente, y luego estuve en la azotea un rato…"

show emi sad_annoyed_close
with charachange

emi "Que no es excusa para holgazanear, ¿sabes?"

emi "Una pequeña experiencia cercana a la muerte no es excusa para botar el ejercicio básico."

show emi basic_closedgrin_close
with charachange

emi "Como correr por las mañanas."

"Asiente, como si algo importante acabara de ser decidido."

show emi basic_happy_close
with charachange

play music music_emi fadein 0.5

emi "¡Entonces ya está arreglado!"

show emi excited_proud_close
with charachange

emi "Has visto el error de tus acciones y estás dispuesto a adherirte a mi rutina, ¿verdad?"

emi "¿Te veo tempranito en la mañana?"

show emi excited_happy_close
with charachange

emi "¿Vamos a ser compañeros de carreras?"

hi "Sabes, ya me habías convencido ayer de que esto era una buena idea."

hi "No necesitas convencerme de nuevo."

"No es que yo haya hecho un buen trabajo siendo el convencido."

"Ella está en lo correcto acerca de comer sano, después de todo. Y heme aquí pidiendo algo asquerosamente insalubre."

"¡Pero delicioso!"

"Hay cosas más importantes que la exquisitez, ¿no es así?"

"¿Como mantenerse con vida?"

"Si Emi no estuviese regañándome por mis malas decisiones, yo probablemente…"

"Oye, espera un segundo."

"Una súbita pregunta surge en mi mente."

hi "Oye, ¿por qué demonios has tomado tal interés en mi bienestar?"

show emi basic_closedgrin_close
with charachange

"Emi se encoge de hombros y me sonríe."

show emi basic_grin_close
with charachange

emi "Eres el chico nuevo."

emi "Me imagino que no tienes ningún amigo aún, ¿verdad?"

show emi sad_grin_close
with charachange

emi "Además, te he causado problemas toda la semana, ¿verdad?"

emi "Te lo debo porque no te enojaste."

show emi basic_happy_close
with charachange

emi "Y le dije al enfermero que lo haría, de todos modos."

"Ah… ajá. La pequeña niña loca y corredora quiere hacerme estar saludable."

"Bueno, supongo que hay destinos peores."

hi "De acuerdo, eso suena… bien."

hi "Gracias por tu preocupación."

hi "¿Mañana por la mañana, entonces?"

stop music fadeout 1.0

hide emi
with charaexit

"Me imagino que eso le pone fin a la conversación, así que me doy vuelta para irme."

emi "¡No tan rápido!"

play music music_running

with vpunch

"Siento una mano en el cuello de mi camisa y en un momento soy jalado desde atrás."

hi "¡Oye, no hay necesidad de ser tan brusca!"

hi "¿Qué quieres ahora?"

show emi sad_shy_close at center
with charaenter

"Emi se ve casi herida por el tono molesto de mi pregunta."

emi "Pensé que te vendría bien un poco de compañía."

show emi basic_annoyed_close
with charachange

"Sus ojos se entrecierran."

emi "Además, ibas a llevarte a escondidas más de esa basura frita, ¿o no?"

"Bueno, no iba a hacerlo, pero ahora que lo menciona eso hubiera sido una muy buena idea."

hi "¡No iba a hacerlo!"

show emi sad_annoyed_close
with charachange

"Otra mirada fulminante."

hi "Está bien, tal vez iba a tomar un poco…"

"La mirada continúa."

hi "Bueno, un montón."

"Por Dios, soy un peligro para mí y para los demás, ¿verdad?"

"Termino accediendo en que debo ser más saludable, y entonces de inmediato comienzo a considerar el siguiente hábito poco saludable que se me presenta."

show emi basic_closedgrin_close
with charachange

emi "¡Lo sabía! No se puede confiar en ti."

show emi basic_grin_close
with charachange

emi "Ahora definitivamente debo quedarme contigo."

"Toda esta situación se siente ridícula."

"Tan solo puedo imaginarme lo que los transeúntes piensan al verme siendo regañado por una diminuta chica de la mitad de mi tamaño."

"Quizás debería rendirme por el momento."

hi "Bien, haz lo que quieras."

"Suspiro."

"Bien podría sacarle el mejor partido a esto."

hi "¿Qué quieres hacer?"

show emi basic_confused_close
with charachange

"Emi piensa por un minuto."

emi "Bueno, le prometí a Rin que pasaría por su mural…"

show emi basic_grin_close
with charachange

emi "¡Así que hagamos eso!"

"Confieso sentir algo de curiosidad por cómo terminó Rin con su mural, y de nuevo considero que hay peores destinos."

$ renpy.music.set_volume(1.0,2.0, "ambient")

scene bg school_courtyard
show crowd
with locationchange

"Asiento con la cabeza y me encuentro siendo casi arrastrado a través de la multitud mientras Emi corre deprisa a nuestro destino."

stop music fadeout 6.0
stop ambient fadeout 2.0

scene bg school_dormext_full at bgright
with locationchange

"Para cuando llegamos a los dormitorios, puedo sentir mi corazón retumbar."

"Mi corazón no debería latir así solo por algo como eso."

"Respiro hondo un par de veces, procurando relajarme."

"Soy uno de los que más normales se ven en esta escuela, pero debo estar aquí."

"A veces casi desearía haber perdido una mano o algo."

"Al menos así sería obvio que pertenezco aquí."

"Pero en cambio ni siquiera parezco enfermo."

"Incluso ahora, intentando recuperar mi aliento, solo me veo fuera de forma."

"Emi mira hacia atrás y nota mi estado de aflicción."

show emi basic_hes at Slide(0.4,0.5,0.5,0.5,0.5)
with charaenter

emi "No te me vas a morir, ¿verdad?"

show emi basic_shock at center
with charachange

emi "¡Por favor no lo hagas!"

show emi sad_depressed
with charachange

emi "Será por mi culpa, y no quiero lidiar con esa clase de remordimiento."

emi "Además, después de la última vez realmente no creo que necesite ver eso una vez más, especialmente porque el enfermero de seguro me dirá que fue mi culpa."

play music music_soothing fadein 8.0

hi "N… nah, estoy bien."

hi "Creo que necesito empezar a correr, después de todo."

show emi basic_closedgrin
with charachange

emi "Y tú que querías seguir comiendo tu grasoso… lo que sea que fuera."

show emi excited_proud
with charachange

emi "¿Ves? Fue bueno haberte encontrado, ¿no?"

"Sí, lo fue."

hi "Tal vez."

show emi basic_grin
with charachange

"Por supuesto que no agrego que no estaría en este estado si ella no me hubiese arrastrado a través de todo el terreno del festival."

"Cualquier conversación subsecuente es interrumpida por la repentina aparición de Rin."

show rin basic_absent at Slide(1.0,0.5,1.0,1.0,1.0)
with Dissolve(1.0)

rin "Oh, son ustedes."

show rin basic_absent at tworight
show emi basic_grin at twoleft
show bg school_dormext_full at center
with charamove

show rin basic_awayabsent
with charachange

rin "Hola Emi."

show emi basic_closedhappy
with charachange

emi "¡Hola Rin! ¡Traje a Hisao conmigo porque estaba por darse un infarto a sí mismo!"

show rin basic_absent
with charachange

hi "¡No es cierto!"

"Mi objeción pasa desapercibida."

show emi basic_grin
with charachange

emi "¡Pasamos a ver cómo quedó el mural!"

"Rin asiente lentamente."

show rin basic_awayabsent
with charachange

rin "Bueno, está justo ahí."

show rin basic_deadpan
with charachange

rin "Pueden verlo con bastante claridad."

"Comienzo a preguntarme cuánto tiempo ha estado Rin parada frente al mural."

"¿Siquiera se habrá detenido alguien para mirarlo?"

"¿Somos los primeros?"

"Obviamente no somos los primeros en verlo, por supuesto."

"Quiero decir, es bastante grande."

"Uno estaría muy apresurado para no verlo."

"Por otro lado, no creo que alguien haya hablado con Rin al respecto."

"Alguien además de nosotros, digo."

"Me siento obligado a decir algo."

hi "Se ve muy bien."

show rin negative_spaciness
with charachange

rin "Aún no estoy contenta con cómo quedó."

rin "Pero supongo que servirá."

"Parece casi resignada a ello."

"No estoy seguro de qué esperaba como resultado, pero supongo que no llegó hasta allí."

scene bg mural at Fullpan(100.0, dir="left")
with Dissolve(2.0)

"Nos paramos al frente del mural, apreciándolo."

"Intento concentrarme lo mejor que puedo en su composición."

"Es de hecho bastante interesante."

"Los colores se arremolinan y se mezclan entre sí, arrastrándome con ellos."

"Tiene una cualidad onírica en el todo que casi me hace sentir adormecido."

"Intento buscar algunos de los colores que Emi y yo le conseguimos."

"Hago lo que puedo, pero no consigo ver nada de azul Prusia."

"Oh, bueno."

"Estoy seguro de que está por allí en alguna parte."

scene bg school_dormext_full
show rin basic_awayabsent at tworight
show emi basic_closedgrin at twoleft
with Dissolve(2.0)

"Comienzan a dolerme los pies, pero Rin no parece muy dispuesta a moverse."

"Emi habla."

show emi basic_confused
with charachange

emi "Oye, Rin, ¿has comido?"

show rin basic_deadpan
with charachange

rin "Por supuesto. De otro modo no puedes sobrevivir."

show emi basic_hes
with charachange

emi "¿Qué tal en las últimas cinco horas?"

show rin relaxed_nonchalant
with charachange

rin "Tal vez. Pero tengo hambre de nuevo, eso podría significar que estoy equivocada."

show emi basic_closedgrin
with charachange

"Emi sonríe y aplaude infantilmente."

show emi basic_grin
with charachange

emi "¡Bien! ¡Ven a comer con nosotros!"

"Rin asiente en afirmación."

show rin basic_deadpannormal
with charachange

rin "Está bien, pero deberíamos apurarnos antes de que se den cuenta de que no estoy."

"De algún modo no pienso que les importe."

"Quienes quiera que sean."

stop music fadeout 3.0
$ renpy.music.set_volume(0.6,0.0, "ambient")
play ambient sfx_crowd_outdoors fadein 1.0

scene bg school_stalls1 at Fullpan(8.0)
with locationskip

"Al dirigirnos a los puestos de comida, lanzo una mirada de anhelo hacia la comida frita."

"No, será mejor que no."

"De todos modos estoy seguro de que Emi no me dejaría."

stop ambient fadeout 1.0

scene bg school_gardens
show emi basic_closedgrin at twoleft
show rin basic_awayabsent at tworight
with locationchange

play music music_ease fadein 9.0

"Encontramos un bonito lugar en el pasto y nos sentamos para comer lo que compramos."

"Bueno, mejor dicho, lo que compré. De algún modo he terminado pagando por toda la comida."

"Sorprendentemente, mi comida (sin freír) está bastante buena."

"El silencio se asienta mientras Emi y yo comemos y Rin mira a… alguna cosa u otra, ocasionalmente dando uno o dos mordiscos de su comida."

"Termino de comer primero y me acuesto en el pasto."

"Emi levanta la vista de su comida."

show emi basic_confused
with charachange

emi "¿Cansado, Hisao?"

hi "Un poco, creo."

show emi basic_annoyed
with charachange

emi "Bueno, no duermas de más ni nada mañana por la mañana."

show emi excited_proud
with charachange

emi "Empezamos nuestras carreras matutinas, ¿recuerdas?"

"En realidad, me había olvidado de ellas."

"De hecho solo estaba pasándola bien."

"Vagar por el festival con ellas ha sido divertido, en verdad."

hi "Sí, pondré una alarma."

show emi basic_annoyed
with charachange

emi "¡Más te vale estar ahí!"

show emi basic_closedgrin
with charachange

emi "¡Me enojaré si no estás!"

hi "Dios no lo quiera."

show rin basic_lucid
with charachange

rin "No creo que Dios tenga algo que ver."

show rin basic_deadpan
with charachange

rin "A menos que ocurra un extraño accidente y tu reloj haga cortocircuito."

show rin basic_deadpannormal
with charachange

rin "Eso tal vez pueda ser un acto impredecible de Dios."

show emi basic_grin
with charachange

emi "Bueno, no causes ningún acto impredecible de Dios, entonces."

"Un plan se forma en mi mente."

"Un plan que me hace sentir un tanto culpable, pero intentaré ejecutarlo de cualquier manera."

"Maldita sea, me he ganado un poco de comida frita."

"Y de todos modos, voy a empezar a trotar mañana, ¿o no?"

"Así que la rutina empezará entonces, no ahora."

"Ergo, la parte dietética empieza mañana también, ergo puedo tener algo poco saludable hoy."

"Una manera de despedirse de todo lo que solía comer con desenfreno antes del hospital."

hi "De hecho, supongo que debería volver a mi habitación."

hi "Tengo algo de tarea por hacer, y si voy a trotar en la mañana debería acostarme temprano…"

show emi basic_annoyed
with charachange

"Esos ojos entrecerrados otra vez."

show emi sad_annoyed
with charachange

emi "¿Seguro que no vas a escabullirte y comprar algo de esas cosas fritas de allá?"

hi "Nah, ya estoy muy lleno para molestarme."

"Le doy una palmada a mi estómago para enfatizar."

hi "Además, ustedes dos me han dejado limpio de todas formas."

show emi basic_closedhappy
with charachange

"Emi se ríe. Es un sonido sorprendentemente agradable."

"Otro remordimiento en la conciencia."

"Ella tiene que saber que le estoy mintiendo, ¿no es así?"

"¿O simplemente es así de confiada?"

"Me siento como una especie de monstruo."

show emi excited_proud
with charachange

emi "Todo parte de mi plan maestro, Hisao."

show emi basic_closedgrin
with charachange

emi "Bueno, entonces supongo que te veré mañana en la mañana."

show emi basic_grin
with charachange

emi "¡Gracias por la comida! ¡Y por hacernos compañía!"

"Y yo pensando que ella me estaba haciendo un favor."

show rin relaxed_surprised
with charachange

"Rin asiente en concordancia."

rin "No diré “nos vemos mañana” porque eso sería como predecir el futuro, y estoy segura de que no puedo hacer eso."

hi "…"

hi "Bueno."

hi "Hasta luego a las dos."

"Me siento extrañamente contento por haber decidido salir de mi cuarto este día."

"No es una mala forma de empezar mi segunda semana aquí, supongo."

stop music fadeout 9.0
play ambient sfx_crowd_outdoors fadein 1.0

scene bg school_stalls1
with locationchange

"Una vez que estoy seguro de haber salido de la vista de Emi, me dirijo derecho a los puestos de comida y compro un poco de pastel."

"Al menos no está frito, ¿no?"

"Eso es algo levemente mejor de lo que planeaba hacer."

"Aunque aún me siento un poco mal por haberle mentido a Emi."

"Ella en verdad parece estar preocupada por mi salud."

"Se lo compensaré de algún modo."

"Mejor me dirijo a mi habitación."

"Oye, {b}en verdad{/b} tengo algo que hacer."

stop ambient fadeout 1.0

scene bg school_dormhisao
with locationskip

"Mi libro me espera, y me dejo caer sobre la cama y leo durante el espectáculo de fuegos artificiales."

$ renpy.music.set_volume(0.1,0.0, "ambient")
play ambient sfx_cicadas fadein 2.0

scene bg school_dormhisao_ni
with Dissolve(2.0)

"Eventualmente todo ese caminar por todas partes (o más precisamente, correr por todas partes) me alcanza."

"Realmente estoy fuera de forma."

"Emi arrastrándome en la mañana para correr bien podría ser algo bueno después de todo."

"Es algo para esperar con ánimos."

stop ambient fadeout 2.0

window hide





label es_A40:

play ambient sfx_crowd_outdoors fadein 0.3
play music music_soothing fadein 0.5

scene bg school_dormext_full
show crowd
with locationskip

"El alegre bullicio de la gente me recibe mientras me abro paso a través de la puerta principal y salgo."

"El campus de la escuela fue transformado en un festival entre ayer y esta mañana."

"Coloridos puestos se alinean en los caminos principales desde la entrada principal hasta el edificio de la escuela."

"Algunas personas siguen llevando cosas de un lugar a otro, pero detrás de la mayoría de los mostradores se encuentran estudiantes relajados que parecen listos para empezar."

"La mayoría de los demás estudiantes se ha levantado temprano para terminar los preparativos."

"Un sentimiento de culpa me atraviesa, pero pronto se va."

"Tan solo soy un humilde estudiante de transferencia, después de todo."

"Algunos visitantes están ya paseándose por el campus."

"Hay algunas familias jóvenes con los padres perturbados tratando de mantener el ritmo de sus hijos demasiado entusiastas…"

"… Unos pocos de nuestros estudiantes acompañados por sus padres…"

"… y mucha gente joven y vieja que está aquí sin ninguna razón que pueda imaginarme."

play sound sfx_warningbell

"El carillón cobra vida y la voz chillona del director anuncia la apertura del festival por el megáfono."

"Todos aplauden educadamente aunque un poco faltos de ánimo."

"Un festival escolar… realmente no teníamos festivales en mi vieja escuela. Se siente algo pasado de moda, especialmente considerando la escuela de donde vine, pero aun así es un poco emocionante."

"Un día libre se siente bien después de la primera semana de trabajo duro, a pesar de haber estado en cama durante cuatro meses antes de esto."

"Recuerdo incluso desear poder ir a las lecciones de matemáticas durante mi estadía en el hospital."

"No puedo recordar el programa para el festival, a pesar de que Mutou lo dijo durante la clase apenas el otro día."

"Bajo de los escalones del dormitorio, con la intención de hacer un recorrido por el campus para ver todo lo que los demás han montado, pero solo logro llegar a la parte inferior de las escaleras."

stop ambient fadeout 1.0

hide crowd
show rin relaxed_boredom at tworight
with Dissolve(2.0)

"Algunas personas están estudiando el mural de Rin, mientras que la propia artista está descansando en las orillas, recargada contra la pared, viéndose extremadamente aburrida y un poco indispuesta."

hi "Buenos días."

show rin relaxed_surprised
with charachange

rin "Hola."

hi "¿Qué tal está yendo?"

show rin relaxed_nonchalant
with charachange

rin "A ningún lugar."

rin "Estoy atorada."

hi "¿A qué te refieres con atorada?"

rin "Quiero decir que no puedo caminar atorada. Creo que mis piernas están fuera de servicio por lo de ayer."

hi "¿Te duelen?"

show rin relaxed_sleepy
with charachange

rin "Es difícil decirlo. Tal vez."

"El esfuerzo de trabajar en el mural fue más grande de lo que me dejó saber. Pensé que era tan solo músculos un poco cansados o algo. Quiero preguntar algo más de ello, pero Rin rápidamente cambia a otro tema."

show rin basic_awayabsent
with charachange

rin "Los amigos del maestro vinieron."

show rin basic_absent
with charachange

rin "Luego se dirigieron al pueblo para el almuerzo y me pidieron que fuera. Fue algo bueno que mis piernas dolieran tanto."


hi "¿Pero solo estarás atorada ahí? Eso no es bueno."

show rin basic_lucid
with charachange

rin "Solo esperaré hasta que pueda caminar de nuevo. Tendrá que ser tarde o temprano, si lo piensas por un rato."

rin "El maestro estaba feliz de que haya terminado el mural."

hi "Debería de estarlo."

show rin basic_awayabsent
with charachange

stop music fadeout 5.0

rin "Pero me pregunto si está terminado después de todo."

hi "¿Oh?"

show rin basic_deadpanupset
with charachange

rin "Ayer pensé que había hecho todo, pero ahora ya no estoy segura. Debería pintar más detalles. Quizás. Probablemente. Es muy difícil decidirlo."

"Terminado o no, el mural se ve genial a plena luz del día."

play music music_another fadein 2.0

scene bg mural at Transform(xalign=0.05)
with Dissolve(2.0)

"Varias partes del cuerpo humano, repetidas una y otra vez en una variedad salvajemente mutativa, mayormente desfiguradas, son el elemento principal."

"Son de apariencia tosca, como si hubieran sido colocadas sin pensarlo y pintadas de manera rudimentaria, pero se ha puesto una gran cantidad de reflexión y cuidado en todas y cada una de ellas."

show bg mural at Transform(xalign=0.25)
with charamove

hi "¿Acaso este tiene una rana saliéndole de la cabeza?"

rin "Es un pez dorado."

show bg mural at Transform(xalign=0.45)
with charamove

hi "¿Qué es eso?"

rin "No es nada."

show bg mural at Slide(0.45,0.45,.6,0.6,25.0, time_warp=acdc_warp)
with None

"En fin…"

"El muro es tan amplio que tengo que girar el cuello de un lado a otro para ver la pintura entera."

"Es difícil considerarla una sola pieza. Los elementos no parecen encajar juntos, pero supongo que crean algún tipo de todo."

"Abstracto como es, no tengo idea de qué se supone que está representando, pero se ve bien. Eso es suficiente para mí."

"Tomo asiento junto a Rin, apoyándome contra la pared como ella lo hace."

"Los alegres ruidos del festival se hacen cada vez más fuertes mientras más y más gente entra al campus."

"Los dormitorios están lejos de las atracciones más grandes en el edificio principal y de los puestos alrededor del patio, así que la mayoría de los visitantes no han encontrado el camino hacia aquí todavía."

show rin negative_spaciness_close at offscreenright
with None

show rin negative_spaciness_close at tworight
show bg mural at Transform(xalign=0.6)
with MoveTransition(3.0, factory=MoveFactory(time_warp=_ease_time_warp))

"Una expresión un tanto aburrida se asienta en el rostro de Rin, haciéndola verse despegada de todo lo que está sucediendo a su alrededor."

"Ella está excesivamente callada. Me pregunto si le dolerá algo."

hi "Entonces, ¿qué dijo la gente de artes sobre tu mural?"

show rin basic_deadpannormal_close at tworight
with Dissolve(1.5)

"Mi pregunta despierta a Rin de sus ensoñaciones. Perezosamente voltea la cara hacia mí."

show rin basic_deadpan_close
with charachange

rin "No estoy segura."

show rin basic_awayabsent_close
with charachange

rin "¿Creo que les gustó? Tal vez sí."

hi "¿Qué hay de ti? ¿Estás contenta con el mural? Porque de alguna manera participé en él, sería terrible si no estuvieses contenta."

"Rin ladea la cabeza, mordiendo su labio inferior."

show rin negative_sad_close
with charachange

rin "Creo que salió decentemente. No está mal pero tampoco está bien. Solo… es. Supongo que soy buena en tener la mente vacía."

hi "¿Puedo preguntar algo más? ¿Qué retrata la pintura en realidad? Pensé en ello el día de ayer, cuando dijiste que no representa nada."

hi "Pero eso es una falacia lógica, ¿no? No puedes hacer algo de la nada, ni siquiera arte."

show rin negative_annoyed_close
with charachange

"Rin frunce el ceño y vuelve la cabeza atrás, hacia las nubes."

rin "No lo sé. No soy muy buena explicando cosas. Es solo un mural; no hay nada especial en él. Ya lo dije."

"Suena molesta con mis preguntas."

rin "No sabía qué pintaría, así que decidí pintar tan solo un mural."

rin "Es un mural que retrata un mural."

show rin basic_deadpancontemplation_close
with charachange

rin "No, espera. Acabo de pensar una mejor manera de decirlo: Se retrata a sí mismo."

show rin basic_deadpannormal_close
with charachange

rin "Así que… su muralidad está al máximo, al menos hasta lo que puedo hacer, así que si piensas que tiene algún significado, creo ese es el mismo que este tiene."

"Eso no tiene sentido."

"Significado… Siento las comisuras de mis labios doblarse hacia arriba en una sonrisa que es apenas un poquito molesta."

stop music fadeout 5.0

scene mural all
with flash

"Nunca he entendido el arte en el significado más profundo de la palabra."

"Entiendo las bases, cómo el arte se supone que sea solo un medio para un intercambio de ideas y pensamientos."

scene bg mural at Slide(1.0,1.0,0.6,0.6,40.0, time_warp=acdc_warp)
with flash

"Sin embargo, nunca aprendí cómo debería interpretar una pieza de arte, de alguna manera descubrir lo que el artista tiene intención de decir a través de esta."

"Yo sé que no es ninguna habilidad especial, pero de alguna forma, mi cerebro nunca puede conectar el arte con cualquier cosa más que lo que veo. Todo lo que veo es un mural."

"Puedo admirar la habilidad técnica, después de todo incluso yo conozco la diferencia entre el mal arte y el arte mediocre; el arte mediocre y el buen arte."

"Pero eso es lo más lejos que puedo llegar, así que no me preguntes sobre significados, Rin."

"Su respuesta sí que me hizo reacio a preguntarle más acerca de ello."

hi "Así que, ¿qué vas a hacer cuando te pongas de pie?"

play music music_happiness fadein 4.0

scene bg mural at Transform(xalign=0.6)
show rin negative_spaciness_close at tworight
with flash

rin "Nada."

hi "¿Nada? Pero está el festival, ¿no quieres divertirte un rato?"

show rin basic_absent_close
with charachange

rin "Estoy bien así."

hi "No te gusta socializar mucho, ¿o sí?"

"Creo que estoy discutiendo más por ella que por mí mismo en este momento. No es que esté particularmente emocionado por el festival, tampoco; solo un poco intrigado por ver cómo es, y eso es todo."

"Su respuesta no es de sorprenderse."

show rin basic_awayabsent_close
with charachange

rin "No, no me gusta."

hi "Supongo que… a mí tampoco, después de todo."

show rin basic_deadpan_close
with charachange

rin "Deberías ir si quieres."

hi "Lo sé, pero puedo hacerte compañía. No estoy acostumbrado a todo esto aún, así que está bien tomárselo tranquilo."

hi "Aunque puedo irme, si quieres estar sola."

show rin basic_deadpannormal_close
with charachange

rin "Me agrada si estás aquí."

"Circulamos uno alrededor del otro con palabras, pero eventualmente terminamos en algún lugar. Que ella dijera eso me hace sentir extrañamente feliz, así que me quedo."

"Su presencia es algo que me agrada también. El aura extraña y cálida de serenidad que ella parece emanar hace que sea cómodo estar en silencio. Eso en verdad me agrada."

"Vemos a gente pasar, ambos en silencio, todos los demás charlando alegremente entre ellos."

"Los estudiantes están llevando a sus familias a los dormitorios para mostrarles sus habitaciones. Nos pasan a nosotros y al mural, quizás mirándolo una o dos veces."

"Les presto a ellos menos atención, y más a mi acompañante, tratando de darme una idea de cómo traspasar su críptico e ilegible rostro de pared."

show rin basic_awayabsent_close
with charachange

show rin basic_absent_close
with charachange

show rin basic_awayabsent_close
with charachange

"Los ojos de Rin se mueven velozmente de una persona a otra sin cesar a medida que pasan."

"¿Está esperando que la gente se detenga en el mural, tal vez con la secreta esperanza de que alguien comente sobre ello?"

"No creo que alguien pudiese asumir que ella es la artista. Solo estamos sentados aquí como un par de vagabundos, después de todo, y ella ni siquiera tiene manos."

"Me pregunto si es siquiera el estilo de Rin el buscar halagos. Ella parece tan distante."

"Más gente pasa, algunos de ellos apuntando sus dedos al mural, intercambiando palabras que no puedo entender. Alguien deja caer un cono de nieve sobre su zapato. Qué mal por él."

hi "A todo mundo parece gustarle."

"Lo sugiero tentativamente, arrojando un tema en el viciado aire de verano que nos separa."

"Rin no responde de inmediato, pero para ahora ya estoy habituado a su ocasional lentitud cuando debe de hablar."
"Es como si tomara grandes cuidados escogiendo sus palabras, lo cual es realmente increíble cuando consideras el revoltijo que sale de su boca."

show rin basic_lucid_close
with charachange

rin "Quería hacerlo de manera que simplemente puedas verlo sin pensar. Entonces me di cuenta de que no tiene ningún sentido. Así que se convirtió en una mezcla de esto y aquello."

show rin negative_spaciness_close
with charachange

rin "Desde lejos parece como que alguien vomitó una manada de mariposas sobre el muro. Lo cual es exactamente lo que esa molesta persona presidenta no quería. ¿Es esa la palabra esa?"

hi "¿Qué palabra?"

show rin basic_deadpannormal_close
with charachange

rin "Esa. ¿Cuál es la palabra para más de una mariposa?"

hi "¿Mariposas?"

show rin basic_deadpanupset_close
with charachange

rin "No, como una manada, o un banco, o un montón."

hi "Oh. No lo sé. ¿Una bandada, quizás?"

rin "Tal vez a la gente le guste el vómito de mariposa."

show rin negative_confused_close
with charachange

"Rin mira al mural, viéndose sorprendentemente infeliz."

rin "La mitad podría ser mejor."

show rin negative_annoyed_close
with charachange

rin "Usualmente me gustan los entremedios, pero este fue un dolor en el trasero. No literalmente, por supuesto… por otro lado, también tuve eso. Supongo que fue literalmente, después de todo."

hi "No seas tan crítica contigo misma."

show rin basic_deadpannormal_close
with charachange

"Ella me mira de modo extraño, pero se calla."

scene bg school_dormext_full at bgright
with locationchange

"Como por este punto empiezo a pensar si realmente debería irme y hacer algo más constructivo con mi domingo."

"Esta es la cumbre del fracaso social. Todo un día libre, un festival justo fuera de mi puerta, ¿y qué es lo que hago?"

"Sentarme aquí con Rin; dos espectadores con nada qué hacer salvo pensar qué pena es ser tan solo un espectador."

"Incluso reconociendo lo triste que es, no hago nada. No me levanto y me retiro para un día de diversión."

stop music fadeout 5.0

play sound sfx_rustling

centered "*chas chas*"

"…"

centered "*drrr*"

play sound sfx_rustling

centered "*chas*"

"…"

scene bg mural at Transform(xalign=0.6)
show rin negative_annoyed_close at tworight
with locationchange

"Rin se mueve inquietamente sin cesar, constantemente acomodando una pierna sobre la otra rodilla y luego de vuelta."


"Tiene una mirada muy irritada en su rostro."

hi "¿Sucede algo malo?"

show rin basic_deadpanupset_close
with charachange

rin "Sí. No. Sí."

scene bg school_dormext_full at bgright
show rin basic_deadpanupset:
    xpos 0.7 ypos 1.0 xanchor 0.5 yanchor 0.8
    easein 0.5 yanchor 1.0
with locationchange

"Ella repentinamente se pone de pie de un brinco. Es sorprendente, pensé que seguía inmóvil pero aparentemente ese no es el caso."

show rin negative_confused at tworight
with charachange

rin "Tengo que ir a encontrar a Emi o alguien, necesito algo de ayuda con algo."

hi "Yo puedo ayudarte."

show rin relaxed_nonchalant
with charachange

rin "No, está bien. Uno de nosotros tiene que quedarse aquí en caso de que algo ocurra."

hi "No seas ridícula. Nada siquiera remotamente interesante ha ocurrido desde que vine aquí, salvo ese tipo al que se le cayó el cono de nieve sobre el pie. Déjame ayudarte, ya que estoy aburrido."

hi "Así que, ¿qué es?"

show rin negative_annoyed
with charachange

"Los labios de Rin se aplanan uno contra el otro en una línea casi perfectamente horizontal."

show rin basic_lucid
with charachange

"Ella cierra los ojos y respira profundamente."

"Cuando abre los párpados la mirada terriblemente severa en sus ojos oscuros me toma por sorpresa."

play music music_rin fadein 0.5

show rin negative_angry
with charachange

rin "Hisao, tú tal vez no quieras escuchar esto, o tal vez sí, no lo sé; pero no tiene importancia e incluso si la tuviera no me estás dejando alguna opción."


rin "Estoy teniendo mi regla y necesito algo de ayuda al respecto. Sin embargo, no siento que nuestra relación esté aún al nivel donde pueda permitirte bajarme la ropa interior en el baño de las chicas, incluso si te ofrecieras."

rin "Es por eso que deberías quedarte aquí mientras yo voy y busco a Emi."

"Entretanto la sangre corre a mis mejillas como la marea creciente."

"Mi cerebro intenta buscar una respuesta desesperadamente, pero la única cosa en la que puedo pensar es cómo eso fue lo más coherente que he escuchado salir de la boca de Rin durante estos cuatro días que la he conocido."

hi "Sí."

hide rin
with charaexit

stop music fadeout 4.0

"No queriendo encontrar la mirada de Rin, volteo mi cara a un lado, pretendiendo ver a los padres de alguien."

"Desde el rabillo del ojo veo a Rin girar sobre sí y salir caminando sin más preámbulos."

"Me siento con ganas de esconderme bajo alguna roca."

"Me pregunto por cuánto tiempo se irá Rin… o si es que regresará."

scene bg mural at Transform(xalign=0.6)
with shorttimeskip

play music music_dreamy fadein 3.0

"Ella efectivamente regresa eventualmente, dando la impresión de aparecerse de la nada y sentándose de vuelta en donde estaba, enseguida de mí."

show rin basic_deadpannormal_close at Slide(0.8,0.5,0.7,0.5,1.0)
with Dissolve(1.0)

rin "Ya volví."

"Lo dice rotundamente, como si mi metedura de pata nunca hubiera ocurrido. Preferiría olvidar todo el problema también, así que me quedo callado."

scene bg mural_ss at Transform(xalign=0.6)
show rin basic_deadpannormal_close_ss at tworight
show rin_shadow basic behind rin:
    xpos 0.7 ypos 1.0 xanchor 0.5 yanchor 0.85
    easein 3.0 xpos 0.8 yanchor 0.9
with Dissolve(3.0)

"El tiempo pasa a un punto muerto y el Sol brilla desde lo alto del edificio principal. Me pega directamente en los ojos, pero solo los entrecierro en lugar de moverme."

"En un momento se torna doloroso mantener los ojos abiertos tan solo un poco, y mis sienes comienzan a doler."

hi "Me duele la cabeza. Creo que este día me dio jaqueca, ¿puedes creerlo?"

show rin basic_deadpan_close_ss
with charachange

rin "¿Tienes hambre?"

hi "¿Cómo está eso relacionado con el dolor de cabeza?"

show rin basic_deadpansurprised_close_ss
with charachange

rin "No lo está. Pregunto porque yo tengo."

"…"

"Su seriedad ajena a lo que la rodea derrite mi irritación con su ridiculez, y encuentro las comisuras de mis labios doblándose levemente hacia arriba de nuevo."

hi "¿Sabes qué? Yo también."

hi "Iré por algo de comida para los dos. ¿Qué quieres? Yo invito."

show rin basic_lucid_close_ss
with charachange

rin "No importa."

show rin basic_deadpannormal_close_ss
with shorttimeskip

"Al regresar con la comida, le doy una porción a Rin, tomando la otra para mí y atacamos la comida sin una palabra."

show rin negative_spaciness_close_ss
show rin_shadow negative at Transform(xpos=0.8,ypos=1.0,xanchor=0.5,yanchor=0.9)
with charachange

"Rin voltea hacia arriba, el tenedor colgándole de una de las comisuras de sus labios."

rin "¿Qué son las nubes? Siempre pensé que eran los pensamientos del cielo o algo así. Porque no puedes tocarlos."

hi "¿Pensabas así cuando eras una niña?"

rin "No, la semana pasada."

rin "Tal vez porque mis pensamientos se sienten como nubes de vez en cuando. Esponjosos y blancos y lentos."

rin "Como si el cielo estuviera en mi mente. Como si mi mente fuera el cielo."

hi "¿El cielo de tu mente?"

rin "Cierra tus ojos y piensa en cielo. No serás capaz de pensar en cualquier otra cosa hasta que te detengas."

scene black
with shuteye

"Lo intento. Funciona. ¿Magia?"

scene bg mural_ss at Transform(xalign=0.6)
show rin basic_deadpannormal_close_ss at tworight
show rin_shadow basic behind rin at Transform(xpos=0.8,ypos=1.0,xanchor=0.5,yanchor=0.9)
with openeye

"Al abrir mis ojos, veo a Rin estudiándome con los suyos. Se siente incómodo porque ella no dice nada. Me doy vuelta."

scene bg misc_sky_ss at Fullpan(20.0)
with locationchange

hi "Las nubes son agua. Agua evaporada."

hi "Sabes, dicen que casi toda el agua en el mundo será en algún momento de su existencia parte de una nube."

hi "Cada gota de lágrimas y sangre y sudor que sale de ti, será una nube. Toda el agua dentro de tu cuerpo también, irá hacia allá arriba en algún momento después de que mueras. Aunque puede tomar algo de tiempo."

rin "Tu explicación es mejor que cualquiera de las mías."

hi "Porque es cierta."

rin "Eso debe de ser."

"Sigo comiendo mi almuerzo antes de que se enfríe."

"El muro ofrece un poco de sombra bendita mientras el Sol da vueltas alrededor de la cúpula del cielo."

"Pero la tarde ya está dándole paso lentamente al anochecer, así que nuestro almuerzo se convierte más en una cena. O cualquiera que sea la palabra para una comida irregular como esta."

"A pesar de cómo decida nombrarla, sin duda que cae muy bien. No he comido un bocado desde hace mucho."

"…"

"Con mi apetito saciado, dejo salir un suspiro de satisfacción. Rin no se ha comido todo lo suyo pero también parece haber terminado de comer."

"Me recuesto, y absorbo el ambiente. El público ya se ha reducido, pero las actividades todavía siguen. Todos parecen estar disfrutándolo."

"¿Y por qué no? Es cálido, el tipo de día de verano perfecto cuando hace calor pero no demasiado para ser incómodo."

"El Sol pronto se pondrá. El tiempo en verdad voló."

scene bg mural_ss at Transform(xalign=0.6)
show rin basic_deadpannormal_close_ss at tworight
show rin_shadow basic behind rin at Transform(xpos=0.8,ypos=1.0,xanchor=0.5,yanchor=0.9)
with locationchange

hi "Hemos estado sentados aquí por seis horas."

show rin basic_deadpansurprised_close_ss
with charachange

rin "Así es."

show rin basic_deadpancontemplation_close_ss
with charachange

rin "¿Quieres hacer algo más ahora?"

hi "No, no realmente."

show rin basic_deadpannormal_close_ss
with charachange

rin "Yo tampoco."

show rin basic_lucid_close_ss
with charachange

"Ella se reacomoda y se recarga contra la pared, y sigo su ejemplo, relajando mi cuerpo."

"Durante varios minutos, nos sentamos ahí sin decir una palabra."

"Trato de sentir el humor de Rin por su comportamiento, la tensión de sus músculos, la diminuta expresión fugaz en su rostro. No sirve de nada. Es ilegible como siempre."

$ renpy.music.set_volume(0.5, 0.0, "ambient")
play music sfx_crowd_outdoors channel 6 fadein 1.0

scene bg school_dormext_full_ss
show crowd_ss
with locationchange

"El gentío se hincha por un lado y por otro, la gente charlando felizmente entre sí. Muy pocas personas prestan verdadera atención al mural, e incluso menos a nosotros."

"Jugueteo con algunas piedritas de por ahí sin prestar atención."

"El acto de hacer algo solo por hacer algo, la cumbre de la ociosidad."

"Centímetro a centímetro, el Sol se arrastra más y más bajo, hacia la línea formada por las copas de los árboles, cambiando el color del cielo cerca del horizonte de amarillo dorado a naranja y rojo mientras el momento de la puesta de sol se acerca."

"Siento como si mi estómago estuviera lleno de plomo después de comer tan pesado, pero la pared de ladrillo se siente sorprendentemente cómoda contra mi espalda."

"Trato de combatir el sentimiento de modorra que me abate, inútilmente."

scene black
with shuteye

stop music fadeout 4.0
$ renpy.music.stop(channel=6,fadeout=2.0)

with Pause(4)
$ renpy.music.set_volume(1.0, 0.2, "ambient")
play ambient sfx_fireworks fadein 1.0

scene bg misc_sky_ni
with openeye

"Despierto de un sobresalto."

"Un estallido bajo retumba a través del campus de la escuela. Imágenes remanentes de brillantes chispas destellan por mi vista como estrellas."

"Algo se levanta hacia los cielos desde la dirección del campo deportivo."

"Una estela de fuego le sigue detrás, hasta que una explosión de flamas rojas y amarillas ilumina el cielo en lo alto de la escuela con otro fuerte estallido."

show fireworks
with dissolve

"Fuegos artificiales."

"El destello de luz repentino contra el lienzo del cielo nocturno me despierta para que me percate de que, en realidad, ya está oscuro."

"¿Cuánto tiempo dormí? Me siento mareado y no puedo sentir mi brazo derecho."

"Al intentar flexionarlo, me doy cuenta del porqué."

play music music_twinkle fadein 1.0

show rin basic_lucid_close_ni:
    xpos 1.0 ypos 1.1 xanchor 0.5 yanchor 1.0
    easein 1.0 xpos 0.9
with Dissolve(1.0)

"Rin se está recargando pesadamente sobre mi hombro, a punto de caer sobre mi regazo."

"Está profundamente dormida, ni siquiera se desconcierta por los fuegos artificiales."

"Su boca está ligeramente abierta y sus ojos se encuentran tranquilamente cerrados. Un infantil y durmiente rostro inocente."

"Sacudo gentilmente a Rin con el brazo libre, intentando despertarla o, en su defecto, moverla de manera que mi otro brazo sea liberado de su presión."

"El rostro de Rin se contrae y sus párpados se cierran todavía más, como si se resistiese a despertar."

show rin basic_deadpanupset_close_ni at Transform(xpos=0.9, xanchor=0.5, ypos=1.1)
with charachange

"Gradualmente abre los ojos pero los mantiene a medio cerrar, dejando a la luz de los fuegos artificiales apenas colarse a través de sus pestañas para que sus verdes iris reflejen los brillantes destellos de las explosiones."

"Luego voltea hacia mí y frunce el ceño."

show rin basic_deadpan_close_ni
with charachange

rin "Solo un rato más, ¿está bien?"

"La voz de Rin es adormilada y lenta, dejando sus palabras; masculladas casi incomprensiblemente, pendiendo perezosamente en el aire."

"Parece que ella no está completamente enterada de la situación."

show rin basic_lucid_close_ni
with charachange

"La cabeza de Rin cae de nuevo en mi hombro y se recuesta sobre mí con todo su peso."

"Se acurruca contra mi costado, tratando de ponerse cómoda pero a la vez haciéndome sentir muy incómodo."

"Me vuelvo intensamente, casi dolorosamente, consciente del cálido cuerpo de Rin y del movimiento profundo y tranquilo de sus pechos contra mi brazo, su respiración pronto regresando a un ritmo regular."

"No puedo evitar admirar su don para dormir, o su tranquilidad mental para usar a alguien que ha conocido por menos de una semana como almohada."

"Los cohetes se levantan hasta el cielo uno a la vez, rompiendo en flores de rojo, verde y dorado, acompañadas por los “oohs” y “aahs” de la audiencia."

"Trato de empujar la desconcertante proximidad de Rin fuera de mi mente, pues ¿qué puedo hacer al respecto? Solo espero que su corto rato sea justamente eso."

"Uno a uno, los resplandecientes estallidos nacen y mueren en un parpadeo, coloreando la oscura noche en una constantemente cambiante pintura abstracta."

"Escucho los bajos estallidos de las explosiones y el silencioso respirar de Rin, intentando aclarar mi cabeza de la desorientación tras despertar."

"Afortunadamente, solo un rato más en verdad resulta ser solo un rato, y Rin despierta de su sueño y se levanta de nuevo antes de que los fuegos artificiales acaben."

show rin relaxed_sleepy_close_ni
with charachange

rin "Me quedé dormida."

show rin basic_awayabsent_close_ni
with charachange

show rin basic_lucid_close_ni
with charachange

show rin basic_awayabsent_close_ni
with charachange

"Finalmente abre sus ojos por completo y parpadea unas veces."

hi "Te quedaste dormida encima de mí. Dos veces."

show rin basic_absent_close_ni
with charachange

rin "¿No te gustó?"

hi "Ehh… bueno…"

show rin basic_absent_close_ni:
    ease 1.0 ypos 1.0

"A pesar de la tartamudez no concluyente, Rin se sienta derecha, alejándose de mí."

hi "Bueno, eres pesada."


"Es una mentira, no pesa casi nada, pero tengo que lanzarle una indirecta de vuelta, aun si es un golpe bajo. Mi falsa protesta falla en obtener reacción alguna ya que la atención de Rin es llevada hacia arriba, a los destellos de los fuegos artificiales."

show rin negative_spaciness_close_ni at Transform(xpos=0.9, xanchor=0.5)
with charachange

"Parece hipnotizada por el colorido juego de las explosiones."

"Una leve sensación de hormigueo va hacia arriba y abajo en mi brazo mientras la sangre comienza a circular de nuevo. Es desagradable pero me ayuda a deshacerme de este mareo."

"Más y más cohetes se levantan hasta el cielo, los colores brillantes de sus explosiones reflejándose desde las nubes."

"Ambos miramos los fuegos artificiales fijamente a través del dosel de los árboles, embelesados por el espectáculo."

"Tendríamos una vista mucho mejor del cielo si nos moviéramos tan solo un par de metros, pero ninguno de nosotros se molesta en siquiera sugerirlo."

show rin negative_worried_close_ni
with charachange

rin "En verdad me gustan los fuegos artificiales, incluso si verlos me hace sentir un poco triste, eso creo. Es como si quisieran tanto que los vieras que son ruidosos y brillantes, pero cuando alguien mira, ya se han ido."

show rin negative_sad_close_ni
with charachange

rin "Es como si ni siquiera fueran reales."

"…"

hi "Son reales, yo puedo decírtelo."

hi "Todo esto es… real, ¿sabes?"

hi "Si piensas en ello, nada dura mucho tiempo realmente. Incluso algo como mi vida o la tuya es solo un parpadeo en la historia de todo, como uno de aquellos cohetes. Puf, y nos hemos ido."

hi "Pero estamos aquí, ¿o no?"

"Sí, esta es la realidad. Rin, sentada junto a mí, los fuertes estallidos de los fuegos artificiales, el cielo vasto e ilimitado. Estas cosas son definitivamente reales, incluso si no permanecen aquí por siempre."

"Siento una calidez en mi interior, y me pregunto si es porque Rin se encuentra tan cerca de mí o es solo la sensación de estar vivo."

show rin negative_spaciness_close_ni
with charachange

rin "En verdad no sé qué debería decir ahora."

hi "Está bien… Quizás solo estoy hablando conmigo mismo."

hi "Pero sabes, los fuegos artificiales son bonitos… pero a fin de cuentas, ¿no es un poco tonto gastar tanto dinero en chispas bonitas que tan solo duran una fracción de segundo?"

show rin negative_sad_close_ni at Slide(0.9,0.5,0.7,0.5,1.0)
with None

show rin relaxed_doubt_close_ni at Slide(0.9,0.5,0.7,0.5,1.0)
with Dissolve(1.0)

"Rin arranca su mirada del espectáculo que sigue su curso y se inclina hacia atrás, viéndome con una cara de repulsión."

rin "Guau, nunca esperé que tú fueras tan cínico."

hi "Cínico es una palabra muy dura. Más que eso, pienso en mí mismo como un realista."

show rin relaxed_surprised_close_ni at tworight
with charachange

rin "¿No es realista solo la palabra que usa un cínico para llamarse a sí mismo?"

stop ambient fadeout 1.0
hide fireworks
with dissolve

"El último cohete se despide con un estallido de plateado y azul, dejando el campus en un silencio inquietante por un momento, hasta que la gente comienza a caminar hacia la puerta principal, como una manada de ganado."

"Espirales de humo se mueven a la deriva hacia los dormitorios desde el campo deportivo. El olor acre y sulfuroso de la pólvora que llevan consigo se siente como si se pegara a mi cabello y ropa."

hi "¿Eso fue todo?"

show rin negative_spaciness_close_ni
with charachange

rin "Eso pienso."

scene bg school_dormext_full_ni
with locationchange

"Me pongo de pie y estiro mi espalda adolorida. Dormir sobre una pared de ladrillo no fue una muy buena idea, después de todo."

show rin negative_spaciness_ni:
    xpos 0.7 ypos 1.0 xanchor 0.5 yanchor 0.8
    easein 1.0 yanchor 1.0
with Dissolve(1.0)

show rin basic_absent_ni at tworight
with charachange

"Rin también se pone de pie y se vuelve hacia mí, con una mirada expectante en sus rasgos cansados."

"Aunque parece tener problemas enfocando sus ojos, está viéndome directamente, algo que siento no ha ocurrido muy seguido en la pasada semana."

hi "Ahh… así que…"

"De pronto me doy cuenta de que hemos estado casi en una cita, como por accidente. Incluso si no hicimos nada."

"Pero no lo fue… así que, ¿por qué la sangre corre hacia mis mejillas y comienzo a tartamudear?"

"No sé qué debería decir, especialmente ya que Rin parece estar esperando a que yo diga algo, pero afortunadamente ella resuelve mi problema por mí."

show rin basic_deadpannormal_ni
with charachange

rin "Buenas noches, Hisao."

hide rin
with charaexit

"Ella me da una mirada prolongada más, midiéndome de pies a cabeza, da vuelta sobre su talón y se marcha, desapareciendo entre la muchedumbre."

stop music fadeout 7.0

"…"

hi "Está bien… Buenas noches."

"Me quedo de pie ahí, dando mi respuesta al aire refrescante de la noche."

"Suspiro."

"El festival resultó no ser nada como lo que esperaba."

"Terminé pasando todo el día en un solo lugar con Rin, a pesar de que ninguno de los dos acordara ni sugiriera que hiciéramos algo."

"Es solo que no tenía nada mejor que hacer y, evidentemente, tampoco ella."

"La calidez de Rin perdura por un momento más en mi cuerpo antes de desaparecer en la noche."

window hide




label es_A41b:



scene bg school_gardens
with shorttimeskip

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_crowd_outdoors fadein 0.5
play music music_soothing fadein 0.5

"Después de comprar un plato de plástico de takoyaki de un puesto perteneciente al grupo contiguo al nuestro, tomo asiento en uno de los jardines escolares y observo a la gente pasar mientras lentamente mordisqueo el objeto más bien insípido."

"Supongo que no debo quejarme. Es mejor que nada y no costó demasiado."

"Mientras miro hacia la escuela, observar a la gente ir y venir prueba ser una forma sorprendentemente entretenida de pasar el tiempo mientras como."

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

show bg school_courtyard
show crowd
with locationchange

"Pequeños niños acompañados de sus padres o abuelos corretean entre el alboroto de evento a evento; una mano arrastrando a su compañía y la otra sosteniendo un inmenso y coloreado bocadillo."

"No puedo evitar notar que el rango de edad entre las personas aquí está inclinado hacia la gente mayor, algo que también había notado cuando estaba caminando por el pueblo."


"Este debe ser uno de esos pueblos donde la única gente que queda son esos que vivieron aquí su vida entera y se niegan fervientemente a irse, y esos que quieren vivir fuera el resto de sus días en uno de los cada vez más escasos lugares tranquilos."

"Supongo que eso también proporciona una forma de explicar lo conservadora que la cultura de la escuela Yamaku parece ser."

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

scene bg school_gardens at Fullpan(8.0)
with locationchange

"No es que me moleste siquiera un poco. Como que me agrada lo calmados que Yamaku y sus alrededores son."

"El calor, sin embargo, es algo completamente distinto. Sentarme en un lugar por tanto tiempo ha enfocado mi mente en lo fastidiosamente húmedo que se está poniendo, ahora que la parte más caliente del día ha llegado."

"Mejor me voy moviendo si yo—{w=.5}{nw}"

play sound sfx_warningbell

"¡Gah!"

"El sonido de las campanas del carillón me toma completamente por sorpresa mientras me levanto, una reacción compartida por unas pocas de las personas paseándose también."

"El sistema de audio chasquea al encender después de que las campanas terminan de repicar."

"Su antigüedad se deja ver mientras el director hace un anuncio apenas entendible a través de este, iniciando oficialmente el festival que está prácticamente en plena marcha."

"Es bastante divertido contrastar las placenteras sonrisas de la gente mayor con los alternadamente dolidos y cansados gestos de los jóvenes a su cargo. Los estudiantes, por otro lado, parecen prestarle poca atención."

"No obstante, conforme el discurso finalmente termina, todos son unidos en educados —si no demasiado entusiastas— aplausos, y después vuelven a lo que hacían."

"Deslizando una mano en mi bolsillo para parecer tan relajado como sea posible, casualmente miro alrededor buscando algo que hacer."

"… Es un tanto difícil ver muy lejos con toda esta gente alrededor."

"Decido recurrir a una probada y fiable regla: ve donde todos los demás parecen estarse amontonando. Justo ahora, ese es el patio de la escuela y sus alrededores."

play sound sfx_can_clatter

"Tirando el plato usado en un bote de basura, me abro camino hacia el edificio de la escuela."

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene bg school_courtyard
show crowd
with locationchange

"Ver el número de puestos alrededor del perímetro del edificio de la escuela me sorprende. Bastantes de los grupos deben haber optado por tener múltiples puestos."

"Mientras decido cuál visitar primero, alcanzo a ver una pancarta familiar con un patrón azul en el borde y texto rojo."

"El puesto de Lilly es tan buen lugar como cualquier otro para empezar. Tengo curiosidad de cómo le está yendo, después de todo el trabajo que ella y su grupo han estado haciendo para él."

$ renpy.music.set_volume(0.5, 2.0, channel="ambient")

scene bg school_stalls2 at Fullpan(8.0, dir="left")
with locationchange

"Dando un paso hacia él, comienzo a ver por qué al grupo le tomó tanto tiempo organizar todo."

"Fácilmente dos veces más ancho que cualquiera de los otros puestos y con equipo de cocina disperso por todos lados, es más cercano a un restaurante al aire libre que a un evento de festival."

"Mientras un estudiante frente a mí toma un tazón de fideos y se marcha, camino hacia el mostrador."

"La chica tras él luce bastante exasperada, y me pide esperar un momento antes de desaparecer debajo del mostrador."

"Aprovechando el momento, doy una mirada rápida alrededor."

"El vapor parece estar elevándose de todos lados, mientras cacerolas y ollas hierven a fuego lento a lo lejos. Los estudiantes más ciegos están desempacando ingredientes mientras son ayudados por alguien quien es probablemente la maestra del 3-2."

"No toma mucho para descubrir a Lilly entre ellos, hablando con la maestra mientras rápidamente cuenta las cajas y paquetes con sus dedos."

"Por su expresión y el hecho de que la maestra y ella parecen estar en un estado de ligera confusión, tal parece que ha habido algún problema en la coordinación."

"Antes de que pueda observar por más tiempo, la chica tras el mostrador se aparece otra vez, solo para ver atrás y preguntar dónde está la caja de repuesto."

"Lilly se detiene por un momento, antes de que ella y la chica cambien lugares en el mostrador y la maestra rápidamente se aleje hacia algún lugar."

stop music fadeout 2.0

show bg school_stalls2 at left
show lilly basic_smileclosed at center
with charaenter

li "Perdón por eso, estamos teniendo algunos problemas. ¿Qué desea ordenar?"

"Me toma un segundo recordar a qué había venido aquí. Mis ojos rápidamente se precipitan a un lado a leer el menú situado en el mostrador."

hi "Oh, umm, supongo que un poco de… ¿sopa de miso?"

show lilly basic_surprised
with charachange

li "Ah, ¿ese es Hisao?"

hi "Síp. Parece que estás bastante ocupada."

play music music_ease fadein 6.0

show lilly basic_weaksmile
with charachange

"Su rostro no hace sino confirmarlo pues deja caer su fachada de mesera."

li "En algún punto del camino, nuestra orden quedó mezclada. Estamos tratando de arreglarlo ahora, pero tal parece que solo tenemos la mitad de lo que necesitábamos."

hi "¿Servir porciones más pequeñas no ayudaría a sobrellevar el problema?"

show lilly basic_sad
with charachange

li "Parece que eso es lo que tendremos que hacer, aunque desearía que no lo hiciéramos. El hecho de que casi la mitad del grupo se ha ido no ayuda, tampoco."

"Doy una mirada tras ella para ver cuánta gente está de hecho operando en el puesto."

"No son más que unos ocho."

hi "¿Entiendo entonces que ese es el porqué tu maestra se fue?"

show lilly basic_weaksmile
with charachange

li "Así es. Ella va a intentar reunir a unos pocos más de nuestros compañeros de clase para ayudar."

"Al escuchar el sonido de pasos detrás de mí, miro furtivamente hacia atrás para encontrar una pareja de ancianos tomando su lugar en la fila. Supongo que mejor dejo de entretenerme y charlar."

hi "Aquí está el dinero por la sopa."

show lilly basic_smile
with charachange

li "Sopa… oh, cierto, sale enseguida."

"Lilly gira y pide un tazón de sopa mientras entrego el dinero por esta."

show lilly basic_reminisce
with charachange

"Tomando las monedas en su palma, no puedo evitar sino notar lo eficientemente que las cuenta con sus largos, pálidos dedos. Eventualmente satisfecha de que he entregado el cambio correcto, ella lo pone en una pequeña bandeja de metal."

show lilly basic_smileclosed
with charachange

"No toma mucho antes de que la sopa sea hecha y cuidadosamente entregada a ella, después de lo cual ella gira y subsecuentemente me la pasa a mí."

hi "Gracias. Volveré para dejar el tazón."

show lilly basic_smile
with charachange

li "Gracias, Hisao. Oh, una cosa más. ¿Has visto a Hanako?"

hi "Hanako… no, hoy no. ¿Por qué?"

show lilly basic_sad
with charachange

"Ella da un pequeño suspiro de absoluta decepción."

li "Está bien. Solo me estaba preguntando qué estaba haciendo ella para el festival."

show lilly basic_weaksmile
with charachange

li "Volverás cuando hayas terminado, ¿entonces?"

hi "Seguro. Estaré alerta buscando a Hanako, también."

li "Gracias, Hisao."

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene bg school_courtyard
show crowd
with locationchange

"Me marcho del local y encuentro un asiento, acunando cuidadosamente el humeante tazón de madera entre ambas manos."

"Comparado a las croquetas de antes, esto es realmente bueno. Un poco frío comparado a lo que probablemente debería estar, pero el sabor es suficiente para compensar eso razonablemente bien."

"Mientras bebo, no puedo sino sentirme un poco culpable por no estar involucrado en el festival como los otros."

"En verdad no hay más remedio, considerando que fui traído a esta escuela hace solo una semana, pero aun así pesa bastante en mi mente."

"Eso, y el hecho de que unos pocos estudiantes no parecen realmente estar disfrutando del festival tanto como los visitantes."

"Eventualmente termino mi tazón y me voy hacia el puesto, para dejarlo ahí."

"Considerando que parece no haber fila en absoluto, me tomo mi tiempo para llegar ahí."

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

scene bg school_stalls2
with locationchange

"Parece que la misión de la maestra rindió frutos: ahora hay más de una docena de estudiantes ayudando, y mucho del desempaque ya se ha hecho."

"A pesar de que la mayoría de ellos parecen bastante relajados mientras trabajan, Lilly aún parece estar algo estresada."





label es_A41a:


stop music fadeout 4.0

"… Cierto. Ya sé lo que haré. Aun si es solo una persona, haré el festival más agradable para ella."

"Mientras coloco el tazón en el mostrador, llamo a Lilly."

show lilly basic_smile at center
with charaenter

li "Ah, Hisao. ¿Lo trajiste de vuelta?"

hi "Claro, aquí está."

hide lilly
with charaexit

"Lo deslizo hasta sus manos, y ella lo pasa a alguien que está aparentemente en la tarea de limpieza. Considerando que no los vi aquí antes, es probablemente un castigo por su tardanza."

hi "Oye, ¿Lilly?"

show lilly basic_smileclosed at center
with charaenter

"Ella se anima y regresa al mostrador al oír mi voz otra vez, dándose cuenta de que estoy aún aquí."

hi "¿Quieres ir a ver algo más del festival?"

play music music_another fadein 0.5

show lilly basic_pout
with charachange

"Ella infla sus mejillas en desaprobación. Se ve un tanto lindo, y en completa contradicción a su usualmente reservada naturaleza."

"Me toma unos segundos dar con lo que está causándole conflicto. Uups."

hi "Ah… emm, no quise…"

show lilly basic_giggle
with charachange

"Lilly me sonríe, exponiendo su broma por lo que es."

li "Aún no estás acostumbrado a la escuela, ¿o sí?"

"Me atrapó."

show lilly basic_reminisce
with charachange

li "Aun así… siento que necesito quedarme aquí con nuestro puesto. Ha tomado hasta justo hace un rato tener todo desempacado."

"Supongo que su renuencia no debe sorprenderme demasiado, considerando cuánto trabajo ha puesto en esto."

hi "Sin embargo, todo parece estar marchando bien ahora. Además, has conseguido ayuda extra, de todas formas."

show lilly basic_surprised
with charachange

"Un chico que estaba a mitad de cocinar unos fideos de soba gira hacia nosotros, sonriendo."


"Estudiante" "Vamos Lils, te has ganado un descanso. Podemos hacernos cargo del fuerte, por ahora."

show lilly basic_displeased
with charachange

li "Si dices que está bien, supongo que lo está…"

show lilly basic_reminisce
with charachange

li "Pero, si necesitan ayuda en algo—"

"Estudiante" "Entonces te hablaremos. Anda, estaremos bien."

hide lilly
with charaexit

"Lilly finalmente da por vencida su resistencia mientras él agita una espátula hacia ella. Ella siente su camino alrededor de la parte trasera del puesto, y toma su bastón en el camino."

"Supongo que lo primero que debemos hacer es buscar a Hanako. Lilly parece un tanto preocupada por ella, y dudo que ella sea el tipo de persona que disfruta revolviéndose en las multitudes así, tan solitaria."

hi "Entonces, supongo que debemos buscar a Hanako. ¿Primero en dónde?"

show lilly cane_reminisce at center
with charaenter

li "Hmm…"

"Los dos nos quedamos callados pensando por un momento."

hi "¿Tal vez está en su dormitorio?"

li "Lo dudo. Ella no tiene muchas cosas ahí, así que no tendría nada que hacer."

show lilly cane_satisfied
with charachange

li "… ¡Ah! ¿La biblioteca?"

"Tan buen lugar como ninguno para buscar a una lectora ávida, supongo."

hi "Será la biblioteca. Entonces revisaremos ahí primero."

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")

scene bg school_lobby
with locationskip

"Además de los apagados sonidos de la muchedumbre colándose desde afuera, la parte interior de la escuela parece casi desierta."

"Con el fin de asegurarse de que todos tenían suficiente espacio, supongo que los eventos fueron organizados para realizarse afuera, en el campus de la escuela."


"Definitivamente es bastante amplio, comparado con los estándares de cualquier otra escuela."

show lilly cane_smileclosed at center
with charaenter

li "Está agradable y tranquilo aquí, ¿no?"

hi "Seguro. Mucho mejor que el ajetreo y el bullicio de afuera."

stop ambient fadeout 3.0

scene bg school_staircase2
with locationchange

"Nos tomamos nuestro tiempo y lentamente atravesamos caminando el primer piso de la escuela, eventualmente alcanzando las escaleras que van al segundo piso."

scene bg school_hallway2
show lilly cane_smileclosed
with locationchange

"No puedo sino notar cómo Lilly anticipa cada puerta y obstáculo, su bastón permaneciendo inmóvil y su mano deslizándose por los rieles del pasillo."

hi "Realmente conoces bien la escuela, ¿o no?"

show lilly cane_smile at center
with charaenter

"Ella sonríe y asiente al momento."

li "He estado aquí por ya unos años, así que sé dónde está todo."

show lilly cane_sad
with charachange

li "Sin embargo los dormitorios aún me hacen tropezar, algunas veces. No he estado ahí por tanto tiempo, y no están tan bien dispuestos como el edificio principal."

li "Si recuerdo correctamente, solían ser edificios sin usar antes de ser renovados y usados como dormitorios."

"Eso explica por qué los dormitorios de hombres y mujeres lucen diferentes desde fuera, y por qué sus habitaciones parecen un tanto inusuales para cuartos de dormir."

"Había asumido que ella había estado viviendo en los dormitorios desde que empezó a asistir a la escuela, pero ahora recuerdo lo que dijo ayer."



hi "Es cierto, mencionaste eso antes."

hi "Había asumido que la mayoría de los estudiantes vivían aquí una vez que se matriculaban. Muchos de ellos parecen hacerlo, en cualquier caso."

show lilly cane_reminisce
with charachange

"La expresión de Lilly se vuelve algo más difícil de leer, mi interrogatorio evidentemente tocando un punto delicado."

li "Bueno… Cómo podría decirlo…"

show lilly cane_weaksmile
with charachange

li "Todos… tienen sus motivos."

"Algo me dice que una de esas personas con “motivos” es Hanako, por eso su cautela con respecto a una respuesta. Mi propio predicamento es otro más de tales casos."

"Creo que es una decisión que cada uno aquí debe hacer por sí mismo… o, en mi caso, que la hagan por ellos."

hi "No puede evitarse, supongo. Al menos Yamaku en sí parece un buen lugar."

show lilly cane_smile
with charachange

li "Es bueno escucharte decir eso. Había pensado que estaba comenzando a desagradarte."

hi "Pero, ¿qué hay de ti?"

show lilly cane_surprised
with charachange

"Mi reversión a la declaración de Lilly la toma por sorpresa."

li "He estado aquí por un tiempo, así…"

hi "No es eso. Es solo que lucías bastante deprimida con respecto a Akira."

show lilly cane_smileclosed
with charachange

li "Hmm~"

hi "¿Qué hay con esa mirada?"

show lilly cane_smile
with charachange

li "Akira está tomada. Lo siento, Hisao."

"Lilly nunca ve lo rápido que mi palma llega a mi rostro por su maliciosa acusación."

hi "Oye, estaba preocupado por ti. Esa no es la forma de responder a la inquietud."

show lilly cane_cheerful
with charachange

"Mientras ella sonríe divertida, damos la vuelta a la esquina del pasillo y entramos a la biblioteca."

scene ev hana_library_read_std
with locationskip

"Cuando lo hacemos, no es difícil divisar a Hanako, considerando que la habitación está completamente libre de otras personas."

scene bg school_library
with locationchange

"Dado que no hay personal por aquí, supongo que no hay necesidad de prestar atención a las reglas usuales de la biblioteca. La llamo desde lejos."

hi "Oye, Hanako."

show lilly cane_surprised at center
with charaenter

li "¿Hanako está aquí?"

"Al escuchar nuestras voces, la cabeza de Hanako salta desde detrás de un libro, probablemente el mismo que había estado leyendo el viernes."

show lilly cane_surprised at twoleft
show bg school_library at bgleft
with charamove
show lilly cane_smile at twoleft
show hanako basic_normal at tworight
with charaenter

ha "¿Hisao… Lilly?"

hi "Simplemente pensamos en pasar por aquí. Lilly acaba de arreglárselas para escapar del puesto de fideos, con un poco de ayuda."

show lilly cane_pout
with charachange

li "Eso no fue realmente un escape…"

show hanako emb_downsmile
show lilly cane_surprised
with charachange

"Hanako suelta una pequeña risilla, sorprendiéndonos a ambos por un momento."

show hanako basic_bashful
with charachange

ha "Acabo de pensar que… Lilly podría no estar disfrutando el festival."

hi "Bueno, ahora podemos disfrutarlo juntos, ¿cierto?"

show lilly cane_smileclosed
with charachange

"Las dos asienten felizmente antes de que salgamos de la biblioteca y nos dirijamos a las festividades."

stop music fadeout 2.0

scene bg school_stalls1_ni
with shorttimeskip

$ renpy.music.set_volume(0.5,0.0, "ambient")

play ambient sfx_cicadas fadein 0.3

"Le entrego algo de cambio a la chica tras el mostrador, y tomo las dos tazas de poliestireno con té. Trato de acentuar mi reverencia un poco para compensar por el hecho de que ella es obviamente sorda."

"Ahora que lo pienso, probablemente debí haber pedido ayuda en lugar de dejar a aquellas dos en el jardín mientras compraba las bebidas."

"Tratar de equilibrar las dos tazas de té caliente (para ellas) y una lata de café (para mí, salida de una máquina expendedora) no es precisamente fácil."

"Sin embargo, con algunas maniobras cuidadosas, logro mantener todo estable y vertical mientras camino a la banca donde Lilly y Hanako están descansando y charlando."

scene bg school_gardens2_ni
show lilly basic_smileclosed_ni at twoleft
show hanako basic_distant_ni at tworight
with locationchange

"Es de hecho un lugar bastante bueno. Alumbrado solo por la luz de luna, está apartado a alguna distancia de los eventos principales."

"Comparado a lo caluroso que había estado durante el día, este lugar también es placenteramente fresco ahora."

"No es que importe mucho. La mayoría de los visitantes se ha retirado a áreas que están ya sea cercanas a los fuegos artificiales, o más arriba en la colina para ver la aparentemente planeada exposición."

show lilly basic_smile_ni
with charachange

li "Bienvenido de vuelta, Hisao."

show hanako basic_normal_ni
with charachange

"Sus oídos son buenos. No estoy exactamente cerca e incluso Hanako no me había notado."

hi "Aquí lo tienen. Disculpas si es instantáneo, pero es todo lo que han dejado para ahora."

"Hanako cuidadosamente toma una taza de mi mano derecha, y gentilmente coloco la otra en las manos extendidas de Lilly."

show hanako basic_smile_ni
show lilly basic_smileclosed_ni
with charachange

li "¿Disfrutaste el festival entonces, Hisao?"

hi "Seguro, fue bastante divertido."

"Una respuesta honesta. Mucha de la comida podrá haber sido de algo baja calidad, pero fue muy divertido al final, especialmente con Hanako y Lilly."

"De hecho, creo que ellas habrán disfrutado aun más que yo. Con ambos, Lilly y yo por ahí, mucha de la naturaleza apartada de Hanako alrededor de otros disminuyó lo suficiente para que ella pudiera disfrutar."

stop ambient fadeout 1.0

$ renpy.music.set_volume(1.0,0.0, "ambient")

play ambient sfx_fireworks
play music music_twinkle fadein 12.0

scene bg misc_sky_ni
show fireworks
with dissolve

"Mientras nos sentamos bebiendo, el silbido del primer juego pirotécnico suena antes de explotar en un vibrante baño de azul contra el cielo nocturno, anunciando el principio del fin del festival."

"Se pueden escuchar los gritos entusiastas de la multitud dispersa por los patios de la escuela celebrándolos."

"Por minutos interminables, Hanako y yo miramos los fuegos artificiales sobre nuestras cabezas mientras Lilly felizmente los escucha con sus ojos cerrados."

"Rojo, verde, amarillo, con forma de estrella, circulares y en patrones, y todo tipo de formas y colores llenan el aire, uno tras otro, y danzan a través del cielo."

"Ningún lugar cerca de donde vivía hace tan espléndidas exhibiciones. Festivales como este eran cosa del pasado en un área metropolitana así."

"Estar viendo tal espectáculo con ellas dos… es probablemente lo más feliz que he estado en un largo tiempo."

scene bg school_gardens2_ni
show lilly basic_weaksmile_ni at twoleft
show hanako basic_distant_ni at tworight
show fireshine
with charachange

li "Así que… eso es todo. El festival al fin está terminando."

hi "Sin duda."

"Ella da un delicado, nostálgico suspiro."

show lilly basic_concerned_ni
with charachange

li "Por mucho que me podría quejar acerca de todas las cosas que tenemos que hacer, aún es triste que nos tendremos que graduar antes del próximo festival de Yamaku."

show lilly basic_concerned_close_ni
with characlose

"Camino al frente y me coloco al lado de Lilly, descansando gentilmente una mano en su hombro."

hi "No te preocupes. Aún tenemos el Tanabata más tarde en el año, ¿cierto?"

show lilly basic_smile_close_ni
with charachange

li "Estás en lo cierto. Sería agradable ir ahí cuando llegue."

"Pasan minutos de silencio, con solo los sonidos de los fuegos artificiales para ser oídos."

"Ver a ellas dos me recuerda aquel consejo que Lilly me había dado mientras caminamos hacia el pueblo juntos."

"“Atesora la oportunidad de hacer nuevos amigos”, ¿eh?"

hi "Oye, ¿Lilly?"

show lilly basic_smileclosed_close_ni
with charachange

"Ella gira su cabeza ligeramente para mostrar que está escuchando, la mirada de Hanako aún firmemente fija en los fuegos multicolor reventando en lo alto."

hi "¿Te molestaría si me uno a ustedes dos para el té de vez en cuando?"

"La sonrisa en su rostro es más que suficiente para ver su respuesta."

show lilly behind_cheerful_close_ni
with charachange

li "Sería un placer, Hisao."

stop music fadeout 2.0
stop ambient fadeout 2.0
window hide




label es_A42:





scene bg school_stalls2
with None

show lilly basic_reminisce at center
with charaenter

"Lilly no luce del todo impresionada, y realmente no puedo culparla."

"Además de sus problemas con su puesto, aún parece estar preocupada por Hanako."

"No puedo realmente ayudarla con lo primero, así que supongo que la única forma en que puedo ayudar es tratando de sacar de su mente a nuestra tímida amiga mutua."

"Colocando el recipiente de vuelta en el mostrador, llamo a Lilly."

hi "Oye, Lilly, no te preocupes por Hanako. Iré a encontrarla para pasar el rato con ella, ¿está bien?"

show lilly basic_weaksmile
with charachange

"Puedo ver el alivio escrito claramente en el rostro de Lilly."

li "Gracias Hisao. Y si ves a cualquiera de mi clase, ¿podrías decirle que vuelva aquí por favor?"

hi "Lo haré. Que la pases bien. Y asegúrate de tomar un descanso, ¿está bien?"

show lilly basic_smile
with charachange

li "Lo haré si puedo. Nos vemos después, Hisao."

stop music fadeout 10.0
$ renpy.music.set_volume(1.0,1.0, "ambient")

scene bg school_courtyard
show crowd
with locationchange

"Dejo a Lilly en el puesto y me alejo en busca de Hanako."

"En cierta forma, me siento mal por dejarla con las multitudes, pero inclusive si ella estaba claramente bajo presión, no puedo evitar sino pensar que está disfrutando de sí misma."

stop ambient fadeout 0.5

scene bg school_hallway2
show crowd
with locationskip

play ambient sfx_crowd_indoors fadein 0.5

"Los pasillos están abarrotados con multitudes en movimiento serpenteando por todo el festival."

"Si hay una cosa que sé sobre Hanako, es que ella no estará en ningún lugar cercano a esto."

"Y con los estudiantes mostrando a sus amigos y familiares sus dormitorios, también dudo que ella vaya a estar allá."

"Siguiendo ciegamente mi intuición, me muevo contra la corriente de la multitud."

"Por suerte, esta multitud parece ser ligeramente menos festiva que la usual multitud de festival; asumo que esto está fuera de consideración para el cuerpo estudiantil."

stop ambient fadeout 5.0

"Una vez que fuerzo mi paso a través de las masas, no toma demasiado para que finalmente ya no quede nadie."

hide crowd
with Dissolve(2.0)

"Esto no es sorpresa, dado que estoy parado frente a la biblioteca."

"Incluso los más entusiastas de los estudiantes no se molestan en mostrar a nadie esta sección de la escuela."

play music music_happiness fadein 2.0
scene bg school_library
with locationchange

"Conforme entro a la biblioteca, el ruido del festival se debilita a un apagado ruido de fondo, y pronto estoy en el área de lectura en la parte trasera de la habitación."

"Detrás de uno de los escritorios particionados veo la parte de arriba de una cabeza, con lacio, y oscuro cabello que llama mi atención."

hi "Oye, Hanako. Tuve el presentimiento de que te encontraría aquí…"

show hanako def_shock:
    xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 0.9
    easein 0.5 yanchor 1.0
with charaenter

"La cabeza salta un poco asustada antes de lentamente atisbar sobre la partición."

ha "¿Hi-Hisao?"

hi "Oye. Lilly está muy ocupada, así que me envió a buscarte."

show hanako basic_normal at center
with charachange

ha "O-oh. ¿Quieres sentarte?"

hi "De hecho, siento un poco de hambre. ¿Te gustaría que vayamos por algo de comer de uno de los puestos?"

show hanako defarms_worry
with charachange

ha "Em… yo… yo traje algo de comida así que…"

"No debería de sorprenderme, pero valió la pena intentarlo. Esperar que ella saliera hoy era algo muy improbable."

hi "¿Qué opinas de que comamos en el cuarto de té? Pasé por ahí en mi camino acá, y no había nadie por los alrededores."

hi "Podemos hacer un poco de comida ahí, y será un poco más cómodo. ¿Qué dices?"

show hanako cover_distant
with charachange

ha "S-seguro. Vamos."

show hanako basic_distant
with charachange

"Hanako cierra su libro y lo guarda con deliberados y practicados movimientos."

hi "¿Lista para ir?"

show hanako basic_normal
with charachange

ha "S… sí."

stop music fadeout 2.0

scene bg school_hallway2
with locationchange

"Caminamos lado a lado desde la biblioteca al cuarto de té."

"Como era de esperarse, apenas hay un alma por los alrededores."

"Si no fuera por los murmullos a través de las paredes, no podrías darte cuenta de que hay un gran festival llevándose a cabo afuera."

show hanako emb_downtimid at tworight
with charaenter

"Hanako lleva su mochila con ambas manos y se enfoca solo en el piso frente a ella."

show hanako emb_downsmile
with charaenter

show hanako emb_downtimid
with charaenter

"De vez en cuando, ella parece modificar su andar un poco y dar pasos ligeramente más pequeños."

"La primera vez que sucedió, no le di importancia, pero pronto noto que lo hace regularmente."

hi "¿Estás bien?"

show hanako defarms_worry
with charachange

"Ella detiene de golpe su andar."

ha "¿Q-qué?"

hi "No lo sé… parecía como que te estabas tropezando o algo…"

play music music_another fadein 0.5

show hanako emb_blushing
with charachange

"Un rubor rosa aparece en sus mejillas y su mirada regresa al piso."

show hanako emb_downtimid
with charachange

ha "Es… no es nada."

hi "¿Sabes?, cuando dices “nada” de esa forma, las personas se sienten con necesidad de hacer más preguntas."

"Por un segundo no creo que ella vaya a contestar."

"Preparado para dejarlo pasar, por poco vuelvo a caminar, cuando…"

show hanako emb_emb
with charachange

ha "Es un… un juego."

hi "¿Juego?"

show hanako emb_downsmile
with charachange

ha "¿Ves… ves el piso aquí?"

"Qué pregunta más extraña. El piso luce justo como cualquier otro piso; cubierto en esos azulejos hechos de cuadros de linóleo."

"Nada digno de mención."

hi "Bueno, sí. ¿Qué hay con ello?"

show hanako emb_downtimid
with charachange

ha "Algunas veces… cuando no hay nadie alrededor… solo piso los más oscuros…"

"La voz de Hanako se apaga conforme su explicación continúa, hasta que apenas puedo escuchar su voz entre el fiero silencio del pasillo vacío."

hi "¿Los más oscuros?"

"Arrastrando su pie, Hanako dirige la punta de su zapato a un mosaico que es apenas un tono más oscuro que los demás."

show hanako emb_downsmile
with charachange

ha "Co-como estos."

hi "Oh, claro, ¿entonces estos no están bien?"

"Indico un mosaico cercano."

show hanako emb_emb
with charachange

ha "S-sí. Algo… algo como eso."

hi "Oh, ya veo. ¿Juegas mucho este juego?"

show hanako emb_downsad
with charachange

"Hanako sacude su cabeza."

hi "¿Solo cuando los pasillos están vacíos?"

show hanako emb_emb
with charachange

"Ella asiente."

hi "Bueno entonces, no hay motivo para detenerse, estoy comenzando a sentirme realmente hambriento."

show hanako emb_smile
with charachange

"Ella asiente una vez más, en esta ocasión con un poco más de entusiasmo."

hi "Bueno entonces, vamos."

hide hanako
with charaexit

stop music fadeout 5.0

"Partimos a través del pasillo, y esta vez noto que Hanako está poniendo un poco menos de atención al piso."

"Me pregunto; ¿qué tan solitario tiene que ser alguien para idear un juego como ese?"

"Pero, antes de darme cuenta de lo que estoy haciendo, me encuentro tratando de apuntar cada paso para que caiga en los mosaicos correctos."

play music music_dreamy fadein 2.0

scene bg school_miyagi
with locationchange

"El ruido del festival es ligeramente mayor dentro del cuarto de té, pero la brisa viniendo a través de la ventana abierta hace que valga la pena."

"Sin pensarlo, camino al alféizar e inhalo profundamente. Algunas veces olvido lo limpio que el aire es aquí comparado al de mi hogar."

show hanako basic_bashful at center
with charaenter

ha "¿Quier… gustas un poco de té?"

hi "Eso sería estupendo, gracias."

hide hanako
with charaexit

"Caigo en la cuenta de que esta es la primera vez que he estado solo con Hanako sin ella intentando estar en cualquier otro lugar."

"Apartando la vista de la ventana, observo mientras ella prepara una sencilla tetera de té y ordena algunos emparedados en un plato."

"La he visto hacer esto antes en algunas ocasiones, pero esta vez ella luce ligeramente diferente."

"Es como si ella estuviera…{w} calmada."

"Eventualmente coloca la pequeña bandeja en la mesa y vierte dos tazas de té."

"La fresca esencia del té preparado se mezcla con la brisa, y por un segundo siento como si fuese el único en el mundo."

hi "Creo que ahora sé por qué te gusta este cuarto."

show hanako defarms_worry at center
with charaenter

ha "Em… no sé a lo que te refieres."

hi "Bueno, hay bastantes personas allá afuera, pero aquí es como si fuera otro mundo."

hi "Puedes pretender que no hay nadie en kilómetros a la redonda."

show hanako emb_downtimid
with charachange

ha "E-estás en lo cierto."

ha "Es como si el mundo hubiera olvidado este cuarto."

show hanako emb_emb
with charachange

ha "Y p-por eso, puedes olvidarte del exterior."

"Eso sería atractivo en algunos casos."

"Hasta donde puedo decir, el abuso convencional no existe en esta escuela."

"Por otro lado, no he visto a una sola persona hablar con Hanako además de Lilly."

"Si eres ignorado por el mundo, un lugar donde puedes olvidarte de su existencia tendría un atractivo especial."

hi "Ese es un buen punto. Es como que este cuarto te ofrece alguna especie de completa libertad."

show hanako emb_smile
with charachange

ha "S-sí."

show hanako basic_bashful
with charachange

ha "Dime… ¿juegas ajedrez?"

hi "¿Ajedrez? Lo he jugado un poco, supongo."

hi "¿Deduzco que has jugado antes?"

show hanako basic_distant
with charachange

ha "Un poco…"

hide hanako
with charaexit

"Sin decir nada más, Hanako se mueve a uno de los armarios y extrae un pequeño juego de ajedrez."

ha "¿Qui… Quieres…?"

hi "Seguro, ¿por qué no?"

"Corto sus palabras, pero a ella parece no importarle."

scene bg school_miyagi
show hanako basic_normal_close at center
with shorttimeskip

"Acomodamos las piezas, y en poco tiempo estamos enviando a los peones a la carga a sus inevitables destinos."

"Me tomo mi tiempo y examino atentamente cada movimiento y sus consecuencias, la nostalgia por el juego quedando en segundo lugar contra las preocupaciones presentes."

"Por un rato el juego es una larga batalla de desgaste, pero descubro una abertura y abro una línea en su defensa."

show hanako basic_worry_close
with charachange

"Unos pocos movimientos después, su rey está acorralado por varias de mis piezas."

hi "Jaque mate."

hi "No eres mala en esto, ¿verdad?"

"Una apreciación honesta. Su técnica es muy buena, pero en varias ocasiones logré explotar su falta de predicción."

"Tomo una pieza y la examino. Luce relativamente nueva, aún sin desgastarse por su edad."

show hanako basic_smile_close
with charachange

ha "Yo… yo creo que no."

hi "¿Lilly juega?"

show hanako def_worry_close
with charachange

"La ausencia de una respuesta de Hanako me hace pensar en mi pregunta."

ha "Un… Un poco…"

ha "E-esta es la primera vez que he jugado contra alguien… además de ella, o…"

show hanako emb_downsad_close
with charachange

"¿O…?"

"Ella se interrumpe abruptamente, dejando la respuesta volando en el aire. Alguien que ella conoció antes de venir a Yamaku, tal vez."

hi "Bueno entonces, me siento honrado de haber jugado contra ti."

show hanako emb_smile_close
with charachange

ha "Em… ¿Podemos jugar una vez más?"

"Ella pregunta como si estuviera pidiéndome que me cortara mis propias manos. ¿Le ha entrado el espíritu competitivo?"

hi "Seguro. Pero no esperes que me la lleve tan tranquilo esta vez…"

"No es que lo haya hecho antes, desde luego. Ella parece apreciar el tono competitivo."

show hanako emb_downsmile_close
with charachange

ha "Lo… lo mismo digo…"

stop music fadeout 2.0







label es_A43:


scene bg school_dormhallway at bgright
show kenji happy at center
with None

stop music fadeout 2.0

"¿Qué es lo que voy a hacer? No tengo ningún plan. En retrospectiva, eso es realmente estúpido."

"¿Quizás debería haber invitado a alguna chica a salir? Por otra parte, dadas las circunstancias, no creo que pudiera haber hecho algo parecido. Es tan solo mi primera semana."

"Una semana que he desperdiciado sintiéndome incómodo alrededor de casi todos, tropezando conmigo mismo tratando de aclimatarme a este lugar."

"Pensando en ello, ¿qué he logrado?"

"¿A quién podría haber invitado?"

"Maldición, parece que Kenji es mi única opción real para una cita hoy."

"Esto es lo más deprimente que me ha sucedido desde que tuve un ataque al corazón porque una chica me confesó que yo le gustaba."

"No hay remedio."

play music music_kenji fadein 0.5

hi "Realmente no lo sé. Supongo que no tengo nada, pero un fuerte parece un poco excesivo."

hi "¿Seguro que no quieres salir? No es como si los visitantes no fueran a venir a los dormitorios este día."

show kenji tsun
with charachange

"Se ve atónito por esta revelación."

ke "Maldición, puede que tengas razón. Este lugar no es seguro hoy."

ke "Debemos encontrar un lugar dónde ocultarnos."

"Guarda silencio por un momento, pensando."

show kenji neutral
with charachange

ke "La azotea."

hi "¿Qué hay de ella?"

show kenji happy
with charachange

ke "Nos vamos a ocultar en la azotea por hoy."

ke "Es el lugar perfecto, nadie nunca sube allá."

show kenji neutral
with charachange

ke "Nos vemos allí en una hora. Tengo que prepararme."

stop music fadeout 1.0

show kenji neutral at Slide(0.5,0.5,0.4,0.5,0.5, time_warp=_ease_out_time_warp)
with None

hide kenji
with charaexit

play sound sfx_doorslam
with vpunch

"Cierra la puerta de golpe y asegura los pasadores con un click."

"Maldición, ¿qué diablos le pasa a Kenji?"

"Y pensar que ahora le sigo la corriente a sus locuras. En verdad me deprime."

"Me siento como un fracasado."

play ambient sfx_crowd_outdoors fadein 0.3

scene bg school_courtyard
show crowd
with locationskip

"Una vez que pongo un pie fuera, el bullicio de la multitud me recibe."

"Toda la escuela rebosa de actividad."

"Hay puestos por todas partes, y la afluencia de gente pululando entre ellos es considerable."

"No esperaba que el festival atrajera a tantos visitantes."

"Debo admitir que la gente a cargo de la decoración del lugar puso mucho empeño en ello, y en verdad se nota."

"La gente parece estar pasándola bien, y el ambiente es colorido, brillante y feliz."

play music music_rain fadein 1.0

"Eso sería, si yo no estuviera de tan mal humor."

"En este momento, es más molesto que cualquier otra cosa."

"Bueno, no hay remedio. Decido seguir con mi plan original y comer, luego supongo que al menos debo ver lo que Kenji está tramando en la azotea."

"…"

scene bg school_stalls2 at Fullpan(8.0)
with locationchange

"Circulo lentamente alrededor del patio para matar algo de tiempo, viendo los puestos pero ya sin ganas de jugar ninguno de los juegos."

"Los colores chillones lastiman mis ojos y me siento más y más enfermo cada minuto."

"Ni siquiera puedo decidir qué quiero comer, y la gran selección, combinada con las masas de visitantes enérgicos, no está ayudando."

scene bg school_stalls1 at bgright
with locationchange

"Tan solo me dirijo al puesto más cercano que parece ofrecer algo más o menos comestible y hago fila."

"Resultan ser fideos."

"También resultan no ser muy buenos."

"Bueno, por lo menos es alimento. No es como si exigiera algo más en este momento."

scene bg misc_sky at Fullpan(25.0)
with locationchange

"Mientras revuelvo mis desagradables fideos, me pregunto ociosamente qué estarán haciendo los demás en este momento."

"Shizune y Misha definitivamente están en algún lugar organizando algo."

"Será mejor mantenerme alejado de ellas. Supongo que no me perdonarían tan fácilmente por dejarlas solas con este asunto."

"Imagino que Emi estará revoloteando por todo el lugar, siendo depresivamente alegre."

"No hay posibilidades de encontrarla, pero tampoco hay posibilidades de evitarla, así que no importa."

"Lilly probablemente estará ayudando a su grupo con ese evento del festival, y demasiado ocupada para la compañía de alguien más."

"Hanako no querría hablar con nadie de todas maneras, ya sea manteniéndose alejada de los demás o ayudando a Lilly."

"Rin debe de estar atendiendo su mural y posiblemente esté siendo de poca ayuda a cualquier grupo hipotéticamente interesado."

"Ir allá por un poco de paz y tranquilidad parece como la opción más agradable de las anteriores, pero por otro lado, tampoco puedo imaginarme al arte siéndome impuesto como algo que suba mi ánimo, así que paso."

scene bg school_stalls1 at bgright
with locationchange

"Mientras estaba perdido en mis pensamientos, mi comida parece haber desaparecido, y lo mismo ha hecho mi hambre."

"Supongo que simplemente bloqueé la experiencia de comer, lo cual debería ser algo bueno."

"Saciado pero insatisfecho, me doy vuelta para caminar hacia el edificio principal. Ya casi ha pasado una hora."

play ambient sfx_crowd_indoors fadein 0.3

scene bg school_lobby
show crowd
with locationskip

"La multitud es aún mayor aquí que afuera."

scene bg school_hallway3
show crowd
with locationchange

"Los pasillos son casi insoportables, y ni siquiera me atrevo a pensar cómo está dentro de los salones."

stop ambient fadeout 1.0

scene bg school_staircase1
with locationchange

"Me dirijo escaleras arriba hacia mi destino."

"La azotea."

"Afortunadamente, la puerta al final de las escaleras no tiene seguro, pero ahora hay un letrero escrito a mano en ella."

window hide

$ written_note("{size=55}{b}PROHIBIDO EL PASO{/b}{/size}", quiet=True)

window show


"Si no les molesta, sin su permiso."

scene bg school_roof at bgright
with locationchange

"El ruido del festival es sorprendentemente reducido acá arriba, y la azotea parece desierta, como lo esperaba."

"Cerca de un lugar donde la malla ciclónica ha colapsado, hay una pila de sábanas que se ven extrañamente fuera de lugar."

stop music fadeout 3.0

"Espera."

play sound sfx_rustling

"¿Acaso esa pila acaba de moverse un poco?"

"Eso sería raro, ya que no hay nada de viento."

"Con cuidado acerco mi mano y le doy un empujoncito para probar."

play sound sfx_impact
show kenji rage_close:
    alpha 0.0 xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 0.7
    easein 0.2 yanchor 1.0 alpha 1.0

with vpunch

$ doublespeak(ke, hi, u"¡AAAAAAAAAAAAHH!")

play music music_comedy fadein 2.0

show kenji rage:
    center alpha 1.0
with charadistant

"Espantado, doy un salto atrás."

ke "¿Quién es?"

hi "Maldita sea, Kenji. Soy yo."

show kenji tsun at center
with charachange

ke "Oh demonios, me asustaste, hombre."

hi "Entonces, ¿qué es lo que estamos haciendo aquí arriba?"

show kenji neutral
with charachange

ke "Vamos a tener un picnic."

hi "¿Qué?"

show kenji happy
with charachange

ke "Sí. Tengo sábanas, pretzeles y whiskey. Este es el mejor arreglo, viejo."

hi "¿Whiskey?"

hi "¿No eres un poco joven para beber alcohol?"

show kenji tsun
with charachange

ke "Tengo 20, ¿sabes?"

hi "… No es cierto."

show kenji neutral
with charachange

ke "Sí los tengo y tú también."

hi "¿Qué? Eso es absurdo."

show kenji tsun
with charachange

ke "Oye, por lo menos TÚ sacas algo de eso, todo lo que saco yo es esta botella de whiskey…"

"Está hablando incoherencias, pero decido seguirle el juego."

hi "Así que, ¿por qué tienes una botella de whiskey?"

show kenji happy
with charachange

ke "Mi mamá no pudo venir a visitarme para el festival, así que en su lugar me mandó un caro whiskey puro de malta."

hi "Una historia probable."

ke "¿Quieres un poco?"

hi "…"

"No es como si tuviera algo que perder. Este día no podría ponerse peor."

hi "… ¿Por qué no?"

hide kenji
with charaexit

show bg school_roof at center
with charamove_accel

show kenji happy_close at offscreenleft
with None

show kenji happy_close at twoleft
show bg school_roof at bgleft
with charamove_decel

"Nos sentamos en la pila de sábanas que Kenji aparentemente arrastró hasta acá."

"Él saca una botella casi completa de whiskey y me la pasa."

hi "¿Ni siquiera trajiste vasos?"

show kenji tsun_close
with charachange

ke "No, este no es ningún picnic romántico de princesitas. ¿Qué carajos, hombre?"

show kenji neutral_close
with charachange

ke "Este es un picnic de machos."

ke "Sin vasos."

ke "Sin servilletas."

ke "Solo whiskey. La bebida de los verdaderos hombres."

hi "Como sea."

show kenji happy_close
with charachange

ke "Y pretzeles."

"Le doy una mirada más de cerca a la botella."

"Whiskey puro de malta añejado 12 años, como dijo."

"Encogiéndome de hombros, le doy un trago. Quema mi garganta como ácido, pero el sabor no es desagradable."

"Lo siento irse directo a mi cabeza, y el regusto perdura en la parte de atrás de mi boca, ansiando otro trago."

show kenji neutral_close
with charachange

ke "Deberíamos establecer nuestra contraofensiva y hablar mierda de las mujeres aquí, donde no pueden oírnos."

show kenji tsun_close
with charachange

ke "Maldición, olvidé mis gráficas."

"Decido jugar un juego conmigo mismo. Cada vez que Kenji mencione “conspiración feminista”, tomaré un trago."

$ wdt_off(False)

stop music fadeout 2.0

scene black
with delayblinds

centered "Cuatro o cinco horas, o posiblemente varios días después:\n{w}(perdí la noción)"

play music music_kenji fadein 0.5

scene ev kenji_rooftop
with delayblinds

window show

ke "¡No deberías sentirte mal, hombre! ¡Relájate de una puta vez! ¡En serio, en serio!"

hi "¡Que estoy relajado, con un demonio!"

ke "¡Lo digo como lo veo!"

scene ev kenji_rooftop_kenji
with flash

ke "Piénsalo. ¿Cuándo fue que vivienda y terrenos empezaron a ser más y más caros? Cuando las mujeres comenzaron a ingresar a la fuerza laboral, porque creó familias nucleares de doble ingreso."

ke "Sí olvidé mis gráficas, pero, y tendrás que confiar en mi palabra para ello, las mujeres están conectadas al decaimiento de toda la sociedad."

show ev kenji_rooftop_large:
    crop (288, 376, 800, 600)
    ease 1.0 crop (1024, 260, 800, 600)

hi "Ya veo. Eso es un poco difícil de creer."

"Incluso si digo eso, de alguna manera, todo lo que dice Kenji parece tener más sentido ahora."

"Todo encaja, pero no sé si es porque él puede explicar las cosas más claramente cuando está ebrio, o porque yo entiendo todo mejor cuando estoy ebrio."

show ev kenji_rooftop_large:
    ease 1.0 crop (288, 376, 800, 600)

ke "No hombre, piensa. ¡Piensa! ¡Piensa en las consecuencias más profundas!"

ke "La gente podía darse el lujo de empezar a decir “Oh bueno, ahora que dos miembros de la familia están ganando dinero, en lugar de uno, seguramente pueden costearse algo como incrementos al precio de propiedades”."

show ev kenji_rooftop_large:
    ease 1.0 crop (1024, 260, 800, 600)

hi "Entiendo tu punto, pero los terrenos en Japón siempre han sido caros."

show ev kenji_rooftop_large:
    ease 1.0 crop (288, 376, 800, 600)


ke "… Y el precio de las tierras generalmente va en aumento cuando un país comienza el proceso de industrialización… ¡Pero no! ¡Es a causa de las mujeres! La correlación implica causalidad, ¿sabes?"

show ev kenji_rooftop_large:
    ease 1.0 crop (1024, 260, 800, 600)


hi "Pensé que correlación no implicaba causalidad. Bueno, como sea, tal vez estés en lo correcto."

show ev kenji_rooftop_large:
    ease 1.0 crop (288, 376, 800, 600)

ke "Siempre tengo la razón. Sí, apuesto a que las mujeres crearon la industrialización, también, para cubrir sus huellas."

ke "Qué diabólico."

ke "Así que sí, ¡todos pueden irse a la mierda!"

scene bg school_roof_ni
show kenji rage_ni:
    xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 0.9
    easein 1.0 yanchor 1.0
with locationchange

"Se pone de pie, impresionándome porque estoy bastante seguro de que yo no podría aunque quisiera, y grita extremadamente fuerte como si hubiera perdido el concepto de volumen. Me crispa y casi quiero taparme los oídos."

stop music fadeout 2.0

ke "Aaagh, hubiera sido agradable si pudiera haber estado allá abajo… Pero no. Sabes, pensar de esa manera es una trampa, piensas que te estás perdiendo de algo, pero al final de ese camino no hay nada más que desgracia…"

show kenji tsun_ni at center
with charachange

play music music_sadness fadein 1.5

"Kenji me arrebata la botella e inclina su cabeza hacia atrás, tratando de verter el alcohol dentro de su boca, pero solo termina empapándose a sí mismo con este."

show kenji rage_ni
with charachange

ke "¡Maldita sea! Verás, ¡mi puntería es terrible, y lo malo de beber es que solo empeora mientras más lo haces!"

show kenji tsun_ni
with charachange

ke "Este día es el día de la desesperanza."

"Su voz inmediatamente baja a casi un susurro, pero comienza a hablar mucho más rápido que antes, arrastrando sus palabras ligeramente a causa del whiskey."

"Al hablar, agita la botella por doquier, derramando un poco aquí y allá."

ke "Sí, ¿sabes cuál fue el evento más impactante en mi vida?"

"Tengo un vago recuerdo de él contándome sobre el segundo evento más impactante en su vida, el cual era un pájaro cagándose en su cabeza."

"No tengo expectativas especialmente grandes de esto, pero, de cualquier manera, asiento para que continúe."

show kenji neutral_ni
with charachange

ke "No lo pensarías, pero una vez tuve una novia aquí, creo que fue el año pasado."

ke "Sí, estás que alucinas, ¿eh? Sabes, nunca le he contado eso a nadie."

"Es cierto, ese pensamiento sí que me deja alucinando. De pronto quiero la botella. La tomo de Kenji y bebo de un trago lo más que puedo."

show kenji tsun_ni
with charachange

ke "Era más inocente en ese entonces, y pensé que estaba cuerda, a diferencia de la mayoría de las mujeres. Pero entonces un día, entablamos… relaciones sexuales."

ke "Estuvo muy bien, pero siguiendo inmediatamente al evento que es la razón de una cosa así, algo extraño y atemorizante sucedió."

show kenji tsun_ni at tworight
show bg school_roof_ni at bgleft
with charamove

"Se arroja a sí mismo sobre la valla, recargándose en ella con los ojos entrecerrados."

ke "¡Comencé a sentirme increíblemente cansado y somnoliento! ¡Eso no es normal, hombre! ¡Qué carajos!"

ke "Digo, normalmente, ese sería un momento de mi vida de alta tensión con adrenalina bombeando, ¡pero los niveles de energía cayeron como un ladrillo!"

ke "Algo siniestro estaba en acción, lo podía sentir."

ke "Fue entonces cuando supe… que las mujeres son peligrosas, ¡minando la fuerza vital de todos los hombres a través de la única mercancía que es controlada casi exclusivamente por ellas!"

ke "Repugnante."

show kenji neutral_ni
with charachange

ke "Sí, estás mejor así, amigo…"

"Kenji estaba en lo correcto, este es realmente el día de la desesperanza. Bebo más para evitar tener que procesar lo que acaba de decir."

ke "Ahora yo soy el último hombre cuerdo en un mundo loco… cuando otras personas se den cuenta, habrá una guerra, una gran guerra entre hombres y las fuerzas del feminismo."

ke "Pero el problema es que no todos los hombres pelearían de mi lado… esa mierda apesta. Podría ser poco exigente, cualquier hombre es bueno. Pero no los tipos criados por su mamá o su hermana, eso seguro."

show kenji tsun_ni
with charachange

ke "Y nadie a quien le guste el porno de chicas con pitos."

hi "Ja… Esa situación me parece poco probable, como si no fuera a suceder, como si… como si no fuera probable que sucediera."

"El alcohol debe estar surtiendo efecto."

"De cualquier forma, todavía me siento deprimido porque este día estoy aquí arriba."

"Realmente no ansiaba el festival con el mismo ánimo que el resto de la escuela, pero aun así."

"Hubiera sido agradable haber ido con alguien. Desde aquí arriba, ciertamente se escuchaba como si todos se hubieran estado divirtiendo. Tal vez sí me perdí de algo."

"Es solo que no había nadie con quien podría haber ido."

"O quizás sí había. Tantas oportunidades, viendo en retrospectiva, y debí haber desaprovechado tantas."

ke "Maldición, esta es la verdadera desgracia… La peor parte es que algunas veces siento como si no tuviera elecciones en mi vida, ¿sabes?"

ke "Como si nunca tuviera una oportunidad de tomar una decisión, la mierda solo sucede."

ke "Como si todo estuviera ya programado. Como el destino… o algo. Como si no hubiera manera de que participara en lo que hago."

stop music fadeout 0.2

show kenji rage_ni
with vpunch

ke "¡Rápido, hazme una pregunta!"

hi "Ah…"

ke "¡Ahora!"

hi "Realmente no puedo…"

show kenji tsun_ni
with charachange

ke "¿Ves? ¡Este es tan solo otro ejemplo de ello! ¡Maldición! ¡Mierda! ¡Maldición! ¿Ya ves? Ahora, cuando estoy tratando de ir en contra de mi destino y tomar las riendas de mi vida, la oportunidad ni siquiera está ahí."

ke "Maldita sea, hombre, me has fallado. Me fallaste por última vez. Cretino."

show kenji tsun_ni:
    xpos 0.7 ypos 1.0 xanchor 0.5 yanchor 1.0
    easeout 0.7 ypos 0.9 yanchor 0.5
with Pause(0.8)

show kenji tsun_ni:
    rotate 0
    easeout 0.7 rotate 90 ypos 1.0 yanchor 0.3

with Pause(.7)


play sound sfx_impact
with vpunch

hide kenji
with None

"Se desliza hasta sus rodillas y luego se cae de lado, acostado sobre la grava de la azotea."

hi "Oye, ¿estás bien?"

ke "No, no estoy bien, ¿que no puedes ver que he caído en desgracia?"

"Habla en tono sarcástico."

show kenji neutral_ni:
    xpos 0.7 ypos 1.0 xanchor 0.5 yanchor 0.0
    easein 0.5 ypos 1.0 yanchor 0.7
with Pause(0.5)

"De pronto, Kenji se levanta y se sienta, se sacude torpemente con la mano, y la estira hacia mí para alcanzar la botella. La pongo en su mano."

show kenji tsun_ni at Transform(xpos=0.7, xanchor=0.5, ypos=1.0, yanchor=0.7)
with charachange

ke "¿Qué demonios? Maldita sea, mataste casi toda la botella. ¿Ves?, es como si no tuviera opciones en la vida…"

ke "¿Es así como va a ser por el resto del tiempo?"

hi "Bueno, estoy bastante seguro de que no va a ser así por el resto del tiempo."

"Lo que sea de lo que esté hablando. Mi cabeza da vueltas. Me levanto y me recargo contra la valla, con la esperanza de que me ayude a concentrarme un poco."

show kenji tsun_ni at center
show bg school_roof_ni at center
with charamove

ke "Sí, lo sé. Tenemos que luchar contra el poder con todo lo que tengamos. Es la única manera de vivir."

play music music_one fadein 6.0

show kenji neutral_ni
with charachange

ke "Eres un buen tipo."

show kenji happy_ni
with charachange

ke "Este lazo fraternal es lo que me permite continuar en estos tiempos oscuros."

show kenji neutral_ni
with charachange

ke "Deberíamos de ir a fastidiar mujeres."

hi "¿Afeitar mujeres? ¿Qué?"

show kenji neutral_close_ni
with characlose

ke "Fastidiar mujeres. Joder mujeres. Pero tenemos que hacerlo ya, antes de que pierda este valor ligado al alcohol."

"Gesticula con furia. Con locura, incluso."

show bg school_roof_ni at Slide(0.5,0.5,0.75,0.75,0.5, time_warp=_ease_time_warp)
show kenji neutral_close_ni at Slide(0.5,0.5,0.3,0.5,0.5, time_warp=_ease_time_warp)
with None

show kenji neutral_ni at Slide(0.5,0.5,0.3,0.5,0.5, time_warp=_ease_time_warp)
show bg school_roof_ni at Slide(0.5,0.5,0.75,0.75,0.5, time_warp=_ease_time_warp)
with charadistant

"Doy un paso atrás."

show kenji neutral_ni at Slide(0.3,0.5,0.5,0.5,0.5, time_warp=_ease_time_warp)
with None

show kenji neutral_close_ni at Slide(0.3,0.5,0.5,0.5,0.5, time_warp=_ease_time_warp)
with characlose

"Él da un paso hacia adelante."

show kenji happy_close_ni
with charachange

ke "¿Qué ocurre contigo? ¿No estás de humor para el amor?"

hi "Para serte franco… no."

show bg school_roof_ni at Slide(0.75,0.75,1.0,1.0,0.5, time_warp=_ease_time_warp)
show kenji happy_close_ni at Slide(0.5,0.5,0.3,0.5,0.5, time_warp=_ease_time_warp)
with None

show kenji happy_ni at Slide(0.5,0.5,0.3,0.5,0.5)
show bg school_roof_ni at Slide(0.75,0.75,1.0,1.0,0.5, time_warp=_ease_time_warp)
with charadistant

"Doy otro paso atrás."

show kenji happy_ni at Slide(0.3,0.5,0.5,0.5,0.5, time_warp=_ease_time_warp)
with None

show kenji happy_close_ni at Slide(0.3,0.5,0.5,0.5,0.5, time_warp=_ease_time_warp)
with characlose

"Él da otro paso hacia adelante."

"Se inclina demasiado hacia mí, incómodamente cerca."

hi "Qué diablos, deja de inclinarte de esa forma, me molesta."

ke "¿Inclinarme cómo? Oye, no deberías recargarte sobre la cerca de esa manera, es medio inseguro."

"Trato de alejarme de Kenji, pero mi equilibrio no es muy bueno."

"Tambaleándome por el mareo, me aferro a uno de los postes de la valla, pero entonces siento cómo cede tan pronto pongo mi peso en él."

"… Esto no está bien. Aunque mi cerebro aturdido por el alcohol parece no ser muy capaz de registrar el porqué."

show black behind bg
with None

show n_vignette:
    xalign 0.5 yalign 0.5 zoom 4.0
    linear 0.2 zoom 1.2
with Pause(0.2)

show n_vignette:
    zoom 1.2
    linear 8.0 zoom 0.001
show kenji happy_close_ni:
    xalign 0.5 yalign 0.5
    linear 8.0 zoom 0.001
show bg school_roof_ni_crop:
    xalign 0.5 yalign 0.5
    linear 8.0 zoom 0.001

"Aunque el rostro de Kenji parece estar empequeñeciéndose cada vez más, lo cual me alivia un poco."

"Empequeñeciéndose bastante, de hecho. Y muy rápidamente."

show nightsky rotation
with None

"Parece haber un poco de viento ahora. De alguna manera me hace sentir casi sin peso."

"Me siento un poco mareado, como si mi mente estuviera en blanco."

hi "Estoy… ¿cayendo…?"

"Puedo ver el cielo nocturno mientras me doy vuelta en el aire. La botella se aleja de mis dedos y se desvanece como si fuera humo mientras caigo."

"Me doy cuenta de que este es el final apropiado para un muy, muy mal día."

window hide

stop music fadeout 0.1
play sound sfx_crunchydeath

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
