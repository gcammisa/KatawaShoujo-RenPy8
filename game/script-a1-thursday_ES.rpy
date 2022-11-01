label es_A19:

window hide None
scene black
with dissolve

play sound sfx_alarmclock
stop ambient

show bg school_dormhisao
with openeye

play music music_dreamy fadein 2.0

window show

"El sonido de una alarma me saca de un sueño irregular hacia el desagradable estado de vigilia."

"Permanezco bajo la sábana por unos minutos, reuniendo energías para levantarme mientras pienso en excusas del porqué no lo he hecho aún."

"Honestamente, no me molestaría quedarme aquí todo el día. La escuela es sorprendentemente agotadora tras una larga pausa, y el choque cultural aún no ha desaparecido, creo."

"Sin embargo, a pesar de tener la impresión de que faltar a clases es sencillo aquí, no creo que me dejen salirme con la mía tan fácilmente."

"Y el enfermero seguramente se pondrá pesado con el sermón del ejercicio, también."

"Así que eventualmente me levanto, trago mis medicamentos matutinos y me pongo mi vieja ropa de futbol."

"Gracias a mi enfermedad, fui exento de participar en las clases de gimnasia de Yamaku, así que no me dieron un uniforme deportivo."

"Pediría uno para cubrir tal contingencia, pero vestir mi vieja ropa de futbol es un poco nostálgico."

"Ya no puedo usarla para eso, así que tal vez pueda tener una nueva vida de esta manera. Un poco como yo."

label es_A19a:



"Después de todo, si voy a empezar a cuidarme, no puedo permitirme andar de haragán. Empezaré desde las bases."

"Bases que incluyen mantener el resto de mi cuerpo en forma junto con lo poco que puedo hacer para fortalecer mi corazón."

"Quizá entonces pueda volver a algo cercano a una vida normal; o al menos algo en lo cual sea menos probable que caiga muerto en cualquier momento."

stop music fadeout 2.0


label es_A19b:


"Me parece un poco estúpido, en verdad."

"Pero supongo que de esta forma puedo al menos decirle honestamente al enfermero que estoy haciendo algo sobre mi salud."

"No es como si haya sido un gran corredor, para empezar."

"Intentar no cuesta nada, creo."

stop music fadeout 2.0


label es_A19c:


show bg school_track
with locationskip

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_emijogging fadein 0.1

"Me sorprende descubrir que no soy el único presente en la pista."


"No solo eso, es además una cara que he visto antes."

"La chica con prótesis de piernas que me derribó ayer en el pasillo está corriendo en la pista ágilmente, como una gacela mitad mecánica."

"¿Cuál era su nombre? Era uno corto, pero no puedo acordarme."

"Parece encontrarse dando vueltas a un trote un poco relajado, sus piernas prostéticas golpeteando rítmicamente contra la superficie dura de la pista."

"Me pregunto qué motivo tendrá para correr tan temprano por la mañana. Tal vez sea por algo similar a mi caso, y el enfermero está obligando a la pobre chica a trotar tal y como lo hace conmigo."

"Definitivamente yo no estaría aquí de no ser por mi salud, y por su insistencia en que lo haga."

"E incluso con las cosas como son, es solo para quitármelo de encima pronto."

"El hecho de que fuera menos probable encontrarme a alguien que presenciara mis lastimosos intentos de ponerme en forma fue meramente un feliz accidente."

"Me iría, pero se ve que mi antigua agresora se percató de mí en su última vuelta."

"Me saluda con la mano alegremente y trota hacia mí."

show emi basic_grin_gym at Slide(0.7,0.5,0.5,0.5,1.0,_ease_in_time_warp)
with charaenter

stop ambient

emi_ "¡Buenos días! Tu nombre es Hisao, ¿verdad?"

play music music_emi fadein 2.0

"Se sonríe, aparentemente complacida de haber recordado mi nombre."

show emi basic_closedgrin_gym at center
with charachange

emi_ "Tal vez no te acuerdes de mí."

show emi basic_grin_gym
with charachange

emi_ "¿Emi? Te tiré al suelo en el pasillo ayer."

label es_A19i:

show emi excited_circle_gym
with charachange

emi "“¿Señorita Ibarazaki?”"

"Imita a Misha “imitando” a Shizune, sin lograr obtener ese tenue tono alegre con su voz aguda."



label es_A19j:

hi "¿Cómo podría olvidar una presentación tan, eh, contundente?"

show emi sad_shy_gym
with charachange

"Emi tiene la decencia de verse ligeramente arrepentida por un instante antes de reír."

show emi sad_grin_gym
with charachange

emi "Sí, discúlpame por eso. Otra vez."

hi "Hmm, bueno, siempre y cuando no hagas un hábito de ello, supongo que estaré bien."

show emi basic_happy_gym
with charachange

emi "¡Genial!"

"No estoy seguro de si se dio cuenta de que estaba bromeando."

hi "Entonces el “espía-asesor” del que hablaba el enfermero… ¿en realidad eres tú?"

show emi basic_closedgrin_gym
with charachange

emi "¡Así es!"

hi "Oh."

hi "Estaba esperando a alguien del cuerpo de enfermería, para ser honesto."

show emi basic_confused_gym
with charachange


emi "¿Qué?, ¿estás diciendo que no luzco como si pudiera ser una espía?"

hi "No, es más como un alivio. Temía que tuviera a alguien para observar cada uno de mis movimientos."

hi "A menos que estés aquí para hacer exactamente eso."

show emi excited_laugh_gym
with charachange

emi "No, estoy aquí por mis propios motivos, el enfermero solo me preguntó si había visto a “un estudiante de intercambio con pelo revuelto y una cara como si estuviera perdido” por la pista."


hi "Entonces, ¿por qué estás aquí?"

"Emi hace una pose dramática."

show emi basic_happy_gym
with charachange

emi "¡Entrenando!"

hi "¿Para qué?"

show emi basic_closedhappy_gym
with charachange

emi "¡Atletismo!"

hi "Ah, ya veo. ¿Entonces estás en el equipo de atletismo?"

"Emi asiente entusiasmadamente."

show emi excited_proud_gym
with charachange


emi "¡Síp! ¡Soy una de las mejores corredoras, también!"

"Y modesta sobre ello, también."

show emi basic_grin_gym
with charachange

emi "¡Oye, deberías unirte!"

emi "Es un buen ejercicio, sabes."

"Creo que tanta actividad es probablemente imposible para mí."

hi "Nah, ni siquiera estoy seguro de si en verdad me gusta tanto correr."

hi "Además, no estoy interesado en deportes organizados, ¿sabes?"

"Es cierto. Ni siquiera había estado muy interesado en el futbol."

"Digo, corría y jugaba con mis amigos y demás, pero ese era el único motivo por el cual jugaba."

"No era por la gloria que puede encontrarse en el campo de juego, eso seguro."

"Emi parece comprender lo que intento decir."

show emi basic_confused_gym
with charachange

emi "Ya veo, ya veo. No muy metido en todo eso de la organización."

show emi excited_proud_gym
with charachange

emi "Pero ahora que estás aquí, eso significa que vamos a estar corriendo juntos, ¿eh?"

hi "¿Qué? Eh, seguro, creo."

"Emi se ve contenta."

show emi excited_joy_gym
with charachange

emi "¿Vas a hacer calentamiento?"

hi "Los verdaderos hombres no calientan."

show emi basic_annoyed_gym
with charachange

emi "¡Oh no, siempre deberías hacer calentamiento! ¡Hisao malo!"

show emi excited_proud_gym_close
with characlose

"Me regaña con entusiasmo, pero luego sonríe y se acerca."

emi "Yo también odio el calentamiento."

show emi excited_laugh_gym_close
with charachange

"Se ríe de repente."

emi "Diablos, ¡y ni siquiera tengo que estirar las piernas!"

play sound sfx_gymbounce

show emi gymbounce
with charadistant

"Como para confirmar su afirmación, ella rebota hacia arriba y abajo un par de veces, dando la impresión pasajera de estar parada sobre resortes. Sus prótesis parecen ser bastante elásticas."

emi "¡Vamos!"

stop music fadeout 1.0

play ambient sfx_emijogging fadein 0.3

scene bg school_track_running
with locationchange

"Y así comenzamos a correr alrededor de la pista, e inmediatamente puedo ver que no estaba mintiendo acerca de ser buena corriendo."

"Emi se mueve con fluidez, lanzándose en una suerte de salvaje abandono."

"Yo me encuentro concentrándome en correr apropiadamente."




label es_A19d:

"Las manos extendidas, ¿cierto?"

"Y algo sobre caer sobre el metatarso del pie, en lugar de los talones…"

"Intento igualar mi paso al de Emi, pero es bastante difícil."

"Aparentemente no soy muy bueno en ello."

"Tal vez Emi podría ayudarme con eso algún día."



label es_A19e:



"Francamente, no recuerdo si hay alguna forma particular para correr, pero no puedo evitar sentir que lo estoy haciendo mal, de algún modo."

"Me siento raro en comparación con Emi, quien parece nunca perder su paso."

"…"

"Creo que ya no quiero hacer esto más."



label es_A19f:

"Realmente no me siento con ánimo de dar más que unas pocas vueltas hoy, y rápidamente paso del trote a la caminata."

scene bg school_track_on
with Dissolve(4.0)

"Emi sigue corriendo, y no parece darse cuenta de que me detuve hasta que me pasa por segunda vez."

stop ambient

"Frena rápidamente, respirando con regularidad en contraste con mis propios jadeos."

play music music_emi fadein 2.0

show emi basic_confused_gym at center
with charamoveinleft

emi "¿Ya terminaste?"

"Dejo caer mi cabeza penosamente."

hi "Je, sí."

hi "No estoy en muy buena forma en este momento."

show emi basic_grin_gym
with charachange

"Emi asiente, para luego sonreírme una vez más."

"Parece sonreír mucho."

emi "Bueno, lo importante es que empezaste, ¿no?"

show emi excited_amused_gym
with charachange

emi "La próxima vez, solo tienes que intentar aguantar más, y luego más, y más, ¡y eventualmente serás grandioso!"

hi "Tendré eso en mente."

hi "Pero creo que ahora iré a prepararme para las clases."

hi "¿No deberías ir tú también?"

"Emi se encoge de hombros despreocupadamente."

show emi basic_grin_gym
with charachange

emi "Nah, tengo tiempo de sobra."

"Noto que no lleva puesto un reloj."

hi "¿Estás segura?"

"Otro desinteresado encogimiento de hombros."

emi "No realmente… ¡Pero tengo que terminar mi rutina!"

show emi basic_closedgrin_gym
with charachange

emi "¡Nos vemos luego, Hisao!"

hi "Eh, sí. Nos vemos."

stop music fadeout 5.0
play ambient sfx_emisprinting

hide emi
with easeoutleft

stop ambient fadeout 2.0


label es_A19g:


"No estoy seguro de si acaso el experimento de esta mañana fue un éxito o un fracaso, pero debo admitir que me siento un poco bien de haber salido esta mañana."

"Y como dijo Emi, solo tengo que seguir tratando para poder mejorar, ¿verdad?"

"La práctica hace al maestro, o algo así."


"Es bueno por lo menos sentir como si haya tomado algún control sobre mi propia salud."

"Tendré que intentar mantener esto."

scene black
with locationskip_in

label es_A19h:


"Aparte de sentirme más cansado que antes, no creo haber logrado nada este día."

"Estoy tan fuera de forma que es vergonzoso."

"Todo esto puede haber sido una pérdida de tiempo. Encontraré alguna otra forma."

scene black
with locationskip_in




label es_A20:

scene bg school_dormext_half
with locationskip_out


"Me dirijo de vuelta a los dormitorios para asearme y ponerme mi uniforme, tratando de resistir el deseo de tomar un realmente largo y caliente baño."


"Estoy cansado por toda esa carrera, así que solo quiero relajarme, pero no quiero romper mi lentamente fabricada rutina de llegar a la escuela antes de las prisas matutinas."

scene bg school_dormbathroom
show steam
show steam2
with shorttimeskip

"Después de tomar un largo baño de todas maneras, me seco y salgo de la cabina para ponerme mi ropa."

show kenji silhouette_naked at center behind steam
with charaenter


"De la nada, una sombra aparece dentro de la neblina, amenazante e irradiando maliciosas intenciones. Atraviesa violentamente la niebla."

play music music_kenji fadein 0.3

hide steam
hide steam2
show kenji neutral_naked
show steam as newsteam behind kenji
show steam2 as newsteam2 behind kenji
with charachange

ke "¿Qué hay?"

hi "¿Qué estás haciendo aquí? Qué demonios, ¡me asustaste! ¡¿Cuál es tu problema?!"

show kenji tsun_naked
with charachange

ke "Debería estar preguntándote eso. Te he estado buscando por todo el lugar, hombre."

hi "¿Qué quieres decir con “por todo el lugar”?"


"Quiero preguntar si ha estado buscándome estando así, completamente desnudo, pero me callo."

"Finalmente me doy cuenta de que estoy todavía desnudo también y rápidamente sostengo mi playera frente a mí, pero Kenji no parece notar nada."

"Sus anteojos están empañados. Pero entonces, ¿por qué no los limpia? ¿Es su visión tan mala que es como si estuviera perpetuamente viendo a través de la niebla?"


ke "Ya sabes, tu cuarto, y… Sí, eso es todo. Oye, quiero decir, al final aún tuve que levantarme. Lo que sea. No es importante. ¿Me prestas algo de dinero?"

show kenji neutral_naked
with charachange


"Él pone una cara de inocente y mira a otro lado, tratando muy esforzadamente de lucir muy casual. No funciona; él es tan transparente como sus anteojos del tamaño de ventanas."

"Hablar neutralmente de esta forma, vistiendo nada, se siente incómodo."

"De hecho, de alguna forma es aún más incómodo estar desnudo frente a alguien cuando no puede verme estar desnudo. Por no decir nada del hecho de que él está desnudo también."

"Trato de sacudirme el sentimiento de encima, con poco éxito."

hi "¿Dinero? Seguro."

show kenji happy_naked
hide newsteam
with charachange

ke "Fabuloso."

hi "Espera, ¿por qué lo necesitas?"

show kenji tsun_naked
with charachange

ke "Ehhhh…"

show kenji neutral_naked
with charachange

ke "¿No puedes simplemente dármelo porque tuve la buena voluntad de no echarle un vistazo a tus bolsillos mientras tú estabas bañándote?"
ke "Podría haberlo hecho, pero ejercí dominio sobre mí mismo. Y al final, ¿no es la intención lo que cuenta? Vamos, sé un camarada."

"Esto no tiene sentido. Si es la intención lo que cuenta, debo negar el préstamo, dado que sus pensamientos fueron tan claramente impuros y sus intenciones son probablemente más siniestras pues no puede decirme cuáles son. Le digo esto a él."

show kenji tsun_naked
with charachange

ke "Estoy ofendido hombre, pero si ese es tu juego, entonces bien, supongo que no tengo elección. Quiero ordenar una pizza, y ya tengo la mayor parte de lo del costo de la pizza. Necesito tu ayuda para el resto."

hi "También obtengo un poco de esa pizza, ¿cierto?"

ke "No."

hi "¿Lo dices en serio?"

show kenji neutral_naked
with charachange

ke "Seguro. Te daría un poco, pero tienes clase, no tienes tiempo de comer pizza."

hi "¡¿Qué hay de ti?!"

ke "No voy a ir a clase, tengo que esperar la pizza y pagarle al tipo. Y luego comerla. No es fácil. Tienes que obtener la pizza furtivamente. Si no lo haces, todos te verán. Y a la pizza. Y pedirán una rebanada."

show kenji tsun_naked
with charachange


ke "Es un duro mundo allá afuera. Todos quieren un pedazo. Entonces te quedas despizzado en un mundo implacable. Ha pasado antes, por eso es que lo sé."


ke "Cada día, planeo mi venganza, para que así cuando la gente que me ofendió ordene una pizza, estaré ahí. ¡Siempre vigilante!"


"Kenji irrumpe en una pose dramática, completamente sin ironía."

show kenji neutral_naked
with charachange

ke "Pero sí, solo necesito como 400 yenes. ¡Por favor! ¡Eres mi única esperanza! No puedo ir afuera y comprar mi propia pizza, ¡está demasiado lejos!"

ke "Trato de no salir a menos que sea absolutamente necesario. Déjame decirte lo que sucedió la última vez que salí sin planearlo cuidadosamente con antelación."

