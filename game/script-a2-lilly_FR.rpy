label fr_L1:

window hide None

scene black
with dissolve

play sound sfx_alarmclock

with Pause(2.0)

scene bg school_dormhisao
with openeye

window show


"Je me réveille avec le son énervant de mon alarme, ses chiffres rouges m'aveuglant."

play music music_dreamy fadein 2.0


"C'est la même alarme que celle que j'avais chez moi, un des seuls objets que j'ai gardé d'avant mon arrivée à Yamaku. J'avais espéré que l'utiliser faciliterait la transition vers ma nouvelle vie."


"Ça ne marche pas vraiment."


"Sortant difficilement de mon lit, je me frotte les yeux pour me réveiller puis je me rends à mon bureau. J'ouvre quelques flacons de médicaments éparpillés, et avale quelques cachets sans eau."


"Maintenant, le procédé commence à devenir automatique - quelque chose dont je devrais me réjouir, vu ma situation."

$ renpy.music.set_volume(0.5, 2.0, channel="music")

scene bg school_dormbathroom
with locationskip


"Me sentant mieux réveillé, je me traîne jusqu'à la salle de bains."

play ambient sfx_shower fadein 8.0

show steam
with charaenter


"En attendant que l'eau se réchauffe, je rêvasse alors que ma routine recommence, une fois de plus."


"Les images colorées du feu d'artifice ainsi que les deux filles avec qui je l'ai regardé me reviennent. C'est étrange que des gens que je connais à peine me fassent autant d'effet."


"En même temps, j'imagine que ce n'est pas une situation banale. Mais au moins, en dehors de mon voisin, j'ai quelqu'un avec qui parler maintenant."

stop ambient fadeout 2.0

hide steam
with charaexit


"Le temps filant avant le début des cours, je commence à me préparer pour l'école."

$ renpy.music.set_volume(1.0, 3.0, channel="music")

scene bg school_scienceroom
with shorttimeskip


"Franchissant la porte de la classe, je remarque que je suis plutôt en avance. Cinq ou six étudiants sont déjà là, même si la plupart d'entre eux seraient mieux dans leur lit."


"C'est dans ces moments-là que j'apprécie être du matin. Cela dit, deux étudiantes en particulier semblent être aussi réveillées que d'habitude."


hi "Salut Shizune, salut Misha."

show shizu behind_blank at tworight
show misha perky_smile at twoleft
with charaenter


"Je réalise soudainement que ma salutation n'atteindra pas cette dernière, je lui fais donc rapidement un signe de la main. Ça n'a pas l'air de la gêner."


"Ou même de l'intéresser."

show shizu basic_normal
with charachange

shi "…"

show misha hips_grin
with charachange


mi "Bonjour, Hicchan~ ! Comment te sens-tu ?"


"Je peux seulement supposer que ces salutations viennent de Shizune. Parfois, c'est dur de savoir si elle parle pour elle ou pour Shizune."


hi "Mieux que beaucoup d'autres j'imagine. Vous avez l'air d’être en forme vous aussi."

show misha sign_smile
with charachange

show misha perky_smile
show shizu basic_frown
with charachange


"Pendant que je dis cela, Misha le transmet à Shizune avec des signes."


"Compte tenu du fait qu'elles ont pris très à cœur les préparations du festival, j'aurais probablement dû mieux choisir mes mots."

show shizu behind_frown
with charachange


shi "... !"

show misha hips_grin
with charachange


mi "Puisque tu viens d'être transféré, nous t'avons ménagé. Mais ne crois pas que tu échapperas à tes responsabilités la prochaine fois."


"Misha semble être sur le point d'ajouter quelque chose, mais recommence vite à interpréter les signes de Shizune, celle-ci semblant ne plus s'arrêter."

show shizu basic_frown
show misha sign_smile
with charachange


mi "Bien que ton aide sur le stand de la classe 3-2 est appréciée—"


"Ah. Les nouvelles vont vite. C'est soit ça, soit elles surveillent tout ce qui arrive dans l'école."

show misha hips_frown
with charachange


mi "—nous aurions préféré que tu te concentres sur ce qui était à ta portée. À savoir, ta propre classe."


"Bien que je déteste l'admettre, elles n'ont pas tort. Avant que je ne puisse répondre, Shizune ajoute quelque chose qui fait sourire Misha."

show shizu behind_blank
with charachange

shi "…"

show misha perky_smile
with charachange


mi "Tu as apprécié le festival alors~ ?"


"Fin du sermon, j'imagine."


hi "Ouais, c'était bien. Pour vous aussi ?"

show shizu behind_smile
show misha hips_grin
with charachange


"Shizune fait un petit hochement de tête tandis que Misha balance sa tête d'avant en arrière. Le contraste est assez drôle."


"Du coin de l'œil, je remarque que de plus en plus d'étudiants arrivent en classe. D'un petit coup d'œil à ma montre, je remarque qu'ils ont quelques minutes de retard."

show hanako emb_downtimid at offscreenright
with None

show misha hips_grin at left
show shizu behind_smile at Transform(xpos=0.48)
show hanako emb_downsmile at Transform(xpos=1.0, xanchor=0.7)
show bg school_scienceroom at bgleft
with charamove


"Je me retourne vers le siège de Hanako et remarque qu'elle est déjà là, en train de lire un livre. Je me demande depuis combien de temps elle est arrivée."

show misha hips_grin:
    ease 1.0 xpos 0.2
show shizu behind_smile:
    ease 1.0 tworight
show hanako emb_downsmile:
    ease 1.0 offscreenright
show bg school_scienceroom:
    ease 1.0 center
with None

hide misha
hide shizu
hide hanako
with Dissolve(1.0)


"Provenant du couloir, les pas lourds annonçant l'arrivée de Mutou présagent la fin de notre discussion. Je prends place à côté de Misha."


"Alors que la porte coulissante s'ouvre, il entre d'un pas lourd. Sa posture est encore pire que d'habitude, et ses yeux peinent à rester ouverts. J'imagine que ma moquerie de la veille sur le personnel était maladroite."

play ambient sfx_paperruffling


"Les élèves ouvrent leur livre pendant qu'il arrive à son bureau, et c'est ainsi que le premier cours de la semaine commence."

stop music fadeout 3.0
stop ambient fadeout 0.5

with shorttimeskip

play sound sfx_normalbell

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0


"Je me frotte les yeux pendant que la sonnerie de midi retentit, content de la pause qu'elle annonce."

show lilly basic_smileclosed at offscreenleft
with None

show bg school_scienceroom at bgright
show lilly cane_smileclosed at Transform(xanchor=0.2)
with charamove


"Je ne suis pas surpris de voir Lilly à côte de la porte, canne en main, attendant patiemment Hanako."


"Repensant à ma requête d'hier de les rejoindre et leur accord, je décide de passer la pause avec elles plutôt que seul."

show hanako emb_smile at Alphain(0.5), Slide(0.5,0.5,0.4,0.5,0.5)
with Pause(0.5)

hide hanako
hide lilly
with charaexit


"Hanako se dirige rapidement vers Lilly et avant que je n'aie le temps de les rejoindre, elles sont déjà dans le couloir."

stop ambient fadeout 1.0

scene bg school_hallway3
show lilly back_listen at twoleft
show lillyprop back_cane at twoleft
show hanako emb_downsmile at tworight
with locationchange

show hanako def_shock
with vpunch


"Entendant le son de mes pas derrière elle, Lilly tourne doucement la tête. Hanako le remarquant aussi, bondit presque de surprise."

show hanako defarms_strain
with charachange


ha "Hi... Hisao ?"

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play music music_normal fadein 2.0

show hanako emb_blushtimid
with charachange


ha "Je veux dire... euh... bonjour, Hisao..."


hi "Salut, désolé si je t'ai surprise."

show lilly cane_smile
hide lillyprop
with charachange


"Lilly se tourne pour me saluer, guidée par Hanako."

show lilly cane_smileclosed
with charachange


li "Bonjour, Hisao. Tu nous rejoins pour déjeuner ?"


hi "Si ça ne dérange pas. Il n'y a pas grand-chose d'autre à faire."

show lilly cane_smile
with charachange


"Lilly hoche légèrement la tête pour me faire comprendre que je ne gênerai pas."

scene bg school_staircase2
with locationchange

with Pause(0.3)

scene bg school_hallway2
with locationchange


"Nous descendons un escalier puis marchons dans le couloir jusqu'à la salle habituelle, notre rythme étant un peu plus rapide que d'habitude grâce à Lilly qui utilise Hanako pour se diriger, plutôt que sa canne et les rampes."

scene bg school_miyagi
with locationchange


"Comme prévu, c'est désert. Les rayons du soleil illuminant la pièce, je remarque que le bruit des autres clubs est à peine audible."


"Balayant la pièce du regard, je vois deux chevalets posés contre un mur qui n'étaient pas là avant. Le club d'art doit utiliser cette pièce pour stocker le surplus."

show hanako emb_smile
with charaenter


ha "Je sors l'échiquier ?"


"La voix de Hanako semble moins tendue quand elle parle à Lilly."

show hanako emb_smile at tworight
show bg school_miyagi at bgright
with charamove

show lilly cane_weaksmile at twoleft
with charaenter


li "Oui. Je vais préparer le thé pendant que tu mets en place les pièces."


hi "Ah, je peux le faire si tu veux."

show lilly cane_surprised
with charachange

with Pause(0.3)

show lilly cane_planned
with charachange


"Elle réfléchit un moment avant de sourire, confirmant que j'ai fait le bon choix. Ses expressions sont vraiment faciles à comprendre."

show lilly cane_satisfied
with charachange


li "Je veux bien. Merci."

show lilly cane_satisfied:
    ease 0.5 ypos 1.3
    "lilly basic_cheerful" with Dissolve(0.5, alpha=True)
    ease 0.5 ypos 1.0
with Pause(1.0)

hide lilly
hide hanako
with charaexit


"Elle pose sa canne rétractée sur son sac et le pousse contre un des pieds de la table, avant de s'asseoir en face de Hanako."


"Pendant que je prépare le thé, je peux entendre les petites pièces en bois se mettre en place sur l'échiquier. Je me demande si Lilly est bonne aux échecs, étant donné sa condition."


"Au moment où je place les tasses fumantes sur la table, Lilly et Hanako ont déjà bougé leurs premières pièces tout en grignotant leurs sandwiches et boules de riz provenant de leurs sacs."

$ renpy.music.set_volume(0.5, 2.0, channel="music")

show chessboard:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)


"Je remarque que l'échiquier qu'elles utilisent a des petits trous au milieu de chaque carré et des pics en dessous des pièces, et chaque case noire est légèrement en relief."


"Regarder les doigts de Lilly parcourir le plateau, prenant connaissance de la position des pièces me fait remarquer l'ingéniosité du plateau. Il a dû être fait spécifiquement pour les aveugles."


$ renpy.music.set_volume(1.0, 5.0, channel="music")

show chessboard:
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide chessboard
with None


hi "Et voilà."

scene bg tearoom_everyone_noon
show tearoom_hanae happy
show tearoom_lillye smileclosed
show tearoom_hisaoe hsmile
show tearoom_chess
with locationskip


"Hanako acquiesce alors que je pose la tasse à côté de l'échiquier. La main de Lilly se met légèrement sur le côté, je mets donc doucement la tasse sur la table, prenant soin qu'elle la touche du bout des doigts ; une attention qu'elle a l'air d'apprécier."

show tearoom_hisaoe outside
with charachange


"Je m'assieds finalement et bois silencieusement mon thé pendant qu'elles jouent. Le contraste de leur comportement pendant le jeu est intéressant à voir."

show tearoom_hanae open
with charachange


"Hanako a le visage proche du plateau, très concentrée. Lilly, quant à elle, reste droite et calme."


"La douce voix de Lilly se fait entendre alors qu'elle continue de jouer."

show tearoom_lillye smile
with charachange


li "Comment étaient les cours maintenant que le festival est fini ?"

show tearoom_hanae shy
show tearoom_hisaoe hthink
with charachange


"Je regarde Hanako pour voir si elle va répondre la première, mais je vois qu'elle fait la même chose que moi."

show tearoom_hisaoe sigh
with charachange


hi "Pas... super. La moitié de la classe semblait somnoler, même le professeur. Sans oublier qu'on a eu un test en plus de ça."

show tearoom_hanae happy
with charachange


"Hanako approuve silencieusement mes dires."

show tearoom_lillye ara
with charachange


li "J'imagine que ça n'a pas dû être facile pour toi, vu que tu es nouveau ici."

show tearoom_hisaoe lsmile
with charachange


hi "Je crois que je m'en suis quand même sorti. Même si l'arrivée d'un test si rapidement m'a pris par surprise, je suis plutôt bon en sciences."

show tearoom_hisaoe hsmile
with charachange


hi "Et toi Hanako, tu as réussi ?"

show tearoom_hanae open
with charachange


ha "Moi ? Ah... ça a été... je crois..."


"Hanako est trop sincère pour être capable de bien mentir. Ça se voit de loin."

show tearoom_lillye thinking
with charachange


"Un léger sourire se dessine sur les lèvres de Lilly. D'après sa réaction, Hanako ne doit pas être assez douée en cours pour bien s'en sortir sans réviser."

show tearoom_hisaoe lsmile
with charachange


hi "Et comment ta classe s'en est sortie, Lilly ?"

show tearoom_lillye giggle
with charachange


li "Étonnamment, très bien en fait. Seul un seul étudiant était absent, ce qui est mieux que ce à quoi le professeur s'attendait."

show tearoom_hanae shy
show tearoom_lillye smileclosed
with charachange


"N'ayant plus rien à ajouter, elles se reconcentrent sur le jeu."

show tearoom_hisaoe relief
with charachange


"Je ne peux pas dire que les échecs soient passionnants à regarder, mais étant donné la nature unique de la partie, je suis absorbé par le jeu."

show tearoom_hisaoe outside
show tearoom_hanae sad
with shorttimeskip


"Alors que la partie progresse, elles montrent toutes les deux qu'elles savent plutôt bien jouer. Ayant capturé deux pions de plus que Hanako, Lilly a le dessus, mais de peu."

show tearoom_hanae open
show tearoom_hisaoe hunsure
with charachange


"...jusqu'à ce que Hanako fasse une action étrange avec sa reine. Profitant de cette faille, Lilly prend sa reine avec son cavalier."

show tearoom_hanae shy
with charachange


"Sans hésitation, Hanako bouge un pion pour prendre la tour de Lilly qui est encore en position initiale, et change le pion en reine."

show tearoom_lillye thinking
show tearoom_hisaoe lunsure
with charachange


"Lilly grimace légèrement alors qu'elle passe ses doigts sur les pièces et réalise qu'elle vient juste de tomber dans le piège de Hanako."


"Vu le manque de réaction de Hanako, elle doit avoir l'habitude. Elles ont dû jouer quelques parties ensemble après tout."


ha "Échec."

show tearoom_hisaoe hsmile
with charachange


hi "Pas mal du tout. Bien joué Hanako."

show tearoom_hanae happy
with charachange


"Le compliment la fait rougir."


ha "M-merci. Je ne... pensais pas que ça marcherait."

show tearoom_hisaoe lsmile
with charachange


"Je regarde Lilly, ses doigts repérant les positions de ses pièces restantes dans une tentative d'extirper son roi de cette situation."


li "Je crois que c'est échec et mat..."

show tearoom_hisaoe loops
with charachange


hi "Mmmh ?"

show tearoom_hisaoe relief
with charachange


"Je regarde de plus près pour confirmer."


"En effet, son roi n'a nulle part où s'enfuir sans être menacé par une autre pièce. Je viens juste d'avoir la réponse à ma question au sujet de celle des deux qui est la plus forte."

show tearoom_hisaoe sigh
with charachange


hi "Il n'y aucun doute."

show tearoom_lillye weaksmile
with charachange


"Lilly lâche un petit soupir tandis que Hanako sourit. D'après leur réaction, cela semble se terminer souvent comme ça."

show tearoom_hisaoe lsmile
with charachange


hi "Depuis combien de temps y jouez-vous ?"

show tearoom_hisaoe hsmile
show tearoom_hanae sad

with charachange


ha "Depuis... que je suis petite."

show tearoom_lillye smileclosed
show tearoom_hisaoe lsmile
with charachange


"Lilly hoche la tête à la réponse brève de Hanako."

show tearoom_lillye smile
with charachange


li "Hanako m'a appris à jouer peu après l'avoir rencontrée. Je peux la battre de temps en temps... mais cela reste rare. Je ne dois pas avoir la bonne façon de penser pour ce jeu."


"Supposant que Lilly est à Yamaku depuis le début du lycée et qu'elle a rencontré Hanako quand elle est devenue interne, cela veut dire qu'elle y joue depuis un an environ."


"Après avoir vu le niveau de Hanako, je ne suis pas surpris que Lilly ait du mal à la battre."

show tearoom_hanae happy
show tearoom_hisaoe hthink
with charachange


ha "Mais... elle est meilleure en langues que moi, alors..."

show tearoom_lillye ara
show tearoom_hisaoe lthink
with charachange


"Lilly sourit, légèrement amusée du retour de compliment de la part de Hanako."

show tearoom_lillye weaksmile
with charachange


li "Eh bien, chacun ses points forts."

stop music fadeout 3.0
play sound sfx_warningbell


"À la surprise de tout le monde, la sonnerie retentit, annonçant la fin de la pause déjeuner."

show tearoom_lillye thinking
show tearoom_hisaoe loops
with charachange


li "Mmh, cette partie a duré plus longtemps que je ne le pensais."


hi "Oui c'est vrai. Je suppose qu'on ferait mieux de retourner en classe."

show tearoom_hanae shy
show tearoom_lillye weaksmile
show tearoom_hisaoe thinkclosed
with charachange


"Hanako est déjà en train de remballer, je prends donc le sac de Lilly et le lui tends. À ma grande surprise, elle le prend mais le repose sur la table."

play music music_daily fadein 2.0

scene bg school_miyagi
show lilly basic_smileclosed at twoleft
show hanako basic_normal at tworight
with locationskip


li "Hisao, je peux te demander quelque chose ?"


hi "Oui, bien sûr."

show lilly basic_smile at twoleft
with charachange


li "Ça te gênerait que je touche brièvement ton visage ?"


hi "Oh, euh... non, vas-y, ça ne me gêne pas."


"La question me prend vraiment au dépourvu, mais en y repensant, cela semble normal. Lilly n'a aucune idée de ce à quoi je ressemble, et c'est le seul moyen pour elle de le savoir."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

show ev lilly_touch_uni
with GenericWhiteout(0.5,0.1,3.0)


"Lilly lève sa main droite, que je prends dans la mienne et amène à mon visage avant de la lâcher."


"La salle est dans un silence complet alors que la main de Lilly passe sur mes traits, sur mon menton, mes joues, et le reste."


"J'aurais cru que ce serait plus gênant que ça. Je suppose que c'est parce qu'elle fait juste ça par sens pratique, rien de différent que de regarder le visage de quelqu'un."


"Sa main est douce, mais ce qui me surprend c'est la longueur de ses doigts, sans mentionner à quel point elle est sûre de chacun de ses mouvements. Je n'ai aucun doute que son sens du toucher est de loin plus sensible et précis que le mien."


"Sa main passe brièvement dans mes cheveux avant de se retirer. Je suis sûr que maintenant elle a mémorisé chaque partie de mon visage. C'est seulement là que je remarque que Hanako nous a regardés silencieusement tout le long."

$ renpy.music.set_volume(1.0, 2.0, channel="music")

scene bg school_miyagi
show hanako basic_distant at tworight
show lilly basic_weaksmile_close at twoleft
with whiteout


li "Merci de m'avoir permis de faire ça, Hisao."

show lilly basic_smile_close at twoleft
with charachange


li "Et je me permets d'ajouter que je te trouve assez beau."


"Je rougis un peu à sa remarque, avant de lever un sourcil."


hi "Mais si tu ne peux pas voir, comment..."

show lilly basic_pout_close at twoleft
with charachange


li "Ce n'est pas parce que je ne peux voir que je n'ai pas mes préférences."

show hanako emb_timid at tworight
with charachange


ha "Hum, on ferait mieux d'y aller maintenant..."


hi "Ouais, pas faux. On te revoit plus tard Lilly."

scene bg school_hallway2
show lilly basic_smile at twoleft
show hanako emb_smile at tworight
with locationskip


"En marchant dans les couloirs pour retourner en classe, je remarque que Hanako est plus silencieuse qu'avant, mais aussi plus à l'aise."


"Lilly, sa main sur l'épaule de Hanako, semble être aussi à l'aise dans sa marche, souriant alors qu'on avance."


"Si je peux passer le reste de mon temps à Yamaku comme ça, je ne m'estimerai pas malheureux. Tout ce qu'il faut pour être bien, ce sont quelques moments de bonheur après tout."

scene bg school_scienceroom
with locationskip

play sound sfx_rumble


"Alors que j'arrive à mon bureau et pose mon sac, je réalise quelque chose. Ou du moins, mon estomac le réalise."


"J'étais tellement occupé avec toutes les deux que j'en ai oublié d'acheter à manger..."

stop music fadeout 2.0

scene black
with dissolve



label fr_L2:

scene bg school_dormhisao
with locationchange


"Samedi. Mon deuxième jour préféré de la semaine."


"C'est surtout dû au fait que c'est l'un des jours où il y a le moins de cours, ceux-ci se terminant à midi."

scene bg school_dormhallway
with locationchange


"Je sors de ma chambre avec confiance, étant sûr d'apprécier le beau temps et la courte journée de cours."

scene bg school_dormhallground
with locationchange

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_footsteps_hard


"Je parcours avec confiance le couloir et descends les escaliers vers l'entrée du dortoir des garçons."

$ renpy.music.set_volume(0.6, 4.0, channel="ambient")


"Confiant, je regarde derrière moi pour voir à qui appartiennent les pas qui s'approchent."

$ renpy.music.set_volume(1.0, 4.0, channel="ambient")


"J'ai... perdu confiance dans le fait que cette journée puisse être bonne."

stop ambient
play music music_kenji fadein 0.5

show kenji happy:
    center
    xpos 0.4
    easein 0.5 xpos 0.5
with charaenter


ke "Yo mec, quoi de neuf ?"


hi "Pas grand-chose. J'ai juste hâte d'être cet après-midi. Et toi ?"

show kenji happy_close at center
with characlose


"Il passe son bras autour de mes épaules d'une manière trop aisée. Il y a un truc."

show kenji neutral_close
with charachange


ke "Sortons un moment, tu veux bien ?"


hi "J'étais justement sur le point de le faire, avant que tu ne m'arrêtes."

show kenji tsun_close
with charachange

scene bg school_dormext_full
with locationchange


"Il ne prend pas très bien ma réaction. L'ignorant, je sors et commence à descendre les marches."


"Il ne lui faut pas longtemps pour me rattraper. Je me demande s'il veut de l'argent ou radoter sur une autre conspiration. Peut-être les deux."


show kenji tsun:
    center
    xpos 0.6
    easein 0.5 xpos 0.5
with charaenter


ke "On a un problème à régler tous les deux."


hi "Oh oh."


ke "C'est à propos de cette blonde. Tu sais de qui je parle."


"Va pour la conspiration. Pendant un moment j'envisage de faire comme si je ne savais pas, mais je réalise que ça ira plus vite si je le laisse dire tout ce qu'il a à me raconter."


hi "Lilly ? Celle de ta classe ?"

show kenji rage at center
with vpunch


ke "Tu l'appelles déjà par son prénom ?!"


"Il a l'air vraiment choqué. Il croyait vraiment que je ne pourrais pas répondre ?"

show kenji tsun
with charachange


"Il reprend ses esprits et toussote dans son poing. Dramatiquement, comme il sait si bien faire."


ke "Peu importe. Je suis là pour te prévenir. Tu sais. D'homme à homme."


hi "Me prévenir de quoi ? Lilly ?"


ke "Ouais. Tu ne la connais pas mec."


"C'est pas tellement faux. Cela fait moins de deux semaines que je les connais, Hanako et elle, et on n'a toujours que bavardé de choses banales à propos de l'école pendant notre pause déjeuner."


hi "Je suis sûr que toi non plus."



ke "Aucun rapport. Tu es celui qui passe beaucoup de temps avec elle."


"Ça m'inquiète un peu que quelqu'un comme Kenji, qui est plutôt asocial, sache qui sont mes amis."


