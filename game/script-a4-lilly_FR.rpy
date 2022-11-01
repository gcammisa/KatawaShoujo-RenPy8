label fr_L21:

window hide None

scene bg school_scienceroom
with locationchange

nvl clear
nvl show dissolve

$ renpy.music.set_volume(0.5, 1.0, channel="music")
play music music_normal fadein 1.0


n "\n\n\nAprès l'émotion de notre voyage à Hokkaido, cela fait bizarre de retourner à la vie normale si brusquement. Un jour normal, le même qu'un autre."


n "\nEnfin, c'est ce que j'aimerais croire, du moins."


n "\nPour dire la vérité, l'atmosphère de la classe, non, de l'école entière a changé."


n "Bien que l'école ait déjà connu quelque chose comme ça, maintenant que les examens approchent, tout le monde s'active pour les révisions, d'une façon rarement vue."


n "Un jour avant le début des examens. Et ce qui est horrible, c'est qu'au lieu de réviser, nous qui étions des étudiants modèles, nous avons gaspillé notre temps dans le nord."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

show misha invis_close:
    xanchor 0.5 xpos -0.1
with None

show misha perky_confused_close:
    xpos 0.1
show bg school_scienceroom at bgright
with dissolvecharamove

window show


"Jetant un coup d'œil dans la classe, même Misha, qui est normalement super énergique, semble abattue. Elle est assise, mâchouillant nerveusement un crayon pendant que Mutou lit son cours."


"Attends... en y regardant de plus près, je crois qu'elle le mange."

show misha invis_close:
    xpos -0.1
show bg school_scienceroom at center
with dissolvecharamove

hide misha
with None


"Détournant les yeux de cet horrible spectacle, je concentre mon attention sur quelqu'un d'autre."

show hanako invis:
    xanchor 0.5 xpos 1.1
with None

show hanako defarms_strain:
    xpos 0.94
show bg school_scienceroom at bgleft
with dissolvecharamove


"Hanako écrit frénétiquement sur son cahier, le visage très proche du papier, semblant recopier chaque mot sortant de la bouche de Mutou."

show shizu invis:
    xanchor 0.5 xpos 0.0
show misha invis_close:
    xanchor 0.5 xpos -0.1
with None

show shizu basic_normal:
    xanchor 0.5 xpos 0.3
show misha perky_confused_close:
    xpos 0.1
show hanako invis:
    xpos 1.1
show bg school_scienceroom at bgright
with dissolvecharamove

hide hanako
with None


"Shizune est, ben... Shizune. Très calme, elle prend assidument des notes sur ce qui se passe."


"Pour dire vrai, c'est ce que je devrais faire aussi, si je ne maîtrisais déjà pas majoritairement le sujet abordé."


"Je me demande comment s'en sort Lilly. Même si elle est sérieuse, elle a beaucoup à faire, contrairement à moi. Ses responsabilités de déléguée, Hanako, ses autres amis, ses études avancées d'anglais... elle gère vraiment beaucoup de choses."

scene bg school_scienceroom
with shorttimeskip

play sound sfx_normalbell


"La sonnerie de midi est un soulagement pour tout le monde, même Mutou. Je pense qu'il préfère largement une classe normale qu'une classe nerveuse à cause de la préparation des examens."

mi "Hicchan~…"

show misha invis_close:
    xanchor 0.5 xpos 0.1
with None

show misha perky_sad_close at twoleft
show bg school_scienceroom at bgright
with dissolvecharamove


mi "Aide-moi~..."


"Je ferme à moitié les yeux, montrant clairement que je ne suis pas intéressé."


mi "Aide-moi, aide-moi, aide-moi~..."


hi "Ça ne va pas ?"

show misha perky_confused_close
with charachange


mi "Shicchan s'en sortira, mais je crois que je vais en mourir. Je vais mourir, Hicchan ? Tu me laisseras mourir de tout ce travail ?"


"Vraiment théâtral. Étant donné qu'elle n'est ni la plus brillante élève de la classe, ni la plus sérieuse, ce n'est pas une grande surprise qu'elle semble avoir du mal avec tout ce travail."


hi "Désolé Misha, mais j'ai mon propre travail. Je croyais que Shizune et toi aviez étudié ensemble durant le week-end ?"

show misha sign_sad_close
with charachange


mi "C'est du gâchis d'étudier pendant les vacances, Hicchan ! Faire du shopping était plus fun, hein, Shicchan ?"

show shizu behind_blank at tworight behind misha
with charaenter


"C'est seulement maintenant que je remarque que Shizune nous regardait depuis tout ce temps et que les bras de Misha lui traduisaient tout en temps réel. Je dois vraiment être à l'ouest pour ne pas l'avoir remarqué."


hi "Pourquoi les filles aiment tant faire du shopping, d'ailleurs ? Même Lilly et Hanako m'ont obligé à y aller quelquefois."

show misha hips_grin_close
with charachange


mi "Mais tu y as été quand même, non ? C'est si rare de voir un gars qui aime faire du shopping~..."


hi "Bah, mon rôle était plutôt de porter les sacs. Je ne peux pas dire que ça m'ait particulièrement plu."


hi "Pour en revenir aux examens, vous avez étudié après être revenues de vacances, hein, Shizune ?"

show shizu basic_normal2
with charachange

shi "…"

show misha sign_smile_close
with charachange


mi "Bien sûr, Hicchan. Il est crucial de réviser les jours précédents..."

show misha perky_sad_close
with charachange

mi "U~rgh."


"Misha fait un bruit ressemblant à une vache agonisante quand elle réalise qu'elle vient d'être trahie par sa meilleure amie."

show shizu basic_angry
with charachange


"À en juger par le regard de Shizune envers Misha, elle lui a probablement dit qu'elle aurait dû étudier comme elle l'a fait."


hi "Ne t'inquiète pas, tu pourras t'en sortir si tu étudies beaucoup à partir de maintenant."


hi "Peut-être."


"Misha ne semble pas vraiment amusée. On dirait que le petit ballon de bonne humeur infinie vient d'éclater."

show shizu behind_blank
with charachange

shi "…"

show shizu behind_blank_close
with characlose

with Pause(0.3)

show shizu adjust_frown_close
show misha perky_confused_close
with vpunch


"Les signes de Shizune restent sans interprétation, ce qui vaut à Misha de se prendre un petit coup sur l'épaule. Il ne lui faut pas longtemps pour qu'elle se remette à la tâche."

show misha hips_smile_close
with charachange


mi "Oh, ah, donc qu'est-ce que tu as fait ce week-end, Hicchan ?"


hi "On a été en voyage dans le nord avec Lilly et Hanako. C'était bien."

show misha perky_smile_close
show shizu behind_blank_close
with charachange


"Je vois deux paires d'yeux se tourner vers moi, pensant sûrement de travers. Le fait que leur suspicion soit fondée rend la situation encore plus gênante."


hi "On s'est juste baladés dans la région et on a étudié, rien de plus."

show misha cross_smile_close
with charachange

mi "Hmm~…"


"Après un mensonge aussi flagrant, je réalise que je n'aurais peut-être pas dû, vu les connexions de Shizune et son manque total de limites quand il s'agit d'interroger quelqu'un qu'elle suspecte de cacher quelque chose."


"Je n'ai vraiment aucune idée de comment elle va le prendre, mais elle finira par le savoir un jour ou l'autre. Et ce ne sont pas ses affaires, avec qui je sors, de toute façon."


hi "Ah, et Lilly et moi sortons ensemble maintenant."

show misha hips_grin_close
show shizu basic_normal2_close
with charachange


"Alors que Misha accueille la nouvelle avec un grand sourire, Shizune semble quelque peu surprise, même si elle parvient à le masquer par son attitude calme."

show shizu behind_blank_close
with charachange

shi "…"

show misha sign_smile_close
with charachange


mi "Avec qui tu sors, ça ne regarde que toi. J'espère que vous serez bien ensemble."


"Misha m'informe avec un regard que c'est le mieux que j'aurai de la part de Shizune. Je n'en demande pas plus."

show shizu basic_normal2_close
with charachange


"Après cela, Shizune commence à dire quelque chose d'autre, puis s'interrompt et secoue la tête pour informer Misha de ne pas traduire."

hide shizu
with charaexit

hide misha
with charaexit


"À la base je trouverais ça bizarre, mais le petit signe de la main que me fait Shizune avant de partir avec Misha, amplifie ma confusion. Shizune n'est pas le genre de personnes à ne pas dire ce qu'elle pense."


"Je hausse les épaules à leur comportement étrange et regarde en direction du bureau de Hanako, mais vois que la chaise est vide. Elle était là juste avant, donc elle n'a sûrement pas eu envie de m'attendre."


"Je vais m'acheter à manger seul, alors."

stop music fadeout 2.0

scene bg school_hallway2
with shorttimeskip


"Parcourant le couloir en direction de la pièce inutilisée qui est devenue comme une deuxième maison pour nous trois, je regarde sans envie le sachet plastique dans ma main qui contient des roulés à la salade et une brique de jus de fruit."


"La nourriture de la cafétéria n'est vraiment pas appétisante. Peut-être que c'est ma punition pour mes récents agissements."


"Ouvrant la porte, je vois une personne de moins que ce que j'attendais."

scene ev lilly_tearoom
with whiteout

play music music_lilly fadein 3.0



"Ça fait bizarre, malgré le fait que je connaisse Lilly depuis des mois, je n'arrive pas à m'empêcher de penser à la première fois où je l'ai vue, assise silencieusement dans la lumière du jour."

show ev lilly_tearoom_open
with charachange


"Comme la première fois, elle ouvre lentement les yeux, les gardant fixes et s'adresse calmement à moi."


li "Bonjour, Hisao."



hi "Salut Lilly."


hi "Hanako est dans le coin ? Elle est partie de la classe sans que je le remarque."

scene bg school_miyagi
show lilly basic_listen_close:
    center
    ypos 1.1
with locationchange


"Lilly fronce les sourcils alors que je prends une chaise et pose mon sac contre un des pieds de la table, sortant mon piètre repas."

show lilly basic_reminisce_close
with charachange


li "Elle est venue... brièvement. Elle a dit qu'elle devait étudier pour ses examens et est partie à la bibliothèque."


"Ni Lilly ni moi ne sommes certains de la véracité de sa déclaration."


hi "Eh bien, au moins elle a de bonnes intentions."

show lilly basic_concerned_close
with charachange


li "C'est gentil, mais elle n'a pas besoin d'en faire autant pour nous laisser de l'espace. Je lui en parlerai sûrement."


hi "Ça serait bien, oui."

show lilly basic_weaksmile_close
with charachange


"Pendant un moment nous déjeunons sans un bruit, Lilly mangeant son sandwich avec élégance, tout en buvant doucement son thé, tandis que moi je tape dans ce qui semble être un sandwich avec de l'herbe dans de la pâte sèche."


"L'atmosphère semble légèrement tendue, aucun de nous ne sachant quoi dire à l'autre."


"Nous finissons notre repas dans le même silence que quand nous avons commencé. Finalement, Lilly le rompt de sa douce voix."

show lilly basic_reminisce_close
with charachange


li "Beaucoup de choses sont arrivées là-bas... n'est-ce pas ?"


hi "Oui."


"Encore une fois, silence, nous réfléchissons tous deux à la même chose. Cependant, je pense être arrivé à une conclusion à ce sujet."


hi "Je sais que tout ce qui est arrivé était un peu précipité, mais... je ne regrette rien de ce qui est arrivé à Hokkaido. Rien du tout."

show lilly basic_oops_close
with charachange


li "Hisao... ?"


"Légèrement tendu, je prends ses mains dans les miennes, à moitié pour me rapprocher, à moitié pour me calmer un peu."


hi "Je reste sur ce que je t'ai dit là-bas, Lilly. Je t'aime et je ne te quitterai pas. J'espère seulement que tu penses la même chose."

show lilly basic_weaksmile_close
with charachange


"Elle reste silencieuse un moment, un moment qui me semble durer une éternité."

show lilly invis_close at center
with dissolvecharamove


"Sa rêverie arrive à sa fin alors qu'elle retire une de ses mains des miennes, la place sur la table pour s'en servir d'appui, se redresse de sa chaise et se penche en avant."


"Après un moment d'hésitation, l'expression légèrement pensive, ses lèvres touchent brièvement les miennes."

show lilly behind_cheerful_close:
    ypos 1.1
with dissolvecharamove


"Mon cerveau s'arrête à ce moment-là, prenant à peine en compte Lilly qui se rassoit sur sa chaise en souriant, les joues rosées."

show lilly basic_smileclosed_close
with charachange


li "Cela me fait plaisir d'entendre ça, Hisao. Je serais heureuse de rester avec toi."


hi "Peut-être que ça serait bien de ralentir un peu les choses, par rapport à avant. On a toujours cours, et on a nos examens après tout."

show lilly basic_giggle_close
with charachange


"Elle émet un rire malicieux, qui se trouve être contagieux."

show lilly basic_smileclosed_close
with charachange


li "Ça serait une bonne idée en effet."

show lilly basic_smile_close
with charachange


li "Tu penses que tu t'en sortiras bien avec les examens ? Ils commencent demain comme tu l'as dit."


hi "J'aurais probablement dû réviser plus, mais je pense que je m'en sortirai."


hi "Cela dit, j'ai eu affaire à Misha et Shizune. Ta classe est aussi inquiète pour les examens que la mienne ?"

show lilly basic_weaksmile_close
with charachange


"Elle soupire, confirmant mes soupçons. Je suis content que l'atmosphère se détende."


li "Je crois bien. Deux personnes m'ont déjà demandé de l'aide et il y en aura sûrement d'autres."


hi "Penses-y comme un premier entraînement en tant que professeur, peut-être ?"

show lilly basic_smile_close
with charachange


li "C'est une bonne façon de voir les choses."

show lilly basic_smileclosed_close
with charachange


li "À ce sujet, comment t'en sors-tu en anglais ? Je me rappelle que ce n'est pas ton domaine de prédilection, et les quelques phrases que tu as mémorisées pour parler à ma mère ne t'aideront sûrement pas."


"Zut, dans le mille."


hi "Tu m'as eu. Si ça ne te gêne pas, tu pourrais m'aider dans cette matière ? S'il te plaît ?"

show lilly basic_planned_close
with charachange


li "Je t'aiderai avec plaisir, Hisao. Mais en échange..."


"Elle abaisse un peu les sourcils, sa nature coquette prenant un peu le dessus."


hi "Pas de problème. Tu t'en sortirais mieux avec quelqu'un pour t'aider, cela dit."

show lilly behind_cheerful_close
with charachange


"Un sourire rayonnant s'affiche sur son visage, une expression féminine qui me ferait presque rougir. Je pense qu'elle sait comment utiliser ses expressions pour me faire flancher. Je vais devoir être sur mes gardes."


"Cela dit, un groupe d'étude semble être une bonne méthode pour combler nos failles à tous les deux."

play sound sfx_warningbell


"La sonnerie résonne, nous rappelant que le temps ne s'est pas arrêté."


hi "Oh, la pause déjeuner est déjà finie. On perd vite la notion du temps ici."

show lilly basic_weaksmile_close
with charachange


li "Cette pièce est tellement loin des autres clubs que peu de bruit arrive jusqu'ici. C'est sûrement pour ça."

show lilly basic_weaksmile_close at center
with charamove


"Un endroit loin des autres, seul avec la personne que j'aime. Alors que Lilly ramasse son sac et sa canne, mes pensées dérivent vers les moments que nous avons passés à Hokkaido."

show lilly basic_satisfied_close
with charachange


li "Ah, avant que j'y aille, Akira et moi allons faire une petite fête pour notre retour dans ma chambre demain, tu pourras venir ?"


"...et je reviens dans le présent."


hi "Je n'ai rien de prévu, donc je devrais pouvoir trouver suffisamment de temps dans mes révisions pour venir."

show lilly basic_smileclosed_close
with charachange


li "Tant mieux."


hi "Pour ce que ça vaut, je suis content que tu sois revenue d'Écosse. Une fois que les examens seront finis, on aura plus de temps pour nous."

show lilly basic_smile_close
with charachange


li "Oui. Les vacances sont peu après, aussi."


hi "On peut commencer les vacances avec Tanabata alors, comme on se l'est promis au festival de l'école."

show lilly basic_arablush_close
with charachange


"Elle met sa main sur sa joue et rit nerveusement, se rappelant les évènements."


"Ça semble bizarre de sa part de réagir comme ça, même si je l'ai déjà vue embarrassée avant."

show lilly basic_weaksmile_close
with charachange


li "Je... ferais mieux d'y aller. Au revoir, Hisao."


hi "Salut."

hide lilly
with charaexit

stop music fadeout 6.0


"Que ce soit par habitude ou par envie de garder un semblant de normalité, je lève la main pour lui dire au revoir, comme je le fais toujours. Au moins cette fois je suis conscient de le faire."


"Je crois que je commence à voir les choses plus loin, pas seulement avec Lilly, mais aussi dans ma vie."


"Je commence enfin à me détacher de mon passé."

scene black
with dissolve




label fr_L22:

$ renpy.music.set_volume(0.8, 0.0, channel="music")
play music music_ease fadein 4.0

scene bg school_girlsdormhall
with locationchange


"Marchant dans les couloirs du dortoir des filles qui m'est maintenant légèrement plus familier, j'entends des rires étouffés plus loin."

show bg school_girlsdormhall at bgleft
with charamove


"Il ne faut pas longtemps pour que j'identifie la chambre de Lilly comme étant la source de ce rire, cependant, cette voix n'est pas la sienne, mais celle de sa soeur."

play sound sfx_doorknock2


"Je frappe à la porte avec mes trois petits coups habituels. J'ai à peine fini que la porte s'ouvre."

show akira invis:
    xanchor 0.5 xpos 1.0
with None

show akira basic_smile:
    xpos 0.9
with dissolvecharamove


aki "Salut Hisao."


hi "Salut à vous trois."


scene ev lilly_bedroom:
    truecenter
    zoom 1.0 subpixel True
    acdc_warp 8.0 zoom 1.03
with locationchange


"Hanako lève timidement la tête, ses mains cachées par sa chemise de nuit trop grande. De son côté, Lilly se tourne dans la direction de ma voix et sourit."


"Ce serait mentir que de dire que je n'apprécie pas de la voir dans ce pyjama."


"Je vois Akira m'adresser un long regard avec un petit sourire, auquel je réponds avec un regard sec."

scene bg school_dormlilly at bgleft
with locationchange


"Elle comprend, hausse les épaules et retourne s'asseoir à la table basse au centre de la chambre. Alors que je les rejoins, Lilly hoche la tête pour me saluer et commence à me verser une tasse de thé."

show hanagown distant:
    twoleft
    ypos 1.14
show akira basic_smile:
    tworight
    ypos 1.14
with charaenter


hi "Je suis content de te revoir, Hanako. On t'a moins vue récemment."


"Lilly semble concentrée en versant le liquide marron clair, mesurant avec attention la quantité, avec son doigt comme toujours."


li "Il semble que Hanako aide quelqu'un de ta classe avec le club journal. Naomi, je crois ?"

show hanagown normal
with charachange


"Hanako hoche la tête pour confirmer."


"Même après deux mois dans la classe, j'ai encore du mal à me rappeler le nom des étudiants avec qui je parle rarement."


"Il faut que je réfléchisse fort pour réussir à mettre un visage sur ce nom, mais je me rappelle finalement la fille qui s'assoit à côté de Hanako au fond de la classe."


"Naomi Inoue. Une fille à l'air normal, sauf pour sa mèche décolorée."


"Étant donné son optimisme et sa franchise, Naomi pourrait avoir vu une ouverture pour attirer Hanako dans son club quand elle envisageait d'en rejoindre un."


"Dans tous les cas, ça fait plaisir de voir Hanako élargir ses horizons. La première fois que je l'ai rencontrée, l'idée qu'elle puisse rejoindre un club avec quelqu'un d'autre que Lilly était limite risible."


hi "Ça explique pourquoi tu étais si occupée. Tu aimes bien ?"

show hanagown smile
with charachange


ha "Mh. C'est... vraiment intéressant."


"Comme toujours, Hanako est loin d'être bavarde. Certaines choses ne changent pas et il semble que la personnalité de Hanako soit l'une d'entre elles. Elle sera sûrement toujours timide."

show hanagown smile:
    center
    ypos 1.14
show akira basic_smile:
    right
    ypos 1.14
show bg school_dormlilly at center
with charamove

show lilly invis at left
with None

show lilly basic_smileclosed_paj:
    ypos 1.17
with dissolvecharamove


"Mon attention est attirée par le bruit de la tasse de thé que pose Lilly sur la table en face de moi. Je la remercie et en bois une longue gorgée. Hanako et Lilly boivent le leur, et Akira a un mug d'où sort une forte odeur de café noir."

show akira basic_laugh
with charachange


aki "Tu es un sale veinard Hisao."


hi "Hein ?"


"Je ne peux pas m'empêcher de grimacer face à son sourire moqueur, toujours visible au bord du mug pressé contre ses lèvres."

show akira basic_ending
with charachange


aki "Voir ma sœur en pyjama, il y a beaucoup d'hommes qui aimeraient être à ta place."


"J'ai vu bien plus que ça, même si je ne l'admettrai pas."

show lilly basic_emb_paj
with charachange


li "Akira !"

show akira basic_smile
with charachange


aki "Hé, je rigole."


"Elle se penche vers moi autant qu'elle le peut, chuchotant avec un sourire sournois sur le visage."

show akira basic_kill
with charachange


aki "Et Hanako aussi. Pervers."


hi "Hé, c'était son idée."

show hanagown distant_blush
with charachange


ha "Euh, je... euh..."


"Nous la regardons tous les deux, elle a la tête baissée et ses mains remuent sur ses genoux."

show hanagown smile
with charachange


ha "Si... c'est Hisao... ça ne me gêne pas..."


"Uwah. Ça pourrait mal tourner pour moi. Je sais que Hanako est trop innocente pour penser à mal, mais l'expression que m'adresse Akira est effrayante."

show lilly basic_concerned_paj
show hanagown normal

with charachange


li "Hum... Akira... s'il te plaît..."


"Il semble que Lilly arrive à sentir le changement soudain dans l'aura d'Akira, sans pour autant le voir d'elle-même."

show akira basic_boo
with charachange


"Akira détourne lentement le regard, comme un chien d'attaque rappelé par son maître juste à temps. Je soupire de soulagement."


"C'est vraiment le bon moment pour essayer de changer de sujet."


hi "Si je peux me permettre de poser la question, qu'est-ce que tu fais comme métier, Akira ? Je t'ai toujours vue dans ce costume."

show akira basic_laugh
with charachange


aki "Tu te demandes ce que tu vas pouvoir faire après la fin de l'école, hein ?"

show akira basic_smile
with charachange


aki "Je suis avocate. Je travaille dans le département légal de la branche japonaise de la compagnie de notre famille."


aki "Une réponse ennuyeuse, je suppose. Le droit est un sujet que la plupart des gens trouvent chiant."


hi "Un peu."

show akira basic_lost
with charachange


aki "Hé, tu n'es pas supposé être d'accord."

show lilly basic_giggle_paj
show hanagown normal
show akira basic_smile
with charachange


"Lilly, buvant son thé, rigole doucement de la scène, suivie de Hanako."


"Cette ambiance amicale m'avait manqué pendant que Lilly et Akira étaient en Écosse. Bien que ce qu'il s'est passé avec Hanako n'ait pas aidé, je crois que l'absence de Lilly nous a beaucoup influencés."

show lilly basic_smileclosed_paj
with charachange


li "Je suis contente d'être rentrée. Tu m'as manqué, Hisao, et toi aussi, Hanako."


hi "Pareil pour nous. J'imagine que tes camarades de classe étaient contents de te revoir aussi."

show lilly basic_ara_paj
with charachange


li "D'une certaine façon, oui."

show akira basic_laugh
with charachange


"Le petit rire amusé d'Akira montre qu'elle est consciente de ce qu'insinue Lilly quand elle dit des choses comme ça. J'imagine que c'est normal, depuis le temps qu'elles se connaissent."

show hanagown normal
with charachange


ha "C'était bien l'Écosse ?"

$ renpy.music.set_volume(0.1, 2.0, channel="music")


"Pendant un moment, je me demande pourquoi elle pose cette question, ça fait un moment qu'elles sont revenues, mais je me rappelle tout ce qui est arrivé. On n'a simplement pas eu le temps d'y penser, avec les examens et notre voyage à Hokkaido."

show lilly basic_reminisce_paj
show akira basic_annoyed
with charachange


"Lilly semble distante pendant un moment, et le fait que la première réaction d'Akira soit de regarder vers sa sœur ne m'échappe pas. Néanmoins, elle se ressaisit vite."

$ renpy.music.set_volume(0.8, 0.4, channel="music")

show akira basic_smile
show lilly basic_weaksmile_paj
with charachange


li "C'était... bien. J'ai... on... n'avait pas vu notre famille depuis longtemps, donc c'était une très belle réunion."

show akira basic_boo
with charachange


aki "Ouais, c'est vrai. Leur maison au bord de la mer, c'était la meilleure chose du voyage cela dit."


"D'après son ton distant, je crois qu'Akira n'aime pas autant sa famille que Lilly."

show lilly basic_giggle_paj
with charachange


li "Tu as seulement aimé parce que tu avais enfin le temps de t'amuser."

show akira basic_ending
with charachange


aki "Juste parce que je nage mieux que toi..."

show lilly basic_smileclosed_paj
with charachange


li "Je n'ai pas pris le côté athlétique de la famille, c'est tout."

show akira basic_laugh
with charachange


aki "Bah, au moins tu peux être sûre que tu as eu les gênes pour la taille."

show akira basic_boo
with charachange


aki "Et le tour de poitrine..."

show lilly basic_weaksmile_paj
with charachange


li "Ce n'est pas le genre de choses qui se dit en présence d'autres gens..."


"Bien que Lilly prétende gronder Akira, elle le fait avec un petit sourire moqueur sur le visage."

show hanagown distant_blush
with charachange


"Je doute qu'Akira s'en préoccupe vraiment, à en juger par son expression nonchalante. Je m'en moque aussi, mais Hanako regarde par terre et rougit jusqu'aux oreilles."


"Les chamailleries des sœurs mises à part, leurs parents ont vraiment un style de vie bourgeois."


"Ça semble complètement différent du style de vie qu'ont mené Lilly et Akira jusque-là. Je suppose que les circonstances ont choisi à leur place."


"Savoir qu'elle vient d'une lignée si aisée ne fait qu'amplifier l'air noble que dégage Lilly. Étrange qu'Akira n'ait rien de tout cela."


"Elles se ressemblent vraiment très peu pour des sœurs. Leur seule similarité semble être leur confiance en soi, ce qui peut à la fois être attachant et difficile à gérer."

stop music fadeout 2.0

scene bg school_dormlilly
show lilly basic_smileclosed_paj:
    twoleft
    ypos 1.17
show akira basic_smile:
    tworight
    ypos 1.14
with shorttimeskip


"Le reste de la soirée continue sur la même lancée, jusqu'à ce que Hanako finisse par nous quitter pour aller se coucher."


"Pendant un moment, le seul son audible est celui de la tasse et la coupelle de Lilly qui s'entrechoquent alors qu'elle boit lentement. Le silence est tendu, avec Lilly et moi attendant que l'éléphant qui est dans la pièce fasse le premier pas."

show akira basic_boo
with charachange


aki "Donc..."

$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_dreamy fadein 4.0

show lilly basic_weaksmile_paj
with charachange


"Lilly pose sa tasse, donnant une attention totale à sa sœur."


"Avec Lilly et moi d'un côté de la table basse et Akira de l'autre, on dirait presque un juge annonçant son verdict."

show akira basic_smile
with charachange


aki "Il paraît que vous sortez ensemble maintenant ?"


"Je regarde Lilly pour avoir la confirmation que c'est d'elle qu'Akira tient l'information. Elle hoche légèrement la tête en sa direction, je l'imite pour confirmer."


"Décidant que c'est le bon moment pour le faire et Akira étant le parent le plus proche de Lilly, je me penche fortement en avant, faisant révérence, les mains au sol et la tête entre celles-ci."


hi "Je prendrai bien soin de ta sœur, Akira. Je te le promets."

show lilly basic_smile_paj
with charachange


li "Tu vois ? C'est un parfait jeune gentleman."


"Elle a dû entendre ma voix venir d'une position plus basse que la normale."


"Je me redresse lentement, regardant timidement vers Akira."


"Pour dire la vérité, je doute que le juge en costume fasse une objection. Elle est le type de personne qui ne se gêne pas pour donner sa désapprobation, ce qui force le respect à mes yeux."

show akira basic_laugh
with charachange


aki "Méthode traditionnelle, hein ? Bah, il est le type de personne qui te convient bien."

show akira basic_smile
with charachange


aki "Je n'ai pas de problème avec ça et je vous souhaite du bonheur. Même si je n'avais pas été d'accord, je n'aurais pas pu faire grand-chose de toute façon."


"Je hoche la tête en sa direction en guise de remerciement, tandis que Lilly soupire, soulagée. Sûrement plus parce que c'est fait que parce qu'elle avait peur qu'Akira ait un problème à ce qu'on soit ensemble."

show akira basic_evil
with charachange


aki "Mais je me demande... comment le reste de la famille l'a pris, particulièrement celle qui réside à Yamaku ? Vous lui avez dit ?"

show lilly basic_listen_paj
with charachange


"Le sourire de Lilly se change en grimace alors qu'Akira affiche un sourire diabolique. C'est les gens qui nous connaissent le mieux qui peuvent plus facilement toucher nos points faibles, après tout."

show lilly basic_weaksmile_paj
with charachange


li "“Faire avec” doit être le meilleur terme pour la situation. N'est-ce pas, Hisao ?"


hi "Ouais, c'est à peu prês ça. Au moins elle est raisonnable."

show akira basic_boo
with charachange


aki "Tant mieux. Cette fille peut être une plaie parfois."

show akira basic_smile
with charachange


aki "On a échangé quelques messages durant et juste après le voyage, et elle était déjà sur mon dos parce que j'ai retrouvé mon copain à mon retour, laissant Hideaki trop longtemps à son goût. Elle tient vraiment à ce petit gars."


"Je me repasse en tête la réaction étrange de Shizune après que je lui aie annoncé la nouvelle, mais décide de ne pas en parler. C'est sûrement juste dû à leur antipathie mutuelle et le commentaire d'Akira le confirme bien."

show akira basic_boo
with charachange


aki "Eh bien, c'est réglé. Je dois aller au travail tôt demain, donc je ferais mieux d'y aller."

show akira basic_smile at tworight
with charamove


"Elle se lève avec un grognement, une main sur son genou pour s'aider à se lever. Je remarque les yeux d'Akira qui s'attardent sur Lilly pendant quelques secondes avant de se détourner, alors qu'elle commence à partir."

hide akira
with charaexit


"Après qu'elle ait franchi la porte, elle s'arrête et regarde en l'air d'un air songeur avant de se tourner vers nous une dernière fois."

show akira invis:
    xanchor 0.5 xpos 1.0
with None

show akira basic_lost:
    xpos 0.9
with dissolvecharamove


aki "Ah oui, j'ai presque oublié de vous dire."

show akira basic_ending
with charachange


aki "Protégez-vous. À chaque fois."


"Je m'étouffe violemment avec le thé que je bois. Contrairement à moi, Lilly reste parfaitement calme, ne semblant pas perturbée. Je suis plutôt impressionné."

show lilly basic_smile_paj
with charachange


li "On se protège, ne t'inquiète pas."

show akira basic_smile
with charachange


aki "C'est bien ma petite. À plus."

show akira invis:
    xanchor 0.5 xpos 1.0
with dissolvecharamove

hide akira
with None


"Et sur ce, elle se tourne et repart, une main levée en guise de salut tandis qu'elle disparaît dans le couloir sombre, fermant la porte derrière elle."

show lilly basic_smile_paj:
    center
    ypos 1.17
show bg school_dormlilly at bgright
with charamove


"Une fois qu'elle est partie, je m'avachis sur la table, complètement vidé de mon énergie à cause d'Akira. L'habileté de Lilly, sa façon de se contenir face au démon en costume est quelque chose que j'admire."


hi "Elle est vraiment très sournoise. Je ne crois pas que je pourrais tenir face à ta sœur."

show lilly basic_smileclosed_paj_close:
    center
    ypos 1.1
with characlose


"Alors que je sens la douce main de Lilly se poser sur la mienne, je tourne la tête sur le côté pour la voir sourire. Pendant un long moment, nous restons simplement assis l'un à côté de l'autre."


"Au vu de sa taille, elle est à peu près aussi grande que moi. Peut-être même quelques centimètres de plus. Et comme ça, elle semble encore plus grande."


"La sensation de sa pâle et douce main contre la mienne est agréable, tout autant que la vue de ses formes qu'épouse son pyjama en soie."

show lilly basic_smile_paj_close
with charachange


li "Tu t'en sors bien, même si tu dis ça."


hi "J'imagine. Tu sais, vous vous ressemblez plus que je l'ai cru au début."

show lilly basic_cheerful_paj_close
with charachange


li "C'est une bonne chose que je t'aie attrapé avant que tu ne coures après elle alors."


"Bien qu'elle en rigole, ce que j'ai dit au sujet de ne pas pouvoir suivre Akira, que ce soit physiquement ou mentalement, était véridique."


"Le caractère calme et distingué de Lilly, presque maternel, est peut-être la chose qui m'a le plus aidé dans ces premières semaines à Yamaku."


"En y pensant..."


hi "Attends... depuis quand est-ce qu'on se protège ?"

show lilly basic_pout_paj_close
with charachange


"Pendant que je lui jette un regard curieux, les joues de Lilly se gonflent alors qu'elle fait la moue en ma direction."


li "Contrairement à toi, je m'en suis rappelée. La boîte est sur l'évier."


"Donc, je ne suis pas le seul à prendre des pilules. En y repensant, je me sens un peu bête de n'y avoir pas pensé du tout et d'avoir laissé Lilly s'en occuper."


"Regardant à côté de l’évier dont elle vient de parler, je remarque les piles de livres qui étaient déjà là, la dernière fois que je suis venu. Pour la plupart, elles sont collées contre le mur pour laisser plus de place autour de la table."


hi "Pourquoi ne prends-tu pas une étagère pour tes livres ? C'est bizarre de voir les livres éparpillés comme ça, vu que le reste de ta chambre est bien rangé."

show lilly basic_smileclosed_paj_close
with charachange


li "Je les trouve plus facilement comme ça, je sais exactement dans quelle pile chaque livre se trouve."


hi "Tu y arriverais aussi s'ils étaient sur une étagère, non ?"

show lilly basic_weaksmile_paj_close
with charachange


li "Peut-être, mais bon..."


"Elle non plus n'est pas immunisée contre la paresse, après tout."


hi "Tu en as tellement, c'est dommage qu'on ne puisse pas se prêter nos livres alors que nous sommes tous deux de gros lecteurs."

show lilly basic_giggle_paj_close
with charachange


"Ça la fait un peu rire."


hi "D'ailleurs, pourquoi tu commandes tes livres via Yuuko ? J'imagine qu'il y a plein de sites où tu peux commander tes livres en braille, surtout en anglais. Il y a plein de programmes de lectures de textes aussi, d'ailleurs."

show lilly basic_displeased_paj_close
with charachange


"Elle détourne légèrement la tête, ce qui me surprend quelque peu."


li "Je ne suis... pas bonne du tout avec les ordinateurs. Je m'en sors avec les machines à écrire normales et en braille... mais c'est tout."


"Son ton me fait sourire. C'est une personne fière, alors admettre ce genre de chose doit être difficile."


"Alors comme ça, Lilly est le genre de personne peu douée avec la technologie. Étant donné sa personnalité un peu traditionnelle, ça ne m'étonne pas tellement."


hi "Je ne m'inquièterais pas si j'étais toi. Beaucoup de gens ont du mal avec les ordinateurs, c'est pas si gênant."

show lilly basic_concerned_paj_close
with charachange


li "“C'est” gênant..."


"Maintenant elle est encore plus déprimée. J'ai l'impression de remuer le couteau dans la plaie, plutôt que de la réconforter."

show lilly basic_weaksmile_paj_close
with charachange


