label es_L21:

window hide None

scene bg school_scienceroom
with locationchange

nvl clear
nvl show dissolve

$ renpy.music.set_volume(0.5, 1.0, channel="music")
play music music_normal fadein 1.0

n "\n\n\nDespués de la emoción de nuestro viaje a Hokkaido, parece extraño volver de pronto a la rutina diaria. En efecto, se siente como un día normal, como cualquier otro."

n "\nBueno, eso es lo que me gustaría pensar, de todos modos."

n "\nA decir verdad, el ambiente del grupo entero, no, de la escuela entera ha cambiado."

n "Si bien antes un trasfondo de sutil agitación había dominado al grupo, ahora que los exámenes están a la vista ha hecho erupción transformándose en un frenético estudio raramente visto de otro modo."

n "Queda un día para que comiencen los exámenes. Es horrible, de verdad, que en lugar de estudiar hayamos ido a desperdiciar nuestro tiempo al norte. Y éramos estudiantes modelo, además."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

show misha invis_close:
    xanchor 0.5 xpos -0.1
with None

show misha perky_confused_close:
    xpos 0.1
show bg school_scienceroom at bgright
with dissolvecharamove

window show

"Echando una mirada alrededor de la clase, hasta la alegre y siempre enérgica Misha parece curiosamente desanimada. Está sentada en su banco, mordiendo nerviosamente un lápiz mientras Mutou imparte la lección desde el frente de la clase."

"Espera… viendo más de cerca, creo que está comiéndoselo."

show misha invis_close:
    xpos -0.1
show bg school_scienceroom at center
with dissolvecharamove

hide misha
with None

"Apartando mis ojos de tan triste espectáculo, dirijo mi atención hacia otro lugar."

show hanako invis:
    xanchor 0.5 xpos 1.1
with None

show hanako defarms_strain:
    xpos 0.94
show bg school_scienceroom at bgleft
with dissolvecharamove

"Hanako está sentada escribiendo desesperadamente en su cuaderno, su rostro apenas a unos cuantos centímetros de la página, aparentemente intentando grabar cada palabra que sale de la boca de Mutou."

show shizu invis:
    xanchor 0.5 xpos 0.0
show misha invis_close:
    xanchor 0.5 xpos -0.1
with None

show shizu basic_normal:
    xanchor 0.5 xpos 0.3
show misha perky_confused_close:
    xpos 0.1
show hanako invis:
    xpos 1.1
show bg school_scienceroom at bgright
with dissolvecharamove

hide hanako
with None

"Shizune, bueno… es Shizune. Más fresca que una lechuga, está sentada tomando apuntes esmeradamente con su atención completamente dedicada al frente del salón."

"A decir verdad, eso es lo que yo debería estar haciendo también, si no fuera por el hecho de que siento que ya tengo un manejo bastante bueno de lo que se está tratando."

"Me pregunto cómo le irá a Lilly. Si bien ella tiene la cabeza en su sitio, tiene bastantes cosas que atender, a diferencia de mí."

"Sus deberes como representante de su clase, cuidar a Hanako, sus otros contactos sociales, sus estudios extras de inglés… esa chica de verdad se hace cargo de mucho."

scene bg school_scienceroom
with shorttimeskip

play sound sfx_normalbell

"La campana del almuerzo saca un suspiro de alivio del grupo entero, incluso Mutou."

"Me da la sensación de que debe preferir el ambiente más relajado de sus clases normales al ritmo agitado de la preparación para el examen al que estamos sometidos en estos momentos."

mi "Hicchan~…"

show misha invis_close:
    xanchor 0.5 xpos 0.1
with None

show misha perky_sad_close at twoleft
show bg school_scienceroom at bgright
with dissolvecharamove

mi "Ayúdame~…"

"Dejo mis párpados a medio bajar, dejando en claro mi intención de hacer lo contrario."

mi "Ayúdame, ayúdame, ayúdame~…"

hi "¿No vas bien?"

show misha perky_confused_close
with charachange

mi "A Shicchan le va a ir bien, pero creo que yo podría morir. ¿Voy a morir, Hicchan? ¿Me dejarás morir por todo este trabajo?"

"Qué sentimental. Dado que ella no es ni la estudiante más brillante del grupo, ni la más aplicada, no me sorprende que le parezca difícil lidiar con la carga."

hi "Lo siento Misha, pero tengo mi propio trabajo que hacer. De todas formas pensé que tú y Shizune habrían estudiado juntas durante el fin de semana largo, ¿no?"

show misha sign_sad_close
with charachange

mi "¡Estudiar es demasiado aburrido para perder unas vacaciones, Hicchan! Ir de compras juntas fue mucho más divertido, ¿no es así, Shicchan?"

show shizu behind_blank at tworight behind misha
with charaenter

"Recién ahora me doy cuenta de que Shizune ha estado mirando hacia nosotros, y que los brazos de Misha se han estado moviendo posiblemente todo este tiempo. De verdad debo estar bastante distraído como para no haberlo notado."

hi "¿Qué pasa con las mujeres e ir de compras, de todas formas? Hasta Lilly y Hanako me han arrastrado con ellas un par de veces."

show misha hips_grin_close
with charachange

mi "¿Pero fuiste de todos modos? Es raro ver a un hombre a quien le guste ir de compras~…"

hi "Bueno, mi rol probablemente pueda ser descrito como “mula de carga”. No puedo decir que comparta tu entusiasmo por la experiencia."

hi "De vuelta a los exámenes; estudiaste después de regresar de los días libres, ¿verdad, Shizune?"

show shizu basic_normal2
with charachange

shi "…"

show misha sign_smile_close
with charachange

mi "Por supuesto, Hicchan. Es de lo más sensato estudiar durante los días antes…"

show misha perky_sad_close
with charachange

mi "U~rgh."

"Misha hace un sonido vagamente parecido al de una vaca moribunda al darse cuenta de su insensatez y sin reparos se desploma en su banco, traicionada hasta por su mejor amiga."

show shizu basic_angry
with charachange

"A juzgar por la mirada bastante frustrada de Shizune hacia Misha, probablemente le haya dicho que estudiara como ella."

hi "No te preocupes, todavía puedes lograr una mejor calificación si comienzas a estudiar ahora."

hi "Quizás."

"Misha no parece demasiado divertida. Parece que el globo vivaz de alegría eterna ha sido reventado cruelmente."

show shizu behind_blank
with charachange

shi "…"

show shizu behind_blank_close
with characlose

with Pause(0.3)

show shizu adjust_frown_close
show misha perky_confused_close
with vpunch

"La señas de Shizune pasan sin ser notadas por una Misha deprimida, lo que le gana un rápido toque en el hombro. Toma apenas un momento para que Misha vuelva a estar en forma."

show misha hips_smile_close
with charachange

mi "Oh, ah, ¿y qué hiciste tú el fin de semana, Hicchan?"

hi "Solamente hice un viaje al norte con Lilly y Hanako. Fue muy agradable."

show misha perky_smile_close
show shizu behind_blank_close
with charachange

"Las veo mirándome con los ojos entrecerrados, sus mentes seguramente pensando vulgaridades. El hecho de que sus sospechas estén fundadas hace que la situación sea aún más incómoda."

hi "Solamente estudiamos y recorrimos el lugar; no pasó nada más."

show misha cross_smile_close
with charachange

mi "Hmm~…"

"Después de una mentira tan flagrante, me doy cuenta de que quizás no fue el mejor camino para seguir, considerando las conexiones de Shizune y su total falta de control cuando se trata de interrogar a alguien que sospecha dice falsedades."

"En realidad no tengo idea de cómo vaya a tomárselo, pero lo averiguará eventualmente de todas formas. No es como si fuera asunto suyo con quién salgo, de todas formas."

hi "Y sí, Lilly y yo estamos saliendo."

show misha hips_grin_close
show shizu basic_normal2_close
with charachange

"Mientras Misha recibe la noticia con una sonrisa entusiasta, Shizune me lanza una mirada de sorpresa moderada un tanto encubierta por su actitud fría."

show shizu behind_blank_close
with charachange

shi "…"

show misha sign_smile_close
with charachange

mi "Con quién salgas es asunto tuyo. Espero que ustedes dos vayan bien juntos."

"Misha me mira como para decir que esto es todo el respiro que podría conseguir con respecto al tema. Es todo lo que quería, en realidad."

show shizu basic_normal2_close
with charachange

"Pero después de decir esto, Shizune comienza a hacer señas para decir algo más, y se detiene y mueve su cabeza hacia Misha para evitar que traduzca."

hide shizu
with charaexit

hide misha
with charaexit

"Normalmente pensaría que esto es bastante extraño, pero la seña extrañamente casual que Shizune me da antes de marcharse con Misha tras de ella aumenta mi confusión."

"Shizune difícilmente es de las personas que se reservan cosas o se comunican sin pensarlo."

"Me encojo de hombros ante el extraño comportamiento del dúo y miro hacia el banco de Hanako, pero veo que su silla está vacía. Ella definitivamente estaba aquí antes, así que supongo que no tenía ganas de esperar."

"Entonces iré a buscar algo de comida solo."

stop music fadeout 2.0

scene bg school_hallway2
with shorttimeskip

"Caminando por el pasillo hacia la habitación desocupada que se ha vuelto un segundo hogar para tres estudiantes en particular, bajo la mirada de forma penosa hacia el arrollado primavera envuelto en plástico y la caja de jugo en mi mano."

"La comida de la cafetería de verdad no es apetitosa. Quizás consideraré esto mi castigo por mis indiscreciones recientes."

"Al abrir la puerta, noto una figura tranquila menos de las que esperaba."

scene ev lilly_tearoom
with whiteout

play music music_lilly fadein 3.0

"Es extraño. A pesar de conocer a Lilly por meses ya, no puedo evitar recordar la primera vez que abrí esta puerta y la vi sentada en silencio bajo la luz del sol."

show ev lilly_tearoom_open
with charachange

"Tal como en ese entonces, ella abre lentamente sus ojos, tan quietos como puedan estar, y me dirige la palabra tranquilamente."

li "Buenos días, Hisao."

hi "Ya es de tarde, creo."

hi "¿Ha estado Hanako por aquí? Se coló fuera de la clase sin que lo notara."

scene bg school_miyagi
show lilly basic_listen_close:
    center
    ypos 1.1
with locationchange

"Lilly sostiene su mejilla pensativa mientras tomo asiento, mi mochila tomando su lugar contra la pata más cercana de la mesa y mi comida poco satisfactoria puesta ordenadamente frente a mí."

show lilly basic_reminisce_close
with charachange

li "Se apareció… por un rato. Dijo que tenía que estudiar para los exámenes que vienen, y se fue a la biblioteca."

"Nos vemos incapaces de creer en sus palabras por completo."

hi "Bueno, por lo menos sus intenciones son buenas."

show lilly basic_concerned_close
with charachange

li "Ella es amable, pero no necesitaba ir tan lejos para dejarnos tener nuestro espacio. Quizás hable con ella al respecto en algún momento."

hi "Probablemente sea lo mejor."

show lilly basic_weaksmile_close
with charachange

"Por un rato comemos en silencio, Lilly mordiendo elegantemente sus emparedados y sorbiendo su té mientras yo me como algo que sabe como a huerto emparedado en masa seca."

"El ambiente se siente un tanto tenso, sin que ninguno de los dos sepa muy bien qué decirle al otro ahora que se han agotado nuestros temas de charla."

"Eventualmente ambos nos acabamos nuestra comida, sin mantener ninguna conversación por un tiempo. Eventualmente, sin embargo, la dulce voz de Lilly rompe el silencio."

show lilly basic_reminisce_close
with charachange

li "Pasaron muchas cosas por allá… ¿no es así?"

hi "Mm."

"Una vez más, silencio. Aunque con ambas mentes pensando en el mismo tema, creo que ya he puesto en orden mis sentimientos al respecto."

hi "Sé que todo sucedió a las apuradas, pero… No me arrepiento de nada de lo que pasó en Hokkaido. De absolutamente nada."

show lilly basic_oops_close
with charachange

li "¿Hisao…?"

"Un poco tenso, sostengo sus manos entre las mías; en parte para sentirla, en parte para calmar mis propios nervios."

hi "No me retracto de lo que dije entonces, Lilly. Te amo, y no te dejaré. Solamente deseo que pienses lo mismo."

show lilly basic_weaksmile_close
with charachange

"Ella reflexiona en silencio por un largo rato, el cual parece una eternidad."

show lilly invis_close at center
with dissolvecharamove

"Su ensimismamiento acaba cuando saca una mano de entre las mías, colocándola después sobre mis manos mientras inclina su cuerpo hacia adelante y se para de su silla."

"Después de dudarlo un momento, su rostro un tanto pensativo, sus labios se juntan con los míos por un breve momento."

show lilly behind_cheerful_close:
    ypos 1.1
with dissolvecharamove

"Mi mente se siente como si se hubiera detenido durante ese momento, apenas registrando a Lilly sentándose en su silla y sonriéndome de vuelta con las mejillas un poco ruborizadas."

show lilly basic_smileclosed_close
with charachange

li "Oír eso me hace muy feliz, Hisao. Me encantaría permanecer junto a ti."

hi "Quizás sea bueno tomarnos las cosas más lentamente, comparado a antes. Todavía tenemos clases, después de todo, y nuestros exámenes."

show lilly basic_giggle_close
with charachange

"Ella se ríe pícaramente, lo cual resulta ser contagioso."

show lilly basic_smileclosed_close
with charachange

li "Esa podría ser una buena idea sin lugar a dudas."

show lilly basic_smile_close
with charachange

li "¿Crees que te irá bien en los exámenes? Solamente queda un día para que comiencen, como dices."

hi "Probablemente debería haber estudiado más, pero creo que tengo una cabeza lo bastante buena para arreglármelas."

hi "Dicho eso, tuve que sacarme de encima a Misha y a Shizune. ¿Tu grupo está tan preocupado por los exámenes como el mío?"

show lilly basic_weaksmile_close
with charachange

"Ella suspira exasperada, confirmándolo. Estoy agradecido de que el ambiente se haya vuelto un poco más ligero."

li "Eso creo. Ya me han pedido ayuda dos de mis compañeros, y no hay duda de que habrá más."

hi "Podrías pensar en ello como tu primer entrenamiento para ser maestra, ¿quizás?"

show lilly basic_smile_close
with charachange

li "Probablemente sea una buena forma de verlo."

show lilly basic_smileclosed_close
with charachange

li "Respecto a eso, ¿cómo te está yendo con tus estudios de inglés? Recuerdo que está lejos de ser tu materia más fuerte, y las pocas oraciones que te memorizaste para hablar con mi madre difícilmente ayudarán."

"Maldición, ha dado en el clavo."

hi "Me atrapaste. Si no te molesta, ¿serías capaz de quizás ayudarme con eso? ¿Por favor?"

show lilly basic_planned_close
with charachange

li "Estaría encantada de ayudarte, Hisao. Pero a cambio…"

"Ella baja sus cejas hacia mí, su naturaleza coqueta descubriéndose vacilantemente."

hi "No hay problema. Pero probablemente te sea más útil algo de ayuda en los estudios."

show lilly behind_cheerful_close
with charachange

"Ella me lanza una sonrisa, una de victoria femenina que casi me hace sonrojar. Tengo la sensación de que ella sabe cómo usar su rostro para alterar mi juicio, así que probablemente debería estar más en guardia."

"Pero aquí y ahora, un grupo de estudio parece una forma conveniente de que ambos reforcemos nuestras habilidades más débiles."

play sound sfx_warningbell

"Suena la campana de la escuela, recordándonos que el tiempo no va a detenerse."

hi "Eh, ya se acabó la hora del almuerzo. De verdad es fácil perder la noción del tiempo aquí."

show lilly basic_weaksmile_close
with charachange

li "Este salón está apartado de los otros clubes y actividades, así que no nos llega mucho sonido. Probablemente ese sea el motivo principal."

show lilly basic_weaksmile_close at center
with charamove

"Un lugar apartado de todos los demás, sola con una única persona a quien ella ama. Cuando Lilly se levanta y recoge su mochila y su bastón, mis pensamientos vuelven al tiempo que pasamos en Hokkaido."

show lilly basic_satisfied_close
with charachange

li "Ah, antes de irme; Akira y yo tendremos una fiesta de bienvenida en mi habitación mañana. ¿Podrás venir?"

"… Y regresan."

hi "Mi agenda está libre, así que debería ser capaz de acomodar suficiente lugar en mi tiempo de estudio para poder ir."

show lilly basic_smileclosed_close
with charachange

li "Es bueno oír eso, Hisao."

hi "Por lo que vale, me alegra que hayas vuelto de Escocia. Una vez que acaben los exámenes, deberíamos tener más tiempo para nosotros."

show lilly basic_smile_close
with charachange

li "Mm. Las vacaciones comienzan poco después, también."

hi "Entonces podemos comenzar las vacaciones con Tanabata, tal como lo prometimos en el festival escolar."

show lilly basic_arablush_close
with charachange

"Ella lleva su mano a su mejilla y se ríe con un poco de nerviosismo, recordando el evento mientras me agradezco en silencio por haberlo recordado."

"Parece extraño verla reaccionar de tal forma, aunque no es como si nunca la hubiera visto avergonzada antes."

show lilly basic_weaksmile_close
with charachange

li "Yo… debería marcharme. Hasta luego, Hisao."

hi "Adiós."

hide lilly
with charaexit

stop music fadeout 6.0

"Ya sea por hábito o por un deseo obstinado de tener un pequeño fragmento de normalidad, levanto la mano en señal de despedida tal como siempre lo hago. Por lo menos ahora estoy consciente de que lo estoy haciendo."

"Creo que estoy comenzando a tener una visión más amplia de la que jamás he tenido antes, no solo con respecto a Lilly sino también con lo que me depara la vida."

"Las cadenas de mi pasado al fin se están rompiendo."

scene black
with dissolve




label es_L22:

$ renpy.music.set_volume(0.8, 0.0, channel="music")
play music music_ease fadein 4.0

scene bg school_girlsdormhall
with locationchange

"Caminando por el pasillo ahora un tanto más familiar de los dormitorios de las chicas, puedo oír un leve sonido de risas más adelante."

show bg school_girlsdormhall at bgleft
with charamove

"No me toma mucho identificar que el origen es la habitación de Lilly, aunque el grave timbre de la voz femenina sin lugar a dudas no es de ella, sino de su hermana."

play sound sfx_doorknock2

"Golpeo con mis nudillos la puerta con los tres toques de siempre, mi mano apenas habiéndose retirado cuando la puerta se abre de golpe."

show akira invis:
    xanchor 0.5 xpos 1.0
with None

show akira basic_smile:
    xpos 0.9
with dissolvecharamove

aki "Hola, Hisao."

hi "Hola. Hola Lilly, Hanako."

scene ev lilly_bedroom:
    truecenter
    zoom 1.0 subpixel True
    acdc_warp 8.0 zoom 1.03
with locationchange

"Hanako alza la mirada tímidamente, sus manos sepultadas bajo su desmedidamente grande camisón rosa. A su lado, Lilly se da vuelta en dirección a mi voz y sonríe."

"Sería una mentira flagrante decir que me desagrada el verla en esa ropa de dormir."

"Noto que Akira me está mirando de reojo con una sonrisa cómplice, la cual respondo con una mirada aguda."

scene bg school_dormlilly at bgleft
with locationchange

"Ella entiende la indirecta, se encoge de hombros y vuelve a la mesa baja en el centro de la habitación. Cuando me uno a ella, Lilly asiente en señal de saludo y comienza a servirme una taza de té."

show hanagown distant:
    twoleft
    ypos 1.14
show akira basic_smile:
    tworight
    ypos 1.14
with charaenter

hi "Es bueno verte otra vez, Hanako. Últimamente has estado más activa."

"Lilly pone cara de concentración mientras el líquido marrón claro, medido cuidadosamente por sus dedos como siempre, fluye de la tetera a la taza."

li "Parece que Hanako ha comenzado a ayudar a alguien de tu grupo con el club de periodismo. ¿Naomi, creo?"

show hanagown normal
with charachange

"Hanako asiente afirmativamente."

"Aun después de haber pasado dos meses con el grupo, todavía tengo problemas recordando los nombres de aquellos estudiantes con los que rara vez hablo."

"Me toma algunos esfuerzos mentales conectar el nombre con un rostro, pero eventualmente recuerdo a la chica que se sienta junto a Hanako al fondo del salón."

"Naomi Inoue. Una chica de aspecto común, excepto por su cabello rubio decolorado."

"Dada su personalidad directa y animada, Naomi puede haber visto una oportunidad de raptar a Hanako para su club cuando ella preguntó sobre unirse a uno."

"De cualquier forma, es bueno ver a Hanako expandiendo sus horizontes. Cuando la conocí, la idea de ella uniéndose a un club con quien fuera salvo Lilly hubiera parecido totalmente ridícula."

hi "Eso explicaría lo ocupada que has estado. ¿Lo estás disfrutando?"

show hanagown smile
with charachange

ha "Mm. Es… de verdad interesante."

"Como siempre, Hanako está lejos de ser locuaz. Algunas cosas nunca cambian, y parece que la personalidad de Hanako es una de ellas; posiblemente siempre sea de las que evitan ser demasiado sociales."

show hanagown smile:
    center
    ypos 1.14
show akira basic_smile:
    right
    ypos 1.14
show bg school_dormlilly at center
with charamove

show lilly invis at left
with None

show lilly basic_smileclosed_paj:
    ypos 1.17
with dissolvecharamove

"Advertido por el sonido de la vajilla contra la mesa cuando Lilly suavemente deja mi bebida frente a mí, le agradezco y doy un largo sorbo."

"Hanako y Lilly están poniendo atención a las de ellas, y Akira se está tragando una taza de café negro de fuerte olor."

show akira basic_laugh
with charachange

aki "Eres un bastardo con suerte, Hisao."

hi "¿Eh?"

"No puedo evitar hacer una mueca ante su sonrisa provocativa, aún visible en los bordes de la taza que cubre sus labios."

show akira basic_ending
with charachange

aki "Ver a mi hermana en su ropa de dormir, hay muchos hombres por ahí a los que les gustaría estar en tu lugar."

"He visto mucho más que eso de ella, no que lo fuera a admitir."

show lilly basic_emb_paj
with charachange

li "¡Akira!"

show akira basic_smile
with charachange

aki "Oye, solo estoy bromeando."

"Ella se inclina hacia mí tanto como puede, susurrando a mi oído con una sonrisa astuta en su rostro."

show akira basic_kill
with charachange

aki "Y Hanako también. Pervertido."

hi "Oye, fue su idea."

show hanagown distant_blush
with charachange

ha "Um, yo… uh…"

"Ambos la miramos, su rostro mirando hacia el suelo y sus manos jugueteando en el regazo de su camisón."

show hanagown smile
with charachange

ha "Si… es Hisao… no me molesta…"

"Ah, esto podría ser malo. Sé que Hanako es por completo demasiado inocente como para ver más allá en tal cosa, pero la expresión que Akira me dirige es positivamente tempestuosa."

show lilly basic_concerned_paj
show hanagown normal
with charachange

li "Um… Akira… por favor…"

"Parece ser que Lilly puede sentir el cambio repentino en el aura de Akira igual que yo, a pesar de no poderlo ver por sí misma."

show akira basic_boo
with charachange

"Akira lentamente aparta la mirada, como un perro guardián amarrado por su dueño en el momento justo. Respiro soltando un suspiro de alivio."

"No puedo pensar en un momento mejor para intentar cambiar el tema que ahora."

hi "Si no te importa que pregunte, Akira, ¿en qué trabajas? Nunca te he visto sin ese traje."

show akira basic_laugh
with charachange

aki "Pensando en qué hacer con tu vida después de que acabe la escuela, ¿eh?"

show akira basic_smile
with charachange

aki "Soy abogada. La mayor parte del tiempo trabajo en el departamento legal de la sucursal japonesa de la compañía familiar."

aki "La respuesta más aburrida posible, supongo. El derecho es un tema bastante árido para la mayoría."

hi "Algo así."

show akira basic_lost
with charachange

aki "Oye, no se supone que me des la razón."

show lilly basic_giggle_paj
show hanagown normal
show akira basic_smile
with charachange

"Lilly se ríe animada mientras sostiene su taza de té y platillo, y Hanako rápidamente se le une."

"Este ambiente amistoso entre todos es algo que extrañé mientras Lilly y Akira estaban de viaje. Si bien el asunto que tuve con Hanako no ayudó, creo que el solo no tener a Lilly por aquí cambió los ánimos."

show lilly basic_smileclosed_paj
with charachange

li "Es bueno estar de vuelta. Te extrañé, Hisao, y a ti también, Hanako."

hi "Lo mismo va por nuestra parte. Me imagino que tus compañeros estaban felices de verte."

show lilly basic_ara_paj
with charachange

li "Por así decirlo, sí."

show akira basic_laugh
with charachange

"El resoplido de Akira demuestra que está bien consciente de la actitud de Lilly hacia tales figuras retóricas. Me imagino que tiene que estarlo, dado el tiempo que han estado juntas."

show hanagown normal
with charachange

ha "¿Se divirtieron en Escocia?"

$ renpy.music.set_volume(0.1, 2.0, channel="music")

"Por un momento me pregunto por qué menciona eso, pues hace un tiempo ya que regresaron, pero entonces recuerdo todo lo que ha pasado."

"Simplemente no hemos tenido tiempo de reflexionar, con todo lo de los exámenes y nuestro viaje a Hokkaido."

show lilly basic_reminisce_paj
show akira basic_annoyed
with charachange

"El rostro de Lilly se vuelve distante un momento, y el hecho de que la primera reacción de Akira sea mirar a su hermana no se me escapa. Sin embargo, ella rápidamente se recupera."

$ renpy.music.set_volume(0.8, 0.4, channel="music")

show akira basic_smile
show lilly basic_weaksmile_paj
with charachange

li "Fue… agradable. Yo… nosotras… no habíamos visto a nuestra familia hace mucho tiempo, así que fue una reunión maravillosa."

show akira basic_boo
with charachange

aki "Sí, supongo que es cierto. Pero el que su casa haya estado a la orilla de la playa fue lo mejor."

"Por su tono despectivo, tengo la sensación de que a Akira no le agrada su familia tanto como a Lilly."

show lilly basic_giggle_paj
with charachange

li "Solo te gustó porque por fin tuviste tiempo para jugar."

show akira basic_ending
with charachange

aki "Solo porque soy mejor nadadora…"

show lilly basic_smileclosed_paj
with charachange

li "Yo no tengo el lado atlético de la familia, eso es todo."

show akira basic_laugh
with charachange

aki "Bueno, puedes contentarte con el hecho de que tienes los genes de la altura al menos."

show akira basic_boo
with charachange

aki "Y los genes del busto…"

show lilly basic_weaksmile_paj
with charachange

li "Eso no es realmente algo que se pueda decir a la gente…"

"Aunque Lilly pretende regañar a Akira, lo hace con una sonrisa inconfundible y un tanto descarada en su rostro."

show hanagown distant_blush
with charachange

"Dudo que a Akira le moleste, a juzgar por su expresión indiferente. Y aunque a mí tampoco, Hanako está mirando hacia abajo a mi lado completamente ruborizada."

"Dejando de lado las humoradas de las hermanas, sus padres de verdad llevan una vida burguesa."

"Parece completamente separada de la vida que Lilly y Akira han vivido hasta ahora. Supongo que el pragmatismo debe haber hecho que tomaran la decisión por ellas."

"Pero venir de un linaje tan pudiente y bien conectado no hace más que sumar al aire casi noble que Lilly parece tener. Es casi sorpresivo que nada de ello se haya pasado a Akira."

"De verdad parecieran no ser hermanas. Su única similitud pareciera ser su confianza compartida, la cual puede ser atrayente y un dolor de cabeza en ocasiones."

stop music fadeout 2.0

scene bg school_dormlilly
show lilly basic_smileclosed_paj:
    twoleft
    ypos 1.17
show akira basic_smile:
    tworight
    ypos 1.14
with shorttimeskip

"La mayor parte de la noche sigue tal cual, con Hanako eventualmente dejándonos a las hermanas Satou y a mí para dirigirse a su habitación a descansar."

"Por un rato, solamente el apenas audible sonido del platillo y la taza de Lilly se puede oír de tanto en tanto a medida que ella bebe lentamente. El silencio se tensa mientras Lilly y yo esperamos que se toque el asunto más obvio."

show akira basic_boo
with charachange

aki "Entonces…"

$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_dreamy fadein 4.0

show lilly basic_weaksmile_paj
with charachange

"Lilly baja su taza obedientemente, dándole a su hermana toda su atención."

"Con Lilly y yo a un lado de la mesa central y Akira en el otro, esto casi se siente como un juez dando un veredicto."

show akira basic_smile
with charachange

aki "¿He oído que ahora ustedes dos están saliendo?"

"Miro de reojo a un costado a Lilly para confirmar que ella es la fuente del conocimiento de Akira. Ella asiente ligeramente a Akira, lo cual remedo afirmando."

"Decidiendo que este es el momento y lugar apropiado para hacerlo, y que Akira es lo más cercano que ha tenido Lilly a una figura paterna por la mayor parte de su vida, me inclino poniendo mis manos en el suelo y mi cabeza casi lo mismo."

hi "Cuidaré bien de tu hermana, Akira. Te lo prometo."

show lilly basic_smile_paj
with charachange

li "¿Ves? Es un caballerito adorable."

"Debe haber sentido mi voz viniendo desde una posición más baja que lo usual."

"Lentamente me levanto, mirando vacilantemente a Akira por debajo de mis cejas."

"A decir verdad, dudo mucho que mi juez vestido de traje ponga objeción alguna. Ella definitivamente es de las que dejan en claro su desaprobación hacia otros, algo que le da una medida de respeto ante mis ojos."

show akira basic_laugh
with charachange

aki "Chapado a la antigua, ¿eh? Bueno, es del tipo de persona que suponía que te gustaría."

show akira basic_smile
with charachange

aki "No tengo problema con ello, y les deseo a ustedes dos lo mejor. Aun si no me gustara, en realidad no es mucho lo que puedo hacer de todas formas."

"Le ofrezco un gesto de aprecio mientras que Lilly suelta un suspiro de alivio, posiblemente más por deber que por haber creído que Akira pudiera haber tenido problemas con que estuviéramos juntos."

show akira basic_evil
with charachange

aki "Pero me pregunto… ¿Cómo lo está tomando el resto de la familia, particularmente la parte que vive en Yamaku? ¿Le han dicho?"

show lilly basic_listen_paj
with charachange

"Las sonrisas se vuelven muecas mientras que Akira sonríe de forma abiertamente malévola. Quienes están más cerca de ti saben mejor cómo hundir el cuchillo, después de todo."

show lilly basic_weaksmile_paj
with charachange

li "“Soportándolo” puede ser la mejor forma de llamar a la situación. ¿Estás de acuerdo, Hisao?"

hi "Sí, eso lo describe bien. Al menos está siendo razonable al respecto."

show akira basic_boo
with charachange

aki "Qué bueno escucharlo. Esa chica puede ser intratable en los momentos más inoportunos."

show akira basic_smile
with charachange

aki "Nos enviamos unos cuantos mensajes un poco después del viaje, y ya me lo estaba poniendo difícil por ver a mi novio cuando regresamos, después de dejar a Hideaki solo por tanto tiempo. A ella de verdad le preocupa el pequeño."

"Recuerdo la extraña reacción de Shizune luego de decirle sobre nuestra relación, pero decido no sacar el tema. Sin lugar a dudas es simplemente por su antipatía mutua, y los comentarios de Akira no hacen más que apoyar eso."

show akira basic_boo
with charachange

aki "Bien entonces, ya está zanjado. Debo ir a trabajar temprano mañana, así que es mejor que me marche."

show akira basic_smile at tworight
with charamove

"Ella se levanta de la mesa con un gruñido, su mano sobre su rodilla para impulsarse hacia arriba. Recién noto los ojos de Akira que permanecen en Lilly por un par de segundos antes de apartarse, mientras ella comienza a salir."

hide akira
with charaexit

"Después de salir por la puerta, se detiene y mira hacia arriba pensativa antes de darse la vuelta hacia nosotros una última vez."

show akira invis:
    xanchor 0.5 xpos 1.0
with None

show akira basic_lost:
    xpos 0.9
with dissolvecharamove

aki "Oh cierto, casi se me olvidó decirles."

show akira basic_ending
with charachange

aki "Usen protección. Cada vez."

"Me atraganto violentamente con el té en mi boca. A diferencia de mí, la compostura de Lilly se mantiene perfectamente estable, ya que parece no haberse inmutado. Estoy algo impresionado."

show lilly basic_smile_paj
with charachange

li "Lo hacemos, no te preocupes."

show akira basic_smile
with charachange

aki "Bien hecho chica. Nos vemos."

show akira invis:
    xanchor 0.5 xpos 1.0
with dissolvecharamove

hide akira
with None

"Y sin más se da la vuelta y sale a trancadas por la puerta, con su mano en alto a medida que desaparece por el oscurecido pasillo, cerrando la puerta tras ella."

show lilly basic_smile_paj:
    center
    ypos 1.17
show bg school_dormlilly at bgright
with charamove

"La mayor reacción que logro tener es caer hacia adelante sobre la mesa, completamente falto de energía y realmente exhausto por su culpa. La habilidad de Lilly de mantenerse calma ante ese demonio vestido de traje es algo que admiro."

hi "Ella en realidad es increíblemente directa. No creo que sea capaz alguna vez de seguirle el ritmo a la energía de tu hermana."

show lilly basic_smileclosed_paj_close:
    center
    ypos 1.1
with characlose

"Cuando siento la suave mano de Lilly posarse sobre la mía, giro mi cabeza a un lado para ver su gentil sonrisa. Por un largo rato, simplemente estamos sentados uno junto al otro en silencio."

"Dada su altura indudablemente inusual, ella es prácticamente del mismo porte que yo; probablemente unos cuantos centímetros más alta quizás. De esta forma, ella parece todavía más alta."

"La sensación de su blanda y suave mano contra la mía es agradable, al igual que el ver la delgada ropa de dormir de seda que está usando, mostrando sus curvas y su escote."

show lilly basic_smile_paj_close
with charachange

li "Pero ustedes dos se llevan bien, aunque digas eso."

hi "Supongo. Sabes, ustedes dos se parecen más de lo que pensé cuando las conocí."

show lilly basic_cheerful_paj_close
with charachange

li "Entonces es bueno que te haya detenido de ir tras ella, ¿no es así?"

"Aunque ella bromee al respecto, mi estimación de mi incapacidad de seguirle el ritmo a Akira, ya sea física o mentalmente, fue completamente en serio."

"La naturaleza lenta y femenina, casi maternal, de Lilly es quizás lo que más me ayudó durante mis primeras semanas en Yamaku."

"Ahora que lo pienso…"

hi "Espera… ¿desde cuándo usamos protección?"

show lilly basic_pout_paj_close
with charachange

"Cuando miro con curiosidad a mi lado, las mejillas de Lilly se inflan al regañarme."

li "A diferencia de ti, yo me acordé. El paquete está en la despensa junto al fregadero."

"Entonces, no soy el único que toma pastillas. En retrospectiva, me siento algo desconsiderado por no recordarlo en absoluto y dejárselo a Lilly."

"Mirando la despensa que ella mencionó, noto una vez más las pilas de libros que llegan hasta la rodilla a nuestro alrededor, que han estado aquí las otras veces que he visitado."

"La mayor parte están alineados contra la pared para dar un poco más de espacio alrededor de la mesa."

hi "¿Por qué no consigues un librero para tus libros? Es extraño ver libros simplemente apilados por ahí, especialmente dado que tu cuarto se vería tan limpio y ordenado de otra forma."

show lilly basic_smileclosed_paj_close
with charachange

li "Son más fáciles de encontrar de esta manera; sé exactamente en cuál pila está cada libro."

hi "¿No lo sabrías luego de dejar cada juego en una repisa distinta?"

show lilly basic_weaksmile_paj_close
with charachange

li "Podrá ser cierto, pero…"

"Así que no es inmune a ataques de pereza después de todo."

hi "Tienes tantos que es una pena que no podamos compartir nuestros libros a pesar de que ambos leemos tanto."

show lilly basic_giggle_paj_close
with charachange

"Ella se ríe por un instante."

hi "Ahora que lo pienso, ¿por qué pides tus libros por medio de Yuuko? Me imagino que debe haber muchos sitios por los que puedas ordenar libros en braille, especialmente braille en inglés. Hay un montón de programas de texto a habla también."

show lilly basic_displeased_paj_close
with charachange

"Ella aparta su cabeza de mí un poco, lo que me parece un tanto sorprendente."

li "Es solo… que no soy tan buena con las computadoras. No tengo problemas con las máquinas de escribir y de braille… pero eso sería todo."

"Su tono casi me hace soltar una carcajada. Ella es una persona orgullosa, así que admitir algo como eso debe ser difícil."

"Entonces, Lilly es de las que les cuesta la tecnología. Dada su personalidad anticuada, eso no es realmente una sorpresa."

hi "Yo no me preocuparía por eso. Hay muchas personas que en realidad no son tan buenas con ellas, así que no es tan inusual."

