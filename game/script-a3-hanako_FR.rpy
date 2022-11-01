label fr_H11:

scene bg school_miyagi_ss
show hanako basic_distant_close_ss at center
with locationchange


"La lumière de la pièce passe doucement du clair de l'après-midi à l'oranger du soir. Une horloge tique paresseusement, comptant les secondes dans le fond, mais est à peine audible."


"Mais peu importe à quel point j’attends, le résultat ne peut être changé."


"La petite pièce fait un clic sur l'échiquier."

show hanako basic_normal_close_ss
with charachange


"Comme un ressort, Hanako fait son mouvement peu après le mien."


"C'est embarrassant. En comparaison de mon mouvement de cinq minutes, elle semble savoir exactement ce qu'elle veut faire."

show hanako basic_smile_close_ss
with charachange

play music music_tranquil fadein 3.0


ha "Echec et mat."


hi "Encore... Ça fait combien ? 3-2 ?"

show hanako cover_bashful_close_ss
with charachange


ha "L-les impasses ne comptent pas."


hi "Rah. Tu deviens meilleure de jour en jour."


"Ça, ou elle se retenait. Je n'aurais jamais pensé ça quand je l'ai rencontrée pour la première fois, mais elle a vraiment un truc pour ce jeu."


"Les échecs semblent être devenus un passe-temps prisé de nous deux ; nous nous isolons dans la pièce où on boit le thé, jouant une partie ou deux après les cours."


"D'ici, on n'entend presque pas les étudiants qui sont à l'extérieur. Les bruits de tous les jours me rappellent un peu ma vie d'avant Yamaku, bien que je sache que c'est une vie que je ne reverrai jamais."


hi "Partante pour une autre partie ?"

show hanako basic_worry_close_ss
with charachange


ha "Je... Je dois finir mes devoirs..."


hi "Oh. Bon, on se voit demain alors."

show hanako basic_distant_close_ss
with charachange


ha "Mais... et pour ça..."


"Hanako pointe le service à thé entourant l'échiquier presque vide."


hi "Ne t’inquiète pas pour ça, je m'en occupe."

show hanako basic_normal_close_ss
with charachange


ha "Oh... d'accord..."

show hanako basic_bashful_close_ss
with charachange


ha "S-salut."


hi "À plus."

hide hanako
with charaexit


"Hanako s'en va alors que je commence à nettoyer."


"Les sifflements et encouragements des clubs de sports à l'extérieur deviennent de moins en moins fréquents, jusqu’à ce que le silence s'installe."


"Une partie de moi veut toujours faire partie d'une équipe. Vu que je jouais au foot ou à d'autres sports avant mon accident, j'imagine que c'est normal de me sentir nostalgique de ce que je ne peux plus faire."


"Mais j'ai d'autres raisons que celle-ci pour venir ici aussi souvent et ça me va de perdre une partie de moi-même pour elles. Lilly est une bonne amie maintenant, mais c'est les petits échanges que j'ai avec Hanako qui me sont le plus cher."


"Les petites victoires que je ressens tous les jours, quand je vois comment elle est sous sa carapace. C'est surtout pour ça que je viens ici."


"Alors que je range les tasses et les coupelles, j’entends parler derrière la porte. M’arrêtant un moment pour écouter, je remarque que c'est Hanako et Lilly et je décide de sortir pour les rejoindre."

scene bg school_hallway2
show lilly basic_weaksmile at twoleft
show hanako emb_downtimid at tworight
with locationchange


li "Tu es vraiment sûre ?"


ha "Je... suis sûre..."

show hanako emb_timid
with charachange


ha "Ah, Hisao."


"Hanako se tourne vers moi et a l'air surprise en me remarquant. Lilly doit l'avoir croisée juste avant qu'elle ne parte."

show lilly basic_smile
with charachange


li "Eh bien, Hisao est là aussi ?"


hi "Salut, Lilly. Quoi de neuf ?"

show lilly basic_smileclosed
with charachange


li "J’espérais, maintenant que j'ai fini mes devoirs de déléguée pour la journée, que vous puissiez m'accompagner tous les deux au Shanghai pour boire le thé. Ça aurait été bien de faire ça en dehors de l'école, pour changer."


hi "Ça me va. Je crois que Hanako a du travail à faire, cela dit..."

show hanako basic_smile
with charachange


ha "P-pas... tant que ça..."

show lilly behind_cheerful
with charachange


li "Parfait. C'est décidé alors."

stop music fadeout 2.0

scene bg suburb_shanghaiint at Fullpan(3.0, dir="left")
with shorttimeskip

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0


"Je tourne la tête alors que nous entrons dans le café. Comme d'habitude, il y a très peu de gens ici et c'est plutôt silencieux."

scene bg suburb_shanghaiint at left
show hanako emb_emb:
    xpos 0.4 xanchor 0.5
show lilly cane_smileclosed at twoleft
with charaenter

play music music_dreamy fadein 6.0


"Lilly continue de tenir le bras de Hanako comme elle l'a fait durant notre lente descente de la colline, bien que ce soit dur de savoir pour quelle raison - pour guider Lilly, ou pour rassurer Hanako."

show lilly basic_smile
with charachange


"Pendant un moment, Lilly enlève son bras posé sur celui de Hanako pour rétracter sa canne alors que Yuuko arrive en trottinant, mais elle remet rapidement son bras là où il était."

show yuukoshang closedhappy_up at tworight
with charaenter


yu "Bienvenue au Shanghai ! Puis-je prendre votre commande ?"

show yuukoshang neutral_up at Transform(ypos=1.25)
with Dissolvemove(0.5)

show yuukoshang neutral_down at tworight
with dissolvecharamove


"Elle se penche et semble de bonne humeur d’après sa parfaite présentation professionnelle. Cela change par rapport à d'habitude."

show lilly basic_smileclosed
with charachange


li "Juste du thé, s'il te plaît. Hanako, Hisao ?"


hi "Je vais prendre une part de tarte et un café."

show hanako basic_smile
with charachange


ha "Juste... d-du thé... s'il te plaît."

show yuukoshang smile_up
with charachange


yu "Bien compris. Asseyez-vous, je reviens tout de suite."

hide yuukoshang
with charaexit


"Yuuko sourit et hoche la tête avant de se dépêcher d'aller jusqu'au comptoir pendant que nous allons vers une table libre à côté de la fenêtre."

hide hanako
hide lilly
with charaexit

show bg suburb_shanghaiint at right
with charamove_slow

show lilly basic_sleepy_close:
    twoleft
    easein 1.0 ypos 1.1
show hanako basic_smile_close:
    tworight
    easein 1.0 ypos 1.09
with charaenter


"Nous nous asseyons, les filles d'un côté avec la canne de Lilly posée à côté d'elles, et moi en face. Je réalise que Hanako n'agit pas comme d'habitude."


"Plutôt que de garder les yeux rivés vers le sol et de se cacher derrière son escorte aveugle, essayant de toutes ses forces de se convaincre que le monde autour d'elle n'existe pas, elle ne baisse presque pas les yeux et aide Lilly."


hi "Ça va, Lilly ? Tu sembles fatiguée."

show lilly basic_weaksmile_close:
    twoleft
    ypos 1.1
with charachange


"Elle baisse un peu la tête, ayant l'air quelque peu embarrassée de le laisser transparaître."


li "Le devoir de déléguée peut être vraiment fatigant, vu que cela signifie avoir souvent affaire au Conseil des Étudiants."

show lilly basic_sleepy_close
with charachange


li "Vraiment très fatigant."

show hanako basic_normal_close:
    tworight
    ypos 1.09
with charachange


ha "Comment... s'en sortent les autres délégués ?"

show lilly basic_reminisce_close
with charachange


li "Mieux que moi, mais pas si bien que ça. Shizune est sévère avec tout le monde."


hi "Tu n'as pas l'air de tellement apprécier. Pourquoi tu es déléguée, si c'est si dur ?"

show lilly basic_displeased_close
with charachange


li "C'est agréable d'être déléguée et je m'en sors bien avec les responsabilités. C'est juste que les gens impliqués sont des fois..."


"Elle s’arrête au bon moment. C'est difficile d'imaginer Lilly dire une insulte, mais j'imagine que si quelqu'un peut la pousser à ça, c'est bien Shizune."

show hanako cover_worry_close
with charachange


"Hanako semble être un peu gênée par le conflit, et avant que je ne puisse changer de sujet, elle se lève."

show hanako basic_worry_close at tworight
with dissolvecharamove

show lilly basic_surprised_close
with charachange


li "Hanako ?"

show hanako defarms_strain_close
with charachange


ha "Je... reviens."

hide hanako
with charaexit


"Sur ce, elle part en direction des toilettes. J'imagine que c'est une façon comme une autre de gérer la situation, enfin, si c'était la raison."

show bg suburb_shanghaiint at center
show lilly basic_concerned_close at Position(xpos=0.5)
with dissolvecharamove


"Lilly, cependant, semble un peu attristée."


hi "Ne t’inquiète pas. Je ne crois pas que ce soit à cause de toi."

show lilly basic_oops_close
with charachange


li "Mais..."


hi "Je crois qu'elle s'améliore en ce moment. Tu l'as vu aussi... non... ?"


"J'ai mal choisi mes mots. Heureusement Lilly ne semble pas mal le prendre et maintenant je ne devrais pas avoir si peur de marcher dans ce champ de mines avec elle."

show lilly basic_sleepy_close
with charachange


li "Possible. Des fois... c'est difficile à dire."


"Le silence règne un moment avant que deux tasses à thé, une tarte, et un mug à café apparaissent en face de nous."

show bg suburb_shanghaiint at right
show lilly basic_sleepy_close at Position(xpos=0.3)
with charamove

show yuukoshang closedhappy_down at tworight
with charaenter


"Je remarque que Yuuko prête une attention particulière à placer la tasse à thé contre les doigts de Lilly, la laissant savoir où elle est."

show yuukoshang closedhappy_up
with charachange


yu "Et voilà."


hi "Merci Yuuko."

show lilly basic_weaksmile_close
with charachange


li "Merci."

hide yuukoshang
with charaexit


"Avec une rapide courbette, la serveuse à lunettes s'en va."

show bg suburb_shanghaiint at center
show lilly basic_weaksmile_close at Position(xpos=0.5)
with charamove


li "Ah, c'est vrai. Je voulais te demander quelque chose et c'est le bon moment maintenant."


hi "Je t'écoute."

show lilly basic_smileclosed_close
with charachange


li "L'anniversaire de Hanako arrive bientôt et j'aurais espéré que tu puisses m'accompagner pour acheter un cadeau en ville ce week-end."


"C'est bientôt l'anniversaire de Hanako. C'est une bonne occasion de lui remonter le moral. Comme Yuuko, elle semble être toujours au bord de la panique ou de la dépression, et je ne l'ai jamais vue s'amuser en dehors de nos parties d’échecs."


"Tout cela mis à part, me familiariser avec la ville en compagnie d'une amie semble une bonne façon de passer le week-end."


hi "Bien sûr, avec plaisir. Tu as quelque chose de prévu pour son anniversaire ? Une fête ou autre ?"

show lilly basic_weaksmile_close
with charachange


li "Hanako étant Hanako, peut-être que quelque chose de discret serait—"

show lilly basic_listen_close
with charachange


"Lilly s’interrompt soudainement, sans que je sache pourquoi, tandis qu'elle amène sa tasse à ses lèvres et commence à boire."


"Après quelques secondes, je remarque Hanako par-delà son épaule. Lilly doit vraiment avoir une bonne ouïe si elle a remarqué le bruit de la porte des toilettes qui s'ouvre."

show bg suburb_shanghaiint at bgleft
show lilly basic_listen_close at Position(xpos=0.3)
with charamove

show hanako basic_normal_close:
    tworight
    easein 1.0 ypos 1.09
with charaenter


"Hanako se rassoit et n'attend pas pour boire son thé. Nous nous retrouvons à manger et boire silencieusement alors que le soleil se couche."


"C'est une bonne façon de passer la fin de la journée et ça me fait apprécier les environs silencieux et sereins de Yamaku. Je crois que je commence vraiment à apprécier la vie ici, aussi isolée qu'elle puisse être."

stop ambient fadeout 2.0

scene bg suburb_shanghaiint at bgleft
show lilly basic_smileclosed_close:
    twoleft
    ypos 1.1
show hanako basic_smile_close:
    tworight
    ypos 1.09
with shorttimeskip


"Je finis mon café et pose mon mug sur la table pendant que les filles discutent entre elles. Le café ici est un peu fort à mon goût, mais il reste bon. Meilleur que ceux que je fais moi-même du moins."


"La discussion des filles tourne surtout autour de leurs préférences de lecture respectives, ce qui me rend quelque peu curieux à propos d'autre chose."


hi "Dis Hanako, je me demandais... à part les échecs et la lecture, tu as d'autres hobbies ?"

show hanako emb_timid_close
with charachange


"Elle s’arrête, ayant l'air surprise que quelqu'un puisse être intéressé par une chose pareille. Il lui faut un petit moment pour formuler une réponse."

show hanako emb_downsmile_close
with charachange


ha "Hum... J'imagine... J'aime un p-peu chanter. Je m'en sors bien avec les ordinateurs aussi, mais je... ne les utilise pas beaucoup."


"Je ne m'attendais pas à ce qu'elle chante. C'est difficile d'imaginer comment elle chante, vu qu'elle parle déjà si doucement."

show lilly basic_smile_close
with charachange


"Lilly, quant à elle, hoche simplement la tête, elle doit déjà savoir tout ça, vu qu'elle est amie avec Hanako depuis près d'un an maintenant."

show hanako cover_bashful_close
with charachange


ha "E-et... t-t..."


hi "Moi ?"

show hanako basic_bashful_close
with charachange


"Elle hésite avant de hocher la tête. C'est normal qu'elle veuille que je parle de mes hobbies après que je lui aie demandé de parler des siens."


hi "Il y a les échecs, bien sûr, mais aussi... euh..."


hi "Il y avait le football, bien que je ne puisse plus vraiment en faire maintenant. La lecture, que j'ai appris à aimer à l’hôpital... euh..."

show hanako basic_normal_close
show lilly basic_sleepy_close
with charachange


"C'est étonnamment difficile. Lilly et Hanako semblent un peu gênées par la direction que prend la discussion et plus j'y pense, plus cela me gêne également."

show lilly basic_weaksmile_close
with charachange


li "On dirait que tu as découvert de nouvelles choses depuis ton accident."


"La franchise de Lilly est enrobée de tout le positif qui peut être trouvé dans ce que j'ai dit. Hanako, quant à elle, est silencieuse."


"Si une situation devient difficile, Hanako semble toujours devenir silencieuse pour éviter d'empirer les choses. Ça, ou alors elle s'en va."

$ renpy.music.set_volume(0.2, 0.0, channel="sound")
play sound sfx_phone

show lilly basic_surprised_close
show hanako cover_worry_close
with charachange


"Une sonnerie nous interrompt. Alors que Lilly cherche dans sa poche, il est évident que le son provient de son téléphone."

show lilly basic_weaksmile_close
with charachange


li "Désolée..."

show hanako basic_normal_close
with charachange


ha "C-c'est pas grave..."

show lilly invis_close at Position(ypos=1.0)
with dissolvecharamove

hide lilly
with None


"Lilly hoche brièvement la tête avant de se lever et de prendre l'appel un peu plus loin pour éviter de nous gêner."


hi "Ça doit être bien d’être populaire."

show hanako cover_bashful_close
with charachange


"Hanako sourit, mais ne continue pas la conversation."

$ renpy.music.set_volume(0.5, 2.0, channel="music")

scene black
with shuteye


"Je finis par me mettre contre le dossier et fermer les yeux, me relaxant autant que je le peux."


hi "On est bien ici. Je me demande ce que ça fait de grandir dans un endroit comme celui-ci, loin de la ville."


ha "T-tu es de la ville ?"


"On dirait que j'ai trouvé un sujet qui l'intéresse."

$ renpy.music.set_volume(1.0, 2.0, channel="music")

scene bg suburb_shanghaiint at center
show hanako basic_smile_close:
    center
    ypos 1.09
with openeye


hi "Ouais, on peut dire que je suis un enfant de la ville, pur et dur."

show hanako basic_worry_close
with charachange


ha "O-on dirait que beaucoup de choses ont changé..."


hi "Oui. Je ne sais toujours pas comment gérer tout ça, cela dit. C'est un peu un choc culturel, de beaucoup de façons différentes."


hi "Tu as dû vivre quelque chose dans le genre quand tu es arrivée à Yamaku, nan ? J'imagine que c'est le cas pour la plupart des étudiants."

show hanako basic_distant_close
with charachange


ha "P-pas vraiment..."


"Hanako détourne un peu le regard, n'ayant pas envie de continuer la conversation. Je penche la tête, intrigué, mais quelques secondes se passent sans réponse de sa part."

scene bg suburb_shanghaiint at bgright
show hanako basic_distant_close:
    tworight
    ypos 1.09
with charamove

show lilly back_pout at twoleft
with charaenter

stop music fadeout 8.0


li "Mais on ne peut pas s'occuper de ça lundi ? Les retombées sont à peine réglées depuis la dernière..."

show lilly back_listen
with charachange


li "Je comprends. J'essayerai de lui parler. Tu sais comment elle est quand elle a une idée derrière la tête."


li "Oui, merci. On en reparlera plus tard alors. Au revoir."

show lilly basic_displeased
with charachange


"La conversation de Lilly s’arrête avec le clac de son téléphone. Elle revient à notre table, mais ne s'assied pas."


hi "Tu dois y aller ?"

show lilly basic_concerned
with charachange


li "Malheureusement. Le devoir de déléguée m'appelle."

show hanako cover_worry_close
with charachange


ha "J-je peux venir avec toi."

show lilly basic_weaksmile
with charachange


li "Ne t’embête pas, Hanako. Je vais juste au Conseil des Étudiants. Pas besoin de gâcher un si bel après-midi pour moi."

show lilly basic_smile
with charachange


li "En plus, si tu me raccompagnais à l'école, qui tiendrait compagnie à notre pauvre Hisao ?"

show hanako basic_normal_close
with charachange


ha "D'accord..."

show lilly basic_weaksmile
with charachange


li "Je peux vous rejoindre pour le thé plus tard ce soir, si vous voulez. J'en aurai sûrement besoin."

show lilly cane_weaksmile
with charachange


"Nous nous mettons d'accord là-dessus, Lilly nous dit au revoir et prend la canne que Hanako lui tend."

hide lilly
with charaexit


"Malgré mon offre de payer pour Lilly, elle insiste pour régler sa part et salue Yuuko avant de partir."

play music music_dreamy fadein 4.0

show bg suburb_shanghaiint at center
show hanako basic_normal_close:
    center
    ypos 1.09
with charamove


"Et enfin... nous nous retrouvons seuls. C'est peut-être gentil de nous laisser tous les deux pour qu'on passe du temps ensemble, mais ça signifie surtout qu'on va rester assis tous les deux en silence pendant un moment."


"Je me demande comment Hanako me voit. Je ne pense pas être effrayant, mais que quelqu'un de mon âge agisse comme ça avec moi me trouble un peu, comme si c'était de ma faute qu'elle soit si gênée."


"Elle pourrait s'habituer plus aux gens si elle sortait de Yamaku, mais encore une fois... quand même des gens beaucoup plus âgés qu'elle réagissent si vivement après un seul coup d'oeil sur son visage, ça doit être difficile."


"C'est un cercle vicieux. Si elle reste à Yamaku, elle ne s'habituera jamais aux contacts des autres, mais si elle sort, tous les efforts qu'elle fera lui seront renvoyés dans la figure par les gens qui ne peuvent pas supporter ses cicatrices."


hi "Tu veux commander quelque chose d'autre ? On n'a pas beaucoup mangé, après tout."

show hanako basic_smile_close
with charachange


"Hanako s'illumine et hoche vigoureusement la tête, contente que j'aie abordé le sujet. Je croise le regard de Yuuko et elle arrive pour prendre nos commandes."

scene bg suburb_shanghaiint at bgright
show hanako basic_smile_close:
    tworight
    ypos 1.09
with charamove

show yuukoshang neutral_down at twoleft
with charaenter


yu "Vous voulez quelque chose d'autre ?"


hi "Je vais prendre un sandwich spécial et un chocolat chaud. Il est un peu tard pour un café. Hanako ?"

show hanako cover_bashful_close
with charachange


ha "J-je vais... prendre la même chose..."

hide yuukoshang
with charaexit


"Avec un hochement de tête et une courbette, Yuuko tourne les talons et retourne derrière le comptoir où elle s'occupe du pain, des épices et de la machine pour faire nos boissons."

show yuukoshang smile_up at twoleft
show hanako basic_bashful_close
with charaenter


"Pas un mot n'est dit avant que Yuuko ne revienne. Elle sourit et nous sert, avant d'aller vers un autre client qui l'appelle."

hide yuukoshang
with charaexit

show bg suburb_shanghaiint at center
show hanako basic_bashful_close:
    center
    ypos 1.09
with dissolvecharamove


"J'abandonne l'espoir d'avoir une conversation avec Hanako et apprécie juste mon repas, aussi frugal qu'il puisse être."


"Le sandwich est bon, comme la plupart des choses faites ici. Après quelques bouchées, je remarque qu'il manque quelque chose, Hanako ne mange pas."

show hanako basic_distant_close
with charachange


"La regardant, je vois Hanako gigotant un peu derrière son sandwich intact."


hi "Pas faim ?"

show hanako cover_worry_close
with charachange


"Elle secoue la tête. Même pendant qu'elle fait ça, les cheveux qu'elle maintient sur le coté droit de son visage continuent de remplir leur fonction et de la cacher presque entièrement."


ha "C-c'est pas ça."


hi "Erh. Et moi qui étais prêt à prendre ta part."

show hanako basic_worry_close
with charachange


ha "Tu avais l'air... t-troublé. Q-quelque chose... ne va p-pas ?"


"Je suis étonné qu'elle pense que je suis celui qui a l'air troublé, mais en y réfléchissant, elle a probablement raison. J'ai dû afficher mes émotions sur mon visage sans le remarquer et elle n'est pas bête, loin de là."


hi "On est amis, hein ?"

show hanako emb_downsad_close
with charachange


ha "Amis..."


"D’après le ton de sa voix et son renfrognement, on dirait que j'ai marché dans un autre champ de mines."


"C'est une autre raison pour laquelle il est difficile d'intéragir avec elle, elle impose une barrière psychologique entre elle et les autres, même avec Lilly et moi. C'est dommage qu—"

show hanako basic_bashful_close
with charachange


ha "Je-je crois qu-qu'on est... amis..."


"Je suis un peu surpris de la réponse directe de Hanako, d'autant plus que j'étais sur le point de renoncer à une réponse tout court."


hi "Je vois..."

show hanako basic_worry_close
with charachange


ha "J-je me trompe ? D-désolée, je-je..."


hi "Non, c'est juste que... en entendre la confirmation de ta part est rassurant."


hi "Pour revenir sur ce que tu as dit plus tôt, depuis que je suis à Yamaku, je ne sais pas trop quelle relation j'ai avec les gens."


"Je me retrouve à rire un peu. C'est surprenant à quel point ça me soulage. Je peux me sentir sourire alors que j'attrape mon chocolat chaud et l'apporte à mes lèvres."


hi "Aie ! C'est chaud..."

show hanako emb_downsmile_close
with charachange


ha "C-c'est pour ça..."

show hanako emb_smile_close
with charachange


ha "C'est pour ça que je n'ai pas encore mangé. J-j'attendais que... mon chocolat refroidisse d'abord."


hi "Je vais attendre aussi, alors."


"Nous partageons un petit rire. La situation n'est pas vraiment drôle, mais pour je ne sais quelle raison... rire me semble la chose la plus naturelle à faire."


"J'imagine qu'on est tous les deux un peu gênés à propos de l'autre. J'étais tellement occupé à penser que c'était Hanako qui avait un problème avec ça, que j'en ai oublié que je n'étais pas à l'aise non plus."


"Mais malgré tout... ça fait plaisir. Plaisir d'avoir quelqu'un qui pense à moi comme ça, à sa façon."

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
stop music fadeout 8.0

scene bg school_dormext_full_ni
with shorttimeskip


"S'ensuit un long trajet dans le silence jusqu’à l'école, où nous nous retrouvons entre les deux dortoirs."


"Des patrouilles de nuit régulières passent entre les deux dortoirs, par sécurité et pour donner rapidement l'alerte en cas d'urgence médicale. Le garde en fonction nous remarque et nous adresse un hochement de tête avant de continuer son chemin."

show hanako emb_downtimid_ni at center
with charaenter


"Un grand bâillement s’échappe de la bouche de Hanako avant qu'elle n'ait une chance de le couvrir. Elle doit être très fatiguée."


hi "Je ferais mieux d'y aller. À demain, Hanako."

show hanako emb_smile_ni
with charachange


ha "B-bonne nuit..."

hide hanako
with charaexit


"Nous nous séparons et allons dans la direction opposée, avant que je m'arrête et me retourne."

show hanako basic_smile_ni
with charaenter


"Hanako se tient là, me faisant un signe en souriant. Je souris et lui retourne le geste et après quelques secondes, elle se tourne et monte les escaliers de son dortoir, disparaissant derrière la porte."

hide hanako
with charaexit


"Ces petits moments qu'on partage sont comme un trésor. Une chose est sûre, je veux protéger ce petit sourire délicat qu'elle affiche face à si peu de gens."


"Je m'interroge sur ces sentiments que j'ai quand Hanako est là, sur ce que je peux faire pour elle... et si ça peut évoluer en quelque chose de plus que ce que nous avons maintenant."

scene black
with dissolve



label fr_H12:

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play music music_happiness fadein 2.0

scene bg school_track
with locationchange


"Le soleil d'été est quelque chose qui doit se savourer, mais quand il est accompagné d'un air frais de la campagne, c'est encore mieux."


"Les membres du club d’athlétisme sont en train de courir sur le terrain, certains jouent avec un ballon de football, d'autres discutent, et quelques-uns rient pendant que deux d'entre eux se disputent."


"Aucun d'entre eux ne fait attention à moi alors que je m'assois dans l'herbe, à l'ombre d'un arbre particulièrement grand. C'est agréable après une longue journée d'école."

play ambient sfx_footsteps_soft fadein 4.0


"Je jouais souvent au foot avant ma crise cardiaque, alors je me suis dit que je me sentirais nostalgique en les regardant. Pourtant, ce que je ressens actuellement est totalement différent."

stop ambient fadeout 0.3

show miki smile:
    center
    easein 1.0 ypos 1.12
with charaenter


"J’entends quelqu'un s'approcher et je me tourne pour voir une de mes camarades de classe s’asseoir à côté de moi. Ça me surprend, vu qu'on n'a jamais vraiment parlé auparavant. De plus, je ne pensais pas que quelqu'un me verrait ici."

show miki grinclosed:
    center
    ypos 1.12
with charachange


mk "Yo."


hi "Salut. Miura, c'est ça ?"

show miki wink
with charachange


mk "Appelle-moi juste Miki. Les noms de famille c'est trop lourd."


hi "Appelle-moi Hisao alors."

show miki smile
with charachange


"Nous regardons tous les deux le terrain où les gars sont en train de jouer. On dirait qu'ils sont prêts pour une deuxième partie ; les gens se mettent en place et le ballon est amené au milieu du terrain."


"Peu après, le coup de sifflet est donné et le match commence."


hi "Tu ne joues pas ?"

show miki grinclosed
with charachange


mk "Nan, je me repose un peu."

show miki wink
with charachange


mk "Et toi ? Tu avais l'air de vouloir jouer quand tu nous regardais."


"Donc quelqu'un m'a bien remarqué."


hi "C'est une longue histoire."

show miki grin
with charachange


"Son expression montre que j'ai piqué son intérêt."


hi "Je suis à Yamaku à cause d'une maladie du cœur. Je ne peux plus vraiment jouer au foot."

show miki smile
with charachange


mk "Tu voulais devenir joueur de foot, hein ?"


hi "Non, c'était vraiment que pour m'amuser. Mes amis y jouaient, alors j'y jouais aussi."


hi "J'aurais pu être n'importe lequel de ces gars avant mon accident. Mais je n'ai pas vraiment envie de retourner à cette époque non plus. C'est un peu compliqué à expliquer."


"J'ai toujours une bonne condition physique grâce au sport que je faisais, même si j'ai perdu beaucoup de ma force. En plus, je m'entendais bien avec les autres membres du club."


"Quand j'y pense, je devrais me sentir mal de voir les gens jouer alors que je ne peux pas. Et pourtant ça ne me gêne pas. Peut-être que c'est une bonne chose, un signe que je suis passé au-dessus de tout ça et que je suis prêt à avancer."


hi "Désolé, je radote un peu."

show miki grinclosed
with charachange


mk "C'est super. Je suis contente d'entendre ça."

show miki smile
with charachange


mk "On dirait que tu t'en sors bien. Certaines personnes qui arrivent ici sont vraiment perturbées au début."


hi "Donc tu es un membre du club d’athlétisme ?"

show miki grin
with charachange


mk "Yep. Depuis que je suis arrivée ici."


hi "J'imagine que tu es amie avec Emi ? Petite, court vite, pas de jambes ? Je ne crois pas qu'il y ait autant de filles que ça dans le club d’athlétisme."

show miki grinclosed
with charachange


mk "Haha, Emi. Tout le monde la connaît."

show miki smile
with charachange


mk "Mais nan, je m'entends mieux avec les mecs, donc Emi et moi on ne parle pas tellement. Bref, et toi ? Tu es dans un club ?"


hi "Ah, euh, je ne suis pas vraiment dans un club. Pas un vrai club, du moins."

show miki wink
with charachange


mk "Tu traînes avec Hanako et l'amazone blonde, c'est ça ?"


"L'amazone blonde... j'imagine que Lilly est assez grande pour correspondre à la description. Je hoche la tête, sans trop approuver son appellation."

show miki grinclosed
with charachange


mk "Alors ne t’inquiète pas. Tant que tu as des amis, tu n'as pas besoin de rejoindre un club."


"Un sifflet provenant du terrain attire notre attention. Un des joueurs est sur le sol, se tenant la jambe et les autres arrêtent de jouer pour se diriger vers lui, même Miki grimace."

show miki serious
with charachange


mk "Ouch, ça a l'air douloureux. Ce gars n'a vraiment pas de chance."


"Alors qu'elle continue de regarder le terrain, je me rappele ses propres blessures. Son bras gauche, s’arrêtant par une bosse, est entouré d'un bandage depuis que je suis à Yamaku, mais sa blessure ne semble pourtant pas récente."


"Elle se tourne pour me parler et me surprend en train de la regarder. Nous restons assis dans un étrange silence alors qu'elle cache son bras avec sa main."


hi "D-désolé. Je crois que je suis toujours un peu..."

show miki smile
with charachange


mk "C'est pas grave. Vraiment."