"Cela dit... Je suis un étudiant transféré, et elle n'est pas seulement déléguée de sa classe, c'est aussi une belle, grande blonde."


"Peut-être devrais-je prendre son avertissement comme un signe qu'une rumeur circule dans l'école, et que j'en suis le sujet."


hi "C'est juste le déjeuner. Rien de spécial."

show kenji neutral
with charachange


ke "Écoute, mec, sous le pont. Tu vois le pont ? Tu es en dessous. Un homme doit faire ce qu'un homme doit faire pour avoir des informations."

show kenji tsun
with charachange


ke "Je voulais juste m'assurer que tu ne finisses pas trop loin sous le pont."


hi "Tu es en train de me perdre là, Kenji."

show kenji happy
with charachange


ke "C'est pas grave, beaucoup de gens se perdent. C'est pour ça que je suis là pour aider."

scene bg school_gardens
show kenji neutral
with locationskip


ke "Juste sois vigilant avec elle, ok ? Elle a l'air inoffensive de l'extérieur, mais j'ai entendu des choses. Des mauvaises choses."

show kenji tsun
with charachange


ke "Tu connais le Conseil des Étudiants, pas vrai ?"


"Il semble frémir involontairement pendant qu'il dit cela. Imaginer Shizune et lui dans une même pièce est amusant. Je me demande s'ils se sont déjà rencontrés."


hi "Ouais, Shizune et Misha sont dans ma classe. Cela dit, j'ai réussi à éviter l'enrôlement."


show kenji happy
with charachange


ke "C'est bien mec, c'est bien."

show kenji tsun
with charachange


ke "Mais cette blonde ? Elle y était. Dans le Conseil des Étudiants. Elle. Y. Était."


hi "Je vois. Et ?"


ke "Et elle n'y est plus maintenant."

stop music fadeout 3.0

hi "…"


ke "Sérieux, penses-y une seconde. Quelque chose a dû se passer."


"J'arrête de marcher un moment, pensant plus à ce qu'il dit que je ne le devrais."


"Ça expliquerait pourquoi elles se disputent toutes les deux, du moins en partie. Attends, non, pas vraiment. Pour quitter le conseil des étudiants, il faut avoir une raison."


"En fin de compte, ça n'explique pas grand-chose. Outre le fait que leur querelle remonte à longtemps."


hi "Tu as peut-être pas tort là-dessus. Mais je ne vois pas trop en quoi ça me concerne cela dit."

show kenji neutral
with charachange


ke "Ok, maintenant pense à ça. Lilly est, de toute évidence, étrangère."


hi "De toute évidence."


ke "La question est, de quelle nationalité est-elle ?"


"J'ouvre la bouche, mais réalise que je ne connais pas la réponse. En fait, je n'y ai même jamais pensé."


"Étant donné qu'elle n'a pas d'accent et qu'elle agit de manière parfaitement japonaise, je n'y ai jamais accordé d'importance. Maintenant qu'il le mentionne, je suis plutôt curieux."


hi "Pour être honnête, je ne sais pas. Peut-être anglaise ? Ils aiment le thé."


"Je ne devrais peut-être pas m'appuyer sur des stéréotypes, mais c'est tout ce que j'ai."

show kenji happy
with charachange

play music music_kenji fadein 1.0


ke "Tu ne réfléchis pas. Heureusement, je suis là pour penser à ta place."


hi "Eh bien, merci."


"Il ne tente même pas de masquer son ricanement."

show kenji neutral
with charachange


ke "Maintenant réponds à ça : quel groupe a une grande influence sociale, est très riche - tu sais que les blondes sont toutes riches, hein ? - a une longue histoire de conflits et était avant une beaucoup plus grosse organisation ?"


hi "L'Église Catholique ?"

show kenji tsun
with charachange


ke "...Ouais, bon, d'accord, elle aussi."

show kenji neutral
with charachange


ke "Mais il y aussi la Mafia. Réfléchis. Riche, étrangère, elle est sans aucun doute liée à la Mafia."


"J'ai des raisons de douter de la logique de ses déductions, mais il ne s'arrête pas."

scene bg school_hallway3
show kenji neutral
with locationskip


ke "Donc est-ce que tu sais d'où je crois qu'elle vient ?"


hi "Italie ?"

show kenji tsun
with charachange


ke "L'Italie n'a pas de quoi être fière mec. Elle se doit d'être de Sicile. Tous les mafieux viennent de là."

show kenji happy
with charachange


ke "Attends. Non, la Russie. Merde, c'est peut-être plus grave que ça en a l'air. La Mafia là-bas est sérieuse mec. Ex-KGB, paramilitaires, contrebande en masse, et—"


hi "Attends, attends, stop, ralentis une seconde. Où tu veux en venir là ?"

show kenji neutral
with charachange


ke "Tu ne sais pas ce qu'elle fera, mec. Je ne me mettrai pas dans ton chemin - les agents n'opèrent pas comme ça - mais je veux que tu sois vigilant."

show kenji tsun
with charachange


ke "Quand l'heure viendra, on aura besoin de toute l'aide qu'on peut avoir. Je ne veux pas te perdre, camarade."


"Bon, au moins, il est inquiet pour moi. Plus ou moins."

stop music fadeout 4.0

show kenji tsun:
    center
    easeout 0.5 xpos 0.6 alpha 0.0
with None


"Je lui dis au revoir de la main alors que nous nous séparons pour aller dans nos classes respectives, mais je ne suis pas sûr qu'il voit mon geste."

scene bg school_scienceroom
with shorttimeskip

play ambient sfx_crowd_indoors fadein 2.0


"Rangeant mes affaires dans mon sac, je vois les livres de la bibliothèque que j'ai empruntés la semaine dernière. Je pourrais tout aussi bien les rendre, sachant qu'il m'a fallu deux jours pour les finir."


"J'envisage d'inviter Hanako avec moi à la bibliothèque, mais elle est déjà partie. Si c'est pour étudier, c'est pas plus mal que j'y aille seul."


"Après m'être rapidement étiré et avoir salué quelques camarades de classe, je me dirige vers la bibliothèque."

stop ambient fadeout 1.0

scene bg school_library
with locationskip


"Alors que j'ouvre mon sac et mets les livres dans le casier des retours situé devant le bureau principal, je remarque une personne étrange derrière celui-ci. Vieille et grisonnante, elle doit remplacer Yuuko quand elle travaille au café."


"Je commence à chercher une table de libre, une tâche quelque peu difficile car même s'il y a peu d'étudiants ici, ils sont tous assis à leur propre table."


"Remarquant un visage familier, je me dirige vers une table proche de la section braille."

show lilly basic_smileclosed
with charaenter


"Il est dur de dire quand Lilly se concentre, son expression étant totalement impassible alors que ses doigts parcourent les pages remplies de points de son livre."


hi "Salut. Ça te gêne si je m'assois ici ?"

show lilly basic_surprised
with charachange


li "Mmh ? Oh, pas de problème..."


"Elle ne dit rien de plus, apparemment toujours concentrée sur sa lecture."

play music music_lilly fadein 10.0

show lilly basic_smile
with charachange


li "Ah, Hisao."

show lilly basic_smileclosed
with charachange


"Elle hoche la tête pour me saluer pendant que je m'assois en face d'elle. Je sors un livre de chimie de mon sac et me remets dans le chapitre qu'on a fait en classe."


"Pendant un moment, on reste assis là à lire, chacun de notre côté."


"La voir me rappelle ce que m'a dit Kenji ce matin. Ça, et le fait que je n'ai jamais vu quelqu'un lire en braille, font que je n'arrête pas de lui lancer des regards."


"Je me sens coupable de faire ça, étant donné qu'elle n'a aucun moyen de le réaliser, donc je décide de lui demander. Ses origines ne sont pas un secret défense après tout, et il y a autre chose que je viens juste de remarquer dans ses mouvements."


hi "Dis Lilly, je peux te poser une question ?"

show lilly basic_smile
with charachange


li "Bien sûr. Quelque chose ne va pas ?"


hi "Je me demandais juste... Tu es à moitié étrangère, non ?"

show lilly basic_giggle
with charachange


"Elle laisse échapper un petit rire avant de fermer son livre."

show lilly basic_cheerful
with charachange


li "J'ai toujours été amusée de remarquer à quel point les gens sont prudents à ce sujet. Akira a déjà mentionné qu'elle et moi avons l'air différentes des autres."

show lilly basic_smile
with charachange


li "Les détails sont un peu compliqués, mais je suis à moitié japonaise et à moitié écossaise."


"...Écossaise ? Ça n'était pas exactement ma première idée. Cela me demande un effort de ne pas le dire à haute voix."


"J'essaye de rassembler mes connaissances de ce pays. Je crois qu'étant dans le Royaume-Uni, l'Écosse n'est pas un mauvais endroit où vivre mais... je n'en suis pas vraiment sûr."


"Ma première idée de l'Angleterre était étonnamment proche, du moins géographiquement. Ça laisse une autre question en suspens cela dit."


hi "Mais tu n'as pas d'accent...?"

show lilly basic_weaksmile
with charachange


li "C'est là que les détails commencent. Je suis née et ai été élevée au Japon, bien que ma mère soit étrangère."


hi "Ah, je comprends."


"Attends, si elle vit à l'internat juste parce qu'Akira travaille beaucoup..."


hi "Donc ta famille habite loin de l'école ?"

show lilly basic_reminisce
with charachange


"Elle soupire légèrement, comme si elle espérait que je n'aille pas plus loin. Est-ce que sa précédente franchise était une façade ?"


li "Pas... exactement. Ça fait longtemps que je ne les ai pas vus en fait."


"J'ai l'impression qu'elle ne me dit pas tout, mais je ne veux pas exagérer non plus. Son visage montre qu'elle est quelque peu gênée."


hi "Donc... tu parles bien anglais ? Pour être honnête je ne sais pas grand-chose de l'Écosse, mais je sais au moins que c'est la langue utilisée là-bas."


"Il lui faut un moment pour répondre, appréciant le changement de sujet."

show lilly basic_smileclosed
with charachange


li "Oui. Ma famille parlait surtout japonais à la maison quand j'étais petite, mais ils se sont assurés que Akira et moi parlions l'écossais tout aussi bien."

show lilly basic_smile
with charachange


li "Je parle la langue, mais je continue de l'étudier à l'école, pour garder mon niveau et avoir les qualifications sur le papier, surtout."


hi "Donc tu es bilingue ? C'est plutôt impressionnant."

show lilly basic_weaksmile
with charachange


li "Je n'irais pas jusque-là. Avoir des parents qui peuvent parler la langue est un grand avantage, et les livres braille en anglais ne sont pas trop durs à acheter ou importer. Avec l'aide de Yuuko du moins."

show lilly basic_smileclosed
with charachange


li "Il y a une demande relativement forte de professeurs d'anglais ici de toute façon, ce qui me donne la motivation pour bien apprendre."


"De la demande pour des professeurs d'anglais ? Pendant un moment, je me demande pourquoi elle a précisé cela."


hi "Tu prévois de devenir professeur d'anglais ?"

show lilly basic_cheerful
with charachange


"Elle hoche la tête avec enthousiasme."


"Ça doit être bien, d'avoir un avenir défini en tête. Je n'ai jamais vraiment pensé au mien, alors je suis un peu envieux."


hi "Mmh..."

show lilly basic_smile
with charachange


li "Qu'est-ce qu'il y a ?"


hi "C'est juste... Je te vois bien en professeur. Ça te convient bien."

show lilly basic_emb
with charachange


"Pendant un moment, elle reste silencieuse. Elle baisse légèrement la tête et émet un rire gêné, quelque chose que je ne l'avais jamais vu faire."


"Entre le rôle de Lilly en tant que déléguée de classe et sa nature dévouée, enseigner semble être le type de travail qui colle bien à sa personnalité."


hi "Désolé, c'était peut-être un peu maladroit. Mais c'est vrai, cela dit."

show lilly basic_weaksmile
with charachange


"Faisant un signe de la main, elle s'en remet vite."


li "C'est pas ça, c'est juste que... une seule autre personne m'a déjà dit ça auparavant."

stop music fadeout 8.0


"Un silence court, quelque peu tendu suit la discussion. Sans le savoir, j'ai fini par arriver sur un autre sujet gênant."


"Je devrais essayer de la réconforter un peu. C'est à cause de moi qu'elle broie un peu du noir comme ça après tout."


hi "Tu veux aller prendre à manger à la cafétéria après ça ?"


"Ça pourrait lui remonter le moral, ou au moins la distraire de sa situation familiale apparemment compliquée."

show lilly basic_planned
with charachange


"À en juger par son sourire, cela semble avoir l'effet escompté."

show lilly basic_ara
with charachange


li "J'apprécie l'offre, mais la nourriture là-bas..."


"Changement de sujet rapide. Elle a raison cela dit - la nourriture de la cafétéria n'est pas des meilleures."


hi "Peut-être le Shanghai ? On pourrait demander à Hanako si elle veut venir aussi."

show lilly basic_surprised
with charachange


li "Ah..."


hi "Qu'est-ce qu'il y a ?"

show lilly basic_weaksmile
with charachange


li "J'avais presque oublié jusqu'à ce que tu me le rappelles. C'est bientôt l'anniversaire de Hanako, et je compte aller en ville demain pour lui acheter un cadeau."


hi "Si c'est une invitation, je serais heureux de t'accompagner."


"M'habituer à la ville serait une bonne chose. Je viens à peine d'arriver ici, alors je me perdrais tout seul."

show lilly basic_smile
with charachange


"Elle hoche la tête, signalant qu'elle approuve joyeusement les plans de ce dimanche."


"Nous finissons par retourner à nos livres respectifs, bien qu'avant de recommencer à lire, je jette un dernier coup d'œil dans sa direction."


"Peut-être que j'ai trop réfléchi à ma propre situation. Après tout, tout le monde ici a ses propres histoires et circonstances."


"La chance de sortir et de me changer les idées me fera du bien."

scene black
with dissolve



label fr_L3:

play ambient sfx_traffic fadein 10.0

scene black
with None

scene bg city_street1 at Fullpan(16.0, "left")
with locationchange


"Fatigué de rester sur place à regarder la télévision à travers la vitrine du magasin, je m'en détache sans grand effort."


"Après avoir vécu à Yamaku, la ville semble être un monde complètement différent."


"Ne pas courir dans les couloirs. Calme et bonne conduite sont de rigueur en classe. Vérifier des deux côtés avant de sortir de cours. Les ascenseurs sont réservés aux étudiants à mobilité réduite. Une seule file dans les escaliers."


"Comparé à des règles aussi strictes, le quartier commerçant de la ville pourrait tout aussi bien être un pays étranger."


"Bien que l’école a eu sa part de brouhaha et de bousculades durant le festival, le monde extérieur est bien différent."


"C'est étrange. Ayant vécu dans une grande ville avant mon accident, cela devrait m’être plus naturel que Yamaku et ses environs."


"Et pourtant ça me paraît étranger. Les escalators et les grands bâtiments arborant chacun des publicités plus grandes que trois personnes, ne font rien pour me distraire de la réaction des gens qui passent."

$ renpy.music.set_volume(0.7, 0.5, channel="ambient")

show lilly cane_smileclosed_cas_close:
    center
    xpos 0.2
    easein 1.0 twoleft
show bg city_street1 at left
with Dissolve(1.0)


"Lilly garde une main sur mon épaule, l'autre tenant sa canne qui tape sur le sol avec la précision d'un métronome. En la regardant, je vois que son sourire neutre est toujours là."


"L'ayant seulement vue dans son uniforme scolaire, je ne l'aurais pas reconnue sur le banc où elle m'attendait, si elle n'avait pas eu sa canne et ses cheveux bien distinctifs."


"Je ne peux pas dire s'ils la regardent à cause de sa taille, son air étranger, le fait qu'elle soit aveugle, ou les trois. Enfin, savoir ne rendrait pas la situation moins inconfortable qu'elle ne l'est."

show lilly cane_smile_cas_close
with charachange


li "Tu as une idée de où chercher en premier, Hisao ?"


"Sa douce voix interrompt mes pensées."


"Je ne peux pas croire qu'elle ne se rend pas compte de l'attention qu'elle attire, mais elle ne laisse rien transparaître. J'ai le sentiment que c'est le genre de personne à aimer se balader, elle doit donc y être habituée maintenant."


hi "Pas vraiment. C'est la première fois que je viens dans cette ville, donc je ne sais pas vraiment où aller."

show lilly cane_listen_cas_close
with charachange


"Elle fronce les sourcils en réfléchissant, essayant de se souvenir d'une route, et aussi d'un moyen de l'indiquer."


"Quelque chose que j'ai remarqué en étant avec elle, c'est que quand elle réfléchit, elle ne montre presque aucun signe corporel."


"Son expression peut changer, mais elle ne fera aucun mouvement. Elle ne semble pas être du genre à s'exprimer avec les gestes, donc j'imagine que c'est dû à sa nature réservée."

show lilly cane_weaksmile_cas_close
with charachange


li "Est-ce qu'il y a un grand magasin d’électronique ici ?"


"Je jette un œil aux alentours, voyant surtout des magasins de vêtements. Après quelques secondes je remarque un magasin avec une enseigne bleue qui correspond à sa description."


hi "Ouaip, c'est juste un peu plus loin. On doit aller par là ?"

show lilly cane_smile_cas_close
with charachange


"Heureusement, c'est l'information dont elle avait besoin. Après un hochement de tête nous avançons vers la destination inconnue de Lilly, se guidant par des repères."

stop ambient fadeout 2.0

scene ev icecream
with shorttimeskip

play music music_happiness fadein 2.0


"Vendeur" "Et voilà. Une vanille, et une chocolat."

scene bg city_street2 at center
with locationchange


"Je lui donne l'argent et apporte les cônes là où Lilly est assise."


"Je n'arrive pas à croire qu'elle m'ait piégé comme ça. Non seulement elle m'a amené jusqu’à un glacier, mais en plus elle s'est arrangée pour que j'aille lui en acheter une. Au moins elle a payé pour la sienne."

show lilly cane_smileclosed_cas at Transform(xanchor=0.5, xpos=0.2, ypos=0.2, yanchor=0.0)
with charaenter


"Elle est là, à attendre patiemment où je l'ai laissée. J'imagine qu'elle prévoyait de faire de cette journée un évènement, plutôt que juste un peu de shopping."

show lilly cane_smileclosed_cas:
    ease 1.0 xpos 0.5 xanchor 0.5 ypos 0.15
show bg city_street2:
    ease 1.0 left
with None

show lilly basic_satisfied_cas_close:
    xanchor 0.5 xpos 0.2 ypos 0.2 yanchor 0.0
    ease 1.0 xpos 0.5 xanchor 0.5 ypos 0.15
show bg city_street2:
    ease 1.0 left
with Dissolve(1.0)


"Je l'appelle et place doucement la glace à la vanille dans ses mains, prenant soin d’être sûr qu'elle la tienne bien avant de la lâcher."


"Au moins ses goûts sont normaux. J’étais inquiet qu'elle puisse demander une saveur bizarre."


hi "Voilà la monnaie."

show lilly basic_smileclosed_cas_close at Transform(xalign=0.5, ypos=0.15)
with charachange


li "C'est bon, garde-la."


"Je commence à protester, mais réalise que c'est futile de le faire pour si peu. Je mets donc la monnaie dans ma poche."

show lilly basic_smileclosed_cas_close
with charachange


"Lilly ne montre aucun signe de vouloir repartir, je m'assois donc à côté d'elle et commence à manger ma propre glace."


hi "Il fait bon. J’espère que ça restera comme ça un moment."

show lilly basic_weaksmile_cas_close
with charachange


li "Toi aussi ? Je commence à penser que je suis la seule personne à préférer l'hiver."


"J'y réfléchis une seconde."


hi "Ouais, c'est bien possible."

show lilly basic_pout_cas_close
with charachange


"Ça marche comme prévu. Elle est mignonne quand elle fait la moue."


hi "Vraiment, je n'arrive pas à imaginer ce qui peut être bien dans l'hiver. Tu ne peux pas sortir sans t'emmitoufler, et même là tu gèles sur place."

show lilly basic_reminisce_cas_close
with charachange


li "Je vivais beaucoup plus au nord avant, là où il y avait souvent de la neige pour jouer, donc je suis un peu nostalgique. Je n'aime pas trop la chaleur non plus."


hi "Au moins tu peux porter une jupe, alors ne te plains pas trop."

show lilly basic_giggle_cas_close
with charachange


"Elle rit un peu alors que nous finissons tous les deux nos cônes en train de fondre."

play ambient sfx_crowd_outdoors fadein 2.0

hide lilly
show crowd at left
with shorttimeskip


"Je regarde la foule passer pendant que nous mangeons, entendant des bribes de conversations."

show lilly basic_satisfied_cas_close at Transform(xalign=0.5, ypos=0.15)
with charaenter


"Regardant Lilly, je la vois lécher sa glace consciencieusement de bas en haut, en ignorant totalement qu'elle commence à couler."


hi "Ça coule."

show lilly basic_surprised_cas_close
with charachange


li "Où ça ?"


hi "Euh... Un peu plus bas ?"

show lilly basic_listen_cas_close
with charachange


"Elle descend un peu sa bouche sur le cône, mais n'a aucune idée d’où exactement la glace coule. S'ensuit un jeu de guidage droite et gauche jusqu’à ce qu'elle trouve enfin."


"Quiconque regardant devrait trouver ça bizarre - une fille avec les yeux fermés tournant la main dans tous les sens alors que le gars à côté d'elle lui donne des instructions. Une étrange variante d'un jeu d'aveugle enfantin, peut-être."

show lilly basic_smileclosed_cas_close
with shorttimeskip


"On arrive finalement au bout du cône, tout en continuant à discuter de tout et de rien."

stop music fadeout 3.0

show lilly back_listen_cas_close
with charachange


"S’arrêtant au milieu d'une phrase, Lilly penche la tête à sa manière. C'est un signe que quelque chose a attiré son attention."

show lilly back_smileclosed_cas_close
with charachange


li "Ah..."


hi "Qu'est-ce qu'il y a ?"

show lilly back_smile_cas_close
with charachange


li "Est-ce que tu peux voir si Akira est quelque part pas loin ? Je crois que je l'ai entendue."

show lilly back_smile_cas_close at Transform(xpos=0.25)
show crowd:
    bgright
    xpos 0.55
show bg city_street2:
    bgright
    xpos 0.55
with dissolvecharamove





"Je regarde dans la direction de son attention, doutant quand même un peu de sa capacité à entendre la voix d'Akira dans ce vacarme."

show akira basic_boo behind crowd:
    tworight
    xpos 0.78 ypos 1.13
with charaenter


"Et pourtant, à travers cette foule de gens qui circulent, je peux voir une fille blonde dans un costume."


"Je lève une main, essayant d'attirer son attention."


hi "Satou ! Hé, Satou !"

show akira basic_smile
with charachange


"Elle s’arrête et regarde dans ma direction, cherchant l'origine de la voix. Pendant ce temps, je remarque que quelqu'un marche à ses côtés."


"Je ne peux pas bien voir qui c'est, avant qu'elles ne viennent nous rejoindre."

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")
play music music_ease fadein 4.0

show akira basic_smile:
    ease 1.0 ypos 1.0 alpha 0.0
with None

show akira basic_smile as akira2 behind lilly:
    tworight
    xpos 0.78 ypos 1.13 alpha 0.0
    ease 1.0 ypos 1.0 alpha 1.0
with Pause(1.0)

hide akira
with None

show lilly back_smile_cas_close at Transform(yalign=1.0)
with charamove


"Alors qu'elles nous rejoignent, Lilly et moi nous levons pour les accueillir."

show lilly back_giggle_cas_close
with charachange


li "Akira ?"

hide akira2
show akira basic_laugh behind lilly:
    tworight
    xpos 0.78 ypos 1.0
with charachange


aki "Salut vous deux."

show lilly back_giggle_cas_close at Transform(xpos=0.1)
show akira basic_smile at Transform(xanchor=0.5, xpos=0.6)
show crowd at center
show bg city_street2 at center
with dissolvecharamove

show hideaki bored at right behind akira
with charaenter


"Elle hoche la tête dans ma direction, geste que je lui retourne. Mon regard se dirige vers la jeune fille à ses côtés, et nos yeux se rencontrent. Akira pose une main sur sa tête, un geste qui ne semble pas la gêner."

