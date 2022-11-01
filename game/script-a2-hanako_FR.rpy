label fr_H2:

scene bg school_miyagi
show hanako emb_downsmile_close
with None

play sound sfx_doorknock2

show hanako emb_timid_close
with charachange


"Pendant que nous mettons les pions en place, la porte s'ouvre."

play sound sfx_dooropen

show bg school_miyagi at bgright
show hanako emb_timid_close at tworight
with charamove

show lilly basic_smileclosed at twoleft
with charaenter


li "Bonjour."

play music music_lilly fadein 4.0

show hanako emb_emb_close
with charachange

ha "Lilly…"


hi "Oh, salut Lilly. Tu as fini ?"

show lilly basic_smile at twoleft
with charachange


li "Vous êtes là tous les deux ? Parfait. Notre professeur a enfin réussi à obtenir de l'aide, donc j'ai pu m'en aller. Vous êtes là depuis tout à l'heure ?"


hi "Pratiquement, nous avons juste joué un peu aux échecs."

show hanako emb_smile_close
with charachange


ha "T-tu veux une tasse de thé ?"

show lilly basic_weaksmile at twoleft
with charachange


li "En fait, je pense que ce serait une bonne idée qu'on sorte un peu..."

show hanako def_worry_close
with charachange


"L'expression sur le visage de Hanako montre qu'elle n'a pas vraiment envie de sortir, même si elle ne sait pas ce que veut faire Lilly."


"Cela fait bizarre de dire à voix haute ce que Hanako affiche sur son visage, mais Lilly ne peut pas le voir."


hi "Je... je pense qu'on devrait juste rester ici..."

show lilly basic_surprised at twoleft
with charachange


li "Vraiment ? C'est tellement bondé ici que je pense qu'on devrait sortir de l'école et aller au salon de thé."

show hanako emb_blushtimid_close
with charachange


ha "Tu veux dire le S-Shanghai ?"

show lilly basic_smileclosed
with charachange


li "Bien sûr, vu que tout le monde est au festival, ça devrait être pratiquement vide."


hi "Salon de thé ?"

show lilly basic_weaksmile
with charachange


li "Oh, c'est vrai, tu ne le connais probablement pas."

show lilly basic_smile
with charachange


li "Il y a une maison de thé pas loin d'ici, à laquelle on va souvent."


hi "Ça a l'air bien. Hanako, qu'est-ce que tu en penses ?"

show hanako defarms_shock_close
with Dissolve(0.2)

show hanako def_worry_close
with charachange


"Hanako est un peu effrayée à l'idée de devoir participer à la conversation, mais au moins, elle l'est moins qu'avant."

show hanako cover_bashful_close
with charachange


ha "Si... si c'est le Shanghai, alors ça ira."

show lilly basic_planned
with charachange


li "Alors c'est décidé. Allons-y."

show hanako basic_bashful
with charadistant


"Hanako et moi nous levons et interrompons notre partie avant même qu'elle ait commencé."


"Avant que je puisse faire quoi que ce soit, Hanako range les pions dans une petite boîte et la remet à son emplacement initial."


hi "On est prêts maintenant. On te suit."

stop music fadeout 8.0

scene bg school_hallway3
with locationchange

show hanako emb_smile at Transform(xanchor=0.5, xpos=0.58)
show lilly basic_smileclosed at Transform(xanchor=0.5, xpos=0.42)
with charaenter


"Hanako se place aux côtés de Lilly et nous sortons dans les couloirs de l’école."

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")

play ambient sfx_crowd_outdoors fadein 1.0

scene bg school_gate_ss
with locationskip


"Elles me font passer à travers une série de portes que je ne connais pas et nous sortons du bâtiment par le côté opposé au festival."


"Grâce au bâtiment qui nous sépare de la foule, le bruit du festival est devenu un murmure."


hi "C'est étrange, je pensais que la plupart des gens allaient commencer à partir maintenant..."

show hanako emb_downtimid_ss at Transform(xanchor=0.5, xpos=0.58)
show lilly basic_smile_ss at Transform(xanchor=0.5, xpos=0.42)
with charaenter


li "Ils restent probablement pour voir les feux d'artifice."


hi "Feux d’artifice ?"

show lilly basic_weaksmile_ss
with charachange


li "Oui, apparemment l’école a préparé tout un spectacle. Beaucoup de gens sont venus de la ville juste pour le voir."


"La décision de Lilly de quitter l’école semble logique maintenant. Hanako aurait probablement du mal avec la ville entière sur les terrains de l’école."

stop ambient fadeout 7.0
play music music_tranquil fadein 3.0

scene bg school_road_ss
with locationchange


"Pour la deuxième fois depuis que je suis arrivé à Yamaku, je me retrouve à descendre cette route avec Lilly."


"C'est seulement maintenant, alors que je n'entends presque plus le bruit du festival, que je me rends compte à quel point il est bruyant. J'entends mes oreilles siffler légèrement à cause de l'agression qu'elles ont subie."

show hanako emb_emb_ss at Transform(xanchor=0.5, xpos=0.58)
show lilly basic_smileclosed_ss at Transform(xanchor=0.5, xpos=0.42)
with charaenter


"Hanako s'accroche à Lilly, mais arrive quand même à la guider. Ça, et éviter le regard des occasionnels piétons que nous croisons, semblent totalement l'accabler."


"Elle lève rarement les yeux du sol et ne dit pas un mot."


"Lilly, quant à elle, maintient son attitude quelque peu guindée, comme à son habitude. Il est évident qu'elle fait des efforts volontaires avec son apparence, plutôt que de se cacher comme Hanako le fait."


"C'est étonnant de voir à quel point elles sont différentes dans leur façon d'être en dehors de Yamaku. Cela dit, il est évident qu'elles font toutes les deux des efforts."

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

window hide

nvl clear

$ renpy.music.set_volume(0.5, 1.0, channel="music")

nvl show dissolve


n "\n\n\nÀ Yamaku, tout le monde est “spécial” ce qui annule la “spécificité” de tous."


n "Mais une fois qu'on s'aventure en dehors de l'école, nous retournons à notre statut de “spéciaux”."


n "Surtout quand on porte notre uniforme. C'est comme tenir une pancarte autour de notre cou qui invite les gens à deviner ce qui ne va pas chez nous."


n "Je suis surpris qu'il y ait autant d'étudiants qui le gardent. Ceci dit, avec les cannes et les fauteuils roulants qui sont communs chez les étudiants, j'imagine que ça ne change pas grand-chose."


n "\nOu peut-être que je suis le seul qui voit ça comme un stigmate ? Peut-être qu'on s'y habitue après un moment, comme avec n'importe quel autre uniforme."

nvl hide dissolve

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear

scene bg suburb_shanghaiext_ss
with locationskip

window show


"La maison de thé semble tout ce qu'il y a de plus classique depuis l'extérieur. Un bâtiment ordinaire avec des décorations typiques."


"Ça ressemble aux endroits à côté desquels on passe sans y penser, juste un autre café banal parmi tant d'autres."


"Si Hanako n'avait pas tiré Lilly vers l'entrée, j'aurais continué ma marche sans même me rendre compte qu'il était là."

play sound sfx_storebell

scene bg suburb_shanghaiint at Fullpan(5.0, dir="right")
with locationchange

stop music fadeout 6.0


"L’intérieur de la maison de thé est beaucoup plus traditionnel. Tout semble être avoir été fait du même arbre, que ce soit le comptoir, les bancs, ou même les tables."


"Mais la caractéristique la plus étonnante du salon est son manque de vie. Je crois que je peux entendre quelque chose bouillir au fond, mais en dehors de ça, la pièce est silencieuse."


"Ne sachant pas quoi faire, nous attendons simplement près de l'entrée, obéissant au panneau disant “Veuillez attendre ici qu'on vienne vous servir.”."


hi "Erh, c'est fermé ou quoi ?"

stop music
play sound sfx_impact2

show yuukoshang panic_up:
    xalign 0.5 yanchor 1.0 ypos 1.5 alpha 0.0
    easein 0.3 ypos 1.0 alpha 1.0
show bg suburb_shanghaiint at right
with vpunch


"Le son d'une chaise qui tombe résonne dans la salle vide, et une tête se lève d'une table."

play music music_comedy fadein 0.5

show yuukoshang neurotic_up:
    ypos 1.0 alpha 1.0
with charachange


yu "Je n’étais pas en train de dormir et bienvenue au Shanghai !"


"Yuuko, portant un tablier et tenant un menu, se dépêche de nous saluer. Ses lunettes mal alignées et ses cheveux en bataille nous font douter de sa phrase précédente."


"Mais savoir si elle dormait ou non n'est pas la première question qui me vient à l'esprit."


hi "Tu travailles ici maintenant ? Et la bibliothèque ?"

show yuukoshang smile_down
with charachange


yu "Hein ? Lilly ? Hisao ?"

show yuukoshang neurotic_up
with charachange


yu "Bienvenue au Shanghai !"

show yuukoshang noglasses_up at Transform(ypos=1.25)
with Dissolvemove(0.2)

play sound sfx_dropglasses

with Pause(0.3)

show yuukoshang noglasses_up at center
with charamove


"Yuuko, encore en train de se réveiller, se penche rapidement et fait tomber ses lunettes dans l'action."


yu "Wah ?! Mes lunettes..."


"Alors que je lui ramasse ses lunettes, Lilly explique la situation."

show yuukoshang noglasses_up at tworight
show bg suburb_shanghaiint at center
with charamove

show lilly basic_weaksmile at twoleft
with charaenter


li "Yuuko travaille à temps partiel ici aussi. C'est une des raisons pour lesquelles nous aimons venir ici."

show yuukoshang neurotic_up
with charachange


"Yuuko récupère ses lunettes et les remet maladroitement."


yu "Oui... c'est vrai... merci..."

show yuukoshang neutral_down
with charachange


yu "Est-ce que je vous montre votre table ?"

show yuukoshang worried_up
with charachange


yu "Il n'y a personne d'autre ici donc vous pouvez choisir votre table et prendre ce que vous voulez, mais il faudra attendre un peu, vu que je dois tout préparer moi-même..."

show lilly basic_smile at twoleft
with charaenter


li "Ça ira, Yuuko. Juste un thé noir et une assiette de sandwiches feront l'affaire."

show yuukoshang happy_down
with charachange


yu "D'accord ! Je m'en occupe tout de suite !"

hide yuukoshang
with charaexit

show lilly basic_smile at center
show bg suburb_shanghaiint at bgright
with charamove


"Yuuko se dépêche de retourner derrière le comptoir, nous laissant debout à l'entrée."


"Elle pousse la demi-porte avant de réaliser qu'elle ne nous a pas placés."


yu "Je suis désolée ! Je suis désolée ! Asseyez-vous où vous voulez ! Je reviens vite !"

stop music fadeout 3.0

hide lilly
with charaexit

show bg suburb_shanghaiint at bgleft
with charamove


"Suivant son conseil, j’amène Lilly à la table la plus proche alors que Hanako nous suit."

show lilly basic_smileclosed:
    twoleft
    ease 1.0 ypos 1.2
show hanako basic_normal:
    tworight
    ease 1.0 ypos 1.17
with Dissolve(1.0)


"Alors que je m'assois à côté de Lilly, je réalise à quel point cet emplacement est pratique pour Hanako."


"Les tables isolées par des séparateurs nous préservent complètement du reste de la salle. Il n'y a pas l'air d'avoir d'autres clients."


"Tout ce qui se trouve là, des coussins aux bancs, et même les pots d'épices, ont l'air vieux mais pas nécessairement usés."


"Je me demande si Lilly choisit des endroits comme ça exprès pour Hanako. Elle semble bien être le type de personne qui irait loin pour satisfaire Hanako."

play music music_another fadein 4.0

show lilly basic_weaksmile:
    ypos 1.2
with charachange


li "Donc, Hisao, je ne savais pas que tu jouais aux échecs..."


hi "Ben, pas très bien, mais je sais comment y jouer."

show lilly basic_smile
with charachange


li "J'imagine que la question est... qui a gagné ?"


"Le sourire innocent de Lilly me fait hésiter. Je ne veux pas avoir l'air de me vanter de ma victoire contre Hanako."

show hanako cover_bashful:
    ypos 1.17
with charachange


ha "C-C'est Hisao."


hi "Oui... mais, euh, pas de beaucoup..."


"Zut. Dire ça à voix haute me donne l'impression d'avoir fait quelque chose de terrible."

show lilly basic_giggle
with charachange


li "Bien joué, Hisao. Tu as réussi là où j'ai échoué."


hi "Merci. Je n'avais pas joué depuis longtemps, ça fait du bien de s'y remettre."

show hanako basic_smile
with charachange


ha "O... oui... C'était bien."


"Hanako joue un peu avec ses cheveux et regarde dans le vide en répondant, mais affiche un léger sourire."


"C'est une réaction un peu plus extrême que ce à quoi je m'attendais, mais cela reste mignon de la part de Hanako."

show hanako defarms_shock at Transform(xpos=0.8)
show lilly basic_surprised at Transform(xpos=0.2)
with Dissolvemove(0.5)

show yuukoshang worried_up at center
with charaenter


"Ça me prend un peu par surprise et c'est seulement l'entrée cataclysmique de Yuuko qui relance la conversation."


hi "Ça va, Yuuko ? Tu as besoin d'aide ?"

show yuukoshang neurotic_up
show hanako def_worry
with charachange


yu "Ça va ça va ça va. Je dois bien le faire, c'est mon travail."

show yuukoshang worried_up
with charachange


"On voit à son expression qu'elle est concentrée. Elle regarde attentivement le plateau qui est dans ses mains, comme si le regarder allait l'aider à rester stable."

show yuukoshang worried_up at centertremble
with charachange


"Cela dit, ce n'est pas très efficace. Les tasses bougent un peu, s’entrechoquant occasionnellement."

show yuukoshang worried_up at Transform(ypos=1.1)
with ease

show yuukoshang worried_up at center
with ease


"En faisant attention, Yuuko pose le plateau sur la table sans dégâts."

show yuukoshang happy_down
with charachange


yu "Voilà !"


hi "Hum, bien joué."

show lilly basic_weaksmile
with charachange


li "Merci, Yuuko."

show yuukoshang neutral_down at Transform(ypos=1.2)
with Dissolvemove(0.2)

with Pause(0.2)

show yuukoshang neutral_down at center
with ease


"Yuuko se penche rapidement avant de répondre."

show yuukoshang closedhappy_down
with charachange


yu "Je vous en prie."

show lilly basic_smile
with charachange


li "Tu voudrais nous rejoindre ? Il y a quelque chose dont je voudrais parler avec toi à propos de la dernière commande, si ça ne te gêne pas..."


"Ah, c'est vrai. Lilly et Yuuko discutaient d'une commande de livres quand j'ai rencontré Hanako."


"Elles discutaient à propos de Lilly qui aidait avec le braille..."

show yuukoshang neurotic_up
with charachange


yu "Ah... oui. On n'a pas eu l'occasion d'en parler, hein ?"

show yuukoshang neurotic_up at Transform(ypos=1.17)
with charamove


"Yuuko s'assied à côté de Hanako."


"Apparemment, son dévouement à ce travail se limite à sa concentration, une fois qu'elle est perdue, c'est fini."

show yuukoshang smile_down
with charachange


yu "Je serai à la bibliothèque demain après-midi si tu veux réessayer..."

show lilly basic_cheerful
with charachange


li "Ça me semble bien. Je viendrai après les cours."

show hanako emb_timid
with charachange


ha "Euh... L-Lilly..;"

show lilly basic_oops
with charachange


li "Oh mince, c'est vrai. Demain c'est lundi. Comment ai-je pu oublier ?"


"Je commence à me sentir un peu hors du coup, là. D'un autre côté c'est un peu normal, je suis là depuis à peine une semaine, il est impossible pour moi de connaître l'emploi du temps de tout le monde."

show lilly basic_weaksmile
with charachange


li "Eh bien, peut-être qu'on pourrait trouver un autre arrangement."

show lilly basic_smile
with charachange


li "Yuuko, tu seras à la bibliothèque plus tard dans la semaine ?"

show yuukoshang worried_up
with charachange


yu "Mmh, peut-être, mais c'est déjà en retard..."

show hanako emb_downsad
with charachange


ha "E-et il y a certaines... choses dont j'ai b-besoin..."

show lilly basic_listen
with charachange


li "Ça peut devenir gênant..."


"Lilly réfléchit une seconde avant de trouver une réponse."

show lilly basic_planned
with charachange


li "Je me demande si on pourrait obtenir l'aide de quelqu'un, si besoin est..."


hi "Mh, pour faire quoi ? J'ai perdu le fil il y a un moment déjà..."


"Être volontaire pour quelque chose sans savoir de quoi il s'agit, ce n'est pas vraiment mon truc."


"Et moi qui croyais être sorti d'affaire quand je me suis échappé des griffes du Conseil des Étudiants et leurs tentatives répétées de me recruter."

