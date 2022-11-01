label es_H21:

scene bg school_scienceroom
with locationchange

play music music_normal fadein 3.0

"Me levanté, tomé mis píldoras, me di un buen baño, rápidamente me deslicé dentro de mi uniforme, comí un sabroso desayuno, agarré mi mochila, y partí, todo por mi rutina diaria usual."

"Solo fue después de arribar a clases que la normalidad del día se fue al traste."

"Después de tomar mi asiento, observé a mis compañeros de clase entrando en el salón por la siguiente hora, hasta que cada asiento vacío fue eventualmente tomado, menos el de Hanako."

stop music fadeout 10.0

$ ksgallery_unlock("evul hanako_emptyclassroom")
scene evbg hanako_emptyclassroom:
    truecenter
    subpixel True zoom 0.9
    easein 20.0 zoom 1.0
show evfg hanako_emptyclassroom:
    truecenter
    subpixel True zoom 0.8
    easein 20.0 zoom 1.0
with whiteout

"Nunca me puedo acostumbrar a la idea de que ella simplemente no se aparezca en clase de vez en cuando. También se siente mucho más preocupante ahora, dado que Lilly se fue."

"Mientras Mutou continúa su monserga, mi mirada se encuentra revoloteando de vez en cuando hacia su asiento, como si fuera a aparecer ahí en cualquier momento."

"Nadie más parece preocuparse en absoluto por su ausencia, pero tienen pocas razones para hacerlo."

"Hanako ausente de clase, después de todo, es perfectamente normal. O al menos, lo era. Su asistencia no ha sido del todo mala por lo que he visto en mi tiempo aquí, pero aparentemente era mucho más marcado antes."

"Este también es un momento ominoso para que ella se vaya. Es un día antes de su cumpleaños, y mis sospechas están comenzando a aumentar, después del ataque que tuvo en clase cuando fue mencionado."

"Una cantidad en aumento de mis pensamientos es tomada por el cómo podría ayudarla, pero al final, siento como que no puedo hacer nada."

scene bg school_scienceroom
with silentwhiteout
play sound sfx_normalbell

"La campana anunciando el comienzo del almuerzo suena, sacudiéndome de mis pensamientos. Puede escucharse un suspiro colectivo de alivio de parte del grupo, pero Mutou parece bastante desconcertado."

"A él no le gusta ser interrumpido a mitad de sus apasionantes clases, después de todo."

"Justo cuando me estoy preguntando qué debería hacer en el receso del almuerzo, dado que Hanako y Lilly no están aquí, la solución se presenta por sí misma."

show shizu invis:
    tworight
    xpos 0.8
show misha invis:
    twoleft
    xpos 0.2
with None

show shizu behind_blank at tworight
show misha hips_grin at twoleft
with dissolvecharamove

play music music_shizune fadein 5.0

mi "¡Buenas tardes, Hicchan~!"

show shizu adjust_happy
with charachange

shi "…"

hi "Buenas tardes Misha, Shizune. Ambas lucen tan animadas como nunca."

show shizu basic_normal2
with charachange

shi "…"

show misha sign_smile
with charachange

mi "Shicchan quiere saber si te gustaría comer el almuerzo con nosotras hoy~."

hi "Seguro. Será bueno tener algo de compañía."

scene bg school_cafeteria
show crowd
with locationskip

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 1.0

"La cafetería zumba en actividad, bastante parecido a como lo hacía mi vieja escuela. Pero Yamaku es diferente, en lo… extrañamente civilizadas que son las prisas de la hora del almuerzo."

"Lo que uno esperaría que fuera una turba rebelde ansiosa por llegar al área de servicio es, en lugar de ello, una limpia y organizada fila."

"Hay una pequeña cantidad de empujones, y las cabezas de las personas están frecuentemente saliendo por los lados para revisar qué está pasando adelante, pero es muy tenue."

"Esto es así, sin duda, debido a las muy serias reglas concernientes a tales asuntos en esta escuela. La misma estricta disciplina se observa cuando los estudiantes se mueven por los pasillos, o vienen o van a sus dormitorios y el portón de la escuela."

"Aunque las razones para ello podrían ser ligeramente desconcertantes, como que ha llegado a agradarme este sentido de orden que es impuesto en la escuela."

show shizu behind_smile:
    tworight
    ypos 1.1
show misha perky_smile:
    twoleft
    ypos 1.1
with charaenter

hide crowd
with charaexit

$ renpy.music.set_volume(0.4, 7.0, channel="ambient")

"Pero realmente no me gustó ser mandado por Shizune y Misha a traer sus almuerzos. Me siento un poco usado mientras tomo asiento en la mesa donde ellas están, dejando caer su comida frente a ellas."

"Pan dulce y leche de fresa para Misha, un tazón de ramen y jugo para Shizune. Suelto un suspiro de alivio mientras bajo toda la comida, después de la considerable dificultad que tuve llevándola toda en adición a mi propio almuerzo."

show misha hips_grin
with charachange

mi "¡Gracias~!"

show shizu behind_smile
with charachange

"Misha da una palmada antes de abrir la envoltura y clavarse en su pan vorazmente. Shizune simplemente da un gesto afirmativo de aprecio con la cabeza antes de revolver su ramen y soplarle un poco para enfriarlo."

"Abro mi almuerzo, otro paquete de pan dulce, y le doy una mordida antes de pasarlo con algo de jugo. El pan es muy dulce, tanto que termino forzándome a tragarlo únicamente para terminar esta experiencia con él."

"A mitad de ello, decido tomar un descanso de la difícil tarea y preguntar lo que está en mi mente."

hi "Así que, supongo que ustedes dos tuvieron una razón para arrastrarme aquí. Ustedes dos parecen tener siempre un motivo oculto, después de todo."

show misha sign_confused
with charachange

mi "¡Qué esfás mifiendo, Hiffan~! No fenemos ningún ofro mofivo~."

show shizu basic_angry
with charachange

"Su boca está llena de pan dulce mientras habla. Es una vista bastante desagradable. Shizune luce un poco asqueada, antes de volver a comer su ramen."

show shizu basic_normal
show misha perky_smile
with charachange

"Espero hasta que Misha traga lo que tiene en su boca antes de hablar otra vez."

hi "¿No están tratando de engatusarme antes de ponerme a trabajar con ustedes después de la escuela?"

show misha hips_smile
with charachange

mi "¡Nop!"

hi "¿No están tratando de extraerme información que podría no querer dar?"

show misha cross_smile
with charachange

mi "¡No-o!"

hi "… Bien. Ustedes ganan. Entonces supongo que solo querían comer el almuerzo con alguien inteligente y guapo como yo."

show misha cross_grin
with charachange

mi "¡Eso es, Hicchan~! ¡Adivinaste~!"

"Shizune no luce impresionada mientras Misha termina de traducir nuestra conversación, y sorbe el último de sus largos fideos antes de decir con señas sus propios pensamientos."

show shizu behind_blank
with charachange

shi "…"

show misha sign_smile
with charachange

mi "Shicchan dice que no deberías tener sospechas de nosotras~. Ella solo está haciendo su trabajo como representante de la clase, después de todo~."

hi "¿Cómo está… em… haciendo eso?"

"Por mucho que odie admitirlo, parece como que aún tengo problemas comunicándome con Shizune."

"Debería ser un simple asunto de mantener contacto visual y dirigirme a Shizune en lugar de Misha cuando hablo, pero cuando alguien más está hablando por ella, es una tarea sorpresivamente difícil."

show shizu basic_normal2
with charachange

shi "…"

show misha hips_smile
with charachange

mi "Es el trabajo de la representante de la clase asegurarse de que a todos les vaya bien en clase, ¿cierto~?"

hi "No… realmente…"

hi "Espera, ¿cómo es que hacerme traer su comida asegura que me irá bien en clase?"

show shizu adjust_frown
with charachange

"Shizune resopla y ajusta sus anteojos desaprobatoriamente."

show shizu behind_frown
with charachange

shi "…"

show misha cross_frown
with charachange

mi "¿Entonces estas son las gracias que recibimos por darte compañía durante el almuerzo?"

$ renpy.music.set_volume(0.0, 3.0, channel="music")

"Eso es esquivar la pregunta por completo. Espera, detente…"

hi "¿Cómo sabías que yo…?"

show shizu basic_normal
with charachange

shi "…"

show misha sign_smile
with charachange

mi "Lilly está fuera y Hanako está ausente, y dado que esas dos son las únicas personas con quienes pasas el tiempo…"

show shizu adjust_smug
with charachange

shi "…"

show misha cross_smile
with charachange

mi "También lo hiciste un tanto obvio de ver~…"

$ renpy.music.set_volume(1.0, 3.0, channel="music")

"Ouch. Bien podría haber hecho eso, pero no necesitaba restregármelo. Tal vez me la hizo pagar por lo de antes."

hi "Cierto. Bueno, gracias. Lo aprecio, y eso es sin sarcasmo."

show shizu basic_normal
show misha perky_smile
with charachange

"Ambas asienten, y proseguimos con nuestros alimentos. Se siente un poco vergonzoso ser acompañado únicamente porque notaron que estaba solo, pero no es como si fueran extrañas tampoco."

"No pasa mucho antes de que termine mi último pan y comience con lo último de mi jugo, y mientras lo hago, me encuentro divagando en lo que había estado pensando antes de que las dos interrumpieran mis pensamientos."

"Se siente como si fuera el único en la clase que se da cuenta de que Hanako no está ahí. Se sintió así las otras veces que se saltó la clase, pero ahora es extremadamente más molesto."

"¿Alguien se preocupa de si es feliz o no? ¿Han simplemente descartado cualquier posibilidad de ayudarla a sentirse mejor? Ni siquiera Mutou intenta mantenerla en clase, y aún no estoy muy convencido de su razonamiento."

show misha perky_smile
with charachange

mi "Oye Hicchan, ¿tu jugo está caducado?"

hi "¿Qué?"

show misha hips_grin
with charachange

mi "Estabas poniendo una cara extraña, como esta~."

show misha perky_confused
show shizu adjust_happy
with charachange

"Como si fuera necesario, Misha imita mi expresión. Su exageración me hace hacer una mueca, aunque Shizune al menos encuentra algo de divertido en ella."

hi "Solo estaba pensando en Hanako."

show misha hips_smile
with charachange

mi "¿Oh?"

show shizu basic_happy
with charachange

"He captado el interés de Misha, y también de Shizune, una vez que mis palabras son interpretadas para ella."

hi "Solo estoy preocupado por que ella esté ausente tan seguido. Pero especialmente ahora con su cumpleaños a la vuelta de la esquina."

show misha perky_sad
show shizu behind_sad
with charachange

"Los recuerdos de ese incidente en clase están aún frescos en sus mentes. Con solo ver sus rostros puedo decirlo."

hi "¿Saben algo de Hanako? ¿Algo que podría ayudar?"

show misha perky_confused
show shizu behind_blank
with charachange

"Misha se encoge de hombros y voltea hacia Shizune, quien le da vueltas a ello por un rato."

show shizu basic_normal2
with charachange

shi "…"

show misha perky_smile
with charachange

mi "Las únicas personas a las que les ha dirigido más de una oración son tú y Lilly."

"Puede que Shizune no pueda transmitir el nombre de Lilly en tono burlón, pero siento como si reluciera en su lenguaje de señas. El efecto se pierde, de cualquier modo, después de la interpretación de Misha."

show shizu behind_blank
with charachange

shi "…"

show misha sign_smile
with charachange

mi "Hay un par de cosas que sabemos sobre Hanako como miembros del consejo estudiantil, gracias a los registros que pasan por nuestras manos, pero no podemos decir nada de lo que está en ellos."

hi "Es entendible."

"Suena bastante como la “confidencialidad del paciente” del enfermero. Cada vez que encuentro a alguien que sabe sobre el pasado de Hanako, resulta ser un callejón sin salida."

"La única forma en que lo descubriré será preguntándole. No sé si me dejará saber tales cosas, pero es por su bien, tengo que intentar al menos."

show shizu adjust_happy
with charachange

shi "…"

show misha hips_smile
with charachange

mi "No te preocupes por eso, Hicchan~. Sucede cada año, después de todo~."

"Eso no quita mi sentimiento de terror en absoluto. Aún me siento un poco en falta por lo que pasó en clase, pero esto se siente como que va más allá, incluso sin su confirmación de ese hecho."

show misha perky_confused
show shizu behind_blank
with charachange

"Misha nota mi expresión preocupada, y su cara alegre y tranquilizadora cae."

mi "Todos tienen problemas con los que lidiar, ¿cierto, Hicchan?"

hi "Seguro. Solo desearía que pudiera ayudar un poco más a Hanako con los suyos."

"Con eso, la conversación se dirige a términos depresivos."

stop music fadeout 4.0

show misha hips_grin
with charachange

"Eventualmente Misha se las arregla para traer el ambiente de nuevo a su usual jovialidad y alegres payasadas, pero mi mente permanece enfocada en Hanako."

"Iré a echarle un vistazo después."

stop ambient fadeout 1.0

scene bg school_dormhallway
with shorttimeskip

"Me aseguro de que mi puerta está cerrada antes de dejar caer mi mochila de la escuela."

"Los dormitorios están tranquilos."

"Mutou me mantuvo ocupado más tiempo del que esperaba, discutiendo mis estudios después de que las clases terminaron y continuando con unas hojas de trabajo para darle a Hanako casi como algo que se le ocurrió después."

"Absorbido en pensamientos, tardo en darme cuenta de la sombra que aparece frente a mí. El mirar hacia arriba me revela al dueño de dicha sombra."

show kenji happy at center
with charaenter

play music music_kenji fadein 0.5

ke "Oye, hombre. No te había visto hace tiempo."

hi "Oh. Hola."

show kenji tsun
with charachange

ke "¿Qué onda con esa respuesta?"

"Mi saludo despistado lo molesta visiblemente. Probablemente yo habría tenido la misma reacción."

hi "Perdón, solo estaba pensando en varias cosas."

ke "“Pensando” es una respuesta bastante pobre para no estar ayudando en la campaña solidaria de la guerra."

hi "¿Y cómo va la guerra?"

show kenji neutral
with charachange

ke "Me estoy preparando. Ahora mismo necesito dinero para ayudar con esas preparaciones."

hi "Si quieres que te preste dinero, solo dilo."

show kenji happy
with charachange

ke "No hombre, estoy bien."

hi "¿Estás… bien? ¿No quieres mi dinero?"

show kenji tsun
with charachange

ke "Oye hombre, no te veas tan sorprendido. Es insultante."

show kenji neutral
with charachange

ke "Soy bastante bueno en el escenario competitivo del boliche, pero ayer, encontré a unos chavos que no sabían eso."

hi "Estoy bastante seguro de que apostar iría contra las reglas de la escuela…"

show kenji tsun
with charachange

ke "Las reglas de la escuela no importan; esta es una situación de guerra. La gente estos días, ellos no tienen apreciación por lo que la guerra significa."

hi "Así que ¿para qué necesitas ese dinero, si me permites preguntar?"

show kenji neutral
with charachange

ke "Comida enlatada imperecedera. Materiales de construcción; más que nada láminas y paneles de madera. Kit de primeros auxilios. Calentador de campamento. Radio portátil. Bolsa de dormir. Reloj mecánico."

"Al inicio me parece más bien un surtido aleatorio de objetos y materiales, pero después de unos segundos, me doy cuenta."

hi "¿No es esa una lista de materiales para un refugio nuclear?"

show kenji happy
with charachange

ke "Ah, así que has leído el panfleto “Protect and Survive”. Es bueno ver a alguien tan informado sobre cómo protegerse a sí mismo."


hi "Realmente no piensas…"

show kenji neutral
with charachange

ke "No es una posibilidad de cero."

hi "No, estoy bastante seguro de que hay cero posibilidades de que eso suceda alguna vez."

show kenji happy
with charachange

"Lenta y dramáticamente levanta una ceja. Bueno, tan dramáticamente como alguien puede levantar una ceja."

hi "Las probabilidades son, no lo sé, cero punto uno en el billonésimo lugar. Es infinitesimal. Además, ¿dónde puedes construir un refugio nuclear de cualquier manera? Ciertamente no en el campus."

show kenji neutral
with charachange

ke "Es mi proyecto de verano mientras estoy en casa. Mi padre dijo que puedo hacerlo."

hi "¿En verdad?"

ke "Sí. Él pensó que mejoraría mis habilidades de construcción y destreza manual. O algo."

"Conociendo a Kenji, su papá probablemente solo pensó que esto podría mantenerlo fuera de su camino por un tiempo."

"Aun así, me hace preguntarme cómo son sus padres. Tal vez son totalmente normales, y Kenji es una aberración. Por otro lado, tal vez este tipo de paranoica y temerosa supervivencia rige a la familia."

show kenji happy
with charachange

ke "Oye, ¿quieres ayudarme a construirlo? Luces como el tipo útil con herramientas. Si tuviera tu ayuda, podríamos hacer un búnker realmente cabrón en lugar de solo un refugio nuclear."

"Lo dudo. Jugar futbol antes de mi accidente me dio buen trabajo de piernas, pero realmente nunca probé mi suerte con nada que se acercara a trabajo manual real."

hi "No lo soy, en verdad. Me temo que estoy ocupado en las vacaciones de todas formas."

show kenji tsun
with charachange

ke "Una pena. Si las feministas alguna vez se apoderan de los códigos de lanzamiento, temo que pocos estarán preparados."

hi "¿Y tu refugio nuclear te protegerá de la explosión de una bomba nuclear, en el caso de que eso en realidad pase?"

ke "Un refugio nuclear no está pensado para protegerte contra la explosión. Para eso son los refugios contra explosiones."

ke "Pensé que lo sabías bien."

hi "Mi error…"

show kenji neutral
with charachange

ke "Mi casa está bastante lejos de todos los sitios militares grandes, así que la lluvia radioactiva que sigue al mecanismo nuclear es una preocupación mayor que la explosión en sí."

show kenji happy
with charachange

ke "Lo que esto hará es mantener el polvo y otras partículas lejos de mí, mi suministro de comida, y mi área de sueño. Pero tiene que durarme al menos catorce días."

hi "Catorce días es un tiempo bastante largo."

show kenji neutral
with charachange

ke "Lo es. Necesito un litro de agua al día para beber, óptimamente dos para poder bañarme también. El aseo personal es bastante fácil; solo algunas bolsas de basura y un bote colocado afuera del área del refugio."

ke "Comida significa suministros enlatados, desde luego."

hi "Por supuesto. ¿Y la radio está para comunicación con el exterior?"

ke "Correcto, correcto. Para que pueda captar alertas del gobierno sobre lo que está pasando afuera. Necesito un reloj mecánico en lugar de uno eléctrico en caso de que el pulso electromagnético de la explosión nuclear aérea lo fría, también."

ke "Están todas las otras cosas que necesito también, como ropa extra, cerillos, y velas. Pero creo que aún tengo tiempo de recolectarlo todo. Tal vez."

"Por mucho que odie decirlo, estoy un poco impresionado. Realmente ha investigado esto y lo ha pensado. Por otro lado, no sé si querría vivir en un mundo postapocalíptico donde solo gente como Kenji ha sobrevivido."

hi "Suena como que realmente sabes lo que estás haciendo."

show kenji happy
with charachange

ke "Lo sé perfectamente."

"Debe ser difícil, vivir en constante miedo como este. También difícilmente socializa, así que el hecho de que haya ido a jugar boliche con otros es en sí mismo una sorpresa."

"Esto me recuerda mentalmente un poco a alguien. Por suerte, su miedo a otros no se manifiesta en una forma tan distintamente excéntrica."

"Una cosa que tengo por seguro es que ciertamente no puedo decirle con exactitud por qué no he pasado mucho el rato con él últimamente."

hi "Es tarde. Tengo cosas que hacer. Pero pensaré sobre hacer un refugio nuclear o algo."

show kenji neutral
with charachange

ke "Sí, bien, esto es genial. Un hombre debe hacer lo que un hombre debe hacer, después de todo."

ke "Debes pasar el rato conmigo alguna vez, por cierto. Eres un tipo genial. Los tipos geniales pasan el tiempo juntos, ¿cierto?"

"Por alguna razón, ese cumplido de hecho se siente algo bien. La situación con Hanako siendo como es, sin embargo, significa que probablemente no podré cumplir su petición. Por ahora, al menos."

hi "Eso estaría bien. Hablaré contigo sobre ello después cuando pueda."

show kenji happy
with charachange

ke "Genial. Nos vemos luego, chico."

stop music fadeout 3.0

hide kenji
with charaexit

"Él se retira a su habitación."

"Mejor voy a ver a Hanako."

stop ambient fadeout 1.0

scene bg school_dormhanako_ni
show hanagown worry_close:
    center
    xpos 0.39
show expression Solid("#00000022")
show hanako_door_base at right
show hanako_door_door at left
with locationskip

"Me paro afuera en la puerta de la habitación de Hanako, esperando que no esté en un mal estado mientras nerviosamente aprieto las hojas de trabajo que Mutou me pidió que le pasara."

"Es una razón más para visitarla, y me da algo sobre lo cual hablar, así que supongo que debería estar agradecido con él por darme esta tarea."

play sound sfx_doorknock2

"Con un largo aliento me tranquilizo, golpeo mis nudillos en la puerta frente a mí."

"… Silencio. Escucho atentamente por cualquier sonido de desorden viniendo de adentro."

$ renpy.music.set_volume(0.5, 0.0, channel="sound")
play sound sfx_hammer

"Toco la puerta otra vez, ligeramente más fuerte."

"Aún no hay respuesta. Qué extraño."

"Rascando mi cabeza, hago un último intento por hacer que responda mientras toco la puerta una última vez."

hi "Hanako, solo soy yo. Mutou dijo que te diera unas cosas."

"Por un rato, el intento parece ser tan infructuoso como el anterior. Pero justo antes de que deslice las hojas bajo su puerta, puedo escuchar la manija crujiendo."

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_dooropen

show hanako_door_door:
    xpos -0.1
with charamove

play music music_moonlight fadein 4.0

"Mientras la puerta se abre a la mitad, rápidamente trato de ver cómo le está yendo a Hanako. Es una tarea que se hace un poco más difícil por su camisón extragrande escondiendo la mayor parte de su cuerpo."

"No luce enferma, o al menos no inmediatamente. Para ser honesto, hubiera preferido eso a su expresión justo ahora. Luce terriblemente cansada, y parece estar reconociendo apenas mi presencia."

hi "Hola, Hanako. Mutou quería que te diera esto porque no estuviste en clase hoy."

"Le ofrezco las hojas sueltas, que ella toma en sus manos con vacilación. La forma en que se mueve es desprovista de pensamiento. Su postura está desplomada, en una forma inusual para alguien en constante tensión y nerviosismo."

show hanagown distant_close
with charachange

"Incluso sus ojos se mantienen mirando lejos de los míos, haciendo lo mejor posible por evitar contacto visual. Muevo mi cabeza un poco para intentar obtener una mejor vista, pero ella termina girando a otro lado."

hi "¿Estás… bien? Si te sientes enferma o algo, podría ir por una enfermera."

"Casi se siente detestable meter en el acto la rutina de “mejórate pronto”. Pero no puedo pensar en nada más que podría hacer por ella."

show hanagown normal_close
with charachange

"Parece concentrarse un poco con la idea… pero solo un poco. Su cabeza permanece girada a otro lado, pero sus ojos se mueven hacia mí."

ha "Estoy bien."

"Sigue un silencio incómodo. Mientras está en suspenso, noto que las mangas y los puños de su camisón tienen pequeñas manchas de humedad. Sus mejillas están un poco rojas también. ¿Ha estado llorando?"

hi "Ya veo."

"Dudo un poco antes de decir las palabras que en realidad vine a decir."

