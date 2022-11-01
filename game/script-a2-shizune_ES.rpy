label es_S8:

window hide None

scene bg school_dormhisao
with locationchange

with Pause(1.0)

nvl clear

nvl show dissolve

play music music_dreamy fadein 5.0

n "\n\nLa mañana siguiente, recuerdo qué perfecta noche fue la de ayer. Tanto así que no puedo dejar de pensar en ello."

n "Probablemente no es el mejor momento para rememorar, ya que tengo un examen en la primera clase."

n "Ah, es tan injusto. ¿Cómo pueden hacer esto? Realizan un festival que es la culminación de lo que tiene que ser el esfuerzo de al menos unas cuantas semanas de trabajo en un domingo, ¿y luego siguen con exámenes iniciando la mañana siguiente?"

n "Tiene que ser algún tipo de broma de mal gusto."

n "No estoy muy preocupado por ello, pero me pregunto si realmente no pudieron haber aplazado esto por lo menos otra semana."

n "\n\nBueno, al menos el clima de esta mañana es tan agradable que puedo estudiar afuera antes de clase."

nvl hide dissolve

scene bg school_courtyard
with locationskip

nvl clear

nvl show dissolve

n "\n\nEs mucho más refrescante aquí afuera de lo que sería en el salón de clase. Por no hablar de lo silencioso que es, estoy comenzando a pensar que todos los demás estarán durmiendo hasta bastante tarde hoy."

n "Bajo las notas que estoy repasando por un segundo y miro fijamente el campus de la escuela, aún repleto con puestos del festival."

n "Mirándolos ahora de día, sin linternas de papel o multitudes de personas para apartar mi atención de ellos, noto algo curioso."

n "Muchos de los puestos que Shizune, Misha y yo visitamos anoche también resultan ser los mismos que construimos."

n "\n…"

n "\nQué adorable. ¿A Shizune se le ocurrió esto? Tuvo que ser intencional, especialmente conociéndola. ¿Ella esperaba que yo lo notara y viera el fruto de nuestras labores?"

play sound sfx_footsteps_soft fadein 5.0
stop music fadeout 4.0

nvl hide dissolve

show shizu basic_normal at center
with charaenter

window show

"Oigo pasos haciendo crujir el césped detrás de mí y me doy vuelta. Me siento un poco paranoico, pero todo lo que encuentro es a Shizune parada allí con una mirada inocua en su rostro."

play music music_shizune fadein 1.0

show shizu adjust_happy
with charachange

shi "…"

hi "Buenos días."

"¿Por qué sigo olvidando que ella no puede oírme?"

"Probablemente es porque me he acostumbrado tanto a Misha traduciendo por ambos que no me he encontrado con muchas situaciones en donde estuviera forzado a reconocer la sordera de Shizune y los problemas que pudieran derivarse de ella."

"Creo que ayer fue la primera."

"La saludo con la mano de todos modos. Por lo menos puedo hacer esto, pero ni siquiera voy a fingir por un momento que podría mantener una conversación con ella, considerando mi ignorancia en el lenguaje de señas."

"¿Sería descortés si simplemente regreso a mis notas? Realmente no sé qué más podría hacer."

hi "¿Dónde está Misha?"

show shizu behind_blank
with charachange

shi "…"

hi "No es solo porque no pueda entenderte. Ustedes dos están siempre juntas de todos modos, así que no estoy acostumbrado a verte sola."

"Sé que es tonto pero por alguna razón hablarle a ella me hace sentir menos incómodo."

show shizu basic_normal2
with charachange

show shizu adjust_happy
with charachange

show shizu behind_blank
with charachange

"Sorprendentemente, no se enoja en absoluto. Ella comienza a hacer señas; pero es diferente de lo normal. Las manos de Shizune se mueven más lentamente, y los gestos son más simples."

"Rápidamente me doy cuenta de que eso no es lenguaje de señas en absoluto, sino que ella aún está intentando comunicarse conmigo."

hi "¿Así que esto es el equivalente al lenguaje de señas reducido a términos simples?"

show shizu behind_frown
with charachange

"Estoy aterrado de que si intento gesticular de vuelta, simplemente quedaría como un completo idiota."

"La mirada en el rostro de Shizune me dice que está comenzando a pensar que intentar tener cualquier tipo de intercambio como este no es exactamente la mejor manera de lograr las cosas."

"Tiene que haber una mejor manera."

"¿Escribir en una libreta? Bueno, sí tengo papel y lápiz. Pero, ¿qué más?"

"¿Celulares? En realidad no le doy mucho uso al mío aquí, así que apenas lo cargo, y ni sé si Shizune tiene uno."

show shizu adjust_happy
with charachange

show shizu basic_normal
with charachange

"Ella toma la iniciativa, levantando un dedo para pedir una pausa antes de sacar una libreta y un bolígrafo de su mochila y escribir una sola palabra en ella:"

window hide

$ written_note("Hola.")

show shizu basic_normal2
with charachange

window show

shi "…"

"Me quedo mirándola inexpresivamente y recibo una mirada similar, pero de alguna manera más intimidante en respuesta. Ella empuja la libreta hacia mí con fuerza, claramente queriendo que yo responda."

window hide

$ written_note("Buenos días.")

show shizu behind_smile
with charachange

window show

"Shizune sonríe con una desproporcionada cantidad de felicidad. Ella comienza a girar su pluma triunfantemente mientras piensa a dónde ir desde aquí."

hi "Oh, vamos, no es que hayamos acabado de inventar el fuego."

show shizu basic_frown
with charachange

"Shizune empuja sus anteojos hacia arriba bruscamente, como si me hubiera escuchado, y luego comienza a escribir a un ritmo vertiginoso."

window hide


$ written_note("¡Usa la libreta! ¡Escribe escribe escribe escribe escribe escribe escribe escribe escribe escribe escribe escribe escribe escribe escribe escribe escribe escribe escribe escribe escribe escribe!")

window show

"Estoy confundido; ¿ahora se supone que debo tomarla y escribir “bueno”?"

"Esto es casi lo más lejos que podría imaginar de una conversación suave y fluida. Me hace envidiar la facilidad con que Misha es capaz de comunicarse con Shizune."

window hide

show shizu behind_blank
with charachange

$ written_note("¿Estás estudiando para el examen?")

window show

"Estoy bastante seguro de que puedo librarme de responder simples preguntas de sí o no como esta con asentimientos."

window hide

show shizu adjust_smug
with charachange

$ written_note("Estás aquí muy temprano; la mayoría de la gente duerme hasta tarde después del festival. Eso significa que eres anormal.")

window show

"… Ah, ¿sí?"

window hide

$ written_note("Tú también estás aquí.")

window show

"Pero antes de entregarle esa respuesta a ella, recuerdo lo que había notado antes, y añado:"

window hide

$ written_note("Tú también estás aquí.\n\nLo de ayer fue divertido. Hoy noté que construí muchos de los puestos a los que fuimos. Tal vez por eso eran tan familiares. ¿Esto fue otro juego?")

show shizu behind_frown
with charachange

window show

"Ella sacude su cabeza de lado a lado con indignación."

window hide

$ written_note("Nada de trucos.")

show shizu basic_normal2
with charachange

$ written_note("Pensé que porque tú habías hecho esos puestos, esos eran los más importantes. Teníamos que visitarlos, porque todos deberían poder apreciar el fruto de sus labores. Quería que pudieras ver y disfrutar lo que habías hecho.")

window show


"Estoy algo conmovido. Aun así, tengo que preguntarme por qué haría algo tan poco común en ella, y se lo pregunto en mi respuesta."

window hide

show shizu behind_blank
with charachange

stop music fadeout 3.0

$ written_note("Porque estabas deprimido.")

window show

"Quiero decir que estaba deprimido por días, pero basta. Es cierto, estaba bastante desanimado, y tampoco estaba siendo muy sutil al respecto la mitad del tiempo, así que es posible que ella lo supiera. Entonces, ¿todo lo que hizo fue para animarme?"

hi "Gracias."

"Lo murmuro antes de que pueda darme cuenta, pero a Shizune no parece importarle. En vez de eso lo escribo, y ella asiente una vez, como si no estuviera acostumbrada a ello."

"El silencio entre nosotros crece enormemente con cada segundo que pasa, y no hay nada que pueda hacer para romperlo. Tener que escribir todo en papel como que destruye cualquier esperanza de ser casual."

window hide

show shizu adjust_happy
with charachange

$ written_note("Buena suerte en el examen.")

window show

"Shizune empuja la libreta justo enfrente de mis ojos, rompiendo mi concentración. Tomando la iniciativa de nuevo, como siempre."

hide shizu
with charaexit

"Mientras ella camina hacia el edificio de la escuela, no puedo dejar de sentirme un poco triste."

window hide

nvl clear

nvl show dissolve


n "\n\nEsos se sintieron como los veinte minutos más largos de mi vida, y todo porque es tan extraño para mí tener una conversación cara a cara con alguien pasándonos notas entre nosotros, que no puedo evitar estar en blanco la mayor parte del tiempo."

n "Me hace querer aprender lenguaje de señas."


n "Eso es más fácil decirlo que hacerlo. Aunque en una escuela como Yamaku, podrían muy bien tener clases de lenguaje de señas. En ese caso, habría muy poca razón para no hacerlo."

n "La única persona en quien puedo pensar para preguntarle, en este momento, es Misha."

n "¿Qué tanto quiero saber esto? Hay dos opciones: esperar hasta después de clase, o ir a buscarla ahora."

n "Supongo que iré ahora, pero no estoy seguro de dónde está ella. Sin embargo, mi mejor apuesta sería comenzar a buscarla en el dormitorio de chicas. Después de todo, si no estaba con Shizune, ese es probablemente el único lugar donde ella estaría."

nvl hide dissolve

nvl clear

scene bg school_dormext_full
with locationchange

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_daily fadein 1.0

nvl show dissolve

n "\n\nUn tipo merodeando casualmente por el dormitorio de chicas temprano en la mañana es inaceptable, pero preguntarle a Misha por las clases de lenguaje de señas enfrente de Shizune sería impensable."

n "Ella tiene que venir a la escuela en algún momento. Después de todo, estamos en la misma clase, así que ella también tiene que realizar el examen."

n "Si espero aquí, me aseguraré de verla tarde o temprano."

n "Solo espero que no pase enfrente de mí mientras estoy hojeando mis notas."

n "\n\nResulta ser una espera bastante larga. Mientras los estudiantes ingresan a la escuela, me pregunto si Misha va a llegar tarde."

n "Finalmente la veo. Mientras ella salta por el campus, me doy cuenta de que tendría que estar ciego para no lograr verla con su cabello increíblemente distintivo."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear

nvl hide dissolve

show misha hips_grin at center
with charaenter

window show

mi "¡Hola, Hicchan~! ¡Buenos días~!"


hi "Buenos días."

"No tengo mucho tiempo antes de que la clase comience, así que voy directo al grano."

hi "Oye, ¿puedo hacerte una pregunta?"

show misha perky_smile
with charachange

mi "¿Una pregunta? Hm~… ¡Muy bien, Hicchan~! ¡Claro~ claro~! ¡Tengo tiempo, pero solo porque voy a llegar tarde!"

hi "¿Qué significa eso?"

show misha hips_grin
with charachange

mi "Jaja~. Debí haberme despertado más temprano, pero estaba tan cansada~… si lo hubiera hecho, tendría que estudiar, pero ya que no lo hice, ¡no dolerá~! ¿Qué ocurre, Hicchan?"

hi "Bueno, hay clases de lenguaje de señas aquí, ¿cierto?"

show misha hips_smile
with charachange

mi "¡Síp~! ¡Son opcionales! ¿Por qué quieres saberlo, Hicchan?"

"Por alguna razón esa pregunta brevemente me hace entrar en pánico."


hi "Por ningún motivo. Suena interesante, pero supongo que ahora es muy tarde para inscribirse, ¿cierto?"

"No estoy siendo exactamente muy sutil aquí, pero Misha nunca parece captar cosas como esa de todos modos, así que probablemente estoy siendo más cuidadoso de lo necesario."

show misha sign_smile
with charachange

mi "¿Hm~? Ah, bueno, Hicchan, he escuchado que cada vez hay menos estudiantes que toman lenguaje de señas cada año. ¡Entonces! ¡Si eso quieres, estoy segura de que te dejarán entrar~!"

show misha hips_grin
with charachange

mi "¿Estás pensando en aprender lenguaje de señas, Hicchan?"

hi "… Sí."

show misha perky_smile
with charachange

mi "Si aprendieras lenguaje de señas, Hicchan, eso haría muy feliz a Shicchan~. Si quieres, podemos ir a la oficina de maestros después de la escuela. Ellos probablemente te dejarán entrar."

hi "Eso sería genial."

hi "Pero no le digas a Shizune que quiero aprenderlo."

show misha perky_confused
with charachange

mi "¿Por qué no?"

hi "Para que pueda ser una sorpresa. Además, se verá mal si se lo cuentas esta mañana, y luego me entero en la tarde de que no puedo tomar las clases."

show misha perky_smile
with charachange

mi "Oh~. Tienes razón, Hicchan. Aun así, esto será difícil~… Es una noticia tan buena…"

hi "Estoy en el consejo estudiantil, así que bien podría intentar aprenderlo. Aun si solo es lo básico, sería un progreso respecto a nada. Además, Shizune y yo no podemos seguir pasando todo a través de ti como si fueras un teléfono o algo así, ¿cierto?"

"…"

with Pause(2.0)

show misha hips_laugh
with charachange

mi "¡Guajaja~!"

show misha hips_grin
with charachange

mi "¡Tienes razón, Hicchan~!"

"…"

stop music fadeout 4.0
play sound sfx_warningbell

"La campana suena para indicar el inicio de la primera clase, interrumpiendo nuestra conversación. Supongo que simplemente le preguntaré a un maestro después de terminadas las clases."

"Su reacción fue un poco extraña, pero me olvido de ello mientras el día avanza."

scene black
with dissolve



label es_S9:

scene bg school_scienceroom
with locationchange

play sound sfx_normalbell

"La campana suena y la maestra al frente del salón gesticula que las clases del día terminaron."

play music music_normal fadein 3.0

"Aunque entrar en esta clase fue sorprendentemente fácil, solo han pasado unos días y aún no estoy acostumbrado a la experiencia."

"Las señas en sí son más fáciles de aprender de lo que esperaba, pero la mayoría de mis compañeros de clase tienen problemas de audición."

"Encima de eso, la maestra favorece la inmersión. No la he escuchado hablar desde que le pregunté si podía tomar la clase. Es un concepto extraño, y realmente inquietante."

scene bg school_hallway3
with locationchange

"En el momento que salgo del salón de clase, oigo una risa familiar explotar por los aires a una corta distancia a mi izquierda."

show misha hips_grin at center
with charaenter

mi "¡Hola, Hicchan~!"

"Misha no está en mi clase de lenguaje de señas, así que esta es la primera vez que la he visto en este contexto. Aún no sé si el hecho de que ella no esté en mi clase es bueno o malo."

"Sería más interesante con ella en la misma, pero el potencial para situaciones incómodas se incrementaría drásticamente."

hi "Hola."

show misha sign_smile
with charachange

mi "¡Es una sorpresa verte aquí, Hicchan! ¡… Ah, es cierto! Estás tomando lenguaje de señas, ¿no es así~? ¡Cierto~!"

show misha perky_smile
with charachange


mi "¿Qué te parece la clase hasta ahora, Hicchan?"

hi "No es fácil aprender un nuevo idioma, pero creo que me estoy acostumbrando. A pesar de lo diferente que es de otros idiomas, de todas formas es más fácil que el inglés."

show misha cross_grin
with charachange

mi "¡Jaja~! ¿En serio, Hicchan?"

show misha cross_smile
with charachange

mi "Hm~… ¡Estoy de acuerdo~!"

"Solo estaba bromeando, pero aparentemente ella habla totalmente en serio."

"Me pregunto cómo Misha puede fácilmente traducir cosas para mí y al mismo tiempo tener una conversación con Shizune en un idioma diferente, tal como ella lo hace."


"Hasta ahora, había dado por sentado lo sorprendente que es."


"Alguien se choca con mi hombro y se disculpa. Se está abarrotando un poco aquí, ya que es el fin de la jornada y todo eso."

hi "Creo que deberíamos hablar en otro lugar mejor que el pasillo. Vamos a la azotea o algo así."

show misha sign_smile
with charachange

mi "¡Está bien~!"

"Decido continuar hablando en el camino. Es lo sorprendente y suficientemente tranquilo como para mantener una conversación mientras vamos."

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 1.0

scene bg school_staircase1
with locationchange

stop music fadeout 5.0

hi "Aún me está tomando algo de tiempo acostumbrarme a tener que mirar siempre a la maestra. Supongo que di por sentado todos esos años de simplemente escuchar las lecciones mientras garabateaba. También hace mucho más difícil tomar notas."

hi "La clase introductoria es pequeña, y ya me estoy quedando atrás. Supongo que tengo muchas cosas por hacer."

play sound sfx_door_creak
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene bg school_roof
with locationchange

hi "Sí, esto es mucho mejor."

"Me doy la vuelta para ver a Misha y la veo mirándome fijamente con sus manos en sus caderas y sus mejillas hinchadas hacia afuera."

show misha hips_frown
with charaenter

play music music_happiness fadein 4.0

mi "¿Hicchan, te estás quedando atrás? ¡Eso no es para nada bueno!"

hi "Comencé la clase una semana después que los demás. No es tan malo."

show misha sign_smile
with charachange

mi "Muy bien, Hicchan, ¡entonces vamos a repasar lo que aprendiste~! Seré tu tutora, ¿bueno~?"

"Esta es la primera vez que he oído “Seré tu tutora” usada fuera de películas pornográficas; no estoy ni de lejos tan excitado como habría esperado."

hi "No sé si necesito una tutora aún."

show misha perky_sad
with charachange

mi "Oh…"

"Ella se ve más decepcionada de lo normal. Me hace sentir incómodo verla hacer esa cara."

show misha hips_frown
with charachange

mi "¡Quiero ser maestra de lenguaje de señas, Hicchan! Pero~, sería realmente genial si primero pudiera intentar darle tutorías a alguien. Aun si es por un ratito, la experiencia sería valiosa."

hi "Ah, bueno, sí, eso es cierto."

hi "No sabía que tú querías ser maestra de lenguaje de señas."

"Es difícil de creer que no está tratando intencionalmente de hacerme sentir culpable, porque ella es muy buena en eso."


"Aun así, tiene sentido. Ella ya es muy buena en el lenguaje de señas por lo que he visto, y ciertamente tiene la voz para tratar con personas sordas. Aunque nunca la vi como el tipo de persona que sería maestra."

show misha hips_grin
with charachange

mi "¡Jajaja~! ¡Esa es la razón por la que quise venir a esta escuela, Hicchan!"

show misha sign_smile
with charachange

mi "También es muy caro asistir aquí, ¿sabes? Como quiero ser maestra de lenguaje de señas, tengo tasas de matrícula reducidas. Si no fuera por eso, no sé si podría continuar aquí."

hi "Ya veo. No es que crea que serías mala dando tutorías, es solo que no sé si las necesito en este momento."

show misha perky_sad
with charachange

mi "Tienes razón, Hicchan, eres inteligente."


hi "Bueno, no, eso solo me hace sonar arrogante."

hi "Muy bien, por favor sé mi tutora."

show misha cross_laugh
with charachange

mi "¡Ajajaja~! ¿En serio? ¡Muy bien~! ¡Bueno bueno bueno~! ¡Viva~! ¡Gracias, Hicchan~! ¡Haré mi mejor esfuerzo!"

show misha sign_smile
with charachange

mi "¡Empecemos ahora mismo~!"

hi "Demasiado pronto."

show misha perky_sad
with charachange

"…"

mi "Extraño a Shicchan~…"

hi "¿Acaso no la viste esta mañana?"

show misha sign_smile
with charachange

mi "¡Pero es difícil hablar con ella en clase, Hicchan! Y hoy tampoco hay consejo estudiantil~."

hi "Bueno, ha habido exámenes toda la semana. Estaría algo enojado si hubiera consejo estudiantil; me alegraré cuando hayan acabado."

show misha perky_confused
with charachange

mi "Cuando regresemos, no vas a escaparte, ¿cierto, Hicchan?"


hi "Por supuesto que no. Ya estoy metido en esto, después de todo."

hi "No te preocupes, no voy a dejar de aparecer de repente. Una promesa es una promesa."

"Misha se detiene por un segundo, sin verse muy convencida."

show misha sign_smile
with charachange

mi "Shicchan se toma el consejo estudiantil muy en serio, Hicchan. Ahora que te has unido, ella trabaja más duro que antes, ya que quiere dar una buena impresión."

show misha hips_frown
with charachange

mi "Algunas personas se unieron al principio, pero dejaron de venir poco después. Shicchan intentó conseguir que más gente se interesara en el consejo estudiantil pero no tuvo éxito."


show misha perky_sad
with charachange

mi "Incluso cuando alguien se unía, al final dejaba de venir. Daban excusas y solo lo posponían más y más hasta que dejaron de venir del todo."

show misha sign_smile
with charachange

mi "Sin embargo… Creo que tú realmente hablas en serio, Hicchan."

"Mis ojos permanecen enfocados en sus manos, inclinándose y moviéndose casi por voluntad propia, suavemente haciendo señas de todo lo que dice a ella misma mientras habla."



show misha perky_smile
with charachange

mi "Cuando dijiste que te unirías, ella estaba muy feliz."

show misha hips_smile
with charachange

mi "Shicchan piensa que eres interesante, Hicchan. Una persona poco interesante no tendrá el impulso necesario para unirse. Aun si lo hace, una persona que no sea interesante abandonará poco después."

mi "Eso es lo que dijo Shicchan."

show misha hips_grin
with charachange

mi "¡Así que~! ¡Es mi deber asegurarme de que continúes~!"

hi "¿Es por eso que quieres ser mi tutora? Eres algo maliciosa."

show misha cross_laugh
with charachange

mi "¿En serio, Hicchan? ¡Es la primera vez que alguien ha dicho eso de mí~! ¡Guajajaja~!"

"No hay posibilidad de que yo evitara el trabajo del consejo estudiantil ahora."


"Recordando los últimos días, he comenzado a darme cuenta de que la única razón por la que me uní en primer lugar fue por Shizune; su competitividad y fuerza de voluntad son atrayentes."

"Pero no puedo decirle eso a Misha."

show misha sign_smile
with charachange

mi "Muy bien, Hicchan, ¡vamos a repasar lo que aprendiste en clase hoy~!"

hi "Ni siquiera sabes lo que aprendí en clase hoy."

show misha hips_grin
with charachange

mi "Hm~, ¡tienes razón, Hicchan~! Muy bien, ¡entonces vamos a comenzar con lo básico~! ¡Te voy a enseñar todo desde el principio~!"

hi "Estás bromeando, ¿cierto?"

show misha perky_confused
with charachange

mi "¿Eh~?"

hi "¿Hablas en serio? Eso es como, días de lecciones, y ni siquiera estamos aprendiendo al mismo nivel…"

show misha sign_smile
with charachange

mi "¡Es como montar en bicicleta, Hicchan~! ¡Nunca olvidas lo básico! ¡Guajaja~!"

show misha sign_confused
with charachange

mi "Aunque no sé cómo montar en bicicleta~…"

"Oh, no."

show misha hips_grin
with charachange

mi "Cierto, cierto~. Quiero ser maestra un día, así que por supuesto que sé lo que estoy haciendo… ¡Muy bien~! ¡Bien bien bien~! ¡Vamos a comenzar~!"

stop music fadeout 3.0

show misha perky_confused
with charachange

mi "Eh…"

show misha sign_confused
with charachange

mi "… Mmm~…"

show misha perky_sad
with charachange

mi "Ajajaja~…"

"Parece como si se estuviera esforzando mucho, así que esto podría ser malo. Bueno, aprender un idioma es muy diferente a enseñarlo, y el primer paso es por lo general el más difícil. Honestamente, yo no lo podría hacer mejor."

"Aun así…"

show misha sign_confused
with charachange

mi "Em… El lenguaje de señas se introdujo formalmente en el siglo XVIII por un francés llamado… ah… cuyo nombre no puedo pronunciar, y él fundó la primera escuela pública para sordos en 1755, pero la historia no escrita del lenguaje de señas dice que…"

show misha sign_sad
with charachange

mi "Realmente no sé por dónde comenzar. Lo siento~… Bueno~, ¿qué mejor lugar para comenzar que la historia del lenguaje de señas? ¿Cierto~? ¡Cierto~!"

show misha hips_grin
with charachange

mi "No, espera, quizás el alfabeto. Muy bien~, ¡que sea el alfabeto, entonces!"

play music music_another fadein 0.5

show misha sign_smile
with charachange

mi "¡Muy bien, Hicchan~! Esto es algo muy básico, aunque algunas personas piensan que esto es todo el lenguaje de señas, y olvidan que hay toda clase de palabras y gestos específicos."

show misha hips_smile
with charachange

mi "¡Aunque realmente no puedes llegar a ninguna parte sin lo básico! Esta es la A. ¿La ves? ¡Ahora, inténtalo!"

hi "Pero esto ya lo sé."

"La complazco de todos modos."

show misha hips_grin
with charachange

mi "¡Jajaja! ¡Sí, esa es!"

show misha sign_smile
with charachange

mi "Ahora, esta es la B, y esta es la C."

"Misha hace un símbolo con cada mano, sin especificar cuál es cuál."

show misha perky_smile
with charachange

show misha sign_smile
with charachange

show misha hips_grin
with charachange

mi "¡Y ahora D, E, F, G, H, I, J, K, L, M, N, Ñ, O, P, Q, R, S, T, U, VWXY y Z~!"

"Sí, esto es malo."

hi "¿Crees que Shizune quiera hacer algo de trabajo del consejo estudiantil hoy de todos modos? Podríamos ir."

show misha sign_smile
with charachange

mi "¡¡Por supuesto que no, Hicchan~!! ¡Vamos, lo haré de nuevo! A, B, C, D, E, F, G, H, I, J, K… ¡Tu turno~!"

hi "¿Así que en realidad no hay trabajo del consejo estudiantil que necesite hacerse, o algo parecido?"

