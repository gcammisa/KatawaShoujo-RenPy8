label fr_A25:

window hide None
scene black
with dissolve

play sound sfx_alarmclock

scene bg school_dormhisao
with openeye

window show


"Mon réveil se déclenche, et je le maudis inutilement pendant un moment jusqu'à ce que je me rappelle que j'avais décidé de donner une autre chance au jogging du matin."


"Je ne sais pas si c'est une si bonne idée, mais je suis déterminé à continuer."


"Ça concerne ma santé, après tout."


"Bien sûr, c'était pas génial pour moi ces derniers temps, mais ça ne rend pas mon existence intolérable au point de ne pas tout essayer pour rester en bonne santé."


"D'ailleurs, il s'agit surtout d'avoir une sorte de contrôle sur ce truc, nan ?"


"Si je peux gérer ça, eh bien, je peux gérer n'importe quoi."


"Du moins c'est ce que je continue de me dire."

scene bg school_track
with locationskip

play ambient sfx_emirunning fadein 0.3


"Encore une fois, il se trouve que je ne suis pas le seul à aller courir."


"Emi est apparemment là depuis un certain temps."


"On dirait qu'elle a déjà eu une bonne suée."


"Mais à quel moment au juste est-ce qu'elle est arrivée ici d'ailleurs ?"

stop ambient fadeout 0.3

show emi basic_grin_gym at center
with charaenter

play music music_emi fadein 0.5


emi "Oh c'est toi !"

show emi basic_closedgrin_gym
with charachange


emi "Je suis surprise de te revoir !"


hi "Pourquoi ça ?"

show emi basic_grin_gym
with charachange


emi "Eh bien, peu de gens arrivent à venir faire un deuxième essai."

show emi basic_annoyed_gym
with charachange


"Elle fronce les sourcils, apparemment gênée par cette pensée."


emi "Comme le reste de l'équipe d'athlétisme, par exemple."


emi "Cela dit, c'était seulement sur une base volontaire, alors c'est pas si étonnant."


emi "Et c'est vraiment tôt le matin..."


"Un haussement d'épaules, et soudainement, il semble qu'elle ait oublié de quoi elle parlait."

show emi basic_happy_gym
with charachange


"Le froncement de sourcils disparaît entièrement, et elle semble se remettre très vite de sa dernière pensée."


emi "Bon ! On y va, alors !"


hi "Quoi ?"

show emi excited_proud_gym
with charachange


emi "T'es revenu ici pour courir, hein ?"


hi "Bah, oui."

show emi basic_closedhappy_gym
with charachange


emi "Alors allons-y !"

scene bg school_track_on
with locationchange


"Je me retrouve soudain saisi et tiré brusquement sur la piste."

play ambient sfx_emijogging fadein 0.3

scene bg school_track_running
with locationchange


"Les choses semblent être une copie de la course d'hier."


"J'ai du mal à tenir le rythme, pendant qu'Emi court avec une aisance que je trouve enviable."


"C'est très gênant, d'être aussi vite épuisé."


"Je sais que je devrais être patient, gravir les marches une par une, mais..."


"C'est difficile de rester positif à ce sujet."


"Nous avons fait le tour de la piste et commençons notre second tour."

play ambient sfx_emirunning


"Emi semble en avoir marre d'aligner son rythme sur le mien, et commence à aller plus vite."


"C'est là que j'ai abandonné hier."



label fr_choiceA25:
menu:
    with menueffect
    "Serai-je capable d'en faire plus ?"
    "C'est parti.":





        return m1
    "C'est pas la peine.":


        return m2

label fr_A25a:



stop music fadeout 10.0


"Je laisse Emi y aller à son propre rythme, et elle ne montre aucune pitié, gagnant une moitié de tour par rapport à moi en un instant."


"Je ne l'en blâme pas."


"Je veux dire, ce n'est pas comme si je faisais vraiment une course avec elle, hein ?"


"À la place, je cours juste à un rythme soutenu, ce que je suis censé faire, hein ?"


"Ce n'est pas utile de repousser mes limites à ce niveau."


"Et puis, est-ce encore la peine ?"

scene bg school_track_on
with locationchange


"Pendant que nous finissons le deuxième tour, je flanche encore."


"Emi continue, et il me semble presque qu'elle est déçue."


"Bah, c'est idiot."


"Je n'ai rien à lui prouver — à y penser, je n'ai rien à me prouver à moi-même non plus, d'ailleurs."


"Je suis bien comme je suis."


"Et je ne suis pas un coureur."


"C'était probablement une mauvaise idée."


"Peut-être qu'il y a quelque chose d'autre que je peux faire à la place."


"Se lever tôt c'est chiant de toute façon. Il y a forcément d'autres moyens de rester en bonne santé."


"Marcher, peut-être. Une bonne promenade d'après-midi."


"Ouais, ça me semble bien. Courir n'est pas pour moi."

stop ambient fadeout 2.0

scene bg school_track
with locationchange


"Je fais un signe d'au revoir à Emi et me dirige vers ma chambre."


"Je penserai à autre chose plus tard."





label fr_A25b:


"Qu'est-ce que je fais là ?"


"Je suis vraiment en train de plier et de laisser Emi prendre la tête ?"

scene bg school_track_running
with locationchange


"J'augmente ma vitesse."


"Le second tour est vite fait, et sans même m'en rendre compte, je continue d'avancer."


"Emi regarde par-dessus son épaule et sourit."

show emi excited_proud_gym at twoleft
with charaenter


emi "Toujours là ?"


hi "Je ne voudrais *huh* pas que tu *huh* penses que je ne suis pas en forme. *huh*"

show emi excited_laugh_gym
with charachange

hide emi
with charamoveoutleft

play ambient sfx_emipacing


"Emi rit — sans casser son rythme, ni le ralentir — et accélère encore."


"Eh bien, si c'est comme ça que tu veux jouer..."


"J'augmente mon propre rythme aussi."


"Je peux sentir mes poumons brûler, et mes jambes commencent à s'interroger sur ce que je suis en train de leur faire faire."


"L'acide lactique crie dans mes muscles, mais je n'écoute pas."


"Je ne peux pas laisser tomber, ça serait perdre."


"La voix rationnelle dans ma tête me demande à quel moment on a commencé à jouer à ce jeu."


"J'aimerais y répondre, mais j'ai beaucoup de difficulté à réfléchir à l'heure actuelle."


"Elle est si {b}rapide{/b}."


"Mais comment est-ce qu'elle—{w=1.5}{nw}"

stop music fadeout 0.2

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)


"C'est comme une chaîne tirant sur ma poitrine, une sensation d'étroitesse étouffante et de douleur."


"Avant que je puisse penser à autre chose que “Oh merde” la piste se dérobe sous mes pieds."

scene bg school_track_on:
    xalign 0.5 yalign 0.52 rotate 0 zoom 1.0
    linear 0.1 rotate -6 zoom 1.2
with vpunch


"Je m'effondre, une main s'accrochant à ma poitrine, l'autre s'appuyant sur le sol pour éviter que je m'écrase le visage."

stop ambient fadeout 0.2


"Emi fait volte-face et écarquille les yeux."


emi "Hisao !"

play ambient sfx_emisprinting


"Elle hurle vers moi, courant dans l'autre sens de la piste."

show emi basic_shock_gym:
    xalign 0.5 yalign 0.7 rotate -6 zoom 1.2
with charamoveinright

stop ambient fadeout 0.1


emi "Qu'est-ce qui ne va pas ?"


hi "Nngh—Rien, juste..."

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)


"Garde ta respiration régulière."


"Reste calme. Ne panique pas."

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)


"Ne panique pas."

show emi basic_shock_gym:
    parallel:
        linear 0.2 rotate -12 zoom 1.5
    parallel:
        "emi basic_hes_gym" with Dissolve(0.2, alpha=True)
with None


emi "Tu as besoin que j'aille chercher l'infirmier ?"

show black
with shuteyefast

scene black
with None


"Je ferme les yeux, me coupant du monde extérieur."

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


"Mon cœur retrouve son rythme normal."


"Doucement, la douleur dans ma poitrine commence à se calmer."


"Et ça finit par partir comme c'est arrivé."


"Ce n'était... rien ? Non, quelque chose est arrivé, clairement.."

play music music_rain fadein 2.0

scene bg school_track_on
show emi basic_hes_gym_close at center
with openeye


"J'ouvre les yeux une nouvelle fois et voit une Emi très inquiète."


hi "Je crois que je vais bien."


"Ma voix semble étrange même pour moi, curieusement très plate. Ça provoque un froncement de sourcils chez Emi."

show emi sad_annoyed_gym_close
with charachange


emi "Je crois pas que tu ailles bien."


"Elle semble prendre une décision, et hoche la tête pour elle-même."

show emi basic_annoyed_gym_close
with charachange


emi "Bien. Tu viens avec moi."


emi "Tu dois voir l'infirmier."

with vpunch


"Emi saisit mon bras et m'aide à me relever. Je me sens un peu bancal, mais je refuse l'offre d'Emi de m'épauler."


"Honnêtement, je suis un peu honteux de ma propre faiblesse."


"J'aimerais mieux qu'Emi ne s'occupe pas de moi, même si ça semble être déjà trop tard."


"Zut, je préfèrerais que personne ne se préoccupe de ma condition, mais sur ce point, ça semble être trop tard pour ça aussi."


"J'aimerais être en mesure de gérer tout ça par moi-même, sans être une gêne pour les autres."


"Tant que j'en suis à vouloir des choses, je préfèrerais ne pas avoir ce problème en premier lieu."

stop music fadeout 1.0

scene bg school_nurseoffice at bgleft
with locationskip

show emi basic_shock_gym at tworight
with easeinright


emi "Infirmier !"


"Emi entre brutalement dans son bureau sans frapper à la porte, mais ça n'a pas l'air d'alarmer l'infirmier le moins du monde."

play music music_nurse fadein 0.5

show nurse grin at twoleft
with charaenter


nk "Bonjour, rayon de soleil. Quoi de neuf ?"


"Rayon de soleil ? Quoi qu'il en soit, il est calmement en train de siroter son café, mais le pose après avoir suivi le regard d'Emi vers moi."

show nurse fabulous
with charachange


nk "Hisao ? Qu'est-ce qui t'amène ici ?"

show emi excited_sad_gym
with charachange


emi "On était en train de courir, et il a trébuché et a commencé à se tenir la poitrine, et j'ai pensé que je devais aller vous chercher et le faire attendre mais il a dit que ça allait mais j'ai pensé que vous devriez le voir quand même et—{w=2.5}{nw}"

show nurse concern
with charachange


nk "Attends Emi. Du calme."

show nurse neutral
with charachange


nk "Hisao, qu'est-ce qui est arrivé ?"


hi "Je ne sais pas. On était en train de courir, et ma poitrine a commencé à me faire mal comme la dernière fois, mais c'est parti après quelques secondes."


hi "C'était juste un mauvais battement ou quelque chose du genre."

show nurse concern
with charachange


"L'infirmier fronce les sourcils, comme pour dire que “juste un mauvais battement” était un genre d'oxymore."


nk "Je ne voulais pas dire ça quand je t'ai suggéré de faire de l'exercice. Tu dois être plus prudent, Hisao."


hi "J'étais prudent, j'ai juste..."


"À bien y penser, “J'ai juste fait une course avec un membre de l'équipe d'athlétisme” ne semble pas être aussi raisonnable que je pensais que ce le serait."


nk "Tu as juste quoi ?"


hi "Euh... c'est que..."


hi "Je faisais une course avec Emi."


nk "Emi, c'est vrai ?"

show emi basic_hes_gym
with charachange


"Emi s'agite, ayant l'air adorablement contrite."


emi "Hum, eh bien..."

show emi basic_closedsweat_gym
with charachange


"Finalement, elle n'arrive pas à se résoudre à le dire à haute voix, et hoche simplement la tête."


"L'infirmier soupire et se frotte mollement le front d'une main."


nk "Emi, tu dois être plus sensible aux limites des autres !"


nk "Je ne sais pas s'il te l'a dit, mais Hisao a un cœur faible, et faire la course avec lui était incroyablement irresponsable."


hi "Euh, en fait, c'est moi qui ai commencé."


"L'infirmier est abasourdi par ma déclaration."


nk "Tu as QUOI ?"


hi "On était juste en train de courir, et Emi a commencé à s'éloigner, et donc j'ai euh, accéléré pour la rattraper."


"L'infirmier regarde le plafond, marmonne une prière pour la patience d'un dieu ou d'un autre, et nous regarde encore une fois tous les deux."


nk "Donc vous êtes {b}tous les deux{/b} idiots."


nk "C'est un réconfort, je suppose."


nk "Maintenant allez, Hisao. Je dois m'assurer que ton cœur ne va pas exploser ou quelque chose comme ça."

show bg school_nurseoffice at left
show nurse concern at center
show emi basic_closedsweat_gym at Alphaout(1.0), offscreenright
with charamove

hide emi
with None


"J'obéis consciencieusement et le suis dans une salle adjacente où nous constatons que je ne suis pas, en effet, en train de passer l'arme à gauche."


nk "Donc comment te sens-tu ?"


hi "Je ne sais pas. Rien de spécial. Fatigué, mais ça doit être juste à cause de l'exercice."


nk "Tu dois rester ici pour quelques heures et te reposer, et nous verrons comment tu te sens après ça."


"Je ne vais pas objecter, donc je m'allonge sur le lit de l'infirmerie."

stop music fadeout 2.0

scene bg school_nurseoffice at left
with shorttimeskip


"Une Emi bien misérable vient après avoir reçu un bon sermon de la part de l'infirmier dans l'autre pièce."


"Je ne pouvais pas entendre ce qu'il disait à travers la porte fermée, mais je suis sûr que ce n'était pas des plaisanteries."

show emi sad_depressed_gym at center
with charaenter

play music music_dreamy fadein 0.5


emi "Écoute, je suis vraiment, vraiment désolée."


emi "J'aurais dû faire plus attention."


hi "Hé, tu ne savais pas. Ce n'est pas ta faute."


"Elle a l'air vraiment triste et désolée, et mes paroles ne font rien pour lui remonter le moral."


emi "Je veux me rattraper."


"Elle fait encore ce hochement de tête décisif."

show emi sad_shy_gym
with charachange


emi "Donc tu dois venir déjeuner avec moi."


emi "C'est moi qui t'apporterai le repas, d'accord ? Quelque chose de vraiment, vraiment bon !"


"Je commence avec un “Tu n'as pas à...” mais je me tais et hoche juste la tête en ayant vu son visage."

show emi excited_proud_gym
with charachange


emi "Bien !"

show emi basic_grin_gym
with charachange


emi "On se retrouve sur le toit."


hi "On ?"

show emi basic_closedgrin_gym
with charachange


emi "Yep ! Il fait beau aujourd'hui, donc le toit est un bon endroit pour déjeuner, tu sais."