hi "¿Te gustaría que me quedara? No tengo nada urgente que hacer en este momento, así que no sería ningún problema."

show hanagown distant_close
with charachange

"Sus ojos se deslizan lejos de mí, y pierdo cualquier esperanza de mejoría en su humor. Espero por una respuesta, pero no dice nada, ni hace ningún gesto. Solo está de pie ahí, sin verme a mí."

hi "¿Hanako…?"

"Ella lentamente sacude su cabeza."

hi "Está bien. Emm… buenas noches, entonces."

stop music fadeout 3.0

show hanako_door_door:
    xpos 0.0
with charamove

play sound sfx_doorclose

"Con eso, Hanako da un paso atrás y cierra su puerta sin decir nada más."

"Más que un poco preocupado, regreso a mi habitación."


scene bg school_dormhallway
with locationskip

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_footsteps_hard

"Deambulando por el corredor, continúo reflexionando sobre lo que pasó."

"Se siente como si Hanako hubiera estado ahí solo parcialmente, como si yo estuviera interactuando con un robot que solo estaba haciendo lo que le fue programado sin pensarlo realmente."

"Era la cáscara de una persona."

"Esto es frustrante. Había esperado que ver a Hanako ayudaría con la situación, pero siento como si solo lo hubiera hecho más difícil de entenderla. ¿Cómo se supone que trataré de ayudarla cuando literalmente me cierra la puerta en la cara de esa forma?"

stop ambient fadeout 0.3

scene bg school_dormhisao_ni
with locationchange

"Ni siquiera me molesto en prender la luz, optando por simplemente cambiarme a mi pijama, rápidamente trago mis píldoras de la noche, y colapso en mi cama."

scene black
with shuteye



label es_H22:

scene bg school_scienceroom
with locationchange

play music music_pearly

"Una vez más, Hanako no asiste a clases. Por más que intento concentrarme en otras cosas, este hecho continúa distrayéndome a lo largo de toda la jornada escolar, e incluso mientras camino a través de los jardines de la escuela a los dormitorios."

"No creo tampoco que el que hoy sea su cumpleaños sea una coincidencia. Sin embargo, no sé el enlace entre los dos eventos, ni tengo idea de lo que está sintiendo."

"Si fuera dolor físico, podría al menos proveer algo de consuelo. Pero con algo como esto, no tengo idea de dónde empezar."

"Recorro la gente que conozco en mi cabeza, pensando en si podrían ayudar. Shizune y Misha no saben mucho acerca de Hanako, y lo poco que saben no pueden decírmelo. Lo mismo con el enfermero."

"Al final, solo hay una persona que conoce bien a Hanako y aceptará decirme algo."

scene bg school_dormhisao
with shorttimeskip

"Entrando a mi habitación del dormitorio, noto algo que me toma con la guardia baja; está comenzando a sentirse familiar."

"Con todo lo que está pasando a mi alrededor, me siento agradecido de que esta habitación ha comenzado finalmente a ser un lugar donde puedo relajarme un poco."

"Cuando entré a Yamaku por primera vez, se sintió inmediatamente ajena en todo sentido, de la pulcritud intacta a la forma en que olía."

"Concentrándome en el problema a la mano, lanzo mi mochila a la cama y abro el cajón superior de mi escritorio."

"Antes de irse, Lilly me dijo el número para llamarla mientras estuviera en Escocia y lo escribí. En retrospectiva, me pregunto si sabría que algo así pasaría."

"Ahora que está fuera de alcance, me doy cuenta de lo mucho que Hanako y yo hemos dependido de su guía."

"Revuelvo cajón tras cajón, buscando ese maldito pedazo de papel. Eventualmente, por suerte, lo encuentro anidado bajo un libro prestado de la escuela."

scene bg school_dormhisao_blurred
show phone mobile:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with locationchange
with Pause (0.5)

"Probablemente debí solo meterlo directamente en mi celular, ahora que lo pienso. Sin más preámbulos, marco los números y presiono ansiosamente el botón de llamada."

"Eventualmente contestan el teléfono, una voz femenina que no reconozco al otro lado. Es probablemente la madre de Lilly."

stop music fadeout 1.0


mystery "{image=vfx/garbage.png} {image=vfx/garbage.png} Satou ¿{image=vfx/garbage.png}?"

"¿Inglés? Súbitamente encontrándome desprevenido, me doy cuenta de que no puedo entender lo que dice, sea por mi vocabulario limitado o su fuerte acento. Debí haber anticipado esto, dado que de acuerdo a Lilly, su madre es nativa escocesa."

"Sigo adelante con la esperanza de que ella sepa algo de japonés, considerando que es el idioma nativo de su hija."

hi "Em, es Hisao Nakai… al habla…"

"Un entusiasta sonido de entendimiento puede ser escuchado al reconocer el idioma. Mi sentimiento de alivio es inmenso."

"Sra. Satou" "Ah, tú debes ser uno de los amigos de la escuela de Lilly, ¿correcto?"

"Aun así, su acento significa que me tengo que concentrar en lo que está diciendo."

hi "Sí, es correcto. Encantado de hablar con usted, Señora Satou."

"Sra. Satou" "¡Es tan gentil de su parte encontrar a alguien tan educado! ¡Lilly, querida, es para ti!"

"Su madre parece agradable, si acaso algo entusiasta dado lo mundano de la situación."

"Hay un pequeño silencio mientras Lilly se toma su tiempo para agarrar el teléfono. En la distancia, puedo distinguir a su madre regañándola juguetonamente por recién levantarse."

li "Hola, Lilly al habla."

hi "Suenas terrible."

"Ella hace un sonido en algún punto entre un animal muriendo y un bostezo."

"Lo que sí me acordé de revisar antes de hablar fue la zona horaria. Debería ser bastante tarde en la mañana por allá, así que realmente no tiene excusa."

hi "¿No te sientes bien?"

li "Solo cansada. ¿Qué hora es allá?"

hi "Casi es de noche. La escuela terminó por hoy no hace mucho."

li "Hanako no está bien, ¿o sí?"

play music music_drama

"Eso fue rápido. Mi suposición de que ella debía saber que algo como esto podría pasar parece haber sido correcta."

hi "¿Cómo supiste?"

li "Porque hoy es su cumpleaños. Tenía la esperanza de que se hubiera puesto al menos un poco mejor después de conocerte, pero…"

li "¿Cómo está ahora mismo?"

hi "No fue a la escuela hoy ni ayer. Aún tengo que ir a ver cómo está hoy. Para ser honesto, después de ver cómo estaba cuando hablé con ella ayer… estoy bastante ansioso."

hi "En verdad no tengo idea de qué pensar de esto. ¿Ha pasado esto en el pasado? ¿Está relacionado con sus cicatrices de alguna forma?"

li "Desafortunadamente sí. Prácticamente lo mismo pasó el año pasado cuando su cumpleaños llegó."

li "Hasta donde puedo decir, es porque sus padres murieron en el accidente que causó sus cicatrices, y Hanako se culpa por sus muertes."

"Lo que dice parece tener sentido. Si se está culpando a sí misma en su cumpleaños, bien podría estarse lamentando incluso de haber nacido."

"Hanako me había mencionado su estadía en el orfanato. Tal vez debo considerar como un hecho que ella confía lo suficiente en mí para decirme tal cosa."

"Pero Lilly viéndose en tanta oscuridad sobre ello, casi al mismo grado que yo, es una sorpresa."

hi "Así que ese es también el porqué ella vive en los dormitorios de estudiantes. ¿Te ha dicho algo más sobre el accidente?"

li "Con lo cercanas que nos hemos vuelto… apenas me ha dicho algo sobre lo que sucedió. Lo que sé sobre ello son más que nada conjeturas."

"Ella suena deprimida, casi derrotada. Considerando el trauma por el que Hanako debió pasar, realmente no puedo culpar a Lilly por no saber. No obstante eso, de todas formas parece considerarlo una falla personal."

hi "No te culpes, Lilly. Con todo lo que ella ha pasado…"

"Hay un largo silencio del otro lado de la línea. Comienzo a preguntarme si la llamada se cortó antes de que la voz del otro lado comience a hablar."

li "Hay otra persona, sin embargo, que también ha sido objeto de preocupación para mí."

hi "¿Oh?"

"Recorro en mi cabeza las personas de las que ella podría estar hablando. Los únicos amigos que parece mantener muy cerca somos Hanako y yo, aunque está Akira también…"

li "Esa persona eres tú, Hisao."

"Hay otro silencio en la línea, pero esta vez es causado por mí."

"Hacer que otros se preocupen por mí es algo que he tratado muy activamente de evitar desde que llegué a Yamaku."

"De hecho, incluso mi interacción con Hanako me ha ayudado a evitar cualquier problema de salud mayor gracias a nuestras relajadas y tranquilas vidas."

hi "Eh… heh. ¿Hay algo de qué preocuparse en mí?"

li "Me disculpo; no era mi intención ofender."

hi "Perdón, solo me tomaste un poco con la guardia baja. Como sea, ¿no es Hanako un problema mayor en este momento?"

li "Ya hace algún tiempo he pensado que ambos podrían haber estado alimentándose entre ustedes los hábitos más preocupantes de cada uno. Traté de enmendar esto antes de irme, pero parece que logré muy poco."

hi "¿“Hábitos preocupantes”?"

li "Cuando te pregunté sobre lo que tenías en mente para el futuro, tu respuesta fue muy similar a lo que Hanako había dicho en el pasado cuando esa pregunta se le presentó."

li "Está bien y es bueno querer protegerla, pero temo que tratar a Hanako de esa forma, como si fuera una hija o alguien con necesidad de cuidados especiales, va a conseguir lo opuesto."




label es_choiceH22:
menu:
    with menueffect
    "La situación efectivamente está de cabeza. Después de todo lo que ha pasado, esta es la primera vez que me encuentro dudando del juicio de Lilly."
    "Estar de acuerdo con Lilly.":


        return m1
    "Confiar en mi propio juicio.":

        return m2

label es_H22a:

"No quiero admitirlo, pero ella puede tener un buen punto. Sin embargo, algo más me molesta."

hi "¿Y tú trataste de… “enmendar” esto?"

hi "Espera… ¿Nuestra salida a la ciudad?"

li "Bastante astuto. Pensé que podría ayudar si los arrastraba a ambos fuera de Yamaku y hacia el mundo más amplio. Aunque estoy agradecida de que por ello se acercaron más entre ustedes."

"Así que notó eso. Supongo que ella bien podría haber estado prestando atención a nosotros, y su oído es increíblemente bueno; tal vez lo bastante para haber escuchado de lo que estábamos hablando, si lo intentó."

hi "Esto suena más como a que nos estabas manipulando."

"Silencio. Es una manera dura de ponerlo, pero no tengo intenciones de retirar esas palabras."

li "Lo siento. Solo estaba… preocupada por ustedes."

hi "Está bien. Supongo que hay cosas más importantes de cualquier modo."

"No es una completa sorpresa que ella haría tal cosa. Su naturaleza maternal puede ser un poco dominante a veces, pero tiene las mejores intenciones."

hi "¿Así que piensas que debería pensar más en mí en lugar de tratar de ofrecer ayuda a Hanako?"

li "Eso lo resume casi todo. Otra vez, lamento no haberte dicho esto de forma más clara antes de hacerlo todo a tus espaldas."

li "Sé que soy al menos tan culpable como tú de ser sobreprotectora con Hanako, pero temo que estás descuidando tu persona en tus esfuerzos por darle felicidad a Hanako."

hi "¿En verdad crees que Hanako estará bien?"

li "No es tan frágil como tú piensas. No sé exactamente por qué experiencias ha pasado, o qué sentimientos hay en su cabeza, pero se las ha arreglado para seguir su camino a través de ello hasta ahora."

li "También es mi esperanza que darle un poco de espacio le permitirá decidir lo que realmente quiere para ella, y le dará la iniciativa para alcanzarlo."

li "Por favor ten fe en Hanako. Eso es todo lo que pido."

hi "Lo… Supongo que lo pensaré un tiempo."

li "Eso está bien. Ser impulsivo no te llevará a ningún lado."

li "Sé que por momentos podrías dudar de tu relación con Hanako, pero ella…"

"Lilly se corta y toma un momento para reconsiderar sus palabras."

li "Por favor ten en mente que no me habría hecho tu amiga si no hubiera pensado que eres una persona fundamentalmente buena. Eres un buen amigo, para mí y Hanako."

hi "Gracias. Eso ayuda."

"Compartimos una charla para tratar de alegrar la atmósfera, pero se siente muy poco natural. Hay mucho que no sé sobre la estadía de Lilly en Escocia, pero después de un tema tan pesado, quiero estar solo por un rato para pensar."

stop music fadeout 8.0

show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with None

scene bg school_dormhisao
show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with locationchange
with Pause (0.5)

hide phone
with None

"Después de unos pocos minutos, terminamos diciendo nuestras despedidas y dejo mi teléfono en el escritorio."

"Comparada a la situación de Hanako, la mía se siente totalmente mundana. Aún tengo a mis dos padres, tuve una niñez razonablemente normal, y a diferencia de muchos en Yamaku, mi condición no es inmediatamente visible para el público."

"Pero por otro lado… ¿no es este solo un intento por justificar la forma en que he estado actuando frente a ella?"

"Eso bien podría ser cómo fueron nuestros pasados, pero cuando se trata del futuro aún no tengo idea de qué es lo que quiero hacer."

"En la escuela solamente me he concentrado en el trabajo de cada día, y he pospuesto más y más cosas para prestarle apoyo a Hanako."

"Recuerdo las palabras que Mutou me dijo después del ataque de Hanako; sobre el propósito de Yamaku y mi educación. En retrospectiva, él probablemente estaba tratando de promover exactamente lo mismo."

"¿Simplemente qué he estado haciendo en el tiempo desde mi ataque al corazón? Si alguna vez me las arreglo para sacar a Hanako de su habitación y hacer que se sincere, ¿entonces qué?"

"Veo hacia afuera de la ventana de mi dormitorio mientras el sol se pone lentamente. Es una buena vista, pero lo que realmente saboreo es la tranquilidad mientras los estudiantes regresan a las habitaciones de su dormitorio."

"Todo lo que quiero hacer ahora es pensar. No estoy seguro de cuánto tiempo tengo, pero quiero planear a dónde iré a partir de aquí."

scene black
with dissolve




label es_H22b:

stop music fadeout 5.0

"Escucho cuidadosamente lo que Lilly tiene que decir, pero no puedo llegar a estar de acuerdo con ella."

"Hanako es una persona delicada en el mejor de los casos, y después de lo que pasó cuando se mencionó su cumpleaños, creo que esta es la última situación donde deberíamos dejarla sola si está recluyéndose deliberadamente."

"Pero se siente como que Lilly tiene una imagen bien definida en su mente de cuál es la mejor forma de lidiar con Hanako. No solo ahora, sino durante todo el tiempo que las he conocido."

"Le doy vueltas en mi cabeza al mejor curso de acción, y me encuentro tratando de estar de acuerdo verbalmente con Lilly en voz baja y de forma tan ambivalente como puedo."

"Tenemos una charla después de eso, pero ninguno de los dos tiene realmente el estómago para ello a la luz de los eventos recientes. Decimos nuestras despedidas antes de colgar."

show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with None

scene bg school_dormhisao
show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with locationchange
with Pause (0.5)

hide phone
with None

"Quiero hablar con Hanako yo mismo, ayudarla lo mejor que pueda. Lo mejor para ella justo ahora sería tener a alguien cerca, no dejarla sola."






label es_H22c:

stop music fadeout 5.0

"Escucho cuidadosamente lo que Lilly tiene que decir, pero no puedo llegar a estar de acuerdo con ella."

"Quiero estar más con Hanako. Quiero ser un mejor amigo, apoyarla cuando necesite apoyo, y estar ahí cuando más necesite de la gente. Creo que ahora es una de esas veces."

"El recuerdo del dueño de la tienda que conocimos en la ciudad aún me desconcierta. Cualquiera que le dé la más ligera mirada a Hanako termina mirándola fijamente, y culparlos por ello sería completamente hipócrita, dada mi propia reacción."

"No me gusta tampoco mi propia cicatriz, pero al menos puedo cubrirla con algo tan simple como una playera. No puedo imaginar una vida donde cada día lo pasara tratando de esconder mi persona tanto como fuera posible."

"Y encima de todo, Hanako ni siquiera tiene personas a su alrededor que le darían apoyo sin importar cómo luce. Vivo lejos de mis padres, pero aún puedo contactarlos y visitarlos cuando desee."

"Le doy vueltas al mejor curso de acción en mi cabeza, y me encuentro tratando de estar de acuerdo verbalmente con Lilly en voz baja y de forma tan ambivalente como puedo."

"Tenemos una charla después de eso, pero ninguno de los dos tiene realmente el estómago para ello a la luz de los eventos recientes. Decimos nuestras despedidas antes de colgar."

show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with None

scene bg school_dormhisao
show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with locationchange
with Pause (0.5)

hide phone
with None

"Hay al menos una cosa que puedo hacer por Hanako. Si hago este pequeño gesto por ella, solo puedo esperar que me permita acercarme ese poquito más a ella."





label es_H23:



scene bg school_dormhanako_ni
show hanako_door_base at right
show hanako_door_door at left
with shorttimeskip

play sound sfx_hammer


play music music_tragic fadein 0.5

"Golpeo mis nudillos tres veces en la puerta de Hanako. Como esperaba, no hay respuesta. Brevemente considero tocar otra vez, pero sé muy bien que solo obtendría el mismo resultado si lo hiciera."

"Descansando mi mano en la manija de la puerta de Hanako, trato de preparar lo que quiero decirle. Pero por más que intento, realmente no puedo pensar en nada que valga la pena decir. Quiero reconfortarla, sí, pero no tengo idea de cómo hacer eso."

"Por sí solo eso es casi suficiente para detenerme. Sin embargo, le dije a Lilly que lo haría, así que siento que tengo que seguir, me sienta confiado o no."

"Giro la manija hacia abajo, con una gran cantidad de vacilación. Sin embargo no se mueve mucho, dado que está cerrada con seguro."

hi "Hanako…"

"Así que en verdad me dejó afuera. Después de todo lo que pasó entre nosotros y el tiempo que pasamos juntos… me ha dejado afuera por completo."

hi "Em… no sé si puedes oírme, pero…"

hi "Solo quiero hablar contigo un poco. Si puedes oírme, ¿podrías quitar el seguro a la puerta?"

with Pause(4.0)

play sound sfx_lock

"Espero en silencio. Los minutos pasan, pero eventualmente escucho pasos viniendo a la puerta y el seguro siendo quitado."

"Al menos está dispuesta a escucharme. Eso es algo bueno."

hi "Yo… no sé realmente qué decir, pero… solo quería verte. Quería asegurarme de que estás bien."

"Tomo un respiro antes de empujar la manija hacia abajo y abrir la puerta. Si le quitó el seguro sin decir protesta, debe estar bien que yo entre."

play sound sfx_door_creak

show hanako_door_door:
    easeout 1.0 xpos -0.2
show hanako_door_base:
    easeout 1.0 xpos 1.1
show bg school_dormhanako_ni:
    center
    easeout 1.0 xpos 0.55
with None

scene bg school_dormhanako
show hanagown distant:
    center
    ypos 1.15
with silentwhiteout

"Hanako está sentada al lado de su cama, su rostro triste como pensando profundamente. Su habitación está tan austera como siempre, y ahora mismo, ella parece estar perfectamente acorde al humor que esta despide."

show hanagown normal
with charachange

show hanagown worry at center
with Dissolvemove(0.2)

"Eventualmente, sus ojos se mueven lentamente hacia la puerta. Tan pronto como nota mi presencia, sale disparada de su cama y salta a sus pies, encarándome de frente."

"Su enorme camisón hace que este gesto luzca mucho más marcado dado que se mueve libremente a lo largo de su delgada figura."

ha "¿Q-qué estás…?"

"Rápidamente me arrepiento de haber venido cuando la veo. Luce deprimida, pero hay un matiz de enojo detrás de eso. Así que ella puede hacer este tipo de expresión también."

hi "Solo… solo quería revisar que estuvieras bien. Pensé que estaría bien, dado que quitaste el seguro a la puerta."

show hanagown distant_blush
with charachange

"Hanako abre su boca para hablar, pero rápidamente la cierra otra vez antes de voltear a otro lado."

show hanagown distant_blush:
    center
    ypos 1.15
with charamove

"Permanecemos en silencio por un tiempo, antes de que ella regrese y se siente en la orilla de su cama. No estoy seguro si está frustrada conmigo y resignada al hecho de que estoy aquí, o está genuinamente cómoda de que yo esté en su habitación."

"Una vez más, me encuentro completamente imposibilitado de descifrar cómo se siente. Es molesto."

"Termino caminando a su escritorio y tomando asiento. Lo hago lentamente, para darle tiempo a decir cualquier queja que pudiera tener sobre el que yo esté ahí, pero no dice nada. Todo lo que hace es mirar al piso, sin mover un músculo."

"Después de sentarme con el respaldo frente a mí, le doy una mejor mirada a Hanako. Parece pálida, pero sus mejillas lucen rojas. No estoy seguro si ha estado comiendo bien, tampoco, dado lo delgada que se ve su figura."

"Lilly podrá haber dicho que sería mejor si mantuviera más la distancia con ella, pero es difícil pensar en eso como la forma correcta de tratar con Hanako cuando luce de esta forma."

"Ella se mantiene mirando al piso sin decir palabra, como esperando a que yo diga algo. Es totalmente razonable, dado que yo fui el que vino a su habitación."

hi "¿Quieres ir a algún lado? Bajar la colina hacia el pueblo puede que sea demasiado, pero podríamos al menos dar una caminata afuera."

show hanagown worry_blush
with charachange

ha "¿Por qué… quieres hacer eso?"

hi "Solo estaba pensando que podría ayudarte un poco. Pasas demasiado tiempo dentro, pronto tu piel se va a poner tan pálida como la de Lilly."

show hanagown distant_blush
with charachange

"Bufo un poco divertido, esperando que Hanako haga lo mismo, pero ella no reacciona; solo vuelve a mirar al piso."

ha "Si tú no quieres ir… t-tampoco yo quiero ir."

hi "Está bien. Jugaba futbol y salía mucho con mis amigos después de la escuela antes de venir a Yamaku, así que me gusta estar al aire libre."

"Hanako no muestra reacción visible. Es difícil hablar cuando la discusión es de un solo lado."

hi "Podríamos ir a la biblioteca… eh, si no estuviera ya cerrada. Aunque los jardines estarían bien."

"Ella comienza a jugar con su cabello. Me distrae, y me parece algo un poco inusual para ella."

"Por otro lado, desde que el incidente en clase sucedió, he andado de puntillas cerca de ella por miedo a lastimarla de esa forma otra vez. Tratar activamente de sacarla podría ser algo bueno."

"Me inclino hacia adelante un poco más en la silla y le doy una sonrisa ligeramente forzada, para intentar alegrar el ambiente un poco."

hi "No habría nadie alrededor para esta hora, así que no tienes que preocuparte por que alguien se atraviese en nuestro camino. Podría ser una pequeña cita o algo."

show hanagown normal
with charachange

"Doy una ligera risilla, pero me detengo cuando Hanako deja de jugar con su cabello y se aferra a su cama con fuerza. La boca de Hanako se mueve, pero por más que intento, no logro captar lo que está murmurando."

hi "¿Hanako?"

ha "Tú… no entiendes…"

"Incluso ahora, apenas puedo entender lo que está diciendo."

"Se siente como que está tratando de hacer su presencia tan pequeña como es posible; hacer eso es increíblemente natural para ella en clase o cerca de otros, pero duele cuando trata de hacerlo cerca de mí."

hi "Te lo dije, está bien. Solo es una pequeña caminata, nadie va a notarnos."

