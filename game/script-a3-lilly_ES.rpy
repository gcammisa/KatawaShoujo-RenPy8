label es_L9:

window hide None

scene black
with dissolve

scene bg misc_sky at Fullpan(10.0)
with locationchange

$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_normal fadein 3.0

window show

"Apoyo mi barbilla sobre mi mano mientras miro distraídamente por la ventana, otra de las clases de Mutou prolongándose más y más como si fuera interminable."

"El cielo estival es casi hipnotizante con su celeste esplendor. Solamente la ocasional nube pasajera interrumpe la azul extensión."

"Esta sensación de añoranza probablemente sea mi lado callejero deseando escaparse."

mu "Nakai, ¿podrías responder esto?"

"Aunque ahora ese lado de mí se ha perdido en el pasado."

scene bg school_scienceroom
show muto normal at center
with locationchange

hi "En ese caso… ¿supongo que uno usaría el sufijo -ano?"

show muto smile
with charachange

mu "Correcto. Siguiendo, el sufijo para…"

"A medida que mi atención hacia Mutou vuelve a desvanecerse, diviso a Misha levantándome el pulgar de forma entusiasta, y le asiento para tranquilizarla."

scene bg school_scienceroom
with shorttimeskip

"Ha pasado un puñado de días desde que Lilly se marchó a Escocia, días que han pasado con relativa tranquilidad."

"La vida siguió mayormente como siempre, a diferencia de lo que esperaba. Si bien pensamientos sobre ella han rondado por la periferia de mi mente desde que ella se fue, los acontecimientos presentes logran reprimirlos. Al menos por el momento."

"Así que me encuentro conversando ociosamente con Hanako, como siempre, cuando llega la hora del almuerzo."

show hanako basic_normal
with charaenter

ha "¿Los que siguen en la serie también son buenos?"

hi "En realidad no. Sería mejor que te quedaras con el original. Sus libros siguientes no le hicieron justicia, aparte quizás de “Dios Emperador”."

show hanako basic_bashful at center
with charachange

ha "Gracias, de verdad no estaba segura de si…"

show misha invis at offscreenleft
show shizu invis at offscreenleft
with None

show hanako defarms_shock at right
show shizu behind_blank at center
show misha hips_smile at left
show bg school_scienceroom at bgright
with dissolvecharamove

"Cuando Hanako da un paso hacia un lado, veo a Shizune avanzar con su típica seriedad, acompañada de su siempre presente sombra de cabello colorido."

"Por mucho que lo intente, no puedo entrever en sus rostros ninguna pista de su intención. El rostro impasible de Shizune y la alegría aparentemente ilimitada de Misha son una combinación demoniaca."

hi "Buenas Shizune, Misha."

show hanako emb_timid
with charachange

ha "Ah… hola."

show shizu basic_normal
with charachange

"Resalto el saludo asintiendo a Shizune para que entienda la idea. Ella inmediata y tajantemente nos devuelve el gesto a ambos."

"Ha pasado tiempo desde que he hablado de verdad con alguna de las dos. Por un rato pensé que podrían haber estado evitándome, pero eventualmente llegué a la conclusión de que Shizune realmente no es el tipo de persona que hace eso."

show shizu adjust_happy
with charachange

shi "…"

show misha sign_smile
with charachange

mi "¡Buenas~! Shicchan dice que Mutou quiere verte en algún momento."

"Debido a esta afirmación, mi rostro se retuerce como si acabara de comerme algo podrido, cosa que divierte sin fin a Misha."

show misha cross_laugh
with charachange

mi "¡Guajajaja~! ¡Cualquiera pensaría que estás en problemas, Hicchan!"

show shizu behind_smile
with charachange

shi "…"

show misha perky_smile
with charachange

mi "Quizás no te des cuenta, pero de entre todos en el grupo eres el que menos tiene de qué preocuparse."

show hanako emb_smile
with charachange

"Vaya voto de confianza más inesperado. Hasta Hanako asiente vacilante para reafirmar el punto."

hi "Gracias, tendré eso en mente. Aunque hay algo que he querido preguntarte."

show shizu basic_normal
with charachange

shi "…"

show misha hips_smile
with charachange

mi "¿Y qué sería eso, Hicchan?"

"Tengo el presentimiento de que esto no irá bien, pero aquí va…"

hi "¿Hay algún motivo por el que tú y Lilly no se lleven bien? Parece que hasta un poco de civilidad les ayudaría a ambas en sus deberes."

show shizu cross_angry
with charachange

"La fría mirada de Shizune cuando Misha le traduce alegremente las palabras me detiene por completo. En retrospectiva, realmente podría haberlo expresado mejor."

show hanako emb_sad:
    xpos 1.05
with dissolvecharamove

"Por el rabillo del ojo, estoy seguro de que veo a Hanako apartarse. Solo un poco."

show shizu basic_angry
with charachange

"Afortunadamente, Shizune nota eso y calma sus ánimos mientras pasa con fuerza su mano por su cabello para liberar tensiones. Perfectamente a tiempo, Misha comienza a interpretar en el momento que los brazos de Shizune comienzan a moverse."

show shizu behind_frown
with charachange

shi "…"

show misha hips_frown
with charachange

mi "Diría que esas cosas no te son relevantes, pero como parece que te has hecho amigo de Lilly…"

show shizu adjust_frown
with charachange

"Ella se detiene para ajustar sus lentes, evidentemente intentando articular su idea de la mejor forma posible."

show shizu basic_angry
with charachange

shi "…"

show misha sign_smile
with charachange

mi "Si bien asumo que es lo mismo para ella, no puedo decir que mi opinión al respecto sea imparcial. Basta decir que éramos más cercanas antes que ahora."

show shizu behind_frown
show misha sign_confused
with charachange

"Shizune le hace un rápido gesto a Misha para que pare de interpretarla, y luego mantiene una breve reunión con ella antes de seguir."

"El hecho de que las dos puedan comunicarse tan fácilmente y a la vez en secreto frente a nosotros es un tanto desconcertante."

show hanako basic_normal
show shizu basic_normal2
show misha sign_sad
with charachange

"Hanako parece compartir mi curiosidad por la reunión, mirando con interés apenas disimulado. Cuando acaban su conversación encubierta, Misha parece un tanto desalentada. Supongo que su opinión al respecto no fue tomada en cuenta."

show misha perky_confused
with charachange

mi "Shicchan dice que deberías preguntarle a Lilly al respecto, ya que ella no quiere ser la que te involucre."

"Ah bueno. Tendré que preguntarle cuando regrese. Al menos saqué algo de información de Shizune; que las dos hayan tenido una relación cercana significa que no siempre estuvieron enfrentadas, o al menos no a este extremo."

hi "Entiendo. Gracias de todas formas."

stop music fadeout 8.0

show shizu invis at offscreenleft
show misha invis at offscreenleft
show hanako basic_normal at center
show bg school_scienceroom at center
with dissolvecharamove

"Con un gesto de cabeza y una despedida las dos se apartan y salen por la puerta, sin duda dirigidas directamente al salón del consejo estudiantil."

hi "… Podría haber sido peor, supongo."

show hanako cover_bashful
with charachange

"Hanako exhala profundamente, aliviada por el desenlace de la confrontación. No puedo decir que la culpe."

show hanako basic_bashful
with charachange

ha "¿Te veré luego, entonces?"

hi "Sí, te veré en el cuarto de té. Nos vemos."

hide hanako
with charaexit

"Con eso, ella se despide y se une al torrente de estudiantes saliendo del salón."

show muto normal at center
with charaenter

mu "¿Nakai, podría hablar contigo un momento?"

"Dicho en su típica monotonía. Aparentemente él decidió que ya era necesario que me recordara ir a verlo."

hide muto
with charaexit

"Eventualmente termino de guardar mis cosas. Para cuando llego a su escritorio el salón está prácticamente vacío."

hi "Ah… ¿Sí señor?"

play music music_happiness fadein 5.0

show muto normal at center
with charaenter

"Él levanta la mirada, juzgando mi rostro antes de soltar una extraña, y evidentemente actuada risa."

show muto smile
with charachange

mu "No tienes que sentirte culpable, no estás en problemas. Solo quiero preguntarte algo que ya le he preguntado a algunos otros estudiantes."

"Eso es algo, por lo menos. Por un momento pensé que mi máxima de mantener mi cabeza agachada y el bolígrafo levantado me había fallado."

hi "¿Entonces sobre qué quiere hablar?"

show muto normal
with charachange

mu "Para comenzar, ¿qué opinas de tu progreso en este grupo, hasta ahora? ¿Bueno? ¿Malo?"

"Detesto ese tipo de preguntas. Por un buen rato intento pensar en una respuesta que no sea patéticamente humilde, ni arrogante."

hi "Diría que voy bien. El trabajo no parece demasiado difícil, y me va mejor en los exámenes de lo que pensé que me iría."

show muto smile
with charachange

mu "Esa es una buena respuesta. Y también una correcta."

"Mentalmente suspiro aliviado por su satisfacción. Decir que no me siento un poco orgulloso de su comentario sería una clara mentira."

"En el remolino de pensamientos que nublaron mi mente después de saber que sería transferido a Yamaku, mis notas parecieron en absoluto insignificantes."

"Estando por completo a oscuras de qué nivel asumirían de mí, una vez que llegué aquí me sentí increíblemente aliviado cuando descubrí que entendía bastante bien el material de clases que estábamos viendo."

show muto normal
with charachange

mu "Sé que tus circunstancias podrían haber puesto un obstáculo en ello, pero ¿has pensado acerca de tu futuro?"

hi "¿Mi futuro?"

mu "Lo que te gustaría hacer como profesión. ¿Tienes alguna idea de dónde te gustaría estar en un lapso de diez o veinte años?"

mu "No me sorprendería que ya hayas tratado este tema en tu escuela anterior, pero si es así no tengo registros de ello."

"Supongo que el último año de la escuela es cuando los estudiantes deberían estar pensando en tales cosas. A decir verdad, en realidad no lo he pensado mucho, en comparación con mi situación más inmediata."

"Adivinando mis pensamientos, Mutou habla."

mu "Está bien si no has decidido nada en específico aún. No me sorprendería si muchos de tus compañeros todavía estuvieran indecisos, después de todo. ¿Quizás seguir uno de tus talentos?"

"Él está intentando sacarme una respuesta de forma bastante evidente, y algo en la forma que dijo lo anterior me hace sospechar."

"Pareciera no tener la intención de interrogar a todos de esta forma, así que debe tener algún criterio de selección. Probablemente, nuestros puntajes en su clase."

hi "Bueno, algo en ciencias podría ser el camino más fácil."

"Su rostro se ilumina, sin lugar a dudas contento con la idea de que un estudiante apreciado siga su materia como carrera."

show muto smile
with charachange

mu "Bien. Tener una idea general es el primer paso. Aunque te aconsejaría que pensaras al respecto."

hi "Lo haré. Las cosas están comenzando a asentarse, lo cual ayudará."

mu "Es bueno oír eso. Oh, y he notado que la asistencia y las notas de Ikezawa han mejorado desde que comenzaron a ser amigos. Me gustaría agradecerte por eso."

hi "Me sorprende que haya notado que nos conocemos."

"Él se ríe de forma tan extraña como su sonrisa."

"Este hombre de verdad no tiene idea de cómo interactuar correctamente con otros. Cada movimiento facial parece un acto de coreografía cuidadoso pero mal dirigido."

show muto normal
with charachange

mu "Se podría decir que tener una idea general de quién conoce a quién es parte del trabajo de un maestro."

"Deteniéndose antes de salirse por una tangente, tose fuertemente en su mano."

mu "Aunque estoy seguro de que tienes cosas que hacer, así que me detendré aquí. Por favor piensa hacia dónde quieres ir a partir de aquí, porque no queda mucho tiempo para terminar la escuela."

hi "Lo haré. Gracias."

stop music fadeout 4.0

scene bg school_hallway3
with locationchange

"Habiendo acabado la breve conversación, me retiro. Él vuelve a enfrascarse con los materiales en su escritorio."

"Esta es una de las veces que siento envidia de Lilly, casi enloquecedoramente. Tener su futuro tan claro y seguro, y aun así avanzar hacia él desde una edad tan temprana…"

"Es una idea tan completamente irreconciliable con mis propios pensamientos, atrapados en el presente como siempre lo han estado."

scene black
with dissolve



label es_L10:

scene bg school_lobby
with locationchange

"Atravesando el vestíbulo camino a la cafetería, lamento en silencio que mi rutina diaria se haya ido completamente por la borda."

"Parecía un día normal; llegué a clases antes que la mayoría, por haberme despertado temprano y haberme vuelto bastante hábil en tragarme las pastillas sin ahogarme mientras me preparo para el día."

"Pero a medida que los estudiantes comenzaron a entrar, una nunca se materializó. Hanako."

play ambient sfx_crowd_indoors fadein 0.5
scene bg school_cafeteria at right
show crowd at left
with locationchange

"Entro, mis ojos escrutando la extensión de la cafetería en busca de un lugar apropiado para sentarme. Es una tarea que se ve dificultada por los grupos de estudiantes moviéndose y platicando."

play sound sfx_impact2
with vpunch
$ renpy.music.set_volume(0.5, 0.3, channel="ambient")

hi "¡Geh!"

"Una mano golpea fuerte mi espalda un par de veces, dejándome sin aliento."

$ renpy.music.set_volume(0.0, 0.0, channel="ambient")
scene black
with shuteyefast

"No me podría importar menos el culpable al enfocar mis pensamientos en mi pecho en una reacción casi automática."

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

"Mi mano instintivamente se aferra a mi pecho, y comienzo a seguir los pasos que he practicado en mi mente cada día."

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

"Respira con calma… inhala… exhala…"

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)

"Con un grado de alivio, lentamente comienzo a sentir mi pecho menos tenso. Para cuando vuelvo a levantar la mirada, mi rostro está cubierto de sudor debido a la experiencia."

$ renpy.music.set_volume(1.0, 5.0, channel="ambient")

scene bg school_cafeteria at right
show crowd at right
show kenji happy_close at center
with openeye

ke "Qué tal… hombre, ¿estás bien?"

hi "¡MALDITA SEA! ¡No {b}hagas{/b} eso, idiota!"

show kenji tsun
with charadistant

"Él retrocede, una expresión de malestar aparente en su rostro. En retrospectiva, probablemente no debería haberle gritado, considerando que no tiene forma de saberlo."

"Suspiro y me enderezo con algo de dificultad."

hi "Disculpa. Es solo que tengo… problemas en el pecho. Los golpes fuertes no me hacen bien."

"Parece extraño verlo tan afectado. El hecho de que no pueda hacer nada al respecto me irrita."

hi "Almorcemos."

show kenji neutral
with charachange

ke "Está bien. Es bueno tener compañía, para variar."

hide kenji
with charaexit

show bg school_cafeteria at left
show crowd at left
with charamove

"Nos dirigimos a la fila. Algo positivo es que Kenji y yo podemos platicar hoy en día, a diferencia de cuando mi única interacción con él eran las charlas antifeministas."

hi "Parece que será difícil encontrar una mesa vacía."

show kenji neutral at center
with charaenter

ke "Hay unas cuantas personas con las que no me importaría sentarme. Aunque nadie es como tú."

$ renpy.music.set_volume(0.0, 0.5, channel="ambient")

"Siento un escalofrío recorrer mi espalda."

hi "Aclara eso ahora mismo."

play music music_kenji fadein 2.0

show kenji tsun
with charachange

ke "Ellos no escuchan. Sus mentes están cerradas. Son los medios, hombre, los malditos medios populares lava cerebros feministas fascistas."

"Él da un respiro, y yo saboreo el segundo de silencio."

$ renpy.music.set_volume(1.0, 10.0, channel="ambient")

ke "Maldición, controlan todo. Todo salvo a ti y a mí."

"Me relajo un poco cuando tomamos nuestra comida y bebidas."

show kenji happy
with charachange

ke "Entonces, ¿qué tienes para mí?"

hi "¿Eh?"

show kenji neutral
with charachange

ke "Vamos, has estado junto a Satou y esa otra chica ya por años. Los rumores abundan en mi grupo, y probablemente en algunos otros también."

hi "Espiar no es un buen hábito."

show kenji happy
with charachange

ke "Déjame adivinar, ¿tú nunca lo haces? ¿Ni siquiera cuando estás aburrido? ¿En serio?"

hi "Bueno… Yo… eh…"

hi "Bien. Lo entiendo."

hide kenji
with charaexit

"Ambos nos detenemos para que nos sirvan sopa en un par de pequeños tazones y los coloquen en nuestras bandejas. El brebaje que cae en los tazones se ve bastante cuestionable, pero al menos huele razonablemente bien."

stop ambient fadeout 1.0

show bg school_cafeteria at center
show crowd at Alphaout(1.0), center
show kenji invis at center
with charamove

show kenji neutral:
    ypos 1.14
hide crowd
with dissolvecharamove

"Cuando nos sentamos en una mesa milagrosamente libre, intento pensar en algo que de verdad le interese en absoluto. Espero que se me ocurra algún tema aceptable."

hi "Encontré una respuesta a la pregunta que me hiciste hace un par de semanas. De dónde viene la mitad no japonesa de Lilly, digo."

show kenji happy
with charachange

ke "Bien hombre. ¿Es Rusia, cierto? Sin duda Rusia."

hi "Escocia."

show kenji tsun
with charachange

"Él se detiene visiblemente por completo."

ke "… ¿Escocia?"

hi "Sí, esa también fue mi reacción. Puede hablar inglés con soltura y todo."

show kenji rage
with charachange

ke "… ¡Maldita sea! ¿Te das cuenta de lo que esto significa? ¿Lo aterradora que esta noticia es para mí?"

label es_choiceL10_1:
menu:
    with menueffect
    "Creo que se está hiperventilando. Desmayarse por un rato probablemente lo relaje más de lo normal."
    "Seguirle el juego.":


        return m1
    "Ignorar sus desvaríos dementes.":

        return m2

label es_L10a:

hi "No tengo idea de lo que significa. Ilumíname."

ke "¡Acabo de perder 1000 yenes, hombre! ¡1000 yenes! Maldición, este es el peor día de todos."

label es_L10b:

"Comienzo a comer, esperando que entienda la indirecta de mi silencio."

ke "¡Acabo de perder 1000 yenes, hombre! ¡1000 yenes! Maldición, este es el peor día de todos."

"No tengo tal suerte."

label es_L10c:

hi "Debes estar bromeando. ¿Hiciste una apuesta por su nacionalidad?"

show kenji tsun
with charachange

ke "Uno de los tipos en mi clase me estaba fastidiando al respecto. Compartí un poco de mi sabiduría, y él tuvo la audacia de decir que mi lógica estaba equivocada."

hi "¿Y qué pensaba él?"

ke "Eh, Alemania o algo así. No importa. Lo que importa son mis 1000 yenes."

show kenji rage
with charachange

ke "Maldición, el día fue arruinado gracias a ella. Qué perra."

show kenji tsun
with charachange

"Parece completamente devastado mientras se zampa varios cúmulos de su pastoso arroz empapado en soya. Solo tarda unos cuantos bocados antes de apuntarme con sus palillos, apuñalando el aire repetidas veces en revelación."

ke "¿Por… mm… qué… mm… querría… mm…?"

hi "¿Acaso tu madre nunca te dijo que no hablaras con la boca llena?"

"Me mira con saña antes de tragarse el resto de la comida que queda en su boca y tomar un trago de jugo. Es bastante feo."

"Recordando mi propia comida frente a mí, decido ponerme en la tarea de comerme de una vez la comida de la cafetería tan rápido como sea posible. Mientras más pronto lo haga, más pronto acabará la experiencia."

show kenji neutral
with charachange

ke "Entonces como decía,"

show kenji tsun
with charachange

ke "¿Por qué querría alguien vivir en ese lugar de todas formas? Digo, ¿qué tiene de interesante? Praderas con pasto. Eso es todo. Muchas, muchas praderas con pasto."

ke "Y hombres en falda."

"No sé qué es peor, esta comida o su visión del mundo. Puedo sentir mi rostro caer debido al peso combinado de ambos. No es que él lo note, o le importe."