show lilly basic_smileclosed
with charachange


li "Oh, bien sûr. L'autre jour j'aidais Yuuko à trier les nouveaux livres en braille dans la bibliothèque."

show lilly basic_weaksmile
with charachange


li "Mais Hanako et moi avons l'habitude de faire des courses le lundi après-midi, c'est plus calme en semaine que le week-end."


li "La dernière semaine, on n'a pas pu y aller parce qu'il y avait le festival. J'ai réussi à trouver un moment plus tard dans la semaine, mais Hanako n'a pas pu."


hi "Vu que je ne peux pas lire le braille, j'imagine que tu voudrais que je fasse les courses avec Hanako ?"

show lilly basic_smile
show hanako emb_timid
with charachange


li "Exact. Tu m'as beaucoup aidée l'autre jour."


hi "Je crois que ça ira. Hanako, qu'est-ce que tu en penses ?"

show hanako basic_smile
with charachange


ha "S-si ça ne te gêne pas..."


hi "Bien sûr que non. Je ne suis pas encore familiarisé avec les magasins des environs, donc c'est une bonne idée."

show hanako basic_bashful
with charachange


ha "D-d'accord."

show lilly basic_smileclosed
with charachange


li "Maintenant que tout cela est réglé, si on buvait notre thé ?"


"C'est maintenant que je remarque que notre thé est là depuis tout ce temps, et qu'il se refroidit doucement."

show yuukoshang panic_up
with charachange


yu "C'est de ma faute ! Laissez-moi vous le verser..."


"Yuuko tend les bras pour l'attraper, mais je l’arrête, elle n'a pas l'air d’être en état de le verser comme il faut."


hi "C'est bon, je m'en occupe. Tu as déjà fait le thé et les sandwiches, tu as rempli ton rôle de serveuse, non ?"

show yuukoshang neurotic_up
with charachange


yu "Je... J'imagine."


"Yuuko se relaxe un peu, mais semble toujours aussi stressée pendant que je verse le thé dans les tasses."

stop music fadeout 1.0
play ambient sfx_fireworks

show white
with Dissolve(0.1)

hide white
show fireshine
show hanako defarms_shock
show yuukoshang panic_up
show lilly basic_surprised
with charachange


"Alors que je suis sur le point de croquer dans le sandwich, on entend un grondement bruyant suivi d'un flash de lumière venant de l'extérieur."

show lilly basic_weaksmile
show yuukoshang smile_down
show hanako emb_timid
with charachange


li "Ah, apparemment ça a commencé."

hide fireshine
show bg misc_sky_ni as front
show fireworks
with locationchange


"C'est seulement maintenant, alors que que je regarde à l’extérieur, que je vois qu'il fait nuit noire."


"Des flèches d’étincelles se lancent vers le ciel pour exploser dans un feu d'artifice en forme de fleur."

hide fireworks
hide front
show fireshine
show yuukoshang happy_down
with locationchange


yu "Allons voir !"

show yuukoshang panic_up
with charachange


yu "Oh... désolée Lilly..."

show lilly basic_ara
with charachange

show hanako_fw behind bg:
    truecenter zoom 1.05 subpixel True
    ease 22.0 zoom 1.0
show ev hanako_shanghaiwindow behind hanako_fw:
    truecenter zoom 1.05 subpixel True
    ease 22.0 zoom 1.0
with None


li "Ne vous privez pas pour moi. D’après ce que j'ai entendu, on n'est pas si mal placés pour voir le feu d'artifice."

play music music_serene fadein 4.0

hide fireshine
hide bg
hide hanako
hide lilly
hide yuukoshang
with locationskip


"À l'exception de Lilly, nous nous précipitons à la fenêtre de la maison de thé pour voir le spectacle."


"Les jets de lumières se reflètent sur les visages souriants de Yuuko et Hanako, et pendant une seconde j'en oublie de regarder par la fenêtre."


"Dans ce nouveau monde, il y a certaines choses qui ne changent pas."


"Je crois que c'est pour ça que l'école fait toute une histoire du festival. C'est une chance de montrer qu'on est tous pareils."

stop ambient fadeout 3.0

hide hanako_fw
with Dissolve(1.0)


"Le spectacle finit trop rapidement, les feux d'artifice sont chers, même pour une école comme ça."

scene bg suburb_shanghaiint at bgright
with locationchange


"Avant que nous retournions à notre thé et nos sandwiches, Hanako se tourne vers moi."

show hanako emb_downsmile_close
with charaenter


ha "Hum, m-merci pour aujourd'hui."

show hanako emb_smile_close
with charachange


ha "...et demain."


hi "T’embête pas, je ne pense pas que j'aurais supporté la foule non plus."


hi "Dans des jours comme ça, c'est plus relaxant de passer du temps loin de tout le reste, tu ne crois pas ?"

show hanako basic_normal_close
with charachange


ha "O-ouais."


hi "On a fait attendre ce thé trop longtemps. Retournons le boire."

show hanako basic_bashful_close
with charachange


ha "D-d'accord."

stop music fadeout 6.0

hide hanako
with charaexit

show bg suburb_shanghaiint at bgleft
with charamove

show lilly basic_smileclosed:
    yanchor 1.0 xanchor 0.5 ypos 1.2 xpos 0.2
show yuukoshang neutral_down:
    yanchor 1.0 xanchor 0.5 ypos 1.17 xpos 0.5
with locationchange

show hanako basic_smile:
    yanchor 1.0 xanchor 0.5 ypos 1.0 xpos 0.8
    easein 1.0 ypos 1.17
with charaenter


"Nous retournons à notre table et à notre collation."

show lilly basic_smile
with charachange


li "Ça avait l'air impressionnant. Plus gros que l’année dernière du moins."

show yuukoshang happy_down
with charachange


yu "Ouais il était bien ! C'est la première fois qu'il était aussi gros."


yu "C'est de mieux en mieux chaque année !"

show lilly basic_weaksmile
with charachange


li "J'ai bien peur que pendant ce temps, le thé se soit refroidi."

show yuukoshang panic_up at center
with Dissolvemove(0.2)

play music music_ease fadein 0.5


yu "Oh non ! Je vais en refaire ! C'est de ma faute !"


hi "Calme-toi, Yuuko, ce n'est la faute de personne."


"Je bois une petite gorgée de ma tasse, pour prouver ce que je viens de dire."


hi "Il n'est pas mauvais froid de toute façon. C'est comme un thé glacé."

show yuukoshang worried_up
with charachange


yu "Vraiment ?"


hi "Oui, vraiment. Si tu ajoutes un peu de sucre, c'est plutôt bon."

show yuukoshang neurotic_up
with charachange


yu "Tu es sûr ?"


hi "Absolument. Maintenant, allons nous asseoir et finir ça ensemble."

show yuukoshang smile_down
with charachange


yu "D-d'accord."

show yuukoshang smile_down at Transform(ypos=1.17)
with charamove


"Yuuko ne semble pas convaincue, mais s'assoit quand même."


"Elle prend avec précaution cinq cuillères à café de sucre et les ajoute à son thé."


hi "Erh, j'ai dit un peu de sucre..."

show yuukoshang neutral_down
with charachange


yu "Je sais, mais j'aime mon thé sucré."


"Curieux, je regarde dans sa tasse. Comme prévu, le sucre a du mal à se dissoudre dans le thé."


"Elle remue sa cuillère deux fois avant de soulever la tasse et de boire son contenu en une seule gorgée."

show yuukoshang happy_down
with charachange


yu "Tu as raison ! C'est pas mauvais du tout !"


hi "Erh, bon..."


"Je regarde Lilly et Hanako, qui ont déjà toutes les deux fini leur thé."


"Ne voulant pas les retenir, j'utilise sa tactique et finis mon thé d'une seule traite."


hi "Bon, il semblerait qu'on ait tous fini."

show lilly basic_smile
with charachange


li "On rentre maintenant ou vous avez encore faim ?"

show yuukoshang neurotic_up
with charachange


"L'expression de Yuuko montre que ce n'est pas une très bonne idée."


hi "Je crois que ce serait mieux qu'on rentre tôt."


hi "On doit rentrer avant le couvre-feu, après tout."

show lilly basic_smileclosed
with charachange


li "Oh, c'est vrai."

show lilly basic_smile
with charachange


li "Je te verrai demain, Yuuko."

show yuukoshang neutral_down
with charachange


yu "À demain, Lilly. Au revoir, vous deux."

stop music fadeout 9.0

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_cicadas fadein 0.5

scene bg suburb_shanghaiext_ni
with locationchange


"Nous sortons de la petite maison de thé et entrons dans les ténèbres de la nuit."

$ renpy.music.set_volume(0.4, 1.0, channel="ambient")
scene bg suburb_roadcenter_ni
with locationchange


"Lilly et Hanako se collent encore une fois, mais dans la nuit, Hanako semble légèrement moins stressée qu'à l'aller."


"Nous allons à contresens des gens sortant de l'école, mais Hanako nous emmène dans des plus petites rues, évitant la foule."

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene bg school_dormext_full_ni
with locationskip


"En dehors des dortoirs, l'école semble étrangement silencieuse en comparaison du bruit qu'il y a eu toute la journée."


hi "Bon, merci à vous deux pour aujourd'hui. J'ai appris beaucoup de choses."

show hanako emb_timid_ni at Transform(xanchor=0.5, xpos=0.59)
show lilly basic_weaksmile_ni at Transform(xanchor=0.5, xpos=0.41)
with charaenter


li "Tu es le bienvenu, mais j'ai peur que je ne doive vraiment y aller. Ce fut une longue journée."


"C'est vrai. Lilly a passé beaucoup de temps debout aujourd’hui et je peux imaginer que le trajet jusqu’à la maison de thé a dû la fatiguer."


"Je me sens un peu coupable d’être probablement le seul dans l'école à s'être levé à dix heures du matin."


hi "Bien sûr."


hi "Bon, je vous vois demain. Bonne nuit."

show lilly basic_cheerful_ni
with charachange


li "Bonne nuit, Hisao."

show hanako basic_smile_ni
with charachange


ha "B... bonne nuit."

hide hanako
hide lilly
with charaexit


"Les filles retournent à leur dortoir et moi au mien."


"En fait, maintenant que j'y pense, je suis aussi fatigué après cette journée."

stop ambient fadeout 2.0

scene black
with dissolve



label fr_H3:

window hide None

scene black
with dissolve

$ renpy.music.set_volume(0.0, 0.0, channel="ambient")
play sound sfx_alarmclock

with Pause(1.2)

play sound sfx_impact2

window show


"Mon alarme me casse les oreilles et se fait rapidement arrêter par mon poing."

scene bg school_dormhisao
with openeye


"Mon corps passe en mode automatique, sortant ma carcasse inconsciente du lit et la dirigeant vers mon uniforme."


"Comme toujours, mes flacons de médicaments attendent patiemment sur mon bureau que je les attrape et avale ma dose journalière de pilules. Dix-sept par jour."

scene bg school_scienceroom at bgright
with locationskip


"Sans m'en rendre compte, je suis déjà devant la porte de la classe 3-3. J'entre et je suis content de voir que je ne suis pas le seul à avoir du mal avec ce lendemain de festival."


"Chaque visage dans la salle de classe est sans vie. Avec le festival maintenant fini, c'est comme si les rêves de tout le monde avaient été accomplis."


"Et sans raison de vivre, les étudiants sont venus machinalement jusqu'en classe."


"Ou peut-être que je cherche trop loin."


"Je vais lentement jusqu’à ma chaise et c'est seulement maintenant que je comprends pourquoi la pièce est si calme."


"Les sièges à côté de moi sont miraculeusement vides, l’interprète pour sourds la plus bruyante du monde n'est pas encore arrivée."

play sound sfx_doorslam
play music music_running

show misha hips_grin:
    yalign 1.0 xanchor 0.0 xpos 1.0
    easein 0.3 xanchor 1.0
with vpunch


"Juste au moment où je suis sur le point de m'asseoir, la porte s'ouvre, révélant une Misha resplendissante, ses couettes en forme de perceuses se balançant de part en part, les bras dirigés vers le ciel."

show misha hips_laugh at right
with charachange


mi "Ya-hoooo~ ! C'est fini !"


"On dirait que tout le monde n'est pas affecté par la dépression post-festival."


"Le reste de la classe la regarde, pensant apparemment la même chose que moi."

show misha sign_confused
with charachange


"Misha, toujours debout à l'entrée avec ses bras en l'air, regarde nerveusement autour d'elle."


"Il est évident qu'elle ressent l'humeur maussade, mais ne sait pas vraiment quoi faire."

show misha sign_confused at center
with ease_decel


"Soudainement, elle se balance en avant."

show misha perky_sad
with charachange


mi "Hey !"

show shizu invis behind misha:
    yalign 1.0 xanchor 0.5 xpos 1.0
with None

show misha perky_sad at twoleft
show bg school_scienceroom at center
show shizu adjust_happy at tworight
with dissolvecharamove


"Alors qu'elle trébuche, elle révèle Shizune, le bras toujours tendu après avoir poussé Misha."

show shizu basic_normal
with charachange

shi "…"


hi "Merci pour le divertissement, mais vous ne devriez pas vous asseoir ?"

show shizu behind_frown
with charachange

shi "…"


"Toujours quelque peu embarrassée, Misha prend quelques secondes pour réaliser qu'elle doit traduire."

show misha sign_smile
with charachange


mi "Oh ! Ouais ! Shicchan dit qu'elle n'est pas contente que tu nous aies laissé tomber la semaine dernière."

show misha cross_frown
with charachange


mi "On était vraiment occupées !"


hi "Vraiment ? Et qu'en est-il de tout ce que j'ai déjà fait pour vous deux ?"

show shizu cross_angry
with charachange

shi "…"

show misha hips_grin
with charachange


mi "Elle dit que ça compte seulement pour les membres du conseil des étudiants. Vu que tu as refusé, elle ne te doit rien du tout."

show misha hips_grin_close
with characlose


"Misha s'approche et chuchote à mon oreille."


mi "En fait, je crois qu'elle est juste un peu déçue que tu n’aies pas passé la journée avec elle."

show misha hips_smile_close
with charachange


mi "Elle est vraiment reconnaissante pour ton travail de la semaine dernière cela dit."

show shizu behind_frustrated
with charachange


"Sentant qu'on parle d'elle, Shizune tape légèrement sur la table avec ses doigts pour que Misha se retourne."

show misha sign_smile
with charadistant

show shizu basic_angry
with charachange

show misha hips_grin
with charachange

show shizu adjust_blush
with charachange


"Je ne comprends rien de ce qu'elles se disent, mais vu l'expression légèrement embarrassée de Shizune et le rire mal contenu de Misha, je peux deviner."

stop music fadeout 8.0


"Pendant ce temps, la porte s'ouvre encore une fois, mais cette fois bien plus lentement."

show hanako invis at offscreenright
with None

show bg school_scienceroom at bgleft
show shizu basic_normal at Transform(xpos=0.42)
show misha hips_smile at Transform(xpos=0.18)
show hanako emb_downtimid at right
with dissolvecharamove


"Hanako entre silencieusement dans la pièce et referme la porte derrière elle."

show hanako emb_timid
with charachange


"Derrière ses cheveux, elle regarde rapidement la classe."


"Nos yeux se rencontrent et elle se raidit. Elle ferme les yeux, respire à fond, et marche jusqu’à mon bureau."

show hanako cover_distant
with charachange


ha "B... bonjour, Hisao."


hi "Salut Hanako. Tu es un peu en retard, non ?"

show hanako basic_normal
with charachange


ha "Je... parlais avec Lilly."

show hanako basic_worry
with charachange


ha "P-pour aujourd'hui."


hi "Ah, tu as eu sa liste ? On peut partir juste après les cours dans ce cas."

show hanako emb_smile
with charachange


ha "D-d'accord."


hi "Vivement ce soir alors."


"Hanako masque son sourire embarrassé et se précipite à sa place."

scene bg school_scienceroom at bgright
with shorttimeskip

play music music_normal fadein 3.0


"Pendant les cours, il paraît évident que ce n'est pas juste les étudiants qui ont un peu de mal après le festival."


"Mutou se contente de nous donner une liste d'exercices et va s'asseoir derrière son bureau."


"J'en oublie complètement la brève pause déjeuner pendant un moment, une telle banalité dans la journée."

play sound sfx_normalbell


"Tout le monde semble surpris de la sonnerie annonçant la fin des cours."

show shizu basic_normal at tworight
show misha perky_smile at twoleft
with charaenter


"Alors que je range mes affaires, Shizune et Misha arrivent et me tendent une embuscade."

show misha hips_grin
with charachange


mi "Dis, Hicchan, il n'est toujours pas trop tard pour nous rejoindre. Il y a beaucoup de choses à faire après le festival..."


hi "Erh, désolé Misha, j'ai... quelque chose de prévu..."

