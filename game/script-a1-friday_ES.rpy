label es_A25:

window hide None
scene black
with dissolve

play sound sfx_alarmclock

scene bg school_dormhisao
with openeye

window show

"Suena mi despertador, y me sacudo inútilmente por un momento hasta que recuerdo que había decidido darle otra oportunidad a correr por la mañana."

"No sé si esta fue mi mejor idea, pero estoy decidido a seguir adelante."

"Esto se trata de mi salud, después de todo."


"Claro, las cosas no han sido grandiosas para mí últimamente, pero eso no ha hecho mi existencia tan intolerable como para no intentar todo lo posible para mantenerme saludable."


"Además, se trata de ejercer algún tipo de control sobre este asunto, ¿no?"

"Si puedo conseguir eso, bueno, puedo conseguir cualquier cosa."

"Al menos eso es lo que sigo diciéndome."

scene bg school_track
with locationskip

play ambient sfx_emirunning fadein 0.3


"Una vez más, parece que no estoy solo en mi carrera."

"Aparentemente Emi ya ha estado aquí por algún tiempo."

"Y por lo visto ya se ha estado ejercitando desde hace rato."

"A todo esto ¿cuándo demonios es que viene a la pista?"

stop ambient fadeout 0.3

show emi basic_grin_gym at center
with charaenter

play music music_emi fadein 0.5

emi "¡Oh, eres tú!"

show emi basic_closedgrin_gym
with charachange

emi "¡Me sorprende verte otra vez!"

hi "¿Eso por qué?"

show emi basic_grin_gym
with charachange

emi "Bueno, no mucha gente logra regresar para un segundo intento."


show emi basic_annoyed_gym
with charachange

"Ella frunce el ceño, aparentemente molesta por un pensamiento pasajero."

emi "Como el resto del equipo de atletismo, por ejemplo."

emi "Aun así, se suponía que fuera de manera voluntaria, por lo que no es una gran sorpresa."



emi "Y supongo que es demasiado temprano en la mañana…"


"Se encoge de hombros, y repentinamente parece que se ha olvidado de lo que estaba hablando."

show emi basic_happy_gym
with charachange



"El gesto de desagrado desaparece por completo, y parece regresar de un golpe a su anterior línea de pensamiento."

emi "¡Bien! ¡Vamos, entonces!"

hi "¿Qué?"

show emi excited_proud_gym
with charachange

emi "Estás aquí para correr otra vez, ¿verdad?"

hi "Bueno, sí."

show emi basic_closedhappy_gym
with charachange

emi "¡Entonces vamos!"

scene bg school_track_on
with locationchange


"Me encuentro súbitamente agarrado y jalado hacia la pista."

play ambient sfx_emijogging fadein 0.3

scene bg school_track_running
with locationchange


"Las cosas parecen estar acomodadas de forma que reflejen la carrera de ayer."

"Es decir, parezco estar luchando, mientras Emi se mueve con una soltura que encuentro envidiable."

"Es increíblemente molesto, agotarse con tanta facilidad."

"Sé que debería ser paciente, trabajar y avanzar poco a poco, pero…"


"Es difícil mantenerse positivo ante esto."


"Rodeamos la pista y empezamos con nuestra segunda vuelta."

play ambient sfx_emirunning

"Emi parece haberse impacientado manteniendo mi paso, y comienza a alejarse."

"Aquí es donde me rendí el día de ayer."



label es_choiceA25:
menu:
    with menueffect
    "¿Seré capaz de hacer algo más?"
    "¡Adelante!":



        return m1
    "Tomarlo con calma.":

        return m2

label es_A25a:



stop music fadeout 10.0


"Dejo ir a Emi a su propio paso, y ella no muestra piedad, adelantándose media vuelta en un instante."

"No la culpo."

"Quiero decir, no es como si estuviera poniendo algún tipo de pelea verdadera aquí, ¿no?"

"En cambio, solo estoy corriendo a un ritmo constante, que es lo que debería de estar haciendo, ¿cierto?"

"No hay necesidad de andar forzando mis límites en esta etapa del juego."

"Dios, ¿acaso esto vale la pena?"

scene bg school_track_on
with locationchange

"Cuando terminamos la segunda vuelta, me detengo de nuevo."

"Emi continúa, y casi me parece que está decepcionada."

"Bien, eso es estúpido."

"No tengo nada que probarle… ahora que lo pienso, no tengo nada que probarme a mí mismo, tampoco."

"Estoy bien tal y como estoy."

"Y lo que no soy es un corredor."

"Esto probablemente fue una mala idea."

"Tal vez hay algo más que pueda hacer en lugar de esto."

"Levantarse así de temprano apesta, de todas formas. Debe haber otra manera de mantenerse saludable."

"Caminar, tal vez. Agradables caminatas por la tarde."


"Sí, eso suena bien. Correr no es para mí."

stop ambient fadeout 2.0

scene bg school_track
with locationchange

"Me despido de Emi con la mano y regreso a mi habitación."

"Pensaré en algo más en otro momento."





label es_A25b:

"¿Qué estoy haciendo aquí?"


"¿Realmente voy solo a ceder y permitirle a Emi adelantarse?"

scene bg school_track_running
with locationchange

"Apresuro el paso."


"La segunda vuelta es terminada rápidamente, y sin considerarlo dos veces continúo."

"Emi voltea y me mira por sobre su hombro y sonríe."

show emi excited_proud_gym at twoleft
with charaenter

emi "¿Todavía sigues?"

hi "No quisiera *uff* que pensaras *uff* que estoy fuera de forma *puff*."

show emi excited_laugh_gym
with charachange

hide emi
with charamoveoutleft

play ambient sfx_emipacing


"Emi se ríe — sin romper su paso, ni un poco — y acelera aún más."

"Bien, si así es como vamos a jugar…"

"Incremento también mi propio ritmo."

"Puedo sentir mis pulmones ardiendo, y mis piernas comienzan a preguntarse qué diablos pienso que estoy haciendo."

"El ácido láctico suelta alaridos en mis músculos, pero cierro mis oídos."

"No puedo permitirme quedar atrás, porque eso sería una derrota."

"La voz racional dentro de mi cabeza levemente inquiere cuándo fue que empezamos a jugar un juego."

"Le respondería, pero estoy teniendo muchos problemas para pensar en este momento."


"Es {b}demasiado{/b} rápida."

"¿Cómo demonios es que logra mantener—{w=.5}{nw}"

stop music fadeout 0.2

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

"Es como si una cuerda tirara de mi pecho, una ahogadora sensación de estrechez y dolor."

"Antes de que pueda pensar otra cosa además de “Oh mierda”, la pista desaparece de debajo de mis pies."

scene bg school_track_on:
    xalign 0.5 yalign 0.52 rotate 0 zoom 1.0
    linear 0.1 rotate -6 zoom 1.2
with vpunch

"Tropiezo, una mano se dispara para apretar mi pecho, la otra golpea la pista tratando de que no caiga sobre mi cara."

stop ambient fadeout 0.2


"Emi da una vuelta y abre los ojos de par en par."

emi "¡Hisao!"

play ambient sfx_emisprinting

"Ella me grita, corriendo a toda velocidad desde el otro lado de la pista."

show emi basic_shock_gym:
    xalign 0.5 yalign 0.7 rotate -6 zoom 1.2
with charamoveinright

stop ambient fadeout 0.1

emi "¿Qué pasa?"

hi "Nngh—Nada, solo…"

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

"Mantén tu respiración constante."

"Tranquilízate. No entres en pánico."

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

"No entres en pánico."

show emi basic_shock_gym:
    parallel:
        linear 0.2 rotate -12 zoom 1.5
    parallel:
        "emi basic_hes_gym" with Dissolve(0.2, alpha=True)
with None

emi "¿Necesitas que traiga al enfermero?"


show black
with shuteyefast

scene black
with None

"Cierro mis ojos, aislándome del mundo exterior."

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.3)

with Pause(1.0)

play sound sfx_heartslow
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.7)

"Mi corazón se esfuerza por recuperar su ritmo."

"Lentamente, el dolor en mi pecho comienza a disminuir."

"Pronto se va como si nada hubiera ocurrido."

"No era… ¿nada? No, algo sucedió ahí."

play music music_rain fadein 2.0

scene bg school_track_on
show emi basic_hes_gym_close at center
with openeye

"Abro mis ojos y alcanzo a ver a una muy preocupada Emi."

hi "Creo que estoy bien."

"Mi voz suena rara incluso para mí mismo, extraña y flemática. Eso hace que Emi frunza el ceño."

show emi sad_annoyed_gym_close
with charachange

emi "No creo que lo estés."

"Parece que ha tomado una decisión, y se asiente con la cabeza a sí misma."

show emi basic_annoyed_gym_close
with charachange

emi "Sí. Tú te vienes conmigo."

emi "Tienes que ver al enfermero."

with vpunch

"Emi me toma del brazo y me arrastra. Me siento un poco tembloroso, pero me niego a aceptar el hombro ofrecido por Emi como soporte."

"A decir verdad, me avergüenzo un poco de mi propia debilidad."

"Realmente preferiría no haber hecho que Emi se preocupara por mí, pero parece ser demasiado tarde."

"Con un demonio, realmente preferiría no haber hecho que nadie se preocupara por mi condición, pero a estas alturas, parece ser demasiado tarde para eso también."

"Me gustaría ser capaz de lidiar con todo esto por mi cuenta, sin serle una molestia a nadie más."


"Y ya que estoy deseando cosas, preferiría no tener esta afección en primer lugar."

stop music fadeout 1.0

scene bg school_nurseoffice at bgleft
with locationskip

show emi basic_shock_gym at tworight
with easeinright

emi "¡Enfermero!"


"Emi irrumpe dentro de su oficina sin tocar, pero esto no parece alarmar al enfermero de ninguna manera."

play music music_nurse fadein 0.5

show nurse grin at twoleft
with charaenter

nk "Buenos días, mi rayito de sol. ¿Qué pasa?"

"¿Rayito de sol? Como sea, él tranquilamente bebe de su taza de café, pero la pone sobre la mesa después de seguir la mirada de Emi hacia mí, parado en la puerta."

show nurse fabulous
with charachange

nk "¿Hisao? ¿Qué te trae por aquí?"

show emi excited_sad_gym
with charachange

emi "Estábamos corriendo y se tropezó y se agarró del pecho y pensé en venir por usted y hacerlo esperar allá pero dijo que estaba bien pero luego pensé que usted debería de verlo de todas formas y—{w=1.5}{nw}"

show nurse concern
with charachange

nk "Calmada, Emi. Tranquilízate."

show nurse neutral
with charachange

nk "Hisao, ¿qué ocurrió?"

hi "No lo sé. Estábamos corriendo, y luego empezó a dolerme el pecho como aquella vez, pero se fue después de unos segundos."

hi "Fueron solo unas palpitaciones o algo."

show nurse concern
with charachange

"El enfermero frunce el ceño, como para decir que “solo unas palpitaciones” es algún tipo de oxímoron."

nk "No me refería a algo como esto cuando sugerí hacer ejercicio. Tienes que ser más cuidadoso, Hisao."

hi "Estaba siendo cuidadoso, es solo…"

"Ahora que lo pienso, “Solo me metí en una carrera con uno de los miembros del equipo de atletismo” no parece tan razonable como lo había pensado."

nk "¿Es solo qué?"

hi "Eh… quiero decir…"

hi "Estaba compitiendo con Emi."

nk "Emi, ¿es esto cierto?"

show emi basic_hes_gym
with charachange

"Emi se inquieta, viéndose adorablemente arrepentida."

emi "Ah, pues…"

show emi basic_closedsweat_gym
with charachange

"Finalmente parece que no puede forzarse a decirlo en voz alta, y simplemente asiente."

"El enfermero suspira y se frota la frente con una mano cansadamente."

nk "¡Emi, tienes que ser más sensible a los límites de los demás!"

nk "No sé si él te dijo, pero Hisao tiene un corazón malo, y haber hecho que compitiera contigo fue increíblemente irresponsable."

hi "Eeh, de hecho yo empecé."

"El enfermero se queda aturdido por mi declaración."

nk "¿Que tu QUÉ?"

hi "Solo estábamos corriendo, y Emi comenzó a alejarse, y por eso yo eh, aceleré para alcanzarla."

"El enfermero mira hacia el techo, murmura una plegaria para la paciencia a algún dios u otro, y voltea su mirada de nuevo a nosotros dos."

nk "Entonces los {b}dos{/b} son unos estúpidos."

nk "Eso es reconfortante, creo."

nk "Oh vamos, Hisao. Tengo que asegurarme de que tu corazón no vaya a explotar o algo así."

show bg school_nurseoffice at left
show nurse concern at center
show emi basic_closedsweat_gym at Alphaout(1.0), offscreenright
with charamove

hide emi
with None

"Diligentemente obedezco y lo sigo a una habitación adyacente donde nos aseguramos de que, de hecho, no me voy a retorcer y morir."



nk "Y bien, ¿qué es lo que sientes?"

hi "No sé. No mucho. Cansancio, pero podría ser solo por el ejercicio."

nk "Deberías quedarte aquí por algunas horas y descansar, y veremos cómo te sientes después de eso."

"No voy a objetar, por lo que me acuesto en la cama de la enfermería."

stop music fadeout 2.0

scene bg school_nurseoffice at left
with shorttimeskip

"Una Emi sumamente miserable entra después de recibir un buen regaño del enfermero en la otra habitación."


"No pude escuchar lo que él decía a través de la puerta cerrada, pero estoy seguro de que no fueron cumplidos."

show emi sad_depressed_gym at center
with charaenter

play music music_dreamy fadein 0.5

emi "Mira, lo siento, lo siento mucho."

emi "Debería haber sido más cuidadosa."

hi "Oye, no lo sabías. No es tu culpa."

"Se ve terriblemente desanimada y arrepentida, y mis palabras no hacen mucho para alentarla."

emi "Quiero compensártelo."

"De nuevo con ese asentir tan decisivo."

show emi sad_shy_gym
with charachange

emi "Así que tienes que venir a almorzar conmigo."


emi "Lo llevaré por ti, ¿está bien? ¡Algo muy, muy bueno!"

"Empiezo a decir “No tienes que…” pero entonces me callo y solo le asiento cuando veo su cara."

show emi excited_proud_gym
with charachange

emi "¡Bien!"

show emi basic_grin_gym
with charachange


emi "Nos reunimos en la azotea."

hi "¿Nos?"

show emi basic_closedgrin_gym
with charachange

emi "¡Síp! El clima está agradable, así que la azotea es un lugar genial para el almuerzo, sabes."

hi "Ya veo."

show emi sad_shy_gym
with charachange

emi "Vas a venir, ¿cierto?"