show lilly basic_concerned_paj_close
with charachange

li "“Tan” inusual…"

"Ahora ella parece más deprimida. Se siente como si yo estuviera hundiendo el cuchillo, en lugar de tratar la herida."

show lilly basic_weaksmile_paj_close
with charachange

"Con un poco de esfuerzo me muevo hacia ella, colocando vacilantemente una mano alrededor de su cadera para abrazarla. Aún no estoy del todo acostumbrado a este tipo de cariño físico, pero a Lilly parece agradarle."

scene ev lilly_kissing
with whiteout

"Lilly sonríe y se da vuelta hacia mí, dándome un beso como recompensa por ceder ante ella. Me atrae, rozando mi labio superior con los suyos antes de presionar contra ambos."

"De esta forma, cada uno de mis sentidos está lleno de ella."

"El apenas perceptible aroma de su cabello, su sabor a medida que su lengua fugazmente toca la mía, la suavidad de sus labios, su imagen acaparando mi mente, el silencio total además de su leve aliento…"

"Nos habremos besado antes, pero aun si esto es más un beso de afecto que otra cosa, sigue siendo una sensación nueva y placentera."

scene bg school_dormlilly at bgright
show lilly basic_cheerfulblush_paj_close:
    center
    ypos 1.1
with locationchange

"A juzgar por lo nítido de su rubor cuando se retira, es obvio que ella siente lo mismo que yo; aun si estamos completamente solos, se sigue sintiendo un poco vergonzoso sincerarnos tanto."

show lilly basic_smileclosed_paj_close
with charachange

li "Si nos tomamos las cosas día a día, creo que sería mejor. Pasos pequeños, ¿cierto?"

hi "Sí. Solo pasos pequeños."

"Tenemos bastante tiempo para estar juntos, aun después de que el año escolar acabe. Mientras nos mudemos juntos, creo que todo saldrá bien; ninguno de los dos se va a ningún lugar pronto, después de todo."

"Por ahora, simplemente estoy agradecido por este pequeño fragmento de tiempo que podemos pasar juntos."

stop music fadeout 2.0

scene black
with dissolve




label es_L23:

scene bg school_nursehall
with locationchange

"Permanezco quieto frente a la puerta que da a la oficina del enfermero por lo que parece al menos una docena de minutos o algo así."

"No es como si nunca hubiera entrado al pequeño cuarto beige antes, ni es por alguna sensación infantil de ansiedad por la visita."

"Quizás sea porque la oficina del enfermero es similar a un confesionario, una admisión de que mi cuerpo tiene defectos. El saber que tal hecho es completamente confidencial entre el enfermero y yo apenas atenúa esa sensación."

"Recordando que la campana que señala el final de la hora del almuerzo sonará pronto, suelto un suspiro y abro la puerta. El peso permanecerá sobre mí solamente este rato más."

play music music_nurse fadein 0.5

scene bg school_nurseoffice
show nurse neutral at center
with locationchange

nk "Vaya, si no es otro que Nakai. Qué bueno verte."

show nurse grin
with charachange

nk "O malo, supongo, considerando que soy enfermero."

"Él suelta una risita, divertido por su pequeño chiste. Encuentro su humor insuficiente y un tanto raro, pero el hecho de que pueda tomarse a la ligera tal situación es quizás reconfortante, o al menos distrayente."

show nurse neutral
with charachange

"Una vez terminado su breve episodio de entretenimiento, junta sus manos y va directo al grano. Tomo asiento al señalarme él que lo haga."

"Desearía que los salones de clases tuvieran asientos así de cómodos."

"Puedo sentir que mi mente comienza a vagar a medida que mis ojos observan rápidamente el cuarto, distraídos por todos los pequeños cambios que ha habido desde la última vez que vine."

show nurse fabulous
with charachange

nk "De acuerdo, ¿qué te trae por aquí? No te he visto a menudo, ¿entonces puedo asumir que tu salud ha estado bien hasta ahora?"

hi "Bueno, en general."

show nurse neutral
with charachange

nk "Ya veo."

"A medida que hablo su sonrisa comienza a desaparecer."

"Me siento algo culpable al respecto. Son esos momentos donde no puedo llamarme a mí mismo “normal” de forma racional los que me ponen tan reacio a ver al enfermero. Son una admisión de que soy diferente a los demás."

stop music fadeout 5.0

hi "Cuando estaba de viaje durante el fin de semana largo, tuve unos cuantos problemas con mi corazón."

"Él murmura de forma muy seria y asiente al mismo tiempo, instándome para que continúe."

hi "Creo que fue… sí, fue mientras caminaba un trecho bastante largo. Creo que el término correcto sería una fibrilación auricular."

hi "De repente caí de rodillas y me sentí casi como si estuviera teniendo un pequeño ataque cardiaco, pero pasó en algo así como medio minuto. Aunque aun después, me sentí bastante fatigado y con náuseas."

show nurse concern
with charachange

nk "Hrm. No está bien. No está para nada bien."

nk "¿Eso fue hace cuántos días, exactamente? ¿Hiciste algo inusual, además de exigirte físicamente, antes del hecho? ¿Estabas tomando tus medicamentos adecuadamente?"

"El enfermero pasa de modo mal bromista a profesional de la salud serio, soltando preguntas, tomando notas, y abriendo cosas en su computadora."

"Le cuento el hecho de que me había olvidado de tomar mis píldoras esa mañana, y la tarde anterior. Fue algo estúpido, pero no puedo cambiar nada al respecto ahora, excepto responder con sinceridad y aguantarme."

"Su seriedad se transforma en fruncir el ceño, y la charla se transforma en un examen instantáneo."

hide nurse
with shorttimeskip

"Termino de abotonarme la camisa y una vez más me invita a sentarme frente a él."

show nurse concern at center
with charaenter

nk "¿Este es el primer problema cardiaco que has tenido desde que llegaste a Yamaku?"

hi "He tenido dolores en el pecho antes, solamente un par de veces, pero eran más una incomodidad que algo como esto."

"Él se reclina en su silla, pareciéndose por un momento a un Poirot de bata blanca mientras medita el misterioso caso del fibrilación auricular."

"Moviendo sus labios de lado a lado para demostrar que está pensando, su bigote inexistente se menea, y eventualmente llega a una conclusión."

show nurse fabulous
with charachange

play music music_nurse fadein 1.0

nk "Bueno, lo sobreviviste. Eso siempre es positivo."

"Pestañeo al oír esto, y luego noto que el enfermero tiene su cara de “te atrapé”."

"En realidad es algo tranquilizador. No creo que él fuese capaz de bromear si las cosas fueran de verdad serias, así que guardo silencio y acepto mi regaño."

show nurse neutral
with charachange

nk "Hablaré con tu doctor, pero en este caso sospecho que se trata simplemente de agotamiento físico."

nk "¿Te has mantenido haciendo ejercicios ligeros como te indiqué?"

hi "Me aseguro de caminar una cantidad razonable todos los días. Usualmente es suficiente para comenzar a sudar, pero por otro lado de verdad no estoy tan en forma como antes."

nk "Entonces eso debería ser suficiente. Lo importante a tener en cuenta es hacer ejercicios de bajo impacto, no carreras cortas de ejercicio intenso como correr y eso."

hi "Entiendo. Desde que salí del hospital he estado mucho más enfocado en mis estudios, en parte para distraerme del hecho de no ser capaz de hacer más actividades físicas."

show nurse grin
with charachange

nk "Es bueno oír que estás lidiando bien con todo. Los cambios de estilo de vida tan repentinos pueden ser difíciles en el mejor de los casos, así que me alegra oír que parece que ya lo tienes todo en orden. Casi todo, mejor dicho."

show nurse neutral
with charachange

nk "Sin embargo, quiero vigilarte de cerca por un tiempo, solamente como observación. Solo para asegurarme de que las cosas no estén poniéndose mal, entiendes."

"Eso es algo que de verdad no quería oír. Desde que llegué a Yamaku, lo único que he querido hacer es vivir tan normalmente como sea posible."

"“Observación” era una de esas palabras que llegué a odiar más que las otras cuando estaba en el hospital."

"Durante todo ese tiempo sentí que podría haber simplemente salido por las puertas del hospital, si no fuera por esa “observación” que los médicos tanto querían."

hi "Claro. ¿Debería venir más a menudo?"

"Él revisa el calendario junto a su computadora, lo cual parece enfermarlo con un serio caso de entrecejo fruncido. Luego de eso se da vuelta hacia mí."

show nurse concern
with charachange

nk "Las vacaciones de verano son un tanto molestas, considerando los tiempos…"

nk "Corroboraré con tu doctor para intentar tener una mejor idea de la situación y ver cómo quiere seguir, pero creo que de momento simplemente deberías tomarte las cosas con calma y con cuidado."

nk "Lo que describes no suena de primeras como algo recurrente, pero no estaría mal relajarte por un tiempo, solo para estar seguro."

hi "¿Qué debería hacer hoy?"

"Él mira por encima de mi hombro hacia el reloj que cuelga sobre la puerta. Nunca lo hubiera notado si no hubiera seguido su mirada."

show nurse fabulous
with charachange

nk "Ya casi es hora de que acaben las clases, así que bien podrías simplemente salir temprano."

"Suelta un guiño disimulado, asegurándose de que yo entienda que me está haciendo un favor."

hi "Bien, órdenes del enfermero. Gracias."

show nurse grin
with charachange

nk "Para eso estoy aquí, después de todo."

show nurse neutral
with charachange

nk "Sé que puede que no quieras oír esto, pero no puedes ignorar tu condición. No dudes en verme si tienes algún otro problema, o si necesitas preguntar algo. Adiós."

hide nurse
with charaexit

"Él se da la vuelta y vuelve a teclear en la computadora frente a él. Supongo que leeré un rato antes de esperar a Lilly en el portón, considerando que no tengo mucho más que hacer."

stop music fadeout 3.0

"Aun mientras me marcho, sus palabras resuenan en mi mente. Mi condición no es algo tan limitante como muchos de los otros acá en Yamaku tienen, y no quiero ser una carga para Lilly pensando al respecto."

"Si simplemente vivo mi vida de forma normal y evito cualquier choque breve y agudo, debería estar bien. No dejaré que mi condición me domine."

scene bg school_gate_ss
show lilly cane_smileclosed_ss at center
with shorttimeskip

play music music_tranquil fadein 3.0

play sound sfx_normalbell

"Lilly se aparece en mi vista tan pronto como suenan las campanas anunciando el fin del día escolar. Ella se despide de un grupo de sus compañeros que se dirigen en dirección contraria, antes de comenzar su viaje semanal a la tienda de abarrotes."

hi "Buenas tardes, Lilly."

show lilly cane_smile_ss
with charachange

"La inmediata sonrisa cálida y porte relajado que asume al notar mi presencia son inesperadamente bienvenidos."

li "Hola, Hisao. Buenas tardes a ti también."

show lilly cane_smileclosed_close_ss
with characlose

"Ella duda un segundo, pero eventualmente se digna a inclinar su cabeza hacia adelante y cerrar sus ojos. Mis labios se juntan con los de ella con un ligero grado de inquietud antes de partir, tomados de la mano."

"El hecho de que no haya tanta diferencia de altura es un tanto útil a veces, al no haber necesidad de que ninguno de los dos incline la cabeza hacia arriba o hacia abajo para juntarla con la del otro."

scene bg school_road_ss
with locationchange

"No nos toma mucho tiempo dejar atrás el ruido de los otros estudiantes, siendo el único sonido audible el golpeteo del bastón de Lilly con su mano libre."

"Silencio, dichoso silencio, es todo lo que nos acompaña a medida que caminamos lentamente bajo la luz del sol poniente."

hi "Creo que está comenzando a gustarme de verdad este pueblo. El enorme campo verde lleno de colinas, árboles por todas partes, los pequeños edificios algo rústicos…"

show lilly cane_smile_close_ss at center
with charaenter

li "¿Así que también has llegado a apreciar la tranquilidad de esto?"

hi "Eso creo. Vengo de una ciudad metropolitana cerca de Tokyo, así que la serenidad de este pueblo de verdad se me hizo extraña cuando llegué por primera vez."

hi "Aunque después de un tiempo se volvió realmente agradable. Creo que ahora lo prefiero al barullo de mi ciudad natal."

show lilly cane_smileclosed_close_ss
with charachange

li "Y yo he preferido la tranquilidad de un pueblo tan rural aun cuando llegué por primera vez, supongo que tenía la ventaja de haber crecido en un área tranquila antes de venir."

show lilly cane_weaksmile_close_ss
with charachange

li "También Hanako dijo que los alrededores son muy bonitos."

"Lilly podrá decir tal cosa muy fácilmente, pero cada vez que menciona cómo describen otros lo que hay a su alrededor como hermoso o lindo, me siento un tanto descorazonado."

"Noto a su expresión volver a una de anticipación ante alguna pregunta. Ella siempre ha captado bien cuando alguien no está diciendo lo que está pensando, así que bien podría hablar."

hi "Me estaba preguntado… uh, cómo decirlo…"

hi "¿Alguna vez… has lamentado no poder ver cómo se ven las cosas por ti misma? Es simplemente algo que me he estado preguntando."

show lilly cane_listen_close_ss
with charachange

"Ella piensa cuidadosamente por un momento."

show lilly cane_smileclosed_close_ss
with charachange

li "¿Alguna vez te has lamentado el no poder oír a la gente susurrar al otro lado de una habitación?"

show lilly cane_smile_close_ss
with charachange

li "Solamente puedo hablar por mí misma, pero el hecho de que no pueda ver es la única cosa que he experimentado en mi vida. Tal como yo no puedo hacer algo que tú sí, tú no puedes hacer cosas de las que yo soy capaz."

show lilly cane_weaksmile_close_ss
with charachange

li "El hecho de que el mundo esté hecho para quienes tienen visión puede ser una molestia a veces, pero hay muchas, muchas personas que sufren mucho más que yo por la forma que tiene el mundo."

hi "Eso tiene sentido, pero de todas formas, es que se siente algo mal describirte algo que tú no puedes experimentar."

show lilly cane_surprised_close_ss
with charachange

"Ella ladea su cabeza, pensativa, como si acabara de decir algo que casi no tiene sentido en absoluto."

li "Pero yo puedo experimentarlo."

show lilly cane_smile_close_ss
with charachange

li "Acabas de decir que te gusta este lugar por cómo son los alrededores. Me gusta este lugar por el mismo motivo."

show lilly cane_smileclosed_close_ss
with charachange

li "Gracias al hecho de que este es un pequeño pueblo rústico rodeado de árboles, da un cierto grado de tranquilidad y serenidad lejos del barullo de la escuela y del ajetreo, sin mencionar los olores de la ciudad."

"Supongo que además tendría mucho parecido con la casa que compartió con Akira."

"Su perspectiva al respecto parece bastante razonable, y no me sorprende que tenga un manejo mucho mejor de su situación particular que yo de la mía."

"Tal como el que haya venido de un lugar algo similar a los alrededores de Yamaku hace que se haya acostumbrado en menos tiempo, el haber nacido ciega afectó su actitud, admite ella misma."

"Debería dejar de estar tan molesto conmigo mismo al respecto, pero no puedo quitarme la sensación de que he dependido demasiado de Lilly, dadas las circunstancias que la mayoría hemos tenido que afrontar en Yamaku."

hi "Eso tiene mucho sentido. Eres bastante buena explicando, como siempre."

hi "Ahora que lo pienso, ¿dónde está Hanako? Estuvo con nosotros durante el almuerzo."

show lilly cane_weaksmile_close_ss
with charachange

li "Parece que está ocupada estudiando. Los exámenes distan mucho de haber acabado, y dijo que quería mejorar su rendimiento con respecto al año pasado."

hi "Si bien admiro su ética de trabajo, de verdad está intentado darnos nuestro espacio últimamente."

show lilly cane_reminisce_close_ss
with charachange

li "Ella es de ese tipo de personas, creo; de los que coloca a las necesidades de los demás por sobre las propias siempre que puede. Es una chica dulce, a pesar de que tantas cosas la han lastimado en el pasado."

show lilly cane_weaksmile_close_ss
with charachange

li "No lo sé… Siento que es recién ahora, cuando ella está más lejos de mí que nunca, que ella está encontrándose realmente consigo misma."

show lilly cane_smile_close_ss
with charachange

li "Fue gracias a ti que ella comenzó a tener más confianza, después de todo, y no gracias a mí."

"Saco mi mano de la suya y suavemente la poso sobre su cabeza."

hi "Lo importante es que estuviste ahí para ella. Ni siquiera puedo imaginarme cómo habría sido sin haber encontrado a alguien como tú. Eso quedó en evidencia mientras estabas en Escocia."

hi "Todos seguimos siendo amigos, así que simplemente tenemos que tener fe en ella. Creo que se volverá una buena persona, y eso es gracias a que tú has estado ahí para ella cuando más lo necesitaba, tal como estuviste ahí para mí."

show lilly cane_weaksmile_close_ss
with charachange

li "Me hace sentir un poco infantil cuando hablas con tanta sabiduría."

hi "Bueno, lo intento."

hi "Por casualidad, ¿harás algo el fin de semana?"

show lilly cane_surprised_close_ss
with charachange

li "Nada que se me venga a la mente. ¿Por qué?"

hi "¿Entonces qué tal una cita el domingo? Sería algo aparte de prepararnos para los exámenes."

show lilly cane_smileclosed_close_ss
with charachange

"Contrarrestando mi corazón cada vez más acelerado, ella simplemente sonríe y asiente."

li "Eso sería encantador."

hi "¿Adónde te gustaría ir?"

show lilly cane_displeased_close_ss
with charachange

"Su rostro de pronto se vuelve uno de reprobación."

li "No puedes hacer eso, Hisao. Es hacer trampa."

hi "¿Hacer qué?"

li "Un caballero nunca le pregunta a una dama dónde tener una cita."

hi "Ah… oh."

show lilly cane_smile_close_ss
with charachange

"Su sonrisa regresa rápidamente, asegurándome que está lejos de hablar en serio."

show lilly cane_smileclosed_close_ss
with charachange

li "No te preocupes por eso. Pensaré en un lugar adonde podamos ir."

hi "Te lo dejo a ti, entonces. Pero prometo que yo decidiré la próxima cita."

stop music fadeout 4.0

"Habiendo hecho nuestro plan para el fin de semana, el resto de la caminata colina abajo continúa en silencio."

"La idea de que ello dure por cualquier cantidad de tiempo, sin embargo, es hecha añicos al ver una figura conocida esperándonos, con sus manos en alto."

show lilly cane_smileclosed_close_ss at twoleft
show bg school_road_ss at bgleft
with charamove

show akira basic_smile_ss at tworight
with charaenter

aki "¿Qué hay?"

scene bg suburb_konbiniint
with shorttimeskip

play music music_daily fadein 0.5

"Dependienta" "¡Gracias, por favor vuelvan pronto!"

scene bg suburb_konbiniext_ss
with locationchange

"El cambio de temperatura al salir de la tienda de abarrotes me hace estremecerme. Se siente como si el verano estuviera comenzando a acabarse."

show lilly cane_weaksmile_ss at center
with charaenter

"Mirando a mi lado, la misma sensación parece afectar también a Lilly, aunque a diferencia de mí ella no logra ocultar este hecho."

"Algo de lo que no me había dado cuenta al principio es lo delicada que es físicamente, aun comparada con personas como Hanako."

"Si tuviera que describirla, tendría que decir que me recuerda a una figura de porcelana."

show akira basic_ending_ss at center behind lilly
with charaenter

show lilly cane_surprised_ss
with vpunch

show lilly cane_reminisce_ss at twoleft
show akira basic_ending_ss at tworight
show bg suburb_konbiniext_ss at bgleft
with dissolvecharamove

"Akira camina atrás de ella y le da un par de palmazos fuertes en su hombro, para la consternación de Lilly. Por un momento ella parece envidiar mi estatus de hijo único tanto como yo envidio su relación tan cercana."

show lilly cane_listen_ss
show akira basic_boo_ss
with charachange

"Las dos hablan entre ellas por unos momentos mientras yo separo mis bolsas, sus voces demasiado bajas como para poder oírlas, pero eventualmente acaban su conversación y comenzamos a caminar de vuelta a la escuela."

scene bg school_road_ss
show akira basic_smile_ss at tworight
with locationskip

aki "Ah, se siente bien salir de esa maldita oficina. Ustedes niños no saben lo bien que lo tienen aquí."

show lilly cane_displeased_ss at twoleft
with charaenter

li "Niños…"

show akira basic_laugh_ss
with charachange

aki "Tsch. “Ustedes dos”, entonces. Los niños crecen tan rápido hoy en día."

show lilly cane_pout_ss
with charachange

li "No tienes la edad suficiente como para decir eso."

show akira basic_lost_ss
with charachange

aki "No lo sé. Estar todo el tiempo con Hideaki me hace sentir anciana; es tan precoz que me recuerda a ti cuando eras más joven."

show lilly cane_weaksmile_ss
with charachange

li "Es un buen chico. Sería una lástima si Shizune llegara a ser una influencia en él."

show akira basic_laugh_ss
with charachange

"Akira retiene una carcajada ante la antipatía de su hermana. De verdad no parece considerarlo algo como para armar un escándalo al respecto, tratándolo más como un espeto infantil."

show akira basic_smile_ss
with charachange

"Ella me mira, aparentemente recordando recién ahora que estoy aquí, y suelta una ligera sonrisa mientras alcanza su bolsillo posterior."

hi "¿Qué sucede?"

show akira basic_ending_ss
with charachange

aki "Dame un segundo, déjame sacarlo…"

"Luego de bastante esfuerzo, ella logra sacar su billetera de cuero negra de su bolsillo posterior, sacando rápidamente lo que parece ser un cuadrado de papel doblado."

"Con Lilly completamente ignorante de lo que está pasando, Akira desdobla el trozo de papel y me lo pasa."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

show stallphoto_insert:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"Una foto vieja de… lo que parece ser Lilly y Shizune más jóvenes trabajando en un puesto de fideos, junto a una chica en el fondo. Ella parece vagamente conocida, pero no puedo decir exactamente por qué."

show lilly cane_smile_ss
with None

$ renpy.music.set_volume(1.0, 1.0, channel="music")

show stallphoto_insert:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide stallphoto_insert
with None

li "¿Qué es eso, Akira?"

show akira basic_boo_ss
with charachange

aki "Creo que lo sabes."

show lilly cane_listen_ss
with charachange

"Lilly piensa esto por unos instantes antes de darse cuenta de su significado."

show lilly cane_surprised_ss
with charachange

li "Akira… de verdad no debías…"

show akira basic_smile_ss
with charachange

aki "Está bien, ¿no es así? Además, es como la única fotografía que tengo de ustedes dos desde que entraron a Yamaku en la que no están en una riña."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

show stallphoto_insert:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"Vuelvo a mirar la fotografía en mi mano."

"Realmente parece extraño ver a Lilly y a Shizune trabajando juntas tan diligentemente sin dar señas de animosidad. Si la foto es de ellas durante el festival de Yamaku, eso significa que debe haber sido tomada hace uno o dos años atrás."

"En otras palabras, cuando ellas aún estaban en el consejo estudiantil juntas."

hi "¿Quién es la chica del fondo? Me parece algo familiar."

aki "Ja, sabía que no la reconocerías. Es Misha antes de teñirse el cabello de rosa."

hi "¿Ella es Misha? No puede ser…"

"Se siente extremadamente extraño ver a Misha sin su peinado tan distintivo. A juzgar por el tono de Akira, a ella no le agrada mucho la idea de moda de Misha."

"Supongo que ese hecho solo acentúa lo extraña que parece la situación. Pensar que eran tan amigables en el pasado… Desearía poder hacer algo para arreglar su relación."

li "Estás muy callado, Hisao."

hi "Es que se siente algo extraño verlas a todas tan amigables de esta forma."

"Lilly se mueve para decir algo, pero se detiene a sí misma. Al final, esto no es un asunto que me incluya; es entre Shizune y Lilly, y nadie más."

li "Las cosas cambian. Desafortunadamente."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

stop music fadeout 6.0

show akira basic_resigned_ss
show lilly cane_reminisce_ss
with None

show stallphoto_insert:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide stallphoto_insert
with None

"Le devuelvo la fotografía a Akira, quien suspira mientras la dobla y la vuelve a meter en su billetera. Un pequeño recuerdo, ocultado discretamente, para ser sacado una vez más algo de tiempo después."

aki "Claro, sí que lo hacen."

"Inicialmente pienso que la reacción de Akira es simplemente en respuesta a la situación entre Lilly y Shizune, pero ella parece mucho más deprimida de lo que esperaría. También la expresión de Lilly se ha vuelto más difícil de leer."

hi "¿Pasa algo malo?"

show akira basic_boo_ss
with charachange

aki "Ah, es solo que me iré a Escocia dentro de poco."

hi "¿Te vas a Escocia otra vez?"

show akira basic_lost_ss
with charachange

"Por un largo rato, Akira parece sorprendida. Es una expresión que le asienta poco."

"Luego de lanzarle una mirada a Lilly, se da vuelta hacia mí como si nunca lo hubiera hecho."

show akira basic_resigned_ss
with charachange

aki "Sí. En un par de semanas me iré a Inverness para trabajar en la oficina central de la compañía. Es un salto bastante grande de posición corporativa, y no es una oportunidad que vaya a volver a aparecer."

"Así que Akira se va a ir de Japón, de forma aparentemente permanente…"

"No puedo evitar sentir que mi suposición de que todos podríamos pasar felizmente nuestros días, divirtiéndonos en este pequeño mundo aislado, está llegando a su fin. Es inquietante."

"Miro a Lilly, algo sorprendido de que ella no me haya contado tal cosa a pesar de ser usualmente tan directa."

"Ella sigue caminando con su cara fija hacia adelante. No puedo leer su expresión, ni puedo siquiera imaginar lo que pasa por su mente, lo que me incomoda dado lo fácil que usualmente es para mí hacer ambas cosas."

"Me recuerda a aquella vez que nos vimos en el Shanghái, justo antes de lo que se podría llamar nuestra primera cita. Aquella vez, todo lo que pude hacer fue animarla sin saber el motivo, y ahora no se siente distinto."

scene bg school_dormext_full_ni
show akira basic_resigned_ni at tworight
show lilly cane_reminisce_ni at twoleft
with shorttimeskip

"Cuando al fin volvemos a los dormitorios de la escuela una vez más, hay un silencio un tanto incómodo. No creo ser el único que lo siente."

hi "Nos vemos mañana entonces, Lilly. Adiós, Akira."

show lilly cane_weaksmile_ni
with charachange

li "Buenas noches, Hisao."

show akira basic_smile_ni
with charachange

aki "Nos vemos."

hide lilly
hide akira
with charaexit

"Y con eso, ellas se dirigen a los dormitorios para chicas."

"Al abrir la puerta a los dormitorios para chicos, me detengo y vuelvo la mirada hacia ellas momentos antes de que sus figuras desaparezcan tras la pesada puerta de madera."

"Fue… un momento extraño cuando Akira dijo que se marchaba. Si bien esa no fue la primera vez en que mis pensamientos en relación a mi nueva vida han sido puestos en duda, es quizás la primera vez que lo hacen de forma tan profunda."

"Todavía no sé qué pensar de la reacción de Akira, y mucho menos de la de Lilly."

"El frío de la noche me recuerda volver a mi habitación antes de pescar un resfriado, mis bolsas colgadas en mis brazos con un peso aparentemente redoblado."

"Por lo menos, tengo una cita con ella planeada para el fin de semana. Simplemente debo dejar de pensar demasiado en las cosas y aceptarlas como son."

"Los exámenes siguen en curso, después de todo, y como el fin del trimestre y el comienzo de las vacaciones de verano se acercan pronto, habrá suficiente para mantenerme ocupado por un tiempo."

"Mientras bostezo y me retiro adentro, mis pensamientos se vuelven a qué decidirá Lilly como el lugar de nuestra reunión de este fin de semana."

scene black
with dissolve



label es_L24:

scene bg city_restaurant at Fullpan(10.0)
with dissolve

play music music_jazz

"Estoy bastante seguro de que esto era lo último que tenía en mente cuando Lilly dijo que ella decidiría adónde tendríamos nuestra cita."

"Ningún hombre o mujer está vestido en menos que su ropa más fina, su formalidad solamente igualada por la de su alrededor; un exquisito papel tapiz rojo adorna las paredes mientras que las luces de la ciudad mucho más abajo parpadean y brillan."

"Combinado con el susurro ambiental de conversaciones tranquilas y el agudo ruido de los servicios y copas de vino, el ambiente es muy formal."

"Sin embargo es lo suficientemente relajado para no sentirme demasiado tenso a pesar de ser esta nuestra primera cita real."

"Una vez que nos sentamos, nuestro mesero se retira para atender a otras personas con una breve reverencia, luego de un asentimiento de aprecio de Lilly."

"Lejos de depender de mi ayuda, Lilly ha logrado orientarse con sorprendente facilidad hasta ahora, a pesar del ambiente poco familiar. Un ligero roce por aquí y por allá, y ella generalmente es bastante hábil orientándose cuando lo necesita."

$ ksgallery_unlock("evul lilly_restaurant_listen")
scene ev lilly_restaurant_listen at restaurant_out
with whiteout

"Mis ojos miran los de Lilly. Puedo darme cuenta por su rostro de que ella está escuchando sus alrededores con tanta atención como yo estoy mirando."

"Aunque a decir verdad, mis ojos se quedan en ella cada vez que recorren el cuarto. El qipao rojo que lleva puesto acentúa su figura de muy buena forma y muestra sus piernas. Hasta su cabello está recogido, y el olor de perfume se nota apenas."

"Si bien mi traje negro es arrendado, logré seleccionar uno apropiado, se siente sorprendentemente cómodo considerando que rara vez he usado uno, y calza con la situación tan bien como el atuendo de Lilly."

hi "¿Supongo que esta es una experiencia nueva para ambos, entonces?"

$ ksgallery_unlock("evul lilly_restaurant_sheepish")
show ev lilly_restaurant_sheepish at restaurant_out
with charachange

"Ella se da vuelta un tanto avergonzada."

li "Nunca he venido a un lugar como este antes, no."

hi "Vaya primera cita, eso es claro. Me va a ser bastante difícil superar esto."

"Una risita ligera. Incluso ahora, nuestro nerviosismo se está disipando."

"Su mano se desliza por el centro de la mesa hasta que toca el menú, el cual toma con ambas manos y lleva hasta su rostro."

li "¿Um, Hisao?"

"Cuando ella baja la lámina beige plastificada justo bajo sus ojos, puedo ver otra expresión avergonzada."

"Dudo que pedirle al mesero un menú en braille sea productivo."

hi "Puedo leértelo, no hay problema."

scene bg city_restaurant at right
with locationchange

"Tomo el mío y le doy una rápida lectura, mi sonrisa flaqueando."

hi "Er, quizás sí lo hay."

show lilly basic_weaksmile_che_close:
    center
    ypos 1.1
with charaenter

li "¿Qué ocurre?"

hi "Hay bastantes opciones aquí… y no estoy del todo seguro de cómo pronunciar unas cuantas de ellas."

"Hay listado un platillo fino tras otro. La mayoría estará en japonés, pero unos cuantos están en inglés y francés. Supongo que era de esperarse, pero no tengo idea de qué están hechos algunos de ellos."

"Oh, este lo reconozco. Espera, un momento…"

hi "… ¿Se puede cocinar eso?"

show lilly basic_giggle_che_close
with charachange

"Una risita ligera de diversión sale desde atrás de la lámina de papel."

hi "Bueno, podría leerlos todos, pero tomaría unas cuantas horas."

show lilly basic_smile_che_close
with charachange

li "¿Hay algo que tenga alguna variedad de pescado?"

hi "Veamos…"

"No. No. No. No. ¿Esos no son venenosos? No. No. No. ¿Se comen esa cosa? No. No. No. No… Ah, aquí vamos."

hi "Una buena opción parece ser una ensalada de atún. Por la foto, también parece ser una porción más que suficiente."

show lilly basic_smileclosed_che_close
with charachange

li "Esa parece una opción razonablemente segura."

hi "Entonces ordenemos dos. Estoy bastante seguro de que un par de estos platos provienen de animales venenosos. Ya he tenido suficientes encuentros con la muerte por el momento."

show lilly basic_weaksmile_che_close
with charachange

"Lilly mantiene la sonrisa, pero hay una ausencia particular de risa. El humor negro puede no ser de su agrado, pero a decir verdad yo tampoco lo encuentro excesivamente divertido."

li "Ciertamente hay bastantes olores interesantes flotando por aquí. Lo mismo es cierto con lo que se puede ver, asumo."

hi "Nunca he estado en ningún lugar parecido a este. Una casa de té japonesa llamativa en un par de ocasiones, pero nunca algo tan espléndido ni de estilo tan europeo."

"Antes de poder decir más, un mesero corpulento en un traje dolorosamente ajustado aparece junto a nuestra mesa para tomar nuestras órdenes."

hi "Salade Niçoise de Atún a la provenzal, por favor. Dos."

"Espero no haber cometido muchos errores con la pronunciación de eso. Aun si lo hice, él no lo demuestra."

show lilly behind_cheerful_che_close
with charachange

li "Y me gustaría una copa de Chardonnay, por favor. ¿Hisao?"

hi "Oh, uh, lo mismo."

"Cuando el mesero asiente y se retira, de pronto me doy cuenta de lo que dije al imitar distraídamente la respuesta de Lilly. Lo lamento muy rápidamente."

hi "Alcohol…"

show lilly basic_pout_che_close
with charachange

li "Solamente un poco."

"Esta chica tiene propensión a quedar enganchada a las cosas, lo juro."

hi "Me sorprende que no hayan pedido identificaciones."

hi "Por otra parte, supongo que ambos nos vemos maduros para nuestra edad."

show lilly basic_smileclosed_che_close
with charachange

li "Tendré que aceptar lo que dices. Pero debo añadir que este no es lo que llamaría el tipo de lugar que pida tal cosa."

hi "Buen punto."

"Ambos nos relajamos un poco en nuestros asientos, intentando apartar nuestras mentes de la agobiante formalidad de nuestros alrededores."

"Tan pronto como lo hacemos, el mismo mesero vuelve a aparecer junto a nuestra mesa con dos copas vacías y una botella, cuyo contenido es rápida y profesionalmente vaciado en las primeras."

scene ev lilly_restaurant_wine:
    zoom 1.05 xalign 0.0 yalign 0.5 subpixel True
    easeout 8.0 zoom 1.0
with flash

"Ambos asentimos de forma educada y él se retira, tomando Lilly su copa y moviéndola de lado a lado."

"El líquido en su interior destella a medida que se mueve por la copa, y tengo que admitir que me hace sentir un poco menos arrepentido de haber pedido lo mismo."

"Supongo que debe requerir esfuerzo juzgar cómo está actuando el líquido adentro basada únicamente en su centro de balance. Quizás es como su origami; toma cada pequeña oportunidad para practicar su destreza."

hi "Supongo que no me sorprende que conozcas un lugar como este. Aquellos con dinero lo harían, supongo."

"Esto me recuerda a las formas tan completamente distintas en que fuimos criados. En Yamaku, es fácil olvidarse de las diferencias sociales y económicas entre los estudiantes usando todos el mismo uniforme, viviendo en los mismos dormitorios."

scene bg city_restaurant at right
show lilly basic_smile_che_close:
    center
    ypos 1.1
with flash

li "Bueno, Akira fue quien me contó al respecto. Ella ha venido a este lugar antes, aparentemente."

"Entonces sobre eso era lo que conspiraban el viernes."

hi "¿Y tú me recriminas por hacer trampa?"

show lilly basic_displeased_che_close
with charachange

li "Eso no es hacer trampa. Es simplemente hacer uso de contactos."

hi "Si tú lo dices. De todas formas, tengo la sensación de que estás más familiarizada con este tipo de restaurantes que yo."

show lilly basic_reminisce_che_close
with charachange

with Pause(0.5)

show lilly basic_smileclosed_che_close
with charachange

"Ella se detiene un momento, con una mirada anhelante, antes de sonreír ligeramente. El cumplido parece animarla."

show lilly basic_planned_che_close
with charachange

li "Puedes agradecerle a mi antigua escuela por eso. Si aparentara menos, estarían gravemente decepcionados."

"Ella ha mencionado su educación previa anteriormente, pero ahora siento algo de curiosidad. Ella parece pensar mucho con respecto a su pasado, así que no veo problema con preguntar."

hi "¿Cómo era allí?"

show lilly basic_smile_che_close
with charachange

li "Era prestigiosa, para damas, y católica; esos hechos hicieron que mis padres la escogieran para mí. Muchas familias adineradas enviaban a sus hijas allí."

hi "Por cómo suena, la vida en ese lugar debe haber sido bastante estricta."

show lilly basic_weaksmile_che_close
with charachange

li "No diría que fue una mala experiencia… pero estás en lo correcto; era muy estricta. Afortunadamente, logré adaptarme lo bastante bien e hice bastantes amigos."

show lilly basic_reminisce_che_close
with charachange

li "Desafortunadamente, no se puede decir lo mismo de mi hermana. Ella encontró el ambiente y los aspectos religiosos sofocantes, y terminó marchándose por un trabajo tan pronto como fue capaz de hacerlo."

