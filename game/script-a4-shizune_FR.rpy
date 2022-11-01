label fr_S30:

window hide None

scene bg school_library
with locationchange

window show

play music music_happiness fadein 2.0


"Seulement un jour plus tard, le week-end est déjà arrivé. Je pose une grande pile de livres sur le bureau de la bibliothécaire sans intention de les claquer, mais à cause du poids, ça arrive quand même."

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_impact

show yuuko panic_up:
    center
    ypos 1.2 alpha 0.0
    easein 0.25 ypos 1.0 alpha 1.0
with vpunch

show yuuko panic_up:
    center
    alpha 1.0
with None


"Yuuko bondit de sa chaise avec suffisamment de force pour déloger ses lunettes. Elles tiennent encore à peine."

show yuuko neutral_up
with charachange


yu "Oh, salut."


hi "Désolé. Je suis ici pour rendre tous les livres que j'ai en retard."

show yuuko worried_down
with charachange


yu "C'est super, mais j'aurais aimé que tu les ramènes plus tôt. Ça n'aurait pas été un problème si la bibliothèque avait plusieurs copies de chaque exemplaire, mais ce n'est pas le cas... et ils agissent comme si c'était de ma faute."


hi "“Ils ?”"

show yuuko panic_down
with charachange


yu "Les autres étudiants. Ils peuvent être... hum, assez insistants."


hi "Désolé. Ça m'est sorti de la tête, je viens de passer quelques journées assez difficiles."

show yuuko worried_down
with charachange


yu "Oh... Hum, j'imagine que tu n'as pas envie d'en parler..."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve


n "\nYuuko se met à la tâche en remettant en rayon les livres que je viens de rendre, les traitant avec soin et précision extrême, comme si elle était démineur de bombe plutôt que bibliothécaire."


n "Durant les derniers jours, j'ai pensé à ce que Misha m'a dit. Bien sûr, j'ai pensé à tout ce qu'elle a dit, mais une chose en particulier revient toujours. Elle a dit qu'elle ne voulait plus que les gens lui manquent ou être séparée d'eux."


n "Quand je me rappelle ces mots, ils me paralysent, comme une gifle claquant sur la joue. Dans quelques mois, nous serons diplômés. Misha et Shizune étaient presque inséparables, mais après la remise des diplômes, elles ne se reverront peut-être jamais. Je me demande si c'est ça qui a tout fait commencer."


n "Si Misha venait à essayer d'en parler à Shizune, Shizune n'y réfléchirait pas du tout. Ça la rendrait triste, et pour cette raison, elle essayerait de l'ignorer. Pour quelqu'un comme Shizune qui est si rapide pour réprimer ses inquiétudes, ça serait facile."

nvl clear


n "\n\nMisha s'est avérée être plus sensible que je ne l'aurais cru. Ça l'aurait anéantie, encore plus parce que la réaction de Shizune aurait été plutôt glaciale. Je ne sais pas si c'est comme ça que Shizune l'a géré, mais c'est bien possible, et je peux comprendre pourquoi elle ferait ça."


n "Je peux aussi comprendre pourquoi Misha serait troublée par la pensée de s'éloigner de quelqu'un qui est si important pour elle. Je n'avais jamais pensé à la fin d'année jusqu’à maintenant."


n "Puis j'ai commencé à penser à des choses comme “Ça fait vraiment seulement moins d'un an ?” J'ai commencé à penser à tous ceux que j'ai rencontrés. Pas seulement Shizune et Misha, mais tout le monde. C'était des pensées affectueuses. Puis j'ai pensé que j'allais les perdre. Soudainement, je peux comprendre les angoisses de Misha."


n "\nÇa serait bien d'en parler à quelqu'un."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear
window show


hi "En fait, j'en ai envie."

show yuuko worried_up
with charachange


yu "Avec qui ?"


"Je peux sentir la légère touche d’appréhension dans sa voix."


hi "Avec toi."

show yuuko neurotic_up
with charachange


yu "Ah... Vraiment ? Tu es sûr ? P-pourquoi moi ?"


hi "Parce que tu es une adulte."

show yuuko neurotic_down
with charachange


yu "C'est pour ça ? Ahhhh... c'est..."


"Sourcillant, elle gigote un peu sur sa chaise, essayant de se mettre à l'aise dans une position apparemment assez inconfortable. On dirait que ça lui va."


hi "C'est difficile d’être un adulte ?"

show yuuko cry_down
with charachange


yu "Oui."

show yuuko panic_down
with charachange


yu "Je ne pense pas être si vieille cela dit... C'est surprenant que des étudiants maintenant, c-comme Shizune et toi, utilisent des choses comme du parfum ou de l'eau de Cologne... Je n'ai jamais fait ça. D'ailleurs je ne le fais toujours pas..."

show yuuko worried_up
with charachange


yu "Hum, d'ailleurs, tu n'as pas ton eau de Cologne au raisin aujourd'hui."


hi "Ouais, ça ne marche pas bien sur moi."

show yuuko worried_down
with charachange


yu "Oh, c'est bien. Je pensais la même chose... Désolée."


"Yuuko semble vraiment désolée, et je ressens un peu de honte. Je souris, malgré ça. Même un petit mensonge comme ça peut te coûter cher, après tout."


"Pour Misha, essayer de dissimuler comment elle se sentait, et afficher un visage heureux pour Shizune pendant si longtemps a dû être épuisant."


hi "Quelqu'un que je connais a parlé du fait qu'on allait avoir notre diplôme dans pas si longtemps, et j'ai réalisé que je n'y avais jamais pensé auparavant."


hi "Je me sens idiot d'avoir passé tant de temps sans y penser. J'ai rencontré beaucoup de gens super, et je n'ai jamais pensé à ce que ce serait si je venais à finir mon année et à ne jamais les revoir."

show yuuko neutral_down
with charachange


yu "Il y a toujours des moyens pour garder contact..."


hi "Ouais, j'imagine. Je me sens bête. Je sais que tout le monde ressent la même chose, probablement. Je suis sûr que tu entends beaucoup ce genre de choses."

show yuuko worried_down
with charachange


yu "N-non... Je ne travaille pas ici depuis si longtemps..."

show yuuko worried_up
with charachange


yu "J'étais inquiète pour la même chose quand j'ai fini le lycée. Je, hum, n'étais pas scolarisée ici, cela dit. Mes amis me manquent aussi... et j'aurais aimé avoir gardé contact avec eux. J'aurais dû plus m'y appliquer."


"Yuuko ne m'aide pas vraiment à me sentir mieux, et elle se tait rapidement en le voyant sur mon visage."


hi "Je ne veux pas finir avec les mêmes regrets."


hi "Je me demande si Shizune pense à ce genre de choses. Parce qu'elle dit parfois qu'elle ne veut pas vivre avec des regrets."

show yuuko panic_up
with charachange


yu "Wow... ça semble impossible, pour moi..."


"Je hoche la tête, ne voulant pas totalement confirmer ce qu'elle pense."

show yuuko closedhappy_up
with charachange


yu "Même si... Je trouve ça admirable... Presque brave. Tu ne penses pas ?"


hi "“Brave” est une étrange façon de dire ça."

show yuuko neutral_down
with charachange


"Yuuko secoue la tête avec insistance."


yu "C'est vrai, pourtant. Et aussi quelque peu intimidant..."


hi "Roh. Tu ne devrais pas être intimidée par des lycéens."

show yuuko worried_up
with charachange


yu "Je vais essayer..."

hide yuuko
with charaexit


"Elle se tourne pour commencer à plier un post-it plusieurs fois. Un comportement assez normal pour une étudiante à l'université, mais plus important, je me demande si j'ai dit quelque chose de mal."


"Ayant été si longtemps avec Shizune, je ne peux pas m’empêcher de tirer toutes les informations que je peux de ces moments de silence."


"Si Yuuko était le genre de personne qui n'était pas intimidée par des lycéens, ça ne serait probablement pas aussi facile de lui parler."


"C'est trop facile de vouloir cacher ses défauts. Quand je pense à tous les gens que je connais, c'est leurs défauts que je préfère."

show yuuko worried_up at center
with charaenter


yu "Hum..."

show yuuko smile_down
with charachange


yu "Je ne crois pas que je le regrette vraiment. J'y ai pensé, et tant que je me rappelle les bons moments, ça suffit."

show yuuko worried_down
with charachange


yu "Je ne sais pas. ...Désolée."


"Je remarque quelques étudiants entrant dans la bibliothèque, et décide que mon temps est écoulé."


hi "Non, ça m'a aidé."


hi "Je crois que deux de mes amies se disputent parce que l'une d'entre elles prend assez mal le fait qu'on ne se reverra peut-être plus après cette année. Et l'autre est trop stoïque à ce sujet, ce qui empire les choses."


hi "Je ne sais pas comment je suis censé gérer ce genre de situation. Ça ne me semble pas être le genre de problème où je devrais choisir un camp, mais ça pourrait le devenir, et je n'ai aucune idée de ce que je vais faire."

show yuuko neutral_down
with charachange


yu "Tu devrais leur dire qu'elles ne devraient pas se battre."


hi "Je sais. Se battre c'est mal."


hi "Ce n'est pas Shizune et Misha, à propos."

show yuuko worried_up
with charachange


yu "D'accord... Mais euh, je ne pensais pas ça..."


"Vraiment embarrassant. Même si c'était une possibilité, je sens quand même mes joues qui rougissent, et même, je viens de dire un mensonge flagrant. Mais parfois, ça peut être la bonne chose à faire."


hi "Tu as des livres sur les gens qui doivent prendre des décisions difficiles ?"

show yuuko happy_down
with charachange


yu "On a beaucoup de livres sur le développement personnel..."


"C'est drôle que ça me surprenne, ça n'aurait pas été le cas il y a quelques mois."


hi "Je voulais dire “sur” pas “pour”. Il n'y en a pas beaucoup, hein ?"

show yuuko worried_down
with charachange


yu "Oui. Hum, pas beaucoup, je veux dire."

stop music fadeout 3.0


"Bien que j'aie un peu d'appréhension, je veux parler à Shizune. Je ne comprends pas pourquoi je me sens si nerveux, et ça ne me plaît pas."

scene bg school_council
with locationskip


"Ça me motive aussi pour la chercher, bien que je n'aie pas à chercher longtemps, elle est dans la pièce du conseil des étudiants, comme toujours."

play music music_pearly fadein 5.0

show shizu behind_blank at center
with charaenter


"Fait inquiétant, Misha n'est pas avec elle. Quand Shizune me remarque, la première chose que je demande est où elle est."

show shizu basic_normal2
with charachange


ssh "Je ne sais pas."


"Il y a tellement d'incertitude que je ne peux pas me contenter de ça."


his "Elle loupe beaucoup l'école."

show shizu adjust_happy
with charachange


ssh "Es-tu la police des présences ?"


his "Drôle de remarque, venant de la présidente du Conseil des Étudiants."

show shizu adjust_smug
with charachange


"Shizune cache un rire derrière sa main, et je commence à croire que je pourrais m’inquiéter pour rien, mais ensuite son rire s'efface pour laisser place à une expression plus sérieuse et pensive."

show shizu basic_normal
with charachange


ssh "Tu as raison."

show shizu behind_blank
with charachange


ssh "Hier,"

show shizu adjust_happy
with charachange


"J’aperçois un léger sourire sur son visage quand elle voit la panique qu'elle a déclenchée en moi en disant ce mot. Malgré ses efforts, elle ne peut pas s’empêcher d'apprécier surprendre tout le monde."


"Mais même, je peux voir qu'elle a des préoccupations plus importantes que ça et son sourire disparaît."

show shizu basic_angry
with charachange


ssh "...avant que vous ne me remarquiez, j'ai vu ce que vous disiez. Je ne suis pas stupide."

show shizu behind_frown
with charachange


ssh "Même si je n'avais pas entendu, j'ai compris pendant que Misha et moi discutions. Même si elle ne m'avait pas tout dit plus tard. Elle n'en a pas fait une grande histoire, mais quelle que soit la façon dont tu regardes ça, c'est ma faute, hein ?"


his "Et qu'est-ce qu'elle t'a dit ?"

show shizu adjust_frown
with charachange


"Shizune grimace à ma question, bien qu'il soit clair qu'elle s'y attendait. Elle continue à parler avec de grands gestes."

show shizu basic_normal2
with charachange


ssh "Beaucoup."

show shizu adjust_frown
with charachange


ssh "Comme par exemple que je peux être égoïste. J'essaye trop d'attirer les gens près de moi, puis les repousse."

show shizu basic_normal2
with charachange


ssh "Je ne savais pas ce que je devais faire. Elle pensait avoir raison de mentionner toutes ces choses, donc j'ai juste acquiescé, mais ça n'a fait qu'empirer les choses."

show shizu behind_sad
with charachange


ssh "Je ne comprends pas."


"Ajustant ses lunettes, elle semble plutôt fatiguée. J’espère que ce n'est pas parce qu'elle a dû éviter Misha, mais ça reste une possibilité, vu la façon dont tourne la conversation."

show shizu adjust_smug
with charachange


ssh "C'est vrai. Même le fait que le Conseil des Étudiants soit si petit, et qu'on ait autant de travail, c'est ma faute. Il est possible que j'aie amené beaucoup de gens à nous rejoindre avant de les repousser du conseil, en agissant comme ça."


"Shizune agite un doigt, admettant que “possible” est un euphémisme. Cependant, vu la façon dont elle le fait, il est évident qu'elle fait ça pour me mettre à l'aise, et donc ce n'est pas forcément ce qu'elle pense."

show shizu basic_normal
with charachange


ssh "Comme Lilly, par exemple. Elle a été la première personne à me rejoindre quand j'ai commencé à essayer de recruter des gens après que tout le monde soit parti, parce qu'ils ne me supportaient pas, j'imagine."

show shizu adjust_happy
with charachange


ssh "On a réussi à organiser le festival, et même géré un stand ensemble à la dernière minute."

show shizu behind_frown
with charachange


ssh "Mais je ne l'aimais pas parce que je la trouvais égoïste, à toujours nous mettre sur la touche pour aider un de ses amis ou autre, nous laissant Misha et moi gérer seules des choses qui concernent l'école entière."

show shizu cross_angry
with charachange


ssh "Si elle avait un problème trop difficile, elle nous laissait seules pendant qu'elle s'en occupait en paniquant, et ne revenait que quand c'était résolu."

show shizu adjust_angry
with charachange


ssh "Elle se concentrait dessus à cent pour cent, et était trop occupée pour s'occuper du travail du conseil !"

show shizu behind_frustrated
with charachange


ssh "Le pire pour moi était qu'elle pouvait être si gentille, et pourtant considérer que les gens étaient toujours disponibles pour l'aider. Pourquoi rejoindre le Conseil des Étudiants, alors ? Ça semblait si égoïste, tu ne trouves pas ?"

show shizu basic_normal2
with charachange


ssh "Mais en fait, c'est moi qui suis comme ça."

show shizu adjust_frown
with charachange


ssh "Comme Misha l'a dit, essayant toujours d'attirer les gens près de moi avant de les repousser."

show shizu behind_sad
with charachange


ssh "C'est comme ça que je l'ai traitée, ce qui fait de moi une mauvaise amie. Et j'ai agi de la même façon avec toi aussi, ça fait de moi une mauvaise petite amie aussi. Même si Misha dit que tu pourrais la remplacer auprès de moi."

show shizu basic_normal2
with charachange


ssh "Je suis en colère d'avoir foiré les choses au point que ça en arrive là. Tout ce que je voulais est..."

stop music fadeout 3.0


"Elle s’arrête un moment pour chercher les bons mots, les doigts tendus, concentrée."

show shizu behind_blank
with charachange


ssh "Rendre les gens heureux, je crois."

show shizu adjust_happy
with charachange


ssh "Même si ça semble être une façon simple de dire ça."


"Alors qu'elle repose sa tête contre sa main, ses mèches de cheveux glissent délicatement devant ses yeux, cachés derrière ses verres polis reflétant très légèrement la lumière."


"C'est peut-être mal de penser ça, mais à cet instant, elle est vraiment belle. Comme si elle était complète."


"J'ai l'impression que c'est ma première chance de répondre à son flot d’émotions. Remplacer Misha en tant qu’interprète de Shizune ? Misha ne peut pas être sérieuse en disant ça."


"Il m'a fallu toute mon énergie pour réussir à suivre jusqu’à maintenant, ses signes étant remplis de gestes que je n'avais jamais vus auparavant."


"C'est sûrement des habitudes développées à force de parler avec Misha durant des années. Je ne pourrai jamais remplacer quelqu'un aussi proche d'elle."


his "Je t'apprécie parce que je t'apprécie, pas parce que tu as fait en sorte que je me rapproche de toi."


"Malgré l'intensité de ses tentatives, du moins. Je continue de fixer ses yeux, aussi vifs que toujours. La première fois que je les ai vus, ils me semblaient un peu intimidants. Comme les yeux d'un prédateur. Ça n'a pas changé, ce qui en soi est rassurant."

show shizu basic_normal
with charachange


ssh "Je veux toujours rendre tout le monde heureux."


his "En commençant par Misha ?"

play music music_shizune fadein 6.0

show shizu basic_frown
with charachange


"Shizune semble un peu énervée que je puisse insinuer qu'elle commence avec qui que ce soit d'autre, et sourit avec confiance, comme si la tristesse d'une amie était un adversaire physique qu'elle pouvait juste étrangler jusqu’à soumission."

show shizu behind_frustrated
with charachange


ssh "Bien sûr, évidemment, naturellement."


show shizu adjust_noglasses
with charachange


"Enlevant ses lunettes, elle s'adosse à sa chaise et laisse échapper un soupir. C'est la première fois que je la vois sans, mais n’ai pas la chance de bien voir avant qu'elle les remette."

show shizu behind_smile
with charachange


ssh "Mais je trop fatiguée pour commencer aujourd'hui. Je ferai ça demain."

show shizu basic_normal
with charachange


ssh "Tu veux aider ?"


his "Ouais."

show shizu adjust_happy
with charachange


ssh "Et... j'ai un autre job pour le conseil des étudiants pour lequel tu pourrais m'aider, pendant que tu y es."


"Bien qu'il s’avère qu'il n'y a pas tant de travail que ça."

stop music fadeout 2.0
$ suppress_window_after_timeskip = True

scene black
with dissolve




label fr_S31:

window hide None

scene black
with dissolve

with Pause(2.0)

play sound sfx_doorknock

with Pause(2.0)

scene bg school_dormhisao
with openeye

window show

play sound sfx_doorknock


"Il n'y a pas école aujourd'hui, donc je m'attendais à pouvoir faire la grasse matinée. Malheureusement, je suis réveillé par des coups sur ma porte à huit heures du matin."


"Au début je crois que c'est Kenji, mais quand mes cris de mécontentement restent sans réponse, je réalise que c'est Shizune."

play sound sfx_dooropen

scene bg school_dormhallway
show shizu adjust_happy_close at center
with locationchange

play music music_another fadein 0.5

show shizu behind_blank at center
with charadistant


"Elle recule immédiatement quand j'ouvre la porte, cachant quelque chose derrière son dos. C'est de mauvais augure."


his "Qu'est-ce que c'est que ça ? C'est une surprise ? Je n'aime pas vraiment les surprises."

show shizu behind_frown
with charachange


"L'expression sur son visage dit qu'elle veut que j’arrête d'être aussi rabat-joie, mais elle est trop occupée à cacher ce qu'il y a derrière son dos pour le signer."

show shizu adjust_smug
with charachange


"Ça doit être frustrant pour elle, parce que quelques secondes plus tard, elle sort l'objet, le faisant tournoyer avec fierté et dangerosité."

show shizu basic_happy
with charachange



ssh "Ta-da. Un panier pique-nique. On peut déjeuner ensemble, tous les trois."


"Ce n'est pas vraiment un panier, ça ressemble plus à un sac plastique. Jetant un coup d’œil rapide à l'intérieur, je peux voir que la plupart de ce qu'il y a dedans est acheté en magasin, pas fait maison. Certains ont même encore les étiquettes dessus."


"Il y a beaucoup de choses différentes quand même. Même un peu de caviar. Je commence lentement à être impressionné par ce repas. Je prends un raisin d'une grappe et le met dans ma bouche."

show shizu adjust_frown
with charachange


ssh "Ne te sers pas comme ça ! J'ai passé toute la nuit à perfectionner cette arme finale."

show shizu adjust_frown:
    ease 0.5 ypos 1.2
    ease 0.5 center
with Pause(0.5)

play sound sfx_pillow

show shizu basic_normal:
    ypos 1.2
    ease 0.5 center
with charachange


"Shizune le place sur le sol pour se libérer les mains, et commence immédiatement à le tapoter joyeusement avec ses pieds comme un ballon de foot. Vraiment pas quelque chose qu'il faut faire avec une “arme finale.”"

show shizu adjust_happy at center
with charachange


ssh "Tout cela fait partir de mon plan “faire-en-sorte-que-Misha-arrête-d'être-aussi-déprimée”. Je suis restée debout toute la nuit à travailler dessus."

show shizu behind_smile
with charachange


ssh "Quand on a essayé de commander la dernière fois, Misha n'a presque rien pris et a trouvé une excuse pour partir plus tôt. Je ne vais pas la laisser s’échapper aussi facilement cette fois. Le repas est déjà là, elle aura juste à s’asseoir et à manger."

show shizu basic_happy
with charachange


ssh "C'est l’appât parfait. Ça ne te semble pas irrésistible ? J'ai essayé de le faire moi-même, mais je ne sais pas comment faire en sorte que tout ait l'air plein de fantaisie, donc j'ai fini par tout acheter. Ça semble délicieux, hein ? Ça doit l’être."


"Elle est très énergique aujourd'hui, motivée par l'idée de réconforter Misha. Bien que ce soit bizarre de la voir contente pour ça, je sais qu'elle est aussi incertaine qu'elle l'était hier."


"La seule chose qui a changé est qu'en voyant ça comme un challenge, elle peut mettre ses inquiétudes de côté et se lancer à fond sans restriction."


"Ça a bien marché pour elle jusque-là. Ça ne me surprendrait pas que ce soit la seule façon de vivre qu'elle connaisse."


his "Il est un peu tôt, cela dit..."

show shizu adjust_frown
with charachange


ssh "Il est déjà huit heures du matin, c'est tard ! Même Misha se lève à huit ou neuf heures. Elle va au lit à dix-neuf heures, mais c'est un détail."


his "Ce n'est pas un détail."

show shizu basic_normal_close
with characlose


"Shizune m'ignore et m’empêche de parler en me prenant les mains plutôt que d'argumenter. La façon dont elle s'attarde contre moi un peu plus longtemps que prévu est vraiment agréable."

show shizu adjust_happy_close
with charachange


ssh "Le fait est qu'elle est réveillée, en train de vagabonder quelque part. Allons la trouver."

scene bg school_courtyard at bgleft
with locationskip


"Elle part en courant vers les jardins avec impatience et enthousiasme tandis qu'elle m’entraîne à la recherche de Misha, ce qui me fait plus penser que Shizune est un chasseur dans un safari plutôt qu'à la recherche d'une amie mutuelle."


"On n'a pas besoin de chercher très loin. Même coupés court, ses cheveux roses ressortent beaucoup. Le fait qu'elle est juste en train de se balader sur les terrains rend ça encore plus facile. Maintenant je parle comme un chasseur de safari."

show shizu adjust_happy_close at tworight
with charaenter


shi "... !"


hi "Misha !"

show mishashort hips_smile at twoleft behind shizu
with charaenter


mi "Hein~ ?"


hi "On te cherchait."

show shizu behind_smile_close
with charachange


ssh "C'est une bonne journée pour un pique-nique, tu devrais venir avec nous. On a même du caviar, pas d’esturgeon bien sûr, mais vraiment bon."

show mishashort perky_confused
with charachange


mi "Caviar ? Esturgeon ?"


"Trouvant apparemment embêtant d'avoir à tout expliquer avec une seule main, Shizune abandonne rapidement."

show shizu adjust_frown_close
with charachange


ssh "Des œufs de poissons."

show mishashort sign_confused
with charachange


mi "Quoi ?"

show shizu behind_smile_close
with charachange


ssh "C'est bon."

show mishashort cross_smile
with charachange


mi "Désolée, Shicchan, je crois que je vais passer pour cette fois."

show shizu basic_angry_close
with charachange


"Quand Misha commence à partir, Shizune me tend le sac pour que je le tienne et que ses mains soient libres."

hide shizu
with None

show shizu basic_angry_close at tworight behind mishashort
with None

show mishashort cross_smile:
    ease 1.0 center
show bg school_courtyard:
    ease 1.0 center
show shizu basic_angry_close:
    ease 1.0 xpos 0.75
with Pause(0.5)
show shizu behind_blank:
    tworight
    xpos 0.725
    ease 0.5 xpos 0.75
with charadistant

show mishashort perky_confused at Position(xpos=0.35)
show shizu behind_blank at Position(xpos=0.65)
show bg school_courtyard at Position(xpos=0.43)
with dissolvecharamove


"Aussitôt que j'ai le sac, elle se précipite en face de Misha, lui barrant la route."

show shizu adjust_happy
with charachange


ssh "Mais j'ai fait beaucoup à manger."

show mishashort perky_sad
with charachange


mi "Désolée, je n'ai pas faim."

show shizu behind_blank
with charachange

shi "…"

show shizu behind_frown
with charachange


ssh "Quand est-ce que tu auras faim alors ?"

show mishashort hips_frown
with charachange


mi "C'est impossible de savoir ça, Shicchan~."

show shizu adjust_frown
with charachange


ssh "Tu peux deviner."


"La tension entre elles deux semble exaspérer Shizune, et elle essaye de forcer le passage pour briser cette tension. Mais cette approche ne va pas marcher."


"J'ai pensé, et espéré, que Misha s'était ressaisie, mais je crois que ce qui est arrivé l'a trop affectée."


"Dans tous les cas, on ne peut rien y faire. Je crois que Shizune peut comprendre ça, d'une certaine façon. Si ce n'était pas le cas, elle n'aurait aucun doute."


"Parce qu'elle ne peut parler, j'ai appris à remarquer son hésitation. C'est très clair, elle pourrait tout autant le crier."

show mishashort sign_smile
with charachange

hide mishashort
with charaexit

stop music fadeout 5.0


"Misha agite une main devant elle, ne voulant pas continuer cette conversation et s'en va. Shizune fulmine silencieusement, ne voulant pas la laisser partir mais n'ayant pas d'autre choix."


"Alors que Misha devient de plus en plus petite en s'éloignant, je me demande où elle va. Est-ce que Shizune se demande la même chose, alors qu'elle se mord la lèvre de frustration ?"


"Je veux lui toucher l'épaule pour la rassurer, mais je m’arrête, n'étant pas sûr que ce soit la bonne chose à faire."


"Pas parce qu'elle a l'air fragile, vulnérable ou triste, c'est l'opposé. Après un moment, son expression n'affiche plus aucune émotion. Seulement de la contemplation. Soudainement, elle se retourne."