show hideaki normal
with charachange


hh "Je ne crois pas qu'on se soit déjà rencontrés. Je suis Hideaki. Ravi de te rencontrer, Hisao."


"Un nom de garçon, hein ? J'ai l'impression d'avoir évité une balle là. Il se penche pour me saluer, quelque peu restreint par la main d'Akira sur sa tête."

show lilly basic_smileclosed_cas_close at Transform(xpos=0.18)
with charachange


li "Oh, Hideaki est là aussi ? Comment vas-tu ?"

show hideaki thinking
with charachange


hh "Akira a bien pris soin de moi, merci."

show akira basic_laugh
show hideaki sad
with charachange


"Akira sourit comme pour confirmer et lui frotte fort la tête, la faisant partir dans toutes les directions. Son visage désemparé est plutôt drôle."

show akira basic_smile
with charachange


aki "L'oncle est encore parti en voyage d'affaires, donc je l’emmène faire un tour en ville aujourd'hui."

show akira basic_boo
with charachange


aki "J'aurais préféré passer la journée avec mon petit copain, mais bon..."

show hideaki closed_up
with charachange


"Hideaki tousse et essaye de recentrer les pensées d'Akira."


"Pendant ce temps, je me pose des questions. Ils sont de la même famille ? Cousins ? Ça expliquerait pourquoi elle prend soin de lui."


hi "D'ailleurs, Hideaki, comment est-ce que tu connais mon nom ?"

show hideaki serious
with charachange


hh "Akira me l'a dit. Étant un étudiant de Yamaku, je suppose que tu as un handicap quelconque ?"


hi "Tout le monde à Yamaku n'est pas handicapé..."


"Ce que j'ai d'ailleurs appris il y a juste quelques jours. Je remercie silencieusement Shizune et Misha pour leurs informations sur le fonctionnement de l’école."


"Grâce à elles, j'ai appris que l’école accepte pratiquement tout le monde souffrant d'un handicap non-mental, et n'est pas discriminatoire envers les gens en bonne santé non plus."


"Je ne vois pas pourquoi des gens sans handicap s'inscriraient cela dit. Bien que le niveau scolaire soit plutôt haut, l’école est extrêmement isolée et très axée sur l'aide aux étudiants handicapés."

show hideaki angry_up
with charachange


hh "Tu évites de répondre."


"Merde, il est tenace."


"Avant que je ne puisse dire un autre mot, il décide de tenter sa chance."

show hideaki evil
with charachange


hh "Si je devais deviner, je dirais... ton cœur ?"

$ renpy.music.set_volume(0.5, 0.5, channel="music")
$ renpy.music.set_volume(0.0, 0.5, channel="ambient")

show akira basic_lost
show lilly basic_listen_cas_close
with charachange


"Akira aussi a l'air intéressée. Il a eu de la chance quand même."


hi "Comment est-ce que tu as... ?"

$ renpy.music.set_volume(1.0, 10.0, channel="music")
$ renpy.music.set_volume(0.5, 10.0, channel="ambient")

show hideaki thinking
with charachange


hh "Il ne te manque aucun membre, tu n'as aucune difformité, donc tu n'as pas de handicap visible de l’extérieur."

show hideaki serious
with charachange


hh "Prenant en compte l'absence de maniérisme étrange, il est aussi improbable que tu aies un handicap mental."

show lilly basic_planned_cas_close
with charachange


li "Mais Yamaku ne prend pas les handicapés mentaux."

show hideaki bored
with charachange


hh "Je sais."

show hideaki serious_up
with charachange


hh "Laissant ça de côté, il ne reste que les anomalies internes."

show hideaki happy
with charachange


hh "Je ne savais pas laquelle ça pouvait être, alors j'ai tenté le coup. Et j'ai eu raison, ta réaction me l'a confirmé."

show akira basic_smile
with charachange


"Un peu stupéfait, je regarde Akira, elle sourit et hausse les épaules, prenant de toute évidence avec humour les déductions de son partenaire."


"Il est perspicace, oui, mais surtout un peu désagréable. Logique, mais avec un manque de tact. Son attitude me rappelle Shizune, et d'une certaine façon, son look aussi."

show hideaki disapproves
with charachange


hh "Pourrais-je savoir pourquoi tu me fixes ? Je ne pense pas être si étrange."


"Il n'a pas l'air d’être un peu étrange ? Je peux ignorer les guêtres et les autres vêtements comme si c'était simplement une coïncidence, mais le ruban dans les cheveux est en trop."


"Ce n'est pas le sujet cela dit."


hi "Désolé. Tu me rappelles juste quelqu'un."

play sound sfx_impact

show akira basic_boo
show hideaki surprise_up
with vpunch


"Akira lui donne un petit coup de coude."

show akira basic_laugh
with charachange


aki "J'te l'avais dit que tu lui ressemblais beaucoup."

show hideaki closed_up
with charachange


"Il tousse dans sa main et essaye de garder une attitude droite et sérieuse."


hh "Je vois que tu as rencontré ma sœur. Peut-être que mon nom complet t'aidera."

show hideaki serious
with charachange


hh "Je suis Hideaki Hakamichi. Tu es probablement en train de penser à ma sœur, Shizune Hakamichi."


"Oh, donc il est le frère de Shizune."


"Attends une minute, si Hideaki est le fils de l'oncle d'Akira, et Shizune est sa sœur, alors ça veut dire que les pères de Shizune et Lilly sont frères. Et donc..."


hi "Lilly et Shizune sont cousines ?"

show lilly basic_concerned_cas_close
show akira basic_smile
with charachange


"Lilly sort un gémissement plaintif à l'annonce de ma découverte. Sa réaction provoque un sourire amusé de sa sœur."


"L’hostilité entre Shizune et Lilly vient de prendre une autre dimension. Je croyais que c’était simplement dû à une difficulté de communication, mais une querelle de famille rend les choses plus compliquées."


show akira basic_laugh
with charachange


aki "Tu peux choisir tes amis, mais tu ne peux pas choisir ta famille."

show akira basic_boo
with charachange


"Elle hausse mollement les épaules. Elle ne doit pas porter autant d'importance à leur conflit que moi."

show akira basic_smile
with charachange


aki "Bah, on n'y peut rien. Qu'est-ce que vous faites ici tous les deux par un si beau jour ?"

show lilly basic_smileclosed_cas_close
with charachange


li "On achète un cadeau pour l'anniversaire de Hanako. C'est bientôt, alors c'est la dernière occasion qu'on a avant que l’école ne reprenne pour la semaine."

stop music fadeout 7.0

show akira basic_lost
with charachange


"Akira fait une tête bizarre, comme si Lilly venait de dire que le ciel n’était pas bleu ou que les nuages n’étaient pas blancs."


aki "Son anniversaire n'est pas le dix du mois prochain ?"

show lilly basic_surprised_cas_close
with charachange


li "Oui... Pourquoi ? Quelque chose ne va pas ?"

show akira basic_resigned
with charachange


"Le visage d'Akira se décompose. C'est une expression étrange à voir de la part de quelqu'un d'aussi têtu."


aki "Nos parents ne t'ont pas encore appelée ?"

show lilly basic_oops_cas_close
show hideaki confused
with charachange


"Alors que Lilly secoue la tête, je regarde Hideaki pour voir s'il sait quelque chose. Un léger haussement d’épaules est sa seule réponse."

show akira basic_boo
with charachange


"Pendant un moment, Akira se demande quoi faire, avant de sourire. Le fait qu'elle puisse cacher ses émotions aussi rapidement et efficacement est quelque peu troublant."

show akira basic_smile
with charachange


aki "Hé Petit, désolé, mais ça te gênerait de traîner avec Hisao pendant un moment ?"

$ renpy.music.set_volume(0.7, 2.0, channel="ambient")

show hideaki normal
with charachange

show lilly basic_oops_cas_close:
    parallel:
        easeout 1.0 xpos -0.5
    parallel:
        linear 0.7 alpha 0.0
show akira basic_smile:
    parallel:
        easeout 1.0 xanchor 1.0 xpos 0.0
    parallel:
        linear 0.7 alpha 0.0
show hideaki normal:
    ease 1.0 center
show bg city_street2:
    ease 1.0 right
show crowd:
    ease 1.0 right
with Pause(1.0)

hide lilly
hide akira
with None


"Il hoche la tête et lui fait un signe de la main, Akira met une main sur l’épaule de Lilly et l’emmène hors de portée de voix."


"Et donc, je suis seul avec “Petit“."



hi "Donc... il fait bon, non ?"

show hideaki thinking at center
with charachange


hh "On dirait bien."

"…"


hi "Ils nous ont abandonnés."

show hideaki serious
with charachange


hh "En effet."


"Quel grotesque essai pour lancer une conversation. Je n'ai aucune idée de comment parler à ce gars, et ses réponses robotiques n'aident pas."

show hideaki triangle
with charachange


"Sans un autre mot, il commence à jouer avec ses pieds montrant de toute évidence son ennui. Il agit vraiment comme un enfant, malgré son attitude sérieuse."


"La conversation étant finie, je décide de faire ce pour quoi je suis venu en premier lieu."


hi "Je vais acheter un cadeau. Tu viens ?"

show hideaki normal
with charachange


hh "Pas grand-chose d'autre à faire."

stop ambient fadeout 0.5

scene bg city_street3
with shorttimeskip

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_traffic fadein 2.0


"Après un petit moment, on arrive devant un petit magasin à côté d'une supérette."


"Pour une fois les vitrines du magasin ne sont pas remplies d'appareils électroniques et de jeux vidéo, mais de poupées, de peluches et d'autres objets étranges en bois."


hi "Les antiquités... d'Othello ?"


"Un magasin d’antiquités ? Bon, s'il y a quelque chose pour Hanako dans cette ville, ça sera ici."


"Je m'approche de la poignée de porte ayant l'air - elle aussi - ancienne, mais me ravise au dernier moment en remarquant que mon compagnon ne me suit pas."


hi "Tu ne rentres pas ?"

show hideaki triangle at center
with charaenter


hh "Je serai au kiosque d'à côté en attendant. T'embête pas pour moi."


"Sa voix montre qu'il ne porte clairement aucun intérêt à ce qu'il y a dans le magasin et qu'il ne se sent pas obligé de me suivre."

hide hideaki
with charaexit


"Alors qu'il part sans dire un autre mot, je pousse la vieille porte en bois et entre dans le magasin, une clochette signalant mon entrée."

stop ambient fadeout 0.5
play sound sfx_storebell

scene bg city_othello at Fullpan(10.0, dir="left")
with locationskip

play music music_soothing fadein 0.5


"L'odeur des vieux livres est des armoires en bois est vraiment particulière."


"Je regarde vers le comptoir à côté de la porte. Derrière celui-ci, un homme grisonnant est assis silencieusement, lisant un livre. Il va bien avec cet endroit."


"Parcourant lentement les allées, aucun des objets faits à la main ou des étrangetés importées ne me semble correspondre à Hanako."


"M'accroupissant, j'examine l'ancien bureau en chêne devant la fenêtre du magasin."


"Au moins trente poupées, toutes différentes en taille. La seule similarité entre elles est les longues robes victoriennes qu'elles portent."


"Je regarde le prix d'une d'entre elles qui est assez grande."


"...Ce n'est pas dans mes prix. Du tout."


"Je fais pareil avec chacune d'entre elles, déprimant de plus en plus au fur et à mesure qu'elles deviennent de plus en plus petites en taille."


"Et ce, jusqu’à ce que j'atteigne la plus petite. Elle est abordable, ayant l'air de bonne qualité, avec des longs cheveux bruns et une petite robe bleue."


"Je pense que c'est le genre de cadeau qui plairait à Hanako. Plutôt jolie, et loin d’être criarde."


"Après l'avoir prise avec soin, je décide de faire un tour du magasin. Je ne sais pas si c'est juste parce que j’aime l’atmosphère ou par simple curiosité."

stop music fadeout 2.0

show bg city_othello at left
with None


"Regardant dans un coin avant d'aller de l'autre côté, je vois que les étagères sont remplies de jouets en bois, que ce soit des voitures ou des automates."

show musicbox closed:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)


"Masquée par une rangée d'ustensiles, je remarque une petite boîte en bois. Alors que je la soulève avec ma main libre, je la trouve étonnamment légère."

show musicbox open:
    ypos 0.5 alpha 1.0
with charachange

play music music_musicbox


"Le couvercle a besoin d'un tout petit mouvement pour s'ouvrir, le petit disque en métal à l’intérieur commence à tourner immédiatement."


"Pendant plusieurs secondes, je reste simplement là à écouter la douce mélodie."


"Pendant que la musique se joue, je prends l’étiquette et la regarde, la petite écriture est un peu dure à lire."


"C'est abordable... Plus ou moins."

show musicbox closed
with charachange

play sound sfx_switch
stop music

show musicbox closed:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide musicbox
with None


"Grimaçant légèrement, je ferme le couvercle et me dirige vers la caisse avec la poupée et la boîte à musique en main."

show shopkeep surprised at center
with charaenter


"Quand je les pose sur le comptoir, l'homme qui est derrière les prend et enlève les étiquettes. Il ne cache pas très bien sa surprise quant au fait que quelqu'un de mon âge achète ce genre d'objet."

show shopkeep thinking
with charachange


"Je lui donne douloureusement l'argent et quitte le magasin avec un petit sac opaque en main."

play ambient sfx_traffic fadein 0.5

scene bg city_street3
show hideaki serious at center
with locationchange


"Le fait que Hideaki soit là me surprend."


hi "Oh. Salut. Je croyais que tu étais au kiosque."

show hideaki bored
with charachange


hh "Akira m'a appelé. Elle nous attend à la fontaine avec Lilly."


"Au moins ça résout d'avance le souci d'avoir à les retrouver."

$ renpy.music.set_volume(0.4, 0.5, channel="ambient")

scene bg city_street2
with locationskip


"On se redirige vers la fontaine. La posture et la présentation parfaites de Hideaki forment un drôle de contraste avec son apparence, même en marchant."

show lilly cane_reminisce_cas at twoleft
show akira basic_boo at tworight
with charaenter


"Lilly et Akira se tiennent là, une drôle d'expression sur le visage."

show akira basic_smile at tworight
with charachange


aki "Yo. Prêt à partir, Petit ?"

show bg city_street2 at bgleft
show lilly cane_reminisce_cas at left
show akira basic_smile at Transform(xpos=0.55)
with charamove

show hideaki happy at right
with charaenter


"L'humeur de Hideaki semble s’améliorer alors qu'il la rejoint."

show hideaki happy_up
with charachange


aki "Lilly, Hisao, à plus. Souhaitez bon anniversaire à Hanako de ma part."


hi "Sans faute. À la prochaine."

show lilly cane_weaksmile_cas
with charachange


li "Au revoir, Akira."

hide akira
hide hideaki
show lilly cane_reminisce_cas
with charaexit

show lilly cane_reminisce_cas at center
show bg city_street2 at bgright
with charamove


"Et sur ce, ils disparaissent tous les deux dans la foule."


"Me tournant vers Lilly, je remarque qu'elle porte un petit sac. C'est maintenant que je remarque pourquoi elle a l'air un peu différente. Habituellement, Lilly est du genre à afficher ses émotions sur son visage, cette fois elles sont difficiles à lire."


"On peut les lire difficilement, mais étant donné les efforts qu'elle fait pour masquer ce qu'elle ressent, je doute qu'elle veuille en parler."


hi "Tu as déjà acheté un cadeau à Hanako ?"

show lilly cane_weaksmile_cas
with charachange


li "Oui. Et toi ?"


hi "Ouais."

show lilly cane_sleepy_cas
with charachange


li "On retourne à la station de bus alors ?"


hi "Ok. Il devrait y en avoir un bientôt."


"Et sur ce, on se remet à marcher."

$ renpy.music.set_volume(0.7, 0.5, channel="ambient")

scene bg city_street1
show lilly cane_concerned_cas_close at twoleft
with locationskip


"L’atmosphère est différente d'avant et vraiment bizarre. La main de Lilly sur mon avant bras est étrangement tendue."


"Le silence continue pendant un moment. Je n'aime vraiment pas la voir comme ça."

show lilly cane_sleepy_cas_close
with charachange


li "L'anniversaire de Hanako devra se dérouler un peu plus tôt. Est-ce que le quatre du mois prochain te convient ?"


"Je n'ai rien d'autre de prévu, alors je hoche la tête par réflexe. C'est seulement après que je me rappelle que ça ne sert à rien. Je lui réponds vite à voix haute."


"Elle essaye de ne plus penser à ce qui la perturbe, mais en vain, il est facile de voir qu'elle est perdue dans ses pensées."

show lilly cane_weaksmile_cas_close
with charachange


li "Désolée Hisao. Tu disais que le bus serait bientôt là, c'est ça ?"


hi "C'est ça."


"Mais maintenant qu'elle le dit, j'ai une idée."


hi "D'ailleurs, tu as autre chose à faire aujourd'hui ?"

show lilly cane_oops_cas_close
with charachange


li "Je... ne pense pas. Pourquoi ça ?"


hi "C'est normalement le moment où je prends ta main et je t'emmène en courant quelque part, mais même sans ça, tu vas devoir me faire confiance, d'accord ?"

show lilly cane_surprised_cas_close
with charachange


"Je prends sa main et la dirige gentiment, son expression distante transformée par la surprise et la curiosité."

stop ambient fadeout 2.0

scene bg city_karaokeint
with shorttimeskip

$ renpy.music.set_volume(1.0, 10.0, channel="ambient")
play music music_another fadein 2.0


"Alors que la serveuse pose la tasse de thé et celle de café que j'avais commandées, je la remercie avant qu'elle ne reparte."


"Pour être honnête, j'ai vraiment eu de la chance de trouver ce café. Je ne savais pas vraiment où j'allais, j’étais plutôt en train de chercher un café qui avait l'air bien."


"Lilly amène la tasse à ses lèvres et boit une petite gorgée, alors que j'en prends une grande du café qui m'a été servi."


"Comme je l’espérais, son visage s'illumine alors qu'elle réalise le parfum du thé."

show lilly basic_weaksmile_cas_close at Transform(xalign=0.5, ypos=0.15, yanchor=0.0)
with charaenter


li "Ah... C'est délicieux !"

show lilly basic_surprised_cas_close
with charachange


li "Hisao, comment as-tu su que c’était... ?"


"J'ai demandé un thé noir français à la vanille, espérant que ça puisse être sa saveur préférée, ou du moins une qu'elle aime. Même en ne connaissant pas grand-chose au thé, ça avait l'air d’être un de ceux qu'elle apprécie."


"...En me basant sur le fait qu'elle aime la glace à la vanille. Je ne suis vraiment pas un amateur de thé."


hi "C’était un coup de chance. Tu aimes vraiment le thé, hein ?"

show lilly basic_smileclosed_cas_close
with charachange


"Elle pose sa tasse et hoche légèrement la tête, affichant de nouveau ce petit sourire que je lui connais."

show lilly basic_smile_cas_close
with charachange


li "Boire du thé est... apaisant, je dirais."


hi "Vu la quantité que tu en bois, tu es sûre que tu n'y es pas accro ? L'addiction à la caféine est plutôt commune de nos jours."

show lilly basic_giggle_cas_close
with charachange


li "Ai-je déjà dit que je ne l’étais pas ?"


"Elle laisse échapper un petit rire. Nous avons tous nos vices, et je pense qu'il y a bien pire en matière d'addiction."


hi "Thé noir français à la vanille, hein ? Je m'en souviendrai."

show lilly basic_smileclosed_cas_close
with charachange


"Pendant un moment, nous buvons silencieusement. C'est réconfortant d'avoir quelqu'un comme elle avec soi, même si c'est juste en étant assis tous les deux en silence."


"Alors que je commence à divaguer en me demandant si c'est pareil pour elle, elle pose sa tasse."

show lilly basic_emb_cas_close
with charachange


li "Hisao, est-ce que je peux te poser une question un peu étrange ?"


hi "Ça dépend de la question, je suppose."

show lilly basic_weaksmile_cas_close
with charachange


li "Je me demandais... quelle était ta couleur préférée. Tout le monde en a une, après tout."


"Je suis sur le point de lui répondre avant de comprendre pourquoi la question en elle-même est étrange."


hi "Ma couleur préférée ? Mais..."

show lilly basic_pout_cas_close
with charachange


"Elle fait un peu la moue, voulant quand même entendre ma réponse. Bien que lui répondre ne semble pas avoir un grand intérêt, cela ne coûte rien de le faire."


hi "J'ai toujours eu un petit truc avec le vert. Je dirais que c'est elle ma couleur préférée."

show lilly basic_satisfied_cas_close
with charachange


li "Le vert hein ? À quoi est-ce que tu penses quand tu vois cette couleur ?"


hi "Euh... L'herbe. Et les arbres en été. L’armée aussi, avec leurs tenues camouflage."

show lilly basic_planned_cas_close
with charachange


li "Les hommes aiment toujours l’armée."

show lilly basic_smile_cas_close
with charachange


li "Mais... ça semble être une belle couleur. Une très jolie couleur."


"Elle hoche légèrement la tête, comme pour approuver mon choix. Considérant à quel point le concept de couleur doit lui être étranger, le définir par association doit être suffisamment compréhensible."


hi "Si tout le monde a une couleur préférée, alors quelle est la tienne ?"

show lilly basic_smileclosed_cas_close
with charachange


li "Le blanc. On m'a dit que c’était la couleur de la neige, et de la crème glacée."


hi "Tu n'es pas meilleure que moi alors, si tu aimes cette couleur juste à cause des glaces. Mais je pense que le blanc est une bonne couleur aussi."


hi "En parlant de couleurs, il fera bientôt noir. Laisse-moi t'aider à te lever."

show lilly basic_smile_cas_close
with charachange

show lilly basic_smile_cas_close at center
with charamove


"Lilly m'offre sa main, que je prends dans la mienne pour l'aider à se lever. La douceur de sa main comparée à la mienne me surprend, je ne suis pas habitué à un tel contact physique."


"Ça ne semble pas la gêner cela dit. Bien que le pourquoi soit évident, ça a juste l'air d’être un autre trait distingué de sa personne."


"Alors qu'elle met sa main dans sa poche, je l’arrête dans son élan."


hi "Ne t’embête pas, je paye."

show lilly basic_cheerful_cas_close at center
with charachange


li "Oh. Merci, Hisao."


"Elle accompagne son remerciement d'un sourire, ce qui est une bien plus grande récompense que ses mots."

stop music fadeout 2.0

scene bg suburb_roadcenter_ni
with shorttimeskip

$ renpy.music.set_volume(0.2, 0.5, channel="ambient")
play ambient sfx_cicadas fadein 0.5


"Au moment où nous descendons du bus, il fait noir."

$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

scene bg school_road_ni
with locationskip


"Nous marchons le long de la colline en silence, en nous comportant tous les deux un peu étrangement, probablement à cause des évènements de la journée."


"Bien que je sois toujours un peu préoccupé par la réaction de Lilly après qu'elle ait parlé avec sa sœur, le fait que j'ai réussi à lui remonter le moral, même un peu, est une victoire."


"Mais... On dirait que l'air ambiant entre nous deux a changé. Peut-être seulement un peu, mais il y a quelque chose qu'aucun de nous deux n'avait réalisé auparavant."

show lilly cane_weaksmile_cas_ni at center
with charaenter


li "C’était... un rendez-vous, n'est-ce pas ?"


"Oui c'en était un. Et ça n'a échappé à aucun de nous deux."


"Aussi gênant que ce soit, je ne pense pas que ce soit une mauvaise chose. En fait, c'est plutôt le contraire. Je ne sais pas ce que c'est, je ne peux pas en être sûr, mais il semble que c'est un peu plus que de l'amitié."


"Compréhension ? Empathie ? Chercher les mots adéquats pour le décrire est difficile. Néanmoins..."


hi "Ça te dirait qu'on refasse ça une autre fois, Lilly ? Sans le shopping ?"

show lilly cane_emb_cas_ni
with charachange


"Ma question se heurte à la même expression de Lilly qu'auparavant. Sa peau pâle rend la teinte rosée de ses joues légèrement plus visible, et son regard, toujours droit et pointant vers l'horizon, est un peu plus bas. Juste un peu."

show lilly cane_cheerful_cas_ni
with charachange


li "...D'accord."