show lilly basic_weaksmile_che_close
with charachange

"Ella suelta una pequeña carcajada con desprecio propio."

li "Aunque no debería quejarme por ello. No muchos tienen la oportunidad siquiera de ir a tal escuela."

hi "¿Tú… sientes resentimiento hacia tus padres por enviarte ahí, y luego marcharse?"

"Ella suavemente niega con la cabeza."

show lilly basic_reminisce_che_close
with charachange

li "Mi familia es muy patriarcal. Mi padre, pensando siempre en el negocio, no tenía idea de qué hacer conmigo."

show lilly basic_weaksmile_che_close
with charachange

li "Al final, él decidió que mi educación era más prioritaria que permanecer con la familia."

li "Él simplemente hizo lo que pensó que era lo mejor."

"Decir una cosa así tan fácilmente. Qué chica más increíble. Dicho sea eso, estoy un tanto sorprendido de que ella no considere que su ceguera tuvo que ver en absoluto… aunque quizás estoy siendo demasiado duro con su familia."

hi "Eres demasiado amable, ¿lo sabes?"

show lilly basic_surprised_che_close
with charachange

li "¿Hmm?"

hi "La mayoría odiaría a sus padres por algo como eso."

show lilly basic_weaksmile_che_close
with charachange

li "Bueno, algunos lo hacen…"

"Sin saber que he levantado mis cejas, ella toma un sorbo de su copa. El vino baja sin esfuerzo, su gusto por ello evidentemente ayudándola a tratar con el sabor del alcohol. No puedo decir que lo mismo se aplique a mí."

show lilly basic_smile_che_close
with charachange

li "¿Y qué hay de ti? ¿Cómo fue tu educación?"

hi "¿La mía? Veamos…"

hi "Era una escuela pública bastante normal, supongo, quizás un poco más agitada de lo normal."

hi "Me iba bastante bien en clases y jugaba en el club de futbol. Ya que soy hijo único y mis dos padres trabajaban mucho, gastaba la mayor parte de mi tiempo libre y mi dinero en la sala de juegos con mis tres amigos."

hi "Pero sin importar lo mucho que jugara, nunca logré vencer a Mai en ninguna de esas máquinas."

hi "Hasta Takumi y Shin perdían contra ella cuando lo intentaban. Y luego quedaba a cargo de intentar ser el adulto responsable cuando Shin y Mai peleaban. Otra vez."

hi "Solo nosotros cuatro, disfrutando de nuestra infancia sin un rumbo fijo. Esos fueron unos tiempos llenos de tonterías."

"Me interrumpo a mí mismo cuando me doy cuenta de que estoy comenzando a divagar, los días en mi antigua escuela desapareciendo bajo el cielo nocturno y las brillantes luces de la ciudad por la ventana."

"El rostro de Lilly es una extraña mezcla de curiosidad y simpatía. Dada la manera estricta en que fue educada, supongo que algo como esto parecería dar un contraste interesante a la única vida que ha conocido."

show lilly basic_satisfied_che_close
with charachange

li "Suena que tu escuela anterior era muy divertida."

hi "En realidad no sé cuánto de eso es nostalgia, pero hay algunos recuerdos agradables."

hi "Pero eso está en el pasado. No puedo volver allí ahora, pero por mi accidente he encontrado una nueva vida que nunca me hubiera imaginado tener."

hi "La paz y tranquilidad de Yamaku, una nueva dirección para mi futuro en las ciencias, la amistad de Shizune, Misha y Hanako, y por sobre todo, tú."

scene ev lilly_touch_cheong
with whiteout

"Ella muestra una profunda y genuina sonrisa mientras mueve su mano hacia mí, sus dedos apenas buscando mi rostro antes de acariciar suavemente mi mejilla."

scene bg city_restaurant at right
show lilly basic_smileclosed_che_close:
    center
    ypos 1.1
with whiteout

"Su mano se retira con recelo luego de un segundo de cálido silencio, cuando notamos al mesero llegando con nuestra comida."

"Lilly hace un excelente trabajo encubriendo su condición, excepto por el hecho de que su asentimiento hacia él está un poco desalineado debido a su silencio."

"Ella de verdad parece esforzarse en parecer tan normal como sea posible en público. Si bien lo noté hace ya un tiempo, aún no puedo determinar del todo si es por querer no ser tratada de forma diferente, un sentimiento de vanidad, o una mezcla de ambas."

scene ev lilly_restaurant_eat
with shorttimeskip

"El plato que fue servido es digno del nombre de ensalada, y la porción es agradablemente grande. Con huevos y tomates en rodajas, de verdad se ve apetitoso."

"Lilly toma su cuchillo con una mano y su tenedor con la otra, poniéndose a trabajar rápidamente al mismo tiempo que yo. Es más tarde de lo que usualmente cenamos, así que ambos estamos deseosos de comenzar."

scene ev lilly_restaurant_chew
with locationchange

"Mi cauteloso corte de hojas y cuadrados vagamente similares a carne con mi tenedor es seguido por el mesurado y silencioso picar y masticar de Lilly."

"Un golpecito ocasional alrededor de los lados de un trozo de comida para distinguir sus bordes es el único indicio de su falta de visión."

scene bg city_restaurant at right
with locationchange

"Acabo con mi plato en poco tiempo, Lilly dando las últimas mordidas mientras la observo sentado."

show lilly basic_smile_che_close:
    center
    ypos 1.1
with charaenter

li "¿Ya has acabado, Hisao?"

hi "Sí. Estaba bastante buena."

"Eso es muy cierto. Nunca pensé que una simple ensalada pudiera ser tan sabrosa y saciadora, pero por otra parte, supongo que es por eso que cuesta tanto comer aquí."

show lilly basic_smileclosed_che_close
with charachange

"Contenta con mi evaluación, y evidentemente de acuerdo, Lilly asiente ligeramente."

hi "Sabes, dado que eres en parte extranjera, de apariencia exótica y bastante bonita, me sorprende que nadie se te haya confesado antes."

show lilly basic_planned_che_close
with charachange

li "Estás asumiendo que nadie lo ha hecho."

"Esa simple afirmación me toma desprevenido. No debería estar sorprendido, dado que momentos antes acabo de darle un cumplido."

hi "¿De verdad?"

show lilly basic_smile_che_close
with charachange

li "He recibido varias confesiones, tanto en esta escuela como en la anterior."

show lilly basic_weaksmile_che_close
with charachange

li "La adolescencia es una época divertida."

"Habla como si estuviera por sobre ello…"

hi "Eh. Qué fácil te es decir tal cosa."

show lilly basic_surprised_che_close
with charachange

with Pause(0.5)

show lilly basic_cheerful_che_close
with charachange

"Lilly parece sorprendida por un momento, y luego una sonrisa juguetona cubre su rostro."

li "¿Son esos… celos?"

hi "¿Qué? No. No lo son."

show lilly basic_giggle_che_close
with charachange

li "Eres un mal mentiroso, Hisao. Deberías tomar eso en cuenta."

show lilly basic_smileclosed_che_close
with charachange

li "Por otra parte, de verdad aprecio lo sincero que eres. Aun si esa no es tu intención, en ocasiones."

li "Pienso que tu honestidad siempre te servirá cuando trates con otros."

"Suelto una tos simulando disconformidad con todo este asunto e intento desviar la conversación a otra parte."

hi "Pero, a decir verdad, prefiero la soledad a estar rodeado por otras personas. No creo que pueda mantener un círculo social como tú lo haces."

show lilly basic_listen_che_close
with charachange

"Ella medita sobre esto un momento."

show lilly basic_smile_che_close
with charachange

li "Tampoco creo que eso sea cierto."

show lilly basic_smileclosed_che_close
with charachange

li "He visto lo amable y preocupado que eres cerca de Hanako, y te llevas maravillosamente bien con otros, incluso aquellos a quienes apenas conoces. Pienso que eres bastante hábil en situaciones sociales."

show lilly basic_cheerful_che_close
with charachange

li "Pero con respecto a eso, ¿qué hay de tus confesiones, Hisao? Estoy segura de que alguien como tú debe haber tenido al menos una admiradora."

"Cuando abro mi boca para hablar, puedo sentir mi rostro volverse ligeramente hosco. En momentos como este, aprecio en secreto el hecho de que ella no puede ver mi expresión."

hi "Solamente… una vez. Se llamaba Iwanako."

hi "Fue cuando ella se me confesó que tuve mi ataque cardiaco. En el bosque, durante el invierno."

show lilly basic_oops_che_close
with charachange

"Lilly se encuentra a sí misma sin habla, sin esperar que el tema se desviara a tal área."

"Mi condición siempre ha sido algo que le preocupa, algo que intento minimizar a pesar de los mejores esfuerzos de mi cuerpo por hacer lo contrario."

hi "Después de eso, me visitó por un tiempo cuando estaba en el hospital. Ella vino y hablamos durante semanas. Usualmente era nada más que plática o chismes del grupo, pero eso era suficiente."

hi "Pero eventualmente… solo dejó de venir."

hi "Estaba ahí todos los días. Luego día por medio. Luego una vez a la semana. Luego finalmente, un día, solo dejó de visitarme por completo."

show lilly basic_sleepy_che_close
with charachange

li "¿Alguna vez… la volviste a ver?"


label es_choiceL24:
menu:
    with menueffect
    "Envuelto en mi propio mundo, niego con la cabeza antes de recordar lo inútil del gesto."
    "Mencionar la carta.":


        return m1
    "Terminar con el tema.":

        return m2




label es_L24a:

"El recuerdo de la única carta que Iwanako me envió se viene a mi mente."

hi "Nunca la volví a ver, pero luego de que me enviaran a Yamaku… me escribió una carta."

"El rostro de Lilly tiene una expresión que conozco bien. He captado su interés. Estaría algo ofendido de que sea simplemente un asunto de curiosidad para ella, pero nunca ha sido muy buena ocultando sus reacciones."

hi "En retrospectiva, en realidad no dijo mucho. Lo que pasaba con mi antiguo grupo, cómo le estaba yendo, y, casi como si se le hubiera ocurrido en el último momento, que probablemente era mejor para ambos que no nos volviéramos a ver."

hi "Luego de leerla, terminé por reevaluar muchas cosas que pensaba que ya había superado. En su mayoría, esa carta me recordó que el mundo a mi alrededor seguía en movimiento, y lo mucho que me había aislado de ello."

hi "Y… supongo que también me recordó lo que había perdido."

show lilly basic_emb_che_close
with charachange

"Ella piensa un poco sobre la información antes de que su rostro se ilumine por la realización. Sin duda se ha dado cuenta de que fue esta carta la que contribuyó a mi desasosiego durante aquel almuerzo en la azotea."

"Es raro ver a Lilly sin palabras, su persona completa un poco desmoralizada en relación a su arrebato de interés anterior. Por carismática que sea, al final eso no es sustituto de experiencia de vida o de relaciones."

show lilly basic_reminisce_che_close
with charachange

li "Quizás… es mejor que la haya enviado a que no."

hi "¿Cómo puede ser eso?"

show lilly basic_weaksmile_che_close
with charachange

li "Puede ser difícil resolver cómo comunicarse de la mejor forma con aquellos a quienes no has visto en mucho tiempo. Más aún, considerando sus situaciones separadas."

li "En lugar de hacer lo que era más fácil, ella reunió la valentía para hablarte una última vez; no solamente por su bien sino que, por cómo suena, también el tuyo."

hi "Quizás. No la odio por eso, y no es que alguna vez lo haya hecho, pero… no lo sé."

"Probablemente una respuesta más evasiva de la que debería dar, pero no es sin motivo. Nunca he visto la situación desde la perspectiva de Iwanako de esa forma antes."



label es_L24b:

"En verdad no quiero sacar el tema de Iwanako más de lo necesario. Esta cita es, después de todo, para mí y para Lilly. No quiero pensar en una relación anterior en un momento como este."

hi "No, eso fue lo último que vi de ella. Tampoco volvimos a hablar."



label es_L24c:

"Los segundos pasan en silencio antes de que Lilly vuelva a hablar."

show lilly basic_sad_che_close
with charachange

li "Mudarte a Yamaku debe haber sido difícil para ti, ya que te arrebataron a tus amigos y hasta a tu novia por algo que no era tu culpa."

hi "La peor parte de ello pasó mientras estaba en el hospital. Cuando todo lo que te rodea son cuatro paredes blancas y una televisión pequeña, tu mente cobra vida propia."

hi "Es como mi antigua escuela, supongo. Solamente intento no quedarme con lo que pasó en el pasado y seguir pensando hacia adelante."

hi "Todo ese recordar me deprime un poco, y es en gran parte gracias a ti que se siente como si las cosas volvieran a estar bien."

show lilly basic_veryemb_che_close
with charachange

li "Es… agradable oír eso, Hisao."

"Ella baja un poco su rostro, con una expresión pensativa. Supongo que fui demasiado lejos y la avergoncé."

hi "Supongo que tú pasaste por algo un tanto parecido a lo que yo cuando entraste a Yamaku de todas formas, ¿cierto? Me imagino que la gran mayoría de los estudiantes de nuestra escuela lo hizo, después de todo."

hi "Tú misma dijiste que hiciste amigos en tu antigua escuela. No puedo imaginarme que muchos te hayan seguido."

show lilly basic_displeased_che_close
with charachange

"La sonrisa de Lilly desaparece, su expresión oscureciéndose inesperadamente. Incluso sus manos retroceden hasta su regazo."

"Luego de un largo rato, ella habla."

show lilly basic_reminisce_che_close
with charachange

li "Hisao… ¿puedes prometerme no decirle a nadie lo que estoy por—"

hi "Lo prometo."

"Ella parece haber sido tomada por sorpresa por mi tono serio, pero luego cede y sonríe débilmente antes de continuar."

show lilly basic_weaksmile_che_close
with charachange

li "Cuando me mudé a Yamaku, sí me lamenté de haber perdido a los amigos que tenía en mi otra escuela."

show lilly basic_reminisce_che_close
with charachange

li "Pero hay una persona de la cual más me arrepiento de no haber vuelto a ver. Él era el motivo por el cual elegí el inglés como una carrera a futuro."

"¿“Él”? Considerando que ella vino de una escuela para chicas, entonces no debe haber sido un compañero…"

li "Rechacé las confesiones que recibí hasta entonces por él. Cada vez que mejoraba mis habilidades con el inglés, sus elogios eran mi recompensa más preciada."

show lilly basic_weaksmile_che_close
with charachange

li "Es gracioso, ¿no es así? Alguien como yo, capaz de jactarse de las personas que se han fijado en mí, queriendo a alguien tan completamente inalcanzable como mi tutor."

li "De verdad es la cosa más ridícula…"

hi "¿Te le…?"

"Ella rápidamente mueve su cabeza de lado a lado."

show lilly basic_displeased_che_close
with charachange

li "No pude. Incluso entonces, sabía que era imposible."

"Un silencio se apodera de ambos."

"Esto parece explicar su ferviente enfoque en su futuro como educadora de inglés, pero no puedo evitar pensar en su confesión a mí."

"Ella lo perdió sin haber expuesto vez alguna sus sentimientos… ¿acaso temió de alguna forma que eso volvería a pasar, pero conmigo?"

"En verdad no sé qué concluir de ello. He escuchado de tales relaciones antes; tabúes nacidos de cosas tales como la pubertad y la juventud. El hecho de que ella haya tenido el criterio de no actuar ante ello, sin embargo, es alentador."

show lilly basic_emb_che_close
with charachange

li "Sé que esto debe sonar extraño, pero por favor… no pienses de mí…"

hi "¿Por qué pensaría menos de ti por eso?"

hi "Para serte honesto, creo que él debe haber sido una muy buena persona si tú lo querías tanto. No solo eso, sino que te detuviste antes de ir demasiado lejos."

with Pause(1.0)

show lilly basic_arablush_che_close
with charachange

"Por un momento, ella parece algo perdida. Sin embargo, lo más inesperado es que no pasa ni un segundo antes de que comience a reír. El sonido me toma desprevenido. No es una risita, ni un bufido contenido, sino una carcajada genuina y honesta."

"Me veo a mí mismo sonriendo, y no solamente por su muestra de alivio y felicidad, sino porque ella confía en mí lo suficiente para dejarme ver este secreto tan privado."

scene ev lilly_touch_cheong
with whiteout

"Antes de darme cuenta, siento su palma tocar mi rostro. Su toque es tan suave como siempre, con su pulgar acariciando lentamente mi mejilla."

li "Eres amable, Hisao. En verdad te amo."

"Ver su rostro así, con su palma acariciando gentilmente mi cara… Creo que esta noche ha sido una noche maravillosa."

hi "Supongo que ambos hemos tenido pasados bastante extraños, ¿eh?"

li "Pienso que para la mayoría de los estándares, nuestro presente también es bastante curioso."

"Sonrío y dejo caer mi cabeza. Esta mujer puede dejarme en vergüenza, de eso estoy bien seguro."

scene bg city_restaurant at right
with whiteout

"Miro hacia atrás alrededor del cuarto con su continuo y silencioso murmullo de los comensales."

hi "Este lugar probablemente cae en la categoría de “curioso” también."

show lilly basic_weaksmile_che_close:
    center
    ypos 1.1
with charaenter

li "Es un poquito… avasallador."

hi "Esa es una forma de describirlo, sí."

"Llamo la atención de un apresurado mesero, un individuo bajo y flaco que no debe tener más de veinte. Me recuerda un poco a Kenji, aunque a diferencia de él, el mesero no está vestido como si fuera invierno en pleno verano."

show lilly basic_smileclosed_che_close
with charachange

"Luego de una reverencia seca y un ofrecimiento para llevarse nuestros platos, Lilly pide la cuenta de forma educada y suave."

"Con una coordinación experta, él maniobra entre las mesas, con nuestros platos en mano, para ir a buscar nuestra cuenta."

"No se demora en reaparecer entre las puertas, entregándole con elegancia nuestra cuenta a Lilly."

show lilly basic_smile_che_close
with charachange

"… quien de inmediato me la pasa a mí, haciendo que él levante una ceja."

"Cuando leo el pequeño boleto impreso por computadora, el costo es considerablemente mayor al que esperaba."

show lilly basic_surprised_che_close
with charachange

li "¿Hisao?"

hi "Oh… uh…"

show lilly basic_smileclosed_che_close
with charachange

"Rápidamente tartamudeo el monto, ante el cual Lilly simplemente asiente y alcanza su cartera."

"Dándole su tarjeta al mesero, este desaparece una vez más."

hi "Esa fue… una cantidad desproporcionadamente grande de dinero."

show lilly basic_emb_che_close
with charachange

"La afirmación parece poner a Lilly un poco incómoda."

show lilly basic_weaksmile_che_close
with charachange

li "Mi familia me deja más que suficiente para mi educación. Lo mismo va para mi hermana, aunque a ella le desagrada que le recuerden ese hecho."

show lilly behind_cheerful_che_close
with charachange

li "Dicho eso, a mí también me desagrada desperdiciar el dinero. Pero por esta vez creo que puedo hacer una excepción. Solo por ti."

hi "No solamente escogiste nuestra cita, sino que pagaste por ambos también…"

"Sostengo el caballete de mi nariz con mis dedos."

hi "No puedo creer lo alto que has puesto la vara para nuestra próxima cita."

show lilly basic_giggle_che_close
with charachange

"Ella suelta una risita."

show lilly basic_smileclosed_che_close
with charachange

li "La esperaré con ansias, Hisao."

"El mesero reaparece junto a nosotros, como si fuera magia, y le devuelve su tarjeta a Lilly. Evidentemente notando su falta de visión, coloca la tarjeta en su mano con una cantidad extra, quizás innecesaria, de firmeza para asegurarse de que la sostuvo."

"Retirándose, él ejerce un poco de diplomacia manteniendo una expresión neutral a pesar de mi propia expresión."

"Juntando mis manos en un aplauso, me levanto de mi asiento para poder terminar nuestra salida nocturna."

hi "¿Nos retiramos entonces, milady?"

stop music fadeout 2.0

scene black
with dissolve




label es_L25:

scene black
with Dissolve(2.0)

scene bg school_dormhisao_ni
with vpunch

hi "¡Guah!"

"Me levanto bruscamente de mis sábanas y me siento completamente erguido en la cama, como si un golpe eléctrico acabara de recorrer todo mi cuerpo."

"El aire nocturno se siente frío contra el sudor en mi piel desnuda, y mi respiración corta e irregular casi llega al punto de hiperventilación."

"Mi mente acelerada, llevo mi mano a mi cabeza en un intento de calmar mi cuerpo en pánico. Me toma unos cuantos segundos darme cuenta de que mi mano está temblando violentamente, aun mientras la presiono contra mi rostro."

"Pasan más segundos en completo silencio, mis intentos desesperados por aplacar mi cuerpo y mi mente lentamente, por suerte, funcionando."

"Recuperando la compostura, comienzo a medir el estado en el que me encuentro. Se siente como si acabara de correr un maratón, cada músculo tenso y el sudor prácticamente cayendo de mi cuerpo."

"Dirijo mi atención con cuidado al pálpito en mi pecho, midiendo el ritmo en mi mente. En efecto, mi poco confiable corazón está funcionando apropiadamente, para variar."

"Tan solo… ¿qué demonios fue eso?"

"¿Un ataque cardiaco? ¿Una mala pesadilla? ¿Efectos secundarios de la medicina? He oído acerca de los ataques de pánico, y esto parece cumplir con las características de uno…"

"Ni siquiera puedo molestarme en pensar al respecto en estos momentos. Me siento completamente exhausto y a la vez completamente despierto, luego de esta experiencia."

"Vuelvo la mirada al otro lado de mi cama, el pálido blanco del rostro de la silenciosa figura casi brillando en la oscuridad nocturna del cuarto. Solo el poder verla es suficiente para calmarme significativamente."

scene ev lilly_sleeping_smile:
    truecenter
    zoom 1.0 subpixel True
    acdc_warp 20.0 zoom 1.05
with locationchange

"Su grácil comportamiento persiste incluso cuando está dormida, su respiración perfectamente medida y su rostro gentil haciendo imposible distinguir si está despierta o de verdad durmiendo."

"Cediendo ante la tentación, paso delicadamente mis dedos por su mano. Su piel es suave al tacto, como siempre lo ha sido, y a la vez cálida incluso en el frío de la noche."

"Es en momentos como este, apreciando en silencio la presencia del otro, que siento que estamos más cerca el uno del otro."

"Mis dedos se detienen en su muñeca y vuelvo a llevar mi mano hacia la cama a mi lado."

"No estoy del todo seguro de por qué, pero a medida que nos acercamos el uno al otro, se sintió como si algo creciera entre nosotros. No estoy del todo seguro de qué es, ni si existió antes de que nos enamoráramos."

"Todo está pasando tan rápido. No me importa en absoluto, pero se siente muy impropio de Lilly estar llevando las cosas así de rápido."

scene bg school_dormhallway
with shorttimeskip

play music music_dreamy fadein 2.0

"Afortunadamente, no hay estudiantes paseando por los pasillos a esta hora de la mañana, si no estaría siendo interrogado sobre por qué llevo dos bandejas de desayuno a mi habitación vestido con un uniforme evidentemente puesto con apuro."

"No es que este tipo de cosas nunca sucedan, por supuesto. Un solo guardia de seguridad patrullando entre dos conjuntos de dormitorios situados uno junto al otro es una fuerza muy pequeña, en comparación con las hormonas adolescentes."

"Ahora que lo pienso, el hecho de que sea lunes por la mañana probablemente ayude. No estoy realmente seguro de por qué, pero los lunes parecen molestarme menos que a la mayoría."

"Me toma un poco de creatividad con mis manos y codo, pero eventualmente logro arreglármelas para abrir la puerta de mi dormitorio."

scene bg school_dormhisao
show lilly basic_sleepy_paj at center
with locationchange

"Entrando, veo a Lilly recién levantándose de la cama y frotando sus ojos, cansada. Está hecha un desastre, tal como la mayoría de las veces que la he visto tan pronto como se despierta. Ella de verdad no es una persona madrugadora."

hi "Lo siento, no era mi intención despertarte."

show lilly basic_displeased_paj
with charachange

"Ella niega adormilada. La luz matutina iluminándola es una vista muy agradable."

show lilly basic_weaksmile_paj
with charachange

li "Está bien, necesitaba levantarme de todas formas. ¿Qué hora es?"

"Dejo mi bandeja sobre mi escritorio y me doy vuelta hacia el reloj para comprobar la hora."

hi "Todavía es temprano. No te preocupes, queda bastante tiempo antes de que comiencen las clases."

show lilly basic_smileclosed_paj:
    ypos 1.2
with dissolvecharamove

"Ella se sienta a un lado de la cama y comienza a oler el aire. Cuando hace eso, rápidamente aparto su bandeja y la coloco sobre el escritorio junto a la mía."

hi "Sí, nos traje desayuno. Pero la ducha y la ropa vienen primero."

scene ev lilly_kissing
with flash

"Ella se queda quieta un momento con su barbilla apuntando un poco hacia afuera. Yo acepto encantado y junto mis labios a los de ella, saboreando la dulce sensación antes de apartarme."

scene bg school_dormhisao
with locationchange

"Con una sonrisa corta y dulce, aparentemente bastante satisfecha, ella lentamente se dirige a las duchas."

"Me estiro e intento despertarme un poco más, mirando brevemente hacia los humeantes platos sobre el escritorio. Arroz, pescado, sopa de miso y algunos vegetales; un desayuno estándar para un día algo inusual."

"Tomo los frascos de mi escritorio y comienzo a tomarme mi régimen diario de píldoras."

show pills:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"A veces me pregunto siquiera para qué sirven estas, dados todos los problemas que he tenido desde el accidente inicial. Ni siquiera puedo decir que no me duela tomármelas, considerando los efectos secundarios hasta ahora."

"Bueno, como sea. Las órdenes del doctor son que tengo que tomármelas, y la razón sugiere que más me vale confiar en su juicio por sobre el mío."

show pills:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide pills
with None

"No toma mucho tiempo para que el sonido de la regadera se detenga, siendo una ducha rápida aparentemente suficiente para Lilly, dadas las circunstancias."

show lilly basic_smile_paj:
    center
    xpos 0.55
    easein 0.5 xpos 0.5
with charaenter

"Saliendo del baño, se ve significativamente más despierta, habiendo tenido la oportunidad de recobrar su consciencia."

show lilly basic_smile_paj_close at center
with characlose

show lilly basic_smileclosed_paj_close:
    ypos 1.1
with dissolvecharamove

"Sin decir palabra, gentilmente tomo su mano con la mía y la guío a mi escritorio. Considerando que no tengo una mesa en mi habitación como ella, tendrá que bastar."

li "Gracias, Hisao. ¿Qué preparaste para el desayuno?"

hi "Solo arroz y vegetales. Algo rápido."

show lilly basic_ara_paj_close
with charachange

"Su rostro se ilumina ante la revelación."

show lilly basic_satisfied_paj_close
with charachange

li "Ese es un desayuno bastante grande. ¿Esto es normal para ti?"

"Ahora simplemente está intentando ser simpática. No tengo dudas, considerando su pasado, de que esta no es una comida de alta categoría en su estándar."

hi "El desayuno es la comida más importante del día. Solo porque somos estudiantes no significa que podamos tomárnoslo a la ligera."

"Eso es lo que creo, de todas formas. Por lo que otros con quienes he hablado han dicho, tal vez soy minoría."

show lilly basic_smileclosed_paj_close
with charachange

"Tomo asiento a un lado de mi cama y comienzo a comer junto con Lilly, sus palillos golpeando suavemente los perfiles de los vegetales tal como la vi hacerlo en nuestra cita."

show lilly basic_smile_paj_close
with charachange

li "Esto está bastante bueno, Hisao. No tenía idea de que podías cocinar así de bien."

"Esta vez es mucho más verdadero, de esto al menos puedo darme cuenta. Dicho sea eso, cocinar realmente no es algo especial; después de un poco de práctica es bastante fácil hacer platos simples."

hi "La mayor parte del crédito se lo lleva la tecnología moderna; de todas formas, luego de años de cocinar para mí mismo, eso espero."

hi "Me aburrí de comer fideos instantáneos y ordenar pizza cada vez que mis padres estaban trabajando, así que aprendí por mi cuenta cómo hacer unos cuantos platos. Pero todavía intento agarrarle la mano."

show lilly basic_cheerful_paj_close
with charachange

li "Serás una buena esposa algún día, Hisao."

"Tomo un grano de arroz y lo coloco en mi pulgar, antes de apuntar con cuidado y arrojarlo con el índice."

show lilly basic_surprised_paj_close
with vpunch

"Lilly da un saltito cuando llega a su mejilla, justo al blanco."

show lilly basic_pout_paj_close
with charachange

"No puedo evitar reírme un poco a sus expensas cuando baja su ceja e intenta con todas sus ganas poner una expresión seria y severa."

show lilly basic_sleepy_paj_close
with charachange

li "Oh, es cierto…"

hi "¿Qué cosa?"

show lilly basic_concerned_paj_close
with charachange

$ renpy.music.set_volume(0.5, 1.0, channel="music")

li "¿Tuviste algún problema para dormir anoche? Parecías preocupado."

"Así que estaba despierta en ese momento, o al menos en parte. Ya sea que fuera por mi corazón o una pesadilla causada por los efectos secundarios de mis medicamentos, lo último que quiero es que se preocupe más por mí."

"Incluso antes de mi relación con Lilly, he sentido que mi cuerpo era un obstáculo en todo lo que hacía. Mi cuerpo es mi carga, así que mientras esté con ella, seguiré actuando tan normalmente como sea posible."

hi "No, no particularmente."

show lilly basic_reminisce_paj_close
with charachange

li "Si es así… entonces eso es bueno."

$ renpy.music.set_volume(1.0, 4.0, channel="music")

"Afortunadamente, ella parece confiar en mi palabra."

show lilly basic_weaksmile_paj_close
with charachange

li "Ahora que lo pienso, había algo más que quería preguntar."

hi "¿Oh?"

show lilly basic_smileclosed_paj_close
with charachange

li "Cómo debería decirlo…"

show lilly basic_smile_paj_close
with charachange

li "¿Cuando sueñas… ves personas y objetos?"

hi "Sí, por supuesto que… oh."

"Me siento más que un poco avergonzado por ese lapsus, por honesto que haya sido. Pero Lilly se ve impasible."

show lilly basic_smileclosed_paj_close
with charachange

li "¿Pero no sientes sabores, tacto, ni hueles cosas?"

"Me muevo para responder, pero me veo a mí mismo estancado antes siquiera de pensar al respecto. Mientras más cavilo, más me doy cuenta de que su hipótesis es correcta."

hi "Eso es… cierto, supongo. Nunca lo había pensado de esa forma. ¿Estás diciendo que tú sí?"

show lilly basic_smile_paj_close
with charachange

li "En general solo escucho en los sueños, pero sí, a veces también toco o huelo cosas."

show lilly basic_planned_paj_close
with charachange

li "Simplemente pregunto porque Akira pensó que era muy extraño que lo hiciera cuando saqué el tema con ella. Si tú tampoco, entonces quizás es debido a mi ceguera."

hi "Eso tiene sentido. Tú confías en tus otros sentidos más que yo, así que quizás eso afecta tus sueños también."

"Las maravillas del cuerpo humano, supongo."

"El resto del tiempo antes de las clases, comemos en silencio el abundante desayuno frente a nosotros, platicando brevemente mientras comemos."

stop music fadeout 2.0

scene bg school_dormext_full
with shorttimeskip

"Un rápido vistazo por la puerta nos asegura que nadie está mirando directamente a la entrada de los dormitorios de chicos, así que salimos caminando sin obstáculos."

play music music_soothing fadein 4.0

hi "Ah, el clima de hoy es agradable."

"Me estiro mientras Lilly y yo nos dirigimos afuera, el brillante sol de la mañana radiando sobre nosotros."

"A esta hora se pueden ver unos cuantos estudiantes haciendo lo mismo, dirigiéndose al edificio principal de la escuela ya sea desde los dormitorios o la puerta principal."

show lilly cane_smile_close at center
with charaenter

li "Se siente bien y cálido."

"Con nuestras manos unidas y su bastón golpeando el suelo, comenzamos en serio a caminar hacia el edificio de la escuela y unirnos a las hordas parloteantes de estudiantes a nuestro alrededor."

show lilly cane_smileclosed_close
with charachange

li "¿Este sería el último día de exámenes, no?"

hi "Sí. ¿Cómo te ha ido en ellos?"

show lilly cane_concerned_close
with charachange

li "Bastante bien, considerando todo. Pero tú pareces un poco estresado por ellos."

hi "Es así de obvio, ¿eh?"

hi "Pero no creo que sea solamente por los exámenes. Han pasado un montón de cosas en muy poco tiempo, y no me está yendo bien en las materias de humanidades."

show lilly cane_smileclosed_close
with charachange

li "¿Pero te está yendo bien en ciencia, no es así?"

hi "Bueno, para mí sería difícil que no me fuera bien en ciencias. Ahora que lo pienso, ¿no dijiste antes que no eras muy buena con las ciencias y matemáticas?"

show lilly cane_oops_close
with charachange

"Ella de pronto parece muy avergonzada, habiendo sentido mi comentario sin lugar a dudas. El orgullo de Lilly en verdad puede ser una espada de doble filo."

show lilly cane_smile_close
with charachange

li "Bueno, aparte de eso… ¿has pensado con respecto a lo que podrías hacer con esa habilidad? Parece una lástima desperdiciarla."

hi "Un poco, principalmente instado por Mutou."

hi "De cualquier forma, probablemente termine con ciencia como carrera de alguna forma."

show lilly cane_smileclosed_close
with charachange

li "Es bueno oír eso, Hisao."

scene bg school_gardens at bgleft
with locationchange

stop music fadeout 0.3
with vpunch

"Cuando entramos a los jardines, de pronto recibo una palmada no solicitada en la espalda."

"El culpable vestido de verde me rodea de una pirueta para saludarme, evidentemente sin prestarle atención alguna a Lilly a mi lado."

play music music_kenji fadein 0.5

show kenji neutral:
    center
    xpos 0.55
    easein 0.5 center
with charaenter

ke "Hola hombre, ¿qué cuentas? No te he visto desde hace un tiempo."

hi "Hola. Simplemente he estado ocupado con los exámenes y esas cosas."

show kenji tsun at center
with charachange

ke "Exámenes, exámenes. Un verdadero hombre del renacimiento no necesita estudiar para destacarse en tales cosas."

"Kenji sí me parece del tipo de personas a las que le va bien en la escuela, incluso si tiene una asistencia horrible y una mala ética de trabajo, así que no tengo motivos para dudar de su habilidad."

"A decir verdad, siento un poco de envidia hacia él; entre estudiar para los exámenes y mi tiempo con Lilly, prácticamente no he tenido tiempo para mí solo. Quizás esto es un poco como se siente Yuuko."

show kenji tsun at tworight
show bg school_gardens at center
with charamove

show lilly cane_smile_close at twoleft
with charaenter

li "Buenos días, Setou. Es bueno oír que te va bien."

"Se siente un poco extraño ver a Lilly hablar tan formalmente. Ella ha terminado por dirigirse a mí de forma mucho más casual a medida que pasan los meses, aunque igualmente la he visto hablar más formalmente con sus compañeros en ocasiones."

"Algunas personas nunca cambian, supongo. No es que diga que sus modales tranquilos y educados sean algo malo; después de todo, fue una de las razones por las que me gustaba estar junto a ella en primer lugar."

"Kenji parece tomarse un momento para distinguir quién está junto a mí, y probablemente no haya notado que estamos tomados de las manos tampoco. Me pregunto si esos anteojos que tiene de verdad hacen algo."

show kenji neutral at tworight
with charachange

ke "Oh, hola Lilly. Buena suerte con tus exámenes también."

show kenji tsun at tworight
with charachange

ke "Te veré después de la escuela entonces, hombre."

"La ligera agudeza de su voz me hace pensar que esas palabras eran más una orden que una despedida casual. Supongo que tendré que allanar las cosas luego."

hi "Claro. Nos vemos."



show kenji invis:
    xpos 0.6
with dissolvecharamove

hide kenji
with None

"Kenji asiente bruscamente. Se mueve para pasar a nuestro lado, pero está demasiado ocupado mirando hostilmente hacia donde está Lilly como para notar su bastón."

show lilly cane_surprised_close at twoleft
with charachange

"Antes de poder intentar reaccionar y salvar la situación, Kenji tropieza y extiende su brazo instintivamente en busca de algo con lo que afirmarse. Desafortunadamente, dicho apoyo resulta ser el brazo de Lilly."

show lilly cane_surprised_close:
    easeout 0.3 ypos 1.2 alpha 0.0
with Pause(0.5)

play sound sfx_pillow
hide lilly
with vpunch

$ doublespeak(ke,li, u"¡Gua!", u"¡Ah!")

"Ambos caen al suelo hechos un montón, conmigo de lado sintiéndome bastante inútil."

hi "Ah, maldición. ¿Están bien?"

show kenji invis:
    center
    ypos 1.2
with None

show kenji neutral:
    ypos 1.0
with dissolvecharamove