hi "No es tan malo. ¿Por qué te importa tanto ella de todas formas? Solamente es la representante de tu clase, después de todo."

show kenji neutral
with charachange

"Él se ríe malévolamente. Si fuera alguien aparte de Kenji, me sentiría incomodado por cómo suena."

ke "Al fin he encontrado una grieta en la armadura de la legión feminista. Tardó un tiempo, pero confío en que con esto podremos derribar todo el sistema."

show kenji happy
with charachange

ke "Estoy por dejarte alucinando. ¿Estás listo?"

stop music fadeout 2.0

"Me desentiendo de sus desvaríos por un momento para terminar mi arroz y comenzar con la desagradable sopa. Una probada es suficiente para confirmar que está fría."

hi "Tan listo como podría estar."

show kenji happy
with charachange

ke "He confirmado que Lilly está en la mafia."

play music music_kenji

hi "¿Qué?"

show kenji neutral
with charachange

ke "De acuerdo, escúchame por un segundo, y te describiré la situación."

"Desearía poder hacer lo contrario."

ke "Lilly va por ahí, caminando por la calle luego de la escuela."

hi "No la estás acechando, ¿o sí?"

show kenji tsun
with charachange

ke "¡No! Maldición hombre, tengo instintos de supervivencia."

"Pero no dignidad, moral, ni estándares sociales…"

show kenji neutral
with charachange

ke "De todas maneras, como iba diciendo. El auto se detiene junto a ella, ¿y adivina quién sale? Un hombre con traje a rayas. Le hace señas, y luego los dos se van así como así. Te lo digo hombre, ella está bajo protección. Bajo. Protección."

"Un hombre con tr… oh. Puedo ver adónde va esto. Me toma esfuerzo no suspirar exasperado."

hi "Déjame adivinar; ¿este hombre era de estatura media, tenía una contextura moderadamente delgada, era rubio, parecía extranjero, y sonreía mucho?"

show kenji rage
with charachange

"Parece afirmativamente aturdido. Tomo ventaja del momento de silencio para tragarme rápidamente un sorbo de sopa fría."

show kenji tsun
with charachange

ke "Creo que eres más observador de lo que pensé."

show kenji neutral
with charachange

ke "Sí, he elegido bien."

"Él se ríe un poco, y asiente a sí mismo tan dramáticamente que parece cómico. No puedo distinguir si es intencional o no, y ese hecho me hace fruncir el ceño."

show kenji happy
with charachange

ke "Esto tiene ramificaciones importantes, sabes. Si de verdad tiene conexiones con gente como ellos, y somos cuidadosos con lo que hacemos con esta información, podríamos convertir esto en nuestra mayor arma contra el consejo estudiantil."

show kenji happy:
    2.0
    "kenji neutral" with Dissolve(0.5, alpha=True)
    3.0
    "kenji happy" with Dissolve(0.5, alpha=True)
    1.0
    "kenji neutral" with Dissolve(0.5, alpha=True)
    4.0
    "kenji tsun" with Dissolve(0.5, alpha=True)
    repeat

"Una vez que comienza a divagar en el campo de las conspiraciones, mi jugo de pronto se vuelve mucho más importante."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

nvl clear

window hide
nvl show dissolve

n "\n\n\n\nEscuchando a medias su discurso, mi mente se escapa hacia el tema de Lilly y su antipatía por Shizune."

n "El pasado entre ellas poco a poco se vuelve más coherente, pero ni siquiera estoy seguro de si debería conocer su pasado de esta forma. En definitiva, incluso si averiguo qué fue lo que pasó, realmente no parece asunto mío el ir e interferir."

n "… Maldición, el que no esté Lilly hace que mis pensamientos divaguen. Estoy notoriamente más aburrido y huraño sin su compañía, y lo mismo va para Hanako. Todo lo que hacemos durante el almuerzo es comer y jugar ajedrez."

n "Ahora que lo pienso, necesito ir a ver cómo se encuentra Hanako después de clases, también. Considerando su mejorada asistencia, me imagino que le ha surgido algo."

stop music fadeout 2.0
$ renpy.music.set_volume(1.0, 6.0, channel="music")

nvl clear

nvl hide dissolve

scene bg school_scienceroom
with shorttimeskip

play sound sfx_normalbell

window show

mu "¿Oh, Nakai?"

show muto normal at center
with charaenter

"Me detengo cuando apenas estoy por salir del salón, dándome media vuelta para encarar a Mutou. Está sosteniendo un par de hojas de ejercicios en las que trabajamos durante el día con su brazo largo y desgarbado."

show muto smile
with charachange

mu "¿Te molestaría entregarle estas a Ikezawa? Normalmente se lo pediría a una de las chicas, pero asumo que tú irás a verla."

"Por un momento, considero brevemente la posibilidad de que esa sea más que una predicción inocente. Aunque rápidamente desecho la idea, ya que es difícil pensar que él pueda actuar de forma tan maquiavélica. No es su naturaleza."

hi "Claro, no hay problema."

scene bg school_girlsdormhall
with locationskip

play music music_night fadein 1.0

"Caminando al pasillo de los dormitorios de chicas, pasan por mi mente varias ideas de por qué Hanako ha estado ausente. La más obvia de ellas es que es solo un simple resfriado."

"Dicho eso, puede que ni siquiera esté enferma. Ha pasado casi una semana desde que Lilly se fue, y a pesar de que ella al menos parezca normal, sospecho que se siente un tanto más insegura al respecto de lo que deja ver."

show bg school_girlsdormhall at right
with charamove

"Eventualmente llego al cuarto de Hanako, su sencilla puerta marrón separándonos. La posición de su cuarto junto al de Lilly es extremadamente conveniente, y probablemente una contribución importante a que se conocieran en primer lugar."

$ renpy.music.set_volume(0.5, 0.0, channel="sound")
play sound sfx_doorknock2

"Haciendo una mueca ante la idea que de esté enferma, golpeteo mis nudillos en la puerta."

"… Silencio. Escucho detenidamente si hay algún sonido de movimiento desde adentro, pero no puedo oír nada."

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_doorknock2

"Vuelvo a llamar a la puerta, un poco más fuerte."

"Aún no hay respuesta. Qué extraño."

$ renpy.music.set_volume(0.5, 0.0, channel="sound")
play sound sfx_dooropen

show bg school_girlsdormhall at center
with charamove

"Se abre una puerta atrás de mí. Una estudiante menor que yo con pecas y un tanto flaca que no reconozco sale por ella y es brevemente sorprendida por mi presencia."

label es_choiceL10_2:
menu:
    with menueffect
    "Chica" "Ah… hola."
    "Preguntar por Hanako.":


        return m1
    "Guardártelo.":

        return m2

label es_L10d:

"De hecho, este puede ser un encuentro bastante fortuito."

hi "Hola. Disculpa, ¿sabes si Hanako ha salido de su cuarto hoy o no? No parece estar respondiendo."

"Chica" "Ikezawa es Ikezawa. Que no responda a la puerta es completamente normal. Esa chica alta extranjera es la única persona con la que habla, después de todo."

"Ella se encoge de hombros antes de seguir caminando por el pasillo, teniendo asuntos mucho más importantes a los cuales atender que Hanako y yo."

"Su actitud despectiva me molesta."

"Hanako debe tener reputación de ermitaña; una reputación que no parece del todo inmerecida, al menos antes de que nos conociéramos."

label es_L10e:

hi "Qué tal. Lo lamento, no te preocupes por mí."

"Creo que la situación con Hanako debería ser mantenida lo más privada posible, por su bien. En realidad no sé nada sobre lo que le haya pasado, pero mi instinto me dice que lo que la aflige no es una enfermedad física."

"No necesita que haya rumores sobre ella. Por mucho que pueda dolerme pensarlo, probablemente prefiera mantener su categoría de miembro de la clase extrañamente ignorada a tener gente hablando a sus espaldas."

"Chica" "Como quieras."

"Con eso, ella se da la vuelta y sigue caminando por el pasillo sin pensarlo dos veces. Qué grosera."

label es_L10f:

show bg school_girlsdormhall at right
with charamove

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_doorknock2

"Rascándome la cabeza, hago un intento final para que Hanako responda cuando golpeo una última vez."

hi "Hanako, soy solo yo. Mutou dijo que te entregara algunas cosas."

"Por un rato, el intento parece tan poco fructífero como el anterior. Aunque justo antes de pasar las hojas por debajo de su puerta, puedo oír vibrar la manija."

play sound sfx_dooropen
with Pause(1.5)

show hanagown distant:
    xpos 1.0 xanchor 0.75
with charamoveinright

"Como la puerta se abre a medias, hago mi mejor esfuerzo para mirar a Hanako tan rápido como sea posible. Es una tarea hecha un tanto más difícil por su gran camisón ocultando buena parte de su cuerpo."

"Ella no parece enferma, o al menos no de forma inmediata. Para ser honesto, hubiera preferido eso a su expresión actual."

hi "Hola, Hanako. Mutou quería que te entregara esto, ya que no fuiste a clases hoy."

"Extiendo las hojas sueltas, las cuales ella toma con sus manos vacilando. La forma en que se mueve es extraña, carente de pensamiento, como si fuera algún tipo de autómata mecánico en lugar de un ser vivo."

hi "¿Estás… bien? Si te sientes enferma o algo, puedo traer al enfermero."

"Se siente casi detestable seguir un acto de “mejórate pronto” tan rutinario. Pero no puedo pensar en nada más que pueda hacer por ella."

show hanagown normal:
    xanchor 0.7
with dissolvecharamove

"Ella parece recuperarse un poco ante la idea… pero solo un poco."

show hanagown distant_blush
with charachange

ha "Estoy bien."

hi "De acuerdo."

stop music fadeout 6.0

with Pause(2.0)

hide hanagown
with charamoveoutright

play sound sfx_doorclose

"Sigue un silencio incómodo, el cual acaba eventualmente cuando ella asiente solemnemente como despedida y cierra la puerta. Toda la experiencia se siente irreal."

"Más que un tanto desanimado, vago de vuelta a mi cuarto y espero que ella se encuentre mejor mañana, a pesar de no saber exactamente qué es lo que le sucede."

scene black
with dissolve



label es_L11:

show bg school_girlsdormhall at right
with locationchange

"Una vez más, me encuentro frente a la puerta de Hanako tras otra de sus ausencias en clase sin explicación."

play sound sfx_doorknock2

"…"

play sound sfx_doorknock2

"…"

"Nada. Considerando que este es el segundo día consecutivo que ha estado así, estoy comenzando a preocuparme por ella."

"Reuniendo mi voluntad, decido intentar hacer que ella responda por última vez."

hi "Hanako, si no dices algo iré a traer al enfermero por ti."

ha "… Vete."

play music music_hanako fadein 10.0

"¿Q… Qué? Es difícil distinguir si su tono es de decepción, ira, o ambos. ¿Qué diantres puedo hacer para ayudarla, si ella ni siquiera quiere ayuda?"

"El mensaje es bastante claro. Sin embargo, simplemente no puedo dejarla así; solo sentada en su cuarto por días enteros."

"Frotando mi sien, pensativo, regreso a mi propia habitación para pensar en cómo proceder. Lo que se necesita aquí es racionalidad, y reaccionar exageradamente podría empeorar las cosas."

scene bg school_dormhisao
with shorttimeskip

"Escarbo cajón por cajón en mi escritorio, buscando dónde dejé ese maldito trozo de papel."

"Antes de irse, Lilly me dijo a qué número llamarla mientras estuviera en Escocia y lo anoté. Pero ahora que lo necesito, la maldita cosa está—"

"Ah. Aquí."

"Probablemente debí solo meterlo directamente en mi celular, ahora que lo pienso. Sin pensarlo más, marco los números y presiono ansiosamente el botón de llamada."

scene bg school_dormhisao_blurred
show phone mobile:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with locationchange
with Pause (0.5)

"El hecho de que el teléfono siquiera suene indica que por lo menos marqué el prefijo para llamar a Escocia bien. Nunca he realizado una llamada internacional antes, así que eso es un alivio."

"Eventualmente contestan el teléfono, una voz femenina que no reconozco al otro lado. Es probablemente la madre de Lilly."

$ renpy.music.set_volume(0.5, 0.2, channel="music")


mystery "{image=vfx/garbage.png} {image=vfx/garbage.png} Satou ¿{image=vfx/garbage.png}?"

"¿Inglés? Súbitamente encontrándome desprevenido, me doy cuenta de que no puedo entender lo que dice, sea por mi vocabulario limitado o su fuerte acento. Debí haber anticipado esto, dado que de acuerdo a Lilly, su madre es nativa escocesa."

"Sigo adelante con la esperanza de que ella sepa algo de japonés, considerando que es el idioma nativo de su hija."

hi "Eh, es Hisao Nakai… al habla…"

"Un entusiasta sonido de entendimiento puede ser escuchado al reconocer el idioma. Mi sentimiento de alivio es inmenso."

"Sra. Satou" "Ah, tú debes ser uno de los amigos de la escuela de Lilly, ¿correcto?"

"Aun así, su acento significa que me tengo que concentrar en lo que está diciendo."

hi "Sí, es correcto. Encantado de hablar con usted, Señora Satou."

"Sra. Satou" "¡Es tan gentil de su parte encontrar a alguien tan educado! ¡Lilly, querida, es para ti!"

"Su madre parece agradable, si acaso algo entusiasta dado lo mundano de la situación."

"Hay un pequeño silencio mientras Lilly se toma su tiempo para agarrar el teléfono. En la distancia, puedo distinguir a su madre regañándola juguetonamente por recién levantarse."

$ renpy.music.set_volume(1.0, 5.0, channel="music")

li "Hola, Lilly al habla."

hi "Suenas terrible."

"Ella hace un sonido en algún punto entre un animal muriendo y un bostezo."

"Lo que sí me acordé de revisar antes de hablar fue la zona horaria. Debería ser bastante tarde en la mañana por allá, así que realmente no tiene excusa."

hi "¿No te sientes bien?"

li "Solo cansada. ¿Qué hora es allá?"

hi "Casi es de noche. La escuela terminó por hoy no hace mucho."

hi "En serio no eres una persona madrugadora, ¿o sí?"

li "No necesito que tú también te burles de eso…"

"Me toma un poco de esfuerzo no reírme de su gruñido de dolor. Pobre chica."

hi "¿Cómo va todo por allá entonces, descontando las mañanas?"

li "Ha sido placentero. Después de no verlos por tanto tiempo, el solo tener una comida junto con mis padres es agradable."

li "Aunque puede que la piscina y el tamaño de la casa tengan que ver con eso también."

"Incluso si no están en Japón, por cómo suena su familia debe de ser bastante adinerada para vivir tan lujosamente."

li "¿Están bien las cosas contigo y Hanako?"

stop music fadeout 0.3

"Maldición, esperaba que ese tema no surgiera tan pronto."

"Me tomo un momento para intentar poner en orden el cómo exactamente describir la situación sin causarle preocupación indebida, pero ella se da cuenta de ello sin decir ninguna palabra."

play music music_moonlight fadein 2.0

li "Hanako no está bien, ¿o sí?"

hi "¿Cómo supiste?"

li "Porque hoy es su cumpleaños. Tenía la esperanza de que se hubiera puesto al menos un poco mejor después de conocerte, pero…"

li "¿Cómo está ahora mismo?"

hi "Faltó a la escuela ayer y parecía como fuera de sí cuando fui a verla. Hoy volvió a faltar, y simplemente me dijo que me marchara."

hi "En verdad no tengo idea de qué pensar de esto. ¿Ha pasado esto en el pasado? ¿Está relacionado con sus cicatrices de alguna forma?"

li "Desafortunadamente sí. Prácticamente lo mismo pasó el año pasado cuando su cumpleaños llegó."

li "Hasta donde puedo decir, es porque sus padres murieron en el accidente que causó sus cicatrices, y Hanako se culpa por sus muertes."

"Lo que dice parece tener sentido. Si se está culpando a sí misma en su cumpleaños, bien podría estarse lamentando incluso de haber nacido."

"Aunque el hecho de que Lilly parezca saber tan poco sobre ello, casi tanto como yo, es una sorpresa."

hi "Así que ese es también el porqué ella vive en los dormitorios de estudiantes. ¿Te ha dicho algo más sobre el accidente?"

li "Con lo cercanas que nos hemos vuelto… apenas me ha dicho algo sobre lo que sucedió. Lo que sé sobre ello son más que nada conjeturas."

"Ella suena deprimida, casi derrotada. Considerando el trauma por el que Hanako debió pasar, realmente no puedo culpar a Lilly por no saber. No obstante, de todas formas parece considerarlo una derrota personal."

hi "No te culpes, Lilly. Con todo lo que ella ha pasado…"

li "Lo sé. Gracias, Hisao. Disculpa por no poder serte más de ayuda."

hi "Está bien, solo tendré que pensarlo un poco más. Gracias, y que te diviertas en Escocia."

li "Ah, yo…"

hi "¿Hmm?"

li "No es nada. Gracias por cuidar de Hanako."

hi "… De acuerdo. Adiós."

li "Adiós."

stop music fadeout 4.0

"Y con eso, la línea queda en silencio."

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

"Entre el número aparentemente cada vez mayor de preguntas que no puedo responder, la más inmediata es qué iba a decir Lilly."

"Oh. Oh no."

"Soy un idiota. Ella debe haber pensado que la llamé para hablar con ella, pero solo pedí ayuda por Hanako."

"Aún más vergonzoso que ese pensamiento es el hecho de que tal estimación sea mayormente correcta."

"Bueno… primero lo primero. Por ahora, necesito por lo menos arreglar la situación con Hanako y asegurarme de que efectivamente esté comiendo bien."

show bg school_girlsdormhall
with shorttimeskip

"Los estudiantes que pasan ocasionalmente le lanzan miradas mal disimuladas al plato de comida que llevo a los dormitorios para mujeres."

"No es una comida como para dar orgullo, siendo simplemente un platillo instantáneo de microondas del minisúper, pero al menos debería llenarla."

show bg school_girlsdormhall at right
with charamove

"Eventualmente llego afuera de su cuarto, después de tener que apartar a un par de chicas que en broma intentaron llevarse la comida que me tomó tanto tiempo conseguir."

"Decido saltarme el golpear, ya que demostró ser una acción completamente inútil y es un tanto difícil hacerlo con mis manos ocupadas."

hi "Hanako, soy Hisao."

hi "Sé que estás escuchando. Traje algo de comida para ti."

"Silencio. Como esperaba."

hi "La dejaré junto a tu puerta. Por favor por lo menos cómetela, ¿de acuerdo?"

"Ya. He dicho mi parte. Ahora depende de ella."

show bg school_girlsdormhall at center
with charamove

"Bajando el plato, camino de regreso hacia mi habitación para comer mi cena."

with shorttimeskip

"Para cuando regreso al dormitorio de Hanako, ya ha pasado una hora."

"Afortunadamente, no hay nada junto a su puerta. Camino de vuelta al menos un poco más feliz por saber que ella está comiendo."

"Si tiene intención de pasar por esto sola, entonces ser capaz de ayudar, incluso si es solo de una forma tan mínima, es por lo menos algo."

scene black
with dissolve



label es_L12:

scene bg school_library_ss
with locationchange

play music music_pearly

"Me siento a leer en la biblioteca después de la escuela, pasando página tras página, apenas registrando las palabras escritas en cada una de ellas por el aburrimiento."

"Con mi mejilla apoyada en mi mano, no puedo evitar notar la sensación un tanto áspera contra mi palma. No me falta mucho para tener que conseguir una navaja."

"Desistiendo de leer, simplemente dejo caer mi cabeza sobre el libro frente a mí."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

nvl clear
nvl show dissolve

n "\n\n\nLas cosas se han calmado considerablemente desde que Hanako comenzó a asistir a clases de nuevo."

n "Cuando recién regresó a clases, no se dijo ni se hizo nada que no fuera parte de la rutina usual, y ha sido lo mismo desde entonces. Ninguno de nosotros deseó sacar el tema de su accidente, así que simplemente no tenía sentido seguirlo."

n "Y así pasaron unos cuantos días, la monotonía diaria continuando tal como antes."