show misha hips_smile
with charachange

mi "¿De qué estás hablando, Hicchan? ¡Vamos, haz señas, haz señas~!"

hi "¿Así?"

show misha sign_smile
with charachange

mi "¡No, así!"

hi "Así…"

show misha perky_smile
with charachange

show misha sign_smile
with charachange

mi "¡Así~!"

hi "A… já…"

show misha perky_sad
with charachange

mi "Desearía que Shicchan estuviera aquí, esto sería mucho más fácil con ella. Jajaja, de todos modos, así es como se enseña el lenguaje de señas la mayor parte del tiempo, ¡con dos instructores~! ¿Sabías eso, Hicchan?"

hi "No."


"Dejo que mi cerebro piense cómo sería esto si Shizune estuviera aquí."

"…"

show misha hips_frown
with charachange

mi "¡Hicchan~! ¿Estás prestando atención?"

hi "Sí."

show misha sign_smile
with charachange

mi "Shicchan dice que el lenguaje de señas es diferente de cualquier otro, porque tienes que pensar en todo antes de que lo digas. Eso significa que cada palabra tiene más peso, Hicchan. Cada una de ellas es más importante de lo normal."

show misha cross_smile
with charachange

mi "Así que~, presta atención, por favor."

show misha sign_smile
with charachange

"Ella continúa su resumen básico de los fundamentos del lenguaje de señas. Finalmente ella comienza a hablar de cosas que comienzo a reconocer."

"Al final, estoy impresionado. Le tomó algunos tropiezos para llegar allí, pero como maestra, ella es muy buena cuando se pone seria."

stop music fadeout 4.0

scene bg school_roof_ss
show misha sign_smile_ss at center
with shorttimeskip

"Después de un rato comienzo a notar que se está haciendo tarde, así que le agradezco a Misha, me despido de ella, y regreso a mi habitación."

stop ambient fadeout 1.0

scene bg school_dormhisao_ss
with locationskip

"Aprendí mucho hoy."

scene black
with dissolve



label es_S10:

play sound sfx_doorknock

scene bg school_dormhisao
with vpunch

"Despierto sobresaltado por un estruendoso sonido de golpes viniendo de mi puerta."

"Mi primer pensamiento es, que podría ser Shizune. Después de todo, solo una persona sorda o un idiota golpearía así de fuerte a esta hora."

hi "¿Quién es?"

"Por supuesto, si es Shizune, no podría escuchar eso ni responderlo."

"No hay respuesta, así que estoy algo contento. No he visto a Shizune en un tiempo."

play sound sfx_dooropen

scene bg school_dormhallway
show kenji tsun at center
with locationchange

play music music_kenji fadein 2.0

"Abriendo la puerta, encuentro a Kenji sobresaliendo en el pasillo, sus ojos moviéndose nerviosamente de un lado a otro."

hi "Ah, eres tú."

show kenji neutral
with charachange

ke "Sí, soy yo. ¿Qué clase de reacción es esa?"

hi "Bueno, podría darte una respuesta más personalizada si hubieras respondido cuando pregunté quién era."

show kenji tsun
with charachange

"Kenji frunce el ceño y empuja sus anteojos hacia arriba exactamente como Shizune."

ke "¿Por qué estás haciendo esa cara rara?"

"Me pregunto cómo es capaz de verme haciendo una cara ahora, pero no fue capaz en las otras millones de veces que he reaccionado a algo raro que él ha dicho o hecho. Como que quiero averiguarlo, pero estoy muy cansado para hacerlo."

hi "Shizune empuja sus anteojos hacia arriba exactamente así. Tú sabes, la presidenta del consejo estudiantil. Es un poco raro."

show kenji rage
with charachange

ke "¿Qué demonios? ¿Qué quieres decir con que hay una chica que hace lo mismo? ¿Te refieres a que toca sus anteojos? Yo hago eso, eso es lo mío."

ke "¿Quién es esa perra? ¿Por qué están esas perras metidas en mis asuntos, robando lo que yo hago?"

show kenji tsun
with charachange


"Su carácter salta de ira a temor en un abrir y cerrar de ojos."

ke "¿Ella está tratando de reemplazarme? ¿Usurpadores de cuerpos? No, espera, esa es una copia exacta. ¿Mujeres usurpadoras?"


ke "Es como una combinación de mis dos miedos más grandes."

show kenji rage
with charachange

ke "¡Lo es!"

"No puedo creer que tenga razón…"

show kenji neutral
with charachange

ke "Oye, ¿vas a ir al pueblo hoy?"

hi "Eh, tal vez más tarde."

show kenji happy
with charachange

ke "Muy bien. Genial. Tengo unas… cosas que quiero que recojas por mí en la oficina de correos. Unas cosas delicadas y secretas."

"Él habla en voz baja, como si hablar de su correo, incluso en un tono de voz normal, lo pusiera en peligro."

hi "Puedes hacer que envíen tu correo directamente aquí, ¿sabes?"

show kenji neutral
with charachange

ke "No, no puedes. Puedes hacer que envíen tu correo a la escuela, y luego el consejo estudiantil lo recoge, y después ellas te lo dan a ti. No es lo mismo que el correo llegando a tus manos."

ke "No confío en el consejo estudiantil. Muchos tipos no reciben su correo aquí, ¿sabes?"

show kenji tsun
with charachange

ke "¡Probablemente se lo roban todo! ¿Creen que solo porque se lo mandan a ellas, tienen licencia para robar?"

ke "Puedo verlas ahora, metidas hasta el cuello en el correo, agarrando rápidamente todo el botín gratis al que puedan echarle mano. Repugnante."


hi "¿Dónde puedo encontrar al cartero que puede aparecer correo de la nada en tus manos?"

ke "No lo sé, apuesto a que el consejo estudiantil lo mató para preservar su monopolio sobre toda la mierda de los estudiantes."

hi "No trabaja de esa manera."

hi "Eso es lo que querías, ¿no? Bien, puedo recoger tu correo por ti, pero al final voy a cobrar todos estos favores. Ya me debes algo de dinero."

show kenji neutral
with charachange

ke "Gracias por recordármelo. Te lo pagaré después de que reciba mi paquete."

ke "Sí, disculpa, en realidad no puedo pagarte hasta entonces. Aún estoy quebrado."

hi "Entonces básicamente lo estoy haciendo por dinero, como un trabajo. ¿Por qué necesitas el paquete en primer lugar? ¿Hay dinero en el paquete?"

show kenji happy
with charachange

ke "No."

"Estoy seriamente estupefacto."

hi "¿Por qué no puedes ir tú por él?"

show kenji neutral
with charachange

ke "Porque hoy voy a remodelar mi habitación como un salón de guerra."

ke "Mientras los días pasan, me doy cuenta cada vez más de lo peligroso que es el feminismo. Realmente está en todas partes, incluso en lugares como Irán. No puedes saber qué tan lejos va."

show kenji tsun
with charachange

ke "Cuando la guerra comience, si no hemos trascendido el concepto de naciones para luchar por nuestros géneros, será el caos."

ke "Nadie sabrá quién tomará cuál lado, y una guerra contra el feminismo no solo significaría la Tercera Guerra Mundial, sino el fin de toda la vida en la Tierra como la conocemos."

ke "Si perdemos, todas nuestras ágiles mujeres japonesas serán violadas y esclavizadas por un montón de supremacistas lesbianas sociópatas."

ke "Mientras tanto, el puñado de hombres que no murieron en la guerra serán castrados y obligados a reparar retretes y a construir enormes monumentos conmemorando la victoria feminista."

hi "Eso es una locura. Estás loco. Creo que estás pensando demasiado en esto."


ke "Mientras los días pasan, me doy cuenta cada vez más de que no eres chévere."

hi "Solo hemos hablado como cuatro veces."

show kenji neutral
with charachange

ke "Oh. Lo siento."

hi "Sí, como sea, traeré tu paquete."

show kenji happy
with charachange

ke "Genial."

play sound sfx_doorslam

stop music fadeout 0.5

scene bg school_dormhisao
with vpunch

"Cierro la puerta y me lanzo de vuelta a la cama."

play ambient sfx_alarmclock


"Al segundo que mi cabeza golpea la almohada, un sonido dolorosamente fuerte asalta mis oídos, y me doy cuenta de que es mi reloj. Que la alarma suene significa que ahora mismo es el momento en que se supone debo despertar en primer lugar."

"Por lo menos, entre semana."

play sound sfx_impact

"Lo tomo y lo tiro sin levantar la vista. Queda atrapado entre la cama y la pared, y el ruido no para. De hecho, parece sonar más fuerte."

stop ambient

"Para el momento en que puedo sacarlo de allí sé que no voy a poder volver a dormir. La única cosa en la que puedo pensar para hacer ahora es ir al pueblo y simplemente traer el estúpido paquete de Kenji, pero es muy temprano para eso."

"Después de la ducha, me tomo mi medicamento. En realidad tengo mucha hambre hoy ya que me fui sin cenar ayer, y antes de eso solo tuve un almuerzo muy ligero."

"Me como las píldoras, masticándolas como una pierna de cordero. Son increíblemente amargas y asquerosas."

"Bueno, la buena medicina sabe mal, o algo así. Todavía tengo hambre, y todavía hay mucho tiempo para quemar, así que decido ir al pueblo y encontrar algún lugar para desayunar."

"No puedo recordar la última vez que comí fuera. Además, el clima es agradable, así que ¿por qué no?"

scene bg school_road
with locationskip

play music music_soothing fadein 3.0

"La caminata al pueblo es más larga de lo que recuerdo, posiblemente porque ha pasado un tiempo, y probablemente porque rara vez vengo aquí solo."

"Apenas hay coches en la carretera porque es muy temprano en la mañana, haciéndola inusualmente tranquila."

scene bg suburb_roadcenter
with locationchange


"La primera cosa que hago es comenzar a buscar un lugar para comer. Inmediatamente pienso en el Shanghái, pero quiero algo más abundante que emparedados o un pastel."

"Pero ya que es tan temprano, decido primero recoger el paquete de Kenji."

"Recogerlo en la oficina de correos no toma mucho tiempo, pero en el momento en que lo veo, estoy enfurecido por lo molesto que será cargar esta cosa en todo el camino de regreso a la escuela."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

show kenjibox:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"La caja es enorme, necesitas dos manos para sujetarla. Insultantemente, ni siquiera es muy pesada."

"Estaba pensando en deambular por un rato, pero con esta cosa a cuestas, eso va a ser un verdadero problema. Supongo que el Shanghái es mi única opción ahora."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

show kenjibox:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide kenjibox
with None

"Todo lo demás está cerrado, y los que no lo están todos tienen casi el mismo menú. Ese hecho también me hace llevarle algo más de clientela a Yuuko."

stop music fadeout 4.0

scene bg suburb_shanghaiext
with locationchange

"Antes de que pueda abrir la puerta y entrar, alguien me da un golpecito en el hombro desde atrás. Me doy la vuelta y veo a Shizune allí. Instintivamente, busco a Misha, pero ella no parece estar aquí."

show shizu adjust_happy at center
with charaenter

ssh "Buenos días."

"Parece que esas clases de lenguaje de señas ya están empezando a dar sus frutos. Estoy tentado en hacerle señas para responderle, pero entonces ella podría pensar que sé más de lo que realmente sé."

"Por ahora, solo la saludo con la mano y abro la puerta. Ella probablemente está aquí por su té matutino y no vino aquí solo para saludarme. Resulta que tengo razón, ya que Shizune me sigue al interior de la casa de té."

play sound sfx_storebell

scene bg suburb_shanghaiint at bgright
with locationchange

"Es un completo pueblo fantasma aquí. No es exactamente hora pico, pero todos los otros cafés que pasé tenían al menos unos cuantos clientes."


"En realidad, el Shanghái ha estado bastante solo cada vez que pasé por aquí. ¿Cómo es que este lugar sigue funcionando?"

show yuukoshang happy_down at center
with charaenter

yu "¡Hola! ¡Gracias por elegir ser clientes de nuestro establecimiento!"

show yuukoshang neurotic_down at Transform(ypos=1.25)
with Dissolvemove(0.2)

play sound sfx_impact
with vpunch

with Pause(0.3)

show yuukoshang neurotic_down at center
with charamove

"Yuuko se inclina con la fuerza de un hacha que cae y su cabeza choca con la caja en mis manos, lanzándola hacia el suelo."

play music music_comedy

show yuukoshang panic_up
with charachange

yu "Oh no, lo siento, lo siento mucho, mucho, ¡por favor perdóneme!"

hi "Está bien, y no tienes que hacer esa cosa de “¡Hola, gracias por elegir nuestro negocio!” ya que te conocemos."

show yuukoshang worried_up
with charachange

yu "Pero es parte de mi trabajo."

show yuukoshang worried_down
with charachange

yu "Están aquí temprano, ¿en qué puedo servirles?"

hi "Solo quiero un poco de café por ahora."

show shizu invis at right
with None

show yuukoshang worried_down at twoleft
show shizu behind_blank at tworight
show bg suburb_shanghaiint at center
with dissolvecharamove

"Me pregunto qué quiere Shizune. Sin Misha, no hay manera real de decirlo, ni alguna forma de preguntar. No he aprendido acerca de eso aún. Ella está aquí, así que estoy bastante seguro de que eso significa que también quiere algo."

hi "Eh, no sé realmente lo que quiere Shizune. ¿Ella pide algo de costumbre?"

hi "Espera, sin embargo ella podría querer algo más. Quizás deberías traernos un menú por si acaso."

"Busco uno alrededor, pero no puedo encontrar nada que se parezca remotamente a un menú."

show yuukoshang neurotic_up
with charachange

yu "Menús… Buscaré uno ahora mismo."

hi "¿Eh?"

show yuukoshang worried_up
with charachange

yu "Em… hay menús. Solo son… raros."

"Es solo un menú de restaurante, no una edición de coleccionista."

show shizu basic_normal2
with charachange

shi "…"

hi "Qué raro."

show yuukoshang neutral_down
with charachange

yu "¿Eso es lo que Shizune está diciendo?"

hi "No, ella no puede oírte. Solo que es raro para un café hacer que tengas que complicarte la vida para buscar un menú."

show yuukoshang worried_up
with charachange

yu "¿Raro…?"

show yuukoshang neurotic_down
with charachange

yu "Sí… tienes razón. Es tan ilógico. Hay tantas cosas… Como, ¿por qué se llama el Shanghái? Esta es una casa de té estilo occidental… pero, el nombre es chino… y la arquitectura es anticuada, pero mi uniforme es tan moderno y sofisticado…"

"Ella parece como si estuviera a punto de desmayarse. Si eso ocurre, ella probablemente se caerá hacia adelante y hará un completo desastre."

show yuukoshang panic_up
with charachange

yu "Ya no puedo trabajar más aquí."

"Qué mal lugar para que su hilo de lógica circular termine."

hi "No, vamos. Ese tipo de cosas es lo que diferencia este lugar; hay muchos cafés por aquí cerca, ¿sabes? Creo que es encantador, en realidad. Por favor no renuncies. El negocio es bueno, ¿no es así?"

show yuukoshang worried_up
with charachange

yu "No realmente…"


hi "Verás, creo que este es un buen trabajo para ti. Te va bien, no deberías renunciar."

"Nunca he tenido que distender este tipo de crisis antes."

stop music fadeout 2.0




"Al final, consigo calmarla, y convencerla de que estoy seguro de que Shizune solo quiere lo que siempre ordena aquí."

hide yuukoshang
with charaexit

show shizu basic_normal2 at center
show bg suburb_shanghaiint at bgleft
with charamove

show shizu basic_normal2:
    ypos 1.15
with charamove

"Yuuko se marcha para traer nuestras bebidas, y para entonces, Shizune ya ha elegido una mesa."

play music music_dreamy fadein 4.0

"No hay otros clientes, y Yuuko no es la persona más habladora, así que es muy tranquilo."

"No me molesta en realidad, pero desearía que hubiera alguna manera en la que pudiéramos comunicarnos. Hay tan pocos momentos en los que estamos solos."

"Shizune y Misha están casi siempre juntas, al punto donde a veces parece como si fueran una."

"Ahora, solo somos ella y yo, y soy incapaz de entenderla o de hacer que me entienda. Es terrible."

hi "¿No tienes tu pequeña libreta hoy? Sé que es fin de semana y todo eso, pero no es propio de ti estar desprevenida."

hi "Bueno, está bien. En realidad no me gusta usarla de todos modos. Sin embargo, sería útil ahora."

show shizu behind_blank
with charachange

shi "…"

show shizu basic_normal
with charachange

shi "… …"

"Shizune comienza a hacer señas en cortas ráfagas interrumpidas al detenerse para tomar un sorbo de té. Es extraño cómo ella no hace el más mínimo intento de cambiar la forma en la que actúa normalmente."

"Estoy hablándole en gran parte porque no estoy acostumbrado a los silencios largos. Brevemente me pregunto si es lo mismo para ella, en cierta manera; sin embargo, parece poco probable."

"Creo más que ella es el tipo de persona que no cambia su forma de actuar por nadie."

hi "Oye, parece que Misha se unió al consejo estudiantil gracias a ti. Con eso somos dos, ¿sabes? Solo estoy ahí porque me obligaste a unirme."

hi "Bueno, no me obligaste realmente, supongo. Si no fuera por ti, no me habría unido."

"Eso suena ligeramente romántico, y estoy sonrojándome un poco. Me siento como un idiota."

hi "Aunque, aún no sé por qué te uniste. Debería haber sido la primera cosa que preguntara, mirando atrás, pero tengo mucha curiosidad. Tendré que recordarlo para preguntarle a Misha en algún momento."

show shizu behind_blank
with charachange

shi "…"

hi "Es agradable hablar contigo, aun si no puedes entenderme. Me pregunto si es lo mismo para ti."

hi "Eso sería realmente… genial."

show shizu adjust_happy
with charachange

shi "…"

hi "No creo que el lenguaje de señas será tan natural para mí como Misha lo hace parecer, pero tiene que ser un paso adelante respecto a usar papel y bolígrafo, ¿cierto?"

show shizu basic_normal2
with charachange

shi "…"

stop music fadeout 4.0

"Ambos hemos terminado con nuestras bebidas por un rato, y los ojos de Shizune caen sobre la caja sentada en su propia silla a mi lado."

show shizu adjust_happy
with charachange

shi "…"

hi "Solo la estoy recogiendo para alguien, no es mía."

play music music_running fadein 0.5

show shizu basic_sparkle
with charachange

"Shizune la acerca hacia ella, con la intención de abrirla, y mi corazón casi salta por mi garganta. Rápidamente intento traerla de vuelta envolviendo mi pierna alrededor de la pata de la silla."

hi "Pero qué demonios, no la abras. No puedes abrir el correo de otras personas, eso no es legal."

show shizu basic_frown
with charachange

shi "…"

hi "¡No!"

show shizu cross_angry
with charachange

shi "¡…!"

"Una vez ella se pone en marcha, no hay casi manera de detenerla. Con los ojos llenos de emoción, ella se ve lista para pelear conmigo por este estúpido paquete y me doy cuenta de qué tan rápido esto podría convertirse en un juego de tira y afloja."

show shizu behind_frown
with charachange

"Ahora estoy casi fuera de mi asiento y moviendo las manos como un controlador de tráfico aéreo, antes de que ella finalmente se calme."

show shizu behind_frown at center
with charamove

"Shizune hace pucheros, no estando contenta con tener su curiosidad frenada, y se levanta para irse."

"Ya es casi hora, supongo. Hemos estado aquí un rato. Protectoramente levanto la caja antes de pararme."

show shizu basic_happy
with charachange


"De repente, ella junta sus dedos con entusiasmo y saca un marcador de su bolsillo, y comienza a escribir en la caja de Kenji."

hi "Oye, ¿qué estás haciendo? ¡Dije que no es mía!"

hi "¡Oye!"

"Ni siquiera puedo verla con la caja bloqueando mi visión."


hi "Bien, por lo menos déjame ponerla en el suelo primero."

"Tengo que hacerlo para leer lo que sea que esté escribiendo, de todos modos."

window hide

$ written_note("Te ayudaré a llevarla.", {"background":Frame("vfx/cardboard.jpg",0,0, tile=True)})


show shizu adjust_smug
with charachange

window show

"Sin embargo no parece que haya terminado, y Shizune después traza una línea feroz para indicar que hay una trampa."

window hide

$ written_note("Te ayudaré a llevarla.\n ___________________\n\nPero, ¡es un juego! El primero en tropezar pierde, y el perdedor tiene que llevarla el resto del camino por su cuenta.", {"background":Frame("vfx/cardboard.jpg",0,0, tile=True)})

window show

hi "Eso es estúpido, hay una posibilidad del cincuenta por ciento de que termine llevándola yo mismo de todos modos."

"En realidad, yo mismo me siento bastante estúpido en este momento. Olvidé que ella no puede oírme. Dejo de hablar y sacudo mi cabeza."

show shizu behind_blank
with charachange

shi "…"

show shizu cross_angry
with charachange

shi "¡…!"

show shizu adjust_angry
with charachange

shi "¡…!"

"No puedo entenderle en absoluto, pero ella da una impresión muy enérgica. Es claro que cree que es una gran idea."

"Bueno, si deja caer la caja o algo así, ella tendrá que llevarla. Eso haría las cosas mucho más fáciles para mí, obviamente."

"Las posibilidades son 50-50, entonces… probablemente son más altas de lo que serían para cualquier otro plan suyo. Muy bien, aceptaré."

show shizu basic_normal_close
with characlose

"Pensando en ello, no estoy seguro de cómo deberíamos hacer esto. Entonces Shizune agarra un extremo de la caja y la levanta, y yo tomo el lado que ella no está agarrando. ¿Está bien así? Es muy incómodo caminar de esta manera."

show bg suburb_shanghaiext
with locationchange

"Dejamos el café, y me encuentro deseando que las calles aún estén vacías. Yuuko parecía confundida en cuanto a lo que estábamos haciendo, e imagino que solo se pondrá peor a medida que más gente nos vea."

show shizu adjust_happy_close
with charachange

show shizu basic_normal_close
with charachange

"Shizune no parece molestarse en absoluto mientras camina con su brazo en este ángulo poco natural; solo sonríe con confianza y de vez en cuando hace algún tipo de gesto extraño."

show bg suburb_roadcenter
with locationchange

"Hay gente mirándonos mientras el tiempo pasa, y la multitud usual de la mañana comienza a llenar las calles."

"Me siento tonto, pero estoy seguro de que si me doy por vencido, Shizune lo tomará como una señal de rendición. No puedo permitirlo, porque creo que me está yendo bien hasta ahora."

show shizu adjust_happy_close
with charachange

show shizu basic_normal_close
with charachange

"Al principio, simplemente descarto las pequeñas señales de la mano de Shizune como su regodeo anticipado, pero rápidamente capto que ella en realidad está indicando hacia dónde quiere ir."

"Me doy cuenta de que esto no es una competencia. No es un gran desafío, en primer lugar, y segundo, en realidad es más un ejercicio de trabajo en equipo. Es solo que Shizune ha hecho un castigo por fallar en lugar de una recompensa por hacerlo bien."

stop music fadeout 3.0

show shizu adjust_blush_close
with charachange

"Nuestros dedos se tocan debajo de la caja, y Shizune aparta su mano, casi dejando caer su lado de la caja en el proceso."

"Bueno, es el fin del juego para ella."

"Ella no se ve muy feliz. ¿Acaso cree que lo hice a propósito para hacerla perder? Si es así, no le está dando mucha importancia. Todo vale en el amor y en la guerra."

show shizu basic_frown
with charadistant

"Siento que debería tomarla y llevarla yo mismo, pero ella me empuja cuando lo intento."

play music music_shizune fadein 1.0

"Ella me mira ferozmente como si quisiera regañarme, pero no puede. Con esa caja en sus manos, básicamente está amordazada."

show shizu basic_normal2
with charachange

show shizu basic_normal
with charachange

"Una triste expresión titila en su rostro por un segundo, quizás al darse cuenta de eso y de tener que reconocer que hay algunas limitaciones con las que tiene que lidiar después de todo."

"Sin embargo, ella sigue siendo tan orgullosa como siempre, aun cuando es en su perjuicio. Ella no aceptaría dejarme permitirle que evada las consecuencias de su apuesta."

"Cualquier cosa se vale durante el juego, pero los resultados tienen que ser honrados al pie de la letra, ¿eh?"

"Shizune es un tipo interesante de persona."

show bg school_dormext_full
with shorttimeskip

"La marcha de regreso a los dormitorios es tranquila. Shizune pasa el viaje moviendo la caja ocasionalmente como un cubo de Rubik gigante. Parece otro juego que ha inventado para divertirse."

"No puede ser bueno para lo que sea que haya dentro, pero no me importa lo suficiente como para detenerla."

"Tal vez así es como ella lidia con las cosas, convirtiendo todo en un juego; sin embargo, es difícil saberlo con certeza."

"Parece inútil tratar de psicoanalizar a Shizune. En el poco tiempo que nos hemos conocido, me he sorprendido en bastantes ocasiones."

show shizu basic_normal2 at centertremble_nl
with None

stop music fadeout 6.0

"Noto tiritar a Shizune. El viento está aumentando, y la escuela es bastante elevada. Tiene sentido que ella esté con frío. Sin embargo, si le diera mi chaqueta, ¿la rechazaría?"

play sound sfx_rustling

show shizu basic_normal2_close at center
with characlose

"Me quito mi chaqueta y la coloco sobre sus hombros antes de que tenga la oportunidad de protestar. Sus hombros son delgados y delicados, tanto así que quiero dejar mis manos sobre ellos por un momento."

show shizu adjust_blush_close
with Dissolve(0.2)

"Shizune se estremece cuando mis dedos la rozan, comprensiblemente sorprendida."

hi "Lo siento."

show shizu basic_normal_close
with charachange

shi "…"

show shizu adjust_happy_close
with charachange

shi "…"

"Sus dedos bailan suavemente sobre la superficie de la caja, y pienso en tomarla, pero dudo que ella me deje. Shizune hace un gesto rápido con sus manos lo mejor que puede, deteniéndose un poco después como si quisiera decir más."