stop ambient fadeout 2.0

scene black
with dissolve




label fr_L4:

scene bg school_girlsdormhall
with locationchange

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")


"Mon cartable à la main, je marche le long du couloir du dortoir des filles."


"Une poupée est à l’intérieur, posée délicatement sur une petite boîte. J'ai cette boîte dans mon sac depuis un moment déjà, ne sachant pas vraiment quoi en faire."


"En y repensant, la situation est bizarre."


"Bien que je sache depuis un moment quand allait avoir lieu la fête d'anniversaire de Hanako, je n'avais aucune idée de comment allaient se passer la célébration jusqu’à ce que je trouve, plus tôt, un mémo laissé dans la salle où on boit du thé."


"Je la relis une deuxième fois, pour être sûr. L’écriture noire est tout à fait lisible malgré la cécité de Lilly et montre beaucoup d'efforts et d'attention."

window hide


$ written_note(u"Hisao,\n\nLa fête aura lieu dans ma chambre. Viens s'il te plaît à six heures dans la chambre 225 du dortoir des filles.\nDésolée de te l'annoncer de cette façon, mais j'ai mes obligations de déléguée de classe.\n\n- Lilly Satou", text_args={"color":"#000000"})

window show


"Peu rassuré, je continue de parcourir le dortoir jusqu’à la la porte de Lilly. J’hésite pendant une seconde, puis frappe trois fois à la porte."

play sound sfx_doorknock2
with Pause(0.5)


"Des voix peuvent être entendues de l’intérieur. En écoutant mieux, je reconnais les voix de Hanako et de Lilly."


"Alors qu'elles finissent, Lilly élève la voix."


li "C'est toi Hisao ?"


hi "Ouaip. J'ai eu le mémo que tu m'as laissé."


li "Tu peux entrer, la porte est ouverte."


"Content d'avoir trouvé la bonne chambre, je tourne la poignée et entre."

play sound sfx_dooropen


"Alors que la porte s'ouvre, mon salut est coupé dans son élan."

window hide

play music music_one fadein 10.0

scene ev lilly_bedroom:
    truecenter
    zoom 1.1 subpixel True
    ease 15.0 zoom 1.0
with GenericWhiteout(0.5,0.1,4.0)

window show


"Lilly, en pyjama, est assise à la table basse au centre de la chambre, tandis que de l'autre côté se trouve Hanako en chemise de nuit. Étant en uniforme scolaire, je me sens un peu à côté de la plaque."


"Je profite rapidement de la vision qui m'est donnée, j'ai du mal à détourner mon regard des longues, fines et pâles jambes de Lilly."


hi "S-salut. Je... crois que j'ai apporté tout ce dont on a besoin."

scene ev lilly_bedroom_large:
    xpos -130 ypos -400 subpixel True
    acdc_warp 12.0 ypos -800
with flash


"Elle sourit et hoche la tête. Je me demande si elle est consciente de la plaisante vue qu'elle m'offre. La fine soie bleu foncé de son pyjama lui va vraiment bien, accentuant à la fois ses yeux et ses courbes."


"Son expression d'hier soir, cette attitude presque timide, semble avoir été remplacée par son calme habituel. C'est bon de voir sa confiance revenue. Mais quand même, je n'arrive pas à chasser de mon esprit l'expression qu'elle avait."

scene ev lilly_bedroom_large:
    xpos -830 ypos -200 subpixel True
    acdc_warp 12.0 ypos 0
with flash


"Je regarde Hanako, qui est nerveusement assise en face d'elle dans sa robe. Ce n'est pas une surprise de la voir porter quelque chose de si traditionnel. Mais cela reste vraiment mignon."


hi "Salut, Hanako. Joyeux anniversaire."


ha "Ah... M-merci."


"Elle est encore plus timide que d'habitude, malgré le fait qu'elle soit de plus en plus à l'aise avec moi au fil des semaines qu'on passe ensemble. Elle doit se sentir mal à l'aise d'être au centre de l'attention."

scene ev lilly_bedroom
with flash


li "Assieds-toi, Hisao. Je vais vous verser du thé."


hi "D'accord."

$ renpy.music.set_volume(0.8, 2.0, channel="music")

scene bg school_dormlilly
with locationchange


"Lilly attrape la théière fumante et verse son contenu dans nos tasses, alors que je m'assois à leurs côtés, posant mon sac contre le mur."


"Mon calme retrouvé et mes hormones remises du choc, je réalise que c'est la première fois que je suis dans la chambre de Lilly."


"La première chose que je remarque est l'odeur ambiante, légèrement différente de celle de ma chambre... probablement un fond de parfum, ou de vernis à ongles. Ou un autre truc que les filles utilisent."


"Il y a aussi la nature vide de la chambre, visuellement. Les murs beiges, un placard sans fioritures, pas de posters sur les murs. Tout est ordonné, c'est quelque chose que j'aurais pu prévoir étant donné sa cécité."


"La seule chose sortant de l'ordinaire sont les piles de livres sur le sol, m'arrivant presque au genou. Certains d'entre eux ont des titres imprimés, d'autres n'ont que des points de braille."


"Le fait que ceux avec des titres imprimés soient tous en anglais est intéressant, bien que pas très étonnant. Elle a mentionné que ses parents avaient appris la langue à Akira et elle, après tout."


hi "Tu as une jolie chambre, Lilly."

show hanagown distant:
    center
    ypos 1.15
with charaenter


"J’entends un merci de sa part par-dessus mon épaule. Le regard de Hanako est fixé sur ses genoux et ses mains sont nerveusement pressées sur sa robe."


"C'est maintenant que je comprends pourquoi. Avec ces habits, ses cicatrices sont beaucoup plus visibles, descendant le long de sa nuque et couvrant son épaule droite."


"Bien que cette fête soit pour elle, elle n'a pas vraiment l'air de l'apprécier maintenant que je suis là."


hi "Et donc, ça te fait quel âge ? Dix-huit ?"


show hanagown worry
with charachange


"Son air surpris, qu'elle ne parvient pas à masquer par manque d'habitude, montre qu'elle essayait de m'effacer mentalement. C'est vraiment très gênant."


ha "O-oui."


hi "Le bon côté c'est que dans deux ans tu pourras boire. Et donc, qui est la plus vieille ? Lilly ou toi ?"

show hanagown normal
with charachange


ha "Lilly. Elle a eu son anniversaire en... f-février. Et... toi ?"


hi "C’était plus tôt cette année."


"Sans préciser qu'il est arrivé pendant que j’étais coincé à l’hôpital. C’était... un dur moment à passer."

show hanagown distant
with charachange

show hanagown distant:
    tworight
    ypos 1.15
show bg school_dormlilly at bgright
with charamove

show lilly basic_smileclosed_paj:
    twoleft
    ypos 1.2
with charaenter

play sound sfx_teacup


"La conversation avec elle se tarit aussi vite que ce à quoi je m'attendais. Lilly a fini de préparer nos thés, et s'assoit en les posant devant nous."


"Je prends ma tasse, remarquant immédiatement un arôme beaucoup plus fort que celui du thé habituel."


hi "Mh, il est différent du thé qu'on prend à l’école."

show lilly basic_smile_paj
with charachange


li "C'est une variété différente de l'autre. Tu n'as jamais goûté l'Orange Jaïpur ?"


hi "Pas... que je sache. Je bois du café d'habitude, comme quand on était en ville. C'est assez bon cela dit."

show hanagown normal
with charachange


"Alors que nous nous asseyons et buvons nos thés, Hanako semble plus relaxée, ou du moins, moins tendue qu'avant."


"Nous finissons tous nos tasses au même moment, Hanako ne réussissant pas à masquer son enthousiasme à l'idée de manger le gâteau qui est sur le côté, ne demandant que ça."

stop music fadeout 4.0


"En y pensant, j'ai faim aussi. Mais je dois faire autre chose en premier."


hi "Lilly ?"

show lilly basic_planned_paj
with charachange


li "Oui, maintenant est un bon moment."


"Sachant exactement ce que l'autre veut dire, je me penche sur le côté et fouille dans mon sac pour prendre la poupée que j'ai choisie pour Hanako, et Lilly se lève pour aller chercher son cadeau."


"Cachant nos cadeaux dans nos mains, nous lui mettons sur la table en même temps."

show lilly basic_cheerful_paj
show hanagown normal_blush
with charachange


$ doublespeak (li, hi, "Joyeux anniversaire !")


"Hanako reste assise en silence devant ses cadeaux pendant plusieurs secondes, par pure surprise."


"Ma petite poupée en bois, avec sa robe victorienne et son petit chapeau, est à côté de l'ours en peluche marron de Lilly."

show hanagown distant
with charachange


"Elle serre sa robe sans ses mains alors qu'elle essaye de parler, sans quitter des yeux ses modestes cadeaux."

show hanagown distant_blush
with charachange


ha "M... merci... Lilly et... Hisao..."

play music music_serene fadein 6.0

scene unlock_ev lilly_hanako_hug_end
show black
show ev lilly_hanako_hug:
    xalign 0.5 yalign 1.0 alpha 0.0 subpixel True
    parallel:
        linear 5.0 alpha 1.0
    parallel:
        easein 15.0 yanchor 0.0 ypos -0.15

with locationskip


"Sa voix devient fébrile alors que Lilly s'avance, l'enveloppant doucement de ses bras."


"La vue de Hanako serrant si fort Lilly dans ses bras réchauffe le cœur, tellement que je ne pourrais m’arrêter de sourire même si je le voulais."


"Alors que Lilly pose gentiment sa tête sur celle de Hanako, elle parle si silencieusement et doucement que je peux à peine l'entendre."


li "Joyeux anniversaire, Hanako."


hi "Joyeux anniversaire."


"Hanako hoche légèrement la tête, tenant encore Lilly pendant un moment avant de la lâcher et de se frotter un œil."


"Je suppose que pour Hanako, avoir une personne qui est là pour elle, n'importe qui, et qui l'aime, doit être spécial. Le fait que maintenant Lilly et moi pouvons partager ce rôle à deux est quelque chose dont je serai toujours heureux."

scene ev hanako_presents1
with locationskip


"Hanako prend délicatement la poupée et la peluche, les tenant tous deux dans ses bras alors qu'elle sourit chaudement."


"Pendant un long moment, nous restons simplement tous les trois, assis en silence. Le silence reste intact jusqu’à ce que la douce voix de Lilly le transcende."


li "Et si on s'occupait du gâteau, maintenant ?"

scene bg school_dormlilly
show lilly basic_smile_paj:
    twoleft
    ypos 1.2
show hanagown smile:
    tworight
    ypos 1.15
with locationskip


"Sa proposition est accueillie par deux visages gourmands."


hi "Pas d'objection pour ma part."


ha "D'accord."

stop music fadeout 2.0

scene bg school_dormlilly
show lilly basic_smileclosed_paj:
    twoleft
    ypos 1.2
show hanagown normal:
    tworight
    ypos 1.15
with shorttimeskip


hi "Pfiou, c'était bon."

play music music_dreamy fadein 4.0


"Je m'avachis un peu, repu, Lilly et Hanako ayant l'air aussi satisfaites que moi. Ça nous a demandé certains efforts, mais on a réussi à finir le gâteau entièrement."

show hanagown normal_blush
with charachange


ha "Je ne pourrais pas prendre une bouchée de plus."

show lilly basic_weaksmile_paj
with charachange


li "La prochaine fois, je prendrai un plus petit gâteau."

show hanagown smile
with charachange


"Hanako et moi sourions, mais je ne peux pas m’empêcher de penser que l’année prochaine, on aura notre diplôme."


"Ce fait est quelque peu déprimant, maintenant que j'ai enfin l'impression que ma vie commence à rentrer dans l'ordre. Plus ou moins."


"Balayant du regard la chambre ordonnée de Lilly, ses livres attirent encore une fois mon attention."


"C'est peut-être un peu impétueux, mais ma curiosité prend le dessus. De toute façon, je ne pense pas que ça la gênera."


hi "Hé Lilly, ça te gêne si je jette un coup d’œil à un de tes livres ?"

show lilly basic_smile_paj
with charachange


li "Fais donc, Hisao."

show lilly basic_planned_paj
with charachange


li "Cela dit, si tu arrives à surmonter deux barrières linguistiques, je serai impressionnée."


hi "Deux ? Braille et... ah, oui, l'anglais."

show lilly basic_smile_paj
with charachange


"Elle hoche la tête."


hi "Je savais que tu étudiais l'anglais, mais je suis toujours impressionné par le fait que tu sois aussi douée que ça."

show lilly basic_giggle_paj
with charachange


li "Certains diraient que c'est une bonne technique pour éviter qu'on emprunte ma collection."


"Elle dit ça sans y prêter attention, mais je suis un peu déçu. Avoir tous ces livres autour de moi sans aucun moyen de les lire me frustre un peu."


"Hanako rit silencieusement alors que j'atteins la pile la plus proche, balayant du regard la couverture. “Death on the Nile”, en lettres capitales sur la couverture, est le seul texte imprimé du livre."

$ renpy.music.set_volume(0.5, 0.5, channel="music")
play sound sfx_paper
show ev braille at Fullpan(10.0, dir="right")
with locationskip


"Je m'assois pendant un moment avec le livre ouvert sur mes genoux pendant que Lilly et Hanako parlent entre elles."


"J'essaye de sentir les points de Braille imprimés sur les pages, mais ils semblent se mélanger les uns aux autres avant de devenir indistincts."


"Je pensais que ça serait plus facile que ça. Avec un peu de pratique, je pense que quelqu'un avec un meilleur sens du toucher que moi peut réussir à lire plutôt vite."

$ renpy.music.set_volume(1.0, 0.5, channel="music")

scene bg school_dormlilly
show lilly basic_smileclosed_paj:
    twoleft
    ypos 1.2
show hanagown normal:
    tworight
    ypos 1.15
with locationskip


"Remarquant un silence probablement là depuis un moment, je lève la tête et vois Lilly souriant alors que Hanako sirote une autre tasse de thé."


hi "Quelque chose ne va pas ?"

show lilly basic_smile_paj
with charachange


li "C'est tout l'inverse, ta curiosité est plaisante."


"Je suis content de son compliment, et je sens même la chaleur me monter aux joues."


hi "Merci, mais je suis juste comme ça."

show lilly basic_weaksmile_paj
with charachange


li "Pour être honnête, je n’étais pas sûre de la façon dont tu nous voyais, vu que tu es un étudiant transféré d'une autre école."

stop music fadeout 12.0

show lilly basic_reminisce_paj
with charachange


li "Si tu nous avais prises en pitié, j'aurais été offensée."

show hanagown distant
with charachange


"Il y a un certain tranchant dans la voix de Lilly, sûrement de la fierté même. Hanako semble être plus recluse que d'habitude, regardant Lilly plutôt que moi."


hi "Je n'aurais pas fait ça. Vu ma situation, je suis peut-être la dernière personne qui prendrait les autres en pitié."


hi "La première réaction de mes parents après ma crise cardiaque... Je ne souhaite à personne de voir cette expression."

show lilly basic_oops_paj
show hanagown distant_blush
with charachange


"Je me retiens d'aller plus loin, mais c'est déjà trop tard. Les deux filles semblent déjà être gênées, surtout Lilly."

show lilly basic_emb_paj
show hanagown worry
with charachange


li "Je... suis désolée. Je n'aurais pas dû aller aussi loin..."

show lilly basic_listen_paj
with charachange

$ renpy.music.set_volume(0.5, 0.0, channel="sound")
play sound sfx_doorknock2


"Le temps de quelques secondes, un silence gênant s'installe, heureusement interrompu par Lilly qui tourne la tête d'une façon que je reconnais maintenant facilement."


hi "Tu entends quelque chose ?"

show lilly basic_surprised_paj
with charachange


li "La porte..."

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_dooropen

show lilly basic_surprised_paj:
    left
    ypos 1.2
show hanagown distant_blush at Transform(xpos=0.4)
show bg school_dormlilly at bgleft
with charamove


"Faisant confiance aux sens de Lilly, tout le monde regarde vers la porte. Et comme prévu, la poignée de la porte se tourne puis un flash jaune et noir entre."

show akira basic_laugh at right
with easeinright

play music music_running

show lilly basic_listen_paj
show hanagown worry
with vpunch


aki "Akira Satou est dans la place ! Joyeux anniversaire Hanako !"

show hanagown worry_blush
with charachange


ha "Ah... merci..."

show akira basic_smile at Transform(ypos=1.15, xpos=0.8, xanchor=0.5)
with dissolvecharamove


"Akira s'assied à la table et pose son sac à côté d'elle. Elle est un peu excentrique et sait se faire bien remarquer quand elle entre."

show hanagown distant
with charachange


"Hanako tire sur sa robe pour se rendre présentable, mais ne semble pas être trop secouée par l’entrée d'Akira. J'imagine qu'elle l'avait déjà rencontrée avant, ce qui n'est pas surprenant sachant à quel point Akira et Lilly sont proches."


"Akira ne semble pas être repoussée par les cicatrices de Hanako, malgré leur importance, et semble aussi ne pas prendre de gants dans sa façon d'agir malgré la nature timide de Hanako."

show lilly basic_weaksmile_paj
with charachange


li "Je croyais que tu avais du travail, Akira. Tu as réussi à trouver du temps pour venir ?"

show akira basic_boo:
    ypos 1.15
with charachange


aki "Plus ou moins. Je n'aime pas trop le fait que les autres soient encore en train de faire des heures sup', alors je reste pas longtemps."

show akira basic_smile
with charachange


aki "Mais je me sentais aussi mal à l'idée de louper l'anniversaire de la jolie petite Hanako, alors pour l'instant je suis là."

show hanagown smile
with charachange


"Elle fait un grand sourire à Hanako, qui rougit fortement en regardant par terre. Sa bouche semble trembler comme si elle essayait de cacher un sourire embarrassant."


"C'est un peu étrange de voir comment sa réaction semble être plus spontanée que lorsqu'elle est embarrassée par son physique. Tout ce qu'elle réussit à faire, c'est hocher légèrement la tête."


"J'imagine que peu de personnes peuvent la faire sourire. Je respecte la façon dont Akira arrive à la gérer, la rendant heureuse, en comparaison du peu que je peux faire."

show akira basic_laugh
with charachange


aki "Maintenant, avant d'y aller..."

play sound sfx_rustling


"Elle attrape son sac derrière elle et sort son contenu."

show wine:
    yalign 0.5 xanchor 0.0 xpos 1.0 alpha 0.0
    easein 1.0 alpha 1.0 xanchor 1.0
with Pause(1.0)


"Elle en sort deux grandes bouteilles en verre, toutes les deux avec des noms français sur l’étiquette."

show hanagown normal
with charachange


"Un mélange de surprise et de curiosité se lit sur le visage de Hanako, et je ne pense pas que le mien soit différent. Lilly, ne voyant pas ce qui se passe, ne peut comprendre la situation."

show hanagown normal_blush
with charachange


ha "Akira... c'est..."

show lilly basic_surprised_paj
with charachange


li "Qu'est-ce que c'est ?"


hi "Du vin. Un rouge et un blanc."

show lilly basic_pout_paj
with charachange


li "A-Akira ! C'est... !"

show akira basic_smile
with None

show wine:
    easeout 1.0 alpha 0.0 xanchor 0.0
with Pause(1.0)

hide wine
with None


aki "Détends-toi, détends-toi, c'est pas comme si Shizune était là pour te réprimander."


hi "Lilly n'a pas tort, ce n'est pas autorisé sur le campus."


hi "...ou autre part d'ailleurs. On est toujours trop jeunes pour boire, tu te rappelles ?"

show akira basic_laugh
with charachange


aki "Tu parles trop pour quelqu'un qui bave pratiquement en voyant la bouteille."


"Elle n'a pas tort là. J'aimerais bien essayer un peu, même juste un petit peu. Bien que Hanako n'ait pas une bouteille à la main comme moi, elle a tout autant l'air d'avoir envie que moi."

show lilly basic_displeased_paj
with charachange


"Lilly se frotte le front, abandonnant le combat sachant qu'Akira gagnera en ignorant simplement ces “règles” et “lois” risibles."

show lilly basic_displeased_paj
with charachange


li "Ne dis pas un mot de tout ceci à quelqu'un de l’école s'il te plaît."

show akira basic_smile
with charachange


aki "Je ne suis pas idiote, ne t’inquiète pas."

show akira basic_boo
with charachange


aki "Cela dit, je vais devoir retourner travailler."

show lilly basic_oops_paj
with charachange


li "Déjà ? Mais tu viens juste d'arriver..."

show akira basic_resigned
with charachange


aki "Désolée Lilly. Contente de vous avoir vues toutes les deux. Toi aussi Hisao."


hi "À plus tard, alors."


ha "Euh... a-au revoir... Akira..."

show akira basic_resigned at Transform(yalign=1.0)
with charamove

hide akira
with charaexit


"Elle se lève avec un grognement et sort de la chambre, nous laissant avec les deux cadeaux sur la table."

show lilly basic_oops_paj:
    twoleft
    ypos 1.2
show hanagown normal_blush:
    tworight
    ypos 1.15
show bg school_dormlilly at center
with charamove


hi "...Intéressant."

show lilly basic_arablush_paj
show hanagown normal
with charachange


"Lilly émet un petit rire nerveux à cause des agissements de sa sœur tandis que Hanako prend une bouteille en main."

show hanagown distant_blush
with charachange


ha "Donc..."


hi "Qu'est-ce que tu en penses, Lilly ?"

show lilly basic_weaksmile_paj
with charachange


"Elle pose son coude sur la table et se frotte le nez en réfléchissant. Elle ne semble vraiment pas capable de rivaliser avec sa sœur."

show lilly basic_smile_paj
with charachange

stop music fadeout 3.0


li "Ben... elles sont là. Autant se servir un peu..."


"Je n'attends pas pour jeter un œil autour de moi et trouver des verres."

scene bg school_dormlilly_ni
with shorttimeskip

play music music_night fadein 0.5


"Un petit grognement me rappelle que Lilly est partie dans son lit pour se reposer il y a quelques minutes."


"Quasiment vidé de mon énergie, je réussis à me lever et me traîner jusqu'au lit, posant mon dos contre celui ci."

show bg school_dormlilly_ni as ovl1:
    xalign 0.5 alpha 0.4 yalign 0.5 zoom 1.0
    ease 1.0 xalign 0.55 alpha 0.5 rotate 1 zoom 1.05
    ease 1.0 xalign 0.5 yalign 0.5 alpha 0.0 rotate 0 zoom 1.0

show bg school_dormlilly_ni as ovl2:
    xalign 0.5 alpha 0.4 yalign 0.5 zoom 1.0
    ease 1.0 xalign 0.45 alpha 0.5 rotate -1 zoom 1.05
    ease 1.0 xalign 0.5 yalign 0.5 alpha 0.0 rotate 0 zoom 1.0


hi "Mon dieu."

show lilly basic_listen_paj_ni:
    center
    ypos 1.2
with charaenter


li "Eurgh..."


"Le grognement de Lilly semble être sans vie."


hi "Trop bu ?"

show lilly basic_concerned_paj_ni
with charachange


li "Ma tête me fait mal."


hi "Ouais, trop bu."


"Je pose ma tête et regarde le plafond. Un désastre total."


"Comme des idiots, nous avons bu toute la soirée, un verre après un autre. Hanako s'est simplement écroulée sur le côté, endormie, et c'est un miracle que je ne me sente pas malade comme Lilly."

show lilly basic_sad_paj_ni
with charachange


li "Hé, Hisao ? Désolée pour aujourd'hui. Je... ne pensais pas que ça allait arriver."


hi "C'est pas grave Lilly, pour être honnête, je me suis beaucoup amusé aujourd'hui."

show lilly basic_weaksmile_paj_ni
with charachange


li "Vraiment ?"


hi "Oui. Je crois que Hanako aussi. Non, j'en suis même sûr."

show lilly basic_reminisce_paj_ni
with charachange


"Il y a un petit silence, avant qu'un autre grognement ne provienne de Lilly, alitée."


hi "Ça va ?"

show lilly basic_weaksmile_paj_ni
with charachange


li "Comme tu l'as dit, j'ai juste trop bu. Quelle heure est-il ?"


hi "L'heure ? Euh, il est..."


"Je regarde rapidement ma montre, les chiffres sont à peine lisibles dans l’obscurité."


hi "À peu près minuit."