hi "Je vois."

show emi sad_shy_gym
with charachange


emi "Tu viendras, hein ?"


emi "Tu ne vas pas me refuser la chance de me rattraper envers toi ?"


hi "Bien sûr que non."

show emi excited_joy_gym
with charachange


emi "Super ! À taleur alors !"

hide emi
with charaexit

with shorttimeskip


"Je reste somnolent, quelque part entre le sommeil et l'éveil, me sentant complètement vidé."


"Pas seulement mon corps, mais tout en moi est mou et paralysé, en dehors de mes sens."


"J'avale avec difficulté ma salive et puis essaye de rester allongé aussi immobile que possible, ce qui dans mon état n'est pas très difficile à faire."


"L'infirmier est en train de bouger de l'autre côté des rideaux qu'il a installés pour me donner de l'intimité. Je peux voir son ombre passer devant la lumière du soleil."


"Il a ouvert la fenêtre de son bureau. Il y a du vent dehors."


"Les rideaux blancs immaculés flottent au vent dans un lourd mouvement paresseux, comme des vagues. La lumière filtre à travers eux lentement, à moitié absorbée dans le tissu."

stop music fadeout 5.0

scene darkgrey
with shuteye


"Je ferme les yeux. La brise sur mon visage est comme le doux tissu des rideaux."


"J'écoute le bruit du battement de mon cœur pendant un moment, essayant d'ignorer le bruit de l'infirmier tapotant sur son clavier, et celui de ma propre respiration."


"Il est stable."


"Merde, ça fait même pas une semaine et je suis de nouveau comme ça. J'ai vraiment foiré cette fois. J'aurais dû savoir que me mesurer à une sportive n'était pas une bonne idée."


"Et pourquoi j'ai essayé d'agir bravement, comme si ma douleur au cœur n'était pas grand-chose, même s'il était évident que ça l'était ?"


"C'était juste un réflexe, de la repousser, la garder à l'intérieur."


"Je ne voulais pas que ça arrive."


"Je ne voulais pas que Emi soit témoin de ça."

"Aaah…"


"Idiotidiotidiot."



"Je dois être plus prudent, ou je finirai encore à l'hôpital, ou pire."

"…"


"C'est ma dernière pensée avant de céder à la fatigue."

scene black
with Dissolve(1.0)

window hide Dissolve(2.0)

with Pause(2.0)

scene bg school_nurseoffice at left
with openeye

window show

play music music_daily fadein 6.0


"Je me suis endormi. Pendant combien de temps ? Quelle heure est-il ?"


"Je me sens un peu étourdi et je continue de cligner des yeux compulsivement."

show bg school_nurseoffice at center
with charamove


"Repoussant le rideau, je plisse les yeux devant la lumière non filtrée passant par la fenêtre. La texture de la toile n'est en rien comme celle du vent d'avant."


"L'infirmier lève le nez de ses papiers, il est assis exactement à la même place qu'il l'était avant."

show nurse fabulous at center
with charaenter


nk "Comment te sens-tu ?"


"Je ne peux pas vraiment dire, donc je ne réponds pas. Je me sens un peu faible de m'être endormi à une heure aussi inhabituelle, j'espère que je n'ai pas l'air trop bizarre."


hi "Quelle heure est-il ?"


"Je croasse la question pour gagner un peu d'orientation. L'infirmier regarde sa montre avant de répondre."


"Les choses semblent se passer au ralenti."

show nurse neutral
with charachange


nk "Dix heures et quart."


"J'essaye de penser pendant un moment à ce que ça veut dire, mais je ne suis pas vraiment sûr."

show nurse concern
with charachange


nk "Tu n'as pas répondu à ma question, Hisao."


hi "Oh. Bien."

show nurse neutral
with charachange


nk "Descends donc du lit alors, et voyons comment tu vas. Ne te..."

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


"C'est ce que j'essaye exactement de faire, mais je perds l'équilibre en me levant trop vite. L'infirmier bouge pour me soutenir et soupire."

show nurse concern
hide dizzy_bg
hide dizzy_fg
with charachange


nk "...relève pas trop vite, c'est ce que j'allais dire. Assieds-toi ici, je vais vérifier ta tension pour être sûr."

$ renpy.music.set_volume(1.0, 2.0, channel="music")


"Je n'aurai pas fait long feu. Je me tais, un peu honteux, pendant que l'infirmier est occupé avec un bidule démodé et mon bras. Après quelques minutes, il l'enlève, n'ayant l'air ni content ni contrarié."

show nurse neutral
with charachange


nk "Tu vas bien. Ta tête a cessé de tourner ?"


hi "Ouais."


nk "Bien. Et comment tu vois les choses maintenant ?"

show nurse concern
with charachange


nk "Tu n'as pas fait preuve d'un très bon jugement tout à l'heure, Hisao."


"Je ravale la réplique que j'allais sortir. C'est ce que je pensais moi-même, mais entendre ça de la part de quelqu'un d'autre me donne envie de protester."


"Ce qu'il dit n'est pas plaisant à entendre. Bien que ce soit vrai."


hi "Non, monsieur."

show nurse neutral
with charachange


"Il hoche la tête, ayant toujours l'air aussi neutre qu'il l'était auparavant."


"Ça serait facile d'être fâché contre lui s'il disait “Je te l'avais dit” ou quelque chose du genre, mais il ne le fait pas."


nk "Je peux essayer de t'aider à garder la santé, mais finalement tout dépend de toi. J'espère que ce petit épisode sera quelque chose qui te le rappellera."

show nurse fabulous
with charachange


nk "Tiens, un mot pour ton professeur. Pour éviter les questions."


"Je prends le bout de papier qu'il m'offre et je pars, n'arrivant pas à penser à quelque chose d'autre à dire."

show nurse neutral
with charachange


nk "Essaye d'éviter les problèmes, veux-tu ? Je ne pense pas que c'était autre chose qu'une frayeur, mais la prochaine fois pourrait être différente."


"Bien compris."

scene bg school_nursehall
with locationchange

stop music fadeout 4.0


"Il y a plusieurs chemins pour aller au bâtiment scolaire depuis l'immeuble auxiliaire, mais je ne suis pas désireux de les découvrir et de potentiellement me perdre, donc je passe par la sortie que je connais."

scene bg school_courtyard
with locationchange


"Je m'arrête à l'escalier du bâtiment auxiliaire, délibérant un moment entre me rendre aux dortoirs pour aller chercher mes livres et des trucs, et aller directement en classe."


"Le soleil m'aveugle, donc je me dirige vers les dortoirs."




label fr_A26:

window hide None
scene black
with dissolve

scene bg school_dormhisao
with openeye

with Pause(0.2)

scene bg school_dormbathroom
with locationskip

window show


"Je me réveille et prends une douche chaude."

label fr_A26a:

scene bg school_dormhisao
with locationskip


"De retour dans ma chambre, la première chose que je vois est la rangée familière de bouteilles de médicaments sur le haut de ma commode, et ça me déprime, comme d'habitude."


"C'est embêtant. Je pensais que ça allait. Je pensais que j'avais fait la paix avec ce truc, eu le dessus."


"Mais ce que j'ai vraiment fait... Je me suis juste permis d'oublier que j'ai un problème. Être ici me rappelle vraiment la réalité, et essayer de lutter contre ça me fait juste mal."


"Y réfléchir n'apporterait rien. Je l'ai déjà fait auparavant, pendant des mois. Je crois qu'il est temps de passer au-dessus de ça."


"Si je me permets d'oublier que ma vie ne sera pas aussi longue que celle des autres, je n'irai nulle part."


"Ma vie peut être différente des autres. Mais c'est une vie en cours."


"C'est comme ça que je rationalise."


"Je prends ma poignée de pilules habituelles, essayant de repousser le sentiment soudain d'abattement. Puis je me prépare pour aller en classe tôt, comme d'habitude."

scene bg school_dormhallway
with locationchange


"Dès que je fais un pas dans le couloir, je remarque Kenji venant du coin, faisant silencieusement son chemin jusqu'à sa chambre avec un grand sac. Vu qu'il se glisse devant moi sans bruit comme un ninja se déplaçant furtivement, je l'appelle."


hi "Yo."

show kenji neutral at center
with charaenter

play music music_kenji fadein 0.5


"Il bondit au son de ma voix."


ke "Oh, yo, mec. Je n'avais pas remarqué que t'étais là. Je suis vraiment fatigué."


"Je pense que c'est plutôt qu'il ne m'a pas vu, mais ce n'est pas la question."


hi "T'étais où aussi tôt ? Un truc à acheter ?"

show kenji tsun
with charachange


ke "Nan pas ça. Des fois je dois aller... voir le prof de maths. Ouais, j'ai pensé que ça serait une bonne idée de savoir quand serait le prochain exam, il peut le dire à l'avance si tu le demandes."


hi "Alors, y a quoi dans le sac ?"

show kenji neutral
with charachange


ke "J'ai pensé à aller acheter des trucs pendant que j'étais dehors. J'ai besoin de fournitures pour continuer de combattre le vaste complot féministe."


hi "Euh, d'accord."


hi "Je pensais que tu n'étais pas sorti."

show kenji happy
with charachange


ke "Je porte un chapeau maintenant."


"Je décide de ne pas faire remarquer le fait qu'il ne porte pas de chapeau."


"Un silence embarrassé s'installe entre nous et puis Kenji le casse en ouvrant la porte de sa chambre, lâchant un bruit de craquement dans l'air qui rend le moment encore plus embarrassant. Il pose le sac dans sa chambre et referme la porte."


hi "Je suis surpris que tu sois sorti pour savoir la date d'un exam. Essayer de prendre avantage d'une opportunité pour étudier est très diligent."

show kenji tsun
with charachange


ke "Je n'étudie jamais."

hi "Oh…"

show kenji neutral
with charachange


ke "Je voulais juste savoir la date du prochain exam. Je vais quand même le faire, duh. J'ai besoin de connaître la date pour savoir quel jour dois venir. Il envoie habituellement les dates par téléphone, donc je dois sortir pour savoir quand c'est."


hi "Et pourquoi tu dois sortir, quand tu peux le savoir sur ton téléphone ?"

show kenji tsun
with charachange


ke "Je n'ai pas de téléphone."


hi "Comment ça tu n'as pas de téléphone ? Tu veux dire que tu le laisses chez toi ?"

show kenji neutral
with charachange


ke "Nan, je n'utilise pas les téléphones. Je n'ai pas de téléphone. Téléphones. J'ai aucun téléphone."


hi "Pourquoi tu n'as pas de téléphone ? Comment tu peux ne pas avoir de téléphone ? Pas de téléphone du tout ? Aucun téléphone ?"

show kenji tsun
with charachange


ke "Je n'aime juste pas les téléphones. En fait, j'ai plutôt peur d'eux. Je ne sais pas pourquoi. Je pense que c'est une sorte de traumatisme refoulé."


ke "Mais, basiquement, quand je porte un téléphone, je suis nerveux. C'est mon plus sombre secret."

show kenji neutral
with charachange


ke "J'ai deux théories là-dessus : soit j'ai peur de recevoir un appel indéfini, de mauvais augure, maléfique qui change la vie, ou alors j'ai été frappé par un téléphone quand j'étais petit. Frappé tellement fort que je m'en rappelle pas."


hi "Frappé à la tête."

show kenji tsun
with charachange


ke "Bah, où d'autre est-ce que j'aurais pu me faire frapper avec un téléphone au point de me rendre incapable de m'en souvenir ? Les fesses ?"


"Logique inattendue. Je me sens très déprimé maintenant. Sentant que la conversation est plus ou moins finie, Kenji ouvre encore la porte et passe la tête à l'intérieur."

show kenji neutral
with charachange


ke "Ouais, je vais dormir, vieux. Bonne journée."


hi "Les cours commencent dans à peine vingt minutes."

show kenji tsun
with charachange


ke "J'ai déjà fait quelque chose aujourd'hui. Trop fatigué pour aller à l'école."

show kenji happy_close
with characlose


ke "Hé, t'as besoin d'un baume à lèvres ? J'en ai accidentellement acheté deux parce que je pensais que le magasin avait commencé à vendre des piles AA individuelles."


hi "Merci, mais non merci."



label fr_A26b:

scene bg school_dormhallway
show kenji happy_close at center
with None

stop music fadeout 0.3

play sound sfx_doorslam

show kenji tsun_close
with vpunch


"La porte du bout du couloir s'ouvre avec un crac comme si elle avait été poussée trop fortement et s'était écrasée contre le mur. Le son est suivi par un éclat de rire pétillant, et je sais instantanément qui c'est."

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


"Au bruit, Kenji disparaît dans sa chambre comme un ninja, claquant la porte juste quand Shizune et Misha arrivent, Shizune avec ses petits pas rapides et Misha rebondissant pesque sur les murs en avançant."

show misha hips_smile_close at twoleft
with characlose


"J'essaye de faire la même chose que Kenji, mais il est trop tard. Misha passe son pied dans la porte, m'empêchant de la fermer, donc je n'ai aucun autre choix que de les laisser entrer."

scene bg school_dormhisao
with locationskip

show shizu behind_smile at center
with charaenter

shi "…"

show shizu behind_smile at tworight
with charamove

show misha hips_grin at twoleft
with charaenter


mi "Salut, Hicchan~ ! Salut~ salut~ !"


hi "Salut."


hi "Qu'est-ce que vous faites ici toutes les deux ?"


"Je me demande si la pause entre les deux phrases a été suffisamment longue pour que ce ne soit pas impoli de ma part."

show shizu basic_normal
with charachange

shi "…"

show misha hips_frown
with charachange


mi "Hicchan, c'est indélicat~ ! On est venues te chercher !"

show misha hips_smile
with charachange


mi "Tu crois qu'on a pensé que tu allais t'échapper et qu'on est venues pour être sûres que tu ne le ferais pas ? Bien sûr que non, Hicchan~ !"


hi "Hé, je n'ai pas dit que c'était pour ça que vous étiez là."


"Mais maintenant je sais que c'est exactement pour cette raison qu'elles sont là."

show misha sign_smile
with charachange


mi "C'est l'heure pour le travail du conseil des étudiants, eh ouais~ !"

show misha hips_grin
with charachange


mi "N'es-tu pas content, Hicchan, de pouvoir aider l'école~ entière~ ! Tu es comme un héros~ ! Les générations futures raconteront des histoires sur ce jour !"


"Intéressant. Je ne pensais pas que rejoindre le conseil des étudiants serait un acte héroïque digne d'Hercule."


hi "Bon... Vu que je l'ai promis..."

show shizu adjust_happy
with charachange

stop music fadeout 7.0


"J'ai négligé Shizune, et seulement maintenant je la remarque à la limite de mon champ visuel, fouillant ma chambre du regard par-dessus mon épaule, analysant objet par objet..."