"En me tortillant un peu, je me rapproche d'elle et place timidement ma main autour de sa taille pour la serrer contre moi. Je ne suis toujours pas habitué à ce genre de contact physique, mais Lilly semble apprécier."

scene ev lilly_kissing
with whiteout


"Lilly sourit et se tourne vers moi, s'approchant pour m'embrasser, comme pour me récompenser de mes actions. Elle frôle d'abord mes lèvres avec les siennes avant de m'embrasser vraiment."


"De cette façon, elle accapare chacun de mes sens. La légère odeur de ses cheveux, le goût de sa langue effleurant la mienne, la tendresse de ses lèvres, l'image d'elle dans mon esprit, le silence est total en dehors de sa légère respiration..."


"On s'est déjà embrassés auparavant et même si c'est plus un baiser de simple affection qu'autre chose, c'est toujours une sensation nouvelle et agréable."

scene bg school_dormlilly at bgright
show lilly basic_cheerfulblush_paj_close:
    center
    ypos 1.1
with locationchange


"À en juger par son visage rouge lorsqu'elle se recule, il est évident qu'elle pense à la même chose que moi. Même si nous sommes seuls, il est toujours un peu embarrassant de s'ouvrir autant l'un à l'autre."

show lilly basic_smileclosed_paj_close
with charachange


li "Si on prend tout au jour le jour, je crois que ça se passera mieux. Par petits pas hein ?"


hi "Ouais. Juste des petits pas."


"On a tout notre temps, même si après la fin de l'année scolaire on emménage ensemble ; je crois que tout ira bien. Aucun d'entre nous n'a l'intention de partir, après tout."


"Pour l'instant, je suis juste content de pouvoir partager ces petits moments avec elle."

stop music fadeout 2.0

scene black
with dissolve




label fr_L23:

scene bg school_nursehall
with locationchange


"Je me tiens debout devant la porte de l'infirmerie depuis ce qui semble être au moins une quinzaine de minutes."


"Ce n'est pas comme si je n'étais jamais entré dans cette petite pièce beige auparavant, ou que j'étais inquiet de la visite comme le serait un enfant."


"Peut-être que c'est parce que l'infirmerie ressemble un peu à un confessionnal, où j'avouerais que mon corps a un défaut. Le fait que c'est quelque chose qui reste entre l'infirmier et moi n'aide pas tellement."


"Me rappelant que la sonnerie de fin de la pause déjeuner va bientôt retentir, je soupire et ouvre la porte. Le fardeau sera bientôt fini."

play music music_nurse fadein 0.5

scene bg school_nurseoffice
show nurse neutral at center
with locationchange


nk "Tiens donc, ne serait-ce pas Nakai. Content de te voir."

show nurse grin
with charachange


nk "Ou mécontent, vu que je suis un infirmier."


"Il rit, visiblement amusé par sa petite blague. Je trouve son humour quelque peu bizarre, mais le fait qu'il puisse prendre à légère une situation comme celle-ci est réconfortant, ou du moins distrayant."

show nurse neutral
with charachange


"Son petit spectacle fini, il claque des mains et se met au travail. Je prends place une fois qu'il me fait signe de m'asseoir."


"J'aimerais que la classe ait des sièges aussi confortables. Mon esprit s'évade alors que je fais le tour de la pièce du regard, distrait par les petits changements depuis la dernière fois que je suis venu."

show nurse fabulous
with charachange


nk "D'accord, alors qu'est-ce qui t'amène ? Je ne t'ai pas vu souvent, alors j'imagine que tu te portais bien jusque-là ?"


hi "Ben, généralement."

show nurse neutral
with charachange


nk "Je vois."


"Son sourire tombe alors que je dis ça. Je me sens un peu coupable de cela. C'est dans ces moments-là que je peux m'estimer “normal” de ne pas vouloir voir l'infirmier. C'est admettre que je suis différent des autres."

stop music fadeout 5.0


hi "Quand je suis parti en voyage durant le grand week-end, j'ai eu quelques problèmes avec mon cœur."


"Il hoche la tête d'un air très sérieux, m'incitant à continuer."


hi "Je crois que c'était... ouais, c'était alors que je marchais sur une longue distance, je crois que le bon terme pour ça est palpitation cardiaque."


hi "Je me suis soudainement senti faible au niveau des jambes, presque comme si j'avais une petite crise cardiaque, et c'est passé en une demi-minute. Mais même après, je me suis senti fatigué et nauséeux."

show nurse concern
with charachange


nk "Mh. Pas bon. Pas bon du tout."


nk "C'était il y a combien de jours, exactement ? Tu as fait quelque chose d'autre d'inhabituel avant ça, mis à part la marche ? Tu prenais bien ton traitement ?"


"L'infirmier passe de blagueur bizarre au mode professionnel sérieux de la santé, prenant des notes et tapant des trucs sur son ordinateur."


"Je lui dis que j'ai oublié de prendre mes pilules ce matin-là et la veille au soir. C'était idiot, mais je ne peux pas changer l'histoire maintenant, je ne peux que répondre honnêtement et serrer les dents."


"Son sérieux se change en froncement de sourcils et la discussion se transforme en une auscultation."

hide nurse
with shorttimeskip


"Je finis de boutonner ma chemise et vais me rasseoir sur la chaise en face de l'infirmier."

show nurse concern at center
with charaenter


nk "C'est la première fois que tu as un problème cardiaque depuis que tu es à Yamaku ?"


hi "J'ai déjà eu des légères douleurs à la poitrine auparavant, juste quelques fois, mais c'était surtout plus de l'inconfort qu'une réelle douleur."


"Il se met au fond de sa chaise, ressemblant légèrement à Hercule Poirot dans une chemise blanche, méditant sur un cas mystérieux de palpitation cardiaque."


"Bougeant les lèvres de droite à gauche pour montrer qu'il réfléchit, sa moustache inexistante se tortillant, il arrive finalement à une conclusion."

show nurse fabulous
with charachange

play music music_nurse fadein 1.0


nk "Bon, tu as survécu. C'est déjà une bonne chose."


"Je ne suis pas sûr de comprendre, puis remarque que l'infirmier fait son expression “je t'ai eu”."


"C'est rassurant, cela dit. Je ne crois pas qu'il sortirait des blagues comme ça si c'était vraiment sérieux. Donc je reste silencieux et je me détends."

show nurse neutral
with charachange


nk "Je vais devoir parler avec ton médecin, mais je pense que c'est simplement dû à l'effort physique."


nk "Tu as continué de faire de l'exercice léger comme je te l'avais demandé ?"


hi "Je m'assure de marcher tous les jours, c'est généralement suffisant pour transpirer un peu, mais encore une fois, je ne suis pas aussi en forme que je l'étais avant."


nk "Ça devrait suffire alors. Le principal, c'est de garder à l'esprit de faire de l'exercice à faible stress, pas de sprint ou quelque chose de brusque."


hi "Je sais. Depuis que j'ai quitté l'hôpital, je me suis beaucoup plus concentré sur mes études, en partie pour ne pas penser au fait que je ne suis plus capable de faire beaucoup de choses physiques."

show nurse grin
with charachange


nk "Je suis content d'entendre que tu t'adaptes bien à un changement de vie aussi soudain. Tout semble être en ordre. Presque tout, je dirais."

show nurse neutral
with charachange


nk "Cependant, je veux garder un œil sur toi pendant un moment, juste observer un peu, tu comprends."


"C'est quelque chose que je ne voulais vraiment pas entendre. Depuis que je suis à Yamaku, tout ce que je veux, c'est vivre une vie aussi normale que possible."


"“Observation” était l'un des mots que j'en suis venu à détester durant mon séjour à l'hôpital. Pendant si longtemps je voulais juste me lever et franchir les portes de l'hôpital, mais les médecins voulaient absolument me garder en “observation”."


hi "D'accord. Je devrai venir plus souvent ?"


"Il vérifie le calendrier à côté de son ordinateur, puis fronce les sourcils, avant de se retourner vers moi."

show nurse concern
with charachange


nk "Ça serait gênant durant les vacances d'été, vu la période..."


nk "Je verrai avec ton docteur et j'essayerai d'avoir une meilleure vue de la situation, voir comment il veut procéder, mais je crois que tu devrais juste prendre les choses prudemment et calmement à partir de maintenant."


nk "Ce que tu décris n'a pas l'air d'être un évènement récurrent, mais ça ne te ferait pas de mal de ralentir les choses pendant un moment, juste pour être sûr."


hi "Qu'est-ce que je dois faire pour les cours de cet après-midi ?"


"Il regarde l'horloge sur le mur au-dessus de mon épaule. Je ne l'aurais même pas remarquée si je n'avais pas suivi son regard."

show nurse fabulous
with charachange


nk "Il est presque l'heure de la fin des cours, donc tu pourrais tout aussi bien partir plus tôt."


"Il m'adresse un clin d'œil, s'assurant que je comprenne qu'il me fait une faveur."


hi "Bon, ordres de l'infirmier. Merci."

show nurse grin
with charachange


nk "Je suis là pour ça après tout."

show nurse neutral
with charachange


nk "Je sais que tu n'as pas envie d'entendre ça, mais tu ne peux pas ignorer ta condition. N'hésite pas à venir me voir si tu as des problèmes, ou même si tu veux juste me demander quelque chose. Au revoir."

hide nurse
with charaexit


"Il tourne sur sa chaise et retourne à son clavier. Je pense que je vais lire jusqu'à ce qu'il soit l'heure d'aller attendre Lilly au portail, vu que je n'ai pas grand-chose d'autre à faire."

stop music fadeout 3.0


"Alors que je pars, ses mots me reviennent en tête. Ma condition n'est pas aussi handicapante que pour la plupart des gens ici à Yamaku et je ne veux pas que Lilly s'embête pour ça."


"Si je vis normalement et évite les coups à la poitrine, ça ira. Je ne laisserai pas ma condition me dominer."

scene bg school_gate_ss
show lilly cane_smileclosed_ss at center
with shorttimeskip

play music music_tranquil fadein 3.0

play sound sfx_normalbell


"Lilly est en vue peu après que la sonnerie de fin de cours retentisse. Elle dit au revoir à quelques-uns de ses camarades de classe qui partent dans l'autre direction, avant de commencer sa virée hebdomadaire vers l'épicerie."


hi "Bonjour Lilly."

show lilly cane_smile_ss
with charachange


"Le sourire immédiat et chaleureux qui s'affiche sur son visage après avoir remarqué ma présence fait chaud au cœur."


li "Bonjour, Hisao."

show lilly cane_smileclosed_close_ss
with characlose


"Elle hésite pendant une seconde puis avance le visage en fermant les yeux. Mes lèvres rencontrent les siennes avec une certaine impatience avant que nous nous séparions, main dans la main."


"Le fait que nous soyons presque de la même taille est parfois pratique. Cela évite que l'un de nous deux lève la tête pour qu'on puisse s'embrasser."

scene bg school_road_ss
with locationchange


"Il ne nous faut pas longtemps pour laisser le bruit des autres étudiants derrière nous, la canne de Lilly étant la seule chose se faisant entendre."


"Un silence, un doux silence est tout ce qui nous accueille tandis que nous descendons lentement la colline sous le soleil couchant."


hi "Je crois que je commence à vraiment aimer cette ville. Les grandes étendues vertes, les arbres partout, les bâtiments rustiques..."

show lilly cane_smile_close_ss at center
with charaenter


li "Donc tu apprécies la tranquillité d'ici aussi ?"


hi "Je crois bien. Je viens d'une ville proche de Tokyo, donc la tranquillité d'ici a été vraiment dépaysante au début."


hi "Puis après un moment, c'est devenu vraiment bien. Je crois que je préfère cela à l'activité de ma ville natale maintenant."

show lilly cane_smileclosed_close_ss
with charachange


li "Je préférais déjà les zones rurales telle que celle-ci avant même d'arriver. Je suppose que c'est parce que j'ai grandi à la campagne."

show lilly cane_weaksmile_close_ss
with charachange


li "Hanako trouve aussi que les environs sont jolis."


"Lilly dit peut-être ce genre de chose facilement, mais chaque fois qu'elle mentionne comment les autres lui décrivent les alentours comme beaux ou magnifiques, je me sens un peu mal."


"Je remarque que son expression est celle qu'elle a quand elle s'attend à ce que je pose une question. Elle devine toujours lorsque quelqu'un ne dit pas ce qu'il pense, je ferais donc tout aussi bien de lui dire."


hi "Je me demandais... euh, comment dire ça..."


hi "Est-ce que tu... regrettes de ne pas pouvoir voir les choses par toi-même ? C'est juste quelque chose que je me demandais."

show lilly cane_listen_close_ss
with charachange


"Elle réfléchit pendant un moment."

show lilly cane_smileclosed_close_ss
with charachange


li "Tu as déjà regretté de ne pas pouvoir entendre les gens chuchoter de l'autre côté de la pièce ?"

show lilly cane_smile_close_ss
with charachange


li "Je ne peux parler que pour moi, mais c'est la façon dont j'ai toujours vécu les choses. Tout comme je ne peux pas faire des choses que tu fais, tu ne peux pas faire des choses que je fais."

show lilly cane_weaksmile_close_ss
with charachange


li "Le fait que le monde soit fait pour ceux qui peuvent voir est gênant parfois, mais il y a beaucoup, beaucoup de gens qui souffrent plus que moi de par la façon dont le monde est fait."


hi "C'est logique, mais bon, c'est toujours étrange de décrire à quelqu'un quelque chose qu'il ne peut pas expérimenter."

show lilly cane_surprised_close_ss
with charachange


"Elle penche la tête d'un air interrogateur, comme si j'avais dit quelque chose qui n'était pas du tout logique."


li "Mais je peux l'expérimenter."

show lilly cane_smile_close_ss
with charachange


li "Tu as dit toi-même que tu aimes cet endroit parce que les environs sont agréables. Je l'aime exactement pour la même raison."

show lilly cane_smileclosed_close_ss
with charachange


li "Grâce au fait que c'est une petite ville rustique entourée par les arbres, ça la rend calme comparée au vacarme de l'école, sans même mentionner les odeurs de la ville."


"J'imagine que ça ressemble aussi beaucoup à la maison qu'elle a habitée avec Akira."


"Elle a une vision particulièrement fine de tout cela et je ne suis pas surpris qu'elle ait un bien meilleur contrôle de sa condition que moi de la mienne."


"Tout comme le fait qu'elle ait réussi à s'adapter à Yamaku rapidement parce qu'elle vient d'un endroit similaire, même si le fait qu'elle soit aveugle l'a ralentie."


"Je devrais arrêter de m'embêter autant avec ça, mais je ne peux pas m'empêcher de penser que j'ai trop dépendu de Lilly, étant donné les circonstances dans lesquelles les gens doivent s'adapter ici."


hi "C'est logique. Tu es douée pour expliquer, comme toujours."


hi "En y pensant, où est Hanako d'ailleurs ? Elle était avec nous au déjeuner."

show lilly cane_weaksmile_close_ss
with charachange


li "Il semblerait qu'elle soit occupée à étudier. Les examens sont loin d'être finis et elle a dit qu'elle voulait faire mieux cette année que la précédente."


hi "Bien que j'admire son sérieux, elle s'arrange vraiment pour nous laisser plus d'espace récemment."

show lilly cane_reminisce_close_ss
with charachange


li "C'est son genre j'imagine, le type de personne qui place les autres avant elle chaque fois qu'elle en a l'occasion. C'est une gentille fille, qui a beaucoup souffert dans le passé."

show lilly cane_weaksmile_close_ss
with charachange


li "Je ne sais pas... J'ai l'impression que c'est seulement maintenant, depuis qu'elle s'éloigne de moi, qu'elle commence à vraiment se trouver."

show lilly cane_smile_close_ss
with charachange


li "C'est grâce à toi qu'elle est devenue plus confiante après tout, pas à moi."


"Je retire ma main de la sienne et la place sur sa tête."


hi "L'important c'est ce que tu étais là pour elle. Je ne peux même pas imaginer ce que ça aurait été si elle n'avait pas trouvé quelqu'un comme toi. Ça s'est confirmé quand tu étais en Écosse."


hi "On est toujours amis tous les trois, donc on devrait juste croire en elle. Je pense qu'elle deviendra quelqu'un de bien et cela, c'est grâce à toi, parce que tu as été là quand elle en avait le plus besoin, tout comme tu as été là pour moi."

show lilly cane_weaksmile_close_ss
with charachange


li "Ça me donne un air un peu enfantin quand tu sembles si avisé."


hi "J'essaye du moins."


hi "Tu fais quelque chose ce week-end, par hasard ?"

show lilly cane_surprised_close_ss
with charachange


li "Pas que je sache. Pourquoi ?"


hi "Alors que dirais-tu d'un rendez-vous dimanche ? Ça fera quelque chose à faire en dehors des révisions pour les examens."

show lilly cane_smileclosed_close_ss
with charachange


"Comme pour rassurer mon cœur battant la chamade, elle sourit et hoche la tête."


li "Ce serait avec plaisir."


hi "Où est-ce que tu voudrais aller ?"

show lilly cane_displeased_close_ss
with charachange


"Son visage affiche immédiatement une expression de mécontentement."


li "Tu ne peux pas faire ça, Hisao, c'est de la triche."


hi "Faire quoi ?"


li "Un gentleman ne devrait jamais demander à une fille où elle voudrait aller en rendez-vous."

hi "Ah… oh."

show lilly cane_smile_close_ss
with charachange


"Son sourire revient vite, me montrant qu'elle n'était pas si sérieuse."

show lilly cane_smileclosed_close_ss
with charachange


li "Ne t'inquiète pas. Je réfléchirai à un endroit où aller."


hi "Je te laisse faire alors. Je promets de décider la prochaine fois."

stop music fadeout 4.0


"Avec nos plans faits pour le week-end, le reste de la promenade continue en silence."


"L'espérance que cela dure pour toujours est brisée quand j'aperçois une forme familière au loin, nous attendant, la main levée."

show lilly cane_smileclosed_close_ss at twoleft
show bg school_road_ss at bgleft
with charamove

show akira basic_smile_ss at tworight
with charaenter


aki "Yo."

scene bg suburb_konbiniint
with shorttimeskip

play music music_daily fadein 0.5


"Vendeuse" "Merci beaucoup, au revoir !"

scene bg suburb_konbiniext_ss
with locationchange


"Le changement de température alors que je franchis la porte me fait frissonner. On sens déjà que l'été commence à passer."

show lilly cane_weaksmile_ss at center
with charaenter


"Tournant la tête, Lilly semble penser la même chose, sauf qu'elle n'arrive pas à le cacher. C'est quelque chose que je n'avais pas remarqué au début, à quel point elle est délicate physiquement, même en comparaison de Hanako."


"Si je devais la décrire, je dirais qu'elle me fait penser à une poupée de porcelaine."

show akira basic_ending_ss at center behind lilly
with charaenter

show lilly cane_surprised_ss
with vpunch

show lilly cane_reminisce_ss at twoleft
show akira basic_ending_ss at tworight
show bg suburb_konbiniext_ss at bgleft
with dissolvecharamove


"Akira lui tape plusieurs fois sur l'épaule, comme pour lui transmettre de la vigueur, tout ceci au grand désarroi de Lilly, qui pendant un moment semble envieuse de mon statut d'enfant unique, tout comme moi je le suis d'avoir quelqu'un d'aussi proche."

show lilly cane_listen_ss
show akira basic_boo_ss
with charachange


"Elles parlent pendant un moment alors que je trie mes sacs, leurs voix étant trop faibles pour que je puisse les entendre, et finalement on repart en direction de l'école."

scene bg school_road_ss
show akira basic_smile_ss at tworight
with locationskip


aki "Ah, ça fait du bien d'être enfin sorti de ce fichu bureau. Vous les gamins ne savez pas la chance que vous avez d'être là."

show lilly cane_displeased_ss at twoleft
with charaenter


li "Gamins..."

show akira basic_laugh_ss
with charachange


aki "Tss. “Vous deux”, alors. Les gamins grandissent trop vite de nos jours."

show lilly cane_pout_ss
with charachange


li "Tu n'es pas assez vieille pour dire ça."

show akira basic_lost_ss
with charachange


aki "Je sais pas. Trainer avec Hideaki me donne l'impression d'être super vieille, il est si précoce qu'il me rappelle toi quand tu étais plus jeune."

show lilly cane_weaksmile_ss
with charachange


li "C'est un gentil garçon. Ça serait dommage que Shizune l'influence trop."

show akira basic_laugh_ss
with charachange


"Akira semble être amusée par l'empathie de sa sœur. Elle ne semble pas vraiment prendre ça au sérieux, mais plutôt comme une dispute enfantine."

show akira basic_smile_ss
with charachange


"Elle regarde dans ma direction, semblant se rappeler que je suis là, et sourit alors qu'elle attrape quelque chose dans sa poche arrière."


hi "Qu'est-ce qu'il y a ?"

show akira basic_ending_ss
with charachange


aki "Attends une seconde, laisse-moi le sortir..."


"Après quelques difficultés, elle réussit à sortir son portefeuille en cuir noir de sa poche arrière, et y prend rapidement ce qui semble être un petit papier."


"Alors que Lilly ignore ce qui se passe, Akira déplie le papier et me le tend."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

show stallphoto_insert:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)


"Une vieille photo de... ce qui semble être Lilly et Shizune plus jeunes en train de tenir un stand de nouilles, avec une autre fille à l'arrière. Elle me semble vaguement familière, mais je n'arrive pas à savoir qui elle est."

show lilly cane_smile_ss
with None

$ renpy.music.set_volume(1.0, 1.0, channel="music")

show stallphoto_insert:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide stallphoto_insert
with None


li "Qu'est-ce qu'il y a Akira ?"

show akira basic_boo_ss
with charachange


aki "Je crois que tu sais."

show lilly cane_listen_ss
with charachange


"Lilly réfléchit un moment avant de réaliser."

show lilly cane_surprised_ss
with charachange


li "Akira... tu n'avais vraiment pas à..."

show akira basic_smile_ss
with charachange


aki "C'est pas grave. En plus, c'est genre la seule photo de toi que j'ai depuis que tu es à Yamaku de l'époque où vous ne vous faisiez pas la guerre."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

show stallphoto_insert:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)


"Je regarde la photo dans ma main."


"Ça fait bizarre de voir Lilly et Shizune travailler ensemble si sérieusement sans aucun signe d'animosité. La photo semble avoir été prise durant le festival de Yamaku, donc elle date d'un an ou deux."


"En d'autres mots, l'époque où elles étaient ensemble au Conseil des Étudiants."


hi "Qui est la fille derrière ? Elle me semble familière."


aki "Ah, je savais que tu la reconnaîtrais pas. C'est Misha avant qu'elle se teigne les cheveux."


hi "C'est Misha ? Pas possible..."


"C'est bizarre de voir Misha sans ses cheveux si distinctifs. À en juger par le ton d'Akira, elle n'est pas favorable au choix de Misha."


"Je pense que ça accentue le côté bizarre de la situation. De penser qu'elles aient pu être aussi proches dans le passé... J'aimerais bien pouvoir faire quelque chose pour recoller les morceaux."


li "Tu es bien silencieux, Hisao."


hi "Ça fait juste bizarre de vous voir ensemble comme ça."


"Lilly ouvre la bouche pour dire quelque chose, mais s'arrête. En fin de compte, ça ne me regarde pas. C'est entre Shizune et Lilly, et personne d'autre."


li "Les choses changent. Malheureusement."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

stop music fadeout 6.0

show akira basic_resigned_ss
show lilly cane_reminisce_ss
with None

show stallphoto_insert:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide stallphoto_insert
with None


"Je rends la photo à Akira, qui soupire et la range dans son portefeuille. Un petit souvenir, une nouvelle fois caché, pour être ressorti une autre fois."


aki "Ouais, c'est ce qu'elles font."


"Je croyais que la réponse d'Akira était simplement en commentaire à la situation entre Lilly et Shizune, mais elle a l'air quelque peu mélancolique. Quelque chose que Lilly a remarqué aussi."


hi "Qu'est-ce qu'il y a ?"

show akira basic_boo_ss
with charachange


aki "Ah, c'est juste que je vais devoir aller en Écosse bientôt."


hi "Tu repars pour l'Écosse ?"

show akira basic_lost_ss
with charachange


"Pendant un long moment, Akira semble surprise, c'est une drôle d'expression pour elle."


"Après un regard en direction de Lilly, elle se tourne vers moi comme si de rien n'était."

show akira basic_resigned_ss
with charachange


aki "Ouais, dans quelques semaines je pars travailler au siège de ma compagnie, à Inverness. C'est une très bonne promotion dans la société et c'est une chance qui n'arrivera qu'une fois."


"Donc Akira va quitter le Japon, apparemment pour de bon..."


"J'ai comme l'impression que ma vision, où nous pourrions vivre heureux comme ça, dans notre petit monde isolé, arrive à sa fin. C'est troublant."


"Je regarde Lilly, légèrement étonné qu'elle ne m'ait pas dit une telle chose alors qu'habituellement elle est si directe."


"Elle continue de marcher avec le visage dirigé vers l'avant. Je ne peux pas voir son expression, ou même deviner ce qu'elle pense, ce qui est gênant étant donné que j'y arrive facilement généralement."


"Ça me rappelle cette fois où on s'est rencontrés au Shanghai, juste avant ce qu'on pourrait appeler notre premier rendez-vous. À ce moment, tout ce que je pouvais faire, c'était la réconforter sans même savoir pourquoi, et maintenant c'est pareil."

scene bg school_dormext_full_ni
show akira basic_resigned_ni at tworight
show lilly cane_reminisce_ni at twoleft
with shorttimeskip


"Alors que nous atteignons enfin les dortoirs de l'école, il y a un silence quelque peu gênant. Je ne pense pas être le seul à le ressentir."


hi "À demain alors, Lilly. Au revoir Akira."

show lilly cane_weaksmile_ni
with charachange


li "Bonne nuit, Hisao."

show akira basic_smile_ni
with charachange


aki "À plus."

hide lilly
hide akira
with charaexit


"Et sur ce, elles partent en direction du dortoir des filles."


"Ouvrant la porte du dortoir des garçons, je m'arrête et les regarde s'éloigner un petit moment jusqu'à ce qu'elles disparaissent derrière la grande porte en bois."


"Quand Akira a dit qu'elle allait partir, c'était ... bizarre. Bien que ce ne soit pas la première fois que ma nouvelle vie est remise en question, c'est sans doute la première fois que c'est aussi brutal."


"Je ne sais toujours pas quoi penser de la réaction d'Akira, et encore moins de celle de Lilly."


"La fraîcheur de la nuit me rappelle que je devrais retourner à ma chambre avant d'attraper quelque chose, les sacs au bout de mon bras semblant avoir doublé de poids."


"De toute façon, j'ai un rendez-vous avec elle prévu ce week-end. J'ai juste besoin d'arrêter de penser autant et de prendre les choses comme elles sont."


"Les examens sont toujours en cours après tout, et avec la fin du trimestre et les vacances d'été arrivant bientôt, j'ai de quoi m'occuper."


"Alors que je bâille et rentre à l'intérieur, mes pensées se tournent vers ce que va choisir Lilly comme lieu pour notre rendez-vous de ce week-end."

scene black
with dissolve



label fr_L24:

scene bg city_restaurant at Fullpan(10.0)
with dissolve

play music music_jazz


"C'était sûrement le dernier endroit auquel j'aurais pu penser quand Lilly a dit qu'elle déciderait où se déroulerait notre rendez-vous."


"Personne n'est habillé autrement que sur son trente et un, ce qui convient bien à cet endroit ; un papier peint rouge à motifs orne les murs alors que les lumières de la ville, bien en dessous, brillent et vacillent."


"Combiné au bourdonnement de discussions discrètes et au son aigu des couverts et verres à vin, l'ambiance est très formelle et pourtant assez relaxée pour que je ne me sente pas crispé, étant donné que c'est notre premier vrai rendez-vous."


"Une fois que nous sommes assis, notre serveur part servir d'autres personnes avec une petite courbette, après un hochement de tête de la part de Lilly."


"Loin de dépendre de mon aide, Lilly a réussi à se déplacer facilement jusque-là, malgré un environnement inconnu. Une petite correction ça et là, mais elle est généralement douée pour s'orienter quand elle en a besoin."

$ ksgallery_unlock("evul lilly_restaurant_listen")
scene ev lilly_restaurant_listen at restaurant_out
with whiteout


"Mes yeux se tournent vers Lilly. Je peux voir à son expression qu'elle écoute ce qui se passe, tout comme moi je regarde."


"Pour dire vrai, mon regard s'arrête sur elle à chaque fois que je balaye les environs du regard. Sa qipao rouge fait ressortir son visage et met en valeur ses jambes. Même ses cheveux sont bien coiffés, accompagnés d'une odeur de parfum."


"Bien que mon costume noir soit une location, j'ai réussi à en trouver un approprié. Il est étonnamment confortable étant donné que j'en ai rarement porté un et il correspond à l'endroit, tout comme la tenue de Lilly."


hi "C'est une nouvelle expérience pour nous deux, alors ?"

$ ksgallery_unlock("evul lilly_restaurant_sheepish")
show ev lilly_restaurant_sheepish at restaurant_out
with charachange


"Elle se tourne vers moi, quelque peu penaude."


li "Oui, je ne suis jamais venue dans un tel établissement auparavant."


hi "Un sacré premier rendez-vous, ça c'est sûr. Ça va être difficile pour moi d'égaler ça."


"Un petit rire. Même maintenant, notre nervosité se dissipe."


"Sa main parcourt le long de la table jusqu'à ce qu'elle touche le menu, qu'elle prend à deux mains et me tend."


li "Hum, Hisao ?"


"Alors qu'elle tient le menu juste en dessous du niveau de ses yeux, je peux voir un autre regard penaud."


"Je doute que demander un menu en braille au serveur serve à quelque chose."


hi "Je peux te le lire, pas de problème."

scene bg city_restaurant at right
with locationchange


"Je prends le mien et le lis rapidement, avec un sourire hésitant."


hi "Erh, il y en a peut-être un."

show lilly basic_weaksmile_che_close:
    center
    ypos 1.1
with charaenter


li "Qu'est-ce qu'il y a ?"


hi "Il y a pas mal de trucs là-dedans et je ne suis pas sûr de la prononciation de certains d'entre eux."


"La carte présente une liste de plats raffinés. La plupart d'entre eux sont écrits en japonais, mais certains sont en anglais ou en français. J'imagine que je devais m'y attendre, mais pour certains plats, je ne sais pas du tout ce que c'est."


"Oh, celui-là je reconnais. Attends..."


hi "...Ça se cuisine ça ?"

show lilly basic_giggle_che_close
with charachange


"Un petit rire se fait entendre de l'autre côté du menu."


hi "Bon, je pourrais tous te les lire, mais ça me prendrait quelques heures."

show lilly basic_smile_che_close
with charachange


li "Il y a quelque chose avec du poisson ?"


hi "Voyons voir..."


"Non. Non. Non. Non. C'est pas empoisonné ça ? Non. Non. Non. Ils mangent ce truc ? Non. Non. Non. Non... Ah, voilà."


hi "La salade au thon semble être un bon choix. D'après la photo, ça semble être plutôt copieux en plus."

show lilly basic_smileclosed_che_close
with charachange


li "Ça semble être une bonne option."


hi "Commandons-en deux alors. Je suis sûr que certains de ces plats sont faits à partir d'animaux toxiques. J'ai eu mon lot d'évènements mortels pour l'instant."

show lilly basic_weaksmile_che_close
with charachange


"Lilly continue de sourire, mais ne rit pas. L'humour noir ne doit pas être sa tasse de thé, pour être honnête ce n'est pas tellement la mienne non plus."


li "En tout cas il y a des odeurs intéressantes. Ça doit valoir pour ce qu'il y a à voir aussi, j'imagine."


hi "Je n'ai jamais été dans un endroit comme celui-ci. Une maison de thé japonaise une fois ou deux, mais jamais dans quelque chose d'aussi occidental."


"Avant que je ne puisse dire autre chose, un serveur corpulent dans une veste serrée apparaît devant nous pour prendre notre commande."


hi "Deux Salades Provençales Niçoises au Thon, s'il vous plaît."


"J'espère que je n'ai pas trop foiré la prononciation. Même si c'est le cas, il ne laisse rien paraître."

show lilly behind_cheerful_che_close
with charachange


li "Et pourrais-je avoir un verre de Chardonnay aussi, s'il vous plaît. Hisao ?"


hi "Oh, euh, pareil."


"Alors que le serveur hoche la tête et part, je réalise soudainement que j'ai imité sans réfléchir la réponse de Lilly. Je le regrette rapidement."


hi "Alcool..."

show lilly basic_pout_che_close
with charachange


li "Seulement un peu."


"Cette fille a tendance à devenir vite accro aux choses. Sérieux..."


hi "Étonnamment ils n'ont pas demandé nos cartes d'identité."


hi "Cela dit, j'imagine qu'on a l'air plutôt mature pour notre âge."

show lilly basic_smileclosed_che_close
with charachange


li "Je vais devoir te croire sur ce coup. Cela dit, je dirais aussi que ce n'est pas le genre d'endroit où ils la demandent."


hi "Pas faux."


"Nous nous relaxons un peu tous les deux, essayant de penser à autre chose que l'étouffante solennité de l'endroit."


"Peu après, le même serveur réapparaît à notre table avec deux verres vides et une bouteille, versant le vin dans les deux verres d'une manière rapide et professionnelle."

scene ev lilly_restaurant_wine:
    zoom 1.05 xalign 0.0 yalign 0.5 subpixel True
    easeout 8.0 zoom 1.0
with flash


"Nous hochons tous les deux la tête alors qu'il part, Lilly prenant son verre et le remuant doucement. Le liquide à l'intérieur brille alors qu'il parcourt le verre et je dois admettre que ça me fait moins regretter d'avoir commandé la même chose."


"J'imagine que ce doit être difficile d'estimer comment se comporte le liquide à l'intérieur du verre simplement avec le poids. Peut-être que c'est comme avec l'origami, Lilly utilise chaque chance d'améliorer sa dextérité."


hi "Je ne suis pas surpris que tu connaisses un endroit comme celui-ci. Ce sont plutôt ceux qui ont de l'argent qui doivent connaître, j'imagine."


"Ça me rappelle à quel point nos éducations sont différentes. À Yamaku, il est facile d'oublier les appartenances sociales et économiques des étudiants, vu qu'ils portent tous le même uniforme et vivent dans le même dortoir."

scene bg city_restaurant at right
show lilly basic_smile_che_close:
    center
    ypos 1.1
with flash


li "En fait, c'est Akira qui m'a parlé de cet endroit. Apparemment, elle est déjà venue ici avant."


"Donc c'est de ça qu'elles parlaient vendredi."


hi "Et tu m'accuses de tricher ?"

show lilly basic_displeased_che_close
with charachange


li "Ce n'est pas tricher. C'est simplement utiliser ses contacts personnels."


hi "Si tu le dis. Cela dit, j'ai le sentiment que tu es plus familière avec ce genre de restaurants que je ne le suis."

show lilly basic_reminisce_che_close
with charachange

with Pause(0.5)

show lilly basic_smileclosed_che_close
with charachange


"Elle s'arrête un moment, une expression mélancolique sur le visage, avant de recommencer à sourire. Le compliment semble lui avoir fait plaisir."

show lilly basic_planned_che_close
with charachange


li "C'est à cause de mon ancienne école. Ça serait les décevoir que de viser plus bas."


"Elle a déjà mentionné sa précédente école auparavant, mais maintenant je suis curieux. Elle semble penser beaucoup à son passé, donc je ne vois pas de problème à lui demander."


hi "Elle était comment ?"

show lilly basic_smile_che_close
with charachange


li "C'est une prestigieuse école catholique pour filles, c'est pour ça que mes parents l'ont choisie pour moi. Beaucoup de familles aisées envoient leurs filles là-bas."


hi "D'après ce que t'en dis, ça semblait être strict."

show lilly basic_weaksmile_che_close
with charachange


li "Je ne dirais pas que c'était une mauvaise expérience... mais c'est vrai, elle était très stricte. Heureusement, j'ai réussi à m'adapter et à me faire quelques amies."

show lilly basic_reminisce_che_close
with charachange