n "Es normal que mi mente vague hacia otros lugares, y más importante aun, otras personas. El agujero con forma de Lilly en la vida diaria de Hanako y en la mía se ha vuelto bastante notorio desde hace un tiempo."

n "Me gustaría decir que esto me ha dado tiempo para refinar exactamente cuál es mi opinión con respecto a ella, pero por desgracia, no he tenido tal suerte."

n "No me ayuda el que muchos de los intentos de hacerlo me han conducido al problemático tema de Iwanako. Cada vez que mis pensamientos vagan en esa dirección, reflexivamente intento pensar en algo distinto."

$ renpy.music.set_volume(1.0, 2.0, channel="music")

nvl clear

nvl hide dissolve

window show

hi "Por qué tenía que suceder ahora…"

yu "Ah…"

show yuuko worried_up_ss
with charaenter

"Me doy vuelta y miro hacia la fuente de la dubitativa voz que viene desde atrás de mí."

hi "Ah, lo siento. No era mi intención molestar a alguien."

show yuuko worried_down_ss
with charachange

yu "No… es eso."

hi "Oh…"

"Miro alrededor del cuarto teñido de naranja, rápidamente dándome cuenta de lo tonta que debe haber sonado mi disculpa. En el tiempo que he estado pensando y vagando aquí, todos se han marchado ya."

hi "¿La biblioteca está cerrando?"

show yuuko neurotic_down_ss
with charachange

yu "Si no quieres irte, puedo mantenerla abierta un poco más. No es ningún problema."

hi "No te preocupes, debería marcharme de todos modos. Gracias."

show yuuko worried_down_ss
with charachange

"Mientras me levanto y comienzo a retirarme, siento los ojos de Yuuko taladrando mi espalda."

hi "¿Pasa algo malo?"

show yuuko worried_up_ss
with charachange

yu "Te ves deprimido. ¿Estás bien?"

"Yuuko nerviosamente juega con sus dedos mientras dice esto, insegura de si está sobrepasando sus límites o no. De verdad no puedo distinguir si está más preocupada por mi ánimo o por haberme molestado."

"Normalmente solo me encogería de hombros y le aseguraría que todo está bien, pero mi ánimo reflexivo se lleva lo mejor de mí. A pesar de ser parte del personal, ella en verdad no da aires de ser una autoridad como los otros."

hi "Es solo… Creo que la mejor forma de llamarlo sería problemas en las relaciones."

show yuuko worried_down_ss
with charachange

yu "Oh. Yo… no soy muy buena con ese tipo de cosas. Mi única relación terminó un tanto abruptamente."

show yuuko smile_down_ss
with charachange

yu "Pero, quiero decir, si quieres hablar al respecto, puedo escuchar. Eso creo."

"Ahora me siento un poco mal por sacar el tema. Sin embargo ella no es tan mayor, así que al menos tiene posibilidades de encontrar a otro compañero."

hi "No es como si estuviésemos en una mala situación en estos momentos. Hemos pasado muchos días juntos como amigos, a veces saliendo a hacer cosas… ese tipo de cosas."

hi "Pero estoy comenzando a querer hacer más por ella, conocer más sobre ella, y estar más con ella. Aunque no estoy seguro si de verdad es amor o no, y nuestra amistad tal como está es agradable."

show yuuko panic_up_ss
with charachange

yu "¡No deberías dejar que eso te detenga!"

show yuuko worried_down_ss
with charachange

yu "Ah… lo lamento."

show yuuko worried_up_ss
with charachange

yu "Cómo decir esto… eh…"

show yuuko neutral_down_ss
with charachange

yu "Creo que es agradable que tengas una buena amistad, pero eventualmente se acabará la escuela. ¿Crees que estarás bien sin saber si ello podría haber ido más allá después de que te gradúes?"

hi "Supongo que ese es el quid de la cuestión. De verdad no tengo idea de cuál es la respuesta a esa pregunta."

show yuuko worried_down_ss
with charachange

yu "Bueno, en eso no puedo ayudarte. Cuáles son tus sentimientos verdaderos es algo que tú tienes que decidir por ti mismo. Pero creo que si la amas, definitivamente deberías decir algo."

show yuuko smile_down_ss
with charachange

yu "Después de pensarlo con mucho detenimiento, decidí que a pesar de que mi relación no funcionó, sigue siendo mejor de esa forma que nunca haber sabido si podría haberlo hecho o no."

"Nunca esperé que Yuuko sonara tan sabia. Sin duda tiene sentido que, con más experiencia de vida que yo, ella tendría una mejor idea sobre esto."

"Aunque supongo que efectivamente no se respondió mucho, hablar con ella me ha ayudado a sacarlo de mi pecho, y no tengo dudas de que debería confesarme si de verdad me gusta Lilly."

"Suelto un suspiro con algo de frustración."

hi "Si tan solo leer tanto de verdad ayudara cuando se trata de situaciones como esta."

show yuuko closedhappy_up_ss
with charachange

"Ella suelta una risita femenina, la cual solo refuerza mi visión de ella como alguien distinto al personal de aquí."

stop music fadeout 9.0

nvl clear

window hide
nvl show dissolve

n "\n\n\n\n\n\nAl final, una vez más todo se reduce a qué pasará después de que se acabe la escuela."

n "Considerando lo que pasó antes de que viniera a Yamaku, se siente como si me pidieran seguir el ritmo a un grupo de corredores a pesar de haber comenzado una decena de metros detrás."

n "Es solo un motivo más para desistir del pasado. Lo último que necesito ahora mismo es verme envuelto en ello y sentir añoranza a la misma vez."

nvl clear
nvl hide dissolve

scene bg school_dormhisao_ss
with locationskip
window show

"Una vez más, me encuentro llamando a Lilly. Mi cuenta de teléfono va a ser horrible, considerando que es una llamada internacional."

"Pero lo vale. No solo quiero suavizar sus sentimientos de la última vez que llamé, sino que honestamente quiero volver a hablar con ella."

scene bg school_dormhisao_blurred_ss
show phone mobile:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with locationchange
with Pause (0.5)

"Cuando finalmente contestan el teléfono, reconozco fácilmente la voz al otro lado de la línea."


"Sra. Satou" "{image=vfx/garbage.png} {image=vfx/garbage.png} Satou {image=vfx/garbage.png}"

hi "<Hello, Mrs. Satou. May I… uh… speak…>"

"Maldición. Olvidé cómo seguía el resto. No es alentador olvidar tan pocas palabras, aun si no pasé mucho tiempo intentando memorizarlas."

hi "¿Podría hablar con Lilly, por favor?"

"Sra. Satou" "Hola de nuevo, Hisao. ¿Estás aprendiendo inglés por tu cuenta?"

hi "Solo un poco. No creo ser lo bastante bueno con los idiomas en general."

"Sra. Satou" "Oh, no digas eso. ¡Tu pronunciación era buena! Te pasaré a Lilly, espera solo un momento."

"Espero obedientemente mientras ella sale en busca de Lilly, el otro lado de la línea en silencio."

"Eventualmente una Lilly mucho más despierta que la última vez responde, siendo la hora allá pasado el mediodía."

play music music_comfort fadein 12.0

li "¿Hisao, estás ahí?"

hi "Sí, estoy aquí. Hola."

li "Buenas tardes. Disculpa por demorarme tanto, estaba afuera en el jardín."

hi "¿Jardinería?"

li "Desafortunadamente he descubierto que no soy buena en ello, así que simplemente huelo las flores. Creo que mis dedos lo aprecian más."

li "¿Supongo que Hanako se ha recuperado un poco?"

hi "Sí. Me aseguré de que comiera, y eventualmente se recobró. Gracias por la ayuda el otro día."

li "No creo que haya sido de mucha ayuda. Aunque lo principal es que ella se encuentre mejor."

hi "Cierto. ¿Entonces cómo va la vida por allá? Suena como si estuvieras viviendo en prácticamente una mansión."

li "Yo no la llamaría mansión…"

"“Pero es bastante grande” obviamente es lo que quiere decir, pero la modestia la detiene. Siento un poco de envidia, pero son sus vacaciones."

li "Aunque es una casa agradable para estar. Hay una playa cerca de aquí también, a la cual Akira le tiene un apego especial."

hi "¿Ella es nadadora?"

li "Me lleva constantemente allá para tener competencias de natación. Las cuales gana. Cada vez."

"Lilly no me da la impresión de ser muy atlética en absoluto, así que no ser hábil nadando parece lo suficientemente lógico."

"Lo más rápido que la he visto moverse es su comprensiblemente relajado paso durante sus caminatas hacia los suburbios colina abajo desde la escuela. Hace que la imagen de ella nadando sea difícil de imaginar."

hi "Las playas allá deben verse agradables. Deberían estar menos repletas que las que hay por aquí al menos."

li "En efecto, Akira dice que el área por aquí se ve hermosa porque está muy apartada de la ciudad."

"Me doy cuenta de lo que he dicho después de decirlo, pero no le molesta en absoluto. Aún es fácil olvidar que ella no puede ver cuando no está aquí, a pesar del tiempo que hemos sido amigos."

li "Dicho eso, el acento local a veces hace un tanto difícil la comunicación. Es un recordatorio constante de que esta no es mi casa."

"Si bien el hecho de que ella no considere la residencia de sus padres como su casa tiene sentido, hace que me dé cuenta de que en realidad no puedo responder si lo mismo va para mí."

"Graduarse de Yamaku está lo bastante lejos como para que sea difícil verlo objetivamente, y he pasado tanto tiempo en este pequeño cuarto. He llegado a aceptar el dormitorio como mi nuevo hogar sorprendentemente rápido."

hi "Supongo que eso sería difícil de tratar. ¿Lo que sabes de inglés va bien?"

li "Afortunadamente. Podré hablarlo con fluidez, pero estar en una posición donde tengo que usarlo a menudo ayuda a reducir mi acento japonés, así que ha sido una práctica útil."

li "¿Oí que estás intentando aprender inglés por tu cuenta?"

hi "Más como memorizar unas cuantas líneas, y fallar incluso eso. De verdad no sirvo para aprender otro idioma."

"Mi admisión de derrota consigue una risa divertida."

li "Yo creo que hay cosas que uno elige hacer en su vida, y también cosas que se eligen para que uno haga en su vida."

li "Puedes reconfortarte con el hecho de que eres mejor que yo en ciencias y matemáticas, al menos."

hi "Para lo único que me ha servido es para ser el estudiante estrella de Mutou…"

li "Yo no me preocuparía por eso. Son habilidades útiles para muchos trabajos, ¿cierto?"

hi "Eso es lo que él me dice. Su rostro definitivamente se encendió cuando dije que probablemente elegiría una carrera relacionada con cualquiera de las dos."

"Ambos compartimos una cálida risa por los eventos que nos han sucedido a ambos en lugares opuestos del mundo. Es agradable, y me recuerda a nuestras sencillas pláticas que nos hemos perdido desde que ella se marchó."

"Mientras ambos esperamos que el otro comience a hablar, decido seguir adelante con mis sentimientos. Puedo sentir mi garganta apretándose un poco."

hi "Nosotros… ah, yo… te extraño."

"El silencio al otro lado de la línea me dice que ella le ha tomado el peso que corresponde a las palabras, pero a medida que continúa no puedo evitar sentir más y más aprehensión."

"Afortunadamente el silencio acaba, casi tan rápido como comenzó."

li "Yo también te extraño, Hisao."

li "Adiós."

hi "Adiós, Lilly."

stop music fadeout 6.0

"Una vez más, se cuelga el teléfono; sencillamente sin nada más que añadir."

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

"Esa voz ligera, dudosa, casi tímida. Su tono cálido y suave… Me estaría mintiendo a mí mismo si fuera a decir que no reconozco este sentimiento por lo que es."

"Con pensamientos de Lilly bailando por mi mente, comienzo a anticipar su regreso. Hoy ha sido un día de lo más excelente."

scene black
with dissolve



label es_L13:

scene bg school_scienceroom
with locationchange

"Me siento escuchando otra de las extensas lecciones de Mutou, mi mente divagando lejos de lo escrito en el sucio pizarrón."

play music music_tranquil fadein 4.0

nvl clear

window hide
nvl show dissolve

n "\nDesde que llamé a Lilly, mi mente se ha visto atraída en dos direcciones. Ambas, en general, conducen a la misma conclusión; he comenzado a sentirme extrañamente separado de mi vida pasada."

n "Solamente ha pasado un mes y medio desde que llegué aquí, y sin embargo esta escuela se ha vuelto como un segundo hogar. He obtenido nuevos amigos y contactos, he logrado tomarle el ritmo al estilo de vida y a la cultura de la escuela, y me he acostumbrado a las mañas de mis compañeros."

n "Acostumbrarse a una escuela donde las discapacidades son la norma, en lugar de la excepción, sigue tomándome por sorpresa a veces cuando pienso en ello. La misma escuela habitada por víctimas de quemaduras, amputados, ciegos, sordos y toda la gama intermedia de discapacidades."

n "Si alguien me hubiera descrito esta escuela antes de venir, lo habría pasado por algo como salido de una imaginación hiperactiva. Incluso cuando recién llegué me sentí como los holandeses, llegando a esta nueva y extraña tierra por primera vez."

n "Es sorprendente lo rápido que uno puede acostumbrarse al ambiente en el que se ve forzado a vivir, de verdad. Y ahora hasta he encontrado a alguien que me tiene completamente enamorado. Qué vida más extraña."

nvl clear
nvl hide dissolve
window show

"Antes de que mi mente pueda vagar más allá, encuentro una página de papel con líneas deslizada bajo mi rostro distraído. La estridente y brillante tinta rosada sin lugar a dudas debe haber sido escrita por Misha."

window hide

show misha hips_grin_close at offscreenleft
with None

show misha hips_grin_close:
    xpos 0.1 xanchor 0.5
show bg school_scienceroom at left
with charamove


$ written_note(u"¡No estés tan aburrido, Hicchan! ¡Ya casi se acaban las clases! ¡Vacaciones de tres días!", text_args={"color":"#FF2AAA"})

window show

"Oh, cierto, tenemos el sábado y el lunes libre. No puedo quejarme de tener menos clases, supongo."

"Destapo mi bolígrafo y escribo rápidamente en la página antes de pasarla furtivamente de vuelta a ella, moviendo mis ojos hacia el frente de la clase de vez en cuando. Mutou sigue garabateando ecuaciones y fórmulas misteriosas en el pizarrón."

window hide

$ written_note(u"Me imagino que tienen algo planeado.")

show misha perky_smile_close
with charachange

window show

"Misha recibe el papel de vuelta y se encorva sobre él cómicamente, hasta para ella, con su lengua saliendo por el costado de su boca. ¿Habrá malinterpretado mi expresión como deprimida, y está intentando animarme?"

window hide

show misha sign_smile_close
with charachange

$ written_note(u"Trabajo del consejo estudiantil con Shicchan, por supuesto.", text_args={"color":"#FF2AAA"})

$ written_note(u"¿De seguro no seguirán desanimadas por eso?")

show misha hips_frown_close
with charachange

$ written_note(u"Pero Hicchan podría habernos ayudado, pobres y solitarias chicas.", text_args={"color":"#FF2AAA"})

$ written_note(u"Les daría una mano por hoy si no fuera a estar ocupado.")

show misha hips_grin_close
with charachange

$ written_note(u"¡Ooh, travieso travieso Hicchan!", text_args={"color":"#FF2AAA"})

$ written_note(u"Solo voy a recibir a Lilly junto con Hanako. No sé qué estará pasando por tu cabeza.")

show misha perky_smile_close
with charachange

$ written_note(u"¿Entonces Lilly ya volvió?", text_args={"color":"#FF2AAA"})

$ written_note(u"Claro, llega en el vuelo de la tarde con su hermana, así que volverá a clases la próxima semana.")

show misha hips_grin_close
with charachange

window show

"Cuando recibe la nota y comienza a escribir, alzo la mirada para ver una imagen poco grata."

stop music fadeout 2.0

show muto irritated behind misha at Alphain(1.0), Slide(0.8, 0.5, 0.6, 0.5, 1.0)
with Pause(0.5)

"Mientras intento desesperadamente llamar la atención de Misha en silencio, Mutou confiadamente avanza por los espacios que separan los pupitres del frente de la clase, su mirada decidida enfocada directamente en ella."

show misha perky_confused_close
with charachange

"Ella de pronto deja de escribir cuando la imponente figura proyecta una sombra imposiblemente larga sobre la página."

show misha sign_confused_close
with charachange

mi "Ah… Yo…"

"Él toma el trozo de papel en silencio y comienza a leer."

"Sudando copiosamente, rápidamente miro a mi alrededor hacia la clase, notando su completo silencio. Por supuesto, tenía que ser la única cosa que de verdad recibe su atención durante la clase."

play sound sfx_impact
show misha perky_sad_close
with vpunch

"Después de unos escasos segundos examinando la página, él enrolla el papel como tubo pequeño y le da un suave coscorrón en la cabeza a Misha con eso."

show muto normal
with charachange

mu "Media hora hasta que puedas irte al consejo estudiantil. Creo que puedes aguantar hasta entonces."

play music music_ease

"El rostro de Misha se viene abajo mientras que la clase entera estalla en carcajadas. Podrá ser extraño, pero sabe cómo tratar con ella de forma excelente."

"Probablemente sentiría lástima por ella si no estuviera ocupado callando mi propia risa."

scene bg hosp_ext at right
show hanako basic_distant_cas at center
with shorttimeskip

play ambient sfx_rooftop fadein 2.0

ha "Hisao, ¿es ese?"

hi "No, creo que esa es una aerolínea extranjera."

"Y así, la tercera aeronave en la que ellas no están aterriza."

"Durante la última media hora hemos estado pasando el tiempo con pequeños fragmentos de plática sin sentido. El vuelo de Lilly y Akira se ha demorado, y a este paso posiblemente será de noche antes de que su vuelo llegue."

show hanako def_worry_cas at twoleft
with shorttimeskip

ha "¿Es ese otro?"

hi "No, no son los colores de la compañía."

show hanako basic_distant_cas
with charachange

show hanako basic_normal_cas
with charachange

"Los ojos de Hanako se mueven de izquierda a derecha, siguiendo el flujo de las personas que entran y salen por la enorme puerta de vidrio frente a nosotros."

"Afortunadamente nadie le pone mucha atención, aparentemente más atentos en asuntos más importantes."

show hanako emb_timid_cas at tworight
with shorttimeskip

ha "¿Quizás ese lo sea?"

hi "No, creo que ese… espera un minuto, creo que ese podría ser después de todo."

show hanako cover_distant_cas at center
with shorttimeskip

"Toma un poco más de tiempo para que la pantalla cambie el estado de su vuelo a “desembarcando”."

"Un bostezo sonoro se me escapa, sin darme tiempo suficiente para contenerlo. Mis horarios de sueño, una vez más, se han desajustado; posiblemente debido a una mezcla de preocupación por Hanako y los efectos secundarios de mis medicamentos."

show hanako emb_smile_cas
with charachange

ha "Hisao, por allá…"

"Miro a Hanako, y luego sigo su mirada hacia la puerta del aeropuerto."

aki "¿Hmm? ¡Oh, Lilly, ahí están!"

li "¿De verdad?"

show akira basic_smile:
    xanchor 0.5 xpos -0.3
show lilly basic_cheerful at offscreenleft
with None

show akira basic_smile at left
show lilly basic_cheerful_cas:
    xanchor 0.5 xpos 0.4
show hanako emb_smile_cas at tworight
show bg hosp_ext at center
with charamove

"Todos nos llamamos saludándonos, moviéndonos rápidamente a un costado para evitar bloquear el paso de los demás."

ha "¡Lilly!"

show hanako emb_downsmile_cas at center
with dissolvecharamove

"Hanako salta hacia adelante para abrazar a Lilly, sin bastar más que la sonrisa en su rostro para ver su felicidad por el regreso de Lilly. Lilly simplemente sonríe como respuesta, con voz suave."

show lilly basic_smileclosed_cas
with charachange

li "Es maravilloso volver a encontrarnos, Hanako."

show akira basic_smile at twoleft
show lilly basic_smileclosed_cas:
    xpos 0.6