"Son ton est léger, mais aucun de nous deux ne rajoute quelque chose. Chaque étudiant handicapé a sa propre façon de gérer ses problèmes et le fait que certains les trouvent gênants est normal. Je suis l'un d'entre eux, après tout."


"Le gars qui s'est fait mal sur le terrain se relève avec de l'aide et finit par boiter hors du terrain en s'appuyant sur l'épaule de quelqu'un d'autre. Probablement juste une foulure, s'il arrive toujours à marcher."


"Le sifflet se fait entendre encore une fois et la partie continue avec un homme de moins sur le terrain."

show miki whistle
with charachange


mk "Traîner avec Hanako et cette fille blonde... tu es en étrange compagnie."


hi "Comment ça ?"

show miki serious
with charachange


mk "C'est juste que Hanako est... je sais pas."


hi "Timide ?"


mk "Non, c'est pas vraiment ça. C'est juste... qu'elle a certains problèmes, je crois. Je n'arrive pas à bien le formuler."

show miki wink
with charachange


mk "Pas qu'elle ne soit pas quelqu'un de bien, hein. Elle est très bien."

show miki serious
with charachange


mk "Juste... difficile à gérer."


"On dirait que Miki, ou du moins quelqu'un d'autre dans la classe, a déjà essayé de se rapprocher de Hanako dans le passé. Et ça ne s'est pas bien passé."


"Je la trouve plutôt dure, vu que tout le monde, pas que ceux à Yamaku, a ses propres problèmes. Mais encore une fois, je ne connais pas Hanako depuis si longtemps, donc ça ne me surprendrait pas qu'il y ait certaines choses que je ne sache pas."


hi "Je vais prendre les choses comme elles viennent. C'est quelqu'un de bien et je pense que c'est tout ce qui compte."


"Miki plisse légèrement les yeux et affiche un grand sourire."

show miki grin
with charachange


mk "Tu l'aimes vraiment beaucoup, hein ?"

label fr_choiceH12:
menu:
    with menueffect
    "Miki ne mâche pas ses mots."
    "L'admettre.":




        return m1
    "Le nier.":


        return m2


label fr_H12a:


hi "Pour être vraiment honnête... ouais, c'est vrai. J’apprécierais aussi si tu ne le disais à personne."

show miki wink
with charachange


mk "T’inquiète, tu peux me faire confiance. Aucun problème."

show miki grinclosed
with charachange


mk "Pour être honnête, je trouve ça mignon. Si tu veux te lancer, ne me laisse pas t’arrêter."


hi "Merci."


"Elle dit peut-être ça, mais elle vient de dire que Hanako a des “problèmes”. Mais même, je préfère m’arrêter à sa dernière phrase. Les problèmes de Hanako ne comptent pas. Je ferai face à tout ce qui arrivera, parce que je veux l'aider."


"S'il y a ne serait-ce que la plus infime possibilité que je puisse sortir Hanako de sa dépression et de son isolement, alors je continuerai, peu importe comment. Si elle a besoin d'un prince, alors je serai ce prince."


"Alors que je pense à la possibilité d'une relation plus poussée, je peux voir Miki sourire en me regardant. Il est évident que je rougis et le fait que je tourne la tête la fait rire."


label fr_H12b:


hi "Je ne crois pas. On est juste amis."

show miki serious
with charachange


mk "Aw. Et moi qui croyais avoir découvert quelque chose d’intéressant. Je comprends ; les filles et les garçons n'ont pas forcément besoin d'être petit ami et petite amie, après tout."


"Ce qu'elle dit est vrai, même s'il est vrai que j'ai des sentiments pour Hanako. Pour l'instant nous sommes de bons amis et je ne veux pas gâcher ça, mais je veux aussi être plus que ça pour elle. C'est compliqué."


label fr_H12c:


"Miki est différente des autres filles. Lui parler me donne plus l'impression de parler à un garçon qu'à une fille. Le fait qu'elle ait dit qu'elle préfèrait la compagnie des garçons n'aide pas à chasser cette impression non plus."


"Un regard à ma montre m'indique que la pause déjeuner finit dans quelques minutes. Il est temps de retourner en classe."


hi "C'est la fin de la pause. On y retourne ?"

show miki smile
with charachange


mk "Ouais, on ferait mieux."

show miki smile at center
with charamove


"Je me relève et m’époussette, offrant une main à Miki pour l'aider à se relever. Elle l'attrape et se relève facilement, montrant les muscles de son bras en action."


hi "En y pensant, pourquoi tu ne portes pas la chemise normale des filles ?"

show miki whistle
with charachange


mk "Bah, c'est trop chaud et contraignant. L'uniforme des garçons est mieux de toute façon."


"Elle tend les bras pour argumenter, ce qui a pour effet de montrer une partie de son corps qui aurait été spécialement cachée avec la chemise."

scene bg school_gardens
with locationchange


"Nous retournons au bâtiment principal en passant par les jardins, discutant en même temps."

show miki smile at center
with charaenter


mk "On dirait que tu t'adaptes bien. Tant mieux. C'était surprenant qu'un étudiant soit transféré à ce moment de l'année, vu que les examens arrivent bientôt."


hi "Ne m'en parle pas..."

show miki grinclosed
with charachange


mk "Haha, ne t’inquiète pas pour les exam. Vas-y avec du culot et tout ira bien."


hi "Ça ne ressemble pas à un bon conseil."

show miki grin
with charachange


"Elle tape plusieurs fois sur mon épaule et sourit. Elle ne semble pas prendre l'école au sérieux."

show miki wink
with charachange


mk "Tu sembles être un mec intelligent et Mutou t'a à la bonne."


hi "Je ne sais pas trop si c'est une bonne ou une mauvaise chose."


hi "Je ne sais toujours pas quoi penser de cette école. Je suis là depuis plusieurs semaines, mais je me sens quand même perdu à certains moments."

show miki smile
with charachange


mk "Tu t'y feras, laisse-toi le temps. C'est un lycée comme un autre."


"Elle dit cela si simplement, je n'y avais jamais pensé comme ça. Pour moi, Yamaku symbolise un changement dans ma vie. Je ne suis plus normal, je suis “différent” et je vais à l'école avec des gens “différents”."


"Et pourtant, je retourne en classe et parle avec une camarade de classe durant la pause déjeuner après en avoir regardé d'autres jouer au foot - tout est parfaitement normal. Peut-être qu'elle a raison, après tout."


"Peut-être que je devrais voir Hanako de la même façon. Tout le monde a ses problèmes, ce n'est pas quelque chose de propre à Yamaku. Après tout, c'est un lycée comme un autre."


"Alors que nous continuons de parler, je me surprends à sourire. Miki et moi sommes différents, mais ça fait du bien de connaître un peu mieux une autre camarade de classe."

stop music fadeout 2.0

scene black
with dissolve



label fr_H13:

play music music_daily fadein 2.0
$ renpy.music.set_volume(0.4, 0.0, channel="ambient")
play ambient sfx_parkambience fadein 2.0

scene bg misc_sky
with locationchange


"Une légère brise amène l'odeur du petit matin à mon nez pendant que j’attends Lilly."


"Des petits nuages blancs parsèment le ciel, brisant le bleu monotone."


li "Hisao ? Tu es là ?"


"La voix de Lilly s'accorde avec la brise comme si elles étaient une seule et même chose."


"J’arrête de regarder le ciel et observe Lilly."

$ renpy.music.set_volume(0.8, 1.0, channel="ambient")

scene bg school_gate
show lilly cane_surprised_cas at center
with locationchange


"Avec un pull beige s’arrêtant au-dessous de l'épaule et une jupe qui descend jusqu'aux genoux, en plus de sandales beiges, elle est vraiment belle à voir."


hi "Ouais, je suis là, Lilly. Près du portail."


hi "Tu as réussi à semer Hanako ?"

show lilly cane_weaksmile_cas
with charachange


li "Oui. Ce n'est pas rare que je sorte durant les week-ends, alors je ne crois pas qu'elle soupçonne quoi que ce soit."

show lilly cane_sleepy_cas
with charachange


li "Ça, et... elle voit quelqu'un."


"Lilly plisse les lèvres, comme si elle n'aurait pas dû dire ça. Je trouve ça un peu difficile à croire."


hi "Hanako voit quelqu'un ? Vraiment ?"

show lilly cane_weaksmile_cas
with charachange


li "Non, c'est juste... elle voit un thérapeute des fois le week-end."


hi "Oh. D'accord. C'est logique."

show lilly cane_reminisce_cas
with charachange


"Lilly se frotte le bras, mal à l'aise, et vu son expression, je préfère changer de sujet."


hi "Euh..."

show lilly cane_surprised_cas
with charachange


li "Oui ?"


hi "Je me demandais... tu peux aller en ville seule ?"

show lilly cane_listen_cas
with charachange


"Lilly soupire devant mes interrogations concernant sa cécité. Je suis mon pire ennemi, parfois."


li "Je peux, oui. C'est plus facile quand je suis avec un ami ou avec ma sœur quand même."


"Je me demande comment Lilly s'entend avec sa sœur. Étant un enfant unique, c'est difficile d'imaginer ce que ça fait d'avoir une sœur, ça me rend même un peu envieux."


hi "D'accord. En tout cas, le bus arrive dans quelques minutes, on devrait sûrement se dépêcher."

show lilly cane_weaksmile_cas
with charachange


li "Oui. Il faudra attendre longtemps si on loupe celui-là."

stop music fadeout 6.0
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene bg school_road
with locationchange


"Sur ce, nous allons en direction de l’arrêt de bus sur la colline. Ce n'est pas loin du portail de l'école, alors c'est pratique."


hi "On a une jolie vue ici. Venant de la ville, je n'ai jamais vraiment vu d'horizon comme celui-ci, encore moins de manière quotidenne."

show lilly cane_smile_cas at center
with charaenter


li "C'est agréable ici pour moi aussi. C'est tranquille et loin des bruits et odeurs de la ville."

show lilly back_listen_cas
show lillyprop back_cane at center
with charachange


"La tête de Lilly se penche légèrement, signifiant qu'elle a entendu quelque chose."

show lilly back_smile_cas
with charachange


li "Oh, voilà le bus..."


"Je regarde en contrebas de la route et vois le bus monter la colline. Son ouïe est vraiment utile."


"Le bus s’arrête sous peu, et une minute plus tard nous sommes en chemin pour la ville."

stop ambient fadeout 2.0

scene bg city_street1
with shorttimeskip

play music music_ease fadein 2.0
$ renpy.music.set_volume(0.4, 0.0, channel="ambient")
play ambient sfx_traffic fadein 2.0


"Parcourant la ville, je me sens nostalgique. Les odeurs, le trafic, les grands bâtiments partout... Ça ressemble beaucoup à ma ville natale en dehors des passages piéton surélevés."


"C'est un peu bizarre, me balader naturellement dans une ville comme je le ferais dans un parc, mais avec des voitures autour de moi."


"Alors que je m'émerveille de l'ingéniosité des passages piéton surélevés, quelque chose me surprend."

show lilly cane_smileclosed_cas_close:
    center
    xpos 0.4
    easein 1.0 xpos 0.5
with charaenter


"Il me faut un moment pour réaliser que Lilly a passé son bras autour du mien et qu'elle tient sa canne de l'autre."


"Pendant un moment je suis surpris, mais j'arrive à garder mon calme pour que Lilly ne le remarque pas. Bien que ce ne soit pas la première fois que Lilly se sert de moi pour se guider, elle se contentait de tenir ma manche jusqu'ici."


"Il est logique qu'il soit plus facile pour elle de naviguer dans une zone complexe et peuplée en étant accroché à quelqu'un, mais je ne suis pas autant habitué à ce genre de contact qu'elle."


"Réalisant finalement qu'un silence s'installe entre nous et que Lilly attend que je fasse un pas, je mets rapidement mon cerveau en marche."


hi "Tu sais, j'étais surpris d'apprendre que Hanako aime chanter. Tu l'as déjà entendue ?"

show lilly cane_smile_cas_close at center
with charachange


li "Oui. Nous sommes allées au karaoké quelques fois, il y avait Akira aussi. Je ne peux pas dire que j'aime beaucoup ça, mais elles deux, si."


"Peut-être que le karaoke convient mieux à Hanako que ce que je pensais. Juste elle et ceux qu'elle connaît, seuls dans une petite pièce."


"Ça lui donnerait une rare chance de baisser sa garde, avec personne d'autre pour la juger."


hi "Peut-être que fêter son anniversaire dans un karaoke serait une bonne idée, non ?"

show lilly cane_sleepy_cas_close
with charachange


li "Mmh. Je ne suis pas sûre qu'elle serait très bien avec toute cette agitation."


"Je suis sur le point de protester, mais son visage montre qu'elle a encore quelque chose à dire. Il lui faut un moment pour formuler sa phrase."

show lilly cane_weaksmile_cas_close
with charachange


li "Encore une fois, la meilleure chose que nous puissions faire pour Hanako est d'essayer de lui créer des bons souvenirs d'anniversaire. La traiter continuellement comme si elle était anormale n'aiderait pas."


hi "Je crois que tu as raison. Si elle peut garder des souvenirs, autres que ceux de son triste passé, alors elle ira peut-être mieux."


"Si on lui achetait quelque chose de bien, qu'elle puisse voir tous les jours, alors peut-être qu'elle sera capable de penser à autre chose qu'à son passé et qu'elle se rappellera qu'elle a des amis."


"Et dans tous les cas, je crois que Hanako peut gérer ça. Avec le temps que j'ai passé avec elle, j'ai appris qu'elle n'était pas aussi fragile qu'on peut le penser au premier abord."


hi "Bon, on y va ? Je ne sais pas vraiment où commencer à chercher, cela dit."

show lilly cane_smileclosed_cas_close
with charachange

stop music fadeout 6.0


li "Oui. Je suggérerais qu'on prenne quelque chose à manger, d'abord."


hi "Je n'ai pas mangé non plus, bonne idée."

show lilly cane_cheerful_cas_close
with charachange


li "Assure-toi de choisir un bon endroit, Hisao."


"Elle m'adresse un sourire moqueur, un de ceux qui me font sourire par réflexe même si elle ne peut pas le voir."


hi "Je vais m'en assurer, ne t’inquiète pas."

stop ambient fadeout 1.0
play music music_another fadein 4.0
scene bg city_karaokeint
with locationskip


"Une fois à l'intérieur, je commande deux parts de tarte avec deux tasses de thé et les apporte à notre table."

show lilly basic_smileclosed_cas_close:
    center
    ypos 1.1
with charaenter


"J'ai choisi ce café parce qu'il devrait convenir à Lilly, petit et silencieux, mais quelque peu classe. À en juger par le léger sourire qu'elle affiche, je... ne suis pas vraiment sûr d'avoir bien fait."


"Il est très, très rare de ne pas la voir sourire, après tout."


"Néanmoins, je prends place à côté d'elle à une des tables en coin et pose nos modestes repas."

show lilly basic_planned_cas_close
with charachange


"Lilly place sa tête au-dessus de la part de tarte et la sent délicatement."

show lilly basic_cheerful_cas_close
with charachange


li "Tarte au citron, n'est-ce pas ? Merci, Hisao."


hi "Pas de problème. Le thé est juste à côté de toi, fais attention à ne pas le faire tomber."

show lilly basic_weaksmile_cas_close
with charachange


"Elle hoche la tête, mais à en juger par le sourire un peu faible qu'elle esquisse, l'avertissement n'était pas nécessaire. J'imagine que le son l'a informée de la position de la tasse."


"Nous entamons notre repas, en restant silencieux pendant tout ce temps. Lilly n'est pas du genre à discuter pendant qu'elle mange, et moi non plus."


"Finalement nous arrivons à la fin de nos repas et notre tasse de thé se vide peu après. Lilly est la première à rompre le silence."

show lilly basic_smile_cas_close
with charachange


li "C'était très bon. Je dois dire que tu as bien choisi, Hisao."


hi "C'est la première fois que je viens ici, alors tout ce que je pouvais faire, c'était regarder pour trouver un endroit qui semblait bien."


hi "Euh... zut. Désolé."


"Je me sens vraiment mal d'évoquer ce sujet avec Lilly, mais elle ne semble pas s'en préoccuper plus que ça. C'est tout l'inverse même, elle semble presque amusée par mon embarras."

show lilly basic_smileclosed_cas_close
with charachange


li "Tu es consciencieux, Hisao, mais des fois j'ai peur que ça ne se retourne contre toi. Tu n'as pas besoin de changer ta façon de parler pour moi."


"Lilly ne s'embête vraiment pas avec son handicap. Je me dépêche quand même de changer de sujet, je ne peux pas vraiment dire que je partage ce confort."


hi "Tu vis ici depuis longtemps ? On dirait que tu connais plutôt bien les environs."

show lilly basic_planned_cas_close
with charachange


"Elle secoue la main devant son visage pour infirmer mes propos."

show lilly basic_smile_cas_close
with charachange


li "Non, rien de tout ça. Je suis à Yamaku depuis le début du lycée, mais je ne suis pas allée souvent en ville parce qu'Akira, ma sœur, m'amenait et me ramenait."


hi "Oh, oui. Tu as mentionné que tu ne vivais dans les dortoirs que depuis récemment."


"C'est étonnant, j'aurais pensé qu'elle vivait ici depuis qu'elle était arrivée à Yamaku, ce qui fait qu'elle aurait déjà vécu quelques années ici."

show lilly basic_smileclosed_cas_close
with charachange


li "J'ai vécu avec ma famille pendant toute mon enfance, et puis après j'étais juste avec ma sœur. Ma famille ayant déménagé à Inverness et Akira travaillant beaucoup, j'ai fini par emménager à Yamaku."


hi "Inverness ? Ce n'est pas en Écosse ça ?"

show lilly basic_surprised_cas_close
with charachange


li "Oh, je ne te l'ai pas dit ? Ma famille vit en Écosse, le lieu de naissance de ma mère. Mon père est japonais, cependant."


"Oh. Je m'étais déjà demandé d’où venait l'apparence de Lilly, mais je n'avais jamais pris la peine de poser la question. C'est donc ça."


hi "Pour être honnête, je n'aurais jamais deviné. Vu que tu n'as pas d'accent, j'imagine que tu es née ici ?"

show lilly basic_giggle_cas_close
with charachange


li "Exact. Je suis contente de mon héritage cela dit, grâce auquel j'ai appris l'anglais dès ma toute petite enfance."

show lilly basic_smile_cas_close
with charachange


li "Et toi, Hisao ?"


hi "Quoi moi ?"


"Elle réfléchit un moment. Elle aurait sûrement dû penser à quelle question poser avant de changer de sujet."

show lilly basic_weaksmile_cas_close
with charachange


li "Je voulais dire... quels sont tes plans pour le futur ?"


hi "Pour être honnête, je n'y ai pensé que récemment."


hi "Après mon accident et mes mois à l’hôpital, apprécier la vie ici avec Hanako et toi m'a suffit."


"En fait, je n'ai pas pensé à un “futur” depuis bien longtemps. Ça semble presque futile."

show lilly basic_sleepy_cas_close
with charachange


li "C'est ta dernière année à l'école. Après ça, tu devras te débrouiller d'une manière ou d'une autre."


hi "Ce n'est pas comme si je ne savais pas ça, je n'y ai juste pas beaucoup pensé depuis..."

show lilly basic_weaksmile_cas_close
with charachange


"Elle ouvre la bouche pour continuer, mais laisse échapper un petit soupir à la place. Elle semble avoir réalisé qu'elle ne me connaît pas assez pour approfondir la conversation."


li "Eh bien, on a tous notre rythme. J’espère juste que tu saisiras ta chance quand tu en auras l'occasion."


hi "...Bien sûr. J'y réfléchirai."

stop music fadeout 2.0

$ renpy.music.set_volume(0.4, 0.0, channel="ambient")
play ambient sfx_traffic fadein 2.0

scene bg city_street2
show lilly cane_smileclosed_cas_close
with shorttimeskip


"Alors que nous sortons du café, Lilly repasse son bras autour du mien."

show lilly cane_smile_cas_close
with charachange


li "Donc, tu as une idée de cadeau ?"


hi "Pour être honnête, non. Je n'ai jamais été bon pour ça."

show lilly cane_weaksmile_cas_close
with charachange


li "Aussi bête que ça puisse avoir l'air, peut-être qu'on devrait juste... jeter un œil aux alentours ?"


"Entendre Lilly prononcer ces mots me choque pendant une seconde."


hi "Euh... ok. Comment veux-tu qu'on fasse ça ?"

show lilly cane_cheerful_cas_close
with charachange


li "C'était la réaction que j'attendais. C'est simple, on passe devant les magasins et tu me dis ce qu'ils contiennent."

show lilly cane_smileclosed_cas_close
with charachange


li "Ça nous donnera des idées."


hi "D'accord... Je n'en suis pas vraiment sûr, mais je vais te faire confiance."

show lilly cane_smile_cas_close
with charachange


li "Je crois que ça ira. Hanako, ma sœur et moi avons bien réussi à le faire."

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")

scene bg city_street3
with locationskip


"Sur la phrase optimiste de Lilly, nous rentrons dans le quartier commerçant de la ville et je commence à décrire ce que je vois à Lilly."


"C'est difficile d'imaginer Hanako faire les boutiques. Elle ne semble pas être le genre de personne à aimer la mode et je ne l'ai jamais vue lire des magazines sur le sujet. En fait, en terme de hobby, je ne l'ai vue que lire des livres."


hi "Il y a un magasin d'articles ménagers juste devant. On dirait que c'est surtout de la vaisselle."

show lilly cane_sleepy_cas_close at center
with charaenter


li "Je ne crois pas qu'elle ait vraiment besoin de ça ; et quel type de message ça lui enverrait ?"


hi "Euh... “cuisine plus” ? Ce n'est peut-être pas une si mauvaise idée..."

show lilly cane_weaksmile_cas_close
with charachange


li "Des fois, il est mieux de laisser les choses telles qu'elles sont, Hisao."


"Encore une fois, j'ai le sentiment que les expériences de Hanako en cuisine ne sont pas toujours un succès. Lilly a sûrement dû l'aider quelques fois."


hi "Voyons voir, à côté il y a une librairie... ça semble être une bonne idée, elle aime beaucoup lire."

show lilly cane_concerned_cas_close
with charachange


li "Oui, mais il y a un problème avec les livres. Je ne sais pas vraiment ce qu'elle a lu ou pas lu."


hi "Et une carte cadeau ?"

show lilly cane_listen_cas_close
with charachange


li "Il n'y a rien de plus impersonnel qu'une carte cadeau. C'est comme dire “Je ne te connais pas assez pour savoir ce que tu aimerais avoir.”"


hi "J'ai toujours pensé que c'était une bonne façon pour que la personne ait ce qu'elle veut."

show lilly cane_displeased_cas_close
with charachange


li "Offrir des cadeaux aux gens est supposé leur montrer le niveau d'affection que tu as pour eux. Si tu ne peux pas décider d'un cadeau pour eux, alors est-ce que tu tiens vraiment à eux ?"


hi "D'accord, d'accord, pas de carte cadeau."


"Lilly semble vraiment impliquée, mais je comprends ce qu'elle veut dire. Si tu vas acheter quelque chose pour quelqu'un, alors tu dois au moins y réfléchir un peu."


"Si je veux prendre quelque chose pour Hanako qui lui rappelle ses amis, alors que vaut une bête carte cadeau ?"


hi "Qu'est-ce que tu lui as acheté l’année dernière ?"

show lilly cane_smile_cas_close
with charachange


li "Une poupée en porcelaine. Je pensais que si elle avait quelqu'un à qui parler, ça la soulagerait un peu."

show lilly cane_weaksmile_cas_close
with charachange


li "Une poupée ne va pas la critiquer, après tout."


hi "Alors je devrais chercher un magasin de poupées ?"

show lilly cane_smileclosed_cas_close
with charachange


li "Si tu le veux bien, j'apprécierais."


hi "Ça me va. Bien que j'aurais aimé que tu le mentionnes plus tôt."

show lilly cane_cheerful_cas_close
with charachange


li "Mais si j'avais fait ça, tu n'aurais pas réfléchi par toi-même, n'est-ce pas ?"


"Encore une fois, Lilly a raison. J'analyse chaque magasin que je vois. Si Lilly avait mentionné une boutique de poupées, je n'aurais pas pensé à autre chose."

$ renpy.music.set_volume(0.4, 1.0, channel="ambient")

scene bg city_street4
with locationskip


"Nous errons dans les rues de la ville, mais je n'arrive pas à trouver quelque chose qui ressemble à un magasin de poupées ou quoi que ce soit qui pourrait être un bon cadeau."


"Le simple fait de chercher m'aide à me vider la tête. Les événements de la semaine dernière commencent à s'effacer et j'ai hâte de donner son cadeau à Hanako..."


"...si j'arrive à en trouver un."


hi "C'est sans espoir. Je pensais qu'on arriverait à trouver quelque chose en ville. Et je suis sûr qu'on est déjà passés dans cette rue."

show lilly cane_oops_cas_close at center
with charaenter


li "On dirait que tu es sur le point d'abandonner, Hisao."


hi "Non, mais c'est beaucoup plus dur que ce que je croyais."

show lilly cane_smileclosed_cas_close
with charachange


li "Essaye de ne pas être si négatif. Peut-être qu'on devrait aller dans quelques magasins et voir ce qu'il y a ?"


hi "Bonne idée. Il n'y a généralement pas grand-chose d’intéressant dans les vitrines."

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")

scene bg city_street3 at right
with locationskip


"Lilly et moi reparcourons les rues une fois de plus, cette fois en rentrant dans les magasins qui attirent notre attention. En fin de compte, rien ne semble être vraiment bien."


"Les goûts de Hanako sont difficiles à cerner à cause de sa nature réservée, et les goûts qu'on lui connaît ne nous aident pas vraiment."

show lilly cane_sleepy_cas_close at center
with charaenter


li "On peut faire une petite pause ? Je suis un peu fatiguée."

show lilly cane_sleepy_cas_close:
    ypos 1.05
with charamove

show bg city_street3 at left
show lilly invis:
    xpos 0.8
    ypos 1.05
with dissolvecharamove


"J'approuve, et je m’arrête pour que Lilly se repose contre une rambarde pendant que je vais chercher des boissons à un distributeur."


"Après avoir marché jusqu'au distributeur et m’être pris de la limonade, je me trouve quelque peu perdu. Ne connaissant pas les goûts de Lilly, je décide de prendre quelque chose qui sonne un peu fille, mais pas trop bizarre : un lait à la fraise."

show bg city_street3 at right
show lilly cane_weaksmile_cas_close:
    center
    ypos 1.05
with dissolvecharamove


hi "Je suis là."


"Je la rejoins et place la brique dans sa main tendue, m'assurant qu'elle la tient vraiment avant de lâcher."

show lilly cane_smile_cas_close
with charachange


"Elle passe ses doigts autour avant de l'ouvrir et de prendre une petite gorgée, son sourire me confirmant que j'ai fait le bon choix. Nous restons là quelques minutes à boire en silence."

$ renpy.music.set_volume(0.2, 0.0, channel="sound")
play sound sfx_phone

show lilly cane_surprised_cas_close
with charachange


"Une sonnerie familière provient de la poche de Lilly. Elle s'excuse rapidement et met une main dans sa poche, en sortant son téléphone."

show lilly cane_weaksmile_cas_close
with charachange


li "Ça te gêne si je prends l'appel?"


hi "Non, vas-y."

show lilly back_listen_cas_close
show lillyprop back_cane_close:
    center
    ypos 1.05
with charachange


"Elle hoche la tête en remerciement avant de se tourner et d'ouvrir son téléphone, l'amenant à son oreille."

show lilly back_smile_cas_close
with charachange


"À en juger par le ton de Lilly, la personne de l'autre côté du fil est sans doute un ami. Je n'écoute pas longtemps, vu que la discussion de Lilly semble être plus que de simples potins."


"Sans avoir grand-chose d'autre à faire, je regarde Lilly. C'est vraiment une jolie fille, ce qui doit sans doute l'aider dans sa popularité à l'école. C'est intéressant de voir le contraste entre Hanako et Lilly, que ce soit dans leur personnalité ou leur apparence."

show lilly back_smileclosed_cas_close
with charachange


"Pendant quelques minutes, je bois juste, en la regardant. Peu de temps après, Lilly dit au revoir à la personne à qui elle parlait et raccroche, replaçant son téléphone dans la poche et s'adossant à la rambarde comme avant."

hide lillyprop
show lilly cane_weaksmile_cas_close
with charachange


li "Désolée, juste un ami de classe."

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_can_clatter


"Je prends une dernière gorgée avant de jeter ma canette. Lilly me donne la brique pour la jeter aussi, l'ayant finie plutôt rapidement."

$ renpy.music.set_volume(0.1, 2.0, channel="ambient")


hi "Tu sembles avoir beaucoup d'amis."

show lilly cane_smile_cas_close
with charachange


li "Oh ?"


"Lilly attend que je continue, apparemment intéressée par mon avis."


hi "Je me disais juste que vous êtes vraiment différentes, Hanako et toi. C'est difficile d'imaginer Hanako faire les mêmes choses que toi, ou connaître autant de monde."

show lilly cane_giggle_cas_close
with charachange


li "Tu sembles penser beaucoup à Hanako."


hi "Je sais pas. C'est juste... qu'elle est mystérieuse, j'imagine. Je veux la connaître plus, mais ce n'est pas facile."

show lilly cane_weaksmile_cas_close
with charachange


li "On dirait presque que tu doutes de ta relation avec elle."


hi "Ce n'est pas ça. Je veux juste faire plus pour elle, être son ami et tout. Je ne sais même pas comment elle me voit vraiment."

show lilly cane_smile_cas_close
with charachange


"Cette remarque semble intéresser Lilly. Je me demande si Hanako a dit quelque chose à Lilly à mon propos."

show lilly cane_smileclosed_cas_close at center
with dissolvecharamove


"Je suis sur le point de demander à quoi elle pense quand elle se redresse."

show lilly cane_cheerful_cas_close
with charachange


li "On y va ?"


"Sa voix et son expression montrent qu'elle joue avec moi. Lilly sait très bien qu'elle me laisse dans l'attente."


"Avec un soupir, je me relève aussi de la rambarde et regarde autour de moi. On a des trucs à faire, j'essayerai juste de lui en reparler plus tard."


"Coincé entre une épicerie et un kiosque, se trouve un petit magasin. Le signe au-dessus de la porte dit “Othello's Antiques” en lettres décoratives anglaises."


"Il serait facile de le louper si on marchait dans la rue, mais vu que je regarde, immobile, les environs, je le remarque."

$ renpy.music.set_volume(0.3, 6.0, channel="ambient")


hi "Dis, Lilly... la poupée que tu as achetée à Hanako, elle était neuve ?"

show lilly cane_smile_cas_close
with charachange


li "Euh, oui, mais je ne suis pas sûre de comprendre où tu veux en venir."


hi "Je crois qu'on a trouvé notre magasin. Il est de l'autre côté de la rue."