ke "Estaba afuera. No puedo recordar lo que estaba haciendo. Algo. ¿Estar parado? Tal vez preguntándome cómo llegué ahí."

show kenji tsun_naked
with charachange

ke "Y luego, de la nada, sucedió."

ke "Como el relámpago de un rayo, partiendo el cielo, tal como partes un emparedado en dos piezas iguales para hacerlo más manejable para comer, un ave cagó en mi cabeza."

ke "Fue el segundo momento más impactante de mi vida."

hi "¿Cuál fue el primero?"

"Me ignora y continúa hablando. Quiero agarrarlo y sacudirlo. ¿Solo está tratando de mantenerse hablando? Me iré por esa opción, incluso si es más probable que simplemente no me haya escuchado."



ke "Era como en las aperturas de algunos tipos de series de anime."
ke "¿Sí sabes cómo siempre hay una parte donde el tipo principal está peleando con su rival, y vuelan el uno hacia el otro y chocan espadas y hay como grandes y dramáticas auras de color y zoom?"

show kenji neutral_naked
with charachange

ke "Fue como eso, pero con popó."

hi "Entiendo."

show kenji happy_naked
with charachange


ke "Así que sí, necesito dinero. ¿Por favor? No me dejes volando, hombre. Solo necesito como 1000 yenes."

hi "Pensé que eran 400."

ke "Está bien."

hi "¿Qué?"

ke "Te los pagaré, lo juro."

hi "Mejor lo haces, eso es lo que significa tomar cosas prestadas."

show kenji neutral_naked
with charachange

ke "No sé cuándo podré pagarte."

hi "Tienes una semana."

show kenji tsun_naked
with charachange

ke "Aaaaaaaaaaaaaaahhhhhhhhhhhhhhhhhhhhhhhhggggggggggghhhhhhhh……"

"Kenji hace una mueca de dolor y sonidos como de una vaca agonizando, un hecho particularmente perturbador dado el hecho de que su batuta se dirige libremente."

ke "No se supone que seas tan rígido sobre el dinero entre hermanos de armas, hombre. Los hombres la llevan lo suficientemente mal con todo como es."
ke "¿Sabías que las estrellas porno masculinas solo ganan la mitad de lo que las estrellas porno femeninas ganan?"

hi "Eso no significa nada a menos que seas una estrella porno."


ke "Entonces tal vez soy una estrella porno, alternativamente, luchando por sobrevivir mientras peleo contra los planes feministas, y tú ni siquiera puedes compartirme tus migajas, bastardo. Nadie entiende. Nadie."

"¿No estarían las feministas en contra de la pornografía en primer lugar?"

hi "¿Esta cosa de los planes feministas otra vez?"

ke "Esta cosa es importante. Puedo ver que te importa un carajo, pero esto es serio, aquí. Feministas… son un enemigo peligroso, no cometas errores. Tómalas a la ligera, y despertarás en la mañana con un cuchillo en la espalda, ¡bam! ¡De la nada!"

hi "¿Cómo te despiertas en la mañana si alguien te apuñaló mientras dormías?"

show kenji happy_naked
with charachange

ke "Las mujeres son terribles para apuñalar cosas."

hi "Pensé que apenas habías dicho que no las tomara a la ligera."

show kenji neutral_naked
with charachange

ke "Bueno, no las tomes a la ligera en las cosas grandes. Individualmente no son una amenaza, pero si hubiera algún tipo de guerra, como una gran guerra, con los hombres de un lado, y las fuerzas feministas del otro, sería muy feo."

show kenji tsun_naked
with charachange


ke "Y ese día llegará, cuando las feministas salgan de su cuartel general central feminista mundial ultra secreto en todo el mundo, y digan “¡Ahora es cuando, hijos de puta!”."

hi "Estás siendo ridículo, no hay tal gran edificio del “cuartel general feminista mundial”, ¿dónde iban siquiera a esconder eso?"
hi "Quiero decir, tendría que ser masivo, no podrías esconder eso en la Tierra, alguien notaría una gran fortaleza con solo mujeres dentro."

show kenji happy_naked
with charachange

ke "¿Quién dijo que estaba en la Tierra?"


"Le doy la espalda a Kenji y comienzo a practicar caras amenazantes en un espejo para poder descubrir qué tipo de gesto expresará mejor mis emociones. No puede verme desde esta distancia de todas formas."

"Lo que, desafortunadamente, significa que él solo continúa despotricando sin ninguna consideración a la sensatez o sensibilidad."

show kenji tsun_naked
with charachange

ke "Sin duda, hay una guerra llevándose a cabo. Una guerra de la que no muchos saben, pero es una enorme que un día se desbordará, y abarcará todo el mundo conocido."
ke "Entonces, tendremos que elegir bandos. Tendremos que tomar una postura. De hecho, está sucediendo justo ahora."

ke "Imagínalo, el sangriento campo de batalla. Un conflicto brutal sin final."

ke "Casi me di por vencido, cuando pensé que esta causa era tonta… Cuando me cansé de la crudeza de nuestra pelea… Cuando confundí la vez en que se fue la luz por un asalto feminista, y pensé que el final estaba cerca…"

ke "Pero después me di cuenta de que si me rendía, todo acabaría, fue como, “epa” y supe que tenía que ir en serio. Porque soy el último hombre cuerdo en un mundo de locos. Es sobre el deber."

hi "Debe ser un movimiento de porquería si todo se mueve alrededor de un tipo desnudo, despotricando en un baño a otro tipo desnudo."

show kenji neutral_naked
with charachange

ke "¿Entonces puedes darme el dinero?"

"Está bloqueando el camino de salida, está empezando a hacer frío porque aún estoy desnudo, y quiero ir a clase, así que accedo a pasarle el dinero."

show kenji happy_naked
with charachange

ke "Formidable. Gracias, chico. Debemos ir a los bolos en alguna otra ocasión."

hi "¿Bolos?"

ke "Sin duda, es el máximo deporte. Casi no hay mujeres jugadoras de bolos tampoco, haciéndolo también el deporte más varonil."

ke "¿Debo de vestir mi playera rosa de bolos con su juego de zapatos o el verde pastel con flores resaltadas?"

hi "¿Hay ropa de bolos?"

show kenji neutral_naked
with charachange

ke "Tal vez."

hi "Como sea, mejor me pagas lo que te presté."

ke "Puedo pagártelo con cosas, ¿cierto?"

"No tengo el tiempo para pedirle que me explique lo que eso significa."

hi "No lo sé. Tengo que ir a clase, tú estás como atravesándote."

show kenji tsun_naked
with charachange

ke "Oh. Perdón. Seguro, no quiero retrasarte, y tengo algunas cosas que hacer también. El momento ha llegado."

hi "¿El momento para qué?"

show kenji happy_naked
with charachange

ke "Solo me gusta decir eso."

ke "Está bien, ahora el momento ha llegado en verdad."

hi "¿Para qué?"

show kenji tsun_naked
with charachange

ke "Tengo que usar el baño. Salte de ahí."

hi "¡Estaba por hacerlo! ¿Y qué significa eso? Es un baño grande."

ke "¿Y? Tengo que estar solo o no puedo ir. La presión…"

hi "Está bien. ¿Y si alguien más entra?"

ke "…"

ke "Pensaré en algo."

"Le lanzo mi gesto practicado y luce un poco tonto reflejado en sus anteojos. Él, o no lo nota, o no lo ve, de todas maneras, así que me visto y vuelvo corriendo a mi habitación, sintiendo como que ha pasado una eternidad desde que me desperté."

stop music fadeout 2.0

scene bg school_dormhisao
with locationskip

"Eso es un tiempo que nunca recuperaré. Le haré pagar por esto de alguna forma."

"Pero justo ahora, tengo que ir a clase."





label es_A21:

scene bg school_scienceroom
with locationskip

play music music_normal fadein 2.0

"Soy la primera persona en el salón, aunque creo que he llegado demasiado temprano. Por otra parte, sentarme solo aquí durante 20 minutos seguro es mejor que tener que sufrir ese tiempo con Kenji."

"La combinación de fatiga, frustración y aburrimiento comienza a hacerme sentir muy cansado."

"Me desvanezco por un segundo, despertándome cuando mi cabeza golpea la superficie de mi pupitre."
"Frotándome la frente, me doy cuenta de que esta es una razón tan buena como cualquier otra para quedarme despierto y después dejar de venir tan temprano a clases."

"Eventualmente escucho un golpeteo afuera, en el pasillo, y la alta figura de Lilly aparece en la puerta. Ella no está en este grupo, así que debe tener algún otro asunto. Tal vez esté buscando a Hanako."

"Lilly se detiene en la puerta, mostrándose vacilante como si fuese una vampiresa que no puede entrar a menos que la inviten. Considero hacerlo ya que ella se ve bastante solitaria parada ahí."

"Sin embargo, entra al salón por su propia cuenta, tras alisar su falda y el cuello de su blusa como si fuese importante verse remilgada al entrar a nuestra aula."

show lilly cane_concerned at left
with charamoveinleft

li "Con permiso."

"Llama al callado salón con una delicada voz indagadora. Me percato de que el silencio puede ponerla nerviosa a causa de su ceguera, así que lo rompo."

hi "Buenos días, Lilly."

show lilly cane_surprised at left
with charachange

show lilly cane_surprised at center
show bg school_scienceroom at bgright
with charamove

li "¿Hisao? Buenos días. No te escuché entrar."

"Me pregunto si ella piensa que es sospechoso que no le haya dicho nada antes. Es probable. Si digo una mentira demasiado grande, me hundiría."

hi "Bueno, es que ya estaba aquí, solo dormido hasta recién."

show lilly cane_listen
with charachange

li "Oh. ¿Has visto a Hanako hoy, por casualidad?"

hi "No, ella parece venir justo antes de que suene la campana… o después de ello. ¿Quieres que le diga algo de tu parte?"

show lilly cane_weaksmile
with charachange

li "No, está bien. Es extraño, pero creo que de momento somos las únicas dos personas en la escuela. No escuché a nadie más en mi camino hacia aquí."

hi "Creo que no debí haberme levantado tan temprano hoy."

show lilly cane_smile
with charachange

li "¿Te estás castigando por hacer algo que las demás personas deberían? La puntualidad es algo bueno. Eso pienso, de cualquier manera."

show lilly cane_concerned
with charachange

li "La de hoy es una mañana muy ajetreada. El festival está por llegar, y hoy es la fecha límite para el registro de eventos, reportes presupuestales, y cualquier otro papeleo oficial."

show lilly cane_weaksmile
with charachange

li "Podría ser que todos están intentando completar los formularios a último momento. Quizá sea ese el motivo por el cual hoy está tan callado."

play sound sfx_doorslam

show lilly cane_surprised
with vpunch

mi "¡Hola~ hola~!"

show shizu behind_blank at offscreenright
show misha hips_grin at offscreenright
with None

show lilly cane_surprised at left
show misha hips_grin at center
show shizu behind_blank at right
show bg school_scienceroom at bgleft
with charamove

hide misha
show misha hips_grin behind shizu
with None

"Misha aparece dentro del salón en el momento justo en el que entra Shizune, gritando con una intensidad que hace a Lilly estremecerse visiblemente."

show misha hips_smile
with charachange

mi "¡Qué tal, Hicchan~!"

hi "Qué tal."

show shizu behind_smile
with charachange

shi "…"

show misha hips_grin
with charachange

mi "¡Mira, es la representante del grupo! ¡Hola~!"

show lilly cane_smile
with charachange

"Lilly sonríe, probablemente entretenida por el uso de Misha —o el de Shizune— de la palabra “mira”."

show lilly cane_smile
with charachange

li "Buenos días."

show shizu adjust_smug
with charachange

shi "…"

show misha cross_smile
with charachange

mi "Claro, tú no eres la representante de este grupo, cierto, ¿cierto~?"

show lilly cane_weaksmile
with charachange

li "No lo soy."

"Lilly se ve más a la defensiva en sus respuestas a Shizune que conmigo el otro día. Creo que en verdad no se llevan para nada bien."

"Entonces me doy cuenta de que Lilly quizás no sepa que Shizune está presente y que esté intentando detectar si ella está o no, para saber con quién está hablando."

"Pues todo lo que ella sabe es que está hablando con Misha, pero sabiendo que ella y Shizune son prácticamente inseparables, puede que espere que sea Shizune quien realmente “habla”."

"Maldición, qué complicado. Decido ayudar a Lilly, por mi propia tranquilidad más que por cualquier otra cosa."

hi "Llegaste temprano, Shizune."

show shizu basic_angry
with charachange

shi "…"

show misha hips_frown
with charachange

mi "¡Estabas aquí más temprano que nosotras!"

"Misha infla sus mejillas con enojo. ¿Por qué se está enojando? ¿Acaso siente emociones por parte de Shizune, también?"

"No es tan raro, sin embargo, que a Shizune no le haya gustado mi pequeño comentario. Es cierto, yo estaba aquí más temprano que ellas, así que decir algo como eso pudo haber sido malinterpretado, definitivamente."

"Especialmente por Shizune, quien no tiene el beneficio de poder escuchar el tono de voz para medir intenciones."

"Antes de que pueda empezar a sopesar si debía o no pedir disculpas, Shizune ya lo ha dejado atrás."

show shizu adjust_smug
with charachange

shi "…"

show misha hips_smile
with charachange

mi "¡Representante~! ¡Qué bueno que estás aquí~! Tenemos que hablar."

show shizu behind_frown
with charachange

shi "…"

show misha hips_grin
with charachange

mi "El festival llega en tres días, ¿cierto? ¡Todos los otros grupos ya han entregado sus informes presupuestales proyectados para sus eventos! ¡Incluso los de primer año! ¡Excepto tú~!"

show misha cross_laugh
with charachange

mi "¡Guajaja~!"

show lilly cane_surprised
with charachange

li "Todavía hay tiempo para entregarlo, ¿no es así?"

stop music fadeout 2.0

show shizu cross_angry
with charachange

shi "…"

show misha cross_frown
with charachange

mi "¡Hoy! ¡La fecha límite es hoy! Sí que te estás tomando tu tiempo, ¿no es así? Si yo pudiese hacer las cosas a mi modo, hubiera tenido todo el papeleo hecho hace días, pero ¡alguien~! tuvo que decir “¡por favor, extiende la fecha límite~!”."

show lilly cane_displeased
with charachange

li "Sí, esa fui yo. Planear algo a esta escala no es una tarea sencilla, y una semana es un margen de tiempo demasiado corto para esperar que un grupo entero resuelva por completo un asunto tan complejo como este."

show shizu adjust_angry
with charachange

shi "…"

show misha hips_frown
with charachange

mi "¿Quieres saber qué es más difícil que distribuir los fondos para los eventos de un grupo? ¡Manejar lo mismo para todos los grupos en la escuela y aún más~! ¡La que hace eso soy yo!"


"Misha coloca sus manos en las caderas y se para derecha. Impresionante, realmente está poniéndose en su papel. Sin embargo, Lilly parece no encontrarle la gracia."

hi "Oye, Shizune, ¿no estás siendo un poco dura con ella? Todavía queda un día entero."

show lilly cane_weaksmile
with charachange

li "Por favor, Hisao. Está bien."

"Lilly parece contenta de que yo esté tomando su lado, pero a la vez un poco conflictuada de que quizá piense que no puede valerse por sí misma."

show lilly cane_listen
with charachange

li "Si esto es por el presupuesto, entonces me decepciona que pienses que me haya olvidado de él. Entiendo lo importante que es."

show shizu behind_frustrated
with charachange

shi "…"

show misha hips_grin
with charachange

mi "¡Entonces~! ¿Puedes dármelo, por favor?"

hi "Shizune, quizá ella no lo tenga en este preciso momento."

show lilly cane_displeased
with charachange

li "No está aquí en este momento. Le pedí a dos estudiantes que se encarguen de ello por mí. Estudiantes de mi grupo."

"Enfatiza la última oración para mi sorpresa. ¿Sabe de los intentos de Shizune y Misha para arrastrarme al consejo estudiantil?"

"Creo que se debe haber corrido la voz, así que ahora me está utilizando como munición contra Shizune. Esto se está poniendo cada vez mejor…"

show shizu cross_angry
with charachange

shi "…"

show misha hips_frown
with charachange

