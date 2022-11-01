label fr_H21:

scene bg school_scienceroom
with locationchange

play music music_normal fadein 3.0


"Je me réveille, prends mes pilules, une bonne douche, enfile mon uniforme, mange un bon petit-déjeuner, attrape mon sac et sors, mettant fin à ma routine matinale."


"C'est seulement après être arrivé en classe que la normalité de la journée se termine."


"Après m’être assis, je regarde mes camarades rentrer un par un dans la salle de classe, jusqu’à ce que chaque siège soit occupé, sauf celui de Hanako."

stop music fadeout 10.0

$ ksgallery_unlock("evul hanako_emptyclassroom")
scene evbg hanako_emptyclassroom:
    truecenter
    subpixel True zoom 0.9
    easein 20.0 zoom 1.0
show evfg hanako_emptyclassroom:
    truecenter
    subpixel True zoom 0.8
    easein 20.0 zoom 1.0
with whiteout


"Je n'arrive pas à me faire à l'idée qu'elle ne vienne pas en classe de temps en temps. Ça m’inquiète encore plus maintenant que Lilly est partie."


"Alors que Mutou continue de parler, je lance malgré moi des coups d’œil à son siège, comme si elle allait apparaître par magie. Personne d'autre ne semble se préoccuper de son absence, ce qui n'est pas étonnant."


"Il n'est pas anormal que Hanako soit absente, après tout. Ou du moins, ça ne l'était pas. Son taux de présence n'est pas si mauvais depuis que je suis là, c'était apparemment pire avant."


"C'est pas bon qu'elle soit absente aujourd'hui. C'est la veille de son anniversaire et je commence à être suspicieux, vu ce qui s'est passé la dernière fois qu'il a été mentionné."


"Je réfléchis à beaucoup de manières différentes de l'aider, mais en fin de compte, j'ai l'impression de ne rien pouvoir faire."

scene bg school_scienceroom
with silentwhiteout
play sound sfx_normalbell


"La sonnerie annonçant le début de la pause déjeuner résonne, me sortant de ma torpeur. Un soupir de soulagement collectif se fait entendre de la part de la classe et Mutou semble quelque peu agacé."


"Il n'aime pas être interrompu au milieu d'une de ses passionnantes leçons, après tout."


"Au moment où je me demande ce que je devrais faire durant le déjeuner, vu que Hanako et Lilly ne sont pas là, la réponse se présente d’elle-même."

show shizu invis:
    tworight
    xpos 0.8
show misha invis:
    twoleft
    xpos 0.2
with None

show shizu behind_blank at tworight
show misha hips_grin at twoleft
with dissolvecharamove

play music music_shizune fadein 5.0


mi "Bonjour, Hicchan~ !"

show shizu adjust_happy
with charachange

shi "…"


hi "Bonjour Misha, Shizune. Vous semblez aussi énergiques que d'habitude."

show shizu basic_normal2
with charachange

shi "…"

show misha sign_smile
with charachange


mi "Shicchan veut savoir si tu es d'accord pour déjeuner avec nous aujourd'hui~ ?"


hi "Bien sûr. Ça fera du bien d'avoir de la compagnie."

scene bg school_cafeteria
show crowd
with locationskip

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 1.0


"La cafétéria vrombit d'activité, comme dans mon ancienne école. Mais Yamaku est différente, dans sa manière d’être... étrangement civilisée durant le rush du déjeuner."


"On pourrait s'attendre à une foule prenant d'assaut le comptoir pour se servir, mais il y a à la place une file d'attente calme et organisée."


"Quelques personnes se bousculent et les têtes des gens se redressent souvent pour voir ce qui se passe devant, mais c'est plutôt contenu."


"C'est dû, sans aucun doute, aux règles sévères de l'école. La même discipline stricte est observée pour les déplacements des élèves dans les couloirs et à l'extérieur, en direction des dortoirs ou du portail."


"Bien que les raisons derrière ça puissent être un peu déconcertantes, j'en suis venu à apprécier l'ordre qui règne dans l'école."

show shizu behind_smile:
    tworight
    ypos 1.1
show misha perky_smile:
    twoleft
    ypos 1.1
with charaenter

hide crowd
with charaexit

$ renpy.music.set_volume(0.4, 7.0, channel="ambient")


"Je n'ai pas vraiment apprécié que Shizune et Misha me demandent de prendre leur déjeuner, cela dit. Je me sens un peu utilisé quand je reviens et m'assois à leur table en posant leur repas devant elles."


"Un cake et un lait à la fraise pour Misha, un bol de ramen et un jus de bruit pour Shizune. Je pousse un soupir de soulagement après avoir posé tout ça, ayant eu du mal à tout transporter, y compris mon propre déjeuner."

show misha hips_grin
with charachange


mi "Merci~ !"

show shizu behind_smile
with charachange


"Misha colle ses mains ensemble avant d'enlever le plastique et d'attaquer son cake. Shizune m'adresse simplement un hochement de tête reconnaissant avant de remuer son bol de ramen fumantes et de souffler dessus pour les refroidir."


"J'ouvre mon propre repas, un autre cake, et prends une bouchée avant de l'agrémenter d'une gorgée de jus de fruit. Le cake est vraiment sucré, tellement que je suis obligé de me forcer à l'ingurgiter."


"L'ayant à moitié fini, je décide de prendre une pause et de demander ce qui me tracasse."


hi "Donc, j'imagine que vous avez une raison pour me faire venir ici ? Vous semblez toujours avoir un but caché, après tout."

show misha sign_confused
with charachange


mi "Qu'effe que tu dis, Hiffan~ ! Nous n'afons pas de but café~."

show shizu basic_angry
with charachange


"Elle parle la bouche pleine de cake. C'est assez déplaisant à voir. Shizune semble un peu repoussée par cette vision et retourne à ses ramen."

show shizu basic_normal
show misha perky_smile
with charachange


"J’attends que Misha finisse ce qu'elle a dans la bouche avant de reparler."


hi "Vous ne mijotez rien pour faire en sorte que je travaille avec vous après l'école ?"

show misha hips_smile
with charachange


mi "Nope !"


hi "Vous n'essayez pas de me soustraire des informations ?"

show misha cross_smile
with charachange


mi "Nope nope !"


hi "...D'accord. Vous avez gagné. J'imagine que vous voulez juste déjeuner avec quelqu'un d'aussi intelligent et beau que moi."

show misha cross_grin
with charachange


mi "C'est ça, Hicchan~ ! Tu as compris~ !"


"Shizune reste placide alors que Misha finit de traduire notre conversation, puis aspire une nouille tout en signant sa réponse."

show shizu behind_blank
with charachange

shi "…"

show misha sign_smile
with charachange


mi "Shicchan dit que tu ne devrais pas être si suspicieux avec nous~. Elle fait juste son travail de déléguée de classe, après tout~."


hi "Et qu'est-ce qu'elle... euh... tu fais ?"


"Même si je n'aime pas l'avouer, j'ai toujours du mal à communiquer avec Shizune."


"Il suffirait que je regarde Shizune dans les yeux et que je lui parle au lieu de regarder Misha, mais vu que quelqu'un d'autre parle pour elle, c'est assez difficile."

show shizu basic_normal2
with charachange

shi "…"

show misha hips_smile
with charachange


mi "C'est le travail du délégué de s'assurer que tout le monde va bien en classe, hein~ ?"


hi "Pas... vraiment..."


hi "Attends, quel rapport entre le fait que j'aille chercher votre nourriture et que j'aille bien en classe ?"

show shizu adjust_frown
with charachange


"Shizune souffle et ajuste ses lunettes d'un air désapprobateur."

show shizu behind_frown
with charachange

shi "…"

show misha cross_frown
with charachange


mi "C'est donc ça les remerciements qu'on obtient pour t'éviter de déjeuner tout seul ?"

$ renpy.music.set_volume(0.0, 3.0, channel="music")


"Elle évite la question. Attends..."


hi "Comment est-ce que tu sais que je... ?"

show shizu basic_normal
with charachange

shi "…"

show misha sign_smile
with charachange


mi "Lilly est partie et Hanako est absente, et vu qu'elles sont les deux seules personnes que tu fréquentes..."

show shizu adjust_smug
with charachange

shi "…"

show misha cross_smile
with charachange


mi "C'était plutôt évident à voir aussi~..."

$ renpy.music.set_volume(1.0, 3.0, channel="music")


"Aïe. C'est peut-être vrai, mais elle n'avait pas besoin de me le balancer comme ça. Peut-être qu'elles se vengent pour avant."


hi "D'accord. Bon, merci. J'apprécie, et ce n'est pas un sarcasme."

show shizu basic_normal
show misha perky_smile
with charachange


"Elles hochent toutes les deux la tête et nous finissons nos repas. Je me sens un peu embarrassé qu'elle soient avec moi juste parce j'étais seul, mais ce n'est pas comme si on était étrangers non plus."


"Il ne faut pas longtemps avant que je finisse mon cake et le fond de ma brique de jus de fruit, et en même temps, je me retrouve à penser à ce qui me travaillait avant qu'elles ne viennent interrompre mes pensées."


"J'ai l'impression d’être le seul dans la classe qui ait remarqué que Hanako n'était pas là. C'était déjà comme ça les autres fois où elle n'est pas venue, mais maintenant c'est encore plus énervant."


"Est-ce que quelqu'un se préoccupe de savoir si elle est heureuse ou non ? Ils ont déjà envisagé de l'aider à aller mieux ? Même Mutou n'essaye pas de la garder en classe et je ne suis toujours pas vraiment convaincu par son raisonnement."

show misha perky_smile
with charachange


mi "Hé, Hicchan, ton jus de fruit est périmé ?"


hi "Hein ?"

show misha hips_grin
with charachange


mi "Tu faisais une drôle de tête, comme ça~."

show misha perky_confused
show shizu adjust_happy
with charachange


"Comme si c'était nécessaire, Misha fait une grimace pour m'imiter. Elle exagère clairement, bien que Shizune semble s'en amuser."


hi "Je pensais à Hanako."

show misha hips_smile
with charachange


mi "Oh ?"

show shizu basic_happy
with charachange


"J'ai accaparé l'attention de Misha, tout comme celle de Shizune, une fois qu'on lui a traduit mes mots."


hi "Je m’inquiétais juste qu'elle soit absente aussi souvent. Surtout maintenant que son anniversaire approche."

show misha perky_sad
show shizu behind_sad
with charachange


"Le souvenir de ce qui s'est passé en classe est encore frais dans leur esprit. Ça se voit sur leur visage."


hi "Tu sais quelque chose sur Hanako ? Quelque chose qui pourrait l'aider ?"

show misha perky_confused
show shizu behind_blank
with charachange


"Misha hausse les épaules et regarde Shizune, qui réfléchit un moment."

show shizu basic_normal2
with charachange

shi "…"

show misha perky_smile
with charachange


mi "Les seuls avec qui elle a parlé plus d'une fois ou deux sont Lilly et toi."


"Shizune n'est peut-être pas capable de faire un ton moqueur quand elle s'exprime, mais j'ai eu l'impression qu'elle l'a fait avec ses signes quand elle a mentionné Lilly. L'effet est cependant perdu après l’interprétation de Misha."

show shizu behind_blank
with charachange

shi "…"

show misha sign_smile
with charachange


mi "Il y a certaines choses que nous connaissons sur Hanako en tant que membres du Conseil Étudiant, vu qu'on a accès à certains fichiers, mais nous ne pouvons pas dire ce qu'ils contiennent."


hi "Normal."


"Ça ressemble beaucoup au “secret médical” de l'infirmier. À chaque fois que je trouve quelqu'un qui sait quelque chose sur le passé de Hanako, je me retrouve face à un mur."


"Je n'ai qu'une seule manière de faire, si je veux savoir : lui demander. Je ne sais pas si elle me laissera savoir de telles choses, mais si c'est dans son intérêt, je dois au moins essayer."

show shizu adjust_happy
with charachange

shi "…"

show misha hips_smile
with charachange


mi "Ne t’inquiète pas, Hicchan~. Ça arrive tous les ans, après tout~."


"Ça ne me rassure pas du tout. Je me sens toujours un peu coupable pour ce qui est arrivé en classe, mais je pense que c'est pire cette fois, même si je ne peux pas en être sûr."

show misha perky_confused
show shizu behind_blank
with charachange


"Misha remarque mon expression troublée et sa joie habituelle s'efface."


mi "Tout le monde a ses problèmes, hein, Hicchan."


hi "Ouais. J'aimerais juste pouvoir aider Hanako avec les siens."


"Sur ce, la conversation s’arrête sur une note déprimante."

stop music fadeout 4.0

show misha hips_grin
with charachange


"Au bout d'un moment, Misha arrive à remonter le moral ambiant avec son habituelle joie et son humeur pétillante, mais je continue de penser à Hanako."


"J'irai la voir plus tard."

stop ambient fadeout 1.0

scene bg school_dormhallway
with shorttimeskip


"Je m'assure que la porte est verrouillée après avoir déposé mon sac dans ma chambre."


"Les dortoirs sont silencieux. Mutou m'a gardé plus longtemps que je ne le pensais après les cours, me parlant de mes études et me donnant des papiers à remettre à Hanako."


"Absorbé par mes pensées, je vois trop tard l'ombre apparaître en face de moi. En relevant la tête, je vois le propriétaire de la dite ombre."

show kenji happy at center
with charaenter

play music music_kenji fadein 0.5


ke "Salut mec. Ça fait un moment."


hi "Oh. Salut."

show kenji tsun
with charachange


ke "C'est quoi cette réponse ?"


"Ma réponse banale semble l’énerver. J'aurais probablement eu la même réaction."


hi "Désolé, je réfléchissais juste à pas mal de trucs."


ke "“Réfléchir” n'est qu'une pauvre excuse pour ne pas contribuer à l'effort de guerre."


hi "Et comment se passe la guerre ?"

show kenji neutral
with charachange


ke "Je me prépare. Là, j'ai besoin d'argent pour finir tout ça."


hi "Si tu veux m'emprunter de l'argent, dis-le."

show kenji happy
with charachange


ke "Nan mec, ça va."


hi "Ça... va ? Tu ne veux pas de mon argent ?"

show kenji tsun
with charachange


ke "Hé mec, n’aie pas l'air surpris. C'est insultant."

show kenji neutral
with charachange


ke "Je suis un assez gros poisson dans le monde du bowling de compétition, mais hier, j'ai trouvé des gars qui ne le savaient pas."


hi "Je suis sûr que c'est contre les règles de l'école..."

show kenji tsun
with charachange


ke "Les règles importent peu, c'est une situation de guerre. Les gens, de nos jours, n'ont aucun respect pour la guerre."


hi "Et donc pourquoi tu as besoin d'argent, si j'ose demander ?"

show kenji neutral
with charachange


ke "Des boîtes de conserve non périssables. Du matériel de construction, surtout du fer plié et des planches en bois. Un kit de premier soin. Un réchaud. Une radio portable. Un sac de couchage. Une lampe torche. Une horloge mécanique."


"Au début j'ai l'impression que c'est une liste d'objets et de matériaux au hasard, mais après quelques secondes, je comprends."


hi "C'est pas une liste de matériaux pour un abri antiatomique ?"

show kenji happy
with charachange


ke "Ah, donc tu as lu le manuel 'Protect and Survive'. C'est bien de trouver quelqu'un qui sait comment se protéger."



hi "Tu ne penses pas sérieusement que..."

show kenji neutral
with charachange


ke "Il y a toujours une possibilité."


hi "Non, je suis sûr que ça n'arrivera pas."

show kenji happy
with charachange


"Il lève lentement un sourcil d'une façon dramatique. Enfin, aussi dramatique que puisse être un lever de sourcil."


hi "La probabilité est genre, je sais pas, zéro virgule un sur un trilliard. C'est infiniment petit. En plus, où est-ce que tu peux construire un abri antiatomique ? Certainement pas sur le campus."

show kenji neutral
with charachange


ke "C'est mon projet de cet été pendant que je suis chez moi. Mon père a dit que je pouvais le faire."


hi "Vraiment ?"


ke "Ouais. Il a dit que ça m'apprendra à construire des trucs et améliorera ma dextérité manuelle. Ou un truc du genre."


"Connaissant Kenji, son père a probablement juste pensé que ça le tiendrait éloigné un moment."


"Cela dit, je me demande comment sont ses parents. Peut-être qu'ils sont totalement normaux et que Kenji est juste une aberration. D'un autre côté, peut-être que ce genre de paranoïa survivaliste est de famille."

show kenji happy
with charachange


ke "Hé, tu veux m'aider à le construire ? Tu sembles être le genre de gars à savoir utiliser les outils. Avec ton aide, on aurait un bunker super classe au lieu de juste un abri antiatomique."


"J'en doute. Jouer au football avant mon accident m'a permis d'avoir de bonnes jambes, mais je n'ai jamais vraiment fait grand-chose de mes mains."


hi "Je ne suis pas doué, vraiment. Et de toute façon, je suis occupé pendant les vacances."

show kenji tsun
with charachange


ke "Dommage. Si les féministes ont un jour accès aux codes de lancement, j'ai bien peur que peu soient préparés."


hi "Et ton abri antiatomique te protégera d'une explosion nucléaire, si ça arrive ?"


ke "Un abri antiatomique n'est pas destiné à protéger contre une explosion. Il faut un abri anti-explosion pour ça."


ke "Je pensais que tu t'y connaîtrais mieux que ça."


hi "Je ne savais pas..."

show kenji neutral
with charachange


ke "Ma maison n'est proche d'aucune base militaire, alors les retombées radioactives suivant une explosion nucléaire sont plus dangereuses que l'explosion en elle-même."

show kenji happy
with charachange


ke "Ça servira à garder la poussière et les particules éloignées de moi, de ma réserve de nourriture et de ma zone de repos. Il doit durer au moins deux semaines, hein."


hi "C'est long quatorze jours."

show kenji neutral
with charachange


ke "Oui. J'ai besoin d'un litre d'eau par jour pour boire, deux optimalement pour que je puisse me laver. Les toilettes ne sont pas un problème. Juste des sacs poubelle et une corbeille en dehors de la zone d'habitation. Pour la nourriture, des conserves."


hi "Bien sûr. Et la radio pour communiquer avec l'extérieur ?"


ke "Oui, oui. Pour que je puisse écouter les alertes du gouvernement sur ce qui se passe à l'extérieur. J'ai besoin d'une horloge mécanique au lieu d'une électrique au cas où il y ait une onde électromagnétique à cause de l'onde de choc nucléaire."


ke "Il y a tous les autres trucs dont j'ai besoin aussi, comme des vêtements de rechange, des allumettes et des bougies. Je crois que j'ai assez de temps pour tout réunir. Sûrement."


"Ça a beau me faire mal de l'accepter, je suis un peu impressionné. Il a vraiment réfléchi à tout ça. Encore une fois, je ne sais pas si je veux vivre dans un monde post-apocalyptique où seuls les gens comme Kenji ont survécu."


hi "On dirait que tu sais ce que tu fais."

show kenji happy
with charachange


ke "Totalement."


"Ça doit être dur, de vivre dans une peur constante comme ça. Il n'est pas très sociable non plus, donc le fait qu'il ait été faire du bowling avec les autres est surprenant."


"Ça me rappelle un peu quelqu'un. Heureusement, sa peur des autres ne se manifeste pas de manière si excentrique."


"Une chose est sûre, c'est que je ne peux pas lui dire pourquoi il ne m'a pas vu récemment."


hi "Il est tard. J'ai des choses à faire. Je vais réfléchir à cette histoire d'abri antiatomique, cela dit."

show kenji neutral
with charachange


ke "Ouais, d'accord, c'est cool. Un homme doit faire ce qu'il doit faire, après tout."


ke "Tu devrais traîner avec moi un de ces quatre, au fait. T'es un mec cool. Les mecs cool devraient traîner ensemble, hein ?"


"Pour je ne sais quelle raison, le compliment me fait vraiment plaisir. La situation avec Hanako étant ce qu'elle est, je ne vais pourtant sûrement pas être capable de faire ce qu'il veut. Pour le moment, du moins."


hi "Ça serait bien. Je reviendrai te voir quand je pourrai."

show kenji happy
with charachange


ke "Cool. À plus mec."

stop music fadeout 3.0

hide kenji
with charaexit


"Il retourne dans sa chambre."



"Je ferais mieux d'aller voir Hanako."

stop ambient fadeout 1.0

scene bg school_dormhanako_ni
show hanagown worry_close:
    center
    xpos 0.39
show expression Solid("#00000022")
show hanako_door_base at right
show hanako_door_door at left
with locationskip


"Je me tiens debout devant la chambre de Hanako, espérant qu'elle ne va pas trop mal, alors que je tiens nerveusement dans mes mains les papiers que Mutou m'a demandé de lui donner."


"C'est une autre raison pour lui rendre visite et ça me donne un sujet de conversation. Donc j'imagine que je devrais m'estimer heureux de les avoir."

play sound sfx_doorknock2


"Avec une longue respiration pour me concentrer, je frappe à la porte."


"...Silence. J'écoute attentivement au cas où elle bougerait à l'intérieur, mais je n'entends rien."

$ renpy.music.set_volume(0.5, 0.0, channel="sound")
play sound sfx_hammer


"Je frappe à la porte encore une fois, légèrement plus fort."


"Toujours aucune réponse. Étrange."


"Me grattant la tête, je fais une dernière tentative en frappant encore une fois."


hi "Hanako, c'est juste moi. Mutou m'a demandé de te donner des trucs."


"Pendant un moment, je crois que ma dernière tentative ne sert à rien non plus. Juste avant de faire passer les feuilles sous la porte, j’entends la poignée se tourner."

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_dooropen

show hanako_door_door:
    xpos -0.1
with charamove

play music music_moonlight fadein 4.0


"Alors que la porte s'ouvre à moitié, j'essaye de voir comment Hanako va. C'est une tâche qui s’avère être difficile à cause de sa robe trop grande qui cache tant son corps."


"Elle n'a pas l'air malade, ou du moins pas pour l'instant. Pour être honnête, j'aurais préféré qu'elle soit malade plutôt que de la voir comme ça. Elle a l'air extrêmement fatiguée et semble à peine remarquer ma présence."


hi "Salut, Hanako. Mutou voulait que je te donne ça, vu que tu n'était pas en cours aujourd'hui."


"Je lui tends les feuilles, qu'elle prend timidement. La façon dont elle bouge est sans vie. Elle est amorphe, ce qui est inhabituel pour quelqu'un qui est généralement si tendu."

show hanagown distant_close
with charachange


"Elle fait de son mieux pour ne pas me regarder dans les yeux. Je bouge un peu pour essayer de mieux voir, mais elle détourne la tête."


hi "Ça... va ? Si tu te sens mal ou autre, je peux aller chercher l'infirmier."


"Je me sens mal de lui sortir l'habituel “j’espère que tu iras mieux”. Je n'arrive pas à imaginer ce que je peux faire d'autre pour elle."

show hanagown normal_close
with charachange


"Elle semble se réveiller un peu après mes paroles... mais juste un peu. Elle garde la tête tournée loin de moi, mais ses yeux se tournent dans ma direction."


ha "Je vais bien."