"Me levanto de la silla y camino hacia la puerta, girando para invitar a Hanako a seguirme. Una vez más, ella no responde a nada de lo que digo."

show hanagown distant
with charachange

ha "Yo no…"

hi "Ir afuera por un rato es bueno para aclarar tu mente."

ha "¿Por qué… quieres hacer esto…?"

hi "Porque quiero ayudarte."

ha "No… quiero… ayuda. ¿Viniste aquí… para tratar de sacarme…?"

hi "No me molesta. Creo que todos necesitan ayuda de vez en cuando. Cuando estaba tratando de sobrellevar mis primeros días en Yamaku, tú y Lilly me ayudaron mucho."

hi "Además, no estoy exactamente ocupado."

ha "No q-quiero ir. Estoy… bien."

hi "En realidad no creo que sea sano permanecer encerrado por tanto tiempo. Al sol aún le queda algo de vida, así que no creo que sea tarde para dar al menos una pequeña caminata."

hi "Probablemente podría sacar provecho de algo de ejercicio en cualquier caso, para ayudar a despertarme. Tengo algo de tarea por terminar, y no sería bueno caer dormido a la mitad del trabajo."

show hanagown normal
with charachange

ha "Entonces… ve."

hi "¿Yo solo?"

"Ella asiente."

hi "Bueno, realmente no estoy contra eso, pero… ¿estás segura? Pasé por acá para invitarte a venir conmigo."

show hanagown distant
with charachange

ha "Estoy bien. Tú puedes ir."

hi "Vamos, solo una pequeña caminata."

ha "Por favor, solo ve. E-estoy bien aquí."

hi "… ¿Hanako?"

"Trato de ver su rostro para medir sus sentimientos, pero su expresión es de piedra. Como si estuviera tan cuidadosamente acomodada, que un simple movimiento podría hacerla colapsar."

hi "Bueno, si quieres quedarte aquí… ¿tal vez podríamos jugar un juego?"

ha "Solo vete. Por favor. No… quiero hacer nada en este momento."

hi "Seguramente hay algo que quieres hacer. Debe ser aburrido, sentarte aquí en tu habitación sola."

ha "Quiero que te vayas."

hi "Vamos, no tienes que ser así. Solo quiero pasar un tiempo contigo. Lilly y yo estamos preocupados, así que…"

show hanagown worry_blush
with charachange

ha "¿Tú… hablaste con ella?"

hi "Eh… sí. Hablamos… por teléfono, apenas hace un rato. Ambos estamos realmente preocupados por ti."

show hanagown irritated
with charachange

"Hanako murmura consigo misma otra vez. Cada vez es más perturbador."

hi "¿Hanako…?"

ha "Te estoy diciendo… por favor, vete. No entiendes nada…"

hi "Si solo tuviéramos una charla, podrías decirme qué es lo que no entiendo…"

ha "Sal… de aquí, p-por favor…"

hi "Solo encerrarte en tu habitación otra vez no va a ayudar en nada, Hanako. Por favor…"

stop music fadeout 2.0

"Silencio."

hi "Hanako, solo quiero ayudarte—{w=0.3}{nw}"

scene ev hanako_rage:
    truecenter
    subpixel True zoom 3.0
    0.25
    linear 0.2 zoom 1.05
    easein 8.0 zoom 1.0
with flash

play music music_rain

"Ella repentinamente salta fuera de su cama, girando hacia mí con una expresión que me toma completamente con la guardia baja."

ha "¡Salte de mi cuarto, salte de mi cuarto, salte de mi cuarto!…" with vpunch

"Hanako me grita con tanta fuerza que, por primera vez en mucho tiempo, me siento genuinamente asustado. Yo… no tengo idea de cómo reaccionar a esto, y que provenga de Hanako entre todas las personas."

ha "¡Fuera! ¡Te lo estoy diciendo, vete!" with vpunch

hi "P-pero… solo estaba tratando de… ayudarte…"

ha "¡Sé que necesito ayuda! ¡Sé que estoy dañada! ¡No necesito que me lo digas!" with vpunch

hi "¡Nunca dije que estuvieras dañada, ni nada como eso!"

ha "¡Está escrito en tu cara, está escrito en la cara de Lilly, está escrito en la cara de todos!" with vpunch

ha "¡Veo a un terapeuta cada semana, Lilly me mima como si fuera su hija, y ahora… incluso tú!" with vpunch

ha "¡Nada ha cambiado, nada en realidad! ¡Odio a Lilly, y… te odio a ti más que a nadie!…" with vpunch

"Su rostro se mueve extraño, casi en formas grotescas."

"Nunca había visto a nadie salirse completamente de control antes, pero pareciera como que la usualmente tranquila y retraída chica frente a mí está yendo a tal ciclo destructivo frente a mis ojos."

"No sé qué hacer. No tengo idea de lo que debo decir o hacer."

ha "¡Vete! ¡Déjame sola! ¡Salte de aquí!" with vpunch

"Doy un paso atrás, luego otro, y luego otro. Mi retirada solo es detenida cuando siento la puerta tras mi espalda."

"No puedo arreglar esta situación. Ahora nada de lo que diga cambiaría nada. Siento como que estoy en un extraño y profundamente perturbador mundo extraño. No quiero estar aquí más tiempo."

"La manija de la puerta pelea contra mis torpes intentos de abrir la puerta sin darle la espalda a Hanako. Eventualmente, por suerte, la manija se mueve hacia abajo. Abro la puerta tan rápido como puedo y casi salto hacia atrás a través de ella."

"Mientras salgo, mantengo mis ojos en la chica frente a mí."

"Ella no está dañada. Hanako no está dañada. Si estuviera dañada, entonces yo estoy tan dañado como ella después de todo lo que me ha pasado. Lilly solo hizo siempre lo mejor por ella, y yo solamente traté siempre de protegerla lo mejor que pude."

scene ev hanako_rage_sad:
    zoom 1.0
with charachange

"Hanako mira hacia abajo, toda su energía agotada. Ahora que he salido de su habitación, lo peor de su furia se ha ido."

"Pero incluso ahora, no puedo atreverme a discutir con ella. No solo es la profunda impresión de lo que dijo… Se siente como que algo más me está deteniendo. Algo profundo, que me hace sentir físicamente enfermo."

show bg school_dormhanako_ni:
    center
    xpos 0.55
    linear 5.0 center
show hanako_door_door:
    left
    xpos -0.2
    linear 5.0 left
show hanako_door_base:
    right
    xpos 1.1
    linear 5.0 right
with flash

stop music fadeout 4.0

"Sin decir palabra, lentamente cierro la puerta. El crujido de las viejas bisagras suena casi ensordecedor."

play sound sfx_doorclose

show bg school_dormhanako_ni at center
show hanako_door_door at left
show hanako_door_base at right
with ease
"Con un golpe seco al final, la puerta de madera se cierra. La Hanako que sentí que conocía desaparece tras ella, y solo débiles fisuras de luz naranja se asoman alrededor de las orillas."

scene bg school_girlsdormhall
with locationchange

"Me siento entumecido. Sin nada más que hacer, comienzo a caminar de vuelta a mi habitación, mecánicamente colocando un pie delante del otro mientras apenas noto las cosas a mi alrededor."

"Mi mente se mantiene avanzando, cuestionando todo lo que pensé que sabía sobre Hanako."

"Pero una cosa no es cuestionada; que al cerrar esa puerta llevó a una conclusión algo más que una simple visita."



label es_H24:



scene bg school_girlsdormhall
with locationchange

play music music_night fadein 4.0

"Después de hablar con Lilly al final del día escolar, me siento en mi escritorio y veo hacia afuera por la ventana, y observo ociosamente a los estudiantes dejar el edificio escolar."
"Usualmente se van en grupos, pero incluso cuando se van solos, se despiden de sus amigos primero."

"Es completamente normal. Algo que habría pasado por alto completamente si hubiera sido otro día, porque es bastante mundano."

"Pero es también algo que Hanako nunca ha hecho en el tiempo que la he conocido. Mientras estoy de pie frente a la puerta de Hanako por segunda vez como dos días, ese hecho no deja mi mente."

"Sostengo dos platos en mis manos. En cada uno están… no exactamente los platillos más rebosantes, pero quiero asegurarme de que Hanako está al menos alimentándose."
"Podría ser también una forma de ganar un poco de influencia para que me deje entrar."

"Lilly y yo hemos dado lo mejor para estar ahí para ella. Desde que tuvo ese ataque en clase, he querido proteger a Hanako muchísimo. Que una cosa así le pase otra vez, o algo incluso peor, es algo en lo que no quiero pensar."

scene bg school_dormhanako_ni
show hanagown distant_close:
    center
    xpos 0.39
show hanako_door_base at right
show hanako_door_door at left
with locationchange

play sound sfx_doorknock2

"La puerta da una pequeña serie de sonidos sordos mientras golpeo en ella a la vez que apoyo cuidadosamente un plato en mi otro brazo. Dudo que Hanako vaya a abrir por mí, así que todo lo que en realidad puedo esperar lograr es atraer su atención."

hi "Buenas noches, Hanako. Solo soy yo."

"Me detengo por un momento para ver si ella responderá, pero el hecho de que no lo hace no es de sorprender."

hi "Yo… tengo un poco de comida para los dos. ¿Puedo entrar?"

"Durante lo que se siente un largo tiempo, algunas voces apagadas del piso de abajo son el único sonido que se escucha."

play sound sfx_lock

"Entonces puedo oír el sonido de pies descalzos viniendo hacia la puerta y tengo que reprimir un suspiro de alivio mientras escucho el seguro de la puerta siendo retirado."

play sound sfx_dooropen

show hanako_door_door:
    xpos -0.1
with charamove

"Cuando Hanako abre la puerta, la miro atentamente."

show hanagown normal_close
with charachange

"Ella mira hacia arriba momentáneamente al plato en mi mano izquierda. Es un modesto curry que hice rápidamente de un paquete."

show hanagown distant_close
with charachange

"Sus ojos se mueven al plato en mi mano derecha, el cual contiene la misma cosa, antes de mirar hacia abajo otra vez."

hide hanagown
with charaexit

"Mientras ella arrastra sus pies de regreso a su habitación, me doy cuenta de que no le he dicho ni una palabra. La sigo con aire sombrío, ligeramente apenado de haber estado tan envuelto en observarla."

play sound sfx_door_creak

show hanako_door_door:
    easeout 1.0 xpos -0.2
show hanako_door_base:
    easeout 1.0 xpos 1.1
show bg school_dormhanako_ni:
    center
    easeout 1.0 xpos 0.55
with None

scene bg school_dormhanako
with silentwhiteout

"Más que nunca, la atmósfera gris y austera de la habitación de Hanako se siente como un reflejo de su personalidad. Las voces de afuera se vuelven completamente inaudibles, y el silencio dentro opresivo, una vez que cierro la puerta."

"Caminando al otro extremo de la habitación, coloco los dos platos en su escritorio. Estoy agradecido de que me dejó entrar, pero cuando volteo a ver su rostro, no puedo evitar tener dudas sobre el haber venido a verla."

show hanagown distant:
    center
    ypos 1.15
with charaenter

"En todo caso no creo que Lilly estuviera bien. Viendo a Hanako así, en lo único en lo que puedo pensar es que darle espacio es la última cosa que debería hacerse. No quiero imaginarlo, pero ella podría hacer algo tonto."

hi "Em… solo es comida instantánea, pero debería ser llenadora."

"Tomo un plato con mi mano, ofreciéndoselo. Sin decir palabra ella lo acepta y se sienta en la orilla de su cama."
"Yo tomo asiento en su silla, y el familiar sonido de personas alimentándose tintinea en la habitación mientras comemos con los tenedores que estaban clavados en el arroz."

"El curry no sabe… mal. No esperaría mucho más de un paquete cuya marca no reconocí, así que el que no sea horrible es al menos algo."

"El estar comiendo mitiga el hecho de que ella no está hablando. A ninguno de los dos nos gusta hablar mientras comemos, y esto me recuerda a los almuerzos que tan seguido pasamos juntos."

hi "Es algo agradable, comer juntos de esta forma."

show hanagown worry
with charachange

"Hanako me mira con aire de duda. Al menos es una mejor expresión que la que ha llevado hasta ahora."

hi "Nos hicimos amigos más que nada compartiendo los recesos del almuerzo, así que es agradable regresar un poco a esos momentos."

"Ella duda por un par de segundos, y me encuentro haciendo una mueca. ¿Dije algo malo?"

show hanagown smile
with charachange

"Eventualmente ella sonríe y asiente. Normalmente estaría animado por esto, pero su sonrisa luce extraña. No puedo realmente encontrar la razón de ello."

ha "Todo es… igual que antes, ¿no?"

hi "S-sí. Desde luego que lo es."

hi "Aún nos tienes a Lilly y a mí para ayudarte y protegerte, y una vez que ella vuelva, todo será como si nunca se hubiera ido."

show hanagown distant
with charachange

"Hanako asiente otra vez, su expresión permaneciendo exactamente igual que antes. Se siente como una Hanako diferente de la que vi al inicio cuando entré en la habitación, y es ligeramente desconcertante."

"Ambos volvemos a nuestra cena después del pequeño comentario. A pesar de que Hanako luce más feliz que antes, mis ojos se mantienen saltando hacia ella como para asegurarme de ese hecho."

"No pasa mucho antes de que lo último del curry de Hanako sea terminado. Termino lo último del mío mientras ella coloca el plato vacío en el escritorio, y coloco mi plato y tenedor usados encima del de ella."

"Brevemente me pregunto qué debería decir, queriendo desesperadamente evitar otro silencio incómodo o la posibilidad de dejar su cuarto después de tan corto tiempo, pero Hanako es la que habla primero."

show hanagown worry_blush
with charachange

ha "Me… me preguntaba… dado que e-estás aquí…"

"Ella rápidamente va a uno de sus cajones, y después de rebuscar muy poco, saca su tablero de ajedrez."

show hanagown smile
with charachange

ha "¿T-te… gustaría jugar…?"

"Esta vez, no puedo reprimir el suspiro de alivio que escapa de mis labios."

hide hanagown
with charaexit

show bg school_dormhanako at left
with charamove_slow

"Asiento apresuradamente, y Hanako inmediatamente se ocupa de acomodar mientras salgo de la silla y tomo asiento en su cama."

"Una vez más, Hanako está dispuesta a dejarme entrar a su mundo, con un gesto tan simple como compartir un juego entre nosotros. Supongo que solo me estaba devanando por nada."

show hanagown smile_close:
    center
    xpos 0.55
    easein 1.0 center
with Dissolve(1.0)

"Después de que el tablero es colocado en la cama entre nosotros, terminamos de acomodar nuestras respectivas piezas."

"A través de nuestra amistad, nunca hemos intercambiado tantas palabras. Sin embargo, cuando estamos así, veo que en realidad probablemente nunca hemos necesitado hacerlo."
"Solo un simple libro, o juego de mesa, o comida entre nosotros es suficiente para superar esa distancia."

"Hago el primer movimiento, tal como siempre lo he hecho. Esta es la forma en que nuestra amistad se formó, y es la forma en la que probablemente siempre será."

"Sin embargo, algo se siente definitivamente diferente en ella, y no puedo realmente captar lo que es. Veo a Hanako atentamente, pero no puedo descifrar nada de su expresión."

"Tan cerca como podamos estar físicamente, se siente como si estuviéramos más alejados que nunca. Sin embargo, Hanako es una persona frágil, y no querría lastimarla nunca."

"Esa es la forma en que las cosas siempre fueron entre nosotros, y la forma en que probablemente siempre serán."

stop music fadeout 2.0






label es_H25:



scene bg school_scienceroom at bgright
with locationchange

"Desde que hablé con Lilly ayer, he querido intentar librarme de la indiferencia que he sentido desde que vine a Yamaku."

"Pero incluso si trato de concentrarme en el libro frente a mí, el lugar vacío de Hanako en la parte de atrás del salón se cierne más alto que una montaña."

"Cada vez que comienzo a concentrarme, mis ojos saltan hacia su banco y otra vez mi mente comienza a girar."

show miki smile at center
with charaenter

"Una vez más mis ojos vagan hacia él, pero esta vez mi visión es bloqueada por otra cierta estudiante."

hi "Oh, qué tal Miki."

show miki grinclosed
with charachange

mk "Tal vez solamente deberías almorzar. Puedo escuchar tu estómago rugiendo desde mi banco."

play music music_happiness

"Dejo caer mi cabeza decepcionado. Ella parece divertirse con mi reacción, y sube a mi banco. Su sonrisa mientras se sienta en él me recuerda al Gato de Cheshire."

show miki grin_close
with characlose

mk "Así que, ¿en qué estás trabajando?"

hi "Algo de Matemáticas. Tengo un manejo decente de ellas, pero quería solo repasar."

show miki whistle_close
with charachange

mk "Oh ¿en serio? Déjame ver eso."

"Antes de poder objetar, ella agarra mi libro de Matemáticas con su mano. Ella escanea la página en la que estaba, sosteniéndolo abierto con la única mano que tiene, su brazo izquierdo descansando inútilmente en su regazo."

"En mi tiempo aquí en Yamaku, he notado que los otros estudiantes tienen un amplio margen de ajuste a sus discapacidades, en un nivel puramente práctico. Miki es una de aquellas que parecen tener algunos problemas."

"El muñón en su brazo izquierdo tiende a estar ya sea colgando a su lado, metido en su bolsillo, o de otra forma fuera de su camino. Algunas veces tiene dificultades haciendo tareas comunes, lo que la vuelve visiblemente frustrada."

"Me siento un poco mal por pensar de esta forma, pero estoy agradecido de que Hanako y yo no tenemos discapacidades que afecten nuestra libertad de movimiento a ese extremo."

"Por otro lado… si el problema de Miki se agravara, al menos no estaría en posibilidades real de morir."

show miki smile_close
with charachange

"Mi atención se reenfoca mientras ella pasa a través de algunas páginas, viendo superficialmente sus contenidos. Con interés tan casual en el tema en cuestión, es claro que ella no va a ser de mucha ayuda."

hi "¿Supongo que no estás muy interesada en estas cosas?"

show miki angry_close
with charachange

mk "Que se jodan las Matemáticas. Son aburridas a morir."

"Ella pone el libro de vuelta frente a mí con indiferencia. Sus ojos se mueven a la libreta junto a él en la que he estado haciendo ecuaciones de práctica."

show miki confused_close
with charachange

mk "Espera, ¿en verdad eres capaz de hacer esas cosas?"

hi "Sí."

show miki wink_close
with charachange

mk "Guau. Nunca antes he hablado con una computadora con patas."

hi "Gracias… creo. Al menos me está yendo mejor en esto que en Historia."

show miki grin_close
with charachange

mk "¿No crees que vale la pena pedirle ayuda a esa bibliotecaria? Escuché que está tirándole a la uni."

hi "Ah, ¿Yuuko? Tal vez. Pero no sé qué es lo que quiere estudiar."

hi "¿Y qué hay de ti? ¿Tienes algo que has pensado hacer después de graduarte?"

show miki grinclosed_close
with charachange

mk "¿Yo? Nah, no realmente. Solo lo disfruto mientras dure."

"Ella parece un poco incómoda cuando se le pregunta acerca de su futuro, y distraídamente frota su antebrazo izquierdo. Como que quiero preguntarle sobre ello, pero creo que no la conozco lo suficiente para hacerlo."

show miki serious_close
with charachange

"La conversación decae, y me recargo en mi silla, dando por perdida la posibilidad de estudiar. Miki nota mi expresión cansada y se ve extrañamente seria."

mk "¿Pensando en Hanako?"

hi "¿Es tan obvio?"

show miki wink_close
with charachange

mk "Has estado viendo a su asiento, y has estado muy quieto. No es difícil atar los cabos."

hi "Solo estoy preocupado por ella."

show miki serious_close
with charachange

mk "Sí, puedo ver por qué lo estarías. Ella puede ponerse… extraña, algunas veces."

"Ella suena desconcertada, pero no puedo culparla."

"Hanako era una persona con la cual era difícil interactuar antes de que se relacionara conmigo, incluso con Lilly cerca para ayudar. No la he conocido por tanto tiempo tampoco, así que algunos de sus hábitos podrían ser desconocidos para mí."

"Mi rostro se torna preocupado. Si no hubiera desarrollado sentimientos hacia ella, lidiar con esto sería al menos un poco más fácil."

show miki whistle_close
with charachange

mk "Ah, quiero decir, sin ofender. No es una mala persona, eso lo sé."


label es_H25a:

hi "Lo sé, no lo tomé de esa forma. Solo es más difícil de tratar cuando, bueno, tú sabes. Sientes algo por alguien."

show miki serious_close
with charachange

mk "Sí, puedo imaginarlo. Es difícil olvidar algo como lo que pasó en clase, también."

"Desearía que no me hubiera recordado eso. Acaba de confirmar que fue claramente visible para los otros en el lugar también."


label es_H25c:

show miki smile_close
with charachange

mk "Vamos, no dejes que te deprima. Ella ha hecho esto antes, solo tienes que esperar a que pase."

"Se encierra en su habitación y actúa como una cáscara vacía de persona por una gran cantidad de tiempo, desde que entró a Yamaku si no es que desde antes también, ¿y se supone que no me preocupe por eso?"

"Bueno, puede que piense eso, pero no hay nada que pueda hacer. No puedo forzarla a salir, y ella ve a un terapeuta, así que no es como si no estuviera recibiendo ayuda por sus problemas."

"Tal vez es natural pensar de esa forma cuando te encuentras tan impotente para ayudar a alguien. “Esa su forma de ser y solo tienes que lidiar con ello”."

show bg school_scienceroom at center
show miki smile_close at twoleft
with charamove

stop music fadeout 3.0

"Mientras reflexiono sobre las cosas, noto movimiento por el rabillo del ojo. Volteo a ver quién es, y termino teniendo que mirar de nuevo."

show hanako invis:
    right
    xpos 1.1
with None

show hanako basic_normal at right
with dissolvecharamove

"No hay duda, es Hanako. Ella camina a través de la puerta justo como lo haría cualquier otro día de escuela normal, y comienza a avanzar hacia su asiento en su usual forma silenciosa y humilde."

show hanako emb_downtimid
with charachange

"Ella me ve por un momento antes de sonrojarse y voltear a otro lado apenada, lo que me hace darme cuenta de que me le había quedado viendo. Lamento eso, pero no hacerlo es difícil después de todo lo que ha sucedido."

hide hanako
with charaexit

play music music_another fadein 4.0

show bg school_scienceroom at bgright
show miki grinclosed_close at center
with dissolvecharamove

"La chica sentada en mi banco me mira, sonriendo."

show miki grin_close
with charachange

mk "¿Ves? Tu novia está de vuelta. ¿Qué te dije?"

hi "Calmada."

"Puede que lo haya dicho como broma, pero me golpeó lo suficientemente cerca para hacerme sentir incómodo."

show miki smile
with charadistant

"Mientras hablamos, alguien dice el nombre de Miki desde la puerta. Ella salta de su posición estratégica en mi banco antes de girar hacia mí."

show miki grin
with charachange

mk "Me tengo que ir, Hisao. Recuerda comer alguna vez, ¿lo harás?"

hi "Bien, lo haré. Nos vemos."

hide miki
with charaexit

"Ella da un casual saludo antes de trotar hacia la puerta, donde un estudiante varón en uniforme de gimnasio está esperándola. Probablemente alguien del club de atletismo."

show bg school_scienceroom at right
with charamove_slow

"Aprovechando la oportunidad, me levanto y me dirijo hacia el banco de Hanako."

show hanako emb_timid:
    center
    ypos 1.15
with charaenter

ha "Ho-hola…"

hi "Hola, Hanako. ¿Qué hay?"