"C'est plutôt envahissant, le sentiment d'être mis à nu comme ça. Encore heureux que je n'ai pas de linge sale sur le sol ou quelque chose comme ça."

show shizu behind_smile
with charachange

shi "…"

show misha perky_confused
with charachange


mi "Hm~ ? Qu'est-ce qu'il y a, Shicchan ?"

show misha hips_smile
with charachange


mi "Ouais, c'est la chambre de Hicchan~ ! On ne l'avait jamais vue avant, je n'avais même pas réalisé !"

show misha hips_grin
with charachange


mi "C'est plutôt vide, mais Hicchan n'a pas encore eu le temps de décorer, n'est-ce pas~ ?"

show misha sign_smile
with charachange


mi "C'est quoi ça ?"


"Elle pointe le doigt vers ma collection de médicaments sur la table de nuit."



label fr_choiceA26:
menu:
    with menueffect
    "Je n'ai vraiment pas envie de parler de ça avec elles."
    "Essayer d'éviter le sujet.":




        return m1
    "Les faire sortir de ma chambre.":


        return m2


label fr_A26c:


hi "C'est rien."

show shizu basic_normal2
with charachange


"Je me positionne rapidement en face d'elles, essayant de cacher tout ça derrière mon dos. Shizune fait un pas en arrière, affichant un air suspicieux, une expression non sans inquiétude."


"J'espère que si je l'évite, elle comprendra que je ne veux pas qu'elle continue sur ce sujet."

show shizu behind_blank
with charachange

shi "…"

show misha perky_confused
with charachange


mi "Vraiment ? Qu'est-ce que tu caches, Hicchan~ ?"


hi "Rien."

show shizu basic_normal
with charachange

shi "…"

show misha sign_confused
with charachange


mi "C'est vrai ça~ ?"


"Je réalise que je ne peux pas vraiment m'en sortir comme ça. Elles sont curieuses par nature et cacher quelque chose ne fera qu'attiser encore plus leur curiosité."


hi "Ouais d'accord, {b}c'est quelque chose{/b}, mais je ne veux pas vraiment en parler, d'accord ? Pas... encore."


hi "On peut mettre ça de côté pour le moment ?"

show misha perky_smile
with charachange


"Pendant que Misha traduit, Shizune me regarde avec ses yeux durs et analytiques comme toujours, réajustant les branches de ses lunettes avec un air de curiosité."


"Les doigts pressés les uns contre les autres, elle est pensive, comme si elle pesait le choix de poursuivre plus loin que nécessaire face à l'impolitesse d'aller contre mon souhait."


"Son expression se fond finalement dans un petit sourire et elle dit quelque chose à Misha en signes."

play music music_dreamy fadein 2.0

show shizu adjust_happy
with charachange

shi "…"

show misha hips_smile
with charachange


mi "D'accord~ ! Alors, on va attendre, et devenir de plus en plus amis, et un jour quand tu le sentiras, tu pourras nous en parler~ !"


"Elles affichent toutes deux un grand sourire, et je me sens choqué et un peu stupide d'avoir réagi comme ça."


"Elles ne sont pas idiotes, et elles ont probablement à moitié compris ce qui ne va pas chez moi. Et..."


"Des mots si simples, si aimables. Je me sens soulagé qu'elles ne pensent pas de mal de moi malgré la situation. Même si je ne suis pas comme le reste des gens ici. Même si je ne suis pas à l'aise sur le sujet."


"On dirait que derrière leurs actes machiavéliques et malfaisants, elles sont toutes les deux des gentilles filles et des personnes bien. C'est ce que je pense."


hi "Merci."


hi "Donc, vous voulez que je vous aide aujourd'hui, hein ? Puisque je suis l'un des vôtres maintenant ?"

show misha hips_grin
with charachange


mi "Yep~ !"


hi "Après les cours ?"

show misha sign_smile
with charachange


mi "Non non non~ ! Maintenant !"


hi "Maintenant ? Mais et les cours ? Vous allez encore les louper ?"

show shizu adjust_smug
with charachange

shi "…"

show misha cross_laugh
with charachange


mi "Hahaha~ ! C'est pour le bien commun, donc nous sacrifions nos cours de maths, et peut-être l'éducation civique aussi~ !"


hi "Bon, j'imagine que ça me va."

show shizu behind_smile
with charachange

shi "…"

show misha sign_smile
with charachange


mi "Fantastique, Hicchan~ ! Tu l'as dit, hein ? Rappelle-toi : “Je veux bien vous aider~” c'est ce que t'as dit, hein~ ?"


hi "Ouais."


"Ce ton... Je regrette soudainement de l'avoir dit."

show shizu basic_normal2
with charachange

shi "…"

show misha hips_grin
with charachange


mi "D'accord~ ! T'es prêt à y aller alors ? On peut aller au bureau ensemble~ !"


hi "Non. Vous allez probablement me faire porter tous vos trucs ou quelque chose de ce genre."

show shizu adjust_happy
with charachange

shi "…"

show misha perky_smile
with charachange


mi "Ne sois pas bête, Hicchan."

show misha hips_smile
with charachange


mi "On n'a jamais marché dans l'école ensemble, Hicchan~."


"J'ai presque envie de demander pourquoi on le devrait, mais ça me retomberait dessus. Elles me considèrent toutes les deux comme leur ami, comme Misha l'a dit plus tôt. Et elles veulent même devenir de meilleures amies pour moi."


"C'est étrange, je n'ai jamais vraiment pensé à elles de cette façon. Ou même vis-à-vis d'une des personnes que j'ai rencontrées cette semaine. C'est vraiment aussi facile ?"


"Juste comme ça..."


hi "Ok, allons-y alors."

show shizu behind_smile
with charachange


"Shizune sourit avec malice et met ses mains derrière le dos."

show misha hips_grin
with charachange


mi "Hahaha~ ! C'est super, Hicchan~ ! D'accord, d'accord, mais d'abord~ ! Tu as vraiment une super idée, Shicchan va adorer ça... Donc~ ! C'est l'heure pour un jeu !"


hi "Oh non."

show misha hips_smile
with charachange


mi "Shicchan tient un billet de 1000 yen dans une main, Hicchan~ ! Si tu devines dans laquelle il est, tu peux l'avoir ! Si tu n'y arrives pas..."

show misha hips_grin
with charachange


mi "Tu porteras tous nos livres jusqu'à l'école~ ! Hein, Shicchan~ ? Hein~ !"


"Shizune et elle échangent un hochement de tête."

show misha sign_smile
with charachange


mi "Ok, Hicchan~ ! Sois prêt~ !"

stop music fadeout 7.0

scene bg school_courtyard
with shorttimeskip


"Portant trois sacs au lieu d'un, je pense à la journée qui est devant moi. Devant nous."


"Je peux voir des étudiants de tous les côtés dans la cour, probablement en train de préparer leurs propres projets."


"Le festival est pratiquement là. Ça veut dire qu'il y a deux cas dans lesquels mon aide serait requise."


"Soit il y a seulement un peu de travail à faire encore et elles veulent juste un coup de main pour boucler les vérifications finales qu'elles sont obligées de faire."


"Ou alors il y a une tonne de travail à faire, et Shizune affiche un visage calme alors qu'il y a une montagne de travail accumulé qui menace de tous nous tuer."



label fr_A26d:

play music music_rain fadein 4.0


"Malgré ça, elles ont vraiment franchi les bornes cette fois. Fichue curiosité."


hi "Rien du tout."

show misha perky_smile
with charachange


mi "Vraiment~, Hicchan ? Ça n'a pas l'air de rien pour moi."

show shizu adjust_smug
with charachange

shi "…"

show misha hips_smile
with charachange


mi "Ça fait vraiment beaucoup de bouteilles, hein~ ? Hein~ ! Elles servent à quoi, Hicchan ?"


hi "Juste quelques trucs."

show shizu basic_normal2
with charachange

shi "…"

show misha perky_confused
with charachange


mi "Ça a l'air bien plus que “juste quelques trucs”..."


"Je ne peux pas leur reprocher d'être comme ça. Misha parle juste pour Shizune, et Shizune est juste curieuse par nature. Pourtant, j'aimerais qu'elles arrêtent et comprennent l'allusion. Mais Misha ne la verra pas, et Shizune ne peut pas."


"À cause de ça, elles continuent d'insister."


hi "C'est vraiment pas vos affaires."


hi "Vous ne devriez pas partir ? La chambre d'un homme est une zone privée, vous savez."


"Shizune semble prendre ça comme un challenge."

show shizu behind_frown
with charachange

shi "…"

show misha hips_frown
with charachange


mi "Qu'est-ce que ça veut dire, Hicchan ? Quand quelqu'un voit quelque chose d'intéressant, son premier instinct est de demander ce que c'est, c'est évident. Où est le mal ?"


hi "Parce que, comme j'ai dit, il n'y a rien à voir."

show misha perky_confused
with charachange


mi "Hicchan, je pense que Shicchan est juste préoccupée."


hi "Ce que j'ai dans ma chambre ne vous concerne pas, c'est tout."

show misha sign_confused
with charachange


mi "Mais..."


hi "Mais merde ! Des fois, j'aimerais que vous arrêtiez de jouer à ça. C'est pas tout le temps drôle. Vous le savez ça, hein ?"


"Je l'ai dit bien plus violemment que je ne le voulais, criant presque directement au visage de Misha. Elle sursaute et se fige en plein signe, et Shizune réagit aussi même si elle ne m'a pas entendu."

stop music fadeout 6.0


"Je suppose que mon visage en colère a dit tout ce qui devait être dit."

show misha perky_sad
show shizu behind_blank
with charachange


"Après que Misha ait lentement fini la traduction, les filles se regardent d'un air de regret."

show shizu behind_sad
with charachange

shi "…"


mi "D'accord, Hicchan, on te laisse seul."


"C'est la première fois que j'entends Misha parler sans sa voix vacillant entre l'aigu et le grave. C'est étrange à entendre, et j'ai envie de m'excuser, mais elles se sont déjà tournées pour partir."


"Alors que le silence s'installe, je regrette de plus en plus ce que j'ai dit."

hide shizu
hide misha
with charaexit


"Les filles partent silencieusement, et après un moment à rester debout dans ma chambre, je m'habille et pars après elles."



label fr_A26e:

show kenji tsun_close
with charachange


ke "Tant pis, mec."

stop music fadeout 2.0

hide kenji
with charaexit


"Il rentre rapidement dans sa tanière, me laissant finalement aller en classe."



label fr_A27:

scene bg school_hallway3
with shorttimeskip


"Les couloirs sont aussi silencieux que la cour l'était, naturellement vu que tout le monde est en classe. Je frappe doucement à la porte de la classe 3-3 et la pousse après que Mutou ait répondu de l'autre côté."

scene bg school_scienceroom
with locationchange


hi "Désolé du retard."


"Quinze paire d'yeux se tournent vers moi."

show muto irritated at center
with charaenter


mu "Bonjour, Nakai."


"Mutou semble être légèrement déconcerté par mon retard, comme si j'avais interrompu son rythme ou quelque chose."


"Vu les cours magistraux que peuvent être ses cours, quand il ne divague pas, ça doit être le cas."


"Je lui passe le mot que l'infirmier m'a donné. Mutou le prend en hochant la tête et le lit rapidement."

show muto normal
with charachange


"Il lève les sourcils et me lance un genre de regard sévère mais ne dit rien, et hoche la tête solennellement à nouveau."


"Je hausse les épaules et il me fait un geste pour que j'aille m'asseoir, ce que je fais, naturellement."


label fr_A27a:

scene bg school_scienceroom
show muto normal at center
with None


hide muto
with charaexit


"Seulement deux paires d'yeux continuent de me regarder avec attention pendant que je marche jusqu'à mon siège."


"Je ne suis pas du tout surpris quand je sens l'ongle de Misha picoter à travers ma chemise à peine quinze secondes après que je me sois assis."

show misha perky_smile_close at offscreenleft
with None

show bg school_scienceroom at bgright
show misha perky_smile_close at Transform(xalign=-0.3)
with charamove

play music music_another fadein 2.0


mi "Psst ! T'étais où ?"


hi "Ça vous regarde pas."


"Je sais que c'est probablement la pire réponse que je peux donner et que ça va uniquement éveiller leur curiosité, mais je n'ai pas l'énergie de monter une histoire pour me couvrir maintenant."

show misha perky_confused_close
with charachange

show bg school_scienceroom at center
show misha perky_confused_close at offscreenleft
with charamove


"Pourtant, Misha recule. Elle abandonne drôlement vite aujourd'hui."

"…"


"Une minute après, elle recommence à me tapoter le dos avec son doigt."

show misha hips_grin_close
with None

show bg school_scienceroom at bgright
show misha hips_grin_close at Transform(xalign=-0.3)
with charamove


mi "Allez, dis-nous ! Shicchan est très intéressée aussi !"


"C'était ce que j'espérais du moins. Elle en parlait juste à Shizune, probablement pour trouver un moyen de me faire cracher le morceau."


hi "Non."

show misha perky_sad_close
with charachange

show bg school_scienceroom at center
show misha perky_sad_close at offscreenleft
with charamove


"Elle se retire pour négocier à nouveau."

show misha sign_smile_close
with None

show bg school_scienceroom at bgright
show misha sign_smile_close at Transform(xalign=-0.3)
with charamove

label fr_choiceA27:
menu:
    with menueffect
    mi "En tant que membre du conseil des étudiants, il est de ton devoir de nous dire pourquoi tu as loupé les cours ! Particulièrement si c'est quelque chose de fun fun fun~ !"
    "Ouais, c'était fun fun fun d'être au bureau de l'infirmier...":





        return m1
    "Je ne veux pas en parler, d'accord ?":



        return m2

label fr_A27b:

stop music fadeout 4.0


"Mais merde. Elle ne sait vraiment pas quand s'arrêter."


hi "Ouais bien. Comme tu veux. Je vais te le dire. J'ai passé un bon moment."


hi "J'ai d'abord eu une crise cardiaque dans la matinée et j'ai été traîner avec le cadre infirmier pendant quelques heures pour m'amuser."


hi "Meilleure matinée de ma vie, je peux te le dire."


"J'essaye d'imiter sa ridicule manière de parler chantonnante tout en gardant ma voix basse pour que personne d'autre ne puisse m'entendre. Les mots sortent de ma bouche comme des balles."

show misha perky_confused_close
with charachange


mi "Hicchan, tu as eu une quoi ? Sérieusement ?"


hi "Laisse tomber. Tu m'as entendu."

show misha perky_sad_close
with charachange


mi "Mais Hicchan, c'est important !"


hi "Non, vraiment. Laisse-moi seul. On est au milieu de la classe, aussi."

show misha sign_sad_close
with charachange


mi "Mais Hicchan !"


"Misha semble inquiète, ou peut-être paniquée. Je me demande si elle réalise elle-même que ce n'était pas une si bonne idée d'être aussi violemment intrusive."