play music music_dreamy fadein 4.0

show shizu basic_angry at center
show bg school_courtyard at right
with dissolvecharamove


ssh "Maintenant, tout ça va être gaspillé."


his "Ouais."

show shizu behind_sad
with charachange


ssh "Ça m'énerve."


"Bien qu'il soit évident qu'elle est plus blessée qu'en colère. Le sac pendant au bout de son bras semble être rempli de plomb."

show shizu behind_blank
with charachange


$ doublespeak(ssh, his, "Allons au rendez-vous.", "Mangeons-le, dans ce cas.")

show shizu adjust_blush
with charachange

shi "…"

show shizu basic_normal
with charachange


ssh "Où est-ce que tu veux aller ?"


his "Je ne sais pas."

show shizu behind_blank
with charachange


ssh "Le toit."

show shizu adjust_happy
with charachange


ssh "C'est mon endroit préféré."


"Un sourire tordu apparaît sur son visage et disparaît tout aussi rapidement."

play ambient sfx_rooftop fadein 1.0

scene bg school_roof
show shizu behind_frown_close at center
with shorttimeskip


"Sur le toit, j'ouvre immédiatement le caviar, ignorant le regard moqueur de Shizune. Je le pose juste après."


his "Où sont les toasts ?"

show shizu basic_normal2_close
with charachange


ssh "Je n'en ai pas fait. Comme je l'ai dit, j'ai tout acheté."


his "Mais pas de toasts..."

show shizu adjust_frown_close
with charachange


ssh "En quoi c'est important ? Dans tous les cas, ils ne vendent pas des toasts seuls. Ça serait stupide."


his "Je suis sûr qu'ils en vendent."

show shizu behind_blank_close
with charachange


ssh "Peut-être dans des magasins pour flemmards, mais pas ici. Pourquoi tu n'utilises pas une chips tortilla plutôt ?"


his "C'est pas la même chose."

show shizu basic_frown_close
with charachange


ssh "Ils sont tous les deux en triangle, arrête de faire ta princesse. Je ne savais pas qu'il y avait une façon de manger du caviar, c'est la première fois que je l'entends."


his "C'est pas pareil du tout."

show shizu adjust_smug_close
with charachange


"Je ne peux pas faire ça. Et puis de toute façon, comment est-ce qu'elle ne peut pas savoir ? Elle vit dans un immense manoir. Shizune profite de l'opportunité pour vider la moitié du pot sur une chips."


his "Hé !"


"Je suis sûr que ce n'est même pas bon mangé comme ça."

show shizu behind_smile_close
with charachange

shi "…"


"Il y a trop à manger pour deux personnes. Et parce que nous ne pouvons pas communiquer, Shizune et moi restons assis en silence à penser au fait que Misha, la personne pour qui tout ça a été organisé, n'est pas là."

show shizu basic_angry_close
with charachange


ssh "C'est énervant qu'elle ne soit pas là. Je ne peux pas apprécier le repas comme ça."


"Je regarde le gobelet en plastique à côté d'elle, encore à moitié rempli de jus de fruit."


his "Je croyais que tu ne voulais pas que ce soit gâché."

show shizu adjust_frown_close
with charachange


ssh "Je voulais que Misha soit là aussi. C'était ça tout l’intérêt. Je n'ai pas été capable d'accomplir ce que je voulais, donc ce n'est pas bon."

show shizu behind_blank_close
with charachange


ssh "Tu devrais manger. Mange plus."


his "Je veux ce qui est frit. Tu n’arrêtes pas d'en manger, même si tu dis que ce n'est pas bon."

show shizu basic_normal_close
with charachange


ssh "Ce qui est frit est toujours délicieux. C'est une exception."


his "Tu vas devenir grosse."


his "Je crois que tu es trop agressive."

show shizu behind_blank_close
with charachange


ssh "C'est comme je t’ai dit hier, j'essaye seulement de la réconforter."


his "Ouais, mais on dirait plus que tu prépares une campagne militaire."

show shizu basic_normal2_close
with charachange


ssh "J'essaye juste de prendre ça au sérieux."

show shizu behind_sad_close
with charachange


ssh "...Et c'est la seule façon que je connais pour être sérieuse."

show shizu basic_normal2_close
with charachange


ssh "Je me sens si inutile. Je déteste ça. Je ne peux même pas lui crier dessus, même si j'en ai envie. Crier, c'est quand c'est sérieux, c'est ça ?"


his "Ouais."

show shizu adjust_frown_close
with charachange


ssh "Tu devrais crier sur Misha pour moi. Tu peux lui dire que je veux qu'elle arrête d'aller si mal. Même si elle se sent triste et seule, ce n'est pas une raison pour rester morne pour toujours."


his "Pourquoi tu ne le fais pas ?"

show shizu basic_frown_close
with charachange


ssh "Je l'ai déjà fait."

show shizu behind_blank_close
with charachange


ssh "Pendant une partie de dés."

show shizu basic_happy_close
with charachange


ssh "Under/Over, pour être précise. J'ai gagné ! Cinq fois !"


"Seulement elles deux peuvent être aussi fières de gagner à un jeu de pure chance."

show shizu adjust_frown_close
with charachange


ssh "Et donc, j'ai essayé de lui parler, mais ça ne s'est pas si bien passé, de toute évidence."


his "Eh bien, tout comme moi. J'ai essayé et échoué."

show shizu basic_normal2_close
with charachange


ssh "Mon but a toujours été d'améliorer les choses."


his "Ouais, et tu ne fais pas les choses à moitié."

show shizu behind_frustrated_close
with charachange


ssh "Mais j'ai échoué aussi..."

show shizu basic_normal2_close
with charachange


ssh "C'est pourquoi je veux ton aide."

show shizu behind_sad_close
with charachange


ssh "Je ne comprends pas ce que je suis censée faire maintenant."


"Pour quelqu'un comme Shizune, qui a seulement interagi avec le monde en argumentant avec les personnes sur son chemin, sa compréhension ne va pas plus loin."

$ renpy.music.set_volume(0.5, 2.0, channel="music")
$ renpy.music.set_volume(0.5, 2.0, channel="ambient")

window hide

scene bg misc_sky at Fullpan(30.0)
with locationchange

nvl clear
nvl show dissolve


n "\n\nJ'ai envie de lui dire qu'elle n'a pas à s’inquiéter. Qu'elle est douée pour remonter le moral des gens, parce qu'elle a réussi à me remonter le moral lors de ma première semaine ici."


n "Rétrospectivement, je devais avoir l'air d'un idiot à être si aigri quand je suis arrivé. Même si je ne trouve pas ça si déraisonnable."


n "Même après avoir eu des mois pour le digérer, découvrir que j'ai un cœur défectueux est difficile à gérer. J'ai eu moins de temps pour encaisser le fait d’être transféré à Yamaku en plus de ça."


n "\n\nPasser le festival avec Shizune m'a vraiment aidé. J'étais content, suffisamment pour oublier tous ces moments où je sentais qu'elle me manipulait. Je comprends maintenant que je me suis laissé manipuler."

nvl clear


n "\n\nMême si j'avais l'impression d’être au tréfonds de la terre, j'avais toujours envie d'avoir une vie normale à nouveau, j'en suis sûr, parce que j'apprécie ce que j'ai maintenant. Je crois que ça doit être pareil pour tout le monde. Pour Misha aussi. Tout le monde veut quelqu'un pour le tirer hors de son auto-apitoiement."


n "C'est juste que Misha voulait que Shizune soit cette personne, mais parce qu'elles ne peuvent pas être ensemble, je crois que Misha ressent qu'elle ne peut pas accepter l'aide de Shizune. Et ça frustre Shizune. Mais si elle a pu remonter le moral d'un étranger comme moi, alors elle mourra en essayant de remonter celui de Misha."


n "\nJe peux le voir dans ses yeux, aussi. Bien qu'elle essaye de gérer ça comme n'importe quel problème de sa vie, Shizune ne peut pas faire ça avec la dépression de Misha. La façon dont elle pense est différente, elle est parfois plus attentive, ou plus téméraire. Elle s'en soucie beaucoup plus."

nvl clear


n "\n\n\n\n\nJe finis par ne rien dire. En partie parce qu'être assis à côté d'elle comme ça, juste nous deux, est suffisamment plaisant pour que je n'interrompe pas le moment par une question."


n "\n\nEt en partie par peur. Je me demande si ses actions de ce jour-là n'auraient pas juste été un coup de chance, ou un enchaînement de coïncidences. Je ne sais pas si ça changerait quoi que ce soit, mais je suis mal à l'aise en y pensant."

$ renpy.music.set_volume(1.0, 2.0, channel="music")
$ renpy.music.set_volume(1.0, 2.0, channel="ambient")

nvl hide dissolve
nvl clear

scene bg school_roof
with locationchange

window show

stop music fadeout 5.0


"Le grillage derrière moi tremble légèrement, et je me tourne pour voir que c'est parce que Shizune s'est endormie. Étant donné qu'elle est restée debout toute la nuit, ça ne me surprend pas."


"D’où est-ce qu'elle sort toute cette motivation ? Pas seulement en ce qui concerne Misha. Je suis cynique, donc c'est dur d'accepter que qui que ce soit puisse être si fort."


"Ma première pensée est que c'est peut-être parce qu'elle se déteste. C'est très plausible."


"Appuyé contre elle, je me sens triste à l'idée que ça puisse être le cas. Mais c'est aussi parce qu'on se ressemble sur le fait qu'on voudrait tous les deux être de meilleures personnes."

stop ambient fadeout 2.0

scene black
with dissolve

$ suppress_window_after_timeskip = True



label fr_S32:

window hide None

scene black
with dissolve

scene bg school_dormhisao
with openeye

window show

play music music_daily fadein 8.0


"On dirait que j'ai trop mangé hier, parce que je me suis réveillé ce matin en me sentant suffisamment nauséeux pour que ce soit un problème."


"Je ne peux pas vraiment reporter le fait d'aller en ville pour faire les courses, cela dit. Donc malgré mon envie de me tourner et de me rendormir, je me force à me lever et à m'habiller."

scene bg suburb_roadcenter
with locationskip


"Après avoir acheté du dentifrice et quelques autres choses, je finis par m'en être débarrassé. Ensuite, j'ai faim. Après m’être arrêté pour déjeuner, je me rends compte du temps qui s'est passé."


"Je ne pensais pas avoir à sortir aussi longtemps. Je ne suis même pas sûr d'avoir verrouillé ma porte. Je devrais vraiment rentrer."

scene bg school_dormhallway
show hideaki bored at center
with locationskip


"Quand je retourne aux dortoirs, je vois Hideaki se tenant devant ma porte. J'ai un peu de mal à trouver beaucoup de choses moins probables, et je ne peux pas m’empêcher de penser que je pourrais avoir une crise cardiaque à cause de la surprise."

show hideaki normal
with charachange


"Aussitôt qu'il me voit, il me dit bonjour de sa façon détachée habituelle. Je suis un peu lent à répondre, donc il répète sa salutation sans tarder."

show hideaki triangle
with charachange


hh "Bonjour."

show hideaki normal
with charachange


hh "Quelque chose ne va pas ?"


hi "Je suis juste surpris de te voir."


"Pas aussi surpris que j'aurais pu l'être, vu qu'il est impossible de le confondre avec quelqu'un d'autre. Je reconnais ses vêtements bizarres trop facilement. En y pensant, je me suis vraiment entouré de gens avec un style bizarre récemment."

show hideaki confused
with charachange


"La tête de Hideaki penche d'un côté. Un peu trop."


hh "Pourquoi ? C'est inhabituel de voir un membre de la famille venir voir quelqu'un ici ?"


hi "Eh bien... ouais."

show hideaki surprise_up
with charachange

show hideaki bored
with charachange


"Donc, Hideaki n'est pas un tel robot après tout. En fait, c'est comme s'il était surpris du fait qu'il puisse encore être surpris. Mais il s'en remet vite."


"Néanmoins, à ce bref instant, il fait son âge. Ce côté mal à l'aise semble le plus honnête de tous chez lui, et ça ne me gênerait pas de le voir plus souvent."


"Pas au point où j'irais fouiller dans ce qui ne me regarde pas. Seule Shizune pourrait être aussi zélée. Mais que j'y aie pensé montre qu'elle déteint sur moi."


hi "Je pensais que tu aurais une raison, c'est tout."

show hideaki triangle
with charachange


hh "Il y en a une."


hi "Tu vois ? Bref, on peut discuter pendant qu'on cherche Shizune. C'est pour ça que tu es là, hein ?"

show hideaki normal_up
with charachange


hh "Shizune est dans la salle du conseil des étudiants. Je te cherchais toi. On fera bientôt un voyage, un voyage en famille. Tu penses qu'elle voudrait venir avec nous ?"


hi "Eh bien, je ne sais pas. Elle était sur le pied de guerre récemment, à cause de beaucoup de choses. Et dès qu'elle est concentrée sur quelque chose, elle ne le lâche plus. ...J'imagine que tu le sais, ça."

show hideaki closed_up
with charachange

hh "Mm."

scene bg school_courtyard
with locationskip


"Hideaki semble bien plus à l'aise que je ne l'étais lors de ma première semaine."


hi "Donc, ce n'est pas ta première fois ici ?"


"Je dis juste ça comme ça. Bien sûr, ignorer complètement ce qui se passe ou ce qui est dit peut être juste de famille. Ça expliquerait pourquoi Hideaki semble si distant avec Shizune. J'ai le sentiment qu'il y a plus que sa surdité derrière ça."

show hideaki bored at center
with charaenter


hh "Non, mais c'est la première fois que je me balade autant. C'est bizarre ici. J'ai croisé quelqu'un qui m'a dit que les femmes n'étaient pas autorisées dans les dortoirs."

show hideaki disapproves
with charachange


hh "Après que je lui aie dit que je n'étais pas une femme, il m'a dit que je me trompais, et m'a accusé d’être un assassin."

show hideaki normal
with charachange


hh "J'ai été prévenu que non seulement il était invincible, mais aussi probablement assez fort pour détruire le bâtiment entier d'un seul coup de poing, ou au moins faire tomber la peinture du mur. D'ailleurs, cette peinture y est vissée."


hi "Ouais, c'est le gars de la chambre d'en face. Il est pas méchant."

show hideaki triangle
with charachange


hh "Je vois. Oh, et tu as laissé ta porte ouverte. C'était déverrouillé quand je suis arrivé."


"Je suis un peu embêté que Hideaki sache ça. La seule façon qu'il ait de le savoir est qu'il ait ouvert ma porte. Mais le sentiment me passe."


hi "C'est pas important."


hi "Je n'ai rien à cacher, ou voler."

show hideaki happy_up
with charachange


hh "Tu as des jolis ballons de football."


hi "C'est une des choses qui n'ont pas d'importance."

show hideaki serious
with charachange


hh "Si tu joues au football, alors un ballon de football est très important."


"Il n'a pas tort. La pensée me fait sourire."

show bg school_lobby
show hideaki closed_up at center
with locationskip


hh "Je suis là parce que mon père a acheté un nouveau téléphone et qu'il voulait transmettre le numéro à Shizune, au cas où elle aurait besoin de l’appeler. Je me suis dit que tu devrais le savoir aussi, vu que tu es son petit ami, non ?"


hi "Ouais..."


hi "...Pourquoi ?"

show hideaki bored
with charachange


hh "Juste au cas où quelque chose ne va pas, ou qu'elle ait besoin de quoi que ce soit."


"Ce n'est pas ce que je voulais dire, mais tant pis."


hi "Même si ça arrivait, elle n'appellerait probablement pas."

show hideaki triangle
with charachange


hh "Elle est comme ça."


hi "Bah, si tu le sais... Mais pourquoi tu es venu jusqu'ici pour ça ? Il aurait pu l'informer par e-mail."

show hideaki closed_up
with charachange


hh "Il n'aime pas utiliser les e-mails."


hi "Il est vraiment de la vieille école. Ne me dis pas qu'il utilise toujours du courrier papier pour son travail, ou autre."

stop music fadeout 3.0


"Silence. Maintenant je me sens mal à l'aise. Est-ce qu'il a pris ma question littéralement ou est-ce qu'il a compris que c'était pour rire ?"


"Nan. Je suis sûr que, malgré tout, ce qu'il veut c'est voir sa fille et rester en contact avec elle. En fin de compte, ils restent une famille après tout. Même s'ils jouent à être toujours sur le dos l'un de l'autre."

scene bg school_council
show jigoro smug at tworight
show shizu basic_normal2 at twoleft
with locationskip

play music music_happiness fadein 2.0


"La porte du bureau du conseil des étudiants est ouverte, et Hideaki et moi trouvons Jigoro en train de crier. Il nous voit, mais décide que ça ne vaut pas le coup de s’arrêter de hurler contre Shizune. Ça remet vraiment en question ma théorie."

show jigoro angry
with charachange


hx "Quand j'étais dans le Conseil des Étudiants, notre pièce était plus petite. Et il y faisait plus froid aussi. Comme travailler dans un réservoir à viande. Pas comme vous, enfants gâtés. Quel gâchis. Être assis dans une si grande pièce à ne rien faire."

show shizu behind_frown
with charachange

shi "…"


hx "Vous n’êtes pas qu'à trois ? Avoir autant de bureaux semble vraiment décadent. Affreux. Vous devez utiliser les bureaux dont vous avez besoin, et pas un de plus. Ça fait partie de mes principes."


"C'est peut-être bizarre de ma part de penser ça, mais... entendre seulement la moitié d'une conversation est assez étrange."


"Maintenant que je suis arrivé, il change de sujet, et commence à parler de la raison de sa présence."

show jigoro neutral
with charachange


hx "Hideaki et moi partons en voyage."

show shizu basic_normal2
with charachange

shi "…"

show jigoro angry
with charachange


hx "Qu'est-ce que tu fais ? Est-ce que tous ceux qui utilisent le langage des signes doivent marmonner en même temps ?"


hi "Non, mais je suis juste un amateur. Ça m'aide à penser. C'est comme une habitude."


hx "Juste un amateur... pas croyable... D'accord."


"Il se retourne vers Shizune juste à temps pour la voir secouer la tête."

show jigoro neutral
with charachange


hx "Tu es sûre que tu ne viendras pas ?"

show shizu adjust_frown
with charachange


"Elle réitère le mouvement de tête."

show jigoro angry
with charachange


hx "Bien."

show jigoro neutral
with charachange


hx "Tu peux lui dire de m’appeler si elle a besoin de quelque chose ?"


hi "Oui."


hi "Même si je pense vraiment qu'envoyer un e-mail aurait été plus simple."

show jigoro angry
with charachange


hx "Je ne vais pas lire d'e-mail sur mon téléphone. Si elle ne parle pas, elle peut appeler Hideaki. Si j'avais dû être joint, tu m'aurais appelé, ou l'autre fille m'aurait appelé. ...Hmph. En fait, vous pouvez tous les trois appeler Hideaki."

hide jigoro
with charaexit

stop music fadeout 3.0


"Et sur ce, il tourne les talons et part, Hideaki trottinant derrière lui. Un long voyage, pour quelque chose qui a pris cinq minutes."


"Aucun d'entre eux ne peut bien exprimer ses sentiments. Dans le cas de Shizune, je me demande si elle le ferait, si elle le pouvait. Ça explique beaucoup, mais elle ne semble pas mécontente de leur façon de fonctionner."

play sound sfx_doorclose
with Pause(1.0)
show shizu basic_normal at center
show bg school_council at bgright
with dissolvecharamove

play music music_normal fadein 3.0


"Quand la porte se ferme derrière eux, nous laissant tous les deux seuls, elle laisse sortir un long soupir qui semble résonner dans le silence la pièce."

show shizu behind_frown
with charachange


ssh "C'est ridicule de me proposer de partir en voyage. Le moment n'aurait pas pu être plus mal choisi. C'est pendant les élections du conseil des étudiants, de un, et de deux, je n'ai même pas remonté le moral de Misha."


his "Ouais, mais tu es peut-être un peu trop concentrée sur ça aussi."

show shizu adjust_frown
with charachange


"Shizune réajuste brusquement ses lunettes."

show shizu behind_frown
with charachange


ssh "Tu as complètement, et à cent pour cent raison. À la minute où j'ai décidé que j'allais réconforter Misha, tout le reste est passé derrière."


his "Je crois que ton père se préoccupe plus de toi qu'il ne le laisse transparaître."

show shizu basic_normal
with charachange


ssh "Je sais."


his "Donc, alors, ça pourrait être une bonne idée de—"

show shizu adjust_frown
with charachange


ssh "Non."


"Et encore une fois, encore plus ferme, comme si elle parlait pour nous deux."

show shizu cross_angry
with charachange


ssh "Non."

show shizu basic_frown
with charachange


ssh "Après avoir été si loin, je ne peux pas faire de pause. Prendre des vacances serait discordant. Ça serait comme se réveiller dans une autre vie. Hier était comme des vacances pour moi. Donc maintenant je dois m'y remettre à fond."

show shizu behind_blank
with charachange


ssh "Je suis désolée, je suis comme ça."

$ renpy.music.set_volume(0.5, 2.0, channel="music")

window hide
nvl clear
nvl show dissolve


n "\n\nJe me rappelle ce qu'a dit Yuuko, qu'elle trouvait Shizune brave, d'une certaine façon. Je crois que je comprends ce qu'elle voulait dire, et je suis d'accord. Même si ça pourrait aussi être identifié comme de la témérité insensée et têtue, j'imagine qu'on peut aussi appeler ça de la “bravoure”."


n "Cependant, je peux voir qu'il y a une faille fondamentale dans le raisonnement de Shizune que je n'avais pas remarquée jusqu’à maintenant."


n "\nJe suis sûr que Shizune y a pensé plus sérieusement et plus longtemps que moi, au sujet de ce qu'elle a pu faire pour compromettre la situation entre elle et Misha à ce point-là. Cependant, fidèle à elle-même, elle n'aurait pas laissé ça comme ça et aurait immédiatement réglé le problème."


n "Ça ignore complètement une grande partie du problème : Misha elle-même. Faire une introspection, puis faire de Misha une partie de l'objectif implique qu'elle se perd dans le processus. Shizune a “dit” beaucoup de choses ces derniers jours, mais rien à propos de ce que ressent Misha."

nvl clear


n "\n\nLa façon de penser de Shizune est anormale. Peu de gens normaux rejetteraient un ami pour après s'attendre à ce que les choses reviennent comme avant aussi facilement. C'est le cas de Shizune, parce qu'elle voit la vie comme si elle pouvait la segmenter et la compartimenter."


n "Misha, comme tout le monde, voit ça comme un ensemble. Un long voyage continu, où un seul moment de douleur sentimentale peut vous suivre pour toujours."


n "Pour Shizune, un événement est un événement, et peu d'entre eux passent ce stade. La vie est compartimentée entre les réussites, les échecs, les décisions, où chacun a un rôle dans chaque événement. C'est pour ça que pour elle des vacances sont impensables. C'est pour ça qu'elle ne peut comprendre que les émotions immédiates des gens."


n "C'est exactement comme ça qu'une personne obsédée par le fait de vivre dans le moment présent voit les choses."


n "Shizune peut voir Misha comme une amie, mais je doute qu'elle ait déjà pensé à elle d'une autre façon jusqu’à récemment. Ou s'est interrogée sur quoi que ce soit à son propos. “Misha est Misha” est suffisant pour elle, même si pour Misha ça doit être vraiment suffocant."

nvl clear


n "\nShizune est juste Shizune pour elle-même. Il est probable qu'elle ne connaisse même pas les effets secondaires de ses actions à long terme sur la vie des gens. Pour Misha, cela dit, je suis sûr que ça lui donne un air presque héroïque. Comme Yuuko admire sa bravoure, et même moi."


n "Et ce qu'en pense Shizune est que c'est bien qu'elle ait pu influencer la vie de quelqu'un. Mais ça s’arrête là. C'est facile de captiver quelqu'un, bien plus dur de faire durer. Et aussi, penser la vie en termes d’événements presque complètement isolés les uns des autres a tendance à isoler les gens, aussi."


n "Bien qu'elle essaye d'y remédier, le fait demeure : Il est simplement impossible que Shizune ait pu éviter de faire du mal à Misha. Son investissement émotionnel en Shizune est quelque chose que Shizune ne pouvait pas assumer, donc elle ne l'a pas fait. Combiné avec sa personnalité, c'était inévitable."


n "Elles m'ont appris ça morceau par morceau au fil des mois que j'ai passés avec elles."


n "\nAlors que j’énumère leurs différences, une idée commence à prendre forme dans mon esprit."

$ renpy.music.set_volume(1.0, 2.0, channel="music")

nvl hide dissolve
nvl clear
window show


his "Est-ce que tu travailles là-dessus tout de suite ? À cette seconde ?"


his "Ton plan pour réconforter Misha."

show shizu basic_happy
with charachange


ssh "Bien sûr. J'y ai pensé tout le temps où on me criait dessus."

show shizu adjust_happy
with charachange


"Remontant ses lunettes sur son nez avec un air étrangement triomphant, elle tape du doigt sur sa tempe."

show shizu behind_smile
with charachange


ssh "Ça s'appelle être multitâche !"

stop music fadeout 4.0


"Vraiment ? Ce n'est pas plutôt dû au fait que tu n'arrives pas à te concentrer sur quelque chose comme ça parce que tu ne peux pas entendre ? Quand je lui demande ce qu'elle pense de mon plan, il s’avère qu'on est arrivés à la même idée."

scene black
with dissolve



label fr_S33:

scene bg school_scienceroom at bgleft
with locationchange

play music music_pearly fadein 5.0


"Bien que ça me mette quelque peu mal à l'aise, vu qu'on parle d'un être humain, la première étape est de coincer Misha."


"Bien que la situation soit un peu trop sortie d'un film policier pour moi, on en arrive là parce que lui parler normalement s’avère presque impossible."


"Mais on a cours ensemble. Même le premier cours de la journée."

show shizu invis:
    center
    xpos 0.75
show mishashort invis_close:
    center
    xpos 0.15
with None

show shizu behind_blank at tworight
show mishashort perky_confused_close at twoleft
show bg school_scienceroom at center
with dissolvecharamove


"Bien qu'il faille attendre un moment pour que l'annonce arrive, à la seconde où j’entends qu'on va travailler en groupe aujourd'hui, Shizune et moi essayons de nous assurer que Misha soit dans le nôtre."


hi "Tu sais, je trouve que Mutou fait étrangement beaucoup de travail de groupe et d’études personnelles, tu n'es pas d'accord ?"

show mishashort perky_smile_close
with charachange


mi "Mh~, mais c'est facile, alors ça va, hein~ ?"


hi "Ouais ? Il y a d'autres choses auxquelles j'ai pensé récemment aussi, mais qui pourraient ne pas aller, cela dit."


"Misha hoche la tête après chaque phrase, et change directement de sujet."

show mishashort sign_confused_close
with charachange


mi "J'y ai pensé aussi, et~... Je ne travaille pas assez quand je travaille avec Shicchan et toi ! Donc, je vais travailler plus dur aujourd'hui. Donc~ ! Ne me distrais pas, Hicchan~. Je dois rester concentrée~."