show lilly cane_surprised_cas_close
with charachange


li "Oh ? Qu'est-ce que c'est ? Une sorte de magasin de jouets ?"


hi "C'est un magasin d'antiquités. Je crois que c'est notre meilleure chance."

show lilly cane_satisfied_cas_close
with charachange


li "Vraiment ? Je ne savais pas qu'il y en avait un ici."


hi "Moi non plus, je l'ai loupé la première fois qu'on est passés. Il est plutôt bien caché."

show lilly cane_smileclosed_cas_close
with charachange


li "En tout cas, ça ne coûte rien de jeter un coup d’œil."


"Contents de cette trouvaille, nous nous dirigeons rapidement vers le magasin, la main de Lilly accrochée à mon coude pour se guider."

stop ambient fadeout 0.5

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_storebell
play music music_soothing fadein 0.5
$ renpy.music.set_volume(1.0, 4.0, channel="ambient")

scene bg city_othello at right
with locationchange


"Le magasin a une étrange odeur musquée. L’intérieur ressemble plus à un garage qu'à un magasin. Les choses sont éparpillées sur le sol sans réelle organisation."

show shopkeep neutral at center
with charaenter


"Le gérant nous adresse un regard ennuyé de ses yeux particulièrement petits. Son visage semble las et fatigué et son style vestimentaire est vraiment anachronique. Il nous adresse un hochement poli de bienvenue avant de retourner à son livre."

hide shopkeep
with charaexit


"Lilly s'accroche fermement à mon bras et je me retrouve à devoir faire attention à ne pas manquer un potentiel cadeau pour Hanako et m'assurer que Lilly ne se cogne pas."

show bg city_othello at center
with charamove_slow


"C'est plutôt difficile, étant donné l'agencement du magasin et les objets dépassant des étagères, mais finalement nous arrivons sains et saufs à un vieux bureau couvert de poupées et d'ours en peluche."


hi "Je crois que c'est bon. Il y a des poupées de tous les genres ici."

show lilly cane_smileclosed_cas_close at center
with charaenter


li "Ça va simplifier les choses. Tu peux en prendre une pour moi, Hisao ?"


"J'avais le sentiment que ça allait finir comme ça. J'imagine Hanako dans ma tête et essaye de deviner laquelle de ces poupées pourrait lui correspondre le mieux."


"Mes yeux parcourent la collection. Chacune est plus belle que la précédente. Il y a beaucoup de styles différents, mais finalement une se démarque des autres."


hi "Voilà, et pourquoi pas celle-ci ?"




"Je prends une petite poupée en porcelaine qui n'a pas l'air trop chère. Habillée d'une robe verte de l'époque victorienne avec un petit chapeau marron sur ses cheveux blonds, elle ressemble un peu à Lilly."

show lilly cane_listen_cas_close
with charachange




"Je lui tends doucement et elle passe délicatement ses doigts autour de l'objet en ayant l'air très concentrée."

show lilly cane_smile_cas_close
with charachange


li "Elle a l'air très jolie. Tu crois que ça conviendra à Hanako ?"


hi "Je pense, oui. Ça irait bien dans sa chambre."

show lilly cane_smileclosed_cas_close
with charachange


li "Dans ce cas, je te fais confiance. Tu lui prends quelque chose aussi, ou ce sera un cadeau de nous deux ?"


hi "Mmh, je ne sais pas trop. Je crois que je devrais lui prendre quelque chose, mais je ne pense pas qu'une autre poupée soit une super idée. Peut-être..."


"Ma voix s'éteint alors que je parcours le magasin du regard. Posée sur une table pas loin de nous se trouve une boîte qui attire mon regard."


hi "Attends ici, je crois que j'ai trouvé quelque chose..."

show lilly cane_ara_cas_close
with charachange


li "Eh bien, eh bien, c'était rapide."




"Je marche avec précaution à côté d'une collection d'objets en cristal et ramasse la boîte. Les côtés en bois sont couverts de gravures représentant d'anciens combats autour d'un château."


"Le dessus, néanmoins, semble très familier. Alternant des carrés en bois verni blanc et noir."


sk "C'est un très bel objet. Un jeu d'échecs importé d'outre-mer."



show bg city_othello at bgleft
show lilly cane_smileclosed_cas_close at twoleft
with dissolvecharamove

show shopkeep neutral at tworight
with charaenter


"L'apparition soudaine du vendeur me surprend un peu. Je ne l'ai pas du tout vu s'approcher."


"J'imagine qu'il essaye d'aider parce qu'on n'a pas l'air de savoir ce qu'on cherche. ...Ou d'un autre côté, peut-être qu'il essaye de garder un œil sur nous parce qu'il pense qu'on pourrait commettre un vol à l’étalage."


hi "Je... cherche un cadeau pour une amie."

show shopkeep happy
with charachange


sk "Je vois. Dans ce cas, ce jeu d’échecs est un bon choix."


"Je réalise quelque chose. L'échiquier est plutôt beau, mais c'est un magasin d'antiquités. Ils ne sont pas connus pour leurs prix bon marché."


hi "Il date de quelle année ?"

show shopkeep neutral
with charachange


sk "C'est une reproduction. Je dirais qu'il a été fait il y a cinq ans."


hi "Je vois. Il coûte combien ?"

show shopkeep thinking
with charachange


"Il réfléchit un peu avant de me répondre, ce qui me perturbe un peu."

show shopkeep neutral
with charachange


sk "Je te le fais à 7000 yen."


"Je fais une grimace. Je ne m'attendais pas à dépenser autant, mais le cadeau semble parfait. Encore une fois, peut-être qu'il me teste pour voir combien il peut me faire payer."


hi "Vous ne pouvez pas me le faire à 5000 ?"

show shopkeep thinking
with charachange


sk "5500, pas mieux."


hi "Ça me va. Oh, et on voudrait aussi prendre cette poupée..."

show shopkeep neutral
with charachange


"Le gérant regarde derrière moi et voit Lilly avec la poupée dans les mains. Il plisse les yeux et met visiblement un moment à s'accommoder."


"En même temps, son sourire s'efface légèrement."


sk "Ah..."


"J'imagine que ça veut dire que tout n'est pas une reproduction dans son magasin."

show shopkeep thinking
with charachange


sk "Es-tu sûre de vouloir cette poupée, jeune fille ?"

show lilly cane_smile_cas_close
with charachange


li "J'ai confiance dans le jugement de mon ami."

show shopkeep surprised
with charachange


sk "Je vois... oh, pardon..."

show lilly cane_smileclosed_cas_close
with charachange


li "Pas de problème. Si vous pouvez me l'emballer dans du papier cadeau, j’apprécierais."

show shopkeep neutral
with charachange


sk "Oui, bien sûr, mais c'est 20000 yen..."


"Lilly fouille dans son sac et sort quatre billets chiffonnés de 5000 yen."

show lilly cane_cheerful_cas_close
with charachange


li "Voilà, 20000 yen."

show shopkeep thinking
with charachange


"Le vendeur prend les billets et la poupée et va jusqu'au comptoir. Je prends le bras de Lilly pour la guider jusque-là."


hi "Tu es sûre ?"

show lilly cane_smileclosed_cas_close
with charachange


li "Ce n'est pas un problème. J'ai... de quoi payer. Comme je l'ai dit, j'ai confiance en ton jugement."


"Je me sens un peu coupable sur deux points, déjà parce que Lilly dépense beaucoup d'argent à cause de ma recommandation et aussi parce que mon cadeau ne vaut pas suffisamment en comparaison."


"Cela dit, Lilly semble toujours être quelque peu gênée quand ça parle d'argent..."

show shopkeep neutral
with charachange


"Je tends l'échiquier au vendeur avec l'argent. Il met l'argent dans la caisse avant d'emballer la poupée puis l'échiquier."


"Finalement, il finit de mettre le papier cadeau et nous tend nos achats."

show shopkeep happy
with charachange


sk "Soyez prudents au retour et n'hésitez pas à revenir."


hi "Merci."

show lilly cane_smile_cas_close
with charachange


li "Oui, merci beaucoup."


"Le gérant se penche pour nous saluer alors que nous partons."

stop music fadeout 6.0
$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_traffic fadein 1.0

scene bg city_street3
with locationchange

show lilly cane_weaksmile_cas_close at center
with charaenter


li "Bon, ça nous a pris toute la journée, mais nous avons trouvé ce que nous cherchions."


hi "En effet."


"Maintenant que les cadeaux sont emballés, je suis impatient de les donner à Hanako. C'est une réaction normale après avoir acheté des cadeaux, de vouloir voir la réaction de la personne quand elle découvre ce que c'est."


"Et j'ai aussi envie de voir Hanako, juste pour m'assurer qu'elle va bien."


hi "On rentre ?"

show lilly cane_smile_cas_close
with charachange


li "Oui, on a beaucoup marché aujourd'hui, je ne me plaindrai pas quand je serai arrivée au dortoir."


"Lilly a raison. Maintenant que je n'ai plus besoin de trouver un magasin, mes jambes sont plutôt fatiguées."


hi "Bon, retour à l'école. J'ai bien envie de me reposer aussi."


"Lilly tend son bras et attrape le mien. Ensemble, nous marchons en direction de l’arrêt de bus."

stop ambient fadeout 2.0

scene black
with dissolve



label fr_H14:

play music music_pearly fadein 5.0

scene bg school_scienceroom at right
with locationchange


"Mutou nous lit des équations et des formules une par une de son ton monotone, comme à son habitude."


"Il est possible qu'il aime vraiment ce qu'il nous apprend, des fois il affiche une étincelle de passion, comme s'il l'apprenait lui-même."


"Mais la plupart des fois c'est juste comme ça, ce qu'on étudie est plutôt simple, donc j'ai du mal à rester concentré sur ce qu'il dit. Et en plus de ça mes jambes me font mal, ce qui rend les choses encore plus difficiles."


"Je commence presque à regretter d'avoir parcouru la ville hier avec Lilly."


"Depuis que j'ai quitté l’hôpital, j'ai fait très peu d'exercice physique. Marcher jusqu’à l'épicerie ne compte pas vraiment. Malgré les tentatives d'Emi quand je suis arrivé à Yamaku, j'ai abandonné l'espoir de regagner mon ancienne forme physique."


"Je suis sûr qu'avoir marché en ville pendant des heures m'a enflammé les muscles des jambes. C'est déprimant et ça me rappelle une autre chose que je ne peux plus faire depuis que j'ai eu ma crise cardiaque. Je me sens pathétique."

show muto normal at twoleft
with charaenter


mu "Maintenant... Ikezawa ?"

show hanako defarms_shock at tworight
with vpunch


"C'est étrange de la part de Mutou de poser une question à Hanako, mais ce n'est pas la première fois. Elle se lève d'un bond, un peu surprise, et le fixe."


"Elle sait qu'il est rare que Mutou l'appelle, alors tous les yeux de la classe vont être sur elle. De cette façon, elle ne prend pas le risque de croiser le regard des autres."

show hanako def_worry
with charachange


ha "O-oui ?"


mu "Dans cet exemple particulier de réaction d'oxydo-réduction, la réaction de la combustion du méthane produit un autre élément qui n'est pas listé. Cet élément est... ?"

show hanako emb_downtimid
with charachange


"Même si c'est une question facile, elle attend timidement un moment avant de répondre, se mordant légèrement la lèvre inférieure comme pour rester concentrée."

show hanako emb_timid
with charachange


ha "Euh... la c-chaleur ?"

show muto smile
with charachange


mu "Correct. C'est une réaction exothermique et la réaction produit plus de chaleur."

show hanako invis:
    ypos 1.1
with dissolvecharamove

hide hanako
with None


"Après un hochement de tête de Mutou, Hanako se rassoit et pousse un soupir de soulagement."


"Un début difficile, mais c'est au moins quelque chose."


"Ce serait bien de la faire sortir pour son anniversaire, quelque part ailleurs que sa chambre ou la salle où on boit le thé. Avec les progrès qu'elle a faits jusqu’à maintenant, je ne crois pas qu'elle aurait tant de mal à aller en ville."

show muto smile at center
show bg school_scienceroom at center
with charamove


mu "Bien. Pour le reste du cours, mettez-vous en groupes de trois ou quatre et faites les problèmes du chapitre 12. Je serai là si vous avez besoin d'aide."

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 8.0

show muto invis:
    ypos 1.1
with dissolvecharamove

hide muto
with None


"Mutou s'assoit derrière son bureau, sort quelques feuilles d'une chemise et commence à travailler dessus. Je croyais que les professeurs étaient censés faire ce genre de choses après les cours, pas pendant."

show shizu invis_close:
    tworight
    xpos 0.8
show misha invis_close:
    twoleft
    xpos 0.2
with None

show shizu behind_blank_close at tworight
show misha hips_smile_close at twoleft
with dissolvecharamove


"Je regarde à ma droite pour trouver quelqu'un avec qui former un groupe. Étant donné les deux visages souriants se dirigeant vers moi, je ne crois pas que j'aurai beaucoup à chercher."


hi "J'imagine qu'on a un groupe de fait."

show misha hips_grin_close
with charachange


mi "Hicchan~ ! Tu veux qu'on travaille ensemble ? Ok, ok~ ! C'est super ! Ça fait vraiment longtemps~ !"

show shizu behind_blank_close:
    ypos 1.09
show misha hips_smile_close:
    ypos 1.09
with dissolvecharamove


"La classe commence à déplacer bruyamment les bureaux, Shizune fait de même en mettant le sien devant le mien. Elle a de la chance de ne pas entendre le bazar que tout cela provoque, c'est assez bruyant pour me gêner."


"Pour dire vrai, travailler avec Shizune et Misha est sûrement un bon parti - Shizune et moi sommes plutôt bons dans cette matière et Misha... a une jolie écriture."

show hanako silhouette behind shizu at center
with charaenter


"Alors que je regarde Misha, je remarque quelqu'un derrière elle. L'ombre attire l'attention de Misha qui se tourne vers la personne aux cheveux sombres."

show shizu behind_blank_close at Position(xpos=0.8)
show misha perky_smile_close at Position(xpos=0.2)
show hanako basic_worry
with dissolvecharamove


mi "Bonjour, Hanako~ !"

show hanako emb_timid
with charachange


ha "Hum... bonjour..."


"Shizune remarque enfin Hanako après avoir suivi le regard de Misha. Rapidement, elle tapote l'épaule de Misha pour avoir son attention avant de lui faire des signes."

show shizu adjust_happy_close
with charachange

shi "…"

show misha sign_smile_close
with charachange


mi "Shicchan dit que si tu cherches un groupe, tu peux rejoindre le nôtre~ !"

show hanako emb_downsmile
with charachange


"Hanako baisse les yeux et rougit un peu. De tous les gens de la classe, nous sommes ceux que Hanako connaît le mieux, alors il est normal qu'elle vienne vers nous en premier."


"Encore une fois, qu'elle aille vers un groupe dans l'intention de le rejoindre est quelque chose qu'elle a apparemment très rarement fait auparavant."

hide hanako
with charaexit

show shizu behind_smile_close:
    tworight
    ypos 1.09
show misha hips_smile_close:
    twoleft
    ypos 1.09
with dissolvecharamove


"Elle part pour apporter son bureau jusqu'ici, Shizune et Misha se retournent vers moi à la seconde où elle a le dos tourné."

show shizu adjust_happy_close
with charachange

shi "…"

show misha perky_smile_close
with charachange


mi "Il semblerait qu'on rejoue encore ensemble, Hicchan~ ! Tu ne joues presque plus avec nous maintenant..."


hi "Je me demande pourquoi ? Vous semblez toujours avoir un but caché."

show shizu basic_frown_close
with charachange

shi "…"

show misha hips_frown_close
with charachange


mi "C'est méchant, Hicchan... C'est presque comme si tu m'insultais~ !"

show misha hips_grin_close
with charachange


mi "Mais~ ! C'est Hicchan, alors je sais que tu rigoles !"


hi "Tu as un si grand sens de l'humour ; ce serait horrible si quelqu'un profitait de ta bonne nature. Comme en t'obligeant à les aider dans leur travail."

show shizu adjust_smug_close
with charachange

shi "…"

show misha cross_laugh_close
with charachange


mi "Wahaha~ !"


"Shizune semble excitée pendant une seconde, un peu surprise que je veuille la défier, mais quand elle voit Hanako revenir, elle reprend son sourire normal. J'imagine que la guerre psychologique est finie pour l'instant."

show hanako invis_close behind shizu at center
with None

show shizu behind_blank_close at Position(xpos=0.85)
show misha perky_smile_close at Position(xpos=0.15)
show hanako emb_downtimid_close at Position(ypos=1.09)
with dissolvecharamove


"Hanako colle son bureau à celui de Misha. Elle a les yeux baissés et je me demande pourquoi, jusqu’à ce que je regarde la classe."


"La plupart des élèves sont occupés avec leur propre groupe, mais quelques-uns lui jettent un regard curieux. À cette distance, il est difficile de savoir si c'est un simple regard ou s'ils parlent d'elle."


"C'est étrange. Personne n'est étonné quand Hanako sort de classe pour éviter un travail de groupe, mais maintenant qu'elle fait un effort, ils la regardent tous comme si elle avait fait quelque chose de mal."


"Nous étalons nos livres et cahiers sur les quatre tables collées. Il ne faut pas longtemps pour que la classe entière se mette au travail."

show misha sign_smile_close
with charachange


mi "Salut, Hanako~ ! Ça fait plaisir d'enfin travailler avec toi~."

show hanako basic_distant_close
with charachange


ha "O-ouais."

show shizu adjust_smug_close
with charachange

shi "…"

show misha hips_grin_close
with charachange


mi "C'est à cause de toi que Hicchan nous évite récemment~ ? Shicchan dit que c'est pas très gentil, mais si Hicchan veut passer du temps avec une jolie fille, c'est compréhensible~ !"

show hanako cover_worry_close
with charachange


ha "J-je ne crois p-pas que ce soit ça..."


"Hanako commence à gigoter, mal à l'aise à cause de l'attention qui lui est accordée."


"Je crois qu'une personne normale aurait abandonné la conversation, mais Misha est l'opposée de Hanako. Ce qui signifie qu'elle est complètement aveugle face aux normes sociales alors que Hanako en est bien trop consciente."


"À cause de ça, Misha la mitraille de questions, trop rapidement pour que je puisse avoir une chance de diriger la discussion vers un sujet plus confortable."

stop music fadeout 7.0

show misha hips_smile_close
with charachange


mi "Vraiment~ ? Alors~ ! Il n'était pas avec toi hier ?"

show hanako emb_downsad_close
with charachange


ha "N... non..."


"Je peux sentir ma couverture s'amincir. Lilly ne veut pas que Hanako sache qu'on lui achetait des cadeaux hier, ni qu'on lui prépare une fête d'anniversaire. Il ne faudrait pas qu'elle le découvre."


hi "Ouais je... faisais autre chose. Tu sais ce que c'est..."

show shizu behind_blank_close
with charachange

shi "…"

show misha sign_smile_close
with charachange


mi "Vraiment~ ? Je me demande ce qui était si important, pour que Hicchan nous évince comme ça~ ! Si ce n'était pas pour passer du temps avec Hanako, je me demande ce qu'il faisait~ ? C'est vraiment intéressant..."


"Maintenant ça ressemble à un interrogatoire. Je suis surpris que Misha soit capable de mettre autant la pression sans vraiment le vouloir."

show hanako defarms_strain_close
with charachange


ha "T... tu étais avec L-Lilly ?"

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")


"Au milieu de nulle part, Hanako réussit à balbutier une réponse. Elle est peut-être silencieuse et timide, mais elle est très perspicace."


hi "Q-qu'est-ce qui te fait dire ça ?"

show hanako emb_sad_close
with charachange


ha "H-hier Lilly a dit quelque chose de s-similaire."

show shizu basic_happy_close at Position(xpos=0.8)
with charachange

shi "…"

show misha hips_smile_close
with charachange


mi "Suspect~ ! Hicchan~ ! Je demande que tu t'expliques !"


hi "Hé, on devrait pas faire le devoir ?"

show misha cross_smile_close
with charachange


mi "Maiseuh~ ! C'est tellement suspect... Même Hanako veut savoir~ !"


"Je me tourne pour regarder Hanako. C'est vrai, d’après l'expression de son visage, elle veut savoir aussi, et je crois qu'on est au-delà du point où je peux m'en sortir sans fournir une explication."


"Je m'excuse auprès de Lilly mentalement. Elle voulait vraiment garder ça secret, mais maintenant ce n'est plus possible."


"Je ressens beaucoup d'émotions en même temps, tellement accumulées que je ne peux pas vraiment les identifier, mais elles s'entrechoquent dans ma tête d'une telle façon que je n'arrive pas à me calmer et parler."


hi "D'accord, je vais te le dire. J'ai été en ville avec Lilly, mais c'est pas ce que tu penses."


hi "Lilly et moi étions... euh... pour l'anniversaire de Hanako... on était..."


"Ça y est, j'ai vendu la mèche. Mais on dirait que Hanako le prend un peu mieux que ce que j'aurais pensé."

show misha perky_confused_close
show shizu adjust_blush_close at Position(xpos=0.85)
show hanako emb_downtimid_close
with charachange


"Un bref silence plane sur notre groupe alors que Shizune et Misha se regardent, un peu gênées. Je peux voir qu'elles ne s'attendaient pas à ce que ça tourne comme ça."


"Misha regarde Hanako pour s'excuser, mais s’arrête. Hanako fixe son bureau et bouge à peine, une expression larmoyante sur le visage. J'avais tort sur le fait qu'elle le prenne bien."

show misha perky_sad_close
with charachange


mi "Hanako ? Je suis désolée..."


"Quelques secondes passent, puis Hanako secoue la tête."

show hanako emb_timid_close
with charachange


ha "C-c'est... pas grave..."


"Elle a une drôle d'expression, comme si elle était très fatiguée. Ça n'est pas normal, mais rien d'alarmant. Personne n'a envie de continuer la conversation, alors on ouvre nos livres et nous commençons le travail."

play music music_rain fadein 12.0
$ renpy.music.set_volume(0.5, 5.0, channel="ambient")

show shizu basic_normal2_close at Position(xpos=0.8)
with charachange


"C'est plutôt ennuyeux. Bien que les équations qu'on doit faire en groupe prennent un moment, la plupart sont juste bêtement mécaniques."


"Bien que ce ne se soit pas aussi mal passé que ça aurait pu, ça a laissé une étrange atmosphère. Néanmoins, on passe outre."


"Le visage de Shizune montre qu'elle pense la même chose du travail que moi, et nous commençons à écrire les résultats."

show misha perky_confused_close
with charachange


"Misha, quant à elle, a les lèvres plissées et joue presque à pile ou face les réponses qu'elle met. Hanako regarde silencieusement, étudiant ce qu'on dit et écrit. Elle a la même expression lorsque le professeur parle."


"C'est dommage qu'elle soit souvent absente. Vu la façon dont elle suit en cours, je crois qu'elle s'en sortirait bien en classe, si elle venait plus régulièrement. Je me demande si c'est pour ça que Shizune est dure avec elle."

show misha perky_smile_close
with charachange


mi "Hé, Hanako, tu arrives à comprendre ça~ ?"


"Misha regarde Hanako, mais je la suspecte plus d’espérer trouver une camarade dans l’ignorance qu'une réelle aide."

show hanako emb_downtimid_close
with charachange


ha "J-je... euh... p-pas vraiment... je c-crois..."


"Je suis surpris de voir à quel point elle est tendue dans sa réponse. Elle souffle, et la façon dont le haut de son corps s’aplatit me fait penser à un ballon se dégonflant."


hi "Tu vas bien ? Je peux m'occuper de cette partie, si tu veux."


"Hanako secoue légèrement la tête, mais surtout, je ne crois pas qu'elle ait besoin d'explication. Misha prend rapidement la parole et je finis par lui expliquer, lentement, étape par étape, comment on en est arrivés au résultat."


"C'est des moments comme ça qui me rappellent que ce genre de travail n'est pas simple pour tout le monde, mais aussi que j'ai cette impression parce que je maîtrise bien le sujet. C'est un sentiment agréable."


"Alors que Misha tape son poing dans sa paume en ayant compris, je découvre un autre sentiment agréable. Mon explication lui a servi, et elle réussit à comprendre l'équation d’après, toute seule, sans que je l'aide."


"Pendant que nous travaillons, Hanako est inhabituellement inactive."


"Elle est déjà silencieuse en temps normal, mais on peut quand même la voir balayer la classe du regard, bouger ses mains, anxieuse, ou baisser les épaules."


"Mais là, ces petits mouvements que j'avais l'habitude de voir sont absents. C'est bizarre quand quelqu'un ne bouge pas du tout. Même Misha se rend compte que quelque chose ne va pas."

show misha perky_confused_close
with charachange


mi "Hanako ? Tu es sûre que ça va ?"


ha "O-oui..."


hi "Tu es sûre ?"

show hanako emb_downsad_close
with charachange


ha "Ça va."


"Un peu plus fort cette fois, mais elle se tourne en disant ça. Ça me fait douter d'autant plus de sa réponse, mais en même temps, je peux dire qu'elle ne veut pas qu'on continue de lui parler."


"Ayant déjà eu une conversation bizarre aujourd'hui dont je ne suis pas totalement remis, je ne veux pas continuer celle-là."


"Nous reprenons notre travail, débattant sur les réponses quand un doute survient, mais je remarque que Hanako ne dit rien du tout. C'est frustrant, elle avait fait tant de progrès."


"Ça me met un peu en colère contre Shizune et Misha d'avoir gâché la surprise que Lilly voulait tant garder secrète. Je sais que je suis fautif, aussi. Peut-être que j'aurais dû faire autrement."

show shizu behind_frustrated_close at Position(xpos=0.85)
with charachange


"Shizune a remarqué que Hanako restait silencieuse et ça l’embête aussi. Je peux le voir sur son visage. C'est étrange de voir que même si elle est sourde, Shizune a remarqué le silence inhabituel de Hanako plus vite que Misha."

show shizu adjust_frown_close
with charachange

shi "…"

show misha sign_smile_close
with charachange


mi "Hanako, tu es trop silencieuse~. Tu dois nous aider aussi~ ! Un jour, on travaillera sur un plus gros projet, un si gros qu'il vaudra le coup d’être fêté, comme avec une glace, ou un gâteau. Si tu agis comme ça, on ne te prendra pas avec nous~ !"


"Je peux dire qu'elles l’embêtent pour qu'elle s'ouvre un peu plus, mais je ne crois pas que ce genre d'approche marche sur Hanako. Ça va juste empirer les choses."


hi "Hé, l’embêtez pas."

show shizu behind_smile_close
with charachange

shi "…"

show misha hips_smile_close
with charachange


mi "Hicchan, c'est juste pour rire~ ! Shicchan dit qu'elle embête tout le monde, de toute façon."

show misha perky_smile_close
show shizu behind_blank_close
with charachange


"Elles abandonnent quand même et Misha me pose une nouvelle question pour changer de sujet. En voyant à quel point le problème sur lequel elle travaille est difficile, je ne sais pas si c'est une belle esquive ou une simple coïncidence."


"Ça prend plus de temps que prévu, parce que Shizune continue de me contredire et que je dois expliquer à Misha et Misha a plus confiance en Shizune qu'en moi. Tellement plus qu'elle en oublie de traduire ce que dit Shizune."


hi "Hé, l'horloge tourne, on devrait accélérer un peu."

stop music fadeout 4.0

show misha perky_confused_close
with charachange


mi "Hicchan~ ! Tu parles comme Shicchan là..."


hi "Juste parce que j'ai regardé ma montre ? Roh, vraiment ? Je suis conscient du temps qui passe, et soudainement je suis le président du Conseil des Étudiants ?"

stop ambient fadeout 4.0

$ ksgallery_unlock("evul hanako_breakdown_down")
scene evbg hanako_breakdown:
    truecenter
    1.0
    zoom 1.05 subpixel True
    easein 8.0 zoom 1.0
show evfg hanako_breakdown_down:
    truecenter
    1.0
    zoom 1.1 subpixel True
    easein 8.0 zoom 1.0
with silentwhiteout

play music music_tragic fadein 8.0


"Je regarde le bureau de Hanako pour voir comment elle va, et m'immobilise. Nos papiers sont couverts d'équations, mais la feuille de Hanako est seulement à moitié faite. On dirait qu'elle n'a rien écrit durant les dernières vingt minutes."


"Quand je réalise ça, j'ai envie de me frapper pour avoir été aussi idiot."


"J'aurais dû savoir que quelqu'un d'aussi fragile que Hanako n'allait pas passer au-dessus de ça aussi facilement, mais j'étais trop occupé à changer de sujet pour le remarquer."


"Elle se renferme doucement sur elle depuis la dernière demi-heure, et je n'en savais rien. Son stylo est toujours dans sa main, mais elle ne le fait pas tourner autour de ses doigts comme elle le fait habituellement. Hanako ne bouge pas d'un cil."

$ ksgallery_unlock("evul hanako_breakdown_up")
scene evbg hanako_breakdown:
    truecenter
    1.0
    zoom 1.0 subpixel False
show evfg hanako_breakdown_up:
    truecenter
    zoom 1.0 subpixel False
with charachange


"C'est seulement au moment où mon regard et ceux de Shizune et Misha se concentrent sur elle qu'elle a un mouvement de recul. Nous détournons le regard, et dans mon cas, en partie de honte d'en être arrivé là."




"Bien qu'à l'extérieur elle se soit complètement renfermée, je sais que c'est une tout autre histoire à l'intérieur."


"À quoi est-ce qu'elle peut penser alors qu'elle essaye de son mieux de se faire la plus petite possible, comme si elle voulait disparaître ?"


"Tout le monde la regarde, lui jetant des regards alors qu'ils finissent leur travail."


"Misha essaye de lui demander ce qui ne va pas, mais ça ne fait qu'empirer le problème. Si elle n'était pas paralysée sur son siège, elle s'enfuirait probablement en courant."

$ ksgallery_unlock("evul hanako_breakdown_closed")
show evfg hanako_breakdown_closed
with charachange


"Les questions de Misha sont dites suffisamment fort pour que tout le monde entende dans la classe, et pendant une seconde je suis prêt à la disputer, parce que je suis sûr que Hanako se sent encore plus mal à cause de ça."


"Bien sûr, si je venais à faire ça, ça ne ferait qu'empirer la situation."


"Je croyais que Hanako était devenue plus forte, et c'est le cas, mais pas suffisamment, j'étais trop naïf. Maintenant, elle est terrifiée, seule au milieu de la classe, et il n'y a rien que je puisse faire sans attirer encore plus l'attention sur elle."


"C'est rageant. Misha est inquiète, et même Shizune se mord les lèvres."


"Personne parmi nous ne sait comment gérer la situation, donc je décide d'appeler Mutou. Son jugement sera sûrement meilleur que le nôtre."