"Un silence gênant s'ensuit. Pendant ce temps, je remarque que les manches de sa robe semblent légèrement tachées. Ses joues sont un peu rouges aussi. Elle a pleuré ?"


hi "Je vois."


"J'hésite un moment avant de dire les mots qui sont la raison première de ma venue."


hi "Tu voudrais que je reste ? Je n'ai rien d'urgent à faire, donc ça ne me gênerait pas."

show hanagown distant_close
with charachange


"Ses yeux s'éloignent de moi et je perds espoir d'améliorer son humeur. J’attends une réponse, mais elle ne dit rien. Elle reste là, à m'éviter du regard."


hi "Hanako... ?"


"Elle secoue lentement la tête."


hi "D'accord. Euh... bonne nuit, alors."

stop music fadeout 3.0

show hanako_door_door:
    xpos 0.0
with charamove

play sound sfx_doorclose


"Sur ce, Hanako recule et ferme la porte sans dire un mot."


"Plus qu'un peu inquiet, je retourne à ma chambre."


scene bg school_dormhallway
with locationskip

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_footsteps_hard


"Déambulant dans les couloirs, je continue de réfléchir à ce qui vient d'arriver. J'ai eu l'impression que Hanako n'était là qu'à moitié, comme si j'interagissais avec un robot qui était juste programmé, sans vraies pensées."


"Elle était l'ombre d'elle-même."


"C'est frustrant. J’espérais que parler avec Hanako aurait amélioré les choses, mais j'ai l'impression que j'ai encore plus de mal à la comprendre. Comment je suis supposé aider quelqu'un qui se renferme quand je lui parle ?"

stop ambient fadeout 0.3

scene bg school_dormhisao_ni
with locationchange


"Je ne prends même pas la peine d'allumer la lumière, j'enfile simplement mon pyjama, avale rapidement mes pilules du soir et m'effondre sur le lit."

scene black
with shuteye



label fr_H22:

scene bg school_scienceroom
with locationchange

play music music_pearly


"Encore une fois, Hanako ne vient pas en classe. Essayant comme je peux de me concentrer quand même, ce fait continue de me distraire durant toute la journée d'école, même alors que je traverse les jardins en direction des dortoirs."


"Je ne crois pas que le fait que c'est son anniversaire aujourd'hui soit une coïncidence. Je ne connais pas le rapport avec tout ça et je ne sais pas comment elle se sent."


"Si c'était de la douleur physique, je pourrais au moins l'aider d'une façon ou d'une autre. Avec quelque chose comme ça, je ne sais vraiment pas quoi faire."


"Je fais la liste des gens que je connais dans ma tête, pensant à qui pourrait aider. Shizune et Misha ne savent pas grand-chose sur Hanako, et le peu qu'elles savent, elle ne veulent pas me le dire. Pareil pour l'infirmier."


"En fin de compte, il n'y a qu'une personne qui connaît bien Hanako et qui veut bien me parler."

scene bg school_dormhisao
with shorttimeskip


"Entrant dans ma chambre, je remarque quelque chose qui me surprend. L'endroit commence à m’être familier."


"Avec tout ce qui est arrivé, je suis content que cette chambre devienne un endroit où je puisse me relaxer. Quand je suis arrivé pour la première fois à Yamaku, je me sentais étranger à tout ; l'aspect très propre de la chambre ou l'odeur qu'elle avait."


"Me concentrant sur ce que je fais, je jette mon sac sur mon lit et ouvre le tiroir de mon bureau."


"Avant qu'elle ne parte, Lilly m'a donné le numéro à appeler pendant qu'elle serait en Écosse et je l'ai écrit. En y pensant, je me demande si elle savait que quelque chose comme ça pouvait arriver."


"Maintenant qu'elle est hors d'atteinte, je réalise à quel point Hanako et moi avons dépendu d'elle."


"Je cherche tiroir après tiroir cette fichue feuille. Finalement, et heureusement, je la trouve cachée en dessous d'un livre de la bibliothèque."

scene bg school_dormhisao_blurred
show phone mobile:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with locationchange
with Pause (0.5)


"En y pensant, j'aurais probablement dû l'enregistrer directement dans mon téléphone portable. Sans plus attendre, j'entre les numéros et presse anxieusement le bouton vert."


"Finalement ça décroche, et une voix féminine que je ne connais pas répond de l'autre côté de la ligne. C'est probablement la mère de Lilly."

stop music fadeout 1.0


mystery "{image=vfx/garbage.png} {image=vfx/garbage.png} Satou {image=vfx/garbage.png}?"


"De l'anglais ? Je réalise que je ne comprends pas un mot de ce qu'elle dit, que ce soit à cause de mon vocabulaire limité ou de son fort accent. J'aurais dû l'anticiper, vu que d’après Lilly, sa mère est écossaise de naissance."


"J’espère qu'elle connaît un peu le japonais, vu que c'est la langue principale de sa fille."


hi "Euh... Je suis Hisao Nakai..."


"Elle semble reconnaître instantanément la langue. Mon soulagement est immense."


"Mme Satou" "Ah, tu dois être un des amis de l'école de Lilly, non ?"


"Même là, son accent me force à me concentrer pour comprendre ce qu'elle dit."


hi "Oui, c'est exact. Enchanté de faire votre connaissance, Mme Satou."


"Mme Satou" "C'est plaisant de trouver quelqu'un d'aussi poli ! Lilly chérie, c'est pour toi !"


"Sa mère semble gentille, même si elle est un peu trop enthousiaste étant donné la situation banale."


"Il y a un petit silence alors que Lilly prend son temps pour arriver au téléphone. Au loin, je peux entendre sa mère lui reprocher gentiment de ne se lever que maintenant."


li "Bonjour, qui est à l'appareil ?"


hi "Ta voix est épouvantable."


"Sa voix est comme un mélange entre un animal agonisant et un bâillement."


"La seule chose dont je me suis rappelé avant de téléphoner a été de vérifier le décalage horaire. C'est la fin de matinée là-bas, donc elle n'a aucune excuse."


hi "Tu ne te sens pas bien ?"


li "Juste fatiguée. Quelle heure est-il là-bas ?"


hi "Fin d'après-midi. L'école est finie depuis un petit moment."


li "Hanako ne va pas bien ,c'est ça ?"

play music music_drama


"C'était rapide. Mon hypothèse selon laquelle elle devait savoir que quelque chose comme ça pouvait arriver semble avoir été exacte."


hi "Comment tu sais ?"


li "Parce qu'aujourd'hui, c'est son anniversaire. J'aurais espéré que ça se passe un peu mieux après qu'elle t’ait connu, mais..."


li "Comment est-ce qu'elle va maintenant ?"


hi "Elle a loupé l'école hier et aujourd'hui. J'irai la voir aujourd'hui. Pour être honnête, après avoir vu comment elle était quand je lui ai parlé hier... Je suis plutôt inquiet."


hi "Je ne sais vraiment pas quoi faire. C'est déjà arrivé avant ? C'est lié à ses cicatrices d'une façon ou d'une autre ?"


li "Malheureusement oui. La même chose est arrivée l'année dernière quand il y a eu son anniversaire."


li "Pour autant que je sache, c'est parce que ses parents sont morts dans l'accident qui lui a causé ses cicatrices, et Hanako se blâme pour leurs morts."


"Ce qu'elle dit est logique. Si elle est comme ça le jour de son anniversaire, ça doit être parce qu'elle regrette d’être née."


"Hanako a mentionné qu'elle était à l’orphelinat. Peut-être que je dois penser qu'elle me fait assez confiance pour me dire une telle chose."


"Lilly semble être presque aussi perdue que moi, à ma grande surprise."


hi "C'est pour ça qu'elle vit dans le dortoir étudiant, alors. Elle t'a dit quelque chose d'autre sur l'accident ?"


li "On a beau être proches... elle ne m'a presque rien dit sur ce qui est arrivé. Je ne connais que le gros de l'histoire."


"Elle semble déprimée. Vu le traumatisme qu'a vécu Hanako, je ne peux pas blâmer Lilly pour ne pas savoir. Néanmoins, elle semble toujours considérer ça comme une défaite personnelle."


hi "Ne t'en veux pas, Lilly. Après tout ce qu'elle a vécu..."


"Il y a un long silence de l'autre côté de la ligne. Je commence à me demander si l'appel n'a pas été coupé avant qu'elle ne reparle."


li "Il y a quelqu'un d'autre, cela dit, qui m’inquiète depuis un petit moment."


hi "Oh ?"


"Je passe en revue les gens dont elle peut parler. Les seuls amis proches qu'elle semble avoir sont Hanako et moi, bien qu'elle puisse aussi parler d'Akira..."


li "Cette personne, c'est toi, Hisao."


"Il y a un autre silence sur la ligne, mais cette fois c'est ma faute."


"Depuis que je suis arrivé à Yamaku j'ai essayé d'éviter que les gens s’inquiètent pour moi. Même mon interaction avec Hanako m'a aidé à éviter des problèmes de santé majeurs grâce à notre rythme de vie plutôt lent."


hi "Euh... ok. Qu'est-ce qui est inquiétant chez moi ?"


li "Je m'excuse, je ne voulais pas t'offenser."


hi "Désolé, ça m'a juste surpris. Hanako n'est pas plus importante pour l'instant ?"


li "Depuis un moment j'ai l'impression que vous vous échangez vos inquiétudes. J'ai essayé d’empêcher cela avant de partir, mais ça n'a pas l'air d'avoir marché."


hi "Échanger nos inquiétudes ?"


li "Quand je t’ai demandé ce que tu avais en tête pour ton avenir, ta réponse a été très similaire à celle de Hanako quand je lui avais posé cette question."


li "C'est bien de vouloir la protéger, mais j'ai peur que traiter Hanako comme ça, comme si elle était ta fille ou quelqu'un qui avait besoin d'une attention spéciale, ça fasse plutôt empirer les choses."




label fr_choiceH22:
menu:
    with menueffect
    "Après tout ce qui est arrivé, c'est la première fois que je me retrouve à douter de l'avis de Lilly."
    "Être d'accord avec Lilly.":




        return m1
    "Faire confiance à mon propre avis.":


        return m2

label fr_H22a:


"Je ne veux pas l'avouer, mais elle a peut-être raison. Quelque chose d'autre me gêne, cela dit."


hi "Et tu as essayé de... “empêcher” ça ?"


hi "Attends... notre sortie en ville ?"


li "Effectivement. J'ai pensé que ça pourrait vous aider si je vous faisais sortir tous les deux de Yamaku. Je suis contente que vous vous soyez rapprochés grâce à ça, cela dit."


"Donc elle a remarqué. J'imagine qu'elle faisait peut-être attention à nous et son ouïe est vraiment bonne, tellement qu'il est possible qu'elle ait pu nous entendre, si elle écoutait."


hi "On dirait de plus en plus que tu essayais de nous manipuler."


"Silence. C'est une façon sévère de voir les choses, mais je n'ai aucune intention de retirer ce que j'ai dit."


li "Je suis désolée. J'étais juste... inquiète pour vous."


hi "C'est pas grave. Il y a des choses plus importantes que ça après tout."


"Ce n'est pas si étonnant qu'elle fasse une telle chose. Sa nature maternelle peut être légèrement étouffante à certains moments, mais elle avait une bonne intention."


hi "Donc tu crois que je devrais penser plus à moi plutôt que d'essayer de m'occuper de Hanako ?"


li "Ça résume à peu près. Encore une fois, je suis désolée de ne pas te l'avoir dit clairement avant de faire les choses dans ton dos."


li "Je sais que je suis au moins aussi surprotectrice que toi envers Hanako, mais j'ai peur que tu puisses te négliger dans le but de rendre Hanako heureuse."


hi "Tu penses vraiment que Hanako ira bien ?"


li "Elle n'est pas aussi fragile que tu le penses. Je ne sais pas exactement ce qu'elle a vécu, ou ce qu'elle peut ressentir, mais elle a réussi à s'en sortir jusqu’à maintenant."


li "J’espère aussi que lui donner un peu d'espace lui permettra de décider ce qu'elle veut vraiment et de lui donner l'initiative pour cela."


li "Aie foi en Hanako. C'est tout ce que je demande."


hi "Je vais... y réfléchir."


li "C'est bien. Être pressé ne te mènera nulle part."


li "Je sais qu'à des moments tu peux douter de ta relation avec Hanako, mais elle est..."


"Lilly s’interrompt et prend un moment pour réfléchir à ce qu'elle veut dire."


li "Garde à l'esprit que je ne serais pas devenue amie avec toi si je n'avais pas pensé que tu es quelqu'un de fondamentalement bon. Tu es un bon ami, pour moi tout comme pour Hanako."


hi "Merci. Ça m'aide."


"Nous discutons un moment de tout et de rien, ce qui détend l’atmosphère, même si les tensions restent. Il y a beaucoup de choses que je ne sais pas sur le voyage de Lilly en Écosse, mais après un sujet aussi grave, je veux être seul pour réfléchir."

stop music fadeout 8.0

show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with None

scene bg school_dormhisao
show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with locationchange
with Pause (0.5)

hide phone
with None


"Après quelques minutes, nous faisons nos au revoir et je pose mon téléphone sur le bureau."


"Comparé à la situation de Hanako, la mienne me semble banale. J'ai toujours mes parents, j'ai eu une enfance normale, et contrairement à beaucoup à Yamaku, mon handicap n'est pas immédiatement visible."


"Mais une fois encore... ce n'est pas juste une façon de justifier la manière dont j'ai agi avec elle ?"


"Nos passés sont peut-être comme ça, mais pour le futur, je n'ai toujours aucune idée de ce que je veux faire. À l'école je me suis juste concentré sur le travail de chaque jour et j'ai négligé de plus en plus de choses pour m'occuper de Hanako."


"Je me rappelle de ce que m'a dit Mutou après la crise d'angoisse de Hanako, sur l’intérêt de Yamaku et sur mes études. En y repensant, il devait essayer de me dire exactement la même chose."


"Qu'est-ce que j'ai fait de mon temps depuis ma crise cardiaque ? Si j'ai réussi à faire sortir Hanako de sa chambre et la faire s'ouvrir un peu, alors quoi ?"


"Je regarde par la fenêtre du dortoir alors que le soleil se couche lentement. C'est une belle vue, mais ce que je savoure le plus est le silence alors que les étudiants rejoignent leurs chambres."


"Tout ce que je veux faire maintenant, c'est réfléchir. Je ne sais pas combien de temps j'ai, mais je veux réfléchir à ce que je vais faire à partir de là."

scene black
with dissolve




label fr_H22b:

stop music fadeout 5.0


"J'écoute avec attention ce que Lilly a à dire, mais je n'arrive pas à me résoudre à être d'accord avec elle."


"Hanako est déjà sensible la plupart du temps, et après ce qui est arrivé quand son anniversaire a été mentionné, je crois que la dernière chose à faire serait de la laisser seule alors qu'elle s'isole délibérément."


"J'ai l'impression que Lilly a déjà une idée très précise de comment s'occuper de Hanako. Pas juste maintenant, mais depuis que je la connais."


"Je réfléchis à la meilleure chose à faire et je me retrouve à dire à Lilly que je suis d'accord avec elle en étant le plus ambigu possible."


"Nous discutons un peu après, mais aucun de nous deux n'a vraiment l'esprit à ça après les événements récents. Nous nous disons au revoir avant de raccrocher."

show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with None

scene bg school_dormhisao
show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with locationchange
with Pause (0.5)

hide phone
with None


"Je veux parler à Hanako, l'aider du mieux que je peux. La meilleure chose pour elle pour l'instant est d'avoir quelqu'un près d'elle, de ne pas être seule."






label fr_H22c:

stop music fadeout 5.0


"J'écoute avec attention ce que Lilly a à dire, mais je n'arrive pas à me résoudre à être d'accord avec elle."


"Je veux être plus avec Hanako. Je veux être un meilleur ami pour elle, l'aider quand elle a besoin d'aide et être là quand elle a besoin de quelqu'un. Je crois que maintenant est l'un de ces moments."


"Le souvenir du gérant du magasin d'antiquités me trouble toujours un peu. N'importe qui jetant un regard à Hanako finit par la fixer, et je ne peux pas leur en vouloir pour ça sans être complètement hypocrite, vu ma propre réaction."


"Je n'aime pas ma cicatrice non plus, mais au moins je peux la couvrir avec quelque chose d'aussi simple qu'une chemise. Je n'imagine pas une vie où chaque jour j'essayerais de me cacher le plus possible."


"Et en plus de ça, Hanako n'a pas de gens proches d'elle qui l'aideraient sans tenir compte de son apparence. Je vis loin de mes parents, mais je peux toujours les contacter et leur rendre visite si j'en ai envie."


"Je réfléchis à la meilleure chose à faire et je me retrouve à dire à Lilly que je suis d'accord avec elle, tout en étant le plus ambigu possible."


"Nous discutons un peu après, mais aucun de nous deux n'a vraiment l'esprit à ça après les événements récents. Nous nous disons au revoir avant de raccrocher."

show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with None

scene bg school_dormhisao
show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with locationchange
with Pause (0.5)

hide phone
with None


"Il y a au moins une chose que je peux faire pour Hanako. Si je fais ce petit quelque chose pour elle, je peux espérer qu'elle accepte que je me rapproche un peu d'elle."





label fr_H23:



scene bg school_dormhanako_ni
show hanako_door_base at right
show hanako_door_door at left
with shorttimeskip

play sound sfx_hammer


play music music_tragic fadein 0.5


"Je frappe trois fois à la porte de Hanako. Comme je m'y attendais, il n'y a pas de réponse. J'envisage brièvement de frapper encore une fois, mais je sais que j'obtiendrai le même résultat qu'avant."


"Posant ma main sur la poignée de porte, j'essaye de préparer ce que je vais lui dire. J'ai beau essayer, je ne trouve rien de bien à dire. Je veux la réconforter, oui, mais je n'ai aucune idée de comment faire ça."


"Ça suffit pour m’arrêter. J'ai dit à Lilly que je le ferais, alors j'ai le sentiment que je dois continuer, que j'aie confiance ou non."


"Je tourne la poignée avec beaucoup d'hésitation. Elle ne tourne pas beaucoup, la porte étant verrouillée."


hi "Hanako..."


"Donc elle m'a vraiment enfermé dehors. Après tout ce qui est arrivé entre nous, et le temps qu'on a passé ensemble... elle me repousse complètement."


hi "Hum... je ne sais pas si tu peux m'entendre, mais..."


hi "Je veux juste te parler un peu. Si tu m'entends, peux-tu s'il te plaît ouvrir la porte ?"

with Pause(4.0)

play sound sfx_lock


"J’attends en silence. Plusieurs minutes passent, puis finalement j’entends des pas venir jusqu’à la porte et le verrou se tourner."


"Au moins elle a l'intention de m'écouter. C'est une bonne chose."


hi "Je... je ne sais pas vraiment quoi dire, mais... je voulais juste te voir. Je voulais m'assurer que tu allais bien."


"Je respire à fond avant de tourner la poignée et d'ouvrir la porte. Si elle l'a déverrouillée sans protester, elle doit bien vouloir que je rentre."

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
show hanagown distant:
    center
    ypos 1.15
with silentwhiteout


"Hanako est assise sur le bord du lit, son visage est assombri alors qu'elle réfléchit. Sa chambre est aussi austère que toujours, et à l'instant, elle semble convenir parfaitement à l'ambiance."

show hanagown normal
with charachange

show hanagown worry at center
with Dissolvemove(0.2)


"Finalement, elle lève lentement les yeux. Dès qu'elle remarque ma présence, elle bondit sur ses pieds, me faisant face."


"Sa robe trop grande donne l'impression que ses mouvements sont plus larges."


ha "Qu-qu'est-ce que tu... ?"


"Je regrette vite d'être entré après l'avoir regardée. Elle semble déprimée, mais il y a une légère colère dans sa voix. Donc elle peut même afficher ce genre d'expression."


hi "Je... Je voulais juste vérifier que tu allais bien. Je pensais que tu étais d'accord, vu que tu as déverrouillé la porte."

show hanagown distant_blush
with charachange


"Hanako ouvre la bouche pour parler, mais la referme vite avant de détourner le regard."

show hanagown distant_blush:
    center
    ypos 1.15
with charamove


"Nous restons en silence un moment, avant qu'elle ne recule et s'asseye sur le lit. Je ne sais pas si elle est frustrée et résignée au fait que je sois là, ou vraiment d'accord avec ma présence."


"Une fois de plus, je me retrouve complètement incapable de comprendre ses sentiments. C'est énervant."


"Je marche jusqu’à son bureau et prends un siège. Je le fais lentement, pour lui laisser le temps de me dire si elle a un problème avec le fait que je reste, mais elle ne dit rien. Tout ce qu'elle se contente de faire est regarder le sol, sans bouger un cil."


"Après m’être assis, je regarde Hanako. Elle est pâle, mais ses joues sont rouges. Je ne suis pas sûr qu'elle mange bien non plus, vu comme elle semble mince."


"Lilly a beau avoir dit qu'il serait mieux que je garde un peu mes distances avec elle, il est difficile de trouver une bonne façon d'agir avec Hanako quand elle est comme ça."


"Elle continue de regarder le sol sans dire un mot, comme si elle attendait que je dise quelque chose. C'est normal, vu que je suis celui qui est venu dans sa chambre."


hi "Tu veux qu'on aille quelque part ? Descendre la colline pour aller en ville est peut-être un peu trop, mais on pourrait aller se balader dehors."

show hanagown worry_blush
with charachange



ha "Pourquoi... tu veux faire ça ?"


hi "Je me disais juste que ça pourrait t'aider un peu. Tu passes trop de temps à l'intérieur, ta peau va devenir aussi pâle que celle de Lilly bientôt."

show hanagown distant_blush
with charachange


"Je ris un peu, espérant que Hanako fasse de même, mais elle ne réagit pas, elle se contente de regarder le sol."


ha "Si tu ne veux pas y aller... J-je ne veux pas y aller non plus."


hi "C'est pas un problème. J'ai joué au foot et traîné avec des amis après l'école avant de venir à Yamaku, donc j'aime bien être dehors."


"Hanako ne montre aucune réaction visible. Il est difficile de lui parler quand la discussion est si unilatérale."


hi "On pourrait aller à la bibliothèque... du moins si elle n'est pas fermée. Les jardins sont bien, aussi."


"Elle commence à jouer avec ses cheveux. C'est distrayant et semble un peu inhabituel pour elle."


"Encore une fois, depuis que l'incident en classe est arrivé, je marche sur la pointe des pieds par peur de lui faire mal une fois de plus. Essayer de la faire sortir peut être une bonne chose."


"Je me penche un peu plus et lui adresse un sourire légèrement forcé pour essayer de lui remonter le moral."


hi "Il n'y aurait personne à cette heure-ci, tu n'aurais pas à t’inquiéter que quelqu'un soit là. Ça pourrait être un petit rendez-vous ou un truc du genre."

show hanagown normal
with charachange


"Je ris un peu, mais vois que Hanako a arrêté de jouer avec ses cheveux et tient fermement le lit. La bouche de Hanako remue, mais j'ai beau me concentrer, je n'entends rien."


hi "Hanako ?"