"Kenji rápidamente se levanta, en apariencia sin inmutarse por el accidente."

ke "No hay problema, hombre, no hay problema. Esto no es nada, mi cuerpo puede soportar peores abusos."

"Lilly yace boca abajo sobre el pasto. No parece estar lastimada por el incidente; más que nada asustada. Me acerco para ofrecerle ayuda."

hi "¿Estás bien, Lilly?"

show kenji happy
with charachange

ke "¿Oye, Satou?"

"Kenji le ofrece una mano, tocando tentativamente la de ella para darle a saber lo que está haciendo."

"Dirá algunas cosas odiosas a veces, pero pienso que podría ser una persona genuinamente buena en el fondo. Me imagino que se siente bastante mal por esto."

stop music fadeout 2.0

"Pero para su sorpresa y la mía, Lilly golpea el suelo con su puño sin advertencia previa."

play sound sfx_impact
with vpunch

li "¡Maldita sea!"

show kenji tsun
with charachange

"Kenji se detiene, tomado por sorpresa por completo ante su arrebato. Yo estoy igual de impactado; ella nunca ha actuado así antes, ni siquiera cerca de Shizune."

ke "Eh…"

show lilly invis_close:
    twoleft
    ypos 1.2
with None
show lilly cane_mad_close at twoleft

with dissolvecharamove

"Al parecer recién ahora recordando que hay gente a su alrededor, Lilly lentamente se pone de pie. Su expresión cuando lo hace me hace retroceder un poco."

show lilly back_listen_close
show lillyprop back_cane_close at twoleft
with charachange

"Solo veo por un instante su expresión antes de que se dé la vuelta, pero no es algo que vaya a olvidar pronto."

"Ella ha demostrado mucho enfado en sus enfrentamientos con Shizune, pero este destello de ira fue algo diferente. No hay manera de que sea simplemente por este pequeño incidente."

hide lilly
hide lillyprop
with charaexit

"Ella se detiene un momento antes de suspirar y adelantarse caminando. De verdad no sé qué interpretar de todo esto."

hi "Yo, eh… hablaré luego contigo, hombre. Nos vemos."

ke "Claro, nos vemos."

hide kenji
with charaexit

"Kenji se rasca la nuca intentando encontrar algo que decir, y luego se encoge de hombros y se marcha caminando, manteniéndose alejado de nosotros."

show bg school_gardens at right
with charamove

show lilly back_listen at center
show lillyprop back_cane at center
with charaenter

"Alcanzo rápidamente a Lilly. Ella gira un poco su cabeza para reconocer mi presencia, pero nada más."

"Probablemente deba reprenderla por estallar de esa forma, pero tampoco quiero entrar en una competencia de gritos con ella. Ella sigue obviamente molesta."

"Al final, mantengo mi boca cerrada y espero a que se calme."

scene bg school_hallway3
with shorttimeskip

"Luego de una silenciosa caminata, eventualmente llegamos al final de las escaleras del tercer piso y a la intersección donde nos separamos todos los días."

show lilly cane_listen_close at center
with charaenter

"Me doy vuelta hacia Lilly antes de que ella se marche. Si bien me gustan los cálidos y cómodos silencios que usualmente compartimos, este no fue nada de eso. No quiero dejar las cosas así."

hi "Pareces más… callada de lo normal recientemente. ¿Pasa algo malo?"

show lilly cane_displeased_close
with charachange

"Ella niega con la cabeza de forma casi automática, como para despejar cualquier idea de que deba preocuparme por ella."

li "Es solo que los exámenes me están pasando la cuenta. Estaré bien."

"No creo que ese sea el motivo. Casi lo digo, pero decido no hacerlo. No tiene sentido intentar sacárselo si no quiere decírmelo, en especial cuando está de tan mal humor como ahora."

hi "Si estás segura. Te veré luego, entonces."

hide lilly
with charaexit

"Cuando me doy vuelta hacia el pasillo para dirigirme a mi salón, la débil voz de Lilly resuena atrás de mí."

show lilly cane_concerned
with charaenter

li "Hisao, um…"

hi "¿Sí?"

li "…"

li "Lo siento."

hide lilly
with charaexit



"Con eso, Lilly comienza a andar por el pasillo hacia su propio salón, su mano deslizándose por el pasamanos de metal."

"Me quedo quieto y la miro hasta que gira hacia su salón y desaparece de mi vista, antes de dirigirme a mi propia clase con un buen grado de renuencia."

scene bg school_scienceroom at left
with locationchange

play music music_normal fadein 4.0

"Como es usual, llego temprano. Mutou está moviendo unas carpetas y papeles en su escritorio, preparándose para el día mientras un puñado de estudiantes deambulan por el salón, conversando."

"Si bien mis sentimientos hacia Lilly no se han disipado, lejos de ello, su mención de mi desempeño en los exámenes me recordó que tengo mi propia vida que atender."

"Luego de pensar en ello, me he dado cuenta de que de verdad quiero seguir una carrera de alguna forma relacionada con las ciencias, en lugar de simplemente que sean el camino de menor resistencia."

"Hasta ahora, no tenía mucha idea de en qué campo de las ciencias quería seguir. Solo “ciencia” es una categoría bastante amplia de trabajos."

"Algo que Lilly mencionó antes enfocó mis pensamientos. Algo que solamente había pensado a la ligera antes, no había considerado en serio seguir este camino en específico."

show bg school_scienceroom at right
with charamove

"Camino hacia el escritorio de Mutou, su atención demasiado enfrascada en preparar la lección del día como para notar mi llegada. Es lo mismo todos los días."

hi "Buenos días."

show muto normal at center
with charaenter

"Él levanta la mirada con una expresión de sorpresa moderada que rápidamente es reemplazada por su típica sonrisa incómoda."

show muto smile
with charachange

mu "Buenos días, Nakai. ¿Puedo ayudarte?"

hi "¿Le molesta si le pregunto algo?"

"Él baja la mirada hacia su desordenada pila de libros sobre el escritorio, antes de dejar los papeles en su mano y pararse con algo de dificultad para dirigirse a mí de forma apropiada."

mu "Para eso estoy aquí, después de todo. Pregunta."

hi "Simplemente me preguntaba… ¿cuál diría que es la motivación tras el enseñar?"

"Él piensa esta pregunta unos cuantos momentos antes de responder, evidentemente lejos de tener una respuesta preparada."

show muto normal
with charachange

mu "Si hablas con diez maestros diferentes, creo que obtendrás diez respuestas diferentes a esa pregunta."

mu "Si bien solamente puedo hablar por mí mismo, diría que enseño porque… hmm…"

"Él vuelve a sumirse en sus pensamientos, evaluando cuidadosamente la forma en que desea presentar su idea."

show muto smile
with charachange

mu "Piénsalo de esta forma; cuando eras niño, probablemente jugabas con palillos y piedrecillas en agua corriente como en cunetas o charcos, ¿cierto?"

hi "Sí. Creo que muchas personas hacen eso cuando son jóvenes."

show muto normal
with charachange

mu "Bueno, no es solamente cuando son jóvenes para algunos, pero sí adopta otra forma. Sin embargo, mi punto es que cuando uno hace eso, siente curiosidad con respecto a cómo fluirá o cambiará el agua."

mu "Todos, incluso a una temprana edad, poseen una curiosidad intensa sobre cómo funciona el mundo a su alrededor, incluso en sus detalles más pequeños."

mu "Aún siento esa curiosidad con respecto al universo."

mu "Incluso el solo leer sobre los nuevos descubrimientos o experimentos clásicos me entrega una sensación renovada de asombro con respecto a lo maravilloso que es todo, desde las estrellas más lejanas hasta los charcos más pequeños."

show muto smile
with charachange

mu "Simplemente deseo poder darle a otros aunque sea una pequeña parte de esa curiosidad que siento. Si puedo hacer eso, aunque tan solo fuese para una persona, creo que puedo ser feliz como maestro."

"Él se rasca la cabeza mientras repasa mentalmente lo que acaba de decir."

"Siento como que ahora lo entiendo mejor. Aun si es extraño con otras personas, él tiene un interés genuino en estar junto a los demás y ofrecerles una parte de su ser que valora."

"Lo que Lilly me dijo ayer resuena en mis oídos. “Creo que tú te llevas bien con los demás”, eh. Ella siempre ha dicho que yo tengo una curiosidad inusual…"

show muto normal
with charachange

mu "Lo lamento si eso fue un tanto disperso. ¿Responde a tu pregunta?"

hi "Lo hace, gracias."

hi "En realidad, también tenía otra pregunta."

mu "¿Oh? ¿Y qué podría ser?"

hi "Um… ¿tiene alguna guía o folletos de universidades? Ya es hora de que comience a realizar postulaciones."

"Él asiente y se agacha a buscar dentro de su escritorio. Cuando lo hace, noto que tiene una sonrisa notablemente auténtica. No creo que alguna vez lo haya visto actuar de forma tan natural con otros."

"Quizás este no es Mutou, el maestro, sino Mutou, la persona."

show muto smile
with charachange

mu "Aquí. Si necesitas más, siéntete libre de preguntar."

"Me entrega alrededor de media docena de folletos y trípticos de varios colores y tamaños, los cuales recibo con entusiasmo."

"Sí, será esta información la que usaré para forjar mi propio futuro. Creo que ahora, luego de todo este tiempo y todas estas pruebas, al fin puedo comenzar a ver el cuadro general de mi vida por delante."

"Mi cuerpo podrá ser de esta forma, pero mi mente sigue siendo muy capaz."

hi "Gracias."

stop music fadeout 2.0

scene black
with dissolve

$ suppress_window_after_timeskip = True



label es_L26:

window hide None

scene black
with dissolve

nvl clear
nvl show dissolve

n "\n\n“Esto es extraño”."

play music music_pearly fadein 5.0

$ ksgallery_unlock("evul hisao_teacup")
show ev hisao_teacup:
    truecenter
    alpha 0.0 subpixel True
    linear 30.0 alpha 0.5
with None

n "\n\nEse único pensamiento ha pasado por mi mente una cantidad incontable de veces desde que mi vida aquí comenzó."

n "Se siente como si fuera una forma fácil de desechar una pregunta difícil, como si simplemente etiquetar algo con esas tres palabras hiciera que desapareciera, o por lo menos que no valiera la pena seguir pensando en ello."

n "Mi vida antes de mi ataque cardiaco se siente más nebulosa cada vez que intento recordarla, y mi mente se esfuerza por seguir todos los eventos que de pronto suceden a mi alrededor desde entonces."

n "Escuché en algún lugar que así es como se siente ser dejado a tu suerte en un país extraño con solamente el conocimiento más básico del lenguaje local."

n "En efecto, cuando pienso al respecto, parece una analogía maravillosamente apropiada para lo que me está sucediendo."

nvl clear

n "\n\nPero se supone que tales situaciones también te vuelven muy competente en ese lenguaje de forma muy rápida, al verte forzado a aprenderlo para poder sobrevivir. Dicho de otro modo, la situación se vuelve del tipo “nada o ahógate”."

n "\nMe pregunto si de verdad he logrado nadar, después de todo este tiempo."

n "Los exámenes me estresan un montón, a pesar de que al fin están acabando, pero he mantenido la aprobación de Mutou, y ahora tengo una especie de dirección para mi futuro."

n "Pero sigo usando esa estúpida frase sin sentido."

n "\n\n“Esto es extraño”."

nvl clear

n "\n\nEn verdad es sorprendente lo rápido que uno llega a aceptar el estar rodeado de personas con discapacidades y condiciones increíblemente impactantes."

n "Tanto así, que de verdad me pregunto por qué me siento tanto como un extranjero."

n "\nCiertamente no es por falta de socialización o amistades. He llegado a conocer a la mayoría de mis compañeros al punto de dirigirme a ellos por sus nombres, y conozco a unos cuantos más en la escuela. Ya sea que les falte un brazo o una pierna, los estudiantes aquí son iguales a los demás de su edad."

n "\n\nPuedo recorrer los pasillos en los que alguna vez me perdía con una facilidad que no esperaba tener alguna vez, gracias a la disposición lógica de la escuela, y puedo hablar y dialogar con comodidad con mis maestros."

nvl clear
nvl hide dissolve

scene ev hisao_teacup:
    truecenter
    zoom 1.0 subpixel True alpha 1.0
    acdc_warp 20.0 zoom 0.8
with locationchange

window show

"Revuelvo suavemente el té en mi taza, la imagen reflejada de mi rostro distorsionándose por el líquido en movimiento."

"Esto es extraño… Solía odiar beber té."

hi "Quizás estoy pensando demasiado."

play sound sfx_teacup

"El conocido ruido de la porcelana chocando con su plato respectivo resuena."

li "¿Sucede algo?"

hi "No te preocupes, no es nada."

scene bg school_dormlilly
show hanagown normal:
    tworight
    ypos 1.15
show lilly basic_smileclosed_paj:
    twoleft
    ypos 1.2
with whiteout

"Bebo un largo sorbo del té frente a mí junto con las chicas."

"Simplemente pasar el tiempo en la habitación de Lilly bebiendo té con ella y Hanako. Se siente conocido, casi nostálgico."

hi "¿Entonces cómo va tu trabajo en el club de periodismo, Hanako?"

show lilly basic_satisfied_paj
with charachange

li "Yo también quiero saber, suena como que sería bastante interesante."

show hanagown distant
with charachange

"El rostro de Hanako se hunde debido a la atención puesta sobre ella, si bien su sonrisa delata el hecho de que en realidad le gusta ser el centro de atención de nosotros dos."

ha "Va… bien. Creo que estoy mejorando en eso."

ha "Naomi y un par de sus amigas manejan la mayoría de los trabajos… buscar historias y otras cosas."

show hanagown smile
with charachange

ha "Yo solamente hago las cosas de la computadora, como juntar las historias e imprimirlas. E-es agradable, porque puedo sentarme y concentrarme."

"Veo que la naturaleza débil con la tecnología de Lilly no es compartida por Hanako."

"Si bien estar sentada en una habitación compilando los artículos periodísticos de otros no me parece particularmente extrovertido, es reconfortante verla aumentar su círculo de amistades."

"Pasos de bebé, supongo. Probablemente sea demasiado esperar que se vuelva una mujer de mundo como Lilly."

show lilly basic_oops_paj
with charachange

li "¿Cómo encuentras a Naomi? He escuchado que ella puede ser bastante problemática en ocasiones."

"Y Lilly está entrando en modo maternal con Hanako. Dejarla partir es algo que ha tenido que aprender."

show hanagown worry
with charachange

"Hanako se rasca la mejilla, pensando su respuesta."

show hanagown smile
with charachange

ha "Naomi es… agradable. Es un poco ruidosa a veces, y un poco agotadora… pero es realmente servicial. Sus amigas son agradables también."

show lilly basic_cheerful_paj
with charachange

li "Es maravilloso escuchar eso, Hanako. Me alegra que hayas encontrado tal fuente de alegría."

"La sonrisa de Lilly es cálida y genuina, pero siento un dejo de melancolía en ella también. Hanako parece no notarlo en absoluto, pero no creo ni por un segundo que me lo esté imaginando."

"Supongo que es porque he llegado lentamente a poner más y más atención a todo lo que sucede a mi alrededor."

"Con las cosas pasando aparentemente cada vez más y más rápido, se siente como si me fuera a perder de algo si no soy tan observante como sea posible."

"Con los exámenes, mi nueva vida amorosa…"

"… El intentar planificar algo con respecto a mis opciones de estudios superiores y universidad, y mi condición cardiaca poniendo frenos a todos en momentos irritantemente aleatorios, mi cerebro ha estado en sobrecarga recientemente."

"Me hace apreciar los raros momentos de tranquilidad como este."

"Supongo que es por esto que Lilly llegó a apreciar sus caminatas semanales a la tienda de abarrotes y sus fiestas de té con Hanako, a pesar de su gusto por estar rodeada por otros; le dan un momento de paz en una vida ocupada y caótica."

hi "Gracias a Dios que los exámenes han acabado, ¿eh?"

show lilly basic_giggle_paj
with charachange

"El comentario se gana una risita honesta de ambas chicas. Parece ser que todos han estado mucho más felices desde que los exámenes acabaron la semana pasada."


hi "¿Entonces qué vas a hacer durante las vacaciones de verano, Hanako? Solamente quedan…"

"Rápidamente cuento los días en mi cabeza. Hoy es lunes, y las clases terminan el sábado…"

hi "… cinco días más, después de todo."

show hanagown normal
with charachange

ha "Estaba pensando en… viajar. Solamente… un poco."

show hanagown smile
with charachange

ha "Hay muchos lugares que quiero ver, y… creo que tengo suficiente dinero para pagar los pasajes de autobús y tren. Naomi y una de las otras chicas en el club de periodismo dijeron que quizás me acompañarían también."

"Su expresión indica que le ha dado al asunto bastantes vueltas. De cierta forma me sorprende que esté contemplando algo como esto."

"Parece ser que en verdad tiene intención de ir por su cuenta."

show lilly basic_smile_paj
with charachange

li "¿Hay algún lugar en particular al que pienses ir?"

show hanagown distant_blush
with charachange

ha "Estaba pensando que… Kyoto suena bien. P-pero… creo que intentaré ir a unos cuantos lugares."

show lilly basic_cheerful_paj
with charachange

"Lilly asiente aprobatoriamente, contenta con los planes de Hanako."

"Si bien poso mis ojos sobre Lilly, evito hacerle la misma pregunta. Ella ha estado evadiendo hablar de sus planes para el futuro durante un tiempo ya, pero nunca logro encontrar un buen momento para abordar el tema a solas con ella."

"Cada vez que tocamos el tema en una conversación, se siente como si ella no estuviera segura de ella misma o estuviera simplemente evadiendo la pregunta. Es preocupante."

hi "Asegúrate de llamar alguna vez cuando estés de viaje. Te di mi número antes, ¿cierto?"

show hanagown smile
with charachange

"Hanako asiente rápidamente, con una sonrisa de felicidad en su rostro."

"Es extraño ver lo feliz que las personas parecen volverse cuando tienen un objetivo hacia el cual avanzar. Yuuko parece animarse cada vez que se saca a tema sus aspiraciones universitarias, y ahora con Hanako es lo mismo."

"¿Entonces por qué siento esta incertidumbre? ¿Y por qué Lilly también?"

"Las relaciones pueden ser irritantemente problemáticas a veces."

show hanagown worry
with charachange

ha "Oh, um… ¿q-qué hora es?"

hi "¿Hmm? Oh…"

"Me toma un segundo recordar que el reloj de Lilly no tiene salidas visuales. De verdad debería saberlo, dadas las veces que he estado en su habitación."


"De cualquier modo, saco mi reloj de mi mochila y lo miro rápidamente, el motivo de su pregunta volviéndose aparente."

hi "Son las diez y veinte. Casi toque de queda."

show hanagown normal:
    ypos 1.0
with dissolvecharamove

"Hanako se para, sacudiéndose el polvo y arreglando su camisón después de eso."

show hanagown smile
with charachange

ha "Es… mejor que me vaya, entonces. Buenas noches Lilly, Hisao."

stop music fadeout 5.0

show lilly basic_smileclosed_paj
with charachange

li "Que duermas bien, Hanako."

hi "Nos vemos mañana."

hide hanagown
with dissolve

"Y con eso, ella camina hacia la puerta y realiza su salida en silencio."

show lilly basic_smileclosed_paj:
    xpos 0.5
show bg school_dormlilly at bgright
with charamove

"…"

"Silencio."

"Esto parece estar sucediendo más y más a menudo entre Lilly y yo recientemente. Luego de unos segundos, finalmente encuentro algo de qué hablar."

play music music_another fadein 4.0

hi "Oh cierto, hablé con Mutou el viernes, y al fin revisé algunas guías sobre universidades y cómo postularme para ellas."

show lilly basic_smile_paj
with charachange

li "Esas son buenas noticias. Si te vas a postular para algunas universidades, ¿asumo que tienes alguna idea en mente sobre qué quieres hacer en el futuro?"

hi "Creo que me he decidido por ser profesor de ciencias. Va a tomar un tiempo pasar por la universidad y todo para tener las certificaciones, pero creo que valdrá la pena."

show lilly basic_satisfied_paj
with charachange

"El rostro de Lilly se ilumina considerablemente por las noticias. Supongo que, con su deseo de volverse profesora, estará encantada por el hecho de que yo tomaré el mismo tipo de camino."

li "Entonces, has decidido seguir una carrera enseñando…"

show lilly basic_smile_paj
with charachange

li "Creo que ese camino te asienta excelentemente, Hisao."

"Sonrío y asiento. Esta vez, aun si sé que ella no puede verme, sé que lo siente."

show lilly basic_planned_paj
with charachange

li "¿Me imagino que Mutou habrá recibido bien la noticia?"

hi "Es una forma de decirlo."

hi "¿Oye Lilly?"

show lilly basic_smile_paj
with charachange

li "¿Sí?"

hi "Sé que quieres ser maestra, pero…"

"Por un segundo, considero si de verdad debería preguntarle lo que tengo en mi mente, pero eso rápidamente es apartado por el hecho de que es algo tarde para tener arrepentimientos."

show lilly basic_smileclosed_paj
with charachange

li "De verdad no creerás que me ofenderé por algo que tenga relación con mi ceguera."

"Su tono acusativo es traicionado por su rostro sonriente, divertida con mi incomodidad para sacar el tema. Algunas cosas nunca cambian."

hi "Buen punto, supongo."

hi "Tan solo estaba pensando si el ser ciega sería un obstáculo o no, ya que tu ambición es ser maestra y todo eso."

show lilly basic_surprised_paj
with charachange

"Ella parece un poco sorprendida antes de pensar un poco la pregunta. Me niego a pensar que nunca ha pensado esto antes."

show lilly basic_emb_paj
with charachange

li "Me pregunto… Hisao, ¿podrías cerrar tus ojos un momento?"

hi "¿De… acuerdo?"

"Levantando una ceja, hago lo que me pide."

$ renpy.music.set_volume(0.5, 2.0, channel="music")

scene black
with shuteye

"No tengo idea de qué tendrá en mente, y mis preguntas no hacen más que aumentar cuando hecho un vistazo por un ojo."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

show bg school_dormlilly at bgright
show lilly basic_smileclosed_paj_close at center
with openeye

"Sacando la cinta negra que usualmente usa en su cabello del gabinete junto a su cama, ella avanza hacia mí mientras lo pasa por sus dedos para eliminar cualquier cabello que haya quedado en el trozo de tela."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene black
with softwipedown

"De pronto comprendo su intención cuando siento la banda negra haciendo contacto con mi rostro, envolviendo mi cabeza y pasando por sobre mis ojos."

hi "Um… ¿para qué es esto exactamente?"

li "Es una pequeña prueba, Hisao. Ya que pareces estártelo preguntando, te dejaré ver las cosas como yo lo hago por un rato."

"Eh, entonces de eso se trata."

"A decir verdad, esto en realidad suena divertido. Infantil y un poco tonto para cualquiera que observe, pero un poco de tontería amena nunca ha dañado a nadie."

"Me levanto jadeando, mis manos rápidamente moviéndose frente a mí para advertirme de cualquier obstáculo."

hi "Bien, ¿ahora qué?"

li "Ahora, tócame."

hi "Si tú lo dices. Entonces…"

"Lentamente me abro camino hacia adelante, en dirección a la voz de Lilly."

"Mi velocidad caminando apenas podría ser llamada un deslizamiento, la experiencia entera sintiéndose tan extraña que no quiero arriesgarme a tropezarme con algo inadvertidamente, como su mesa o sus pilas caóticas de libros."

play sound sfx_rustling

"Algo blando, pero sólido, roza mi pierna izquierda. Una inspección más rigurosa revela que es la cama de Lilly."

"Sigo avanzando, agradecido de que la habitación de Lilly esté tan ordenada y limpia. Hasta las pilas de libros que tiene están en general cerca de las paredes, lejos del peligro."

play sound sfx_pillow

"La dura pared que hace contacto con mis manos extendidas me hace fruncir el ceño, frustrado."

hi "Oye Lilly, ¿dónde estás?"

li "¿Qué haces por allá? Yo estoy aquí."

"La voz de Lilly viene del otro lado de la habitación, lejos de donde estaba antes, incluso para mis oídos sin entrenar. ¿Si está haciendo un esfuerzo para evitar que la alcance, entonces esto es tan solo un juego para ella?"

"… Por supuesto que lo es. Comparada a una vida donde hasta el concepto de visión es uno abstracto, unos cuantos minutos con una venda en los ojos son nada."

"Supongo que ha dejado en claro su punto; ella es más que capaz de desplazarse por su cuarto, y más aun, he visto lo independiente que es comparada a muchos de los demás en Yamaku."

"Bueno, aun si esto es solamente un juego, bien podría jugarlo con todo mi empeño."

"A un ritmo mucho mayor que antes me dirijo hacia la fuente de su voz, evadiendo hábilmente la mesa en el centro de su habitación gracias al hecho de que recuerdo su posición."

hi "¡Ahora te tengo!"

"Ella suelta una risita traviesa, una lo suficientemente larga para distinguir que está pasando justo a mi lado."

play sound sfx_impact2
with vpunch

"Rápidamente me doy vuelta para encarar la nueva dirección— ¡la mesa no estaba ahí antes!"

hi "Au… au… au…"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

show bg school_dormlilly
with softwipeup

"Lentamente me siento junto a la mesa, levantando las vendas de mis ojos mientras froto mi cabeza adolorida."

play sound sfx_impact
with vpunch

"Le doy una patada irritado a la mesa que se encuentra justo frente a donde caí. Completamente inútil, pero esa cosa se lo merecía."

show lilly basic_oops_paj_close at center
with charaenter

li "¿Hisao?"

"Lilly sigue de pie justo a mi lado, obviamente sin estar segura de qué me ha sucedido."

hi "Lo siento. Como que me caí."

show lilly basic_concerned_paj_close
with charachange

li "¿Te has lastimado?"

hi "Me duele la cabeza, pero creo que estoy bien. Creo que la mesa se movió para hacerme caer."

show lilly basic_giggle_paj_close:
    ypos 1.1
with dissolvecharamove

"Ella se ríe mientras camina y se sienta junto a mí, su mano descansando sobre la mía."

show lilly basic_weaksmile_paj_close
with charachange

li "¿Entonces supongo que con eso se acaba todo?"

hi "Eso creo."

hi "Pero también creo que entiendo el punto. Aunque desearía que no hubiera tenido que sufrir tal dolor de cabeza."

show lilly basic_surprised_paj_close
with charachange

"Lilly súbitamente muestra un rostro inexpresivo."

li "¿El punto?"

"Y le respondo con una mirada extraordinariamente impasible."

hi "¿Eso solo era para divertirte?"

show lilly basic_reminisce_paj_close
with charachange

li "Simplemente pensé que podría introducirte con un poco más de facilidad al tema. Siempre pareces ir de puntillas al respecto, después de todo."

show lilly basic_smileclosed_paj_close
with charachange

li "Con respecto a enseñar, la vista no es tan importante. Hay muchas clases dictadas por maestros completamente ciegos, y tengo más que suficientes recursos para aprender el tema."

show lilly basic_smile_paj_close
with charachange

li "Es tan simple como eso, en verdad."

"Dejo caer mis hombros y resoplo una risa."

hi "Sí, entiendo. Supongo que ambos tendremos que trabajar duro para alcanzar nuestros objetivos, entonces."

stop music fadeout 4.0

show lilly basic_cheerful_paj_close
with charachange

li "Hmm…"

hi "¿Qué sucede?"

"Dudando un poco, Lilly adelanta su barbilla y cierra sus ojos en un gesto inconfundible."

scene ev lilly_kissing
with whiteout

play music music_one fadein 1.0

"Acepto encantado, nuestros labios encontrándose. Cuando lo hacen, de pronto siento sus manos recorriendo mi pecho por debajo de mi camisa."

"La sensación de su mano contra mi piel desnuda es suficiente para hacer que mi corazón de pronto acelere."

"¿Así que está con esos ánimos de nuevo?"

"Bueno, no es que me queje. A ella de verdad le gusta esto, y a pesar de todos mis medicamentos, mi libido por suerte sigue intacta."

"Me inclino más en el beso, sosteniendo con firmeza su mano mientras la siento trazar el contorno de mi pecho."

scene bg school_dormlilly
show lilly basic_smileclosed_paj_close:
    center
    ypos 1.1
with whiteout

"Eventualmente nos separamos el uno del otro, la habitación en silencio salvo por nuestra respiración."

show lilly basic_surprised_paj_close
with charachange

li "¿Oye, Hisao?"

hi "¿Sí?"

show lilly basic_emb_paj_close
with charachange

li "No podrías… ¿volver a ponerte las vendas?"

"Su tentativa sugerencia me toma por sorpresa."

"Supongo que también quiere enseñarme el sexo a través de sus ojos. O simplemente quiere averiguar si seré el mismo durante el acto estando obstruido por las vendas."

$ renpy.music.set_volume(0.5, 0.0, channel="music")


scene black
with softwipedown

"Con una medida de inquietud templada por la curiosidad, hago lo que me dice y bajo las vendas poniéndolas sobre mis ojos. El mundo vuelve a ser oscuridad."

"Me tenso por reflejo cuando siento la mano de Lilly rozar suavemente un costado de mi rostro, completamente incapaz de anticipar su toque."

"De verdad necesito acostumbrarme a este tipo de contacto. Incluso después de las semanas que hemos estado saliendo, no es tan natural para mí como lo es para ella."

"… ¿Silencio?"

hi "Oye, Lilly…"

li "Shh."

"Sigo obedientemente su instrucción y escucho en silencio, intentando distinguir algo, cualquier cosa, que esté sucediendo a mi alrededor."

"Comparado con antes cuando perseguía a Lilly, con la necesidad de desplazarme entre los obstáculos de la habitación ahora desaparecida, puedo tomarme mi tiempo y concentrarme mucho más en escuchar."

"Toma un tiempo, pero eventualmente logro distinguir el apagado sonido de su respiración en la habitación completamente silenciosa."

"Inhala… exhala… inhala… exhala…"

"Comparándola con mi propia respiración, me doy cuenta de que es definitivamente mucho más profunda de lo normal, especialmente para ella."

"Otro sonido se abre paso a mis oídos, uno que no puedo identificar de forma inmediata. No creo que lo haya oído antes, pero…"

"Mi corazón se detiene un instante cuando me doy cuenta del origen, mi mano casi por reflejo extendiéndose hacia ello. Su rostro se siente más suave de lo usual bajo mi tacto, su cabeza apenas girando en reconocimiento hacia los dedos en su mejilla."

li "Hisao…"

"Trago saliva y me tomo un momento para intentar calmarme. Necesito toda la concentración que pueda conseguir en esta situación para poder captar completamente mis alrededores."

"Luego de respirar un par de veces, creo que he logrado recobrar la calma. Con un toque tan ligero que no sería capaz de perturbar una pluma, comienzo a mover mi mano por su cuerpo."

"… Y puedo sentir cómo vuelvo a perder la concentración, gracias a esa delgada ropa de dormir de seda suya descansando de forma tan perfecta sobre las curvas de su cuerpo."

"Si ella está así, entonces eso significa que tiene que estar sentada contra su cama y encarándome. Ahora, para continuar."

"… De acuerdo, esta debe ser su cadera. Si simplemente me muevo lentamente hacia abajo…"

label es_L26h:

"La respiración de Lilly se detiene cuando mi mano se acerca a la de ella, siguiendo vacilantemente los dedos entre sus piernas a medida que entran por debajo de su ropa interior."

"Apenas la más mínima humedad toca mis dedos, pero es suficiente para adivinar fácilmente lo que está haciendo."

"Mi mente de pronto es invadida por visiones de cómo debe estar ella frente a mí en estos momentos. Nunca la había imaginado siquiera haciendo esto antes, y ser incapaz de verla en el acto no hace más que aumentar el ánimo."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

scene bg school_dormlilly
with softwipeup

"Levanto las vendas de mis ojos, sacando un par de pelos que estaban atascados en la cinta antes."

"Por un lapso de tiempo que solamente puedo aventurar, mi mente queda completamente en blanco. Lo único que puedo hacer es mirar mientras mis ojos ya libres abarcan todo lo que hay frente a ellos."

scene evh lilly_masturbate:
    truecenter
    subpixel True zoom 1.1
    acdc_warp 10.0 zoom 1.0
with flash

"Tal como había supuesto, Lilly está sentada frente a mí."

"Con una mano en el suelo para apoyarse, y los dedos de la otra rozando ligeramente su entrepierna, ocultos por su ropa interior azul oscuro, creo que es la imagen más erótica que jamás he visto."

"Una vez más extiendo mis manos y retiro su pelo de su rostro, su barbilla inclinada hacia afuera mientras llena su cuerpo envuelto de placer con otra bocanada de aire."

hi "Lilly…"

"Lilly se ve curiosamente adorable cuando sonríe al llamarla por su nombre. Siempre parece como si fuera en los momentos en los que está menos atenta cuando deja entrever sus emociones más interesantes."

"No pasa mucho tiempo antes de que ella comience a mover sus dedos más rápido que antes, su excitación en evidente aumento, y el aroma de su sudor en el aire reiterando ese hecho."

"Me siento frente a ella. No es como si mi propia excitación me mantuviera quieto; me está tomando cada fibra de mi ser dejarla continuar por su cuenta en lugar de abalanzarme sobre ella."

scene evh lilly_masturbate_come_face
with flash

"Es extraño… Al principio noté que sus nublados ojos azules me distraían, casi perturbadores por su falta de foco. Pero ahora eso me molesta mucho menos que antes."

"Al soltar ella un gemido mi atención vuelve a enfocarse en ella, su respiración mucho más rápida que antes y sus caderas meciéndose sutilmente."

scene evh lilly_masturbate_come
with flash

"Tan pronto como me doy cuenta de lo cerca que está Lilly del límite, su respiración se detiene. Sus ojos se cierran mientras que cada músculo en su cuerpo parece contraerse, y llegar inconfundiblemente a su clímax."

"Por solamente unos pocos segundos se tensa, acurrucada en éxtasis antes de que su cuerpo se relaje y un largo y exhausto suspiro se escape de sus labios."

scene bg school_dormlilly
with locationchange

"Yo… no tengo idea de qué decir. Reina el silencio mientras yo simplemente la observo, su cabello cubriendo su rostro mientras está ahí sentada."

show lilly basic_emb_paj_close:
    center
    ypos 1.1
with charaenter

li "Hisao…"

"Cuando ella extiende su mano para tocar mi rostro, mis deseos me arrebatan por completo el control de mi cuerpo. Sin siquiera pensarlo dos veces, me abalanzo sobre su figura."

"Es un sentimiento inusual, estar así. Me siento extrañamente poderoso, sosteniéndome a mí mismo sobre su rostro inexpresivo. Como si, por primera vez desde el accidente hace ya tanto tiempo, me sintiera físicamente fuerte."

hi "Lilly… Te deseo."

show lilly basic_weaksmile_paj_close
with charachange

"Para mi sorpresa, ella sonríe débilmente antes de extender su mano hacia arriba para sentir el costado de mi rostro. Es una expresión casi descarada, de las que usualmente tiene después de haber obtenido algo de mí."

hi "¿Tú… querías que hiciera esto?"

show lilly basic_smileclosed_paj_close
with charachange

"Ella mantiene su sonrisa y asiente en silencio. Supongo que fue una manera efectiva de hacerme tomar la iniciativa para variar."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene black
with softwipedown

"Y, nuevamente para mi sorpresa, ella le da a las vendas aún sobre mi cabeza un fuerte tirón hacia abajo. Una vez más, estoy sumido en la oscuridad completa."

li "Te dije… que las mantuvieras puestas… ¿no es así?"

"Ese dejo provocativo en la voz de Lilly, acentuado por su respiración… ella parece nunca perder su habilidad para tomar control de la situación."

"Pero esta vez… solamente esta vez…"

li "¿¡Ah, Hisao!? ¿Qué estás—?"

"Deslizo mi mano bajo ella, su suave piel y seda hundiéndose en mis manos al levantar gentilmente su cuerpo, con un grado de dificultad."

"Si bien no la describiría como pesada… su altura hace más complicado el intentar levantarla."

"Solamente toma un par de pasos cuidadosamente dados para sentir el borde de su cama contra mis piernas, y dejo a Lilly en sus sábanas tan gentilmente como cuando la levanté."



hi "¿Tu cama será más cómoda que el suelo, cierto?"

li "Siempre un caballero, ¿no?"

"Rápidamente paso mis manos por las curvilíneas y largas piernas de Lilly, su encanto lejos de verse disminuido sin el lujo de la visión, y saco su ropa interior y los shorts de su ropa de dormir de sus tobillos."

"No tengo idea de dónde habrán quedado…"

"Bueno, supongo que eso no importa. Deben estar por ahí."

"Con un mínimo de problemas, bajo mis propios pantalones de mi ropa de dormir y ropa interior, ubicándome entre sus piernas. O al menos, donde creo que es entre sus piernas."

"Con una mano en su cama para apoyarme, la derecha se mueve vacilantemente hacia abajo."

"Uh, ups. Mi primer contacto con ella es mi palma tocando torpemente la parte frontal de su nariz."