li "Malheureusement, on ne peut pas en dire de même pour ma soeur. Elle trouvait l'atmosphère et l'aspect religieux étouffants et elle a fini par partir pour travailler dès qu'elle a pu."

show lilly basic_weaksmile_che_close
with charachange


"Elle laisse sortir un petit rire."


li "Je ne devrais pas me plaindre, quand même. Beaucoup n'ont même pas la chance d'aller dans une telle école."


hi "Tu... en veux à tes parents de t'avoir envoyée là-bas, puis d'être partis ?"


"Elle secoue la tête."

show lilly basic_reminisce_che_close
with charachange


li "Ma famille est très patriarcale. Mon père, qui ne pense toujours qu'au travail, ne savait vraiment pas quoi faire de moi."

show lilly basic_weaksmile_che_close
with charachange


li "En fin de compte, il a décidé que mon éducation était plus importante que le contact familial."


li "Il a juste jugé que ce serait le mieux."


"Dire des choses comme ça aussi facilement. Quelle fille incroyable. Cela dit, je suis un peu surpris qu'elle ne pense pas que sa cécité ait joué une part dans tout cela... Peut-être que je juge trop sévèrement sa famille."


hi "Tu es trop gentille, tu le sais ça ?"

show lilly basic_surprised_che_close
with charachange


li "Mmh ?"


hi "Beaucoup auraient détesté leurs parents pour moins que ça."

show lilly basic_weaksmile_che_close
with charachange


li "C'est le cas de certains..."


"Ne remarquant pas mon sourcil levé, elle prend une autre gorgée de son verre. Le vin glisse le long du verre, le fait qu'elle aime le vin l'aide à gérer le goût de l'alcool. Je ne peux pas en dire autant pour moi."

show lilly basic_smile_che_close
with charachange


li "Et toi ? Comment était ton école ?"


hi "La mienne ? Eh bien..."


hi "C'était une école publique tout à fait normale, j'imagine, peut-être un peu plus animée que la normale."


hi "Je m'en sortais bien en classe et étais dans le club de foot. Vu que je suis enfant unique et que mes parents travaillaient beaucoup, j'ai passé beaucoup de temps et dépensé beaucoup d'argent dans des salles d'arcades avec mes trois amis."


hi "Peu importe le nombre de parties que j'ai pu faire, je n'ai jamais pu battre Mai à un de ces jeux. Même Takumi et Shin perdaient face à elle. Et je me retrouvais à devoir jouer le rôle de l'adulte responsable quand Shin et Mai se battaient. Encore."


hi "Juste nous quatre, appréciant simplement notre enfance. C'était de bons moments."


"Je me surprends à divaguer, les souvenirs de mes vieux jours d'école disparaissant dans les lumières de la ville et le ciel de nuit de l'autre côté de la fenêtre."


"On peut lire sur le visage de Lilly un étrange mélange de curiosité et de sympathie. Étant donné son éducation stricte et la vie qu'elle a connue, j'imagine que ce genre de chose doit être intéressante pour elle."

show lilly basic_satisfied_che_close
with charachange


li "On dirait que ton ancienne école était bien."


hi "Je ne sais pas si c'est juste par nostalgie, mais ce sont des bons souvenirs."


hi "C'est le passé dans tous les cas. Je ne peux pas y retourner, mais à travers mon accident j'ai trouvé une nouvelle vie que je n'aurais jamais imaginé avoir."


hi "La paix et le calme de Yamaku, une nouvelle direction pour mon avenir dans les sciences, mon amitié avec Shizune, Misha et Hanako, et surtout, toi."

scene ev lilly_touch_cheong
with whiteout


"Elle affiche un grand sourire sincère alors qu'elle avance sa main vers moi, ses doigts cherchant un peu mon visage avant de me caresser doucement la joue."

scene bg city_restaurant at right
show lilly basic_smileclosed_che_close:
    center
    ypos 1.1
with whiteout


"Sa main se retire après une seconde de silence, alors que nous remarquons que le serveur arrive avec nos assiettes."


"Lilly arrive tant bien que mal à masquer sa condition, sauf que son hochement de tête n'est pas très bien dirigé à cause du silence du serveur."


"Elle doit vraiment travailler dur pour avoir l'air aussi normale en public. Bien que je l'aie remarqué il y a un moment, je ne sais toujours pas si c'est par envie de ne pas être traitée différemment ou un peu de vanité. Peut-être les deux."

scene ev lilly_restaurant_eat
with shorttimeskip


"Le plat servi porte bien son nom et il est bien garni. Avec des tranches d'œufs et de la tomate, il a l'air très bon."


"Lilly prend son couteau dans une main et sa fourchette dans l'autre, s'attaquant rapidement au plat tout comme moi. Il est plus tard que l'heure habituelle à laquelle nous mangeons, donc nous avons tous les deux faim."

scene ev lilly_restaurant_chew
with locationchange


"Mes fourchetées prudentes de feuilles et de carrés ressemblant à de la viande vont de pair avec le silence de Lilly alors qu'elle mange en s'appliquant."


"Un occasionnel petit coup sur le bord du plat pour en connaître les limites est le seul signe de sa cécité."

scene bg city_restaurant at right
with locationchange


"Je finis mon repas en peu de temps, Lilly finit son assiette tandis que je reste à l'observer."

show lilly basic_smile_che_close:
    center
    ypos 1.1
with charaenter


li "Tu as fini, Hisao ?"


hi "Ouais, c'était vraiment bon."


"C'est vrai. Je n'aurais jamais pensé qu'une simple salade ait pu être si bonne et copieuse, mais encore une fois, il faut bien que l'établissement justifie son prix."

show lilly basic_smileclosed_che_close
with charachange


"Satisfaite aussi, Lilly hoche la tête."


hi "Tu sais, vu que tu es en partie étrangère et aussi belle, je suis surpris que personne ne se soit déclaré à toi auparavant."

show lilly basic_planned_che_close
with charachange


li "C'est ce que tu crois."


"Sa réponse me prend par surprise. Je ne devrais pas, vu que je viens juste de la complimenter."


hi "Vraiment ?"

show lilly basic_smile_che_close
with charachange


li "J'ai reçu plusieurs déclarations, dans cette école et dans la précédente."

show lilly basic_weaksmile_che_close
with charachange


li "L'adolescence est une drôle de période."


"Elle en parle comme si elle était déjà au-dessus de tout ça..."


hi "Huh. Tu dis ça si facilement."

show lilly basic_surprised_che_close
with charachange

with Pause(0.5)

show lilly basic_cheerful_che_close
with charachange


"Lilly semble surprise pendant un moment, mais un sourire joueur s'affiche sur son visage."


li "Est-ce de la... jalousie ?"


hi "Quoi ? Non. Pas du tout."

show lilly basic_giggle_che_close
with charachange


li "Tu mens mal, Hisao. Tu devrais en être conscient."

show lilly basic_smileclosed_che_close
with charachange


li "Encore une fois, j'apprécie ta sincérité. Même si des fois, elle n'est pas forcément voulue."


li "Je crois que ton honnêteté te servira toujours avec les autres."


"Je me racle la gorge pour montrer mon désaccord avec ce qu'elle dit et essayer de changer de sujet de conversation."


hi "Pour dire la vérité, je préfère être seul qu'entouré de gens. Je ne crois pas que je pourrais maintenir un cercle social comme tu le fais."

show lilly basic_listen_che_close
with charachange


"Elle y réfléchit un moment."

show lilly basic_smile_che_close
with charachange


li "Je ne crois pas que ce soit vrai non plus."

show lilly basic_smileclosed_che_close
with charachange


li "J'ai vu la gentillesse et l'attention que tu portes à Hanako quand tu es avec elle et tu t'entends très bien avec les autres, même ceux que tu connais à peine. Je crois que tu es plutôt à l'aise socialement."

show lilly basic_cheerful_che_close
with charachange


li "Mais sur ce sujet, qu'en est-il de toi, Hisao ? Je suis sûre que quelqu'un comme toi a au moins eu une admiratrice."


"Alors que j'ouvre la bouche pour parler, je peux sentir mon visage faire une légère grimace. C'est dans ces moments-là que j'apprécie secrètement qu'elle ne puisse pas voir mes expressions."


hi "Juste... une. Son nom était Iwanako."


hi "C'était quand elle a fait sa déclaration que j'ai eu ma crise cardiaque. C'était dans les bois, durant l'hiver."

show lilly basic_oops_che_close
with charachange


"Lilly reste sans voix, ne s'attendant pas à ce que la discussion dérive sur ce sujet."


"Ma condition l'a toujours inquiétée, alors j'essaye de minimiser cela malgré mon corps qui fait de son mieux pour prouver le contraire."


hi "Après ça, elle est venue me voir à l'hôpital pendant un moment. Pendant des semaines elle est venue et on a discuté. On parlait généralement de tout et de rien, mais c'était suffisant."


hi "Mais finalement... elle a fini par ne plus venir."


hi "Elle était là chaque jour. Puis tous les quelques jours. Puis une fois par semaine. Puis un jour, elle a fini par ne plus venir du tout."

show lilly basic_sleepy_che_close
with charachange


li "Tu... l'as revue depuis ?"


label fr_choiceL24:
menu:
    with menueffect
    "Étant encore dans mes souvenirs, je secoue la tête, avant de me rappeler que c'est inutile."
    "Mentionner la lettre.":




        return m1
    "Changer de sujet.":


        return m2




label fr_L24a:


"Je me rappelle de la seule lettre que m'a envoyée Iwanako."


hi "Je ne l'ai jamais revue, mais après que je sois arrivé à Yamaku... elle m'a envoyé une lettre."


"Lilly montre une expression que je connais bien. J'ai piqué son intérêt. Je serais légèrement offensé si ce n'était que de la curiosité pour elle. Elle n'a jamais été très douée pour masquer ses réactions."


hi "En gros, elle n'a pas dit grand-chose. Ce qui se passait en classe, comment elle s'en sortait, et, presque l'air de rien, que ça serait probablement mieux pour nous deux si on ne se voyait plus jamais."


hi "Après avoir lu la lettre, j'ai ressassé beaucoup de choses que je croyais avoir mises derrière moi. Cette lettre est un rappel pour moi que le monde continue de tourner, peu importe à quel point j'en suis isolé."


hi "Et... je crois que ça me rappelle ce que j'ai perdu."

show lilly basic_emb_che_close
with charachange


"Elle réfléchit un moment à ce que je viens de lui dire avant de réaliser quelque chose. Elle a sans aucun doute compris que c'est cette lettre qui a contribué à mon angoisse durant ce déjeuner sur le toit."


"C'est rare de voir Lilly ne sachant pas quoi dire. Aussi charismatique qu'elle puisse être, ça ne remplace pas l'expérience de vie ou de relation."

show lilly basic_reminisce_che_close
with charachange


li "Peut-être... que c'est mieux qu'elle te l'ait envoyée plutôt qu'elle ne l'ait pas fait."


hi "Comment ça ?"

show lilly basic_weaksmile_che_close
with charachange


li "Ça peut être difficile de savoir comment parler avec des gens qu'on n'a pas vus depuis longtemps. Sans compter les circonstances de votre séparation."


li "Au lieu de faire ce qui était le plus facile, elle a trouvé le courage de te parler une dernière fois, pas seulement dans son intérêt, mais aussi dans le tien."


hi "Peut-être. Je ne lui en veux pas pour ça, non pas que je lui en aie déjà voulu, mais... je sais pas."


"C'est peut-être un peu vague comme réponse, mais ce n'est pas sans raison. Je n'avais jamais regardé la situation depuis le point de vue d'Iwanako."



label fr_L24b:


"Je ne veux pas parler d'Iwanako plus que nécessaire. Ce rendez-vous est, après tout, pour Lilly et moi. Je ne veux pas penser à une précédente relation dans un moment comme celui-ci."


hi "Non, je ne l'ai plus revue après cela. On ne s'est plus jamais reparlé depuis."



label fr_L24c:


"Il y a plusieurs secondes de silence avant que Lilly ne parle."

show lilly basic_sad_che_close
with charachange


li "Déménager à Yamaku a dû être dur pour toi, perdre tous tes amis et même ta petite copine sans que ce soit de ta faute."


hi "Le pire, c'était quand j'étais à l'hôpital. Quand tout ce que tu as autour de toi sont des murs blancs et une petite télévision, ton esprit commence à te jouer des tours."


hi "C'est comme mon ancienne école. J'essaye juste de ne pas penser à ce qui s'est passé pour continuer d'avancer."


hi "Me rappeler tout cela me ralentit et c'est surtout grâce à toi que je sens que les choses commencent enfin à reprendre un cours normal."

show lilly basic_veryemb_che_close
with charachange


li "Ça... fait plaisir à entendre, Hisao."


"Elle baisse légèrement la tête, pensive. Je pense que j'ai été trop loin et que je l'ai embarrassée."


hi "J'imagine que tu es passée par quelque chose dans le même genre quand tu es arrivée à Yamaku, non ? Comme la plupart des étudiants, je pense."


hi "Tu as dit toi-même que tu t'étais fait des amis dans ton ancienne école. Je ne pense pas que beaucoup t'aient suivie."

show lilly basic_displeased_che_close
with charachange


"Le sourire de Lilly s'efface, son expression s'assombrissant. Elle retire même ses mains pour les mettre sur ses genoux."


"Après un long moment, elle ouvre la bouche."

show lilly basic_reminisce_che_close
with charachange


li "Hisao... peux-tu promettre de ne dire à personne ce que je m'apprête à—"


hi "Je te le promets."


"Elle semble légèrement surprise par mon ton sérieux, mais s'apaise et sourit faiblement avant de continuer."

show lilly basic_weaksmile_che_close
with charachange


li "Quand je suis arrivée à Yamaku, j'ai en effet regretté de perdre les amis que j'avais dans mon autre école."

show lilly basic_reminisce_che_close
with charachange


li "Mais il y a une personne en particulier que j'ai regrettée de ne plus voir. Il était la raison pour laquelle j'ai choisi l'anglais pour ma future carrière."


"“Il ?” Étant donné qu'elle vient d'une école de filles, ça ne pouvait pas être un autre élève alors..."


li "J'ai rejeté toutes les déclarations que j'ai reçues juste pour lui. Chaque fois que je m'améliorais en anglais, ses félicitations étaient la plus belle des récompenses."

show lilly basic_weaksmile_che_close
with charachange


li "C'est risible, non ? Quelqu'un comme moi, capable de se vanter d'avoir des gens qui se sont déclarés à moi, aimer quelqu'un d'aussi inatteignable qu'un tuteur."


li "C'est vraiment ridicule..."


hi "Est-ce que tu... ?"


"Elle secoue rapidement la tête de droite à gauche."

show lilly basic_displeased_che_close
with charachange


li "Je n'ai pas pu. Même à ce moment-là, je savais que c'était impossible."


"Un silence règne à notre table."


"Ça explique pourquoi elle est aussi sérieuse dans son apprentissage de l'anglais, mais je ne peux pas m'empêcher de penser à la confession qu'elle m'a faite."


"Elle l'a perdu sans même lui avouer ses sentiments... est-ce qu'elle a eu peur que cela puisse se reproduire avec moi ?"


"Je ne sais vraiment pas quoi en penser. J'ai déjà entendu parler de relations taboues comme ça, nées de la puberté et de la jeunesse. Le fait qu'elle ait eu un assez bon jugement pour ne pas agir est rassurant."

show lilly basic_emb_che_close
with charachange


li "Je sais que c'est bizarre, mais s'il te plaît... ne pense pas de moi que..."


hi "Pourquoi est-ce que je devrais en penser quelque chose de mal ?"


hi "Pour être honnête, je crois qu'il a dû être quelqu'un de vraiment bien pour que tu l'aimes autant. Pas seulement ça, mais tu t'es arrêtée avant d'aller trop loin."

with Pause(1.0)

show lilly basic_arablush_che_close
with charachange


"Pendant un moment, elle semble quelque peu perdue. Et étrangement, il ne lui faut pas une seconde pour qu'elle commence à rire. Ça me prend par surprise. Ce n'est pas un sourire, ou même un petit rire étouffé, mais un véritable rire."


"Je me retrouve à sourire, pas seulement parce qu'elle semble contente, mais aussi parce qu'elle me fait assez confiance pour me laisser connaître ses secrets les plus intimes."

scene ev lilly_touch_cheong
with whiteout


"Avant que je ne le réalise, je sens sa main me toucher le visage. Son toucher est aussi gentil que d'habitude et son pouce me caresse doucement la joue."


li "Tu es gentil, Hisao. Je t'aime vraiment."


"La voir comme ça, avec sa main me caressant le visage... Je crois que ce fut une magnifique soirée."


hi "On a tous les deux un passé assez bizarre, hein ?"


li "Je crois que d'un point de vue général, notre présent est assez étrange aussi."


"Je souris. Cette femme a vraiment le moyen de me faire tourner en bourrique, ça c'est sûr."

scene bg city_restaurant at right
with whiteout


"Je regarde autour de moi, la pièce vrombissant toujours des discussions des clients."


hi "Cet endroit rentre probablement dans la catégorie “étrange”, aussi."

show lilly basic_weaksmile_che_close:
    center
    ypos 1.1
with charaenter


li "C'est un peu... arrogant."


hi "C'est un mot pour le décrire, oui."


"Je regarde le serveur parcourant la salle, un petit gars maigre pas plus vieux que la vingtaine. Il me rappelle un peu Kenji, bien que contrairement à lui, le serveur ne soit pas habillé pour l'hiver durant l'été."

show lilly basic_smileclosed_che_close
with charachange


"Après s'être penché, il nous propose de prendre nos plats, Lilly demande l'addition poliment."


"Avec une coordination experte, il manœuvre entre les tables, nos plats en main, pour aller chercher notre addition."


"Il réapparaît en un rien de temps, tendant intelligemment l'addition à Lilly."

show lilly basic_smile_che_close
with charachange


"...qui me la tend directement, ce qui l'interloque."


"Lisant le petit ticket imprimé, le prix est bien plus élevé que ce que j'aurais cru."

show lilly basic_surprised_che_close
with charachange


li "Hisao ?"


hi "Oh... euh..."

show lilly basic_smileclosed_che_close
with charachange


"Je balbutie rapidement le montant, Lilly hoche la tête et attrape son sac à main."


"Elle donne sa carte au serveur qui disparaît encore une fois."


hi "C'était... un très gros montant."

show lilly basic_emb_che_close
with charachange


"Mon commentaire semble mettre Lilly légèrement mal à l'aise."

show lilly basic_weaksmile_che_close
with charachange


li "Ma famille me donne plus que ce dont j'ai besoin pour mon éducation. La même chose vaut pour ma sœur, bien qu'elle n'aime pas se le faire rappeler."

show lilly behind_cheerful_che_close
with charachange


li "Cela dit, je n'apprécie pas non plus de jeter l'argent par les fenêtres. Mais cette fois je crois que je vais faire une exception. Juste pour toi."


hi "Non seulement tu as choisi le lieu de notre rendez-vous, mais tu as aussi payé pour nous deux..."


"Je me frotte le front, en signe de réflexion."


hi "Je ne peux pas croire que tu aies mis la barre si haute pour notre prochain rendez-vous."

show lilly basic_giggle_che_close
with charachange


"Elle émet un petit rire."

show lilly basic_smileclosed_che_close
with charachange


li "J'attendrai ça avec impatience, Hisao."


"Le serveur réapparaît comme par magie et rend à Lilly sa carte. Ayant remarqué qu'elle est aveugle, il place la carte dans sa main, presque exagérément, pour être sûr qu'elle la tienne."


"En partant, il reste diplomate en gardant un visage neutre malgré ma propre expression."


"Claquant des mains, je me lève, histoire de mettre fin à notre soirée."


hi "Et si nous y allions, ma chère ?"

stop music fadeout 2.0

scene black
with dissolve




label fr_L25:

scene black
with Dissolve(2.0)

scene bg school_dormhisao_ni
with vpunch


hi "Gyah !"


"Je repousse rapidement les draps et me redresse d'un coup sur le lit, comme si un choc électrique avait parcouru mon corps."


"L'air frais de la nuit me fait frissonner alors qu'il se confronte à la transpiration sur ma peau nue, ma respiration est courte, à la limite de l'hyperventilation."


"L'esprit embrouillé, je mets la main sur mon front dans une tentative d'apaiser l'état de panique de mon corps. Il me faut quelques secondes pour réaliser que ma main tremble violemment, même alors que je la tiens sur ma tête."


"D'autres secondes passent dans un silence complet, ma tentative désespérée de reprendre le contrôle de mon corps et de mon esprit marchant lentement."


"Me ressaisissant, je commence à prendre conscience de l'état dans lequel je suis. Je me sens comme si j'avais couru un marathon, chaque muscle de mon corps est tendu et je transpire à grosses gouttes."


"Je fais particulièrement attention aux battements de mon cœur. Cela dit, mon cœur, peu fiable, marche bien pour une fois."


"Mais... c'était quoi ça ?"


"Une crise cardiaque ? Un mauvais cauchemar ? Un effet secondaire des médicaments ? J'ai entendu parler des crises d'angoisse, et vu les caractéristiques, cela semble en être une..."


"Je ne m'embête même pas à penser à cela maintenant. Après cette expérience, je me sens épuisé et pourtant complètement éveillé."


"Je regarde de l'autre côté du lit, sa peau pâle alors qu'elle dort brille presque dans l'obscurité de la chambre. Juste la voir est suffisant pour me calmer."

scene ev lilly_sleeping_smile:
    truecenter
    zoom 1.0 subpixel True
    acdc_warp 20.0 zoom 1.05
with locationchange


"Elle reste gracieuse même quand elle dort, sa respiration parfaitement régulière et son visage neutre rendent impossible de savoir si elle est éveillée ou endormie."


"Succombant à la tentation, je passe mes doigts le long de sa main. Sa peau est douce au toucher, comme elle l'a toujours été, et pourtant chaude malgré la fraîcheur de la nuit."


"C'est dans des moments comme ça, appréciant silencieusement la présence de l'autre, que je ressens le plus qu'on est proches."


"Mes doigts s'arrêtent sur son poignet et je repose ma main sur le lit."


"Je ne sais pas vraiment pourquoi, mais alors que nous devenions plus proches, je sentais que quelque chose grandissait entre nous. Je ne suis pas vraiment sûr de ce que c'est, ni si ça existait avant que nous tombions amoureux."


"Tout va si vite. Ça ne me gêne pas, mais ça ne ressemble pas à Lilly de presser les choses à ce point."

scene bg school_dormhallway
with shorttimeskip

play music music_dreamy fadein 2.0


"Heureusement, il n'y a pas beaucoup d'étudiants dans les couloirs à cette heure-ci de la matinée, au cas où on me demanderait pourquoi j'amène deux plats pour le petit déjeuner dans ma chambre en ayant mis mon uniforme n'importe comment."


"Ce n'est pas comme si ce genre de choses n'arrivaient jamais, bien sûr. Un seul garde patrouillant entre les deux dortoirs situés l'un en face de l'autre représente une très petite armée en comparaison des hormones adolescentes."


"En y pensant, le fait qu'on soit lundi aide sûrement. Je ne sais pas vraiment pourquoi, mais les lundis semblent me perturber moins que les autres jours."


"Il m'aura fallu un peu de créativité avec ma main et mon coude, mais finalement j'arrive à ouvrir la porte de ma chambre."

scene bg school_dormhisao
show lilly basic_sleepy_paj at center
with locationchange


"En rentrant, je vois Lilly se tenant debout à côté du lit, se frottant les yeux. Elle a l'air dans le brouillard, comme toutes les fois où je l'ai vue quand elle se lève. Elle n'est vraiment pas du matin."


hi "Désolé, je ne voulais pas te réveiller."

show lilly basic_displeased_paj
with charachange


"Elle secoue difficilement la tête. Le soleil du matin l'illuminant la rend très belle à voir."


show lilly basic_weaksmile_paj
with charachange


li "C'est bon, je devais me lever de toute façon. Quelle heure est-il ?"


"Je pose mon plat sur le bureau et tourne l'horloge pour voir l'heure."


hi "Toujours tôt. Ne t'inquiète pas, on a encore le temps avant les cours."

show lilly basic_smileclosed_paj:
    ypos 1.2
with dissolvecharamove


"Elle s'assoit sur le côté du lit et commence à humer l'air. Pendant qu'elle fait cela, je pousse le plat plus loin sur le bureau."


hi "Oui, je nous ai pris un petit déjeuner. Douche d'abord, cela dit."

scene ev lilly_kissing
with flash


"Elle se tient immobile un moment avec le menton légèrement vers l'avant. J'acquiesce joyeusement et presse mes lèvres contre les siennes, savourant la douce sensation avant de me retirer."

scene bg school_dormhisao
with locationchange


"Avec un petit, doux sourire, apparemment satisfaite, elle se dirige lentement vers les douches."


"Je m'étire pour essayer de me réveiller un peu plus, regardant brièvement les plats fumants sur mon bureau. Riz, poisson, soupe miso et des légumes, un petit déjeuner standard pour un jour pas ordinaire."


"J'attrape mes flacons et commence à avaler le régiment journalier de pilules."

show pills:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)


"Quelquefois je me demande à quoi servent ces trucs, étant donné tous les problèmes que j'ai eus depuis mon accident initial. Je ne peux même pas dire que ça ne me fait pas de mal de les prendre, vu tous les effets secondaires."


"Bah, peu importe. Le docteur m'a dit qu'il faut les prendre et je crois que je ferais mieux de croire son jugement plutôt que le mien."

show pills:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide pills
with None


"Il ne faut pas longtemps avant que le bruit de la douche ne cesse. Étant donné les circonstances, une douche rapide semble convenir à Lilly."

show lilly basic_smile_paj:
    center
    xpos 0.55
    easein 0.5 xpos 0.5
with charaenter


"Sortant de la salle de bain, elle a l'air beaucoup plus réveillée."

show lilly basic_smile_paj_close at center
with characlose

show lilly basic_smileclosed_paj_close:
    ypos 1.1
with dissolvecharamove


"Sans un mot, je lui prends la main et la guide jusqu'à mon bureau. Vu que je n'ai pas une table comme elle dans ma chambre, cela devra faire l'affaire."


li "Merci, Hisao. Qu'est-ce que tu as fait pour le petit déjeuner ?"


hi "Juste du riz et des légumes. Quelque chose de rapide."

show lilly basic_ara_paj_close
with charachange


"Son visage s'illumine alors que je dis cela."

show lilly basic_satisfied_paj_close
with charachange


li "C'est certainement un bon petit déjeuner. Tu manges comme ça d'habitude ?"


"Elle est juste gentille. J'ai un léger doute, vu son passé, que ce ne soit pas un grand petit déjeuner selon ses standards."


hi "Le petit déjeuner est le repas le plus important de la journée. On ne doit pas le négliger, même si on est juste étudiants."


"C'est ce que je crois du moins. D'après ce qu'en disent les autres, je dois faire partie d'une minorité."

show lilly basic_smileclosed_paj_close
with charachange


"Je m'assois sur le côté du lit et commence à manger avec Lilly, ses baguettes tapant sur le côté du bol de légumes comme je l'ai remarqué durant notre rendez-vous."

show lilly basic_smile_paj_close
with charachange


li "C'est vraiment bon, Hisao. Je ne savais pas que tu cuisinais si bien."


"Cette fois elle le pense vraiment, je peux le dire. Cela dit, cuisiner n'est vraiment pas ma spécialité. Après un peu de pratique, il est facile de faire quelque chose comme ça."


hi "Tout le mérite revient à la technologie moderne ; cela dit, cela fait des années que je me fais à manger, c'est normal que je sache faire ça."


hi "J'en ai eu marre des nouilles instantanées ou de commander des pizzas à chaque fois que mes parents travaillaient, alors j'ai appris à faire quelques trucs. Mais j'ai encore du mal avec certains plats, quand même."


show lilly basic_cheerful_paj_close
with charachange


li "Tu feras une bonne épouse un jour, Hisao."


"Je prends un grain de riz et le place sur mon pouce, avant de viser avec attention et de donner une bonne pichenette dessus."

show lilly basic_surprised_paj_close
with vpunch


"Lilly sursaute un peu alors qu'il atteint sa joue, en plein dans le mille."

show lilly basic_pout_paj_close
with charachange


"Je ne peux pas m'empêcher de rire un peu à ses dépens alors qu'elle fronce les sourcils et fait de son mieux pour prendre une expression sérieuse."

show lilly basic_sleepy_paj_close
with charachange


li "Oh, c'est vrai..."


hi "Qu'est-ce qu'il y a ?"

show lilly basic_concerned_paj_close
with charachange

$ renpy.music.set_volume(0.5, 1.0, channel="music")


li "Tu as eu du mal à dormir la nuit dernière ? Tu bougeais beaucoup."


"Donc elle était réveillée, ou du moins partiellement. Que ce soit mon cœur ou un cauchemar causé par les effets secondaires de mes médicaments, la dernière chose que je veux, c'est qu'elle s'inquiète pour moi."


"Avant même que je connaisse Lilly, je sentais que mon corps me ralentissait dans tout ce que je faisais. Mon corps est mon fardeau à moi seul, et aussi longtemps que je serai avec elle, je ferai de mon mieux pour agir normalement."


hi "Non, pas particulièrement."

show lilly basic_reminisce_paj_close
with charachange


li "D'accord... ça va alors."

$ renpy.music.set_volume(1.0, 4.0, channel="music")


"Heureusement, elle semble me croire."

show lilly basic_weaksmile_paj_close
with charachange


li "En y pensant, il y a quelque chose d'autre que je voulais te demander."


hi "Oh ?"

show lilly basic_smileclosed_paj_close
with charachange


li "Comment est-ce que je pourrais dire ça..."

show lilly basic_smile_paj_close
with charachange


li "Quand tu rêves... est-ce que tu vois des gens et des objets ?"


hi "Oui, bien sûr je... oh."


"Je me sens un peu bête d'avoir dit ça, même si c'est vrai. Lilly ne semble pas s'en préoccuper cela dit."

show lilly basic_smileclosed_paj_close
with charachange


li "Mais tu n'as pas la sensation du goût, du toucher ou de l'odorat ?"


"Je m'apprête à lui répondre, mais me retrouve à ne pas savoir quoi dire. Plus j'y pense, et plus je me rends compte que ce qu'elle dit est vrai."


hi "C'est... vrai. Je crois. Je n'y ai jamais pensé. Tu peux toi ?"

show lilly basic_smile_paj_close
with charachange


li "Généralement j'entends juste dans mes rêves, mais oui, des fois je touche et sens les choses aussi."

show lilly basic_planned_paj_close
with charachange


li "Je te demande, parce qu'Akira a trouvé ça bizarre quand je lui ai dit. Si tu n'as aucune de ces sensations non plus, alors c'est sûrement parce que je suis aveugle."


hi "Ça serait logique. Tu comptes plus sur tes autres sens que moi, alors peut-être que ça affecte aussi tes rêves."


"Les mystères du corps humain, j'imagine."


"Pendant le temps restant avant d'aller en cours, nous mangeons silencieusement le petit déjeuner en face de nous, discutant un peu."

stop music fadeout 2.0

scene bg school_dormext_full
with shorttimeskip


"Je regarde rapidement derrière la porte pour voir s'il n'y a personne à l'entrée du dortoir des garçons, que nous puissions sortir sans problème."

play music music_soothing fadein 4.0


hi "Il fait beau ce matin."


"Je m'étire alors que Lilly et moi mettons un pied dehors, le soleil du matin nous éclairant."


"Il y a quelques autres étudiants qui font la même chose, faisant leur chemin jusqu'au bâtiment principal depuis les dortoirs ou le portail principal."

show lilly cane_smile_close at center
with charaenter


li "C'est vrai qu'il fait bon."


"Nous tenant la main et sa canne tapant sur le sol, nous commençons notre marche jusqu'à l'école et rejoignons les troupes d'étudiants discutant autour de nous."

show lilly cane_smileclosed_close
with charachange


li "C'est le dernier jour des examens, non ?"


hi "Ouais. Tu t'en sors comment, toi ?"

show lilly cane_concerned_close
with charachange


li "Assez bien, en y repensant. Tu sembles un peu stressé, cela dit."


hi "Ça se voit autant que ça ?"


hi "Je ne crois pas que ce soit juste les examens cela dit. Beaucoup de choses sont arrivées en peu de temps et je ne m'en sors pas très bien en sciences humaines."

show lilly cane_smileclosed_close
with charachange


li "Tu t'en sors mieux dans les matières scientifiques, non ?"


hi "Bah, ce serait dur pour moi si je ne m'en sortais pas au moins là. En y pensant, tu n'as pas déjà dit que tu n'étais pas très bonne en sciences et en maths ?"
show lilly cane_oops_close
with charachange


"Elle prend une expression un peu gênée, ma remarque ayant sans aucun doute du vrai. La fierté de Lilly est vraiment à double tranchant."

show lilly cane_smile_close
with charachange


li "Bon, mis à part ça... tu as déjà pensé à ce que tu feras de tes capacités dans le domaine ? Ça serait dommage de les gâcher."


hi "Un peu, surtout à cause de Mutou."


hi "Dans tous les cas, je finirai probablement par faire carrière là-dedans."

show lilly cane_smileclosed_close
with charachange


li "Ça fait plaisir à entrendre, Hisao."

scene bg school_gardens at bgleft
with locationchange

stop music fadeout 0.3
with vpunch


"Alors que nous entrons dans les jardins, je reçois soudainement une tape dans le dos dont je me serais bien passé."


"Le coupable habillé de vert se place à côté de moi, ne prêtant apparemment aucune attention à Lilly qui est à mes côtés."

play music music_kenji fadein 0.5

show kenji neutral:
    center
    xpos 0.55
    easein 0.5 center
with charaenter


ke "Salut mec, quoi de neuf ? Ça fait longtemps que je t'ai pas vu."


hi "Salut. J'ai juste été occupé avec les examens et tout."

show kenji tsun at center
with charachange


ke "Examens, ekchamens. Un vrai homme de la Renaissance n'a pas besoin d'étudier pour exceller dans de telles choses."


"Kenji me dit cela comme s'il était le genre de personne à bien s'en sortir en cours. Il a beaucoup d'absences et ne travaille pas vraiment, donc j'ai des raisons de douter de ses capacités."


"Pour être honnête, je suis un peu envieux. Entre les examens et mon temps avec Lilly, je n'ai presque aucun moment pour moi. Peut-être que Yuuko ressent la même chose."

show kenji tsun at tworight
show bg school_gardens at center
with charamove

show lilly cane_smile_close at twoleft
with charaenter


li "Bonjour Setou. Contente d'entendre que tu t'en sors bien."


"Cela fait un peu bizarre d'entendre lilly parler de manière si formelle. Elle me parle de manière de plus en plus détendue au fil des mois, bien que je l'ai déjà entendue parler plus familièrement avec ses camarades de classe aussi."


"Certaines personnes ne changent jamais, j'imagine. Pas que je pense que son côté poli et calme soit une mauvaise chose, c'est une des raisons pour lesquelles j'aime être avec elle, après tout."


"Kenji semble mettre un moment pour comprendre qui est à côté de moi, n'ayant probablement pas remarqué que nous nous tenions la main. Je me demande si ses lunettes servent à quelque chose."

show kenji neutral at tworight
with charachange


ke "Oh, salut Lilly. Bonne chance pour les examens, aussi."

show kenji tsun at tworight
with charachange


ke "Je te vois après les cours alors, mec."


"Le côté tranchant de sa voix me fait penser que ses mots impliquent plus quelque chose d'obligatoire plutôt qu'un simple au revoir. J'imagine que je vais devoir gérer ça plus tard."


hi "Ok. À plus."



show kenji invis:
    xpos 0.6
with dissolvecharamove

hide kenji
with None


"Kenji hoche la tête sèchement. Il avance pour nous dépasser, mais est trop occupé à regarder en direction de Lilly pour remarquer sa canne."

show lilly cane_surprised_close at twoleft
with charachange


"Avant que je ne puisse réagir et éviter le drame, Kenji trébuche et attrape par réflexe ce qui est à portée de main, ce qui se trouve être, malheureusement, le bras de Lilly."

show lilly cane_surprised_close:
    easeout 0.3 ypos 1.2 alpha 0.0
with Pause(0.5)

play sound sfx_pillow
hide lilly
with vpunch


$ doublespeak(ke,li,"Whoa !", "Ah !")