ha "Tu... ne comprends pas..."


"Même maintenant, je peux à peine entendre ce qu'elle dit. J'ai l'impression qu'elle essaye de se faire la plus petite possible. C'est normal pour elle de le faire en classe ou quand il y a des gens, mais ça me fait mal qu'elle soit comme ça avec moi."


hi "Je te l'ai dit, c'est bon. C'est juste une petite balade, personne ne nous remarquera."


"Je me lève et vais en direction de la porte, me tournant pour inviter Hanako à me suivre. Encore une fois, elle ne répond pas à ce que j'ai dit."

show hanagown distant
with charachange


ha "Je ne..."


hi "Sortir un peu sera bien pour te vider la tête."


ha "Pourquoi tu... veux faire ça..."


hi "Parce que je veux t'aider."


ha "Je ne... veux pas... d'aide. Tu es juste venu... pour essayer de me faire sortir... ?"


hi "Ça ne me gêne pas. Je crois que tout le monde a besoin d'aide de temps en temps. Quand j'ai passé mes premiers jours à Yamaku, Lilly et toi, vous m'avez beaucoup aidé."


hi "Et puis de toute façon, je ne suis pas occupé."


ha "Je ne veux p-pas y aller. Je... vais bien."


hi "Je ne crois pas vraiment que ce soit sain de rester à l'intérieur aussi longtemps. Il y a encore un peu de soleil, il n'est pas trop tard pour se balader un peu."


hi "Ça me ferait sûrement du bien de faire un peu d'exercice de toute façon, pour me réveiller. J'ai des devoirs à faire et je ne voudrais pas m'endormir au milieu."

show hanagown normal
with charachange


ha "Alors... Vas-y."


hi "Tout seul ?"


"Elle hoche la tête."


hi "Ben, ça ne me gêne pas vraiment, mais... tu es sûre ? Je suis passé pour t'inviter à venir avec moi."

show hanagown distant
with charachange


ha "Je vais bien. Tu peux y aller."


hi "Aller, juste une petite balade."


ha "S'il te plaît, juste, pars. J-je suis bien ici."


hi "...Hanako ?"


"J'essaye de voir son visage pour jauger ce qu'elle ressent, mais son expression est masquée. Comme si elle était si fragile qu'un simple mouvement la briserait."


hi "Bon, si tu veux qu'on reste là... peut-être qu'on peut jouer à un jeu ?"


ha "Juste pars. S'il te plaît. Je ne... veux rien faire tout de suite."


hi "Il y a sûrement quelque chose que tu veux faire. Ça doit être ennuyeux d'être assise dans ta chambre toute seule."


ha "Je veux que tu partes."


hi "Allez, ne sois pas comme ça. Je veux juste passer du temps avec toi. Lilly et moi sommes inquiets, alors..."

show hanagown worry_blush
with charachange


ha "Tu... lui as parlé ?"


hi "Euh... ouais. On était... au téléphone, il y a un petit moment. On est tous les deux vraiment inquiets pour toi."

show hanagown irritated
with charachange


"Hanako marmonne quelque chose. C'est troublant."


hi "Hanako... ?"


ha "Je te dis... s'il te plaît, va-t'en. Tu ne comprends rien..."


hi "Si on discutait juste un peu, tu pourrais me dire ce que je ne comprends pas. Je veux juste te protéger, je ne vois pas vraiment..."


ha "Sors... s-s'il te plaît..."


hi "T'enfermer dans cette pièce n'aidera en rien, Hanako. S'il te plaît..."

stop music fadeout 2.0


"Silence."


hi "Hanako, je veux juste t'aider—{w=0.3}{nw}"

scene ev hanako_rage:
    truecenter
    subpixel True zoom 3.0
    0.25
    linear 0.2 zoom 1.05
    easein 8.0 zoom 1.0
with flash

play music music_rain


"Elle se lève soudainement de son lit, se tournant vers moi avec une expression qui me prend complètement par surprise."


ha "Sors de ma chambre, sors de ma chambre, sors de ma chambre... !" with vpunch


"Hanako me crie dessus avec une telle force que pendant un moment, je suis vraiment effrayé. Je... je n'ai aucune idée de comment réagir à cela, surtout que ça vient de Hanako."


ha "Pars ! Je te dis de partir !" with vpunch


hi "M-mais... J'essayais juste... de t'aider..."


ha "Je sais que j'ai besoin d'aide ! Je sais que je suis brisée ! Je n'ai pas besoin que tu me le dises !" with vpunch


hi "Je n'ai jamais dit que tu étais brisée, ou quelque chose du genre !"


ha "C'est écrit sur ton visage, c'est écrit sur le visage de Lilly, c'est écrit sur le visage de tout le monde !" with vpunch


ha "Je vois un thérapeute chaque semaine, Lilly se comporte avec moi comme si j'étais une enfant, et maintenant... même toi !" with vpunch


ha "Rien n'a changé, rien du tout ! Je déteste Lilly, et toi... je te déteste plus que n'importe qui... !" with vpunch


"Son visage se contorsionne. Je n'ai jamais vu quelqu'un sortir de ses gonds comme ça, mais on dirait que la fille calme et renfermée de d'habitude se transforme devant mes yeux."


"Je ne sais pas quoi faire. Je n'ai aucune idée de ce que je devrais dire ou faire."


ha "Pars ! Laisse-moi seule ! Sors d'ici !" with vpunch


"Je fais un pas en arrière, puis un autre, et un autre. Ma retraite est seulement interrompue quand je sens la porte contre mon dos."


"Je ne peux pas arranger la situation. Rien de ce que je dirais ne changerait quoi que ce soit maintenant. J'ai l'impression que je suis dans un étrange et troublant monde étranger. Je ne veux pas rester ici."


"La poignée de la porte me glisse entre les mains tandis que j'essaye de l'ouvrir sans tourner le dos à Hanako. Finalement, la poignée tourne. J'ouvre la porte aussi vite que je le peux et en tombe presque en arrière."


"Alors que je sors, je garde les yeux sur la fille en face de moi."


"Elle n'est pas brisée. Hanako n'est pas brisée. Si elle était brisée, alors je serais aussi brisée qu'elle après tout ce qui m'est arrivé. Lilly a seulement fait de son mieux, et j'ai seulement essayé de la protéger."

scene ev hanako_rage_sad:
    zoom 1.0
with charachange


"Hanako baisse le regard, toute son énergie s'évanouit. Maintenant que je suis ressorti de sa chambre, sa rage est partie."


"Mais même maintenant, je n'arrive pas à me décider à lui reparler. Ce n'est pas juste le choc de ce qu'elle m'a dit... j'ai l'impression que quelque chose d'autre m’arrête. Quelque chose de profond, qui me rend physiquement malade."

show bg school_dormhanako_ni:
    center
    xpos 0.55
    linear 5.0 center
show hanako_door_door:
    left
    xpos -0.2
    linear 5.0 left
show hanako_door_base:
    right
    xpos 1.1
    linear 5.0 right
with flash

stop music fadeout 4.0


"Sans un mot, je referme lentement la porte. Le bruit des vieux gonds est assourdissant."

play sound sfx_doorclose

show bg school_dormhanako_ni at center
show hanako_door_door at left
show hanako_door_base at right
with ease

"Avec un bruit final, la porte en bois se ferme. La Hanako que je pensais connaître disparaît derrière elle, et seule une légère ligne de lumière passe autour de la porte."

scene bg school_girlsdormhall
with locationchange


"Je me sens engourdi. Sans rien d'autre à faire, je commence à marcher en direction de ma chambre, plaçant mécaniquement un pied devant l'autre en faisant à peine attention à ce qui se passe autour de moi."


"Mon esprit s'emballe et je me questionne sur tout ce que je pensais savoir de Hanako."


"Mais une chose est sûre. Cette porte fermée signifiait plus que la fin d'une simple visite."



label fr_H24:



scene bg school_girlsdormhall
with locationchange

play music music_night fadein 4.0


"Après avoir parlé à Lilly à la fin de la journée, je m'assieds à mon bureau et regarde par la fenêtre, voyant les étudiants partir. Ils sortent habituellement en groupes, mais même quand ils partent seuls, ils disent au revoir à leurs amis."


"C'est une situation normale. Quelque chose que je n'aurais pas remarqué si ça avait été un autre jour, tellement la situation est commune."


"Mais c'est aussi quelque chose que Hanako n'a jamais vécu depuis que je la connais. Alors que je me tiens devant la porte de Hanako pour la seconde fois en deux jours, ce fait ne quitte pas mon esprit."


"Je tiens deux plats dans les mains. Qui ne sont pas... exactement les plus excitants des repas, mais je veux m'assurer que Hanako se nourrit bien. Ça peut aussi me servir d'argument pour qu'elle me laisse entrer."


"Lilly et moi avons fait de notre mieux pour être là pour elle. Depuis qu'elle a fait une crise d'angoisse, je veux protéger Hanako à tout prix. Que quelque chose comme ça puisse lui arriver encore une fois, ou même pire, je ne veux pas y penser."

scene bg school_dormhanako_ni
show hanagown distant_close:
    center
    xpos 0.39
show hanako_door_base at right
show hanako_door_door at left
with locationchange

play sound sfx_doorknock2


"Je frappe plusieurs fois à la porte tout en tenant avec précaution le plat dans mon autre main. Je doute que Hanako ouvre la porte juste pour moi, alors j’espère vraiment que le plat gagnera son attention."


hi "Bonsoir, Hanako. C'est juste moi."


"J'attends une réponse pendant un moment, mais sans surprise, je n'entends rien."


hi "J'ai... j'ai à manger pour nous deux. Je peux entrer ?"


"Pendant un moment qui me semble long, seules quelques voix étouffées au rez-de-chaussée peuvent être entendues."

play sound sfx_lock


"Puis j’entends le bruit de pieds nus sur le sol et je retiens un petit soupir de soulagement quand j’entends le verrou de la porte tourner."

play sound sfx_dooropen

show hanako_door_door:
    xpos -0.1
with charamove


"Quand Hanako ouvre la porte, je la regarde."

show hanagown normal_close
with charachange


"Elle regarde un moment le plat dans ma main gauche. C'est un curry modeste que j'ai rapidement fait avec un sachet tout prêt."

show hanagown distant_close
with charachange


"Ses yeux se dirigent vers le plat de ma main droite, qui tient la même chose, avant de baisser la tête."

hide hanagown
with charaexit


"Alors qu'elle retourne dans sa chambre, je réalise que je ne lui ai pas dit un mot. Je la suis, hésitant, légèrement embarrassé de l'avoir autant fixée."

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
with silentwhiteout


"Plus que jamais, l'ambiance grise et morose de la chambre de Hanako semble être un reflet de sa personnalité. Les voix venant de l’extérieur deviennent complètement inaudibles et le silence intérieur devient oppressant une fois que je referme la porte."


"Marchant au fond de la chambre, je place les deux plateaux sur son bureau. Je suis content qu'elle m'ait laissé entrer, mais une fois que je me retourne et la vois, je me demande si j'ai fait le bon choix."

show hanagown distant:
    center
    ypos 1.15
with charaenter


"Je ne pense pas que Lilly ait raison, cela dit. En voyant Hanako comme ça, je suis sûr que la laisser seule est la dernière des choses à faire. Je n'ai pas envie de l'imaginer, mais elle pourrait faire quelque chose d'idiot."


hi "Hum... c'est juste un repas instantané, mais ça devrait être nourrissant."


"Je prends un plat et lui tend. Elle le prend sans un mot et s'assoit sur le bord du lit. Je m'assois sur la chaise, et nous entamons chacun notre repas en plantant nos fourchettes dans le riz."


"Le curry en lui-même est... pas mauvais. Je n'en attendais pas plus d'un paquet dont je ne connaissais pas la marque, donc c'est déjà ça."


"Le repas fait qu'elle ne parle pas. Aucun de nous n'aime parler pendant que nous mangeons, et ça me rappelle les déjeuners qu'on a partagés si souvent."


hi "C'est agréable, de manger ensemble comme ça."

show hanagown worry
with charachange


"Hanako me regarde avec un drôle d'air. C'est déjà mieux que l'expression qu'elle avait jusqu’à maintenant."


hi "On est devenus amis surtout grâce à ces déjeuners, c'est agréable de refaire quelque chose comme ça."


"Elle hésite quelques secondes et ça me fait grimacer. J'ai dit quelque chose de mal ?"

show hanagown smile
with charachange


"Au bout d'un moment, elle sourit et hoche la tête. Ça m'aurait encouragé normalement, mais son sourire est un peu étrange. Je n'arrive pas à savoir pourquoi."


ha "Tout... est pareil qu'avant, hein ?"


hi "O-ouais. Bien sûr."


hi "Tu nous as toujours, Lilly et moi, pour t'aider et te protéger, et une fois qu'elle sera revenue, tout sera comme si elle n'était jamais partie."

show hanagown distant
with charachange


"Hanako hoche la tête une fois de plus, son expression restant exactement la même. Elle semble différente de la Hanako qui était devant moi quand je suis entré dans la pièce, c'est légèrement troublant."


"Nous finissons notre dîner après ce court échange. Même si Hanako semble mieux qu'avant, je continue de la regarder pour me rassurer."


"En peu de temps, le curry de Hanako est fini. Je finis le mien tandis qu'elle pose le plateau sur le bureau et je mets le mien par-dessus."


"Je me demande ce que je devrais dire, voulant désespérément éviter un autre silence gênant ou avoir à partir après si peu de temps, mais Hanako est celle qui brise le silence."

show hanagown worry_blush
with charachange


ha "Je... Je me demandais... vu que t-tu es là..."


"Elle se précipite vers l'un de ses tiroirs et après avoir cherché un peu, elle en sort son échiquier."

show hanagown smile
with charachange


ha "T-tu voudrais... jouer... ?"


"Cette fois, je n'arrive pas à empêcher le soupir de soulagement de sortir de mes lèvres."

hide hanagown
with charaexit

show bg school_dormhanako at left
with charamove_slow


"Je me dépêche d'accepter son offre et Hanako installe les pions pendant que je me lève et vais m’asseoir sur le lit."


"Encore une fois, Hanako me laisse entrer dans son monde, avec quelque chose d'aussi simple qu'une partie. J'imagine que j'angoissais juste sans raison."

show hanagown smile_close:
    center
    xpos 0.55
    easein 1.0 center
with Dissolve(1.0)


"Après que le jeu ait été mis en place entre nous sur le lit, nous finissons de placer nos pièces respectives dessus."


"Durant notre amitié, nous n'avons pas échangé beaucoup de mots. Quand nous sommes comme ça, je vois qu'on n'en a jamais eu vraiment besoin. Juste un simple livre, un échiquier, ou un repas entre nous est suffisant pour combler la distance."


"Je fais mon premier mouvement, tout comme j'ai toujours fait. Notre relation est comme ça, et elle sera sûrement toujours comme ça."


"Il y a quelque chose de différent cela dit, et je n'arrive pas à savoir quoi. Je regarde intensément Hanako, mais n'arrive pas à lire son expression."


"On a beau être proches physiquement, j'ai l'impression qu'on est très loin l'un de l'autre. Hanako est une personne fragile et je voudrais ne jamais lui faire de mal."


"C'est la façon dont les choses étaient, et c'est la façon dont les choses seront probablement toujours."

stop music fadeout 2.0






label fr_H25:



scene bg school_scienceroom at bgright
with locationchange


"Depuis que j'ai parlé à Lilly hier, je veux essayer de résoudre le problème du manque d'énergie que je ressens depuis mon arrivée à Yamaku."


"Mais même si j'essaye de me concentrer sur le livre, le siège vide de Hanako au fond de la classe me perturbe. Chaque fois que je commence à me recentrer sur le livre, mes yeux partent en direction de son bureau et je réfléchis."

show miki smile at center
with charaenter


"Une fois de plus mes yeux dérivent, mais cette fois ma vision est bloquée sur une certaine autre fille de ma classe."


hi "Oh, salut Miki."

show miki grinclosed
with charachange


mk "Peut-être que tu devrais manger. Je peux entendre ton estomac grogner depuis mon bureau."

play music music_happiness


"Je laisse ma tête tomber après sa remarque. Elle semble s'amuser de ma réaction et s'assied sur mon bureau. Le sourire qu'elle affiche tandis qu'elle fait ça me rappelle le Chat Cheshire."

show miki grin_close
with characlose


mk "Alors, sur quoi tu bosses ?"


hi "Les maths. J'ai un niveau décent, mais je voulais réviser."

show miki whistle_close
with charachange


mk "Oh vraiment ? Laisse-moi voir ça."


"Avant que je ne puisse objecter, elle prend le livre de mathématiques de mes mains. Elle regarde la page sur laquelle j'étais, gardant ouvert le livre avec son unique main, son bras gauche inutile posé sur sa cuisse."


"Depuis que je suis à Yamaku, j'ai vu que beaucoup des étudiants présents ont un handicap purement physique. Miki fait partie de ceux qui semblent avoir du mal."


"Son bras gauche a tendance à pendre le long de son corps, être glissé dans une poche, ou même mis de côté. Des fois elle a du mal à effectuer des tâches simples, ce qui la rend visiblement frustrée."


"Je me sens un peu mal de penser comme ça, mais je suis content que Hanako et moi n'ayons pas de handicap qui affecte notre liberté de mouvement."


"Cela dit... si le problème de Miki venait à empirer, au moins elle ne serait sûrement pas en danger de mort."

show miki smile_close
with charachange


"Elle réattire mon attention alors qu'elle feuillette les pages, regardant son contenu d'un œil tellement distrait qu'il est clair qu'elle ne pourrait pas m'aider dans la matière."


hi "J'imagine que ce genre de trucs ne t’intéresse pas ?"

show miki angry_close
with charachange


mk "À mort les maths. C'est super chiant."


"Elle repose avec indifférence le livre en face de moi. Elle remarque le cahier à côté dans lequel j'ai fait mes équations jusqu’à maintenant."

show miki confused_close
with charachange


mk "Attends, tu arrives à comprendre ce genre de trucs ?"


hi "Ouais."

show miki wink_close
with charachange


mk "Woaw. Je n'ai jamais parlé à un ordinateur avec des jambes auparavant."


hi "Merci... je crois. Au moins je m'en sors mieux là qu'en histoire."

show miki grin_close
with charachange


mk "Il vaudrait peut-être mieux demander de l'aide à la bibliothécaire. J'ai entendu dire qu'elle visait l'université."


hi "Ah, Yuuko ? Peut-être. Je ne sais pas ce qu'elle veut étudier, cela dit."


hi "Et toi ? Tu penses à ce que tu vas faire l'année prochaine ?"

show miki grinclosed_close
with charachange


mk "Moi ? Nan, pas vraiment. Juste apprécier le temps qui reste."


"Elle semble un peu gênée par la question et se frotte le bras gauche sans y penser. J'ai plus ou moins envie de lui demander ce qui s'est passé, mais je ne crois pas suffisamment la connaître pour ça."

show miki serious_close
with charachange


"La conversation se tarit et je m'adosse à ma chaise, abandonnant l'idée d'étudier. Miki remarque mon expression fatiguée et semble étrangement sérieuse."


mk "Tu penses à Hanako ?"


hi "Ça se voit tant que ça ?"

show miki wink_close
with charachange


mk "Tu as passé la matinée à regarder son siège et tu es plutôt silencieux. Pas trop dur de faire le lien."


hi "Je suis juste inquiet pour elle."

show miki serious_close
with charachange


mk "Ouais, je peux comprendre pourquoi. Elle est... bizarre, parfois."


"Elle semble gênée et je ne peux pas lui en vouloir. Hanako était compliquée à approcher avant qu'elle ne s'habitue à moi. Je ne la connais pas depuis si longtemps non plus, certaines de ses habitudes me sont toujours inconnues."


"Le trouble s'affiche sur mon visage. Si je n'avais pas développé de sentiments pour elle, ça aurait été plus facile à gérer."

show miki whistle_close
with charachange


mk "Sans vouloir l'offenser, cela dit. Ce n'est pas une mauvaise personne, ça je le sais."


label fr_H25a:


hi "Je sais, je ne l'ai pas mal pris. C'est juste plus difficile à gérer quand... tu sais. Quand tu as des sentiments pour quelqu'un."

show miki serious_close
with charachange


mk "Ouais, j'imagine bien. C'est difficile d'oublier ce qui lui est arrivé en cours, aussi."


"J'aurais aimé qu'elle ne me le rappelle pas. Elle a juste confirmé que c'était clairement visible par tous les autres dans la classe."


label fr_H25c:

show miki smile_close
with charachange


mk "Allez, ne sois pas si déprimé. C'était déjà arrivé, tu dois juste attendre que ça passe."


"Elle s'est enfermée dans sa chambre et agit comme une coquille vide, elle l'a déjà fait depuis qu'elle est à Yamaku et peut-être même avant, et je suis censé ne pas m'en inquiéter ?"


"Enfin, je dis ça, mais je ne peux rien faire. Je ne peux pas la forcer à sortir et elle voit un thérapeute, donc ce n'est pas comme si elle ne recevait aucune aide pour ses problèmes."


"Peut-être qu'il est normal de penser de cette façon quand on ne peut rien faire pour aider quelqu'un. “Elle est juste comme ça, et tu dois faire avec.”"

show bg school_scienceroom at center
show miki smile_close at twoleft
with charamove

stop music fadeout 3.0


"Alors que je rumine, je remarque un mouvement du coin de l’œil. Je regarde pour voir qui c'est et je suis pris par surprise."

show hanako invis:
    right
    xpos 1.1
with None

show hanako basic_normal at right
with dissolvecharamove


"C'est Hanako. Elle passe la porte comme elle l'aurait fait n'importe quel autre jour normal d'école, et commence à se diriger vers son siège à sa manière silencieuse habituelle."

show hanako emb_downtimid
with charachange


"Elle me regarde un moment avant de rougir et de détourner le regard, embarrassée, ce qui me fait réaliser que je la fixais. Je me sens désolé d'agir de cette façon, mais c'est difficile de ne pas le faire après tout ce qui est arrivé."

hide hanako
with charaexit

play music music_another fadein 4.0

show bg school_scienceroom at bgright
show miki grinclosed_close at center
with dissolvecharamove


"La fille assise sur mon bureau me regarde, souriante."

show miki grin_close
with charachange


mk "Tu vois ? Ta chérie est déjà revenue. Qu'est-ce que je t'avais dit ?"


hi "Tais-toi donc."


"C'était censé être une blague, mais sa remarque est si proche de la vérité qu'elle m'a mis mal à l'aise."

show miki smile
with charadistant


"Alors que nous discutons, quelqu'un à la porte appelle Miki. Elle descend de la table avant de se tourner vers moi."

show miki grin
with charachange


mk "J'dois y aller, Hisao. Rappelle-toi de manger, hein ?"


hi "Ouais, d'accord. À plus."

hide miki
with charaexit


"Elle me fait un geste de la main avant de se précipiter à la porte où un étudiant en uniforme de sport l'attend. Probablement quelqu'un du club d'athlétisme."

show bg school_scienceroom at right
with charamove_slow


"Saisissant l'opportunité, je me lève et vais au bureau de Hanako."

show hanako emb_timid:
    center
    ypos 1.15