"Estoy seguro de que lo que ella quiere decir es “gracias”. Me alegro de haber podido entenderlo."

scene black
with dissolve

$ suppress_window_after_timeskip = True



label es_S11:

window hide None

scene bg school_cafeteria
with locationchange

nvl clear

nvl show dissolve

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_normal fadein 0.5

n "\n\nLa maestra de lenguaje de señas dice que soy muy bueno."

n "Intento no pensar mucho en ello, pero la verdad es que últimamente lo estoy estudiando tan minuciosamente que es difícil no seguir regresando a ello al menos un par de veces al día. Supongo que lo estoy aprendiendo más rápido de lo esperado, pero aún no es suficiente."

n "Lo entiendo muy bien; entenderlo es simple. Bueno, tengo que concentrarme en ello para leerlo, pero es bastante fácil cuando lo hago."

n "Las señas en sí se pueden hacer, solo necesito un poco más de práctica. Sin embargo, ¿intentar hacer ambas cosas al mismo tiempo, incluso a la mitad de la velocidad con la que Misha lo hace? Es imposible."

n "Donde estoy ahora es bueno para mi nivel, pero con el fin de llegar al punto donde podré realmente conversar con Shizune, necesitaré más trabajo."

n "\nEstoy haciendo mi mejor esfuerzo para llegar a ese punto paso a paso, estudiando tanto como puedo durante el almuerzo."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear

nvl hide dissolve

window show

"Levanto la mirada de la “Introducción al Lenguaje de Señas Japonés” para revisar si Shizune o Misha están cerca."

"Por supuesto, ya que esto está ocupando mi hora de almuerzo, he tenido que evitarlas por unos cuantos días. Lo que es más, tendré que continuar haciéndolo si quiero evitar que Shizune se entere."

"De espaldas al rincón, explorando el área cada diez minutos, me siento como una especie de criminal intentando evadir la captura."

"…"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

nvl show dissolve

nvl clear

n "\n\nCada vez que puede, Misha me pregunta por qué quiero esconder de Shizune el hecho de que estoy aprendiendo lenguaje de señas."

n "Mirando hacia atrás, en realidad no había ninguna razón, pero ahora creo que lo sé."

n "Si quiero que Shizune pueda tratarme como un verdadero igual, el lenguaje de señas es un paso importante hacia esa meta."

n "Si quiero poder tratar a Shizune como una igual, entonces el lenguaje de señas es un paso importante hacia esa meta."

n "Otro paso importante es estar seguro de que ella no lo sepa, para que cuando finalmente podamos hablar en igualdad de condiciones, estaré completamente listo, capaz de hacerlo bien, no como algún diletante."

n "Cualquier cosa menos, creo, sería insultante. Ella lo vería de la misma manera."

n "\nAsí que para mí, esta es la única opción. Especialmente ahora que he decidido ser tan firme con ello."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear

nvl hide dissolve

window show

"Shizune tiene un aura enorme. Es muy fácil verla venir, o hasta sentirla venir. Más que nada porque el cabello de Misha ilumina cualquier multitud en la que ella esté como un faro, y puedes escucharla reír a un kilómetro de distancia."

"Aunque, incluso si Misha no estuviera con ella, sería lo mismo. Su franqueza y eficiencia son partes esenciales de ella, así que no es sorpresa que estas reluzcan en la forma en que camina también."

"Debido a todos esos factores, puedo guardar mis cosas y poner mi mejor cara casual mucho antes de que me vean y vengan hacia donde estoy."

show shizu behind_smile at tworight
show misha perky_smile at twoleft
with charaenter

hi "Hola."

show shizu adjust_smug
with charachange

ssh "Consejo estudiantiiil."

show misha hips_grin
with charachange

mi "¡Consejo estudiantil~!"


"“Consejo estudiantil” fue la primera cosa que pedí aprender; parecía que me sería útil."

hi "Sí, lo he estado evadiendo desde hace un tiempo, ¿eh?"

show misha sign_smile
show shizu behind_smile
with charachange

mi "¡Síp~!"

show shizu behind_smile_close at closeright
show misha perky_smile_close at closeleft
with characlose

show shizu behind_smile_close:
    ypos 1.07
show misha perky_smile_close:
    ypos 1.1
with charamove

stop music fadeout 3.0

"Shizune se sienta enfrente de mí, a mi derecha, y Misha a mi izquierda. Fue un error ubicarme en el rincón; ahora estoy, bueno, arrinconado."

scene bg school_lobby
with shorttimeskip

"Al final, soy arrastrado al salón del consejo estudiantil, pero no me importa. Estaba comenzando a extrañarlas un poco, de todos modos."

"En ciertos modos esto lo hace más fácil: satisfecha con haberme atrapado, Shizune no me pregunta dónde he estado todo este tiempo."

"Una vez que estoy frente a la puerta, me pregunto qué podría ser tan importante para que estén tan ansiosas de empujarme adentro."

scene bg school_council at bgright
with locationchange

hi "Juegos."

play music music_another fadein 0.5


"Hay más juegos que libros. Esto por fin explica por qué siempre que vengo aquí hay montones de libros apilados en todas las mesas y ocasionalmente en partes del piso: necesitan el espacio para poner todos estos juegos en alguna parte."

show misha cross_laugh
with charaenter

mi "¡Jajaja~!"

show misha hips_grin
with charachange

mi "Es aburrido jugar demasiado entre nosotras, Hicchan. Así que, es tu turno, ¿bueno? ¡Bien~! ¡Entonces está decidido~!"

hi "¡Ni siquiera dije nada!"

show shizu invis at right behind misha
with None

show misha hips_grin at twoleft
show bg school_council at center
show shizu basic_normal at tworight
with dissolvecharamove

show shizu behind_blank
with charachange

shi "…"

show misha sign_smile
with charachange

mi "Hicchan, este es uno de los últimos días en que podremos relajarnos así por un tiempo. Así que~, es especialmente importante que le saquemos el máximo provecho, ¿no lo crees?"

show misha cross_smile
with charachange

mi "La fiesta de Tanabata llegará pronto, y tendremos que aportar con mucho trabajo para eso, también."

show misha hips_grin
show shizu behind_smile
with charachange

mi "Así que, por ahora, ¡juega con nosotras~!"

"Ahora que lo pienso, es verdad. Ni siquiera lo había notado porque he estado tan absorto en querer aprender lenguaje de señas. Poco después de un festival, otro más grande aparece."

"Me pregunto si Shizune intentará atrapar a un par de nuevos miembros para ayudar con esto también."

hi "Tienes razón."

show misha cross_laugh
with charachange

mi "¡Jajaja~! ¡Viva~! ¡Hicchan está de acuerdo~! ¡Vamos a celebrar!"

show shizu basic_happy
with charachange

ssh "Ya sé, deberíamos jugar un juego."

show misha sign_smile
with charachange

mi "¡Vamos a jugar un juego para celebrar, Hicchan~!"

hi "No lo sé, ese tipo de cosas por lo general terminan mal para mí."

show misha perky_sad
with charachange

mi "Hicchan está preocupado por los riesgos~."

"Misha hace una cara muy decepcionada. Es difícil saber si ella se está burlando de mí, ya que sus expresiones son tan exageradas por defecto. Ella es el tipo de chica que “va con todo”."

"Giro mi cabeza hacia Shizune. Ahora, esta persona, definitivamente se está burlando de mí."

hi "Oigan, dejen eso. Pero, sí, jugaré con ustedes si me dicen primero qué está en juego."

show shizu adjust_smug
with charachange

shi "…"

show misha cross_grin
with charachange

mi "Qué japonés, poniendo las consecuencias sobre todo lo demás."

show misha sign_smile
with charachange


mi "Hicchan, ¿alguna vez has escuchado la expresión “Los árboles no dejan ver el bosque”?"

hi "No."

"Eso es mentira. Pero tengo mi orgullo, el cual en este momento se siente herido."

hi "Muy bien, jugaré, pero quiero elegir el juego."

show shizu adjust_happy
show misha perky_smile
with charachange

"Misha asiente."

hi "Además, elijo el castigo si pierdes."

show shizu cross_angry
with charachange

"Shizune hace una X con sus brazos. Eso o significa “denegado” o que está a punto de usar su ataque especial."

hi "Ajá, ¿ahora quién le teme a las consecuencias?"

show shizu behind_frown
with charachange

ssh "Qué vengativo, aún pensando tan rencorosamente por una bromita simpática."

show shizu basic_frown
with charachange

ssh "Si un … te mordiera, seguramente devolverías el mordisco."

"Shizune hace el gesto de una palabra que no capto muy bien."

show misha hips_frown
with charachange

mi "Hicchan es tan vengativo~, aunque era solo una bromita simpática. ¡Si un armadillo te mordiera, seguramente devolverías el mordisco!"

hi "¿Armadillo?"

show misha sign_smile
with charachange

mi "¡Es tonto devolverle el mordisco a un armadillo, Hicchan!"

show shizu behind_blank
with charachange

shi "…"

show misha cross_laugh
with charachange

mi "¡Pero Hicchan lo haría de todos modos! ¿Ves~? ¡Jajaja!"

hi "Ya veo."

show shizu adjust_smug
with charachange

"Shizune ajusta sus anteojos con un pequeño ademán ostentoso de su mano."

show shizu behind_smile
with charachange

shi "…"

show misha sign_smile
with charachange

mi "Hicchan, no teníamos nada planeado en absoluto si fueras a ganar o a perder, tú solo asumiste que habría algo así~."

hi "Me pregunto por qué."

show misha hips_grin
with charachange

mi "Hm~, ¡yo también~! Pero, ¡oh bueno~! No lo hay. ¿Eso cambia tu parecer, Hicchan?"

hi "Bueno… sí."

show misha hips_laugh
with charachange

"Misha mueve su brazo como un molino de viento a alta velocidad para mostrar su alegría. Un hábito extraño. Este es el tipo de cosas que solo podrías ver en el salón del consejo estudiantil, ocupado únicamente por tres personas."

"En cualquier otro lugar ella terminaría pegándole a alguien en la cara."

show misha hips_grin
with charachange

mi "¡Viva viva~! ¡Vamos a empezar ahora mismo!"

hi "Todavía no."

show misha hips_smile
with charachange

mi "…"

show shizu behind_blank
with charachange

shi "…"

mi "…"

shi "…"

hi "Está bien, está bien."

hi "Sin embargo, todos tenemos que poder jugar. Esa es mi condición."


hi "No me gustan los juegos en donde una persona es claramente el jugador estrella de buenas a primeras, o juegos donde solo dos personas pueden jugar y así uno de nosotros tiene que sentarse. Tiene que ser algo que los tres podamos jugar por igual."

show shizu basic_normal
with charachange

shi "…"

show misha sign_smile
with charachange

mi "¿Damas?"

"En el momento en que lo dice, Misha saca una bolsa de damas y las pone sobre la mesa."

hi "Solo dos personas pueden jugar eso. Les dije que—"

show misha hips_grin
with charachange

mi "¡Bueno bueno~! Hicchan, ¿qué tal… Monopoly?"

"Una caja de Monopoly se acerca lentamente hacia mí, y la quito de las manos de Misha y la pongo bajo mi silla."

hi "No me gustan los juegos que giran en torno a una cuestión de suerte; son demasiado sobre azar y no sobre habilidad. Además, ¡deja de precipitarte con estos juegos!"

show misha perky_confused
with charachange

mi "La suerte es como una habilidad, ¿sabes?"

hi "¡No, no lo es!"

show shizu adjust_smug
with charachange

shi "…"

show misha sign_smile
with charachange

mi "¡Puede serlo si estás constantemente con suerte~! ¿Cierto~?"

hi "Una vez en ese punto es algo completamente distinto."

show shizu adjust_happy
show misha hips_grin
with charachange

mi "Hm~, hm~ hm~ hm~~. ¿Bacará? ¿Canicas? ¿Life? ¿Serpientes y escaleras? ¿Ruleta? ¿Blackjack? ¿Futbol de mesa? ¿Trivial Pursuit?"

"Misha comienza a nombrar con entusiasmo un montón de juegos como si los estuviera leyendo de una lista. Con cada sugerencia, una nueva caja, tablero, y piezas aparecen a su alrededor."

"Un raro catálogo de juegos que van desde los dirigidos a niños hasta instrumentos de apuestas serios de aspecto pulido que se ven muy fuera de lugar en este humilde salón."

show misha sign_smile
with charachange

mi "¿Ajedrez de a tres?"

hi "¿Acaso es eso posible?"

show shizu behind_smile
with charachange

ssh "Vamos a intentarlo."

show misha cross_laugh
with charachange


mi "¡Sí sí~, intentémoslo, definitivamente~! ¡Ajajajaja~!"

show shizu basic_happy
show misha hips_grin
with charachange

"Ellas sacan un tablero de ajedrez de sus espaldas con un gesto exagerado como dos magas jóvenes. Bueno, la magia sí requiere una prestidigitación hábil, y ellas tienen de eso con creces."

"No estoy sorprendido. Sin embargo, todavía es de alguna manera inquietante."

hi "¡Dejen de hacer eso!"

stop music fadeout 2.0

ha "¿D-disculpen…?"

show shizu basic_normal
show misha perky_confused
with charachange

"Una voz muy tímida logra hacerme levantar la mirada."

show hanako invis at offscreenright
with None

show misha perky_confused at left
show shizu basic_normal at center
show bg school_council at bgleft
show hanako emb_downtimid:
    xanchor 0.7 xpos 1.0
with dissolvecharamove

ha "P-perdí mi credencial, y alguien me dijo… que aquí podría averiguar dónde conseguir una nueva. Si estoy interrumpiendo a-algo, puedo volver más tarde."

show hanako emb_timid
with charachange

"Los ojos de Hanako vagan por el salón, observando el paisaje de libros de registro apilados, sillas dispersas aleatoriamente, y juegos de mesa volcados."

"Supongo que esta no es exactamente la imagen que un consejo estudiantil organizado y bien administrado como el nuestro debería estar emitiendo."

hi "Hola."


"Es la única cosa en la que puedo pensar para romper el hielo. Desafortunadamente, solo parece asustarla más."

show hanako def_worry
with charachange

ha "…"

show hanako def_strain
with charachange

ha "Ah…{w=0.5} mi credencial…{w=0.5} yo…"

show misha sign_smile
with charachange

mi "Estás en nuestra clase, no es así, ¿cierto? ¡Cierto~! ¡Entonces~! No seas tan tímida, ¿bueno? ¡Vamos!"

show shizu behind_smile
with charachange

shi "…"

show misha hips_grin
with charachange

mi "Síp, aunque somos tus mayores, ¡no es que vayamos a morder!"

hi "No somos sus mayores, estamos en la misma clase."

play music music_happiness fadein 3.0

"Aun así, estoy agradecido con ellas por intervenir."

show misha hips_smile
with charachange

mi "¿Qué es lo que dijiste que quieres? ¿Una credencial~? ¡Cierto~!"

show hanako basic_distant
with charachange

ha "Sí."

"Sus ojos se apartan de Misha. Siendo tímida, no sorprende que ella no sea la mejor en mantener contacto visual. Sigo hacia donde ella está mirando, y noto que su mirada se detiene en el tablero de ajedrez sobre la mesa."

show hanako basic_normal
with charachange

show hanako basic_distant
with charachange

"Los ojos de Hanako se abren de par en par, solo por un momento. Shizune lo nota también."

show shizu basic_happy
with charachange

shi "…"

show misha perky_smile
with charachange

mi "¿Te gusta el ajedrez?"

show hanako defarms_strain
with charachange

ha "¿¡Eh!?"

show shizu adjust_smug
with charachange

shi "¡…!"

show misha hips_smile
with charachange

mi "Te gusta el ajedrez, ¿cierto~? ¡Sí, te gusta, sin duda~!"

show misha hips_grin
show shizu adjust_happy
with charachange

mi "¿Qui~{w=0.2}e~{w=0.2}res~{w=0.2} ju~{w=0.2}gar~?"

"Vacilación. Ella podría tratar de escaparse. Me niego a involucrarme en esto; no terminará bien."

show hanako basic_normal
with charachange

"Para mi asombro, Hanako parece estar considerando la idea muy seriamente. Ella se toca las puntas de sus dedos pensativamente, dándole vueltas a la idea."

"Ese nivel de consideración es más o menos una confirmación."

show misha sign_smile
with charachange

mi "Vamos a tomar un descanso para almorzar, así que tendrás que esperar de todos modos. ¿Por qué no juegas con nosotros mientras tanto~? ¡Vamos, será divertido, muy divertido~!"

mi "Te gusta el ajedrez, ¿no? Puedo darme cuenta, en serio, en serio, es obvio, ¡así que~! Por favor~, ¿quieres?"

show hanako cover_distant
with charachange

ha "Bueno…"

show misha cross_laugh
with charachange

mi "¡Guajaja~! ¡Viva~! ¡Éxito, éxito, bien bien bien~! ¡Eso es genial~!"

scene ev shizu_chess_large:
    subpixel True xanchor 1140 yanchor 1100 xpos 400 ypos 300 zoom 1.0
    easein 10.0 yanchor 1050
with flash



"El tablero de ajedrez es montado."

"La jugada inicial es importante."

show ev shizu_chess_large:
    ease 1.0 xpos 400 xanchor 1400 yanchor 400 ypos 300
    acdc_warp 10.0 xanchor 1300

"Sin embargo, a Shizune no parece importarle."

show ev shizu_chess_large:
    ease 0.5 xanchor 800 yanchor 360
    easein 10.0 xanchor 700 yanchor 360

"Hanako considera sus movimientos con cuidado, deslizando las piezas hacia adelante solo un poco, luego regresándolas con incertidumbre, corrigiéndose a sí misma una y otra vez."

"Ella está realmente metida en este juego; no puedes llamarla una jugadora casual. Definitivamente una entusiasta."

"Shizune no puede tomársela a la ligera; no importa lo que ella haga, Hanako tiene una respuesta apropiada."

"Pero hay algo que anda mal con el ritmo de este juego."

scene ev shizu_chess_base:
    truecenter subpixel True zoom 1.05
    easein 5.0 zoom 1.0
with flash

"Shizune mueve muy rápido. No, ni siquiera muy rápido, sino con una velocidad ilógica. Es como si ni siquiera estuviera pensando en lo que hará a continuación."

"O Shizune está en el ámbito de los supercomputadores, o no se está tomando este juego muy en serio."

"O tal vez Hanako simplemente no es muy buena."

scene ev shizu_chess_base
show sc_shiz normal:
    xalign 1.0 yalign 0.0
with charachange

"Shizune obliga a un cambio de peones."

scene ev shizu_chess_base3
with charachange

"Los turnos de Hanako toman cada vez más tiempo mientras el juego avanza, y ni siquiera ha pasado tanto."

"De repente todo se vuelve claro: Shizune tiene mucho más tiempo para pensar en su próxima jugada porque Hanako se toma una eternidad en mover una pieza."

"A pesar de eso, es un juego interesante."

window hide

nvl clear

$ renpy.music.set_volume(0.5, 1.0, channel="music")

nvl show dissolve

n "\n\nCaballo negro a f6."

n "Alfil a d3."

n "Dado que las dos están jugando en serio, ninguna está jugueteando con la otra. No hay un jugador claramente dominante, al menos por ahora. Tal vez esto es ayudado por el hecho de que ellas no son muy cercanas entre sí, por lo que puedo ver."

n "Shizune es una oponente misteriosa para Hanako, y Hanako es un enigma para Shizune. El ceño fruncido de Hanako muestra que está metida en el juego. Ella realmente quiere ganar, y Shizune siempre quiere ganar."

n "Su falta de familiaridad es un poco deprimente, pero le está dando vida al juego, y permitiéndoles verse entre sí como una buena competencia."

n "Tal vez puedan hasta terminar siendo amigas con esto, o por lo menos, rivales en el ajedrez. Es un pensamiento optimista."

n "Aunque al recordar el juego de Risk contra Shizune, ella no quiere aplastar a la gente simplemente por el gusto de hacerlo."

nvl clear

n "\n\n\nEl juego continúa."

n "Shizune hace doce movimientos en cuatro minutos. Qué oponente tan aterradora."

n "Pero Hanako se defiende, aunque su rey está siendo bastante perseguido por el tablero."

n "Peón a h6."

n "Caballo blanco a e6."

n "El fin está cerca."

n "\n\n…"

stop music fadeout 3.0

n "El juego termina."

nvl clear

nvl hide dissolve

scene bg school_council
show shizu adjust_happy at center
show misha perky_smile at left
show hanako basic_normal at right
with locationchange

window show

shi "…"

show misha sign_smile
with charachange

mi "¡Ese fue un juego muy bueno~!"

$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_ease fadein 5.0

show hanako cover_bashful
with charachange

ha "G-gracias…"

show shizu behind_smile
with charachange

shi "…"

show misha hips_smile
with charachange

mi "Estuvo muy cerca~, pensé que iba a perder. Eres muy hábil."

"Magnánima en la victoria, y extendiendo una mano a la derrotada. Tal vez es porque Hanako está tomando su derrota muy bien."

show shizu basic_normal
with charachange

shi "…"

show misha perky_smile
with charachange


mi "Este es un juego divertido, pero tomó mucho tiempo. ¡Casi toda la hora!"

mi "El ajedrez es muy formulista, especialmente a este nivel. ¿Qué tal algunas reglas avanzadas~?"

hi "¿Qué?"

show hanako cover_worry
with charachange

ha "¿A… vanzadas…?"

show shizu basic_sparkle
with charachange

show shizu adjust_smug
with charachange

show shizu basic_happy
with charachange

shi "… … …"

show misha hips_smile
with charachange

mi "¡Sí, sí~! Como ajedrez rápido, o ajedrez con piezas adicionales, o tal vez podemos formar parejas y jugar ajedrez por equipos, con uno o dos tableros, ¡tú eliges!"

mi "¡Vamos vamos vamos vamos, será divertido, en serio, en serio~! El ajedrez regular es tan lento, muy metódico, es aburrido."

show misha hips_grin
with charachange

mi "¡Quiero jugar un ajedrez que premie el pensamiento rápido, y la audacia! Cualquiera de estos, comparando el ajedrez con eso es como comparar damas con go, o tres en raya con shogi, ¿cierto? ¡Cierto~!"

show misha cross_laugh
with charachange

mi "¡Guajajaja~! ¡Incluso el ajedrez láser podría ser más emocionante, elige algo, elige~!"

show hanako defarms_strain
with charachange

ha "Aaaah…"

"Como un ciervo en los faros. Muchas emociones surgen en mí, mirando la mente de Hanako tambalearse enfrente del tablero de ajedrez como si estuviera a punto de desmayarse."

"La que domina es la diversión, pero me acerco un poco en caso de que realmente pueda caerse."

scene ev shizu_chess_base2:
    truecenter subpixel True zoom 1.05
    easein 5.0 zoom 1.0
with flash

"El tablero es montado de nuevo, pero esta vez, no es ni parecido."


"Hanako ni siquiera puede hacer un movimiento por miedo a chocar su mano con la de Shizune. Ella está en todo el tablero. Es un ataque sin cuartel. Donde sea que Hanako quiera poner una pieza, Shizune ya está ahí."

"Es el juego más rápido que he visto en mi vida."

scene bg school_council
show shizu basic_sparkle at center
show misha hips_grin at left
show hanako defarms_strain at right
with locationchange

mi "¡Vamos a cambiar las reglas y juguemos de nuevo~! ¡Al mejor de seis, como Kasparov y Deep Blue~!"

hide hanako
with easeoutright

"Hanako se disculpa y huye del salón."

show shizu basic_normal
show misha perky_confused
with dissolve

mi "¿Eh? ¡Espera!"

hide misha
with charaexit

mi "Ah, ¿ella no quería saber dónde podía conseguir una nueva credencial? ¡Disculpa! ¿Hola~? ¡Regresa, por favor! ¡Espera, espera~! ¡Espera~!"

stop music fadeout 3.0

"Extrañamente, entre más se aleja Misha, más fuerte parece ser el volumen de su voz."

show bg school_council at bgright
show shizu basic_normal at tworight
with charamove

show misha perky_sad at twoleft
with charaenter

mi "No pude alcanzarla~…"

show shizu adjust_happy
with charachange

play music music_normal fadein 3.0

shi "…"

"Shizune le da una palmadita en su hombro para tranquilizarla."

hi "Vamos, vamos."

show misha hips_smile
with charachange

mi "¡Vamos, vamos~!"

hi "Estás muy alegre como para ser alguien que necesitaba una palmadita en el hombro."

show misha cross_laugh
with charachange

mi "¡Ajajaja~!"

"…"

show shizu basic_normal2
with charachange

shi "…"

show misha sign_smile
with charachange

mi "Hicchan, ¿odias los juegos en donde está involucrada la suerte?"

"Una pregunta de la nada, pero que se siente como una importante."

"Si no lo fuera, ¿por qué Shizune estaría mirándome, observando mi reacción? Mientras miro en su dirección, ella intenta fingir que no lo está haciendo, simulando un aire casual al hacer girar una pieza de ajedrez en sus dedos."

show misha hips_grin
with charachange

mi "“No me gustan los juegos que giran en torno a una cuestión de suerte”, ¿cierto? Ese eras tú, Hicchan~."

hi "Sí. Aunque girar en torno a la suerte no es lo mismo que simplemente tener suerte involucrada."

hi "No odio los juegos solo por tener un elemento de suerte. La mayoría de los juegos tienen en ellos un elemento de suerte, de todos modos. Es lo que los hace interesantes."

hi "Creo que un juego donde se sabe desde el principio qué tan lejos puedes llegar es aburrido. Entonces no es un juego, ¿no es así? Solo son movimientos mecanizados."

hi "Para un juego donde tienes de poco a ningún control, no creo que pudiera meterme en algo así."

show shizu behind_smile
with charachange

ssh "Ya veo."

show shizu adjust_smug
with charachange

shi "…"

show misha hips_smile
with charachange

mi "Esa chica no es muy buena en el ajedrez."

show shizu basic_normal
with charachange

shi "…"

show misha sign_smile
with charachange

mi "El ajedrez es un juego formulista. ¡Así que~! Es un juego que no es apto para ella… No había nada formulista en ella."