show hanako emb_downsmile_cas at tworight
show bg hosp_ext:
    xpos 0.55
with charamove

"Mientras las dos se dan un abrazo, bien merecido luego de todo lo que ha pasado mientras ella no estaba, me doy la vuelta hacia Akira."

show akira basic_ending
with charachange

aki "Hola."

hi "Llegan bastante tarde."

show akira basic_annoyed
with charachange

aki "Cierto, había una tormenta bastante fuerte sobre el aeropuerto. Quedamos empapadas solamente con ir del auto a la puerta."

hi "Entonces supongo que aprecias más el clima de acá. Bienvenida tú también, Lilly."

stop music fadeout 4.0

show hanako basic_smile_cas:
    xpos 0.8
show akira basic_smile
show lilly basic_weaksmile_cas
with dissolvecharamove

"Hanako se separa de Lilly cuando hablo. Por un buen rato, ninguno de los dos dice palabra alguna."

"Al contrario de cómo pensé que su regreso a casa sería, el ambiente se siente incómodo, casi agobiante. Ambos intentamos adivinar los sentimientos del otro, sin estar del todo seguros de lo que deberíamos decir."

"Maldición. Esto es exactamente lo que me temía cuando pensé en intentar hacer avanzar las cosas entre nosotros."

"Lilly pasa su mano por su rubio cabello y se retuerce uno de sus flequillos incómodamente, claramente intentando pensar en cómo reaccionar mejor."

"Por suerte, eventualmente, Lilly suelta un suspiro ligero e interrumpe el silencio."

show lilly basic_smile_cas
with charachange

play music music_lilly fadein 6.0

li "Gracias, Hisao. Es bueno estar de vuelta."

show hanako basic_worry_cas
with charachange

ha "¿Estás bien? Pareces cansada."

"Evidentemente sin haberse recuperado del todo bien, ella rápidamente mueve su mano frente a su rostro para evitar cualquier preocupación que Hanako pueda tener por ella."

show lilly basic_weaksmile_cas
with charachange

li "Estoy bien, de verdad. Es solo que el cambio de horario me ha afectado un poco."

show akira basic_laugh
with charachange

aki "Débil."

hi "¿Tú no tienes?"

show akira basic_ending
with charachange

"Ella simplemente sonríe de oreja a oreja, hinchando su modesto pecho."

aki "¡Me siento absolutamente bien!"

show lilly basic_sleepy_cas
with charachange

li "Eso no es justo…"

show akira basic_smile
show hanako basic_normal_cas
with charachange

aki "Jaja, ah bueno. No debería tomarte mucho librarte de eso."

show lilly basic_smile_cas
with charachange

li "¡Ah! Es cierto, ¿Hisao?"

hi "¿Sí?"

show lilly basic_smileclosed_cas
with charachange

li "¿No tenemos vacaciones de la escuela pronto?"

hi "Me habría olvidado si Misha no me lo hubiera recordado esta mañana. Tenemos un fin de semana de tres días a partir de mañana."

show akira basic_laugh
with charachange

"Akira alegremente golpea con su codo suavemente el costado de Lilly, sonriendo."

show akira basic_smile
with charachange

aki "Te dije que no te lo perderías."

hi "¿Tienes algo planeado?"

show lilly basic_smile_cas
with charachange

li "Si ni tú ni Hanako están ocupados…"

hi "No tengo planes, así que algo que hacer sería apreciado. ¿Hanako?"

show hanako basic_smile_cas
with charachange

ha "No, nada."

show lilly basic_cheerful_cas
with charachange

li "Eso es bueno. Pensaba que podríamos ir a la casa de verano de mi familia por un poco de paz durante el descanso. Aunque no la hemos usado mucho últimamente, así que tendremos que desempolvar un poco las cosas mientras estemos allá."

hi "¿Oh? ¿Dónde queda?"

show akira basic_ending
with charachange

aki "Hacia el norte, en Hokkaido. El lugar está prácticamente deshabitado, así que debería ser un descanso agradable y tranquilo para ustedes."

hi "¿Tú no vienes?"

show akira basic_smile
with charachange

aki "Nah. Tengo unas pequeñas vacaciones propias planeadas con mi novio."

"Bajo mis ojos hacia ella, sospechando de sus intenciones."

hi "Suena como si solo fuéramos a limpiar la casa de verano para ti."

show lilly basic_displeased_cas
with charachange

li "Esa es… quizás una conclusión válida…"

"Ambos nos centramos en Akira, su rostro un tanto evasivo. Parece que estábamos en lo cierto."

show akira basic_boo
with charachange

aki "Eso es solo un bono conveniente. En serio. El tipo y yo la dejamos en una condición bastante buena la última vez que estuvimos ahí, lo juro."

show akira basic_smile
with charachange

aki "Bueno entonces, me largo de aquí."

show lilly basic_reminisce_cas
with charachange

li "¿Tan pronto? Akira…"

"Ella rápidamente se da la vuelta y se aleja caminando, su mano en alto."

show akira basic_laugh
with charachange

aki "Nos vemos en unos cuantos días, chicos."

show akira basic_laugh at Alphaout(1.0), offscreenleft
with charamove

hide akira
with None

show lilly basic_reminisce_cas:
    xpos 0.4
show hanako basic_smile_cas:
    xpos 0.6
show bg hosp_ext at bgleft
with charamove

"Lilly y yo solo podemos suspirar ante su retirada presurosa."

show hanako cover_bashful_cas
with charachange

ha "Suena como un lugar agradable al cual ir."

show lilly basic_smileclosed_cas
with charachange

"Lilly asiente con entusiasmo, llevando su maleta en una mano y colocando la otra sobre el hombro de Hanako para guiarse a medida que comenzamos a dirigirnos hacia el área de taxis."

"Luego del alboroto de estos últimos días, pasar un fin de semana en el campo solo con ella y Hanako suena como un sueño."

"Mientras más pienso en ello, más seguro estoy. Este será el lugar y el momento indicado para confesarle mis sentimientos."

stop music fadeout 2.0
stop ambient fadeout 2.0

scene black
with dissolve



label es_L14:

scene bg city_station
with locationchange

play music music_daily fadein 7.0

"El frío matutino cubre mi cuerpo tembloroso. Exhalo sobre mis manos ahuecadas para intentar desesperadamente detener el frío mientras esperamos en la plataforma de la estación."

"Las ropas de Lilly no parecen bastante apropiadas para la temperatura a nuestro alrededor. Solo puedo esperar que sea un indicio del clima que ella espera que haya en nuestro destino."

show lilly basic_sleepy_cas at twoleft
show hanako basic_distant_cas at tworight
with charaenter

hi "Rayos, Lilly, ¿por qué teníamos que llegar aquí tan temprano?"

show lilly basic_displeased_cas
with charachange

li "Desafortunadamente el horario del tren jugó en nuestra contra. El próximo tren a Hokkaido pasa a las dos de la tarde."

hi "Genial. Simplemente genial."

"Me detengo un momento para frotarme los ojos y despertar, y Lilly prestamente toma ventaja de la oportunidad."

show lilly basic_weaksmile_cas
with charachange

li "Anímate, Hisao. Una vez que lleguemos allá, será mucho más cálido."

hi "¿Por qué no simplemente tomar el tren bala? Un tren normal va a demorarse horas en llevarnos allá, así que bien podríamos tomar la línea Shinkansen tan al norte como llegue, y solo hacer un transbordo al final."

show lilly basic_smile_cas
with charachange

li "Los trenes antiguos tienen cierto encanto, ¿no estás de acuerdo?"

hi "Estaría de acuerdo si no me estuviera congelando con el frío matutino porque decidimos tomar uno."

show hanako emb_timid_cas
with charachange

ha "Lo… siento, Hisao."

hi "¿Lo sientes? ¿Por qué?"

show hanako emb_downtimid_cas
with charachange

ha "Fui yo… la que sugirió tomar un tren normal."

"Vaya forma de hacerme sentir culpable. Lo único que puedo hacer es suspirar y cubrir mi rostro con mi mano."

hi "Está bien, solo estoy refunfuñando."

show lilly basic_ara_cas
with charachange

li "Vaya vaya, Hanako, no necesitas cargar con toda la culpa tú sola. Incluso sin tu sugerencia, yo aun así habría optado por lo mismo."

show hanako emb_smile_cas
with charachange

hide hanako
hide lilly
with charaexit

"Agradecido por la rápida intercepción de Lilly, doy un breve vistazo por la estación."

"Aparte de nosotros, la plataforma del tren está desierta, la niebla matutina asentándose en los bancos vacíos. Supongo que nadie más fue lo suficientemente masoquista para aguantar la mañana tan temprana."

"Aunque si alguien lo fuera, entonces habría más que notado las enormes maletas que tanto Lilly como Hanako trajeron con ellas."

hi "¿Pero qué tenían que empacar en esas cosas, de todas formas?"

show lilly basic_listen_cas at center
with charaenter

li "¿Las maletas? Hmm…"

"Ella se detiene un momento e inclina su cabeza de forma pensativa."

show lilly basic_smileclosed_cas
with charachange

li "Un cambio de ropas, impermeable, ropa de dormir, algunos libros… Creo que eso es la mayor parte."

hi "Lo haces sonar como si yo no estuviera preparado."

show lilly basic_surprised_cas
with charachange

li "¿Trajiste menos?"

hi "Ropa interior y un juego de cartas. Eso sería todo."

"Y mis medicamentos, pero no importa eso."

li "¿Sin ropa de dormir?"

hi "Maldición. Sabía que olvidaba algo."

"Mientras alboroto mi pelo de frustración, Lilly suspira."

show lilly basic_weaksmile_cas
with charachange

li "Debe haber ropa que puedas usar allá. Akira todavía va allí ocasionalmente, después de todo, y creo que algo de la ropa de nuestros padres todavía está guardada."

show lilly basic_smile_cas
with charachange

li "No creo que haya problema con que tomes prestado un juego de ropa de dormir, si lo necesitas."

hi "Gracias. De todas formas, no me importa dormir con mi ropa normal."

show lilly basic_surprised_cas
with charachange

li "¿Por dos días?"

hi "Buen punto."

"Realmente no. Aunque dos días sería un caso límite, es más el hecho de que verse aunque sea un poco como un vago sería inaceptable en la presencia de dos chicas."

hide lilly
with charaexit

"Mientras hablamos sin prisa en la plataforma de la estación suena un aviso por los parlantes, anunciando con un fuerte volumen la llegada de nuestro vehículo."

"Aunque, mirando por sobre Lilly y Hanako, el tren aún está fuera de nuestra vista. Una rápida mirada a mi reloj basta para ver que es el que tenemos que abordar."

hi "El tren de las cinco treinta era el nuestro, ¿cierto?"

show lilly basic_smileclosed_cas at twoleft
show hanako basic_distant_cas at tworight
with charaenter

li "Correcto."

hi "¿Alguna de ustedes quiere que lleve sus maletas? La mía no es precisamente pesada."

show lilly basic_ara_cas
with charachange

li "Vaya vaya, qué caballeroso de tu parte, Hisao."

hi "Vamos, no acepten a regañadientes."

"Cuando me agacho para tomar la gran maleta de Lilly, levanto la mirada para ver a Hanako tomando la de ella."

hi "¿Estás bien con eso?"

show hanako basic_normal_cas
with charachange

"Asiente en silencio como única respuesta. Estoy comenzando a sentir que para cuando acabe el viaje, seré capaz de contar cada frase suya con una mano."

stop music fadeout 5.0
play ambient sfx_trainint fadein 5.0

$ ksgallery_unlock("ev lilly_trainride")
scene train_scenery
show train_scenery_fg
show evfg lilly_trainride at train_shake
with shorttimeskip

"Con el paisaje matutino pasando por la ventana y el ocasional traqueteo del tren moviendo el carro, intento concentrar mi atención en las avejentadas cartas que hay en mis manos."

hi "La alzo en cinco."

ha "Ah… yo…"

"Ella frunce su rostro y se inclina hacia Lilly de forma conspiradora, ambas intercambiando palabras susurradas. Considerando lo mucho que esto ha pasado hasta ahora, estoy comenzando a dudar del manejo de Hanako sobre el póquer."

"Aunque no parece molestar la lectura de Lilly, sus manos revoloteando sobre cada página con solo la ocasional corrección para compensar los movimientos y saltos del tren."

"Mi colección de piezas de ajedrez que estamos usando como fichas crece consistentemente de todas formas, así que en realidad no me preocupa."

"Mirando a nuestro alrededor, nuestro vagón está casi tan vacío como la plataforma de la estación en la que esperamos por el tren mismo. Solo un puñado de personas pueden verse, la mayoría parecen turistas o parejas de vacaciones."

"Mientras las dos continúan planificando su estrategia de forma menos que clandestina, un niño pequeño mira sobre su asiento y fija sus ojos en mí. Esperando que no comience a observar a Hanako, simplemente le saludo con la mano y sonrío."

"Afortunadamente, vuelve a ocultarse tras su asiento después de encontrarme demasiado aburrido para desperdiciar su atención."

ha "Acepto y la alzo en… otros cinco."

hi "Maldición, me atrapaste. Me retiro."

"Estaba fingiendo, y ella me atrapó. Dejando caer mi cabeza, aparto una gran porción de mis ganancias."

$ ksgallery_unlock("ev lilly_trainride_smiles")
show evfg lilly_trainride_smiles at train_shake
with charachange

"Hanako parece absolutamente encantada, e incluso si Lilly mantiene su atención enfocada en su material de lectura, puedo ver una sonrisa en su rostro. Ambas están extremadamente satisfechas."

"Por un momento intento adivinar lo que está leyendo Lilly, pero la portada está demasiado gastada para leerla más allá del hecho de que hay letras latinas en ella. Una lástima que no pueda leer el braille sobre el título impreso."

hi "¿Qué estás leyendo, Lilly? Parece como si el título estuviera en inglés."

li "Así es. Es “And Then There Were None”, una vieja historia británica. Podría leértela si quieres."

"Ella extiende la oferta con una sonrisa, claramente en broma."

hi "Creo que pasaré, gracias."

stop ambient fadeout 2.0

scene bg hok_houseext at Fullpan(10.0, dir="left")
with shorttimeskip

play music music_tranquil fadein 3.0
play ambient sfx_parkambience fadein 4.0

"Luego de un viaje aparentemente interminable, finalmente llegamos a la tierra prometida de la casa de verano de los Satou. Aun después del viaje en tren, la caminata pareció tomar una eternidad."

"Pero a pesar de mi refunfuño, nunca habría imaginado la vista que nos esperaría una vez que pasáramos por ese largo camino abandonado."

"Parece más una casa de campo que la casa cotidiana que me había imaginado, de tamaño pequeño y rodeada de árboles y arbustos."

"Cuando avanzamos podemos ver una vacía extensión de campos de trigo y tierra de cultivo, las cercas simplemente hechas de destartaladas tablas de madera."

"De verdad remarca lo lejos que estamos de las ciudades principales, y es una vista que se siente antitética al ambiente en el que crecí."

"Lo único que no me sorprende es el estilo occidental."

show bg hok_houseext at left
with None

hi "Vaya, este lugar es sorprendente…"

show lilly basic_smileclosed_cas at twoleft
show hanako basic_bashful_cas at tworight
with charaenter

ha "Mm, es maravilloso."

show lilly basic_smile_cas
with charachange

li "Es bueno oír eso. Aunque Akira haya dicho que mantuvo la casa en una condición razonable, me preocupaba que pudiéramos tener un estándar distinto de lo que es “razonable”."

hi "Pareciera que no hay otra alma en kilómetros. Pensé que Akira era de las que prefieren quedarse en la ciudad."

show lilly basic_listen_cas
with charachange

"Lilly frunce el ceño pensativa, aparentemente recordando algo casi olvidado."

show lilly basic_weaksmile_cas
with charachange

li "Hmm, por lo que recuerdo hay un pueblo pequeño no muy lejos. Pero además de eso, esto es principalmente viejos campos de cultivo."

show lilly basic_smile_cas
with charachange

li "Akira y yo nos quedamos por un tiempo en la casa de nuestros padres que estaba en la ciudad más cercana, pero después de que se fueron decidimos mudarnos a una casa más pequeña y más fácil de mantener."

hi "Encontrar un lugar como este en Japón hoy en día… es un tanto anacrónico."

show lilly basic_smileclosed_cas
with charachange

li "Bueno, este pueblo tiene bastante historia."

"Vuelvo la mirada hacia la calle por última vez antes de regresar a la tarea actual."

hi "¿Entramos, entonces? Estoy sediento."

show hanako basic_normal_cas
with charachange

ha "Fue una larga caminata para llegar aquí."

show lilly basic_smile_cas
with charachange

"Lilly asiente de forma entusiasta, nosotros tres cargando nuestras maletas hasta la casa."

stop ambient fadeout 1.0
$ renpy.music.set_volume(0.7, 1.0, channel="music")

scene bg hok_lounge
with locationchange

"Tan pronto como pisamos adentro, Hanako y yo comenzamos a mirar a nuestro alrededor, observando cada detalle de dónde nos estaremos quedando durante los próximos días."

"Todos los artefactos de la vida de otro detenidos en pleno movimiento desperdigados por la casa, tales como una guía de televisión junto al mostrador sobre el cual estaba, y ollas en la cocina adjunta todavía sobre el horno."

"Es una sensación extraña, de verdad; como si estuviéramos entrando en la vida de Akira por un breve momento, antes de marcharnos en un par de días tal como llegamos."

"Por supuesto, la realidad más mundana es que ella simplemente no ha limpiado muy bien lo que ha dejado."

hi "¿Dónde deberíamos dejar nuestras maletas?"

show lilly basic_smileclosed_cas at twoleft
show hanako basic_normal_cas at tworight
with charaenter

li "Le mostraré a Hanako nuestro dormitorio. Puedes dejar las tuyas acá, si quieres."

hi "¿Eso significa que no estaré en el mismo dormitorio que ustedes dos?"

show hanako emb_blushing_cas
show lilly basic_emb_cas
with charachange

"Hanako se ruboriza por completo mientras que Lilly sostiene su mejilla con su mano."

show lilly basic_ara_cas
show hanako emb_emb_cas
with charachange

li "Oh vaya, qué atrevido."

"Ustedes dos…"

hi "Un momento, si voy a dejar mis maletas aquí, ¿dónde dormiré?"

show lilly basic_weaksmile_cas
with charachange

li "Bueno, viendo que nos falta un dormitorio para invitados…"

hi "El futón convertible, ¿eh?"

show lilly basic_concerned_cas
with charachange

li "Lo lamento, Hisao."

"Suspiro, lamentando mi lugar en el peldaño más bajo de las prioridades de lugares para dormir."

hi "Supongo que no hay otra opción."

hide lilly
hide hanako
with charaexit

"Lilly se marcha para mostrarle a Hanako su dormitorio, así que doy un pequeño recorrido por mis alrededores luego de dejar mi maleta en el suelo."

scene bg hok_kitchen
with locationchange

"La cocina, tal como la sala de estar, es bastante modesta. La naturaleza rústica de los muebles de madera reitera lo lejos que estamos de la civilización."

scene bg hok_lounge
with locationchange

"Regresando a la sala de estar, decido ver la televisión hasta que ellas vuelvan. Con un toque del control remoto esta inmediatamente cobra vida, puesta aparentemente en un canal de noticias."

"Casi dejándome caer de cansancio en lugar de sentarme, me recuesto y la miro."

stop music fadeout 5.0
$ renpy.music.set_volume(1.0, 8.0, channel="music")

"Y miro."

"Y miro…"

window hide

scene black
with shuteye

with Pause(4.0)

window show

ha "Hisao…"

play ambient sfx_cicadas fadein 5.0

scene bg hok_lounge_ni
show lilly basic_smileclosed_cas at twoleft
show hanako basic_normal_cas at tworight
with openeye

"Rápidamente pestañeo para despertarme, Lilly y Hanako habiendo regresado sin sus maletas."

"Por el cielo nocturno de Hokkaido visible por la ventana, parece que me quedé dormido. Viendo el reloj montado en la pared, ya son las diez."

show lilly basic_weaksmile_cas
with charachange

li "Entonces ya has encontrado la televisión."