mi "¡Era tu responsabilidad~! Un informe de presupuesto no es algo que deberías estar delegando así como así; como representante de grupo, ¡es tu trabajo estar siempre atenta de todo!"
mi "¡Este tipo de indiferencia ante el procedimiento adecuado es realmente terrible~!"

show lilly cane_listen
with charachange

li "Lo completaron, siendo capaces de hacerlo, pero los estudiantes han estado enfermos recientemente, así que no pudieron venir a la escuela y dármelo de vuelta. Si así deseas, puedo disculparme de su parte por haberse enfermado."

show misha hips_grin
with charachange

mi "¡Está bien~!"

"Aunque Misha no se da cuenta de la pequeña indirecta de Lilly, Shizune sí, y parece estar dividida entre sentirse ofendida por el atrevimiento de Lilly y saltar de alegría ante la posibilidad de un desafío."


show shizu behind_frown
with charachange

shi "…"

show misha hips_smile
with charachange

mi "Lilly, ¿acaso no viven aquí en la escuela? Es una caminata de cinco minutos, sabes~."

mi "¿Qué podrían tener que les impide tomarse 5 minutos de sus ocupadas vidas… para dejar algo que afectará el goce del grupo entero?"

show shizu adjust_angry
with charachange

"Lilly abre su boca para decir algo, pero Shizune cierra la distancia entre ellas y comienza a gesticular furiosamente, agitando las manos como un director de orquesta."

"Misha hace su mejor esfuerzo para transmitir la misma pasión, pero parece no perder su tono alegre. El resultado es interesante y un tanto surrealista."

shi "…"

show misha cross_frown
with charachange

mi "¿Y qué pasa con esa actitud~? Dije que no es algo que deberías estar delegando; eres la representante del grupo ¿o no?"

show misha hips_frown
with charachange

mi "Dime los nombres de esos dos estudiantes, ellos deberían tener tu trabajo si ni siquiera puedes estar a cargo de algo tan simple tú misma."

show lilly cane_displeased
with charachange

li "Un formulario no es la totalidad de lo que se supone debo hacerme cargo."

"El tono de Lilly está tornándose ligeramente impaciente, pero está haciendo un buen trabajo en no dejar ver a Shizune lo molesta que se está poniendo. Está jugando con sus cartas cerca de su pecho."

"Shizune, por otra parte, envuelve la orilla de sus anteojos alegremente con sus dedos, sabiendo que Lilly no puede ni oír ni ver lo emocionada que está."

show shizu adjust_smug
with charachange

shi "…"

show misha hips_grin
with charachange

mi "¡Por supuesto, haces tanto, representante~! ¡Debe ser tan complicado ser tú~!"

show lilly cane_listen
with charachange

"Lilly aprieta sus labios con las palabras de Misha, entendiendo claramente la intención detrás de ellas aun a pesar de que Misha las pronuncia sin siquiera una pista del sarcasmo que se supone deben tener."

"Shizune y Lilly no se llevan bien, eso está claro, pero esto parece un poco extremo. Parece que Lilly ha tenido suficiente y está lista para contraatacar."

play music music_tension

$ wdt_off(False)

scene black
with Dissolve(0.2)

show showdown_lilly_slice at Transform(xanchor=0.0, xpos=1.0, yalign=0.0)
show showdown_shizu_slice at Transform(xanchor=1.0, xpos=0.0, yalign=1.0)
with None

play sound sfx_draw
show showdown_lilly_slice at Transform(xalign=0.0, yalign=0.0)
with slice_in

with Pause(0.2)

play sound sfx_draw
show showdown_shizu_slice at Transform(xalign=1.0, yalign=1.0)
with slice_in

with Pause(0.2)

play sound sfx_thunder
scene ev showdown
with Fade(0.2, 0.0, 3.0, color="#FFF")


play sound sfx_slide2
show ev showdown_large:
    size (800,600) crop (0, 0, 2400, 1800) subpixel True
    easeout 0.2 crop (280, 100, 800, 600)
with None

window show

li "De hecho estaba discutiendo el reporte presupuestal antes de que llegases. Debes ser muy talentosa para haber terminado todos tus deberes del consejo estudiantil tan rápido que puedas rastrearme para asegurarte de que no olvide los míos."

play sound sfx_slide
show ev showdown_large:
    ease 0.2 crop (1400,160, 800, 600)
with None

mi "¿Me estás acusando de haraganear? ¡Parece que estás confundiéndome contigo misma~!"

play sound sfx_slide2
show ev showdown_large:
    ease 0.2 crop (280,100, 800, 600)
with None

li "No lo creo. Eso sería algo muy difícil de hacer para mí; compararme contigo."


play sound sfx_slide2
show ev showdown_large:
    ease 0.2 crop (1400,160, 800, 600)
with None

mi "Tienes razón, la diferencia entre nosotras es como el cielo y el infierno."

play sound sfx_slide
show ev showdown_large:
    ease 0.2 crop (280,100, 800, 600)
with None

li "Y no es difícil adivinar cuál de los dos representarías tú."

$ _window = False

play sound sfx_thunder
scene ev showdown
with Fade(0.2, 0.0, 1.5, color="#FFF")

window show

"El aire entre ellas se riza con el calor de su enemistad. Bueno, no realmente. Sin embargo ya no pueden disimularlo. Incluso Misha parece que comienza a entender la verdadera naturaleza de esta conversación."

stop music fadeout 5.0

scene bg school_scienceroom
show lilly cane_listen at left
show misha perky_confused at center
show shizu basic_angry at right
with flash

shi "…"

show misha sign_confused
with charachange

mi "¡Hicchan~! ¡No estés de holgazán tú tampoco~!"

hi "¿De qué estás hablando?"

show shizu basic_frown
with charachange

shi "…"

show misha hips_smile
with charachange


mi "¿No vas a formar parte del festival, Hicchan? Lo harás, ¿verdad? ¡Entonces~! ¡Espero hagas mucho más que esta persona para asegurarte que no haya contratiempos~!"

label es_choiceA21:
menu:
    with menueffect
    "No entiendo por qué Shizune se está enojando conmigo."
    "¡No me arrastres a esto! ¡He hecho mi parte!":



        return m1
    "Oigan, vamos. No sean tan duras con Lilly y conmigo…":

        return m2

label es_A21a:

hi "¿Por qué estoy siendo arrastrado a esto? Creo que he hecho más que suficiente."

hi "Si estás enojada con Lilly, eso no tiene nada que ver conmigo."

show lilly cane_reminisce
with charachange

li "Ahora, espera tan solo un segundo… ¿estás insinuando que la presidenta tiene más razón en regañarme a mí que a ti?"

"Ah, maldición, creo que pude haberlo dicho de una mejor manera."

hi "No, no sé nada al respecto pero… lo que quiero decir…"

show shizu behind_frown
with charachange

shi "…"

show misha perky_confused
with charachange

mi "¿Qué estás diciendo, Hicchan?"

hi "Es solo que difícilmente pienso que es justo que puedas decir eso, viendo que las he ayudado."

"El ambiente ha cambiado. Esto es como un duelo entre dos pistoleros ahora. Bueno, antes también era así, pero ahora la atención de Shizune está puesta en mí."

"Y la de Lilly también, aunque se mantiene callada. Me temo que la hice enojar mucho sin darme cuenta."

show shizu cross_angry
with charachange

shi "…"

show misha hips_frown
with charachange

mi "¿Estás diciendo que estoy equivocada?"

"Qué situación más peligrosa."

hi "Es muy temprano para discutir contigo… Sí, creo que es injusto de tu parte que me saltes encima."

show shizu behind_frustrated
with charachange

shi "…"

show misha hips_smile
with charachange

mi "¡Hicchan, quieres demasiado~! ¡Pero~! Tienes un punto a favor. ¡Está bien, está bien~! No eres un flojo, Hicchan."

show misha hips_laugh
with charachange

mi "¡Jajaja~!"

"Shizune empuja sus anteojos hacia arriba con su pulgar, casi en un ademán de aprobación."

show shizu adjust_happy
with charachange

shi "…"

show misha perky_smile
with charachange

mi "¡Eso está bien! ¡Si no eres inútil, no debes dejar que nadie diga que lo eres~!"
mi "¡Pero la próxima vez que lo diga, realmente será así porque me estarás decepcionando como la señorita representante de grupo aquí presente, así que no permitas que se te suba a la cabeza!"

show lilly cane_displeased
with charachange

"Lilly entiende la indirecta, una expresión venenosa congelada en su rostro."

show misha hips_smile
with charachange

mi "¡Representante~! Shicchan dice: “¡No te olvides de ese informe, por favor~!”."

li "No lo haré."

show lilly cane_listen
with charachange

li "¿Sería eso todo?"

show misha hips_grin
with charachange

mi "¡Síp~!"

li "Entonces, buen día a todos."

"Su voz hubiera cortado el aire del salón a la mitad, si este fuese más tangible."

hide lilly
with charaexit

"Lilly deja el salón, comprensiblemente de mal humor pero aun así logrando verse con aplomo y tranquila como es usual."

show misha hips_grin at twoleft
show shizu adjust_happy at tworight
show bg school_scienceroom at bgleft
with charamove

hi "Shizune, realmente te pasaste un poco hoy."

show misha perky_smile
with charachange

mi "Es cierto, Shicchan, solo un poco~."

"Si hubiese estado esperando que Shizune admitiera a regañadientes que yo tenía la razón también en eso, creo que habría esperado demasiado. Ella no responde."

show shizu basic_normal2
with charachange

shi "…"

show misha cross_laugh
with charachange

mi "¡Jajaja~! Shicchan piensa que deberías meterte en tus propios asuntos."

show misha hips_smile
with charachange

mi "¡Hicchan, tenemos unas cosas de último minuto que hacer antes de clases~! Podríamos llegar tarde, ¡así que~! ¿Puedes, por favor, cubrirnos?"

hi "Seguro."

show misha cross_grin
with charachange

mi "¡Perfecto~! ¡Viva~! ¡Muy bien~! ¡Gracias, Hicchan!"

hide misha
hide shizu
with charaexit

"Caminan hacia afuera aunque faltan solo diez minutos antes de que suene la campana, indicando el comienzo de las clases."



label es_A21b:

hi "Oigan, soy el chico nuevo, ¿recuerdan?"

hi "No es como si pudiese haber hecho mucho, incluso si quisiera."

show lilly cane_displeased
with charachange

li "Eso es cierto, no deberías esperar que un estudiante de intercambio se meta de lleno en su primera semana."

"Que Lilly esté de mi lado se siente extrañamente cómodo así que decido apoyarla también."

hi "Sí, estás siendo irracional con nosotros dos."

show shizu behind_frustrated
with charachange

shi "…"

show misha hips_frown
with charachange

mi "Excusas, excusas. La señorita representante de grupo ha tenido tiempo de sobra para presentar su informe."

mi "Y te ofrecimos repetidamente una posición para ayudar con el trabajo del consejo estudiantil, pero te rehusaste a comprometerte a hacer del festival un éxito."

hi "Sí, pero como dije antes, no estoy seguro de si…"

"No tengo tiempo para esto ahora; no importa lo que haga, significará meterse en una confrontación con Shizune, y eso es lo que ella quiere."

hi "Como sea. Olvídalo."


label es_A21c:

"Les doy la espalda."

hide shizu
hide misha
with charaexit

show lilly cane_displeased at center
show bg school_scienceroom at bgright
with charamove

hi "Lilly, las clases empezarán pronto, así que podemos seguir hablando después. Le diré a Hanako que la estabas buscando."

"Puedo sentir a Shizune congelarse. Quizá esta sea la primera vez que ha sido ignorada de una manera tal."

show lilly cane_smile
with charachange

li "Gracias, Hisao, me voy, entonces."

"Lilly me da la sonrisa más dulce que he visto toda la semana, y da media vuelta para salir."

hide lilly
with charaexit

"Tan pronto como Lilly sale por la puerta, repentinamente me siento indeciso a darme vuelta para encarar a Shizune."

"Puedo sentir sus ojos quemándome la espalda, y no puedo juntar el coraje para mirarla. Debe estar furiosa. Sigo esperando que Misha diga algo para aliviar la tensión, pero realmente es pedir demasiado."

"Al final, vuelvo a mi asiento y escucho el sonido de los pasos de Shizune mientras marcha fuera del aula. No vuelve hasta pocos minutos antes de la clase."



label es_A21d:

hide shizu
hide misha
hide lilly
with charaexit

"Les doy la espalda."

"Regreso a mi asiento y apago mis oídos para no escuchar el gran final de la discusión entre Lilly y Shizune."

"Eventualmente, Lilly abandona nuestro salón y tanto Shizune como Misha se sientan, sin hablarme."

"Puedo sentir los ojos de Shizune quemándome la espalda. Probablemente está enojada conmigo, pero yo estoy igual de enojado con ella."

"No comprendo por qué ella tuvo que arrastrarme a la discusión."





label es_A22:

scene bg school_scienceroom at bgleft
with shorttimeskip

play music music_daily fadein 0.5

"Hanako no viene a las clases de la mañana en lo absoluto, dejando un asiento vacío y solitario en la parte de atrás del salón."

"Debo decirle que Lilly la estaba buscando si la veo más tarde."

"Tras los eventos de esta mañana, la clase es bastante aburrida en comparación. Doy vuelta a las páginas de mi libro de texto con pereza."

"Hemos estado cubriendo la misma cantidad de páginas cada día, así que leer más adelante es más o menos darme un avance de lo que se tratará la lección de mañana."

"El reloj al frente del salón suena insoportablemente alto. El maestro no ha dicho nada en más de siete minutos, optando en vez de ello cubrir el pizarrón con filas y filas de ecuaciones sacadas directamente del libro."

"El rítmico choque de la tiza contra el pizarrón parece sincronizarse perfectamente con el tic-tac del reloj."

show misha cross_smile_close at offscreenleft
with None

show misha cross_smile_close at Transform(xpos=0.1, xanchor=0.5)
show bg school_scienceroom at center
with charamove

"Comienzo a copiar las ecuaciones solo para pasar el tiempo, sin notar la cabeza de Misha asomándose por sobre mi hombro hasta que está casi completamente arriba de mí."

hi "¿Qué estás haciendo?"

"Intento balancear entre decirlo lo suficientemente bajo como para no llamar la atención de la clase, pero lo suficientemente fuerte para atraer la de ella."

show misha cross_grin_close
with charachange

show misha cross_grin_close at twoleft
show bg school_scienceroom at bgright
with charamove

mi "¿Qué estás haciendo, Hicchan~?"


"El pánico se dispara dentro de mí cuando Misha comienza a hablar en su volumen normal, y suelto una respuesta apresurada manteniendo mi voz baja, a pesar de que ella acaba de destruir cualquier esperanza que pudiese haber tenido de ser discreto."

hi "Estoy copiando esas cosas, ¿qué estás haciendo tú? ¿Por qué tan fuerte?"

show misha perky_confused_close
with charachange

mi "Ooh~, ¿en serio? Pero si está todo en el libro… ¡Por eso nadie más lo está copiando~!"

hi "Ya sé, ¿por qué estás hablando tan fuerte?"

show misha hips_grin_close
with charachange

mi "¿Por qué hablas tan bajito, Hicchan? Es difícil escucharte."

"Miro alrededor para ver si alguien notó nuestra conversación y es bastante obvio que todos lo han hecho, incluso el maestro."

show shizu behind_smile at right
with charamoveinright

"Shizune sonríe con timidez, y comienzo a preguntarme si Misha está haciendo esto porque ella le dijo."

"¿Es esto por lo que ocurrió entre ella y Lilly antes?"

"¿Es esto lo que me toca por intentar ser razonable? ¿Por intentar tomar el camino medio? Shizune es excesivamente orgullosa de sí misma, aunque a estas alturas debo saber esperar esa clase de actitud de su parte."

hi "¿Por qué estás haciendo esto?"

show misha perky_confused_close
with charachange

mi "¿Eh?"

"Misha es totalmente ajena a la mirada incómoda que el maestro nos da a ambos, mientras trata de balancear el libro de texto en un dedo."
"Por un breve segundo parece como si las cosas podrían ponerse feas, pero el maestro simplemente aleja la mirada, como si no valiese la pena."

"Supongo que esto es algo bueno, y me desplomo aliviado en mi asiento."

scene bg school_scienceroom at bgright
with shorttimeskip

"El resto del día pasa sin sobresaltos, y esta vez soy capaz de apreciar que así lo fue."

play sound sfx_normalbell