mi "Alguien que juega ajedrez así, mirando solamente la pieza siguiente, jugando tan superficialmente, no puede ser llamada una jugadora seria de ajedrez."

show misha perky_smile
with charachange

mi "Cualquiera que ame el ajedrez al punto donde sus ojos brillan así cuando ven un tablero de ajedrez, sería el tipo de persona que estudiaría el juego."

mi "Si lo estudias casualmente, puedes aprender a ver por lo menos dos movimientos con anticipación, incluso contra profesionales."

show misha hips_frown
with charachange

mi "¿Por qué alguien que ama tanto el juego… con ese entusiasmo… sabría tan poco de él? ¿Incluso menos que alguien con un interés pasajero en él?"

"Shizune baja la pieza en su mano. Es una torre."

show shizu behind_frown
with charachange

shi "…"

show misha hips_smile
with charachange

mi "Sus sentimientos son reales, pero sus sentimientos por el juego no son reales. ¿Entiendes, Hicchan~?"

show misha perky_smile
with charachange

mi "¡No hay suerte en el ajedrez~! Es muy importante darse cuenta de eso. La suerte en los juegos es buena porque le da a todos una oportunidad. Solo suficiente para que importe, pero no tanta como para que la habilidad sea penalizada."

mi "El ajedrez es aburrido porque no es un juego; para mí, parecen fórmulas."

show misha sign_smile
with charachange

mi "Hanako tampoco es el tipo de persona que amaría algo así~."

show shizu adjust_angry
with charachange

shi "…"

show misha cross_frown
with charachange

mi "Si valoras algo, luchas. La lucha es la prueba de cuán prec— ¿preciado es? Eso creo, al menos. ¡O~! ¡Cedes de inmediato~! Dado que es tan preciado que te impide pensar. El primero es un amor apasionado. El segundo es un amor tierno."

show shizu basic_normal2
with charachange

shi "…"

show misha hips_smile
with charachange

mi "Traté de luchar contra ella, persiguiendo su rey, e intentando hacerla caer. Aunque no tuve éxito, porque ella se apegó solamente a lo que funcionaba."

mi "Los momentos más difíciles fueron cuando ella movía más rápido. Eso significa que ella sabía exactamente cómo lidiar en esas situaciones."

show misha sign_smile
with charachange

mi "Eso significa que alguien le enseñó. ¿Entiendes, Hicchan~?"

hi "No realmente."

show shizu adjust_happy
with charachange

shi "…"

show misha hips_grin
with charachange

mi "Si amas tanto el ajedrez, pero no puedes darlo todo, es porque amas los recuerdos unidos a él y no al juego en sí; es tan preciado para ella como para verlo como una herramienta para una verdadera competencia."

show shizu behind_blank
with charachange

shi "…"

show misha perky_smile
with charachange

mi "Debido a eso, no puedes hacerte amigos con ello. No sin palabras."

stop music fadeout 5.0

"Bueno, tu manera de hacer amigos no es el tipo de manera que funciona con todo el mundo, Shizune."

"La mirada en su cara no es de tristeza, por lo menos hasta donde puedo notar, pero sus palabras son muy tristes."

hi "Oigan, vamos a jugar un juego."

hi "Mientras el tablero aún está aquí."

play sound sfx_warningbell

"Pero la campana suena y me interrumpe."

scene black
with dissolve

$ suppress_window_after_timeskip = True


label es_S12:

window hide None

scene bg school_council
with locationchange

nvl clear

nvl show dissolve

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_daily fadein 0.5

n "\nLas cosas han vuelto a la normalidad. Bueno, fui transferido en un momento muy inusual, y difícilmente puedo decir que tuve unas primeras semanas normales aquí. Supongo que es más que las cosas se han calmado, y alcanzado la normalidad."

n "He estado aquí más tiempo del que pensé."

n "Es difícil no pensar en todas las cosas que debí haberme perdido en esta escuela antes de mi llegada, o en las cosas que pudieron haber pasado en mi vieja escuela desde que me fui."

n "Me pregunto de dónde vienen estos sentimientos, ya que no dejé mucho atrás."

n "Tengo mucho más aquí de lo que me gusta. Si ese no fuera el caso, entonces ni siquiera me molestaría con algo como el consejo estudiantil, o Shizune y Misha. Me costaría trabajo que algo me importara, si esta escuela fuera como me imaginé que sería."

n "Así que incluso esta sensación de una rutina diaria me alegra, en cierta forma."

n "Le tengo terror a la cantidad de trabajo que va a golpearme en el consejo estudiantil después de la escuela, lo suficiente para querer considerar abandonar mis deberes, solo por esta vez. Sin embargo, es bueno sentir que hay algo que puedo hacer."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

window show

show shizu basic_normal
with charaenter

"Shizune deja caer un montón de hojas de asistencia a mi lado."

show shizu adjust_happy
with charachange

ssh "Gracias de nuevo por ayudarnos."


show shizu adjust_happy at tworight
show bg school_council at bgright
with charamove

show misha hips_grin at twoleft
with charaenter

mi "¡Gracias de nuevo, Hicchan~!"

"Aunque sí es mucho trabajo. Tuve que saltarme de nuevo las clases de lenguaje de señas, pero ahora estoy en un nivel donde puedo entender la mayoría de las conversaciones que tienen Shizune y Misha, así que no me molesto mucho por ello."

"Sin embargo, Shizune aún no lo sabe. Estoy decidido a mantener las cosas así hasta que esté muy seguro de mis habilidades. Quizás es un poco infantil de mi parte."

show shizu behind_frown
with charachange

ssh "Tanabata es en menos de cinco días, pero solo van a comenzar a construir los puestos mañana."

show misha sign_smile
with charachange

mi "Hicchan, puede que nuevamente tengamos que ayudar con la construcción de los puestos desde mañana."

hi "¿Por qué? ¿Entonces cuál fue el propósito de desarmarlos? Eso tomó días, ¿no?"

show misha hips_grin
with charachange

mi "¡Síp! ¡Así es~! A pesar de que Hicchan no estuvo aquí para eso~."

hi "Habría ayudado si lo hubieran pedido."

show shizu basic_normal
with charachange

ssh "No habría tenido sentido aburrirte con los deberes de limpieza después de que disfrutaras tanto del festival."

show misha hips_smile
with charachange

mi "No habría tenido sentido aburrirte con hacerte limpiar justo después del festival, habría arruinado la diversión."

show shizu behind_smile
with charachange

ssh "Además…"

show misha hips_grin
with charachange

mi "¡Ajajaja~! Hicchan es perezoso de todos modos, ¡habrías intentado huir de nuevo~! A Shicchan no le gusta jugar al perro zorrero."

hi "Eso duele."

show shizu adjust_smug
with charachange

"Shizune se cubre la boca con su mano y comienza a temblar. Me toma un segundo darme cuenta de que se está riendo, más que todo porque lo está haciendo sin sonido alguno."

"Es un poco extraño de ver, pero es más o menos el mismo tipo de ánimo que Misha, sin romper los tímpanos."

show misha sign_smile
show shizu adjust_happy
with charachange

mi "Hm~, aunque esa es una buena pregunta, Hicchan."

hi "¿Eh?"

show misha hips_grin
with charachange

mi "¡Los puestos~!"

show shizu basic_normal2
with charachange

ssh "Es un problema de almacenaje. La escuela no tiene un lugar donde guardar tantos puestos, ya que cada uno es bastante grande. Ellos tampoco pagarán por almacenaje externo, así que esto fue lo que decidieron. Es ineficiente, pero más barato."

show misha sign_smile
with charachange

mi "¡Porque~! La escuela no tiene un lugar donde guardar tantos puestos, Hicchan."

show shizu behind_frown
with charachange

shi "…"

show misha perky_confused
with charachange

mi "Ah, sí sí~, cierto, sí lo tienen, ¡pero no quieren pagar~! Lo siento, Shicchan~…"

show shizu basic_normal2
with charachange

ssh "Es debido a la generación anterior."

show shizu behind_frustrated
with charachange

ssh "La dirigencia decidió que los costos de almacenaje externo habían subido mucho, y el anterior consejo estudiantil tenía muy poca fuerza de voluntad para decirles que es estúpido tener que construir y desmontar sesenta puestos dos veces cada año."

show shizu adjust_angry
with charachange

shi "¡…!"

show misha cross_grin
with charachange

mi "¡¡Muy bien~!!"

show shizu behind_smile
with charachange

shi "…"

show misha perky_smile
with charachange

mi "¡Hicchan, vamos a comer algo~! Se siente como si hubiéramos estado trabajando todo el día~…"

hi "Estuvimos trabajando. Ahora que lo pienso, tengo hambre. Habría almorzado, pero por alguna razón había mucha gente hoy, así que decidí que no valía la pena."

show misha cross_laugh
with charachange

mi "¡Ajajaja~! Hoy estaba así porque adicionalmente tenían unas cosas especialmente interesantes a la venta."

hi "¿Como qué? No, no me digas. Supongo que no importa, ya que de todos modos no podré comerlas."

show shizu adjust_smug
show misha hips_grin
with charachange

"Shizune se ve extrañamente complacida consigo misma. Me pregunto cuál podría ser el contexto de eso."

show shizu behind_smile
with charachange

ssh "Me preparé con tiempo para esto."

"Radiante de satisfacción consigo misma, ella saca una amplia variedad de comida de su mochila. Inmediatamente puedo ver que el noventa por ciento de la misma o más fue sacada del salón de almuerzos."

stop music fadeout 5.0

"Hay mucha, también. ¿No hay un límite en la cantidad que una persona puede comprar?"

"Eso significa que definitivamente estos beneficios son mal habidos."

hi "El pan de chuleta de ternera siempre se acaba en el primer minuto del almuerzo. Estoy impresionado de que pudieras conseguir uno."

hi "Gracias."

show misha perky_smile
show shizu basic_sparkle
with charachange

"Lo alcanzo rápidamente, pero Shizune inmediatamente trata de agarrarlo también."

play music music_another fadein 0.5

show shizu basic_happy_close
with characlose

"Su mano se afloja por un segundo cuando toca la mía, pero ella inmediatamente avanza con esfuerzo redoblado, ese espíritu ardiente y competitivo destellando peligrosamente en sus ojos. Sus dedos fisgonean los míos, buscando una apertura."

"No cedo un centímetro, preparado para pelear por este pan con mi vida. Puede que nunca tenga otra oportunidad para comer esto."

"Estoy completamente consciente de que si continuamos así, podríamos aplastar el pan, reduciendo enormemente su comestibilidad."

hi "Misha… Dile que a menos que ella lo suelte, el pan va a ser aplastado."

show misha perky_confused
with charachange

mi "¿Hmmmmm? ¿Por qué no puedes hacerlo tú mismo?"

"Estoy sorprendido de que ella pueda tan tranquilamente dejar escapar que yo podría comunicarme sin problemas con Shizune si lo quisiera."

"Casi considero la posibilidad de que fuese intencional, pero estoy seguro de que ella solo estaba distraída intentando rasgar la envoltura de la pajilla de una caja de jugo."

hi "¿No es obvio? No puedo soltar el pan."

show misha sign_smile
with charachange

mi "Entonces, no puedo decirle eso a Shicchan."

show misha hips_grin
with charachange

"Ella pone sus palmas hacia el cielo y se encoge de hombros, con una amplia sonrisa en su rostro."

hi "¿Por qué no?"

show misha sign_smile
with charachange

mi "¡Porque~! Tú tienes un interés en esto, ¡así que no puedo confiar en ti~! Si Shicchan quiere responder, tiene que soltar el pan, y entonces tú ganas. Quién sabe, quién sabe, ¿tal vez eso es lo que quieres, Hicchan?"

show misha cross_smile
with charachange

mi "¡No sería justo, así que voy a ser neutral! ¡Como Suiza~!"

hi "¿Suiza?"

show misha perky_smile
with charachange

mi "¿Sabes de Suiza?"

hi "Por supuesto que sí… es neutral, son neutrales."

show shizu basic_sparkle_close
with charachange

"Shizune me mira engreídamente, sacando ligeramente la punta de la lengua de entre sus dientes mientras continúa tirando firmemente del pan de chuleta de ternera entre nosotros."

show shizu adjust_happy
with charadistant

"De repente, ella lo suelta y levanta las manos, con las palmas hacia afuera. El gesto universal de paz."

show shizu behind_blank
with charadistant

ssh "Esta parece una mala manera de resolver esto, ¿no es así? Y puede que aplastemos el pan."

show shizu behind_frown
with charadistant

"Ella mira ferozmente, y su expresión pasiva rápidamente cae en una mueca de desaprobación."

show shizu adjust_angry
with charadistant

shi "¡…!"

show misha hips_frown
with charachange

mi "¡Hicchan! ¡Suelta el pan! ¡Estamos negociando ahora!"

"Suelto el pan a regañadientes."

show misha perky_smile
show shizu behind_blank
with charachange

"La mano de Misha entra como una flecha desde el lado, sus dedos tamborileando sobre la mesa mientras se abre paso."

show misha hips_grin_close
with characlose

mi "¡Ah~! ¡Jaja~! No se preocupen por mí, en realidad ni siquiera me gusta la ternera. ¡Solo tomaré este emparedado de aquí~! Y algo para tomar, también…"

show misha perky_smile
with charadistant

"Tomándolos con cuidado, ella se retira inmediatamente."

"Ella tiene la idea correcta. Simplemente podría elegir algo más, hay muchas cosas deliciosas aquí. El pan de katsudon de pollo también es popular en ventas, de alto rango en gusto y demanda. Pero ya he comido uno antes."

show shizu basic_angry
with charachange

ssh "Eres tan inmaduro, Hisao. Esto no sería un problema si eligieras algo más. El pan de katsudon de pollo es delicioso."

show misha hips_smile
with charadistant

mi "Eres tan inmaduro, Hicchan. ¿Por qué no eliges el pan de katsudon de pollo? ¡Es delicioso~!"

hi "Pero ya he comido eso."

show shizu behind_frown
with charachange

shi "…"

show misha hips_frown
with charachange

mi "¡Hicchan~! ¿Por qué estás tan obsesionado con comer el pan de chuleta de ternera, es-pe-cí-fi-ca-men-te?"

hi "Normalmente es difícil de conseguir. Las cosas raras son más deliciosas."

show shizu basic_frown
with charachange

ssh "Estás actuando como un niño."

show misha cross_frown
with charachange

mi "Estás actuando como un niño, Hicchan."

hi "¿Por qué tú no te comes el pan de pollo?"

show shizu adjust_blush
with charachange

ssh "Eso no es importante."

"Sonrojándose, sonríe astutamente y continúa."

stop music fadeout 6.0

show shizu basic_happy
show misha perky_smile
with charachange

ssh "No hay manera de razonar contigo. Así que parece que hay solo una manera de resolver esto: vamos a jugar por él."

show misha sign_smile
with charachange

mi "Eso no importa: ¡jugaremos por él~!"

"De alguna manera, esperaba esto. Es la conclusión lógica."

"Shizune ha estado estudiando por mucho tiempo, de manera continua hasta ahora. Con nuestros exámenes finales terminados, supongo que el excedente de energía tiene que ir a alguna parte."

hi "¿Jugar qué?"

hide misha
with None
show misha perky_smile behind shizu at twoleft
with None

show shizu behind_blank_close
with characlose

ssh "El juego más antiguo conocido por el hombre, sobre el cual se ha conocido que descansa el destino de naciones: Piedra, Papel o Tijera."

show misha sign_smile
with charachange

mi "Jugaremos Piedra, Papel o Tijera."

show misha perky_confused
with charachange

mi "¿De verdad? Eso suena muy serio, Shicchan…"

play music music_shizune fadein 1.0

"No hay humor en su expresión, ella está decidida en esto."

hi "Muy bien, muy bien."

show shizu adjust_happy_close
with charachange

"Ella retira su mano, y yo le copio el gesto."

hi "¡Ya!"

show shizu basic_angry_close
with charachange

"Ambos sacamos piedra. Un empate. Había pensado que tenía el plan perfecto. La piedra es invencible. Shizune frunce el ceño, profundamente molesta por este inesperado giro de eventos. ¿No salió según lo planeado?"

show shizu adjust_angry_close
with charachange

ssh "¡Otra vez!"

show shizu basic_frown_close
with charachange

"Dos papeles."

hi "Maldición."

show shizu adjust_angry_close
with charachange

ssh "¡¡Otra vez!!"

show shizu basic_frown_close
with charachange

"Ambos tiramos dos piedras otra vez, pero una tercera mano está entre nosotros representando tijeras."

show misha hips_grin
with charachange

mi "Esto se ve divertido, ¿puedo jugar?"

show misha cross_laugh
with charachange

mi "¡Jajajaja~!"

show shizu behind_frown_close
with charachange

ssh "… … …"

show misha perky_smile
with charachange

mi "¿Es un duelo, Shicchan?"

show shizu adjust_angry_close
with charachange

shi "…"

show misha sign_confused
with charachange

mi "Eh~, ¿conducta de duelo? Hm~… ¡Tienes razón, tienes razón~! Realmente no lo sé…"

show shizu cross_angry_close
with charachange

shi "…"

show misha perky_confused
with charachange

"Entre más rápido ella hace señas, más difícil es seguirlas. De hecho, parece que hasta Misha está teniendo problemas para mantener el ritmo."

hi "¿De qué está hablando?"

show shizu adjust_angry_close
with charachange

ssh "¡Una vez más!"

show shizu basic_frown_close
with charachange

"Empatamos de nuevo. Cada vez, Shizune exige una revancha, finalmente saltándose ese paso por completo y tirando piedra, papel o tijeras con un desenfreno cada vez más temerario."

"Incluso jugando completamente al azar, seguimos empatando. Esto es casi imposible matemáticamente."

stop music fadeout 8.0

show misha hips_grin
with charachange

"Misha se cierne sobre nosotros, mirándolo todo y riendo cada vez que empatamos. Después de dieciséis rondas, Shizune aleja su silla de la mesa y se levanta."

show shizu behind_blank_close
with charachange

shi "¡…!"

show misha hips_smile
with charachange

mi "¡Suficiente con esto, Hicchan~! Ya veo lo que he estado haciendo mal, todo esto terminará en la próxima ronda, así que prepárate, ¿bueno~? ¡Bueno~!"

show misha sign_smile
with charachange

mi "He estudiado tus procesos de pensamiento y~ veo cómo juegas. Voy a anticipar tu próxima jugada y la combatiré hábilmente."

"Esto es una novedad para mí, ya que no puedo recordar por qué estamos haciendo esto."

show shizu adjust_happy_close
with charachange

"Shizune sonríe con confianza, con una mirada atrevida y valiente en su rostro. Sus ojos fríos brillan con un espíritu competitivo puro mientras retira su mano, incitándome sin palabras a hacer lo mismo."

"Su forma es increíble, como una jugadora de bolos profesional o algo así, solo para lanzar un movimiento con la mano."

show shizu basic_happy_close
with charachange

"Dos papeles."

play music music_comedy

show shizu cross_stunned_close
with charachange


"El cuerpo de Shizune se afloja de inmediato, y ella se frota las sienes con una mirada de exasperación mientras deja salir un suspiro tan largo que suena como un neumático desinflado."

"Me doy cuenta de que quedé más hambriento en el rato que hemos estado haciendo esto."

hi "Podemos simplemente partirlo."

show shizu behind_blank_close
with charachange

"Rompo el pan por la mitad y le ofrezco una mitad a Shizune. Ella lo toma."

show shizu adjust_happy_close
with charachange

ssh "Gracias."

"Ella mira el pan en su mano, estudiándolo."

show shizu basic_normal2_close
with charachange

ssh "Pero, de alguna manera, esto se siente vacío."

show shizu basic_normal2_close
with charachange

"Sin importar cómo se siente, ella aun así lo come."

"De repente, veo a Misha observando la escena con el rabillo de mi ojo."

show misha hips_grin
with charachange

mi "Hicchan~… Eso fue muy romántico, creo."

hi "Oh, por favor."

show misha cross_laugh
with charachange

mi "¡Guajajajajaja~!"

show misha hips_smile
with charachange

stop music fadeout 5.0

"Ella ríe y toma un bocado de su segundo emparedado."

"Comemos en silencio por un rato, Shizune y yo logrando evitar cualquier otro concurso. Y entonces, regresamos a trabajar."

scene bg school_council_ss
with shorttimeskip

play music music_tranquil fadein 3.0

"Mientras termino la típica clasificación de documentos del día, pienso para mí mismo que esta podría ser la manera de Shizune de intentar comenzar la semana por todo lo alto."

"Después de todo, mañana es cuando comenzará el trabajo de verdad, y con sus manos literalmente llenas construyendo puestos, ella no podrá “hablar” mucho."

"Probablemente será muy aburrido y agotador, como lo fue la primera vez. En ese caso, estoy agradecido por su esfuerzo. Es bueno tener días como este, como una manera de pasarla bien antes de los días venideros. Creo que esa también fue su idea."

"… También recuerdo que todavía tengo que deshacerme del paquete de Kenji. La maldita cosa es voluminosa, y de alguna manera nunca he podido ubicarlo desde que lo recogí."

scene bg school_lobby_ss
with locationchange

"Después de que el consejo estudiantil se aplazara por el día, camino hacia las máquinas expendedoras para buscar algo para beber, separándome de Shizune y Misha."

"Es un viaje corto, pero incluso después de algunos segundos comienzo a tener el sentimiento de que no estoy solo."

scene black
with hands_in

"Un par de manos cubren mis ojos."

mi "¡Adivina quién~!"

hi "¿Shizune?"

mi "¡Guajajaja~! ¡Soy yo, Hicchan~!"

hi "Sí, lo sé."

scene bg school_lobby_ss
with hands_out

with Pause(0.3)

show misha hips_frown_close_ss at Slide(0.3, 0.5, 0.5, 0.5, 1.0)
with Dissolve(1.0)

mi "¿Entonces por qué dijiste que era Shicchan~? ¡Está bien equivocarse a veces, Hicchan~! Eres muy orgulloso."

show misha sign_smile_close_ss at center
with charachange

mi "De todos modos~, después del consejo estudiantil, no sueles tener ningún plan, ¿cierto~? Así que, ¿vas a ir directamente a tu habitación?"

hi "¿A dónde más iría?"

show misha hips_grin_close_ss
with charachange

mi "¡Bien, eso es genial~! ¡Eso es genial, Hicchan~! Quería hablar contigo hoy, ¡así que esto resulta perfecto!"

"Dos estudiantes de preparatoria, solos después de clases en un edificio tranquilo y vacío. Mientras el sol tiñe el cielo con un romántico color ámbar, la chica linda dice que quiere hablar."

"Qué situación tan reservada y atractiva, mi imaginación es un hervidero. Probablemente no va a ser ni de cerca tan emocionante como lo estoy imaginando, pero es divertido jugar de esa manera."

play sound sfx_can
show misha perky_confused_close_ss
with Dissolve(0.2)

"El chasquido al destapar mi café enlatado destruye toda oportunidad de mantener un humor tan cursi, sonando más fuerte de lo que habría pensado alguna vez imaginable, amplificado por el contexto de la situación. Suspiro de decepción y alivio."

hi "Entonces, ¿qué ocurre?"

show misha perky_smile_close_ss
with charachange

mi "¿Hm? ¡Oh! En realidad~… Estoy un poco atrasada en algunas de mis clases, y si no me pongo al día, ¡podría ser un problema~! No puedo aplazarlo por más tiempo."

show misha perky_sad_close_ss
with charachange

mi "Mis maestros dicen que tengo que comenzar a tomarme las cosas realmente en serio, así que debería escuchar, especialmente~ porque esta es la tercera vez."

mi "¡Lo siento~! Lo siento, Hicchan."

hi "¿Por qué te disculpas?"

show misha sign_sad_close_ss
with charachange

mi "No podré ayudarles a ti ni a Shicchan con el consejo estudiantil por unos días~. Solo será por dos o tres días, ¡en serio! ¡Sin duda intentaré regresar lo más pronto posible! Pero~…"

"No puedo decir que estoy feliz por esto. Se supone que esta semana también va a ser muy atareada, ¿cierto? Ese es un momento inoportuno. Por un segundo quiero preguntar si tal vez Shizune podría mover algunos hilos para librarla de eso."

"Pero Misha se ve tan genuinamente apenada al respecto. Sería muy insensible de mi parte decir algo así."

"Además, si ella dice que es algo que no puede aplazarse por más tiempo, estoy inclinado a creerle, considerando lo sorprendentemente seria que puede ser con los deberes del consejo estudiantil."

hi "Sí, ya veo. Está bien. El año pasado lograron hacerlo solo Shizune y tú, ¿no es así? Así que estoy seguro de que podré también. No te preocupes por eso."

show misha hips_grin_close_ss
with charachange

mi "¿En serio? ¡Gracias, Hicchan~! ¡En serio~! ¡Viva viva~! ¡No sabía que Hicchan se lo tomaría tan bien~! ¡Pensé que estarías preocupado, por todo~ el trabajo que va a haber, con Tanabata aproximándose y todo eso~!"

"Maldita sea, ella me conoce extrañamente bien."

show misha sign_smile_close_ss
with charachange

mi "¡… Pero~! ¡Hicchan está tan tranquilo~! Me alegra~…"

hi "Jaja, sí. Tienes razón en cierto modo, estaba pensando en ello, pero no es gran cosa. No voy a volverme loco por eso."

hi "Pero va a ser un poco molesto pasar esa libreta de un lado a otro para hablar con Shizune."

show misha hips_frown_close_ss
with charachange

mi "¡Hicchan, solo dile a Shicchan que también puedes usar lenguaje de señas! No entiendo por qué no lo harás."

hi "Todavía no. Ya puedo entender muchas cosas, pero quiero estar bien seguro. Je, de hecho, no me molestaría. El secretismo también me está matando, y sería bueno poder hablar con ella en una conversación real."

hi "No te preocupes, al final voy a tener que decírselo. Quiero hacerlo. En realidad, estoy intentando pensar en una buena oportunidad para ello."

show misha hips_smile_close_ss
with charachange

mi "¡Eso no será un problema, Hicchan~!"

hi "¿Por qué no?"

stop music fadeout 3.0

show misha sign_smile_close_ss
with charachange