show hanako emb_downtimid
with charachange

ha "N-nada…"

"Tal vez hablar con ella tan pronto luego de volver a clase fue un mal movimiento."

hi "¿Quieres venir conmigo por algo de la cafetería? Estoy bastante hambriento."

show hanako cover_worry
with charachange

ha "Pero… pensé que estabas estudiando."

"El estudio puede esperar. Presentarse a clase después de todo este tiempo debe haber pedido algo de coraje a Hanako, así que lo menos que puedo hacer es estar con ella."

"“Esa es su forma de ser y solo tienes que lidiar con ello” es la forma en que Miki y probablemente el grupo entero ve a Hanako. Sin embargo puedo hacer más por ella. Quiero hacer más por ella."

hi "Después de ser distraído por Miki, no creo que vaya a lograr hacer nada. Vente, vamos."

show hanako basic_bashful at center
with dissolvecharamove

"Ella duda, pero eventualmente se levanta y se me acerca mientras comenzamos a caminar. Estos podrán ser pequeños pasos para ella, pero el hecho de que finalmente está fuera de su habitación por su propia voluntad saca un gran peso de mis hombros."

stop music fadeout 2.0

scene black
with dissolve



label es_H26:

scene bg suburb_shanghaiint at bgright
with locationchange

play music music_dreamy fadein 2.0

"Mi pluma garabatea afanosamente en una hoja de mi cuaderno que lentamente se va llenando. Mi otra mano permanece en la página de un libro de consulta que tomé de la biblioteca, marcando el lugar en el que voy mientras mis ojos saltan de uno a otro."

"Mientras trabajo, ocasionalmente hago círculos rojos o subrayados en las hojas fotocopiadas de papel que yacen en la mesa frente a mí."

"Deseando un cambio de escenario de la biblioteca y evitar las distracciones del salón de clases, decidí hacer uso del Shanghái para algún tiempo de estudio tranquilo."

"Tal como esperaba terminó siendo un agradable y tranquilo lugar, y poder tomar un café mientras estudio es un buen extra."

"Puede que Hanako haya vuelto a su ser normal desde que salió de su habitación, pero yo he hecho más bien lo opuesto. La rutina diaria puede que haya regresado a nosotros, pero me siento como si fuera una persona diferente."

"Tal vez no lo soy. Solo han pasado unos pocos días, después de todo, desde que decidí que quería tratar de salir de la rutina en la que me había metido después de mi accidente."

"Pero quiero cambiar, y ahora estoy trabajando activamente en dirección a ese objetivo."

"O al menos, quisiera pensar que lo estoy haciendo."

hi "Ugh, esto es imposible. Intentar esto por la fuerza bruta no va a funcionar."

"Y además, tengo otra cosa que debo escribir después de esto. Temo que eso no va a ser más fácil."

yu "Em…"

"Miro hacia arriba con ligera sorpresa a la fuente de la indecisa voz."

show yuukoshang worried_up at center
with charaenter

"Yuuko está de pie a la cabecera de la mesa con una toalla húmeda en su mano, claramente aprovechando la oportunidad de limpiar las mesas mientras no hay otros clientes en el lugar. Parece curiosa, sus ojos tanto en mi trabajo como en mí."

hi "¿Qué pasa?"

show yuukoshang worried_down
with charachange

yu "Solo me estaba preguntando… ¿con qué tipo de trabajo es con el que estás teniendo tantos problemas?"

hi "Oh. Solo es Historia. Estoy bien con Ciencias y Matemáticas, así que estoy tratando de llevar mis otras materias a la par."

show yuukoshang happy_up
with charachange

"Yuuko luce positivamente deleitada ante esta situación. Siento como si acabara de elegir la respuesta correcta en algún gran show de preguntas y respuestas."

show yuukoshang closedhappy_down
with charachange

yu "¡Oh! ¡Creo que puedo ayudarte con eso!"

show yuukoshang worried_down
with charachange

yu "Em, si no te molesta… desde luego…"

"Considero brevemente declinar su oferta para no causarle muchos problemas, pero ella luce demasiado emocionada por esto como para que yo lo haga. Sería ruin echarla a tierra de esa forma, después de tal reacción."

hi "Si quieres ayudar, realmente lo apreciaría."

show yuukoshang closedhappy_up
with charachange

hide yuukoshang
with charaexit

"Ella aplaude y rápidamente deposita su toalla en el mostrador, antes de regresar y tomar asiento frente a mí."

show yuukoshang invis at center
with None

show yuukoshang smile_down at Position(ypos=1.15)
with dissolvecharamove

"Tomo un cuaderno de encima del libro de texto y se lo doy para que lo examine."

show yuukoshang neutral_up
with charachange

yu "¿Así que estás estudiando el periodo Edo?"

hi "Sí. Pero no soy muy bueno en esto."

show yuukoshang worried_up
with charachange

"Ella toma el libro de texto y lee unas pocas páginas de una sección aleatoria cerca de la mitad por un rato, pero el aura de entusiasmo que había estado radiando previamente está debilitándose con rapidez."

hi "¿Supongo que esta no era el tipo de Historia que estabas esperando?"

show yuukoshang worried_down
with charachange

yu "Desafortunadamente no. Mi área principal es Historia Europea, especialmente la era clásica. Lo lamento."

"Parece un poco abatida, pero mientras cuidadosamente cierra el libro y lo deja en la mesa, su rostro se anima otra vez."

show yuukoshang smile_down
with charachange

yu "¿Gustas otra taza de café?"

hi "¿Hmm? Oh, sí, seguro."

show yuukoshang invis at center
with dissolvecharamove

"Me inclino hacia adelante y agarro mi libro otra vez mientras Yuuko se levanta, toma mi taza, y lentamente camina hacia el mostrador para preparar otro café."

"Como es usual, ella es absolutamente silenciosa mientras hace eso; cada pizca de su concentración está enfocada en no tropezar o tirar la taza completamente blanca."

"Tomo la oportunidad para echarme hacia atrás y relajarme un poco, mientras el murmullo de la máquina de café está llenando el, de otra forma, silencioso ambiente."

"Son pequeños detalles como ese los que me hacen darme cuenta de lo mucho que he llegado a apreciar las pequeñas cosas de la vida."

"La paz y la tranquilidad del pueblo local, la disciplina y el orden de Yamaku, el verde de los árboles que eran tan raros en mi ciudad natal, el relajado ritmo al cual los residentes de edad viven sus vidas…"

"Todo se siente tan… seguro. Es reconfortante."

"Puedo sentir que estoy comenzando a quedarme dormido, cuando el sonido de la taza viniendo a descansar en la mesa atrae mi atención. Parece que arribó en el momento justo."

show yuukoshang neutral_down at Position(ypos=1.15)
with dissolvecharamove

"Yuuko toma su asiento previo una vez más mientras me acomodo y llevo una mano alrededor de la taza para revisar su temperatura. Está un poco caliente para tomarlo justo ahora, así que le soplo un poco."

show yuukoshang worried_down
with charachange

yu "Es una pena que no te guste tanto la Historia. Más o menos adiviné que estarías más metido en la ciencia."

hi "¿Cómo es eso?"

show yuukoshang smile_up
with charachange

yu "Ya leíste casi por completo la sección de ciencia ficción de la biblioteca. No era difícil de notar."

hi "Tienes un buen punto ahí. Bueno, ¿qué puedo decir? Me has encasillado bastante bien."

show yuukoshang neutral_down
with charachange

hi "Pero suena como que realmente te interesas en la Historia, especialmente considerando lo específica que fuiste sobre ella. ¿Estudias en esa área o algo? ¿Vas a excavaciones cruzando el océano?"

show yuukoshang closedhappy_up
with charachange

"Ella ríe nerviosamente a la idea."

show yuukoshang neurotic_down
with charachange

yu "Me gustaría visitar el mediterráneo alguna vez y ver la vieja arquitectura y el arte por mí misma, pero no creo que podría confiar mis manos a cosas tan delicadas."

show yuukoshang neutral_down
with charachange

yu "Estoy ahorrando para estudiarlo formalmente en la universidad, aunque también leo sobre ello siempre que tengo tiempo libre fuera del trabajo."

"Así que Miki estaba en lo cierto sobre sus aspiraciones universitarias. Considerando cómo le va como mesera, un camino más teórico le sentaría mejor. Sin embargo, es agradable escuchar que tiene ambiciones, considerando lo duro que trabaja."

"Asiento y le doy cuidadosamente un sorbo a mi café. Para este momento ya se ha enfriado a la temperatura correcta, así que comienzo a tomarlo mientras le echo un ojo al libro debajo, tratando de leer al mismo tiempo."

"Unos pocos minutos pasan tranquilamente, Yuuko mirando afuera de la ventana viendo al mundo avanzar mientras tomo mi café y estudio."

show yuukoshang closedhappy_up
with charachange

"Un movimiento atrapa mi atención, y miro hacia arriba para ver a Yuuko sonriendo y agitando la mano a alguien afuera. Seguir su mirada sorpresivamente me revela que ese alguien es Hanako."

"Nos está mirando desde el lado de la calle contrario a donde estamos. Su timidez usualmente por completo visible está en su mayoría ausente, probablemente gracias a que hay poca gente alrededor ahora mismo."

"Evidentemente decide unírsenos, pues después de un pequeño saludo con la mano, ella da un vistazo rápido hacia ambos lados de la calle y cruza hacia el lado en el que el café está ubicado."

$ renpy.music.set_volume(0.3, 0.0, channel="sound")
play sound sfx_storebell

show hanako invis:
    right
    xpos 1.0
with None

show yuukoshang happy_up:
    twoleft
    ypos 1.15
show bg suburb_shanghaiint at center
show hanako basic_normal at tworight
with dissolvecharamove

"La familiar campanilla del Shanghái suena mientras Hanako entra y se abre camino hacia la mesa donde estamos sentados."

show hanako cover_distant at Position(ypos=1.15)
with dissolvecharamove

ha "Ho-hola…"

show yuukoshang smile_down
with charachange

yu "Buenas tardes."

hi "Hola, Hanako. ¿Qué pasa?"

show hanako emb_smile
with charachange

ha "N-nada… solo… s-salí de paseo… porque el clima era lindo."

hi "Sí, entiendo lo que quieres decir. Estoy feliz de que decidí estudiar aquí en lugar de la biblioteca."

"Es agradable aquí gracias a eso, mejor que la algunas veces sofocante biblioteca. Veo a Yuuko, quien asiente como respuesta."

show yuukoshang neutral_down
with charachange

yu "Es lindo. Solo es una pena que el verano no puede durar para siempre."

show yuukoshang neurotic_up
with charachange

yu "Oh espera, perdón, ¿gustas algo de beber?"

show hanako basic_smile
with charachange

show yuukoshang neutral_down
with charachange

"Hanako sacude su cabeza. Por suerte, es suficiente para tranquilizar a Yuuko."

show hanako basic_bashful
with charachange

ha "¿C-cómo vas con el estudio?"

hi "Bien… o algo así."

hi "Oh cierto, ¿has hablado con Lilly?"

show yuukoshang smile_up
with charachange

yu "También me interesa; ¿cómo le está yendo?"

show hanako cover_worry
with charachange

ha "E-está disfrutándolo… creo."

"Creo… que eso es todo lo que sabremos por ella. Estar cerca de Yuuko la está poniendo tensa."

show yuukoshang closedhappy_down
with charachange

yu "Ah, sería tan lindo viajar a Escocia."

show yuukoshang happy_down
with charachange

yu "Campos verdes, castillos, preciosos pueblos pequeños, hombres en falda escocesa, historia interesante…"

"No puedo decir que veo el atractivo de los hombres en falda escocesa. Pero sí parece un lugar pintoresco."

play sound sfx_storebell

show hanako defarms_shock
show yuukoshang panic_up
with vpunch

"Mientras hablamos, el repique de la campanilla de la puerta suena otra vez. Hanako se sobresalta, notando la expresión de pánico de Yuuko por la posibilidad de tener que dejar a los clientes esperar unos segundos, debido a su plática con nosotros."

show yuukoshang worried_down at twoleft
with Dissolvemove(0.3)

with Pause(0.2)

hide yuukoshang
with charaexit

"Yuuko nos da una reverencia rápida, luego sale volando apurada a saludar a los nuevos clientes, un hombre anciano y su esposa. La observo por un rato, estirando mi cabeza para tener una mejor vista."

show hanako def_worry
with charachange

"Hanako me está mirando con su único ojo visible."

show hanako def_worry:
    center
    ypos 1.15
show bg suburb_shanghaiint at bgleft
with charamove

show hanako emb_downtimid
with charachange

"Ella desvía su cabeza apenada cuando giro para hacer contacto visual con ella."

hi "Solo estaba pensando que es bueno tener ambiciones para el futuro. Yuuko me estaba diciendo antes un poco sobre sus aspiraciones universitarias."

show hanako emb_timid
with charachange

ha "Oh."

hi "Es una pena. Si ella no fuera tan neurótica y con exceso de trabajo, pienso que podría ser una persona realmente feliz."

"Por mucho que quisiera hacer de anfitrión con Hanako y entretenerla un poco, sí necesito estudiar también. Para ser honesto, no creo que la distracción de Yuuko haya ayudado tampoco."

hi "Perdón si estoy un poco distraído. Necesito tratar de terminar esto, de otra forma voy a reprobar los exámenes de Historia bastante mal."

"Soy dejado mientras paso la mano por mi cabello con frustración. Esa carta también necesita hacerse, una vez que regrese a mi habitación del dormitorio."

hi "Espero tener más suerte con eso que con esto. Maldición."

show hanako emb_downtimid
with charachange

ha "¿C-con qué?"

hi "Oh, eh… iba a… escribir a Iwanako. Pero justo ahora, esto es más importante."

"Todo lo que he hecho es exaltarme. No puedo enfocarme en el trabajo frente a mí cuando mi estómago está lentamente revolviéndose con la posibilidad de realmente intentar escribirle, después de todo este tiempo."

"Me fuerzo a concentrarme en el libro, agarrando mi pluma una vez que doy un rápido sorbo a mi café."

show hanako basic_distant
with charachange

"Después de unos pocos segundos, Hanako se detiene mirándome silenciosamente y se reclina en su asiento, relajándose tanto como parece ser posible para ella hacerlo, mirando por la ventana el pasar del tiempo."

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
stop music fadeout 3.0

"Permanecemos de esta forma por un largo rato antes de regresar a nuestros dormitorios juntos. Estoy sorprendido de que tuvo la paciencia de esperarme."

scene ev hisao_letter_open
with shorttimeskip

play music music_night fadein 1.0

"La carta de Iwanako yace en mi escritorio junto a una hoja blanca de raya y un sobre sin usar. El golpeteo de mi pluma es lo único que puede escucharse a esta hora de la noche."

"Como temía, mi segunda tarea del día resulta ser tan difícil como la primera, si no es que más."

"Han sido tantos meses desde que nos vimos. Aun así, todavía puedo recordar cómo lucía, cómo se escuchaba, y cómo actuaba. Pero para estos momentos, los pequeños detalles están comenzando a desvanecerse."

"Cuando vi su carta por primera vez, apenas reconocí su letra. Incluso había olvidado la pluma rosa que siempre usó hasta que su escritura me lo recordó."

"Me pregunto por qué no la usó para su carta; solía escribir todo con ella. Tal vez ahora piensa que es demasiado inmaduro."

"Debería estar pensando en mí mismo, y en qué es lo que quiero comunicarle. Sin embargo, mi mente no puede dejar de concentrarse en ella. En el pasado que compartimos antes de que nos fuera arrebatado tan repentinamente."

"Las decoraciones brillantes y ligeramente chillonas van con su sentido de estética. Tomando la carta para darle un vistazo más de cerca, doy un largo suspiro."

"Este es el último enlace vinculándome al pasado. Iwanako no cesó de existir repentinamente cuando dejó la habitación del hospital por última vez, pero necesitaba esta carta para recordarme aquello."

"Tenía todos estos sentimientos cuidadosamente archivados. Sentí como si no los necesitara, que podría simplemente comenzar la vida desde cero. Era más fácil de esa forma."

"Al final, supongo que fue una idea algo ingenua. Tarde o temprano, mi pasado me habría alcanzado de una forma u otra."

"¿Pero qué se supone que le diga? ¿“Gracias por terminar conmigo”? Todo lo que hizo la carta fue acabar con la sensación de conclusión que desde antes sentí."

"Por más que lo intento, no puedo escribir ni una simple palabra en el papel frente a mí. No puedo pensar ni siquiera en exactamente qué es lo que quiero decir."

stop music fadeout 4.0

scene bg school_dormhisao_ss
with locationchange

"Colocando la carta encima de la hoja en blanco, recojo los materiales y los guardo en mi cajón."

"El sonido metálico que mi escritorio hace al cerrar hace que me tense momentáneamente en frustración, antes de levantarme para ir por una bebida de la máquina expendedora en el primer piso."

scene bg school_dormhallway
with locationchange

"Traté pero no pude hacerlo. Después de todo el tiempo que ha pasado, aún no sé cómo lidiar con Iwanako."

scene black
with dissolve



label es_H27:

scene bg school_library
with locationchange

play music music_happiness

"La biblioteca, aunque no está zumbando por la actividad, está notablemente más ocupada de lo usual."

"Los exámenes no están muy lejos, y esto está reflejado en el número de estudiantes quemándose las pestañas en los libros de texto en las mesas a nuestro alrededor."

"He estado estudiando bastante en los días pasados, tal como ellos, con la esperanza de hacerlo bien en el examen."

"Esto también significa que Hanako y yo hemos estado jugando menos, así que ella ha comenzado a estudiar también solo para rellenar su tiempo."

"Sin embargo, me he encontrado olvidado por ella en este día en particular."

"El libro de texto frente a mí ha permanecido en la misma página por algún tiempo. Después de tanto leer los temas podrían no importarme nada de no ser por los exámenes."

"Mis ojos se encuentran saltando a donde Hanako estaría usualmente, tal como los días que no está en clase. Su usual puf en la esquina de la habitación está manifiestamente desocupado."

"Fue aquí que nos hablamos por primera vez. Traté de comenzar una conversación con ella, ella se puso nerviosa, y eventualmente salió huyendo de la habitación por completo."

"Probablemente no debería sonreír por eso, pero fue algo divertido, en retrospectiva. Hoy en día es más y más difícil imaginarla haciendo algo así. Incluso con Lilly fuera, le ha estado yendo bien ahora que salió de su habitación."

"Quiero hablar con ella, o al menos jugar otro juego de ajedrez. Estoy cansado de estudiar, y han pasado algunos días desde que en realidad hicimos algo juntos."

"La pregunta de dónde encontrar a Hanako no es una particularmente difícil. Si no está en la biblioteca, las posibilidades son que esté en el cuarto de té buscando paz y tranquilidad, o en su habitación del dormitorio."

"Decidiendo revisarlas en ese orden, empaco mis libros y me dirijo fuera de la biblioteca."

stop music fadeout 5.0


scene bg school_girlsdormhall
with shorttimeskip

"Me estiro y doy un largo gemido mientras camino a través del pasillo. Estudiar podría ser frustrante algunas veces, pero con el progreso que siento que he hecho, también hay un sentido de orgullo en hacerlo. Es una buena sensación."

scene bg school_dormhanako_ni
show hanako_door_base at right
show hanako_door_door at left
with locationchange

"No se escucha ningún sonido desde adentro mientras estoy de pie frente a la puerta de la habitación de Hanako. Supongo que eso no es muy indicativo sobre si está dentro o no, dado lo tranquila que es."

"Aun así, no estaba en el cuarto de té. Trato de golpear levemente para dar a conocer mi presencia, pero soy sorprendido cuando encuentro la puerta abierta y cediendo a mi contacto."

play sound sfx_door_creak

show hanako_door_door:
    easeout 1.0 xpos -0.2
show hanako_door_base:
    easeout 1.0 xpos 1.1
show bg school_dormhanako_ni:
    center
    easeout 1.0 xpos 0.55
with None

scene bg school_dormhanako
show hanako basic_distant:
    center
    ypos 1.15
with silentwhiteout

"Con un pequeño crujido, la puerta se abre. Parece que mis sospechas eran correctas; Hanako está aquí."

"Está sentada en la mesa con un libro abierto frente a ella, pero no le presta atención dado que está mirando por la ventana. Parece completamente inconsciente de mi presencia."

"Con su cabeza descansando pensativamente en su mano, luce calmada y sosegada. Es una pena que no pueda lucir de esta forma más seguido."

show hanako basic_distant_close:
    center
    ypos 1.1
with characlose

"Sonriendo un poco, camino a la mesa y suavemente le hablo."

hi "Buenas noches, Hanako."

show hanako basic_normal_close
with charachange

"La cabeza de Hanako gira un poco para verme, pero aún parece estar solo parcialmente. Coloco una mano en la mesa y bajo mi cabeza para ver mejor su rostro, con ligera curiosidad sobre el humor en que se encuentra."

hi "¿Qué pasa?"

show hanako basic_worry_close
with Dissolve(0.2)

"Ella ahoga un pequeño grito, finalmente reconociendo mi presencia en la habitación."

"Hanako está sonrojándose bastante. Su boca está abierta solo un poco, como detenida a mitad de una oración. Pero más llamativo es lo que está haciendo."

scene ev hanako_eye:
    truecenter
    subpixel True zoom 0.9
    acdc_warp 20.0 zoom 1.0
with locationchange

"Está mirándome directamente. Sus ojos están fijos en los míos, desde una distancia tan corta que casi puedo ver mi propio reflejo en ellos. No miran a otro lado, no se mueven del todo. Están completamente inmóviles, solo mirando a los míos."

"Son oscuros, y le dan casi un aire analítico. Incluso cuando lee temas en los que no tiene interés, ella parecería estar absorta en su trabajo para el observador casual. Absorbe información bastante bien, e incluso ahora, puedo sentir eso."

"Siento como que estoy viendo algo que nunca vi antes tras de esos ojos. Pero no sé lo que es."

hi "¿Hanako…?"

"Sus labios se mueven solo un poco, hablando algo silenciosamente. Parece estar a punto de decir algo, pero no lo dice."

"Pero así es como es Hanako siempre. A punto de decir algo, pero sin decirlo nunca. Mientras miro atentamente sus ojos, me doy cuenta de algo."

"Todos tienen sus propios pensamientos, cosas que quieren decir, su propia forma de ver el mundo. Pero no puedo dar con lo que Hanako quiere decir, y no puedo dar con lo que está pensando. Nunca he podido hacerlo."

"Es frustrante. Se siente como que no la conozco en absoluto, a pesar del tiempo que hemos pasado juntos."

ha "Hi… sao…"

scene bg school_dormhanako
show hanako basic_worry_close
with charachange

"Solo es hasta ahora que me encuentro sonrojándome. He estado mirando los ojos de Hanako desde una distancia tan corta sin ningún respeto hacia ella, y ella ha estado mirando los míos sin eludirlos."

show hanako emb_downtimid_close
with charachange

"Rápidamente miro a otro lado cubriendo mi cara con la mano. Hanako hace lo mismo."

"Otro silencio incómodo reina. Odio esto. Al inicio los acepté simplemente como un hecho de la vida cerca de Hanako, pero ahora solo se sienten como la afirmación de lo poco que podemos comunicarnos."

"Un poco de enojo logra surgir entre la completa mezcla de emociones que estoy experimentando justo ahora. Quiero acortar la distancia entre nosotros. Los amigos no tienen que andar de puntillas entre ellos de esta forma."

"Hablo antes de poder razonar sobre lo que voy a decir. Mi cicatriz no es tan mala como la de Hanako, y no puedo de ninguna forma comparar mi vida con la de ella, pero quiero mostrarle que no está sola."

"Hacerlo de una forma tan contundente podría ser la única forma de hacerle ver mi punto."