emi "¿No me negarías la oportunidad para compensarte, ¿verdad?"

hi "Por supuesto que no."

show emi excited_joy_gym
with charachange

emi "¡Genial! ¡Nos vemos allá!"

hide emi
with charaexit

with shorttimeskip

"Me mantengo a flote en algún lugar entre el sueño y la realidad, sintiéndome completamente exhausto."

"No únicamente mi cuerpo, sino todo mi ser se encuentra sin fuerza y paralizado, aparte de mis sentidos."

"Trago con dificultad y entonces trato de mantenerme lo más quieto posible, lo cual en este estado no me resulta algo muy difícil de lograr."

"El enfermero se encuentra del otro lado de las cortinas que corrió para darme privacidad. Puedo ver su sombra moverse de lado a lado bajo la luz del sol."

"Ha abierto la ventana de su oficina. Hace viento afuera."


"Las blancas cortinas revolotean en la brisa en un pesado, perezoso movimiento, como olas. La luz se cuela a través de ellas lentamente, absorbida en parte por la tela."

stop music fadeout 5.0

scene darkgrey
with shuteye

"Cierro mis ojos. La brisa en mi rostro se siente como la suave tela de las cortinas."

"Escucho los latidos de mi corazón por un momento, intentando acallar el sonido del enfermero tecleando en su computadora, y mi propia pesada respiración."

"Es estable."

"Maldita sea, ni siquiera una semana y ya acabé en un lugar como este. Realmente lo arruiné esta vez. Debería haber tenido una mejor idea que actuar como el deportista estrella a medio cocer enfrente de uno verdadero."


"¿Y por qué intenté hacerme el valiente, como si esas palpitaciones no hubieran sido gran cosa, incluso cuando era obvio que lo eran?"

"Fue tan solo un reflejo, empujarlo fuera, mantenerlo adentro."

"No quería que ocurriera."

"No quería que Emi lo viera."

"Aaah…"

"Estúpidoestúpidoestúpido."

"Debo ser más cauteloso, o terminaré en el hospital otra vez, o peor."

"…"

"Ese es mi último pensamiento antes de dejarme llevar por el cansancio."

scene black
with Dissolve(1.0)

window hide Dissolve(2.0)

with Pause(2.0)

scene bg school_nurseoffice at left
with openeye

window show

play music music_daily fadein 6.0

"Me quedé dormido. ¿Por cuánto tiempo? ¿Qué hora es?"

"Me siento un poco mareado y no dejo de parpadear compulsivamente."

show bg school_nurseoffice at center
with charamove


"Empujando la cortina a un lado, entrecierro los ojos contra la luz sin filtrar que se vierte por la ventana. La textura de la lona no se siente para nada como el viento de antes."

"El enfermero levanta la mirada de su trabajo, sentándose exactamente donde estaba antes."

show nurse fabulous at center
with charaenter

nk "¿Cómo te sientes?"

"En verdad no puedo decirlo, por eso no respondo nada. Me siento algo aturdido por quedarme dormido en una hora tan rara, con suerte no me veo muy raro."

hi "¿Qué hora es?"

"Yo hablando con voz ronca tratando de lograr un poco de orientación. El enfermero viendo su reloj antes de responder."

"Las cosas parecen suceder en cámara lenta."

show nurse neutral
with charachange

nk "Diez y cuarto."

"Trato de pensar lo que significa por un momento pero no estoy realmente seguro."

show nurse concern
with charachange

nk "No respondiste mi pregunta, Hisao."

hi "Oh. Bien."

show nurse neutral
with charachange

nk "Entonces bájate de esa cama, y veamos qué tal te va. No…"

$ renpy.music.set_volume(0.5, 0.2, channel="music")

show bg school_nurseoffice as dizzy_bg behind nurse:
    xalign 0.5 yalign 0.5 rotate 0 zoom 1.0 alpha 0.0
    ease 0.4 rotate 6 zoom 1.05 alpha 0.5

show nurse neutral as dizzy_fg:
    xalign 0.5 yalign 0.5 rotate 0 zoom 1.0 alpha 0.0
    ease 0.4 rotate -4 zoom 1.05 alpha 0.5
with Pause(0.4)

show bg school_nurseoffice as dizzy_bg behind nurse:
    ease 1.0 rotate 0 zoom 1.0 alpha 0.0

show nurse neutral as dizzy_fg:
    ease 1.0 rotate 0 zoom 1.0 alpha 0.0

"Trato de hacer justamente eso, solamente para tambalearme cuando me muevo demasiado rápido. El enfermero se mueve para sostenerme por un brazo y suspira."

show nurse concern
hide dizzy_bg
hide dizzy_fg
with charachange

nk "… te levantes muy rápido, es lo que te iba a decir. Solo siéntate, voy a checarte la presión para asegurarme."

$ renpy.music.set_volume(1.0, 2.0, channel="music")

"Vaya que mis buenas intenciones duraron por un buen tiempo. Me callo, avergonzado de mí mismo, mientras el enfermero se ocupa con un anticuado artefacto y mi brazo. Después de un par de minutos, lo guarda, sin verse satisfecho ni descontento."

show nurse neutral
with charachange

nk "Estás bien. ¿Dejó de darte vueltas la cabeza?"

hi "Sí."


nk "Bien. Y ¿cómo le está yendo al resto de ti?"

show nurse concern
with charachange

nk "No demostraste buen juicio allá afuera, Hisao."

"Me trago la réplica que iba a hacer. Es lo que había pensado, pero escucharlo de otro me hace querer protestar."

"No es agradable escuchar lo que dice. No lo hace estar menos en lo cierto."

hi "No, señor."

show nurse neutral
with charachange

"Asiente con la cabeza, todavía viéndose tan neutral como antes."

"Sería fácil enojarse con él si dijera “Te lo dije” o algo parecido, pero no lo hace."

nk "Puedo intentar ayudarte a mantenerte saludable, pero al final la decisión es tuya. Espero que este pequeño episodio sea algo que te lo recuerde."

show nurse fabulous
with charachange

nk "Ten, una nota para tu maestro. Para evitar un interrogatorio."

"Tomo el trozo de papel que me ofrece y me retiro ya que no puedo pensar en nada más que decir, tampoco es como si realmente quisiera."

show nurse neutral
with charachange

nk "Mantente fuera de problemas, ¿me oyes? No creo que haya sido más que un susto, pero la próxima vez puede ser diferente."

"Lo escucho."

scene bg school_nursehall
with locationchange

stop music fadeout 4.0


"Hay alguna manera de ir al edificio de la escuela directamente desde el edificio auxiliar, pero no tengo interés en buscarla y posiblemente perderme, así que opto por la salida que yo sé que sirve."

scene bg school_courtyard
with locationchange

"Me detengo en las escaleras del edificio auxiliar, deliberando por un momento entre ir a los dormitorios por mis cosas y mis libros o ir directamente a clase."

"El sol hace que me ardan los ojos, por lo que me dirijo a los dormitorios."




label es_A26:

window hide None
scene black
with dissolve

scene bg school_dormhisao
with openeye

with Pause(0.2)

scene bg school_dormbathroom
with locationskip

window show

"Despierto y tomo una ducha caliente."

label es_A26a:

scene bg school_dormhisao
with locationskip


"De regreso a mi habitación, lo primero que veo es la familiar hilera de frascos con medicamentos alineados sobre mi guardarropa, y me deprime, como es usual."

"Es molesto. Pensé que estaba bien. Pensé que había hecho las paces con esto, que lo había superado."

"Pero lo que en verdad hice… fue permitirme olvidar que tengo un problema. Estar aquí ciertamente me recuerda la realidad, y tratar de pelear contra ella solo lastima."



"Reflexionar sobre ello no hará gran cosa. Ya he hecho esto antes, durante meses. Parece que es tiempo de superarlo."

"Si me concedo olvidar que mi vida definitivamente no será tan larga como la de los demás, no llegaré a ninguna parte."

"Mi vida puede ser diferente de las demás. Pero es una vida en progreso."

"Así es como lo racionalizaré."


"De un trago tomo el puñado usual de pastillas, intentando empujar fuera de mi cabeza el repentino sentimiento lúgubre. Entonces me preparo para salir temprano a clases, como de costumbre."

scene bg school_dormhallway
with locationchange


"Al salir al pasillo, noto a Kenji viniendo desde la esquina de este, sigilosamente dirigiéndose hacia su habitación con una gran bolsa. Mientras se escabulle delante de mí sin hacer ruido como un ninja escondiéndose a plena vista, decido llamarlo."

hi "Hey."

show kenji neutral at center
with charaenter

play music music_kenji fadein 0.5

"Da un salto al sonido de mi voz."

ke "Oh, qué tal, viejo. No me di cuenta de que estabas ahí. Estoy muy cansado."

"Creo que más bien no me vio, pero ese no es el problema."


hi "¿Dónde estuviste tan temprano? ¿De compras?"

show kenji tsun
with charachange

ke "Nah, no estaba de compras. Algunas veces tengo que visitar… al maestro de matemáticas. Sí, pensé que sería una buena idea averiguar cuándo sería el siguiente examen, ya que te dice por adelantado si quieres saber."

hi "Y entonces, ¿qué hay en la bolsa?"

show kenji neutral
with charachange

ke "Se me ocurrió ir de compras mientras estaba fuera. Necesito suministros para continuar la pelea en contra de la vasta conspiración feminista."

hi "Ah, muy bien."

hi "Creí que no salías."

show kenji happy
with charachange

ke "Ahora llevo un sombrero."

"Decido no señalar el hecho de que no lleva un sombrero."

"Un silencio incómodo se asienta entre nosotros y entonces Kenji lo rompe empujando su puerta lentamente, lanzando un chirrido al aire que solo acrecenta la incomodidad del momento. Deja la bolsa dentro de su cuarto y cierra la puerta."

hi "Me sorprende que te hayas desviado de tu camino para averiguar la fecha de un examen. Tratar de tomar ventaja de una oportunidad para estudiar es bastante diligente."

show kenji tsun
with charachange

ke "Yo nunca estudio."

hi "Oh…"

show kenji neutral
with charachange

ke "Solo quería saber qué día era el siguiente examen. Aún tengo que tomarlo, duh. Necesito saber de antemano para saber qué día no puedo faltar a clases. Usualmente manda actualizaciones de esa basura por teléfono, así que tuve que salir y averiguar."

hi "¿Y por qué tienes que salir, cuando puedes saberlo con tu teléfono?"

show kenji tsun
with charachange

ke "No traigo teléfono."

hi "¿A qué te refieres con que no traes un teléfono? ¿Quieres decir que lo dejas en casa?"

show kenji neutral
with charachange

ke "Nah, no uso teléfonos. No tengo teléfono. Teléfonos. No tengo teléfono."

hi "¿Por qué no tienes teléfono? ¿Cómo puedes no tener teléfono? ¿Ningún teléfono? ¿Nada?"

show kenji tsun
with charachange

ke "Solo no me gustan los teléfonos. De hecho, me dan un poco de miedo. No sé por qué. Creo que es algún tipo de trauma reprimido."

ke "Pero, básicamente, cuando escucho un teléfono, me pongo nervioso. Es mi más oscuro secreto."

show kenji neutral
with charachange

ke "Tengo dos teorías sobre eso: o tengo algún temor de recibir alguna llamada mortal, indefinida y ominosa capaz de alterar mi vida, o fui golpeado con un teléfono en el pasado. Golpeado tan fuertemente que no puedo recordarlo."

hi "Golpeado en la cabeza."

show kenji tsun
with charachange

ke "Bueno, ¿dónde más podría ser golpeado con un teléfono para hacerme incapaz de recordarlo? ¿El culo?"

"Inesperadamente lógico. Ahora me siento muy deprimido. Presintiendo que esta conversación está más o menos acabada, Kenji abre su puerta de nuevo y se prepara para entrar."

show kenji neutral
with charachange


ke "Bueno, me voy a dormir, mi amigo. Que disfrutes."

hi "Las clases van a empezar en 20 minutos."

show kenji tsun
with charachange

ke "Ya hice algo por hoy. Demasiado cansado para ir a la escuela."

show kenji happy_close
with characlose

ke "Oye, ¿necesitas algo de bálsamo labial? Compré dos por accidente porque pensé que la tienda había empezado a vender baterías doble A individuales."

hi "Gracias pero no gracias."



label es_A26b:

scene bg school_dormhallway
show kenji happy_close at center
with None

stop music fadeout 0.3

play sound sfx_doorslam

show kenji tsun_close
with vpunch

"La puerta al final del pasillo se abre estrellándose contra la pared por haber sido empujada con demasiada fuerza. El sonido es seguido por una tronadora risa burbujeante, e instantáneamente sé de quién se trata."

play music music_comedy fadein 0.3

show misha perky_smile at center behind kenji
show shizu basic_normal2 at center behind kenji
with zoomin


show shizu basic_normal2:
    easein 1.0 tworight
show misha perky_smile:
    easein 1.0 twoleft
show kenji tsun_close:
    0.25
    easeout 0.5 offscreenleft alpha 0.0
with Pause(1.0)

hide kenji
with None

play sound sfx_impact2


"Con el ruido, Kenji desaparece dentro de su habitación como un ninja, azotando la puerta justamente cuando Shizune y Misha caminan para acá."
"La primera anda con pasos cortos y eficientes, mientras que la segunda más o menos rebota por las paredes."

show misha hips_smile_close at twoleft
with characlose

"Trato de hacer lo mismo que Kenji, pero es demasiado tarde. Misha pone su pie en el paso de la puerta para impedirme cerrarla, así que no tengo más remedio que dejarlas entrar."


scene bg school_dormhisao
with locationskip

show shizu behind_smile at center
with charaenter

shi "…"

show shizu behind_smile at tworight
with charamove

show misha hips_grin at twoleft
with charaenter

mi "¡Qué tal, Hicchan~! ¡Hola~ hola~!"

hi "Qué tal."

hi "¿Qué hacen por aquí?"


"Me pregunto si la pausa entre esas dos oraciones fue lo suficientemente larga para ser cortés."

show shizu basic_normal
with charachange

shi "…"

show misha hips_frown
with charachange

mi "¡Hicchan, qué grosero~! ¡Venimos a recogerte!"

show misha hips_smile
with charachange

mi "¿Acaso se te ocurrió que pensamos que te ibas a escapar y venimos para asegurarnos de que no fuera así? ¡Seguramente no, Hicchan~!"

hi "Oye, yo no dije que eso fuera por lo que estaban aquí."

"Pero ahora sé que eso es exactamente por lo que están aquí."

show misha sign_smile
with charachange

mi "¡Es hora del trabajo del consejo estudiantil, sí que lo es~!"

show misha hips_grin
with charachange