"Ils tombent tous les deux au sol alors que je me sens tout à fait inutile."


hi "Ah, zut. Vous allez bien ?"

show kenji invis:
    center
    ypos 1.2
with None

show kenji neutral:
    ypos 1.0
with dissolvecharamove


"Kenji se relève vite, semblant indemne de l'accident."


ke "Pas de problème, mec, pas de problème. C'est rien, mon corps peut encaisser bien plus que ça."


"Lilly est à plat ventre sur l'herbe. Elle n'a pas l'air de s'être fait mal, plus surprise qu'autre chose. Je m'approche pour lui offrir mon aide."


hi "Tu vas bien, Lilly ?"

show kenji happy
with charachange


ke "Hé, Satou ?"


"Kenji lui tend la main, la touchant un peu pour lui faire comprendre ce qu'il fait."


"Il dit des choses odieuses parfois, mais je pense que c'est vraiment un mec bien dans le fond. Je crois qu'il se sent mal pour ce qui vient d'arriver."

stop music fadeout 2.0


"À sa grande surprise et à la mienne, Lilly frappe du poing sur le sol."

play sound sfx_impact
with vpunch


li "Merde !"

show kenji tsun
with charachange


"Kenji s'arrête sur place, pris par surprise par sa réaction. Je suis tout aussi choqué, elle n'a jamais agi comme ça, même pas avec Shizune."


ke "Euh..."

show lilly invis_close:
    twoleft
    ypos 1.2
with None
show lilly cane_mad_close at twoleft

with dissolvecharamove


"Ne semblant se rappeler que maintenant qu'il y a des gens autour d'elle, Lilly se remet lentement sur ses pieds. L'expression qu'elle a à ce moment-là me fait reculer un peu."

show lilly back_listen_close
show lillyprop back_cane_close at twoleft
with charachange


"Je ne vois qu'un peu son visage avant qu'elle ne se tourne, mais ce n'est pas quelque chose que j'oublierai de sitôt."


"Je l'ai déjà vue énervée avec Shizune, mais cet éclair de rage, c'était quelque chose d'autre. C'est clairement pas juste à cause de ce petit incident."

hide lilly
hide lillyprop
with charaexit


"Elle reste figée pendant un moment avant de soupirer et de recommencer à marcher. Je ne sais vraiment pas quoi faire."


hi "Je vais, euh... je te parlerai plus tard, mec. À plus."


ke "Ouais, à plus."

hide kenji
with charaexit


"Kenji se gratte la tête pour essayer de trouver quelque chose à dire, puis hausse les épaules et marche plus loin, s'éloignant de nous."

show bg school_gardens at right
with charamove

show lilly back_listen at center
show lillyprop back_cane at center
with charaenter


"Je rattrape rapidement Lilly. Elle tourne légèrement la tête pour confirmer qu'elle sait que je suis là, mais ne fait rien d'autre."


"Je devrais sûrement la réprimander pour avoir réagi comme ça, mais je ne veux pas commencer une dispute avec elle. Elle est toujours apparemment énervée."


"En fin de compte, je ne dis rien et attends qu'elle se calme."

scene bg school_hallway3
with shorttimeskip


"Après une marche silencieuse, nous arrivons enfin au troisième étage, là où nous nous séparons chaque jour."

show lilly cane_listen_close at center
with charaenter


"Je me tourne vers Lilly avant qu'elle ne parte. Bien que j'aime les silences chaleureux que nous partageons souvent, ce n'en était pas un. Je ne veux pas laisser les choses comme ça."


hi "Tu sembles... plus silencieuse que d'habitude. Quelque chose ne va pas ?"

show lilly cane_displeased_close
with charachange


"Elle secoue la tête presque automatiquement, comme pour éviter à tout prix que je m'inquiète pour elle."


li "C'est juste les examens qui font leur effet. Je vais bien."


"Je ne crois pas que ce soit la raison. Je suis sur le point de le dire, mais je me ravise. Je n'ai aucun intérêt à la forcer si elle ne veut pas me le dire, surtout quand elle est de mauvaise humeur."


hi "D'accord alors. À ce midi."

hide lilly
with charaexit


"Alors que je me tourne pour aller en direction de ma classe, la douce voix de Lilly résonne derrière moi."

show lilly cane_concerned
with charaenter


li "Hisao, euh..."


hi "Ouais ?"

li "…"


li "Je suis désolée."

hide lilly
with charaexit




"Sur ce, Lilly part dans l'autre sens en direction de sa classe, sa main glissant le long des rampes en métal."


"Je me tiens là à la regarder jusqu'à ce qu'elle rentre dans sa classe, avant de partir vers la mienne avec une légère réticence."

scene bg school_scienceroom at left
with locationchange

play music music_normal fadein 4.0


"Comme d'habitude, je suis en avance. Mutou est en train de se battre avec des piles de dossiers et de papiers sur son bureau en préparant la journée, pendant qu'un petit groupe d'étudiants discutent."


"Bien que je pense toujours à Lilly, le fait qu'elle ait mentionné les examens me rappelle que j'ai encore des questions sans réponses."


"Après y avoir pensé, j'ai simplement réalisé que je voulais vraiment poursuivre en sciences pour ma carrière, plutôt que de les prendre par défaut."


"Jusqu'à maintenant, je ne ne savais pas du tout dans quoi je voulais travailler. La “science” est un domaine plutôt vaste."


"Ce que Lilly a dit plus tôt m'a permis de revoir les choses à ce sujet. Je n'avais que brièvement envisagé cela auparavant, sans le considérer comme une éventualité sérieuse."

show bg school_scienceroom at right
with charamove


"Je marche jusqu'au bureau de Mutou, trop concentré sur sa préparation des cours pour remarquer mon approche. C'est pareil tous les jours."


hi "Bonjour."

show muto normal at center
with charaenter


"Il lève la tête avec une expression de légère surprise qui est rapidement remplacée par son typique sourire bizarre."

show muto smile
with charachange


mu "Bonjour, Nakai. Est-ce que je peux t'aider ?"


hi "Je peux vous demander quelque chose ?"


"Il baisse les yeux vers son fouillis sur le bureau, avant de poser les feuilles qu'il a dans les mains et de se lever avec quelques difficultés pour s'adresser à moi."


mu "Je suis là pour ça, après tout. Demande donc."


hi "Je me demandais juste... pourquoi vous avez choisi d'enseigner ?"


"Il réfléchit pendant quelques instants avant de répondre, n'ayant apparemment pas de réponse toute prête."

show muto normal
with charachange


mu "Si tu posais la question à dix professeurs différents, tu aurais toujours dix réponses différentes à cette question."


mu "Bien que je ne puisse parler que pour moi, je dirais que j'enseigne parce que... mmh..."


"Il repart dans ses pensées une fois de plus, réfléchissant à comment exprimer ce qu'il veut dire."

show muto smile
with charachange


mu "Penses-y de cette façon, quand tu étais un enfant, tu t'es déjà amusé à jeter des cailloux dans l'eau des caniveaux ou des flaques, non ?"


hi "Ouais, je crois que beaucoup de gens font ça quand ils sont petits."

show muto normal
with charachange


mu "Eh bien, certaines personnes continuent de le faire quand elles sont grandes, de manière figurative. Là où je veux en venir, c'est que quand quelqu'un fait cela, c'est par curiosité, pour voir comment l'eau va bouger ou changer."


mu "Tout le monde, même à un jeune âge, est émerveillé de voir comment le monde marche, même dans ses petits détails."


mu "Je ressens toujours cette fascination pour l'univers. Même juste lire des choses à propos de nouvelles découvertes ou d'expériences classiques me rappelle à quel point tout est extraordinaire, des étoiles jusqu'au petit caillou."

show muto smile
with charachange


mu "J'espère juste que je peux transmettre un peu de cet émerveillement aux autres. Si je peux faire ça, même si ce n'est qu'à une seule personne, je crois que je peux être heureux en tant que professeur."


"Il se gratte la tête comme s'il réfléchissait à ce qu'il venait de dire."


"J'ai l'impression de mieux le comprendre maintenant. Même s'il est bizarre avec les autres, il a une véritable envie d'être avec eux et de leur offrir un peu de ce qu'il estime important."


"Ce que Lilly m'a dit résonne dans ma tête. “Je crois que tu t'entends très bien avec les autres”, hein. Elle a toujours dit que j'étais très curieux..."

show muto normal
with charachange


mu "Désolé si je n'ai pas été très clair. Est-ce que cela répond à ta question ?"


hi "Oui, merci."


hi "J'en ai une autre, en fait."


mu "Oh ? Et quelle est-elle ?"


hi "Hum... Vous avez des brochures ou des guides pour l'université ? Il est temps que je commence à m'intéresser à cela."


"Il hoche la tête et se penche pour regarder dans son bureau. Pendant qu'il regarde, je remarque qu'il affiche un vrai sourire. Je ne crois pas que je l'avais déjà vu sourire naturellement auparavant."


"Peut-être que ce n'est pas Mutou l'enseignant, mais Mutou la personne."

show muto smile
with charachange


mu "Tiens, si tu as besoin de plus, demande-moi."


"Il me tend une demi-douzaine de brochures et de livrets de diverses couleurs et tailles, que je prends avec enthousiasme."


"Oui, c'est avec cette information que je vais forger mon propre avenir. Je crois que maintenant, après tout ce temps et ces épreuves, je peux enfin commencer à voir mon futur se profiler devant moi."


"Mon corps est peut-être comme il est, mais mon esprit est toujours fiable."


hi "Merci."

stop music fadeout 2.0

scene black
with dissolve

$ suppress_window_after_timeskip = True



label fr_L26:

window hide None

scene black
with dissolve

nvl clear
nvl show dissolve


n "\n\n“C'est étrange.”"

play music music_pearly fadein 5.0

$ ksgallery_unlock("evul hisao_teacup")
show ev hisao_teacup:
    truecenter
    alpha 0.0 subpixel True
    linear 30.0 alpha 0.5
with None


n "\n\nCette pensée m'a traversé l'esprit de nombreuses fois depuis que ma vie a commencé ici."


n "Ça paraît être une façon facile d'éviter une question gênante, comme si le simple étiquetage de quelque chose avec ces trois mots le faisait disparaître, ou au moins rendait inutile le fait d'y réfléchir davantage."


n "Ma vie avant ma crise cardiaque m'apparaît vraiment floue à chaque fois que j'essaye de m'en rappeler, et mon esprit se bat pour faire face à tout ce qui m'est arrivé depuis."


n "J'ai entendu quelque part que c'est ce que l'on ressent lorsqu'on échoue dans un pays dont on ne comprend que très basiquement la langue."


n "Quand j'y pense, c'est une très belle analogie de ce qui m'arrive."

nvl clear


n "\n\nMais de telles situations sont aussi censées t'aider à comprendre très rapidement la langue, parce que tu es forcé de l'apprendre pour survivre. Dit d'une autre façon, c'est un peu “marche ou crève.”"


n "\nJe me demande si, après tout ce temps, j'ai vraiment réussi à marcher."


n "Les examens m'ont beaucoup stressé, même s'ils arrivent à leur fin, mais je suis resté dans les bonnes grâces de Mutou et j'ai plus ou moins une direction pour mon avenir maintenant."


n "Mais je continue d'utiliser cette stupide phrase."


n "\n\n“C'est étrange.”"

nvl clear


n "\n\nIl est impresionnant de voir à quelle vitesse quelqu'un peut s'adapter à un entourage de personnes avec des handicaps parfois troublants."


n "Tellement que je me demande vraiment pourquoi j'ai autant l'impression d'être un étranger."


n "\nCe n'est sûrement pas parce que je ne socialise pas assez. J'en suis venu à appeler par leur prénom la plupart de mes camarades de classe ainsi que quelques autres étudiants dans l'école. Qu'il leur manque un bras ou une jambe, les étudiants ici sont comme n'importe quelle personne de leur âge."


n "\n\nJe peux parcourir les couloirs dans lesquels je me suis déjà perdu avec une facilité que je ne m'attendais pas à avoir, merci à l'aménagement logique des bâtiments, et je peux même engager une discussion avec mes professeurs."

nvl clear
nvl hide dissolve

scene ev hisao_teacup:
    truecenter
    zoom 1.0 subpixel True alpha 1.0
    acdc_warp 20.0 zoom 0.8
with locationchange

window show


"Je remue doucement le thé dans ma tasse, mon reflet se retrouvant tordu par le liquide en mouvement."


"C'est si étrange... Avant, je détestais boire du thé."


hi "Peut-être que je réfléchis trop."

play sound sfx_teacup


"J'entends le son familier que fait la porcelaine de Chine d'une tasse à thé touchant sa coupelle."


li "Quelque chose ne va pas ?"


hi "Ne t'inquiète pas, ce n'est rien."

scene bg school_dormlilly
show hanagown normal:
    tworight
    ypos 1.15
show lilly basic_smileclosed_paj:
    twoleft
    ypos 1.2
with whiteout


"Je prends une grande gorgée de thé en même temps que les filles."


"Juste passer mon temps avec Lilly et Hanako dans cette pièce, à boire du thé. Cela me semble si familier que c'en est presque nostalgique."


hi "Donc comment se passe ton travail dans le club journal, Hanako ?"

show lilly basic_satisfied_paj
with charachange


li "Je veux savoir aussi, ça a l'air d'être intéressant."

show hanagown distant
with charachange


"Hanako penche un peu la tête à cause de l'attention qu'elle attire, bien que son sourire trahisse le fait qu'elle aime bien être le centre d'attention quand il ne s'agit que de nous deux."


ha "C'est... bien. Je crois que je m'améliore."


ha "Naomi et quelques-unes de ses amies font la plupart du travail... obtenir les histoires et le reste."

show hanagown smile
with charachange


ha "Je m'occupe juste des trucs d'ordinateur, comme mettre les histoires ensemble et les imprimer. C-c'est bien, je peux m'asseoir et me concentrer."


"Je vois que la technophobie de Lilly ne touche pas Hanako. Bien qu'être dans une pièce à rassembler les histoires des autres pour en faire un document ne me semble pas très extraverti, ça fait plaisir de voir qu'elle élargit son cercle d'amis."


"C'est un petit pas, j'imagine. C'est un peu trop espérer de vouloir qu'elle devienne sociale comme Lilly."

show lilly basic_oops_paj
with charachange


li "Comment tu trouves Naomi ? J'ai entendu dire qu'elle pouvait être fauteuse de trouble à des moments."


"Lilly est vraiment maternelle avec Hanako. Elle va devoir apprendre à la laisser partir."

show hanagown worry
with charachange


"Hanako se gratte la joue d'un doigt, pensant à sa réponse."

show hanagown smile
with charachange


ha "Naomi est... gentille. Elle est un peu bruyante des fois et peut-être un peu épuisante... mais elle aide beaucoup. Ses amies sont gentilles, aussi."

show lilly basic_cheerful_paj
with charachange


li "Je suis contente d'entendre ça, Hanako. C'est bien que tu aies trouvé quelque chose qui t'intéresse."


"Le sourire de Lilly est chaleureux et honnête, mais je peux sentir une pointe de mélancolie aussi. Hanako ne semble pas le remarquer, mais je ne pense pas que ce soit mon imagination."


"J'imagine que c'est parce que j'ai lentement commencé à faire plus attention à ce qui m'entoure. Les choses semblant aller de plus en plus vite, j'ai l'impression que si je ne fais pas attention, je vais louper quelque chose."


"Entre les examens, ma nouvelle vie amoureuse, mon orientation pour l'université, sans oublier ma condition cardiaque me freinant dans tout ce que je fais de manière aléatoire, mon cerveau surchauffait un peu récemment."


"Cela me fait apprécier les rares moments calmes comme celui-ci."


"Ça doit être pour ça que Lilly est venue à apprécier les marches hebdomadaires jusqu'a la supérette et boire du thé avec Hanako, même si elle est souvent entourée d'autres personnes ; ces moments lui donnent un instant de paix."


hi "Ça fait du bien que les examens soient finis, hein ?"

show lilly basic_giggle_paj
with charachange



"Cette question fait rire Hanako et Lilly. Tout le monde semble être de bien meilleure humeur depuis que les examens ont fini la semaine dernière."


hi "Donc qu'est-ce que tu fais pour les vacances d'été, Hanako ? Il ne reste que..."


"Je compte rapidement dans ma tête. On est lundi et l'école finit samedi..."


hi "...cinq jours, après tout."

show hanagown normal
with charachange


ha "Je pensais... voyager. Juste... un peu."

show hanagown smile
with charachange


ha "Il y a beaucoup d'endroits que je veux voir et... je crois que j'ai assez d'argent pour payer le bus et les voyages en train. Naomi et une des autres filles du club ont dit qu'elles viendraient aussi."


"Son expression indique qu'elle y a beaucoup pensé. Je suis surpris qu'elle prévoie de faire des choses comme ça."


"Il semblerait qu'elle devienne vraiment autonome."

show lilly basic_smile_paj
with charachange


li "Il y a quelque part en particulier où tu penses aller ?"

show hanagown distant_blush
with charachange


ha "Je pense que... Kyôto serait bien. J-je crois que je vais essayer quelques autres endroits... aussi."

show lilly basic_cheerful_paj
with charachange


"Lilly hoche la tête, approuvant joyeusement les plans de Hanako."


"Alors que je regarde Lilly, je m'empêche de lui poser la même question. Depuis un moment, elle est évasive sur ce qu'elle compte faire, mais je n'ai jamais eu de bonne occasion de lui en parler seul à seul."


"À chaque fois que cela arrive dans la conversation, on dirait qu'elle ne sait pas ou qu'elle évite simplement la question. C'est troublant."


hi "N'oublie pas d'appeler de temps en temps quand tu es dehors. Tu as mon numéro, hein ?"

show hanagown smile
with charachange


"Hanako hoche rapidement la tête, un sourire joyeux sur le visage."


"C'est bizarre de voir comment les gens semblent être heureux quand ils ont un but vers lequel avancer. Yuuko semble rayonner à chaque fois que ses objectifs universitaires sont abordés et maintenant Hanako réagit pareil."


"Donc pourquoi je me sens toujours aussi incertain ? Et pourquoi Lilly aussi ?"


"Les relations peuvent vraiment être d'un compliqué parfois."

show hanagown worry
with charachange


ha "Oh, euh... qu-quelle heure est-il ?"


hi "Mmh ? Oh..."


"Il me faut une seconde pour me rappeler que Lilly n'a pas de support visuel sur son horloge. Je devrais le savoir, étant donné toutes les fois où j'ai été dans sa chambre."



"J'attrape mon sac pour en sortir ma montre et comprends la raison de la question de Hanako."


hi "Il est dix heures vingt. Presque le couvre-feu."

show hanagown normal:
    ypos 1.0
with dissolvecharamove


"Hanako se lève, époussette ses vêtements et défroisse sa chemise de nuit."

show hanagown smile
with charachange


ha "Je... ferais mieux d'y aller alors. Bonne nuit Lilly. Bonne nuit Hisao."

stop music fadeout 5.0

show lilly basic_smileclosed_paj
with charachange


li "Dors bien, Hanako."


hi "À demain."

hide hanagown
with dissolve


"Sur ce, elle passe la porte et la referme silencieusement derrière elle."

show lilly basic_smileclosed_paj:
    xpos 0.5
show bg school_dormlilly at bgright
with charamove

"…"


"Silence."


"Ça semble arriver de plus en plus souvent entre Lilly et moi récemment. Après quelques secondes, je trouve enfin quelque chose à dire."

play music music_another fadein 4.0


hi "Oh, d'ailleurs, j'ai parlé à Mutou vendredi et j'ai enfin des guides pour l'université et comment s'y inscrire."

show lilly basic_smile_paj
with charachange


li "C'est une bonne chose. Si tu comptes t'inscrire à l'université, j'imagine que tu as une idée de ce que tu comptes faire dans le futur ?"


hi "Je crois que j'ai envie de devenir professeur de sciences. Ça va mettre un moment entre l'université et tout ce qu'il faut pour être qualifié, mais je crois que ça vaudra le coup."

show lilly basic_satisfied_paj
with charachange


"Le visage de Lilly rayonne en entendant mon annonce. J'imagine que, étant donné que son vœu est de devenir professeur, elle est contente que je choisisse le même chemin."


li "Donc, tu as décidé de faire carrière dans l'enseignement..."

show lilly basic_smile_paj
with charachange


li "Je trouve que ça te correspond parfaitement, Hisao."


"Je souris et hoche la tête. Cette fois, même si je sais qu'elle ne peut pas me voir, je sais qu'elle le ressent."

show lilly basic_planned_paj
with charachange


li "J'imagine que Mutou doit avoir bien pris la nouvelle ?"


hi "C'est peu de le dire."


hi "Dis Lilly ?"

show lilly basic_smile_paj
with charachange


li "Oui ?"


hi "Je sais que tu veux devenir professeur, mais..."


"Pendant une seconde, je me demande si je devrais vraiment lui demander, mais après tout, il est un peu trop tard pour cela."

show lilly basic_smileclosed_paj
with charachange


li "J'espère que tu ne crois pas que je me vexerais si ça a un rapport avec le fait que je sois aveugle."


"Son ton accusateur est trahi par son visage joueur, Lilly étant amusée par ma gêne sur le sujet. Certaines choses ne changent jamais."


hi "Pas faux."


hi "Je me demandais juste si le fait que tu sois aveugle est une gêne, avec tes ambitions de devenir professeur et tout."

show lilly basic_surprised_paj
with charachange


"Elle semble légèrement surprise avant d'y réfléchir. Je refuse de penser qu'elle ne s'est jamais posé la question."

show lilly basic_emb_paj
with charachange


li "Je me demande... Hisao, tu pourrais fermer les yeux un moment?"


hi "D'a... ccord ?"


"Un sourcil levé, je fais ce qu'elle me demande."

$ renpy.music.set_volume(0.5, 2.0, channel="music")

scene black
with shuteye


"Je n'ai aucune idée de ce à quoi elle pense et mes interrogations s'accentuent alors que j'entrouvre un œil."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

show bg school_dormlilly at bgright
show lilly basic_smileclosed_paj_close at center
with openeye


"Prenant sur la table de nuit le ruban noir qu'elle porte habituellement dans les cheveux, elle s'avance vers moi tout en glissant ses doigts dessus pour enlever les cheveux restants."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene black
with softwipedown


"Je comprends soudainement ses intentions quand je sens le tissu noir au contact de mon visage, s'enroulant autour de ma tête et sur mes yeux."


hi "Hum... pour quoi faire, exactement ?"


li "C'est un petit test, Hisao. Vu que tu te demandais, je vais te laisser voir les choses à ma façon pour un moment."


"Oh, c'est donc pour ça."


"Pour être honnête, ça a l'air marrant. Un peu enfantin et j'aurais l'air bête si quelqu'un me voyait, mais faire un peu les idiots n'a jamais fait de mal à personne."


"Je me relève prudemment, les mains en face de moi pour éviter les obstacles."


hi "D'accord, maintenant je fais quoi ?"


li "Maintenant, touche-moi."


hi "D'accord. Bon alors..."


"J'avance prudemment, vers le son de la voix de Lilly."


"Je marche très lentement, l'expérience étant totalement nouvelle pour moi et je ne veux pas trébucher sur quelque chose comme une table ou une de ses piles de livres."

play sound sfx_rustling


"Quelque chose de doux et pourtant solide touche ma jambe gauche. Après inspection, il se trouve que c'est le lit de Lilly."


"Je m'avance, content que la chambre de Lilly soit si petite et bien rangée. Même les piles de livres sont généralement proches du mur, en dehors du chemin."

play sound sfx_pillow


"Je fronce les sourcils quand mes mains rencontrent le mur."


hi "Hé Lilly, tu es où ?"


li "Qu'est-ce que tu fais là-bas ? Je suis par ici."


"La voix de Lilly vient de l'autre côté de la pièce, loin de là où elle était avant, je peux le dire même avec mes oreilles peu entraînées. Si elle va de l'autre côté pour éviter que je l'atteigne, alors ce n'est qu'un jeu pour elle ?"


"...Bien sûr. Comparé à toute une vie sans le sens de la vue, quelques minutes avec un bandeau ne sont rien."


"J'imagine qu'elle a prouvé ce qu'elle voulait, elle est largement capable de se déplacer dans sa chambre et même en dehors d'ailleurs, j'ai vu à quel point elle est indépendante en comparaison de beaucoup d'autres à Yamaku."


"Bon, même si ce n'est qu'un jeu, je peux tout aussi bien y jouer sérieusement."


"Avec une vitesse bien plus grande que la première fois, je m'avance vers la source de sa voix, évitant intelligemment la table dans le centre de la pièce, me rappelant de sa position."


hi "Je t'ai eue !"


"Elle émet un petit rire, suffisamment long pour que je me rende compte qu'elle passe juste à côté de moi."

play sound sfx_impact2
with vpunch


"Je me tourne de nouveau dans sa directio— la table n'était pas là avant !"


hi "Aïe... aïe... aïe..."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

show bg school_dormlilly
with softwipeup


"Je m'assois lentement à côté de la table, enlevant mon bandeau et frottant ma tête endolorie."

play sound sfx_impact
with vpunch


"Je donne un coup de pied à la table qui est juste en face de l'endroit où je suis tombé. Ça ne sert à rien, mais elle l'a mérité."

show lilly basic_oops_paj_close at center
with charaenter


li "Hisao ?"


"Lilly se tient toujours à côté de moi, ne sachant pas ce qui s'est passé."


hi "Désolé, je suis tombé."

show lilly basic_concerned_paj_close
with charachange


li "Tu t'es fait mal ?"


hi "Un peu à la tête, mais ça va. Je crois que la table s'est mise dans mon chemin pour me faire tomber."

show lilly basic_giggle_paj_close:
    ypos 1.1
with dissolvecharamove


"Elle rit un peu et vient s'asseoir à côté de moi, posant sa main sur la mienne."

show lilly basic_weaksmile_paj_close
with charachange


li "J'imagine qu'on arrête là ?"


hi "Je crois bien."


hi "Mais je crois aussi avoir compris où tu voulais en venir. Bien que j'aurais aimé que cela n'implique pas un tel mal de tête."

show lilly basic_surprised_paj_close
with charachange


"Lilly ne semble pas comprendre."


li "Où je voulais en venir ?"


"Et je lui réponds par un regard totalement vide."


hi "C'était juste pour s'amuser ?"

show lilly basic_reminisce_paj_close
with charachange


li "Je pensais juste que ça pourrait t'aider à te familiariser avec le sujet. Tu sembles toujours marcher sur des œufs quand tu en parles."

show lilly basic_smileclosed_paj_close
with charachange


li "Pour enseigner, la vue n'est pas si importante. Il y a beaucoup de classes tenues par des professeurs aveugles et il y a suffisamment de ressources pour que je me documente sur le sujet."

show lilly basic_smile_paj_close
with charachange


li "C'est aussi simple que ça, vraiment."


"J'affaisse mes épaules et souris."


hi "Ouais, je comprends. Je pense qu'on va juste devoir travailler tous les deux pour atteindre nos objectifs, alors."

stop music fadeout 4.0

show lilly basic_cheerful_paj_close
with charachange


li "Mmh..."


hi "Qu'est-ce qu'il y a ?"


"Après une petite hésitation, Lilly avance son menton et ferme les yeux dans une mimique qui ne s'oublie pas."

scene ev lilly_kissing
with whiteout

play music music_one fadein 1.0


"J'accepte avec plaisir, nos lèvres se touchent. À ce moment, je sens sa main glisser sur ma poitrine par dessous ma chemise. La sensation de sa main contre ma peau nue est suffisante pour que mon cœur accélère."


"Elle a encore envie ?"


"Bah, je ne me plains pas. Elle apprécie vraiment ça et même avec tous mes médicaments, ma libido est toujours intacte."


"Je continue de l'embrasser, lui tenant la main alors que je sens qu'elle dessine les contours de mon torse."

scene bg school_dormlilly
show lilly basic_smileclosed_paj_close:
    center
    ypos 1.1
with whiteout


"Finalement nous nous séparons, la pièce est silencieuse en dehors de nos respirations."

show lilly basic_surprised_paj_close
with charachange


li "Dis, Hisao ?"


hi "Ouais ?"

show lilly basic_emb_paj_close
with charachange


li "Tu ne penses pas que... tu pourrais remettre le bandeau ?"


"Sa proposition timide me surprend."


"J'imagine qu'elle veut m'initier au sexe de la façon dont elle le vit aussi. Ou juste savoir comment je serai durant l'acte, entravé par le bandeau."

$ renpy.music.set_volume(0.5, 0.0, channel="music")


scene black
with softwipedown


"Tout en étant un peu troublé, je fais ce qu'elle dit et mets le ruban sur mes yeux. Le monde redevient noir encore une fois."


"Je deviens tendu par réflexe alors que je sens la main de Lilly me caresser doucement le visage, totalement incapable d'anticiper ses actions."


"Il faudrait vraiment que je m'habitue à ce genre de contacts. Même après plusieurs semaines à sortir ensemble, ça n'est pas aussi naturel pour moi que ça l'est pour elle."


"...Silence ?"


hi "Dis, Lilly..."


li "Chuut."


"Je suis ses instruction et écoute attentivement, essayant de deviner ce qui se passe autour de moi."


"En comparaison d'avant où j'essayais d'attraper Lilly, le besoin de me déplacer avec précaution n'est plus là, je peux prendre mon temps et me concentrer plus sur l'écoute."


"Il faut un moment, mais je peux finalement entendre le doux bruit de sa respiration dans la chambre silencieuse."


"Inspirant... expirant... inspirant... expirant..."


"Comparant à la mienne, je réalise qu'elle respire plus profondément que la normale, spécialement pour elle."


"Je détecte un autre son, un que je n'arrive pas à identifier immédiatement. Je ne crois pas l'avoir déjà entendu, mais..."


"Mon cœur redouble de vitesse alors que je réalise la source de ce bruit, ma main se dirigeant vers elle presque par réflexe. Son visage semble plus doux que d'habitude sous mon toucher, sa tête se penchant très légèrement sous ma main."

li "Hisao…"


"J'avale ma salive et prends un moment pour essayer de me calmer. J'ai besoin de toute ma concentration pour prendre conscience de mon environnement."


"Après quelques respirations, je crois que j'ai réussi à me ressaisir. Avec un toucher si léger que ça ne dérangerait pas une plume, je commence à descendre ma main le long de son corps."


"...et je peux sentir que je perds encore une fois ma concentration, tout cela à cause de son fin pyjama en soie qui épouse parfaitement les formes de son corps."


"Si elle est comme ça, alors ça veut dire qu'elle doit être assise contre son lit, me faisant face."


"...D'accord, ce doit être sa hanche. Si je descends encore lentement..."

label fr_L26h:


"La respiration de Lilly s'interrompt en un sursaut alors que ma main passe sur la sienne, suivant timidement ses doigts entre ses jambes et les perdant alors qu'ils continuent dans sa culotte."


"Une très légère sensation de mouillé arrive sur mes doigts, mais c'est suffisant pour comprendre ce qu'elle fait."


"Mon esprit est soudainement assailli d'images de ce qu'elle doit faire en face de moi. Je ne l'ai jamais imaginée faire ça auparavant, et être incapable de la voir décuple mon envie."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

scene bg school_dormlilly
with softwipeup


"Je soulève le ruban et enlève de mes yeux les quelques cheveux qui étaient restés coincés dedans."


"Pendant un moment je ne peux que deviner, ma vision étant complètement floue. Je me contente d'attendre que tout apparaisse en face de moi."

scene evh lilly_masturbate:
    truecenter
    subpixel True zoom 1.1
    acdc_warp 10.0 zoom 1.0
with flash


"Juste comme je le pensais, Lilly est assise en face de moi."


"Avec une main sur le sol pour garder un certain équilibre et son autre main cachée dans sa culotte bleu foncée, ses doigts remuant entre ses jambes, je crois que c'est la chose la plus érotique que je n'ai jamais vue."


"Je tends le bras et écarte les cheveux de son visage, son dos étant penché vers l'arrière alors qu'une vague de plaisir passe dans son corps dans une autre inspiration."

hi "Lilly…"


"Lilly est vraiment mignonne alors qu'elle sourit quand je l'appelle par son nom. J'ai l'impression que c'est dans les moments où elle fait le moins attention qu'elle laisse toujours les émotions les plus sincères s'afficher sur son visage."


"Il ne faut pas longtemps avant qu'elle bouge ses doigts de plus en plus vite, son excitation s'accentuant, l'odeur de sa transpiration le confirmant."


"Je m'assois en face d'elle. Ce n'est pas comme si mon excitation n'était pas présente ; il me faut toute ma volonté pour la laisser continuer seule au lieu de me mettre sur elle."

scene evh lilly_masturbate_come_face
with flash


"C'est étrange... Au début je trouvais ses yeux vagues presque troublants à toujours être dans le vide. Maintenant cela ne me fait presque plus rien."


"Mon attention se reconcentre sur elle alors qu'elle laisse échapper un gémissement, sa respiration devenant de plus en plus rapide et ses hanches remuant."

scene evh lilly_masturbate_come
with flash


"Aussitôt que je réalise à quel point Lilly est proche de la fin, sa respiration se bloque. Ses yeux se ferment alors que chaque muscle de son corps semble se contracter, avant d'atteindre l'orgasme."


"Pendant quelques secondes elle se rétracte sur elle-même, subissant l'extase avant que son corps ne se détende dans un long souffle sortant de ses lèvres."

scene bg school_dormlilly
with locationchange


"Je... n'ai aucune idée de quoi dire. Le silence règne alors que je la regarde, ses cheveux devant le visage alors qu'elle est assise, épuisée."

show lilly basic_emb_paj_close:
    center
    ypos 1.1
with charaenter


li "Hisao..."


"Au moment où elle enlève les cheveux de son visage, mon envie finit de dominer entièrement mon corps. Sans y penser une seconde, je m'avance vers elle."


"C'est un sentiment inhabituel. Je me sens étrangement puissant. Me tenant en face de son visage vide. En y pensant, c'est la première fois depuis l'accident que je me sens physiquement fort."


hi "Lilly... Je te veux."

show lilly basic_weaksmile_paj_close
with charachange


"À ma grande surprise, elle sourit légèrement avant de tendre le bras pour me toucher le visage. Elle a une expression presque vantarde, une de celles qu'elle affiche quand elle a réussi à obtenir quelque chose de moi."


hi "Tu... voulais que je le fasse ?"

show lilly basic_smileclosed_paj_close
with charachange


"Elle continue de sourire et hoche silencieusement la tête. J'imagine que c'est une bonne façon de me faire prendre l'initiative pour une fois."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene black
with softwipedown


"Et, à ma grande surprise encore, elle abaisse de nouveau rapidement le bandeau autour de ma tête. Encore une fois, je me retrouve dans le noir complet."


li "Je t'ai dit... de le garder... non ?"


"Le ton moqueur dans la voix de Lilly, ponctuée par sa respiration... elle ne semble jamais perdre son habilité à contrôler la situation."


"Mais cette fois... juste cette fois..."


li "Ah, Hisao ?! Qu'est-ce que tu— ?"


"Je passe mes mains en dessous d'elle, touchant la soie et sa peau alors que je la soulève lentement, avec une légère difficulté."


"Bien que je ne la décrirais pas comme lourde... sa taille ne simplifie pas l'exercice."


"Il ne me faut que quelques pas prudents pour que je sente le bord de son lit contre mes jambes, et je repose Lilly sur ses draps, tout aussi délicatement que je l'ai soulevée."




hi "Ton lit sera plus confortable que le sol, non ?"


li "Toujours un gentleman, n'est-ce pas ?"


"Je passe rapidement mes mains sur les grandes jambes de Lilly, toujours aussi attrayantes même sans pouvoir les voir, et lui ôte son bas de pyjama et sa culotte qui étaient à ses chevilles, pour les envoyer au loin."


"Je n'ai aucune idée de l'endroit où ils ont été envoyés..."


"Bah, ça m'importe peu. Ils sont quelque part dans la pièce."


"Sans trop de problème, je retire mon propre pyjama et mes sous-vêtements et me positionne entre ses jambes. Ou du moins, ce que je crois être entre ses jambes."


"Avec une main sur le lit pour me maintenir, j'avance ma main droite, incertain."