"Je lève les yeux et réussis à croiser son regard, lui faisant silencieusement signe de venir jusqu'ici. Je veux faire ça aussi discrètement que possible, s'il y a une chose qui peut empirer la situation, c'est bien un supplément d'attention."


"Je sais que Hanako peut voir que tout le monde regarde notre groupe. Elle, spécifiquement. Parce qu'ils savent que s'il y a un problème, ce doit être elle."


"Tout le monde la connaît, et c'est la première chose que tout le monde pense. Sa réputation d'élève absentéiste l'a marquée en tant que personne anormale, même à Yamaku."


"Qui sait combien de fois ils l'ont déjà fixée auparavant. Peut-être que c'est parce que la classe la fixe autant qu'elle a peur du regard des gens."


"Le temps qu'il faut à Mutou pour marcher jusque-là semble être une éternité pour Hanako, on dirait qu'elle est sur le point de tomber."

scene bg school_scienceroom
show shizu behind_blank_close:
    tworight
    xpos 0.85 ypos 1.09
show misha perky_sad_close:
    twoleft
    xpos 0.15 ypos 1.09
show hanako emb_downtimid_close:
    center
    ypos 1.09
show muto irritated behind shizu at tworight
with dissolve


"Mutou commence à nous demander discrètement ce qui ne va pas avant de s'interrompre en voyant Hanako."

show misha perky_sad_close
with charachange


mi "Est-ce que... on lui a fait quelque chose... ?"

show muto normal
with charachange


mu "Ne t'inquiète pas."


"Mutou se penche après avoir calmé Misha et regarde intensément Hanako."



show muto smile
with charachange


mu "Ikezawa. Je peux faire quelque chose pour t'aider ?"


"Sa voix est calme et gentille. Tout le monde agit différemment avec Hanako maintenant que tout le monde a remarqué que quelque chose ne va pas avec elle."

show muto smile_close
with characlose


"Hanako ne répond pas, alors Mutou pose doucement une main sur son épaule."

show hanako emb_downsad_close at centertremble_sit
with charachange


"Elle commence à trembler à son contact, mais ne relève pas la tête. Hanako continue de fixer les équations sur son bureau, son regard tellement vide que je doute qu'elle les voie vraiment."


"C'est pire qu'avant. Je me rappelle qu'il n'y a même pas une heure, elle était capable de lui parler presque normalement."

show muto irritated
show hanako emb_downsad_close:
    center
    ypos 1.09
with charadistant


"Mutou grimace un peu en se redressant et maintenant son expression est changée, je peux voir qu'il n'est pas totalement insensible à ce qu'il s'est passé."

show muto normal
with charachange


"Il prend une respiration avant de parler avec une voix très calme. Je suis impressionné par la vitesse avec laquelle il prend le contrôle de la situation."


mu "D'accord. Tout va bien alors."

play ambient sfx_crowd_indoors fadein 8.0


"Mutou ne semble dire ça à personne en particulier. Cependant, ses mots sont suffisamment convaincants pour que la plupart des gens qui regardaient Hanako retournent à leur travail."


"Il jette un rapide coup d’œil autour de lui. Quelques personnes regardent encore curieusement dans notre direction, mais mis à part ça, nous avons réussi à nous libérer de la plus grande partie de l'attention."

show muto smile
with charachange


"Mutou remarque que je fais la même chose que lui et sourit un peu, avec son manque de naturel habituel."


mu "Je crois, dans l’intérêt d'Ikezawa, qu'il serait bien de l'éloigner des autres rapidement."


mu "Nakai, Hakamichi, pouvez-vous sortir avec Ikezawa ? Je vais garder les autres élèves concentrés, occupez-vous juste d'elle, d'accord ?"

show misha sign_confused_close
show shizu behind_blank_close
with charachange


"Il regarde Misha pour lui dire d’interpréter ses mots pour Shizune, mais elle a déjà fini la traduction. C'est remarquable de voir à quel point elle n'a pas besoin de penser à ce qu'elle fait pour traduire, même si elle semble un peu hébétée en même temps."

show muto invis
show misha perky_confused_close
show shizu behind_blank_close:
    xpos 0.85
    ypos 1.0
with dissolvecharamove

hide muto
hide shizu
with None

show shizu behind_blank_close behind hanako:
    tworight
    xpos 0.85
    ypos 1.0
with None


"Hochant la tête, Shizune et moi nous levons et allons à côté de Hanako. Mutou recule pour nous laisser faire et parle à la table derrière lui à des étudiants qui étaient en train de discuter de ce qui se passe."

show hanako emb_downsad_close at center
with charamove


"Nous nous regardons avant de nous baisser à l'unisson pour prendre un de ses bras par dessus nos épaules et soulever Hanako."

show hanako emb_downsad_close:
    twoleft
    xpos 0.35
show shizu behind_blank_close at tworight
show bg school_scienceroom at bgleft
show misha invis_close at Position (xpos=-0.1)
with dissolvecharamove


"Nous commençons à marcher, lentement, pour nous assurer de ne pas lui faire mal. On a beau essayer d'avoir l'air normal, je suis sûr qu'il y aurait encore plus de regards si Mutou ne faisait pas diversion."


"Finalement, nous atteignons la porte et la franchissons."

stop ambient fadeout 0.5

scene bg school_hallway3
with locationchange


"Il n'y a personne à l'extérieur, alors nous marchons le long du couloir. Elle ne semble pas être plus à l'aise que quand elle était en classe. Après un moment, je lui demande si elle préfère s’asseoir."

show shizu adjust_happy_close at tworight
show hanako emb_downsad_close:
    twoleft
    xpos 0.35
with charaenter


"Nous restons là à attendre qu'elle dise quelque chose. Shizune frotte un peu l'épaule de Hanako, mais elle ne répond pas."

show shizu behind_smile_close
with charachange


"Alors que Shizune réessaye, Hanako secoue la tête doucement. Nous la regardons tous les deux, alors nous le remarquons immédiatement."

show shizu adjust_happy_close
show hanako emb_sad_close
with charachange


"La main de Shizune se pose sur l'épaule de Hanako alors qu'elle semble revenir à elle, faisant face à deux visages inquiets la regardant."


"Elle nous regarde silencieusement un moment. Je suis inquiet qu'elle puisse se mettre à paniquer ou faire quelque chose d’extrême, mais son expression change lentement d'un visage sans vie à un visage timide normal."

show hanako emb_downtimid_close
with charachange


"Elle baisse la tête sans dire un mot, nous évitant du regard. Elle a l'air embarrassée, presque honteuse."


"Je veux dire quelque chose, quoi que ce soit, pour l'aider. Je ne peux pas. Je ne sais pas vraiment ce qui est arrivé, ou même ce qui l'a causé. Je me sens inutile, honteux de ne servir à rien."

show shizu basic_normal2_close
with charachange


"Shizune soupire avant de me regarder. Même sans mots, je crois savoir ce qu'elle me demande."


hi "Je vais emmener Hanako à l'infirmerie, ça te va ?"


"J'essaye de communiquer mes intentions via des gestes, mais je ne pense pas réussir à faire passer le message."

show shizu behind_frustrated_close
with charachange


"Shizune fait une drôle de tête face à mes gesticulations, confirmant mes soupçons."

show shizu adjust_frown_close
with charachange


"Elle me pointe du doigt d'un air décisif, puis vers les escaliers. Elle attend que je hoche la tête avant de pointer le doigt vers elle, puis vers la salle de classe."


"Shizune est vraiment meilleure à ce jeu que moi."

show shizu behind_blank_close
with charachange


"Je hoche la tête, vu que son plan est le même que le mien. Shizune se prépare à repartir, mais seulement après avoir regardé Hanako pendant un moment."

hide shizu
with dissolve


hi "Ça te va si je t'accompagne à l'infirmerie ?"

stop music fadeout 4.0


"Hanako ne dit rien et reste debout. Alors que je commence à marcher, elle me suit sagement. J'ai lu des choses sur l'état catatonique auparavant, mais je crois que cette fois je le vois pour de vrai."


"Elle a l'air extrêmement fatiguée. Après tout ce qui est arrivé, ça ne me surprend pas."

stop music fadeout 1.0
scene bg school_nurseoffice
with locationskip


"Après que Hanako ait silencieusement retiré ses chaussures et se soit allongée sur le lit de l'infirmerie, l'infirmier et moi retournons vers le bureau."

play music music_hanako fadein 0.3


"Il ferme le rideau derrière nous. Nous nous asseyons et je lui raconte tout ce qui s'est passé, en détails."


"Je veux comprendre ce qui s'est passé et l'infirmier a une chance de savoir."

show nurse concern at center
with charaenter


"Il hoche la tête à la fin de mon explication, ayant l'air troublé."


nk "Ça a dû être très troublant pour toi d'avoir vu tout ça."


hi "Je mentirais si je disais que non. J'ai compris qu'elle s'est plus ou moins évanouie, mais je ne comprends pas pourquoi c'est arrivé ou pourquoi elle agit comme ça."


"Il hoche la tête, mais son visage est sombre."


hi "Vous ne savez pas non plus ?"


nk "Eh bien... oui et non. C'est compliqué."


nk "J'imagine que tu as entendu parler du concept du secret médical ?"


nk "C'est un peu compliqué à cause de ça. Je vais te dire ça très simplement, ça concerne seulement Ikezawa, son thérapeute et moi."


"J'allais protester, mais y réfléchis une seconde. Ce qu'il dit est totalement logique."


hi "Je comprends."

show nurse neutral
with charachange


nk "Bien, bien. J'aimerais t'aider plus, mais je crois que ce dont Ikezawa a besoin, ce n'est pas quelqu'un qui creuse dans son passé ou ses émotions. Juste quelqu'un qui soit là pour elle."


nk "Elle a besoin d'un ami."

show nurse fabulous
with charachange


nk "Pour ce que ça vaut, je crois que tu as bien fait de l’amener ici. On dirait que tes amis et toi avez bien géré la situation."

show nurse grin
with charachange


nk "Je te donnerais bien une sucette ou un autocollant en récompense, mais tu es trop âgé pour ça."


"Il affiche un grand sourire, faisant visiblement de son mieux pour détendre l’atmosphère. Je ne suis pas vraiment d'humeur à rire, mais il réussit à me soutirer un sourire."


hi "Merci. Euh, ça vous gêne si je reste ici avec Hanako ?"

show nurse neutral
with charachange


nk "C'est gentil à toi, mais je crois que ce serait mieux de la laisser se reposer pour l'instant."


nk "Elle sera de retour dans sa chambre ce soir, tu pourras lui rendre visite à ce moment-là."


"J'approuve et me lève. J'ai l'impression que tout ce que je peux faire avec l'infirmier c'est d’être d'accord avec ce qu'il dit, mais c'était pareil avec les docteurs de l’hôpital après tout."

stop music fadeout 3.0

scene bg school_nursehall
with locationchange


"La marche jusqu’à la salle de classe me semble longue, je suis fatigué après que tant de choses soient arrivées aussi soudainement."

scene bg school_scienceroom
with locationskip

play music music_dreamy fadein 2.0
$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0


"Même alors que je rentre dans la classe, je pense à Hanako."


"Mon estomac est noué alors que je réfléchis à tout ça. Je ne sais toujours pas ce que je vais lui dire quand je la reverrai."


"Heureusement, la classe ne fait pas attention à moi. Il y a quelques regards interrogatifs, mais la plupart des gens ne semblent pas être au courant de ce qui s'est passé."


"Mutou lève les yeux pour avoir mon attention alors que je passe devant son bureau."

show muto normal at center
with charaenter


mu "Nakai... J'en déduis que Ikezawa est à l'infirmerie ?"


hi "Ouais. Je l'ai emmenée et l'infirmier a dit qu'elle devait se reposer."


"Mutou hoche la tête, me confirmant que j'ai fait le bon choix. Il se gratte le menton pendant une seconde avant de se lever."

show muto smile
with charachange


mu "Continuez les exercices. Nakai, je voudrais te voir dans le couloir, s'il te plaît."


"Il parle calmement, mais il ne semble pas agir différemment de d'habitude. Étant un enseignant, c'est peut-être normal."

stop ambient fadeout 1.0
scene bg school_hallway3
with locationchange


"Alors que nous allons dans le couloir, je remarque qu'il regarde rapidement des deux côtés pour vérifier qu'il n'y a pas d'étudiants dans les environs."


"Les couloirs sont plongés dans le silence et j’attends que Mutou parle."

show muto smile at center
with charaenter


mu "Nakai, quel est le but de cette école à ton avis ?"


hi "Mmh... de combler les besoins des étudiants handicapés ?"

show muto normal
with charachange


"Mutou se gratte la tête et la secoue."


mu "Non. Si on voulait faire ça, on aurait construit une nouvelle école de fond en comble. Avec un étage. Des tableaux qui parlent en classe. Ce genre de trucs."


mu "Regarde autour de toi, Nakai. Cette école vous donne à tous un avenir qui vous aurait été refusé dans une école normale."


hi "Hein ?"


mu "Penses-y de cette façon. Si on voulait que tu aies ton diplôme et que tu ailles directement dans un hôpital, tu crois qu'on aurait fait autant d'efforts ?"


"Le ton direct de Mutou me perturbe sur le moment, me faisant oublier la situation immédiate."


hi "Non..."


mu "Exact. Nous voulons que vous sortiez en tant que membres utiles de la société."


hi "Je... ne suis pas sûr de vous suivre..."

show muto smile
with charachange


mu "J'ai de grands espoirs en toi, Nakai. Tu es sûrement le premier étudiant que j'ai qui arrive à suivre mes cours."


"Ça n'est pas quelque chose qu'un professeur doit admettre si facilement."


mu "Tu pourrais facilement étudier les sciences à l'université. Tu y as déjà pensé ?"


hi "Pas vraiment."


mu "Alors, qu'est-ce que tu as envisagé ? Pour ton avenir."


hi "Je... n'ai pas tellement pensé à mon avenir."


"Pendant un moment je me rappelle distinctement que Lilly m'a demandé la même chose."


"Ça fait à peine cinq mois que je me suis retrouvé au sol lors de cette journée enneigée. C'est trop tôt pour que je pense à mon avenir et surtout, les problèmes de Hanako me semblent plus importants pour l'instant."

show muto irritated
with charachange


"Mutou soupire avant de continuer."

show muto normal
with charachange


mu "Pense à cet établissement en tant qu'opportunité. Tu as des locaux pratiques, des bons professeurs et en plus l'infirmier et son personnel."


mu "Tu ne devrais rien faire d'autre que de penser à ton avenir."


hi "Euh... d'accord."


"Alors que je relève la tête pour croiser son regard, je pense à quelque chose. C'est presque comme si Mutou ignorait le problème actuel."


hi "Excusez-moi, mais pourquoi le personnel ne semble pas se préoccuper du fait que Hanako loupe les cours ?"


hi "Je vous ai vu la regarder sortir de classe plus d'une fois. Vous ne devriez pas dire quelque chose ?"

show muto smile
with charachange


mu "Eh bien, Nakai, ce n'est pas aussi simple. Chaque étudiant a ses besoins particuliers, c'est la raison d’être de cette école."


mu "Par exemple, je ne te garderais pas en classe si tu avais du mal à respirer, n'est-ce pas ?"


hi " Mais ce n'est pas..."


"Mutou m’interrompt avant que je ne puisse finir ma phrase."

show muto normal
with charachange


mu "Le cas d'Ikezawa est similaire. Mais à la place d'une réanimation cardiaque ou d'un pacemaker, elle a besoin de temps et d'espace."


mu "L'école est au courant de ça depuis le jour où elle est arrivée ici, donc à chaque fois qu'elle sort de cours, nous la laissons faire."

show muto smile
with charachange


mu "Et même si elle n'est pas la meilleure des élèves, elle arrive à réussir tous ses examens, donc ça n'affecte pas ses capacités scolaires. Ça suffit non ?"


"Je cherche à protester, mais ne trouve pas d'argument. Bien que son handicap semble être surtout physique, le pire reste les dégâts psychologiques."


"Ça me rebute toujours, cela dit. Il n'ignore pas juste sa responsabilité envers son problème ? Elle ne peut pas continuer comme ça toute sa vie."

show muto normal
with charachange


mu "Je comprends que tu puisses ne pas être habitué à ce genre de choses encore. C'est un grand changement pour toi. Cela dit, il reste moins d'un an avant le diplôme."


mu "Peut-être que tu n'auras pas à t'habituer à cette école. Si tu continues tête baissée, je suis sûr que tu t'en sortiras bien aux examens."


"Je hoche la tête, plus pour dire que j'ai compris plutôt que je suis d'accord. J'avais l'impression de m’être habitué à cette école, mais on vient de me démontrer le contraire."


hi "Mais... et pour Hanako ?"


mu "Je pense... bon, j’espère, qu'elle s'en sortira suffisamment pour faire ce qu'elle veut."


mu "Je ne sais pas ce qu'elle a envie de faire, cela dit. Tous les étudiants ne quittent pas l'école avec une idée de ce qu'ils veulent faire, malheureusement."


"Il prend soin d'appuyer sur le dernier mot, comme si ce n'était pas suffisamment clair déjà et me laisse un moment pour réfléchir là-dessus."

show muto smile
with charachange


mu "Aujourd'hui fut une journée difficile pour toi et je doute que tu sois capable de te concentrer après ce qui est arrivé, alors je te permets de partir pour le reste de la journée."


mu "Tu as des bonnes notes jusque-là, tu arriveras à rattraper sans problème ce qu'on faisait."


"Il ajoute un sourire à son compliment, comme pour se faire pardonner du sérieux de la discussion jusque-là."


mu "Va chercher tes affaires, je te verrai demain."


hi "D'accord. Merci."

stop music fadeout 5.0

hide muto
with charaexit


"La discussion avec Mutou m'a perturbé. Je ne sais toujours pas ce que je peux faire pour aider Hanako et je suis encore plus confus à cause de ce que m'a dit Mutou."


"Et ce qui m’embête toujours aussi est le fait que Hanako a été aidée autant par Shizune, l'ennemie de son amie, que par moi, mais je ne sais pas si c'est juste de la fierté masculine ou une vraie gêne."

scene bg school_scienceroom
with locationchange


"Alors que je récupère les affaires de Hanako et les miennes, je continue de penser à ce que je ressens."


"Je veux lui dire que je la comprends et que je suis là pour elle... mais bien que j'aurais pu dire ça hier, je ne peux pas maintenant."


"J'aimerais pouvoir."




label fr_H15:

scene bg school_dormhisao_ss
with shorttimeskip

play music music_night fadein 1.0


"Je suis allongé sur mon lit, réfléchissant."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

nvl clear
window hide
nvl show dissolve


n "\n\nAprès la crise d'angoisse de Hanako, je me suis retrouvé à remettre en question la relation que j'ai avec elle et ce que je sais d'elle."


n "J'ai eu du mal avec les quatre mois que j'ai passés à l’hôpital. Un regard à ses cicatrices me dit qu'elle a dû y passer beaucoup plus de temps."


n "En plus de ça, je ne connais quasiment rien de son passé. Elle m'a dit pour le feu, mais seulement les grandes lignes."


n "Et pour sa famille ? Je n'ai pas demandé à Lilly, il n'y a pas eu de bonne opportunité pour ça."


n "Je ne sais pas où elle a grandi, ou comment était son ancienne école. Je ne connais pas ses anciens amis, ses vœux et ses ambitions. Même pas ses goûts en musique, en nourriture ou en films... toutes ces petites choses que je connais sur tous mes anciens amis."


n "\n\nMais qu'est-ce que j'ai fait, pendant tout ce temps que j'ai passé avec elle et Lilly ?"

$ renpy.music.set_volume(1.0, 1.0, channel="music")
$ renpy.music.set_volume(0.1, 0.0, channel="sound")
play sound sfx_normalbell

nvl clear
nvl hide dissolve
window show


"Au loin, j’entends la sonnerie annoncer la fin des cours. Avec de la chance, Lilly réalisera vite que ni Hanako ni moi ne sommes là et ira au dortoir."

$ renpy.music.set_volume(0.5, 0.0, channel="sound")
stop music fadeout 0.5
play sound sfx_phone


"Mon téléphone sonne, me sortant de ma torpeur. Ça me surprend un peu, vu qu'il a très rarement sonné depuis mon arrivée ici."

scene bg school_dormhisao_blurred_ss
show phone mobile:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with locationchange
with Pause (0.5)


hi "Bonjour, Hisao Nakai à l'appareil..."


li "Oh, Hisao, heureusement j'ai réussi à te joindre. Tu n'étais pas aux endroits habituels, alors je me suis dit que ça serait le moyen le plus rapide de te contacter."


"J'aurais sûrement dû deviner que ce serait Lilly, vu qu'elle est l'une des rares personnes à avoir mon numéro. Même à travers le téléphone, sa voix semble légèrement perturbée."


hi "Je... Hanako et moi sommes partis de cours plus tôt. Elle a eu une sorte de crise d'angoisse..."


"La ligne est silencieuse. S'il n'y avait pas eu un bruit de fond, j'aurais cru que Lilly avait raccroché."


li "D'accord. Tu peux venir dans ma chambre ? J'aimerais te parler."


hi "Ok. J'aimerais... profiter de l'occasion pour te parler, d'ailleurs."


li "Bien... bien. J'ai... également de mauvaises nouvelles. Je crois qu'on devrait discuter de ça face à face."


"C'est difficile d'identifier le sérieux de la situation au ton de Lilly. Elle semble si calme le reste du temps, mais ça peut être une bonne ou une mauvaise chose, suivant la façon dont on voit les choses."


hi "D'accord, j'arrive."

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


"Je prends les affaires de Hanako et je vais en direction de la chambre de Lilly."

scene bg school_girlsdormhall
with locationskip

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_doorknock2


"Je frappe à la porte et elle me demande aussitôt d'entrer."

play music music_drama fadein 4.0

scene bg school_dormlilly
show lilly basic_sleepy:
    center
    ypos 1.17
with locationchange


"Lilly est assise à la table qui est dans sa chambre, affichant un air sérieux. J'imagine que c'est à cause des mauvaises nouvelles."


"Suivant son geste d'invitation, je m'assois devant elle et pose les affaires de Hanako sur la table."

show lilly basic_weaksmile
with charachange


li "Bon, il n'y a aucune raison d'attendre davantage. Tu peux commencer, Hisao ? Qu'est-ce qui s'est passé aujourd'hui ?"


"Mon souvenir de l'incident ayant déjà commencé à s'effacer, je fais de mon mieux pour l'expliquer à Lilly."


"Hanako invitée à travailler en groupe, les questions de Shizune et Misha, notre escapade en ville découverte, et la crise d'angoisse juste après."


"J'ajoute, après coup, la réaction qu'a eue Shizune, et Lilly semble apprécier la nouvelle."


"J'imagine que les rivales ne deviennent pas rivales sans raison. Il doit y avoir une histoire derrière tout ça, mais ce n'est pas le moment de m'en préoccuper."

show lilly basic_concerned
with charachange


li "Je vois. Elle a dit que les rendez-vous avec son thérapeute aidaient, mais j'avais des doutes. C'est bien dommage."

show lilly basic_reminisce
with charachange


li "Son anniversaire avait déjà causé des problèmes auparavant, mais j'avais espéré que ça se serait amélioré avec toi et avec la thérapie plus intensive."

show lilly basic_oops
with charachange


li "Où est Hanako maintenant ?"


hi "La dernière fois que je l'ai vue, elle était à l’infirmerie. J'imagine qu'elle est retournée dans sa chambre maintenant."

show lilly basic_sleepy
with charachange


li "Elle n'était pas à la bibliothèque ou dans la pièce habituelle quand j'ai vérifié, alors tu dois avoir raison."


hi "Tu as dit que tu avais aussi des mauvaises nouvelles... qu'est-ce qu'il y a ? Ça concerne Hanako ?"


"Lilly change de position. Son langage corporel me dit qu'elle cherche les bons mots."

show lilly basic_concerned
with charachange


li "Ma tante est tombée très malade. J'ai bien peur de devoir retourner en Écosse pour lui rentre visite et passer du temps avec ma famille."


hi "Quoi ? Est-ce qu'elle va bien ? Quand est-ce que tu pars ?"

show lilly basic_reminisce
with charachange


li "Je ne sais pas exactement dans quel état elle est, bien que j'aie entendu dire que son état était stable. Je partirai samedi, c’était le prochain vol disponible."


"“Stable.” C'est un code pour “a besoin de rester à l’hôpital”. J'ai été “stable” suffisamment longtemps pour le savoir, et aussi savoir que ça ne veut pas forcément dire en forme, mais qu'il garde juste la tête hors de l'eau."


"D'un autre coté, “stable” est bien meilleur que “état critique”. Au moins elle n'est pas sur le point de mourir."


hi "Stable... c'est déjà ça."

show lilly basic_sad
with charachange


li "Oui, mais ça veut dire que je ne serai pas là pour l'anniversaire de Hanako."

show lilly basic_concerned
with charachange


li "Je voulais te le dire maintenant pour qu'on puisse réfléchir avant de le dire à Hanako, mais après les événements d'aujourd'hui, je me demande s'il ne faudrait pas simplement annuler la fête."


hi "Je... ne crois pas que ce soit une bonne idée. Hanako sait déjà qu'on a prévu une fête maintenant, ne rien faire n'est pas la meilleure option."


hi "Et de toute façon, on doit faire quelque chose pour ton départ, hein ?"

show lilly basic_weaksmile
with charachange


li "Tu dis ça comme si je n'allais pas revenir. Si tout se passe bien, je devrais être partie juste une semaine, peut-être deux."


hi "C'est déjà ça."

show lilly basic_oops
with charachange


li "Avec ça à l'esprit, qu'est-ce que tu suggères ?"


hi "Étant donné les circonstances, je ne crois pas que le karaoke soit approprié. Tu ne pars pas pour une raison joyeuse, alors trop s'amuser serait bizarre."


hi "Qu'est-ce que vous avez fait pour son anniversaire l’année dernière ?"

show lilly basic_reminisce
with charachange


li "L’année dernière... Je n'ai pas pu la faire sortir de sa chambre. Elle avait verrouillé la porte."


li "Je n'ai pu que laisser à manger devant sa porte, m'assurant qu'au moins elle mangeait bien."


"C'est la première fois que je vois Lilly aussi déprimée. Je me sens désolé pour elle, étant donné à quel point elle a dû se sentir triste de ne pas avoir pu être capable d'aider son amie proche."


hi "Peut-être que ça serait mieux de faire la fête avant que tu partes, alors ?"

show lilly basic_weaksmile
with charachange


li "Ça semble être l'option la plus simple."


hi "Je crois qu'on devrait au moins le dire à Hanako, à la fois pour ton voyage et la fête. J'ai les affaires de cours à lui donner aussi."

show lilly basic_smile at center
with dissolvecharamove


li "D'accord. On y va alors ?"


hi "Je... je crois que c'est une bonne idée."


"Une partie de moi meurt d'envie de voir Hanako. La dernière fois que je l'ai vue elle avait l'air d'un zombie, et les dernières heures ont été horribles rien qu'en y pensant."

stop music fadeout 4.0

scene bg school_girlsdormhall
with locationchange


"Nous nous levons en silence et sortons de la chambre de Lilly. Celle de Hanako est juste à côté de celle-ci."

play sound sfx_doorknock2


"On n'obtient pas de réponse en frappant doucement, mais la porte s’avère ne pas être verrouillée. Lilly attend un moment avec la poignée tournée dans la main, puis ouvre la porte."

play music music_moonlight fadein 0.5

scene bg school_dormhanako_ni at Fullpan(8.0)
with locationchange


"La chambre de Hanako est étonnamment vide et monotone. Il n'y a pas de décoration sur les murs blancs, une couverture bleu foncé unie et quelques livres, papiers et objets purement utilitaires sur les étagères."


"Même ses draps sont monochromes. La pièce entière correspond au caractère de Hanako."

scene ev hanako_cry_closed
with whiteout


"Hanako est quant à elle en boule sur son lit. Elle ne pleure peut-être pas à ce moment-là, mais ses yeux clos et les traces laissées sur ses joues montrent qu'elle a pleuré."


"Je rentre en silence dans sa chambre et pose son sac contre son bureau, effrayé de la surprendre."


li "Bonjour, Hanako. Hisao m'a dit ce qui est arrivé aujourd'hui... est-ce que ça va ?"

show ev hanako_cry_away
with charachange


"Hanako ouvre les yeux, très légèrement."


ha "Je... je vais bien..."

show ev hanako_cry_open
with charachange


"Elle penche un peu la tête pour me voir et remarque ma grimace avant que je puisse la cacher."


ha "D-désolée... d-de t'avoir in-inquiété."

show ev hanako_cry_closed
with charachange


ha "V-vraiment... Je vais b-bien maintenant..."


"Elle n'a vraiment pas l'air d'aller bien, bien qu'au moins elle semble plus calme qu'avant. Elle a toujours l'air de pouvoir se briser au moindre souffle, cela dit."


hi "Je te l'ai déjà dit, non ? Tu n'as pas besoin de t'excuser pour ça."


li "Hisao a raison. On... Je... n'aurais pas dû te cacher la fête d'anniversaire."


"Je vois que Hanako tremble à ce mot. Lilly comprend le silence qui s'ensuit et s'abaisse au niveau de Hanako."


li "Je suis celle qui devrait être désolée, Hanako."

show ev hanako_cry_away
with charachange


"Les yeux de Hanako s'ouvrent pour voir Lilly. Elle la regarde un moment avec ses yeux sombres et analytiques."

play sound sfx_rustling

scene bg school_dormhanako_ni
show hanako emb_downsad_ni:
    center
    ypos 1.3
    easein 1.0 ypos 1.15
with locationchange


"Lilly doit avoir un bon effet sur elle, vu que Hanako arrive à se redresser sur le lit et s'assoit au bord. Hanako s’inquiète de beaucoup de choses, mais être une gêne pour les autres doit être ce qui la dérange le plus."

show bg school_dormhanako_ni at bgright
show hanako emb_downsad_ni:
    xpos 0.6
    ypos 1.15
with charamove

show lilly invis:
    twoleft
    xpos 0.4
with None

show lilly basic_weaksmile_ni at Position(ypos=1.17)
with dissolvecharamove


"Entendant Hanako bouger, Lilly s'avance et touche le côté du lit, s’asseyant à côté d'elle, et prend la main de Hanako dans les siennes."


"Le sentiment d’être un intrus dans leur relation est un sentiment qui s'est raréfié au fur et à mesure qu'on a appris à se connaître, mais il est occasionnellement présent. Ce moment est l'un d'entre eux, je crois."


hi "Lilly, si tu veux que je parte..."

show hanako emb_sad_ni
with charachange


ha "Je ne... veux pas..."

show lilly basic_surprised_ni
with charachange


"Lilly et moi sommes tous deux surpris par la prise de courage de Hanako. Je lui réponds un petit “D'accord”, et m'assois sur la chaise de son bureau."

show lilly basic_concerned_ni
with charachange