show hanako invis at offscreenright
with None

show bg school_scienceroom at center
show shizu basic_normal at Transform(xpos=0.42)
show misha hips_grin at Transform(xpos=0.18)
show hanako cover_distant at right
with dissolvecharamove


"Comme si elle avait entendu, Hanako apparaît derrière moi, tenant un petit sac et essayant d’éviter un contact visuel avec les autres."

show misha cross_laugh
with charachange


"Les yeux de Misha s’écarquillent et elle éclate de rire."


mi "BWAHAHA ! Tu vas vite, hein Hicchan~ ? On ne te gênera pas dans ton rendez-vous ! Bwahahaha !"

show shizu behind_blank
with charachange


"Derrière Misha rigolant à gorge déployée, je vois Shizune qui ne porte aucun intêret à la scène. Je me trompe peut-être, mais je crois qu'elle m'ignore délibérément."

show hanako emb_downtimid_close
with characlose


"Quelqu'un tire doucement sur ma chemise, et en me tournant je vois les yeux de Hanako rivés sur la porte."

show hanako emb_timid_close
with charachange


ha "On... on y..."


hi "D'accord. Shizune, Misha, je vous verrai plus tard."


hi "Et je ne suis toujours pas intéressé par le conseil."

show misha cross_grin
with charachange


mi "Trouble-fête."

stop music fadeout 2.0

hide misha
hide shizu
with charaexit

show bg school_scienceroom at bgleft
show hanako emb_timid_close at center
with charamove


"Misha et Shizune se retirent dans le couloir, se faisant activement des signes."


hi "Tu as tout ? On y va."

play music music_soothing fadein 4.0

scene bg school_gate
with locationskip


"Une armée d'étudiants sortent de l'école et se dirigent vers la ville."


"C'est un peu bizarre. Cela ressemble presque à la sortie des cours de n'importe quelle autre école, mais l'illusion ne prend pas à cause de la vue d'une occasionnelle chaise roulante ou d'un membre manquant."


"Je remarque que personne n'est seul."

scene bg school_road
with locationchange

show hanako emb_downsad_close at center
with charaenter


"Et, alors que Hanako et moi passons le portail, je remarque qu'elle se rapproche de moi."


"Pas suffisamment pour être considérée comme “proche”, mais elle n'est pas aussi éloignée qu'elle l'est habituellement."


"J'imagine qu'on n'est pas assez proches pour qu'elle fasse comme elle fait avec Lilly."


"Cependant, même si elle est un peu plus proche de moi physiquement, mentalement, elle a fait un grand pas en avant."


"Elle tient ses mains serrées autour des sangles en cuir de son sac, à tel point que ses phalanges deviennent blanches. Elle a la tête baissée et la bouche plissée."


"On aurait presque l'impression qu'elle va au bureau du principal pour la première fois."


"J'essaye de masquer le petit rire que j'ai en y pensant, mais je n'y arrive pas."

show hanako emb_timid_close
with charachange


ha "Q-qu'est-ce qu'il y a... ?"


"J'imagine que ça ne sert à rien de le cacher..."


hi "Désolé, pendant une seconde tu faisais une tête, comme si tu allais avoir des problèmes."

show hanako defarms_strain_close
with charachange


ha "Q-q-qu'est-ce que tu veux dire ?"


hi "Je crois que tu as besoin de te relaxer un peu. Nous n'allons pas loin et il n'y a que des étudiants ici, hein ?"

show hanako def_worry_close
with charachange


ha "O-oui."


"Ça me gêne un peu de voir Hanako avoir autant de difficultés."


hi "Et tu fais ça chaque semaine, c'est ça ?"

show hanako basic_worry_close
with charachange


ha "O-oui. Avec Lilly."


"Bien sûr. “Avec Lilly.” Je me demande si elle est déjà sortie de l'école sans elle."


"On ne le remarque pas du premier coup d'œil, mais la dépendance de Hanako envers Lilly est vraiment forte."


"Si elle ne peut même pas sortir de l'école sans elle, comment est-ce qu'elle aurait survécu si elles ne s’étaient pas rencontrées ?"


"Est-ce qu'elle aurait trouvé de l'aide auprès de quelqu'un d'autre ? Et qu'est-ce qui l'a attirée chez Lilly ?"


"C'est parce qu'elle est aveugle ? Ou parce que Lilly était juste assez gentille pour lui tendre la main ?"


"Je me demande si quelqu'un d'autre aurait pu remplir ce rôle."


hi "Dans tous les cas, je suis là. Et puis ce n'est pas loin. Ce sera fini avant que tu ne t'en rendes compte."

show hanako emb_downsmile_close
with charachange


"Les phalanges de Hanako retrouvent lentement leur couleur tandis qu'elle essaye de cacher un petit sourire."


"Nous marchons, côte à côte, le long de la pente descendante vers la ville. La foule d'étudiants se fait de plus en plus petite alors que nous avançons."


"Les étudiants les plus rapides passent devant, ceux ayant des problèmes de mobilité restent derrière, éparpillant tout le monde."

scene bg suburb_konbiniext
with locationskip


"Au moment où nous arrivons à l'épicerie, nous sommes pratiquement seuls."

scene bg suburb_konbiniint
with locationchange


"M'utilisant comme un bouclier entre elle et le vendeur, Hanako parcourt les allées, mettant divers produits dans le panier."


"Pain, lait, thé... thym ?"


"Quel genre d'épicerie vend des herbes ?"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

nvl clear

nvl show dissolve


n "\n\nEncore une fois, rien dans cette ville ne semble normal, ce qui, en y repensant, n'est peut-être pas si mal."


n "Tout est si différent et incommode, s'attarder sur tout ça n'est pas vraiment une option."


n "Quand j'y pense, ça me rappelle Hanako."


n "Peu importe à quel point on essaye, on ne peut pas éviter ses cicatrices. Elles interrompent encore mes pensées quand je les vois."


n "Même si je ne veux pas l'avouer, je crois que je me force à les ignorer."


n "Pas que je n'ai pas mes propre cicatrices. La ligne le long de mon sternum ne partira jamais complètement."


n "J'ai juste le luxe de pouvoir la cacher facilement."


n "\nMais d'une certaine façon, nos cicatrices nous rappellent qu'on est ici pour une raison."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

window show

"…"


"Hanako met un dernier objet dans son panier puis me le tend timidement, avec quelques billets."

show hanako emb_downtimid_close at center
with charaenter


ha "T-t-tu pourrais..."


"Il me faut une seconde pour comprendre ce qu'elle essaye de me dire."


hi "Oh, tu veux que je paye ?"

show hanako emb_downsad_close
with charachange


"Elle hoche la tête, mais ne me regarde pas."


"J'imagine que d'habitude la tâche incombe à Lilly."


hi "Bien sûr. Laisse-moi juste prendre quelques trucs..."


"J'attrape rapidement quelques trucs pour moi et me dirige vers le comptoir avec Hanako sur mes talons."


"Le vendeur m'adresse un hochement de tête inintéressé alors qu'il scanne mes articles."


"J'imagine que nous ignorer est la bonne façon de gérer les anomalies de Yamaku. Ils doivent avoir beaucoup d'étudiants ici, vu que c'est le magasin le plus proche de l'école."


"Le personnel doit avoir sa propre façon de gérer les étudiants. Ou peut-être pas. Peut-être que je suis le seul à réfléchir autant à ça."

stop music fadeout 2.0

scene bg suburb_konbiniext_ss
with locationchange


"Après avoir payé, Hanako et moi sortons du magasin."

scene bg school_road_ss
with locationskip

play music music_tranquil fadein 10.0


"La route est déserte maintenant. Les étudiants qui voulaient sortir sont déjà loin et personne n'est rentré encore."


"Et vu qu'il n'y a que l'école sur le chemin, il n'y a personne d'autre aux alentours."

show hanako def_worry_close_ss at center
with charaenter


"Le fait qu'il n'y ait personne se reflète sur Hanako, ses bras le long du corps, portant un sac chacun, sa tête maintenant redressée et son dos droit..."


"On dirait presque qu'elle apprécie cette marche."


hi "Donc, pourquoi tu as acheté tous ces trucs bizarres ? Un mélange d'épices ? Pourquoi tu aurais besoin de ça à l'école ?"

show hanako basic_normal_close_ss
with charachange


ha "Je... J'aime des fois... faire à m-manger."


hi "Bon, ok, moi aussi mais... des épices ?"


hi "C'est pas facile à cuisiner, tu crois pas ?"

show hanako emb_blushing_close_ss
with charachange


ha "P-pas vraiment."


hi "Bah, c'est bien. Il faudra que tu m'apprennes un jour."

show hanako emb_smile_close_ss
with charachange


ha "O-oui."


"Elle ne semble pas très certaine, mais je ne pense pas qu'il soit utile de la pousser."


"Au moins, elle semble plus contente qu'elle ne l'était à l'aller."


"Simplement ça, ça me fait plaisir."

scene bg school_dormext_full_ss
with shorttimeskip

show hanako basic_normal_close_ss at center
with charaenter


"En dehors du dortoir des filles, Hanako et moi trions nos sacs de courses."


"En comparaison, j'ai pas acheté grand-chose."


hi "Je te le dis, tu me bats à plate couture là..."

show hanako defarms_shock_close_ss
with charachange


ha "N-non, je n'ai pas... J'ai juste..."


hi "C'est une blague."

show hanako def_worry_close_ss
with charachange


hi "J'ai une pile de travail en retard de la semaine dernière, je dois y aller."


hi "Ça ira pour porter ça jusqu’à ta chambre ?"

show hanako cover_bashful_close_ss
with charachange


ha "O-ouais."


hi "Tu es sûre ? D'accord alors. À demain."

show hanako basic_smile_close_ss
with charachange


ha "S-salut."

hide hanako
with charaexit

stop music fadeout 7.0


"Nous nous séparons et je retourne à ma chambre."

scene bg school_dormhisao_ss
with locationskip


"Attendant d’être remplis, il y a une pile de papiers sur mon bureau. Avec tout ce qui est arrivé la semaine dernière, j'ai à peine eu le temps de rattraper mon retard."


"J'ai essayé de rester au niveau pendant que j’étais à l’hôpital, mais il y a certaines choses que je n'ai jamais vues, même dans mon ancienne école."


"Aucunement préparé, j'ouvre une canette et me mets au travail."

scene black
with dissolve



label fr_H4:

scene black
with None

play music music_daily fadein 6.0

scene bg school_dormhisao
with locationchange


"Les journées sont de plus en plus chaudes."


"Ce matin, je me suis réveillé couvert de sueur."


"Au moment où les étudiants commencent à quitter les dortoirs pour prendre leur petit déjeuner et s'occuper de leurs obligations matinales, le soleil est déjà haut dans le ciel, et étrangement, ça me met de bonne humeur."


"Il n'est même pas encore huit heures et pourtant j'ai le sentiment que cette journée va être une de ces journées plaisantes, tranquilles et chaudes."


"Si je n'étais pas dans une école qui considère une absence de cours comme une situation potentiellement mortelle, j'envisagerais de sécher la journée et de me relaxer dans les jardins."


"Oui, aujourd'hui va être une longue journée de paresse."


"Pendant une seconde, je m’arrête et pense à ce que m'a dit l'infirmier sur le sport. Peut-être que je devrais continuer le jogging."


"Courir avec quelqu'un comme Emi est peut-être un peu difficile, mais si je le fais à mon rythme..."


"Bah, de qui je me moque. Je n'arriverai pas à me tenir à quelque chose comme ça sans motivation."


"C'est pas comme si je restais assis toute la journée. Les trajets jusqu’à l'épicerie comptent comme un exercice, non ? Surtout le retour sur la colline..."


"Ouais, c'est pas bien grave. Comparé à des mois allongé dans un lit d’hôpital, je fais beaucoup d'exercice maintenant."

scene bg school_scienceroom
with shorttimeskip


"On dirait que je ne suis pas le seul à apprécier la journée."


"Presque tout le monde dans la classe regarde le ciel par la fenêtre."


"Même Shizune semble manquer de sérieux dans son travail."


"Misha, aussi effrontée que toujours, a même déboutonné le haut de sa chemise et s'évente avec un cahier."


"Elle a dû remarquer que je la fixais car maintenant elle me tire la langue."


"Cependant, elle ne montre aucune intention de reboutonner sa chemise ou de cacher ce qu'elle a fait."

play sound sfx_normalbell


"La sonnerie du déjeuner semble prendre tout le monde par surprise et la classe se vide bien plus lentement qu'à l'habitude."


"La chaleur semble calmer la hâte de tout le monde."

stop music fadeout 8.0


"Bon, presque tout le monde."

show hanako emb_emb
with charaenter


ha "H... Hisao ?"


hi "Salut Hanako. Qu'est-ce que je peux faire pour toi aujourd'hui ?"


"Hanako a déjà un sac avec son déjeuner à la main."


"Je n'ai pas besoin d’être un détective pour comprendre où tout cela mène."

show hanako emb_smile
with charaenter


ha "Hum... tu veux manger avec nous aujourd'hui aussi ?"

show hanako basic_bashful
with charaenter


ha "J'ai... j'ai amené suffisamment pour tout le monde..."


hi "Génial. Tu n'as pas à être aussi formelle cela dit, tu sais."

show hanako basic_normal
with charaenter


ha "Ah... oui."


hi "J'imagine qu'on va dans la salle où on boit le thé ?"

show hanako cover_worry
with charaenter


ha "O... oui."

show hanako basic_normal
with charaenter


ha "Lilly a dit qu'elle nous rejoindrait là-bas, donc on devrait... devrait..."


hi "Devrait ?"

show hanako emb_smile at center
with charaenter


ha "...devrait y aller ensemble..."


hi "Ça marche. La chaleur m'a donné plutôt faim."


"Hanako souffle de soulagement tandis que je rassemble mes affaires."

scene bg school_miyagi
with locationskip

play music music_happiness fadein 1.0


"Comme d'habitude, l'aura de la pièce est apaisante vu qu'elle est isolée du reste du monde."


"Cela dit, le vacarme habituel de l'école semble quelque peu apaisé, sûrement à cause de la paresse engendrée par la forte chaleur."


"Hanako pose lentement tout ce qu'il y a à manger sur la table, s'appliquant à chaque geste, comme si elle essayait de ne pas penser à autre chose."


"Ce n'est pas grand-chose, mais je peux dire à son comportement qu'elle a tout préparé avec beaucoup d'attention."


hi "Lilly n'est pas encore là. On commence sans elle ou pas ?"

show hanako emb_timid:
    center
    ypos 1.17
with charaenter


ha "E-elle sera bientôt là..."

show hanako emb_downtimid
with charachange


"Hanako se débat avec le couvercle de la boîte de riz."


hi "Laisse-moi t'aider..."


"Je prends la boîte des mains de Hanako et essaye de forcer le couvercle."


"J'ai beau essayer, il semble scellé."


hi "Laisse-moi deviner, tu as mis le riz dedans alors qu'il était encore chaud ?"

show hanako emb_sad
with charachange


ha "O-oui. J’étais pressée..."


"Je pose la boîte sur la table entre nous."


hi "Je le savais. Il ne voudra pas s'ouvrir. On va avoir besoin d'eau chaude pour ça."


hi "Mais ça va être difficile ici. Il y aurait de l'eau partout."


li "Bon, dans ce cas-là, si je contribuais au déjeuner ?"

show lilly invis at left
with None

show hanako emb_smile:
    tworight
    ypos 1.17
show bg school_miyagi at bgright
show lilly basic_cheerful at twoleft
with dissolvecharamove


"Lilly, souriante, est à la porte, tenant un sac dans lequel il y a divers petits pains et roulés. Je ne peux pas m’empêcher de sourire aussi."

show lilly basic_smileclosed
with charachange


li "Vu que vous avez changé vos plans à cause de moi, j'ai pensé que je devais apporter un petit quelque chose."


hi "Merci Lilly, laisse-moi te débarrasser de ça..."

show lilly basic_smileclosed at Transform(ypos=1.2)
with charamove


"Les pains de Lilly rejoignent donc les plats sans riz de Hanako. Je me dépêche de faire du thé pour compléter tout ça."


hi "Bon, ça donne faim."

show hanako emb_downtimid
with charachange


"Alors que je prends une bouchée, je remarque que Hanako essaye de ne pas montrer qu'elle me regarde."


"Ce n'est rien de spécial, mais je ne peux pas me plaindre, je suis assez paresseux quand il s'agit de cuisiner."


hi "J'imagine que ça a été fait avec ce que tu as acheté hier ?"

show hanako emb_blushtimid
with charachange


ha "O-oui."


"Les yeux de Hanako se rivent sur moi, attendant un avis."


hi "Eh ben, ça valait le coup. Merci, Hanako."

show hanako cover_bashful
with charachange


ha "Je... je voulais te montrer... après hier..."


hi "T’embête pas. J’étais juste un peu surpris de ce que tu as acheté."