show lilly basic_concerned_paj_ni
with charachange


li "L'heure du couvre-feu est passée alors."


hi "Ouais, je m'en doutais. On va devoir dormir ici cette nuit."


"Aussitôt dit, j’entends les draps bouger alors que Lilly se redresse."

show lilly basic_oops_paj_ni
with charachange


li "Hanako..."


hi "Ah, non, reste couchée, n'essaye pas de te lever."

show lilly basic_displeased_paj_ni
with charachange


li "Hisao, je dois..."


hi "Tu es dans un plus mauvais état que moi. Repose-toi."

show lilly basic_oops_paj_ni
with charachange


li "Mais pour..."


hi "Je vais prendre des couvertures et les mettre sur elle, ne t’inquiète pas."

hide lilly

with charaexit


"Alors que je laisse échapper un grand bâillement et que je me lève pour aller chercher les couvertures, j’entends Lilly se recoucher avec un petit boum sur le lit."


li "Merci, Hisao."


hi "Pas de problème, c'est le moins que je puisse faire. Tu as l'air complètement épuisée."


li "Je ne suis pas... épuisée... juste un peu... fatiguée."


"Elle commence à faire la moue, une légère distorsion dans sa voix se fait entendre à cause de l'alcool. J'attrape quelques couvertures pliées au bout de son lit."


"Marchant silencieusement jusqu’à Hanako, je place avec précaution les couvertures sur elle, m'assurant de ne pas la réveiller."


"Quoi que je fasse,je doute de pouvoir la réveiller, vu la forte odeur d'alcool se dégageant de son souffle.."


"Je me redresse et jauge la situation."

stop music fadeout 4.0


"Deux filles, toutes deux très ivres, et un gars dormant dans la chambre de l'une d'entre elles. Quel scandale ça ferait, si ça venait à se savoir."


"Alors que je vais me rasseoir à côté du lit, je jette un dernier coup d’œil à Lilly."


"Elle est étendue là, quelque peu contorsionnée, se reposant paisiblement."


"Je m'accroupis pour mieux la voir."

play music music_comfort

scene ev lilly_sleeping:
    truecenter zoom 1.05 subpixel True
    acdc_warp 20.0 zoom 1.0
with locationchange


"Sa peau blanche se confond avec l'oreiller, un air paisible sur son visage endormi."


"D'habitude elle semble si empathique et directe, toujours là et prenant soin de Hanako. Maintenant, elle semble tout ce qu'il y a de plus délicat."


"Je repense aux cadeaux de Hanako."


"Je m'attendais à ce que ce soit une belle fête pour elle, mais je ne pensais pas que ce serait aussi mouvementé."


"Un anniversaire après l'autre, année après année."


"Juste Lilly et elle, toutes seules."


"...Je pense que ce n'est pas juste les cadeaux qui lui ont fait plaisir."

scene bg school_dormlilly_ni
with locationchange


"Me résignant à dormir confortablement, je m'assois sur le côté du lit une fois de plus."


li "Hé, Hisao."


"La voix de Lilly est si faible que je peux à peine l'entendre. Elle doit être sur le point de s'endormir."

scene ev lilly_sleeping:
with locationchange


hi "Ouais ?"

scene ev lilly_sleeping_smile
with charachange


li "Merci."


hi "Merci ? Pourquoi ?"


li "Pour être là."


hi "...C'est rien."

scene bg school_dormlilly_ni
with locationchange


"Entendant une respiration profonde, il est évident que Lilly s'est endormie."


"Après avoir fermé les yeux, il ne me faut pas longtemps pour m'endormir à mon tour."

stop music fadeout 2.0

window hide

scene black
with shuteye



label fr_L5:

window hide None

scene black
with Pause(4.0)

stop music

window show


mystery "Hisao ?"


mystery "Hisao, est-ce que... ?"


"La douce et à peine audible voix, parvenant à mes oreilles, me réveille doucement. J'aimerais être réveillé comme ça plus souvent."


"Avec un marmonnement, j'ouvre doucement mes..."

scene bg school_dormlilly
show lilly superclose
with openeye_shock

show lilly superclose_shock
with Dissolve(0.2)


$ doublespeak(hi, li, "Wah !", "Ah !")

play sound sfx_impact2

show lilly superclose_ouch
with vpunch

show lilly basic_concerned_paj:
    xalign 0.5 yanchor 1.0 ypos 1.2
    ease 0.4 ypos 1.4
with Dissolve(0.2)


"Surpris par le visage de Lilly, se tenant étrangement à quelques millimètres du mien, je réagis brusquement et nos têtes s'entrechoquent. L'impact de nos fronts nous fait tomber sur le dos et gémir de douleur, Lilly ayant l'air d'un jouet couinant."


hi "Aïe, aïe, aïe."

play music music_happiness fadein 6.0


"Je me frotte doucement le front d'une main. Lilly est allongée devant moi, son visage visiblement endolori."


hi "Ah... désolé. Ton visage était plutôt proche du mien et j'ai réagi par réflexe. Ça va ?"

show lilly basic_concerned_paj:
    ease 1.0 ypos 1.2
with Pause(0.5)


li "Ma tête..."


"On dirait qu'elle ne va pas très bien. En y pensant, je doute que ce soit juste l'impact qui lui cause ce gros mal de tête."


hi "Gueule de bois ? Tu as pas mal bu hier."

show lilly basic_sad_paj:
    ypos 1.2
with charachange


"Pendant que je me lève, elle hoche silencieusement la tête pour confirmer."

show lilly basic_concerned_paj:
    ease 1.0 ypos 1.0
with Pause(0.5)


"Je lui offre une main, et l'aide à se mettre sur ses pieds. Regardant derrière elle, je vois Hanako toujours endormie."

show lilly basic_reminisce_paj at center
with charachange


li "C'est pas juste... J'ai bu autant que toi..."


hi "C'est très différent de ce dont je me rappelle. Et de toute façon, les filles tolèrent moins bien l'alcool que les hommes."

show lilly basic_displeased_paj
with charachange


li "Ça n'aide pas."


hi "Bon, je vais te chercher un verre d'eau. Fais juste attention à ne pas trébucher sur Hanako."

hide lilly
with charaexit


"Je me frotte les yeux, et vais jusqu'au lavabo. Aider quelqu'un qui a la gueule de bois n'est pas la façon rêvée de passer une matinée."


"Le verre se remplit en quelques secondes, l'eau claire reflétant le fil de lumière qui passe à travers les rideaux."


"Lilly s'est assise sur le côté du lit. Je marche jusqu’à elle en prenant soin de ne pas heurter Hanako qui dort paisiblement, et mets le verre d'eau dans ses mains tendues."

show lilly basic_weaksmile_paj_close:
    center
    ypos 1.2
with charaenter


li "Merci."


hi "Pas de problème."

stop music fadeout 12.0


"Je m'assois à côté d'elle, le lit étant étonnamment confortable."


"Elle boit lentement et méthodiquement. Un moment de silence se passe, avec pour seul bruit le souffle de Hanako."

show lilly basic_reminisce_paj_close
with charachange


"Avec une légère culpabilité, je regarde le visage de Lilly et essaye de lire son expression. Ses sourcils sont légèrement froncés, et elle semble perdue dans ses pensées."

show lilly basic_emb_paj_close
with charachange


"Pendant un moment j’hésite, mais place finalement ma main sur son épaule pour la rassurer. Je ne m'attendais pas à ce qu'elle sursaute, cela dit."


hi "Ah, désolé. Je ne voulais pas—"

show lilly basic_sad_paj_close
with charachange


"Lilly secoue la tête, un peu plus rapidement que d'habitude."


"Elle prend une grande inspiration pour se ressaisir avant de prendre la parole."

show lilly basic_weaksmile_paj_close
with charachange


li "Je dois être affreuse à voir..."


"J'envisage de protester, mais réalise rapidement que ça serait une chose futile à faire. Mais quand même, je voudrais qu'elle s'ouvre un peu plus."


hi "Si tu veux parler de quelque chose, je suis là."

show lilly basic_displeased_paj_close
with charachange


"Lilly laisse échapper un petit soupir, comme pour se moquer d'elle-même."

show lilly basic_reminisce_paj_close
with charachange


li "C'est juste que... beaucoup de choses arrivent en même temps."

show lilly basic_sad_paj_close
with charachange


li "Je suis désolée d’être si étrange ces temps-ci, surtout quand on était en ville. Même maintenant je suis toujours un peu confuse."


hi "Crois-moi, je vois de quoi tu parles."

show lilly basic_weaksmile_paj_close
with charachange


"Elle sourit d'un air rêveur, reposant sa joue sur sa main."


li "On est deux jeunes idiots complètement cassés, hein ?"


hi "Allez, dis pas ça. Une fois notre diplôme en main, on retournera dans le monde réel."


"Le monde réel ? Des fois je me surprends moi-même à penser ce genre de chose. J'imagine que Yamaku et ses environs, comparés au reste du monde, me semblent toujours étranges."


"Peut-être que je ne m'y ferai jamais. C'est étrange en y repensant, être isolé de la société comme ça, ce n'est pas si mal. Un drôle de sourire sur son visage, Lilly semble partager la même idée que moi."


"Finalement, son sourire s'efface."

show lilly basic_displeased_paj_close
with charachange


li "Je vais retourner en Écosse pour une semaine ou deux, bientôt."


hi "C'est pour ça qu'on a dû reprogrammer l'anniversaire de Hanako ?"


"Elle hoche la tête."


hi "Tu pourras revoir ta famille au moins. Tu n'en as pas envie ?"

show lilly basic_concerned_paj_close
with charachange


li "Je n'ai pas revu ma famille depuis six ans. Je ne sais même pas comment agir avec eux maintenant."


"Attends... quoi ? Je reste bouche bée alors que j'essaie d'analyser ce qu'elle a dit."

play music music_moonlight fadein 6.0


"Si elle a dix-huit ans, ça veut dire qu'elle n'avait que douze ans quand ils sont partis. J'ai beau avoir assez peu vu mes parents, vu qu'ils travaillaient beaucoup, mais ça..."


"Je me sens bête alors que je cherche une façon de répondre."


hi "C'est... mais, pourquoi ?"

show lilly basic_reminisce_paj_close
with charachange


li "Pourquoi ils sont partis, ou pourquoi ils nous invitent Akira et moi ?"


hi "Les deux, j'imagine."

show lilly basic_sleepy_paj_close
with charachange


li "L'entreprise de mon père a sa maison-mère en Écosse, et on lui a proposé un bon poste là-bas. Et en fin de compte, il a dû déménager."


li "Ma mère l'a suivi, mais Akira et moi sommes restées au Japon pour le travail d'Akira dans la branche japonaise de l'entreprise de mon père, et pour mon éducation."

show lilly basic_concerned_paj_close
with charachange


li "Et pour l'autre question... une de mes tantes est gravement malade."


hi "Ah. Désolé..."

show lilly basic_weaksmile_paj_close
with charachange


li "Ne le sois pas. C'est étrange, vraiment, on nous demande d'y aller pour elle, alors qu'on la connaît à peine. Je ne peux même pas me rappeler le son de sa voix."


"Le plus étrange est le total manque d'antipathie qu'elle ressent envers sa famille pour avoir fait une chose pareille. Je ne peux pas m'empêcher de me sentir un peu mal à l'aise."


"Cela dit, son attitude est juste là pour cacher ses émotions. La voir comme ça me rend triste."

stop music fadeout 5.0


"Sachant quoi faire, je me lève du lit. Lilly remarque mes mouvements, penchant sa tête et approchant sa main pour sentir où j’étais."

show lilly basic_oops_paj_close
with charachange


li "Hisao... ?"

play sound sfx_rustling


"Je vais jusqu’à mon sac, toujours contre le mur. Ouvrant la poche principale et en sortant le sac opaque, je prends la petite boîte en bois dans mes mains."


hi "Ouvre les mains, Lilly."

show lilly basic_surprised_paj_close
with charachange


"Elle a l'air surprise mais acquiesce."

show lilly basic_surprised_paj_close:
    ease 1.0 xpos 0.4
show bg school_dormlilly:
    center
    ease 1.0 xpos 0.4
with Pause (1.0)

show musicbox closed behind lilly:
    alpha 0.0  zoom 0.5  xanchor 0.0 xpos 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.6 alpha 1.0
show boxstrip behind lilly:
    alpha 0.0  zoom 0.5  xanchor 1.0 xpos 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.6 alpha 1.0
with Pause (1.0)


"Je suis amusé de voir son expression curieuse quand je place la boîte à musique dans ses mains, sa façon délicate de la tenir comme si c’était la chose la plus fragile du monde."

stop music fadeout 2.0


"Elle passe ses doigts sur la boîte sans dire un mot, essayant de comprendre sa nature."


"Finalement ses doigts trouvent la faille du couvercle, et elle le soulève."

show musicbox open:
    xpos 0.5 ypos 0.6 alpha 1.0
with charachange

play music music_musicbox


"Je m'assieds à côté d'elle sur le lit, regardant son visage intensément."


"Elle reste là à écouter la petite mélodie, sa bouche légèrement ouverte."

show musicbox closed
show lilly basic_smileclosed_paj_close:
    xpos 0.4
with charachange

play sound sfx_switch
stop music

show musicbox closed:
    ease 1.0 ypos 0.7 alpha 0.0
show boxstrip:
    ease 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

show lilly basic_smileclosed_paj_close:
    ease 1.0 xpos 0.5
show bg school_dormlilly:
    ease 1.0 center
with Pause (1.0)

hide musicbox
hide boxstrip


"Il lui faut un long moment avant qu'elle ne referme le couvercle avec un petit clac, coupant court à la musique jouant dans ses mains."


"Le sourire sur son visage, gentil et rêveur, montre que j'ai fait le bon choix."


hi "Penses-y comme un cadeau d'au revoir pour ton voyage en Écosse."

show lilly basic_smile_paj_close:
    xpos 0.5
with charachange


li "Oui..."

play sound sfx_rustling

show lilly basic_smile_paj_close:
    twoleft
    ypos 1.2
show bg school_dormlilly at bgleft
with charamove


"Un gigotement peut se faire entendre sur le sol devant nous, le bruit ayant réveillé Hanako."

show hanagown distant:
    tworight
    ypos 1.3
    easein 1.0 ypos 1.1
with Dissolve(1.0)


"Elle sort des couvertures que j'avais mises sur elle, étant toute barbouillée et se frottant les yeux."


hi "Je vois que tu es enfin réveillée."

show hanagown normal:
    ypos 1.1
with charachange


ha "Mmh ? Quoi ?"

show lilly basic_planned_paj_close
with charachange


"Hanako regarde autour d'elle avec les yeux à moitié ouverts, son cerveau encore endormi. Son état second nous fait rire, Lilly et moi."

show lilly basic_planned_paj_close:
    ease 1.0 twoleft
with Pause(1.0)

show lilly basic_planned_paj at twoleft
with charadistant


"Alors que Lilly sort du lit et se dirige vers Hanako, je jette un dernier coup d’œil à la chambre."


hi "Je crois que je vais y aller, alors. Je vais avoir droit à des questions si on me voit sortir du dortoir des filles le matin."

show lilly basic_smile_paj
with charachange


li "Au revoir, Hisao."

show hanagown smile
with charachange


ha "Oh... Au revoir."


"Je me lève et marche jusqu’à la porte, attrapant mon sac plus léger en chemin."

scene bg school_girlsdormhall
with locationchange


"Une fois dans le couloir, j’entends les pas de Lilly derrière moi."


hi "Mmh ? Qu'est-ce qu'il y a ?"

show lilly basic_smileclosed_paj_close:
    yalign 1.0 xpos 0.3 xanchor 0.5
    easein 1.0 xpos 0.5
with Dissolve(1.0)


"Sans un mot, elle arrive vers moi. Je me fige alors que je sens sa main passer sur ma joue, tous mes nerfs s'imbibant de la sensation de ses doigts et de sa paume sur moi."

play music music_romance


"Juste après, son visage s'approche lentement du mien, puis un léger, momentané toucher de ses lèvres sur mon autre joue."


"Pendant un moment, tout semble gelé. J’amène sans y penser mes doigts sur ma joue, comme pour essayer de revivre la sensation."


hi "Lilly..."

show lilly basic_smile_paj_close at center
with charachange


li "C'est mon remerciement, Hisao."


hi "Remerciement... ?"

show lilly basic_cheerful_paj_close
with charachange


li "Pour ton cadeau. Passe une bonne journée à l’école."

show lilly basic_cheerful_paj_close:
    easeout 1.0 xpos 0.3 alpha 0.0
with Pause(1.0)

hide lilly
with None


"Et sur ce, elle disparaît derrière sa porte et la referme. J'entends les voix étouffées de Hanako et Lilly à travers, comme hier soir."

"…"


"...Je crois que ça va être dur de ne pas passer une bonne journée après ça."

show bg school_courtyard
with locationskip


"Je marche avec un certain entrain. Je crois qu'il y a des gens autour qui m'ont vu sortir du dortoir des filles, mais je m'en moque complètement."

stop music fadeout 2.0

scene black
with dissolve



label fr_L6i:

scene black
with None


mi "Hicchan~."


hi "Va-t'en."


mi "Hicchan~."


hi "Laisse-moi tranquille."


mi "Allez, Hicchan~."


hi "Hmph, laisse-moi dormir."


"Après deux nuits sans fermer l'œil, incapable de dormir, la dernière chose dont j'ai envie, c'est d'être réveillé maintenant que j'ai réussi à m'endormir."


"C'est peut-être la dernière heure de cours, avec un cahier comme oreiller, mais n'importe quoi m'irait tant que je peux dormir."



mi "Tu vois Hicchan, même Shicchan veut que tu te réveilles~ !"


"Je me moque de ce que veut Shizune, laisse-moi tranquille."


mi "Roh, Hicchan, je vais devoir..."


"Attends, Misha va... ?"


mi "...te réveiller..."


"C'est pas bon !"

play music music_running

scene bg school_scienceroom
show misha hips_grin_close at center
with vpunch


hi "JE SUIS DEBOUT ! JE SUIS DEBOUT ! TU N'AS... pas à..."


"Je peux sentir le rouge me monter aux joues."


"Les étudiants toujours en classe regardent l'idiot qui vient de crier alors qu'il dormait quelques instants auparavant."


hi "...Et merde."

play sound sfx_impact2
with vpunch


"Je laisse ma tête retomber sur la table avec un boum."

show misha cross_laugh_close
with charachange


mi "Wahahahahaha~ !"


"Le rire incontrôlé de Misha résonne dans toute la classe."

show shizu invis behind misha:
    center
    xpos 0.95
with None

show misha hips_grin_close at twoleft
show shizu adjust_happy at tworight
show bg school_scienceroom at bgleft
with dissolvecharamove


"Alors que je tourne mes yeux injectés de sang vers Shizune qui se trouve derrière elle, je la vois qui ajuste avec précaution ses lunettes, essayant désespérément de maintenir un air de désapprobation."


"En me concentrant, je peux voir un sourire mal dissimulé se dessiner sur son visage."


hi "Tu quoque, Shizune ?"


show shizu behind_blank
with Dissolve(0.3)


"Arrivant à peine à se contrôler, Shizune regarde dans une autre direction rapidement, en croisant les bras."

show misha cross_laugh_close
with charachange


mi "Wahahahahahaha~ !"


"Le rire de Misha double de volume en voyant Shizune. Tout ce que je peux faire c'est me plaquer la main sur le visage, en signe de résignation."


hi "Vous deux..."

show misha sign_smile_close
with charachange


mi "C'était qui, qui dormait en classe, Hicchan~ ?"


hi "Ouais, ouais, c’était moi."

show misha hips_frown_close
with charachange


mi "Pauvre Shicchan qui faisait de son mieux pour te réveiller. N'est-ce pas ?"

show shizu basic_angry
with charachange


"Je regarde de nouveau vers Shizune qui, avec un simple haussement d’épaules en guise de confirmation, se retourne avec les bras croisés."


hi "Pourquoi est-ce que Shizune essayait de me réveiller ?"

show misha hips_smile_close
with charachange


mi "Shicchan voulait te donner les polycopiés que le professeur remplaçant a distribués pendant que Hicchan dormait."


hi "Polycopiés ?"

play sound sfx_paper
show shizu behind_frown_close
show misha hips_frown_close
show blanknote at truecenter
with vpunch


"Je me retrouve soudainement avec deux feuilles de papier devant mon visage."

show blanknote at Transform(xpos=0.3)
with charamove


"Suivant la main qui les tient, je vois le visage toujours boudeur de Shizune, me regardant avec une mine renfrognée. Je pense que je suis en tort là."


hi "...Ah. Euh, désolé pour tout à l'heure."

stop music fadeout 8.0


"Loupé. Elle continue d'afficher une expression énervée. Je joins les mains et baisse la tête pour m'excuser."


hi "Vraiment, vraiment désolé."

show shizu behind_frustrated_close
with charachange

show blanknote:
    easeout 0.5 ypos 0.8 alpha 0.0
with Pause(0.5)

hide blanknote
with None


"Elle souffle et laisse simplement tomber les papiers sur mon bureau."


hi "Zut."

show shizu adjust_angry_close
show misha sign_smile_close
with charachange


"Je relève la tête pour voir Shizune et Misha en train de s'échanger des signes, un air de frustration sur le visage de Shizune."

show shizu basic_angry_close
with charachange


shi "... !"


"On dirait que c'est plus une tirade qu'un dialogue, ponctuée par des regards dans ma direction. C'est plus que troublant."


hi "Um..."

show shizu behind_frown_close
show misha hips_frown_close
with Dissolve(0.3)


"Elles arrêtent toutes les deux de faire des signes et me regardent à l’unisson, ayant toutes deux le même regard de désapprobation. En un mouvement, la main de Misha se place au-dessus de moi et descend à toute vitesse."

scene black
with None

play sound sfx_impact2
play music music_running


"Avant que je puisse espérer réagir, ma tête est propulsée vers le bas comme une enclume." with vpunch


"Je mets mes mains sur la tête, plus par réflexe que par réelle douleur."


hi "Aïe ! Pourquoi t'as fait ça ?!"

scene bg school_scienceroom at bgleft
show shizu adjust_smug_close at tworight
show misha hips_grin_close at twoleft
with openeye


"J'ouvre les yeux pour les voir toutes les deux en train de sourire et d’échanger des pouces levés."

show misha hips_smile_close
show shizu behind_smile_close
with charachange


mi "Shicchan dit qu'elle te pardonne maintenant, Hicchan~ !"


hi "Est-ce que tu pourrais pardonner avec un peu moins de force la prochaine fois ?"

show misha cross_laugh_close
with charachange


mi "Wahahahaha~ !"


"Je les regarde avec un visage fatigué. Misha et Shizune : un, Hisao : zéro."

show shizu adjust_happy_close
with charachange

shi "…"

show misha hips_grin_close
with charachange


mi "Oh, Shicchan dit aussi que tu devrais vérifier ton courrier plus souvent~ !"

show letter_insert:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)


"Elle sort une enveloppe jaune et me la tend avec un large sourire."


"Étrange. Qui aurait pu m’écrire une lettre ? Ce n'est pas le moment pour le découvrir cela dit."

show letter_insert:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide letter_insert
with None


"Abandonnant la sieste qui m'a été cruellement volée, je me frotte le front et me lève lentement, range les papiers et l'enveloppe dans mon sac avant de le mettre sur mon épaule."

show misha cross_laugh at Transform(yalign=1.0, xanchor=0.5, xpos=0.355)
show shizu behind_smile at Transform(yalign=1.0, xanchor=0.5, xpos=0.615)
with charadistant


"Je fais un pas et m'en vais après un bref au revoir, pendant que Misha se tient les côtes en rigolant et que Shizune hoche la tête pour me rendre mon au revoir."

stop music fadeout 3.0
play ambient sfx_crowd_indoors fadein 0.5

scene bg school_hallway3
show crowd
with locationchange


"Je rejoins la foule d’étudiants sortant par la porte ouverte, et tourne au coin du couloir."

$ renpy.music.set_volume(0.7, 0.5, channel="ambient")

show hanako emb_downtimid at center
with charaenter


"...Et me retrouve face à face avec Hanako."


hi "Wah. Euh, salut Hanako."

show hanako emb_timid
with charachange


ha "Bonjour... Hisao."

show hanako emb_downtimid
with charachange