li "Hanako, j'ai bien peur d'avoir de mauvaises nouvelles."


"Donc Lilly va lui annoncer. Hanako ayant confirmé qu'elle m'estimait important, peut-être que Lilly a pensé que c'était le bon moment, ou du moins, le meilleur moment possible."

show lilly basic_sad_ni
with charachange


li "Ma tante est tombée malade, alors j'ai besoin de retourner dans ma famille pour un moment."

show hanako cover_worry_ni
with charachange


"De l’inquiétude remplace l'expression pleine de remords de Hanako."


ha "Ta... famille... Tu veux dire en Écosse ?"

show lilly basic_reminisce_ni
with charachange


li "Oui. Akira et moi partirons samedi."

show hanako defarms_strain_ni
with charachange


ha "D-donc tu t'en vas ?"

show lilly basic_weaksmile_ni
with charachange


li "Je ne serai pas partie longtemps. Probablement une semaine ou deux. Je serai revenue avant que tu t'en rendes compte, et Hisao sera là, hein ?"


hi "Oui, je ne vais nulle part."

show hanako basic_worry_ni
with charachange


"Hanako semble être seulement un peu rassurée par ce fait, mais elle arrive à trouver du courage en elle quand même."


ha "T-ta tante s'en sortira ?"

show lilly basic_reminisce_ni
with charachange


li "Je n'en suis pas sûre."


"Le silence tombe. C'est terrible que la seule chose qui fasse sortir Hanako de sa déprime soit le malheur de quelqu'un d'autre."


"Je décide de parler de l'autre sujet qui nous amène ici, pour la distraire au moins en partie de l'ambiance triste qui plane dans la pièce."


hi "Bref, on pensait que ce serait une bonne idée de faire une petite fête d'adieu pour Lilly, et qui pourrait aussi être... ouais..."


"Je m’arrête avant de mentionner son anniversaire, vu que ça semble être un déclencheur de forte émotion pour elle."


"Lilly presse gentiment la main de Hanako."

show lilly basic_weaksmile_ni
with charachange


li "Ça te va, Hanako ? Ça ne sera rien de grand hein, juste un petit truc entre nous dans ma chambre."

show hanako def_worry_ni
with charachange


ha "D-donc juste dans l'école ? Juste nous ?"

show lilly basic_smileclosed_ni
with charachange


li "Oui, juste nous trois. Si tu veux, je peux demander à Akira de venir aussi."

show hanako basic_normal_ni
with charachange


ha "D'accord... Tu pars juste pour une semaine ?"

show lilly basic_smile_ni
with charachange


li "Une semaine ou deux, oui. Je te promets que ça ne durera pas longtemps."

show hanako cover_distant_ni
with charachange


ha "D-d'accord..."


"La plupart des gens seraient tristes d'entendre qu'un membre de la famille d'un ami va mal, et heureux de faire une fête, mais, avec Hanako, les deux événements sont reçus de la même manière."


hi "D'accord. On dirait que tu as besoin de te reposer, Hanako, alors il est sûrement mieux qu'on retourne à nos chambres maintenant."

show lilly basic_weaksmile_ni
with charachange


li "Tu sais que si tu as besoin de quoi que ce soit, tu peux toujours parler à Hisao ou à moi, hein ?"


"La voix de Lilly est pensive, une étrange crainte pour quelqu'un qui est sûre d'elle d'habitude."

show hanako basic_bashful_ni
with charachange


ha "Je... sais. Merci, Lilly, Hisao."

show lilly basic_smileclosed_ni at Position(ypos=1.0)
with dissolvecharamove


li "Dans ce cas, bonne nuit, Hanako."

show hanako basic_normal_ni
with charachange


ha "Bonne nuit..."

stop music fadeout 4.0

scene bg school_girlsdormhall
with locationchange


"Je souffle longuement après que la porte se soit refermée derrière nous. Je me sens un peu comme si j'avais été sous l'eau, et que j'étais revenu à la surface seulement maintenant."

show lilly basic_concerned at center
with charaenter


"Lilly ne semble pas être si bien que ça non plus. Elle est pâle et crispée."


hi "Ça va ?"


li "Je suis un peu fatiguée. Les choses ont été... trépidantes récemment."


hi "Tu as dormi tout court ? “Un peu fatiguée” est un euphémisme, vu ton expression."

show lilly basic_sleepy
with charachange


li "Je crois que j'ai pu dormir quelques heures avant les cours. Ça ira."


"Je me sens mal de presser Lilly. Je crois qu'on est tous les deux fatigués à cause de tout ce qui est arrivé."


hi "Je crois que tu devrais te reposer. Ça a été une longue journée et il ne sert à rien de rester debout après tout ça."

show lilly basic_weaksmile
with charachange


li "C'est gentil de t’inquiéter, Hisao. Bonne nuit dans ce cas."


hi "D'accord. Bonne nuit Lilly."

hide lilly
with charaexit


"Je laisse Lilly dans le couloir tandis qu'elle ouvre la porte de sa chambre et je retourne à la mienne."

scene ev hanako_cry_closed_fb
show noiseoverlay
with flash


"Alors que je parcours le couloir silencieux, je n'arrive pas à effacer l'image de Hanako de ma tête. Blottie, avec des larmes sur les joues. Je commençais à croire qu'elle était juste une fille normale avec une timidité extrême, mais c'est bien plus profonds."


"Essayer de faire avancer notre relation maintenant, alors qu'elle est si fragile et vulnérable, ne serait pas bien. Je n'ai pas besoin d'être plus que son ami pour la protéger, pour essayer d'éviter que ce genre de choses arrivent encore."


"Le fait que je ressente potentiellement plus que ça pour elle... cela n'importe plus. Hanako est importante pour moi et c'est pour ça que je ne peux pas profiter d'elle."


"Mais même... je ressens toujours cette brulure quand je pense de cette façon."

scene bg school_girlsdormhall
with flash


"Pour l'instant, j'ai besoin de dormir. Avec de la chance, demain sera une meilleure journée."

scene black
with dissolve



label fr_H16:

scene bg school_scienceroom
with locationchange


"Hanako me perturbe plus quand elle est absente que quand elle est dans la salle."


"J'ai l'impression que son bureau vide m'appelle. Je regarde sans cesse au-dessus de mon épaule, espérant qu'elle apparaisse par magie."



"Elle s'assure de se faire aussi petite que possible quand elle vient en cours, et même si elle allait mieux récemment, ce fait n'a jamais changé."


"Personne ne fait jamais attention à elle en classe, et maintenant qu'elle n'est pas là, ils ne remarquent pas son absence, comme si elle n'avait jamais existé."


"Lilly a bien dit qu'il était courant qu'elle loupe les cours, mais c'est toujours très perturbant."

play sound sfx_normalbell


"La sonnerie annonçant la fin des cours me fait sursauter. C'est seulement à ce moment que je remarque que Misha me tapote avec son crayon pour attirer mon attention."

show shizu invis:
    center
    xpos 0.4
show misha invis_close:
    center
    xpos 0.1
with None

show bg school_scienceroom at bgright
show misha sign_smile_close at Position(xpos=0.2)
show shizu behind_blank at center
with dissolvecharamove

play music music_normal fadein 3.0


mi "Allô... il y a quelqu'un~ ?"


hi "Arrête ça."

show misha hips_grin_close
with charachange


mi "Ah ! Te voilà ! Bienvenue sur terre, Hicchan~ !"


hi "Mais de quoi tu parles ?"

show misha hips_smile_close
with charachange


mi "Tu semblais être dans la lune, je commençais à croire que tu essayais de contacter des extraterrestres."


"Je n'ai pas beaucoup dormi la nuit dernière, donc je ne doute pas des mots de Misha. Je ne sais pas vraiment si c'est dû à mes médicaments, la crise d'angoisse de Hanako hier, mon inquiétude pour elle en général, ou les trois à la fois."


"Je bâille fortement avant de poser mon menton sur ma main, me rappelant à quel point j'ai mal dormi."

show misha perky_confused_close
with charachange


mi "Hé, tu vas bien ? Hier, ça m'a plutôt secouée aussi..."


hi "Ouais... ouais, j'imagine. Je voulais rediscuter avec Hanako."

show misha perky_smile_close
with charachange


mi "Tu l'as vue hier soir ?"


hi "Ouais, Lilly et moi sommes allés lui parler."


hi "Hum, ça va sembler bizarre, mais tu peux dire “merci” à Shizune ? De la part de... Lilly et de moi."


"Je sais que Lilly n'a techniquement pas remercié Shizune, mais je pouvais voir à sa réaction hier soir qu'elle le voulait. Du moins, c'est comme ça que je l'ai interprété."

show shizu adjust_blush
with charachange

show shizu cross_angry
with charachange

shi "…"

show misha sign_confused_close
with charachange


mi "Euh... Je crois que ce que Shicchan essaye de dire est “de rien”."


"Les gestes rapides et les joues enflammées de Shizune m'indiquent qu'elle disait quelque chose de complètement différent. Son expression énervée est suffisamment drôle pour me faire rire cela dit."

show misha perky_confused_close
with charachange


mi "Qu'est-ce qui est aussi drôle, Hicchan~ ? C'est quelque chose qu'on a dit ?"


hi "Non, non, ce n'est pas ça. Je pensais juste que Shizune pouvait être mignonne parfois."

show misha cross_laugh_close
with charachange


mi "Wahahaha~ ! Tu as raison~ ! Shicchan est vraiment mignonne quand elle essaye de ne pas l’être !"


"Je remarque que Misha a décidé de ne pas traduire sa réponse à Shizune. Peut-être que l’énervement de Shizune suffit sans qu'on dise “mignonne” à tout va."

show shizu adjust_frown
with charachange


"Néanmoins, Shizune se calme rapidement et dit quelque chose d'autre à Misha."

show shizu behind_smile
with charachange

shi "…"

show misha perky_smile_close
with charachange


mi "Oh~ ? D'accord... Hicchan, Shicchan veut que tu viennes manger avec nous."


hi "Manger hein ?"


"Me détournant un peu d'elles, histoire de ne pas être influencé par leurs sourires suppliants, je réfléchis."


"L'invitation est tentante. Un dîner à l’extérieur avec deux jolies filles n'est pas une mauvaise chose, après tout. Mais la vision de Hanako, enfermée dans sa chambre, ne quitte pas mon esprit."


hi "Désolé, pas cette fois."

show misha perky_sad_close
with charachange

mi "Awww…"

show shizu behind_frown
with charachange


"Misha ne traduit pas ma réponse, mais Shizune comprend facilement avec la grimace qu'elle affiche."

show shizu basic_normal2
with charachange


"Elle bouge les bras, commençant apparemment une sorte de protestation, mais s’arrête et tapote l'épaule de Misha deux fois. Au moment où Misha lui accorde son attention, la seule action de Shizune est un haussement d'épaules."

show misha perky_confused_close
with charachange


mi "Ah bon. Comme tu veux, Hicchan."


hi "Je vous promets que je vous rejoindrai une autre fois."

show misha perky_smile_close
show shizu behind_blank
with charachange


"Misha semble vouloir continuer, mais Shizune ne partage pas son avis. Avec un signe de la tête pour dire à Misha de la suivre, Shizune lève simplement la main pour me dire au revoir."

hide misha
hide shizu
with charaexit

stop music fadeout 3.0


"Alors qu'elles passent la porte, je lève également le bras jusqu’à ce qu'elles soient parties."


"Je ne pensais pas qu'elles seraient si déçues et je me sens un peu mal de les avoir lâchées. Mais en même temps, j'ai des choses à faire."

scene bg school_girlsdormhall at right
with shorttimeskip


"Le dortoir des filles est particulièrement bruyant aujourd'hui, avec plein de filles jouant et regardant la télévision dans la salle commune du rez-de-chaussée. Je peux entendre leurs voix même maintenant que je suis devant la porte de Hanako."


"C'est un étrange contraste avec l'étage vide où elle se trouve. Les voix venant de plus bas rendent le vide un peu moins triste."


"J'avais espéré que Hanako soit en classe aujourd'hui, spécialement après avoir parlé à Lilly et moi hier soir, mais je crois que je ne dois pas lui en vouloir. C'était un moment plutôt difficile pour elle."

scene bg school_dormhanako_ni
show hanagown worry_close:
    center
    xpos 0.39
show expression Solid("#00000022")
show hanako_door_base at right
show hanako_door_door at left
with locationchange

play sound sfx_doorknock2


"Ne sachant pas dans quel état elle est, je respire à fond avant de frapper brièvement sur la porte marron."


"Je reste debout là, faisant de mon mieux pour ne pas avoir l'air anxieux."


"Alors que les secondes s'écoulent, je commence à croire qu'elle est endormie ou qu'elle ne m'a pas entendu. Cela dit, la poignée de porte tourne un peu avant que je ne puisse refrapper."

play sound sfx_dooropen

show hanako_door_door:
    xpos -0.05
with charamove


"La porte s'ouvre très légèrement et un œil apparaît dans l'entrebâillement. Je suis sûr qu'elle installerait un judas sur sa porte si elle en avait le droit."


"Je me tiens là et lui souris. Je ne crois pas que dire quoi que ce soit pourrait l'aider après tout."


"Hanako me regarde sans un mot non plus. La porte n'est pas suffisamment ouverte pour que je puisse voir son expression, je peux seulement imaginer ce qu'elle pense."


"Un long moment se passe alors que nous nous regardons, le seul bruit audible est ce qui vient du rez-de-chaussée."

hide hanagown
with charaexit


"Je ne sais pas vraiment combien de temps il aura fallu, mais elle bouge enfin. Je me demande si elle va me laisser entrer ou me planter dehors, quand enfin la porte s'ouvre."

play sound sfx_door_creak

show hanako_door_door:
    easeout 1.0 xpos -0.2
show hanako_door_base:
    easeout 1.0 xpos 1.1
show bg school_dormhanako_ni:
    center
    easeout 1.0 xpos 0.55
with None

scene bg school_dormhanako
show hanagown normal at center
with silentwhiteout

play music music_comfort


"Maintenant que j'ai une vue complète de sa chambre, la première chose que je remarque sont les cheveux mouillés de Hanako. Elle s'est lavée récemment, ce qui est rendu encore plus évident par l'odeur de shampoing qu'elle répand."


"Elle a une expression intriguée, comme si elle ne s'attendait pas à ma venue. Quand bien même, je ne sais pas vraiment ce qu'elle pense."


"J'ai l'impression qu'elle était partie longtemps et que maintenant elle est revenue, mais qu'aucun de nous deux ne sait comment réagir."

show hanagown distant
with charachange


"Hanako réalise qu'elle me fixe et détourne les yeux avant de se tourner sur le côté. Je décide de prendre ça comme une invitation et fais un pas dans sa chambre, refermant la porte derrière moi."


"Je peux voir ses mains sortir de la robe trop grande pour elle. J'essaye de me concentrer sur ce que je veux dire, mais son odeur m'embrouille l'esprit."


"À ma grande surprise, ce n'est pas moi, mais Hanako qui rompt le silence."

show hanagown normal
with charachange


ha "Pourquoi..."


hi "Parce que... euh..."


"...Pourquoi je suis venu ici ?"


"J'étais inquiet pour Hanako, alors je suis venu la voir. Elle m'a laissé entrer, et puis... quoi ? Qu'est-ce que je voulais faire ? Qu'est-ce que je voulais dire ?"


"Pourquoi je n'y ai pas pensé avant d'arriver ici..."


"Je veux me rattraper pour ce que j'ai fait. Je veux essayer de réduire la distance entre nous et la voir heureuse. Comment est-ce que je peux faire ça si je ne connais rien d'elle ?"


"Je me demande... Je me demande si c'est comme ça que Iwanako se sentait quand elle m'a vu allongé dans cette chambre d’hôpital."


hi "Je euh... Je... euh..."


"Un soupir me permet de me ressaisir. Je ne crois pas avoir déjà été aussi nerveux près de quelqu'un. Quand je suis comme ça, je ne pense pas pouvoir mentir. Même si j'y arrivais, Hanako s'en rendrait compte tout de suite."


hi "Je ne sais pas. Je voulais... juste te voir, je crois."

show hanagown smile
with charachange


"Ses doigts arrêtent de bouger, ce qui me surprend. Je regarde son visage, elle sourit et hoche la tête. Ma réponse lui convient ?"


ha "Euh... vu que tu es là..."

show hanagown distant_blush
with charachange


ha "J'aimerais... jouer aux échecs avec toi..."


"Je souris, rassuré qu'après tout ce qui s'est passé, après que j'aie autant stressé, elle veuille juste jouer. Regardant son visage, un sourire fragile dessus, je réalise que c'est plus que ça."


"Elle aurait pu ne pas répondre à la porte. Elle aurait pu la refermer juste après avoir vu mon visage. Elle aurait pu me demander de partir."


"Elle aurait pu me rejeter n'importe quand, mais elle ne l'a pas fait. Maintenant, elle veut jouer au même jeu que celui auquel on a joué la première fois qu'on a passé du temps ensemble."


"Un sentiment de soulagement me submerge."


"Tout ira bien. Hanako m'a laissé rentrer dans son monde. Tant qu'on peut être ensemble, je crois que tout ira bien."


hi "Avec plaisir."

stop music fadeout 2.0

scene black
with dissolve



label fr_H17:

scene bg school_girlsdormhall
with locationchange


"Le jour de la fête d'anniversaire de Hanako est arrivé."


"Pour être honnête, j'ai hâte de revoir Hanako et Lilly en pyjamas. Hanako dans sa robe est plutôt mignonne, bien qu'un peu classique, et l'ensemble en soie de Lilly est assez beau."


"Mais l’événement est un peu gâché par la réaction de Hanako."


"Je ne comprends toujours pas ce qui est arrivé, j'arrive à peine à imaginer les raisons possibles. Mais je ne crois pas que j'aurai une réponse si je ne lui demande pas."

play sound sfx_doorknock2


"Avec ça à l'esprit, je frappe à la porte voisine de la chambre de Hanako."


li "C'est toi, Hisao ?"


hi "Ouais, c'est moi."


"Je peux entendre des petits pas arriver jusqu’à la porte et le verrou s'ouvrir. Je ne crois pas avoir déjà vu Lilly verrouiller sa porte auparavant, ça me rend un peu suspicieux."


"Une fois que la porte s'ouvre, la vue est... un peu décevante pour une fête d'anniversaire."

play music music_ease fadein 1.0

scene ev lilly_bedroom
with locationchange


"Hanako retourne à son siège avec un petit sourire et un hochement de tête, me laissant fermer la porte et, imaginant que c'est ce qu'elles veulent, verrouiller la porte."


"À ce moment-là, je réalise que ce qu'il se passe ici est une réunion pour boire le thé, juste comme une autre. D'une certaine façon, ce n'est pas surprenant."

scene ev lilly_bedroom_large:
    ypos 0 xpos -860
with locationchange


"Je constate avec soulagement que Hanako semble relativement calme. Ne pas être venue en cours a dû lui faire du bien et lui a donné du temps pour se remettre de tout ça."

scene bg school_dormlilly
show lilly basic_smileclosed_paj:
    twoleft
    ypos 1.2
show hanagown distant:
    tworight
    ypos 1.17
with locationchange


"Je m'assieds entre elles deux à la table basse, la théière fumante au centre."


"Un grand sac marron à côté de Lilly attire mon attention. Je regarde discrètement dans sa direction plusieurs fois, mais n'arrive pas à bien voir."


"Regardant Hanako, il me semble qu'elle est aussi curieuse que moi."


hi "Dis, Lilly ?"


"Lilly finit la tasse de thé qu'elle a portée à ses lèvres avant de la reposer et de me donner son attention."

show lilly basic_smile_paj
with charachange


li "Oui ?"


hi "Je me demandais juste ce qu'était ce sac marron..."


"Elle affiche un petit sourire."

show lilly basic_cheerful_paj
with charachange


li "C'est le cadeau d'Akira. Malheureusement, elle a dit qu'elle avait du travail et qu'elle ne pouvait pas venir."


"Lilly se penche et attrape l'objet situé à l'intérieur du sac."


"Je lève un sourcil alors que deux objets, non pas un, émergent du sac. Lilly tient deux bouteilles en verre. C'est donc pour ça que la porte était fermée."

show wine:
    yalign 0.5 xanchor 0.0 xpos 1.0 alpha 0.0
    easein 1.0 alpha 1.0 xanchor 1.0
with Pause(1.0)


ha "Du vin..."


"Lilly les pose toutes les deux sur la table, un vin rouge et un blanc. J'aimerais croire que c'est du faux vin sans alcool, mais si c'était le cas, je n'aurais pas besoin d’être inquiet."


hi "Alcool ? Vraiment ? Tu es sûre que c'est une bonne idée ?"

show lilly basic_smileclosed_paj
with charachange


"Lilly sourit et rit doucement. Je ne crois pas qu'elle le soit vraiment."


li "C'est un cadeau de ma sœur. Je sais que c'est un peu limite, mais juste un peu ne devrait pas faire de mal."


"Si Lilly était sérieuse à ce sujet, je ne pense pas qu'elle aurait accepté aussi facilement. Cela dit, je pensais qu'Akira était sérieuse et responsable, un peu comme une Lilly plus âgée, mais j'avais tort. On n'a même pas l'âge légal pour boire."


hi "Bon, dans ce cas, je ne me plaindrai pas. Ça n'a pas l'air mauvais, de toute façon."


"Je ne suis pas un connaisseur, mais au moins les bouteilles ont l'air bien. À part deux petits verres de vin que j'ai eu l'occasion de boire à des repas de famille, je n'en ai pas eu assez pour savoir vraiment le gôut que ça a."

show hanagown smile
with None

show wine:
    easeout 1.0 alpha 0.0 xanchor 0.0
with Pause(1.0)

hide wine
with None


"Ça, et on ne peut pas dire que je sois d'un grand sérieux non plus. À en juger par l'expression de Hanako, elle pense la même chose, et c'est son anniversaire après tout."

show lilly basic_smile_paj
with charachange


li "J'en ouvre une ?"


hi "Oui. Je vais prendre des—{w=0.3}{nw}"

$ renpy.music.set_volume(0.5, 0.5, channel="music")
$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_doorknock2

show lilly basic_displeased_paj
show hanagown worry
with vpunch


"Je bondis en entendant trois forts coups à la porte. Hanako tourne la tête et Lilly ferme les yeux alors qu'elle écoute attentivement. Aucun d'entre nous n'a envie de se faire prendre."

show lilly basic_oops_paj
with charachange


li "Qui est-ce ?"


mystery "Laisse-moi entrer, je gèle !"

show lilly basic_weaksmile_paj
with charachange

$ renpy.music.set_volume(1.0, 6.0, channel="music")


"Lilly laisse échapper un soupir de soulagement avant de demander à Hanako d'ouvrir la porte."

show hanagown invis at tworight
with dissolvecharamove

hide hanagown
with None


"Elle se lève et remet en place sa robe avant de se diriger vers la porte, n'étant apparemment toujours pas sûre de qui c'est, mais faisant suffisament confiance à Lilly pour faire ce qu'elle dit."


"Je peux voir une silhouette sombre avec une tête blonde apparaître par-delà l'épaule de Hanako alors qu'elle ouvre la porte."


mystery "Joyeux anniversaire Hanako."


ha "M-merci... Akira..."


"Hanako salue Akira tout en remuant les doigts. Donc, voilà la grande sœur de Lilly."

show bg school_dormlilly at bgleft
show lilly basic_weaksmile_paj:
    left
    ypos 1.2
with charamove

show hanagown invis at center
show akira invis at right
with None

show hanagown normal at Position(ypos=1.17)
show akira basic_smile:
    right
    xpos 0.95
with dissolvecharamove


"Akira suit Hanako jusqu’à la table après avoir fermé la porte derrière elle, me donnant le temps de bien la voir."


"Elle a l'air de faire à peu près la même taille que Hanako, avec des cheveux blonds plutôt courts. Ça, ajouté à son tour de poitrine plutôt modeste, son costume masculin et sa voix rauque, lui donne un air très androgyne."

show akira basic_ending at Position(ypos=1.18)
with dissolvecharamove


"Sans rien dire d'autre, elle s'assied à la table en face de moi."

show lilly basic_smile_paj
with charachange


li "Ça fait plaisir d'avoir ta compagnie, Akira. Tu as réussi à t'échapper du travail ?"

show akira basic_boo
with charachange


aki "Ouaip. Je dois y retourner dans pas longtemps, mais j'ai réussi à trouver le temps de venir jusqu'ici."

show akira basic_smile
with charachange


aki "Et donc... j'imagine que ce jeune homme est Hisao ?"


"Elle affiche un sourire confiant à mon intention, donc je hoche poliment la tête en retour. Vu qu'elle utilise déjà mon prénom, elle est beaucoup moins formelle qu'elle en a l'air."


"Attends, si elle sait déjà qui je suis, ça veut dire que Lilly lui a parlé de moi. Je me demande ce qu'elle a dit."

show lilly basic_smileclosed_paj
with charachange


li "Désolée de ne pas t'avoir présenté, Hisao. C'est Akira Satou, ma grande sœur."


hi "Je vois. Content de te rencontrer."

show akira basic_ending
show hanagown worry:
    0.1
    ease 0.1 ypos 1.15
    ease 0.1 ypos 1.17
with Dissolve(0.1)


"La personne en question tape dans ses mains, faisant un peu sursauter Hanako."

show akira basic_lost
with charachange


"Akira le remarque et semble mal à l'aise pendant une poignée de secondes, avant de retourner à son état initial."

show akira basic_smile
with charachange


"C'est seulement maintenant que je réalise qu'Akira ne prête aucune attention aux cicatrices de Hanako. Hanako semble être à l'aise avec Akira, sans être forcément détendue."

show akira basic_laugh
with charachange


aki "Bon, je vois que les cadeaux sont déjà ouverts ? Pas besoin d'attendre, Hisao et la fille dont c'est l'anniversaire aujourd'hui semblent être impatients."

show lilly basic_cheerful_paj
with charachange


"Lilly rit un peu alors que je me tourne, embarrassé de ne pas avoir pu cacher mon intérêt. Les yeux de Hanako montrent qu'elle a envie d'essayer le vin avec moi, donc j'affiche une fausse expression d'indifférence."

show lilly basic_smile_paj
show akira basic_smile
show hanagown distant
with charachange


"Akira arrive à ouvrir la première bouteille sans effort et Hanako va chercher des verres avant que je ne verse du vin blanc dans les quatre."


"J'ai entendu quelque part que le vin blanc possède moins d'alcool que le vin rouge, donc je crois que c'est mieux de commencer par ça."


hi "Voilà pour Hanako, et au voyage de Lilly."

show lilly basic_giggle_paj
show akira basic_laugh
with charachange


$ doublespeak (li, aki, "Tchin !")


show hanagown smile
with charachange


ha "T-tchin..."

show lilly basic_smileclosed_paj
show akira basic_smile
with charachange


"Après le lever traditionnel des verres, nous buvons le liquide jaune pâle. Ça ne ressemble en rien à ce que j'ai bu avec mes parents, la saveur fruitée cachant presque entièrement le goût de l'alcool."


"Peut-être que c'est le goût qu'est censé avoir le bon vin. Aussi, il est possible qu'Akira ait juste choisi un vin qui nous convienne, vu qu'aucun d'entre nous n'est habitué à l'alcool."


"Ou du moins, j’espère qu'aucun d'entre nous ne l'est."


hi "Ce n'est pas trop mauvais. Je m'attendais à quelque chose de... plus fort."

show akira basic_ending
with charachange


aki "Si tu n'avais pas aimé, j'ai quelques autres variétés que tu aurais pu essayer."


hi "On dirait que tu t'y connais plutôt pas mal en vin."

show akira basic_smile
with charachange


aki "Juste un peu, je suis plus amatrice de bière."

show akira basic_laugh
with charachange


aki "J'ai une assez bonne descente, cela dit."


"Comme pour prouver ce qu'elle dit, elle remplit de nouveau son verre avant de l’amener à ses lèvres et de jeter la tête en arrière."

stop music fadeout 6.0

show akira basic_smile
show hanagown normal
with charachange


"Hanako et moi regardons en silence le contenu du verre d'Akira disparaître. Je n'arrive pas à savoir si je suis impressionné ou troublé, mais je n'ai certainement aucune envie de l'imiter."

show lilly basic_displeased_paj
with charachange


"Lilly grimace légèrement à la vantardise de sa sœur. Je remarque qu'elle boit quand même son verre en même temps, cela dit."

show lilly basic_weaksmile_paj
with charachange


li "Bref, maintenant que le cadeau d'Akira a été ouvert et goûté, si on passait aux nôtres ?"

show hanagown worry
with charachange


ha "C-cadeaux ?"

play music music_twinkle fadein 6.0

show lilly basic_smile_paj
with charachange


li "Oui, on t'a acheté des cadeaux. C'est ton anniversaire après tout."

show lilly basic_smileclosed_paj
with charachange


li "Celui-là est de moi."


"Lilly sort la poupée soigneusement empaquetée de dessous la table, et la tend à Hanako."


"Hanako tient le cadeau comme s'il était de verre, le tournant avec précaution pour retirer le ruban adhésif qui tient l’emballage. Finalement le papier tombe, révélant la robe vert émeraude de la poupée."

show hanagown normal_blush
with charachange


ha "Elle est... magnifique."


"Je ne sais pas tellement quelle réaction j'attendais de la part de Hanako. Le manque presque total de poupées dans sa chambre me faisait penser qu'elle ne s'y intéressait pas, mais ses yeux pétillants me montrent le contraire."


"Elle tourne la poupée avec la même délicatesse dont elle a fait preuve pour ouvrir l’emballage, comme si elle s'attendait à ce qu'elle disparaisse de ses mains."

show lilly basic_weaksmile_paj
with charachange


li "Je suis contente que tu l'aimes. Hisao l'a choisie, pour être honnête."


"Hanako se rappelle soudainement qu'elle n'est pas seule dans la pièce, et relâche l'attention qu'elle portait à la poupée."

show hanagown smile
with charachange


ha "O-oui, je l'aime bien. M-merci, Lilly et H-Hisao."


hi "En fait, je t’ai pris quelque chose d'autre..."


"J'attrape mon sac et en sors le jeu d’échec emballé."


hi "Voilà. Joyeux anniversaire."

show hanagown normal
with charachange


"Hanako pose avec précaution la poupée de Lilly à côté d'elle et ouvre mon cadeau avec le même soin qu'elle a montré pour celui de Lilly."




"Peu de temps après, les carrés de l'échiquier sont visibles, et Hanako passe doucement ses doigts sur la surface taillée."

show hanagown normal_blush
with charachange


ha "Oh !"


"Presque par accident elle actionne le mécanisme du tiroir, se surprenant en même temps. Elle l'ouvre et en sort une des pièces grises."


"Elle semble être absorbée par les pièces d’échecs comme elle l'était par la poupée."


hi "Elles sont en corail. Du corail naturel, pas teint. C'est ce qu'on m'a dit."

show hanagown smile
with charachange