show lilly basic_weaksmile
with charachange


li "Hanako a toujours aimé expérimenter des choses en cuisine. C'est bon... la plupart... du temps."


"Bien que le sourire de Lilly ne s'en aille pas, le léger changement dans son ton me dit que les choses ne se sont pas toujours aussi bien passées."


"Et ce n'est pas comme si Hanako avait beaucoup d'amis pour tester ses préparations..."

stop music fadeout 7.0


"Attends... Lilly attendait que je commence ? Elle n'a pas mangé avant que je dise que c'était bon..."


"Son petit sourire me dit que c'était une action délibérée. Il faudra que je trouve un moyen de lui rendre la pareille."


hi "Bah, c'est bon, c'est tout ce qui compte, non ?"

show hanako basic_smile
with charachange


ha "O-oui."

show lilly basic_smileclosed
with charachange


"Lilly, satisfaite de ne pas être la première à tester la création de Hanako, commence à manger ce qui est devant elle."


"Je me retrouve à la regarder toucher le plat avec les baguettes, touchant et traçant délicatement les contours pour s'assurer de l'emplacement de la nourriture avant de la prendre avec dextérité."


"On pourrait croire que c'est un enfant qui joue avec sa nourriture, mais elle le fait avec une telle précision et attention qu'il est évident que c'est juste comme ça qu'elle mange."


"Voulant profiter du repas, je commence à manger aussi."

show hanako emb_downsmile
with charachange


"Hanako a une approche différente. Elle attend que Lilly et moi nous soyons servis pour prendre rapidement sa part."

show hanako emb_smile

with shorttimeskip

play music music_dreamy fadein 4.0


"En peu de temps les boîtes se retrouvent vides, sauf celle du riz, toujours fermée."

show lilly basic_smile
with charachange


li "Merci Hanako, je suis repue."

show hanako basic_smile
with charachange


ha "N-non... merci pour le pain..."


hi "Oui, ça aurait été un désastre sinon."

show lilly basic_planned
with charachange


li "De rien."

show lilly basic_weaksmile
with charachange


li "Mais maintenant, je dois repartir. Il est bien trop facile d’être en retard en mangeant ici."


hi "Ouais, je vois ce que tu veux dire. Je crois qu'on va juste débarrasser ici et y aller."

show lilly basic_smileclosed at twoleft
with dissolvecharamove


li "Sur ce, bon après-midi."

hide lilly
with charaexit

show hanako basic_smile:
    center
    ypos 1.17
show bg school_miyagi at center
with charamove


"Lilly part, sa canne tapotant le sol tandis qu'elle avance dans le couloir silencieux."


"Hanako et moi remballons tout et restons assis, attendant la sonnerie."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene bg misc_sky at Fullpan(20.0)
with locationchange


"Ensemble, nous regardons le ciel azur par la fenêtre."

play sound sfx_warningbell


"S'il n'y avait pas eu la sonnerie, j'aurais pu jurer que le temps s'était arrêté."


"L'envie de sécher les cours de l’après-midi me prend."


"Je regarde Hanako qui, elle non plus, ne montre aucune envie de bouger."


ha "Non... encore un peu..."

$ renpy.music.set_volume(1.0, 3.0, channel="music")

scene bg school_miyagi
show hanako basic_smile:
    center
    ypos 1.17
with shorttimeskipsilent


"L’intervalle entre la sonnerie préventive et celle de fin de la pause déjeuner passe en un clin d’œil."


hi "On devrait vraiment y aller... les gens vont commencer à s’inquiéter et à nous chercher, si on sèche..."

show hanako basic_distant
with charachange


"Hanako soupire."

show hanako basic_normal
with charachange


ha "Tu as raison."

show hanako basic_normal at center
with charamove


"Lentement, elle se lève et je fais de même."

scene bg school_staircase2
with locationskip


"Silencieusement, nous montons les escaliers jusqu'au troisième étage et allons jusqu’à notre classe."

scene bg school_hallway3
with locationchange

play sound sfx_dooropen


"Une fois devant la porte, je me mets devant Hanako et ouvre la porte, baissant la tête en excuse d'avance."

scene bg school_scienceroom at center
with locationchange

stop music fadeout 5.0


hi "Excusez-nous pour le retard."

play sound sfx_doorclose


"Je ne suis pas accueilli par une réprimande, ou même par une instruction énervée de rejoindre mon siège, mais simplement par le silence d'une quinzaine d'étudiants essayant de ne pas rire."


"Mutou, toujours en retard, n'est pas encore arrivé. Cependant, le fait que Hanako et moi sommes arrivés ensemble est évident."

show misha hips_grin at center
with charaenter

mi "Pff… pffwa…"


"Quatorze étudiants essayent de ne pas rire et une finit par céder."

play music music_comedy

show misha cross_laugh
with charachange


mi "Pft-bwahahaha ! Les amoureux sont de retour~ !"

show misha hips_laugh
with charachange


mi "WAHAHAHA~ !"


hi "Ouais, merci. Tu peux te calmer maintenant."

hide misha
show hanako invis_close:
    center
    xpos 1.0
with charaexit

show bg school_scienceroom at bgleft
show hanako emb_downsad_close:
    xpos 0.8
with dissolvecharamove


"Je passe la porte et réalise que Hanako est collée contre mon dos, se cachant de toute la classe."

show hanako invis_close:
    xpos 0.7
with dissolvecharamove


"Alors que je m'approche de mon bureau, elle se sépare de moi et se précipite au sien. Ses efforts pour bloquer tout le monde dans son esprit se voient clairement sur son visage."

scene bg school_scienceroom at bgright
with charamove


"Regardant rapidement la porte pour vérifier que le professeur n'arrive pas, je vais jusqu'au bureau de Hanako et lui chuchote à l'oreille."


hi "Ne t’inquiète pas pour Misha, elle est toujours comme ça. J'ai apprécié ce midi. Ne t’en fais pas, d'accord ?"


"Hanako hoche la tête à l’intérieur de ses bras, mais ne montre pas son visage."

play sound sfx_dooropen

show muto invis at tworight
with None

show muto normal at center
show bg school_scienceroom at center
with dissolvecharamove


"J'aimerais rester et la consoler un peu plus, mais Mutou choisit ce moment exact pour entrer dans la classe, en train de parler, comme s'il avait commencé dans le couloir."

show muto smile at center
with charaenter


mu "...qui, bien sûr, est directement proportionnel à la charge mais inversement proportionnel au carré de la distance..."

hide muto
with charaexit

play sound sfx_doorclose


"Il est tellement dans son discours qu'il ne remarque même pas que je me faufile à ma place."


"Pendant que Mutou continue sa lecture, Misha se penche vers moi."

show misha invis at offscreenleft
with None

show misha perky_smile_close:
    xanchor 0.5 xpos 0.16
with dissolvecharamove


mi "Le professeur n'a peut-être pas remarqué que tu étais en retard, mais moi oui."


"C'est assez évident, vu le spectacle auquel on a assisté."

show misha hips_grin_close
with charachange


mi "J'ai eu comme instruction de te laisser tranquille pour aujourd'hui, mais à une seule condition."


hi "Oh ? Laquelle ?"

show misha sign_smile_close
with charachange


mi "Tu dois nous aider cet après-midi~ !"


"J'étire mon cou pour voir au-dessus de l'épaule de Misha."


"Shizune s'arrange pour ne pas croiser mon regard."


hi "D'accord. Juste pour aujourd'hui."


hi "Je t'ai déjà dit que je ne rejoindrais pas le conseil, tu t'en souviens ?"

show misha hips_grin_close
with charachange


mi "Bien sûr ! Te forcer serait considéré... euh, considéré..."

show misha perky_confused_close
with charachange


"Elle regarde sur son cahier, là où est écrit de toute évidence le script qu'elle doit jouer."

show misha hips_grin_close
with charachange


mi "...sous la contrainte et donc contre la réglementation."


hi "C'est très étrange de ta part de penser à la réglementation maintenant."

show misha sign_smile_close
with charachange


mi "Les choses doivent être faites selon les règles !"

show misha perky_smile_close
with charachange


mi "C'est juste que les règles n'ont pas été écrites pour toutes les situations, donc il y a des fois où on peut les ignorer."


hi "Et vous vous demandez encore pourquoi personne d'autre ne veut être dans le Conseil des Étudiants..."

stop music fadeout 3.0

show misha hips_frown_close
with charachange

with Pause(0.3)

show misha invis at offscreenleft
with dissolvecharamove

hide misha
with None


"Après avoir tiré la langue, Misha retourne à son cahier et nous attendons la fin de la dernière demi-journée d'école."

with shorttimeskip

play sound sfx_normalbell

show shizu invis_close at offscreenright
show misha invis_close at offscreenleft
with None

show misha hips_smile_close at twoleft
show shizu behind_blank_close at tworight
with Dissolvemove(0.5, time_warp=_ease_in_time_warp)


"Avant même que je ne puisse me lever, Misha et Shizune placent chacune une main sur mes épaules."


hi "Hé, j'ai dit que je vous aiderais, roh..."

play music music_shizune fadein 1.0

show misha hips_grin_close
with charachange


mi "C'est juste pour s'en assurer, Hisao, s'en assurer~ !"

show hanako invis behind shizu at offscreenright
with None

show misha hips_smile_close at Transform(xpos=0.17)
show shizu behind_blank_close at Transform(xpos=0.5)
show bg school_scienceroom at bgleft
show hanako emb_timid:
    xanchor 0.5 xpos 0.9
with dissolvecharamove


ha "H-Hisao ?"


"Hanako essaye timidement de passer en tournant autour de nous et je réalise qu'elle peut être ma seule chance de m’échapper."


hi "Oh salut Hanako. Quoi de neuf ?"

show shizu basic_angry_close
with charachange

shi "…"

show misha hips_frown_close
with charachange


mi "Hé, qu'est-ce qui te fait croire que tu as le temps de discuter ?"


hi "Oh détends-toi, ça ne prendra pas longtemps... désolée Hanako, tu disais ?"

show hanako emb_downtimid
with charachange


ha "Je... J'allais aller à la bibliothèque, et... et je me disais..."


"Les doigts de Hanako se contorsionnent et ses yeux regardent partout dans la pièce, sauf vers nous."

show misha sign_smile_close
with charachange


mi "Désolé Hanako, mais Hisao doit venir avec nous. Il a du travail à faire."

show shizu behind_smile_close
with charachange

shi "…"

show misha hips_grin_close
with charachange


mi "Oh ! Mais tu peux aider si tu veux."

show hanako cover_worry
with charachange


ha "Euh..."

label fr_choiceH4:
menu:
    with menueffect
    mi "Alors, Hisao ?"
    "Qu'est-ce que t'en penses, Hanako ?":




        return m1
    "J'ai suffisamment travaillé pour le conseil.":


        return m2


label fr_H5_1:


scene bg school_scienceroom at bgleft
show hanako cover_worry:
    xanchor 0.5 xpos 0.9
show shizu behind_smile_close at Transform(xanchor=0.5, xpos=0.5)
show misha hips_grin_close at Transform(xanchor=0.5, xpos=0.17)
with None


hi "Qu'est-ce que tu en dis, Hanako ? Si on s'y met tous, ça ne prendra pas longtemps."

show hanako emb_timid
with charachange


"La façon dont gigote Hanako répond à ma question avant même qu'elle n'ouvre la bouche."

show hanako emb_downtimid
with charachange


ha "Je... Je dois vraiment y aller..."


"Bon, il fallait s'y attendre. On dirait que ce sera juste les filles du conseil et moi."


"C'est plus facile de me résigner à un autre après-midi de travail dans la petite salle."


hi "Je te rejoindrai plus tard, ok ?"

show hanako emb_smile
with charachange


ha "D-D'accord."

stop music fadeout 3.0

show misha hips_grin_close at twoleft
show shizu behind_smile_close at tworight
show hanako invis at offscreenright
show bg school_scienceroom at center
with dissolvecharamove

show misha hips_smile_close at twoleft
hide hanako
with charachange


mi "Voilà ! Maintenant que les au revoir sont finis, c'est l'heure de travailler !"

scene bg school_hallway3
with locationchange


"Misha et Shizune m'escortent jusqu’à la salle du conseil des étudiants, ne me lâchant pas les épaules une seule seconde."


"Je me sens un peu mal de laisser tomber Hanako comme ça, mais si c'est le prix à payer pour que Misha la laisse tranquille, alors qu'il en soit ainsi."

scene bg school_council
with locationchange


hi "Et donc, qu'est-ce qu'on doit faire aujourd'hui ?"

show misha sign_smile at center
with charaenter

play music music_ease fadein 8.0


mi "Un compte rendu !"


hi "Hein ? C'est pas un truc supposé arriver après quelque chose ?"

show misha hips_grin
with charachange


mi "Ouaip ! On doit collecter toutes les informations du festival pour que Shicchan puisse débriefer les professeurs."

show misha hips_grin at twoleft
show bg school_council at bgleft
with charamove

show shizu adjust_happy at tworight
with charaenter


"Shizune laisse tomber une grande pile de feuilles sur le bureau et sourit succinctement."

show misha hips_smile
with charachange


mi "On doit la trier en deux piles."

show misha sign_smile
with charachange


mi "Une pour les trucs financiers, comme les factures, et une pour les retours, une pour les positifs, peut-être une pour les trucs qui pourront être un problème pour l'année prochaine, une pour les problèmes qui ne seront sûrement pas réglés..."


hi "Ça fait plus que deux piles..."

show misha perky_confused
with charachange


mi "Hein ? Ah, ouais. Ouais je croyais que ça serait seulement en deux piles. Désolée."


hi "D'accord. Et pendant que je ferai ça, qu'est-ce que vous ferez ?"

show misha hips_grin
show shizu adjust_smug
with charachange


mi "Ben on a loupé le déjeuner parce qu'on a collecté tous ces rapports, alors on va aller chercher à manger !"


"Pourquoi est-ce que vous ne les avez pas triés quand vous les avez collectés aussi..."


"Heureusement mon mécanisme de prévention m'a empêché d'ouvrir la bouche, ce qui aurait empiré la situation."

show misha perky_confused
with charachange


mi "Hein ?!"

show misha perky_sad
with charachange


mi "C'est pas juste !"

show shizu behind_blank
with charachange

shi "…"


"J’étais tellement en train de me plaindre de la quantité de travail que je n'avais pas remarqué que Shizune continuait de faire des signes."


"S'il n'y avait pas eu les cris de Misha, je n'aurais probablement rien remarqué du tout."

show shizu adjust_smug
with charachange

show shizu basic_normal
with charachange

show shizu behind_blank
with charachange


"Shizune semble assigner des tâches à Misha, mais aucune d'entre elles n'a l'air plaisante."

show misha sign_sad
with charachange

show misha perky_sad
with charachange

show misha perky_sad at Transform(ypos=1.15)
with charamove


"Arrivant à une conclusion, Misha répond brièvement à Shizune et s'assoit sur le siège à côté de moi."

show shizu adjust_happy
with charachange

hide shizu
with charaexit

show misha perky_sad at Transform(xpos=0.5)
show bg school_council at center
with charamove


"Shizune nous dit quelque chose avant de sortir."


hi "Vous parliez de quoi ?"

show misha perky_confused
with charachange


mi "Shicchan était inquiète que tu fasses mal les choses si tu n’étais pas supervisé."

show misha perky_sad
with charachange


mi "Et vu qu'elle ne peut pas te dire ce que tu loupes, elle me fait rester. Awww... c'est nul, je voulais aller avec Shicchan !"

show misha cross_smile
with charachange


mi "Mais elle va revenir avec à manger~ !"

show misha cross_grin
with charachange


mi "C'est bien ça !"


"La vitesse avec laquelle Misha change d'humeur est extraordinaire. Du tréfonds de la terre au sommet du monde en un battement de cil."


"C'est difficile d'imaginer comment quelqu'un peut fonctionner comme ça."


hi "Bah, ça aurait pu être pire."


hi "Bon, qu'est-ce qu'on est censés faire ?"

show misha sign_smile
with charachange


mi "Trier."


hi "J'ai compris ça."

show misha hips_smile
with charachange


mi "Bon, commençons à faire des piles. On verra après comment les organiser."


hi "D'accord..."

show misha perky_smile
with charachange


"On commence à trier tous les papiers dans des piles incroyablement complexes."


"Au début c'est juste par simples catégories, financier, retours, rapports d'incidents..."


"Puis ils se divisent en bons et mauvais rapports, et de plus en plus, jusqu’à ce qu'on n'ait plus l'air de jeter des papiers au hasard sur la table."


hi "C'est sans espoir."

show misha perky_confused
with charachange


mi "Hein ? Pourquoi ? On fait ce qu'on nous a demandé, non ?"


hi "Oui, mais on a plus l'air de faire n'importe quoi."

show misha hips_grin
with charachange


mi "Non, je crois qu'on avance bien. Shicchan sera capable de s'en sortir à partir de là."