with charaenter


ha "B-bonjour..."


hi "Salut, Hanako. Quoi de neuf ?"

show hanako emb_downtimid
with charachange


ha "R-rien..."


"Peut-être que lui parler aussi peu de temps après son retour en classe était une mauvaise idée."


hi "Tu veux qu'on aille prendre quelque chose à la cafétéria ? J'ai plutôt faim."

show hanako cover_worry
with charachange


ha "Mais... je pensais que tu voulais réviser."


"Les révisions peuvent attendre. Venir en classe après tout ce temps a dû demander beaucoup de courage à Hanako, donc le moins que je puisse faire est de rester avec elle."


"“Elle est juste comme ça, et tu dois faire avec” est la façon dont Miki, et probablement la classe entière, voient Hanako. Mais je peux faire plus pour elle. Je veux faire plus pour elle."


hi "Après avoir été distrait par Miki, je ne crois pas que je vais réussir à travailler. Allez, on y va."

show hanako basic_bashful at center
with dissolvecharamove


"Elle hésite, mais finit par se lever et nous commençons à marcher. C'est peut-être de petits pas pour elle, mais le fait qu'elle soit enfin sortie de sa chambre de sa propre initiative m'enlève un grand poids des épaules."

stop music fadeout 2.0

scene black
with dissolve



label fr_H26:

scene bg suburb_shanghaiint at bgright
with locationchange

play music music_dreamy fadein 2.0


"Mon stylo parcourt et remplit lentement une page de mon cahier. Mon autre main reste sur la page d'un livre de référence que j'ai emprunté à la bibliothèque, gardant les lignes intéressantes tandis que mes yeux font des aller-retours."


"Alors que je travaille, je fais des ronds et des cercles sur les feuilles photocopiées qui traînent sur la table en face de moi."


"Voulant changer d'air par rapport à la bibliothèque et éviter d'être distrait par des gens en classe, je décide de profiter du Shanghai pour étudier en silence."


"C'est agréable et silencieux comme je m'y attendais, et pouvoir boire un café pendant que j'étudie est un plus."


"Hanako est peut-être retournée à son état normal depuis qu'elle est sortie de sa chambre, mais j'ai fait l'opposé. On est peut-être retournés à notre routine habituelle, mais j'ai l'impression d’être différent."


"Peut-être que je ne le suis pas. Ça fait seulement quelques jours, après tout, que j'ai décidé de sortir du tréfonds dans lequel je suis tombé après mon accident. Mais je veux changer et je travaille maintenant activement dans ce but."


"Ou du moins, j'aimerais le croire."


hi "Erh, c'est impossible. Se forcer ne marchera pas."


"En plus, j'ai quelque chose d'autre à écrire après avoir fait ça. J'ai bien peur que ça ne soit pas plus facile."


yu "Hum..."


"Je lève la tête en direction de la petite voix."

show yuukoshang worried_up at center
with charaenter


"Yuuko se tient devant la table avec une serviette humide à la main, profitant apparemment qu'il n'y ait personne pour nettoyer les tables. Elle semble curieuse, fixant ce que j'ai en face de moi."


hi "Qu'est-ce qu'il y a ?"

show yuukoshang worried_down
with charachange


yu "Je me demandais juste... sur quel genre de travail tu avais tant de mal ?"


hi "Oh. C'est juste de l'histoire. Je suis pas mauvais en science et en maths, donc j’essaye de m'améliorer dans les autres matières."

show yuukoshang happy_up
with charachange


"Yuuko semble rayonner en entendant ça. J'ai l'impression d'avoir donné la bonne réponse à un jeu télévisé."

show yuukoshang closedhappy_down
with charachange


yu "Oh ! Je crois que je peux t'aider pour ça !"

show yuukoshang worried_down
with charachange


yu "Hum, si ça ne te gêne pas... bien sûr..."


"J'envisage brièvement de refuser son aide pour ne pas trop l’embêter, mais elle semble si excitée que je n'en ai pas le cœur. Ça serait méchant de lui refuser ça, après une telle réaction."


hi "Si tu veux bien m'aider, j'apprécierai."

show yuukoshang closedhappy_up
with charachange

hide yuukoshang
with charaexit


"Elle joint ses mains et se dépêche de poser sa serviette sur le comptoir avant de s’asseoir à côté de moi."

show yuukoshang invis at center
with None

show yuukoshang smile_down at Position(ypos=1.15)
with dissolvecharamove


"Je prends mon cahier et lui tends."

show yuukoshang neutral_up
with charachange


yu "Donc tu étudies la période Edo ?"


hi "Ouais. Mais je ne m'y connais pas trop, cela dit."

show yuukoshang worried_up
with charachange


"Elle prend mon cahier et lit quelques pages au hasard, mais l'aura d'enthousiasme qui émanait d'elle s'évanouit rapidement."


hi "J'imagine que ce n'est pas la période de l'histoire que tu espérais."

show yuukoshang worried_down
with charachange


yu "Malheureusement non. Mon domaine est l'histoire européenne, surtout celle de l’ère classique. Désolée."


"Elle semble un peu attristée, referme le cahier et le repose sur la table."

show yuukoshang smile_down
with charachange


yu "Tu voudrais un autre café ?"


hi "Mmh ? Oh, oui, bien sûr."

show yuukoshang invis at center
with dissolvecharamove


"Je m'avance et récupère mon cahier alors que Yuuko se lève, prend mon mug, et se dirige lentement vers le comptoir pour le remplir."


"Comme d'habitude, elle est silencieuse. Elle est totalement concentrée sur ce qu'elle fait pour ne pas en renverser ou faire tomber le mug blanc."


"Je profite de l’opportunité pour m'adosser et me relaxer un peu, le bruit de la machine à café résonnant dans la salle à part ça silencieuse."


"Ce sont des petits détails comme ça qui me montrent à quel point j'ai fini par apprécier les petites choses de la vie."


"Le calme d'une petite ville, la discipline et l'ordre de Yamaku, le vert de ses arbres qui étaient si rares dans ma ville natale, le rythme relaxé avec lequel les étudiants vivent leurs vies..."


"Tout semble si... sûr. C'est réconfortant."


"Je commence à m'assoupir quand la tasse vient se poser sur la table. Le café n'est pas arrivé trop tôt."

show yuukoshang neutral_down at Position(ypos=1.15)
with dissolvecharamove


"Yuuko se rassied et je passe ma main sur la tasse. Il est un peu trop chaud pour que je le boive de suite, alors je souffle un peu dessus."

show yuukoshang worried_down
with charachange


yu "C'est dommage que tu n'aimes pas tant l'histoire. Je me doutais que tu étais plus scientifique."


hi "Comment ça ?"

show yuukoshang smile_up
with charachange


yu "Tu as presque lu toute la section science-fiction de la bibliothèque. Ce n'était pas dur à remarquer."


hi "C'est pas faux. Bah, qu'est-ce que je peux dire ? Tu m'as plutôt bien jugé."

show yuukoshang neutral_down
with charachange


hi "On dirait que tu aimes vraiment l'histoire, vu à quel point tu étais précise. Tu étudies dans ce domaine ? Tu veux faire des fouilles outremer ?"

show yuukoshang closedhappy_up
with charachange


"Elle rit nerveusement."

show yuukoshang neurotic_down
with charachange


yu "J'aimerais visiter la Méditerranée un jour et voir la vieille architecture et l'art de mes propres yeux, mais je ne crois pas que je me ferais confiance pour manipuler des choses aussi fragiles."

show yuukoshang neutral_down
with charachange


yu "J'économise pour étudier à l'université bien que je me documente à chaque fois que j'ai du temps libre."


"Donc Miki avait raison pour ses aspirations universitaires. Vu comment elle s'en sort comme serveuse, un parcours axé sur la théorie correspond plus à Yuuko. C'est agréable d'entendre qu'elle a des ambitions, vu qu'elle travaille si dur."


"Je hoche la tête et prends une gorgée de café. Maintenant il est à la bonne température, alors je commence à boire en gardant un œil sur le livre, essayant de lire en même temps."


"Quelques minutes passent en silence, Yuuko regarde par la fenêtre et observe le monde défiler pendant que je bois mon café et étudie."

show yuukoshang closedhappy_up
with charachange


"Un mouvement attire mon œil et je lève la tête pour voir Yuuko sourire et faire un signe à quelqu'un à l'extérieur. Suivant son regard, cette personne se révèle être Hanako."


"Elle nous regarde depuis le trottoir d'en face. Sa timidité, qui d'habitude est si omniprésente, est peu visible, probablement grâce au faible nombre de personnes présentes."


"Elle décide de nous rejoindre et après un petit signe, elle regarde des deux côtés de la rue avant de traverser et de rentrer dans le café."

$ renpy.music.set_volume(0.3, 0.0, channel="sound")
play sound sfx_storebell

show hanako invis:
    right
    xpos 1.0
with None

show yuukoshang happy_up:
    twoleft
    ypos 1.15
show bg suburb_shanghaiint at center
show hanako basic_normal at tworight
with dissolvecharamove


"La sonnette familière du Shanghai résonne alors que Hanako entre et s'assied à la même table que nous."

show hanako cover_distant at Position(ypos=1.15)
with dissolvecharamove


ha "B-bonjour..."

show yuukoshang smile_down
with charachange


yu "Bonjour."


hi "Salut, Hanako. Quoi de neuf ?"

show hanako emb_smile
with charachange


ha "R-rien... juste... j-je me baladais... il fait bon."


hi "Ouais, je vois. Je suis content d'avoir décidé d'étudier ici au lieu de la bibliothèque."


"C'est agréable ici, plus que la bibliothèque où il y a des fois pas mal de monde. Je regarde Yuuko, qui hoche la tête en réponse."

show yuukoshang neutral_down
with charachange


yu "C'est agréable. Dommage que l'été ne puisse pas durer pour toujours."

show yuukoshang neurotic_up
with charachange


yu "Oh, désolée, euh, tu veux boire quelque chose ?"

show hanako basic_smile
with charachange

show yuukoshang neutral_down
with charachange


"Hanako secoue la tête. Heureusement cela suffit à calmer Yuuko."

show hanako basic_bashful
with charachange


ha "C-comment tu t'en sors avec tes révisions ?"


hi "Ça... va."


hi "Ah oui, tu as parlé à Lilly ?"

show yuukoshang smile_up
with charachange


yu "Ça m’intéresse aussi, comment est-ce qu'elle va ?"

show hanako cover_worry
with charachange


ha "E-elle s'amuse... je crois."


"Je... crois que nous la stressons surtout plus qu'autre chose. Être avec Yuuko la tend un peu."

show yuukoshang closedhappy_down
with charachange


yu "Ah, j'aimerais bien aller en Écosse un jour."

show yuukoshang happy_down
with charachange


yu "Des plaines vertes, des châteaux, des charmantes petites villes, des hommes en kilts, une histoire intéressante..."


"Les hommes en kilts ne m’intéressent pas tellement. Ça semble être un bel endroit cela dit."

play sound sfx_storebell

show hanako defarms_shock
show yuukoshang panic_up
with vpunch


"Alors que nous discutons, la sonnette résonne encore une fois. Hanako est surprise, remarquant l'expression paniquée de Yuuko à l'idée qu'elle puisse avoir à faire attendre les clients quelques secondes, vu qu'elle discutait avec nous."

show yuukoshang worried_down at twoleft
with Dissolvemove(0.3)

with Pause(0.2)

hide yuukoshang
with charaexit


"Yuuko nous abandonne après une brève révérence, puis se hâte d'aller accueillir les nouveaux clients, un vieil homme et sa femme. Je la regarde un moment, me tordant la nuque pour avoir un bon angle de vue."

show hanako def_worry
with charachange


"Hanako me regarde de son seul œil visible."

show hanako def_worry:
    center
    ypos 1.15
show bg suburb_shanghaiint at bgleft
with charamove

show hanako emb_downtimid
with charachange


"Elle tourne la tête, embarrassée, alors que j'ai un contact visuel avec elle."


hi "Je me disais juste que c'est bien d'avoir des ambitions pour l'avenir. Yuuko me parlait un peu de ce qu'elle voulait faire à l'université."

show hanako emb_timid
with charachange

ha "Oh."


hi "C'est dommage. Si elle n'était pas si nerveuse et overbookée, je crois qu'elle serait heureuse."


"J'ai beau avoir bien envie de boire quelque chose avec Hanako et de discuter avec elle, je dois travailler aussi. Pour être honnête, je ne crois pas que le fait que Yuuko m'ait distrait ait aidé non plus."


hi "Désolé si je suis un peu distrait. J'ai besoin de m'occuper de ça, sinon je vais me planter à l'examen d'histoire."


"Je passe la main dans mes cheveux par frustration. Je dois m'occuper de la lettre aussi, une fois que je serai retourné au dortoir."


hi "J’espère que j'aurai plus de chance avec ça qu'avec l'histoire. Rah."

show hanako emb_downtimid
with charachange


ha "D-de quoi ?"


hi "Oh, euh... Je voulais... écrire à Iwanako. Cela dit, là c'est plus important."


"J'ai seulement réussi à me déconcentrer. Je n'arrive pas à me concentrer sur mon travail alors que mon estomac se tord lentement quand je pense à lui répondre, après tout ce temps."


"Je me force à me concentrer sur le livre, ramassant mon stylo après avoir bu une gorgée de café."

show hanako basic_distant
with charachange


"Après quelques secondes, Hanako arrête de me regarder silencieusement et s'adosse à son siège, se relaxant autant qu'il est possible pour elle de le faire, regardant par la fenêtre pour passer le temps."

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
stop music fadeout 3.0


"Nous restons comme ça un long moment avant de repartir ensemble pour les dortoirs. Je suis surprise qu'elle ait eu la patience de m'attendre."

scene ev hisao_letter_open
with shorttimeskip

play music music_night fadein 1.0


"La lettre d'Iwanako est sur mon bureau à côté d'une feuille de papier et d'une enveloppe inutilisée. Le cliquetis de mon stylo est le seul son audible à cette heure de la nuit."


"Comme j'en avais peur, ma seconde tâche de la journée s’avère être aussi difficile que la première, si ce n'est plus."


"Ça fait tant de mois que nous ne nous sommes pas vus. Pourtant, je peux toujours me rappeler à quoi elle ressemble, le son de sa voix et comment elle agissait. Maintenant, cela dit, les petits détails commencent à s'effacer."


"La première fois que j'ai vu sa lettre, j'ai à peine reconnu son écriture. Même le stylo rose qu'elle utilisait toujours était sorti de ma mémoire jusqu’à ce que sa façon d'écrire me rappelle tout cela."


"Je me demande pourquoi elle ne l'a pas utilisé pour la lettre, elle avait l'habitude de tout écrire avec. Peut-être qu'elle pense que c'est trop immature maintenant."


"Je devrais réfléchir à ce que je veux lui dire. Je n'arrive pas à me concentrer. Je pense au passé qu'on a partagé avant qu'il nous soit enlevé aussi brusquement."


"Les décorations joyeuses et légèrement criardes lui conviennent bien. Ramassant la lettre et la regardant, je soupire."


"C'est le dernier lien me raccordant à mon passé. Iwanako n'a pas soudainement cessé d'exister quand elle est sortie de ma chambre d’hôpital pour la dernière fois, mais j'avais besoin de cette lettre pour me le rappeler."


"J'avais tous ces sentiments que je repoussais. J'avais l'impression de ne pas en avoir besoin, que je pouvais recommencer complètement ma vie. C'était plus facile comme ça."


"En fin de compte, j'imagine que c'était une façon naïve de penser. Tôt ou tard, mon passé m'aurait rattrapé d'une façon ou d'une autre."


"Mais qu'est-ce que je suis censé lui dire ? “Merci d'avoir mis un point final” ? Tout ce que la lettre a fait est mettre fin au faux sentiment d'aboutissement que je ressentais."


"J'ai beau essayer, je n'arrive pas à écrire un seul mot sur la feuille en face de moi. Je n'arrive même pas à trouver ce que je veux dire exactement."

stop music fadeout 4.0

scene bg school_dormhisao_ss
with locationchange


"Posant la lettre au-dessus de la feuille vierge, je rassemble mes affaires et les range dans le tiroir."


"Le bruit que le bureau fait alors que je referme le tiroir me rend un peu nerveux, étant déjà frustré, et je me lève et vais prendre une boisson au distributeur du rez-de-chaussée."

scene bg school_dormhallway
with locationchange


"J'ai essayé, mais je n'ai pas réussi. Après tout ce temps, je ne sais toujours pas comment faire avec Iwanako."

scene black
with dissolve



label fr_H27:

scene bg school_library
with locationchange

play music music_happiness


"La bibliothèque, bien que pas pleine à craquer, est visiblement plus remplie que d'habitude. Les examens sont proches et ça se reflète sur le nombre d'étudiants ayant le nez dans des livres aux tables autour de nous."


"J'ai beaucoup révisé ces derniers jours, tout comme eux, dans l'espoir de réussir mes examens. Ça veut aussi dire que Hanako et moi avons moins joué ensemble, donc elle a commencé à étudier aussi pour passer le temps."


"Néanmoins, aujourd'hui elle semble m'avoir oublié."


"Le manuel en face de moi est à la même page depuis longtemps. Après tant de temps passé à lire sur des sujets qui ne m’intéressent pas du tout, j'ai fini par divaguer."


"Mes yeux se dirigent là où Hanako serait habituellement, comme je faisais quand elle n'était pas en classe. Son pouf habituel dans le coin de la pièce est vide."


"C'était la première fois où nous nous sommes rencontrés, j'ai essayé d'engager une conversation avec elle, et elle a fini par s'enfuir."


"Je ne devrais probablement pas sourire en y pensant, mais c'est plutôt amusant. Aujourd'hui, il serait de plus en plus étonnant qu'elle fasse quelque chose comme ça. Même avec Lilly partie, elle va bien depuis qu'elle est sortie de sa chambre."


"Je veux lui parler, ou au moins faire une autre partie avec elle. J'en ai marre d'étudier et ça fait plusieurs jours qu'on n'a rien fait ensemble."


"Savoir où se trouve Hanako n'est pas si difficile. Si elle n'est pas à la bibliothèque, alors elle doit être dans la salle où on boit le thé pour être au calme, ou dans sa chambre."


"Décidant de vérifier dans cet ordre-là, je range mes affaires et sors de la bibliothèque."

stop music fadeout 5.0


scene bg school_girlsdormhall
with shorttimeskip


"Je m'étire pendant que j'avance dans le couloir. Étudier peut être frustrant parfois, mais avec les progrès que je pense avoir faits, je ressens un peu de fierté d'avoir accompli ça. C'est agréable."

scene bg school_dormhanako_ni
show hanako_door_base at right
show hanako_door_door at left
with locationchange


"Je n'entends rien depuis l'extérieur alors que je me tiens devant la chambre de Hanako. J'imagine que ce n'est pas très indicatif du fait qu'elle soit là ou non, vu à quel point elle est silencieuse."


"Cependant, elle n'était pas dans la salle où on boit le thé. Je frappe doucement à la porte pour lui signaler ma présence et je suis surpris de voir que la porte est déverrouillée et même pas fermée."

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
show hanako basic_distant:
    center
    ypos 1.15
with silentwhiteout


"Avec un léger craquement, la porte s'ouvre. On dirait que mes suppositions étaient correctes, Hanako est là."


"Elle est assise à sa table avec un livre ouvert en face d'elle, mais n'y prête aucune attention tandis qu'elle regarde par la fenêtre. Elle semble ne pas remarquer ma présence."


"Avec le menton posé sur sa main, elle semble calme et apaisée. Dommage qu'elle n'ait pas l'air comme ça plus souvent."

show hanako basic_distant_close:
    center
    ypos 1.1
with characlose


"Souriant un peu, je marche jusqu’à elle et lui parle doucement."


hi "Bonjour, Hanako."

show hanako basic_normal_close
with charachange


"Hanako tourne légèrement la tête pour me voir, mais elle n'est encore qu'a moitié présente. Je pose une main sur la table et baisse la tête pour mieux la voir, quelque peu curieux de savoir son humeur."


hi "Quoi de neuf ?"

show hanako basic_worry_close
with Dissolve(0.2)


"Elle sursaute un peu, étant finalement consciente de ma présence dans la pièce."


"Hanako rougit très fortement. Sa bouche est très légèrement ouverte, comme si elle avait été interrompue au milieu d'une phrase. Ce qui est plus étonnant cela dit, est ce qu'elle fait."

scene ev hanako_eye:
    truecenter
    subpixel True zoom 0.9
    acdc_warp 20.0 zoom 1.0
with locationchange


"Elle me regarde directement. Ses yeux sont rivés aux miens, tellement proches que je peux presque me voir dans leur reflet. Ils ne se détournent pas, et ne bougent pas. Ils sont absolument immobiles. Fixés sur les miens."


"Ils sont sombres et lui donnent un air concentré. Même lorsqu'elle lit des choses qui ne l’intéressent pas, elle semble être appliquée plutôt qu'ennuyée. Elle retient très bien les informations, et même maintenant, je le ressens."


"J'ai l'impression de voir quelque chose que je n'avais jamais vu derrière ces yeux. Je ne sais pas quoi."


hi "Hanako... ?"


"Ses lèvres bougent un peu, comme si elle était sur le point de dire quelque chose, mais ne le fait pas."


"Mais Hanako est comme ça. Sur le point de dire quelque chose, mais finit par ne jamais le faire. Alors que je regarde intensément dans ses yeux, je réalise quelque chose."


"Tout le monde a son propre avis sur les choses, des choses qu'ils veulent dire, leur propre vision du monde. Mais je n'arrive pas à entendre ce que veut dire Hanako et je ne comprends pas son avis sur les choses. Je n'en ai jamais été capable."


"C'est frustrant. J'ai l'impression de ne pas la connaître du tout, malgré tout le temps qu'on a passé ensemble."


ha "Hi... sao..."

scene bg school_dormhanako
show hanako basic_worry_close
with charachange


"C'est seulement maintenant que je me rends compte que je rougis. Je regarde directement dans les yeux de Hanako à une si courte distance et elle regarde dans les miens sans vaciller."

show hanako emb_downtimid_close
with charachange


"Je détourne rapidement le regard et couvre mon visage de ma main. Hanako fait de même."


"Un autre silence gênant règne. Je déteste ça. Au début je les acceptais comme normaux avec Hanako, mais maintenant ils semblent juste nous montrer à quel point nous n'arrivons pas à communiquer."


"De la colère se glisse dans le mélange complexe d'émotions que je ressens. Je veux combler le vide entre nous. Des amis ne devraient pas avoir à tâtonner comme ça."


"Je parle avant de débattre avec moi-même de ce que je vais faire. Ma cicatrice n'est pas aussi grave que celle de Hanako et je ne peux pas comparer ma vie à la sienne, mais je veux lui montrer qu'elle n'est pas seule."


"Faire ça d'une manière aussi crue est la seule façon de faire passer le message."


hi "Hanako... je veux te montrer quelque chose."

show hanako emb_timid_close
with charachange


"Je respire à fond pour me préparer. Ça pourrait provoquer un très mauvais revers de flamme, mais j'ai l'impression qu'on est assez proches pour ça."


