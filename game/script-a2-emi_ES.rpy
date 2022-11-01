
label es_E3:

window hide None

scene black
with dissolve

$ renpy.music.set_volume(1.0,0.0, "ambient")
play sound sfx_alarmclock

"El pitido de mi alarma hace añicos el silencio de la madrugada, y me pregunto de dónde sacar la motivación para levantarme."

scene bg school_dormhisao
with openeye

"Aún falta un buen rato para las clases, pero acordé correr con Emi por las mañanas."

"La verdad, correr no me interesa mucho como pasatiempo, ni siquiera como un ejercicio que posiblemente alargue mi vida."

"Sin embargo, me siento obligado a cumplir lo que prometí ayer a Emi, y es por eso que estoy poniéndome una pantaloneta y una camiseta ligera."

scene bg school_courtyard
with locationskip

"El frío aire mañanero acaricia mi rostro mientras los rayos del sol provocan que el rocío sobre el césped destelle, casi cegándome al principio."


"Mientras voy hacia la pista, me asalta un pensamiento desagradable."

"¿Qué tal si todo esto es algún tipo de broma de Emi?"

"¿En serio me sorprendería?"

"Diablos, probablemente yo también se lo haría al chico nuevo."

"Como mínimo, estoy seguro de que Emi y Rin apostaron sobre si realmente me presentaría o no."

scene bg school_track
with locationchange

"Siento cierta inquietud mientras la pista aparece a la vista."

show emi basic_annoyed_gym at center
with charaenter

play music music_emi fadein 1.0

emi "¡Llegas tarde!"


"Parece que Emi ya está aquí. Qué alivio."

hi "No según mi reloj. Ambos llegamos temprano, de hecho."

show emi basic_closedhappy_gym
with charachange


emi "Maldición. Me atrapaste."

"Emi está sentada en las gradas, ataviada con sus ropas para correr, esperándome con cierta paciencia."

hi "Me alegra que realmente estés aquí. Temía que esto fuera una broma o algo."

show emi basic_grin_gym
with charachange

emi "Nah, nunca haría que alguien se levante temprano por nada."

show emi excited_proud_gym
with charachange

emi "Además, Rin ahora me debe 500 yenes. Ella no creía que realmente vendrías."

"¡Lo sabía!"

"Es bueno saber que Emi estaba de mi lado, por lo menos."

show emi gymbounce_once
with Dissolve(0.1)

"Emi salta fuera de las gradas y empieza a estirar."

play sound sfx_gymbounce

show emi gymbounce
with Dissolve(0.05)

"Ella es notablemente ágil, casi como una bailarina."

"Yo también me preparo para estirar, pero entonces me doy cuenta de que no recuerdo con exactitud cómo hacerlo adecuadamente."

"Han pasado años desde la última vez que tuve que estirar para algo, si no cuentas mi lamentable intento de correr la semana pasada."

"Y en realidad creo que esa vez tampoco estiré previamente."

"El espectro de mi larga estadía en el hospital se alza de nuevo."

"Aunque no puedo decir que fuera muy activo antes de la estadía en el hospital, así que tal vez solo me siento melancólico."

show emi basic_closedgrin_gym at center
with charachange

"Emi suelta una risita mientras me ve estirar."

show emi basic_grin_gym
with charachange

emi "No no no Hisao, ¡debes aguantar por más tiempo!"

hi "¡Lo intento! Duele un poquito."

show emi excited_proud_gym
with charachange

emi "¡Ja! Eso es porque no estás en forma. Debes ganar algo de flexibilidad, así."

hide emi
with charamoveoutbottom

"Para demostrarlo, Emi se agacha y coloca la cabeza entre sus piernas."

"Dios te bendiga, Emi."

hi "Ya veo. ¿Debería esforzarme por lograr ese tipo de cosas?"

show emi basic_closedgrin_gym
with charamoveinbottom

emi "¡Por supuesto! La flexibilidad es importante para cualquier atleta. Cuanto más estires, más rápido podrás correr."

"Eso no tiene ningún sentido para mí, pero Emi parece creer que es verdad."

"Con la ayuda de Emi, me las arreglo para estirar adecuadamente."

show emi basic_grin_gym
with charachange


"No puedo evitar notar que cuando ella piensa en cómo explicarme las cosas, frunce la boca por la concentración."

"Es adorable."

show emi excited_proud_gym
with charachange

emi "Nada mal, Hisao. Vamos, será mejor que empecemos a correr."

show emi excited_happy_gym
with charachange

emi "Empezaremos con solo un kilómetro y medio, ¿está bien?"

show emi basic_happy_gym
with charachange

emi "Eso es cuatro vueltas alrededor de la pista, ¿entendido?"

hi "Suena bien."

show emi basic_happy_gym:
    center
    easeout 0.5 xpos 0.4 alpha 0.0
with None

stop music fadeout 2.0

"No debería de ser demasiado difícil, ¿cierto?"

scene bg school_track_on
with locationchange

"Un difuso recuerdo de haber corrido lo mismo en clases de gimnasia emerge en mi cabeza."

"Sí, no estuvo tan mal."

play music music_running fadein 0.5

scene bg school_track_running
with Dissolve(2.0)

$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

play ambient sfx_emijogging fadein 1.0

"Emi establece un buen ritmo, y me posiciono detrás de ella."

$ renpy.music.set_volume(1.0, 0.5, channel="ambient")

show emi basic_grin_gym at left
with charamoveinleft

emi "Trata de seguirme, ¿de acuerdo, Hisao?"

hi "Copiado."

$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

hide emi
with charamoveoutleft


"Completamos la primera curva sin incidentes, aunque ya puedo sentir mi frecuencia cardiaca elevarse levemente."

"Al pasar la segunda curva, he empezado a respirar a través de la boca."

"Emi no parece tener ni una gota de sudor."

"Como para puntualizar su superioridad, se da vuelta y empieza a correr de espaldas."

$ renpy.music.set_volume(1.0, 0.5, channel="ambient")

show emi basic_closedgrin_gym at center
with charaenter

emi "¿Estás bien, Hisao?"


hi "Nunca… mejor."

show emi excited_proud_gym
with charachange

emi "¿En serio? En ese caso tal vez debería de aumentar la velocidad, ¿eh?"

hi "Oh… no, … no deberías de…"

hi "… exigirte… dema… siado."

"La pesadez de mis jadeos y exhalaciones hace que la frase suene menos convincente de lo que esperaba. Emi se limita a sonreír y se da vuelta de nuevo."

show emi excited_proud_gym at left
with charamove

emi "Tú mandas, Hisao. Mantendremos este ritmo."

$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

hide emi
with easeoutleft


"Tengo la sensación de que se burlan de mí."

"Si no estuviera en tan pésima forma, probablemente me sentiría ofendido."

"Para la tercera vuelta, mi respiración se basa en jadeos irregulares."

"También estoy cubierto por mi propio sudor. Asqueroso."

"Cerramos la curva para iniciar la cuarta vuelta, y Emi mira hacia atrás, sonriéndome."

$ renpy.music.set_volume(1.0, 0.5, channel="ambient")

show emi basic_closedgrin_gym at left
with charamoveinleft

emi "¡Aquí vamos!"

play ambient sfx_emisprinting

hide emi
with easeoutleft

$ renpy.music.set_volume(0.3, 0.5, channel="ambient")

"Ella se aleja a una velocidad deslumbrante mientras yo me apego a mi ritmo con terquedad."

"Para cuando llego a la primera curva, ella ya está terminando la segunda."

"Mientras forcejeo del otro lado de la pista, Emi continúa corriendo y me alcanza."

play ambient sfx_emijogging

$ renpy.music.set_volume(1.0, 0.5, channel="ambient")

show emi excited_proud_gym
with charamoveinright

emi "¡Vamos, Hisao! ¡Puedes hacerlo!"

$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

hide emi
with charamoveoutleft

"Le respondería, pero estoy demasiado concentrado llevándole aire a mis pulmones e ignorando el ardor en los músculos de mis piernas."

"Una parte de mí quiere decir algo como “Tal vez {b}tú{/b} puedes, pero yo estoy a punto de morir”."

"Por otra parte, dudo poder formar alguna palabra en estos momentos."

"Emi sigue mi ritmo mientras recorro la segunda curva y cruzo la línea de meta."

stop ambient fadeout 1.5

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

stop music fadeout 5.0

show bg school_track_on
show emi basic_happy_gym
with locationchange


"Ese sprint parece haberla hecho sudar."

"De hecho ha causado que su camiseta se vuelva ligeramente transparente. Al parecer lleva un sujetador deportivo negro."

"Siento una ligera punzada de culpa por ser el tipo de hombre que mira el pecho de una chica, pero mi pecho y mis piernas me arden tanto que no consigo preocuparme mucho por eso."

show emi excited_proud_gym
with charachange

emi "Nada mal para un primer intento, Hisao."

play music music_happiness fadein 0.5

hi "Mu— … muy amable… de tu parte… decir eso."

"Emi no parece estar exhausta, pero al menos respira con más pesadez que antes de que empezáramos a correr."

"Debe de ser culpa del sprint."

show emi basic_grin_gym
with charachange


emi "Oye, debo correr un poco más. Deberías caminar alrededor de la pista para relajarte."

emi "Luego podemos estirar, y habremos terminado, ¿de acuerdo?"

hi "Suena genial."

"Mis piernas están en llamas, y aún respiro con dificultad, pero asombrosamente mi corazón parece estar tomando bien la tensión."

"Otro triunfo de las ciencias médicas, supongo."

show emi basic_closedhappy_gym
with charachange

emi "Deberías de poner los brazos detrás de la cabeza. Hace que sea más fácil recuperar el aliento."

$ renpy.music.set_volume(0.3, 1.0, channel="ambient")

play ambient sfx_emipacing

hide emi
with charamoveoutleft

"Sorprendentemente, tiene razón. Empiezo a pasear por la pista, feliz de sentir cómo recupero el aliento."

$ renpy.music.set_volume(1.0, 0.5, channel="ambient")

show emi blur at offscreenright
with None

show emi blur at offscreenleft
with move

$ renpy.music.set_volume(0.3, 0.5, channel="ambient")

hide emi
with None

"Veo algo borroso cuando Emi pasa corriendo a mi lado."

"Verla correr es absolutamente fascinante."

"No es solo porque use prótesis, aunque eso es interesante."

show ev emi_run_face_zoomin
show ev emi_run_face as unlockstub behind ev
with dissolve

"Lo más interesante es la forma en la que le cambia el rostro."

"No puedo más que vislumbrarlo mientras ella corre, pero sus ojos parecen cobrar vida con una especie de alegría feroz."

"Es como si no hubiera nada más en el mundo excepto ella y la pista."

stop ambient fadeout 0.5

$ renpy.music.set_volume(1.0, 0.5, channel="ambient")

scene bg school_track_on
with locationchange

"Para el momento en que he llegado al tramo final, Emi parece haber terminado con sus sprints."


"Ahora respira con pesadez, pero tiene una sonrisa de satisfacción en el rostro. Me hace señas con alegría mientras me acerco a ella."

show emi basic_grin_gym at center
with charaenter

emi "Te sientes mejor, ¿verdad?"

hi "De hecho, sí."

show emi sad_grin_gym
with charachange


emi "¿Quieres dar otra vuelta conmigo? También tengo que enfriarme un poco, sabes."

"Una parte de mí preferiría sentarse, y no moverse, pero algo me dice que sería una mala idea."

"Además, si me siento, podría no volver a levantarme jamás."

hi "Claro, ¿por qué no?"

"Ahora Emi también tiene las manos detrás de la cabeza, lo que la hace verse bastante relajada."

"Y el posicionamiento de sus brazos levanta su camiseta lo suficiente como para que yo pueda ver una pequeña franja de su vientre."


"Me esfuerzo en actuar como un caballero y no mirar, pero el contraste de su piel contra la pantaloneta roja es bastante llamativo."

show emi basic_grin_gym
with charachange

emi "Entonces, ¿cómo te sientes, Hisao?"

hi "Sorprendentemente bien, en realidad. Estoy adolorido y cansado, pero… sorprendentemente bien."

"En cuanto lo digo, me doy cuenta de que es verdad."

"Claro, parte de mí quiere tirarse al suelo y morir, pero siento como si hubiera logrado algo."

"Es casi como un fulgor en todo mi cuerpo que persiste a pesar del dolor."

show emi excited_proud_gym
with charachange

emi "Sí, es la euforia del corredor."

hi "¿Euforia del corredor?"

show emi basic_hes_gym
with charachange

emi "Sí, tiene algo que ver con… ¿la adrenalina?"

"Emi piensa por un momento mientras caminamos, tratando de recordar."

show emi basic_closedgrin_gym
with charachange

"Luego se encoge de hombros y me sonríe."

show emi basic_grin_gym
with charachange

emi "En realidad no lo recuerdo. Aunque es una sensación agradable, ¿verdad?"

show emi basic_happy_gym
with charachange

stop music fadeout 0.5
play sound sfx_heartstop

emi "Mejor que el sexo, ¿cierto?"

"Abro la boca para responder justo antes de procesar lo que acaba de decir."

hi "…"

"Emi observa mi cara unos instantes antes de soltar una carcajada."

play music music_comedy fadein 1.0

show emi excited_laugh_gym
with charachange

emi "¡Perdón, perdón! ¡No pude resistirlo! ¡Es que eres demasiado fácil!"


hi "¿Por qué acepté correr contigo de nuevo?"

"Emi solo se ríe con más ganas. Ella agarra mi antebrazo y lo inclina, permitiéndole ver mejor mi reloj. Su rostro cambia en el momento que ve la hora."

show emi basic_shock_gym
with charachange

emi "¡Oh no! ¡Será mejor que nos apresuremos, Hisao!"

show emi basic_closedsweat_gym
with charachange

emi "¡Las clases comienzan en una hora, y necesito ducharme!"

hi "Tal vez yo también debería de hacerlo…"

show emi basic_hes_gym
with charachange

emi "También tengo que ver al enfermero… ¡Tal vez me escriba una nota por llegar tarde!"

hi "¿Por qué necesitas ver al enfermero?"

show emi basic_closedgrin_gym
with charachange

"Emi señala sus prótesis, como si eso lo explicara todo."

show emi basic_grin_gym
with charachange

emi "Es importante revisar por irritación."

emi "Ya sabes, por el sudor o la fricción, o lo que sea."

show emi excited_amused_gym
with charachange

emi "Normalmente solo voy luego de la práctica, pero si vamos a estar haciendo estas carreras por las mañanas supongo que lo veré dos veces al día."

"Espera, ¿así que Emi empezó con estas carreras cuando yo aparecí?"

hi "Si es más conveniente para ti correr conmigo más tarde…"

show emi sad_grin_gym
with charachange

emi "¡No seas tonto! He querido empezar a correr por las mañanas desde hace un tiempo."

emi "Pero si no tenía un compañero con quién hacerlo, sería más difícil mantener una rutina."

show emi basic_grin_gym
with charachange

emi "Siempre es más difícil abandonar un compromiso si estás decepcionando a alguien más, ¿sabes?"

show emi basic_closedgrin_gym
with charachange

emi "¡Así que tú serás mi compañero durante las mañanas!"

show emi excited_proud_gym
with charachange

emi "Ambos necesitamos el ejercicio, así que todo encaja, ¿no crees?"

hi "Sí, perfecto."

"Aunque, ¿tenía que ser yo?"

"Bueno, supongo que no puedo quejarme mucho. Es bastante divertido estar con Emi."

"Y tiene razón. Sí necesito el ejercicio. Órdenes del doctor, incluso."

show emi basic_happy_gym
with charachange

"Emi se despide rápidamente."

emi "¡Bien, me voy! Ven a almorzar con nosotras, ¿de acuerdo?"

hi "¿Qué?"

show emi basic_closedhappy_gym
with charachange

emi "¡Almuerzo! Ya sabes, ¿la comida? ¿A la mitad del día? ¡Ven con nosotras!"

hi "¿Dónde?"

show emi basic_grin_gym
with charachange

emi "En la azotea. A Rin le gusta allá arriba."

hi "¿Cuándo?"

show emi basic_annoyed_gym
with charachange

emi "A la hora del almuerzo, ¿cuándo más? Esa fue una pregunta tonta."


hi "Sí, pero en cierto modo sentí que necesitaba preguntar las tres cosas para no dejar cabos sueltos."

show emi excited_laugh_gym
with charachange

"Emi suelta una carcajada, y luego sonríe. No creo haber visto a una chica sonreír tanto antes."

show emi excited_happy_gym
with charachange

emi "Nada mal, Hisao. ¡Hasta pronto!"

play ambient sfx_emisprinting

hide emi
with easeoutleft

stop ambient fadeout 2.0
stop music fadeout 8.0

"Y con eso, sale corriendo como una bala hacia el edificio de la escuela."

"Supongo que primero visitará al enfermero."

scene bg school_dormbathroom
with locationskip

"Me apresuro en volver a mi habitación y me meto en la ducha, solo para encontrarme con que el agua necesita un momento para calentarse."

play ambient sfx_shower
with vpunch

"La sorpresa del agua helada casi me mata."

show steam
with Dissolve(2.0)

"Me las arreglo para calentar un poco el agua y paso un buen rato sintiendo mis músculos relajarse."

"Mi corazón, asombrosamente, es el menos afectado por la carrera."

"Supongo que eso es algo bueno, aun si hace que me sienta un poco cobarde."

"Quiero decir, por lo menos tendría una excusa además de “no estoy en forma” si mi corazón estuviera molestándome."

"Supongo que tendré que seguir con este asunto de las carreras, si no estoy seguro de que Emi no me lo perdonaría."

"No es hasta que salgo y me seco que me doy cuenta de que solo me quedan diez minutos para ponerme la ropa e ir a clases."

"Mierda."


label es_E4:

scene bg school_dormbathroom
show steam
with None

stop ambient fadeout 1.0

scene bg school_scienceroom
with shorttimeskip

window show

play sound sfx_normalbell

"Las manecillas del reloj me liberan por fin del tedio de otra clase más repleta de diversión."

"Levantarme de mi asiento resulta ser un mayor problema del que tenía anticipado."

"Mis piernas me están matando por la carrera de la mañana."


"Tal vez hacer las carreras con Emi no es una idea tan alentadora después de todo."


"Sin embargo, la carrera me ha dado un apetito infernal."

play ambient sfx_crowd_indoors fadein 1.0

scene bg school_hallway3
show crowd
with locationchange

"Estoy a medio camino hacia la cafetería cuando recuerdo que llevo mi almuerzo conmigo."

"Mis padres consideraron adecuado proveerme de algunas cosas preenvasadas cuando me mudé, y fue algo bueno."

"El corredor está lleno de estudiantes que se dirigen a la cafetería."

"Caminar de regreso es como nadar contracorriente, pero tengo una cita que cumplir en la azotea."

stop ambient fadeout 4.0

scene bg school_staircase1
with locationchange

"Me toma un rato encontrar las escaleras que llevan a la azotea, aunque me atrevería a apostar a que Emi y Rin todavía no están allá arriba."

"De hecho, creo que vi a Emi en el corredor, entre las personas que iban hacia la cafetería."

play sound sfx_door_creak
$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 0.5

scene bg school_roof at bgright
with locationchange

"Salgo por la puerta que da a la azotea y respiro profundamente."

"El aire fresco soplando contra mi rostro casi hace que mis piernas duelan menos."

show rin basic_awayabsent at center
with charaenter

rin "Tal vez si me pongo de cabeza…"

$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_rin fadein 1.0

"Una parte de mí quiere sorprenderse de que Rin ya esté aquí."

hi "¿Qué lograrás con eso?"

show rin basic_deadpan
with charachange


rin "Cosas en las nubes."

hi "¿No puedes tan solo… verlas normalmente?"

show rin basic_deadpanupset
with charachange

"Rin pone los ojos en blanco en algo que se acerca a la exasperación."

rin "Entonces no tendría una nueva perspectiva."

hi "¿Y estar de cabeza realmente te da una nueva perspectiva?"

show rin basic_delight
with charachange

"¡Ajá! Eso la tomó por sorpresa. Rin se ve pensativa."

rin "Quizá tengas razón. Tal vez de lado."

hide rin
with charamoveoutbottom

"Mientras Rin se acuesta en la banca para mirar hacia el cielo, me rindo."

play sound sfx_impact2
with vpunch

show emi basic_closedgrin at center
with charaenter

"Afortunadamente Emi elige ese momento para irrumpir por la puerta llevando dos bolsas."

"Casi arranca la puerta de las bisagras."

show emi basic_hes
with charachange

emi "¡Lamento haber tardado tanto! Había un montón de gente en la fila."

show emi basic_grin
with charachange

show emi basic_grin at twoleft
show bg school_roof at center
with charamove

"Ella deja la primera bolsa frente a Rin y toma asiento en la banca junto a ella."

hi "¿Le compras el almuerzo a Rin?"

show emi basic_closedgrin
with charachange

emi "Algunas veces, sí. Haría que Rin me devolviera el favor comprándome el mío, pero no estoy segura de cómo lo cargaría."

show rin basic_deadpan at tworight
with charamoveinbottom

rin "Además nunca le compraría el almuerzo."


"Si Rin se ofendió por el comentario de Emi, no lo demuestra. Emi resuella."

show emi basic_annoyed
with charachange

emi "Qué malagradecida."


"No estoy seguro si bromean la una con la otra o si presencio el inicio de una pelea de chicas."

show emi basic_closedgrin
show rin basic_amused
with charachange


"Se miran la una a la otra por unos tensos segundos antes de comenzar a sonreír."

show rin basic_awayabsent
with charachange

rin "Oye, Emi, ¿crees que estar de cabeza da una nueva perspectiva sobre las cosas?"

"¿Acaso no tuvimos ya esta conversación?"

show emi basic_hes
with charachange

"Emi se ve pensativa, al parecer dedicándole a la pregunta algo de reflexión."

"Luego de una larga y profunda pausa, habla."

show emi basic_closedsweat
with charachange

emi "No tengo idea."

"Bueno, al menos está tan perdida como yo."

stop music fadeout 4.0

show emi excited_happy
with charachange

emi "Oye, Hisao, vendrás a la competencia de atletismo, ¿cierto?"

"La pregunta sale de la nada y me toma desprevenido."

hi "Eh… ¿Aún no lo sé?"

show rin basic_absent
show emi sad_annoyed
with charachange

emi "Honestamente, Hisao, después de todos los problemas por los que pasé para dejarte correr conmigo por las mañanas, ¿ni siquiera irás a mi competencia de atletismo?"

show rin basic_awayabsent
with charachange


"¿Acaso no fue ella quien me pidió que la acompañara en las carreras?"

"De hecho, ni siquiera me dio a escoger."

hi "Espera, no, no dije eso…"

play music music_ease fadein 3.0

show emi basic_closedgrin
show rin basic_absent
with charachange

"Ella se ve radiante, como si yo hubiera aceptado darle un millón de dólares."

show emi basic_closedhappy
with charachange

emi "¡Así que vendrás, después de todo! ¡Eso es genial!"

"¡Tampoco dije eso!"

show rin basic_deadpan
with charachange

rin "Yo también iré, así que me aseguraré de que venga, Emi."

show emi basic_grin
show rin basic_absent
with charachange

emi "¡Buena idea, Rin! ¿Tal vez podemos ir a comer o algo luego de que la competencia termine?"

"Siento que acabo de ser timado, pero no por estas dos."

"Más como por una fuerza externa, empujándome irrevocablemente hacia mi destino."

"… O tal vez no debería de leer libros que muestren tantas teorías conspiratorias. O podría terminar sonando como Kenji."

"Sin embargo, creo que ahora tendré que ir."

"No creo que pueda soportar verlas decepcionadas."


"Nunca me lo perdonarían."

hi "¿Y cuándo es?"

show emi basic_annoyed
with charachange

emi "¡La siguiente semana, tonto! Te lo dije hace unos días."

hi "No, no lo hiciste."

show emi sad_shy
with charachange

emi "¿Lo olvidé? Bueno, aun así no olvidarás venir, ¿verdad?"

hi "¡Por supuesto que no! ¡Incluso pondré una nota en el calendario o algo!"

show rin basic_lucid
with charachange

"Rin asiente solemnemente."

show rin basic_deadpancontemplation
with charachange

rin "Probablemente sea una buena idea, sabes. A menos de que el tiempo cambie su curso."

show emi basic_confused
with charachange

emi "¿Puede hacerlo?"

show rin relaxed_nonchalant
with charachange

"Rin se encoge de hombros con reticencia."

show rin negative_spaciness
with charachange

rin "Aún no lo ha hecho, pero nunca sabes…"

show emi basic_closedgrin
with charachange

"Esta vez es Emi la que se encoge de hombros."

show emi basic_closedhappy
with charachange

emi "Supongo que no se puede hacer nada si eso pasa."

show rin basic_deadpannormal
with charachange

rin "A menos de que seas un viajero del tiempo o algo así."

hi "Realmente no creen que eso pueda pasar, ¿verdad?"

show emi basic_confused
with charachange

emi "No me parece que lo creamos… ¿o sí?"

show rin relaxed_nonchalant
with charachange

"Rin se encoge de hombros de nuevo. Esa parece ser su respuesta predeterminada a todo."

show rin basic_deadpandelight
with charachange

rin "Supongo que no. Pero me reservo el derecho a cambiar de opinión en cualquier momento."

"Proviniendo de Rin, esta declaración tiene una inquietante cantidad de sentido."

"El hecho de que ahora lo note me asusta un poco."

"Me pregunto si Emi se siente así todo el tiempo."

show emi basic_closedgrin
with charachange

"Aunque si lo hace no lo demuestra. Emi simplemente asiente."

show emi basic_grin
with charachange

emi "Como esperaba."

show rin basic_deadpanupset
with charachange

rin "¿Qué se supone que significa eso?"

show emi sad_grin
with charachange

"Esta vez, es Emi quien se encoge de hombros."

"Es como si usara las propias armas de Rin en su contra."

show emi excited_proud
with charachange

emi "Tu respuesta es la clase de cosas que esperaría de ti, es todo."

show rin negative_worried
with charachange

rin "¿En serio soy tan predecible?"

show emi basic_closedgrin
with charachange

"La sonrisa de Emi parece rayar en el regodeo."

emi "Nah, es solo que tu impredecibilidad es bastante predecible."

show rin relaxed_nonchalant
with charachange

rin "Bueno, entonces está bien."

play sound sfx_warningbell

"No tengo oportunidad de ver si Rin lo decía en serio o no, ya que suena la campana."

"No noté para nada cómo transcurría el tiempo del almuerzo."

"Pasar el rato con estas dos fue demasiado interesante."

show emi basic_shock
with vpunch

"Emi pega un brinco, con una mirada de pánico en su rostro."

emi "¡Oh, no! ¡Necesitaba pasar por mi habitación para recoger mi cuaderno para la siguiente clase!"

show rin basic_deadpandelight
with charachange

rin "¿No desearías tener una máquina del tiempo ahora?"

"Rin se ve algo presumida mientras dice esta oración; como si acabara de ganar una discusión."

"Emi ignora el comentario de Rin."

show emi basic_hes
with charachange


emi "Perdona, Hisao, ¿pero podrías asegurarte de botar nuestra basura?"

show emi basic_closedsweat
with charachange

emi "Usualmente limpio yo misma, ¡pero tengo que correr!"

hi "Claro, no hay problema."

hide emi
with easeoutleft

"Emi sale disparada con una urgencia que estoy empezando a esperar de ella."

hide rin
with charaexit

"No me molesto en preguntarle a Rin por qué no puede ayudar. Ya parece estar absorta en algo más mientras se aleja."

"Probablemente esté acostumbrada a que Emi se encargue de limpiar, y por alguna razón dudo que Emi le haya reclamado por eso alguna vez."

"Limpiar lo del almuerzo no toma mucho rato, así que tengo tiempo de sobra para tirar la basura e ir a clase."

stop ambient fadeout 1.0

scene bg school_scienceroom
with locationskip

"Misha me recibe con un saludo y una sonrisa maliciosa mientras entro por la puerta."

show misha cross_grin at center
with charaenter

mi "No te vi en la cafetería, Hicchan."

hi "Sí, decidí que ahí estaba demasiado concurrido."

show misha hips_grin
with charachange

"La sonrisa de Misha se ensancha aún más."

mi "¿En serio? ¿Seguro de que no estabas participando en alguna reunión ilícita?"

hi "¿Q… qué? ¿De qué estás hablando?"

show misha sign_smile
with charachange

mi "Estabas en la azotea, ¿cierto? ¡Con Rin y Emi, nada menos! ¡Tú, casanova!"

hi "So… solo almorzamos, ¡es todo!"

show misha cross_laugh
with charachange

"Misha suelta una carcajada, llamando la atención de varios de mis compañeros."

mi "¡Guajajaja! ¡Eres tan adorable cuando te sonrojas así, Hicchan!"

show misha cross_grin
with charachange

"Ella me lanza un guiño conspiratorio."

show misha cross_smile
with charachange

mi "No te preocupes, tu secreto está a salvo conmigo."

hi "¡No hay ningún secreto!"

show misha perky_confused
with charachange

mi "¿Eh?"

"Misha se ve decepcionada y luego se anima de nuevo."

show misha hips_grin
with charachange

mi "¡El tiempo lo dirá~!"

"No sé de qué diablos está hablando, pero afortunadamente nuestro profesor entra, y la clase comienza."