"Le silence s'installe entre nous pendant que des étudiants qui discutent passent à côté. Elle n'arrête pas de gigoter, ses yeux rivés sur ses chaussures."


"Je me masse les sinus tout en clignant des yeux pour essayer de rendre les choses plus claires. Je peine à rester éveillé."


hi "Hanako, tu veux dire quelque chose. Qu'est-ce qu'il y a ?"

show hanako emb_blushing
with charachange


ha "Euh... Je voulais te... donner ça..."


hi "Mmh ?"

show hanako basic_worry
with charachange


"Elle tient dans ses mains une feuille de papier pliée en quatre. Je cligne encore une fois des yeux pour réussir à lire ce qui y est écrit."

window hide


$ written_note("\nOeufs x2\nPain de mie x1\nCéréales au blé complet x1\nThym x1\n")

window show

play music music_happiness fadein 0.5


hi "...Une liste de courses ?"


"Je relève la tête, un sourcil levé."

show hanako emb_timid
with charachange


ha "D'habitude je vais faire les courses avec Lilly mais je ne peux pas y aller, alors..."


hi "Tu veux que j'aille faire les courses pour toi ?"

show hanako defarms_shock
with charachange


ha "C-c'est pas grave si tu ne veux pas ! Je pensais juste que, peut-être, euh..."


"Elle panique. Je soupire. Une autre bataille de perdue. Même si je ne me suis pas tellement battu cette fois."


"Je souris avec lassitude et pose une main sur sa tête pour la calmer."


hi "C'est bon, je comptais y aller de toute façon. Tu as juste besoin de ce qui est sur la liste ?"

show hanako def_worry
with charachange


"Elle hoche la tête puis se penche, deux fois, pour montrer sa gratitude."

show hanako cover_distant
with charachange


ha "O-on avait prévu de se rejoindre devant le portail à dix-huit heures... merci, j'allais y aller, mais j'ai besoin de réviser pour l'examen de demain."


hi "Examen ? Ah, c'est vrai, en science. Comment tu t'en sors ?"

show hanako cover_bashful
with charachange


"Elle semble se réjouir de la question."

show hanako basic_bashful
with charachange


ha "Je... révise plus qu'avant. Je crois que je... peux m'en sortir pas trop mal."


hi "Travaille bien, alors."

show hanako basic_smile
with charachange


"Elle commence à sourire aussi, avec plus d’honnêteté que moi."


"J'ai confiance en moi quant au fait de m'en sortir à cet examen sans réviser, et le fait qu'elle fasse l'effort d'apprendre au lieu de juste lire à la bibliothèque est encourageant."


hi "Je vais aller acheter tes trucs et je te les apporterai au dortoir dans la soirée. À plus tard."

stop music fadeout 3.0
$ renpy.music.set_volume(1.0, 3.0, channel="ambient")

hide hanako
with charaexit


"Avec un petit signe de la main, nous nous séparons."


"Je vais faire mes devoirs avant de partir à la rencontre de Lilly. Je devrais pouvoir finir dans les temps."

stop ambient fadeout 1.0

scene bg school_gate_ss
with shorttimeskip

play music music_soothing fadein 2.0


"Un problème de maths particulièrement compliqué me donne du fil à retordre et me met en retard pour mon rendez-vous avec Lilly."


"De quelques minutes seulement, mais suffisamment pour me faire marcher rapidement en direction du portail de l’école."

scene bg school_road_ss
with locationchange


"Je tourne à droite et commence à me diriger vers la petite ville en bas de la colline, croisant quelques étudiants allant de l'autre côté, vers la station de bus."


"Je mets ma main droite dans ma poche alors que je marche dans la lumière orange du crépuscule."


"Heureusement l’étouffante chaleur d’été a commencé à disparaître, laissant place à une brise plaisante."

show lilly back_listen_ss at center
show lillyprop back_cane_ss at center
with charaenter


"Alors que je suis en train de m’étirer les bras, une silhouette familière apparaît, une canne dans sa main droite."


hi "Ah, Lilly."

show lilly cane_listen_ss
hide lillyprop
with charachange


"Elle s’arrête et se retourne, penchant légèrement la tête pour essayer de comprendre de qui venait la voix."


hi "C'est moi."


"Je la rattrape vite, me mets à ses côtés et me synchronise à son rythme."

show lilly cane_smile_ss
with charachange


li "Bonjour, Hisao."


hi "Salut toi."

scene bg misc_sky_ss at Fullpan(10.0, dir="right")
with locationchange


"Je regarde le ciel."


"Les nuages, colorés d'un orange crépusculaire, noient le chemin de leur lumière. Les grandes ombres des arbres tapissent la route en bas de la colline."

scene bg school_road_ss
show lilly cane_smileclosed_ss
with charachange


li "Alors, Hisao, qu'est-ce qui t’amène ici ?"


hi "Je vais juste en ville acheter quelques trucs. Hanako m'envoie."

show lilly cane_surprised_ss
with charachange


li "Hanako a fait ça ?"


hi "Ouais, elle a dit qu'elle avait besoin d’étudier pour un examen demain. J'avais prévu d'y aller de toute façon, donc autant acheter ses trucs en même temps."


"Sans préciser que Lilly aurait aussi besoin d'aide pour faire les courses, mais c'est un fait évident qui n'a pas besoin d’être dit."

show lilly cane_weaksmile_ss
with charachange


li "C'est bien qu'elle s'applique à étudier."


hi "J'ai pensé la même chose quand elle m'a demandé de venir avec toi."

hide lilly
with charaexit


"Nous continuons de marcher lentement, le son familier de sa canne tapant le sol. En dehors de quelques rares voitures et du murmure des branches, il règne un silence paisible ."


"Dieu merci, je peux enfin me relaxer pour la première fois de la journée."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene evbg lilly_sunsetwalk:
    truecenter subpixel True zoom 0.9
    acdc_warp 20.0 zoom 1.0
show evfg lilly_sunsetwalk:
    truecenter subpixel True zoom 0.85
    acdc_warp 20.0 zoom 1.0
with locationskip


"Je regarde Lilly."


"Son visage de porcelaine ne semble jamais perdre cet air de confiance paisible. J'imagine qu'on peut dire la même chose de sa personnalité."


"Alors qu'elle marche silencieusement, son visage fixé devant elle, je regarde à mon tour devant moi et savoure l'air frais balayant mon visage."


"C'est probablement le moment le plus serein que j'ai eu depuis la volte-face toute récente de ma vie."


"Avoir un moment comme cela, en marchant pour aller faire les courses. Quelle vie bizarre."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

scene bg school_road_ss
with locationskip


"Je sens la note chiffonnée dans ma poche, et la sors pour relire son contenu."


hi "Voyons voir... œufs, pain, céréales, thym, laitue, jambon..."

show lilly cane_weaksmile_ss
with charaenter


li "Ça fait beaucoup à porter, non ?"


hi "Ouais. Elle mange vraiment tant que ça ?"


"Mon cerveau me rappelle à ce moment que oui, il y a quelqu'un à côté de moi."


hi "A-attends, je veux dire..."

show lilly cane_giggle_ss
with charachange


"Elle rit ouvertement."

show lilly cane_planned_ss
with charachange


li "Eh bien, eh bien, Hisao."


"Son rire est toujours présent dans ses mots, bien qu'elle fasse ce qu'elle peut pour le retenir."

show lilly cane_satisfied_ss
with charachange


li "Tu es plutôt direct aujourd'hui, n'est-ce pas ?"


hi "Ouais, tu m'as bien eu là. Cela dit, ça fait vraiment beaucoup."

show lilly cane_smileclosed_ss
with charachange


li "D'habitude je vais faire les courses avec Hanako, donc je sais ce qu'elle achète. C'est la même chose toutes les semaines."


hi "Oh. Elle cuisine bien ?"

show lilly cane_weaksmile_ss
with charachange


"Elle émet un rire quelque peu nerveux."


li "Généralement c'est moi qui finis par cuisiner. J'avais l'habitude de le faire pour Akira, alors ça ne me gêne pas de le faire aussi pour Hanako."


hi "Tu peux cuisiner ? Mais..."

show lilly cane_cheerful_ss
with charachange


"Lilly a un petit rire suite à ma réflexion. Je me demande si le fait qu'elle soit autant amusée par mes remarques est réel, ou si c'est juste parce qu'elle voudrait que je sois plus à l'aise au sujet de sa cécité."

show lilly cane_smileclosed_ss
with charachange


li "J'ai mes propres méthodes. Certaines choses sont plus difficiles que d'autres parce que je ne peux pas voir ce que je fais, mais ça me prend juste un peu plus de temps. Les doigts peuvent être des outils de mesure très pratiques par exemple."


"Je vois ce qu'elle veut dire, mais elle doit être très prudente pour ne pas se blesser. Je me demande combien de fois c'est arrivé, étant donné qu'elle cuisine seule depuis probablement des années, depuis qu'Akira travaille et que ses parents sont partis."


"Après ça, la conversation arrive à sa fin."



"En comparaison des silences gênants avec Hanako, Lilly semble plus à l'aise avec le fait de parler quand il y a quelque chose à dire, et de rester silencieuse quand il n'y a rien."


"Sous mes pieds, le sol lisse baigne dans une lueur orange, les quelques feuilles déjà tombées s'écrasent sous nos pieds pendant que nous marchons. Je laisse échapper un grand bâillement, le manque de sommeil revenant me hanter."

show lilly cane_smile_ss
with charachange


li "Tu n'as pas beaucoup dormi la nuit dernière ?"


hi "Je n'ai pas pu dormir du tout ces deux dernières nuits. Probablement de l'insomnie."

stop music fadeout 8.0

show lilly cane_oops_ss
with charachange


"Le visage de Lilly montre de l'inquiétude. Je ressens comme un échec personnel chacune des fois où je la vois s'inquiéter pour moi, même s'il est agréable de savoir que quelqu'un s'intéresse à moi."


li "Tu fais de l'insomnie ? Tu ne vas pas aller voir l'infirmier pour ça ?"


hi "Nan, pas besoin. Ça m'est déjà arrivé avant. Ce sont mes médicaments qui perturbent mon sommeil des fois."

show lilly cane_concerned_ss
with charachange


li "...Ah. Je... suis désolée."


hi "T’embête pas, c'est pas comme si c’était de ta faute. Au moins j'aurai pas trop de mal à m'endormir ce soir."

show lilly cane_sleepy_ss
with charachange


li "Tu m’inquiètes des fois."


hi "Je... t’inquiète ?"


"Je me gratte l’arrière de la tête. Je veux lui en parler."


hi "Dis, Lilly..."

show lilly cane_smile_ss
with charachange


li "Mmh ?"


hi "Je ne veux pas que ça te semble bizarre mais... essaye d'oublier mes problèmes de cœur, s'il te plaît."

show lilly cane_oops_ss
with charachange


"Elle a l'air perdue. Je ne peux pas lui en vouloir."


hi "Ce que j'essaye de dire c'est... ne me traite pas différemment à cause de ça."

show lilly cane_emb_ss
with charachange


"Elle hoche légèrement la tête, ses joues blanches rougissant très légèrement."


li "C'est normal que je m’inquiète pour toi..."


hi "Ça fait quand même plaisir de savoir que quelqu'un est là pour moi."

show lilly cane_smileclosed_ss
with charachange


"C'est peut-être embarrassant à dire, mais c'est la vérité. Lilly respire à fond pour reprendre son calme et affiche un léger sourire, bien que ses joues restent rougies."


"Le reste du trajet jusqu'au magasin se passe dans le silence."

scene bg suburb_konbiniint
with shorttimeskip

play music music_daily fadein 4.0


"Vendeuse" "Bienvenue !"


hi "Je pense prendre mes trucs en premier et ceux de Hanako après."

show lilly cane_smileclosed at center
with charaenter


"J'attrape deux paniers rouges parmi la pile à l’entrée et en donne un à Lilly."

show lilly cane_smileclosed at Transform(ypos=800)
with charamove

show lilly basic_smileclosed at Transform(ypos=800)
with charachange

show lilly basic_smileclosed at center
with charamove


"Tout comme elle a l'habitude de faire, elle pose le panier sur le sol, rétracte sa canne et la coince dans la poignée du panier, avant de le ramasser."

$ renpy.music.set_volume(0.5, 0.5, channel="music")

show lilly basic_smileclosed at Slide(0.5,0.5,0.3,0.5,1.0, time_warp=_ease_time_warp)
with None

show lilly basic_smileclosed_close at Slide(0.5,0.5,0.3,0.5,1.0, time_warp=_ease_time_warp)
with Dissolve(1.0)


"Quand elle attrape mon bras comme ça, je suis surpris de voir à quelle vitesse ce genre de contact est devenu naturel. Dû à la nécessité, sans aucun doute."

show lilly basic_smile_close at twoleft
with charachange


li "On y va ?"

$ renpy.music.set_volume(1.0, 2.0, channel="music")


hi "Ouais."


"Pendant qu'on parcourt le magasin, les personnes passant occasionnellement à côté de nous ne nous prêtent aucune attention. C'est agréable, en comparaison des regards et chuchotements de la ville."

show lilly basic_smileclosed_close
with charachange


"Après avoir fait chaque rayon, je vérifie rapidement avec Lilly ce dont elle a besoin et attrape en même temps ce dont j'ai besoin, mettant les objets dans nos paniers respectifs."


"C'est un drôle de sentiment, de devoir dépendre autant de quelqu'un pour quelque chose d'aussi basique que faire les courses. La présence de Hanako est une nécessité pour qu'elle puisse avoir ce qu'elle veut après tout."


hi "Voilà. J'ai plus ou moins fini avec mes trucs et ceux de Hanako. Tu as besoin de quelque chose d'autre, Lilly ?"

show lilly basic_smile_close
with charachange


li "Non, ça doit être bon."


hi "Allons payer alors."


"Étrangement, la queue pour payer est longue. Sachant que le magasin n'a qu'une seule caisse, ça risque de prendre un moment."


hi "Zut."

show lilly basic_surprised_close
with charachange


"Lilly fait une drôle de tête, incapable de savoir la raison de ma plainte."


hi "La queue est vraiment longue. On dirait qu'on va devoir attendre."

show lilly basic_weaksmile_close
with charachange


li "C'est étrange."


"Partageant le même sentiment de résignation, nous nous plaçons à contrecœur à la fin de la file d'attente."

$ renpy.music.set_volume(0.5, 10.0, channel="music")


"Une personne finit, et la file avance. Une autre personne finit, la file avance."


"Au moment où nous atteignons enfin la caisse, je suis si près de m'endormir que Lilly doit me tapoter gentiment dans le dos pour me faire avancer."

show lilly basic_oops_close
with charachange


li "Hisao... Hisao !"

$ renpy.music.set_volume(1.0, 0.3, channel="music")


hi "Mmh ? Ah, désolé."

show lilly basic_displeased_close
with charachange


"Elle pousse un petit soupir de consternation alors que nous avançons, je prends les courses de Hanako et les miennes pour les mettre dans des sacs séparés."


"Vendeuse" "Merci beaucoup, au revoir !"

stop music fadeout 5.0

scene bg suburb_konbiniext_ni
show lilly basic_smileclosed_ni
with locationskip


"Au moment où nous sortons du magasin, Lilly tient un seul sac alors que je me bats avec quatre d'entre eux. C'est assez difficile, mais heureusement les sacs sont légers."


"Même sans regarder le ciel, il est évident que beaucoup de temps s'est écoulé, la route extérieure est dans l'obscurité et éclairée par des lampadaires."

show lilly cane_smile_ni
with charachange


"Une fois que Lilly a déplié sa canne, nous nous dirigeons vers les dortoirs en utilisant le même chemin qu'à l’aller, s’éloignant de la lumière accueillante du magasin."

scene bg school_road_ni
with locationskip

play music music_dreamy fadein 8.0


"Malgré le fait qu'il n'y ait pas de voitures sur la route, les sacs pleins compensent le manque de bruit, s'entrechoquant constamment."

show lilly cane_ara_ni
with charaenter


li "Eh bien, eh bien, Hisao, ça fait plaisir de voir que tu manges bien."


hi "Je suis un homme en pleine croissance après tout, je dois manger tout ce que je peux !"

show lilly cane_weaksmile_ni
with charachange


li "Mmh... Ça doit être bien, être un homme."


hi "H-hein ?"


"Ne sachant pas si elle ignore ma remarque hors sujet, ou si elle ne l'entend pas, elle continue sans faire de commentaire."

show lilly cane_smile_ni
with charachange


li "La plupart du temps, le poids ne vous gêne pas quand vous mangez."


hi "Je vois de quoi tu parles. Les femmes ont tendance à s’inquiéter de trucs comme ça plus souvent que nous, j'imagine."

show lilly cane_smileclosed_ni
with charachange


li "Exactement. Ça me rend quelque peu envieuse, pour être honnête."


hi "Eh bien, c'est pas comme si on pouvait totalement l'ignorer non plus."


"Avec un hochement de tête affirmatif, nous continuons notre marche."


hi "Oh, c'est vrai."

show lilly cane_smile_ni
with charachange


li "Qu'est-ce qu'il y a ?"


hi "Hanako a mentionné que ton anniversaire était plus tôt cette année. Tu as fait quelque chose de spécial à ce moment-là ?"

show lilly cane_listen_ni
with charachange


"Elle marque une longue pause, perdue dans ses pensées le temps de quelques secondes, avant de se rappeler l’évènement."

show lilly cane_weaksmile_ni
with charachange


li "Pas vraiment. Hanako et moi avons juste passé la soirée ensemble comme on l'a fait pour le sien."


hi "Ton anniversaire est censé être un grand évènement, tu sais."


"Ça a l'air d’être un moyen plutôt triste de passer un anniversaire, juste Hanako et elle restant dans sa chambre au dortoir."


"Les anniversaires ont toujours été une occasion de voir la famille pour moi. Il y a eu une époque où, malgré leur travail, mes parents trouvaient tous les deux le temps d’être là ce jour, ou au moins, pour ma fête d'anniversaire."


"Ça me rappelle que Lilly a mentionné ne pas avoir vu sa famille depuis longtemps, et qu'elle a même fini par déménager de la maison d'Akira."


"J'imagine que c'est pareil dans des situations comme ça. Sachant son incapacité de lire un emballage, faire les courses doit être très dur sans avoir quelqu'un avec elle."


"En fin de compte, elle nous a juste Hanako et moi. Et Akira quand elle ne travaille pas."


"Cela dit, elle semble avoir pas mal d'amis moins proches parmi les étudiants, sans mentionner des gens comme Yuuko."


"Ça semble être son propre choix qu'il y ait une telle séparation entre ceux qui lui sont proches, et ceux avec qui elle socialise."


"Ça me fait me sentir un peu misérable de voir comment Lilly semble avoir mis sa vie en place comme elle l'entend."


"Et pourtant Hanako est là pour célébrer son anniversaire, et je suis là pour l'aider avec les courses. C'est une étrange forme de symbiose, j'imagine."

show lilly cane_oops_ni
with charachange


li "Est-ce que ça va, Hisao ?"


hi "Pardon ?"


li "Tu semblais juste très silencieux, c'est tout."


hi "Ah, désolé. Je réfléchissais juste."

show lilly cane_smileclosed_ni
with charachange


li "Oh ?"

label fr_choiceL6_1:
menu:
    with menueffect
    "Ah, maintenant j'ai piqué sa curiosité. Ça semble être quelque chose de trop personnel pour en parler cela dit..."
    "Éviter le sujet.":




        return m1
    "Dire la vérité.":


        return m2

label fr_L6a:



hi "J’étais juste en train de penser à certains trucs qui sont arrivés, ne t’inquiète pas."

stop music fadeout 2.0

show lilly cane_listen_close_ni
with characlose


li "Mmh ?"


"Elle se penche encore plus, me forçant à me décaler sur le côté."


hi "Allez, ça ne t'arrive jamais de faire ça ?"

show lilly cane_cheerful_close_ni
with charadistant


li "Tu as dit ça comme si tu cachais quelque chose..."

play music music_lilly fadein 4.0


"Erh. Pourquoi est-ce qu'elle est si perspicace ?"


"En me tournant vers elle, je vois qu'elle affiche un sourire joueur."


"Elle... joue avec moi ? Même si c'est vrai, je préfère ne pas continuer la discussion."


hi "Je te l'ai dit, ce n'est rien."

show lilly cane_displeased_close_ni
with charachange


"Lilly fronce les sourcils de désapprobation."


li "Est-ce bien vrai ?"


hi "Oui, ça l'est."

show lilly cane_surprised_close_ni
with charachange


li "Tu es un très mauvais menteur, Hisao."


hi "C'est vrai, et c'est pour ça que je ne mens pas. Je suis quelqu'un de très honnête."

show lilly cane_weaksmile_close_ni
with charachange


li "Je suis sûre que tu l'es. Je crois que je peux te pardonner. Juste cette fois."


hi "Me pardonner ? Et pourquoi donc ?"

show lilly cane_giggle_close_ni
with charachange

with Pause(0.2)

show lilly cane_smile_ni
with charadistant


"Elle rit un peu et retourne à sa marche silencieuse. À quoi est-ce qu'elle pense maintenant ?"

stop music fadeout 4.0


"Je regarde vers le ciel noir en soupirant doucement."


"Je crois que c'est quelque chose dont je dois m'occuper moi-même, plutôt que de compter sur les autres pour tout."

label fr_L6b:



hi "C’était juste que... j’étais en train de penser à quel point tu sembles avoir tout prévu et tout sous contrôle, même avec Hanako qui compte sur toi. J’admets que moi-même, j'ai eu un peu besoin de toi quand j'ai été transféré."


hi "Je pense que c'est une très bonne qualité."


"Je me tourne vers Lilly, surveillant sa réaction."

stop music fadeout 2.0

show lilly cane_listen_close_ni
with characlose


"Elle se force à regarder devant et fronce un peu les sourcils. Son expression est un peu étrange, comme si elle essayait de trouver les bons mots."


hi "...Lilly ?"

show lilly cane_weaksmile_close_ni
with charachange


li "Je te remercierais bien, mais... dire que je ne compte pas sur les autres est exagéré. Tu aurais tort de penser que Hanako compte simplement sur moi sans rien en retour."


"Elle semble avoir du mal à dire cela, même si c'est majoritairement ce que je pensais déjà."


"Si elle essayait de maintenir son indépendance, comme n'importe qui l'aurait fait dans sa position, aveugle ou non, peut-être qu'elle trouverait difficile de parler de ses propres besoins."


"C'est seulement maintenant que je réalise qu'elle a omis quelque chose volontairement. Je décide de continuer par là, en plaisantant, pour éviter que ça devienne trop personnel."


hi "Oh ? Et moi alors ?"

play music music_lilly fadein 2.0

show lilly cane_smile_ni
with charadistant


"Elle se met à courir devant moi et se tourne, me bloquant la voie."

show lilly behind_cheerful_ni
with charachange


"Avec un sourire, elle se tient les mains derrière le dos et se penche en avant."


li "Tu es différent."

show lilly back_giggle_ni
show lillyprop back_cane_ni
with charachange


"Et sur ce, elle se retourne et continue de marcher devant moi, un certain entrain dans les pas."


"Tout ce que je peux faire est lever un sourcil et lui adresser un sourire étourdi. Je ne crois pas que je l'avais déjà vue aussi joueuse auparavant."


"Donc... je suis “différent”. C'est dur de savoir en quoi exactement, mais la connaissant, l'ambiguïté était volontaire."


"Notre relation a changé, déjà parce que j'ai commencé à me débrouiller seul et à m’intéresser à la situation des gens autour de moi."


"Quant au pourquoi... probablement un mix entre la curiosité personnelle et une envie d'essayer de gérer ma situation."


"Je suis moins sûr pour Lilly cela dit. C'est pourquoi son propre avis, similaire à mes propres sentiments envers elle, me rend confus."


"La regardant faire son chemin, la canne tapant de gauche à droite, je décide de m'occuper de ça plus tard, et de juste sourire. C'est un de ses bons côtés, et je ne veux pas l'oublier."

stop music fadeout 2.0

label fr_L6c:


scene bg school_girlsdormhall
with shorttimeskip

play music music_normal fadein 4.0


"Finalement nous arrivons au dortoir des filles, mes bras souffrant du poids des courses."


hi "Ha... on y est enfin. Fiou."

show lilly invis:
    right
    xpos 0.95
with None

