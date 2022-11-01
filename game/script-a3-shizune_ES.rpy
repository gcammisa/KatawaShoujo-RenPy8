label es_S17:

window hide None

scene bg school_hallway3
with locationchange

nvl clear
nvl show dissolve

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_normal fadein 3.0

n "\nLos días siguientes pasan sin novedades y con sorprendente rapidez. Encuentro una motivación renovada en aprender lenguaje de señas. Parece que tengo un don para aprender señas, así que sería un desperdicio no hacerlo, y quedarme atrás sería incluso más inaceptable."

n "Las vacaciones de verano se acercan. Aunque imaginé que el trabajo del consejo estudiantil vería una disminución proporcional a lo letárgicas que mis clases se están volviendo, no ocurre así. Todos los días, quedo abrumado con trabajo cada vez más carente de sentido."

n "A pesar de lo mucho que quiero, no tengo ni siquiera un segundo libre para hablar con Shizune actualmente. Cada vez que la miro, su cara está enterrada en algún libro de registros o en alguna pila de papeles que necesitan ser revisados por triplicado."

n "\n\nHoy, desperté temprano para venir a la escuela antes que todos los demás, con la esperanza de alcanzar a Shizune. Ella tiene la costumbre de venir a primera hora en la mañana, para ser más puntual que todos los demás estudiantes. Desafortunadamente, creo que estoy más temprano que ella."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

play sound sfx_doorclose

window show

"Escuchar la puerta del salón del consejo estudiantil cerrarse con un clic a mi derecha me dice que no es el caso. Supongo que llegué aquí justo detrás de ella."

play sound sfx_dooropen

scene bg school_council
with locationchange

"Entro al salón y le doy un toquecito a Shizune en su hombro para llamar su atención."




show shizu behind_smile at center
with charaenter

"Tal vez ella espera una conversación, lo cual es la razón por la que baja el envase de cartón de jugo de naranja que tiene en su mano."

ssh "Buenos días."


his "¿Dónde está tu media naranja?"

show shizu adjust_frown
with charachange

ssh "Somos individuos separados."

"Pensando en ello, a ellas les deben decir eso bastante. No puedo pensar en otra manera de explicar lo preparada que estaba con esa respuesta."

show shizu basic_normal
with charachange

ssh "Estás aquí temprano. Eso es bueno, puedes ayudarme a revisar algunos folletos. Saldrán más tarde hoy."


his "Vine aquí temprano específicamente para poder verte sin tener que hacer trabajo."

show shizu behind_smile
with charachange

ssh "Según Misha, llegar temprano no es nuevo para ti."

his "Tampoco es nuevo para ti."

show shizu adjust_happy
with charachange

ssh "¿Estás diciendo que quieres competir?"

"Shizune ajusta sus anteojos con indiferencia, un gesto que contradice lo vertiginosa que está en su interior sobre la idea de tener algo muy insignificante para tomar de manera competitiva y seria."

"Creo que entre más pequeño es el asunto, más le emociona."

his "No es una competencia. ¿Quieres convertirlo en un concurso? Yo no."

"Casi olvido añadir la última parte, la parte más importante."

show shizu behind_smile
with charachange

ssh "… Bueno, está bien. Quedan muchos días en el año escolar, me cansaría de eso de todos modos."

"Con eso, Shizune toma su jugo y se lo termina. Me pregunto si ella va a intentar lanzar el envase vacío a la basura, pero no lo hace. De hecho, ella parece perpleja en cuanto a por qué parezco tan decepcionado. Será mejor que vaya al grano."

his "Solo quería hablar. Nuestras vacaciones prácticamente están aquí, ¿sabes?"

his "Y deberíamos pasar más tiempo juntos, de todos modos. Estaba pensando que podríamos hacer eso durante el verano."

show shizu adjust_blush
with charachange

"El rostro de Shizune se pone tan rojo como debe estar el mío, y comienza a ajustar sus anteojos, nerviosa. Vaya gesto multiuso. Ella tamborilea sus dedos juntos, pensativa, considerando sus siguientes palabras con cuidado."

show shizu basic_normal
with charachange

ssh "¿Te refieres a una cita?"

his "Solo porque vamos a salir a alguna parte, ¿eso inmediatamente lo convierte en una cita?"

show shizu behind_blank
with charachange

ssh "¿No lo es?"

show shizu adjust_frown
with charachange

ssh "Quiero que sea una cita."

his "Entonces es una."

show shizu basic_happy
with charachange

"Shizune aplaude con aprobación una vez, antes de añadir a mi declaración:"

show shizu behind_blank
with charachange

ssh "Pero no hoy."

show shizu basic_normal2
with charachange

ssh "Me voy por una semana a visitar a mi familia."

"Esa es una manera extrañamente formal de decirlo, y por esa razón, mi interés se despierta."

"Tal vez su familia es del tipo formal y correcto, que vive en una mansión gigante y antigua con un arroyuelo y un estanque koi, donde todos usan kimonos todo el tiempo."

"Es una suposición salvaje, pero es divertido especular a veces. Me pregunto si Shizune simula la apariencia de ser una buena hija, tranquila y madura como Lilly, cuando está con su familia."

"No puedo imaginarlo, pero si hay siquiera una posibilidad de que sea cierto, entonces tengo que verlo."

his "¿Solo una semana? El viaje no debe ser tan lejos, entonces."

show shizu behind_frustrated
with charachange

ssh "Por supuesto que no, ellos aún están en Japón, después de todo."

his "En serio…"

show shizu adjust_happy
with charachange

ssh "No es como si pudieras venir conmigo. ¿Eso es lo que estás intentando decir?"

his "¿Por qué no puedo?"

show shizu basic_normal2
with charachange

ssh "No es como si lo disfrutarías."

his "Eso no lo sabes. Podría ser divertido."

his "Ah, casi lo olvidé: no respondiste a mi pregunta. ¿Vas a ir sola, o Misha va contigo? ¿Tu familia sabe de señas?"

show shizu behind_blank
with charachange

ssh "Misha va a ir también."

"La parte de la pregunta que queda sin responder es la más reveladora."

"Si la familia de Shizune no puede comunicarse con ella, tengo que preguntarme cómo fue su infancia. Probablemente escribía todo en esa libreta que lleva consigo y que todavía saca de la nada a veces."

"Por lo general, es cuando ni Misha ni yo estamos cerca. Puedo verla desde lejos cuando la saca como un último recurso, haciendo muecas todo el tiempo."

his "Si Misha va, entonces yo voy a ir, también."

show shizu basic_normal
with charachange

ssh "¿Te gusta Misha?"

his "Es cuestión de principios."

"Considero la idea de que Shizune pueda de hecho estar celosa, pero lo dudo. Ella por lo general luce sus emociones muy claramente en su rostro, y no veo nada que apoye mi teoría ahora mismo."

show shizu adjust_frown
with charachange

ssh "Creo que solo estás aburrido."

show shizu behind_smile
with charachange

ssh "Pero está bien. De acuerdo, iremos todos juntos. Es lo que deseaba desde el principio."

show shizu adjust_smug
with charachange



ssh "Hoy no puedes escaparte del consejo estudiantil para preparar tus valijas, solo porque vas a venir con nosotras con tan poca antelación, ¡no es excusa!"

his "Está bien, apenas tengo cosas para empacar de todos modos."

show shizu basic_normal
with charachange

"Shizune hace una pausa, juntando sus dedos pensativamente."

show shizu behind_blank
with charachange

ssh "Debiste haber venido a esta escuela con muy poca antelación."



label es_S17a:

"Podría ser que ella esté recordando la vez cuando Misha y ella se metieron inesperadamente a mi habitación y alcanzaron a ver todos mis medicamentos. Ese fue un momento incómodo que me gustaría olvidar, y no me gusta recordarlo."

"La manera como ella anda de puntillas alrededor del tema incluso ahora solo me hace sentir más incómodo."


label es_S17x:

his "Así fue. Fue como una decisión en el acto. Sin embargo, resultó mejor de lo que esperaba."

"Espero que Shizune no continúe con ese asunto, y para mi alivio, no lo hace."

show shizu adjust_happy
with charachange

ssh "Mi casa está en una zona especialmente bella de Saitama."

show shizu behind_smile
with charachange

ssh "Nos iremos temprano en la mañana, así que prepárate. Vamos a hablar de eso más tarde, ¿bueno? Por ahora, esos folletos no se revisarán solos, y tú vas a ayudarme."

stop music fadeout 3.0

hide shizu
with charaexit

"Mientras Shizune se aboca de lleno en su trabajo, arrastrándome con ella, creo que parece casi, pero no del todo, emocionada por ir."

scene black
with dissolve



label es_S18:

scene bg school_dormhallway
with locationchange

play music music_daily fadein 0.5

"Cuando Shizune y Misha llegan temprano a la mañana siguiente para recogerme, están vestidas en algo distinto al uniforme escolar que me había acostumbrado a ver."

show shizu behind_blank_cas at center
with charaenter

"Tiene sentido, ya que estamos en vacaciones, pero aun así es chocante. El vestido de Shizune es elegante y a la moda, casi demasiado para un lugar tranquilo como Yamaku."

"Recordando lo que llevó en el festival de Tanabata, estoy comenzando a notar una tendencia en ella."

"Todas sus ropas son maduras y de muy buen gusto; muy bien elaboradas. Así que, entonces, me pregunto por qué ella misma es tan inmadura."

show bg school_dormhallway at bgright
show shizu behind_blank_cas at tworight
with charamove

show misha perky_smile_cas at twoleft
with charaenter

"Bueno, al menos la ropa de Misha refleja su yo interior por fuera."

show shizu adjust_frown_cas
with charachange

ssh "Estás trayendo muy poco."

hi "Dije que lo haría. Dije que no había mucho para empacar."

show shizu basic_frown_cas
with charachange

"Shizune hace pucheros y sacude con el pie su propia colección de equipaje, bastante grande, como si estuviera avergonzada. Misha solo trae una maleta consigo, pero es casi más grande que ella. Se ve acomplejada por ello también."

"Dios, esa maleta es tan grande como un auto compacto. El color verde guisante también es inquietante. Parece algo usado para transportar cadáveres. La manera como se ven ahora mismo me hace querer molestarlas un poco."

hi "Oh, eso es mala suerte para ti y para Misha, ¿no es así? Tener que cargar esas enormes maletas. Tienen que empacar ligero la próxima vez, como yo. Todo cabe en una maleta pequeña."

show misha hips_grin_cas
with charachange

mi "¡Como James Bond~!"

hi "Sí, exactamente como James Bond."

show shizu adjust_frown_cas
with charachange

shi "…"

"Shizune suavemente tira de sus anteojos en concentración."

show shizu basic_normal_cas
with charachange

ssh "Deberíamos dividir la cantidad que llevamos por igual."

show misha sign_smile_cas
with charachange

mi "¡Vaya~! ¡Es una gran idea, Shicchan~!"

hi "¿Qué? No."

show shizu adjust_smug_cas
with charachange

ssh "Nos beneficiaría a todos nosotros."

show misha cross_laugh_cas
with charachange

mi "¡Síp~! ¡Guajaja~!"

hi "Voy a tener que decir que no."

show shizu cross_angry_cas
with charachange

ssh "¡Eres minoría!"

"Ella casi se lanza hacia adelante cuando lo dice en señas. Aterrador."

hi "Ah, bueno. Solo estaba bromeando. No me importa llevar un poco extra. Solo pensé que sería divertido jugar con ustedes dos."

hi "Pero, si iban a intentar hacerme llevar todo, iba a montarme sobre esa gigantesca maleta verde montaña abajo como un trineo."

show shizu adjust_smug_cas
with charachange

shi "…"

"Eso parece hacer reír a Shizune, y levanta una mano hacia su boca para contenerla. Es como si la estuviera escondiendo. Me pregunto si ella puede reír. Si no, eso puede ser el porqué ella hace eso. Como que me hace sentir triste."

stop music fadeout 3.0

scene bg city_station
with locationskip

"Habiéndonos ocupado de eso, nos dirigimos a la estación del tren, y sigue un paseo muy tranquilo."

"Shizune y Misha logran quedarse dormidas casi al instante, pero yo me encuentro incapaz de hacerlo. Eso nunca me ha pasado antes. Quizás es mi medicamento."

scene bg shizu_houseext
with shorttimeskip

play music music_soothing fadein 0.5

"Cuando llegamos a la casa de Shizune, es mucho más grande de lo que imaginé que sería. No creo que enorme sea una exageración."

hi "¿Vives en una mansión?"

show shizu cross_angry_cas at center
with charaenter

"Shizune se para en la punta de sus pies, indignada, para que estemos al nivel de nuestros ojos, y frunce el ceño profundamente, después de que mi comentario es traducido por Misha. Es como si dijera, “¿cómo puedes decir algo así?”."

show shizu basic_frown_cas
with charachange

ssh "Esta es solo una casa normal. Nada tan ostentoso como una mansión."

"Creo que nuestras definiciones de esos términos son bastante diferentes, entonces."

show bg shizu_houseext at bgright
show shizu basic_frown_cas at tworight
with charamove

show misha hips_grin_cas at twoleft
with charaenter

mi "Guajaja~. Hicchan, ¿estás sorprendido? ¿Quieres que te muestre dónde te vas a quedar?"

show shizu behind_blank_cas
with charachange

ssh "Creo que tenemos una habitación de huéspedes, pero no estoy segura de si tenemos dos. Iré a revisar."

show misha sign_smile_cas
with charachange

mi "Hm~, ¡pero no es problema, Hicchan~! Shicchan y yo podemos compartir una habitación si es necesario. Bueno~, a menos que la suya esté siendo utilizada para algo más."

hide shizu
with charaexit

hide misha
with charaexit

stop music fadeout 5.0

"¿“No estoy segura”? Estoy comenzando a pensar que Shizune no pasa mucho tiempo en casa. Antes de que pueda hacer una broma al respecto a costa de ella, Shizune se desvanece en la casa, y Misha va con ella, dejándome solo en el jardín."

"No quiero seguirlas adentro todavía. Dejo mi maleta junto a la puerta principal, y aprovecho la oportunidad para mirar los jardines, simplemente dando una vuelta rápida alrededor de la casa."

show hideaki bored at center
with shorttimeskip

"Aunque toma solo unos minutos, cuando regreso lo primero que noto es que mi maleta no está, y una pequeña niña está en su lugar. Se parece mucho a Shizune, aunque Shizune no usaría pantaloncillos cortos rojos ni medias con estrellas y lunas."

hi "¡Hola! ¿Eres la hermana menor de Shizune o algo así?"

show hideaki normal
with charachange

hh "No. Soy su hermano menor. Mi nombre es Hideaki."

show hideaki thinking
with charachange

hh "Gusto en conocerte."

play music music_happiness fadein 2.0

"La voz que responde es directa, monótona, y también sin duda masculina. Me siento avergonzado hasta el punto en que casi podría darme la vuelta e irme ahora mismo, si pudiera recordar el camino de regreso al tren."

show hideaki serious
with charachange

hh "¿Eres la segunda persona que mi hermana trajo con ella?"

hi "“¿Trajo con ella?”. No soy equipaje."

hi "En fin, soy Hisao. ¿Tú tomaste mi maleta?"

show hideaki triangle
with charachange

hh "Sí, es mi derecho quedarme con cualquier cosa que encuentre en mi propiedad."

hi "No, no lo es. Así no es como funciona en absoluto."

"Supongo que incluso los niños pequeños y particularmente bienhablados creen en la ley de “el que se lo encuentra, se lo queda”. Aunque lo llamo pequeño, no parece tan joven, ahora que lo pienso. Tal vez dos o tres años más joven, como mucho."

show hideaki normal
with charachange

hh "Se la di a Shizune. Está adentro. ¿Estás en el consejo estudiantil?"

hi "Sí, ¿cómo supiste? ¿Ella saca el tema a menudo?"

"Casi digo “¿ella habla de eso a menudo?”. Eso podría haber sido malo."

show hideaki bored
with charachange

hh "Sí, todo el tiempo. ¿Te llevas bien con ella?"

hi "¿Llevarme bien? Esa es una pregunta extraña. No estaría en el consejo estudiantil si no pudiera llevarme bien con ella. Qué hay de ti, ¿ustedes dos se llevan bien?"


"Aunque tiene una voz monótona, su rostro es tan expresivo como el de Shizune, y contradice lo que realmente siente. Debe ser cosa de familia. Parece que él no está feliz con mi pregunta, por cualquier razón."

show hideaki thinking
with charachange


hh "Lo siento. Solo estaba preguntando porque ustedes dos actúan muy parecido."

"No sé por qué, pero se siente como si me estuviera tomando el pelo. Desafortunadamente, funciona. No me gusta ser comparado con Shizune."

hi "Tú eres más como Shizune, pero eso es de esperarse. Hasta te confundí con su hermana menor. Si no quieres que la gente cometa ese error, deberías vestir más apropiadamente."

show hideaki confused
with charachange

hh "No entiendo, mi ropa va acorde con la temporada."

hi "¿Qué hay de las medias?"

show hideaki angry_up
with charachange

hh "Están a la moda."

show hideaki disapproves
with charachange

hh "Actúas como mi hermana. Al final la gente comenzará a confundirte con ella."

"Supongo que mi comentario lo golpeó más duro de lo que pensé. Eso explicaría este intento de darle la vuelta."

hi "Odio ser comparado con otras personas."

show hideaki evil
with charachange

hh "A Shizune tampoco le gusta cuando es comparada con otras personas."


"Había pensado que Hideaki era un poco más maduro que Shizune, pero ellos tienen la misma vena competitiva y la misma inclinación por provocar a la gente. Me pregunto si él es así debido a Shizune, o si es al revés."

hi "Y tampoco a ti, ¿cierto? Muy bien, lo entiendo. No debería ser tan mezquino."

show hideaki normal
with charachange

stop music fadeout 4.0

"Especialmente con niños pequeños. Hideaki parece aceptar esto como un reconocimiento de derrota, lo cual es algo que siento que no puedo dejar ir. Sin embargo, solo tendré que dejarlo ir mientras tenga la oportunidad."

scene bg shizu_living
with locationchange

"Puedo oír la risa de Misha rebotando por los pasillos al momento que entro por la puerta de la casa, y la sigo hacia lo que supongo sería la sala de estar. Tiene más personas de las que esperaba."

show lilly basic_displeased_cas:
    center
    ypos 1.17 xpos 0.55
show akira basic_boo:
    tworight
    ypos 1.15 xpos 0.72
show hideaki bored:
    center
    xpos 0.92
    easein 1.0 ypos 1.1
show shizu behind_blank_cas:
    twoleft
    ypos 1.11 xpos 0.27
show misha perky_smile_cas:
    center
    ypos 1.1 xpos 0.08
with charaenter

play music music_another fadein 4.0

"Entre ellos veo una cola de caballo rubia, distintiva y familiar. Estoy más confundido que sorprendido en cuanto a por qué Lilly está aquí. Lilly tampoco se ve eufórica por este encuentro casual."

"Sentada junto a Lilly está una mujer alta y de aspecto andrógino en un traje elegante. Me gustaría asumir que es su hermana mayor, pero no quiero correr el riesgo."

show lilly basic_listen_cas
with charachange

li "No esperaba que llegaras tan pronto."

"Al inicio creo que ella me está hablando, pero resulta que se está refiriendo a Shizune. No creo que Lilly ni siquiera note mi presencia. Claramente las sorprendí en medio de la conversación, y parece que con su enfoque en Shizune, ella no podría oírme."

show shizu basic_frown_cas
with charachange

ssh "Debería haber reorganizado mi horario completo por ti."

show misha sign_smile_cas
with charachange

mi "Shicchan dice: ¡Debería haber reorganizado mi horario solo por ti~!"

show lilly basic_displeased_cas
with charachange

li "Eso habría estado bien, pero no esperaría que hicieras algo así."

show misha hips_smile_cas
with charachange

mi "¡Oh, hola, Hicchan~! Finalmente estás aquí."

hi "Sí. Hola, Lilly."

show lilly basic_surprised_cas
with charachange

li "Oh, ¿Hisao? Esta es una gran sorpresa. Akira, él es Hisao, un compañero de clases. Hisao, ella es Akira, mi hermana."

show akira basic_smile
with charachange

aki "Qué hay."

"Ella levanta la mano en un gesto de saludo breve y bastante casual. Así que es la hermana mayor después de todo."

show akira basic_boo
show lilly basic_weaksmile_cas
with charachange

aki "Espero que no vayamos a estropear ninguno de sus planes. Ya que solo vamos a estar aquí por un día más, Lilly y yo pensamos que ella bien podría venir conmigo."

"Akira se voltea hacia mí, como si se sintiera obligada a explicar. Estoy agradecido por eso."

show akira basic_ending
with charachange

aki "Supongo que mi posición aquí sería mejor descrita como una niñera."

show hideaki disapproves
with charachange

"Akira despeina el cabello de Hideaki mientras él continúa con su pasatiempo de verse disgustado."

hh "Eso es humillante."

show akira basic_smile
with charachange

aki "¿En serio? Cambiaré mi título una vez tengas unos cuantos años encima. O al menos unos cuantos centímetros."

"Ellos hacen una pareja interesante, aunque Akira se ve más como una abogada que como una niñera. Sin embargo, todavía no estoy muy seguro de por qué ella y Lilly están aquí."

"Echando un vistazo alrededor de la sala, hay raquetas de tenis, palos de golf, e incluso una pila de cañas de pescar y cajas de aparejos ocultos aquí y allá."

"Detrás de cada silla, en cada esquina, y bajo cada mesa hay alguna pieza de equipo al aire libre aficionado. Recojo una de las cañas de pescar y juego con ella."

hi "Esta es una casa bonita."

hi "Shizune, parece que tu papá tiene muchas aficiones."

show misha sign_smile_cas
with charachange

show misha perky_smile_cas
with charachange

"Por un momento olvido hacer las señas de lo que digo, pero Misha ya está en el proceso de interpretar lo que dije para ella. Aún estoy un poco impresionado en lo automática que es la interpretación para Misha."

show hideaki normal
with charachange

hh "¿Tú pescas?"

hi "No, no sé cómo. Como que quiero aprender, ya que oí que es relajante."

show shizu behind_blank_cas
with charachange

ssh "Hay un río a solo una corta distancia en auto, toda mi familia sabe cómo pescar. Si quieres, podríamos ir allí algún día."

show akira basic_laugh
with charachange

aki "¿Hideaki y tú pueden pescar? No esperaba que gente de su edad lo supiera, considerando que siempre parecía un pasatiempo para ancianos."

show akira basic_ending
with charachange

aki "Saben, Lilly es estupenda en la cocina. Si tuviéramos algo de pescado fresco…"

"No es difícil seguir la línea de pensamiento de Akira."

show lilly basic_displeased_cas
with charachange

li "Si quieren comer pescado, podríamos ir a la tienda."

"La voz de Lilly suena ligeramente más autoritaria de lo normal. Ella realmente no parece compartir el entusiasmo de su hermana por la idea."

show shizu basic_happy_cas
with charachange

shi "…"

show misha hips_grin_cas
with charachange

mi "Es más divertido ir a pescar; ¡incluso podríamos convertirlo en un juego e intentar ver quién atrapa el más grande~! Eso sería emocionante, ¿cierto? ¡Sí~! Hicchan, ¿qué piensas? Suena divertido, ¿no es así?"

hi "Sí, sin duda podría serlo."

show akira basic_smile
with charachange

aki "Me parece una buena idea. Tampoco sé cómo pescar, así que ahora es un momento tan bueno como cualquier otro para aprender."

show akira basic_boo
with charachange

"Sus ojos se mueven hacia Lilly, quien permanece impasible. Esto amarga un poco la sonrisa de Akira, y me hace preguntar por qué Lilly está siendo tan obstinada al respecto."

show hideaki normal
with charachange

hh "No creo que tengamos suficiente equipo de pesca para todos."

show shizu behind_smile_cas
with charachange

ssh "Podemos tomar turnos. Será una batalla de equipos."

show hideaki confused
with charachange

hh "¿Ella qué está diciendo?"

hi "Podemos tomar turnos. Ella también quiere que sea un concurso."

show akira basic_laugh
with charachange

aki "Vamos Lilly, bien podríamos sacarle el máximo provecho a esto."

show akira basic_boo
with charachange

aki "¿Así que esto va a ser una competencia para ver quién puede atrapar el pez más grande, o la mayor cantidad?"

show shizu adjust_smug_cas
with charachange

ssh "Parece que la hermana mayor entiende mejor, como siempre."

show shizu basic_normal_cas
with charachange

shi "…"

show misha sign_smile_cas
with charachange

mi "Shicchan dice que supone que Lilly preferiría ir a la tienda, ¿cierto~? ¡Es mucho menos trabajo, así que es natural que ella lo prefiriera! Pero ir a pescar sería más divertido, y ahorraríamos dinero. ¡Akira, tienes la idea correcta~!"

show akira basic_smile
with charachange

"Akira da una sonrisa cortés, aunque un poco forzada. El elogio de Shizune no era su objetivo, después de todo."

show lilly basic_sleepy_cas
with charachange

li "…"

show lilly basic_weaksmile_cas
with charachange

li "¿El río no queda muy lejos?"

show akira basic_ending
with charachange

aki "No creo que sea tan lejos, y puedo conducir si tenemos que hacerlo. Me parece bien, siempre y cuando atrapen algo."

hi "¿A tu auto le puede caber tanta gente, además de todo el equipo de pesca?"

show akira basic_boo
with charachange

"Ella frunce sus labios mientras sus dedos se mueven sutilmente, contando la cantidad de pasajeros y la carga requerida. Si vamos a ir Shizune, Misha, Lilly, Akira, Hideaki y yo…"

show akira basic_lost
with charachange

aki "Seis personas. Maldición, mi auto solo puede llevar cinco."

show akira basic_ending
with charachange

aki "De hecho, si Hideaki se sentara en mi regazo, podríamos—"

show hideaki angry_up
with charachange

hh "No me voy a sentar en tu regazo."

show akira basic_resigned
with charachange

aki "Oh."

show shizu adjust_happy_cas
with charachange

shi "…"

show misha hips_smile_cas
with charachange

mi "Shicchan dice que el auto de su padre sería lo suficientemente grande."

show akira basic_lost
with charachange

aki "¿Qué, el Fuga? Si a él no le molesta que lo usemos, entonces supongo que no tenemos otra opción. Se siente un poco mal abandonar mi auto, considerando que no lo tendré por mucho tiempo."



"Pese a la obstinación de Lilly, y a las preguntas de Hideaki sobre si preferiríamos comer primero que apostar una cena de pescado que podría no materializarse, no hay modo de disuadir a Akira y a Shizune mientras discuten sobre el plan de transporte."

stop music fadeout 5.0

scene ev shizune_car
with shorttimeskip

play ambient sfx_businterior fadein 1.0

"Mis expectativas de un recorrido algo relajante en auto por el campo se cumplen. La forma de conducir de Akira es tan tranquila y relajada como los alrededores, hasta el punto que Misha se queda dormida durante el viaje."

"Pensé que este viaje habría sido demasiado lento para el gusto de Shizune, pero parece disfrutarlo genuinamente. Incluso con Hideaki incómodamente apretujado entre ella y la puerta, ella solo sigue mirando por la ventana y sonriendo."

stop ambient fadeout 0.5

scene bg shizu_fishing at left
with shorttimeskip

play ambient sfx_parkambience fadein 0.5

"La zona alrededor del río es muy bonita. Akira y Shizune se van al río tan rápidamente que no tenemos más opción que perseguirlas. De lo contrario, nos habríamos quedado comiendo polvo."

show lilly basic_weaksmile_cas at left
show hideaki bored at center
show misha hips_grin_cas at right
with charaenter

"Puedo ver que Hideaki y Lilly solo están complaciendo a sus hermanas, con Lilly siendo la menos entusiasta de los dos. Sin embargo, Misha parece tan feliz como siempre. Parece que ha logrado aferrarse a un poco de la emoción de Shizune y Akira."

"En cuanto a mí, preferiría comer ahora, pero la idea de pescado fresco preparado por Lilly es atrayente."

"El río es más grande de lo que imaginé, aunque muy pintoresco y pacífico. Aparte de un pequeño muelle al parecer construido solo para pescar, este lugar parece intacto por la civilización, y me doy cuenta de cuánto verdor he visto últimamente."

show shizu invis at offscreenright
show akira invis:
    center
    xpos 1.5
with None

show bg shizu_fishing at right
show lilly invis at Position(xpos=-0.6)
show hideaki invis at offscreenleft
show misha perky_confused_cas at left
show shizu basic_happy_cas:
    center
    xpos 0.37
show akira basic_smile:
    center
    xpos 0.8
with Dissolvemove(1.5)

"Shizune aparta a Misha para que puedan explicarle a Akira cómo pescar. Hideaki y Lilly están hablando entre sí, así que decido unirme al trío entusiasta."

show akira basic_ending
with charachange

aki "Hmm… ¿así que cuál de estos señuelos debería usar, entonces? ¿Puedo usar este pequeño y bonito?"

show shizu basic_frown_cas
show misha sign_smile_cas
with charachange

mi "¡Espera, espera~! ¡Este es un concurso, necesitamos elegir los equipos primero! Shicchan y yo estaremos en un equipo, por supuesto. Hicchan, vas a estar en nuestro equipo, ¿cierto? ¡Podemos ser el equipo del consejo estudiantil~!"

hi "Muy bien."

show akira basic_laugh
with charachange

aki "Muy bien, entonces. Con eso somos Hideaki, Lilly y yo en el otro equipo. Lilly, ¿cómo deberíamos llamarnos?"

stop music fadeout 2.0

play sound sfx_flash

show bg shizu_fishing at left
show lilly basic_sleepy_cas at twoleft
show hideaki bored at tworight
show misha invis at Position(xpos=0.85)
show shizu invis at offscreenright
show akira invis:
    center
    xpos 1.5
with Dissolvemove(0.5)

$ doublespeak (li, hh, u"No veo por qué sea importante.", "No creo que importe.")

play sound sfx_flash

show bg shizu_fishing at right
show lilly invis at Position(xpos=-0.6)
show hideaki invis at offscreenleft
show misha perky_confused_cas at left
show shizu basic_angry_cas:
    center
    xpos 0.37
show akira basic_ending:
    center
    xpos 0.8
with Dissolvemove(0.5)

show akira basic_lost
with charachange

aki "Es el equipo Sin Entusiasmo…"

play music music_comedy fadein 0.5


"Una vez más, los mejores esfuerzos de Akira son rechazados. A Shizune y Misha, por otra parte, no les falta el entusiasmo en absoluto."

show misha hips_smile_cas
show shizu behind_frown_cas
with charachange

ssh "¡Hisao! Tú puedes ser nuestro hombre clave, por favor esfuérzate en atrapar tantos peces como sea posible, o el más grande."

hi "¿Por qué yo? Nadie me ha enseñado cómo pescar todavía."

show misha hips_grin_cas
show shizu behind_blank_cas
with charachange

mi "Podemos hacerlo ahora~."

"Después de un rápido tutorial, Shizune inmediatamente intenta meternos en una discusión sobre la estrategia en una competencia de pesca en equipo."

"De alguna manera, la competencia no parece particularmente aplicable a un deporte donde pasas horas sentado y esperando a que un pez muerda un gusano."

show shizu adjust_happy_cas
with charachange

ssh "Parece que a Hideaki le quedó la caña de repuesto. Sabes que solo es una cuerda atada a un palo de bambú, ¿cierto? Eso significa que al momento de decidir el orden, tú deberías competir contra él."

hi "¿Qué, por qué yo?"

show misha sign_smile_cas
with charachange

mi "Tú eres el que tiene menos experiencia aquí, Hicchan~."

hi "¿Sí? ¿Así que quién es la mejor aquí? ¿Shizune? Hideaki es tu hermano, probablemente es igual de bueno. Probablemente pesca todo el tiempo, ya que él vive cerca de un lago. Podría incluso ser mejor."

show akira basic_annoyed
with charachange

aki "Mirarlos a ustedes tres me hace doler la cabeza. Saben que solo estoy oyendo dos tercios de la conversación, ¿cierto? ¿De qué se trata?"

hi "Escoger nuestra alineación."

"Akira pone cara de preocupación. Ella se está poniendo impaciente, lo cual probablemente no es muy irrazonable."

show shizu basic_sparkle_cas
with charachange

ssh "Si estás impaciente, eso solo me emociona más. Ahora quiero aumentar la apuesta."

show akira basic_lost
with charachange

aki "¿Ella qué está diciendo?"

hi "Quiere aumentar la apuesta."

show akira basic_laugh
with charachange

aki "Yo no estaría tan apresurada; tenemos suerte de principiante dos veces de nuestro lado, después de todo. La única manera de que puedas superar eso es capturando un océano entero."

show shizu adjust_happy_cas
with charachange

shi "…"

show misha hips_grin_cas
with charachange

mi "Este es un cuerpo de agua dulce, bióloga marina~."

"Un insulto extraño, entregado con un júbilo imperturbable e inocente. Akira no parece molestarse. Se lo toma a risa, y Shizune se parece nuevamente a su usual y traviesa forma de ser. Me alegra que se lleven bien."

show akira basic_smile
with charachange

aki "¿Entonces vamos a elegir equipos, o qué? Estoy un poco hambrienta…"

show shizu basic_normal_cas
with charachange

ssh "Hisao, Misha, y yo estamos en un equipo, y Lilly, Hideaki, y tú están en el otro, ¿no es así?"

show akira basic_ending
with charachange

aki "Supongo que ese es el arreglo más obvio. ¿Pero no sería más divertido mezclarlos un poco? ¿Eh?"

show misha perky_smile_cas
with charachange

mi "Hmm~, ¿no quieres pescar con tu propia hermana?"

show akira basic_boo
with charachange

aki "Bueno, ninguna de nosotras sabe cómo pescar, así que ponernos a las dos en el mismo equipo es algo…"

"Bueno, suena como si hubiera oído algo un poco peligroso. Intento cambiar el tema antes de que Shizune pueda convertir esa mirada incrédula en su rostro en algo más."

hi "Así que, ¿supongo que Shizune y tú se conocen?"

show akira basic_smile
with charachange

aki "Claro que sí. Nos conocemos desde hace mucho tiempo."

show shizu basic_normal2_cas
with charachange

"Akira le lanza una sonrisa cómplice a Shizune. No es hasta que Misha ha terminado de traducir lo que ella dijo que Shizune pone cara de preocupación."

"Akira sin duda es diferente de Lilly. Aparte de su apariencia, ella es mucho más informal y relajada. Esperaba que toda la familia de Lilly fuera correcta y formal como ella, así que esto es una sorpresa. Pero, siento que es fácil hablar con ella."

show akira basic_laugh
with charachange

aki "Por más que me guste hablar de atrapar peces, seguramente deberíamos hacerlo en algún momento."

show shizu behind_blank_cas
with charachange

ssh "¿Sugerirías que debería haber una alineación, como en el beisbol? ¿O debería ser todos a la vez, o estilo batalla de relevos?"

show shizu basic_sparkle_cas
with charachange

ssh "¿Todos pueden sentarse donde quieran, o los equipos tienen que estar juntos? ¿Anunciamos dónde pescamos? ¿Qué tamaños de peces estaremos contando?"

show akira basic_lost
with charachange

"Al ver a Akira gemir después de que Misha obedientemente traduce para ella, Shizune frota sus anteojos, riendo en silencio."

show shizu adjust_happy_cas
with charachange

stop music fadeout 4.0

ssh "No importa. Vamos a pescar, entonces."

show shizu behind_smile_cas
with charachange

ssh "Puede ser un concurso individual."

stop ambient fadeout 2.0

scene ev shizu_fishing_ah
with shorttimeskip

play music music_ease

"Me siento, listo para pescar, aunque no me siento muy confiado. Todos los demás ya están sentados, excepto Akira, quien toma asiento junto a mí y lanza su sedal después de quitarse su saco y arremangarse."

"Hideaki y Misha terminan sentándose en la orilla y pescando juntos, ya que no hay suficiente espacio en el muelle para todos. A decir verdad, preferiría estar sentado junto a Shizune, pero Akira parece bastante accesible."

aki "Cuidado, estás un poco cerca. No enredes nuestros sedales, ¿de acuerdo?"

hi "Entonces, ¿nunca has pescado antes?"

aki "No, pero he visto cómo lo hacen en la televisión. Siempre quise atrapar uno de esos peces grandes con una espada en lugar de cara. Un marlín, creo."

li "Si no recuerdo mal, esos son del océano; son peces de agua salada."

aki "Eso lo sé. ¿Por qué todos actúan como si no supiera la diferencia entre los peces de agua dulce y los de agua salada?"

li "Si no tienes cuidado, espantarás a los peces, sean de agua salada o no."

"La voz de Akira es un poco fuerte entre sus esfuerzos por incitar a Shizune y entretener a Lilly, así que ella puede que tenga razón. Mi sedal no parece estar agarrando nada, pero no sé cuánto de eso se debe a Akira."