mi "¡No estás contento, Hicchan, de tener la oportunidad de ayudarle a toda~ la escuela~! ¡Eres como un héroe~! ¡Las generaciones futuras contarán historias sobre este día!"

"Interesante. No pensé que unirse al consejo estudiantil fuese una hazaña digna de Hércules."

hi "Bueno… supongo que sí lo prometí…"

show shizu adjust_happy
with charachange

stop music fadeout 7.0

"Me había olvidado de Shizune y solo ahora es cuando la noto de reojo, asomándose a mi habitación por sobre mi hombro, su analítica mirada saltando de un objeto a otro."

"Esto es algo intrusivo, la sensación de estar expuesto se arrastra por mis bolas. Por suerte no tengo ropa sucia sobre el piso o algo por el estilo."

show shizu behind_smile
with charachange

shi "…"

show misha perky_confused
with charachange

mi "¿Hm~? ¿Qué pasa, Shicchan?"

show misha hips_smile
with charachange

mi "¡Sí, esta es la habitación de Hicchan~! ¡No la habíamos visto antes, no me había dado cuenta!"

show misha hips_grin
with charachange

mi "Es un poco simple, pero Hicchan no ha tenido tiempo de decorarla todavía, ¿no es ese el caso~?"


show misha sign_smile
with charachange

mi "¿Qué son esas cosas?"


"Ella señala a mi colección de medicamentos sobre la mesa de noche."




label es_choiceA26:
menu:
    with menueffect
    "En verdad no quiero hablar de ello con estas dos."
    "Tratar de evadir el tema.":


        return m1
    "Echarlas fuera de mi cuarto.":

        return m2


label es_A26c:

hi "No es nada."

show shizu basic_normal2
with charachange

"Rápidamente me paro enfrente de ellas, tratando de ocultar las cosas detrás de mí. Shizune toma un paso atrás, con una mirada sospechosa, pero no es una expresión sin preocupación."

"Espero que, si lo evado, ella comprenda que no la quiero insistiendo al respecto."

show shizu behind_blank
with charachange

shi "…"

show misha perky_confused
with charachange

mi "¿Es verdad? ¿Qué estás escondiendo, Hicchan~?"

hi "Nada."

show shizu basic_normal
with charachange

shi "…"

show misha sign_confused
with charachange

mi "¿En serio~?"

"Me doy cuenta de que en realidad no me puedo zafar de esta. Son entrometidas por naturaleza y ocultarlo únicamente despertará más su curiosidad."

hi "Sí está bien, es {b}algo{/b}, pero realmente no quiero hablar de ello, ¿de acuerdo? No… todavía."

hi "¿No podemos poner esto de lado por ahora?"

show misha perky_smile
with charachange

"A medida que Misha traduce, Shizune fija su mirada fuertemente en mí, tan concentrada y analítica como siempre, curioseándome por encima de la montura de sus anteojos."

"Presiona sus dedos uno contra otro pensativamente, como si sopesara el valor de seguir más de lo necesario contra el insulto de irrespetar mis deseos."

"Su expresión finalmente se funde en una leve sonrisa y le dice algo en señas a Misha."

play music music_dreamy fadein 2.0

show shizu adjust_happy
with charachange

shi "…"

show misha hips_smile
with charachange

mi "¡Está bien~! ¡Entonces, vamos a esperar, y nos haremos mejores y mejores amigos, y un día cuando tengas ganas, nos lo puedes contar~!"

"Ambas me dan una amplia sonrisa, y me siento perplejo y un poco estúpido por mi comportamiento."

"No son estúpidas, y probablemente puedan intuir, al menos a medias, qué es lo que me ocurre. Y…"

"Palabras tan simples y amables. Me siento aliviado de que no piensen mal de mí a pesar de que yo sea así. A pesar de no ser como el resto. A pesar de que no pueda estar tranquilo acerca de eso."

"Parece que detrás de las travesuras odiosas, estas dos chicas son en verdad amables y buenas personas. Eso es lo que pienso."

hi "Gracias."

hi "Así que, quieren que les ayude por este día, ¿cierto? ¿Ya que soy uno de ustedes?"

show misha hips_grin
with charachange

mi "¡Síp~!"

hi "¿Después de clases?"

show misha sign_smile
with charachange

mi "¡No no no~! ¡Ahora!"

hi "¿Ahora? ¿Pero qué hay sobre las clases? ¿Van a faltar de nuevo?"

show shizu adjust_smug
with charachange

shi "…"

show misha cross_laugh
with charachange

mi "¡Jajaja~! ¡Es por el bien común, así que sacrificamos nuestras lecciones de matemáticas, y tal vez estudios sociales también~!"

hi "Bueno, creo que por mí está bien."

show shizu behind_smile
with charachange

shi "…"

show misha sign_smile
with charachange

mi "¡Asombroso, Hicchan~! Tú lo dijiste, ¿está bien? Recuerda: “Por mí está bien ayudar~”, es lo que tú dijiste, ¿cierto~?"

hi "Seguro."

"Ese tono… De repente me arrepiento de haberlo dicho."

show shizu basic_normal2
with charachange

shi "…"

show misha hips_grin
with charachange

mi "¡Muy bien~! ¿Entonces ya estás listo para ir? ¡Podemos ir a la oficina juntos~!"

hi "No. Probablemente me harán cargar todas sus cosas o algo por el estilo."

show shizu adjust_happy
with charachange

shi "…"

show misha perky_smile
with charachange

mi "No seas tonto, Hicchan."

show misha hips_smile
with charachange

mi "Nunca hemos caminado a la escuela juntos, Hicchan~."

"Casi quiero preguntar por qué lo haríamos, pero entonces me doy cuenta. Ambas me consideran su amigo, como dijo Misha antes. Y quieren que seamos mejores amigos, incluso."

"Es extraño, nunca había pensado en ellas de esa forma. O de cualquiera que haya conocido durante esta semana. ¿En verdad es así de sencillo?"

"Así de simple…"

hi "Está bien, vamos, entonces."

show shizu behind_smile
with charachange

"Shizune sonríe disimuladamente y pone sus manos detrás de ella."

show misha hips_grin
with charachange

mi "¡Jajaja~! ¡Grandioso, Hicchan~! ¡Bien, muy bien, pero primero~! Tuviste una excelente idea, le gustó mucho a Shicchan… ¡Así que~! ¡Es tiempo de un juego!"

hi "Oh no."

show misha hips_smile
with charachange

mi "¡Shicchan tiene un billete de 1000 yenes en una de sus manos, Hicchan~! Si adivinas en cuál, ¡te lo puedes quedar! Si no lo logras…"

show misha hips_grin
with charachange

mi "¡Cargarás todos nuestros libros a la escuela~! ¿Cierto, Shicchan~? ¡Cierto~!"

"Shizune y ella asienten una a la otra."

show misha sign_smile
with charachange

mi "¡Muy bien, Hicchan~! ¡Prepárate~!"

stop music fadeout 7.0

scene bg school_courtyard
with shorttimeskip

"Cargando con tres mochilas en lugar de una, me pregunto sobre el día que me espera. Que nos espera."


"Puedo ver estudiantes yendo y viniendo por el patio, probablemente preparando sus propios proyectos."

"El festival está prácticamente aquí. Eso significa que solo hay dos posibles razones de que mi ayuda sea requerida."

"O únicamente queda una pequeña cantidad de trabajo por hacer, y ellas solo quieren una mano para terminar las revisiones finales mundanas que están obligadas a hacer."

"O hay un montón de trabajo pendiente, y Shizune está poniendo un rostro tranquilo mientras un torrente de trabajo postergado y apilado amenaza con matarnos a todos."



label es_A26d:

play music music_rain fadein 4.0

"Aun así, ya se han pasado de la raya esta vez. Fastidiosas entrometidas."

hi "No es nada."

show misha perky_smile
with charachange

mi "¿En verdad~, Hicchan? No se ve como si fuera nada, para mí."

show shizu adjust_smug
with charachange

shi "…"

show misha hips_smile
with charachange

mi "Qué línea tan larga de frascos, ¿cierto~? ¡Cierto~! ¿De qué son todos esos, Hicchan?"

hi "Solo unas cuantas cosas."

show shizu basic_normal2
with charachange

shi "…"

show misha perky_confused
with charachange

mi "Eso se ve como mucho más que “unas cuantas cosas”…"

"No puedo culpar a alguna de ellas por ser de esta manera. Misha solo está hablando por Shizune, y Shizune es curiosa por naturaleza. Aun así, desearía que dejaran de escarbar y entendieran la indirecta. Pero Misha no lo hace, y Shizune no puede."

"Por eso es que siguen presionando."

hi "Realmente no es ningún asunto suyo."

hi "¿No deberían de marcharse? La habitación de un hombre es privada, ya saben."

"Shizune parece tomar eso como un reto."

show shizu behind_frown
with charachange

shi "…"

show misha hips_frown
with charachange

mi "¿Qué significa eso, Hicchan? Cuando alguien ve algo interesante, su primer instinto es preguntar qué es, eso es obvio. ¿Qué hay de malo en eso?"

hi "Porque, como dije, no hay nada que ver."

show misha perky_confused
with charachange

mi "Hicchan, creo que Shicchan solo está preocupada."

hi "Lo que tenga en mi habitación no es ningún asunto suyo, eso es todo."

show misha sign_confused
with charachange

mi "Pero…"

hi "¡Maldita sea! Algunas veces quisiera que ustedes dos dejaran de jugar tanto. No es divertido todo el tiempo. Eso lo saben, ¿no?"

"Eso lo digo con más fuerza de la que quería, casi gritándoselo en la cara a Misha. Ella se estremece y se congela en media traducción, e incluso Shizune reacciona aunque no me haya escuchado."

stop music fadeout 6.0

"Creo que mi rostro enojado dijo todo lo que se le tiene que decir."

show misha perky_sad
show shizu behind_blank
with charachange

"Después de que Misha termina de traducir, las chicas se ven la una a la otra con cara de culpa."

show shizu behind_sad
with charachange

shi "…"

mi "Está bien, Hicchan, te dejaremos a solas."


"Es la primera vez que he escuchado a Misha hablar sin los característicos altibajos de su voz. Se siente tan extraño de oír, y quiero disculparme, pero ellas ya se han dado vuelta para marcharse."

"Mientras el silencio se asienta, lamento lo que dije más y más."

hide shizu
hide misha
with charaexit

"Las chicas se retiran calladamente, y después de un tiempo de quedarme parado en mi habitación me visto y las sigo."



label es_A26e:

show kenji tsun_close
with charachange

ke "Viejo, como sea."

stop music fadeout 2.0

hide kenji
with charaexit


"Entra velozmente a su guarida, permitiéndome al fin ir a clase."




label es_A27:

scene bg school_hallway3
with shorttimeskip

"Los corredores se encuentran tan silenciosos como lo estaba el patio, naturalmente ya que todos están en clase. Toco ligeramente en la puerta del 3-3 y la abro cuando Mutou llama del otro lado."


scene bg school_scienceroom
with locationchange

hi "Perdón por llegar tarde."

"Quince pares de ojos voltean hacia mí."

show muto irritated at center
with charaenter

mu "Buenos días, Nakai."

"Mutou parece estar un poco confundido por mi llegada tardía, como si hubiera interrumpido su flujo o algo así."

"A juzgar por las aburridas conferencias que suelen ser sus clases, ese puede ser el caso."

"Le paso la nota que el enfermero me dio. Mutou la toma asintiendo y la lee rápidamente."

show muto normal
with charachange

"Levanta sus cejas y me da una mirada un poco severa pero no dice nada, solo asiente solemnemente una vez más."

"Me encojo de hombros y me hace un gesto de que me mueva así que naturalmente lo hago."


label es_A27a:

scene bg school_scienceroom
show muto normal at center
with None


hide muto
with charaexit

"Solo dos pares de ojos se mantienen siguiéndome mientras camino a mi asiento."



"No estoy sorprendido en lo más mínimo cuando siento la uña de Misha picándome a través de mi camisa alrededor de quince segundos después de haberme sentado."


show misha perky_smile_close at offscreenleft
with None

show bg school_scienceroom at bgright
show misha perky_smile_close at Transform(xalign=-0.3)
with charamove

play music music_another fadein 2.0

mi "¡Psst! ¿Dónde estabas?"

hi "No es asunto tuyo."

"Sé que esta es posiblemente la peor respuesta que puedo darle ya que únicamente servirá para captar su atención, pero no tengo energía para inventar una excusa más elaborada en este momento."

show misha perky_confused_close
with charachange

show bg school_scienceroom at center
show misha perky_confused_close at offscreenleft
with charamove

"Sin embargo, Misha desiste. Ella es inesperadamente rápida para rendirse este día."

"…"

"En un minuto está de vuelta para picotearme con su dedo."

show misha hips_grin_close
with None

show bg school_scienceroom at bgright
show misha hips_grin_close at Transform(xalign=-0.3)
with charamove

mi "¡Vamos, dinos! ¡Shicchan está muy interesada también!"

"Tan solo me hacía ilusiones. Únicamente se fue a hablar con Shizune, probablemente para idear maneras de hacerme soltar la lengua."

hi "No."

show misha perky_sad_close
with charachange

show bg school_scienceroom at center
show misha perky_sad_close at offscreenleft
with charamove

"Retrocede para negociar otra vez."

show misha sign_smile_close
with None

show bg school_scienceroom at bgright
show misha sign_smile_close at Transform(xalign=-0.3)
with charamove

label es_choiceA27:
menu:
    with menueffect
    mi "¡Como miembro del consejo estudiantil, es tu deber decirnos por qué faltas a clases! ¡Especialmente si es algo muy, muy, muy divertido~!"
    "Sí, me divertí muchísimo en la oficina del enfermero…":



        return m1
    "No quiero hablar de eso, ¿está bien?":


        return m2

label es_A27b:

stop music fadeout 4.0

"Con un demonio. Ella no sabe cuándo parar."

hi "Bien, seguro. Lo que sea. Te lo diré. Estaba pasando un rato estupendo."


hi "Tuve un ataque cardiaco a primera hora de la mañana y luego estuve unas horas con el jefe de enfermería por diversión."

hi "La mejor mañana de mi vida, te tengo que decir."

"Trato de imitar su canturreo ridículo mientras mantengo la voz baja de forma que nadie más me oiga. Las palabras salen escupidas de mi boca."


show misha perky_confused_close
with charachange

mi "Hicchan, ¿tuviste un qué? ¿En serio?"

hi "Solo olvídalo. Ya me oíste."

show misha perky_sad_close
with charachange

mi "¡Pero Hicchan, esto es importante!"

hi "No, en serio. Déjame en paz. Estamos a media clase, además."

show misha sign_sad_close
with charachange

mi "¡Pero Hicchan!"