ha "Merci, Hisao..."


hi "Pas de problème. C'est ton anniversaire, après tout."

show hanagown distant
with charachange


ha "C'est vrai... mon anniversaire..."


"Une fois encore, la réaction de Hanako semble un peu décalée, et elle referme avec attention le tiroir."

show akira basic_lost
with charachange




"Je remarque que le sourire d'Akira commence à s'effacer. Je me demande si elle sait tout ce qui est arrivé en classe, vu qu'elle semble faire attention à Hanako."


hi "Je te battrai un de ces quatre."

show hanagown smile
with charachange


ha "Je... m'assurerai de te battre toi..."


show ev hanako_presents2:
    truecenter
    subpixel True zoom 1.1
    acdc_warp 10.0 zoom 1.0
with whiteout


"Elle prend la poupée qu'elle a reçue de Lilly et la serre fort contre elle avec le petit échiquier, posant la pièce dessus."


"Ça semble la calmer quelque peu, et nous restons assis en silence un moment."


"Je crois que c'est une des rares fois où je l'ai vue vraiment heureuse, serrant l'amitié de deux personnes contre elle aussi fort qu'elle le peut."

show akira basic_boo
show lilly basic_smile_paj
with None

hide ev
with locationchange


ha "Merci, Lilly. Merci, Hisao."

show hanagown worry_blush
with charachange


"En nous remerciant, Hanako lâche la pièce d’échecs et se dépêche de la ramasser."

show hanagown distant
with charachange


"Après l'avoir récupérée, Hanako pose l'échiquier et boit nerveusement son vin. Comme si elle venait de se rappeler du monde réel et que son échappatoire la plus rapide était dans un verre."


hi "Hé, doucement, tu ne devrais pas boire aussi vite..."

show lilly basic_weaksmile_paj
with charachange


li "C'est une fête, Hisao..."


"Même si elle dit ça, il y a une certaine inquiétude dans sa voix. Hochant la tete, Lilly suit l'exemple de Hanako, même si elle ne boit pas aussi vite."


"Elle semble prendre de petites gorgées et laisser le vin glisser sur sa langue avant de l'avaler. J'imagine que c'est probablement la meilleure façon de faire, et je l'imite."


hi "Vu que c'est aussi une sorte de fête de départ, j’espère que tu apprécieras quand même ton voyage, Lilly. Avec de la chance, ta tante ira bien."

show hanagown worry
with charachange


ha "J-j’espère que ta tante ira bien aussi, Lilly..."

show lilly basic_surprised_paj
with charachange


"Lilly et moi sommes surpris qu'elle souhaite cela avec tant de ferveur, malgré sa propre situation familiale. Je suis un peu impressionné."

show lilly basic_weaksmile_paj
with charachange


li "Eh bien, eh bien. Merci à vous deux. Je m'assurerai de transmettre vos souhaits à ma famille."

show akira basic_smile
with charachange


aki "En fin de compte, tout ira bien, Lilly. Ne t’inquiète donc pas."


"Vu que l'humeur de la pièce est devenue bien plus maussade, je décide d'essayer de changer de sujet."


hi "Bon, et si on entamait le gâteau ?"

show hanagown normal
show lilly basic_smileclosed_paj
show akira basic_ending
with charachange


"Ma suggestion a eu l'effet escompté, tout le monde se réjouit instantanément."

show hanagown normal_blush
with charachange


ha "O-oui, s'il te plaît..."

show lilly basic_surprised_paj
with charachange


li "Gâteau ? Je ne savais pas qu'il y avait un gâteau..."


hi "J'en ai pris un avant de venir, avec des petits encas."

show lilly basic_giggle_paj
with charachange


li "Bien joué, Hisao. Au moins l'un d'entre nous a pensé à en amener un."


"Tout le monde semble apprécier l'idée, alors je sors le gâteau de mon sac et commence à le couper."


"Je n'aurais pas pensé que le vin se mariait bien avec le gâteau au chocolat, mais personne ne semble s'en soucier. Plus personne ne parle alors que nous commençons à manger."


"Je n'étais pas sûr que ce soit une bonne idée à la base ; après la crise d'angoisse de Hanako, je m'attendais au pire pour ce soir, mais je crois que l'idée de Lilly de lui faire de bons souvenirs pour son anniversaire marche bien."


"D’après la réaction de Hanako face aux cadeaux, je peux dire qu'elle apprécie vraiment."

show lilly basic_smileclosed_paj
show akira basic_smile
show hanagown drunknormal
with shorttimeskip


"Hanako essaye de se verser un autre verre de vin, mais finit par en faire tomber sur la table. Elle en a pris quelques-uns déjà, et sachant qu'elle n'a jamais bu d'alcool auparavant, ça ne m'étonne pas qu'elle soit quelque peu pompette."

show hanagown drunksad
with charachange


ha "D-désolée Lilly... Je ne voulais pas... Je..."


hi "Ne t’embête pas, je m'en occupe..."

$ ksgallery_unlock("unlock_ev lilly_hanako_hug_end")
show ev lilly_hanako_hug:
    xalign 0.5 yalign 1.0 subpixel True
    easein 12.0 yanchor 0.0 ypos -0.15
with whiteout


"Lilly tend les bras et prend gentiment Hanako qui panique un peu dans ses bras, me donnant une occasion de m'occuper de la table."


li "Ça va, Hanako. Je suis juste contente que tu sois là."


"Hanako hoche un peu la tête en réponse. C'est normal, j'imagine, que Lilly soit celle qui l'aide dans un moment comme celui-là. Je n'ai aucune idée de comment Hanako serait si elle n'était pas là."


"Les voir toutes les deux comme ça me fait apprécier d’être là, dans un moment aussi intime. Même Akira ne peut pas s’empêcher de sourire en voyant ça."


"Je n'aurais jamais pensé me faire des amis aussi vite et je suis encore plus content que ce soit elles, mes amies."

stop music fadeout 3.0

show lilly basic_cheerful_paj:
    xpos 0.02
    ease 1.0 xpos 0.0
show hanagown drunksmile:
    xpos 0.48
    ease 1.0 xpos 0.5
with None

hide ev
with locationchange


"Elles se séparent lentement, Hanako se ressaisissant quelque peu pendant que je retourne rapidement à ma tache."


"Je trouve une serviette parmi le set à thé de Lilly et commence à éponger le liquide. Au moment où j'ai fini, Hanako et Lilly ont réussi à déboucher la deuxième bouteille et ont rempli leurs verres."

show akira basic_ending
with charachange


aki "On dirait que vous appréciez le vin. N'en abusez pas en tout cas, hein."


"Nous hochons tous la tête et approuvons, mais son rappel est quelque peu bizarre de la part de quelqu'un qui amène de l'alcool à des mineurs."

play music music_comedy fadein 0.5

show lilly basic_cheerfulblush_paj at Position(xpos=0.0)
show hanagown drunkgiggle at Position(xpos=0.5)
show akira basic_boo
with shorttimeskip


"Le deuxième verre de vin descend beaucoup plus vite que le premier et avant que nous le remarquions, la seconde bouteille est vide. Bien qu'Akira nous aide à les finir, Hanako semble avoir bu autant qu'elle."


"Ma tête est quelque peu légère, mais je crois que j'ai réussi à évaluer ma tolérance assez bien. Hanako sourit un peu bêtement, jouant avec les cheveux de sa poupée. Je crois que je peux dire sans me tromper qu'elle ne s'est pas modérée comme moi."


"Je ne crois pas que c'était l'intention de Hanako de se rendre ivre, mais on dirait que l'alcool a fait de l'effet d'un coup. Elle est très mince, ce qui ne doit pas l'aider, j'imagine."


"Lilly lève son verre, faisant tourner son doigt sur le bord. Ses joues sont rosées, mais elle arrive à éviter d'avoir l'air complètement ivre. Akira est, comme prévu, toujours sobre."


"Son sourire est peut-être un peu plus large qu'avant. Peut-être."

show hanagown drunkgiggle:
    ease 0.1 ypos 1.15
    ease 0.1 ypos 1.17
with None

show hanagown drunkpout
with charachange


"Hanako a le hoquet soudainement et fait tomber accidentellement la poupée."

show hanagown drunksad
with charachange


ha "Je... crois que je devrais aller me coucher. M-merci, Hisao, et Lilly, et Aaaakiraaaa."


"Elle a du mal à prononcer le nom de Akira, évitant de justesse de rire au milieu. Elle est complètement ivre, et je n'arrive pas à décider si je dois me sentir mal ou non d'être amusé de la voir dans cet état."


"C'est vraiment bizarre de la voir agir aussi librement. Dommage que ça soit juste à cause de l'alcool."

show akira basic_ending at Position(ypos=1.0)
with dissolvecharamove


aki "Laisse-moi t'aider."


"Akira commence à aider Hanako, mais est arrêtée par Lilly qui tousse fort."

show lilly basic_planned_paj
with charachange


li "Hisao, est-ce que tu pourrais... ?"

show akira basic_lost
with charachange


"Akira semble un peu surprise et je dois admettre que moi aussi. Ça ne me gêne pas du tout, surtout quand c'est dit avec un tel sourire... c'est juste inattendu."


hi "D-d'accord. Pas de problème."

hide hanagown
with None

show hanagown drunksad:
    center
    ypos 1.17
with None

show hanagown drunkgiggle_close at Position(ypos=1.0)
show akira basic_smile
with dissolvecharamove

stop music fadeout 4.0


"Je ramasse l'échiquier et aide Hanako à se lever. Je me sens un peu quelque peu responsable d'elle, vu que mis à part Akira, je suis probablement la personne la plus sobre dans cette pièce. Elle tient la poupée d'une main et m'offre l'autre."



show hanagown drunkgiggle_close:
    parallel:
        ease 0.5 xpos 0.45
        ease 1.5 xpos 0.55
        ease 0.5 center
    parallel:
        1.5
        "hanagown drunkgiggle_close_ni" with Dissolve(1.0, alpha=True)
show bg school_dormlilly:
    ease 1.0 xpos 0.45
show akira basic_smile:
    ease 1.0 xpos 1.0 alpha 0.0
show lilly basic_planned_paj:
    ease 1.0 xpos 0.05 alpha 0.0
with None

show bg school_girlsdormhall:
    center
    xpos 0.6
    ease 2.5 xpos 0.4
with Dissolve(1.0)

hide akira
hide lilly
with Pause(0.5)

show bg school_dormhanako_ni:
    center
    xpos 0.45
    ease 1.0 center
with Dissolve(1.0)


"Nous trébuchons à la porte, dans le couloir, et dans la chambre de Hanako. Elle s'est cognée à moi plusieurs fois aussi."

play sound sfx_switch

scene bg school_dormhanako
show hanagown drunkgiggle_close at center
with Dissolve(0.2)


"À l’intérieur de la pièce, j'allume la lumière tandis que Hanako porte son attention vers une étagère. Une élégante poupée y est assise, regardant la chambre vide."

show hanagown drunksmile_close
with charachange


ha "Voilà... tu seras bien ici..."

show ev hanako_dolls
with locationchange


"Hanako pose avec précaution la poupée à côté de l'autre et ajuste sa robe."


"Elles sont assises en silence, cheveux et vêtements parfaitement arrangés. Tout comme la théière colorée de Lilly, ça donne un contraste distinctif avec le blanc et gris de sa chambre."



show hanagown drunksmile_close:
    ease 0.25 ypos 1.05
    ease 1.0 ypos 1.0
with None

hide ev
show hanagown drunkdistant:
    ease 0.25 ypos 1.05
    ease 1.0 ypos 1.0
with charadistant


"Satisfaite que ses poupées, ses deux seules vraies possessions, soient en sécurité, Hanako fait un pas en arrière et se redresse en chancelant. Je m'avance pour l'attraper si besoin est, mais elle retrouve son équilibre sans mon aide."


"Pendant un moment, nous restons tous les deux silencieux tandis que Hanako regarde son étagère."

show hanagown drunkdistant:
    ease 1.0 xpos 0.48
    ease 1.0 xpos 0.5
    repeat
with Pause(0.5)



"Après une minute ou deux, elle commence à se balancer un peu de droite à gauche. C'est très perturbant."


hi "Ça... ça va ?"

show hanagown drunksmile at center
with dissolvecharamove


"Hanako relève la tête et se tourne vers moi comme si elle avait oublié que j'étais aussi dans la pièce."

show hanagown drunksmile_close:
    ease 1.0 ypos 1.05
with vpunch

stop music fadeout 0.3
play sound sfx_pillow


"Ce à quoi je ne m'attendais pas, c'est qu'elle fait deux pas en avant et me serre dans ses bras, posant sa tête contre ma poitrine."

play music music_heart fadein 0.5


"Je peux sentir mon cœur battre et tous mes sens revenir malgré leur affaiblissement à cause de l'alcool."


"L'odeur de vin dans son souffle, le toucher de ses doigts à travers mes vêtements, l'odeur de ses cheveux sous mon menton..."


"Mes mains restent devant moi, n'osant pas la toucher. J'ai envie de la serrer contre moi, de lui dire que tout ira bien... mais ça ne semble pas être la bonne chose à faire. Vraiment pas."


hi "Hanako..."

show hanagown drunknormal_close at Position(ypos=1.05)
with charachange


ha "Mais je veux resteeeer avec toi et Lillyyyy."


"La diction de Hanako me rappelle un peu Misha. Elle ne serait probablement pas contente que je lui dise ça."


hi "Tu sais que je ne peux pas. Tu es une fille et je suis un garçon, après tout. Et Lilly a besoin de dormir."

show hanagown drunkpout_close
with charachange


"Elle grogne en signe de mécontentement. C'est tellement étrange de la voir agir aussi librement."


hi "Ne t’inquiète pas, on se verra demain, d'accord ?"


"Je décide de poser une main sur sa tête pour la rassurer, c'est le seul contact physique que je m'accorderai à son égard tant qu'elle sera dans cet état."


"Hanako frotte son nez contre ma poitrine, comme si elle voulait encore plus se coller contre moi. Ça ne fait que m’embarrasser encore plus, et alors que ses bras se resserrent davantage, je décide d'y mettre un terme."


"Je pose mes mains sur ses épaules et la repousse gentiment. Sa prise se resserre un peu, mais elle finit par lâcher."

show hanagown drunkworry_close
with charachange


ha "Je ne veux pas que tu partes..."


hi "Hanako, s'il te plaît. Akira et Lilly vont commencer à penser des choses bizarres si je reste trop longtemps ici."


"C'est vrai. Je ne veux prendre aucun risque, et je me sens vraiment mal à l'aise maintenant."


"Je ne devrais pas essayer de réfléchir à ce qu'elle fait. J'ai lu que mis à part l'effet euphorisant de l'alcool, les gens, lorsqu'il sont soûls, peuvent avoir un comportement inhabituel, et que ça ne reflète pas forcément un désir enfoui."


"Et même sans ça, il y a plein de façons d’interpréter ce qu'elle dit. Tant qu'elle va bien, je vais essayer de partir de cette chambre le plus vite possible."

show hanagown drunkworry_close:
    ease 0.1 ypos 1.03
    ease 0.1 ypos 1.05
with Pause(0.2)


"Hanako a encore le hoquet et semble ne pas aller bien alors qu'elle se tient debout et regarde dans le vide de la chambre."


"Sa personnalité a changé au fur et à mesure qu'elle buvait, et maintenant, seule dans sa chambre avec moi, sa joie précédente semble l'avoir quittée. Est-ce qu'elle jouait juste pour s'assurer que je ne m’inquiétais pas ?"


"Même si c'est ça... qu'est-ce que je pourrais faire pour elle, vu que je fais exactement la même chose vis-à-vis de ma propre condition ?"

show hanagown drunkworry_close:
    ease 1.0 ypos 1.1 alpha 0.0
with Pause(1.0)

hide hanagown
with None


"Reprenant mes esprits, j'arrive finalement à orienter Hanako vers son lit et elle se bat un moment avec ses draps ; je ne suis pas sûr qu'elle gagne."


hi "Désolé pour ce soir, Hanako. Je sais que tu ne t'en rappelleras probablement pas, mais... joyeux anniversaire. Je suis désolé de ne pas pouvoir faire plus pour toi."


"Elle me regarde un moment. Je ne sais absolument pas si ce que j'ai dit est arrivé à ses oreilles, mais elle ferme les yeux paisiblement."

play sound sfx_switch

scene bg school_dormhanako_ni
with Dissolve(0.2)


"Je soupire de soulagement avant de repartir, éteignant la lumière au passage."

stop music fadeout 4.0

scene bg school_girlsdormhall
with locationchange


"J'hésite un peu avant de rouvrir la porte de Lilly, me demandant rapidement ce que je devrai répondre s'ils me questionnent sur Hanako. Après quelques secondes, je n'arrive pas à trouver quoi que ce soit."

scene bg school_dormlilly
show lilly basic_smileclosed_paj:
    twoleft
    ypos 1.2
show akira basic_smile:
    tworight
    ypos 1.18
with locationchange


"J'ouvre la porte et m'assure de la refermer derrière moi, au cas où un étudiant qui passe aperçoive le vin, avant de tourner mon attention vers les deux filles assises à la table basse."


"Akira sourit, tout comme Lilly. J'apprécie le changement d’humeur par rapport à celle régnant dans la chambre de Hanako."

show lilly basic_smile_paj
with charachange


li "Est-ce toi, Hisao ?"


hi "Oui. Hanako est au lit, elle dort maintenant."

show lilly basic_weaksmile_paj
with charachange


li "Tant mieux. Je dois avouer que je n'aurais pas cru qu'elle boirait autant."

show akira basic_lost
with charachange


aki "Hé, c'est pas grave. Elle va bien et est au lit maintenant. Vu comment elle est..."


"Elle s’interrompt bizarrement, mais Lilly et moi ne disons rien. Pour quelqu'un d'aussi anxieux et angoissé, boire donne une échappatoire facile à tous ces sentiments."

play music music_night fadein 4.0


"J'aimerais pouvoir faire plus pour elle. Je me sens inutile."


"Regardant Lilly, je repense à ce que je me suis demandé en ville. Ma relation avec elle est celle d'un ami et n'a jamais été autre chose, mais maintenant je sais pourquoi."


"Lilly a été là pour Hanako et moi depuis la première fois où je l'ai rencontrée, mais elle est comme ça pour tout le monde, essayant de faire son possible pour qu'ils aillent mieux."


"Avec ça à l'esprit, je me demande alors, qu'est-ce qui nous unit Hanako et moi ?"


"Après avoir sauvé notre relation de la crise d'angoisse que j'ai déclenchée en classe sans faire exprès, j'ai l'impression qu'on est redevenus amis, mais elle occupe de plus en plus mes pensées."


"Je ne peux pas dire que je pense à une autre fille de la même façon, mais peut-être que c'est juste une réaction normale face à quelqu'un agissant comme ça."


hi "Dis, Akira ?"

show akira basic_boo
with charachange

show akira basic_smile
with charachange


"Elle bâille avant de me regarder. Il se fait tard."


hi "Tu sais ce qui est arrivé à Hanako, hein ?"

show akira basic_resigned
with charachange


aki "Ouais. Lilly me l'a dit."

show akira basic_boo
with charachange


aki "Je me suis arrangée pour avoir une pause pour venir ici et rendre sa fête un peu plus joyeuse. On s'entend plutôt bien."


"C'est surprenant à entendre de la part de quelqu'un d'aussi extravertie qu'elle, mais si Hanako l'a connue via Lilly, peut-être qu'elle a eu le temps de s'habituer à Akira."

show akira basic_smile at tworight
with dissolvecharamove


aki "Et sur ce, je ferais mieux d'y aller. Je vais déjà être en retard vu l'heure qu'il est."

show lilly basic_oops_paj
with charachange


li "Mais il est déjà si tard..."

show akira basic_boo
with charachange


aki "Désolée. On a une tonne de travail à faire, donc je dois faire des heures sup'."

show akira invis:
    xpos 0.8
with dissolvecharamove


"Elle se relève avec un grognement et se dirige vers la porte. Juste avant de partir, elle se tourne vers nous."

show akira basic_lost:
    tworight
with dissolvecharamove


aki "Tu n'as pas oublié pour l'heure du vol et tout ?"

show lilly basic_smileclosed_paj
with charachange


li "Ne t’inquiète pas, tout est bon. J'aurai juste à faire mes valises au moment voulu."

show akira basic_ending
with charachange


aki "C'est bien. Bon les gars, à plus tard."

show akira invis:
    xpos 0.8
with dissolvecharamove

hide akira
with None


"Et sur ce, elle passe la porte avec la main levée en signe d'au revoir."

show lilly basic_smileclosed_paj at Position(xpos=0.5)
show bg school_dormlilly at bgright
with charamove


hi "Ta sœur c'est... vraiment quelque chose."

show lilly basic_giggle_paj
with charachange


"J'aurais probablement dû réfléchir davantage avant de dire ça. Cela dit, Lilly semble amusée par mon commentaire."


hi "Tu vas bien après avoir autant bu ? Encore sobre ou tu le caches juste bien ?"

show lilly basic_smileclosed_paj
with charachange


li "Rassure-toi, je vais bien. Je sais me modérer. Tu te maîtrises bien aussi, apparemment."


hi "Ouais, ben, on va dire que je sais me modérer aussi."


"Avec une légère hésitation, je m'assieds à la table en face de Lilly. Je veux lui dire directement, histoire de connaître le fin mot de tout ça."


hi "Je voulais te demander, mais ça m'a pris un moment pour me décider..."


hi "Tu sais ce qui a déclenché sa crise d'angoisse ? J'ai cru comprendre que c'était lié à son anniversaire, mais je n'en suis pas sûr."


hi "Même Akira était très prudente avec elle, donc j'imagine qu'elle sait aussi."

show lilly basic_reminisce_paj
with charachange


"Le sourire de Lilly s'efface, la gaieté de la fête d'anniversaire est maintenant finie."


li "Pour être honnête, je ne suis pas sûre moi-même."


li "Hanako t'a dit pour le feu de sa maison. Elle m'a dit la même chose, après qu'on ait passé beaucoup de temps ensemble."

show lilly basic_concerned_paj
with charachange


li "Outre ça... elle ne m'a jamais rien dit."


hi "Elle ne t'a jamais dit..."

show lilly basic_sad_paj
with charachange


li "Imaginant le pire, de quoi est-ce qu'elle peut se souvenir ? Une vie d'isolement et peut-être la mort de sa famille ? Allant peut-être même jusqu’à blâmer son existence pour leurs morts ?"


"Même en pensant au peu que je sais du passé de Hanako, c'est lugubre. Avoir vécu ça, vivre avec ces souvenirs, doit être vraiment ignoble."


"Lilly semble tout aussi déprimée, mais je peux voir qu'elle se ressaisit comme elle peut."


"J'ai le sentiment qu'on parle plus franchement qu'on ne le devrait grâce au vin, mais parler de ça est sûrement une bonne chose après tout."


hi "Je me sens vraiment inutile dans tout ça. Qu'est-ce que je peux faire pour elle ?"

show lilly basic_sleepy_paj
with charachange


li "Je ne suis pas vraiment sûre d'avoir raison de te dire ça, mais Hanako m'a dit que tu as été la voir la veille du jour où on est allés lui parler."

show lilly basic_weaksmile_paj
with charachange


li "Je dois avouer que je n'avais pas prévu qu'elle fasse un aussi grand pas après ce qui est arrivé, et je ne m'y attendais pas de ta part non plus. Je crois que c'était gentil à toi."


hi "Ce n'était pas grand-chose, vraiment."


hi "C'est juste... dans des moments comme ça, je pense des fois que ça serait mieux si on n'avait jamais besoin de partir de Yamaku, ou du moins de cette ville. Les choses sont plus faciles sans les autres."


"Je ne m'attendais pas à ce que Lilly soit si troublée après ce que j'ai dit, et pendant un moment elle semble perdue dans ses pensées."

show lilly basic_oops_paj
with charachange


"Elle fait mine de dire quelque chose, mais s’arrête juste avant, et réfléchit. C'est troublant."

show lilly basic_reminisce_paj
with charachange


li "Je crois..."

show lilly basic_smile_paj
with charachange


li "Dis-moi, tu as quelque chose de prévu vendredi après-midi ?"


hi "Vendredi après-midi ? Non..."


hi "Ton vol pour l’Écosse n'est pas le lendemain ? Je ne crois pas que ce soit une bonne idée que tu te fatigues avant d'y aller."

show lilly basic_weaksmile_paj
with charachange


li "Ça ira, ne t’inquiète pas pour moi. Je ferais bien ça demain soir, mais j'imagine que Hanako ne se sentira pas très bien pendant un moment."


"Imaginer comment elle sera demain me fait grimacer. Peut-être qu'on peut espérer qu'elle n'a pas fini par vomir après avoir trop bu."


hi "Bon, dans tous les cas, je serai là. On fera quoi ?"

show lilly basic_smileclosed_paj
with charachange


li "Rien d'inhabituel. Juste une petite excursion."

show lilly basic_cheerful_paj
with charachange


li "Et tu ferais mieux d'y aller, Hisao. Je pense que le couvre-feu sera bientôt là."


"Oh zut, le couvre-feu, j'avais complètement oublié."


"Je regarde l'horloge à côté du lit de Lilly, mais c'est un truc bizarre sans numéros écrits dessus. Ce qui est normal, vu le handicap de Lilly."


"Ne voulant pas risquer qu'un agent de sécurité me surprenne, je me lève et décide d'aller à ma chambre."


hi "Bon, j'imagine que je vous verrai demain, si vous arrivez à vous lever du moins."

show lilly basic_smileclosed_paj
with charachange


li "C'est gentil de t’inquiéter Hisao. À demain."

scene bg school_girlsdormhall
with locationchange


"Sur ce, je me dirige vers sa porte et me retrouve dans le couloir."


"J’espère qu'elle a une bonne idée pour la sortie."

stop music fadeout 2.0

scene black
with dissolve



label fr_H18:

scene black
with dissolve

play sound sfx_doorknock


"Un poing frappe violemment contre la porte et me donne l'impression qu'on m'enfonce un clou dans la tête."


"Une, deux, trois fois, je souffle, énervé, et garde les yeux fermés, espérant que la personne à la porte finisse par s'en aller."


"Je me sens vraiment mal. J'ai l'impression que mon visage est fait de plomb, mes bras sont lourds et je me sens nauséeux. C'est comme ça depuis une demi-heure, depuis que je me suis réveillé, et je n'arrive pas à trouver l'énergie pour me sortir du lit."


"Donc... c'est ce qu'ils appellent une gueule de bois."


"Je me demande si ce n'est pas le meilleur traitement pour les adolescents qui veulent boire comme des adultes. Vu à quel point c'est désagréable, je n'ai pas envie de réitérer l’expérience."

play sound sfx_doorknock


"Et une autre série de coups se propage dans la petite pièce. J'aimerais qu'ils s'arrêtent, je n'ai aucune intention de sortir de mon lit à cause d'eux."


"Des secondes passent, puis des minutes. Vu qu'il n'y a plus de coups à la porte, ils doivent être partis. Tant mieux."

play music music_dreamy fadein 2.0

scene bg school_dormhisao
with openeye


"Regardant mon horloge, je constate que l'heure où je vais vraiment devoir me préparer pour les cours approche. Je ne crois pas que je vais y arriver, cela dit."


"Je n'aime pas louper les cours, mais je ne crois pas que je serai capable de suivre, de toute façon. Je sais que j'ai l'air affreux sans avoir besoin de me regarder dans le miroir."

scene bg school_hallway3
with shorttimeskip


"Les gens pressés du matin me donnent suffisamment de temps pour que je puisse rester à l'extérieur de la classe un petit moment sans avoir l'air trop suspect. J’espère que Mutou ne posera pas de questions sur mon absence d'hier."


"J'étais malade, c'est bien vrai, c'est juste les raisons pour lesquelles je l'étais que je dois cacher."


"Confiant sur le fait que je peux m'en sortir en omettant certains fragments de la vérité, je rentre dans la classe en faisant de mon mieux pour avoir l'air normal."

scene bg school_scienceroom
with locationchange


"L'instant où j'ouvre la porte et fais un pas, je sens une douzaine d'yeux me regarder. Je ne l'imagine pas, ils ne font même pas l'effort de le cacher."

show hanako emb_emb:
    tworight
    ypos 1.15
with charaenter

show hanako emb_downtimid
with charachange


"Je balaye la classe du regard et je vois Hanako. Nos yeux se rencontrent momentanément, mais elle baisse vite la tête et fixe son bureau."


"Elle a vendu la mèche ? Mutou tolérerait peut-être ça, mais des mineurs qui boivent sur le campus, ce n'est pas le genre de chose qui puisse être pris à la légère."


"Je le regarde avec inquiétude."

show muto normal at twoleft
with charaenter


mu "Tu te sens mieux aujourd'hui ?"


hi "Ouais. Merci."


"Il me fait signe d'aller à ma place. Mes jambes sont raides comme des bâtons. Ça va être une longue journée."

scene bg school_scienceroom at bgleft
with shorttimeskip

stop music fadeout 2.0
play sound sfx_normalbell


"Dès que la sonnerie de midi résonne, je vais au bureau de Hanako et lui demande ce qui se passe."


hi "Hanako... tu l'as dit... ?"

show hanako emb_emb:
    center
    ypos 1.15
with charaenter


"Elle me regarde et secoue la tête. C'est déjà ça."

show hanako emb_downtimid
with charachange


ha "C'est juste..."


hi "Juste... ?"


mi "Eh bien bonjour, Hicchan. Contente de te revoir~ !"

show bg school_scienceroom at bgright
show hanako emb_downtimid:
    right
    ypos 1.15
with dissolvecharamove

show shizu basic_sparkle at center
show misha perky_smile at twoleft
with charaenter

play music music_happiness fadein 2.0


"Je grimace et me tourne vers la voix qui ne se confond pas. La voix est bien trop joyeuse pour être naturelle, même de la part de Misha."


"Que Misha sourie joyeusement n'est pas étrange. De la part de Shizune, c'est un très mauvais signe. Celui qu'elle affiche est lu dans mon esprit comme “J'ai une dizaine de chefs d'accusations contre toi”."


hi "Salut Shizune, salut Misha. Vous euh... semblez contentes de me voir."

show shizu adjust_smug
with charachange


shi "... ?"

show misha hips_grin
with charachange


mi "Tu ne te sentais pas bien hier, Hicchan~ ?"


hi "Non, non je ne me sentais pas bien. Mais je vais mieux maintenant au moins."

show shizu behind_smile
with charachange

shi "…"

show misha cross_smile
with charachange


mi "Tant mieux, Hicchan."


"Pourquoi est-ce que j'ai l'impression que Shizune m’attire dans un piège ?"


hi "On dirait que tu n'es pas complètement sérieuse."

show shizu adjust_happy
with charachange

shi "…"

show misha hips_smile
with charachange


mi "Oh non, Hicchan, nous sommes vraiment contentes que tu ailles mieux~."