hi "Je ne vais pas me mettre tout nu ou quoi que ce soit de bizarre, je vais juste retirer ma chemise."

show hanako def_shock_close at center
with dissolvecharamove


"Les yeux de Hanako s'écarquillent comme des soucoupes. Son visage affiche un mélange de curiosité et de nervosité. Ça m'aide à évacuer un peu de ma nervosité à faire ça devant quelqu'un."

play sound sfx_rustling


"Lentement, avec mon corps se tendant entièrement, je défais ma cravate et enlève le premier bouton. J'essaye d'ignorer Hanako pour rendre les choses plus faciles, mais ça ne marche pas vraiment."


"Alors que je continue en descendant, je m'attends à entendre une protestation de sa part. Cependant, elle reste silencieuse, ce qui rend ça encore plus étrange."


"Avec le dernier des boutons de ma chemise enlevé, je respire à fond et la regarde."

scene ev hisao_scar_large:
    xanchor 0 yanchor 0 xpos -600 ypos -140
with whiteout

play music music_heart fadein 0.5


"Le regard de Hanako est fixé sur ma cicatrice, comme prévu, et une fois que je hoche la tête pour lui dire qu'elle peut, elle s'avance et place timidement sa main sur la ligne verticale traversant ma poitrine."

show ev hisao_scar_large:
    ease 1.0 xpos 0 ypos -290


"La cicatrice sur sa main, la peau endommagée dessus, contraste avec la ligne uniforme dont est faite la mienne. Sa main ne tremble pas du tout, contrairement à ce que j'aurais cru."


ha "C'est..."


hi "La cicatrice de la chirurgie qui a suivi ma crise cardiaque. Ils ont dû ouvrir ma poitrine pour opérer mon cœur."

show ev hisao_scar_large:
    ease 1.0 xpos -600 ypos -140


ha "Je ne savais pas..."


"Les mots de Hanako sont plus calmes et posés qu'à l'habitude. La douce sensation de ses doigts passant sur ma cicatrice me fait hésiter avant de continuer."


hi "Tu es la première personne à la voir depuis que je suis sorti de l’hôpital."

scene ev hisao_scar:
    truecenter
    zoom 1.05 subpixel True
    easein 8.0 zoom 1.0
with flash


ha "Mais... pourquoi est-ce que tu me la montres ?"


hi "Je voulais me prouver que je pouvais le faire, que je pouvais accepter mon passé et avancer. Je voulais te la montrer aussi."


"Elle hoche la tête. D’après sa réaction, elle semble savoir à quel point c'est difficile pour moi. Plus que tout, cette cicatrice est un rappel visible de ma condition. Un rappel que je ne suis plus “normal”."


"C'est quelque chose que, jusqu’à maintenant, j'ai essayé d'ignorer."


"Alors que les minutes passent, le regard de Hanako se balade. Ses yeux s'éloignent un peu de ma cicatrice. La situation est quelque peu différente d'avant et me met mal à l'aise."

scene bg school_dormhanako
show hanako basic_normal_close at center
with silentwhiteout


"Elle retire sa main et je commence à reboutonner ma chemise. Son visage rougit et repasse soudainement à son attitude timide et tendue tandis qu'elle éloigne son regard."


"La pièce est complètement silencieuse pendant que je remets ma cravate, me sentant un peu gêné après un moment aussi intime."


hi "Donc... Apparemment tu n'es pas la seule à avoir une cicatrice."

show hanako basic_smile_close
with charachange


"Hanako sourit un peu à la blague, allégeant heureusement un peu l’atmosphère."


ha "Merci... H-Hisao. Je crois... que je comprends."


"Je pousse un long soupir de soulagement. Je ne savais vraiment pas comment elle le prendrait, mais je suis content que ce soit bien passé. Le sourire de Hanako me le prouve."


"Je suis en train de trouver le chemin que je veux suivre et Hanako a besoin de trouver le sien. C'est une chose qu'elle doit faire par elle-même et c'est une chose dont elle a besoin pour mettre derrière elle son passé."

show hanako basic_distant_close
with charachange


"Hanako regarde sa montre. Il se fait tard maintenant."

show hanako basic_worry_close
with charachange


ha "Hisao... hum..."


hi "Ouais, je ferais mieux d'y aller. Je ne suis pas mécontent d'aller me coucher. Ça a été une longue journée, après tout."


hi "Bonne nuit, Hanako."

show hanako basic_bashful_close
with charachange


ha "B-bonne nuit."

stop music fadeout 3.0

scene bg school_girlsdormhall
with locationchange


"Je sors de sa chambre et marche dans le couloir en silence. Je crois que nous avons eu tous les deux notre lot d'émotion pour la journée."

scene black
with dissolve



label fr_H28:

scene bg city_street1
with locationchange

play music music_daily fadein 2.0
$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_traffic fadein 2.0


"La chaleur de l'été me fait transpirer et des gouttes perlent sur mon front. Passer un mouchoir ne m'aide pas tellement à me mettre plus à l'aise."


"Abandonnant l'idée d'en faire plus aujourd'hui, je m’arrête et m'adosse à l'une des clôtures, posant mon sac sur le sol."


"Les magasins dans la ville en bas de Yamaku ont assez de choses pour me convenir, mais une sortie occasionnelle dans le quartier commercant d'une grande ville est parfois nécessaire."


"J'y ai été quelques fois. La ville commençant à m’être familière, le sentiment de nostalgie s'estompe quelque peu."


"Je réalise que je respire fort. J'ai l'impression d’être un vieil homme qui a fait trop d'efforts, c'est un peu perturbant."


"Je mets une main sur ma poitrine et me concentre un peu pour m'assurer que je n'ai pas exagéré au point de me causer un problème plus grave."


"Heureusement, mon cœur agit normalement. Il n'y a pas de douleur et le battement est régulier, bien qu'un peu rapide, normal après avoir fait ce genre de choses alors qu'il fait aussi chaud."


"Je déteste mon corps. C'est frustrant d’être freiné, encore plus d’être freiné par peur de mourir en faisant quelque chose d'aussi simple que marcher en ville."

$ renpy.music.set_volume(0.2, 0.0, channel="sound")
play sound sfx_phone


"Alors que je pense à ma santé, je sens ma poche vibrer. Au moment où mon téléphone commence à sonner, ma main est déjà dessus."


"Un regard sur l'écran me montre un numéro appelant que je ne reconnais pas. Étrange."

$ renpy.music.set_volume(0.1, 2.0, channel="ambient")
$ renpy.music.set_volume(0.5, 2.0, channel="music")

scene bg city_street1_blurred
show phone mobile:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with locationchange
with Pause (0.5)


"Haussant les épaules, je prends l'appel et porte le téléphone à mon oreille."


hi "Bonjour, Hisao Nakai à l'appareil."

mystery "…"


"Quelques courtes respirations peuvent être entendues, mais aucune voix."


hi "Allô ?"


ha "H... Hisao ?"


"C'est Hanako. Sa voix est vraiment facile à reconnaître, même si je ne lui ai jamais parlé au téléphone."


hi "Hanako ? Désolé, je ne m'attendais pas à ce que tu m'appelles. Quoi de neuf ?"


ha "E-euh... Je... euh..."


ha "Si... si tu n'es pas occupé... J-je me demandais si t-tu voulais... a-aimerais me... rej—"


hi "Rejoindre ?"


ha "Oui ! E-euh... Je veux dire..."


"Elle semble avoir beaucoup de mal. Je peux entendre des voix étouffées en bruit de fond et il est à peu près l'heure du thé, donc j'imagine qu'elle veut que je la rejoigne au Shanghai ou un truc du genre."


hi "Ça me va. Tu es au Shanghai ?"


ha "J-je suis... en ville..."


"Hanako est ici ? Seule ? C'est surprenant. Ça ne m'étonne pas qu'elle soit comme ça, si elle est entourée de gens et toute seule."


hi "Ça tombe bien, j'y suis aussi. Où est-ce que tu es ?"


"Hanako arrive à bégayer une adresse et des indications de direction basiques de l'endroit où elle se trouve. Heureusement elle n'est pas loin, donc je lui dis que j'arrive tout de suite juste avant de raccrocher."

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
$ renpy.music.set_volume(1.0, 1.0, channel="music")
stop ambient fadeout 2.0

show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 0.5 ypos 0.6
with None

scene bg misc_sky
with locationchange

stop music fadeout 5.0


"Je regarde le ciel. Le soleil d'été tape fort."


"C'est la première fois que Hanako me propose de faire quelque chose ensemble mis à part une partie de jeu. Et c'est la première fois, du moins depuis que je la connais, qu'elle va en ville toute seule. Peut-être que ça signifie que Lilly avait raison."

scene bg city_karaokeint
with shorttimeskip

$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_soothing fadein 2.0
$ renpy.music.set_volume(0.4, 0.0, channel="ambient")
play ambient sfx_crowd_outdoors fadein 2.0


"Au moment où j'arrive au café où se trouve Hanako, j'ai recommencé à respirer fort. Je transpire tellement que j'ai l'impression d’être une glace fondante, et j'arrive à peine à tenir mon sac dans ma main."


"J'ai besoin de m'asseoir, vraiment."


"Les tables à l'extérieur sont toutes occupées par des couples discutant et des filles se racontant des potins. Le contraste d'âge entre les groupes d'ici et les gens de la ville à côté de Yamaku est énorme."


"Je regarde les gens assis aux tables, mais ne trouve pas Hanako. Elle a dit qu'elle était à l'extérieur, alors j'ai juste dû la louper. Pas si difficile, vu à quel point elle se fait petite d'habitude."


"Je regarde encore une fois, plus lentement cette fois, prenant un soin particulier à chercher le chapeau de Hanako. Il se reconnaît facilement et je serais très surpris si elle ne le portait pas."


"La voilà. La tête baissée et assise à une table dans un coin collé au bâtiment."

$ renpy.music.set_volume(0.2, 4.0, channel="ambient")


"Je marche jusqu’à elle et m'assure d'avoir son attention avant de m’asseoir, ne voulant pas lui faire peur. Elle me remarque et me fait un petit signe alors que j'arrive à sa table."

show hanako basic_worry_cas_close:
    center
    ypos 1.1
with charaenter


ha "T-tu te sens bien ?"


"Je fais de mon mieux pour en rire, mais ce fait me fatigue encore plus."


hi "Pas très en forme ces jours-ci. Ne t'en fais pas pour ça."

show hanako basic_distant_cas_close
with charachange


"Hanako hoche la tête, mais semble toujours un peu embêtée."


"Maintenant que je peux bien voir son visage, quelque chose semble différent. Je ne sais pas si ce sont mes yeux qui me jouent des tours, mais elle est vraiment jolie et semble être calme."

show hanako basic_normal_cas_close
with charachange

show hanako basic_distant_cas_close
with charachange


"Ses yeux se lèvent vers moi avant de rapidement se rebaisser. Je commence à penser que ça va être un long moment silencieux, mais une serveuse arrive et pose une tasse de thé devant Hanako."

show hanako emb_downtimid_cas_close
with charachange


"Hanako se tourne et baisse un peu la tête presque automatiquement. C'est un geste qu'elle a dû beaucoup utiliser et il est très efficace pour cacher ses cicatrices."


"Son bras droit est toujours posé sur la table et la cicatrice sur sa main est visible. Elle l'attire l’œil de la serveuse et je me dépêche de la distraire."


hi "Excusez-moi, je pourrais commander ?"


"La serveuse hoche la tête et m'accorde quelques secondes pour regarder le menu."


hi "Pourrais-je avoir un smoothie à la mangue, s'il vous plaît ?"


"Elle hoche la tête avant de retourner de manière enthousiate à l’intérieur du bâtiment. Tout est si différent en ville, de beaucoup de façons."

show hanako emb_timid_cas_close
with charachange


"Hanako me regarde et ajuste un peu son chapeau. Si elle a vu que la serveuse regardait ses cicatrices, elle ne le montre pas."


ha "P-pas de café... ?"


hi "Je crois que si je prenais un café avec cette chaleur, j'en mourrais."

show hanako emb_downtimid_cas_close
with charachange


"Posant mon menton sur la main, je regarde mon amie silencieuse. Elle semble un peu gênée, une réaction inattendue à ma mauvaise blague. Une émotion dont je me serais passé surgit en moi alors que je comprends pourquoi."


"Contrairement à beaucoup d'autres dans Yamaku, ma condition va plus loin que de me limiter dans mes activités. Ou pour être précis, dépasser ces limites pourrait avoir de plus graves conséquences."


"Heureusement, c'est arrivé très rarement depuis que je suis à Yamaku. Je pensais que c'était tellement rare que Hanako et Lilly n'y penseraient pas du tout. Il s’avère que j'avais tort."


"Hanako boit silencieusement son thé pendant que j’attends ma boisson, s'assurant qu'il est à la bonne température avant de le boire plus franchement."


"Je me sens coupable d’être la cause d'un silence aussi inconfortable, vu que dans le passé j'ai tenu rigueur à Hanako du même genre de silences."


"Au bout d'un moment, la serveuse arrive en bondissant presque et me tend ma boisson. Je sors de la monnaie de ma poche et lui mets dans la main, avant qu'elle aille s'occuper d'un autre client. Mes yeux la suivent tandis qu'elle part."

show hanako emb_sad_cas_close
with charachange


ha "Tu trouves qu'elle est... belle... ?"


"Hanako suit mon regard et ses yeux s'attardent sur la serveuse qui nous a servis. Je peux sentir le sang me monter aux joues alors que je prends le smoothie qui est sur la table."


hi "Nan, c'est pas mon type. Elle ressemblait beaucoup à une vieille amie que je connaissais avant ma crise cardiaque."

show hanako basic_worry_cas_close
with charachange


ha "Tu... avais beaucoup d'amis ?"


hi "J'en avais quelques-uns dans mon ancienne école, mais pas beaucoup. On était juste quatre à traîner ensemble après l'école et tout ça."

show hanako basic_normal_cas_close
with charachange


ha "Tu leur parles toujours ?"


"Je secoue la tête."


hi "Non. On a progressivement perdu contact quand j'étais coincé à l’hôpital."

show hanako cover_worry_cas_close
with charachange


ha "Tu n'es... pas triste ? Ou énervé ?"


"Hanako semble surprise. J'imagine que c'est une réaction normale."


hi "Bah, leur vie a continué d'avancer pendant que j'étais coincé. Je l'avais plutôt mal pris à l'époque, mais maintenant je garde surtout de bons souvenirs."


hi "Et puis maintenant que je suis à Yamaku, j'ai de nouveaux amis."


"C'est une version bien épurée de ce que je ressentais à l'époque. Je suis passé à travers des périodes sombres durant mon séjour à l’hôpital, et je suis vraiment content que Hanako et Lilly aient été là pour m'aider quand je suis arrivé."

show hanako basic_bashful_cas_close
with charachange


"Hanako rougit tandis que nous apprécions nos boissons. Elle semble s’être calmée depuis que je suis arrivé, et je me sens un peu mieux depuis que je suis assis, ça promet d’être un bon après-midi."


"Même si elle est plus calme qu'avant, elle continue de gigoter un peu. Elle passe une main sur sa frange comme si elle cherchait quelque chose à dire."


hi "Ah oui. Je voulais te demander..."

show hanako emb_timid_cas_close
with charachange


"Hanako penche la tête d'un air curieux."


hi "Je ne savais pas que tu avais un téléphone portable. Comment tu as eu mon numéro ?"

show hanako emb_smile_cas_close
with charachange


ha "L-Lilly... me l'a... donné."


"J'aurais dû le deviner."


hi "Tu sais, t'aurais pu me demander aussi, je te l'aurais donné."


hi "Tu veux qu'on échange nos adresses e-mail ?"

show hanako basic_bashful_cas_close
with charachange


"Hanako hoche la tête, pose sa boisson et sort le téléphone de sa poche alors que je fais de même."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

show hanaphone:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)


"Étonnamment, elle a le même modèle que moi. En rose cela dit."


hi "Beau téléphone."

show hanako basic_smile_cas_close
with None


$ renpy.music.set_volume(1.0, 1.0, channel="music")

show hanaphone:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide hanaphone
with None


"Elle me regarde avec une expression curieuse, puis remarque mon téléphone et rit un peu. C'est l'une des seules fois où j'ai vu Hanako baisser suffisamment sa garde pour rire."

show hanako cover_bashful_cas_close
with charachange


ha "Je ne l'ai pas choisi moi-même cela dit."


hi "Oh ?"

show hanako basic_bashful_cas_close
with charachange


ha "C'est un cadeau, de Lilly."

show hanako emb_emb_cas_close
with charachange


ha "Je n'ai jamais vraiment eu besoin d'un téléphone, et je n'avais pas de quoi m'en acheter un. Elle m'en a offert un pour noël, disant qu'on pouvait l'utiliser pour rester en contact."


"Elles se voient tous les jours, dans et en dehors de l'école."


"Encore une fois, Lilly a son statut de déléguée et d'autres amis avec qui elle parle. Elle l'avait sans doute prévu pour les situations comme maintenant, où elle est partie pour un moment."


hi "Lilly est quelqu'un de spécial pour toi, hein ?"

show hanako emb_downsmile_cas_close
with charachange


ha "Oui. Je... l'aime... beaucoup."


"Hanako baisse les yeux et sourit alors qu'elle pense à elle. Aucune de mes amitiés n'a été aussi profonde que la leur, et je dois admettre que je suis quelque peu jaloux de leur relation."


"Nous échangeons nos adresses e-mail et j'ajoute le numéro de Hanako dans ma liste de contacts."

show hanako basic_smile_cas_close
with charachange


ha "...Voilà. Ça en fait trois maintenant."


hi "Trois ?"

show hanako basic_bashful_cas_close
with charachange


ha "Lilly, Akira et toi."


hi "Ah, Akira. Elle est intéressante, hein ?"

show hanako emb_smile_cas_close
with charachange


ha "Oui. Elle est très gentille, aussi. Son costume lui donne un... air cool."


hi "Je suis un peu surpris que vous vous connaissiez aussi bien, avec son travail qui lui prend autant de temps."

show hanako emb_downsmile_cas_close
with charachange


"Hanako baisse un peu la tête et prend une autre gorgée. Si je ne la regardais pas avec attention, je manquerais le petit sourire. J'imagine qu'elle connaît si peu de gens, que ceux qu'elle connaît doivent beaucoup compter pour elle."


ha "Tu... en as combien ?"


hi "Moi ? Sûrement neuf ou dix."


"J’hésite à les énumérer par peur d'évoquer le fait que Hanako n'a plus ses parents et apparemment pas de famille proche non plus. Il y a aussi Shizune et Misha, qui font partie d'une autre catégorie."


hi "Je suis sûr que Lilly en a plus que nous deux réunis."

show hanako basic_smile_cas_close
with charachange


"Hanako émet un petit rire et je souris. Je suis content qu'elle soit aussi à l'aise avec moi. Dans des moments comme ça, j'ai l'impression d’être plus proche d'elle."


hi "Je peux te poser une question ?"

show hanako basic_normal_cas_close
with charachange


"Hanako hoche la tête alors qu’elle finit sa tasse de thé."


hi "Tu ne sembles pas envieuse que Lilly ait autant d'amis. Tu n'as pas envie de te faire plus d'amis, ou de connaître certaines des amies de Lilly ?"

show hanako cover_worry_cas_close
with charachange


ha "Je ne suis pas envieuse. Je... n'aime pas beaucoup les gens, alors ça ne me gêne pas de ne pas avoir beaucoup d'amis."


"Ce... n'est pas vraiment la réponse que j'attendais. Elle ne semble pas gênée ou triste en disant ça, mais plutôt sérieuse."

show hanako cover_distant_cas_close
with charachange


ha "Je..."


"Hanako se frotte le bras, visiblement gênée et ayant pris mon silence comme une invitation à continuer. Je ne sais pas vraiment quoi dire, alors je finis par l'écouter en silence."


ha "Au collège, je me suis fait... beaucoup malmener. On m'insultait, j'étais exclue des groupes de travail et en sport. Il y avait... pire, aussi."


hi "Et c'est pour ça que tu n'aimes pas les gens ?"


"Elle secoue la tête."

show hanako emb_timid_cas_close
with charachange


ha "C'est à cause de... l'école primaire."


"Je me sens mal d'avoir abordé le sujet. Les adultes ont déjà suffisamment de mal à gérer les cicatrices de Hanako, les enfants doivent être encore pires."


"Je pensais qu'elle essayait de se faire toute petite en présence de gens pour qu'ils ne la regardent pas ou parce qu'elle était effrayée par eux, pas parce qu'elle ne voulait pas interagir avec eux."


"Je remarque que le smoothie que j'ai négligé a commencé à se liquéfier un peu, alors je me dépêche de le finir."

stop music fadeout 5.0

show hanako emb_downtimid_cas_close
with charachange


"Alors que je bois, Hanako joue avec son téléphone. On dirait qu'elle vient de se rappeler qu'il y a des gens autour et commence à se tendre un peu."


"Ce n'est pas un mauvais téléphone, j'ai économisé un bon moment pour m'offrir le mien. Si Lilly est allée dans une école privée, elle n'a probablement pas eu trop de problème pour lui en offrir un."


"La regarder jouer avec me donne une idée..."


hi "Hé Hanako, attends-moi, je reviens vite."

$ renpy.music.set_volume(0.4, 4.0, channel="ambient")


"Je pose le verre maintenant vide, glisse mon téléphone dans ma poche et me lève, faisant attention au sac que j'avais placé contre mon pied. Heureusement, être assis et discuter avec Hanako m'a aidé à récupérer mon souffle."

show hanako defarms_worry_cas_close
with charachange


ha "Hein, q-quoi ? O-où tu vas ?"


hi "Reste juste là, je reviens vite !"

$ renpy.music.set_volume(0.0, 1.0, channel="ambient")

show bg city_karaokeint
show hanako invis_close
with shorttimeskip

$ renpy.music.set_volume(0.2, 0.3, channel="ambient")

"J'aurais bien voulu trottiner pour revenir, mais je sais que je ne peux pas. Je finis par marcher jusqu'au café, un petit sac bleu dans ma main droite."

show hanako defarms_worry_cas_close
with charachange

play music music_another fadein 3.0


"Hanako me remarque vite, semblant aussi confuse que quand je suis parti. Je dépose le petit sac devant elle et me rassoit."

show hanako basic_worry_cas_close
with charachange


ha "C'est... ?"


hi "C'est pour toi. Tu peux l'ouvrir."

show hanako cover_worry_cas_close
with charachange


ha "M-mais..."


hi "Vas-y."


"Elle ne semble pas sûre, mais finit par ouvrir le sac et en sortir le contenu."

show phonestrap:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

$ renpy.music.set_volume(0.5, 1.0, channel="music")


"Un strap avec une chaîne argentée finissant par une délicate fleur est posée sur ses doigts. Ce n'est pas exactement un grand bijou, mais c'est tout ce que je peux me permettre."

show hanako cover_bashful_cas_close
with None


"Les yeux de Hanako s'illuminent quand elle le voit. C'est le genre de réaction que j'attendais."