"Misha suena consternada, o tal vez con pánico. Me pregunto si ella misma se da cuenta de que no fue la más brillante de las ideas el ser tan entrometida."

"…"

"La dejo cociéndose en sus propios jugos por unos momentos antes de responder. Esto no se traducirá a Shizune pero no me interesa."

hi "No estés jodiendo, Misha."

hi "Y dile eso también a Shizune."

"Mientras las palabras dejan mi boca, me arrepiento inmediatamente de haberlas dicho, pero no es como si pudiera retirarlas."

show misha perky_sad_close
with charachange

show bg school_scienceroom at center
show misha perky_sad_close at offscreenleft
with charamove

hide misha
with None

"Para mi sorpresa parcial, Misha en verdad se calla aunque no me molesto en asegurarme de si le pasa el mensaje a Shizune. No importa de cualquier forma."

"Mutou termina su clase en una charla genérica sobre el festival dentro de dos días."





label es_A27c:

hi "Ríndete. No voy a hablar."

show misha hips_grin_close
with charachange

mi "¿Con que así es~?"

hi "Sí."

show misha perky_confused_close
with charachange

"Ella lo piensa por un momento."

show misha hips_frown_close
with charachange

mi "¡Pero qué avaro, Hicchan~!"

"Puedo escuchar el puchero en su voz, decepcionada y decaída."

show bg school_scienceroom at center
show misha hips_frown_close at offscreenleft
with charamove

"Retrocede de nuevo por el momento para negociar con la mitad cerebral del dúo dinámico, antes de regresar."

show misha hips_smile_close
with None

show bg school_scienceroom at bgright
show misha hips_smile_close at Transform(xalign=-0.3)
with charamove

mi "Pienso que deberíamos almorzar juntos y discutir más sobre esto… dice Shicchan."

show misha hips_grin_close
with charachange

mi "Nosotras invitamos."

show misha sign_smile_close
with charachange

mi "¡Además, tienes que compensarnos por no haber estado en la mañana y necesitamos ayuda con el trabajo~!"

"Los demás estudiantes a nuestro alrededor empiezan a mirarnos, posiblemente porque Misha se está inclinando sobre el escritorio demasiado, tanto que casi tocamos cabezas. Su cabello rizado me roza el cuello."


"Huele a champú y probablemente a lo que sea que se pone allí para que luzca de esa manera."

"Creo que la chica enfrente de mí está tratando de escuchar. Espero nadie esté teniendo la idea equivocada de esto, aunque no estoy muy seguro de cómo podría ser posible tener cualquier otro tipo de idea."

"Por suerte Mutou se mantiene inconsciente, o deliberadamente pasa por alto a Misha. Hasta ahora."

"En realidad no puedo ganar esta, ¿o sí?"



label es_choice2A27:
menu:
    with menueffect
    "Prometí comer con Emi también, pero no puedo estar en dos lugares a la vez."
    "Iré a almorzar con Emi y su amiga.":


        return m1
    "Iré con Shizune, después de todo ahora estoy en el consejo.":

        return m2


label es_A27h:


hi "Lo siento, no puedo. Ya prometí almorzar con alguien más."

show misha perky_confused_close
with charachange

mi "¿Eeeh? ¿Quién? ¿Es una chica~?"

hi "Sí…"

show misha hips_grin_close
with charachange


"Su risita me obliga a salir rápidamente con algo más para que no tenga la idea equivocada."

hi "¡No es nada de eso! Es… un poco complicado."

show misha perky_smile_close
with charachange

"Complicado… sí, eso es mi vida, a pesar de haberme asentado en una rutina escolar diaria."

"Todo debe ser puesto en una nueva perspectiva dentro de esta segunda vida, reconsiderada desde el punto de vista de este nuevo yo."

"El yo con un corazón roto."

hi "Además, no sé si podré venir al consejo después de todo."

hi "O al menos por ahora. Tengo otro asunto en el cual concentrarme primero."

"Eso es cierto. Debo replantear mis prioridades. Esto es algo que le ha dado vueltas a mi cabeza desde que el enfermero me dio ese sermón. Realmente no puedo darme el lujo de pretender que no tengo esta condición."

"Me sorprende que pueda pensar tan analíticamente, pero me dejaré llevar por ahora."

hi "Prometo dar una explicación apropiada más tarde, pero no ahora, ¿de acuerdo? Por favor dile a Shizune que siento decepcionarla."

show misha perky_confused_close
with charachange

mi "Si tú lo dices, Hicchan."

"Suena sorprendida, y seria, no creo haber oído a Misha así antes."

show bg school_scienceroom at center
show misha perky_confused_close at offscreenleft
with charamove

hide misha
with None

stop music fadeout 3.0

"Por suerte Misha comprende que hablo en serio, un golpe de suerte que haya podido decir lo que quise tan claramente que incluso ella lo entendió. Ella retrocede para traducirle nuestra discusión a Shizune."

"Ninguna de las dos me habla después de eso."



label es_A27i:

hi "Bien, iré con ustedes, pero deja de molestarme por el resto de la clase, ¿de acuerdo?"

show misha hips_grin_close
with charachange

mi "¡Es un trato, Hicchan~!"

stop music fadeout 2.0

show bg school_scienceroom at center
show misha hips_grin_close at offscreenleft
with charamove

scene bg school_scienceroom
with shorttimeskip

play sound sfx_normalbell

with Pause(7.0)

play ambient sfx_crowd_indoors fadein 0.3

scene bg school_hallway3
show crowd
with locationchange

"De camino al salón del consejo estudiantil, puedo ver estudiantes yendo y viniendo por los corredores, probablemente preparando sus propios proyectos."

"El festival está prácticamente aquí. Eso significa que hay únicamente dos razones para que mi ayuda sea requerida."

"O tan solo queda una pequeña cantidad de trabajo por hacer, y ellas simplemente quieren una mano para terminar con las revisiones finales mundanas que están obligadas a hacer."

"O hay un montón de trabajo pendiente, y Shizune está poniendo un rostro tranquilo mientras un torrente de trabajo postergado y apilado amenaza con matarnos a todos."

stop ambient fadeout 1.0


label es_A27d:



scene bg school_scienceroom
with locationskip

"Para variar, no me encuentro entre los primeros en venir a las clases de la mañana."

"En cambio, casi todos parecen estar aquí. Reconozco a la mayoría de mi grupo por sus caras ahora, aunque sus nombres todavía se me escapan."



label es_A27e:



scene bg school_scienceroom
with shorttimeskip

play music music_normal fadein 3.0

"La clase prosigue con soltura. Creo que empiezo a entrar en el ritmo de la escuela."

"Incluso me he dejado de preocupar por tomar notas y ser por demás atento. Los primeros días estaba bastante tenso en clase."

"Mutou termina temprano su lección sobre la electricidad, pero continúa sin pausa sobre el festival."

show muto normal at center
with charaenter

mu "Y bien, como ustedes saben, el festival es pasado mañana. Espero que los proyectos de todo mundo sean exitosos este año."

show muto smile
with charachange

mu "Que pasen un buen rato, pero también vengan el domingo, por favor tengan el significado de este festival en mente…"

mi "¡Juegos y comida frita!"

"Todos estallan de risa, y yo también."

show muto irritated
with charachange

mu "Sí, gracias Mikado."

show muto normal
with charachange

mu "Pero a lo que me refiero es más el—{w=.5}{nw}"

play sound sfx_normalbell

"Lo que resta de la oración es ahogado por las campanadas anunciando el almuerzo, y todo el mundo comienza a empacar sus cosas."

"Mutou reflexiona por un momento, pero como casi nadie parece prestarle atención, se da por vencido y se sienta."

stop music fadeout 2.0

scene bg school_hallway3
show crowd
with locationchange

play ambient sfx_crowd_indoors fadein 0.3

"El corredor está lleno… o tan lleno como los corredores en esta escuela pueden estar. La mayoría de los estudiantes parece dirigirse a la cafetería."






label es_A27f:

scene bg school_scienceroom
with shorttimeskip

stop music fadeout 2.0

"Misha, y por asociación, Shizune, no me molestan durante toda la mañana."

play sound sfx_normalbell

"Cuando suena la campana, ni siquiera volteo a verlas cuando camino hacia fuera del salón."

scene bg school_hallway3
show crowd
with locationchange

play ambient sfx_crowd_indoors fadein 0.3

"El corredor está lleno… o tan lleno como los corredores en esta escuela pueden estar. La mayoría de los estudiantes parece dirigirse a la cafetería."





label es_A28:

scene bg school_council
with locationchange

show misha perky_smile at twoleft
show shizu behind_smile at tworight
with charaenter

"Una vez dentro de la oficina, miro alrededor y veo que está desierto."

hi "Creo que esto significa que no queda mucho trabajo por hacer, ¿eh? Ya que no hay nadie aquí, y todo eso."

show misha sign_smile
with charachange

mi "¡Siempre es así, Hicchan~!"

"Esto confirma lo que había estado pensando desde antes pero nunca había sido capaz de confirmar de forma definitiva: Shizune y Misha son el consejo estudiantil. Todo el consejo estudiantil."

hi "Maldición. Así que es cierto. El consejo estudiantil son en realidad solo ustedes dos."

play music music_ease fadein 4.0

show misha hips_grin
show shizu cross_wut
with charachange

"Shizune tiene aspecto de estar atrapada preguntándose si debería de estar avergonzada o explotar de ira, y Misha está igualmente dividida entre reír y tratar de detenerla."

show shizu behind_frustrated
with charachange

shi "…"

show misha sign_smile
with charachange

mi "¡Bueno, entonces, Hicchan, te alegrará saber que como somos solo nosotros tres, tenemos mucho que hacer! ¡Mucho~! Mucho~ mucho~ mucho~…"

hi "Eso no me alegra para nada."

show shizu adjust_happy
with charachange

"Pero parece que hace muy feliz a Shizune."

show misha cross_laugh
with charachange

mi "¡Guajaja~!"

show misha hips_grin
with charachange

mi "¡Solo bromeaba!"


label es_A28a:


scene bg school_council
with shorttimeskip

"El trabajo resulta ser la clasificación y doble revisión de la enorme cantidad de papeleo necesario para que un evento como el festival escolar pueda realizarse."

"La burocracia es una cosa abrumadora."

play sound sfx_normalbell

"Pero nos las arreglamos para terminar justo cuando suena la campanada del almuerzo."

show misha hips_grin at twoleft
show shizu adjust_happy at tworight
with charaenter

mi "Bien~, ahora que hemos terminado, ¡podemos relajarnos un poco! Pero no demasiado, ¡tenemos mucho más que hacer por la tarde~!"

label es_A28b:

$ renpy.music.play(music_ease, fadein=4.0, if_changed=True)

show shizu behind_smile
with charachange

shi "…"

show misha sign_smile
with charachange

mi "En realidad no es tanto trabajo, Hicchan~. Así que~, podemos permitirnos disfrutar un pequeño almuerzo primero."

show misha cross_laugh
with charachange

mi "¡Jajaja~!"


"Ambas sacan una pequeña colección de contenedores de plástico de la pura nada."

show misha hips_grin
with charachange

mi "Hm~ hm~… ¡Es chuleta de pollo con tomates y brotes de soya~! ¿No suena delicioso, Hicchan?"

mi "Fue hecho esta misma mañana, y sigue caliente, ¡así que anda come come~!"

"Tomo uno de los contenedores y lo abro. Se ve bien, y ciertamente huele bien. El hecho de que me encuentro muy hambriento se le suma aún más."


hi "Vaya, se ve genial. ¿De dónde sacaste esto?"

show shizu basic_normal
with charachange

shi "…"

show misha hips_smile
with charachange

mi "¡Eso no tiene importancia, Hicchan!"

show misha sign_smile
with charachange

mi "Se suponía que habría un puesto de venta de almuerzos, pero la chica a cargo de pronto dijo que no podía hacerlo. Shicchan dijo, “Qué desperdicio, fue mucho trabajo engañar a Hicchan para que hiciera esto~” —"

hi "Hey, qué diablos…"

show misha hips_grin
with charachange

mi "… ¡Y bien~! Shicchan quería ver si podía hacerlo, pero luego cambió de opinión, ¿verdad, Shicchan~?"

show shizu basic_angry
with charachange

"Shizune se enfurruña y enoja, disparándole a Misha una mirada de disgusto. No creo que se suponía que yo escuchara esa historia."

hi "¿Esta es tu comida de prueba?"

show shizu behind_frown
with charachange

shi "…"

show misha sign_smile
with charachange

mi "¡Yo también la estoy comiendo, Hicchan~!"

show misha hips_grin
with charachange

mi "¡Y también lo hace Shicchan~!"

"¡Eso no responde la pregunta!"

"No obstante, separo un par de palillos que Shizune me ofrece, recojo un pedazo de chuleta, y lo pongo en mi boca."

hi "Es inesperadamente bueno. No pensé que Shizune fuera tan buena cocinera."

show shizu basic_frown
with charachange

"Shizune baja sus palillos para decirle algo a Misha bruscamente, quien traga su chuleta con evidente dificultad para poder hablar por ella."

show misha sign_smile
with charachange

mi "¡Hicchan~! ¡No hables con comida en tu boca~!"

hi "No es como si disfrutara haciéndolo. De todos modos, qué maternal de su parte al mostrar ese tipo de preocupación…"

show shizu behind_frown
with charachange

shi "…"

show misha hips_frown
with charachange

mi "¡Ni siquiera puedes comer correctamente, Hicchan~! ¡Eso es todo lo que es~!"

show misha perky_sad
with charachange

"Llegamos a un punto muerto. No puedo comer para poder hablar con Shizune, quien no puede comer para poder castigarme por comer incorrectamente."
"Misha, atrapada en medio de nosotros dos, está en la misma situación, y se ve como la más descorazonada por cómo va esto."

show shizu behind_blank
show misha perky_smile
with charachange

"De cualquier modo, la comida se está enfriando cada segundo, y no estaba muy caliente para empezar. A donde quiera que esto estaba yendo, termina extinguiéndose bastante rápido una vez que nos damos cuenta de eso, y comemos."

play sound sfx_warningbell

"Después de un tiempo suena la campana, pero Misha no hace ningún intento en decírselo a Shizune, así que estoy seguro de que planean faltar a clases y pasar el resto del día aquí otra vez."

show shizu adjust_smug
with charachange

shi "…"

show misha sign_smile
with charachange

mi "Hicchan, ¿tienes planes para el festival?"

hi "No, no realmente. Después de todo, solo he estado aquí por una semana, ¿qué podría preparar en ese tiempo?"

show misha cross_laugh
with charachange

mi "¡Guajaja~! Hicchan, nos has ayudado bastante, ¡no te menosprecies!"