"Shizune hace todo lo posible para relajarse en el sol, y consigue simularlo muy bien, pero puedo notar que ella estaría un poco desanimada por no saber de qué se está hablando. No tener a Misha cerca puede ser un verdadero problema."

ssh "Hisao, ¿cuál es el resultado hasta ahora? ¿Vamos ganando? Espero que así sea, dado que te encomendé a ti el éxito del equipo."

"Logro hacer algunas señas incómodas ubicando creativamente mi caña. Probablemente esto es cercano a balbucear en términos del habla."

hi "Estás como, justo allí. ¿No puedes saberlo?"

ssh "Decepcionante; te dejas distraer. Tienes que concentrarte."

hi "Debí haberlo sabido. Bueno, está 0-0 en cualquier caso."

"Akira se ríe entre dientes, aunque es claro que eso realmente le bajó los humos."

hi "¿Son solo números ahora, o también estamos llevando un registro del tamaño?"

ssh "Ambos; asuntos de calificación."

hi "¿Quién va a calificarlos? ¿Eres una jueza de peces certificada?"

"Shizune niega con la cabeza para indicar que no lo es."

ssh "… Pero no parece que sea muy difícil. Dile a Misha que deje de sacudir las manos así, está espantando a todos los peces. Y pregúntale a Hideaki por qué ni siquiera se ha molestado en lanzar todavía."

"Echo un vistazo a los dos y grito lo que Shizune les dijo a ellos."

mi "¡Shicchan, creo que está molesto por haberse quedado con la caña de repuesto~!"

"Ya que Misha es, en gran medida, incapaz de hacer señas de manera coherente ahora mismo, solo recibe una mirada desconcertada de Shizune como respuesta. Shizune simplemente suspira después de que lo traduzco para ella."

aki "¡Oye, aunque estés deprimido por ello, tienes que intentarlo! Podrías atrapar el premio mayor, por lo que tú sabes. ¡Pero no atraparás nada a menos que lo hagas!"

"Siento que al menos la mitad de su apoyo se debe a que si Hideaki atrapa “el premio mayor”, ella quiere estar allí para comerlo, y tener a seis personas pescando solo lleva a mejores posibilidades de atrapar algo que tener a cinco."

"El ajetreo constante e incómodo que tengo que hacer para comunicarme con Shizune, sin mencionar que está cada vez más inquieta, me hace pensar que podría estar bien que ella tenga la oportunidad de pescar."

hi "Oigan, ¿podemos cambiar ahora?"

aki "Claro. ¿Lilly?"

li "No, no, por favor. No tengo idea de cómo pescar."

"Le digo en señas lo que dicen, dado que parece que he tomado el lugar de Misha como intérprete de Shizune en este momento."

ssh "Qué magnánimo de ti, Lilly."

"Oh cielos, aquí vamos. No me molesto en traducir lo que ella dice por temor a provocar otra pelea."

hi "Shizune dice que al menos deberías intentarlo. Hasta podría llegar a ser divertido."

li "Muy bien. Akira, ¿cómo usas esto?"

aki "Es bastante sencillo…"

"Me pregunto qué tan ético es cambiar intencionalmente y por completo lo que Shizune dijo de esa manera. Al menos valió la pena."

scene ev shizu_fishing_sl
with shorttimeskip

li "… Creo que entiendo. ¿Qué cebo crees que sería el mejor para usar? Preferiría algo que no lastimara mucho al pez."

aki "Si vas a meterle un anzuelo por la boca, no creo que el cebo vaya a lastimarlo mucho más."

hi "¿Y dejarlo ir…? No, no, no hagas eso."

li "Pero si no es grande, no tiene mucho sentido matarlo…"

"Con mis manos libres, es mucho más fácil para mí traducir lo que todos están diciendo. Ahora Shizune es la que tiene que lidiar con sus manos ocupadas, pero parece tomarlo con calma."

ssh "Eso es muy arrogante. Muy bien, sacaré del agua solamente a los grandes también, de ahora en adelante."

aki "¿Qué está diciendo?"

"Akira solo suspira después de que lo traduzco para ella."

aki "No, no me gusta ese “solamente”. Sabes, un pez es un pez, y tomas lo que puedes."

"Desafortunadamente, Shizune no puede oírla y Lilly no parece estar prestando mucha atención ahora."

"A Lilly se le está dando fácilmente la pesca; es una actividad muy relajante, después de todo. No pasa mucho antes de que ambas atrapen un pez, y sorprendentemente, Lilly está tan interesada como Shizune en saber cuál es el más grande de los dos."

stop music fadeout 3.0

"A medida que las horas pasan, parece que ellas incluso están comenzando a divertirse."

scene bg shizu_fishing_ss
with shorttimeskip

play ambient sfx_parkambience fadein 4.0
play music music_tranquil fadein 3.0

"Al final del día, tenemos varios peces de buen tamaño entre nosotros. Hasta Hideaki y Misha lograron atrapar uno. Nadie saca a relucir que estábamos compitiendo para ver quién podía atrapar más. No creo que a nadie le importe ya."

show akira basic_smile_ss at center
with charaenter

"Shizune y Misha están hablando entre ellas a cierta distancia, mientras Hideaki y Lilly están haciendo lo mismo. Decido aprovechar la tranquilidad del momento para hablar con Akira."

hi "Lilly y Shizune se llevaron bien hoy. En realidad no lo esperaba, después de ver cómo se tratan entre sí en la escuela."

show akira basic_boo_ss
with charachange

"Ella da un bufido entretenido. Parece que no se toma sus disputas tan seriamente como yo."

aki "Ellas tienen sus razones. Lilly y yo nos vamos mañana por un tiempo, así que estuvimos pensando en darles una visita."

show akira basic_ending_ss
with charachange

aki "Al final, me alegra que lo hayamos hecho."

"Después de un breve silencio, ella se estira en voz alta y luego aplaude para llamar la atención de todos."

show akira basic_smile_ss
with charachange

aki "Bueno, eso parece suficiente para alimentar a todos. Deberíamos regresar, ahora."

show bg shizu_fishing_ss at bgright
show akira basic_smile_ss at tworight
with charamove

show lilly basic_weaksmile_cas_ss at twoleft
with charaenter

"Lilly asiente con la cabeza, pero luego duda. Incluso con su rostro un poco ensombrecido, ella parece estar de mejor humor que esta mañana. Akira realmente parece saber cómo tratarla, y distendió su antipatía hacia Shizune muy bien."

show akira basic_ending_ss
with charachange

aki "La captura de hoy se ve deliciosa, como que desearía tener un poco de salsa de soya para poder comerla ahora."

show lilly basic_surprised_cas_ss
with charachange

li "Pensé que querías que yo lo cocinara…"

show akira basic_laugh_ss
with charachange

aki "¿No crees que comerlo crudo esté bien?"

"A pesar de las protestas, o las bromas de Akira, ya que no puedo saber cuál de las dos es, decidimos esperar para al menos cocinar el pescado antes de comerlo."

stop ambient fadeout 2.0

scene bg shizu_houseext_lights
with shorttimeskip

stop music fadeout 3.0

"Ya se ha hecho bastante tarde mientras estuvimos fuera, y para cuando regresamos a la casa de Shizune, es buen momento para la cena."

scene black
with dissolve



label es_S19:

scene bg shizu_guesthisao
with locationchange

play music music_pearly fadein 5.0

"Algunas de mis píldoras se esparcieron por todo el fondo de mi maleta, lo cual no noté hasta minutos antes de que estuviera listo para irme a la cama anoche. Pasé bastante tiempo sacándolas de mi equipaje."

"Para cuando me levanto, ya estoy comenzando el día con una migraña, gracias a la combinación de problemas para quedarme dormido y levantarme tarde."

scene bg shizu_living
show hideaki normal_up at center
with locationchange

"Cuando entro a la sala de estar, Hideaki está allí terminándose su desayuno. Con su tenedor elevado a medio camino de su boca, él parece inseguro sobre si debería seguir comiendo o saludarme. Tal vez debería salir de la sala."

show hideaki triangle
with charachange

hh "Buenos días."

hi "Buenos días."

show hideaki thinking
with charachange

hh "¿Qué crees que deberíamos desayunar?"


hi "¿“Deberíamos”? ¿Tú no estás desayunando ya?"

show hideaki normal
with charachange

hh "Sí. Todos los demás ya comieron."

"A pesar de eso, él repite su pregunta de nuevo. Solo está intentando ser amable. Es una manera extraña de demostrarlo, pero sin embargo se lo agradezco, y me estoy sintiendo con mucha hambre."

"Intento hacer algo de conversación con él mientras preparo mi desayuno, para llenar el silencio."

hi "Esa salida a pescar ayer fue divertida. ¿Los Hakamichi y los Satou a menudo se juntan así?"

show hideaki bored
with charachange

hh "No realmente."

hi "Ya veo."

"En realidad, no. Hay una breve pausa antes de que Hideaki se digne a ponerme un poco más al corriente."

show hideaki thinking
with charachange

hh "Asuntos familiares. Nuestros padres son cuñados, y no se agradan entre sí."

"Escuchar eso me da mucho qué pensar. Pone en contexto la manera como Shizune y Lilly lidian entre sí, y hasta me hace no querer involucrarme más."

hi "Ah. Los asuntos familiares pueden ser problemáticos."

show hideaki normal
with charachange

"Hideaki simplemente asiente mientras me siento en la mesa con mi desayuno. Desearía que fuera un poco más fácil conversar con él."

"Mientras estoy comiendo, noto que la casa parece extrañamente tranquila para un lugar en el que está Misha. Si Shizune y Misha ya desayunaron, no puede ser porque estén dormidas. Le pregunto a Hideaki dónde están."

show hideaki bored
with charachange

hh "Shizune y Misha se fueron a hacer algunos mandados para nuestro papá. A los comerciantes locales les gusta tratar con Misha, así que él insistió."

hi "Bueno, ella tiene una personalidad amable y alegre. Puedo ver por qué les gusta. Tal vez deberías comenzar a tomar lecciones de ella, podrías aumentar tus relaciones comerciales."

show hideaki confused
with charachange

hh "¿Hablas en serio?"

"Él parece hablar en serio. No sé qué tipo de relaciones de negocios necesitaría un niñito. Tal vez quiere tener la mejor venta de pasteles para recaudar fondos de todos los tiempos."

"Es una lástima que al final tendré que irme de aquí y no estaré para ver lo que sea que esté planeando."

"Me pregunto de nuevo qué tipo de persona es el papá de Shizune, aparte de ser relativamente apasionado por el aire libre. Lo que sé hasta ahora es que les pide a sus socios y a los amigos de su hija que le hagan favores."

"Estoy asumiendo que él es extremadamente tímido o extremadamente perezoso. Tal vez es demasiado pronto para hacer un pronóstico grosero, pero ciertamente explicaría en gran parte la personalidad de Shizune."

show hideaki triangle
with charachange

hh "¿Quieres ir a alguna parte?"

hi "No realmente. ¿Por qué, tú sí?"

show hideaki normal
with charachange

hh "Pensé que podría haber algún lugar al que quisieras ir. ¿No quieres hacer turismo, o comer en un restaurante específico?"

hi "No lo sé. Nunca he estado aquí antes."

show hideaki thinking
with charachange

hh "Ya veo."

"Estaba a punto de preguntarle sobre cómo era Shizune cuando era más joven, pero consiguió despistarme con solo una pregunta. Esta parece ser una conversación tan incómoda para él como lo es para mí."

hi "Vaya que estás ansioso por complacerme hoy. ¿Por qué estás siendo tan amable? ¿Estás mostrando tu lado amable secreto ahora que tu hermana no está por aquí?"

show hideaki bored
with charachange

hh "Tienes algo de razón. Shizune quería que te hiciera compañía hoy."

"No quiero molestarlo, e intento hacerle ver eso, pero Hideaki es tan terco como su hermana y siente como si ese fuera su deber. También parece estar intentando seriamente ser amable."

"Rápidamente, comienzo a darme cuenta de que la idea de Hideaki de diversión es pescar, coleccionar cámaras, y hacer juegos de palabras esotéricos."

"Pescar es divertido, pero es algo que preferiría hacer antes que hablar. Lo mismo ocurre con las cámaras; preferiría manejarlas que coleccionarlas."

"Esto es algo que Hideaki nota por su cuenta."

show hideaki normal_up
with charachange

hh "¿Estás aburrido?"

hi "No estoy aburrido en absoluto."

"Casi bostezo las palabras, así que Hideaki las ignora por completo."

show hideaki sad
with charachange

hh "Estás aburrido. Shizune dijo que te divirtiera, y creo que no sé cómo hacer eso."

hi "Estoy divirtiéndome."

show hideaki serious
with charachange

hh "No pareces divertirte."

hi "¡Lo estoy!"

show hideaki normal
with charachange

hh "¿Por qué gritas? Espero que no grites tanto cerca de Shizune."

"Es difícil saber si está bromeando. Sea como sea, estoy un poco sorprendido. Intento ignorar eso y cambiar el tema."

hi "¿Solo coleccionas cámaras, o también te gusta la fotografía?"

show hideaki bored
with charachange

hh "No realmente. Si así fuera, habría más fotos en esta casa de las que hay ahora. ¿Qué hay para tomarle fotos?"

hi "No lo sé. ¿Pájaros? ¿Arquitectura? ¿Uno de esos restaurantes de los que estabas hablando? Pensé que esta ciudad tenía montones de cosas interesantes. ¿Cómo puedes vivir en un lugar con tantas cosas para hacer y no hacer nada?"

show hideaki triangle
with charachange

hh "Pensé que no sabías qué había para hacer aquí. De repente tienes tantas ideas y eres una autoridad en lo interesante que es. Eres como nuestra junta de turismo. ¿Quieres ir a ver pájaros o edificios?"

hi "Está bien, está bien, no hay necesidad de que te enojes tanto."

show hideaki normal
with charachange

hh "… No estoy enojado. Solo creo que si te interesa tanto, entonces deberíamos ir a un parque de diversiones."

hi "¿Por qué?"

show hideaki confused
with charachange

hh "Para que así puedas divertirte. Será divertido."

"¿Él tendrá esta misma expresión monótona y seria en su rostro mientras estemos montando montañas rusas y torres de caída? Eso sin duda bajaría los niveles de diversión. La idea no me convence de que valga la pena el viaje."

hi "No lo sé, siempre me pareció que ir a un parque de diversiones implicaba pasar más tiempo esperando en filas que realmente haciendo cosas. Tendrías que ir más temprano solo para saltarte las filas."

show hideaki normal
with charachange

hh "¿Alguna vez has estado en uno?"

hi "No, pero parece que así es como es."

show hideaki bored
with charachange

hh "… Bien. ¿Qué tal un parque normal? Hay uno cercano donde a Shizune le gusta ir. Quizás esté allí, y pueda dejarte con ella."

hi "¿Qué quieres decir con “dejarme”? No soy equipaje."

show hideaki triangle
with charachange

hh "No quieres ir a un parque de diversiones. No sé qué hacer."

"Parece como si hubiera herido sus sentimientos al negarme a ir con él. Ya estoy racionalizando mi decisión. No me gusta esperar en filas. Sería muy parecido a una cita. Preferiría ir con Shizune. Sería muy agotador."

hi "No es nada personal, es solo que preferiría que Shizune me mostrara la ciudad."

stop music fadeout 2.0

"Y no creo que ir a un parque de diversiones con mi condición sea una buena idea."

scene bg shizu_park
with locationskip

play music music_soothing fadein 0.5

"El parque está tan cerca que su propiedad casi podría ser considerada una extensión del mismo. Ambos, este lugar y el jardín trasero de Shizune parecen casi iguales, excepto que el parque tiene bancos y más gente."

"Dicho esto, es muy agradable. Incluso hay gente paseando a sus perros, y niños volando cometas que pueden ser vistas a lo lejos dejándose llevar perezosamente de un lado a otro sobre los árboles."

"Podría sentarme aquí, en un lugar relajante y escénico como este, para siempre."

show hideaki bored at center
with charaenter

"Hideaki, por otra parte, parece estar extremadamente aburrido. Quiero picarlo con el dedo para ver si aún está vivo. Pero, ¿reaccionaría de todas maneras?"

hi "¿Estás aburrido?"

show hideaki normal
with charachange

hh "No. ¿Vas a trotar o a jugar frisbee con los perros como todos los demás? ¿Eso es lo que la gente hace en los parques?"

hi "Bueno, vas a los parques para regresar a la naturaleza y disfrutar del ambiente. Es por eso que trotas en el parque, en lugar de hacerlo por la acera o algo así. Puedes trotar en cualquier lugar."

hi "No puedo creer que esté teniendo esta conversación. ¿Cómo puedes no saber esto? No deberías haber sacado ese tema, es muy raro. ¿Nunca has oído hablar de que “los niños deberían ser vistos y no escuchados”?"

show hideaki bored
with charachange

hh "Sí."

show hideaki triangle
with charachange

hh "Mentí. Estoy aburrido. ¿Te gustaría jugar un juego?"

"Me quejo, de manera que se oiga, con la esperanza de que entienda que no quiero. A él no le importa. De hecho, ya está jugando con una baraja de cartas."

show hideaki serious
with charachange

hh "¿Por qué estás molesto? Es por eso que estamos aquí."

hi "Pensé que estábamos aquí para buscar a Shizune."

show hideaki happy
with charachange

hh "Exacto. Es por eso que deberíamos jugar un juego. Es una trampa para Shizune. Puedes atrapar cualquier cosa, incluyendo gente."

show hideaki thinking
with charachange

hh "Si competimos entre nosotros en un espíritu de competencia y de manera deportiva, ella vendrá aquí para retar al ganador, como un tiburón. Entonces la derrotaré como un cazador de safari. Y luego tomaremos una foto de la ceremonia de premiación."

"Los tiburones no van por ahí desafiando a la gente a juegos de azar como si fueran retadores de dojos."

hi "¿Cuándo trajiste esa cámara? De todos modos, no. Tengo suficientes juegos saliendo con tu hermana."

show hideaki normal
with charachange

hh "No, vamos. Será divertido. Podemos jugar ajedrez."

hi "Por favor, no. Además, jugar ajedrez en el parque es algo que los viejos hacen, como pescar. Vas a envejecer muy rápido si sigues haciendo todas estas cosas de viejos."

show hideaki darkside
with charachange

"Hideaki se congela como si yo de repente comenzara a hablar un idioma extranjero. Tal vez lo ofendí de nuevo. Tal vez él en secreto tiene 50 años y ha envejecido increíblemente bien. Que él sea el hermano de Shizune podría ser una pantalla."

show hideaki disapproves
with charachange

hh "¿Qué tal damas, o go? O incluso backgammon está bien, aunque no me gusta. Si los juegos de mesa no son lo tuyo, podemos jugar juegos de cartas. Cualquier cosa que no sea seven card, porque eso es para debiluchos."

show hideaki evil
with charachange

hh "¿Tienes miedo de que vayas a perder? Si puedes vencerme te daré dulces."

hi "Hideaki, eres igual que Shizune. Estoy comenzando a pensar que todo esto es un pretexto para jugar juegos."

show hideaki thinking
with charachange

hh "No. Eso no es cierto."

hi "¡Lo eres! Apuesto a que esa vena competitiva es genética. Te venderé a la ciencia."

show hideaki normal
with charachange

hh "Nadie puede poseer a un ser humano."

hi "¿Qué tal si mejor te enseño lenguaje de señas?"

hi "Cuando Shizune me preguntó si quería venir aquí, hablamos un poco, y parecía que tú y tu papá no usaban lenguaje de señas. Solo estoy suponiéndolo, pero si no lo usas, podría enseñarte un poco. Aunque no soy un experto."

hi "De todos modos, creo que podría ser bueno para ti que muevas más tus brazos."

"Él apenas mueve sus brazos. La mayor parte del tiempo solo cuelgan sin fuerzas a sus lados. Qué inquietante."

"Me ha estado molestando que toda la familia de Shizune aparentemente no sabe hacer señas. Me pregunto cómo hacía antes de conocer a Misha. ¿Contrataban traductores para ella? ¿Escribía todo en esa libreta que lleva consigo?"

"Lo segundo es lo más probable, o podría escribirlo en un teléfono. Eso explicaría por qué le desagrada tanto usar la libreta. Por triste que sea, como que puedo ver por qué Hideaki o su padre no se habrían molestado en aprender lenguaje de señas."

"Probablemente era demasiada molestia en ese momento. Es muy fácil pensar eso. Sin embargo, por lo que he visto hasta ahora, ninguno de ellos está resentido entre sí ni está demasiado afectado por eso."

"Podría ser que estoy pensando demasiado la situación."

hi "Vamos. Bueno, para ser honesto, yo mismo aún estoy aprendiendo lenguaje de señas. Traje todos mis libros conmigo para poder mantener el ritmo. Aun así, al menos puedo enseñarte el alfabeto. Es muy sencillo. Esto es “cometa”."

"Me siento muy cursi en este momento, y más aún cuando Hideaki me devuelve la mirada inexpresivamente, como si todo el concepto de aprender fuera extraño para él."

show hideaki bored
with charachange

hh "A Shizune también le gustaba volar cometas aquí."

"Este es su intento de salvar la conversación, y estoy feliz de ayudar."

hi "Pescar, ¿y ahora cometas, también? ¿A Shizune le gustan mucho todos estos pasatiempos relajantes?"

show hideaki thinking
with charachange

hh "Cometas de combate. De hecho, acerca de Shizune—{w=0.5}{nw}"

stop music fadeout 0.3

show misha cross_grin_cas behind hideaki:
    center
    ypos 1.1 alpha 0.0
    linear 0.2 ypos 1.0 alpha 1.0
show hideaki ohshit
with vpunch

"Hideaki se congela cuando Misha aparece detrás de él y pone sus manos sobre sus ojos."

play music music_comedy fadein 0.5

mi "¡Hola hola~! ¡Adivina quién~!"

"También parecía finalmente estar relajándose."

hi "Hola, Misha. ¿Shizune está contigo?"

mi "¡Hicchan, no lo estropees! No lo eches a perder, no arruines la sorpresa, ¿bueno~?"

show hideaki thinking
with charachange

hh "Misha."

show bg shizu_park at bgright
show hideaki normal at tworight
show misha perky_confused_cas at twoleft
with dissolvecharamove

mi "¡Bingo~! ¡Es correcto! Pero~, fue demasiado fácil, por alguna razón."

"No sé lo que quiere decir ella con “por alguna razón”."

show misha hips_frown_cas
with charachange

mi "¡Demasiada gente puede saber que fui yo! ¡Quiero sorprender a alguien! Estaba segura de que lograría engañar a Hideaki~. ¿Por qué no caíste, hm~?"

show hideaki bored
with charachange

hh "Eres la única persona que hace eso. Tú, y los secuestradores."

show misha cross_laugh_cas
with charachange

mi "¿En serio? ¡Guajaja~!"

show hideaki serious
with charachange

hh "¿Por qué te ríes?"

show shizu invis:
    center
    xpos 0.1
with None

show bg shizu_park at left
show misha cross_laugh_cas at Position(xpos=0.4)
show hideaki serious at Position(xpos=0.8)
show shizu basic_angry_cas at Position(xpos=0.2)
with dissolvecharamove

ssh "¿Le estás dando problemas a Hisao? Pensé que lo llevarías a algún lugar más emocionante que el parque. Ni siquiera está tan lejos de casa. Eres muy perezoso."

show misha hips_frown_cas
with charachange

mi "Hideaki, ¿le estás dando problemas a Hicchan? ¡Deberías haberlo llevado a un lugar más emocionante! El parque está muy cerca de casa, Shicchan dice que eres perezoso~."

show hideaki bored
with charachange

hh "Él quería venir aquí. ¿Por qué eres tan discutidora?"

show shizu behind_frown_cas
with charachange

ssh "Tengo que mantener a mi hermano menor a raya."

show hideaki triangle
with charachange

hh "¿Qué está diciendo?"

hi "Que tú debes ser mantenido a raya."

show hideaki serious
with charachange

hh "En serio…"

"Están listos para pelearse tan pronto. Por una parte, he oído que los hermanos que pelean mucho no son raros, y el hecho de que peleen en absoluto demuestra que debe haber algún nivel de comunicación en marcha. Así que, es bueno que se lleven bien."

scene bg shizu_houseext
with locationskip

stop music fadeout 4.0

"Discuten todo el camino de regreso a casa. Misha traduce para Shizune, y yo para Hideaki. Así que parece más como si nosotros fuéramos los que estamos discutiendo, excepto que no realmente. Nadie podría escuchar a Misha y creer eso."

"El día fue divertido al final, por lo menos."

$ suppress_window_after_timeskip = True

scene black
with dissolve



label es_S20:

window hide None

scene black
with dissolve

show bg shizu_guesthisao
with openeye

window show

"A pesar de haber estado aquí por solo dos días, se siente como si hubiera sido mucho más. Despierto sintiéndome más cansado que renovado. Quizás porque me he estado moviendo casi constantemente desde que llegué aquí."

"Sea cual sea la razón, me está haciendo levantar cada día inusualmente tarde. Me gusta dormir hasta tarde, pero podría ser un inconveniente si termina convirtiéndose en un hábito."

"Puedo oír una voz profunda y masculina gritando fuerte en el fondo. Debe ser el papá de Shizune. O tal vez, con el tamaño de este lugar, sus acreedores. Es más probable lo primero, ya que los gritos no parecen de enojo, solo fuertes."

scene bg shizu_living
show hideaki normal:
    center
    xpos 0.5
show misha perky_smile_cas:
    center
    xpos 0.3
show shizu basic_normal_cas:
    center
    xpos 0.08
show jigoro smug:
    center
    xpos 0.87
with charaenter

play music music_another fadein 0.5

"Shizune, Hideaki y Misha están sentados en la sala de estar, teniendo una conversación unilateral con un hombre oso gigante que alterna entre atragantarse con comida de un plato balanceándose sobre su pierna y darle vueltas a una espada."

"Por como se ven Hideaki y Shizune, esperaba que su papá fuera una persona muy reservada, pulcra y posiblemente andrógina, así que estoy muy sorprendido. Estoy sorprendido por un momento, hasta que comienza a hablarme."

show jigoro laugh
with charachange

hx_ "¡Hola! Tú debes ser el otro amigo de Shizune. ¿Descansaste bien anoche? Las habitaciones de huéspedes son un poco escasas, si hay algo que necesites, siéntete libre de decírmelo."

hi "Gracias. Debe ser el padre de Shizune. Es un gusto conocerlo. Soy el compañero de clases de Shizune, Hisao Nakai."

show jigoro neutral
with charachange

hx_ "El placer es mío. He querido conocerte, después de escuchar que tendría un segundo invitado en mi casa. Inesperado. Escuchas algo como eso, y obviamente quieres ver cómo es esa persona. ¿Te gustaría mi tarjeta de presentación?"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

show jigorocard:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"Él sostiene una caja llena de ellas por un segundo y puedo ver que su nombre es Jigoro y que sus horas de oficina son de ocho a seis. También dicen que es un “consultor”. Qué tipo tan preparado, llevando su caja de tarjetas en su propia casa."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

show jigorocard:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide jigorocard
with None

show jigoro smug
with charachange

hx "Acabamos de sentarnos para un almuerzo algo tarde, llegas justo a tiempo para acompañarnos. Bien. Elige un lugar para sentarte y te traeré un plato. Espero que no te moleste comer hígado de oso."

"Pensé que el hígado de oso era tóxico. De todos modos, la idea de comer un hígado de oso no me atrae, excepto por la habilidad de decirle a la gente que comí hígado de oso. Supongo que no dolería probarlo. Pero el papá de Shizune solamente se ríe."

show jigoro laugh
with charachange

hx "Solo estoy bromeando. Aunque, tal vez no sería tan mala idea cocinarles algunos hígados de oso para ustedes, chicos. Los harán fuertes."

show jigoro neutral
with charachange

hx "En realidad vamos a comer omelets. Te haré uno ahora mismo. ¿Es inusual para ti, tener omelet de almuerzo?"

show hideaki triangle
with charachange

hh "Muy inusual."

hi "No, para nada."

hide jigoro
with charaexit

"Jigoro se desvanece hacia donde debe estar la cocina. Estoy sorprendido de que a pesar de vivir en este lugar, él tenga que cocinar mi almuerzo. Tal vez solo cocina porque le gusta hacerlo."

show jigoro smug:
    center
    xpos 0.87
with shorttimeskip

"Mi humeante plato de comida está listo en muy poco tiempo. Huele muy bien."

hx "¿Estás en el consejo estudiantil, como Shizune? ¿El consejo estudiantil está tan ocupado, que Shizune tiene que arrastrar a sus amigos a dondequiera que va?"

show shizu behind_blank_cas at Position(xpos=0.12)
with charachange

ssh "A veces las vacaciones son solo vacaciones."

hi "Tiene razón en la parte del consejo estudiantil. Aunque creo que estamos aquí solo por diversión."

show jigoro neutral
with charachange

hx "Ya veo. ¿Eso es cierto? Cuando yo era joven, nuestros consejos estudiantiles tenían tanto trabajo que no creo que pudiéramos habernos permitido ir de vacaciones."

hx "Debe ser agradable, tener tanto tiempo libre. Debería darte bastante tiempo para pensar en tu futuro."

"No me gusta la dirección que está tomando esta discusión, y comienzo a pensar en cómo evitarla."

hx "¿Has pensado en eso? ¿Sobre lo que quieres hacer?"

hi "No, no lo he pensado mucho últimamente. ¿Qué hace, si no le molesta que le pregunte? Debe ser algo muy bueno, si puede darle una casa como esta."

show jigoro angry
with charachange

hx "¿Por qué quieres saber eso? Los niños no están interesados en los negocios. ¿Qué interés tienes en mis negocios? Sospechoso. ¿Eres alguna especie de recaudador de impuestos, muchacho?"

"Supongo que realmente no le gusta que le hagan preguntas."

show misha hips_grin_cas
with charachange

mi "Hicchan no es hijo de un recaudador de impuestos, creo~. Hicchan, ¿qué hacen tus padres? ¡Nunca nos contaste~!"

hx "Tú, cállate. No me interrumpas. Odio que me interrumpan. Descortés."

show misha perky_sad_cas
with charachange

mi "Aah~…"

show shizu basic_normal2_cas at Position(xpos=0.08)
with charachange

"Shizune no se ve muy feliz con este giro en la situación. Incluso con Misha incapaz de decirle en señas lo que está ocurriendo, ella puede leer el ambiente fácilmente. Su mirada se vuelve más latente mientras Jigoro continúa vociferando."

hx "Una cosa más. Mi equipo de pesca. Llegué a casa y estaba en un gran montón en la esquina. Las cañas estaban apiladas de manera desordenada encima del aparejo."

show hideaki thinking
with charachange

hh "Ese fui yo."

"No puedo recordar si en realidad fue él. Si no fue, aprecio que esté dispuesto a sacrificarse por nosotros. Eso no importa porque Jigoro lo ignora sin perder el ritmo."

show jigoro smug
with charachange

hx "Bueno, en fin, me alegra que mi equipo de pesca pudiera darles tanto entretenimiento a los amigos de mi hija. Ni siquiera me dijeron que iban a estar usándolo. Esas son cañas caras y hechas a la medida. No son para diletantes."

"De repente me doy cuenta de los fragmentos de cáscara de huevo en mi tortilla. ¿Es simplemente un mal cocinero? ¿Los come por el calcio? ¿Fueron puestos allí a propósito para ponerme aún más incómodo?"

"Aunque confundido, no estoy tan desconcertado como creo que normalmente estaría. Así y todo, mi vida ha sido muy extraña últimamente, y me sigo encontrando con todo tipo de personas diferentes. Ya nada me sorprende."

show jigoro angry
with charachange

hx "Ni siquiera las limpiaron después de usarlas. Terrible."

hx "¿Al menos saben cómo pescar? Improbable. No hay suficientes cañas para todos ustedes. ¿Cómo funciona eso? ¿Todos ustedes compartieron? ¿Una persona pone el cebo en el anzuelo, y otra lanza? ¿Dos personas para enrollar? Incompetente."

hi "Bueno, fuimos seis de nosotros, así que todos no podíamos hacerlo al mismo tiempo. Primero fuimos Akira, Hideaki, Misha y yo."

hx "Deja de hablar. Eso suena indescriptiblemente sucio. He tenido suficiente de tu porquería. Qué vulgar. La próxima vez asegúrate de que tus declaraciones no sean expresadas de manera tan vergonzosa ni descuidada."

hi "¿Qué…?"

hx "“¿Qué?” Eres tan irrespetuoso. Increíble. ¿Todos los tipos de delincuentes son así? Incluso la manera como vistes muestra un frívolo desprecio por la autoridad. Chaleco. Vergonzoso…"

hi "¿Delincuente? Estoy en el consejo estudiantil."

"Estoy dolido por su comentario sobre mi chaleco, especialmente viniendo de un tipo con una camisa tan de mal gusto. Aunque supongo que en realidad no puedo decir nada. Él tiene una espada. Puede que también mate osos."

stop music fadeout 0.3
play sound sfx_impact
with vpunch

"Misha pone ruidosamente su plato sobre la mesa."

show misha hips_smile_cas
with charachange

mi "¡Eso fue delicioso~! Shicchan y yo ya acabamos. Hicchan, tú también, ¿cierto~? ¡Deberíamos irnos!"

"Qué simple, pero efectiva estrategia de salida."

scene bg shizu_houseext
with locationchange

"Apenas tengo el tiempo para dejar mi plato antes de que ellas me levanten y me saquen de allí, y finalmente lleguemos afuera."

show shizu behind_frustrated_cas at tworight
show misha perky_confused_cas at twoleft
with charaenter

shi "…"

show misha sign_confused_cas
with charachange

mi "¡Increíble~! ¡Es como si en realidad estuviera viendo un interrogatorio~! ¡Esto no es un show de policías! Los huéspedes sin duda tienen responsabilidades, ¿pero él no ha escuchado alguna vez sobre ser un anfitrión cortés~? ¡En serio~!"


"Misha intenta imitar de manera efusiva los gestos enfadados y cortantes de Shizune lo mejor que puede. Ella conoce muy bien las expresiones, pero el tono de su voz es el mismo de siempre, por lo tanto carece de la ira necesaria para que sea creíble."

show misha hips_smile_cas
with charachange

mi "Guajaja~. ¡No te lo tomes a mal, Hicchan~! El papá de Shicchan le hace esto a todos, creo que es como una broma~."

hi "Esa fue la broma más agresiva posible."

"Tampoco estoy del todo convencido de que fuera una broma, considerando esta retirada rápidamente preparada, pero este no es un buen momento para discutir cómo el padre de Shizune puede ser un imbécil."

play music music_shizune fadein 4.0

show misha sign_smile_cas
with charachange

mi "¡Hicchan, vamos de compras!"

show shizu adjust_happy_cas
with charachange

ssh "Aún no has ido a la ciudad, ¿no es así? Será divertido. Podemos apreciar las vistas, e ir a un parque de diversiones, tal vez comer en un buen restaurante."

hi "Acabamos de almorzar."

"Aunque no comí mucho."

show shizu behind_smile_cas
with charachange

ssh "Está bien, en ese caso, solo tenemos que asegurarnos de que hoy estemos tan ocupados que para cuando hayamos terminado, sea la hora de cenar."

show misha cross_grin_cas
with charachange

mi "¡Resulta perfecto~! ¡Vamos, Hicchan~!"

show shizu behind_smile_cas_close at closeright
show misha cross_smile_cas_close at closeleft
with characlose

"Ellas de inmediato me flanquean y enganchan mis brazos con los suyos, Shizune toma un brazo y Misha toma el otro. Al principio, casi nos tropezamos. Shizune camina a un ritmo muy enérgico, y Misha tiene una manera inusualmente vivaz de moverse."

scene bg shizu_park
with locationchange

"Nos acostumbramos a esto rápidamente, y noto que vamos a ir a la ciudad atravesando el parque. No parece eficiente, así que supongo que esta es la ruta escénica."

"Caminar así impide la comunicación entre nosotros de manera significativa. No puedo hablarle a Shizune en absoluto. Shizune y Misha están reducidas a gestos con una mano únicamente. Sin embargo, se siente bien, así que no me molesta mucho."

"Cuando se lo digo a modo de chiste a Misha, ella responde con una ligera confusión."

show misha perky_confused_cas_close at closeleft
with charaenter

mi "¿En serio, Hicchan~? Hm… Si de verdad quieres llamar la atención de Shicchan, puedes decirme, y entonces puedo tocarla en el hombro por ti."

hi "Simplemente podrías soltarme y lo haré yo mismo. ¿Cómo puedes tocarla en el hombro desde allí?"

show misha hips_grin_cas_close
with charachange

mi "¡Así~!"

with vpunch

show shizu behind_frustrated_cas_close behind misha at closeright
with charachange

"Ella de repente se detiene en seco bruscamente, e intenta llegar a sus espaldas y a través de mis hombros para llamar la atención de Shizune. Tiene éxito, pero solo porque cuando Misha se detuvo, tuve que hacerlo yo también o todos nos caeríamos."