"Oh, oups. Mon premier contact avec elle est ma paume se retrouvant maladroitement sur son nez."


"Elle rit un peu avant de tourner la tête. Comprenant ce qui se passe, je pose ma main sur son visage et utilise mon pouce pour lui caresser la joue, comme elle le fait si souvent avec moi."


"Ça serait plus facile si elle ne bougeait pas la tête dans ma main, mais la sensation est agréable."


"J'avale ma salive et essaye de me redresser, utilisant mon autre main pour me guider, tandis que je rentre en elle."


"Aussitôt que je sens sa chaleur autour de moi, je réalise à quel point je suis excité."


"Sans la vision, je suis libre de me concentrer beaucoup plus sur mes autres sens, comme le toucher. L'expérience entière semble plus vive, plus intense qu'elle ne l'était avant."


"Je commence lentement à bouger les hanches d'avant en arrière, mon cœur battant vite d'excitation."


"Je sens que Lilly ferme fort les yeux, le mouvement de sa joue en dessous de mon pouce me rappelant la légère prise que j'ai sur son visage."


"C'est difficile de m'empêcher d'être complètement submergé. Et dire que c'est comme ça à chaque fois pour elle, expérimenté à travers chacun de ses sens sauf celui qui est le plus important pour moi."


"De sa joue à son cou, je commence à glisser ma main vers son bras pour sentir son corps."


"Le bas de son cou... sa peau légèrement humide..."


"Mon odorat est stimulé par l'odeur de sa transpiration et de la mienne. Même l'odeur ambiante, sensiblement différente de celle de ma propre chambre, ajoute à la sensation."


"Quand je mets ma main sur son sein, son petit gémissement résonne dans mes oreilles, en même temps que le son de notre acte."


"La peau sous ma main bouge d'avant en arrière à chacune de nos poussées, ma prise sur celle-ci se resserrant alors que mon envie pour la peau presque nue du corps de Lilly grandit."


"Je peux même sentir son petit téton contre ma paume. Ma main glisse dessus et mes doigts le pincent à travers la fine soie de son haut de pyjama."


"Son petit bruit plaintif se transforme en gémissement alors qu'elle ressent le même plaisir que moi. Je peux sentir mon cœur battre fort dans ma poitrine et son battement à elle sous ma main."


"Je peux sentir ses mains serrer mes poignets, sa poigne étonnamment ferme alors que sa poitrine se soulève dans un plaisir irrésistible."

label fr_L26x:

scene black
with dissolve


"Plus... Je veux plus..."

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)

window show


"Je peux sentir ma poitrine se serrer alors que je continue mes à-coups, tous les deux entièrement pris par notre acte."

$ renpy.music.set_volume(0.4, 0.5, channel="music")

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)

window show


"Rien... d'inhabituel... je dois juste respirer plus doucement pour me... reprendre..."

$ renpy.music.set_volume(0.3, 0.5, channel="music")

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)

with Pause(0.7)

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

window show


"Cette sensation est... normale..."

$ renpy.music.set_volume(0.2, 0.5, channel="music")

window hide

play sound sfx_heartfast
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

hi "Aah… aaaaaaaah…"

window hide

play sound sfx_heartfast
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


"C'est... je ne peux plus... la douleur est trop forte..."

window hide

play sound sfx_heartstop
show heartattack alpha
with Dissolve (0.1)

stop music fadeout 0.3

show heartattack residual
with Dissolve (0.8)

window show


hi "AAAAARGH !"

with vpunch


"Je tombe en arrière, me séparant brusquement de Lilly, me frappant maladroitement le pied contre la table, et j'atterris violemment sur le sol."


"Respirant très fort, j'essaie très vite d'attraper le ruban sur mes yeux et m'allonge sur le dos. Je dois retirer ce truc, je dois retirer ce truc..."

scene white
with softwipeup

scene bg misc_ceiling
show heartattack residual
with locationchange


"Pendant un moment, tout est blanc. Alors que la lumière m'aveugle, ma respiration ralentit tout doucement."

window hide

$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_tragic fadein 4.0

hide heartattack
with Dissolve(3.0)

window show


"Des secondes passent et je mesure avec précision le rythme de mes battements avec toute ma concentration."


"Mon cœur est... normal. Il est revenu à la normale."


"Je me sens encore plus étrange alors que je reste hébété sur le sol, regardant le plafond. L'adrénaline continue de circuler dans mes veines, mais je me sens complètement épuisé."


"Alors que je me redresse, j'entends Lilly sortir du lit et venir vers moi."

show bg misc_ceiling_blur as bg2:
    center
    alpha 0.0
    linear 1.0 alpha 1.0
show lilly superclose_shock:
    xalign 0.5 yanchor 0.5 ypos 0.15 alpha 0.0
    subpixel True rotate 180
    easein 1.0 alpha 1.0 ypos 0.3
with Pause(1.0)


li "Hisao ? Tu vas bien ? Hisao ?!"


hi "Je vais bien, Lilly. Je vais... bien."

show lilly superclose:
    xalign 0.5 yanchor 0.5 ypos 0.3 alpha 1.0
    subpixel True rotate 180
with charachange


"Elle soupire de soulagement, son expression inquiète s'effaçant."


"L'expression que je vois sur son visage après coup est celle que je ne voulais jamais voir chez elle. C'est une expression que je déteste depuis la première fois où je l'ai vue sur mes parents, à l'hôpital, au tout début."


"Pitié. Lilly... a pitié de moi."

scene black
with shuteye


"Je ferme les yeux et me tourne, impuissant. J'ai envie de vomir."

play sound sfx_rustling


"Je peux entendre Lilly s'éloigner et se rhabiller, je perçois le bruit que font ses vêtements après qu'elle ait passé un moment à les chercher."


hi "Désolé..."

scene bg school_dormlilly
show lilly basic_concerned_paj at center
with openeye


"Elle secoue lentement la tête en finissant de boutonner son haut. Son gentil sourire semble si fragile, si délicat, que ça me fend le cœur."

show lilly basic_concerned_paj_close
with characlose

show lilly basic_concerned_paj_close:
    ypos 1.1
with charamove


"S'approchant avec précaution, elle touche le bord de la table basse avant de s'asseoir à côté de moi, passant ses bras autour de ma poitrine."


li "Je suis désolée, Hisao. Je n'aurais pas dû t'imposer mes désirs."


hi "Ne t'excuse pas. Je vais bien, tu m'as déjà vu comme cela avant."


hi "Je pense juste que je n'aurais pas dû y aller si fort."


"Mes paupières sont lourdes. Être assis à côté d'elle comme cela me permet de dissiper l'adrénaline de mon corps et de me relaxer un peu."

show lilly basic_oops_paj_close
with charachange


li "C'est... pour ça que tu ne te mets jamais au-dessus ?..."


hi "Ouais. C'est une bonne chose que tu aimes ça, hein ?"

show lilly basic_weaksmile_paj_close
with charachange


"La blague semble la soulager un peu, chose qui me permet de me sentir moins gêné par tout cela."


"La tête de Lilly vient se poser sur mon épaule alors que je lutte pour garder les yeux ouverts, avec de plus en plus de difficulté à chaque battement de paupière. Je me sens totalement vidé de mon énergie."


li "Ça va, Hisao. Tout va bien."

stop music fadeout 5.0


"Juste après avoir dit ça, un petit fredonnement sort de ses lèvres. Trop fatigué pour réfléchir, tout ce que je peux faire est écouter la douce musique."


"C'est une douce musique mélancolique. Ça me semble familier, mais plus j'essaye de me rappeler d'où elle vient et moins j'arrive à me concentrer."


"Sentir sa tête sur mon épaule, l'odeur de ses cheveux et son corps contre le mien est apaisant. Sa faible voix aussi apaise mon esprit autant que la chaleur de son corps relaxe mes muscles."


"Ce moment unique, silencieux... après tout ce qui est arrivé, je me rends compte à quel point je suis épuisé. Je peux sentir mes paupières devenir de plus en plus lourdes."


"Même si ce moment arrive après ce chaos, j'aimerais qu'il dure pour toujours."


"Lilly et moi, ensemble, partageant un petit moment à deux, comme nous en avions l'habitude."


"Mais si c'est le cas... pourquoi est-ce que je la sens... beaucoup plus loin de moi que je ne l'ai jamais sentie ?"

scene black
with dissolve





label fr_L27:

scene bg school_library
with locationchange

play sound sfx_doorslam
play music music_happiness fadein 2.0


"Le claquement bruyant des livres tombant dans le bac des retours rompt le silence de la bibliothèque scolaire."


"C'est devenu une habitude pour moi de venir à la bibliothèque au moins une fois par semaine. Non seulement lire m'occupe, mais discuter de livres avec Hanako et Lilly aussi."

show yuuko panic_up at center
with charaenter


"Apparemment surprise, Yuuko se tourne en direction du bruit. J'aurais cru qu'elle serait habituée au bruit des livres qui tombent, vu qu'elle travaille ici."

show yuuko neutral_down
with charachange


yu "Oh, bonjour Hisao. Déjà revenu ?"


"Je prends un moment avant de répondre, mes pensées toujours distraites par la mélodie familière de Lilly qui ne me quitte pas depuis plusieurs jours, depuis que je me suis endormi en l'écoutant."


hi "Mmh ? Oh, ouais. Je rends juste quelques livres que j'avais empruntés."


"Elle baisse les yeux en direction de la caisse où j'ai lâché les livres."

show yuuko closedhappy_down
with charachange


yu "Tu lis vraiment beaucoup, hein ?"


hi "C'est plus devenu une routine maintenant. Ça passe le temps, au moins."

show yuuko worried_up
with charachange


yu "J'aimerais bien avoir du temps libre aussi..."


"Passer d'une discussion normale à la dépression en moins de cinq secondes... Je crois que c'est un nouveau record pour elle. Elle semble un peu déprimée aujourd'hui, même en comparaison de d'habitude."


"Vu qu'elle a deux travails pour vivre, je peux imaginer comment ça doit ralentir son rythme de vie."


"En y pensant, la paye de son job ici ne doit pas être si mal. L'idée du personnel d'une école privée si prestigieuse mourant de faim me semble improbable."


hi "Avoir deux travails doit prendre beaucoup de temps. Je n'y arriverais probablement pas."

show yuuko neutral_up
with charachange


yu "Tu as de la chance d'être étudiant. Tu crois que tu pourras aller à l'université ?"


"Si elle demande, c'est parce que l'université est le résultat attendu de ce genre d'éducation. Les écoles privées sont assez chères."


hi "Je... crois. J'ai l'argent, je pense."


hi "J'ai un but qui nécessite que j'y aille, du moins. Et j'ai des bonnes notes. Le plus important, c'est comment je ferai pour payer."

show yuuko worried_down
with charachange


yu "L'université coûte tellement cher qu'il me faut deux jobs pour me permettre d'y aller... Payer les dépenses quotidiennes est difficile aussi."

show yuuko neutral_down
with charachange


yu "Si tu lis autant, tu dois bien t'en sortir à l'école, non ?"


"Une logique intéressante. Pas fausse, cela dit."


hi "Je crois. Je n'ai pas trouvé les examens particulièrement durs, à part pour un ou deux."


hi "Ça te gêne si je te demande quelles études tu fais ?"

show yuuko happy_up
with charachange


"Yuuko semble s'illuminer avec ma question."

show yuuko closedhappy_up
with charachange


yu "Anthropologie. Pour être précise, je me spécialise dans l'histoire et la démocratie de la civilisation athénienne de l'ère classique."


"Elle semble vraiment connaître son truc. Un tel enthousiasme est admirable et c'est agréable de la voir avec autant d'entrain pour quelque chose."


"J'imagine que même quelqu'un comme Yuuko peut être heureuse si elle a un avenir défini."


hi "Ça a l'air bien. Si tu—{w=0.6}{nw}"

stop music fadeout 0.5
play sound sfx_phone

show yuuko panic_up
with vpunch


"Nous sursautons tous les deux au bruit venant de ma poche."

scene bg school_hallway3
with locationchange


"M'excusant expressément et partant rapidement dans le couloir tout en me débattant avec le clapet de mon téléphone, je regarde l'écran."


"...Étrange. C'est un numéro que je ne reconnais pas. Étant donné que je peux compter le nombre de gens ayant mon numéro sur une main, je me demande si ce n'est pas un télévendeur qui a eu de la chance."

scene bg school_hallway3_blurred
show phone mobile:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with locationchange
with Pause (0.5)


hi "Bonjour, Hisao Nakai à l'appareil."


mystery "Roh, décroche plus vite la prochaine fois. Bref, devine qui c'est ?"

play music music_comedy fadein 1.0


"Il ne me faut qu'une seconde pour reconnaitre la distincte voix profonde de l'autre côté de la ligne."


hi "Salut, Misha. Je ne m'attendais pas à ce que tu m'appelles."


aki "Hein ?! Tu penses vraiment que je parle comme elle ?"


hi "Pas du tout, Akira. Mais je ne me rappelle pas t'avoir donné mon numéro, alors j'en profite pour me moquer."


aki "Oh, ça ? Je l'ai obtenu de Lilly. Pas dur."


"Elle annonce ça avec fierté. Elle essaye de me déstabiliser, je le sais."


"J'imagine que je ne devrais pas être surpris qu'elles partagent mon numéro, vu à quel point elles sont proches."


hi "Donc, quoi de neuf ?"


aki "Tu es libre là ?"


hi "Je... crois ? Pourquoi ?"


aki "On pourrait se voir au parc en ville ? Je veux te parler de certains trucs."


hi "Est-ce que tu m'invites à un rendez-vous ?"


aki "Quoi ? Bien sûr que non..."

stop music fadeout 5.0


"Elle semble découragée, son attitude moqueuse étant partie instantanément. C'est bizarre de sa part."


hi "Bon, je vois pas de raison de refuser. Tu veux qu'on se rejoigne quand ?"


aki "Genre... maintenant."


hi "Quoi, maintenant ? Mais c'est—"


"Le silence venant du téléphone me montre qu'elle a raccroché sans dire un mot de plus."

show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with None

scene bg school_hallway3
show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with locationchange
with Pause (0.5)

hide phone
with None


"Pendant un long moment je reste planté là à regarder le “FIN D'APPEL” sur l'écran avant de repasser la conversation dans ma tête."


hi "Sérieux, c'est quoi ça Akira ?"

scene bg suburb_park_ss
with shorttimeskip

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_parkambience fadein 2.0


"Regardant à droite et à gauche, je traverse la route et arrive au parc."


"J'ai appris à prendre mon temps lors de promenades comme ça, surtout parce que le rythme de Lilly durant nos balades en ville m'impose de marcher plus lentement."


"Cela dit, j'espère qu'Akira ne m'attendait pas immédiatement."

$ ksgallery_unlock("evul akira_park")
scene ev akira_park:
    subpixel True xalign 1.0 yalign 0.0 zoom 1.0
    acdc_warp 15.0 zoom 0.8
with whiteout

play music music_night


"Il ne me faut que quelques secondes pour la voir, attendant sur un banc, une canette de bière à la main."


"L'expression qu'elle m'adresse alors que je m'approche n'affiche aucun signe de salutation ou de joie."


hi "C'est quoi cette tête ? Je n'étais pas obligé de venir, tu sais."


aki "Je savais que tu viendrais. Tu es ce genre de personne, après tout."

scene bg suburb_park_ss
with locationchange

play sound sfx_can_clatter


"Je baisse un sourcil à sa remarque tandis qu'elle pose sa canette, vidée le temps que j'arrive. Akira s'assied sur le vieux banc en bois et je fais comme elle."

play sound sfx_can


"Elle prend une autre canette de bière à côté d'elle et l'ouvre, prenant une grande gorgée. Elle semble vraiment aimer ce truc."


hi "J'imagine que je n'ai pas besoin de te demander à propos de quoi tu veux me parler, ou plutôt, de qui tu veux me parler ?"

show akira basic_resigned_close_ss at tworight
with charaenter


aki "Lilly m'a dit que tu avais posé des questions sur notre famille."


"On dirait bien qu'elles partagent plus que des numéros de téléphone. Je serais probablement inquiet s'il n'y avait pas une absence totale de malice dans sa voix. En fait, son ton est presque mélancolique."


hi "Surtout par curiosité."


hi "...Je dois admettre que je n'aurais jamais deviné que vous étiez à moitié écossaises."

show akira basic_ending_close_ss
with charachange


"Elle sort un petit rire ironique."

show akira basic_smile_close_ss
with charachange


aki "Je l'ai déjà entendu ça, crois-moi."

show akira basic_distant_close_ss
with charachange


"Le petit sourire s'efface de son visage et elle regarde au loin."


"En dehors de couples de personnes âgées parlant tout en marchant doucement, c'est plutôt silencieux ici."

show akira basic_lost_close_ss
with charachange


aki "Elle ne t'a pas tout dit cependant, hein ?"


hi "C'était assez bref. Tes parents vivent en Écosse, elle ne les avait pas vus depuis ses douze ans et elle a envie de les revoir."

show akira basic_annoyed_close_ss
with charachange


aki "Je suis toujours surprise de voir à quel point elle leur est dévouée, malgré tout ce qui s'est passé."


"La façon dont elle dit cela semble presque moqueuse. Elle soupire un peu, comme pour laisser partir de mauvaises pensées."

show akira basic_resigned_close_ss
with charachange


aki "Pourquoi crois-tu qu'ils soient partis, Hisao ?"


hi "Pourquoi ils sont partis ?"


hi "D'après ce que Lilly m'a dit, c'était pour le travail. Je crois qu'un job plutôt bien payé était impliqué aussi, étant donné la façon dont tes parents semblent vivre."


hi "Donc Lilly a été dans une école privée et c'est pour ça qu'elle se comporte de manière si distinguée."


aki "Ouais. Vu que les affaires d'Inverness ont explosé, notre père a décidé de déménager directement au quartier général de l'entreprise."

show akira basic_smile_close_ss
with charachange


aki "C'est la conclusion à laquelle je pensais que tu arriverais aussi. Tu es trop gentil."


hi "Tu ne crois pas qu'ils sont partis pour leur carrière ?"

show akira basic_resigned_close_ss
with charachange


aki "Je suis assise là, à leur en mettre plein la tête. Qu'est-ce que tu en penses ?"

show akira basic_lost_close_ss
with charachange


aki "Académie Yamaku. J'ai toujours trouvé cet endroit un peu glauque. Comme si c'était un isoloir pour ceux dont “la société” ne veut pas entendre parler."

show akira basic_annoyed_close_ss
with charachange


aki "Ils ont probablement regretté le fait que Lilly n'était pas assez vieille pour qu'ils puissent la balancer ici dès qu'ils sont partis."


"Un long silence suit cette violente critique envers ses parents et Yamaku."


"Le fait que Lilly soit aveugle n'était pas quelque chose qui pouvait être ignoré par une famille de haut standing essayant de sauver les apparences, encore moins quand une offre lucrative est sur la table."


"Au bout d'un moment, Akira sort un petit rire railleur et dit ce qu'elle ressent."


aki "Déménager pour assurer nos besoins financiers futurs avec son nouveau travail. Même à l'époque je n'y croyais pas."


"Ne souhaitant pas être venu juste pour qu'elle puisse critiquer ses parents, j'essaye d'aiguiller la discussion sur autre chose."


hi "Donc tu es restée au Japon avec Lilly ?"

show akira basic_resigned_close_ss
with charachange


aki "Soit je restais avec elle, soit elle partait vivre avec nos vieux grands-parents."


hi "Et la famille de Shizune ? Si vous êtes cousins, ils..."

show akira basic_annoyed_close_ss
with charachange


aki "Mon père et le père de Shizune se détestent. J'aurais été plus qu'heureuse de leur dire d'aller se faire voir et de vivre avec eux quand même, mais Lilly ne l'aurait pas voulu."

show akira basic_resigned_close_ss
with charachange


aki "J'ai aussi eu une offre d'emploi à ce moment, alors on a fait de notre mieux pour garder la maison de nos parents en bon état et essayer de continuer nos vies comme s'ils n'étaient jamais partis."


hi "Donc vous avez vécu par vos propres moyens ?"

show akira basic_lost_close_ss
with charachange


aki "En gros. Lilly avait école et moi je travaillais, donc on n'avait pas trop le temps de s'attrister sur notre sort."


aki "Avec l'école, ses études et ses corvées ménagères pendant que je travaillais, j'ai quand même l'impression de l'avoir laissé tomber. En fin de compte, j'ai essayé d'être là pour elle mais je me suis loupée."

show akira basic_annoyed_close_ss
with charachange


aki "Attendre d'une fille de dix-neuf ans qu'elle soit la mère d'une enfant aveugle. C'est ridicule."


"Donc... Lilly et Akira ont vécu seules après que leurs parents aient déménagé, avec Lilly se débrouillant majoritairement toute seule. J'imagine que ça explique son indépendance, en comparaison de beaucoup d'autres à Yamaku."


"J'ai peut-être été souvent seul quand mes parents travaillaient, mais c'est... vraiment quelque chose d'autre."

show akira basic_resigned_close_ss
with charachange


aki "Désolée de t'avoir fait subir mes plaintes, Hisao."


hi "Ça ne me gêne pas du tout, mais... ça te dérange si je te demande pourquoi tu me dis tout ca ?"

show akira basic_smile_close_ss
with charachange


aki "Hmph. Tu as toujours été curieux."

show akira basic_distant_close_ss
with charachange


aki "Le contexte, j'imagine."


aki "La vie n'est pas un conte de fée, Hisao. Certaines personnes doivent l'apprendre par la manière forte."


"Elle prend une longue gorgée de sa canette, son visage devenant déprimé et distant."

stop music fadeout 2.0

show akira basic_resigned_close_ss
with charachange


aki "J'ai rompu avec mon petit copain il y a quelques jours. Une fois que je serai partie, nous ne pourrons plus nous revoir."


aki "Mais c'est comme ça qu'est la vie. Tu ne peux pas juste attendre de ta vie qu'elle reste la même pour toujours. Des fois des choses arrivent et tu dois faire avec, même si ça implique de souffrir ou de faire souffrir les autres."


"Elle prend une grande bouffée d'air avant de regarder le ciel teinté d'orange."

show akira basic_distant_close_ss
with charachange


aki "Rah... si je fumais, je pourrais prendre une longue taffe là et avoir l'air cool."


"Je veux répondre, dire quelque chose pour l'aider d'une façon ou d'une autre, mais je me sens inutile. Je n'ai jamais été dans ce genre de situation et je n'ai pas l'expérience nécessaire pour pouvoir dire quelque chose pour la réconforter."


"Akira regarde dans ma direction et ne me lâche pas, ce qui m'embarrasse."

show akira basic_lost_close_ss
with charachange


aki "Je dois avoir l'air pas mal pathétique là, me plaindre à quelqu'un que je connais à peine."


hi "Pas tant que ça, et je suis expert dans l'art d'être pathétique."

show akira basic_ending_close_ss
with charachange


"Elle rit, ce que je considère comme une victoire personnelle."

show akira basic_smile_close_ss
with charachange


aki "Tu es un bon gamin, Hisao. Quand j'ai dit que j'approuvais ta relation avec ma sœur, je ne disais pas ça pour être gentille."

show akira basic_smile_ss:
    tworight
    ypos 1.1
    ease 0.5 ypos 1.0
with charadistant

play sound sfx_can_clatter


"Elle se relève du banc avec un grognement qui semble inapproprié pour son âge et jette la canette vide dans une poubelle après une dernière gorgée."

show akira basic_boo_ss at tworight
with charachange


aki "C'est juste dommage que ça ne compte pas vraiment dans ce monde."

show akira basic_resigned_ss
with charachange


aki "Quand j'ai dit que je partais pour l'Écosse, je l'ai décidé parce qu'une bonne opportunité s'est proposée dans le quartier général de l'entreprise."


aki "Quand nos vieux m'ont dit ça quand on était chez eux, ils ont aussi proposé à Lilly de les rejoindre à Inverness."

play music music_sadness fadein 0.5


"Pas possible..."


"Ses réponses évasives quand je lui posais des questions sur son avenir... le sentiment étrange qui s'était répandu entre nous... cette poussée de colère sans raison..."


"Tout s'explique."


"Cette même famille dont elle s'est rappelé l'existence après l'anniversaire de Hanako, cette même famille qui les a laissées seules, Akira et elle, pour s'envoler vers de plus verts pâturages..."


"Maintenant je me sens idiot de n'avoir jamais poussé Lilly à me dire ce qui l'embêtait. Je n'ai jamais pensé que quelque chose était arrivé durant ses vacances avec sa famille à Inverness."


"Et maintenant, un malaise grandit en moi. Si sa famille l'a invitée à les rejoindre en Écosse, de l'autre côté de la terre..."


hi "Elle a... accepté ?"

show akira basic_lost_ss
with charachange


aki "Lilly ne m'a pas dit ce qu'elle avait décidé et il semblerait qu'à toi non plus."


aki "C'est pour ça que j'ai voulu te parler, Hisao."


hi "Le contexte, hein..."


"Je colle mon dos au banc, avec des sentiments d'inquiétude et de frustration sûrement écrits sur mon visage."

show akira basic_resigned_ss
with charachange


aki "Lilly est une personne forte, Hisao. Mais elle n'est pas infaillible."


aki "Je pense que c'est mon job de m'inquiéter pour elle, étant sa grande sœur, mais je crois que tu mérites de savoir."


hi "Je comprends."

show akira basic_lost_ss
with charachange


aki "Ça va ? Tu as l'air déprimé."


hi "Non. Je... réfléchis."

show akira basic_ending_ss
with charachange


aki "C'est bien. Réfléchir est une bonne chose. Te précipiter ne te mènera nulle part."

show akira basic_boo_ss
with charachange


"Elle regarde sa montre, bougeant à peine le poignet."

show akira basic_lost_ss
with charachange


aki "Je dois y aller. Ça ira toi ?"


hi "Ça ira, ne t'inquiète pas. Je vais en parler à Lilly et tout arranger."

show akira basic_smile_ss
with charachange


"Elle sourit, mais son sourire ne semble pas être tout à fait sincère."


"Nous sommes là, occultant volontairement le fait que Lilly est devant le plus grand choix de sa vie et qu'elle essaye de porter ce fardeau toute seule."


"Une part de ce fardeau est notre relation."

stop music fadeout 5.0
hide akira
with charaexit


"Au moment où je relève la tête, Akira est déjà en train de partir, une main en l'air."


"Pour la première fois depuis longtemps, j'ai enfin une réponse à quelque chose. Ou pas. Mais au moins j'ai une question à poser."


"“Vas-tu rester, ou partir ?”"

stop ambient fadeout 2.0

scene black
with dissolve




label fr_L28:

scene bg suburb_roadcenter_rn
show rain normal
with locationchange

play ambient sfx_rain fadein 4.0


hi "Dépêche-toi, Lilly !"

show lilly basic_concerned_cas_close_rn behind rain at center
with charaenter


li "Je vais aussi vite que je peux !"


"Je peux à peine entendre la voix de Lilly avec le bruit de la pluie. Même si je n'aime pas la tirer comme ça, la situation l'oblige."


"J'avance, ma main libre sur la tête dans une tentative inutile de garder mes cheveux secs. J'ai l'impression de ne voir qu'en gris. C'est vraiment un sale temps pour l'été, vraiment pas ce que j'aurais souhaité pour un rendez-vous."


"C'est nul. J'ai même vérifié la météo avant, une des seules fois où je l'ai fait d'ailleurs. Et elle a confirmé qu'il ferait beau dimanche après-midi."


"Je regarde Lilly, ses épaules sont maintenant complètement trempées, sa main droite tenant fort la mienne et la gauche tenant sa canne rétractée."


"Cette horrible averse est arrivée alors que nous étions à mi-distance entre Yamaku et notre destination, donc on a décidé de se dépêcher de parcourir la distance qu'il nous restait plutôt que de faire demi-tour."


"Absolument pas habituée à courir si vite, Lilly utilise toute sa concentration pour ne pas tomber."

show lilly basic_oops_cas_close_rn
with charachange


li "Hisao, tu sais où tu vas ?!"


"Elle en est réduite à crier pour essayer de se faire entendre au-dessus du bruit du vent et de la pluie."


hi "Le Sha—"


"Le reste de ma phrase est complètement étouffé par une pluie encore plus forte."

show lilly basic_sad_cas_close_rn
with charachange


li "Le quoi ?!"


hi "Le Shanghai ! "

show lilly basic_concerned_cas_close_rn
with charachange


li "C'est encore loin ?!"


hi "On y est presque !"

show bg suburb_shanghaiext_rn
show lilly basic_concerned_cas_close_rn
with shorttimeskip


"Il ne faut pas longtemps avant que je m'adresse de nouveau à elle."


hi "C'est bon, c'est juste là !"


"Je m'arrête juste en face du bâtiment familier, les lanternes extérieures l'éclairant toujours, et j'attends que Lilly reprenne son souffle avant de rentrer."


hi "Les dames d'abord."

play sound sfx_storebell

show lilly basic_smileclosed_cas_close_rn at center
with charachange

with Pause(0.5)

hide lilly
with charaexit


"La petite cloche intérieure résonne alors que je lui tiens la porte, j'ai droit à un sourire et un petit hochement de tête en guise de remerciement, puis j'entre à mon tour."

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
play music music_dreamy fadein 3.0

scene bg suburb_shanghaiint
show lilly basic_smileclosed_cas at center
with locationchange


"Alors que je rentre et m'essuie les pieds, un seul coup d'œil est nécessaire pour remarquer qu'il n'y a presque personne. Le Shanghai ne semble pas déborder d'activité d'habitude et aujourd'hui ne diffère pas. Seules quelques tables sont occupées."


"Peu après que la cloche ait retenti, quelqu'un qu'on attendait vient nous accueillir."

show bg suburb_shanghaiint at bgleft
show lilly basic_smileclosed_cas at twoleft
with charamove

show yuukoshang happy_up at tworight
with charaenter


yu "Bienvenue au Shanghai !"


"Yuuko semble plutôt joyeuse aujourd'hui. Essayer de prédire son humeur est plutôt dur, mais pour une fois c'est bien."

show lilly basic_smile_cas
with charachange


li "Bonjour, Yuuko."


hi "Salut."

show yuukoshang closedhappy_down
with charachange


yu "Bonjour à vous deux."

show yuukoshang neutral_down:
    ypos 1.25
with Dissolvemove(0.2)

with Pause(0.2)

show yuukoshang neutral_down at tworight
with charamove


"Elle se penche en avant et en perd presque l'équilibre en se redressant et nous fixe un moment."

show yuukoshang worried_down
with charachange


yu "Qu'est-ce qui vous est arrivé ? Vous êtes..."


"Ses yeux se dirigent vers la porte derrière nous."

show yuukoshang panic_up
with charachange


yu "Oh. Oh mince."


hi "On est à l'intérieur, au moins. C'est le plus important."

show lilly basic_weaksmile_cas
with charachange


li "Il fait bon ici. Tu as de la chance de travailler à l'intérieur aujourd'hui."

show yuukoshang smile_down
with charachange


yu "C'était plutôt calme. J'aime bien les jours comme ça."

show yuukoshang worried_down
with charachange


yu "Oh, ah, désolée... Hum. Quelque chose vous ferait envie ?"

show lilly basic_smile_cas
with charachange


li "Un thé français à la vanille, s'il te plaît."


hi "La même chose."

show yuukoshang closedhappy_up
with charachange


yu "D'accord. Ça arrive tout de suite."

hide yuukoshang
with charaexit


"Elle part rapidement avec un air sérieux sur le visage, essayant du mieux qu'elle peut de ne pas oublier nos commandes. Dans tous les cas, elle est sérieuse dans ses travails."

show bg suburb_shanghaiint at center
show lilly basic_smileclosed_cas_close at center
with dissolvecharamove

show lilly basic_smileclosed_cas_close:
    ypos 1.1
with charamove


"J'amène Lilly jusqu'à une table vide pour que nous nous asseyions. Comme d'habitude, il y a une grande différence entre la façon dont je me laisse tomber de fatigue sur le siège et la façon dont Lilly se pose délicatement sur le sien, sa canne à côté d'elle."


"Pendant un moment, je me contente de regarder la pluie tomber derrière la fenêtre. De temps en temps je vois quelqu'un courir dans la rue pour rester aussi sec que possible, ses mains tenant un parapluie trempé."


"Lilly est aussi silencieuse que moi, les yeux clos tandis qu'elle écoute tout ce qu'il se passe."


"C'est un silence agréable, relaxant même. Le même type de silence que nous avons partagé si souvent ces derniers mois."

stop music fadeout 5.0


"Pour Lilly, du moins."


"Je ne peux pas m'empêcher de penser à ce que m'a dit sa sœur, aux moments que nous avons passés ensemble depuis que je suis à Yamaku et à la façon dont on a commencé à sortir ensemble."


"Peu importe à quel point j'essaye, je n'arrive pas à comprendre Lilly. C'est comme si plus j'essayais d'imaginer ses sentiments et sa potentielle décision, plus la conclusion devenait difficile à établir."


"Je me mets à douter de l'avoir déjà comprise tout court. En fin de compte, je vais devoir lui demander, même si je voulais vraiment éviter de le faire."

show lilly basic_smile_cas_close
with charachange


li "Tu sembles silencieux aujourd'hui, Hisao."


hi "Ah bon ?"

show lilly basic_ara_cas_close
with charachange


li "Tu semblais si enthousiaste à l'idée de m'emmener en rendez-vous, j'imaginais que tu avais envie de faire quelque chose de précis."


hi "Non, pas vraiment. Je voulais juste passer du temps avec toi."

show lilly basic_weaksmile_cas_close
with charachange


li "Ah, d'accord..."


hi "C'est vrai. Il y a quelque chose."

show lilly basic_cheerful_cas_close
with charachange


"Un petit sourire s'affiche sur le visage de Lilly, sachant qu'elle vient de m'avoir. Ça rend la conversation encore plus embarrassante."


hi "C'est juste que... j'ai parlé avec Akira."

show lilly basic_surprised_cas_close
with charachange


li "Oh ?"


hi "Un problème ?"

show lilly basic_weaksmile_cas_close
with charachange


li "Vous semblez bien vous entendre, non ?"


hi "Bah, je trouve qu'elle est plutôt cool. Ça serait bien si un des professeurs était comme elle."

show lilly basic_sleepy_cas_close
with charachange

li "“Cool…”"


"Pendant un moment, j'essaye de comprendre son ton, ma bouche se tordant en un sourire alors que j'en réalise la raison."


hi "Tu ne serais pas jalouse, par hasard ?"

show lilly basic_pout_cas_close
with charachange


li "Je ne suis pas jalouse !"


"Après m'avoir autant taquiné sur le sujet lors de notre premier rendez-vous, je n'ai aucun remords à m'amuser à ses dépens cette fois."


"Cela dit, ça ne reste qu'une distraction par rapport à la vraie raison pour laquelle j'ai amené Lilly ici."


hi "Ne t'inquiète pas, c'était surtout pour parler de tout et de rien. Cela dit, il y a quelque chose qu'Akira a mentionné dont je voulais te parler."


hi "Quand tu as été voir ta famille à Inverness, elle a dit..."

show lilly basic_reminisce_cas_close
with charachange


li "Akira t'a dit que ma famille m'a invitée à les rejoindre, n'est-ce pas ?"

play music music_drama fadein 2.0


"Plusieurs secondes s'écoulent alors que j'essaye de lire l'expression de Lilly, un étrange mélange de sentiments s'affichant. Elle semble énervée, mais aussi quelque peu confuse."

show bg suburb_shanghaiint at bgleft
show lilly basic_reminisce_cas_close:
    twoleft
    ypos 1.1
with charamove

show yuukoshang neutral_up at tworight
with charaenter


yu "Hum... voilà..."


"Yuuko pose timidement nos boissons sur la table, se faisant toute petite."

hide yuukoshang
with charaexit

show bg suburb_shanghaiint at center
show lilly basic_reminisce_cas_close:
    center
    ypos 1.1
with charamove


"Alors qu'elle retourne au comptoir après un bref hochement de tête, je réalise que l'atmosphère entre Lilly et moi est tendue et que nos expressions sont pensives."

show lilly basic_displeased_cas_close
with charachange


li "Même après m'avoir dit que je devais vivre ma propre vie, elle continue d'interférer dans les pires moments..."