show lilly cane_smileclosed at right
with dissolvecharamove


"Je me penche pour m'essuyer le front avec le dos de la main. Lilly s’arrête en face de sa porte et pose son sac, cherchant la clé dans sa poche."

show lilly cane_smile
with charachange


li "Merci, Hisao. J’apprécie vraiment ton aide."


hi "Oh, c'est rien."

show lilly cane_smileclosed
with charachange


li "C'est peut-être rien pour toi, mais c'est... vraiment quelque chose pour moi."

show lilly invis:
    right
    xpos 1.05
with dissolvecharamove

play sound sfx_doorclose

hide lilly
with None


"Et sur ce, elle franchit la porte, la fermant derrière elle."


"Je cligne des yeux. C’était des remerciements sincères, mais ne je peux pas m’empêcher de penser qu'il y a quelque chose de plus en eux."


"De toute façon, j'ai quelque chose d'autre à faire avant de pouvoir penser à ça."

scene bg school_dormhanako_ni
show hanako emb_timid_close:
    center
    xpos 0.45
show hanako_door_base at right
show hanako_door_door at left
with locationchange

play sound sfx_doorknock2


"Je me mets en face de la porte de Hanako et frappe deux fois, les sacs toujours en train de s'entrechoquer dans ma main."

play sound sfx_dooropen

show hanako_door_door:

    xpos -0.05
with charamove


"Après quelques secondes, la porte s'ouvre lentement. Si je n’étais pas en train de regarder attentivement, j'aurais pu dire qu'elle n'a pas bougé du tout."


"Je penche la tête et essaye de voir dans l’entrebâillement de la porte."


hi "Hé, Hanako, je t'apporte tes courses."

show hanako basic_normal_close at Position(xpos=0.4)
with charachange


ha "Ah !"

show hanako_door_door:
    xpos -0.3
show bg school_dormhanako
with dissolvecharamove


"Sur ce, la porte s'ouvre complètement, rendant sa chambre visible au-dessus de ses épaules. Très peu décorée, elle est probablement encore plus banale que ma chambre."


"Je tends mon bras droit, peinant à le maintenir dans cette position à cause du poids des sacs."

show hanako emb_smile_close
with charachange


ha "M-merci, Hisao."

show hanako emb_downtimid_close
with charachange


ha "Désolée de t'avoir... fait porter ça."


hi "C'est pas grave, ne t’inquiète pas. Ne me force pas à le faire tous les jours non plus, hein ?"

show hanako basic_normal_close
with charachange


"Je lui passe les sacs tout en riant un peu à ma remarque."


hi "Je vais y aller maintenant. Bonne nuit, Hanako."

show hanako cover_bashful_close
with charachange


ha "Bonne nuit. Je, euh, te vois en classe... demain..."

show hanako_door_door at left
with charamove

play sound sfx_doorclose


"Après avoir fait une courbette, les sacs encore dans ses mains, elle recule et ferme la porte."

stop music fadeout 5.0

scene bg school_dormext_full_ni
with locationskip


"Marchant jusqu’à mon propre dortoir, je mets un sac dans l'autre main pour équilibrer le poids."


"Même en faisant cela, je n'arrive pas à retirer le sourire de Lilly de mon esprit. Quand je l'ai rencontrée, il aurait été impossible de l'imaginer comme ça."


"On est devenus beaucoup plus proches ces dernières semaines depuis la première fois que je les ai rencontrées, Hanako et elle."


"Le temps que je passe avec elle chaque jour. Les petits échanges de bonheur que nous partageons. Ces petits moments de joie quand on se rapproche."


"Je suis loin d’être certain, mais je ne crois pas que ce soit simplement de l'amitié."

scene bg school_dormhisao
with locationskip


"Une fois que j'arrive dans ma chambre, je range les courses et commence à me préparer pour la nuit."

show letter_insert:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)


"Je range les livres d’école dont j'aurai besoin dans mon sac, et sors l'enveloppe jaune que Misha m'a donnée tout à l'heure."


"J'ai été tellement occupé par d'autres choses que je n'ai pas eu le temps de la lire. Qui peut bien m’écrire ?"


"Le nom ornant le dos de l'enveloppe me paralyse. Ça fait si longtemps que je n'ai pas vu son écriture, que sans le nom, je n'aurais certainement pas pu l'identifier."


"“Iwanako.”"


"Pourquoi... m'a-t-elle écrit ? Je ne trouve pas de bonne raison pour qu'elle l'ait fait."


"J'ai presque envie de ne pas l'ouvrir. Mais ça ne servirait pas à grand-chose. Si je ne l'ouvrais pas, son existence même me perturberait jusqu’à ce que j'en fasse quelque chose."

scene ev hisao_letter_open
with shorttimeskip

play music music_rain fadein 6.0


"Je regarde la feuille de papier sur mon bureau, ses décorations aux couleurs de l’été rayonnant joyeusement en ma direction."


"L’écriture est en rose, se mariant difficilement avec le tournesol jaune au bord de la feuille. L’écriture est propre, les caractères ont été écrits soigneusement et avec une attention inhabituelle."


"C'est à peine si j'accordais de l'importance à la lettre quand elle m'a été donnée, mais maintenant je ne peux pas m’empêcher d'y penser."

window hide
nvl clear
nvl show dissolve


n "\n\n\nBien que j'aimerais dire que je ne sais pas pourquoi elle utilise une méthode si obsolète de communication, vu qu'un appel téléphonique ou un e-mail aurait été plus rapide et pratique, sa raison est assez évidente."


n "Une lettre laisse une distance confortable entre l'expéditrice et le destinataire. Contrairement à un téléphone, il n'est pas requis d'engager une conversation, et contrairement à un mail, on attend moins une réponse immédiate."


n "\nDes phrases telles que “les étudiants de troisième année semblent très inquiets pour les examens finaux“ ou “c'est bizarre de penser qu'on est déjà en dernière année, non ?“ sont juste là pour parler de choses peu importantes. Des choses qui auraient pu être répondues à n'importe lequel des messages que je lui ai envoyés pendant que j’étais à l’hôpital."


n "La fin, cela dit, est la vraie raison pour laquelle elle a envoyé cette lettre. Les dernières lignes, ajoutées presque comme un post scriptum."

nvl clear
nvl hide dissolve

play sound sfx_paper

scene ev hisao_letter_open_2
with locationchange

nvl show dissolve


n "\n\n\n\n\n\n\n“Je me demande si on se reverra. Peut-être que c'est mieux si on ne se revoit pas.”"


n "C'est une remarque qui devrait faire mal. J'ai toujours entendu que les ruptures étaient difficiles, mais là c'est plutôt une réaffirmation de ce qu'on savait déjà tous les deux."


n "Ce qui est dans le texte précédent, qui n'est là que pour combler les lignes, est ce qui me met le plus mal à l'aise. Je n'arrive pas à comprendre pourquoi, peu importe combien de temps je reste là à lire cette lettre sur fond d’été."

nvl clear


n "\n\n\n\n\n\n\n\n“Si tu veux correspondre avec moi, écris-moi par tous les moyens possibles.”"


n "Il est évident que ce n'est pas le genre de lettre à laquelle on doit répondre. En fin de compte, cette lettre n'est rien de plus qu'une simple abdication de responsabilité, une note finale pour s'assurer que notre relation est vraiment finie."

stop music fadeout 3.0

nvl hide dissolve
nvl clear

scene bg school_dormhisao
with locationchange

window show


"Sur ce, je réussis à jeter la lettre et l'enveloppe dans la corbeille avec peu de peine, me débarrassant de leur existence."


"Je vais au lit avec des sentiments partagés, gâchant une plaisante soirée par l'intrusion de mon passé."


"Ironiquement, il me faut un bon moment avant de réussir à m'endormir."

scene black
with dissolve

$ suppress_window_after_timeskip = True

label fr_L7:

window hide None

scene black
with dissolve

nvl show dissolve


n "\n\n\n\nJe transpire beaucoup, attendant le moment crucial."


$ renpy.music.set_volume(0.7, 0.0, channel="music")
play music music_tension fadein 6.0


n "Chaque tic de l'horloge tend mes muscles un peu plus, chaque minute me donnant des cheveux blancs."


n "Ça vient pour moi, je peux le sentir."

play sound sfx_slide


n "\n\n{image=vfx/reddash.png}{color=#FF0000}{b}La Mort.{/b}{/color}"


n "\n\nLa Mort sous la forme d'une feuille de papier."

$ renpy.music.set_volume(1.0, 0.5, channel="music")

nvl clear
nvl hide dissolve

scene bg school_scienceroom at bgright
with locationchange

window show


"Je prends la petite pile de papiers que me tend l’étudiant en face de moi et la fais passer derrière après avoir pris celle à mon nom."


"Regardant dans le coin en haut à droite de la page, mes craintes se réalisent au centre de ce petit cercle rouge."

stop music
play sound sfx_thunder
with vpunch


"Quarante-trois."


"Ma tête tombe et je soupire en me résignant. Maudissant le monde entier, je peux sentir l'aura d'un sentiment similaire se propager dans la classe. C'est étrange, mais ce fait me remonte très légèrement le moral."


"Le malheur aime la compagnie après tout."


"Alors que le professeur ouvre la bouche, tout le monde se prépare pour le massacre inévitable..."

play music music_normal fadein 1.0

play sound sfx_normalbell


"... Sauvés par le gong."


"Nous nous dépêchons de prendre nos sacs et partons pour manger, mais le professeur lance une attaque au flan."


"Professeur" "Nous discuterons des scores de l'examen la prochaine fois. Pas besoin de le préciser, il y aura de quoi en parler."


"Un gémissement collectif résonne dans la classe, maintenant réduite à sortir découragée."

scene bg school_hallway3 at bgright
with locationchange


"Je mets la feuille dans mon sac et sors dans le couloir, la chiffonnant en même temps. Déjà hier, j'ai eu cette lettre qui a fini sur mon bureau, et maintenant ça."


hi "Je déteste l'anglais..."

stop music fadeout 0.7


mystery "HI—{w=0.3}SA—{w=0.3}O !"


"Une voix de femme venant de derrière m'appelle."

play music music_tension


"Je m’arrête sur place, mon visage devenant comme de la pierre. Comme si je pouvais sentir mon cerveau se déconnecter de mon corps."


"Mes yeux bougent lentement vers la droite, essayant de voir l'origine de la voix désincarnée."

stop music fadeout 0.3


"...rien ?"


"Mon visage commence à se tordre alors que le temps passe, et je décide de me risquer à tourner la tête. Tout doucement, je la tourne vers la—"

play sound sfx_impact


hi "GYAAAAH !" with vpunch


"Je bondis littéralement de surprise, et fais tomber mon sac en criant."


"Alors que je reprends mon calme, je me tourne pour voir... J'aurais dû le savoir."

hi "Emi."

play music music_running

show emi excited_proud at center
with charaenter


emi "Je t'ai eu, Hisao."


"Elle se tient là avec un sourire sournois sur le visage, les mains en avant et les doigts vers l’intérieur. C'est elle qui m'a pincé les côtes."


"Je la regarde en grimaçant, me frottant la tête de frustration."


hi "C'est pas une façon de saluer, tu sais."

show emi sad_pout
with charachange


emi "Tu n'as aucun sens de l'humour."


hi "J'ai laissé mon sens de l'humour en classe d'anglais. Plains-toi au professeur si tu veux que je le récupère."

show emi sad_shy
with charachange


"Elle me sort sa meilleure moue, avec ses yeux de chiot battu. Lilly m'a appris à résister à cette technique, mais la petite taille d'Emi ajoute suffisamment d'effet pour me radoucir."


hi "Donc, quoi de neuf ? Ça fait un moment que je ne t'ai pas vu."

show emi basic_closedgrin
with charachange


emi "Comme d'hab, comme d'hab. Je cours tellement vite que personne ne veut me rejoindre pour mes courses matinales."

show emi basic_annoyed
with charachange


emi "C'est pas drôle."


"Sa modestie ne cesse jamais de m'amuser."

show emi basic_grin
with charachange


emi "Cependant..."

"Uh oh."

show emi sad_shy
with charachange


emi "Tu sais à quoi je pense, n'est-ce pas Hisao ?"


"On lit trop facilement sur mon visage, c'est une de mes pires habitudes. Elle voit clairement à travers moi."


"Heureusement, je vois quelqu'un d'autre approcher, me donnant une échappatoire."


hi "Oh, salut Hanako."

show emi sad_shy at twoleft
show bg school_hallway3 at center
with charamove

show hanako emb_downtimid at tworight
with charaenter


"Je la salue de la main, et fais de mon mieux pour agir comme si je n'avais pas remarqué la moue d'Emi. Hanako me fait un signe en retour."

show hanako emb_smile
with charachange


ha "B-bonjour, Hisao... et Emi."

show emi basic_closedgrin
with charachange


emi "Salut Hanako."


hi "Je vous rejoins, Lilly et toi, dans une seconde."


hi "D'ailleurs, en parlant de compagnie pour déjeuner, c'est bizarre de te voir sans Rin, Emi."

show emi basic_shock
show hanako defarms_shock
with vpunch


emi "Ah ! Rin !"

stop music fadeout 3.0

hide emi
with easeoutleft


"Sans dire un autre mot, elle nous oublie et part en courant dans le couloir. Elle a dû oublier que Rin l'attendait."


"Hanako et moi restons là, sans un mot, seulement capables de nous tenir là, à regarder la boule d’énergie partir à toute vitesse."

play music music_running

show emi basic_closedgrin at left
with easeinleft


emi "Ah, oui, Hisao."


"Elle s’arrête brusquement juste avant de disparaître au coin du couloir vers l'escalier du toit, et se retourne pour être en face de nous."

show emi excited_proud
with charachange


emi "Je déteste l'anglais aussi."

stop music fadeout 4.0

hide emi
with easeoutleft


"Et sur ce, elle disparaît."


"Tout ce que je peux faire est baisser la tête, et soupirer."

show hanako basic_smile
with charachange


"Entendant un petit rire derrière moi, je me tourne et vois Hanako sourire."

play music music_daily fadein 4.0

show hanako basic_smile at center
show bg school_hallway3 at bgleft
with charamove


"Je ramasse mon sac tombé au sol et l’époussette."


hi "Bon, elle est partie."

show hanako def_worry
with charachange


ha "Tu... n'aimes pas l'anglais ?"


hi "Mmh ? Oh, euh, non. J'ai eu un examen en anglais il y a un petit moment, et Emi m'a surpris au moment où je me morfondais sur la note."

show hanako emb_downsad
with charachange


ha "Ah, désolée..."


"Elle évite mon regard, se sentant visiblement coupable. Quelqu'un d'autre aurait pu croire que je venais de lui rappeler la mort d'un de ses proches."


hi "T’embête pas, c'est pas ta faute. Comment tu t'en sors en anglais toi ?"

show hanako emb_sad
with charachange


"Elle relève la tête, toujours en évitant mon regard."

show hanako basic_worry
with charachange


ha "Ça va, je... crois."


"Et voilà le silence gênant. Ils semblent trop communs avec Hanako."

show hanako basic_bashful
with charachange


ha "Oh, Lilly a demandé si... tu voulais nous rejoindre pour déjeuner sur le toit."


"Je ne pense pas avoir quoi que ce soit de prévu."


hi "Bien sûr, je viens tout de suite."

show hanako cover_distant
with charachange


ha "Euh... Je vais... aller chercher mon déjeuner à la cafétéria alors... voilà."


hi "Vas-y, tu n'as pas besoin de mon autorisation pour partir, tu sais."

show hanako basic_smile
with charachange


ha "D-d'accord. Je... j'y vais alors."

hide hanako
with charaexit

stop music fadeout 5.0


"Elle répond timidement, hoche rapidement la tête et se dirige vers la cafétéria."

play ambient sfx_crowd_indoors fadein 2.0

show crowd:
    bgleft
    alpha 0.0
    parallel:
        ease 1.0 center
    parallel:
        linear 2.0 alpha 1.0
with None

show bg school_hallway3 at center
with dissolvecharamove


"Je pense qu'elle a dû oublier d'amener son déjeuner aujourd'hui. Parcourant les couloirs, de plus en plus d’étudiants sortent de leurs classes et passent à côté de moi, se dirigeant dans la même direction que Hanako."


"À l'instant où j'arrive aux escaliers, je dois me frayer un chemin dans un petit groupe d’étudiants en train de discuter."

stop ambient fadeout 0.5

scene bg school_staircase1
with locationchange

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_rooftop



"J'arrive finalement à passer le dernier groupe et monte les escaliers, puis ralentis un peu le rythme avant d'ouvrir la porte du toit."

play sound sfx_door_creak
$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

scene bg school_roof
show white
with locationchange


hi "Raaaah !"


"Je me couvre les yeux un moment, aveuglé par le soleil d’été."

show white:
    alpha 1.0
    linear 10.0 alpha 0.0

show lilly basic_smile behind white:
    left
    ypos 1.2
show emi basic_grin behind white:
    center
    ypos 1.15
show rin basic_absent behind white:
    right
    ypos 1.17
with charaenter


mystery "Mmh ?"

play music music_soothing fadein 8.0


"Recouvrant lentement ma vision, les alentours prennent forme."


"Lilly, Emi et Rin sont assises ensemble sur le toit, le haut de la forêt qui entoure Yamaku est visible à travers le grillage, comme pour cadrer la vue."

show emi basic_closedgrin
with charachange


emi "Ah, Hisao !"

show lilly basic_smileclosed
show rin basic_deadpannormal
with charachange


"Lilly et Rin m'adressent un hochement de tête en guise de salutation."


"Je commence à marcher vers le trio quelque peu dépareillé, et ne peux pas m’empêcher de m’étonner de la vitesse à laquelle Emi engloutit le reste de sa banane à moitié mangée."


hi "Salut. Ça fait bizarre de vous voir toutes les trois ensemble comme ça."

show lilly basic_weaksmile
with charachange


li "Ça semble être le jour des coïncidences. Emi et Rin ont décidé de manger sur le toit le même jour que Hanako et moi."

show emi basic_annoyed
with charachange


emi "Tu l'as volé ! Cet endroit était à nous !"


hi "Ne dis pas ça, c'est pas possible de voler un endroit."


"Je m'assieds aux côtés de Lilly, formant un demi-cercle avec elles trois."

show rin basic_deadpanupset
with charachange


rin "Je crois qu'elle a raison."


hi "Toi aussi ?"

show rin basic_deadpan
with charachange


rin "Le papillon est son complice."


hi "Le pa..."


"Regardant autour, je vois un petit papillon jaune passer devant nous."


hi "Donc dis-moi, comment est-ce que le papillon a aidé Lilly à “voler” cet endroit ?"

show rin basic_lucid
with charachange


rin "Il a espionné notre conversation et lui a dit."


"J'aurais dû m'attendre à un tel raisonnement de la part de Rin. Néanmoins, ça ne fait pas de mal de jouer un peu."


hi "Tu me dis qu'elle peut parler aux papillons ?"

show rin basic_awayabsent
with charachange


rin "Il y a des gens qui peuvent murmurer à l'oreille des chevaux. Ça s'appelle des murmureurs."

show rin basic_deadpanamused
with charachange


rin "Lilly doit murmurer à l'oreille des papillons."


"Je m'enfouis le visage dans les mains, tandis que Lilly s'approche de son étrange camarade. Elle ne semble pas partager le sens de l'humour de Rin."

show emi basic_confused
with charachange


emi "Les murmureurs ne travaillent pas comme ça."


"Emi et Rin continuent leur plaisanterie alors que je me tourne vers Lilly, qui finit sa petite boîte de riz au curry avec une paire de baguettes en bois."


hi "Donc qu'est-ce qui t’amène ici, d'ailleurs ?"

show lilly basic_smile
with charachange


li "Un peu d'air frais de temps à autre ne fait pas de mal."

show emi basic_shock
with charachange


emi "Ah !"


"Emi s’interrompt dans sa vaine tentative d'apprendre le principe de la logique à Rin."

show emi sad_annoyed
with charachange


emi "C'est aussi pour ça qu'on est venues ici !"


"Quelque chose me dit que c’était son idée juste à elle, et que Rin a juste été traînée ici de force par Emi. Cela dit, on pourrait dire la même chose de Lilly et Hanako."

show lilly basic_weaksmile
with charachange


li "Eh bien, eh bien. Nous pouvons partager."

$ renpy.music.set_volume(0.001, 1.0, channel="music")

play sound sfx_door_creak


show lilly basic_surprised
show emi basic_hes
show rin basic_awayabsent
with charachange


"On peut entendre le grincement de la porte du toit au moment où Lilly finit sa phrase. Un moment de silence règne alors que l'attention de tout le monde se concentre sur la personne qui passe la porte."

show lilly basic_surprised:
    xanchor 0.5 xpos 0.4
show emi basic_hes:
    xpos 0.68
show rin basic_awayabsent:
    xpos 1.08
show bg school_roof at bgright
hide white
with charamove

show hanako basic_distant:
    xanchor 1.0 xpos 0.0 yalign 1.0
    easein 3.0 xanchor 0.0 xpos -0.06
    ease 1.0 ypos 1.17
with None


"Hanako arrive lentement vers nous, ses yeux rivés sur le sol, n’appréciant pas l'attention qu'elle attire. Elle se tend quand ses yeux croisent ceux de Rin."


"Je ne peux pas m’empêcher de lever un sourcil alors qu'elle arrive vers nous et s'assoit, faisant de son mieux pour éviter de lever les yeux, même lorsqu'elle sort et entame le pain de la cafétéria."

show rin basic_absent
show emi basic_grin
show hanako basic_normal:
    xanchor 0.0 xpos -0.06 ypos 1.17
with charachange


hi "Donc comment est-ce que Emi et toi vous vous êtes connues, d'ailleurs ?"

$ renpy.music.set_volume(1.0, 8.0, channel="music")

show lilly basic_smileclosed
show rin basic_awayabsent
with charachange


li "Emi est plus ou moins connue dans l’école pour ses capacités athlétiques. Elle est le membre le plus rapide du club d’athlétisme, elle a même battu Miki Miura à la compétition la semaine dernière."


"Miki Miura... ah, la fille bronzée qui est devant dans la classe. En prenant en compte sa taille et son corps athlétique, être capable de la distancer en course est un bel accomplissement."

show emi excited_amused
with charachange


"Regardant vers Emi, il est clair qu'elle est consciente de ce fait et en rayonne de fierté."

show emi excited_happy
with charachange


emi "Donc, Hisao. Tu as eu quelle note en anglais ?"


"Aïe."

show rin basic_absent
with charachange


hi "Sans commentaire."

show emi basic_annoyed
show rin basic_awayabsent
with charachange


emi "Bouuuh~."


"Elle gonfle les joues et fait la moue, mais il ne lui faut pas longtemps pour s'en remettre."

show emi excited_proud
with charachange


emi "Alors, je te dis ma note, et tu me dis la tienne. D'accord ?"

stop music fadeout 4.0

show rin basic_absent
with charachange


hi "Ok, ok."

show emi basic_closedhappy
show rin basic_awayabsent
with charachange


emi "D'accord, à trois, on dit tous les deux notre note."

show emi excited_joy
with charachange


emi "Un…{w=1.0} Deux…{w=1.0} Trois !{w=1.0}{nw}"

show emi basic_closedgrin
with charachange


$ doublespeak (hi, emi, "…", "Trente-deux !")


"Je rayonne d'un sourire machiavélique."

play music music_comedy

show hanako cover_smile
show lilly basic_cheerful
show rin basic_amused
show emi excited_sad
with charachange
with vpunch
play sound sfx_impact


emi "Ah ! Méchant ! Méchant, méchant, méchant, méchant !"

show rin basic_absent
with charachange


hi "C'est toi qui l'as dit, pas moi. Cela dit, le fait que tu aies réussi à avoir un score encore plus bas que le mien est assez remarquable."

show emi sad_grit
show rin basic_awayabsent
with charachange


emi "Grr~ !"


"Elle a l'air d'un petit terrier grognant en face d'un intrus. Ce n'est pas vraiment effrayant."

show lilly basic_displeased
show hanako basic_normal
with charachange


li "De toute façon, avoir une note plus haute que trente-deux n'est pas quelque chose dont on peut être fier. Et encore moins en dessous. Quelle que soit la matière."

show rin basic_absent
with charachange


hi "Oui, Lilly."

show rin basic_awayabsent
show emi sad_shy
with charachange