show misha hips_laugh_cas_close
with charachange

show shizu adjust_blush_cas_close
with charachange

"Obviamente, Shizune tuvo que parar bruscamente también. La escena hace que Misha suelte una de sus características carcajadas, lo que nos sacude más, y Shizune comienza a agitar su mano libre para hacer que ella pare, lo que causa que ría más."

"Es muy gracioso verla ponerse tan nerviosa, y también comienzo a reír."

stop music fadeout 2.0

scene black
with dissolve



label es_S21:

scene bg shizu_guesthisao
with locationchange

play music music_dreamy fadein 2.0

"He estado descuidando mis estudios de lenguaje de señas, así que probablemente debería pasar algo de tiempo repasándolo. Aunque, creo que he aprendido mucho solo por ósmosis."

"Estoy muy orgulloso de eso, y tendré que ser cuidadoso de no presumir de ello."

"Muchos de los libros que traje conmigo no son manuales para aprender lenguaje de señas, sino estudios sobre diferentes “dialectos” de señas. Sé que Shizune tiene algunas señales secretas con Misha, cuyo significado conocen solo ellas dos."

"Después de ver un par de ellas, este libro me llamó la atención en la biblioteca de la escuela."

"Tal vez debería incorporar algunos ejemplos en mis propias señas, para molestarlas, porque estoy bastante seguro de que ellas han comenzado a usar más sus palabras en clave cuando comencé a aprender lenguaje de señas. Eso les enseñará."

"Después de un rápido descanso para una ducha, continúo practicando mis señas en el espejo de la habitación de huéspedes. Ayer, mis dedos se golpearon muy fuerte entre sí. Aún me duele, y no quiero que eso se repita."

play sound sfx_doorknock2

show hideaki normal at center
with charaenter

"Oigo tocar la puerta detrás de mí y me giro para encontrar a Hideaki parado en la puerta, mirándome. Qué amable de su parte tocar, pero por lo general no abres la puerta primero."

show hideaki triangle
with charachange

hh "¿Qué estás haciendo?"

hi "Estoy practicando lenguaje de señas. ¿Cuánto tiempo has estado allí parado?"

show hideaki thinking
with charachange

hh "No he visto nada."


"Ese no es el punto. Ni siquiera sé qué quiere decir con eso. No es que estuviera haciendo algo que me dé vergüenza que la gente me vea haciendo."

"Sin embargo, el lenguaje de señas debe verse extraño para la mayoría de la gente. Solo estoy acostumbrado a ello por estar tanto junto a Shizune y a Misha."

hi "Estoy repasando mi lenguaje de señas, y leyendo sobre él también. Cosas como su historia, aunque eso lo cubren en la clase de lenguaje de señas."

show hideaki normal
with charachange

hh "¿Tu escuela enseña lenguaje de señas como una clase?"


hi "Sí. Una de las primeras cosas que mencionaron fue que no es muy común hacerla. Supongo que somos muy internacionales, o algo así."

show hideaki serious
with charachange

hh "Parece divertido."

hi "Bueno, yo no lo llamaría divertido."

show hideaki bored
with charachange

hh "Si no disfrutas esto, parece que pasas por mucho trabajo solo para hablar con mi hermana."

hi "¿Por qué todos siguen diciendo eso?"

show hideaki happy
with charachange

"La boca de Hideaki se retuerce como si estuviera a punto de reírse, pero se contiene. Ahora que lo pienso, él no se ha reído ni una vez desde que lo conocí. Podría tomar como un cumplido el que él no se ría de mí, pero tengo curiosidad de verlo."

hi "Ríe."

show hideaki thinking
with charachange

stop music fadeout 4.0

hh "…"

show hideaki bored
with charachange

hh "¿Por qué?"

"Fue la manera más rápida y directa que se me pudo ocurrir hacia el logro de mi objetivo."


show hideaki normal_up
with charachange

hh "¿Puedes enseñarme lenguaje de señas?"

"Lo dice llanamente, pero su lenguaje corporal está nervioso, mostrando que claramente necesita esforzarse para preguntar."

"Supongo que a Hideaki le gusta su hermana después de todo. Pero yo pensaría que Misha es mucho más accesible, así que me pregunto por qué no le preguntó a ella."

"En secreto, estoy gritando “¡sí!” por dentro. Había pensado que él quería aprender lenguaje de señas y hasta lo saqué a relucir, pero había evadido el tema hábilmente."

"Resulta que yo tenía razón después de todo. Realmente no sé por qué esto me pone tan contento."

hi "Claro."

"Pero ahora que pienso en ello, no soy maestro de lenguaje de señas. Ni siquiera sé por dónde empezar. En clase, estaría aprendiendo cosas poco a poco durante una semana. ¿Hideaki espera que le enseñe algo útil en un curso intensivo de un día?"

show hideaki normal
with shorttimeskip

play music music_normal fadein 3.0

"Mi maestra pasó un par de días solo mostrando la historia del lenguaje de señas. Decido comenzar con eso, para ganar tiempo mientras pienso cómo puedo pasar de esto a la parte dura. Cinco minutos después, Hideaki levanta su mano."

show hideaki serious_up
with charachange

hh "No entiendo lo que estás haciendo."

hi "Eh… bueno, no puedes simplemente saltar a enseñar, ¿sabes? Tienes que avanzar poco a poco. Es como cuando vas a nadar, no saltas directo al lago como en una película."

show hideaki triangle
with charachange

hh "Yo no nado."

"Es como si los científicos lograran crear un proceso para succionar todas las cualidades hiperactivas, exasperantes e infantiles de un niño pequeño y luego las implantaran en el papá, creando un papá furioso e imbécil, y dejando atrás a Hideaki."

"Comienzo a sentir claustrofobia, a pesar del hecho de que la habitación de huéspedes es tres veces más grande que mi habitación y solo estamos nosotros dos aquí."

"Todo está en mi cabeza, lo sé, y no me importa. Aun así lo uso como excusa para mover la lección afuera."

scene bg shizu_garden
with locationskip

"Es mucho más fácil concentrarse aquí afuera. Incluso los pocos preciosos segundos que tardamos en reubicarnos lograron permitirme ordenar mis pensamientos."

"No hubo preguntas durante este momento. Hideaki parece no poder hablar y caminar al mismo tiempo."

"Con el tiempo, sin embargo, comienzo a darme cuenta de que si voy a enseñarle algo, tengo que mantener la lección en constante movimiento."

"En el momento en que se presente una oportunidad, él hará una pregunta, que llevará a más preguntas. Entonces no habrá fin a ello."

"La segunda vez que me pregunta por qué un cierto movimiento de mano significa lo que hace, y tengo que llegar muy adentro en mi memoria buscando etimología que no sé sobre un gesto que sabía solo un mes más que él, comienzo a buscar una salida."

hi "Hideaki, vamos a tomar un descanso."

show hideaki bored
with charachange

hh "Bueno."

show hideaki serious
with charachange

hh "¿Cómo es tu escuela?"

"Este niño es como un pequeño periodista, pero tiene sentido que alguien de su edad tenga curiosidad, y esta es una pregunta que no me molesta."

hi "¿Cómo es? En realidad nunca lo he pensado. Está en la cima de una montaña, así que a veces se siente algo aislado y solitario allí arriba, aunque también esa es la razón por la que tiene una vista grandiosa."

hi "Los estudiantes allí son interesantes. De hecho, me sentí mal al comienzo. Sabes qué tipo de escuela es, ¿cierto?"

show hideaki normal
with charachange

hh "Sí."

hi "Me sentí mal porque no quería ir allí. Ni siquiera recuerdo exactamente qué estaba pensando en ese momento. Probablemente era algo como, una escuela para lisiados sería un lugar deprimente. Estaban diciéndome que fuera allí a que me olvidaran."

hi "Entonces, todos allí solo estaban viviendo sus vidas, en mayor parte. Así que me sentí aún peor. No era para nada diferente, así que me sentí como un imbécil."

hi "Shizune fue la primera persona que conocí. Ella está en la mayoría de mis clases. Misha, también, siempre están juntas."

hi "Supongo que la escuela es lo bastante complaciente como para emparejarlas tanto como sea posible. Hay una chica en mi clase, Hanako, por la que me siento mal."

hi "Ella tiene unas quemaduras, y parece tener un complejo por ellas. Pero creo que se ve bien. Es una chica bonita. Y también es amiga de Lilly. Conoces a Lilly, ¿cierto? ¿Ella habla de Hanako?"

show hideaki thinking
with charachange

hh "Sí, a veces."

hi "Estoy intentando recordar quién más es interesante. Tenemos a una pequeña estrella, un as del atletismo que corre con unas prótesis."

hi "Hay una chica, Rin, quien no tiene brazos, pero es una gran pintora. Todo su arte tiene una cualidad dura y viva. ¿Alguna vez has ido a Yamaku? Probablemente hayas visto algo de su arte rondando por allí."

hi "Un poco rara, a veces, pero siempre he escuchado que los tipos artísticos y creativos son así. Eso me recuerda, el tipo que vive al otro lado del pasillo enfrente de mí también es muy raro. Pero al menos él puede ser interesante."

show hideaki normal
with charachange

hh "Tú también eres interesante."

hi "¿Eso es malo? ¿Y qué pasa con ese tono? ¿Qué significa eso? ¿Estás diciendo que soy raro, Hideaki?"

show hideaki triangle
with charachange

hh "Hablas mucho."

"Mi primer instinto es ir a la defensiva, pero entre más lo pienso, más razón tiene."

hi "Así es, sí hablo mucho. No creo que antes lo hiciera."

hi "Creo que… probablemente es por todo el tiempo que paso junto a Shizune y Misha. Hablando con ellas, me quedo atrapado en toda su lógica circular y también en cómo hacen todo. Siento que van a ahogar mi voz, o que me quedaré atrás."

show hideaki confused
with charachange

hh "¿Mi hermana puede ahogar tu voz?"

hi "No es que ella literalmente hable más que yo y eso, obviamente. Es difícil de explicar."

hi "Ellas tienen más energía que yo. Es como, una agresividad. No siento como si tuviera que igualarla, pero quiero hacerlo. Creo que tal vez tu hermana tiene ese efecto en la gente."

show hideaki thinking
with charachange

hh "…"

hi "¿Admiras a tu hermana?"

show hideaki normal_up
with charachange

"Me mira fijamente sin comprender, tenso y confundido en cuanto a cómo reaccionar a la pregunta."

show hideaki angry_up
with charachange

stop music fadeout 5.0

hh "Seré mejor que Shizune."

hi "¿Mejor en qué?"

show hideaki angry
with charachange

hh "En… todo."

hi "¿Como qué?"

show hideaki triangle
with charachange

hh "Puedo hacer trucos de magia."

hi "¿Te refieres a decirle a la gente que tienes su nariz, o más bien al tipo de magia donde te sacas un conejo del culo?"

"No se ve feliz. Algún día, veré a Hideaki reírse. Podría tratar de hacerle cosquillas, si es necesario."

play sound sfx_doorslam

show hideaki surprise
with vpunch

show hideaki thinking at twoleft
show bg shizu_garden at bgleft
with dissolvecharamove

show jigoro neutral at tworight
with charaenter

"La puerta de atrás se abre de golpe y Jigoro sale dando zancadas, manteniendo su espalda recta y dando zancadas gigantes, lentas y majestuosas, como un rey o como un grandísimo idiota."

"Intento apartar la mirada, bajo la lógica de que si no lo veo, él no puede verme. Desafortunadamente, no da resultado y él se acerca tan rápido que es como si apareciera de la nada sobre mi hombro."

show jigoro laugh
with charachange

play music music_happiness fadein 2.0

hx "Ajá. ¿Qué pasa aquí? ¿Qué están haciendo ustedes dos, agitando sus manos frenéticamente? ¿Jugando con un cordel como un montón de niñas?"

hi "Le estoy enseñando a Hideaki algo de lenguaje de señas. ¿Qué hay de usted, Sr. Hakamichi?"

show jigoro angry
with charachange

"Él entrecierra sus ojos con sospecha, como si no estuviera acostumbrado a que la gente sea amable con él."

hx "Estoy escribiendo una autobiografía de mi vida y obra. Y por “escribir” quiero decir que se la estoy dictando a mi biógrafa. Desafortunadamente, se le hizo tarde. Poco profesional."

show jigoro smug
with charachange

hx "Quizás deberías leerla cuando esté publicada a finales de este año. Puedo ponerte en la lista de espera. Tal vez te dará la brújula moral que parece te falta en tu vida, y te inspire para que dejes de ser mediocre."

"No puede ser sostenible para él ser tan casualmente insultante con todo el mundo."

"Sin embargo, Hideaki probablemente es muy distante como para notarlo, Shizune es sorda, y la mayoría de los insultos deben pasar sobre la cabeza de Misha. Pero sin duda Akira debe tener una opinión al respecto."

"Intento no pensar en ello. Si está haciendo esto para incomodarme, entonces tengo que estar calmado o él gana. Él no debe ganar de ninguna manera, en absoluto. Así es como debe sentirse Shizune."

hi "¿Cuántos años tiene?"

show jigoro neutral
with charachange

hx "Cuarenta y seis."

hi "Esa no parece ser la edad suficiente para justificar escribir una biografía. Quiero decir, ni siquiera es viejo. ¿La mayoría de la gente no comienza a escribir sus memorias a una edad mucho mayor que esa?"

show jigoro angry
with charachange

hx "Cállate, muchacho. Voy a darte un consejo: no hables sobre asuntos de edad con gente mayor que tú. Tienes menos de la mitad de mi edad, no tienes derecho de hablar sobre vejez. Tengo una úlcera mayor que tú."

"Debió habérsela revisado. Aunque puede que tenga razón, sin duda él es mayor que yo."

show jigoro laugh
with charachange

hx "… En cualquier caso, incluso si tuviéramos la misma edad, no tendría que darte explicaciones, chaleco."

hi "Ugj."

show jigoro angry
with charachange

hx "¿Por qué haces ese ruido? ¿Estás furioso? Bueno, obviamente. Bien. Tu chaleco es terrible, y quiero que te sientas mal por ello. Ese gesto me dice que está funcionando."

hi "Me gusta mi chaleco."

show jigoro smug
with charachange

hx "Estoy seguro de que también te gusta inhalar pegamento. Eso no lo hace correcto."

hi "Yo no inhalo pegamento. ¿De dónde tuvo la impresión de que lo hago?"

show hideaki normal
with charachange

hh "Eso es calumnia."

"Me pregunto cómo Hideaki sabe qué es la calumnia. Tal vez Jigoro es abogado. En cierto modo puedo verlo, aunque pensé que solo los abogados de la TV eran así de antagónicos. No sé si debería arriesgarme y preguntarle si ese es su trabajo."

hi "Él tiene razón. Es calumnia. ¿Usted es abogado?"

show jigoro neutral
with charachange

hx "Estaba suponiéndolo, una suposición basada en el hecho de que eres estúpido. Es como cuando tú estás asumiendo que soy abogado, excepto que no tienes razón para pensar eso."

hx "Si quieres tanto saber lo que hago, ¿por qué no preordenas mi autobiografía?"

show jigoro angry
with charachange

hx "Ahora estás insultando mi libro, y, por extensión, mi vida entera. ¿Qué te da el derecho de hacer eso? Arrogante. Estoy tratando de pensar en cómo podría hacerte entender mi lucha. Tal vez golpeándote. Con mi autobiografía."

hx "Espero que te alejes de la golpiza después de haber aprendido una valiosa lección, como no hacer suposiciones."

show hideaki bored
with charachange

hh "Asalto…"

"Pero él también hizo una suposición, que yo inhalaba pegamento. Considero llamarle la atención sobre este ejemplo flagrante de hipocresía, pero no creo que valga la pena. Probablemente se explicaría diciendo “Cállate, muchacho”."

show jigoro smug
with charachange

hx "En mis tiempos, los niños eran vistos y no escuchados, y ser un adulto significaba haber experimentado muchas privaciones."

hx "Incluso con una mirada, la gente inmediatamente podía juzgar el carácter de un hombre. La infancia solo existía para templarte para la adultez."

hx "Cuando me miras, ¿no puedes ver el catálogo de mis experiencias incluso con una mirada?"

hi "Eh… tal vez. ¿Usted era espadachín?"

"Él también podría ser hawaiano, y hombre lobo."

hi "Espere, ¿no me dijo antes que no hiciera suposiciones? Ahora, acaba de pedirme que supusiera algo. Y usted está diciendo que cuando tenía mi edad todos lo hacían. Y eso tuvo que ser, como, en los 80. ¡Eso ni siquiera fue hace mucho tiempo!"

"Estoy listo para decirle lo que pienso, por hablar como si hubiese tenido que caminar quince kilómetros en la nieve para abordar un tren de carbón."

"Un tren donde él mismo tenía que palear el carbón, antes de escalar una montaña mientras luchaba contra ogros para llegar a la escuela."

"Pero ahora que por fin quiero una pelea, Jigoro está feliz de pasar un buen rato con solo seguir divagando sobre lo difícil que era crecer hace una generación, girando su espada como un bastón y parando en ocasiones para bostezar o mirar la hora."

"La tardanza de su autobiógrafa todavía es lo primero en su mente. Eso significa que todo el tiempo que ha estado insultándome, debió haber estado haciéndolo solo para pasar el tiempo. Para colmo de males, su reloj también es muy bonito."

show jigoro angry
with charachange

hx "… Cuando tenía tu edad, los niños tenían responsabilidades. No como hoy. Repugnante. Ya nadie piensa en las consecuencias de sus actos. Solo hacen lo que quieren, pensando que nadie los hará responsables por sus actos ya que son jóvenes."

"Es extraño, esa descripción encaja con Shizune y con Misha. Pensé algo parecido apenas ayer. Pero solo les encaja un poco."


hx "Mírate. Un inhalador de pegamento amoral, sin rumbo y delincuente, con una completa falta de etiqueta y sin absolutamente ningún sentido de la moda. Eres el Japón del mañana. Vergonzoso. ¿Este es el futuro de este otrora gran país?"

hi "Conozco a alguien con quien se llevaría bien."

hx "¡No interrumpas! ¿Quién? ¿Uno de tus amigos? ¿Por qué querría hablar con un horrible adolescente? ¿Has estado escuchando? ¿Por qué eres tan grosero, muchacho? Tu actitud no es una que te haga muchos amigos."

hi "Desearía que dejara de darme tantos consejos."

"O al menos, desearía que me diera consejos que él mismo tuviera la decencia de cumplir."

show jigoro neutral
with charachange

hx "¿Dónde has estado?"

hi "¿Eh?"

show jigoro angry
with charachange

stop music fadeout 3.0

hx "Tú no, idiota."

show jigoro angry at Position(xpos=0.85)
show hideaki normal at Position(xpos=0.45)
show bg shizu_garden at center
with dissolvecharamove

show shizu behind_blank_cas behind hideaki:
    twoleft
    xpos 0.2
with charaenter

shi "…"

hi "Ups. No me fijé que estabas allí."

show shizu adjust_happy_cas
with charachange

"Shizune sonríe y hace un pequeño gesto con la mano. Su llegada hace que Jigoro deje de hablar, así que ya estoy feliz de verla solo por esa razón."

show shizu basic_normal2_cas
with charachange

ssh "Misha y yo decidimos ir a la ciudad de nuevo. Hisao, noté que ayer estabas mirando algo de ropa en la ventana de una tienda, y pensé en regresar y comprarte algunas de esas prendas. Aunque se suponía que era una sorpresa."

"Se ve molesta porque la sorpresa está arruinada, aunque fue ella misma quien la arruinó."

show shizu behind_blank_cas
with charachange

ssh "¡Aquí tienes!"

hi "Gracias."

show shizu basic_normal_cas
with charachange

ssh "Misha quería cortarse el pelo. Le dije que no lo hiciera, pero dijo que era demasiado caliente para el verano."

hi "¿Sí? No lo sé, tiene sentido para mí. Debe ser como un horno ahí abajo. Quiero verlo. ¿Dónde está Misha, de todos modos?"

mi "¡Por aquí~! ¡Hola, Hicchan~! ¡Hola, Sr. padre de Shicchan~! ¡Hola, Hideaki~!"

show jigoro smug
with charachange

hx "…"

play music music_running

show mishashort hips_grin_cas behind shizu at offscreenleft
with charamoveinright

hide mishashort
with None

show mishashort hips_grin_cas at offscreenleft
with None

show shizu basic_normal_cas:
    xpos 0.3
show jigoro smug:
    xpos 0.95
show hideaki normal:
    xpos 0.55
show mishashort hips_grin_cas:
    center
    xpos 0.1
show bg shizu_garden:
    xpos 0.55
with dissolvecharamove

"Misha corre alrededor de nosotros en un círculo amplio antes de detenerse junto a Shizune."

"Por primera vez, ella no ha puesto sus manos sobre mis ojos, aunque ahora veo que tiene bolsas para cargar por su cuenta, así que no es que pudiera aun si quisiera. Aunque estoy seguro de que lo ha intentado antes."

"Sus rizos meticulosamente arreglados se han ido, a favor de un aspecto más corto y deportivo. Misha incluso se ve más feliz de lo normal, probablemente porque sabe que no tendrá que despertarse cada mañana al amanecer solo para arreglarse el pelo."

show jigoro angry
with charachange

hx "¿Qué es ese corte de pelo? Pareces una interna. Tu viejo corte de pelo apenas te hacía ver como si estuvieras usando una peluca de juez rosa. De jueza a interna es una degradación enorme."

show shizu behind_frown_cas
with charachange

ssh "Hisao, ¿está diciendo algo insultante? ¡Dile que no insulte a mis amigos!"

hi "No insulte a mis amigos."

hx "¿Quién de ustedes está hablando?"

hi "Ambos. Estoy de acuerdo con ella."

show mishashort hips_smile_cas
with charachange

mi "¡Jejeje~! ¿Qué piensas, Hicchan?"

show shizu adjust_frown_cas
with charachange

ssh "Deberías habértelo dejado como estaba."

show mishashort perky_sad_cas
with charachange

mi "Oh~… Hicchan, te ves decepcionado, ¿tampoco te gusta?"

hi "Bueno, sí, admitiré que como que me gustaba más tu viejo corte de pelo, pero creo que este es bonito también. Te queda bien."

show mishashort hips_grin_cas
with charachange

mi "¡Oh, gracias, Hicchan~!"

hx "Conmovedor. Si te gusta tanto, tal vez ustedes dos deberían intercambiar."

hi "No puedes intercambiar un corte de pelo."

hx "Qué lástima. Incluso su viejo corte de pelo te quedaría mucho mejor que tu corte actual y perezoso. Espantoso. En cuanto a ti…"

show jigoro laugh
with charachange

hx "Hmmm… En realidad, este es mucho menos llamativo que tu otro corte de pelo. Me gusta."

show mishashort cross_laugh_cas
with charachange

mi "¡Ajajajaja~! ¿En serio? ¡Gracias, Sr. papá de Shizune~!"

show jigoro angry
with charachange

hx "Es Sr. Hakamichi. Habla como una persona normal."

show mishashort perky_smile_cas
with charachange

mi "¿Hm~? ¡No entiendo~! Bueno, ¡bueno bueno~! ¡Lo llamaré Sr. Hakamichi!"

hx "Agh, es como hablarle a una flauta de émbolo. Despreciable. ¿Dónde está mi biógrafa? ¡Hideaki!"

show jigoro invis
show shizu basic_normal_cas
show hideaki bored
with charaexit

"Él comienza a murmurar en silencio y se aleja. Supongo que un aspirante a anciano malhumorado como Jigoro sería reacio, por lo menos, a gritarle a las chicas. De repente, él se vuelve, incapaz de resistirse a su deseo de tener la última palabra."

show jigoro angry
with charaenter

hx "Y otra cosa, no tienes que hablar tan fuerte. No me gusta que me griten."

show mishashort hips_grin_cas
with charachange

mi "¿Qué? ¿Gritar~? ¡Yo no estoy gritando~!"

"No puedo pensar en nadie menos calificado para hablar sobre qué es llamativo o para regañar a alguien más por gritarle a la gente. Es como un desfile de hipocresías y las críticas solo siguen llegando."

"Una reacción inusual parece estar teniendo lugar. Misha aparentemente encuentra gracioso a Jigoro y se ríe casi siempre que él dice algo, lo que hace que él la regañe más fuerte. Supongo que esto es lo que llaman un círculo vicioso."

"La voz de Misha está salpicada con explosiones de risas y parece venir de todas partes. Por otro lado, la de Jigoro está en auge y dirigida como un cañón. En cualquier caso, ambas son increíblemente fuertes."

"Entre más se hablan entre sí, más parecen estar enfrentando el volumen del otro y hablando más fuerte."

show mishashort perky_sad_cas
with charachange

mi "¡Au~! ¡Me duelen mis oídos~!"

hx "¿POR QUÉ ESTÁS GRITANDO?"

hide shizu
with charaexit

show black
with hands_in

"Las manos de Shizune envuelven mis ojos desde atrás, algo que estoy tan acostumbrado a que Misha haga que por primera vez me encuentro confundido por eso, ya que Misha está enfrente de mí."

show shizu adjust_happy_cas_close at center behind black
show hideaki bored at center
with None

hide black
with hands_out


"Ella retira sus manos y levanta un dedo a la altura de sus labios."

show shizu behind_smile_cas_close
with charachange

ssh "¡Qué perfecta distracción! Ahora es nuestra oportunidad. Vamos a escabullirnos."

his "¿Por qué tenemos que escabullirnos? ¿Por qué no simplemente nos vamos caminando?"

show shizu adjust_smug_cas_close
with charachange

ssh "No sería tan divertido."

show shizu basic_happy_cas_close
with charachange

ssh "Está decidido: es una misión secreta. Escapar sin ser detectado. Saca a Hideaki para ganar puntos extra."

hide shizu
with charaexit

stop music fadeout 3.0

"Ella ya ha simplificado la situación a un juego. Shizune se aleja silenciosamente de la escena y comienza a acercarse lentamente a la casa. Yo camino hacia ella, normalmente."




label es_S22:

scene bg shizu_living
with locationskip

"Al comienzo no puedo encontrar a Shizune, pero al final ella ingresa a la parte principal de la casa, bebiendo de un vaso de agua con hielo y moviendo sus anteojos de un lado a otro con su mano libre. Ella se los pone rápidamente tan pronto me ve."

show shizu basic_normal2_cas at center
with charaenter

play music music_ease fadein 4.0

ssh "No rescataste a Hideaki. Eso significa que no obtienes los puntos extra. Si también fueras calificado por estilo, tendría que descontar puntos por un escape aburriiiiiido."

his "Parecía que querías hablar conmigo, no sabía que debía tener estilo con eso. Sabes, algunos dicen que las personas con más estilo son las que no se esfuerzan tanto en verse geniales."

show shizu cross_wut_cas
with charachange

ssh "Vaya que eres genial."

"Me pregunto cómo es posible que yo pueda captar su sarcasmo tan fácilmente, y qué tan difícil pudo haber sido para ella aprender el concepto del sarcasmo sin poder oír. No puedo imaginarlo."

his "Parece que estás de buen humor."

"Aunque supongo que en realidad no es buen humor. Es más como si estuviera muy emocionada."

show shizu behind_frown_cas
with charachange

ssh "Estoy de mal humor."

show shizu basic_normal2_cas at Position(ypos=1.1)
with dissolvecharamove

"Dejando su bebida, Shizune se sienta en el sofá."

show shizu behind_frown_cas
with charachange

ssh "Me gustaba mucho más su peinado habitual. Se veía tan bonito. Era refinado y meticuloso. Ahora se ve muy deportiva y marimacha."

his "Yo no llamaría a Misha refinada y meticulosa. Eso suena más como tú. Deberías darle una oportunidad. Déjate crecer el pelo y haz que se vea como rizos."

his "Hm… en realidad, tal vez este peinado te quede bien."

show shizu adjust_frown_cas
with charachange

"Shizune frota bruscamente el marco de sus anteojos, viéndose molesta por las insinuaciones detrás de lo que acabo de decirle en señas. Qué bien, porque estaba completamente insinuando eso. Ella se acerca un poco a mí cuando me siento."

show shizu basic_angry_cas
with charachange

ssh "¿Soy un marimacho?"

his "Bueno, nadie te llamaría marimacho… Basado en apariencias."

"Shizune me mira enfurecida, eso no le hizo gracia. Tengo que luchar para mantener una cara seria."

his "Tal vez ustedes dos deberían intercambiar cortes de pelo de todos modos."

shi "…"

show shizu behind_frown_cas
with charachange

ssh "Suenas como mi padre."

show shizu adjust_smug_cas at center
with Dissolvemove(0.2)

"Es cierto. Shizune ríe sin hacer ruido cuando ve mi disgusto al darme cuenta de ello. Poniéndose de pie de un salto, ella hace girar una espada invisible en su mano izquierda mientras se para militarmente recta y hace una mueca."

"Una imitación aterradoramente precisa."

show shizu basic_frown_cas
with charachange

ssh "De todos modos, no recibo consejos de alguien que usa un chaleco azul con pantalones cafés. ¿Dónde está tu sentido de la combinación de colores? Espantoso."

show shizu adjust_smug_cas
with charachange

ssh "… Pero cambiar mi corte de pelo, podría ser divertido. ¿No es así? Quiero ver cómo reaccionarían todos."

his "Realmente te debe gustar jugar con la gente. A veces, creo, demasiado."

show shizu adjust_frown_cas
with charachange

"No hay respuesta. La manera como ella juguetea con sus anteojos, con el ceño fruncido, me dice que es porque no puede."

show shizu behind_blank_cas
with charachange

ssh "Es divertido."

"Entonces, con más confianza y mientras se acerca más a mí:"

show shizu basic_happy_cas
with charachange

ssh "Es divertido arrastrar más y más gente a mi vida."

his "Ah, ya veo."

"Me pregunto si estoy incluido en ese número. Quiero preguntar, pero ni siquiera estoy seguro de cómo lo haría."

show shizu adjust_happy_cas
with charachange

"Shizune mueve su dedo preventivamente, indicando que no responderá una pregunta como esa de todos modos."

stop music fadeout 0.5

show shizu adjust_blush_cas_close
with vpunch

"Ella trata de alcanzar su vaso, pero no parece darse cuenta de lo mucho que logró alejarse de él todo este tiempo. Para evitar volcarse torpemente, Shizune intenta agarrarse de mí, y termina tirándome encima de ella."

scene ev shizu_couch
with vpunch

play music music_serene fadein 9.0

"Mientras me inclino sobre ella, puedo sentir el calor emanando de su cuerpo y me doy cuenta de lo cerca que estamos. Puedo oír su suave respiración y el roce ligero de su ropa mientras ella se mueve nerviosamente por un momento."

"Un rubor comienza a aparecer poco a poco en sus mejillas, pero sus ojos miran directamente a los míos, oscuros y sin pestañear."

"Es la misma mirada de la primera vez que la vi, penetrante y falta de alguna emoción clara. Solo esperando a ver qué pasará a continuación, como los ojos de un gato. Me hace sentir incómodo, que me miren de esa manera."

"Esta es la primera vez que he estado tan cerca de ella por un periodo prolongado de tiempo, y el ambiente es diferente ahora. La situación ahora no es igual a un contacto de manos pasajero o a los juegos habituales de ella y de Misha."


"Los dedos de Shizune se entrelazan tímidamente, pero ella no hace ningún movimiento para hacer señas."

"La mirada en sus ojos significa algo, como lo había pensado. Es más como expectativa. Me pregunto si tal vez he estado siguiendo el hilo de sus expectativas todo este tiempo."

scene bg shizu_living
with vpunch

show shizu behind_blank_cas_close
with charaenter

"Siento que ella me agarra por los hombros y luego suavemente, pero con firmeza, me aparta de ella."

"Ruedo hacia un lado sobre el sofá mullido y me ubico sentándome a menos de treinta centímetros de ella. Tal como me siento, ella bien podría haberme lanzado a diez metros."

"Cuando pienso en ello, esta es quizás una de las más grandes desventajas del lenguaje de señas. Shizune dijo que el hecho de que tengas que hacer las señas con tus manos significa que tienes tiempo para reflexionar sobre lo que dices antes de decirlo."

"Pero por otra parte, también significa que lo que normalmente solo sería un silencio incómodo se convierte en un muro infranqueable."

"Simplemente soltaría algo, cualquier cosa, para tratar de disipar la tensión que estoy sintiendo ahora mismo si pudiera, pero no puedo."

"Por lo general, creo que lo que sería normal sería disculparme, y quizás retirarme. Pero ahora mismo, me pregunto si eso aún es aplicable. No puedo superar qué tan culpable parecería una acción como esa. Como si estuviera escabulléndome."

"Por supuesto, tampoco es que simplemente pueda simular que nada pasó. Eso sería un insulto para nosotros dos. Así que, por más que no quiero, me disculpo rápidamente, tan rápido que olvido decirlo en señas. Después regreso a mi habitación."

window hide None

scene bg shizu_guesthisao_ss
with locationskip

play sound sfx_pillow
with vpunch

$ renpy.music.set_volume(0.5, 1.0, channel="music")

show black
with shuteye

window show

"Suspirando, me dejo caer de espaldas a la cama. Ojalá pudiera irme a dormir ahora mismo, pero me siento completamente despabilado."

play sound sfx_doorclose
$ renpy.music.set_volume(1.0, 3.0, channel="music")

with Pause(3.0)

show shizu basic_normal2_cas_close
hide black
with openeye

"Me incorporo cuando escucho la puerta cerrarse y abro mis ojos para ver a Shizune sentada en la silla enfrente de mí."

show shizu behind_blank_cas_close
with charachange

shi "…"

"Ella hace una pregunta que me pasa de largo, debido a mi sorpresa. No es un sentimiento que se me da bien ocultar, y no creo que eso sea lo que ella esperaba."

"Lo que sea que estaba diciendo, ella da marcha atrás, y no trata de hacer señas de nuevo por un momento."

show shizu adjust_happy_cas_close
with charachange

ssh "Esta es la primera vez que he estado en tu habitación."

"Shizune junta sus dedos y adopta un intento exagerado de verse avergonzada y modesta ante la idea. No puedo apreciar la broma, solo el hecho de que ella esté aquí me hace sentir disperso."

his "Muy gracioso. Ni siquiera es mi habitación. Es tu habitación de huéspedes."


label es_S22a:

his "Además, Misha y tú irrumpieron en mi habitación una vez."

show shizu behind_blank_cas_close
with charachange

"Parece como si ella esperara que yo dijera algo más. Recuerdo sentirme muy asustado cuando irrumpieron en mi habitación, con miedo a las conclusiones que sacarían al ver el muro de píldoras cubriendo el lugar. Aunque no creo que Shizune lo recuerde."

show shizu basic_normal_cas_close
with charachange

ssh "Eso te puso nervioso."


label es_S22b:

ssh "Aún te veías sorprendido cuando entré."


label es_S22c:

"La manera como lo dice tan objetivamente me hiere."

his "Muchas cosas me ponen nervioso."

his "Tú eres una de ellas."

show shizu behind_blank_cas_close
with charachange

shi "¿…?"

his "Porque eres demasiado entusiasta en involucrar siempre a la gente en… lo que sea que estés haciendo. Ya sea para unirse al consejo estudiantil, o hasta para tomar un descanso. No importa si quieran o no."

show shizu basic_angry_cas_close
with charachange

shi "…"

show shizu adjust_happy_cas_close
with charachange

shi "… … … …"

show shizu basic_normal2_cas_close
with charachange

shi "… …"

"Ella hace señas casi a paso de tortuga, sus manos pausándose demasiado a mitad de la frase, haciendo que las palabras se disipen sin forma antes de que pueda tratar de entenderlas. Intento no decir que este es el caso."

"Parece funcionar, pero ella se ve un poco triste, y lamento no tener nada que decirle para alejarla de la expresión extrañamente melancólica y distante que tiene. Todo lo que puedo hacer es esperar a que ella salga de eso."

show shizu behind_sad_cas_close
with charachange

ssh "Tienes razón. Quiero arrastrar a todos a mi vida. Pero, últimamente, ya no estoy segura de si eso es lo correcto."

his "Disfruté que me llevaras a tu restaurante favorito la otra noche."

show shizu basic_normal_cas_close
with charachange

ssh "No es que ese fuera mi restaurante favorito… Tengo otros que me gustan. Hasta podría clasificarlos por número."

his "En serio…"

show shizu adjust_frown_cas_close
with charachange

ssh "Esta silla es muy dura. Quiero sentarme en la cama."

"Haciéndole señas para que lo haga, espero a que ella se levante de la silla y tomo su lugar cuando lo hace. Aunque no tenía la intención de que lo fuera, a ella le parece divertido."

show shizu behind_smile_cas_close
with charachange

stop music fadeout 5.0

ssh "Cierra tus ojos."

his "¿Por qué?"

show shizu adjust_smug_cas_close
with charachange

ssh "Es una sorpresa."

show black
with shuteye