hi "Está bien."

show shizu basic_angry
with charachange

shi "…"

show misha hips_frown
with charachange

mi "¡Hablamos en serio~!"

hi "¡Está bien!"

"Ambas parecen indignarse por las cosas más extrañas."

show shizu adjust_happy
with charachange

shi "…"

show misha hips_smile
with charachange

mi "Sí vas a ir, ¿cierto, Hicchan? Deberías por lo menos ver lo que hemos reali- ¿zado…? Todo mundo debería ser capaz de ver lo que han hecho para en verdad poder comprender su trabajo, ¡esa es mi creencia~! ¡Tú no eres la excepción!"

show misha perky_smile
with charachange

mi "¡Hicchan, definitivamente deberías ir~! Si no tienes nada planeado, ¡entonces podríamos ir juntos~!"

show shizu adjust_blush
with charachange

hi "¿Necesitan una mano? Si hay algo en lo que necesiten ayuda, estoy bien con quedarme."

"Me siento más tranquilo que antes; mis preocupaciones y temores previos se han ido ya. Había olvidado los problemas de esta mañana por completo hasta ahora, divirtiéndome con Shizune de esta forma."

"Divirtiéndome con Shizune… Parece como un concepto desconocido en el cual pensar, pero, ahora que lo veo, realmente he disfrutado los momentos que pasé con Shizune y Misha estos últimos días, a pesar de todo lo demás."

"Si es posible que vayamos juntos, entonces quizá me pueda permitir quedarme un poco más de tiempo. Y creo que es mejor que tener clases."

show shizu behind_blank
with charachange

shi "…"

show misha hips_smile
with charachange

mi "¿En serio, Hicchan? ¡Muy bien~! ¡Podemos considerarlo como tu paga por el almuerzo gratis~!"

show misha cross_laugh
with charachange

mi "¡Grandioso, esto es genial, de veras~ de veras~ genial~! ¡Shicchan esperaba hablar de esto más tarde de todos modos! ¡Ajajaja~! ¡Guajajajajaja~!"

"Eso no es un almuerzo gratis de ninguna manera. Normalmente estaría enojado, o al menos un poco alterado, pero mi humor ha mejorado desde antes, así que lo dejaré pasar."

"Ayudarlas consiste principalmente en el estampado de formas y hacer lo que parecen ser diez mil copias por pieza de cincuenta diferentes reportes de presupuesto."

"No es difícil, pero muy aburrido, y de acuerdo con Misha, la más sencilla de las tareas con las que tienen que lidiar."

"Me siento cada vez más y más cansado, y con eso, menos ansioso de regresar a clase. Esto es especialmente malo porque mientras más tiempo pase fuera de clase, más difícil parece simplemente levantarse y volver."

"Estas dos, son una influencia terrible. Terribles modelos a seguir. No es como si me molestara demasiado, y estoy seguro de que nadie las admira, pero es el fundamento de la cosa…"

show shizu adjust_happy
with charachange

shi "…"

show misha hips_grin
with charachange

mi "¡Terminé~!"

hi "Ah, eso fue rápido. Yo acabaré antes de que este periodo termine, eso creo."

show misha sign_smile
with charachange

mi "No, no, Hicchan, todo terminó. Así que, ¡tú también terminaste~!"

hi "Eso no tiene ningún sentido, ¿me estás diciendo que todo esto es arbitrario y me han estado manteniendo aquí solo por diversión?"

show misha hips_grin
with charachange

mi "No~…"

show shizu basic_normal
with charachange

shi "…"

show misha perky_smile
with charachange

mi "¡Pero te hemos mantenido aquí por tiempo suficiente~! ¡Deberías volver a clase, Hicchan~! ¡Todavía puedes llegar a la mayoría de este periodo!"

hi "¿Qué hay de ustedes?"

show shizu behind_blank
with charachange

shi "…"

show misha hips_smile
with charachange

mi "¡Por supuesto que también iremos, claro; estamos justo detrás de ti!"

stop music fadeout 6.0

scene bg school_hallway3
with locationchange

"Tranquilizado, comienzo a ir de vuelta al salón de clase, pero el periodo está casi por terminar, por lo que empiezo a pensar que sería inútil a medio camino y paso la diferencia entre esta clase y la siguiente bebiendo jugo en el corredor."

"Mantengo un ojo en la puerta del salón del consejo estudiantil, pero no se abre."
"¿Qué es lo que les toma tanto tiempo? ¿Estarán ocupadas terminando mi parte del trabajo? Bueno, no debería de ser tanto tiempo, a menos que haya más, y solamente querían que me fuera."

"Mientras más lo pienso, más probable parece ser."

"Shizune es… bueno, no es una idiota, pero está claro que es incapaz de decir las cosas directamente."

"Tal vez sea porque no puede hablar, por lo tanto le es más difícil. Tiene a Misha, pero después de todo, tan fácil como puedan hacerlo parecer, todavía hay una diferencia entre una conversación casual y lenguaje de señas."

play sound sfx_normalbell

"Considero ir de vuelta para ver cómo están, pero suena la campana, y tengo que regresar a clase."

scene bg school_scienceroom
with locationchange

"Se me unen pocos minutos después, y los pensamientos que tenía en mente antes se desvanecen en la rutina escolar."

with shorttimeskip

"Para cuando recuerdo, la escuela ya ha acabado por el día y me encuentro demasiado cansado como para hacer algo que no sea ir a casa, hacer mi tarea, y finalmente dormir."

$ suppress_window_after_timeskip = True

scene black
with Dissolve(3.0)




label es_A29:

scene bg school_hallway3
show crowd
with None

play ambient sfx_crowd_indoors fadein 0.3
play music music_emi fadein 0.3

show emi basic_happy at center
with charaenter

emi "¡Hisao!"

show emi excited_proud
with charachange

emi "¡Te haré por una sola y única vez, una super extra especial oferta para el almuerzo!"

show emi excited_laugh
with charachange

emi "¡Los almuerzos caseros de Emi, y el privilegio de disfrutarlos en privado con dos tremendas hermosuras!"

"Su venta excesivamente coqueta hace eco por el corredor, una hazaña notable ya que está lleno de gente."

show emi basic_closedgrin
with charachange

"Emi hace una muy confiada pose como si fuera un intento de vencer su propia ridiculez, inflando su muy modesto pecho y formando la V de la señal de victoria con su mano."

hi "Suena delicioso. ¿A qué se debe este honor de ser invitado?"

show emi excited_proud
with charachange

emi "Estabas ahí parado viéndote muy perdido y triste, entonces pensé que te serviría tener un poco de compañía."

"Esa es posiblemente la razón más deprimente imaginable."

show emi basic_closedgrin
with charachange

emi "Así que, ¿qué te parece? Probablemente estás muy solo y comerías esa horrible comida de cafetería en completa soledad, de otra manera."

hi "Eeeh…"

show emi excited_proud
with charachange

emi "¡Estoy bromeando, estoy bromeando!"

hi "Seguro, comeré tu almuerzo. Con placer."

show emi basic_happy
with charachange

emi "¡Vamos a la azotea!"

hi "¿La azotea?"

hi "¿Por qué la azotea?"

show emi basic_closedgrin
with charachange

emi "¡Porque es ahí donde almorzamos!"

emi "¡Y si no voy allá arriba, entonces es posible que ella deambule por ahí y yo sé que luego simplemente pasará hambre porque nunca lleva un almuerzo para ella!"


hi "¿Quién lo hace?"

show emi basic_closedhappy
with charachange

emi "¡Ven conmigo!"

"Sin responder mi pregunta o esperar por una respuesta, ella me toma del brazo y me arrastra a través de los corredores."

"Intento llevar una conversación en el camino."

hi "¿Por qué tienes un almuerzo extra?"

show emi sad_grin
with charachange

"Emi sonríe con culpa."

emi "En realidad, es el almuerzo de ayer."

emi "Metí una carrera durante el almuerzo y olvidé comérmelo."

"Ah."




label es_A29x:

"Su expresión es tan graciosa que casi río a carcajadas."

"Emi ríe entre dientes, para sí misma o para alguien más, o tal vez sin alguna razón. Me gusta ese sonido."

"El carácter alegre y lleno de energía de Emi alivia la sensación de constricción detrás de mi cabeza a causa de la discusión con Shizune y Misha."

"Dejo que ese asunto se vaya de mi mente, y sonrío por primera vez en este día."



label es_A29a:


scene bg school_hallway3
show crowd
with None

play ambient sfx_crowd_indoors

"Normalmente me dejaría llevar por la corriente y almorzaría por mi cuenta, pero este día es diferente."

"Este día, he sido invitado a almorzar en la azotea."

"Un lugar peculiar, pero es ahí donde se me dijo que fuera."

"Afortunadamente, me las arreglo para encontrar refugio de la tormenta al abrigo de la puerta del salón de clase."

stop ambient fadeout 1.0

hide crowd
with Dissolve(2.0)

"Eventualmente el torrente se tranquiliza y doy un paso precavido en el corredor."

"Solo para ser recibido por Emi, quien viene volando como bala de cañón."

play music music_emi fadein 0.3

show emi basic_happy at center
with charaenter

emi "¡Hey! ¡Qué tal Hisao! ¡Justo a tiempo!"

show emi excited_proud
with charachange

emi "¡Hoy tengo un almuerzo super extra, como lo prometí! ¡Vamos arriba!"



label es_A29b:



stop music fadeout 2.0
stop ambient fadeout 1.0

scene bg school_staircase1
with locationchange

"La escalera a la azotea está un poco descuidada, pero está claro que se ha estado usando recientemente."

"En la parte más alta de las escaleras se encuentra una puerta, con todo y candado perdido."

"¿Me pregunto quién será ese intrépido individuo que quitó el candado?"

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 2.0

scene bg school_roof at bgright
show emi basic_closedgrin at center
with Fade(0.5,0.3,1.0,color="#FFF")

"Emi abre la puerta de un empujón y entra radiante a la luz del sol."


show rin silhouette at offscreenright
with None

show bg school_roof
show emi basic_closedgrin at left
show rin silhouette at tworight
with ease

show emi basic_shock
with vpunch

"De pronto aparece un extraño alto y oscuro de la nada, de pie e imponente frente a nosotros. Emi se estremece, y casi cae por las escaleras."

$ doublespeak (emi, rin_, u"¡Aaay!", "Hola.")

show emi basic_hes
with charachange

show emi basic_hes at twoleft
with charamove

emi "¡Cielos! ¡Rin, me asustaste!"

"Espera, ¿no es ella…?"

show rin relaxed_surprised
with charachange

play music music_rin fadein 2.0

rin "Hola."

"Al notar que Rin me hablaba a mí, Emi me ve con curiosidad."

show emi basic_confused
with charachange

emi "¿Ustedes dos se conocen?"

"Veo a Emi con confusión."

hi "¿Acaso ella es esa amiga tuya?"

show rin relaxed_nonchalant
with charachange

"Rin ha volteado su mirada hacia las nubes flotando por sobre la escuela."

rin "No sabía que conocieras a esta persona, Emi."

stop music fadeout 2.0

"…"

"El incómodo silencio dura tan solo unos segundos hasta que Emi deja salir una pequeña risilla, haciendo a un lado la coincidencia."

show emi basic_closedgrin
with charachange

emi "Invité a Hisao a almorzar. Si lo conoces, es aún mejor."

show rin basic_deadpan
with charachange

rin "Oh. ¿Esto significa que a mí no me toca comida? ¿O lo invitaste a almorzar sin el almuerzo?"

show emi basic_grin
with charachange

emi "Ahh, ninguno, traje comida para tres."

show rin basic_deadpanamused
with charachange


rin "Bien pensado."

hide rin
hide emi
with charaexit

"Ellas caminan al otro lado de la azotea mientras yo me quedo en la torre del reloj por un tiempo, tomando la atmósfera."

play music music_soothing fadein 0.5

"No hay nadie más que nosotros aquí. Creo que la azotea no es un lugar muy popular como lo es en las demás escuelas."

"Unas cuantas bancas y mesas desgastadas se encuentran desperdigadas por las orillas, quizás en un intento de hacer ver este lugar menos desolado."

"Los guijarros que cubren la azotea resuenan bajo nuestros pies."

"Me asomo a través de la cerca de malla metálica para echar un vistazo a los terrenos de la escuela y más allá."

"Estudiantes pasean en parejas y grupos por el patio y en la cafetería."

"Algunos camiones de entrega pasan la escuela hacia las tiendas cercanas."

"En alguna parte un perro guardián le ladra a un transeúnte."

"De algún modo, cuando miro al centro del pueblo, el sentimiento de ciudad pequeña resuena con fuerza, siendo casi palpable."

"La vida apresurada de las grandes metrópolis parece ser tan lejana y externa; nadie tiene que correr para alcanzar el autobús como si su vida dependiera de ello o tener sus sentidos sobrecargados con las luces de neón y embotellamientos de tráfico."

"Me siento sorprendentemente optimista sobre esta nueva vida mía, viendo al pueblo donde viviré, incluso si tan solo estaré en él por un corto año."

"El descubrimiento de mi enfermedad y tener que mudarme lejos de casa, todo vino tan pronto que no había tenido tiempo de pensar en cómo me siento al respecto."

"Cuando salgo de la sombra de la torre del reloj, siento el calor tocar mi espalda."


"El sol brilla desde un cielo celeste perfectamente despejado."

"Una brisa fresca barriendo la azotea me hace temblar, pero es solo por un instante."

"El viento lleva consigo el aroma de árboles y flores, no el esmog y humo de auto como solía hacerlo hace unas cuantas semanas."

"Emi se sienta en una banca con Rin a rastras y saca dos cajas pequeñas de almuerzo y una grande de su bolsa."

show rin basic_deadpannormal at tworight
show emi basic_happy at twoleft
with charaenter

emi "¡Vamos, Hisao! ¿Qué estás esperando?"

"Ella me insta a que me les una, haciendo espacio en la ya de por sí pequeña banca."

hide emi
hide rin
show bg school_roof at bgleft
with charamoveoutleft

show emi basic_happy_close at closeleft
show rin basic_deadpannormal_close at closeright
show bg school_roof at center
with charamoveinleft


"Me siento en la orilla de la banca para tomar el mínimo espacio posible. Está bastante estrecho, pero de alguna manera los tres cabemos en ella."

hi "Impresionante vista."

show emi basic_closedhappy_close
with charachange

"Emi suprime una risa y coloca uno de sus almuerzos frente a Rin, y me entrega otro a mí."

show emi excited_proud_close
with charachange

emi "¡Aquí tienes! ¡El almuerzo, como lo prometí!"

"Hecho en casa, incluso. Estoy impresionado."

hi "Vaya. Esto se ve realmente bueno."