emi "Désolée, Lilly."

show lilly basic_smile
with charachange


li "Je pourrai t'aider avec l'anglais, si tu veux. Ça me ferait plaisir de-"

show emi basic_closedgrin
with charachange


emi "Non, non, pas besoin. Mais c'est gentil. Vraiment."

show lilly basic_reminisce
show hanako basic_smile
show rin basic_deadpanamused
with charachange


"Lilly a l'air légèrement déçue, ses espoirs de transmettre son savoir venant d’être détruits. À en juger par les rires de la part de Hanako et de Rin, Emi ne reçoit pas beaucoup de pitié de la part des autres."

stop music fadeout 0.5
$ renpy.music.set_volume(0.0, 4.0, channel="ambient")

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)

window show


"Alors que je ris joyeusement, ma voix est brusquement stoppée par ma poitrine qui se serre."

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)

window show


"Je m'assois en silence quelques secondes, me concentrant uniquement sur le battement de mon cœur. Ce n'est qu'une petite douleur, mais j'ai l'impression qu'elle grandit."

play music music_tragic fadein 0.5

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
with Dissolve (0.2)

window show


"Respire profondément... respire profondément..."

window hide

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

window show


"Je relève la tête pour essayer de rester attentif à ce qu'il se passe, mais je vois Emi se figer quand elle remarque du coin de l'œil l'expression de douleur sur mon visage."

show emi basic_hes
with charachange


emi "Hé, Hisao... ça va ?"

show hanako def_worry
show lilly basic_surprised
show rin basic_deadpanupset
with charachange


hi "Oui, je... vais bien..."

window hide

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

window show


"Je baisse les yeux et redouble d'efforts pour essayer de rester calme, je serre les poings et étouffe la douleur."

window hide

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

with Pause (0.7)

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

stop music fadeout 4.0

window show


"Cela prend un petit moment, mais la douleur, heureusement, commence à s’effacer."

$ renpy.music.set_volume(0.5, 4.0, channel="ambient")


"Quand je relève la tête, il y a un silence gênant qui plane et des visages inquiets. J'imagine que je vais devoir m'expliquer."

play music music_rain fadein 10.0


hi "Arythmie. Je vais bien, j'ai... juste eu une palpitation cardiaque."

show lilly basic_listen
with charachange


li "Tu es sûr ? On ne devrait pas aller chercher l'infirmier ?"

show hanako def_worry:
    ypos 1.0
with ease


"Entendant ça, Hanako se lève vite et commence à se ruer vers la porte."


hi "Hanako, stop. Lilly, je vais bien."

show rin basic_deadpan
with charachange


rin "Tu ressembles à une grosse tomate mouillée."


hi "Hein ?"


"Portant la main à mon front, je peux sentir les gouttes de transpiration et les enlève avec ma manche."


hi "Merci. Je te l'ai dit, je vais bien. Je suis juste... quelque peu fragile, j'imagine."

show hanako basic_worry
with charachange

show hanako basic_worry:
    ypos 1.17
with charamove

show emi sad_shy
show rin basic_deadpanupset
show lilly basic_sleepy
with charachange


"L’atmosphère est passée de la gaieté générale à une ambiance morose, la situation étant trop bizarre pour que qui que ce soit sache comment réagir."


"Et bien sûr, tout ceci est de ma faute. Ça devait arriver maintenant, avec les autres à côté de moi."

stop music fadeout 8.0

show lilly basic_weaksmile
with charachange


li "Oh, Emi ?"

show emi basic_hes
show rin basic_awayabsent
with charachange


emi "Mmh ?"


"En train de boire une brique de jus de fruit, elle lève la tête."

show lilly basic_smileclosed
with charachange


li "Je ne t’ai pas encore dit ma note d'anglais, n'est-ce pas ?"

show emi basic_annoyed
with charachange


emi "Ouais, bon. Tu es à moitié étrangère, alors ta note ne compte pas vraiment de toute façon."


"Étant intrigué, je me tourne vers Lilly."

show rin basic_absent
with charachange


hi "Tu as eu quelle note alors ?"

show lilly basic_cheerful


"Elle me sort un sourire effronté."

show rin basic_awayabsent
show lilly basic_planned
with charachange


li "Cent. Note maximale."

play music music_lilly fadein 0.5


"Pas possible. J'en laisse la bouche ouverte de stupeur."


"Prenant en compte que ces examens sont super durs même pour les natifs, je ne peux pas imaginer à quel point elle a dû travailler. Je suis sûr qu'elle a retenu tout le dictionnaire."

show rin basic_absent
with charachange


hi "C'est..."

show rin basic_awayabsent
show emi sad_pout
with charachange


emi "Tu vois ! Seulement quelqu'un à moitié étranger peut avoir un aussi bon score."

show rin basic_absent
with charachange


hi "“Tu vois”..."

show rin basic_awayabsent
show emi basic_closedsweat
with charachange


emi "Erh..."

show lilly basic_giggle
show hanako basic_smile
with charachange


"Lilly et moi sourions aux dépens d'Emi, sa réaction étant identique à la mienne, lorsque j'ai marché sur cette mine la première fois. L'origine étrangère de Lilly soulève une question, cela dit."

show rin basic_absent
with charachange


hi "Ah, c'est vrai. Tu pars demain pour l’Écosse, non ?"

show rin basic_awayabsent
show lilly basic_smile
with charachange


li "Oui. Emi a entendu des rumeurs à ce propos d'ailleurs, il semblerait que les nouvelles se répandent vite, sachant que je ne l'ai dit qu'à un ami de ma classe il y a quelques jours."

show emi sad_grin
with charachange


emi "Ça doit être bien d'aller de l'autre côté du monde en vacances."

show emi excited_happy
with charachange


emi "Tu pourras m'acheter un souvenir pendant que tu seras là-bas ?"

show rin basic_absent
with charachange


hi "Ne fais pas la timide surtout."

show lilly basic_giggle
with charachange


"Lilly émet un rire léger, elle s'attendait à la réaction gênée d'Emi."


"Le reste du déjeuner continue joyeusement, la bonne humeur d'avant ma palpitation étant revenue."

stop music fadeout 8.0

scene bg school_roof
show lilly basic_smileclosed:
    center
    ypos 1.2
with shorttimeskip


"Après les au revoir des autres personnes, seuls Lilly et moi restons."


hi "Hé, Lilly ?"


"Elle remballe les derniers ustensiles dans son sac et le ferme, avant de relever légèrement la tête."

show lilly basic_smile

with charachange


li "Mmh ?"


hi "Euh... merci d'avoir changé de sujet tout à l'heure. Je voulais le faire, mais je ne savais pas vraiment comment."


"Je voudrais bien être de meilleure humeur, mais entre la lettre d'hier, mon examen loupé et maintenant mon cœur faisant des siennes, cela rend les choses difficiles."

show lilly basic_weaksmile
with charachange


"Elle m'adresse un sourire indulgent. J’espère qu'elle n'a pas remarqué que je suis morose, mais la connaissant, elle s'en est sûrement rendue compte."


li "Emi est forte, mais elle est aussi humaine. On s’inquiète pour toi, Hisao."


hi "Attends, pourquoi je t’inquiète ?"

$ renpy.music.set_volume(0.5, 2.0, channel="ambient")

show lilly basic_displeased
with charachange


"Son sourire s'efface, son visage devenant sérieux."


li "Hisao, nous ne sommes pas ignorantes de ta situation."


li "Contr..."

show lilly basic_concerned
with charachange


"Elle s’interrompt brusquement, n'étant pas sûre de continuer sa phrase. Je souris doucement et pose ma main sur son épaule."

play music music_twinkle fadein 10.0


hi "Ne t’embête pas. Je m'inquiète pour moi-même, c'est suffisant. Je ne veux pas que vous portiez aussi mon fardeau."

show lilly basic_oops
with charachange


li "Mais..."


hi "Si vous vous en souciez, je devrai m'inquiéter de vos inquiétudes. Ça... complique trop les choses."


hi "Je vais bien, d'accord ?"

show lilly basic_reminisce
with charachange


"Pendant un moment elle a l'air perdue dans ses pensées, réfléchissant à comment réagir."

show lilly basic_weaksmile
with charachange


li "Hisao, il te reste du papier de l'emballage de notre déjeuner ?"


hi "Je... crois. Je vais voir."

play sound sfx_rustling


"Je fouille dans mon sac les restes du déjeuner et trouve une feuille de papier de l’emballage de mon sandwich."


"Me demandant la raison de tout ceci, je place la feuille de papier carrée dans la main de Lilly. Sans un autre mot, elle fait le tour de la feuille avec ses doigts."

show lilly basic_smile
with charachange


li "Ça devrait être suffisant..."


"Assis tous les deux sur le toit, les minutes qui s'écoulent nous rapprochant de la reprise des cours, elle pose la feuille sur le sol et commence son travail."

show lilly basic_smileclosed
with charachange


"En silence, je regarde ses doigts plier la feuille dans tous les sens avec une extraordinaire dextérité. Une petite pliure ici, une grande pliure là, ses doigts continuant lentement mais sûrement."


"Son expression est calme et sereine. Le fait que son visage soit face à l'horizon alors que la feuille est au sol rend la vision de son travail plus que curieuse."


"Ses épaules se relâchent un peu une fois qu'elle a fini. C'est seulement une fois qu'elle tient l'objet dans ses mains que je réalise ce que c'est."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene white
with dissolve

with Pause(0.1)

scene ev lilly_crane:
    truecenter
    zoom 1.1 subpixel True
    ease 15.0 zoom 1.0
with Dissolve(4.0)


"Une petite grue en origami."


"Un peu marron à cause de la couleur du papier utilisé, le résultat est plus que précis."


hi "Tu peux faire des origami ?"


li "J'ai appris comment faire quand j’étais plus jeune. Ça améliore un peu la dextérité."


hi "Ah..."


"Un peu déconcerté, je prends avec précaution le petit oiseau de ses mains pâles comme s'il allait se casser au moindre mouvement. Il semble être plutôt bien fait."
$ renpy.music.set_volume(1.0, 2.0, channel="music")

scene bg school_roof
show lilly cane_smile at center
with locationskip


"Nous attrapons tous les deux nos sacs et nous dirigeons vers la porte, Lilly déplie sa canne en même temps."

stop ambient fadeout 2.0

scene bg school_hallway3
with locationskip


"Je regarde encore l’œuvre de Lilly pendant que nous parcourons le couloir, sa main s'aidant de la rampe en métal pour se diriger."


"Elle a appris l'origami pour avoir une meilleure dextérité, l'utilisation de ses mains signifie tellement étant donné sa condition... ah, c'est donc ça."


"Je souris en réalisant la signification de l'oiseau."


"“Tout le monde ici doit trouver ses propres moyens de gérer son handicap. Tu n'es pas seul ici quand tu as des problèmes.”"


hi "Merci, Lilly. J’apprécie l'attention."

show lilly cane_cheerful
with charaenter


"Elle sourit tendrement et hoche la tête, n'ajoutant rien d'inutile, comme à son habitude."

show lilly cane_smileclosed
with charachange


li "Tout ce que je demande, c'est que tu prennes soin de toi, Hisao."


hi "Ne t’inquiète pas, je le ferai."

show lilly cane_smile
with charachange


li "Promis ?"


hi "Promis."

hide lilly
with charaexit

stop music fadeout 7.0


"Et sur ce, nous nous séparons."


"Pour être honnête, je ne sais pas ce qui me gêne le plus - le fait que je puisse mourir à tout instant, ou le fait que tout le monde le sache."


"Je pense que je vais juste prendre chaque jour comme il vient. Comme le cadeau dans ma main me le rappelle, je suis pas seul ici. Même si je suis comme ça, je ne suis pas seul."


"S'ils s’inquiètent, si n'importe qui s’inquiète, je sourirai."


"Je sourirai suffisamment pour que toutes leurs inquiétudes s'en aillent."

scene black
with dissolve



label fr_L8:

scene black
with dissolve

play sound sfx_normalbell

scene bg school_scienceroom
show muto normal at center
with locationchange


"Au moment où la sonnerie résonne, tout le monde lâche un soupir de soulagement."

play music music_happiness fadein 2.0


"La majeure partie de la matinée a été prise par une lecture soporifique sur la stœchiométrie, un sujet incompatible avec la chaleur qui règne dans la classe."

hide muto
with charaexit


"Sachant qu'il est inutile d'essayer de nous en apprendre plus, Mutou abandonne l’idée et commence à ranger ce qui est sur son bureau."

$ renpy.music.set_volume(0.7, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 0.5

show hanako basic_normal at center
with charaenter


"Alors que les élèves commencent à discuter, je vois Hanako se lever et venir vers ma table. Elle a été beaucoup moins absente récemment, ce qui me fait plaisir."

show hanako basic_smile
with charachange


ha "Bonjour Hisao."


hi "Salut. On va aller chercher Lilly, alors ? Il est presque l'heure pour elle de partir à l'aéroport."

show hanako cover_worry
with charachange


ha "Euh... à ce propos..."

show hanako basic_worry
with charachange


ha "Elle a dit qu'elle serait un peu retenue par les élèves dans sa classe."


"C'est assez logique. Sa classe sort habituellement un peu plus tôt que la nôtre, Lilly devrait déjà être là. Sa classe doit la retenir."


hi "Bah, c'est pas grave. On peut aller devant sa classe pour une fois, non ?"

show hanako emb_smile
with charachange


"Elle sourit et hoche la tête, nous prenons nos affaires et partons pour la classe 3-2."

stop ambient fadeout 1.0

scene bg school_hallway3
with locationchange


"Quand nous arrivons à notre destination, je m’arrête et m'amuse de la scène qui se passe en classe."


"Une des plus petites élèves de la classe tient Lilly serrée dans ses bras, sa tête atteignant à peine son menton. Ses autres amis sont rassemblés autour d'elle. Lilly se contente de sourire et de rendre l'embrassade qui lui est offerte."


"Je pense que Lilly est plutôt populaire. Comparée au statut de dictateur sévère mais équitable de Shizune en 3-3, Lilly semble plus être comme une mère pour la 3-2, sans mentionner sa taille ou son apparence."


"L'attitude ostensiblement détachée de Kenji alors qu'il remballe ses affaires et sort par l'autre porte de la classe, était à prévoir. Je suis sûr qu'il ne doit pas apprécier toute l'agitation faite par le départ de Lilly."


"Regardant à côté de moi et voyant Hanako suivre mon regard, je décide enfin d'entrer dans la classe."

$ renpy.music.set_volume(0.7, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 0.5

scene bg school_room32
show crowd at center
show lilly basic_surprised at center
with locationchange


hi "Bonjour, Lilly, je suis avec Hanako."

show lilly basic_surprised at twoleft
show crowd at bgleft
show bg school_room32 at bgleft
with dissolvecharamove

show hanako emb_downtimid at tworight
with charaenter


"Hanako rétrécit à vue d’œil face au chahut autour de Lilly. Elle a beau essayer, je doute qu'elle surpasse complètement sa timidité maladive un jour."

show hanako emb_emb at tworight
with charaenter


ha "Bonjour..."


"Lilly réussit à estimer notre position, ses camarades de classe se décollent d'elle sans protester. Une légère exaspération est inscrite sur le visage de Lilly, je ne peux pas lui en vouloir."

show lilly basic_smileclosed
with charachange


li "Bonjour Hisao, bonjour Hanako. A-t-on encore beaucoup de temps avant de devoir partir ?"


"Je regarde rapidement ma montre. On a dix, voire quinze minutes avant de devoir se mettre en chemin."


hi "Ouais, on a encore un peu de temps. Il est trop tôt pour que tu t'inquiètes."


"Camarade de classe" "Ah, c'est toi Hanako ?"


"Oh oh. Je crois qu'on vient d’être capturés dans la toile sociale de Lilly."


"La fille est probablement aussi mal voyante que Kenji, vu ses verres en cul de bouteille. Ses cheveux courts lui donnent un air qui correspond à son expression excitée."

show hanako def_shock
with charachange


ha "B-bonjour... euh...'"


"Elle prend la main de Hanako et la secoue avec enthousiasme. Je ne comprends vraiment pas comment les filles peuvent agir aussi familièrement avec quelqu'un qu'elles ne connaissent que par une relation commune."


"Pendant que Hanako échange des salutations nerveuses, je regarde autour de moi à la recherche de mon voisin. J'ai beau chercher, il semble être sorti de la classe sans que personne ne le remarque."


"Je réfléchis un moment à une carrière possible qui pourrait bénéficier de sa compétence spéciale, avant de revenir à des choses plus importantes."

show lilly basic_smile
show hanako cover_distant
with charachange


"Lilly semble contente, même si elle est quelque peu réservée face à l'enthousiasme qu'attire Hanako. Elle ne le remarque peut-être pas, mais Hanako est beaucoup moins paniquée que ce que j'aurais cru."


"Me frayant un chemin à travers la troupe d’étudiants, j'arrive finalement à l'atteindre."


hi "Ne t’inquiète pas, Hanako va bien."

show lilly basic_weaksmile
with charachange


li "Merci. J'avais peur qu'elle puisse être quelque peu étouffée."


"Camarade de classe" "Ne t’inquiète pas, on sera gentilles !"

show lilly basic_concerned
with charachange


"Lilly et moi grimaçons à l'unisson. Le sourire nerveux de Hanako s'intensifie alors que deux autres filles arrivent pour la rencontrer."


"C'est assez impressionnant de voir qu'il y a juste un mois elle n'aurait pas été capable de tolérer une situation similaire. Quand je l'ai rencontrée pour la première fois, on était juste deux, elle est sortie en courant de la bibliothèque."


hi "Donc, tu as tout ce dont tu as besoin ?"

show lilly basic_smile
with charachange


li "Tout est prêt. J'ai juste besoin de passer par ma chambre pour prendre mes sacs, et Hanako et moi devons nous changer."


hi "J'imagine qu'on ferait mieux de se dépêcher alors. Hanako ?"

show hanako cover_bashful
with charachange


"La tête de Hanako se tourne vers moi en une demi-seconde, appréciant visiblement la chance de s'extirper du petit groupe agglutiné autour d'elle."

show hanako basic_bashful
with charachange

stop music fadeout 2.0


ha "Je-j'arrive !"

stop ambient fadeout 0.5

scene bg hosp_ext
with shorttimeskip

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 1.0
play music music_tranquil fadein 3.0


"Le long trajet en taxi jusqu’à l’aéroport est étonnamment agréable, malgré le fait qu'on soit un peu serrés sur la petite banquette arrière. Enfin, “malgré” n'est peut-être pas le bon mot."


"Lilly paie le chauffeur pour la course pendant que nous sortons, Hanako regardant dans tous les sens. Heureusement il n'y a pas beaucoup de monde, la plupart des gens étant à l’intérieur du bâtiment plutôt que dehors."

show akira basic_boo at tworight
show hideaki bored:
    yalign 1.0 xanchor 0.5 xpos 0.9
with charaenter


"On remarque facilement Akira et Hideaki en train de discuter contre un muret. Un grand sac noir de voyage, avec des roues et des anses, est à côté d'eux."

show hideaki surprise_up
with charachange


"Hideaki est le premier à nous remarquer, et le dit à Akira qui nous fait des grands gestes de la main."

show akira basic_laugh
with charachange


aki "Hé ! Hé~ !"


"J'attrape le gros sac de Lilly qui me remercie avec un hochement de tête et nous les rejoignons."

show akira basic_smile
show hideaki normal
with charachange


aki "J'ai pris tout ce qu'il me fallait, et toi ? Tu n'as pas oublié le billet d'avion ?"

show lilly basic_smileclosed_cas at twoleft
with charaenter


li "J'ai tout, ne t’inquiète pas. Et toi ?"

show akira basic_laugh
with charachange


aki "Ouaip. Je l'ai aussi. On peut y aller."

show hideaki evil
with charachange


hh "Le retrouver n'a pas été sans difficulté..."

play sound sfx_impact

show akira basic_kill
show hideaki ohshit
with vpunch


"Cette remarque lui vaut de se faire écraser la tête par une prise ferme d'Akira."

show akira basic_boo
show hideaki sad
with charachange


aki "Haha, ouais, j'avais oublié qu'il était dans la poche de mon pantalon. Pantalon que j'avais mis dans la machine à laver..."

show lilly basic_concerned_cas
with charachange


li "Oh non..."

show akira basic_laugh
with charachange


aki "Ne t’inquiète pas, ne t’inquiète pas. Tu savais que tu pouvais imprimer tes billets sur Internet de nos jours ? C'est vraiment cool."

show hideaki bored
with charachange


"L'expression sur le visage de Hideaki me montre qu'ils n'y ont pas pensé tout de suite. Ça aurait pu être pire j'imagine."

show lilly basic_weaksmile_cas
with charachange


li "On ferait mieux d'y aller. Le check-in devrait être ouvert."

show akira basic_lost
with charachange

stop music fadeout 2.0


aki "Ouais, t'as raison."


"Il y a une certaine mélancolie dans leurs voix. Ne rien dire à ceux laissés sur place, revoir leur famille après toutes ces années doit être énorme pour eux."

show hanako emb_sad_cas at center
with charaenter

play music music_serene fadein 4.0

ha "Lilly…"


"Hanako entoure Lilly de ses bras pour lui dire au revoir, une embrassade qui est réciproque. Lilly et moi partageons une brève embrassade à notre tour, et nous disons au revoir."


"À côté de nous, Akira et Hideaki se séparent aussi et se disent un mot ou deux. Ça aurait probablement eu l'air bien s'il n'y avait pas une différence de taille presque comique entre eux deux."

show lilly basic_smile_cas
show akira basic_smile
show hanako emb_downtimid_cas
show hideaki normal
with charachange


"Lilly attrape le bras de sa sœur une fois que les au revoir sont finis, et elles passent les grandes portes vitrées."

show lilly back_smileclosed_cas
with charachange


li "Au revoir Hisao, Hanako !"

show akira basic_laugh
with charachange


aki "À plus ! Ne fais rien d'idiot, Petit !"

hide lilly
hide akira
with charaexit


"Nous leur faisons des signes jusqu’à ce qu'ils disparaissent dans la foule de gens à l’intérieur."


"Et sur ce... nous nous retrouvons seuls."


hi "Bon... voilà."

show hideaki bored
with charachange


"Je me tourne vers Hideaki qui commence déjà à s'en aller."


hi "À plus."

show hideaki bored_up
with charachange

show hideaki invis:
    xpos 1.0
with dissolvecharamove

hide hideaki
with None


"Il nous fait un signe de la main, d'une manière semblable à ce qu'aurait pu faire Akira. En fin de compte, il ne reste plus que Hanako et moi, qui nous tenons à l'extérieur."

show hanako emb_timid_cas
with charachange


"Je pose ma main sur son épaule. Elle regarde en direction des portes du bâtiment, comme si elle pouvait les revoir une seconde avant qu'ils ne disparaissent."


hi "Ne t’inquiète pas, ça passera vite."

show hanako basic_normal_cas
with charachange


"Elle hésite un moment, puis hoche la tête."


"La chaleur étouffante de l’été nous accompagne dans notre marche jusqu’à l’arrêt de bus."

hide hanako
with charaexit


"C'est étrange, vraiment. Juste quand je commençais à voir Lilly différemment, elle part comme pour rejoindre son passé."


"D'une certaine façon, c'est ce que je fais depuis que je suis arrivé à Yamaku."


"J'ai beau beaucoup penser à ce qui m'est arrivé, je suis tout sauf unique. Tout le monde a ses propres problèmes et des chemins différents à emprunter."


"Pourtant je n'arrive pas à savoir comment je vais faire. Ma vie a été presque réinitialisée, et je n'arrive pas à trouver quoi que ce soit de satisfaisant pour remplir le vide en moi."


"Peut-être que le départ de Lilly est une bonne chose pour moi. Sans elle sur qui me reposer, je vais devoir prendre plus sur moi. Je vais devoir être là pour Hanako aussi."


"C'est étrange tous ces changements aussi rapidement après mon séjour de plusieurs mois à l'hôpital, où j'avais l'impression d'être séparé de la réalité. Mais tout ceci me donne des raisons supplémentaires de bien faire."


"Je ne peux laisser aucune opportunité me glisser entre les doigts dans ma tentative de reconstruire ma vie."

stop music fadeout 3.0
stop ambient fadeout 3.0

window hide

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