"…"


"Je la laisse mijoter pendant un moment avant de répondre. Ça ne sera pas traduit à Shizune mais je m'en fous."


hi "Fous-moi la paix, Misha."


hi "Et dis à Shizune de faire pareil."


"Dès que les mots sortent de ma bouche, je regrette immédiatement de les avoir dits, mais ce n'est pas comme si je pouvais les retirer maintenant."

show misha perky_sad_close
with charachange

show bg school_scienceroom at center
show misha perky_sad_close at offscreenleft
with charamove

hide misha
with None


"Je suis assez supris de constater que Misha se tait effectivement même si je n'ai pas vérifié qu'elle passait le message à Shizune. C'est pas important de toute façon."


"Mutou finit son cours sur une discussion à propos du festival dans deux jours."





label fr_A27c:


hi "Abandonne. Je ne le dirai pas."

show misha hips_grin_close
with charachange


mi "Vraiment~ ?"


hi "Ouais."

show misha perky_confused_close
with charachange


"Elle réfléchit pendant un moment."

show misha hips_frown_close
with charachange


mi "C'est pas juste, Hicchan~ !"


"Je peux entendre la moue dans sa voix, déçue et abattue."

show bg school_scienceroom at center
show misha hips_frown_close at offscreenleft
with charamove


"Elle recule encore pendant un moment pour négocier avec le cerveau du duo dynamique, avant de revenir."

show misha hips_smile_close
with None

show bg school_scienceroom at bgright
show misha hips_smile_close at Transform(xalign=-0.3)
with charamove


mi "Je pense qu'on devrait manger ensemble et en discuter un peu plus... dit Shicchan."

show misha hips_grin_close
with charachange


mi "C'est nous qui paierons."

show misha sign_smile_close
with charachange


mi "D'ailleurs, tu dois te rattraper pour ne pas être venu ce matin nous aider avec le travail~ !"


"Les autres étudiants autour de nous commencent à nous regarder, probablement parce que Misha est tellement penchée par-dessus son bureau qu'elle peut presque me cogner la tête. Ses cheveux bouclés me frôlent le cou."


"Ça sent le shampoing et très fort quoi que ce soit qu'elle mette pour qu'ils tiennent comme ça."


"Je pense que la fille en face de moi essaye d'écouter. J'espère que personne ne se fera de mauvaise idée, bien que je ne sois pas vraiment sûr qu'il soit possible de se faire un autre genre d'idée."


"Heureusement Mutou reste sans rien dire, ou ignore délibérément Misha. Pour l'instant."


"Je ne peux pas gagner cette fois, hein ?"



label fr_choice2A27:
menu:
    with menueffect
    "J'ai promis à Emi de manger avec elle aussi, mais je ne peux pas être à deux endroits en même temps."
    "Je vais déjeuner avec Emi et son amie.":




        return m1
    "Je vais avec Shizune, je suis du conseil des étudiants maintenant.":


        return m2


label fr_A27h:



hi "Désolé, je peux pas, j'ai déjà promis de déjeuner avec quelqu'un."

show misha perky_confused_close
with charachange


mi "Eeeh ? Qui ? C'est une fille~ ?"


hi "Ouais..."

show misha hips_grin_close
with charachange


"Son rire me force à enchaîner rapidement avec quelque chose pour qu'elle ne se fasse pas de mauvaise idée."


hi "Rien à voir avec ça ! C'est... un peu compliqué."

show misha perky_smile_close
with charachange


"Compliqué... ouais, c'est ce que ma vie est, en dépit du fait qu'elle est déjà dans une routine quotidienne de vie scolaire."


"Tout doit être mis dans un nouveau type de perspective dans cette nouvelle vie, reconsidérée depuis le point de vue du nouveau moi."


"Le moi avec un cœur brisé."


hi "Aussi, je ne sais pas si je peux venir au conseil après tout."


hi "Ou du moins pour le moment. Il y a une autre chose sur laquelle j'ai besoin de me concentrer."


"C'est vrai. Je dois revoir mes priorités. C'est quelque chose qui a tourbillonné dans ma tête depuis que l'infirmier m'a parlé. Je ne peux vraiment pas faire semblant de ne pas avoir ce problème."


"Je suis surpris de penser aussi analytiquement, mais je vais suivre le mouvement pour l'instant."


hi "Je promets de vous l'expliquer en détail plus tard, mais pas maintenant, d'accord ? S'il te plaît, dis à Shizune que je suis désolé de la laisser tomber."

show misha perky_confused_close
with charachange


mi "Si tu le dis, Hicchan."


"Elle a l'air surprise, et sérieuse, ce que je crois n'avoir jamais vu venant de Misha auparavant."

show bg school_scienceroom at center
show misha perky_confused_close at offscreenleft
with charamove

hide misha
with None

stop music fadeout 3.0


"Heureusement Misha comprend que je suis sérieux, un coup de chance que je puisse dire ce que je veux aussi clairement et qu'elle comprenne. Elle se recule pour traduire notre discussion à Shizune."


"Aucune des deux ne m'a reparlé après ça."



label fr_A27i:


hi "Bien, je viens avec vous, mais lâchez-moi pour le reste des cours, d'accord ?"

show misha hips_grin_close
with charachange


mi "Ça marche, Hicchan~ !"

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


"Sur le chemin de la salle du conseil des étudiants, je croise des étudiants dans les couloirs, probablement en pleine préparation de leurs propres projets."


"Le festival est pratiquement là. Ça veut dire qu'il y a deux cas pour lesquels mon aide serait requise."


"Soit il y a encore un peu de travail à faire, et elles veulent juste un coup de main pour boucler les vérifications finales qu'elles sont obligées de faire."


"Ou alors il y a une tonne de travail à faire, et Shizune affiche un visage calme alors qu'il y a une montagne de travail accumulé qui menace de tous nous tuer."

stop ambient fadeout 1.0


label fr_A27d:



scene bg school_scienceroom
with locationskip


"Pour une fois, je ne suis pas dans les premiers à être en classe ce matin."


"À la place, presque tout le monde semble être déjà là. Je reconnais la plupart des gens de la classe maintenant, mais les noms m'échappent encore."



label fr_A27e:



scene bg school_scienceroom
with shorttimeskip

play music music_normal fadein 3.0


"Le cours se poursuit paresseusement. Je crois que je commence à m'habituer au rythme de l'école."


"J'ai même cessé de m'inquiéter de la prise de notes et d'être ouvertement attentif. Les premiers jours, j'étais très nerveux en classe."


"Mutou termine sa lecture sur l'électricité en avance, mais enchaîne avec le festival sans une pause."

show muto normal at center
with charaenter


mu "Donc, comme vous le savez, le festival est après-demain. J'espère que les projets de tout le monde vont être réussis cette année."

show muto smile
with charachange


mu "Passez un bon moment, mais quand viendra dimanche, gardez s'il vous plaît le sens du festival en tête..."


mi "Jeux et nourriture frite !"


"Tout le monde éclate de rire, et moi aussi."

show muto irritated
with charachange


mu "Oui, merci Mikado."

show muto normal
with charachange


mu "Mais ce que je veux dire est que—{w=.5}{nw}"

play sound sfx_normalbell


"Le reste de sa phrase est englouti dans la sonnerie du déjeuner, et tout le monde commence à ranger ses affaires."


"Mutou parle encore pendant un moment, mais puisque personne ne semble lui accorder d'attention, il abandonne et s'assied."

stop music fadeout 2.0

scene bg school_hallway3
show crowd
with locationchange

play ambient sfx_crowd_indoors fadein 0.3


"C'est bondé dans le couloir... ou aussi bondé que le reste des couloirs de l'école doivent probablement l'être. La plupart des étudiants semblent se diriger vers la cafétéria en bas."






label fr_A27f:

scene bg school_scienceroom
with shorttimeskip

stop music fadeout 2.0


"Misha, et par extension, Shizune, ne m'embêtent pas de la matinée."

play sound sfx_normalbell


"Quand la cloche sonne, je ne les regarde même pas et sors de la classe."

scene bg school_hallway3
show crowd
with locationchange

play ambient sfx_crowd_indoors fadein 0.3


"C'est bondé dans le couloir... ou aussi bondé que le reste des couloirs de l'école doivent probablement l'être. La plupart des étudiants semblent se diriger vers la cafétéria en bas."





label fr_A28:

scene bg school_council
with locationchange

show misha perky_smile at twoleft
show shizu behind_smile at tworight
with charaenter


"Une fois dans le bureau, je regarde autour de moi et remarque qu'il est désert."


hi "J'imagine que ça veut dire qu'il ne reste pas grand-chose à faire, hein ? Vu qu'il y a personne ici, et tout."

show misha sign_smile
with charachange


mi "C'est toujours comme ça, Hicchan~ !"


"Ça confirme ce que je pensais avant mais qui n'avait jamais été clairement confirmé : Shizune et Misha sont le conseil des étudiants. Le conseil des étudiants tout entier."


hi "La vache. Donc c'est vrai. Il n'y a vraiment que vous deux dans le conseil des étudiants."

play music music_ease fadein 4.0

show misha hips_grin
show shizu cross_wut
with charachange


"Shizune a l'air d'être coincée entre avoir honte et exploser de colère, et Misha est également partagée entre rire et essayer de l'arrêter."

show shizu behind_frustrated
with charachange

shi "…"

show misha sign_smile
with charachange


mi "Eh bien, donc, Hicchan, tu seras content de savoir que vu qu'il y a que nous trois, on a beaucoup à faire ! Beaucoup~ ! Beaucoup~ beaucoup~ beaucoup~..."


hi "Ça ne me rend pas spécialement content."

show shizu adjust_happy
with charachange


"Mais ça semble rendre Shizune très contente."

show misha cross_laugh
with charachange


mi "Wahaha~ !"

show misha hips_grin
with charachange


mi "On plaisante !"

label fr_A28a:


scene bg school_council
with shorttimeskip


"Le travail se révèle être une sorte de triage et de double vérification d'une montagne de paperasse nécessaire pour qu'un évènement comme le festival scolaire puisse avoir lieu."


"La bureaucratie est une chose ahurissante."

play sound sfx_normalbell


"Mais on a réussi à finir juste quand la cloche annonçait midi."

show misha hips_grin at twoleft
show shizu adjust_happy at tworight
with charaenter


mi "D'accord~ maintenant qu'on a fini, on peut se reposer un peu ! Mais pas trop, on en a beaucoup plus à faire pendant l'après-midi~ !"

label fr_A28b:

$ renpy.music.play(music_ease, fadein=4.0, if_changed=True)

show shizu behind_smile
with charachange

shi "…"

show misha sign_smile
with charachange


mi "Il n'y en a pas vraiment autant que ça, Hicchan~. Donc~, on peut se permettre de profiter d'un bon déjeuner d'abord."

show misha cross_laugh
with charachange


mi "Hahaha~ !"


"Elles sortent toutes les deux une rangée de boîtes entourées d'un plastique destiné à protéger la nourriture de l'air ambiant."

show misha hips_grin
with charachange


mi "Hm~ hm~... c'est de l'escalope de poulet avec des tomates et des germes de soja~ ! Ça n'a pas l'air délicieux, Hicchan ?"


mi "Ça a été fait ce matin, et c'est encore tiède, donc mange mange mange~ !"


"Je prends une des boîtes et l'ouvre. Ça a l'air bien, et ça sent bon aussi. Le fait que j'ai vraiment faim accentue la chose."


hi "Woaw, ça a l'air super. Où est-ce que vous avez eu ça ?"

show shizu basic_normal
with charachange

shi "…"

show misha hips_smile
with charachange


mi "C'est pas important, Hicchan !"

show misha sign_smile
with charachange


mi "C'était supposé être pour un stand à paniers-repas, mais la fille qui le tenait a soudainement dit qu'elle ne pouvait pas le faire. Shicchan a dit “Quel gâchis, c'était tellement dur de leurer Hicchan pour qu'il fasse ça~”—"


hi "Hé, mais qu'est-ce que..."

show misha hips_grin
with charachange


mi "...Donc~ ! Shicchan voulait voir si elle pouvait le faire, mais ensuite elle a changé d'avis, hein, Shicchan~ ?"

show shizu basic_angry
with charachange


"Shizune boude de colère, fusillant Misha d'un regard mécontent. Je ne pense pas que j'étais supposé entendre cette histoire."


hi "C'est votre nourriture de test ?"

show shizu behind_frown
with charachange

shi "…"

show misha sign_smile
with charachange


mi "J'en mange aussi, Hicchan~ !"

show misha hips_grin
with charachange


mi "Et Shicchan aussi~ !"


"Ça ne répond pas à la question !"


"Néanmoins, je sépare la paire de baguettes que Shizune m'offre, prends un morceau d'escalope et le mets dans ma bouche."


hi "C'est étonnamment bon. Je n'avais pas espéré que Shizune puisse être une aussi bonne cuisinière."

show shizu basic_frown
with charachange


"Shizune baisse ses baguettes pour faire des signes secs à Misha, qui engloutit son escalope avec une difficulté notable afin de parler pour elle."

show misha sign_smile
with charachange


mi "Hicchan~ ! Ne parle pas la bouche pleine~ !"


hi "C'est pas comme si ça m'amusait. D'ailleurs, c'est vraiment maternel comme réflexion..."

show shizu behind_frown
with charachange

shi "…"

show misha hips_frown
with charachange


mi "Tu ne peux même pas manger correctement, Hicchan~ ! C'est tout~ !"

show misha perky_sad
with charachange


"C'est une impasse. Je ne peux pas manger si je veux parler avec Shizune, qui ne peut pas manger pour me reprocher de manger de la mauvaise façon. Misha, coincée entre les deux, est dans la même situation, et c'est elle qui a l'air la plus attristée."

show shizu behind_blank
show misha perky_smile
with charachange


"De toute façon, notre repas refroidit de seconde en seconde, et il n'était pas très chaud au départ. Peu importe où se dirigeait notre discussion, elle s'éteint vite et nous nous concentrons sur le plat devant nous."

play sound sfx_warningbell


"Après un moment, la cloche sonne, mais Misha ne prend pas l'initiative de le dire à Shizune, donc je suis sûr qu'elles ont prévu de sécher les cours et de passer encore le reste de la journée ici."

show shizu adjust_smug
with charachange

shi "…"

show misha sign_smile
with charachange


mi "Hicchan, tu as quelque chose de prévu pour le festival ?"


hi "Non, pas vraiment. Après tout, je ne suis là que depuis une semaine, qu'est-ce que j'aurais pu préparer en aussi peu de temps ?"

show misha cross_laugh
with charachange


mi "Wahaha~ ! Hicchan, tu nous as vraiment beaucoup aidées, ne te rabaisse pas !"


hi "D'accord."

show shizu basic_angry
with charachange

shi "…"

show misha hips_frown
with charachange

mi "On est sérieuses~ !"


hi "D'accord !"