stop music fadeout 2.0




label es_E5:

scene bg school_scienceroom
with shorttimeskip

play sound sfx_normalbell

"Otro día de clases finalmente se ha arrastrado hasta su final."

"Inesperadamente, me las arreglo para mantenerme despierto todo el día."

"Estoy muy seguro de que eso cuenta como un milagro."

"Por unos instantes, mis piernas no parecen querer ponerse en pie."


"Supongo que la carrera me agotó bastante."

scene bg school_hallway3
with locationchange

"Me dirijo al pasillo y me encamino a mi habitación."

scene bg school_dormhisao
with locationskip


"Tomo asiento y por un rato me dedico sin entusiasmo a mi tarea, sintiéndome como un buitre que picotea un cadáver particularmente desagradable."

"Él sabe que esa es su comida, pero no está seguro si debería de ordenar comida a domicilio en su lugar."

"No creo que pueda soportar esto, pero es importante terminar mis deberes."

hi "Ahora, vamos a ver… ¿qué se supone que debería estar revisando?"

"Sé que es una batalla perdida, pero aun así lucho."

"A mitad de la tarea de matemáticas, suelto mi lápiz."

"Esto no está funcionando. Necesito una distracción."

"Desafortunadamente, mis opciones para distraerme son algo escasas."

"En estos momentos no estoy de humor para leer."


"Kenji está, para variar, fuera de su habitación en estos momentos."

"Si voy al aula del consejo estudiantil, solo terminaré haciendo trabajo para esas dos."

"Y solo Dios sabe dónde están todos los demás, excepto por…"

"Bueno, supongo que esa es una opción."

"Agarro mis zapatos y me encamino hacia la pista. Emi probablemente está allá abajo."

play music music_tranquil fadein 3.0

scene bg school_track_ss
with locationskip

"La práctica de atletismo apenas está terminando cuando llego a la pista."


"El sol está empezando a fundirse con el horizonte."

"¿En serio ya se hizo tan tarde?"

show emi basic_grin_gym_ss at center
with charaenter

emi "¿Qué estás haciendo aquí abajo, Hisao?"

show emi excited_proud_gym_ss
with charachange

emi "Viniste a espiarme, ¿no?"

"Me encojo de hombros. Para ser honesto, no estoy seguro de por qué vine aquí."

hi "No tenía nada mejor que hacer."

"Me parece que eso es cierto."

"En este momento, Emi es la única persona que se me ocurre que podría visitar."

show emi basic_annoyed_gym_ss
with charachange

emi "Así que soy tu último recurso, ¿verdad?"

show emi sad_angry_gym_ss
with charachange

emi "Nadie interesante alrededor, así que simplemente iré a ver a Emi, ¿es eso lo que pensaste?"

"Realmente se ve enojada."

"Se me presenta una oportunidad para molestarla."

hi "De hecho, sí, supongo que lo eres."

show emi sad_annoyed_gym_ss
with charachange

"Emi hace un puchero, abriendo más los ojos para dar la máxima impresión de semejanza a un cachorrito."

hi "¡Bromeaba! ¡Solo bromeaba!"

show emi basic_closedgrin_gym_ss
with charachange

emi "¡Así que estás aquí para acosarme!"

"Espera, ¿qué?"

hi "¡No me refería a eso!"

hi "Además, ¿por qué te acosaría? No es como si hiciera falta acosarte."

hi "Si no estás dormida o en clase, estás acá abajo, ¿cierto?"

"Emi se ríe con este comentario."

show emi basic_happy_gym_ss
with charachange

emi "Bueno, no estás completamente equivocado, supongo, pero olvidaste de comer. También como, sabes."

"Asiento, concediéndole la razón."

show emi sad_grin_gym_ss
with charachange


emi "Además, algunas veces ando con Rin… así que realmente podría hacer falta algo de esfuerzo para acosarme."

hi "¿Qué hacen ustedes dos juntas de todas formas? No parecen tener mucho en común."

show emi basic_closedgrin_gym_ss
with charachange

"Ella coloca sus manos en sus caderas y adopta un aire de superioridad."

show emi basic_grin_gym_ss
with charachange

emi "Eso es lo que tú crees. Tengo todo tipo de pasatiempos ocultos, sabes."

hi "Oh, ¿en serio? ¿Como cuáles?"

show emi sad_grin_gym_ss
with charachange

"Emi pone su cabeza de lado, como si intentara recordar qué es lo que hace en su tiempo libre."

show emi basic_closedgrin_gym_ss
with charachange

emi "Bueno, Rin y yo salimos de compras de vez en cuando."

"Supongo que tiene sentido. Emi es una chica, después de todo. Pero, ¿Rin?"

hi "¿Rin va contigo?"

show emi basic_grin_gym_ss
with charachange

emi "Usualmente nos damos una vuelta por la tienda de artículos de arte."

emi "Además le gusta esa tienda de música que vende todo tipo de cosas que suenan raro."

show emi basic_closedhappy_gym_ss
with charachange

emi "Dice que le ayudan a concentrarse."

"Eso tiene un poco más de sentido."

hi "Ya veo. ¿Algún otro pasatiempo oculto?"

show emi excited_proud_gym_ss
with charachange

"Emi menea un dedo frente a mí."

emi "Vamos vamos, ¿por qué habría de revelarte todos mis oscuros secretos? ¡Apenas nos conocemos!"

"Por algún motivo creo que eso fue todo lo que Emi considera como pasatiempo."

"Aun así, no me parece que mi pregunta haya sido resuelta."

hi "Aunque tengas algunos pasatiempos, sigo sin ver por qué andas tanto con Rin."

hi "Digo, es algo extraña, ¿no es cierto?"

"Este comentario provoca que Emi se ría con ganas."

show emi basic_closedhappy_gym_ss
with charachange


emi "¡Ja! ¡Eso es quedarse corto!"

hi "Entonces, ¿por qué? Quiero decir, eres mucho mejor conversando y esas cosas, así que pensé que andarías con muchas personas, pero creo que solo te he visto con Rin."

show emi sad_annoyed_gym_ss
with charachange

"Emi se ve inusualmente defensiva."

emi "Oye, ¡ando con muchas personas que no son Rin! Solo no me ves haciéndolo porque no estoy en tus clases."

hi "Bien, pero eso aún no explica por qué andas con Rin."

"Ni siquiera estoy seguro de por qué quiero saber esto."

"Supongo que es porque el almuerzo fue muy extraño."

show emi basic_confused_gym_ss
with charachange

"Emi se encoge de hombros, viéndose muy parecida a Rin por un momento."

stop music fadeout 4.0

emi "Es porque tenemos perspectivas similares."

"Si me fueras a preguntar por la respuesta más improbable, sería esa."

hi "¿Qué quieres decir?"

emi "Es como…"

play music music_emi fadein 1.0

show emi basic_grin_gym_ss
with charachange

emi "Mira, Rin pinta y todo eso, ¿cierto?"

hi "Sí…"

"No estoy seguro de adónde va esto."

show emi basic_closedgrin_gym_ss
with charachange

emi "Bueno, yo corro."

hi "¿Y?"

show emi basic_happy_gym_ss
with charachange

emi "Y… es por eso que somos similares."

hi "…"

hi "No te sigo."

show emi basic_annoyed_gym_ss
with charachange

"Emi frunce el ceño, como si intentara descifrar su respuesta."

emi "Bueno, tal vez es que hacemos las cosas por las mismas razones."

hi "¿Eh?"

show emi sad_grin_gym_ss
with charachange

emi "Ya sabes, seguimos nuestras pasiones."

hi "Entonces a ti te apasiona correr y a Rin le apasiona el arte, ¿es eso?"

emi "Bueno, algo así. Déjame pensar…"

show emi basic_closedgrin_gym_ss
with charachange

emi "Bueno, Rin me lo explicó una vez, pero no sé cuánto de eso entendí."

"No me sorprende. Creo que una explicación de Rin probablemente confundiría a cualquiera."

show emi basic_grin_gym_ss
with charachange

emi "Ella dice que ambas perseguimos un extremo."

emi "Algo como, ella siempre intenta encontrar nuevas maneras de mostrar un sentimiento particular o algo."

show emi sad_grin_gym_ss
with charachange

emi "Y yo corro por la sensación que tengo al hacerlo."

emi "Y ya que no permitimos que nada nos ralentice, hemos creado una conexión basada en eso."

hi "¿A qué te refieres con “que nada nos ralentice”?"

show emi basic_confused_gym_ss
with charachange

"Emi se ve sorprendida y señala sus piernas."

emi "Ya sabes, porque soy atleta. Y Rin es pintora aunque no tenga brazos."

emi "Así que respetamos la determinación de cada una."

show emi basic_closedhappy_gym_ss
with charachange

emi "Y es por eso que andamos juntas."

show emi sad_grin_gym_ss
with charachange

emi "Creo."

"Bueno, no estoy seguro de que eso haya tenido algún sentido para mí… pero dada la expresión indecisa de Emi, ella tampoco está muy segura."

emi "Honestamente, no es algo en lo que piense demasiado."

emi "Simplemente nos llevamos bien, creo que eso es lo que de verdad importa."

"Supongo que en eso tiene razón."

"Me asalta otra duda, y ya que no tengo nada mejor que hacer, la pregunto."

hi "Y, ¿qué hizo que te gustara tanto el atletismo?"

show emi basic_closedgrin_gym_ss
with charachange

emi "Oh, ¡he estado corriendo desde que era muy pequeña!"

show emi basic_grin_gym_ss
with charachange

emi "Mi padre era atleta, y en cuanto pude caminar, empezó a enseñarme a correr."

show emi sad_grin_gym_ss
with charachange

emi "Era nuestro vínculo padre/hija, ¿sabes?"

show emi sad_depressed_gym_ss
with charachange

stop music fadeout 10.0

emi "Nuestro pasatiempo en común."

"Una sombra cruza su rostro, y estoy sorprendido de que se vea… triste."

"¿Pasó algo entre ellos?"

show emi basic_shock_gym_ss
with charachange


emi "Vaya, no me queda mucho tiempo."

show emi basic_closedsweat_gym_ss
with charachange

emi "¡Perdón, pero tengo que hacer unas cuantas vueltas más antes de visitar al enfermero!"

play ambient sfx_emipacing

hide emi
with easeoutleft

$ renpy.music.set_volume(0.3, 1.0, channel="ambient")

"Ella corre por la pista, su cabello ondulando en el aire."

"Me parece que va mucho más rápido de lo que lo hacía esta mañana."

"Mientras recorre la pista, logro echar un vistazo a su rostro."

scene ev emi_run_face_zoomout_ss
with locationchange


"Es prácticamente el mismo de esta mañana, pero sus ojos parecen haber adoptado una delineación más intensa."

"Supongo que tiene razón."

"Realmente no sé mucho de ella."

scene bg school_track_ss
with locationchange

"La observo correr por un rato, y luego me levanto para regresar a mi habitación."

emi "¡Oye!"


"Ella ve cómo me alejo y mueve los brazos para llamar mi atención."

emi "¡No lo olvides! Mañana por la mañana a la misma hora, ¿entendido?"

hi "Entendido."

stop ambient fadeout 2.0

"Me dirijo de vuelta a mi habitación."

"La tarea aguarda."


label es_E6:

scene bg school_track_ss
with None

scene bg school_dormhisao_ni
with shorttimeskip

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

"No puedo dormir."

"Mi cuerpo está agotado, pero mi mente se mantiene despierta, mirando hacia el techo en la profunda oscuridad de mi habitación."


"Me parto la cabeza buscando un hilo de pensamientos, con la esperanza de poder extenuar a mi cerebro."

"Todo en lo que puedo pensar es en cómo no puedo pensar en nada."

"Esto no es nada productivo."

"Me pregunto si esto es un efecto secundario de mi medicina, aunque sería extraño que se haya tomado tanto tiempo en aparecer."

"Por otra parte, puede que sencillamente no esté tan acostumbrado a mi nuevo entorno como me gustaría creer."

"No lo sé, pero sea cual sea la razón, estoy despierto y no debería."

"Esto es ridículo."

play sound sfx_switch

scene bg school_dormhisao
with Dissolve(0.2)

"Ignorando la rigidez de mi cuerpo, salgo de la cama y miro mi reloj."

"Cuatro de la mañana. La última vez que me fijé era apenas la una, así que tal vez dormí un poco."


"No sé."

"Me arropo y salgo de mi habitación."

"Una caminata podría hacerme bien."

scene bg school_courtyard_ni
with locationskip

"Estoy sorprendido de lo frío que está el aire comparado con la relativa calidez del día."

"Casi puedo ver mi respiración mientras deambulo por el campus, esperando a que salga el sol o a que me quede dormido."

"A estas alturas, cualquiera de las dos me sirve."

scene bg school_track_ni at left
with locationchange

"Termino en la pista, donde por primera vez, Emi no está corriendo."

"Supongo que tiene sentido; es demasiado temprano, incluso para ella."

"Las bancas de las gradas están heladas, pero a estas alturas agradezco la sensación."

show bg school_track as overlay:
    left
    alpha 0.0
    linear 15.0 alpha 0.5
with None

"El sol está empezando a mostrar su cara en el horizonte, y sé con una terrible certeza que no dormiré más por hoy."

"Los rayos del sol, cada vez más fuertes, comienzan a calentarme, y observo el rocío en el suelo empezar a evaporarse levemente."

"Mi mente se calma, un poco."

stop music fadeout 2.0

scene black
with shuteye

window hide

with Pause(3.0)

play sound sfx_rustling

window show hpunch

"Alguien está sacudiéndome."

emi "Oye, ¡despierta!"

hi "¿Eh? ¿Dónde? ¿Qué?"

scene bg school_track
show emi basic_shock_gym_close at center
with openeyefast


"Supongo que me quedé dormido, después de todo."

show emi basic_annoyed_gym_close
with charachange

emi "¿Qué estás haciendo aquí afuera? ¡Vas a pescar un resfriado o algo!"

play music music_dreamy fadein 4.0

"Me froto los ojos y me encuentro con Emi, que se inclina sobre mí con una expresión de preocupación."

"Aún estoy algo adormecido, por lo que mi respuesta es un murmullo."

hi "No podía dormir. Vi salir el sol."

show emi basic_confused_gym_close
with charachange

emi "Suena como algo que diría Rin."

"Me encojo de hombros, sintiendo la rigidez que provoca dormir en una banca por unas cuantas horas."

hi "¿Tú crees? No lo sé."

show emi basic_grin_gym_close
with charachange

"Emi sonríe con mi (levemente irritada) respuesta."

show emi basic_closedgrin_gym_close
with charachange

emi "Así que no podías dormir, ¿eh? ¡Es obvio que tendremos que ponerte a correr aún más hoy!"

"Aunque solo la he conocido por cerca de una semana, esta parece una respuesta muy típica de Emi al problema."

hi "Oye, ¡mi cuerpo estaba exhausto después de lo de ayer!"


hi "Mi mente no se detenía, es todo."

show emi basic_confused_gym_close
with charachange

emi "No veo la diferencia. Si te esfuerzas al correr, tu cerebro también se agotará."

"Estoy dudando seriamente de la prudencia de hacer esto a primera hora de la mañana."


"No sé si mis notas podrán soportar que extenúe a mi cerebro de esa manera."

show emi basic_closedgrin_gym_close
with charachange

with vpunch

show emi basic_closedgrin_gym
with charadistant

"Emi me arrastra fuera de las gradas con una fuerza sorprendente para alguien de su tamaño."

emi "¡Ahora arriba, Hisao! ¡Tenemos trabajo que hacer!"

"No estoy muy seguro de querer hacer esto hoy, para ser honesto."

"Quiero decir, obviamente no dormí mucho… ¡y lo poco que dormí fue en las gradas!"

hi "No sé… ¿realmente debería de ponerme a correr?"

show emi basic_annoyed_gym
with charachange

"Emi fija su mirada en mí."

"Por todos los cielos."

show emi sad_annoyed_gym
with charachange

emi "¿De qué estás hablando? ¡Claro que deberías ponerte a correr!"


emi "¿De qué otra forma piensas hacer algo contra esa tensión?"

show emi basic_annoyed_gym
with charachange

emi "¡Has estado durmiendo en las gradas, por el amor de Dios!"

emi "La mejor manera de deshacerte de ese malestar es corriendo un poco."

emi "¡Ahora deja de esconderte en las gradas y ven aquí!"

"No puedo discutir contra eso. Estoy seguro de que me mataría si no hago lo que me dice."

"Me pongo de pie y bajo a la pista."

scene bg school_track_on
with locationchange

"El sol está calentando agradablemente las cosas, creo."


"Empezamos a estirar, y de nuevo me encuentro en dificultades para no mirar."

"Si es así como tengo que despertar todos los días, podría ser capaz de acostumbrarme."

show emi basic_annoyed_gym
with charachange

emi "Sabes, Hisao, no es educado mirar."

hi "¡No estaba mirando! ¡Lo juro!"

"Emi levanta una ceja y me sopesa por un instante, como si evaluara mi respuesta."

"Hay un breve instante en el que temo por mi vida."

show emi basic_closedhappy_gym
with charachange

"Pero al final deja entrever una sonrisa y se ríe, sacudiendo la cabeza lentamente."

show emi basic_grin_gym
with charachange

emi "La verdad, no tenías que negarlo con tanto vigor."

stop music fadeout 5.0

"En respuesta, doy unas palmadas y busco un cambio de tema."

hi "¡Muy bien! Suficiente estiramiento, ¿verdad?"

show emi sad_grin_gym
with charachange

"Emi se encoge de hombros despreocupadamente."

emi "¿Te sientes relajado? Así es como realmente te das cuenta."

"Bueno, me siento listo para correr, si es a lo que se refiere."

hi "Sí, me siento listo para empezar."

show emi basic_grin_gym
with charachange

emi "Igual que ayer, ¿de acuerdo?"

emi "Solo correremos un kilómetro y medio a un ritmo firme."

show emi basic_closedhappy_gym
with charachange

emi "No te preocupes por ir demasiado rápido, solo concéntrate en mantener el ritmo, ¿entendido?"

hi "Tú mandas."

play music music_running fadein 0.5

show emi basic_grin_gym
with charachange

play ambient sfx_emijogging

hide emi
with charamoveoutleft

$ renpy.music.set_volume(0.5, 2.0, channel="ambient")

"Emi sonríe de nuevo y empezamos a correr por la pista."

scene bg school_track_running
with Dissolve(2.0)

"…"

"…"

"Creo que voy a morir."

"Ni siquiera hemos terminado la primera vuelta, y mis piernas están en llamas."

"Mi respiración se compone de jadeos irregulares."

"Puedo sentir gotas de sudor bajando por mis cejas, y apenas completamos la segunda curva."

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

show emi basic_closedgrin_gym at left
with charamoveinleft

emi "¡Vamos, Hisao! ¡Te faltan tres vueltas más para terminar!"

$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

hide emi
with easeoutleft

"No puedo hacerlo…"

"No puedo hacerlo."

"¡No puedo hacerlo!"


"Creo que no voy a vomitar."

"De alguna forma estamos en la segunda vuelta. Emi ni siquiera está sudando."

"¿Cómo puede hacer esto tan despreocupadamente?"

"Por alguna razón me sigo moviendo."

"Ella es como una máquina."

"Tercera vuelta. ¿Qué pasó con la segunda?"

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

show emi excited_proud_gym at left
with charamoveinleft

emi "¡Ya casi, Hisao!"

$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

hide emi
with easeoutleft

"¡Mentirosa! ¡Aún faltan dos!"

"Nada que hacer."

hi "N… no… puedo… ha… cerlo."

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

show emi basic_annoyed_gym
with charamoveinleft

"Emi se da vuelta y empieza a correr hacia atrás."

"Su rostro es una máscara de enojo que me sorprende."

show emi sad_angry_gym
with charachange

emi "¡Nunca digas eso!"

emi "Si dices eso, ya has perdido."

show emi sad_angry_gym at left
with charamove

emi "¡Sigue moviéndote! ¡Si estás vivo, puedes seguir moviéndote, maldita sea!"

$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

hide emi
with easeoutleft

"Vaya, palabrotas. Ahora estamos en la cuarta vuelta."

"Parece que ella realmente quiere que yo continúe."

"Piernas muévanse. Muévanse. Muévanse. Se sienten tan flojas."

"Estoy en fango, o en melaza, o en alquitrán."

"No puedo seguir."

"Seguiré."

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

show emi basic_grin_gym at left
with charamoveinleft

emi "¡El tramo final, Hisao! ¡Dale lo mejor que tengas!"

$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

hide emi
with easeoutleft

"Muevo las piernas lo más rápido que puedo."

"Ellas siguen negándose a obedecer mis órdenes."

"De algún modo, sigo moviéndome."

"De algún modo, termino."

stop ambient fadeout 0.5

show emi excited_happy_gym at center
with charaenter

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

emi "¡Eso es, Hisao! ¡Sabía que lo lograrías!"

"El enojo que Emi demostró una vuelta atrás se ha ido, reemplazado con orgullo."

"Ella está verdaderamente radiante, como si acabara de ganar la medalla de oro o algo."

scene bg school_track_on
show emi excited_happy_gym at center
with vpunch

"Me tambaleo hasta parar y caigo sobre mis manos y rodillas, jadeando por aire."

"Mi corazón está latiendo mucho más fuerte de lo que lo ha hecho en un largo tiempo."

stop music fadeout 1.0

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack
with Dissolve (0.2)

"No creo que lo haya hecho desde…"

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack
with Dissolve (0.2)

"Oh Dios."

scene black
with shuteyefast

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.2)

"Por favor cálmate, corazón."

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.5)

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.2)

"Solo cálmate. Deja de acelerar."

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.5)

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.2)

"Empiezo a toser, y por alguna razón, siento una sonrisa cruzar mi cara."

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.5)

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.2)

"Entonces así es como muero, ¿eh?"

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.5)

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.2)

"¿Tratando de mantenerme saludable?"

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.5)

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.2)

"Qué irónico."

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.5)

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.5)

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.2)

"Estoy listo para rendirme en este preciso instante."

play sound sfx_heartslow
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.8)

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack
with Dissolve (0.8)

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack
with Dissolve (0.2)

"Pero entonces, siento mi corazón reducir el ritmo."

"Dos manos me agarran debajo de los brazos y me dan un tirón hacia arriba."

scene bg school_track_on
show emi basic_confused_gym_close at center
with openeye

"Miro hacia arriba y veo a Emi de pie a mi lado, con una mezcla de alivio y preocupación."

emi "¡De pie!"

show emi sad_grin_gym_close
with charachange

emi "Vamos, nunca recuperarás el aliento de esa forma."

"De algún modo, me las arreglo para ponerme de pie. Intento levantar los brazos sobre mi cabeza, pero se sienten como de plomo."

"Empiezo a caminar alrededor de la pista mientras Emi se mantiene cerca, como si estuviera preocupada de que me vaya a caer al suelo o algo."

"Podría no estar muy equivocada."



"Me siento terrible, y lo digo."

show emi basic_closedhappy_gym_close
with charachange

"Emi se ríe."

show emi basic_happy_gym_close
with charachange

emi "Pero terminaste, ¿verdad?"

show emi basic_grin_gym_close
with charachange

emi "Dijiste que no podrías, pero lo hiciste."

emi "¿Acaso no vale eso la pena?"

"No estoy seguro, y realmente no tengo el aire para decirlo."

"Pero esa pequeña sonrisa que sentí en mi rostro hace un momento no se ha ido."

"¿Y qué si mi corazón es débil?"

"Aun así sobreviví esta mañana."

"Quizá sobreviva mañana, también."

scene bg school_track
with shorttimeskip

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")

play ambient sfx_emisprinting

"Tan pronto se vuelve aparente que no me voy a caer sin previo aviso, Emi empieza con sus sprints."

"No sé cómo diablos se las arregla para esprintar luego de correr más de kilómetro y medio, pero supongo que está en mucho mejor forma que yo."

"Una vez más, mientras camino por la pista, no puedo evitar observar a Emi correr."



scene ev emi_run_face_zoomin
with locationchange

"Es extraño, pero es como si fuera una persona distinta cuando se está exigiendo."

"La última vez me fijé en sus ojos, pero esta vez es su boca lo que me llama la atención."

"No tiene su sonrisa habitual."

"Aún está sonriendo, pero con cierta tensión."

"Es casi siniestro, como si estuviera peleando en una batalla perdida pero no le importara."

"Ella parece estar corriendo con más ganas, como lo hizo ayer."

"El sudor empieza a correr por su cara, pero sigue adelante."

"Su boca finalmente se abre porque no puede obtener suficiente aire por la nariz."

"Mientras pasa junto a mí de nuevo, piernas a un ritmo, los brazos en sincronía, y sus labios ligeramente entreabiertos…"

"Se ve hermosa."

stop ambient fadeout 2.0

scene bg school_track
with shorttimeskip

play music music_normal fadein 3.0
$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

"Después de que hemos dado unas cuantas vueltas para enfriarnos, Emi vuelve a ser la misma de siempre."

"La transformación que vi en ella ha desaparecido."

show emi basic_happy_gym at center
with charaenter

emi "No estuviste mal hoy, Hisao."

"Hay casi admiración en su voz."

hi "¿A qué te refieres? Me habría detenido si no me hubieras gritado."

show emi sad_shyblush_gym
with charachange

"Emi se sonroja un poco, viéndose avergonzada por su arrebato."

emi "Perdón por eso, es solo que… no puedo soportar ver a la gente rendirse."

emi "Especialmente por algo como esto."

show emi sad_grin_gym
with charachange

emi "Decir “no puedo seguir” es tonto cuando obviamente estás moviéndote mientras lo dices."

emi "De eso se trata todo esto."

hi "Qué, ¿decir cosas tontas?"

show emi basic_annoyed_gym
with charachange

"Emi me saca la lengua."

emi "Idiota. Me refiero a demostrar que estás vivo."

"Demostrar que estoy vivo, ¿eh? No sabía que tuviera que ser tan doloroso."

"Pero se siente bastante bien, a pesar de eso."

show emi excited_proud_gym
with charachange

emi "Además, este es uno de los días más duros."

hi "¿A qué te refieres?"

show emi basic_grin_gym
with charachange

emi "Siempre que empiezas algún ejercicio, es difícil el primer día, realmente duro el segundo, y luego el tercero es más fácil."

emi "Seguirás teniendo días que son muy difíciles, pero cada vez serán menos."

hi "Entonces esto se volverá más sencillo, ¿eh?"

show emi basic_closedhappy_gym
with charachange

emi "Sí, por supuesto."

show emi basic_closedgrin_gym
with charachange

emi "Pero entonces tendrás que aumentar la dificultad, o nunca avanzarás."

emi "Solo disminuirás el ritmo, y perderás la sensación de superación."

hi "Entonces tendré que correr más de cuatro vueltas, ¿eh?"

show emi excited_proud_gym
with charachange

emi "¡Síp! Pero no por un tiempo, tendrás que ser cuidadoso, ya sabes."

"Un pensamiento asalta a Emi, y su rostro se ilumina."

show emi basic_closedhappy_gym
with charachange

emi "¡Lo tengo!"

hi "¿Qué tienes?"

show emi basic_happy_gym
with charachange

emi "¡Puedes venir a ver al enfermero conmigo! ¡Así no caerás muerto o algo así!"

"Qué encantador."

hi "Eh… ¿cuándo?"

show emi basic_grin_gym
with charachange

emi "¡Ahora mismo, por supuesto! Necesitarás una ducha y todo eso, ¿cierto? ¡Entonces no tenemos mucho tiempo!"

"Agarrando mi mano, se va, arrastrándome junto a ella."

stop music fadeout 2.0


label es_E7:

scene bg school_nurseoffice
show nurse neutral at center
with shorttimeskip

nk "Por todos los cielos, andas apurada el día de hoy, ¿no, Emi?"

play music music_nurse fadein 2.0

"No tengo idea de cómo llegamos a la oficina del enfermero tan rápido, pero aquí estamos."

show nurse neutral at twoleft
show bg school_nurseoffice at bgleft
with charamove

show emi basic_grin_gym at tworight
with charaenter

"El enfermero le sonríe a Emi y parece ignorarme por completo."

show nurse grin
with charachange

nk "Sabes que tienes tiempo de sobra para tomar un baño e ir a clases."

show nurse concern
with charachange

nk "No hace falta correr así por los pasillos. ¡Podría escucharte venir a un kilómetro de distancia!"

"Por algún motivo, no parece estar regañando a Emi de verdad."

"Es como si esto fuera algún tipo de rutina entre los dos."

"Emi hace una imitación aceptable de remordimiento."

show emi excited_sad_gym
with charachange

emi "¡Lo siento! ¡No lo volveré a hacer!"

show nurse grin
show emi basic_closedhappy_gym
with charachange

"Tanto el enfermero como Emi se ríen de alguna broma secreta."

show emi basic_grin_gym
show nurse neutral
with charachange

"De repente, parece que él me nota."

show nurse fabulous
with charachange

nk "Ah, hola, Hisao."

show nurse neutral
with charachange

nk "¿Qué te trae por acá?"

hi "Bueno, he estado—{w=.3}{nw}"

show emi basic_closedgrin_gym
with charachange

emi "Hisao se ha unido oficialmente a mis carreras matutinas."

"Empiezo a explicar, pero Emi me interrumpe."

show emi basic_happy_gym
with charachange