hi "Hanako… quiero mostrarte algo."

show hanako emb_timid_close
with charachange

"Inspiro profundamente para prepararme. Podría salirme el tiro por la culata, pero siento que hemos llegado a ser lo suficientemente cercanos como para que esto esté bien."

hi "No voy a desnudarme ni hacer nada extraño, solo me quitaré la camisa."

show hanako def_shock_close at center
with dissolvecharamove

"Los ojos de Hanako se abren grandes como platos. Su rostro es una divertida mezcla de curiosidad y nerviosismo mientras se pone de pie. Eso me ayuda a calmar mi propio nerviosismo sobre hacer esto frente a otra persona."

play sound sfx_rustling

"Lentamente, con todo mi cuerpo sintiéndose tenso, desato mi corbata y comienzo a desabrochar los primeros botones. Estoy tratando de bloquear mentalmente a Hanako para hacer esto más fácil, pero no está funcionando realmente."

"Mientras progreso hacia abajo, espero escuchar alguna protesta de su parte. Sin embargo ella permanece en silencio, lo que me hace sentir incluso más extraño."

"Con el último botón desabrochado, tomo un respiro y volteo a verla."

scene ev hisao_scar_large:
    xanchor 0 yanchor 0 xpos -600 ypos -140
with whiteout

play music music_heart fadein 0.5

"La mirada de Hanako está fija en mi cicatriz, como esperaba, y una vez que asiento para decir que está bien, ella se adelanta e indecisamente coloca su mano en la línea vertical que corre hacia abajo por mi pecho."

show ev hisao_scar_large:
    ease 1.0 xpos 0 ypos -290

"La cicatriz en su mano, un patrón de piel dañada a través de su superficie, contrasta con la única y uniforme línea que forma la mía. Su mano no está temblando de ningún modo, a diferencia de lo que pensé."

ha "Esta es…"

hi "La cicatriz de la cirugía que siguió a mi ataque al corazón. Los cirujanos tuvieron que abrir mi pecho para operar mi corazón."

show ev hisao_scar_large:
    ease 1.0 xpos -600 ypos -140

ha "Nunca pensé…"

"Las palabras de Hanako son más calmadas y suaves de lo usual. La suave sensación de sus dedos moviéndose de mi cicatriz a mi pecho me hace dudar un poco antes de seguir."

hi "Eres la primera persona que la ve desde que dejé el hospital."

scene ev hisao_scar:
    truecenter
    zoom 1.05 subpixel True
    easein 8.0 zoom 1.0
with flash

ha "Pero… ¿por qué me estás mostrando esto?"

hi "Quería probarme a mí mismo que podía hacer esto; que podía aceptar mi pasado y continuar. Y quería mostrártelo también."

"Ella asiente. Por su reacción, parece saber lo difícil que esto es para mí. Más que nada, esta cicatriz representa un recordatorio visible de mi condición. Un recordatorio de que ya no soy “normal”."

"Eso es algo que, hasta ahora, he tratado lo más posible de ignorar."

"Mientras los minutos pasan, la mirada de Hanako persiste. Sus ojos lucen menos enfocados en mi cicatriz que antes. La situación se siente un poco diferente de como se sentía antes, y me hace sentir un poco incómodo."

scene bg school_dormhanako
show hanako basic_normal_close at center
with silentwhiteout

"Su mano se retrae, y cierro mi camisa y comienzo a abotonarla. Su rostro sonrojado repentinamente regresa a su típico estado de tensión y timidez al tiempo que voltea a otro lado."

"La habitación está en completo silencio mientras acomodo mi camisa y corbata, sintiéndome desconcertado después de tal inesperado momento de intimidad."

hi "Así que… supongo que no eres la única que tiene cicatrices."

show hanako basic_smile_close
with charachange

"Hanako sonríe con la pequeña broma, por suerte alegrando la atmósfera un poco."

ha "Gracias… Hi-Hisao. Creo… que entiendo."

"Doy un largo suspiro de alivio. Realmente no sabía cómo lo tomaría, pero estoy feliz de que todo parece haber funcionado como esperaba. La sonrisa de Hanako solo me reafirma lo anterior."

"Estoy encontrando el camino que quiero seguir, y lo que Hanako necesita es encontrar el suyo. Es algo con lo que no puedo ayudar, y algo que ella necesita para lograrlo es superar su pasado."

show hanako basic_distant_close
with charachange

"Hanako revisa su reloj. Ya se está haciendo tarde."

show hanako basic_worry_close
with charachange

ha "Hisao… em…"

hi "Sí, mejor me voy. Estaré agradecido de dormir un poco. Ha sido un largo día, después de todo."

hi "Buenas noches, Hanako."

show hanako basic_bashful_close
with charachange

ha "B-buenas noches."

stop music fadeout 3.0

scene bg school_girlsdormhall
with locationchange

"Me dirijo hacia afuera de la habitación y hacia el pasillo, permaneciendo en silencio mientras lo hago. Creo que ambos hemos pasado por algunas emociones el día de hoy."

scene black
with dissolve



label es_H28:

scene bg city_street1
with locationchange

play music music_daily fadein 2.0
$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_traffic fadein 2.0

"El calor del sol de verano martillea en mi frente sudorosa. Limpiarme con un pañuelo no ayuda mucho a hacerme sentir más cómodo."

"Dándome por vencido con la idea de lograr hacer más hoy, me detengo y me recargo contra una de las cercas de seguridad, descansando mi mochila en el piso."

"Las tiendas en el pueblo bajo Yamaku están bien surtidas y ofrecen suficiente variedad para arreglármelas, pero un viaje de compras al menos ocasional a la ciudad es algo que realmente no puede evitarse."

"Ya he estado aquí algunas veces. La disposición de la ciudad está haciéndose más familiar, y la nostalgia de su atmósfera está comenzando a borrarse."

"Me doy cuenta de que estoy comenzando a jadear. Sueno como un hombre viejo que se ha esforzado de más, y tener que conectarme con el hecho de que soy la fuente es un poco perturbador."

"Coloco una mano en mi pecho y me concentro por un rato para asegurarme de que no he ido lo bastante lejos como para causar más problemas."

"Afortunadamente, mi corazón está actuando de forma normal. No hay dolor débil, y el ritmo es regular, aunque un poco acelerado, mientras me recupero de hacer cosas de más con este tipo de calor."

"Odio mi cuerpo. Es frustrante ser retenido, aun lo es más ser retenido por el miedo a que mi vida se termine, cuando hago algo tan simple como caminar por la ciudad por un rato."

$ renpy.music.set_volume(0.2, 0.0, channel="sound")
play sound sfx_phone

"Mientras pondero mi salud, siento mi bolsillo vibrar. Para el momento en que mi teléfono ha comenzado a sonar, mi mano ya está pescándolo."

"Una mirada a la pantalla muestra la llamada de un número que no reconozco. Extraño."

$ renpy.music.set_volume(0.1, 2.0, channel="ambient")
$ renpy.music.set_volume(0.5, 2.0, channel="music")

scene bg city_street1_blurred
show phone mobile:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with locationchange
with Pause (0.5)

"Encogiéndome de hombros, presiono el botón para contestar la llamada y traigo el teléfono a mi oído."

hi "Hola, Hisao Nakai al habla."

mystery "…"

"El sonido de un par de pequeñas aspiraciones puede percibirse, pero ni una palabra se hace escuchar."

hi "¿Hola?"

ha "¿Hi… Hisao?"

"Es Hanako. Su voz es realmente fácil de ubicar, aun si nunca la he escuchado por teléfono antes."

hi "¿Hanako? Perdón, no esperaba que tú llamaras. ¿Qué pasa?"

ha "E-em… Yo… em…"

ha "Si… si no estás ocupado… m-me preguntaba s-si quisieras… q-que nos… v—"

hi "¿Viéramos?"

ha "¡Sí! E-em… quiero decir…"

"Ella suena realmente angustiada con esto. Puedo escuchar voces apagadas de fondo, y es casi la hora del té de la tarde, así que supongo que querrá que la vea en el Shanghái o algo así."

hi "Suena bien. ¿Estás en el Shanghái?"

ha "E-estoy en… la ciudad…"

"¿Hanako está aquí? ¿Sola? Eso es una sorpresa. No es extraño que se encuentre así, si está rodeada de gente y completamente sola."

hi "Eso va de maravilla; justo ahora estoy vagando por ahí. ¿Dónde estás?"

"Hanako se las arregla para balbucear el nombre de la calle, dirección, y algunas indicaciones de donde está. Por suerte no está tan lejos, así que acuerdo verla pronto antes de colgar."

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
$ renpy.music.set_volume(1.0, 1.0, channel="music")
stop ambient fadeout 2.0

show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 0.5 ypos 0.6
with None

scene bg misc_sky
with locationchange

stop music fadeout 5.0

"Volteo al cielo. El calor de verano está golpeando."

"Esta es la primera vez que Hanako ha pedido que hagamos algo juntos más allá de un simple juego de mesa, y la primera vez, al menos desde que la he conocido, que ha venido a la ciudad por sí sola. Tal vez esto significa que Lilly estaba en lo correcto."

scene bg city_karaokeint
with shorttimeskip

$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_soothing fadein 2.0
$ renpy.music.set_volume(0.4, 0.0, channel="ambient")
play ambient sfx_crowd_outdoors fadein 2.0

"Para el momento en que me tambaleo hasta el café donde Hanako se encuentra, he comenzado a jadear otra vez. Estoy sudando tanto que me siento como una paleta de hielo derritiéndose, y apenas puedo sostener la mochila en mi mano."

"Necesito sentarme, desesperadamente."

"Las mesas afuera están todas ocupadas por parejas charlando afanosamente y chicas chismeando entre ellas."

"El contraste entre los grupos de diferentes edades y los estilos de las personas aquí y las personas del pueblo cerca de Yamaku es sorprendente."

"Observo entre las personas sentadas en las mesas, pero no puedo ver a Hanako. Ella dijo que estaba sentada afuera, así que solo debo estarla pasando por alto. No es difícil, dado lo pequeña que siempre trata de hacer su presencia."

"Miro alrededor otra vez, más lentamente esta vez, tomando particular cuidado en ver si puedo encontrar la boina de Hanako. Es bastante distintiva, y estaría muy sorprendido si no la estuviera vistiendo."

"Ahí está. Sin duda, su cabeza está gacha y la mesa en la que está sentada está justo al lado del edificio en una desapercibida esquina."

$ renpy.music.set_volume(0.2, 4.0, channel="ambient")

"Camino a donde ella está y me aseguro de que tengo su atención antes de sentarme, para no darle un susto. Ella me nota, y agita un poco su mano mientras llego a su mesa."

show hanako basic_worry_cas_close:
    center
    ypos 1.1
with charaenter

ha "¿T-te sientes bien?"

"Trato lo mejor que puedo de reír con la pregunta, pero hacerlo únicamente me hace quedar con menos aliento."

hi "No estoy en muy buena forma. No te preocupes."

show hanako basic_distant_cas_close
with charachange

"Hanako asiente, pero aún parece un poco desconcertada."

"Ahora que puedo echarle un buen vistazo a su rostro, algo en ella parece un poco diferente. No estoy seguro de si mis ojos están engañándome, pero luce algo linda."

show hanako basic_normal_cas_close
with charachange

show hanako basic_distant_cas_close
with charachange

"Sus ojos se mueven hacia arriba para mirarme, antes de rápidamente mirar hacia abajo otra vez. Comienzo a pensar que esto va a ser una más bien silenciosa reunión, pero afortunadamente una camarera llega y deja una taza de té frente a Hanako."

show hanako emb_downtimid_cas_close
with charachange

"Hanako casi de forma automática gira ligeramente a un lado y baja el lado de su cabeza."
"Es un movimiento impresionantemente practicado, y hace un buen trabajo con su propósito deseado, esconder sus cicatrices de alguien que se está inclinando cerca."

"Sin embargo, su brazo derecho está aún yaciendo en la mesa, con la cicatriz en el dorso de su mano bastante visible. Esta captura la atención de la mesera, y rápidamente me muevo para distraerla."

hi "Disculpe, ¿podría tomar mi orden?"

"La mesera asiente y me da un par de segundos para mirar al menú."

hi "¿Podría traerme un batido de mango, por favor?"

"Ella asiente antes de casi saltar entusiasmada adentro. Todo es tan diferente en la ciudad, en más de una forma."

show hanako emb_timid_cas_close
with charachange

"Hanako voltea de nuevo arriba hacia mí y ajusta su boina un poco. Si notó a la mesera mirando sus cicatrices, no lo muestra."

ha "¿N-no quieres café…?"

hi "Creo que moriría por este calor si tomara algo como café ahorita."

show hanako emb_downtimid_cas_close
with charachange

"Descansando mi cabeza en mi mano, miro a mi silenciosa compañera. Parece desconcertada; una reacción bastante inesperada a mi insulsa broma. Una sensación nada bienvenida surge dentro de mí cuando me doy cuenta de por qué."

"A diferencia de la mayoría en Yamaku, de hecho, a diferencia de nadie a quien conozca, mi condición va más allá de limitar las actividades que puedo hacer."

"O para ser más preciso, sobrepasar esos límites podría traer consecuencias mucho más graves."

"Afortunadamente, es algo que ha surgido muy raramente desde que entré a Yamaku. Pensé que era tan raro que Hanako y Lilly no pensarían en ello en absoluto. Tal parece que estaba equivocado."

"Hanako bebe su té en silencio mientras espero mi bebida, confirmando que tiene la temperatura correcta con un pequeño sorbo antes de comenzar formalmente."

"Me siento culpable por ser la causa de un silencio incómodo, dado que en el pasado he sido algo duro con Hanako por ellos."

"Eventualmente la misma mesera de antes aparece, trayendo mi bebida. Junto el cambio de mi bolsillo y lo deposito en su mano estirada, antes de que se vaya a atender a otro cliente. Mis ojos se entretienen en ella mientras se aleja."

show hanako emb_sad_cas_close
with charachange

ha "¿Crees que luce… linda…?"

"Hanako está siguiendo mi mirada, sus ojos asimilando a la mesera que nos sirvió. Puedo sentir mi sangre yendo lentamente a mis mejillas mientras coloco mi batido de vuelta en la mesa."

hi "Nah, no puedo decir que esté realmente interesado en ese tipo. Solo lucía bastante como una vieja amiga que conocí antes de mi ataque al corazón."

show hanako basic_worry_cas_close
with charachange

ha "¿Tenías… muchos amigos?"

hi "Tenía unos pocos en mi escuela previa, pero no diría que muchos. Nosotros cuatro solo pasábamos el tiempo juntos después de la escuela y demás."

show hanako basic_normal_cas_close
with charachange

ha "¿Aún les hablas?"

"Sacudo mi cabeza."

hi "No. Perdimos contacto gradualmente mientras estaba retenido en el hospital."

show hanako cover_worry_cas_close
with charachange

ha "¿No estás… triste por eso? ¿O enojado?"

"Hanako luce genuinamente sorprendida. Supongo que es la reacción correcta."

hi "Bueno, la vida continuó avanzando para ellos mientras yo estaba atascado en la sala de hospital. Estaba bastante enojado por ello en ese momento, pero ahora solo son un montón de buenos recuerdos."

hi "Además, una vez que vine a Yamaku encontré nuevos amigos."

"Eso es toda una tapadera de lo que mis sentimientos eran entonces. Pasé por algunos muy oscuros momentos durante mi estadía en el hospital, y estoy realmente feliz de que Hanako y Lilly estuvieron cerca después de que lo dejé."

show hanako basic_bashful_cas_close
with charachange

"Hanako se sonroja mientras pasamos a disfrutar nuestras bebidas."

"Ella parece haberse calmado desde que llegué, y he comenzado a sentirme un poco mejor ahora que he tenido la oportunidad de descansar un poco, así que esta ya está comenzando a ser una linda excursión."

"Incluso si está más calmada que antes, sin embargo, aún está un poco agitada. Ella pasa su mano a través de uno de sus flecos mientras trato de pensar en algo que decir."

hi "Es cierto. Quería preguntar…"

show hanako emb_timid_cas_close
with charachange

"Hanako inclina su cabeza interrogativamente."

hi "No sabía que tuvieras un teléfono móvil. ¿Cómo obtuviste mi número?"

show hanako emb_smile_cas_close
with charachange

ha "L-Lilly… me… lo dio."

"Debí suponerlo."

hi "Sabes, podrías simplemente habérmelo pedido; te lo habría dado."

hi "¿Quieres intercambiar direcciones de correo?"

show hanako basic_bashful_cas_close
with charachange

"Hanako asiente, dejando su bebida y sacando su teléfono de su bolso mientras hago lo mismo."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

show hanaphone:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"Es, sorpresivamente, el mismo modelo que el mío. Pero rosa."

hi "Lindo teléfono."

show hanako basic_smile_cas_close
with None

$ renpy.music.set_volume(1.0, 1.0, channel="music")

show hanaphone:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide hanaphone
with None

"Voltea a verme con una expresión de curiosidad, antes de notar mi teléfono y reír. Es una de esas pocas veces en que he visto a Hanako bajar su guardia lo suficiente para algo así."

show hanako cover_bashful_cas_close
with charachange

ha "Sin embargo yo no lo escogí."

hi "¿Oh?"

show hanako basic_bashful_cas_close
with charachange

ha "Fue un regalo, de Lilly."

show hanako emb_emb_cas_close
with charachange

ha "Nunca necesité un teléfono en realidad, y no podía pagar uno. Sin embargo ella me lo compró para Navidad, diciendo que podríamos usarlo para mantenernos en contacto."

"Ellas básicamente se ven todos los días de todas formas, tanto dentro como fuera de la escuela…"

"Por otro lado, Lilly tiene sus tareas de representante de la clase y sus otros amigos con los que habla. Probablemente ayudaría para situaciones como esta, también, cuando se va por un tiempo."

hi "Lilly es una persona muy especial para ti, ¿verdad?"

show hanako emb_downsmile_cas_close
with charachange

ha "Lo es. Yo… la quiero… mucho."

"Hanako mira hacia abajo y sonríe mientras piensa en ella. Ninguna de mis amistades fue tan profunda como la suya, y tengo que admitir que me siento un poco celoso de su relación."

"Nos decimos nuestras direcciones de correo y las digitamos en nuestros respectivos teléfonos, recupero el número de Hanako de antes y lo coloco en mi lista de contactos."

show hanako basic_smile_cas_close
with charachange

ha "… Hecho. Eso hace tres ahora."

hi "¿Tres?"

show hanako basic_bashful_cas_close
with charachange

ha "Lilly, Akira y tú."

hi "Ah, Akira. Es una persona interesante, ¿no?"

show hanako emb_smile_cas_close
with charachange

ha "Lo es. Pero también es muy linda. Su traje la hace… lucir un tanto genial."

hi "Estoy un poco sorprendido por lo bien que ustedes se conocen, con todo y su trabajo tomando tanto de su tiempo."

show hanako emb_downsmile_cas_close
with charachange

"Hanako mira un poco hacia abajo y toma otro sorbo de su bebida. Si no estuviera mirando atentamente su rostro, habría pasado por alto la pequeña sonrisa en él."

"Supongo que cuando conoce a tan poca gente, aquellos que conoce deben significar mucho para ella."

ha "¿Tú cuántos… tienes?"

hi "¿Yo? Unos nueve o diez."

"Dudo un poco antes de listarlos por miedo a reiterar el hecho de que Hanako no tiene padres, o aparentemente parientes cercanos. También dos de esos son Shizune y Misha, lo que es otra caja de Pandora."

hi "Imagino que Lilly tendrá más que nosotros dos juntos."

show hanako basic_smile_cas_close
with charachange

"Hanako lanza una risilla infantil, y no puedo evitar sonreír. Es una buena sensación que se haya vuelto tan cómoda cerca de mí; en momentos como este, siento como que me estoy acercando a hablar con su verdadero ser."

hi "¿Te molesta si pregunto algo que he estado pensando?"

show hanako basic_normal_cas_close
with charachange

"Hanako sacude su cabeza mientras toma el último sorbo de su té, terminándolo."

hi "No pareces muy celosa de que Lilly tenga muchos amigos. ¿No quieres hacer algunos amigos tú también, o conocer a algunos de los de ella?"

show hanako cover_worry_cas_close
with charachange

ha "No soy celosa. No… me gusta la gente, así que no me importa tener amigos."

"Esa no es… en realidad la respuesta que estaba esperando. No parece temerosa ni triste cuando dice esto, sino más bien, bastante seria."

show hanako cover_distant_cas_close
with charachange

ha "Yo…"

"Hanako frota su brazo incomodada, habiendo tomado mi silencio como razón para continuar. No estoy realmente seguro de lo que debo decir, así que termino simplemente dándole mi atención en silencio."

ha "En la secundaria, era acosada… bastante. Me pusieron apodos, y fui excluida del trabajo en grupo y equipo de deportes. Hubo… cosas peores también."

hi "¿Y eso es lo que hace que no te guste la gente?"

"Ella sacude su cabeza."

show hanako emb_timid_cas_close
with charachange

ha "Eso fue… la escuela primaria."

"Me siento mal por sacar esto ahora. Los adultos tienen suficientes problemas lidiando con las cicatrices de Hanako; los niños serían mucho peor."

"Había asumido que la forma en que trataba de hacer que su presencia no fuera sentida era solo para evitar que las personas se le quedaran viendo, o porque tenía miedo de ellas."

"Ciertamente no porque genuinamente no quería interactuar con ellas en primer lugar."

"Noto la condensación de mi olvidado batido formando un pequeño charco alrededor de la parte de abajo del vaso, así que tomo la oportunidad para terminarlo."

stop music fadeout 5.0

show hanako emb_downtimid_cas_close
with charachange

"Mientras bebo, ella comienza a jugar con su teléfono. Parece que ha recordado a las personas a su alrededor otra vez, y comenzado a tensarse."

"No es exactamente un teléfono barato, tuve que ahorrar por bastante tiempo para poder permitírmelo cuando compré el mío. Sin embargo si Lilly fue a una escuela privada, probablemente no tendría tanto problema para comprar uno para regalo."

"Verla jugar con él me da una idea…"

hi "Oye Hanako, espérame. Vuelvo enseguida."

$ renpy.music.set_volume(0.4, 4.0, channel="ambient")

"Dejo el ahora vacío vaso, deslizo mi teléfono en mi bolsillo, y comienzo a moverme, cuidadosamente caminando por un lado de la bolsa que había colocado entre mis pies."

"Afortunadamente, relajarme mientras hablaba con Hanako me ha ayudado a sentirme mucho mejor que antes."

show hanako defarms_worry_cas_close
with charachange

ha "Espera, ¿q-qué? ¿A d-dónde vas?"

hi "Solo espera aquí, ¡estaré de vuelta en un rato!"

$ renpy.music.set_volume(0.0, 1.0, channel="ambient")

show bg city_karaokeint
show hanako invis_close
with shorttimeskip

$ renpy.music.set_volume(0.2, 0.3, channel="ambient")
"Por mucho que me hubiera gustado trotar de vuelta, sé bastante bien que no podría. Termino caminando de vuelta al café, con una pequeña bolsa azul en mi mano derecha."

show hanako defarms_worry_cas_close
with charachange

play music music_another fadein 3.0

"Hanako me nota rápidamente, luciendo tan confundida como cuando la dejé. Deposito la diminuta bolsa frente a ella y vuelvo a sentarme."

show hanako basic_worry_cas_close
with charachange

ha "¿Esto es…?"

hi "Es para ti. Puedes abrirlo."

show hanako cover_worry_cas_close
with charachange

ha "P-pero…"

hi "Vamos."

"No luce muy segura de esto, pero eventualmente cede, lentamente abre la bolsa y saca su contenido."

show phonestrap:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