"Cuando suena la campana, no estoy apurado, así que me quedo un rato, repasando lo que vimos en clase hoy. Prefiero salir último de todos modos, así no tengo que lidiar con toda esa gente en los pasillos."

"Noto que Shizune y Misha también se quedaron atrás, hablando con alguien de otro grupo."

"Shizune está haciendo señas tan rápido que sus manos hacen ruidos que me recuerdan a espadas atravesando el aire."

"Misha está intentando desesperadamente ir a su par, pero es obvio que apenas puede siquiera entenderla."

"Agacho la cabeza. Lo que sea que estén discutiendo parece un asunto serio. Probablemente algo que me supera."
"No solo eso, sino que también Shizune parece enojada, aunque puede simplemente ser su severidad natural haciéndola aparentar eso."

"Shizune hace señas al punto tal que sus muñecas hacen ruido, y Misha lucha para escupir su equivalente vocal."

"A veces se tropieza con las oraciones como si estuviese lidiando con trabalenguas. Y además de eso, tiene que traducir a lenguaje de señas todo lo que la otra chica le está diciendo."

"Parece un trabajo duro."

"Misha se ve cansada, casi como si estuviera por desvanecerse."

"Afortunadamente para ella, su asunto termina pronto y las chicas vuelven a sus asientos una vez más."

show shizu behind_blank at tworight
show misha perky_sad at twoleft
with charaenter


mi "¡Uwaaah! ¡Qué cansada estoy!"

"Misha cuelga la cabeza sobre su banco, viéndose exhausta."

hi "Los preparativos para el festival deben de ser duros para ustedes."

"Efectivamente, parece que la gente en esta escuela se toma el festival muy en serio. Cada vez que veo gente pasando el rato antes y después de clases están siempre hablando acerca de sus planes para ello."

"Es algo estupendo ver que todos están tan entusiastas al respecto."

"Probablemente yo sea el único que no tiene algo para hacer."

show shizu basic_normal
show misha perky_confused
with charachange

"Shizune comienza a hablar en lenguaje de señas y Misha se reanima, mirando sus manos con ojos levemente fuera de foco."

show shizu behind_frown
with charachange

shi "…"

"Ella hace señas con movimientos fuertes, pesados, dramáticos."

"Misha traduce sus señas en habla para mí."

"Lo hace tan bien que es casi como si Shizune estuviera realmente hablando, transmitiendo sus pensamientos directamente a través de Misha."

show misha cross_frown
with charachange

mi "Bueno, estamos en el consejo estudiantil, sabes, así que estamos bastante ocupadas."

hi "¿Sarcasmo?"

show misha perky_confused
with charachange

mi "¿Eh?"

"El tono de las acciones de Shizune me hace pensar que ella está “hablando” con desdén, pero Misha lo interpreta normalmente, reemplazando cualquier intención que pudiera haber tenido con su propio giro alegre de las cosas."
"Todavía es desorientador, no creo que algún día me acostumbre."

hi "No importa."

hi "¿Cómo podría olvidarme, con ustedes dos intentando hacer que me una al menos dos veces al día?"

show misha cross_laugh
with charachange

mi "¡Jajaja~! Pero, Hicchan, algunos podrían decir que el trabajo es demasiado."

show shizu basic_normal2
with charachange

show misha perky_sad
with charachange

mi "Sería agradable si los estudiantes mostraran un poco más de apoyo a su liderazgo, un poco de aprecio a quienes están trabajando tan duro para hacerlo todo posible."

show shizu behind_frown
with charachange

show misha perky_smile
with charachange

mi "Quizás, por ejemplo, un poco de ayuda. Eso no es pedir demasiado, ¿no es cierto? ¡Síp~! ¡La ayuda sería apreciada~! ¡De estudiantes como tú~!"

show shizu adjust_angry
with charachange

show misha hips_frown
with charachange

mi "Si los estudiantes mostrasen su dedicación y espíritu escolar, y ofrecieran su ayuda, bueno, no la necesito exactamente…"

show shizu behind_smile
with charachange

show misha hips_smile
with charachange

mi "Pero tampoco la rechazaría necesariamente… ¡Así que~! Sería lindo si alguien lo hiciera…"

stop music fadeout 2.0

show shizu adjust_blush
show misha perky_confused
with charachange

mi "¿Oh? ¡Hola~!"

show shizu adjust_blush at offscreenleft
show misha perky_confused at Transform(xanchor=0.5, xpos=-0.45)
show bg school_scienceroom at bgleft
with charamove

show hanako emb_timid at Transform(xanchor=0.5, xpos=0.93)
with charamoveinright

play music music_pearly fadein 1.0

"Miro por sobre mi hombro y veo a Hanako mirando tímidamente hacia el salón de clases, la mayor parte de su cuerpo escondido detrás de la puerta."

show misha perky_smile at Transform(xanchor=0.5, xpos=0.15)
with charamove

mi "¡Oye! ¿Jugando a la delincuente otra vez?"

show hanako emb_blushtimid
with charachange

"Hanako se sonroja marcadamente por la pregunta tan directa de Misha, incluso si fue solo en tono de broma."

show shizu basic_angry at Transform(xanchor=0.5, xpos=0.35)
with charamove

shi "…"

show hanako emb_downsad
with charachange

show hanako emb_downsad at Transform(xanchor=0.5, xpos=0.97)
with charamove

"Shizune la mira de forma penetrante, causando que Hanako mire hacia abajo y comience a alejarse al punto tal donde solo sus dedos pueden verse asiéndose nerviosamente del borde de la puerta."

"Tal vez esté mostrando su disgusto hacia Hanako por asociación de su disgusto por Lilly."

"Así parece, y probablemente Hanako lo sepa también."

"Parece que se han olvidado momentáneamente de hacer que me quede por el resto del día."

hi "¿Qué ocurre, Hanako?"

show hanako emb_timid
with charachange

ha "¿Ha p… pasado Lilly por a… aquí?"

mi "Lo lamento, no he visto a Satou. Aunque ella, eh, vino por la mañana."

show hanako emb_downtimid
with charachange


"Hanako sigue mirando con inquietud a Shizune, quien a su vez le lanza su mirada analítica usual. ¿Qué está intentando hacer?"

"Por supuesto que Shizune no va a apartar su mirada, y ella es suficientemente intimidante de por sí; así que solo puedo imaginarme lo aterrada que debe estar Hanako."

"Sin embargo es un poco gracioso, ver la reacción de Hanako ante la actitud normal de Shizune. Parece que esto es lo que ocurre cuando se juntan dos polos completamente opuestos."

show hanako emb_timid
with charachange

ha "¿Saben… saben d-dónde está?"

show shizu behind_frown
with charachange

shi "…"

show misha hips_frown
with charachange

mi "Si le queda algo de cerebro, está en su salón de clases, trabajando en su proyecto del festival. Pero quién sabe dónde está holgazaneando esa mujer."



label es_A22a:

show misha hips_grin at Transform(xanchor=0.5, xpos=0.15)
with charachange

mi "¡Debe estar perdiendo el tiempo en algún lado, justo como Hicchan~! ¡Guajaja~!"

"Maldición, ¿qué pasa con Shizune y su necesidad de señalar cosas como esta?"



label es_A22b:

scene bg school_scienceroom at bgleft
show shizu behind_frown at Transform(xanchor=0.5, xpos=0.35)
show misha hips_frown at Transform(xanchor=0.5, xpos=0.15)
show hanako emb_timid at Transform(xanchor=0.5, xpos=0.97)
with None


mi "¡Debe estar perdiendo el tiempo en algún lado~! ¡Qué mujer más inútil~!"

show hanako emb_downtimid
with charachange

hide hanako
with easeoutright

"Hanako asiente con rapidez y se retira apresurada, obviamente para evitar cualquier contacto adicional con Shizune. Desafortunadamente, esto regresa su atención por completo hacia mí."

stop music fadeout 2.0

show shizu behind_frown at tworight
show misha hips_frown at twoleft
show bg school_scienceroom at bgright
with charamove

show misha hips_grin
show shizu behind_smile
with charachange

mi "Pero Hicchan no es inútil, ¿cierto? ¿Cierto? ¡Él mismo lo dijo~! ¡Guajaja~!"

"Puedo ver a dónde va esto, y no deseo formar parte de ello, no después de aquella experiencia ayer."

hi "Bueno, buena suerte con sus preparativos…"

"Comienzo a guardar las cosas en mi mochila, listo para echarme a correr a la salida."

"Desafortunadamente estoy hasta la otra punta del salón de clases."

"La corta distancia hasta la puerta me parece una vasta Tierra de Nadie ahora."

show misha perky_smile
show shizu behind_blank
with charachange

play music music_shizune fadein 4.0

show bg school_scienceroom at bgleft
show shizu behind_blank at center
show misha perky_smile at Transform(xalign=-0.15)
with charamove

show bg school_scienceroom at center
show shizu behind_blank at tworight
show misha perky_smile at twoleft
with charamove

"Tanto Shizune como Misha comienzan a maniobrar lentamente frente a mí, cortando mi ruta de escape de una manera inquietantemente cautelosa que me hace pensar en combates nave a nave."

show misha hips_grin
with charachange

mi "¡Creo que Shicchan está diciendo que deberías ayudarnos, Hicchan~!"

hi "Caray, no sabría, ella es tan sutil."

show misha perky_confused
with charachange

mi "¡Pero~! Esa es la intención, así que ¿por favor? No puedo seguir el ritmo, realmente tenemos que construir puestos para el festival, casi todos ellos por nuestra cuenta, ¿puedes creer eso?"

show misha perky_sad
with charachange

mi "Martillando tablas una sobre otra, una y otra vez, ¡es muy duro!"

mi "Estoy tan acostumbrada que estaba haciendo como si tuviese un martillo en mis manos durante clases, ¡y ni siquiera me había enterado!"

"Golpea su banco algunas veces, imitando golpes de martillo."

mi "Es tan repetitivo, ¡no lo soporto! Y ayer, martillé todas las tablas una arriba de la otra…"

mi "Era una pila de tablas todas clavadas juntas, y luego tuve que sacarle los clavos y hacerlo todo otra vez, ¡y me gritaron y se rieron de mí~!"

hi "Eh…"

show misha perky_smile
with charachange

mi "Entonces…"

show misha hips_grin_close
with characlose

"Misha aprieta una mano en mi hombro y sonríe, pasándose pícaramente la lengua por sus dientes."

mi "¿Tienes planes para hoy, Hicchan?"

mi "Me pregunto si los tienes~."

hi "Seguro que tengo planes…"

show misha perky_confused_close
with characlose

mi "¿De veras~?"

mi "Nos vas a ayudar, ¿verdad?"

"Noto que sus manos se están moviendo constantemente."

"Está traduciendo todo lo que ambos decimos para que Shizune pueda entender."

"Shizune está siendo algo callada hoy. ¿Seguirá enojada? Bueno, probablemente al menos un poco. Lo puedo ver en sus ojos. Aunque bien esta podría simplemente ser otra forma de hacerme sentir culpa y así darle una mano."

"Tengo que encontrar una forma para salir de esto."

hi "Oye, debería irme ahora, a la biblioteca. Tú sabes, tarea…"

hi "Debería irme, ¿no es verdad? Tengo que ser diligente, porque soy un nuevo estudiante y todo, así que tengo que dar una buena primera impresión, ¿verdad? Sí…"

hi "Entonces, ¡nos vemos luego!"

show misha perky_confused_close at offscreenleft
show shizu behind_blank at twoleft
show bg school_scienceroom at bgleft
with ease

hide misha
show misha perky_confused_close behind shizu at offscreenleft

show shizu basic_normal2 at offscreenright
show bg school_scienceroom at center
with ease_accel

show shizu cross_angry_close at tworight
show bg school_scienceroom at bgright
with ease_decel

"Me giro para irme corriendo a la puerta pero Shizune está bloqueando mi camino, con sus brazos cruzados sobre su pecho y una severa expresión en su rostro."

show shizu basic_angry_close
with charadistant

"Ella menea un dedo burlonamente y comienza a hablar en señas con Misha con la manera de una líder de escuadrón dándole instrucciones a sus compañeros soldados."

show shizu basic_angry
with charadistant

show misha perky_smile at twoleft
with charamove

mi "¡No parecía que estuvieras en algún apuro para ir a la biblioteca, Hicchan~!"

show misha hips_grin
with charachange

mi "Eso es cierto, Shicchan~, sí parece que iba a holgazanear por el resto del día, probablemente."

show misha hips_laugh
with charachange

mi "¡Jajaja~! ¡Guajaja~! ¡Estás rodeado~!"

show shizu behind_frown
with charachange

shi "…"

show misha hips_smile
with charachange

mi "¡Vamos al salón del consejo estudiantil~!"

"Suelta una pequeña risa, y luego rompe en carcajadas."

show misha cross_laugh
with charachange

mi "Lo lamento, Hicchan. Me siento mal, pero esto nos conviene a todos, ¿cierto?"

show shizu basic_normal2
with charachange

shi "…"

show misha sign_smile
with charachange

mi "¡Eso es cierto, Shicchan! Sí~, ese es un buen punto, también."

show shizu behind_blank
with charachange

shi "…"

show misha hips_smile
with charachange

mi "Sí, es beneficioso para todos, soluciona todos nuestros problemas."

show shizu basic_frown
with charachange

shi "…"

show misha hips_frown
with charachange

mi "¡Sí, sí~!, yo también pensé que apreciaría más nuestros esfuerzos."

show misha hips_frown_close
show shizu basic_frown_close
with characlose

"Se acercan hacia mí, como si fuesen a embestirme."

hi "Oigan, chicas, dos contra uno no es muy justo, ¿o sí?"

show shizu behind_blank_close
with charachange

shi "…"

"Ella sigue mirando hacia adelante, impasible, entonces da una siniestra sonrisa."

show shizu basic_sparkle_close
show misha hips_grin_close
with characlose

mi "¡Vamos, tenemos mucho trabajo por hacer! ¡Vamos al aula del consejo estudiantil~!"

hi "Caray, no lo sé…"

show misha cross_laugh_close
with characlose

"Misha se ríe."

show misha hips_grin_close
with characlose

mi "¿Déjà vu~?"

"Ella ríe disimuladamente, antes de soltar otra carcajada."

show misha cross_laugh_close
with characlose

mi "Jajaja, sabes, mi horóscopo decía que hoy sería un buen día para mí."

show misha perky_smile_close
with characlose

mi "Y ahora que vas a ayudar—{w=.5}{nw}"

show shizu adjust_smug_close
with charachange

"Shizune le dice algo con señas."

show misha hips_grin_close
with charachange

mi "¡Cierto~!, digo, ¡ahora que has decidido ayudarnos, completamente bajo tu propia voluntad, podré tomármelo con calma! Qué suerte~, ¿eh?"

"Abro mi boca para decir algo pero me percato de que no tiene sentido."

"Me vuelvo a concentrar en tratar de pensar en una manera para salir de esto. No, sus acciones son claramente intencionadas, no tiene sentido intentar razonar con ellas."

"No se puede razonar con los locos. Frunzo el ceño, y ni siquiera notan mi descontento, confirmando todavía más mis sospechas."


"Se ven muy relajadas ahora. Supongo que piensan que ya han ganado, así que bajan la guardia."

stop music fadeout 2.5

"Eso es un poco arrogante."

"Pasan por delante de mí a medida que se mueven por la puerta."

hide shizu
hide misha
with charaexit

"Y sigilosamente camino hacia atrás de vuelta al salón cuando salen al pasillo, girando hacia las escaleras."

"Suelto un suspiro de alivio y rápidamente guardo el resto de mis cosas para poder escapar."

play sound sfx_doorslam

"La puerta del aula se cierra de golpe."

play music music_running fadein 0.5

show shizu cross_angry at offscreenright with None
show misha cross_frown at offscreenleft with None
show shizu cross_angry at tworight
show misha cross_frown at twoleft
with ease

shi "…"

mi "Eso no fue muy agradable. Jajaja, aunque realmente nos engañaste. ¿No es verdad, Shicchan?"

show shizu behind_frown
with charachange

shi "…"

show misha hips_grin
with charachange

mi "Cierto, cierto… ¡Jajaja!"

show misha cross_frown
with charachange

mi "¿Qué fue eso? ¡Pensé que dijiste que nos ayudarías!"

mi "¡Y luego nos quedaste mal! Y pensaste que te saldrías con la tuya, ¿o no?"

show misha cross_laugh
with charachange