emi "Pensé que él podría visitarte para que no se muera o algo así."

show nurse fabulous
with charachange

"El enfermero alza una ceja en fingido horror."


nk "Sí, eso sin duda acabaría con mi trabajo en un parpadeo, ¿no creen?"

show nurse neutral
show emi basic_grin_gym
with charachange

nk "Pues bien, Hisao, vamos a echarte un vistazo."

nk "¿Podrías levantarte la camiseta?"

"Repentinamente estoy muy consciente de que Emi está en el cuarto conmigo y me sonrojo, a mi pesar."

"El enfermero parece notar mi incomodidad, pero solo parece divertirle."

show nurse grin
with charachange

nk "Eres un poco tímido, ¿eh?"

"Él se inclina ante Emi, disculpándose."

nk "Perdona, Emi, intenté conseguirte un espectáculo gratuito, pero no parece haber funcionado."

show emi basic_annoyed_gym
with charachange

"Emi endurece un poco la expresión y le lanza una mirada de irritación."


emi "Eres un idiota."

show emi excited_proud_gym
with charachange

"Emi me hace una media reverencia a modo de disculpa."

emi "Esperaré afuera, ¿de acuerdo, Hisao?"

hide emi
with charaexit

show nurse grin at center
show bg school_nurseoffice at center
with charamove


"Empiezo a balbucear que realmente no es un problema, no tiene que irse, pero ella ya cruzó la puerta y el enfermero se ríe mientras la ve marcharse."

show nurse fabulous
with charachange

nk "¡Aún puedo! ¡Ja!"

hi "No entiendo."

show nurse grin
with charachange

"Se ríe de nuevo, como si bromeara con algo que no comprendo."

nk "Aún puedo ponerla nerviosa. Es una especie de disputa que hemos tenido desde hace tiempo."

"Eso suena increíblemente siniestro para mí, y parece que el enfermero también se da cuenta."

show nurse concern
with charachange

nk "Eh. Ahora que lo pienso, eso sonó mucho peor de lo que en realidad es."

hi "No iba a decir nada…"

nk "No no, tienes razón. Debería de informarte un poco para que no te hagas una idea equivocada."

show nurse neutral
with charachange

nk "Verás, la verdad es que soy relativamente nuevo aquí. Me contrataron el mismo año en el que Emi empezó a venir aquí."

nk "Antes de eso, trabajé con Emi en su rehabilitación inicial luego de su accidente."

"Espera un momento, ¿qué?"

show nurse concern
with charachange

nk "Tuvimos que amputarle las piernas luego de un aparatoso accidente automovilístico. Casi la mata, y logró—"

"Se calla bruscamente. Parpadeo al recibir esta inesperada información."

nk "Bueno, no me corresponde decir eso. De todas maneras, nos hemos conocido por bastante tiempo."

nk "Así que tenemos una relación un poco más familiar de lo que es estrictamente profesional."

"Se ve avergonzado, como si hubiera hecho algo estúpido."

"Supongo que está realmente preocupado por eso. Sacudo una mano para darle a entender que no pasa nada."


hi "No se preocupe, señor. Prometo que voy a ser discreto."

"Me había estado preguntando qué provocó que Emi perdiera sus piernas, y ese era uno de los escenarios que imaginé."

"Había tantas maneras en las que podría haber ocurrido, pero escuchar los hechos directamente… no deja de ser un poco chocante."

show nurse neutral
with charachange

nk "Bueno, gracias. Eres un buen niño, Hisao."

nk "Puedo ver por qué te hiciste amigo de Emi."

show nurse fabulous
with charachange

nk "Ella es indomable, sabes."

hi "¿A qué te refieres?"

nk "No la viste aprendiendo a caminar. Ella se esforzaba mucho más que todos los demás en el hospital. Se rehusaba a rendirse."

nk "Normalmente tomaría años llegar al punto en el que puedes considerar correr de nuevo. Emi lo hizo todo en aproximadamente un año."

"Parece casi orgulloso de ella, como un padre que ve a su hija ganar una competencia o algo."

show nurse neutral
with charachange

nk "Demonios, probablemente lo habría hecho aún más rápido de no ser porque no la dejaríamos."

hi "¿No la dejarían? ¿Por qué no?"

show nurse concern
with charachange

stop music fadeout 4.0

nk "Porque se esforzaría tanto que sus piernas podrían sangrar donde se unen a sus prótesis."

nk "Es una preocupación real, es por eso que viene aquí todos los días luego de correr."


nk "Ni hablar del riesgo de infección si se cortara en las piernas y sus prótesis estuvieran sucias."

show nurse neutral
with charachange

nk "Pero suficiente de eso."

show nurse fabulous
with charachange

play music music_nurse fadein 2.0

nk "Si no nos apresuramos, Emi pensará que tramamos algo."

"Cuando dice esto, me guiña un ojo y empieza a revisar mi ritmo cardiaco."

"El estetoscopio está demasiado frío."

"Debería de haberlo calentado o algo antes de usarlo."

"Después de unos segundos retrocede, satisfecho."

show nurse neutral
with charachange

nk "Bueno, suenas bastante bien para mí, Hisao. No tuviste ningún dolor en el pecho mientras corrías, ¿o sí?"

hi "No, no realmente. Aunque tuve problemas para recuperar el aliento, y mi corazón también estaba agitado al final."

show nurse concern at center
with charachange

"El enfermero frunce el ceño mientras digo esto, pero luego se encoge de hombros."

show nurse neutral at center
with charachange

nk "Probablemente sea solo porque estás fuera de forma… pero si no mejoras, entonces deberías hacérmelo saber, ¿entendido?"

nk "No te exijas demasiado, y por supuesto, si tienes cualquier dolor en el pecho, ven a verme inmediatamente, ¿de acuerdo?"

"Me pongo la camiseta de nuevo, y el enfermero se asoma por la puerta para llamar a Emi."

show nurse neutral at twoleft
show bg school_nurseoffice at bgleft
with charamove

show emi basic_annoyed_gym at tworight
with charaenter

emi "¿Qué les tomó tanto tiempo? ¡Ahora llegaré tarde!"

stop music fadeout 2.0

show nurse fabulous
with charachange

"El enfermero me lanza una mirada elocuente."

show nurse grin
with charachange

nk "Solo seducía a Hisao, eso es todo."

play music music_comedy fadein 0.5

show emi sad_annoyed_gym
with charachange

emi "¿¡Qué!? Vamos, ¿qué te he dicho de seducir a mis amigos?"

"Esperaba que Emi se sorprendiera por esto, pero en vez de eso, simplemente se ve molesta, regañando al enfermero como si fuera un niño robando galletas."

"Mientras tanto, me esfuerzo en no sonrojarme por la insinuación del enfermero."

show nurse fabulous
with charachange


nk "Intentaré no hacerlo de nuevo, ¡aunque temo que el joven Hisao podría estar ya perdido para el género femenino por siempre!"

stop music fadeout 0.5

hi "Ni aunque me paguen."

with Pause(3.0)

play music music_comedy fadein 0.5

show nurse grin
show emi excited_laugh_gym
with charachange

"No quise decirlo en voz alta, pero ambos me observan por un momento antes de estallar en carcajadas de nuevo."

show emi basic_happy_gym
with charachange

emi "Te dije que era divertido, ¿verdad?"

"Huh. Supongo que Emi habla de muchas cosas con el enfermero."

show nurse fabulous
show emi basic_grin_gym
with charachange

nk "Bueno, Hisao, probablemente deberías irte. Necesitas bañarte antes de que empiecen las clases, ¿no crees?"

"¡Diablos! Tiene razón, ¡y parece que solo me queda media hora!"

hi "Gracias por tu tiempo. ¡Te veo luego, Emi!"

scene bg school_nursehall
with locationchange

stop music fadeout 5.0

"Me apresuro en salir del cuarto en lo que el enfermero empieza a remover las prótesis de Emi."

"Mientras me dirijo al corredor, apenas alcanzo a oír su voz detrás de mí."

nk "Emi, debes ser más cuidadosa…"

scene bg school_dormhisao
with locationskip

"Regreso a mi habitación y me ducho en tiempo récord. Caigo en la cuenta de que ya he estado despierto por cuatro horas, y las clases ni siquiera han empezado."

"Este va a ser un día muy, muy largo."

"Espero no quedarme dormido en clase."

$ suppress_window_after_timeskip = True

scene black
with dissolve


label es_E8:

window hide None

scene black
with dissolve

show bg school_dormhisao
with openeye

window show

play music music_pearly fadein 5.0

"Me despierta la luz de la mañana colándose por mi ventana, en vez de mi alarma, y me doy cuenta de que debe de ser domingo."


"Emi, bondadosamente, se ha dignado a concederme los fines de semana libres de carreras."

"La verdad no sé si ayer desperté, o si solo dormí durante todo el día."

"Mis piernas gimen en protesta mientras salgo de mi cama."

"Todas estas carreras realmente me han agotado."

"Sin embargo, no puedo negar que Emi no me mentía."

"Se ha vuelto un poquito más fácil."



"Me preocupaba que las carreras empezaran a trastornarme, pero hasta este momento no me han afectado tanto."

"Bueno, solo ha pasado una semana."

"Creo que tengo tiempo de sobra para comenzar a temer al sonido de mi alarma por las mañanas."

"Tampoco es que pueda abandonarlo ahora."

"Como dijo Emi, es más difícil detener una rutina cuando hay otra persona."

"Y francamente no creo estar preparado para hacer frente a una Emi decepcionada."

"Probablemente usaría esos ojos de cachorrito y me sentiría terrible conmigo mismo."

"Lo que me recuerda… ¿no se supone que hoy debería de estar en alguna parte?"

$ renpy.music.set_volume(0.3,2.0,channel="music")

scene bg school_track_fb
show emi basic_closedhappy_gym_fb at center
show noiseoverlay
with flashback

emi "Oye, vendrás a mi competencia de atletismo el domingo, ¿verdad?"

show emi basic_grin_gym_fb
with charachange

emi "De qué estoy hablando, claro que vendrás."

show emi sad_grin_gym_fb
with charachange

emi "¿Verdad?"

"Esos ojos de cachorrito de nuevo."

hi "¡Por supuesto que voy a ir!"

hi "Te lo debo, ¿no es cierto?"

show emi excited_proud_gym_fb
with charachange

emi "¡Exactamente! Así que no lo olvides, ¿de acuerdo?"

$ renpy.music.set_volume(1.0,2.0,channel="music")

scene bg school_dormhisao
with flashforward

"¡Diablos, la competencia de Emi!"

"Será mejor que empiece a moverme si no quiero faltar a su carrera, ya que ella es la única razón por la que estoy considerando ir."

"Si no, no tendría ningún sentido."

scene bg school_courtyard
show crowd
with shorttimeskip

play ambient sfx_crowd_outdoors fadein 3.0

"Y así, pronto me encuentro rodeado por una multitud de personas, todas aquí para ver a nuestro equipo de atletismo competir contra otra escuela como esta."

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")
$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

nvl clear

nvl show dissolve

n "\nLo admito, es casi reconfortante saber que no somos la única escuela como esta."

n "Después de que ves que puede haber {b}dos{/b} escuelas con un montón de… niños defectuosos, bueno."

n "… Dejas de sentirte tan defectuoso."

n "También dejas de sentirte único, lo que en la mayoría de los casos sería algo malo, pero en este caso dista mucho de serlo."

n "Supongo que eso es parte del atractivo de Yamaku."

n "Aprender que no eres único… diablos, aprender que hay muchos otros que matarían por sufrir tus problemas en vez de lo que sea que tienen ellos."

n "Algunos de estos niños no están aquí porque les falte una pierna o tengan un problema en el corazón."

n "Algunos de ellos podrían estar aquí porque estarán muertos en dos, quizá tres años si tienen suerte."

n "Y eso solo si reciben los cuidados correctos."

n "Es una especie de amargo consuelo ser capaz de decir “Bueno, al menos tengo una oportunidad de estar vivo mientras termino la universidad”, pero está ahí."

$ renpy.music.set_volume(1.0, 2.0, channel="ambient")
$ renpy.music.set_volume(1.0, 2.0, channel="music")
nvl clear

nvl hide dissolve

window show

stop music fadeout 3.0

"Soy expulsado de mis mórbidas reflexiones por la aparición de Rin cerca de la entrada a las gradas."

show rin basic_deadpannormal at center
with charaenter

rin "Viniste."

hi "Por supuesto. Dije que lo haría, ¿no es cierto?"

show rin basic_deadpanamused
with charachange

rin "Eso no necesariamente implica que cumplirías tu palabra."

show rin basic_awayabsent
with charachange

rin "Muchas personas dicen cosas y no hablan en serio."

hi "Bueno, yo no."

play music music_soothing fadein 0.5

show rin relaxed_boredom
with charachange

"Rin se encoge de hombros. Al parecer aburrida por nuestra conversación, se da vuelta y se dirige de nuevo hacia las gradas."

rin "Ahora le debo dinero a Emi."

hi "¿Y eso por qué?"

show rin basic_absent
with charachange

rin "No pensé que te aparecerías."

rin "Emi sí."

show rin basic_awayabsent
with charachange

rin "Así que le debo 500 yenes."

hi "Ustedes dos apuestan demasiado, ¿o no?"

"Mi compañera sin brazos se encoge de hombros otra vez."

show rin basic_deadpan
with charachange

rin "No lo creo."

scene bg school_track
show crowd
show rin basic_deadpan
with locationchange

"Subimos a las gradas, y Rin señala hacia arriba con la cabeza."

show rin negative_spaciness at center
with charaenter

rin "Allá arriba."

show rin basic_deadpancontemplation
with charachange

rin "Salí para ver si vendrías."

"Por la apuesta, me imagino."

"Rin dirige el camino, y pronto nos hemos sentado en una banca casi vacía."

$ renpy.music.set_volume(0.3, 3.0, channel="ambient")

show rin basic_deadpancontemplation at tworight
show bg school_track at bgright
show crowd:
    linear 1.0 alpha 0.0
with charamove

hide crowd
show meiko smile at twoleft
with charaenter

"Hay una señora sentada junto a Rin —la madre de alguien, supongo."

"Lleva el cabello bastante largo recogido en una trenza. Al ver a Rin, ella le da una sonrisa extrañamente familiar."

show meiko happy
with charachange

emm_ "Vaya, esta es una sorpresa."

show meiko wink
with charachange

emm_ "Pensé que ibas por un bocadillo, no por un chico."

hi "¿Eh?"

show rin basic_surprised
with charachange

rin "¿Un bocadillo?"

show rin relaxed_nonchalant
with charachange


rin "Ya me preguntaba por qué andaba yo allá abajo."

show meiko happy
show rin basic_awayabsent
with charachange

"La mujer se ríe, de nuevo de una manera que me parece familiar."

"¿Dónde la he visto antes?"

show meiko smile
with charachange

emm_ "Bueno, supongo que siempre has sido alguien que sale por algo y trae otra cosa."

emm_ "¡Pero qué descortés soy! No me he presentado."

emm_ "Soy Meiko Ibarazaki, la madre de Emi."

show meiko happy
with charachange

emm "Encantada de conocerte."

"Bueno, eso lo explica."

"Ella es como una Emi mayor, más alta y mejor dotada."

"Aparte de que su cabello es de un tono más oscuro que el de Emi, realmente no hay duda del parecido."

show rin basic_absent
show meiko smile
with charachange

hi "Disculpe, soy Hisao. Hisao Nakai."

hi "Y en serio, no tiene que pedir disculpas por no presentarse, señora Ibarazaki."

hi "En realidad es el trabajo de Rin en esta situación, ¿no es así?"

show meiko happy
show rin basic_awayabsent
with charachange

"Otra risa de la madre de Emi."

emm "Entonces me parece que no has conocido a Rin el tiempo suficiente."

show meiko smile
with charachange

emm "Es mejor no esperar que recuerde algo como eso."

show meiko wink
with charachange

emm "Tiene otras cosas en las que pensar, supongo."

show rin basic_deadpannormal
with charachange

"Rin asiente, viéndose complacida por esta apreciación."

show rin basic_deadpan
with charachange

rin "Tiene razón."

show rin basic_lucid
with charachange

rin "Estaba pensando en puestas de sol."

show meiko happy
show rin basic_awayabsent
with charachange

emm "¿Ves? En realidad nos corresponden a nosotros las presentaciones y demás."

"A falta de una mejor respuesta, asiento."

"La señora Ibarazaki se reclina un poco en su asiento y alza una ceja."

$ renpy.music.set_volume(0.0, 0.5, channel="ambient")

show meiko serious
with charachange

stop music fadeout 0.8

emm "Así que, ¿cuánto tiempo hace que tú y Rin han estado saliendo?"

"Mi respuesta consiste en silencio en lo que mi cerebro repentinamente se pone en marcha. Pero justo antes de que pueda empezar a balbucear una apresurada explicación, la madre de Emi rompe en carcajadas de nuevo."

play music music_soothing fadein 0.5
$ renpy.music.set_volume(0.3, 0.5, channel="ambient")

show meiko happy
with charachange

emm "¡Ja! Eres de los que se sonrojan, ¿no es así?"

"No sé si hay alguna manera de conservar mi dignidad en esta situación, así que me conformo con responder entre dientes."

show meiko smile
show rin basic_absent
with charachange

hi "Tal vez."

show rin basic_awayabsent
with charachange

emm "Así que esto debe ser un romance reciente, ¿verdad?"

show rin basic_absent
with charachange

hi "Espera, esa no es la pregunta que—"

show meiko happy
show rin basic_awayabsent
with charachange

"Otra carcajada."

show meiko smile
with charachange

emm "Lo sé, pero es divertido verte retorcer."

show meiko wink
with charachange

emm "Lo siento. Perdona las diversiones de una vieja."

"¿Vieja?"

"No me lo parece en absoluto."

"Evidentemente Emi sacó los rasgos juveniles de su madre."

show rin basic_absent
with charachange

hi "Supongo que lo puedo dejar pasar."

show meiko happy
show rin basic_awayabsent
with charachange

emm "Qué amable de tu parte."

stop music fadeout 6.0

show rin basic_deadpan
with charachange

rin "Está empezando."

stop ambient fadeout 2.0

scene ev emitrack_blocks at Fullpan(12.0, dir="left", time_warp=_ease_in_time_warp)
with locationskip

"Dirijo mi atención a la pista, donde se preparan para el primer sprint."

"Parece ser la carrera de 400 metros."

"Mis ojos examinan a las corredoras antes de encontrar a Emi."

scene ev emitrack_blocks_close
with flash

"Está sonriendo, con una mirada casi arrogante en su cara."

show insert startpistol at right
with easeinright

"El juez de salida levanta su pistola."

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")

play sound sfx_startpistol
play ambient sfx_emisprinting

scene ev emitrack_running at Fullpan(1.0, dir="left", time_warp=_ease_in_time_warp)
with silentflash


"Emi sale disparada de los tacos de salida, desapareciendo de la línea de inicio en un abrir y cerrar de ojos."

"Es sorprendente. Incluso cuando las demás velocistas convergen en los carriles más cercanos a la línea interior, Emi arranca al frente del grupo."

"Para el momento en que llega a la curva final, algunas de las otras corredoras la han alcanzado."

"Aunque sus esfuerzos resultan inútiles, ya que un último impulso de Emi las deja por lo menos medio segundo atrás."

scene ev emitrack_finishtop:
    xalign 0.5 yalign 0.0 zoom 4.0 subpixel True
    0.2
    linear 0.3 zoom 1.05
    easein 8.0 zoom 1.0
with flash

stop ambient fadeout 1.0
play sound sfx_crowd_cheer

"La Sra. Ibarazaki exclama y grita, aplaudiendo freneticamente, basicamente viéndose como cualquier otro padre animando a su hijo."

"Emi sale de la pista, viéndose satisfecha consigo misma."

scene bg school_track at bgright
show meiko happy at twoleft
show rin basic_deadpandelight at tworight
with locationchange

play music music_daily fadein 2.0

"La animo junto a todos los demás."

"La anunciadora (quien suena sospechosamente similar a Misha) anuncia alegremente los resultados."

show meiko smile
show rin basic_awayabsent
with charachange

emm "Creo que se ha vuelto más rápida desde la última vez."

show rin basic_absent
with charachange

hi "Eso fue increíble."

show meiko happy
show rin basic_awayabsent
with charachange

"La señora Ibarazaki sonríe con orgullo."

emm "Emi es una corredora tremenda."

show meiko smile
with charachange

"Nos sentamos en silencio mientras preparan el siguiente evento."

"Me sorprende ver a Emi caminando de nuevo hacia la pista."

show rin basic_absent
with charachange

hi "Esperen, ¿que no acaba de correr?"

"La madre de Emi asiente."

show rin basic_awayabsent
with charachange

emm "Sí, pero ella corre en varios eventos para su equipo. Especialmente los sprints."

show meiko happy
with charachange

emm "Es mucho, pero Emi puede soportarlo."

"Por cómo se ven las cosas, está en lo correcto."

"Emi no parece cansada, como si no hubiera corrido en el evento anterior."

"De no ser por el sudor visible en su camiseta, nunca lo sabrías."

show rin basic_absent
with charachange

hi "¿Cuál evento es este?"

show meiko smile
show rin basic_awayabsent
with charachange

emm "La carrera de 200 metros."

emm "Ella correrá en esta, la de 100 metros, y los relevos."

show rin basic_absent
with charachange

hi "Ya veo."

show rin negative_spaciness
with charachange

play sound sfx_startpistol
play ambient sfx_emisprinting

"Una vez más suena el pistoletazo, y una vez más Emi despega de los tacos de salida."


"El sonido de un golpeteo desvía mi atención de la carrera."

"Es el pie de Rin."

"Parece completamente absorta en la carrera."

show meiko happy
with charachange

stop ambient fadeout 1.0
play sound sfx_crowd_cheer

"La madre de Emi echa porras de nuevo, y supongo que la carrera terminó."

"No me parece que los sprints tomen mucho tiempo para acabarse."

hi "Tu pie."

show rin relaxed_surprised
show meiko smile
with charachange

rin "¿Hmm?"

hi "Tu pie estaba golpeando las gradas."

show rin basic_deadpan
with charachange

rin "Oh."

hi "Parece que esto te gusta mucho. Estoy sorprendido."

show rin basic_deadpansurprised
with charachange

"Rin me mira crípticamente."

rin "¿Por qué no habría de gustarme?"

hi "Por nada en particular, solo pensé que cosas como los deportes no te interesarían."

show rin relaxed_nonchalant
with charachange

rin "Hmm, supongo que tienes razón."

rin "No es tan interesante."

show rin basic_deadpannormal
with charachange

rin "Pero estoy viendo a Emi, no al deporte."

hi "No entiendo."

show rin basic_lucid
with charachange

rin "Emi es más Emi que nunca cuando corre."

rin "No puedes ver a Emi en su más Emi muy seguido."

show rin basic_deadpanamused
with charachange

rin "Pero aquí, puedes. ¿Ves?"

"Dirige mi atención hacia la pista una vez más, donde la carrera de los 100 metros está a punto de comenzar."

stop music fadeout 6.0
stop sound fadeout 2.0

scene ev emitrack_blocks_close
with locationskip

"Miro a Emi de cerca."

"A medida que se sube a los tacos de salida, todo su cuerpo parece relajarse, pero es un relajamiento falso."

"Puedo ver que ella en realidad es como un resorte."

scene ev emitrack_blocks_close_grin
with locationchange

"Cuando el juez de salida le dice a todos que se preparen, ella mueve su cabeza hacia arriba de golpe y sus ojos se entrecierran un poco."

"Su boca se curva hacia arriba en lo que podría ser una sonrisa y podría ser un gruñido."

play sound sfx_startpistol
play ambient sfx_emisprinting

scene ev emi_run_face_zoomin
with locationskip

"Cuando la pistola se dispara, es como si hubiera sido liberada de una jaula, como si siempre estuviera moviéndose con esta rapidez deslumbrante, pero no pudiéramos verlo hasta que la pistola de salida disipase la ilusión de inmovilidad."

"Todo termina en unos cuantos segundos, pero en esos segundos siento como si hubiera presenciado algo muy personal para Emi."

stop ambient fadeout 1.0
play sound sfx_crowd_cheer

"Tan pronto cruzó la línea de meta, la mirada feroz fue reemplazada por su sonrisa normal."

"El general vencedor regresando a su granja."

hi "Asombrosa."

hi "Ella es realmente asombrosa. Nunca he visto a nadie moverse así de rápido."

scene bg school_track at bgright
show meiko smile at twoleft
show rin basic_deadpanamused at tworight
with locationchange

emm "Bueno, no me mires a mí, soy demasiado relajada como para correr así de rápido."

show meiko worry
show rin basic_awayabsent
with charachange

emm "No, creo que todo el coraje de Emi viene de parte de su padre."

"A la mención del padre de Emi, la señora Ibarazaki se ve melancólica, casi triste."

emm "Él hizo que se interesara en el atletismo, ¿sabes?"

show rin basic_absent
with charachange

hi "Sí, ella me lo dijo."

"No estoy seguro de si sería grosero o no de mi parte preguntar por el padre de Emi."

"Pero después de esa mirada en su rostro unos días atrás, me siento obligado a hacerlo."

hi "¿Dónde está su padre ahora, si se puede saber?"

"La madre de Emi vacila, claramente no quiere contestar la pregunta pero al mismo tiempo intenta no parecer descortés."

show meiko serious
show rin basic_awayabsent
with charachange

emm "Él… ya no está aquí."

hi "Lo siento, no quise traer malos recuerdos."

show rin basic_absent
with charachange

hi "Es solo que Emi se veía un poco triste cuando lo mencionó antes."

show meiko worry
show rin basic_awayabsent
with charachange


emm "Eso no es sorprendente, teniendo todo en cuenta."

hi "¿Hmm?"

emm "Eran muy unidos."

show rin basic_absent
with charachange

hi "Ya veo."

play sound sfx_cellphone

"Un ruido intermitente emana súbitamente del bolsillo de la Sra. Ibarazaki. Rebuscando en él, ella saca un celular y lo mira."

show meiko serious
show rin basic_awayabsent
with charachange

emm "… ¿En serio, mensajes de texto?"

emm "¿Cuántos años tiene? ¿Dieciséis?"

hi "¿Hmm?"

show meiko smile
with charachange

emm "Oh, nada."

show meiko wink
with charachange

emm "Tengo que ir a encontrarme con un amigo mío."

show meiko happy
with charachange

emm "¿Le dirían a Emi que estoy muy orgullosa de ella y que la llamaré más tarde en la noche?"

show rin basic_absent
with charachange

hi "Por supuesto."

hide meiko
with charaexit

show rin basic_absent at center
show bg school_track at center
with charamove

show rin basic_awayabsent
with shorttimeskip

play music music_tranquil fadein 2.0

"Admito que me distraje por un rato."

"Casi no me doy cuenta de que los relevos están por empezar. Pero cuando miro, no puedo encontrar a Emi."

hi "Pensé que Emi correría en los relevos."

show rin basic_deadpan
with charachange

rin "Ella es el ancla."

show rin basic_deadpannormal
with charachange

rin "Así que no correrá por un rato, todavía."

hi "Ah."

show rin basic_deadpandelight
with charachange

rin "¿Lo viste?"

hi "¿Huh?"

rin "Emi en su más Emi."

hi "Tal vez."

show rin basic_deadpanupset
with charachange

rin "Hmm. Quizás esta vez."

play sound sfx_startpistol

"La carrera comienza, y le echo porras a las compañeras de equipo de Emi cuando pasan la estafeta."

play ambient sfx_emisprinting

scene ev emitrack_running:
    truecenter zoom 1.0 subpixel True
    ease 20.0 zoom 1.05 xalign 0.0 yalign 0.0
with locationskip

"Finalmente, veo a Emi hacer el sprint en la pista para tomar el último pase."

"Una vez más estoy sorprendido por cuán grácil se ve cuando corre."

"Es realmente hermoso."

"La mirada de determinación y audacia en su rostro solo acentúa la imagen."

"Emi en su más Emi, supongo."

stop ambient fadeout 1.0
play sound sfx_crowd_cheer

show ev emitrack_finish
with locationskip

"Pero entonces, mientras cruza la línea de meta, la veo tropezar brevemente."

"Es muy ligero, pero es definitivamente un tropezón."

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

scene bg school_track
show rin negative_worried at center
with locationskip

"Rin inhala bruscamente, y se ve realmente preocupada por un momento."

rin "Oh, Emi…"

hi "¿Crees que se lastimó?"

show rin basic_surprised
with charachange

rin "¿También lo notaste?"

show rin negative_confused
with charachange

rin "Debe de ser malo."

show rin negative_annoyed
with charachange

"Frunce el ceño, como si decidiera qué debería hacer después."

"Eventualmente parece ser demasiado aburrido, y se encoge de hombros de nuevo."

show rin basic_deadpanupset
with charachange

rin "Bueno, vamos abajo."

rin "Tenemos que coronar a la vencedora."

show rin basic_deadpanamused
with charachange

rin "Mira si puedes encontrar una ramita de laurel."

hi "Eso no va a ser fácil."

show rin basic_deadpannormal
with charachange

"Rin se encoge de hombros."

show rin basic_deadpan
with charachange

rin "Al menos lo intentamos."

"Bueno, en realidad no le pusimos mucho empeño."

"O ninguno en absoluto. Pero vamos, como sea."