"Le soleil d'été se reflète sur l'argent qui recouvre le bijou tandis qu'il remue un peu. Ce n'est pas trop prétentieux, mais c'est quand même charmant. Je trouve que ça lui va bien."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

show phonestrap:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide phonestrap
with None


"Hanako repose le strap sur la table et me regarde."

show hanako cover_worry_cas_close
with charachange


ha "Mais... ce n'est pas... Noël, ou mon anniversaire..."


hi "T’embête pas pour ça. Je me suis dit que ça serait bien de décorer ton téléphone avec quelque chose."

show hanako basic_worry_cas_close
with charachange


ha "J-je n'ai rien à te donner..."


hi "Je te l'ai dit, ne t’embête pas. Les amis peuvent s'offrir des choses de temps en temps, hein ?"

show hanako emb_downsmile_cas_close
with charachange


ha "Amis..."


"Hanako baisse tellement la tête que je ne peux pas voir son expression. Elle finit par hocher la tête avant de prendre son téléphone et d'y attacher le strap."

show hanako emb_smile_cas_close
with charachange

$ renpy.music.set_volume(0.5, 1.0, channel="music")

show hanaphonestrap:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)


"Elle me regarde et sourit en tenant son téléphone arborant maintenant une petite fleur."


ha "Merci... Hisao."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

show hanaphonestrap:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide hanaphonestrap
with None


"Son sourire s'avère contagieux."


"Du coin de l’œil, je remarque un couple se lever et partir. Ce qui me rappelle que le bus pour Yamaku passera bientôt."


hi "Il va falloir que j'y aille si je veux avoir le prochain bus. Tu viens aussi ?"

show hanako def_worry_cas_close
with charachange


ha "Ah, o-oui."

show hanako invis_close at center
with dissolvecharamove


"Elle hoche hâtivement la tête avant de remettre avec attention son téléphone dans sa poche et se lever de sa chaise. Je fais de même et ramasse le sac que j'avais posé en arrivant."

stop ambient fadeout 1.0
stop music fadeout 3.0

scene bg city_street2
show hanako emb_downsmile_cas_close at center
with locationskip

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_traffic fadein 1.0


"Nous marchons côte à côte jusqu’à l’arrêt de bus, ne disant rien jusque-là. Hanako regarde fixement devant elle, bien qu'elle semble être plutôt contente."


"Je ne sais pas ce que je pourrais lui dire, mais je ne suis pas sûr de devoir dire quelque chose non plus. Le fait que Hanako soit contente, en plus contente grâce à moi, c'est suffisant pour que le poids de mon sac se résume à une plume."

stop ambient fadeout 2.0

scene black
with dissolve




label fr_H29:

scene bg school_scienceroom

with locationchange

play music music_normal fadein 2.0


"J'arrive en classe après la marche habituelle depuis le dortoir. Mes yeux se dirigent immédiatement vers le troisième siège en partant de la gauche de la dernière rangée ; le siège de Hanako."


"Il est vide, et après avoir fait le tour de la classe du regard, il semblerait qu'elle ne soit pas encore là. Les deux filles du club journal qui sont assises à la gauche de Hanako sont déjà là, tout comme Shizune et Misha, mais c'est tout."


"Nous échangeons nos salutations matinales avant que je m'asseye. Je dois admettre que c'est un léger soulagement. Ça me donne au moins quelques minutes pour réfléchir."


"Non pas que je ne le faisais pas depuis un moment, mais depuis notre rencontre en ville, j'ai Hanako en tête."


"Je ne sais toujours pas quoi faire de ma relation avec Hanako. Je l'apprécie beaucoup, je peux le dire. Je veux la protéger de la douleur qu'elle ressent. Je ne crois pas que mes sentiments soient juste de l'amitié."


"Mais cela dit... J'ai l'impression de ne même pas la connaître."


"Si je tentais quelque chose, comment est-ce qu'elle le prendrait ? Est-elle dans un état émotionnel qui lui permet de prendre une décision raisonnable sur une relation ? Comment elle gérerait ce qui pourrait arriver après ?"

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_footsteps_hard fadein 4.0


"Il est aussi possible que je me trompe complètement sur Hanako ; ce qui n'est pas forcément inconcevable vu ses compétences sociales sous-développées."


"Le bruit de pas à la porte me sort de ma torpeur."

stop ambient fadeout 0.3

show miki invis:
    right
    xpos 1.1
with None

show miki whistle at right
with dissolvecharamove


"Ce n'est que Miki."

show miki smile
with charachange

show miki invis at Position (xpos=0.9)
with dissolvecharamove


"Elle se rend à peine compte que je suis là quand je croise son regard. Je suis sur le point de détourner le regard, mais quelqu'un arrive juste après que Miki se soit assise."

show hanako invis:
    right
    xpos 1.1
with None

show hanako emb_downtimid at right
with dissolvecharamove

stop music fadeout 2.0


"Je m'immobilise quand je vois Hanako entrer. Ce n'est pas une réaction rationnelle, mais je n'ai aucune idée de ce que je devrais faire ou dire."

show hanako emb_timid
with charachange


"Pendant un moment, nos regards se rencontrent."

show hanako emb_downtimid
with charachange

show hanako invis at Position (xpos=0.9)
with dissolvecharamove


"Et puis, tout aussi rapidement, elle détourne le regard et se dirige vers son siège sans dire un mot."

scene bg school_library_ss
with shorttimeskip

play music music_tranquil fadein 3.0


"Comme j'en ai maintenant pris l'habitude après les cours, je suis plongé dans un livre que je trouve complètement inintéressant."


"Étudier n'est pas quelque chose qui me vient naturellement. Je n'ai pas beaucoup étudié avant de venir à Yamaku et jusqu’à maintenant j'ai réussi à passer entre les mailles du filet avec juste du talent. Ça me frustre de ne plus pouvoir faire ça."


"À en juger par le visage des autres étudiants dans la bibliothèque, je ne crois pas être le seul à m'en plaindre. Le malheur aime la compagnie."


"J'ai décidé de passer le déjeuner avec Hanako, vu qu'on n'a pas mangé ensemble depuis un moment. J'aurais pu aussi bien passer mon temps à étudier cela dit, car mis à part quelques mots, nous avons passé le repas en silence."


"Pourquoi est-ce qu'elle continue de faire ça ? Je veux juste la protéger, être là pour elle, mais à chaque fois que j'ai l'impression qu'on se rapproche, elle recule."


ha "T-tu es occupé... ?"

$ renpy.music.set_volume(0.0, 0.3, channel="music")

show hanako defarms_shock_ss at center
with vpunch


hi "Hanako ?!"


"Je tourne la tête, surpris, ce qui la fait reculer d'un pas, effrayée."

show hanako emb_downsad_ss
with charachange


"C'était un mauvais timing. Si je n'avais pas pensé à elle à ce moment précis, je n'aurais probablement pas été aussi surpris."

$ renpy.music.set_volume(1.0, 5.0, channel="music")


hi "Désolé, tu m'as surpris."


"Je la fixe du regard plus longtemps qu'à la normale avant de retourner au livre devant moi. J'ai l'impression de plus regarder les mots que les lire."


"J'ai le sentiment que Hanako s'en rend compte aussi, alors je soupire et ferme le livre."


hi "Quoi de neuf ?"

show hanako emb_sad_ss
with charachange


ha "Je me... d-demandais juste ce que tu l-lisais..."


"Elle semble un peu déçue de ma réaction quand je l'ai vue. Abandonnant l'idée de continuer de travailler, je me lève et repose le livre à sa place sur l’étagère."


hi "Juste un manuel d'anglais."

show hanako basic_normal_ss
with charachange


ha "Ç-ça t'a aidé ?"


hi "Ça m'a aidé à réaliser que je n'aimais pas l'anglais, ouais."

show hanako basic_smile_ss
with charachange


"Hanako rit un peu. Je réfléchis au drôle de statut qu'a notre amitié, mais je sais que ses petites réactions font partie des choses que je ne verrais pas si je n'étais pas plus proche d'elle qu'au moment où nous nous sommes rencontrés."


"Je la regarde un moment, pensant à ce que je sais et ce que je ne sais pas d'elle. C'est un peu déprimant."

show hanako basic_worry_ss
with charachange


ha "Qu-quelque chose... ne va pas ?"

stop music fadeout 5.0


"Si je veux en savoir plus sur elle, peut-être que je devrais être plus direct."


"Parler avec Hanako normalement, plutôt que d'avoir constamment peur de la froisser, a marché, alors je pourrais tout aussi bien essayer d’être direct pour une fois."


hi "Dis Hanako, je peux te poser une question ?"

show hanako cover_worry_ss
with charachange


ha "D-d'accord."


hi "Je... veux savoir comment était ta vie. Ta vie avant d'arriver à Yamaku."

show hanako emb_blushing_ss
with charachange


"Elle hésite. J'envisage brièvement de changer de sujet, mais elle semble prendre la question très au sérieux."


"Je m'assois et la regarde prendre silencieusement son temps. Elle ne me regarde pas dans les yeux et on dirait presque qu'elle discute toute seule pour savoir si elle doit me répondre ou non."


"Sa réponse se manifeste avec un petit hochement de tête qui semblerait presque à contre-cœur. Elle a l'air beaucoup plus tendue que quand j'ai posé la question."

show hanako basic_worry_ss
with charachange


ha "D'accord. M-mais en en retour... tu dois me d-dire pour la tienne aussi..."


hide hanako
with charaexit


"Je hoche la tête et la suis alors qu'elle sort de la bibliothèque pour qu'on puisse parler."

scene bg school_hallway3
show hanako basic_normal at center
with locationchange

play music music_serene fadein 0.5


"La plupart des étudiants sont déjà partis, donc à part quelques personnes traînant près des locaux pour les clubs, les couloirs sont vides."


hi "J’imagine... qu'on va commencer avec ma venue à Yamaku."


hi "Voyons voir... J'étais à hôpital quand mes parents m'ont parlé pour la première fois de l’Académie Yamaku."


hi "Les docteurs m'ont dit que je ne devrais pas retourner dans mon ancienne école. Mes parents ont approuvé et m'ont persuadé de m'inscrire à Yamaku, même si ça signifiait vivre loin d'eux pour la première fois."

show hanako cover_worry
with charachange


ha "Ça a dû... être dur pour toi."


hi "Eh bien... ouais. Je dois admettre que oui. Mes parents travaillent beaucoup tous les deux, donc être plus ou moins indépendant, ce n'était pas nouveau pour moi. C'était le fait que j'allais devoir aller dans une école pour handicapés qui m'a le plus gêné."


hi "Et toi ?"

scene bg school_staircase2
show hanako emb_downtimid_close at right
with locationchange


"Un petit groupe de filles discutant passent à côté de nous, et Hanako se colle contre moi jusqu’à ce que nous soyons en bas des escaliers. Elle ne s'approche pas autant quand nous marchons juste dans l'école, donc ça me trouble un peu."

show hanako emb_downsad_close
with charachange


ha "Le personnel à l'o-orphelinat m'a proposé plusieurs possibilités sur ce que je pouvais faire. Le collège... ne s'est pas bien passé, donc j'ai pensé que Yamaku serait mieux."


ha "C'est isolé, et je me suis dit que ça serait plus facile si la plupart des autres étaient handicapés aussi."

scene bg school_lobby_ss
with locationchange


"Il est ironique que la raison qui a poussé Hanako à venir ici soit celle qui m'a le plus repoussé. Moi, j'avais l'impression d’être isolé quelque part loin de la société et de tous ceux que je connaissais. Pour Hanako, c'était certainement attrayant."


hi "Comment était la vie à l'orphelinat ?"

show hanako emb_timid_ss at center
with charaenter


ha "Ça... allait. Le personnel était gentil et ils prenaient soin de nous. Les enfants là-bas ne me parlaient pas beaucoup, mais je n'avais pas vraiment envie de leur parler non plus, donc ça ne me gênait pas."

show hanako emb_downsmile_ss
with charachange


ha "L'orphelinat avait une petite bibliothèque, donc j'ai commencé à lire pour passer le temps. Le personnel ne disait rien parce que, comme ça, j'étais plus facile à gérer que beaucoup d'autres enfants."


hi "Tu ne t'es pas fait d'amis là-bas ?"

show hanako basic_worry_ss
with charachange


ha "Non. Je crois... que ma vie était en pause... à cette époque. Je le savais, mais ça ne me gênait pas."


"Elle a eu sa vie en suspens pendant beaucoup de temps... Enfin, cela dépend quand l'incendie a eu lieu, mais ça a été une grande partie de sa vie. Pas de parents, pas d'amis, apparemment pas de famille..."

scene bg school_courtyard_ss
with locationchange


"Nous passons la porte et arrivons dans la cour. Je m'attendais à me faire agresser par la lumière du soleil, mais il est déjà tard."

show hanako emb_timid_ss at center
with charaenter


"Hanako me regarde par intermittence, donc je détourne un peu le regard."


ha "C'était comment pendant que tu étais à l’hôpital ?"


"Je réfléchis rapidement et essaye de remettre mes pensées en ordre."


"J'hésite un peu, mais je sais que je dois lui dire. Nous sommes assez proches pour qu'elle soit à l'aise au point de me raconter tout ça, alors il est de mise que je fasse de même."


hi "Ça allait à certains moments, mais à d'autres, c'était plutôt dur. Au début, tout le monde envoyait des cartes et venait me rendre visite. C'était un peu comme s’être cassé un bras ou un truc du genre."


hi "Voir tous mes amis faisait partie des bons moments. Iwanako venait souvent aussi. Plus souvent que n'importe qui."


hi "Mais il y a eu les mauvais moments, aussi. Quand mes amis ont arrêté de venir, j'ai réalisé à quel point ma situation était grave. Ça me rappelait que ce n'était pas juste un bras cassé, mais que j'étais devenu une personne différente."


hi "Même les moments où Iwanako venait me voir devenaient une torture. À la fin, ils se passaient en silence, alors qu'au début, elle parlait constamment."


"Mais Iwanako était comme ça. Elle était fragile, mais elle parlait constamment pour essayer de cacher ce fait. Pas d'un sujet précis, juste... elle parlait."


hi "Je crois que les trois pires moments ont été quand mes parents m'ont dit que je ne pourrais pas retourner dans mon ancienne école, quand j'ai passé mon anniversaire à l’hôpital, et... quand Iwanako est partie pour la dernière fois."

scene bg school_gardens_ss
with locationchange


"Nous laissons le bâtiment scolaire derrière nous et continuons notre chemin à travers les jardins. Il y a peut-être des gens errant dans l'école, mais à l'extérieur, nous sommes complètement seuls."

show hanako basic_worry_ss at center
with charaenter


ha "Comment était ton collège ?"


hi "C'était bien. J'ai grandi dans une grande ville et le collège était proche de chez moi, donc il y avait beaucoup de monde. Ça ne me gênait pas, sûrement parce que j’y étais habitué."


hi "J'avais des bonnes notes et je jouais au foot avec mes amis. J'ai passé beaucoup de temps à traîner avec eux après l'école aussi. Ils m’embêtaient un peu avec mes cheveux cela dit."

show hanako def_worry_ss
with charachange


ha "Tes cheveux ?"


"Je grimace un peu et mets une main sur mes cheveux pour les couvrir."


hi "Je n’arrête pas d'avoir des épis qui refusent de s’aplatir ou rester là où je veux qu'ils soient et ma mère refusait que je me fasse raser la tête. Ils avaient l'habitude de se rebeller, peu importe ce que je faisais pour les aplatir."

show hanako basic_smile_ss
with charachange


ha "Ça le fait toujours, un peu."


hi "J'avais peur que tu dises ça."

show hanako cover_worry_ss
with charachange


ha "D-désolée, je ne voulais pas... !"


"Je ris pour la rassurer."


hi "C'est bon, je sais que ça le fait toujours."


"Ça fait bizarre que quelqu'un soit aussi intéressé par mon passé. Si c'était n'importe qui d'autre, je penserais qu'elle est juste polie, mais ce n'est pas quelque chose que Hanako ferait. Ou si elle l'avait fait, ça se verrait."

scene bg school_dormhallground
show hanako emb_downtimid_close at right
with locationskip


"Il y a quelques filles dans la salle commune au rez-de-chaussée et Hanako se colle contre moi une fois de plus. Je m'attendais à ce qu'elle me lâche après, mais elle continue d’être contre moi alors que nous montons les escaliers."

stop music fadeout 5.0


"Quelque chose dans la manière dont elle me tient me semble... différent de la normale."

scene bg school_girlsdormhall
with locationchange


"Je réfléchis intensément pendant que nous arrivons en haut des escaliers. C'est seulement quand nous nous arrêtons que je relève les yeux et me rends compte que je l'ai suivie sans me poser de question."


hi "Pourquoi est-ce qu'on est venus à ta chambre ?"

show hanako basic_distant_close at center
with charaenter


"Elle regarde fixement la porte, ne me lance même pas un regard."


hi "Hanako ?"

show hanako basic_normal_close
with charachange


"Elle va pour répondre, mais s’arrête."

hide hanako
with charaexit

play sound sfx_dooropen


"Au lieu de ça, elle se décolle silencieusement de moi, ouvre la porte et la franchis."


"Je regarde des deux côtés du couloir, ne sachant par vraiment quoi faire. Haussant les épaules, je décide de la suivre, n'ayant aucune raison de faire autrement."

scene bg school_dormhanako_ss
show hanako basic_normal_ss at center
with locationchange


"Hanako se tient debout au milieu de sa chambre et me regarde directement. C'est troublant quand elle fait ça et tellement inhabituel pour elle. J'ouvre la bouche pour parler, mais elle me devance."


ha "Tu pourrais... fermer la porte à clé ?"


"Hanako lève une main jusqu’à sa poitrine et agrippe sa chemise à l'emplacement de son cœur."

hide hanako
with charaexit

play sound sfx_doorclose
with Pause (0.8)

play sound sfx_lock


"Je me tourne et ferme la porte, puis m'immobilise."


"L’atmosphère commence à être vraiment étrange. Ce sentiment se renforce quand j’entends les rideaux se fermer derrière moi."


"Il fera bientôt nuit. Je suis un garçon dans la chambre d'une fille. Elle ferme les rideaux et je verrouille la porte. Elle n'a.... elle n'a pas ça à l'esprit... hein ?"


"J'avale ma salive et me tourne très, très lentement. Hanako est au centre de la pièce, mais me tourne le dos."

show hanako emb_downtimid_ss at center
with charaenter


ha "Tu m'as parlé de ton passé, alors je dois te parler du mien."


"Elle respire à fond et s’arrête pendant quelques secondes. Ses mains se dirigent vers son col qu'elle commence à défaire."


hi "H-Hanako..."

show hanako emb_timid_ss
with charachange


ha "S-s'il te plaît... ne dis rien."


"Je reste silencieux tandis qu'elle retire son ruban et continue de déboutonner sa blouse, avant de s'occuper du clip de son soutien-gorge. Elle fait ça lentement. Peut-être que ça semble lent à cause de ce qu'elle fait. Je ne sais pas vraiment."


"Paralysé, je me contente de la regarder déboutonner sa jupe avec les mains qui tremblent et la laisser tomber sur le sol."

play music music_hanako fadein 1.0

scene ev hanako_scars:
with whiteout


"Finalement, elle retire sa chemise, son soutien-gorge tombant de ses épaules. Hanako se tient debout au centre de la pièce, ayant seulement ses collants et sa culotte pour vêtements."


ha "C'est moi. Tout... moi."

show ev hanako_scars_large:
    xalign 0.0 yalign 1.0 subpixel True
    acdc_warp 30.0 xalign 1.0 yalign 0.0
with locationchange


"Je regarde immédiatement la cicatrice dans son dos. Elle est similaire à celle de son visage, mais elle est aussi beaucoup plus grande. Sa cicatrice est bien pire sur son épaule, le bas de son dos et sa cuisse."


"Tout comme ma crise cardiaque a redéfini ma vie... c'est l’événement qui a redéfini celle de Hanako."


"Si j'avais vu ça la première fois que je l'ai rencontrée, j'aurais été choqué. Pas juste à la vue, mais aussi à l'idée qu'on puisse survivre à quelque chose comme ça."


"Mais après avoir eu le temps de m'habituer à l'idée, et après avoir vu la cicatrice sur son visage, sa main et son cou, ma réaction est moins virulente. Ma réaction actuelle n'est pas due à ses cicatrices, mais à son corps."


ha "L'incendie s'est produit quand j’avais huit ans. C'était la nuit, on dormait quand il a démarré."


"La voix de Hanako tremble et la blouse qui bouge dans sa main trahit le fait que ses mains font de même."


ha "Je... me suis mise en boule... quand le feu est passé sur moi. Ma mère... a essayé de me protéger. C-c'est la seule raison pour laquelle... j'ai survécu..."


"Les yeux de Hanako deviennent humides, sa voix tremble sous la pression combinée du fait de s'exposer comme ça face à moi et de revivre ces souvenirs douloureux."


"Je veux lui dire quelque chose, quoi que ce soit, pour qu'elle se sente mieux. Je ne peux pas. Je me sens complètement inutile. Elle se force à se rapprocher de moi et pourtant ce sont les moments où je la sens le plus loin."


ha "Je suis désolée... de te faire voir ça."


"Il n'y a aucune raison de nier l'évidence. Je crois que ce que je devrais dire et ce que Hanako veut que je dise, c'est la vérité. Ce que je pense, honnêtement."


hi "Ça importe peu. Tu es quelqu'un de fantastique, Hanako. Ton corps ne change pas ce fait."


"Elle me regarde longuement, sa respiration est irrégulière alors qu'elle essaye de contenir les émotions que nous ressentons tous les deux. On dirait qu'elle regarde plus à travers moi que moi directement."


"Je marche lentement vers elle et place doucement ma main sur son épaule tandis qu'elle lâche sa blouse. Elle sursaute légèrement ; pas de peur, mais de simple surprise."


"Être si proche d'elle me fait ressentir beaucoup de choses. La cicatrice de son épaule, visible, semble comme du cuir au toucher et fait un étrange contraste avec sa peau douce et ses cheveux sombres."


"Hanako est une fille, avec tout ce que ça implique. Elle est grande pour une femme, mais a toujours des formes. Le bas de sa nuque, légèrement visible grâce à ses cheveux passés par dessus son épaule, est très séduisant."


ha "Je sais... que je ne suis pas belle... comme Lilly. Je voulais... voulais juste... que tu me voies. La vraie moi."


hi "Je connais déjà la vraie toi. Tu n'as pas besoin de retirer tes vêtements pour ça."

scene bg school_dormhanako_ss
show hanagown stockworry_blush_close_ss at center
with locationchange


"Ses lèvres sont ouvertes, juste un peu. Elle est surprise quand, sans réfléchir, je me penche et presse mes lèvres contre les siennes."


"Le baiser ne dure qu'un instant avant que nous nous séparions, la respiration rapide. Le sentiment des lèvres de Hanako s'attarde sur les miennes et ses yeux restent toujours rivés aux miens."

show hanagown stockdistant_blush_ss at center
with charachange


"Tremblant un peu, je retire ma cravate et défais les boutons de ma chemise. Hanako reste immobile là où elle est, regardant le sol devant elle plutôt que moi en train de me déshabiller."