show shizu basic_happy
with charachange

shi "…"


"Shizune déborde de bonheur. Il ne peut y avoir qu'une raison pour qu'elle soit comme ça. Oh non."

show misha perky_smile
with charachange


mi "En fait, on était inquiètes pour vous. Après tout..."

show misha sign_smile
with charachange


mi "Hanako, Lilly et toi étiez tous absents hier."


"Ouaip. Elle nous a eus. Il ne me reste plus qu'à déclarer forfait."


hi "J'imagine que tu as tes théories. Tu pourrais... ne le dire à personne ?"

show misha cross_smile
with charachange


mi "Il est un peu tard pour ça, Hicchan~."


"Elle a raison, vu les regards que j'ai récoltés en entrant en classe. Pourtant, ils sont plus du niveau de la suspicion que des accusations, donc on s'en sortira sûrement."

show hanako emb_downsad
with charachange


"Le visage de Hanako sombre encore un peu plus. Tant d'attention est gênant pour moi, encore plus pour elle. À en juger par les réactions de Shizune et Misha, elles l'ont remarqué aussi."

show shizu basic_angry
with charachange

shi "…"

show misha hips_frown
with charachange


mi "La seule raison pour laquelle on est si dures avec toi, c'est parce que tu nous as ignorées hier~ !"


"Hier ? Il me faut un moment pour me rappeler, étant donné l'état dans lequel j'étais à ce moment-là."


hi "Oh, c'est vrai, les coups à la porte ce matin. C'était vous ?"

show shizu behind_frown
with charachange

shi "…"

show misha cross_frown
with charachange


mi "Oui. Et tu nous as laissées poireauter pendant des décennies alors qu'on a fait l'effort de venir à ton dortoir aussi tôt le matin."


hi "Désolé. J'avais un... problème de nausée ? Un problème de nausée."


"Elles ne me croient pas. Je ne peux pas leur en vouloir."

show shizu behind_frustrated
with charachange


"La tête de Shizune tombe de résignation avant qu'elle ne cherche quelque chose dans sa poche."


"Quelque chose de blanc et jaune dépasse un peu et quand elle le sort, ça s’avère être une enveloppe avec des décorations en couleurs dessus."

show letter_insert:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)


"Elle me la tend et je la prends."


mi "C'est ce qu'on essayait de te donner, Hicchan ! Tu ne regardes pas ta..."

stop music fadeout 5.0


"La voix de Misha s'éteint alors que je lis ce qui est écrit sur l'enveloppe."

stop music fadeout 0.3


hi "Iwanako..."


"Je regarde l'enveloppe un moment, avant de soudainement me rappeler qu'il y a des gens autour de moi."

show misha cross_smile
show shizu behind_blank
show hanako emb_timid
with None

show letter_insert:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide letter_insert
with None


"Elles ont une expression très étrange, quelque peu envahissante. J'ai besoin d’être seul."

show hanako emb_sad
with charachange


ha "Iwanako... ?"


hi "Ce n'est rien. Merci de me l'avoir apportée."

show misha hips_grin
with charachange


mi "J’espère bien, après tout ce qu'on a traversé pour pouvoir te la donner~."

show misha hips_frown
with charachange


"Je recule et dis au revoir. Misha fait la moue d'une manière théâtrale alors que je passe la porte, mais Shizune et Hanako restent visiblement très curieuses au vu de ma réaction. J’espère qu'elles ne me questionneront pas plus tard."

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_parkambience fadein 2.0

scene bg school_gardens2
with locationskip

play music music_serene fadein 2.0


"L'odeur du jardin est, comme toujours, très agréable. Quelques-uns des signes les plus visibles de la richesse de l'école, en dehors de sa taille en général, sont la grandeur et l'entretien de ses jardins."


"On peut voir beaucoup d'étudiants manger, discuter, ou même jouer dans l'herbe. Même le personnel apprécie l'été ici, gardant un œil sur les étudiants tout en se baladant le long des chemins."


"Je n'ai jamais vu quelque chose comme ça dans ma ville natale. En excursions, peut-être, mais certainement pas dans l'école ou à proximité de là où je vivais."


"Même le banc sur lequel je m'assois pour lire est chaud grâce au soleil d'été et me rappelle ce pourquoi je n'ai pas encore mis le blazer de l'école depuis mon arrivée."

show letter_open_insert:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)


"En y pensant, les tournesols et la couleur jaune du papier sont plutôt appropriés vu le temps. Si seulement les mots l'étaient aussi."


"Et voilà, c'est maintenant, alors que je pensais que j'avais réussi à oublier tout ça, que cette lettre gênante arrive."


"Son écriture me paraît légèrement familière, et c'est seulement maintenant que je la revois que je me rappelle qu'elle utilisait beaucoup son stylo rose. Elle a toujours été très féminine."


"Mais elle était aussi plutôt fragile. Je n'ai jamais su si j'aimais cet aspect d'elle, bien qu'avec l'arrivée de cette lettre, la question soit devenue largement discutable."


"La lettre commence avec une banale mise à jour sur la façon dont vont les choses dans sa vie. Mon ancienne classe a eu un bon début d'année scolaire, beaucoup sont anxieux pour les examens qui arrivent, blablabla."

play sound sfx_paper

hide letter_open_insert
show letter_open_insert_2
with charachange


"Mais ça finit sur une note très personnelle. J'ai l'impression qu'elle a écrit la plus grande partie de la lettre juste pour essayer de mieux faire passer la fin."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide


$ written_note("Je voulais exprimer mes sentiments, mais les mots ne sortaient pas. Je ne pouvais rien dire pour te réconforter. Je suis vraiment désolée de ne pas avoir pu t'aider quand tu en avais le plus besoin, même si je t’appréciais tant. Au moins maintenant, finalement, je peux être honnête.\n\n\n\n")


$ written_note("Si je pouvais revenir à ces jours qu'on passait dans le silence, en février et mars, je te dirais de ne pas abandonner. C'est ce que je dirais. Peut-être que tu n'aurais pas dérivé si loin si j'avais dit quelque chose. J’espère que tu as réussi à te remettre sur pied par toi-même.\n\n\n\n")


$ written_note("Maintenant que la distance entre nous est aussi physique, ça me semble définitif. Je me demande si on se reverra. Peut-être que c'est mieux si on ne se revoit pas. Si tu veux correspondre avec moi, écris-moi par tous les moyens possibles. J'aimerais beaucoup entendre parler de ta nouvelle école et de comment tu vas. Je ne te souhaite que le meilleur.\n\nSincèrement, Iwanako")

window show

$ renpy.music.set_volume(1.0, 1.0, channel="music")


"Et donc, voilà. Notre relation est terminée. Clair, propre et sans ambiguïté."


"Je n'étais pas dans l'illusion qu'on puisse être réunis un jour. La dernière fois qu'elle est venue me voir, aucun d'entre nous n'a ouvert la bouche, en dehors des derniers mots qu'elle a dit avant de partir : “Au revoir.”"


"Mais comme ça... ça ressemble plus à une fin. Le point final d'une expérience qu'on a voulu faire, et pour laquelle on a échoué."

show letter_open_insert_2:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide letter_open_insert_2
with None


"Un cri détourne mon attention de la lettre. C'est juste des étudiants qui font les idiots et un professeur s'approche d'eux pour leur parler."


mystery "Est-ce que ça va ?"

show yuuko neutral_down at center
with charaenter


"Une petite voix s'approche de moi. Pendant un moment je pensais que c'était Hanako, mais il s'avère que c'est Yuuko."


hi "Oh, bonjour Yuuko. Je pensais que tu serais à la bibliothèque."

show yuuko closedhappy_up
with charachange


"Elle m'adresse un grand sourire, un de ceux qui correspondent à l’atmosphère, et brandit un emballage de repas dans sa main. Quelqu'un a dû la remplacer pendant qu'elle est allée chercher à manger."


"Ça me rappelle que je n'ai rien mangé encore. Je n'ai pas spécialement faim cela dit, et sauter un repas ne me fera pas de mal."

show yuuko smile_up
with charachange


yu "La place est libre ?"


hi "Bien sûr, vas-y."

show yuuko neutral_down at Position(ypos=1.15)
with dissolvecharamove


"Je remets rapidement la lettre dans l'enveloppe, la glisse dans mon sac qui est contre le banc alors que Yuuko s'assoit à côté de moi. Elle met son emballage dans la poubelle à côté de nous."


"Sans grand-chose à faire, je m'adosse au banc et apprécie le soleil, réfléchissant à la lettre."


"Les jardins luxuriants, le ciel bleu clair... tout semble si différent ici. Même les environs, avec la colline et la forêt qui l'entoure sont complètements opposés à la scène urbaine dont je me rappelle."


"Peut-être que c'est comme le mal du pays. Encore une fois, ce n'est pas si mal ; les environs autour de Yamaku, bien que très différents, sont plutôt agréables. Je pourrais m'y habituer."

show yuuko smile_down
with charachange


yu "Dis, Hisao ?"


hi "Ouais ?"

show yuuko worried_down
with charachange


yu "Tu n'as pas répondu à ma question. Je ne comptais pas t’embêter, mais tu sembles troublé."

show yuuko panic_up
with charachange


yu "Si tu ne veux pas en parler, ce n'est pas grave, ça ne me gêne pas. Hum, d-désolée de demander quelque chose d'étrange comme ça..."


hi "Ça ne me gêne pas."


hi "C'est juste que... j'ai reçu une lettre de quelqu'un que je connaissais avant de venir à Yamaku. Ça m'a fait réfléchir à certains trucs."


hi "Je croyais que je réussirais à surmonter la plupart des problèmes qu'a causés mon accident, mais maintenant je ne sais pas vraiment. J'aurais préféré ne pas la recevoir."

show yuuko worried_up
with charachange


yu "Ce n'est pas une bonne chose, Hisao."

show yuuko neutral_down
with charachange


yu "Quand mon petit copain m'a quittée, il l'a fait très soudainement et ne m'a jamais dit pourquoi. Au début j'étais très déprimée, mais j'ai décidé de lui pardonner."


hi "Tu lui as pardonné ? Il n'aurait pas pu t'en parler simplement ?"


yu "Il a toujours été de ces gens qui ont du mal à se rapprocher des autres."


yu "En fin de compte, j'ai décidé que j'étais tombée amoureuse de lui pour une raison, il était quelqu'un de bien, et je crois que si j'avais été dans sa position, j'aurais sûrement eu du mal à aller lui parler."


hi "Je ne... vois pas vraiment le lien avec ma lettre."

show yuuko worried_up
with charachange


yu "Je veux dire que... euh, comment dire ça..."


yu "Ça a dû être très dur pour cette personne d'envoyer la lettre, et en plus, je crois qu'elle a dû avoir beaucoup de mal à trouver quoi dire."


"Iwanako a réussi à envoyer une lettre et à mettre fin à notre relation, quelque chose que je n'ai jamais réussi à faire."


"Tandis que moi, j'essaye de protéger Hanako comme je peux, surtout maintenant que Lilly va partir un moment, et je ne suis même pas capable de gérer mes propres problèmes."

show yuuko neutral_down
with charachange


yu "C'est logique au moins ce que je dis ?"


"Elle a pris le fait que je ne réponde pas comme un doute. Elle est vraiment trop attentive aux expressions des gens, à l'instar d'une certaine autre personne."


hi "Oui, c'est logique."


hi "La lettre était un choc, vraiment. J'ai essayé de me persuader que ma vie avait été remise à zéro quand je suis arrivé à Yamaku, mais je sais que ce n'était pas le cas. Je suis un peu perdu, je ne sais pas comment gérer ces sentiments."

show yuuko worried_down
with charachange


yu "Je ne pense pas pouvoir t'aider pour ça. Désolée."


hi "C'est bon. Je crois que parler avec toi m'a aidé à rendre les choses un peu plus claires, donc merci quand même."

show yuuko closedhappy_down
with charachange


"Elle hoche la tête et sourit. Yuuko est une gentille fille, dommage qu'elle angoisse si facilement."

play sound sfx_warningbell

show yuuko panic_up
with vpunch


"La sonnerie nous surprend tous les deux."


yu "Ah, j'étais censée être de retour avant la sonnerie !"


hi "Oups..."

show yuuko worried_up at center
with Dissolvemove(0.3)


"Elle se lève du banc et se met presque à courir sans dire un mot, mais elle se retourne, se rappelant que je suis là."

show yuuko neutral_up
with charachange


yu "À plus tard Hisao, courage, hein ?"


hi "J'essayerai. Merci, Yuuko."

stop music fadeout 9.0

hide yuuko
with charaexit


"Après une petite courbette, Yuuko se précipite en direction de la bibliothèque. Sa ruée attire l’œil de quelques étudiants qui sont en chemin vers leurs classes."


"Me levant sans énergie du banc, je suis leur exemple."


"Même alors que je traverse les jardins sur le chemin du bâtiment principal, je garde la lettre en tête."

stop ambient fadeout 2.0
stop music fadeout 2.0

scene black
with dissolve



label fr_H19:

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_traffic fadein 1.0

scene bg city_street2_ni
with locationchange


"Parcourir les rues de la ville me rend nostalgique. Alors que Yamaku peut être l'inverse de là où j'ai vécu dans le passé, la nuit, la ville m'est très familière."


"Mes yeux jonglent constamment entre les écrans brillants sur les immeubles, les lampadaires, les businessmen qui décompressent après le travail et les couples qui sont en rendez-vous."


"Même si je ne le voulais pas, je ne peux pas m’empêcher d'être imprégné par tous les aspects de la ville. Je savoure sa familiarité comme un bonbon sur la langue."

show akira basic_boo_ni:
    center
    xpos 0.59
show lilly cane_smileclosed_cas_ni:
    center
    xpos 0.41
with charaenter


"Lilly marche à ma gauche avec sa canne qui se balance, tenant le bras de sa sœur tout en lui parlant."


"En comparaison du taxi ou du bus, être conduit par Akira dans sa belle voiture était plutôt agréable."

show hanako invis_close:
    center
    xpos 1.0
with None

scene bg city_street2_ni at bgleft
show akira basic_boo_ni:
    center
    xpos 0.39
show lilly cane_smileclosed_cas_ni:
    center
    xpos 0.21
show hanako basic_distant_cas_close_ni at tworight
with dissolvecharamove


"Peut-être pas pour la personne à ma droite, cela dit. Alors que Lilly est habituée au style de conduite de sa sœur et que moi, j'apprécie un peu l'excitation, Hanako s'est tenue très fort à la porte pendant la durée du voyage."

show hanako basic_smile_cas_close_ni
with charachange


ha "T-tout semble si b-beau la nuit..."

show hanako emb_downtimid_cas_close_ni
with charachange


"Hanako baisse rapidement les yeux après avoir croisé le regard de quelqu'un."


hi "Ouais, c'est vrai."


"Ma réponse n'est pas très inspirée, vu que je suis distrait par mes pensées."


"Une de ces distractions, à part la vue de la ville, est Hanako."


"C'est la première fois que je la vois autrement que dans son uniforme scolaire ou en pyjamas. Je me suis arrêté sur place une seconde quand je l'ai vue, à la porte de l'école."


"Vu la façon dont sa tête est baissée quand elle marche à côté de nous, j'imagine que le chapeau qu'elle porte est plus qu'un accessoire de mode."


"Bien qu'à l'origine j’étais sceptique face au plan de Lilly de nous emmener en ville, maintenant que la nuit est tombée, il est évident qu'elle a réfléchi. Peu de gens font attention à Hanako, vu que la nuit cache plutôt bien ses cicatrices."


hi "Donc... on est en ville. Une idée de quoi faire ?"

show akira basic_smile_ni
with charachange


"Akira affiche un grand sourire. Quelque chose me dit que c'est elle qui a pris cette décision, même si c'est sa sœur qui a proposé la sortie à la base."

show akira basic_ending_ni
with charachange


aki "Tu verras. Suis-nous."


"Je hoche la tête et fais de mon mieux pour retenir une grimace. Après ce qui est arrivé à l'anniversaire de Hanako, je n'ai pas tellement confiance dans le jugement d'Akira."

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
$ renpy.music.set_volume(0.1, 0.0, channel="music")
play music music_jazz fadein 14.0

scene bg city_street3_ni
with locationchange


"Nous continuons de marcher et je remarque que nous passons devant de plus en plus de cafés, restaurants, et autres endroits où manger."


"De temps en temps nous croisons un homme ivre en costume sortant d'un bar, généralement supporté par un autre, mais la plupart des clients ici semblent jeunes et branchés."


"Différents types de musiques affluent alors que nous marchons. Le bruit constant des musiques qui se superposent devrait être usant, mais ça me rappelle l'époque où j'allais en ville avec mes vieux amis alors ça ne me gêne pas."


"Hanako et moi avons commencé à nous décaler un peu de Lilly et Akira. Une dérive qui s’arrête quand j’entends un petit choc à côté de moi."

show hanako defarms_shock_cas_ni
with vpunch


ha "D-d-désolée... !"


"Au moment où elle se redresse de sa courbette d'excuse, le businessman d'âge moyen contre lequel elle s'est cognée est déjà en train de partir après s’être à moitié excusé."

show hanako emb_downtimid_cas_ni
with charachange


"Hanako semble un peu perturbée par l'expérience, et alors qu'elle accélère pour me rattraper, je remarque qu'elle a la tête encore plus basse. Elle lui est sûrement rentrée dedans parce qu'elle regardait ses pieds et non là où elle allait."

show hanako emb_timid_cas_close_ni
with charachange


"Je me décale un peu sur le côté et mets une main sur son épaule droite, la rapprochant un peu plus de moi."


ha "Hisao ?"


hi "Ça va. Tu peux marcher plus près de moi si tu veux."

show hanako emb_smile_cas_close_ni
with charachange


"Hanako hésite, mais finit par hocher la tête."

stop ambient fadeout 1.0
$ renpy.music.set_volume(0.5, 10.0, channel="music")

scene bg city_karaokeext_ni
show crowd_ni
show akira basic_smile_ni:
    center
    xpos 0.39
show lilly cane_listen_cas_ni:
    center
    xpos 0.21
show hanako basic_smile_cas_close_ni at tworight
with locationskip

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_crowd_outdoors fadein 2.0


"Après quelques fois où j'ai pensé qu'on était à destination, nous arrivons vraiment. Nous sommes maintenant sortis des rues les plus fréquentées et actives du quartier."


"Je suis un peu surpris. L'âge moyen des gens ici est plutôt élevé et il y a une forte odeur de cigarette. La zone est loin d’être miteuse cela dit et c'est amusant de voir la réaction de Lilly à l'odeur de la fumée."


"Bien que ce soit masqué par le bruit des gens qui parlent, de la musique jazz peut être entendue de l’intérieur. En regardant la devanture, je comprends pourquoi."


hi "Un club de jazz. Je dois admettre que je ne m'y attendais pas."

show lilly cane_giggle_cas_ni
with charachange


"Lilly rit un peu et sourit."

show lilly cane_smileclosed_cas_ni
with charachange


li "D'une certaine façon, j'ai l'impression que j'aurais dû m'y attendre, Akira."


"Alors que nous discutons à l'extérieur, je remarque de plus en plus de regards dans notre direction. Des gens nous regardent et se tournent vite, mais ça rend la chose encore plus évidente."


"J'ai remarqué ça de temps en temps pendant que nous marchions, mais maintenant c'est plus fréquent."


"Ça ne m'était jamais arrivé avant. Je suis un jeune adulte japonais, juste légèrement plus grand que la normale, je n'attire pas l'attention normalement."

show akira basic_laugh_ni
with charachange


aki "Hé, allez, ce n'est pas juste parce que vous êtes jeunes que vous ne pouvez pas apprécier, hein ?"


hi "Euh... Je n'ai rien contre la musique, si c'est ce que tu veux dire."

show hanako cover_bashful_cas_close_ni
with charachange


ha "Ç-ça... ne me gêne pas... non plus..."


"Elle réussit à peine à sortir ces mots. Ça change beaucoup de quand on est seuls à Yamaku et je suis un peu déçu qu'elle soit aussi tendue pour ce qui est censé être un moment agréable en ville."


"C'est difficile de voir le visage de Hanako, vu qu'elle a la tête baissée. Ça ne m'étonne pas qu'elle n'aille pas souvent en ville, et quelque part je suis content que mes propres cicatrices ne soient pas aussi visibles."


"Lilly attire aussi les regards des gens, mais la raison est clairement différente. Elle n'a pas l'air du tout japonaise et cela vaut aussi pour sa sœur. De loin, ça se voit beaucoup plus que sa cécité."


"Elle n'est peut-être pas capable de le voir elle-même, mais je ne doute pas qu'elle puisse entendre les phrases murmurées des gens qui la voient alors qu'ils pensent qu'elle ne peut pas entendre."


"Mais dans tous les cas, ça ne semble pas la gêner."

hide akira
hide lilly
with charaexit


"Akira est toujours aussi confiante, cela dit. Avec un grand sourire, elle avance avec Lilly et nous suivons tous les deux."

stop ambient fadeout 1.0
$ renpy.music.set_volume(1.0, 10.0, channel="music")

scene bg city_clubint:
    center
    xpos 0.6
show crowd
with locationchange