show misha cross_grin
with charachange


mi "Donc je crois qu'on peut s’arrêter là."


"C'est presque comme si le bon sens de Misha était sorti de la pièce avec Shizune."


"Cela dit, aucun intérêt d'en discuter."

show misha sign_smile
with charachange


mi "À propos..."

show misha cross_smile
with charachange


mi "C'est quoi l'histoire avec Hanako et toi ?"


hi "Quelle histoire ?"

show misha hips_smile
with charachange


mi "Tu étais avec elle aujourd'hui, hein~ ?"

show misha hips_grin
with charachange


mi "Il s'est passé quelque chose ? Un potin intéressant que tu me caches~ ?"


hi "Si je te parlais de moi, ce ne serait plus un potin, tu ne crois pas ?"

show misha perky_confused
with charachange


mi "J'imagine..."


hi "On est juste des bons amis."


hi "Pourquoi ça t’intéresse ? Je croyais que Shizune et toi ne l'aimiez pas..."

show misha cross_frown
with charachange


mi "C'est pas vraiment ça. Tu sais que Shicchan et Lilly ne s'entendent pas trop."


mi "Et vu que Hanako est toujours avec Lilly, on ne lui parle pas trop."

show misha sign_smile
with charachange


mi "Mais ça ne veut pas dire que je ne m’inquiète pas pour elle."


hi "Qu'est-ce qui t'inquiète ?"

show misha perky_sad
with charachange


mi "Eh bien, elle ne parle avec personne d'autre, non ? C'est pas bon Hicchan !"


"Si Shizune et Lilly ne s'apprécient pas parce que “leurs personnalités sont différentes” alors je ne veux pas savoir comment Misha et Hanako s'entendraient..."

show misha perky_confused
with charachange


mi "Je veux dire, d'une façon ou d'une autre, on est tous dans le même bateau ici, non~ ?"


hi "D'une certaine façon, oui."

show misha sign_smile
with charachange


mi "La dernière fois, quand elle est sortie de classe au milieu d'un cours, Shicchan a demandé au professeur ce qui serait fait à ce sujet."

show misha sign_confused
with charachange


mi "Il a dit que chaque étudiant avait des besoins spéciaux et que Shicchan n'avait pas besoin de s’inquiéter pour ça."

show misha perky_confused
with charachange


mi "Hanako ne fait jamais de travail de groupe, elle s'enfuit juste."


mi "Ce n'est pas suffisant pour s’inquiéter ?"


hi "C'est pas faux. Elle parle toujours très peu quand on discute à deux."

show misha perky_sad
with charachange


mi "C'est déjà bien mieux que tout ce que j'ai pu faire. Shicchan et moi avons toutes les deux essayé quand elle est arrivée, mais elle a eu peur et s'est enfuie."


"Je pourrais dire à Misha qu'il m'est arrivé exactement la même chose, mais elle semble réfléchir intensément."


"Écouter Misha sans l'influence de Shizune est... intéressant."

show misha cross_frown
with charachange


mi "Je crois qu'elle a besoin de réaliser que les gens se moquent de ce dont elle a l'air et qu'elle peut nous faire confiance."

show misha cross_smile
with charachange


mi "Si elle le pouvait, je me sentirais mieux pour elle."


"Je crois que je n'ai jamais vu Misha aussi longtemps sans qu'elle fasse de signes."


"Quand elle est avec Shizune, elle est constamment en train de bouger les mains, lui traduisant tout ce qui se passe."


"Un tel niveau effort doit être épuisant, même pour un esprit agile."


"Et il faut se rendre à l'évidence, Misha n'est pas la personne la plus brillante que je connaisse."


hi "Je vais garder un œil sur elle pour toi."


hi "Mais tu devrais probablement t'excuser pour tout à l'heure. Je ne crois pas que Hanako apprécie ce genre de blagues."

show misha perky_confused
with charachange


mi "Oh ? Oh~ !"

show misha perky_sad
with charachange


mi "Je n'avais même pas remarqué. Désolée."


hi "C'est pas à moi qu'il faut le dire, juste parle-lui-en."

show misha perky_smile
with charachange


mi "D'accord. Je le ferai dès demain matin."


hi "Bien."

play sound sfx_doorslam
with vpunch


"Une cacophonie en provenance de la porte annonce le retour de Shizune."


"J'imagine qu'elle ne peut pas vraiment savoir le bruit qu'elle fait."

show misha hips_grin
with charachange


mi "Oh, Shicchan ! Tu es de retour !"

show shizu invis at Transform(xanchor=0.5, xpos=1.0)
with None

show misha hips_grin at Transform(xpos=0.3)
show shizu behind_blank at tworight
show bg school_council at bgleft
with dissolvecharamove


"Shizune apparaît, les bras chargés de sacs de la supérette."

show shizu basic_normal2
with charachange

shi "…"

show misha sign_smile
with charachange


mi "Nous avons des restes du festival. Vu qu'on s'occupe des affaires du festival, je me suis permise de faire une petite folie."

show misha hips_grin
with charachange


mi "Bonne idée Shicchan, dix points."


hi "On a le droit de faire ça ?"

show shizu cross_angry
with charachange

shi "…"

show misha cross_frown
with charachange


mi "Pour quelqu'un qui refuse de nous rejoindre, tu sembles te poser beaucoup de questions sur la politique du conseil."

show misha cross_grin
show shizu adjust_smug at tworight
with charachange


mi "Je dois punir ton insolence en rationnant ta portion du festin."


hi "D'accord, d'accord, j'ai compris."

show misha perky_smile
show shizu adjust_happy at Transform(ypos=1.15)
with dissolvecharamove


"Misha pousse les piles de papiers d'un côté pour faire de la place à l'avalanche de nourriture que Shizune déverse."


"Alors que je vois l'étendue de mon dur travail se faire effacer d'un mouvement de main, même s'il n'était pas bien utile, je réalise pourquoi ces deux-là ont besoin d'aide ici."


"Le repas de l'épicerie n'est pas exquis, mais au moins c'est nourrissant."

show shizu behind_smile
with charachange

shi "…"

show misha sign_smile
with charachange


mi "Merci de nous aider aujourd'hui. La plupart du temps, nous faisons juste des rapports pour le personnel."

show misha perky_smile
with charachange


mi "Cette année on peut au moins faire des bonnes rubriques pour le compte rendu."


hi "Es-tu sûre que ce n'est pas une organisation corrompue ?"

show misha hips_grin
with charachange


mi "Pas du tout, pas du tout. On suit les règles. Ce n'est pas notre faute si les règles ne sont pas suffisamment spécifiques."


hi "Je croyais que c'était la définition de corruption..."

show misha hips_smile
with charachange


mi "Tu réfléchis trop~ !"


hi "Tu sais quoi ? Tu as probablement raison."


hi "Dans tous les cas, je dois y aller..."


hi "...si j'y suis autorisé, du moins."

show shizu adjust_smug
with charachange

shi "…"

show misha hips_grin
with charachange


mi "Ton travail a été jugé suffisant. Tu peux partir."


hi "D'accord, merci."


hi "Tu sais, si tu appuyais sur le côté “repas gratuit” plutôt que sur le côté “travail infini”, tu pourrais probablement recruter plus de gens."

stop music fadeout 6.0

show misha sign_smile
with charachange

show shizu behind_blank
with charachange


mi "Tu as peut-être raison."


hi "Réfléchis-y."


hi "Et pense aussi à ce dont on a parlé... tu n'as pas besoin de le dire à Shizune si tu ne veux pas."

show misha perky_confused
with charachange


mi "Quoi ? Oh, d'accord. J'essayerai de la voir demain."

show misha perky_smile
with charachange


mi "B'nuit, Hicchan."


hi "Bonne nuit, Misha, Shizune."

scene black
with dissolve


label fr_H5_2:

scene bg school_scienceroom at bgleft
show hanako cover_worry:
    xanchor 0.5 xpos 0.9
show shizu behind_smile_close at Transform(xanchor=0.5, xpos=0.5)
show misha hips_grin_close at Transform(xanchor=0.5, xpos=0.17)
with None


hi "Hé, Shizune, je sais que j'ai dit que je vous aiderais, mais j'ai déjà des choses de prévues. D'ailleurs, j'ai déjà fait ma part la semaine dernière, non ?"


hi "Je te promets de me rattraper une prochaine fois."

show misha sign_confused_close
with charachange

show shizu basic_frown_close
with charachange

show misha perky_smile_close
with charachange

show shizu behind_blank_close
with charachange


"Shizune et Misha me libèrent de leurs griffes et ont une longue conversation silencieuse."

show misha sign_smile_close
with charachange


mi "Bon, tu as raison sur ce point. Pour être honnête, on comptait juste dépenser le reste du budget en gâteaux."

show misha cross_laugh_close
with charachange


mi "Donc, si tu n'es pas là, ça nous arrange, plus de gâteaux pour nous. Wahahaha~ !"

stop music fadeout 6.0

show shizu invis at offscreenleft
with dissolvecharamove

show misha invis at offscreenleft
with dissolvecharamove

hide shizu
hide misha
with None


"Shizune fait volte-face et marche jusqu’à la porte, Misha la suivant juste après."


hi "Eh bien, c'était beaucoup plus facile que je l'aurais cru. La semaine dernière elles ressemblaient à des molosses. Ou des gardiens de prison."


hi "Ou peut-être des gardiens de prisons élevés par des molosses..."


"Je n'arrive pas à croire que j'ai pensé cela et encore moins que je l'ai dit à voix haute. Je crois que j'ai besoin de prendre mes distances avec Kenji."


hi "...Peu importe. Bref, on va à la bibliothèque ?"

show hanako basic_smile
with charachange


ha "O-oui."

play ambient sfx_crowd_indoors fadein 0.5

scene bg school_hallway3
show crowd
with locationchange


"Hanako me suit dans les couloirs bondés jusqu’à la bibliothèque, m'utilisant comme bouclier."

stop ambient fadeout 0.5
play music music_happiness fadein 2.0

scene bg school_library
show hanako invis at offscreenright
show yuuko neutral_down at center
with locationchange

show hanako basic_worry at tworight
with dissolvecharamove


"Une fois les portes passées, Hanako se rue au comptoir où Yuuko trie des livres."

show hanako emb_emb
with charachange


"Avant que je ne puisse arriver, Hanako lui a chuchoté quelque chose."

show yuuko neurotic_up
with charachange


yu "Hum, tu trouveras ça dans la section documentaire, mais je ne sais pas où exactement. Si tu veux, je peux chercher..."

show hanako emb_downsad
with charachange


ha "P-pas la peine."


hi "Salut Yuuko, vous parlez de quoi ?"

show yuuko neutral_down
with charachange


yu "Oh, Hisao... Hanako cherchait un livre sur..."

show hanako emb_blushing
with charachange


ha "R-rien..."


hi "Un livre sur rien ? Dans la section documentaire ?"

show hanako def_strain
with charachange


ha "Je... J'étais juste..."

show yuuko neurotic_up
with charachange


"Je regarde Yuuko. Elle a l'air d’être sur le point d'exploser sous la pression qu'elle a de garder secrète la requête de Hanako."


hi "Yuuko, qu'est-ce que..."

show yuuko happy_down
with charachange


yu "Échecs ! Elle cherche un livre sur les échecs !"


"Je note dans un coin de ma tête de ne jamais faire confiance à Yuuko pour des informations importantes."

show hanako defarms_shock
with charachange

ha "Y-Yuuko…"

show yuuko panic_up
with charachange


yu "Je suis désolée Hanako... ça m'a échappé..."


hi "Bon, ce n'est plus un secret maintenant. Allez, laisse-moi te donner un coup de main, je devrais m'améliorer aussi."

show hanako def_worry
with charachange


ha "D... d'accord."

hide yuuko
with charaexit

show hanako def_worry at center
show bg school_library at bgleft
with charamove


"Yuuko disparaît derrière le comptoir, honteuse, tandis que Hanako s'engouffre dans les profondeurs de la section documentaire."


"Je sais qu'il est supposé y avoir un système pour indexer ces livres, mais je ne vois pas comment quelqu'un peut le comprendre sans passer la moitié de sa vie dans une bibliothèque."


"C'est sûrement pour ça que tous les bibliothécaires que je connais sont névrosés."



"Au fond de l'aile, entre un livre sur les tours de magie avec des cartes et un livre sur les jeux d'enfants, se tient un livre portant le titre “Tactiques aux échecs pour les champions”."

show hanako basic_bashful
with charachange


"Avant que je ne puisse l'atteindre, Hanako a le livre dans les mains, le tenant contre sa poitrine."


hi "Bon, j'imagine qu'il est à toi alors. Je pourrai te l'emprunter quand tu auras fini ?"

show hanako cover_worry
with charachange


ha "O-oui. Je... Je n'avais juste jamais joué contre une autre personne que L-Lilly avant, alors j'ai pensé..."


"Zut. Ce n'est pas comme si j’essayais de battre Hanako délibérément ou quoi que ce soit, mais elle semble l'avoir pris à cœur."


"Au moins, ça veut dire qu'elle veut rejouer avec moi. C'est plutôt bien, non ?"


hi "Bah, c'est pas comme si j'étais un pro ou autre, j'y ai juste un peu joué avant..."


"Ça me rappelle que je n'ai pas parlé de mon problème à Hanako. Je m’arrête une seconde, décidant de me couvrir. Ce sera une conversation pour un autre jour."


hi "...avant que je vienne ici."

stop music fadeout 6.0

show hanako cover_distant
with charachange




ha "Ça... ça va ?"


hi "Ouais, je me rappelais juste un truc..."


"Quand j'y pense, je ne devrais pas être effrayé de parler à Hanako de mon handicap et de ma période à l’hôpital. Vu ses cicatrices, elle a probablement passé un bon moment dans un lit d’hôpital, elle aussi."


"Mais pour je ne sais quelle raison, je n'arrive pas à lui en parler. Du moins pas aujourd'hui. Et pas aussi soudainement."


"Pressé de changer de sujet, j'attrape un livre au hasard sur l’étagère."





"C'est un livre sur les roller coasters les plus rapides du monde."


"...publié en 1982. Bon, pas vraiment à jour, mais ça devrait être intéressant."


hi "Bon, on a tous les deux un livre, on va s'asseoir ?"

show hanako cover_bashful
with charachange


"Hanako ne résiste pas au changement de sujet et nous nous dirigeons dans le coin lecture de la bibliothèque."

hide hanako
with charaexit


"Aucun de nous ne dit un mot, nous ouvrons simplement nos livres et commençons à lire."


"J'essaye de lire le mien, mais il semble que les roller coasters de 1982 n'étaient pas aussi grands que ceux construits ces dernières années."


"La plupart de ceux cités sont faits en bois. Ça ne me semble pas vraiment prudent."


"Si je dois monter dans quelque chose de potentiellement dangereux, je veux qu'il soit fait de métal, ou un autre mot impressionnant comme “Titanium” ou “Ruthenium”."


"Je perds rapidement mon intérêt pour le livre et mes yeux se baladent dans la pièce pour finir par s’arrêter sur Hanako."

show ev hana_library_read_std:
    truecenter zoom 1.0 subpixel True
    easein 20.0 zoom 1.05
with locationskip


"Hanako semble être absorbée par son livre, parcourant les pages dans tous les sens, comme pour confirmer ce qu'elle vient de lire."


"Je me demande si c'est vraiment efficace ou si elle se sature juste."


"Elle enlève inconsciemment les cheveux devant son visage, dévoilant ses cicatrices."


"Je ne suis pas sûr de ce que je dois faire. Je peux lui demander pour ses cicatrices ? Ou son passé ? Combien de temps elle est restée à l’hôpital ? Elle doit toujours voir un médecin ?"


"Ça semble être le genre de questions que tu poserais à quelqu'un qui vient d’être transféré dans l'école."


"Mais, jusqu’à aujourd'hui, personne ne me les a posées. Bon, sauf Rin, mais je ne crois pas que ce soit une référence."


"Pour l'instant, je ne vais rien dire. Si quelqu'un veut que je sache quelque chose, il me le dira. Essayer de forcer le sujet pourrait renfermer Hanako sur elle-même."

scene bg school_library_ss
show yuuko worried_up_ss at center
with shorttimeskip


yu "Hum... désolée de vous interrompre, mais je dois fermer la bibliothèque."

play music music_tranquil fadein 3.0


hi "Déjà ?"


"Je regarde ma montre. D'une manière ou d'une autre, perdu dans mes pensées, presque deux heures se sont écoulées."

show yuuko smile_down_ss
with charachange


yu "Vous voulez emprunter ces livres ? Je peux le faire..."

show hanako invis:
    xpos 0.9 xanchor 0.5 ypos 1.17 yanchor 1.0
with None

show hanako basic_worry_ss:
    xpos 0.7
show bg school_library_ss at bgleft
show yuuko smile_down_ss at twoleft
with dissolvecharamove