"Ella suelta una risita antes de girar su cabeza hacia un lado. Entendiendo la señal, dulcemente acuno su mejilla y uso mi pulgar para sentir los contornos de su rostro tal como lo hace ella conmigo."

"Esto sería mucho más fácil si ella no moviera su rostro hacia mi mano, pero la sensación de ella acariciándola es agradable."

"Trago e intento recuperar la calma, saco mi otra mano de la cama y la uso para guiarme hacia ella."

"Tan pronto como siento su calidez a mi alrededor, rápidamente me doy cuenta de lo excitado que estoy."

"Sin mi vista tengo la libertad para concentrarme mucho más en mis otros sentidos, incluyendo el tacto. Toda la experiencia se siente más nítida, más intensa que antes."

"Lentamente comienzo a mover mis caderas hacia atrás y hacia adelante, mi corazón latiendo desbocado de excitación."

"Siento los ojos de Lilly cerrarse con fuerza, el movimiento de sus mejillas bajo mi pulgar recordándome del agarre suave que tengo a un costado de su rostro."

"Es difícil evitar quedar por completo sobrepasado. Es difícil pensar que así es como se siente el sexo usualmente para ella, experimentado por todos los sentidos salvo aquel que más aprecio."

"Desde su mejilla a su cuello, comienzo a mover mi mano hacia abajo para abarcar la sensación de su cuerpo."

"El contorno de su clavícula… el ligero rocío posado en su piel…"

"Mi sentido del olfato es estimulado por el aroma de su transpiración y la mía en el aire. Incluso el olor del ambiente, notablemente distinto del de mi propia habitación, aporta a la sensación."

"Cuando muevo mi mano hacia sus blandos pechos, su débil gemido alcanza mis oídos, junto con el sonido de nuestro acto."

"La piel bajo mi mano se mueve hacia atrás y hacia adelante con cada movimiento, mi agarre sobre ella aumentando a medida que mi deseo por el cuerpo casi desnudo de Lilly ante mí crece."

"Hasta puedo sentir su pequeño pezón contra mi palma. Mi mano se desliza más aún y mis dedos lo pellizcan a través de la delgada seda del camisón de su ropa de dormir."

"Su gimoteo se transforma en gemidos a medida que es invadida por el mismo placer que yo. Puedo sentir mi corazón latir con fuerzas en mi pecho, y el latido de ella bajo mi mano."

"Puedo sentir sus manos afirmar mis muñecas, su agarre sorprendentemente firme mientras que su pecho se levanta por el sobrecogedor placer."

label es_L26x:

scene black
with dissolve

"Más… quiero más…"

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)

window show

"Puedo sentir mi pecho tensarse al mecerme frenéticamente hacia atrás y hacia adelante, ambos completamente extasiados."

$ renpy.music.set_volume(0.4, 0.5, channel="music")

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)

window show

"Nada… muy inusual… solo necesito respirar más profundo para recuperar… me…"

$ renpy.music.set_volume(0.3, 0.5, channel="music")

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)

with Pause(0.7)

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

window show

"Esta sensación es tan solo… normal…"

$ renpy.music.set_volume(0.2, 0.5, channel="music")

window hide

play sound sfx_heartfast
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

hi "Aah… aaaaaaaah…"

window hide

play sound sfx_heartfast
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

"Esto no es… no puedo… ¡este dolor es demasiado…!"

window hide

play sound sfx_heartstop
show heartattack alpha
with Dissolve (0.1)

stop music fadeout 0.3

show heartattack residual
with Dissolve (0.8)

window show

hi "¡AAAAARGH!"

with vpunch

"Caigo hacia atrás alejándome de Lilly con un indecoroso apuro, golpeando torpemente la parte de atrás de mi pie contra la mesa y cayendo al suelo con un impacto sin ceremonias."

"Respirando sin control, intento desesperadamente arrancar la cinta de mis ojos mientras yazco de espaldas. Tengo que sacarme esta cosa, tengo que sacarme esta cosa…"

scene white
with softwipeup

scene bg misc_ceiling
show heartattack residual
with locationchange

"Por un momento, todo queda en blanco. A medida que el torrente de la recién hallada luz asalta mis ojos, mi respiración baja luego de estar al borde de hiperventilarme."

window hide

$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_tragic fadein 4.0

hide heartattack
with Dissolve(3.0)

window show

"Pasan los segundos, y mido cuidadosamente el ritmo de mis latidos con cada fragmento de concentración que puedo reunir."

"Mi corazón está… normal. Ha vuelto a la normalidad."

"Mi cuerpo se siente completamente extraño mientras yazco aturdido en el piso mirando hacia el techo. La adrenalina de antes sigue corriendo por mis venas, pero mi mente está completamente agotada."

"Me apoyo sobre mis codos al oír que Lilly se baja de la cama y viene hacia mí."

show bg misc_ceiling_blur as bg2:
    center
    alpha 0.0
    linear 1.0 alpha 1.0
show lilly superclose_shock:
    xalign 0.5 yanchor 0.5 ypos 0.15 alpha 0.0
    subpixel True rotate 180
    easein 1.0 alpha 1.0 ypos 0.3
with Pause(1.0)

li "¿Hisao? ¿Estás bien? ¿¡Hisao!?"

hi "Estoy bien, Lilly. Estoy… bien."

show lilly superclose:
    xalign 0.5 yanchor 0.5 ypos 0.3 alpha 1.0
    subpixel True rotate 180
with charachange

"Ella suspira aliviada, su expresión de preocupación colapsando."

"El rostro que pone luego es el último que me hubiera gustado ver en ella. Es una expresión que detesté cuando la vi por primera vez en mis padres en el hospital hace ya tantos meses."

"Lástima. Lilly… siente lástima por mí."

scene black
with shuteye

"Simplemente cierro mis ojos y me doy vuelta, impotente. Siento ganas de vomitar."

play sound sfx_rustling

"Puedo escuchar el sonido de Lilly apartándose y arreglándose rápidamente, el sonido de su ropa volviendo a ser puesta luego de un momento de búsqueda apenas audible."

hi "Lo siento…"

scene bg school_dormlilly
show lilly basic_concerned_paj at center
with openeye

"Ella niega lentamente con su cabeza mientras termina de abrocharse la camisa. Su dulce sonrisa parece tan frágil, tan delicada, que hunde mi corazón."

show lilly basic_concerned_paj_close
with characlose

show lilly basic_concerned_paj_close:
    ypos 1.1
with charamove

"Acercándose con cuidado, ella tantea el borde de la mesita baja antes de sentarse junto a mí, poniendo sus brazos alrededor de mi pecho."

li "Lo lamento, Hisao. No debería haberte forzado a seguir mis deseos."

hi "No tienes que disculparte. Normalmente estaría bien, tú misma lo has visto antes."

hi "Supongo que no debería haber intentado esforzarme tanto."

"Mis párpados se sienten pesados. Estar sentado tranquilamente junto a ella de esta forma probablemente esté haciendo que la adrenalina abandone mi sistema, y haciendo que mi mente se relaje."

show lilly basic_oops_paj_close
with charachange

li "¿Entonces es por eso… que nunca tomabas la iniciativa…?"

hi "Sí. Supongo que es bueno que a ti te guste tomarla, ¿eh?"

show lilly basic_weaksmile_paj_close
with charachange

"La broma parece alegrar un poco su expresión, un hecho que me ayuda a sentir menos inquietud sobre mi poco confiable ser."

"La cabeza de Lilly se posa a descansar sobre mi hombro mientras que yo lucho por mantener mis ojos abiertos, con más dificultad luego de cada parpadeo. Me siento completamente agotado."

li "Está bien, Hisao. Todo está bien."

stop music fadeout 5.0

"Tan pronto como ella dice esto una melodía corta y tranquila se escapa de sus labios. Demasiado cansado para pensar, lo único que puedo hacer es escuchar su suave tarareo."

"Es una melodía calma, casi melancólica. Suena conocida, pero mientras más intento recordar su origen menos capaz de concentrarme parezco."

"La sensación y el olor de su cabeza descansando gentilmente sobre mi hombro y su cálido cuerpo contra el mío son relajantes. El suave tarareo de su voz también relaja mi mente tanto como su calidez relaja mis músculos."

"Este tranquilo y singular momento… luego de todo este tumulto me hace notar lo agotado que estoy. Puedo sentir mis párpados lentamente volverse más y más pesados."

"Aun con el caos de antes, desearía que este momento durara para siempre."

"Lilly y yo juntos, compartiendo un momento solitario juntos, tal como solíamos."

"Pero si ese es el caso… ¿por qué se siente… como si ella estuviera más lejos que nunca?"

scene black
with dissolve





label es_L27:

scene bg school_library
with locationchange

play sound sfx_doorslam
play music music_happiness fadein 2.0

"El sonoro tintineo de los libros cayendo en el buzón de retorno rompe abruptamente el silencio que impera en la biblioteca de la escuela."

"Se ha vuelto un hábito mío venir a la biblioteca al menos una vez a la semana. No solo el leer me mantiene ocupado, sino que además también lo hace el discutir sobre libros con Hanako y Lilly."

show yuuko panic_up at center
with charaenter

"Evidentemente asustada, Yuuko de pronto se da vuelta en dirección al ruido. Habría pensado que ya estaba acostumbrada a la gente dejando libros a estas alturas, ya que trabaja acá."

show yuuko neutral_down
with charachange

yu "Oh, hola Hisao. ¿De vuelta?"

"Me toma un momento responder, mi mente aún distraída por la conocida melodía tarareada por Lilly que no ha abandonado mis oídos en varios días desde que me quedé dormido escuchándola."

hi "¿Hmm? Oh, sí. Tan solo regreso unos libros que tomé prestados."

"Ella baja su mirada, presumiblemente hacia el receptáculo al cual cayeron los libros."

show yuuko closedhappy_down
with charachange

yu "Eres un lector asiduo, ¿no es así?"

hi "Se ha vuelto algo así como una rutina a estas alturas. Al menos, mata el tiempo."

show yuuko worried_up
with charachange

yu "Desearía tener tiempo libre para matar…"

"De charla a depresión en menos de cinco segundos. Creo que ese es un nuevo récord para ella. Parece un poco deprimida en general, aun comparada a lo normal."

"Considerando que tiene que trabajar en dos lugares para mantenerse, puedo entender cómo eso puede pasarle la cuenta a su estilo de vida."

"Ahora que lo pienso, la paga en su trabajo acá no puede ser tan mala. La idea de que el personal de una escuela privada tan prestigiosa pase hambre me suena ilógica."

hi "Trabajar en dos lugares debe quitar mucho tiempo. Yo probablemente nunca lo podría hacer."

show yuuko neutral_up
with charachange

yu "Tienes suerte, por ser estudiante. ¿Crees que serás capaz de ir a la universidad?"

"Si está preguntando, entonces supongo que ese es el resultado esperado de tener este tipo de educación. Las escuelas privadas como esta no salen precisamente baratas."

hi "Eso… creo. Tengo el dinero, creo."

hi "Tengo planes que requerirán ir a una, y mis notas son lo bastante buenas. Es más un tema de cómo lo pagaré."

show yuuko worried_down
with charachange

yu "La universidad cuesta tanto que tengo que trabajar en dos lugares para costeármela… pagar además los gastos de vida lo hace mucho más difícil."

show yuuko neutral_down
with charachange

yu "Pero si estás leyendo tanto, eso significa que estás bien con los estudios, ¿cierto?"

"Interesante conclusión. Pero no una del todo errada."

hi "Eso supongo. No encontré difíciles los exámenes, aparte quizás de uno o dos."

hi "¿Te molestaría si pregunto qué es lo que estudias en la universidad?"

show yuuko happy_up
with charachange

"Yuuko parece animarse sinceramente por la pregunta."

show yuuko closedhappy_up
with charachange

yu "Antropología. Para ser más específica, me estoy especializando en la historia de la civilización y democracia ateniense de la época clásica."

"Ella de verdad parece manejarse en el tema. Tal entusiasmo es admirable, y es bueno verla sinceramente emocionada por algo."

"Supongo que incluso alguien como Yuuko puede sentirse feliz si tiene su camino visible por delante."

hi "Es bueno oír eso. Si t—{w=0.6}{nw}"

stop music fadeout 0.5
play sound sfx_phone

show yuuko panic_up
with vpunch

"Ambos nos sobresaltamos ante la repentina interrupción proveniente de mi bolsillo."

scene bg school_hallway3
with locationchange

"Disculpándome notoriamente y dirigiéndome con rapidez hacia el pasillo mientras abro torpemente la cubierta de mi teléfono móvil, observo la pantalla."

"… Curioso. Es un número de móvil que no reconozco. Considerando que puedo contar el número de personas que tienen mi número con una mano, me pregunto por un rato si será algún vendedor telefónico con suerte."

scene bg school_hallway3_blurred
show phone mobile:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with locationchange
with Pause (0.5)

hi "Hola, Hisao Nakai al habla."

mystery "Cielos, contesta antes la próxima vez. De todas formas, ¿adivina quién?"

play music music_comedy fadein 1.0

"Solamente me toma un segundo reconocer esa distintiva voz grave y brusca."

hi "Hola, Misha. No esperaba que me llamaras."

aki "¿¡Eh!? ¿De verdad crees que sueno como ella?"

hi "Para nada, Akira. Pero no recuerdo haberte dado mi número, así que pensé en gastarte una broma."

aki "Oh, ¿eso? Hice que Lilly me lo diera. No fue difícil."

"Ella ciertamente reboza orgullo al decir eso. Está intentando hacer que me pierda en su ritmo, lo sé."

"Supongo que no debería estar sorprendido de que las dos compartan mi número, dado lo cercanas que son."

hi "Entonces, ¿qué pasa?"

aki "¿Estás libre ahora mismo?"

hi "Eso… creo. ¿Por qué?"

aki "¿Podrías encontarte conmigo en el parque que hay en el pueblo? Solo quiero hablar contigo sobre algunas cosas."

hi "¿Es eso una invitación a una cita?"

aki "¿Qué? Por supuesto que no…"

stop music fadeout 5.0

"Ella de pronto suena abatida, su provocación anterior desapareciendo en el acto. Parece extraño en ella."

hi "De todos modos, no veo por qué no. ¿Cuándo quieres que nos veamos?"

aki "Algo como… ahora. Algo así."

hi "Espera, ¿ahora mismo? Pero son—"

"El profundo silencio que sale del teléfono me anuncia el hecho de que ella ha cortado la comunicación sin ceremonias."

show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with None

scene bg school_hallway3
show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with locationchange
with Pause (0.5)

hide phone
with None

"Durante un buen rato me quedo ahí parado, mirando el mensaje de “LLAMADA TERMINADA” en la pantalla mientras repaso la conversación en mi cabeza."

hi "¿Qué demonios, Akira?"

scene bg suburb_park_ss
with shorttimeskip

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_parkambience fadein 2.0

"Echando un vistazo a ambos lados de la calle, cruzo el camino y entro al parque."

"He aprendido a llevar mi ritmo durante tales caminatas, principalmente debido a que el paso más lento de Lilly durante nuestros viajes al pueblo significa que tengo que ir más lento conscientemente."

"Dejando eso de lado, espero que Akira no esperara que me apareciera inmediatamente."

$ ksgallery_unlock("evul akira_park")
scene ev akira_park:
    subpixel True xalign 1.0 yalign 0.0 zoom 1.0
    acdc_warp 15.0 zoom 0.8
with whiteout

play music music_night

"Solamente me toma unos cuantos segundos encontrarla, esperando sentada en una banca con una lata de cerveza en mano."

"La mirada que tiene al verme caminar hacia ella carece de cualquier muestra de reconocimiento o saludo."

hi "¿Qué pasa con esa mirada? No tenía por qué venir, sabes."

aki "Sabía que lo harías. Eres de ese tipo de personas, después de todo."

scene bg suburb_park_ss
with locationchange

play sound sfx_can_clatter

"Frunzo el ceño por su comentario mientras ella se deshace de la lata, ya vacía para cuando llegué, y suena un repiqueteo metálico. Akira se sienta en la vieja banca de madera, y yo la imito."

play sound sfx_can

"Saca otra lata de cerveza de junto a ella y la abre antes de hablar, dando un gran sorbo. De verdad parece gustarle esa cosa."

hi "¿Supongo que no necesito preguntar de qué se trata todo esto, o mejor dicho, de quién se trata?"

show akira basic_resigned_close_ss at tworight
with charaenter

aki "Escuché de Lilly que preguntaste acerca de nuestra familia."

"Ellas comparten más que solamente números telefónicos, eso es seguro. Probablemente estaría muy preocupado ahora mismo si no fuera por la ausencia total de malicia en su voz. En cambio, su tono suena casi melancólico."

hi "Simple curiosidad, principalmente."

hi "… Debo admitir que nunca hubiera adivinado que ustedes dos eran mitad escocesas."

show akira basic_ending_close_ss
with charachange

"Ella suelta una risita socarrona."

show akira basic_smile_close_ss
with charachange

aki "He oído eso antes, créeme."

show akira basic_distant_close_ss
with charachange

"La ligera sonrisa se desprende de su rostro, sus ojos fijos en la distancia."

"Aparte de la ocasional pareja de ancianos hablando mientras andan lentamente por los caminos, y el extraño auto envejecido, está agradablemente callado."

show akira basic_lost_close_ss
with charachange

aki "Pero ella no te lo dijo todo, ¿o sí?"

hi "Fue bastante breve. Sus padres viven en Escocia, ella no los ha visto desde que tiene doce, y quiere volver a verlos."

show akira basic_annoyed_close_ss
with charachange

aki "Siempre me ha sorprendido lo dedicada que es a nuestros padres, a pesar de todo el bien que nos hicieron."

"La forma en que lo dice suena casi burlesca. Ella suelta un ligero suspiro, como para apartar rápidamente sus sentimientos."

show akira basic_resigned_close_ss
with charachange

aki "¿Por qué crees que se fueron, Hisao?"

hi "¿Por qué creo que se fueron?"

hi "Por lo que Lilly me dijo, fue por su trabajo. Supongo que también había de por medio un puesto con una paga decente, dada la forma en que sus padres parecen vivir."

hi "Entonces Lilly fue a una escuela privada, y es por eso que se comporta con la gracia y el aire de clase superior."

aki "Sí. Como el negocio en Inverness prosperó, nuestro padre decidió mudarse directamente a la misma ciudad donde estaba la casa matriz."

show akira basic_smile_close_ss
with charachange

aki "Pero esa es justamente la conclusión a la que pensé que llegarías. Tú eres demasiado buena persona."

hi "¿No crees que se hayan ido por su carrera?"

show akira basic_resigned_close_ss
with charachange

aki "Estoy sentada aquí quejándome contigo al respecto. ¿Qué crees?"

show akira basic_lost_close_ss
with charachange

aki "La Academia Yamaku. Siempre he sentido que ese lugar es un tanto raro; como si fuera un escondite aislado para aquellos que la “sociedad correcta” no quiere ver ni oír."

show akira basic_annoyed_close_ss
with charachange

aki "Ellos probablemente solo se lamenten el hecho de que Lilly no tuviera la edad suficiente para poder ser dejada ahí para cuando se fueron."

"Su abrupta y muy dura crítica a sus propios padres y de Yamaku es seguida por un largo silencio."

"La ceguera de Lilly difícilmente es algo que pueda ser ignorado por una familia de clase alta intentando mantener las apariencias, mucho menos cuando hay una oferta lucrativa sobre la mesa."

"Eventualmente Akira resopla socarronamente, sus sentimientos aflorando."

aki "Mudarse para asegurar nuestro futuro financiero con su nuevo cargo laboral. Incluso en su momento yo apenas pude creerlo."

"Sin querer ser solamente una vía para su descargo, intento sutilmente dirigir la discusión."

hi "¿Entonces permaneciste en Japón con Lilly?"

show akira basic_resigned_close_ss
with charachange

aki "O bien me quedaba con ella, o se iba a vivir con unos abuelos frágiles."

hi "¿Qué hay de la familia de Shizune? Si son primas, entonces…"

show akira basic_annoyed_close_ss
with charachange

aki "Nuestros padres se odian. Yo habría estado más que feliz de decirles que se jodieran y vivir con ellos de todas formas, pero Lilly no hubiera querido eso."

show akira basic_resigned_close_ss
with charachange

aki "Además también tenía una oferta de trabajo por aquel entonces, así que hicimos lo posible para mantener la casa de nuestros padres en condiciones, e intentamos continuar con nuestras vidas como si ellos nunca se hubieran marchado."

hi "¿Entonces simplemente vivieron por su cuenta?"

show akira basic_lost_close_ss
with charachange

aki "Básicamente. Lilly tenía la escuela y yo mi trabajo, así que no estábamos precisamente languideciendo."

aki "Con su educación, su estudio, y el tener que hacer las cosas del hogar mientras yo trabajaba, no puedo evitar sentir que le he fallado. Al final, intenté estar ahí para ella, y lo arruiné."

show akira basic_annoyed_close_ss
with charachange

aki "… Esperar que una chica de diecinueve sea madre de una niña ciega. Es ridículo."

"Entonces… Lilly y Akira vivieron solas luego de que sus padres se mudaron, Lilly cuidando de sí misma. Supongo que eso explica su aparente independencia, comparada a muchos otros en Yamaku."

"Puede que yo haya vivido solo durante gran parte del tiempo ya que mis padres trabajaban, pero eso… es algo completamente distinto."

show akira basic_resigned_close_ss
with charachange

aki "Lo siento por hacerte escuchar mis quejas, Hisao."

hi "No me molesta, pero… ¿te importaría si pregunto por qué me estás diciendo todo esto?"

show akira basic_smile_close_ss
with charachange

aki "Hmph. Siempre has sido curioso."

show akira basic_distant_close_ss
with charachange

aki "Contexto, supongo."

aki "La vida no es un cuento de hadas, Hisao. Algunos tienen que aprender esto de la manera difícil."

"Le da un largo sorbo a la lata en su mano, su rostro mostrando más depresión que distancia."

stop music fadeout 2.0

show akira basic_resigned_close_ss
with charachange

aki "Terminé con mi novio hace unos cuantos días. Cuando me vaya, no vamos a poder volvernos a ver."

aki "Pero así es la vida. No puedes simplemente preparar tu vida y esperar que permanezca de esa forma para siempre; a veces pasan cosas que tienes que soportar, aun si eso significa herirte a ti mismo o a otros."

"Ella da un largo respiro antes de levantar la mirada al cielo anaranjado."

show akira basic_distant_close_ss
with charachange

aki "Maldición… si fumara, podría darle una larga calada ahora mismo y verme algo genial."

"Quiero responder, para ayudarla en lo que pueda, pero me siento completamente inútil. Este tipo de situaciones es de las que nunca he vivido, y simplemente no tengo la experiencia para decir algo significativo para reconfortarla."

"Akira mira hacia mí y evidentemente se da cuenta de esto, para mi vergüenza."

show akira basic_lost_close_ss
with charachange

aki "Debo verme bastante patética en estos momentos, quejándome de esto con alguien que apenas conozco."

hi "Apenas, y yo soy prácticamente un experto en verme patético."

show akira basic_ending_close_ss
with charachange

"Ella suelta una risa, un acto que se siente como una victoria personal para mí."

show akira basic_smile_close_ss
with charachange

aki "Eres un buen chico, Hisao. Cuando dije que estaba de acuerdo con que estuvieras con mi hermana, no estaba bromeando o simplemente siendo simpática."

show akira basic_smile_ss:
    tworight
    ypos 1.1
    ease 0.5 ypos 1.0
with charadistant

play sound sfx_can_clatter

"Ella se levanta de su asiento con un gruñido, uno que parece inapropiado dada su edad, y arroja la lata ahora vacía en el basurero luego de dar un último sorbo."

show akira basic_boo_ss at tworight
with charachange

aki "Solo que es desafortunado que eso en realidad no cuente mucho en este mundo."

show akira basic_resigned_ss
with charachange

aki "Cuando dije que me iba a Escocia, lo hacía porque se abrió una vacante en la casa matriz de la compañía."

aki "Pero cuando nuestros padres me dijeron eso cuando estábamos en su hogar, también le dieron a Lilly la orden de volver con ellos a Inverness."

play music music_sadness fadein 0.5

"No puede ser…"

"Sus evasivas cuando le pregunté sobre su futuro… aquella incomodidad que poco a poco ha aparecido entre nosotros… ese arrebato de ira tan poco característico de ella…"

"Todo eso de pronto tiene sentido."

"La misma familia que ella recordaba después de la fiesta de cumpleaños de Hanako, la misma familia que las dejó a ella y a Akira a su suerte para marcharse a pastos más verdes…"

"Ahora me siento estúpido por nunca arrinconar a Lilly para saber lo que le estaba molestando. Ni siquiera consideré si algo había pasado durante ese viaje a la casa de su familia en Inverness."

"Y ahora, una sensación de inseguridad crece en mi pecho. Si su familia la ha llamado para que vuelva con ellos a Escocia, al otro lado de la Tierra…"

hi "¿Ella ha… aceptado?"

show akira basic_lost_ss
with charachange

aki "Lilly no me ha dicho si piensa aceptar, y parece que tampoco te lo ha dicho a ti."

aki "Es por eso que te llamé aquí para hablar, Hisao."

hi "Contexto, eh…"

"Me apoyo en la silla, mis sentimientos de preocupación y frustración sin duda marcados por todo mi rostro."

show akira basic_resigned_ss
with charachange

aki "Lilly es una persona fuerte, Hisao, pero no es infalible."

aki "Supongo que es mi trabajo preocuparme por ella, al ser la hermana mayor, pero creo que mereces saberlo."

hi "Entiendo."

show akira basic_lost_ss
with charachange

aki "¿Estás bien? Suenas deprimido."

hi "No, solo estoy… pensando."

show akira basic_ending_ss
with charachange

aki "Eso es bueno. Pensar es bueno. Ser impulsivo no te llevará a nada."

show akira basic_boo_ss
with charachange

"Ella mira su reloj, apenas moviendo su muñeca."

show akira basic_lost_ss
with charachange

aki "Tengo que irme. ¿Estarás bien?"

hi "Estaré bien, no te preocupes. Tendré que hablar con Lilly al respecto y arreglar todo."

show akira basic_smile_ss
with charachange

"Ella pone una sonrisa, pero no se siente tan genuina o sincera."

"En verdad, ambos estamos rodeando el hecho de que Lilly se encuentra sobre el precipicio de la decisión más grande de su vida y está intentando llevar toda la carga ella sola."

"Y parte de esa carga es el asunto de nuestra relación."

stop music fadeout 5.0
hide akira
with charaexit

"Para cuando alzo la mirada, Akira ya está caminando con su mano en alto."

"Por primera vez en mucho tiempo, al fin tengo una respuesta a algo. Quizás ni siquiera eso. Pero al menos ahora tengo la pregunta correcta para hacer."

"“¿Te irás o te quedarás?”."

stop ambient fadeout 2.0

scene black
with dissolve




label es_L28:

scene bg suburb_roadcenter_rn
show rain normal
with locationchange

play ambient sfx_rain fadein 4.0

hi "¡Apúrate, Lilly!"

show lilly basic_concerned_cas_close_rn behind rain at center
with charaenter

li "¡Voy tan rápido como puedo!"

"Apenas puedo distinguir la voz de Lilly por sobre el ensordecedor golpeteo de la lluvia. A pesar de que me desagrada llevarla a rastras, la situación lo requiere."

"Me doy vuelta hacia el frente, mi mano libre sobre mi cabeza en un esfuerzo inútil por mantener al menos mi cabello seco."

"Mi visión parece haberse vuelto en grises. Este clima de verdad es horrendo para ser verano, y el último tipo de clima en el que me gustaría tener una cita."

"Una lástima. Incluso revisé el pronóstico del clima de antemano, una de las pocas veces que lo he hecho, para que al final dijera que este domingo por la tarde estaría bien."

"Mirando a Lilly, sus hombros ya están completamente mojados, su mano derecha sujetando firmemente la mía y su mano izquierda afirmando su bastón retraído."

"Este horrendo aguacero llegó justo cuando estábamos en camino entre nuestro destino y Yamaku, así que decidimos intentar apresurarnos el resto de la distancia en lugar de dar vuelta."

"Sin estar para nada acostumbrada a correr así de rápido, Lilly está usando toda su concentración para evitar tropezarse."

show lilly basic_oops_cas_close_rn
with charachange

li "¿¡Hisao, sabes adónde vamos!?"

"Incluso queda reducida a gritar e intentar ser escuchada por sobre el ruido combinado del viento y la lluvia."

hi "El Sha—"

"El resto de mi voz es completamente opacada por una ráfaga incluso más fuerte de lluvia."

show lilly basic_sad_cas_close_rn
with charachange

li "¿¡El qué!?"

hi "¡El Shanghái!"

show lilly basic_concerned_cas_close_rn
with charachange

li "¿¡Qué tan lejos está!?"

hi "¡Ya no debería estar lejos!"

show bg suburb_shanghaiext_rn
show lilly basic_concerned_cas_close_rn
with shorttimeskip

"No toma mucho tiempo antes de volver a llamarla."

hi "¡Parece que estamos a salvo, está un poco más adelante!"

"Rápidamente me detengo justo frente al familiar exterior, la linterna afuera todavía entregando su confiable brillo, y espero a que Lilly recupere su aliento antes de entrar."

hi "Las damas primero."

play sound sfx_storebell

show lilly basic_smileclosed_cas_close_rn at center
with charachange

with Pause(0.5)

hide lilly
with charaexit

"La pequeña campana adentro suena cuando sostengo la puerta abierta para ella, recibiendo una sonrisa y un gesto educado de recompensa antes de seguirla."

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
play music music_dreamy fadein 3.0

scene bg suburb_shanghaiint
show lilly basic_smileclosed_cas at center
with locationchange

"Al entrar tras ella y limpiar mis pies, basta solo una rápida mirada para notar la clara falta de actividad. El Shanghái no parece recibir mucha clientela, y hoy no es la excepción. Solo hay ocupadas un par de mesas."

"Llamada por el sonido de la campana, una persona esperada viene a recibirnos."

show bg suburb_shanghaiint at bgleft
show lilly basic_smileclosed_cas at twoleft
with charamove

show yuukoshang happy_up at tworight
with charaenter

yu "¡Bienvenidos al Shanghái!"

"Yuuko se ve alegre hoy. Intentar predecir su ánimo es bastante difícil, pero es un buen cambio con respecto a lo normal."

show lilly basic_smile_cas
with charachange

li "Hola, Yuuko."

hi "Buenas."

show yuukoshang closedhappy_down
with charachange

yu "Buenas tardes a los dos."

show yuukoshang neutral_down:
    ypos 1.25
with Dissolvemove(0.2)

with Pause(0.2)

show yuukoshang neutral_down at tworight
with charamove

"Ella hace una reverencia, pillada algo desprevenida una vez que se endereza y nos ve con más detenimiento."

show yuukoshang worried_down
with charachange

yu "¿Qué les pasó? Ambos se ven…"

"Sus ojos se mueven hacia el vidrio de la puerta tras nosotros."

show yuukoshang panic_up
with charachange

yu "Oh. Oh cielos."

hi "Ahora estamos adentro, por lo menos. Creo que eso es lo más importante."

show lilly basic_weaksmile_cas
with charachange

li "Es agradable y acogedor. Tienes suerte de trabajar adentro hoy."

show yuukoshang smile_down
with charachange

yu "Ha estado bastante tranquilo. Me gustan los días como este."

show yuukoshang worried_down
with charachange

yu "Oh esperen, um, lo lamento… ¿quieren algo?"

show lilly basic_smile_cas
with charachange

li "Té de vainilla francés, por favor."

hi "Yo tomaré lo mismo."

show yuukoshang closedhappy_up
with charachange

yu "Bien. Viene enseguida."

hide yuukoshang
with charaexit

"Ella rápidamente se escabulle con una expresión de determinación en su rostro, intentando con ganas no olvidar nuestra orden. Por lo menos, sin duda es entregada a su trabajo."

show bg suburb_shanghaiint at center
show lilly basic_smileclosed_cas_close at center
with dissolvecharamove

show lilly basic_smileclosed_cas_close:
    ypos 1.1
with charamove

"Llevo a Lilly a un asiento vacío antes de sentarnos. Como siempre, hay una gran diferencia entre mi caer exhausto a mi asiento y el delicado desliz de Lilly al de ella, su bastón a su lado."

"Por un rato simplemente miro caer la lluvia afuera. Una persona ocasionalmente corre calle abajo intentando permanecer tan seca como sea posible, sus manos a menudo afirmando con fuerza un paraguas empapado."

"Lilly está sentada tan en silencio como yo, sus ojos cerrados mientras escucha con atención todo lo que está pasando."

"Es un silencio cómodo y relajante que existe entre nosotros; del mismo tipo de los que a menudo compartimos juntos en los meses pasados."

stop music fadeout 5.0

"Para Lilly, al menos."

"No puedo evitar escuchar las palabras de su hermana en mi mente, a veces contrastándolas con nuestro tiempo juntos desde que llegué a Yamaku, y a la forma en que nos hemos llevado desde que comenzamos a salir juntos."

"Sin importar lo mucho que lo intente, no logro entender a Lilly. Es como si mientras más me empeñara en adivinar sus emociones y su decisión potencial, más difícil se volviera llegar a una conclusión clara."

"Me hace dudar de si en verdad la he entendido. Al final, voy a tener que preguntar, aunque realmente quisiera evitar hacerlo."

show lilly basic_smile_cas_close
with charachange

li "Te ves callado hoy, Hisao."

hi "¿De verdad?"

show lilly basic_ara_cas_close
with charachange

li "Parecías tan entusiasmado por tener una cita conmigo, que pensé que había algo en específico que querías hacer."

hi "No, en realidad no. Solamente quería pasar algo de tiempo contigo."

show lilly basic_weaksmile_cas_close
with charachange

li "¿Es eso cierto…?"

hi "Bien. Había una cosa más."

show lilly basic_cheerful_cas_close
with charachange

"Una ligera sonrisa se abre paso hasta el rostro de Lilly, sabiendo muy bien que me ha ganado. Eso hace que lo que quiero decir sea aún más incómodo."

hi "Es solo que… Akira y yo estuvimos hablando."

show lilly basic_surprised_cas_close
with charachange

li "¿Oh?"

hi "¿Por qué ese tono?"

show lilly basic_weaksmile_cas_close
with charachange

li "Ustedes dos parecen llevarse bien, ¿o no?"

hi "Bueno, sí pienso que es una persona bastante genial con la cual hablar. Sería agradable si alguno de los maestros se pareciera en algo a ella."

show lilly basic_sleepy_cas_close
with charachange

li "“Genial”…"

"Por un momento intento reconocer el tono de su voz, mi boca doblándose en una sonrisa cuando lo hago."

hi "No estarás celosa, ¿o sí?"

show lilly basic_pout_cas_close
with charachange

li "¡No estoy celosa!"

"Luego de haberme molestado por tal cosa en nuestra primera cita, no me siento tan mal por divertirme un poco a sus expensas en esta ocasión."

"Pero mientras calmarnos, esto no es más que una distracción menor del verdadero motivo por el cual traje a Lilly aquí."

hi "No te preocupes, fue más que nada plática normal. Dicho sea eso, hubo algo que Akira mencionó de lo que quería hablar contigo."

hi "Cuando fueron a ver a tu familia en Inverness hace poco, ella dijo…"

show lilly basic_reminisce_cas_close
with charachange

li "Akira te contó sobre el llamado de mi familia, ¿no es así?"

play music music_drama fadein 2.0

"Los segundos pasan mientras intento leer la expresión de Lilly, una extraña mezcla de sentimientos escrita en ella. Parece molesta, pero también algo confundida."

show bg suburb_shanghaiint at bgleft
show lilly basic_reminisce_cas_close:
    twoleft
    ypos 1.1
with charamove

show yuukoshang neutral_up at tworight
with charaenter

yu "Um… aquí…"

"Yuuko deja vacilantemente nuestras bebidas sobre la mesa, su presencia extrañamente pequeña."

hide yuukoshang
with charaexit

show bg suburb_shanghaiint at center
show lilly basic_reminisce_cas_close:
    center
    ypos 1.1
with charamove

"Cuando ella regresa hacia el mostrador luego de una breve reverencia, me doy cuenta de que el ambiente entre Lilly y yo está denso y las expresiones de ambos están algo pensativas."

show lilly basic_displeased_cas_close
with charachange

li "A pesar de decirme que debería manejar mi propia vida, de todas maneras interfiere en los peores momentos…"

hi "No creo que debas culpar a Akira por esto. Ella tan solo está cuidando de ti, y no es como si yo no pudiera entender su preocupación con respecto a esto."

show lilly basic_weaksmile_cas_close
with charachange

"La irritación de Lilly abre paso a un incómodo, y mayormente infructuoso, intento de ocultar sus sentimientos. Ella de verdad no maneja bien el ser acorralada con temas personales."

li "Lo sé, pero… solamente quería algo más de tiempo. Sabía que lo adivinarías eventualmente, pero…"

hi "¿Me estabas ocultando esto intencionalmente? ¿Por cuánto tiempo planeabas hacerlo?"

show lilly basic_displeased_cas_close
with charachange