"Elles semblent toutes deux s'indigner sur des trucs très étranges."

show shizu adjust_happy
with charachange

shi "…"

show misha hips_smile
with charachange


mi "T'abandonnes jamais, hein, Hicchan ? Tu dois au moins voir ce qu'on a accompli... ? Tout le monde devrait être capable de voir ce qu'il a fait afin de pouvoir complètement comprendre son travail, c'est ma conviction~ !"

show misha perky_smile
with charachange


mi "Hicchan, tu dois définitivement y aller~ ! Si tu n'as rien de prévu, alors peut-être qu'on peut même y aller ensemble~ !"

show shizu adjust_blush
with charachange


hi "Vous avez besoin d'un coup de main ? Si vous avez besoin d'aide pour quelque chose, je veux bien traîner avec vous."


"Je me sens plus à l'aise qu'avant ; mes précédentes préoccupations et craintes ont disparu depuis longtemps. J'avais oublié le problème de ce matin jusqu'à maintenant, m'amusant avec Shizune comme ça."


"M'amuser avec Shizune... Ça semble un concept peu familier comme ça, mais, à y repenser, j'ai réellement apprécié les moments que j'ai passés avec Shizune et Misha ces derniers jours, en dépit de tout le reste."


"Si on peut être ensemble, alors peut-être que je peux me permettre de traîner avec elles un peu plus longtemps. Et c'est mieux que les cours après tout."

show shizu behind_blank
with charachange

shi "…"

show misha hips_smile
with charachange


mi "Vraiment, Hicchan ? D'accord~ ! On peut considérer ça comme une contrepartie au repas gratuit~ !"

show misha cross_laugh
with charachange


mi "Génial, c'est génial, vraiment~ vraiment~ génial~ ! Shicchan espérait aborder le sujet plus tard de toute façon ! Ahahaha~ ! Wahahahahaha~ !"


"C'est pas un repas gratuit du tout alors. Normalement je serais en colère, ou au moins un peu perturbé, mais mon moral s'est amélioré par rapport à avant, donc je laisse couler."


"Les aider consiste la plupart du temps à estampiller et à faire un truc comme dix mille copies de chacun des cinquante rapports budgétaires différents."


"Ce n'est pas dur, mais très ennuyeux, et selon Misha, la plus simple des tâches qu'elles aient à faire."


"Je me sens de plus en plus fatigué, et avec ça, moins pressé de retourner en classe. C'est spécialement mauvais parce que plus je passe de temps en dehors de la classe, et plus ça devient dur de penser à me lever et y retourner."


"Elles deux, elles ont une terrible influence. Des modèles terribles. Pas que ça me gêne spécialement, et je suis sûr que personne n'y fait attention, mais c'est pour le principe de la chose..."

show shizu adjust_happy
with charachange

shi "…"

show misha hips_grin
with charachange


mi "Fini~ !"


hi "Ah, c'était rapide. J'aurai fini avant la fin de l'heure, je pense."

show misha sign_smile
with charachange


mi "Non, non, Hicchan, tout est fini. Donc t'as fini, aussi~ !"


hi "Ça n'a pas de sens, tu me dis que tout ceci était arbitraire et que vous me gardiez ici juste pour ça ?"

show misha hips_grin
with charachange


mi "Non~..."

show shizu basic_normal
with charachange

shi "…"

show misha perky_smile
with charachange


mi "Mais on t'a gardé suffisamment longtemps~ ! Tu devrais retourner en classe, Hicchan~ ! Tu peux toujours faire la majeure partie de cette heure-là !"


hi "Et vous alors ?"

show shizu behind_blank
with charachange

shi "…"

show misha hips_smile
with charachange


mi "Bien sûr on vient aussi, bien sûr ; on est juste derrière toi !"

stop music fadeout 6.0

scene bg school_hallway3
with locationchange


"Rassuré, je commence à me diriger vers la classe, mais le cours est presque terminé, donc je commence à penser qu'il serait inutile d'y aller, et que je peux passer le temps avant la fin de l'heure en buvant une boisson dans le couloir."


"Je garde un œil sur la porte du conseil des étudiants. Qu'est-ce qui leur prend autant de temps ? Elles font ma part du travail ? Bah, ça ne devrait pas prendre autant de temps, sauf s'il y en a plus, et qu'elles voulaient juste que je parte."


"Plus j'y pense, et plus ça semble vraisemblable."


"Shizune est... bon, pas une idiote, mais clairement, elle n'est pas en mesure de s'en sortir avec tous ces trucs."


"Peut-être que c'est parce qu'elle ne peut pas parler, donc c'est plus dur pour elle. Elle a Misha, mais dans l'ensemble, aussi facile que ça puisse paraître, il y a toujours une différence entre parler normalement et le langage des signes."

play sound sfx_normalbell


"J'envisage d'y retourner pour vérifier ce qu'elles font, mais la cloche sonne, et je dois aller en classe."

scene bg school_scienceroom
with locationchange


"Elles me rejoignent quelques minutes plus tard, et la pensée que j'avais avant s'évanouit dans la routine de la vie scolaire."

with shorttimeskip


"Le temps que je m'en rende compte, l'école est finie pour la journée, et je suis trop fatigué pour faire quelque chose à part rentrer, faire mes devoirs, et puis aller dormir."

$ suppress_window_after_timeskip = True

scene black
with Dissolve(3.0)




label fr_A29:

scene bg school_hallway3
show crowd
with None

play ambient sfx_crowd_indoors fadein 0.3
play music music_emi fadein 0.3

show emi basic_happy at center
with charaenter


emi "Hisao !"

show emi excited_proud
with charachange


emi "Je vais te faire, pour-une-fois-seulement, une super offre pour un extra déjeuner spécial !"

show emi excited_laugh
with charachange


emi "Un panier-repas fait maison par Emi, et le privilège d'en profiter en privé avec deux superbes bombes !"


"Sa façon de vanter son repas en flirtant à moitié résonne dans le couloir, un fait remarquable vu qu'il est plein de monde."

show emi basic_closedgrin
with charachange


"Emi prend une pose très confiante comme dans une tentative de mettre en avant son propre ridicule, gonflant sa très modeste poitrine et faisant le V de la victoire avec sa main."


hi "Ça a l'air délicieux, et qu'est-ce qui me vaut l'honneur d'être invité ?"

show emi excited_proud
with charachange


emi "T'es planté là en ayant l'air vraiment perdu et triste, donc j'ai pensé que tu pouvais avoir besoin de compagnie."


"C'est probablement la plus déprimante raison imaginable."

show emi basic_closedgrin
with charachange


emi "Donc alors ? Ou sinon, tu es vraiment solitaire et tu veux manger tout seul l'horrible nourriture de la cafétéria."


hi "Euuh..."

show emi excited_proud
with charachange


emi "Je plaisante, je plaisante !"


hi "Bien sûr, j'accepte ton offre. Avec plaisir."

show emi basic_happy
with charachange


emi "Allons sur le toit !"


hi "Le toit ?"


hi "Pourquoi le toit ?"

show emi basic_closedgrin
with charachange


emi "Parce que c'est là qu'on mange notre déjeuner !"


emi "Et si je ne monte pas là-haut, alors elle va probablement aller se balader et je sais qu'elle aura faim parce qu'elle ne prend jamais de déjeuner par elle-même !"


hi "Qui ça ?"

show emi basic_closedhappy
with charachange


emi "Viens avec moi !"


"Sans répondre à ma question ou attendre une réponse, elle m'attrape par le bras et m'emmène dans les escaliers."


"J'essaye de faire la conversation en chemin."


hi "Pourquoi t'as un repas en plus ?"

show emi sad_grin
with charachange


"Emi affiche un sourire coupable."


emi "En fait, c'est le déjeuner d'hier."


emi "J'ai couru à midi, et j'ai oublié de le manger."

"Huh."




label fr_A29x:


"Son expression est si drôle que j'en éclate presque de rire."


"Emi rit doucement, d'elle-même ou de quelque chose d'autre, ou peut-être sans raison particulière. J'aime son rire."


"Emi est ensoleillée, et son caractère énergique allège la sensation de contrition qui est à l'arrière de ma tête depuis la dispute avec Shizune et Misha."


"Je laisse ce souci me sortir de la tête, et sourit pour la première fois de la journée."



label fr_A29a:


scene bg school_hallway3
show crowd
with None

play ambient sfx_crowd_indoors fadein 0.3


"Normalement, je rejoindrais la mêlée et prendrais mon repas moi-même, mais aujourd'hui c'est différent."


"Aujourd'hui, j'ai été invité à déjeuner sur le toit."


"Un endroit étrange, mais c'est là qu'on m'a dit d'aller."


"Heureusement, je réussis à trouver un abri contre la tempête derrière la porte de la classe."

stop ambient fadeout 1.0

hide crowd
with Dissolve(2.0)


"Finalement, le torrent se calme et je marche prudemment dans le couloir."


"Seulement pour rencontrer Emi, qui vient en fonçant dans le couloir comme un boulet de canon."

play music music_emi fadein 0.3

show emi basic_happy at center
with charaenter


emi "Hey ! Salut Hisao ! Super timing !"

show emi excited_proud
with charachange


emi "J'ai un repas en plus aujourd'hui, comme promis ! Montons sur le toit !"



label fr_A29b:



stop music fadeout 2.0
stop ambient fadeout 1.0

scene bg school_staircase1
with locationchange


"L'escalier menant au toit est un peu délabré, mais il a clairement été utilisé récemment."


"Il y a une porte en haut des escaliers, avec un cadenas manquant."


"Je me demande qui est l'intrépide qui a retiré le verrou."

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 2.0

scene bg school_roof at bgright
show emi basic_closedgrin at center
with Fade(0.5,0.3,1.0,color="#FFF")


"Emi pousse la porte et marche droit dans les radieux rayons du soleil."

show rin silhouette at offscreenright
with None

show bg school_roof at center
show emi basic_closedgrin at left
show rin silhouette at tworight
with ease

show emi basic_shock
with vpunch


"Soudain, un grand étranger ténébreux apparaît de nulle part, se tenant majestueusement devant nous. Emi sursaute, en tombant presque dans les escaliers."


$ doublespeak (emi, rin_, "Aaah !", "Bonjour.")

show emi basic_hes
with charachange

show emi basic_hes at twoleft
with charamove


emi "Haa ! Tu m'as fait peur, Rin !"


"Attends, c'est pas..."

show rin relaxed_surprised
with charachange

play music music_rin fadein 2.0


rin "Bonjour."


"Remarquant que Rin me parle, Emi me regarde curieusement."

show emi basic_confused
with charachange


emi "Vous vous connaissez ?"


"Je regarde confusément Emi."


hi "C'est elle ton amie ?"

show rin relaxed_nonchalant
with charachange


"Rin a tourné son regard vers les nuages qui passent au-dessus de l'école."


rin "Je ne savais pas que tu le connaissais, Emi."

stop music fadeout 2.0

"…"


"Le silence embarrassé dure quelques secondes jusqu'à ce que Emi laisse échapper un petit rire, à cause de la coïncidence."

show emi basic_closedgrin
with charachange


emi "J'ai invité Hisao à déjeuner. Si tu le connais, c'est encore mieux."

show rin basic_deadpan
with charachange


rin "Oh. Ça veut dire que je n'aurai pas à manger ? Ou tu l'as invité à déjeuner sans déjeuner ?"

show emi basic_grin
with charachange


emi "Hum, aucun des deux, j'ai à manger pour trois."

show rin basic_deadpanamused
with charachange


rin "Bien pensé."

hide rin
hide emi
with charaexit


"Elles marchent jusqu'à l'autre bout du toit alors que je reste immobile pendant un moment, m'imprégnant de l'atmosphère."

play music music_soothing fadein 0.5


"Il n'y a personne d'autre que nous ici. J'imagine que le toit n'est pas aussi populaire qu'il l'est dans les autres écoles."


"Quelques bancs et tables délabrés sont disséminés aux coins, peut-être dans une tentative de rendre le toit moins désolé."


"Les petits cailloux partout sur le toit craquellent sous nos pieds."


"Je m'avance vers la clôture et jette un regard sur le terrain de l'école et au-delà."


"Des étudiants se promènent en paires et en groupes autour du bâtiment de la cafétéria."


"Quelques camions de livraison arrivent à l'école depuis l'épicerie la plus proche."


"Quelque part un chien de garde aboie sur un passant."


"D'une certaine façon, quand je regarde vers le centre-ville, je pourais presque sentir le cœur de cette petite ville me toucher de façon presque palpable."


"Le mode de vie trépidant des grandes métropoles semble tellement loin d'ici ; les gens n'ont pas besoin de courir pour attraper un bus comme si leur vie en dépendait, ou d'avoir leurs sens surchargés par la lumière et les embouteillages."


"Je me sens étonnamment optimiste à propos de ma nouvelle vie, regardant ma nouvelle ville, même si elle ne sera mienne que pendant une courte année."


"Découvrir ma maladie et déménager de chez moi a été si soudain que je n'ai même pas eu le temps de penser à la façon dont je le vivais."


"Quand je sors de l'ombre de la tour de l'horloge, je sens la chaleur caresser mon dos."


"Le soleil brille dans un ciel céruléen parfaitement clair."


"Une légère brise soufflant sur le toit me fait frissonner, mais seulement brièvement."


"Le vent porte l'odeur des arbres et des fleurs, pas la fumée et l'odeur d'échappement des voitures comme autrefois, il y a juste quelques semaines de ça."


"Emi s'installe sur un banc avec Rin en remorquage et sort un gros et deux petits paniers-repas de son sac."

show rin basic_deadpannormal at tworight
show emi basic_happy at twoleft
with charaenter


emi "Viens, Hisao ! Qu'est-ce que t'attends ?"


"Elle me fait signe de les rejoindre, me faisant de la place sur le banc déjà petit."

hide emi
hide rin
show bg school_roof at bgleft
with charamoveoutleft

show emi basic_happy_close at closeleft
show rin basic_deadpannormal_close at closeright
show bg school_roof at center
with charamoveinleft



"Je m'assieds sur le bout du banc pour prendre le moins de place possible. C'est plutôt étroit mais on arrive quand même à tous tenir."


hi "C'est une vue impressionnante."

show emi basic_closedhappy_close
with charachange


"Emi retient un rire et place un panier-repas en face de Rin, et m'en tend un autre."

show emi excited_proud_close
with charachange


emi "Et voilà ! Un déjeuner, comme promis."


"Fait maison, pas moins. Je suis impressionné."


hi "Woaw. Ça a l'air vraiment bon."

show emi excited_amused_close
with charachange


emi "Merci ! Je les fais moi-même quand j'peux."


"La conversation s'éteint dès que je commence à manger."

show rin basic_awayabsent_close
with charachange


"Après quelques bouchées, je relève la tête et remarque Rin ouvrant habilement sa boîte et amenant un morceau de nourriture dans sa bouche en n'utilisant que ses pieds."