"Decido complacerla y los cierro. Puedo sentirla inclinándose hacia mí, y de repente, algo suave y húmedo toca mis labios. Mi cuerpo se pone tenso por la sorpresa. Afortunadamente, no es una reacción tan incómoda como la que podría haber tenido."

"Solo fue un beso rápido, y casi creo que eso es todo, pero entonces me besa de nuevo, esta vez más profundamente. Sus manos se deslizan sobre mis hombros, hasta mi cuello, y luego bajan de nuevo. Luego por mis hombros y hacia abajo, a mis brazos."

"Puedo sentir el peso de su cuerpo sobre mis piernas, y el erotismo de la situación no se me escapa. En este momento, estoy listo para intentar abrir mis ojos solo un poco, pero como si lo esperara, ella pone sus dedos sobre mis párpados."

play sound sfx_rustling

"Segundos después, algo ata mis manos a la altura de las muñecas, y entro en pánico, sin saber qué pensar de esto. Mi primera idea es preguntarle a Shizune qué está pensando. Aunque sé que no puede oírme, estoy seguro de que ella entiende la idea."

"Ella no soltará mis manos, trazando sus dedos sobre ellas, desde las líneas de mis palmas, sobre mis nudillos, y hacia mis muñecas."

scene evh shizune_hcg_tied_stare:
    yalign 0.0 xalign 1.0 subpixel True
    easein 6.0 xalign 0.5 zoom 0.5
    truecenter
    zoom 1.0
    "evh shizune_hcg_tied_stare_small"
with whiteout

play music music_heart fadein 5.0

hi "Oye, ¿qué estás haciendo? ¿Qué es esto?"

"Por supuesto, con mis manos atadas a mi espalda, bien podría estar amordazado. Una parte de mí no puede dejar de pensar que esto es lo que ella quería."

scene evh shizune_hcg_tied_smile_small
with charachange

"Como si leyera mis pensamientos, una expresión traviesa ilumina su rostro, pero su rubor no se desvanece. De hecho, solo aumenta cuando nuestros ojos se encuentran."

"Avergonzada, ella se inclina más en nuestro abrazo parcial, escondiendo su rostro en mi hombro y cuello. Su cabello es suave y me hace cosquillas, y dejo salir una risa sabiendo que ella no me oirá; no se ofenderá."

label es_S22h:

scene evh shizune_hcg_tied_blush_small
with charachange

"Las manos de Shizune se mueven hacia abajo, a la bragueta de mis pantalones, cubierta por su falda. Sus manos desaparecen de la vista, solo para retirarlas bruscamente al tocar mi erección."

"Shizune casi se cae de mí del nerviosismo. Es como si ella no esperara que estuviera allí."

"La muestra repentina de ingenuidad es el contraste más fuerte de lo lejos que ella ha llegado hasta ahora, y me parece divertido. De repente, ella parece muy inmadura de nuevo. Una chica de preparatoria haciendo el papel de una mujer más agresiva."

scene evh shizune_hcg_tied_blush:
    yalign 0.0 xalign 0.8
show evh_hi shizune_hcg_tied_hisao2:
    yalign 0.0 xalign 0.8
with flash

"Ella toca mi pene curiosamente con su dedo índice, su rostro se enrojece mientras mueve el resto de sus dedos hacia el fondo. Sus movimientos son suaves y curiosos, y contradicen la mirada avergonzada en su rostro."

show evh shizune_hcg_tied_stare
hide evh_hi
with charachange

"Es probable que Shizune esté tan nerviosa como yo, así que estoy un poco aliviado cuando ella detiene su toqueteo exploratorio, pero entonces pienso en lo que seguirá."

"Ella podría intentar desabotonar mi camisa. Quién sabe qué diría al ver la cicatriz en mi pecho. Aún estoy acomplejado por eso, y puedo imaginar la preocupación en su rostro al verla; juntando sus dedos pensativa."


"Afortunadamente, en esta posición, ella no podría quitarme el chaleco sin arrancármelo. El temor se desvanece de mi mente. Ahora, solo estoy experimentando una mezcla extraña e incómoda de expectativa y nerviosismo."

show evh shizune_hcg_tied_blush
with charachange

"Una ligereza recién descubierta en mis rodillas me devuelve a la realidad, y puedo ver a Shizune parada sobre la punta de los dedos de sus pies deslizando su ropa interior por sus muslos. Cuando me ve mirándola, ella intenta cubrir mis ojos con una mano."

"Me pregunto exactamente cuándo comencé a sentirme atraído por ella. No solo atraído físicamente, sino cautivado por ella. Y, me pregunto por qué."
"Ella es bonita, pero por otra parte, también es muy combativa. No solo eso, sino que parece que le gusta ser así."
scene evh shizune_hcg_tied_blush_small
with charachange

"La manera como ella está actuando ahora, sin embargo, y en otras ocasiones, no encaja realmente en esa imagen. Estoy comenzando a pensar que quizás el hecho de que ella atara mis manos podría haber sido por más razones que solo las más obvias."

"Aun así, esa agresividad que ella muestra por doquier tan cómodamente como una tarjeta de presentación es real. No sé si ese tipo de actitud pueda ser considerada peligrosa o no. Si lo es, me pregunto en qué tipo de persona me convierte eso."

hi "Probablemente fue la primera semana que estuve aquí. Una semana no parece mucho cuando lo pienso, pero en ese momento sí lo fue. Aunque en esa semana pensaba bastante que mis días estaban contados, aun así parecía pasar tan lentamente."

"Aunque ella no puede oírme, me tranquiliza."

hi "Comencé a darme cuenta de que no tenía mucho de qué quejarme. Pero todavía hay…"

hi "Bueno, no importa."

scene evh shizune_hcg_tied_stare_small
with charachange

"Ella me mira, por la simple razón de que estoy hablando. Como no puede entender lo que estoy diciendo, Shizune se pone cada vez más nerviosa, pero no hace ninguna seña en respuesta."

scene evh shizune_hcg_tied_close_small
show evh_hi shizune_hcg_tied_hisao2_small
with charachange

"Shizune toma aliento bruscamente mientras se inclina sobre mi pene, intentando mantenerse erguida mientras se balancea encima de mí."

"La falda de su vestido cubre nuestras partes íntimas, y atrapa nuestro calor corporal debajo de ella como una carpa. Debajo de ella, siento un calor insoportable, y la mano de Shizune guiándome hacia ella solo lo aumenta."

show evh shizune_hcg_tied_kinky3_small
with flash

"En el momento en que la penetro, Shizune se estremece, y luego casi cae encima de mí. La sensación repentina nubla mi mente, y siento que irradian ondas de placer a través de mí desde ambos extremos de mi cuerpo."

"Se siente como si toda la parte inferior de mi cuerpo estuviera envuelta en el calor y la humedad del cuerpo de Shizune, capaz de sentir cada movimiento y cada estremecimiento cuando ella comienza a moverse."

show evh shizune_hcg_tied_kinky2_small
with charachange

"Shizune comienza a mover sus caderas, al principio lentamente, pero con su ritmo aumentando cada vez que ella se levanta casi por completo de mí, solo para volver a dejarse caer en el último momento."

scene evh shizune_hcg_tied_kinky2:
    zoom 1.0 yalign 0.1 xalign 0.7
    acdc_warp 6.0 xalign 0.9
with flash

"Al estar tan cerca de ella, puedo ver las gotas de sudor en su piel y el vapor que se forma en sus anteojos cuando se deslizan por su nariz, acercándose mucho a su boca antes de que ella los vuelva a empujar."

"Las puntas de sus dedos presionan mis hombros, aferrándose a ellos para mantener el equilibrio, empujando contra ellos para levantarse de mí, y luego bajando por mis brazos y agarrándose de mis muñecas y manos cuando ella vuelve a bajar."

scene evh shizune_hcg_tied_close_small
with flash

"Maniobrar de esta manera es difícil en el mejor de los casos. Shizune trata de apoyarse contra mí con sus pies mientras se mueve arriba y abajo. Intento besarla, pero solo logro tener éxito en tocar nuestras frentes, al menos no dolorosamente."

"Mis pensamientos vagan brevemente sobre si la puerta está cerrada con llave o no. Si fuera a abrirse ahora, probablemente tendría un ataque al corazón, literalmente. Y luego está la cuestión de quién abriría la puerta."

"El sentimiento de peligro solo sirve para hacer más torturadores los movimientos de Shizune, y desearía que se moviera más rápido, pero desde esta posición, puede que ni siquiera sea posible."

show evh shizune_hcg_tied_kinky1_small
show evh_hi shizune_hcg_tied_hisao2_small
with charachange

"Comienzo a mover las caderas hacia arriba al ritmo de ella, intentando entrar más profundo en ella."

"No me importa que mis movimientos estén sacudiendo la silla en la que estamos, creando un golpe fuerte cuando la silla de madera golpea el suelo de madera."

$ ksgallery_unlock("evhul shizune_hcg_tied_hisao2_small")
show evh shizune_hcg_tied_kinky3_small
with charachange

shi "¡… Nn…!"

"Su respiración se hace más fuerte, e incluso parecen escapar gemidos reprimidos de su garganta. Aunque es obvio que ella quiere contenerlos, aún son tan fuertes que cualquiera que esté parado en la puerta podría oírlos."

"Dejo de penetrar a Shizune, en parte porque es más difícil mantener su ritmo mientras comienza a meterse más y más en ello y a moverse más rápido de lo que puedo para lograr igualarla mientras estoy debajo de ella."

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.4)

window show

"Mi corazón se acelera tan rápido que casi puedo oír la sangre palpitar en mis sienes, y más preocupante aún, puedo sentir un leve latido en mi pecho. Dejo de pensar en la presión que siento entre mis muslos, aunque solo sea por un momento."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene white
with whiteout

"Ese momento, sin embargo, es suficiente. Combinado con su estrechez apretándose alrededor de mí y la sensación de su piel frotándose contra la mía, me tenso y disparo dentro de Shizune. Un sentimiento fugaz de poder y vuelo."

label es_S22x:

$ renpy.music.set_volume(1.0, 2.0, channel="music")
$ renpy.music.play(music_heart, fadein=2.0, if_changed=True)

scene evh shizune_hcg_tied_close:
    yalign 0.1 xalign 0.8
show evh_hi shizune_hcg_tied_hisao2:
    yalign 0.1 xalign 0.8
with Dissolve(2.0)

"Después de eso, escucho el sonido de mis latidos desacelerándose hasta que alcanzan su ritmo normal. Escucho el sonido de la respiración de Shizune mientras hace lo mismo."

hide evh_hi
with charachange

"Sus anteojos están ligeramente ladeados, y esta es la primera vez que ella no está jugando con ellos de algún modo. Quiero enderezarlos por ella, pero en el momento en que lo intento, recuerdo que no puedo. Shizune parece haberlo olvidado también."

stop music fadeout 7.0

scene evh shizune_hcg_tied_close_small:
    truecenter
    subpixel True zoom 1.2
    easein 10.0 zoom 1.0
with Dissolve(2.0)

"En vez de levantarse, ella ejerce presión contra mí en la silla para extender su alcance. Es casi como si esta fuera la única posición en la que puede pensar para desatar mis manos. Eso es lo que creo mientras la siento desatando mis muñecas."

"Sin embargo, ella no se baja de mí. Sus dedos suavemente se acarician contra los míos, a veces doblándose hacia adentro para moverse sobre mis palmas. Es curioso, pero me siento más conectado con Shizune a través de este simple acto que antes."

"Shizune se queda presionada contra mí de esta manera por un tiempo. Es un poco incómodo, pero me hace sentir feliz, como si pudiera quedarme así por horas."

scene black
with dissolve

label es_S23:

scene bg shizu_guesthisao
with locationchange

play music music_daily fadein 0.5

"Los días desde entonces han pasado tan rápido que el tiempo pareció escurrirse por mis dedos como agua. Cada vez que he intentado hablar con Shizune, ella o se ha ido a hacer mandados o está con Misha. Siento como si estuviera evitándome."

"No estoy sorprendido. Por supuesto que me molesta, pero creo que la forma en que está actuando parece bastante natural. Por otra parte, no es que haya pasado por esto antes."

scene bg shizu_living at left
show mishashort perky_smile_cas at center
with locationskip

"Cuando no puedo encontrar a Shizune, termino topándome con Misha, y cuando lo hago le pido que me ayude con mis señas. Sin embargo, siempre termina escapándose. Nos vamos después de hoy, así que estoy decidido a no dejarla escapar esta vez."

"Una vez regresemos a la escuela, seguramente vamos a tener que comenzar a trajinar con más asuntos del consejo estudiantil en preparación para el reinicio escolar. Quiero repasar mis señas tanto como pueda para entonces, incluso si es todo un día."

hi "¡Vamos, solo es tener un par de conversaciones en lenguaje de señas! Haces eso todo el tiempo. De hecho, lo estás haciendo ahora mismo."

show mishashort cross_laugh_cas
with charachange

mi "Guajaja~, ¿en serio, Hicchan? ¡Eso es gracioso!"

"Misha detiene temporalmente sus señas inconscientes para mover sus manos frente a su rostro para negarlo, pero luego rápidamente continúa haciendo gestos de todo lo que los dos estamos diciendo a nadie en particular."

show mishashort sign_confused_cas
with charachange

mi "Hicchan, eres tan persistente. De repente estás nuevamente interesado en el lenguaje de señas… ¿Podría ser que Hicchan quiera convertirlo en una profesión? ¡Eso no es justo, esa fue mi idea primero~!"

show mishashort cross_frown_cas
with charachange

mi "Deberías tener cuidado, Hicchan. Los tiempos cambian muy rápido~… Para cuando decidí que quería ser intérprete de lenguaje de señas, ya tenían celulares en los que la gente podía escribir párrafos enteros. ¡Asombroso~! ¡Pero no muy bueno para mí!"

"Como si ella supiera que otro aplazamiento no va a ser suficiente esta vez, Misha cambia su tono muy rápidamente a uno más compungido."

show mishashort perky_sad_cas
with charachange

mi "Lo siento, Hicchan, ¡es que estoy tan~ cansada~! Sobre todo últimamente, aunque estar con Shicchan es divertido, ¡ella tiene mucha más energía que yo! Como si fuera poco, enseñar sería muy~ agotador; ¡no tengo tanto aguante! ¡Lo siento~!"

"Ella no parece muy cansada, gritando la declaración con su típica alegría y vigor. Aunque sé que está mal de mi parte seguir molestándola así."

show mishashort sign_smile_cas
with charachange

mi "En realidad~, ¡Shicchan y yo estábamos planeando ir de compras! Es nuestra última oportunidad de comprar algunos recuerdos."

hi "Recuerdos, ¿eh? Casi olvidé que estaba de vacaciones."

hi "Entiendo lo que estás diciendo. Enseñar no parece tan fácil. Hideaki me pidió que le enseñara cómo hacer señas y estuve increíblemente perdido todo el tiempo."

hi "Bueno, me pregunto cómo resultará para ti cuando te conviertas en maestra de lenguaje de señas. No puedes cansarte tan fácilmente haciendo eso."

show mishashort perky_confused_cas
with charachange

mi "¡Sí, cierto, cierto~! ¡Espero que no!"

show mishashort hips_smile_cas
with charachange

mi "Hicchan, ahora estoy un poco preocupada. Pero~, ¡recuerdos! ¡Entonces~!, en otro momento, Hicchan. Ajaja jajaja~. ¿También quieres que te traigamos algo?"

"Solo porque entiendo no significa que no quiero que me enseñe. Aunque supongo que no puedo presionarla más ahora. Hasta estoy molesto por lo egoísta que se vería si lo hago. Me doy por vencido."

hi "No. No me traigan nada. Hablo en serio, no me sorprendan con una camisa graciosa o algo así, ¿de acuerdo?"

show mishashort cross_grin_cas
with charachange

mi "Jejeje~."

"No me gusta como suena eso."

hide mishashort
with charaexit

"Poniéndose sus zapatos, ella grita adiós a la casa, por lo demás vacía, y abre la puerta para irse, dejando entrar un soplo frío de aire fresco hacia el pasillo."

"Un mechón de cabello oscuro asomándose desde el marco de la puerta me dice que Shizune está esperándola afuera."

hi "Buenos días."

show mishashort invis:
    center
    xpos 0.8
show shizu invis:
    center
    xpos 1.0
with None

show bg shizu_living at right
show shizu adjust_happy_cas at tworight
show mishashort perky_smile_cas at center
with Dissolvemove(2.0)

"Misha traduce por mí desde más allá de la entrada, y Shizune se gira para darme un pequeño saludo."

"Aunque es mínimamente diferente de sus típicos saludos informales, allí hay una inconfundible vacilación. Me deja con un sentimiento distante y vagamente vacío."

show shizu behind_blank_cas
with charachange

shi "…"

show mishashort hips_grin_cas
with charachange

mi "¡Hicchan, te levantaste temprano~! ¿Estoy interrumpiendo una conversación?"

hi "Estaba intentando hacer que Misha me enseñara cómo hablarte, pero supongo que yo estaba siendo impaciente, y eso puede esperar. Ustedes dos estaban planeando ir de compras hoy, de todos modos."

"Estando Misha allí, olvido hacer las señas de mis palabras cuando las digo. Desafortunadamente, ya que Shizune se movió para ocupar la puerta, Misha está detrás de ella."

"Este breve desajuste en nuestras posiciones significa que lo que digo se pierde totalmente en ella."

show shizu basic_angry_cas
with charachange

ssh "No te entiendo en absoluto."

"Hay cosas que quiero decir que no puedo poner de una manera que ella entendería, y hay conversaciones enteras que ella podría tener que yo no lograría entender. Quiero decirle ahora que no será así por mucho tiempo."

hide shizu
hide mishashort
with charaexit

"En vez de eso, solo digo “no importa” y les digo que la pasen bien, y luego me despido de ellas."

"Parece que nadie está en casa hoy, así que me siento con un libro en la silla más grande y de aspecto más cómodo de la sala de estar. No es un libro de lenguaje de señas, sino una de las novelas que saqué de la biblioteca en mi primera semana."

"Eso fue hace mucho tiempo. Realmente debería comenzar a leer ese montón de libros que pedí prestados, o al menos devolverlos."

stop music fadeout 2.0

show jigoro neutral at center
with charaenter

"Dieciséis páginas más tarde, Jigoro entra en la sala, con una pila de papeles en una mano y su espada girando ociosamente como un bastón en la otra, sacudiéndose casualmente el agua de una ducha reciente de su cabello."

show jigoro angry
with charachange

show jigoro angry at Position(ypos=1.15)
with charamove

"Al ser visto haciendo algo tan poco caballeroso, se congela como un ciervo ante los faros de un auto, y lentamente se mueve, ardiendo con una furia poderosa pero sin fundamento mientras se sienta en el sofá a unos metros de distancia."

"Esta es solo la tercera vez que lo he visto y ya estoy comenzando a sentir náuseas en reacción. Supongo que en cierto modo esto podría ser considerado una especie de carisma."

"Aún no he dicho nada y él ya no parece muy contento. Probablemente sea una mala idea provocarlo, y solo hablar con él puede contar como provocarlo. Sin embargo, no puedo dejar de pensar en las situaciones alternativas que podrían ocurrir."

"Digamos que no abro mi boca para nada y me retiro, quizás para irme a leer en mi habitación o afuera. Eso sin duda sería recibido como un insulto imperdonable. Él probablemente me diría que me detenga y acabaría conmigo."

"Sea como sea, no muy cortés de mi parte."

hi "¿Qué está leyendo?"

show jigoro smug
with charachange

play music music_another fadein 6.0

hx "El borrador de mi autobiografía. Es la historia de un hombre que despierta para encontrar a un huésped no invitado en su sala de estar, sentado en su silla y leyendo basura literaria superficial."

"Apenas he comenzado a leer el libro, ni siquiera tengo una opinión sobre él todavía. Ya puedo ver cómo va a desarrollarse esta conversación, así que bien podría intentar llevarla a una dirección diferente."

hi "¿Dónde está Hideaki?"

show jigoro angry
with charachange

hx "Hasta haces preguntas groseramente. Vergonzoso. Aparte de eso, ¿por qué me harías una pregunta tan estúpida como esa? ¿Cómo voy a saberlo? ¿Soy el guardián de mi hijo?"

"“Bueno, usted es su papá, y parece que él vive aquí, así que…”. Pero, supongo que no puedo decir eso, por muy tentador que sea."

"Me doy por vencido. Ya intenté tener una charla trivial con él y fallé. Es como tratar de hablar con una pared de ladrillo que también te odia. Esa es mi señal para irme y escudriño en mi billetera para ver si tengo suficiente dinero para ir al cine."

"Cuando estoy a punto de levantarme, tengo mis dudas. Estoy muy cansado de estar intentando restarle importancia a mis situaciones problemáticas tratando de alejarme constantemente de ellas."

"Es hipócrita de mi parte enfadarme con Misha por intentar aplazar las cosas cuando hasta yo huyo de mi propia novia. Cuando Jigoro intenta detenerme, casi me alegro, aunque ya no tengo ninguna intención de irme."

show jigoro neutral
with charachange

hx "Espera."

"Lo dice con mucha autoridad pero nada más, como si fuera una idea de último momento particularmente imponente. Solo una persona muy poderosa o muy arrogante puede decirle a alguien que espere de esa manera. Estoy algo impresionado."

show jigoro smug
with charachange

hx "Estás en el consejo estudiantil con Shizune, ¿no es así? ¿Cuál es tu trabajo allí?"

hi "No creo que haya roles específicos, aparte del de presidente. Shizune siempre está intentando reunir gente para que ayude aquí y allá."

hi "Por lo general podríamos conseguir, digamos, una persona para que eche una mano, pero si no, nosotros tres hacemos lo que se necesite hacer."

"Se me cruzó por la mente un par de veces, cuando la vi por primera vez, que la mirada inquietantemente analítica de Shizune podría ser por su sordera, pero resulta que es un rasgo compartido por todos los demás en su familia."

show jigoro neutral
with charachange

hx "¿Y eso te parece bien?"

hi "¿Por qué no lo sería?"

show jigoro laugh
with charachange

hx "¿Shizune, tú, y esa chica de pelo rosado? ¿Ese es realmente todo el consejo estudiantil?"

show jigoro smug
with charachange

hx "Con un consejo estudiantil tan pequeño, ni siquiera se molestarían en realizar elecciones. Voy a tratar de adivinar y decir que tú no te uniste al consejo estudiantil, Shizune te metió en él. Dijiste que no sabes exactamente cuál es tu cargo."

hx "Eso tiene sentido. Supongo que si ni siquiera fuiste elegido, no podrías haber esperado saberlo. Después de todo, si no eres elegido, en realidad no eres nada."

show jigoro laugh
with charachange

hx "Nadie va a respetar un consejo estudiantil como ese. ¿Un cuerpo no electo de tres personas intentando gorronear con el equivalente a trabajadores temporales?"

hx "Debe ser una escuela deplorable si tres chicos que hacen una fiesta de té pueden manejar todos los asuntos."

hi "¿Y qué tiene que ver lo pequeño que sea? Si el consejo estudiantil logra hacer las cosas, ¿no es suficiente?"

hi "No es solo un juego, tampoco. Tal vez realmente debería ir un día a la escuela. Si va allí en los días correctos, hasta podría ser capaz de ver lo que Shizune puede lograr."

show jigoro angry
with charachange

hx "¿Crees que tengo tanto tiempo libre que puedo darme el lujo de ir tan relajadamente a tu pueblo remoto y ver las hazañas de autoengrandecimiento de mi hija? Nunca he estado más disgustado en mi vida."

hi "Lo que usted está diciendo es que bien podrían no tener un consejo estudiantil, pero el hecho es que hay uno. Y Shizune fue elegida para él, y para ella no es una posición sin propósito. De hecho, ella trabaja muy duro por ello."

show jigoro laugh
with charachange

hx "Suenas como alguien que votó por ella."

hi "No, no estuve allí para eso."

show jigoro neutral
with charachange

hx "Ja. Ni siquiera votaste por ella. Bueno, aparte de eso, ¿por qué no le preguntas a Hideaki sobre esto?"

show jigoro smug
with charachange

hx "Shizune ha querido ser presidenta de consejo estudiantil de preparatoria desde la secundaria. Ella le hacía leer todos sus discursos de práctica, haciéndole perder su tiempo. ¿Por qué razón?"

"Todo este tiempo, ni siquiera ha levantado la mirada mientras hojea su manuscrito. Se está volviendo cada vez más frustrante."

hi "Porque no es un juego; no dirigimos la escuela, pero no es que simplemente estemos jugando a ello y sin tomarlo en serio."

"Me pregunto si es tan malo no ser un purista."

show jigoro angry
with charachange

hx "He estado en tu escuela. En serio… Los estudiantes allí…"

"Ya puedo pensar en un millón de cosas que podría decir, y me estoy preparando para que se me caiga el alma a los pies al escuchar cualquiera de ellas. Es curioso, probablemente sean cosas que yo haya pensado antes."

hx "Ni siquiera tienen el deber de limpiar."

"Eso no era lo que esperaba en absoluto. También está equivocado."

hi "Claro que sí. Yo debería saberlo, logro escaparme de ello ya que estoy en el consejo estudiantil."

show jigoro neutral
with charachange

"El concepto de estar equivocado confunde a Jigoro. Debería aprovechar esta oportunidad para ir al ataque. Es realmente extraño que esté pensando de esta manera por una simple conversación."

hi "Parece como si la última vez que estuvo allí fue realmente hace mucho tiempo."

hi "Si puede escribir calmadamente unas memorias, puede hablar con Shizune de vez en cuando. ¿No cree que ella tenga cosas de las que esté orgullosa?"

hi "Así somos los jóvenes. Tenemos cosas de las que estamos orgullosos. Si está escribiendo una autobiografía, debería entenderlo."

"Una oportunidad así, y la eché a perder. No sé cómo yo esperaba que reaccionara. Tal vez introspectivamente, pero Jigoro solo parece enojarse cada vez más."

"Pero mientras lo hace, también parece más calmado, en cierto modo. Más seguro de sí mismo y en control."

show jigoro angry
with charachange

hx "¿Quién te crees que eres para asumir que mi vida es tan fácil? Ni siquiera has leído mi biografía, pero eres capaz de decirme cómo debo manejar todos mis asuntos, incluyendo lidiar con mi propia hija. Nunca podrías entender."


hx "Aun si me levantara de este sofá, caminara hacia ti en este instante, y te golpeara en la frente con nudilleras de acero con una edición resumida de la historia de mi vida en ellas, dejando mi biografía impresa en tu cara, no lo entenderías."

hx "Por doce años, Shizune ni siquiera me habló, aunque contraté a varios tutores e intérpretes de todo tipo para tratar de hacer que se volviera normal. No es tan simple como piensas que es."

show jigoro smug
with charachange

hx "Si ella no quiere molestarse conmigo, entonces está bien. Asumo que es normal. ¿Cuándo fue la última vez que hablaste con tus padres?"

"Ha pasado mucho tiempo, y me siento avergonzado. Más porque me atrapó que por la facilidad con que podría haber hecho una llamada telefónica a mis padres o enviarles un correo electrónico, o incluso una carta, y no lo hice."

"Saber esto solo me hace sentir más avergonzado."

show jigoro laugh
with charachange

hx "Eso pensé."

hi "Si quisiera ver a mis padres, no podría. Esto es diferente. No está tan lejos de ella, ¡solo hay que tomar un tren!"

show jigoro neutral
with charachange

hx "Eso es suficiente. No es no. Eres muy persistente. Si tan solo fuera por algo que importara. No puedo ver qué puedes haber aprendido de mi hija además de eso y de cómo responderle insolentemente a la gente. ¿Eso es todo?"

stop music fadeout 10.0

"La respuesta es sí. No era así de persistente o de argüidor antes de conocer a Shizune y a Misha."

"Después de todo, antes de conocerlas, solo experimentaba una pequeña muerte. Es un misterio el porqué me negué a unirme al consejo estudiantil en primer lugar."


label es_S23a:

"Me tomó un esfuerzo monumental solo presentarme en mi primer día allí. Podría haberme sometido a cualquier persona y a cualquier causa. Simplemente podría haber sido casualidad que el consejo estudiantil me atrajera tan poco que luchara contra él."



label es_S23x:

"Posiblemente fue por intentar escapar tanto de sus quejas que pude recuperar mi energía. Es una bonita idea."

"Pienso de nuevo sobre por qué aún estoy aquí. Discutir con Jigoro es inútil, pero creo que casi lo estaba anhelando."

"Y él tiene razón, no puedo entenderlo. Y aunque lo hiciera, no le importaría. Soy un piojo que se arrastra sobre una ballena: completamente insignificante."

"Él tiene una confianza que yo no tengo. Shizune la tiene, y podría ser que la razón por la que estoy aquí ahora, en una discusión casi a gritos con su padre, es porque algo de esa valentía se pegó en mí. Sin embargo, no tengo nada para continuarla."

"Aun así, lo odio. No sé qué puedo hacer. Hace unos meses, creo que lo habría golpeado y dejaría que las consecuencias tuvieran lugar como puedan. Pero ahora, no puedo tomar ese riesgo. Si él fuera a devolverme el golpe, probablemente me mataría."

"Así que al final, la única cosa que puedo hacer es mirar a Jigoro en silencio, sabiendo que no tengo respuesta, y odiarlo, y sentirme completamente desconcertado. Curiosamente, él lo toma como un desafío."

show jigoro angry
with charachange

hx "Hmf. Pues, bien. Diviértete con eso."

show jigoro invis at center
with dissolvecharamove

"Levantando su espada y usándola para ponerse de pie, se da la vuelta y de manera casual se retira de la sala. Quiero lanzarle mi libro, pero estoy feliz de estar finalmente solo, aunque ya no estoy de humor para leer más."

scene black
with dissolve

label es_S24:

scene bg city_station
with locationchange

"Nuestro viaje de regreso sigue retrasándose de una manera u otra. Shizune y Misha regresan tan tarde que no sirve de nada irnos y terminamos quedándonos un día más."

"A la mañana siguiente, perdemos el tren por un solo minuto y luego los dos siguientes no llegan. Perdemos el cuarto tren porque me alejé para conseguir una bebida mientras tanto. Shizune no estaba muy feliz por eso."

scene bg school_dormhisao
with shorttimeskip

play music music_dreamy fadein 2.0

"Para cuando finalmente regreso a mi habitación, me siento muy cansado, aunque pasé la mayor parte del viaje de regreso durmiendo. No puedo decir que es solo por hoy; esto parece un síntoma habitual al viajar. No es la primera vez que ha pasado."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

scene black
with shuteye

window show

"Si nadie lo ha hecho antes que yo, podría hacer una tesis sobre ello, tal vez la envíe a una revista médica. “Síndrome del Regreso de un Viaje”. No muy creativo. Me quedo dormido antes de que pueda pensar en un mejor nombre."

window hide

play sound sfx_doorknock
with Pause(1.0)

scene bg school_dormhisao
with openeye

$ renpy.music.set_volume(1.0, 1.0, channel="music")

window show

"Un golpe fuerte en mi puerta me despierta solo a unas pocas horas en mi siesta. Estoy molesto porque había estado en medio de un sueño que no puedo recordar, al haber sido despertado en medio de él. Pero estoy seguro de que era uno bueno."

"Me pregunto brevemente quién sería, pero no es como si recibiera muchas visitas, así que estoy seguro de que es Kenji."
"Espero que solo esté preparando el comité de bienvenida y no vaya a pedirme dinero otra vez. Si así fuera estaría casi conmovido."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene black
with shuteye

"Aunque no lo suficiente para combatir el deseo de darme la vuelta y seguir durmiendo."

stop music fadeout 5.0

window hide

with Pause(4.0)

scene bg school_dormhisao
with openeye

window show

"Unas pocas horas más tarde, despierto de nuevo e inmediatamente observo un sobre en el suelo."

"Debe ser algo que llegó al correo mientras no estaba. Ese es el departamento de Shizune y Misha, así que me pregunto si pasaron por aquí para dármelo, o quizás alguien las reemplazó en su ausencia y le dijo a Kenji que lo pasara…"

show letter_insert:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_rain fadein 4.0

"Cuando lo recojo, cualquier remanente de somnolencia en mí desaparece al instante."

"Aunque el nombre del remitente no estuviera en él, habría sabido de quién era al mirar el sobre en sí, dándome cuenta de por qué se veía tan familiar. Reconociendo la delicada caligrafía que la dirige."


"Es de Iwanako. Al principio, no puedo creerlo, pero no sería muy difícil para ella localizarme si lo quisiera."

"Por supuesto, no había pensado que quisiera hacerlo. Ella quizás fue mi novia por solo cinco segundos. Después de eso, apenas nos hablábamos el uno al otro."

show letter_insert:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide letter_insert
with None

"Sería muy fácil dejar esta carta en algún lugar y olvidarme de ella. Una parte de mí quiere hacer eso. O botarla, sin leerla. Por qué quiero hacer estas cosas, no lo sé. Sería fácil hacerlas. Más fácil que leerla."

scene ev hisao_letter_open
with locationchange

"Abriendo el sobre con la punta de un bolígrafo, estoy sorprendido por la extensión de la carta que se desparrama."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

$ written_note("Querido Hisao,\n\n¿Cómo estás? Espero que estés bien y feliz en tu nueva escuela. Todos aquí te extrañan. Casi todo nuestro grupo de segundo año fue colocado junto en el grupo 3-1 para el último año, así que hemos estado bastante cómodos desde el principio. Estoy segura de que habrías sido asignado a este, también.")

$ written_note("Los ánimos entre los de tercer año parecen ser de muchas ansias por los exámenes finales, aun estando tan lejos. Los maestros nos fastidian por ello todo el tiempo, incluso el viejo señor Tachibana quien es, por cierto, nuestro maestro de cabecera este año. ¿Podrías creerlo? Estaba segura de que se retiraría después de nuestro segundo año, pero aquí está, dándonos lata a todos para que estudiemos para los exámenes.\n")

$ written_note("Creo que cosas como esa son la principal razón de que los ánimos entre los de tercero sean de tanto nerviosismo. Debo admitir que de algún modo también estoy perdiendo confianza en mí misma, a pesar de que siempre me ha ido razonablemente bien en los exámenes.\n\n\n\n\n")

$ renpy.music.set_volume(1.0, 1.0, channel="music")

window show

"La charla me hace sentir nostálgico. Es casi como si estuviera en el hospital de nuevo. De vez en cuando Iwanako me visitaba y me contaba lo más importante que estaba pasando en una clase a la que, incluso entonces, presentía que nunca volvería."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

$ written_note("Es tan extraño pensar que ya estamos en el último año, ¿no es así? El tiempo realmente ha pasado volando. Me pregunto adónde fue. Los nuevos de primer año parecen tan jóvenes y de algún modo tan inocentes. No dejo de preguntarme si yo era como ellos en mi primer año. He estado sintiéndome así de nostálgica durante todo el primer trimestre.\n\n\n")

show ev hisao_letter_open:
    "ev hisao_letter_open_2" with locationchange
with None
$ ksgallery_unlock("ev hisao_letter_open_2")

$ written_note("Hay otras cosas que quiero decir. Te estoy escribiendo porque sentí que hay cosas que debería haber dicho después del incidente en aquel invierno. Realmente me arrepiento de no haber sido capaz de decirlas en persona, y no tengo excusa para ello.\n\n\n\n\n")

$ written_note("La verdad es, las veces que te visité en el hospital hicieron que me preocupara por ti. No estoy hablando de tu salud. Parecías haberte distanciado y desanimado más. Era natural después de que ocurriera algo como eso, estoy segura, pero de alguna manera tuve la sensación de que habías renunciado a algo en ese entonces. ¿La felicidad, tal vez?\n")

$ written_note("Quería por algún medio expresar mis sentimientos, pero las palabras correctas no venían a mí. No podía decir algo para consolarte. Realmente siento no poder haberte apoyado cuando más lo necesitabas, aunque me gustes tanto. Por lo menos ahora, finalmente, puedo ser más honesta.\n\n\n\n")

$ renpy.music.set_volume(1.0, 1.0, channel="music")

window show

"Qué momento tan conveniente para que ella redescubra su sinceridad. Bueno, mientras lo pienso, sé que ella tiene razón. “Distanciado y desanimado” es una buena manera de describirlo. Y tal vez también me había dado por vencido."

"Pesa en mi corazón el recuerdo de cuando estaba en el hospital, sintiéndome tan amargado cuando ella finalmente dejó de aparecer."

"No estaba sorprendido, y no tenía derecho a estarlo. ¿Cómo podría no dejar de ir cuando era lo único que esperaba de ella?"

"Ella me visitó durante solo seis semanas después del incidente. Si me alejé de ella, fue porque ya podía sentirla alejándose de mí desde el momento en que aparecía."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

$ written_note("Si pudiera volver a aquellos días silenciosos en febrero y marzo, te diría que no renunciaras a ti mismo. Eso es lo que diría. Quizás no te hubieses alejado tanto si tan sólo hubiera dicho algo. Espero que hayas podido recuperarte por tu cuenta.\n\n\n\n")