"La expresión de indignada se desvanece y comienza a reírse histéricamente, calmándose solo tras una agraviada mirada de Shizune."

show misha cross_grin
with charachange

mi "Oh, ah… Sí~, ¡pensaste que te podrías salir con la tuya! ¡Pero un criminal siempre regresa a la escena del crimen!"

"Ni siquiera logré salir del aula en primer lugar. No, espera, ni siquiera accedí en ayudar en primer lugar."

show misha perky_smile
with charachange

mi "No muy brillante, ¿o sí, criminal? Pensar que puedes eludir tus deberes así como así… ¡Qué bajo, Hicchan~!"

hi "¿Soy un criminal? ¿Qué hice? ¿Cuál es el cargo? ¿De qué soy culpable?"

show misha hips_grin
with charachange

mi "¡Eso lo decidirá la corte, criminal! ¡No creo que tengamos que decírtelo!"

show misha perky_smile
with charachange

mi "Además, tú eres el criminal aquí, ¡tú sabes lo que hiciste!"

hi "¿Alguna vez leíste “El Proceso” de Kafka?"

show misha hips_grin
with charachange

mi "No, ¿qué es eso, Hicchan~? ¿Qué tiene que ver con esto?"

hi "Lo leí hace unos meses. Es acerca de esta gente que hace un juicio sumario a un hombre que solo desea vivir su vida. Se niegan a dejarlo en paz, y no puede luchar contra el sistema."

show shizu basic_frown
with charachange

shi "…"

show shizu behind_frown
with charachange

shi "…"

show misha hips_smile
with charachange

mi "Hicchan, ¿y eso qué tiene que ver?"

show misha sign_confused
with charachange

mi "¡Oye~!, ¿qué significa eso?"

"Ella se vuelve hacia mí de nuevo tras intercambiar señas durante un largo rato."

show misha hips_frown
with charachange

mi "Sabes, las dos estamos un poco decepcionadas de ti. Nos has defraudado, Hisao."

show shizu basic_frown
with charachange

shi "…"

mi "Nos fallaste."

show shizu behind_frown
with charachange

shi "…"

mi "Nos dejaste colgadas. Y afuera en el frío~."

show shizu cross_angry
with charachange

shi "…"

show misha sign_smile
with charachange

mi "¿Es esa una manera de tratar a una persona? ¿Huir de tus responsabilidades, abandonar a tus camaradas?"

show misha hips_frown
with charachange

mi "Creemos que nos la debes para honrar tu compromiso."

hi "¿Qué? ¡Pero yo no me comprometí a nada~!"

"Mi respiración se atora en mi garganta y momentáneamente comienzo a ahogarme."

show shizu basic_frown
with charachange

shi "…"

show misha cross_smile
with charachange

mi "¡Eso no es cierto, Hicchan! Dijiste que no eras inútil, definitivamente lo dijiste, sí, definitivamente, definitivamente, ¡definitivamente~!"

show misha hips_grin
with charachange

mi "¡Estamos apelando a ti con esas palabras~! ¡Más vale que te prepares para demostrar que no eres un tipo inútil!"

mi "¡Tu honor quedará manchado por siempre si intentas escaparte de esta~!"

mi "Así que, por el resto del día, vamos a estar juntos, solo nosotros tres, ¡y trabajando duro!"

show shizu behind_frown
with charachange

shi "…"

show misha hips_smile
with charachange

mi "¡No puedes engañarnos!"

mi "Deberías estar feliz, estás haciendo un gran servicio por tu escuela. No preguntes lo que tu escuela puede hacer por ti…"

mi "¡Sino lo que tú puedes hacer por tu escuela!"

show misha cross_laugh
with charachange

mi "¡Jajaja!"

mi "¡Jajajajajajaja!"

"Qué deprimente."

show misha cross_grin
with charachange

mi "¡Anímate, anímate, Hicchan!"

"Me golpea con dureza en la espalda con la fuerza suficiente para sacarme el aire de mis pulmones. Lucho para poder respirar."

mi "Además, ¿no estás feliz de que vas a pasar el día con dos chicas bonitas?"

show misha hips_laugh
with charachange

mi "¡Jajajaja!"

"Creo que tienen razón. Sí se me escaparon esas palabras, después de todo."

stop music fadeout 3.0

"Aceptando mi destino, las sigo al salón del consejo estudiantil…"

scene bg school_council_ss
with shorttimeskip

play sound sfx_hammer
play music music_tranquil fadein 3.0

"… Y martilleo el último clavo al puesto. Tomó toda la tarde, y la hora de la cena está por terminar. Pero ya está hecho."

show shizu basic_normal_ss at center
with charaenter

"Shizune saca un rollo de cinta métrica y un pequeño nivel, y lo inspecciona con cuidado."

show shizu behind_smile_ss
with charachange

"Sonríe, viéndose satisfecha, y hace gestos a Misha para que se acerque."

show shizu adjust_happy_ss
with charachange

shi "…"

show shizu adjust_happy_ss at tworight
show bg school_council_ss at bgright
with charamove

show misha perky_smile_ss at twoleft behind shizu
with charaenter

mi "Dice que hiciste un muy buen trabajo. De hecho, tal vez tengas un don para esto."

show misha hips_smile_ss
with charachange

mi "Guau, yo también estoy impresionada. Y eso fue rápido, ¿has hecho esto antes?"

hi "No. Jamás."

hi "Jamás en mi vida."

hi "Y jamás lo volveré a hacer."

show shizu behind_smile_ss
with charachange

shi "…"

mi "Bueno, la cuota para el día eran seis puestos. En unos minutos yo y Shicchan deberíamos terminar este."

show misha hips_grin_ss
with charachange

mi "Eso significa~… ¡Nos faltan cuatro para terminar!"

show misha sign_smile_ss
with charachange

mi "¡Ella dice que llevamos buena velocidad~!"

show misha hips_grin_ss
with charachange

mi "¿No es esto muy divertido?"

hi "¿Qué?"

"Podría pensar en un millón de cosas que preferiría hacer, pero supongo que todos tienen que hacer su parte para el festival, incluso yo."

hi "Ambas tienen suerte de que las estoy ayudando, si realmente no hubiese querido, me podría haber zafado fácilmente."

show shizu basic_normal2_ss
with charachange

shi "…"

show misha perky_smile_ss
with charachange

mi "¿De veras, Hicchan?"

show shizu adjust_smug_ss
with charachange

shi "…"

show misha cross_laugh_ss
with charachange

mi "¡Guajaja~! ¡Shicchan piensa que estás hablando por hablar! ¡Los japoneses no tienen reflejo de lucha o fuga, Hicchan~!"

"Shizune junta sus dedos maliciosamente."

show shizu basic_happy_ss
with charachange

shi "…"

show misha hips_grin_ss
with charachange

mi "¡Definitivamente~! ¡Definitivamente, definitivamente~! Si realmente hubieses querido escapar, ¡hubieras tomado acción inmediata~! Así es como sabes que alguien habla en serio, ¡cuando no tienen dudas ni arrepentimientos!"

show shizu basic_normal_ss
with charachange

shi "…"

show misha sign_smile_ss
with charachange

mi "Quizás haya sido una mala idea haberte dicho eso, ya que ahora Hicchan sabe qué hacer la próxima vez~."

"Sin embargo, solo el hecho de que no tiene problema en decírmelo muestra que duda que seré capaz de hacer algo al respecto."

"Eso solo me da más ganas de hacerlo, y casi quiero que la oportunidad de hacerlo vuelva a surgir. Pero si eso ocurre, ella podría atraparme otra vez, de algún modo."

show shizu behind_smile_ss
with charachange

shi "…"

show misha perky_smile_ss
with charachange

mi "Shicchan dice que está contenta ahora."

stop music fadeout 1.5

scene bg school_council_ni
with shorttimeskip

play music music_dreamy fadein 0.5

"Mucho, mucho después en la noche, estamos ante seis puestos completos."

"Con el orgullo de un trabajo bien hecho, nos sentamos y admiramos el fruto de nuestra labor, sin compartir una palabra entre nosotros. Solo admirando."

"Me doy cuenta de que me siento bastante sediento."

hi "Oigan, ¿no hay una máquina expendedora en el pasillo? Están prendidas todo el día, ¿verdad?"

show misha hips_smile at center
with charaenter

mi "Seguro, las bebidas son bastante baratas, también. Usualmente tomamos algo de ahí en días como este."

"Busco en mi bolsillo, y encuentro una sola moneda de cien yenes."

hi "¿Es esto suficiente? Me estoy sintiendo algo sediento."

show misha hips_grin
with charachange

mi "¿Cien yenes? Puedes conseguir cualquier bebida en la máquina con eso."

hi "Eso es bueno, eso está muy bien, entonces."

show misha hips_grin at twoleft
show bg school_council_ni at bgleft
with charamove

show shizu adjust_happy at tworight
with charaenter

shi "…"

show misha sign_smile
with charachange

mi "Ah, espera un segundo."

show misha hips_grin
with charachange

mi "¿Hm? ¿Qué ocurre, Shicchan? ¿Quieres que él te traiga algo para beber también? ¡Jajaja!"

show shizu behind_smile
with charachange

shi "…"

show misha perky_smile
with charachange

mi "Hicchan, hoy nos has ayudado en verdad, así que hoy yo… quiero decir Shicchan, te invitará."

show misha perky_confused
with charachange

mi "Oye, ¿qué hay de mí?"

show shizu adjust_smug
with charachange

shi "…"

show misha perky_smile
with charachange

mi "¿Qué te gustaría? ¿Estoy sedienta?"

show misha perky_confused
with charachange

mi "¡Yo también!"

hi "Hm, no lo sé. Cualquier cosa está bien. La soda de melón, creo."

show shizu behind_smile
with charachange

shi "…"

show misha perky_sad
with charachange

mi "¡Oye, Shicchan, espera! ¡Yo también quiero algo para beber!"

hide shizu
with charaexit

show misha perky_sad at center
show bg school_council_ni at center
with charamove

mi "¡Ooh…!"

show misha perky_confused
with charachange

mi "Sabes, son ocasiones como esta cuando pienso que solo se está burlando de mí."

hi "Probablemente sea eso. Estoy seguro de que te traerá algo, ¿verdad?"

mi "Sí, usualmente lo hace. Pero… una nunca sabe…"

hi "Je."

show misha perky_confused at twoleft
show bg school_council_ni at bgleft
with charamove

show shizu basic_normal2 at tworight behind misha
with charaenter

"Shizune regresa con dos sodas de melón y una lata de jugo de frutas."

"Me entrega una de las sodas, y la otra se la da a Misha."

show misha hips_grin
with charachange

mi "¡Gracias, Shicchan~! Tenía mi completa fe en que me traerías una, ¡sabía que podía contar contigo! ¡Guajajaja!"

show misha perky_confused
with charachange

mi "¿Pero cómo sabías que quería esto? Usualmente compro otra cosa."

show shizu behind_smile
with charachange

shi "…"

show misha hips_grin
with charachange

mi "¿Qué? ¿Sabías que me gustaría probarlo? ¿Y que me gustan esta clase de cosas infantiles? ¡Jajajaja!"

show misha hips_laugh
with charachange

mi "¡Jajajaja!"

"Le hago un gesto dándole las gracias a Shizune, quien sonríe y asiente."

show shizu adjust_happy
with charachange

shi "…"

stop music fadeout 4.0

show misha sign_smile
with charachange

mi "Oye, Hicchan…"

hi "¿Sí?"

show shizu behind_smile
with charachange

shi "…"

show misha perky_smile
with charachange

mi "Hemos estado pasando mucho tiempo juntos. Y ya, en tan poco tiempo, hemos hecho tanto."

mi "Deberíamos dejarnos de rodeos. Lo que quiero decir es,"

"Esto suena mucho como si me estuviese invitando a salir, pero no puede ser. Sin embargo, mi corazón está latiendo como un martillo neumático. Maldición, esto me recuerda a un episodio similar a principios de este año."

"Intento decir algo, pero mi cerebro no puede decidir si detenerla o decirle que continúe."

"Siento que me enrojezco hasta las orejas."

show shizu adjust_smug
with charachange

shi "…"

show misha hips_smile
with charachange

mi "Lo que estoy intentando decir es…"

show misha hips_grin
with charachange

play music music_ease

mi "¿Te gustaría unirte al consejo estudiantil?"

hi "Ah, qué decepción."

show misha cross_laugh
show shizu adjust_blush
with charachange

mi "¡Jajaja! ¡Jajajaja! ¡Jajajajaja! ¡Guajaja! ¡Jajajaja!"

mi "¿Pensabas que quería invitarte a salir, Hicchan?"

mi "¡Jajajaja! ¡Jajaja! ¡Jajaja! ¡Jajajaja!"

mi "¡Jajajajajajajaja!"

"Me siento muy avergonzado en este momento, puedo sentir cómo mi cara se pone cada vez más roja."

"Shizune también intenta esconder su rostro ruborizado luego de que Misha haya traducido, y luego pone unas hojas de papel enfrente de mí."

show shizu behind_frustrated
with charachange

shi "…"

show misha cross_grin
with charachange

mi "Entonces, ¿qué te parece? Todo el papeleo está aquí."

show misha cross_smile
with charachange

mi "Y ya estás sentado, de todos modos. Parece como si estuvieses en casa aquí. ¡Bebidas y todo~!"



show shizu basic_normal
with charachange

shi "…"

show misha hips_grin
with charachange

mi "¿Qué dices?"

"Misha guarda silencio un poco y pregunta nuevamente, esta vez algo más solemnemente."

show misha cross_smile
with charachange

mi "Hicchan, ¿qué dices?"

show misha sign_smile
with charachange

mi "No precisamente odias esto, ¿cierto?"



"Estoy más que un poco sorprendido ante el repentino cambio de tono. No sé realmente cómo reaccionar."

"En primera instancia, no está gritando a todo pulmón sin consideración o tacto alguno."

"Antes, estoy seguro de que ella ya sabía que iba a decirle que no."

"Esta vez, parece estar hablando de verdad en serio."

show misha perky_smile
with charachange

mi "Creo que tal vez deberías unirte. No solo porque nos sería útil tu ayuda, pero, bueno, estás juntándote con nosotras de todas formas."

mi "Creo que a Shicchan le gustaría si te unieras. No es como si nos odiases o algo, ¿cierto?"

show misha perky_sad
with charachange

mi "No nos haría daño que te unieses. Y lo apreciaría si lo hicieses."

"Parece estar teniendo dificultades para poder darse a entender, lo cual es extraño para alguien tan conversadora como Misha."

"Por algún motivo, esto casi me inquieta."

show shizu behind_blank
with charachange

"Mis ojos se mueven hacia Shizune, quien me mira tentativamente, limpiando sus uñas distraídamente."

show misha perky_smile
with charachange

mi "Si no quieres unirte, prometemos que no preguntaremos otra vez, pero si lo haces, estaríamos realmente felices."

"Tanto Shizune como Misha parecen incapaces de mirarme a los ojos."

"No puedo mentir, la idea de poder estar alrededor de dos chicas tan lindas es algo que no podría dejar pasar."

"No estoy esperando colaborar con esta clase de trabajo todos los días, aunque debería haber menos carga tras el festival."

"Al menos eso espero."

hi "Está bien. Supongo que no puede hacer daño, así que, ¿por qué no?"

show shizu adjust_happy
with charachange

shi "…"

show misha hips_grin
with charachange

mi "Espléndido. ¡Espléndido! ¡Ajajaja~!"

"Shizune junta sus dedos con satisfacción."

show shizu basic_happy
with charachange

shi "…"

show misha perky_smile
with charachange

mi "Ella llenará todos los datos, Hicchan. ¡Felicidades, ahora eres un miembro oficial del consejo estudiantil!"

hi "Genial. No estoy esperando trabajar demasiado."

hi "Para ser honesto, jamás hice este tipo de actividades antes."

hi "¿Pero tal vez será una experiencia positiva?"

"Misha comienza a aplaudir, riéndose a la vez con exuberancia."

show misha hips_laugh
with charachange

mi "¡Felicidades, Hicchan!"

show shizu adjust_smug
with charachange

shi "…"

mi "¡Felicidades!"

show shizu behind_smile
with charachange

shi "…"

mi "¡Felicidades!"

show shizu adjust_happy
with charachange

shi "…"

mi "¡Felicidades!"



hi "Entiendo el mensaje."
"No puedo evitar sonreír, encuentro esta infantil actitud bastante adorable."