"Même si je l'ai déjà vu avant, je ne peux rien faire d'autre qu'être impressionné par sa dextérité."


"Ça me rappelle aussi dans quel genre d'endroit je suis actuellement."


"Est-ce que je vais m'habituer un jour à voir des choses comme ça ?"


"Je n'arrive pas à me décider si être habitué à quelque chose comme ça serait une bonne ou une mauvaise chose."


"Est-ce que m'habituer à cet endroit veut dire que je renonce à être une personne normale ?"


"Ou ça veut juste dire que je deviens plus compréhensif à propos des gens autour de moi ?"


"Je suis distrait de mes pensées par la vue d'Emi dévorant son déjeuner comme s'il avait insulté ses ancêtres."

show rin basic_absent_close
with charachange


hi "T'as l'air d'avoir vraiment faim."

show emi basic_grin_close
with charachange


"Emi relève la tête, la bouche à moitié pleine, et avale avant de hocher la tête."


emi "Ma course du matin m'ouvre toujours l'appétit."

show emi basic_closedhappy_close
with charachange


emi "Ce qui est super, parce que je brûle tout le déjeuner plutôt rapidement."

show emi excited_proud_close
with charachange


emi "Et m'aide à garder ma silhouette féminine."

show rin basic_deadpan_close
with charachange


rin "Il arriverait quoi si tu la perdais ? Tu deviendrais un homme ?"


"Je suis près de m'étouffer avec mon repas en essayant de ne pas rire."

show emi basic_annoyed_close
with charachange


emi "C'est une façon de parler."

show rin basic_deadpandelight_close
with charachange


rin "Et ta silhouette doit courir le matin aussi ?"


hi "Vous parlez toujours comme ça ?"

show rin relaxed_surprised_close
show emi basic_confused_close
with charachange


$ doublespeak(emi, rin, "Parler comme quoi ?", "Comme quoi ?")


"Je pense que ça répond à ma question."


hi "Euh, laissez tomber."


hi "Donc, euh..."


"Je lutte pour trouver les mots, et pose la question évidente."


hi "Comment vous vous êtes rencontrées ?"

show rin basic_awayabsent_close
with charachange


"Rin semble se contenter de laisser Emi répondre à la question."

show emi basic_grin_close
with charachange


emi "Quelqu'un au département du logement a pensé qu'on se complétait bien l'une l'autre, donc on a été assignées à des chambres voisines."


hi "Complétait l'une l'autre ?"

show rin basic_deadpannormal_close
with charachange


rin "Comme des chaussures et un costume."


hi "Hein ?"

show emi basic_closedgrin_close
with charachange


"Emi rit de ma confusion."


emi "Mets-nous ensemble et on a tous nos membres, tu vois ?"

hi "Ah."

show emi basic_happy_close
with charachange


emi "Donc j'ai commencé à aider Rin à se préparer le matin, et c'est tout !"

show emi basic_grin_close
with charachange


emi "Je veux dire, tu ne peux pas aider quelqu'un à s'habiller tous les matins et ne pas t'entendre avec elle."


hi "Je vois."


"Rin choisit ce moment pour intervenir."

show rin basic_deadpan_close
with charachange


rin "J'ai du mal avec les chemises."


hi "Oui, ça semble... plutôt évident."

show rin basic_surprised_close
with charachange


rin "Vraiment ?"


hi "Un peu... ?"


"Ça n'aide pas, mais au moins Emi semble trouver ça drôle."


"Ça, combiné avec le fait que Rin est vraiment curieuse, ça me fait me sentir mieux, et pourtant, confus."


hi "Je veux dire, t'as pas de bras."



hi "Donc, euh, mettre une chemise semble être quelque chose qui serait... difficile."


"Tu sais quoi ? Je vais juste me taire maintenant."


"Ça va me sauver de bien des ennuis à long terme."


"Rin hoche la tête avec ce que je suspecte être de la sagesse."

show rin basic_lucid_close
with charachange


rin "Je vois."

show rin basic_absent_close
with charachange


"La conversation prend fin dès que je détourne mon attention sur mon déjeuner."


"C'est vraiment très bon."


"Emi finit son repas en premier et émet un grognement satisfait."

show emi excited_laugh_close
with charachange


emi "Ah, c'était bon."


"Pendant qu'elle est occupée à essuyer les restes de son déjeuner, Rin parle."

show rin basic_deadpan_close
with charachange


rin "J'ai soif."

show emi basic_shock_close
with charachange


emi "Oh ! J'ai presque oublié ! Désolée !"

show emi basic_closedgrin_close
with charachange


"Avec un grand geste, elle attrape son sac et en sort trois briques de jus de fruit."


"Elle me lance ce qui semble être du jus de canneberge, il y en a une pour Rin qui semble être une sorte de lait à la fraise (complétement rose), et en garde une (tout aussi rose) aux fruits pressés pour elle-même."

show rin basic_awayabsent_close
with charachange


"Rin plante adroitement sa paille dans le haut de sa brique et commence à boire."


"Je suis encore une fois impressionné par sa souplesse, mais cette fois je garde mon commentaire pour moi."


"Je ne crois pas que Emi ou Rin soit le genre de personnes à penser à deux fois à la façon dont elles se débrouillent avec leurs handicaps particuliers."


"Et spécialement Rin."


"En effet, elle donne l'impression d'être totalement ignorante du fait qu'il lui manque des membres."


"Que ce soit ou non une décision consciente, c'est une autre affaire."


"Je ne suis franchement pas sûr."

show emi basic_grin_close
with charachange


emi "Alors Hisao, tu trouves ça comment ici ?"

show rin basic_absent_close
with charachange


hi "Hmm ?"


hi "C'est plutôt bien, en fait. J'aime bien les endroits élevés, pour la vue."


hi "Merci de m'avoir invité ici."


hi "Et pour le repas, aussi."

show emi excited_amused_close
with charachange


"Emi fait un sourire de mille watt, contente de ma réponse, apparemment."


emi "Aucun problème !"

show emi excited_proud_close
with charachange


emi "N'hésite pas à manger avec nous la prochaine fois aussi, d'accord ?"


emi "Je ne te ferai pas de déjeuner, mais tu peux apporter le tien ici."


hi "Pas de service déjeuner ? Je sais pas..."

show emi basic_annoyed_close
with charachange


"Emi affiche un air ironiquement offensé."


emi "Tu essayes de tirer avantage de ma gentillesse ?"


emi "Quel culot !"

show emi basic_closedgrin_close
with charachange


"Elle rit."

show emi sad_depressed_close
with charachange


emi "Eh bien, si c'est ta réponse, je pense que Rin et moi continuerons à manger toutes seules..."


"Je suis soudainement attaqué par le plus déchirant regard de chiot que je n'ai jamais vu sur le visage d'Emi."


hi "Je rigole ! Je plaisantais !"


hi "J'adorerais manger mon déjeuner ici."


hi "Bon emplacement, et la compagnie est pas mal aussi."

show emi basic_grin_close
with charachange


"Emi fronce les sourcils à ma déclaration de “pas mal” mais semble plutôt contente que j'aie accepté son invitation."


"J'imagine que ça fait de nous des amis maintenant."


"Ou du moins des connaissances."

play sound sfx_warningbell


"La cloche sonne, signalant l'heure de redescendre."

show emi basic_hes_close
with charachange


emi "Rin, tu n'as pas fini ton repas encore une fois !"

show rin basic_deadpan_close
with charachange


rin "Je n'avais pas si faim."

show emi basic_annoyed_close
with charachange


emi "Si tu ne manges pas plus, tu vas t'évanouir !"

show rin relaxed_boredom_close
with charachange


"Rin hausse les épaules, comme si c'était un risque acceptable."

stop music fadeout 4.0


hi "Allez, on ferait mieux d'y aller."

stop ambient fadeout 2.0

scene bg school_staircase1
with locationchange


"Nous partons tous les trois dans les escaliers."

scene bg school_scienceroom
with shorttimeskip


"Les cours de l'après-midi passent. Encore une fois, je me retrouve sans rien à faire après l'école, donc je me dirige vers la bibliothèque pour rendre quelques livres que j'ai fini de lire."

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

scene bg school_library
with locationskip


"En rentrant, je vois qu'il y a à peu près autant d'étudiants ici qu'il y en avait mardi, c'est d'autant presque évident avec le silence total qui enveloppe la pièce."

play sound sfx_impact2
with vpunch

show yuuko panic_up at center
with easeinbottom

play music music_happiness fadein 2.0


"Pendant que je lâche les livres que j'avais empruntés dans le casier de retour qui est sur le comptoir, Yuuko apparaît soudainement derrière, surprise du bruit que ça a fait quand ils ont heurté le casier à côté d'elle."


hi "Ah, désolé Yuuko. Je ne voulais pas vous surprendre."

show yuuko worried_up
with charachange


yu "Non, non. C'est bon. Ça arrive... souvent. Je suis habituée maintenant."

show yuuko neurotic_up
with charachange


yu "Hum, je peux t'aider ?"


hi "C'est bon, je pense que je sais où tout se trouve. Merci quand même."

hide yuuko
with charaexit


"Je pense que je vais emprunter un ou deux autres livres pendant que je suis là. Il n'y a pas grand-chose d'autre à faire, et après avoir autant lu durant mon séjour à l'hôpital, c'est devenu une habitude dure à rompre."

stop music fadeout 5.0


"Je me promène dans la section science-fiction à l'arrière de la bibliothèque, scrutant les étagères pour quoi que ce soit qui me sauterait aux yeux."


"Pendant ce temps, je regarde dans le coin où Hanako était la dernière fois que je me trouvais ici, ne m'attendant pas à grand-chose."

scene ev hana_library_read_std
with locationskip


"...étonnamment, pourtant, elle est là, complètement absorbée dans un livre assez épais. Je décide de ne pas la gêner comme la dernière fois et de retourner à ma recherche de livres à lire."

scene bg school_library_ss
with shorttimeskip

play music music_tranquil fadein 6.0


"Après une durée indiscernable de temps passé à parcourir les allées, je me décide finalement pour deux livres à prendre et les sors de l'étagère."


"Avec un minimum de tapage, je marche rapidement jusqu'au comptoir, fais enregistrer les livres et les mets dans mon sac pendant que je sors."

scene bg school_courtyard_ss
with locationskip


"Au moment où je sors du bâtiment principal, le soleil n'est pas encore totalement couché. Il reste quelques élèves, mais la majorité sont partis ; sans doute dans leurs maisons et dortoirs."




label fr_A29c:

scene bg school_dormhisao_ss
with locationskip


"Me sentant complétement vide, je me dirige vers ma chambre pour lire les livres que j'ai empruntés. J'ai eu bien suffisamment d'action et d'excitation pour la journée."


"Le premier est “Alice au pays des merveilles”. Je connais l'histoire, bien sûr, mais je n'ai jamais lu le livre original."


"C'est juste aussi fou que ce que je me rappelle de l'histoire, avec les personnages loufoques et l'intrigue absurde."


"Je commence à penser que je suis moi aussi une sorte d'Alice, dégringolant, impuissant, dans le terrier du lapin dans ce Pays Imaginaire Handicapé."


"...D'accord, c'est une expression un peu forte. Pourtant, l'endroit isolé et la manière dont l'école s'adapte à absolument tout sont inquiétants. C'est comme un autre monde."


"Je me demande pourquoi je ne peux pas ébranler le sentiment d'être un étranger comme Alice, en dépit du fait que presque tout le monde est si accueillant et amical avec moi."


"Tournant une autre page, mon esprit commence à dériver loin du livre. C'est silencieux, je peux entendre le battement de mon cœur heurter le tissu de ma chemise."


"Pour je ne sais quelle raison, je me sens vraiment mal depuis ce qui s'est passé dans la forêt avec Iwanako. Comme si j'étais enfermé dans une cage avec quelque chose d'agressif et effrayant."

stop music fadeout 5.0

scene bg school_dormhisao_ni
with Dissolve(3.0)


"Je pose le livre pendant un moment et regarde le plafond, prenant mon temps pour me débarrasser de ce sentiment."


"200 pages plus tard, je m'endors."

scene black
with shuteye




label fr_A30:

scene bg school_courtyard_ss
with None

$ renpy.music.play(music_tranquil, fadein=3.0, if_changed=True)


"Je devrais aller acheter des trucs. Je ne peux pas continuer à aller à la cafétéria ou aller manger dehors durant mon année ici."

scene bg school_gate_ss
with locationchange


"Alors que je passe la porte, je fais quelques étirements pour essayer d'atténuer la fatigue qui s'est accumulée au cours de la semaine."

scene bg school_road_ss
show lilly back_smileclosed_ss at center
show lillyprop back_cane_ss at center
with locationchange




"Après avoir traversé et tourné au coin, je vois un personnage solitaire marcher en descendant en direction de la petite ville plus loin. La couleur de ses cheveux et le bruit de sa canne ne trompent pas."

show lilly cane_surprised_ss
hide lillyprop
with charachange


"Je marche rapidement jusqu'à elle, ce qui semble attirer son attention sans qu'un mot ait besoin d'être dit."


hi "Salut, Lilly."

show lilly cane_weaksmile_ss
with charachange


"Elle prend un moment pour placer ma voix, ajustant légèrement sa tête pour faire mieux face à la source vocale."



show lilly cane_smile_ss
with charachange


li "...Hisao ?"


hi "Yep, c'est moi."


"Elle semble avoir une bonne mémoire pour les voix. Le fait qu'elle ait effectivement réussi à s'en souvenir est une agréable surprise."


li "Bonsoir. Qu'est-ce qui t'amène ici ?"

show lilly cane_weaksmile_ss
with charachange


"Encore une fois, elle se courbe poliment. Et, encore une fois, je fais de même poliment avant de réaliser que je n'ai pas à le faire."


hi "Je vais juste en ville. Et toi ?"

show lilly cane_ara_ss
with charachange


li "Eh bien, eh bien, quelle coïncidence."


hi "On fait la même chose, hein ?"

show lilly cane_smile_ss
with charachange


li "Mmh. Je vais habituellement faire les courses le vendredi."

show lilly cane_surprised_ss
with charachange


"Elle fait une pause pendant un moment, ayant l'air soudainement un peu perdue."


li "Cela dit, Hanako vient habituellement en ville avec moi."


"Ah. Pas perdue, mais inquiète. Elles semblent être très proches toutes les deux. C'est un peu surprenant que Hanako puisse simplement oublier Lilly comme ça."


hi "Je l'ai remarquée lisant à la bibliothèque. Elle est probablement coincée dans un livre."

show lilly cane_weaksmile_ss
with charachange


"Elle laisse échapper un petit soupir de soulagement."


li "Merci. Elle a l'habitude de faire ça."


hi "Lectrice avide ?"

show lilly cane_smile_ss
with charachange