show emi excited_amused_close
with charachange

emi "¡Gracias! Los hago yo misma cuando puedo."


"La conversación va muriendo mientras me concentro en la cuestión de alimentarme."

show rin basic_awayabsent_close
with charachange

"Tomando unos bocados, miro hacia arriba y veo a Rin abriendo habilidosamente la caja de su almuerzo y poniendo un tenedor lleno de comida dentro de su boca, usando solo sus pies."

"A pesar de ya haberlo visto antes, no puedo evitar estar impresionado por su destreza."

"Es también un recordatorio del tipo de lugar donde me encuentro ahora."

"¿Habrá algún momento cuando me acostumbre a escenas como esta?"

"Tampoco puedo decidirme si habituarse a cosas como estas sea algo bueno o algo malo."

"¿Será que habituarse a este lugar significa que estoy renunciando a ser una persona normal?"

"¿O solo querrá decir que estoy obteniendo un mayor entendimiento sobre quienes me rodean?"

"Me distraigo de mis pensamientos al ver a Emi desgarrando su almuerzo como si hubiera insultado a sus antepasados."

show rin basic_absent_close
with charachange

hi "Te ves muy hambrienta."

show emi basic_grin_close
with charachange

"Emi voltea hacia arriba, boca medio llena, y traga antes de asentir."

emi "Mis carreras matutinas siempre me abren el apetito."

show emi basic_closedhappy_close
with charachange

emi "Lo cual es genial, porque entonces arraso con el almuerzo bastante rápido."

show emi excited_proud_close
with charachange

emi "Me ayuda a mantener mi figura femenina."

show rin basic_deadpan_close
with charachange

rin "¿Qué sucedería si la perdieras? ¿Te convertirías en hombre?"

"Por poco me ahogo con mi almuerzo tratando de no reírme."

show emi basic_annoyed_close
with charachange

emi "Es una forma de hablar."

show rin basic_deadpandelight_close
with charachange

rin "¿Acaso tu figura también tiene que correr por las mañanas?"

hi "¿Siempre hablan de este modo?"

show rin relaxed_surprised_close
show emi basic_confused_close
with charachange

$ doublespeak(emi, rin, u"¿Hablar de qué modo?", u"¿De qué modo?")

"Creo que eso responde mi pregunta."

hi "Eh, no importa."

hi "Así que, eh…"

"Me cuesta pensar en algún tema de plática y me conformo con la pregunta obvia."

hi "¿Cómo es que ustedes se conocieron?"

show rin basic_awayabsent_close
with charachange

"Rin parece estar de acuerdo con dejar contestar a Emi esta pregunta."

show emi basic_grin_close
with charachange

emi "Alguien en el departamento de vivienda pensó que nos complementaríamos bien la una con la otra, entonces se nos asignaron habitaciones contiguas."

hi "¿Complementarse la una con la otra?"

show rin basic_deadpannormal_close
with charachange

rin "Como zapatos y un traje."

hi "¿Eh?"

show emi basic_closedgrin_close
with charachange

"Emi se ríe de mi confusión."

emi "Júntanos a las dos y tenemos todas las extremidades, ¿entiendes?"

hi "Ah."

show emi basic_happy_close
with charachange

emi "¡Así que empecé a ayudarle a Rin a alistarse en las mañanas, y eso fue todo!"

show emi basic_grin_close
with charachange

emi "Quiero decir, no puedes ayudarle a vestirse a alguien todas las mañanas y no llevarte bien."

hi "Ya veo."

"Rin escoge este momento para intervenir."

show rin basic_deadpan_close
with charachange

rin "Tengo problemas con las camisas."

hi "Cierto, eso parece… bastante obvio."

show rin basic_surprised_close
with charachange

rin "¿En verdad?"

hi "¿Un poco…?"

"Esto no parece estar ayudando, pero por lo menos Emi parece encontrar todo este asunto divertido."

"Eso, combinado con el hecho de que Rin es realmente curiosa, me hace sentir ligeramente mejor y, sin embargo, confundido."

hi "Digo, no tienes brazos."

hi "Entonces ah, ponerse una camisa parece como una de esas cosas que serían… difíciles."

"¿Saben qué? Simplemente me quedaré callado de ahora en adelante."

"Me ahorrará muchos problemas a la larga."

"Rin asiente en lo que me parece se supone ser una manera sabia."

show rin basic_lucid_close
with charachange

rin "Ya veo."

show rin basic_absent_close
with charachange

"La conversación termina mientras dirijo mi atención de vuelta a mi almuerzo."

"Es en realidad muy bueno."

"Emi acaba con su almuerzo primero y hace un ruido de satisfacción."

show emi excited_laugh_close
with charachange

emi "Ah, eso estuvo bueno."

"En lo que ella se ocupa de terminar su almuerzo, Rin habla."

show rin basic_deadpan_close
with charachange

rin "Tengo sed."

show emi basic_shock_close
with charachange

emi "¡Oh! ¡Casi me olvido de eso! ¡Perdón!"

show emi basic_closedgrin_close
with charachange

"Con un gesto, ella busca en su bolsa y saca un trío de cajitas de jugo."

"Me lanza uno que parece ser jugo de arándano, otro para Rin que parece leche de fresa (con todo y diseño rosado), y se queda con algún (igualmente rosado) tipo de ponche de frutas para sí misma."

show rin basic_awayabsent_close
with charachange

"Rin diestramente encaja su pajilla a través del tope de su cajita de jugo y comienza a beber."

"Una vez más me encuentro asombrado por lo flexible que es, pero ahora decido quedarme con mi comentario."

"De alguna manera, no pienso que Emi o Rin sean el tipo de personas que piensen dos veces sobre el modo de cómo sortean sus discapacidades."

"Especialmente Rin."

"Seguramente, da la impresión de ignorar por completo que le hagan falta extremidades en lo absoluto."

"Sea o no una decisión consciente, es un asunto aparte."

"Honestamente no estoy seguro."

show emi basic_grin_close
with charachange

emi "Así que, Hisao, ¿qué te parece acá arriba?"

show rin basic_absent_close
with charachange

hi "¿Hmm?"

hi "Es bastante agradable, en verdad. Me gustan los lugares altos, por la vista."

hi "Gracias por invitarme a venir aquí."

hi "Y por el almuerzo, también."

show emi excited_amused_close
with charachange

"Emi muestra una sonrisa de mil watts, complacida por mi respuesta supongo."

emi "¡No hay problema!"

show emi excited_proud_close
with charachange

emi "Siéntete libre de comer con nosotras la próxima vez, ¿está bien?"

emi "No te haré el almuerzo, pero puedes traer el tuyo acá arriba."

hi "¿Sin servicio de almuerzo? No estoy seguro…"

show emi basic_annoyed_close
with charachange

"Emi se hace la ofendida."

emi "¿Tratando de aprovecharte de mi buena voluntad?"

emi "¡Qué atrevimiento!"

show emi basic_closedgrin_close
with charachange

"Emi ríe."

show emi sad_depressed_close
with charachange

emi "Bueno, si esa es tu respuesta, creo que Rin y yo tendremos que seguir comiendo completamente solas…"

"Soy súbitamente asaltado por la interpretación más desgarradora de ojos de perrito que he visto nunca cuando Emi hace un puchero."

hi "¡Bromeaba! ¡Solo bromeaba!"

hi "Me encantaría almorzar aquí de nuevo."

hi "Buen lugar, y la compañía también es buena."

show emi basic_grin_close
with charachange

"Emi frunce un poco el ceño por mi declaración de “buena” pero parece estar bastante contenta de que haya aceptado su invitación."

"Creo que esto nos hace amigos."

"O al menos conocidos."

play sound sfx_warningbell

"La campana del almuerzo suena, señalando el regreso a abajo."

show emi basic_hes_close
with charachange

emi "¡Rin, no terminaste tu almuerzo otra vez!"

show rin basic_deadpan_close
with charachange

rin "No tenía tanta hambre."

show emi basic_annoyed_close
with charachange

emi "¡Si no comes más, te desmayarás!"

show rin relaxed_boredom_close
with charachange

"Rin se encoge de hombros, como si esto fuera un riesgo aceptable."

stop music fadeout 4.0

hi "Vamos, será mejor que nos vayamos."

stop ambient fadeout 2.0

scene bg school_staircase1
with locationchange

"Los tres bajamos las escaleras juntos."

scene bg school_scienceroom
with shorttimeskip

"Las clases de la tarde terminan. Una vez más, me encuentro sin un plan para hacer algo después de clase, así que me dirijo a la biblioteca para devolver un par de libros que he terminado de leer."

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

scene bg school_library
with locationskip

"Al entrar, veo que hay tantos estudiantes como los hubo el martes, es bastante más evidente por la casi totalidad del silencio envolviendo el lugar."


play sound sfx_impact2
with vpunch

show yuuko panic_up at center
with easeinbottom

play music music_happiness fadein 2.0

"Al echar los libros que pedí prestados dentro de la rendija de devoluciones en el mostrador, Yuuko súbitamente aparece detrás de ella, muy sobresaltada a causa del golpe que resuena cuando llegan al carrito a su lado."

hi "Ah, lo siento Yuuko. No quise asustarte."

show yuuko worried_up
with charachange

yu "No, no. Está bien. Eso sucede… mucho. Ya estoy acostumbrada."

show yuuko neurotic_up
with charachange

yu "Eh, ¿puedo ayudarte?"

hi "Está bien, creo saber dónde queda todo. Gracias de cualquier forma."

hide yuuko
with charaexit

"Supongo que iré por otro libro o dos ya que estoy aquí. No hay mucho más que hacer, y después de leer tanto durante mi estancia en el hospital, se ha convertido en un hábito difícil de romper."

stop music fadeout 5.0

"Recorro la sección de ficción hacia la parte trasera de la biblioteca, examinando los estantes por cualquier cosa que me llame la atención."

"Mientras lo hago, volteo hacia la esquina donde Hanako se encontraba la última vez que estuve aquí, sin esperar hallar algo en realidad."

scene ev hana_library_read_std
with locationskip

"… aunque, por sorpresa, ella está ahí, completamente absorbida en un libro de lo más grueso. Decido no entrometerme como la última vez y regreso a buscar material de lectura."

scene bg school_library_ss
with shorttimeskip

play music music_tranquil fadein 6.0

"Después de una cantidad imperceptible de tiempo andando por los pasillos, finalmente escogí un par de libros y los deslicé fuera de la repisa."

"Con el mínimo ruido, camino de regreso al mostrador, registro mis libros y los meto dentro de la mochila mientras camino hacia fuera."

scene bg school_courtyard_ss
with locationskip

"Para cuando salgo del edificio principal, la puesta de sol no se encuentra lejana. Un pequeño flujo de estudiantes queda todavía, pero la mayoría ya se ha marchado; presumiblemente a sus casas o dormitorios."



label es_A29c:

scene bg school_dormhisao_ss
with locationskip

"Sintiéndome completamente agotado, me dirijo a mi habitación para leer los libros que pedí prestados. Ya ha habido suficiente acción y emoción por un día."

"El primero es “Alicia en el País de las Maravillas”. Conozco la historia, por supuesto; pero en realidad nunca había leído el libro original."

"Es exactamente igual de extraño a como recuerdo la historia, con personajes absurdos y trama incoherente."

"Empiezo a pensar en mí mismo como una especie de Alicia también, desventuradamente cayendo por el agujero de conejo hacia este Lisiado País de las Maravillas."

"… Está bien, eso es una expresión bastante fuerte. Aun así, la ubicación aislada y la manera abierta de cómo la escuela se acomoda a absolutamente todo es inquietante. Es como otro mundo."

"Me pregunto por qué no puedo deshacerme de este sentimiento de ser un forastero como Alicia, a pesar de que casi todos sean tan hospitalarios y amistosos conmigo."

"Pasando a otra página, mi mente comienza a flotar a la deriva cada vez más lejos del libro. Todo se encuentra tranquilo, puedo escuchar los latidos de mi corazón golpeando suavemente contra la tela de mi camisa."

"Por alguna razón, esto me hace sentir realmente mal desde aquella vez en el bosque con Iwanako. Como si estuviera encerrado en una jaula con algo horrible y tenebroso."

stop music fadeout 5.0

scene bg school_dormhisao_ni
with Dissolve(3.0)

"Dejo el libro por un rato y miro hacia el techo, tomando mi tiempo para quitarme esa sensación de encima."

"200 páginas después, me duermo."


scene black
with shuteye




label es_A30:

scene bg school_courtyard_ss
with None

$ renpy.music.play(music_tranquil, fadein=3.0, if_changed=True)

"Supongo que debo comprar algunos suministros. No puedo vivir de la comida de la cafetería y comiendo fuera durante toda mi estancia aquí."

scene bg school_gate_ss
with locationchange

"Al salir por el portón, hago unos pocos estiramientos para tratar de vencer el cansancio acumulado durante la semana."

scene bg school_road_ss
show lilly back_smileclosed_ss at center
show lillyprop back_cane_ss at center
with locationchange



"Sin embargo, después de pasar a través y rodear la esquina, veo una figura solitaria bajando la colina hacia el pueblo. El color de su cabello y el golpeteo de su bastón son inconfundibles."

show lilly cane_surprised_ss
hide lillyprop
with charachange

"Rápidamente camino en su dirección, un acto que parece llamar su atención sin necesidad de decir una palabra."

hi "Qué tal, Lilly."

show lilly cane_weaksmile_ss
with charachange

"Se toma un momento para localizar la voz, ligeramente ajustando su cabeza para volverse un poco más hacia el origen de mi voz mientras lo hace."



show lilly cane_smile_ss
with charachange

li "… ¿Hisao?"

hi "Síp, ese soy yo."

"Parece tener buena memoria para las voces. El hecho de que haya recordado es en realidad una agradable sorpresa."

li "Buenas tardes. ¿Qué te trae por aquí?"

show lilly cane_weaksmile_ss
with charachange

"Una vez más, hace una pequeña y cortés reverencia. Y, una vez más, respondo de la misma forma antes de darme cuenta de que no es necesario hacerlo."

hi "Solo voy al pueblo, ¿y tú?"

show lilly cane_ara_ss
with charachange

li "Vaya, vaya, pero qué coincidencia."

hi "Haciendo lo mismo, ¿eh?"

show lilly cane_smile_ss
with charachange

li "Mm. Usualmente voy de compras los viernes."

show lilly cane_surprised_ss
with charachange

"Hace una pausa por un momento, súbitamente viéndose un poco perdida."

li "Habiendo dicho eso, Hanako usualmente viene al pueblo conmigo…"

"Ah. No perdida, sino preocupada. Ambas parecen mantener lazos muy cercanos. Es un poco sorprendente que Hanako se haya simplemente olvidado de Lilly de esa manera."