stop music fadeout 5.0
stop sound fadeout 5.0
play ambient sfx_crowd_outdoors fadein 2.0

scene bg school_track_on
show crowd
show rin basic_awayabsent at center
with locationskip

"Emi está rodeada por sus compañeras, todas ellas felicitándola por la carrera."

"Rin parece estar esperando a que Emi se percate de su llegada."

"Ah, cierto, supongo que no puede precisamente hacerle gestos con las manos."

"Por otro lado, no estoy seguro de que Rin haría tal cosa aun si tuviera brazos."

"No parece que su estilo sea atraer la atención de los demás hacia ella. O hacer algún gesto más que encogerse de hombros."

"De cualquier modo, no estoy dispuesto a esperar, así que le hago un gesto a Emi, quien vuelve a ver y me sonríe alegremente… eh, nos sonríe."

show bg school_track_on at bgright
show crowd at bgright
show rin basic_awayabsent at tworight
with charamove

play music music_emi fadein 1.0

show emi basic_closedhappy_gym at twoleft
with charaenter

emi "¡Qué tal, te apareciste!"

show emi excited_proud_gym
with charachange

emi "Supongo que Rin me debe dinero, ¿eh?"

show rin basic_deadpanupset
with charachange

rin "Te hubiéramos traído una corona de laureles, pero Hisao no encontró ninguna."

show emi basic_grin_gym
with charachange

hi "Oye, tú tampoco."

show rin basic_deadpan
with charachange

rin "No era mi trabajo buscar."

hi "¿Cuándo asignamos los trabajos?"

show rin basic_deadpannormal
with charachange

rin "Cuando dije “Mira si puedes encontrar una ramita de laurel”."

show rin basic_deadpandelight
with charachange

rin "Trata de seguir el ritmo."

"Me encojo de hombros. Creo que Rin me lo está contagiando."

hi "Parece que es mi culpa después de todo, Emi."

show emi basic_closedhappy_gym
show rin basic_awayabsent
with charachange

"Emi se ríe de Rin y de mí."

show emi basic_happy_gym
with charachange

emi "Está bien, estoy segura de que me lo compensarán de alguna manera."

show rin basic_absent
with charachange

hi "Ah, claro."

show rin basic_awayabsent
show emi excited_amused_gym
with charachange

emi "¡Bien! Así que, ¿cómo me vi?"

show rin basic_absent
with charachange

"Me detengo antes de soltar “hermosa” o “asombrosa” y me conformo con un sustancialmente más seguro “muy impresionante”."

show emi basic_closedgrin_gym
with charachange

"Emi parece complacida con esta valoración."

"No menciono cuán todavía más impresionante es su desempeño dada su falta de piernas. Me imagino que ya lo sabe."

"Además, parece que le restaría mérito a su esfuerzo, de algún modo."

show emi basic_grin_gym
show rin basic_awayabsent
with charachange

emi "¡Estupendo saberlo! Me preocupaba haberme visto un poco lenta en los relevos, pero supongo que lo hice bien, ¿eh?"

show rin basic_absent
with charachange

hi "De hecho, noté—{w=.4}{nw}"

play sound sfx_impact

show rin basic_deadpanupset
with vpunch

"Rin me da un golpe con el pie y evita que termine mi oración."

show emi basic_confused_gym
with charachange

emi "¿A qué se debió eso?"

show rin basic_deadpancontemplation
with charachange

rin "Lo notó. Al final."

show emi basic_annoyed_gym
with charachange

emi "Hmm, eso no es bueno."

show emi sad_grin_gym
with charachange

emi "Supongo que el enfermero me lo revisará más tarde."

show emi sad_grit_gym
with Dissolve(0.2)

show emi sad_grin_gym
with charachange

"Hay una negligencia en su voz, como si no fuera gran cosa, pero repentinamente noto una pequeña mueca en su cara."

"Como si intentara esconder el hecho de que le duele."

"Es entonces cuando me doy cuenta de que su respiración es algo superficial, también."

"Supongo que realmente está lastimada."

"Ella debe notar mi preocupación, porque da un saltito hacia mí y me da unas palmaditas amistosas en el hombro."

show emi basic_closedgrin_gym_close
show rin basic_deadpannormal
with characlose

emi "¡Oye, te ves un poco preocupado!"

show emi basic_grin_gym_close
with charachange

emi "¡Estoy bien, en serio!"

emi "Solo un poco adolorida por tanto correr, es todo."

show emi excited_proud_gym_close
with charachange

emi "Y vamos, un poco de dolor no va a detenerme."

hi "¿Ah no?"

show emi basic_closedgrin_gym_close
with charachange

"Emi sonríe, y por un momento se ve como lo hizo durante la carrera, feroz e inconquistable."

"O por decirlo de otra manera, realmente hermosa."

show emi basic_grin_gym_close
with charachange

emi "Aún no lo ha hecho."

hi "Bien. Entonces supongo que no debería de preocuparme, ¿eh?"

show emi basic_closedhappy_gym_close
with charachange


emi "¡Ya lo creo, carajo! ¡Soy Emi Ibarazaki, la más rápida sin piernas! ¡No me detendré por nada!"

hi "Impresionante."

show emi basic_closedgrin_gym_close
with charachange

"Emi se ríe, y luego parece recordar algo."

show emi basic_grin_gym_close
with charachange

emi "Oh, antes de que lo olvide…"

emi "¡Rin y yo vamos a hacer algo el próximo domingo como festejo después de la competencia!"

show emi excited_proud_gym_close
with charachange

emi "¡Deberías de venir!"

show emi sad_grin_gym_close
with charachange

emi "Normalmente lo hacemos un día después, pero ya que la competencia fue un domingo, tengo tareas y clases y todas esas cosas de las que encargarme."

show emi basic_closedgrin_gym_close
with charachange

emi "Además de nuestra carrera de mañana, por supuesto."

hi "Claro, por supuesto."

hi "Oh, cierto. Tu mamá quería decirte que está orgullosa de ti."

hi "Te llamará más tarde en la noche."

show emi basic_happy_gym_close
with charachange

emi "¡Pensé que la había visto en las gradas!"

show emi basic_closedhappy_gym_close
with charachange

emi "¡Me alegra que haya podido venir!"

show emi sad_grin_gym_close
with charachange

emi "Solía ser mi padre quien venía a mis competencias, pero mamá ha hecho un gran trabajo tomando su lugar."

show emi sad_shy_gym_close at Transform(function=tf_lefttremble)
with Dissolve(0.1)

"Ella tiembla un poco, y me doy cuenta de que está toda sudada."

"También ha empezado a soplar una brisa."

"No tengo frío, y traigo mi chaqueta conmigo, así que sin decir nada la coloco sobre sus hombros."

play sound sfx_rustling

show emi basic_shock_gym_close at twoleft
with vpunch

with Pause(0.5)

show emi basic_grin_gym_close
with charachange

"Emi se sobresalta un poco y luego me sonríe."

show emi basic_closedhappy_gym_close
with charachange

emi "Vaya, ¡gracias!"

show emi sad_grin_gym_close
with charachange

emi "Supongo que se está poniendo algo frío."

hi "Sí, eso parece."

"Justo cuando empiezo a preguntarme si darle mi abrigo a Emi podría ser malinterpretado, un chico con el uniforme de atletismo se acerca."

"Compañero" "¡Oye, Emi! ¡Te vas a perder la ceremonia de premiación!"

show emi basic_closedgrin_gym_close
with charachange

emi "¡Oh, sí, gracias!"

show emi basic_grin_gym
show rin basic_awayabsent
with charadistant

"Ella se vuelve hacia Rin y hacia mí."

emi "No tienen que quedarse aquí para esta parte. Dura una eternidad."

show emi basic_closedgrin_gym
with charachange

emi "Además, deberías ponerte a hacer tu tarea ahora si no quieres estar despierto hasta tarde, Hisao."

show emi excited_proud_gym
with charachange

emi "¡Carrera mañana por la mañana! ¡No lo olvides!"

show rin basic_absent
with charachange

hi "¿Cómo podría?"

show emi basic_closedhappy_gym
show rin basic_awayabsent
with charachange

emi "Buen punto. Digo, es pasar tiempo {b}conmigo{/b}, después de todo."

play sound sfx_emirunning

hide emi
with easeoutleft

stop sound fadeout 3.0

show bg school_track_on at center
show crowd at center
show rin basic_awayabsent at center
with charamove

"Con esto, se despide rápidamente y se apresura para recibir sus medallas, o lo que sea que hagan pasar por una medalla estos días."

scene bg school_courtyard
show crowd
show rin relaxed_nonchalant at center
with locationskip

stop music fadeout 7.0

"Rin y yo nos alejamos de la pista, Rin permaneciendo absorta en sus pensamientos por el resto del camino hacia su dormitorio."

"Mientras me despido, ella habla."

show rin basic_deadpan
with charachange

rin "Creo que es probable que no recuperes esa chaqueta."

hi "Estoy seguro de que eventualmente la recuperaré."

show rin basic_deadpannormal
with charachange

rin "Interesante. Tomarlo como venga, ¿eh?"

show rin basic_deadpandelight
with charachange


rin "Algo muy típico de Emi."

hide rin
with charaexit

"Con esta extraña declaración, se da vuelta y camina hacia el edificio."

"En serio, ¿tan importante era?"

"Emi tenía frío y, a menos de que me equivoque, dolor."

"Darle una solución para al menos uno de esos problemas parecía una reacción obvia."

"Aunque supongo que hay una posibilidad de perder mi chaqueta si Emi nunca recuerda regresarla."

"Supongo que Rin tiene razón."

"Aun así, no soy capaz de reunir la suficiente preocupación por todo este asunto."

"Después de todo, ha estado más cálido últimamente."

"No necesito una chaqueta."

"Extraño. Creo que solía ser más responsable con mis cosas."

"“Muy típico de Emi”, ¿eh?"

"Tal vez no sea algo tan malo."

stop ambient fadeout 2.0

scene black
with dissolve


label es_E9:

scene bg school_nurseoffice
show nurse concern at center
with locationchange

nk "No has estado olvidando tomar tus medicinas, ¿verdad?"

play music music_nurse fadein 0.5

nk "Escucho un pequeño murmullo."

nk "Deberías tomarlo con calma por unos días."

"Las palabras del enfermero me hieren más de lo que el cansancio de las carreras podría hacerlo jamás."

"¿Tomarlo con calma por unos días?"

"Sabía que debía quedarme callado."

"Mantengo los ojos en el piso, sintiéndome como un completo idiota."

"Por supuesto que no he recordado tomar mi medicina."

"He tenido que salir apresuradamente de mi habitación para llegar a la pista antes que Emi."

"Después de la competencia de atletismo hace unos días, me sentí… inspirado."

"Así que he estado corriendo algunas vueltas de calentamiento por las mañanas antes de que Emi llegue."

"Pero hoy cuando corríamos, sentí un pequeño dolor en el pecho."

"Fue muy leve, y solo duró un segundo, así que se lo mencioné al enfermero."

hi "Honestamente, no fue tan malo."

hi "Quiero decir, seguí corriendo y terminé sin problemas, así que realmente no puede haber sido tan malo…"

"¿Por qué siento como si le estuviera dando excusas al enfermero?"

"Es más, ¿por qué siento la necesidad de justificar el haber continuado corriendo a pesar del dolor?"

"En realidad, todo se debe a mi renuencia de preocupar a Emi, quien se veía preocupada de todos modos."

"No estoy seguro de cómo se enteró de que algo andaba mal, pero dice que tropecé levemente."

"Ella fue la que insistió en que se lo dijera al enfermero, así que ahora me siento mal por haberla preocupado."

"El enfermero sacude su cabeza tristemente mientras Emi aguarda afuera del cuarto."

nk "Hisao, sé que es difícil para ti adaptarte a una nueva rutina, pero si no quieres terminar con un montón de problemas tendrás que esforzarte más."

nk "No puedes permitirte olvidar tus píldoras, y no puedes exigirte más de la cuenta."

hi "Pero si no me exijo, ¿cómo voy a mejorar?"

"No sé de dónde vino eso."

"El enfermero parece tener una idea."

show nurse fabulous
with charachange

nk "Vaya, ¿dónde he escuchado eso antes?"

show nurse grin
with charachange

"Se ríe y me da unas palmadas en el hombro."

nk "¡Ja! Supongo que ella te está contagiando."

show nurse concern
with charachange

"Su expresión vuelve a cambiar, y está de vuelta en su modo serio."

nk "Mira, no digo que no debas esforzarte."

nk "Pero eso no significa que no debes tomar tu medicina, y tampoco significa que no debes detenerte si tu pecho empieza a molestarte."

nk "Preferiría no tener algún caso fatal mientras trabajo aquí."

show nurse neutral
with charachange

nk "Un objetivo algo sublime, a decir verdad, pero siempre estoy dispuesto a aceptar un desafío."

"Detesto admitirlo, pero creo que tiene razón."

"Debo recordar tomar mis medicamentos."


hi "Tienes razón. Lamento haberte preocupado."

show nurse fabulous
with charachange

nk "¿Quién está preocupado? Eres un chico inteligente, ¿cierto?"

show nurse neutral
with charachange

nk "Sé que puedes ser responsable, Hisao. En una situación como la tuya, debes aprender a ser responsable con rapidez."

hi "Lo sé, lo sé."

"Repentinamente su expresión se torna sinuosa."

show nurse fabulous
with charachange

nk "Entonces, supongo que has empezado a disfrutar tus carreras con Emi, ¿eh?"

hi "Sí, realmente me han estado ayudando."

hi "Digo, hasta hoy me estaba sintiendo mucho más saludable."

hi "Además es realmente impresionante ver a Emi correr. ¿La viste en la competencia de atletismo?"

hi "¡Estuvo increíble!"

show nurse grin
with charachange

"El enfermero asiente, sin dejar de sonreír."

nk "Lo estuvo, Hisao. Vi sus primeras dos carreras antes de que tuviera que encargarme de unos asuntos, pero ella me lo contó todo."

show nurse fabulous
with charachange

nk "Muy amable de tu parte haberle prestado la chaqueta, por cierto."

hi "¿Eh? Oh, sí, no fue nada."

"Honestamente me había olvidado de eso. Aún no la he recuperado."

show nurse neutral
with charachange

"El enfermero sonríe de una manera que me hace sentir como si él acabara de hacer un chiste."

nk "No para ti, pero Emi realmente lo apreció."

nk "Y sé que aprecia que corras con ella en las mañanas."

"Esto me toma un poco desprevenido. Cierto, ella mencionó que es más fácil seguir una rutina con otra persona, pero para nada pensé que le estuviera haciendo un favor."

hi "Pensé que ella me hacía a mí el favor de ayudarme a seguir las órdenes del doctor."

nk "Ella se esfuerza más cuando tú estás cerca."

nk "Si hay otra persona corriendo con ella, se esforzará aún más."

nk "Y ella se esfuerza todavía más cuando eres tú porque, bueno, eres tú."

hi "¿Qué diablos significa eso?"

show nurse grin
with charachange

nk "Jojo, te encantaría saberlo, ¿no?"

"Se ríe al estilo de los malvados megalómanos."

show nurse neutral
with charachange

nk "No, en serio, es porque eres su amigo."

nk "Si Rin corriera con ella, seguro que haría lo mismo."

nk "Bueno, probablemente."

nk "Pero ese no es el punto."

nk "El punto es que la estás ayudando, aunque no sepas que lo haces."

show nurse fabulous
with charachange

nk "Y ella está agradecida por ello, aunque nunca lo mencione."

hi "¿A qué te refieres con, “aunque nunca lo mencione”?"

show nurse neutral
with charachange

nk "Emi no habla demasiado, pero nos conocemos lo suficiente como para que yo sea capaz de entenderla la mayor parte del tiempo."

"Lo admito. No tengo ni idea de qué está hablando."

"Para mí, Emi siempre parece muy parlanchina."

hi "Ya veo."


"De repente el enfermero se da cuenta de que ha estado hablando de más y se calla, viéndose algo avergonzado."

show nurse fabulous
with charachange

nk "De todas formas, no tienes que dejar tu ejercicio por las mañanas."

show nurse neutral
with charachange

nk "Solo camina por la pista en lugar de correr por unos cuantos días. Deja que las cosas se calmen."

show nurse concern
with charachange

nk "¡Y toma tu condenada medicina!"

scene bg school_nursehall
with locationchange

stop music fadeout 0.3
play sound sfx_impact

show emi basic_confused_gym_close
with vpunch

"Me río mientras salgo de la oficina, chocando directamente con Emi."

show emi basic_confused_gym
with charadistant

hi "Ups, perdón por eso."

show emi basic_hes_gym
with charachange

emi "¿Estás bien? ¿Qué dijo el enfermero?"

emi "¿Necesitas ir a un hospital?"

show emi basic_shock_gym
with charachange

emi "Ay diosito, fue mi culpa, ¿no es cierto?"

show emi basic_closedsweat_gym
with charachange

emi "Te he estado exigiendo demasiado, ¿verdad?"

show emi excited_sad_gym
with charachange

emi "¡Soy una persona horrible!"

"Las palabras salen como un torrente. Está realmente agitada."

"No esperaba que estuviera tan preocupada por mí, para ser honesto."

"Debo calmarla… ¿pero cómo diablos hago eso?"

"Hago lo único que se me ocurre."

show emi basic_shock_gym_close
with characlose

play music music_serene fadein 6.0

"Le doy un abrazo. Emi se tensa un poco, así que le doy unas palmaditas en la cabeza en lo que espero sea una manera tranquilizadora."

hi "¡Oye, cálmate un poco!"

hi "Estoy bien, ¿de acuerdo? No te preocupes."

show emi basic_hes_gym_close
with charachange

"Puedo sentir el cuerpo de Emi relajarse mientras continúo asegurándole que estoy bien."

"Sus brazos se cierran en torno a mí, como si intentara confirmar que no estoy a punto de caer muerto."

"Alcanzo a oler su cabello. Huele a sudor, o como la adrenalina debería oler. Es la esencia de la actividad."

"Y un poco de fresas. De su champú, me imagino."

hi "Solo debo recordar tomar mi medicina, eso es todo."

hi "No te preocupes por eso. No es tu culpa."

show emi sad_depressed_gym_close
with charachange

emi "¿Estás seguro?"

"Su voz suena amortiguada, principalmente porque en este momento su cara está presionada contra mi pecho."

hi "Sí, estoy seguro. Solo debo tomarlo con calma por algunos días."

"De repente me doy cuenta de lo cerca que estamos los dos."

"También me doy cuenta de lo bien que se siente estar así de cerca."

"Puedo sentir los latidos de su corazón calmarse, y debo resistir el impulso de descansar mi barbilla en lo alto de su cabeza."

show emi sad_grin_gym_close
with charachange

emi "Gracias al cielo."

emi "Realmente me tenías preocupada, Hisao."

stop music fadeout 1.5

show nurse concern behind emi:
    center
    xpos 0.0 xanchor 0.3
    easein 0.5 xanchor 0.2
with Dissolve(0.5)

nk "Emi, ¿piensas entrar algún día?"

show nurse grin
with charachange

nk "… Oh, lo siento. ¿Interrumpo algo?"

show emi basic_shock_gym
with vpunch

"Los dos nos separamos como si el otro acabara de prenderse en llamas."

show emi basic_hes_gym
with charachange

"Emi se acomoda el cabello hacia atrás nerviosamente y se ríe."

play music music_emi fadein 1.0

emi "¡Claro que no!"

show emi sad_shy_gym
show nurse fabulous
with charachange

emi "Yo eh… te veré luego, ¿de acuerdo?"

show emi basic_closedgrin_gym
with charachange

emi "Oh, ¿Hisao?"

hi "¿Hmm?"

show emi basic_annoyed_gym_close
with characlose

with hpunch

emi "¡Toma tu maldita medicina!"

"Esta última frase es puntuada con un golpe en el hombro."

hi "Sí, sí, lo recordaré."

hi "Te veo luego."

show nurse grin
with charachange

"El enfermero me sonríe de nuevo como si bromeara con algo que no entiendo y se despide de mí mientras me dirijo a mi habitación, sintiendo un ardor en las mejillas."

stop music fadeout 8.0

scene bg school_dormhisao
with locationskip

"Necesito una ducha."

"Una fría, si los pensamientos que ahora recorren mi cabeza son un indicio."

"Ella era realmente suave."

"Mis píldoras esperan por mí cuando entro a mi habitación."

"Me las trago sin pensarlo dos veces."

"No sé por qué no pensé en esperar hasta después de las carreras para tomarlas. Por alguna razón se me ocurrió que era cuando despertaba, nada más."

"Pero no, solo deben ser ingeridas cada veinticuatro horas. La hora exacta del día no importa."

"Mis pensamientos regresan al abrazo en el corredor."

"Es extraño, esperarías que alguien huela mal después de una carrera, pero por alguna razón, Emi olía… bien. Ese matiz de sudor parecía simplemente encajar con ella."

"Realmente necesito esa ducha."

scene black
with dissolve

$ suppress_window_after_timeskip = True


label es_E10:

window hide None

scene bg school_roof
with locationchange

nvl clear

nvl show dissolve

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 1.0

n "\n\nEs extraño que se sienta tan natural ir a la azotea estos días."

n "Nunca habría hecho tal cosa en mi vieja escuela."

n "En esos días me gustaba comer solo… no, eso no es totalmente cierto. A pesar de que me gustaba sentarme solo, también me gustaba ver a la gente."

n "Siempre pensé que yo era de ese tipo de persona, pero al parecer estaba equivocado."

n "Por otra parte, también pensaba que era del tipo de persona que tenía un corazón normal, así que ahí lo tienes."

n "No me conozco tan bien."

n "Ahora estoy en la azotea para almorzar con un par de personas."


n "Y ambas son chicas, lo cual es aún más raro."

n "Por extraño que parezca, me siento más cercano a Emi y a Rin de lo que me sentía a cualquier otra persona en mi vieja escuela."

n "Por algún motivo tengo la sensación de que al menos me visitarían si yo terminara en el hospital."

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

nvl hide dissolve

nvl clear

window show

"Me concentro en la vista desde la azotea, desterrando tales pensamientos de mi cabeza."

"Sopla una ligera brisa, y el sol brilla alto en el cielo."

"El cielo es de un azul profundo, casi sin ninguna nube. Se ha vuelto placenteramente cálido, y mientras espero por mis amigas cierro los ojos y disfruto de la sensación del sol atravesando mi piel."

$ renpy.music.set_volume(0.1, 2.0, channel="ambient")

window hide

scene black
with shuteye

with Pause(4.0)

window show


"Voces invaden mi mente desde los bordes de la percepción."

emi "—parece que se nos quedó dormido, Rin."

rin "Tal vez está fingiendo, para inspirarnos una falsa sensación de seguridad."

emi "¿Por qué haría eso?"

rin "Ni idea."

emi "Aun así, es un buen punto."

emi "Deberíamos patearlo o algo para asegurarnos de que realmente esté dormido."

stop music fadeout 1.0

hi "¿Eh? ¿Qué?"

$ renpy.music.set_volume(0.5, 5.0, channel="ambient")

scene bg school_roof
show rin basic_absent at tworight
show emi excited_happy_close at twoleft
with openeye

play music music_ease fadein 3.0

"Emi se cierne sobre mí como solo una chica pequeña puede, mirándome con atención."

show emi basic_closedgrin_close
with charachange

emi "Oh, estás despierto. Supongo que ya no tendremos que patearte."

show rin basic_deadpan
with charachange

rin "¿Era eso parte de tu plan maestro?"

hi "¿De qué estás hablando?"

show emi basic_grin_close
with charachange

"Emi se encoge de hombros, sus coletas balanceándose con el movimiento."

show emi basic_closedhappy_close
with charachange

emi "Yo tampoco estoy segura."

show emi sad_grin_close
with charachange

emi "Debes de estar bastante cansado para quedarte dormido aquí."

show emi basic_closedgrin_close
with charachange

emi "Aunque es bastante cómodo, supongo."

show emi basic_closedgrin_close:
    yanchor 0.9
with ease
with vpunch

"Ella se deja caer junto a mí y empieza a comer."

show rin basic_absent
with charachange

show rin basic_absent:
    yanchor 0.77
with charamove

"Rin se sienta frente a nosotros, un movimiento que solo me hace más consciente de la chica sentada junto a mí."

"Si no la conociera mejor, diría que Rin lo hizo a propósito."

"Me concentro en mi comida, intentando desconectarme de la mayoría de la conversación que están teniendo Rin y Emi."

"Aun así, y a pesar de mis esfuerzos, me encuentro lanzando miradas hacia Emi cada vez que habla."

show emi basic_grin_close
with charachange

"Noto cómo frunce los labios cuando está pensando en algo, entrecerrando los ojos un poco como si eso fuera a mejorar su capacidad de razonamiento."

show rin basic_deadpan
with charachange

show emi basic_grin_close at Transform(function=tf_leftrock)
with None

show emi basic_closedhappy_close at Transform(function=tf_leftrock)
with charachange

"Rin dice algo que hace reír a Emi, y noto, quizá por primera vez, cómo se ríe con todo su cuerpo, meciéndose hacia adelante y hacia atrás, con la cabeza echada hacia atrás, casi como si estuviera a punto de caerse."

"Probablemente me veo como un acosador."

show emi basic_confused_close
with charachange

"Es hasta este momento cuando me doy cuenta de que Emi me está mirando. Elevó un poco la voz, así que probablemente acaba de preguntarme algo."

hi "¿Eh? Perdón, me distraje un poco por un momento."

show rin basic_deadpannormal
show emi basic_annoyed_close
with charachange


"Emi pone los ojos en blanco, mientras que un leve movimiento de una ceja es la única señal de que Rin está siquiera poniendo atención."


emi "Dije, ¿también te dieron un cuestionario de orientación profesional en tu clase?"

show emi basic_grin_close
with charachange


emi "Ya sabes, una de esas cosas tipo “¿Qué quieres hacer después de la secundaria?”."

hi "No… lo creo. Tal vez nos den uno mañana."

show emi excited_happy_close
with charachange

emi "¿Qué vas a poner?"

"Esa es una muy buena pregunta."

"Supongo que siempre pensé en ir a la universidad luego de la secundaria, pero no tengo idea de lo que haría una vez llegue ahí."

"Y con el ataque al corazón y todo, en realidad he estado concentrándome en cada día a como venga en vez de hacer planes a largo plazo."

"Supongo que puedo empezar a planificar a futuro con seguridad, de nuevo."

"Siempre me ha gustado tener por lo menos un leve plan para mi futuro, así que será bueno idear uno de nuevo."

"Por supuesto, eso no cambia el hecho de que justo ahora no tengo absolutamente…"

hi "… Ni idea."

hi "Siempre asumí que lo averiguaría en la universidad. Eso o simplemente ser un asalariado. Eso es bastante popular."

"¿Pero en serio quiero serlo? Esa es una pregunta difícil."

"Supongo que en realidad no quiero hacer nada."

show emi basic_closedhappy_close
with charachange

emi "No suenas muy emocionado por esto, ¿verdad?"

show emi basic_closedhappy_close at Transform(function=tf_leftrock)
with None

"Se ríe cuando dice esto, y su risa me cautiva de nuevo."

"Es tan… femenina. Aguda y risueña, como… bueno, perdón por el cliché, como el murmullo de un arroyo."

"Brota fuera de ella, empezando en su vientre y subiendo hasta su garganta."

"No puedo evitar reírme, es contagioso."

hi "Sí, supongo que no estoy muy feliz con la idea del asalariado."

hi "Pero para ser honesto, no le he dedicado mucha reflexión al futuro recientemente."

hi "Supongo que, estos días, he estado más preocupado en vivir un día a la vez."

show emi basic_grin_close
with charachange

"Emi considera esto por un momento y sonríe."

emi "¡Esa es una muy buena idea, Hisao!"

show emi excited_proud_close
with charachange

emi "Yo simplemente escribí, “Pirata”."

"Quedo aturdido por un momento, luego empiezo a reír."

"Me detengo y me las arreglo para balbucear una pregunta."

hi "No hablas… no hablas en serio, ¿verdad?"

show emi sad_annoyed_close
with charachange

"Emi finge estar ofendida."

emi "Bueno ya tengo las piernas para eso, así que se me ocurrió…"

show rin basic_amused
with charachange

"Hasta Rin parece divertirse con esto."

show emi basic_annoyed_close
with charachange

emi "Solo esperen, ¡seré el terror del ancho mar!"

emi "¡Les mostraré a todos!"

show emi basic_closedhappy_close
with charachange

emi "¡He estado trabajando en mi voz de pirata!"

show emi basic_closedhappy_close at offscreenleft
with ease

hide emi
with None

show emi basic_closedhappy at offscreenleft behind rin
with None

show emi basic_annoyed at left
with ease

"Súbitamente se levanta y empieza a gritar órdenes con voz fanfarrona."

show emi basic_annoyed at center
with ease


emi "¡Arr, grumetes, disparen a sus costados con las bombardas hasta que encallen!"

show emi basic_annoyed at twoleft
with ease


emi "¡Usaremos sus entrañas como ligueros!"

show rin basic_deadpanamused
with charachange

rin "¿Por lo menos sabes qué significa eso?"

show emi basic_confused
with charachange

"La inesperada interrupción de Rin detiene a Emi en seco."

show emi sad_shy
with charachange

emi "En realidad no."

show emi basic_closedgrin
with charachange

emi "¡Pero es la presentación lo que importa!"