"D'un certain côté, je préfère ça. J'ai toujours été quelque peu gêné par mon corps, mais ma cicatrice a bien empiré les choses. D'un autre côté, l’atmosphère est vraiment étrange."

show hanagown stocknormal_blush_ss at center
with charachange


"Ma chemise tombe sur le sol, en boule comme celle de Hanako. Le corps entier de Hanako tremble alors qu'elle entend le bruit de ma braguette s'ouvrir et mon pantalon se retirer."


"Mon pantalon rejoint ma chemise sur le sol à côté du lit, tout comme mes chaussettes peu après. J'hésite à retirer mon boxer, mais je finis par le laisser."


"Il représente la dernière barrière que je ne pense pas pouvoir franchir pour l'instant. L'embarras m’arrête et je ne voudrais pas paniquer encore plus Hanako."

show hanagown stockdistant_blush_ss at center
with charachange


hi "Hanako..."

hide hanagown
with charaexit


"Elle hoche la tête sans même me regarder et va jusqu'au lit tout comme moi. Elle marche comme si ses jambes étaient des bâtons. Je trouverais ça amusant si je ne faisais pas exactement la même chose."


"Je prends l'initiative, me tournant et m’asseyant sur le bord du lit. Je la regarde dans les yeux pour l'inviter à s’asseoir à coté de moi ou devant moi, mais finis par détourner le regard pour m’empêcher de fixer son corps."

label fr_H29h:

scene evh hanako_bed_boobs_glance
with whiteout


"Néanmoins, elle comprend et s'assoit entre mes jambes. Alors qu'elle fait ça, une vague de sensations me parcourt."



"La sensation de son dos contre mon entrejambe est la plus évidente, mais son odeur est tout aussi forte. Elle a légèrement transpiré en ayant été aussi nerveuse, et l'odeur de ses cheveux contre mon visage est là aussi."


"J'essaye de sourire pour rendre la situation légèrement plus confortable pour elle, mais c'est quand même bizarre. Décidant de faire progresser les choses, je place une main sur sa poitrine et l'autre sur sa jambe."

show evh hanako_bed_boobs_blush
with charachange


"Ses lèvres se plissent tandis qu'elle essaye de réprimer un petit gémissement de surprise."


hi "Désolé, je ne voulais pas te surprendre."


"Hanako respire à fond et secoue la tête."


"J'avale difficilement ma salive et commence à bouger la main, sentant et caressant son sein et son téton. C'est vraiment agréable, tendre sous la main, mais suffisamment ferme."


"Pendant un moment je ne pense pas que ça l'aide à se mettre dans l'ambiance, mais elle abaisse lentement ses paupières. Sa respiration devient plus rythmée et son corps se relaxe un peu contre le mien."


"Ça me fait plaisir d’être capable de détendre Hanako. C'est définitivement plus agréable que la seule sensation de son corps. Je peux sentir une petite bosse entre mes doigts qui n'était pas là avant."


show evh hanako_bed_crotch_blush
with charachange


"Je descends lentement ma main, essayant de ne pas la surprendre. Elle ne proteste pas et mes doigts finissent par bouger de haut en bas sur la douce rainure entre ses jambes."


"Son corps est pressé contre le mien et il y a une lègère transpiration sur nos corps. Son corps est chaud et tout ceci ne fait que m'exciter encore plus, de même pour elle."


"Hanako pousse un léger gémissement, mes doigts pressant un peu plus et bougeant un peu plus vite presque instinctivement. La fille devant moi, la fille se pressant contre moi... je la veux. Toute entière."

show evh hanako_bed_crotch_glance
with charachange


"J’arrête de bouger les doigts et Hanako souffle de soulagement lors de cette pause face à tous les sentiments qui bouillent en elle. Elle me regarde légèrement, silencieuse mais dans l'attente."


"Je hoche la tête. Je ne sais pas lequel de nous deux est le plus inquiet à cet instant."

scene bg school_dormhanako_ss
with locationchange


"Je me recule sur le lit, me décollant de Hanako avec un certain regret. Quant à elle, elle se laisse tomber sur le côté et pose la tête sur son oreiller, respirant fortement durant tout ce temps."

scene evh hanako_missionary_underwear
with whiteout


"Hanako est allongée devant moi, sa culotte maintenant foncée, sa poitrine découverte, son visage rougi et ses yeux rivés aux miens... ses cicatrices lui donnent un air encore plus unique."


"Je reste pantois devant le fait qu'elle me laisse la voir comme ça."


"Je me rapproche d'elle, mettant mes mains sur ses hanches. J’attends son hochement de tête pour tirer délicatement sur ses collants, faisant bien attention."


"Je ne crois pas que j'arriverai à les retirer sans les déchirer, donc je finis par les laisser sur ses jambes et écarte sa culotte sur le côté."


"Hanako est allongée pratiquement nue sur le lit, ses parties intimes et ses cicatrices totalement visibles."


"Mettant mes doigts sur son entrejambe, je la touche encore un peu, la faisant respirer plus vite. Si elle est si excitée, ça devrait aller, donc j'ouvre mon boxer et me rapproche un peu plus."


"Le corps de Hanako se tend alors que je m'approche d'elle et ses yeux s'écarquillent. Elle a... peur ?"


"Je respire à fond, avant de réaliser quelque chose auquel j'aurais dû penser avant. Je ferme les yeux et me concentre."


"Mon cœur frappe fort alors que je me concentre sur son battement. Il est plus rapide qu'à la normale, bien sûr, mais le battement est régulier. Je... crois... que je peux y arriver, si j'y vais lentement."


ha "Ça... va... ?"


"J'ouvre les yeux et la regarde. J'imagine que je devais avoir une expression inquiète."


hi "Ça va. Je m'assurais juste que ça allait."


"Elle hésite un peu avant de hocher la tête. Elle semble un peu moins effrayée qu'avant, donc peut-être que lui montrer que j'étais inquiet aussi l'a rassurée."


"Je me penche et presse mes lèvres contre les siennes, nos langues se touchant timidement. Je peux sentir son corps se détendre sous le mien, ce qui nous remet tous les deux dans l'ambiance."


"Puis je me rappelle quelque chose et recule."


"Je me penche sur le côté du lit, là où se trouve mon pantalon et mets la main dans la poche arrière. Je cherche quelques secondes, jusqu’à ce qu'un petit carré à dents se fasse sentir sous mes doigts."


"Je le sors rapidement et me remets sur le lit, me reculant un peu de Hanako et me débattant avec l'emballage. Il faut un petit moment pour que je mette tout correctement, mais finalement le plastique recouvre parfaitement tout ce qu'il doit."


"La légère confusion alors que j’essayais de mettre un préservatif pour la première fois l'amuse un peu, et alors que je me positionne au-dessus d'elle, nous partageons un rire nerveux. Maintenant, j'ai besoin de me concentrer."



"Je baisse le regard et essaye de mettre mes genoux là où je pense être le bon emplacement, et je prends mon pénis dans ma main qui tremble légèrement. Hanako me regarde, puis ses yeux se détournent vers là où nos entrejambes se rencontrent."


"Après avoir respiré, je positionne le bout et me pousse à l'intérieur."

scene evh hanako_missionary_closed
with charachange


ha "Aahn... !"


"D'un seul coup, je suis complètement à l'intérieur d'elle. Une vague de sensations et d'émotions remplissent ma tête et Hanako gémit de douleur."


"Regarder son visage me met mal à l'aise. J'ai poussé trop fort et trop vite par erreur et lui ai causé plus de douleur que nécessaire. Aucun de nous ne sait vraiment ce qu'il fait et la dernière chose que je veux est lui faire mal."

scene evh hanako_missionary_open
with charachange


"Hanako rouvre les yeux et me regarde. Elle a dû voir à quel point j'étais troublé et elle fait de son mieux pour sourire. Ce n'est pas très convaincant."


"Je baisse le regard et commence lentement à bouger mes hanches après lui avoir donné un moment pour se remettre."


"Les mouvements ne me semblent vraiment pas naturels et je peux sentir mes muscles bouger d'une façon inconnue jusqu'à maintenant."


"Je sais que je stresse mon cœur plus que je ne le devrais, mais à chaque mouvement je fais attention aux battements."


"L’intérieur de Hanako est chaud et agréable et si le préservatif ne réduisait pas la sensation, je doute que je serais en mesure de durer longtemps. Ses légers gémissements et mouvements n'aident pas non plus."

scene evh hanako_missionary_clench
with charachange


"Pour Hanako, la douleur ne semble pas s’être autant dissipée que je l'aurais espéré. Ses cicatrices font qu'une partie de son corps bouge de manière légèrement différente de l'autre et quelques cheveux sont collés à son visage."


"Je passe mes bras autour de son corps et la soulève légèrement. Nous essayons de nous positionner un peu différemment pour minimiser sa douleur."


"Avec mes mains tenant ses jambes, nous bougeons maintenant avec de moins en moins de contenance dans nos mouvements. L'odeur de Hanako m’enivre et dans cette position, je n'éprouve pas trop mon corps."


"Ma notion du temps s'évanouit et je peux sentir que je respire trop vite. Je veux que Hanako apprécie aussi et je ne peux pas m’arrêter avant d'avoir atteint ce point."


"Une nouvelle vague de plaisir me frappe soudainement. La sensation commence à se concentrer et je ne crois pas que je vais réussir à me contrôler encore longtemps. J’accélère, me préoccupant de moins en moins du rythme."


"À chaque fois que j'ai l'impression de trouver un nouveau rythme, je le perds dans nos mouvements. D’après les sons qu’émet Hanako, je ne pense pas que cette position l'ait beaucoup aidée et je ne pense pas que je vais réussir à me retenir, non plus."


"Je la rallonge sur le lit, étant tous les deux au-delà du point où nous pouvons faire autre chose qu'atteindre la fin."


"Un mouvement après l'autre, je commence à sentir la fin venir, me tendant pour la repousser autant que je peux."


hi "Hanako... !"

scene evh hanako_missionary_closed
with charachange


"Hanako pousse un petit cri pendant que ma vision devient blanche. Mes reins se cognent contre elle avec beaucoup de force alors que j'atteins l'orgasme, et je peux me sentir jouir en elle."


"Son corps remue sous les mouvements du mien, ce qui ajoute encore plus à la sensation de plaisir."

window hide

label fr_H29x:

scene bg school_dormhanako_ni
show white
with Dissolve(3.0)

window show


"Et puis, après quelques secondes... c'est fini."


"Le son de la respiration de Hanako et de la mienne arrive à mes oreilles, presque trop bruyamment. Hanako a un bras devant son visage, la bouche ouverte."

stop music fadeout 10.0

show white:
    linear 10.0 alpha 0.0


"Alors que je me tiens au-dessus d'elle, mes bras perdent soudainement leur force et ma vision se trouble. Je me laisse tomber sur le lit à côté de Hanako, par peur de lui tomber dessus."


"Nous sommes tous deux étendus l'un à côté de l'autre, nus et collés pour tenir dans un lit une place. J'essaye de concentrer ma vision sur le plafond, sans grand succès. Je prends une couverture et la place sur nous pour nous couvrir du froid."


"Le seul bruit dans la chambre est celui de notre respiration. La transpiration qui s'est accumulée sur mon corps me met mal à l'aise. Nous sommes tous les deux physiquement et mentalement épuisés."

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.8)

window show


"Ma vision revient lentement à la normale alors que je continue de fixer le plafond, mais mes membres sont toujours faibles. J'essaye de me concentrer sur ma poitrine et trouve le battement irrégulier et légèrement douloureux."

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.8)

window show


"C'est un moment dangereux. Je dois réfléchir et ne pas paniquer, ne pas empirer la situation."

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.8)

window show


"Avec un grand effort, je reprends le contrôle de ma respiration, me forçant à faire de longues et profondes inspirations. J'en compte une demi-douzaine avant de me sentir physiquement calme et presse une main sur ma poitrine pour me rassurer."


"Mes battements sont revenus à la normale. Je vais bien."

scene ev hanako_after_worry
with locationchange

play music music_twinkle fadein 1.0


"Je me tourne vers Hanako, qui me regarde également. Elle a l'air plutôt hébétée, mais en dessous de ça, il y a de l’inquiétude. Elle a compris ce qui s'est passé."


hi "Je... vais bien. Tout est... revenu à la normale."


"Je me trouve à peine en état de sortir les mots entre deux respirations. Je ne pense pas que le sexe fatigue autant un corps normal, donc je n'ai aucun doute que ma condition soit fautive. Pourquoi est-ce que mon corps a dû me faire ça maintenant ?"

scene ev hanako_after_smile
with charachange


"Toutes les pensées sur mon cœur s'évaporent quand je vois le grand sourire qui se forme sur le visage de Hanako."


"Comme toujours, je lui retourne son sourire sans réfléchir. Le sourire de Hanako a toujours été contagieux dans sa tendresse presque enfantine, quelque chose qui lui est propre."


"À cet instant... nous n'avons pas besoin de parler. Nous n'en avons pas besoin pour communiquer."

stop music fadeout 2.0

scene black
with shuteye



label fr_H30:

scene black
with dissolve

hi "Mmh…"

play music music_pearly

scene bg school_dormhanako at left
with openeye


"Mes paupières sont lourdes alors que j'ouvre les yeux lentement, la lumière de l'extérieur m'aveugle un peu le temps qu'ils s'ajustent. Mon corps est mou et ma tête est lourde."


"Me réveiller avec un plafond que je ne connais pas est un sentiment désagréable. Ça me rappelle la première fois où je me suis réveillé avec le plafond blanc de l’hôpital."


"C'est après avoir passé quelques secondes à regarder le plafond que je réalise où je suis. C'est la chambre de Hanako."


"J'ai l'impression que mon cœur s'est arrêté encore une fois alors que les événements de la nuit dernière me passent en tête, le sang me monte aux joues et je referme les yeux une fois de plus."


"Il n'y a aucun intérêt à me prendre la tête si tôt, donc j'essaye de mettre ces pensées de côté pour l'instant."


"Je tourne la tête pour voir si Hanako est là où elle était quand je me suis endormi. Tout ce qu'il y a maintenant est un espace vide sur le lit, et pareil pour la chambre."


"Je m'assieds lentement et me frotte les yeux."

show bg school_dormhanako at right
with charamove_slow


"Je suis la seule personne ici. Je suis toujours nu et après un regard rapide sur le sol, je remarque que mes vêtements sont parfaitement pliés dans un coin de la pièce. J'ai beau essayer, je ne vois pas ceux de Hanako."


"Le paquet vide du préservatif a disparu aussi, probablement jeté."


"Avec un bâillement, je me lève et vais chercher mes sous-vêtements. Je grimace un peu à l'idée de remettre ceux de la veille, mais je n'ai pas tellement le choix."


"Prenant avantage du fait que j'ai un peu de temps seul, je m'habille pour la journée de cours à venir."


"Et puis... je suis seul."


"N'ayant plus rien à faire, mon esprit dérive sur le fait que je suis debout dans la chambre de quelqu'un avec qui j'ai passé la nuit, mais qu'elle n'est pas là."

play sound sfx_rumble


"Mon estomac se trouve être d'une meilleure aide que mon cerveau. Avec un grognement bruyant, il me rappelle que je pourrais tout aussi bien prendre un petit déjeuner."


"J'aimerais me réveiller à côté d'elle, mais... peut-être que c'est une bonne chose que j'aie un moment seul."


"La chambre de Hanako, comme toujours, est assez morne. Il y a quelques objets décoratifs, et presque aucun effet personnel qui ne soit pas caché dans des tiroirs ou ailleurs."


"Elle a vécu ici pendant trois ans, mais la chambre semble avoir été occupée à peine une journée."


"Je ne devrais pas réfléchir autant. Elle peut vivre très bien comme ça, certains le font. Savoir accorder aussi peu de valeur aux biens matériels a ses avantages, mais même, c'est un peu troublant étant donné son passé."


"Elle a dit qu'elle voyait sa vie comme en suspens quand elle était à l'orphelinat. Elle vit sûrement de la même façon, mais... après ce qui est arrivé la nuit dernière, c'est difficile d'imaginer qu'elle continue de penser ça."

play sound sfx_dooropen


"Le bruit de la poignée me sort de mes pensées et je me tourne."

show hanako basic_normal at center
with charaenter


"Hanako entre et ferme la porte derrière elle. Elle a ce qui semble être deux plats instantanés dans les mains, donc elle a un peu de mal."


hi "Bonjour, Hanako."

show hanako basic_bashful
with charachange


ha "B... bonjour."


"Elle se penche un peu pour me saluer avant d'aller jusqu'au bureau et d'y poser les deux plats. Je peux maintenant voir que c'est deux plats au satay, avec une fourchette plantée dans le riz de chacun."

show hanako basic_distant at Position(ypos=1.15)
with dissolvecharamove


"Je la remercie d'avoir amené le repas et nous en prenons chacun un. Elle s'assoit sur la chaise de son bureau tandis que je me mets sur le bord du lit."


"Je n'aime pas parler en mangeant, alors le silence qui règne n'est pas gênant. C'est le fait qu'il existe parce que nous ne savons pas quoi nous dire qui est gênant."

show hanako basic_normal
with charachange

show hanako basic_distant
with charachange


"Hanako me jette un regard de temps en temps pendant qu'elle mange. Je le remarque juste parce que je fais la même chose."


"Nous mangeons ensemble comme si nous étions un couple. On a même couché ensemble la nuit dernière. Une première pour nous deux. Quelque chose semble... malvenu, cela dit."


"Peut-être que c'est pour ça que nous ne disons pas un mot alors que nous finissons nos assiettes et les laissons dans l'évier."

scene bg school_girlsdormhall
with locationchange


"Peut-être que c'est pour ça que nous sortons de sa chambre sans nous tenir la main, ou discuter."


"Peut-être que c'est pour ça que j'ai l'impression qu'on est encore plus éloignés qu'avant."


scene bg school_scienceroom at left
with locationskip


"Nous entrons ensemble dans la classe, n'osant même pas regarder l'autre. Je me rends compte que c'était peut-être une erreur. Shizune lève un sourcil en nous voyant, suspicieuse."

show hanako cover_distant at center
with charaenter


"Nous arrivons au milieu de la classe et nous nous regardons l'un l'autre. Je ne suis pas sûr de ce que je devrais dire."


"Est-ce qu'elle veut que je m'adresse à elle comme à une petite amie ? Je ne croyais pas que notre relation était... Oh. C'est pour ça que tout semble si bizarre."


hi "À p-plus."

show hanako cover_bashful
with charachange


ha "D'accord."

hide hanako
with charaexit


"Je lève une main, gêné, tandis que nous nous séparons pour aller à nos sièges respectifs."


"Je ne peux même pas la regarder tellement je suis embarrassé. J'ai l'impression que le fossé entre Hanako et moi est de ma faute."

show shizu invis:
    center
    xpos -0.1
show muto invis:
    center
    xpos 0.75
with None

show shizu basic_normal:
    xpos 0.0
with dissolvecharamove

show muto normal:
    tworight
with dissolvecharamove


"Shizune commence à se diriger vers moi, mais Mutou entre dans la pièce."

show shizu invis at Position(xpos=-0.1)
with dissolvecharamove


"Je suis content qu'il arrive à ce moment-là, éloignant Shizune et ses questions, qui attendront une autre fois."


"Je n'aurais pas pu y répondre, de toute façon."


"J'aime Hanako, mais je ne lui ai jamais avoué mes sentiments. Hanako n'a jamais dit qu'elle voyait en moi plus qu'un ami, non plus. Et pourtant, nous avons couché ensemble."

stop music fadeout 2.0

scene bg school_scienceroom at left
with shorttimeskip

play sound sfx_normalbell


"La sonnerie annonce la pause déjeuner. Mutou est pris un peu par surprise, sa leçon de chimie interrompue au milieu d'une phrase."


"Pour la classe entière, sa leçon est passée dans une oreille et est ressortie par l'autre, tandis que moi je réfléchissais à Hanako. Je n'arrive pas à penser à autre chose, et jusqu’à maintenant j'ai surtout réussi à me prendre la tête."


"Je réalise qu'elle n'a jamais dit oui à ce que nous avons fait. Elle n'a pas dit non, non plus, mais... est-ce qu'elle en aurait été capable ?"


"Elle est extrêmement docile la plupart du temps, et il n'y a aucun doute qu'il lui a fallu un effort immense pour me montrer ses cicatrices."


"Je décide d'essayer au moins de discuter avec elle. Ça sera toujours mieux que la discussion monosyllabique que nous avons eue jusque-là."

show bg school_scienceroom at bgleft
with charamove_slow

show hanako emb_downtimid:
    center
    ypos 1.15
with charaenter


"Je vais jusqu’à son bureau pour discuter, mais elle rougit immédiatement et baisse la tête avant que je ne puisse arriver jusqu’à elle."

play music music_rain fadein 4.0


"Je prends une respiration, mais me retrouve sans savoir quoi dire. Qu'est-ce que je pourrais lui dire ?"


"Entendant des pas approcher, je me tourne et vois Shizune et Misha se dirigeant déjà vers nous, sans aucun doute dans l'intention de poser des questions gênantes."


"Quelques autres camarades de classe commèrent entre eux en nous regardant du coin de l’œil. Ils doivent avoir remarqué que Hanako et moi sommes arrivés ensemble."


"J'ouvre la bouche pour rassurer Hanako, mais elle me devance."

show hanako def_strain
with charachange


ha "Je... Je..."

show hanako defarms_strain:
    center
with Dissolvemove(0.3)


ha "Jedoisallerfairequelquechose!"

show hanako defarms_strain:
    easeout 0.5 alpha 0.0 xpos 0.0 xanchor 1.0
with Pause(0.5)

hide hanako
with None


"Elle se lève et se précipite vers la porte. Quelques livres et stylos qui étaient sur son bureau finissent sur le sol dans la précipitation."


"Peu de gens semblent se préoccuper de ce qui vient de se passer. Quelques personnes se tournent pour voir ce qu'il se passe, mais elles retournent vite à ce qu'elles faisaient."


"Je suis là, à regarder désespérément la porte par où Hanako a disparu. L'idée de lui courir après m'est passée par la tête, mais je suis presque sûr que Hanako peut courir plus vite que moi."


"Et en plus... qu'est-ce que je lui dirais une fois que je l'aurais rattrapée ?"


"Finalement, je m'accroupis et ramasse ce qu'elle a fait tomber de son bureau. Je me sens mal, réduit à ça alors que les étudiants passent à côté de moi pour sortir de la classe."

show shizu invis_close:
    tworight
    xpos 0.8
show misha invis_close:
    twoleft
    xpos 0.2
with None

show shizu behind_blank_close at tworight
show misha perky_smile_close at twoleft
with dissolvecharamove


"Je sens une tape sur mon épaule. Je tourne la tête pour voir Shizune et Misha en train de me regarder, de la curiosité écrite sur leurs visages et un peu gênées en pensant que ce qui est arrivé est partiellement de leur faute."

show shizu basic_normal2_close
with charachange

shi "…"

show misha sign_confused_close
with charachange


mi "Hicchan, si on peut aider..."


"Je secoue la tête. Elles ne peuvent pas m'aider sur ce coup-là, et d’après l'expression de Shizune et le ton de Misha, je crois qu'elles le savent aussi."