$ renpy.music.set_volume(0.5, 1.0, channel="music")

"Una cadena plateada para teléfono cuelga en sus dedos, terminando en una delicada flor. No es exactamente una pieza maestra de joyería, pero es todo lo que me pude permitir."

show hanako cover_bashful_cas_close
with None

"Los ojos de Hanako se iluminan cuando lo ve. Es el tipo de reacción que estaba esperando."

"El sol de verano destellea el plateado mientras gira un poco de aquí hacia allá. No es muy ostentosa, pero luce un tanto encantadora. Creo que le va bien."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

show phonestrap:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide phonestrap
with None

"Hanako baja la correa del celular a la mesa y me mira una vez más."

show hanako cover_worry_cas_close
with charachange

ha "Pero… no es… navidad, ni mi cumpleaños…"

hi "Está bien, no te preocupes por eso. Solo pensé que sería bueno tener algo para decorar tu teléfono."

show hanako basic_worry_cas_close
with charachange

ha "N-no tengo nada para darte…"

hi "Te lo dije, está bien. Los amigos se pueden dar cosas entre ellos de esta forma algunas veces, ¿cierto?"

show hanako emb_downsmile_cas_close
with charachange

ha "Amigos…"

"Hanako baja su rostro tanto que no puedo ver su expresión. Ella eventualmente asiente, antes de tomar su teléfono y juguetear con la correa para sujetarla correctamente."

show hanako emb_smile_cas_close
with charachange

$ renpy.music.set_volume(0.5, 1.0, channel="music")

show hanaphonestrap:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"Ella voltea a verme y sonríe mientras sostiene su teléfono, ahora adornado con una pequeña flor."

ha "Gracias… Hisao."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

show hanaphonestrap:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide hanaphonestrap
with None

"Su sonrisa se prueba infecciosa."

"Por el rabillo del ojo noto a una pareja levantándose y yéndose. Eso me recuerda que el autobús de vuelta al pueblo bajo Yamaku vendrá pronto."

hi "Será mejor que me vaya si quiero alcanzar el siguiente autobús de vuelta al pueblo. ¿Vienes también?"

show hanako def_worry_cas_close
with charachange

ha "Ah, s-sí."

show hanako invis_close at center
with dissolvecharamove

"Ella asiente apresuradamente antes de colocar cuidadosamente su teléfono de vuelta en su bolsillo y levantarse de su silla. Hago lo mismo y tomo la bolsa que había dejado atrás en mi salida."

stop ambient fadeout 1.0
stop music fadeout 3.0

scene bg city_street2
show hanako emb_downsmile_cas_close at center
with locationskip

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_traffic fadein 1.0

"Caminamos lado a lado mientras nos dirigimos a la estación de autobús, sin intercambiar palabras entre nosotros. La mirada de Hanako está firmemente fija por delante de ella, aunque luce muy feliz consigo misma."

"No estoy seguro de lo que debo decirle, pero tampoco estoy seguro de que necesite decir nada. El hecho de que Hanako está feliz, y feliz debido a mí, es suficiente para hacer sentir la carga en mi brazo tan ligera como una pluma."

stop ambient fadeout 2.0

scene black
with dissolve




label es_H29:

scene bg school_scienceroom
with locationchange

play music music_normal fadein 2.0

"Finalmente alcanzando el salón después de la usual caminata desde los dormitorios, entro. Mis ojos inmediatamente giran al tercer asiento de la izquierda en la fila de atrás; el asiento de Hanako."

"Está vacío, y después de dar un vistazo alrededor del salón, parece que aún no está aquí. Las dos chicas del club de periodismo están aquí en los dos asientos a la izquierda del de Hanako, tal como están Shizune y Misha, pero eso es todo."

"Intercambiamos saludos matutinos y tomo mi asiento. Debo admitir que esto es un pequeño alivio y me da al menos unos minutos más para pensar."

"No es que no lo haya estado haciendo antes; desde nuestro viaje a la ciudad Hanako ha estado siempre en mi mente."

"Aún no sé qué sacar de mi relación con Hanako. Me gusta, puedo admitírmelo a mí mismo. Quiero protegerla y defenderla del dolor que siente. Realmente no pienso que mis sentimientos continúen siendo los de una amistad."

"Pero dicho eso… siento que ni siquiera la conozco."

"Si yo hiciera el primer movimiento, ¿cómo lo tomaría? ¿Está ella en un estado emocional que le permita tomar una decisión razonable sobre una relación? ¿Cómo lidiaría ella con cualquier cosa que pasara después?"

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_footsteps_hard fadein 4.0

"También está la posibilidad de que solo esté malinterpretando completamente a Hanako; no es algo difícil de hacer con alguien cuyas habilidades sociales parecen tan poco desarrolladas."

"El sonido de unos pasos viene hacia la puerta, haciendo que me anime."

stop ambient fadeout 0.3

show miki invis:
    right
    xpos 1.1
with None

show miki whistle at right
with dissolvecharamove

"Termina siendo Miki."

show miki smile
with charachange

show miki invis at Position (xpos=0.9)
with dissolvecharamove

"Apenas reconoce mi existencia cuando accidentalmente hago contacto visual con ella. Estoy por voltear a otro lado, pero otra persona viene no mucho después de que ella toma asiento."

show hanako invis:
    right
    xpos 1.1
with None

show hanako emb_downtimid at right
with dissolvecharamove

stop music fadeout 2.0

"Siento que me congelo mientras veo a Hanako entrar. Esta no es una reacción racional, pero no tengo idea de cómo debo actuar o qué debo decirle."

show hanako emb_timid
with charachange

"Por un momento, nuestros ojos se encuentran."

show hanako emb_downtimid
with charachange

show hanako invis at Position (xpos=0.9)
with dissolvecharamove

"Y luego, rápidamente, ella mira a otro lado y se mueve a su asiento sin decir una palabra."

scene bg school_library_ss
with shorttimeskip

play music music_tranquil fadein 3.0

"Como es ya usual por las siguientes clases del periodo, mi cara está enterrada en un libro que encuentro plenamente interesante."

"Estudiar no es algo que viene a mí naturalmente. No estudiaba mucho antes de venir a Yamaku, y hasta ahora me las he arreglado más que nada para aprobar por el puro talento. Es frustrante que ya no pueda hacer eso."

"Juzgando por los rostros de los otros pocos estudiantes en la biblioteca, no creo estar solo en mi desagrado por eso. La miseria ama la compañía, supongo."

"Decidí pasar el almuerzo con Hanako, dado que no hemos comido el almuerzo juntos desde hace ya un tiempo."

"Sin embargo bien podría haber pasado el tiempo estudiando; además de pequeños fragmentos patéticos de conversación, hubo apenas unas palabras entre nosotros."

"¿Por qué continúa haciéndome esto? Solo quiero protegerla, estar ahí para ella, pero cada vez que siento como que nos estamos acercando, terminamos más separados."

ha "¿E-estás ocupado…?"

$ renpy.music.set_volume(0.0, 0.3, channel="music")

show hanako defarms_shock_ss at center
with vpunch

hi "¿¡Hanako!?"

"Mi cabeza voltea de repente en sorpresa, causando que ella se retraiga espantada."

show hanako emb_downsad_ss
with charachange

"Ese fue un mal momento. Si no hubiera estado pensando en ella en ese mismo instante, probablemente no habría sido siquiera sorprendido."

$ renpy.music.set_volume(1.0, 5.0, channel="music")

hi "Perdón, solo me asustaste."

"Me encuentro mirándola fijamente por más tiempo del que debería, así que regreso al texto yaciendo frente a mí. Siento como que estoy más solamente viendo las palabras que en realidad leyendo."

"Tengo la sensación de que Hanako puede notar esto también, así que suspiro y cierro el libro."

hi "¿Qué sucede?"

show hanako emb_sad_ss
with charachange

ha "Solo estaba… p-preguntándome qué estabas l-leyendo…"

"Luce un poco deprimida después de mi reacción al verla. Dándome por vencido con la idea de lograr avanzar más, me levanto y regreso el libro a su lugar en un estante cercano."

hi "Solo un libro de texto de inglés."

show hanako basic_normal_ss
with charachange

ha "¿Te ha s-servido?"

hi "Me hizo darme cuenta de que no me gusta el inglés, sí."

show hanako basic_smile_ss
with charachange

"Hanako lanza una pequeña risilla. Podría reflexionar sobre el extraño estado de nuestra amistad, pero sé que esos pequeños gestos son cosas que no vería si no estuviera al menos un poco más cercano a ella que cuando nos conocimos."

"La observo por un momento, pensando en lo que sé sobre ella. Es un tema ligeramente deprimente."

show hanako basic_worry_ss
with charachange

ha "¿S-sucede algo… malo?"

stop music fadeout 5.0

"Si quiero saber más sobre ella, tal vez debería dejar de ser tan evasivo sobre ello."

"Hablar con Lilly como una igual en lugar de estar con constante miedo de hacerla enojar ha funcionado bien, así que simplemente debo intentar una aproximación directa con Hanako también."

hi "Oye Hanako, ¿te molesta si te hago una pregunta?"

show hanako cover_worry_ss
with charachange

ha "N-no hay problema."

hi "Quería… quería saber cómo era tu vida. Tu vida antes de venir a Yamaku."

show hanako emb_blushing_ss
with charachange

"Ella duda. Por un momento considero echarme para atrás, pero ella parece estar tomando la pregunta muy en serio."

"Me siento y la observo, dejándola tomarse su tiempo en silencio. No está haciendo contacto visual conmigo, y luce casi como si estuviera debatiendo con ella misma sobre abrirse un poco más."

"Su respuesta finalmente sale en un forzado, casi renuente asentimiento. Luce más tensa de lo que lucía antes de que le preguntara."

show hanako basic_worry_ss
with charachange

ha "Está bien. Pero a cambio… tienes que d-decirme sobre tu vida también…"

hide hanako
with charaexit

"Asiento, y la sigo mientras comienza a caminar hacia fuera de la biblioteca para que podamos hablar."

scene bg school_hallway3
show hanako basic_normal at center
with locationchange

play music music_serene fadein 0.5

"Para este momento la mayoría de los estudiantes han dejado el edificio principal, así que además de algunas pocas personas rondando cerca de los salones de los clubes, los pasillos están más que nada vacíos."

hi "Creo… que comenzaremos con la llegada a Yamaku."

hi "Veamos… estaba en el hospital cuando mis padres me dijeron por primera vez sobre la Academia Yamaku."

hi "Los doctores me dijeron que ya no debería regresar a mi antigua escuela. Mis padres estuvieron de acuerdo y me persuadieron de que acudiera a Yamaku, aun si eso significaba vivir lejos de ellos por primera vez."

show hanako cover_worry
with charachange

ha "Debe haber sido… difícil para ti."

hi "Bueno… sí, debo admitir que lo fue."

hi "Mis padres trabajan por muchas horas y tiempo completo, así que vivir razonablemente independiente no fue algo nuevo para mí. Fue el hecho de que iba a ir a una escuela para estudiantes discapacitados lo que me golpeó más duro, creo."

hi "¿Y tú?"

scene bg school_staircase2
show hanako emb_downtimid_close at right
with locationchange

"Un pequeño grupo de chicas charlando pasa cuando nos acercamos a las escaleras, con Hanako presionándose fuertemente a mi lado hasta que alcanzamos la planta baja."

"Usualmente ella no se acerca tanto mientras solo caminamos por la escuela, así que quedo un poco desconcertado."

show hanako emb_downsad_close
with charachange

ha "El personal en el o-orfanato me ofreció algunas opciones sobre lo que podía hacer. La secundaria… no había sido buena, así que pensé que Yamaku podría ser mejor."

ha "Estaba aislada, y pensé que podría ser más fácil arreglármelas aquí con los demás siendo discapacitados."

scene bg school_lobby_ss
with locationchange

"Es bastante irónico que las razones que Hanako buscó en Yamaku son exactamente las razones por las que odié la idea."

"Para mí, se sintió como que estaba siendo hecho a un lado en algún lugar lejos de la sociedad, y de todos los que conocía. Para Hanako, esa fue probablemente una posibilidad llamativa."

hi "¿Cómo era la vida en el orfanato?"

show hanako emb_timid_ss at center
with charaenter

ha "Era… buena. El personal era agradable, y se ocupaban de nosotros. Los niños ahí no me hablaban mucho, pero tampoco quería en realidad hablar con ellos, así que no me importaba."

show hanako emb_downsmile_ss
with charachange

ha "El orfanato tenía una pequeña biblioteca, así que comencé a leer para pasar el tiempo. Al personal no le importaba, porque me volvía más fácil de manejar que muchos de los otros niños."

hi "¿No hiciste ningún amigo ahí?"

show hanako basic_worry_ss
with charachange

ha "No. Creo que… mi vida estuvo en suspenso… durante ese tiempo. Sabía eso, pero no me importaba."

"Pero pensar que su vida estuvo en suspenso por todo ese tiempo… dependiendo de cuándo sucedió el incendio, esa fue una porción grande de su vida. Sin padres, sin amigos, aparentemente sin familiares…"

scene bg school_courtyard_ss
with locationchange

"Caminamos a través de la puerta hacia el patio. Espero necesitar desviar mis ojos del sol, pero para este momento está ya avanzada la puesta."

show hanako emb_timid_ss at center
with charaenter

"Los ojos de Hanako continúan saltando hacia mí, así que desvío la mirada por un rato."

ha "¿Cómo era en el hospital?"

"Rápidamente aclaro mis ideas y trato de reenfocarlas."

"Dudo por un momento, pero sé que tengo que decirle. Somos lo suficientemente cercanos como para que ella se sienta cómoda diciéndome esto, así que es simplemente justo ser recíproco."

hi "Estuvo bien por momentos, pero en otros, fue bastante malo. Al inicio, todos enviaron sus simpatías, y venían a visitar seguido. Era solo como tener un brazo roto o algo."

hi "Ver a todos mis amigos fue uno de los buenos momentos. Iwanako venía seguido también; más seguido que nadie."

hi "Pero también hubo malos momentos. Cuando mis amigos dejaron lentamente de venir, comencé a darme cuenta de lo grave que mi situación era. Me recordó que no tenía solo un miembro roto, sino que ahora era una persona diferente que antes."

hi "Incluso los momentos que Iwanako pasaba conmigo se volvieron tortuosos. Al final, se redujeron a silencio, cuando antes, ella estaba hablando constantemente."

"Pero así es como siempre fue Iwanako. Ella podría haber sido una persona frágil, pero hablaba constantemente para intentar esconder ese hecho. No de nada en particular, solo… hablaba."

hi "Creo que los puntos más bajos deben haber sido cuando mis padres me dijeron que ya no regresaría a mi vieja escuela, mi cumpleaños pasando mientras estaba en el hospital, y… cuando Iwanako se fue por última vez."

scene bg school_gardens_ss
with locationchange

"Dejamos los edificios escolares tras nosotros mientras comenzamos a seguir el camino principal a los jardines. Puede que haya habido algún extraño espectador en los edificios escolares, pero afuera, estamos prácticamente solos."

show hanako basic_worry_ss at center
with charaenter

ha "¿Cómo fue tu secundaria?"

hi "Me gustaba. Crecí en un área bastante metropolitana, y la secundaria estaba cerca, así que estaba bastante abarrotada. No me importaba, probablemente porque estoy acostumbrado a estar entre el gentío y alrededor de mucha gente."

hi "Sacaba buenas calificaciones, y jugaba futbol con mis amigos. También pasaba una buena cantidad de tiempo saliendo con ellos después de la escuela. Aunque también era molestado un poco por mi cabello."

show hanako def_worry_ss
with charachange

ha "¿Tu cabello?"

"Hago una pequeña mueca mientras pongo una mano sobre mi cabello para cubrirlo."

hi "No dejaba de haber mechones y pedazos que se negaban a aplastarse o permanecer donde yo quería, y mi madre no me dejaba rasurármelo. Tenía el hábito de saltar, sin importar lo mucho que tratara de acomodarlo."

show hanako basic_smile_ss
with charachange

ha "Aún lo hace, un poco."

hi "Me preocupaba que recibiría esa respuesta."

show hanako cover_worry_ss
with charachange

ha "¡P-perdón, no quise…!"

"Lanzo una ligera risa y la termino."

hi "Está bien, sé que aún lo hace."

"Se siente extraño tener a alguien que actúa tan interesado en mi pasado. Si fuera alguien más solo pensaría que está siendo educado, pero eso es algo que realmente no pienso que Hanako haría. O si lo hiciera, lo haría tan mal que sería obvio."

scene bg school_dormhallground
show hanako emb_downtimid_close at right
with locationskip

"Hay una buena cantidad de chicas en las habitaciones comunes en la planta baja, y Hanako se presiona contra mi lado una vez más mientras las pasamos."

"Espero que ella se separe, pero en lugar de eso continúa aferrándose a mí mientras caminamos hacia las escaleras."

stop music fadeout 5.0

"Algo sobre la forma en que me está agarrando se siente… diferente de lo usual."

scene bg school_girlsdormhall
with locationchange

"Me quedo absorto en mis pensamientos mientras subimos las escaleras y caminamos por el pasillo. Es solo cuando nos detenemos que me doy cuenta de que la he estado siguiendo sin preguntar."

hi "¿Por qué venimos a tu habitación?"

show hanako basic_distant_close at center
with charaenter

"Ella mira directo a la puerta, sin lanzar ni una mirada en mi dirección."

hi "¿Hanako?"

show hanako basic_normal_close
with charachange

"Ella se mueve para contestar, pero se detiene."

hide hanako
with charaexit

play sound sfx_dooropen

"En lugar de ello, en silencio se separa de mi lado, abre su puerta, y pasa adentro."

"Volteo a ambos lados del pasillo, un poco perdido sobre exactamente qué debo hacer. Encogiéndome de hombros decido seguirla dado que no tengo ninguna razón para no hacerlo."

scene bg school_dormhanako_ss
show hanako basic_normal_ss at center
with locationchange

"Hanako está de pie a mitad de su habitación y me mira directamente. Es desconcertante cuando hace esto, dado que es una acción muy inusual para ella. Abro mi boca para hablar, pero ella se me adelanta."

ha "¿Podrías… cerrar y asegurar la puerta?"

"La mano de Hanako alcanza su pecho, agarrando su blusa en su corazón."

hide hanako
with charaexit

play sound sfx_doorclose
with Pause (0.8)

play sound sfx_lock

"Giro y aseguro la puerta, luego me congelo."

"La atmósfera está comenzando a sentirse algo extraña. Esta sensación es solo más profunda cuando escucho las cortinas siendo corridas tras de mí."

"Pronto será de noche. Somos un chico, y una chica, en una habitación. Ella está cerrando las cortinas, y yo estoy cerrando y asegurando la puerta. No puede… en realidad no puede tener eso en mente… ¿o sí?"

"Trago saliva y giro lenta, muy lentamente. Hanako está en el centro de la habitación, pero no ha girado a verme."

show hanako emb_downtimid_ss at center
with charaenter

ha "Me hablaste sobre tu pasado, así que tengo que hablarte sobre el mío."

"Ella aspira larga y temerosamente, y se detiene por unos segundos. Sus manos se mueven a su listón y comienza a jalarlo, confirmando mis sospechas."

hi "Ha-Hanako…"

show hanako emb_timid_ss
with charachange

ha "P-por favor… no digas nada."

"Obedientemente permanezco en silencio y ella deja caer su listón y pasa a desabotonar su blusa, antes de ocuparse del seguro de su sostén. El proceso es lento. Tal vez solo se siente lento por lo que está haciendo. No estoy seguro."

"Congelado en el lugar, todo lo que puedo hacer es mirar mientras Hanako, con sus manos temblando, desabotona su falda y la deja caer al piso."

play music music_hanako fadein 1.0

scene ev hanako_scars:
with whiteout

"Finalmente, toma su blusa en sus manos y se la quita, su sostén cayendo de sus hombros. Y así, Hanako permanece de pie a mitad de la habitación desnuda, excepto por sus medias y su ropa interior."

ha "Esta soy yo. Todo… lo que soy."

show ev hanako_scars_large:
    xalign 0.0 yalign 1.0 subpixel True
    acdc_warp 30.0 xalign 1.0 yalign 0.0
with locationchange

"Mis ojos son inmediatamente capturados por la cicatriz en su espalda."

"La piel en su lado derecho es de una textura similar a aquella en su rostro, pero también está tensada y cubriendo un área mucho mayor. La cicatrización es mucho peor en su hombro, nalga, y muslo."

"Tal como mi ataque al corazón redefinió mi vida… este es el evento que redefinió la de Hanako."

"Si hubiera visto esto cuando la conocí, habría estado impactado. No solo por la vista, sino también por la idea de que a algo como esto se pueda sobrevivir."

"Pero después de haber tenido tiempo para hacerme a la idea, y después de ver las cicatrices en su cara, manos y cuello, mi reacción es más mesurada. Mi reacción justo ahora no es debido a sus cicatrices, sino a su cuerpo."

ha "El incendio sucedió cuando tenía ocho años de edad. Era de noche, y estábamos durmiendo cuando comenzó."

"La voz de Hanako tiembla, el movimiento de su blusa revela el hecho de que sus manos están haciendo lo mismo."

ha "Yo… me acurruqué… cuando el fuego me barrió. Mi madre… trató de protegerme. E-esa es la única razón… por la que viví…"

"Los ojos de Hanako comienzan a humedecerse, su voz a romperse bajo la presión combinada de estar expuesta de esta forma a mí, y dejar salir esos dolorosos recuerdos de tanto tiempo atrás."

"Quiero decir algo, lo que sea, para hacerla sentir mejor. Pero no puedo. Me siento completamente inútil cuando me enfrento a situaciones como esta."

"Ella se está forzando a acercarse tanto, y aun así es en momentos como este en que me siento más distante a ella."

ha "Perdóname… por hacerte ver esto."

"No tiene caso negar lo obvio. Creo que lo que debo decir ahora, y lo que Hanako quiere que diga, es la verdad. Lo que genuina y honestamente, creo."

hi "No importa. Eres una persona maravillosa, Hanako. Tu cuerpo no cambia eso."

"Ella me ve por un largo rato, su respiración es irregular mientras trata de mantenerse estable entre las emociones que ambos estamos sintiendo. Se siente menos como que me está viendo que viendo a través de mí."

"Lentamente camino hacia ella, y gentilmente coloco mis manos en sus hombros mientras ella deja caer su blusa. Ella ahoga un pequeño grito; no por miedo, sino simplemente sorpresa."

"Estar tan cerca a ella hace a mi mente convertirse en un revoltijo de sentimientos. La cicatrización en su hombro, tan a la vista y como cuero al tacto, choca extrañamente con su de otra forma suave piel y sedoso cabello oscuro."

"Hanako es una chica, con todo lo que ello conlleva. Es más alta de lo usual para una mujer, pero aún tiene curvas en los lugares correctos. La nuca solo visible gracias a su cabello echado sobre su hombro, es atractiva."

ha "Sé… que no soy bonita… como Lilly. Solo… quería que… me vieras. La Yo real."

hi "Pero ya he visto a la verdadera tú. No necesitabas quitarte la ropa de esa forma."

scene bg school_dormhanako_ss
show hanagown stockworry_blush_close_ss at center
with locationchange

"Sus labios están abiertos, solo un poco. Ella deja salir un fuerte suspiro mientras, sin pensarlo, aguantando la respiración me inclino hacia adelante y presiono mis labios contra los de ella."

"El beso solo dura un efímero momento antes de que nuestros rostros se separen, nuestra respiración es rápida y nerviosa. La sensación de la boca de Hanako permanece, y sus ojos permanecen fijos en los míos."

show hanagown stockdistant_blush_ss at center
with charachange