show shizu behind_frustrated
with charachange


"C'était une esquive bien trop crédible. Shizune ne semble pas contente non plus, vu que Misha n'a pas pris la peine de signer quoi que ce soit de ce qu'elle a dit, faisant tourner un stylo dans sa main à la place."


"D’après la façon dont elle le fait en tremblant, je suis sûr qu'elle le fait pour ne pas se mettre à signer sans faire exprès."


"Vu comment est Misha, distraite et mal à l'aise, je doute que ce soit parce qu'elle veuille garder Shizune éloignée pour une raison malhonnête. Cependant, il est toujours évident que c'est une façon de prendre ses distances avec Shizune."


hi "Shizune veut te parler."

show mishashort perky_sad_close
with charachange

mi "…"

show mishashort perky_confused_close
with charachange


mi "Ça ne peut pas attendre plus tard, Hicchan ?"

show shizu basic_angry
with charachange


ssh "Non."


hi "Pourquoi pas maintenant ?"

show mishashort sign_confused_close
with charachange


mi "On est au milieu d'un cours~..."


"Maintenant elle fait tournoyer un stylo dans chaque main. Je commence à penser que le fait qu'elle signe puisse être devenu comme un tic nerveux pour elle. Ce n'est pas une bonne alternative, bien que la voir faire ça est impressionnant."


hi "Après les cours, alors."

scene bg school_scienceroom at bgleft
with shorttimeskip


"Après les cours, je ne gâche pas une seconde avant de me mettre en action."

show shizu invis:
    center
    xpos 0.75
show mishashort invis_close:
    center
    xpos 0.15
with None

show shizu behind_frown at tworight
show mishashort perky_sad_close at twoleft
show bg school_scienceroom at center
with dissolvecharamove


"Alors que tout le monde sort de la classe, nous laissant juste tous les trois, Misha regarde de tous les côtés sauf devant elle."


hi "Tu veux manger quelque chose ?"

show mishashort hips_frown_close
with charachange


mi "Pourquoi est-ce que Shicchan et toi n’arrêtez pas de me demander si je veux manger quelque chose~ ? ~Hicchan ?"


hi "Parce qu'on va à la cafétéria et qu'on n'a pas mangé ensemble depuis un long moment. Alors, pourquoi pas ?"

show mishashort perky_confused_close
with charachange


mi "C'est à propos du Conseil des Étudiants ?"

show shizu behind_blank
with charachange

shi "…"

show mishashort perky_sad_close
with charachange


"Prenant l'absence de réponse de Shizune comme une confirmation, Misha soupire."

show mishashort hips_frown_close
with charachange


mi "Shicchan, tu ne penses qu'à ça ?"

stop music fadeout 5.0

hide mishashort
with charaexit


"Avant que Shizune puisse répondre, elle part. Je dois dire que je ne me sens pas très confiant après ce qui vient de se passer."

show shizu behind_blank at center
show bg school_scienceroom at bgleft
with charamove


"Aucun de nous deux n’espérait que ça puisse se passer parfaitement, mais ça aurait été bien."

show shizu adjust_frown
with charachange


"Lisant dans mes pensées, Shizune fait passer un doigt sur ses lunettes un moment avant de signer."

show shizu basic_angry
with charachange


ssh "Je sais ce que tu penses, mais non, je ne pense pas qu'on devrait lui laisser de l'espace. Je t’ai dit que je n'abandonnerais pas aussi facilement."


his "Ouais, enfin, maintenant je commence à me demander si ce n'est pas trop tôt."

show shizu behind_frown
with charachange


ssh "Tu as la frousse ?"

show shizu adjust_frown
with charachange


ssh "Eh bien pas moi. Je n'abandonnerai pas."

show shizu behind_blank
with charachange


ssh "Il y a une différence entre aider les gens et les cajoler. Je veux juste que Misha se ressaisisse et arrête d'agir aussi bizarrement."

show shizu basic_normal
with charachange


ssh "Je sais qu'elle peut le faire. Même si elle veut essayer, les gens ne changent pas en un jour. S'ils pouvaient, le monde serait un bien meilleur endroit."


his "D'accord, tu gagnes."


his "Alors j'imagine que c'est le moment où on se sépare et où on la cherche."


"Même si je suis le seul qui soit vraiment supposé la trouver."

show shizu adjust_happy
with charachange

play music music_tranquil fadein 3.0


ssh "Si je la trouve en premier, je t'appelle sur ton portable."


"Souriant, Shizune sort son téléphone. Je remarque qu'elle a un très grand nombre de messages non lus, et voyant sa réaction, elle aussi. Laissant son téléphone pendre en le tenant par le strap quelques secondes, elle grimace."

show shizu behind_frown
with charachange


ssh "Je n'aime pas utiliser ce truc."

show shizu basic_angry
with charachange


ssh "Pourquoi je ne peux pas juste claquer des doigts ?"


his "Et puis quoi ? Je ne suis pas un chien. Et ça ne va pas aussi vite qu'un téléphone."

show shizu behind_smile
with charachange


his "Tu t'amuses beaucoup, hein ?"


"Secouant la tête, elle continue."

show shizu adjust_happy
with charachange


ssh "Il est assez évident de savoir où elle va aller. Tu ne peux pas la chercher sur les terrains de l'école, elle va vouloir aller aussi loin qu'elle le peut."

show shizu behind_blank
with charachange


ssh "Vérifier le magasin de thé ? C'est généralement vide à cette heure-ci. Misha adore y aller quand elle loupe les cours, et elle adore les parfaits en vente là-bas."


"J'ai envie de lui dire : “Tu la connais vraiment bien.” Mais elle réfléchirait trop, et comprendrait de travers, donc je choisis de juste hocher la tête et de partir, jusqu’à ce que je sente qu'elle me retient par la manche."

show shizu basic_normal_close
with characlose


hi "Quoi ?"


"Je dis ça instinctivement, oubliant qu'elle ne peut pas m'entendre."

show shizu behind_smile_close
with charachange


ssh "C'est agréable de ne pas avoir à faire ça toute seule maintenant, parce que je peux te faire confiance. Je suis vraiment contente."


"Ça me fait plaisir d'entendre ça. Je ne trouve rien à dire, et me contente de hocher de nouveau la tête."

play ambient sfx_crowd_indoors fadein 2.0

scene bg school_lobby
show mishashort perky_confused:
    center
    xpos 0.6
    ypos 1.05
show crowd
with locationskip


"Me dirigeant vers l'extérieur, je vois l’arrière d'une tête de fille aux cheveux roses, et je vais par là. Je réalise que ce n'est pas le chemin à prendre pour sortir de l'école."


"C'est le chemin vers le conseil des étudiants. Si je voulais éviter Shizune, je n'irais pas par là."


"C'est étrange que Misha aille dans cette direction, alors. Peut-être qu'elle veut parler avec Shizune."


"Auquel cas, je dois me demander si laisser les choses se dérouler par elles-mêmes serait une si mauvaise idée, surtout si ça semble aller dans une bonne direction."

show mishashort invis as mishafront:
    center
    xpos 0.6
    ypos 1.05
with None

show mishashort invis at center
show mishashort hips_smile as mishafront at center
with Dissolvemove(0.7)

hide mishashort
hide mishafront
with None

show mishashort hips_smile at center
with None


"Soudainement, Misha s’arrête et se tourne, me prenant par surprise."

show mishashort hips_grin
with charachange


mi "Surprise~, Hicchan~ ! Tu me cherchais ? Je le sentais~ !"


"J'allais dire “Je te cherchais justement”, mais ce n'est plus la peine maintenant."

show mishashort hips_grin:
    easeout 0.7 xpos 1.0 alpha 0.0
with Pause(0.7)


"Elle n'a même pas encore fini sa phrase qu'elle passe comme une fusée à côté de moi, se dirigeant vers la sortie. Je dois admettre que Misha est vraiment bien plus malicieuse que je ne l'aurais cru. Et étonnamment rapide aussi."

stop ambient fadeout 2.0

scene bg school_courtyard
with locationskip


"Bien que ce soit plus difficile physiquement que je ne l'aurais cru, je réussis à la rattraper avant qu'elle n'arrive au portail."


hi "Tu es vraiment la femme la plus malpolie du monde à cet instant."


hi "Tu ne peux pas arrêter de t'enfuir une seconde ? Je veux te parler."

show mishashort cross_smile at center
with charaenter


"Misha tourne les talons, ayant l'air un peu amusée, et lève les mains comme pour me dire d'accord. Maintenant que j'ai son attention, j'ai du mal à trouver la bonne chose à dire."


hi "Où tu vas ?"

show mishashort sign_smile
with charachange


mi "Au Shanghai~."


hi "Je peux aller avec toi ?"

show mishashort perky_confused
with charachange


"L'attente de sa réponse semble durer une éternité. C'est presque comme si je pouvais entendre ma montre égrener chaque seconde."

show mishashort hips_smile
with charachange


mi "D'accord, Hicchan."

stop music fadeout 3.0


"J'ai le sentiment qu'elle accepte juste parce qu'elle n'a pas envie de continuer la conversation."

scene bg suburb_shanghaiint
show mishashort perky_smile:
    center
    ypos 1.02
with shorttimeskip

with Pause(0.2)

play sound sfx_storebell
show mishashort perky_confused:
    ease 0.1 ypos 1.0
    ease 0.2 ypos 1.02
with Pause(0.3)


"Quand nous arrivons, un couple vient après nous, faisant sursauter Misha."

show mishashort perky_smile_close at Position(ypos=1.1)
with dissolvecharamove


"Voyant que ce n'est pas Shizune, elle se relaxe, souriant presque comme d'habitude en commandant un parfait à Yuuko et se dirigeant vers la table la plus proche."


hi "Tu t'es enfuie trop vite. Tu aurais au moins pu attendre de voir ce qu'elle allait dire."

show mishashort hips_frown_close
with charachange


"Le fait que Misha s’énerve m'indique que peut-être elle était effrayée de ce qu'aurait pu dire Shizune."


mi "Pourquoi vous faites ça tous les deux, Hicchan ?"


hi "Parce que Shizune veut toujours être ton amie. Je crois que pour elle c'est comme lancer un missile nucléaire depuis un sous-marin, il faut deux clés pour ça."

show mishashort perky_confused_close
with charachange

mi "…"


hi "Qu'est-ce qu'elle peut faire d'autre, après tout ?"


"Elle ne signe plus automatiquement tout ce qu'elle entend ou dit maintenant, et je suis sûr que c'est pour ça que Shizune a eu autant de mal avec elle."


hi "Quand elle essayait de juste t'en parler, tu ne l'écoutais pas."

show mishashort perky_sad_close
with charachange

play music music_night fadein 6.0


"L'expression coupable de Misha m'indique que j'ai appuyé là où il faut."


hi "Tu détestes vraiment Shizune à ce point-là ?"

show mishashort sign_confused_close
with charachange


mi "Non, Hicchan. Je te l'ai dit ça."

show mishashort perky_confused_close
with charachange


"Elle répond sans tressaillir, jouant avec une cuillère."


hi "Ouais, je sais."


hi "Je suis sûr qu'elle le sait aussi, mais je me demande si ça serait plus facile si c'était le cas."


hi "La seule chose à laquelle elle a réfléchi cette dernière semaine est comment te rendre heureuse, vu qu'elle est toujours attachée à toi. Hier, cela dit, elle a pensé que ça serait peut-être plus facile si tu la détestais."


hi "Comme tu ne lui as pas dit que tu la détestais, Shizune croit que vous pouvez toujours être amies. Elle est comme ça, pensant seulement aux extrêmes."


"Son parfait commence à fondre, les ingrédients commencent à se rejoindre dans de petites rivières qui me rappellent les racines d'un arbre qui grandit sur des photos prises durant un grand laps de temps."

show mishashort cross_frown_close
with charachange


mi "C'est stupide. Shicchan n'est pas si stupide, Hicchan. Ne sois pas ridicule~."


hi "Ça n'a rien à voir avec l'intelligence. Des gens intelligents peuvent faire des choses stupides. J'étais terrifié la semaine derrière quand on a parlé, mais j'étais soulagé parce qu'on aurait dit que les choses auraient pu revenir à la normale."


hi "Je ne m'attendais pas à ce que vous ayez une dispute juste après."

show mishashort perky_confused_close
with charachange


mi "Ce n'était pas une dispute, Hicchan. Je lui ai juste crié dessus."


"J'ai remarqué que la voix de Misha ne change jamais vraiment de ton, juste de volume. Sa voix est si faible par culpabilité que j'ai du mal à croire que ce soit la sienne."


hi "Dans tous les cas, j'étais content, parce que j'ai cru que vous pouviez toujours être amies. Elle a besoin de toi."

show mishashort sign_confused_close
with charachange


mi "Mh~. Non, ce n'est pas vrai, Hicchan."


hi "Comment tu sais ça ? Il y a beaucoup de choses que Shizune ne peut..."


"Exprimer ? Dire ? Raconter ? J'ai peur que si je dis la mauvaise chose, ça ruine l'ambiance. J'ai enfin une conversation avec elle et ne veut pas la gâcher. Je me demande si c'est la première fois qu'elle a une conversation honnête avec moi."


hi "Le simple fait qu'elle ne te l'ait pas dit ne veut pas dire qu'elle ne t'apprécie pas."

show mishashort hips_frown_close
with charachange



mi "C'est pas logique..."


hi "Si. Sinon, elle se disputerait avec toi."

show mishashort hips_grin_close
with charachange

mi "Wahaha~."


hi "Tu ne crois pas ? Elle se dispute avec tout le monde, alors pourquoi pas avec toi ? Parce que tu es son amie, et qu'elle t'accorde de l'importance. Et Shizune en souffre, aussi."


hi "Elle est juste pas douée pour exprimer ses sentiments. Elle le fait généralement de la mauvaise façon, aussi. Mais elle t'adore quand même."

show mishashort perky_confused_close
with charachange


mi "Hicchan, tu te rappelles quand j'ai dit que je voulais pas détester Shizune, ou lui faire de mal ? La vérité est que~, j'ai fini par faire les deux. Maintenant il y a, genre, une gêne entre nous deux. C'est difficile à expliquer."


hi "Vous êtes si têtues toutes les deux. Tu disais que tu ne voulais pas t'éloigner de Shizune, mais tu laisses quand même ça arriver."


hi "Et Shizune ne fait pas mieux. Elle veut que tu sois son amie, mais te respecte trop pour être aussi agressive avec toi qu'elle pourrait l’être avec n'importe qui."


"Et je suis sûr que Misha interprète l'espace que lui donne Shizune comme un manque d'attention."

show mishashort perky_sad_close
with charachange


mi "J'ai déjà tout foiré, Hicchan. Ça arrivera encore~, j'en suis sûre. Quand j'y pense comme ça, je ne sais pas ce que je suis censée faire. Ça ne fera qu'empirer les choses. Alors c'est mieux si je ne fais rien en fin de compte, hein~ ?"


hi "Ne sois pas ridicule. Pourquoi est-ce que tu penses ça ? Sois plus positive."


"J'ai envie de lui dire “Ça devrait être facile pour toi” mais ça ferait présomptueux."

show mishashort hips_smile_close
with charachange


mi "Hicchan~, je ne savais pas que tu étais si optimiste. Je ne m'y attendais pas."

hi "…"

show mishashort perky_smile_close
with charachange


mi "Tu agis toujours si lugubrement quand j'essaye de te surprendre."


hi "Non, c'est juste récent chez moi. Vraiment. Je déteste juste quand les gens abandonnent trop facilement maintenant."

show mishashort cross_grin_close
with charachange

mi "Haha~."

show mishashort perky_smile_close
with charachange


mi "“Maintenant”, hein~... ?"


hi "Ça m'énerve quand les gens abandonnent. J'avais l'habitude de penser qu'abandonner était une façon de s'enfuir, vu que c'est comme ça que les gens décrivent toujours ça, mais maintenant que j'y pense, c'est plus comme jeter quelque chose."


hi "Quand tu fuis quelque chose, tu peux y penser comme si c'était toujours là. Quand j'étais à l’hôpital, je ne voulais pas juste fuir mes problèmes, je voulais aussi ne plus jamais y penser."


"Misha mange une cuillérée de sa crème glacée grise un peu fondue. Est-ce qu'elle vient de se rappeler qu'elle était là, ou est-ce qu'elle l'aime comme ça ?"


hi "Dans tous les cas, ce que je veux dire est que tu ne peux pas faire ça. Les gens sont trop sentimentaux pour que tu puisses juste jeter tes souvenirs d'eux."


hi "C'est impossible. Shizune ne pense à la vie qu'en termes de victoire et de défaite ; tu ne crois pas qu'elle aimerait ne pas avoir à se rappeler les fois où elle perd ?"


hi "Tu ne peux pas juste choisir. C'est comme vouloir vivre dans une bulle. Le pire est que ta façon de pensée est destructrice. Ça te rend tellement pessimiste que tu as peur de tout."

stop music fadeout 4.0


hi "Allez."


"Je lui attrape la main et fais signe à Yuuko avec l'autre pour payer ce qu'on a pris."

show mishashort sign_confused_close
with charachange


mi "Où est-ce qu'on va maintenant ?"


hi "On retourne à l'école avant que le déjeuner soit fini, mais je veux passer à certains endroits avant."

scene bg school_gate:
    right
    subpixel True
    linear 30 left
with locationskip

play music music_comfort


"Bien que je me sente fatigué après avoir fait ce qui peut être décrit au mieux comme un jogging rapide, Misha et moi arrivons finalement aux portes de l'école avec une dizaine de minutes d'avance."


hi "Je ne voulais même pas vraiment venir dans cette école, tu sais. Je n'avais pas le choix. Quand je suis arrivé à cette porte, je suis sûr qu'une partie de moi pensait “Quel endroit déprimant.”"


hi "Ça ne semble pas déprimant du tout pourtant. Je croyais avoir tout compris. Je me sens pratiquement comme une nouvelle personne."


hi "Si je le pouvais, je retournerais dans le passé et me dirais d’arrêter de croire que je peux tout juger d'un seul regard et agir comme si ma vie était déjà finie, et que je peux encore m'amuser."

scene bg school_gardens:
    right
    subpixel True
    linear 30 left
with locationskip


"Il y a pas mal de monde sur les terrains de l'école. C'est l'heure du déjeuner, donc c'est normal."


hi "C'est là que Shizune et toi m'avez fait vous aider à mettre en place deux festivals. Vraiment beaucoup de travail. Je pensais “Je n'ai pas le temps pour ça.”"



hi "Quand j'y repense, je n'ai pas fait tant que ça. Et je n'avais aussi rien de mieux à faire. J'aurais juste passé mon temps tout seul."

scene bg school_scienceroom:
    right
    subpixel True
    linear 30 left
with locationskip


"Je l’entraîne jusqu’à notre salle principale, qui est vide à l'exception de Mutou qui essaye de manger un sandwich avant que les cours ne reprennent."


hi "À chaque fois que je pensais à l'une d'entre vous, j’espérais juste que vous me laissiez seul. Que ce soit là, ou..."

scene bg school_lobby
with locationskip


"Laissant Mutou à son déjeuner, nous nous dirigeons vers le distributeur le plus proche, et je prends un soda pendant que j'ai encore cinq minutes. J'ai passé la pause déjeuner entière avec Misha, ce qui est plus longtemps que ces derniers jours réunis."


hi "...quand vous me suiviez à la cafétéria, ou essayiez de me coincer après les cours."


hi "Je n'ai jamais réalisé qu'on avait parlé que, genre, quatre fois. Ça me restait vraiment en tête. Je ne le réalise seulement que maintenant."

show mishashort hips_smile at center
with charaenter


mi "Je me rappelle de ça, Hicchan. Mais~, je sais où sont tous ces endroits, aussi."


hi "Attends, laisse-moi finir mon tour guidé. On n'a plus beaucoup de temps. À propos, tu veux un soda ?"

scene bg school_staircase2
with locationchange


"Nous nous dirigeons vers les escaliers, je suis content de ne plus avoir à la tirer par la main maintenant."


hi "Tu as le vertige dans les escaliers, c'est ça ?"

show mishashort perky_sad_close at twoleft
with charaenter


mi "Ouais~."


hi "Alors là ça suffira."

show mishashort perky_sad_close:
    ease 1.0 ypos 1.2
with Pause(1.0)


"Je m'adosse au mur alors que Misha s'assied sur les marches."


hi "Les gens avec qui tu as été en primaire ou au collège te manquent des fois ?"

show mishashort perky_confused_close
with charachange


mi "Non."


"C'était rapide. Elle n'y a même pas pensé. Je grimace par réflexe."


hi "J'avais plus d'amis dans mon ancienne école, mais je ne leur parle plus maintenant. J'ai l'impression que c'était dans une vie antérieure. Ce qui est triste en y pensant."


hi "Des fois j'ai envie de leur reparler, mais je sais que je ne peux pas. J'ai peur, et je suis embarrassé, des trucs comme ça. Ils sont trop loin de moi pour que je puisse les voir maintenant. Alors j'envisage de les appeler, mais je ne connais pas leurs numeros."


hi "Et je suis parti sur une mauvaise note. Alors pourquoi est-ce qu'ils voudraient me revoir ?"


hi "J'ai l'impression que je devrais juste oublier, mais j'y pense toujours et regrette de ne pas avoir plus essayé de rester en contact."


hi "Et je commence à penser que peut-être oublier serait une mauvaise chose. Ça serait une insulte pour tous les gens avec qui je me suis amusé et ai passé du bon temps."


hi "Comme je l'ai déjà dit, même s'il y a de mauvais moments aussi, c'est pas grave tant que tu peux repenser aux bons moments."


hi "Je ne pensais pas comme ça avant. C'était comme si je m'étais réveillé un jour et que j'avais réalisé que je n'avais pas d'amis. J'ai perdu tous mes amis, et c'était horrible. Je détesterais vraiment si Shizune et toi finissiez pareil, c'est tout."

show mishashort perky_sad_close
with charachange


mi "“C'est tout~.”"


hi "Ça me rend triste de penser que tu puisses faire la même chose et repousser ton amie. Surtout vu que tu n'es pas loin de Shizune, je veux dire, tu vis même dans le même dortoir."


mi "Amie, mh~..."

show mishashort perky_confused_close
with charachange


mi "Tu es mon ami aussi, hein, Hicchan ?"


hi "Ouais."


hi "Tu as dormi tout le long, mais les feux d'artifice étaient vraiment bien, au festival."


hi "C'est la première fois que je voyais des feux d'artifice comme ça. Et la première fois depuis longtemps que je voyais vraiment le ciel. Et je n'avais jamais vraiment regardé les étoiles avant non plus."


"J'avais feuilleté un livre à l’hôpital à ce sujet, et j'ai beaucoup appris."


"Du genre que les étoiles ne se contentent pas de brûler, qu'elles sont plus comme une suite constante d'explosions, et qu'elles sont si loin que certaines étoiles qu'on voit peuvent être éteintes depuis des milliers d'années déjà."


"C'est juste que leur lumière atteint seulement maintenant la Terre. J'ai vu une maquette comparant la taille de la planète avec le soleil, et après avec d'autres soleils. Le Japon n'était même pas visible sur la petite Terre dans le livre."


hi "Tu sais ce que j'ai réalisé ?"

show mishashort perky_smile_close
with charachange


"Elle me regarde, attendant la suite."


hi "Ils sont incroyablement brillants."

show mishashort hips_grin_close
with charachange

mi "Ahahaha~."


hi "C'est vrai."

show mishashort perky_confused_close
with charachange


mi "Pourquoi est-ce que tu fais ça, Hicchan ?"


hi "Fais quoi ?"

show mishashort cross_frown_close
with charachange


mi "Je ne suis pas idiote."


hi "Je ne sais pas. Plusieurs raisons. Parce que tu es l'amie de Shizune ? Et que j'aime à quel point vous êtes proches ? Et peut-être que j'essaye de te dire qu'on a tous nos défauts, mais qu'abandonner est idiot. Enfin, ça me semble valoir le coup."

show mishashort sign_smile_close
with charachange


mi "C'est la seule raison ?"


hi "Et tu es mon amie."

show mishashort hips_smile_close
with charachange


mi "C'est tout ?"


hi "Je ne peux pas faire quelque chose sans raison ?"

show mishashort hips_grin_close
with charachange


mi "Wahaha~. Tu peux, tu peux~, mais~, je veux savoir."


hi "Eh bien, qu'est-ce que tu veux entendre ?"

play sound sfx_warningbell
stop music fadeout 3.0


"La cloche sonne avant que Misha puisse répondre, donc elle finit par rire à la place."

scene black
with dissolve




label fr_S34:

scene black
with dissolve


"Je vois moins Misha les jours suivants. Mais je ne m’inquiète pas, parce que à chaque fois que je la vois, elle ressemble plus à son ancienne elle."


"Une fois qu'il est suffisamment clair que ce n'est pas mes espoirs qui me font imaginer ça, je commence à me détendre à nouveau."

window hide

with Pause(1.0)

scene bg school_dormhisao
with openeye

window show


"Je me réveille très tôt et me sens malade dimanche. J'ai été me coucher trop tôt la nuit dernière aussi. Quelque chose ne va pas avec mes rideaux, ils ne se ferment pas complètement."


"À cause de ça, je ne peux pas essayer de me rendormir. J'ai le soleil dans les yeux à chaque fois. Je suis sûr que c'est probablement pour ça que je me suis réveillé si tôt ce matin."

play sound sfx_doorknock


"Être aussi malade et fatigué est un cocktail menant à la frustration. Je suis presque content quand quelqu'un frappe à ma porte."

scene bg school_dormhallway
show kenji neutral at center
with locationchange

play music music_kenji fadein 0.5


"C'est une personne qui m'est familière et qui tient une pomme presque entièrement mangée dans sa main."


"Croquant une dernière fois dedans, il essaye de la lancer dans ma corbeille et la loupe complètement, et elle s’explose sur le mur à peu près deux mètres trop haut."



"Pour être honnête, la plupart des morceaux restants réussissent à tomber dans la corbeille, mais je suis sûr que personne n'est assez effronté pour faire ça volontairement."

show kenji happy
with charachange


ke "Tir parfait !"

show kenji neutral
with charachange


ke "Quoi de neuf, coloc ?"


hi "Je ne suis pas ton coloc, on ne vit pas ensemble."

show kenji tsun
with charachange


ke "Peu importe."


hi "Si, tu devrais au moins connaître la différence entre vivre ensemble dans le même bâtiment et vivre ensemble dans la même chambre."

show kenji neutral
with charachange


ke "J'ai besoin d'utiliser ta chambre."


hi "Pour quoi ?"


"J'ai foiré, j'aurais dû dire “hors de question”."

show kenji tsun
with charachange


ke "Le Conseil des Étudiants continue de me livrer mon courrier, même après que j'aie demandé qu'elles me le mettent dans mon casier ou autre."