hi "Sí. De verdad este lugar se siente agradable y hogareño."

show lilly basic_smile_cas
with charachange

li "Me alegra que te guste."

show lilly basic_giggle_cas
with charachange

li "Ya estabas ido cuando regresamos luego de desempacar nuestras cosas, así que no tuvimos las ganas de despertarte antes."

"A juzgar por su risita, debo sonar gracioso cuando duermo. Rápidamente decido no preguntar."

show hanako emb_smile_cas
with charachange

ha "Hay un poco de cena esperándote en la cocina…"

show hanako emb_downtimid_cas
with charachange

"Hanako bosteza marcadamente, apenas recordando tapar su boca en el último segundo."

show lilly basic_weaksmile_cas
with charachange

li "Vaya vaya, ¿estás cansada?"

show hanako emb_timid_cas
with charachange

ha "Ah, mm. No dormí mucho anoche."

hi "Yo también estoy bastante agotado. Fue una larga caminata hasta aquí, y se está haciendo tarde."

show lilly basic_smileclosed_cas
with charachange

li "Si ese es el caso, supongo que deberíamos retirarnos por el resto de la noche. Buenas noches, Hisao."

show hanako basic_smile_cas
with charachange

ha "Buenas noches."

hi "Buenas."

hide hanako
hide lilly
with charaexit

"Con eso, ellas se dan la vuelta y regresan a su dormitorio tranquilamente."

"Frotando mis ojos, suspiro. Me pregunto si podré volver a dormir después de ser despertado."

"Supongo que comeré algo y veré algo más de TV en silencio antes de acostarme."

stop ambient fadeout 2.0

scene black
with dissolve



label es_L15:

scene black
with dissolve

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_parkambience fadein 6.0

ha "¿Sigue dormido?"

li "Eso creo."

"No lo estoy. Estoy, sin embargo, increíblemente cansado."

ha "Ya es casi mediodía…"

"Eso ya lo sé."

li "Posiblemente se haya quedado despierto para ver televisión. Lo podía oír desde nuestro dormitorio."

"Solo porque no podía quedarme dormido."

ha "¿Deberíamos despertarlo?"

"No hagas eso, Hanako. Por favor."

li "No, deberíamos dejarlo. Dudo que quiera ser despertado temprano si no pudo dormir bien por la noche."

"Gracias, Lilly."

li "Además, suena tan tranquilo. Sería una lástima despertarlo cuando está así."

"Mantén la expresión firme, Hisao. Aunque es lindo que a ella le importe tanto."

ha "Ah…"

li "Hanako, ¿podrías ir al refrigerador y sacar lo que se necesita para el almuerzo?"

ha "De acuerdo, ¿solo los vegetales y el arroz?"

li "Mm, eso debería ser suficiente. Solo necesitamos algo simple, ya que podemos comer en el pueblo más tarde."

"Se pueden oír los pasos de Hanako en el piso alfombrado, alejándose de la sala de estar. A medida que lo hacen, siento la mano de Lilly posándose gentilmente en mi pecho."

"Me toma un esfuerzo titánico no reaccionar, pero algo en ella me hace pensar que sabe que estoy despierto."

"Sigue un largo silencio."

"El único pensamiento en mi mente es que hay una mano extendida gentilmente posada sobre mi pecho. Luego de una cantidad indistinguible de tiempo, Lilly retira su mano."

li "Buenos días, Hisao."

$ renpy.music.set_volume(1.0, 3.0, channel="ambient")
play music music_dreamy fadein 8.0

scene bg hok_lounge
show lilly basic_smileclosed_cas at center
with openeye

"Concediendo la derrota fácilmente, me levanto y froto mis ojos."

hi "¿Cómo lo sabías?"

show lilly basic_weaksmile_cas
with charachange

li "Tu respiración era irregular."

"Si bien eso tiene sentido, no debe haber necesitado tanto tiempo para adivinarlo. Conociendo su audición, posiblemente lo haya sabido antes de poner su mano sobre mí."

show lilly basic_displeased_cas
with charachange

li "Si quieres dormir más, en serio deberías acostarte más temprano. Escuché la televisión hasta bien entrada la noche."

hi "Perdón por eso. Mis medicamentos han estado interfiriendo con mi sueño durante ya hace algún tiempo. Aun si estoy cansado tengo problemas para quedarme realmente dormido."

show lilly basic_oops_cas
with charachange

li "Lo… siento por sacar el tema, Hisao."

label es_choiceL15:
menu:
    with menueffect
    "Suspiro. Este es exactamente el tipo de cosas que desearía que los demás no hicieran."
    "Discutirlo.":


        return m1
    "Eludir el tema.":

        return m2


label es_L15a:

hi "Vamos, tú te preocupas por mí más de lo que yo lo hago a veces. Solo significa que tengo que dormir un poco más, eso es todo."

show lilly basic_reminisce_cas
with charachange

li "Pero de todas formas…"

hi "Diría que me veo completamente bien, pero supongo que eso no significaría mucho para ti."

show lilly basic_displeased_cas
with charachange

"Ella suelta un suspiro de consternación antes de rematar con una risita divertida, cediendo el punto."

show lilly basic_weaksmile_cas
with charachange

li "Sí tú lo dices. Por favor cuídate, Hisao."

hi "Ve, Hanako podría necesitar algo de ayuda."

hide lilly
with dissolve

"Ella se mueve para protestar, pero accede a regañadientes y desaparece en la cocina, su mano recorriendo las lisas paredes blancas a medida que camina lentamente."

label es_L15b:

hi "Hanako probablemente… pueda necesitar algo de ayuda."

show lilly basic_displeased_cas
with charachange

hide lilly
with dissolve

"Lilly parece a punto de protestar por un momento, pero eventualmente accede, asintiendo antes de dirigirse a la cocina."

label es_L15c:

"Por un rato me quedo sentado y miro la televisión en un intento de despertarme un poco más, pero es inútil. No tengo nada mejor que hacer, así que sigo el ejemplo de Lilly."

stop ambient fadeout 5.0

scene bg hok_kitchen
with locationchange

"Cuando doy vuelta en la esquina, veo a Hanako y a Lilly, de espaldas, cortando tranquilamente la comida en el mostrador color granito."

"Me veo temporalmente absorto mientras miro a Lilly guiando el cuchillo hacia abajo con el dedo sobre la lechuga que está cortando, cada corte hecho lentamente pero con precisión."

"Parece un tanto lenta, pero considerando que no puede ver lo que está haciendo, es una sorpresa que pueda siquiera cocinar, no se diga para ella y para Hanako."

hi "Hola Hanako, Lilly. ¿Quieren ayuda?"

show lilly back_surprise_cas at twoleft
show hanako basic_normal_cas at tworight
with charaenter

stop music fadeout 0.3

$ doublespeak(li, ha, u"¿Es Hisa— ¡ah!",  u"Oh, buenos días Hisao.")

show lilly basic_oops_cas
with charachange

"Lilly se yergue bruscamente por la sorpresa antes de darse vuelta, su quejido llamándonos inmediatamente a Hanako y a mí a su lado."

hi "Qué… ah."

"Un pequeño hilo escarlata cae por sus pálidos dedos, el cuchillo habiendo cortado lo suficientemente profundo para sacar sangre."

"Con el sonido de la televisión cubriendo mis pasos, no debe haberme notado venir. Para compensar el tener que usar el tacto para guiar todo lo que hace mientras cocina, debe necesitar poner atención extra."

show hanako defarms_shock_cas
with charachange

play music music_dreamy fadein 8.0

ha "¡Lilly!"

show lilly basic_weaksmile_cas
with charachange

li "No te preocupes, Hanako. Es solo una herida pequeña."

hi "De todas formas deberías poner una vendita sobre ella, al menos hasta que deje de sangrar. Las cosas de primeros auxilios están en el baño, ¿cierto?"

show lilly basic_sleepy_cas
with charachange

li "Eso creo. ¿Estarás bien aquí, Hanako?"

show hanako cover_worry_cas
with charachange

"Frunzo el ceño por la poca atención que se pone a sí misma mientras Hanako asiente de forma rápida, casi automática."

show hanako basic_worry_cas
with charachange

ha "Está bien, puedo seguir preparando el almuerzo."

scene bg hok_bath
with locationskip

"Un silencio incómodo impera mientras dejo la botella de antiséptico y una caja de curitas a un costado del lavabo, el dedo de Lilly extendido hacia mí para que lo cure."

"La tapa de la botella sale con un mínimo de resistencia, y la pequeña mota de algodón que empapo en el líquido se tiñe de un verde pálido."

hi "Bien, quédate quieta. Esto probablemente duela un poco."

show lilly basic_weaksmile_cas_close at center
with charaenter

"Ella asiente débilmente mientras sostengo su mano para inmovilizarla. Con toda la amabilidad que puedo reunir, suavemente coloco el copo mojado en la pequeña línea roja."

show lilly basic_oops_cas_close
with charachange

li "¡Ah!"

hi "¿Qué? Apenas lo toqué."

show lilly basic_reminisce_cas_close
with charachange

li "Lo siento…"

"Suelto un suspiro, tanto por su reacción como para calmar mis propios nervios. Su tolerancia al dolor es sorprendentemente baja."

hi "Te diría que lo aguantaras como hombre, pero en realidad no puedo hacer eso."

show lilly basic_weaksmile_cas_close
with charachange

"Cuando ella suelta una risita, aprovecho su distracción momentánea y presiono suavemente el algodón contra su dedo unas cuantas veces. Afortunadamente, es suficiente para cumplir el fin."

"Ambos nos tranquilizamos un poco cuando coloco la vendita sobre la punta de su dedo, cubriendo la herida asegurándome de que no se quede atorada en su uña."

hi "Bien, terminé. Ahora puedes moverte."

"Retirando su mano de la mía, ella gentilmente la afirma con la otra."

show lilly basic_smileclosed_cas_close
with charachange

li "Gracias."

hi "No hay problema. Es lo menos que puedo hacer luego de haber hecho que te lastimaras, después de todo."

show lilly basic_emb_cas_close
with charachange

"Ella baja un poco su cabeza ante la disculpa, frotando distraídamente su mano en lo que parece ser vergüenza."

show lilly basic_weaksmile_cas_close
with charachange

li "En verdad no me molesta."

stop music fadeout 5.0

"Su respuesta no parece tener mucho sentido, dado que lo que sucedió es claramente mi culpa."

"No puedo evitar hacer una mueca, a pesar del hecho de que su delicada sonrisa se mantiene. A ella no debe gustarle que le recuerden de los límites que su falta de visión le impone."

"Es algo por lo cual no puedo culparla en absoluto. He caído ante el mismo tipo de sentimientos antes, a pesar de que mi condición no sea ni remotamente tan ubicua en mi vida."

"Ninguno de los dos más feliz, regresamos hacia los varios olores de comida cocinándose que vienen de la cocina."

scene bg hok_lounge
with shorttimeskip

play music music_another fadein 8.0

"Dejo los platos de comida, vapor emanando lentamente de los platillos de arroz bien cocido y curry, mientras que Hanako coloca los cubiertos."

"Cuchillo a un lado, tenedor al otro. Occidental. Qué perfectamente apropiado para alguien como Lilly."

"Cuando nos sentamos, poniendo especial atención en el mantel rojo oscuro que cuelga bajo nuestras rodillas, Lilly sale de la cocina."

"En sus manos hay tres copas y… ¿una botella de vino?"

"Cuando recuerdo nuestro encuentro anterior con ese elíxir endemoniado, oculto mi rostro con mi palma."

hi "¿Alcohol? ¿De verdad?"

show lilly basic_cheerful_cas at center
with charaenter

"Ella se detiene cuando llega a la mesa, con una sonrisa traviesa en su rostro."

show lilly basic_giggle_cas
with charachange

li "Akira específicamente me dio permiso para sacar una botella de su colección."

"¿No solo le da alcohol a menores de edad, sino que también les deja tomar del propio? Akira no es el modelo perfecto de adulto responsable."

"Aunque, más al punto, es que esta difícilmente es una comida que merezca alcohol. Estoy comenzando a pensar que Lilly es de las que se enganchan fácilmente."

hi "Ese no es el problema, realmente. En verdad no tengo recelos por eso, pero ¿no tuviste una mala experiencia la última vez?"

show lilly basic_smileclosed_cas
with charachange

li "La última vez fue posiblemente por beber demasiado, así que una sola copa no debería traer problemas."

show lilly basic_smile_cas
with charachange

li "Piensa en ello como una experiencia de aprendizaje."

hi "No puedo recordar muchas experiencias que me hayan hecho sentir horrible antes de dejarme dormido, pero aceptaré tu palabra."

show lilly basic_smileclosed_cas
with charachange

"Ella introduce un dedo ileso dentro para sentir el nivel del líquido, la punta contra el fondo a medida que el líquido sube."

"El blanco de su dedo casi parece brillar cuando le llega la luz del sol, su delicado contorno nublado y refractado por la copa."

"Sus dedos definitivamente son más largos que los míos, del tipo que creo que serían más apropiados para una pianista que para una maestra. Probablemente habría sido buena si hubiera aprendido cómo tocar."

hide lilly
with charaexit

"Rápidamente comenzamos con nuestra comida, cuchillos y tenedores repicando contra los platos."

"Ninguno de nosotros está particularmente deseoso de hablar mientras come, Lilly siendo demasiado reservada para tal cosa, Hanako probablemente demasiado tímida para iniciar una conversación, y yo demasiado ocupado degustando la comida."

"Tal actividad tan cotidiana, comer juntos en una mesa. Parece tan normal, y sin embargo hace que me dé cuenta de cuánto tiempo ha pasado desde que he hecho algo como esto."

"Solo nosotros tres, sentados alrededor de una sola mesa comiendo como si fuéramos una familia malformada. Quizás este viaje, tan alejados de todo como estamos, valió la pena."

with shorttimeskip

"Nos toma algo de tiempo, pero eventualmente nos terminamos nuestra sorprendentemente satisfactoria comida. El vino, afortunadamente, no ha tenido mucho efecto ya que solo hemos tomado una copa o dos cada uno."

"Me recuesto sobre el respaldo, frotándome el estómago con satisfacción."

hi "Estoy lleno."

show lilly basic_smileclosed_cas at twoleft
show hanako basic_smile_cas at tworight
with charaenter

"Lilly toca su boca con una servilleta. Dos veces, solo dos veces, y con intervalos de tiempo parejos entre medio. A veces es difícil decir si el cómo actúa es una rutina bien entrenada o un acto bien practicado."

show lilly basic_satisfied_cas
with charachange

li "Creo que yo también lo estoy. ¿Te gustó, Hanako?"

show hanako cover_bashful_cas
with charachange

ha "Mm, estuvo bueno."

show lilly basic_smileclosed_cas
with charachange

li "Ahora que estamos bien alimentados, ¿partimos?"

hi "¿Partir? ¿Hacia dónde?"

show lilly basic_weaksmile_cas
with charachange

li "Ah, no fuiste parte de la discusión que tuvimos Hanako y yo más temprano."

"Tengo la impresión de que está haciendo un comentario sutil sobre el que me haya quedado dormido."

show hanako basic_bashful_cas
with charachange

ha "Iremos al pueblo que hay cerca."

"Supongo que debería haber esperado que dos chicas usaran unas vacaciones como excusa para ir de compras, sin importar en qué parte del mundo puedan estar."

"Aunque sí estoy interesado en ver más del norte, así que esto puede ser algo bueno."

hi "Suena bien. ¿Qué tan larga es la caminata, entonces?"

show lilly basic_smile_cas
with charachange

li "Se supone que es entre un kilómetro y medio y dos y medio."

stop music fadeout 4.0

hi "Cerca, ¿eh? Genial."

"Simplemente genial."

scene bg hok_road at bgright
with shorttimeskip

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_parkambience fadein 6.0
play music music_soothing fadein 0.5

"A medida que subimos por el camino rodeado de árboles y maleza, observo a Lilly y a Hanako caminando adelante."

"La suave brisa no hace sino remover el sonido del bastón de Lilly golpeando suavemente el suelo. Noto que Lilly se ha quitado la curita ahora que su dedo ha dejado de sangrar."

"Un respiro profundo que llena los pulmones con el fresco aire campestre me hace desear aún más que el aire que había en casa hubiera sido tan limpio."

"No puede haber sido ni un kilómetro, pero ya estoy comenzando a sudar. No es un día agradablemente fresco, así que no debería exigirme demasiado."

hi "Oye Lilly, por cierto, ¿qué tan bien conoces este pueblo?"

show lilly back_smileclosed_cas at center
show lillyprop back_cane
with charaenter

li "Como pasé muchas de mis vacaciones en este lugar hasta que entré a Yamaku, diría que lo conozco bastante bien. Solíamos venir aquí en auto una vez a la semana en ese entonces."

"Cómo desearía que Akira estuviera aquí para llevarnos en auto."

"Rápidamente me tomo un momento para frotar mis manos un par de veces, aliviando la sensación extrañamente fría en ellas."

hi "¿Te gustaba este lugar?"

show lilly cane_weaksmile_cas
hide lillyprop
with charachange

li "Diría que es agradable durante el invierno, pero como puedes suponer, en verano se pone un tanto caluroso como para ser cómodo. Es agradable y tranquilo, por lo menos."

li "La casa verdadera de mi familia está bastante más al sur. Cuando se fueron de Japón, mis padres nos la dieron a Akira y a mí. Ahora solo Akira vive ahí, luego de que me mudara a Yamaku."

hi "Bueno, tranquilo ciertamente describe este lugar."

"Aunque yo habría dicho solitario."

"Además del augurado pueblo pequeño, no hay alma alguna por kilómetros a la redonda. Al venir de un hogar ubicado en lo profundo de la gran ciudad, ciertamente es distinto."

"Creo que si no hubiera venido a Yamaku, estar aquí afuera en el campo de esta forma sería demasiado cambio como para acostumbrarme."

"Aunque después de habituarme al aislamiento de la escuela, la idea de vivir en un lugar como este se ha vuelto casi atrayente. Estar en un lugar apartado del barullo de los centros metropolitanos."

show lilly cane_smile_cas
with charachange

li "Y bien Hisao, ¿has estado en Hokkaido antes?"

hi "No. Solía vivir en el sur, y nunca hicimos ningún viaje de estudio ni tuvimos vacaciones tan lejos."

show lilly cane_cheerful_cas
with charachange

li "Bueno, entonces es una experiencia nueva para ti."

hi "Sí, lo es. Me sorprende lo agradable que se siente este lugar."

hi "¿Qué hay de ti, Hanako?"

show lilly cane_cheerful_cas at twoleft
show bg hok_road at center
with charamove

show hanako emb_smile_cas at tworight
with charaenter

"Ella mueve la cabeza de lado a lado."

show hanako basic_bashful_cas
with charachange

ha "También es mi primera vez."

"A medida que seguimos caminando, comienzo a sentir punzadas en mis piernas. Es un tanto preocupante, dado que no hay ningún motivo para que eso suceda."

stop ambient fadeout 9.0
stop music fadeout 4.0

hi "¿Podrían esperar un momento? Solo necesito…"

show lilly cane_surprised_cas
with charachange

li "¿Pasa algo?"

hi "Nah, es solo que siento punzadas en…"

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
with Dissolve (0.8)

with Pause(0.05)

play sound sfx_heartstop
show heartattack alpha
with Dissolve (0.1)

show heartattack residual
with Dissolve (0.8)

play music music_tragic fadein 0.5

window show

"Mis cuerdas vocales de pronto se tensan mientras que mi pecho se estrecha instantáneamente. De inmediato pongo mi brazo sobre él, intentando calmar el golpe de dolor que se expande por todo mi cuerpo."

show lilly cane_reminisce_cas
show hanako defarms_strain_cas
with charachange

li "¿Hisao?"

"El rostro de Lilly solo está un tanto preocupado, sin ver lo que hace que Hanako retroceda."

hi "Estoy bien, estoy… bien. Solo… cansado…"

"Retiro mi brazo de mi pecho y me fuerzo a comenzar a caminar otra vez. Solo es una palpitación menor, así que pasará tal como los otros."

play sound sfx_heartslow

show heartattack alpha
with Dissolve (0.1)