mi "Bueno~, porque yo… como que… le dije a Shicchan que tú podías entenderle. ¡Ella estaba preocupada por lo mismo, de que ustedes no podrían entenderse entre sí~! ¡Así que~! ¡Yo estaba preocupada, pero al final resultó bien después de todo~!"

show misha sign_confused_close_ss
with charachange

mi "¿Jajaja?"

"Me vuelvo loco."

play music music_running

hi "¡¡AAAAAAAAAAHHH!!"

hi "¿Sabes lo estúpido que me veo ahora? Estuve allí sentado como la mitad del maldito día actuando como si no pudiera leer lenguaje de señas, ¿y estás diciéndome en serio que ella sabía todo el tiempo que yo podía?"

hi "Probablemente estaba pensando, “este tipo es un completo idiota, fingiendo que no puede entenderme”. Acabo de quedar en ridículo."

hi "¡¿Cómo pudiste dejarme hacer esto?!"

show misha hips_frown_close_ss
with charachange

"Misha frunce el ceño, aparentemente sin saber qué decir al darse cuenta de que lo estoy tomando de una manera diferente a la que pudo haber esperado. Ella no habla de nuevo hasta después de ver que me he calmado."

show misha hips_smile_close_ss
with charachange

mi "… Pero, Hicchan, ¡creo que esto es sin duda lo mejor~!"

"Ella lo dice sin inmutarse, habiendo esperado pacientemente hasta que mi pánico desapareciera para decirlo."

"La alegre entrega de sus palabras hace parecer como si hubiera cortado el tiempo entre cuando ella me dio la noticia y ahora. Es muy divertido, en cierto modo."

hi "Tienes una mente muy cerrada, ¿lo sabías?"

show misha hips_grin_close_ss
with charachange

mi "¡Sí~!"

stop music fadeout 4.0

"El daño está hecho. Si Misha puede creer que las cosas funcionarán con tan inquebrantable certeza, entonces quizás vale la pena darle una oportunidad."

"Y si las cosas no funcionan, correré tan rápido como me sea posible…"

"Para intentar compensarme de todos modos por si acaso, ella se ofrece a comprarme otra bebida de la máquina expendedora. Es una muestra muy pequeña de disculpa, pero creo que la intención es lo que cuenta, y sus intenciones son sinceras."

"Además es una bebida gratis, así que acepto."

scene black
with dissolve


label es_S13:

scene bg school_dormhisao
with locationchange

"Me trago mi puñado diario de pastillas con un vaso de agua."

"Después de ocho horas seguidas de sueño, en realidad no sé a qué le tenía tanto miedo anoche. Mientras mastico una tableta particularmente grande a la mitad, sigo racionalizando mis preocupaciones para eliminarlas."

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_dreamy fadein 2.0

window hide

nvl clear

nvl show dissolve

n "Shizune sabía que estaba tomando lenguaje de señas durante todo el día de ayer, y no le dio mucha importancia a ello."

n "Ella puede ser muda, pero eso no significa que no pueda dar a conocer sus sentimientos. No, de hecho, parece que ella es la más directa al respecto."

n "Ella no se anda con rodeos ni se contiene, siempre deja las cosas en claro y sin remordimientos, así que no puede haber errores."

n "Así que, si ella no estaba furiosa en ese momento, es improbable que lo estuviera en absoluto. Y encima de eso, no hice nada malo, de todos modos."

n "Pero mientras mi miedo desaparece, la idea de pasar un par de días con Shizune sin Misha toma su lugar. En realidad no había pensado en ello ayer, pero la idea se vuelve cada vez más intimidante. Es cierto que puedo entender el lenguaje de señas bastante bien, pero…"

n "Sin duda vacilaría en decir que puedo entenderlo por encima de un nivel básico, y si fuera a aumentar la velocidad en sus gestos, lo cual ella hace bastante, no creo que pueda mantener el ritmo."

n "Hacer señas tampoco es mi punto fuerte. Hacer ambas cosas al mismo tiempo al igual que Misha todavía es un sueño distante."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

scene bg school_scienceroom
show misha hips_grin at twoleft
show shizu behind_smile at tworight
with shorttimeskip

window show

mi "¡Hicchan~!"

hi "¿Qué?"

show misha sign_smile
with charachange

mi "¡No lo olvides, dijiste que hoy ayudarías a construir los puestos~! Detrás de la escuela después de clases, ¿de acuerdo~?"

hi "Lo sé, lo sé."

show shizu adjust_happy
with charachange

shi "…"

show misha hips_smile
with charachange

mi "¡La última vez que ayudaste, Hicchan, realmente lo apreciamos~! Esta vez, es aún más importante, así que evadirlo es imperdonable, ¿bueno?"

"Quiero preguntar por qué es eso, pero no hay ninguna oportunidad. Además, Misha está atrasada en sus clases, así que parece una mala idea distraerla ahora que sé eso. Siempre puedo preguntárselo en el almuerzo, lo cual termino haciendo."

scene bg school_cafeteria
show misha sign_smile at twoleft
show shizu behind_blank at tworight
with shorttimeskip

mi "Porque, Hicchan, un festival que celebra un pueblo es exactamente lo que parece. Es para celebrar tu hogar y su historia."

show misha hips_grin
with charachange

mi "¡Tanabata es diferente, es para deseos y amantes~! Eso sin duda lo hace más importante, ¿no es así? Sí~, naturalmente, lo sería~."

hi "¿Pero realmente es para eso?"

show shizu basic_frown
with charachange

shi "…"

show misha cross_frown
with charachange

mi "Hicchan, no tienes sentido de la diversión…"

"Ella infla sus mejillas en disgusto antes de expulsar el aire como un globo desinflándose."

show misha hips_frown
with charachange

mi "¡Tienes que apreciar cosas como esa, incluso si al final es solo una excusa para comer cosas interesantes y vestirse bien~!"

show misha sign_smile
with charachange

mi "Estaré decepcionada de ti si no lo haces, ¿bueno?"

stop music fadeout 5.0

"Antes de que pueda decir nada, ella se gira al lado para tragarse una croqueta."

scene bg school_gardens2
with shorttimeskip

"Después de clases, me encuentro con Shizune detrás de la escuela, donde parece que ella ya preparó todo en algún momento de ayer."

show shizu adjust_happy at center
with charaenter


"Ella me saluda con un pequeño gesto, y entonces con un ademán del martillo ya en su mano, extiende su brazo hacia los puestos detrás de ella, algunos de ellos ya medio terminados, otros aún son montones desordenados de tablas atadas con cuerdas."

hide shizu
with charaexit

show bg school_gardens2_ss as overlay at Alphain(20.0), center
with None

play ambient sfx_stallbuilding fadein 8.0

"Mientras el tiempo pasa, me doy cuenta de que las píldoras no hacen mucho. Aún me canso más de lo que debería normalmente."

"Por suerte, la espalda de Shizune está hacia mí, así que puedo permitirme tomar muchos descansos sin tener que preocuparme de que ella pregunte por qué."

"Pero cuando me detengo a pensar en ello, comienzo a sentirme bastante culpable por aprovecharme de su incapacidad de escuchar que mi martillo dejó de golpear. Es una cosa terrible de la que alegrarse."

"Su ética de trabajo es admirable. Es obvio que eso la aburre, y hasta la molesta, pero ella no afloja el paso. Cuando se cansa de clavar un puesto con un brazo, ella cambia al otro."

hi "Shizune—"

"Me siento como un idiota en el momento en que digo su nombre."

"No puedo decirle lo que pienso. Hay un martillo en mi mano también, y al final, siento que tengo que seguir su ritmo."

"Tampoco puedo holgazanear, especialmente cuando solo somos nosotros dos. No hay tiempo de hacer señas, no hay oportunidad. Ni siquiera para un cumplido por un trabajo bien hecho."

"Incluso algo tan casual como eso requeriría que yo baje mi martillo, llame su atención, y luego se lo diga en señas."

"Un simple gesto convertido en algo tan innecesariamente complejo, como un solo paso dado sobre un camino que es más largo de lo imaginado al principio."

"La he conocido lo bastante como para saber esto, y aun así lo olvidé."

"El aire se llena con el golpeteo rítmico de clavos siendo enterrados en la madera."

"En realidad es algo agradable después de un rato. Para pasar la monotonía de la tarea a mano, intento hacer coincidir mi martilleo con el de Shizune, luego lo alterno e intento formar un ritmo. Por supuesto, ella no lo nota."

"Eso hace que me pregunte, ¿la falta de sonido hace que este trabajo parezca más interminable y aburrido para ella?"

stop ambient fadeout 3.0

"¿Es extraño, ser incapaz de oír los resultados de sus acciones incluso cuando siente las vibraciones a través de sus dedos? O, al no tener un concepto de sonido, ¿eso no le molesta en lo más mínimo?"

"Distraído, no noto a Shizune acercarse sigilosamente hasta que su cabeza salta a la vista."

scene bg school_gardens2_ss
show shizu adjust_happy_ss at center
with charaenter

play music music_soothing fadein 5.0

ssh "¿Tomando un descanso?"

his "Sí, supongo."

show shizu behind_smile_ss
with charachange

ssh "Muy bien, hagamos eso."

show shizu basic_normal_ss
with charachange

ssh "Puedes entender el lenguaje de señas."

show shizu behind_blank_ss
with charachange

ssh "Eso lo hace más conveniente para los dos. A pesar de que lo escondiste de mí."

hi "Jajaja…"

show shizu basic_normal2_ss
with charachange

ssh "¿Por qué?"

his "¿Por qué qué?"

show shizu behind_blank_ss
with charachange

ssh "¿Por qué decidiste aprender lenguaje de señas?"

"Sus ojos no se desprenden de los míos ni por un segundo, si necesita leer mi respuesta, su visión periférica es bastante buena. Una vez que ella se fija en algo, no aparta su mirada."

"Es extraño lo penetrantes que pueden ser sus ojos, oscuros como un lago de noche."

his "Porque quería. Parecía que sería útil. Y lo fue, ¿no es así?"

show shizu adjust_happy_ss
with charachange

ssh "Sí."

show shizu basic_normal_ss
with charachange

shi "…"

his "Lo siento, no capté nada de eso."

his "¿Ves? Este tipo de cosas surgen de vez en cuando. Desearía que Misha estuviera aquí."

show shizu behind_blank_ss
with charachange

ssh "Ella tiene trabajo para compensar, ¿no es así?"

ssh "Eso podría ser en parte mi culpa. Misha no necesita lecciones suplementarias. Sus notas no son las mejores, pero ella entiende cómo las decisiones que toma afectan a los demás. Eso la pone delante de muchas personas."

show shizu basic_angry_ss
with charachange

ssh "Especialmente de ciertas rubias."

hi "Ah…"

"Ella no olvida las cosas fácilmente."

show shizu behind_smile_ss
with charachange

ssh "Tu lenguaje de señas es muy bueno. Estás aprendiendo extrañamente rápido."

his "He estado tomando clases por un tiempo. Y es algo fácil de aprender después de un tiempo, a través de inmersión, o por ósmosis, ese tipo de cosas. No es tan malo."

his "Y si estoy realmente atascado, Misha también está allí."

show shizu adjust_smug_ss
with charachange

shi "…"

show shizu behind_smile_ss
with charachange

shi "…"

"Supongo que hablé demasiado pronto. No entendí nada de eso. Hora de dar marcha atrás."

his "Bueno, sí, de hecho no es tan fácil. De hecho es difícil como el demonio. Como intentar recoger vidrio roto."

his "Pero supongo que en cierto modo también es interesante. Como una aventura. Bueno, no…"

show shizu basic_normal2_ss
with charachange

ssh "Recoger vidrio roto no es una aventura."

his "Claro que lo es. Es igual de exigente."

show shizu behind_blank_ss
with charachange

ssh "Si usas un recogedor y una escoba no lo es."

"Me siento frustrado y triste."

"Cuando levanto la mirada, noto que ella tiene una lata de gaseosa en su mano."

hi "¿De dónde sacaste eso?"

show shizu adjust_happy_ss
with charachange

"Olvido decirlo en señas, pero ella entiende de todos modos, siguiendo mis ojos, y saca otra de detrás de su espalda. Ella la lanza en mi dirección, y la atrapo con ambas manos."

show shizu behind_smile_ss
with charachange

ssh "Traje una más para ti."

play sound sfx_can

"Ella se detiene para deslizar su uña por debajo de la lengüeta de su lata y destaparla antes de ponerla a un lado por un momento."

show shizu basic_normal_ss
with charachange

ssh "Si vas a tratar de ayudarme tanto, entonces tengo que estar pendiente de ti también. Es natural."

show shizu behind_blank_ss
with charachange

ssh "Si vas a aprender lenguaje de señas, eso es algo completamente diferente. Naturalmente voy a estar impresionada. Lo que nos separa a los dos es la obligación."

show shizu adjust_happy_ss
with charachange

stop music fadeout 8.0

ssh "Estoy muy feliz."

show shizu behind_smile_ss
with charachange

"Ella se toma su bebida de un golpe, estira sus brazos hacia atrás y salta sobre sus pies."

show shizu adjust_smug_ss
with charachange

ssh "¡Muy bien! ¡De vuelta al trabajo!"

hide shizu
with charaexit

"Y así, terminó. Shizune regresa a su trabajo con la misma energía que antes, los rastros persistentes de una sonrisa en su rostro como la única evidencia de que ella había tomado un descanso en absoluto."

show bg school_gardens2_ni as overlay at Alphain(10.0), center
with None

"Mientras hago lo mismo, creo que Misha tenía razón en decir que todo resultaría para mejor. Todo hasta ahora parece estar yendo en esa dirección."

"Misha aparece cuando comienza a oscurecer, luciendo tan cansada como me siento, y Shizune decide parar por hoy."

"Mientras cubrimos el trabajo del día y nos separamos, miro la forma fluida como ellas hablan entre sí, y la facilidad con la que ríen juntas mientras caminan a sus dormitorios."

"Me hace apreciar más la habilidad de Misha en el lenguaje de señas. Me pregunto si lograré llegar a ese nivel, o incluso si tendré el tiempo para hacerlo."

scene black
with dissolve


label es_S14:

scene black
with None

play sound sfx_impact

scene bg school_dormhisao
with vpunch

"La primera cosa que hago esta mañana es tropezar una vez más con el paquete de Kenji cuando salgo de la cama, encontrándome cayendo de cabeza hacia el piso antes de estar completamente despierto."

show kenjibox:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"Quiero golpear esta cosa con el primer objeto contundente que pueda encontrar, como si fuera a hacer un jonrón, pero ni siquiera tengo la energía para eso tan temprano en la mañana… y eso probablemente dañaría lo que hay dentro."

"Y eso sería malo."

show kenjibox:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide kenjibox
with None

scene bg school_dormhallway
with locationchange

"La deslizo hacia el pasillo. Navega entre el piso liso con poca dificultad y se detiene con un golpe suave y casi inaudible al chocar con la puerta de Kenji. De inmediato, una docena de cerraduras se desatrancan seguidamente como una sinfonía creciente."

play music music_kenji fadein 0.5

show kenji tsun at Slide(0.4, 0.5, 0.5, 0.5, 0.5)
with charaenter

ke "¿Quién es?"

"Lo dice, mientras ciegamente sale hacia el pasillo de todos modos, de algún modo pasando sobre la caja de una manera que sería impresionante e inusitadamente elegante si no fuera por el hecho de que sé que fue completamente accidental."

hi "Soy yo, traje tu correo. Estás parado sobre él."

show kenji happy at center
with charachange

ke "Lo sé. Muchas gracias, hombre."

hi "… Sí, como sea."

hi "¿Y qué hay dentro?"

show kenji tsun
with charachange

"Él se encoge, inmediatamente volviéndose muy defensivo y agitado."

ke "No es nada."

hi "Vamos, dime, tengo curiosidad."

hi "Y sabes, casi me rompo el cuello al tropezar con ella, y antes de eso tuve que llevar esa caja estúpidamente grande a todas partes tapándome la vista, cruzando calles con ella delante de mí… Creo que al menos puedes decirme qué hay dentro a cambio."

ke "Son cosas secretas. No puedo decírtelo, porque entonces no sería muy secreto y esa mierda. No es nada importante."

hi "Bueno, si no es nada importante, puedes decírmelo."

ke "Si no es nada importante, ¿por qué tienes que saberlo?"

hi "¿Por qué eso es malo?"

ke "¿Por qué tienes que saberlo?"

hi "¿Por qué no puedo saberlo?"

show kenji neutral
with charachange

ke "¿Por qué estás respondiendo mis preguntas con preguntas?"

hi "¿Por qué no respondes mi primera pregunta?"

ke "¿¡Por qué no respondes mi última pregunta!?"

"Me doy cuenta de que nuestras voces son más altas con cada respuesta. Al fondo del pasillo, una puerta se abre y alguien asoma su cabeza con curiosidad para ver qué está pasando."

"Debemos parecer tan tontos, pero apuesto a que soy el único de los dos con la suficiente vergüenza como para darme cuenta de ello."

hi "Bien, puedes llevártelo a tu tumba. De todos modos tengo que alistarme para la escuela."

show kenji tsun
with charachange

ke "Maldición, no. ¿Por qué tienes tanto afán en irte? Quédate un momento. ¿Quieres algo de café? Ha pasado un tiempo. Sabes, pensé que estabas muerto ya que fuiste tan lento con la entrega del paquete."

hi "¡Tienes suerte de que estuviera dispuesto a recoger tu paquete en primer lugar, listillo!"

show kenji neutral
with charachange

ke "Vaya, cálmate. Hombre, eres tan beligerante. ¿Es por el cuento del consejo estudiantil? Oí que pasas el rato con ellas ahora."

hi "Lo oíste de mí. Cuando te lo dije."

ke "¿En serio?"

ke "Sí, bueno, como sea, hombre. El punto es que ellas son terribles."

show kenji tsun
with charachange

ke "Eres el chico nuevo, así que por supuesto no lo sabrías, pero por aquí ella es una figura muy divisiva. Antes de que llegaras, ella intentó instituir una política de insignias. Es una larga historia, así que quizás deberías sentarte."

"Busco una silla, pero no puedo encontrar una ya que estamos en un maldito pasillo. Levanto un dedo y comienzo a pensar que tal vez debería decírselo, pero ya comenzó a hablar. No queriendo gastar el movimiento del brazo, miro mi reloj."

ke "Habría sido un verdadero reinado de terror, de haber ocurrido."

hi "Espera, ¿estás juzgándola basado en algo que ni siquiera ocurrió?"

stop music fadeout 8.0

ke "Sí. Bueno, su idea era como insignias de mérito, pero también habría insignias de demérito."

hi "¿Qué harían esas?"

show kenji neutral
with charachange

ke "No lo sé, nunca ocurrió. Aunque parecía malo, así que cuando escuché sobre eso no salí de mi habitación por unas cuantas semanas."

hi "Así que escuchaste que habría grandes cambios y te escondiste en tu habitación, simplemente intentando sobrevivir al cambio."

show kenji tsun
with charachange

ke "No, decidí hacer algo al respecto. Encontré la oficina del consejo estudiantil después de un rato y fui directo allá con una lista de demandas y un montón de gente a la que agarré para hacerme ver como si tuviera partidarios."

hi "Espera, ¿así que no solo no ocurrió, sino que a nadie le importó siquiera?"

show kenji rage
with charachange

play music music_tension

"Kenji no me oye, habiendo conseguido un buen impulso en marcha. Envuelto en la energía de su propio desatino, él comienza a enloquecer por completo y a sacudir sus brazos, pareciendo lanzar salvajemente gestos de pandillas."

ke "Me acerqué al escritorio y le dije, “¡Oye tú, mujer fascista! ¿Qué es esta idea de la insignia?”."

ke "“¿Qué tan aislada puedes estar, aquí en tu torre de marfil, mirándonos engreídamente por encima del hombro como si fuéramos un montón de idiotas? ¿Quién te crees que eres?”."

ke "“Tu nivel de elitismo es terrible, probablemente eres una de esas personas ricas y extravagantes que tienen choferes que los llevan por los barrios pobres para así señalar a la gente y reírse…”."

ke "“… y solo beben granos de café costosos cagados por el último dinosaurio vivo y preparados en un cráneo de oro sólido”."

ke "“¿Y cómo podrías? Ve y abre un libro de historia; ¿no sabes que la burguesía siempre es derrocada en una revolución sangrienta por mierda como esta? ¡Estúpida! ¡Eres una idiota!”."


ke "“Claro, los revolucionarios por lo general terminan convirtiendo todo en un completo mierdero más adelante, pero un maníaco es la única clase de persona que crearía una política como esta…”."

ke "“… es como algo que yo crearía para hacer sufrir a la gente, ¡solo que real y tú quieres institucionalizarla! ¿Dónde terminará esta profanación de nuestros derechos? ¡Somos el pueblo! ¡Esto no es justicia!”."

show kenji neutral
with charachange

ke "Eso fue lo que dije."

show kenji rage
with charachange

ke "Luego añadí un grito de “¡Pueden quitarnos nuestras cosas, pero nunca nos quitarán nuestra libertaaaaaad!” para atraer a las masas como en esa película sobre la vida de William Wallace donde le quitaron sus cosas pero no su libertad, y luego lo mataron."

stop music fadeout 5.0

show kenji tsun
with charachange

ke "… Pero ella simplemente me ignoró y ni siquiera levantó la mirada de lo que escribía en su mierda de papelito."

ke "Tal vez la abrumé con mi lógica, tanto que ella solo se retiró a la negación. Tal vez ella solo es una imbécil. De cualquier manera, ella no respondió, y el futuro se negó a cambiar."

ke "Para rematar, cuando regresaba noté que había perdido mi credencial estudiantil en alguna parte. Esta es la historia de mi vida. Una lucha constante y aparentemente inútil. Como intentar escalar una pared de ladrillos con esponjas como manos."

hi "Oye, dijiste que nada cambió, pero ella no hizo que todos usaran un montón de insignias estúpidas. Entonces, sí cambió."

play music music_kenji fadein 0.5

show kenji happy
with charachange

ke "Sí, eso es cierto. Muy bien, tal vez no son tan malas, entonces."

"Supongo que eso sirve de algo, si puedo hacer que Kenji admita que tal vez dos mujeres pueden no ser tan malas después de todo. Lo tomaré. Sobre todo si eso me permite salir de esta conversación; no me di cuenta de cuánto tiempo había pasado."

stop music fadeout 2.0

scene bg school_dormext_full
with locationchange

"Intento repasar mi típica rutina matutina tan rápido como sea posible. Reviso mi reloj de nuevo cuando dejo los dormitorios y veo que ya llego tarde."

scene bg school_scienceroom
with shorttimeskip

play music music_daily fadein 1.0

"Afortunadamente, el resto del día pasa sin problemas, y después de terminadas las clases, me dirijo a encontrarme con Shizune otra vez."

scene bg school_gardens2
with locationskip

"Detrás de la escuela, la sorprendo apoyada contra un puesto terminado con partes de él aún salpicadas con trozos de papel y cinta, restos de señales de la última vez que se usó. Girando distraídamente un clavo en su mano, ella no me ha notado aún."

"La tentación de acercarme sigilosamente a ella es insoportable. Años de mirar documentales extranjeros de vida salvaje me han preparado para esto. Estoy con el viento, las condiciones son favorables."

"Sin embargo, entre más lo pienso, más me parece una mala idea."

"Si me sorprende a medio camino quedaré como un idiota, y si ella no sabe que soy yo, podría terminar con una lesión. Sea como sea, también pareceré un poco insensible."

"Entonces, probablemente sería mejor no intentar nada gracioso… tan decepcionante como es."

show shizu adjust_blush at center
with charaenter

"Camino enfrente de ella, asustándola un poco."

his "¿Por qué tan sorprendida? ¿Te atrapé holgazaneando?"

show shizu behind_blank
with charachange

ssh "No, estaba tomando un descanso."

his "No parece que ni siquiera hayas sudado. Ese es un gran descanso, presidenta."

show shizu behind_frustrated
with charachange

"Los ojos de Shizune se mueven de un lado a otro momentáneamente, y creo que he logrado ponerla nerviosa."

"Hay exasperación en su rostro, y una pequeña tensión también, pero no puede dar marcha atrás; eso sería impensable para ella. Sus dedos bailan entre sí impacientemente."

show shizu basic_normal2
with charachange

ssh "Estás actuando de manera competitiva hoy. ¿Estás tratando de hacer que mi sangre hierva? ¿Quieres convertirlo en un concurso? Competiremos para ver quién puede construir más puestos para el atardecer."

his "¡No, no! Te estoy tomando el pelo. Está bien, no es un verdadero consejo estudiantil si no puedes burlarte un poco de la presidenta del consejo estudiantil. Estás de acuerdo, ¿no?"

show shizu behind_frown
with charachange

ssh "Eso no está en los estatutos del consejo estudiantil, así que no es cierto."

his "¡No hay estatutos!"

"Al menos, no creo que los haya. La única cosa a la que ellas juran lealtad es a un montón de menús de comida para llevar."

show shizu adjust_smug
with charachange

ssh "De todos modos, es bueno que finalmente estés aquí, incluso si podrías haber estado antes. Toma un martillo y continuaremos donde dejamos."

hide shizu
with charaexit

play ambient sfx_stallbuilding fadein 0.5

"Mientras trabajamos montando los puestos de nuevo, lentamente me doy cuenta de que en realidad es mucho menos trabajo del que habría esperado. En realidad, de acuerdo con Shizune, deberíamos acabar para el fin del día con un poco de suerte."

"La última vez que hice algo así para ellas, nos tomó a Misha, a ella y a mí casi cuatro días para hacerlo. No puede ser simplemente mi imaginación."

stop ambient fadeout 2.0

his "Sabes, esto no parece ser tanto trabajo."

show shizu behind_blank at center
with charaenter

ssh "Porque no lo es."

play ambient sfx_parkambience fadein 10.0

"Esa respuesta me deja queriendo un poco más. Sabiendo que no es lo mejor, Shizune baja su martillo para dar detalles."

show shizu basic_happy
with charachange

ssh "Sería imposible para dos personas hacer tanto trabajo en menos de una semana. La verdad es que no desmonto la mitad de los puestos, solo los guardo en algún otro lugar. De hecho, más bien los escondo a la vista."