show misha hips_grin
with charachange

mi "¡Tú sabes, el consejo estudiantil está siempre ocupado! Pero por hoy, hemos terminado. ¡Nos vemos mañana, Hicchan!"

show misha hips_smile
with charachange

mi "¡Aún nos queda trabajo, así que estaremos contando contigo!"

stop music fadeout 4.0

scene bg school_hallway3
with locationchange

"Dejo el lugar, completamente agotado. El campus está totalmente desierto, y la escuela se ve ominosa a estas horas. La oficina del consejo es la única con luces a estas horas."

"¿Es así como será el consejo estudiantil? Mi cuerpo tal vez no lo soporte."





label es_A23:

scene bg school_scienceroom at bgleft
with shorttimeskip

play music music_tranquil fadein 3.0

"Hanako no aparece en absoluto durante las clases de la mañana, dejando su asiento luciendo vacío y solitario en la parte de atrás del salón."

"Tengo que decirle que Lilly la estaba buscando si la llego a ver luego."

"Tras los eventos de esta mañana, la clase es bastante aburrida en comparación. Le doy vuelta a las páginas de mi cuaderno perezosamente."

"Tengo un poco de atraso en los estudios por eliminar, a pesar de haber intentado mantenerme a la par con estos en el hospital, pero no estoy muy entusiasmado al respecto."

"El reloj al frente del salón suena insoportablemente fuerte. El profesor no ha dicho nada en más de siete minutos, optando en vez de ello por cubrir el pizarrón con filas y filas de ecuaciones sacadas directamente del libro."

"El golpeteo rítmico de la tiza contra el pizarrón parece sincronizar perfectamente con el sonido del reloj."

"Comienzo a copiar las ecuaciones solo para pasar el tiempo, incluso aunque están justo ahí en el libro de texto."

scene bg school_scienceroom at bgright
with shorttimeskip

play sound sfx_normalbell

"Cuando la campana suena, no me apresuro porque no tengo nada que hacer, así que me quedo por un rato, repasando lo que vimos en clase hoy. Prefiero irme al final de todos modos, para no tener que lidiar con la multitud en los pasillos."

"Noto que Shizune y Misha también se han quedado atrás, hablando con alguien de otra clase."

"Shizune está haciendo señas tan rápido que sus manos hacen ruidos que me recuerdan a espadas atravesando el aire."

"Quizá haya ira contenida ahí dentro."

"Misha está intentando desesperadamente mantener el ritmo, pero es claro que apenas puede siquiera entenderla."

"Agacho la cabeza. Lo que sea que estén discutiendo, parece algo serio."

"Shizune hace señas al punto tal que sus muñecas hacen ruido, y Misha lucha para escupir su equivalente vocal."

"A veces se tropieza con las oraciones como si estuviese lidiando con trabalenguas. Y además de eso, tiene que traducir a señas todo lo que la otra chica le está diciendo."

"Parece un trabajo duro."

"Misha se ve cansada, casi como si estuviera por desvanecerse."

"Afortunadamente para ella, su asunto termina pronto y las chicas vuelven a sus asientos una vez más."

show shizu behind_blank at tworight
show misha perky_sad at twoleft
with charaenter

mi "¡Uwaaah! ¡Estoy tan cansada!"

"Ella está apoyando su cabeza sobre su banco, luciendo exhausta."

"Usaré la oportunidad para reconciliarme un poco con Shizune, intentando no ser arrastrado a eso del consejo estudiantil otra vez, aunque sospecho que esa puerta ya se ha cerrado para mí."

hi "Las preparaciones para el festival deben ser algo bastante pesado para ustedes."

"Efectivamente, la gente en esta escuela parece tomarse el festival muy en serio. Cada vez que veo gente vagando antes y después de clases están siempre hablando acerca de sus planes para este."

"Es bastante bueno ver que todos están tan entusiastas al respecto."

"Probablemente yo sea el único que no tiene algo que hacer."

show shizu basic_angry
with charachange


"Shizune se burla de mí en un principio, como tratando de decidir entre ignorarme o mirarme con desprecio, pero al final empieza a hacer señas sin decidirse por ninguna."

show misha perky_confused
with charachange

"Misha se anima, mirando sus manos con sus ojos levemente fuera de foco."

show shizu behind_frown
with charachange

shi "…"

"Ella hace señas con movimientos fuertes, pesados y dramáticos."

"Misha traduce sus señas en diálogo para mí."

"Lo hace tan bien que casi parece como que Shizune habla directamente, transmitiendo sus pensamientos directamente a través de Misha."

"Debió haberlo practicado vigorosamente."

show misha cross_frown
with charachange

mi "Pues por supuesto, estamos en el consejo estudiantil, sabes, así que estamos bastante ocupadas."

show shizu basic_frown
with charachange

shi "…"

show misha sign_smile
with charachange

mi "Es una tarea importante por nuestra parte, para asegurar el éxito del festival con toda nuestra capacidad."

show shizu behind_frown
with charachange

shi "…"

show misha hips_frown
with charachange

mi "Nos avergonzaríamos ante las generaciones pasadas de consejos estudiantiles si el festival fallase."

show shizu adjust_angry
with charachange

shi "…"

show misha sign_smile
with charachange

mi "Por eso no debe haber fallas… emmm creo que eso era “obstáculos”, nada en absoluto que pudiera hacer que el festival no sea exactamente perfecto."


"El apasionado discurso de Shizune y la actuación de Misha son en verdad extrañamente concordantes con ellas."

stop music fadeout 2.0

show shizu adjust_blush
show misha perky_confused
with charachange

mi "¿Oh? ¡Hola~!"

show shizu adjust_blush at offscreenleft
show misha perky_confused at Transform(xanchor=0.5, xpos=-0.45)
show bg school_scienceroom at bgleft
with charamove

show hanako emb_timid at Transform(xanchor=0.5, xpos=0.93)
with charamoveinright

play music music_pearly fadein 1.0

"Miro por sobre mi hombro y veo a Hanako mirando tímidamente dentro del salón, con la mayor parte de su cuerpo escondido detrás de la puerta."

show misha perky_smile at Transform(xanchor=0.5, xpos=0.15)
with charamove

mi "¡Oye! ¿Jugando a la delincuente otra vez?"

show hanako emb_blushtimid
with charachange

"Hanako se ruboriza con fuerza ante la directa ofensiva de Misha, aunque solo haya sido en broma."

show shizu basic_angry at Transform(xanchor=0.5, xpos=0.35)
with charamove

shi "…"

show hanako emb_downsad
with charachange

show hanako emb_downsad at Transform (xanchor=0.5, xpos=0.97)
with charamove

"Shizune la examina con su mirada, haciendo a Hanako mirar hacia abajo y comenzar a echarse hacia atrás al punto tal donde solo sus dedos se pueden ver asiendo nerviosamente el borde de la puerta."

"Tal vez esté mostrando su disgusto por Hanako por asociación de su disgusto por Lilly."

"Así lo parece, y Hanako probablemente lo sabe también."

hi "¿Qué ocurre, Hanako?"

show hanako emb_timid
with charachange

ha "¿Ha pa… pasado Lilly por aquí?"

mi "Lo lamento, no he visto a Satou. Aunque ella, eh, vino por la mañana."

show hanako emb_downtimid
with charachange

"Hanako sigue mirando con inquietud a Shizune, quien a su vez le lanza su mirada analítica usual. ¿Qué está intentando hacer?"

"Por supuesto que Shizune no va a apartar su mirada, y ella es suficientemente intimidante de por sí; así que solo puedo imaginarme lo aterrada que debe estar Hanako."

"Sin embargo es un poco gracioso, ver la reacción de Hanako ante la actitud normal de Shizune. Parece que esto es lo que ocurre cuando se juntan dos polos completamente opuestos."

show hanako emb_timid
with charachange

ha "¿Saben… saben d-dónde está?"

show shizu behind_frown
with charachange

shi "…"

show misha hips_frown
with charachange

mi "Si le queda algo de cerebro, está en su salón de clases, trabajando en su proyecto del festival. Pero quién sabe dónde está holgazaneando esa mujer."



label es_A23a:

scene bg school_scienceroom at bgleft
show hanako emb_timid at Transform (xanchor=0.5, xpos=0.97)
show shizu behind_frown at Transform(xanchor=0.5, xpos=0.35)
show misha hips_frown at Transform(xanchor=0.5, xpos=0.15)
with None

hide hanako
with charamoveoutright

"Hanako asiente rápidamente y se retira apurada."

stop music fadeout 2.0

show misha hips_grin
with charachange

mi "¿De qué estábamos hablando? Oh cierto, estamos trabajando realmente duro para hacer del festival una realidad."

"Y volver locas a otras personas en el camino."

hi "Bueno, que tengan suerte con eso."

"Me levanto para irme, saliendo antes de que alguna de las dos logre seguir recriminándome por holgazanear."

scene bg school_hallway3
with locationchange

"Los pasillos están un tanto callados, como es de esperarse. Todos deben estar en reuniones de clubes o en preparaciones para el festival. O ambos."

"Las palabras de Shizune acerca de mí siendo un haragán hacen eco en mi cabeza."

"Me siento un poco culpable sobre no contribuir, pero parece ser que carezco la determinación para hacer algo concreto al respecto."

"Para el festival, ya es demasiado tarde a menos que cuente haber ayudado a Shizune y Misha, cosa que por supuesto no hago. Y clubes… No lo sé."

"Tal vez no soy el tipo de persona que se una a clubes."

play music music_soothing fadein 4.0

scene bg school_dormext_half
with locationskip

"A mitad del camino desde el edificio de la escuela a los dormitorios noto una figura al frente de estos."

"Es Rin."

"Parece ser que hoy también está trabajando en su mural."

"Camino hacia ella, pero no parece percatarse de que me aproximo."

scene bg mural_unfinished
show rin basic_awayabsent_close at tworight
with locationchange

"Está sentada en una caja dada vuelta, mirando fijamente al muro que está pintando con una brocha sostenida entre los dedos del pie."

"El mural ha progresado considerablemente desde ayer, pero aún está a medio terminar hasta donde puedo decir."

"Más colores han aparecido y las retorcidas figuras cuasihumanas se han esparcido y aumentado en número."

"Debo decir, su estilo es bastante llamativo y muy singular. No es como si fuera conocedor del arte en alguna escala mensurable, pero se ve muy bien, a pesar de todo."

"Aclaro la garganta para llamar su atención, pero sin asustarla para no quebrar su concentración."

rin "Espera."

"Ni siquiera se da la vuelta para ver quién es."

"Esperaré."

stop music fadeout 6.0

"…"

"…"

"…"

"…"

with shorttimeskip

"…"

"Quince minutos más tarde decido que su concentración efectivamente no se ha roto, y también que he esperado lo suficiente como para justificar darle un toque en el hombro para recordarle mi presencia."

"Rin gira su cabeza mecánicamente hacia mi dirección, y termina mirándome directamente a nivel de mi entrepierna."

show rin basic_deadpan_close
with charachange

rin "Oh, es Hisao."

play music music_rin fadein 0.3

"¿Puede darse cuenta? Me sentiría mucho menos incómodo si me mirase a la cara."

hi "Una astuta observación. Trabajando duro, puedo ver."

"La conversación comienza como si no hubiese estado ya aquí desde hace un cuarto de hora, pero no es una preocupación. Al menos comienza."

hi "Se ve bien."

"Es verdad, las capas de pintura escondiendo otras capas de pintura, mezclando y dando forma a las figuras humanas realmente crean una vista impresionante. Pero Rin parece molesta."

show rin basic_deadpanupset_close
with charachange

rin "No deberías comentar sobre las obras en progreso. Siete años de mala suerte."

hi "Suena terrible. Supongo que me retracto, entonces."

"Aun así, se ve bien. Me pregunto si me tocan catorce años de mala suerte por pensar eso."

show rin basic_awayabsent_close
with charachange

"Rin se da vuelta para ver su pintura y le da un toque con el pulgar del pie."

show rin relaxed_nonchalant_close
with charachange

rin "¿Podrías mezclar un poco de este color? Se me está terminando."

"Rin mira hacia abajo a un tazón medio vacío con los restos de la misma pintura rosácea dentro."

"No pensaba quedarme y ayudarla con este proyecto… Creo que no pensé mucho en hacer algo."

show rin basic_absent_close
with charachange

"Miro a Rin, ella me mira de vuelta con ojos vacíos."

hi "Solo esta vez."

show rin basic_awayabsent_close
with charachange

"Rin toma otra brocha y la empapa en otra tonalidad de rojo pálido. Hay docenas de tazones similares por toda su área de trabajo. Por el aspecto de esta escena podría deducir que ha estado sentada allí por horas."


"Me pregunto si así lo ha hecho. Aunque eso significaría que ha estado faltando a clases; lo cual, por supuesto, no diría que está más allá de alguien como Rin."

"Vierto un poco de blanco y rojo en el tazón, tratando de igualar el color de la pintura que ya está en la pared."


"Al parecer no puedo hacerlo bien."

"Es realmente inconveniente de su parte no mezclar suficiente pintura en primer lugar. Lograr que sea exactamente la misma tonalidad será imposible, pero al menos puedo intentar llegar lo más cerca posible."

hi "Hablando de trabajo duro, ¿no es eso demasiada carga para ti? Es una pintura muy grande y todo."

show rin basic_deadpan_close
with charachange

rin "Oh, no soy lo suficientemente vieja y amargada todavía para pensar así."

hi "Supongo que no lo eres."

show rin basic_deadpannormal_close
with charachange

rin "Supones bien."

show rin basic_deadpancontemplation_close
with charachange

rin "Aunque las piernas duelen. Se sienten como babosas. Babosas hechas de babosas marinas."

hi "¿Por la posición?"

rin "Sí, me gusta hacerlo en una posición horizontal, si sabes de lo que estoy hablando."

rin "Pero no hay más remedio. No puedo pedirle al muro que se acueste."

show rin negative_spaciness_close
with charachange

"Diciendo eso, se estira un poco, flexionando las piernas y su espalda mucho más de lo que un ser humano debería hacerlo. Es impresionante con cuán poco esfuerzo maneja su cuerpo."

show rin negative_annoyed_close
with charachange

show rin negative_spaciness_close
with charachange

"Hay un leve estremecimiento en su expresión usualmente en blanco —una pizca de dolor, quizás— mientras estira sus pantorrillas."

"Rin debe tener una resistencia y destreza mucho mayor que una persona normal para ser capaz de vivir como lo hace, pero se está agotando trabajando en esto."

hi "¿Para qué presionarte tanto? Tómate un descanso o algo, al menos. Continúa mañana si es tan malo."

show rin basic_deadpannormal_close
with charachange

"Esto le hace dar una pausa."

"Y larga también, sintiéndose como un bostezo mental."

"…"

show rin basic_deadpan_close
with charachange

rin "No lo creo, Hisao."

rin "No me estoy presionando."

hi "Pues seguro parece que lo haces."

show rin basic_deadpannormal_close
with charachange

rin "No. No tiene que ver con presionarse o empujarse ni nada relacionado a ese tipo de cosas."

show rin basic_awayabsent_close
with charachange

rin "Hay un chico."

hi "¿Un chico?"

show rin basic_absent_close
with charachange

rin "Sí."

hi "¿Dónde?"

show rin basic_deadpannormal_close
with charachange

rin "En el club de arte."

hi "Ehh… ¿y?"

show rin basic_deadpan_close
with charachange

rin "Es ciego."

hi "Oh. ¿Cómo puedes pintar si eres ciego?"

show rin basic_awayabsent_close
with charachange

rin "Ni idea."

hi "¿Y por qué está allí?"

show rin basic_absent_close
with charachange

rin "Ese es el punto. Está allí."

"Debería realmente hablar más de una palabra a la vez para hacer que esto se sienta más como una conversación y menos como un interrogatorio."

show rin basic_awayabsent_close
with charachange

rin "En verdad no puede hacer nada que llamarías arte, ¿cierto? Pero aun así él va. Y pinta."

show rin basic_deadpannormal_close
with charachange

rin "¿Por qué?"

hi "No lo sé. ¿Por qué?"

show rin basic_deadpan_close
with charachange

rin "No lo sé. Por eso pregunté."

hi "¿Entonces?"

show rin basic_deadpannormal_close
with charachange

rin "Él no pinta seguido pero creo que sus pinturas son muy interesantes."

hi "Seguro que lo son."