hi "Je ne crois pas que tu doives blâmer Akira. Elle veille juste sur toi et je comprends pourquoi elle s'inquiète sur ce coup-là."

show lilly basic_weaksmile_cas_close
with charachange


"L'irritation qu'affiche Lilly montre qu'elle essaye sans succès de masquer ce qu'elle ressent. Elle n'apprécie vraiment pas d'être coincée sur un sujet comme celui-ci."


li "Je sais, mais... je voulais juste plus de temps. Je savais que tu le saurais à un moment donné, mais..."


hi "Tu me le cachais intentionnellement ? Tu comptais faire ça pendant combien de temps ?"

show lilly basic_displeased_cas_close
with charachange


li "Comme je l'ai dit, je voulais juste plus de temps pour réfléchir. Je voulais être sûre de ma décision avant de te le dire."


hi "Tu as décidé de ce que tu allais faire, en fin de compte ?"


"Je sais ce que je veux qu'elle dise, mais une horrible sensation refuse de me quitter."

show lilly basic_sleepy_cas_close
with charachange


li "Ma famille veut vraiment que je les rejoigne et Akira y va aussi. Je pourrai toujours enseigner, que ce soit ici ou là-bas."


hi "Donc... tu pars."


hi "Tu le savais depuis combien de temps ? Je sais déjà qu'on te l'a proposé quand tu as été en Écosse, il y a un mois."

show lilly basic_concerned_cas_close
with charachange


li "Quelque... temps."


"Ma frustration atteint sa limite, le fait qu'elle ait fait ça m'affecte plus que ça ne le devrait."


"Non seulement parce qu'elle part, mais aussi parce qu'elle me l'a caché, et sans oublier qu'elle a été pendant longtemps le seul pilier solide sur lequel je pouvais compter..."


"J'ai comme l'impression que le sol sous mes pieds se craquelle, trop vite pour que je puisse m'enfuir. Peut-être que c'est moins de la frustration que du pur malaise."

hi "Lilly…"

show lilly basic_sad_cas_close
with charachange


li "Je suis désolée. J'ai juste... Je voulais juste y réfléchir plus longtemps. Je ne voulais pas profiter de toi, alors s'il te plaît—"


hi "Je sais, Lilly. Je sais. C'est juste vraiment soudain."


hi "J'imagine que ça veut dire qu'une fois que tu seras partie, on se séparera ?"


"Aussi rare que ça puisse être de sa part, elle ne sait vraiment pas quoi dire."


"Elle n'a pas l'air surprise, vu qu'elle y a déjà pensé, mais elle a plutôt l'air de ne pas du tout savoir comment gérer la situation maintenant qu'elle est face à elle."

show lilly basic_oops_cas_close
with charachange


li "O-on pourrait essayer de poursuivre une relation à longue distance. C'est de plus en plus commun de nos jours, après tout..."


"Elle baisse peu à peu la voix en parlant, montrant qu'elle n'y croit pas elle-même."

$ renpy.music.set_volume(0.5, 1.0, channel="music")
$ renpy.music.set_volume(0.05, 1.0, channel="ambient")

window hide
nvl clear
nvl show dissolve


n "\n\n\nLilly est bien trop de la vieille école pour vivre une relation sans aucune présence physique et moi aussi. Tout ce qu'on pourrait partager, ce sont nos voix de l'autre côté du monde."


n "En fin de compte, essayer de tout rationaliser est futile. Essayer de comparer tout ce qui arrive avec le futur ou le passé rend juste les choses trop difficiles à appréhender."


n "Ces instants de silence quand on marchait côte à côte, ces précieux moments qu'on a passés avec Hanako et Akira, les discussions durant les déjeuners, les fois où l'on a fait l'amour, l'aveu de nos sentiments envers l'autre..."


n "\n\n\nTout cela ne sert à rien. Juste un moment fugace dans nos jeunes vies."

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear
window show


hi "En fait on est deux enfants prétendant être adultes, hein ?"

show lilly basic_sad_cas_close
with charachange


"Un long, long silence reste en suspens entre nous. Le bruit des autres clients buvant et discutant rend la situation encore plus étrange et irréelle."


"Lilly garde la tête penchée, son expression abattue à peine visible."

stop music fadeout 4.0

show lilly basic_concerned_cas_close
with charachange


li "Je suis désolée, Hisao."


"Une simple excuse, rien de plus. Elle ne trouve visiblement rien d'autre à dire."


"Avec un long soupir, je rassemble ce qui reste de mes pensées et pose la dernière question que j'ai pour elle."


hi "Quand est-ce que tu pars ?"

show lilly basic_sad_cas_close
with charachange


li "Je vais partir avec Akira, donc ce sera dans un peu moins d'une semaine."


hi "Le début des vacances d'été ?"

show lilly basic_sleepy_cas_close
with charachange


li "Juste un peu après, oui."


"Son ton est inhabituellement lent et plat, je peux voir sur son visage qu'elle est désolée et déprimée et qu'elle essaye de le masquer dans sa voix."


"En fin de compte, je ne peux même pas tenir ma promesse d'aller à Tanabata avec elle."

stop ambient fadeout 14.0
$ ksgallery_unlock("evul hisao_teacup")
show ev hisao_teacup:
    truecenter
    zoom 0.85 subpixel True
    acdc_warp 15.0 zoom 0.8
with locationchange


"Je baisse les yeux et vois mon visage se refléter dans ma tasse de thé maintenant tiède."


"Je pensais vraiment que j'avais laissé ce genre d'expression derrière moi."


"Pendant un moment, je regarde la surface plane, essayant de me remettre de tout cela pour choisir ce que je devrais faire, que ce soit maintenant ou dans le futur."


"Mais, comme avant, cet effort est inutile."

hide ev
show lilly basic_reminisce_cas_close
with locationchange


"Je relève la tête et vois Lilly boire son thé froid sans se plaindre, le visage sombre et les épaules baissées. Elle a l'air de réfléchir et une étrange atmosphère s'immisce entre nous alors que nous nous isolons pour relativiser tout cela."


"Même quand la tasse de Lilly se retrouve presque vide, la mienne est encore pleine."


"Un long moment se passe avant que je ne remarque que la pluie s'est arrêtée de tomber à l'extérieur et que les autres clients du Shanghai sont partis."

scene bg school_dormhallway
with shorttimeskip

stop ambient
play music music_moonlight fadein 0.5


"Le froid du soir imprègne les couloirs du dortoir. En me dirigeant vers ma chambre, j'aperçois une silhouette qui n'est pas la bienvenue."

show kenji happy:
    center
    xpos 0.4
    easein 0.5 xpos 0.5
with charaenter


"La porte ouverte en face de la mienne annonce l'arrivée de mon voisin à lunettes."


ke "Hey mec, quoi de..."

show kenji tsun at center
with charachange


ke "Woah mec, tu fais une tête horrible, je crois. Tu vas bien ?"


"Il a toujours eu énormément de tact."


hi "Je... ne veux vraiment pas en parler. Il est tard."

show kenji neutral
with charachange


ke "D'accord. Pas de problème."


ke "Si tu veux en parler, je suis là, tu sais."


"Je le regarde un moment avant d'abandonner mon expression sévère et de me frotter la nuque, embarrassé par la réponse froide que je lui ai donnée."


hi "Merci, Kenji."

show kenji happy
with charachange


ke "Pas de problème. C'est à ça que servent les amis, hein ?"


hi "Ouais, t'as raison. Hum, à plus."

scene bg school_dormhisao_ni
with locationchange


"J'ouvre la porte de ma chambre et la ferme alors qu'il me fait un signe d'au revoir."

play sound sfx_doorslam


"Le bruit que fait la porte en se fermant sonne comme la fin de la vie que j'ai menée à Yamaku jusqu'à maintenant."


"Je me tiens debout dans ma chambre sombre, ne trouvant aucune réponse à ce que je peux faire à partir de maintenant."


"Qu'est-ce que je peux faire ?..."

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
stop music fadeout 2.0

scene black
with dissolve



label fr_L29:

scene bg school_scienceroom
with locationchange


"Alors que les cours touchent à leur fin, je reste simplement assis à passer le temps en regardant par la fenêtre."

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_normal fadein 2.0

window hide
nvl clear
nvl show dissolve


n "\n\nÇa fait quelques jours que Lilly m'a dit ce qu'elle comptait faire. Je n'ai pas assisté à notre déjeuner habituel depuis ce moment-là, ce n'est pas comme s'il y avait eu un intérêt à le faire."


n "Hanako a été occupée par le club journal qu'elle a rejoint récemment et a même commencé à parler à Naomi en classe de temps en temps."


n "Même Lilly, en dehors du fait qu'une rencontre entre nous deux serait gênante dans tous les cas, a été débordée par ses responsabilités en tant que déléguée à cause des vacances d'été approchant."


n "Et maintenant, elles arrivent. Après la sonnerie, les vacances d'été commenceront."


n "\n\n\nJ'imagine que je vais finir par aller voir mes parents et traîner dans mon ancienne maison, vu que ce que je comptais faire n'est plus possible maintenant."

nvl clear


n "\n\nPendant ce temps, Akira et Lilly seront en route pour l'Écosse, pour vivre le reste de leur vie."


n "Peu importe à quel point j'essaye de rationaliser le fait qu'une fois les vacances d'été commencées, ma vie retournera à l'état dans lequel elle était avant, je n'y arrive pas."


n "Tout le monde avance dans sa vie. Lilly rejoint sa famille, Akira va travailler dans l'entreprise de son père, Hanako a de nouveaux amis et hobbies, et même Yuuko avance dans ses projets d'université."


n "Même moi, j'avance, en fin de compte. Avec les notes que j'ai eues à Yamaku, même après un début difficile, le chemin pour enseigner les sciences semble clair."


n "\n\nJ'imagine que je devrais au moins être content pour cela, mais ça ne me réjouit pas plus que ça."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

window show


mi "Hicchan~ !"


"J'arrête de ruminer et tourne la tête vers la voix joyeuse, affichant l'expression la plus sereine possible."

show misha hips_smile at twoleft
show shizu behind_smile at tworight
with charaenter


"Comme je m'y attendais, Shizune est là avec Misha. J'ai comme l'impression qu'elles me veulent quelque chose."


hi "Salut Misha, Shizune. Quoi de neuf ?"

show misha hips_grin
with charachange


mi "Eh bien~..."

show misha perky_smile
with charachange


mi "Shicchan et moi pensions que~..."

show misha sign_smile
with charachange


mi "Vu qu'on est juste deux pauvres petites filles qui ont besoin d'aide avec tout le travail qui leur a été donné juste avant que les vacances commencent~..."


hi "Ok, je peux vous aider."

show misha perky_sad
with charachange


mi "Mais Hicchan, on a vraiment beso—"

stop music fadeout 0.2

show misha perky_confused
with charachange


mi "Quoi ?"


"Je crois que j'ai cassé Misha."

show shizu behind_blank
with charachange


"Même Shizune lève un sourcil alors que sa complice s'arrête sur place."

show misha hips_grin
with charachange


mi "Donc tu vas nous aider, Hicchan ?"


hi "C'est ce que je viens de dire."


"Ce n'est pas comme si j'avais mieux à faire. Peut-être que les aider dans leur travail me permettra de penser à autre chose."


"Misha semble vraiment contente de ma réponse, mais l'expression de Shizune est difficile à lire. Je me retrouve à l'éviter du regard, comme si elle semblait afficher une expression de pitié. Ça doit être mon imagination."

scene bg school_council
with shorttimeskip

play music music_daily fadein 0.5


"Ce n'est pas la première fois que je me retrouve dans la salle du conseil des étudiants. Je suis déjà venu ici à plusieurs reprises ; pour aider Lilly avec ses devoirs de déléguée, ou pour m'occuper d'un détail avec le Conseil des Étudiants même."


"Maintenant, c'est différent."

show sc_comp:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)


"Avec des papiers et dossiers éparpillés sur toutes les tables de la pièce, seul un petit ordinateur noir se distingue de ce bazar."


"Il a l'air ancien, alors j'imagine qu'il sert à archiver des informations depuis des années."

show sc_comp:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide sc_comp
with None


hi "Donc, qu'est-ce qui doit être fait aujourd'hui ? On dirait qu'il y a beaucoup de travail."

show misha hips_smile at twoleft
show shizu behind_frown at tworight
with charaenter

shi "…"


"L'expression de Shizune devient sérieuse alors qu'elle fait des signes. C'est inquiétant."

show misha hips_grin
with charachange


mi "Tout, Hicchan !"


"Mes inquiétudes n'étaient pas à la hauteur."


hi "Tu as dit... tout ?"

show shizu basic_normal
with charachange

shi "…"

show misha sign_smile
with charachange


mi "Tout ce qui se trouve sur les bureaux est ce qu'il reste à faire."

show misha perky_smile
with charachange


mi "Tout cela a besoin d'être enregistré informatiquement, c'est pour ça qu'il y a l'ordinateur portable."


hi "Et j'imagine que je vais être celui qui va le faire ?"

show shizu behind_smile
with charachange

shi "…"

show misha hips_smile
with charachange


mi "Shicchan dit qu'elle t'a vu utiliser les ordinateurs de la bibliothèque il y a quelques jours et que tu semblais vraiment à l'aise avec~."


"À l'aise avec les ordinateurs ? Je sais taper sur le clavier, j'imagine. Mais ça reste une surestimation de mes compétences."


hi "J'écrivais juste un devoir à rendre..."


hi "Attends... Shizune me regardait faire ça ?"

show shizu adjust_smug
with charachange

shi "…"

show misha sign_smile
with charachange


mi "On doit connaître ses alliés avant qu'ils ne connaissent leurs ennemis, bien sûr~."

show misha cross_grin
with charachange


mi "Woaw, c'est plutôt sage..."


"Pour une fois, ce n'est pas difficile de savoir qui a dit quoi."


"Néanmoins, ça ne semble pas valoir le coup de se disputer. S'asseoir devant un ordinateur et écrire ne semble pas bien difficile, si ça peut aider Shizune et Misha."

show shizu basic_normal
with charachange

shi "…"

show misha perky_smile
with charachange


mi "En plus, ça t'aidera à penser à autre chose~."


hi "Penser à autre chose ? À autre chose que quoi ?"

show misha perky_confused
with charachange


"Le visage de Misha n'affiche plus aucune expression alors qu'elle traduit ça pour Shizune, qui se tourne pour regarder par la fenêtre après une brève réponse."

show shizu behind_blank
with charachange

shi "…"

show misha sign_smile
with charachange

show shizu basic_normal2
with charachange


"Misha recommence immédiatement à sourire alors qu'elle me traduit ce qui a été dit. Elle était confuse j'imagine, mais il en faut plus pour perturber Shizune."

show misha cross_smile
with charachange


mi "Je me disais juste que tu voulais penser à autre chose qu'aux examens, bien sûr~."


hi "De toute façon, il faut le faire tôt ou tard. Je vais vous aider."

show misha hips_smile
with charachange


mi "C'est l'esprit, Hicchan !"




















scene bg school_council
with shorttimeskip


"Et voilà le cinquième tableau rempli et sauvegardé. Passons à celui du mois suivant..."


"Au bout d'un moment, on arrive à s'organiser."


"Shizune rassemble toutes les feuilles et les remet en ordre sur une pile à côté de moi. Pendant ce temps, Misha s'occupe de tout ce qui est travail écrit, ses stylos roses laissant une marque indélébile feuille après feuille."


"Une fois le rythme trouvé, ce n'est pas si dur. Shizune et Misha semblent gérer de la même manière que moi, communiquant sans un mot tout en travaillant avec ferveur."


"Je regarde régulièrement la feuille à côté de l'ordinateur, apparemment c'est une liste d'étudiants et leurs adresses, dont je recopie le contenu sur l'ordinateur. Je ne prête pas attention à ce que j'écris jusqu'à ce que j'arrive à un certain nom."


"Hakamichi... classe 3-3... Oh. Elle est originaire de Saitama."


"Ma curiosité est interrompue par trois légers coups à la porte."

show misha perky_smile:
    twoleft
    xpos 0.4
    easein 0.5 twoleft
with charaenter


"Misha y va rapidement pour voir qui c'est, tapant sur l'épaule de Shizune au passage pour lui laisser savoir ce qui se passe."

show misha hips_grin at twoleft
with charachange


mi "Ah, tu es là~."


hi "Mmh ? Qui est-ce ?"


"Marquant une légère pause pour entrer Shizune dans le fichier avec les autres, je regarde pour voir qui est à la porte."

stop music fadeout 0.5

show lilly invis:
    left
    xpos -0.2
with None

show bg school_council at bgright
show misha hips_grin at center
show lilly basic_weaksmile_cas at left
with dissolvecharamove


"...Lilly ?"


"Après avoir adressé un hochement de tête à Misha en guise de salutation, elle penche la tête comme elle le fait si souvent."

show lilly basic_surprised_cas
with charachange


li "Est-ce Hisao ?"


"Elle est plutôt douée pour reconnaître ma voix à la moindre phrase de ma part."


hi "Ouais, c'est moi. Euh... salut."

show lilly basic_reminisce_cas
with charachange


"L'atmosphère est légèrement tendue alors qu'elle se penche pour me saluer. Aucun de nous deux ne sait comment se comporter avec l'autre, étant donné qu'elle part dans quelques heures."


"Heureusement Shizune et Misha sont trop occupées à travailler pour s'en rendre compte."


hi "Alors... tu as du travail à faire aussi ?"

show lilly basic_sleepy_cas
with charachange


li "Malheureusement. Je suis venue aussi vite que j'ai pu, mais ma classe m'a fait une petite fête d'adieu surprise, alors j'ai dû aller me changer."


"Je regarde l'horloge de l'ordinateur. Il est presque l'heure de la fin du déjeuner, donc j'imagine que Lilly a réussi à se faire dispenser des cours de l'après-midi."


show lilly basic_weaksmile_cas
with charachange


li "J'en déduis que Shizune aussi est là ?"

play music music_shizune fadein 3.0

show shizu behind_blank at right
with charaenter

shi "…"

show misha cross_smile
with charachange


mi "Bien sûr !"

show shizu adjust_smug at right
with charachange

shi "…"

show misha sign_smile
with charachange


mi "Et j'ai été là durant toute la pause déjeuner aussi."


"Ce dernier commentaire n'était pas nécessaire. Shizune provoque Lilly, je peux le sentir."

show lilly basic_displeased_cas
with charachange


li "Je suis désolée de ne pas travailler aussi dur que toi, Shizune. Je m'efforcerai d'engager plus de valets pour faire mon travail à l'avenir."


"Et Lilly a mordu à l'hameçon, empirant les choses."

show shizu basic_frown
with charachange

shi "…"

show misha hips_frown
with charachange


mi "Mais n'es-tu pas celle qui donne toujours du travail à faire à ses camarades de classe~ ?"

show lilly basic_listen_cas
with charachange


li "La différence est qu'ils choisissent d'aider, contrairement à la prise tyrannique que tu exerces sur ta propre classe."

show shizu behind_frown
with charachange

shi "…"

show misha cross_smile
with charachange


mi "La tyrannie marche~ ! Même si on fait les choses différemment, on a toujours le même résultat, n'est-ce pas~ ?"

show lilly basic_displeased_cas
with charachange


li "C'est une école, pas un état policier. Il faudra que tu me rappelles quand tu as été élue monarque de la classe, j'en ai peur."

show shizu cross_angry
with charachange

shi "…"

show misha cross_frown
with charachange


mi "Tu dois saisir le pouvoir, ce n'est pas aussi bien si ça t'est juste donné~ ! Mais j'imagine que tu ne peux pas vraiment comprendre ça, n'est-ce pas~ ?"

show shizu adjust_angry
with charachange

shi "…"

show misha hips_smile
with charachange


mi "Tu vas aussi devoir me rappeler depuis quand les monarques se font élire."


"Lilly frémit à sa réponse. Le combo de deux coups de Shizune a percé ses défenses."

show lilly basic_displeased_cas
with charachange


li "Et pourtant avec tout ton pouvoir, tu n'as pas une seule personne qui t'aide sans que tu la forces."

show shizu behind_frustrated
with charachange

shi "…"

show misha sign_smile
with charachange


mi "Mais Hisao s'est porté volontaire~ ! Il travaille si dur, il fait ça au lieu de bêtement s'amuser, n'est-ce pas~ ?"

show lilly basic_listen_cas
with charachange


li "Tiens donc. Hisao ?"


"Ah, c'est pas bon. Je suis entre deux feux, là."


"Bien que ça me fasse mal de faire ça, la vérité a au moins une chance de tout arrêter maintenant."


hi "C'est bon, Lilly, elles ne m'ont pas forcé ou quoi que ce soit."

show lilly basic_displeased_cas
with charachange


"Lilly affiche une grimace de désapprobation, émettant silencieusement de forts sentiments de mécontentement dans ma direction."


"Elle peut être effrayante quand elle le veut, bien qu'heureusement ça ne soit pas souvent."

show shizu cross_angry
with charachange

shi "…"

show misha hips_frown
with charachange


mi "Hicchan, tu dis ça comme si ça arrivait souvent~..."


hi "C'est pas le cas ?"


hi "En fin de compte, ça importe peu, tant que tout est fait. Finissons juste notre boulot qu'on puisse rentrer chez nous."

hide shizu
with charaexit

hide lilly
with charaexit

hide misha
with charaexit


"Shizune renifle ironiquement et retourne aux papiers en face d'elle, pendant que Lilly soupire et trouve son chemin en suivant les placards alignés contre le mur."


"Ça semble être la première fois que j'arrive à désamorcer une de ces situations, mais le cessez-le-feu, construit autour d'une peur et d'un respect mutuel me fait plus penser à la guerre froide qu'à une réelle paix."


"Je ne peux pas récolter tous les mérites cela dit. Le fait que Lilly ait abandonné si facilement a sûrement affecté Shizune."

show bg school_council at center
with charamove

show lilly basic_listen_cas at center
with charaenter


"Avant de retourner à mon travail, je remarque que Lilly lève les bras pour attraper quelque chose au-dessus de l'armoire. Je lui offrirais bien mon aide, mais sa taille lui suffit largement pour l'attraper."

show lilly basic_displeased_cas:
    ypos 1.15
with dissolvecharamove


"Une fois qu'elle pose l'étrange engin sur le bureau à côté de moi, je réalise ce que c'est... plus ou moins... alors qu'elle enlève le cache vert qui le couvre et s'assoit."

show brailler:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)


"À première vue, ça semble être une vieille machine à écrire bleue, mais il ne me faut pas longtemps pour réaliser qu'elle n'est pas ordinaire."


"Elle a moins de touches qu'une machine normale et les touches n'ont pas de lettres imprimées dessus. Seulement des petits points noirs en braille, ce qui me donne une idée du but de cette machine."


hi "Machine à écrire pour aveugles ?"

show lilly basic_smile_cas
with None

show brailler:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide brailler
with None


li "Oh, ça ? Eh bien, tu n'es pas loin."


li "Ça s'appelle un brailleur Perkins, mais c'est plus ou moins une machine à écrire pour aveugles, oui. Ça imprime le braille sur la page au lieu du texte, c'est pourquoi il a moins de touches."


hi "Oh... c'est vraiment pratique."

show lilly basic_cheerful_cas
with charachange


"Ma curiosité la fait sourire. Je dois admettre que ça m'a intrigué."

hide lilly
with charaexit


"Sans rien dire d'autre, nous retournons tous les deux à nos tâches. Le claquement bruyant du brailleur de Lilly et le bruit de ma frappe sur le vieil ordinateur portable emplissent la pièce."


"C'est une bonne ambiance, vraiment. Tout le monde sait ce qu'il a à faire, Lilly et moi sommes assis l'un à côté de l'autre, sans dire un mot alors que nous travaillons."


"De la nostalgie. C'est ce que je ressens."


"C'est plaisant, mais quelque peu gâché par l'idée que notre temps ensemble approche à sa fin."

show lilly basic_smile_cas:
    center
    ypos 1.15
with charaenter


li "Excuse-moi, Misha ?"

show bg school_council at bgleft
show lilly basic_smile_cas:
    twoleft
    ypos 1.15
with charamove

show misha hips_smile at tworight
with charaenter


"Pour s'adresser correctement à elle, Misha ressort du placard dans lequel elle fouillait, bien que Lilly soit aveugle. Pendant un moment je trouve cela étrange, mais je réalise que je fais exactement pareil."


mi "Ouaip ?"

show lilly basic_weaksmile_cas
with charachange


li "Pourrais-tu demander à Shizune où sont les registres de présence de la classe 3-2 ? Je crois qu'ils ont été déplacés."

show misha hips_grin
with charachange


mi "Okidoki !"

hide misha
with charaexit

stop music fadeout 8.0


"Et sur ce, elle s'approche de Shizune, qui travaille à une table derrière nous."


"La connaissance qu'a Lilly de la salle du conseil et l'efficacité avec laquelle elle travaille me rappellent que Shizune, Misha et elles travaillaient ensemble au Conseil des Étudiants avant."


"Peut-être que c'est une fin appropriée pour elle à Yamaku, travailler comme elle l'a toujours fait, entourée de ceux qu'elle aimait, ou du moins, appréciait."


"Je lève les yeux et je suis surpris de voir Shizune fouiller dans un tiroir, plutôt que ce soit Misha."

show shizu behind_blank at tworight
with charaenter


"Elle finit par en sortir un dossier, entièrement vierge si ce n'est les points en relief visibles sur sa couverture, et le tend à Lilly."


"Lilly glisse une main dessus pour vérifier ce que c'est, ses doigts passant sur le braille, confirmant que c'est ce qu'elle a demandé."

show lilly basic_smile_cas
with charachange


li "Merci Misha."


"Aucune réponse."

show shizu behind_smile
with charachange


"Aucune réponse, si ce n'est une étrange grimace... non... un sourire... sur le visage de Shizune."

show ev lilly_sheets:
    truecenter
    zoom 1.05 subpixel True
    easein 10.0 zoom 1.0
with whiteout


"Quelques secondes se passent avant que Lilly remarque que ce n'est pas Misha derrière elle, mais Shizune. Son moment de surprise est remplacé par un léger sourire."


"Pendant quelques instants, la pièce n'est plus aussi vide qu'elle l'était."


"Finalement, Shizune retourne à son poste et Lilly recommence à taper."


"Ça n'a duré que quelques secondes, mais on dirait que des années de communication ont eu lieu pendant cet échange silencieux."

scene bg school_council_ss at right
with shorttimeskip

play music music_tranquil fadein 3.0


hi "Voilà, fini."


"Je penche la tête en arrière et me frotte les yeux. Regarder ce petit écran pendant si longtemps a eu son effet."

show lilly basic_smile_cas_ss:
    center
    ypos 1.15
with charaenter


li "Excellent timing, la seule chose qu'il me reste à faire, c'est de classer ça et j'aurai fini aussi."


hi "Bien. Je peux ranger le brailleur pendant que tu fais ça."

show lilly basic_smileclosed_cas_ss
with charachange


li "Merci, Hisao."


hi "Misha, vous avez bientôt fini ?"


"Je regarde autour de moi alors que je range le brailleur et les vois à la porte, attendant que nous finissions."

scene bg school_council_ss at left
show misha hips_smile_ss at center
show shizu behind_blank_ss at right
show lilly basic_smileclosed_cas_ss at left
with shorttimeskip


"Sans perdre de temps, nous finissons tout et les rejoignons."


hi "Merci d'avoir attendu."

show misha hips_grin_ss
with charachange


mi "On ne pouvait pas partir sans toi, Hicchan, tu nous as beaucoup aidées !"

show shizu behind_smile_ss
with charachange


"Shizune hoche la tête, satisfaite de mes efforts."


hi "J'imagine que... c'était ton dernier travail en tant que déléguée."

show lilly basic_smile_cas_ss
with charachange


li "Oui."

show misha perky_sad_ss
with charachange


mi "Tu me manqueras Lilly. C'était fun de travailler avec toi."

show lilly basic_weaksmile_cas_ss
with charachange


li "Merci, Misha. C'était bien de travailler avec toi... et Shizune."

show shizu basic_normal_ss
with charachange


"Shizune réfléchit un moment avant de formuler sa réponse. Ce n'est pas comme si elle parlait souvent sans réfléchir, c'est même plutôt l'inverse, mais cette fois encore plus que d'habitude."

show shizu adjust_smug_ss
with charachange

shi "…"

show misha perky_confused_ss
with charachange


"Misha semble un peu surprise avant de traduire."

show misha hips_smile_ss
with charachange


mi "Shizune dit... qu'elle espère que tu travailleras mieux là-bas que tu ne l'as fait ici."

show lilly basic_giggle_cas_ss
with charachange


"Loin de mal le prendre, Lilly rit, la main devant la bouche."

show lilly basic_smileclosed_cas_ss
with charachange


li "Dans ce cas, s'il te plaît dis à Shizune d'être un peu plus compréhensive envers ceux qui restent ici."


"Compétitives jusqu'à la fin. Peut-être que Shizune et Lilly ne sont pas si différentes après tout."

show shizu behind_smile_ss
with charachange

shi "…"

show misha hips_grin_ss
with charachange


mi "Shicchan dit qu'elle fera en sorte de vérifier que tu tiens ta promesse."

show lilly basic_cheerful_cas_ss
with charachange


li "C'est quand elle veut."

show lilly basic_smile_cas_ss
with charachange


li "Je ferais mieux d'y aller. Au revoir, Shizune. Au revoir, Misha."

show lilly basic_smileclosed_cas_close_ss
with characlose


li "Hisao ?"


"Lilly passe son bras autour du mien, se dispensant de sa canne pour se guider. Avec un hochement de tête en direction des deux autres filles, nous passons la porte et nous dirigeons vers les terrains de l'école."


"Alors que je me tourne pour dire au revoir, je remarque que Shizune regarde attentivement Lilly. Elles peuvent ne pas beaucoup s'aimer, elles restent de la même famille."

scene bg school_courtyard_ss
with locationskip


hi "Tu t'es occupée de tous tes papiers, alors ?"

show lilly basic_smileclosed_cas_ss at center
with charaenter


li "Oui, ils ont été remplis et envoyés."


hi "Toujours aussi sérieuse, hein ?"

show lilly basic_weaksmile_cas_ss
with charachange

stop music fadeout 4.0


"Elle sourit du compliment, mais j'ai l'impression que sa joie n'est qu'une façade et qu'elle sait tout ce qu'elle va laisser derrière elle."


"Ça me rappelle la première fois où je l'ai rencontrée, toujours souriante, toujours quelque peu distante vis-à-vis de tout le monde."


"Même maintenant, elle est toujours un peu comme ça, surtout envers ceux qu'elle ne côtoie pas beaucoup. J'avais espéré que notre temps ensemble aurait changé cela."

scene bg school_gardens_ss
with locationchange


"Notre rythme ralentit alors que nous arrivons aux jardins de l'école, totalement déserts."

show lilly basic_weaksmile_cas_ss at center
with charaenter


li "Hisao ? Quelque chose ne..."

play music music_comfort

show lilly basic_surprised_cas_close_ss
with vpunch


"Lilly s'interrompt alors que je me tourne et passe mes bras autour d'elle, la serrant fort contre moi. Je ne suis peut-être pas habitué aux actions impulsives, mais je veux juste être contre elle, même si c'est pour la dernière fois."


"Tous les autres étudiants sont retournés aux dortoirs ou chez eux et maintenant, seul le bruit du vent sur les feuilles se fait entendre."

show ev lilly_touch_cas
with charachange


"Alors que je me recule, je peux voir qu'elle n'affiche plus son sourire habituel."


"Elle hésite à retirer sa main, ne voulant pas me lâcher, mais n'osant pas."


"Elle fait de son mieux, mais je vois qu'elle tremble légèrement. Lilly est peut-être capable de se contrôler généralement, mais là, même elle n'est pas capable de garder son calme."


"C'est la femme que j'en suis venu à aimer, mais aussi celle qui va, très bientôt, quitter le pays pour toujours."


li "Je suis désolée, Hisao."


hi "Ce n'est pas grave. Tu as ta propre vie à mener."

scene bg school_girlsdormhall
with shorttimeskip


"Nous marchons le long du couloir du dortoir des filles, main dans la main, nos émotions grandement réprimées. Néanmoins, nous nous tenons la main bien plus fort qu'avant."


"Des voix étouffées peuvent être entendues depuis la chambre de Lilly mais il n'est pas difficile de savoir à qui elles sont."

scene bg school_dormlilly

show hanako invis at tworight
show lilly invis at twoleft
with locationchange

show lilly basic_weaksmile_cas at twoleft
show hanako emb_downsad:
    xpos 0.4 xanchor 0.5
with dissolvecharamove

show lilly basic_surprised_cas
with vpunch


"Au moment où elle ouvre la porte, Hanako arrive en courant et serre Lilly dans ses bras, la prenant par surprise."


ha "Lilly ! Lilly !"

show lilly basic_oops_cas
with charachange


li "Ha-Hanako... ?"

show hanako emb_downtimid
with charachange


ha "Tu vas me manquer... Lilly..."

show lilly basic_weaksmile_cas
with charachange


"Comme je pouvais m'y attendre, elle a les larmes aux yeux. En réponse, Lilly frotte doucement les cheveux de Hanako, puis recule et lui adresse un sourire chaleureux pour la rassurer."

show akira invis:
    right
    ypos 1.15
with None

show akira basic_lost at right
with dissolvecharamove


"Regardant derrière Hanako, je peux voir Akira se lever du lit de Lilly et se frotter la tête."

show akira basic_smile
with charachange


"Ses yeux se dirigent vers moi, elle m'adresse un petit sourire forcé. J'essaye de lui retourner un sourire plus naturel, mais je doute que le résultat soit probant."

show akira basic_boo
with charachange


aki "Bon, tout est réglé ? Tu as réussi à te retenir de tuer Shizune ?"

show lilly basic_giggle_cas
with charachange


"Le commentaire fait rire sa sœur."


li "Oui, j'ai tout réglé, et oui, j'ai réussi à me retenir. Tu as préparé tout ce qu'il te fallait ?"

show akira basic_smile
with charachange


aki "J'ai deux sacs ici, mais le reste est toujours à la maison des Hakamichi. Je peux aller les récupérer en attendant le vol de demain soir, cela dit."


"Akira tapote le dessus de deux gros sacs de voyage. Elle est probablement venue pour aider à faire les valises et s'assurer que tout est en ordre du côté de Lilly, avant de partir avec elle."

show hanako cover_worry at center
with dissolvecharamove


ha "Lilly... tu t'en sortiras... là-bas ?"

show lilly basic_smileclosed_cas
with charachange


li "Ça ira, je t'assure. J'aurai Akira avec moi après tout, tu sais que je peux compter sur elle."

show hanako basic_worry
with charachange


ha "Mais..."

show lilly basic_smile_cas
with charachange


li "Ne t'inquiète pas, Hanako. J'ai ton numéro, donc on peut continuer de se parler. Et avec l'aide d'Akira, je peux t'envoyer des mails aussi."

show akira basic_boo
with charachange


aki "Hey, ne te sers pas de moi juste parce que tu ne veux pas apprendre à utiliser un ordinateur."

show lilly basic_giggle_cas
show hanako basic_smile
with charachange


"Hanako et Lilly rient toutes les deux brièvement, détendant un peu l'atmosphère."

show lilly basic_smileclosed_cas
with charachange


li "Ça marche pour toi aussi, Hisao. Je te promets de garder contact avec toi depuis l'Écosse."


hi "Je sais. Je n'en espérais pas moins."


"Elle est gentille de faire cela, mais on sait tous les deux que ça revient à rompre. Aucun de nous n'a l'illusion qu'on puisse gérer une relation à distance."


"Après la fin de la discussion, nous partons tous les quatre pour une longue marche solennelle jusqu'au portail de l'école."

scene bg school_gate_ni at bgleft
with shorttimeskip


"Les nombreuses lampes éparpillées autour de Yamaku n'arrivent pas à bien éclairer le noir total qui règne dehors."


"J'aperçois une voiture garée sur le trottoir juste devant l'école, le noir brillant de celle-ci reflétant la lueur des lampadaires. J'en discute avec Akira dans un souci d'alléger un peu l'ambiance."


hi "C'est ta voiture ? C'est quoi ?"

show akira basic_smile_ni at center
with charaenter