ha "O-oui s'il te plaît."


hi "J'ai fini, je rangerai celui-là en sortant. C'était pas intéressant de toute façon."

show hanako emb_timid_ss at tworight
with dissolvecharamove


"Hanako marque sa page d'un papier et se lève. Les filles vont au comptoir et je range mon livre là où il se trouvait."

show yuuko neurotic_up_ss
with charachange


"Yuuko scanne le livre de Hanako en tâtonnant un peu."

show yuuko neutral_down_ss
with charachange


yu "Ah... voilà. La troisième fois est la bonne. Vu que c'est un documentaire, tu peux l'avoir pour une semaine."

show hanako basic_smile_ss
with charachange


ha "Ç-ça ira."

scene bg school_hallway2
with locationchange


"Yuuko éteint l'ordinateur de la bibliothèque et nous accompagne jusqu’à la porte."

show yuuko panic_up at twoleft
show hanako def_worry at tworight
with charaenter


yu "Arh ! Je ne savais pas qu'il était si tard... !"


hi "Mais tu nous as dit que tu devais fermer..."

show yuuko worried_up
with charachange


yu "Oui, je sais mais c’était avant que je regarde l'heure !"

show yuuko neurotic_up
with charachange


yu "Je vous verrai plus tard."

hide yuuko
with easeoutleft


"Yuuko part comme une flèche dans le couloir, tenant son sac à main derrière elle comme un étendard."

show hanako def_worry at center
show bg school_hallway2 at bgleft
with dissolvecharamove


hi "Tous les bibliothécaires sont vraiment névrosés."

show hanako emb_timid
with charachange


ha "Hein ?"


hi "Ah, t’embête pas. Je pensais juste que je n'ai jamais rencontré un bibliothécaire qui sache organiser son temps, même s'ils y arrivent avec les livres."

show hanako basic_smile
with charachange


ha "Oh... Je v-vois ce que tu veux dire..."


"Hanako sourit, amusée. Ce n'était pas censé être une blague, mais j'ai dû lui rappeler un autre bibliothécaire... ou un truc du genre..."

show hanako cover_worry
with charachange


ha "Je... je devrais rentrer."


hi "Ouais, moi aussi. Je n'avais pas remarqué qu'il était si tard. Merci de m'avoir laissé traîner avec toi."

show hanako basic_bashful
with charachange


ha "P-pas de problème."


hi "Je vais à ma chambre aussi de toute façon, ça t’embête si je fais le chemin avec toi ?"

show hanako emb_blushing
with charachange


ha "N-non, non."

hide hanako
with charaexit


"Hanako part avant moi et j'ai besoin de trottiner un peu pour la rattraper."

scene bg school_dormext_full_ss
with locationchange

show hanako def_worry_ss at center
with charaenter


"Nous traversons les jardins, arrivant finalement devant les dortoirs."


hi "Woaw, tu marches plutôt vite. J'étais dans un club de football avant et tu as réussi à me semer."

stop music fadeout 6.0

show hanako emb_downsmile_ss at center
with charaenter


"Je regrette d'avoir dit ça. Ce n'est pas tellement qu'elle va vite, mais plutôt que ma condition m'a rendu beaucoup plus faible qu'avant."


"La réaction de Hanako est étrange. Je m'attendais à ce qu'elle ralentisse un peu, mais elle se contente de rougir et de regarder ses pieds en souriant."


"Un silence se dresse entre nous. Ça arrive souvent avec Hanako, mais c'est légèrement différent cette fois. Après quelques secondes, je romps le silence."


hi "On y est. Je te vois en classe demain ?"

show hanako emb_smile_ss
with charachange


ha "O-oui."

hide hanako
with charaexit


"Hanako me fait un petit signe d'au revoir avant de s’aventurer dans les dortoirs. Je reste là et la regarde partir, avant de partir dans la direction de ma propre chambre."

scene black
with dissolve



label fr_H6:

scene bg school_dormhisao
with locationchange


"Des oiseaux qui chantent."


"En temps normal, ce serait un bon moment pour penser à la beauté de la nature."


"Mais il est six heures du matin."

play sound sfx_pillow

scene black
with Dissolve(0.2)


"Me couvrant la tête avec l'oreiller, je m'écrase le visage sur le matelas, espérant que l'impact me rendormira."

"Futile."


"Je remue, me tourne, mais le sommeil ne revient simplement pas."

play music music_daily fadein 10.0

scene bg school_dormhisao
with locationchange


"D'accord nature, tu as gagné. Tu vois ? Je me lève maintenant..."


"Le manque de sommeil me brouille l'esprit et il n'y a qu'un seul remède pour ça. Un bon petit déjeuner."

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 0.5

scene bg school_cafeteria
with locationchange


"Ce serait bien d’être le premier ici."


"Être le premier à se servir dans un plat chaud, m'asseoir où je veux..."


"Ça aurait été bien."


"Mais même mon réveil exceptionnellement tôt me place derrière les étudiants les plus assidus."


"J'imagine qu'il y a des gens qui aiment se lever tôt ici, pour une raison ou une autre."


"Un groupe d'étudiants en tenue de sport sont concentrés autour d'une table, discutant joyeusement de tactique de jeu tout en ingérant ce qui est devant eux."


"Dispersés dans la salle, il y a d'autres étudiants qui sont encore à moitié endormis, souffrant sûrement du même fléau que moi - les oiseaux bruyants."


"Et, bien sûr, il y a les gens qui aiment simplement se lever tôt, ceux qui ont leurs sacs remplis de cahiers et de devoirs faits."


"C'est difficile de ne pas déprécier les gens comme ça, encore plus quand tu es fatigué."


"Trouvant un visage familier, je me dirige vers celui-ci."


"Lilly est assise seule, sentant délicatement le contour d'une assiette d’œufs avec sa fourchette."


"Je m'en veux presque d'interrompre ses mouvements réglés comme une horloge."


"Je me demande si quelqu'un d'aveugle peut être dans la lune comme ça. Elle bouge d'une manière prédéfinie apprise au fil des années, juste comme quelqu'un de normal mangerait tout en lisant le journal."


hi "Bonjour, Lilly. Je ne m'attendais pas à te voir si tôt."

show lilly basic_surprised:
    center
    ypos 1.2
with charaenter


li "Oh, Hisao, tu m'as surprise. Je ne savais pas que tu prenais ton petit déjeuner de si bonne heure."


hi "C'est une exception. Je préfère largement être en retard en cours qu'en avance au petit déjeuner."

show lilly basic_weaksmile
with charachange


"Lilly pousse un petit soupir tandis que je commence à manger."


"Elle retourne vite à son activité précédente, qui semble toujours aussi peu prenante."


"Chacun de ses mouvements manque d'énergie. J'imagine que c'est pareil que de regarder dans le vide en faisant une action banale."


"Mais après quelques bouchées, Lilly pose sa fourchette et presse une serviette sur ses lèvres."

stop music fadeout 6.0
stop ambient fadeout 6.0

show lilly basic_concerned
with charachange


li "Hisao, ça te gêne si je te pose une question ?"


"Zut, tout ce que je voulais c'était manger, et quelques heures de sommeil. Personne ne dit “je peux te poser une question” pour une simple question."


hi "Non, vas-y."

show lilly basic_listen
with charachange


li "Tu estimes Hanako comme une amie ?"


"Hu, ça semble être une question piège."


hi "Je... j'imagine, oui. Pourquoi ?"

show lilly basic_weaksmile
with charachange


li "Juste comme ça."

show lilly basic_displeased
with charachange

play music music_serene fadein 8.0


li "J'ai une autre question cela dit. Qu'est-ce qui fait que tu l'estimes comme une amie ?"


"Cette question est vraiment bizarre. Qu'est-ce qu'elle attend de moi ?"


hi "Je ne sais pas vraiment. Je crois que c'est parce qu'elle est un peu différente dans sa façon de traiter les gens..."

show lilly basic_reminisce
with charachange


li "Mmh. Depuis que je la connais, elle n'a jamais vraiment lié de liens avec d'autres personnes que moi."

show lilly basic_concerned
with charachange


li "Elle ne semble pas s’intéresser aux autres et je crois que les gens sont un peu effrayés par son apparence."


hi "Vraiment ? Je croyais que ce genre de choses n'arrivaient pas ici. La discrimination et tout ça."

show lilly basic_listen
with charachange


li "Mmh, si je devais reformuler ça..."


"Elle fronce les sourcils, quelque chose qui m’inquiète légèrement."

show lilly basic_weaksmile
with charachange


li "Je dirais que tu es un peu naïf."


"Naïf ? Je serais insulté si elle n'avait pas cette petit grimace cynique sur le visage."


hi "Je... vois."

show lilly basic_reminisce
with charachange


li "Bien que Yamaku ait un sens de la communauté plus fort que les autres écoles, elle est loin d’être sans conflits."

show lilly basic_displeased
with charachange


li "Les règles ne peuvent pas changer la nature humaine après tout, juste la refouler."


"C'est quelque chose que j'avais déjà remarqué."


"Juste des petites choses, comme certaines personnes ou groupes qui s'évitent dans les couloirs. C'est pas bien différent de mon ancienne école."


"Lilly et Shizune aussi peuvent être considérées comme rivales, même si elles sont toutes les deux tout à fait respectables."


"Du moins, c'est comme ça que Misha traduit ce qu'exprime Shizune. Qui sait ce qui se passe vraiment derrière ses signes et ses lunettes."


hi "J'imagine que tu as raison. La première fois que je suis venu ici, tout était vraiment perturbant."


hi "Je faisais tout le temps des erreurs, ou du moins je croyais en faire. Comme la première fois que je t'ai rencontrée, et que je t’ai dit “Je vois”."


hi "Je ne savais pas si c'était considéré comme malpoli ou autre, donc j'ai essayé d'éviter ça, traiter les gens différemment et tout ça."


hi "Je me suis dit que Hanako et toi étiez tout à fait normales et j'ai essayé d'ignorer l’évidence."


hi "J'ai parlé à Hanako comme si elle était une personne quelconque et on est devenus amis."


hi "Du moins, c'est comme ça que je le vois."


hi "Mais tu sais, je me sens mal rien que de dire quelque chose comme ça à voix haute. C'est comme si ça me demandait un effort pour penser à Hanako ou même à toi, en tant que personnes normales. Je ne crois pas que ce soit bien."

show lilly basic_smileclosed
with charachange


li "Hisao, je crois que tu es naïf, mais que tu es aussi quelqu'un de bien. C'est peut-être ta meilleure qualité."


hi "Je... vais... prendre ça comme un compliment..."

show lilly basic_smile
with charachange


li "Dis-moi, tu es libre ce soir ?"


hi "Si tu ne comptes pas les devoirs, alors je suis libre comme l'air."

show lilly basic_cheerful
with charachange


li "Dans ce cas, ça t’intéresserait de nous rejoindre pour le thé ?"


hi "Erh, je n'ai pas beaucoup d'argent en ce moment, alors sortir n'est pas vraiment..."

show lilly basic_smile
with charachange


li "Oh, je ne parlais pas de sortir, juste ici, ce soir."


hi "On peut accéder aux classes le soir ici ?"

show lilly basic_giggle
with charachange


li "Non, c'est pas ce que je voulais dire. Hanako et moi utilisons souvent ma chambre pour boire du thé ensemble. Passe-donc ce soir."


hi "D'accord, pas de problème. Tu es dans quelle chambre ?"

show lilly basic_smileclosed
with charachange


li "225, la chambre 25 du deuxième étage."


hi "Ok, compris."

show lilly basic_weaksmile
with charachange


li "Bon, je dois y aller. J'ai mes devoirs de déléguée à remplir après tout."

show lilly basic_cheerful at center
with dissolvecharamove


li "À ce soir, Hisao."


hi "Ouais, à plus tard."

hide lilly
with charaexit

stop music fadeout 8.0


"Attends... je viens d’être invité dans la chambre d'une fille après les cours. C'est autorisé ça ?"


"Il y a un couvre-feu ici, mais je n'ai jamais entendu une règle pour les visiteurs dans les chambres."


"Mais c'est quand même suffisant pour que mon cerveau privé de sommeil se réactive."


"Et rajoutant un petit déjeuner à ça, je suis bien réveillé."

scene bg school_scienceroom
with locationskip


"Je vais en classe à contrecœur, toujours un peu excité à l'idée d'enfreindre les règles."


"Je me sens comme un enfant prévoyant de sortir par la fenêtre la nuit."


"Bon, peut-être que j’exagère un peu, mais quand tu compares une invitation à une fête à six heures de cours, je sais lequel gagne."


"Misha et Shizune font peu pour me délivrer de mon ennui. Pour une fois, elles semblent déterminées à faire les exercices donnés par Mutou."

scene bg school_scienceroom_ss
with shorttimeskip

play sound sfx_normalbell


"Et finalement, la journée arrive à sa fin."

scene bg school_dormhisao_ss
with locationskip


"Je me dépêche de retourner à ma chambre pour me laver et me coiffer. Heureusement, je ne croise pas Kenji."

scene bg school_dormext_full_ss
with locationchange


"Peu après, je quitte le dortoir des garçons."



label fr_H7:

scene bg school_girlsdormhall
with locationskip

play sound sfx_doorknock2


"Je frappe nerveusement à la porte de la chambre 225, vérifiant ma montre une fois de plus."


li "C'est toi, Hisao ? La porte est ouverte, tu peux entrer."


"La voix de Lilly se fait entendre à travers la porte et apaise ma nervosité."


"C'est la première fois que je suis invité dans la chambre d'une fille la nuit."


"Même si je sais qu'il n'y a pas de but caché à cette invitation, ça ne m’empêche pas d'imaginer toutes les possibilités."


"Un garçon. Deux filles. Dans une chambre de dortoir. Avec un service à thé."


"Dit comme ça, ça sonne un peu bizarre."


"Soufflant un peu pour me calmer, je pose avec précaution ma main sur la poignée et ouvre la porte."

play sound sfx_dooropen

window hide

scene white
with dissolve

with Pause(0.1)

play music music_one fadein 10.0

scene ev lilly_bedroom:
    truecenter
    zoom 1.1 subpixel True
    ease 15.0 zoom 1.0
with Dissolve(4.0)

window show


"La porte s'ouvre complètement et j'ai mon premier aperçu de la chambre de Lilly."


"Ses meubles semblent presque anciens, mais les murs ne sont pas décorés du tout. Au centre de la pièce, il y a une table basse où se trouve un petit service à thé."


"Tout dans la pièce semble à sa place, sauf peut-être les quelques piles de livres collés contre les murs."


"Mon sens de la vue n'est pas le seul à être stimulé. Une légère odeur peut être sentie. Vernis à ongle, parfum, maquillage... c'est difficile de décrire cette odeur autrement que “féminine”."


"Je finis de balayer la pièce du regard avant de me concentrer sur les filles."

scene ev lilly_bedroom_large:
    xpos -130 ypos -400 subpixel True
    acdc_warp 4.0 ypos -600
with flash


"Lilly est assise à la table basse, portant un pyjama bleu foncé avec un short qui montre ses séduisantes jambes pâles."

show ev lilly_bedroom_large:
    ease 1.0 ypos -300 xpos -830
    acdc_warp 12.0 ypos 0 xpos -830
with None


"En face d'elle, Hanako est assise, portant une robe de chambre classique rose clair."


"Ses mains sont entre ses jambes, ses épaules en avant et sa tête baissée, comme si elle essayait de se cacher dans sa robe."


"Ce serait sûrement facile pour elle, sa robe de chambre est sûrement deux tailles trop grande pour elle."


"Le bout des manches pend un peu, lui donnant l'air d’être une enfant ayant mis les habits de ses parents."


"Elle redresse la tête pour confirmer que c'est bien moi et sourit vaguement d'un air gêné, avant de rebaisser très vite la tête."

show ev lilly_bedroom_large:
    ease 1.0 xpos -130 ypos -400
with None


li "Ne reste pas debout dans le couloir, Hisao, entre donc."

scene bg school_dormlilly
show lilly basic_smile_paj:
    twoleft
    ypos 1.2
show hanagown distant:
    tworight
    ypos 1.17
with locationchange

play sound sfx_doorclose
stop music fadeout 10.0


"Je fais un pas dans la chambre, fermant la porte derrière moi."

show lilly basic_weaksmile_paj
with charachange


li "Eh bien, eh bien. J'ai bien peur que ce soit une petite chambre pour trois personnes. Viens, assieds-toi."


"Je marche lentement jusqu’à la table et m'assieds, essayant de ne rien cogner en chemin."


"Je ne peux pas m'empêcher de jeter un regard rapide au haut de Lilly."


"Me faire prendre à ce moment-là serait terrible."

show lilly basic_smileclosed_paj
with charachange


li "Bon, buvons ce thé. Hanako, tu peux verser ?"

show hanagown normal_blush
with charachange


ha "B... bien sûr. Hi... sao... tu..."