ke "Mais elles continuent de me le mettre sous ma porte, me livrant mon courrier sans que je le remarque, donc aujourd'hui, je vais me tapir ici en attendant qu'elles agissent... comme un détective, ou un chasseur de safari."

show kenji neutral
with charachange


ke "J'ai besoin de rester dans ta chambre aujourd'hui et de regarder via le trou de la serrure, sinon je ne pourrai pas les prendre sur le fait. Et peut-être demain, aussi."

show kenji happy
with charachange


ke "Ça va être génial, on prendra de la pizza, les deux jours. Ou peut-être qu'on devrait prendre la pizza un jour et quelque chose d'autre le deuxième jour ? Mais quoi ? Et quel jour est le jour de la pizza ?"


hi "Pas aujourd'hui. Jamais. Tu sais, je suis dans le Conseil des Étudiants. Pourquoi tu ne m'as pas juste demandé ?"


"S'il l'avait fait, j'aurais pu m'en occuper très facilement et n'aurais pas eu Kenji dans ma chambre. C'est gagnant-gagnant, sauf que j'imagine que là il va pouvoir m’extorquer une pizza."


"Je commence à penser que c'était peut-être le but de Kenji depuis le début."


"Mais... Non, j'en doute. Il est impossible qu'il ait pu prévoir quelque chose d'aussi élaboré."

show kenji tsun
with charachange


ke "Tu le sais ?"


hi "Quand ils livrent le courrier ? Eh bien, non. Ils me donnent le mien quand je vais au Conseil des Étudiants généralement. Mais je pourrai leur demander. Alors je pourrai te le dire. C'est comme ça que les gens découvrent les choses, en demandant."

show kenji neutral
with charachange


ke "Pas les hommes des cavernes. Et ouais, pas de réponse à ça, hein ? Échec et mat."


hi "...Utilise ton propre trou de serrure."

show kenji tsun
with charachange


ke "Et si elles me voient ?"


hi "Elles ne peuvent pas, c'est le principe des trous de serrure. Toi seul pourras voir."


show kenji happy
with charachange


ke "C'est vrai ? Enfin... Pas moyen. Elles s'attendront à ce que je sois dans ma chambre de toute façon. Elles sentiront ma présence et sauront que je suis là. Elles ne s'attendront jamais à ce que je sois dans la chambre en face."


hi "Je vais au bureau du conseil des étudiants et je vais te prendre ton courrier. Tout de suite."

show kenji tsun
with charachange


ke "Dans ce cas je ne peux pas te laisser partir."


hi "C'est idiot. Et si je dois utiliser les toilettes ?"

show kenji neutral
with charachange


ke "Tes tours ne marcheront pas avec moi."

scene bg school_dormhisao
with locationchange


"Je m'assieds à mon bureau et commence à faire mes devoirs pour le week-end."


hi "Tu sais, tu vas finir par sortir à un moment, tu ne peux pas rester là pour toujours, et me garder éternellement. C'est ma chambre en plus."

show kenji neutral at tworight
with charaenter


ke "Ouais, je ne pense pas pouvoir. À quelle heure est-ce que le courrier arrive ?"


hi "Maintenant."

show kenji tsun
with charachange


ke "Pourquoi est-ce que les femmes sont si lentes ?"


hi "Pourquoi tu te préoccupes autant du courrier après tout ? Tu attends quelque chose ?"

show kenji neutral
with charachange


ke "J’attends toujours quelque chose. ...Pas aujourd'hui, cela dit."


hi "Tu veux qu'elles envoient quelque chose pour toi ? Tu envoies des choses parfois ?"

show kenji tsun
with charachange


ke "Nope ! C'est comme ça qu'elles t'attrapent. Je n'ai pas envoyé de courrier depuis que j'ai huit ans. J'ai envoyé une lettre à Lego pour leur demander de faire des Lego Dragon Ball."


show kenji happy
with charachange


ke "Ils ont dit qu'ils pouvaient pas avoir les droits et m'ont donné des bons de réduction. Ça a valu le coup, mais après ça je me suis assuré de faire profil bas."

show kenji neutral
with charachange


ke "Tu n'envoies pas de courrier, hein ?"


hi "J'ai écrit à mes parents la semaine dernière."

show kenji tsun
with charachange


ke "Mais c'est comme ça qu'elles t'attrapent !"


hi "Ouais, j'aurais dû le savoir. C'est peut-être pour ça qu'elles ont inséré cette mini-puce en moi l'autre jour."

show kenji neutral
with charachange


ke "Donc... les rumeurs étaient vraies."


"J'aimerais savoir d’où il tient cette rumeur."


hi "Je plaisantais. C'est une blague."

show kenji tsun
with charachange


ke "Blague ? Merde. Tu me ferais des blagues ? J'imagine que c'est ce qu'on ressent... quand on te fait des blagues. Je n'aurais jamais cru que ça m'arriverait. C'est sérieux. Mec, je crois que tu ne comprends pas les profondeurs de mon dilemme."


ke "C'est en plusieurs actes. Des actes compliqués, avec plusieurs joueurs. C'est vraiment dur, d'accord ? Après que j'aie fini je mangerai un poisson entier, pour célébrer."


ke "Aaaah, merde. Je voulais une pizza. Je veux toujours une pizza. Je peux avoir du poisson sur la pizza ? Ils font ça maintenant ?"


hi "Alors c'est toi qui payes. Tu ne m'as toujours pas remboursé, et je n'ai pas faim de toute façon."

show kenji neutral
with charachange


ke "T'es pas d'humeur pour une pizza ? C'est pas possible ça, fiston."

show kenji tsun
with charachange


ke "Ça se doit d’être une pizza. Je suis au stade pizza de ma vie. Avant j'étais au niveau glace, mais ma petite copine n’arrêtait pas de manger toutes les fraises de mon napolitain. Ça t’arrivera probablement aussi."


"C'est difficile de dire s'il est sérieux, la moitié du temps. Je peux seulement voir son expression quand il n'a pas le nez contre la porte."


hi "J'en doute. Hé, tu sais que j'ai une petite copine, hein ? Pas Iwanako, non plus. La présidente du Conseil des Étudiants, à vrai dire."

show kenji neutral
with charachange


ke "Je le sais depuis longtemps."


hi "Quoi ? Sérieux ?"

show kenji happy
with charachange


ke "J'ai mes sources."

show kenji tsun
with charachange


ke "Bref... Je me suis rendu compte que j'étais devenu gros avec toute cette glace. C'était une mise au point difficile. Comme dormir sur une plage et se faire réveiller par une vague qui détruit ton château de sable."

show kenji neutral
with charachange


ke "J'ai commencé à courir. Je devais perdre du poids. Mais peut-être... que je courais pour me fuir moi-même."


play sound sfx_doorknock
stop music
show kenji rage:
    tworight
    ease 0.3 twoleft
with vpunch


"Une série de frappes soudaines le font bondir en arrière, suffisamment pour qu'il cogne le mur derrière lui. Je profite de l'opportunité pour marcher jusqu’à la porte et l'ouvrir."

play sound sfx_dooropen

scene bg school_dormhallway
show shizu behind_blank
with locationchange


ssh "Bonjour. Quoi de neuf ?"


ke "J'ai entendu dire que si tu mets du sel devant ta porte elles ne peuvent pas entrer si elles ne sont pas invitées."

play music music_comedy fadein 4.0

scene bg school_dormhisao
show kenji neutral at center
with whip_left


hi "Je ne vais pas mettre du sel devant ma porte."

show kenji happy
with charachange


ke "Mais... tu l'envisages. Bien."

scene bg school_dormhallway
show shizu behind_blank
with whip_right


hi "Bonjour. Tu es là pour délivrer le courrier ?"

show shizu adjust_happy
with charachange


"Hochant la tête, Shizune agite quelques enveloppes devant nos visages. Je les prends, libérant ses mains pour converser."

show shizu basic_normal2
with charachange


ssh "Comment tu savais, comment tu savais ?"


hi "Tu les cachais derrière ton dos, c'était vraiment évident."


ke "Cacher quoi ?"

scene bg school_dormhisao
show kenji tsun at center
with whip_left


hi "Le courrier."

scene bg school_dormhallway
show shizu basic_normal2
with whip_right

with Pause(0.2)

show shizu adjust_smug
with charachange


ssh "Pas grave, je n'essayais pas vraiment de les cacher de toute façon."


hi "Ça ne te ressemble pas. Tu es du genre à penser que “il ne faut pas faire les choses à moitié.”"


ke "Des filles qui prennent l'initiative ? Et moi ? J'utilise cette phrase depuis des années. Où est ma parade, fréro ?"


ke "Je crache littéralement de l'or, et vous les femmes le volez et le portez comme si c'était deux robes pour le prix d'une. Vous êtes le Picard de mon Kirk. Ou peut-être même Janeway."

show shizu behind_frown
with charachange


ssh "Pas tout le temps. Tu te moques de moi ?"

show shizu adjust_happy
with charachange


"Remarquant finalement Kenji, elle lui fait un signe."

scene bg school_dormhisao
show kenji tsun at center
with whip_left


hi "Kenji, la présidente du Conseil des Étudiants te dit salut."

show kenji neutral
with charachange


ke "Salut."

scene bg school_dormhallway
show shizu behind_blank at center
with whip_right


ssh "Présente-moi. Je n'ai aucune idée de ce qu'il a dit, mais il semblait sûr de lui."


"Oh oui, personne n'est plus doué que lui pour dire ce genre de choses avec assurance."


hi "Je l'ai déjà fait. Je t’ai même présentée par ton titre. C'est Kenji, c'est le gars qui habite la chambre en face de la mienne. Bref, tu as son courrier aussi ?"

show shizu adjust_happy
with charachange


ssh "Je livre juste ton courrier parce qu'il était là. J'y ai accès plus tôt ! Tout est une question de localisation. Considère ça comme un avantage d’être dans le Conseil des Étudiants."


"Ça ne me semble pas très équitable. Elle prend beaucoup de libertés grâce à sa position. Au moins ça reste de petites choses."


label fr_S34a:


ssh "Je ne suis jamais entrée dans ta chambre auparavant. C'est intéressant."


label fr_S34b:


ssh "C'est la première fois que je suis vraiment capable de voir ta chambre."


"C'est un mensonge flagrant, ou elle l'aurait signé beaucoup plus vite. Je suis sûr que Shizune se rappelle que ce n'est pas la première fois."


label fr_S34c:

show shizu basic_frown
with charachange


ssh "Pourquoi est-ce qu'il peut voir ta chambre et que moi je ne peux pas ? C'est un truc de mecs ?"


hi "Il n'y a pas de club secret pour les mecs."


ke "Y devrait y en avoir. Avec des bagues. Des bagues avec des emblèmes qui défoncent. Et de l'or !"

show shizu adjust_smug
with charachange


ssh "Tu es sûr ? Tu es vraiment sûr ? J'ai toujours cru qu'il y avait une fraternité secrète des hommes."


ke "Pourquoi est-ce qu'elle m'ignore ? Laisse-moi lui parler du club de mecs. Et aussi, c'est quoi cette histoire de signaux des mains ? Est-ce qu'elle essaye de me jeter un sort ou un truc du genre ?"

scene bg school_dormhisao
show kenji tsun at center
with whip_left


hi "Non, reste en dehors de ça. Je vais devoir traduire tout ce que tu lui dis, et je ne suis pas sûr d'y arriver. Et elle comprendra sûrement mal, et puis tu comprendras mal la réponse, et je vais devoir traduire ce que tu réfutes."

show kenji happy
with charachange


ke "Réfuter ? Pourquoi est-ce que je me réfuterais ? J'aime bien mon fut."

scene bg school_dormhallway
show shizu behind_frustrated at center
with whip_right


ssh "Qu'est-ce qu'il dit ?"


hi "Il dit qu'il ne va pas réfuter."

show shizu basic_normal
with charachange


ssh "Réfuter quoi ? Je n'ai même pas encore commencé à le défier."


"Je n'aime pas la façon dont elle dit ça. Donc, il apparaît qu'elle le veut. Mais à quel propos ? Ça importe peu, puisque ça finirait mal dans tous les cas."


hi "Ne cherche pas les problèmes quand il n'y en a pas."

show shizu adjust_frown
with charachange


ssh "Je n'ai jamais rencontré tes amis. Pourquoi je ne peux pas ? On dirait qu'il est... passionné."


"J'imagine que vu la façon dont il s'agite, il serait bête d’espérer que Shizune pense autre chose. Bref, je ferais mieux de changer de sujet."


"Non pas que je pense que ça puisse marcher sur elle, mais je suis sûr qu'elle est venue pour une autre raison que celle de me donner mon courrier."


"Si c'était pour si peu, elle n'aurait pas pris la peine de frapper."


hi "Tu n'es pas venue juste pour me donner mon courrier ou discuter avec mes amis, hein ?"

play sound sfx_snap


"Shizune claque des doigts de frustration. Son claquement est toujours aussi bruyant."

show shizu basic_normal
with charachange


ssh "Tu as raison."

show shizu behind_smile
with charachange


ssh "Allons quelque part."


hi "Tu as déjà une idée de où ?"

show shizu adjust_smug
with charachange


ssh "Effectivement. Allons à l'endroit habituel."



"Elle sort un sac de rempli de tupperwares bien fermés qu'elle avait posé à côté de la porte. J'imagine qu'il y a à manger à l'intérieur, et cette fois, ça ne semble pas acheté en magasin. Le posant entre ses pieds, elle continue."

show shizu behind_smile
with charachange


$ doublespeak (ke, ssh, "C'est pour moi ?", "C'est la vraie surprise. Alors ?")

show shizu adjust_smug
with charachange


ssh "Il faut que j'aie quelque chose sur tout le monde au bout du compte."


"Je hoche la tête, de la façon qu'ont les gens de faire quand quelqu'un fait une remarque en face d'eux qui en dit plus qu'ils le voulaient à la base."

show kenji invis:
    center
    xpos 0.0
with None

show shizu behind_smile at tworight
show kenji tsun at twoleft
show bg school_dormhallway at bgright
with dissolvecharamove


ke "Ouais, d'accord, si vous comptez m'ignorer tous les deux, je m'en vais. Vous êtes cruels. Vous le regretterez !"

stop music fadeout 2.0

hide kenji
with charaexit

scene ev shizu_roof at shizu_roof_in
with shorttimeskip


play ambient sfx_rooftop fadein 1.0
play music music_soothing fadein 0.5


"Peu de temps après, nous nous retrouvons sur le toit de l'école."


"Est-ce que c'est habituellement déserté à cette heure-là ? Une belle journée, le week-end ? Non, bien sûr que non. Je ne peux que penser que c'est à cause de Shizune. Non pas que vider le toit requiert plus que de mettre un signe sur la porte."


"Le tupperware qui contenait le repas que m'avait préparé Shizune est posé à côté de moi. C'était un autre repas silencieux, vu que tenir les baguettes nous empêche de discuter."


"Bien que ça ne souffle pas suffisamment pour être un problème, le vent est un peu fort aujourd'hui. Le sac plastique s'envole et virevolte un peu avant de passer sur mes jambes et d’être arrêté par la pointe des pieds de Shizune."

show ev shizu_roof_towardsangry at shizu_roof_in
with charachange


"Immédiatement, elle l'attrape et commence à faire des signes, ne semblant pas contente que je rie, même si elle essaye de ne pas rire elle-même. Avec le sac la gênant, cependant, elle doit finalement s'asseoir dessus pour continuer."


ssh "Très drôle."

show ev shizu_roof_towardsnormal at shizu_roof_in
with charachange


ssh "C'était comment ?"

show ev shizu_roof2_towardsnormal at shizu_roof_in
with charachange


his "Le repas ? Il avait un goût familier."

show ev shizu_roof2_towardsangry at shizu_roof_in
with charachange


ssh "Ça veut dire que c'était mauvais."

show ev shizu_roof_towardsangry at shizu_roof_in
with charachange


his "Non, non. Je me rappelle avoir mangé l'exact même repas, quand tu l'as fait."


"Pas exactement le même. Les crevettes frites, c'était nouveau."


ssh "C'est la seule chose que je sais faire, mais j'aurais dû m'améliorer."


his "Tu l'as fait combien de fois en tout ?"

show ev shizu_roof_towardsnormal at shizu_roof_in
with charachange


ssh "C'est la seconde fois."


his "Que tu fais ce repas en particulier ?"

show ev shizu_roof at shizu_roof_in
with charachange


ssh "Que je cuisine."

show ev shizu_roof_smile at shizu_roof_in
with charachange


ssh "La prochaine fois, c'est ton tour d'essayer."

show ev shizu_roof_towardsangry at shizu_roof_in
with charachange


"La façon qu'elle a de continuellement tirer sur le coin du sac me perturbe. Je crois que je sais pourquoi elle fait ça."

show ev shizu_roof2_towardsangry at shizu_roof_in
with charachange


his "Ça t’embête vraiment à ce point-là ?"

show ev shizu_roof2_towardsnormal at shizu_roof_in
with charachange


ssh "Je veux bien les ranger."

show ev shizu_roof_towardsnormal at shizu_roof_in
with charachange


his "T’embête pas, je vais les prendre."



"Alors que je ramasse les tupperwares, je réalise qu'elle a dû faire beaucoup à manger pour pouvoir remplir tout ça. Je n'ai même pas tant mangé. Shizune doit avoir un sacré métabolisme pour manger tout ça."

stop music fadeout 1.0
play sound sfx_impact

scene black
with vpunch


"Même si je ne suis debout que depuis une seconde, c'est suffisant pour que je trébuche bêtement tout seul. Arrivant à peine à me retenir de tomber tête la première, je finis à genoux, juste à côté des cuisses de Shizune."

scene bg school_roof
with locationchange

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack
with Dissolve (0.7)


"Alors que je me redresse, une main serrée sur ma poitrine, tout ce à quoi je pense est la douleur que j'ai aux coudes et comment cette chute aurait pu me tuer. Je me sens nauséeux."


"Shizune appuie sur mon épaule pour m'aider à me remettre droit, et je remarque qu'elle me regarde bizarrement. Malheureusement même une légère poussée est suffisante pour me prendre par surprise."

show shizu basic_normal2_close:
    center
    ypos 1.1
with charaenter


ssh "Tu vas bien ?"


"Je hoche la tête, mais nous ne nous rasseyons pas l'un à côté de l'autre. C'est normal qu'étant seul avec Shizune il y ait beaucoup de silences, mais je commence à ne le remarquer que maintenant. Encore une fois, elle est celle qui brise la glace."

show shizu behind_smile_close
with charachange


ssh "Je m'attendais à ce que tu tentes quelque chose de pervers."

hi "…"

show shizu behind_sad_close
with charachange


"Et maintenant l'ambiance redevient gênante."


his "Comment va Misha ?"

show shizu basic_normal_close
with charachange

play music music_twinkle fadein 6.0


ssh "Misha semble plus contente maintenant qu'elle est redevenue comme avant. Je me suis dit que ce serait une bonne façon de le célébrer, et de te remercier de l'avoir aidée."


"Sa main s’interrompt un moment pendant qu'elle dit le dernier mot de sa phrase."


his "Tu penses trop comme une femme d'affaire."

show shizu behind_blank_close
with charachange


ssh "Je ne peux pas m'en empêcher, c'est comme ça qu'on m'a appris à faire les choses."

show shizu adjust_happy_close
with charachange


ssh "Ça me fait plaisir que tu demandes des nouvelles de Misha. Il n'est pas exact de dire qu'elle redeviendra comme avant. Elle ne le sera qu'avec toi."

show shizu basic_normal_close
with charachange


ssh "La Misha que tu connais est complètement différente de celle que je connais moi. Je me rappelle quand je l'ai rencontrée la première fois. Même si elle est mieux quand elle est joyeuse et souriante, ce n'est pas comme ça qu'elle est généralement."

show shizu behind_blank_close
with charachange


ssh "Je me demande si c'est vrai pour toi aussi ?"


"Je ne réponds pas."


his "Eh bien, si Misha est heureuse, alors ça importe peu, si ça s'est arrangé en fin de compte. Ton plan a marché."


his "Tu la connaissais aussi bien que tu l'as dit. Tu savais tout ce qu'elle dirait. Si ton idée était que je lui parle moi, alors ça ne fait pas de moi ta marionnette ? Je n'ai rien fait, alors."

show shizu cross_angry_close
with charachange


ssh "Ce n'est pas vrai. C'était ton idée à la base."

show shizu basic_frown_close
with charachange


ssh "J'avais tort. J'ai une façon très erronée de voir les choses, maintenant que j'y pense. Je suis sûr que tu le sais. Des fois, je gère tout comme une compétition entre moi-même et tous les autres. Même quand il n'y a pas d'intérêt à cela."


"Des fois ?"

show shizu behind_blank_close
with charachange


ssh "Je sais à quel point c'est facile d'ignorer quelqu'un quand il n'y a que les signes. J'aurais dû demander de l'aide. J'étais tellement sûre de pouvoir me débrouiller. C'est courageux ce que tu as fait. Même si tu ne vas pas en récolter le crédit."

show shizu basic_normal_close
with charachange


ssh "Ça mis à part, tu t'es vraiment conduit admirablement ces derniers temps."


"C'est étrange qu'elle me complimente comme ça alors que son expression faciale n'a pas changé du tout."

show shizu adjust_frown_close
with charachange


ssh "Mais !"

show shizu basic_happy_close
with charachange


ssh "“Les gens ne changent pas si facilement.” Selon toi. C'est ça ?"


"Elle me fait un clin d’œil, s'amusant clairement."


his "Est-ce que Misha te dit tout ?"

show shizu behind_blank_close
with charachange


ssh "Presque tout."


his "J'imagine que tu vas me dire que j'ai tort là-dessus, hein ?"

show shizu basic_normal2_close
with charachange


ssh "Oui et non."

show shizu adjust_frown_close
with charachange


ssh "Je suis celle qui a dit ça à Misha avant n'importe qui. Mais elle l'a mal compris. Ce n'est pas facile, mais le fait qu'elle agisse comme ça rend ça impossible."

show shizu basic_normal_close
with charachange


ssh "C'est possible, si tu le fais peu à peu. J'envisage d'essayer d’être moins compétitive."


his "Je croyais que tu appréciais ça, pourtant."

show shizu behind_smile_close
with charachange


ssh "Peut-être juste un peu. C'est pour ça que j'ai spécifiquement utilisé le mot “moins.”"


"Elle s'adosse au grillage. Il y a des choses que j'ai envie de lui dire, mais ça ne semble pas être le bon moment pour ça. C'est un sentiment que j'ai. Je sais qu'elle n'a pas encore fini."

show shizu basic_normal2_close
with charachange


ssh "Beaucoup de gens pensent que j'en fais trop."

show shizu adjust_happy_close
with charachange


ssh "J'ai... toujours pensé que je faisais juste ce qu'il faut."



"Le bruit que fait le grillage alors qu'elle s'adosse contre lui, et le délicat son aigu de ses boutons de manchette frottant contre les fils de fer sont étrangement apaisants. Tout comme la légère brise venant de derrière."

show shizu basic_normal_close
with charachange


"Shizune regarde également vers le bas, et je me demande si elle croit toujours qu'elle manque quelque chose. Le claquement de doigt qu'elle utilise pour attirer l'attention des gens prouve aussi qu'elle a une compréhension du son."

show shizu invis_close at center
with dissolvecharamove

hide shizu
with None


"Ça doit être bizarre, d’être capable de le comprendre, mais pas de l'expérimenter. Elle commence à marcher lentement sur le toit, restant collée au grillage, frottant ses boutons de manchette contre les fils. Ce n'est pas rythmique du tout."

show shizu invis_close at twoleft
with None

show shizu basic_normal_close at center
with dissolvecharamove


"Je pars dans mes pensées pendant qu'elle fait ça, et je sors de ma torpeur quand elle tourne autour de moi et me tape sur l'épaule."

show shizu behind_blank_close
with charachange


ssh "Tu te rappelles de quoi on parlait ?"


his "Quand ? Maintenant ? Bien sûr, ça vient juste d'arriver."

show shizu basic_angry_close
with charachange


ssh "Ça fait presque dix minutes."

show shizu adjust_frown_close
with charachange


ssh "La première fois que je t’ai vu, tu semblais très attaché à l'idée de te sentir désolé pour toi-même."


"Ça fait mal, même si c'est vrai."

show shizu behind_smile_close
with charachange


ssh "Désolée, désolée."

show shizu basic_normal_close
with charachange


ssh "Ça m'a donné envie de te remonter le moral dès le premier regard. J'avais peur que ce soit pour rien, aussi. Je pensais que ça serait dur de te faire changer d'avis."

show shizu behind_smile_close
with charachange


ssh "Mais c'est quand même arrivé. J'ai trouvé ça très surprenant, et tu étais facilement influencé. Quand bien même. J'étais surprise. Ça m'a fait reconsidérer beaucoup de choses. Comme... tout ça valait le coup, en fin de compte."


his "Tout ?"

show shizu adjust_happy_close
with charachange

stop music fadeout 4.0


ssh "—C'est pour ça que je t'apprécie."


his "Je vois."


"C'est agréable d'enfin savoir."

stop ambient fadeout 2.0

scene black
with dissolve



label fr_S35:

scene bg school_council_ss at right
show mishashort hips_smile_close_ss at closeleft
show shizu behind_blank_close_ss at closeright
with locationchange

play music music_ease


hi "...Et rappelez-vous, vous devez prendre ce travail au sérieux. Trop de gens pensent qu'ils peuvent juste ne rien faire, et que ce n'est pas important. C'est dangereux de penser comme ça."

show mishashort cross_frown_close_ss
with charachange


mi "Absolument~. Vous ne pouvez pas être trop sérieux~ ! Si vous ne pensez pas toujours en grand, pensez positif, et si vous montrez des signes de faiblesse, les gens vont commencer à penser que vous êtes incompétents, vous savez~."

show mishashort sign_confused_close_ss
with charachange


mi "Et peu après vous serez incapables de faire quoi que ce soit parce que votre pouvoir aura été délégué morceau par morceau, et il ne vous restera rien. C'est ce qui est arrivé la dernière fois~."

show mishashort hips_grin_close_ss
with charachange


mi "Donc~ ! Rappelez-vous~, ça peut sembler être un travail facile, mais des carnages se sont déjà produits dans cette pièce. Ahaha~."


mi "Et~, en plus de ça, gérer le personnel de l'école aussi ! Même essayer d'avoir un rapport de budget de la part d'un délégué de classe peut être un combat à mort~, parfois."


hi "...Ouais. C'est tuer ou être tué. Il n'y a pas d'amis dans la fosse et vous ne faites pas de prisonniers. ...Tu es sûre de ça ? C'est pas exagéré ?"

show shizu basic_angry_close_ss
with charachange


ssh "Vous ne semblez pas assez excités, je dois m'assurer que la transition se fait parfaitement. Encore une fois, avec du cœur !"

show aoi_keiko:
    yalign 1.0 xanchor 0.5 xpos 0.0 alpha 0.0
with None

play sound sfx_flash

show bg school_council_ss at left
show mishashort invis_close at Position(xpos=1.1)
show shizu invis_close at Position(xpos=1.6)
show aoi_keiko:
    center
    alpha 1.0