"Temblando un poco yo mismo, remuevo mi corbata y comienzo a desabrochar los botones de mi camisa. Hanako permanece de pie en donde está, mirando al piso frente a ella en lugar de verme desvestirme."

"Por un lado, estoy agradecido por eso. Siempre he sido algo inseguro de mi cuerpo, pero mi cicatriz hizo eso mucho peor. Por otro lado, sin embargo, esta atmósfera se siente muy extraña."

show hanagown stocknormal_blush_ss at center
with charachange

"Mi camisa cae al piso amontonada, tan desordenada y arrugada como la blusa y falda de Hanako. El cuerpo entero de Hanako se estremece visiblemente con el sonido del cierre de mis pantalones siendo bajado."

"Mis pantalones se unen a mi camisa en el piso de Hanako junto a la cama, tal como lo hacen mis calcetines al poco rato. Dudo un poco antes de quitarme mis boxers, y termino dejándomelos puestos."

"Representan el último obstáculo que no creo poder sobrepasar aún. La pura vergüenza me detiene, junto con el no querer que Hanako se altere aún más. Mi inquietud sobre la situación me ha dejado también necesitando mi propia estimulación."

show hanagown stockdistant_blush_ss at center
with charachange

hi "Hanako…"

hide hanagown
with charaexit

"Ella asiente con la cabeza sin voltear a verme en realidad, y se dirige a la cama igual que yo. Ella camina como si sus piernas fueran palillos de madera. Lo encuentro divertido si no fuera porque estoy haciendo lo mismo."

"Tomo la iniciativa, girando y sentándome en la orilla de la cama. Miro a su rostro para invitarla a tomar asiento ya sea junto a mí o frente a mí, pero termino mirando incómodamente hacia abajo para dejar de quedármele viendo a su cuerpo."

label es_H29h:

scene evh hanako_bed_boobs_glance
with whiteout

"Sin embargo, ella capta la indirecta y renuentemente se sienta entre mis piernas. Mientras lo hace, una ráfaga de sensaciones me golpea al unísono."

"La sensación de su parte trasera contra mi entrepierna es la más obvia, pero la de su aroma es igual de fuerte. Ya ha conseguido sudar un poco por su nerviosismo, y el olor y la sensación de su cabello son restregados a través de mi rostro."

"Trato de poner una sonrisa e intento hacer la situación un poco más cómoda para ella, pero se siente realmente forzado. Decidiendo intentar hacer avanzar las cosas, una mano se encuentra con su pecho mientras la otra yace en su pierna."

show evh hanako_bed_boobs_blush
with charachange

"Sus labios se contraen fuertemente mientras ella trata, sin éxito, de suprimir un quejido de sorpresa por la acción."

hi "Perdón, no quise asustarte."

"Hanako toma un respiro y sacude su cabeza como única respuesta."

"Trago saliva con dificultad, antes de comenzar a mover mi mano por ahí, sintiendo y masajeando su pecho y pezón. Se siente realmente bien, todo pasando bajo mi palma con solo un poco de firmeza."

"Por un tiempo no pienso que le esté ayudando a meterse en el ambiente en absoluto, pero lentamente sus párpados comienzan a bajar. Su respiración se reduce a un patrón más rítmico, y su cuerpo comienza a relajarse en el mío."

"Es una satisfacción nueva poder hacer a Hanako sentirse así; definitivamente mejor que la sola sensación de su cuerpo. Puedo sentir también una pequeña y firme hinchazón rozando contra mis dedos que no estaba ahí antes."


show evh hanako_bed_crotch_blush
with charachange

"Lentamente muevo mi mano hacia abajo, tratando de no sorprenderla mucho. Ella no protesta, y mis dedos pronto comienzan a moverse arriba y abajo en el suave surco entre sus piernas."

"Su cuerpo está presionado contra el mío ahora, con un pequeño destello de sudor en ambos. Ella se siente cálida, y todo esto ha servido con creces para provocarme, igual que a ella."

"Hanako da un pequeño grito ahogado, mis dedos presionan un poco más fuerte y se mueven un poco más rápido casi instintivamente. La chica frente a mí, la chica presionando contra mí… la quiero. Todo de ella."

show evh hanako_bed_crotch_glance
with charachange

"Dejo de mover mis dedos, haciendo a Hanako dar un largo respiro de alivio por las sensaciones que estaban brotando dentro de ella. Su rostro mira un poco al mío, en silencio, pero expectante."

"Todo lo que hago es asentir. No sé cuál de nosotros está más aprehensivo justo ahora."

scene bg school_dormhanako_ss
with locationchange

"Me echo hacia atrás en la cama, desembarazándome de Hanako con una cierta cantidad de reticencia. Por su parte, ella se desliza y yace con su cabeza sobre su almohada, respirando fuertemente durante todo esto."

scene evh hanako_missionary_underwear
with whiteout

"Hanako yaciendo frente a mí, sus pantaletas oscurecidas, su pecho palpitando, su cara sonrojada, sus ojos mirando los míos… sus cicatrices solo la hacen ver más única. Termino quedándome sin palabras porque me permitiera verla así."

"Me acerco a ella, cerrando mis manos en su cintura. Espero que ella asienta antes de sostener delicadamente sus medias, bajándolas un poco tan gentilmente como puedo."

"No creo poder quitarlas sin romperlas, así que termino dejándolas en sus piernas y hago sus pantaletas a un lado."

"Hanako yace prácticamente desnuda en la cama; sus más delicadas partes y las cicatrices de su cuerpo están ahora a plena vista."

"Llevando mis dedos a su entrepierna, la acaricio un poco más, haciendo que su respiración pueda escucharse. Debería estar bien si está así de excitada, así que abro mis boxers y me muevo un poco hacia arriba en la cama."

"El cuerpo entero de Hanako se tensa mientras me acerco más a ella, sus ojos se ensanchan. ¿Está… asustada?"

"Tomo un largo respiro, antes de darme cuenta de algo que debí haber pensado antes. Cierro mis ojos y me concentro profundamente."

"Mi corazón golpea mientras enfoco mi mente en su palpitar. Es más rápido de lo usual, desde luego, pero el pulso es regular. Creo… que… puedo mantenerlo controlado, si hago esto lentamente."

ha "¿Estás… bien…?"

"Abro mis ojos y volteo a verla. Supongo que eso debió lucir bastante preocupante para alguien más viéndome."

hi "Estoy bien. Solo me estaba asegurando de que lo estaba."

"Ella duda un poco antes de asentir. Luce un poco menos asustada que antes, así que tal vez mostrarle que también estaba preocupado le ayudó a tranquilizarse."

"Me inclino y presiono mis labios contra los de ella, nuestras lenguas tocándose vacilantes. Puedo sentir su cuerpo tornándose menos tenso bajo el mío, así que nos está regresando a ambos al ambiente correcto."

"Luego recuerdo algo y me retiro."

"Me inclino al lado de la cama donde están mis pantalones, mi mano alcanza mi bolsillo. Siento a ciegas por unos segundos, hasta que con la punta de mi dedo rozo un pequeño cuadro de aluminio."

"Rápidamente lo saco y me enderezo en la cama, alejándome de Hanako un poco y manipulando el paquete. Toma un rato para que todo vaya correctamente, pero eventualmente la funda de hule cubre lo que debe, encajando cómodamente."

"Mi ligera confusión en mi primer intento por manejar un condón parece haberla divertido un poco, y mientras me posiciono sobre ella, compartimos una nerviosa risa. Pero, ahora, necesito intentar concentrarme."

"Miro hacia abajo y trato de llevar mis rodillas y cintura a lo que creo son las posiciones correctas y tomo mi pene con mi ligeramente temblorosa mano."

"La cara de Hanako se dirige a mí, pero sus ojos están apuntados abajo a donde nuestras entrepiernas se encuentran."

"Con un corto respiro, posiciono la cabeza y presiono mi cadera hacia adelante."

scene evh hanako_missionary_closed
with charachange

ha "¡Aahn…!"

"De un golpe, presiono dentro de ella por completo. La ráfaga de sensaciones y emociones llena mi cabeza, y Hanako aúlla de dolor."

"Mirar a su rostro me hace sentir inquieto. Inadvertidamente presioné demasiado fuerte y muy rápido, y le causé más dolor del necesario. Ninguno de nosotros sabe en realidad lo que está haciendo, y lo último que quería era lastimarla."

scene evh hanako_missionary_open
with charachange

"Hanako abre sus ojos otra vez y mira hacia mí. Ella debe haber visto lo preocupado que lucía, dado que trata lo mejor posible de poner una cara feliz. No es muy convincente."

"Miro hacia abajo y comienzo, lentamente, a mover mi cadera otra vez después de darle unos momentos para recuperarse."

"El movimiento se siente realmente poco natural, y puedo sentir músculos moviéndose por toda la parte baja de mi cuerpo que no había sentido moverse de esta forma antes."

"También sé que estoy poniendo un estrés en mi corazón que probablemente no debería, y con cada movimiento le doy seguimiento al ritmo de mi corazón."

"La sensación dentro de Hanako es suave y cálida, y si no fuera por el condón apagándola un poco, dudo que podría durar mucho en realidad. Sus suaves jadeos y constantes movimientos no ayudan para nada tampoco."

scene evh hanako_missionary_clench
with charachange

"Del lado de Hanako, la mirada de dolor no parece estarse disipando como yo esperaba."

"Su piel cicatrizada hace que un lado de su cuerpo se mueva un poco diferente del otro, y mechones de su cabello están para este momento pegándose a su rostro."

"Coloco mis brazos alrededor de su cuerpo y lo levanto ligeramente. Después de retorcernos un poco, tratamos de posicionarnos un poco diferente para minimizar su dolor."

"Con mis manos sosteniendo sus piernas, ambos nos estamos moviendo, para este momento, en movimientos menos y menos mesurados. El olor de Hanako llena mis sentidos, y desde esta posición, no estoy estresando tanto mi cuerpo."

"Mi sentido del tiempo parece distorsionado, y siento como que estoy comenzando a desmayarme por hiperventilación. Pero quiero que Hanako se sienta bien, y no me puedo detener ahora que hemos alcanzado este punto."

"Una nueva ola de placer comienza súbitamente a invadirme. Mis sensaciones están comenzando a brotar, y no creo poder controlarlas más. Acelero, concentrándome menos y menos en contener mi paso."

"Cada vez que se siente como que hemos encontrado un ritmo, lo perdemos en nuestros movimientos."

"Por los sonidos que está haciendo, no creo que esta posición haya ayudado a Hanako a sentirse mucho mejor, y no creo que vaya a poder sostenerla por más tiempo, tampoco."

"Giro y la dejo descender a la cama otra vez, ambos bastante más allá del punto de hacer nada más que alcanzar el final."

"Una arremetida tras otra, puedo sentir ese punto llegar, tensándome frenéticamente trato de aplazarlo tanto como puedo."

hi "¡Hanako…!"

scene evh hanako_missionary_closed
with charachange

"Hanako da un pequeño grito mientras mi mente se pone en blanco."

"Mi cintura golpea la de ella con una buena cantidad de fuerza mientras alcanzo el punto del clímax, y puedo sentirme sacudiéndome dentro de ella. Su cuerpo se tuerce y mueve bajo el mío, solo intensificando las sensaciones de euforia."

window hide

label es_H29x:

scene bg school_dormhanako_ni
show white
with Dissolve(3.0)

window show

"Y luego, después de un par de segundos… termina."

"El sonido de Hanako respirando y mis propios tintineos en mis oídos, son casi dolorosamente altos. Hanako mantiene un brazo sobre su cara, su boca abierta y tragando aire."

stop music fadeout 10.0

show white:
    linear 10.0 alpha 0.0

"Mientras me tranquilizo, súbitamente mis brazos casi ceden y mi visión se distorsiona, como si alguien la hubiera agarrado y jalado a un lado. Me dejo caer de lado sobre la cama junto a la palpitante Hanako, por miedo a caer sobre ella."

"Ambos yacemos al lado del otro, desnudos y presionados uno contra el otro para caber en la cama hecha para una persona. Mis ojos tratan de enfocarse en el techo, sin mucho éxito."

"Jalar una sábana sobre nosotros para alejar el frío es todo lo que puedo hacer."

"El único sonido en la habitación es el de nuestra respiración. El sudor que se ha acumulado en mi cuerpo se siente incómodo. Ambos estamos física y emocionalmente exhaustos, y hechos un desastre."

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.8)

window show

"Mi visión lentamente comienza a regresar a la normalidad mientras continúo viendo al techo, pero mis miembros se sienten como gelatina. Trato de concentrarme en mi pecho, y encuentro su pulso irregular y ligeramente doloroso."

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.8)

window show

"Este es un momento peligroso. Tengo que pensar en todo esto y no entrar en pánico, para no hacer la situación peor."

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.8)

window show

"Con gran esfuerzo, tomo control de mi respiración errática, forzándome a hacer largas y profundas aspiraciones. Cuento media docena antes de comenzar a sentirme físicamente tranquilo otra vez, y presiono mi mano contra mi pecho para asegurarme."

"El latido de mi corazón está de vuelta a la normalidad. Estoy bien."

scene ev hanako_after_worry
with locationchange

play music music_twinkle fadein 1.0

"Giro mi cara hacia la de Hanako, quien ya está mirándome. Su expresión luce bastante aturdida, pero bajo eso, hay definitivamente una mirada de interés. Se ha dado cuenta de lo que pasó."

hi "Estoy… bien. Todo está… de vuelta a la normalidad."

"Me encuentro apenas capaz de sacar esas palabras entre cada respiración."

"No creo que el sexo cansaría tanto un cuerpo normal, así que no tengo duda de que mi condición es al menos parcialmente culpable. ¿Por qué mi cuerpo tenía que hacer esto justo ahora?"

scene ev hanako_after_smile
with charachange

"Todos los pensamientos sobre mi corazón, sin embargo, son hechos a un lado mientras veo la ancha sonrisa formándose en el rostro de Hanako."

"Como siempre, sonrío de vuelta sin pensarlo. La sonrisa de Hanako siempre ha sido infecciosa en su casi infantil dulzura y pasión, algo que la aparta de todos a quienes conozco."

"Ahora mismo… no necesitamos palabras. Todo lo que queremos comunicarnos, podemos compartirlo bien sin decirlo."

stop music fadeout 2.0

scene black
with shuteye



label es_H30:

scene black
with dissolve

hi "Mmh…"

play music music_pearly

scene bg school_dormhanako at left
with openeye

"Mis ojos se sienten pesados mientras se abren lentamente, la luz viniendo de afuera me hace parpadear un poco para dejarlos ajustarse. Mi cuerpo se siente como plomo, y mi cabeza se siente igual de pesada."

"Despertar hacia un techo desconocido es una sensación incómoda. Me recuerda a la primera vez que me desperté para ver el techo de azulejos blancos con hoyuelos del hospital."

"Es solo después de pasar unos segundos viendo hacia él que me doy cuenta de dónde estoy. Esta es la habitación de Hanako."

"Siento como que mi corazón se detuvo otra vez, mientras los eventos de la noche pasada pasan rápidamente por mi cabeza, la sangre se lanza a mis mejillas, y cierro mis ojos una vez más."

"Sin embargo, no hay muchas razones para desgastarme tanto tan temprano, así que trato de sacar esas cosas de mi mente por ahora."

"Giro mi cabeza a un lado para ver si Hanako está donde estaba cuando me quedé dormido. Todo lo que hay ahora es un espacio vacío en la cama, y el cuarto más allá."

"Perezosamente me siento y tallo mis ojos, antes de pellizcar el caballete de mi nariz y ver alrededor de la habitación."

show bg school_dormhanako at right
with charamove_slow

"La única persona aquí soy yo. Aún estoy desprovisto de mi ropa, y después de un rápido vistazo al piso por ella, noto que está cuidadosamente doblada en una esquina de la habitación. Por más que intento, no puedo ver a Hanako en ningún lado."

"El paquete de aluminio del condón ha sido removido también, presumiblemente puesto en la basura."

"Con un gran bostezo, salgo de la cama y rápidamente busco la ropa interior. Hago una mueca ante la posibilidad de colocarme mis boxers otra vez después de que los esfuerzos de ayer hicieron su trabajo en ellos, pero no tengo otra elección."

"Tomando ventaja del hecho de que tengo un poco de tiempo sin nadie alrededor, me visto para el día escolar que viene en poco tiempo."

"Y luego… estoy solo."

"Sin nada más en lo que ocuparme, mi mente se enfoca más en el hecho de que estoy de pie en el cuarto de alguien más después de que hemos pasado la noche juntos, pero no hay ni una señal de ella alrededor."

play sound sfx_rumble

"Mis intestinos prueban ser de más ayuda que mi cerebro solucionando este acertijo. Con un fuerte gruñir, me recuerdan que ella bien podría haber ido simplemente por el desayuno."

"Me hubiera gustado despertar junto a ella, pero… tal vez es algo bueno que haya tenido unos momentos a solas."

"La habitación de Hanako como siempre, es bastante lóbrega de apariencia. Hay algunas pocas decoraciones valiosas, y prácticamente no hay artefactos personales que no estén escondidos en cajones o armarios."

"Ella ha vivido aquí por tres años, pero la habitación luce como si hubiera estado ocupada por apenas un día."

"No debería pensar de más en esto."

"Ella bien podría gustar de vivir de esta forma, como algunos lo hacen. Tener la habilidad de poner tan poca inversión en posesiones físicas tiene sus ventajas, pero aun así, se siente un poco desconcertante dado su pasado."

"Ella dijo que se veía a sí misma como teniendo su vida en suspenso mientras estuvo en el orfanato. Ciertamente ella vive como si todavía fuera así, pero… después de lo que pasó anoche, es bastante difícil imaginar que aún piense de esa forma."

play sound sfx_dooropen

"El sonido de la manija de la puerta rompe mis pensamientos, y volteo a verla."

show hanako basic_normal at center
with charaenter

"Sin duda, Hanako pasa y asegura la puerta tras ella. Tiene lo que parecen ser dos comidas instantáneas preparadas en sus manos, así que esto es un poco difícil."

hi "Buenos días, Hanako."

show hanako basic_bashful
with charachange

ha "Ho… hola."

"Ella da una pequeña reverencia antes de dirigirse a su escritorio, colocando ambos platos. Ahora puedo ver que son pequeños platos de saté, sus contenidos humeantes, con un tenedor clavado dentro del arroz de cada uno."

show hanako basic_distant at Position(ypos=1.15)
with dissolvecharamove

"Le doy las gracias por traerlos, y ambos tomamos uno y nos agachamos a comer. Ella se sienta en su silla del escritorio, mientras que yo me siento en la orilla de la cama."

"No me gusta hablar mientras como, así que el silencio entre nosotros no es molesto por sí mismo. Es el hecho de que solo existe porque en realidad no sabemos qué decirnos el que es desconcertante."

show hanako basic_normal
with charachange

show hanako basic_distant
with charachange

"Hanako mira hacia mí de vez en cuando mientras come. Puedo notarla haciéndolo solo porque yo estoy haciendo lo mismo."

"Estamos comiendo juntos como si fuéramos una pareja. Incluso tuvimos sexo anoche; primera vez para ambos. Pero algo se siente… mal."

"Tal vez ese es el porqué no podemos decir ni una palabra entre nosotros mientras terminamos nuestros platos y los dejamos en el lavabo."

scene bg school_girlsdormhall
with locationchange

"Tal vez ese es el porqué dejamos la habitación de Hanako sin agarrarnos la mano, ni hablando de cualquier cosa."

"Tal vez ese es el porqué se siente como si estuviéramos más apartados de lo que nunca estuvimos antes."


scene bg school_scienceroom at left
with locationskip

"Entramos juntos al salón de clases, ninguno de nosotros viendo al otro. Justo después de que lo hacemos, me doy cuenta de que este podría haber sido un error. Shizune levanta una ceja ante el espectáculo, se han elevado sus sospechas."

show hanako cover_distant at center
with charaenter

"Alcanzamos el pasillo central entre los bancos del salón y nos miramos el uno al otro."

"No estoy muy seguro de lo que debo decir. ¿Quiere que me dirija a ella como novia? No pensé que nuestra relación fuera… Oh. Ese es el porqué esto se siente tan extraño."

hi "N-nos vemos."

show hanako cover_bashful
with charachange

ha "Está bien."

hide hanako
with charaexit

"Incómodamente levanto una mano mientras partimos y tomamos asiento en nuestros respectivos bancos."

"Ni siquiera puedo mirar atrás hacia ella por vergüenza. Siento como que el abismo entre Hanako y yo existe por mi culpa."

show shizu invis:
    center
    xpos -0.1
show muto invis:
    center
    xpos 0.75
with None

show shizu basic_normal:
    xpos 0.0
with dissolvecharamove

show muto normal:
    tworight
with dissolvecharamove

"Shizune comienza a caminar hacia mí, pero entonces Mutou entra al lugar."

show shizu invis at Position(xpos=-0.1)
with dissolvecharamove

"Estoy agradecido por su arribo tan oportuno, alejando a Shizune y sus preguntas, a esperar otro momento."

"No habría podido contestarle, de cualquier modo."

"Me gusta Hanako, pero nunca le he dicho cuáles son mis sentimientos por ella. Hanako nunca me dijo que me viera como nada más allá de un amigo, tampoco. Pero a pesar de ello, dormimos juntos."

stop music fadeout 2.0

scene bg school_scienceroom at left
with shorttimeskip

play sound sfx_normalbell

"La campana para señalar el comienzo del almuerzo suena. Mutou es tomado un poco con la guardia baja, su discurso de química es cortado a media oración, para su disgusto."

"Durante la totalidad de la clase, sus desvaríos me han pasado de una oreja a la otra mientras mi mente meditaba la pregunta sobre Hanako. No puedo sacarla de mi mente, y ahora he conseguido irritarme por ello."

"Me doy cuenta de que nunca dijo sí a lo que hicimos. No dijo no tampoco, pero… ¿habría podido decirlo? Es extremadamente sumisa en el mejor de los casos, y no hay duda de que le tomó un esfuerzo titánico mostrarme sus cicatrices."

"Decido intentar al menos hacer una conversación con ella. Eso sería mejor que la comunicación monosilábica que ha sido lo más que hemos logrado entre nosotros hoy."

show bg school_scienceroom at bgleft
with charamove_slow

show hanako emb_downtimid:
    center
    ypos 1.15
with charaenter

"Camino a su banco con la intención de charlar, pero ella se sonroja incómoda y mira hacia abajo antes de que yo haya llegado."

play music music_rain fadein 4.0

"Aspiro para hablar, pero me encuentro sin palabras. ¿Qué se supone que le debo decir?"

"Escucho pasos acercándose, giro para ver a Shizune y Misha dirigiéndose ya a nosotros, sin duda con la intención de comenzar a preguntar cosas problemáticas."

"Otro par de estudiantes están mirando hacia nosotros y cuchicheando entre ellos mientras lanzan miradas furtivas. Deben habernos notado también a Hanako y a mí llegando juntos más temprano."

"Abro mi boca para tranquilizar a Hanako, pero se me adelanta."

show hanako def_strain
with charachange

ha "Yo… yo…"

show hanako defarms_strain:
    center
with Dissolvemove(0.3)

ha "¡Tengoqueirahaceralgo!"

show hanako defarms_strain:
    easeout 0.5 alpha 0.0 xpos 0.0 xanchor 1.0
with Pause(0.5)

hide hanako
with None

"Ella sale de su silla y se apresura a la puerta. Un par de los libros y plumas que estaban en su banco son enviados al piso en su prisa."

"No mucha gente parece preocuparse por este evento. Unos pocos miran alrededor para ver de qué se trata este alboroto, pero pronto regresan a lo que estaban haciendo antes."

"Soy dejado mirando desesperadamente a la puerta por la que Hanako desapareció. La idea de correr tras ella pasa por mi mente, pero estoy bastante seguro de que Hanako puede correr más rápido que yo."