li "Como dije, solo quería más tiempo para pensarlo bien. Quería estar segura de mi decisión antes de decírtela."

hi "¿Y qué decidiste, al final?"

"Sé qué es lo que quiero que diga, pero una horrenda sensación se niega a desaparecer de mis entrañas."

show lilly basic_sleepy_cas_close
with charachange

li "Mi familia en verdad quiere que regrese con ellos, y Akira también se irá. Todavía podría dedicarme a enseñar como carrera, ya sea aquí o allá."

hi "Entonces… te vas."

hi "¿Desde hace cuánto lo sabes? Ya sé que te lo preguntaron cuando fuiste a Escocia por primera vez, hace un mes."

show lilly basic_concerned_cas_close
with charachange

li "Desde hace… algún tiempo."

"Mi frustración prácticamente revienta. El hecho de que ella haya hecho esto me afecta más de lo que debería."

"No solo porque ella se marche sino además por haber estado ocultando activamente sus propios planes, y después de parecer por tanto tiempo el único pilar de apoyo y confiabilidad sólido en el cual podía contar…"

"Se siente como si los cimientos bajo mis pies de pronto cambiaran dramáticamente, mucho más rápido de lo que puedo adaptarme. Quizás esto no es tanto frustración sino más bien inquietud."

hi "Lilly…"

show lilly basic_sad_cas_close
with charachange

li "Lo siento, yo solamente… quería pensar esto por completo. No estaba intentando aprovecharme de ti, por favor—"

hi "Lo sé, Lilly. Lo sé. Es solo que esto es demasiado repentino."

hi "¿Creo que esto significa que una vez que te vayas, terminamos?"

"Por una de las pocas veces que la he visto desde que la conocí, ella ha perdido realmente el habla."

"No parece sorprendida, sin lugar a dudas porque ha caído en cuenta de este hecho en cuanto tomó su decisión, pero por otra parte, ella parece realmente insegura de cómo tratar con la situación ahora que esta se encuentra frente a ella."

show lilly basic_oops_cas_close
with charachange

li "P-podríamos intentar continuar una relación a distancia. Se están volviendo más y más comunes en estos días, después de todo…"

"Incluso mientras lo dice, el tono de su voz delata que en realidad no cree en lo que está diciendo."

$ renpy.music.set_volume(0.5, 1.0, channel="music")
$ renpy.music.set_volume(0.05, 1.0, channel="ambient")

window hide
nvl clear
nvl show dissolve

n "\n\n\nLilly es demasiado anticuada como para ser capaz de lidiar con una relación sin ningún tipo de presencia física, e incluso yo también lo soy, hasta cierto punto. Lo único que podríamos ser para el otro sería una voz al otro lado del mundo."

n "Al final, intentar racionalizar todo es inútil. Cualquier intento de conectar lo que está pasando con el futuro o el pasado tan solo parece volverse más difícil mientras más me concentro."

n "Esos tranquilos momentos cuando simplemente caminábamos uno junto al otro, el precioso tiempo que pasamos con Hanako y Akira, las pláticas casuales que teníamos durante el almuerzo, las veces que hicimos el amor, las confesiones de nuestros sentimientos hacia el otro…"

n "\n\n\nTodo en vano. Todo simplemente un momento pasajero de nuestras jóvenes vidas."

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear
window show

hi "Somos tan solo dos niños pretendiendo ser adultos, ¿no es así?"

show lilly basic_sad_cas_close
with charachange

"Un largo, largo silencio queda en el aire entre nosotros. El ruido de los otros comensales bebiendo y hablando solamente hace que la situación se sienta más extraña y disjunta."

"El rostro de Lilly permanece bajo, su expresión abatida nublándolo."

stop music fadeout 4.0

show lilly basic_concerned_cas_close
with charachange

li "Lo siento, Hisao."

"Una simple disculpa, y nada más. Ella queda sin ningún tipo de respuesta o comentario adicional."

"Con un largo suspiro, reúno lo que queda de mi pensamiento y hago la pregunta final que tengo para ella."

hi "¿Cuándo te marchas?"

show lilly basic_sad_cas_close
with charachange

li "Me iré con Akira, así que será en poco menos de una semana."

hi "¿Al comienzo de las vacaciones de verano?"

show lilly basic_sleepy_cas_close
with charachange

li "Un poco después, sí."

"Su tono es inusualmente lento y firme, su ánimo deprimido y pesaroso más notorio en su rostro mientras más intenta ocultarlo en su voz."

"Al final, ni siquiera puedo mantener mi promesa de ir a Tanabata con ella antes de que se marche."

stop ambient fadeout 14.0
$ ksgallery_unlock("evul hisao_teacup")
show ev hisao_teacup:
    truecenter
    zoom 0.85 subpixel True
    acdc_warp 15.0 zoom 0.8
with locationchange

"Bajo la mirada, y veo mi rostro reflejado en la ahora tibia taza de té ignorado frente a mí."

"De verdad creí haber dejado este tipo de expresiones atrás."

"Por un rato simplemente miro la superficie quieta, intentando ordenar mis emociones para tratar de descubrir qué camino debería tomar, ya sea ahora mismo o en un futuro."

"Pero, al igual que antes, el esfuerzo es inútil."

hide ev
show lilly basic_reminisce_cas_close
with locationchange

"Levanto la mirada para ver a Lilly bebiendo con gentileza su té enfriado sin quejarse, su rostro encogido y sus hombros caídos."

"Ella parece estar también perdida en sus pensamientos, un ambiente extrañamente frío apareciendo entre los dos a medida que nos aislamos para meditar las cosas."

"Incluso mientras la taza de Lilly es vaciada lentamente, la mía permanece sin tocar."

"Pasa un largo rato antes de notar que la lluvia está amainando afuera y que los demás comensales del Shanghái ya se han ido."

scene bg school_dormhallway
with shorttimeskip

stop ambient
play music music_moonlight fadein 0.5

"El frío de la tarde oscureciendo rápidamente penetra el pasillo de los dormitorios. Mientras camino decaído por el pasillo hacia mi cuarto, veo un movimiento no deseado adelante."

show kenji happy:
    center
    xpos 0.4
    easein 0.5 xpos 0.5
with charaenter

"Para variar, el abrir de la puerta opuesta a la mía anuncia la llegada de un Kenji anteojudo."

ke "Hola hombre, qué…"

show kenji tsun at center
with charachange

ke "Vaya hombre, te ves horrible, creo. ¿Estás bien?"

"Él de verdad tiene un don para mejorar cualquier situación."

hi "En… realidad no quiero entrar en detalles. Es tarde."

show kenji neutral
with charachange

ke "De acuerdo. Está bien."

ke "Si alguna vez quieres hablar al respecto, tú sabes, estoy aquí."

"Lo miro por un momento antes de dejar de lado mi expresión severa y rascarme incómodo la parte de atrás del cuello, avergonzado por mi respuesta confrontacional."

hi "Gracias, Kenji."

show kenji happy
with charachange

ke "Oye, está bien. Para eso están los amigos, ¿cierto?"

hi "Claro, tienes razón. Um, nos vemos."

scene bg school_dormhisao_ni
with locationchange

"Abro la puerta de mi propio dormitorio y la cierro detrás de mí mientras que él rápidamente se despide."

play sound sfx_doorslam

"El sólido sonido que la puerta hace al chocar contra el marco hace un último llamado a la vida que he tenido desde que llegué a Yamaku."

"Simplemente me quedo de pie en mi habitación oscurecida, intentando infructuosamente pensar en qué debería hacer de este punto en adelante."

"¿Tan solo qué debería hacer…?"

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
stop music fadeout 2.0

scene black
with dissolve



label es_L29:

scene bg school_scienceroom
with locationchange

"Cuando la clase termina, simplemente dejo descansar mi cabeza sobre mi mano y miro por la ventana para pasar el tiempo."

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_normal fadein 2.0

window hide
nvl clear
nvl show dissolve

n "\n\nHan pasado algunos días desde que Lilly me contó sus planes. No he ido a nuestro lugar de almuerzo de siempre desde entonces, no es como si tuviera mucho sentido."

n "Hanako ha estado ocupada con el club de periodismo al cual se ha unido hace poco, y ha comenzado a hablar en clases con Naomi de vez en cuando."

n "Incluso Lilly, además del hecho de que encontrarnos sería extraño en cualquier caso, ha estado completamente atareada con sus deberes de representante de su clase a medida que se acercan las vacaciones de verano."

n "Y ahora, ya están prácticamente aquí. Cuando termine de sonar la campana de hoy, las vacaciones de verano habrán comenzado."

n "\n\n\nSupongo que lo único que haré será visitar a mis padres y vagar en mi antiguo hogar, ahora que mis planes anteriores están por completo descarriados."

nvl clear

n "\n\nMientras tanto, Akira y Lilly estarán en camino a Escocia, para vivir ahí el resto de sus vidas."

n "Sin importar lo mucho que intente racionalizar la idea de que una vez que comiencen las vacaciones de verano, mi vida regresará a como era antes, esto simplemente se niega a suceder."

n "Todos están siguiendo con sus vidas. Lilly se reencontrará con su familia, Akira está avanzando en el negocio de su padre, Hanako está consiguiendo nuevos amigos y pasatiempos, e incluso Yuuko sigue adelante con sus aspiraciones universitarias."

n "Incluso yo sigo adelante, al final. Con las calificaciones que he obtenido hasta ahora en Yamaku, en especial luego de un comienzo tan complicado, el camino para enseñar ciencias como profesión parece sencillo."

n "\n\nSupongo que al menos debería estar feliz por ese hecho, pero en realidad no parece ayudar."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

window show

mi "¡Hicchan~!"

"Rápidamente detengo mi reflexión y me doy vuelta para encarar la voz vivaz junto a mí, colocando la expresión más animada que puedo hacer."

show misha hips_smile at twoleft
show shizu behind_smile at tworight
with charaenter

"Como esperaba, Shizune está parada a un lado. Tengo la ligera sospecha de que quieren algo de mi parte."

hi "Hola Misha, Shizune. ¿Qué sucede?"

show misha hips_grin
with charachange

mi "Bueno~…"

show misha perky_smile
with charachange

mi "Shicchan y yo estábamos pensando~…"

show misha sign_smile
with charachange

mi "Como somos solamente dos pobres niñas pequeñas que necesitan ayuda con todo el trabajo que nos han dado justo antes de que comiencen las vacaciones~…"

hi "Claro, puedo ayudar."

show misha perky_sad
with charachange

mi "Pero Hicchan, en verdad neces—"

stop music fadeout 0.2

show misha perky_confused
with charachange

mi "¿Qué?"

"Creo que rompí a Misha."

show shizu behind_blank
with charachange

"Incluso Shizune alza las cejas ante el estremecimiento de su cómplice detenida de improviso."

show misha hips_grin
with charachange

mi "¿Entonces nos ayudarás, Hicchan?"

hi "Acabo de decir que lo haría, ¿no?"

"No es como si tuviera algo mejor que hacer. Quizás ayudarlas con su trabajo me ayudará a distraerme de la situación."

"Misha parece sinceramente eufórica por mi respuesta, pero la expresión de Shizune es nebulosa y difícil de leer."

"Me encuentro a mí mismo apartando rápidamente mis ojos de los de ella, ya que casi parece una expresión de lástima. Sin duda, debe ser simplemente mi imaginación."

scene bg school_council
with shorttimeskip

play music music_daily fadein 0.5

"Esta es difícilmente la primera vez que he estado en el salón del consejo estudiantil."

"En efecto, terminé viniendo aquí a menudo, ya sea para ayudar a Lilly con su trabajo de representante de clase, o para tratar alguna u otra cosa con el consejo estudiantil mismo."

"Ahora, sin embargo, es un lugar bastante distinto."

show sc_comp:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"Hay papeles y carpetas desparramados por todas las mesas del salón, y solo una pequeña y solitaria portátil negra encima de un escritorio separado del desastre."

"Parece claramente antiguo, y supongo que ha estado sirviendo valientemente en su tarea de archivar información durante años y años."

show sc_comp:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide sc_comp
with None

hi "Entonces, ¿qué hay que hacer? Esto parece mucho por hacer."

show misha hips_smile at twoleft
show shizu behind_frown at tworight
with charaenter

shi "…"

"La expresión de Shizune se vuelve determinada a medida que hace gestos. Es una expresión preocupante."

show misha hips_grin
with charachange

mi "¡Todo, Hicchan!"

"Mi preocupación estaba bien fundada."

hi "¿Todo… dices?"

show shizu basic_normal
with charachange

shi "…"

show misha sign_smile
with charachange

mi "Lo que queda sobre los escritorios es lo que hay que hacer."

show misha perky_smile
with charachange

mi "Todo tiene que ser grabado digitalmente, lo cual es la función de la portátil."

hi "¿Y supongo que yo seré el que hará esto?"

show shizu behind_smile
with charachange

shi "…"

show misha hips_smile
with charachange

mi "Shicchan dijo que te vio con las computadoras en la biblioteca hace unos cuantos días, y que parecías ser bastante bueno con ellas~."

"¿Bueno con las computadoras? Puedo escribir con el tacto, supongo, pero aun así parece una sobreestimación de mis habilidades."

hi "Solo estaba transcribiendo tareas…"

hi "Espera, ¿Shizune estaba viéndome hacer eso?"

show shizu adjust_smug
with charachange

shi "…"

show misha sign_smile
with charachange

mi "Uno debe conocer a sus aliados antes de poder conocer a sus enemigos, por supuesto~."

show misha cross_grin
with charachange

mi "Vaya, eso es bastante sabio…"

"En esta ocasión, no es difícil distinguir quién dijo qué."

"De todas formas, no parece valer la pena discutir por eso. Estar sentado frente a una computadora escribiendo apenas parece oneroso, en lo que respecta a tareas para ayudar a Shizune y Misha."

show shizu basic_normal
with charachange

shi "…"

show misha perky_smile
with charachange

mi "Además, te ayudará a distraerte de las cosas~."

hi "¿Distraerme de las cosas? ¿Distraerme de cuáles cosas?"

show misha perky_confused
with charachange

"El rostro de Misha queda en blanco mientras le traduce esto a Shizune, si bien la respuesta de esta última es simplemente una mirada rápida hacia la ventana luego de hacer brevemente unas señas."

show shizu behind_blank
with charachange

shi "…"

show misha sign_smile
with charachange

show shizu basic_normal2
with charachange

"El rostro de Misha rápidamente recupera su sonrisa mientras traduce. Ella estaba confundida, supongo, pero Shizune es más difícil de leer."

show misha cross_smile
with charachange

mi "Simplemente pensaba que te podría gustar despejar tu mente de los exámenes, por supuesto~."

hi "De cualquier forma, bien podríamos ponernos a trabajar antes y no después. Seguiré con su juego."

show misha hips_smile
with charachange

mi "¡Ese es el espíritu, Hicchan~!"




















scene bg school_council
with shorttimeskip

"Y esa es la quinta hoja de datos compilada y guardada. Le toca a la del mes siguiente…"

"Luego de un rato de armar revuelo, todos logramos organizarnos un poco."

"Shizune ha estado juntando las hojas sueltas y, afortunadamente, ordenándolas en una pequeña pila a mi lado."

"Mientras tanto, Misha se ha estado encargando de escribir a mano, su femenino bolígrafo rosa dejando su inconfundible marca en papel tras papel."

"Una vez que le tomé el ritmo, esto en verdad no fue tan malo. Shizune y Misha también parecen tener el control de todo, comunicándose sin palabras mientras hacen sus tareas con dedicación."

"Constantemente miro la hoja junto a la computadora, aparentemente una lista de estudiantes y sus respectivas direcciones, mientras ingreso obedientemente los datos escritos en ella."

"No le pongo mucha atención a lo que estoy escribiendo hasta que llego a la mitad de la página."

"Hakamichi… grupo 3-3… Eh. Su familia vive en Saitama."

"Mi vaga curiosidad acaba abruptamente al escuchar tres golpes ligeros sobre la puerta."

show misha perky_smile:
    twoleft
    xpos 0.4
    easein 0.5 twoleft
with charaenter

"Misha rápidamente se levanta para ver quién es, tocando a Shizune en el hombro de paso para darle a entender lo que está pasando."

show misha hips_grin at twoleft
with charachange

mi "Ah, estás aquí~."

hi "¿Hmm? ¿Quién es?"

"Con una breve pausa para ingresar los datos de Shizune en el archivo junto con los demás, levanto la mirada para ver quién está en la puerta."

stop music fadeout 0.5

show lilly invis:
    left
    xpos -0.2
with None

show bg school_council at bgright
show misha hips_grin at center
show lilly basic_weaksmile_cas at left
with dissolvecharamove

"… ¿Lilly?"

"Luego de inclinar brevemente su cabeza para saludar a Misha, ella levanta su cabeza de modo habitual."

show lilly basic_surprised_cas
with charachange

li "¿Ese es Hisao?"

"Ella es increíblemente buena distinguiendo mi voz a partir de las frases más pequeñas hoy en día."

hi "Sí, soy yo. Um… hola."

show lilly basic_reminisce_cas
with charachange

"El ambiente se siente un poco incómodo cuando hace una reverencia. Ninguno de los dos sabe bien qué tan íntimos deberíamos ser con el otro, dado que ella se va en cuestión de horas."

"Este es un hecho que, afortunadamente, ni la distraída de Misha ni la esforzada Shizune notan."

hi "Entonces… ¿también tienes trabajo que hacer?"

show lilly basic_sleepy_cas
with charachange

li "Desafortunadamente. Llegué apenas pude, pero mi grupo me detuvo con una fiesta de despedida sorpresa, y tenía que cambiarme de ropa."

"Bajo la mirada hacia el reloj de la computadora. Ya prácticamente ha terminado la hora del almuerzo, así que supongo que Lilly logró escaparse del último periodo también."

show lilly basic_weaksmile_cas
with charachange

li "¿Asumo que Shizune también está aquí?"

play music music_shizune fadein 3.0

show shizu behind_blank at right
with charaenter

shi "…"

show misha cross_smile
with charachange

mi "¡Por supuesto!"

show shizu adjust_smug at right
with charachange

shi "…"

show misha sign_smile
with charachange

mi "¡Y además he estado aquí durante todo el almuerzo!"

"Ese último comentario en realidad no era necesario. Shizune está provocando a Lilly para tener otra pelea, puedo sentirlo."

show lilly basic_displeased_cas
with charachange

li "Lo lamento por no poder ser tan trabajadora como tú, Shizune. Me empeñaré en contratar más lacayos para que hagan mi trabajo en el futuro, te lo aseguro."

"Y Lilly se acaba de tragar la carnada, complicando más las cosas."

show shizu basic_frown
with charachange

shi "…"

show misha hips_frown
with charachange

mi "¿Pero no eres tú la que siempre le deja el trabajo a sus compañeros~?"

show lilly basic_listen_cas
with charachange

li "La diferencia es que ellos deciden ayudar por su cuenta, no como en tu tiránico control sobre tu propio grupo."

show shizu behind_frown
with charachange

shi "…"

show misha cross_smile
with charachange

mi "¡La tiranía funciona~! Aun si hicimos las cosas de forma distinta, de todas maneras obtuvimos los mismos resultados, ¿cierto~?"

show lilly basic_displeased_cas
with charachange

li "Esto es una escuela, no un estado policial. Tendrás que recordarme cuándo te nombraron monarca del grupo, me temo."

show shizu cross_angry
with charachange

shi "…"

show misha cross_frown
with charachange

mi "¡Uno debe arrebatar el poder, no es tan bueno si simplemente se te es concedido~! Pero creo que tú en verdad no entenderías eso, ¿cierto~?"

show shizu adjust_angry
with charachange

shi "…"

show misha hips_smile
with charachange

mi "También tendrás que recordarme cuándo se eligieron monarcas para sus cargos~."

"Lilly claramente se enfurece al oír esto. La combinación uno-dos de Shizune la deja a la defensiva."

show lilly basic_displeased_cas
with charachange

li "Y sin embargo con todo tu aclamado poder, no puedes hacer que una persona te ayude sin tener que forzarla."

show shizu behind_frustrated
with charachange

shi "…"

show misha sign_smile
with charachange

mi "¡Pero Hisao se ofreció~! Es tan esforzado, que está haciendo esto en lugar de socialización sin sentido, ¿cierto~?"

show lilly basic_listen_cas
with charachange

li "¿Eso es cierto, Hisao?"

"Ah, esto no es bueno. En verdad he acabado entre la espada y la pared."

"Por mucho que me duela hacer esto, la verdad por lo menos tiene la posibilidad de detener esta discusión aquí y ahora."

hi "Está bien, Lilly, ellas no me acosaron para que viniera ni nada."

show lilly basic_displeased_cas
with charachange

"Lilly pone una expresión de descontento, irradiando en silencio su fuerte sentimiento de desagrado en mi dirección general."

"Puede ser bastante aterradora cuando quiere serlo, aunque afortunadamente no pasa a menudo."

show shizu cross_angry
with charachange

shi "…"

show misha hips_frown
with charachange

mi "Hicchan, lo haces sonar como si fuera algo habitual~…"

hi "¿No lo es?"

hi "Al fin y al cabo, eso no importa mientras todo esté haciéndose a buen ritmo. Acabemos pronto con este trabajo para poder irnos a casa."

hide shizu
with charaexit

hide lilly
with charaexit

hide misha
with charaexit

"Shizune resopla de forma burlona y continúa marcando las hojas frente a ella, mientras que Lilly suspira y se abre camino por la habitación con su mano siguiendo los gabinetes alineados junto a la pared."

"Esta sería la única vez que he logrado apaciguar con éxito una de estas situaciones, pero la tregua a regañadientes hecha a base de miedo y respeto mutuo hace que esto se sienta más como una guerra fría que una paz verdadera."

"Pero no puedo llevarme todo el crédito; la partida de Lilly seguramente ha afectado a Shizune de algún modo, para hacer que desista tan fácilmente."

show bg school_council at center
with charamove

show lilly basic_listen_cas at center
with charaenter

"Momentos luego de volver al trabajo, noto que Lilly está extendiendo sus brazos para agarrar algo de encima de uno de los gabinetes. Casi ofrezco mi ayuda, pero su altura le da una gran capacidad para bajarlo de forma segura."

show lilly basic_displeased_cas:
    ypos 1.15
with dissolvecharamove

"Una vez que deja el extraño artefacto en un escritorio junto a mí, me doy cuenta de lo que es… algo así… mientras ella saca la vieja cubierta verde y se sienta."

show brailler:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"A primera vista parece ser una vieja máquina de escribir azul metálica, pero no me toma mucho darme cuenta de que está lejos de lo común."

"Tiene muchas menos teclas de lo esperado, y las que tiene no presentan letras sobre ellas. Solamente las sombras dibujadas por los pequeños puntos de braille dan una pista de su propósito."

hi "¿Máquina de escribir para ciegos?"

show lilly basic_smile_cas
with None

show brailler:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide brailler
with None

li "¿Oh, esto? Bueno, no andas lejos."

li "Normalmente se les llama máquina Perkins, pero es básicamente una máquina de escribir para ciegos, sí. Forma braille en la página en lugar de texto, por lo que tiene menos teclas."

hi "Eh… eso es bastante genial."

show lilly basic_cheerful_cas
with charachange

"Ella suelta una sonrisa cálida debido a mi curiosidad. Tengo que admitir que atrae mi gusto por lo novedoso."

hide lilly
with charaexit

"Sin más que añadir, cada uno sigue con la tarea asignada. El sonoro traqueteo de las piezas mecánicas de la máquina de braille de Lilly y el golpeteo del viejo y gastado teclado de la portátil rápidamente se hacen sentir en el cuarto."

"Es un ambiente agradable, en verdad. Todos saben lo que tienen que hacer, y Lilly y yo podemos sentarnos uno junto al otro e intercambiar palabras de vez en cuando mientras trabajamos."

"Nostálgico. Así es como se siente."

"Es agradable, pero se ve un poco mancillado por saber que nuestro tiempo juntos está por terminar."

show lilly basic_smile_cas:
    center
    ypos 1.15
with charaenter

li "¿Disculpa, Misha?"

show bg school_council at bgleft
show lilly basic_smile_cas:
    twoleft
    ypos 1.15
with charamove

show misha hips_smile at tworight
with charaenter

"Para dirigirse adecuadamente a ella, Misha salta desde los gabinetes cuyo contenido está examinando, a pesar de la falta de visión de Lilly. Por un momento pienso que es extraño, pero luego me doy cuenta de que es exactamente lo que yo hago."

mi "¿Qué sucede?"

show lilly basic_weaksmile_cas
with charachange

li "¿Podrías preguntarle a Shizune dónde están los registros de asistencia del grupo 3-2? Creo que los han cambiado de lugar."

show misha hips_grin
with charachange

mi "¡Okie dokie!"

hide misha
with charaexit

stop music fadeout 8.0

"Y con eso, ella parte revoloteando hacia Shizune, quien está trabajando en una mesa detrás de nosotros."

"La familiaridad de Lilly con el salón del consejo, y la eficiencia con la que trabaja, me recuerdan que ella, Misha y Shizune solían trabajar todas juntas en el consejo estudiantil."

"Quizás este sea un final apropiado para su estadía en Yamaku; trabajando tal como solía hacerlo, rodeada por aquellos a quienes ella ama y, al menos, quiso."

"Levanto la mirada, tomado por sorpresa al ver a Shizune buscando en una gaveta, y no a Misha."

show shizu behind_blank at tworight
with charaenter

"En efecto, ella saca una carpeta de cartulina, completamente en blanco salvo por unos puntos apenas visibles al frente, y la sostiene frente a Lilly."

"La mano de Lilly tantea para verificar qué es, sus dedos tocando los puntos de braille y confirmando que es lo que pidió."

show lilly basic_smile_cas
with charachange

li "Gracias, Misha."

"No hay respuesta."

show shizu behind_smile
with charachange

"No hay respuesta, claro, exceptuando por una extraña mueca… no… sonrisa… en el rostro de Shizune."

show ev lilly_sheets:
    truecenter
    zoom 1.05 subpixel True
    easein 10.0 zoom 1.0
with whiteout

"Pasan unos cuantos segundos antes de que Lilly caiga en cuenta de que no es Misha quien está detrás de ella, sino Shizune. Su momentánea expresión de sorpresa es reemplazada por una sonrisa un poco tímida."

"Por unos momentos, el cuarto queda por completo quieto y silencioso."

"Sin embargo, eventualmente Shizune vuelve a su lugar de trabajo y Lilly comienza a escribir una vez más."

"Solo duró unos cuantos segundos, pero se siente como si hubieran sido años de comunicación recuperada en aquel silencioso intercambio."

scene bg school_council_ss at right
with shorttimeskip

play music music_tranquil fadein 3.0

hi "Ahí, terminé."

"Inclino mi cabeza hacia atrás y froto mis ojos para intentar quitarles su cansancio. Mirar esa pequeña y bastante mala pantalla se llevó su cuenta."

show lilly basic_smile_cas_ss:
    center
    ypos 1.15
with charaenter

li "Excelente sincronización; lo único que queda por hacer es archivar estas cosas y también habré terminado con mi trabajo."

hi "Bien. Puedo guardar la máquina de braille y apartarla mientras tú haces eso."

show lilly basic_smileclosed_cas_ss
with charachange

li "Gracias, Hisao."

hi "Misha, ¿a ti y a Shizune les queda mucho por terminar?"

"Las busco a mi alrededor mientras repongo la cubierta de la máquina de braille, solo para verlas esperando en la puerta. Supongo que deben estar esperándonos."

scene bg school_council_ss at left
show misha hips_smile_ss at center
show shizu behind_blank_ss at right
show lilly basic_smileclosed_cas_ss at left
with shorttimeskip

"Con un mínimo de tiempo perdido, archivamos y guardamos todo lo que queda y nos unimos a ellas."

hi "Gracias a ambas por esperarnos."

show misha hips_grin_ss
with charachange

mi "¡No podíamos irnos sin ti, Hicchan, has sido de gran ayuda!"

show shizu behind_smile_ss
with charachange

"Shizune asiente afirmativamente, satisfecha con mi trabajo."

hi "Supongo… que eso es lo último del trabajo de representante de clase hecho, entonces."

show lilly basic_smile_cas_ss
with charachange

li "Así es."

show misha perky_sad_ss
with charachange

mi "Te extrañaré, Lilly. Pienso que fue divertido trabajar contigo."

show lilly basic_weaksmile_cas_ss
with charachange

li "Gracias, Misha. Ha sido bueno trabajar contigo… y con Shizune."

show shizu basic_normal_ss
with charachange

"Shizune piensa por un instante antes de formular su respuesta. No es que a menudo se comunique sin pensar, al contrario, pero esta vez lo considera aún más de lo normal."

show shizu adjust_smug_ss
with charachange

shi "…"

show misha perky_confused_ss
with charachange

"Misha parece un poco sorprendida antes de pasar el mensaje."

show misha hips_smile_ss
with charachange

mi "Shizune dice… que más te vale que hagas tu trabajo allá mejor que lo hacías aquí."

show lilly basic_giggle_cas_ss
with charachange

"Lejos de sentirse ofendida, Lilly tapa una risita con su mano."

show lilly basic_smileclosed_cas_ss
with charachange

li "Si ese es el caso, entonces por favor dile a Shizune que en el futuro sea más comprensiva con los que aún están aquí."

"Competitiva hasta el final. Quizás Shizune y Lilly no son tan diferentes después de todo."

show shizu behind_smile_ss
with charachange

shi "…"

show misha hips_grin_ss
with charachange

mi "Shicchan dice que estará vigilando para asegurarse de que cumplas con tu parte de la promesa."

show lilly basic_cheerful_cas_ss
with charachange

li "Entonces así es como será."

show lilly basic_smile_cas_ss
with charachange

li "Es mejor que parta, entonces. Adiós, Shizune. Adiós, Misha."

show lilly basic_smileclosed_cas_close_ss
with characlose

li "¿Hisao?"

"Lilly afirma mi brazo con los de ella, la necesidad de un bastón inexistente si yo estoy aquí para guiarla. Asintiendo en despedida a ellas dos, salimos por la puerta y nos dirigimos hacia el patio de la escuela."

"Cuando me doy vuelta para despedirme de ellas, noto la mirada de Shizune aún fija en Lilly. Podrán molestarse entre ellas, pero los lazos familiares no se rompen tan fácilmente."

scene bg school_courtyard_ss
with locationskip

hi "¿Ya tienes todos tus papeles en orden entonces?"

show lilly basic_smileclosed_cas_ss at center
with charaenter

li "Si, ya los he llenado y entregado todos."

hi "Como siempre tienes todo bajo control, ¿no es así?"

show lilly basic_weaksmile_cas_ss
with charachange

stop music fadeout 4.0

"Ella sonríe con sinceridad debido al cumplido, pero se siente como si su felicidad fuera solamente una tapa del hecho de que está plenamente consciente de todo lo que está dejando atrás."

"Me recuerda a cómo solía ser cuando la conocí; siempre sonriendo, siempre un poco distante, siempre un poco apartada de todos."

"Incluso ahora, ella aún mantiene aquel aire alrededor de varios, especialmente aquellos a quienes no es cercana. Tenía la esperanza de que nuestro tiempo juntos hubiera cambiado ese hecho."

scene bg school_gardens_ss
with locationchange

"Nuestro paso disminuye, deteniéndonos ambos en los ya vacíos jardines de la escuela."

show lilly basic_weaksmile_cas_ss at center
with charaenter

li "¿Hisao? ¿Sucede…?"

play music music_comfort

show lilly basic_surprised_cas_close_ss
with vpunch

"Las palabras de Lilly son interrumpidas al darme vuelta y rodearla con mis brazos, acercando sus caderas."

"Puede que usualmente no sea dado a actos tan impulsivos, pero tan solo quiero estar cerca de ella, incluso si esta es la última vez que podré hacerlo."

"Todos los demás estudiantes han regresado a sus dormitorios y hogares, y solo el susurro de las hojas con la brisa genera sonido alguno."

show ev lilly_touch_cas
with charachange

"Cuando retrocedo, puedo ver que ella se ha deshecho de su bien cuidada sonrisa."

"Su mano vacila, sin querer dejar o permanecer en mis facciones."

"Está haciéndose la valiente, pero su ligero temblor la delata. Lilly podrá ser capaz de controlarse bien, pero ni siquiera ella puede mantener la compostura en este momento."

"Esta es la mujer que he llegado a amar, pero también aquella que en muy poco tiempo se irá del país para siempre."

li "Lo siento, Hisao."

hi "Está bien. Tienes que dirigir tu propia vida, después de todo."

scene bg school_girlsdormhall
with shorttimeskip

"Caminamos por el pasillo del dormitorio de las chicas tomados de la mano, nuestras emociones ya aplacadas en gran medida. Sin embargo, nuestras manos sostienen la del otro mucho más firmemente que antes."

"Se pueden oír voces débiles y amortiguadas provenientes de la habitación de Lilly, sus orígenes no muy difíciles de adivinar."

scene bg school_dormlilly

show hanako invis at tworight
show lilly invis at twoleft
with locationchange

show lilly basic_weaksmile_cas at twoleft
show hanako emb_downsad:
    xpos 0.4 xanchor 0.5
with dissolvecharamove

show lilly basic_surprised_cas
with vpunch

"En el momento en que ella abre la puerta, Hanako la atraviesa apresurada y rodea con sus brazos a Lilly, tomándola muy obviamente por sorpresa."

ha "¡Lilly! ¡Lilly!"

show lilly basic_oops_cas
with charachange

li "¿Ha-Hanako…?"

show hanako emb_downtimid
with charachange

ha "Voy a extrañarte… Lilly…"

show lilly basic_weaksmile_cas
with charachange

"Como era de esperarse, está al borde del llanto. Lilly amablemente frota el cabello de Hanako con su mano en respuesta, y luego se separa y pone una cálida y reconfortante sonrisa."

show akira invis:
    right
    ypos 1.15
with None

show akira basic_lost at right
with dissolvecharamove

"Más allá de Hanako, puede verse a Akira levantándose del costado de la cama de Lilly y rascando su cabeza."

show akira basic_smile
with charachange

"Sus ojos se apartan de Lilly y Hanako hacia mí, con una sonrisa débil y amortiguada en su rostro. Intento devolver una expresión de felicidad más sincera, pero el resultado probablemente es el mismo."

show akira basic_boo
with charachange

aki "Entonces, ¿está todo listo? ¿Lograste contenerte de matar a Shizune?"

show lilly basic_giggle_cas
with charachange

"El comentario saca una risita divertida de su hermana."

li "Sí, lo tengo todo en orden, y sí, logre no hacerlo. ¿Has empacado todo lo que necesitas?"

show akira basic_smile
with charachange

aki "Tengo los dos bolsos aquí mismo, pero aún quedan algunas cosas en la casa de los Hakamichi. Pero puedo buscar eso mientras esperamos allá el vuelo de mañana en la tarde."

"Akira le da unas fuertes palmadas a dos grandes maletas negras en el suelo. Probablemente vino a ayudar a empacar y asegurarse de que todo estuviera en orden del lado de Lilly, antes de irse con ella."

show hanako cover_worry at center
with dissolvecharamove

ha "¿Lilly… estarás bien… allá?"

show lilly basic_smileclosed_cas
with charachange

li "Estaré bien, te lo aseguro. Akira cuidará de mí también, y tú sabes que ella es confiable."

show hanako basic_worry
with charachange

ha "Pero…"

show lilly basic_smile_cas
with charachange

li "No te preocupes, Hanako. Después de todo tengo tu número de teléfono, así que podemos permanecer en contacto. Con la ayuda de Akira, podría enviarte cosas por internet."

show akira basic_boo
with charachange

aki "Oye, no me uses solo porque no quieres aprender a usar una computadora."

show lilly basic_giggle_cas
show hanako basic_smile
with charachange

"Hanako y Lilly se ríen brevemente, el ambiente animándose aunque sea un poco."

show lilly basic_smileclosed_cas
with charachange

li "Pero eso también va para ti, Hisao. Prometo que te contactaré una vez que llegue a Escocia."

hi "Lo sé. Lo esperaré con ansias."

"Su oferta puede ser amable, pero ambos sabemos que esto es equivalente a terminar. Ninguno de los dos tiene expectativas con respecto a lo bien que podríamos mantener una relación de larga distancia."

"Sin palabra que nos impulse, los cuatro comenzamos la larga y solemne caminata hacia el portón de la escuela."

scene bg school_gate_ni at bgleft
with shorttimeskip

"Las numerosas lámparas dispersas alrededor de los terrenos de Yamaku no logran hacer mucho más que dar puntos de luz en una, de otra forma, densa oscuridad."

"Un auto estacionado en el camino frente a los terrenos de la escuela se hace visible, su exterior negro brillante reflejando las tenues luces de Yamaku. Le hablo a Akira intentando aliviar un poco el pesado ambiente."

hi "¿Ese es tu auto? ¿De qué tipo es?"

show akira basic_smile_ni at center
with charaenter

aki "¿No sabes mucho sobre automóviles, no es así? Es un Lancer Evo. Sólido y veloz."

"Bueno, no es como si su comentario sobre mi conocimiento esté lejos de la realidad. Nunca me han llamado la atención."