show rin basic_lucid_close
with charachange

rin "Una vez intenté eso. Pintar a ojos cerrados."

show rin basic_deadpannormal_close
with charachange

rin "No fue muy interesante. Y limpiar el piso tomó años. No lo volví a intentar."

show rin basic_deadpandelight_close
with charachange

rin "Pero está mejorando en la escultura."

hi "Ya veo."

"Quizás quería plantear una idea con esto. Tal vez se olvidó que tenía una."

hi "Parece que el club de arte está lleno de gente interesante."

show rin basic_deadpan_close
with charachange

rin "No realmente."

"Una afirmación bastante directa, y sin captar el sarcasmo en lo más mínimo."

hi "¿No?"

show rin basic_awayabsent_close
with charachange

rin "Justo como lo dije. No son muy interesantes. Usualmente no tengo mucho interés en gente que no es interesante."

show rin basic_absent_close
with charachange

rin "Tal vez tú lo tengas."

hi "Tal vez."

"…"

show rin basic_awayabsent_close
with charachange

rin "Pero ese chico es interesante."

show rin basic_lucid_close
with charachange

rin "Tal vez yo sea como ese chico, o tal vez tú lo eres. Tal vez todos lo sean."

rin "Haciendo cosas que no puedes hacer, solo porque puedes."

"Eso fue bastante profundo, creo; y se lo digo."

hi "Eres profunda."

show rin basic_deadpannormal_close
with charachange

rin "Nah. Soy una persona desconsiderada y superficial. La gente me dice eso todo el tiempo."

show rin basic_deadpanamused_close
with charachange

rin "¿Sabías que solo puedo pensar hasta cuatro cosas a la vez?"

hi "No, pero ahora lo sé."

show rin basic_lucid_close
with charachange

rin "En este momento estoy pensando en el inodoro del baño de las chicas del segundo piso, helado con sabor a helado, el dedo medio del pie y un corte de cabello."

show rin basic_awayabsent_close
with charachange

rin "Voy a necesitar un corte de cabello."

show rin negative_spaciness_close
with Dissolve(0.1)

show rin basic_delight_close
with Dissolve(0.1)

show rin negative_spaciness_close
with Dissolve(0.05)

show rin basic_delight_close
with Dissolve(0.05)

show rin negative_spaciness_close
with Dissolve(0.05)

show rin basic_delight_close
with Dissolve(0.05)

show rin negative_spaciness_close
with Dissolve(0.1)

show rin basic_delight_close
with Dissolve(0.2)

"Sacude su cabeza vigorosamente y deja que su corto y desaliñado cabello se sacuda a la par. Puedo ver que hacer eso es algo que le gusta hacer."

show rin basic_awayabsent_close
with charachange

"Nos quedamos callados mientras Rin camina distraída alrededor, pateando suavemente algunas brochas. El pensamiento sobre el club de arte se queda en mi cabeza un tiempo más."

"Siento que estoy cruzando territorio inexplorado con esto del arte. La forma en que estos encuentros con Rin se llevan a cabo, son como si estuviera a punto de empezar un hábito de fumar o algo. Probablemente debería dejar de hablar con ella."

"No es que me caiga mal, a pesar de la confusión que acarrea ser ella misma, y el arte no me cae mal tampoco. Incluso he dibujado por diversión algunas veces. Simplemente carezco de un impulso creativo, o de cualquier habilidad técnica."

"Es por eso que usualmente, si voy a dibujar algo, el síndrome del papel blanco me toma por sorpresa y me congelo por completo."

"Eso, o logro dibujar algo completamente desfigurado y me frustro ante mi inutilidad de trasladar mi imagen mental al papel, y lo abandono antes de siquiera poder ponerle esfuerzo."

"Rin claramente no posee este problema… pero ella me frustra de una manera completamente diferente. Estar con ella es como mirar un espejo que no refleja nada."

"Hace que uno se pregunte la cordura de hacerlo."

show rin basic_absent_close
with charachange

"Rin se sienta en su caja, balanceándose de lado a lado, aparentemente cómoda con el incómodo silencio. Me está mirando otra vez, o tal vez está mirando por sobre mi hombro. No puedo deducir bien dónde es que están enfocados sus ojos."

"Estoy pensando en irme para que ella pueda seguir trabajando sin distracciones y yo pueda hacer lo que sea que vaya a hacer yo solo. No es como si tuviese algo que debería hacer hoy…"

hi "Oh, demonios."

show rin basic_deadpan_close
with charachange

rin "¿Dónde?"

hi "Nada, es solo que me olvidé de decirle a Hanako que Lilly estaba buscándola."

hi "¿La conoces? ¿De mi grupo?"

show rin basic_deadpanamused_close
with charachange

rin "Oh, ella. La Misteriosa Chica del Baño."

show rin basic_amused_close
with charachange

rin "Esa persona es graciosa. La vi entrar al baño cinco veces en un solo receso hace tres semanas. Estoy segura de que es el récord mundial."

show rin basic_deadpandelight_close
with charachange

rin "Fue muy misterioso."

hi "¿Por eso la llamas la Misteriosa Chica del Baño?"

show rin basic_absent_close
with charachange

rin "¿Qué otro motivo puede llegar a haber? Bueno, si lo hay, es un eterno misterio. No la seguí ahí adentro."

"…"

show rin basic_awayabsent_close
with charachange

rin "¿Quizás fue la semana anterior a esa? Pudo haber sido."

"…"

rin "Mirarla me da hambre."

hi "No digas eso."

hi "Al menos, no cerca de ella."

show rin basic_deadpannormal_close
with charachange

"Rin se gira para mirarme, como si no estuviese segura del porqué la reproché."

"Pero no muestra más entendimiento que antes, así que me doy por vencido en este punto."

hi "¿Entonces quieres ir a cenar?"

show rin basic_awayabsent_close
with charachange

rin "No. Aún no."

"Rin ha volteado su mirada hambrienta hacia el muro, luciendo con un poco más de energía, o al menos un poco menos letárgica que antes."

"Es como si la pared fuese un oponente que ella debe derrotar, algo que debe superar antes de que pueda darse el gusto de cenar."

"Esta es la sensación que tengo. Un raro sentimiento de empatía me domina y me hace sonreír un poco por dentro."

"Para toda su rareza, Rin es bastante genial, después de todo."

hi "Me voy, de todos modos."

hi "Que te diviertas."

stop music fadeout 3.0

"Rin ya ha tomado una brocha y la está hundiendo en pintura fresca, así que por supuesto ya no puede oírme, o no responde nada en caso de que me oiga."






label es_A24:

stop music fadeout 6.0

scene bg school_scienceroom at bgleft
show hanako emb_timid at Transform (xanchor=0.5, xpos=0.97)
show shizu behind_frown at Transform(xanchor=0.5, xpos=0.35)
show misha hips_frown at Transform(xanchor=0.5, xpos=0.15)
with None

show bg school_scienceroom at right 
show hanako emb_timid at right
show shizu behind_frown at offscreenleft
show misha hips_frown at offscreenleft
with charamove

hide misha
hide shizu
with None

hi "¿Necesitas encontrarla? Te estuvo buscando en la mañana pero supongo que no se encontraron."

"Ella espera un poco sin responder a la sencilla pregunta, luciendo en exceso como si no estuviera segura de si es apropiado responder a una pregunta así."

show hanako emb_blushtimid
with charachange

ha "S… sí."

hi "Puedo ir contigo."

hi "Si te parece bien."

show hanako emb_downtimid
with charachange

show hanako emb_blushtimid
with charachange

"Hanako asiente apenas, aún en guardia y sus hombros rígidos como madera. Tengo la sensación que podría estar más cómoda por su cuenta después de todo, pero es muy tarde como para echarse atrás."

"Tiene esta expresión de gran preocupación que parece llevar casi constantemente, una que me hace estar constantemente en guardia. Me pregunto por qué."

"Creo entender el porqué parece siempre ser tan cautelosa… o tal vez más algo como, el porqué podría haber una persona como ella."

"Pero todavía sigo sin tener idea de cómo actuar ante una persona así."

hi "Pronto será la hora de la cena. ¿Planeabas comer con Lilly?"

show hanako emb_downtimid
with charachange

show hanako emb_blushtimid
with charachange

"Hanako asiente levemente."

"Así que ella debe de haber estado tratando de entrar a la cafetería."

"Bueno, hay una multitud de gente para la cena, tanta como la que llena la cafetería durante el almuerzo."

"No es tan malo ya que la hora de la cena es más larga que la del almuerzo, pero puedo entender por qué Hanako podría desanimarse de entrar."

"Tomo mi mochila y partimos. Hanako brinca un poco para alcanzar mi velocidad inicial, así que la disminuyo para coincidir con su paso."

scene bg school_hallway3
with locationchange

"No toma mucho tiempo para que los dos estemos caminando a un paso cómodo por el pasillo."

show hanako def_worry at right
with charaenter

"Casi se siente como si fuésemos juntos a dar un paseo; algo que no puedo decir que haya hecho antes con una chica."

"Sin embargo Hanako no parece estar pensando lo mismo. A pesar de que estamos caminando al mismo ritmo, se mantiene siempre a más de un brazo de distancia."

"Creo que todavía le incomoda un poco estar cerca de mí. Dado lo tímida que es, no parece haber mucho que pueda hacer al respecto, al menos por ahora."

scene bg school_cafeteria
with locationchange

play music music_night fadein 3.0

"Para cuando llegamos a la cafetería, no hay mucha gente, pero Lilly no se ve por ningún lado."

show hanako emb_downsad at center
with charaenter

"La cabeza de Hanako se hunde aún más abajo de lo usual."

hi "¿Ya has buscado en algún otro lugar?"

show hanako basic_worry
with charachange

ha "S-solo en la biblioteca… Yo es-estaba leyendo…"

"Así que pasa el tiempo de las clases a las que falta en la biblioteca."

hi "Ah, así que no fue exactamente una búsqueda muy exhaustiva, entonces. Bueno, si tuviese que adivinar, estaría en su salón como dijo Shizune, ¿no es cierto?"

show hanako cover_worry
with charachange

ha "Ci-Cierto."

show hanako basic_normal
with charachange

"Con el asentimiento de cabeza más pequeño, Hanako coincide con mi razonamiento."

"Dios, está siendo tan tímida."

"Es como si necesitase guantes acolchados de seda con doble capa para siquiera comenzar a interactuar con ella."

"Algo de charla podría ayudarle a estar un poco más acostumbrada a mí. No es difícil darse cuenta de que el silencio entre nosotros está rondando por las mentes de ambos."

hi "Así que tú y Lilly suelen estar juntas después de clases, ¿verdad?"

show hanako emb_downtimid
with charachange

ha "S-Sí."

"No estoy del todo seguro de lo que esperaba de su respuesta, o por qué siquiera hice esa pregunta. Eso era bastante obvio, después de todo."

"No parece como si fuera del tipo que cultiva un círculo social tampoco, así que sospecho que Lilly bien podría ser su única amiga."

hi "Debe ser una molestia estar en grupos diferentes, me supongo."

"Hanako asiente con fuerza, casi de reflejo. Comparada con la cuidadosa planeación que Lilly invierte en sus acciones y palabras, Hanako se apresura en hacer sus respuestas lo más rápidas y cortas posible."

show hanako emb_downsmile
with charachange

ha "Pero Lilly… pasa por el salón. Incluso cuando está ocupada…"

"Ella da una pequeña sonrisa mientras lo dice, evidentemente apreciando el hecho que Lilly se preocupa en ayudarla."

"Es bastante tierno, en verdad. No hay necesidad de decir nada más, ambos felices que la discusión ha llegado a su fin."

scene bg school_staircase2
with locationchange

"Al ascender por las escaleras de vuelta al vestíbulo nos encontramos con un grupo de estudiantes bajando las escaleras como un cardumen moviéndose de un área de alimentación a la otra."

show hanako cover_worry_close at Transform(xanchor=0.4, xpos=0.0)
with easeinleft

"Parecen mantenerse en sus propios asuntos, pero antes de que pueda notarlo, Hanako se ha movido detrás de mí."

hi "Oye, ¿estás bien?"

show hanako basic_worry_close
with charachange


ha "S-Solo sigue caminando…"

hide hanako
with easeoutleft


"Los estudiantes nos pasan sin siquiera mirarnos dos veces, y Hanako vuelve a tomar su posición a mi lado al entrar al edificio, el momentáneo indulto por su ansiedad ha sido arrebatado."

scene bg school_lobby
show hanako basic_normal at center
with locationchange

"Incluso al subir hacia el tercer piso, ella no parece relajarse."

"No es como si jamás hubiese conocido a alguien tímido, o incluso chicas tímidas, pero Hanako parece estar bastante alejada de lo que llamaría normal en su miedo hacia otras personas."

"Si no fuese por Lilly actuando como mediadora, dudo que Hanako fuese siquiera capaz de poder caminar al lado mío como ahora. Parece desactivarse por completo en presencia de otros."

"El resto de la caminata hasta el salón de Lilly continúa en un forzado silencio, mientras me lamento de su incapacidad de socializar en absoluto."

scene bg school_hallway3
with locationskip