hi "La encontré leyendo en la biblioteca. Probablemente se quedó absorta en un libro."

show lilly cane_weaksmile_ss
with charachange

"Ella deja salir un leve suspiro de alivio."

li "Gracias. Ella tiene el hábito de hacer eso."

hi "¿Lectora ávida?"

show lilly cane_smile_ss
with charachange

li "Sí. A ella no le agrada estar en grupos grandes de gente, así que leer lejos de los demás le permite relajarse un poco."

"Aunque probablemente ella no lo hacía con esa intención, no puedo evitar una mueca al recordar nuestro primer encuentro."

show lilly cane_smileclosed_ss
with charachange

"Sin ganas de sacarlo al aire, me quedo en silencio mientras continuamos caminando por la tranquila calle."

"Tac, tac. Tac, tac."

"Con la calle desprovista de autos y los estudiantes de Yamaku cada vez más lejos de nosotros, el callado susurro de las hojas y el golpeteo mesurado del bastón de Lilly contra la acera es todo lo que se puede oír."

"Es un poco agradable, especialmente comparado con el bullicio de donde solía vivir."

"Sin darme cuenta, me he relajado tanto que un gran bostezo se me escapa antes de que pueda controlarlo."

show lilly cane_giggle_ss
with charachange

li "¿Cansado?"

hi "Sí, estuve corriendo por todas partes estos últimos días."

"Eso es un eufemismo, para estar seguro. Transferirse a una escuela diferente sería suficientemente malo, pero nada como esto…"

show lilly cane_smile_ss
with charachange

li "Bueno, esperemos que todo se tranquilice para ti. El festival ha puesto a todos en un embrollo, y tú has sido arrojado en medio de todo esto."

"Titubeo por un momento, pero dada su aparente tolerancia a la franqueza, decido dar por entero mis pensamientos."

hi "Eso creo. Yamaku es un lugar algo diferente. Lo que quiero decir es: la formalidad rodeando todo, el aislamiento a su alrededor… sin mencionar la más obvia diferencia."

hi "Es como una mentalidad completamente diferente. Sin embargo, supongo que me acostumbraré con el tiempo."

show lilly cane_smileclosed_ss
with charachange

"Ella asiente de forma prosaica, aparentemente satisfecha con mi respuesta. Se siente casi como si me hubiera incluido en el rebaño de estudiantes que está guiando, junto con el grupo 3-2 y Hanako."

"Bueno, no es que me queje. Es bueno sacarme los pensamientos de la cabeza, en cualquier caso."

show lilly cane_smile_ss
with charachange

li "Viendo el lado amable, uno podría verlo como una oportunidad para un nuevo inicio. Deberías atesorar la oportunidad de hacer nuevos amigos."

"Eso es optimista. Aun así, es bueno tener una actitud positiva sobre estas cosas, supongo."


hi "Creo que es una buena forma de verlo."

scene bg suburb_roadcenter_ss
show lilly cane_reminisce_ss at center
with shorttimeskip

stop music fadeout 6.0

"Caminando por la calle, ella parece tornarse un poco inquieta. Antes de poder preguntarle qué es lo que piensa, ella parece tranquilizarse y habla sobre algo más."

show lilly cane_weaksmile_ss
with charachange

li "Entonces, ¿adónde es que vas en el pueblo?"

"Esa es en verdad una muy buena pregunta. Había venido a comprar comida, pero la composición del lugar es todavía un misterio para mí."

"Tenía la intención de simplemente deambular por ahí y ver qué me encontraba, pero con la puesta de sol acercándose y el anochecer no muy lejano, eso no parece muy inteligente."

"Tendré que preguntarle por direcciones. De nuevo."

hi "Solo iba a comprar comida… pero ahora que lo mencionas, en realidad no sé el camino."

show lilly cane_planned_ss
with charachange

li "Oh vaya, esto es bastante afortunado. Iba a ir al almacén por mi cuenta."

hi "Parece ser que estaré bajo tu cuidado otra vez, entonces. Gracias."

"Juntos caminamos a la tienda, mi paso cuidadosamente reducido para mantenerme a su lado. Comparado con mi ritmo de caminar usual, el suyo es bastante más lento. No es como si fuera sin razón."

scene bg suburb_konbiniext_ss
with shorttimeskip

play music music_daily fadein 2.0

"Después de lo que no podrían haber sido más de algunos minutos, veo nuestro objetivo. Este pueblo es en verdad muy pequeño."

scene bg suburb_konbiniint
with locationchange

"Sin más preámbulos, nos dirigimos hacia el interior con un saludo desde el mostrador."

show lilly cane_weaksmile at center
with charaenter

li "¿Te importa si te acompaño? Usualmente Hanako me ayudaría, pero ya que ella no está aquí…"

"Me toma un momento para entender qué es lo que quiere decir."

"Considerando que ella no podría ser capaz de leer ninguna de las etiquetas, ir de compras sin ninguna ayuda sería un gran problema para ella."

"Con eso dicho, no puedo ignorar la sensación de que ella ya había tenido esta idea desde que dije que vendría aquí."

hi "Seguro. Sería un placer."

"Agarro dos cestos rojos bastante usados de la pequeña pila al lado de la entrada y le entrego uno a Lilly."

show lilly cane_weaksmile at Transform(ypos=800)
with charamove

show lilly basic_smileclosed at Transform(ypos=800)
with charachange

show lilly basic_smileclosed at center
with charamove

"Ella lo deja en el suelo, poniendo su mochila dentro, repliega su bastón y lo desliza a través del asa del cesto antes de levantarlo de nuevo con su mano derecha."

"Espera, si ella no usa su bastón…"


show lilly basic_smileclosed at Slide(0.5,0.5,0.3,0.5,1.0, time_warp=_ease_time_warp)
with None

show lilly basic_smileclosed_close at Slide(0.5,0.5,0.3,0.5,1.0, time_warp=_ease_time_warp)
with Dissolve(1.0)

"Antes de que pueda terminar el pensamiento, ella viene a mi lado y pellizca el puño de mi uniforme con sus esbeltos dedos."

show lilly basic_concerned_close at twoleft
with characlose


li "¿Te parece bien esto?"

hi "Ah, seguro."

show lilly basic_smileclosed_close
with characlose

"No tengo razón alguna para decir que no. Puedo pensar en peores cosas que ir de compras con una chica bonita sosteniéndose de mí, inclusive si es por necesidad."

"Navegamos nuestro rumbo a través de la tienda, donde ni un solo cliente ocasional que iba de pasada parecía inmutarse."

"Considerando qué tan cerca se encuentra Yamaku, creo que ver estudiantes de ahí debe ser completamente normal para los residentes locales."

"Al llegar a cada pasillo, rápidamente reviso con Lilly y encuentro lo que necesita. Lo tomo junto con lo que yo busco, y pongo los artículos en nuestros respectivos cestos."

"Supongo que esta es la misma rutina que Hanako y ella siguen cada viernes."

hi "Bien, todo lo que resta es el pan y eso terminaría con mis compras. ¿Necesitas algo más, Lilly?"

show lilly basic_smile_close
with characlose

li "No, esto debería ser todo."

hi "Entonces, nos vamos."

show lilly basic_smileclosed_close
with characlose

"Con un pequeño desvío a la sección de la panadería, nos dirigimos a la caja."

"La fila, por suerte, es casi inexistente. No toma mucho tiempo antes de que ambos paguemos por nuestra comida y salgamos por la puerta."

scene bg misc_sky_ni at Fullpan(15.0)
with locationchange

"Entretanto Lilly retoma su bastón y lo extiende por completo, pierdo un minuto viendo hacia arriba en el cielo nocturno mientras sostengo nuestras bolsas."

"Por un momento trato de hacer nubes con mi aliento, pero el calor del verano no parece cooperar."

"Eventualmente ella se endereza, tomando la oportunidad para estirarse rápido antes de tomar su bolsa y dejarme con las dos mías."

scene bg suburb_konbiniext_ni
show lilly cane_listen_ni at center
with locationchange

hi "¿También estás cansada?"

show lilly cane_sleepy_ni
with charachange


li "Los preparativos para el festival han sido un completo caos. Shizune acosándome todo el tiempo tampoco ayuda, realmente."

hi "Oye, ella solo trata de tener todo organizado. Mejor ahora que más tarde, ¿cierto?"

show lilly cane_weaksmile_ni
with charachange

li "Supongo que sí. Disfrutaré relajándome por el pueblo mañana, eso es seguro."


"Creo que los preparativos deben de estar teniendo un efecto negativo en ellas dos."

scene bg suburb_roadcenter_ni at bgright
with locationchange

"Caminamos dentro de una calle tranquila, hablando entre nosotros mientras cargamos nuestras bolsas de comida y suministros de la tienda."

"… Espera, ¿qué es eso?"

"Noto una figura muy distintiva viniendo hacia nosotros, solo su silueta definible a causa de los faroles."

"Por un segundo pienso que se trata de otro estudiante varón de mi grupo, pero a medida que él; o debería decir ella, se acerca la reconozco rápidamente."

show bg suburb_roadcenter_ni at center
show rin relaxed_nonchalant_ni at right
with charamoveinright

stop music fadeout 8.0

hi "¿Rin? ¿Qué estás haciendo aquí afuera tan tarde?"

show lilly cane_surprised_ni at center
with charaenter

li "¿Rin?"

"Lilly levanta la cabeza, como si tratara de concentrarse en escuchar más claramente. De pronto me viene que probablemente debería de interpretar la escena para ella."

hi "Es Rin… Tezuka, creo que era su apellido, de nuestra escuela."

show lilly cane_weaksmile_ni
with charachange

"Lilly se tensa con el nombre y muestra una expresión de apariencia complicada, algo como una fusión forzada entre una sonrisa serena y un doloroso horror."

li "Ah. Entiendo."

"Creo que Lilly también conoce a Rin."

show rin basic_awayabsent_ni
with charachange

show bg suburb_roadcenter_ni at bgleft
show rin basic_awayabsent_ni at tworight
show lilly cane_weaksmile_ni at twoleft
with charamove

"Rin se gira para vernos, viéndose terriblemente desorientada. No estoy completamente seguro de que reconozca a alguno de nosotros, o si lo hace no se da cuenta de ello."

"Parece un zombi. O una estatua. Una estatua de un zombi."

"Pero lentamente, algunos síntomas de comprensión parecen iluminar sus ojos oscuros: esto es algo a lo que debe reaccionar."

show rin basic_lucid_ni
with charachange

show rin basic_awayabsent_ni
with charachange

"Rin parpadea una vez. Muy meticulosamente."

show rin basic_absent_ni
with charachange

rin "Hola."

"…"

"Hay una pausa incómoda, todos esperando a que otra persona diga algo."

hi "¿Qué estás haciendo aquí tan tarde?"

"…"

rin "Yo…"

show rin basic_deadpan_ni
with charachange

rin "Me estaba preguntando sobre eso, también. Justo ahora."


play music music_rin fadein 0.5

show rin basic_deadpannormal_ni
with charachange

rin "Algunas personas preguntaron eso hace solo un rato. Imagino que tenían la misma duda."

rin "No sabía. Ellos tampoco sabían. Pregunté. Es por eso que también tengo esa duda."

rin "Y fue más o menos así. Es el misterio de un asesinato sin el asesinato."

"…"

show rin negative_spaciness_ni
with charachange

rin "Estaban yendo para allá."

show rin basic_absent_ni
with charachange

"Se da vuelta hacia su derecha para demostrar la dirección que las otras personas tomaron, como si eso fuese importante, entonces se vuelve de nuevo como un títere mecánico en uno de aquellos mecanismos de relojería sumamente complicados."

"Para una persona que da la impresión de ser del tipo callado, Rin en verdad usa muchas palabras para decir cosas que no necesitan tantas para decirse."

"Inseguro de si ya ha terminado, no digo nada. Tampoco lo hace Lilly, quien parece estar igualmente despojada de palabras de momento."

"Pienso que ambos estamos, de hecho, igualmente asustados de que cualquier tipo de respuesta pudiera provocarla a continuar."

"Nuestra estupefacta carencia de reacción no desconcierta a Rin en lo absoluto. Sigue viéndonos a la expectativa, un apacible atisbo de expresión sobre su rostro en blanco."

"Ella parece ser ese tipo de persona. Siempre relajada."

"Como si sedantes para elefantes fluyeran por sus venas en lugar de sangre."

show lilly cane_concerned_ni
with charachange

li "¿Acaso tienes amnesia? No recuerdo que tuvieses algo por el estilo, aunque…"

hi "No, no creo que sea eso."

hi "Sin embargo, puede ser que los otros transeúntes estuvieran preocupados. Te ves realmente perdida, la manera en la que estás parada en medio de la calle."

show rin basic_deadpan_ni
with charachange

rin "Oh, ya veo."

show rin relaxed_nonchalant_ni
with charachange

rin "Tal vez debería haber tomado otro tipo de pose, en ese caso."

"Considero por un momento si debería seguir este ángulo más a fondo, o darme por vencido por el bien de mi propia cordura."

"Me decido por lo último."

"Parece ser que, la mayoría del tiempo, es mejor no pensar demasiado acerca de lo que Rin balbucea."

"Hablar con Rin es como jugar ajedrez con una supercomputadora que aparentemente hace movimientos completamente al azar como si se burlara de todo lo que sabes de ajedrez. Es como eso, excepto con interacción humana."

"E incluso si ganara, se siente como si perdiera."

"Maldición, es justo como dijo Kenji. Incluso si gano, pierdo. ¿Es este el poder de las chicas de Yamaku?"

"…"

"Hago la idea a un lado como si fuera demasiado peligroso considerarlo más a fondo. Probablemente es solo la propaganda antimujeres de Kenji sorprendiéndome en un momento de debilidad."

hi "Seguro, puede que haber tomado otra pose hubiera funcionado."

hi "Bueno, de todos modos, ¿no tienes ni idea de lo que hacías aquí?"

show rin negative_annoyed_ni
with charachange

"Ella frunce el ceño viéndose extremadamente disgustada por mi pregunta, sus consecuencias, o la respuesta que está a punto de dar."

rin "Sí tengo. Alguna idea. No puedo decir qué tipo de idea, en realidad."

show lilly cane_smile_ni
with charachange

li "Eso suena como un avance, al menos."

"Lilly se escucha como si hubiera encontrado una oportunidad para entablar algún tipo de conversación normal. No puedo decir que comparta su optimismo."

rin "Sí, hay un poco. Definitivamente. El resto vendrá más tarde."

show rin basic_deadpanupset_ni
show lilly cane_weaksmile_ni
with charachange

rin "Estoy segura de eso. Siempre tengo… razones."