show akira basic_resigned_ni
with charachange

"Ella suelta un pequeño suspiro."

show akira basic_lost_ni
with charachange

aki "Se ha portado bien. Lástima que deba separarme de él mañana, igual que de la casa de verano. Ustedes fueron los últimos en visitarla antes de que cambiara de manos."

"Alejándome de mi bastante pobre intento de conversación, miro de reojo a Hanako y a Lilly, siguiéndonos más atrás."

show akira basic_lost_ni at tworight
show bg school_gate_ni at center
with charamove

show hanako emb_downtimid_ni:
    xpos 0.4 xanchor 0.5
show lilly basic_weaksmile_cas_ni at twoleft
with charaenter

"Por lógica, Hanako debería estar conduciendo a Lilly, pero definitivamente sucede lo contrario al estar ella firmemente aferrada al brazo de Lilly."

"Es una imagen deprimente."

show akira basic_resigned_ni
with charachange

aki "Entonces… supongo que esto es todo."

show lilly basic_reminisce_cas_ni
with charachange

li "Así es."

"Si bien el momento para que todos nos despidamos es ahora, en realidad nadie quiere dar el primer paso. Es como si mientras más durara el silencio, más probable fuera que ellas simplemente no se marcharan."

show hanako emb_downsad_ni
with charachange

ha "Lilly… ¿de verdad te tienes que ir?"

show lilly basic_concerned_cas_ni
with charachange

li "Lo siento, Hanako. Pero no te dejaré para siempre; aún puedo llamarte. Hisao seguirá estando aquí también."

"Asiento, pero Hanako simplemente se aferra más al brazo de Lilly."

"Luego de pasar tanto tiempo sin tener a quién llamar familia, debe ser terrible tener que decir adiós a la persona que fue tan cercana a una madre como alguien podría haber sido en su vida."

show lilly basic_sad_cas_ni
with charachange

"Lilly suelta un largo y triste suspiro. Todo lo que Akira y yo realmente podemos hacer es estar de pie en silencio en los márgenes, ya que la única persona que puede resolver esto es la propia Lilly."

"Eventualmente, Lilly saca su brazo del agarre de Hanako y sostiene sus hombros amablemente, una forma mucho más decisiva de tratarla de lo que alguna vez haya visto de Lilly."

show lilly basic_reminisce_cas_ni
with charachange

li "Hanako, ¿recuerdas cuando nos conocimos?"

show lilly basic_weaksmile_cas_ni
with charachange

li "Cuando entraste a mi habitación por primera vez luego de escucharme consolar a una amiga, no dijiste ni una palabra en toda la noche. Incluso mientras te servía té y te hablaba, tú te sentaste en silencio y simplemente escuchaste lo que decía."

li "Hicieron falta varias reuniones en silencio como aquella antes de que comenzaras a abrirte a mí, pero cuando comenzaste a hacerlo, sentí algunos de los momentos más felices que he sentido."

show lilly basic_sleepy_cas_ni
with charachange

li "No me volví tu amiga porque sintiera lástima por ti, Hanako. Me volví tu amiga porque sabía que tú te escondías no solo de mí, sino de todos."

li "Tus ambiciones, personalidad, intereses, gustos… Yo no sabía nada de ellos, y tampoco los conocía nadie más."

show lilly basic_weaksmile_cas_ni
with charachange

li "Pero mientras te mostrabas a mí, comencé a darme cuenta del tipo de persona que eras, y me sentí segura de que nuestro encuentro fue un momento muy especial."

show hanako emb_blushtimid_ni
with charachange

ha "Pero yo…"

"Lilly interrumpe sus palabras mientras lleva sus manos al rostro de Hanako y mueve sus flequillos a un lado, poniendo suavemente sus labios en la frente de Hanako."

show lilly basic_smile_cas_ni
with charachange

"Cuando retira su cabeza, dejando a Hanako sin palabras y con ojos húmedos, Lilly suelta una amplia sonrisa."

li "Creo que eres una persona muy hermosa, Hanako, y estoy segura de que te volverás una mujer fuerte y segura."

li "Eres una amiga muy querida, y alguien a quien amo mucho. Al igual que Hisao, nunca me olvidaré de ti mientras viva."

show lilly basic_smileclosed_cas_ni
with charachange

li "Podré irme, pero tú tienes una vida propia que llevar. Tal como yo los tengo, tú tienes tus propios amigos y pasatiempos, y tus propios sueños para después de la graduación. Quiero que te dediques a ellos, aun después cuando yo ya no esté."

show lilly basic_smile_cas_ni
with charachange

li "Es por eso que creo que estarás bien. Porque eres tu propia persona, y con tu propia vida. Tú misma me demostraste eso."

show hanako emb_downtimid_ni
with charachange

"Hanako baja su cabeza avergonzada, pero asiente mientras lo hace."

ha "E… Entiendo…"

ha "Sé que tengo que decir adiós… Sé que tienes que tomar tu propio camino…"

show hanako emb_smile_ni
with charachange

ha "Pero… gracias, Lilly. Por todo."

show lilly basic_reminisce_cas_ni
with charachange

li "Gracias, Hanako. ¿Estarás bien?"

"Pasan unos cuantos segundos de silencio antes de que llegue la respuesta."

show hanako cover_smile_ni
with charachange

ha "Lo estaré."

show lilly basic_smile_cas_ni
with charachange

"Lilly sonríe, sin duda alguna en parte por alivio."

show lilly basic_smileclosed_cas_ni
with charachange

li "Eso me hace muy feliz, entonces. Adiós."

show hanako basic_bashful_ni
with charachange

ha "Adiós… Lilly."

show lilly basic_weaksmile_cas_ni
with charachange

li "Y adiós a ti también, Hisao."

hi "Adiós. Te extrañaré."

show lilly basic_weaksmile_cas_close_ni
with characlose

"Ella se detiene un momento antes de caminar hacia mí. Su mano derecha, extendida frente a ella, sostiene mi hombro."

"Su mano izquierda lenta y grácilmente se extiende hacia mi rostro, conteniendo mi mejilla en su palma."

show lilly basic_smile_cas_close_ni
with charachange

"Por un rato simplemente sostiene mi rostro, sus dedos apenas moviéndose para sentir su contorno. Usualmente su mano se sentiría cálida al hacer tal cosa, pero el aire nocturno le ha dado a su piel un toque fresco."

"No estoy seguro de cuánto tiempo permanecemos así, sus ojos nublados apuntando justo por debajo de los míos mientras me sonríe de forma melancólica, casi distante. Pero, eventualmente, tomo su fría mano con la mía."

"Es difícil hacerlo, pero con un ligero suspiro retiro suavemente su mano de mi mejilla."

hi "Espero que tengas una vida larga y feliz, Lilly, vayas donde vayas."

show lilly basic_weaksmile_cas_close_ni
with charachange

li "Gracias. Me aseguraré de tenerla."

"Ella respira una vez de forma extensa y temblorosa antes de voltear un poco en dirección a Akira."

show lilly back_sad_cas_close_ni at twoleft
with charachange

li "Akira…"

show akira basic_lost_ni
with charachange

aki "De acuerdo."

show hanako basic_bashful_ni at left
show lilly back_sad_cas_ni at center
show bg school_gate_ni at right
with dissolvecharamove

"Asintiendo, toma la mano de Lilly y comienza a guiarla hacia el auto estacionado afuera de las puertas. Ambas caminan lentamente y deliberadamente, como si sus movimientos hubieran sido ensayados de antemano."

"Es extraño sentirse así ahora, ver a alguien irse de Yamaku. La sensación de inquietud que siento ahora me recuerda a la primera vez que pasé por aquellos portónes negros de hierro fundido, que siempre parecieron demasiado pomposos para lo que eran."

"Al marcharse ellas, todos nosotros sabemos muy bien que nuestras vidas están cambiando de forma irreversible. Siempre me he dicho a mí mismo que tan solo tengo que tomar la vida como llega, pero todo está cambiando tan rápido, tan de pronto."

"Al final, Lilly es una parte irremplazable de las vidas de Hanako y mía."

"El sonido de Akira abriendo la puerta de pasajeros para Lilly me saca de mis pensamientos, despidiéndose con la mano mientras Lilly entra."

show akira basic_smile_ni
with charachange

aki "¡Nos vemos chicos! ¡Cuídense!"

show lilly basic_weaksmile_cas_ni
with charachange

li "¡Adiós Hanako, adiós Hisao!"

show hanako cover_smile_ni
with charachange

"La mano de Hanako rápidamente se alza, su rostro iluminado por su entusiasta despedida."

ha "¡Adiós Lilly! ¡Adiós!"

hi "¡Nos vemos, Akira, y adiós Lilly!"

hide lilly
hide akira
with charaexit

"La puerta se cierra mientras todos ponemos nuestro mejor rostro de despedida feliz, Akira entrando al auto y encendiendo el motor de forma expedita."

"La mano de Lilly apenas puede verse despidiéndose a través de las ventanas polarizadas, las manos de nosotros dos también en alto."

"Tal como las otras veces que he hecho tal cosa, no puedo distinguir precisamente por qué yo, o Hanako, nos despedimos con la mano dado que ella nunca nos verá hacerlo. Pero no importa."

"Incluso mientras ese brillante auto negro va colina abajo y desaparece en la noche oscura, seguimos despidiéndonos con la mano de Akira y Lilly."

stop music fadeout 5.0

"Y luego… se han ido."

show bg school_gate_ni at center
show hanako basic_normal_ni at center
with dissolvecharamove

"Una extraña quietud se materializa cuando nuestras manos regresan a nuestros costados."

"No sé exactamente qué debería hacer o cómo debería sentirme. Al final, simplemente nos quedamos ahí en silencio mirando hacia donde el auto desapareció de nuestra vista."

ha "Adiós… Lilly."

show hanako basic_normal_close_ni
with characlose

"Todo lo que puedo hacer en respuesta a su tranquila y lastimosa despedida es colocar una mano sobre sus hombros."

show hanako basic_distant_close_ni
with charachange

"Ella me mira durante algunos momentos antes de volver a mirar colina abajo, segura al saber que sigo aquí para ella."

"Lo que haremos de ahora en adelante no parece del todo incierto. Todos tenemos nuestras propias ambiciones, tal como dijo Lilly."

"Pero incluso así, se siente como si ahora faltara alguna cierta parte en nuestras vidas. Algo que nunca podrá ser reemplazado."


window hide Dissolve(1.0)
$ suppress_window_before_timeskip = True

scene black
with Dissolve(2.0)



label es_L30:



scene bg school_hallway2
with locationchange

play music music_daily fadein 1.0

"El sonido de mi teléfono móvil cerrándose contrasta con el cotilleo y ruido ambiental audible incluso en el pasillo fuera de la biblioteca."

"Es el primer día de las vacaciones de verano."

"Un momento que había parecido perpetuamente tan lejano, y sin embargo ahora no solo ya ha llegado sino que ha quedado dolorosamente en evidencia por los estudiantes, o la ausencia de ellos, en la escuela."

"La mayoría de los estudiantes han regresado a casa a pasar las vacaciones con sus familiares. Los pocos que quedan pasan por lo general conversando entre ellos, usualmente con respecto a lo que piensan hacer en las semanas que vienen."

"Me hace sentir como si yo fuera el raro, al tomar ventaja de que la biblioteca de la escuela siga abierta durante los primeros días de las vacaciones."

"Aparentemente es para que los estudiantes entreguen cualquier libro que hayan tomado prestado y aún no hayan devuelto, y para aquellos cuyos padres los pasarán a buscar, para ayudarlos a pasar el tiempo hasta que sean retirados."

"Gracias a la reciente y extensa llamada telefónica de mis padres, la cual me sacó tan descortésmente de mi sueño sobre el puf al final de la biblioteca, ahora me encuentro en la segunda categoría."

"Deslizando mi teléfono en mi bolsillo, esta vez recordando ponerlo en silencio, regreso al tranquilo y completamente plácido cuarto."

scene bg school_library_ss
with locationchange

"Es una imagen nostálgica."

"Tal como cuando Lilly me llevó por primera vez a la biblioteca, el tinte naranja del ocaso inunda el cuarto con su luz mientras que Hanako está sentada en un puf leyendo en silencio y Yuuko trabaja atenta, apenas visible tras el mostrador."

"Hanako en especial ha estado notoriamente más callada de lo usual desde los eventos de ayer, pero en realidad no puedo culparla."

"No era solo yo quien dependía de esa persona, después de todo."

"Vuelvo caminando en silencio al puf cerca de ella donde estaba sentado antes, teniendo doblemente cuidado de no hacer ruido innecesario."

scene ev hana_library
with locationchange

show ev hana_library_read
with charachange

"El suave soplido que suelta a medida que el puf se hunde bajo mi peso hace que los ojos de Hanako salten hacia mí, pero solamente por un segundo."

"Tengo la sensación de que Hanako ha estado callada solo en parte debido a la pena por la partida de Lilly."

"En cambio, ella parece más atenta y moderada de lo que esperaba; quizás debido a su deseo de arreglar el cómo tratar con la partida de Lilly en lugar de simplemente estar deprimida por el hecho. Me hace sentir un tanto orgulloso de ella."

hi "¿Oye, Hanako?"

show ev hana_library
with charachange

ha "¿S-sí?"

hi "¿Sigues con tu idea de viajar?"

"Ella asiente determinada."

ha "Partiré en uno o dos días más. Naomi ha decidido venir conmigo también."

hi "Vaya, qué rápido. ¿Adónde irán primero?"

ha "Creo que comenzaremos yendo hacia el norte… y luego doblaremos hacia abajo e iremos al sur."

hi "Entonces… ¿Hokkaido será primero?"

"Ella asiente otra vez, más dubitativa esta vez. Ninguno de los dos pasa por alto el significado de ese lugar."

hi "¿Sabes qué harás con los gastos para el viaje y el alojamiento?"

ha "Sí, ya lo he preparado todo. Creo que debería estar bien. Naomi dice que también tiene todo listo por su parte."

hi "Sabes que si necesitas cualquier cosa solo debes llamar, ¿cierto? Te di antes mi número. Puede ser en cualquier momento del día."

show ev hana_library_smile
with charachange

"Ella sonríe, lo cual se siente como una pequeña victoria personal en sí mismo."

ha "Lo sé."

ha "G-gracias… Hisao."

"Quizás Lilly tenía razón. Si bien puedo ofrecerle a Hanako cualquier ayuda que pueda dar, siento como si supiera que no la necesita."

"Ella en verdad ha crecido."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\n\nLos planes de Hanako para sus vacaciones hacen un fuerte contraste con mi decisión de simplemente seguir la sugerencia de mis padres y permanecer con ellos."

n "Las vacaciones siempre me han entusiasmado menos que a los demás, así que quizás esto es simplemente un regreso al statu quo."

n "\nAntes de mi ataque cardiaco, vivía tan sin rumbo que las vacaciones no eran muy diferentes de mi vida diaria de todas formas."

n "Después de las clases vagaría un tanto por la ciudad, a menudo con algunos amigos, antes de dirigirme a casa a cenar usualmente con uno de mis padres, pero rara vez ambos."

n "Sus horarios de trabajo no les dejaban mucho tiempo para estar en casa, e ir allá directamente de la escuela simplemente significaría que terminaría aburrido. Era un chico urbano hecho y derecho."

nvl clear

n "\n\n\nPero desde que llegué a Yamaku, se siente como si hubiera cambiado fundamentalmente como persona. La llamada telefónica con mis padres borró cualquier rastro de duda que pudiera haber tenido al respecto, en cualquier caso."

n "Si bien antes llevaba un nivel bastante normal de independencia para un adolescente, sin ser eso demasiado, mis padres estaban más que satisfechos al oír de mi nueva capacidad para cuidarme yo solo."

n "Lavar la ropa, cocinar para mí, limpiar, todo además de las otras tareas generales que nacen de vivir sin padres cerca… solo insignificantes cosas que tuve que aprender, pero con relativa facilidad."

n "\nCuando pienso al respecto, siempre dependí de ellos, incluso si no estaban en casa todo el tiempo. Pero, decir que nunca dependí de nadie luego de mudarme a los dormitorios de Yamaku estaría lejos de la verdad."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve
window show

yu "Um… disculpa…"

stop music fadeout 3.0

scene bg school_library_ss
show yuuko worried_down_ss at center
with locationchange

"Ambos levantamos la vista a la figura que juguetea incómodamente con sus dedos frente a nosotros. Algunas cosas nunca cambian."

show yuuko worried_up_ss
with charachange

yu "Ya está siendo hora de cerrar, así que um…"

"Oh, cierto. Me había olvidado que la biblioteca cierra más temprano durante las vacaciones."

"Hanako y yo nos levantamos y nos sacudimos el polvo, colocando nuestros libros de vuelta en el librero tras nosotros. El hecho de que nuestros gustos de lectura se superpongan en gran medida es útil en ocasiones."

"Con una reverencia a Yuuko para disculparnos por demorarnos tanto, Hanako nos deja."

show bg school_library_ss at bgleft
show yuuko worried_down_ss at twoleft
with dissolvecharamove

show hanako basic_normal_ss at tworight
with charaenter

ha "Nos vemos mañana, Hisao."

hi "Adiós."

hide hanako
with charaexit

"Y con eso, ella sale por las grandes y viejas puertas de madera que anuncian la entrada a la biblioteca."

play music music_happiness fadein 3.0

show bg school_library_ss at center
show yuuko neutral_down_ss at center
with dissolvecharamove

yu "Ella es una persona callada, ¿no es así?"

"Supongo que debería sorprenderme de que una empleada comparta una opinión personal de esta forma, pero luego de conocer a Yuuko por un tiempo es esperable."

"Nuestra relación es más personal, en lugar de una en la que ella actúe como una autoridad."

hi "Claro, creo que así es como ella es."

hi "Pero tiene mucha más confianza en ella misma estos días."

show yuuko smile_down_ss
with charachange

yu "No la conozco tan bien como tú, pero creo que estoy de acuerdo. Es bueno verla hablando con la gente aquí; ella no solía hacer eso antes."

hi "Oye, Yuuko… ¿sabes de la partida de Lilly, cierto?"

show yuuko worried_down_ss
with charachange

yu "Ella me dijo hace unos cuantos días. Debe ser difícil, dejar a todos detrás como lo está haciendo."

"Ella rápidamente me mira luego de decir eso, probablemente recordando que yo acudí a ella antes por consejos con respecto a la relación entre Lilly y yo."

show yuuko worried_up_ss
with charachange

yu "¿Vas a estar bien?"

"Esa es… una pregunta difícil. Es algo que preferiría no pensar por ahora, dados asuntos más urgentes."

hi "Algo parece un tanto extraño en todo este asunto, ¿no crees?"

"Yuuko parece pensar por un rato, apretujando distraídamente su rostro en una variedad de muecas creativas mientras lo hace."

show yuuko worried_down_ss
with charachange

yu "No creo conocerla lo bastante bien como para hacer ese tipo de juicios."

yu "Lo siento por no poder ser más de ayuda."

hi "No, está bien. Solamente estoy pensando en voz alta."

"Suelto un profundo suspiro y rasco mi cabeza frustrado."

hi "Hay tantas cosas pasando a la vez sobre las que no tengo control… se siente como si estuviera saturado."

show yuuko neutral_down_ss
with charachange

yu "Creo que todos pasan por momentos como esos."

yu "Lo importante es concentrarse en lo que puedes hacer, en lugar de lo que no puedes hacer. Al menos, así es como lo veo."

show yuuko smile_down_ss
with charachange

yu "Si no pensara de esa forma, no creo que fuera capaz de llevar mi vida tal como está."

"Ella lo dice con una sonrisa y un tono ligero, pero sus palabras están lejos de ser alguna broma. Estando repartida entre dos trabajos, para con algo de suerte hacer suficiente dinero no solo para vivir, sino que para la universidad, debe ser agotador."

"Quizás es por eso que, viniendo de ella, esto parece tener más significado que si hubiera venido de la mayoría de los demás."

hi "Supongo que tienes razón con eso."

hi "Otra vez gracias por tu consejo, Yuuko."

show yuuko smile_down_ss:
    ease 0.5 ypos 1.2
with None

show yuuko closedhappy_down_ss:
    ease 0.5 ypos 1.2
with charachange

with Pause(0.2)

show yuuko closedhappy_down_ss:
    ease 0.5 ypos 1.0
    linear 0.5 alpha 0.0
with charamove

"Ella hace una reverencia y sonríe otra vez, antes de volver al mostrador donde pasa tanto de su tiempo."

stop music fadeout 2.0

scene bg school_dormhisao_ni
with shorttimeskip

"Las diminutas alas de la grulla de cartón entre mis dedos son lo único visible en la luz tenue de mi habitación, apenas un poco de luz lunar asomándose entre las cortinas y por sus bordes."

show origami_hand:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with None

show origami_hand:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
show bg school_dormhisao_blurred_ni
with Dissolve (1.0)

play music music_twinkle fadein 10.0

"Yazco quieto en mi cama oscura por un largo rato, mirando ociosamente la pequeña ave de origami."

"Se siente como si hubieran pasado tantas cosas desde que Lilly la hizo, pero al mismo tiempo se siente como si muy poco hubiera cambiado."

"Comparado a todos los demás, he vuelto al principio. Podré haber encontrado una idea de adónde quiero llevar mi vida, pero eso es difícilmente algo que me afecte en estos momentos."

"Hanako ha cambiado, al menos eso lo sé. En todo caso, ella simplemente me hace sentir como que no tengo excusa para estar así, considerando su situación anterior."

"Lilly, en cambio…"

"Doy vuelta al ave en mis dedos, mirándola desde otro ángulo más."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\nCuando la conocí, ella parecía apartada y quizás un tanto distante. Sus acciones siempre eran cuidadosas, medidas y precisas, y su compostura mantenida con cuidado siempre daba la apariencia de serenidad y confianza infalibles."

n "A medida que pasó el tiempo, se volvió menos formal. Solo un poco, pero lo suficiente. Se sintió bien verla bajar sus inhibiciones junto a mí, y abrirse, aunque fuera un poco, por su propia voluntad; se sintió como si estuviera viendo a su verdadero ser volverse lentamente más visible y enérgico."

n "\nPero, ahora, estoy comenzando a tener dudas."

n "\nQuizás son de esperarse después de lo que es, efectivamente, el fin de nuestra relación. No se sienten nuevas o extrañas, sino como un libro viejo que se ha vuelto a encontrar y desempolvado."

n "Pronto me di cuenta luego de conocer a Lilly de que ella me veía como veía a Hanako; como alguien que necesitaba ayuda y cuidado. Al principio, simplemente pensé que estaríamos bien como amigos, ayudándonos mutuamente en nuestro limitado tiempo juntos en la escuela."

nvl clear

n "\n\nPero luego comencé a atesorar más y más nuestros momentos juntos, desde nuestras silenciosas caminatas a nuestras charlas durante el almuerzo. Las partes buenas de su personalidad se volvían cada vez más evidentes, y cada vez más agradables."

n "La ausencia causada por el viaje de Lilly a Escocia para visitar a su lejana familia y tía enferma solamente me hizo darme cuenta de lo mucho que me gustaba tan solo estar junto a ella, y pensé que ella sentía algo parecido."

n "\nPero, para ella, quizás eso no era todo lo que había en nuestra relación."

n "\nAun después de que ella regresara a Japón, eso solo significó que volvió a perder a su familia luego de verlos por tan poco tiempo."

n "Ella vivió gran parte de su vida sin una familia a su lado, sin mencionar a Akira trabajando largas horas, que tuvo poca opción más que ser así."

nvl clear

n "\n\nPensé que su sentido de independencia era un rasgo bueno y admirable. Iba en un completo contraste con mi dependencia de mis padres antes de mi ataque cardiaco, por reacio que haya estado para admitirlo."

n "Sin embargo, también significó que ella nunca dejó que la gente se le acercara mucho."

n "Perdió a su familia posiblemente debido a su ceguera, fue a una escuela diferente de cualquiera que ella conociera debido a eso, y se esforzó aun más para asegurarse de que no terminaría como una carga para su hermana y aquellos que la rodeaban."

n "\nY ahora, Akira va a Inverness, tal como la familia que pensó que había perdido."

n "Nunca me contó de sus planes, por mucho que estuviera en conflicto con respecto a ellos."

n "Lilly no quería ser una carga para nadie, incluso para mí."

n "\n\n… Soy un idiota."

nvl clear

n "\n\nNunca lo cuestioné. Nunca intenté estar ahí ni pregunté cuando ella necesitaba que lo hiciera."

n "Simplemente arreglé mi vida y esperé que permaneciera así para siempre, nosotros dos teniendo una larga relación donde ambos trabajábamos para alcanzar nuestro futuro juntos."

n "\nUn pequeño foso de frustración y enojo hacia mí mismo brota en mi pecho."

n "\nSolamente dejé que todo pasara, sin nunca intentar ayudar a Lilly."

n "\nQue ella estuviera ahí era suficiente. Pensé que podría seguir avanzando si eso fuera cierto."

n "Pero nunca pudo haber sido suficiente. Era una dependencia infantil en alguien, sin ningún intento de entenderle o ayudarle con su situación."

n "Gracias a eso, perdí a Lilly. Perdí a la persona que más amaba porque no estuve ahí para ella cuando me necesitaba."

stop music fadeout 5.0

nvl clear
nvl hide dissolve

show origami_hand:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with None

show origami_hand:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
show bg school_dormhisao_ni
with Dissolve (1.0)

hide origami_hand
with None

window show

"Con un sentimiento cada vez más furioso inundándome, me doy vuelta y dejo la grulla de vuelta en el escritorio junto a mi reloj, el lugar donde ha vivido desde el día que ella la dobló para mí."

"Desde aquel día cuando ella misma dijo que mis cargas no debían ser mías."

"Los molestos números rojos de mi reloj alarma brillan a través de la oscuridad de la habitación hasta mis ojos agotados."

"Diez en punto. Tarde. Pronto será el toque de queda."

hi "Me pregunto…"

"Akira mencionó que se marcharían esta tarde."

"No tengo idea de a qué hora es exactamente su vuelo… pero eso significa que hay una oportunidad, aunque sea pequeña, de que no se hayan marchado todavía."

"La adrenalina comienza a recorrer mi cuerpo mientras me siento en mi cama, mis ojos de pronto bien abiertos con la posibilidad."

"No hay garantías de que no se hayan marchado ya, y en efecto es posible que ya lo hayan hecho, pero también está la posibilidad de que no lo hayan hecho, por pequeña que sea."

"Solo esta vez, tal como debió haber sido antes…"

play sound sfx_switch

show bg school_dormhisao
with Dissolve(0.2)

$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_friendship fadein 9.0

"Me levanto y corro hacia mi armario, arrojando afuera algunas ropas tan rápido como puedo y poniéndomelas en rápida sucesión."

"Cada segundo que pasa es un segundo que no puedo recuperar, un segundo que puede significar la diferencia entre alcanzarlas y perderlas para siempre."

"Incluso si fallo, tengo que intentarlo. No puedo permitirle que deje todo atrás sin siquiera intentar detenerla. Sin, solo esta vez, estar ahí para ella."

"Con el resto de mi ropa puesta, apresuradamente tomo el teléfono del escritorio. Afortunadamente, el número de la compañía local de taxis sigue en mi historial de llamadas."

show bg school_dormhisao_blurred
show phone mobile:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with locationchange
with Pause (0.5)

"Una voz áspera y sin entusiasmo anuncia el nombre de la compañía mientras yo camino alrededor de la habitación. Me toma algo de esfuerzo detener mi voz y mantenerla clara por teléfono."

scene bg school_dormext_full_ni
with locationskip

"El gélido aire nocturno barre contra mí cuando abro la puerta de los dormitorios, pero de todas formas sigo con mi rápida marcha mientras troto y corro a medias hasta las puertas de la escuela."

"Puede que aún no sea el toque de queda, pero está precariamente cerca. Si hubiera un guardia por ahí sin duda alguna tendría algunas preguntas para mí, pero parece que he logrado salir justo antes de que lleguen, o que estén a la vuelta de la esquina."

scene bg school_gardens_ni
with locationchange

"Mi paso acelera mientras me abro paso por los jardines de la escuela, su encanto nocturno ya desaparecido cuando comienzo a correr hacia el portón de la escuela."

scene bg school_courtyard_ni
with locationchange

"Las lámparas del patio, por tenues que sean, entregan suficiente iluminación para alumbrar el camino y evitar que me tropiece. Los edificios mismos adoptan una apariencia rústica, casi antigua cuando los miro de reojo."

"En retrospectiva, parece extraño que alguna vez hayan parecido tan oscuros y sobrecogedores para mí. Ahora simplemente parecen edificios de escuela un tanto anacrónicos, lo mismo que cualquier otro salvo por su edad."

scene bg school_gate_ni
with locationchange

"Dejando las puertas detrás de mí, me detengo abruptamente justo ante el taxi. Estacionado al igual que el auto de Akira antes, su llamativo e iluminado letrero parece fuera de lugar en el tranquilo fondo campestre."

"Me apretujo impaciente por la puerta, señalándole al conductor la dirección donde ellas dos deberían con algo de suerte estar alojándose."

scene bg shizu_houseext_ni
with shorttimeskip

"Para cuando el taxi se detiene luego de su viaje a una velocidad enloquecedoramente casual, ya está realmente entrada la noche."

"La casa es en verdad enorme, su tamaño mucho mayor de lo que esperaba, y está siniestramente tranquila. Temiendo lo peor, le pido al conductor que permanezca solo en caso de que mis esfuerzos sean en vano."

"Un solo toque del sofisticado sistema de intercomunicación afuera de la puerta produce una breve melodía electrónica en el camino de otra forma silencioso. No pasa mucho antes de escuchar una voz grave y algo áspera en él."

mystery "Esta es la residencia Hakamichi. Por favor indique su nombre y por qué está molestándonos tan tarde."

"Sigo adelante a pesar de hacer una mueca de dolor por dentro ante la audible molestia en su voz."

hi "Habla Hisao Nakai. Esperaba encontrarme con Lilly o Akira, si siguen aquí."

"Sorprendentemente, logro reunir bastante energía en mi voz, suficiente para dejar al otro lado del intercomunicador en silencio."

show bg shizu_houseext_lights
with Dissolve(0.2)

"Pasan unos cuantos segundos en silencio, pero justo antes de presionar el botón otra vez y preguntar qué está sucediendo, se prende una luz afuera de la puerta frontal."

"Entrecierro mis ojos para intentar distinguir quién viene, pero cuando él pasa frente a un gran auto estacionado con cañas de pescar sobresaliendo de atrás, su identidad se hace clara."

"Su rostro está típicamente plácido y carente de emoción mientras camina sin prisa hasta la puerta."

"Sigue siendo infantil de manerismos, a pesar de su actitud. Presionando unos cuantos botones desde detrás de la reja, la puerta lentamente se abre."

show hideaki surprise_ni at center
with charaenter

hh "¿Hisao? ¿Qué estás haciendo aquí?"

"Creo que es la mayor cantidad de emoción que he escuchado en su voz, no que esa meta sea difícil de alcanzar."

hi "Akira me dijo que ella y Lilly se quedarían aquí antes de tomar su vuelo."

hi "Necesito hablar con Lilly, solo una última vez. ¿Siguen aquí?"

show hideaki sad_ni
with charachange

"La expresión en su rostro lo dice todo."

"Fracasé. Llegué demasiado tarde. La única vez que debía actuar rápido, y…"

show hideaki serious_up_ni
with charachange

hh "De hecho… es posible…"

hi "¿Qué? ¿Qué es?"

show hideaki confused_ni
with charachange

"Él queda un tanto sobrecogido por mi fervor, pero no puedo evitarlo en este punto."

show hideaki normal_ni
with charachange

hh "Se fueron hace poco; solo unos cuantos minutos antes de que llegaras, de hecho. Si vas directamente al aeropuerto, podrías… ¿¡Hisao!?"

"Voy corriendo de vuelta al taxi que me espera, tomando el poco dinero que queda en mi bolsillo mientras lo hago."

hi "¡Gracias, Hideaki!"

"Y con eso me siento, y prestamente le ladro mi destino."

scene bg city_street4_ni
show crowd_ni
with shorttimeskip

play ambient sfx_crowd_outdoors fadein 2.0

"Mi pecho late alocadamente mientras me apresuro calle abajo, mi cuerpo doblándose de distintas formas para pasar entre los peatones que caminan junto a mí."

"Con el camino bloqueado por completo por taxis y otros autos, dejando pasajeros y recogiendo a otros durante el tiempo que tienen que esperar, terminamos teniendo que detenernos casi una cuadra antes."

"Pero eso quedó en el pasado. Lo que importa es alcanzar a Lilly."

"Un pie toca el suelo, el otro rápidamente lo sigue sin siquiera pensarlo, como si mis piernas hubieran cobrado vida propia y todo lo que mi mente pudiera hacer es concentrarse en mirar frente a mí."

"Solo un vistazo de ese largo cabello suyo. Ese largo, y rubio cabello que era del mismo color que el trigo que se extendía hasta donde el ojo podía ver."

"Al final, dependía de Lilly, tal como Hanako. Incluso después de que comenzamos a salir, todavía no se siente como si ella se hubiese permitido depender de mí."

"Excepto por un momento. Aquel momento cuando nos sostuvimos firmemente en aquel brillante campo amarillo."

"En aquel momento ella debe haber temido perderme tal como perdió a los demás. Es por eso que, solo esta vez…"

"El aire nocturno me envuelve, arrebatándome cada resto de calor de mi cuerpo, hasta el punto en que se siente como si fuera pleno invierno en lugar de una noche de verano."

"Mis dedos, mis manos, mis pies… todos se sienten increíblemente fríos."

"El sonido de las multitudes que pasan queda reducido a no más que un ruido de fondo mientras que el sonido de mis zapatos contra el pavimento resuena fuertemente, cada paso adelantándose hacia la persona que tengo que alcanzar."

"Forzado por mi pecho endureciéndose en respuesta al frío de la noche, pongo un brazo sobre él para intentar calmarlo."

window hide

scene bg hosp_ext_ni
show crowd_ni
with locationchange

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)

window show

"Cuando el aeropuerto es visible, empero, me doy cuenta de que esta sensación es una que he sentido antes."

"No ahora… de todos los momentos para esto, por favor no este."

"Trago saliva y sigo adelante de todas formas, exigiendo a mi cuerpo tanto como este pueda."

"Salta sudor de mí mientras me abalanzo hacia adelante, mis hombros chocando contra el costado de alguien y mi mente de pronto inundada de emociones y recuerdos."

"Continúo sin disculparme. Ahora tengo que seguir moviéndome. Si me detengo, no estoy seguro de que pueda volver a comenzar, e incluso si puedo todo sería en vano si no llego a tiempo."

with vpunch

"Golpeo a otra persona, luego otra, ofreciendo poca resistencia a ser empujado de lado a lado."

"Mis pies están entumecidos. Mis brazos están perdiendo la sensación. Mi pecho me fuerza a encorvarme de forma extraña, endureciéndose aún más."

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

window show

"Esa tarde en la nieve… aquella vez en que mi vida cambió irreversiblemente… imágenes de Iwanako y esa maldita carta pasan una y otra vez por mi mente, el primer amor que perdí gracias a mi condición."

"No puedo dejar que eso vuelva a suceder. Ya no me importa lo que me pase, solo necesito verla una última vez."

"… ¡Ahí!"

scene ev lilly_airport
with flash

"Un trocito de amarillo y blanco se hace visible a la distancia, su figura enmarcada en una silueta por las luces que salen de la entrada del aeropuerto."

hi "¡Lilly! ¡Lilly!"

hi "¡Lilly! ¡Detente, por favor! ¡Lilly!"

"Vamos Lilly, sé que tu audición está lejos de lo—"

scene bg hosp_ext_ni:
    xalign 0.5 yalign 0.52 rotate 0 zoom 1.0
    linear 0.1 rotate -6 zoom 1.2
show crowd_ni:
    xalign 0.5 yalign 0.52 rotate 0 zoom 1.0
    linear 0.1 rotate -6 zoom 1.2
with vpunch

play sound sfx_impact

hi "¡Gah!"

"Mi vista de pronto se sale de control y acaba en el suelo, mi cuerpo desparramado sin cuidado luego de golpear a alguien y tropezarme."

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

window show

"Antes de poder evaluar el daño, un dolor increíble se enciende en todo mi cuerpo. Todos mis pensamientos quedan en blanco mientras me encojo y aferro frenéticamente mi pecho."

mystery "Oye, ¿estás bien? Esa fue una caída bastante fea."

"Este dolor… No puedo…"

hi "¡Argh… aaaaaargh!"

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

window show

"Cualquier golpe seco podría acabar conmigo. Cualquier sobreesfuerzo. Pensé que podría sobreponerme a mis propios límites esta vez…"

mystery "¡Algo anda mal con él!"

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.8)

window show

mystery "¿Qué sucede, estás…?"

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

window show

"Las voces de aquellos que se reúnen a mi alrededor son reemplazadas gradualmente por un fuerte zumbido en mis oídos. Ahora ya soy incapaz de mover mi cabeza, mis ojos giran hacia arriba para ver a los mudos mover sus labios."

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

stop ambient fadeout 0.3