li "Exact. Elle n'aime pas être avec beaucoup de gens, donc lire loin de tout le monde lui permet de se détendre un peu."


"Même si elle n'en avait pas l'intention, je ne peux pas m'empêcher de grimacer en me rappelant ma première rencontre avec elle."

show lilly cane_smileclosed_ss
with charachange


"Ne voulant évidemment pas en parler, je reste silencieux pendant que nous continuons sans un mot notre marche sur la route tranquille."


"Tac, tac. Tac, tac."


"Avec la route dépourvue de voitures et les étudiants de Yamaku de plus en plus loin derrière nous, le bruissement silencieux des feuilles et le tapotement mesuré de la canne de Lilly contre le trottoir sont tout ce qui peut se faire entendre."


"C'est plutôt pas mal, spécialement comparé à l'agitation de l'endroit où j'avais l'habitude de vivre."


"Avant que je m'en rende compte, je me suis tellement détendu qu'un bâillement prolongé s'échappe sans que je puisse le contrôler."

show lilly cane_giggle_ss
with charachange


li "Fatigué ?"


hi "Ouais, c'était plutôt la course ces derniers jours."


"C'est un euphémisme, évidemment. Être transféré dans une autre école serait déjà difficile, mais rien à côté de ça..."

show lilly cane_smile_ss
with charachange


li "Eh bien, heureusement tout devrait se ralentir pour toi. Le festival met tout le monde en vrille en ce moment, et tu es apparu en plein milieu."


"Pendant un moment j'ai hésité, mais étant donné son apparente tolérance à la franchise, je décide de lui dire le fond de ma pensée."


hi "J'imagine. Yamaku est différent quand même. Je veux dire, les formalités entourant tout ça, l'isolement du campus... sans mentionner la différence la plus évidente."


hi "C'est un état d'esprit complétement différent. Je vais sûrement m'y habituer, avec le temps."

show lilly cane_smileclosed_ss
with charachange


"Elle fait un hochement de tête approbateur, apparemment satisfaite de ma réponse. Je me sens presque comme si elle m'avait inclu dans le troupeau d'élèves qu'elle mène, avec la classe 3-2 et Hanako."


"Bah, pas que ça m'intéresse. C'est bien de penser à autre chose qu'à ma poitrine en tout cas."

show lilly cane_smile_ss
with charachange


li "Regardant le bon côté des choses, on peut y voir la chance pour un nouveau commencement. Tu devrais chérir l'opportunité de te faire de nouveaux amis."


"C'est optimiste. Cela dit, c'est une bonne chose d'avoir une attitude positive à propos de telles choses, en y pensant."


hi "J'imagine que c'est une bonne façon de voir les choses."

scene bg suburb_roadcenter_ss
show lilly cane_reminisce_ss at center
with shorttimeskip

stop music fadeout 6.0


"Marchant sur la route descendante, elle semble être devenue quelque peu troublée. Avant que je puisse demander ce qui la perturbe, elle se ressaisit et parle d'autre chose."

show lilly cane_weaksmile_ss
with charachange


li "Donc, tu vas où en ville ?"


"C'est effectivement une très bonne question. Je suis venu pour acheter à manger, mais la disposition de l'endroit m'est encore étrangère."


"J'avais l'intention de me balader et voir ce que je pouvais trouver, mais avec le coucher de soleil approchant déjà et la nuit qui n'est pas trop lointaine, ça ne semble pas très sage."


"Je vais devoir lui demander mon chemin. Encore."


hi "Je vais juste acheter à manger... mais maintenant que tu en parles, je ne connais pas vraiment le chemin."

show lilly cane_planned_ss
with charachange


li "Eh bien, tu as de la chance. J'allais justement à la supérette moi-même."


hi "On dirait que je vais encore devoir compter sur toi, alors. Merci."


"Nous marchons ensemble vers le magasin, mon rythme soigneusement ralenti pour rester à côté d'elle. Comparé à mon rythme de pas habituel, le sien est un peu plus lent. Non pas que ce soit sans raison."

scene bg suburb_konbiniext_ss
with shorttimeskip

play music music_daily fadein 2.0


"Après ce qui n'a pas pu être plus que quelques minutes, j'ai l'objectif dans ma ligne de mire. Cette ville est vraiment très petite."

scene bg suburb_konbiniint
with locationchange


"Sans plus attendre, nous rentrons à l'intérieur avec des salutations depuis le comptoir."

show lilly cane_weaksmile at center
with charaenter


li "Ça te gêne si je cherche avec toi ? Habituellement Hanako m'aide, mais vu qu'elle n'est pas là..."


"Ça me prend un moment avant de réaliser ce qu'elle veut dire."


"Considérant qu'elle n'est pas capable de lire les emballages, faire ses courses sans aide doit être très difficile pour elle."


"Cela dit, je ne peux pas me retirer de la tête qu'elle a eu cette idée depuis que j'ai dit que je venais ici."


hi "Bien sûr. Ça serait avec plaisir."


"Je prends deux paniers rouges un peu usés dans la petite pile à l'entrée, en donnant un à Lilly."

show lilly cane_weaksmile at Transform(ypos=800)
with charamove

show lilly basic_smileclosed at Transform(ypos=800)
with charachange

show lilly basic_smileclosed at center
with charamove


"Elle le pose sur le sol, met son cartable dedans, rétracte sa canne et la glisse à travers les poignées du panier avant de le ramasser avec sa main droite."


"Mais, si elle n'utilise pas sa canne..."

show lilly basic_smileclosed at Slide(0.5,0.5,0.3,0.5,1.0, time_warp=_ease_time_warp)
with None

show lilly basic_smileclosed_close at Slide(0.5,0.5,0.3,0.5,1.0, time_warp=_ease_time_warp)
with Dissolve(1.0)


"Avant que je puisse finir ma pensée, elle vient à côté de moi et attrape la manchette de mon uniforme de ses doigts fins."

show lilly basic_concerned_close at twoleft
with characlose


li "Ça ne te gêne pas ?"


hi "Non, pas de problème."

show lilly basic_smileclosed_close
with characlose


"Je n'ai aucune raison de refuser. Il y a des choses pires que de faire les courses avec une jolie fille accrochée à moi, même si c'est par nécessité."


"Nous poursuivons notre route dans le magasin, et aucun des occasionnels clients qui passent n'ont l'air de ciller."


"Considérant à quel point Yamaku est près d'ici, j'imagine que voir des étudiants de là-bas doit être tout à fait normal pour les résidents locaux."


"Pendant que nous parcourons chaque allée, je vérifie rapidement avec Lilly et trouve ce qu'elle cherche. Je prends en même temps ce dont j'ai besoin, et mets nos articles dans nos paniers respectifs."


"J'imagine que c'est la même routine que Hanako et elle suivent chaque vendredi."


hi "Bien, il reste que le pain et ça devrait être bon pour moi. Tu as besoin de quelque chose d'autre, Lilly ?"

show lilly basic_smile_close
with characlose


li "Non, ça devrait être tout."


hi "Allons-y alors."

show lilly basic_smileclosed_close
with characlose


"Avec un crochet rapide à la section boulangerie, nous nous dirigeons vers le comptoir."


"La file d'attente, heureusement, est presque inexistante. Il ne faut pas longtemps avant que nous payions tous les deux pour notre nourriture et passions la porte."

scene bg misc_sky_ni at Fullpan(15.0)
with locationchange


"Pendant que Lilly étend sa canne sur toute sa longueur, je perds une minute à regarder le ciel nocturne, tenant nos deux sacs."


"Pendant un moment j'essaye de faire de la fumée avec mon souffle, mais la chaleur de l'été ne semble pas coopérer."


"Finalement elle se redresse, s'étire rapidement avant de prendre son sac et de me laisser avec les deux miens."

scene bg suburb_konbiniext_ni
show lilly cane_listen_ni at center
with locationchange


hi "T'es fatiguée aussi ?"

show lilly cane_sleepy_ni
with charachange


li "Les préparations du festival ont été un chaos total. Shizune me marchant sur les talons n'arrange pas les choses, non plus."


hi "Hé, elle essayait juste de faire en sorte que tout soit organisé. Vaut mieux maintenant que plus tard, non ?"

show lilly cane_weaksmile_ni
with charachange


li "Je suppose. Je vais apprécier de me détendre en ville demain, ça c'est certain."


"Je suppose que les préparations du festival doivent se faire sentir sur elles deux."

scene bg suburb_roadcenter_ni at bgright
with locationchange


"Nous marchons dans la rue calme, parlant entre nous tout en portant nos sacs de nourriture et de fournitures du magasin."


"...Attends, c'est quoi ça ?"


"Je remarque une personne très distinctive faisant chemin vers nous, sa silhouette éclairée par les réverbères."


"Pendant une seconde je crois que c'est un autre étudiant de ma classe, mais quand il, ou devrais-je dire elle, se rapproche, je la reconnais rapidement."

show bg suburb_roadcenter_ni at center
show rin relaxed_nonchalant_ni at right
with charamoveinright

stop music fadeout 8.0


hi "Rin ? Qu'est-ce que tu fais ici aussi tard ?"

show lilly cane_surprised_ni at center
with charaenter


li "Rin ?"


"Lilly penche la tête, ayant l'air d'essayer de se concentrer pour mieux écouter. Il me vient soudainement que je devrais probablement lui représenter la scène."


hi "C'est Rin... Tezuka, je crois que c'est son nom de famille, elle est de notre école."

show lilly cane_weaksmile_ni
with charachange


"Elle se raidit au nom et affiche une expression compliquée, quelque chose comme une fusion forcée entre un sourire tranquille et une grimace douloureuse."


li "Ah. Je comprends."


"J'imagine que Lilly connaît Rin aussi."

show rin basic_awayabsent_ni
with charachange

show bg suburb_roadcenter_ni at bgleft
show rin basic_awayabsent_ni at tworight
show lilly cane_weaksmile_ni at twoleft
with charamove


"Rin se tourne vers nous, ayant l'air terriblement absente. J'hésite un peu entre le fait qu'elle ne nous reconnaisse pas et celui qu'elle ne le montre pas."


"Elle a l'air d'un zombie. Ou d'une statue. Une statue d'un zombie."


"Mais doucement, certains signes de compréhension semblent apparaître dans ses yeux sombres : quelque chose qui a dû la faire réagir."

show rin basic_lucid_ni
with charachange

show rin basic_awayabsent_ni
with charachange


"Rin cligne une fois des yeux. Très doucement."

show rin basic_absent_ni
with charachange


rin "Bonjour."

"…"


"C'est une pause un peu gênante, tout le monde attendant que quelqu'un d'autre dise quelque chose."


hi "Qu'est-ce que tu fais ici aussi tard ?"

"…"


rin "Je..."

show rin basic_deadpan_ni
with charachange


rin "Je me le demandais aussi. À l'instant."

play music music_rin fadein 0.5

show rin basic_deadpannormal_ni
with charachange


rin "Des gens m'ont posé la question juste avant. J'imagine qu'ils se demandaient la même chose."


rin "Je ne savais pas. Ils ne savaient pas non plus. J'ai posé la question. C'est pourquoi je me demande."


rin "Donc c'était plutôt ça. C'est un meurtre mystérieux sans meurtre."

"…"

show rin negative_spaciness_ni
with charachange


rin "Ils allaient par là."

show rin basic_absent_ni
with charachange


"Elle se tourne vers la droite pour montrer la direction qu'ont pris les autres gens comme si c'était important, et repivote le dos comme un pantin mécanique dans l'une de ces horloges très compliquées."


"Pour une personne qui donne l'impression d'être du type tranquille, Rin utilise vraiment beaucoup de mots pour dire des choses qui n'ont pas besoin d'être dites."


"N'étant pas sûr qu'elle ait terminé, je ne dis rien. Pareil pour Lilly, qui semble tout aussi pauvre en mots pour le moment."


"Je pense qu'en fait nous avons tous les deux peur qu'une réponse puisse provoquer une suite de sa part."


"Notre manque évident de réaction ne déconcerte pas du tout Rin. Elle continue de nous regarder dans l'expectative, un soupçon d'expression calme sur son visage vierge."


"Elle semble être ce type de personne. Toujours aussi détendue."


"Comme si du sédatif pour éléphant coulait dans ses veines à la place du sang."

show lilly cane_concerned_ni
with charachange


li "Tu souffres d'amnésie ? Je ne me souviens pas que tu aies quelque chose de la sorte, cependant..."


hi "Non, je ne pense pas que ce soit ça."


hi "Les autres passants devaient juste être inquiets, je pense. Tu as l'air vraiment perdu, à rester debout là au milieu de la rue."

show rin basic_deadpan_ni
with charachange


rin "Oh, je vois."

show rin relaxed_nonchalant_ni
with charachange


rin "Peut-être que je devrais prendre un autre genre de pose dans ce cas."


"Je me demande pendant un moment si je dois poursuivre dans ce sens, ou abandonner dans l'intérêt de ma propre santé mentale."


"Je choisis la deuxième solution."


"Apparemment la plupart du temps, il vaut mieux ne pas approfondir ce dont parle Rin."


"Parler avec Rin est comme jouer aux échecs avec un supercalculateur qui fait des mouvements totalement aléatoires comme pour se moquer de tout ce que vous savez à propos des échecs. C'est comme ça, mais avec l'interaction humaine."


"Et même si je gagne, j'ai l'impression d'avoir perdu."


"Rah, exactement comme Kenji l'a dit. Même quand je gagne, je perds. Est-ce là le pouvoir des filles de Yamaku ?"

"…"


"Je mets la pensée de côté, elle est trop dangereuse pour continuer plus loin. C'est probablement juste la propagande anti-féministe de Kenji qui m'atteint dans un moment de faiblesse."


hi "Ouais, peut-être que prendre une autre pose aurait marché."


hi "Bref, tu as une idée de ce que tu fais là ?"

show rin negative_annoyed_ni
with charachange


"Elle fronce les sourcils, l'air extrêmement mécontent à cause de ma question, ses conséquences, ou de la réponse qu'elle va donner."


rin "J'en ai une. Une idée. Je ne peux pas vraiment dire quel genre d'idée."

show lilly cane_smile_ni
with charachange


li "Ça a l'air de progresser, au moins."


"Lilly a l'air d'avoir repéré une ouverture pour une sorte de conversation normale. Je ne peux pas dire que je partage son optimiste."


rin "Oui, il y a du progrès. Définitivement. Le reste viendra plus tard."

show rin basic_deadpanupset_ni
show lilly cane_weaksmile_ni
with charachange


rin "J'en suis sûre. J'ai toujours des... raisons."


"Le silence qui suit ne tue l'espérance de Lilly que trop visiblement. Ça n'a pas duré longtemps."


"Pour Rin, pour autant que je puisse dire, sans fondement, conviction mise à part... qu'est-ce qui devrait être fait ?"