play sound sfx_warningbell

show emi basic_hes
show rin basic_awayabsent
with charachange


"El sonido de la campana evita que siga demostrando sus ideas."

hide emi
with easeoutleft

"Emi se retira inmediatamente, dejándonos a Rin y a mí solos en la azotea."

show rin basic_awayabsent:
    xpos 0.5
show bg school_roof at bgleft
with charamove

show rin basic_deadpancontemplation
with charachange

"Rin me mira intensamente por unos segundos."

hi "¿Pasa… algo malo?"

show rin basic_lucid
with charachange

"Rin considera esta pregunta minuciosamente por un momento."

"Luego de una larga pausa, sacude la cabeza."

show rin basic_deadpannormal
with charachange

rin "Nop."

hi "Oh, eh…"

extend " entonces, ¿por qué la mirada?"

show rin basic_awayabsent
with charachange

"Rin sacude la cabeza de nuevo."

rin "Nop, no lo entiendo."

hi "¿Entender qué?"

show rin basic_deadpan
with charachange

rin "El asunto de las miradas. Ustedes dos parecen hacerlo, pero yo no."

"Genial. Me vio mirando. Ahora probablemente pensará que soy un pervertido o algo así."

"De hecho, probablemente no. Es Rin de quien estamos hablando, después de todo."

"Aun así, siento la necesidad de defenderme."

hi "No estaba mirando, solo estaba cansado."

show rin basic_deadpancontemplation
with charachange

"Hasta Rin resopla con esto, pero no dice nada."

hi "¡No, en serio! Solo estaba… distraído, es todo."

show rin basic_lucid
with charachange

rin "Mmm."

stop music fadeout 4.0

"Ansioso por terminar esta conversación, me dirijo de vuelta a clase."

stop ambient fadeout 2.0

scene bg school_scienceroom
show misha cross_grin at twoleft
show shizu behind_blank at tworight
with locationskip

"Soy recibido por los espectros gemelos de Shizune y Misha, quienes parecen significar trabajo."

"Bueno, Shizune parece significar trabajo, a fin de cuentas."

"Misha simplemente parece estar a punto de soltar una carcajada en cualquier instante."

play music music_shizune fadein 3.0

show misha perky_smile
with charachange

mi "¿En la azotea de nuevo, Hicchan?"

show misha hips_frown
with charachange

mi "Sabes que eso es peligroso, ¿verdad~?"

show shizu basic_angry
with charachange

shi "…"

show misha sign_smile
with charachange

mi "¡Eso es cierto~!"

show misha hips_smile
with charachange

mi "¡La escuela no puede hacerse cargo de ninguna lesión provocada por estar allá arriba, sabes!"

show misha cross_frown
with charachange

mi "Además, ¡podríamos reportarte por romper las reglas~!"

show misha cross_frown_close
with characlose


"Misha se acerca y susurra conspiratoriamente."

show misha sign_smile_close
show shizu behind_smile
with charachange

mi "¡Pero no lo haremos, Hicchan!"

show misha hips_grin_close
with charachange

mi "¡Ustedes tres son demasiado lindos juntos~!"

show misha cross_laugh
with charadistant

"Se aleja de nuevo, riéndose de mi repentino sonrojo."

mi "¡Guajajaja~!"

show misha cross_grin
with charachange

mi "¡Es tan fácil molestarte, Hicchan~!"

hi "Oye, vamos."

hi "Aún soy nuevo aquí, o algo así."

hi "¿No es malvado recibir así a los recién llegados?"

show misha hips_grin
with charachange

mi "¡Nop~!"

show misha sign_smile
with charachange

mi "¡Es una ayuda para que te adaptes a tu nuevo entorno!"

hi "Ah, ya veo."

hi "Bueno… ¿tienes que ser tan entusiasta con eso?"

show misha hips_grin
with charachange

mi "¡Síp!"

show misha hips_smile
with charachange

mi "¡Ah! Dejando eso de lado, Hicchan, ¡te buscábamos esta mañana, pero no estabas en tu habitación!"

hi "Claro que no. Estaba fuera por mi ejercicio matutino, o aquí en clase, muy temprano."

hi "A diferencia de ustedes."

show shizu basic_angry
show misha hips_frown
with charachange

"Shizune se ve furiosa, y un poco después, también Misha. O al menos lo intenta."

mi "¡Eso fue por culpa del trabajo del consejo estudiantil! ¡Deberías estar agradecido de que trabajemos tan duro por ti~!"

hi "Oh, lo estoy, lo estoy. ¿Entonces para qué me necesitaban?"

"No otro intento de involucrarme en su sucio trabajo, espero."

show misha sign_smile
with charachange

mi "Teníamos que darte algo~ pero ya que no estabas, ¡lo dejamos en tu habitación!"

hi "¿Algo? ¿Como qué?"

show misha hips_grin
with charachange

mi "Oh, ¡te darás cuenta cuando regreses, Hicchan~! ¡Guajajaja~!"

hide misha
hide shizu
with charaexit


"Mutou entra en el salón finalizando nuestra charla, y todos nos dirigimos a nuestros asientos."

stop music fadeout 10.0

"Es hasta después de haberme sentado en mi pupitre y de que el maestro ha empezado a hablar acerca de algún tema que me percato de algo extraño."

"¿A qué se refería Rin con, “Ustedes dos parecen hacerlo”?"

"¿Emi también estaba mirando algo?"

"Por un breve momento, considero la posibilidad de que Emi estuviera mirándome de la manera en que yo la miraba."

"Eso, por supuesto, es ridículo."

"Pero no puedo negar que no me molestaría si fuese verdad…"

"Pero es mejor no pensar en eso. No hace falta avivar mis esperanzas."

"Ahora que lo pienso, ¿cuándo empecé a tener esas esperanzas?"

"Sacudo mi cabeza en un intento de aclararla, y me concentro en la lección."

scene bg school_dormhallway
with shorttimeskip

"Luego de clases, me encamino a mi habitación. Mutou realmente amontonó la tarea hoy."

play sound sfx_impact2

show kenji tsun at left
with vpunch

"Aun así, antes de que pueda abrir mi puerta, soy interceptado repentinamente por Kenji, quien acaba de irrumpir fuera de su habitación en un aluvión de papeles."

ke "Oye, necesitamos hablar."

play music music_kenji fadein 1.0

ke "Esa farsa de la azotea, hombre."

ke "Tiene que parar."

hi "¿Qué?"

ke "¡Tu vaivén en la azotea con las maravillas sin extremidades!"

ke "¡Son mujeres, hombre! ¡Vas a terminar muerto si haces tonterías como esas!"

hi "No entiendo."

show kenji neutral
with charachange

"Kenji suspira y se ajusta los anteojos, antes de lo que podría ser interpretado como un intento de explicarse pacientemente."

ke "Mira, somos amigos así que te digo esto por tu propio bien."

ke "Pero si yo fuera a matar a alguien, lo haría arrojándolo por la azotea y haciéndolo parecer un accidente."

show kenji tsun
with charachange

ke "Y si yo pensé en ello, puedes estar seguro de que ellas lo pensaron también."

ke "Son astutas, casi tan astutas como yo."

hi "Ya veo."

show kenji happy
with charachange

ke "¡Bien!"

ke "Me alegra que tuviéramos esta charla."

show kenji neutral
with charachange

ke "Préstame 500 yenes."

hi "… ¿Perdón?"

show kenji tsun
with charachange

ke "¡Necesito conseguir una bebida, hombre!"

ke "He estado dentro todo el día y el agua del grifo ha sido comprometida, como estoy seguro de que ya sabrás."

ke "Así que debo abastecerme con algo enlatado, ¿entiendes? Pero para hacer eso necesito 500 yenes."

show kenji neutral
with charachange

ke "Y ya que salvé tu vida con mi oportuno consejo, al menos podrías prestarme 500 yenes."

"Ya saben, si hace que se vaya, 500 yenes es una ganga."

stop music fadeout 6.0

show kenji happy
with charachange

show kenji happy:
    easeout 0.5 alpha 0.0 xanchor 0.2
with None

"Le doy el dinero a Kenji, quien asiente en agradecimiento y se va apresuradamente por el corredor, pero no antes de asegurar su puerta."

"Qué persona tan agotadora. Mejor me voy, antes de que él cambie de parecer."

scene bg school_dormhisao
with locationchange

"¿Hm?"

"Cuando cierro la puerta, mis pies tocan algo que yace en el suelo."

"Es un rectángulo de papel de colores brillantes. Ah, esto debe ser el “algo” que mencionó Misha antes."

"Probablemente un panfleto del consejo estudiantil que deslizó por debajo de la puerta."

"Como sea, cuando lo recojo, me doy cuenta de que no podría haber estado más equivocado."

"Alguien de verdad me envió una carta de papel escrita a mano, a la vieja usanza."

"¿Es más, quién se molesta en hacer algo como eso en esta época? Aun así, por improbable que suene el hecho de recibir una, definitivamente es una carta lo que tengo en mis manos."

"Planeaba terminar mi tarea, comer algo, e irme a la cama y así estar listo para la carrera de mañana por la mañana."

"Sin embargo, la carta naturalmente ha llamado mi atención. Me siento frente al escritorio para examinarla detenidamente."

scene ev hisao_letter_closed:
    xalign 0.5 yalign 0.5 zoom 1.1 subpixel True
    acdc_warp 10.0 zoom 1.0
with locationchange

play music music_rain fadein 5.0

"Es el primer objeto por correo que he recibido aquí en Yamaku, así que se sentiría especial aunque no fuera algo tan raro como una carta escrita a mano."

"Lo que me causa aún más aprensión es el nombre del remitente, escrito cuidadosamente en la parte posterior del sobre."

"“Iwanako”."

"No tengo idea de por qué ella me escribiría. No he estado en contacto con nadie de mi antigua escuela desde que fui transferido, e Iwanako es la última persona de quien esperaría el gesto de escribirme una carta."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\n\n\n\nLa última vez que vi a Iwanako fue terriblemente incómodo; hasta vergonzoso. Ella vino a mi cuarto del hospital, me peló una manzana por cortesía y luego prácticamente permanecimos en silencio por media hora."

n "Ella dijo “adiós” y no me miró a los ojos cuando cerró la puerta."

n "Podría haber sido un final natural a la serie de visitas que probablemente resultaron muy dolorosas para nosotros dos."


n "Siempre que me visitaba en el hospital quería hablarle, pero algo me detenía cada vez."

n "Cada vez que callaba hacía la siguiente ocasión aún más difícil."

nvl clear

n "\n\n\n\nSe veía tan llena de remordimiento que no quería decir nada que pudiera molestarla, y nunca pude encontrar las palabras correctas."

n "Creo que Iwanako se culpaba a sí misma por mi ataque al corazón. Eso es ridículo, por supuesto, pero saberlo y creerlo son dos cosas muy distintas."

n "Le dije que no había sido su culpa, ella asintió y realmente creí que había entendido que de no ser por eso, tarde o temprano algo más habría provocado que mi corazón fallara."

n "Aun así ella se veía tan desesperanzadamente triste cada vez que abría esa puerta y entraba a mi cuarto."

n "Así que nunca fui capaz de decirle las cosas que le quería decir. Al final, eso puede haberla herido aún más."

$ renpy.music.set_volume(1.0, 2.0, channel="music")

nvl hide dissolve
nvl clear

scene ev hisao_letter_open
with locationchange

window show

"Con cuidado, abro el sobre y saco la carta doblada de adentro."

window hide

$ written_note("Querido Hisao,\n\n¿Cómo estás? Espero que estés bien y feliz en tu nueva escuela. Todos aquí te extrañan. Casi todo nuestro grupo de segundo año fue colocado junto en el grupo 3-1 para el último año, así que hemos estado bastante cómodos desde el principio. Estoy segura de que habrías sido asignado a este, también.")

$ written_note("Los ánimos entre los de tercer año parecen ser de muchas ansias por los exámenes finales, aun estando tan lejos. Los maestros nos fastidian por ello todo el tiempo, incluso el viejo señor Tachibana quien es, por cierto, nuestro maestro de cabecera este año. ¿Podrías creerlo? Estaba segura de que se retiraría después de nuestro segundo año, pero aquí está, dándonos lata a todos para que estudiemos para los exámenes.\n")

$ written_note("Creo que cosas como esa son la principal razón de que los ánimos entre los de tercero sean de tanto nerviosismo. Debo admitir que de algún modo también estoy perdiendo confianza en mí misma, a pesar de que siempre me ha ido razonablemente bien en los exámenes.\n\n\n\n\n")

$ written_note("Es tan extraño pensar que ya estamos en el último año, ¿no es así? El tiempo realmente ha pasado volando. Me pregunto adónde fue. Los nuevos de primer año parecen tan jóvenes y de algún modo tan inocentes. No dejo de preguntarme si yo era como ellos en mi primer año. He estado sintiéndome así de nostálgica durante todo el primer trimestre.\n\n\n")

$ written_note("Hay otras cosas que quiero decir. Te estoy escribiendo porque sentí que hay cosas que debería haber dicho después del incidente en aquel invierno. Realmente me arrepiento de no haber sido capaz de decirlas en persona, y no tengo excusa para ello.\n\n\n\n\n")

window show

"Sí, creo que ya he tenido suficiente de esto."

scene bg school_dormhisao
with locationchange

"Arrugo la hoja de papel y la arrojo a través de la habitación. Mi pulso falla, así que la carta rueda bajo mi mesita de noche en vez de caer en la papelera."

"Esa fue una disculpa por abandonarme. Excepto que, a estas alturas, ya no sé si realmente la necesito."

"Lo del hospital parece haber sido hace una vida atrás, y aquí, ahora, tengo otras cosas en mente."

stop music fadeout 8.0

"Emi, para empezar."

"No fue agradable ser abandonado durante mi estadía, pero no es algo por lo que me siga preocupando."

"De hecho, ni siquiera había pensado en el hospital por lo que se siente como una eternidad hasta que esta carta llegó. Es casi una molestia haberla recibido."

"Yo también tengo exámenes por los que estudiar. No tengo tiempo para el pasado."

"Ahora, sobre aquella tarea…"

scene black
with dissolve



label es_E11a:

scene black
with None

hi "De todas formas, ¿cuál es el plan para hoy?"

play music music_daily fadein 1.0

scene bg school_girlsdormhall
with dissolve

"Estoy esperando pacientemente en el corredor del dormitorio de las chicas justo afuera de las habitaciones de Emi y Rin."

"Al parecer Emi está ayudando a Rin a vestirse."

"Supongo que tiene perfecto sentido, ya que no tengo idea de cómo se vestiría Rin de otra manera."

emi "¡Picnic!"

hi "¿Picnic?"

emi "¡Eso es lo que dije!"

hi "Suena muy emocionante."

emi "Lo sé, ¿verdad?"

"Rin elige este momento para hacer una observación."

rin "Hoy el cielo se ve amenazador."


"En realidad, también noté eso, mientras venía de camino. A pesar del sol de la mañana, la tarde parece haber tomado su lugar con tristeza."

"También hay cierta pesadez en el aire, lo cual usualmente anuncia una tormenta."

"Me pregunto si debería de haber traído un paraguas…"

hi "Ella tiene razón."

hi "Emi, ¿segura de que aún quieres arriesgarte a que te atrape la lluvia?"

"Ni siquiera sé por qué me molesté en preguntar."

show emi basic_shock:
    center
    xpos 0.9
    easein 0.5 xpos 0.7
with charaenter

"Emi sale de la habitación de Rin hacia el pasillo viéndose sorprendida de que yo haya siquiera insinuado cancelar nuestros planes."

emi "¡Por supuesto!"

show emi basic_annoyed
with charachange

emi "¿Qué? ¿Se supone que la amenaza de la lluvia me detenga?"

"No puedo hacer más que sonreír a su beligerante respuesta. Es casi como si retara a la lluvia a caer."

"Si la Madre Naturaleza estuviera caminando por la calle, creo que Emi probablemente empezaría una pelea con ella."

"O al menos la retaría a una carrera."

"De hecho, Emi se ve casi agresivamente animada el día de hoy."

show rin basic_absent:
    center
    xpos 0.9 alpha 0.0
    ease 1.0 xpos 0.7 alpha 1.0
show emi basic_annoyed at twoleft
show bg school_girlsdormhall at bgleft
with charamove

"Rin sale al corredor, viéndose igual que siempre."

hi "Pues bien, ¿estamos listos para partir?"

show emi basic_closedhappy
with charachange

emi "¡Yo lo estoy!"

show rin basic_deadpannormal:
    tworight alpha 1.0
with charachange

"Rin asiente y dice una sola palabra."

show rin basic_deadpan
with charachange

rin "Cesta."

hi "¿Disculpa?"

show rin basic_deadpannormal
with charachange

rin "La cesta. En el cuarto de Emi. Deberías llevarla."

show emi basic_hes
with charachange

"Emi se lleva las manos a la boca, avergonzada."

show emi basic_closedsweat
with charachange

emi "¡Ay diosito! ¡Casi me olvido de eso! ¡Justo a tiempo, Rin!"

show emi basic_closedsweat at offscreenleft
with ease

with Pause(0.3)

show emi basic_closedgrin at twoleft
with ease

"Emi se apresura a entrar en su habitación y sale con lo que parece una muy bien surtida cesta de picnic."

with vpunch

"Cuando me la pasa, también noto que se siente lo suficientemente pesada como para ser una. Por Dios, ¿cuánta comida empacó?"

"… Mejor dicho, ¿de dónde sacó el dinero para todo esto?"

hi "Entonces, ¿estamos listos para partir?"

show emi basic_grin
with charachange

emi "¡Síp!"

show rin basic_awayabsent
with charachange

"Rin asiente de nuevo, y nos dirigimos afuera de los dormitorios."

scene bg school_courtyard_rn
with locationskip

"No puedo evitar fruncir el ceño cuando noto lo gris que se ha puesto el cielo en los diez minutos que estuve adentro."

"Sin embargo, Emi no parece preocupada por cosas tan triviales como el color del cielo. Ella da saltitos con seguridad mientras caminamos."

"Lo que me recuerda…"

hi "¿Adónde vamos?"

"Esto detiene a Emi en seco y ella me lanza una mirada avergonzada."

show emi sad_shy_rn at center
with charaenter

emi "Sabes, realmente no he pensado en eso."

emi "¿Qué piensas tú, Hisao?"

"Bueno, está el lugar donde comimos durante el festival, pero podría resultar agradable dejar el campus por un rato. Aunque no estoy seguro de si hay algún buen lugar para eso en el pueblo."

"Justo cuando estoy por abrir la boca, Rin interfiere inesperadamente con una sugerencia."

show emi sad_shy_rn at twoleft
show bg school_courtyard_rn at bgleft
with charamove

show rin basic_deadpan_rn at tworight
with charaenter

rin "Hay un parque en el pueblo, cerca de la tienda de arte."

show emi basic_closedhappy_rn
with charachange

emi "¡Gran idea, Rin! ¡Me había olvidado por completo de ese lugar!"

"Crisis evitada."

hi "¿Sabes cómo llegar allí, Rin?"

show rin basic_deadpannormal_rn
with charachange

"Rin se encoge de hombros."

show rin basic_awayabsent_rn
with charachange

rin "Es muy probable."

show emi excited_amused_rn
with charachange

emi "¡Con eso me basta!"

"Preferiría saberlo con certeza… pero, qué demonios."

hi "Guíanos, Rin."

scene bg school_gate_rn
with locationchange

"Los tres nos apresuramos en salir del campus y tomamos la calle que baja al pueblo."

scene bg school_road_rn
with locationchange

"La cesta está algo pesada. Espero que el parque esté cerca."

scene bg suburb_roadcenter_rn
with locationchange

"Pasamos la tienda de artículos de arte, Rin disminuye un poco el ritmo mientras lo hacemos."

"Emi nota el cambio en el ritmo de Rin y se detiene."

show emi basic_grin_rn at twoleft
show rin relaxed_nonchalant_rn at tworight
with charaenter

emi "¿Quieres entrar, Rin?"

show rin basic_awayabsent_rn
with charachange

"Rin se encoge de hombros."

show rin basic_deadpan_rn
with charachange

rin "No necesito nada."

show emi excited_proud_rn
with charachange

emi "¿Estás seguuura?"

show rin basic_delight_rn
with charachange

show rin basic_deadpandelight_rn
with charachange


"Hay un muy leve asomo de sonrisa en el rostro de Rin, reemplazado rápidamente por su expresión usual."

show rin basic_deadpan_rn
with charachange

rin "La vida es impredecible, pero por lo menos estoy bastante segura de eso."

show rin basic_deadpanamused_rn
with charachange

rin "Gracias por la oferta."

show emi basic_closedhappy_rn
with charachange

emi "Bueno, no es como si fuera yo quien lleva la cesta."

show emi basic_grin_rn
with charachange

emi "Pero apuesto a que a Hisao tampoco le habría importado, ¿verdad?"

hi "Oh, claro que no. Esto apenas pesa."

"Flexiono para enfatizar."

show emi excited_laugh_rn
with charachange

"Emi sofoca una risotada señalando el parque al que súbitamente llegamos."

$ renpy.music.set_volume(0.02, 0.0, channel="ambient")
play ambient sfx_rain fadein 15.0

scene bg suburb_park_rn at bgright
with locationchange

emi "¡Oh, recuerdo este lugar!"

show emi basic_closedhappy_rn
with charachange

emi "Me encontré aquí contigo aquella vez, ¿verdad, Rin?"

show emi basic_closedhappy_rn at twoleft
show bg suburb_park_rn
with charamove

show rin basic_deadpannormal_rn at tworight
with charaenter

"Rin levanta ligeramente una ceja."

show rin basic_deadpan_rn
with charachange

rin "Tal vez."

show rin relaxed_boredom_rn
with charachange

rin "No estoy dispuesta a asegurarlo de una manera u otra."

show rin relaxed_nonchalant_rn
with charachange

rin "La memoria es engañosa, sabes."


"Bueno yo sí lo estoy. Llegamos en una sola pieza después de todo."

"El sol todavía no se asoma por ningún lugar, pero ni a Emi ni a Rin parece importarles."

scene ev picnic_normal:
    yalign 1.0 subpixel True
    easein 8.0 yalign 0.0
with whiteout







"Encontramos un lugar para sentarnos en la hierba y dejo la cesta en el suelo agradecido."

"Hay una impresionante cantidad de comida preparada. ¿Tal vez se supone que nos uniéramos con algunos de los compañeros de equipo de Emi o algo así?"




emi "¡Muero de hambre! ¡Empecemos!"

"Ella ataca la comida como si no hubiera tenido nada para comer por años."

stop music fadeout 2.0

play sound sfx_thunder

show ev picnic_rain:
    yalign 0.0
with charachange





$ renpy.music.set_volume(0.2, 0.5, channel="ambient")

show rain light
with dissolve

"Apenas estoy alcanzándome algo de comida cuando siento la primera gota de lluvia caer en la palma de mi mano."

hi "Uh oh."


hi "Parece que el clima no va a cooperar con nosotros, después de todo."

hide ev
show bg suburb_park_rn behind rain
show emi sad_grit_rn behind rain:
    twoleft
    ypos 1.15
show rin basic_absent_rn behind rain:
    tworight
    ypos 1.2
with flash

"Emi lanza una mirada al cielo como si solo con eso fuera a detener a la lluvia."

"Estoy a punto de creer que puede hacerlo. Es una mirada aterradora."

show emi basic_annoyed_rn
with charachange

emi "Más le vale cooperar."

show emi sad_angry_rn
with charachange

emi "¿Me oyes, cielo? ¡Detén esa lluvia en este mismo instante!"

"El cielo no parece inclinado a escucharla, a pesar del tono dominante que ha adoptado contra él."

$ renpy.music.set_volume(0.5, 4.0, channel="ambient")

show rain medium
with dissolve

"En vez de eso, la lluvia parece haber aumentado. Rin arruga la nariz en disgusto por este cambio de eventos."

show rin basic_deadpan_rn
with charachange

rin "Lamentable."

show emi basic_confused_rn
with charachange

emi "¿A qué te refieres?"

show rin basic_deadpannormal_rn
with charachange

"Rin se encoge de hombros."

show rin relaxed_nonchalant_rn
with charachange

rin "Podría pintar esto si no estuviera acá afuera. Una lástima perdérmelo, es todo."

"No se ve enojada o molesta por ello, solo un poco decepcionada."

show emi basic_closedhappy_rn
with charachange

"Emi se ríe en respuesta al comentario de Rin."

show emi basic_grin_rn
with charachange

emi "Supongo que deberíamos haber parado en esa tienda de artículos de arte después de todo, ¿eh?"

$ renpy.music.set_volume(1.0, 6.0, channel="ambient")

show rain normal
with dissolve

"La lluvia aumenta un poco más, ofendida porque aún no hayamos huido."

"A pesar de las temperaturas cálidas que hemos estado disfrutando, la lluvia es bastante fría. Desearía haber traído mi paraguas."

hi "Oye, probablemente deberíamos ir bajo techo para mantenernos secos."

show emi basic_confused_rn
show rin basic_absent_rn
with charachange

emi "Ya estamos bastante mojados, Hisao."

hi "Sí, pero así podemos secarnos y esperar a que pase la tormenta. No quieres pescar un resfriado o algo, ¿verdad?"

show emi basic_annoyed_rn
with charachange

"Emi considera esto por un momento. Puedo decir que parte de ella quiere quedarse afuera en la lluvia solo para desafiar al clima."

"Desafortunadamente para ella, al clima difícilmente le importe lo que hagamos."

show emi basic_closedgrin_rn
with charachange

emi "Supongo que tienes razón."

show emi sad_grin_rn
with charachange

emi "¿A dónde podríamos ir?"

"No tengo una respuesta para ella. El área todavía es muy nueva para mí."

"Aunque creo que me estoy acostumbrando lentamente a la escuela, el pueblo a su alrededor sigue siendo un misterio."

"Todo lo que conozco es la tienda de artículos de arte, y eso es solo porque acabamos de pasar junto a ella."

show emi basic_closedgrin_rn
with charachange

"Por fortuna, Emi pronto chasquea sus dedos en victoria."

show emi basic_happy_rn
with charachange

emi "¡Eso es! ¡Hay una casa de té cerca!"

emi "¡Podríamos tomar algo de té y secarnos, sin problema!"

"Eso no suena como una mala idea."

hi "¡Genial! ¿Sabes dónde está?"

show emi basic_grin_rn
with charachange

"Emi asiente, viéndose bastante segura."

show emi basic_closedgrin_rn
with charachange

emi "¡Claro que sí!"

show emi basic_hes_rn
with charachange

emi "Creo."

show emi excited_laugh_rn
with charachange

emi "Pero será una aventura de cualquier forma, ¿cierto?"

hi "Aventura, ¿eh? Bueno, supongo que podríamos tener una pequeña aventura."

"Creo que mientras nos quitemos de la lluvia estaré feliz."

show emi basic_grin_rn at twoleft
show rin basic_absent_rn at tworight
with dissolvecharamove

"La cesta del picnic está un poco más liviana ahora, por lo menos."

hi "¡Guíanos!"

show bg suburb_roadcenter_rn
hide rin
hide emi
with locationchange

"Rin y yo seguimos a Emi mientras esta traza un camino a través de las calles con algo que se aproxima a la confianza."

show emi basic_confused_rn at center behind rain
with charaenter

emi "Ahora, aquí a la izquierda…"

show emi excited_joy_rn
with charachange

emi "¡Ahí! ¡El Shanghái!"

"Emi resplandece victoriosamente mientras señala hacia la casa de té."

show bg suburb_shanghaiext_rn
hide emi
with locationchange


label es_E11x:

"Ahora que lo pienso, he estado aquí antes. Se ve bastante concurrido adentro; completamente por culpa de la repentina lluvia, estoy seguro."

play sound sfx_storebell
stop ambient fadeout 0.5
play music music_jazz fadein 2.0

scene bg suburb_shanghaiint
with locationchange