with Dissolvemove(0.5)


"Shizune tourne le poignet comme un maestro, intimidant visiblement les deux filles se tenant devant elle. Et dire que tout ça a commencé parce que l'une d'entre elles a demandé si elle ne prenait pas le travail trop au sérieux."


ssh "Est-ce que vous comprenez ?!"


hi "Est-ce que vous comprenez ? Faites comme si je criais."


"Aoi" "D'accord, d'accord ! Aaargh ! Ce Conseil des Étudiants est trop bizarre."


"Keiko" "Oui, monsieur."


hi "“Monsieur ?” À qui est-ce que vous parlez d'ailleurs ?"

play sound sfx_flash

show bg school_council_ss at right
show mishashort hips_smile_close_ss at closeleft
show shizu adjust_frown_close_ss at closeright
show aoi_keiko:
    yalign 1.0 xanchor 0.5 xpos 0.0 alpha 0.0
with Dissolvemove(0.5)


ssh "Ce n'est pas bizarre ! Vous devez y penser comme à un travail. Si vous voulez, pensez qu'ils vous paient avec le droit d'utiliser ce superbe bureau."

play sound sfx_flash

show bg school_council_ss at left
show mishashort invis_close at Position(xpos=1.1)
show shizu invis_close at Position(xpos=1.6)
show aoi_keiko:
    center
    alpha 1.0
with Dissolvemove(0.5)


hi "Vous voulez un autre sermon ?"


"Aoi" "Noooon..."


ssh "Vous pouvez partir maintenant."

stop music fadeout 5.0

scene bg school_council_ss
show mishashort perky_smile_ss:
    twoleft
    ypos 1.1
with shorttimeskip


"Et juste comme ça, la présentation du conseil des étudiants qui a duré une heure est terminée."


"Personnellement, j'ai trouvé que ça a duré cinquante minutes de trop, et aussi trouvé drôle qu'elle intègre un tour de l'école dans laquelle on est déjà tous depuis un moment, mais j'imagine que ça ne fait pas de mal."


"Je m'attendais à ce que Shizune retombe sur sa chaise, vu qu'elle a été sur les nerfs toute la journée, mais elle ne le fait pas. Elle continue de faire les cent pas dans la pièce."

show shizu invis:
    center
    xpos 1.0
with None

play music music_shizune fadein 1.0

show shizu adjust_frown_ss at tworight
with dissolvecharamove


ssh "Elles ont encore beaucoup de chemin à faire ! Pour l'instant, elles ne valent rien."

show mishashort sign_confused_ss:
    twoleft
    ypos 1.1
with charachange


mi "Eh ?"


hi "Quoi ?"

show shizu behind_frustrated_ss
with charachange


ssh "Elles croient pouvoir être le nouveau Conseil des Étudiants ? Elles sont si dispersées. Tout ce que je peux voir est le manque d'expérience. C'était notre meilleure année, je ne crois pas qu'elles ont ce qu'il faut pour prendre le relais."

show shizu basic_frown_ss
with charachange


ssh "Et je sais qu'il y a plus que eux deux. C'est comme un film avec beaucoup de budget et énormément de marketing qui est détruit par la critique, qui est la suite d'un film avec peu de marketing et de budget, et qui est pourtant acclamé."

show mishashort perky_confused_ss
show shizu behind_blank_ss:
    ypos 1.1
with dissolvecharamove


"Au bout d'un moment, elle s’arrête et s'assoit."


hi "Ça va te manquer ?"

show shizu basic_normal_ss
with charachange


ssh "Bien sûr."

show mishashort perky_sad_ss
with charachange


mi "Mh~... Je préférerais aussi ne pas avoir à partir."

show mishashort hips_smile_ss
with charachange


mi "J'aime être dans le Conseil des Étudiants, même si ça peut être fatigant aussi."


hi "Ouais, c'est clairement fatigant."

show mishashort hips_grin_ss
with charachange


mi "Seulement parce que Shicchan essaye toujours d'en faire plus qu'elle ne le doit~."

show shizu adjust_frown_ss
with charachange


ssh "Tu oublies que si j'avais fait le strict minimum, on n'aurait rien fait de l'année, mis à part distribuer des flyers et prévoir les prochaines élections pour que le Conseil d’après puisse passer une autre année à ne rien faire."

show shizu behind_frown_ss
with charachange


ssh "Et tu me demandes de laisser ça arriver ? Ne sois pas ridicule. Dans un Conseil des Étudiants comme ça, on n'aurait même pas suffisamment de pouvoir pour s'amuser."

show shizu adjust_happy_ss
with charachange


ssh "Je suis juste contente que même si j'ai clairement besoin de les mater, ces deux-là ne sont pas trop mauvaises. Pas encore en fonction, mais le nouveau Conseil des Étudiants devrait être entre de bonnes mains."


hi "Comment tu le sais ?"

show shizu behind_smile_ss
with charachange


ssh "Après le festival, elles m'ont demandé si on pouvait aussi organiser un événement pour Halloween, comme une maison hantée ou quelque chose du genre. Elles avaient quelques autres idées, aussi."

show shizu adjust_smug_ss
with charachange


ssh "Bien sûr ma réponse a été “non”. J'ai dû demander à Misha de leur dire de le faire elles-mêmes, si elles le voulaient à ce point. Elles étaient en colère, je ne sais pas pourquoi."

show mishashort cross_laugh_ss
with charachange


mi "Ahaha~."


hi "Bien sûr qu'elles se sont énervées si tu as dit ça."


"Et le fait que Misha transmette le message n'a pas dû aider."

show mishashort cross_smile_ss
show shizu behind_blank_ss
with charachange


ssh "J'étais en colère aussi."

show shizu basic_frown_ss
with charachange


ssh "D'un coup, elles veulent tout. Si elles voulaient une maison hantée, ou un voyage à la plage, ou autre, pourquoi est-ce qu'elles n'ont pas essayé de l'organiser auparavant ? C'est comme si elles profitaient de moi."

show shizu behind_frown_ss
with charachange


ssh "J'ai travaillé dur pour organiser ces festivals, et en retour elles sont venues me dire “C'était bien, mais tu peux faire ça maintenant ? Et pourquoi pas ça ? C'est ce dont j'ai vraiment envie.”"

show mishashort sign_smile_ss
with charachange


mi "Shicchan avait tort~ cela dit."

show shizu basic_happy_ss
with charachange


ssh "Oui. Elles voulaient rejoindre le Conseil des Étudiants pour que tout ça puisse arriver. Je les ai rendu jalouses et je les ai agacées. Ça peut être une sorte de motivation aussi."

show shizu adjust_happy_ss
with charachange


ssh "Le désir de faire quelque chose de grand s'étend, même si c'est juste pour frimer. Elles ont décidé de me défier."

show shizu behind_blank_ss
with charachange


ssh "Je suis impressionnée. Enfin, pour l'instant. Je dois voir comment ça se déroule un peu plus longtemps pour en être sûre."

play sound sfx_snap

show shizu adjust_happy_ss
show mishashort perky_confused_ss:
    ease 0.1 ypos 1.05
    ease 0.1 ypos 1.1
with vpunch


"Elle claque des doigts soudainement, ce qui fait presque tomber Misha de sa chaise. J'imagine que c'est impossible de s'y habituer."

show shizu basic_happy_ss
with charachange


ssh "C'est vrai ! On voulait faire une fête pour célébrer le fait de passer les rênes au nouveau Conseil des Étudiants, n'est-ce pas ? Pourquoi ne pas la faire maintenant ? Ou au moins la préparer maintenant, et la faire demain."


hi "Mais elles n'en ont même pas encore la charge. En fait, c'est la première chose que tu leur as dit : “Vous n’en avez pas encore la charge.” Ça me semble prématuré."

show shizu adjust_frown_ss
with charachange

shi "…"

show shizu behind_blank_ss
with charachange


ssh "Misha, qu'est-ce que tu en penses ?"

show mishashort hips_smile_ss
with charachange


mi "Mmh~, je suis d'accord, c'est trop tôt. En plus~, je ne pense pas que je pourrai y aller de toute façon. Désolée~ ! En fait, je dois partir tout de suite."


ssh "Pourquoi pas ?"

show mishashort hips_grin_ss
with charachange


mi "No~ comment~ !"

show shizu adjust_frown_ss
with charachange


ssh "Allez, dis-moi."

show mishashort perky_confused_ss
with charachange


mi "Bon... d'accord~ !"


"Tu sembles bien résister à la pression, Misha."

show mishashort sign_confused_ss
with charachange


mi "J'y ai pensé, et... Même si je ne voulais pas y aller, j'aurais dit oui~ ! D'habitude~. Je suis comme ça. Je devrais vraiment arrêter de faire ça, et c'est une bonne occasion pour commencer, j'imagine."

show mishashort perky_sad_ss
with charachange


mi "Si c'est une fête pour dire au revoir, je ne veux pas. Ça serait trop triste~. Je veux faire quelque chose d'autre à la place. Et après tout, Hicchan, Shicchan et toi serez toujours là demain. Ça ferait bizarre."

show mishashort hips_grin_ss
with charachange


mi "Et puis en plus, j'ai d'autres trucs de l'école à faire aujourd'hui~ ! Je ne peux pas abandonner comme ça."

show shizu adjust_frown_ss
with charachange


ssh "On peut la reporter."

show mishashort hips_frown_ss
with charachange


mi "Non. Pas d'au revoir en avance~ !"


"Elle semble très ferme en disant ça."


hi "Tu n'es pas censée partir tout de suite ?"

show mishashort hips_grin_ss
with charachange


mi "Mh~ ? Oh, c'est vrai~ ! Wahaha~ !"

show mishashort perky_smile_ss at twoleft
with Dissolvemove(0.7)

show mishashort sign_smile_ss
with charachange


mi "D'accord, à part maintenant, pas d'au revoir en avance, d'accord ?"

show shizu behind_blank_ss
with charachange


ssh "J'ai compris."

show mishashort hips_grin_ss
with charachange


mi "D'accord, à plus tard~ !"

stop music fadeout 4.0

hide mishashort
with charaexit

show bg school_council_ss:
    subpixel True
    center
    parallel:
        "bg school_council_ni" with Dissolve(5.0)
    parallel:
        ease 5.0 bgleft
show shizu behind_blank_ss:
    subpixel True
    parallel:
        "shizu behind_blank" with Dissolve(5.0, alpha=True)
    parallel:
        ease 5.0 xpos 0.5
with None


"Sur ce, il reste juste Shizune et moi seuls dans la pièce du conseil des étudiants."

play music music_dreamy fadein 4.0

with Pause(2.0)


"Le soleil se couche lentement tandis que nous nous asseyons en silence, cherchant tous les deux quelque chose à dire."

show bg school_council_ni at bgleft
show shizu adjust_frown:
    center
    subpixel False ypos 1.1
with Dissolvemove(0.5)


ssh "Ça serait une si mauvaise idée ?"


his "Ouais. Je n'y avais pas pensé comme ça, mais Misha a raison. Il y une ambiance générale dans les fêtes, et celle-là serait triste. Avoir une fête triste ne donne pas trop envie."

show shizu basic_angry
with charachange


ssh "Pourquoi est-ce que ça serait triste ?"


"C'est une question piège ? J'en suis sûr. Shizune a les yeux rivés aux miens, attendant ma réponse avec un air analytique détaché que je n'avais pas vu depuis longtemps, mais qui me semble quand même familier."


"Je réfléchis avec attention à ma réponse, mais aussi à ce que ça signifie pour elle pour qu'elle me le demande."


"Peut-être que Shizune trouve ça déprimant aussi. Ou peut-être qu'elle ne comprend pas pourquoi qui que ce soit peut trouver ça déprimant. Les deux cas sont plausibles."


his "J'ai pensé au fait que quand on a notre diplôme, c'est fini. Ça va être la fin du Conseil des Étudiants. Je me demandais si tu voyais les choses pareil que moi."

show shizu behind_frown
with charachange


ssh "Ne sois pas stupide. J'ai hâte que ça arrive. Je ne serai plus une étudiante, alors je m'attendrai à des choses bien différentes. Les attentes qu'ont les gens de moi, et les attentes que j'aurai de tout le reste. Ça semble excitant !"

show shizu adjust_frown
with charachange


ssh "Quant au Conseil des Étudiants, il sera sûrement entre de bonnes mains. Je n'ai pas de raison d’être triste."


his "Je ne crois pas que tu sois honnête. Tu semblais contrariée d'avoir à abandonner ton Conseil des Étudiants il n'y a même pas quelques semaines. Ce n'était pas la question de le laisser à une bande de débutants, c'était le fait de devoir arrêter."

show shizu behind_smile
with charachange


"Je ne m'y attendais pas, mais Shizune se met à sourire."


his "Donc, tu ne réfutes pas."


his "Alors ça n'a aucun sens. Pourquoi est-ce que tu voudrais faire une fête alors ?"

show shizu basic_normal
with charachange


ssh "J'essaye de passer au-dessus de tout ça. Et puis... Les fêtes d'adieu sont importantes. Les gens disent que le premier pas est le plus important, mais continuer d'avancer et s’arrêter proprement est tout aussi important, tu n'es pas d'accord ?"


his "C'est bien possible."

show shizu adjust_smug
with charachange


ssh "Bref, je ne considère pas ça comme un au revoir. Mais ça reste un événement. Tu dois passer par toutes les étapes."

show shizu behind_blank
with charachange

stop music fadeout 4.0


ssh "Tu ne vas pas le faire ?"


his "Faire quoi ?"

show shizu basic_normal
with charachange


ssh "M'embrasser, bien sûr."


his "C'est ça “les étapes ?”"

show shizu behind_blank
with charachange


ssh "Ça serait la chose normale à faire, non ?"


"C'est le moment d'agir. Si je n'agis pas, je suis sûr que mon cœur va exploser."

show shizu adjust_blush_close
with charachange


"Je l'embrasse immédiatement, tellement rapidement que je n'ai même pas le temps de l’apprécier. Même si elle était préparée pour ça, Shizune rougit vivement. J'ai l'impression que je réagis de la même façon."

play music music_one fadein 4.0

scene evh shizu_undressing_clothed_stare
with whiteout


"Je m'avance pour l'embrasser encore, mais alors que je fais ça, elle se recule au même moment et saute sur la table derrière elle. Seuls, dans le silence total, nous continuons de nous regarder l'un l'autre pendant un moment."

show evh shizu_undressing_clothed_kiss
with charachange


"Cette fois, je l'embrasse plus langoureusement. Ses lèvres sont fines et sèches, et légèrement entrouvertes. Je suis seulement capable d'apprécier la sensation pendant un moment avant que Shizune ne m'embrasse à son tour avec fougue."


"Sa mèche me passe devant les yeux tandis que je me laisse aller dans les méandres de son baiser. Je peux sentir la forme de son corps en dessous de ses vêtements, ce qui fait que je la serre encore plus."

show evh shizu_undressing_clothed_blush
with charachange


"Il nous faut tous les deux des efforts pour nous éloigner l'un de l'autre. Nous rougissons tous les deux, de par les baisers et les pensées qui sont venues avec, et je suis loin d’être celui qui respire le plus fort."


"Alors que Shizune commence à retirer ma cravate, je commence à défaire sa blouse. Il me faut un moment pour comprendre comment faire. Je n'avais jamais encore pensé à la façon dont se retirent les blouses de notre école avant."


"La blouse de Shizune est un peu serrée pour elle, et ses bras restent coincés un moment à cause de ça. Je tire dessus pour l'enlever, mais vu la façon dont elle gigote pour la retirer, ce n'est pas facile. C'est comique à voir."

play sound sfx_rustling

show evh shizu_undressing_unclothed_closed
with charachange


"Une fois que les bras de Shizune sont libres, elle retire son débardeur et ouvre sa jupe pour la laisser glisser le long de ses jambes. Les seules choses qu'elle porte encore sont son soutien-gorge et sa culotte."


"Son corps est curvé et ferme, et la couleur de sa peau fait contraste avec le noir de ses sous-vêtements. C'est vraiment beau à voir, surtout devant le fond illuminé par la lune."

show evh shizu_undressing_unclothed_blush
with charachange


"Elle regarde ma poitrine et enlève les boutons de ma chemise un par un. Elle est grandement ralentie alors que je passe mes mains sur ses cuisses. C'est un peu amusant de jouer comme ça avec elle."

show evh shizu_undressing_unclothed_kiss
with charachange


"Finalement, ma chemise tombe sur le sol. Shizune me surprend en m'embrassant rapidement sans me prévenir, mais je lui rends rapidement son baiser."

show evh shizu_undressing_unclothed_talk
with charachange


ssh "Pourquoi tu oses plus aujourd'hui que sur le toit ?"


ssh "Ou dans ta chambre ?"


"J'essaye de trouver une bonne réponse, mais ce n'est pas facile. Comment est-ce que je pourrais répondre à ça ? C'est pas possible, sauf si je venais à dire que faire de la paperasse me met d'humeur."


"Ma chemise ayant été enlevée, Shizune passe à ma ceinture, et je décide de l'aider à la défaire plutôt que de répondre à sa question. Je ne crois pas que ça serait une bonne idée de toute façon."

scene bg school_council_ni
with locationchange


"Ce n'est pas dur de l'enlever, et elle tombe sur le sol avec un bruit métallique. Je vais pour l'embrasser et commence à glisser ma main le long de sa hanche, mais elle s'avance soudainement en avant et me fait trébucher en arrière."


"Le bord de la table derrière moi ne me vient pas à l'esprit avant que je le sente cogner le bas de mon dos. Je n'avais pas remarqué que la table était là. Ça fait que je serre un peu plus fort Shizune et nous tombons tous les deux sur la table."

label fr_S35h:

show evh shizu_pushdown
with charachange


"Je retiens un soupir alors que Shizune se tient victorieuse au-dessus de moi. Elle a gagné encore une fois."


"Je suis distrait jusqu’à ce que le soutien-gorge de Shizune me tombe dessus, comme s'il était tombé du ciel. Je finis par rire, même si j'essaye de me retenir, et c'est suffisamment contagieux pour que Shizune rie aussi."


"Libérée du soutien-gorge, sa poitrine est plus grosse que je ne le pensais, même si elle était déjà remarquablement grosse sous sa chemise. Elle ramasse son soutien-gorge et le fait tomber au sol alors que mes mains passent sur son corps."


"Me chevauchant avec ses genoux sur la table, Shizune retire sa culotte, et mes mains se dirigent d’elles-mêmes vers ses hanches pour l'aider. J’aperçois ma montre. Ça ne fait que quelques minutes, mais ça me semble avoir duré bien plus longtemps."


"Elle se penche plus sur moi, de plus en plus proche jusqu’à ce que nos torses nus se touchent, sa poitrine me faisant une drôle de sensation en touchant la cicatrice de mon cœur."

window hide

show evh shizu_straddle_open
with whiteout

with Pause(7.0)

window show


"Quand Shizune s'assoit, je me sens glisser à l’intérieur d'elle, étant lentement enveloppé alors que sa poitrine se décolle de moi. Une attaque sur deux fronts. Je pense difficilement, étant donné la situation. Ça lui ressemble bien."

show evh shizu_straddle_tease
with charachange


ssh "Je devrais arrêter maintenant, et te laisser languir dans ton désir."


"Elle dit ça, et commence à remuer sur moi, me faisant fermer les yeux au plaisir soudain. Très drôle, Shizune. Je perds rapidement le fil de mes pensées."

show evh shizu_straddle_closed
with charachange

shi "…sss."


"Shizune se mord la lèvre alors que sa voix sort. Un son involontaire. C'est la première fois que je l'entends autant, et elle rougit en réalisant qu'elle l'a laissé sortir."


"Pour masquer ça, Shizune s'appuie plus sur moi, me faisant bouger, ce qui fait entrer mon érection encore plus profondément en elle."


"J’élève les hanches à la soudaine sensation de mouvement, et Shizune me combat, essayant de me replacer sur la table quand je lève les mains pour l'attraper."

show evh shizu_straddle_smile
with charachange


"À ce moment, ses hanches répondent avec une force encore plus grande."


"Le son des doux et restreints gémissements de Shizune et la vue de sa poitrine remuant à chaque fois que ses hanches se joignent aux miennes ne fait qu’accélérer l’inévitable, alors que le bruit de notre acte s’étend dans l’immobilité de la pièce."

shi "Mmphh…"

shi "…nn…"


"Je ne pourrai pas continuer longtemps. La sensation de plaisir que je ressens entre mes jambes, multipliée par la pression du poids de Shizune sur moi m’empêche de réfléchir. Mes hanches commencent à bouger toutes seules."


"La main de Shizune repousse la mienne sur la table. Chacun de ses gestes est une poussée."


"La table en dessous grince sous notre poids. Je doute qu'elle s'effondre, mais le bruit est vraiment quelque chose."

show evh shizu_straddle_come
with charachange


"Pas que Shizune le remarque. Son rythme n'en est que plus rapide, jusqu’à ce que j'aie l'impression qu'elle pourrait me faire passer à travers la table avec la force qu'elle y met. Sans un avertissement, ses mouvements arrivent à une accélération finale."

scene bg school_council_ni
with locationchange
with vpunch


"Soudainement, elle s’arrête, tombant presque sur moi avec tellement de vitesse que si elle ne s'était pas retenue, elle nous aurait sûrement assommés tous les deux. Ça aurait été vraiment le pire, si quelqu'un nous avait surpris ici tous les deux assommés."


"Je suis surpris, mais pas suffisamment pour oublier que nous sommes tous les deux nus et la soudaine interruption qui vient, à mon grand désespoir, d'arriver."


"Pourquoi est-ce que c'est arrivé ? Est-ce que c'était volontaire, pour me laisser languir dans mon désir ? Shizune laisse sortir un long souffle, réalisant cela en même temps que moi."

show shizu behind_blank_nak
with charaenter


ssh "Désolée, j'ai trébuché, ou glissé, ou quelque chose comme ça."


his "Je viens de penser, est-ce que la porte est verrouillée ?"

hide shizu
with charaexit



"Elle se lève rapidement de la table et s'y dirige pour vérifier, et la verrouille, la déverrouille, et la reverrouille, essayant de tourner la poignée pour s'assurer. Quand elle est enfin rassurée, elle fait un signe qui ne convient pas à la situation."

show shizu behind_smile_nak
with charaenter


ssh "Sécurisé !"


his "Je suis content que tu puisses le prendre aussi légèrement."

show shizu behind_frown_nak
with charachange


ssh "Je ne l'ai pas fait exprès. Pourquoi tu ne prends pas le dessus, alors ?"

show shizu behind_smilelow_nak
with charachange


ssh "Allez."

hide shizu
with charaexit


"J'attrape Shizune par les épaules et essaye de la mettre sur la table à ma place. Ses sourcils froncent de mécontentement alors que le bord de la table la cogne dans le dos, tout comme ça me l'a fait. Elle opte pour se mettre dessus d’elle-même."

scene evh shizu_table_smile
with dissolve


"C'est aussi la première fois que je vois Shizune allongée et nue. Le contour de sa poitrine et de son ventre est magnifique, et mes yeux continuent jusqu’à ses hanches généreuses. Une délicate forme de sablier."


"Je passe mes mains le long des formes de son corps, de ses épaules jusqu'en bas."


"Je m’insère lentement en Shizune en me tenant à elle. Une intense chaleur et étroitesse m'entoure immédiatement, et je commence à bouger en elle pour reprendre là où nous nous sommes arrêtés."


"Son corps me semble si chaud, lorsque ma peau le touche quand nos hanches se rejoignent à chaque poussée, et que nous nous tenons l'un l'autre. J'ai l'impression que je vais être brûlé par la chaleur de son corps."


"En plus de ça, je suis plus sensible maintenant qu'avant, et me retrouve à aller plus fort en Shizune pour compenser."

scene evh shizu_table_normal
with charachange


"Mes mains tiennent ses cuisses et je l’embête par la même occasion avec ma main, perdant presque l'équilibre quand elle réagit vivement, poussant fortement son corps contre moi, nous faisant presque tomber tous les deux."


"Montant mes mains sur son corps, j'attrape ses seins généreux et les palpe comme j'ai toujours voulu faire. Ils me semblent encore plus gros au toucher qu'à la vue et débordent de mes mains, doux et parfaitement formés."


"Elle se tortille alors que je passe mes doigts sur ses tétons, et elle passe ses bras autour des miens, me tenant les doigts et m'attirant plus proche d'elle. J'ai l'impression de faire du catch avec elle, la prise est imparable."


"Depuis la première fois où nous avons joint nos mains, nous sommes connectés."


"Que ce soit quand elle m'a tiré par la main à un événement du conseil des étudiants, ou quand elle me l'a tenue en tant que ma petite copine, je crois que c'est la même confiance qui passe dans la façon dont elle me prend la main."


"Elle s'agrippe comme elle le peut à la surface de la table et croise ses jambes dans mon dos, nous serrant encore plus l'un contre l'autre, nous connectant encore plus et m'emprisonnant à l’intérieur d'elle."

show evh shizu_table_comeopen
with charachange


"L’intérieur est si chaud et étroit, et avec la façon dont elle me force en elle, le frottement ne fait qu’accélérer, me faisant atteindre ma limite."

show evh shizu_table_comeclosed
with whiteout

stop music fadeout 4.0


"Bien trop tôt, la sensation s’arrête. Tout ce que je peux faire après ça est rester en elle avec les mains tenant la table, à la fois par manque d’énergie et aussi parce que ses jambes me retiennent toujours. Quant à Shizune, elle sourit presque rêveuse."


"La voir comme ça me fait sourire également. Ses jambes s'abaissent lentement, me permettant de me retirer."

label fr_S35x:

scene bg school_council_ni
with locationchange


"Épuisé, je m'adosse à un bureau et essaye de reprendre mon souffle avant de remettre mes vêtements."


"Je remarque une palpitation sourde dans ma poitrine alors que je reboutonne ma chemise. Ça donne un mauvais arrière-goût à tout ce qui vient de se passer."

show shizu behind_smile_nak
with charaenter


ssh "Heureusement que Misha n'a pas pu être là, hein ?"


his "Tu plaisantes beaucoup je trouve aujourd'hui."


his "Je me demande ce qu'elle avait à faire."

show shizu behind_blank_nak
with charachange


"Shizune fend l'air paresseusement du doigt et pointe la porte."


ssh "Va voir toi-même."


his "Pourquoi tu ne me le dis pas juste ?"

show shizu behind_smile_nak
with charachange


ssh "C'est plus intéressant si tu le vois toi-même. Voir c'est croire."


his "Bien sûr. C'est malin. Peut-être que je vais faire ça. Et toi, tu vas rester là toute la journée ? Il se fait tard."

show shizu behind_blank_nak
with charachange


ssh "J'ai l'impression que c'est mon dernier jour en tant que présidente du Conseil des Étudiants, donc peut-être que je vais rester là ce soir. C'est peut-être la dernière chance que j'aurais de dormir à mon bureau, après une longue journée."