show shizu adjust_smug
with charachange

"Ella mueve un dedo pícaramente."

show shizu adjust_happy
with charachange

ssh "Pero ese es un secreto, y no es apropiado revelar los trucos del oficio."

his "No eres maga."

show shizu behind_smile
with charachange

"Haciendo un guiño, ella saca dos recipientes plásticos de su mochila, luego los pone en una tabla cercana antes de levantar ligeramente sus manos como para decir “¡Ta-rá!”."

show shizu adjust_happy
with charachange

ssh "Hoy hice el almuerzo para los dos."

show shizu behind_smile
with charachange

ssh "Puedes tener este. La comida se movió en mi mochila y ahora está un poco revuelta."

"Ella me entrega uno de los recipientes. Lo abro. Se ve delicioso, aunque un poco simple. Me entrega un par de palillos, como si lo acabara de recordar, y como lo que parece ser carne a la parrilla."

his "Es muy sabroso."

his "¿No te gusta que tu comida toque otra comida?"

show shizu basic_normal
with charachange

ssh "No me gusta."

his "Eres muy exigente."

show shizu behind_blank
with charachange

ssh "A veces revuelvo mi comida por mi cuenta, pero no siempre, y no todo. No me gusta cuando lo hacen por mí. Lo que es importante es la elección."

show shizu basic_normal
with charachange

"Ella apunta decididamente para enfatizarlo, y luego rompe sus palillos para comer su propia comida."

"Mientras sigo comiendo, noto dos cosas. La primera es que casi todo lo que estoy comiendo aparte del arroz está frito. Hasta los vegetales están fritos."

"Y hay mucha carne. ¿Ella come este tipo de cosas todo el tiempo? Me pregunto cómo se las arregla para mantenerse tan delgada a pesar de ello."

"La segunda cosa que noto es que no puedo hablar con ella mientras como. Hablar con tu boca llena es un poco grosero de todos modos, pero con nuestras manos sujetando nuestros palillos y tazones, la comunicación entre los dos es imposible. Tal como ayer."

"Aunque estamos pasando tiempo juntos, aunque me tomé el tiempo de aprender lenguaje de señas, se siente como si estuviera hablando menos con ella. A pesar de eso, también se siente como si la estuviera entendiendo más."

stop music fadeout 4.0

show shizu basic_normal at tworight
show bg school_gardens2 at bgright
with charamove

show lilly cane_smileclosed at twoleft
with charaenter

"Oigo el sonido de algo golpeteando contra uno de los puestos y levanto la mirada para ver a Lilly parada a mi lado, sintiendo su camino con su bastón."

hi "Hola."

"Por poco me contengo antes de que pueda decir “no te vi allí”."

show lilly cane_surprised
with charachange

li "Oh, Hisao, ¿eres tú? Pensé que olía algo de comida deliciosa, y me pregunté qué podría ser."

show shizu behind_frustrated
with charachange

ssh "¿Ella qué está diciendo?"

play music music_happiness fadein 6.0

"Es difícil mover mis manos a la vez mientras le digo algo completamente diferente a Lilly. Esto tiene que ser por qué Misha simplemente gesticula todo, todo el tiempo. Un poco tonto, pero parece que simplificaría mucho las cosas."

show shizu basic_happy
with charachange

"Shizune junta sus dedos con alegría ante mi traducción, como si oyera un chiste."

show shizu adjust_smug
with charachange

ssh "Toda esta comida fue cocinada hace horas, pero para alguien tan lenta como tú, quien ni siquiera puede entregar un pedazo de papel sin estar una semana tarde, ¡supongo que tu percepción del tiempo tendría que ser un poco diferente!"

hi "Eso… no es muy bueno."

show lilly cane_displeased
with charachange

"Un ceño fruncido cruza el rostro de Lilly en reacción a una respuesta que ella no oyó."

hi "Ah, lo siento. Solo estoy almorzando tarde aquí. La presidenta del consejo estudiantil cocinó todo."

show lilly cane_reminisce
with charachange

li "¿La presidenta del consejo estudiantil está aquí ahora mismo?"

hi "Está justo aquí."

show lilly cane_listen
with charachange

li "Me disculpo, no lo noté. Normalmente su nivel de presencia es mucho más alto. No era consciente de que el consejo estudiantil sirve almuerzos al aire libre, ¿por qué no fui invitada?"

li "Sin embargo, creo que es bueno tener suficiente tiempo libre para poder hacer cosas como esta."

show shizu behind_frustrated
with charachange

ssh "¿Ella qué está diciendo?"

"…"

show shizu basic_angry
with charachange

ssh "Si fuera a invitarte a alguna parte, simplemente te aparecerías tarde."

"Pero las palabras de Shizune están fuera de la percepción de Lilly, un hecho que cada vez es más y más exasperante para ella."

show shizu behind_frown
with charachange

ssh "Traduce por mí completamente, por favor."

"Qué frase tan cortés. Es una pena que ella básicamente me esté pidiendo que le deje soltar por completo los perros de guerra."

"Aun así, no puedo quedarme quieto. El sentimiento de ser incapaz de incluso responder y ser entendido es tan aislante. Ella nunca me lo perdonaría. Simplemente intentaré suavizar sus palabras un poco."

hi "Bueno, de hecho, todo esto fue cocinado hace un rato."

show lilly cane_weaksmile
with charachange

li "¿En serio? Eso es bueno."

show shizu cross_angry
with charachange


ssh "Voltea aquí, es muy irrespetuoso no mirar a la persona con la que estás hablando. Esa no es la forma en la que una dama correcta y formal debería comportarse."


hi "La mitad de lo que estoy diciendo en realidad es lo que Shizune está diciendo. A ella no le gusta que la gente no mire en su dirección cuando trata de decir algo importante. Ella está, eh, a la derecha de mi voz."

"Aunque en este caso puedo entender por qué Lilly no lo haría. Esta es una situación muy incómoda y es desalentador ser el único conducto para el diálogo entre ellas dos."

"Sinceramente, había olvidado lo que pasó la última vez que topetaron cabezas como ahora. Es claro que Shizune lo recuerda, y Lilly misma está siendo bastante hostil, a su propia manera."

show lilly cane_displeased
with charachange

li "Lo siento, dichas formalidades se me olvidaron por completo. Olvidé que la presidenta del consejo estudiantil es el tipo de persona que exigiría tal respeto y cumplimiento a las reglas en todo momento."

show lilly cane_listen
with charachange

li "Supongo que el gobierno estudiantil requiere que tú seas muy eficiente. Por otra parte, ella ciertamente tiene tiempo para su propia diversión también, así que eso no debe ser completamente cierto."

show shizu adjust_angry
with charachange

ssh "¡El consejo estudiantil no es una dictadura, ni un juego de suma cero!"

play sound sfx_snap

"Shizune apunta a Lilly con su dedo como el cañón de una pistola y hace sonar sus dedos explosivamente, haciendo que se estremezca y se torne visiblemente molesta."

show lilly back_listen
show lillyprop back_cane at twoleft
with charachange

li "¿Es cierto? Entonces eso hace más impresionante que hayas sido parte de él por tanto tiempo, jugando como si fuera una. Admiro el hecho de que seas tan tenaz. Para manejarlo todo, debes ser muy responsable también."

show shizu behind_frown
with charachange

ssh "No tanto como me gustaría serlo. Aunque no puedes quejarte de ti misma, ¿o sí?"

show shizu cross_rage
with charachange

ssh "Tú eres muy responsable; ¿acciones como pedir que se extienda una fecha límite y luego perder el tiempo hasta la próxima fecha límite? ¡Ese es el modelo mismo de la responsabilidad!"

hi "Shizune está feliz de oír eso. Pero, aparentemente tú misma eres bastante responsable, dice ella."

show lilly cane_surprised
hide lillyprop
with charachange

li "¿De verdad?"

hi "Más o menos…"

"Lilly no parece muy feliz."

hi "No estamos teniendo una comida al aire libre, solo estamos tomando un pequeño descanso para almorzar. De hecho estamos aquí afuera construyendo puestos para el festival."

show shizu behind_frown
with charachange

ssh "No lo sabrías, ya que nunca sales. ¿Se te acabó el té?"

hi "¿Vas a ir al pueblo? ¿De compras?"

show lilly back_devious
show lillyprop back_cane at twoleft
with charachange

li "No. Como dije antes, solo estaba pasando, en caso de que no oyeras. Odiaría interrumpir a la presidenta del consejo estudiantil. No estás haciendo nada ahora, pero ustedes dos deben estar muy ocupados."

show lilly cane_listen
hide lillyprop
with charachange

li "En cualquier caso, Hisao, estoy segura de que la presidenta del consejo estudiantil será capaz de encontrar o hacer trabajo para los dos si ella lo necesita."

show shizu cross_rageclosed
with charachange

ssh "¡Te voy a devorar!"

hi "Sí, muy ocupados."

"“Devorar” es una palabra difícil. Me alegra poder leerla. Aunque no es tiempo para celebrar, no sobre eso. En vez de ello, parece que podrían dejar de pelear. Brindaría por eso."

show lilly cane_listen
with charachange

li "Que tengas un buen día, Hisao. Adiós, presidenta del consejo estudiantil."

hi "Gracias, igualmente."

show shizu basic_frown
with charachange

ssh "Sigue elegante."

hide lilly
with charaexit

show shizu basic_normal2 at center
show bg school_gardens2 at center
with dissolvecharamove

stop music fadeout 4.0

"Tan pronto Lilly se va, Shizune se aboca de lleno en los restos de su almuerzo lo más rápido posible, como si cada bocado que ella engullera fuera un medio para olvidar que todo esto ha ocurrido."

hide shizu
with charaexit

"Cuando ella ha acabado, regresa inmediatamente a martillar con la misma mentalidad. Es bueno que esté desahogando su frustración, pero ahora no parece que ella esté de humor para hablar más."

show bg school_gardens2_ss
with shorttimeskip

play music music_tranquil fadein 3.0

"Casi dos horas más tarde, ella se detiene, habiendo segado a través del resto de los puestos sin parar en ese tiempo."

"Aún se siente difícil acercarse a ella, y pienso en lo fácil que una conversación puede morir. Después de que tomara tanto tiempo poder estar a solas con ella y hablarle directamente, eso casi duele."

show shizu basic_normal_ss at center
with charaenter

ssh "Tu traducción fue buena."


his "¿En serio?"

show shizu adjust_happy_ss
with charachange

ssh "¡De primera clase!"

"Ella lo puntúa con un pulgar hacia arriba."

show shizu behind_blank_ss
with charachange

ssh "… Para tu nivel."

show shizu basic_normal_ss
with charachange

ssh "No hay muchas personas sordas en la escuela, y las clases de lenguaje de señas han estado al borde de ser canceladas desde hace un tiempo. Estoy segura de que no tienes muchos compañeros, ¿o me equivoco?"

show shizu behind_blank_ss
with charachange

ssh "Si solo estás aprendiendo lenguaje de señas ahora, tu velocidad va a ser limitada. Es por eso que el interés en él disminuye, porque se necesita más esfuerzo del normal solo para comunicarse. Imagino que es lo mismo con todos los idiomas."

show shizu basic_normal2_ss
with charachange

ssh "En una situación así, las conversaciones en lenguaje de señas son menos … de lo que intrínsecamente serían para comenzar."

his "No entiendo esa palabra. ¿Menos qué?"

show shizu behind_blank_ss
with charachange

show shizu basic_normal2_ss
with charachange

ssh "Es-{w=0.2}pon-{w=0.2}tá-{w=0.2}ne-{w=0.2}as."

show shizu behind_blank_ss
with charachange

ssh "Misha es la única persona que realmente puede captarla."

his "Sí, eso es definitivamente cierto."

show shizu behind_sad_ss
with charachange

show shizu behind_blank_ss
with charachange

"Su expresión cambia por un segundo, y vuelve a cambiar muy rápido como para asimilarla, pero tengo la sensación de que esto no se supone que sea tenido en cuenta."

"De lo que realmente quiero saber es…"

his "¿Por qué Lilly y tú pelean tanto?"

show shizu basic_frown_ss
with charachange


"Poniéndose un poco tensa y visiblemente frunciendo el ceño, Shizune junta sus dedos y los cubre repetidamente como si mezclara una baraja invisible de cartas."

show shizu behind_frustrated_ss
with charachange

ssh "Dos peleas de las que sepas no valen llamarse “tantas”. Si hubieras estado aquí el año pasado podrías decir eso."

his "Escuché que fue un año difícil. Algo sobre cómo trataste de instituir una política de insignias."

show shizu cross_wut_ss
with charachange


his "Ja ja, ¿sorprendida? Bueno, quiero escuchar más de eso después, definitivamente, pero… no te agrada mucho Lilly, ¿no es así? No esquives mi pregunta."

show shizu behind_frustrated_ss
with charachange

ssh "No estoy esquivando nada."

show shizu basic_angry_ss
with charachange

ssh "Ella era parte del consejo estudiantil hasta el año pasado. No nos llevábamos muy bien. Ella quería seguir haciendo las cosas como las hacía el viejo consejo estudiantil. El viejo consejo estudiantil era tan ineficaz. Era estúpido, e insultante."

show shizu behind_frown_ss
with charachange

ssh "Yo quería hacer más, y tuvimos una discusión."

show shizu basic_frown_ss
with charachange

ssh "Muchas discusiones."

show shizu adjust_angry_ss
with charachange

ssh "Ella no podía hacer nada a tiempo."

show shizu behind_frustrated_ss
with charachange

ssh "Entonces, dijo que lo que yo quería hacer no tenía sentido, solo eran tareas inútiles de más. ¿Esto te parece una tarea inútil y sin sentido?"

"Shizune hace un gesto alrededor de nosotros."

show shizu basic_frown_ss
with charachange

ssh "Lo que realmente no tiene sentido es un consejo estudiantil que no hace nada. Débil, perezoso y aburrido. ¡Especialmente aburrido!"

show shizu adjust_angry_ss
with charachange

ssh "No podía emocionarme al estar sentada en un salón sin nada que hacer, eso era una pérdida de tiempo. ¿Por qué estaría allí? Eso no hacía correr mi sangre. ¡Discutir con ella sí!"

show shizu behind_blank_ss
with charachange

ssh "Si ella pudiera haber estado así de motivada antes, no habría tenido que poner tanta dedicación en ser mi enemiga. Pero si ella muestra tanto de ese espíritu, no es una completa pérdida. ¡Al menos es algo! Aún es emocionante."

his "Ya veo."

his "¿Y qué hay del asunto de la insignia?"

show shizu adjust_happy_ss
with charachange

stop music fadeout 4.0

"Ella se ríe, cubriendo su boca con su mano como si la escondiera. Su risa es la única cosa que esconde con frecuencia."

show shizu behind_smile_ss
with charachange

ssh "Eso solo fue una broma."

show shizu adjust_happy_ss
with charachange

ssh "Divertirse un poco de vez en cuando es importante, también."

stop ambient fadeout 0.5

scene black
with dissolve



label es_S15:

scene bg school_dormext_full
with locationchange

play music music_normal fadein 0.5

"El día siguiente, termino buscando un poco al inicio del almuerzo, cuando descubro que a mi máquina expendedora habitual, cerca de los edificios de los dormitorios, se le acabó mi habitual café enlatado favorito. La desviación toma más de lo que esperaba."

scene bg school_gardens
with locationchange

"Las cosas han estado tan frenéticas últimamente que necesito algo de tiempo para notar por qué algo huele diferente mientras camino por los jardines de la escuela al regresar a la cafetería. El césped ha sido recién cortado."

"La revelación hace que me detenga y mire por un momento. El extraño grupo de estudiantes charlando o jugando sobre el césped y un par de maestros conversando en el camino adelante dan lugar a una escena muy idílica."

stop music fadeout 2.0

"Desafortunadamente, un sentimiento de inminente terror comienza a acercarse sigilosamente a mí después de un rato. El sentimiento de que no estoy solo."

play music music_kenji fadein 0.5

show kenji neutral at center
with charaenter

ke "Oye, Hisao, ¿eres tú?"

hi "Sí, soy yo."

"Supongo que debería estar feliz de que sea él y no, digamos, un acuchillador. Kenji comienza a hablar como si tuviera una conversación con una persona distinta a mí."

show kenji happy
with charachange

ke "Lo sabía. Ese corte de pelo es inconfundible. Ninguna persona normal tendría un corte como ese."

"Inconscientemente, comienzo a tocarme la parte de atrás de mi cabeza. Una vez me doy cuenta de lo que estoy haciendo, me siento insultado, sin embargo muy sorprendido como para indignarme por ello."

hi "Sí… ¿Qué estás haciendo aquí?"

show kenji neutral
with charachange

ke "Midiendo la temperatura."

show kenji happy
with charachange

ke "El invierno vendrá pronto. Será muy frío como para que las mujeres salgan y coman sus almuerzos energéticos estilo “Sexo en la Ciudad”, seguidos por caminatas obstructivas en formación de ola humana en áreas urbanas concurridas."

ke "Cuando esto ocurra, el hombre podrá caminar por las calles sin restricciones una vez más, y reclamar lo que es su patrimonio."

show kenji neutral
with charachange

ke "Con el fin de prepararme para ese día, no he estado comiendo nada más que pizzas durante la última semana, para guardar energía."

hi "Muy bien."

hi "Eso es lo que hacen los osos."

show kenji happy
with charachange

ke "¿Y qué? Hay mucho que podemos aprender del oso."

"Kenji asiente, enfáticamente estando de acuerdo consigo mismo."

show kenji neutral
with charachange


ke "Muy bien, así que mira esta mierda: estaba en el pueblo hoy, comprando leche. Tenían una nueva dependienta, una chica hipster con una gorra de beisbol con dos palos de hockey en ella. La llamaré “chica hipster de la gorra de beisbol de hockey”."

ke "Noté que la leche no tenía etiqueta de precio, así que le dije que fuera allí y etiquetara esa leche, para futuras generaciones."

"¿Él estaba en el pueblo hoy? Debió haberse saltado sus clases de la mañana. Quiero regañarlo, pero su torrente verbal me impide que meta una palabra."

show kenji tsun
with charachange

ke "Me dijo que no la molestara, porque estaba enferma. ¿Enferma? ¿¡Enferma!? Aquí vivimos en una sociedad. No puedes abandonar la interacción humana porque estás enfermo. ¿Sabes cuánto esfuerzo me toma incluso levantarme en la mañana?"

show kenji rage
with charachange

ke "Aun así lo hago, y me levanté esa mañana para ir allí y comprar leche, no para que mis preguntas vitales sean simplemente apartadas por una estúpida chica universitaria hipster que usa una {b}gorra de beisbol de hockey{/b} para trabajar. {b}Adentro{/b}."

show kenji tsun
with charachange

ke "Bueno, solo estaba intentando defender la integridad de sus productos. ¿Un envase de leche sin etiqueta de precio? Cuando veo algo así, eso lleva a preguntas. Preguntas importantes. Es su trabajo responderlas, maldita sea."

ke "Ese es el problema con las mujeres, no tienen sentido del deber."

show kenji neutral
with charachange

ke "Me da mucha diarrea, pero no me ves quejándome por ello. Sigo adelante y hago lo que tengo que hacer de todos modos, porque ser un hombre se trata de todo eso. Aun si tienes diarrea, continúas, por el sueño de un mejor mañana."

hi "Sabes, la diarrea frecuente es mala."

hi "Tal vez deberías dejar de beber tanta leche."

ke "No puedo hacer eso, es lo que me permite mantener mi increíble fuerza. Y en este mundo… la fuerza de un hombre es la única cosa que no le pueden quitar con intimidaciones por una sociedad cada vez más sumisa ante las mujeres."

show kenji happy
with charachange

ke "Es por eso que camino dejando frascos abiertos de aceitunas por todas partes. A veces solo para demostrar que puedo."

hi "¿Las refrigeras después de abrirlas?"

show kenji tsun
with charachange

ke "¿Qué? Hombre, no lo sé, eso no es importante."

hi "Tienes que refrigerarlas después de abrirlas. Hasta los niños de primaria saben eso."

show kenji neutral
with charachange

ke "Ellos no pueden abrir el frasco en primer lugar, así que no importa."

hi "Ah, eso es cierto."

show kenji happy
with charachange

ke "Soy un genio."

"Se frota su barbilla, seguro de sí mismo, lo cual es algo que imaginé que los científicos hacían, hasta que conocí a Mutou y quedé tremendamente decepcionado."

show kenji neutral
with charachange

ke "Bueno, no puedo ir a esa tienda de nuevo, ya que claramente ha sido puesta en peligro por perras. A menos que… me disfrace. Tal vez cambiar a un par de anteojos diferentes."

hi "El peor disfraz de todos."

show kenji tsun
with charachange

ke "Pffft, ha estado funcionando a la perfección todos estos años. Ni siquiera necesito anteojos para ver. Son para efecto. También, para proteger mi identidad. Soy como Superman."

hi "El peor disfraz de todos."

show kenji happy
with charachange

ke "Te lo digo, cuando la gente ve mi credencial estudiantil, ni siquiera puede reconocerme."

hi "¿En serio? Déjame ver."

show kenji neutral
with charachange

ke "No puedo hacer eso. No puedo andar mostrando mi credencial a todo el mundo. Fue hecha hace mucho tiempo. En un tiempo diferente. Tenía cabello hippie."

stop music fadeout 2.0

"Mientras estoy intentando imaginar eso, Kenji se quita sus anteojos."

$ ksgallery_unlock("evul kenji_glasses_closed")
scene evbg kenji_glasses:
    truecenter
    subpixel True zoom 0.82
    acdc_warp 20.0 zoom 0.8
show evmg kenji_glasses_closed at kenji_mg_out
show evfg kenji_glasses:
    truecenter
    subpixel True zoom 1.0
    acdc_warp 20.0 zoom 0.8
with whiteout

play music music_friendship


"Él entrecierra sus ojos tan pronto están fuera de su cara, lo cual lo hace ver aún más cansado de lo que ya está. Tenía razón; él sí se ve muy diferente. Casi como si no hubiera dormido en años. Pero no es tan diferente como para que sea un buen disfraz."

hi "Necesitas dormir más."

$ ksgallery_unlock("evul kenji_glasses_frown")
show evmg kenji_glasses_frown at kenji_mg_out
with charachange

ke "No."

hi "Parece que lo necesitas."

$ ksgallery_unlock("evul kenji_glasses_normal")
show evmg kenji_glasses_normal at kenji_mg_out
with charachange

ke "De ninguna manera. Estos son simplemente los ojos de un hombre que ha visto cosas. Los ojos de un chamán. Cosas terribles, que no puedes imaginar."

ke "Como cuando hice un barco en una botella y mi mamá se sentó sobre ella. Había sangre y jirones de estampado floral por todas partes. Eso es experiencia de vida."

"Kenji no parece muy horrorizado, aunque creo que esto es de hecho la primera cosa que me cuenta sobre él mismo que podría haber sido legítimamente traumática."

"También está hablando a unos treinta grados a mi izquierda, así que supongo que su ceguera es real. Muevo una mano enfrente de él de todos modos, con poco efecto."

ke "Hombre, espero que te des cuenta de que solo estoy bromeando."

"Me río, fingiendo que lo hice. De alguna manera, mirarlo a los ojos es más difícil de lo usual."

show evmg kenji_glasses_closed at kenji_mg_out
with charachange

ke "¿Quieres un pequeño dato? La gente con ojos pequeños usa anteojos grandes."

hi "He leído eso en alguna parte. Es porque hacen que tus ojos se vean menos redondos y pequeños."

ke "¿En serio? No sabía eso."

stop music
$ renpy.music.set_volume(0.5, 0.0, channel="sound")
play sound sfx_scratch


scene bg school_gardens
show kenji tsun at center
with locationchange

$ renpy.music.set_volume(1.0, 2.0, channel="sound")

"Él se vuelve a poner sus anteojos, y me siento extrañamente aliviado por un momento hasta que recuerdo que aún tengo que lidiar con él, con o sin anteojos."

play music music_kenji fadein 2.0

ke "Bueno, en fin… Una vez una chica artista quería pintar mi retrato, creo. Tuve que hablar con ella como cinco veces antes de que comenzara a tener sentido."

"Debe haber sido Rin, supongo."

hi "¿Qué aspecto tenía?"

show kenji neutral
with charachange

ke "No lo sé. Una mujer con sandalias."

"Estaba esperando que dijera algo más específico, como “no tenía brazos”. Rin sí usa sandalias, pero siento que la posibilidad de que haya otra estudiante de arte, con un espíritu libre y que use sandalias además de ella, es razonablemente alta."

show kenji happy
with charachange


ke "Lo estuve pensando, claro. Algún día, después de que queme toda la documentación de que existo, puede que esté bien dejar atrás un retrato, para que la gente pueda verlo y recordar al salvador de la humanidad. Lo necesitarán para modelar la estatua."

show kenji neutral
with charachange

ke "Luego pensé en ello un poco más y tuve que rechazar su idea. Era tentador, pero ella lo quería para una cosa de la escuela. Sería exhibido."

show kenji tsun
with charachange

ke "La gente preguntaría quién era yo, solo que aún no he salvado a la sociedad, así que no tendría sentido. Y luego si alguien me reconocía, tendría que dar explicaciones."

ke "Esa ya es una cadena de eventos con la que no quiero lidiar. No quiero verme metido en una situación extraña; mierda como esa siempre pasa. Sobresalir es una manera segura de ser incluido en una lista."

show kenji neutral
with charachange

ke "Es por eso que hago un esfuerzo tan cuidadoso al mezclarme con la gente en mi vida diaria. Hasta que pueda hacer mi jugada."

hi "Claro."

hi "¿Qué lista?"

ke "Hay muchas listas."

show kenji happy
with charachange

ke "¿Y qué estás haciendo aquí, de todos modos?"

hi "Nada. Como que llegué aquí por accidente."

ke "Me pasa todo el tiempo. Bueno, espero que funcione para ti. Creo que voy a regresar a mi habitación. Necesito configurar mi TV para grabar mis programas."

hi "¿Tienes TV?"


ke "Sí, deberías venir en algún momento, podemos ver el juego. En alta definición."

stop music fadeout 4.0