show shizu behind_blank_close
with charachange

with Pause(0.3)

hide misha
hide shizu
with charaexit


"Shizune hoche la tête, puis se penche comme pour s'excuser avant de sortir de la classe. Misha la suit peu après, tenant avec obéissance son rôle en tant qu'ombre de Shizune."


"Je me redresse, tenant ses livres et crayons, et les remets dans son bureau. Maintenant que la classe est vide, je me tiens contre son bureau à réfléchir en silence."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve


n "\n\nJ'ai l'impression que nous sommes déconnectés émotionnellement. Nous ne nous connaissons pas depuis si longtemps, et malgré mon envie de sortir avec elle, je ne sais pas vraiment comment Hanako voit les choses."


n "J'ai étudié autant que je le pouvais pour les examens, mais je n'ai toujours pas l'impression d'avoir fait mon choix pour la suite. J'ai essayé d’être un ami pour Hanako, même si je ne pouvais pas lui dire mes sentiments, et tout ce que ça a fait est nous éloigner."


n "\nJe n'ai même pas pu répondre à la seule fille qui m'a aimé, Iwanako."


n "\nQu'est-ce que je devrais faire... qu'est-ce que je peux faire... Je ne sais vraiment pas. Cependant, je sais que personne ne peut m'aider pour ça."


n "Juste retourner à la façon dont les choses étaient avant suffirait à me satisfaire, mais je sais que ce n'est pas possible. Quelque chose a changé entre nous depuis la nuit dernière. Peut-être que ça avait déjà changé avant et que cette nuit a confirmé la chose."

nvl clear


n "\n\nJe sais que pour Hanako, il y a un mur entre elle et moi. Je me suis retrouvé confronté à ce mur à chaque fois que j'ai essayé d'interagir avec elle."


n "Mais maintenant je commence à penser que j'ai mon propre mur entre nous, tout comme elle. Elle m'a quasiment extirpé mon passé, et le mien est pourtant moins traumatisant que le sien."


n "J'ai envie de dire que c'est parce que je n'ai pas eu beaucoup de temps pour m'ajuster depuis ma crise cardiaque, mais je sais que ça serait juste trouver une excuse."


n "La seule fois où je me rappelle qu'elle s'est ouverte à moi de sa propre initiative, c'était quand nous jouions au billard en ville, et j'ai été celui qui l'a empêchée de continuer."


n "\n\nJe veux connaître mieux Hanako. Je veux sauver notre relation, ou même juste notre amitié."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear
window show


"Mon esprit commence à dériver alors que je suis assis contre son bureau, à penser dans la classe vide là où nous avons passé tant de temps ensemble."

stop music fadeout 2.0


"Je veux parler à Hanako."



label fr_H31:

scene bg suburb_park
with shorttimeskip

play music music_moonlight fadein 0.5

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_parkambience fadein 2.0


"Je marche rapidement dans le parc, anxieux. De temps en temps je sors mon téléphone de ma poche, mais je finis par hésiter et le remettre."


"Si c'était une situation normale, je ne serais pas en train de louper les cours. Malheureusement elle ne l'est pas, et donc je me trouve dans la ville à côté de l'école à deux heures de l’après-midi."


"Depuis que j'ai rencontré Hanako, j'ai été celui qui a tout initié entre nous. Celui qui a commencé les conversations, est allé là où elle était, et a suggéré ce que nous pourrions faire. Aujourd'hui, cette fois, je ne veux pas être celui qui fait ça."


"Je mets ma main dans ma poche encore une fois. Cette fois je navigue rapidement jusqu'au menu des e-mails avant d'avoir une chance de changer d'avis."


"“Hanako, si tu veux parler, je serai au parc en ville pendant un moment.”"


"Combattant un dernier doute, je choisis Hanako dans la liste et appuie sur envoyer."


"Et maintenant, j’attends. J'ai fait ma part, ce qui arrivera sera la décision de Hanako. Ça ne servirait à rien que je la traîne ici. Elle a besoin de décider elle-même si elle veut me voir ou non."

stop ambient fadeout 4.0

with shorttimeskip


"Le jus de pomme du distributeur est horriblement amer. Ma prise sur la canette fait qu'un côté est légèrement gondolé."


"Je ne devrais pas être aussi tendu, mais j'imagine que c'est inévitable."


"Hanako est importante pour moi."


"Ce qui est arrivé ces derniers jours nous a causé à tous deux beaucoup de pression. L'idée de perdre tout le progrès qu'on a fait pour se rapprocher l'un de l'autre, et de perdre notre amitié en même temps, est effrayante."


"Mais même là... je ne sais pas vraiment à quel point nous sommes proches. On a peut-être couché ensemble, mais avant ça, nous étions juste des amis. Peut-être que nous étions plus que ça, mais même ça, je ne l'avais jamais réalisé."


"Peut-être que c'est pourquoi je me sens si mal à l'aise. Je ne comprends pas Hanako, malgré tout notre temps ensemble. Les minutes passent, et je ne sais toujours pas si elle va venir."


ha "H... Hisao... ?"


"Je m'immobilise un moment, ne croyant presque pas la voix que je viens d'entendre. Je pose la canette et me lève d'un coup."

show hanako basic_worry_cas at center
with charaenter


hi "Hanako..."

show hanako emb_downtimid_cas
with charachange


"Nous nous regardons pendant quelques secondes, avant que Hanako ne soit trop embarrassée pour maintenir un contact visuel et commence à jouer nerveusement avec la mèche de cheveux couvrant un côté de son visage."


"Quand j'ai été voir Hanako dans sa chambre après sa crise d'angoisse, je n'avais aucune idée de quoi dire. Ça allait, cela dit. Tout ce que l'on voulait était la présence de l'autre."


"Maintenant... J'ai l'impression d'avoir besoin de lui parler directement. Je veux casser ce mur entre nous, avant qu'il ne nous sépare pour de bon."

stop music fadeout 4.0


hi "Hanako... Je..."


hi "Ce que nous avons fait cette nuit... comment est-ce que je dois l’interpréter ?"

show hanako cover_worry_cas
with charachange


"Hanako arrête de jouer avec ses cheveux et me regarde, la tête légèrement baissée. Elle semble honteuse, ce qui est probablement une copie de ce quoi j'aurais l'air si je n'avais pas l'air si inquiet."

show hanako basic_worry_cas
with charachange

play music music_innocence fadein 4.0


ha "Je pensais... que tu pourrais finir par t'en aller si je n'étais que quelqu'un que tu avais besoin de protéger..."

show hanako emb_sad_cas
with charachange


ha "Je pensais que si je te laissais faire ça... je serais plus que ça pour toi."


"Ma première réaction est de l’incompréhension, mais... je lui ai fait ça, après tout. J'ai eu plein de fois l'opportunité d’arrêter les choses, faire marche arrière et remettre en question ce que nous faisions. En fin de compte... je ne l'ai pas fait."


"Un horrible sentiment me remonte dans tout le corps. Elle s'est offerte à moi à cause de ce qu'elle croyait que je voulais, et maintenant j'ai l'impression d'avoir profité d'elle. Elle était consentante, mais seulement à cause de fausses promesses."


"Je n'ai jamais été bon pour masquer mes émotions physiquement, et là ce n'est pas différent. Hanako baisse encore une fois la tête avec un étrange mélange de déprime, regret et mal-être inscrit sur son visage."


"Un lourd silence plane, mis à part le vent passant dans les arbres."

show hanako emb_downsad_cas
with charachange


ha "Je le savais... tu n'as pas pu me voir de cette façon..."


"Les mots de Hanako sont à peine plus forts qu'un chuchotement, semblant être destinés autant à elle qu'à moi."


hi "De quelle façon ? De quoi tu parles ?"


ha "Tout ce que j'étais pour toi c'était... une personne inutile. Juste quelqu'un... à protéger. Quelqu'un comme... un enfant."

show hanako cover_distant_cas
with charachange


ha "J-je voulais être plus que ça pour toi, mais après autant de temps... je... me suis habituée."


"C'est la première fois que j’entends sa voix comme ça. Elle semble dégoûtée. Pas de moi, mais d'elle-même."

show hanako cover_worry_cas
with charachange


ha "Après que je sois sortie de ma chambre... J'ai vu que tu avais commencé à t'éloigner."

show hanako basic_worry_cas
with charachange


ha "J'avais l'impression que j'allais te perdre, parce que... tu voulais quelqu'un avec qui tu pouvais avoir... ce genre de relation."

show hanako emb_downtimid_cas
with charachange


ha "Tu étais plus discret à l'école qu'avant et tu t'entendais si bien avec Yuuko... J'ai pensé... que je pourrais te perdre."


"Elle pensait que j'étais lassé d'elle, parce que je voulais une relation amoureuse ?"


hi "On... est amis, hein ? Je ne t'abandonnerais pas comme ça, même si ce que tu disais était vrai."

show hanako emb_timid_cas
with charachange


ha "L'amitié... est quelque chose que je pensais avoir abandonné. J'ai arrêté de croire les autres... après ce qui est arrivé suite à l'accident..."

show hanako emb_downsad_cas
with charachange



ha "Avant que l'accident arrive, je m'entendais bien avec les gens et les autres enfants. Je n'avais pas beaucoup d'amis... mais ça ne me gênait pas, parce que j'adorais ceux que j'avais."

show hanako emb_sad_cas
with charachange


ha "Cependant, après..."

show hanako emb_downsad_cas
with charachange


ha "Je me faisais insulter par les autres et beaucoup malmener. Ça fait mal... très profondément. Les professeurs ont essayé de m'aider, mais ils ne pouvaient pas faire grand-chose, et même beaucoup détournaient le regard juste en me voyant."


ha "Parmi ceux qui m'insultaient et m’embêtaient... il y avait ceux que je pensais être mes amis les plus proches."

show hanako cover_worry_cas
with charachange


ha "À partir de là, j'ai pensé que ça importait peu si les gens ne faisaient pas attention à moi. Mon existence est une gêne pour les autres, après tout. C’était plus... facile... si je n'existais plus."

show hanako cover_bashful_cas
with charachange


ha "Mais après avoir rencontré Lilly et puis toi..."

show hanako basic_normal_cas
with charachange


ha "J'ai essayé, mais je... ne pouvais pas me résoudre à repenser comme ça."


"Tout ce temps... elle ne m'a pas fait confiance. Elle pensait qu'elle ne valait rien. Quelqu'un qu'on jette une fois qu'on en a marre."


"Ça fait mal. C'est le genre de personne que je ne voulais jamais, jamais être, parce que je sais mieux que d'autres à quel point c'est horrible d’être jeté par les gens pour qui on croyait compter."


"Elle craque en se remémorant son passé. Je me sens inutile, complètement incapable de la consoler. D'une étrange façon cela dit, je suis presque content qu'elle veuille bien que je sache tout ça."


"Le mur entre nous s'effondre, même si ça fait mal de le casser."


hi "Hanako, si tu me l'avais dit..."

show hanako cover_worry_cas
with charachange


ha "J'avais... tort ?"


hi "Bien sûr tu..."


"Elle n'avait pas tort. C'est difficile de l'avouer, mais ça ne sert à rien de le nier. Pour Lilly et pour moi, elle était quelqu'un que nous essayions de protéger."


"Elle était devenue pour moi ce que j'étais devenu pour mes amis après ma crise cardiaque - quelqu'un de cassé. Je l'appréciais beaucoup, peut-être même que je l'aimais, mais je n'ai jamais agi parce que je croyais qu'elle était trop fragile."


hi "Je veux dire... je ne te regarde pas comme ça maintenant."


hi "J'étais inquiet après ce qui est arrivé en classe et je pensais que je devais essayer de te protéger."


hi "Quand tu t'es enfermée dans ta chambre, j'ai eu peur. Je pensais que tu me rejetais et ça m'a forcé à beaucoup penser à... différentes choses."

show hanako defarms_strain_cas
with charachange


ha "Je ne te rejetais pas !"


"Elle sort ça avec presque de la peur dans sa voix, me surprenant. Elle devient rapidement embarrassée par son cri, avant de fermer les poings et réfléchir pour dire ce qu'elle a en tête."

show hanako emb_timid_cas
with charachange


ha "Je ne t'aurais jamais fait ça. Pas à toi."

show hanako emb_downtimid_cas
with charachange


ha "Même si j'avais peur... même si j'ai essayé de te repousser... tu essayais toujours de te rapprocher de moi."


ha "Je me suis enfermée parce que... j'étais juste un poids pour toi. Pour Lilly. Pour tout le monde."

show hanako emb_sad_cas
with charachange


ha "Ch-chaque anniversaire était le même. Tout le monde faisait de son mieux pour prétendre que je comptais. Tout le monde prétendait que tout allait bien... pour cet unique jour de l'année."

show hanako emb_downsad_cas
with charachange


ha "Je ne voulais pas exister, mais ils ne m'ont pas laissée. Même après avoir rencontré Lilly... tout était pareil. J'étais aussi inutile que je l'avais toujours été, incapable de faire quoi que ce soit pour elle, ou pour moi."


ha "Je ne voulais pas que ce soit pareil... avec toi."


"Lilly et moi avions complètement tort. D’après ce qu'elle dit, tout ce qu'on a fait pour elle... l'aurait uniquement fait se sentir encore plus mal. Même ce que je croyais être sûr à son sujet était faux."


hi "Après que tu te sois enfermée dans ta chambre, j'ai décidé de travailler sur mon passé aussi, et de faire le tri pour mon futur. Je ne savais pas comment faire pour gérer les pertes que j'avais subies en venant à Yamaku, j'ai essayé de m'en sortir seul."


hi "J'ai pensé... que ça nous aiderait à devenir de meilleurs amis... si je faisais ça."

hide hanako
with charaexit


"Un silence encore. J'essaye de continuer de la regarder, mais je ne peux pas. Je me sens vraiment mal et même si je tiens à m'excuser... je ne sais pas comment je vais pouvoir."


"Je l'entends respirer profondément et la regarde seulement après l'avoir entendue s'effondrer au sol."

scene ev hanako_park_alone
with whiteout


"L'entendre pleurer me fend le cœur. Je sais que je suis responsable, et je sais que je ne peux rien faire pour l'aider. Si Hanako se sent honteuse, alors je me sens d'autant plus honteux."

show ev hanako_park_away
with charachange


"Je me précipite vers elle alors que ses larmes continuent de couler sur ses joues. Je me fous de si je dois regarder ou non. Je veux juste être proche d'elle à cet instant."


ha "Je suis désolée, Hisao... J-j'ai tout gâché..."


hi "Ça va. Tout va bien. Je suis celui qui devrait être désolé. Je complotais dans ton dos et je ne t’ai jamais rien dit."


"Je peux sentir ma prise sur Hanako se resserrer alors que ma vision se brouille. Je ne veux pas essayer de me retenir. Je dois continuer de parler alors qu'une boule se forme dans ma gorge."


hi "Pour te dire la vérité, Hanako... j'avais peur. Pour la première fois depuis ma crise cardiaque, j'avais vraiment peur."

show ev hanako_park_look
with charachange


ha "Hisao... ?"


hi "J'ai tant perdu en venant à Yamaku. Je... dépendais de toi, plus que je ne le pensais."


hi "Même maintenant, j'ai toujours ce vide en moi. Après avoir perdu ma vie entière et tout ce que je connaissais, la pensée de te perdre toi aussi..."

show ev hanako_park_away
with charachange


ha "Mais je suis juste une personne inuti—"


hi "Tu es mon amie, Hanako ! Tu es..."


hi "Non, tu es plus que ça. Je t'aime, Hanako. Je t'aime tant, que la pensée de te perdre m'effraye énormément..."


"Ah, c'est pas bon... Je laisse vraiment tout sortir. Je n'arrive pas à me résigner à la regarder dans les yeux."

show ev hanako_park_look
with charachange


ha "Je suis désolée, Hisao..."


ha "Je ne peux pas m’empêcher... de me sentir un peu heureuse. Pendant si longtemps... c'est tout ce que je voulais... entendre..."

show ev hanako_park_closed
with charachange


"Le dernier barrage craque et le bruit de ses pleurs se fait entendre tandis que son corps se colle contre le mien. Nous nous étreignons, encore plus connectés par notre chagrin et notre bonheur partagés."


"Je ne sais pas comment seront les choses, après ça. Maintenant, cela dit... je m'en moque. Il n'y a personne d'autre dans le monde avec qui nous pourrions partager ces souvenirs et ces émotions. Personne."

stop music fadeout 2.0

scene bg suburb_park
with shorttimeskipsilent

play ambient sfx_parkambience fadein 2.0
play sound sfx_can_clatter


"Après avoir mis la canette dans une poubelle à côté du banc, je m'assieds près de Hanako. Elle me rend le mouchoir en tissu que je lui avais donné pour qu'elle puisse s'essuyer le visage, ce qui n'a pas beaucoup aidé."


"Encore une fois, je doute être beaucoup plus présentable. Je me sens vide et un peu embarrassé d'avoir laissé sortir ces émotions en public comme ça. Ce n'est pas une mauvaise sensation, cela dit. Je crois que Hanako ressent la même chose."


hi "Ça va un peu mieux ?"

play music music_comfort fadein 4.0

show hanako cover_bashful_cas_close:
    tworight
    ypos 1.1
with charaenter


ha "O-oui. merci."


"Pendant un moment, nous restons assis et prenons notre temps avant de reparler. Nous avons tous les deux besoin d'un peu de temps pour nous en remettre."

show hanako basic_smile_cas_close
with charachange


ha "Le temps est agréable à cette période de l'année."


hi "Oui, c'est vrai."

show black
with shuteye


"Je ferme les yeux un moment, appréciant la chaleur du soleil et la brise fraîche sur mon visage. Il fait vraiment bon aujourd'hui. Vraiment, vraiment bon."


hi "Tu sais... je n'ai pas vraiment envie de retourner en cours là, et toi ?"

hide black
show hanako basic_bashful_cas_close
with openeye



"Elle secoue la tête en finissant de s’essuyer les yeux avec sa manche. Le petit sourire qu'elle m'adresse est agréable, il me rappelle à quel point son sourire est honnête."


"Sourire pour quelqu'un d'autre est peut-être normal, une chose de tous les jours. Mais pour Hanako... elle sourit si rarement et si sincèrement, qu'à chaque fois qu'elle le fait, je me sens soulagé et heureux."

show hanako cover_worry_cas_close
with charachange


ha "Je suis désolée. Pour... tout."


hi "C'est pas grave. Je crois qu'on a tous les deux de quoi être désolés."

show hanako emb_timid_cas_close
with charachange


ha "Je sais que... je suis trop timide. Je sais que tu ne veux pas que je le sois, je ne crois pas que je puisse..."


hi "Tu peux changer, Hanako. Je le sais parce que depuis que je te connais, tu as déjà changé. Pour être honnête, je peux être assis avec toi et te parler seulement parce que tu as beaucoup changé depuis qu'on s'est rencontrés."

show hanako emb_downtimid_cas_close
with charachange


ha "Mais... je ne peux pas être comme ça avec... quelqu'un d'autre. Je n'ai rien de prévu après la fin de l'année, non plus..."


"La confiance de Hanako commence à s’évanouir encore, mais je crois que maintenant je peux enfin lui parler librement. Je peux le faire parce que je sais qu'on se ressemble sur beaucoup de points."


hi "Laisse-toi un peu de temps, et je crois que tu seras capable d'aller de l'avant. Non, je suis sûr que tu en seras capable. Je peux voir que tu as essayé, et j'ai confiance en toi."


ha "Et tu peux compter sur moi si tu as l’impression d'avoir besoin de l'aide de quelqu'un, tu sais."

show hanako defarms_strain_cas_close
with charachange


ha "M-mais je ne peux pas te demander de..."


hi "Tu peux, parce que c'est exactement ce que je te demande. Je vis la même chose, tu sais."


hi "Ça s'appelle l'amour."

show hanako basic_bashful_cas_close at tworight
with dissolvecharamove


"Hanako sourit, puis je me lève du banc. Elle fait de même."


hi "J'ai un peu faim. Tu veux qu'on aille prendre un truc ?"


"Elle hoche vigoureusement la tête. La façon dont elle sourit, la façon dont elle agit, même juste comment elle est... J'ai l'impression que c'est la première fois que je la vois vraiment heureuse."

$ renpy.music.set_volume(0.6, 1.0, channel="ambient")

scene bg suburb_roadcenter
with locationchange


"Nous parcourons tous les deux la rue, marchant côte à côte."

show hanako emb_emb_cas_close at center
with charaenter


ha "Hisao ?"


hi "Ouais ?"

show hanako emb_downtimid_cas_close
with charachange


ha "Je... Je crois... que je ne te comprends pas vraiment."


hi "Je ne crois pas te comprendre non plus. Mais c'est pas grave."


"Il n'y a pas de désespoir dans nos voix. Ne pas comprendre l'autre est normal, les murs que nous avons établis entre nous ne peuvent pas tomber en une seule journée."


"Mais ce n'est pas grave. Tant que nous vivons ça au jour le jour, et essayons de comprendre l'autre... je crois que tout ira bien."

show hanako emb_timid_cas_close
with charachange

show hanako emb_downtimid_cas_close
with charachange


"Alors que nous marchons dans la rue, le regard de Hanako jongle entre mon visage et la rue."


hi "Tu penses à quelque chose ? Tu sembles agitée."

show hanako basic_normal_cas_close
with charachange


"Elle ralentit avant de complètement s’arrêter. Quand je me tourne pour la voir, elle prend une grande respiration et me regarde. Cette expression... je l'ai vue une fois auparavant. Juste une fois, quand je l'ai accidentellement vue dans sa chambre."


ha "Je... je crois... je crois que j'ai quelque chose... que je dois te donner."


hi "Qu'est-ce que c'est ? Tu n'as pas à être aussi secrète à ce sujet."

show hanako cover_distant_cas_close
with charachange


ha "Je voulais te le donner depuis très, très longtemps, mais... maintenant que je dois... c'est trop embarrassant..."


hi "Ne t’inquiète pas. Je l'accepterai, quoi que ce soit."

show hanako basic_bashful_cas_close
with charachange


"Elle affiche un grand sourire, puis pose une main sur mon épaule."


ha "Alors, accepte mon premier cadeau pour toi, Hisao."


hi "Hanako... ?"

stop ambient fadeout 1.0

window hide
scene unlock_ev hanako_goodend_close
show unlock_ev hanako_goodend_muffin
show unlock_ev hanako_goodend

show ev hanako_goodend_close:
    xalign 0.0 yalign 0.0
    zoom 1.0 subpixel True
    linear 6.5 zoom 0.8
with whiteout

$ renpy.pause(4.0, hard=True)

play sound sfx_whiteout

scene ev hanako_goodend:
    xalign 0.0 yalign 0.0
    zoom 1.0 subpixel True
    parallel:
        easein 12.0 zoom 0.8
    parallel:
        6.0
        "ev hanako_goodend_muffin" with Dissolve(2.0)
with locationchange

$ renpy.pause(12.0, hard=True)

$ renpy.music.set_volume(1.0, 2.0, channel="ambient")
stop music fadeout 4.0

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