$ written_note("Ahora que la distancia entre nosotros es también física, se siente también más definitiva, de algún modo. Me pregunto si nos encontraremos de nuevo. ¿Tal vez sea mejor si no? Aun así, si te gustaría mantener correspondencia conmigo, por supuesto que puedes escribirme de vuelta. Me agradaría mucho escuchar sobre tu nueva escuela y cómo te está yendo. Te deseo todo lo mejor.\n\nAtentamente, Iwanako")

$ renpy.music.set_volume(1.0, 1.0, channel="music")

window show

"Es un sentimiento extraño. Sé que nunca volveré a saber de ella."

"Si ella realmente quisiera seguir en contacto, no habría elegido un medio como el correo común para hacerlo."

"Si pudo conseguir mi dirección, entonces mi correo electrónico o mi número telefónico no habrían sido tanto trabajo, si ella los hubiera querido. Esto es solo un adiós."

stop music fadeout 4.0

"Exhalo, solo hasta ahora dándome cuenta de que había estado leyendo con la respiración contenida. ¿Ahora quién está siendo distante, Iwanako? Pero tal vez realmente sea lo mejor."

"Para que ella tome un bolígrafo y me escriba esta carta, solo puede ser porque se sentía culpable por cómo terminaron las cosas."

"Que ella se viera afectada por cómo nos distanciamos de la vida del otro me hace sentir una especie de felicidad melancólica."

"Casi quiero agradecerle, y solo no lo hago porque sé que ella no querría que yo respondiera."

play sound sfx_doorknock

scene bg school_dormhisao
with locationchange

"Alguien toca a mi puerta, y luego se abre de todos modos casi una milésima de segundo después. Olvidé cerrarla con llave, estúpidamente."

ke "¿Qué tal, hombre? ¿Por qué está abierta tu puerta?"

"Corro hacia la puerta, más rápido de lo que probablemente sea médicamente seguro para mí hacerlo, para poder evitar que Kenji vea las montañas de píldoras a solo un metro de distancia de él, bloqueadas de su vista solo por la puerta."

"Y luego está la carta que estoy sosteniendo. Si él pregunta por ella, no creo que pueda inventarme algo convincente."

"A casi un metro de distancia de él me doy cuenta de que su visión es tan mala que probablemente nunca fue un problema. Ni siquiera me vio prácticamente a punto de empujarlo hacia atrás por el marco de la puerta."

scene bg school_dormhallway
show kenji tsun_close at center
with locationchange

play music music_kenji fadein 0.5

ke "Oye, ¿pero qué demonios, hombre?"

hi "¿De qué estás hablando? Tu habitación tiene mil millones de cerraduras en ella, pero ahora mismo irrumpes en las puertas de los demás."

hi "Ni siquiera esperaste un segundo después de golpear antes de que intentaras abrir la puerta, fue casi simultáneo. Ya estabas abriendo la puerta mientras golpeabas."

show kenji happy_close
with charachange

ke "¿Ves? Es exactamente por eso que tengo todas esas cerraduras. Es un mundo frío e indiferente allí afuera, un mundo de intrusos. Ahora también lo entiendes."

show kenji neutral_close
with charachange

ke "Acabé de enseñarte una valiosa lección, viejo. El conocimiento es poder. ¿Por qué me estás gritando? Soy un héroe."

show kenji tsun_close
with charachange

ke "Mírate… ni siquiera cerraste con llave tu puerta. La mujer promedio podría haberte matado ya mil millones de veces, y luego haberte reemplazado con un clon femenino indistinguible del original. Casi me pasó a mí."

"Ignorando la última parte, ya que es muy confusa, es curioso que él dijera eso. Fue incapaz de detenerme al empujarlo de frente, pero al parecer una mujer podría haberme matado mil millones de veces."

"Si este hombre es un héroe, todos estamos condenados."

show kenji happy_close
with charachange

ke "¿Qué es eso que tienes allí?"

"De alguna manera, él es capaz de ver la carta todavía en mi mano. Con lo que he estado moviéndola en el aire, no es de extrañar. La vuelvo a doblar rápidamente, pero tengo cuidado de no ocultarla detrás de mí o algo así. Eso sería muy sospechoso."

"Parece que estoy más nervioso de lo que pensaba por el hecho de que Iwanako me escribiera."

hi "Recibí una carta."

show kenji neutral_close
with charachange

ke "Ah, sí, yo la puse ahí. Estaba durmiendo, y entonces desperté porque escuché explosiones."

ke "Me puse mi casco y luego me asomé afuera para ver qué estaba pasando, pero solo era esa mujer del consejo estudiantil golpeando a tu puerta. Era la que no tiene pelo rosado."

show kenji tsun_close
with charachange

ke "Ella estaba golpeando tan fuerte que era obvio que estaba llena de furia asesina. Furia hacia ti. Entonces de alguna manera me sintió detrás de ella, e intenté escapar, pero era demasiado tarde. Me sorprendió y comenzó a señalar a la puerta."

"Abro mi boca para decirle que ella es sorda, pero decido no hacerlo. Por varias razones."

ke "Realmente no le entendía, y se enfurecía cada vez más y más, como un anciano tratando de usar un teléfono con pantalla táctil."

show kenji happy_close
with charachange

ke "Ella iba a matarme. Matarme y reemplazarme con una versión mujer de mí. Pero entonces la luz del sol se reflejó en mis anteojos y la cegó, salvando mi vida."

show kenji neutral_close
with charachange


ke "Fue como, contempla, rayos ópticos. No entiendo cómo alguien con anteojos puede ser herido con anteojos. Ella también los usa, debería ser inmune a sus rayos mortales… pero bueno. Me dio un sobre con tu nombre en él y se fue."

show kenji happy_close
with charachange

ke "Claramente, ella estaba buscando sangre, así que mentí y le dije que no estabas. Creo que no estabas, ¿cierto? He estado tratando de pedirte si querías ayudarme con mi tarea desde hace una semana, pero seguía sin recibir respuesta."

ke "¡… Bienvenido de nuevo, hombre!"

hi "Gracias."

show kenji neutral_close
with charachange

ke "Sí, así que ella me dio el sobre y tenía tu nombre en él. No quería quedarme con él, porque, ¿qué tal si fuera una bomba? Así que solo lo metí debajo de tu puerta cuando ella se fue."

ke "Iba a decírtelo, pero regresaste antes de que pudiera hacerlo. Por lo menos no es una bomba."

hi "Vaya, gracias. No voy a ayudarte con tu tarea de matemáticas, porque, ¿qué tal si tu libro de texto de matemáticas es una bomba?"

show kenji tsun_close
with charachange

"Se ve devastado, y también como si estuviera considerando la posibilidad de que realmente podría ser una bomba. Supongo que es posible, ya que realmente nadie usa tanto un libro de matemáticas."

scene bg school_dormhisao
with locationchange

"Tiro la carta sobre el tocador detrás de mí y me doy la vuelta para irme, cerrando la puerta detrás de mí de un golpe mientras lo hago."

"La puerta choca contra la punta del zapato de Kenji y rebota, abriéndose, mientras él salta dando vueltas por un momento, actuando como si doliera mucho más de lo que debería."

show kenji neutral at center
with charaenter

"Antes de que lo sepa, él ya está dentro de mi habitación. Soy incapaz de detenerlo antes de que recoja la carta, extrañamente ignorando las torres de frascos de píldoras que la rodean."

hi "No leas correo que no es tuyo."

show kenji happy
with charachange

ke "Vamos, ¿qué es? ¿Una carta de amor de tu novia? ¿Incluyó algunas fotos? ¿Fotos sexis?"

play sound sfx_dropstuff
stop music fadeout 4.0

"Recostándose contra el tocador y sin prestarle atención a los frascos que riega por todo el suelo al hacerlo, Kenji lee en silencio la carta de Iwanako."

"El proceso parece durar una eternidad, y con lo cerca que la tiene de su rostro, hace que parezca como si tratara de comérsela."

show kenji tsun
with charachange

ke "¿Quién es “Iwanako”?"

hi "Mi ex-novia."

play music music_night fadein 4.0

show kenji neutral
with charachange

ke "Ex-novia, ¿eh? Esta es la carta de ruptura, entonces. Pensé que eran un mito."

hi "No. Supongo que lo es, pero en serio, ella ha sido mi ex-novia por un tiempo. De todos modos, creo que ya lo superé."

"Kenji hace un gesto de aprobación, claramente aliviado de que no voy a llevar esto hacia una dirección incómoda, aunque casi quiero hacerlo ya que le dije que no la leyera."

show kenji happy
with charachange

ke "Sí, esa es una buena actitud. Está bien, yo también tuve una mala ruptura, pero no puedes dejar que eso te desanime. Quiero decir, solo mírame."

hi "Ehhhh…"

ke "Pero, oye, te escribió una carta. Tal vez ella quiere que vuelvan a estar juntos, ¿eh? Lo dice justo aquí, escríbele de vuelta. Deberías hacerlo. ¿Ella es linda?"

"Para un tipo que cree que las feministas están trabajando para esclavizar a los hombres de todo el mundo, él realmente está interesado en las chicas lindas."

hi "Tengo novia. Además, mira el contexto, ella no quiere que le escriba de vuelta. Solo porque eso es lo que dice, no es lo que quiere decir."

show kenji neutral
with charachange

ke "Pero eso es lo que ella escribió. Esta chica roca-pez-niño sin duda aún te quiere. Incluso lo dice justo aquí."

hi "Lo leí, sé lo que dice. Te lo dije, tienes que mirar el contexto. Dijo que me alejé de ella, y todo allí muestra que ella lo aceptó."

hi "Creo que la razón por la que me escribió es que solo quiere, supongo, despedirse de forma amistosa. Pero hemos terminado, ella no quiere que volvamos a estar juntos o lo que sea que estés pensando."

"Mientras más lo pienso, me parece que solo estoy intentando hacer excusas para mí mismo. No es bueno estar en ese lugar."

"Estoy convencido de que ella no quiere que le escriba de vuelta. Puedo vivir con eso. Si fuera a escribirle de vuelta y recibiera una respuesta menor a la deseada, o ninguna respuesta, entonces me sentiría defraudado."

"Quizás el temor a eso es la razón por la que estoy intentando justificar mi decisión. Podría ser, pero no quiero pensar en ello. La idea es extrañamente repulsiva."

hi "¿Por qué es tan importante para ti, de todos modos?"

show kenji happy
with charachange

ke "Porque deberías escribirle de vuelta. Ella quiere que lo hagas. Quiero ver cuál va a ser la respuesta."

show kenji neutral
with charachange

ke "Maldición, ni siquiera tiene que ser una carta agradable. Eso también es genial, pero podrías escribir una carta airada y llamarle la atención. Esa es mi nueva estrategia de ataque, solo voy a llamarle la atención a las mujeres. Deberías intentarlo."

hi "Aunque ella me escribió una carta, tienes que entender lo que eso significa. Escribirle una carta a alguien es diferente ahora. No es algo que simplemente haces. No en este tipo de situación."

hi "Puedes tomar tu teléfono y llamar a alguien al otro lado del mundo en un instante, y hablarle casi como si estuviera contigo. O enviarle un correo electrónico; será notificado inmediatamente de que lo recibió y puede responderlo, así como así."

hi "Una carta puede ser una cosa personal, pero ella quería mantenerse alejada de mí. No es que pueda aparecerme por allí y visitarla."

hi "Si tuviera su número, podría llamarla, o si tuviera su correo, podría enviarle un correo. Si ella realmente quisiera volver a escuchar de mí, habría dejado uno de esos allí."

"Me siento tonto por asegurarme continuamente de que no estoy sorprendido porque Iwanako me escribiera, cuando es muy obvio que lo estoy."

show kenji tsun
with charachange

ke "Podría ser como algo gradual para ella. Podría ser muy tímida para llamarte. Recuerdo que mi novia siempre me enviaba mensajes de texto porque era muy tímida. Era muy molesto, hombre."

ke "En realidad me importaban una mierda los teléfonos así que no me interesaban, y resulta que tenía que pagar por cada uno de ellos. Pero no me gustan los teléfonos así que ni siquiera podía llamarla de vuelta para decirle que dejara de hacer eso."

show kenji neutral
with charachange


ke "Pero lo hice de todos modos. Le llamé la atención. Hasta usé un teléfono. Literalmente fue la llamada de atención."

hi "Supongo que lo fue."

"Aunque él tenga razón, significa que Iwanako aún quiere mantener su distancia de mí. Ella “no está lista” para conversar conmigo cómodamente."

"¿Por qué? ¿Soy una especie de bicho raro? En ese caso, no me siento más tranquilo por sus acciones de todos modos. Tal vez lo estoy pensando demasiado, pero no lo sé."

"Kenji no puede pensar en nada que decir de eso, y el silencio que sigue es tan incómodo y pesado que comienzo a contar los segundos hasta que él se invente una razón para pedir permiso e irse."

show kenji tsun
with charachange

ke "La extraño…"

hi "¿A tu ex?"

ke "Sí. Aunque estaba loca, era agradable estar con ella."

ke "Me duele la espalda. Si ella todavía estuviera por aquí podría decirle que me masajeara. Tampoco sé cómo usar un horno. Extraño la comida horneada."

ke "E íbamos a veces a jugar bolos en el pasillo. También extraño eso. Tuve que jugar yo solo a los bolos en ese último festival."

hi "¿Juegas a los bolos en el pasillo? Vas a golpear a alguien."

ke "Ella solía decir eso todo el tiempo…"

"Kenji suspira con nostalgia, claramente sin apreciar lo mucho que alguien podría resultar herido al resbalar sobre un pino de bolos. Al parecer, tampoco lo hizo su novia, ya que ella jugaba bolos con él."

"Qué extraña definición del amor, pero supongo que es algo."

hi "Quizás tú deberías escribirle una carta. Si ella te responde, puedes casarte."

stop music fadeout 0.3

show kenji rage
with charachange

ke "¿¡Casarme!? No. No no no. No."

hi "Bueno, está bien. ¿Pero por qué no? Ella claramente te gusta, a pesar de que odias a las mujeres."

show kenji tsun
with charachange

play music music_kenji fadein 2.0

ke "¡Feministas! Mujeres no, feministas. Hay una diferencia. Hay mujeres no feministas. Maldición, tu discriminación es increíble. Correlación no es igual a causalidad. Aunque ella esté loca y sea mujer, no significa que sea una mujer loca y feminista."

show kenji neutral
with charachange

ke "Es como que la ausencia de evidencia no es la evidencia de ausencia. Si eso es cierto, entonces por la propiedad relativa, la presencia de evidencia no es igual a la evidencia de presencia."

hi "En realidad, creo que lo es. Y no creo que se llame la propiedad relativa."

show kenji tsun
with charachange

ke "¡No, cállate, son matemáticas! ¿Estás diciendo que las matemáticas están mal?"

"Creo que él está mal."

"Así que hasta Kenji tiene alguien que le gusta. Estoy tentado en preguntar por qué él y su ex terminaron, o indagar por más información en general, pero no debería. Eso no solo sería entrometido, sino que él podría devolverme la pregunta."

stop music fadeout 8.0

"Esta conversación me hace pensar en Shizune, aunque los pensamientos que tengo son dispersos y nebulosos. Solo preguntas."

"Me pregunto si incluso tuve la oportunidad de amar a Iwanako, y toda esta situación con ella aún me remuerde, una nota amarga en el fondo de mi mente."

"Me gusta mucho más Shizune. Sin embargo se siente como si la estuviera persiguiendo, incluso ahora. No me molesta la persecución, pero quiero cerrar esa distancia entre nosotros."

"La carta de Iwanako es responsable, pero también me he sentido así por un tiempo. Me he acercado más, pero no es suficiente. Quiero intentarlo de nuevo, ahora mismo."

hide kenji
with charaexit

"Le digo a Kenji que se salga para poder cambiarme, y luego me dirijo al salón del consejo estudiantil."

scene bg school_courtyard
with locationskip

"El campus está casi desierto hoy, lo cual es una lástima, porque está muy agradable afuera."

scene bg school_hallway3
with locationskip

play sound sfx_doorknock2

"Nadie responde cuando golpeo. Intento entrar de todos modos, pero está cerrado. Cuando retiro mi mano de la manilla, está cubierta de polvo. Parece que nadie ha estado aquí desde que nos fuimos."

"Como ya estoy aquí afuera y vestido, bien podría ir a buscar algo para comer en el pueblo. Pero mi billetera se quedó en mi habitación."

scene ev misha_sad:
    truecenter
    subpixel True zoom 1.05
    easein 10.0 zoom 1.0
with locationskip

"En el camino de regreso allí, me encuentro con Misha sentada detrás del edificio principal."

"Sus ojos están cerrados del sueño, y se ve muy tranquila. Siempre ha sido difícil imaginarla sin moverse constantemente de un lugar a otro o saltando impacientemente sobre la punta de sus pies."

"Mi primer instinto es llamarla y preguntarle si ha visto a Shizune, o si quiere ir al pueblo conmigo, pero ahora que la he visto no tengo ganas de molestarla. La dejo sola."

scene black
with dissolve

$ suppress_window_after_timeskip = True

label es_S25:

window hide None

scene bg school_council_bw
with locationchange

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_pearly

nvl clear
nvl show dissolve

n "\n\n\nDurante los primeros días desde que regresé, casi olvidé que estaba en el consejo estudiantil. Logré enterarme por doquier que por lo general el consejo estudiantil se inunda de trabajo cerca del final de las vacaciones, pero no tenía que ser el caso."

n "Las pocas veces que lograba encontrarme con Shizune o Misha, ellas estaban con demasiada prisa como para yo tener la oportunidad de preguntar si necesitaban ayuda. En los momentos que no lo estaban, solo podía hablar con Misha."

n "\nShizune diría algo acerca de que había trabajo, pero que era tan poco que involucrarnos a Misha o a mí simplemente nos aburriría."

n "\n\nDespués de un tiempo, la idea de tener algo de tiempo libre nuevamente ha comenzado a crecer en mí, aunque todavía había periodos en los que sentía que tenía demasiado."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

scene bg school_council
show shizu basic_normal2 at center
with locationchange

window show

"Pero justo cuando me estaba acostumbrando a eso, las cosas cambiaron de nuevo. Ahora me encuentro de vuelta en el salón del consejo estudiantil, discutiendo con Shizune sobre cuáles cajas de pañuelos de papel son mejores urnas de votación."

hi "Te lo estoy diciendo, funcionan muy bien, siempre y cuando consigamos las que tienen forma de cubo, no las rectangulares."

hi "Misha, ¿puedes decírselo en señas? Como que tengo las manos llenas… Pensándolo mejor, olvídalo."

"Ella está ocupada cortando papeletas, así que si fuera a hacer un movimiento errado, probablemente lanzaría esas tijeras hacia la cabeza de alguien."

"Dejo caer la caja de pinturas para carteles que estoy cargando en mi mesita del salón del consejo estudiantil, y toso cuando una ola de polvo me golpea en el rostro. Realmente ha pasado mucho tiempo."

show shizu behind_blank
with charachange

ssh "¿Creen que deberíamos cambiar el tamaño de las papeletas?"

show bg school_council at bgright
show shizu behind_blank at tworight
with charamove

show mishashort sign_confused at twoleft
with charaenter

mi "¿Qué~? Pero Shicchan, ya he cortado muchas de ellas…"

show shizu basic_normal
with charachange

ssh "Podemos hacerlas más pequeñas. Será más eficiente. Solo tenemos que reducir el tamaño de la letra. De esa manera, más papeletas cabrán en una sola caja. Entonces, solo necesitaremos la mitad de la cantidad de papel."

show shizu behind_smile
with charachange

ssh "El formato de votación puede cambiarse. Podría ser más como una elección real; entonces podríamos librarnos comprando menos cajas."

show shizu adjust_happy
with charachange

ssh "Con el dinero sobrante, podemos comprar una pizza, o quizás comida china, o un pastel, o tres tazones del nuevo tazón de ramen que quiero probar."

"Shizune frota con emoción un dedo a lo largo del marco de sus anteojos mientras reflexiona en más maneras de reducir los gastos de nuestro presupuesto hasta en medio yen."

"Ya que creo que ella es la única que sabe siquiera cuánto es nuestro presupuesto, tengo miedo de preguntar qué tan pequeño es para que tenga que hacer esto."

hi "¿Qué hay de todas las papeletas que Misha ya cortó?"

show shizu basic_happy
with charachange

ssh "No se preocupen, no se preocupen. Puedo convertirlas en blocs de notas y venderlos en la tienda de la escuela."

show mishashort perky_confused
with charachange

mi "Shicchan, pero no se ven muy bonitas~…"

show shizu adjust_frown
with charachange

"Shizune parece estar en desacuerdo. Ahora están discutiendo, pero parece que consiste en nada más que decirse entre sí en señas “Que sí” y “Que no” hasta que están tan cansadas que solo se turnan señalándose entre sí imperiosamente."

"Es extraño, en parte porque se ve algo ridículo, pero también porque nunca las he visto estar en desacuerdo."

"Por otra parte, las dos se han visto muy estresadas en estos últimos días."

"Shizune ha estado cada vez más absorta en la idea de las elecciones del consejo estudiantil, aunque están a meses de distancia."

"Imagino que así es como actúan los políticos cuando se dan cuenta de que un cambio de régimen es inminente y que su era terminó."

"Estoy teniendo problemas en tomarme completamente en serio los asuntos del consejo estudiantil, incluso ahora, mientras practico mi caligrafía en letreros que no se usarán en semanas, pero puedo entender por qué Shizune sí se los toma en serio."

"Después de todo, ella ha sido presidenta del consejo estudiantil durante tres años. Según su papá, ella ha querido el trabajo por incluso más tiempo. Supongo que tres años es una carrera muy corta como para que ella la deje sintiéndose satisfecha."

hi "¿El último consejo estudiantil pasó por tantas dificultades para hacer una transición sin problemas para ti?"

show shizu behind_frustrated
with charachange

"Shizune hace una cara de disgusto que me dice que no fueron de mucha ayuda en absoluto."

hi "Entonces supongo que estás haciendo todo esto para poner un buen ejemplo."

show shizu basic_frown
with charachange

shi "…"

show mishashort hips_frown
with charachange

mi "¡Eso solo entra en juego si ellos aprenden algo de eso, Hicchan~! ¡Si no, estaré hiper-furiosa~! Si resultan ser poco fiables, sin duda voy a ser dura con ellos~."

"No suena muy amenazante cuando Misha lo dice."

hi "Así que, ¿ya los conociste?"

show shizu adjust_smug
with charachange

shi "…"

show mishashort hips_grin
with charachange

mi "Ajaja~. ¡Hicchan, todavía no hay candidatos~!"

hi "¿Qué? ¿Ninguno?"

show shizu behind_smile
show mishashort hips_smile
with charachange

ssh "Ni siquiera para presidente del consejo estudiantil. Es por eso que estoy intentando despertar el interés por el puesto. ¿Qué piensas?"

"Ella levanta con orgullo un cartel en el que ha estado trabajando por su cuenta. Se ve muy, eh, militar."


hi "Entonces, puede que te estés tomando esto demasiado en serio."

show shizu adjust_frown
with charachange

"Shizune frunce el ceño y juega con sus anteojos, ofendida."

ssh "¿Eso es raro?"

hi "Sí."

show shizu behind_smile
with charachange

"Ella se ve extrañamente feliz de que esté en desacuerdo con ella, y creo que si no estuviera genuinamente concentrada en lo que estaba haciendo, intentaría discutir conmigo solo porque sería interesante para ella."

show shizu basic_normal
with charachange

ssh "¿Qué hay de raro en eso?"

show shizu adjust_smug
with charachange

"Parece que lo hará después de todo. Pero entonces, Shizune hace un gesto con la mano despectivamente, como si tratara de atrapar las palabras en el aire para borrarlas. En vez de eso, ella las catapulta a insultar a sus futuros sucesores."

hi "Bueno, una cosa que es rara es que en mi vieja escuela las elecciones ocurrirían en casi seis meses, ya que, tú sabes, nos graduaremos en marzo. Es muy raro pensar en ellas tan pronto."

show shizu behind_blank
with charachange

ssh "Es un poco diferente aquí."

show shizu adjust_frown
with charachange

shi "…"

show mishashort sign_smile
with charachange

mi "¡Hicchan, estaré desanimada si no tenemos ningún reemplazo cuando me tenga que ir~! Shicchan dice."

show mishashort hips_grin
with charachange

mi "¡Pero~!, no es que la escuela deje de funcionar sin un consejo estudiantil. ¡Pero será más difícil para ellos repartir formularios~!"

show mishashort cross_laugh
with charachange

mi "Jajaja~."

show shizu basic_normal2
show mishashort cross_smile
with charachange

"Sin embargo, Shizune no se está riendo. La broma de Misha hace que se estremezca, como si le picaran. Aunque Misha no quiso que resultara así, su ocurrencia tuvo una crueldad insensible al final."

show shizu adjust_frown
with charachange


ssh "Hmf. Estoy intentando hacer que más gente se lance, pero todos son tan perezosos. Creen que pueden estar tranquilos solo porque todavía no hay una fecha límite. Holgazanes, no aprovechan la ventaja de jugar primero."

show shizu cross_angry
with charachange

ssh "¿“Aún” faltan seis meses? ¡Si ellos no hacen su jugada ahora, no merecen un voto!"

show mishashort sign_smile
with charachange

mi "¿Realmente creen que es un trabajo tan fácil que pueden hacer todo en el último minuto y simplemente vagar en su labor~? ¡Insultante~! ¡En serio~, en serio~!"

show mishashort hips_frown
with charachange

mi "¡Se los van a comer vivos una vez tengan que sentarse en este pequeño escritorio y vean cuánto trabajo tienen que hacer~!"

show shizu behind_frustrated
with charachange

ssh "Si esta fuera una elección real, estarían en serios problemas. El otro día estaba leyendo sobre las leyes de campaña japonesas. Solamente las malas, por alguna razón."

hi "Por alguna razón."

"Por un segundo, Shizune estaba “hablando” como su padre, y estaba saliendo de la boca de Misha. Espeluznante."

hi "Bueno, en primer lugar, shogun de las sombras, no puedes insistir en eso. Ellos serán elegidos."

hi "Segundo, es solo una elección escolar. No es que se estén lanzando como candidatos al consejo municipal, o a la Dieta. No creo que se apliquen las leyes de campaña japonesas."

"Tercero, aunque no quiero decirlo, estoy nervioso de que Shizune esté tan entusiasmada por esto, hablando de elecciones y votos."

"Según su papá, ella misma ni siquiera fue elegida. Ahora que lo pienso, tampoco puedo recordar si alguna vez Shizune haya dicho que fue elegida."

"Entonces, ¿ella obtuvo esta posición al ser reclutada por el consejo estudiantil, y dejando que se viniera abajo hasta que ella fue la única que quedó? De alguna manera, nunca lo había considerado."

"No sé qué pensar sobre eso, pero no me sorprendería. Solo somos tres personas ahora."

"Si las circunstancias detrás de su ascenso a presidenta del consejo estudiantil fueran así de tristes, me pregunto si habrá un voto en absoluto. El interés podría ser así de bajo; o inexistente, en realidad. Entonces toda su energía se iría hacia la nada."

"Hago un signo de exclamación al final del cartel en el que estoy trabajando. Es un poco simple, así que pienso que añadirle uno está bien. De hecho, aún puede que sea muy simple. Hago el signo el doble de grande."

hi "Aún digo que necesitas bajarle el ritmo. Si estas cosas no van a ser relevantes durante meses, quizás estás trabajando demasiado duro en ello. Eso es lo que pienso. Te estás preocupando demasiado."

"No sé cómo decir en señas la palabra “relevantes”. Lo intento, y solo termino trazando una línea larga de pintura donde no quería. No hay manera de que pueda arreglar eso."

hi "Misha, ¿puedes preguntarle eso?"

show mishashort sign_smile
with charachange

show shizu adjust_happy
with charachange

"Shizune se ríe en silencio, apretando sus dientes para que no salga ningún sonido."

show shizu behind_blank
with charachange

ssh "Porque hay mucho de qué preocuparnos."

hi "¿Como qué?"

show shizu basic_normal
with charachange

ssh "Como… por lo general las cajas terminan viéndose muy bonitas, así que la gente se las lleva. Hay que planear para eso."

show mishashort hips_grin
with charachange

mi "¡Guajaja~! ¡Deberíamos hacer que se vean graciosas esta vez, entonces, así nadie se las llevará! ¿Qué tal eso, Shicchan~?"

hi "Podemos dibujar algunas caras raras en ellas. O podemos poner una pequeña foto de Shizune en cada una de ellas que diga “Robar está mal”."

show shizu behind_frown
with charachange

ssh "No. ¡No es gracioso! Ese no es el único problema. Está la participación electoral, por supuesto…"

show shizu basic_normal2
with charachange

ssh "… Y el peor de los casos sería que no haya ningún candidato."

"Aunque parece que lo dijera en broma, por la manera en que sonríe mientras lo dice en señas, así no es como sale."

show mishashort cross_laugh
with charachange

"Hasta Misha entiende que la posibilidad es muy real, y aunque intenta salvar el humor al puntuar la declaración de Shizune con una risa, no funciona."

show shizu behind_frustrated
with charachange

shi "…"

show shizu basic_angry
with charachange

ssh "¿Qué les pasa a ustedes dos?"

show shizu adjust_frown
with charachange

ssh "Solo estaba bromeando. En realidad hay algo de interés este año. Si no lo hubiera, ¿estaría haciendo todo este trabajo? No soy estúpida."

show shizu behind_smile
with charachange

ssh "Cuando las elecciones terminen, compraré la cena para todos. Ya lo estoy planeando."

hi "¿Incluso al nuevo consejo estudiantil?"

show shizu adjust_smug
with charachange

ssh "No, ellos pueden comprar su propia cena de celebración. Solo será para el actual consejo estudiantil. Estaré feliz una vez haya terminado de hacer estos trabajos ingratos todo el tiempo."

show mishashort hips_grin
with charachange

mi "¿Una cena solo para nosotros~? ¡Viva~! ¡Es como una pequeña fiesta, Shicchan~!"

stop music fadeout 3.0

"Aunque su alegría obviamente es forzada, no digo nada. Por el resto del periodo, el cual afortunadamente no es muy largo, trabajamos en silencio."

scene bg school_hallway3
with shorttimeskip

play music music_daily fadein 0.5

"Después de clases, encuentro cerrado el salón del consejo estudiantil. Es extraño, porque Shizune estaba tan ocupada antes, que esperaría que continuara trabajando después de la escuela. Eso sería lo que normalmente haría."

"Tal vez ella escuchó mi sugerencia y decidió tomar un descanso. Espero que sea así de simple."

scene bg school_courtyard_ss
with locationskip

"Sintiéndome un poco intranquilo, tomo una breve caminata por la escuela."

"Es solo semiinconsciente; no puedo recordar cuándo comencé a mover los pies, pero ya he cubierto lo suficiente del campus como para comenzar a sentirme cansado. No es que ahora eso signifique algo."

"Solo una pequeña caminata por el campus de la escuela, y ya estoy sin aliento. Realmente patético."

scene bg school_hallway3
with locationskip

"Antes de que lo sepa, estoy nuevamente enfrente de la oficina del consejo estudiantil. Esta vez, también hay alguien más."

show mishashort hips_smile at center
with charaenter

mi "¡Hola, Hicchan~!"

hi "Está cerrada."

"Al ver una lata de limonada en su mano, instintivamente comienzo a buscar una máquina expendedora cercana. Tengo mucha sed."

show mishashort sign_smile
with charachange

mi "¡Lo sé, Hicchan~! ¡Shicchan está en alguna otra parte, supongo~!"

hi "Qué raro."

show mishashort hips_grin
with charachange

mi "Ajajaja~. No estamos pegadas, Hicchan~."

"Misha toma un trago largo de su limonada, al final volteándola y vertiendo el resto en su boca. Siento que se está burlando de mí."

show mishashort perky_smile
with charachange

mi "¿Quieres una, Hicchan~?"

hi "No, está bien. No puedo tomar la bebida de alguien más, es de mala educación. Además, te estás burlando de mí, ¿no es así? Acabé de ver que te tragaste todo eso."

show mishashort sign_smile
with charachange

mi "¡Tengo otra en mi mochila~! Estaba preparada, ¿ves~, ves~? ¡Soy como Shicchan~!"

hi "Ella está demasiado preparada. Es bueno que algo de eso se te pegue, de todos modos. Después de qué, ¿dos años?"

show mishashort cross_laugh
with charachange

mi "¡Guajaja~!"

"La manera como ella me mira mientras bebo es un poco desconcertante, pero estoy muy agradecido de que se preocupe mucho por ello."

hi "Shizune y tú siempre terminan invitándome a algo. Está comenzando a avergonzarme."

show mishashort hips_smile
with charachange

mi "¿En serio~, Hicchan? Ajaja~. Entonces, cómprame un almuerzo algún día, ¿bueno~? ¡Entonces~!, estaremos a mano."

hi "Bueno, es curioso que digas eso. Iba a preguntarte si querías comer en el pueblo…"

show mishashort hips_grin
with charachange

mi "¡Sí~ sí~! ¡Hoy tengo mucha hambre, Hicchan! ¡Gracias!"

show mishashort invis at tworight
with dissolvecharamove

stop music fadeout 3.0

"… Ayer. Iba a preguntarle ayer. Misha me corta antes de que pueda terminar la frase, y no puedo encontrar una apertura para corregirla mientras corre con entusiasmo alrededor de mí, riendo, agitando sus brazos a sus lados con emoción."

scene bg suburb_roadcenter_ss
with locationskip

play music music_dreamy fadein 2.0

"Ya tengo mi billetera conmigo, así que comienzo a caminar hacia el pueblo con Misha siguiéndome, jugando ociosamente con sus manos y preguntándose en voz alta adónde deberíamos ir a comer. Al menos, eso creo. Ella me podría estar preguntando."

hi "¿Tienes algún lugar específico a donde quieras ir?"

show mishashort hips_smile_ss at center
with charaenter

mi "Hmmm~. Quiero ir a la casa de té, allí tienen un parfait muy grande."

hi "Te vi comer un parfait allí la última vez, se veía muy grande."

show mishashort hips_grin_ss
with charachange

mi "¡No no no~! ¡Este es muy, muy~ grande! ¡También es muy caro~!"

hi "¿Muy, muy~ caro?"

show mishashort cross_laugh_ss
with charachange

mi "¡Jajaja~! Un poco~…"

hi "Vaya. Bueno, Shizune y tú pagaron mi comida un montón de veces, así que está bien."

show mishashort perky_confused_ss
with charachange

mi "Hicchan, no creo que yo haya hecho eso alguna vez~. ¿Estás seguro de que no fue solo Shicchan?"

hi "¿En serio estás discutiendo en contra de una comida gratis? No te preocupes por eso."

scene bg suburb_shanghaiint
with locationskip

"Vamos al Shanghái, y somos recibidos por una mesera quien sorprendentemente no es Yuuko."

"Misha está muy ansiosa de comer ese parfait, porque grita su orden tan pronto entra por la puerta. Cuando llega, puedo ver que es muy grande y de apariencia muy costosa."

show mishashort perky_confused_close at center
with charaenter

mi "¿No vas a pedir nada, Hicchan~? Si tienes hambre, podemos compartir."

hi "No. No me gustan los parfaits. No me gusta el pralín."


show mishashort sign_smile_close
with charachange

mi "¡Puedes quitarlo~!"

hi "No puedes simplemente quitar el pralín; no seas tonta."

show mishashort perky_smile_close
with charachange

"Incluso si pudiera, Misha está mezclando su comida al punto donde ya no es posible. También se ve algo asqueroso."

"Me pregunto si tantos sabores pueden mezclarse bien. ¿En serio ella puede saborear algo en esa mezcla viscosa? De todos modos, ella está actuando como si fuera delicioso."

show mishashort hips_grin_close
with charachange

mi "Mm~. Los parfaits son lo mejor~, tengo dientes sensibles, así que el helado no es una opción~. Pero el pastel es muy suave, y si hay mucho glaseado, me aburro. El parfait es interesante."

show mishashort perky_smile_close
with charachange

mi "¿Cuántos cafés aquí tienen parfaits~? Creo que, ¡diez! Los he probado todos, me gusta más este. ¡Tiene un poquito de flan~!"

hi "Suenas como si fueras una especie de experta en postres."

show mishashort hips_smile_close
with charachange

mi "¡No solo postres~! Quiero comer toda clase de cosas deliciosas~."

show mishashort hips_grin_close
with charachange

mi "¡Algún día, tendré suficiente dinero para comprar un filete de dos kilos de carne Matsusaka~!"

hi "Son como más de cien mil yenes… Entonces supongo que este tipo de comida decadente es como tu pasatiempo, ¿eh?"

"Un pasatiempo no es algo que debería tomar meses para conocerlo de alguien. He sido muy grosero, en retrospectiva. También, ese es un pasatiempo costoso."

show mishashort perky_confused_close
with charachange