"Y además… ¿qué le diría una vez que la alcanzara, en cualquier caso?"

"Eventualmente, solo me agacho y comienzo a levantar los objetos que se cayeron de su escritorio al piso. Me siento bajo en cada aspecto, reducido a esto al tiempo que los estudiantes me pasan de largo mientras salen del salón."

show shizu invis_close:
    tworight
    xpos 0.8
show misha invis_close:
    twoleft
    xpos 0.2
with None

show shizu behind_blank_close at tworight
show misha perky_smile_close at twoleft
with dissolvecharamove

"Siento un toque en mi hombro. Volteo hacia arriba para ver a Shizune y Misha mirándome."

"Ambas con la curiosidad sobre la situación escrita en sus rostros, mezclada con una apariencia de ligera disculpa por la idea de que prácticamente ellas fueron las responsables de lo que acaba de pasar."

show shizu basic_normal2_close
with charachange

shi "…"

show misha sign_confused_close
with charachange

mi "Hicchan, si podemos ayudar en algo…"

"Solo sacudo mi cabeza. Este no es un asunto para ellas, y por la expresión de Shizune y el tono de voz de Misha, creo que ellas lo saben también."

show shizu behind_blank_close
with charachange

with Pause(0.3)

hide misha
hide shizu
with charaexit

"Shizune acepta mi respuesta, y da una reverencia solemne antes de salir del salón. Pronto Misha la sigue, obedientemente siguiendo su rol como sombra de Shizune."

"Me levanto, con los libros y plumas en la mano, y los coloco dentro del banco de Hanako. Con el salón ya vacío, termino solamente reclinándome contra el banco y pensando en silencio."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\nSe siente como que hay una completa desconexión emocional entre Hanako y yo. No nos hemos conocido por mucho tiempo, y a pesar de querer empezar a salir con ella, realmente no sé mucho sobre el cómo ve Hanako las cosas."

n "He estado estudiando tanto como he podido para los exámenes, pero aún no siento que haya tenido ningún sentido real de dirección tras ello. Traté de ser un amigo para Hanako, incluso si no pude decirle mis sentimientos, y todo lo que hemos hecho es alejarnos el uno del otro."

n "\nNi siquiera pude escribirle una carta de vuelta a la única chica que me amó jamás, Iwanako."

n "\nQué debo hacer… qué puedo hacer… simplemente no sé la respuesta a ninguna de esas preguntas. Pero sí sé que no hay nadie más que pueda ayudarme con ellas."

n "Solo con regresar a la forma en que las cosas eran sería suficiente para hacerme feliz, pero sé que no podrá suceder jamás. Algo cambió entre nosotros anoche. Tal vez cambió desde antes, y solo ahora alcanzó el punto crítico."

nvl clear

n "\n\nSé que hay una pared que Hanako tiene entre ella y yo. He estado chocando contra esa pared cada vez que he tratado de interactuar con ella a cualquier nivel."

n "Pero ahora estoy comenzando a pensar que yo tengo mi propia pared entre nosotros tal como ella. Prácticamente ella tuvo que arrastrar mi pasado fuera de mí, y el mío era mucho menos traumático que el de ella."

n "Quiero decir que es porque no he tenido suficiente tiempo para adaptarme desde mi ataque al corazón, pero sé bastante bien que sería solo una excusa."

n "La única vez que recuerdo que en verdad se sintió como que se estaba abriendo a mí por decisión propia, cuando estábamos jugando billar en la ciudad, yo fui el que la detuvo de ir más allá."

n "\n\nQuiero conocer mejor a Hanako. Quiero salvar nuestra amistad, si no es que comenzar una relación verdadera con ella."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear
window show

"Mi mente comienza a golpear mientras me reclino en su banco, pensando en el vacío salón de clases en el que hemos pasado mucho tiempo juntos."

stop music fadeout 2.0

"Tengo que hablar con Hanako."



label es_H31:

scene bg suburb_park
with shorttimeskip

play music music_moonlight fadein 0.5

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_parkambience fadein 2.0

"Doy vueltas en el parque, sintiendo a la ansiedad volcarse sobre mí. A cada rato alcanzo mi bolsillo para tomar mi teléfono, pero cada vez dudo y termino deslizándolo de vuelta."

"Si esta fuera una situación normal, no estaría saltándome las clases. Desafortunadamente, no lo es, y por lo tanto me encuentro en el pueblo bajo la escuela a las dos de la tarde."

"Desde que conocí a Hanako, he sido el que inicia todo entre nosotros. El que empezaba las conversaciones, iba a donde quiera que ella estuviera, y sugería lo que debíamos hacer. Hoy, esta vez, no quiero ser el único haciendo eso."

"Mi mano se hunde en mi bolsillo una vez más. Esta vez navego rápidamente al menú de mensajes de texto antes de tener oportunidad de cambiar de opinión otra vez."

"“Hanako, si quieres hablar, estaré en el parque del pueblo por un rato”."

"Peleando contra una última cantidad de duda, digito mi mensaje a Hanako y presiono el botón para enviarlo."

"Y ahora… espero. Mi parte en esto ha sido completada; lo que ahora necesita pasar es que Hanako tome una decisión. No tendría sentido que yo la arrastrara aquí. Ella necesita decidir por sí misma si quiere verme."

stop ambient fadeout 4.0

with shorttimeskip

"El jugo de manzana de la máquina expendedora sabe terriblemente amargo mientras lo trago de golpe. Mi agarre en la lata ha causado que se abolle ligeramente en el medio."

"No debería estar así de tenso, pero probablemente es inevitable."

"Hanako significa mucho para mí."

"Lo que sucedió en el último par de días ha puesto mucha presión en ambos. La idea de perder todo el progreso que hemos hecho en acercarnos el uno al otro, y perder nuestra amistad por completo, es profundamente perturbadora."

"Pero incluso entonces… aún no sé qué tan cercanos somos realmente. Puede que hayamos tenido sexo, pero antes de eso, todo lo que supe que éramos era amigos. Tal vez somos más que eso, pero si es así, nunca me di cuenta."

"Tal vez ese es el porqué me siento tan incómodo justo ahora. No entiendo a Hanako, a pesar de todo el tiempo que hemos pasado juntos. Los minutos pasan, y aún no tengo idea de si aparecerá."

ha "¿Hi… Hisao…?"

"Me detengo por un momento, casi sin creer que estoy escuchando la voz que estoy escuchando. Dejo caer la lata y me levanto sobresaltado."

show hanako basic_worry_cas at center
with charaenter

hi "Hanako…"

show hanako emb_downtimid_cas
with charachange

"Nos miramos por unos segundos, antes de que Hanako se sienta demasiado apenada para mantener el contacto visual y comience a juguetear nerviosamente con su bruscamente cortado mechón de cabello cubriendo su cara."

"Cuando fui a ver a Hanako en su habitación por mí mismo después de su ataque, no tenía idea de qué decir. Eso estaba bien, entonces. Todo lo que queríamos era la presencia del otro."

"Pero ahora… siento como que necesito hablarle directamente. Quiero romper esta pared entre nosotros, antes de que nos aparte a los dos para siempre."

stop music fadeout 4.0

hi "Hanako… yo…"

hi "Lo que hicimos esa noche… ¿cómo debo interpretarlo?"

show hanako cover_worry_cas
with charachange

"Hanako deja de jugar con su cabello y me mira, su cabeza inclinada ligeramente hacia abajo."

show hanako basic_worry_cas
with charachange

play music music_innocence fadein 4.0

ha "Pensé… que eventualmente te irías si yo fuera solo alguien a quien necesitabas proteger."

show hanako emb_sad_cas
with charachange

ha "Pensé que si te dejaba hacer eso… podrías verme como algo más que eso."

"Mi primera reacción es desconfianza, pero… lo hice con ella, después de todo. Tuve muchas oportunidades donde podría haber parado las cosas, dar un paso atrás, y cuestionar lo que estábamos haciendo. Al final, sin embargo… no lo hice."

"Una horrible sensación se eleva en el fondo de mi estómago. Ella se me ofreció debido a lo que pensó que yo quería, y ahora, se siente como que tomé ventaja de ella. Puede que haya estado dispuesta, pero solo bajo falsas premisas."

"Nunca he sido bueno en ocultar mis emociones de mostrarse físicamente, y ahora no es diferente. Hanako mira hacia abajo una vez más, con una extraña mezcla de depresión, remordimiento, y náusea escrita en su rostro."

"Denso silencio flota en el aire, exceptuando la brisa soplando a través de los árboles a nuestro alrededor."

show hanako emb_downsad_cas
with charachange

ha "Sabía… que no me podías ver de esa forma…"

"Las palabras de Hanako son dichas en poco más que un susurro, aparentemente dirigido tanto a ella como a mí."

hi "¿En qué forma? ¿Qué quieres decir?"

ha "Todo lo que siempre fui para ti fue… una persona inútil. Solo alguien… a quien proteger. Alguien como… una niña."

show hanako cover_distant_cas
with charachange

ha "Q-quería ser más que eso para ti, pero después de tanto… me… acostumbré a eso."

"El tono de su voz es diferente a cualquiera que le haya escuchado antes. Suena asqueada. No de mí, sino de ella."

show hanako cover_worry_cas
with charachange

ha "Después de que salí de mi habitación… vi que estabas comenzando a alejarte."

show hanako basic_worry_cas
with charachange

ha "Sentí como que iba a perderte, porque… querías a alguien con quien pudieras tener… ese tipo de relación."

show hanako emb_downtimid_cas
with charachange

ha "Estabas más silencioso en la escuela que antes, y estabas llevándote tan bien con Yuuko… pensé… que podría perderte."

"¿Ella pensó que estaba aburrido de ella, porque quería una relación romántica?"

hi "Pero… somos amigos, ¿cierto? No te abandonaría simplemente de esa forma, incluso si lo que estás diciendo fuera verdad."

show hanako emb_timid_cas
with charachange

ha "Amistad… fue algo a lo que pensé que había renunciado. Dejé de creer en otros… después de lo que pasó luego del accidente…"

show hanako emb_downsad_cas
with charachange

ha "Antes de que sucediera el accidente, me llevaba bien con las personas y otros niños. No tenía muchos amigos… pero no me importaba, porque atesoraba aquellos que tenía."

show hanako emb_sad_cas
with charachange

ha "Pero después de él…"

show hanako emb_downsad_cas
with charachange

ha "Los otros me ponían nombres, y me molestaban mucho. Dolía… muy profundamente. Los maestros trataban de ayudar, pero no podían hacer mucho, e incluso muchos de ellos retrocedían solo con verme."

ha "Entre aquellos poniéndome nombres y molestándome… estaban los que yo pensé que eran mis amigos más cercanos."

show hanako cover_worry_cas
with charachange

ha "Desde entonces, creí que no importaba si nadie más me reconocía. Todo lo que siempre hizo mi existencia fue crearle problemas a la gente… era más fácil… si simplemente no existía."

show hanako cover_bashful_cas
with charachange

ha "Pero después de conocer a Lilly, y luego a ti…"

show hanako basic_normal_cas
with charachange

ha "Traté, pero… no pude hacerme pensar de esa forma otra vez."

"Todo ese tiempo… no confió en mí. Pensó, tal como para todos en su vida había sido, que no tenía valor para mí. Alguien a quien tirar una vez que me aburriera de estar con ella."

"Eso duele. Ese es el tipo de persona como el que nunca, nunca quise que me viera, porque sé mejor que nadie lo horrible que se siente ser tirado por aquellos a los que pensé que les agradaba."

"Ella está derrumbándose por los recuerdos que está rememorando. Me siento inútil, completamente imposibilitado de consolarla. Pero en una extraña manera, casi estoy agradecido de que está permitiéndome saber esto."

"La pared entre nosotros está yéndose, incluso si duele tanto echarla abajo."

hi "Hanako, si solo me hubieras dicho…"

show hanako cover_worry_cas
with charachange

ha "¿Estaba… equivocada?"

hi "Desde luego que…"

"No lo estaba. Hanako no estaba equivocada. Es difícil forzarme a admitir esto, pero sé que tratar de negarlo es inútil. Para mí, y para Lilly, ella era alguien a quien tratábamos de proteger."

"Ella se había vuelto para mí lo que yo me había vuelto para mis amigos después de mi ataque al corazón, una persona rota. Ella me gustaba, incluso posiblemente la amaba, pero nunca actué respecto a eso precisamente porque pensé que ella era muy frágil."

hi "Quiero decir… no te veo de esa forma ahora."

hi "Me preocupé por ti después de lo que te sucedió en clase, y pensé que debía tratar de protegerte."

hi "Pero cuando te encerraste en tu cuarto, me asusté. Pensé que me estabas rechazando, y me forzó a pensar bastante sobre… diferentes cosas."

show hanako defarms_strain_cas
with charachange

ha "¡No te estaba rechazando!"

"Ella lo deja salir con casi un tono de miedo en su voz, tomándome con la guardia baja. Ella rápidamente se apena de su arrebato, antes de apretar sus puños y decidir en su mente lo que quiere decir."

show hanako emb_timid_cas
with charachange

ha "No te haría nunca eso. No a ti."

show hanako emb_downtimid_cas
with charachange

ha "Incluso aunque estaba asustada… incluso aunque traté de alejarte… aún intentaste acercarte a mí."

ha "Me encerré porque… solo era una carga para ti. Para Lilly. Para todos."

show hanako emb_sad_cas
with charachange

ha "C-cada cumpleaños era igual. Todos pretendiendo lo mejor posible que yo importaba. Todos pretendiendo que todo estaba bien… por ese día del año."

show hanako emb_downsad_cas
with charachange

ha "No quería existir, pero no me dejaban. Aun después de conocer a Lilly… todo era lo mismo. Era tan inútil como siempre he sido, incapaz de hacer nada por ella, o por mí."

ha "No quería ser igual… para ti."

"Lilly y yo estábamos completamente equivocados. Por lo que ha dicho, todo lo que hicimos por ella… solo la habría hecho sentir peor. Incluso lo poco en lo que pensé que estaba en lo correcto sobre ella era una malinterpretación total."

hi "Después de que te encerraste en tu habitación, decidí tratar de acomodar mi pasado también, y ordenar mi futuro. No sabía cómo lidiar con las cosas que perdí al llegar a Yamaku, así que estaba tratando de arreglarlas yo mismo."

hi "Pensé… que nos ayudaría a hacernos mejores amigos… si hacía eso."

hide hanako
with charaexit

"El silencio flota en el aire otra vez. Trato de mantenerme mirándola, pero no puedo. Realmente me siento decaído, y aunque quiero disculparme… no sé cómo podría hacerlo."

"La escucho respirar profundamente, y solo volteo a verla otra vez después de escucharla caer al piso."

scene ev hanako_park_alone
with whiteout

"El sonido de su llanto rompe mi corazón. Sé que soy responsable de esto, y sé que no puedo hacer nada para ayudarla. Si Hanako se siente avergonzada, entonces yo lo siento aún más."

show ev hanako_park_away
with charachange

"Me apresuro a ella mientras las lágrimas continúan rodando por sus mejillas sin detenerse, envolviendo mis brazos alrededor de ella. No me preocupo más por cómo debo de verme. Solo quiero estar cerca de ella ahora mismo."

ha "Lo lamento, Hisao… He echado todo a perder…"

hi "Está bien. Todo está bien. Soy yo el que debería lamentarlo. Estaba entrometiéndome a tus espaldas, y nunca te dije nada."

"Puedo sentir mi agarre tensarse en Hanako mientras mi visión se vuelve borrosa. No puedo molestarme en tratar de contenerme ahora. Tengo que forzar mis palabras a salir cuando un nudo comienza a formarse en mi garganta."

hi "Para ser honesto, Hanako… tenía miedo. Por primera vez desde mi ataque al corazón, estaba realmente asustado."

show ev hanako_park_look
with charachange

ha "¿Hisao…?"

hi "Perdí tanto cuando vine a Yamaku. Estaba… dependiendo de ti, más de lo que nunca pensé hacer."

hi "Aun ahora, todavía tengo ese hueco dentro de mí. Después de perder mi vida entera, y a todos los que conocía, la idea de perderte también…"

show ev hanako_park_away
with charachange

ha "Pero soy solo una inútil—"

hi "¡Tú eres mi amiga, Hanako! Tú eres…"

hi "No, eres más que eso. Te amo, Hanako. Te amo tanto que la idea de perderte me asustó demasiado…"

"Ah, esto es malo… realmente estoy dejando salir todo esto. No puedo atreverme a mirarla a la cara ahora mismo."

show ev hanako_park_look
with charachange

ha "Lo siento, Hisao…"

ha "No puedo evitar… sentirme un poco feliz. Por tanto tiempo… eso es lo que quería… escuchar…"

show ev hanako_park_closed
with charachange

"La última de las compuertas se rompe. El sonido de su llanto impregnando el aire mientras su cuerpo se sacude contra el mío."

"Nos abrazamos fuertemente, conectados más que nunca en nuestro dolor compartido, y nuestra felicidad compartida."

"No sé cómo van a ser las cosas, después de esto. Pero justo ahora… no me importa. No hay ninguna otra persona en el mundo con quien podríamos compartir estos recuerdos y emociones. Nadie."

stop music fadeout 2.0

scene bg suburb_park
with shorttimeskipsilent

play ambient sfx_parkambience fadein 2.0
play sound sfx_can_clatter

"Después de tirar la lata sucia en un bote junto a la banca, tomo asiento junto a Hanako. Ella hace a un lado el pañuelo que le di para limpiarse, que no ha ayudado mucho."

"Por otro lado, dudo que yo luzca mucho más presentable."

"Aun ahora, me siento vacío y un poco avergonzado por dejar salir mis emociones en público de esa forma. Sin embargo no es una mala sensación. Creo que Hanako se siente de la misma forma, también."

hi "¿Te has calmado un poco?"

play music music_comfort fadein 4.0

show hanako cover_bashful_cas_close:
    tworight
    ypos 1.1
with charaenter

ha "S-sí. Gracias."

"Por un rato, solo nos sentamos y tomamos nuestro tiempo antes de hablarnos otra vez. Ambos necesitamos un poco de tiempo para recuperarnos."

show hanako basic_smile_cas_close
with charachange

ha "El clima es lindo en esta época del año."

hi "Sí, lo es."

show black
with shuteye

"Cierro mis ojos por un momento, disfrutando la sensación del calor del sol y la fría brisa contra mi rostro. El clima es realmente bueno hoy. Realmente, realmente bueno."

hi "Sabes… realmente no quiero volver a clases justo ahora. ¿Tú quieres?"

hide black
show hanako basic_bashful_cas_close
with openeye

"Ella sacude su cabeza mientras termina de limpiar sus ojos con su puño. La pequeña sonrisa que da es linda, y es un recordatorio de lo sincera que puede ser."

"Sonreír para otras personas podría ser completamente normal, cosa de todos los días. Pero para Hanako… ella sonríe tan raramente y tan sinceramente, que cada vez que lo hace, siento una sensación de alivio y felicidad."

show hanako cover_worry_cas_close
with charachange

ha "Perdón. Por… todo."

hi "Está bien. Creo que ambos tenemos un poco por lo cual disculparnos."

show hanako emb_timid_cas_close
with charachange

ha "Sé que… soy muy tímida. Sé que no quieres que lo sea, no creo poder…"

hi "Puedes cambiar, Hanako. Lo sé porque, incluso en el tiempo que te he conocido, ya has cambiado. Para ser honesto, el solo poder sentarme aquí y hablarte así significa que has cambiado bastante desde que nos conocimos."

show hanako emb_downtimid_cas_close
with charachange

ha "Pero… no puedo ser así con… nadie más. No tengo ningún plan para cuando la escuela termine, tampoco…"

"La confianza de Hanako comienza a deslizarse otra vez, pero creo que ahora, puedo finalmente hablarle como a una igual. Puedo hacerlo porque sé que somos iguales en muchas formas."

hi "Solo date tiempo, y creo que podrás conseguir lo que quieres. No, estoy seguro de que podrás conseguirlo. Puedo ver que lo has intentado, y tengo fe en ti."

hi "Y puedes depender de mí si sientes como que necesitas a alguien para apoyarte, sabes."

show hanako defarms_strain_cas_close
with charachange

ha "P-pero no puedo pedirte eso…"

hi "Puedes, porque eso es exactamente lo que yo te estoy pidiendo. Estoy pasando por lo mismo, sabes."

hi "Se llama amor."

show hanako basic_bashful_cas_close at tworight
with dissolvecharamove

"Hanako sonríe, antes de que yo salga de la banca y me sacuda. Ella hace lo mismo al poco rato."

hi "Tengo algo de hambre. ¿Quieres ir por algo de comer?"

"Ella asiente vigorosamente. La forma en que está sonriendo, la forma en que está actuando, incluso el aire en general que despide… siento como que esta es la primera vez que la veo genuinamente feliz."

$ renpy.music.set_volume(0.6, 1.0, channel="ambient")

scene bg suburb_roadcenter
with locationchange

"Ambos nos dirigimos a la calle, caminando uno al lado del otro."

show hanako emb_emb_cas_close at center
with charaenter

ha "¿Hisao?"

hi "¿Sí?"

show hanako emb_downtimid_cas_close
with charachange

ha "Creo… que… no te entiendo realmente."

hi "Creo que no te entiendo tampoco. Pero creo que está bien."

"No hay ni una señal de desesperación en nuestras voces. No entendernos el uno al otro es simplemente natural; las paredes que establecimos entre nosotros no podrían de ningún modo ser destruidas en un solo día."

"Pero está bien. Mientras lo hagamos día a día, y tratemos de entendernos el uno al otro… creo que todo estará bien."

show hanako emb_timid_cas_close
with charachange

show hanako emb_downtimid_cas_close
with charachange

"Sin embargo, mientras caminamos por la calle, los ojos de Hanako saltan a mi rostro y de regreso a la calle repetidamente."

hi "¿Hay algo que te preocupe? Luces inquieta."

show hanako basic_normal_cas_close
with charachange

"Ella avanza más despacio antes de detenerse por completo."

"Cuando giro a verla, ella toma un largo y profundo respiro, mirando mi cara atentamente. Esta expresión… la vi una vez antes en su rostro. Solo una, cuando accidentalmente la sorprendí en su habitación."

ha "Creo… creo que… creo que tengo algo… que necesito darte."

hi "¿Qué es? No necesitas ser evasiva con ello."

show hanako cover_distant_cas_close
with charachange

ha "Quería darte esto desde hace mucho, mucho tiempo, pero… ahora que debo… es demasiado vergonzoso…"

hi "No te preocupes. Lo aceptaré, sea lo que sea."

show hanako basic_bashful_cas_close
with charachange

"Ella da una dulce y tímida sonrisa, antes de tomar mi hombro con su mano."

ha "Entonces, por favor acepta mi primer regalo para ti, Hisao…"

hi "¿Hanako…?"

stop ambient fadeout 1.0

window hide
scene unlock_ev hanako_goodend_close
show unlock_ev hanako_goodend_muffin
show unlock_ev hanako_goodend

show ev hanako_goodend_close:
    xalign 0.0 yalign 0.0
    zoom 1.0 subpixel True
    linear 6.5 zoom 0.8
with whiteout

$ renpy.pause(4.0, hard=True)

play sound sfx_whiteout

scene ev hanako_goodend:
    xalign 0.0 yalign 0.0
    zoom 1.0 subpixel True
    parallel:
        easein 12.0 zoom 0.8
    parallel:
        6.0
        "ev hanako_goodend_muffin" with Dissolve(2.0)
with locationchange

$ renpy.pause(12.0, hard=True)

$ renpy.music.set_volume(1.0, 2.0, channel="ambient")
stop music fadeout 4.0

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