show hanagown distant_blush
with charachange


ha "...tu veux..."

show hanagown worry_blush
with charachange


ha "...tu veux du..."


hi "Avec plaisir. Tu as besoin d'aide ?"

show hanagown normal_blush
with charachange


ha "N... non, ça va..."

show hanagown smile
with charachange


ha "Merci..."

play music music_dreamy fadein 2.0

show lilly basic_giggle_paj
with charachange


"Lilly n'arrive pas à s’empêcher de sourire face à la nervosité de Hanako, et je ne peux pas lui en vouloir."

show hanagown distant
with charachange


hi "Longue journée ?"

show hanagown smile
with charachange


ha "O... ouais."

show lilly basic_smileclosed_paj
with charachange


"Je me relaxe, assis entre elles deux."


"À ma gauche se trouve Lilly vêtue de bleu et à ma droite Hanako en rose."

show teaset:
    xalign 0.5 yanchor 0.5 ypos 0.6 alpha 1.0
    easein 0.5 ypos 0.5
with charaenter


"Le service à thé sur la table est mignon, peint en rouge avec des motifs floraux."


"Ça fait bizarre en contraste avec les meubles sophistiqués de Lilly, ce qui me fait penser que c'est Hanako qui l'a choisi."


"Il y a un léger “schting” quand Hanako cogne accidentellement la théière sur la tasse où elle verse le thé."

show hanagown worry
show lilly basic_displeased_paj
with None

show teaset:
    easeout 0.5 alpha 0.0 ypos 0.6
with Pause(0.5)

hide teaset
with None


"Elle respire rapidement, elle doit être vraiment nerveuse, même si ce n'est pas le genre de choses dont quelqu'un d'autre se soucierait."

show hanagown worry_blush
with charachange


"Hanako en tremble même."

show lilly basic_weaksmile_paj
with charachange


li "C'est pas grave, Hanako. Pas besoin d’être nerveuse."

show hanagown normal
with charachange


"Hanako semble se calmer grâce aux mots de Lilly et verse le thé dans les deux autres tasses."

show hanagown normal_blush
with charachange


ha "Voilà, Hisao... Lilly."


"Hanako pose avec attention une coupelle et une tasse en face de Lilly et de moi. C'est agréable de se faire servir comme ça."

show lilly basic_smile_paj
with charachange


li "Merci Hanako."


hi "Ouais, merci."

show hanagown smile
with charachange


ha "D-de rien."

show lilly basic_smileclosed_paj
with charachange


"Lilly cherche sa tasse, et après l'avoir trouvée, en boit une petit gorgée."


"Je fais la même chose. Le thé est quelque peu meilleur que celui qu'on boit d'habitude à l'école."


hi "C'est bon, c'est très différent de tous les thés que j'ai bus jusqu’à aujourd'hui..."

show lilly basic_ara_paj
show hanagown normal_blush
with charachange


li "On dirait que tu as choisi le bon, Hanako."

show lilly basic_smileclosed_paj
with charachange


li "Tu as bien fait, même si c'était osé."

show hanagown smile
with charachange


"Le sourire de Hanako revient, encore plus grand qu'avant."


"Même avec son visage à moitié couvert de cicatrices, son sourire timide est vraiment très mignon."

show hanagown distant_blush
with charachange


ha "Je suis contente que tu l'aimes..."


"Hanako, se relaxant enfin, commence à boire sa tasse."


label fr_H7a:

$ renpy.music.set_volume(0.5, 1.0, channel="music")
window hide
nvl clear
nvl show dissolve


n "Je repense à ma discussion avec Misha l'autre jour."


n "Est-ce que je dois m’inquiéter du comportement de Hanako, ou est-ce qu'elle est juste timide ?"


n "Et puis il y a eu Lilly plus tôt ce matin."


n "L’inquiétude qu'elles ont toutes les deux semble justifiée, et elles connaissent la situation mieux que moi."


n "Mais, vraiment, comment est-ce que je peux aider ?"


n "Je ne suis pas chirurgien plastique, donc je ne peux rien faire pour son apparence, et je ne suis pas un psychologue pour l'aider à être plus sociable."


n "Alors qu'est-ce qu'elles attendent de moi ?"


n "C'est frustrant. Hanako et moi sommes rapidement devenus amis et à cause de ça, c'est comme si tout le monde voulait que je résolve ses problèmes."


n "Et je n'ai aucune idée de comment faire ça."


n "Personne ne peut guérir mon cœur, ni les yeux de Lilly, ni personne d'autre ici dans cette école."


n "Cependant, je ne vois pas de mal à devenir plus proche de Hanako. Maintenant qu'elle est plus à l'aise avec moi, j'apprécie de passer du temps avec elle."

$ renpy.music.set_volume(1.0, 1.0, channel="music")
nvl clear
nvl hide dissolve
window show



label fr_H7b:


$ renpy.music.set_volume(0.5, 1.0, channel="music")
window hide
nvl clear
nvl show dissolve


n "\n\n\n\nÇa me fait penser à ce qu'a dit Lilly au petit déjeuner."


n "Pourquoi je suis ami avec Hanako ?"


n "Lilly semble vraiment préoccupée par le bien-être de Hanako, mais ce n'est pas comme si je pouvais faire quoi que ce soit pour l'aider."


n "Pour autant que je sache, ses cicatrices ne la limitent pas physiquement, et tous ceux que j'ai rencontrés ont réussi à surmonter leur handicap dans une certaine mesure."


n "Je n'ai pas de motivation cachée pour être avec Hanako, on a juste des intérêts communs."


n "\nCe n'est pas suffisant ?"

$ renpy.music.set_volume(1.0, 1.0, channel="music")
nvl clear
nvl hide dissolve
window show




label fr_H7c:

show lilly basic_smile_paj
with charachange


li "Donc, Hisao, tu apprécies ?"


"Les mots de Lilly me font descendre de mon nuage et il me faut une seconde pour me rappeler où je suis."


"Je suis dans une pièce avec deux filles dans leurs vêtements de nuit. C'est quelque chose qui s’apprécie."


hi "Ouais, c'est relaxant. Presque comme si je n'étais plus à l'école. Vous faites ça souvent ?"

show lilly basic_weaksmile_paj
with charachange


li "Assez souvent, mais pas aussi souvent que nous prenons le thé dans l'école."


"Vu qu'elles le font presque tous les jours, ça ne m'étonne pas."


"Alors que j'avance la tasse pour boire une autre gorgée, je la trouve tristement vide."


hi "C'était délicieux. Merci Hanako, et toi aussi Lilly."

show hanagown smile
with charachange


ha "De rien."

show lilly basic_smile_paj
with charachange


li "Oui, je t'en prie, Hisao. Ça fait plaisir d'avoir une troisième personne ici."


hi "Si vous avez besoin de quelqu'un pour remplir ce rôle, je suis toujours disponible. Toujours."


"Il faut que je m'assure qu'elles comprennent le message."

stop music fadeout 8.0
show lilly basic_sleepy_paj
with charachange


"Lilly laisse échapper un bâillement, qu'elle cache tardivement avec sa main."

show lilly basic_weaksmile_paj
with charachange


li "Excusez-moi, je crois que je suis un peu fatiguée."

show hanagown distant
with charachange


ha "Je crois qu'on est tous un peu fatigués..."

show lilly basic_ara_paj
with charachange


li "Eh bien, eh bien, on ne tient pas longtemps ce soir, Hanako."

show lilly basic_weaksmile_paj
with charachange


li "On devrait vraiment aller dormir, on a tous classe demain."


hi "Ouais... Je vais y aller."

show lilly basic_smile_paj
with charachange


li "Merci d’être venu, Hisao."

show hanagown normal
with charachange


ha "M... merci. Tu reviendras ?"


hi "Une armée toute entière ne pourrait pas m'en empêcher."

show lilly basic_cheerful_paj
with charachange


li "Je suis impressionnée par ta détermination, Hisao."


hi "Dans tous les cas, tu as raison. On ferait mieux d'y aller."


"Je me lève et me dirige vers la porte."

show hanagown normal at tworight
with dissolvecharamove


"Hanako se tient timidement derrière moi."


"Je m’arrête et la regarde."


hi "Tu viens avec moi ?"

play music music_comedy fadein 0.5

show hanagown normal_blush
with charachange


"Hanako rougit instantanément."

show hanagown distant_blush
with charachange


ha "Non... Je... pas... cette chambre... n'est pas..."


hi "Hanako, c'était une blague."

show hanagown smile
with charachange


ha "Oh... d'accord... bonne nuit..."

show lilly basic_smileclosed_paj
with charachange


li "Bonne nuit, Hanako. Bonne nuit, Hisao."


hi "Bonne nuit à vous deux."


"Et sur ce, notre petite fête s’achève."

scene bg school_girlsdormhall
with locationchange


"Je ne suis toujours pas sûr de ce que Lilly veut que je fasse pour Hanako, mais je ne vais pas la laisser tomber."


"J’attends que la porte se ferme derrière nous avant de me tourner vers Hanako."

show hanagown distant_blush
with charaenter


hi "Hé, Hanako, tu n'as pas à être nerveuse avec moi tu sais."


hi "Je veux dire, on est amis, non ?"

show hanagown normal_blush
with charachange


ha "O-oui. On est... amis."


hi "Si tu veux qu'on fasse des trucs ensemble ou autre, dis-le moi. Je te dois toujours une revanche aux échecs, tu te rappelles ?"

show hanagown distant
with charachange


ha "D-d'accord..."

show hanagown normal
with charaenter


ha "M-mais ne crois pas que tu vas gagner..."


hi "Ça ne serait pas drôle si c'était facile."

show hanagown smile
with charachange


"Hanako sourit à ma remarque."


ha "B-bonne nuit Hisao..."

show hanagown invis at tworight
with Dissolvemove(0.5, time_warp=_ease_out_time_warp)

hide hanako
with None

stop music fadeout 5.0


"Sur ce, Hanako retourne rapidement dans sa chambre, située à côté de celle de Lilly."


"Je commence à retourner à mon dortoir, mais le simple fait de marcher semble drainer mon énergie."

scene bg school_dormhisao
with locationskip


"J'arrive à peine à ma chambre avant d’être frappé par une vague de fatigue."

play sound sfx_switch

scene bg school_dormhisao_ni
with Dissolve(0.2)


"J’enlève mes chaussures, tombe sur mon lit et m'endors au moment même où ma tête touche l'oreiller."

scene black
with dissolve


label fr_H8:

scene bg school_dormhallway
with locationchange


"J'ouvre la porte de ma chambre, prêt pour une autre journée de cours."

show kenji invis at twoleft
with None

show kenji neutral_close at center
with Dissolvemove(0.5, time_warp=_ease_in_time_warp)


ke "Bien dormi ?"

play music music_kenji fadein 0.5


"L'arrivée soudaine de Kenji me fait sursauter et j'évite de justesse de me cogner la tête contre lui."


"Je sais qu'il voit mal, mais il sait qui je suis maintenant. Il a vraiment besoin de se tenir aussi proche ?"

show kenji neutral
with charadistant


hi "Ouais. Comme un bébé."

show kenji tsun
with charachange


ke "Rah, pourquoi les gens disent ça ? Tu as déjà vu un bébé dormir ?"


ke "Ils pleurent. Toute la nuit. Toutes les nuits. Les bébés ne dorment pas très bien."


"Et ainsi s'en alla ma bonne humeur. Je dois me rappeler de parler clairement avec Kenji."


hi "D'accord, j'ai compris. C'était une façon de parler."

show kenji neutral
with charachange


ke "Ouais, ok, peu importe. Tu étais où la nuit dernière ? J'avais une faveur à te demander mais tu n'étais pas là."


"Pendant une seconde j'envisage de dire la vérité à Kenji, que j'étais avec Hanako et Lilly."


"Heureusement, cette seconde passe très vite."


hi "J'étais sorti. Voir les environs et tout. Tu sais, en reconnaissance."

show kenji happy
with charachange


ke "C'est bien mec, c'est bien. Je savais que tu étais du genre à prévoir les choses à l'avance..."


hi "Bref, tu voulais me demander quoi ?"

show kenji neutral
with charachange


ke "J'allais commander à emporter et j'avais besoin de monnaie."


hi "Quoi ? Je t’ai donné de l'argent la semaine dernière et tu ne m'as toujours pas remboursé !"

show kenji tsun
with charachange


ke "Tss, et je commençais à croire que tu étais cool."


"Kenji fouille dans sa poche et en sort son portefeuille."


"Alors qu'il compte les 400 yen qu'il me doit, je peux clairement voir qu'il a au moins deux billets de 10000 yen."


hi "Mais... Pourquoi tu m'empruntes de l'argent alors que tu en as autant ?"


"Kenji soupire, réalisant qu'il s'est fait prendre."


ke "Lâche-moi, mec. Ça porte malheur de casser un billet pour quelque chose qui vaut moins de la moitié de sa valeur."


ke "Le dîner d'hier soir va me coûter sept ans de malheur. Sept ans !"

show kenji happy
with charachange


ke "Tu ne crois pas que c'est suffisant pour aider quelqu'un ? J'aurais une peine plus courte si je volais le truc en question."


"Mon bon sens me crie de lui dire quelque chose, mais heureusement, je me retiens."


"Discuter d'une chose comme ça avec Kenji compliquerait juste les choses."


hi "Ouais, tu as sûrement raison. Peut-être que tu devrais mieux prévoir les choses ?"

show kenji neutral
with charachange


ke "Ouais mec, je sais. Mais j'ai tant de choses à faire, c'est difficile. Et tu n'es jamais là, alors je dois me débrouiller."


ke "On est supposés être frères d'armes, tu te rappelles ?"


hi "Ouais, ouais, je sais. Conspiration globale et tout. Je reste sur mes gardes."

show kenji neutral_close
with charachange


"Kenji s'approche suffisamment pour que je puisse sentir son haleine empestant l'ail."

show kenji tsun_close
with charachange


ke "Tu ferais mieux, mec. Tu passes déjà moins de temps ici. C'est ce qu'elles font en premier."


ke "Elles essayent de nous séparer. Diviser pour mieux régner. Sun Tzu a dit ça."


hi "Compris. Maintenant, je dois y aller. J'ai classe. Tu viens ?"

show kenji neutral_close
with charachange


ke "Nan, je suis fatigué. Je suis resté debout toute la nuit pour m’assurer que rien n'allait arriver après avoir cassé le billet."


hi "Toujours aussi rationnel, à ce que je vois."

show kenji tsun_close
with charachange


ke "Peu importe. Bonne nuit."

stop music fadeout 3.0

show kenji invis at twoleft
with Dissolvemove(0.5, time_warp=_ease_out_time_warp)


"Kenji retourne dans sa chambre, et je l'entends verrouiller sa porte."



label fr_H9:

scene bg school_dormhallway
with None

scene bg school_scienceroom
show muto smile at center
with shorttimeskip

play music music_daily fadein 4.0


mu "...et c'est pour ça que certaines personnes ne peuvent pas rouler leur langue ou que d'autres ont leur second doigt de pied plus grand que le premier."


"Mutou nous adresse un grand sourire, apparemment fier de son explication sur les gênes récessifs."


"Cependant, peu importe à quel point il peut être impressionné par la science qui nous définit, la classe semble endormie."


"Pourquoi est-ce qu'une mauvaise explication peut rendre la plus intéressante des choses sans intérêt ?"

show muto irritated
with charachange


"Je peux voir Mutou se ratatiner alors qu'il voit que rien de ce qu'il a dit la dernière demi-heure n'a été retenu."

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 4.0


"Des chuchotements commencent à apparaître dans la classe, et comme une avalanche, le bruit ambiant augmente."

show muto normal
with charachange


"Vaincu, Mutou trouve quelques exercices sur le livre et se lève pour nettoyer le tableau."

hide muto
with charaexit


"Comme j'aurais pu m'y attendre, Hanako remballe ses affaires et part dès que les gens commencent à parler et rire entre eux."


"La surprise de voir quelqu'un s'en aller si facilement commence à s'effacer, mais ça ne m’empêche pas de m'interroger sur un truc."


"Est-ce qu'elle part parce qu'elle ne veut pas que les gens lui parlent ? Ou juste parce que les gens discutant autour d'elle la perturbent ?"

play sound sfx_normalbell
$ renpy.music.set_volume(1.0, 4.0, channel="ambient")


"Avant que je ne puisse penser davantage, la sonnerie m’interrompt. Je me demande si elle ne profitait pas juste de l'opportunité pour partir plus tôt."


"Les étudiants discutent pendant qu'ils rangent leurs livres et sortent leurs repas, et tandis que Misha est distraite, j'attrape mon déjeuner et sors."

stop ambient fadeout 1.0

scene bg school_miyagi
show lilly basic_smileclosed:
    center
    ypos 1.2
with locationskip


"Lilly est déjà là, préparant son déjeuner seule."


hi "Hanako n'est pas encore là ?"