mi "¡Eso supongo~! ¿… Decadente~?"

hi "Sí."

show mishashort hips_grin_close
with charachange

"Misha se ríe, levantando la mano a la cara. Parece que algo de helado se metió por accidente en su nariz. Ella no lo nota. Yo no puedo dejar de notarlo. Desearía que se lo limpiara. Estoy a punto de decirle sobre eso, pero ella de repente dice,"

show mishashort perky_confused_close
with charachange

mi "No sé qué significa eso."

hi "Oh. Supongo que es una mala palabra, de todos modos. Tiene implicaciones. Epicúreo es mejor. Significa, alguien que disfruta comer buena comida. Pero ese es el adjetivo. Así que, mundana es la palabra para eso."

show mishashort cross_laugh_close
with charachange

mi "¡Guajaja~!"

show mishashort cross_grin_close
with charachange

mi "Hicchan, eres muy parlanchín."

hi "Lo siento."

show mishashort perky_smile_close
with charachange

mi "Jajaja~. Creo que eso es lo que le gusta a Shicchan de ti."

hi "¿Que soy parlanchín? Entonces necesito comprar algunos diccionarios de sinónimos."

show mishashort hips_grin_close
with charachange



mi "¡Guajaja~! ¡No, no de esa manera, Hicchan~!"

"Decido ordenar algo de café después de todo, pero toma tiempo hacer que la mesera lo note, y pienso realmente que esperar mi café tomará casi la misma cantidad de tiempo."


"La tienda de té se está llenando. No es una sorpresa, ya que hemos estado aquí casi por una hora mientras ella estaba degustando ese postre."

"Ordeno mi café para irnos, pero Misha ordena uno también, así que parece que vamos a estar aquí más tiempo del que pensé."

hi "Realmente desearía que fuera tan fácil. Es difícil hablar con ella últimamente."

show mishashort sign_smile_close
with charachange

mi "¡Shicchan ha estado ocupada debido a las elecciones~!"

hi "Sé que no podemos divertirnos todo el tiempo. Es solo que hay mucho que quiero decirle, creo. Pero siempre lo arruino cuando llega el momento. Y ahora ni siquiera tengo el tiempo. Debido a las elecciones."

hi "Pero no son por un tiempo."

show mishashort hips_frown_close
with charachange

mi "Hicchan, ¿crees que Shicchan te está evitando?"

"Misha parece enojada. Eso es de esperarse, pero no siento que ese sea el caso en absoluto."

hi "No."

show mishashort perky_sad_close
with charachange

mi "De veras~…"

"La forma distraída como lo dice me hace pensar que Misha está decepcionada con mi respuesta. En ese caso, podría ser como se siente."

"Estoy intranquilo por hacerle una pregunta como esta, pero confío en que Misha la responderá honestamente. De lo contrario, ni siquiera lo soñaría."

hi "¿Tú sí?"

show mishashort hips_smile_close
with charachange

mi "¡No, por supuesto que no, Hicchan~! ¡Pero~!… A veces es frustrante~. Shicchan tiene tanta energía, y siempre está intentando hacer que la gente se sienta tan emocionada como ella por las cosas~."

show mishashort perky_sad_close
with charachange

mi "Pero es como si Shicchan no supiera cómo manejar las cosas cuando todos están muy emocionados. ¡O~! Creo que ella quiere asegurarse de que nada salga mal. Cuando quiero ayudar, Shicchan siempre me aparta."

mi "Es frustrante."

show mishashort hips_grin_close
with charachange

mi "¡Probablemente lo estoy pensando demasiado~! ¿Cierto~?"

"Misha toma un gran trago de su taza de café, y luego saca la lengua."

show mishashort hips_laugh_close
with charachange

mi "¡Au~! Caliente~ caliente~ caliente~… ¡pensé que ya se había enfriado~!"

hi "¿Realmente ha pasado tanto tiempo?"

"Reviso mi reloj. No ha pasado mucho tiempo en absoluto, pero al mirar afuera, el sol ya está comenzando a ponerse."

hi "No realmente. Eh, pero se oscureció muy rápido hoy, así que entendería por qué podrías pensar eso."

show mishashort perky_sad_close
with charachange

"Por mis palabras, Misha mira afuera y bosteza casi inmediatamente. Se ve con sueño. Eso es curioso, porque…"

hi "¿Estás con sueño? Estabas completamente despierta hace apenas dos segundos."

show mishashort sign_sad_close
with charachange

mi "Me siento cansada cuando se hace de noche, Hicchan~."

hi "¿Así nada más? ¿Eres un pájaro?"

show mishashort perky_smile_close
with charachange

mi "Ajajaja~."

"Levanto mi propio café y tomo un sorbo. No está para nada caliente, pero sabe muy bien. Me lo tomo tan rápido como puedo, porque ahora yo también quiero regresar a mi habitación. Misha intenta emularme, pero aún está muy caliente para ella."

"Mientras espero a que ella termine, comienzo a preguntarme qué quiso decir cuando dijo que a Shizune le gustaba algo de mí. De repente, tengo mucha curiosidad, pero sacar a relucir eso de nuevo ahora se siente como una acción innecesaria."

show mishashort hips_grin_close
play sound sfx_impact
with vpunch

"Intento sopesar la opción de nuevo, pero soy interrumpido por Misha al golpear su vaso de cartón vacío sobre la mesa con un fuerte ruido seco."

show mishashort cross_grin_close
with charachange

mi "¡Listo~!"

"Ella deja salir una risa corta, viéndose muy complacida consigo misma. Casi como una niña pequeña."

"Me pregunto si ella también tenía ese peinado en forma de rizos cuando era pequeña. ¿O era algo más parecido a su aspecto actual? Tendría más sentido."

hi "Supongo que deberíamos regresar entonces. No puedo ver a la mesera. Intenta no quedarte dormida mientras pago el sundae, ¿bueno?"

show mishashort sign_smile_close
with charachange

mi "No es un sundae; es un parfait, Hicchan."

show mishashort cross_laugh_close
with charachange

mi "Guajaja~."

hi "Tienes helado en tu nariz."

stop music fadeout 2.0

scene black
with dissolve

label es_S26:

scene bg school_scienceroom at right
with locationchange

play sound sfx_paper
play music music_normal fadein 3.0

"La tarde siguiente en clase, estoy haciendo dos problemas en una hoja de ejercicios de lógica matemática cuando una hoja doblada de papel me golpea en la cabeza."

"Estoy seguro de saber de quién es, pero rápidamente miro alrededor del salón de clase de todos modos, por si acaso."

show shizu invis at left
with None

show bg school_scienceroom at left
show shizu behind_blank at center
with dissolvecharamove

"Nadie en este salón de clases es bueno actuando casual. Puedo notar que todos vieron quién me la lanzó, y al ver a la misma culpable, fue obviamente Shizune. Ella ni siquiera está tratando de ser tímida al respecto."

"El campo es tan diferente. En mi vieja escuela, ahora mismo no tendría idea de quién fue."

"Al abrir la nota, dice:"

window hide

$ written_note("¡Misha está ausente! ¡Ayúdame hoy después de clases!")

window show

hi "No entiendo qué pasa con esta nota, ¿por qué no puedes usar lenguaje de señas?"

"Una gran parte de cómo aprendí lenguaje de señas fue copiando el estilo de Misha de hacer señas mientras habla, así que termino espetando la frase en voz alta mientras la digo en señas a Shizune. Una risa suave ronda por el salón. Qué incómodo."

his "Ayudaré si no tengo que hacer mucho."

show shizu basic_angry
with charachange

ssh "Eso es tonto, obviamente si Misha está ausente tienes que ayudar tanto como dos personas."

"No sé si eso realmente significa algo. Después de todo, Misha estaba quejándose ayer principalmente de cómo Shizune no dejaba que la ayudara. Tampoco hago mucho tal cual."

"Después de fingir pensarlo por un momento, le escribo una nota de vuelta diciéndole que lo haré. En realidad estoy feliz de que me lo pidiera, porque he estado queriendo hablarle por un tiempo."

"Es una buena oportunidad, pero siento que al menos debería hacerlo parecer como si estuviera poniendo algo de resistencia a la idea."

hide shizu
with charaexit

"Regreso a mi hoja de ejercicios e inmediatamente quedo atrapado en el tercer problema. Después de intentar resolverlo, le lanzo mi propia nota de manera casual a Shizune. Dice:"

window hide

$ written_note("¿Por qué Misha está ausente? ¿Y cuál es la respuesta a la pregunta 3?")

show shizu behind_blank at center
with charaenter

window show

ssh "Ella me dijo que estaba enferma y que le dolía el estómago. A Misha le dan muchos dolores de estómago, pero desearía que hubiera elegido un mejor momento en esta semana."

show shizu basic_normal2
with charachange

ssh "Usa lenguaje de señas."

"Creería que ella tiene dolor de estómago por la manera en que se tragó un parfait más grande que su cabeza el otro día."

"Pero si los tiene muy a menudo, o es una coincidencia o ella tiene la costumbre de comer cosas que pueden dejarla con un dolor debilitante."

"Noto que el maestro nos mira fijamente con desaprobación. No lo culpo. Estamos “hablando” en clase, y en lenguaje de señas, de una manera muy visible y distrayente."

"Intento carraspear para retirarme de nuestra conversación, pero Shizune no capta el mensaje."

"Bueno, obviamente. Sin embargo, antes de intentar hacerle llegar el mensaje de nuevo con mis manos, puedo ver que Shizune nota lo que pasa, solo que no le importa."

show shizu adjust_smug
with charachange

ssh "¿Todavía quieres saber la respuesta a la pregunta 3? Te la diré, pero tienes que darme la respuesta a la pregunta 25."

his "Oye, estaba pensando en cómo un maestro que no sepa lenguaje de señas podría pensar que estamos abusando de él y usándolo para hacer trampa, si fuera a suponer lo peor. ¡No puedo creer que realmente estés haciendo eso! Y, no he llegado a la 25."

show shizu behind_frown
with charachange

ssh "Tú querías saber cuál era la respuesta a la 3; tú preguntaste primero. Hipócrita."

his "Eres la presidenta del consejo estudiantil, no puedes hacer trampa."


"No tengo tiempo para esto, y creo que estoy probando la paciencia del maestro al punto de quiebre. Me gustaría seguir criticándola mientras trabajo en los problemas de matemáticas enfrente de mí, pero necesitaría por lo menos dos manos más."

show shizu basic_normal
with charachange


"Shizune es un poco más creativa, y sortea esta limitación usando secuencias largas y semi-rotas de palabras más simples. Tomo un par de notas mentales en medio de estar mareado por un par de ecuaciones particularmente largas."

show shizu adjust_smug
with charachange

play sound sfx_impact2
with vpunch

"Justo antes de que suene la campana, ella tapa su bolígrafo y lo golpea triunfante sobre su banco con un chasquido ensordecedor que hace saltar a todo el salón, rápidamente olvidado porque todos preferirían ir a almorzar que preguntar su origen."

stop music fadeout 6.0

show shizu basic_normal_close at twoleft
with characlose

"Después de un par de estiramientos breves, ella se levanta y merodea sobre mi hombro izquierdo."

show shizu behind_frown_close
with charachange

ssh "¿Todavía no has acabado? Iba a preguntarte si querías que entregara la tuya también, mientras me levantaba."


his "Alguien me distrajo. Tuve que rogarle al maestro que me diera nueve minutos desde ahora hasta que termine de revisarlos para terminarlo. Por cierto, no es fácil resolver esto con una sola mano mientras tengo una conversación."

"Él no estaba contento con la solicitud, queriendo irse de aquí tanto como yo."

"Ya que solo me falta un problema para terminarlo, parece que Shizune en realidad no me cree. En el instante en que lo entrego, me encuentro siendo arrastrado al salón del consejo estudiantil."

scene bg school_council
with locationskip

play music music_happiness fadein 2.0

"Está misteriosa e irritantemente limpio. No puedo encontrar las cosas en las que estaba trabajando ayer."

his "¿Dónde está todo?"

show shizu behind_blank at center
with charaenter

ssh "Hice algo de limpieza."

his "Eso no me dice nada. Ves, es como si olvidaras dónde pusiste las cosas que guardaste. Ah bueno, si no puedo encontrarlas, supongo que me iré a casa."

show shizu basic_normal2
with charachange

ssh "Están en el cajón justo allí."

"Shizune se enfada cuando saco los carteles en los que estaba trabajando, y luego los revuelvo un poco, ya que ella los apiló por color. No es que me esté burlando de ella; solo tengo mi propio sistema, aunque dudo que ella me creyera si se lo dijera."

his "Me gusta cuando las cosas están un poco desordenadas. Es más natural. Y ahorra tiempo. Está bien donde las dejé, y no tengo que estar buscando en los estantes solo para encontrar en lo que estaba trabajando ayer."

show shizu adjust_frown
with charachange

ssh "Perezoso."

his "Eso no es cierto. No soy perezoso, siempre vas demasiado lejos."

"Rápidamente miro su escritorio. Un bloc de notas colocado con cuidado en una esquina, detrás de él un pequeño calendario de escritorio con cada caja llena de notas en una caligrafía clara, pero microscópica."

"A la derecha, tres cajas de bolígrafos, de colores azul, negro y rojo."

his "Mira, hasta pones los bolígrafos de vuelta en su caja original al final de cada día, todos clasificados por color y todo eso. No creo que ni siquiera eso pueda llamarse ser un obsesivo del orden."

show shizu behind_frown
with charachange

ssh "¿Tú qué haces con ellos, tirarlos en una taza sobre tu escritorio?"

his "Oye, creo que eso es ser lo suficientemente organizado."

show shizu basic_frown
with charachange

ssh "Eres tan desordenado, ni siquiera puedes peinarte de manera adecuada."

his "Eso duele…"

"No es que no lo intente; es que no se queda plano. Recojo una caja de bolígrafos y rápidamente la abro para ver si también los pone de manera que todos estén mirando a la misma dirección. Ella entiende lo que estoy pensando, y no se ve muy entretenida."

play sound sfx_dropstuff

"Resulta que la caja no estaba bien cerrada en el fondo, y tan pronto la recojo, inmediatamente salen de ella como una catarata."

his "Es mi culpa. Yo los recogeré, no te preocupes."

stop music fadeout 4.0
play sound sfx_impact

show shizu adjust_blush_close
with vpunch

"Me agacho a recoger los bolígrafos, olvidando que con su atención enfocada en ellos, ella no pudo haberme visto haciéndole señas. La cabeza de Shizune me golpea en el pecho; no muy fuerte, pero me desequilibra lo suficiente como para hacerme caer."

show shizu adjust_blush
with charadistant

"Me río de ello, y espero que ella haga lo mismo. Pero en vez de eso, cuando ella se pone tensa y se aleja de mí, un sentimiento de terror comienza a apoderarse de mí."

"Es una reacción rara. Comienzo a pensar en la razón por la que ella tendría una reacción tan extraña. Es muy obvia: se chocó de cabeza con alguien con una condición cardiaca."


label es_S26a:

"Shizune sabría que tengo una, al haber visto las filas y filas de píldoras alineadas en el borde de mi tocador. O por lo menos, ella sabría que tengo algo lo bastante severo que requiera tantos medicamentos, pero que no es visible a simple vista."


label es_S26b:

"Shizune sabría que tengo una, quizás gracias a los registros a los que tiene acceso por sus deberes en el consejo estudiantil. O por lo menos, ella sabría que tengo algo lo bastante severo como para que necesite monitoreo."


label es_S26c:

"Así que ella me está tratando como si estuviera hecho de cristal. Para ella, es la manera natural de reaccionar. No he olvidado cómo se asustó cuando Emi se chocó conmigo. ¿Por qué habría de ser diferente para ella?"

show shizu basic_normal
with charachange

"Estoy seguro de que ella está recordando eso, ahora mismo. Puedo verlo en su rostro. Se ve enojada consigo misma."

"Esta sería una buena oportunidad para recordar aquella ocasión. Aunque no quiero volver a sacar ese tema de nuevo, sería una buena idea hacerlo. Limpiaría el aire."

"Aun así, tengo miedo, y termino sin decir nada. En parte porque mientras me imagino tener que llamar su atención del piso, y luego decirle en señas el tipo de lisiado que soy con un gesto a la vez, la idea empieza a parecer cada vez más deprimente."

hide shizu
with charaexit

"Al tomar asiento, decido simplemente intentar terminar estos carteles para alejar mi mente de eso. Hay algunos que no recuerdo haber hecho. Por el texto de esquina a esquina y la caligrafía ultra-ordenada, puedo notar que Shizune debió hacer estos."

"Eso significa que el resto debió haber sido hecho por Misha. Esos son mucho más visuales, con pequeños y bonitos dibujos estilizados de nosotros en ellos."

"No sé cómo sentirme al ser usado como personaje mascota, pero no estoy realmente emocionado por eso."

scene bg school_council_ss
with shorttimeskip

play music music_tranquil fadein 3.0

"Pasa algo de tiempo; lo bastante para que el sol comience a ponerse. Oigo a Shizune bajando su bolígrafo y haciendo sonar sus nudillos metódicamente, uno a la vez."

"Es tan fuerte en el silencio del salón que levanto la mirada, preguntándome si está intentando llamar mi atención."

show shizu behind_blank_ss
with charaenter

"Aunque eso no era lo que ella quería, cuando me ve mirándola, Shizune comienza a hacer señas sin perder el ritmo."

show shizu basic_normal_ss
with charachange

ssh "Vamos a tomar un descanso."

his "Estoy sorprendido de que dijeras eso."

show shizu adjust_happy_ss
with charachange

ssh "Está bien. Ya casi acabo, de todos modos. Y tengo hambre. ¿Tú no?"

his "Un poco."

show shizu basic_normal2_ss
with charachange

ssh "Yo tengo mucha hambre."

his "Podríamos pedir algo."

show shizu behind_smile_ss
with charachange

ssh "Estaba pensando en ti. Yo ya tengo algo para comer."

his "¿Dónde?"

show shizu adjust_smug_ss
with charachange

"Ella saca un bollo de canela de debajo de su escritorio, levantándolo lentamente a la altura de su cabeza, como un mago levitando una roca."

show shizu behind_smile_ss
with charachange

ssh "¡Pero!"

show shizu basic_sparkle_ss
with charachange

ssh "Solo hay uno. No es suficiente para los dos."

"Ah, qué dramática. Puedo saber lo que esto significa. Una sensación de déjà vu me invade brevemente."

his "Podríamos dividirlo y ya."

show shizu adjust_frown_ss
with charachange

ssh "Eso. No. Es. Divertido. Muy aburrido. Juguemos shogi por él."

"Ella ya tiene el tablero listo. Ese escritorio debe tener de todo en él."

his "¿Ajedrez no?"

show shizu behind_smile_ss
with charachange

ssh "El ajedrez tiene promociones aburridas, esto es mejor."

his "No estoy seguro de eso. Bueno, en realidad soy bastante decente en el shogi, así que esto está bien."

show shizu basic_happy_ss
with charachange

ssh "¿En serio? Muy bien, entonces podemos hacerlo un poco más interesante. Cada jugada tiene que completarse en treinta segundos. Tú también puedes añadir una regla."

his "No, gracias, cualquier cosa que podría añadir solo me perjudicaría más de lo que me ayudaría. Un límite de tiempo de treinta segundos ya es muy difícil para mí."

his "Estás haciendo que me arrepienta de pensar que estaba bien presumir un poco."

scene bg school_council_ss
show shizu basic_normal_close_ss at center
with shorttimeskip

"Después de que Shizune gana el derecho a mover primero en un rápido cara o cruz, inmediatamente comienza a jugar con el objetivo de promover todas sus piezas lo más pronto posible."

"Parece un estilo de juego muy básico, y no puedo dejar de pensar que podría ser una especie de trampa."

"Sin embargo, no lo es. La atracción de este juego para Shizune parece ser el hecho de que puede mejorar sus piezas, y robar las mías. Ella es muy buena en ello, pero la hace predecible. Me termina yendo un poco mejor de lo que esperaba."

"Pero el límite de tiempo de 30 segundos es muy doloroso. El juego termina en un empate. En este punto, creo que se supone que o vuelvas a jugar o cuentes las piezas por puntos."

"Shizune no quiere jugar de nuevo en aras del tiempo, pero ganar por puntos claramente no la satisface."

show shizu adjust_frown_close_ss
with charachange

stop music fadeout 4.0

"Ella se sienta allí, moviendo un general plateado de un lado al otro mientras contempla por cuál de esas dos opciones irá. Se toma tanto tiempo que creo que se ha olvidado de la apuesta."

"Al final, ella deja de juguetear con la pieza de shogi y la baja."

show shizu behind_blank_close_ss
with charachange

ssh "¿Misha está enojada conmigo?"

"Eso realmente salió de la nada."

play music music_pearly fadein 5.0

"La franqueza de Shizune es desorientadora, porque con ella, cualquier tipo de sinceridad es una muestra de total seriedad."

"No hay una sonrisa juguetona en su rostro, en vez de ella está su típica máscara estoica de concentración, lista para intentar ver si estoy a punto de decirle la verdad."

"Me molesta que ella piense que yo le diría cualquier otra cosa, pero también ahora sé que probablemente han peleado recientemente, fuera de mi vista, y me hace sentir afable saber que ambas se preocupan tanto la una por la otra."

his "No. Lo dudo muchísimo."

his "¿Sabías que ella cree que tú estás enojada con ella?"

show shizu behind_sad_close_ss
with charachange

"Shizune asiente lenta e incómodamente."

show shizu basic_normal2_close_ss
with charachange

ssh "Sí."

his "Ella fue más indirecta con la pregunta que tú. Algo sorprendente, porque pensé que tú eras a la que le gustaba jugar juegos."

show shizu behind_blank_close_ss
with charachange

ssh "No todo el tiempo."

"…"

his "¿Ustedes dos han estado peleando o algo así?"

show shizu adjust_frown_close_ss
with charachange

ssh "No."

"Ella es muy rápida en negarlo, y no está feliz con la idea. Siento como si hubiera pisado una mina."

show shizu behind_sad_close_ss
with charachange

ssh "Lo siento. En realidad, sí. Solo un poco."

show shizu behind_blank_close_ss
with charachange

ssh "Sé que ella no tiene interés en el consejo estudiantil. Ella solo se unió por mí. Aun así estoy agradecida. Estoy tan feliz de que sea mi amiga. Pero no entiendo qué le molesta esta vez."

his "¿Por qué no simplemente se lo preguntas?"

show shizu basic_normal2_close_ss
with charachange

ssh "Ella no me lo dirá. En vez de eso, tendré que averiguarlo por mi cuenta. Estaba segura de que yo era muy perceptiva, aunque no puedo oír. Eso fue tonto. Ahora lo sé mejor."

show shizu behind_sad_close_ss
with charachange

ssh "Probablemente sea algo que es mi culpa."

stop music fadeout 8.0

"Shizune no entra en detalles sobre lo que podría haber sido. Estoy seguro de que es porque ella misma no entiende completamente la situación."

"Es extraño pensar que Shizune, por lo general tan segura de todo, podría estar asustada por una pequeña discusión con una amiga. Pero entre más lo pienso, más tiene sentido."

"Ellas son mucho más cercanas entre sí que los amigos normales, y Shizune está bastante aislada de otras personas, en cierta forma. El hecho de que ella sea sorda no es poca cosa en ello."

"Pero tengo la sensación de que ella usa a Misha como mediadora entre otras personas de su propia voluntad, no solo porque eso haya sido forzado en ella. Ella puede comunicarse muy bien con su libretita. Simplemente la odia."

"Después de tanto tiempo de hablar a través de otra persona, supongo que comienzas a perder el tacto. Parece inevitable. No es una idea tan alejada pensar que ella no es tan buena con la gente."

hide shizu
with charaexit

"Regreso a trabajar, como queriendo cada vez más comerme ese bollo de canela mientras el tiempo pasa, pero cuando cuento las piezas de shogi que quedan sobre la mesa de Shizune, puedo decir de un vistazo que ella ganaría."

"También estoy muy hambriento como para concentrarme si tuviéramos que volver a jugar. Motivado por mi deseo de terminar y comer algo, pongo los toques finales en el último de los carteles."

his "Listo. Creo que estos son suficientes. Demasiados pueden ser algo malo."

play music music_shizune fadein 3.0

show shizu behind_blank_ss at center
with charaenter

ssh "Bueno."

his "¿Eso es todo? ¿Solo “bueno”?"

show shizu adjust_frown_ss
with charachange

shi "¿…?"

show shizu behind_blank_ss
with charachange

ssh "… Probablemente haré algunos yo misma, después de que termine de elegir cuál formato de votación usar."

his "Arrgghh. Demasiados carteles es malo, también. ¿No has escuchado alguna vez de la sobresaturación?"

his "Realmente pienso que te estás esforzando demasiado."

show shizu basic_normal_ss
with charachange

"Juntando sus dedos, Shizune parece que casi podría admitirlo."

show shizu behind_blank_ss
with charachange

ssh "Tal vez."

his "Eso también es lo que Misha piensa."

show shizu basic_normal2_ss
with charachange

"Observo mientras sus dedos continúan entrelazándose inquietamente y jalándose entre sí en un tira y afloja miniatura."

his "No me importa, pero hoy pregunté en un par de clases y el interés es bajo. Es como tú dijiste. Así que…"

show shizu adjust_frown_ss
with charachange

ssh "¿Eso lo vuelve malo?"

his "No. Pero… lo hace algo inútil."

show shizu basic_angry_ss
with charachange

ssh "No lo es."

"Sí, ¿pero para quién? Dudo que hasta Shizune realmente crea eso."

show shizu behind_frustrated_ss
with charachange

ssh "No estoy haciendo todo este trabajo solo para mi propio ego."

his "Eso no es lo que quiero decir."

"La primera oportunidad en días de estar solo con ella, y ya la he arruinado. Aun así, en realidad ella no se ve enojada."

"Es más como si estuviera frustrada por no poder expresarse claramente. Ya que ella es una experta en el lenguaje de señas, no pensaría que ese fuera el caso."

"Me pregunto qué ventajas le traería a ella el poder hablar, y si ella alguna vez lo ha pensado."

show shizu basic_frown_ss
with charachange

ssh "Es otro proyecto mío. Tal como los festivales. Voy a hacerlo, porque es mi trabajo. Es solo que una elección del consejo estudiantil no es tan divertida como un festival, así que a nadie le importa."

"Ella brevemente junta las puntas de sus dedos, como si fuera a decir “Pero, tal vez…”. Hay algo de verdad en ello, pero Shizune no quiere decir nada que pudiera ser reducido a algo tan simplista."

show shizu behind_frown_ss
with charachange

ssh "Pero no me importa. Quiero hacer que la gente se altere, pero no es por mí. No quiero estar involucrada en absoluto."

his "¿Qué quieres decir? Vas a todos y cada uno de los festivales."

show shizu adjust_frown_ss
with charachange

"Shizune mueve su mano fingiendo indignación."

show shizu behind_blank_ss
with charachange

ssh "Bueno… también tengo que divertirme. Pero sabes, no es lo mismo."

"Su estado de ánimo parece haber mejorado, si puede lograr gastar una broma."

show shizu basic_normal2_ss
with charachange

ssh "No quiero que nadie se proponga involucrarme. Es una molestia. No quiero esa responsabilidad."

show shizu adjust_frown_ss
with charachange

ssh "Las cosas se están volviendo muy complicadas como están ahora. Entre más intento darle bombo a las elecciones, más involucrada tengo que estar. Nadie quiere hacer su jugada aún, y no se siente como si mi tiempo haya acabado, aunque debería."

show shizu behind_frustrated_ss
with charachange

"Cruzándose de brazos y reclinándose, ella rechina sus dientes en frustración."

show shizu cross_angry_ss
with charachange

ssh "Todos son tan perezosos; es imposible hacer que hagan algo. En cualquier otra parte, las elecciones serían un evento emocionante. Es ilógico, ¿por qué todos tienen que ser tan diferentes? Si tan solo hubiera alguna manera de castigarlos…"

show shizu adjust_angry_ss
with charachange

ssh "… Como encadenar la escuela a sus bancos. Que votar sea obligatorio. Si no votas, serás azotado."

"Aterrador. Me pregunto qué tan hipócrita sería si me quedara en cama el día de la elección. Con la gripa. Y un resfriado. Y faringitis. Y un tobillo torcido."

his "Deberías ponerte en uno de estos."

his "No como castigo. No malentiendas."

"Levanto uno de los carteles de Misha."

his "Como en este. Es como una buena idea. Misha había dado con algo. Es mucho más bonito que solo texto. Pensaba que te gustaría. Tener mascotas bonitas despertaría algo de emoción."

show shizu basic_normal_ss
with charachange

ssh "Tal vez si es solo Misha."

his "¿Por qué yo no? Alguien me dijo que en esta escuela hay ligeramente más chicas que chicos… También tienes que atender esa demografía."

show shizu adjust_blush_ss
with charachange

"Shizune se ríe audiblemente esta vez. Estoy sorprendido, y cuando ve mi rostro, ella también. Su rostro se sonroja, avergonzada de haber dejado escapar un sonido. Lo cual es muy confuso, por decir lo menos."


his "¿Por qué no te pones en él?"

"Ella solo aleja mi pregunta con un gesto."

show shizu basic_angry_ss
with charachange

ssh "Es problemático."

his "¿Qué quieres decir con problemático? Todos saben que estás en el consejo estudiantil."

"Mi estómago gruñe, y me hace dar cuenta de que estoy más hambriento de lo que pensaba. Shizune usa el momento para desviar mi pregunta cambiando el tema."

show shizu behind_blank_ss
with charachange

ssh "¿Ocurre algo?"

his "No. Mi estómago gruñó."

show shizu basic_normal_ss
with charachange

ssh "Ya veo."

"Ella mira el postre olvidado sobre su escritorio y luego frunce el ceño, al verlo inadecuado para dos personas."

show shizu adjust_happy_ss
with charachange

ssh "Vamos al Shanghái, si tienes tanta hambre. Puede que esté un poco lleno a esta hora tan tarde, pero Yuuko está trabajando allí hoy. Sin duda conseguiremos una mesa."

"Hay algo preocupantemente engañoso en esa sonrisa."

his "Paso. Ya he estado allí dos veces esta semana, de aquí para allá."


show shizu basic_frown_ss
with charachange

"Shizune hace pucheros, apoyándose contra su escritorio y apretujando su postura en protesta."

his "¿Qué?"

show shizu adjust_frown_ss
with charachange

ssh "Estoy decepcionada de que dijeras que no."

his "Bueno, no puedo estar de acuerdo contigo en todo."

show shizu behind_frown_ss
with charachange

ssh "No das tu opinión muy a menudo, de todos modos. Sería más fácil para mí si fuera así, pero no muy interesante, ¿cierto? Entonces, hay algunas decisiones en las que deberías estar en desacuerdo conmigo. Tienes el deber de hacerlo."

his "¿Cómo se supone que sepa cuál es cuál?"

show shizu basic_normal_ss
with charachange

ssh "Es fácil."

his "No, no lo es. A veces es difícil para mí saber si estás bromeando o hablando en serio."

stop music fadeout 9.0

"Aunque eso parecería bastante obvio, ya que ella se comunica por completo en lenguaje de señas. Pero no diría que eso es todo lo que hay."

"Recuerdo que cuando tuve mi ataque cardiaco, Iwanako no paraba de hablar al comienzo. Al final, deseaba que se callara."

"O lo habría hecho, si no hubiera estado feliz de tener algún tipo de compañía en absoluto. Poco a poco, dejé de estar tan agradecido."

"Cuando hablábamos, se sentía como si no hubiera nada más que intercambios ritualizados de cortesía."

"Iwanako se esforzaba muchísimo en ofuscar cómo se sentía, lo cual era que yo no tenía esperanzas. Al final, su comportamiento exterior igualó a sus sentimientos interiores."

"Por esa razón, pude aceptarlo cuando un día ella dejó de aparecer. Ya no estaba sorprendido para cuando ocurrió. Aunque ella misma se consideraba una maestra en esconder sus sentimientos, yo no estaba sorprendido."

"He escuchado que juegos como el shogi y el ajedrez pueden decirte mucho sobre una persona. Desearía saber lo que Shizune pensó que decían de mí."

"Podría ser que soy un poco más como Iwanako de lo que me gustaría pensar, si solo puedo empatar con Shizune retirándome. Sugiero que deberíamos pedir algo para comer."

scene black
with dissolve



label es_S27:

scene bg school_hallway2
with locationchange

"El día siguiente, me dirijo a mi máquina expendedora habitual durante el almuerzo solo para descubrir que se le agotó mi bebida favorita. Oculta muy lejos de la mayoría de los salones de clase, entre un almacén y la biblioteca, es como si nadie supiera de ella."

"Esperaba que una máquina expendedora tan cerca de la biblioteca estuviera llena de compradores, pero por otra parte, la biblioteca está vacía gran parte del tiempo, y cualquiera que va allí solo lo hace para buscar cosas con qué rellenar un ensayo."

"Nadie se queda allí más tiempo del que es absolutamente necesario. Durante el último mes ha estado funcionando a mi favor, pero la desventaja con una máquina expendedora de la que nadie sabe es que nunca es reabastecida."

play sound sfx_can

"Conformándome con una lata de gaseosa de naranja, decido beberla aquí en vez de esperar a llegar a la cafetería, cuando la puerta de la biblioteca se abre a mi lado."

show yuuko worried_down at center
with charaenter

yu "Ah…"

show yuuko worried_up
with charachange

yu "¡Estaba buscándote!"

play music music_happiness fadein 2.0

"Yuuko parece estar actuando mucho más enérgica de lo normal hoy, aunque eso no es suficiente para evitar que vuelva a balbucear inmediatamente después."

show yuuko worried_down
with charachange

yu "D-devuelve tus libros, por favor. Quiero decir… los libros de la biblioteca. Los libros que sacaste están vencidos desde hace mucho. Algunos de ellos están en listas de espera…"

hi "Ups. Lo olvidé. Sigo sacando los nuevos, y olvido regresar los viejos."

show yuuko neurotic_up
with charachange

yu "Eso me pasa todo el tiempo en la biblioteca de la universidad, es tan vergonzoso."

hi "¿Ellos envían a alguien para que intente hacer que los lleves de regreso?"

show yuuko worried_up
with charachange

yu "No… La biblioteca de la universidad es más grande, ellos no se dan cuenta si pido prestado algo por más tiempo de lo normal. Es conveniente, porque su política sobre quedarse con los libros por mucho tiempo es… muy estricta, más estricta que aquí…"

"Me gusta cómo a pesar de lo que dijo, Yuuko no tiene problemas al pedir prestados libros por más tiempo de lo que se supone, de todos modos."

"Eso hace que ella, al estar muy por encima de mi propia tardanza, sea un poco hipócrita. El ladrón juzga por su condición, supongo."

"Captando el significado de sus palabras casi al mismo tiempo que yo, Yuuko se calla por completo y comienza a retractarse furiosamente."

show yuuko panic_up
with charachange

yu "… Ahh… ah… ¡Eso es diferente… de esta situación! Es completamente diferente…"

"Yuuko mira sus uñas por un segundo como si realmente quisiera mordérselas, pero está muy acomplejada como para hacerlo."

show yuuko worried_down
with charachange

yu "Por ejemplo, cuánto tiempo ha pasado… Sacaste algunos de estos libros hace meses, Hisao. Lo siento… Es solo que, otras personas también quieren leerlos. Pero si eres un lector lento, está bien…"

hi "No, es una total metedura de pata de mi parte. Para ser honesto, ni siquiera he leído algunos de ellos. No debería seguir sacando libros cuando tengo lecturas pendientes."

yu "Eso no es bueno…"

hi "Sí, realmente no lo es…"


"Ahora estoy comenzando a copiar su hábito de ir apagando mi voz silenciosamente. Por alguna razón, su torpeza es muy contagiosa."

"Dicho eso, estoy sorprendido. Yuuko parece casi normal hoy, aunque de vez en cuando, sus tics nerviosos de mesera siguen apareciendo."

"Ahora que lo pienso, ella no actuaba así cuando la vi por primera vez. Ella era un poco torpe y neurótica, pero no era ni parecido a este estado tan severo hasta que Shizune, Misha y yo nos encontramos con ella en el Shanghái."

"Podría ser que Yuuko tenga un complejo al tener a chicos de la escuela viéndola trabajar como mesera."


"Entonces supongo que fue un poco extraño para ella elegir el café más cercano a la escuela para trabajar. En ese caso, tal vez que el lugar tenga tan pocos clientes podría ser considerado un golpe de suerte."

hi "Bueno, entiendo. Los regresaré justo después de la escuela."

show yuuko smile_up
with charachange

yu "Tan pronto como sea posible, por favor."

show yuuko worried_up
with charachange

yu "Ahh… espera, ¿puedo pedirte una cosa más?"

hi "Claro, ¿qué es?"

show yuuko worried_down
with charachange

yu "Te… tengo que irme por un momento, pero no puedo dejar la biblioteca vacía…"