aki "Tu n'y connais pas grand-chose en voitures, hein ? C'est une Lancer Evo. Robuste et rapide."


"Au moins, sa remarque n'est pas fausse. Ça ne m'a jamais intéressé."

show akira basic_resigned_ni
with charachange


"Elle pousse un petit soupir."

show akira basic_lost_ni
with charachange


aki "C'était une bonne voiture. Dommage que je doive la laisser demain, tout comme la maison de vacances. Vous étiez les derniers à la visiter avant qu'elle ne change de propriétaire."


"Abandonnant ma tentative ratée de changer de sujet, je regarde Hanako et Lilly, qui sont derrière nous."

show akira basic_lost_ni at tworight
show bg school_gate_ni at center
with charamove

show hanako emb_downtimid_ni:
    xpos 0.4 xanchor 0.5
show lilly basic_weaksmile_cas_ni at twoleft
with charaenter


"En théorie, Hanako devrait guider Lilly, mais en réalité c'est plutôt l'inverse, Hanako se cramponnant au bras de Lilly."


"C'est un peu déprimant."

show akira basic_resigned_ni
with charachange


aki "Bon... On y est."

show lilly basic_reminisce_cas_ni
with charachange


li "Oui."


"Bien qu'il soit temps de faire les adieux, personne ne veut commencer. Comme si le fait que personne ne parle allait les empêcher de partir."

show hanako emb_downsad_ni
with charachange


ha "Lilly... tu dois vraiment y aller ?"

show lilly basic_concerned_cas_ni
with charachange


li "Je suis désolée, Hanako. Je ne partirai pas pour toujours tu sais. Je peux toujours t'appeler. Et Hisao sera là aussi."


"Je hoche la tête, mais Hanako se contente de serrer encore plus le bras de Lilly."


"Après avoir passé autant de temps sans qu'elle ait quelqu'un qu'elle puisse considérer comme sa famille, ce doit être atroce de devoir dire au revoir à la seule personne qu'elle pouvait voir comme telle."

show lilly basic_sad_cas_ni
with charachange


"Lilly laisse échapper un long soupir triste. Tout ce qu'Akira et moi pouvons faire, c'est regarder la scène. La seule personne pouvant faire quoi que ce soit étant Lilly."


"Finalement, Lilly desserre son bras de la prise de Hanako et l'attrape par les épaules, d'un air sérieux que je l'ai rarement vu arborer."

show lilly basic_reminisce_cas_ni
with charachange


li "Hanako, tu te rappelles la première fois où nous nous sommes rencontrées ?"

show lilly basic_weaksmile_cas_ni
with charachange


li "Tu es venue dans ma chambre pour la première fois après avoir entendu par mégarde un ami me consoler, et tu n'as pas dit un seul mot de toute la soirée. Même après que j'ai versé le thé et parlé, tu es simplement restée là à écouter."


li "Il a fallu de nombreuses soirées dans le silence avant que tu ne t'ouvres à moi, mais quand tu l'as fait, ça a été un des moments les plus heureux de ma vie."

show lilly basic_sleepy_cas_ni
with charachange


li "Je ne suis pas devenue amie avec toi parce que j'avais pitié, Hanako. Je suis devenue ton amie parce que je savais que tu ne te cachais pas juste de moi, mais de tout le monde."


li "Ton ambition, ta personnalité, ce que tu aimais... Je ne savais rien de tout ça, personne ne le savait."

show lilly basic_weaksmile_cas_ni
with charachange


li "Alors que tu te montrais à moi, j'ai commencé à réaliser la personne que tu étais et je suis devenue sûre que notre rencontre était un moment spécial."

show hanako emb_blushtimid_ni
with charachange


ha "Mais je..."


"Lilly interrompt Hanako en posant sa main sur son visage, lui enlevant la frange de devant celui-ci, pour poser doucement ses lèvres sur son front."

show lilly basic_smile_cas_ni
with charachange


"Alors qu'elle se redresse, laissant Hanako sans voix et les larmes aux yeux, Lilly affiche un grand sourire."


li "Je crois que tu es quelqu'un de magnifique, Hanako. Et je suis certaine que tu deviendras une femme forte et confiante."


li "Tu es ma très chère amie et quelqu'un que j'aime beaucoup. Tout comme Hisao, je ne t'oublierai pas tant que je vivrai."

show lilly basic_smileclosed_cas_ni
with charachange


li "Je pars peut-être, mais tu as ta propre vie à mener. Tout comme moi, tu as tes amis, des hobbies et tes propres espoirs après le diplôme. Je veux que tu te dévoues à eux, même après mon départ."

show lilly basic_smile_cas_ni
with charachange


li "C'est pour cela que je crois que ça ira. Parce que tu es toi, que tu as ta propre vie. Tu me l'as prouvé."

show hanako emb_downtimid_ni
with charachange


"Hanako baisse la tête, embarrassée, et acquiesce en même temps."


ha "Je... je comprends..."


ha "Je sais que je dois te dire au revoir... Je sais que tu as ta propre route à suivre..."

show hanako emb_smile_ni
with charachange


ha "Mais... merci, Lilly. Pour tout."

show lilly basic_reminisce_cas_ni
with charachange


li "Merci à toi, Hanako. Ça ira ?"


"Quelques secondes s'écoulent avant qu'elle ne réponde."

show hanako cover_smile_ni
with charachange


ha "Ça ira."

show lilly basic_smile_cas_ni
with charachange


"Lilly sourit, sans doute soulagée."

show lilly basic_smileclosed_cas_ni
with charachange


li "Ça me rend heureuse alors. Au revoir."

show hanako basic_bashful_ni
with charachange


ha "Au revoir... Lilly."

show lilly basic_weaksmile_cas_ni
with charachange


li "Au revoir à toi aussi, Hisao."


hi "Au revoir. Tu vas me manquer."

show lilly basic_weaksmile_cas_close_ni
with characlose


"Elle s'avance vers moi. Sa main droite, tendue dans ma direction, se pose sur mon épaule."


"Sa main gauche s'approche lentement de mon visage et prend ma joue dans sa paume."

show lilly basic_smile_cas_close_ni
with charachange


"Pendant un moment elle reste là, à tenir mon visage, ses doigts bougeant légèrement pour en mesurer les contours. D'habitude sa main serait chaude en faisant une chose pareille, mais l'air de la nuit rend sa peau quelque peu froide."


"Je ne sais pas vraiment combien de temps on reste comme ça, ses yeux voilés juste devant les miens alors qu'elle affiche un sourire mélancolique, presque distant. Finalement, je prends sa main dans la mienne."


"C'est difficile à faire, mais avec un léger soupir, je retire doucement sa main de ma joue."


hi "J'espère que tu auras une longue et heureuse vie, Lilly. Peu importe où tu iras."

show lilly basic_weaksmile_cas_close_ni
with charachange


li "Merci. Je m'y appliquerai."


"Elle respire à fond, tremblant un peu, avant de se tourner vers Akira."

show lilly back_sad_cas_close_ni at twoleft
with charachange


li "Akira..."

show akira basic_lost_ni
with charachange


aki "D'accord."

show hanako basic_bashful_ni at left
show lilly back_sad_cas_ni at center
show bg school_gate_ni at right
with dissolvecharamove


"Avec un hochement de tête, elle prend la main de Lilly et commence à la guider jusqu'à la voiture. Elles marchent lentement et de manière droite, comme si leurs mouvements avaient été révisés à l'avance."


"C'est étrange de voir ça, quelqu'un partir de Yamaku. Ce sentiment me rappelle la première fois que j'ai passé ce grand portail en fer noir. Il m'a toujours paru trop pompeux pour ce qu'il est."


"Alors qu'elles partent, nous sommes tous conscients que nos vies changent irréversiblement. Je me suis toujours dit que je prendrais la vie comme elle vient, mais tout change si vite, si soudainement."


"En fin de compte, Lilly est une partie irremplaçable de ma vie et de celle de Hanako."


"Le bruit que fait Akira en ouvrant la porte passager pour Lilly me sort de ma torpeur, Akira nous faisant signe alors que Lilly monte."

show akira basic_smile_ni
with charachange


aki "À plus les gars ! Prenez soin de vous !"

show lilly basic_weaksmile_cas_ni
with charachange


li "Au revoir Hanako, au revoir Hisao !"

show hanako cover_smile_ni
with charachange


"La main de Hanako se lève rapidement, son visage rougi par la séance d'adieux."


ha "Au revoir Lilly ! Au revoir !"


hi "À plus Akira, au revoir Lilly !"

hide lilly
hide akira
with charaexit


"La porte se ferme alors que nous affichons tous un grand visage égayé. Akira monte dans la voiture et la démarre rapidement."


"La main de Lilly peut être aperçue à travers la vitre teintée alors que nous agitons les mains aussi."


"Comme à chaque fois que j'ai pu le faire, je ne comprends pas vraiment pourquoi Hanako ou moi lui faisons signe alors qu'elle ne peut pas le voir. Mais ça importe peu."


"Meme après que la voiture noire et brillante ait disparu de notre vue dans la nuit noire, nous continuons de faire des signes à Akira et Lilly."

stop music fadeout 5.0


"Et... elles sont parties."

show bg school_gate_ni at center
show hanako basic_normal_ni at center
with dissolvecharamove


"Un étrange calme s'empare de nous alors que nos mains se repositionnent le long de nos corps."


"Je ne sais pas vraiment ce que je devrais faire, ou ressentir. En fin de compte, on se tient là, regardant là où la voiture a disparu."


ha "Au revoir... Lilly."

show hanako basic_normal_close_ni
with characlose


"La seule chose que je peux faire, pour répondre à son triste au revoir, c'est placer une main sur son épaule."

show hanako basic_distant_close_ni
with charachange


"Elle me regarde un moment avant de regarder dans le vide, s'assurant que je suis toujours avec elle."


"Ce que nous allons faire à partir de maintenant ne semble pas si obscur. Nous avons nos propres ambitions, comme Lilly l'a dit."


"Mais même avec ça, j'ai l'impression qu'il manque quelque chose dans nos vies maintenant. Quelque chose qui ne sera jamais remplacé."


window hide Dissolve(1.0)
$ suppress_window_before_timeskip = True

scene black
with Dissolve(2.0)



label fr_L30:



scene bg school_hallway2
with locationchange

play music music_daily fadein 1.0


"Le clac du clapet de téléphone portable fait contraste avec le bruit ambiant audible à l'extérieur de la bibliothèque."


"C'est le premier jour des vacances d'été. Un moment qui semble toujours trop loin mais qui est maintenant arrivé. Et c'est encore plus visible à cause de l'absence des élèves de l'école."


"La plupart des étudiants sont rentrés chez eux pour passer les vacances avec leur famille. Les seuls qui restent discutent entre eux, en général de ce qu'ils prévoient de faire dans les semaines à venir."


"Profiter que la bibliothèque scolaire soit ouverte les premiers jours des vacances me donne l'impression d'être à part."


"Parfois, quelques élèves passent pour déposer les livres qu'ils avaient empruntés ou pour passer le temps, en attendant que leurs parents viennent les chercher."


"Et grâce à un coup de fil de mes parents qui m'a réveillé alors que je faisais une sieste dans un pouf au fond la bibliothèque, j'appartiens maintenant à la seconde catégorie."


"Remettant mon téléphone dans ma poche, me rappelant cette fois de le mettre en silencieux, je retourne dans la bibliothèque."

scene bg school_library_ss
with locationchange


"Je me sens nostalgique. Comme quand Lilly m'a emmené pour la première fois à la bibliothèque, un coucher de soleil inonde la pièce alors que Hanako est assise dans un pouf en lisant un livre et que Yuuko s'agite derrière le comptoir."


"Hanako est beaucoup plus silencieuse depuis hier, mais je ne peux pas lui en vouloir."


"Je n'étais pas le seul à dépendre de Lilly, après tout."


"Je retourne en silence vers le pouf où j'étais assis avant, prenant soin de ne pas faire de bruit."

scene ev hana_library
with locationchange

show ev hana_library_read
with charachange


"Le bruit que fait le pouf lorsque je m'assois dessus fait que Hanako regarde dans ma direction, mais juste une seconde."


"J'ai le sentiment que Hanako n'est pas silencieuse juste à cause du départ de Lilly."


"Elle semble plus concentrée et calme que ce que j'aurais pensé. Peut-être que c'est dû à son désir de gérer le départ de Lilly plutôt que d'être juste déprimée. Ça me rend fier d'elle."


hi "Dis Hanako ?"

show ev hana_library
with charachange


ha "O-oui ?"


hi "Toujours partante pour ton projet de voyage ?"


"Elle m'adresse un hochement de tête déterminé."


ha "Je partirai dans un jour ou deux. Naomi a décidé de venir aussi."


hi "Woaw, c'est bientôt. Vous allez où en premier ?"


ha "Je crois qu'on ira d'abord au nord... puis on fera une boucle vers le sud."


hi "Donc... Tu vas à Hokkaido en premier ?"


"Elle hoche encore la tête, plus doucement. La signification de cet endroit ne nous a pas échappé."


hi "Tu sais comment tu vas faire pour les frais de voyage et le reste ?"


ha "Ouais, je me suis arrangée. Je crois que ça ira. Naomi a dit que c'est réglé de son côté aussi."


hi "Tu sais que si tu as besoin de quoi que ce soit, tu m'appelles hein ? Je t'ai donné mon numéro l'autre fois. Hésite pas, à n'importe quelle heure."

show ev hana_library_smile
with charachange


"Elle me sourit, ce qui en soi est une petite victoire personnelle."


ha "Je sais."


ha "M-merci... Hisao."


"Peut-être que Lilly avait raison. Bien que je puisse offrir mon aide à Hanako, j'ai l'impression qu'elle n'en a peut-être pas besoin."


"Elle a vraiment grandi."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve


n "\n\n\nLes plans de Hanako pour les vacances sont complètements différents des miens. Je me contente de suivre la suggestion de mes parents, de rester avec eux."


n "Les vacances m'ont toujours moins excité que la plupart des gens, donc peut-être que c'est juste comme avant."


n "\nAvant ma crise cardiaque, j'ai tellement toujours vécu sans but que les vacances n'étaient pas bien différentes de ma vie de tous les jours."


n "Après l'école je traînais en ville, souvent avec des amis, avant de rentrer à la maison pour manger avec généralement l'un de mes parents, mais rarement les deux."


n "Leurs horaires de travail ne leur laissaient pas beaucoup de temps libre, et si je rentrais directement après les cours je finissais par m'ennuyer. J'étais un pur enfant de la ville."

nvl clear


n "\n\n\nDepuis que je suis venu à Yamaku, j'ai l'impression d'avoir fondamentalement changé en tant que personne. Cet appel de mes parents me l'a confirmé."


n "Bien qu'avant j'avais un niveau d'indépendance normal pour un adolescent, c'est-à-dire pas énorme, mes parents ont été plus que contents d'entendre que maintenant je sais m'occuper de moi."


n "Laver, cuisiner, nettoyer, tout ceci additionné aux autres corvées dont je dois m'acquitter n'ayant plus mes parents avec moi... Ce sont juste des petites choses auxquelles j'ai su m'habituer, sans trop de problème."


n "\nQuand j'y pense, j'ai toujours dépendu d'eux, même s'ils n'étaient pas souvent à la maison. Dire que je n'ai jamais dépendu de qui que ce soit après avoir emménagé à Yamaku serait faux, cela dit."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve
window show


yu "Euh... excuse-moi..."

stop music fadeout 3.0

scene bg school_library_ss
show yuuko worried_down_ss at center
with locationchange


"Nous levons tous les deux la tête vers la silhouette embarrassée en face de nous. Certaines choses ne changent jamais."

show yuuko worried_up_ss
with charachange


yu "C'est presque l'heure de la fermeture, alors euh..."


"Ah oui. J'avais oublié que la bibliothèque fermait plus tôt pendant les vacances."


"Hanako et moi nous levons et reposons les livres sur l'étagère derrière nous. Le fait que nos goûts en matière de livres soient similaires est pratique parfois."


"Avec un geste envers Yuuko pour s'excuser d'être aussi longue, Hanako part la première."

show bg school_library_ss at bgleft
show yuuko worried_down_ss at twoleft
with dissolvecharamove

show hanako basic_normal_ss at tworight
with charaenter


ha "À demain, Hisao."


hi "À demain."

hide hanako
with charaexit


"Et sur ce, elle passe les grandes portes en bois de la bibliothèque."

play music music_happiness fadein 3.0

show bg school_library_ss at center
show yuuko neutral_down_ss at center
with dissolvecharamove


yu "C'est quelqu'un de discret, hein ?"


"J'imagine que je devrais m'étonner qu'un membre du personnel donne son avis comme ça, mais après avoir appris à connaître Yuuko, ce n'est pas bien étonnant. Elle s'approche plus d'une amie que d'une personne d'autorité, de mon point de vue."


hi "Ouais, elle est comme ça."


hi "Elle a plus confiance en elle ces derniers jours, cela dit."

show yuuko smile_down_ss
with charachange


yu "Je ne la connais pas aussi bien que toi, mais je suis d'accord. Je suis contente de la voir parler à des gens ici, elle ne faisait pas ça avant."


hi "Dis, Yuuko... tu es au courant pour le départ de Lilly, non ?"

show yuuko worried_down_ss
with charachange


yu "Elle me l'a dit il y a quelques jours. Ça doit être dur, laisser quelqu'un derrière elle comme elle le fait."


"Elle se retourne rapidement vers moi après avoir dit ça, se rappelant sûrement que je l'ai déjà consultée pour des conseils au sujet de ma relation avec Lilly auparavant."

show yuuko worried_up_ss
with charachange


yu "Ça va aller toi ?"


"C'est... une question difficile. C'est une chose à laquelle je ne préfère pas penser pour l'instant, il y a des choses plus urgentes."


hi "Quelque chose ne tourne pas rond dans tout cela, tu ne crois pas ?"


"Yuuko semble réfléchir un moment, se grattant le visage inconsciemment de diverses manières pendant ce temps."

show yuuko worried_down_ss
with charachange


yu "Je ne crois pas la connaître assez pour porter ce genre de jugements."



yu "Désolée, je ne peux pas t'aider."


hi "Nan t'embête pas. Je pense plus ou moins à voix haute."


"Je soupire profondément et me gratte la tête, frustré."


hi "Il y a tant de choses qui arrivent sans que je puisse les contrôler... j'ai l'impression d'être submergé."

show yuuko neutral_down_ss
with charachange


yu "Je crois que tout le monde passe par des périodes comme ça."


yu "Ce qui est important, c'est de te concentrer sur ce que tu peux faire, plutôt que sur ce que tu ne peux pas faire. Du moins, c'est comme ça que je le vois."

show yuuko smile_down_ss
with charachange


yu "Si je ne pensais pas comme ça, je ne crois pas que j'arriverais à gérer ma vie telle qu'elle est."


"Elle dit ça avec un sourire et un ton léger, mais elle est vraiment sérieuse. Être pris entre deux travails comme ça, juste pour espérer avoir assez d'argent pour vivre et aller à l'université, doit être épuisant."


"Peut-être que c'est pourquoi, venant d'elle, ça semble avoir plus de sens que de la part de quelqu'un d'autre."


hi "Tu dois avoir raison sur ce point."


hi "Merci encore pour tes conseils, Yuuko."

show yuuko smile_down_ss:
    ease 0.5 ypos 1.2
with None

show yuuko closedhappy_down_ss:
    ease 0.5 ypos 1.2
with charachange

with Pause(0.2)

show yuuko closedhappy_down_ss:
    ease 0.5 ypos 1.0
    linear 0.5 alpha 0.0
with charamove


"Elle sourit et retourne derrière le comptoir où elle passe la plupart de son temps."

stop music fadeout 2.0

scene bg school_dormhisao_ni
with shorttimeskip


"Les petites ailes de la grue en carton dans mes mains sont à peine visibles dans la pénombre de ma chambre, où seul un petit clair de lune passe entre les rideaux."

show origami_hand:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with None

show origami_hand:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
show bg school_dormhisao_blurred_ni
with Dissolve (1.0)

play music music_twinkle fadein 10.0


"Je m'étends dans le noir pendant un long moment, regardant le petit oiseau en origami."


"Beaucoup de choses sont arrivées depuis que Lilly me l'a fait, mais en même temps, peu ont changé."


"Par rapport aux autres, je suis de retour à la case départ. J'ai peut-être une idée de la direction que va prendre ma vie, mais ça affecte peu ma vie actuelle."


"Hanako a changé, ça je le sais. Ça me fait penser que je n'ai aucune excuse pour être comme ça, vu que même dans sa situation, elle a su évoluer."


"Lilly, cela dit..."


"Je tourne l'oiseau entre mes doigts, le regardant sous un autre angle."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve


n "\n\nLa première fois que je l'ai rencontrée, elle semblait quelque peu distante. Ses actions étaient toujours mesurées et précises et son attitude calme et posée lui donnait une aura de confiance et de sérénité."


n "Avec le temps, elle est devenue moins formelle. Un peu, mais juste assez. Ça me faisait plaisir de la voir baisser sa garde avec moi et s'ouvrir, même juste un peu. J'avais l'impression de la découvrir, elle, vraiment."


n "\nMaintenant, je commence à avoir des doutes."


n "\nPeut-être que je devais m'y attendre après qu'on ait rompu. Ces doutes ne me semblent pas nouveaux, mais plutôt comme des vieux livres qu'on retrouve et dont on enlève la poussière."


n "J'ai vite réalisé, après avoir rencontré Lilly, qu'elle me voyait comme elle a vu Hanako, comme quelqu'un qui avait besoin d'aide et d'attention. Au début, je pensais qu'on serait très bien en tant qu'amis, s'aidant mutuellement durant notre temps à l'école."

nvl clear


n "\n\nMais j'ai commencé à chérir nos moments de plus en plus, de nos marches silencieuses à nos discussions pendant le déjeuner. Les bons côtés de sa personnalité se ressentaient mieux et je l'appréciais plus."


n "L'absence causée par le voyage de Lilly en Écosse pour visiter sa famille et sa tante malade m'a permis de réaliser à quel point j'aimais être avec elle et j'ai pensé qu'elle ressentait la même chose."


n "\nPour elle, cela dit, peut-être qu'il n'y avait pas que ça qui entrait en ligne de compte."


n "Mais après qu'elle soit revenue au Japon, elle a perdu une nouvelle fois sa famille, après ne les avoir vus que peu de temps."


n "Elle a vécu tellement longtemps sans sa famille, sans compter Akira qui travaille beaucoup, qu'elle n'avait pas d'autre choix que d'être comme ça."

nvl clear


n "\n\nJ'ai trouvé son indépendance admirable. C'était vraiment l'opposé de quand je dépendais de mes parents avant ma crise cardiaque, même si j'ai eu du mal à l'admettre."


n "Cela dit, ça voulait aussi dire qu'elle ne laissait pas les gens s'approcher d'elle."


n "Elle a perdu sa famille sûrement à cause de sa cécité, a été dans une école différente de tous ceux qu'elle connaissait à cause de cela, et a dû travailler dur pour faire en sorte qu'elle ne soit pas un fardeau pour sa sœur et ceux autour d'elle."


n "\nEt maintenant, Akira part à Inverness, tout comme sa famille qu'elle croyait avoir perdue."


n "Elle ne m'a jamais parlé de ses plans, aussi tiraillée puisse-t-elle être à leur sujet."


n "Lilly n'a jamais voulu devenir un fardeau, même pas pour moi."


n "\n\n...Je suis un idiot."

nvl clear


n "\n\nJe ne me suis jamais posé la question. Je n'ai jamais essayé d'être là pour elle ou même de savoir si elle avait besoin de moi."


n "Je me suis juste reposé sur mes acquis en espérant que cela reste comme ça pour toujours, que nous puissions avoir tous les deux une longue et heureuse relation où nous aurions avancé ensemble vers notre avenir."


n "\nUn petit pic de frustration et de colère contre moi-même monte dans ma poitrine."


n "\nJ'ai juste laissé les choses arriver, sans jamais essayer de l'aider."


n "\nSa présence suffisait. Enfin, j'aurais pu continuer si cela avait été vrai."


n "Mais ça ne pouvait pas être suffisant. C'était une dépendance enfantine, sans aucune tentative de compréhension de la situation."


n "À cause de ça, j'ai perdu Lilly. J'ai perdu la personne que j'aimais le plus parce que je n'étais pas là pour elle quand elle avait besoin de moi."

stop music fadeout 5.0

nvl clear
nvl hide dissolve

show origami_hand:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with None

show origami_hand:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
show bg school_dormhisao_ni
with Dissolve (1.0)

hide origami_hand
with None

window show


"Avec une colère grandissant à l'intérieur de moi, je me tourne et repose la grue sur le bureau à côté de mon horloge, l'endroit où elle a toujours été depuis que Lilly me l'avait offerte."


"Depuis ce jour où elle m'a dit que je n'avais pas besoin de porter mon fardeau tout seul."


"Les chiffres rouges sur mon horloge brillent dans les ténèbres de ma chambre, agressant mes yeux fatigués."


"Dix heures. Du soir. C'est bientôt l'heure du couvre-feu."


hi "Je me demande..."


"Akira a mentionné qu'elles partaient ce soir."


"Je n'ai aucune idée de l'heure exacte de leur vol... mais ça veut dire qu'il y a une chance, aussi petite soit-elle, qu'elles puissent ne pas être parties."


"L'adrénaline commence à parcourir mon corps alors que je me redresse, les yeux écarquillés."


"Il n'y a aucune garantie qu'elles ne soient pas parties, elles le sont sûrement déjà d'ailleurs, mais il y a aussi une chance qu'elles soient encore là."


"Juste cette fois, comme j'aurais dû le faire avant..."

play sound sfx_switch

show bg school_dormhisao
with Dissolve(0.2)

$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_friendship fadein 9.0


"Je me lève et me précipite vers mon armoire pour enfiler des vêtements aussi vite que je le peux."


"Chaque seconde qui passe est une seconde perdue, une seconde qui peut faire la différence entre les rattraper et les perdre pour toujours."


"Même si j'échoue, je dois essayer. Je ne peux pas la laisser tout abandonner sans même essayer de la retenir. Sans, pour une fois, être là pour elle."


"Avec le reste de mes vêtements enfilés, j'attrape avec hâte mon téléphone sur le bureau. Heureusement, le numéro de la compagnie de taxi est toujours dans mon historique."

show bg school_dormhisao_blurred
show phone mobile:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with locationchange
with Pause (0.5)


"Une voix enthousiaste annonce le nom de la compagnie alors que je fais les cent pas dans la chambre. Il me faut un certain effort pour ne pas parler trop vite et être clair."

scene bg school_dormext_full_ni
with locationskip


"L'air froid de la nuit m'accueille alors que j'ouvre les portes du dortoir, mais cependant je vais jusqu'au portail en petite foulée."


"Ce n'est peut-être pas encore le couvre-feu, mais il est bientôt l'heure. S'il y avait un garde, il aurait sans doute quelques questions pour moi, mais on dirait que j'ai réussi à sortir juste avant qu'il n'arrive."

scene bg school_gardens_ni
with locationchange


"Mon rythme s'accélère alors que je traverse les jardins, leur attrait nocturne toujours présent alors que j'arrive au portail de l'école."

scene bg school_courtyard_ni
with locationchange


"Les lampes du jardin, assez faibles, me procurent assez de lumière pour savoir où je marche sans tomber. Les bâtiments semblent rustiques, presque antiques quand je les regarde."


"En y repensant, ça me fait bizarre qu'ils m'aient paru aussi sombres auparavant. Maintenant ils ont juste l'air de bâtiments scolaires quelque peu anachroniques, comme beaucoup d'autres."

scene bg school_gate_ni
with locationchange


"Laissant le portail derrière moi, j'arrive à l'endroit du rendez-vous juste avant le taxi. Garé à l'endroit où se trouvait la voiture d'Akira, son apparence criarde et brillante semble inopportune par rapport aux environs calmes et verts."


"Je me précipite à l'intérieur et donne au conducteur l'adresse où elles devaient rester avant d'aller à l'aéroport."

scene bg shizu_houseext_ni
with shorttimeskip


"Au moment où le taxi arrive, après avoir roulé doucement à m'en rendre presque fou, on est au beau milieu de la nuit."


"La maison est vraiment énorme, beaucoup plus grande que ce que je croyais et surtout trop calme. Craignant le pire, je demande au conducteur de rester, juste au cas où mes efforts auraient été vains."


"Une simple pression sur l'interphone de luxe produit une courte mélodie électronique. Il ne faut pas longtemps avant qu'une voix masculine quelque peu bourrue me réponde."


mystery "Vous êtes à la résidence Hakamichi. Veuillez donner votre nom et la raison pour laquelle vous nous dérangez si tard."


"J'appuie sur le bouton malgré mon sourcillement face à l'irritation visible dans sa voix."


hi "Je suis Hisao Nakai. J'aurais espéré voir Lilly ou Akira, si elles sont encore là."


"Étonnamment, je réussis à mettre un tant soit peu d'énergie dans ma voix, suffisamment pour rendre l'autre côté de l'interphone silencieux."

show bg shizu_houseext_lights
with Dissolve(0.2)


"Quelques secondes passent et juste avant que je rappuie pour demander ce qui se passe, une lumière apparaît à la porte de devant."


"Je plisse les yeux pour essayer de voir qui vient et alors qu'il passe derrière une voiture garée avec des cannes dépassant du coffre, son identité devient claire."


"Son visage est placide et sans émotions alors qu'il arrive à hauteur du portail. Il est toujours enfantin dans ses manières, malgré son comportement. Après qu'il ait pressé quelques boutons de l'autre côté, le portail s'ouvre lentement."

show hideaki surprise_ni at center
with charaenter


hh "Hisao ? Qu'est-ce que tu fais là ?"


"Je crois que c'est la première fois que j'entends de l'émotion dans sa voix."


hi "Akira m'a dit qu'elles restaient ici avant de partir prendre leur vol."


hi "Je dois parler à Lilly, juste une dernière fois. Elles sont encore là ?"

show hideaki sad_ni
with charachange


"L'expression sur son visage en dit long."


"J'ai échoué. C'est trop tard. C'est la seule fois où j'avais besoin d'agir rapidement et..."

show hideaki serious_up_ni
with charachange


hh "En fait... c'est possible..."


hi "Quoi ? De quoi ?"

show hideaki confused_ni
with charachange


"Il est un peu surpris par ma ferveur, mais je m'en moque, vu la situation."

show hideaki normal_ni
with charachange


hh "Elles sont parties il n'y a pas longtemps, quelques minutes avant que tu n'arrives, en fait. Si tu vas directement à l'aéroport, tu pourrais être capable de... Hisao ?!"


"Je fonce vers le taxi qui m'attend, attrapant le peu d'argent qu'il me reste dans les poches en même temps."


hi "Merci, Hideaki !"


"En m'asseyant, je crie presque ma destination au chauffeur."

scene bg city_street4_ni
show crowd_ni
with shorttimeskip

play ambient sfx_crowd_outdoors fadein 2.0


"Mon cœur bat rapidement alors que je descends la rue en courant, faisant mon chemin entre les personnes qui circulent."


"Avec la route qui bouchonnait à cause des taxis et des autres voitures déposant des passagers et en prenant d'autres, on a fini par être bloqués presque cinq cents mètres avant."


"Mais c'est le passé maintenant. Ce qui importe, c'est d'atteindre Lilly."


"Un pied touche le sol, l'autre le suit rapidement sans y penser un seul instant, comme si mes jambes fonctionnaient toutes seules et que tout ce que mon esprit pouvait faire c'était se concentrer sur la vue en face de moi."


"Juste un aperçu de ses cheveux. Ses longs cheveux dorés qui étaient de la même couleur que le blé qui s'étendait à perte de vue."


"En fin de compte, je dépendais de Lilly, tout comme Hanako. Même après qu'on ait fini par sortir ensemble, je n'ai jamais eu l'impression qu'elle ait fini par se reposer sur moi."


"Sauf à un moment. Cet unique moment où nous nous sommes étreints dans ce champ doré."


"À ce moment elle a dû avoir peur de me perdre, tout comme elle a perdu tous les autres. C'est pourquoi, juste cette fois..."


"Le froid de la nuit m'enveloppe, drainant chaque fibre de chaleur de mon corps, à tel point que j'ai plus l'impression que c'est une nuit d'hiver que d'été."


"Mes doigts, mes mains, mes pieds.. ils sont tous de plus en plus froids."


"Le brouhaha des gens qui passent est réduit à un bruit de fond alors que le son de mes pas frappant le sol résonne bruyamment, chaque pas se dirigeant vers la personne que je dois atteindre."


"Ma poitrine se serrant en réponse au froid de la nuit, je pose une main dessus pour essayer de la calmer."

window hide

scene bg hosp_ext_ni
show crowd_ni
with locationchange

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)

window show


"Quand l'aéroport est en vue, je réalise le sens de cette sensation."


"Pas maintenant... n'importe quand, mais pitié, pas maintenant."


"J'avale ma salive et continue d'avancer, poussant mon corps jusqu'à ses limites."


"De la sueur coule le long de mon corps alors que je me rue vers l'avant, mon épaule cogne quelqu'un au passage et mon esprit est envahi d'émotions et de souvenirs."


"Je continue sans m'excuser. Je dois continuer d'avancer. Si je m'arrête, je ne suis pas sûr de pouvoir repartir, et même si j'y arrive, ce serait une perte de temps que je ne peux pas me permettre."

with vpunch


"Je cogne une autre personne, puis une autre, qui offrent peu de résistance alors que je passe en les bousculant."


"Mes pieds sont engourdis. Mes bras perdent leurs sensations. Ma poitrine me force à me voûter bizarrement, se resserrant encore plus."

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

window show


"Cet après-midi dans la neige... cette fois où ma vie a irréversiblement changé... des images d'Iwanako et de cette fichue lettre me traversent l'esprit, le premier amour que j'ai perdu à cause de ma condition."


"Je ne peux pas laisser cela arriver encore une fois. Je m'en fous de ce qui peut m'arriver, je dois juste la voir une dernière fois."


"...Là !"

scene ev lilly_airport
with flash


"Une mèche jaune se laisse voir un peu plus loin, la silhouette étant éclairée par les lumières de l'entrée de l'aéroport."


hi "Lilly ! Lilly !"


hi "Lilly ! Arrête-toi, s'il te plaît ! Lilly !"


"Allez Lilly, je sais que tu entends bien mieux qu—"

scene bg hosp_ext_ni:
    xalign 0.5 yalign 0.52 rotate 0 zoom 1.0
    linear 0.1 rotate -6 zoom 1.2
show crowd_ni:
    xalign 0.5 yalign 0.52 rotate 0 zoom 1.0
    linear 0.1 rotate -6 zoom 1.2
with vpunch

play sound sfx_impact


hi "Argh !"


"Je finis sur le sol, mon corps se contorsionnant après avoir cogné quelqu'un et trébuché."

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

window show


"Avant que je puisse évaluer les dégâts, une douleur incroyable s'enflamme dans mon corps. Toutes mes pensées se troublent alors que je me tords et m'agrippe la poitrine."


mystery "Hé, ça va ? C'était une chute plutôt violente."


"Cette douleur... Je peux pas..."


hi "Argh... aaaaaargh !"

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

window show


"N'importe quel coup pouvait m'avoir. N'importe quel surmenage. Je pensais pouvoir dépasser mes limites cette fois..."


mystery "Y a quelque chose qui ne va pas avec lui !"

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.8)

window show


mystery "Qu'est-ce qui se passe, tu..."

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
with Dissolve (0.8)

window show


"Les voix de ceux qui se rassemblent autour de moi sont remplacées peu à peu par un son strident à mes oreilles. Maintenant je suis incapable de bouger la tête, je bouge les yeux pour voir leurs lèvres remuer sans le son."

window hide

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.8)

with Pause(0.15)

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.8)

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.8)

with Pause(0.05)

play sound sfx_heartstop
show heartattack alpha
with Dissolve (0.1)

stop ambient fadeout 0.3

show heartattack residual
with Dissolve (0.8)

window show


"Même si j'agrippe ma poitrine, je réalise que je ne peux plus sentir mes doigts, ou mes pieds. J'ai l'impression que mon corps entier s'arrête, en commençant par les extrémités."