$ renpy.music.set_volume(0.8, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 1.0


"J'aurais pensé que mes yeux auraient besoin de s'ajuster à la lumière à l'intérieur, mais il ne fait pas bien plus clair qu'à l'extérieur."


"La musique que nous entendions est bien plus audible maintenant, mêlée au bruit des verres et des discussions des clients. En regardant à ma droite, je vois l'origine de la musique, un groupe de jazz joue derrière quelques tables."


"La clientèle est surtout composée d'hommes, et bien qu'il y ait quelques femmes, personne n'a l'air d'avoir en dessous de trente ans. À part nous, bien sûr."


"J'ai un peu l'impression d'être arrivé dans les années 1920 et l’atmosphère est assez agréable. Je ne suis pas totalement à l'aise à cause de mon âge, mais si j'étais plus vieux, je me sentirais sûrement comme à la maison."

show hanako basic_smile_cas_close at tworight
with charaenter


"Hanako semble un peu plus relaxée maintenant, probablement parce que personne ne la regarde. Tout le monde est en train de discuter, boire, ou regarder le groupe."

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

show akira basic_smile behind crowd:
    center
    easein 1.0 ypos 1.06
hide crowd
with Dissolve(1.0)


"Akira prend un siège au bar sans même jeter un œil aux environs. Elle est sûrement déjà venue auparavant."

show lilly basic_smileclosed_cas:
    twoleft
    xpos 0.25
    easein 1.0 ypos 1.1
with Dissolve(1.0)


"Lilly rétracte sa canne, trouve le tabouret du bar et s'assied à côté de sa sœur. Le barman leur jette un regard pendant qu'il nettoie un verre, puis le pose pour aller les voir."


"Barman" "Bonsoir mesdames. Qu'est-ce que ce sera ?"

show akira basic_ending:
    center
    ypos 1.06
with charachange


aki "Juste un scotch, merci. Lilly ?"

show lilly basic_cheerful_cas:
    twoleft
    xpos 0.25 ypos 1.1
with charachange


li "Pourrais-je avoir un verre de cham—{w=0.5}{nw}"

show lilly basic_surprised_cas
show akira basic_boo
with vpunch


"Un coude en costume noir l'atteint aux côtes."

show lilly basic_weaksmile_cas
with charachange


li "Jus d'orange, s'il vous plaît."


"Barman" "Pas de problème, ça arrive tout de suite."


"Le barman commence à préparer leurs verres. Quelques secondes passent avant qu'Akira se rappelle que Hanako et moi sommes là et se tourne vers nous."

show akira basic_smile
with charachange


aki "Vous voulez quelque chose, ou vous allez rester debout ?"


"Hanako semble être un peu agitée. Peu importe où nous pouvons nous asseoir, il y a des gens à côté d'elle et je ne pense pas qu'elle puisse se faire passer pour une majeure, contrairement à Lilly."

show bg city_clubint:
    xpos 0.4
show akira basic_smile:
    xpos 0.3
show lilly basic_weaksmile_cas:
    xpos 0.05
show hanako basic_smile_cas_close:
    xpos 0.5
with charamove


"Regardant autour de moi, je vois un coin de jeu à notre droite. Il y a quelques tables de billards et personne ne les utilise."


"Je regarde Hanako dans l'intention de lui demander si elle veut jouer, mais elle est déjà en train de les regarder avec envie. Peut-être qu'il n'y a pas besoin de mots, après tout."


hi "On va jouer au billard là-bas."

show akira basic_boo
with charachange


"Akira se penche en arrière pour voir derrière moi, avant de hausser les épaules et de se repositionner."

show lilly basic_giggle_cas
with charachange


li "On dirait que tu vas devoir te contenter de moi. Comme c'est dommage."

show akira basic_smile
with charachange


aki "Amusez-vous bien."

$ renpy.music.set_volume(0.8, 1.0, channel="music")
stop ambient fadeout 14.0

hide hanako
with charaexit


"Nous nous tournons et allons vers le coin abandonné, Hanako ouvrant la marche."


"L'idée d'une bonne partie en silence loin de tout le monde l'aide à marcher plus vite. Ses yeux sont fixés sur son objectif."

scene bg city_clubpool
with locationchange


"La grande table est bien éclairée malgré les environs sombres, grâce aux néons au-dessus. Une grande peinture de... quelque chose... couvre le mur."


"Il n'y a pas grand-monde qui passe dans ce coin du club, et je peux voir Hanako devenir moins tendue."

show hanako basic_smile_cas at center
with charaenter


ha "Tu... s-sais comment jouer ?"


hi "Je ne suis pas un expert, mais ouais, je sais."

show hanako basic_bashful_cas
with charachange


ha "Alors euh... le jeu de la huit ?"


hi "Ok."

hide hanako
with charaexit


"Hanako prend le talc et deux queues posées sur des crochets sur le mur pendant que je sors les boules des poches de la table et attrape le triangle sur l’étagère en dessous."


"Elle attend patiemment que j'installe la table. Après avoir mis la dernière boule dans le triangle, je me retrouve à devoir me battre avec mon perfectionnisme qui exige que la dernière rangée de boules soit exactement perpendiculaire aux bords."


"Les boules disposées et prêt à jouer, je me recule et prends la queue que me tend Hanako. Je regarde rapidement le bout pour vérifier qu'il est en bon état."


hi "Tu as déjà joué auparavant ?"

show hanako cover_bashful_cas
with charaenter


ha "Une fois... ou deux. Je c-connais juste... les règles."

$ renpy.music.set_volume(0.5, 1.0, channel="music")


"L'ambiance entre nous deux est un peu bizarre. Elle est toujours assez nerveuse. Compréhensible, vu qu'on est en public."


"Finalement, le silence est de trop, même pour Hanako, et elle commence à parler en bégayant."

$ renpy.music.set_volume(0.8, 1.0, channel="music")

show hanako basic_worry_cas
with charachange


ha "Qu-qui va... c-casser ?"


"Je réfléchis un moment avant de sortir une pièce de ma poche."


hi "Je prends face, tu as pile."


"Après un hochement de tête de la part de Hanako, je lance la pièce, l'attrape, et la retourne sur le dos de ma main gauche."


hi "On dirait que c'est toi qui casses."

$ ksgallery_unlock("ev hanako_billiards_distant")
scene ev hanako_billiards_break
with locationchange


"Hanako hoche encore une fois la tête, avant de se mettre au bout de la table."


"Elle n'est pas aussi silencieuse d'habitude avec moi, je me demande si c'est parce qu'on a évoqué son passé."

scene bg city_clubpool
with flash


play sound sfx_billiards_break


"Elle recule d'une manière entraînée avant de donner un coup au centre de la boule blanche. Elle traverse le tapis vert avant de percuter les boules soigneusement disposées à l'autre bout."


"Les boules s'éparpillent sur la table à grande vitesse. Elle a bien cassé et les boules sont bien distribuées sur la table. Mes yeux passent déjà de l'une à l'autre pour voir laquelle sera la plus facile à rentrer."

play sound sfx_billiards


"Hanako se recule et je tape la boule."

show hanako basic_smile_cas at center
with charaenter


ha "Bien joué."


"C'est seulement après le commentaire de Hanako que je réalise que la boule que j'ai frappée est dans une poche."


"Je la regarde et remarque un petit sourire sur son visage. C'est agréable de voir que jouer la détend un peu."


hi "J'imagine que je prends les rayées alors."

show hanako cover_distant_cas
with charachange


"Je recule d'un pas et la laisse faire son tour, mais elle n'avance pas. À la place, elle regarde par terre et se frotte le bras."


"Maintenant je peux identifier sa gestuelle comme une de celles qu'elle a quand elle veut dire quelque chose, mais n'est pas assez confiante pour le faire."


hi "Qu'est-ce qu'il y a ?"

show hanako cover_bashful_cas
with charachange


ha "C'est juste... que tu as un... grand s-sourire. Tu aimes... jouer au billard ?"


"Je soupire et m'adosse à la table."


hi "J'aime bien y jouer, ouais. Je crois que je souriais parce que j'étais nostalgique."

show hanako def_worry_cas
with charachange


"Hanako penche la tête d'un air interrogateur."


hi "Mes amis et moi jouions au billard dans les salles d'arcade pas loin de là où nous vivions avant, même la nuit."

show hanako basic_worry_cas
with charachange


ha "M-mais tes parents..."


hi "Mes parents travaillaient tous les deux, alors ils ne me disaient rien si je n'étais pas à la maison. Je faisais mes devoirs sans trop de problèmes, donc j'avais le temps de faire d'autres trucs."

show hanako basic_distant_cas
with charachange


"Notre conversation s’arrête là, la timidité de Hanako l’empêchant de continuer. En réponse, je me pousse pour la laisser jouer."


scene ev hanako_billiards_smile
with locationchange


"Il n'y a pas de coups faciles, alors Hanako se penche et prend un moment pour s'aligner."

scene ev hanako_billiards_smile_close:
    truecenter
    zoom 1.0 subpixel True
    easein 6.0 zoom 0.8
with flash


"L'expression de Hanako est la même que lorsque nous jouons aux échecs, relaxée et concentrée à la fois. Les athlètes parlent parfois d'un moment où rien de ce qui n'est pas nécessaire ne les perturbe, je me demande si elle est dans cet état-là."


"Sa posture est bonne. Meilleure que la mienne, en tout cas. Très proche d'une méthode d'un manuel de jeu, alors que moi j'ai l'habitude de me mettre dans la position la plus naturelle que je puisse trouver."

scene ev hanako_billiards_serious
with locationchange


"Elle aligne la queue sur son objectif, elle la recule un peu et fait quelques mouvements pour s'assurer qu'elle est bien positionnée."


"Hanako prend le jeu au sérieux. C'est le seul vrai hobby que je lui connaisse, à part la lecture. C'est agréable de partager ce genre d'expérience avec elle."

scene bg city_clubpool
with flash

play sound sfx_billiards


"Elle envoie le coup après avoir visé et la boule frappée vient se heurter à une boule attendant dans un angle proche d'un coin."


"Les préparations de Hanako paient quand la boule roule en direction de la poche. Pendant un moment on dirait qu'elle va s’arrêter au bord du trou, mais elle tombe finalement."


hi "Eh bien, il était dur ce coup-là. Si tu peux réussir ça, je ne pense pas avoir mes chances."

show hanako emb_emb_cas at center
with charaenter


ha "Je ne suis pas... a-aussi bonne..."


hi "Ce n'est pas juste ce coup, même quand tu t'alignes, tu sembles très sérieuse. Comme quand tu joues aux échecs."

show hanako emb_downsmile_cas
with charachange


"Le compliment la fait un peu rougir. Elle pose la queue contre la table et se redresse, avant de se tourner vers moi."


ha "C'est juste... que j'aime bien ça..."


"Elle gigote avec ses mains et ses doigts."

show hanako emb_downtimid_cas
with charachange


ha "Quand j'étais à l'orphelinat... j'ai juste... c-continué de faire les choses que j'aimais... avant."


ha "Si je j-jouais avec les autres, c-c'était suffisant pour les adultes là-bas, alors..."


"Je n'y ai jamais pensé comme ça. Le personnel d'un orphelinat voudrait que tout le monde socialise un peu."


hi "Si ça te gêne pas trop de me dire... comment c'était à l'orphelinat ?"

show hanako emb_sad_cas
with charachange


ha "P-pourquoi tu veux savoir ?"


"J'ai touché quelque chose de sensible, mais le fait qu'elle réponde est déjà positif. Avant, elle serait sûrement partie sans dire un mot."

show hanako emb_blushing_cas
with charachange


ha "Je vais... te le dire, mais..."


hi "Mais... ?"

show hanako cover_worry_cas
with charachange


ha "Tu peux... m-me dire qui est I-Iwa... n-nako... ?"

$ renpy.music.set_volume(0.2, 1.0, channel="music")


hi "Iwanako... ? Oh, la lettre."


"Je me demande depuis combien de temps elle attendait la bonne opportunité pour me le demander. Je suis surpris, mais n'hésite pas. Partager les informations est normal."

$ renpy.music.set_volume(1.0, 8.0, channel="music")
$ renpy.music.set_volume(0.4, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 8.0


hi "C'est... quelqu'un que j'aimais."

show hanako basic_normal_cas
with charachange


"Sa nervosité a disparu, du moins pendant le temps que ça lui a pris de demander. Sa curiosité la domine et je me sens un peu mal d’être interrogé comme ça."


"Il n'y a pas moyen que je puisse raconter mon histoire avec Iwanako ici. Je ne sais pas moi-même ce que je pense de tout ça, même après avoir parlé à Yuuko, et je veux éviter le sujet avec Hanako."

show hanako def_worry_cas
with charachange


"Hanako ne semble pas vraiment satisfaite par cette étrange fin de discussion, mais je préfère ne pas continuer. Elle a à peine réussi à me demander, sans savoir si je voulais en parler ou non."


"Je me mets en place pour jouer mon tour. Le manque de discussion entre nous deux est comblé par le bruit des clients et du groupe dans le club."

hide hanako
with charaexit


"Trouvant une action qui ne semble pas trop difficile, je tente mon coup."

play sound sfx_billiards


"Je frappe la boule et la trajectoire est bonne, mais j'y ai mis trop de force. La boule frôle le trou et passe à côté."


"Je grince un peu des dents. J'étais assez bon avant, c'est frustrant d'avoir autant perdu."


"Je recule et laisse son tour à Hanako, jetant un œil là où se trouvent Lilly et Akira. Elles discutent entre elles et semblent bien s'amuser."

scene ev hanako_billiards_serious
with locationchange


"Je me tourne vers Hanako alors qu'elle joue son coup. Avec la même expression qu'avant, elle s'aligne et frappe."

scene bg city_clubpool
with flash

play sound sfx_billiards


"Tout comme avant, elle fait tomber la boule qu'elle visait. Elle tombe dans la petite poche plus proprement que sa précédente, cela dit. On dirait qu'elle se met un peu plus dans l'ambiance du jeu."


hi "Bien joué."


"Elle hésite un moment et commence à me parler sans tourner la tête."

scene ev hanako_billiards_smile_med
with locationchange


ha "L'orphelinat... était bien. C'était un peu comme Yamaku... et le personnel était v-vraiment gentil."

show ev hanako_billiards_distant_med
with charachange


ha "Mais alors que l-les années passaient, j'ai réalisé quelque chose. J'étais d-différente."


"Ça fait bizarre de la voir parler si librement d’elle-même. Elle se force visiblement. Ça me rappelle quand elle a insisté pour me dire pour le feu."


"Hanako doit penser qu'elle doit me dire tout ça si elle veut que je lui parle de mon passé."


"Sa prise sur la queue se resserre alors qu'elle continue de parler."

$ ksgallery_unlock("ev hanako_billiards_timid")
show ev hanako_billiards_timid_med
with charachange


ha "L-la plupart des enfants étaient là pour se faire adopter, tout comme moi. Mais contrairement à moi... ils sont partis, u-un par un. Au moment où je suis arrivée à Yamaku, j'étais... parmi les plus vieux enfants là-bas."


ha "Pendant un moment, j'ai-aidais des enfants p-plus jeunes, m-mais finalement..."

scene bg city_clubpool
with locationchange


"Je pose une main sur son épaule. Elle se force maintenant."


hi "C'est bon."

show hanako emb_blushtimid_cas_close at center
with charaenter


"Elle semble légèrement surprise un moment, puis hoche la tête avant de poser la queue et de se tourner vers moi."

show hanako basic_worry_cas_close
with charachange


ha "Tu... penses vraiment ?"


hi "Oui, ne t’inquiète pas. Même quand Lilly ne sera plus là, je serai là pour te protéger, d'accord ?"

show hanako basic_normal_cas_close
with charachange


"Hanako me regarde un long moment et je suis un peu pris par surprise."


"Son expression n'a pas changé par rapport à avant, ayant l'air quelque peu larmoyante, et le silence qui règne entre nous n'est pas inhabituel. Je crois que c'est le fait qu'elle me fixe aussi longtemps qui est bizarre."


"J'ai l'impression qu'elle me juge. C'est très étrange et assez inconfortable."


hi "Hanako... ?"

show hanako cover_smile_cas_close
with charachange


ha "J-je comprends. Merci."


"Elle sourit et détourne un peu le regard, mais semble toujours gênée. Hanako n'est pas très bonne pour faire semblant, et le moment présent ne déroge pas à la règle."

hide hanako
with charaexit


"Je vais à la table et joue mon tour pour essayer de me distraire, mais ça ne semble pas marcher. Est-ce qu'elle croit que je ne suis pas à la hauteur ? Est-ce que je la déçois ?"


"J'y réfléchis probablement trop. Bien que j'aie appris à accepter son silence, des fois j'aimerais qu'elle parle plus."

play sound sfx_billiards


"Avec un 'poc', j’envoie la boule blanche traverser la table vers ma cible."

show hanako def_strain_cas at center
with charachange

ha "Ah…"


"Hanako voit ce qui arrive tout comme moi. La boule frappe fort l'autre, et la boule rayée que je voulais mettre vire vers la boule huit."


"Alors que Hanako et moi regardons et nous mordons la lèvre, la boule se cogne à la noire et l'envoie se loger dans une poche dans le coin."

show hanako basic_smile_cas
with charachange


"Je soupire. On dirait que Hanako sourit de nouveau, donc peut-être que ce n'était pas pour rien."


hi "C'était un mauvais tir, tu as gagné. On dirait que je suis plutôt rouillé après tout ce temps."

hide hanako
with charaexit


"Hanako se penche et commence à envoyer les boules restantes dans les poches les plus proches. Je lui demanderais presque si elle veut faire une autre partie, mais un coup d’œil rapide à ma montre me confirme qu'il est plutôt tard."


"Lilly et Akira semblent être toujours en train de boire au bar. On va devoir aller les chercher."


ha "Hum, Hisao..."

scene ev hanako_billiards_distant
with locationchange


"Je me retourne vers Hanako, qui est toujours au billard en train de finir les boules. Sa voix semble différente d'avant."

scene ev hanako_billiards_smile
with charachange


ha "Je suis... là pour toi aussi..."

stop ambient fadeout 2.0

hi "Ah…"


"Je rougis soudainement. C'est normal qu'elle me réponde ça, vu ce que j'ai dit plus tôt, mais c'est quand même un choc de l'entendre."

scene ev hanako_billiards_smile_close:
    xalign 0.0 yalign 0.0 zoom 0.8 subpixel True
    acdc_warp 20.0 zoom 1.0
with locationchange


"Quelle est ma relation avec cette fille ? Je veux la protéger, la rendre heureuse... Je ne suis pas sûr que ce soit de l'amour, mais je ne pense pas que ce soit la même chose que ce que je ressens pour Lilly non plus."


"Je me sens désolé pour elle, qui a vécu tant de choses dans sa vie. Ses parents sont morts dans le feu de sa maison et elle a passé la plus grande partie de son enfance dans un orphelinat... Je ne peux même pas imaginer le genre de vie qu'elle a vécue."


"Mais j'ai l'impression de ne presque rien pouvoir faire pour elle, surtout maintenant que Lilly va quitter le pays."

stop music fadeout 10.0

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_traffic fadein 4.0

scene bg city_karaokeext
show akira basic_boo_ni:
    center
    xpos 0.39
show lilly cane_smileclosed_cas_ni:
    center
    xpos 0.21
show hanako basic_normal_cas_close_ni at tworight
with locationskip


"Hanako et moi finissons de ranger la table et les queues, et nous passons chercher Lilly et Akira avant de sortir du club."


"J'ai l'impression que quelque chose a changé entre Hanako et moi. Je ne sais pas tellement ce que c'est, mais Hanako agit différemment maintenant. Comme si on était plus éloignés, ou quelque chose comme ça."

show akira basic_smile_ni
with charachange


aki "Donc, vous vous êtes amusés ?"

show hanako emb_smile_cas_close_ni
with charachange


"Hanako et moi hochons tous deux la tête. La partie était bien et nous en avons tous les deux appris plus l'un sur l'autre, donc c'est une réponse honnête."

show lilly cane_sleepy_cas_ni
with charachange


"Lilly semble être un peu distraite."


hi "Inquiète pour ton voyage, Lilly ?"


"Elle s’arrête avant de soupirer et de sourire faiblement."

show lilly cane_weaksmile_cas_ni
with charachange


li "Un peu. Ça signifie beaucoup."

show akira basic_laugh_ni
show lilly cane_surprised_cas_ni
with vpunch


"Ce commentaire est ponctué par une tape sur l'épaule de la part de sa sœur. Hanako lui sourit, aussi."

show hanako basic_smile_cas_close_ni
with charachange


ha "Ça ira, Lilly. J’espère que tu apprécieras ton temps là-bas."

show lilly cane_smile_cas_ni
with charachange


li "Merci, Hanako, j'essayerai. Ce sera bien de rejoindre ma famille après tout, même si c'est pour peu de temps."


"Sur ce, nous commençons notre marche en direction de la voiture d'Akira. Nous continuons de discuter, mais surtout de tout et de rien."

stop ambient fadeout 2.0
stop music fadeout 2.0

scene black
with dissolve



label fr_H20:

play music music_daily fadein 2.0

scene bg school_girlsdormhall
show lilly basic_smile_cas at twoleft
show hanako basic_normal_cas at tworight
with locationchange


hi "Bien. Tu prends le bus, Lilly ?"

show lilly basic_smileclosed_cas
with charachange


"Lilly montre une grande valise à côté d'elle."

show lilly basic_weaksmile_cas
with charachange


li "Je dois la prendre avec moi, donc j'ai appelé un taxi. Il arrivera au portail de l'école dans cinq minutes."


hi "Ah, d'accord."

show lilly basic_sleepy_cas:
    ypos 1.1
with dissolvecharamove


"Lilly se penche et attrape la poignée de la valise. Le poids lui cause des difficultés, alors je lui offre de la prendre moi-même."

show lilly basic_smileclosed_cas at twoleft
with dissolvecharamove


li "C'est bien gentil à toi, Hisao."


"Elle n'a pas de scrupule à accepter et je me retrouve à devoir la porter. Elle n'est pas vraiment légère, mais pas si lourde, non plus. Je ne pense pas que ce sera si dur de la porter."

show lilly basic_weaksmile_cas
with charachange


li "Merci, alors. Nous devrions nous dépêcher cela dit, si le taxi part il me faudra un moment pour en avoir un autre. Tu es prête, Hanako ?"

show hanako cover_worry_cas at tworight
with charachange


ha "O-oui. Allons-y."

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_parkambience fadein 2.0

scene bg school_gate at bgright
with locationskip


"Nous nous dirigeons vers le portail aussi vite que nous pouvons, seulement pour découvrir que le taxi n'est pas encore arrivé."


hi "En tout cas, ça fait de l'exercice matinal. L'infirmier m'a dit que je devais en faire."

show lilly basic_weaksmile_cas at center
with charaenter


li "Je pense qu'il imaginait d'autres choses en disant ça, Hisao. Et probablement plus régulièrement. Tu as l'intention de porter les valises des gens tous les jours ?"


hi "J'imagine que non. On dirait qu'on va devoir attendre un peu. Tu ne devrais pas appeler la compagnie si le taxi est en retard ?"

show lilly basic_smileclosed_cas
with charachange


li "Je vais attendre dix petites minutes, mais ils ne m'ont jamais laissé tomber auparavant. Il y a sûrement juste un peu de monde sur la route."


hi "D'accord."


hi "Combien de temps dure le vol vers l’Écosse ?"

show lilly basic_smile_cas
with charachange


li "Près de seize heures, si je me rappelle bien. Difficile à dire avec le changement d'horaire."

show bg school_gate at center
show lilly basic_smile_cas at twoleft
with charamove

show hanako defarms_worry_cas at tworight
with charaenter


ha "Si long..."


"C'est maintenant que je réalise que Hanako est inhabituellement silencieuse, même pour elle. Elle ne gère pas bien le stress, elle a l'air vraiment crispée."


hi "Ouais, je ne peux pas imaginer être dans un avion pendant si longtemps."


"Le seul vol que j'ai fait était pour aller au nord du pays en vacances, donc c'est vraiment difficile d'imaginer. Vu que Hanako a passé tant de temps dans un orphelinat durant son enfance, elle a probablement très peu voyagé, encore moins pris l'avion."

show lilly basic_weaksmile_cas
with charachange


li "Ce n'est pas si dur. Je vais passer la plupart du temps endormie ou à réviser mon anglais. Je l'utilise rarement ici donc j'ai besoin de me refamiliariser un peu."

show hanako cover_worry_cas
with charachange


ha "T-ton accent ne sera pas... un problème ?"

show lilly basic_smile_cas
with charachange


li "Je ne m'en inquiète pas tellement. Ça sera peut-être un problème au début, mais je m'habituerai vite."

show hanako basic_worry_cas at Position(ypos=1.14)
show lilly basic_smileclosed_cas at Position(ypos=1.17)
with dissolvecharamove


"Nous nous asseyons sur un petit banc à côté du portail de l'école."


"Étrangement, même si je sais que Lilly s'en va, je ne trouve rien à lui dire. Lilly est débrouillarde, c'est sûrement pour ça que je ne pense pas autant à elle qu'à Hanako."

show hanako emb_downsad_cas
with charachange


"Lilly ne le voit peut-être pas, mais Hanako se ronge les ongles nerveusement. Je m'approche pour lui parler, mais j'entends un moteur monter la colline avant d'en avoir la chance."


hi "Ah, je crois que le taxi est là..."

show lilly basic_cheerful_cas
with charachange


li "Effectivement Hisao, moi-même je viens de l'entendre."


"Je me sens un peu fier. Avoir remarqué quelque chose en même temps que Lilly doit signifier que je suis plus conscient de ce qui m'entoure."


"Bon, au moins on n'aura pas à appeler la compagnie de taxi."

show hanako basic_worry_cas at tworight
show lilly basic_smileclosed_cas at twoleft
with dissolvecharamove


"Alors que le taxi s’arrête là où nous nous tenons, le conducteur baisse la fenêtre et se penche. Après avoir confirmé que, oui, Lilly est la même Lilly Satou que celle qui l'a appelé, nous prenons ses bagages."

hide lilly
with charaexit


"Le conducteur ouvre le coffre et prend la valise, et Lilly monte sur la banquette arrière alors qu'il referme le coffre."


"Une fois les portes fermées et rassis sur son siège, il attend que nous fassions nos au revoir."

show hanako emb_downtimid_cas
with charachange


ha "Profite de ton voyage, Lilly."


hi "Prends soin de toi."


"Hanako a l'air abattue, ça s'entend même dans sa voix."


li "Oui, bien sûr. Je reviens vite, ne t’inquiète pas. Et il y aura quelqu'un d'autre pour toi, hein Hisao ?"


hi "Oui, évidemment."

show hanako emb_blushtimid_cas_close
with characlose


"Je me tourne et souris à Hanako, posant une main sur son épaule."

show hanako emb_downtimid_cas_close
with charachange


"Elle ne me regarde dans les yeux que quelques secondes, les joues rouges, puis se tourne vers Lilly."


hi "À la prochaine, Lilly."

show hanako basic_worry_cas_close
with charachange


ha "Au revoir !"

stop music fadeout 6.0


"Lilly fait ses au revoir avec une légère réticence. Sans autre commentaire, le conducteur démarre et ils descendent la colline, en direction de l'aéroport."


"Nous restons tous les deux debout devant le portail pendant un moment après qu'ils soient partis, ne sachant pas vraiment quoi faire."

show bg school_gate at bgleft
show hanako basic_worry_cas_close at center
with charamove


hi "Bon, qu'est-ce que tu veux faire ?"

show hanako def_worry_cas_close
with charachange


ha "Je... ne sais pas."

label fr_choiceH20:
menu:
    with menueffect
    "Tu veux aller en ville ?":


        return m1
    "Et si on rentrait aux dortoirs ?":


        return m2



label fr_H20_1:

scene bg school_gate at bgleft
show hanako def_worry_cas_close at center
with None

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")


"Le bus s’arrête, se tenant près du portail telle une sentinelle muette, me donnant une drôle d'idée."


hi "Tu veux qu'on aille en ville pour voir une librairie ou un truc ? On a le reste de la journée après tout."


"C'est une demande risquée, vu que Hanako n'aime pas aller en ville. J'estime déjà le fait qu'on ait réussi à la faire sortir en ville la nuit comme un petit miracle, mais je veux honnêtement passer plus de temps avec elle."


"De toute façon, elle va sûrement juste refuser et retourner au..."

show hanako basic_smile_cas_close
with charachange


ha "D'accord."


hi "Vraiment ?"

show hanako basic_bashful_cas_close
with charachange


ha "V-vraiment. Allons-y."


"Je ne sais pas vraiment pourquoi Hanako a accepté, mais je ne vais pas la contredire."

stop ambient fadeout 2.0

scene bg city_street2
show crowd
with shorttimeskip

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_crowd_outdoors fadein 2.0


"Descendant du bus, je remarque immédiatement qu'il y a beaucoup de monde. En y pensant, j'aurais dû le savoir ; bien sûr qu'il y aurait beaucoup de monde en centre ville un samedi après-midi."

show hanako emb_downtimid_cas_close at center
with charaenter


"Hanako se rapproche de moi, et je peux sentir sa main me serrer le bras. Son corps est collé contre le mien et sa tête est penchée si bas qu'elle cache la plupart de ses cicatrices."


hi "Donc euh, on y va ? On cherche une librairie ?"


"Le cadeau de Hanako et mes dépenses communes ont bien creusé mon budget, mais je devrais pouvoir me permettre quelques livres. J'essaye toujours de mettre un peu de côté pour cela après tout."


"Pendant une seconde je crois que Hanako ne m'a pas entendu, mais je la vois hocher très légèrement la tête."

show hanako emb_smile_cas_close
with charachange


ha "D-d'accord. T-tu en connais une ?"


hi "En fait, oui. On est passés devant plusieurs fois quand Lilly et moi cherchions tes cadeaux..."

show hanako emb_downsad_cas_close
with charachange


"L'expression de Hanako s’assombrit pendant une seconde. Je dois me rappeler d’arrêter de mentionner son anniversaire."

show hanako emb_timid_cas_close
with charachange


ha "Vous... avez mis longtemps ?"


"Ou peut-être que j'ai mal jugé son expression."


hi "On voulait être sûrs de trouver le bon cadeau, après tout."

show hanako emb_smile_cas_close
with charachange


"Hanako sourit et rougit un peu. Rien que ça, c'est un petit trésor."


hi "Bref, il devrait y avoir une librairie pas loin. Tu veux qu'on y aille ?"

show hanako basic_bashful_cas_close
with charachange


ha "O-oui."

scene bg city_street1
show crowd
with locationchange


"La foule commence à s'épaissir alors que nous nous dirigeons en direction de la librairie. Hanako accroche son autre bras à moi, ralentissant quelque peu notre progression."


"Alors que nous marchons, le bruit du trafic routier me fait penser à une potentielle discussion pour la distraire."


hi "Je me demandais, Hanako... tu as déjà pensé à apprendre à conduire ?"

show hanako cover_worry_cas_close
with charachange


ha "C-conduire ?"


hi "Ouais. Tu as de la chance, d'une certaine façon ; beaucoup d'étudiants à Yamaku n'ont pas le droit de conduire."


"Ce n'est pas le meilleur sujet de conversation, mais je veux essayer de distraire Hanako. Elle est vraiment tendue."


"Encore une fois, tout ce que j'ai réussi à faire est rendre la situation étrange. Elle n'y avait sûrement jamais pensé. J'aurais dû me taire."

stop ambient fadeout 0.5

scene bg city_street3 at left
with locationchange

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_traffic fadein 1.0


"Après peu de temps, nous arrivons à une des librairies devant lesquelles Lilly et moi sommes passés durant notre recherche."


hi "Quel genre de librairie ferme le samedi ?"

show hanako def_worry_cas_close at center
with charaenter


ha "Les librairies... ne se font plus autant d'argent qu'avant, à cause d'Internet. Peut-être qu'ils doivent fermer les week-ends ?"


"Elle semble s'y connaître en technologie. J'imagine que c'est une des choses normales quand on apprécie la solitude."


hi "Euh, c'est pas bête... il est plus facile de trouver des livres en ligne. Dans tous les cas, on dirait que c'est mort pour cette idée. Tu veux faire autre chose ?"

show hanako emb_smile_cas_close
with charachange


ha "S-si ça ne... ne te gêne pas... tu pourrais me montrer là où tu as acheté mon cadeau ?"


hi "Bien sûr, pas de problème. Ce n'est pas loin."

hide hanako
with charaexit

show bg city_street3 at right
with charamove_slow


"Je vais en direction du magasin, à moitié sûr de sa localisation. Je ne veux pas revivre l'expérience de la dernière fois, passer la moitié de la journée à marcher sans rien trouver."


hi "Nous y voilà, Othello's Antiques."

show hanako basic_normal_cas_close at center
with charaenter


ha "C-c'est petit."


hi "Oui. Ça nous a pris un moment pour le trouver."

show hanako basic_distant_cas_close
with charachange


ha "On peut y entrer ?"


hi "Pourquoi pas, c'est ouvert."

stop ambient fadeout 0.5
play sound sfx_storebell
play music music_soothing fadein 0.5

scene bg city_othello
with locationchange


"Hanako pousse la porte et entre avant moi. Encore une fois, le magasin est vide, il n'y a que le gérant."

show shopkeep neutral at center
with charaenter


"Il fait une petite grimace en me voyant."


sk "Oh, vous n'êtes pas là pour un retour, hein ? Attends, ce n'est pas la fille qui était avec toi la dernière fois..."


hi "Erh, non, nous ne sommes pas là pour ramener quoi que ce soit. On était juste en ville et on voulait venir jeter un coup d’œil."

show shopkeep thinking
with charachange


"Le gérant y réfléchit un long moment. J'imagine qu'il ne doit pas avoir beaucoup de lycéens qui viennent régulièrement dans son magasin."

show shopkeep happy
with charachange


sk "Se pourrait-il que ce soit l'amie pour qui vous avez acheté les cadeaux ?"


hi "Oui. Ils étaient pour elle."

show shopkeep happy at twoleft
show bg city_othello at bgleft
with charamove

show hanako defarms_strain_cas_close at tworight
with charaenter


"Le gérant se tourne vers Hanako, qui s'immobilise comme un lapin pris dans les phares."

show shopkeep surprised
with charachange


"Il allait lui parler, mais s'arrête, ayant l'air un peu embêté."

show shopkeep thinking
with charachange


"Il se surprend en train de la fixer et tourne la tête, s'adressant à nous indirectement. Son expression est gênée et tendue, tout comme son corps entier."


"Je voudrais lui en vouloir, mais je sais que j'ai eu la même réaction la première fois que j'ai vu Hanako. D'abord de la surprise, puis de la curiosité, et enfin un détournement de regard gêné."

show hanako emb_downsad_cas_close
with charachange


"Hanako semble moins paniquée qu'avant... mais je crois que le sentiment qu'elle ressent est pire. Elle n'est pas énervée, ou gênée. Elle est désolée."

show shopkeep neutral
with charachange


sk "Tu as de la chance, jeune fille. D'avoir des amis pour qui tu comptes autant."

show hanako emb_downtimid_cas_close
with charachange


ha "M-merci..."


"Si je n'avais pas passé autant de temps avec Hanako, je n'aurais pas réalisé qu'elle venait de dire quelque chose. Cela dit, le marmonnement du gérant n'était pas clair non plus, vu qu'il parlait dans une autre direction."

hide hanako
with charaexit

show bg city_othello at left
show shopkeep invis:
    xpos 0.6 alpha 0.0
with dissolvecharamove


"Hanako se balade dans le magasin, regardant les divers objets présentés. Elle trouve la section des poupées et passe de longues minutes à les étudier une par une."


"C'est un côté de Hanako que je ne connais que très peu. J'étais étonné quand Lilly a dit qu'elle aimait les poupées, et encore plus quand j'ai découvert sa “collection” sur son étagère."

show hanako basic_normal_cas_close at center
with charaenter


"Elle a l'air d'aller mieux maintenant qu'elle est distraite et hors du champ de vision du gérant, mais elle est toujours un peu perturbée par l'expérience."


"J'ai mes propres problèmes, mais je n'ai jamais vu d'étrangers agir comme ça avec moi, comme si j'étais complètement différent d'eux."

show hanako basic_smile_cas_close
with charachange


ha "Il est bien ce magasin."


hi "Ouais, je ne m'attendais pas à ça. Tu veux acheter quelque chose ?"

show hanako cover_worry_cas_close
with charachange


ha "J-je n'ai pas apporté d'argent."


hi "On peut toujours revenir."


"Maintenant que je sais où c'est."

show hanako cover_bashful_cas_close
with charachange


ha "O-on peut ?"


hi "Bien sûr. On peut revenir ici aussi souvent que tu le veux."

show hanako basic_bashful_cas_close
with charachange


ha "M-merci."


hi "Tu n'as pas besoin de me remercier, j'avais presque oublié où était la boutique."


"Je ne crois pas que l'un de nous pense vraiment ce qu'il dit, mais plutôt qu'il répète ce qu'il croit devoir dire."

show hanako emb_smile_cas_close
with charachange


ha "O-on peut retourner à l'école maintenant ?"


hi "Bien sûr. Allons-y."

stop music fadeout 5.0
play ambient sfx_traffic fadein 2.0

scene bg city_street3 at right
with locationchange


"Alors que nous partons en direction de l’arrêt de bus, je vois le gérant nous regarder à travers les rideaux."


"Je ne sais pas vraiment ce que son regard veut dire. C'est un peu bizarre, et le fait que Hanako ne l'ait pas vu entraîne à la fois un soulagement et un certaine frustration."

stop ambient fadeout 2.0

scene bg school_dormext_full
with shorttimeskip


"Hanako et moi nous arrêtons en arrivant entre les deux bâtiments des dortoirs. Nous avons à peine dit un mot depuis que nous avons quitté la ville."

show hanako basic_bashful_cas at center
with charaenter


ha "Alors euh, au revoir."


hi "Tu veux prendre un thé ou quelque chose ? Ou jouer une partie ?"

show hanako emb_emb_cas
with charachange


"Hanako secoue la tête, embarrassée."


ha "Je... je suis fatiguée. Peut-être plus tard ? J'ai des devoirs..."


"Elle semble un peu déprimée. Hanako a visiblement envie de faire plus, mais j'imagine qu'elle doit avoir des cours à rattraper, elle a loupé quelques jours après tout."


hi "Ah, les devoirs. Merci de me le rappeler ; j'en ai une tonne à faire aussi. On se voit demain."

show hanako basic_smile_cas
with charachange


ha "Au revoir, Hisao."

hide hanako
with charaexit


"Avant que je puisse lui dire au revoir, Hanako a tourné les talons et commence à marcher en direction du dortoir des filles."


"Je regarde la porte après qu'elle l'ait passée et me dirige vers mon propre dortoir."


"Aujourd'hui était une longue journée."

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")



label fr_H20_2:

scene bg school_gate at bgleft
show hanako def_worry_cas_close at center
with None

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")


hi "Je ne sais pas pour toi, mais je crois que je vais essayer de faire une sieste. J'ai très mal à la tête."

show hanako basic_distant_cas_close
with charachange


"À en juger par l'expression rassurée de Hanako, j'ai bien choisi. Je ne crois pas qu'elle veuille sortir."

hide hanako
with charaexit


"Sans dire un mot, elle se tourne et traverse le portail de l'école."

scene bg school_dormext_full
with locationskip


"Nous marchons côte à côte jusqu'aux dortoirs, nous arrêtant, gênés, à l'endroit où nous devons nous séparer."

show hanako cover_distant_cas at center
with charaenter


ha "Alors euh, a-au revoir."


hi "Tu veux boire un thé ou quelque chose, après ? Ou faire une partie ?"

show hanako emb_timid_cas
with charachange


"Hanako secoue la tête, embarrassée."

show hanako emb_downtimid_cas
with charachange


ha "Je... je suis fatiguée. Peut-être demain ? J'ai du travail."


"J'imagine qu'elle doit avoir des cours à rattraper, elle a loupé quelques jours après tout."


hi "Ah, les devoirs. Merci de me le rappeler ; j'en ai une tonne à faire aussi. On se voit demain."

show hanako emb_downsmile_cas
with charachange


ha "Au revoir, Hisao."

hide hanako
with charaexit


"Avant que je puisse lui dire au revoir, Hanako a tourné les talons et commence à marcher en direction du dortoir des filles."


"Je regarde la porte après qu'elle l'ait passée, et me dirige vers mon propre dortoir."


"Demain sera une meilleure journée."

stop ambient fadeout 1.0
$ renpy.music.set_volume(1.0, 2.0, channel="ambient")

window hide

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