show lilly basic_smile
with charachange


li "Oh, Hisao, comment vas-tu ? J'ai bien peur de n'avoir pas vu Hanako depuis ce matin."


"C'est vrai, Hanako et Lilly vivent à côté l'une de l'autre."


"Étrangement, je crois que leurs conversations matinales sont plus logiques que les divagations de Kenji."


hi "C'est étrange. Elle est sortie de classe plus tôt, donc je pensais qu'elle serait là."

show lilly basic_displeased
with charachange


li "Donc elle sort encore plus tôt de classe..."


hi "Hein ? Ouais. Je l'ai vue faire ça quelques fois."

show lilly basic_sad
with charachange

stop music fadeout 7.0


"Lilly baisse un peu la tête, visiblement déprimée. On dirait quelqu'un qui est habitué à entendre des mauvaises nouvelles."


li "Je croyais qu'elle arrêterait de faire ça maintenant que vous êtes devenus amis."

show lilly basic_weaksmile
with charachange


li "Chacun son rythme, j'imagine."


hi "D'ailleurs, pourquoi elle sort plus tôt ?"

show lilly basic_reminisce
with charachange


li "Je n'en suis pas exactement sûre moi-même. Je pense que c'est parce qu'elle ne veut pas se retrouver dans une situation où elle doit répondre à quelqu'un."


"Je me rappelle ma première rencontre avec elle, je trouvais qu'elle ressemblait à un animal acculé. Peut-être que je n'étais pas loin de la vérité."


hi "Et elle semble bien s'entendre avec toi, et avec moi... un peu..."

show lilly basic_displeased
with charachange


li "C'est un peu plus compliqué que ça. J'imagine que la première chose que les gens lui demandent, c'est comment elle a eu ses cicatrices."


li "Elle en parle rarement avec moi, mais je sais qu'elle n'aime pas se rappeler ce qu'il s'est passé."

show lilly basic_reminisce
with charachange


li "Elle fuit la classe et les conversations pour se préserver de ce genre de choses, si tu veux."


hi "Oh... donc alors, pourquoi est-ce qu'elle me parle ?"

show lilly basic_weaksmile
with charachange


li "Tu l'as dit toi-même hier au petit déjeuner. Tu essayes d'ignorer ses cicatrices. Une fois qu'elle a vu que tu n'allais pas lui demander, elle s'est ouverte à toi."


hi "Mh, tu as sûrement raison. Peut-être. Je sais pas. Tu la connais mieux que moi, alors je vais te faire confiance là-dessus."

play music music_normal fadein 3.0

show lilly basic_giggle
with charachange


li "Je ne m’inquiéterais pas pour ça si j'étais toi. Je suis sûre que tu la connaîtras aussi bien que moi en peu de temps."

show lilly basic_smileclosed
with charachange


li "Je suis contente qu'elle ait un nouvel ami et vous avez tant de centres d'intérêt en commun..."


hi "Bah, lire n'est pas vraiment ce que j'appellerais un sport d'équipe. C'est agréable d'avoir de la compagnie, cela dit."

show lilly basic_smile
with charachange


li "C'est là où je veux en venir. Hanako est comme les autres, dans son cœur. Elle aussi veut de la compagnie dans des moments comme ça."


hi "Oh, je vois. Je crois. Pour être honnête, vous me rendez un peu confus."

show lilly basic_smileclosed
with charachange


li "C'est normal, Hisao. On se connaît depuis peu de temps, on ne peut pas attendre de toi que tu nous comprennes, tout comme on ne peut pas te comprendre."

show lilly basic_weaksmile
with charachange


li "Mais c'est aussi ça qui est drôle quand on se fait des amis, hein ?"


hi "Oui, oui c'est vrai."

show lilly basic_giggle
with charachange


li "Aussi... Je pense que c'est aussi parce qu'on est du sexe opposé. Les hommes et les femmes ont souvent du mal à se comprendre."


"Elle dit ça avec un petit rire, trouvant amusants tous ces petits détails de la vie."

show lilly basic_cheerful
with charachange


li "J’espère que tu ne m'en tiendras pas rigueur, mais je vais commencer à manger."


hi "Non, vas-y, je crois que je vais manger quelque chose aussi. J'ai aussi quelques livres à déposer à la bibliothèque avant la reprise des cours, alors je ferais mieux de me dépêcher."

show lilly basic_smileclosed
with charachange


li "Tu y trouveras sûrement Hanako. Si tu la vois, tu peux lui dire de venir dans ma chambre ce soir ? J'aimerais lui parler."


hi "Tu ne viens pas ?"

show lilly basic_weaksmile
with charachange


li "Malheureusement, j'ai une réunion de délégués tout à l'heure, alors je partirai dès que j'aurai fini de manger."


hi "D'accord, si je ne la vois pas à la bibliothèque, je lui dirai en classe. Je suis sûr qu'elle reviendra après le déjeuner."


"Nous nous taisons dès que nous commençons à manger, et je prends une seconde pour réfléchir à ce que l'on vient de dire."


"J'ai toujours pensé que la timidité de Hanako était simplement due à un complexe à cause de ses cicatrices."


"Mais c'est une façon très superficielle de la voir."


"Juste au moment où je pensais être capable de voir à travers le brouillard qui entoure Lilly et Hanako, je réalise que je suis encore plus paumé qu'au début."



"Lilly finit rapidement son repas, ne voulant pas arriver en retard à sa réunion. Je ne peux pas lui en vouloir."


"Shizune sera sûrement là, et je doute qu'elle veuille lui faire le plaisir d'avoir quelque chose d'autre à se faire reprocher."

show lilly basic_smile
with charachange


li "Je dois y aller. Même heure demain ?"


hi "Même heure, même chaîne. Je ferais mieux d'y aller aussi, je ne veux pas risquer d'etre en retard."

show lilly cane_smileclosed
with charachange

show lilly cane_smileclosed at center
with charamove

stop music fadeout 4.0


"Lilly sourit gentiment, ramasse sa canne et sort dans le couloir."



label fr_H10:

scene bg school_hallway2
with locationchange


"Je tourne le dos à Lilly alors que nous allons dans des directions opposées. J’espère qu'elle ne se disputera pas encore avec Shizune."


"J'ai beau aimer Lilly, Shizune et Misha m'ont bien aidé à m’intégrer, même si la moitié de nos conversations tournaient autour de leurs tentatives de recrutement."


"Encore une fois, je les connais à peine. Peut-être qu'elles étaient dirigeantes d'une société sécrète, mais que leur amour les a séparées..."


"Mec, je dois arrêter de lire ces mauvais livres de fiction. Ça me pourrit le cerveau. Ça, ou je dois m'éloigner de Kenji et de sa mauvaise influence."


"C'est triste que je ne puisse plus distinguer les deux maintenant."

scene bg school_library at right
with locationskip

play music music_happiness fadein 2.0


"Je laisse tomber mes livres dans la caisse des retours et ils tombent avec un gros bruit."

play sound sfx_impact2

show yuuko panic_up
with vpunch


"Cependant, cela surprend Yuuko."


yu "H-Hisao ! Tu m'as fait peur !."


hi "Désolé, je pensais que tu t'y serais habituée depuis le temps. Ou alors le niveau des étudiants est tellement bas que personne n'emprunte de livres ?"

show yuuko worried_up
with charachange


yu "Hein ? Non, je pense que tout le monde ici sait bien lire..."


hi "Ouais... laisse tomber."


"Il y a certains combats qu'on ne peut pas gagner. Essayer d'expliquer une blague en fait partie. Mon père me l'a appris de la manière forte."


hi "Dis, Yuuko, tu as vu Hanako ? Elle est partie de classe plus tôt mais je ne l'ai pas trouvée dans sa cachette habituelle."

show yuuko closedhappy_down
with charachange


yu "Je crois l'avoir vue se faufiler ici avant le déjeuner..."

show yuuko panic_up
with charachange


yu "Oh ! Mais je ne suis pas supposée le dire !"


hi "Je viens de te dire que je l'ai vue sortir, pas besoin de stresser..."

show yuuko smile_down
with charachange


yu "Oh... c'est vrai. Elle est probablement dans le fond."


hi "Merci. Tu as reçu des nouveaux livres récemment ?"

show yuuko worried_up
with charachange


yu "Non, désolée. Je te le ferai savoir quand ce sera le cas."


hi "D'accord."


"S'il y a une chose que je sais sur les bibliothécaires, qu'ils travaillent à temps partiel ou non, c'est qu'ils apprécient les gens qui ont un véritable intêret pour leur travail."

hide yuuko
with charaexit

show bg school_library at Fullpan(10.0, dir="left")
with None


"Je parcours l'allée en direction du coin de lecture de Hanako, prenant quelques livres en chemin."


"Des fois j'ai du mal à trouver un livre qui puisse m'intéresser dans les étagères. Un nom d'auteur ou un titre à deux mots ne veut pas dire grand-chose dans cet océan de mots."


"Pour cette raison, je relis parfois des livres que j'ai déjà lus."


"Un titre inconnu d'un auteur connu se distingue de ses voisins, alors je le retire de l’étagère."


"Au moins, je ne l'ai jamais lu celui-là."

scene ev hana_library_read_std
with locationskip


"Comme prévu, Hanako est assise dans son pouf, concentrée sur un exemplaire de “Dance Dance Dance.”"


hi "Salut Hanako. Comment ça va ?"


"Je me retiens de lui demander pourquoi elle est sortie de classe aussi tôt. Si les soupçons de Lilly sont fondés, alors lui poser la question la brusquerait."


"C'est mieux de la laisser pour l'instant. Quelquesfois c'est mieux de ne pas poser de question."

show ev hana_library_smile_std
with charachange


ha "Bonjour, H-Hisao. Je vais bien."


"Quelque chose semble bizarre, et après quelques secondes, je réalise ce que c'est. Hanako sourit."


"Elle a l'air d’être contente de me voir. C'est agréable par rapport à d'habitude, où elle se raidit instinctivement. J’espère que je pourrai la voir comme ça plus souvent maintenant qu'on se connaît mieux."


hi "Tant mieux. Comment est le livre ? Il paraît qu'il est spécial."


ha "I-il est bien... Je crois."


ha "Je viens juste de le commencer, alors je n-ne sais pas vraiment."


hi "D'accord. Dis-moi comment il est, je l'emprunterai peut-être quand tu l'auras fini."


ha "D-d'accord."


"Il reste un bon quart d'heure avant la fin de la pause déjeuner. Pas suffisamment pour commencer un livre, mais trop pour rester à ne rien faire."

show ev hana_library_read_std
with charachange


"Et Hanako est déjà repartie dans sa lecture, alors je doute que je puisse discuter avec elle."


"Bah, autant me mettre à l'aise."

play sound sfx_pillow


"Je m'affale dans un pouf et j'ouvre mon livre."


"Le style familier de l'auteur se reconnaît dès la première ligne. Alors que les phrases deviennent des paragraphes, je commence à me détendre."

stop music fadeout 8.0


"Mais peu importe à quel point j'essaye, je n'arrive pas à me mettre dans l'ambiance du livre."


"C'est déjà dû au manque de temps, mais l'élément de distraction le plus important est Hanako."

show ev hana_library_std
with charachange

show ev hana_library_read_std
with charachange


"À peu près toutes les dix secondes, elle lève les yeux de son livre, mais quand nos regards se rencontrent, elle se recache rapidement derrière la couverture."


"J'imagine qu'elle voulait parler après tout."

scene bg school_library
with locationskip


hi "Qu'est-ce qu'il y a ? Tu as l'air d'être un chien de chasse à l’affût."

show hanako emb_blushing:
    center
    ypos 1.17
with charaenter


ha "N-... ce n'est rien."


hi "Je te l'ai déjà dit auparavant, “rien” veut dire “quelque chose” quand tu le dis comme ça."

show hanako cover_worry
with charachange


"Hanako se tortille un peu dans son pouf, espérant qu'en changeant de position, elle trouvera les mots qu'elle cherche."

show hanako emb_downsad
with charachange


ha "Je... J'ai eu un accident."


hi "Accident ? Maintenant ? Tu vas bien ?"

show hanako emb_sad
with charachange


"Hanako secoue la tête, ses cheveux passant au-dessus de ses épaules par mèches couleur améthyste sur un fond de peau pâle et foncée."

show hanako emb_downsad
with charachange


ha "N-non. Quand j'étais p-petite."

play music music_hanako


"Je réalise à ce moment-là."


ha "Quand je... quand j'étais..."


hi "C'est bon Hanako, tu n'as pas à m'en parler si tu ne veux pas..."


"Elle secoue encore la tête."

show hanako emb_sad
with charachange


ha "N-non. Je veux... Je dois te le dire."

scene ev hanako_crayon1:
    truecenter zoom 1.0 subpixel True
    linear 20.0 zoom 1.05
with locationskip


ha "Quand j'étais petite... Il y a eu un feu."


ha "M-ma maison a b-brûlé et j'ai failli... failli ne pas survivre."

show ev hanako_crayon2:
    linear 8.0 zoom 1.05
with charachange


ha "A-après ça... Je me suis retrouvée seule..."

scene bg school_library
show hanako emb_downsad_close:
    center
    ypos 1.1
with locationskip


"Les yeux de Hanako brillent dans la faible lumière de la bibliothèque, alors que je lui attrape la main."


hi "C'est bon, Hanako. Tu n'as pas à continuer."

show hanako emb_sad_close
with charachange


ha "M-mais... Je dois..."


hi "Pourquoi ? Pourquoi tu devrais ?"

show hanako cover_distant_close
with charachange


ha "L-la nuit dernière, Lilly m'a d-dit pour ton cœur..."

show hanako cover_worry_close
with charachange


ha "E-et je... je ne trouvais pas ça j-juste."


hi "Juste ?"

show hanako emb_blushing_close
with charachange


ha "Q-que je sache pour toi m-mais que tu ne saches pas pour moi..."


"Je serre un peu la main de Hanako."


hi "Ne sois pas bête. Mais oui, j'ai une maladie du cœur."


"Je me penche un peu vers Hanako."


hi "Ce que je n'ai pas dit à Lilly, c'est que j'ai eu ma première crise cardiaque quand une fille m'a fait sa déclaration."


"Je souris un peu pour apaiser la tension."

show hanako cover_worry_close
with charachange


ha "V-vraiment ?"


hi "Vraiment. Je n'ai plus entendu parler d'elle depuis un moment cela dit, donc j'imagine que c'est fini."


"Je sais que c'est fini. Il n'y a pas d'autre façon d’interpréter ce qui est arrivé la dernière fois que je l'ai vue. D'une certaine façon, ne plus avoir entendu parler d'elle m'a permis de mettre derrière moi cette période de ma vie."


hi "Donc maintenant, on en sait tous les deux un peu plus l'un sur l'autre. Mais tu n'as pas à me parler de certaines choses si tu ne veux pas."


"En fait, je me sens un peu mal d'avoir repensé à tout cela. Je peux presque sentir le désinfectant de l’hôpital me brûler les narines."


"J'imagine qu'il en est de même pour Hanako."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve


n "\n\nQuand j'étais à l’hôpital, j'ai été dans le service des grands brûlés une fois, juste une fois. Je m'ennuyais et je me suis baladé dans tous les services."


n "Je suis passé par l'oncologie et j'ai pensé que je pouvais le supporter, mais quand je suis arrivé chez les grands brûlés, j'ai fait demi-tour et suis retourné dans mon lit."


n "Hanako a dû passer des mois dans un endroit comme celui-là, ne sentant rien d'autre que la peau brûlée, le fort désinfectant et l'air stérilisé."


n "Les cas les plus graves étaient gardés dans des bulles où aucun objet étranger ne pouvait entrer. Ça aurait signifié pas de lecture."


n "\nJe serais devenu fou si je n'avais pas pu avoir mes livres à l’hôpital."


n "Et elle a dit qu'elle s'était retrouvée seule..."


n "Est-ce que ses parents sont morts ? Je vais devoir demander ça à Lilly. Je serais capable de dire quelque chose d'idiot sans faire exprès."

stop music fadeout 2.0

nvl clear
nvl hide dissolve

show hanako emb_timid_close
with charachange

window show


ha "M-merci, Hisao."

show hanako emb_downtimid_close
with charachange


ha "Je... je n'ai pas raconté ça à beaucoup de gens."


hi "Pour être honnête, je n'ai pas parlé de mes... problèmes à grand monde non plus."

show hanako cover_smile_close
with charachange


ha "A-alors je ne le dirai à p-personne non plus."


hi "D'accord."

play sound sfx_warningbell


"Mon contact avec la main de Hanako se transforme en une poignée de main alors que la première sonnerie parvient à nos oreilles."


hi "Bon, on ferait mieux de retourner en classe, non ?"

show hanako basic_bashful_close
with charachange


ha "O-oui."
$ renpy.music.set_volume(1.0, 0.0, channel="music")

window hide

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