scene ev lilly_airport_end:
    truecenter
    zoom 1.2 rotate -8 subpixel True
    easein 12.0 zoom 1.0 rotate 0
with slowfade


"Avec un dernier effort, je tourne la tête vers l'avant, vers l'entrée de l'aéroport."


"Lilly est là, derrière la foule. Sa tête est penchée, mais juste un peu."

show passoutOP1
with None


"Je peux sentir ma vision s'amenuiser alors que j'essaye de crier, mais aucun son ne sort de ma bouche malgré mes efforts. Lentement mais sûrement, ma vision devient noire et je perds conscience de ce qui se passe."


"Donc... c'est comme ça que ça finit..."


"J'ai échoué. J'étais si proche, vraiment très proche, mais au tout dernier moment ma condition m'a empêché de saisir la chance d'une nouvelle vie."


"Maintenant je vais mourir, étalé à quelques mètres de l'entrée d'un aéroport, avec une foule de gens autour de moi et Lilly partant pour l'Écosse juste un peu plus loin."

hi "Li… lly…"

stop music fadeout 4.0


"Ce dernier mot utilise tout ce qu'il me restait d'énergie. Le monde devient un trou noir dans lequel je disparais alors que chaque muscle de mon corps s'immobilise."


"Je suis désolé, Lilly."


"Je suis arrivé trop tard."

scene black
with dissolve




label fr_L31:

scene white
with dissolve


"…"

"……"

"………"


"Qu'est-ce... qui se passe... ?"


"Alors que j'ouvre lentement les yeux, une lumière blanche m'agresse."


"Pendant plusieurs minutes je reste là, regardant devant moi alors que des pensées s'assemblent doucement dans mon cerveau qui se réveille lentement."

show bg hosp_ceiling:
    alpha 0.0
    linear 5.0 alpha 1.0
with None


"Lentement mais sûrement, ma vision commence à revenir, transformant cette lumière blanche en formes."


"C'est seulement au bout d'un moment que je me rends compte que c'est un plafond au-dessus de moi."

scene bg hosp_room2
with locationchange


"Redressant doucement la tête, je prends silencieusement conscience avec tous mes sens de ce qui m'entoure."


"L'odeur de désinfectant dans l'air donne à cet endroit l'impression d'être trop propre pour être naturel."


"Murs de couleur pêche, peints parfaitement sans fissure, tache ou imperfection. Un seul tableau est sur le mur, parfaitement droit. Tout comme les murs, il est aussi ennuyeux et neutre que possible."


"Mon attention est attirée par les rideaux un peu transparents, seul élément qui bouge dans ma vision, couvrant une fenêtre ouverte."


"Quand je bouge mon bras pour essayer de me redresser et de voir par celle-ci, je sens le cathéter me gêner dans mon mouvement. C'est seulement maintenant, aussi, que je remarque les tuyaux passer le long de mes joues jusque dans mon nez."


"Après avoir remué, je m'arrange pour voir juste un coin de la fenêtre."

scene ev lilly_hospitalwindow
with whiteout


"Derrière les feuilles de quelques grands arbres, je peux voir une étendue verte. Une île de verdure à l'extérieur de la ville."


"À en juger par le soleil, il est midi. De quel jour, je ne sais pas."


"Donc... Je suis de nouveau dans un hôpital."


"Je pousse un long soupir et essaye de rassembler mes pensées, mon cerveau semblant aller dans des dizaines de directions différentes avec autant d'émotions me submergeant en même temps."

scene bg hosp_room2
with locationchange


"Après m'être rallongé doucement, je décide de commencer par le début : pourquoi je suis là."


"Je repars dans le passé, mais n'arrive pas à bien me rappeler de ce qui est arrivé. Les événements de la nuit dernière... ou peu importe quelle nuit c'était... me reviennent en une série d'images plutôt qu'en un souvenir clair."

scene bg school_dormhisao_ni_fb
show origami_fb at center
show noiseoverlay
with flash


"Couché sur mon lit regardant l'oiseau en origami."

scene bg shizu_houseext_lights_fb
show hideaki serious_up_fb at center
show noiseoverlay
with flash


"Parlant à Hideaki à la résidence des Hakamichi."

scene bg hosp_ext_fb
show crowd_still1_fb at center
show noiseoverlay
with flash


"Courant dans la rue, zigzaguant entre les piétons et en bousculant de plus en plus au passage."

scene bg hosp_ext_fb:
    xalign 0.5 yalign 0.52 rotate -6 zoom 1.2
show crowd_still2_fb:
    xalign 0.5 yalign 0.52 rotate -6 zoom 1.2
show noiseoverlay
with flash


"Tombant."

scene ev lilly_airport_end_fb
show noiseoverlay
with flash


"Regardant vers l'entrée de l'aéroport, voyant le dos de Lilly alors que je suis couché sur le sol..."

"…"

scene bg hosp_room2
with fade


"Le silence de la chambre me semble soudainement étouffant."

play music music_rain fadein 2.0

window hide
nvl clear
nvl show dissolve


n "\nDonc voilà. J'avais une chance de corriger mon erreur et je l'ai loupée."


n "Que je sois en tort pour avoir négligé ma médication et pas pris soin de me ménager, ou que mon corps le soit pour m'avoir lâché trop tôt, ça ne m'importe plus maintenant."


n "Tout ce qui importe est que, encore une fois, je suis seul."


n "L'oreiller bleu pastel oppose peu de résistance alors que je me laisse retomber sur le lit, sa taie qui gratte et les draps raides offrent peu de confort."


"Comparé à la noirceur des évènements de la nuit dernière, les lumières de la pièce sont aveuglantes. Tout ce qu'elles font, c'est accentuer le fait que cet endroit semble être dans un autre monde."


n "\nArythmie."


n "\nUn mot bizarre. Un mot étranger. Un mot avec qui tu ne veux pas être dans la même pièce."


n "Une pathologie rare. Cela fait que le cœur est instable et bat occasionnellement trop fort. Ça peut être fatal."

nvl clear


n "\nIls ont dit “C'est un miracle que vous ayez vécu aussi longtemps sans que rien n'arrive.”"


n "Et pourtant, c'est arrivé. Ma maladie m'a tout pris, mon ancienne école n'importait plus. Ma maison est devenue un endroit lointain. Mes deux amis et mon premier amour ont fini par arrêter de venir après un moment."


n "Je suis devenu cynique et aigri. Distant et passif. Pour ma défense, personne n'aurait pu éviter que cela arrive, mais néanmoins, quand j'ai quitté l'hôpital, j'étais bien différent de quand j'y suis rentré."


n "Les choses ont changé. Je me suis fait de nouveaux amis. Hanako, Shizune et Misha. J'ai trouvé un nouveau sens au mot “maison” avec le dortoir, un nouvel intérêt dans la science et dans le monde autour de moi, et j'ai trouvé une direction dans ma vie que je n'avais jamais envisagée."


n "\nMais j'ai aussi découvert d'autres choses."


n "L'isolement de Yamaku et ses environs n'étaient pas vraiment désagréables, le calme donne une tranquillité d'esprit que je n'aurais peut-être pas trouvée ailleurs, mais cela donne l'impression d'être mis à l'écart du reste du monde."

nvl clear


n "\n\nLes gens dans la rue te regardent parfois bizarrement, ou tournent rapidement la tête quand ils voient que tu les remarques. Même si ma condition n'est pas visible, mon uniforme l'est."


n "Même s'il ne l'était pas, je suis quand même différent. Je prends dix-sept pilules par jour, matin, midi et soir. Ma cicatrice, bien que cachée derrière mes vêtements, est toujours une marque permanente de ma condition. Et surtout, il y a un vrai risque de mort."


n "Une mauvaise chute. Une claque dans le dos. Un sprint. N'importe quoi pourrait avoir raison de moi et j'ai plusieurs fois été à la limite du drame malgré tout ce que je fais pour prendre soin de moi."


n "\nMais ça m'allait. J'aurais pu vivre avec tout ça."


n "Parce qu'il y avait une chose que j'avais trouvée, ou plutôt retrouvée, après être entré à Yamaku."


n "\nQui m'a été encore une fois enlevée."

nvl clear


n "\nC'est seulement maintenant que je réalise à quel point mon nouveau bonheur était fragile. Tout dépendait d'elle, le pilier de ma vie depuis que j'étais entré à Yamaku sans espoir, confus et sans but."


n "Lilly Satou était la seule personne sur qui je pouvais vraiment compter et qui a répondu à l'amour que je ressentais pour elle. Mais j'ai échoué avec elle et je l'ai seulement réalisé une fois trop tard."


n "Je pensais que je pouvais continuer ma vie telle qu'elle était pour toujours, mais le vrai monde ne fonctionne pas comme ça. J'ai finalement réalisé le sens de ces mots, seulement après avoir été confronté à mon échec de ne pas m'en être rendu compte à temps."

n "\n…"


n "\nLes environs sont bien trop familiers. C'est comme si Yamaku n'avait été qu'un rêve, que je n'étais jamais ressorti après ma première crise cardiaque."


n "C'est peut-être pour ça que je me sens si fatigué. J'ai l'impression d'avoir vécu ces derniers mois en l'espace de quelques minutes."

nvl hide dissolve
nvl clear

scene black
with shuteye

window show


"Le poids de mes paupières me force à fermer les yeux, ma fatigue physique et mentale ne me permet pas de résister."

window hide
with Pause(1.0)
with shorttimeskip
with Pause(1.0)
window show


"Un marmonnement incompréhensible me sort du sommeil."


"Avec les yeux toujours clos, je peux me rendre compte que quelqu'un, probablement une infirmière, salue un docteur."

scene bg hosp_room2
with openeye


"Alors que j'ouvre les yeux, je remarque la porte se fermer dans ma vision périphérique."


"Le docteur se tient là à lire les notes d'un porte-documents qu'il a en main, passant avec attention sur chaque page."


"Après avoir consulté ses documents importants, il lève la tête et me voit éveillé. C'est seulement maintenant que je remarque quelque chose de bizarre avec son expression, mais je n'arrive pas à savoir quoi."


"Docteur" "Ah, je vois que vous êtes réveillé... M. Nakai."


"Son regard furtif à la tête de lit, pour vérifier mon nom, montre qu'il n'était même pas noté sur les documents."


"Docteur" "Je dois avouer que c'est un peu dommage, vos parents sont venus plus tôt pendant que vous dormiez. Je peux leur dire que vous êtes réveillé maintenant, si vous le voulez."


hi "Hum... Je veux bien. Merci."


"Je réponds quelque peu dans le brouillard, une réponse qu'il attendait visiblement."


"Docteur" "Pas de problème."


"Docteur" "Si vous avez une question, je suis là pour y répondre. Sauf si vous préférez vous reposer, l'anesthésie continuera de faire effet un petit moment, j'en ai peur."


"L'anesthésie... bien sûr. C'est pour ça que je me sentais si bizarre la première fois que je me suis réveillé."


"Je secoue lentement la tête, ne voulant pas déloger un tuyau ou quoi que ce soit qui rendrait la situation encore plus inconfortable. Le docteur pose poliment son porte-documents en réponse."


hi "J'imagine que la question est en gros... qu'est-ce qui s'est passé ?"


"Docteur" "Pour dire les choses simplement, vous avez malheureusement eu une autre crise cardiaque. Bien que pas aussi sévère que la première, vous avez eu de la chance qu'elle arrive dans un lieu si proche d'un hôpital."


"Docteur" "Après avoir été stabilisé, vous avez été emmené en salle d'opération. S'en est suivie une opération laparoscopique dans le but d'insérer un pacemaker temporaire."


"Docteur" "L'incident est arrivé il y a deux jours et les traitements d'urgence ont été menés peu après. Depuis, vous avez été gardé en observation constante pendant votre sommeil."


hi "Je vais bien alors ? Il ne reste plus de problème à régler ?"


"Docteur" "En comparaison de ce qui a dû être fait après votre première crise cardiaque, c'était assez mineur."


"Docteur" "Bien qu'il y aura une autre opération dans quelques jours pour retirer le pacemaker, en supposant qu'il n'y ait pas de complications, ce devrait être tout."


"Il continue de parler, le sujet basculant vers l'arythmie et mes médications, dont je connais déjà la plupart. Je commence à hocher la tête et feindre l'intérêt, tout en pensant à autre chose."


"Je commence à penser à quel point le tableau neutre derrière lui est bien accroché et à quel point les environs et le docteur lui-même sont blancs et stériles."


"Docteur" "Si ce que je dis vous ennuie, sentez-vous libre de me le dire, M. Nakai. Dieu sait à quel point je peux perdre fil de ce que je dis parfois."


"Il rit brièvement à sa propre blague tandis que je grimace bizarrement, m'étant fait attraper."


"Le rire du docteur est différent de celui de l'infirmier de Yamaku cela dit. Me posant la question, je réalise finalement pourquoi l'homme en face de moi me semble un peu “bizarre”."


"Son sourire est stérile. Il récite parfaitement sa petite blague et s'en suit un rire innocent."


"C'est comme si, plutôt que de parler à l'homme dont le nom est parfaitement écrit sur le badge épinglé sur sa blouse, j'interagissais avec un acteur lisant un script écrit à l'avance, chaque action ayant été chorégraphiée et répétée."


"J'imagine que c'est ça, être docteur."


"Il doit garder son sourire soigné et stérile quand il parle à la fille qui a un cancer qui s'étend dans son corps, quand il rassure la femme qui va sûrement mourir en accouchant, et avec tous les autres patients gravement malades et agonisants."


"Quelque peu distant. Quelque peu réservé."


"Je me demande si j'ai été trop dur avec lui, surtout en sachant que ce n'est pas juste les gens de sa profession qui sont comme ça."


"Après tout, celle que j'aimais gardait les mêmes distances avec les autres."


"Regardant le docteur, je réalise que j'ai réfléchi avec la tête baissée un long moment."


"Docteur" "Je comprends que vous devez toujours être fatigué. Cela fait beaucoup d'un seul coup et comme je l'ai mentionné, l'anesthésie doit toujours faire effet."


"Docteur" "Si ca ne vous gêne pas, je vais vous laisser vous reposer et dire à vos parents que vous êtes réveillé."


hi "Je crois... que c'est une bonne idée. Merci."

stop music fadeout 6.0


"Il hoche la tête avant de prendre son porte-documents et de se diriger jusqu'à la grande porte blanche dans le coin de la pièce avant de la refermer derrière lui."


"En fin de compte, je suis encore une fois seul."


"Lilly est partie. Akira est partie. Hanako doit être en voyage, et même mes parents sont partis de l'hôpital."


"Quatre murs couleur pêche, un plafond blanc et une seule fenêtre pour voir le monde extérieur."


"C'est difficile de penser à l'avenir quand le passé est tout autour de vous, vous étouffant de sa poigne blanche, stérile, et son odeur de désinfectant."


"Ne trouvant rien d'autre à faire, je me contente de dormir, comme si ce n'était qu'un autre rêve, comme l'a été Yamaku."

scene black
with dissolve



label fr_L32:

scene white
with dissolve


"Blanc."


"Un blanc stérile et propre, pour une chambre stérile et propre."

$ renpy.music.set_volume(0.05, 0.0, channel="music")
play music music_musicbox fadein 10.0

show bg hosp_ceiling:
    alpha 0.0
    linear 5.0 alpha 1.0
with None


"Les yeux ouverts, je regarde le plafond pendant un moment. Il est aussi intéressant que le serait la télévision, montée sur un rail en métal pendant du plafond devant le lit."


"La télévision a été allumée pendant que mes parents étaient là. Le son coupé, elle était aussi banale qu'elle l'a été durant mon premier séjour à l'hôpital."


"Plus tôt, une infirmière m'a proposé de couper les enceintes de l'électrocardiogramme. J'ai refusé, le son étant entièrement normal pour moi maintenant."


"C'est presque réconfortant, d'une certaine façon. Le son régulier comme un métronome donne quelque peu l'impression que le temps passe, même dans un endroit comme celui-ci."


"Après un moment à avoir écouté le bip tout en étant complètement éveillé, je réalise qu'il y a un autre bruit dans la pièce."

$ renpy.music.set_volume(0.1, 5.0, channel="music")


"Me concentrant pour écouter, tâche plutôt facile étant donné le manque de distraction, une petite mélodie se fait entendre."


"Légère et peu bruyante, la musique semble fragile alors qu'elle est étouffée par le bruit de l'électrocardiogramme."

scene bg hosp_room2
with locationchange


"Tournant légèrement la tête sur le côté pour voir la source de la mélodie sans enlever aucun des tuyaux coincés en moi, je remarque une petite boîte en bois sur la table de nuit à côté du lit."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

show musicbox open:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)


"Ma bouche s'ouvre légèrement pendant que je regarde en silence le petit cylindre de métal jaune tourner à l'intérieur, les petites bosses sur sa surface bougeant lentement."


"Cette boîte à musique... c'est celle que j'ai donnée à..."

show musicbox open:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide musicbox
with None


"Le bruit de la porte me sort de mes pensées, ma tête et mon cœur s'arrêtant le temps d'un instant alors que mes yeux se tournent pour voir qui est là."


"Longue jupe brune... pull beige s'arrêtant sur l'épaule... peau pâle, presque de porcelaine... yeux bleus opaques et de longs cheveux blonds.."

show lilly basic_reminisce_cas at center
with charaenter


"Tout ce que je peux faire, c'est regarder Lilly marcher lentement dans la chambre, ses doigts frôlant légèrement le mur pour s'orienter. Et mon esprit reprend enfin le cours des choses."


hi "L... Lilly... ?"

show lilly basic_oops_cas
with charachange


"Elle s'arrête de marcher, son corps entier se raidissant."


li "Hisao ? C'est toi ?"


"Sa voix est calme et pensive, tout comme son expression."


hi "Je croyais que tu étais..."

show lilly basic_sad_cas
with charachange


"Lilly fait un pas timide en avant, puis un autre, comme si elle se retenait."

show lilly basic_sad_cas_close
with characlose


"Le contrôle qu'elle exerce sur elle-même ne sert finalement à rien, vu qu'elle se précipite sur moi alors que sa dernière résistance tombe."

$ ksgallery_unlock("unlock_ev lilly_hospitalclosed")
scene ev lilly_hospitalclosed at l_hosp_out
with whiteout


"Je suis surpris quand elle passe ses bras autour de moi et que des larmes commencent à couler sur ses joues ; quelques minutes avant je croyais qu'elle était de l'autre côté du monde."


"Après un moment d'hésitation, je pose une main sur son épaule."


li "Hisao ! Hisao !"


"Le corps de Lilly tremble et ses larmes tachent le drap bleu foncé, ses émotions la submergeant alors qu'elle se contient tellement habituellement."


"Avec son visage maintenant plus proche, je vois mieux sa peau pâle baigner dans la lumière provenant de la fenêtre et je remarque que ses joues sont plus rouges qu'elles ne devraient l'être."


hi "Ça va, Lilly. Je vais bien. Tu n'as pas besoin de—"

$ ksgallery_unlock("unlock_ev lilly_hospital")
show ev lilly_hospital at l_hosp_out
with charachange


"Elle se redresse rapidement, ses pleurs étant accompagnés de tristesse et d'entêtement visibles dans ses yeux humides. Sa nature fière, qui a toujours été une chose à laquelle il faut faire attention, me prend par surprise."


li "Arrête de me dire de ne pas m'inquiéter pour toi, Hisao !"


li "Juste cette fois... laisse-moi pleurer..."


"Je ne sais pas quoi dire. Elle attend une réponse, mais repart dans un sanglot après quelques secondes."

show ev lilly_hospitalclosed at l_hosp_out
with charachange


"J'avale ma salive pour essayer de contenir mes propres émotions pendant qu'elle pleure sur le lit, submergée par un étrange mélange de tristesse et de soulagement."


"Lilly est... là. Elle est vraiment là. Si je ne pouvais pas sentir sa peau sous ma main, j'aurais du mal à y croire. Mes efforts n'ont pas servi à rien. La tentative de mon corps de me retirer encore une fois tout ce qui m'était cher n'a pas réussi."


"Mais maintenant... Je ne me sens pas aussi heureux que je croyais que je le serais."


"La voir comme ça, pleurer sur moi comme ça... c'est la seule chose que je voulais éviter depuis que j'en suis venu à l'aimer, non, même depuis que je suis sorti de l'hôpital."


hi "Je suis désolé Lilly. C'est de ma faute si je suis ici. Je n'aurais pas dû autant forcer."


"Je laisse échapper un rire d'autodérision."


hi "Après des mois à faire ce que je peux pour que personne n'ait à s'inquiéter pour moi, je fais quelque chose comme ça... Je suis pas très malin en fait."

scene bg hosp_room2
show lilly basic_weaksmile_cas_close at center
with whiteout


"Après quelques reniflements et une longue inspiration, Lilly arrive à se ressaisir et se calmer un peu."


"Malgré ses joues rouges, ses yeux humides et les traces de ses larmes encore visibles, elle affiche toujours ce sourire délicat qu'elle a souvent."


li "Ne te blâme pas. J'ai entendu plus tard que ça t'est arrivé alors que tu me courais après, non ?"


hi "Même..."


"Elle s'essuie les yeux du dos de la main et reprend son attitude habituelle maintenant que son flot d'émotions est tari."

show lilly basic_reminisce_cas_close
with charachange


li "Pourquoi as-tu couru après moi, Hisao ?"

show lilly basic_concerned_cas_close
with charachange


"Je suis sur le point de répondre, mais remarque que son visage commence à se crisper."


li "Même après que je t'aie dit au revoir et que je sois partie de l'Académie..."


"Elle prend un moment pour se ressaisir, ses émotions refaisant surface."


hi "Je voulais juste te dire que je suis désolé."

show lilly basic_surprised_cas_close
with charachange


li "Désolé ?"


hi "Pour les fois où je n'étais pas là quand tu avais besoin de moi."


hi "Jusqu'à maintenant, je croyais que le fait que tu sois là suffirait. J'avais juste besoin de toi à mes côtés pour que mon quotidien soit agréable."


hi "Même si mon corps est comme ça, je veux t'aider, Lilly. Être là quand tu as besoin de quelqu'un."

show lilly basic_weaksmile_cas_close
with charachange


li "Mais tu étais toujours là, Hisao..."


hi "Pourquoi est-ce que tu voulais aller en Écosse, Lilly ?"

show lilly basic_sleepy_cas_close
with charachange


li "Pourquoi ?... Je te l'ai déjà dit, parce qu'Akira y allait et parce que ma famille m'a invitée à les rejoindre."


hi "Pourquoi tu n'as pas dit que tu voulais y aller ?"

show lilly basic_oops_cas_close
with charachange


li "Je—"


hi "Je ne suis pas souvent têtu, mais cette fois je pense que j'ai besoin de l'être. Je veux que tu restes, Lilly."


hi "Je veux que tu restes là où sont tous ceux que tu connais, et là où tes rêves et ambitions sont nés. Si tu choisis de rester, je resterai toujours à tes côtés. Je ne te laisserai pas perdre quelqu'un d'autre."


hi "Quand j'ai eu ma crise cardiaque, j'ai été arraché de tous ceux que je connaissais et de tous les endroits que je fréquentais. Tu m'as montré une nouvelle vie quand je suis arrivé à Yamaku. J'ai perdu mon passé, mais tu m'as montré un futur."


hi "Il est vrai que je n'ai pas toujours été là pour toi. Je suis peu fiable, des fois j'ai menti et je croyais que je te comprenais alors que je ne me comprenais même pas moi-même."


hi "Malgré tout ça, je veux aussi t'apporter un avenir. Je veux être là pour toi, partager tes fardeaux et ton bonheur, juste comme je te l'ai promis à Hokkaido."


hi "Je veux que tu me fasses confiance. Je sais que j'ai eu du mal à te faire confiance, après avoir perdu tant de personnes après ma crise cardiaque, mais c'est pour ça que je sais qu'être incapable de faire confiance aux autres peut être terrible."


hi "C'est pourquoi je ne peux pas me contenter de te regarder tout abandonner comme ça. Je ne veux pas que tu vives ce que j'ai vécu. Je ferai tout pour empêcher cela."

show lilly basic_weaksmile_cas_close
with charachange


li "Tu peux être vraiment ferme quand tu veux l'être, hein ?"


hi "Comme je l'ai dit, ça n'arrive pas souvent."


"Mon faible sourire s'efface, alors que l'intraveineuse me fait un peu mal au bras. C'est un rappel douloureux de mon état."

show lilly basic_concerned_cas_close
with charachange


"Le visage de Lilly se tend lorsque je laisse s'échapper un gémissement de douleur, regrettant immédiatement de ne pas l'avoir mieux camouflé. Je soupire de la voir encore comme ça."


hi "J'ai essayé d'empêcher tout le monde de s'inquiéter pour moi depuis que j'ai quitté l'hôpital, mais je n'ai pas pu empêcher la personne que j'aime le plus de pleurer sur moi."


hi "Même si je suis finalement capable de mettre des mots sur mes sentiments, je me sens plutôt inutile avec un corps comme celui-ci."


hi "Chaque fois que j'essaye d'accomplir quelque chose, il m'en empêche et même maintenant les choses se sont bien passées grâce à la chance."


hi "J'imagine que c'est quelque chose d'autre dont je devrais m'excuser. Tout ce que j'arrive à faire est t'inquiéter. Même maintenant, il est peu probable que je vive une longue vie."


"La sensation de la douce main de Lilly caressant ma joue gauche me fait redresser la tête et elle me sourit tendrement."

show lilly basic_smileclosed_cas_close
with charachange


li "Je crois que c'est normal pour toi de dire ça. Tu as toujours été si sincère et inquiet."

show lilly basic_smile_cas_close
with charachange


li "Tu es aussi réservé et doux, patient avec Hanako, et curieux à propos de tout et de tout le monde."

show lilly basic_weaksmile_cas_close
with charachange


li "Quand j'ai dit que tu me manquais quand j'étais avec ma famille, je n'exagérais pas. Je pensais toujours un peu à toi et ça m'a aidée pendant ces moments."

show lilly basic_reminisce_cas_close
with charachange


li "C'est pour cela que j'étais confuse quand ma famille m'a invitée à les rejoindre. Même après que j'ai cru avoir pris ma décision, tu as fait de ton mieux pour me faire changer d'avis."

show lilly basic_weaksmile_cas_close
with charachange


li "Je ne t'ai pas avoué mes sentiments par pitié ou parce que je te croyais différent de ce que tu es. Je me suis confiée à toi parce que je ne veux jamais te perdre, et je veux que tu fasses partie de ma vie, peu importe ce que ça implique."

show lilly basic_smileclosed_cas_close
with charachange


li "Tu es une personne fantastique, Hisao. Ton cœur ne change rien à cela, donc s'il te plaît, ne t'en excuse pas."


"Pendant un long moment, le silence règne dans la pièce."


"Je ne suis pas sûr de ce qu'est ce nouveau sentiment en moi, mais il s'efface alors que je regarde le visage souriant de Lilly, aussi chaleureux qu'il a toujours été."


"C'est seulement au moment où son pouce passe sur ma joue, essuyant une seule larme, que je réalise que c'est tout ce que j'ai toujours voulu."


"Pour ce qui semble être la première fois, j'affiche un grand et honnête sourire. Alors que Lilly le ressent avec sa paume, elle fait de même."


"Nous restons là longtemps, sans dire un mot, aucun d'entre nous deux n'ayant besoin de communiquer pour exprimer ses sentiments envers l'autre."


hi "Je sais que je ne peux pas te promettre de toujours être là, ou que nous serons ensemble pour toujours."


"Avec quelques difficultés, je lève lentement la main et la pose sur son épaule."


hi "Mais... Je crois que je peux au moins t'emmener à Tanabata l'an prochain, pour me faire pardonner de t'avoir fait louper celui de cette année."

show lilly basic_emb_cas_close
with charachange


"Lilly semble surprise, je ne peux pas lui en vouloir."


li "Tu... t'en rappelles ?"


hi "J'ai une bonne mémoire. Des fois."

show lilly basic_giggle_cas_close
with charachange


"Elle relève un peu la tête, retire sa main de ma joue et laisse échapper un petit rire amusé. Son rire léger, presque innocent, me fait sourire."

show lilly basic_cheerful_cas
with charadistant


"Souriant toujours, elle se redresse et pose une main sur ma poitrine."


"J'ai l'impression de la voir pour la première fois, le soleil provenant de la fenêtre brillant derrière elle comme lorsque je suis entré dans cette pièce où elle buvait du thé."

show lilly basic_smile_cas
with charachange


li "Eh bien d'accord. Nous devrions nous promettre d'aller ensemble au Tanabata de l'année prochaine."


"Même si elle ne me voit pas le faire, je hoche la tête."


hi "Je le promets."

show lilly basic_smileclosed_cas
with charachange


li "Je le promets."

window hide

stop music fadeout 4.0




label fr_L33:

window hide None

play ambient sfx_parkambience fadein 6.0

scene bg lilly_hilltop
with Dissolve(3.0)

play music music_lilly fadein 5.0

window show


"Akira, Lilly et moi sommes silencieusement assis dans l'herbe sur la digue en haut de la ville, la brise provenant du ciel sans nuage nous caressant."


"On est peut-être à quelques minutes de marche de la ville, sur une colline juste en dehors de ses limites, mais la vue est vraiment étonnante."

show lilly basic_smileclosed_cas_close:
    left
    ypos 1.1
with charaenter


"Lilly est assise à mes côtés, les yeux clos alors que la douce brise passe dans ses cheveux."


li "C'est un bon endroit."


hi "Ouais. Je ne savais pas qu'il y avait un endroit comme ça près de Yamaku."

show akira basic_ending_close:
    right
    ypos 1.1
with charaenter


aki "Et c'est moi qui l'ai trouvé, bien sûr."


"Le sourire d'Akira est honnête, mais son ton est légèrement différent de d'habitude."

show akira basic_smile_close
with charachange


aki "C'est bien que tu sois sorti de l'hôpital, Hisao."


hi "Personne n'en est aussi content que moi. Je ne supporte pas les hôpitaux."


aki "Donc vous retournez à l'école demain ?"


$ doublespeak(hi, li, "Ouaip.", "Ouaip.")

show akira basic_ending_close
with charachange


"Akira rit, amusée, avant de regarder la ville en contrebas. Les arbres entre les bâtiments frémissent avec le vent."


hi "Dommage qu'on n'ait pas pu aller au nord pour les vacances d'été, ou faire Tanabata."

show lilly basic_weaksmile_cas_close
with charachange


li "Je ne m'inquiète pas. Il y a toujours une prochaine fois."

show akira basic_smile_close
with charachange


aki "Tu seras diplômé avant les prochaines vacances, non ?"


hi "Ouais. Il y aura l'université après ça, hein."


aki "Vous allez à la même ?"

show lilly basic_smile_cas_close
with charachange


li "Sûrement. On a tous les deux d'assez bonnes notes pour y entrer."


hi "Tu sembles si sûre..."

show lilly basic_cheerful_cas_close
with charachange


li "Ne t'inquiète pas, tu es meilleur que moi dans la plupart des matières."


hi "J'imagine qu'on verra ça en temps voulu."

show akira basic_laugh_close
with charachange


aki "C'est le bon esprit. Profitez juste de Yamaku pendant que vous y êtes."

show lilly basic_weaksmile_cas_close
with charachange


"Lilly soupire à la différence qui existe entre Akira et nous deux."

show lilly basic_reminisce_cas_close
with charachange


li "Tu as vraiment besoin de retourner en Écosse ?"

show akira basic_resigned_close
with charachange


aki "Ouais. Les vieux sont déjà assez énervés contre moi comme ça."


hi "Tu ne pensais pas rester aussi longtemps ?"

show akira basic_ending_close
with charachange


"Elle affiche son petit sourire habituel."


aki "Obtenir un visa pour mon petit copain a pris du temps."


hi "Il part avec toi ?"

show akira basic_smile_close
with charachange


aki "Juste pour un moment dans un premier temps. Il est étonnamment ouvert au monde, alors je crois qu'il s'en sortira bien."

show akira basic_lost_close
with charachange


"Akira sort un petit rire moqueur."


aki "Si notre père le pouvait, il m'aurait fait rentrer il y a longtemps déjà."

show akira basic_laugh_close
with charachange


aki "Je n'ai juste pas pu m'empêcher de trouver une excuse pour rester avec ma petite sœur favorite un peu plus longtemps."

show lilly basic_smileclosed_cas_close
with charachange


"Elle se penche à droite et étreint Lilly d'une façon joueuse, lui remontant le moral considérablement."


li "C'est bien d'être avec toi une dernière fois."


hi "Pour ce que ça vaut, je pense la même chose."

show akira basic_smile_close
with charachange


aki "Bah, merci à vous deux. J'essayerai de revenir de temps en temps, ne vous inquiétez pas."

show lilly basic_reminisce_cas_close
with charachange


li "C'est dommage que ton travail te prenne autant de temps."

show akira basic_lost_close
with charachange


aki "La boîte ne tournera pas toute seule, j'en ai bien peur, et je pense que ça va être la même chose là-bas."

show akira basic_smile_close
with charachange


aki "En en parlant, je ferais mieux d'y aller."


hi "Amuse-toi bien là-bas, Akira."

show akira basic_laugh_close
with charachange


aki "Haha, ouais."

show akira basic_smile_close at right
with dissolvecharamove


"Avec un léger grognement, elle appuie sur ses mains pour se relever."

show akira basic_lost_close at right
with charachange


aki "Bon. J'y vais. L'avion ne m'attendra pas, après tout."


"Il y a une certaine mélancolie dans sa voix et elle fixe sa sœur du regard."

show lilly basic_weaksmile_cas_close
with charachange


li "J'irai bien, Akira."

show akira basic_resigned_close
with charachange


aki "Ouais, je sais."

show lilly basic_smileclosed_cas_close
with charachange


li "Allez, c'est pas si mal. On se reverra bientôt."


"C'est bizarre de voir Lilly rassurer Akira pour une fois. Elle a vraiment changé."

show lilly basic_smile_cas_close
with charachange


li "Au revoir, Akira."


hi "Salut."

show akira basic_smile_close
with charachange


"Pendant une seconde, Akira, toute de noir vêtue, nous regarde un moment, avec un grand sourire. Je ne l'avais sûrement jamais vue avec un aussi grand sourire."

show akira basic_boo at tworight
with charadistant


"Elle prend une grande inspiration avant de partir, met une main dans sa poche et tourne les talons."


"Et alors qu'elle marche, elle garde une main en l'air."

show akira basic_ending
with charachange


aki "À plus, vous deux !"

hide akira
with charaexit


"Une musique de jazz sans rythme, ni mélodie ou ligne directrice, jusqu'à la fin."

show bg lilly_hilltop at bgright
show lilly basic_smileclosed_cas_close at center
with dissolvecharamove


"Après un moment en silence, Lilly et moi nous relevons."


"Me tournant vers elle avec un large sourire, je tends la main."


hi "On y va ?"


"Elle prend ma main dans la sienne, avec un petit hochement de tête et un sourire aussi magnifique et chaleureux qu'il a toujours été."

show lilly basic_cheerful_cas_close
with charachange


li "On y va, Hisao."

scene unlock_ev lilly_goodend
show evbg lilly_goodend:
    truecenter
    zoom 3.0 subpixel True
    1.0
    linear 0.5 zoom 0.9
    easein 12.0 zoom 0.8
show evfg lilly_goodend:
    truecenter
    zoom 6.0 subpixel True
    1.0
    linear 0.5 zoom 1.2
    easein 12.0 zoom 0.8
with whiteout


"Alors que nous partons en direction de l'école, ce merveilleux sourire se grave dans ma mémoire. Ce merveilleux sourire que nous partageons tous les deux."


"Nos passés sont peut-être parfois couverts par une ombre de tristesse, mais ils sont aussi une partie irrévocable de nos vies et de nos personnalités. Même si je pouvais le changer, je ne le ferais pas. Parce que c'est mon passé qui m'a amené jusqu'ici."


"C'est pourquoi, même avec tout ce qui nous est arrivé et tout ce qui pourra nous arriver... ensemble, nous continuerons de marcher vers l'avant."


"Vers l'avant... vers l'avenir. Notre avenir."

window hide Dissolve(1.0)

stop ambient fadeout 2.0
stop music fadeout 2.0

scene black
with Dissolve(1.0)

with Pause(1.0)

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