his "C'est bizarre."


his "Je vais dormir dans mon lit."


ssh "Dormir assis est un talent. Très pratique."


his "Bien sûr."

scene bg school_lobby_ni
with locationchange


"Pendant un moment j'envisage d'aller voir ce que fait Misha, juste parce que Shizune a rendu ça secret, comme si elle construisait une machine à remonter le temps ou un truc du genre. Mais en fin de compte, je décide de ne pas le faire."




label fr_S36:

scene bg school_courtyard_ni
with locationskip


"L'air de la nuit est agréable à ce moment de l'année. C'est rafraîchissant et un peu humide, mais pas assez frisquet pour rendre désagréable le fait d’être dehors. Il n'est cependant pas assez tard pour que la cour soit vide."


"Après que Shizune et moi nous soyons dit au revoir, je pars pour retourner au dortoir. Je n'ai même pas le temps d'y arriver avant d’être distrait."


"Ça ne semble pas être une mauvaise idée d'aller voir ce que fait Misha. Je n'ai rien de mieux à faire. Pas de devoirs. Je n'ai rien de bien à lire. En plus de ça, j'ai envie de savoir."

scene bg school_lobby_ni
with locationchange


"Ce n'est pas la première fois que je suis dans le bâtiment principal après les heures de cours, mais généralement, c'est alors que je pars avec Shizune et Misha après une longue journée au Conseil des Étudiants. Pas en y entrant tout seul."


"L’atmosphère est silencieuse, un mot que je n'utiliserais pas normalement pour décrire ces halls. C'est un peu flippant. Une lumière clignote un peu plus loin. C'est comme dans un film d'horreur quand on attend que quelque chose arrive."

play sound sfx_rustling
with vpunch


"Sentant une main sur mon épaule, je me raidis instinctivement."


"Ce n'est pas Misha, sinon j'aurais des mains devant les yeux et un “devine qui c'est” avec. Donc, qui c'est ? J’espère que ce n'est pas Kenji, ou qu'au moins c'est quelqu'un que je connais, ou ça prendrait une drôle de tournure."

show shizu invis_close at tworight
with None

show shizu behind_blank_close_ni at center
with dissolvecharamove

play music music_happiness fadein 4.0


"Qui que ce soit, il se met rapidement devant mes yeux. C'est Shizune."


hi "Qu'est ce que tu fais là ?"


"Je suis soulagé d'avoir oublié de le signer."

show shizu adjust_frown_close_ni
with charachange


"Shizune met un doigt devant ses lèvres, j'imagine que même si elle ne peut pas m'entendre, elle peut dire d’après mon expression que j'étais bruyant. Et apparemment, ce n'est pas la chose à faire."


"Mais alors, pourquoi est-ce que Misha est son interprète ?"


his "Oh, très drôle. Pourquoi tu es là ?"

show shizu basic_normal_close_ni
with charachange


ssh "J'attendais que tu viennes voir. Je savais que tu viendrais. Ça a pris un moment, cela dit."


his "Tu as attendu ici ?"

show shizu behind_blank_close_ni
with charachange


ssh "Oui, mais ce n'est pas important. On doit être discrets, si on ne veut pas que Misha nous découvre. Dis-moi si je ne suis pas assez discrète, d'accord ?"

show shizu basic_normal_close_ni
with charachange


"Sur ce, Shizune commence à avancer sur la pointe des pieds au milieu du hall. Je lui tapote l'épaule pour avoir son attention."


his "Ce n'est pas discret du tout."


his "Pourquoi est-ce qu'on doit être discrets ?"

show shizu behind_frustrated_close_ni
with charachange


"Elle refuse de répondre, probablement parce que signer et marcher discrètement au même moment ne semble pas facile."

scene bg school_hallway3_ni
with locationskip


"Avant que je le sache, nous sommes devant notre classe."

stop music fadeout 0.5
play sound sfx_snap
with vpunch


"Soudainement, un son comme un claquement de fouet fend l'air, suivi par un grognement de frustration familier."


"Je suis sûr qu'un son comme ça n'est pas bon pour mon cœur. Sans mentionner que tout semble un million de fois plus bruyant quand c'est silencieux comme ça. Ça vient de l'intérieur de la classe, et je m'avance jusqu’à Shizune pour voir à l’intérieur."

scene ev misha_nightclass:
    center
    xpos 0.4
show ovl misha_nightclass_aperture at left
with silentwhiteout

play music music_comedy fadein 0.5


mu "Est-ce que tu peux arrêter de jeter ton stylo, s'il te plaît ? Et comment c'est possible de jeter un stylo aussi bruyamment ?"


ssh "Il a l'air très énervé."


"Je comprends pourquoi. Je sympathise avec Mutou. J'ai été capable d'entendre le stylo de Misha fendre le mur du son à travers un mur et une épaisse porte de classe. Ça lui a probablement percé un de ses tympans et laissé une marque dans le mur."

show ev misha_nightclass:
    ease 1.0 xpos 0.23 xanchor 0.0
show ovl misha_nightclass_aperture:
    ease 1.0 right
with None


mi "Je ne le jette pas~, quand je suis nerveuse, j'aime faire tourner mon stylo, mais~, j'oublie après que je le tiens, et—"


mu "Ça n'a aucune importance, dans tous les cas, il ne devrait pas y avoir de stylo qui vole. J'en ai assez durant les heures d'école normales, je n'ai pas besoin de ça après."


mi "O-oui~ ! Désolée."


mu "Peu importe, arrête de lancer, ou lâcher, ou faire tomber des choses, s'il te plaît. Les professeurs doivent travailler, aussi."

scene bg school_hallway3_ni
show shizu behind_blank_close_ni at center
with locationchange


"Je remarque que Shizune regarde la même scène que moi. Mutou crie à pleins poumons, et Misha est Misha."


"Je peux les entendre assez bien à travers la porte. Mais Shizune ne peut évidemment rien entendre du tout. Je me demande ce qu'elle comprend."


"Elle doit savoir, vu qu'elle comprend suffisamment pour vouloir que je le voie aussi, mais je me demande si elle a l'impression de manquer des choses des fois, en ayant à faire tant d'efforts pour comprendre ce qu'elle voit."

show shizu basic_normal_close_ni
with charachange


ssh "On dirait qu'elle prend des cours supplémentaires. C'est le cas ?"


his "Ouais."


"Je lui réponds, même si je sais que la question est complètement rhétorique."

show shizu behind_smile_close_ni
with charachange


ssh "Misha m'a dit qu'elle voulait être un professeur de langue des signes plus tard. Si elle peut avoir une recommandation, elle pourra étudier outre-mer. C'est pour ça qu'elle travaille autant. Elle a toujours des notes assez moyennes."


his "Maintenant je me sens coupable. Je ne sais toujours pas ce que je vais faire moi."

show shizu adjust_smug_close_ni
with charachange


ssh "Et moi non plus !"


"La façon joyeuse dont elle signe ça ne lui ressemble pas, et c'est bien évidemment faux."

show shizu basic_normal2_close_ni
with charachange


ssh "Partons, il ne faut pas qu'on nous voie. Ça serait gênant si on nous trouve en train de nous tenir ici comme des idiots."


his "Où ça ? Dans la salle du conseil ?"

show shizu adjust_happy_close_ni
with charachange

stop music fadeout 3.0

show shizu invis_close at tworight
with dissolvecharamove


"Secouant la tête, elle se glisse dans la classe de l'autre côté du couloir."

scene bg school_room34_ni
with locationchange


his "Super cachette."

show shizu behind_blank_ni at center
with charaenter


ssh "Tu es plus sarcastique que d'habitude récemment. Et que la porte soit fermée est une bonne chose. Bref, c'était intéressant, non ?"


his "Oui, mais je ne suis pas vraiment surpris."

play sound sfx_doorclose


show shizu adjust_smug_ni at Position(ypos=1.1)
with dissolvecharamove


"Je ferme la porte derrière nous, incitant Shizune à rire silencieusement alors qu'elle s'assoit sur une chaise. Pendant une seconde, ça me déprime. J'ai envie d'entendre son vrai rire."

show shizu behind_smile_ni
with charachange

play music music_innocence fadein 10.0


ssh "Moi je l'ai été. Je regardais Misha de haut, je ne pensais pas du tout qu'elle avait un but. Mais il s’avère que j'avais tort, j'ai fait une présomption sans preuve. J'ai cru que Misha était comme moi sur ce point. J'étais idiote. J'ai perdu."

show shizu basic_normal_close_ni
with charachange


"Shizune s’arrête pour se craquer les doigts, et met ses mains l'une sur l'autre avant de s'avancer sur sa chaise. Dans l'étrange silence du bâtiment, je peux entendre Mutou crier sur Misha à travers un couloir et deux portes."


"Les yeux de Shizune fixent les miens, ne clignant pas des yeux à travers ses lunettes, observant ma réaction à sa remarque."


"C'est un test. Son opinion des gens est rarement faite d'après la façon dont ils répondent aux questions, c'est la façon dont ils répondent aux affirmations qui comptent."


"En y pensant, c'est logique. L'incapacité de Shizune à parler, tout comme sa personnalité en général font que tout ce qu'elle “dit” est un grand engagement de sa part. Tout."


"Pour cette raison, je doute parfois qu'elle dise quoi que ce soit si elle n'a pas prévu quelque chose derrière."


"Ça fait vraiment paranoïaque. Même Kenji le penserait. Je suis tellement perdu dans mes pensées que j'oublie de lui répondre. Elle prend ça comme un manque de réponse. Il y avait un temps limite de réponse plus court que d'habitude."

show shizu adjust_smug_close_ni
with charachange


ssh "Comme je pensais."


his "Comment ça ?"

show shizu behind_blank_close_ni
with charachange


ssh "Tu n'es pas d'accord ?"


his "Pas vraiment, c'est pas ça. Je ne comprends pas."

show shizu basic_normal2_close_ni
with charachange


ssh "Je veux forcer les gens à faire ce que je veux."


"Quelle honnêteté rafraîchissante."

show shizu behind_frown_close_ni
with charachange


ssh "Ne me regarde pas bizarrement comme ça. Ce n'est pas comme si c'était toujours mon intention."

show shizu basic_normal_close_ni
with charachange


ssh "Au début, je m'ennuyais juste. Je voulais voir quelqu'un ayant de la passion pour quelque chose. Et qu’après je puisse essayer de le battre. Je voulais tester ses capacités ou ses convictions."

show shizu adjust_frown_close_ni
with charachange


ssh "Mais c'est impossible, personne n'a de passion pour quoi que ce soit dans cette école. Ils gardent juste ça pour eux."

show shizu behind_frustrated_close_ni
with charachange


ssh "Je n'arrive pas à y croire. C'est trop ennuyeux comme ça. Je ne pensais pas que des gens aussi ennuyeux pouvaient exister. Ça va bien plus loin que l'idée de ne pas vouloir faire de vagues."

show shizu adjust_angry_close_ni
with charachange


ssh "Ils devaient avoir des passions. Ils devaient cacher quelque chose. Je voulais savoir quoi, le révéler, et leur extirper."

show shizu behind_blank_close_ni
with charachange


ssh "Une des façons les plus simples pour que les gens s'ouvrent à toi, et pour les réconforter, c'est de leur dire quelque chose sur toi. Et là tu pourras plus facilement leur faire raconter des choses sur eux."

show shizu adjust_happy_close_ni
with charachange


ssh "C'est du donnant donnant, mais avec un élément de manipulation, ce qui rend les choses intéressantes."

show shizu behind_blank_close_ni
with charachange


ssh "Je ne peux pas faire ça. Si je demandais à Misha de parler pour moi, ça me rendrait arrogante. Le message est obligé de passer par un messager. Je suis à côté de Misha, lui demandant de dire quelque chose sur moi."

show shizu adjust_frown_close_ni
with charachange


ssh "Tu n'as pas à être capable de lire la langue des signes pour comprendre ça. Si j'étais forcée de voir ça, je penserais que je suis arrogante aussi."

show shizu basic_angry_close_ni
with charachange


ssh "J'étais frustrée, je n'arrivais pas à trouver un moyen d'avoir une conversation avec qui que ce soit d'autre que Misha. Personne ne s'ouvrait à moi."

show shizu behind_frown_close_ni
with charachange


ssh "J'en suis arrivée à la conclusion que je ne peux pas faire en sorte que les gens se confient à moi, ou me fassent confiance."


ssh "Je peux seulement créer des choses, les montrer aux gens, et espérer les rendre heureux. Ou je pourrais être plus insistante et espérer que quelqu'un finisse par accrocher."


"J'imagine que ça, c'est moi. C'est un peu déprimant."

show shizu basic_normal_close_ni
with charachange


ssh "Au milieu de tout ça, je crois que j'ai commencé à ignorer Misha, ou à la voir moins comme une personne, ou quelque chose comme ça. J'ai considéré que je n'avais plus à m'occuper de Misha. C'était comme si elle était juste une extension de moi-même."

show shizu behind_sad_close_ni
with charachange


ssh "J'ai oublié que pendant tout ce temps, Misha était là, s'ouvrant à moi, et se donnant à cent pour cent chaque jour."

show shizu basic_angry_close_ni at center
with Dissolvemove(0.7)


ssh "J'ai perdu de vue ce que je cherchais, parce que c'était juste devant moi. Vraiment stupide de ma part. Je suis vraiment devenue arrogante. C'est pour ça que j'ai perdu. J'ai une vision plus étroite qu'au début. J'ai régressé."


"Elle bouge d'avant en arrière maintenant, broyant presque du noir, et pourtant tellement remplie d'énergie qu'elle ne peut pas s’empêcher de bouger."


"Si on la reliait avec deux fils électriques, je suis sûr que Shizune pourrait alimenter une lampe. C'est bizarre que je puisse avoir une pensée aussi légère alors qu'elle est si sérieuse."

show shizu adjust_frown_close_ni
with charachange


ssh "Et malgré ça, Misha me dit que je suis son inspiration. Ce n'est pas ridicule ? Je ne suis pas le genre de personne qui peut inspirer les autres."

show shizu behind_blank_close_ni
with charachange


ssh "Même si quelqu'un qui vous inspire a des faiblesses, ça peut être acceptable. J'y ai pensé. Il y a même une hypocrisie acceptable."

show shizu basic_normal2_close_ni
with charachange


ssh "Par exemple... Si ton héros est un athlète, mais qu'il n'était pas quelqu'un d’agréable, tu pourrais toujours le respecter pour ses capacités athlétiques, même s'il n'est pas parfait."

play sound sfx_snap
show shizu adjust_angry_close_ni
with charachange


ssh "Cependant,"


"Elle claque des doigts brusquement. Ça résonne comme un éclair dans la salle vide, et Shizune prend quelques secondes pour s'étirer les doigts. En y pensant, c'est la première fois qu'elle signe autant."

show shizu cross_angry_close_ni
with charachange


ssh "Si quelqu'un comme moi n'a pas de but, c'est totalement inacceptable. Ça serait la pire forme d'hypocrisie. Et les hypocrites ne méritent pas d'avoir une quelconque responsabilité, ils ne peuvent même pas s'occuper d’eux-mêmes."


"C'est vraiment très pessimiste. Ça m’énerve d'y penser."


"Je me détestais il y a quelques mois. Je devais ressembler à ça pour les autres."


"Et, c'est drôle, c'est Shizune et Misha qui m'ont convaincu d’arrêter. Sans elles, je suis sûr que les choses auraient été bien différentes, et pas pour le mieux."


"Récemment, j'ai l'impression qu'on a partagé nos malheurs autant qu'on s'est supportés les uns les autres, mais je crois que c'est un ensemble qui vient avec le fait d'avoir des amis et d’être proche de quelqu'un."


his "Tu es la chef de toute façon."

show shizu behind_frown_close_ni
with charachange


ssh "Seulement parce que personne d'autre ne veut l’être."


his "Mais tu l'es quand même, vu que les gens continuent de te faire confiance. En fait, ça ne rend pas ça encore plus important ?"


his "Dans tous les cas, tu es la chef, tu es un personnage qui inspire. Tu es responsable de ce que tu apprivoises."


his "J'ai lu ça dans un livre quelque part."

show shizu basic_normal_close_ni
with charachange


ssh "C'est intelligent."


"Shizune semble seulement afficher des émotions sur son visage quand elle le veut, mais je ne crois pas qu'elle soit sarcastique."

show shizu adjust_frown_close_ni
with charachange


ssh "Je ne veux pas “apprivoiser” qui que ce soit, cela dit."


his "Être la chef et qu'on te regarde avec admiration alors. C'est pareil."

show shizu behind_frustrated_close_ni
with charachange


ssh "Je n'ai jamais voulu être chef, ça c'est juste fini comme ça."


his "Je ne crois pas, tout ce que tu essayes de faire est d'avoir de plus en plus de responsabilités."

show shizu adjust_frown_close_ni
with charachange


ssh "Attends, attends. Je n'allais pas te dire que je n’appréciais pas ça. Je me moque d’être la chef, mais ça ne me gêne pas. Je me moque d’être la meilleure, mais ça ne me gêne pas. Tu as raison, cela dit, sur le fait que je veuille des responsabilités."

show shizu basic_happy_close_ni
with charachange


ssh "Bien sûr je veux plus de responsabilités. Avoir des responsabilités me fait me sentir en vie. C'est pour ça que j'ai rejoint le Conseil des Étudiants : S'il n'y avait pas de pression, je ne pourrais pas le supporter."

show shizu behind_blank_close_ni
with charachange


ssh "Quand bien même, maintenant je suis la chef. J'ai toujours pensé qu’être la chef voulait dire que tu donnais des ordres, mais ça représente bien plus."

show shizu adjust_frown_close_ni
with charachange


ssh "Ça représente le fait d'avoir un but. Si je n'ai pas de but, alors ça ne sert à rien. Les gens me suivraient juste pour mon propre amusement. Ça serait égoïste."


"C'est un point de vue étrangement moral pour quelqu'un qui semble tant aimer le fait d’être toujours devant les gens."

show shizu basic_normal2_close_ni
with charachange


"Posant son menton sur ses mains, Shizune semble vraiment enfantine à ce moment alors qu'elle réfléchit à son problème. L'expression qu'elle a sur le visage est un peu comique, parce qu'elle est facile à lire, et donc ça ne lui ressemble pas."


his "Ça vient avec le job. Je crois qu'il faut que tu sois la chef. Tu ne serais pas satisfaite avec quoi que ce soit d'autre, tu t’ennuierais juste."

show shizu basic_frown_close_ni
with charachange


"Shizune ne répond pas, mais d’après son expression agacée, je crois avoir raison."


his "Je crois que j'ai besoin d’être dirigé, aussi."

show shizu adjust_happy_close_ni
with charachange


ssh "Est-ce qu'on t'a dit que c'est important pour contribuer à la société ?"


"Quelle réponse étrange. C'est tellement sorti de nulle part que je ne sais pas comment répondre. Et ça m’embête, même si je ne sais pas pourquoi. Peut-être parce que ça ne semble pas être quelque chose qu'elle dirait."


"Alors je commence à penser que ce n'est pas la pensée de Shizune. Je me demande qui lui a dit ça. Bah, sûrement son père. Mais il y a une chance qu'elle ait pensé à ça toute seule. Si c'est le cas, est-ce parce qu'elle ne peut pas entendre ?"


his "Pourquoi est-ce que tu dis ça ?"

show shizu behind_blank_close_ni
with charachange


ssh "Juste comme ça."


his "Je ne te crois pas."


his "Mais je crois que c'est vrai, cela dit."

show shizu basic_normal_close_ni
with charachange


ssh "Je vois."

show shizu adjust_frown_close_ni
with charachange


ssh "Je ne sais pas si c'est pareil pour moi. Je déteste ça."


"Je crois que tout le monde a besoin d'un but. En y pensant, c'est logique que Shizune n'en ait pas un. Sinon toute son énergie aurait été dirigée vers quelque chose."


"Vu qu'elle n'a rien vers quoi la canaliser, Shizune la laisse partir dans tous les sens. Ça me rappelle une ligne électrique tombée durant un orage. Sauvage et incandescente, mais sans but et dangereuse. Tout comme Shizune."


"J'ai envie de dire que c'est pour ça qu'elle ressent le besoin de tout transformer en compétition, mais... c'est probablement juste parce qu'elle est comme ça. Avoir un but dans lequel canaliser son énergie est juste l'étape suivante."

show shizu behind_blank_close_ni
with charachange


ssh "Envisage ça : Je pourrais faire des affaires. Ma famille a des bonnes connexions, ça ne devrait pas être trop dur. ...Dit comme ça, je semblerais presque sans éthique et opportuniste, hein ?"


his "Un peu."

show shizu adjust_frown_close_ni
with charachange


ssh "Je ne m’arrêterai pas, cela dit. Je travaillerai dur, jusqu’à ce que je sois au sommet."


ssh "Quand j'aurai autant d'argent que possible, tellement que je ne saurai pas quoi en faire, je passerai à l'étape suivante. Après m’être assise dessus un moment, bien sûr. Comme un dragon dans les contes."


his "Tu veux être... ?"

show shizu basic_happy_close_ni
with charachange


ssh "Une philanthrope !"

hi "…"

show shizu adjust_smug_close_ni
with charachange


ssh "Tss tss. Qu'est-ce que tu croyais ? Que je voulais être une pingre ?"

show shizu behind_blank_close_ni
with charachange


ssh "Bon, c'est vrai, c'est une partie du plan. Ne pense pas que ça va s’arrêter là, hein."

stop music fadeout 8.0


"Shizune semble encore mal à l'aise. Bien sûr, même si elle a semblé surmonter son problème rapidement, personne ne peut chasser ses anxiétés aussi vite. Personne ne peut résoudre ses problèmes aussi facilement."


"Ce qui est important est qu'elle semble vouloir y mettre du cœur. C'est toujours difficile de dire si cette motivation qui lui vient est une bonne ou une mauvaise chose."


"Mais elle a quelque chose auquel elle peut se raccrocher maintenant. Je peux en être sûr. Je suis content pour elle. Et en même temps, un peu triste. Je suis celui qui est derrière. Maintenant, je suis le seul restant sans but."

$ suppress_window_after_timeskip = True

scene black
with dissolve



label fr_S37:

window hide None
nvl clear

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_daily fadein 0.5

scene bg school_dormhisao_bw
with dissolve

nvl show dissolve


n "\n\n\n\n\n\n\n\n\nIl n'y a pas eu d'autres événements depuis cette semaine-là."

nvl clear


n "\nBien sûr, c'est ce que je pensais la semaine avant ça. Et le fait que Shizune et Misha se soient soudainement réconciliées me rend quelque peu envieux et perdu. Je pensais qu'il ne serait pas possible que je puisse rester calme face à ça."


n "Mais heureusement, ça ne m'a pas tant gêné que ça. Et avant que je le sache, il y avait déjà suffisamment à faire à l'école pour que je réussisse à me sortir ça de la tête. Et encore une fois, tout allait bien."


n "J'avais tort. J'ai vu les vulnérabilités précieusement cachées de Shizune et Misha, mais elles sont toujours fortes."


n "Et maintenant, on sera bientôt diplômés. Je suis devenu tellement à l'aise ici que ça m'a perturbé. Je me suis senti triste et ne voulais pas y penser. Alors je ne l'ai pas fait, pas jusqu’à récemment."


n "Il y a à peu près une semaine, j'ai commencé à faire une liste des gens à qui je devrais dire au revoir avant de partir. La première règle que je me suis fixée est que je ne les écrirais pas dans un ordre précis, comme du moins important au plus important."


n "Et pourtant, j'ai fini par faire comme ça aussi malgré moi, même si ça s'est avéré être une liste plus courte que ce à quoi je m'attendais. Kenji est quelque part au milieu."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

scene bg school_dormhisao
show kenji neutral at center
with locationchange

window show


ke "Ils ont dit que je devrais bien finir l'école un jour. Et bah, je leur ai montré. J'ai été logé ici gratuitement pendant assez longtemps. Si tu prends en compte la hausse des prix de l'immobilier, je crois que je peux dire que je suis gagnant en fin de compte."

show kenji happy
with charachange


ke "Non, tu sais quoi ? J'ai gagné. L'histoire se portera garante de ma victoire."


hi "Victoire de quoi ?"


ke "J'ai réussi à garder profil bas, et j'ai exploité les failles. J'ai battu le système."


hi "Dit comme ça, on dirait surtout que tu as couru pour fuir le système."


ke "Quelquefois, courir est la plus grande forme de victoire ; comme aux Jeux Olympiques."


"Je suis trop fatigué pour débattre avec lui. De qui il se moque ? Et puis tout le monde sait que le lancer de poids est la meilleure épreuve des Jeux Olympiques."


hi "Donc, ce que tu dis est que ça ne va pas te manquer ?"

show kenji neutral
with charachange


ke "De quoi ?"


hi "L'école, bêta."

show kenji tsun
with charachange


ke "Non. Je te l'ai dit, il y a trop de féministes ici. Il n'y a plus rien à faire. Mais au moins je serai capable de partir avant que ça n'atteigne une masse critique. Je ne reviendrai que dans plusieurs années, quand ils auront fait une statue en mon honneur."


hi "Ils font ces réunions de “dix ans plus tard”, ici ?"

show kenji neutral
with charachange


ke "Comment tu veux que je sache ça ? Probablement. Bref, je dois commencer à faire mes valises. Prends soin de toi, mec."


hi "T'aurais dû commencer il y a une semaine, comme moi."


"Pas que j'aie eu grand-chose à ranger de toute façon."

show kenji tsun
with charachange


ke "C'est pas comme ça que t'es censé faire. Tu es censé tout faire à la dernière minute."


ke "Les hommes sont doués pour tout faire à la dernière minute, la dernière minute peut être plus productive que, genre, la semaine entière avant ça. C'est une façon d'équilibrer les niveaux."

show kenji neutral
with charachange


ke "Pffft, tu ne comprendras jamais nos façons de faire viriles."


hi "Prends soin de toi aussi."

show kenji happy
with charachange

show kenji invis at right
with dissolvecharamove

play sound sfx_doorslam

hide kenji
with vpunch


"Après un salut, il rentre à reculons dans sa chambre et claque la porte assez fort pour que le dortoir entier l'entende. J'ai remarqué que beaucoup de personnes claquaient les portes ici. C'est peut-être un truc local."


"“Prends soin de toi.” C'est la première fois que je l'entends dire ça. Généralement nos conversations se finissaient sur “à plus” ou “j'te rembourserai plus tard, mec.” Il était un peu énervant parfois, mais il me manquera. Je le raye de ma liste mentale."


"La liste est très réduite maintenant, et encore une fois je m'interdis de faire selon un certain ordre. Comme je l'ai déjà dit, je n'ai jamais eu cette intention."

scene bg school_dormhallway
with locationchange


"Donc, je pars à la recherche de Shizune et Misha. Je ne peux penser qu'à un seul endroit où elles pourraient être. Le bureau du conseil des étudiants, bien sûr."

play ambient sfx_crowd_indoors fadein 2.0

scene bg school_lobby
show crowd
with locationskip