stop music fadeout 4.0
$ renpy.music.set_volume(0.1, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0

"Luego de subir las escaleras, el ruido proveniente del salón de Lilly es audible desde la mitad del pasillo. No esperaba para nada un bullicio tal."

hi "Bueno, creo que la encontramos…"

"Esto no fue difícil. Me pregunto ¿habrá venido Hanako aquí primero y luego habrá ido hacia mí como apoyo?"

"Bueno, si eso es verdad, entonces significa que al menos está comenzando a confiar un poco en mí. Eso solo puede ser algo bueno."

"Eventualmente, ambos llegamos hasta la puerta del salón 3-2. Con Hanako colocándose atrás de mí no muy sutilmente, abro la puerta."

play sound sfx_dooropen
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")
play music music_another fadein 1.0

scene bg school_room32 at bgright
with locationchange

"El interior es una colmena de actividad, aparentemente con cada estudiante en el salón hablando a la vez mientras trabajan apresuradamente en sus tareas separadas."

"A juzgar por las latas de pintura, decoraciones y letreros, debe ser por el festival escolar próximo."

"Creo que mi primer prioridad debería ser encontrar a Lilly…"

"…{w} Allí."

"Encontrarla entre el bullicio es sorprendentemente sencillo, gracias a su apariencia."

"Con un par de estudiantes a su alrededor mientras está de pie al frente de la clase, ella parece estar a cargo de los preparativos, o al menos ocupada organizándolos."

"Cuidadosamente negociando un camino a través de los varios estudiantes encorvados sobre el suelo a falta de espacio en sus bancos, levanto una mano por puro hábito cuando finalmente llegamos con Lilly."

hi "Hola, Lilly."

show lilly basic_surprised at center
with charaenter

"Lilly levanta la cabeza mientras interrumpe la conversación con una chica notablemente más baja que debe ser su compañera de clases, intentando escuchar lo mejor posible."

li "Perdón, quién…"

hi "Ah, lo siento. Hisao. También vengo con Hanako."

show lilly basic_smile
with charachange

show lilly basic_smile at twoleft
show bg school_room32 at center
with charamove

show hanako basic_normal at tworight
with charaenter


ha "Ho-hola."


"Ella es bastante asustadiza. Considerando el número de gente alrededor, no es muy difícil de intuir por qué."

"Lilly se toma una pausa momentánea para analizar la situación antes de girarse al otro estudiante una vez más."

show lilly basic_smileclosed
with charachange

li "Por el momento, solo pídele consejos a Moriya. Kenji ya está ocupado pintando una de las pancartas."

"Con un rápido movimiento de cabeza la chica se va, sus dedos deslizándose cuidadosamente a lo largo de la pared para orientarse."

$ renpy.music.set_volume(0.1,1.0)

"Espera… ¿Kenji? ¿Ese Kenji?"

"Rápidamente me giro, inclinándome a un costado para ver tras Hanako."

"Efectivamente, en una esquina del salón, Kenji está encorvado sobre una tela mientras la pinta. Sus ojos se mantienen solo a centímetros de la brocha, recordándome lo cerca que tenía que estar para poder ver mi rostro cuando lo conocí."

$ renpy.music.set_volume(1.0,1.0)

show lilly basic_smile
with charachange

li "Disculpa. Nuestro grupo no tiene muchos estudiantes con siquiera vista parcial, así que son muy demandados."

"Es cierto, el grupo 3-2 era especialmente para estudiantes con mala vista. Prepararse para el festival debe ser bastante arduo para ellos."

hi "¿Necesitas una mano? Te podría ayudar si lo necesitas. Tal vez Hanako también podría."

"Una oportunidad de ocupar su mente en algo le haría bien, pero dudo que tenga la valentía de preguntar directamente. Ella asiente en afirmación rápidamente, así que tengo confianza en que hice lo correcto."

"Lilly da un notable suspiro de alivio."

show lilly basic_weaksmile
with charachange

li "Ah, eso está bien. De hecho, ahora esto podría estar terminado antes de que todos se vayan a cenar."

show lilly basic_listen
with charachange

li "¿Podrían ayudar a la persona que está pintando el letrero principal? Es una gran tarea para él, pero nadie más puede ayudar."

hi "¿Kenji? Seguro."

show lilly basic_surprised
with charachange

"Parece sorprendida de que lo conozco. No puedo culparla, realmente."

li "¿Asumo que se han conocido?"

hi "Nuestras habitaciones en el dormitorio están una al lado de la otra. Difícil no vernos, en verdad."

show lilly basic_ara
with charachange

li "Bueno, es bueno ver que estás haciendo amigos tan rápido."

"Amigo… Me pregunto si es la palabra adecuada para usar con él."

"El silencio de Hanako durante la conversación me recuerda el motivo por el cual la puse a ayudar en primer lugar."

hi "Vamos a ayudarlo, entonces. Él sabe lo que hay que hacer, ¿verdad?"

show lilly basic_smileclosed
with charachange

li "Así es. Solo pregunta si tienes algún problema."

hide lilly
hide hanako
with charaexit

$ renpy.music.set_volume(0.5, 2.0, channel="ambient")

"Coreando en asentimiento, Hanako y yo comenzamos otra caminata a través del salón de clase."

"Kenji está sentado en cuclillas, su mirada fija en el lienzo blanco enfrente de él."

show kenji tsun at Transform(yanchor=0.45, ypos=1.0, xalign=0.5)
with charaenter

hi "Hola, Kenji."

"… No hay respuesta. Kenji continúa arrastrando su brocha empapada en pintura sobre el gran kanji a medio pintar que está dibujado en el lienzo con lápiz."

hi "¿Kenji?"

show kenji tsun at center
with charamove

ke "¿Eh? ¿Qué? ¿Quién es?"

"Si esta es la forma en la que trata a sus compañeros de clase, no es de extrañar que esté trabajando en esto solo."

hi "Soy yo, Hisao. Del—{w=.5}{nw}"

ke "Sí, sí, ya sé, hombre. Pero, ¿qué estás haciendo aquí?"

"Su actitud desdeñosa me molesta."

"Debe de ser del tipo que se enfoca realmente en su trabajo y odia ser molestado por cualquiera hasta que termine, supongo."

show kenji tsun at twoleft
show bg school_room32 at bgleft
with charamove

show hanako cover_distant at tworight
with charaenter

"Mientras hablamos, el sonido de los pasos de Hanako al caminar desde detrás de mí me recuerda que ella está aquí."

hi "Estaba por ayudarte con el letrero. Hanako y yo, quiero decir."

show hanako cover_worry
with charachange

ha "Ho… Hola…"

show kenji happy
with charachange

ke "Oh. Eh, hola. Supongo que está bien."

"Ni bien Hanako entra en la ecuación, su actitud cambia completamente. Su repentina hospitalidad fingida es un poco inquietante."

"Ah, cierto. Mujeres. Pensándolo bien, esta puede no haber sido una gran idea después de todo."

stop music fadeout 2.0

scene bg school_room32 at bgleft
show kenji neutral_close at left
show hanako basic_distant_close at right
with locationskip


"Hanako y yo, sin más opción, nos instalamos al lado opuesto de Kenji en el letrero, notando las varias pequeñas latas de pintura en el suelo a su alrededor."

"Puesto de fideos… ¿del grupo 3-2?"

hi "¿Ustedes venderán fideos en el festival este domingo?"

show kenji happy_close
with charachange

ke "Sí, unos puestos afuera. O algo así."

"¿“O algo así”? Su naturaleza evasiva desencadena una buena cantidad de sospecha de mi parte. Sin embargo, concentrarme en la tarea viene primero."

hi "Entonces, ¿cómo quieres dividir esto? ¿Nosotros hacemos los bordes mientras tú haces el texto? ¿O quieres cambiar y hacer los bordes?"

show kenji tsun_close
with charachange

ke "El texto es mío. Ustedes hagan los bordes."

"Tiene sentimientos sorprendentemente fuertes al respecto."

show hanako basic_distant_close
with charachange

"Al extenderme para tomar un pincel, noto que Hanako ya está debatiendo en qué colores usar."

show hanako basic_normal_close
with charachange
show hanako basic_distant_close
with charachange
show hanako basic_normal_close
with charachange

"Para cuando he puesto el pincel sobre la tela, ella ya ha comenzado en un delicado diseño. Parece que mi idea de hacer que dejara de pensar sobre todo mundo a su alrededor funcionó."

"Con un trazo azul oscuro, los tres nos ponemos silenciosamente a trabajar."

"No antes de que Kenji, sin embargo, se aproveche de que Hanako está trabajando para inclinarse hacia mí y susurrarme conspiratoriamente."

show bg school_room32 at center
show kenji tsun_close at center
show hanako basic_normal_close at offscreenright
with charamove

show kenji neutral_close
with charachange

play music music_kenji fadein 0.5

ke "Bueno, hombre, ¿por qué estás aquí?"

hi "Hanako solo quería algo de ayuda para encontrar a Lilly, eso es todo."

show kenji tsun_close
with charachange

"Aparentemente Kenji reprueba mis intenciones."

ke "Ya entiendo. Parece que te he juzgado mal."

show kenji happy_close
with charachange

ke "Te estás infiltrando, ¿no es cierto? ¿Entrar hasta el fondo encubierto?"

"Debí haberlo adivinado. Dejar que la verdad se le escape podría ser probablemente mejor que mentirle o molestarlo de todos modos."

hi "¿Por eso estás aquí?"

ke "Obviamente. Apesta, pero no hay mejor forma de conseguir información que entrar por tu cuenta."

show kenji tsun_close
with charachange

ke "Tenemos que estar unidos, hombre. Esta es una escuela dura, un mundo duro."

hi "Sí, muy duro."

"Se le escapa el verdadero sentido de lo que dije mientras se reclina hacia atrás, satisfecho con que simpatizo con su causa. Mejor me pongo a trabajar."

stop music fadeout 2.0
stop ambient fadeout 2.0

scene bg school_room32
show kenji neutral_close at left
show hanako basic_normal_close at right
with shorttimeskip

ha "Terminé."

hi "Parece que yo también. Buen trabajo."

"Los dos conectamos las líneas de nuestros diseños, el mío siendo la copia más cercana que pude hacer del suyo."

scene bg school_room32
with locationskip

"Con un gruñido, me levanto del suelo y miro a mi alrededor."

play music music_dreamy fadein 4.0

"Además de Hanako y yo, solo queda Kenji terminando un cartel, además de Lilly y un par de estudiantes hablando entre ellos en el salón."

"Mirando mi reloj, no es sorpresa. Se está haciendo bastante tarde."

hi "¿Necesitas una mano?"

show hanako basic_normal at center
with charamoveinbottom

"Le ofrezco una mano a Hanako, que usa para levantarse."

"Al hacer esto, no puedo evitar mirar a su muñeca; si las cicatrices se extienden incluso hasta ahí, ¿cuánto de su cuerpo fue quemado?"

show hanako emb_downtimid
with charachange

"Sin embargo siento un poco de remordimiento al respecto cuando ella rápidamente se cubre la muñeca con su otra mano."

hi "Se ve bien, ¿no es así?"

show hanako emb_timid
with charachange

"Hanako se ve sorprendida por un momento antes de darse cuenta de que estoy hablando del letrero."

show hanako basic_bashful
with charachange

ha "Así es… creo."

"Su sonrisa muestra que siente un ligero sentimiento de orgullo en el resultado, tal como yo lo siento."

hide hanako
with charaexit

"Con el suelo notablemente más despejado ya que las decoraciones están ahora sobre bancos y estantes, es mucho más sencillo llegar a Lilly al cruzar el salón."

hi "Ya hemos terminado el letrero. ¿Supongo que esto es todo lo que necesita hacerse?"

show hanako basic_smile at tworight
show lilly basic_smileclosed at twoleft
with charaenter

"Lilly asiente a modo de agradecimiento."

show lilly basic_smile
with charachange

li "Gracias Hisao, Hanako. ¿Hay alguna forma en la que se los pueda agradecer…?"

hi "Está bien. Mejor que quedarme estudiando en mi habitación, en cualquier caso."

show hanako basic_normal
with charachange

ha "A mí tampoco me molesta."

"Lilly asiente, antes de recordar repentinamente una última persona."

show lilly basic_surprised
with charachange

li "Oh, ¿Kenji sigue aquí?"

"Justo cuando abro la boca, Kenji da la respuesta desde el otro lado del salón."

ke "Sí, acabo de terminar."

"Cuidadosamente Kenji desliza su cartel en una sección vacía del estante para que se seque, antes de pasarnos rápidamente e ir hacia la salida."

show hanako basic_normal at center
show lilly basic_surprised at left
show bg school_room32 at bgleft
with charamove

show kenji neutral at Transform(xalign=1.15)
with charaenter

ke "Nos vemos, hombre."

hi "Hasta luego."

hide kenji
with charaexit

show hanako basic_normal at tworight
show lilly basic_surprised at twoleft
show bg school_room32 at center
with charamove

"Los dos estudiantes restantes se despiden de Lilly antes de irse también, dejándonos solo a nosotros tres."

hi "Bueno, parece que esos fueron todos."

show lilly basic_displeased
with charachange

li "Espero que no tengamos que hacer algo así de nuevo."

hi "¿Trabajar más allá de las hora de clases?"

show lilly basic_concerned
with charachange

li "Así es. Los planes del grupo este año fueron ambiciosos. Quizás demasiado ambiciosos."

show hanako emb_smile
with charachange

ha "Sin embargo, los puestos se ven bien."

hi "Tiene razón, se ve que han puesto mucho trabajo en ellos."

show lilly basic_ara
with charachange

li "Vaya vaya. Estoy segura de que muchos de nosotros estarían felices de oír eso. Al menos ahora no hay mucho trabajo que hacer hasta el festival."

show hanako basic_smile
with charachange

ha "Ahh… Se está haciendo bastante tarde. ¿Deberíamos irnos?"

show lilly basic_smileclosed
with charachange

li "Esa es probablemente una buena idea. ¿Volverás a los dormitorios tú también, Hisao?"

hi "Sí, creo que las acompañaré."

scene bg school_gardens2_ni
with locationskip

"La iluminación nocturna hace que los jardines se vean bastante diferentes. Comparado con la apariencia verde usual, las cosas se ven mucho más tranquilas."

"Considerando que es tan tarde, la falta de estudiantes alrededor puede que también colabore."
"Se les puede ver a uno o dos corriendo deprisa hacia y desde los dormitorios tratando de aprovechar al máximo el tiempo restante antes del toque de queda, pero no más."

"Todo lo que se puede escuchar son nuestros pasos, además del bastón de Lilly regularmente golpeteando gentilmente el suelo frente a ella."

"Es agradable poder finalmente relajarse un poco luego de estar tan locamente apresurado en la escuela."

"Sin siquiera notarlo, dejo salir un pequeño bostezo."

show lilly cane_smile_ni at twoleft
show hanako basic_normal_ni at tworight
with charaenter

li "¿Cansado?"

hi "Sí. Creo que aún me estoy habituando al correr de las cosas."

hi "Aunque la… este… cosa… con Shizune me tomó un poco desprevenido."

"Aprieto los dientes un poco ante la cándida mención de su, bastante público, altercado. Dicho eso, aún quiero aclarar qué diablos había detrás de eso."

show lilly cane_displeased_ni
with charachange

li "Ah… respecto a eso…"

li "Lamento que eso haya sido tan público. Shizune y yo… tenemos nuestra historia."


label es_A24c:




"Su voz parece ligeramente irritada al recordar a Shizune y, pensándolo mejor, posiblemente mi parte en lo sucedido."

show lilly cane_listen_ni
with charachange

li "Apreciaría si no la ayudases. Lo último que ella necesita es ser incitada."

"Bueno, eso confirma mis sospechas de ese momento. La hice enojar."

"Eso dicho, mientras que quizás inadvertidamente yo la haya lanzado a los perros, no podía saberlo y por ende no estoy en posición tal que necesite pedir disculpas."

"Un par de minutos de tenso silencio pasan entre nosotros, mientras que los ojos de Hanako saltan de izquierda a derecha."

"Renunciando a la oportunidad de recibir algún tipo de disculpa, Lilly se rinde y cambia el tema."



label es_A24d:



"Su voz muestra un leve dejo de irritación al recordar a Shizune, obviamente sin deseos de discutir mucho más."

show hanako basic_distant_ni
with charaenter

"Miro a Hanako para ver qué opina al respecto, pero su expresión es, como era de esperar, evasiva y difícil de leer."

"De todos modos creo que ella pidiendo perdón al respecto es algo, incluso si mi curiosidad se mantiene sin respuesta."



label es_A24e:



show lilly cane_weaksmile_ni
with charachange

li "De cualquier manera, estaré contenta una vez que el festival termine."

"El cambio de tema es bienvenido, despejando el denso aire con rapidez."

hi "Puedo imaginármelo. Los festivales de mi antigua escuela fueron mucho más sencillos que este."

show lilly cane_smileclosed_ni
with charachange

li "Yamaku enfatiza la idea de una comunidad escolar, así que el personal gusta de hacer festivales y demás en ocasiones especiales."

hi "Y aun así los estudiantes son los que hacen todo el trabajo. Qué mundo más injusto."

show lilly cane_giggle_ni
show hanako emb_emb_ni
with charachange

"Hanako y Lilly ríen en concordancia, saboreando el hecho de que nadie del personal está alrededor para escucharnos refunfuñar."

show lilly cane_smile_ni
show hanako basic_smile_ni
with charachange

li "Supongo que venir de una estricta escuela solo para chicas me ayudó un poco con Yamaku. En comparación, Yamaku es mucho más relajada."

"Eso sería un gran paso para explicar su bien educado modo de hablar y comportamiento, de cualquier manera."

scene bg school_dormext_half_ni
show lilly cane_smile_ni at twoleft
show hanako basic_smile_ni at tworight
with locationskip

"Al llegar a los dormitorios, eventualmente llega el momento de irnos a nuestras respectivas habitaciones."

hi "Nos vemos Lilly, Hanako."

"Las dos asienten cordialmente antes de dirigirse al dormitorio de las chicas, justo al lado del de los chicos."

stop music fadeout 4.0

hide lilly
hide hanako
with charaexit

"Como debería esperarse de una disposición tal, hay un miembro del personal patrullando casualmente afuera para prevenir cualquier travesura nocturna."

"Una vez que lo paso, estiro rápidamente mis brazos y masajeo mi cuello, ambos bastante adoloridos tras haber trabajado en el suelo por largo tiempo, antes de caminar a mi habitación."

"Aunque se siente bien en verdad tener algo de dirección. Tras tanto tiempo en el hospital, los hechos diarios de estudiar, las tareas y los profesores parecen casi una bendición."

"Supongo que si las cosas siguen así, mi tiempo en Yamaku podría terminar bien."


label es_A24a:

scene bg school_dormhisao_ni
with locationskip

"Adhiriéndome a la persistente voz del enfermero en mi cabeza, pongo la alarma de mi reloj para que me levante lo suficientemente temprano para volver a ir a trotar."

"Hice una promesa y voy a mantenerla. Además, Emi es capaz de delatarme si no aparezco."

"Pero no es que sea tan malo."

$ suppress_window_after_timeskip = True

scene black
with shuteye


label es_A24b:

scene bg school_dormhisao_ni
with locationskip

"Me siento cansado, así que pongo la alarma de mi reloj para levantarme lo más tarde posible y aún llegar a la primera clase."

"La voz del enfermero está casi dándome lata en mi cabeza por los trotes matutinos. Tomo la resolución de compensar al respecto yendo a caminar mañana después de la escuela."

"Apuesto que a Emi no le importará de cualquier manera."

$ suppress_window_after_timeskip = True

scene black
with shuteye

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