yu "Lo siento, ¿pero puedo pedirte que la cuides mientras no estoy? Solo por un momentito, ¡regresaré tan pronto como pueda! Estás en el consejo estudiantil, así que estoy segura de que si lo hicieras, estaría bien."

hi "Muy bien, lo haré, no te preocupes po—"

show yuuko closedhappy_up
with charachange

yu "¡Gracias!"

show yuuko neurotic_up
with vpunch

"Yuuko rápidamente se dobla hacia adelante como si estuviera tan agradecida que está a punto de darme un abrazo, pero se detiene a dos centímetros de él, lo cual al final hace que el gesto se vea extremadamente confuso."

"También estoy sorprendido de que pueda controlar tan bien su impulso, ya que ella parece algo torpe."

hide yuuko
with charaexit

stop music fadeout 6.0

"Antes de que al menos pueda decir “De nada”, ella ya está corriendo con la urgencia de alguien que va tarde a una cita."

"Ese podría ser el caso, pero no me sentiría seguro al asumirlo. Es Yuuko, y ella parece ser el tipo de persona que trata todo de esa manera."

scene bg school_library
with locationchange

"Ahora que estoy en la biblioteca, me siento un poco tonto. En realidad no sé qué se supone que haga. ¿Debería sentarme como normalmente lo haría y leer? Probablemente sí, pero no alcanzaría los altos estándares de Yuuko."

"Tal vez debería sentarme en el escritorio de la bibliotecaria, y darle a todo el que ingrese una mirada severa y analítica. Uso la de Shizune como punto de partida, y la practico un par de veces en la superficie reflejada de un bolígrafo."

"Creo que se ve bastante bien. Me frustra el hecho de que nadie ingrese, así que abandono la idea rápidamente, y en vez de eso simplemente decido ir a buscar a Hanako."

"Está desierto. Creo que veo a alguien, pero en el segundo en que parpadeo, quien sea que era se ha ido."

"Tan pronto regreso al escritorio de Yuuko y abro un libro que se ve interesante, una persona conocida se mueve enfrente de mí como un péndulo que cae."

show kenji invis:
    center
    xpos 0.4
with None

show kenji tsun at center
with dissolvecharamove

play music music_kenji fadein 0.5

ke "Oye, bibliotecaria, he estado buscándote durante unos, diez minutos. ¿¡Qué!? ¿Eres tú? Hombre, realmente te mueves mucho, o el consejo estudiantil hace que te muevas. ¡Esas perras! ¿Cómo pudieron?"

show kenji rage
with charachange

ke "¡Esclavistas!"

"Él debe estar exagerando, porque solo me tomé treinta segundos para dar una lenta caminata por todo el lugar. La idea es superada por mi sorpresa al verlo."

hi "¿De dónde saliste? ¿Qué estás haciendo aquí?"

show kenji tsun
with charachange

ke "¿Qué, no puede un hombre ir a la biblioteca ahora? Ni siquiera puedo ir a la biblioteca sin que algún joven como tú me interrogue por eso. Veo a una chica que viene aquí todo el tiempo, pero nadie nunca le pregunta qué está haciendo aquí."

ke "¿Es porque ella lee y yo no?"

"Debe estar hablando de Hanako. Aunque supongo que ambos evitan a la gente, quiero decirle que leer es lo que sueles hacer en una biblioteca."

"Así que si él no está leyendo, lo que sea que esté haciendo está destinado a hacerlo ver mucho más sospechoso que ella."

"Pero al final, estoy muy sorprendido de que él se aparezca prácticamente de la nada."

hi "Eso— eso no me dice lo que estás haciendo aquí."

show kenji neutral
with charachange

ke "Estoy aquí por tu culpa."

"Su respuesta me hace sentir confundido. Tal vez me quedé dormido y todo esto es solo un sueño raro, y este Kenji no es real, sino en realidad es mi subconsciente. ¿Él va a comenzar ahora a darme consejos profundos pero imprecisos?"

show kenji tsun
with charachange

ke "Por tu culpa fui expulsado de mi habitación por las feministas. Ahora vago por esta biblioteca, como un soldado sin país o un fantasma. Debería perseguirte por arruinar las cosas para mí."

"Es una lástima, habría sido un sueño interesante, pero parece que él es el auténtico."

ke "Sí, tenías que comenzar a trabajar con mujeres, y eso las llevó hasta mi puerta. ¿Lo recuerdas? Deberías, ya que tú estabas allí. Después de ese día, sabía que estarían encima de mí. Debí haber confiado en mis instintos, pero era joven y estúpido."

hi "Eso ni fue hace una semana."

ke "Entonces, mi papá llamó y dijo que una de mis cartas no había sido enviada. La oficina de correos no podría haberla perdido, así que debió haber sido interceptada. ¡Guerra de información!"

show kenji neutral
with charachange

ke "Ahí es cuando supe que mi escondite secreto estaba en peligro. Ahora estoy huyendo, como un fugitivo. Es un código rojo."

hi "Las habitaciones no son secretas, ponen tu nombre y tu número en una placa justo en la entrada."

show kenji rage
with charachange

ke "Lo sé, lo vi. Son diabólicas. ¿¡Por qué no simplemente ponen un cartel grande de “Se Busca” del salvaje oeste, si van a ser así!? “Se Busca: ¡Vivo o Muerto!”. Probablemente vivo, así pueden clonarme o convertirme en un saltamontes."

show kenji tsun at Position(ypos=1.15)
with Dissolvemove(0.5)

"Al saltar sin avisar hacia una silla vacía enfrente de mí, Kenji saca un cigarrillo y comienza a girarlo entre sus dedos. Nunca lo he visto fumar antes, así que debe ser para efecto."

ke "Ni siquiera puedo volver a vivir donde quiero. Aquí es donde todo inicia."

ke "La brillantez táctica… Quiero decir, una vez que están en tu casa, se acabó, como las termitas. Si el plan feminista para la dominación COMIENZA allí, ¿adónde carajos podemos ir?"

show kenji happy
with charachange

ke "La única pregunta es cómo pudieron sacar una página del manual de estrategias de las termitas, cuando las mujeres son naturalmente repelidas por la madera."


hi "“Nunca puedes regresar a casa otra vez”. ¿Así es como dice el dicho?"

show kenji neutral
with charachange

ke "Hombre, no sé del nunca. Acabo de estar allí. No sé en qué otro lugar pueda ducharme y tener ropa limpia. Y comer, y usar el baño. Y ver televisión. Tengo que seguir viendo las noticias, para mantenerme informado."

"Para alguien expulsado de su habitación y viviendo a la fuga, él claramente no tiene reparos en regresar allí varias veces al día durante largos periodos de tiempo."

"Pero por ahora él se ha alejado lentamente de mí y le está hablando a un escaparate giratorio de novelas policiacas. Realmente no tiene sentido interrumpirlo, supongo."

play sound sfx_can_clatter

"Termino mi gaseosa y tiro la lata en la cesta cercana a la puerta. Golpea el borde, pero entra de todos modos. Silenciosamente hago un gesto de victoria con el puño."

show kenji neutral at center
with dissolvecharamove

"Kenji rápidamente se levanta y comienza a dirigirse hacia la puerta. En realidad no estaba prestando atención; espero no haber hecho ese gesto del puño en un momento inapropiado."

hi "¿Adónde vas?"

show kenji tsun
with charachange

ke "Seguías tragándote ese jugo."

hi "¿Y? Ni siquiera era jugo, era gaseosa. Y ya se acabó. ¿Y qué quieres decir con “tragármela”? Tomé dos sorbos."

ke "Sí, claro, tomaste como cincuenta millones de sorbos."

hi "Eso ni siquiera es posible."

show kenji neutral
with charachange

ke "Quizás para ti; yo voy más allá de lo imposible todo el tiempo. Bueno, como sea, ahora yo también tengo sed. Voy a traer mi propio jugo, ya regreso."

show kenji invis at Position(xpos=0.4)
with dissolvecharamove

with Pause(0.5)

show kenji neutral at center
with dissolvecharamove

"Regresa casi de inmediato, tan rápido que sospecho que él conoce de mi máquina expendedora secreta."

ke "También te traje una. Espero que te guste el jugo de uva. Ahora estamos a mano por lo de la pizza."

hi "Gracias."

show kenji neutral at Position(ypos=1.15)
with charamove

"Quiero decirle que le presté casi diez veces el valor de una lata de jugo de uva, pero eso podría hacerme ver mezquino. Sin oposición, Kenji se sienta y comienza a beber jugo furiosamente, como un hombre con una venganza contra las uvas."

show kenji happy
with charachange

ke "Sabes, es un golpe de suerte que lograra encontrarme contigo aquí, hombre. Como que necesito que me hagas un favor."

"Aunque es cínico, me pregunto si el jugo que me dio fue para poder pedirme este favor. Si lo es, es muy transparente, y mal planeado. Aunque dudo que Kenji pensara en algo tan profundo. Pedir las cosas directamente es más de su estilo."

ke "Necesito que me recomiendes algunos libros."

hi "Pero pensé que no leías."

show kenji neutral
with charachange

ke "¿Cómo supiste?"

hi "Tú me lo dijiste. Dijiste que crees que la gente te discrimina porque no lees."

show kenji happy
with charachange

ke "Bueno, así es. Y yo sí leo, leo audiolibros, porque ese es el estilo del futuro."

show kenji neutral
with charachange

ke "Pero tengo que leer un libro al mes para Estudios Literarios, y descubrí que en realidad la escuela no acepta clásicos tales como “Criptografía Avanzada”. Si no leo un montón de libros, van a reprobarme."

show kenji tsun
with charachange

ke "No puedo reprobar Estudios Literarios… Eso me haría un analfabeto. Eso significaría que mi mamá tenía razón. Mi mamá no puede tener razón. Tendré que estudiar tanto alfabetismo como sea posible."

hi "¿Y qué tal hacer algunos créditos extra?"

ke "No, gracias. Ya es bastante malo que vaya a tener que cargar estas estúpidas cosas ahora."

"Él recoge un diccionario, lo hojea, y lo coloca en el estante de novelas policiacas detrás de él."

ke "No puedo creer que realmente este sea el medio por el que nuestros antepasados solían ver porno."

"Escupo mi bebida sobre el libro que aún estoy sosteniendo, dañándolo más allá de toda esperanza de arreglo. Rápidamente reviso la contraportada y veo que su precio de venta sugerido es de 7900 yenes. Creo que podría tener un ataque cardiaco."


show kenji happy
with charachange

ke "Vaya, destruido. Pero no deberías haber hecho eso, aquí se toman el vandalismo muy seriamente. Te van a azotar."

"Él se ríe alegremente, divirtiéndose, antes de tomar un sorbo extremadamente largo y fuerte de su lata de jugo."

hi "No es vandalismo, no lo hice a propósito. Tú me hiciste hacerlo, con tus palabras."

hi "¿Y qué quieres decir con azotar? No quiero ser azotado."

show kenji neutral
with charachange

ke "Espera, cálmate, no quise decir que realmente te azoten, solo te hacen pagarlo, y te gritarán mucho, muchísimo. Es como si fueran a arrancarme el culo de un mordisco. Aun así no es gran cosa."

hi "No me importa si es figurativo, no quiero que me azoten, ni que me arranquen el culo de un mordisco, ni ningún tipo de castigo, id… idiota."

hi "¿Qué voy a hacer? Soy la única persona aquí. Que ella sepa, de todos modos. Ni siquiera puedo tirar el libro a la basura. Lo encontrarán. Entonces ella sabrá."

show kenji tsun
with charachange

ke "Maldición, viejo, deja de ser tan raro."

hi "¿Qué hay de raro en no querer ser multado?"

ke "Hombre, deja de alterarte, viejo."

hi "No me estoy alterando, estoy intentando ahorrar dinero."

ke "Qué tacaño."

show kenji invis at center
with Dissolvemove(0.5)

hide kenji
with None

stop music fadeout 1.0

"Estoy a punto de estrangularlo cuando escucho el “guajaja” de Misha viniendo del pasillo. Aparentemente, Kenji lo oye también, y usa la oportunidad para desvanecerse rápidamente detrás de la sección de autobiografías. Como el viento."

show mishashort hips_grin at center
with charaenter

play music music_comedy fadein 0.5

mi "¡Hola, Hicchan~!"

show bg school_library at bgleft
show mishashort hips_grin at twoleft
with charamove

show yuuko neurotic_down at tworight
with charaenter

"Misha grita exhuberantemente, arrastrando a una avergonzada Yuuko detrás de ella."

show mishashort sign_confused
with charachange

mi "¡Hicchan~! ¿Estabas hablando contigo mismo?"

"Por una parte, decir que sí podría hacerme ver algo loco. Por otra parte, si desenmascaro a Kenji, él podría salir corriendo y hacerme parecer loco por asociación."

hi "Sí."

show mishashort cross_grin
with charachange

mi "¡Ajaja~! ¡Está bien~! No te avergüences, Hicchan; yo a veces lo hago también, ¡cuando estoy sola! La~ la~ la~."

show yuuko worried_up
with charachange

yu "Ah… ¿no pasó nada mientras yo no estaba?"

hi "Absolutamente nada."

show yuuko worried_down
with charachange

yu "Huele a… uvas."

hi "Estoy usando colonia con aroma a uva."

"Miento descarada y obviamente. Por su reacción, voy a asumir que ella sabe que estoy mintiendo, o cree que tengo un pésimo sentido por las colonias."

"Ya que la lata de jugo de uva que bebí está justo allí, es probable que sea lo primero. Afortunadamente, ella no hace más preguntas."

hi "¿Qué están haciendo ustedes dos juntas?"

show mishashort sign_smile
with charachange

mi "¡Estuvimos almorzando juntas~! ¡Estrictamente negocios, un almuerzo de negocios~!"

"Intento imaginarme a Misha en traje, teniendo un almuerzo de negocios con alguien. De alguna manera, no puedo verlo."

hi "¿Qué tipo de negocios?"

show yuuko panic_up
with charachange

yu "¿No lo sabes?"

show mishashort hips_grin
with charachange

mi "¡Ajaja~! No es nada~, nada~. ¡Es normal que una parte del consejo estudiantil no sepa lo que la otra está haciendo~!"

hi "Oye, no digas “nada, nada” de algo como eso. Eso no es normal en absoluto. De hecho, es malo. Solo somos tres personas."

show yuuko neurotic_up
with charachange

"Yuuko ríe nerviosamente. Debe estar aterrorizada."

show yuuko worried_down
with charachange

yu "Misha dice que quieren poner carteles en la biblioteca… para las elecciones. Ahh… aunque falta muchísimo tiempo, supongo que está bien. No sabía que incluso yo podía decidir ese tipo de cosas…"

show mishashort cross_laugh
with charachange

mi "¡Sí puedes~! ¿No es genial~? ¡Ajaja~! ¿No estás feliz? ¡Viva~ viva~!"

show yuuko panic_up
with vpunch

"Misha agarra las manos de Yuuko y la obliga a aplaudir con alegría por ella. Yuuko no se ve muy feliz de conocer que tiene más responsabilidad y poder del que ella había pensado antes."

show mishashort sign_smile
with charachange

mi "¡Hicchan~! ¡Ya que estás aquí, puedes ayudarme a colgarlos!"

"Sacando un montón gigante de carteles de su mochila, ella los divide a la mitad como una baraja de cartas y me pasa la mitad ligeramente aplastada."

show mishashort hips_smile
with charachange

mi "¡Shicchan tuvo una idea muy buena~! ¡También podemos poner algunos folletos dentro de los libros~! ¡Entonces, aunque intenten ignorarnos, no podrán hacerlo! ¡Podrían hasta ser accionados por resorte!"

"Misha hace su mejor esfuerzo para transmitir el mismo tono que Shizune usó. Suena parecida a la real, y también un poco amenazante."

hi "Ella probablemente estaba bromeando."

show mishashort perky_confused
with charachange

mi "Eso me gustaba~."

show yuuko cry_up
with charachange

yu "N-no… por favor… eso no…"

show mishashort cross_smile
with charachange

mi "¡Un bombardeo de mercadotecnia superultraagresivo~! ¡También vamos a comenzar a ir de puerta en puerta~!"

hi "Esa es una idea terrible."

show mishashort cross_frown
with charachange

"Misha hace pucheros con su mejor imitación de Shizune, golpeteando las puntas de los dedos rápidamente en molestia."

mi "¡Hicchan~! Piensas que todas las ideas son terribles…"

hi "Sí, pero esa idea es muy terrible, demasiado terrible para ignorarla. No puedo permitir eso."

show mishashort hips_smile
with charachange

mi "¡Guajaja~! Hicchan, eso suena como un desafío. ¡Motín~, motín~!"

show yuuko cry_down
with charachange

yu "E-el motín es malo… No peleen."

show mishashort hips_grin
with charachange

mi "¡Guajaja~! ¡Era solo una broma~!"

show yuuko worried_down
with charachange

yu "Bueno…"

show yuuko worried_up
with charachange

yu "No peleen."

show mishashort cross_laugh
with charachange

mi "Aja~ ja~ ja~."

"La manera como Yuuko suena cuando intenta ser firme me hace pensar en una maestra de kínder. Supongo que la hace muy persuasiva a su propia manera."

hide mishashort
hide yuuko
with charaexit

stop music fadeout 5.0

"Poner los carteles es sorprendentemente difícil, simplemente porque la biblioteca ya está cubierta con tablones de anuncios y folletos alineados cada dos metros, algunos de ellos en lugares tan improbables que nunca los habría notado antes."

play sound sfx_warningbell

"El decidir cuál de ellos quitar a favor de los nuestros le añade mucho tiempo a lo que habría sido un trabajo simple. Para cuando la campana suena para indicar el final del almuerzo, Misha y yo aún tenemos una considerable cantidad de carteles."

"Al salir, decido pegar uno justo al lado de la puerta. Debe ser uno que Misha hizo; tiene un pequeño dibujo de Shizune en la parte inferior."

scene black
with dissolve

label es_S28:

scene bg school_scienceroom
with locationchange

"Un par de días después, Shizune se va a almorzar sola y no regresa. Ella realmente debe estar inundada con trabajo del consejo estudiantil, aunque sé que probablemente gran parte de ese trabajo se lo puso ella misma."

scene bg school_hallway3
with shorttimeskip

"Cuando llego al salón del consejo estudiantil, encuentro la puerta sin seguro. Antes de abrirla, me detengo por un segundo, para ver si puedo oír la risa de Misha a través de ella. Nada."

"Casi tomaría eso como una señal de que no hay nadie adentro, pero Shizune no dejaría la puerta sin seguro en ese caso."

play sound sfx_dooropen

scene bg school_council
with locationchange

"Ella está en su escritorio, durmiendo en su silla con los brazos cruzados sobre su pecho."

"Qué pose tan rígida; si no fuera por sus ojos cerrados, no habría manera de saber que estaba dormida. De hecho, ni siquiera puedo estar seguro de que esté dormida ahora."

"Normalmente, daría golpecitos en un escritorio para despertar a alguien más, pero no funcionaría con ella."

"Inmediatamente comienzo a pensar en trucos que podría hacerle si está durmiendo. Es decepcionante que mi hilo de pensamiento vaya por ese tipo de direcciones."

show shizu basic_normal at center
with charaenter

ssh "Hola. Buenas tardes."


play music music_shizune fadein 3.0

"Ella gesticula un saludo con cada mano. Es muy confuso."

his "Oye, ¿qué estabas haciendo? ¿Holgazaneando en secreto?"

show shizu behind_smile
with charachange

"Shizune sonríe, pero baja la cabeza para esconderla, y en lugar de eso hace su mejor esfuerzo para verse molesta."

show shizu adjust_frown
with charachange

ssh "No te quedes ahí parado, me pone nerviosa si estoy sentada y tú no."

"Tomo asiento en la silla más cercana, mientras que Shizune hace una pausa para ajustar sus anteojos sobre el caballete de su nariz, como si estuviera afinando un instrumento."

show shizu adjust_angry
with charachange

ssh "¿Por qué estás tan lejos?"

his "¿Eso también te pone nerviosa?"

"Frunciendo sus labios, a Shizune no le hace mucha gracia que yo me burle de ella."

his "Tenía algo de tiempo libre, así que pensé que pasaría y vería si todavía estabas ocupada."

show shizu behind_blank
with charachange

ssh "¿Quieres ayudarme?"

his "Sí."

show shizu adjust_smug
with charachange

ssh "Lástima."

show shizu behind_smile
with charachange

ssh "Estoy agradecida, pero no es necesario. Acabo de terminar lo último, y ahora todo lo que se necesitaba hacer ya está hecho."

his "Qué formal. Misha estaba igual de formal ayer. ¿Ambas están portándose serias en los asuntos oficiales del consejo estudiantil?"

show shizu basic_normal2
with charachange

ssh "Siempre soy seria. Como deberían serlo los candidatos al consejo estudiantil."

"Eso fue rápido. De cero a criticar inmediatamente a personas que ni siquiera son sus colegas aun antes de que yo haya tenido la oportunidad de estirar las piernas."

show shizu behind_frown
with charachange

ssh "Al menos los presidentes. Ellos necesitan iniciativa, luego quizás puedan motivar a todos los demás, o al menos reprenderlos. Pero aunque haya un montón de ellos, todos son tan faltos de carácter."

show shizu basic_angry
with charachange

ssh "No hay nadie lanzándose para vicepresidente. Así que, todos ellos quieren el premio mayor, pero ninguno tiene el impulso apropiado para él. Y luego los tesoreros son siempre tan excéntricos, he decidido usar mi poder para eliminar la posición."

his "Espera un segundo, por favor. ¿Acaso puedes hacer eso? No creo que funcione de esa manera."

show shizu adjust_frown
with charachange

ssh "Es como es."

"Con eso, Shizune mira sombríamente a la distancia, frotando el marco de sus anteojos. Eso no responde la pregunta, futura dictadora."

show shizu behind_frown
with charachange

ssh "Estoy decepcionada. Deberían quererme fuera de aquí más rápido, porque quieren el puesto, o al menos no estar de acuerdo con que yo lo tenga."

ssh "Si no puedo movilizar un montón de aspirantes al consejo estudiantil por cualquier razón, todo mi trabajo habrá sido para nada."

show shizu adjust_angry
with charachange

ssh "¡Si van a ser tan lentos con eso, entonces me aferraré a mi cargo tanto tiempo como sea posible!"

play sound sfx_snap

"Shizune puntúa la frase con un chasquido de sus dedos, creando un sonido tan agudo como un disparo. Me pregunto si ella sabe lo fuerte que puede hacer eso."

"Definitivamente es un captador de atención, así que solo podría verlo como invaluable para un mudo. Ella podría haberlo practicado por eso."

his "“Todo”, ¿eh? Eso es muy severo."

show shizu behind_blank
with charachange

ssh "Siempre pensé que esta es la verdadera prueba. Dejar una impresión duradera es importante. Es por eso que no construyo castillos de arena, se desmoronan cuando te vas."

his "Quizás, pero si veo uno especialmente genial, aún pienso que es impresionante. Diré que es impresionante."


his "Como que te admiro. Así que, para mí, eso sí sirvió de algo."

show shizu adjust_happy
with charachange

"Ella tira de sus anteojos como si quisiera quitárselos, sonriendo con ironía."

show shizu basic_normal
with charachange

ssh "Lo siento."

show shizu behind_blank
with charachange

ssh "Fui descuidada, y algo egoísta se me escapó."

show shizu basic_normal
with charachange

ssh "Siempre he querido estar en la cima. No importaba lo que era, mientras fuera la mejor en ello, y lo entendiera completamente, y lo hiciera mío."

show shizu adjust_happy
with charachange

ssh "Como cuando escuchas una canción y sueñas con ser músico, o ves un avión y deseas poder ser piloto. ¿Alguna vez has tenido un sueño como ese?"

his "Sí."

"La primera vez que jugué futbol, me preguntaba si quizás podría ser tan bueno como para cautivar a la gente. Pero eso solo era una fantasía. Tan pronto vi la brecha entre la gente con talento de verdad y yo, dejé esos sueños detrás de mí."

"Bueno, con mi corazón como está, no puedo jugar futbol nunca más, de todos modos."

his "¿Todavía tienes sueños como ese?"

show shizu basic_normal2
with charachange

ssh "No, son poco realistas. Me di cuenta de ello muy rápido. Siempre hay alguien mejor."

"Una expresión nostálgica cruza su rostro. Ella se ve extrañamente madura ahora mismo, como si los días de competir vigorosamente contra los demás por supremacía hubieran terminado hace mucho tiempo."

"Por supuesto, sé que nada podría estar más lejos de la verdad. Apenas la semana pasada, ella quería ver quién de nosotros podía inflar la burbuja más grande con un pedazo de chicle."

"Podría ser que ella era incluso peor cuando era joven; un pensamiento aterrador."

show shizu behind_smile
with charachange

ssh "Me gustaba eso. Que siempre hubiera alguien mejor. Cuando alguien más grande que yo aparecía, me emocionaba tanto. Quería desafiarlo."

show shizu adjust_frown
with charachange

ssh "Aunque al final, por lo general resultaban ser mejores, y yo me quedaba asombrada. Hay unas personas que están en un nivel completamente diferente. Después de un tiempo, me puse celosa. Quería algo como eso para mí misma."

his "¿Eso es lo que es el consejo estudiantil, la cosa indicada para ti?"

show shizu basic_normal
with charachange

ssh "No, no. Aunque a veces se siente así, esa no fue la razón por la que decidí hacerlo. Esa es otra historia."

show shizu adjust_happy
with charachange

ssh "Pero… me gusta ser la presidenta del consejo estudiantil. Incluso si el trabajo es duro y siempre estoy abarcando más de lo que puedo, eso es lo que lo hace emocionante."

ssh "De todos modos, la gente que está en la cima no debería poder estar cómoda todo el tiempo."

his "Suenas como una granjera."

"Aunque no le quedarían bien, Shizune se vería bonita con un overol y un sombrero de paja."

his "Entonces, si esa no fue la razón, ¿por qué te lanzaste para el puesto?"

show shizu behind_frown
with charachange

ssh "No lo hice, pero al final, decidí quedarme con él de todos modos. Quería ser la presidenta del consejo estudiantil porque el viejo consejo estudiantil era estúpido."

show shizu basic_normal
with charachange

ssh "Y quiero animar a la gente, para que así ellos puedan decir, “Eso fue interesante, hoy fue interesante”. Ese tipo de cosas. Experiencias memorables."

show shizu behind_smile
with charachange

ssh "Estoy feliz, porque creo que tuvimos éxito. Misha, tú y yo."

show shizu basic_normal2
with charachange

ssh "Pero también tengo un deseo egoísta. Al principio era algo que pensé que solo sería una agradable bonificación, pero me he vuelto codiciosa."

show shizu behind_blank
with charachange

ssh "Es por eso que me haría feliz que las elecciones salgan bien. Sería la única manera en la que podría ver que mi deseo se cumpliera."

his "¿Cuál es, entonces?"

show shizu adjust_blush
with charachange

ssh "Es un secreto."

"Sintiendo que yo no podría estar listo para dejar pasar una elusión tan débil así de fácil, Shizune rápidamente detiene cualquier intento de hacer más preguntas, con la vergüenza coloreando su rostro."

"Es algo que ella quiere conservar para sí misma porque es muy tonto hacer lo contrario."

"Comienzo a sentir una punzada de hambre, y reviso mi reloj. Es más temprano de lo que parece. Demasiado temprano para la cena."

his "¿Tienes alguna clase de comida en tu escritorio?"

show shizu cross_wut
with charachange

"Por un segundo, parece que la pregunta la confunde, pero se recupera rápidamente."

show shizu behind_frustrated
with charachange

ssh "Los escritorios son para suministros."

his "La comida es un suministro."

show shizu basic_normal
with charachange

ssh "Deberías haber almorzado."

his "No pensé que sería un problema si no lo hubiera hecho. Si estuviera trabajando, no tendría que pensar en ello. Estaría muy ocupado para estar hambriento."

show shizu adjust_happy
with charachange

"Ella levanta la mano hacia su boca en un pobre intento de esconder una risa, e intenta esconderla más al fingir usarla para empujar sus anteojos hacia arriba del caballete de su nariz."

his "Supongo que tú no, puesto que ya comiste."

"No soy lo bastante bueno para decir en señas las palabras adecuadas, así que me conformo con señalar el montón de recipientes de comida china inclinándose precariamente por fuera del bote de la basura."

show shizu basic_normal
with charachange

ssh "Esos son de ayer."

his "Entonces ambos tenemos hambre. Vamos a conseguir algo para comer."

his "No de la cafetería. No había nada bueno durante el almuerzo, así que dudo mucho que haya algo bueno que sobre. ¿Ordenamos algo?"

show shizu behind_frown
with charachange

ssh "Ordenar dos días seguidos no es natural. Solo en caso de emergencias. Esa es mi política personal."

"Es por eso que ella debería pensar en poner algunos aperitivos en su escritorio, sería una manera más fácil de lidiar con este tipo de “emergencias”."

"Quiero decírselo, pero decirle en señas lo hambriento que estoy unas cinco veces me ha cansado demasiado como para actuar como un sabelotodo."

"Sin embargo, la tentación es muy grande."

mi "¡Hola~! ¡Hola, hola!"

"La voz con altibajos distintiva de Misha suena apagada a través de la puerta. Ella entra de golpe un segundo después."

show shizu behind_blank at tworight
show bg school_council at bgright
with dissolvecharamove

show mishashort perky_confused at twoleft
with charaenter

mi "…"

show mishashort perky_smile
with charachange

mi "¡Hicchan~! ¡También estás aquí~!"

hi "¿“También”? ¿Cómo supiste que ya había alguien aquí?"

show mishashort sign_smile
with charachange

mi "Si abre, alguien está adentro~."

show mishashort cross_laugh
with charachange

mi "¡Guajaja~!"

show mishashort hips_grin
with charachange

mi "¿Estoy interrumpiendo~?"

show shizu basic_normal
with charachange

"Shizune niega con su cabeza."

show mishashort hips_smile
with charachange

mi "¡Genial~! ¡Realmente es genial~! ¡Pero~! Estaba segura de que interrumpiría. ¿Este es un descanso?"

hi "Eso también pensé, pero resulta que todo lo relacionado con el consejo estudiantil terminó, por ahora. ¿Es por eso que estás aquí?"

show mishashort perky_smile
with charachange

mi "¡Guajaja~! ¡Sí~! ¡Así es, Hicchan!"

ssh "Lamento decepcionarte. Solo estábamos discutiendo si ordenamos algo para cenar o no."

show mishashort hips_grin
with charachange

mi "Eso suena divertido~."

hi "Pero Shizune no está siendo muy divertida al respecto. Ella dice que no puede ordenar comida dos días seguidos. ¿También tienes hambre? Porque si tienes, podríamos superarla por votos."

show mishashort hips_smile
with charachange

mi "Hm~ hm~, ¡eso suena divertido, Hicchan! Y, estoy un poquito hambrienta…"

hi "Pensé que dirías que suena como un motín."

show shizu adjust_frown
with charachange

"Shizune pellizca el marco de sus anteojos, pensando claramente que esto sí parece un motín, pero al estar en minoría por un claro margen de 2 a 1, no hay nada que pueda hacer. Misha ya ha sacado su teléfono. Es muy llamativo."

show mishashort sign_smile
with charachange

mi "Shicchan, prometiste que tendríamos una cosa del consejo estudiantil, solo para nosotros, ¿cierto~? ¡Cierto, cierto~! ¡Puede ser ahora~!"

show shizu behind_frown
with charachange

"Shizune solo niega con su cabeza. La última fiesta a la que podrá asistir como presidenta del consejo estudiantil de Yamaku es muy especial para ella como para darle esa etiqueta a nuestra cena temprana y espontánea."

stop music fadeout 3.0

"Aunque estoy seguro de que la verdadera será tal como esta: una comida como cualquier otra, con nosotros tres."

scene bg school_dormext_full_ss
with shorttimeskip

"Después de que terminamos de comer y limpiar, me despido de ellas y me dirijo a mi habitación. Aunque no me siento particularmente cansado, creo que me iré directo a dormir esta noche."

"Si estuviera en casa, mi mamá me daría lata para que no me vaya a la cama justo después de comer, pero lo que ella no sepa no le hará daño."

scene bg school_dormhisao_ss
with locationskip

"Le doy un vistazo al reloj tan pronto entro, y me doy cuenta de que es mucho más tarde de lo que había pensado."

"También se siente un poco tonto mirar el reloj cuando tengo un teléfono y un reloj de muñeca. Me quito mi reloj y lo levanto con una mano, mientras levanto mi teléfono con la otra. Me hace sentir poderoso, y estúpido."

play sound sfx_doorknock

"Intento irme a dormir sin éxito, y me alegro cuando alguien me interrumpe al golpear a mi puerta solo unos minutos después. Imagino que no podría ser nadie más que Kenji, lo cual es la razón por la que estoy sorprendido cuando resulta ser Misha."

play sound sfx_dooropen

scene bg school_dormhallway
show mishashort hips_smile at center
with locationchange

mi "¡Hola, Hicchan~!"

show mishashort perky_sad
with charachange

mi "No pareces feliz de verme~…"

hi "No, solo estoy algo sorprendido. ¿Shizune recordó algo que quiere que haga después de todo?"

hi "Es tarde, pero… en fin. Supongo que es bueno que no me haya cambiado."

show mishashort sign_smile
with charachange

mi "No~. ¡Solo pensé en seguirte, Hicchan~!"

hi "¿Por diversión?"

"No, por supuesto que no. Es porque ella quiere hablar. Debe ser sobre algo importante, y algo que ella no quiere que Shizune sepa."

hi "¿Quieres entrar?"

show mishashort hips_grin
with charachange

mi "Sí~, ¡gracias, Hicchan!"

scene bg school_dormhisao_ss
show mishashort invis at center
with locationchange

show mishashort perky_smile_ss at Position(ypos=1.13)
with dissolvecharamove

play sound sfx_doorclose

"Ella entra e inmediatamente se sienta en la silla. Es lo natural, pero esperaba que ella se sentara en la cama."

show mishashort cross_frown_ss
with charachange

mi "Hicchan…"

"Misha frunce el ceño con severidad, con los brazos cruzados sobre su pecho. Es como si ella estuviera tratando de interpretar a un interrogador sombrío. Todo lo que falta es el bigote y la bombilla que parpadea, colgando de un cable."

mi "¿Pusiste triste a Shicchan?"

play music music_drama fadein 6.0

hi "¿Qué quieres decir?"

show mishashort hips_frown_ss
with charachange

mi "Cuando fui a la oficina hoy, Shicchan no pudo escucharme llegar. Es por eso~, cuando abrí la puerta, vi una expresión muy confusa en su rostro. Shicchan se veía feliz y triste, y~ quería saber por qué."

hi "Bueno, no fue por mí. Ni siquiera la vi."

hi "Creo que ella está deprimida porque en unos meses ya no será más presidenta del consejo estudiantil."

show mishashort perky_confused_ss
with charachange

mi "Hm~… ¡Cuando le pregunté a Shicchan al respecto, ella dijo que estaba bien~!"

hi "Eso no tiene sentido. Shizune diría eso, pero es ridículo pensar que ella lo dejaría pasar tan fácilmente."

hi "Quiero decir, hay veces en las que ella querrá pelear por la última manzana, o leche chocolatada, o lo que sea. Y esas son cosas que ni siquiera importan."

show mishashort hips_frown_ss
with charachange

mi "La leche chocolatada es importante."

hi "Está bien, lo es. No te enojes. Pero no tanto como el consejo estudiantil lo es para ella. Ella no se despediría de ello tan fácilmente."

show mishashort hips_grin_ss
with charachange

mi "Guajaja~. Tienes razón~."

"Pensé que esto se suponía que era un interrogatorio, pero parece que Misha ya se ha olvidado de eso."

show mishashort sign_smile_ss
with charachange

mi "¡Pero~! No quiero que Shicchan me mienta para hacerme sentir mejor."

show mishashort hips_grin_ss
with charachange

mi "¡Jajaja~! La mayoría de la gente no sabe lo seria que es Shicchan y creo que ella solo está fingiendo. Estoy feliz de que la entiendas, Hicchan."

hi "Es obvio. Especialmente con la manera como habló sobre eso hoy."

"Misha se inclina para acercarse con interés, descansando su cabeza sobre sus manos."

show mishashort cross_smile_ss
with charachange

mi "¿En serio~? ¿Qué dijo?"

"Ellas son tan cercanas que no pienso mucho en lo fisgona que está siendo."

hi "Por qué ella se unió al consejo estudiantil. Algo así. Ella comenzó, pero luego decidió que algunas cosas deberían permanecer confidenciales. Y dijo en señas, “Es un secreto”. Entonces, supongo que eso es lo que me dijo: es un secreto."

show mishashort sign_smile_ss
with charachange

mi "Bueno~, ¡si alguien te dice que tiene un secreto, casi que puedes llamar a eso un secreto en sí, Hicchan~!"