"Tournant dans un couloir, je manque de rentrer dans un petit groupe d'étudiants. Pendant une seconde, un petit frisson me traverse le corps, car pour ce que j'en sais, cet événement aurait pu m’être fatal."


"C'est le nouveau Conseil des Étudiants. Ils ne sont pas beaucoup, mais bien plus que trois. Ce qui est bien, vu que ça veut dire qu'il y en a assez pour que chacun ait son propre titre."


"Ça aurait été cool si j'avais pu avoir une petite plaque sur un bureau avec mon nom et mon titre inscrits dessus. Je ne crois pas qu'ils fassent encore ça aujourd'hui. Ou qu'ils l'aient fait tout court même."


"Le nouveau Conseil des Étudiants m'entoure pendant que je réfléchis. Si quelqu'un venait à voir ça, il trouverait ça sûrement sinistre."


"Peut-être qu'ils sont venus pour enfin se venger pour toutes les fois où je les ai appelés “le nouveau Conseil des Étudiants”. Je traduisais juste pour Shizune, mais peut-être que j'aurais dû faire preuve de plus de tact. Je ne regrette rien."


"Je me retrouve à être remercié pour “tout ce que j'ai fait”."


"On me remercie. Ça devrait me faire plaisir, vu à quel point j'ai pu penser qu'être dans le Conseil des Étudiants était un travail ingrat. Ça devrait me faire plaisir, mais je ne peux pas complètement apprécier."

$ renpy.music.set_volume(0.5, 1.0, channel="music")
$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

window hide
nvl clear
nvl show dissolve


n "\n\nJe me demande comment les choses se seraient passées si le Conseil des Étudiants s'était avéré aussi grand que celui qui va nous remplacer."


n "Même s'ils n'ont que seulement deux ou trois autres membres, c'est suffisant pour qu'ils aient attribué des rôles. Pas comme nous, où Shizune semblait être présidente, mais c'était un peu tout."


n "Que le nouveau conseil me remercie, me donne une drôle d'impression. C'est comme revenir à la maison et voir qu'un arbre dont tu t'étais occupé il y a des années a maintenant grandi. Mais j'ai l'impression de ne pas m'en être suffisamment occupé. Je me demande ce que j'aurais pu faire de plus."


n "Ça rendrait sûrement Shizune furieuse que je me sente distant de ce que j'ai fait dans le Conseil des Étudiants, ou que je puisse insinuer que je n'en ai pas fait assez, mais c'est vrai. Je n'ai fait que la suivre."


n "\nDonc, d'une façon, j'ai aussi l'impression de voir l'arbre, mais de loin. Comme si je le voyais de la fenêtre d'un train en mouvement."

$ renpy.music.set_volume(1.0, 1.0, channel="music")
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")
stop music fadeout 4.0

nvl hide dissolve
nvl clear
window show


"J'ai réfléchi trop longtemps. Quand j'émerge enfin, je réalise que je suis encore là, entouré par le nouveau Conseil des Étudiants. Je fais la seule chose que je peux faire, m'excuser pour n'avoir pas été attentif, et les remercie à mon tour."

stop ambient fadeout 0.5

scene bg school_council
with locationchange

play music music_normal fadein 3.0


"Quand ils s'en vont, j'entre dans le bureau du conseil des étudiants qui héberge un véritable bazar, mais semble avoir gagné un ordinateur."





"C'est logique. Je me rappelle qu'une des filles a dit qu'elle prévoyait d'utiliser un ordinateur pour rentrer toutes les données ennuyantes de Shizune."


"Je ne me rappelle pas laquelle a dit ça, cela dit. Aoi semble être la plus ambitieuse, mais aussi Keiko est plus sérieuse. Bah, c'est plus important maintenant."


"Je ne suis pas seul dans la pièce, mais au lieu de trouver Shizune comme je m'y attendais, c'est juste Misha. Elle est assise sur le bureau de Shizune, comme le fait souvent Shizune, balançant les jambes d'avant en arrière."

show mishashort invis:
    center
    ypos 1.2
with None

show mishashort hips_grin at center
with Dissolvemove(0.5)


"Quand nos yeux se rencontrent, elle saute du bureau et fait inexplicablement une pose de super héros."


mi "Salut, Hicchan~ ! Je suis surprise de te voir ici~ !"


hi "Qu'est-ce que tu fais ?"

show mishashort cross_smile
with charachange


mi "Toi d'abord~."


hi "Je cherchais Shizune."

show mishashort cross_grin
with charachange


mi "Moi, aussi~ ! Je pensais qu'elle serait là, mais j'ai eu Hicchan à la place~ !"


hi "Ah bah merci."

show mishashort sign_smile
with charachange


mi "Wahaha ! C'est~ bien aussi ! Vraiment, vraiment~. Je voulais te parler aussi de toute façon~."


hi "À quel propos ?"


"Je prends un moment pour regarder dans la salle. Je vois un réchaud. Elles s'installent vraiment."

show mishashort perky_sad
with charachange


mi "Je voulais te dire désolée~, bien sûr~, pour tout ce que je vous ai fait subir, à Shicchan et à toi."


hi "Ne dis pas qu'on a “subi”."

show mishashort sign_confused
with charachange


mi "D'accord~, d'accord~."


hi "Ne t'excuse pas auprès de Shizune."

show mishashort hips_smile
with charachange


mi "Ahaha~. D'accord~, d'accord~. Mais je ne suis pas là pour ça, Hicchan. Je ne m'excuserai pas auprès de Shicchan. Puisque tu es là, je veux te poser une question."

show mishashort perky_confused
with charachange


mi "Hicchan, qu'est-ce qui pourrait rendre Shicchan heureuse à ton avis ?"


hi "La domination mondiale, évidemment."

show mishashort cross_laugh
with charachange


mi "Wahaha~ !"

show mishashort hips_smile
with charachange


mi "Même si tu plaisantes, Hicchan~... Non, même si elle y arrivait, ça ne rendrait pas Shicchan heureuse. Seulement pour un petit moment."

show mishashort sign_smile
with charachange


mi "Hicchan, tu as déjà entendu parler de ces artistes qui déchirent leurs peintures dès qu'ils ont fini de les faire ? Il existe des personnes comme ça dans le monde, tu sais~ !"

show mishashort perky_smile
with charachange


mi "Je m'en rappelle tout d'un coup. C'est comme Shicchan, maintenant que j'y pense. À chaque fois que Shicchan défie quelqu'un et réussit, elle agit comme si ses compétences n'avaient plus aucun intérêt après."

show mishashort perky_confused
with charachange


mi "Je me demande~, est-ce que c'est parce qu'elle ne peut pas créer quelque chose de permanent ?"

show mishashort perky_sad
with charachange


mi "C'est tout comme ces artistes qui veulent créer une pièce qu'ils laisseront derrière eux~, une vraiment bien~, mais ne peuvent pas le faire."


mi "C'est vraiment évident quand j'y repense maintenant~, mais je ne l'avais pas vu auparavant. Maintenant, je suis effrayée. Je me demande si Shicchan sera heureuse un jour."


hi "Non, je ne crois pas. Pas au sujet d’être heureuse. Je crois que tu as tort. Shizune est heureuse plus souvent que je ne le croyais."


hi "Je crois que c'est assez impressionnant. D'habitude, les gens ne pensent pas à des choses comme ça jusqu’à ce qu'ils soient d'âge moyen ou mourants. Des choses comme “je veux laisser quelque chose derrière moi”"


"Comme moi."


"J'ai pris un peu d'avance. Ma vie était courte, et semblait encore plus courte quand j'ai eu ma crise cardiaque."


"Je ne pensais pas à ce que je laissais derrière moi, parce que je me suis rapidement rendu compte que je ne laissais presque rien. Tout ce qui me restait était le fait de ruminer ma propre aigreur."


hi "Shizune veut déjà laisser sa marque quelque part. Mais elle veut le faire en aidant les gens. C'est pour ça que les célébrations sont si importantes pour elle. Elle veut même être une philanthrope."


hi "Je crois que c'est la meilleure façon de vivre, que de vivre de ce que tu donnes aux autres. Même si c'est pour une raison égoïste, c'est bon aussi."


hi "Shizune est déjà heureuse, parce que si les choses se passent bien, alors il y aura toujours quelqu'un d'autre pour le voir et s'en rappeler. C'est ce qui la rend heureuse."


"Misha soupire, les bras tendus, semblant taper l'air du bout du doigt."

show mishashort sign_sad
with charachange


mi "Avant je pensais encore... mh~... que je pourrais être capable de rendre Shizune heureuse ; et j'avais une bonne position pour faire ça. Vu que j'étais son interprète, je pouvais être pour toujours avec elle. Peut-être..."

show mishashort perky_confused
with charachange


mi "Et~, j'ai pensé que ce serait comme devenir... l'ombre de Shicchan."

show mishashort perky_sad
with charachange


mi "J'ai continué d'essayer même si elle me rejetait. J'avais l'impression d’être coincée et de ne rien pouvoir faire de plus que regarder Shicchan s'éloigner de plus en plus de moi. J'étais effrayée, même si j'aurais du juste me résigner."


mi "C'est difficile. peut-être que j'aurais au moins pu comprendre Shicchan~."

show mishashort cross_smile
with charachange


mi "Mais on dirait que j'avais complètement tort après tout~... Je ne savais même pas ça, et ne le comprenais pas non plus... Shicchan appellerait ça une défaite totale."

show mishashort cross_frown
with charachange


mi "D'accord~, j'ai fini. C'est tout, Hicchan~. Mais~ ! Vu que tu es celui qui connaît le mieux Shicchan, tu ne peux pas la faire pleurer. Ou je serai en colère~ !"

show mishashort hips_smile
with charachange


mi "Je vais partir outre-mer après ça. J'ai même des lettres de recommandation, sinon je ne pourrais pas faire ça, normalement~ ! Peut-être que j'étudierai et deviendrai un professeur de langue des signes là-bas ? Qui sait~ !"

show mishashort hips_grin
with charachange


mi "Ça veut dire~ ! Que tu dois veiller sur Shicchan, d'accord ?"

stop music fadeout 8.0


"Le sourire de Misha est aussi honnête qu'il l'a toujours été, mais il est évident qu'elle a changé. Son regard est celui d'une fille bien plus attentive. On dirait que c'est vrai que le malheur apporte la sagesse. Ça me rappelle le regard de Shizune."


"Je me demande ce qu'a dû vivre Shizune pour devenir ce qu'elle est. Je peux deviner. Ou peut-être qu'elle a toujours été comme ça. J'ai envie de la voir encore plus, et suggère à Misha qu'on devrait la chercher ensemble."


"Bien sûr, c'est juste un prétexte pour passer plus de temps avec une amie. C'est bizarre que j'ai autant l'impression que ça fait longtemps qu'on n'a pas été ensemble, ensevelis sous le travail et la routine du conseil des étudiants."


"Penser au futur peut donner une fausse image du passé."


"En parlant d'images..."

scene bg school_courtyard at bgleft
show yuuko neutral_up at center
with locationskip

play music music_ease fadein 8.0


"À l'extérieur, Yuuko se tient là, tenant dans les mains un petit appareil photo. Je ne l'aurais pas remarqué s'il n'avait pas réfléchi la lumière du soleil. Misha appelle Yuuko. Je croyais qu'on était supposés chercher Shizune."

show yuuko neutral_up at tworight
show bg school_courtyard at center
with charamove

show mishashort hips_grin at twoleft
with charaenter


mi "Salut~ salut~ !"

show mishashort cross_smile
with charachange


mi "Qu'est-ce que tu fais~ ?"

show yuuko closedhappy_down
with charachange


yu "Je prends juste des photos de tout le monde."

show mishashort hips_grin
with charachange


mi "C'est évident~ !"


"Bizarre. Misha, je n'oublierai jamais que tu m'as appris que quelqu'un peut avoir autant de secrets et pourtant avoir un énorme manque de tact."


hi "Où est ma photo ?"

show yuuko worried_up
with charachange


yu "T-tu veux un exemplaire ? Je... ne sais pas. Eh bien... Seulement si tu promets de garder ça secret, sinon tout le monde en voudra une aussi."

show mishashort cross_smile
with charachange


mi "Ça m'est arrivé en primaire, sauf que c'était des bonbons à la place~ !"

show yuuko smile_up
with charachange


yu "D'accord... Je vais prendre une photo de toi alors..."


hi "Ah, attends, je ne suis pas prêt. Je plaisantais juste."

show mishashort sign_smile
with charachange


mi "Hicchan, fais un signe de paix~ !"



hi "Je ne vais pas faire ça."

play sound sfx_camera
with cameraflash


"Le flash de l'appareil photo s'active, m'aveuglant."

show mishashort perky_confused
show yuuko worried_down
with charachange


"Yuuko laisse sortir un gémissement de frustration. On n'est pas censés utiliser le flash à l'extérieur."

show yuuko invis at right
with dissolvecharamove


"Elle commence à s'excuser même si elle n'a pas de raison de le faire, et s'éloigne discrètement."


hi "Ah, attends."

show yuuko worried_up at tworight
with dissolvecharamove


yu "Oui ?"

show mishashort sign_smile
with charachange


mi "Tu as vu Shicchan par ici~ ?"

show yuuko neutral_up
with charachange


yu "Oui... Devant le portail."


hi "Merci."


"J'ai à peine le temps de finir de la remercier avant d'avoir à suivre Misha."

play ambient sfx_crowd_outdoors fadein 3.0

scene bg school_gate
show crowd at center
show shizu behind_blank at center
with locationskip


"Heureusement, pas pour très longtemps. La porte est à peine à une minute de marche d'ici, meme si ça peut suffire pour être fatigant pour moi, parfois. On voit Shizune avec le Conseil des Étudiants, ils la remercient probablement aussi."

$ renpy.music.set_volume(0.3, 1.0, channel="ambient")

show shizu adjust_frown
with charachange

hide crowd
with charaexit


"Aussitôt qu'elle les voit, elle leur fait signe de s'en aller. Ce qui est très facile, vu que je pense qu'aucun d'entre eux ne comprend la langue des signes, donc ils ne pestent pas avant de partir."


"Ce qui m’amène à me demander pourquoi ils la remercient si personne ne peut lui signer, mais c'est l'intention qui compte."

show mishashort invis at twoleft behind shizu
with None

show mishashort hips_grin:
    xpos 0.36
show shizu adjust_blush
with Dissolvemove(0.4)

show bg school_gate at bgright
show mishashort perky_smile at twoleft
show shizu behind_smile at tworight
with dissolvecharamove


"Misha se jette immédiatement dans les bras de Shizune et s'adosse au portail, à côté d'elle. D'un autre côté, je décide de rester un peu éloigné, de les laisser parler. Après tout, Misha voulait parler à Shizune pendant tout ce temps. Je peux attendre."

show bg school_gate at right
show shizu invis:
    xpos 0.4
show mishashort invis:
    xpos 0.0
with dissolvecharamove


"Je tourne même le dos, pour ne pas pouvoir “espionner” leur conversation."


"Je finis par perdre la notion du temps."


"Quand je regarde ma montre, ça fait déjà dix minutes. Je me demande si elles ont fini, et me tourne pour les voir juste derrière moi."

show bg school_gate at bgright
show mishashort perky_smile at twoleft
show shizu behind_blank at tworight
with dissolvecharamove


ssh "À quoi tu penses ?"


hi "À des trucs philosophiques ennuyeux dont je n'ai pas envie de parler. Ne t’inquiète pas, je ne réfléchis pas trop non plus."

show shizu adjust_smug
with charachange


ssh "Bien. Devenir tout philosophe à un moment comme ça serait la pire chose à faire."


hi "Ouais. Je veux juste rester là un moment. C'est relaxant."

show mishashort hips_grin
with charachange


mi "Wahaha~ ! Ce fut~ une semaine bien remplie."


hi "Pas vraiment, pas pour moi."

$ renpy.music.set_volume(0.5, 1.0, channel="music")
$ renpy.music.set_volume(0.1, 1.0, channel="ambient")

window hide
nvl clear
nvl show dissolve


n "\n\n\n\nJe sais qu'elles ont dû être occupées. Mais je crois que je sais ce que je veux faire maintenant, et quand je m'en suis rendu compte, je ne me suis pas particulièrement senti excité ou anxieux."


n "C'est l'opposé. Je me sens en paix pour la première fois depuis longtemps, et je veux savourer ce sentiment un peu plus longtemps."


n "\nJe crois que je veux enseigner ici."


n "\nAussitôt que j'y ai pensé, une longue route s'est ouverte dans mon esprit. Une route incertaine, qui m'a reconduit ici."

nvl clear


n "\n\n\n\nJe me demande si je rencontrerai quelqu'un comme moi dans le futur. Quelqu'un rempli d'aigreur."


n "Je veux parler à cette personne, vu que je ne peux pas me parler à moi-même. Je veux lui dire que la vie est trop courte, quelque chose qui ne pouvait pas m’être dit, seulement montré. Je veux le faire sans aucune pitié."


n "Si j'avais été pris en pitié, je suis sûr que je serais seulement mort un peu plus. Quand je pense à la première semaine, je pense encore à quel point ça s'est bien passé. Tellement bien que ça ne peut être appelé que le résultat de la gentillesse. Je ressens l'envie de montrer la même gentillesse à d'autres."


n "\nEt j'ai aussi envie de continuer de poursuivre Shizune."

$ renpy.music.set_volume(1.0, 1.0, channel="music")
$ renpy.music.set_volume(0.3, 1.0, channel="ambient")

nvl hide dissolve
nvl clear

show mishashort perky_smile
with charachange

window show


mi "Qu'est-ce que voulait le nouveau Conseil des Étudiants, Shicchan~ ?"


"C'est difficile de rêvasser quand on entend la voix de Misha."


hi "Je ne savais pas qu'ils avaient quelqu'un qui comprenait la langue des signes."

show shizu behind_smile
with charachange


ssh "Ils n'en ont pas. Je crois que c'était sûrement juste un au revoir, alors j'ai apprécié, même si je n'ai pas pu leur dire."

show shizu basic_normal
with charachange


ssh "Comment est-ce que vous avez su que j'étais ici ?"


hi "C'est censé être un secret ? Dans tous les cas, on a juste demandé à Yuuko. Elle a pris une photo de toi aussi ?"

show shizu behind_blank
with charachange


ssh "Oui, sans me demander. Vu qu'il est rare que Yuuko fasse quelque chose de spontané, je l'ai laissé faire."

play sound sfx_snap
show shizu basic_sparkle
with charachange


"Elle claque des doigts, plus parce que je crois qu'elle aime ça qu'en concrétisation de quelque chose."

show shizu behind_smile
with charachange


ssh "On devrait prendre une photo à trois."

show shizu adjust_happy
with charachange


ssh "On n'a pas encore pris de photos en tant que conseil des étudiants. C'est l'occasion parfaite."

show shizu basic_normal
with charachange


ssh "Mais, si je regarde cette photo dans un an, je ne veux pas que les gens sur la photo me fixent juste du regard."


mi "Mh~ ? Qu'est-ce que ça veut dire, Shicchan ?"

show shizu adjust_frown
with charachange


ssh "Les photos sont censées capturer le moment, non ? Sans aucun doute. Elles ne sont pas des portraits. Juste être debout comme ça serait trop sérieux. Ça ne capturerait pas fidèlement ce que je ressens."

show shizu behind_smile
with charachange


ssh "J'ai le sentiment qu'on se reverra. Donc, ce n'est pas l'occasion de prendre une photo sérieuse. Ça devrait plus être une photo “à plus tard” ; rien d'important. Ça devrait être plus... festif."


hi "Oh non..."

show shizu basic_happy
with charachange


ssh "Comme ça. Suivez mon exemple."

show shizu adjust_smug
with charachange

show shizu behind_smile
with charachange


"Shizune prend une pose comme un mousquetaire, tellement brièvement que je suis sûr que même elle, sait que c'est bête."

show mishashort cross_laugh
with charachange


mi "Ahahaha~ !"


hi "Est-ce qu'on doit vraiment prendre... une pose aussi flashy ?"

show shizu adjust_happy
with charachange


ssh "Je peux en trouver une meilleure. Misha, vas chercher Yuuko !"

show mishashort sign_smile
with charachange


mi "Je n'aime pas cette pose non plus, mais c'est une bonne idée~."


hi "Ça veut rien dire."

show mishashort invis:
    xpos 0.0
with dissolvecharamove


"Elle est déjà partie, et revient en traînant Yuuko avec elle."

show yuuko invis:
    center
    xpos -0.2
with None

show bg school_gate at left
show shizu behind_smile_close:
    xpos 0.83
show mishashort hips_grin at center
show yuuko neutral_up at left
with dissolvecharamove


"Le flash est désactivé. Une LED rouge clignote trois fois après que Yuuko ait pressé le bouton. Shizune nous regarde tous les deux pour s'assurer qu'on fait comme il faut. Synchronisation des montres. On saute."

play sound sfx_camera
$ renpy.music.set_volume(0.0, 0.5, channel="ambient")

scene ev shizu_goodend
with cameraflashlong


ssh "Je suis sûre qu'elle sera excellente."


ssh "D'accord, ..."


mi "Maintenant, faisons-en une avec Yuuko, aussi~ !"


yu "N-non, s'il vous plaît..."


hi "Ce n'est pas nécessaire."


"Je veux un exemplaire de cette photo aussi."

show ev shizu_goodend_pan
with None


"Je mourrai sûrement plus jeune que la plupart des gens. Ma vie peut s'interrompre à n'importe quel moment. Je n'ai pas de temps à perdre alors. Je veux vivre autant que possible. Je veux aussi voir les gens sourire de ce que j'ai accompli."


"Vivre par procuration à travers le bonheur des autres ne semble pas si horrible. Ressentir la joie via le bonheur de quelqu'un d'autre. C'est la façon la plus facile que je connaisse d’expérimenter ma vie, et de lui donner un sens."


"Peut-être que c'est le sens que Shizune a trouvé pour elle-même, bien que ce soit juste ma théorie. Les gens se retrouvent souvent seuls dans leurs vies, et sans orientation."


"Cependant, les gens peuvent se réfugier dans des moments de bonheur. Ces moments qui parsèment la vie de quelqu'un comme les arrêts de trains sur une carte. Ou des souvenirs sur un long chemin."


"Ces moments seuls, en y pensant, peuvent donner un sens à la vie de quelqu'un. Chaque ami, festival, rencontre et séparation."


"Je veux être capable de demander à Shizune un jour si j'ai raison. Je veux passer le temps que j'ai avec elle. Et enfin, je veux que Shizune sourie pour elle."

$ renpy.music.set_volume(0.3, 1.0, channel="ambient")

scene bg school_gate at left

show mishashort perky_smile at twoleft 
show shizu behind_smile_close at tworight 


with locationchange


hi "Je t'aime."


"Je m’arrête, me demandant si elle va me regarder, confuse, et vouloir savoir pourquoi je dis ça au milieu de nulle part. Elle ne le fait pas."



hi "Ils font une réunion des anciens élèves ici ?"

show shizu adjust_happy_close
with charachange


ssh "Bien sûr que oui."

show mishashort sign_smile
with charachange


mi "Un membre du Conseil des Étudiants devrait savoir ça~ !"

show shizu behind_smile_close
with charachange


ssh "Je veux vous revoir plus tôt que ça, compris ?"

show shizu adjust_happy_close
with charachange


ssh "Et ça vaut pour tous les deux."

show mishashort hips_grin
with charachange


mi "D'accord~ !"


hi "Ouais."

show shizu basic_happy_close
with charachange


ssh "Yuuko ! Fais la pose aussi !"

show shizu adjust_happy_close
with charachange


ssh "Après ça, on pourra aller boire le thé."


"Shizune rit, comme si elle se moquait de tout ce qui pouvait se passer dans le monde entier, et le rire de Misha se joint au sien aussi facilement que s'il s'agissait de son propre rire. On se reverra."

stop ambient fadeout 2.0
stop music fadeout 2.0







label fr_S38:

play music music_pearly

scene bg school_scienceroom
with locationchange


"Le jour suivant, Misha est de retour en classe, bien qu'elle ait toujours l'air plutôt morne. Non pas que je m'attendais à ce qu'elle aille magiquement mieux, ça aurait été impossible étant donné ce qui s'est passé."


"Cette fois, c'est Shizune qui n'est pas là. Au début, je ris presque du fait que quand ce n'est pas l'une qui est absente, c'est l'autre. Mais en y pensant, il n'y a rien de drôle. En fait, j'ai du mal à me concentrer sur mon travail à cause de ça."


"Elle est peut-être juste malade. Ou elle sèche juste les cours. Mais ça pourrait aussi être quelque chose de plus sérieux, et je suis tenté de demander à Misha si elle sait, mais je ne fais rien en fin de compte."


"Je ne regrette pas de m'être imposé hier, effrayé que Misha fasse quelque chose d'irréfléchi."

play sound sfx_normalbell


"Mais maintenant, j'ai l'impression que je devrais lui laisser un peu d'espace. Finalement, la sonnerie retentit, et Misha se lève pour aller manger comme tout le monde. Je décide de déjeuner dans une classe vide aujourd'hui... mais pas celle-là."

scene bg school_hallway3
with locationchange


"Malheureusement, beaucoup d'autres étudiants semblent avoir la même idée, donc il n'y a pas beaucoup de classes vides. Au bout d'un moment, alors que je suis en train d'abandonner l'idée, j'en trouve une dans le noir au bout du couloir."

scene bg school_miyagi
show lilly back_surprise:
    center
    ypos 1.15
with locationchange


"Allumant la lumière, je me rends compte que celle-là n'est pas vide non plus. La tête de Lilly est tournée dans ma direction, ce qui me fait peur avant que je réalise qu'elle m'a probablement entendu activer l'interrupteur."

show lilly basic_listen
with charachange


li "Bonjour."


hi "Salut Lilly. Je ne pensais pas qu'il y aurait quelqu'un ici."

show lilly basic_weaksmile
with charachange


li "C'est toi, Hisao ?"


hi "Ouais, mais tu le savais probablement déjà."


"Je me tourne pour partir, et Lilly élève rapidement la voix."

show lilly basic_smile
with charachange


li "Tu n'as pas à partir aussi vite. On peut déjeuner dans la même pièce. Et en fait, je préférerais déjeuner avec quelqu'un."


"Je suis sur le point de lui demander comment elle savait que j'allais manger, mais je me retiens. C'est juste du bon sens, et je ne veux pas sembler trop facilement impressionnable."

show lilly basic_smile_close:
    center
    ypos 1.1
with characlose


"Je m'assieds au bureau devant elle, après avoir retourné ma chaise pour lui faire face. J'ai entendu dire que notre esprit appréhende les choses qu'on voit selon la façon dont on les a déjà vues auparavant, ou en fonction de ce à quoi on s'attend."


"Surtout pour l'économie de ne pas avoir à calculer tout ce qu'on voit."


"Lilly ne semble jamais s’arrêter de se questionner sur ce qu'elle entend. Donc, je me demande, est-ce que c'est parce que son esprit remplit les blancs à sa place ? Ou est-ce qu'elle se contente juste d'accepter les choses comme elles arrivent ?"