"On pourrait juste la laisser à ses trucs, quels qu'ils soient... mais il est tard et je ne pense pas que nous serions remerciés si Rin est trouvée se tenant ici au milieu de la nuit."


"Et elle y sera sûrement, sauf si elle parvient à se rappeler ce qu'elle faisait ici à l'origine."


"Quant à moi, s'il faut essayer de deviner ce qui lui est passé par la tête quand elle a décidé de s'embarquer dans cette aventure, les chances semblent égales à celles de gagner à la loterie."


"Plusieurs fois d'affilée."


"Lilly est étrangement silencieuse aussi. J'apprécierais un certain appui de sa part à ce moment, spécialement si elle est plus habituée à Rin que je le suis."


"Mais on n'y peut rien. Il semblerait que sa familiarité avec Rin soit exactement la raison pour laquelle elle est restée discrète."


hi "Donc, je suppose que tu allais quelque part, tu ne revenais pas à l'école... une idée de où ?"

show rin relaxed_surprised_ni
show lilly cane_surprised_ni
with charachange


"Ses yeux s'agrandissent sous le choc et elle recule d'une façon un peu artificielle, rendant évident le fait qu'elle ait déjà agi de cette façon lors de situations de ce genre."


rin "Tu lis dans les pensées ? C'est ça ton handicap ? Vraiment unique !"


hi "Non... Quoi ? Pourquoi tu penserais ça ?"

show rin relaxed_disgust_ni
show lilly cane_listen_ni
with charachange


rin "Tu savais ce que je faisais."

show lilly cane_displeased_ni
with charachange


hi "Eh, c'était juste une supposition éclairée. On marchait dans la même rue dans l'autre direction juste avant, pour aller au magasin."


hi "Si tu allais à l'école, on se serait croisés en chemin."

show rin basic_deadpanupset_ni
with charachange


rin "Oh."


"Elle a l'air un peu déçue."


"Comme Kenji, Rin est plutôt rapide pour sauter aux conclusions complètement irrationnelles."


"Peut-être que c'est quelque chose dans l'eau d'ici. Je me fais un petit mémo comme quoi je devrais commencer à stocker de l'eau minérale."


hi "Tu sais, c'est la deuxième fois cette semaine que quelqu'un me demande si je suis un devin."


hi "Je donne vraiment cette impression ?"

show rin basic_deadpannormal_ni
with charachange


"Rin hausse les épaules, ce qui est la seule réponse que j'obtiens."


hi "Tu sais—{w=0.3}{nw}"

show lilly cane_smile_ni
with charachange


li "Peut-être que tu devrais retourner avec nous à l'école ?"


"Lilly me devance juste quand j'étais sur le point de discréditer mes prétendus pouvoirs divinatoires. Elle a l'air plutôt inquiète, le sourire confus sur son visage dissimule mal ce fait."


"Peut-être qu'elle est arrivée à la même conclusion que moi. Pour le bien de tout le monde, je décide de laisser tomber le sujet du devin, c'est idiot de toute façon."


hi "Ouais, Lilly a raison. Si tu ne peux pas t'en rappeler, ça ne sert à rien de rester ici."

show rin basic_awayabsent_ni
with charachange


"Rin réfléchit à cette simple déduction pendant un moment, puis hoche la tête."

show rin basic_absent_ni
with charachange

stop music fadeout 2.0


rin "D'accord."

scene bg school_road_ni
with shorttimeskip

$ renpy.music.set_volume(0.1, 0.0, channel="ambient")
play ambient sfx_cicadas
play music music_dreamy fadein 2.0


"Nous partons de nouveau vers l'école, après avoir perdu plus de temps que nécessaire avec cet épisode."

show rin basic_awayabsent_ni at tworight
show lilly cane_smileclosed_ni at twoleft
with charaenter


"Rin marche au bord du trottoir, à sa manière arythmique, ressemblant à un mélange entre un somnambule et un funambule, pendant que Lilly garde une main sur mon épaule, tapotant le sol avec sa canne."


"Tac tap tap tac tac tac tap tap tap."


"À part ça et quelques fragments de début de conversation, c'est calme. Un calme vraiment différent de celui relaxant de la ville, cela dit."


hi "Donc comment va le mur ?"

show rin basic_deadpan_ni
with charachange


rin "On va être malchanceux. Ne jamais parler d'un travail en cours."

show lilly cane_weaksmile_ni
with charachange


li "Je suis sûre qu'il sera magnifique."

show rin basic_deadpannormal_ni
with charachange


rin "Malchance."


"Tac tap tap tac. Elle ne se gêne pas pour en parler. La politesse de Lilly semble hors propos, pour la première fois. Tap tap tap."


"La colline sur laquelle repose Yamaku a une pente étonnamment abrupte en montée. Nous ralentissons le rythme, mais je sens quand même mon pouls et ma respiration devenir plus lourds."


"On y est presque, je peux déjà voir le portail."


"Plus important que ça, cependant, je remarque que la main de Lilly se resserre légèrement sur mon épaule. Interprétant ça comme le signe qu'elle veut demander quelque chose, j'ouvre la bouche."


hi "Un problème, Lilly ?"


"Je résiste à l'envie de dire “A part notre compagne de voyage ?” Mais uniquement de justesse."


"Pendant un moment elle semble se demander si elle doit en parler, mais le fait en fin de compte."

show lilly cane_concerned_ni
with charachange


li "Est-ce que tout... va bien ?"


hi "Bien ? Qu'est-ce que tu veux dire ?"


"Le fait que je ne puisse pas interpréter sa question incroyablement vague la déstabilise durant une seconde."


li "C'est juste que... tu me sembles anormalement fatigué."


"Maintenant qu'elle le dit, je remarque que ma respiration est étrangement lourde. La montée à pied m'a été vraiment difficile."


label fr_choiceA30:
menu:
    with menueffect
    "Lilly l'a remarqué trop vite..."
    "Désolé, je ne suis pas trop en forme.":




        return m1
    "Je ne veux pas vraiment en parler.":


        return m2

label fr_A30a:

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
stop music fadeout 5.0


hi "Je... Je vais bien."


hi "Il y a pas de quoi s'inquiéter, la colline est juste étonnamment abrupte, tu penses pas ?"


hi "Je me demande pourquoi ils ont fait l'école aussi haute après tout, il y a des étudiants en fauteuil roulant et tout pourtant ?"

show lilly cane_sad_ni
with charachange


li "C'est vrai."

show lilly cane_concerned_ni
with charachange


"Lilly fronce les sourcils avec inquiétude, et je ne veux vraiment pas qu'elle ait ce genre d'expression à mon propos. On se connait à peine."


hi "Ouais, pas qu'on puisse trouver un endroit comme celui-là n'importe où, je suppose, mais je me demande à quoi ils pensaient."


"Ma voix est trop calme, ça sonne bizarre à l'oreille et je parle trop vite. Je me demande ce que Lilly peut déduire de seulement la voix de quelqu'un."

li "Mmm…"


hi "Continuons. On y est presque de toute facon."

hide lilly
hide rin
with charaexit


"Pendant le reste de la route pour retourner à l'école, nous gardons le silence."


stop ambient fadeout 3.0

scene black
with Dissolve(3.0)


label fr_A30b:

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")


hi "Ça va, j'ai juste besoin de reprendre mon souffle. Je suis pas vraiment en forme, ces jours-ci."

show lilly cane_oops_ni
with charachange


li "Oh."


li "Est-ce quelque chose qui... est lié au fait que tu aies été transféré ici ? Je veux dire..."

show lilly cane_concerned_ni
with charachange


"Elle s'arrête elle-même un peu brusquement, peut-être en réalisant qu'elle était un peu indiscrète. Sa supposition était bonne cependant, et même si je n'aime pas le sujet, ce n'est pas comme si j'allais mentir à son propos."


"Si c'est Lilly, ça me gêne pas. Je crois."


hi "Je suis juste un peu faible pour le moment."

show lilly cane_oops_ni
with charachange


li "Hanako a dit que tu avais l'air assez... bien portant, donc j'ai naturellement pensé..."

show lilly cane_sad_ni
with charachange


"Lilly ne finit pas sa phrase à nouveau, la laissant en suspens avec une certaine inquiétude."


"Alors qu'elle plisse le front, l'expression gênée de Lilly me pousse à dire quelque chose pour la rassurer."


"Il est surprenant qu'elle soit aussi peu à l'aise, considérant à quel point elle est directe avec sa propre cécité. Elle doit savoir que tous ne partagent pas son aisance à propos de ces choses."


hi "Non, c'est bon."


hi "J'ai un très... j'imagine que le meilleur terme serait mauvais... cœur. Arythmie."


hi "J'ai eu une attaque cardiaque assez méchante il y a un moment à cause de ça, et j'ai passé la plupart du printemps à l'hôpital. J'ai fini à Yamaku sur ordre du médecin."


"Elle hoche silencieusement la tête, signe de compréhension."


"Ma réponse, cependant, ne semble qu'accentuer le plissement de son front. Elle ne semble pas vraiment savoir comment réagir, étant donné que nous ne nous connaissons pas aussi bien tous les deux."


"Je ne peux pas vraiment l'en blâmer, vu que j'ai eu exactement la même réaction."


label fr_A30c:


"Je suis surpris au moment où son visage montre qu'elle vient de réaliser quelque chose."

show lilly cane_oops_ni
with charachange


li "Attends... donc la fois où Emi et toi vous êtes percutés... ?"


"Je grimace légèrement. Sa capacité à relier les points aussi rapidement est inattendue."


hi "Ouais. Je suppose que je suis un exemple typique de la raison pour laquelle ces règles sur le fait de courir dans les couloirs existent."

show lilly cane_sad_ni
with charachange


"C'est sorti beaucoup plus sec que je l'avais prévu. Lilly n'a visiblement pas envie de continuer sur le sujet."


label fr_A30d:


"Même si j'ai envie de calmer son inquiétude, je n'ai vraiment pas envie de m'attarder sur ça non plus."


hi "Ne t'inquiète pas pour ça."

show lilly cane_weaksmile_ni
with charachange


"J'essaye d'afficher un sourire rassurant mais j'en réalise la futilité. Sans savoir ça, Lilly me montre un sourire rassurant mais ne dit rien de plus."

$ renpy.music.set_volume(0.5, 5.0, channel="ambient")
stop music fadeout 2.0

scene bg school_dormext_half_ni
show rin relaxed_surprised_ni at tworight
show lilly cane_weaksmile_ni at twoleft
with shorttimeskip


"Arrivant aux dortoirs, Rin s'arrête en face de son mur comme si la foudre l'avait frappée. Elle a été tellement silencieuse pendant presque tout le chemin du retour que j'en avais presque oublié qu'elle était là."

show rin relaxed_disgust_ni
with charachange


rin "On est vendredi, hein ?"

show lilly cane_smile_ni
with charachange


li "Oui... Vendredi huit Juin."

show rin basic_upset_ni
with charachange

play music music_rin fadein 0.5


rin "C'est pas bon."

show lilly cane_surprised_ni
with charachange


li "Pas bon ? Pourquoi ?"

show rin negative_annoyed_ni
with charachange


rin "Je pense que je vais me mettre en position fœtale et vomir. Peut-être dans l'ordre inverse."

show lilly cane_concerned_ni
with charachange


li "Il y a un problème ?"

show rin negative_confused_ni
with charachange


rin "Non. Il n'y a pas de problème. C'est vendredi et il n'y a aucun problème pour l'instant. Ce mur, il a besoin d'être fini pour dimanche. Donc tout va bien."

show rin negative_worried_ni
with charachange


rin "Vous avez des drogues ? Ou une machine à voyager dans le temps ?"

show rin negative_confused_ni
with charachange


rin "C'est pas bon. Pas bon."


"Donc elle a du mal à tenir la date limite. Me rappelant l'exaspération de Shizune pour l'insouciance de Rin il y a quelques jours, je ne sais pas quoi penser."


"Elle peut s'attendre à un “je te l'avais dit” sauf si elle arrive à faire tout ce qu'elle doit faire pour dimanche matin."


"Rin continue de fixer le mur ayant l'air aussi mortifiée que possible."

show rin negative_annoyed_ni
with charachange


rin "Laissez-moi. Je vais avoir besoin de travailler pendant un certain temps."


"Je regarde Lilly, espérant partager un regard incrédule avec elle pendant que je roule des yeux, mais je réalise qu'elle n'est pas du genre à faire ce genre de choses."

show rin negative_angry_ni
with charachange


rin "Laissez-moi."

stop music fadeout 2.0

hide rin
with charaexit

show lilly cane_concerned_ni at center
show bg school_dormext_half_ni at bgright
with charamove


"Nous le faisons, bien sûr, ne voulant pas aggraver la situation plus qu'elle ne l'est déjà."


"J'ai une sorte de mauvais pressentiment. Rin a vraiment le don de rendre les gens inquiets à son sujet."


"Elle a l'air d'être le genre de personne qu'il ne faudrait jamais laisser seule."


hi "Peut-être qu'on devrait appeler quelqu'un ? Elle avait l'air d'être en état de choc ou quelque chose comme ça."

show lilly cane_oops_ni
with charachange


li "Je suis sûre qu'elle ira bien. Elle est juste... euh... comment dire..."


"Lilly se creuse un peu la tête, essayant de trouver une manière polie de dire que Rin est folle sans dire qu'elle est folle."


hi "Unique ?"

show lilly cane_weaksmile_ni
with charachange


li "Oui, quelqu'un de vraiment unique."


hi "Je pense que tu peux dire ça."

show lilly cane_giggle_ni
with charachange


"Elle rit mélodieusement à l'idée, hochant la tête pour approuver."

show lilly cane_weaksmile_ni
with charachange


li "Désolée de t'avoir laissé comme ça pendant que tu lui parlais. Je... ne la comprends pas vraiment, donc je garde mes distances."


"Donc j'avais raison. Lilly affiche un léger sourire contrit comme si elle était désolée que ses propres lacunes l'empêchent de devenir plus proche de Rin."


"Je ne suis pas en état de la blâmer. Du tout."


"Lilly laisse échapper un long souffle, probablement un bâillement déguisé. J'imagine qu'elle doit être aussi épuisée que je le suis."

show lilly cane_cheerful_ni
with charachange


li "Je ferais mieux de partir maintenant et de donner ça à Hanako. Merci de ta compagnie, Hisao."


"Elle m'adresse un très gentil sourire. Elle a l'air différente de la normale, en dépit du fait qu'elle semble sourire très souvent."


"Je ne peux pas mettre le doigt sur cette différence. C'est juste différent."


"Relaxée, je dirais, mais c'est probablement un soulagement d'être débarrassée de Rin. Peut-être."


hi "Ouais... bonne nuit. Salue Hanako pour moi."

show lilly cane_smile_ni
with charachange


li "Je le ferai. Bonne nuit."

hide lilly

stop ambient fadeout 2.7

scene black
with Dissolve(3.0)

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