show heartattack residual
with Dissolve (0.8)

"Solo toma unos pasos antes de que mi cuerpo comience a revelarse en contra mía de forma violenta, mis piernas de pronto comienzan a ceder debajo de mí y toda la tensión de mis rodillas se evapora."

scene bg hok_road:
    xalign 0.5 yalign 0.52 rotate 0 zoom 1.0
    linear 0.1 rotate -6 zoom 1.2
show lilly cane_reminisce_cas:
    xanchor 0.5 xpos 0.3 yalign 0.52 rotate 0 zoom 1.0
    linear 0.1 xpos 0.25 rotate -6 zoom 1.2
show hanako defarms_strain_cas:
    xanchor 0.5 xpos 0.7 yalign 0.52 rotate 0 zoom 1.0
    linear 0.1 xpos 0.75 rotate -6 zoom 1.2
show heartattack residual
play sound sfx_pillow
with vpunch

"Antes de poder reaccionar ceden por completo bajo mi propio peso, dejándome apenas el tiempo suficiente para prepararme y caer con las cuatro extremidades."

hi "Ah, maldición…"

show hanako defarms_shock_cas
with charachange

ha "¡Hisa… AAAAH!"

"Cuando alzo la mirada hacia ella me doy cuenta de que mi rostro sigue tenso de dolor, lo que solo añade más a su preocupación."

show lilly cane_oops_cas
with charachange

li "¿¡Hisao!? ¡Hanako, dime qué está pasando!"

li "¡Hanako, dime!"

show hanako def_strain_cas_close
with characlose

"Hanako rápidamente se acerca a mi lado mientras que Lilly casi entra en pánico, sin tener idea de exactamente en qué tan mala condición me encuentro. Mientras está ahí petrificada, bajo mi rostro y respiro profundamente."

scene black
show heartattack alpha
with shuteyefast

"Llego a darme cuenta de algo que me irrita sin fin con mi estúpido ser. Con toda la emoción de mis nuevos alrededores, me olvidé por completo de tomarme mis medicamentos anoche o incluso hoy por la mañana."

stop music fadeout 9.0

hide heartattack
with Dissolve(3.0)

"Respirando otra vez, el agudo dolor en mi pecho empieza a desaparecer tan pronto como comenzó."

"Gracias al cielo. Gracias al cielo. Gracias al cielo, gracias al cielo, gracias al cielo."

play ambient sfx_parkambience fadein 6.0

scene bg hok_road
show lilly cane_oops_cas at twoleft
show hanako def_strain_cas_close at tworight
with openeye

"Cuando lo hace, soy plenamente consciente del sudor que ahora cae por mi rostro y las dos chicas asustadas a mi alrededor."

show lilly cane_reminisce_cas
with charachange

li "¡Hisao!"

hi "Estoy bien, Lilly. Estoy… bien."

show hanako defarms_strain_cas_close
play sound sfx_impact
with vpunch

"Arrugo mi frente en un esfuerzo por levantarme, los brazos de Hanako acercándose rápidamente para atraparme si caigo cuando me tambaleo un poco antes de recuperar mi balance."

"Miro a Lilly y a Hanako, con la preocupación expresa en sus caras. Me siento horrible. Completamente horrible."

show lilly cane_sad_cas
with charachange

li "Creo que deberíamos regresar."

hi "Yo…"

"Dándome cuenta de lo inútil de protestar, aparto la mirada con frustración."

hi "Está bien."

stop ambient fadeout 2.0

$ suppress_window_after_timeskip = True

scene black
with dissolve



label es_L16:

window hide None

scene black
with dissolve

scene bg hok_lounge_ss
with openeye

window show

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_cicadas fadein 2.0

"Abro mis ojos adormiladamente, carente de energía por completo."

"Por un rato, simplemente yazco sin vida, mirando el techo mientras repaso los acontecimientos de la mañana en un intento de organizar mis pensamientos."

"Fuimos a caminar al pueblo. Mi corazón casi cede. Regresamos. Me tomé mis medicamentos. Dormí."

"Solo puedo recordar cada fragmento de tiempo como una foto, pero la secuencia es bastante clara. El recuerdo del rostro de las chicas mientras me esforzaba por pararme es desagradable, hiriendo mis sentimientos severamente."

"Si miro lo suficiente el techo, puedo imaginarme los bordes de las cubiertas y los pequeños puntos del techo en el hospital. Ese hecho por sí solo es suficiente para que me siente e intente recuperar la compostura."

"Me rasco detrás de mi cabello despeinado, mirando por la habitación. Lilly y Hanako no están por ninguna parte, y la televisión está apagada."

"El reloj sobre ella dice que es bastante entrada la tarde. El cielo notoriamente más enrojecido fuera de la ventana lo confirma aún más."

"Me doy vuelta y me levanto del futón, tambaleándome un poco mientras extiendo mis brazos para balancearme. Supongo que mejor voy a buscar a las chicas para ver si están… bien…"

"Cuando miro por la ventana, veo algo tenuemente a la distancia."

"Forzando mis ojos, apenas puedo distinguir la figura de una persona. Su largo cabello rubio, ondeando con la suave brisa, la hace casi fundirse con el amarillo brillante de los campos de trigo."

"Sin pensarlo dos veces, salgo de la habitación para seguir a esa aparición solitaria."

stop ambient fadeout 2.0
play music music_innocence fadein 14.0

scene bg hok_wheat_ss at Fullpan(8.0)
with Fade(0.5, 0.2, 3.0, color="#fff")

"El brillo del sol poniente asalta mis ojos recién despiertos, forzándome a apartar la vista hasta que se ajustan."

"Los largos tallos de trigo rozan contra mis piernas mientras vadeo entre ellos, el campo densamente cubierto haciendo difícil avanzar."

"A pesar de ello, mis ojos permanecen fijos hacia adelante, fieles a la figura solitaria. La alcanzo en minutos, metros detrás de su espalda."

hi "¿Lilly?"

scene bg hok_wheat_ss at right
show lilly back_pout_cas_ss at center
with charaenter

"Ella simplemente asiente."

hi "¿Dónde está Hanako?"

show lilly back_listen_cas_ss
with charachange

li "Está en la cama. Se fue a dormir luego de que la calmara."

"Ella dice esto de forma bastante neutra y con la menor cantidad de palabras posible, como si decir algo más estuviera estrictamente prohibido."

"Hay algo distinto en ella. Su figura normalmente confiada parece curiosamente frágil, sin que su cuerpo oponga resistencia a la brisa que sopla su falda."

"Los tallos de trigo se mecen de lado a lado mientras pasa una ensordecedora pausa, su susurro siendo el único sonido."

"Estando de pie solos en el campo, sé lo que tengo que preguntar."

hi "¿Qué ocurre, Lilly? No actúas como lo haces siempre."

show lilly back_sad_cas_ss
with charachange

li "¿Recuerdas cuando te hablé de mi familia, Hisao?"

hi "Tu familia…"

"Bajo la mirada, pensativo, repasando mis dispersos recuerdos. El suceso parece saltar a la vista cuando lo busco, aflorando a la superficie tan pronto intento recordarlo."

hi "¿Después de la fiesta de cumpleaños de Hanako?"

"Ella asiente una sola vez."

show lilly back_pout_cas_ss
with charachange

li "Fue agradable… en ese entonces. Tú y yo, celebrando con Hanako. Simplemente compartiendo obsequios, hablando, divirtiéndonos juntos. Fue casi como si fuéramos una familia. Una pequeña, y malformada familia."

show lilly back_sad_cas_ss
with charachange

li "Pensé que eso podría seguir para siempre. Solo nosotros tres, felizmente juntos."

"Ella respira profundamente, con un temblor ligero que es apenas audible a través del aire en movimiento."

show lilly back_pout_cas_ss
with charachange

li "Aun si mi familia estaba tan lejos… mientras estuviéramos juntos, eso era todo lo que necesitaba. No quiero perderte, Hisao."

li "Ni siquiera me di cuenta del miedo que tenía de perder a alguien más hasta hoy. Hasta…"

hi "Lo siento, Lilly. Sé que mi cuerpo es débil, pero incluso así cometo los errores más estúpidos."

stop music fadeout 4.0

show lilly back_sad_cas_ss
with charachange

li "No te disculpes… por favor no te disculpes…"

hi "¿Lilly…?"

show lilly basic_concerned_cas_ss
with charachange

"Ella se da la vuelta para encararme, sus pálidas mejillas manchadas con lágrimas."

show lilly basic_concerned_cas_close_ss
with characlose

"A paso torpe ella se desploma hacia mí, sus brazos extendidos en busca de aunque sea un leve roce contra mí."

play music music_romance fadein 2.0

window hide

scene unlock_ev lilly_wheat_close
show ev lilly_wheat_large:
    yalign 0.5 xalign 0.0 subpixel True
    easein 20.0 xalign 1.0
show ovl lilly_wheat_foreground:
    yalign 0.5 xalign 0.0 subpixel True
    easein 20.0 xalign 1.0
with GenericWhiteout(1.0, 0.0, 4.0)

window show

"Mi corazón no acelera ni late a medida que avanzo hacia Lilly, sujetándola y afirmándola gentilmente en mis brazos mientras ella rápidamente se aferra a mí, sollozando."

"Con su rostro temblando contra mi hombro, las siguientes palabras que salen de su boca son las que menos esperaba."

li "Te amo, Hisao. ¡Te amo, te amo, te amo, te amo, te amo!"

li "No te vayas, te lo ruego. Nunca, nunca te vayas. ¡Te amo, así que por favor…!"

"Entonces… es por eso que ha estado actuando así. Esa dulce voz cuando la llamé, su preocupación irreflexiva ante el más mínimo dolor que pudiera sentir yo…"

"Luego de haber sido dejada en Japón sin su familia, y solo con Akira, Hanako y yo a su alrededor, tenía miedo de perder a otra persona más que le fuera cercana. Ella genuinamente estaba preocupada por mí."

"Es un sentimiento extraño. Una mezcla de sorpresa y pena, y sin embargo también de la más profunda gratitud que creo he sentido. La única reacción que puedo exhibir entre mis emociones en conflicto es un suspiro sereno."

hi "Tonta."

li "¿Hi… sao?"

"Por un efímero momento, siento su cuerpo detenerse. El único movimiento que se siente es la tranquila brisa del atardecer."

hi "Lo dije antes, ¿no es así? Es normal sentir preocupación por aquellos que te rodean."

hi "Yo sigo aquí, y siempre estaré aquí, porque quiero verte más cada día. Para compartir tu felicidad, para apoyarte en tu pena…"

hi "Pero por sobre todo, seguiré aquí porque quiero ver tu sonrisa. Tu sonrisa verdadera."

"Un soplo solitario de viento mece los largos tallos de trigo, un segundo de silencio pasa."

hi "Sonríe cuando quieras sonreír. Llora cuando quieras llorar. Te amo, Lilly. Así que no tienes que contenerte más."

"Con eso, sus brazos se aferran a mi espalda tan fuerte como puede, su rostro enterrado junto al mío."

scene ev lilly_wheat_small:
    xalign 0.5 yalign 0.5 zoom 1.1 subpixel True
    ease 16.0 zoom 1.0
with whiteout

"Sus lágrimas caen en mi espalda y llora sin contenerse mientras lo último de su resistencia desaparece."

li "¡Hisao! ¡Hisao! ¡Hisao!"

"Cierro mis ojos y bajo mi cabeza hasta su hombro, sosteniendo su temblorosa figura firmemente."

hi "Está bien, Lilly. Yo nunca me iré."

hi "Lo prometo."

stop music fadeout 6.0



label es_L17:

scene bg hok_lounge_ss
with locationskip

"Caminamos lentamente de vuelta a la casa, sosteniéndonos fuertemente cuando nos sentamos adentro. Lilly apoya su cabeza en mi hombro mientras que yo rodeo su cadera con mi brazo."

"Ninguno de los dos tiene algún deseo de romper el silencio."

"Con sus ojos cerrados es difícil saber si se ha quedado dormida. No es que me importe: la calidez de su cuerpo apoyado contra mí, la suavidad de su mano sostenida delicadamente en la mía…"

"Durante un largo, largo tiempo nos sentamos apoyados el uno contra el otro, compartiendo nuestro calor y sentimientos a medida que la noche eventualmente comienza a asentarse."

"La dulce y suave voz de Lilly acaba el silencio."

show lilly basic_smileclosed_cas_close_ss at center
with charaenter

play music music_twinkle fadein 6.0

li "Gracias, Hisao."

hi "¿Gracias?"

show lilly basic_smile_cas_close_ss
with charachange

li "Por corresponder mis sentimientos."

hi "¿Pensabas que no lo haría?"

show lilly basic_weaksmile_cas_close_ss
with charachange

li "Existía la posibilidad."

"Respiro profundamente, reflexivo. Eso fue solo mi culpa."

hi "Es gracioso, de hecho. Estaba pensando en decirte mis propios sentimientos en algún momento pronto."

hi "Supongo que, en ese sentido, me ahorraste el esfuerzo."

show lilly basic_giggle_cas_close_ss
with charachange

"Ella levanta un poco su cabeza y suelta una risita divertida. Sonrío por lo franca que es, tan propia de una chica por su delicadeza. Ella se recompone pronto, su cabello descansando contra mis hombros."

hi "¿Te sientes un poco mejor?"

show lilly basic_smileclosed_cas_close_ss
with charachange

"Ella asiente un poco."

show lilly basic_smile_cas_close_ss
with charachange

li "Eres considerado, Hisao. Es por eso que te quiero."

hi "Lamento ser así. Por mucho que no quiera hacer que te preocupes por mí, no podía hacer nada para prevenirlo."

show lilly basic_concerned_cas_close_ss
with charachange

li "No te disculpes por ello. Por favor no lo hagas."

hi "¿Lilly?"

show lilly basic_reminisce_cas_close_ss
with charachange

li "¿Alguna vez me he disculpado por mi ceguera, aunque sea una vez? No puedes evitar ser como naciste, Hisao. No tiene sentido disculparse por quién eres."

"Ella dice eso con sorprendente convicción. Al final, fue quizás esta mentalidad la que la alentó a entablar amistad conmigo en tan poco tiempo, además de sus instintos maternales."

"Ella pareció tomar confianza bastante rápido, pero nunca me pregunté el porqué. Ahora parece obvio que lo hizo para poder ayudarme mientras pasaba por uno de los peores momentos de mi vida."

"Me muevo para responder, pero me detengo cuando siento sus dedos recorrer amablemente mi cabello. Siento su suave y delicado tacto bajando para recorrer los contornos de mi rostro, su palma finalmente asentándose en mi mejilla."

show lilly basic_weaksmile_cas_close_ss
with charachange

li "Eres una persona hermosa, Hisao. Por favor, nunca te disculpes por eso."

"Por un momento, me quedo sin palabras. Lentamente bajo mi cabeza, dándole un dulce beso en su ligero y voluminoso cabello."

hi "Somos una pareja de verdaderos viejos tontos, ¿no es así?"

show lilly basic_cheerful_cas_close_ss
with charachange

li "… Así es."

"Luego de una larga paz, ella vuelve a hablar."

show lilly basic_smile_cas_close_ss
with charachange

li "¿Hisao?"

hi "¿Sí?"

show lilly basic_smileclosed_cas_close_ss
with charachange

li "No…"

stop music fadeout 4.0

show lilly basic_weaksmile_cas_close_ss
with charachange

li "No me molestaría si tú…"

"Siento su mano tensándose bajo la mía, temblando un poco. Mi boca se abre, pero por mucho que lo intente, no puedo formular una respuesta a su proposición."

hi "Lilly…"

"Antes de poder decir alguna otra palabra, ella desliza su mano de bajo la mía y suavemente sostiene el costado de mi rostro una vez más."

show lilly basic_pout_cas_close_ss
with charachange

li "Por favor."

"Suelto una sonrisa serena, sosteniendo su mano contra mi mejilla mientras asiento una sola vez."

hi "De acuerdo."

play music music_heart fadein 0.5

show lilly basic_smileclosed_cas_close_ss
with charachange

"Mientras miro sus ojos, ella se inclina hacia mí. Sus delicados labios tocan los míos mientras ella se guía con su mano."

"Ella se separa en menos de un segundo, sonriendo débilmente."

show lilly basic_smile_cas_close_ss
with charachange

li "Te amo, Hisao."

show lilly basic_smileclosed_cas_close_ss
with charachange

"Nos volvemos a besar, esta vez acercándonos ambos."

"Si bien el beso anterior fue de amor, este es de pasión, nuestras lenguas tocándose y nuestra respiración pesada. Pasados maravillosos segundos nos separamos, nuestros rostros de verdad sonrojados."

"Ambos llevamos nuestros dedos hacia nuestros labios al unísono, recordando la efímera sensación, rápidamente siendo superados por nuestros deseos y nuestra timidez."

show lilly basic_pout_cas_close_ss
with charachange

"Pero Lilly es la primera en moverse incómoda."

hi "¿Qué ocurre?"

show lilly basic_weaksmile_cas_close_ss
with charachange

li "¿No deberíamos… ponernos más cómodos?"

hi "¿Hmm? Ah, e-está bien…"

"Ahora que lo menciona, este futón sería un poco estrecho para hacer mucho en él. Considerando los pensamientos que pasan por la mente de ambos, es sorprendente que uno de nosotros aún tenga un dejo de previsión."

show lilly invis:
    ypos 1.2
with dissolvecharamove

hide lilly
with vpunch

"Tomo sus manos y la guío a un lado mientras me muevo, el breve y embarazoso baile acabando con ambos sentados indecisamente en el suelo colocados el uno frente al otro."

"Cuando me adelanto para levantar su camisa, ella se detiene después de haber movido sus manos para hacer lo mismo."

show lilly basic_concerned_cas_close_ss:
    center
    ypos 1.17
with charaenter

li "Estás temblando…"

"Me detengo un momento y miro mis manos."

"En efecto, se están agitando un poco. Si es por nerviosismo o excitación, no estoy seguro."

hi "Ah… supongo que lo estoy."

show lilly basic_weaksmile_cas_close_ss
with charachange

li "¿Entonces estás tan nervioso como yo?"

"Retiro mis manos y suspiro, afianzándome. Tenemos suficiente tiempo, así que no hay necesidad de apresurar esto."

hi "Lo siento. Es mi primera vez, así que estoy un poco…"

show lilly basic_cheerfulblush_cas_close_ss
with charachange

"Ella se ríe de forma temblorosa, confirmando lo que ya había deducido razonablemente."

show lilly basic_smile_cas_close_ss
with charachange

li "Es lo mismo en mi caso. Estoy feliz… de que podamos compartir esto juntos."

"Duplico su sonrisa, inclinándome hacia adelante y tomando su cuerpo entre mis brazos mientras ella se estira para devolverme el abrazo."

hi "Te amo, Lilly."

show lilly basic_smileclosed_cas_close_ss
with charachange

li "Ya dijiste eso."

"No puedo evitar sonreír. Aun en tal situación, ella todavía mantiene su ingenio."

hide lilly
with charaexit

"Separándonos de nuestro abrazo, decidimos quitarnos nuestra propia ropa. Si bien es más fácil de esta forma, no dudo en absoluto que es solo un intento de distraernos de nuestros nervios."

"Con las manos un poco tensas, comienzo a desabrochar el primer botón de mi camisa."

"Una vez que nos quitamos por completo la ropa, la cual queda apilada desordenadamente tras nosotros, mi aliento es arrebatado por la imagen ante mí."

label es_L17h:

show lilly behind_reminisce_nak_ss
with charaenter

"Sus largas y bien formadas piernas, amplias caderas y sus senos, rollizos pero refinados… su rostro ligeramente sonrojado, delicado y reservado, está enmarcado por los flecos de su cabello."

"Sus manos, sostenidas con firmeza tras ella, solo sirven para acentuar su pecho. Su alto y blanco cuerpo es hermoso descubierto."

"Esta chica frente a mí, reservada pero juguetona, astuta pero acogedora, es la chica de la que me he enamorado."

"Me inclino hacia adelante, tomando con delicadeza sus hombros con mis manos."

show lilly behind_listen_nak_close_ss
with charachange