hi "¿Al igual que como, de acuerdo a ti, la suerte es una habilidad?"

show mishashort hips_grin_ss
with charachange

mi "¡Puede ser!"

show mishashort cross_laugh_ss
with charachange

mi "¡Guajaja~!"

hi "Ten cuidado, no tan fuerte."

show mishashort perky_confused_ss
with charachange

mi "¿Por qué, Hicchan?"

hi "Vas a despertar a la mitad de la gente en el edificio, y encima de eso, las habitaciones no son mixtas."

show mishashort hips_frown_ss
with charachange

mi "Hicchan, ¿estás pensando en algo sucio?"

hi "Deja de ser rara."

show mishashort hips_grin_ss
with charachange

mi "Ajajaja~."

show mishashort hips_smile_ss
with charachange

mi "Si es así, está bien, creo."

"Al escuchar eso me doy cuenta de lo fácil que ha sido para mí hablar con Misha todo este tiempo, que podría durar todo este tiempo sin sentir la necesidad de estar en guardia. Esta es la primera vez que lo estoy."

show mishashort perky_sad_ss
with charachange

mi "Me siento triste, Hicchan."

mi "Es curioso, entre más feliz está Shicchan, más deprimida me siento. A pesar de que debería estar feliz por Shicchan. Aún lo estoy… Pero~, no puedo hablar de mis problemas con ella."

hi "¿Por qué no?"

show mishashort sign_sad_ss
with charachange

mi "Así como Shicchan no puede hablar de sus problemas conmigo. Es lo mismo, Hicchan. Si tenemos ese tipo de problema, entonces ya no estoy segura de lo que debería hacer. Me pregunto… si soy una mala amiga."






show mishashort perky_sad_close_ss at center
with characlose

stop music fadeout 2.0

"Misha se levanta y rápidamente se deja caer en la cama, hasta que estamos sentados a unos centímetros de distancia."

"Solo un par de segundos después, ella mueve su cabeza hacia adelante, y me da un pequeño beso. No va a mis labios, más debido a la mala puntería de su parte que de la mía."

hi "¿Qué estás haciendo?"

"Aunque solo es una formalidad. Sería estúpido no saber qué está insinuando, es solo que parece tan improbable que estoy esperando que haya alguna manera de que no tenga que lidiar con ello."


show mishashort hips_grin_close_ss
with charachange

"Ahora ella decide ser tímida, y se ríe, avergonzada."

mi "…"

show mishashort perky_smile_close_ss
with charachange

mi "¿Te gusto, Hicchan?"

hi "Sí."

"Su cabeza está enterrada en mi pecho. Se siente como si le estuviera hablando a mi cicatriz. Ella podría ser capaz de sentirla frotándose contra su mejilla."

"Me había esforzado mucho para esconderla de las dos antes. Parece una cosa tan tonta haberme preocupado tanto por eso, en retrospectiva."

show mishashort perky_sad_close_ss
with charachange



label es_choiceS28:
menu:
    with menueffect
    mi "Por favor consuélame, Hicchan. Solo por hoy."
    "Consolar a Misha.":



        return m1
    "Rechazar.":

        return m2


label es_S28a:

play music music_moonlight fadein 4.0

"Por más que finja protestar, he permitido que las cosas lleguen a este punto. Aunque sabía desde mucho antes de que saliera con eso que esto era lo que ella estaba insinuando."

"Por lo menos, yo estaba bien con este resultado. Si necesitaba alguna otra prueba, es simple: aún no la había rechazado."

"Podría haberlo hecho en cualquier momento, y estuvo mal de mi parte no hacerlo antes, pero ahora, no hacerlo es algo más allá del simple descuido."

show mishashort perky_sad_close_ss:
    linear 0.2 alpha 0 ypos 1.1
with vpunch

hide mishashort
with None

"Misha toma mi silencio como aceptación, y se aprieta contra mí fuertemente, como si intentara entrar en mi ropa. Mis brazos están envueltos por la suavidad de su piel y la calidez de su cuerpo. Me doy la vuelta por reflejo, y termino encima de ella."

"Ella me mira, como si esperara que yo tome la iniciativa, y nerviosamente cierra sus ojos en el momento en que le devuelvo la mirada. Supongo que no tengo elección, y torpemente comienzo a tratar de desvestirla, algo que nunca he hecho antes."

label es_S28h:

scene evh misha_naked:
    xalign 1.0 ypos 0.0 subpixel True
    easein 12.0 xalign 0.0
with whiteout

"Después de todo, solo he tenido sexo una vez antes, y estaba amarrado a una silla. Esta vez, yo tengo el control, como hubiera deseado entonces. Pero realmente es algo aterrador, ahora que lo tengo."

"Comienzo por desabotonar su blusa, y quitársela de sus hombros."

"Su figura es más curvilínea de lo que esperaba, y complementa su bonito rostro."

"Su sostén se desabrocha en su espalda, y tengo problemas para quitarlo, en parte porque Misha parece avergonzada de sus pechos, y con poco entusiasmo intenta cubrirlos incluso antes de que lo haya quitado."

"Cuando desabrocho su falda y comienzo a bajar sus pantaletas, ella ofrece más momentos de resistencia débil y falsa. Es solo una formalidad."

"Me doy cuenta de que las formalidades son muy importantes para Misha. Es por eso que ella siempre saluda a todo el mundo tan alegremente, incluso cuando probablemente no esté feliz de ver a alguien."

"Sus ojos están abiertos ahora, y muevo mi mano hacia el interior de su muslo, casi riendo cuando ella se estremece y casi la aplasta cuando aprieta sus piernas. Una reacción genuina, y una bonita."

"Shizune fue mejor en esconder su inexperiencia, aunque estaba igual de avergonzada."

hi "¿Estás lista?"

"Ella asiente sin mirarme."

scene evh misha_sex_aside:
    truecenter
    subpixel True zoom 1.05
    easein 6.0 zoom 1.0
with locationchange

"Cuando entro en ella, puedo sentir que se pone rígida con nerviosismo, lo que también comienzo a sentir cuando encuentro resistencia dentro de ella. Me siento tan tenso que cada vez que me muevo, se siente dolorosamente mecánico."

"Me pregunto si debería ir más rápido, como hizo Shizune. Pero Shizune es bastante atrevida. Ahora es una situación diferente, una en la que me arrepiento de haberme metido. Comienzo a empujar lentamente, y Misha hace una mueca de dolor."

mi "Por favor hazlo rápido…"

scene evh misha_sex_closed:
    zoom 1.0
with locationchange

mi "Ah…"

"Me detengo."

scene evh misha_sex_aside
with locationchange

mi "No, está bien."

"Y entonces entro aún más profundo en ella, lo más que puedo, sintiendo las manos de Misha agarrando mis brazos, y luego subiendo más alto, como si intentara escalarlos."

"Agarrándose de mis hombros, ella se presiona contra mí, uniéndonos más estrechamente, y no puedo hacer nada más que empujar de vuelta."

scene evh misha_sex_closed
with locationchange

mi "Ah~… aaah…"

"Al escuchar sus gemidos, voy más rápido y encuentro un ritmo. Sus manos se agarran entre sí alrededor de mi espalda, y siento sus codos enterrándose en el espacio bajo mis costillas mientras me muevo en ella."

"La sangre palpita en mis oídos como el redoble de un tambor, hasta que apenas puedo escucharla a ella."

mi "Hnn~…"

scene evh misha_sex_aside
with locationchange

mi "Esta es mi primera vez con un hombre. Es raro."

"Desearía que dejara de hablar. Su voz es tan callada y entrecortada que tengo problemas para entenderla, pero el tono de tristeza que la impregna es inconfundible, y solo me hace sentir más culpable."

"Se supone que la esté consolando, pero es completamente físico, y si Misha está siendo tranquilizada de cualquier manera por esto, no lo está mostrando. Eso me hace cuestionar si mi decisión fue la correcta. Realmente estoy empezando a dudarlo."

scene evh misha_sex_closed
with locationchange

"A pesar de eso, su suave arrullo en mi oído me hace continuar, al igual que la estrechez caliente y resbaladiza alrededor de mi miembro."

"Al final, con su pierna envuelta alrededor de la mía, ella se pone tensa al llegar al orgasmo, su suave cuello frotándose en mi mejilla."

scene evh misha_naked
with whiteout

stop music fadeout 6.0

"Le toma un minuto para separarse de mí. Me da una oportunidad para ver su cuerpo por completo, su piel rosada ruborizada con un rojo brillante y con pequeñas gotas de sudor. Siento frío."

mi "¿… Hicchan?"

"No puedo escuchar nada más que el tictac del reloj, y el sonido de mi propia respiración."

mi "… No importa, Hicchan."

"Busco la mano de Misha con la mía, y la acaricio. Qué ligera y delicada parece, incluso cuando me agarra con fuerza por la muñeca. La sensación es familiar."

scene black
with dissolve




label es_S28b:

show mishashort perky_sad_close_ss:
    linear 0.2 alpha 0 ypos 1.1
with vpunch

hide mishashort
with None

play sound sfx_pillow

"Antes de que pueda responder, ella empuja todo su peso contra mí, y me desequilibra lo bastante como para enviarnos a los dos hacia la cama. Si no respondo rápido, entonces la situación solo será más precaria."

"Sé que nunca debí haber dejado que las cosas se enredaran tanto como ya lo están."

"Entonces, aunque no es la manera más discreta de rechazarla, la aparto de mí. Misha cae hacia atrás sobre las sábanas, tan suave que parece que difícilmente se cayó en absoluto."

"Con los ojos cerrados, ella se queda así por un momento, antes de levantarse con una risa vacía."

show mishashort invis:
    center
    ypos 1.2
with None

show mishashort perky_sad_ss at center
with dissolvecharamove

play music music_moonlight fadein 6.0

mi "Tienes razón, Hicchan. Lo siento."

scene black
with shuteye

"No estoy seguro de cómo me siento. Arrepentido, un poco, aunque he terminado odiando el arrepentimiento. Triste, por una multitud de razones. También estoy un poco enojado, con ella y conmigo mismo."

"Y en cierta forma, hasta parece que en realidad no estoy sintiendo nada en absoluto."

hi "No lo sientas."

mi "No, Hicchan. Está bien~. Lo siento, en serio, en serio~."

mi "Pero… con solo preguntar fue suficiente para mí, creo."

mi "Estoy más feliz de que dijeras que no."

hi "¿Es eso cierto? Pues, eso es bueno."

mi "Sí~, lo es. Gracias, Hicchan."

"Ella se levanta y se apoya contra la pared. Estoy asumiendo que lo está. Mi cabeza me duele tanto que no me molesto en abrir los ojos."

"Estoy acostado en mi cama, escuchando el crujido de mi cabello frotándose contra las sábanas y el césped ondeando con el viento afuera."

"Supongo que debería decir algo más para tranquilizarla, pero me pregunto si eso realmente ayudaría. Tal vez sería mejor no decir nada. Simplemente no lo sé, aunque creo que en esta situación, no hay nada correcto que pueda hacer."

mi "Buenas noches, Hicchan."

play sound sfx_doorclose

stop music fadeout 4.0

"Con eso, ella se va, la puerta cerrándose con un clic detrás de ella como un susurro culpable."

"Tal vez es porque estoy ansioso de dejar el día de hoy detrás de mí, pero después de que Misha se fue, encuentro mucho más fácil quedarme dormido. Lo hago casi al instante."

scene black
with dissolve




label es_S29:

scene bg school_dormhisao
with locationchange

play music music_night fadein 4.0

"La mañana siguiente, me despierto pensando que la mayor parte del día va a ser gastado intentando evitar a Shizune y a Misha."

"Lo que pasó anoche todavía me hace sentir intranquilo. Había pensado que dormir ayudaría a aliviar ese sentimiento. Me siento como un idiota por creer que eso sería tan fácil."

"Pienso si Misha puede sentirse de la misma manera o no. Si es así, ella probablemente no irá a la escuela hoy."

"Había considerado hacer lo mismo, pero sería muy sospechoso, y el quedarme encerrado todo el día asustado no me llama la atención. En realidad nunca me ha llamado la atención."

scene bg school_scienceroom
with locationskip

"Como lo pensé, Misha no está en clase esta mañana."

"Shizune está, pero hoy es un día más ocupado de lo normal, así que ella pone toda su concentración en su trabajo en clase, y eso significa que hay poco tiempo libre para que ella inicie una conversación conmigo."


label es_S29a:

"Es extraño que deba huir de la idea de tener que hablar con Shizune después de pasar tanto tiempo intentando hacer justamente eso, pero no puedo pensar en alguna otra forma en la que me debería sentir. Tuve sexo con su mejor amiga."

"Si me siento así por eso, me pregunto cómo debe sentirse Misha. ¿Igual de arrepentida? Cuando se me insinuó, estaba más deprimida que sexy para comenzar. Solo puedo imaginarme cuán peor podría ser ahora."

"Pensándolo así, quiero verla de nuevo. Pero solo a medias. La otra mitad de mí aún está aterrorizada, aunque odio usar esa palabra."

"Me hace sentir avergonzado, pero estoy seguro de que es la única manera de describirme a mí mismo en este momento. No es un buen sentimiento."


label es_S29b:

"Me he acostumbrado tanto a ver a Shizune y a Misha juntas que no me había dado cuenta hasta ayer de lo mucho que últimamente eso no se ha dado."

"Y eso es una lástima, porque el asiento vacío junto a ella me recuerda que son una pareja. Así que, lo de ayer es algo que me llevaré a la tumba."

"Si me siento así por eso, me pregunto cómo debe sentirse Misha. ¿Igual de arrepentida? Cuando se me insinuó, estaba más deprimida que sexy para comenzar. Solo puedo imaginarme cuán peor podría ser ahora."

"Pensándolo así, quiero verla de nuevo. Pero solo a medias. La otra mitad de mí aún está aterrorizada, aunque odio usar esa palabra."

"Me hace sentir avergonzado, pero estoy seguro de que es la única manera de describirme a mí mismo en este momento."


label es_S29x:

scene bg school_library
with shorttimeskip

"Paso el siguiente par de clases en la biblioteca, sin ánimos para estar en clase por el resto del día, pero poco dispuesto a regresar a los dormitorios."

show shizu invis at center
with None

show shizu behind_frown at Position(ypos=1.14)
with dissolvecharamove

"Mientras estoy hojeando perezosamente las páginas de una novela de ficción histórica poco interesante, Shizune se sienta en la silla frente a mí, haciendo pucheros."

show shizu adjust_frown
with charachange

ssh "Creo que es algo inútil venir a la escuela y luego saltarte todas las clases."

his "Lo siento."

show shizu behind_frustrated
with charachange

ssh "Al menos diles a todos que estás enfermo."

his "Es solo que no me siento con ganas hoy. Aunque ayer estaba bien. Mañana, probablemente estaré bien. Tomar un día por enfermedad a mitad de semana es muy sospechoso. Esa “gripa de 24 horas” o lo que sea no funcionará."

show shizu adjust_frown
with charachange

ssh "Eso no es sospechoso."

his "Lo es."

show shizu basic_angry
with charachange

"Me giro de vuelta a mi libro, pero Shizune suavemente lo baja, en contraste con su expresión, la cual abarca la línea entre preocupación e ira."

show shizu behind_blank
with charachange

ssh "¿Ocurre algo?"

his "¿Qué?"

show shizu basic_normal2
with charachange

ssh "¿Hay algo que te molesta? Porque estás actuando un poco sospechoso hoy, de una manera diferente."

show shizu behind_blank
with charachange

ssh "Si algo te molesta, solo dímelo, o me enojaré. No soy buena leyendo a la gente."

"Qué cosa tan ridícula de decir, después de captar mi estado de ánimo tan fácilmente."

"Ella solo está bromeando a medias, pero hay algo de verdad en ello. Después de todo, ella no puede escuchar el tono, y tiene que depender de la lectura para comunicarse con los demás."

"Es como si solo pudieras tener conversaciones con alguien a través de mensajes de texto. Eso tiene que molestarte de alguna manera."

"Probablemente esa es la razón por la que ella mira tan intensamente a la gente, para medir su reacción. O quizás es por eso que presiona tanto a la gente, para hacer que reaccione."

"He pensado en ello antes, pero es muy difícil decir con seguridad cuáles son las motivaciones exactas de Shizune para todo."

"Así que, me pregunto cuánto de eso fue una broma. A veces, es fácil saberlo. Esta vez, no lo es. Asumiendo que no era una broma, no puedo decírselo de todos modos."

"Debido a que esto es lenguaje de señas, hay suficiente tiempo para serenarme y mentir eficazmente."

his "Nada."

show shizu cross_wut
with charachange

shi "…"

his "Solo he estado pensando mucho sobre el futuro del consejo estudiantil últimamente. Creo que Misha está haciendo lo mismo… bueno, a su propia manera."

show shizu behind_frustrated
with charachange

ssh "Yo también, pero ella no está aquí hoy. Desearía que me hubiera hecho saber algo, porque puede que necesite su ayuda más tarde hoy. La tuya también, a menos que estés ocupado."

his "No lo estoy…"

show shizu basic_normal
with charachange

ssh "Gracias."

show shizu behind_sad
with charachange

ssh "Siento que últimamente estoy perdiendo a mucha gente cercana a mí."

"No puedo pensar en una buena manera para responder a eso. Algo que la tranquilice y le dé confianza, decirle que no se preocupe. “Estoy aquí para ti. No soy una de esas personas”."

"Entonces, ¿quién lo es? Y parece tan forzado. Hago un movimiento de mi mano que parece extremadamente cruel tan pronto lo hago."

his "No deberías sentirte así."

show shizu basic_normal2
with charachange

shi "…"

his "Puede que esté un poco enfermo, no lo suficiente para pasar por la molestia de hacerlo oficial. Es solo que es más fácil para mí de esta manera."

show shizu behind_frown
with charachange

ssh "Es la manera equivocada."

"He escuchado que la manera difícil y la manera correcta por lo general son la misma cosa, así que no es un gran trecho decir que lo contrario es cierto."

show shizu basic_normal
with charachange

ssh "Bien, de acuerdo. Si dices que estás bien, eso es suficiente para mí."

his "Espera."

show shizu behind_blank
with charachange

shi "¿…?"

his "Tú me preguntaste, así que te la devuelvo. ¿Todo anda bien contigo?"

show shizu basic_normal2
with charachange

ssh "Sí."

stop music fadeout 3.0

"Ella lo dice en señas sin dudarlo un instante. Después de eso, Shizune espera para ver si voy a seguir con ello."

show shizu invis at center
with dissolvecharamove

hide shizu
with None

"No lo hago, y se va. Me siento como un idiota por no continuar, aunque creo que es mejor que no lo haya hecho."

"He estado en la biblioteca por bastante tiempo, y decido subir a la azotea para un cambio de ritmo."

play sound sfx_door_creak
play ambient sfx_rooftop fadein 1.0

scene bg school_roof_ss
with locationskip

"Una brisa fresca me golpea en el instante en que abro la puerta. Esta realmente es mi área favorita de la escuela, creo. Entonces veo que no soy el único aquí. Puedo ver a una chica con pelo color rosado chicle enfrente de mí."

"Está de espaldas a mí, pero no tengo que ver su rostro para saber quién es. Estoy seguro de que Misha es la única persona en el mundo con el pelo así."

"Tengo el sentimiento de que me he encontrado con ella en un mal momento. Obviamente ella quiere estar sola, y me pregunto si no ha notado mi presencia. Si es así, me iré ahora mismo. Pero lo hizo, y se gira para verme."

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

scene ev misha_roof_normal:
    yalign 1.0 xalign 0.5 subpixel True
    easein 12.0 yalign 0.0
with whiteout

play music music_sadness fadein 8.0

mi "Oh, Hicchan. Pensé que alguien estaba detrás de mí, pero no pensé que ibas a ser tú. Esta vez, tú me sorprendiste."

"Si ella se refiere a su costumbre de acercarse sigilosamente detrás de mí y pedirme que adivine quién es… Nunca me he sorprendido por eso."

hi "También estoy sorprendido. Pero esto es bueno. Tenía algo que quería hablar contigo, de todos modos."

mi "…"

hi "Eso no…"

hi "¿Qué está pasando entre Shizune y tú? Ella no me lo dirá, así que te lo pregunto a ti."

"“Porque es más fácil sacarte una respuesta a ti, ya que el mismo lenguaje de señas que me da la libertad de mentirle a ella le da una protección contra mis preguntas, así que puede evadirlas más fácilmente”. Cuando ella duda, la presiono más."

hi "Dame una respuesta sincera, por favor."

mi "Es complicado, Hicchan… Es por algo que sucedió hace mucho tiempo. Pensé que simplemente podía olvidarme de ello, pero~… es muy difícil. Así que~, ¡eso y la graduación aproximándose me hicieron querer pasar más tiempo con Shicchan~!"

scene ev misha_roof_sad
with charachange

mi "Pero ahora Shicchan siempre está ocupada. ¡Entonces~! Hemos estado peleando. Pero, ahora estoy cansada de eso."

mi "Porque~… me gusta Shicchan."

hi "A mí también."

scene ev misha_roof_normal
with charachange

mi "Guajaja~. No, no~. Sé que te gusta, Hicchan. Quiero decir que a mí me gusta Shicchan de la misma manera."

scene ev misha_roof_closed
with charachange

mi "Quiero que sea mi novia."

"Misha cierra sus ojos, como un criminal condenado confesando el último de sus pecados delante del verdugo. Eso solo me dificulta más pensar en una respuesta, y sé que tengo que dar una."

hi "Ya veo. Nunca lo supe."

scene ev misha_roof_normal
with charachange

mi "En realidad no quería venir a esta escuela, Hicchan~. Pero sonaba interesante, y aun si todos me odiaran, al menos se sentiría como si me dejaran en paz. Estaba aprendiendo lenguaje de señas, pero no era muy buena en ello~."

mi "Shicchan estaba intentando hacer que la gente se uniera al consejo estudiantil, porque eran solo Lilly y ella. Entonces, ella se acercó a mí. No podía entenderla en absoluto~."

scene ev misha_roof_angry
with charachange

mi "¡Pero~! Shicchan no usaba bolígrafo ni papel. Ella supo que yo estaba tomando clases de lenguaje de señas. Fui expuesta rápidamente, no sabía nada~… Eso solo la hizo esforzarse más, y odiaba a Shicchan y pensaba que se estaba burlando de mí."

scene ev misha_roof_normal
with charachange

mi "Pero esa no fue la razón~…"




mi "¡Así que~! Poco a poco me enamoré de Shicchan, y le dije… que la amaba."

scene ev shizu_flashback:
    truecenter
    zoom 1.15 subpixel True
    easein 30.0 zoom 1.0
with whiteout

mi "Fue en el salón del consejo estudiantil, ya sabes. Cuando éramos solo nosotras dos."

mi "Tenía unas fantasías con Shicchan estando sola en la oficina, intentando organizar todo ella sola. Me parecía tan solitaria, y tan triste~. Creo que yo quería que fuese así~."

mi "De esa manera, podría estar allí para Shicchan, y quizás yo le gustara a Shicchan. Aunque no había razón para que yo lo creyera, lo hice de todos modos. Quería que fuera cierto, así que estaba bien con dejarme creerlo, aunque creo que lo sabía."

mi "Ese día fue muy, muy~ hermoso también, Hicchan~. Habíamos acabado con todo, y yo estaba mirando por la ventana. Incluso a través de la ventana, la luz era tan cálida~… Quería quedarme así para siempre, junto a Shicchan."

mi "¡Pero~! Entonces miré a Shicchan, y ella estaba de espaldas a la ventana y todavía estaba trabajando en algo, aislándose del resto del mundo."
mi "La luz estaba sobre sus hombros, como cuando yo me ponía una manta sobre los hombros cuando era una niñita."

"Misha se detiene por un segundo como si intentara aferrarse a la imagen de Shizune en su mente."

mi "Shicchan se veía… hm~… Era como, Shicchan se veía de una manera que me hacía querer estar con ella… Pero se sentía como si fuera difícil que eso ocurriera."

mi "Guajaja~. Eso fue~, hace~ mucho~ tiempo. Mi pelo era diferente en ese entonces, también. ¿Un poco desordenado~? Me lo corté porque Shicchan siempre estaba hablando de eso."

mi "¡En fin~! Se lo dije, justo en ese momento y lugar; me confesé~."

scene ev misha_roof_sad
with whiteout

mi "Fui rechazada~."

mi "Entonces~, pensé que eso era todo, Hicchan. Pero Shicchan siempre estaba tratando de encontrarme, y odié a Shicchan de nuevo por eso. Y cuando le pregunté por qué lo estaba haciendo, era porque yo era su amiga."

"Sus mejillas tienen un toque de rojo en ellas. Me pregunto cuánta experiencia ha tenido ella con el llanto, que puede contenerse tan bien de hacerlo. Si ella no hiciera una pausa para secarse los ojos, puede que nunca lo hubiese notado."

scene ev misha_roof_closed
with charachange

mi "Tener a Shicchan diciendo eso me hizo feliz, pero también triste, y aunque ella nunca quiso hacerme daño, todavía duele. Incluso ahora…"

mi "Shicchan tiene una manera de manipular a la gente, Hicchan. A veces ella quiere hacerlo, y a veces realmente no, pero ocurre de todos modos~. Y a veces simplemente no estoy segura… de exactamente cuál es cuál. Y siento duda…"


mi "Simplemente desearía que Shicchan se sintiera atraída por mí y no por ti. Hizo que me preguntara si estaba empezando a odiarte a ti y a Shicchan… solo un poco. A mí… no me gustaba eso."

hi "Así que estabas pensando, ¿tal vez sería mejor si yo no estuviera aquí en absoluto?"

scene ev misha_roof_normal
with charachange

"Ella se ve confundida. El pensamiento nunca ha pasado por su mente."

mi "No es eso, Hicchan."

scene ev misha_roof_sad
with charachange

mi "Lo pensé mucho en estos últimos días, y no quiero odiar a nadie. Ni a ti, ni a Shicchan. Es tan estúpido que me haya sentido así, ¿no es cierto, Hicchan? No quiero pensar en ese tipo de cosas nunca más."

mi "Y extrañar a las personas, y estar alejada de ellas; estoy cansada de eso, y no quiero pensar más en eso."

mi "Pero ya lo hice. ¡Entonces~!… En realidad todavía soy el peor tipo de persona. No estaba pensando que sería mejor si Hicchan nunca hubiera venido a esta escuela. Estaba pensando… ¿no sería mejor si simplemente yo muriera?"



label es_S29xa:


scene ev misha_roof_closed
with charachange


mi "Después de todo, incluso ahora he hecho algo de verdad terrible. Imperdonablemente terrible."

"Misha se presiona más fuerte contra la valla a sus espaldas, como si esperara escurrirse a través de ella."

hi "No seas estúpida."

"Estoy sorprendido por el tono de mi voz."

hi "Lo siento."

hi "Me di cuenta de que odio cuando me quedo sintiéndome arrepentido, de cualquier cosa. Incluso así, es imposible para mí no terminar arrepintiéndome de algo."

hi "Ayer, hice algo estúpido. Eso es probablemente parte de la razón por la que estoy aquí ahora mismo, así podría descubrir si quizás podría… corregirlo, de alguna manera."

hi "¿Alguna vez te sientes así? Dijiste que has hecho algunas cosas terribles. Puedes intentar arreglarlas."

scene ev misha_roof_normal
with charachange

mi "Hicchan~, no es eso…"

"Sé que ella está pensando que estoy diciendo esto más por mí que por ella."

hi "No. No lo es."

hi "Solo creo que matarte es el arrepentimiento más grande con el que una persona puede terminar."

mi "…"

mi "Hicchan, eres tan dramático."

scene ev misha_roof_closed
with charachange

"Si ella hablaba en serio, nunca lo sabré. No intento averiguarlo; mientras ella deja salir un suspiro y cierra sus ojos como si fuera a dormir, siento que el ánimo peligroso que estaba captando de ella ha pasado."



label es_S29xb:

stop music fadeout 0.5
$ renpy.music.set_volume(0.0, 0.5, channel="ambient")

"Misha se presiona más fuerte contra la valla a sus espaldas, como si esperara escurrirse a través de ella."

scene bg school_roof_ss
show mishashort perky_confused_close_ss at center
with vpunch

$ renpy.music.set_volume(1.0, 6.0, channel="ambient")

"Sin pensar realmente en ello, agarro su mano. Mis reflejos son terribles, y logro agarrarle solamente algunos de sus dedos, pero eso no es importante."

play music music_rain fadein 6.0

hi "Lo siento. Es solo que dijiste algo muy raro ahora."

show mishashort perky_sad_close_ss
with charachange

mi "Jajaja~. Sí~, supongo que así es, Hicchan."

hi "Sí."

hi "¿Quieres saber lo que pienso?"

hi "Shizune es el tipo de persona que no dejará que nadie se acerque a ella, excepto en sus términos. Es frustrante, a veces es hasta exasperante."

hi "Eso probablemente me habría molestado, cuando estaba en el hospital y cualquiera que se cerrara conmigo estaba muerto para mí. Había olvidado eso por completo hasta hace poco. Recibí una carta, y toda era sobre eso."

hi "Estaba furioso. Pensé, “¿Cómo puedes acusarme de alejarme de todos y de darme por vencido? ¿No es eso lo que todos los demás hicieron conmigo? ¿Qué más se supone que haga? ¿Qué puedo hacer?”."

hi "Sí, incluso ahora, sé que así es como pasó, pero… ella también tenía razón. Sí me alejé."

hi "Entonces, he decidido que no voy a dejar que eso vuelva a ocurrir."

show mishashort perky_confused_close_ss
with charachange


label es_S29xba:

mi "¿El hospital? Hicchan… ¿para eso son esas pastillas?"


label es_S29xbb:

mi "¿El hospital? Hicchan… qué estás…"


label es_S29xbc:

hi "Solo escucha, por favor."

hi "Shizune es lo opuesto a lo que yo era. Ella siempre ha querido atraer más gente hacia ella. Esa fue la razón por la que Shizune estuvo interesada en mí en primer lugar, creo. Y creo que yo estaba decidido a no dejar que eso ocurriera, en cierta forma."

"Misha baja sus ojos, entendiendo perfectamente."

hi "Nunca me di cuenta de lo difícil que eso puede ser."

hi "Y ahora, siento que voy a devolverle el favor, aunque me tome el doble de tiempo. Ya he aprendido un segundo idioma solo para llegar hasta aquí."

hi "No fue tan difícil como lo pensé, pero definitivamente fue difícil. A veces, sentía que estaba abriéndome paso por una montaña, con el dolor en mis manos."

hi "Y tú hiciste lo mismo. Y fue por la misma razón, ¿no fue así? Eso es realmente sorprendente. Lo cual es la razón por la que me pone triste, y un poco enojado, que dijeras una estupidez como esa."


mi "…"

hi "Eso es lo que creo, de todos modos."

show mishashort perky_sad_close_ss
with charachange

"Sus hombros se caen, y Misha casi se desliza hacia el piso, como si se hubiera agotado toda su energía."

mi "Eres muy dramático, Hicchan."

"Ella lo dice, mientras aparta la mirada, girando su cabeza casi como si quisiera mirar al campus de la escuela, pero sin girarla lo suficiente para hacerlo."

mi "Guajaja~."



label es_S29y:

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene bg school_roof_ss
show mishashort perky_confused_close_ss at center
with locationchange

stop music fadeout 0.5
$ renpy.music.set_volume(0.2, 0.0, channel="sound")
play sound sfx_door_creak

"La puerta se abre detrás de nosotros, el sonido apenas se puede escuchar por encima de la brisa del ambiente."

scene bg school_roof_ss at bgleft
show mishashort perky_confused_close_ss at closeleft
with charamove

show shizu behind_blank_ss at tworight
with charaenter

ssh "Los he estado buscando a ustedes dos por todas partes. ¿Esta es una reunión secreta?"

"Ella se acerca a nosotros, apoyándose contra la valla junto a Misha como si necesitara detenerse y recuperar el aliento, antes de apartarse de ella y continuar."

show shizu basic_normal_ss
with charachange

ssh "Estoy aburrida estando sentada en el salón del consejo estudiantil todos los días ahora, sin ninguno de ustedes yendo siquiera. Tomarse algo de tiempo para descansar está bien, pero esto es demasiado."

"Normalmente, Misha y yo estaríamos inventando excusas a modo de broma en este momento. Esta vez, solo hay silencio. Shizune, siempre esperando resistencia, se sorprende por la falta de ella."

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_snap
show shizu adjust_happy_ss
with Dissolve(0.3)

"Unos cuantos segundos pasan en un silencio incómodo, el cual Shizune rompe con un chasquido ensordecedor de sus dedos, sonriendo como si dijera “eureka”."

show shizu basic_happy_ss
with charachange

ssh "Vamos a hacer algo juntos."

hi "¿Como qué?"

show shizu behind_smile_ss
with charachange

ssh "¡Cualquier cosa! Deberíamos ir primero al salón del consejo estudiantil, y luego pensar en algo desde allí."

hi "Eso más bien parece un truco para ponernos a trabajar."

show shizu basic_normal2_ss
with charachange

ssh "Muy gracioso."



label es_S29ya:

show shizu behind_smile_ss
with charachange

ssh "No es un truco. Lo prometo. Será algo divertido."

show mishashort perky_sad_close_ss
with charachange

play music music_rain fadein 4.0

"Misha contrasta la sonrisa cordial en el rostro de Shizune con una expresión solitaria en el suyo."

"Si Misha realmente está celosa de que yo le aparte a Shizune de ella, entonces esto solo empeoraría si los tres fuéramos juntos. Imagino que sería como frotarle sal a una herida abierta. Así que tengo la idea de dejarlas que pasen tiempo juntas."

"No soy tan idealista que piense que una sola tarde para ellas resolverá todo, pero podría ayudar. Parece una mejor opción que ir con ellas, porque mi presencia definitivamente no ayudaría en absoluto."

hi "Entonces ustedes dos pueden divertirse. Voy a irme a la cama temprano."

show shizu basic_normal_ss
with charachange

ssh "¿Estás seguro? Apenas terminó el almuerzo."

hi "Te lo dije, no me siento muy bien hoy. Creo que me enfermé de algo."

show shizu adjust_frown_ss
with charachange

ssh "Pensé que dijiste que excusas como esa no funcionarían."

"Me atrapó."

show shizu basic_normal2_ss
with charachange

ssh "Está bien. Pero rechazar la invitación de alguien es grosero. Esperaré que me lo compenses."

show shizu adjust_happy_ss
with charachange

"Shizune se da la vuelta y sonríe a Misha, y comienza a hacer señas de algo que no puedo ver. Asumo que está entre las líneas de “parece que solo vamos a ser nosotras dos”."

stop music fadeout 3.0

"Eso es bueno."

stop ambient fadeout 2.0

window hide



label es_S29yb:

show mishashort hips_grin_close_ss
with charachange

play music music_comfort fadein 5.0

"Misha se ríe, logrando dejar salir un “guajaja” contenido. Que Shizune no pueda verlo me hace sentir mejor. Significa que no fue solo para su beneficio."

show shizu behind_smile_ss
with charachange

ssh "Estaba pensando que de hecho ambos podrían ayudarme con algo. ¿Qué más hay? No podemos salir a comer. Ya hemos ordenado ayer, y eso ya fue romper la política. Tres días seguidos sería imperdonable."

show mishashort perky_smile_close_ss
with charachange

mi "¡Pero~! ¡Eso fue ordenar comida, Shicchan~! Salir a comer es diferente."

hi "Sí, totalmente diferente."

show shizu adjust_frown_ss
with charachange

ssh "Ambos se están engañando."

show shizu basic_normal_close_ss at closeright
with characlose

"Antes de que pueda responder, Shizune agarra mi mano, limitando mi capacidad para hacerlo."

"Con mis opciones reducidas tan drásticamente, no tengo más remedio que conformarme con hacerle una cara. Ella hace una de vuelta, antes de extender su mano a Misha también."

"Cuando Misha se muestra reacia a tomarla, camino hacia adelante tanto como me lo permite el aferrarme a Shizune al mismo tiempo, y tomo su mano yo mismo."

show mishashort hips_smile_close_ss
with charachange

mi "… Jajaja."

"Ella solo tiene un segundo para sonreír antes de que Shizune comience a tirar de nosotros con impaciencia hacia la puerta, sujetándonos juntos, como una cadena humana."

stop ambient fadeout 1.0

scene ev shizu_hands
with locationskip

"Aunque es peligroso, ninguno de nosotros parece pensar en saltarse paso alguno del camino a través de la escuela, fuera de las puertas, y a través del campus."

"Esto se siente familiar, como si hubiéramos caminado así antes. Nosotros tres, tomados de la mano. Por supuesto, el ambiente era mucho más feliz entonces."

"Puedo ver la tristeza que persiste en sus rostros, y me hace preguntar si algo realmente ha cambiado. Si todo esto es solo una distracción o no. Pero creo que solo soy yo volviendo a ser cínico por la ocasión. Es un comienzo."

stop music fadeout 3.0

window hide
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