hide kenji
with charaexit


"Antes de que pueda preguntarle de qué está hablando, se ha ido. Se fue como vino: sin respeto hacia las otras personas. Algo sorprendente."

"Ahora que Kenji se ha ido, continúo mirando sin rumbo fijo los jardines de la escuela en su esplendor de verano. No sirve de nada, él los arruinó para mí."

scene bg school_cafeteria
with locationchange

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 1.0

"Cuando regreso a la cafetería, agotado pero vivo, pienso en almorzar con Shizune de nuevo, pero la encuentro ya sentada en una mesa con Misha."

"Si fuera alguien más, pensaría en lo lejos que estarían como para que yo las escuche. Sin embargo, son Shizune y Misha."

"Si yo quisiera, podría “escuchar a escondidas” su conversación fácilmente. Qué cosa sucia para pensar, pero está allí… Sin embargo, no quiero."

"Deben tener mucho de qué ponerse al tanto, aun si solo han pasado algunos días. Estoy inclinado a dejarlas solas para que puedan hacer eso."

"Sin embargo, en el instante en que me ven, ellas me hacen un gesto."

show misha hips_grin at twoleft
show shizu basic_normal at tworight
with charaenter

stop ambient fadeout 5.0
play music music_shizune fadein 1.0

mi "¡Hola, Hicchan~!"

"Oír su voz de nuevo incluso después de tan poco tiempo separados es chirriante, y hago una mueca de dolor."

"En estos últimos días, había olvidado que la comunicación con Shizune es casi completamente en silencio, y al concentrarme en hacerlo bien, me había desconectado hasta del ruido del ambiente."

"Bueno, me acostumbraré a ello de nuevo. Me alegra que ella haya vuelto."

show misha sign_smile
with charachange

mi "¡Terminé de ponerme al día con mis trabajos~! Justo a tiempo~, no tendré que perderme el festival. Guajaja~."

show shizu adjust_smug
with charachange

ssh "Si ellos realmente intentaran imponer eso, te sacaría del oficio del consejo estudiantil."

show misha perky_confused
with charachange

mi "Si ellos realmente, realmente intentaran imponer eso, ¿me sacarías del oficio del consejo estudiantil~?"

hi "Eso es abuso de poder."

show shizu behind_frown
with charachange

shi "…"

show misha hips_frown
with charachange

mi "¡No, no lo es, Hicchan~!"

show misha sign_smile
with charachange

mi "Shicchan dice que si hubiera solo dos miembros del consejo estudiantil supervisando el festival, sería un problema, ¿no es así? ¡Sí~, definitivamente! ¡Tienen que ser por lo menos tres! ¡Es por el bien de todos, es perfectamente razonable, es necesario~!"

show shizu adjust_happy
show misha perky_smile
with charachange

"Shizune se inclina un poco sobre la mesa mientras Misha entregaba sus justificaciones ligeramente inquietantes y militarísticas, en un tono infantil, alegre y con altibajos."

"Sin embargo, Shizune se ve tan feliz, juntando sus dedos e intentando contener la risa mientras Misha hacía pucheros más seriamente en su nombre."

hi "Si tú lo dices."

"Estoy realmente feliz ahora mismo, de que podamos hablar tan fácilmente entre nosotros. Todos los tres."

"Al comienzo pensé que podría haberme encontrado en una mala situación. Estaba seguro de que Shizune odiaría tener que cargar con ser la guía turística para el chico nuevo."

"Yo tampoco quería ser ese tipo de carga. También sería incómodo incluso si ella no fuera sordomuda."

"Justo ahora, ella dijo que todos tendríamos que estar en el festival, todo el consejo estudiantil. No creo que el consejo estudiantil tenga alguna jurisdicción real sobre Tanabata. Es solo la manera de Shizune de decir que quiere que lo pasemos juntos."

"Es bueno tener amigos."

"Es un pensamiento simple, pero uno que me hace realmente feliz, que pudiéramos terminar siendo algo así tan fácilmente. A pesar de la manera indirecta como lo dijo, me alegra que Shizune lo piense con tanta firmeza como para expresarlo en absoluto."

show shizu basic_normal
with charachange

ssh "¿Por qué esperaste hasta que te saludáramos para venir a sentarte con nosotras?"

"Una pregunta de la nada. Los ojos de Shizune están expectantes mientras Misha repite su mensaje. Tengo ganas de provocarla."

hi "¿Quieres desesperadamente que me siente contigo?"

show shizu behind_blank
with charachange

ssh "Estamos en el consejo estudiantil. Deberíamos sentarnos juntos tanto como sea posible. Es lógica."

show shizu adjust_happy
with charachange

ssh "Cualquiera saltaría ante la oportunidad de sentarse con dos chicas lindas, de todos modos."

"Ella hace una pausa, en caso de que yo pueda decir algo como “¡No eres tan linda!” e instantáneamente me encierre en una obvia situación sin salida. Cuando no muerdo el anzuelo, Shizune se vuelve más enérgica y continúa."

show shizu basic_happy
with charachange

ssh "Eres anormal."

"Bueno, no esperaba que ella terminara así."

hi "Eres muy rápida en llamar anormales a otras personas. Qué arrogante."

show shizu adjust_smug
with charachange

ssh "Eres muy rápido en llamar arrogantes a otras personas. Eso te hace arrogante, y la arrogancia también es anormal. Eres doble anormal."

hi "Eso no funciona así. Es una escala variable."

show misha hips_grin
with charachange

mi "Jajaja~."

"Apoyándose sobre su brazo, Misha cierra sus ojos y deja salir una risa baja y lenta, como una risa entre dientes."

hi "No te rías…"

show shizu behind_blank
with charachange

ssh "No te rías en este tipo de situación."

"Noto que Misha hace señas de todo lo que le digo a Shizune de todos modos, aunque yo mismo estoy haciendo señas. Esto es redundante, pero es una acción inconsciente para Misha. Por otro lado, no puedo parar."

"Si me permito relajarme y hacer menos señas solo porque Misha regresó, ¿entonces para qué fue todo esto? Tampoco quiero arriesgarme a perder la familiaridad con cómo hacer señas. Ahora mismo mis manos son bastante lentas para hablar por mí."

show misha sign_smile
with charachange

mi "Hicchan, ¡Shicchan y tú se hablan entre sí mucho más ahora~! De aquí para allá, ¡también es muy divertido! Como un viejo matrimonio, ¿cierto~ cierto~?"

"Qué comentario tan cargado, en tantos sentidos. Aunque, debido a que es Misha, no puede haber sido a propósito."

hi "Eso no es un cumplido."

"Shizune no reacciona al intento de Misha de emparejarnos a nosotros dos. Quizá no lo vio. A veces ocurre, lo he notado. Todavía me pregunto si en realidad es así de simple, y por qué me importa tanto, pero no quiero pensar demasiado en eso."

"Quiero irme. Sigo pensando que estoy acaparando el tiempo de Misha con Shizune, y podría ser que Misha interrumpiera justo ahora a propósito, sintiéndose también así. Pero dudo que ellas dejen que me vaya. En ciertos sentidos son demasiado amables."

hi "Bueno, Shizune, si realmente quieres saberlo, no quería sentarme aquí porque no quería entrometerme."

hi "Pensé que porque Misha estuvo ausente por lecciones suplementarias o lo que sea, ustedes dos tendrían mucho de qué hablar, y debería dejarlas solas para que se pusieran al día. Por eso pensé en quedarme atrás."

hi "No te preocupes, Misha, no estoy intentando monopolizar a Shizune."

show misha cross_laugh
with charachange

mi "¡Guajaja~! ¡Hicchan! No es eso~."

show shizu basic_normal
with charachange

shi "…"

show misha hips_smile
with charachange

mi "¡Eres tan considerado, Hicchan! Shicchan lo siente~ y se disculpa."

hi "Realmente no creo que valga la pena disculparse, entonces, no te preocupes por ello. Oigan, ¿no creen ustedes dos que, ya que Misha regresó, deberíamos ir a celebrarlo de alguna manera? Eso pienso."

show misha cross_frown
with charachange

mi "¡Hicchan~! Normalmente, tener que ponerse al día con los trabajos no es algo para celebrar."

show shizu adjust_happy
with charachange

ssh "No, es una buena idea."

hi "El momento es perfecto, y Shizune dijo que el consejo estudiantil también debería divertirse un poco a veces. Probablemente has escuchado eso también, ¿cierto, Misha? Debería estar bien."

show shizu behind_blank
with charachange

shi "…"

hi "De hecho, esperen un segundo. ¿No tuviste que ponerte al día porque faltaste a tantas clases para comenzar?"

hi "Entonces, faltar a clases para celebrar sería algo estúpido. Tal vez el momento no es perfecto, como dije, pero podríamos ir después de la escuela."

show misha sign_smile
with charachange

mi "¿A dónde deberíamos ir?"

"Misha dice la pregunta de Shizune en voz alta antes incluso de que se detenga a pensarlo, ambas ignorándome por completo."


hi "¡Oigan, escúchenme, equipo de dos personas cortas de vista del consejo estudiantil!"

show shizu adjust_smug
with charachange

shi "…"

show misha hips_grin
with charachange

mi "¡Guajaja~! ¡Hicchan, tú también eres parte de este equipo!"

hi "Ah, sí. Supongo que lo soy."

show misha hips_smile
with charachange

mi "¡Sí sí~! ¡Lo eres, Hicchan!"

show shizu behind_smile
with charachange

ssh "Tan olvidadizo, y problemático. Siento pena por la chica que se enamore de ti."

show misha sign_smile
with charachange

mi "¡Entonces~! ¿A dónde creen que deberíamos ir?"

"Estoy riendo a pesar de mí mismo, esperando señalar cómo Misha parece tan entusiasta ahora, cuando ella era la que estaba más inquieta al respecto hace unos segundos. Por cualquier razón, no puedo obligarme a hacerlo. Pero, también está bien."

stop music fadeout 4.0

"Después de una corta discusión sobre a dónde ir, parece que el único lugar que todos los tres conocemos y al que estamos dispuestos a viajar es el Shanghái."

"Una casa de té no parece un mal lugar para celebrar, especialmente porque estoy seguro de que venden pastel allí, y el pastel es la comida más festiva."

scene bg suburb_shanghaiext
with shorttimeskip

"Además, no he visto a Yuuko por un tiempo, y las chicas tampoco. Por todas estas razones, además del hecho de que es tan cerca, termino de pie enfrente de la pequeña tienda de té con Shizune y Misha antes de que lo sepa."

play sound sfx_storebell

scene bg suburb_shanghaiint
with locationchange

show yuukoshang neutral_down at center
with charaenter

yu "¡Bienvenidos!"

play music music_dreamy fadein 2.0

"Ha pasado un tiempo desde que oí la voz de Yuuko, así que estoy sorprendido de nuevo por la energía que pone en sus saludos. Algo así como una Misha extremadamente nerviosa."

show yuukoshang neutral_down at tworight
show bg suburb_shanghaiint at bgright
with charamove

show misha perky_smile at twoleft
with charaenter

mi "¡Hola~! ¡Pero~! No tienes que hacer eso todo el tiempo si solo somos nosotros."

show yuukoshang worried_up
with charachange

yu "Sí tengo…"

show misha sign_confused
with charachange

mi "Pero—"

show misha cross_laugh
with charachange

mi "¡Está bien~! ¡Está bien~! ¡Si tú lo dices, Yuuko! ¡Jajajajaja~!"

"Aprovecho este momento para echar un vistazo alrededor de la casa de té y noto que está tan vacía como siempre. Es hora del almuerzo; básicamente la hora pico para un establecimiento de este tipo."

"Sin embargo, está tan baldío como siempre. Tiene que haber una razón para esto."

show yuukoshang worried_up at center
show misha hips_smile at left
show bg suburb_shanghaiint at center
with dissolvecharamove

show shizu behind_blank_close:
    yalign 1.0 xpos 1.0 xanchor 0.8
with charaenter

"Shizune suavemente me da un golpecito en mi brazo para llamar mi atención."

show shizu adjust_happy_close
with charachange

ssh "¿Qué quieres pedir?"

show yuukoshang neurotic_up
with charachange

"Yuuko se ve un poco agitada después de que Misha automáticamente transmite la pregunta."

yu "N-no, se supone que yo… pregunte eso… ¿Hay algo que pueda hacer por ustedes?"


show shizu behind_smile_close:
    ypos 1.1
show misha perky_smile:
    ypos 1.14
with dissolvecharamove


hi "Solo un poco de café por ahora, supongo. Gracias."

show yuukoshang neutral_down
with charachange

"La dedicación que Yuuko tiene hacia sus deberes como mesera es algo admirable. También lo es la velocidad con la que ella lleva rápidamente las rebanadas de pastel y nuestras bebidas a nuestra mesa cuando ordenamos."

hide yuukoshang
with charachange

show shizu behind_smile_close:
    closeright
    ypos 1.1
show misha perky_smile:
    twoleft
    ypos 1.14
with charamove

"Nuevamente, somos los únicos clientes aquí. Quién sabe cómo sería estando el lugar lleno."

"Shizune y Misha inmediatamente engullen sus pasteles con deleite, probablemente porque no pueden hablar con utensilios en sus manos."

"El propósito de compartir una comida con amigos como esta es poder hablar sobre ella, después de todo. Tiene sentido que fuese igual con ellas."

"Apenas estoy a la mitad de mi pastel cuando oigo sus tenedores tintinear mientras los ponen sobre sus platos vacíos."

hi "No es saludable inhalar tu comida."

show misha hips_grin
with charachange

mi "¡Jajaja~! ¡Hicchan suena como un anciano~!"

"Me avergüenzo y de inmediato siento como si hubiera sido golpeado."

show shizu adjust_happy_close
with charachange

shi "…"

show misha sign_smile
with charachange

mi "¿Vas a usar un yukata mañana, Hicchan?"

hi "No, ni siquiera tengo uno. Bueno, aunque lo tuviera, no soy el tipo de chico que hace cosas como esa."

hi "¿Qué hay de ustedes? ¿Ustedes dos van a arreglarse?"

show shizu behind_blank_close
show misha perky_smile
with charachange

ssh "Por supuesto."

hi "¿Qué quieres decir con “por supuesto”? No te arreglaste la última vez."

show shizu basic_normal2_close
with charachange

ssh "¡Una vez no es una tendencia! Es una situación completamente diferente, de todos modos. Aparte de no ser Tanabata, el festival fue en el campus de la escuela; los estudiantes deben usar su uniforme en el campus de la escuela."

"Claramente una broma, pero su entrega no es nada diferente de lo habitual. Eso no es normal, pero su sentido del humor nunca lo fue, y estoy acostumbrado a ello."

"Supongo que su manera de decir cosas escandalosas en serio es un poco mejor que si ella fuera a decir cosas serias escandalosamente."

"Lo que es más problemático en todo caso, es que he comenzado a asociar una voz con sus señas, y está chocando con cómo Misha dice en voz alta todo lo que Shizune gesticula de todos modos. Me siento desorientado."

show shizu behind_smile_close
with charachange

ssh "¡Me arreglaré esta vez!"

show misha sign_smile
with charachange

mi "¡Me arreglaré esta vez~! ¡Ya verás, Hicchan!"

show misha hips_smile
with charachange

mi "¡No solo Shicchan, sino también yo~!"

show misha hips_grin
with charachange

mi "Tal vez~ voy a cambiar mi peinado, también."

hi "No hagas eso, de verdad no puedo imaginarte con un aspecto diferente."

show shizu adjust_happy_close
with charachange

"Shizune menea un dedo y sonríe."

show shizu adjust_smug_close
with charachange

ssh "Qué desaprobación tan rápida y firme. ¿Qué tal si yo fuera a cambiar mi peinado?"

hi "Quizá deberías dejarte crecer el cabello y hacer que se vea como rizos."

show shizu behind_blank_close:
    xpos 1.0 xanchor 0.8
show misha hips_smile:
    left
    ypos 1.14
with dissolvecharamove

show yuukoshang neutral_up at center behind misha
with charaenter

"Ella no parece alegrarse. Afortunadamente, veo a Yuuko acercarse, probablemente para recoger nuestros platos o preguntar si necesitamos algo de ella."

hi "Yuuko, ¿vas a hacer algo para Tanabata?"

show yuukoshang panic_up
with charachange

yu "¿Eh?"

"Es como si ella estuviera practicando cómo preguntar más fluidamente si yo necesitaba otra taza de café mientras venía, pero no tiene idea de qué hacer cuando le hacen una pregunta primero. Me siento mal."

show yuukoshang worried_down
with charachange

yu "Sí, voy a… trabajar…"

show misha perky_sad
with charachange

mi "Yuuko~, ¿te hacen trabajar en días festivos? Ooooh…"

show yuukoshang neutral_down
with charachange

yu "T-tenemos la mayoría de las ventas en días festivos, y a veces turistas. No me importa. Tengo que hacer mi mejor esfuerzo."

show shizu adjust_happy_close
show misha perky_smile
with charachange

ssh "Entiendo completamente. Qué admirable."

"Shizune asiente con su cabeza en solidaridad, sintiendo una especie de afinidad con Yuuko a través de su determinación común de ser la mejor."

"Sin embargo, para Shizune es un asunto de orgullo mientras que para Yuuko podría sentirse que ella realmente necesita este trabajo y quizás un aumento."

hi "¿La mayoría de las ventas, eh? Así que, ¿cuántas personas en promedio durante un día festivo?"

show yuukoshang neurotic_up
with charachange

yu "Ah, bueno…"

show yuukoshang worried_up
with charachange

yu "…"

hide yuukoshang
with charaexit

show shizu behind_smile_close:
    closeright
    ypos 1.1
show misha perky_smile:
    twoleft
    ypos 1.14
with dissolvecharamove

"Yuuko se aleja y comienza a limpiar un vaso de varillas de coctel. Eso no es cortés. ¡Esto no es lo que haría una verdadera mesera! Sin embargo, en cierto modo ya obtuve mi respuesta. Claramente, las ventas son escasas como mucho."

"Comienzo a preguntarme de nuevo cómo el Shanghái permanece abierto."

"Tal vez este estilo ecléctico de casa de té es una tendencia que era escandalosamente exitosa antes de que yo llegara aquí pero que ya no lo es, y solo lo están manteniendo así mientras remodelan."

"Quizás el dueño es rico y está metido en algún tipo de apuesta con alguien más o en un esquema loco para ver quién puede perder más dinero. Quizás convenientemente me pierdo por segundos de las multitudes de clientes en cada visita."

"O tal vez este lugar es simplemente una fachada para traficantes de armas."

hi "Ya que no hay nadie más aquí, ¿por qué no te sientas con nosotros?"

"Podemos hablar sobre la inviabilidad económica… Pero Yuuko no muerde el anzuelo, moviendo su cabeza de lado a lado enfáticamente."

show misha hips_grin
with charachange

mi "¡En realidad nunca he celebrado Tanabata antes, ni me he arreglado para algo así~! Finalmente podré usar mi yukata. ¡Viva viva~!"

hi "¿Qué quieres decir con nunca? ¿Qué hay del año pasado?"

show misha sign_smile
with charachange

mi "Hm~… ¡el año pasado, Shicchan, la representante de la clase 3-2 y yo dirigimos un puesto para el festival! ¿Fue un puesto de soba, creo~? ¡Sí, lo fue~! ¡Síp!"

show shizu adjust_blush_close
with charachange

"La representante de la clase 3-2 de ciegos debe ser Lilly. Estoy sorprendido de que pudieran trabajar juntas en algo, pero Misha probablemente sería la mejor mediadora para ese tipo de cosas, con lo inocente que es."

show misha hips_grin
with charachange

mi "¡Shicchan cocinaba, y Lilly tomaba las órdenes, y yo las traducía para ellas~!"

show misha hips_smile
with charachange


mi "Shicchan seguía diciendo, “¡Es tan ineficiente~! ¡Misha~! ¿Por qué tienes que ser la intermediaria? Mejor dicho~, ¿por qué hay una intermediaria en primer lugar? ¿Eh~? ¡Estaría bien si yo cocinara y tú tomaras las órdenes! ¡Esto no tiene ningún sentido!”."

show misha sign_smile
with charachange

mi "¡Pero~! Creo que todos se divirtieron al final. ¿Cierto, Shicchan~?"

show shizu behind_frustrated_close
with charachange

shi "… … …"

"Shizune ajusta sus anteojos de mala gana, causando que Misha estalle en risas."

show misha hips_grin
with charachange

mi "¡Fue idea del viejo consejo estudiantil~! ¡Por eso fue~!"

hi "Así que, ¿cómo era el anterior consejo estudiantil, entonces?"

"Shizune finalmente decide intervenir otra vez, o es más como que ella no puede detenerse."

show shizu basic_angry_close
with charachange

ssh "Terrible."

"Eso fue directo. Ella termina con un movimiento de corte, como si emitiera juicio sobre ellos. Espero que ella explique un poco."

show shizu adjust_angry_close
with charachange

shi "…"

show misha sign_confused
with charachange

mi "¡En las universidades y en algunas escuelas privadas, los consejos estudiantiles pueden tener control sobre millones de yenes para presupuesto y se distribuye como sea necesario!"

mi "¡Vaya~! ¿En serio? ¿Millones? ¡Ah, cierto~! ¡Y también están mucho más involucrados en las actividades escolares, Hicchan!"

"Por el tono de Misha, parece que esto es más nuevo para ella que para mí."

show misha hips_frown
with charachange


mi "¡El consejo estudiantil de esta escuela era un chiste en comparación~! ¡No le das a la gente posiciones de poder si no tienen poder en absoluto! ¿Cuál es el punto~?"

show shizu behind_blank_close
with charachange

ssh "Entonces…"

show misha sign_smile
with charachange

mi "¡… quería que tuviéramos más y más trabajo~! Fue difícil convencer a la escuela y a los otros miembros del consejo estudiantil para que lo permitieran."

mi "De hecho~, mucho del trabajo que nos has visto hacer en realidad es trabajo que yo asumí, lo cual era de lo que Lilly estaba hablando."

show misha hips_grin
with charachange

mi "¡Si no fuera por Shicchan, el consejo estudiantil simplemente archivaría reportes de asistencia todos los días~!"

show misha cross_laugh
with charachange

mi "¡Jajaja~! ¿Preferirías eso, Hicchan?"

show misha sign_smile
with charachange

mi "Por supuesto, Hicchan, tan pronto como la carga de trabajo comenzó a aumentar, la mayoría del consejo estudiantil dejó de venir."

show misha hips_laugh
with charachange

mi "¡Guajajaja~!"

show shizu basic_normal2_close
show misha hips_smile
with charachange

shi "…"

"Los dedos de Shizune se doblan sobre sí cuidadosamente. Parece que quiere añadir algo, pero no se atreve a hacerlo."

"Como ella dijo, el lenguaje de señas te da un poco más de tiempo para pensar en lo que “dices”. Supongo que ella siente que no puede hablar sobre esto."

show shizu behind_blank_close
with charachange

ssh "Eso fue entonces, y esto es ahora. Vamos a divertirnos mañana."

"Eso es con lo que finalmente se decide."

hi "Sí."

show shizu adjust_happy_close
with charachange

shi "…"

show misha perky_smile
with charachange

stop music fadeout 5.0

mi "¡Muy bien~! ¡Entonces, el consejo estudiantil es ¿a-pla-za-do? por hoy~!"

show misha hips_grin
with charachange

mi "Tiene que ser aplazado de manera emocionante, porque hoy fue un buen día."

show misha cross_laugh
with charachange

mi "¡Ajajaja~!"

scene bg school_road_ss
with shorttimeskip

"La escuela parece haber terminado para el momento en que dejamos la casa de té, ya que puedo ver estudiantes que bajan de la escuela mientras subimos por el camino hacia ella."

"Un par de personas que usan nuestro uniforme miran a Shizune cuando pasan por su lado, y me pregunto si la reconocen como la presidenta del consejo estudiantil o si sus ojos solo están siendo atraídos a la cabeza de Misha."

"Es imposible no oír las charlas en el aire, y el tema es, la mayoría de las veces, planes para Tanabata. Me pregunto cuántos de ellos estarán usando o van a ir a los puestos que volví a montar."

"Me hace sentir un poco de orgullo, una emoción que nunca he sentido haciendo algo para la escuela."

"Tal vez así es como se siente Shizune también. Casi quiero preguntar, pero parece estúpido querer hacerlo."

scene bg school_courtyard_ss
with locationskip

"Así que solo me aferro a la idea mientras nosotros tres caminamos hacia el campus y luego nos separamos; Shizune al salón del consejo estudiantil, y Misha y yo a nuestras habitaciones."

"No es hasta que ellas se han ido, que me doy cuenta de que nuevamente no les pregunté cuándo y dónde querían que nos encontráramos mañana."

$ suppress_window_after_timeskip = True

scene black
with dissolve


label es_S16:

window hide None

scene black
with dissolve

scene bg school_dormhisao
with openeye

window show

"Aunque es un día festivo, despierto a la misma hora de siempre, en un día cuando todos los demás probablemente estarán durmiendo por otras seis horas."

play music music_pearly fadein 3.0

"Me tomo mi régimen matutino de píldoras por primera vez en unos días. La verdad es que dejé que se me olvidaran mis medicamentos. Mirando las filas de frascos enfrente de mí, no sé cómo pude hacerlo."

"Diecisiete medicamentos diferentes. Me siento lo bastante lleno como para saltarme el desayuno después de tomarlos todos."

"Ya estoy levantado, así que bien podría salir a caminar."

scene bg school_dormext_full
with locationskip

"El clima se ve agradable afuera, emanando una atmósfera idílica con la que a menudo había soñado."

"Para mí siempre ha sido una especie de noción romántica el poder deambular alrededor del campo, tomando el aire fresco."

"Ahora que la oportunidad para hacer precisamente eso está aquí, no puedo resistirme, aunque sé que debe parecer tonto."

scene bg school_courtyard
with locationchange

"Me detengo en el edificio principal para comprar una bebida, y luego decido entrar en él y tal vez rondar un poco por la azotea."

"La vista puede ser bastante asombrosa a esta hora, y también estoy seguro de que nadie más estará allí arriba. Y nunca he estado allí arriba solo."

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 1.0