"Sur son bureau se trouvent quelques cookies et un thermos de thé. Elle doit être du genre à prendre des déjeuners légers. Je mords dans mon sandwich. Certains des ingrédients ressortent de l'autre côté."

show lilly basic_ara_close
with charachange


li "On n'a pas parlé depuis longtemps, je suis surprise que tu te rappelles toujours mon nom."


hi "Mmphffmm ?"

show lilly basic_smileclosed_close
with charachange


li "Tu dois être très occupé dans le Conseil des Étudiants."


hi "C'est différent chaque semaine. Il y a certaines semaines plutôt lentes, et certaines autres où j'envisage de me faire porter pâle."


"Attends Lilly, j'ai besoin d'une seconde pour reprendre mon souffle pendant que je mange."

show lilly basic_smile_close
with charachange


li "Et c'est comment récemment ?"


hi "Imprévisible."

play sound sfx_snap

show lilly basic_oops_close
with vpunch


"Je claque les doigts, ce qui, d’après son expression faciale, l'agace beaucoup."

show lilly basic_reminisce_close
with charachange


li "Je crois que tu fréquentes trop deux filles en particulier."


hi "Il est vrai que c'est une des marques de fabrique de Shizune. Personnellement, je l'apprécie."

show lilly basic_displeased_close
with charachange


li "Et moi je l'ignore."


"Son ton ne change absolument pas, mais l'humeur de Lilly s'est évidemment détériorée."


hi "Ça ne semble pas facile. Je me demande depuis un moment comment elle fait pour le faire aussi bruyamment, mais je crois que je me fais mal aux phalanges."

show lilly behind_displeased_close
with charachange


li "Même si c'était suffisamment fort pour briser la vitre, je l'ignorerais. Je ne suis pas un animal de foire. J'ai ce luxe."


hi "Tu es encore en colère pour ça ?"


"Je lui pose la question aussi précautionneusement et diplomatiquement que possible, bien qu'en fin de compte je demande juste pour satisfaire ma curiosité."

show lilly basic_weaksmile_close
with charachange


li "Non, bien sûr que non, bien que je n'aime pas Shizune."

show lilly basic_reminisce_close
with charachange


li "On a été ensemble dans le Conseil des Étudiants pendant un bref moment."


hi "C'est ce que j'ai entendu."

show lilly basic_sleepy_close
with charachange


li "J'aurais aimé que tu ne sois pas si rapide à les rejoindre."

show lilly basic_listen_close
with charachange


li "Je n'aime pas la façon dont Shizune dirige le Conseil des Étudiants. Tu savais qu'elle a fait fuir la plupart des anciens membres ? C'est pour ça que je crois qu'elle essaye de s'entourer de personnes qui ne lui opposeront aucune résistance."

show lilly basic_reminisce_close
with charachange


li "Et ils ne le font pas. C'est comme un cercle de dépendance."


"Je suis sûr que Shizune est consciente de ce que dit Lilly. Après tout, je me rappelle qu'elle l'a spécifiquement nié plusieurs fois, ce que j'ai trouvé étrange."


"On dit que plus on est précis à propos d'un déni et plus il est probable que les allégations soient vraies. Dans ce cas, je crois que je ne suis pas d'accord. Shizune est la seule dont l'opinion ne peut pas être considérée comme totalement objective."


hi "Tu lui as dit tout ça ?"

show lilly basic_displeased_close
with charachange


li "Très souvent."


"Lilly s'arrête pour finir le fond de sa tasse. Il me reste peu de temps pour finir mon repas et j'en profite pour manger autant que possible durant cette brève pause."

show lilly basic_sleepy_close
with charachange


li "Tous ses amis sont liés au Conseil des Étudiants, comme Misha."


li "J'ai entendu que les choses étaient sensibles entre Misha et elle. Elles se sont disputées ?"


hi "Pas véritablement."

show lilly basic_surprised_close
with charachange


li "Vraiment ?"

show lilly basic_reminisce_close
with charachange


li "Dans tous les cas, il n'y a aucun intérêt à essayer de les réconcilier. Shizune essaye toujours de se confronter aux choses de face, mais ça ne marche pas dans le monde réel. C'est juste être têtu et non pas brave ou plein de bonnes intentions."


hi "C'est un avis un peu général, tu ne trouves pas ?"

show lilly basic_smileclosed_close
with charachange


li "Mh, c'est possible."

show lilly basic_weaksmile_close
with charachange


li "Qu'est-ce qui te semble le mieux avec du thé ? Des cookies, ou des cakes ? J'aime les deux, mais différemment. Je ne pourrais pas choisir."

show lilly basic_displeased_close
with charachange


li "Je n'aime pas les gens qui me forcent constamment à choisir et veulent tout transformer en compétition."


li "Quand j'ai rejoint le Conseil des Étudiants, je pensais que ça signifierait seulement contribuer à ce que les choses se déroulent correctement et aider les gens, comme le fait une déléguée de classe."

show lilly basic_reminisce_close
with charachange


li "À la place, chaque jour consistait à voir Shizune patrouiller partout, utilisant Misha comme un mégaphone, disant à quel point on devait surpasser l'ancien Conseil des Étudiants, et faire de plus en plus d’événements, et les faire de plus en plus grands."


hi "Mais vous voulez la même chose en fin de compte. Toutes ces choses rendent ça intéressant. En fait, ce n'est pas une histoire d'ego. Les gens aiment les feux d'artifice, les stands de nouilles, les pommes d'amour, et s'habiller autrement."


hi "Plus le Conseil des Étudiants en fait, et plus l'école nous donne de responsabilités. Ça signifie plus de travail, mais d'un autre côté, ça signifie aussi plus de liberté."


hi "Si tu as le pouvoir de faire des choses comme t'occuper de l'organisation d'un festival, ils penseront que tu es suffisamment compétent pour le gérer au lieu de le rejeter instantanément."


hi "Bref, j'ai envie de ça, moi aussi. Ça a sa part de travail sans intérêt, mais il y a des moments qui font que ça vaut le coup. Ça me donne quelque chose à faire. Si j'avais juste l'école, je crois que j'exploserais."


show lilly basic_weaksmile_close
with charachange


li "Je crois que Yamaku est bien plus décontractée que les autres écoles."


"Yamaku n'est pas comme les autres écoles, après tout."


"Je commence à divaguer vers une autre mentalité familière. D'une certaine façon, c'est presque trop décontracté."


"Et si j'étais quelqu'un d'autre, je suis sûr que je trouverais étouffant que ce soit aussi décontracté, bien que dans une autre école, que ce soit aussi décontracté serait considéré comme normal."


"Mais ici, le calme serait presque malvenu. Je me sentirais différent, parce que je ne suis pas quelqu'un de normal, après tout."


"Je m'en rappellerais chaque fois que j'entendrais mon sang battre dans mes tempes. Je me sentirais cloîtré et faible, et mon aigreur ne ferait que grandir."


hi "Ouais, bien sûr."


hi "Le fait est que je crois que je comprends le pourquoi de tout ça. Tu rends vraiment les choses difficiles pour Shizune."

show lilly basic_sleepy_close
with charachange


li "C'est bien possible, mais quand il s'agit de traiter les gens individuellement, elle ne le fait pas très bien."


"Malheureusement, je peux difficilement réfuter ça."

show lilly basic_smile_close
with charachange


li "Tu as l'heure ? J'aimerais aller en classe dix minutes avant la sonnerie."


hi "Alors tu es pile à l'heure si tu pars maintenant."

show lilly invis_close at center
with dissolvecharamove

stop music fadeout 4.0


"S'excusant, Lilly part, et je reste assis, écoutant le cliquetis de sa canne sur le sol s'évanouir dans le murmure des autres étudiants qui discutent dans les classes et le couloir."


"Je me sens épuisé, et j'ai complètement oublié que je voulais parler à Shizune aujourd'hui."

scene black
with dissolve




label fr_S39:

scene bg school_hallway3
with locationchange


"Après les cours le jour suivant, je me dirige immédiatement vers la salle du conseil des étudiants pour parler à Shizune."


"Même si elle est en classe, essayer d'attirer son attention et d'avoir une conversation avec elle près de la porte ou dans le couloir risque d’être un peu compliqué."

scene bg school_lobby
with locationchange


"Je ferais mieux d'essayer de la trouver dans la salle du conseil des étudiants. Je prends mon temps pour aller jusque là-bas, m'achetant un jus de fruit à un distributeur en chemin."


"Je réfléchis aussi déjà à ce que je veux lui dire. Ce n'est rien de vraiment important, seulement quelques questions à propos des événements à venir."

scene bg school_council
with locationchange

play music music_rain fadein 8.0


"La porte est déverrouillée quand j'arrive. Je penserais que la salle est vide si je ne pouvais pas voir le sac de Shizune sur son bureau, et le haut de sa tête dépasser derrière celui-ci. On dirait qu'elle s'est construit un petit château fort."

show shizu basic_normal at center
with charaenter


"Shizune fait un signe derrière son sac avant de le ramasser d'un doigt et de le mettre hors du chemin."


"Mais après ça, elle retourne tapoter son stylo sur le bureau et fixe une liste du regard comme si elle contenait le sens de la vie."

show shizu adjust_frown
with charachange


ssh "Qu'est-ce que tu veux ?"


his "Je voulais savoir si je pouvais aider à quoi que ce soit. Comme pour tous ces trucs là-bas, c'est quoi ?"


"Je pointe une pile de dossiers derrière elle, mais elle secoue la main pour me dissuader."

show shizu behind_blank
with charachange


ssh "Je peux gérer ça toute seule."


his "Alors et pour les élections ?"


his "Et aussi, où est Misha ?"

show shizu behind_sad
with charachange

shi "…"

show shizu basic_normal2
with charachange


ssh "Ça se passe bien. Et j'ai dit à Misha que j'allais tout gérer toute seule."


his "Pourquoi ?"


"Shizune fait tourner lentement son stylo dans sa main, faisant attention à chaque doigt, comme une aiguille dans un vêtement."

show shizu behind_blank
with charachange


ssh "Sans raison."


his "Vraiment ?"

show shizu adjust_frown
with charachange


ssh "Sans raison."


"Elle se répète pour accentuer ce qu'elle vient de dire, pour que j'abandonne l'idée qu'il puisse y avoir quelque chose derrière ça. Mais il y a quelque chose, elle n'agit vraiment pas normalement."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve


n "\n\n\n\n“Pourquoi t'es aussi silencieuse là-dessus ?” est la phrase qui m'arrive immédiatement à l'esprit, même si ce n'est pas le moment pour faire de l'humour. Ça décrit bien ce que je ressens. On ne peut pas communiquer normalement, alors j'apprécie le peu de façons qu'on a. Et être rejeté comme ça fait mal."


n "Mais il est évident que quelles que soient ses raisons, ça va être assez difficile de parler à Shizune aujourd'hui. Et au-delà du fait qu'elle soit têtue, elle semble déprimée, mais vu la façon dont tourne la conversation, je ne vois pas comment je vais pouvoir trouver ce qui la déprime."


n "\nD'une certaine façon, ça ne me donne qu'encore plus envie de savoir. Et ça veut dire que je dois demander à Misha. Le problème est que je ne sais pas vraiment où va Misha durant son temps libre."

$ renpy.music.set_volume(1.0, 1.0, channel="music")
stop music fadeout 3.0

nvl hide dissolve
nvl clear

scene bg school_lobby
with shorttimeskip

window show


"Après avoir demandé à beaucoup de personnes si elles avaient vu une fille avec des cheveux rose fluo, et avoir eu beaucoup de réponses négatives, je trouve enfin quelques personnes l'ayant vue."

scene bg school_cafeteria
show mishashort perky_smile at center
with locationchange

play music music_moonlight fadein 8.0


"Au moment où j'arrive à la cafétéria, là où Misha était apparemment durant tout ce temps, j'ai déjà fait deux fois le tour de l'école et suis très fatigué. Je réalise que j'étais déjà passé devant elle, mais ne l'avais pas vue à cause d'un pilier."


hi "Pourquoi est-ce que tu es plus douée pour me trouver que je le suis pour te trouver ?"

show mishashort hips_smile
with charachange


mi "Tu me cherchais, Hicchan ?"

show mishashort hips_grin
with charachange


mi "Mh~... Qui sait~ ? Je crois que c'est juste une coïncidence."


hi "Tu sais, le principe des coïncidences c'est qu'elles ne sont pas constantes."

show mishashort cross_laugh
with charachange

mi "Hahaha~."


hi "Tu prends un déjeuner en retard ?"

show mishashort sign_smile
with charachange


mi "Je n'ai pas pu manger durant le déjeuner, alors ouais~ ! Mais~, pas trop, pour que je puisse quand même dîner après."

show mishashort perky_smile
with charachange


mi "Tu voulais me parler de quelque chose, Hicchan ?"


"Je ne perds pas de temps."


hi "Ouais. La raison de ma présence c'est que... Tu as remarqué que Shizune était de mauvaise humeur aujourd'hui ?"

show mishashort perky_confused
with charachange


mi "Je voulais te demander la même chose, Hicchan~."

show mishashort perky_sad
with charachange


mi "Enfin~, sauf qu'elle est comme ça depuis plusieurs jours déjà."


hi "Je vois."

show mishashort sign_confused
with charachange


mi "Hicchan, tu crois que c'est à cause de quelque chose que j'ai fait ? Tu crois que j'ai énervé Shicchan, comme la dernière fois ?"


hi "Non. Elle semble plus en colère contre moi de toute façon."


"Je ne mens pas, vraiment. Malheureusement, mes tentatives pour la rassurer ne semblent pas si bien marcher. À sa façon, Misha est assez têtue, aussi."

scene bg school_dormhisao_ss
with locationskip


"Finalement, je retourne à mon dortoir. Les derniers jours n'ont été qu'une suite d’événements frustrants et ça m'épuise. Je me sens assez fatigué pour décider d'aller faire une sieste, espérant que je trouverais une façon de résoudre tout ça."

stop music fadeout 3.0

window hide

scene black
with shuteye

with Pause(1.0)
with shorttimeskip
with Pause(1.0)

scene bg school_dormhisao_ni
with openeye

window show

play music music_night fadein 1.0


"Quand je me réveille, je me sens mieux, mais toujours pas clair sur la conduite à tenir. La seule chose qui a changé est qu'il fait noir dehors."


"En ouvrant un peu la fenêtre, je peux dire qu'il fait toujours bon. Après avoir avalé sans eau mes pilules du soir, je fais une petite marche jusqu'aux distributeurs."

scene bg school_lobby_ni
with locationskip


"Ils n'ont pas ce que je prendrais normalement, alors je frappe au hasard et quelque chose tombe."

scene bg school_courtyard_ni
with locationchange


"Les lumières sont éteintes dans le bâtiment principal, ce qui inclut la salle du conseil des étudiants."

play sound sfx_rustling


"Alors que je pense tout seul, j’entends quelque chose bouger derrière moi. J'ai déjà vu ce film auparavant, et c'est un son très effrayant à entendre, seul dans la nuit."

show kenji happy_ni at center
with charaenter


"Heureusement, c'est Kenji, qui sort des buissons avec son humeur joviale habituelle."


ke "Salut."


hi "Mais c'est pas vrai ! Ça t'arrive souvent d’apparaître devant les gens comme ça la nuit en disant “salut” comme si de rien n'était ?"

show kenji neutral_ni
with charachange


ke "Non, ça serait bizarre. Je savais que ça serait toi. J'ai une extrêmement bonne vision nocturne. Peut-être parce que je suis un surhomme."


hi "Qu'est-ce que tu fais là, alors ?"

show kenji tsun_ni
with charachange


ke "Je pourrais te demander la même chose. Qu'est-ce que TU fais là ?"


"J'envisage de lui dire la vérité, mais me ravise rapidement. Ça prendrait trop longtemps de lui expliquer."


hi "J'hurle à la lune."

show kenji neutral_ni
with charachange


ke "Je fais ça aussi, des fois. Mais il n'y a pas de lune ce soir, cela dit."


"Je l'écoute à peine, me sentant un peu agacé de cette interruption."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve


n "\n\nJ'ai menti, langue déliée, que tout allait bien. Ou mains déliées, pour être exact. Et au même moment, j'avais une tout autre conversation avec Misha."


n "Cette conversation pourrait énerver Shizune, ce qui est compréhensible. Mais il n'est pas possible qu'elle ait pu m'entendre. Même les mains de Misha, qui d'habitude signent tout ce qu'elle pense, étaient immobiles. Même si ça n’avait pas été le cas, je me tenais devant elle, bloquant la vue de Shizune."


n "La seule façon pour que Shizune ait pu comprendre la conversation est qu'elle sache lire sur les lèvres. C'est sûrement la première chose que j'ai demandée en étudiant la langue des signes, juste par curiosité. Ce n'est pas facile, non plus parfait... alors je n'y avais jamais pensé jusqu’à maintenant."


n "\nÇa serait logique, et le taux d'erreur de lecture quand on lit les lèvres n'arrangerait pas les choses."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear
window show


ke "...Alors j'ai réalisé que je pouvais utiliser les ténèbres pour acheter du lait. Généralement, je profite de la pluie ou d'une vague de motards ou de touristes. C'est bien plus pratique... Mais je dépense trop d'argent pour du lait maintenant."

show kenji happy_ni
with charachange


ke "Tu sembles quelque peu morne ou ailleurs ou quelque chose du genre. Ne pense pas trop, un homme doit se limiter à l'action ! Tu peux penser du matin au soir, mais pour changer les choses, il faut agir."


ke "Je fais des trucs tout le temps sans même y penser. C'est pour ça qu'en primaire ils m'appelaient “créateur de problèmes”. Je trouvais ça cool. On dirait presque un nom Indien."


hi "Je suis pas vraiment d'humeur."

show kenji neutral_ni
with charachange


ke "Tu passes une mauvaise journée ?"


hi "Ouais, je sais pas trop. Je suis un peu distrait, là."

stop music fadeout 7.0

hide kenji
with dissolve


"Tellement distrait que c'est seulement quand il est parti que je remarque que son conseil n'était pas si mauvais. Je crois que Shizune m'aurait donné le même. Et là, il est trop tard pour le remercier."


"J'ai déjà répondu trop méchamment. J'ai vraiment l'impression d’être un salaud."


"En y repensant, ces derniers jours je n'ai cessé de regretter tout ce que j'ai fait. Je n'ai même pas pris le temps d'y songer et, par la même occasion, d'apprendre de mes erreurs. Ça ne mène qu'à - n'a toujours mené qu'à - encore plus de regrets."

scene black
with dissolve



label fr_S40:

play music music_dreamy fadein 2.0

scene bg school_dormhisao
with locationchange

play sound sfx_doorknock2


"Le lendemain matin, alors que je m'habille, j’entends quelqu'un frapper à ma porte. Enfilant rapidement les vêtements qu'il me reste à mettre, j'ouvre la porte, n’arrêtant pas de me demander qui pourrait être derrière."

scene bg school_dormhallway
show shizu basic_normal
with locationchange


"Il s’avère que c'est Shizune."

show shizu behind_blank
with charachange


ssh "Misha m'a dit que tu me cherchais."


"Je suis un peu agacé de ne même pas avoir un “bonjour”, mais ce n'est pas très grave."


his "C'était le cas."

show shizu basic_normal2
with charachange


ssh "Mais tu m'as trouvée hier."


"Shizune passe son doigt le long d'une fissure sur le mur. On dirait qu'elle essaye d'avoir l'air distant."

show shizu adjust_smug
with charachange


ssh "Bah, je n'ai pas simplifié les choses, hein ?"


his "C'est pas grave."

show shizu behind_blank
with charachange


ssh "C'est pour ça que je suis là. On peut parler aujourd'hui. Bien que... j'ai envie d'aller ailleurs."


his "Et les cours ?"

show shizu adjust_smug
with charachange


ssh "T’embête pas, t’embête pas."

show shizu basic_normal2
with charachange


ssh "Et si on faisait un tour de l'école ? Tout, sauf le bâtiment principal, sera déserté. La première heure ne devrait pas tarder à commencer."


"Je jette un coup d’œil rapide à ma montre et vois qu'elle a raison."


his "D'accord."

stop music fadeout 6.0

show shizu basic_angry
with charachange

shi "…"


his "Quelque chose ne va pas ?"

show shizu behind_blank
with charachange


ssh "Pourquoi est-ce que tu crois que quelque chose ne va pas ?"


his "Parce qu'il est évident que tu es énervée. Je pouvais le voir."


his "C'est de ça dont je voulais te parler."

show shizu basic_normal2
with charachange


"Shizune fait rapidement craquer ses phalanges alors que je lui parle."

show shizu behind_blank
with charachange


ssh "Apparemment, il est plus facile de savoir ce que je ressens que ce que je croyais. Je faisais de mon mieux pour le cacher. Tu arrives à savoir ce que je pense là ?"

hide shizu
with charaexit


"Je ne réponds pas, et Shizune s'avance vers la porte, suffisamment lentement pour que je sache qu'elle veut que je la suive. Elle a les mains derrière le dos, et elle se tient comme si elle s’apprêtait à se pencher en avant à n'importe quel instant."

scene bg school_courtyard
with locationchange


"Dehors, je me rends compte que Shizune a raison. L'école est complètement déserte. Bien que ce n'est pas la première fois que je vois l'école comme ça, c'est assez sinistre."

scene bg school_backexit at right
with locationchange


"Shizune agit presque comme si je n'étais pas là, regardant le contenu d'un distributeur et marchant lentement jusqu’à ce que nous arrivions derrière le bâtiment principal."

show shizu invis_close at tworight
with None

show shizu basic_normal_close:
    ypos 1.05
with dissolvecharamove


"Finalement, elle s'adosse contre un mur et me fait face, mais c'est comme si j'avais oublié comment commencer une conversation."

play music music_sadness fadein 8.0

show shizu behind_blank_close
with charachange


ssh "Il y a une expression qui dit : “Tu ne sais pas à quel point tu as foiré jusqu’à ce que tu foires.”"


his "Qui dit ça ?"

show shizu basic_normal2_close
with charachange


ssh "Moi, j'imagine."

show shizu basic_angry_close
with charachange


"Réfléchissant à ce qu'elle vient de dire, elle secoue la main de frustration."

show shizu behind_blank_close
with charachange


ssh "D'accord, je vais dire ça différemment."

show shizu basic_normal_close
with charachange


ssh "Quand j'étais petite, on devait faire des affiches pour le Jour de la Terre à l'école. Et il y avait une autre fille dans ma classe que tout le monde considérait comme étant la meilleure artiste."

show shizu behind_blank_close
with charachange


ssh "Ce n'était pas parce qu'elle dessinait mieux que les autres, c'était parce qu'elle était capable de mettre beaucoup de choses sur une seule image."

show shizu adjust_frown_close
with charachange


ssh "Je voulais être meilleure qu'elle, alors j'ai fait des tas d'affiches jusqu’à ce que j'arrive à la meilleure affiche possible. Je devais être la meilleure. En fin de compte, tout le monde a trouvé que mon affiche était la meilleure, même le professeur."

show shizu basic_normal_close
with charachange


ssh "Une semaine après, c'était devenu sans intérêt, je l'ai jetée à la poubelle."

show shizu behind_blank_close
with charachange


ssh "Je crois que je t’ai déjà raconté quelque chose comme ça auparavant."


his "Ouais."

show shizu basic_angry_close
with charachange


ssh "Quand j'ai l'impression d'avoir fini, j'aimerais pouvoir effacer l'ardoise, que j'aie réussi ou non. Je fais subir beaucoup à Misha, et je t’ai entraîné dans tout ça aussi."

show shizu adjust_frown_close
with charachange


ssh "Et chaque moment où j'aurais pu résoudre cette situation idiote, ou l’empêcher d'arriver tout court, revient me hanter."

show shizu behind_sad_close
with charachange


ssh "C'est une sensation horrible. Surtout quand je ressens que je n'ai rien fait correctement et tout fait n'importe comment. Comme récemment. C'est le pire échec possible. J'ai l'impression d’être un échec sur toute la ligne."

show shizu basic_normal2_close
with charachange


ssh "J'aimerais pouvoir effacer tout ce que j'ai fait et être seule, vu que tout ce que j'ai fait c'est faire souffrir Misha pendant deux ans. Et t'avoir entraîné avec moi pendant un an pour des raisons égoïstes."


his "C'est pas grave."

show shizu adjust_frown_close
with charachange


ssh "Si, ça l'est. Tu ne comprends pas. J'y pensais justement ; dans tout ce que j'ai fait, j'ai eu l'impression d'avoir à battre quelqu'un d'autre. Tout le monde, même. Si c'est comme ça, alors dans mes relations avec les gens ? C'est quasiment pareil."


"Je peux voir où cela mène."

show shizu behind_sad_close
with charachange


ssh "Le fait est que j'ai mené la vie dure à tant de gens en étant égoïste, et maintenant je veux être loin des gens pour un moment."


his "Même moi ?"


"Il y a une pause."

show shizu basic_normal_close
with charachange


ssh "Oui."


"Suivi par une pause encore plus longue, cette fois de ma part."


his "Je vois."


his "C'est la chose la plus égoïste que tu puisses faire."


his "Tu ne fais que prendre une autre décision toute seule."

show shizu basic_normal2_close
with charachange

shi "…"


"Pendant une minute, on dirait qu'elle essaye de trouver une bonne façon de répondre, mais en fin de compte, elle hoche juste la tête. Ce que je crois être la meilleure façon de répondre de toute façon."


"Ça lui ressemble bien, d’être directe même à un moment comme celui-ci, mais sans vraies excuses."


"Tout un tas d’émotions tourbillonnent en moi. Je vois une bouilloire devant moi, de l'eau bouillant à l'intérieur, si proche que je peux sentir la chaleur s'en échapper. Je sais qu'il n'y a pas de méthode ou marchandage possible à cet instant."

show shizu adjust_frown_close
with charachange


ssh "Tu m'as dit que tout allait bien, mais ce n'était pas vrai, hein ?"

show shizu behind_sad_close
with charachange


ssh "Je ne peux plus le croire maintenant."


hi "D'accord."

show bg school_backexit at center
show shizu invis_close:
    xpos 0.85
with dissolvecharamove


"Ne prenant même pas la peine de le signer, je me lève. J'ai les mains dans les poches, jouant avec ma monnaie. L'air du matin me glace le visage."

scene ev shizu_badend:
    xalign 0.0 yalign 0.5 zoom 1.1 subpixel True
    acdc_warp 10.0 zoom 1.0
with locationchange


"Alors que je me tourne pour la regarder, elle semble très seule. Ça me rappelle moi. J'avais cette expression avant. Peut-être que je l'ai maintenant aussi. J'ai l'impression que l'image d'une fille aussi seule restera à jamais gravée dans ma mémoire."


"Chaque moment où j'aurais pu éviter ça, ou résoudre le problème revient me hanter. Ça me fait sourire un moment, sans amusement."

stop music fadeout 4.0

window hide

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