"El silencio siguiente mata las esperanzas de Lilly de forma muy clara. Eso no duró mucho."

"Dejando de lado las afirmaciones, hasta donde puedo ver sin fundamentos, de Rin… ¿qué se debería hacer?"

"Podríamos simplemente dejarla con sus propios asuntos, cualesquiera que sean… pero es tarde y no creo que nos agradezcan si Rin es encontrada aquí de pie a la mitad de la noche."

"Lo que posiblemente hará, a menos que logre recordar qué hacía aquí en primer lugar."

"En cuanto a mí intentando adivinar qué podría haber estado sucediendo dentro de su mente cuando decidió embarcarse en esta aventura, la probabilidad parece estar a la par con ganar la lotería."

"Varias veces seguidas."

"Lilly se encuentra extrañamente callada también. Ahora agradecería un poco de apoyo de fuera, especialmente si ella está más familiarizada con Rin que yo."

"Pero no tiene remedio. Parece ser precisamente su familiaridad con Rin lo que la mantiene en silencio."

hi "Entonces, supongo que ibas a algún lado, no regresando a la escuela… ¿alguna idea de a dónde?"

show rin relaxed_surprised_ni
show lilly cane_surprised_ni
with charachange

"Sus ojos se abren por la sorpresa y se sacude de una forma un poco artificial, haciéndolo parecer un acto ensayado para situaciones como esta."

rin "¿Puedes leer la mente? ¿Es esa tu discapacidad? ¡Qué peculiar!"

hi "No… ¿Qué? ¿Por qué pensarías eso?"

show rin relaxed_disgust_ni
show lilly cane_listen_ni
with charachange

rin "Sabías lo que estaba haciendo."

show lilly cane_displeased_ni
with charachange

hi "Ah, fue tan solo una conjetura. Caminamos por esta misma calle en la otra dirección hace poco, para ir a la tienda."

hi "Si hubieras estado yendo a la escuela, te habríamos encontrado en el camino."

show rin basic_deadpanupset_ni
with charachange

rin "Oh."

"Parece un poco decepcionada."

"Al igual que Kenji, Rin parece apresurarse a brincar a conclusiones completamente irracionales."

"Tal vez sea algo en el agua de aquí. Hago una nota mental para abastecerme de bebidas."

hi "Sabes, esta es la segunda ocasión en esta semana que alguien me pregunta si puedo leer la mente."

hi "¿En verdad doy esa impresión?"

show rin basic_deadpannormal_ni
with charachange

"Rin se encoge de hombros, lo cual es lo único que me da como respuesta."

hi "Sabes—{w=0.3}{nw}"

show lilly cane_smile_ni
with charachange

li "Tal vez deberías venir con nosotros de regreso a la escuela."

"Lilly interviene justo cuando estoy a punto de desacreditar aún más mi supuesta capacidad para leer mentes. Ella suena bastante preocupada, la sonrisa tenue en su rostro hace un mal trabajo ocultándolo."

"Puede que haya llegado a la misma conclusión que yo. Por el bien de todos, decido dejar el tema del lector de mentes, ya que es enteramente estúpido."

hi "Sí, Lilly está en lo correcto. Si no puedes recordar, no tiene sentido quedarse aquí."

show rin basic_awayabsent_ni
with charachange

"Rin considera esta relativamente sencilla deducción por un momento, luego asiente."

show rin basic_absent_ni
with charachange

stop music fadeout 2.0

rin "De acuerdo."

scene bg school_road_ni
with shorttimeskip

$ renpy.music.set_volume(0.1, 0.0, channel="ambient")
play ambient sfx_cicadas
play music music_dreamy fadein 2.0

"Nos dirigimos a la escuela de nuevo, habiendo desperdiciado mucho más tiempo del necesario con este episodio."

show rin basic_awayabsent_ni at tworight
show lilly cane_smileclosed_ni at twoleft
with charaenter

"Rin camina al borde de la acera a su manera arrítmica, viéndose como una mezcla de sonámbula y funámbula, mientras Lilly mantiene una de sus manos en mi hombro tocando el suelo con su bastón."

"Tac tap tap tac tac tap tap tap."

"Aparte de eso y un par de fragmentados inicios de conversación, está silencioso. Un silencio muy distinto de aquel de cuando bajábamos al pueblo."

hi "¿Y cómo va el mural?"

show rin basic_deadpan_ni
with charachange

rin "Nos va a dar mala suerte. Nunca hables de trabajos en progreso."

show lilly cane_weaksmile_ni
with charachange

li "Estoy segura de que será maravilloso."

show rin basic_deadpannormal_ni
with charachange

rin "Mala suerte."

"Tac tap tac tap. A ella no le importa hablar de ello. La cortesía de Lilly se siente fuera de lugar, por primera vez. Tap tap tap."

"La colina en la cual, en su parte más alta, descansa Yamaku, es sorprendentemente empinada cuando se va cuesta arriba. Disminuimos el paso, pero aun así siento mi pulso elevarse y la respiración tornarse pesada."

"Casi llegamos, ya puedo ver el portón."

"Aunque, más que eso, me percato de que la mano de Lilly se tensa ligeramente sobre mi hombro. Interpretándolo como un gesto de que quiere preguntar algo, le hablo."

hi "¿Pasa algo malo, Lilly?"

"Resisto la urgencia de decir “¿Aparte de nuestra compañera de viaje?”. Pero solo por poco."

"Por un instante parece considerar si debería siquiera de mencionarlo, pero decide hacerlo de cualquier forma."

show lilly cane_concerned_ni
with charachange

li "¿Está… todo bien?"

hi "¿Todo bien? ¿A qué te refieres?"

"El hecho de que no pueda interpretar su increíblemente vaga pregunta la disuade, por un segundo."

li "Es solo que… pareces estar muy cansado, eso creo."

"Ahora que lo menciona, me doy cuenta de que mi respiración es extrañamente pesada. La caminata cuesta arriba ha hecho estragos en mí."


label es_choiceA30:
menu:
    with menueffect
    "Lilly lo notó demasiado pronto…"
    "Perdón, no estoy en muy buena condición.":


        return m1
    "En verdad no quiero hablar de eso.":

        return m2

label es_A30a:

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
stop music fadeout 5.0

hi "E… estoy bien."

hi "No hay nada de qué preocuparse, la colina solo es sorpresivamente empinada, ¿no crees?"

hi "Me pregunto por qué es que tienen la escuela tan alta de todas maneras, ¿acaso no tenemos estudiantes en sillas de ruedas y todo?"

show lilly cane_sad_ni
with charachange

li "En efecto."

show lilly cane_concerned_ni
with charachange

"La frente de Lilly se arruga con preocupación, y yo realmente no quiero que tenga ese tipo de expresión por mí. Apenas nos conocemos."

hi "Sí, justo lo que pensaba. No es como si pudieras encontrar un lugar así en donde sea, supongo, pero eso me hace dudar de en qué estaban pensando."

"Mi voz es en exceso tranquila, suena rara a mis propios oídos y hablo demasiado rápido. Por un momento me pregunto qué tanto puede intuir Lilly solamente con la voz de alguien."

li "Mmm…"

hi "Continuemos. Ya estamos por llegar de todas maneras."

hide lilly
hide rin
with charaexit

"Por el resto del camino de vuelta a la escuela, todos nos mantenemos en silencio."

stop ambient fadeout 3.0

scene black
with Dissolve(3.0)


label es_A30b:

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")

hi "Todo está bien, solo necesito recuperar el aliento. Mi condición no es la mejor, estos días."

show lilly cane_oops_ni
with charachange

li "Oh."

li "¿Es eso algo que… esté relacionado con que hayas sido transferido aquí? Quiero decir…"

show lilly cane_concerned_ni
with charachange

"Ella para de hablar de una forma bastante abrupta, tal vez dándose cuenta de que estaba siendo un poco intrusiva. Sus instintos son agudos, y aunque no me agrade el tema no es como si debiera mentir sobre ello."

"Si se trata de Lilly, no creo que me moleste."

hi "Es solo que me encuentro un poco débil por el momento."

show lilly cane_oops_ni
with charachange

li "Hanako dijo que te veías bastante… sano, así que naturalmente pensé…"

show lilly cane_sad_ni
with charachange

"Lilly vuelve a no terminar su oración, dejándola irse con un grado de preocupación."

"A medida que frunce el ceño, la incómoda expresión de Lilly me empuja a por lo menos decir algo para aliviar sus sentimientos."

"Es sorprendente que esté así de agitada, considerando la actitud directa que tiene con su propia ceguera. Ella debe saber que no todos comparten tal holgura sobre dichas cosas."

hi "No, está bien."

hi "Tengo un corazón… creo que la mejor manera de decirlo sería… hecho un desastre. Arritmia."

hi "Tuve un ataque cardiaco fuerte hace un tiempo a causa de eso, y pasé la mayoría de la primavera en un hospital. Terminé en Yamaku bajo las órdenes del doctor."

"Ella asiente silenciosamente en entendimiento."

"Mi respuesta, sin embargo, únicamente logra hacer fruncir aún más el ceño a Lilly. No parece saber muy bien cómo reaccionar, ya que en realidad no nos conocemos tan bien."

"Realmente no puedo culparla por ello, dado que incluso yo tengo esa misma reacción."


label es_A30c:

"Para mi sorpresa, en espacio de un momento su rostro muestra que ha llegado a alguna clase de realización."

show lilly cane_oops_ni
with charachange

li "Espera… ¿entonces aquella vez cuando Emi y tú chocaron en el corredor…?"

"Hago una mueca ligeramente. Su habilidad de conectar puntos tan rápido es inesperada."

hi "Sí. Creo que soy un ejemplo andante del porqué existen esas reglas sobre correr en los corredores."

show lilly cane_sad_ni
with charachange

"Eso fue bastante más seco de lo que había previsto. Lilly rehúye visiblemente el continuar con el tema."


label es_A30d:

"Aunque sí quiero aliviar su preocupación, realmente no quiero hacer hincapié en esto tampoco."

hi "No te preocupes por eso."

show lilly cane_weaksmile_ni
with charachange

"Intento ofrecer una sonrisa tranquilizadora pero entonces me doy cuenta de la futilidad. Sin saberlo, Lilly me sonríe con serenidad pero no dice nada más."

$ renpy.music.set_volume(0.5, 5.0, channel="ambient")
stop music fadeout 2.0

scene bg school_dormext_half_ni
show rin relaxed_surprised_ni at tworight
show lilly cane_weaksmile_ni at twoleft
with shorttimeskip

"Llegando a los dormitorios, Rin se detiene frente a su mural como si un rayo la hubiese alcanzado. Se había encontrado tan callada por casi todo el camino de regreso que me olvidé por completo de que ella estaba aquí."


show rin relaxed_disgust_ni
with charachange

rin "Es viernes, ¿no es así?"

show lilly cane_smile_ni
with charachange

li "Sí… viernes, ocho de junio."

show rin basic_upset_ni
with charachange

play music music_rin fadein 0.5

rin "Esto es malo."

show lilly cane_surprised_ni
with charachange

li "¿Malo? ¿Por qué?"

show rin negative_annoyed_ni
with charachange

rin "Creo que me pondré en posición fetal y vomitaré. Posiblemente en orden inverso."

show lilly cane_concerned_ni
with charachange

li "¿Ocurre algo malo?"

show rin negative_confused_ni
with charachange

rin "No. Nada está mal. Es viernes y nada está mal aún. Este mural, necesitará ser terminado para el domingo. Así que todo está bien."

show rin negative_worried_ni
with charachange

rin "¿Tienen drogas? ¿O una máquina del tiempo?"

show rin negative_confused_ni
with charachange

rin "Esto no está bien. Nada bien."

"Entonces está atrasada. Recordando la exasperación de Shizune a causa de la actitud despreocupada de Rin varios días antes, no sé en qué pensar."

"Se ha dejado expuesta a un “te lo dije” a menos que pueda terminar lo que sea que deba terminar para la mañana del domingo."

"Rin se queda mirando a su mural luciendo todo lo mortificada que pueda."

show rin negative_annoyed_ni
with charachange

rin "Déjenme. Voy a tener que trabajar por un tiempo."


"Le doy un vistazo a Lilly, esperando que comparta una mirada de incredulidad conmigo mientras pongo los ojos en blanco, pero entonces me percato de que ella no es de quienes hacen ese tipo de cosas."

show rin negative_angry_ni
with charachange

rin "Déjenme."

stop music fadeout 2.0

hide rin
with charaexit

show lilly cane_concerned_ni at center
show bg school_dormext_half_ni at bgright
with charamove

"Lo hacemos, por supuesto, no queriendo agravarla más de lo que ya está."

"Siento el estómago revuelto. Seguro que Rin tiene una cierta habilidad de hacer que las demás personas se preocupen por ella."

"Parece una persona que jamás debería quedarse sola."

hi "¿Tal vez deberíamos llamar a alguien? Se escuchaba como si estuviera entrando en shock o algo parecido."

show lilly cane_oops_ni
with charachange

li "Estoy segura de que estará bien. Ella solamente es ah… eeeh… cómo decir…"

"Lilly inclina la cabeza a un lado, tratando de encontrar una forma elegante de llamar loca a Rin sin llamarle loca."

hi "¿Peculiar?"

show lilly cane_weaksmile_ni
with charachange

li "Sí, una persona muy peculiar."

hi "Creo que podrías decir eso."

show lilly cane_giggle_ni
with charachange

"Ella se ríe melodiosamente de la idea, asintiendo en acuerdo."

show lilly cane_weaksmile_ni
with charachange

li "Discúlpame por haberte dejado solo mientras hablabas con ella. Yo… en verdad no la entiendo, así que mantengo mi distancia."

"Entonces, creo que estaba en lo correcto. Lilly ofrece una leve sonrisa de disculpa como si se arrepintiera de que sus propias deficiencias le hayan prevenido acercarse a Rin."

"No soy quien para culparla. En absoluto."

"Lilly deja salir un largo suspiro, probablemente un bostezo disimulado. Imagino que se encuentra tan exhausta por todo esto como yo."


show lilly cane_cheerful_ni
with charachange

li "Será mejor que me marche y le entregue esto a Hanako. Agradezco la compañía, Hisao."

"Ella me sonríe muy dulcemente. Se siente diferente de lo normal, a pesar del hecho de que ella parece sonreír tan a menudo."

"No puedo decir cuál es la diferencia. Simplemente es diferente."

"Relajada, diría yo, pero puede ser solo alivio por deshacerse de Rin. Quizás."

hi "Seguro… Buenas noches. Saluda a Hanako de mi parte."

show lilly cane_smile_ni
with charachange

li "Lo haré. Buenas noches."

hide lilly

stop ambient fadeout 2.7

scene black
with Dissolve(3.0)

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