"Mientras hago eso, ella lleva sus manos a mi pecho. Con un aliento un tanto errático, nos inclinamos en un beso apasionado."

"Siento una de las manos de Lilly deslizarse lentamente hasta mi hombro, avanzando muy gentilmente junto con su cabeza. Asumiendo su intención, me reclino hacia el piso."

hi "Ah…"

scene evhunlock lilly_handjob_chest_normal_small
show evh lilly_handjob_chest_normal:
    xalign 0.7 yalign 1.0 subpixel True
    ease 8.0 xalign 0.4 yalign 0.2
with whiteout

"Ella se agazapa junto a mí, una mano acariciando mi cabello mientras la otra recorre mi pecho. La sensación de sus senos contra este es suficiente para excitarme."

"Esta debe ser su forma de captar lo que yo ya he visto de ella; a pesar de su falta de vista, ella graba cada detalle de mi cuerpo desnudo y mi pecho en su mente."

"Cuando su dedo medio cae en la pequeña grieta de las cicatrices de mi pecho, un remanente de mi operación hace muchos meses, ella lentamente recorre su extensión con su mano."

show evhunlock lilly_handjob_chest_frown_small
show evh lilly_handjob_chest_frown:
    xalign 0.4 yalign 0.2
with charachange

li "Esto es…"

hi "La cicatriz de mi cirugía. Tuvieron que hacer eso para poder operarme el corazón."

"Por un momento ella queda sin palabras, la idea de unas cicatrices tan extensas sumándole una nueva preocupación. Su expresión cambia de curiosidad a aprehensión."

li "¿De verdad… deberíamos estar haciendo este tipo de cosas…?"

"Esas palabras me molestan más allá de lo racional. El rostro de Lilly me parte el corazón más de lo que sus palabras podrían hacerlo, y sin embargo no sé la respuesta a su pregunta."

"No puedo dejar que esta condición me domine para siempre. Puede que no sea recomendable médicamente, pero me niego rotundamente a vivir mi vida en tal prisión."

hi "Está bien, Lilly. Hacer esto estará bien."

show evh lilly_handjob_chest_normal
with charachange

"Su expresión preocupada se mantiene por un momento más, pero eventualmente cede, su mano moviéndose hacia la parte de abajo de mi pecho y luego hacia mis muslos."

show evh lilly_handjob_chest_normal:
    zoom 1.0 xalign 0.4 yalign 0.2
    ease 4.0 zoom 0.667 xalign 0.5 yalign 0.5
with None

show evh lilly_handjob_stroke_normopen:
    zoom 1.0 xalign 0.4 yalign 0.2
    ease 4.0 zoom 0.667 xalign 0.5 yalign 0.5
with charachange

"Con una expresión de moderada sorpresa, ella lentamente baja sus manos, su aliento entrecortado cuando roza un costado de mi vello inferior."

"Ella vacilantemente mueve su mano hacia un lado, tocando delicadamente la parte más honesta de mi cuerpo."

show evh lilly_handjob_stroke_normshut_small:
    truecenter
    zoom 1.0
with charachange

li "E… esto es…"

hi "S-Sí."

"Nuestro nerviosismo llega a su punto culminante cuando el acto comienza, su mano acariciando suavemente hacia arriba y hacia abajo como si se fuera a romper si se respirara sobre ello."

"No estoy seguro de si es solamente para calmarme o porque quiero calmarla, pero tomo mi mano libre y sostengo un costado de su rostro con ella. La sensación de su mano y su suave piel es agradable, y eso parece alivianar un poco su humor."

"El simple hecho de que estoy siendo tocado por ella es sorprendentemente erótico. Siento relajarse mi cuerpo mientras me rindo al incontenible placer."

"Pasan largos minutos casi en total silencio, nuestra respiración pesada el único sonido que se puede escuchar en la casa. Los dedos de Lilly dejan de acariciar con afecto mi cabello y ella abre sus labios una vez más."

show evh lilly_handjob_stroke_flustopen_small
with charachange

li "Hisao…"

"Espero un segundo por el resto de la frase, pero no le sigue nada. Podrá estar intentando tomar la iniciativa, pero aun así está increíblemente nerviosa."

"No puedo evitar sonreír mientras aparto el cabello de su cara un par de veces, reconfortándola."
"Tan nerviosa como pueda estar, agradezco que sea Lilly la que tome la iniciativa. Probablemente estaría igual de ansioso que ella si fuera yo el que la sirviera."

show evh lilly_handjob_stroke_normopen_small
with charachange

hi "De acuerdo."

"Ella se detiene un momento antes de asentir levemente, sentándose y pasando sus piernas por sobre las mías. Una vez más mi respiración me es arrebatada por la magnífica imagen de su cuerpo sobre el mío."

show evh lilly_cowgirl_smile_small
with whiteout

"Tan solo puedo mirar petrificado mientras ella delicadamente baja su cuerpo, posando sus labios enrojecidos sobre mí. Ella lentamente comienza a mover sus caderas hacia abajo, su tersura envolviendo mi consciencia."

show evh lilly_cowgirl_weaksmile_small
with charachange

"Ella respira profundamente para serenarse, su rostro permaneciendo firme. Con sus manos acogiendo mi cuerpo a falta de su vista, la situación íntima lía sus esfuerzos típicos de compensar por la falta de contacto visual."

"Gradualmente se baja hacia mí, sus rodillas y manos apoyándola mientras lo hace. Su cuerpo entero se tensa mientras entro, su expresión obviamente siendo una de dolor reprimido."

"A pesar de eso, no puedo evitar disfrutar de la cálida y suave sensación que envuelve mi consciencia, la ola de placer abrumando todos mis sentidos."

"Los últimos vestigios de ellos desaparecen dentro de ella mientras que sus uñas raspan un poco mi pecho en un intento para detenerse de chillar de dolor. Un gemido adolorido, demasiado para poder reprimirlo completamente, se escapa de sus labios."

"Cuando abro mi boca para reconfortarla, noto gotas rojas apenas visibles entre sus piernas."

hi "Lilly, si es demasiado…"

scene evh lilly_cowgirl_strain_small
with charachange

"Ella aprieta su boca firmemente, agitando con fuerza y rápidamente su cabeza de lado a lado en señal de resistencia. Luego de unos cuantos segundos relaja su cuerpo un poco, aunque obviamente está lejos de sentirse cómoda."

li "Es… está bien… estoy bien."

scene evh lilly_cowgirl_frown_small
with charachange

"Ella traga con fuerza, intentando calmarse."

"Levantándose lentamente y volviendo a bajarse, ella se relaja un poco más a medida que la sensación de placer comienza a sobrepasar la de dolor."

scene evh lilly_cowgirl_strain_small
with charachange

"Su respiración comienza a concordar con el mismo patrón entrecortado que la mía, su cuerpo moviéndose casi provocativamente lento. Pareciera que lentamente está comenzando a disfrutar del acto, mis sentimientos finalmente alcanzándola."

"No estoy seguro si va a esta velocidad por ella o por mí, pero de cualquier forma… con este ritmo lento y constante, creo que puedo… mantener mi cuerpo bajo control. Es divertido, de cierta forma, que incluso ahora dependo de ella."

"Que estemos unidos de esta forma, nuestros sentimientos tan cercanos… me hace feliz. Compartir nuestro primer momento juntos de esta forma… es un sentimiento… casi… sobrecogedor…"

hi "Te amo… Lilly…"

scene evh lilly_cowgirl_cry_small
with charachange

li "¡Hisao… Hisao…!"

"Puedo sentir su cuerpo tensarse, su respiración y movimientos perdiendo gradualmente el control."
"Me alegra hacerla sentir tan bien, pero a medida que mis pensamientos se concentran cada vez más, puedo sentirme acercándome rápidamente a mi límite."

scene white
with Dissolve(3.0)

"El control de mi cuerpo es arrebatado de mi mente en un instante mientras aprieto mis dientes con fuerza, dejando escapar un fuerte gemido cuando llego a mi clímax y mis caderas chocan con las de ella."

"Su cuerpo se encoge en ese mismo momento, sus senos tocando mi pecho."

"Permanecemos unidos en total éxtasis por un breve momento, mi mente completamente tomada por la sensación durante unos maravillosos segundos."

scene evh lilly_cowgirl_weaksmile_small
with charachange

"Todo acaba demasiado pronto y nuestros cuerpos colapsan de cansancio con Lilly apenas manteniéndose sobre mí."

"Sin energía alguna logro rodear con mis brazos su débil y sudoroso cuerpo, y durante varios minutos simplemente permanecemos ahí, disfrutando en silencio del contacto entre nosotros mientras nos recuperamos de la experiencia."

"Ninguno de nosotros se creía preparado para tal cosa, de eso estoy seguro."

"Completamente agotado, más allá del punto como para conversar, miro su rostro extenuado. Pareciera como si el esfuerzo, tanto físico como mental, la hubiera casi forzado al borde del colapso."

hi "Te amo, Lilly."

scene evh lilly_cowgirl_smile_small
with charachange

"Ella asiente débilmente, acariciando mi cabello con su mano izquierda. Si pudiéramos simplemente permanecer juntos así por una eternidad, sería un paraíso sin comparación."

stop music fadeout 2.0

scene black
with dissolve



label es_L18:

scene bg hok_lounge_rn
with locationchange

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_rain fadein 1.0

"Luego de ser despertado por un sonido, abro mis ojos con un grado de recelo."

"Girando mi cabeza hacia la izquierda, veo que la lluvia afuera choca contra las ventanas sonoramente. Rocío tras rocío azotan el vidrio por el viento, como si intentaran con todo su empeño compensar el calor veraniego anterior."

"Me siento en el futón, sosteniendo mi nuca para intentar aplacar el dolor por haber dormido en una posición incómoda."

"De todas formas debería estarme lamentando el cambio de clima, dado que es nuestro último día aquí. Pero los acontecimientos de ayer se niegan a dejar de invadir mi mente."

"La sensación de sostener el cuerpo en llanto de Lilly en mis brazos. La acometida de deseo y hormonas que nos recorrió al pasar la noche juntos. Parece casi inútil intentar racionalizar todo lo que pasó."

"En un intento por distraerme, gruño y me inclino para alcanzar mi maleta sin pararme. Sacando una botella tras otra, saco el régimen diario de medicamentos de sus contenedores y me los trago sin más."

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")

window hide
nvl show dissolve

nvl clear

n "\n\n\n\nTomó una cantidad sorprendentemente breve de tiempo acostumbrarme a tragar las pastillas sin agua. Dicho eso, supongo que lo mismo va para acostumbrarme a vivir en una escuela para estudiantes discapacitados."

n "Recordando Yamaku, me siento más agradecido de tener la oportunidad de alejarme, aunque sea por un mínimo tiempo."

n "Aprecio la oportunidad de pasar tiempo solo con Lilly y Hanako, lejos del ajetreo de la vida escolar, incluso considerando las últimas complicaciones."

n "Nunca pensé que lo diría, pero la idea de vivir lejos de la ciudad en un lugar tranquilo y agradable es atrayente. Es un pensamiento que, hace apenas un año atrás, me habría parecido simplemente ridículo."

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")

nvl clear
nvl hide dissolve

window show

"Un destello de rosado, sin duda alguna el camisón de Hanako, se asoma por la esquina. Dándome cuenta de que debo verme horrible ya que recién acabo de despertar, meto el resto de las píldoras en mi boca y paso mi mano por mi cabello."

show hanagown smile_rn at center
with charaenter

ha "Buenos días, Hisao."

hi "Ah, bu— ¡agh!"

$ renpy.music.set_volume(0.0, 0.2, channel="ambient")

with vpunch

"Le respondo olvidándome por completo de que estoy en medio de tragarme una píldora particularmente grande. Tosiendo y resoplando, me atraganto violentamente con ella."

show hanagown worry_rn
with charachange

ha "¡Ah, Hisao!"

$ renpy.music.set_volume(0.2, 10.0, channel="ambient")

"Luego de resoplar sonoramente y golpear mi pecho un par de veces para forzarla a bajar, logro recuperarme."

hi "Estoy bien. Lo siento, me olvidé que estaba tragando."

play music music_happiness fadein 5.0

show hanagown distant_rn
with charachange

ha "Lo lamento, no era mi intención—"

"Levanto mi mano, señalándole a Hanako que se detenga."

hi "Me atraganté. Es mi culpa. Buenos días, Hanako."

"Ella se detiene un momento antes de responder con una reverencia."

show hanagown distant_rn at tworight
show bg hok_lounge_rn at bgright
with charamove

show lilly basic_sleepy_paj_rn at twoleft
with charaenter

"Caminando, no, tambaleándose detrás de Hanako está la conocida figura de Lilly, también llevando su ropa de dormir. Con sus ojos llenos de sueño y su cabello enmarañado, es un espectáculo digno de ver."

hi "Hola, Lilly."

show lilly basic_weaksmile_paj_rn at twoleft
with charaenter

li "Buenos días… Hisao."

"Por un rato, un silencio domina el ambiente ya que ninguno de los dos sabe qué hacer."

"Dado lo que pasó anoche, ambos tenemos más que suficiente razón para encontrar la situación incómoda. ¿Cómo deberíamos reaccionar al encontrarnos después de algo como… eso?"

"El mejor camino a seguir probablemente sea hablar con Lilly a solas, para ordenar las cosas."

hi "Ah, yo… comenzaré a preparar el desayuno."

"Lilly evidentemente entiende lo que estoy pensando."

show lilly basic_smileclosed_paj_rn
with charachange

li "Lo ayudaré. Hanako, ¿podrías ordenar la mesa?"

"Ella asiente, su cabeza desapareciendo en un estante al ponerse rápidamente a trabajar en la tarea asignada."

$ renpy.music.set_volume(0.1, 0.5, channel="ambient")

scene bg hok_kitchen_rn
with locationchange

"Me froto un poco más los ojos para despertar mientras trastabillo hacia el refrigerador y saco algo de leche, y Lilly lleva varias cajas de colores brillantes de las despensas inferiores a mi lado."

"Mientras preparamos la comida de aspecto insípido, susurro más bajo de lo usual. Conociendo el oído de Lilly, no debería tener problemas en entender lo que digo."

hi "¿Estás bien, Lilly? Después de lo de anoche…"

show lilly basic_reminisce_paj_rn at center
with charaenter

"Ella asiente de forma delicada, su expresión débil."

"Si bien su cansancio seguramente juega su parte, ella parece genuinamente insegura sobre lo que pasó entre nosotros, y cómo seguir. No puedo culparla, considerando que mis sentimientos son exactamente los mismos."

show lilly basic_sad_paj_rn
with charachange

li "Lo siento, Hisao. No estaba pensando con claridad ayer. Nunca me detuve a considerarte a ti o a Hanako, e incluso llegué a…"

"Comienza a agitarse. Con sus manos y su voz tensándose, le doy un suave golpe para intentar aliviar la situación."

hi "No tienes que disculparte. Después de todo, yo también dije que me gustabas."

show lilly basic_oops_paj_rn
with charachange

li "Pero yo…"

"A medida que su compostura comienza a desvanecerse, se hace obvio que no hay alternativa."

show lilly basic_sad_paj_close_rn
with characlose

"Dándome vuelta hacia Lilly, dulcemente abrazo su alta figura. Ella no opone resistencia en absoluto, afortunadamente apartándose, apenas, del borde de sus emociones."

show lilly basic_sad_paj_close_rn at twoleft
show bg hok_kitchen_rn at bgleft
with charamove

show hanagown normal_rn at tworight
with charaenter

"A pesar de que nuestro reconfortante abrazo duró apenas segundos, noto a Hanako observando sin decir palabra. El plato en su mano está suspendido a centímetros de la mesa, su acción detenida a medio camino por lo que ha visto."

stop music fadeout 2.0

scene bg hok_lounge_rn
show hanagown distant_rn:
    tworight
    ypos 1.15
show lilly basic_sleepy_paj_rn:
    twoleft
    ypos 1.17
with shorttimeskip

$ renpy.music.set_volume(0.2, 0.5, channel="ambient")

"El choque de los utensilios contra los platos es el único sonido que se puede escuchar mientras comemos en silencio. Si bien antes solo dos de nosotros podíamos habernos sentido inseguros de nosotros mismos, la situación entera ha cambiado."

"Luego de semanas de dichosa amistad, pasando los días compartiendo las comidas y con conversaciones sin mucho significado, la relación entre Lilly y yo, no, la de todos nosotros, ha cambiado irreversiblemente."

"No puedo soportar esto."

hi "Lilly…"

stop ambient fadeout 25.0

show lilly basic_listen_paj_rn
with charachange

"Ella asiente solemnemente, dejando con delicadeza su cuchara en el plato frente a ella. Ninguno de nosotros sabe exactamente cómo considerar al otro, mucho menos cómo nos verá Hanako."

show lilly basic_weaksmile_paj_rn
with charachange

li "Esto podrá sonar repentino pero… me he confesado a Hisao."

show hanagown distant_blush_rn
with charachange

"Por un momento, Hanako parece casi confundida; precisamente la reacción que pensé que tendría. Ella eventualmente asiente, su cuchara aún en su boca mientras lo hace."

show hanagown normal_blush_rn
with charachange

ha "¿Aceptaste?"

hi "Lo hice."

show hanagown smile_rn
with charachange

"Ella sonríe de forma tan amplia y honesta, que me encuentro a mí mismo sonrojado. Creo que es la expresión más radiante que le he visto."

play music music_serene fadein 6.0

ha "Entonces estoy feliz. Estoy muy, muy feliz."

show lilly basic_sleepy_paj_rn
with charachange

li "Lo siento por no haberte dicho nada antes. Las cosas han sido…"

"Hanako mueve la cabeza de lado a lado con énfasis, aparentemente olvidándose en su apuro de que Lilly no podría notarla."

show hanagown distant_blush_rn
with charachange

"Ella comienza a jugar con sus dedos, pareciendo un poco más nerviosa que antes."

ha "A decir verdad, comencé a pensar que podrían gustarse hace tiempo. Al principio en realidad no sabía qué pensar al respecto… pero yo…"

show hanagown smile_rn
with charachange

ha "Decidí al final que… si mis amigos son felices, entonces yo soy feliz."

ha "De verdad me alegró tener otro amigo cuando conocimos a Hisao, así que el que hayas encontrado el amor a través de él es incluso mejor… ¿cierto?"

"Una sensación de alivio por la aprobación de nuestra relación me cae como una ola. Lo mismo pasa con Lilly, a juzgar por su expresión."

show lilly basic_weaksmile_paj_rn
with charachange

li "Gracias, Hanako. De verdad aprecio que seas tan comprensiva."

show hanagown distant_rn
with charachange

"La voz de Lilly aún suena un tanto arrepentida, o al menos insegura. Eso no se le pasa a Hanako, quien parece perderse en sus pensamientos por unos cuantos momentos antes de voltear hacia mí."

show hanagown smile_rn
with charachange

ha "Hisao, ¿te molesta si Lilly y yo salimos por un momento?"

hi "Ah, no, siéntanse libres…"

show lilly basic_surprised_paj_rn
with charachange

li "¿Hanako?"

show hanagown smile_rn at tworight
with charamove

show lilly basic_surprised_paj_rn at twoleft
with charamove

hide lilly
hide hanagown
with charaexit

stop ambient
$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

"Hanako se levanta de su asiento, tomando la mano de Lilly y casi arrastrándola de la mesa por su entusiasmo. Considerando el ritmo lento y firme típico de Lilly, la prisa de Hanako hace que sus pisadas sean torpes y casi pierde su balance un par de veces."

"Es un espectáculo bastante gracioso, que me deja sin palabras mientras las veo desaparecer por la puerta."

"Solo ahora me doy cuenta de que la lluvia se ha detenido, reemplazada por un cielo mucho más vívido y brillante para compensar por la matutina extensión de gris apagado."

"Para Hanako, esta debe ser una revelación bastante grande. Lilly y yo de verdad somos los únicos con quienes se asocia, casi como si fuéramos padres para ella."

"Supongo que esa bien podría ser la mejor manera de describir la relación que compartimos. Un padre, una madre y una hija, todos jugando en nuestra pequeña familia de fantasía como si pudiera durar para siempre."