show heartattack residual
with Dissolve (0.8)

window show

"Aun mientras aferro mi pecho, me doy cuenta de que ya no puedo sentir mis dedos, ni mis pies. Se siente como si mi cuerpo entero se estuviera apagando, comenzando por mis extremidades."

scene ev lilly_airport_end:
    truecenter
    zoom 1.2 rotate -8 subpixel True
    easein 12.0 zoom 1.0 rotate 0
with slowfade

"Con un último esfuerzo, giro mi cabeza para mirar hacia la entrada del aeropuerto que arroja su luz sobre mí."

"Lilly está allí, detrás de la multitud. Su cabeza está girada, pero solo apenas."

show passoutOP1
with None

"Puedo sentir mi visión apagarse mientras intento gritar, pero nada sale de mi boca a pesar de todos mis esfuerzos. Lenta pero seguramente, mi visión comienza a ennegrecer la imagen ante mí."

"Así que… así es como termina."

"Fracasé. Estaba tan cerca, tan tan cerca, pero al último momento mi condición me arrebató la oportunidad de una nueva vida y me arrastró de vuelta."

"Ahora voy a morir, desparramado a metros del aeropuerto, con una multitud de personas balbuceantes rodeándome y con Lilly marchándose a Escocia apenas un poco más allá."

hi "Li… lly…"

stop music fadeout 4.0

"Esa última palabra extingue lo último de mis energías. El mundo se sume en una profunda e inescapable oscuridad mientras cada músculo en mi cuerpo se apaga."

"Lo siento, Lilly."

"Llegué demasiado tarde."

scene black
with dissolve




label es_L31:

scene white
with dissolve


"…"

"……"

"………"

"¿Qué… está pasando…?"

"A medida que abro lentamente mis ojos, una brillante y blanca luz asalta mis retinas."

"Por varios minutos simplemente yazgo donde estoy, mirando sin pensar hacia el frente mientras mis dispersos pensamientos se aglutinan en mi mente que se despierta lentamente."

show bg hosp_ceiling:
    alpha 0.0
    linear 5.0 alpha 1.0
with None

"Lento pero seguro, el blanco empieza a enfocarse mientras un espacio vacío comienza a dibujarse en mi campo de visión."

"Es solo cuando la iluminación entra a mi visión que mi mente cae en cuenta de que esto es el techo sobre mí."

scene bg hosp_room2
with locationchange

"Levantándome lentamente, absorbo en silencio con todos mis sentidos los detalles del cuarto en el que me encuentro."

"El olor y gusto a un fuerte blanqueador llenan el aire, dando la impresión de un lugar demasiado limpio para ser natural."

"Paredes de un inofensivo color durazno claro, todas perfectamente pintadas sin ninguna grieta, mancha o imperfección."

"Una sola pintura enmarcada cuelga de la pared, perfectamente enderezada. Como las murallas, es tan aburrida e inofensiva como puede ser."

"Mi atención es atraída por la cortina traslúcida que ondea frente a mi visión, mis ojos siguiéndola hasta la ventana abierta que cubre."

"Pero cuando muevo mi brazo derecho para intentar levantarme y mirar a través de ella, siento el catéter hundirse incómodamente. Solo ahora, también, caigo en cuenta de la cánula que rodea mis mejillas y llega hasta mi nariz."

"Luego de moverme un poco, decido simplemente mirar por una esquina de la ventana."

scene ev lilly_hospitalwindow
with whiteout

"Más allá de las gruesas hojas de varios árboles grandes, puedo ver el verde abajo, extendiéndose hasta un campo. Una normal isla de verde en las afueras de la ciudad."

"A juzgar por el sol afuera, es mediodía. De cuál día, empero, no estoy seguro."

"Entonces… estoy en un hospital otra vez."

"Suelto un largo y agotado respiro mientras intento recolectar mis dispersos pensamientos, mi mente aparentemente dirigida hacia una docena de direcciones diferentes a la vez con la misma cantidad de emociones recorriéndome."

scene bg hosp_room2
with locationchange

"Luego de tenderme hacia atrás lentamente, decido comenzar por el principio; por qué estoy aquí."

"Hago retroceder mi mente, pero no puedo distinguir un recuerdo claro de lo que sucedió. Los sucesos de anoche… o la noche que haya sido… vuelven más como una serie de instantáneas que como un recuerdo coherente."

scene bg school_dormhisao_ni_fb
show origami_fb at center
show noiseoverlay
with flash

"Tendido en mi cama mirando el ave de origami."

scene bg shizu_houseext_lights_fb
show hideaki serious_up_fb at center
show noiseoverlay
with flash

"Hablando con Hideaki afuera de la residencia Hakamichi."

scene bg hosp_ext_fb
show crowd_still1_fb at center
show noiseoverlay
with flash

"Corriendo calle abajo, pasando junto a los peatones y chocando contra más y más de ellos."

scene bg hosp_ext_fb:
    xalign 0.5 yalign 0.52 rotate -6 zoom 1.2
show crowd_still2_fb:
    xalign 0.5 yalign 0.52 rotate -6 zoom 1.2
show noiseoverlay
with flash

"Cayendo."

scene ev lilly_airport_end_fb
show noiseoverlay
with flash

"Mirando a la enceguecedoramente brillante entrada al aeropuerto, viendo la espalda de Lilly mientras yazgo tendido en el suelo…"

"…"

scene bg hosp_room2
with fade

"El silencio del cuarto privado de pronto se siente abrumador."

play music music_rain fadein 2.0

window hide
nvl clear
nvl show dissolve

n "\nEntonces eso fue. Tuve mi oportunidad de corregir mi error, y la arruiné."

n "Ya sea que yo tuviera la culpa por olvidar mis medicamentos y no controlarme, o mi cuerpo la tuviera por rendirse tan pronto, eso no importa ahora."

n "Todo lo que importa es que, una vez más, estoy solo."

n "La almohada azul pastel cede sin ofrecer mucha resistencia al dejarme caer sobre la cama, su almidonada funda, junto con sus almidonados cobertores, dando poca comodidad."

n "Comparada a la oscuridad de los eventos de anoche, la brillante luz de la habitación a mi alrededor es llamativa. Pero todo lo que hace es enfatizar lo sobrenaturales que son los lugares como este."

n "\nArritmia."

n "\nUna palabra inusual. Una extranjera, alienígena. Una con la que no quieres estar en la misma habitación."

n "Una condición rara. Provoca al corazón a actuar de forma errática y ocasionalmente latir demasiado rápido. Puede ser fatal."

nvl clear

n "\n“Fue un milagro que hayas podido continuar por tanto tiempo sin que sucediera nada”, me dijeron."

n "Y luego, sucedió. Mi condición me arrebató todo; mi vieja escuela ya no era de importancia. Mi hogar quedó reducido a un lugar lejano. Tanto mis amigos como mi primer amor simplemente dejaron de visitar después de pasado un tiempo."

n "Me volví cínico y amargado. Distante y sumiso. En mi defensa, ninguna persona podría haber evitado eso luego de que le pasara tal cosa, pero de todas formas dejé el hospital como una persona definitivamente muy cambiada."

n "Las cosas cambiaron. Hice nuevas amistades con Hanako, Shizune y Misha. Encontré un nuevo sentido de “hogar” en mi dormitorio, un nuevo interés por las ciencias y el mundo a mi alrededor, y encontré una dirección en mi vida que nunca había sentido antes."

n "Pero también descubrí otras cosas."

n "La sensación de aislamiento en Yamaku y sus alrededores no era del todo indeseada, la tranquilidad otorgando una paz mental que tal vez no hubiera encontrado en otro lugar, pero le dio al área una sensación de estar fuera del camino, mantenida fuera de vista."

nvl clear

n "\n\nLa gente en las calles en ocasiones miraba incómodamente, o giraban rápido sus cabezas cuando se daban cuenta de que estábamos mirando. Incluso si mi condición no era visible, mi uniforme sí lo era."

n "Incluso si no lo fuera, yo aún era diferente. Tomaba diecisiete pastillas al día, en la mañana, al mediodía, y en la noche. Mi cicatriz, si bien escondida bajo la ropa, todavía era una marca permanente de mi condición. Y por sobre todo, estaba la posibilidad real de mi muerte."

n "Una mala caída. Un distraído golpe fuerte en la espalda. Una simple carrera llevada demasiado lejos. Cualquier cosa podría haber gatillado mi corazón, y varias veces me equilibré al borde del abismo incluso con todo el cuidado que tenía conmigo."

n "\nPero estaba bien. Podía haber vivido con todo eso."

n "Porque había una última cosa que encontré, o mejor dicho reencontré, después de entrar a Yamaku."

n "\nLa cual una vez más me fue arrebatada frente a mis ojos."

nvl clear

n "\nSolo ahora me doy cuenta de lo delicado que era mi nuevo sentido de la felicidad. Todo dependía de ella, la cabecilla de mi vida desde que entré a Yamaku como un taciturno, confundido y errante estudiante de transferencia."

n "Lilly Satou era la persona en la que podía depender por sobre todos los demás, y quien reciprocaba el amor que sentía por ella. Pero le fallé, y me di cuenta de ello demasiado tarde."

n "Pensé que podría simplemente establecer mi vida y continuar de esa forma para siempre, pero el mundo real no funciona de esa forma. Finalmente me di cuenta del significado de aquellas palabras, solo para ser abatido mientras confrontaba mi fracaso al no hacer eso a tiempo."

n "\n…"

n "\nLos alrededores en los que me encuentro ahora son demasiado familiares. Es como si Yamaku hubiera sido un sueño, y aún estuviera recuperándome de mi primer ataque cardiaco fuerte."

n "Quizás es por eso que me siento tan cansado. Se siente casi como si hubiera vivido todos estos últimos meses de mi vida en el lapso de minutos."

nvl hide dissolve
nvl clear

scene black
with shuteye

window show

"El peso de mis párpados cierra mis ojos, mi cansancio físico y mental evitando que oponga resistencia."

window hide
with Pause(1.0)
with shorttimeskip
with Pause(1.0)
window show

"Murmullos ininteligibles desde el frente de la cama me sacan de mi sueño."

"Con mis ojos aún cerrados, puedo concentrarme y distinguir a alguien, aparentemente una enfermera, despidiéndose de un doctor."

scene bg hosp_room2
with openeye

"Cuando abro mis ojos, noto la puerta cerrarse en mi visión periférica."

"El doctor comienza a leer algunas notas de un portapapeles sostenido en su mano, repasando con cuidado las páginas."

"Luego de consultar sus evidentemente importantes documentos, él levanta la mirada y nota la mía. Es ahora que noto algo ligeramente extraño con respecto a su expresión y disposición general, pero no puedo decir exactamente qué es."

"Doctor" "Ah, veo que está despierto… Sr. Nakai."

"Su rápida mirada hacia el final de la cama, para verificar mi nombre, demuestra que sus documentos obviamente no lo tenían escrito en ellos."

"Doctor" "Debo admitir que esto es un tanto desafortunado; sus padres lo visitaron hace un momento mientras usted dormía. Podría notificarles que está despierto ahora, si gusta."

hi "Um… gracias. Eso sería bueno."

"Doy una respuesta un tanto aturdida, probablemente la que él esperaba, antes de pensar realmente en lo que estoy diciendo."

"Doctor" "No hay problema."

"Doctor" "Si tiene alguna pregunta que desee hacer, estaría encantado de responderla. Eso es, a menos que prefiera descansar; la anestesia seguirá afectándolo por un tiempo, me temo."

"La anestesia… por supuesto. Es por eso que me sentía tan extraño la primera vez que desperté."

"Lentamente niego con mi cabeza, sin intención de desencajar algún tubo o causarme algún tipo de molestia mayor a la necesaria. El doctor cortésmente baja su portapapeles en respuesta."

hi "Supongo que mi principal pregunta es… ¿qué pasó exactamente?"

"Doctor" "Dicho de forma simple, desafortunadamente tuvo otro ataque cardiaco. Aunque no fue tan severo como el primero, tuvo mucha suerte de que sucedió tan cerca de un hospital."

"Doctor" "Luego de estabilizarlo, fue llevado al salón de operaciones. Lo que siguió fue una laparoscopía para insertar un marcapasos temporal."

"Doctor" "En general, el incidente ocurrió hace dos días, y el tratamiento de emergencia se llevó a cabo muy pronto después. Desde entonces, lo hemos mantenido bajo observación mientras dormía."

hi "¿Estaré bien? ¿Hay algún problema duradero?"

"Doctor" "Comparado al procedimiento que se realizó durante su primer ataque cardiaco, esto fue relativamente menor."

"Doctor" "Si bien tendrá que someterse a cirugía una vez más en unos cuantos días para retirar el marcapasos, asumiendo que no haya complicaciones, no debería haber consecuencias a largo plazo."

"Sigue hablando, el tema cambiando a una repetición de hechos con respecto a la arritmia y mis medicamentos que ya conozco en su mayoría. Comienzo a asentir y fingir interés, mientras mi mente va a la deriva."

"Comienzo a pensar en lo perfectamente colgada que está la inofensiva pintura que cuelga en la pared detrás de sus hombros, y de lo limpio y estéril de los alrededores, incluyendo al mismo doctor."

"Doctor" "Si mi murmullo lo aburre, está invitado a decirlo, Sr. Nakai. Dios sabe, pierdo el control a veces."

"Suelta una breve risa de su burla hacia sí mismo mientras yo hago una mueca incómodo, descubierto de mal forma."

"Pero la risa del doctor suena diferente a la del enfermero en Yamaku, ahora que lo pienso. Mientras busco la razón, me doy cuenta de por qué el hombre frente a mí da una sensación un tanto “rara”."

"Su sonrisa es ordenada y estéril. Dice su pequeño chiste perfectamente, con una risita común e inofensiva."

"Es como si, en lugar de hablar con un hombre cuyo nombre está escrito con claridad en una chapa en su bata de laboratorio, estuviera interactuando con un actor que lee un libreto ensayado, cada acción coreografiada de antemano."

"Pero supongo que debe ser de esta forma, siendo doctor."

"Debe mantener su ordenada y estéril sonrisa cuando habla con la chica con cáncer lentamente avanzando por su cuerpo, cuando calma a la mujer que seguramente morirá por el parto…"

"… Y con todos los otros pacientes terminales o críticamente enfermos."

"Esa pequeña porción de distancia. Esa pequeña porción de desinterés."

"Me hace dudar de si he sido demasiado duro, especialmente considerando que es una disposición alejada de ser adoptada solo por la gente en su profesión."

"Después de todo, a quien amé mantuvo esa misma distancia con los otros."

"Alzando nuevamente la mirada hacia el doctor, me doy cuenta de que he estado pensando con mi cabeza inclinada durante un rato."

"Doctor" "Entiendo que debe seguir cansado. Ha pasado por mucho, y como mencioné antes, la anestesia debería seguir afectándolo."

"Doctor" "Si no le molesta, lo dejaré descansar y le diré a sus padres que ha despertado por usted."

hi "Creo… que eso sería bueno. Gracias."

stop music fadeout 6.0

"Él asiente de forma seca antes de tomar su portapapeles y abrirse camino hasta la gran puerta blanca en una esquina de la habitación, cerrándola detrás de sí con un golpe."

"Al final, vuelvo a estar solo."

"Lilly se ha ido. Akira se ha ido. Hanako debe estar viajando, e incluso mis padres ya han dejado el hospital."

"Cuatro pálidas paredes durazno, un techo blanco, y una sola ventana abierta para mirar hacia el mundo exterior."

"Es difícil pensar en el futuro cuando el pasado está amontonado a tu alrededor, claustrofóbico en su limpio, estéril, almidonado, y con olor a blanqueado puño."

"Sin tener qué hacer o en qué concentrarme, me contento con dormir el tiempo que haga falta como si esto fuera solamente otro sueño como Yamaku lo fue."

scene black
with dissolve



label es_L32:

scene white
with dissolve

"Blanco."

"Un estéril y limpio blanco para un estéril y limpio cuarto."

$ renpy.music.set_volume(0.05, 0.0, channel="music")
play music music_musicbox fadein 10.0

show bg hosp_ceiling:
    alpha 0.0
    linear 5.0 alpha 1.0
with None

"Mis ojos se abren, y simplemente miro el techo durante un tiempo. Es casi tan interesante como lo sería la televisión, montada en su repisa de metal colgada del techo frente a la cama."

"En efecto, todo el uso que se le dio a la televisión fue durante el tiempo en que mis padres estuvieron aquí. Encendida en silencio mientras esperaban que me despertara, era casi tan banal como la primera vez que estuve en un hospital."

"Hoy más temprano una enfermera me ofreció apagar los parlantes de la máquina de electrocardiogramas. Me negué simplemente porque el sonido es completamente normal para mí ahora."

"Es casi reconfortante, de cierta forma. Su regularidad como de metrónomo entrega al menos una sensación de que el tiempo está avanzando, incluso en un lugar como este."

"Pero después de un tiempo escuchando sus pitidos completamente despierto, me doy cuenta de que hay otro sonido en la habitación."

$ renpy.music.set_volume(0.1, 5.0, channel="music")

"Concentrando todos mis esfuerzos en escuchar, una tarea facilitada por la falta de distracciones, se puede oír una pequeña melodía metálica."

"Ligera y tranquila, la música suena casi frágil al ser ahogada por los pulsos del electrocardiograma."

scene bg hosp_room2
with locationchange

"Ladeando apenas mi cabeza a un lado para poder ver la fuente de la melodía sin desencajar ninguno de los sensores y tubos puestos en mí, noto una pequeña caja de madera en la mesa de noche junto a la cama."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

show musicbox open:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"Mi boca se abre apenas mientras miro en silencio el pequeño cilindro amarillo de metal rotando lentamente adentro, las pequeñas protuberancias en su superficie apareciendo y desapareciendo gradualmente."

"Esta caja musical… es la que le regalé…"

show musicbox open:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide musicbox
with None

"El crujido de la puerta me saca de mi ensimismamiento, mi cabeza y mi corazón permaneciendo quietos mientras mis ojos se mueven para ver quién está entrando."

"Larga falda canela… chaleco durazno por debajo del hombro… piel pálida, casi de porcelana… ojos azules nublados y un largo cabello amarillo…"

show lilly basic_reminisce_cas at center
with charaenter

"Todo lo que puedo hacer es observar mientras Lilly entra lentamente a la habitación, sus dedos recorriendo suavemente la pared para orientarse, y mi mente se detiene con un estremecimiento."

hi "¿L… Lilly…?"

show lilly basic_oops_cas
with charachange

"Ella se detiene en la mitad de un paso, su cuerpo completo tensándose."

li "¿Hisao? ¿Fuiste tú?"

"Su voz es serena y pensativa, haciendo eco a su expresión."

hi "Pensé que estabas…"

show lilly basic_sad_cas
with charachange

"Lilly da un vacilante paso adelante, luego otro, como si estuviera conteniéndose."

show lilly basic_sad_cas_close
with characlose

"Pero el control sobre su compostura es en vano, y finalmente ella se apresura adonde estoy acostado mientras que lo último de su resistencia cae."

$ ksgallery_unlock("unlock_ev lilly_hospitalclosed")
scene ev lilly_hospitalclosed at l_hosp_out
with whiteout

"Me toma un poco por sorpresa cuando se aferra a mí, agachándose mientras comienzan a caer lágrimas de sus mejillas, ya que hace solo minutos atrás pensaba que ella estaba al otro lado del mundo."

"Luego de un momento de duda, coloco mi mano derecha en su suave hombro."

li "¡Hisao! ¡Hisao!"

"El cuerpo de Lilly tiembla mientras sus lágrimas manchan las sábanas, sus emociones aflorando a través de su exterior cuidadosamente mantenido."

"Con su rostro ahora más cerca, y siendo más fácil ver su pálida piel iluminada por la luz del sol de la ventana, noto sus mejillas más rojas de lo que deberían estar."

hi "Está bien, Lilly. Estoy bien. No necesitas—"

$ ksgallery_unlock("unlock_ev lilly_hospital")
show ev lilly_hospital at l_hosp_out
with charachange

"Ella se endereza rápidamente, su llanto acallado por la fuerza mientras que tanto pena como tenacidad permanecen en sus ojos humedecidos. Su naturaleza orgullosa, siempre siendo algo con que enfrentarse, me toma desprevenido."

li "¡Deja de decirme que no me preocupe por ti, Hisao!"

li "Solo esta vez… déjame llorar…"

"Quedo sin palabras. Ella espera una respuesta, pero su compostura vuelve a caer luego de unos cuantos segundos."

show ev lilly_hospitalclosed at l_hosp_out
with charachange

"Trago saliva con fuerza e intento calmar mis propias emociones mientras ella llora en mi cama, una extraña mezcla de alivio y depresión aflorando."

"Lilly está… aquí. En verdad está aquí."

"Si no pudiera sentir su piel bajo mi mano, difícilmente creería a mis propios ojos. Mis esfuerzos no fueron para nada; el intento de mi cuerpo por arrebatarme una vez más todo lo que me era importante ha sido frustrado."

"Pero ahora… No me siento tan feliz como creí que me sentiría."

"Verla aquí, llorando de esta forma por mí… esto es lo único que quería evitar desde que llegué a amarla, no, desde dejar el hospital."

hi "Lo siento, Lilly. Es mi culpa estar aquí; no debería haber intentado exigirme tanto."

"Suelto un bufido autodespectivo."

hi "Luego de pasar meses manteniéndome bien para que nadie se preocupara por mí, fui e hice algo como esto. Supongo que soy muy tonto."

scene bg hosp_room2
show lilly basic_weaksmile_cas_close at center
with whiteout

"Con un par de lloriqueos y un largo respiro, Lilly logra recuperar la compostura y calmarse un poco."

"A pesar de sus mejillas rojas, ojos húmedos y las líneas de sus lágrimas aún visibles, ella delicadamente pone aquella sonrisa débil que tan a menudo solía mostrar."

li "No debes culparte. Después escuché que había pasado mientras estabas corriendo por la calle detrás de mí, ¿cierto?"

hi "Aun así…"

"Ella limpia sus ojos con la parte de atrás de su mano, regresando más a su antiguo ser a medida que la avalancha de emociones se termina."

show lilly basic_reminisce_cas_close
with charachange

li "¿Por qué me perseguiste, Hisao?"

show lilly basic_concerned_cas_close
with charachange

"Me muevo para responder, pero noto su cara contrayéndose."

li "Incluso después de que dije adiós, y de que dejé la Academia Yamaku…"

"Ella toma un momento para calmarse, sus emociones a punto de aflorar una vez más."

hi "Solo quería pedirte disculpas."

show lilly basic_surprised_cas_close
with charachange

li "¿Disculpas?"

hi "Por todas las veces que no estuve ahí cuando me necesitabas."

hi "Hasta ahora, pensaba que el que tú siguieras ahí sería suficiente. Solo te necesitaba a ti a mi lado para hacer que cualquier día se sintiera mejor."

hi "Aun si mi cuerpo es así, quiero ayudarte, Lilly; estar ahí cuando necesites a alguien."

show lilly basic_weaksmile_cas_close
with charachange

li "Pero siempre estuviste ahí, Hisao…"

hi "¿Por qué querías ir a Escocia, Lilly?"

show lilly basic_sleepy_cas_close
with charachange

li "¿Por qué…? Te lo dije antes: porque Akira se va, y por la llamada de mi familia a su casa."

hi "¿Por qué no dijiste que querías ir?"

show lilly basic_oops_cas_close
with charachange

li "Yo—"

hi "No soy terco a menudo, pero esta vez creo que necesito serlo. Quiero que te quedes aquí, Lilly."

hi "Quiero que permanezcas aquí donde viven todos los que conoces, y donde todos tus sueños y ambiciones se crearon. Si eliges quedarte, nunca dejaré tu lado. No te dejaré perder a otra persona."

hi "Cuando tuve mi ataque cardiaco, me arrebataron a todos y todo lugar que conocía. Me mostraste una nueva vida después de llegar a Yamaku. Perdí mi pasado, pero tú me mostraste un futuro."

hi "Es verdad que no siempre he estado ahí para ti. No soy confiable, a veces mentí, y pensé que llegaría a entenderte cuando ni siquiera me entendía a mí mismo."

hi "Sea como fuere, también quiero darte un futuro. Quiero estar ahí para ti, compartir tus cargas y tu felicidad, tal como te lo prometí en Hokkaido."

hi "Quiero que confíes en mí. Sé que tuve problemas para confiar en ti, después de haber perdido a tanta gente que conocía luego de mi ataque cardiaco, pero así es como sé que ser incapaz de confiar en otros puede sentirse horrible."

hi "Es por eso que no puedo verte simplemente desechar todo de esta forma. Nunca quise que pasaras por lo mismo que yo. Haría lo que fuera para detener eso."

show lilly basic_weaksmile_cas_close
with charachange

li "Puedes ser bastante firme cuando te lo propones, ¿no?"

hi "Como dije, no es a menudo."

"Mi débil sonrisa se cae, empero, al hundirse la aguja del intravenoso en mi brazo. Es un severo recordatorio de mi atadura a mi condición."

show lilly basic_concerned_cas_close
with charachange

"El rostro de Lilly se tensa mientras suelto una leve exclamación de dolor, haciéndome desear de inmediato haberla suprimido mejor. Todo lo que puedo hacer es suspirar derrotado."

hi "He intentado no dejar que nadie se preocupe por mí durante todo el tiempo desde que dejé el hospital, pero ni siquiera puedo evitar que la persona que más amo llore por mí."

hi "Incluso si al fin soy capaz de expresar mis sentimientos con palabras, me siento bastante inútil con un cuerpo así."

hi "Cada vez que intentaba alcanzar algo, simplemente me era arrebatado, e incluso ahora las cosas acabaron para mejor solo por suerte."

hi "Supongo que eso es algo más por lo que debería disculparme. Lo único que puedo hacer es hacerte preocupar. Ahora mismo hay muy pocas posibilidades de que viva una vida remotamente completa."

"La sensación de la cálida y suave mano de Lilly moviéndose por mi mejilla izquierda me hace levantar mi cabeza, su sonrisa gentil y cálida mientras me toca."

show lilly basic_smileclosed_cas_close
with charachange

li "Creo que para ti es muy natural decir algo así. Siempre fuiste tan sincero y tímido."

show lilly basic_smile_cas_close
with charachange

li "También eras reservado y apacible, y paciente hasta el exceso con Hanako, y a la vez curioso por todo y todos."

show lilly basic_weaksmile_cas_close
with charachange

li "Cuando dije que te extrañaba mientras estaba con mi familia, no estaba mintiendo o exagerando. Ocupabas mis pensamientos todo el tiempo, y me ayudó a pasar ese momento."

show lilly basic_reminisce_cas_close
with charachange

li "Es por eso que estaba tan confundida sobre qué hacer cuando mi familia me llamó. Incluso después de pensar que había tomado una decisión, intentaste con todas tus fuerzas confrontarme al respecto."

show lilly basic_weaksmile_cas_close
with charachange

li "No me confesé a ti por lástima o por creer que eras de alguna forma distinto de lo que realmente eres. Me confesé porque no quiero perderte nunca, y quiero que siempre seas parte de mi vida, sin importar lo que pueda cambiar."

show lilly basic_smileclosed_cas_close
with charachange

li "Eres una persona muy hermosa, Hisao. Tu corazón no cambia nada de eso, así que por favor, ya no te disculpes por cómo eres."

"Por un largo rato, impera el silencio en la habitación."

"En realidad no estoy seguro de qué es este nuevo sentimiento en mi interior, pero se vuelve insignificante mientras miro sin palabras el rostro sonriente de Lilly, cálido y gentil como siempre."

"Es solo cuando su pulgar cruza mi mejilla, apartando una única gota de humedad, que me doy cuenta de que esto es todo lo que quería."

"En lo que se siente como la primera vez, pongo una sincera y amplia sonrisa. Cuando Lilly la siente contra su palma, me regresa el gesto."

"Pasa más tiempo antes de que alguno de los dos diga una palabra, sin la necesidad de hablar para comunicar nuestros sentimientos hacia el otro."

hi "Sé que no puedo prometerte que siempre estaré cerca, o que estaremos juntos por siempre."

"Con algo de dificultad levanto lentamente mi mano, colocándola sobre su pálido hombro."

hi "Pero… creo que al menos puedo llevarte al festival de Tanabata el próximo año, para compensar el hacer que te perdieras el de este."

show lilly basic_emb_cas_close
with charachange

"La expresión de Lilly es de sorpresa, aunque no puedo decir que la culpe."

li "¿Te… acordaste de eso?"

hi "Tengo una memoria muy buena. A veces."

show lilly basic_giggle_cas_close
with charachange

"Ella levanta un poco su cabeza y saca su mano de mi mejilla, soltando una pequeña y divertida risita. Sonrío distraídamente ante lo sincera que es, casi femenina en su ligereza."

show lilly basic_cheerful_cas
with charadistant

"Todavía sonriendo cálidamente, ella se recompone y se endereza con una mano descansando en mi pecho."

"Se siente como si la estuviera viendo por primera vez, el sol de la ventana brillando detrás de ella tal como lo hizo cuando entré por primera vez a ese cuarto donde ella estaba bebiendo té."

show lilly basic_smile_cas
with charachange

li "Muy bien entonces. ¿Hacemos una promesa entre nosotros de ir a Tanabata el próximo año juntos?"

"Aun si ella no puede verme hacerlo, asiento aprobando."

hi "Lo prometo."

show lilly basic_smileclosed_cas
with charachange

li "Lo prometo."

window hide

stop music fadeout 4.0




label es_L33:

window hide None

play ambient sfx_parkambience fadein 6.0

scene bg lilly_hilltop
with Dissolve(3.0)

play music music_lilly fadein 5.0

window show

"Akira, Lilly y yo estamos sentados en silencio sobre el terraplén cubierto de hierba muy por sobre el pueblo local, la brisa soplando gentilmente en el despejado cielo."

"Podremos estar a tan solo unos cuantos minutos a pie del pueblo, en una colina apenas afuera de sus límites, pero la vista es completamente inesperada."

show lilly basic_smileclosed_cas_close:
    left
    ypos 1.1
with charaenter

"Lilly está sentada junto a mí, sus ojos cerrados, y la suave brisa pasa a través de su pelo."

li "Este es un lugar agradable."

hi "Sí. No sabía que había un lugar como este cerca de Yamaku."

show akira basic_ending_close:
    right
    ypos 1.1
with charaenter

aki "Y yo tenía que ser la que lo descubriera, por supuesto."

"La sonrisa de Akira es auténtica, pero su tono es un poco distinto de su naturaleza despreocupada de siempre."

show akira basic_smile_close
with charachange

aki "Pero es bueno que ya estés fuera del hospital, Hisao."

hi "Nadie está más feliz que yo. No puedo soportar los hospitales."

aki "Entonces, ¿ustedes dos vuelven a clases mañana?"

$ doublespeak(hi, li, u"Síp.", u"Síp.")

show akira basic_ending_close
with charachange

"Akira suelta una risa, divertida, antes de volver la mirada hacia el pueblo abajo, los árboles entre los edificios meciéndose con el viento."

hi "Una lástima que no pudiéramos ir al norte durante las vacaciones de verano, o ir al Tanabata."

show lilly basic_weaksmile_cas_close
with charachange

li "Yo no me preocuparía, siempre está la próxima vez."

show akira basic_smile_close
with charachange

aki "Se graduarán antes de las próximas vacaciones de verano, ¿no es así?"

hi "Sí. Pero seguirá la universidad después de eso, recuerda."

aki "¿Van a la misma?"

show lilly basic_smile_cas_close
with charachange

li "Posiblemente. Ambos tenemos notas lo suficientemente altas como para cumplir los requisitos."

hi "Suenas tan segura…"

show lilly basic_cheerful_cas_close
with charachange

li "No te preocupes, tú eres mejor que yo en la mayoría de las materias."

hi "Supongo que lo veremos a su debido tiempo."

show akira basic_laugh_close
with charachange

aki "Ese es el espíritu. Solamente disfruten en Yamaku mientras están ahí."

show lilly basic_weaksmile_cas_close
with charachange

"Lilly suelta un triste suspiro ante la distinción hecha entre Akira y nosotros dos."

show lilly basic_reminisce_cas_close
with charachange

li "¿De verdad tienes que regresar a Escocia?"

show akira basic_resigned_close
with charachange

aki "Sí. Esa gente ya va por mi sangre con cómo están las cosas."

hi "¿No debías quedarte tanto tiempo?"

show akira basic_ending_close
with charachange

"Ella pone su típica sonrisa amplia."

aki "Sacar un pasaporte para mi novio tomó algo de tiempo."

hi "¿Vas a llevarlo contigo?"

show akira basic_smile_close
with charachange

aki "Solo por un tiempo al principio. Es un hombre sorprendentemente cosmopolita, así que creo que le irá bien."

show akira basic_lost_close
with charachange

"Akira resopla divertida."

aki "Si nuestro padre se hubiera salido con la suya, yo me habría ido hace mucho tiempo."

show akira basic_laugh_close
with charachange

aki "Solo no podía dejar pasar una excusa para permanecer con mi hermana pequeña favorita un poco más."

show lilly basic_smileclosed_cas_close
with charachange

"Ella se inclina a la derecha y le da a Lilly un fuerte y juguetón abrazo, animándola considerablemente."

li "Es bueno estar contigo una última vez."

hi "Si sirve de algo, yo siento lo mismo."

show akira basic_smile_close
with charachange

aki "Ja, gracias a ambos. Intentaré volver alguna vez, no se preocupen."

show lilly basic_reminisce_cas_close
with charachange

li "Es una pena que el negocio te mantenga tan ocupada."

show akira basic_lost_close
with charachange

aki "Ese lugar no se dirigirá por sí solo, me temo, y creo que va a ser lo mismo por allá."

show akira basic_smile_close
with charachange

aki "Considerando eso, es mejor que me marche."

hi "Diviértete allá, Akira."

show akira basic_laugh_close
with charachange

aki "Jaja, lo haré."

show akira basic_smile_close at right
with dissolvecharamove

"Con un leve gruñido, se levanta con sus manos y se para, sacudiéndose mientras lo hace."

show akira basic_lost_close at right
with charachange

aki "Bueno, será mejor que me vaya. El avión no me esperará, después de todo."

"Hay una cierta melancolía inusual en su tono de voz, sus ojos firmemente puestos en su hermana."

show lilly basic_weaksmile_cas_close
with charachange

li "Estaré bien, Akira."

show akira basic_resigned_close
with charachange

aki "Sí, lo sé."

show lilly basic_smileclosed_cas_close
with charachange

li "Vamos, no es tan malo. Podrás volver a vernos pronto."

"Es extraño que Lilly conforte a una dubitativa Akira para variar. Ella en verdad ha cambiado."

show lilly basic_smile_cas_close
with charachange

li "Adiós, Akira."

hi "Ciao."

show akira basic_smile_close
with charachange

"Por un segundo, la figura de negro baja su mirada hacia nosotros dos, sonriendo ampliamente. Quizás más ampliamente de lo que la he visto antes."

show akira basic_boo at tworight
with charadistant

"Ella suelta un largo y un poco indeciso respiro para calmarse antes de partir, pero eventualmente mete su mano en sus bolsillos y se da la vuelta."

"Y con eso se marcha caminando, una mano en el aire mientras anda."

show akira basic_ending
with charachange

aki "¡Nos vemos luego, ambos!"

hide akira
with charaexit

"Una tonada de jazz sin ritmo, melodía o dirección hasta el final."

show bg lilly_hilltop at bgright
show lilly basic_smileclosed_cas_close at center
with dissolvecharamove

"Luego de unos momentos de estar sentados en silencio, Lilly y yo nos levantamos y nos sacudimos."

"Dándome vuelta hacia ella con una ancha sonrisa, extiendo mi mano."

hi "Partimos nosotros, ¿entonces?"

"Ella toma mi mano con la suya, asintiendo gentilmente y con una sonrisa tan hermosa y cálida como siempre."

show lilly basic_cheerful_cas_close
with charachange

li "En efecto partimos, Hisao."

scene unlock_ev lilly_goodend
show evbg lilly_goodend:
    truecenter
    zoom 3.0 subpixel True
    1.0
    linear 0.5 zoom 0.9
    easein 12.0 zoom 0.8
show evfg lilly_goodend:
    truecenter
    zoom 6.0 subpixel True
    1.0
    linear 0.5 zoom 1.2
    easein 12.0 zoom 0.8
with whiteout

"Mientras nos dirigimos hacia la escuela, esa maravillosa sonrisa se graba en mis recuerdos. Esa maravillosa sonrisa que ambos compartimos."

"Nuestros pasados podrán estar dispersos y a veces eclipsados por la tristeza, pero también son una parte irrevocable de nuestras vidas y personalidades. Aun si pudiera cambiar una sola cosa, no lo haría, porque mi pasado fue lo que me trajo aquí."

"Es por eso que, aun con todo lo que nos ha pasado antes, y todo lo que podría acontecernos… juntos, seguiremos caminando hacia adelante."

"Adelante… hacia el futuro. Nuestro futuro."

window hide Dissolve(1.0)

stop ambient fadeout 2.0
stop music fadeout 2.0

scene black
with Dissolve(1.0)

with Pause(1.0)

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