$ renpy.music.set_volume(0.7, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0

with Pause(1.0)

show yuukoshang neutral_down at center
with charaenter

yu "¡Bienvenidos! Puedo a—"

show yuukoshang happy_down
with charachange

yu "Oh, eres tú."

"Yuuko parece conocer a Emi."

show yuukoshang happy_down at tworight
show bg suburb_shanghaiint at bgright
with charamove

show emi basic_closedhappy at twoleft
with charaenter

"Emi sonríe alegremente, contenta de que la recuerden."

show emi basic_grin
with charachange

emi "¡Qué tal Yuuko! ¿Tienes lugar para sentarnos?"

show yuukoshang neutral_down
with charachange




label es_E11y:

"Se ve bastante concurrido adentro, un síntoma de la repentina lluvia, estoy seguro."

play sound sfx_storebell
stop ambient fadeout 0.5
play music music_jazz fadein 2.0

scene bg suburb_shanghaiint
with locationchange

$ renpy.music.set_volume(0.7, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0

with Pause(1.0)

show yuukoshang neutral_down at center
with charaenter

yu "¡Bienvenidos! Puedo a—"

"Estoy sorprendido de ver que nuestra mesera es nada menos que Yuuko."

"Sí que parece encajar con el uniforme. Es difícil creer que esta sea la misma bibliotecaria de nuestra escuela."

"¿Tiene dos empleos? Supongo que debe de ser eso."

show yuukoshang happy_down
with charachange

yu "Oh, eres tú."

"Yuuko parece conocer a Emi."

show yuukoshang happy_down at tworight
show bg suburb_shanghaiint at bgright
with charamove

show emi basic_closedhappy at twoleft
with charaenter

"Emi sonríe alegremente, contenta de que la recuerden."

show emi basic_grin
with charachange

emi "¡Qué tal, Yuuko!"

hi "Hola, Yuuko. No sabía que también trabajabas aquí."

show yuukoshang worried_down
with charachange

yu "¿Te conozco?"

show yuukoshang worried_up
with charachange

yu "Me pareces realmente familiar, pero no creo haberte visto aquí antes."

hi "Eh, nos conocimos en tu otro trabajo. En la biblioteca de Yamaku. ¿Recuerdas?"

show yuukoshang happy_up
with charachange

"Abre más sus ojos al recordar."

show yuukoshang closedhappy_down
with charachange

yu "¡Sí, eso es! Es bueno verte de nuevo…"

show yuukoshang panic_down
with charachange

yu "Oh no, ¡esto es malo!"

show yuukoshang panic_up
with charachange

yu "¡Debería haber recordado la cara de un cliente! ¡Lo siento… realmente lo siento!"

"Yuuko pasa de la realización al pánico en medio segundo, haciendo una serie de rápidas reverencias. Apenas evito ser golpeado por su cabeza en el proceso."

hi "¡Guau, oye, cálmate!"

hi "Escucha, yo no era un cliente la primera vez que nos vimos, de hecho nunca he estado antes en el Shanghái, así que todo está bien."

"No es un gran derroche de lógica, pero parece relajarla un poco."

show yuukoshang worried_down
with charachange

yu "¿En serio crees eso?"

hi "Eh, sí, seguro. Totalmente. ¿No es cierto, chicas?"

show emi basic_closedgrin
with charachange

"Emi ha estado observando cómo se desenvuelve este pequeño drama con considerable entretenimiento."

show emi excited_proud
with charachange

emi "Síp, ¡claro que sí!"

show yuukoshang neutral_up
with charachange

yu "Bien, de acuerdo…"

show emi basic_happy
with charachange

emi "Así que, Yuuko, ¿tienes lugar para sentarnos?"

show yuukoshang neutral_down
with charachange


label es_E11z:

$ renpy.music.set_volume(0.3, 3.0, channel="ambient")

"Yuuko asiente y nos lleva a una mesa esquinera, dándonos unas pequeñas toallas antes de tomar nuestra orden."

show yuukoshang happy_down
with charachange

yu "¿Qué van a ordenar?"

show emi basic_closedhappy
with charachange

emi "¡Pastel! Y también algo de té, supongo."

show yuukoshang neutral_down
with charachange

yu "¿Qué tipo de pastel?"

show emi excited_proud
with charachange

emi "¡Sorpréndeme!"

show yuukoshang worried_up
with charachange

"Yuuko se ve incómoda con la idea de sorprender a alguien, pero asiente y se vuelve hacia Rin."

show rin invis:
    yalign 1.0 xpos 1.0 xanchor 0.6
with None

show yuukoshang neutral_down:
    xpos 0.55
show emi basic_grin at left
show rin basic_absent at right
show bg suburb_shanghaiint at center
with dissolvecharamove

yu "¿Y para ti?"

show rin negative_spaciness:
    right alpha 1.0
with charachange

rin "Tomaré una pajilla. Mis pies están todos mojados."

show yuukoshang worried_up
with charachange

yu "¿Disculpa?"

show rin basic_awayabsent
with charachange

rin "De las que son para beber. Una, por favor."

show yuukoshang worried_down
with charachange

"Yuuko obviamente está insegura de qué pensar sobre esto. Vacila con el bolígrafo y sus apuntes, viéndose como si estuviera a punto de llorar, antes de volverse hacia mí."

show yuukoshang neutral_down
with charachange

yu "¿Y usted, señor?"

hi "Solo té, creo."

"Emi probablemente me regañaría si ordeno pastel."

show emi sad_depressed
with charachange

emi "¡Oh, vamos Hisao! No me dejes ser la única con comida, ¡me sentiré como un cerdo!"

hi "Solo trato de comer saludablemente."

hi "Son tus órdenes, después de todo."

show emi basic_closedgrin
with charachange

emi "Bueno… ¡hoy es tu día libre! ¡Podrás ser más saludable mañana!"

hi "Bueno, entonces supongo que pediré algo de pastel después de todo."

show yuukoshang neurotic_up
with charachange

"Yuuko se ve algo molesta por mi cambio de parecer."

yu "¿De cuál?"

"Miro a Emi de reojo y sonrío."

hi "Sorpréndeme."

show yuukoshang smile_down
with charachange

"Yuuko suspira y asiente."

yu "Muy bien. Su orden estará lista pronto."

show emi basic_grin at left
show yuukoshang neutral_down
show rin basic_awayabsent
with shorttimeskip

"A pesar de la multitud, nuestra orden efectivamente llega rápido."

show emi excited_joy
with charachange

emi "¡Gracias, Yuuko!"

"Yuuko asiente, agradecida."

stop music fadeout 4.0

show yuukoshang happy_down
with charachange

yu "Este no es el chico de siempre, ¿verdad?"

"¿Qué? ¿El chico de siempre?"

show emi basic_hes
with charachange

"Emi debe notar mi confusión, porque se ve un poco avergonzada."

emi "¿Q-qué? Oh, sí. Supongo que no lo es."

show emi sad_grin
with charachange

emi "Este es mi amigo Hisao."

hi "Ya nos habíamos conocido."

show yuukoshang smile_down
with charachange

yu "Huh. Un mundo pequeño."

show yuukoshang neutral_down
with charachange

yu "Bueno, avísenme si desean algo más."

hide yuukoshang
with charaexit

show emi sad_grin at twoleft
show rin basic_awayabsent at tworight
with charamove

"Con eso, Yuuko se aleja rápidamente para esperar en alguna otra mesa, dejándome para reflexionar su comentario."

"No soy el chico de siempre, ¿eh? Supongo que tiene sentido, ¿cierto? Emi es bastante popular, o eso me han dicho."

"Probablemente sea ese chico del equipo de atletismo."

"Esto es estúpido. Puedo sencillamente preguntarle a Emi."

show rin basic_absent
with charachange

play music music_comedy fadein 0.5

hi "Así que, ¿quién es este otro chico, eh? ¿Tienes un amante secreto o algo?"

show emi basic_closedhappy
show rin basic_awayabsent
with charachange

"Emi se ríe de nuevo, solo que tengo el presentimiento de que es tanto por el nerviosismo como por cualquier otra cosa."

show emi basic_grin
with charachange

emi "Es solo el capitán del equipo de atletismo. Le gusta venir acá algunas veces, luego de las prácticas."

show emi basic_closedgrin
with charachange

emi "Y si tenemos algo que discutir también vengo."

"Hmm, me suena terriblemente sospecho…"

show rin basic_absent
with charachange

hi "Oh, ya veo."

"Podría olvidar el asunto, pero no puedo resistir inmiscuirme un poco más."

hi "¡Entonces {b}sí{/b} es un amante secreto!"

hi "¡Lo sabía!"

show rin basic_deadpanamused
with charachange

"Rin observa nuestra plática, viéndose medianamente entretenida antes de murmurar algo que no logro captar."


rin "… de todas maneras."

show emi basic_confused
with charachange


$ doublespeak(emi,hi,u"¿Qué?", u"¿Eh?")

show rin basic_surprised
with charachange

"Rin se despierta bruscamente de su ensimismamiento."

rin "¿Eh?"

hi "¿Qué acabas de decir?"

show rin basic_deadpan
with charachange

rin "Eh."

hi "No, antes de eso."

show rin relaxed_nonchalant
with charachange

rin "Ni idea."

hi "Oh. Bueno."

hi "De acuerdo."

show emi basic_grin
show rin basic_deadpannormal
with charachange

"Dejo pasar el asunto, pero no puedo evitar darme cuenta de que Emi parece aliviada por la interrupción de Rin."

"Tal vez me pasé un poco…"

"La conversación merma por un rato mientras Emi y yo nos concentramos en el pastel."

"El mío es de fresas, y es sorprendentemente bueno."

play sound sfx_slide2

show emi excited_happy_close
with characlose

show emi basic_closedgrin
with charadistant

"Emi parece pensar lo mismo, ya que se acerca súbitamente con un tenedor y roba un pedazo."

hi "¡Ladrona!"

show emi excited_proud
with charadistant

emi "Pirata. Hay una diferencia."

hi "¡No estamos en el agua!"

show emi basic_closedgrin
with charadistant

emi "Bueno, no. Pero hay un montón de agua afuera, así que también funciona, ¿verdad?"

show emi sad_grin
with charadistant

emi "Además, puedes tomar un poco del mío. Creo que es de arándanos o algo así."

show emi sad_depressed
with charadistant

emi "Debería de haber pedido de fresas. Me gustan las fresas."

hi "Si de verdad lo necesitas, siéntete libre de servirte del mío."

"Por alguna razón, me siento obligado a añadir:"

hi "Teniendo en cuenta que ya lo hiciste sin más."

show emi basic_closedgrin
with charadistant

"Emi me saca la lengua, pero eso no evita que se apropie de mi pastel. Yo también pruebo un poco del de ella."

"Es de frambuesa, y muy bueno."

show rin relaxed_boredom
with charachange

rin "La lluvia se detuvo."

"Al parecer Rin estaba en lo correcto."

"Y justo a tiempo. He terminado mi comida, y parece que Emi también."

hi "Bueno, será mejor que paguemos y empecemos a movernos antes de que comience a llover de nuevo."

stop ambient fadeout 1.0

scene bg suburb_shanghaiext_rn
with locationchange

"Toma un par de minutos llamar la atención de Yuuko, pero pagamos y salimos rápidamente."

show emi basic_grin_rn at center
with charaenter

emi "Entonces, ¿quieres regresar al parque?"

"Me quedo boquiabierto."

hi "¿Estás bromeando? ¡Probablemente lloverá de nuevo!"

"De hecho, creo que acabo de sentir unas gotas de lluvia."

show emi sad_grin_rn
with charachange

emi "Hmm… puede que tengas razón."

show emi basic_closedgrin_rn
with charachange

emi "Bien, dejaré que te escapes esta vez, pero me debes un picnic. ¿Entendido?"

"No sé si me habla a mí, a Rin, o a los dos."

hi "Bien, bien."

show emi excited_proud_rn
with charachange

emi "¡Ahora apresúrense! Quería correr un poco en la pista, y sería agradable hacerlo sin la lluvia."

hi "¡Pensé que este era tu día libre!"

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
stop music fadeout 6.0

show emi sad_depressed_rn
with charachange

emi "Bueno…"

"Repentinamente Emi parece renuente a explicarse."

show emi sad_grin_rn
with charachange

emi "Necesito la práctica."

show emi basic_grin_rn
with charachange

emi "Y necesito quemar ese pastel, de todas formas."

"¿Por qué tengo la sensación de que ella está olvidando mencionar algo?"

hi "¿Estás segura? No fue mucho pastel…"

show emi basic_closedgrin_rn
with charachange

emi "No, no fue mucho pastel para {b}ti{/b}. Yo me comí la mayoría."

"En eso tiene razón."

label es_choiceE11:
menu:
    with menueffect
    "Aun así, siento que por lo menos debería ofrecerme para correr con ella…"
    "Ofrecerme para correr con Emi.":




        return m1
    "Guardar silencio.":

        return m2

label es_E11b:


hi "Oye, correré contigo."

hi "Yo también debería, ¿cierto?"

show emi basic_annoyed_rn
with charachange

"Emi sacude la cabeza con vehemencia."

emi "No lo harás, Hisao. El descanso es crítico para ti, ¿recuerdas?"

emi "No permitiré que te exijas demasiado."

"Creo que ella es mejor dando consejos que recibiéndolos."

hi "Lo que digas, Emi."

"Creo que lo mejor es no presionar en el asunto."

label es_E11c:



"Pensándolo bien, ella parece preferir estar sola en este momento."

"Decido guardarme el ofrecimiento."

label es_E11d:



stop music fadeout 12.0

scene bg school_dormext_full_rn
with locationskip


play ambient sfx_rain fadein 2.0
show rain normal
with Dissolve(2.0)

"Mientras nos acercamos al dormitorio de las chicas, empieza a llover de nuevo."

show emi sad_annoyed_rn at center behind rain
with charaenter

"La expresión de Emi se amarga levemente."

emi "Oh, vaya…"

emi "Estúpida lluvia."

hi "Oye, pronto acabará. Entonces podrás ir a correr, ¿verdad?"

show emi basic_grin_rn
with charachange

"Emi resopla, al parecer divertida."

show emi excited_proud_rn
with charachange

emi "Como si no fuera a correr en la lluvia."

hi "¡Bueno, no deberías! ¡Pescarás un resfriado!"

show emi basic_grin_rn
with charachange

"Emi sacude la mano distraídamente."

emi "¡Ridículo! Yo no me resfrío."

show emi basic_closedgrin_rn
with charachange

emi "Mi sistema inmunológico es demasiado resistente para algo como eso."

"No puedo evitar reírme."

hi "Bueno, entonces te veré mañana, ¿de acuerdo?"

show emi basic_happy_rn
with charachange

emi "¡Sí!"

show emi basic_grin_rn
with charachange

emi "¡Gracias por venir! Oh, ¡y por cargar la cesta del picnic!"

show emi excited_amused_rn
with charachange

emi "La llevaré para el almuerzo de mañana. ¡Podemos tener nuestro picnic en la azotea!"

hi "Suena bien. ¡Las veo luego!"

hide emi
with charaexit

"Emi agarra la cesta y cruza la puerta apresuradamente."

"Rin me hace una especie de media cabezada y también camina hacia adentro."

"Maldición, está mojado aquí afuera."

"Necesito regresar a mi habitación y ponerme algo de ropa seca."

stop ambient fadeout 2.0

scene bg school_dormhallway
with locationskip

"Pronto estoy frente a mi puerta, pero soy interceptado por la súbita aparición de Kenji, quien parece estar cargando un montón de libros."

show kenji neutral at center
with charaenter

ke "Oye hombre, dame una mano, ¿podrías?"

hi "¿Eh?"

play music music_kenji fadein 0.5

with vpunch

"Los libros son arrojados a mis brazos sin contemplaciones mientras Kenji busca a tientas las llaves de su habitación."

show kenji happy
with charachange

ke "Gracias, eres un salvavidas."

ke "Si no hubieras estado cerca tendría que haber dejado mi puerta sin llave, y eso solo es rogar por problemas."

show kenji tsun
with charachange

ke "La oportunidad perfecta para preparar una emboscada, o tal vez simplemente colocar una bomba si no quieren ensuciarse demasiado las manos."

ke "Probablemente no."

ke "Temen poder quebrarse una uña o algo si tienen que apuñalarme."

ke "Mujeres."

"Mi mente analiza digerir el torrente verbal que acaba de ser liberado, pero elige permanecer cómodamente en la ignorancia."

hi "Ah… ajá."

show kenji happy
with charachange

ke "Como sea, ¿dónde has estado, hombre?"

show kenji neutral
with charachange

ke "¡No me habría caído mal un poco de ayuda cargando estos desde la biblioteca!"

ke "Llamé a tu puerta, pero no estabas ahí."

hi "Oh, lo siento."

"En realidad no. Pareces creer que soy algún tipo de mula de carga."

hi "Estaba fuera con Emi y Rin."

show kenji rage
with charachange

"Kenji se tambalea por la sorpresa."


"Parece como si acabara de dispararle a su perro, si él tuviera un perro."

ke "¿Las amiguitas sin extremidades de nuevo?"

show kenji tsun
with charachange

ke "¿Qué hiciste esta vez?"

hi "Bueno, terminamos en el Shanghái—"

"No puedo proseguir por una súbita exclamación de angustia."

show kenji rage
with vpunch

ke "¿El Shanghái?"

ke "¿Por qué el Shanghái?"

ke "No no no no, hombre, ¡simplemente no puedes ir al maldito Shanghái!"

ke "¡Es el lugar más peligroso de la ciudad!"

ke "¡Una verdadera fortaleza de sus mejores agentes!"

ke "¡Lo sé! ¡Las he conocido!"

ke "No se detendrán ante nada para inspirarte una falsa sensación de seguridad, y luego ¡BAM!"

play sound sfx_impact2
with vpunch

"Golpea su puerta para enfatizar."

ke "Billetera desaparecida. ¿Pasaje del autobús? Desaparecido. ¿Identificación? ¡Jodidamente {b}desaparecida{/b}, hombre!"

show kenji tsun
with charachange

ke "¡Prométeme que no irás allí de nuevo!"

"Él se ve tan fervientemente opuesto a la idea del Shanghái que estoy dispuesto a mentir un poco para poder entrar a mi habitación."

hi "Por supuesto, no iré allí de nuevo."

"O al menos, nunca te diré si voy allí de nuevo."

"Esto parece apaciguar a mi acompañante de anteojos."

show kenji neutral
with charachange

ke "Bien, bien."

show kenji happy
with charachange

ke "Perdona por ser tan agresivo, pero conozco el peligro de ese lugar demasiado bien como para simplemente dejarte vagar por la guarida del león de nuevo."

ke "Saliste vivo de allí una vez, pero intentarlo una segunda vez es tentar a la suerte."

hi "Sí, bueno, necesito cambiarme y eh, hacer la tarea. Entonces… te veré luego."

show kenji tsun
with charachange

ke "¿Eh?"

show kenji neutral
with charachange

ke "Oh, claro. Lo que sea."

"De repente, recuerdo que aún sostengo sus libros."

hi "Será mejor que agarres estos."

"Miro uno de los títulos por una fracción de segundo, algo acerca de criptografía."

"Qué bicho raro."

stop music fadeout 6.0

show kenji neutral:
    center
    easeout 0.5 xpos 0.3 alpha 0.0
with None

"Kenji agarra su precioso cargamento y desaparece por su puerta."

$ renpy.music.set_volume(0.1, 0.0, channel="ambient")
play ambient sfx_rain fadein 1.0

scene bg school_dormhisao
with locationchange

"Abro mi propia puerta y entro, agradecido de poder quitarme estas ropas empapadas."

"La lluvia gana fuerza, y empiezo a desear que Emi no esté afuera corriendo con este clima. Se veía muy decidida a correr sola, no puedo evitar preguntarme si su pierna aún le molesta."

"Intento recordar si la vi cojear hoy, pero no puedo. Supongo que estaba muy distraído disfrutando del día, incluso si nos llovió."

"Y mientras recuerdo los eventos de hoy, continúo desviándome hacia mi compañera de carreras."

"Su completo rechazo a permitir que la lluvia arruinara nuestros planes fue increíblemente tierno."

"Pero ahí también había algo más."

"Una especie de actitud imperturbable cuando se trata de disfrutar el día a como venga."

"Realmente me gusta esa cualidad."


"Tal vez yo también deba hacer eso."

stop ambient fadeout 2.0
scene black
with dissolve

$ suppress_window_after_timeskip = True



label es_E12a:

window hide None

scene black
with dissolve

play sound sfx_alarmclock

with Pause(2.0)

scene bg school_dormhisao
with openeye

window show

"El sonido de mi alarma me saca de un sueño que involucraba piratas y otras cosas que honestamente no puedo recordar."

scene bg school_track
with locationskip

play music music_pearly

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

"Tengo la vista un poco nublada, y se siente como si me tomara más tiempo del usual vestirme y bajar hacia la pista."

"Un vistazo a mi reloj de pulsera revela que estaba en lo correcto, y en realidad estoy algo atrasado."

"El asunto es…"

"No veo a Emi."

"Eso es extraño. Debería estar aquí."

"Definitivamente debería estar aquí."

"Quiero decir, yo llegué {b}tarde{/b}."

"Supongo que no fui el único que tuvo problemas levantándose esta mañana."

"El pensamiento de que ayer nunca dejó de llover del todo cruza mi mente. ¿Aun así fue a correr?"

label es_E12b:



"Parece probable. Emi es muchas cosas, pero prudente no es una de ellas. Probablemente pensó que la lluvia no se detendría, y es por eso que estaba tan decidida a correr sola."

"A pesar de eso, yo habría corrido contento con ella, incluso si era bajo la lluvia."

"Diablos, al menos podría haberla convencido de que entrara una vez que se pusiera realmente feo. Ese es el motivo por el cual ella no quería que yo viniera, por supuesto."

label es_E12c:



"Debí haberme ofrecido a correr con ella."

"Entonces podría haberle quitado esa idea, o al menos podría haber sabido si ella estaba bien. ¿Qué tal si fue alcanzada por un rayo o algo?"

"Nunca me lo perdonaría."

"…"

"De acuerdo, puede que eso sea un poco estúpido."

"Emi es una chica capaz. Ni siquiera ella se quedaría fuera durante una tormenta eléctrica."

"Al menos en este caso confío en su juicio."

label es_E12d:



"Aun así, no puedo evitar querer saber dónde está."

"… Bueno, nada que hacer. Será mejor estirar y correr, y esperar a que Emi se aparezca con una sonrisa y una excusa."

scene bg school_track_running
with shorttimeskip

show bg school_track_on
with Dissolve(3.0)

"En mi vuelta de enfriamiento, me veo obligado a admitir que Emi no se aparecerá."

"Además, no tengo ni idea de dónde está. La ansiedad me mortifica mientras que al mismo tiempo me pregunto por qué estoy tan preocupado por ella."

"Correr me ayudó a olvidarme de ello por un rato, pero ahora que he terminado me preocupo de nuevo."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

nvl clear

nvl show dissolve

n "\n\nFue extraño no tenerla aquí."

n "Completamente desconcertante."

n "De repente caigo en la cuenta de que he estado corriendo para estar con Emi tanto como he estado corriendo para mantenerme saludable —probablemente más por estar con Emi, ahora que pienso en ello."

n "Es una de esas cosas que son completamente obvias y aun así, por algún motivo, nunca me había dado cuenta."

n "Ella de verdad es alguien con quien disfruto estar."

n "Como revelaciones, son difícilmente inquietantes."

n "Pero a la vez, me encuentro sintiéndome ligeramente sorprendido."

n "¿Cuándo pasó esto?"

n "Bueno, no hay tiempo para pensar en esto, aunque quiero reflexionar sobre esta novedad, tengo un mayor deseo por saber qué le pasó a Emi."

n "Le preguntaré al enfermero cuando vaya a verlo."

$ renpy.music.set_volume(1.0, 2.0, channel="music")
stop music fadeout 2.0

nvl clear

nvl hide dissolve

scene bg school_nurseoffice
show nurse neutral at center
with shorttimeskip

nk "Bueno, pareces estar en buena forma, Hisao."

hi "Es bueno oírlo."

"Me vuelvo a poner la camiseta y me levanto para irme, como siempre."

"Excepto que en vez de irme, pregunto algo."

hi "Oye, ¿dónde está Emi? No se apareció esta mañana."

hi "¿Se encuentra bien?"

show nurse concern
with charachange

"Mientras intento ocultar valientemente la ansiedad en mi voz, la expresión del enfermero sugiere que he fallado miserablemente."

nk "¿Quieres decir que no te dijo?"

nk "Ella está enferma, en cama."

hi "¿Qué? ¿Enferma?"

show nurse neutral
with charachange

"El enfermero se encoge de hombros."

nk "Sí, ella vino a mi oficina temprano en la mañana con fiebre."

nk "Para ser honesto estoy sorprendido de que haya logrado llegar hasta aquí."

show nurse concern
with charachange

nk "Estaba ardiendo cuando llegó."

nk "Creía que planeaba hacértelo saber, pero ella me pidió que te lo dijera… ¡oh diablos!"

stop music fadeout 2.0

show nurse neutral
with charachange

"El enfermero me lanza una sonrisa avergonzada que parece por lo menos parcialmente sincera."

nk "Le dije que pasaría por la pista para decírtelo en caso de que ella lo olvidara. Perdón por eso."

play music music_nurse fadein 1.0

show nurse fabulous
with charachange

nk "Pero no necesitamos decirle a Emi que lo olvidé, ¿cierto?"

"Le devuelvo una sonrisa astuta al enfermero."

hi "Oh, claro que no."

hi "Es buen material de chantaje."

hi "Lo guardaré para cuando necesite un favor tuyo."

show nurse grin
with charachange

"El enfermero se ríe."

nk "Bueno, supongo que me merecía eso."

nk "Pero sabes, tengo formas de chantajearte de las que ni siquiera estás consciente."

show nurse fabulous
with charachange

nk "Así que no tientes tu suerte, ¿entendido?"

"Mi expresión se gana otra carcajada del enfermero."

show nurse grin
with charachange

nk "Solo bromeo, Hisao."

show nurse concern
with charachange

nk "Pero en serio, no le digas a Emi que lo olvidé, ¿de acuerdo?"

hi "Tu secreto está a salvo conmigo."

show nurse neutral
with charachange

nk "Oh bien. Ahora anda, sal de aquí."

hi "Espera, tengo otra pregunta más."

show nurse fabulous
with charachange

nk "Dispara."

hi "¿Ella va a estar bien?"

show nurse grin
with charachange

nk "Oh sí, definitivamente."

show nurse neutral
with charachange

nk "Su fiebre era fuerte, pero ya estaba empezando a bajar cuando vino a mi oficina."

nk "Probablemente iré a verla de nuevo en el almuerzo para estar seguro, pero imagino que estará en pie para el anochecer sin importar lo que le diga."

hi "Hmm, tal vez debería visitarla luego de clases."

"Me toma un segundo enterarme de que lo dije en voz alta."

show nurse fabulous
with charachange

"El enfermero levanta una ceja y me lanza una mirada analítica por un momento."

nk "Hmm…"

show nurse neutral
with charachange

nk "Bueno, puede que no sea una mala idea."

nk "Podrías hacerme saber si ha empeorado, supongo."

show nurse concern
with charachange

nk "Pero nada de hacer cosas raras, ¿entendido? Sé cuáles medicinas estás tomando, después de todo."

"Creo que eso es una amenaza contra mi vida, pero no estoy seguro."

stop music fadeout 7.0

scene bg school_nursehall
with locationchange

"De cualquier forma, le aseguro al enfermero que mis intenciones son puras y salgo de la oficina."

"Interesante que el enfermero me vea como una especie de pretendiente potencial de Emi."

"Aún más interesante es lo complacido que eso me hace sentir."

"Necesito una ducha."

scene bg school_scienceroom
with shorttimeskip

play sound sfx_normalbell

"Suena la campanada del almuerzo, y no me encuentro dispuesto a subir hasta la azotea."

"Después de todo, apuesto a que Rin sabe dónde está Emi, y de ser ese el caso entonces dudo que se moleste en ir allá arriba."

"Más concretamente, dudo que tengamos cualquier tipo de conversación interesante si lo estuviera. Posiblemente prefiera estar sola allá arriba, para que así no le arruine accidentalmente su línea de pensamiento o algo."

"Desafortunadamente, tampoco me siento realmente dispuesto a ir a la cafetería."

"Supongo que entonces iré a la biblioteca."

"Necesito un nuevo libro para leer, de todos modos, habiendo terminado el otro ayer antes de dormir. Tal vez pueda encontrar más del mismo autor."

scene bg school_library
with locationskip

play music music_happiness fadein 2.0

"Amo las bibliotecas."

"Huelen como a polvo y papel y tinta."

"Todas estas historias y hechos y opiniones almacenados juntos en un lugar hacen que el aire vibre por el gran potencial."

"Aún no estoy seguro de cómo navegar por la biblioteca de Yamaku, habiendo estado apegado principalmente a libros que traje conmigo, así que busco a la bibliotecaria para pedir ayuda."

"…"

"Hmm. Supongo que no está por aq—{w=0.5}{nw}"

show yuuko smile_down:
    center
    xpos 0.4
    easein 0.5 center
with charaenter

yu "… no puedo creerlo."

"Yuuko, viéndose bastante distraída, emerge repentinamente de uno de los pasillos."

hi "Eh, disculpa."

show yuuko neutral_down
with charachange

yu "Oh, ¿puedo ayudarte?"

hi "De hecho, estaba buscando un libro…"

show yuuko panic_up
with charachange

yu "¡Yo también!"

show yuuko smile_down
with charachange

yu "“Criptografía Avanzada”. Acabamos de adquirirlo, y ya se ha perdido."

show yuuko worried_up
with charachange

yu "¡Tenía tantas ganas de leer ese!"

hi "¿Criptografía?"

show yuuko neurotic_up
with charachange

yu "Sí, vaya… eh, lo que pasa…"

yu "Este chico que conocía. Conozco. Um."

yu "No estoy segura de cómo describirlo…"

hi "Ve al grano."

show yuuko smile_down
with charachange

yu "Él hizo que me interesara por la criptografía y ahora el libro no está, ¡y creo que ha sido robado!"

hi "Suena realmente terrible."

show yuuko worried_up
with charachange

yu "Sí, ¡especialmente porque ahora tengo que buscarlo por toda la biblioteca!"

yu "¡Aunque es probable que ni siquiera esté aquí!"

hi "Te ves… ocupada."

show yuuko neurotic_up
with charachange

yu "Un poco."

show yuuko neurotic_up:
    center
    easeout 0.5 alpha 0.0 xpos 0.6
with None

"Ella sale corriendo por otro pasillo, y me resigno a encontrar mi propio libro."

"Hmm, muchas opciones."

stop music fadeout 2.0

hide yuuko
with shorttimeskip

"Oh vamos, ¿cómo me perdí?"

"¡Estos ni siquiera son libros impresos! Están todos en braille."

"Supongo que tiene sentido en una escuela como esta, pero honestamente, es un poco molesto."

li "Lo lamento, ¿hay alguien allí?"

"Una voz melodiosa sale desde atrás de uno de los cubículos establecidos para el estudio."

show lilly basic_displeased at center
with charaenter

"Cuando me acerco, veo que Lilly ha estado leyendo un libro mientras yo daba tumbos por el pasillo."

hi "Oh no, yo debería disculparme. No era mi intención hacer tanto ruido."

show lilly basic_ara
with charachange

li "Vaya, ¿eres tú, Hisao?"

show lilly basic_smile
with charachange

li "No he sabido nada de ti desde hace un tiempo."

show lilly basic_pout
with charachange

li "Empezaba a pensar que te habías olvidado de mí por completo."

hi "Eh, perdona."

play music music_lilly fadein 4.0

show lilly basic_giggle
with charachange

"Lilly se ríe de esa manera tan refinada suya y sacude la cabeza."

show lilly basic_smile
with charachange

li "Solo te estoy molestando, Hisao."

li "Por lo que he escuchado, has estado ocupado."

show lilly basic_cheerful
with charachange

li "Carreras matutinas con Emi Ibarazaki {b}y{/b} almuerzos en la azotea, si no me equivoco."

hi "Je, sí."

hi "Supongo que los rumores se difunden rápidamente."

show lilly basic_weaksmile
with charachange

li "Eso y que ya no puedo mimar a la pobre Hanako en la azotea."

show lilly basic_displeased
with charachange


li "Siempre están allá arriba, reclamando el sitio para ustedes tres."

"Ella me reprende gentilmente, aunque es bastante claro que solo me está molestando de nuevo."

"Aun así, siento una extraña necesidad de disculparme."

hi "Perdona, podríamos almorzar en algún otro lugar si realmente es un problema—"

show lilly basic_ara
with charachange

li "Oh no, no me preocuparía por ello."

show lilly basic_smile
with charachange

li "Hanako y yo tenemos otras cosas que hacer en el almuerzo, también."

li "Como leer en la biblioteca, como puedes ver."

hi "Oh, ¿Hanako también está aquí? No la vi."

show lilly basic_smileclosed
with charachange

"Lilly sonríe, un poquito enigmática."

li "Oh, está por alguna parte."

show lilly basic_smile
with charachange

li "Pero estoy sorprendida, Hisao. Estás aquí, en vez de allá arriba."

li "¿Qué te trae a la biblioteca?"

hi "Bueno, Emi está enferma, así que no hay ningún almuerzo en la azotea que me mantenga ocupado…"

show lilly basic_giggle
with charachange

"Lilly levanta una ceja por esto antes de reírse entre dientes de nuevo."

li "Vaya, la pobre Rin debe sentirse excluida."

hi "¡No es eso!"

show lilly basic_weaksmile
with charachange

li "Ah, pero estoy segura de que no lo es. Emi tiende a ser la vida de cualquier grupo en el que esté."

show lilly basic_sad
with charachange

li "Es una pena escuchar que enfermó. ¿Estará bien?"

"Por algún motivo tengo la sensación de que Lilly solo pregunta por amabilidad, pero respondo de todas maneras."

hi "El enfermero piensa que sí. Voy a pasar a ver cómo está luego de la escuela."

show lilly basic_smileclosed
with charachange

"Otra ceja levantada."

li "Vaya, qué caballeroso eres, Hisao."

hi "No es nada, en serio. Tan solo me preocupo por mi amiga, después de todo."

show lilly basic_planned
with charachange

li "Ah, ¿entonces solo son amigos? Qué desilusión."

"Me sonrojo, aliviado de que Lilly no lo pueda ver."

show lilly basic_giggle
with charachange

"Pero de algún modo ella sabe que me he puesto nervioso por su comentario de todas formas, y se ríe."

li "Lo lamento, Hisao. Te estoy molestando de nuevo."

show lilly basic_smile
with charachange

li "Por favor dile a Emi que espero que se sienta mejor, ¿lo harías?"

"Una mirada a mi reloj revela que estoy muy cerca de quedarme sin tiempo para encontrar mi libro."

hi "Por supuesto."

hi "Oye, tengo que encontrar un libro antes de que acabe el almuerzo, así que mejor empiezo a moverme."

hi "Te veo después."

"Esa probablemente no fue la mejor frase que podía usar."

"Lilly, sin embargo, toma mi metedura de pata con calma."

show lilly basic_weaksmile
with charachange

stop music fadeout 3.0

li "Hasta encontrarnos de nuevo, Hisao."

scene bg school_hallway2
with shorttimeskip

"Nunca encuentro el libro que estaba buscando, pero salgo con otra cosa en su lugar."

"Mi estómago gruñe un poco, haciéndome saber que debería haber almorzado algo."

"Oh, bueno."

"Buscaré algo antes de visitar a Emi más tarde."


label es_E13:

scene bg school_hallway2
with None

scene bg school_scienceroom
with shorttimeskip

play music music_normal fadein 3.0

"Pareciera que el tiempo ha decidido ralentizarse con el único propósito de aburrirme hasta el cansancio."

"La clase parece arrastrarse por años."


"Sospecho que estar consumido por la preocupación probablemente tenga algo que ver."

play sound sfx_normalbell

"Gracias al cielo suena la campana y me apresuro en salir de clase, provocando algunas cejas levantadas, estoy seguro."

scene bg school_hallway3
with locationchange

"He pasado la mayor parte del día preocupándome tan discretamente como he podido."

"Incluso si el enfermero piensa que Emi está perfectamente bien, quiero ir a ver por mí mismo."

stop music fadeout 14.0

scene bg school_girlsdormhall
with locationskip

"No toma mucho tiempo llegar al dormitorio de las chicas y encaminarme a la habitación de Emi."

"Una vez que estoy fuera de su puerta, me detengo repentinamente. ¿Y si está descansando?"


"No me gustaría despertarla, especialmente si aún se siente enferma."

"Por otra parte, si ella duerme todo el día podría arruinar su horario de sueño."

"Pero el descanso es importante si estás enfermo, ¿verdad?"

"No puedo decidir qué hacer, así que termino parado frente a la puerta viéndome como un idiota."

"Entonces escucho la voz de Emi detrás de la puerta."

emi "Gracias por tu preocupación, pero en serio estoy bien."

"¿Me está hablando a mí?"

emi "¡Te veré mañana en la práctica!"

"Supongo que no."

"Sin embargo, evidentemente no está dormida, así que puedo llamar a la puerta sin problema."





"¿Entonces por qué tengo esta sensación de incomodidad en mis entrañas? No estaba nervioso por venir el otro día, ¿entonces por qué hoy sí?"

"Aunque no he tenido mucho tiempo para indagar sobre este nuevo interés en el bienestar de Emi."

"No tengo mucha experiencia en el asunto, por supuesto, pero ciertamente esto parece trascender los sentimientos de pura amistad."

"Pero, ¿puedo dar ese paso? ¿Acaso podré alguna vez arriesgar lo que tengo ahora?"

"Quiero decir, es suficiente con ser su amigo, ¿verdad?"

"De cualquier manera, ¿no debería tan solo abrir la puerta y ver cómo está? Es por eso que vine aquí… ¿cierto?"

stop music fadeout 1.5

"¿Qué tal si aún no está vestida?"

play ambient sfx_heartslow

with Fade (0.05, 0.0, 0.3, color="#ffc0cb")

"La imagen que cruza mi mente provoca que mi corazón se salte un latido, literalmente."

stop ambient fadeout 3.0


"Probablemente no debería pensar en esas cosas de nuevo. No si quiero evitar un ataque cardiaco."

"De repente caigo en la cuenta de que todavía estoy parado en el pasillo viéndome como un idiota."

play sound sfx_doorknock2

"Emi aún parece estar en medio de una conversación, pero llamo a la puerta de todas formas. Espero que no le moleste la interrupción."

emi "Te preocupas dem— ¡Entra! La puerta está abierta."

"Lo está. Abro la puerta y entro, y es alrededor de ese punto en que los procesos de mi mente se detienen abruptamente."

play music music_serene fadein 4.0

scene ev emi_sleepy_face:
    subpixel True
    center
    zoom 1.05
    ease 15.0 zoom 1.0
with whiteout


"Emi está sentada en la cama, su cabello despeinado por pasar el día dormida. Creo que esta es la primera vez que la veo sin esas familiares coletas en su cabello."

"Su camiseta de gimnasio y su pantaloneta, colocadas con evidente precipitación antes de que yo entrara, están arrugadas y dobladas por no haber sido guardadas adecuadamente."

scene ev emi_sleepy_legs at Fullpan(8.0)
with flash

"Sus piernas yacen descubiertas sobre las sábanas."

"Nunca he visto a Emi sin sus prótesis antes. Y aquí está, piernas esbeltas terminando en muñones justo debajo de sus rodillas."

"Pero por extraña que sea la imagen, me encuentro más cautivado por todo lo que está al norte de la cintura."

scene ev emi_sleepy:
    subpixel True
    center
    zoom 1.05
    ease 15.0 zoom 1.0
with flash

"Parece que Emi ha terminado su conversación con quien fuera que estaba en el teléfono con ella, y ahora está observando mi reacción atentamente con su ojo abierto mientras se restriega el sueño del otro."

"Su expresión, lejos de ser de vergüenza, consiste más bien en un bostezo sorprendentemente amplio. Uno quizás apropiado para una boca tan pequeña."

"Una sonrisa que por un breve instante parece casi de coqueteo se forma en las esquinas de su boca cuando ve que estoy adentro."

"No puedo hacer nada más que permanecer en un estado fluctuante entre miedo, confusión, y ni un poquito de lujuria."

"Emi se aparta el cabello de los ojos rápidamente, colocándolo en su lugar antes de dirigirse a mí."

scene bg school_dormemi
show emi sad_grin_gym at center
with locationchange


emi "Te ves un poco sorprendido, Hisao."

"Una oleada de risa emerge de ella, y me encuentro sonriendo y frotándome la parte trasera de mi cabeza avergonzadamente."

hi "Perdona, es que…"

"Nunca había visto a alguien tan despeinado verse tan atractivo."

"Nunca te había visto sin tus piernas puestas."

"Nunca te había visto tan…"

hi "Um, perdona."

show emi basic_closedgrin_gym
with charachange

"Emi se ríe de nuevo y se mueve para sentarse un poco más derecha."

"Soy cautivado por los movimientos de su camiseta, muy cerca de perder la cabeza."

show emi basic_grin_gym
with charachange

emi "Me preguntaba cómo sería tu reacción."

show emi basic_closedhappy_gym
with charachange

emi "Verás, el enfermero llamó y me dijo que vendrías."

show emi basic_grin_gym
with charachange

emi "Y sé que nunca me has visto… bueno, ya sabes."

show emi sad_grin_gym
with charachange

emi "Sin piernas."

"Respondo en un tono de casual sorpresa."

hi "Oh, ¿no las tienes puestas? No me di cuenta."

"Esta es casi la verdad. Estuve muy cerca de no hacerlo."

"No intento ser condescendiente ni nada, fíjate. Por algún motivo creo que Emi se ofendería por eso."

stop music fadeout 0.5
play sound sfx_pillow
show emi basic_annoyed_gym
with vpunch

"En vez de eso, ella me saca la lengua y arroja una almohada a mi cabeza."

emi "Idiota."

"Atrapo la almohada hábilmente y apunto cuidadosamente antes de lanzarla."

play music music_running

show emi basic_annoyed_gym:
    center
    parallel:
        ease 0.5 xpos 0.7
    parallel:
        "emi basic_closedhappy_gym" with Dissolve(0.5, alpha=True)

"Emi se ríe y gira hacia un lado, esquivando mi tiro, con el desplazamiento de su camiseta distrayéndome lo suficiente para que la siguiente almohada me golpee justo en medio de los ojos."

play sound sfx_pillow

hi "¡Au!" with hpunch

"Tomo represalias, por supuesto."

"Y una vez que he tomado represalias dos veces, bueno, una guerra estaba destinada a empezar tarde o temprano."

"Y la verdad, cuando Emi parece tener mucho mejor pulso que yo, bueno…"

"Era solo cuestión de tiempo antes de que tuviera que recurrir a un ataque suicida."

show bg school_dormemi:
    center
    ease 0.5 bgleft

show emi basic_closedhappy_gym:
    ease 0.5 center

with None

show emi basic_closedhappy_gym_close:
    ease 0.5 center

with characlose

hi "¡Te tengo!"

show emi basic_hes_gym_close
with charachange

emi "¡Eep!"

window hide None

play sound sfx_pillow

show comic vfx1
show emi basic_closedsweat_gym_close
with vpunch

with Pause(0.5)

play sound sfx_pillow

show comic vfx2
with hpunch

with Pause(0.5)

play sound sfx_pillow

show comic vfx3
with vpunch

with Pause(0.5)

show comic vfx3:
    truecenter
    easeout 0.5 yanchor 0.3 alpha 0.0
with Pause(0.5)







stop music fadeout 3.0

scene black
with dissolve

window show

"Y una vez que el ataque fue completado, bueno, está claro que tengo que luchar por arrojar las almohadas lejos de ella."

"Y con ese tipo de lucha, obviamente terminamos en esta posición."

window hide

play music music_twinkle fadein 2.0

scene ev emi_bed_full:
    xalign 0.5 yalign 1.0 subpixel True
    easein 15.0 yalign 0.0

with Dissolve(1.0)

with Pause(3.0)

window show

"Y así me encuentro mirándola desde mi posición, encima de ella."

"Ella está sonriendo, ojos brillando por la diversión, tal vez un poco sudada por nuestro forcejeo."

"Su pecho sube y baja, aspirando aire."

"La pequeña parte de mi cerebro que no está atrapada en estos momentos por la visión y el olor de ella observa que aún debe de estar enferma, porque su resistencia no es la que debería."

"Nos quedamos así por un rato."

"No estoy seguro de por cuánto tiempo, porque todo parece volverse borroso. Todo lo que no es ella, al menos."

"Sus ojos se encuentran con los míos, y en lo profundo de los suyos casi puedo ver un atisbo de… qué, ¿miedo? ¿Anhelo?"

"¿Esperanza?"

hi "¿Emi…?"

stop music fadeout 0.5

show ev emi_bed_unsure at center
with vpunch

"Una tos la hace estremecerse repentinamente, y casi tropiezo en la urgencia de quitarme, para disculparme por todo."

play music music_emi fadein 3.0

hi "Perdona, no debí…"

show ev emi_bed_happy
with charachange

emi "Está bien, está bien."

"Ella me da unas palmaditas tranquilizadoras en el hombro."

show ev emi_bed_normal
with charachange

emi "Entonces… ¿qué te trae por aquí?"

"Aún está respirando con agitación, y eso provoca que su voz tiemble ligeramente."

hi "Bueno, antes de ser atacado tan groseramente con almohadas, venía a ver qué tal estabas."

window hide None

play sound sfx_pillow

show comic vfx4
show ev emi_bed_frown
with vpunch

with Pause(0.5)

show comic vfx4:
    truecenter
    easeout 0.5 yanchor 0.3 alpha 0.0
with Pause(0.5)

window show

"Esto me consigue otro empujón, y estoy muy cerca de caer de su cama."

show ev emi_bed_normal
hide comic
with charachange

"Los ojos de Emi brillan de nuevo, y me pregunto cómo es que nunca antes noté lo atractivos que son."

show ev emi_bed_smile
with charachange

emi "Te consumía la preocupación, ¿cierto?"

"Su tono es burlón, arrogante. Provocativo."

"Arroja dramáticamente un brazo hacia su frente, su sonrisa aún es evidente bajo él."

show ev emi_bed_unsure
with charachange

emi "¿No podías soportar pensar en mí yaciendo enferma de muerte?"

"Cuando los dos nos recuperamos de nuestro breve encuentro de lucha libre, Emi parece estar provocándome de nuevo."

hi "Bueno, no diría consumido por la preocupación, pero luego de que no te presentaste esta mañana como toda una cobarde…"

show ev emi_bed_frown
with charachange

"Emi hace una mueca, cruzando sus brazos con petulancia y sacando su labio inferior."

emi "No es mi culpa."

emi "El enfermero no me lo permitiría."

hi "Claro que no lo haría. Te creo completamente."

"Emi saca su lengua de nuevo."

emi "Eres un verdadero idiota, Hisao."

hi "Entonces, cómo estuvo tu día, ¿eh? ¿Disfrutaste holgazanear?"

show ev emi_bed_normal
with charachange

emi "En realidad no, el teléfono me despertó bastante temprano."

hi "¿El teléfono?"

emi "Sí, el capitán del equipo llamó para asegurarse de que yo estuviera bien."

emi "También para hacerme saber que no había problema en que me saltara la práctica."

"Bien, al menos no estuvo sola todo el día. Alguien se aseguró de que estuviera bien."

"Aunque no puedo evitar pensar que ese debería haber sido yo."

hi "Oh, eso es bueno."

hi "Él realmente se preocupa por ti, ¿eh?"

show ev emi_bed_smile
with charachange

"Emi se encoge de hombros."

emi "Es su trabajo."

emi "Parte de ser el capitán significa que sabes dónde están los miembros del equipo cuando no están en la escuela."

emi "Aun así, creo que fue agradable que llamara, ¿eh?"

hi "Síp. Claro que sí."

"Emi bosteza y se retuerce para estar en una posición más cómoda."

show ev emi_bed_normal
with charachange

emi "Así que, ¿cómo estuvo tu día?"

hi "Sin incidentes, ¿sabes?"

hi "Me adelanté y corrí solo, y hablé con el enfermero acerca de cómo estabas…"

stop music fadeout 2.0

scene bg school_dormemi_ni
with shorttimeskip

"Divago a través de los eventos del día, ninguno de los cuales es particularmente fascinante."

"Es ahí cuando soy distraído por un brazo encontrando su camino a través de mi cintura."

"Parece que Emi se durmió mientras yo hablaba así que agarro su manta para cubrirnos."

play music music_comfort fadein 9.0

scene ev emi_sleep_unsure
with locationchange

"Ella se voltea de lado, y una pierna se acomoda sobre las mías, atrapándome eficazmente."

hi "Oye."

"Sería una lástima despertarla, pero tengo otras cosas que hacer."

play sound sfx_rustling

"La sacudo gentilmente, pero en respuesta ella solo tensa más sus brazos sobre mí y suspira un poco."

"Mi resistencia a esta posición se desmorona bastante rápido."

"La sensación de su cuerpo respirando regularmente es tranquilizadora e increíblemente estimulante al mismo tiempo."

"Mi respiración no puede decidir entre relajarse o agitarse."

"Gana el relajamiento, y me encuentro colocando un brazo alrededor de Emi."

scene ev emi_sleep_normal
with dissolve

hi "Creo que estoy enamorado."

"Las palabras se deslizan y flotan en el aire inadvertidas."

"Al menos espero que hayan pasado inadvertidas."

scene ev emi_sleep_weep
with dissolve

"Emi gime débilmente en su sueño, y su abrazo se tensa de nuevo."

"Por primera vez desde que la conozco, veo lágrimas cayendo por el rostro de Emi."

"Se siente como si mi corazón se fuera a partir."

"Instintivamente tenso mi propio brazo y acaricio su cabello en lo que espero sea una manera tranquilizadora."

"Palabras de consuelo, insignificantes en esta situación, surgen en mi mente."

"Quizás debería despertarla. ¿Se supone que despiertes a las personas que están teniendo pesadillas?"

"Por mi propia vida, juro que no lo recuerdo."

"La decisión se me escapa de repente cuando Emi se mueve bruscamente con un grito."

scene ev emi_sleep_cry
with dissolve

emi "¡Papá!"

"Esto es… más de lo que quiero escuchar sin que ella lo sepa. Me apresuro en sentarme derecho y la sacudo gentilmente por los hombros para despertarla."

scene bg school_dormemi_ni
with locationchange

hi "Oye, ¿estás bien?"

"Qué pregunta tan tonta."

show emi basic_shock_gym_close_ni at tworight
with charaenter

emi "¿Eh? ¿Qué?"

show emi basic_hes_gym_close_ni
with charachange

emi "¿Hisao?"

"Sacude la cabeza como para despejarla y se restriega los ojos apresuradamente."

hi "Tuviste una pesadilla. Creo."

show emi sad_shy_gym_close_ni
with charachange

"Emi se estremece de nuevo y mira hacia mí con algo de recelo, como si no estuviera segura de si está despierta o no."

emi "S-sí, supongo."

hi "¿Quieres hablar de ello?"

emi "¿Hmm?"

"Un veloz debate interno parece estar ocurriendo en su cabeza, el cual se resuelve con un encogimiento de hombros."

show emi basic_hes_gym_close_ni
with charachange

emi "Nah, en realidad no recuerdo mucho."

"Estoy seguro de que me está mintiendo, pero por alguna razón no creo que deba presionar el asunto."

show emi sad_shyblush_gym_close_ni
with charachange

"Emi se estremece de nuevo y se vuelve hacia mí, viéndose un poco aturdida."

emi "Perdón por quedarme dormida así."

"Mantengo mi voz lo más calmada que puedo."

hi "Oye, no te preocupes por eso. Has estado enferma."

emi "Sí, supongo que la medicina para el resfriado me pone algo somnolienta."

hi "Me imagino."

"Emi no me parece del tipo de persona que se quedaría dormida por cualquier cosa."

"Rin, tal vez. Pero Emi es demasiado enérgica."

show emi basic_grin_gym_close_ni
with charachange

"Emi medio sonríe a mi respuesta, y así sin más está de vuelta a ser la misma de siempre."

show emi basic_closedgrin_gym_close_ni
with charachange

emi "Bueno, ¡prepárate para mañana por la mañana, Hisao!"

show emi excited_proud_gym_close_ni
with charachange

emi "¡Tendremos que esforzarnos el doble para compensar lo de hoy!"

hi "¡Pero yo fui a correr esta mañana!"

show emi basic_annoyed_gym_close_ni
with charachange

emi "¡Sin excusas!"

hi "Oh, bien, ¡estaré preparado para ti!"

show emi basic_grin_gym_close_ni
with charachange

"Emi asiente, satisfecha."

emi "Bien."

"Tomo esto como mi señal para salir."

hi "Bueno, mejor me voy. Especialmente si quiero dormir lo suficiente para mañana."

show emi basic_grin_gym_ni
with vpunch

"Salgo de la cama y me dirijo a la puerta."

show emi sad_shy_gym_ni
with charachange

emi "Oye, Hisao…"

hi "¿Hmm?"

"Giro completamente sobre mis talones y me vuelvo hacia Emi."

show emi basic_hes_gym_ni
with charachange

"Ella abre su boca para decir algo, y luego de hacerlo, la veo titubear levemente."

"Ella cierra su boca y la vuelve a abrir."

show emi sad_grin_gym_ni
with charachange

emi "… Gracias."

emi "Por la visita, quiero decir."

emi "Eres algo así como el primer visitante que he tenido que no es Rin."

"Eso sí que es sorprendente. Pensaría que Emi tendría gente visitándola todo el tiempo."

"Ella ciertamente es popular, o eso pensé. Siempre hablando con personas en los corredores."

show emi sad_shy_gym_ni
with charachange

"Emi duda de nuevo."

emi "Y gracias por quedarte cuando yo… bueno."

show emi sad_depressed_gym_ni
with charachange

"Una mirada de dolor revolotea en su cara."

emi "Ya sabes."

show emi sad_grin_gym_ni
with charachange

emi "Ayudó."

show emi basic_closedgrin_gym_ni
with charachange

"Ella se anima de nuevo y se despide alegremente."

emi "¡Te veo mañana!"

hi "Sí, te veo luego."

"Estoy a punto de salir por la puerta cuando algo me hace voltearme de nuevo."

hi "Oye, Emi."

show emi basic_grin_gym_ni
with charachange

emi "¿Hmm?"

hi "Cuando quieras hablar, házmelo saber, ¿de acuerdo?"

show emi sad_shy_gym_ni
with charachange

"Emi parece sorprendida por este ofrecimiento."

show emi basic_closedgrin_gym_ni
with charachange

"Su sonrisa se amplía aún más."

emi "Tenlo por seguro, Hisao."

show emi basic_grin_gym_ni
with charachange

emi "¡Te veré en la mañana!"

scene bg school_girlsdormhall_ni
with locationchange

"Salgo de la habitación de Emi con mi cabeza en un remolino."

"¿En serio debería haberme ido?"

"¿Ella realmente estaba bien?"

"Quiero dar la vuelta y marchar de nuevo por el corredor, abrir la puerta y decirle…"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

nvl clear

nvl show dissolve

n "\n\nDecirle que la amo, decirle que pienso que es hermosa, decirle que estaré allí cuando me necesite."

n "Quiero quedarme con ella, sostenerla cerca mientras se duerme de nuevo."

n "¿Cuántas noches se habrá despertado así?"

n "Solo para encontrarse con que no hay nadie allí."

n "Quiero ser la persona con la que ella pueda estar cuando eso suceda."

n "Es un pensamiento tonto, lo sé."

n "No nos conocemos tan bien el uno al otro, ¿verdad?"

n "Toda la idea, así como es estimulante, también me hace sentir preocupado."

n "Preocupado, quizás, de que propase mis límites."

n "Y ahora para añadir a mis problemas, pareciera que Emi ya tiene interés en alguien más."

nvl clear

n "\n\n\n\n\n\nEste capitán suyo que parece tan interesado en su bienestar."

n "Cierto, solo los he visto juntos unas pocas veces, pero eso no cambia el hecho de que parecen más adecuados el uno para el otro."

n "En realidad no hay nada que hacer acerca de eso."

n "Necesito alejar mi mente de toda esta situación."

$ renpy.music.set_volume(1.0, 2.0, channel="music")

nvl clear

nvl hide dissolve

window show

"Tengo tarea que hacer."

"Tal vez eso me distraiga."

stop music fadeout 2.0

$ suppress_window_after_timeskip = True

scene black
with dissolve


label es_E14:

window hide None

scene black
with dissolve

scene bg school_dormhisao
with openeye

window show

"Una noche intranquila me ha dejado sintiéndome bastante aturdido esta mañana."

play music music_drama fadein 8.0

"Los eventos del día anterior siguen invadiendo mi mente."

"El recuerdo de cómo se sentía Emi contra mí."

"El recuerdo de nuestra lucha."

"Y más preocupante, el recuerdo de su pesadilla."

"Ella tenía tanto dolor."

"No puedo dejar de preguntarme cómo será para ella despertarse sin nadie allí."

scene bg school_dormbathroom
show steam
with locationskip

play ambient sfx_shower fadein 1.0

"La ducha me despierta de golpe con agua caliente. Despierto, pero todavía preocupado."

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")
$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

nvl show dissolve

nvl clear

n "\n¿Qué pasará hoy?"

n "¿Las cosas simplemente volverán a la normalidad?"

n "¿Fin del episodio, de vuelta al statu quo?"

n "Hubo una conexión ayer. Algo que casi nos empujó más allá de los lazos de pura amistad."

n "¿Habría sido eso tan malo?"

n "Mi mente regresa a la mirada en los ojos de Emi luego de nuestra pelea con almohadas. Casi parecía como si me retara a seguir."

n "Casi."

n "Pero no lo puedo saber con seguridad."

n "Como sea, el capitán del equipo probablemente esté primero en sus afecciones."

n "Pero incluso mientras digo eso, mi mente ya está resoplando burlonamente. Solo estoy buscando una excusa. Una razón por la que todo podría salir mal."

n "Una razón para no intentarlo."

nvl clear

n "\n\n\n\nNo es como si los hubiera visto juntos fuera de las prácticas de atletismo."

n "Y claramente nunca la ha visitado. La misma Emi lo dijo. Si fueran cercanos, él seguramente la visitaría."

n "Soy un cobarde."

n "Debería atreverme de todas maneras, al diablo con las consecuencias."

n "Eso es lo que Emi haría, creo. Qué demonios, {b}sé{/b} que eso es lo que haría."

n "Y es por eso que estoy parcialmente convencido de que no hay interés de su parte. Ella tampoco ha actuado."


n "Tal vez por este capitán. Es posible que ella tenga algún tipo de romance no correspondido."

nvl clear

n "\n\n\n\n\n\n¿Pero quién sería capaz de aclararme su relación?"

n "Es imposible que sea Emi. Ella probablemente solo reiría y preguntaría por qué quiero saberlo… y aún no estoy listo para responder eso."

n "Rin… Rin probablemente solo me daría una respuesta críptica o algo. Y después con mi suerte, ella le preguntaría a Emi, quien me preguntaría que por qué quiero saberlo, y ya he cubierto ese problema."

n "Me pregunto…"

nvl clear

n "\n\n\n\n\n¿Podría salirme con la mía preguntándole al enfermero? Él se ve muy protector con Emi. Estoy seguro de que sabría si hubiera algo ahí…"

n "Y él me debe una por no dejar que Emi se enterase de que olvidó decirme que ella estaba enferma, así que se quedará callado."

n "Aun así, ¿qué tal si me pregunta por qué quiero saberlo?"

n "Puedo quitármelo de encima. Solo diré que estoy curioso como amigo. Él se lo creerá, ¿cierto?"

n "¡Claro!"

n "Eso está arreglado, entonces."

n "Luego de correr, hablaré con él mientras Emi espera fuera de la oficina."

stop ambient fadeout 2.0

nvl clear

nvl hide dissolve

scene bg school_track
with locationskip

nvl show dissolve

n "\n\n\n\nNo hay señales de Emi cuando llego a la pista. ¿Aún está muy enferma?"

n "Decido darle diez minutos."

n "Llegué un poco temprano, y ella estaba enferma ayer, así que si tarda un poco en aparecerse no debería ser una sorpresa."

n "Aun así, no me gustaría desperdiciar mi tiempo, así que me ocupo en estirar y caminar hacia atrás y adelante con ansiedad."

n "¿Y qué tal si fui demasiado lejos ayer?"

n "¿Y qué tal si ella no viene porque está avergonzada?"

n "Qué tal si…"

$ renpy.music.set_volume(1.0, 2.0, channel="music")
$ renpy.music.set_volume(1.0, 2.0, channel="ambient")

nvl clear

stop music fadeout 2.0

nvl hide dissolve

window show

show emi basic_closedgrin_gym at center
with charaenter

emi "¡Llegaste temprano de nuevo, Hisao!"

show emi excited_proud_gym
with charachange

emi "¡Estoy impresionada!"

"Así de fácil, siento algo de tensión abandonando mi cuerpo."

"Emi se ve alegre y animada como siempre, sin siquiera dar señas de haber estado enferma el otro día, menos aún de no haber descansado bien al dormir."

"Aun así, tengo que preguntar."

hi "¿Dormiste bien anoche?"

play music music_serene

"Es solo una pregunta rápida. Parloteo trivial."

"La clase de cosas que preguntan las personas cuando se encuentran en la cafetería mientras toman su café de la mañana."

"Pero no para nosotros. Al menos, no para mí."

"No sé si Emi se da cuenta de que estoy realmente preocupado por qué tan bien durmió anoche, pero la pregunta la hace detenerse."

show emi basic_grin_gym
with charachange

"Después de un momento en el que parece reflexionar genuinamente sobre esto, asiente."

show emi basic_closedhappy_gym
with charachange

emi "¡Síp! ¡Claro que sí!"

"¿Fue por mí?"

"¿Realmente ayudé?"

"¿O solo dices eso para hacer que deje de preguntar?"

hi "Es bueno saberlo."

show emi basic_closedgrin_gym
with charachange

"Emi sonríe y empieza a calentar."

show emi basic_grin_gym
with charachange

emi "Entonces, ¿preparado para empezar?"

hi "Pfft, ¿que si estoy preparado? ¡Claro que estoy preparado! ¡Nací preparado!"

show emi basic_closedhappy_gym
with charachange

"Emi se ríe de mi fanfarronería, y comenzamos a correr."

scene bg school_track_running
with shorttimeskip

"Mantengo un ritmo estable todo el tiempo, respirando firmemente."

scene bg school_track_on
with Dissolve(2.0)

"Aún me siento muerto al final, pero al menos ahora no jadeo como un pez fuera del agua."

show emi basic_happy_gym:
    center
    xpos 0.6
    easein 0.5 center
with charaenter

"Emi resplandece alegremente luego de la carrera de hoy."

emi "¡Buen trabajo, Hisao! ¡Estás mejorando!"

show emi basic_closedgrin_gym
with charachange

emi "¡Serás la mitad de rápido que yo en poco tiempo!"

"Esta última línea la dice con la sonrisa provocadora a la que tanto me he acostumbrado."

hi "Oh, qué emocionante."

play ambient sfx_emisprinting

$ renpy.music.set_volume(0.3,1.0,channel="ambient")

hide emi
with easeoutleft

"Emi empieza con sus sprints mientras yo doy una vuelta de enfriamiento."

"Ella realmente se está esforzando hoy."

stop ambient fadeout 1.0

scene bg school_track
with shorttimeskip

$ renpy.music.set_volume(1.0,0.0,channel="ambient")

"Para el momento en que he terminado con mi vuelta, ella está tendida en las gradas, viéndose exhausta."

hi "Cielos, no te estarás exigiendo demasiado el día de hoy, ¿verdad?"

hi "Acabas de tener un resfriado, como podrás recordar."

show emi basic_annoyed_gym at center
with charaenter

"Emi lanza un resoplido molesto y se sienta."

emi "¡Bah! Solo intento recuperar el tiempo perdido, eso es todo."

show emi excited_happy_gym
with charachange

emi "Hoy me esforcé el doble, sabes."

show emi excited_laugh_gym
with charachange

emi "Una buena carrera siempre ayuda con las molestias, sabes."

show emi basic_closedgrin_gym
with charachange

emi "Despeja la mente, también."

hi "¿Oh?"

show emi excited_happy_gym
with charachange

"Emi asiente vigorosamente."

show emi excited_amused_gym
with charachange

emi "¡Síp! Es un gran escape para ese tipo de cosas."

"Ella no explica más, y yo no pregunto."

"Sospecho que sé la verdadera razón por la que se esforzó tanto hoy."

"Estar enferma no tiene nada que ver con eso. Algo la está molestando."

"Tal vez la pesadilla. Tal vez algo más."

"Pero no me corresponde fisgonear aquí."

"Ella me lo diría si quisiera que yo lo supiese."

hi "Estoy seguro de que es útil."

show emi basic_grin_gym
with charachange

emi "No tienes ni idea."

"La sinceridad en su voz confirma mis sospechas."

"El único problema es…"

"Incluso sabiendo que ella me lo diría si quisiera que yo lo supiese, sigo queriendo saberlo."

hi "Entonces, ¿tienes algo en mente?"

"Emi no parece sorprendida por mi pregunta."

show emi basic_closedgrin_gym
with charachange

"En vez de eso, se encoge de hombros."

show emi sad_grin_gym
with charachange

emi "Nah, no es nada por lo que valga la pena preocuparse."

"Parece como si intentara convencerse a sí misma tanto como intenta convencerme a mí."

"Abro mi boca para preguntar si lo de ayer es responsable de su estado mental actual, pero lo pienso mejor."

"Demasiado riesgo de que tome la pregunta de la manera equivocada."

"Además, ni yo mismo estoy seguro de qué pensar respecto a lo de ayer."

"En realidad solo puedo llegar lo suficientemente lejos como para pensar en cómo se sentía el tener a Emi durmiendo junto a mí antes de que mi cerebro colapse."

"Tenerla frente a mí ahora, cubierta en sudor y mirándome perversamente, hace que se me dificulte pensar."

hi "Sí, entiendo."

show emi basic_hes_gym
with charachange

emi "Será mejor que nos apresuremos para ver al enfermero. Nos estamos quedando sin tiempo."

hi "¿Acaso no es siempre igual?"

show emi basic_grin_gym
with charachange

"Emi se ríe por esto, una risilla seca que parece muy impropia de ella."

show emi sad_grin_gym
with charachange

emi "Demasiado cierto."


"Por un breve instante, ella se ve mayor, desgastada por una vieja herida."

"Pero igual que ayer casi puedo verla asumir la carga y enderezarse ligeramente."

"Y luego regresa a ser Emi de nuevo."

show emi excited_proud_gym
with charachange

emi "Vamos, Hisao. ¡Una carrera!"

play ambient sfx_emisprinting

hide emi
with easeoutleft

stop ambient fadeout 2.0

"Con una repentina sonrisa, sale disparada."

hi "¡Oye! ¡No es justo!"

"Salgo detrás de ella, sabiendo que no la alcanzaré pero no me preocupo."

"Incluso si no hay esperanza de alcanzarla, todavía correré detrás de ella."

stop music fadeout 2.0

scene bg school_nursehall
show emi basic_grin_gym at center
with locationskip

"Emi está esperándome en la puerta cuando llego."

show emi basic_closedhappy_gym
with charachange

emi "Vaya vaya, ¡miren quién se apareció al fin!"

hi "Sí, sí."

hi "Disfruta de tu victoria mientras puedas."

show emi basic_closedgrin_gym
with charachange

"Emi sonríe mientras el enfermero asoma la cabeza por la puerta."

show nurse neutral:
    center
    xpos 0.0 xanchor 0.5
    easein 0.5 xpos 0.1
with charaenter

nk "Vaya, ahí estás."

nk "Entra, Hisao."

play music music_nurse fadein 1.0

scene bg school_nurseoffice
show nurse neutral at center
with locationchange

"En lo que se ha vuelto una rutina familiar a estas alturas, revisa mi presión sanguínea y mi frecuencia cardíaca."

show nurse fabulous
with charachange

nk "Estás un poco acelerado hoy, ¿no?"

hi "Sí, hice una especie de carrera con Emi hasta acá."

show nurse grin
with charachange

"El enfermero se ríe."

nk "¡Eso nunca es buena idea!"

show nurse neutral_close
with characlose

"Él se aproxima para susurrarme algo de manera conspiratoria."

show nurse fabulous_close
with characlose

nk "No sé si lo has oído… pero Emi es algo así como una estrella de atletismo."

show nurse fabulous
with vpunch

"Retrocedo fingiendo sorpresa."

hi "¿En serio? ¡Ella nunca lo mencionó antes!"
show nurse grin
with charachange

"Los dos compartimos una carcajada."

show nurse neutral
with charachange

nk "¿Ella lo hizo bien hoy?"

nk "¿El resfrío parecía molestarla?"

hi "¿Por qué no le preguntas a ella?"

show nurse concern
with charachange

"Él pone los ojos en blanco, exasperado."

nk "Claro que le preguntaré a ella también, pero me dirá que no tuvo ningún problema, sin importar si tuvo alguno o no."

show nurse fabulous
with charachange

nk "Así que te pregunto a ti, porque eres su amigo y probablemente me dirías si ella tuvo algún problema hoy."

"Cuando lo pone de esa manera, tiene mucho más sentido."

hi "Ella se veía bastante bien hoy, quizás un poco más cansada que de costumbre."

hi "Ya estaba sintiéndose mejor cuando pasé a verla ayer, así que no estoy tan sorprendido."

show nurse neutral
with charachange

"El enfermero asiente, aunque noto que se tensa levemente cuando menciono la visita de ayer."

nk "Bien, es bueno saberlo."

nk "Pensé que sería algo de 24 horas. Emi tiende a recuperarse rápidamente de resfriados y cosas así."

hi "Oye, hablando de Emi…"

hi "¿Ella y el capitán del equipo están…? Bueno, ya sabes."

show nurse fabulous
with charachange

"Una mirada de sospecha cruza su rostro."

nk "¿Por qué preguntas?"

hi "Bueno, es que parecen ser algo cercanos, y tan solo tengo curiosidad, ¿sabes?"

hi "Y nunca se lo preguntaría a ella, porque sería algo vergonzoso."

"Hasta aquí todo bien. Ahora para convencerlo totalmente."

hi "Además, pienso que hacen una linda pareja."

show nurse grin
with charachange

"El enfermero se ríe."

nk "Bueno, no creo que seas el primero en pensar eso."

nk "Pero creo que puedo decir con cierta certeza que ellos dos nunca harán algo como eso."

hi "¿Con certeza?"

show nurse neutral
with charachange

nk "Síp."

show nurse fabulous
with charachange

nk "No es que te lo pueda decir, claro. Confidencialidad y todo eso."

hi "Sí claro, solo estás ocultándome un secreto."

show nurse grin
with charachange

nk "Eso también."

show nurse neutral
with charachange

nk "Bien. Sal de aquí. Soy un hombre ocupado, sabes."

stop music fadeout 2.0

scene bg school_nursehall
show emi basic_grin_gym at center
with locationchange

"Pongo los ojos en blanco ante esta última declaración y salgo por la puerta, señalándole a Emi que entre."

show emi basic_grin_gym:
    center
    easeout 0.5 xpos 0.4 alpha 0.0
with Pause(0.5)

hide emi
with None

"Todo ese tiempo, estoy intentando evitar hacer una danza de celebración."

window hide

play music music_running

centered "Ellos dos nunca harán algo como eso."

window show

"Esa es exactamente la clase de cosas que quería escuchar."

"Estoy medio tentado a hacer algún tipo de movimiento con Emi justo ahora, pero creo que el enfermero lo desaprobaría."

"Además, todavía no sé con exactitud qué siente Emi hacia mí."

"Quiero decir, es obvio que se preocupa por mí como un amigo, ¿pero podría ser algo más que eso? No puedo estar seguro."

"Aun así, no puedo evitar sentirme esperanzado. Solo necesito encontrar un buen momento para decirle a Emi cómo me siento."

"Ese acertijo debería mantenerme ocupado por el resto del día, por lo menos."

stop music fadeout 6.0


label es_E15:

scene bg school_nursehall
with None

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 1.0

scene bg school_roof
with shorttimeskip

"La azotea está completamente desierta."

"Normalmente contaría con que Rin esté acá arriba antes que yo, pero está extrañamente ausente."

"Me pregunto si al fin decidió acompañar a Emi a la cafetería. Eso parece muy improbable, pero es en todo lo que puedo pensar en estos momentos."

"Parte de mí quiere ir a buscar a Rin, pero una parte considerablemente mayor de mí está demasiado complacida con la forma en la que se siente el sol en mi piel como para importarle."

"Manoseo mi comida ociosamente mientras espero a que Emi y Rin se aparezcan."

"No toma mucho tiempo para que escuche los sonidos de alguien subiendo por las escaleras."

$ renpy.music.set_volume(0.5, 0.0, channel="sound")
play sound sfx_door_creak

"Espero hasta que la puerta empiece a abrirse antes de hablar."

hi "Les tomó bastante tiempo."

hi "Mantenerme aquí esperándolas, en serio."

hi "Ustedes dos son…"

hi "¿Eh?"

"Bueno, eso es extraño."

show emi basic_confused at center
with charaenter

"La única persona de pie frente a la puerta es Emi, quien se ve algo confusa."

emi "¿A qué te refieres con “eh”?"

show emi basic_grin
with charachange

emi "¡Soy yo! Ya sabes, ¡Emi! Corremos por las mañanas."

"Ella sonríe, y siento mi corazón brincar ligeramente en mi pecho ante la imagen."

hi "Sí, eso lo sabía. Solo estoy confundido…"

hi "… ¿Dónde está Rin?"

show emi sad_depressed
with charachange

"La sonrisa de Emi es reemplazada por una expresión de profunda culpabilidad."

emi "Sí, acerca de eso…"

emi "Es que… de algún modo…"

show emi sad_shy
with charachange

emi "Lepasémiresfriado."

play music music_another fadein 0.5
$ renpy.music.set_volume(1.0, 0.0, channel="sound")

hi "Oh, cielos."

hi "¿También estoy en peligro?"

"Tendría sentido, después de todo. Emi y yo estuvimos en estrecho contacto el otro día…"

"¿Entonces qué hicieron ella y Rin para que esta última se enfermara?"

"…"

"Calma, viejo verde. No vayas por ese camino."

"Probablemente Rin solo tiene un sistema inmunológico más débil que el mío."

show emi basic_shock
with charachange

"Emi parece sorprendida por mi comentario, como si no hubiera considerado eso antes."

emi "¡Espero que no!"

show emi excited_sad
with charachange

emi "¡Me sentiría terrible si te enfermaras por mi culpa, Hisao!"

hi "Oh, cielos, creo que siento que me va a dar fiebre…"

show emi sad_annoyed
with charachange

"Emi se ve horrorizada, y rápidamente cambia a una expresión más enojada."

emi "¡Hisao!"

emi "¡Deja de sentirte enfermo en este instante!"

show emi basic_annoyed
with charachange

emi "¡No te lo permito!"

show emi basic_annoyed_close
with vpunch

"Ella me sacude impulsivamente por el cuello de la camisa."

emi "¿Me estás escuchando, sistema inmunológico de Hisao?"

show emi sad_angry_close
with charachange

emi "¡Mueve el trasero y ponte en marcha!"

"Le doy un pulcro saludo."

hi "Copiado, mi señora."

show emi basic_grin
with charadistant

"Emi retrocede y asiente, satisfecha."

show emi basic_closedgrin
with charadistant

emi "Bien."

show emi basic_happy
with charadistant

emi "No se te está permitido perderte ninguna de nuestras carreras matutinas, después de todo."

hi "¡Pero tú te perdiste una!"

show emi sad_annoyed
with charachange

"Emi se cruza de brazos y me mira altivamente."

emi "Sí, pero ese es un caso especial. Era yo, y no tú."

hi "Esa no es una verdadera explicación."

show emi basic_confused
with charachange

"Emi se ve asombrada."

emi "Estás bromeando, ¿verdad?"

show emi basic_annoyed
with charachange

emi "¡Esa explicación tiene perfecto sentido!"

hi "¡No lo tiene! ¡Es un descarado estándar de doble moral!"

show emi sad_annoyed
with charachange

emi "No veo qué tiene que ver eso con nada de esto."

hi "Oh, bueno."

show emi basic_closedgrin
with charachange

"Emi parece complacida por su victoria."

hi "De todas formas, ¿Rin se pondrá bien? No está terriblemente enferma, ¿verdad?"

show emi basic_grin
with charachange

"Emi sacude la cabeza."

emi "¡Nop! Estará bien."

show emi excited_proud
with charachange

emi "Le conseguí algo de medicina para resfriados que debería ayudarla."

show emi basic_hes
with charachange

emi "Aunque debería haberme asegurado de que no intentara tomarlas todas a la vez…"

show emi basic_grin
with charachange

emi "Lo ha hecho antes, sabes."

"Por algún motivo no me parece tan sorprendente."

"Dudo que Rin sea alguien que le preste atención a las dosis máximas o cosas similares."

hi "Entonces quizás deberías pasar a verla más tarde. Solo para estar seguros."

show emi sad_grin
with charachange

"Emi se encoge de hombros."

emi "Pasaré luego de la práctica. Estará bien hasta entonces."

"Asiento, comprendiendo que esta línea de conversación ha terminado."

"El único problema es, no sé de qué más hablar."

hi "Entonces…"

hi "¿Tienes más competencias de atletismo próximamente?"

window hide

nvl clear

nvl show dissolve

n "\n\n\n\n\n\n\n\nEsta es una manera terriblemente indirecta de intentar averiguar si ella está libre el fin de semana."

n "Si está libre, entonces tal vez pueda pedirle una cita o algo."

n "Bueno, asumiendo que realmente pueda formar las palabras."

nvl clear

nvl hide dissolve

window show

show emi basic_grin
with charachange

"Emi sacude su cabeza."

show emi basic_closedgrin
with charachange

emi "Nah, no por otro par de semanas, creo. La temporada está terminando."

"Oh, sí. Llegué a mitad de todo, ¿verdad?"

"¿Significa eso que los exámenes están muy cerca? Probablemente debería averiguar eso."

hi "¿Qué haces los fines de semana si no tienes una competencia?"

show emi excited_proud
with charachange

"Una ceja se levanta, y el rostro de Emi adquiere una mirada burlona."

emi "Estás realmente curioso el día de hoy, ¿verdad?"

"Me encojo de hombros y espero que se vea casual."

hi "Solo intento tener una conversación."

hi "No sé cómo es ser una estrella de atletismo, después de todo."

show emi basic_closedgrin
with charachange

emi "Pfft, adulador."

"Ella mueve una mano perezosamente."

show emi basic_grin
with charachange

emi "No soy tan buena, sabes."

show emi basic_closedhappy
with charachange

emi "Solo sucede que me viste en un buen día, es todo."

hi "Mentirosa."

show emi sad_grin
with charachange

stop music fadeout 6.0

emi "Jeje, sí."

emi "Pero la humildad es la señal de un buen atleta."

show emi sad_depressed
with charachange

emi "O al menos eso es lo que mi padre solía decir."

"Se encoge de hombros e intenta ocultar sin éxito la expresión de preocupación que ha aparecido en su cara."

hi "Oye, ¿qué pasa? Pareces preocupada por algo."

"Emi empieza a negarlo, luego suspira derrotada."

"Me pregunto si está demasiado cansada de estar obligándose a negarlo como siempre."

"O si a estas alturas realmente confía lo suficiente en mí como para sincerarse."

show emi sad_shy
with charachange

play music music_comfort fadein 9.0

emi "Bueno, ¿recuerdas lo de anoche?"

"Cómo podría no hacerlo. Decido asentir, de todas formas."

show emi sad_depressed
with charachange

emi "Esa no es la primera vez que me ocurre."

emi "De hecho, me ocurre a…"

"Ella se detiene, como si repentinamente hubiera caído en la cuenta de lo que hace."

"Es casi como si estuviera rompiendo algún tipo de regla personal aquí."

"Pero empieza de nuevo, escogiendo sus palabras cuidadosamente."

emi "Bueno, no a menudo, pero…"

show emi sad_shy
with charachange

emi "En ocasiones."

emi "Tan solo ha sido una de esas semanas en las que ocurre."

show emi sad_depressed
with charachange

"Se le escapa un suspiro, y se ve terriblemente frustrada."

show emi sad_shy_close
with characlose

"Me acerco y le doy un abrazo, el cual, a diferencia de la última vez, no parece sorprenderla."

"En vez de eso, parece relajarse cuando mis brazos se cierran en torno a ella."

"Permanecemos así por un rato."

hi "Oye, sabes que estaba siendo sincero anoche."

hi "En serio puedes hablar conmigo cuando estas cosas te estén molestando. Siempre es difícil enfrentarse a este tipo de cosas solo, ¿sabes?"

show emi sad_grin_close
with charachange

"Emi sonríe y rompe el abrazo, pero sigue apoyándose en mi hombro."

emi "Gracias, Hisao."

show emi basic_grin_close
with charachange

emi "Estaré bien, creo."

"Ya puedo verla recuperándose, lista para sellarlo todo de nuevo."

"Supongo que ese asunto ya está cerrado."

hi "Entonces, ¿has reflexionado sobre ese cuestionario de orientación profesional?"

show emi basic_closedgrin_close
with charachange

emi "No puedo decir que lo haya hecho."

show emi basic_grin_close
with charachange

emi "No suelo planificar muy a futuro, sabes."

emi "Aunque supongo que al menos podría comenzar a planificar la universidad, ¿eh?"

"Me encojo de hombros."

hi "Supongo, a menos de que hablaras en serio acerca del asunto de los piratas."

hi "La última vez que me fijé, los piratas no tenían mucha necesidad de universidades."

hi "A menos de que haya algo así como una universidad de piratas por ahí en algún lugar."

show emi basic_closedgrin_close
with charachange

"Emi suelta una risita y empieza a verse igual que antes, pero hay un nuevo elemento en su expresión."

"Travesura. Así es como lo describiría."

"Emi se ve traviesa, observándome hacia arriba con su cabeza recostada en mi hombro."

show emi sad_grin_close
with charachange

emi "¿Vendrías conmigo si yo decidiera ser una pirata?"

hi "¡Claro que lo haría!"

hi "¿Quién en su sano juicio rechazaría la oportunidad de ser un pirata contigo?"

show emi basic_grin_close
with charachange

emi "Bueno, si lo dices de esa manera, no estoy segura."

show emi basic_closedgrin_close
with charachange

"Suelta una risita de nuevo."

"Noto que mi corazón parece haberse acelerado. Probablemente sea por la proximidad de Emi."

"Ese toque de fresas, de nuevo."

"No puedo evitar sonreír cuando miro hacia abajo."

"Ella está feliz de nuevo."

show emi sad_shy_close
with charachange

emi "Oye, Hisao."

hi "¿Hmm?"

show emi sad_grin_close
with charachange

emi "Si vas a besarme, deberías hacerlo pronto. Creo que la campana del almuerzo está a punto de sonar."

stop music fadeout 1.0

"Mis pensamientos se oprimen hasta detenerse."

"Estoy seguro de que mi boca está abierta por la sorpresa."

"Todo lo que consigo decir es un sofocado “¿Eh?”"

show emi basic_closedgrin_close
with charachange

"Esto divierte a Emi aún más."

show emi excited_proud_close
with charachange

emi "Estabas pensándolo, ¿verdad?"

"Ella se endereza, acercando su rostro al mismo nivel que el mío."

show emi basic_grin_close
with charachange

emi "Probablemente lo disfrutaría, ¿sabes?"

show emi sad_grin_close
with charachange

emi "Eres realmente…"

show emi sad_shy_close
with charachange

emi "… Bueno."

"Ella se recompone por un momento, al parecer a punto de decir algo importante."

show emi sad_grin_close
with charachange

emi "Si no te has dado cuenta aún, creo que me he enamorado un poquito de ti."

show emi basic_grin_close
with charachange

emi "Tendrás que hacer algo al respecto."

"Esta vez su sonrisa provoca cortocircuitos en varios procesos importantes de mi cerebro."

"En algún momento me volví hacia ella, y en algún otro momento sus brazos se movieron alrededor de mi cuello."

"E incluso en algún otro momento, mis brazos la agarraron por la cintura."


"Mentiría si pudiera decir precisamente cuándo pasó eso."

"Porque de momento, solo hay una voz en mi cabeza gritándome que la bese."

"Miro hacia los ojos de Emi."

"Ahí está."

"Lo que vi ayer en la cama. Está allí de nuevo."

"De repente me doy cuenta de que ella está preocupada de que yo la rechace."

stop ambient fadeout 1.5

"Qué preocupación tan tonta de su parte."

window hide

play music music_romance fadein 0.5

scene white
show ev emi_firstkiss:
    truecenter
    zoom 4.0 rotate 20 subpixel True
    0.7
    linear 0.3 zoom 1.1 rotate 0
    easein 12.0 zoom 1.0
with GenericWhiteout(0.5, 0.2, 2.0)

with Pause (5.0)

nvl clear
nvl show dissolve

n "\n\n\n\nSus labios saben ligeramente a fresas."

n "Ella se acerca más, y sus brazos se tensan alrededor de mi cuello, asegurándose de que yo no retroceda."

n "No es como si hubiera algún peligro de eso."

n "Hay una agitación en mi interior."

n "El mundo se cae."

n "Solo estamos ella, yo, y esta banca."

n "Mis brazos se tensan, acercando su cintura, en trance por sentirla a ella."

n "Inhalo su esencia, mi mente intenta desesperadamente memorizar todo sobre ella; cómo sabe, cómo huele, cómo se siente."

play sound sfx_warningbell
play ambient sfx_rooftop fadein 4.0

nvl clear

nvl hide dissolve

scene bg school_roof
show bg school_roof_blurred as overlay:
    center
    linear 6.0 alpha 0.0
show emi sad_shyblush_close
with silentflash

window show

"El tintineo de la campana nos regresa de golpe a la realidad, y rompemos el beso."

"Las mejillas de Emi están ligeramente coloradas, y ella parece estar recuperando el aliento. En su defensa, yo también lo estoy."

"Nos quedamos ahí por unos segundos, intentando que nuestras cabezas entiendan lo que acabamos de hacer."

"Emi es la primera en romper el silencio."

show emi sad_grin_close
hide overlay
with charachange

emi "Entonces…"

show emi basic_closedgrin_close
with charachange

emi "… ¿Quieres comer algo luego de que termine con la práctica?"

hi "Qué coincidencia."

hi "Estaba a punto de preguntarte lo mismo."

"Bueno, en realidad pensaba que iba a ser algo así como una cita formal el fin de semana o algo. Pero el pensamiento estaba ahí, creo."

with vpunch

"Emi me da un empujoncito juguetón."

show emi basic_happy_close
with charachange

emi "Sí claro."

show emi basic_closedhappy_close
with charachange

emi "Aún estabas aturdido por lo increíblemente buena que soy besando."

"Empezamos a bajar las escaleras de vuelta a nuestros salones de clase respectivos."

stop ambient fadeout 2.0

scene bg school_hallway3
show emi sad_grin at center
with locationskip

hi "Oye, tampoco te vi hablando inmediatamente después."

show emi basic_closedgrin
with charachange

emi "Cierto."

show emi basic_closedhappy
with charachange

emi "Te veo luego de la práctica, Hisao."

show emi basic_closedgrin_close
with charachange

show emi basic_closedgrin_close:
    center
    easeout 0.5 xpos 0.6 alpha 0.0
with None

"Ella se inclina repentinamente y me da un beso rápido en medio del corredor, enviándome a otro momentáneo episodio de caída libre mental."

scene bg school_scienceroom
with locationchange

"Mientras me dirijo a mi salón, una risueña Misha me saluda."

show misha hips_grin at center
with charaenter

mi "¡Vaya, Hicchan, tan romántico, tú~!"

mi "¿Te confesaste en la azotea? ¿Lo hiciste~?"

hi "Eh, de hecho creo que fue al contrario."

show misha cross_laugh
with charachange

"Esto provoca un refrescante ataque de risa en Misha."

show misha hips_grin
with charachange

mi "Amor de jóvenes, es tan impredecible, ¿verdad~?"

"Siendo Misha, supongo que debía esperar que me molestara de esta manera."

hi "Supongo…"

show misha hips_grin:
    center
    easeout 0.5 xpos 0.4 alpha 0.0
with None

"Antes de que realmente pueda responder, Mutou ha entrado en el salón y Misha se va a su asiento, riéndose en el proceso."

"Sospecho que tendré un montón de conversaciones así ahora, especialmente si tengo en cuenta cómo Emi me besó en medio del corredor."

"Pero por alguna razón, no me preocupo por eso."

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
stop music fadeout 5.0

"Por primera vez desde que llegué aquí, mi corazón se siente ligero."

window hide

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