"Podrá ser una dinámica extraña, y una que ciertamente no puede durar por mucho tiempo… pero quizás, solo por este pequeño momento, está bien."

"Cuando me levanto de la mesa y voy a reunirme con Lilly y Hanako en el campo afuera, me asiento a mí mismo en afirmación."

"Este pequeño momento de felicidad, sin importar lo breve que sea, estará conmigo, con todos nosotros, para siempre."

stop music fadeout 2.0

label es_L19:

scene bg hok_bath
show steam
with shorttimeskip

"Sumergido en el agua caliente, dejo que un largo suspiro se escape de mis labios. La sensación de que aparentemente todos los músculos de mi cuerpo se relajen es eufórica."

"No tengo idea de cuánto ha pasado desde que me di un verdadero baño con agua caliente, pero ahora mismo no me interesa intentar recordar."

play music music_dreamy fadein 2.0

nvl clear
window hide

nvl show dissolve

n "Quizás le estoy dando al simple hecho de que por fin puedo darme un baño verdadero más crédito del que merece; la oportunidad de simplemente calmarme, permitirme relajarme y tener tiempo para mí mismo es bienvenida."

n "Hanako, Lilly y yo vagamos afuera, explorando la extensión de la sorprendentemente amplia área de tierra que rodea la casa. Luego pasamos la mayor parte de la tarde descansando, mirando la televisión, leyendo, y jugando cartas."

n "Puede no haber sido el final más emocionante para el viaje, pero tal tranquilidad tan serena es algo para saborear. Incluso luego de que regresemos a la escuela mañana, creo que recordaré esta pequeña casa en Hokkaido por un largo tiempo."

n "Es una lástima que solo nos queden unas cuantas horas para pasar aquí antes de tomar el tren de vuelta."

n "Lo único que puedo hacer es bostezar satisfecho mientras miro el vapor subir lentamente desde la apacible y clara superficie del agua, mis ojos eventualmente fijándose en el techo."

n "Nuestros exámenes son inminentes. Apenas he estudiado para ellos."

n "Y además de eso, ni siquiera sé qué haré después de graduarme. Pasar los exámenes está bien y todo, pero ¿con qué fin?"

n "Y ahora, de todos los momentos, estoy entrando en una relación."

nvl clear
nvl hide dissolve
window show

hi "¿Qué demonios estoy haciendo?"

"…"

"… Supongo que no debería pensar de esa forma. Lo hecho, hecho está, y quizás esto pueda ser visto como otro aspecto de mi nueva vida en la que estoy trabajando."

"Disfruto estando con Lilly, y después de todo la vida es más que la escuela y una carrera."

"Mientras intento afanosamente racionalizar todo lo que ha pasado, oigo una serie de golpes en la puerta. Me levanto y me siento derecho, intentando adivinar el origen."

"Tres, no más y no menos. Ligeros pero asertivos en su golpeteo, y espaciados tan regularmente que podrían calibrar un metrónomo. Estaría extremadamente sorprendido si no fuera Lilly."

li "¿Puedo… entrar?"

"Sí, es Lilly."

hi "Sigo en la bañera, saldré en un segundo."

li "… Lo sé."

stop music fadeout 3.0

"La voz que viene del otro lado de la puerta me paraliza. Luego de pensarlo un segundo, me acuesto de lado en la bañera y dejo caer mis brazos sobre el costado de ella."

"A pesar de hacer mi mejor esfuerzo para disimularlo, no puedo evitar dejar que mi mente divague."

hi "C-claro, entra."

show lilly basic_smileclosed_cas at Alphain(1.0), Slide(0.4, 0.5, 0.5, 0.5, 1.0)
with Pause(1.0)

"Con eso abre la puerta, entrando lentamente al cuarto y cerrando la puerta detrás de ella. Parece extrañamente calmada, contrarrestando mi corazón acelerado."

hi "Ah… ho-hola… Lilly."

play music music_one fadein 9.0

show lilly basic_smile_cas at center
with charachange

li "¿Te incomoda si tomo un baño contigo?"

hi "Para nada. Adelante."

show lilly basic_listen_cas at center
with charachange

"Asintiendo ligeramente ella comienza a quitarse el suéter de sus hombros, descubriendo su pecho poco a poco."

hi "Puedo hacer eso por ti, si quieres."

show lilly basic_emb_cas at center
with charachange

li "Rechazado."

hi "¿Por qué?"

show lilly basic_pout_cas at center
with charachange

li "…"

"Su rostro me dice que aún no se siente del todo cómoda dejándome asistirla. No puedo decir que la culpe."

hide lilly
with charaexit

play sound sfx_rustling

"Ella sigue desvistiéndose, su camisa y falda cayendo al suelo dejándola con su sujetador y pantaletas de encaje blanco. Eventualmente, queda desnuda en el centro del cuarto."

label es_L19h:

show lilly behind_sleepy_nak at center
with charachange

"Comparado con la última vez, es mucho más fácil abarcar su figura entera. Es una imagen maravillosa."

li "¿Hisao?"

hi "¿Hmm?"

show lilly behind_pout_nak at center
with charaenter

li "Estás pensando cosas pervertidas, ¿no es así?"

hi "Dame un respiro, te estás desnudando frente a mí."

show lilly behind_weaksmile_nak at center
with charachange

"Ella frunce el ceño, pensativa."

li "Supongo que esto será un tanto más erótico para ti que para mí."

hi "¿Por qué?"

hi "… Ah."

show lilly behind_giggle_nak at center
with charachange

"Suelta una risita alegre, la cual parece calmar un poco sus nervios."

show lilly behind_smile_nak at center
with charachange

li "Si esto es demasiado para ti, Hisao, puedo volver luego."

hi "No, no, está bien. Solo estoy un poco… bueno…"

hi "Eres realmente hermosa, sabes."

show lilly behind_emb_nak at center
with charachange

"Mi comentario en serio le saca a Lilly un vivo rubor."

li "Hisao…"

"Pongo una sonrisa. Ella es linda cuando se le toma desprevenida."

show lilly behind_smileclosed_nak at center
with charachange

li "De cualquier modo, ¿puedo entrar?"

hi "Ah, claro."

hide lilly
with charaexit

"Me inclino hacia adelante y tomo sus suaves manos con las mías, ayudándola por sobre el costado de la bañera."

"Ella tantea el costado de la bañera y luego baja lentamente, mi respiración deteniéndose cuando se sienta y apoya su espalda contra mi frente, sus piernas entremedio de las mías. Esperaba que se sentara al otro costado."

scene evh lilly_bath_smile_small
with whiteout

"Soltando una larga exhalación para calmarme, apoyo mis brazos en los costados de la bañera mientras me esfuerzo por controlar mis deseos."

"Lejos de perderme de vista sus… atributos, la sensación de su cuerpo contra el mío es sorprendentemente relajante. Si Lilly es tan sensible al tacto, debe serlo con mayor razón para ella."

li "Tomas tus baños bastante calientes, ¿no es así?"

hi "Un poco. ¿Quieres que deje correr algo de agua fría para entibiarla un poco?"

"Ella niega ligeramente con la cabeza."

li "No, así está bien."

hi "De acuerdo."

"La conversación llega a un súbito fin, siendo reemplazada por silencio."

show evh lilly_bath_emb_small
with charachange

"Un muy largo, y muy incómodo, silencio."

li "Quizás esto fue algo dema…"

hi "No te preocupes, está bien."

"La situación solo se torna más incómoda. Como para distraerse, Lilly pasa su mano libre por sus piernas mientras mantiene una sobre sus senos por recato."

"Me siento mirando ociosamente la pared frente a mí y el vapor que sube, de vez en cuando echando una mirada a su cuerpo."

"El blanco de su piel reluce mientras ella continúa pasando su mano por sus piernas, su largo y su tono aún más evidentes."

hi "Sabes, comparada con Akira, te vez mucho más como una extranjera."

li "Genéticamente tengo del lado de mi madre. Akira tiene más de mi padre."

hi "Supongo que eso tiene sentido. ¿Cómo diantres una escocesa nativa y un empresario japonés se conocieron, de todos modos?"

li "Mi madre era reportera. Conoció a mi padre cuando él fue a una conferencia en Inverness."

hi "Ah, ya veo. Que tengas de tu lado escocés también explicaría tu altura, supongo."

"Bajo la mirada hacia ella mientras me asiente, y suspiro ante lo ridículo de la situación."

hi "Esto de verdad es demasiado, ¿no es así?"

show evh lilly_bath_smile_small
with charachange

li "Pero lo estás disfrutando, ¿o no?"

hi "De cierta forma, sí. Supongo que las cosas salieron bien, al final."

hi "Todo se ha arreglado, Hanako tomó bien nuestra relación, y volveremos a la escuela mañana."

li "Así es. Es una pena volver tan pronto, pero seguiremos teniendo nuestros recuerdos de este lugar."

hi "¿Recuerdos, eh? Eso supongo. Tendremos que ver cómo va todo una vez que regresemos, pero por ahora… simplemente estoy feliz de que yo te guste."

hi "He estado angustiándome durante semanas por eso, así que agradezco que las cosas hayan resultado de esta forma."

"Ella asiente, apoyándose en mí mientras compartimos el calor de nuestros cuerpos."

"No estoy seguro si estará de acuerdo con ello o no, pero mi tentación rápidamente comienza a poder más que mi autocontrol."

hi "¿Oye, Lilly?"

li "¿Sí?"

hi "¿Cómo estuvo? Anoche, digo."

"Ella se detiene a pensar antes de bajar un poco la mirada. Una sonrisa delicada se abre camino hacia sus labios mientras se sonroja, su cuerpo relajándose aún más. Es más que suficiente para responder la pregunta."

"Aun mientras asiento en respuesta, recuerdos de anoche recorren mi mente. Considerando la situación, en realidad no creo que alguien pueda culparme."

li "Hisao, tu corazón está latiendo…"

"Su voz es interrumpida cuando coloco delicadamente una mano en su muslo. Si bien resistí antes, el recuerdo de nuestra primera vez es suficiente para hacer que ceda."

"Ella deja que su cuerpo se apoye sobre el mío sin protestar, una invitación que me sería difícil ignorar. Planto un ligero beso en su cuello para aceptar, antes de mover mi mano lentamente por sobre sus suaves piernas."

li "Hisao, por favor…"

"Incluso mientras dice eso, su boca se curva en una sonrisa, su tono entre avergonzado y una risita incómoda."

show evh lilly_bath_open_small
with charachange

"Eventualmente ella toma una de mis manos con la de ella, guiándola hacia su seno derecho. Aprecio enormemente la guía tentativa que ella está dispuesta a darme."

show evh lilly_bath_grab_small
with charachange

"Todas las señales de tensión en su cuerpo desaparecen. Continúo acaparando la sensación de su suave piel, acrecentada mientras mi otra mano se desliza entre sus piernas."

"Me pregunto si la sensación de mis manos sobre ella se ve exagerada por su falta de vista, ya que sus otros sentidos están tan bien ajustados."

"Ella parece estarlo disfrutando en sorprendente demasía, después de todo. Me da una sensación un tanto extraña, pero placentera."

show evh lilly_bath_moan_small
with charachange

"Solo toma unos cuantos minutos para que su cuerpo comience a retorcerse sutilmente, sus esfuerzos para callar sus gemidos volviéndose visibles al fruncir sus labios. Sus alegres y susurradas protestas se vuelven notoriamente más débiles."

"Eso me hace darme cuenta de que todo lo que se ha retorcido contra mi cuerpo me ha excitado cada vez más también."

hi "Lilly…"

show evh lilly_bath_smile_small
with charachange

"Retiro mis manos para darle a sus confundidos sentidos tiempo de responder. Asintiendo, ella se para temblorosa y me ofrece su mano para que la conduzca fuera de la apretada bañera."

scene evh lilly_afterbath_open_small
with locationchange

"Ella maniobra para salir de la bañera junto conmigo, nuestras manos sostenidas entre sí."

"Eventualmente me siento junto a la bañera, ambos moviéndonos hasta ponernos cómodos. Con una ligera exclamación, reprimida desesperadamente para evitar ser audible afuera, ella baja su cuerpo sobre el mío una vez más."

"La forma en que se mueve hace obvio el que debe aún estar al borde del clímax."

"Ella lentamente comienza a mover sus caderas hacia arriba y hacia abajo, su lengua encontrándose con la mía al sostener ella mi cabeza hacia arriba. Me doy cuenta de lo mucho que darle placer me ha excitado."

scene evh lilly_afterbath_shut_small
with locationchange

li "Hisao… Hisao…"

"A pesar de que sus nublados ojos permanecen cerrados, su firme agarre en mis hombros indica que está por acabársele la resistencia."

"A medida que nuestra respiración se torna cada vez más y más irregular, rápidamente siento que también alcanzo mi límite."

"Una serie de respiros estridentes es la única advertencia antes de su última exclamación de éxtasis, su cuerpo entero tensándose y sus uñas enterrándose en mis hombros."

"Mi entrepierna golpea la suya, ambos paralizados contra el otro en clímax."

with Fade(0.5,1.0,4.0, color="#FFF")
stop music fadeout 8.0

"En unos cuantos valiosos segundos, todo ha acabado, Lilly desplomándose hacia mí mientras intento recuperarme."

hi "Eso fue… bueno…"

"Ella toma una bocanada de aire antes de responder, recobrándose mientras asiente."

li "Mm…"

"Ella inclina su cabeza hacia abajo para darme un ligero beso, y mi mano se extiende para sostener hebras de su desordenado cabello mientras una vez más nos sentamos en dichoso silencio."

stop music fadeout 2.0

scene black
with dissolve

label es_L20:

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_trainint fadein 5.0

scene ev lilly_trainride_ni
show train_scenery_ni
show train_scenery_fg_ni
show lilly_trainride_ni norm at train_shake
with locationchange

"Después de una caótica carrera a la estación y encontrar nuestros asientos en el carro de otro modo vacío, de inmediato caemos. Viendo la hora —cerca de medianoche— no es de sorprender que pocos tomen este tren en particular."

"Hanako está profundamente dormida sobre el hombro de Lilly y yo apenas puedo reunir suficiente energía para permanecer despierto. La agitación que tuvimos hace poco probablemente no ayudó."

"Probablemente estaría bastante deprimido por tener que volver a la escuela si mi cerebro estuviera funcionando."

"Como está, sin embargo, la imagen del paisaje nocturno que va pasando es sorprendentemente hermosa."

"Mi sonoro bostezo es tapado casi por completo por el claqueteo de la vía del tren y el repiqueteo del viejo carro."

hi "Tan cansado…"

play music music_comfort fadein 2.0

show lilly_trainride_ni ara at train_shake
with charachange

li "¿Y quién tiene la culpa de eso, Hisao?"

"Ella de verdad alcanza la línea entre ofensiva y divertida a veces. Aunque logro forzar una sonrisa cansada."

"Vuelvo a mirar por la ventana, mi reflejo apenas visible en el transparente cristal. A decir verdad, ella tiene toda la razón. Si no fuera por ese pequeño interludio hace unas cuantas horas, ambos tendríamos mucha más energía."

"Y además, ambos tuvimos que bañarnos otra vez, casi haciendo que llegáramos tarde a la salida del tren."

hi "Claro, claro, fue mía. De todas formas, meterse a una bañera con un hombre es algo peligroso."

show lilly_trainride_ni smile at train_shake
with charachange

li "Evidentemente."

hi "Lo siento. Supongo que tomé ventaja de la situación en ese momento."

show lilly_trainride_ni weaksmile at train_shake
with charachange

li "Bueno… No me disgustó precisamente…"

"Cuando deja de hablar, vuelvo la mirada hacia ella. Mis ojos se estrechan cuando veo sus mejillas un tanto ruborizadas y una pequeña sonrisa, su mente obviamente en otro lugar."

hi "Dilo."

li "Yo… sabía que existía la posibilidad… de que eso sucediera."

hi "Lo sabía. Tienes la mente tan sucia como yo."

"Ella rápidamente tose sobre su mano, dejando claro como el agua su disconformidad."

show lilly_trainride_ni pout at train_shake
with charachange

li "Esa es una manera bastante vulgar de decirlo."

hi "¿Oh? ¿Y qué sugieres tú?"

li "Simplemente tengo un sano impulso sexual adolescente."

hi "En otras palabras, mente sucia."

"Casi pareciendo sentir el momento, Hanako murmura en silencio mientras frunce su ceño en el regazo de Lilly."

show lilly_trainride_ni opensmile at train_shake
with charachange

"La expresión de disconformidad de Lilly desaparece al sonreír y acariciar con su mano el largo y oscuro cabello de Hanako."

"Todo lo que puedo hacer es observar. Observar y sonreír."

"Si alguien fuera a preguntarme cuándo me enamoré de ella, no sería capaz de responder. Lo mejor que se me podría ocurrir sería “solo sucedió en algún momento, pero no me di cuenta”."

"Si alguien fuera a preguntarme por qué la amo, sin embargo, entonces podría responder con mucha más facilidad."

hi "De verdad amas a Hanako, ¿no es así?"

show lilly_trainride_ni smile at train_shake
with charachange

"Ella asiente profundamente, sonriendo de forma afectuosa."

label es_choiceL20:
menu:
    with menueffect
    li "Es una lástima que tengamos que regresar a la escuela. Ella pareció relajarse tanto mientras estábamos apartados."
    "Hablar de Hanako.":


        return m1
    "Hablar de la escuela.":

        return m2


label es_L20a:


$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

hi "Yo no me preocuparía. Hanako ha estado ganando confianza gracias a ti, al menos desde que las conozco."

show lilly_trainride_ni weaksmile at train_shake
with charachange

"Ella suelta un suspiro autocrítico."

li "Creo que simplemente le di compañía y apoyo. Desde que ella te conoció se ha abierto mucho más, hasta a mí."

"Tengo la sensación de que ella está menospreciando su influencia en Hanako, especialmente dado que antes de que las dos se conocieran, Hanako no tenía amigos."

"Los amigos que tenía en mi escuela anterior cumplían lo que esperaba de ellos, en su mayor parte simplemente estar ahí para platicar, pero en el caso de Hanako y Lilly de verdad hay sentimientos en su relación."

"Una parte de mí lo envidia, pero otra parte no puede ignorar el hecho de que el año escolar eventualmente acabará. Luego de la graduación, de verdad no tengo idea de lo que hará Hanako."

"Este viaje me ha enseñado lo mucho que hemos llegado a dependernos el uno de los otros."

"Sin duda alguna, todos vamos a tener que tomar decisiones. Quizás ese es el motivo por el cual, a pesar de que nuestro regreso a la escuela también anuncia un regreso a la normalidad de la vida cotidiana, no puedo evitar sentirme un poco inquieto."

label es_L20b:


$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

hi "Cierto. También comenzarán los exámenes, lo cual es otro tema que tratar. ¿Crees que estás preparada para ellos?"

show lilly_trainride_ni weaksmile at train_shake
with charachange

li "Eso creo. Pero no creo que sea un periodo agradable en absoluto."

"No puedo decir que esté en desacuerdo con ella. Los exámenes se me habían olvidado por completo por un tiempo, y a pesar de que pueda irme bien en la mayoría de las pruebas, no puedo asumir que pasaré fácilmente con tan poco estudio previo."

"Lilly parece ser más estudiosa, o al menos más regular, que yo. Dicho eso, ella tiene que lidiar con que le vaya bastante mal en algunas materias sin importar lo mucho que lo intente."

hi "Al menos durará solo un par de semanas."

label es_L20c:


hi "Del lado positivo, no faltará mucho para que lleguen las vacaciones de verano después de que se acaben los exámenes. Podríamos venir aquí durante las vacaciones de verano si quieres."

"Por un momento ella piensa la idea, su rostro volviéndose un tanto distante. Solo puedo suponer que está pensando en todo lo que ha pasado en este lugar."

show lilly_trainride_ni opensmile at train_shake
with charachange

li "Eso sería… bueno, creo."

"Asiento aprobando, sonriéndole."

"Verano, junto a Lilly. Esta idea parece la forma perfecta de pasar nuestras vacaciones."

stop music fadeout 3.0
stop ambient fadeout 3.0

window hide
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