scene bg school_staircase1
with locationchange

"La escuela está tranquila hoy. Desierta. Mis pasos haciendo eco en la escalera hacia la azotea son inquietantemente fuertes."

"No debería molestarme debido al tiempo que he pasado en las clases de lenguaje de señas en el silencio casi total, o por trabajar tanto con Shizune últimamente, pero aún me molesta."

"Hace que los ruidos más pequeños que ni siquiera habría notado antes parezcan estruendosamente fuertes. Se siente como si estuviera husmeando en algún lugar en el que no debería estar."

"Me pregunto por qué estoy teniendo esa sensación. Tal vez la escuela está embrujada o algo así."

play sound sfx_door_creak
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")
stop music fadeout 3.0

scene bg school_roof at left
with locationchange

"Cuando abro la puerta a la azotea, veo que no estoy solo. Misha se apoya contra la cerca, observando el campus de la escuela, no habiéndome notado en absoluto."

"Al instante, sé lo que tengo que hacer: tengo que poner mis manos sobre sus ojos y decir “¿Adivina quién?”. Es la única opción."

"A mitad de camino, comienzo a pensar en lo mal que esto se vería si Shizune apareciera de repente, habiéndose ido solo por un segundo para traer unos emparedados, y me viera acercándome sigilosamente a Misha de esta manera."

"Rezo en silencio para que tal malentendido casual no ocurra."

show bg school_roof at right
with charamove

hi "¿Adivina quién?"

mi "¡Hicchan!"

"Ella dice, sin dudarlo por un segundo, sin desviarse ni ligeramente de su tono normal. Mi diversión había terminado antes de que comenzara."

play music music_soothing fadein 1.0

show misha hips_grin_close at Slide(0.6, 0.5, 0.5, 0.5, 0.5)
with charaenter

mi "¡Hola, Hicchan! ¡Buenos días~!"

show misha sign_confused_close at center
with charachange

"Ella instintivamente trata de mover sus manos para formar un saludo y se le enredan en el cercado."

hi "Buenos días. No esperaba encontrarte aquí. ¿Qué estás haciendo levantada tan temprano?"

show misha perky_smile_close
with charachange

mi "¡Podría preguntarte lo mismo, Hicchan! ¿Qué estás haciendo levantado tan temprano? ¡No esperaba encontrarte aquí~!"

hi "Yo te pregunté primero."

show misha hips_grin_close
with charachange

mi "Hm~… tienes razón. ¡Guajaja~!"

show misha sign_smile_close
with charachange

mi "Suenas igual que Shicchan."

hi "No, no es cierto."

"… Digo, de la manera menos convincente posible. Afortunadamente, Misha no nota lo mal actor que soy."

hi "¿Estás esperando lo de esta noche?"

show misha hips_smile_close
with charachange

mi "¡Por supuesto, Hicchan~! No me gustan las celebraciones, o tal vez no tanto como a Shicchan, pero los puestos en Tanabata siempre tienen cosas interesantes para comprar y toda clase de platos de temporada. ¡Y~! ¡Puedo vestir un yukata~!"

"Su elección de palabras es un poco extraña. Suena como si estuviera diciendo que no le gustan las celebraciones, pero le gusta hacer todo lo relacionado con ellas. Sin embargo, no sé si valga la pena insistir, y podría ser que simplemente malentendí."

show misha perky_smile_close
with charachange

mi "¿Qué hay de ti, Hicchan~?"

hi "Lo estoy esperando, de lo contrario me quedaría en casa, ¿no es así? Ese es el paso lógico."

show misha hips_grin_close
with charachange

mi "¡Ajaja~! ¡Hicchan, tú no eres tan lógico~! ¡Así que~! ¡Es muy sorprendente! Hm, pero, muy bien. Solo estaba asegurándome, porque no parecía que te hubieras divertido mucho la última vez. Shicchan y yo estábamos un poco preocupadas por eso."

hi "Oye, me divertí. Supongo que terminé apreciándolo más de lo que esperaba."

show misha perky_smile_close
with charachange

mi "¿En serio, Hicchan~? ¡Guajajaja~! ¿Cuál parte del festival? ¡Dime~!"

hi "Bueno, hubo fuegos artificiales al final. Fueron… muy bonitos."


hi "Creo que te dormiste durante ellos."

show misha hips_smile_close
with charachange

mi "Oh~… Siempre me quedo dormida temprano. ¡Pero~! ¡No me dormiré durante ellos este año! ¡Definitivamente me quedaré despierta!"

hi "No creo que haya fuegos artificiales durante Tanabata. Es un ambiente completamente diferente."


hi "Sin embargo, tal vez puedas hacer que Shizune les solicite que los pongan. Y que muevan los fuegos artificiales a una hora más temprana."

show misha cross_laugh_close
with charachange

mi "¡Jajajajajaja~! ¡Tal vez lo haga~! ¡Esa es una gran idea, Hicchan!"

hi "¡Ah, no, no, no lo es! No hagas eso. No estaba hablando en serio."

hi "Aunque… tal vez eso molestaría a Shicc— Shizune."

show misha hips_grin_close
with charachange

mi "Guajaja~. Lo haces sonar como si quisieras eso, Hicchan."

show misha cross_smile_close
with charachange

mi "¡Hicchan~! ¿Te gusta Shicchan?"

"No puedo decir sí o no, y, sentado como estoy, ni siquiera puedo irme tranquilamente."

hi "No seas tonta; la que me gusta eres tú."

show misha perky_smile_close
with charachange

mi "¡Ajajaja~! ¿En serio, Hicchan? ¡Hm~! No, estás bromeando, ¿cierto? Te debe gustar más Shicchan."

hi "Misha, sacas muchas conclusiones precipitadas."

show misha sign_smile_close
with charachange

mi "¡Pero casi la llamaste Shicchan! ¡Entonces~! Tengo razón, ¿cierto~?"

hi "Es porque tú la llamas Shicchan todo el tiempo. Se me atascó en la cabeza. Aprender lenguaje por ósmosis es común, ¿sabes? Además, es un pequeño lapsus."

hi "Y por tu lógica, ella debería gustarte más que a mí. Y… ¿te estás burlando de mí o algo así?"

show misha cross_laugh_close
with charachange

mi "¡Guajaja~!"

show misha perky_smile_close
with charachange

mi "Tal vez~."

show misha hips_smile_close
with charachange

mi "Tengo hambre. ¿Has desayunado, Hicchan?"

hi "No. Solo medicamentos."

show misha sign_confused_close
with charachange

mi "Hm…"

"Misha hace girar su dedo perezosamente en el aire para mantener sus manos ocupadas."

show misha hips_grin_close
with charachange

mi "¡Deberíamos comer algo, entonces~! ¿Crees que aún estén sirviendo el desayuno hoy?"

"Eso es realmente el tipo de cosa que un miembro del consejo estudiantil debería saber. Sin embargo, no puedo decir eso. Estoy en el consejo estudiantil y no lo sé."

hi "No parecía que alguien estuviera trabajando en la cocina cuando entré al edificio, pero no lo sé con certeza."

show misha perky_smile_close
with charachange

mi "Oye, Hicchan, ¿alguna vez has escuchado de esas máquinas expendedoras de donde puedes conseguir comida, como hamburguesas, sopa, y hasta pizza? ¿No sería genial si tuviéramos algunas de esas en nuestra escuela~?"

hi "No lo sé, siempre pensé que esas máquinas eran algo raras."

show misha hips_smile_close
with charachange

mi "¡Imagina qué fantástico sería si tuviéramos máquinas como esas en nuestra escuela, Hicchan~! Sería casi como magia, ¿no es así?"

mi "Comida caliente saliendo de una máquina expendedora, eso es tan increíble, nunca podría imaginar eso. ¡Ver una de esas máquinas sería como un sueño!"

show misha perky_sad_close
with charachange

mi "Hm~… Sin embargo, no tenemos máquinas como esa en todo el pueblo~. ¡Es muy temprano para ir incluso al pueblo~! No podré desayunar, Hicchan, esa es la comida más importante del día. ¡Todos lo dicen~! ¡Ah, quiero comer!"

hi "Eres muy tonta. Si te molesta tanto, te compraré una gaseosa."

show misha hips_frown_close
with charachange

"Misha infla sus mejillas y pone su cara seria."

mi "Hicchan, una gaseosa no es un desayuno. Es como agua~."

hi "No es como agua, es un líquido. El agua no es comida. Un líquido puede ser comida."

"“¿Ahora quién suena como Shizune, Misha?”. Quiero decirlo. Incluso su tono me recuerda la manera imperturbable y realista de Shizune de expresar lo ridículo. Pero si dijera eso, yo sería el que sonaría como Shizune de nuevo."

"Es terrible, su competitividad realmente se me está pegando."

hi "Vamos a buscar algo para comer, entonces."

show misha cross_frown_close
with charachange

mi "…"

show misha cross_laugh_close
with charachange

mi "Bueno. ¡Ajajajaja~!"

stop music fadeout 3.0
stop ambient fadeout 1.0

scene bg school_lobby
with locationskip

"Como era de esperarse, nuestra búsqueda por comida en un edificio vacío de la escuela tan temprano en la mañana solo lleva al fracaso."

"Misha decide irse por su cuenta después de que ambos decidimos rendirnos por el momento, prometiendo desayunar aunque por ahora está más cercana la hora para el almuerzo."

scene bg school_dormhisao
with locationskip

"Regreso a mi dormitorio. Las horas siguientes pasan lentamente, y paso el tiempo poniéndome al día con mis lecturas."

show bg school_dormhisao_ni as overlay at Alphain(6.0), center
with None

play music music_dreamy fadein 6.0

"Algunos de estos libros no los he tocado desde que estaba en el hospital. Pensando en ello, no fue hace mucho, aunque definitivamente se siente como si lo fuera."

"Un día libre, y no puedo pensar en nada que hacer. Tomo una corta siesta, y mientras me cambio por segunda vez hoy, me doy cuenta de que de hecho nunca confirmé con Shizune ni con Misha cuándo y dónde nos encontraríamos."

"Supongo que al final ellas vendrían a buscarme, pero me vería muy estúpido si resultara así."

scene bg school_dormhisao_ni
with None

"Ya es de noche, así que debería al menos hacer un esfuerzo por encontrarlas primero."

scene bg school_courtyard_ni
with locationskip

"Aunque el campus no está exactamente inundado de gente y debería ser imposible no ver el cabello rosado de Misha incluso si lo estuviera, tengo mucha dificultad para encontrarlas."

scene bg school_gate_ni
with locationchange

"Finalmente, me encuentro con ellas en el portón, el cual fue el primer lugar que había mirado."

show shizuyu basic_happy_ni at center
with charaenter

ssh "¡Hola!"

"Ella intenta enfatizar su saludo normal con un grandioso movimiento circular pequeño al final."

show shizuyu basic_happy_ni at tworight
show bg school_gate_ni at bgright
with charamove

show misha sign_smile_yuk_ni at twoleft
with charaenter

mi "¡Hicchan~! ¿Cómo estás?"

"Es extraño verlas en yukata, aunque he estado viendo yukatas en general toda la noche."

"El de Shizune es simple y de buen gusto, lo cual parece obvio para ella en retrospectiva. Por todos sus grandes ademanes y su comportamiento exagerado, creo que ella preferiría morir antes que vestirse para la ocasión."

"Lo que llama mi atención es la horquilla que está usando, una flor de perla que brilla suavemente a la luz de la luna."

"Se ve bonito en ella, pero de una manera que también se siente fuera de lugar. Como si fuera demasiado elaborado para una chica de preparatoria, o tal vez solo para alguien tan secretamente infantil como Shizune."

"El yukata de Misha es casi lo que esperaba, así que de hecho le queda muy bien. Combinado con su cabello rosa chicle, se ve linda, pero anacrónica."

hi "Ustedes dos se ven bien."

show misha perky_smile_yuk_ni
with charachange

mi "¡Gracias, Hicchan~!"

show shizuyu cross_angry_ni
with charachange

shi "…"

mi "Hicchan, llegas un poco tarde. Estuvimos esperando un rato por ti, ¿olvidaste la hora o el lugar?"

mi "¡Oh bueno~! ¡Vámonos, Hicchan~!"

show shizuyu cross_happy_ni
with charachange

shi "…"

"Que Misha abandone esta línea de discusión me salva de lo que potencialmente podría ser una cosa bastante embarazosa que admitir; específicamente, que había estado buscándolas durante al menos una hora."

"Mirando a Shizune y a Misha luciendo tan alegres, es difícil no querer caer en la atmósfera y disfrutar de una noche agradable."

"Lo que me molesta es que estoy teniendo algunos problemas leyendo las señas de Shizune esta noche. No he ido a clases de lenguaje de señas en casi una semana, así que no estoy sorprendido."

"Supongo que al haber perdido el enfoque por un tiempo, estoy decayendo. Ciertamente no sería la primera vez."

hi "Esperen, ¿a dónde vamos? ¿Al pueblo?"

show shizuyu basic_happy_ni
with charachange

ssh "Sí."

hi "Eso no tiene ningún sentido. Ni siquiera hemos mirado qué hay en el campus. A menos que ustedes dos hayan decidido divertirse mientras yo no estaba mirando."

show shizuyu cross_happy_ni
with charachange

ssh "Vamos a regresar; estaremos planeando el recorrido."

show misha sign_smile_yuk_ni
with charachange

mi "¡Jajaja~! Sea como sea, Hicchan, tenemos que ir al pueblo y luego regresar si queremos ver todo. ¡Entonces~! De este modo, después de que acabemos, estaremos cerca de nuestras habitaciones cuando estemos cansados. ¡Resulta perfecto~!"

show shizuyu basic_happy_close_ni at closeright
with characlose

stop music fadeout 2.0

"Eso es ciertamente lógico. Shizune no me da mucho tiempo para discutir de todos modos, agarrándome por el brazo e intentando arrastrarme suavemente."

scene ev shizutanabata:
    truecenter zoom 8.0 rotate 45.0 subpixel True
    easein 1.0 zoom 1.1 rotate 0.0
    easein 8.0 zoom 1.0
with locationskip

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_crowd_outdoors fadein 2.0
play music music_ease

"Las calles iluminadas solo por la luz de la luna y las linternas bajas teñidas con papel de seda me tranquilizan."


"Ahora que estamos en el pueblo, Shizune se mueve un poco más despacio para apreciar las vistas."

"Entonces, decido caminar más rápido para fastidiarla, pero ella rápidamente reajusta su propia velocidad para igualar, dejando salir una risa silenciosa antes de hacerle señas rápidamente a Misha con su mano libre."

shi "…"

mi "¿Qué quieres hacer primero, Hicchan~?"

hi "¿Qué tal algunos juegos, si los hay?"

mi "Pensé que no te gustaban los juegos, Hicchan."

hi "No me importa."

"Por segunda vez hoy, siento sus delgados dedos envolviéndose entre los míos. Se siente como si todo este tiempo, he sido arrastrado por voluntad de Shizune. En ocasiones, es bastante agotador, pero creo que en mayor parte, no diría que lo odio."

"Es solo la cualidad de algunas personas para arrastrar a otros a sus vidas, como una tormenta. Esa palabra le queda bien a Shizune a veces, creo. Aunque no quise decírselo a Misha hoy temprano, ella sí me gusta."

mi "Hicchan, vas a ganar una muñeca para mí esta vez, ¿cierto~?"

hi "¿Aún estás pensando en eso? Está bien, lo haré."

$ renpy.music.set_volume(1.0, 2.0, channel="ambient")

scene bg suburb_tanabata_ni at bgright
show nightwash
with shorttimeskip

"El tiempo pasa más rápido de lo que pensé que podría mientras corremos de aquí para allá, intentando hacer tantas cosas frívolas como sea posible."

show misha perky_smile_yuk at center behind nightwash
with charaenter

mi "¡Conos de nieve! Hicchan, ¿quieres uno~?"

"Misha corre hacia el puesto, sin siquiera esperar a escuchar mi respuesta."

show misha perky_smile_yuk at twoleft
show bg suburb_tanabata_ni at center
with charamove

show shizuyu cross_happy_close at closeright behind nightwash
with charachange

ssh "Se ven deliciosos, también quiero uno. Jugaremos piedra, papel o tijera para ver quién puede pagarlos todos."

hi "O… podríamos pagar cada uno por nuestra cuenta."

show misha sign_smile_yuk
with charachange

mi "Hicchan~, ¿qué sabor quieres?"

hi "El azul."

show shizuyu basic_angry_close
with charachange

ssh "Azul no es un sabor."

hi "Ya lo sabía…"

ssh "Ordenar algo basado en el color es infantil."

hi "Tú eres infantil. ¿Qué vas a pedir? ¿Vas a pedir fresa? ¡Ja! Ese es un sabor tan infantil, solo los niños comen fresa."

show shizuyu cross_angry_close
with charachange

ssh "¡Deberías pedir simple, el sabor más maduro de todos!"

"Quiero saber de dónde viene su personalidad. Me pregunto si pensaría así si ella no hubiera sido la primera estudiante con la que terminé teniendo una conversación en mi primer día aquí."

"Es completamente posible que me hubiera perdido las partes de ella que me seguían atrayendo."

"Si no supiera que ella no podía oírme, y que era tan competitiva, y tan enfocada en conseguir que me uniera al consejo estudiantil, y alternativamente tan juguetona y lista…"

"Sin estas nuevas facetas constantes para mantener mi interés en ella, ¿me habría terminado gustando tanto?"

"Es probable que lo esté pensando demasiado."

hi "¿No vas a pedir un deseo?"

show misha perky_confused_yuk
with charachange

mi "¡Shicchan nunca pide deseos, Hicchan!"

hi "¿Oh, en serio? ¿Ni siquiera en Año Nuevo? ¿Y eso por qué?"

show shizuyu basic_happy_close
with charachange

shi "…"

"Shizune junta sus dedos y sonríe, pero no responderá."

ssh "Es un secreto."

show misha sign_smile_yuk
with charachange

mi "¡Yo sé~!"

mi "Hicchan, ¿quieres que te lo diga?"

show shizuyu cross_blush_close
with charachange

shi "¡…!"

hi "Sí."

show shizuyu basic_angry_close
with charachange

"Shizune alterna entre tantas iteraciones enérgicas de “no” de las que puede pensar."

show misha perky_smile_yuk
with charachange

mi "¡Guajaja~! Te lo diré más tarde, ¿bueno?"

show misha perky_sad_yuk
with charachange

stop music fadeout 5.0

mi "En realidad, me siento cansada. Creo que voy a ir a la cama temprano~."

show shizuyu cross_blush_close
with charachange

ssh "¿En serio?"

hi "No se siente como si hubiera sido tanto tiempo."

"El tiempo vuela cuando te diviertes."

show misha sign_smile_yuk
with charachange

mi "¡Pero~! Sí lo ha sido, Hicchan. ¿Tal vez pueda visitar a Yuuko primero, y luego regresar? O~… no lo sé~."

show misha perky_smile_yuk
with charachange

mi "Bueno, eso no importa. Diviértanse sin mí, ¿bueno~?"

hi "Vamos a regresar pronto a la escuela de todos modos, Misha."

hide misha
with charaexit

show shizuyu cross_blush_close at center
show bg suburb_tanabata_ni at bgleft
with charamove

"Misha no quiere oírlo, y se va de todos modos. Shizune comienza a preguntarse por qué tan pronto como yo lo hago, pero mientras yo lo mantengo en mi cabeza, ella lo dice en señas, pareciendo querer discutir las posibles razones."

scene bg suburb_tanabata_ni at bgleft
show nightwash
with shorttimeskip

"Después de que ambos terminamos de ver todo lo que hay que ver, reviso la hora, y descubro que es muy tarde. Mi energía está comenzando a desvanecerse, y es un milagro que haya podido tener tanta, también."

"Incluso Shizune está comenzando a verse un poco cansada. Nos dirigimos de regreso al campus."

stop ambient fadeout 0.5

scene bg school_courtyard_ni
with locationskip

play ambient sfx_cicadas fadein 0.5

"Shizune parece decepcionada cuando ve el edificio de la escuela iluminado y lleno de estudiantes."

his "¿Ocurre algo?"

show shizuyu basic_aside_ni at center
with charaenter

ssh "Quería subir a la azotea, pero ahora hay mucha gente. Estoy cansada, así que podría ser lo mejor."

his "Probablemente hay parejas en la azotea, ya que es ese tipo de festividad."

his "Por otra parte, no lo sabría. ¿Es así como es en realidad? Realmente nunca había estado en algún festival antes de venir aquí."

shi "…"

his "Estoy decepcionado, pensé que dijiste que querías ver lo que estaba haciendo la escuela de último, como guardando lo mejor para el final."

his "¿Ahora me estás diciendo que no quieres? ¿Ni siquiera un poco? Pensé que tendrías más energía. Yo no estoy cansado."

show shizuyu basic_happy_ni
with charachange

"Esto parece despertar su espíritu competitivo, y Shizune inmediatamente se anima, aunque es entonces que me doy cuenta de que no tenía ningún lugar en mente para llevarla, y yo mismo no tengo ganas de ir al edificio principal."

scene bg school_gardens_ni at Fullpan(4.0, dir="right")
with locationchange

"Afortunadamente, el área detrás de la escuela está desierta y se ve impresionante hoy. Nunca había apreciado cuán extensa y bien cuidada estaba hasta verla de noche. Casi parece no terminar nunca a la luz de la luna."

show shizuyu basic_happy_ni at center
show bg school_gardens_ni at right
with charaenter

ssh "Es muy bonito, aunque solo es un campo."


"Había pensado antes que ella era muy inmadura para llevar las ropas anticuadas que está usando esta noche, pero ahora mismo, ella es bastante hermosa en ellas."

"Me hace recordar ese día, el otro festival al que fui con ella. Se veía de la misma manera entonces."

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")
$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_serene fadein 1.0

window hide

nvl clear

nvl show dissolve

n "\nQuiero decirle que me gusta. Decididamente, de un golpe. Pero incluso pensar en ello es tan incómodo."

n "Y entre más me gusta, más incómodo y temeroso estoy de decirle lo que siento, incluso ahora, cuando podría hacerlo si quisiera, sin tener que pasar por otra persona."

n "Sin mencionar, ¿qué tal si lo que ocurrió la última vez vuelve a pasar? Si eso ocurre, puede que no salga tan fácilmente con una estadía en el hospital de meses de duración. Ni siquiera quiero pensar en ello."

n "Intento sacar los pensamientos de mi mente de cualquier forma posible. Intento descartarlos como miedos improbables."

n "Aun así…"

n "La primera vez que había visto todas mis píldoras, las había imaginado cayendo en cascada ante mí, suficientes como para ahogarme."

n "Aún pienso en ello de vez en cuando. No puedo decir que no es una preocupación legítima. Sin embargo, momentos como este son lo bastante agradables como para poder olvidarlo."

nvl clear
nvl hide dissolve

$ renpy.music.set_volume(1.0, 1.0, channel="music")
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene ev shizuconfess_normal
with flash

window show

ssh "Lo que más me gusta de esta escuela es que está en la cima de una montaña."

his "¿Es porque está mucho más cerca del cielo?"

ssh "Sí."

his "También me gusta, pero más por el aire fresco."

his "Eres tan competitiva. Demasiado competitiva. Si una ballena te mordiera, le devolverías el mordisco."

scene ev shizuconfess_smile
with charachange

shi "…"

"Eso la hace reír, y guiña."

ssh "¿Eso sería tan malo?"

"Su sonrisa es contagiosa."

his "Sí."

shi "…"

scene ev shizuconfess_closed
with charachange

ssh "Es cierto. Soy terrible, un poco."

scene ev shizuconfess_smile
with locationchange

ssh "Pero si puedo hacer feliz a la gente, no soy del todo terrible, ¿verdad? Entonces, está bien. Tengo muchos ejemplos en mi defensa."

"Tal vez incluso este momento es una especie de juego para ella."

his "Así es."

stop music fadeout 2.0

"Este es un momento romántico. No sé si una oportunidad así pueda venir de nuevo, y me siento obligado a decir algo embarazoso y estúpido. Si lo pienso demasiado, dudo que mis manos me vayan a escuchar."

his "¿Quieres ser mi novia?"

scene bg school_gardens_ni at right
show shizuyu cross_blush_ni
with locationchange

shi "…"


"Espero haber hecho bien las señas."

"Me siento nervioso; como si quisiera arrancar a correr, pero estoy clavado en este lugar. No podía oír nada hace pocos minutos, ahora estoy captando cada pequeño ruido del ambiente. Realmente estoy nervioso, y me pregunto si se nota."

"Antes, las horas pasaban como segundos. Ahora, los segundos pasan como eones."

show shizuyu basic_blush_ni
with charachange

"Entonces veo las manos de Shizune moviéndose de manera insegura ante ella, frotándose una sobre la otra, deteniéndose a mitad de camino durante cada gesto."

"Es como ella dijo, el lenguaje de señas te da la oportunidad de pensar bien tus palabras, y ella se está esforzando mucho en hacer eso ahora mismo."

"Una situación a la que no sabe cómo responder. Debe ser impensable. Tan estoica como Shizune intenta ser, no puede esconder sus mejillas enrojecidas, y es muy linda y femenina así. Y me tranquiliza saber que ella está tan nerviosa como yo."

"El pensamiento es otra manera en la que me he encontrado compitiendo con ella."

show shizuyu cross_happy_ni
with charachange

ssh "Está bien."

play music music_romance fadein 1.0

show shizuyu basic_happy_close_ni
with characlose

"Esa es una respuesta simple. Pero tan pronto como lo pienso, Shizune da un paso adelante y me abraza."

stop ambient fadeout 3.0

window hide

nvl clear

nvl show dissolve

n "\n\n\n\n\n\n\n\n\nUn abrazo inseguro y cuidadoso, como si yo estuviera hecho de cáscara de huevo, y como si ella no supiera cómo abrazar a alguien. Aunque para ser honesto, es un tema con el que tampoco soy familiar."

n "Su yukata es fresco y sedoso bajo mis dedos, pero también puedo sentir el calor de Shizune."

n "Al final, ella pensó que este es el mejor gesto posible para mostrar lo que sentía."

stop music fadeout 3.0

nvl hide dissolve
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
