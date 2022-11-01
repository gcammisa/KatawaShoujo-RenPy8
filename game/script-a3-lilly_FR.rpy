label fr_L9:

window hide None

scene black
with dissolve

scene bg misc_sky at Fullpan(10.0)
with locationchange

$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_normal fadein 3.0

window show


"Le menton posé sur la main, je regarde par la fenêtre, les yeux dans le vague. Mutou dicte une leçon, une de celles dont on ne voit pas la fin."


"Le ciel d'été est presque beau avec ses couleurs azur. Seul un petit nuage vient briser cette grande étendue bleue."


"Ce sentiment de nostalgie, soufflé de l'extérieur, me donne envie de m'échapper."


mu "Nakai, peux-tu répondre à ça ?"


"Mais cette envie ne peut être satisfaite."

scene bg school_scienceroom
show muto normal at center
with locationchange


hi "Dans ce cas... je crois que ce serait le suffixe -ane ?"

show muto smile
with charachange


mu "Correct. Donc le suffixe pour..."


"Une fois ma réponse faite, mon attention pour le cours s'évanouit de nouveau. Je remarque Misha qui m'adresse un pouce levé. Je lui fais un hochement de tête en retour."

scene bg school_scienceroom
with shorttimeskip


"Ça fait plusieurs jours que Lilly est partie pour l'Écosse, jours qui se sont passés paisiblement."


"Contrairement à ce que j'aurais pensé, la vie continue son cours habituel. Bien que des pensées pour Lilly dansent dans ma tête depuis qu'elle est partie, les évènements présents arrivent à les contenir. Du moins pour l'instant."


"Je me retrouve donc à parler avec Hanako de tout et de rien, comme d'habitude, quand l'heure du déjeuner arrive."

show hanako basic_normal
with charaenter


ha "Les derniers qui sont sortis sont aussi bien ?"


hi "Pas vraiment. Tu ferais mieux de te contenter de l'original. Ses derniers livres n'ont pas tenu le niveau, sauf peut-être “Le Dieu Empereur”."

show hanako basic_bashful at center
with charachange


ha "Merci, je n'étais pas vraiment sûre que..."

show misha invis at offscreenleft
show shizu invis at offscreenleft
with None

show hanako defarms_shock at right
show shizu behind_blank at center
show misha hips_smile at left
show bg school_scienceroom at bgright
with dissolvecharamove


"Alors que Hanako se décale sur le côté, je vois Shizune arriver avec sa démarche professionnelle habituelle, suivie par son ombre aux cheveux roses."


"J'ai beau essayer, je n'arrive pas à savoir ce qu'elles veulent. Le visage neutre de Shizune et l'expression joyeuse de Misha forment une combinaison diabolique."


hi "Salut Shizune, salut Misha."

show hanako emb_timid
with charachange


ha "Euh... salut."

show shizu basic_normal
with charachange


"J'ajoute un hochement de tête en direction de Shizune avec ma salutation pour faire passer le message. Elle nous renvoie la gestuelle."


"Ça fait longtemps que je n'ai pas eu une vraie conversation avec elles. Pendant un moment je croyais qu'elles m'évitaient, mais j'ai fini par conclure que Shizune n'est pas ce genre de personne."

show shizu adjust_happy
with charachange

shi "…"

show misha sign_smile
with charachange


mi "Bonjour~ ! Shicchan dit que Mutou veut te parler quand tu auras le temps."


"À l'écoute de cette phrase, je fais une grimace, comme si je venais de manger quelque chose d'avarié, ce qui amuse Misha."

show misha cross_laugh
with charachange


mi "Wahahaha~ ! On pourrait penser que tu vas avoir des problèmes, Hicchan !"

show shizu behind_smile
with charachange

shi "…"

show misha perky_smile
with charachange


mi "Tu n'en as peut-être pas conscience, mais tu es celui qui a le moins à s'inquiéter de toute la classe."

show hanako emb_smile
with charachange


"Je ne m'attendais pas à une telle remarque. Même Hanako hoche la tête pour confirmer."


hi "Merci, je m'en rappellerai. Il y avait quelque chose que je voulais te demander d'ailleurs."

show shizu basic_normal
with charachange

shi "…"

show misha hips_smile
with charachange


mi "Et qu'est-ce donc, Hicchan ?"


"J'ai le sentiment que ça ne se finira pas très bien, mais au point où j'en suis..."


hi "Il y a une raison pour laquelle Lilly et toi ne vous entendez pas ? Je pense que quelques efforts vous aideraient dans votre travail."

show shizu cross_angry
with charachange


"Le regard froid de Shizune après que Misha lui ait traduit ma phrase me paralyse. En y repensant, j'aurais pu mieux choisir mes mots."

show hanako emb_sad:
    xpos 1.05
with dissolvecharamove


"Du coin de l'œil, je suis sûr d'avoir vu Hanako reculer. Juste un peu."

show shizu basic_angry
with charachange


"Heureusement, Shizune s'en rend compte et se calme en se passant la main dans les cheveux pour dissiper sa colère. Sur le qui-vive, Misha se met à interpréter ce que commence à dire le second bras de Shizune."

show shizu behind_frown
with charachange

shi "…"

show misha hips_frown
with charachange


mi "Je dirais bien que ce genre de chose ne te regarde pas, mais vu que tu sembles être devenu ami avec Lilly..."

show shizu adjust_frown
with charachange


"Elle s'arrête et réajuste ses lunettes, essayant de trouver le meilleur moyen de continuer."

show shizu basic_angry
with charachange

shi "…"

show misha sign_smile
with charachange


mi "Bien que ça doit être pareil pour elle, je ne suis pas vraiment impartiale sur le sujet. Cela dit, nous étions plus proches avant."

show shizu behind_frown
show misha sign_confused
with charachange


"Shizune fait un signe à Misha pour lui dire d'arrêter de traduire, puis elles échangent quelques phrases. Le fait qu'elles puissent communiquer aussi facilement et pourtant si secrètement juste devant nous est légèrement déconcertant."

show hanako basic_normal
show shizu basic_normal2
show misha sign_sad
with charachange


"Hanako semble partager ma curiosité, ayant l'air quelque peu intéressée. Alors qu'elles finissent leur conversation inaudible, Misha semble légèrement déçue. Je pense que son opinion sur le sujet n'a pas été prise en compte."

show misha perky_confused
with charachange


mi "Shicchan dit que tu devrais plutôt demander à Lilly, qu'elle ne veut pas être celle qui t'implique dans tout cela."


"Ah. J'aurai juste à lui demander quand elle reviendra. Au moins j'ai réussi à avoir certaines informations grâce à Shizune, elles étaient proches avant et n'étaient pas toujours sur le dos l'une de l'autre. Ou du moins pas à ce point."


hi "D'accord. Merci quand même."

stop music fadeout 8.0

show shizu invis at offscreenleft
show misha invis at offscreenleft
show hanako basic_normal at center
show bg school_scienceroom at center
with dissolvecharamove


"Après un hochement de tête et un au revoir, elles s'en vont toutes les deux, se dirigeant sans doute en direction de la salle du conseil des étudiants."


hi "...Ça aurait pu être pire j'imagine."

show hanako cover_bashful
with charachange


"Hanako laisse échapper un long soupir, contente que la confrontation soit finie. Je ne peux pas lui en vouloir."

show hanako basic_bashful
with charachange


ha "Je te vois tout à l'heure alors ?"


hi "Ouais, je te rejoindrai dans la salle habituelle. À plus."

hide hanako
with charaexit


"Sur ce, elle me fait un signe de la main et rejoint le groupe d'étudiants sortant de la classe."

show muto normal at center
with charaenter


mu "Nakai, je peux te parler un moment ?"


"Il dit cela à sa manière monotone habituelle. Il pense apparemment que j'ai besoin qu'il me rappelle que je dois lui parler."

hide muto
with charaexit


"Je finis finalement de remballer mes affaires. Au moment où j'arrive à son bureau, la classe est presque vide."


hi "Euh... oui, monsieur ?"

play music music_happiness fadein 5.0

show muto normal at center
with charaenter


"Il lève la tête, regarde mon expression avant de sortir un rire bizarre, visiblement forcé."

show muto smile
with charachange


mu "Pas besoin de t'inquiéter, je n'ai rien à te reprocher. Je veux juste te poser une question que j'ai déjà posée à d'autres étudiants."


"C'est déjà ça. Pendant un moment je croyais que ma méthode qui consiste à garder la tête basse et le stylo actif avait échoué."


hi "Donc qu'est-ce que vous vouliez me demander ?"

show muto normal
with charachange


mu "Pour commencer, qu'est-ce que tu penses de ta progression en classe jusque-là ? Bonne ? Mauvaise ?"


"Je déteste ce genre de question. Pendant un moment j'essaye de penser à une réponse qui n'est ni trop humble ni trop vantarde."


hi "Je crois que je m'en sors bien. Ce n'est pas trop dur, et je m'en sors mieux avec les examens que je ne l'aurais cru."

show muto smile
with charachange


mu "C'est une bonne réponse. Bien dite de surcroît."


"Je soupire mentalement, de soulagement. Dire que je ne suis pas fier de son commentaire serait mentir."


"Dans le maelström de pensées qui habitaient ma tête après avoir appris que je serais transféré à Yamaku, les notes semblaient peu importantes."


"Je ne savais pas du tout quel niveau on attendrait de moi, alors une fois que je me suis rendu compte que je pouvais suivre sans trop de problèmes, j'ai été soulagé."

show muto normal
with charachange


mu "Je sais que les circonstances n'aident pas, mais as-tu déjà pensé à ton avenir ?"


hi "Mon avenir ?"


mu "Ce que tu aimerais faire comme métier. As-tu une idée de où tu seras dans dix ou vingt ans ?"


mu "Je ne serais pas surpris que ce sujet ait déjà été abordé dans ton école précédente, mais je n'en ai aucune trace."


"Je suppose que la dernière année du lycée est le moment où les étudiants doivent penser à ce genre de choses. Pour être honnête, vu ma situation actuelle, je ne m'en suis pas soucié."


"Voyant mon visage indécis, Mutou répond tout seul."


mu "Ce n'est pas grave si tu n'as rien décidé de précis encore. Je ne serais pas surpris que beaucoup de tes camarades soient aussi indécis après tout. Peut-être que tu pourrais poursuivre dans un des domaines dans lesquels tu es bon ?"


"Il essaye visiblement de me faire répondre, et quelque chose à la fin de sa dernière phrase me rend suspicieux."


"Il ne semble pas avoir ce genre de discussion avec tout le monde, alors il doit avoir une sorte de critère de sélection. Probablement nos notes dans son cours."


hi "Eh bien, quelque chose dans le domaine de la science devrait m'être peu difficile."


"Son visage s'illumine, aucun doute que la pensée qu'un de ses étudiants puisse choisir sa matière comme chemin de carrière lui fasse grandement plaisir."

show muto smile
with charachange


mu "Bien. Avoir une idée générale est le premier pas. Cependant, je te conseille de continuer à y penser."


hi "Bien sûr. Ma situation est plutôt stable en ce moment, ça va simplifier les choses."


mu "Tant mieux. Oh, et j'ai remarqué que le taux de présence d'Ikezawa a augmenté depuis que vous êtes devenus amis. J'aimerais te remercier pour cela ."


hi "Ça me surprend que vous sachiez que nous sommes amis."


"Il me sort un rire aussi bizarre que quand il sourit."


"Ce gars ne sait vraiment pas comment réagir avec les gens. Chaque expression de sa part semble être forcée et difficile."

show muto normal
with charachange


mu "Savoir ce genre de choses est aussi une part du travail d'enseignant."


"Se retenant de partir dans un autre sujet, il tousse bruyamment dans sa main."


mu "Je suis sûr que tu as des choses à faire aussi, donc je vais m'arrêter là. Essaye de penser un peu à ton avenir, il te reste peu de temps avant la fin du lycée."


"J'y penserai. Merci."

stop music fadeout 4.0

scene bg school_hallway3
with locationchange


"La conversation s'arrêtant là, je pars. Mutou quant à lui retourne à tous ses papiers sur le bureau."


"C'est une des choses que j'envie à Lilly, c'en est presque fatigant. Avoir un avenir si clair et assuré et y travailler à un âge si jeune..."


"C'est si étrange pour moi, qui me suis toujours contenté de vivre au jour le jour."

scene black
with dissolve



label fr_L10:

scene bg school_lobby
with locationchange


"Marchant dans le couloir pour aller à la cafétéria, je regrette silencieusement que ma routine quotidienne ait été complètement chamboulée."


"Ça semblait être un jour normal ; je me réveille tôt et réussis à avaler mes pilules sans m'étouffer puis j'arrive en classe avant la plupart des autres élèves."


"Mais alors que les étudiants arrivaient un par un, une ne s'est jamais montrée. Hanako."

play ambient sfx_crowd_indoors fadein 0.5
scene bg school_cafeteria at right
show crowd at left
with locationchange


"J'arrive à la cafétéria, cherchant une place pour m'asseoir. C'est une tâche difficile avec tous les groupes d'étudiants se déplaçant et discutant."

play sound sfx_impact2
with vpunch
$ renpy.music.set_volume(0.5, 0.3, channel="ambient")


hi "Argh !"


"Une main me frappe plusieurs fois dans le dos, me prenant par surprise."

$ renpy.music.set_volume(0.0, 0.0, channel="ambient")
scene black
with shuteyefast


"Je me moque complètement du coupable, me concentrant sur ma poitrine presque par réflexe."

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)


"Ma main se resserre instinctivement sur ma poitrine, alors que je passe par toutes les étapes que je révise dans ma tête chaque jour."

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)


"Respirer calmement... inspirer... et expirer..."

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)


"Je peux sentir ma poitrine devenir moins tendue, ce qui me rassure. Au moment où je relève la tête, mon visage est couvert de sueur."

$ renpy.music.set_volume(1.0, 5.0, channel="ambient")

scene bg school_cafeteria at right
show crowd at right
show kenji happy_close at center
with openeye


ke "Hé... mec, ça va ?"


hi "BORDEL ! Ne fais {b}pas{/b} ça, idiot !"

show kenji tsun
with charadistant


"Il recule, une expression gênée sur le visage. Je n'aurais probablement pas dû crier comme ça, il ne pouvait pas savoir."


"Je soupire et me ressaisis avec quelques difficultés."


hi "Désolé. J'ai juste un... problème à la poitrine. Les coups ne sont pas une bonne idée."


"C'est bizarre de le voir si chamboulé. Le fait que je ne puisse rien y faire m'embête."


hi "Allons prendre à manger."

show kenji neutral
with charachange


ke "D'accord. C'est bien d'avoir un peu de compagnie, pour une fois."

hide kenji
with charaexit

show bg school_cafeteria at left
show crowd at left
with charamove


"Nous commençons à faire la queue pour manger. Maintenant, je peux parler de tout et de rien avec Kenji, alors qu'avant nos seuls échanges tournaient autour de ses discours antiféministes. C'est appréciable."


hi "On dirait que ça va être dur de trouver une table libre."

show kenji neutral at center
with charaenter


ke "Il y a des gens avec qui ça ne me gênerait pas de manger. Mais tu as quelque chose de plus."

$ renpy.music.set_volume(0.0, 0.5, channel="ambient")


"Je sens un frisson remonter le long de mon échine."


hi "Quoi de plus ?"

play music music_kenji fadein 2.0

show kenji tsun
with charachange


ke "Ils n'écoutent pas. Leurs esprits sont fermés. C'est les médias, mec, les fichus médias lobotomiseurs féministes fascistes."


"Il prend sa respiration et je savoure la seconde de silence."

$ renpy.music.set_volume(1.0, 10.0, channel="ambient")


ke "Merde, elles contrôlent tout. Tout sauf toi et moi."


"Je me relaxe un peu pendant que nous prenons notre repas."

show kenji happy
with charachange


ke "Donc, qu'est-ce que t'as pour moi ?"


hi "Hein ?"

show kenji neutral
with charachange


ke "Allez, tu traînes avec Satou et l'autre fille depuis des lustres déjà. Il y a des rumeurs dans ma classe et probablement aussi dans d'autres classes."


hi "Tu ne devrais pas écouter les ragots."

show kenji happy
with charachange


ke "Laisse-moi deviner, tu ne le fais jamais ? Même pas quand tu t'ennuies ? Vraiment ?"


hi "Eh bien... je... euh..."


hi "D'accord. Tu as raison sur ce coup."

hide kenji
with charaexit


"Nous nous arrêtons tous deux pour avoir un bol de soupe et le plaçons sur notre plateau. Cette mixture est plutôt discutable, mais au moins, elle sent bon."

stop ambient fadeout 1.0

show bg school_cafeteria at center
show crowd at Alphaout(1.0), center
show kenji invis at center
with charamove

show kenji neutral:
    ypos 1.14
hide crowd
with dissolvecharamove


"Nous nous asseyons à une table miraculeusement libre et j'essaye de penser à quelque chose qui pourrait l'intéresser. J'espère pouvoir trouver un sujet de conversation correct."


hi "J'ai trouvé la réponse à la question que tu m'as posée il y a quelques semaines. Les origines étrangères de Lilly."

show kenji happy
with charachange


ke "C'est bien ça mec. C'est la Russie, nan ? C'est trop la Russie."


hi "L'Écosse."

show kenji tsun
with charachange


"Il semble paralysé par mes propos."


ke "...Écosse ?"


hi "Ouais, c'était ma réaction aussi. Elle parle anglais couramment et tout."

show kenji rage
with charachange


ke "...Merde ! Tu réalises ce que ça veut dire ? À quel point cette nouvelle est horrible pour moi ?"

label fr_choiceL10_1:
menu:
    with menueffect
    "Je crois qu'il fait de l'hyperventilation. S'évanouir pendant un petit moment le relaxerait sûrement."
    "Aller dans son sens.":




        return m1
    "Ignorer ses délires.":


        return m2

label fr_L10a:


hi "Aucune idée de ce que ça représente. Éclaire-moi."


ke "Je viens de perdre 1000 yen, mec ! 1000 yen ! Merde, c'est le pire jour de ma vie."

label fr_L10b:


"Je commence à manger, espérant qu'il comprenne la raison de mon silence."


ke "Je viens de perdre 1000 yen, mec ! 1000 yen ! Merde, c'est le pire jour de ma vie."


"Ça ne marche pas vraiment."

label fr_L10c:


hi "Sérieux, tu as parié sur sa nationalité ?"

show kenji tsun
with charachange


ke "Un des mecs de ma classe se posait la question. Je lui ai fait part de ma sagesse, et il a eu l'audace de dire que ma logique était erronée."


hi "Qu'est-ce qu'il croyait lui ?"


ke "Euh, Allemagne ou un truc du genre. Peu importe. Ce qui importe ce sont mes 1000 yen."

show kenji rage
with charachange


ke "Merde, ma journée est gâchée à cause d'elle. Quelle pétasse."

show kenji tsun
with charachange


"Il a l'air vraiment dévasté pendant qu'il mange son riz pâteux trempé dans la sauce soja. Il ne prend que quelques bouchées avant de pointer ses baguettes vers moi, les remuant avec un air inspiré."


ke "Pourquoi... mm... mm... est-ce que... mm..."


hi "Ta mère ne t'a jamais appris à ne pas parler la bouche pleine ?"


"Il m'adresse un drôle de regard avant d'avaler ce qui lui restait dans la bouche et de prendre une gorgée de soupe. C'est plutôt inélégant."


"Me rappelant que j'ai aussi à manger en face de moi, je décide de finir le repas de la cafétéria le plus rapidement possible. Plus vite j'aurai terminé, plus vite je pourrai en finir avec cette expérience."

show kenji neutral
with charachange


ke "Donc comme je disais,"

show kenji tsun
with charachange


ke "Pourquoi est-ce que quelqu'un voudrait vivre dans un endroit comme ça ? Je veux dire, qu'est-ce qu'il y a à voir ? Des plaines. C'est tout. Des tas et des tas de plaines."


ke "Et des hommes en kilts."


"Je ne sais pas tellement ce qui est le pire : La nourriture, ou bien sa vision du monde. Je peux sentir mon visage faire une grimace un peu à cause des deux. Mais il ne le remarque pas. Ou bien ne s'y intéresse pas."


hi "Ce n'est pas si mal. Pourquoi ça t'intéresse tant après tout ? Elle est juste ta déléguée de classe, c'est tout."

show kenji neutral
with charachange


"Il ricane diaboliquement. Si c'était quelqu'un d'autre que Kenji, je me sentirais mal pour lui."


ke "J'ai enfin trouvé la faille dans l'armure de la légion féministe. Ça m'a pris un moment, mais j'ai confiance dans le fait que c'est comme ça que je vais faire tomber tout le système."

show kenji happy
with charachange


ke "Je suis sur le point de faire une révélation monumentale. Tu es prêt ?"

stop music fadeout 2.0


"Je reste silencieux un moment le temps de finir mon riz et de commencer la soupe peu appétissante. Une gorgée est suffisante pour me confirmer qu'elle est froide."


hi "Aussi prêt qu'on puisse l'être."

show kenji happy
with charachange


ke "J'ai la preuve que Lilly est dans la Mafia."

play music music_kenji


hi "Quoi ?"

show kenji neutral
with charachange


ke "Bon, reste avec moi une seconde et je te décris la scène."


"J'aimerais avoir le choix."


ke "Lilly est là, marchant dehors après les cours."


hi "Tu ne l'espionnes pas j'espère ?"

show kenji tsun
with charachange


ke "Non ! Merde mec, j'ai quand même un peu d'instinct d'auto-préservation."


"Mais pas de dignité, ou de morale, ou de notions de comportement en société..."

show kenji neutral
with charachange


ke "Bref, une voiture se gare à côté d'elle et devine qui en sort ? Un homme en costume rayé. Il lui fait signe, elle monte dans la voiture et ils partent. Je te le dis mec, elle est sous protection. Sous. Protection."


"Un homme dans un... oh. Je comprends maintenant. Il me faut un effort pour ne pas soupirer d'exaspération."


hi "Laisse-moi deviner, il était de taille normale, avait une constitution assez fine, cheveux blonds, l'air étranger, et souriait beaucoup ?"

show kenji rage
with charachange


"Il a l'air totalement ébahi. Je profite du moment de silence pour avaler une autre gorgée de soupe froide."

show kenji tsun
with charachange


ke "On dirait que tu es plus observateur que je le croyais."

show kenji neutral
with charachange


ke "Oui. Je t'ai bien choisi."


"Il rit un peu et hoche la tête tout seul d'une manière si dramatique que c'en est comique. Aucune idée de si c'est intentionnel ou non."

show kenji happy
with charachange


ke "La mafia a un important réseau tu sais. Si elle est vraiment connectée à des gens comme eux et qu'on se sert bien de cette information, ça pourrait devenir notre meilleure arme contre le Conseil des Étudiants."

show kenji happy:
    2.0
    "kenji neutral" with Dissolve(0.5, alpha=True)
    3.0
    "kenji happy" with Dissolve(0.5, alpha=True)
    1.0
    "kenji neutral" with Dissolve(0.5, alpha=True)
    4.0
    "kenji tsun" with Dissolve(0.5, alpha=True)
    repeat


"À partir du moment où il commence à déblatérer sur la conspiration, ma soupe devient soudainement plus importante."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

nvl clear

window hide
nvl show dissolve


n "\n\n\n\nÉcoutant seulement à moitié ce qu'il dit, mes pensées se dirigent vers Lilly et son antipathie pour Shizune."


n "Le passé entre elles devient de plus en plus clair, mais je ne suis pas sûr que ce soit une bonne idée que j'approfondisse cela. Même si j'arrive à savoir ce qui s'est passé, ce ne sont vraiment pas mes affaires."


n "...Zut, le fait que Lilly ne soit pas là me fait divaguer. Je m'ennuie beaucoup plus sans sa compagnie et je suis plus renfrogné. Et c'est la même chose pour Hanako. Tout ce que nous faisons durant le temps de midi, c'est manger et jouer aux échecs."


n "En y pensant, je dois aller voir Hanako après les cours, aussi. Vu qu'elle venait beaucoup plus souvent à l'école récemment, je suppose qu'il se passe quelque chose pour qu'elle ne vienne pas."

stop music fadeout 2.0
$ renpy.music.set_volume(1.0, 6.0, channel="music")

nvl clear

nvl hide dissolve

scene bg school_scienceroom
with shorttimeskip

play sound sfx_normalbell

window show


mu "Oh, Nakai ?"

show muto normal at center
with charaenter


"Je m'arrête alors que je suis sur le point de sortir de la classe, tournant la tête pour voir Mutou. Il me tend avec son grand et maigre bras les feuilles sur lesquelles on a travaillé aujourd'hui."

show muto smile
with charachange


mu "Tu pourrais les donner à Ikezawa ? Je demanderais normalement à une des filles de le faire, mais je suppose que tu iras voir comment elle va."


"Pendant un moment je considère la possibilité que ce soit plus qu'une innocente prédiction. Je repousse vite cette idée, vu qu'il est difficile d'imaginer Mutou agir comme cela. Ce n'est pas dans sa nature."


hi "Ok, pas de problème."

scene bg school_girlsdormhall
with locationskip

play music music_night fadein 1.0


"Marchant le long du couloir du dortoir des filles, je cherche des explications quant à l'absence de Hanako. La plus évidente d'entre elles est qu'elle a simplement attrapé un rhume."


"Cela dit, elle peut ne pas être malade du tout. Ça fait presque une semaine que Lilly est partie, et malgré le fait qu'elle essaye de paraître normale, je crois bien qu'elle a plus de mal qu'elle ne le laisse croire."

show bg school_girlsdormhall at right
with charamove


"Finalement j'arrive devant la chambre de Hanako, une simple porte marron nous séparant. La position de sa chambre à côté de celle de Lilly est très pratique et c'est probablement à cause de cela qu'elles se sont rencontrées."

$ renpy.music.set_volume(0.5, 0.0, channel="sound")
play sound sfx_doorknock2


"Grimaçant légèrement en l'imaginant malade, je frappe à la porte."


"...Silence. J'écoute attentivement à travers la porte, mais n'entends rien."

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_doorknock2


"Je frappe encore une fois à la porte, un peu plus fort."


"Toujours aucune réponse. Étrange."

$ renpy.music.set_volume(0.5, 0.0, channel="sound")
play sound sfx_dooropen

show bg school_girlsdormhall at center
with charamove


"Une porte s'ouvre derrière moi. Une fille que je ne connais pas, avec des taches de rousseur et quelque peu frêle, est surprise par ma présence."

label fr_choiceL10_2:
menu:
    with menueffect
    "Fille" "Euh... salut."
    "Demander pour Hanako.":




        return m1
    "Ne rien dire.":


        return m2

label fr_L10d:


"En fait, elle pourrait m'aider."


hi "Salut. Excuse-moi, est-ce que tu sais si Hanako est sortie de sa chambre aujourd'hui ? Elle ne répond pas quand je frappe."


"Fille" "Ikezawa, c'est Ikezawa. Le fait qu'elle ne réponde pas est totalement normal. Elle accepte de ne parler qu'à la grande fille avec un air étranger."


"Elle hausse les épaules avant de s'en aller, ayant des choses plus importantes à faire que de s'occuper de Hanako ou de moi."


"Son attitude m'énerve."


"Hanako doit avoir une réputation de solitaire. Une réputation qu'elle n'a pas volée, du moins c'est ce que je pensais avant de la rencontrer."

label fr_L10e:


hi "Désolé, ne fais pas attention à moi."


"Dans son intérêt, je crois que la situation de Hanako devrait rester aussi privée que possible. Je ne sais pas ce qui lui est arrivé mais mon instinct me dit que ce n'est pas une maladie qui l'a fait rester ici."


"Elle n'a pas besoin que des rumeurs circulent à son sujet. Bien que cela me gêne de le dire, Hanako préfèrerait sûrement garder son statut d'élève bizarre à qui on ne parle pas, plutôt que l'on parle d'elle dans son dos."


"Fille" "Peu importe."


"Sur ce, elle tourne les talons et s'en va sans me dire au revoir. Malpolie."

label fr_L10f:

show bg school_girlsdormhall at right
with charamove

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_doorknock2


"Me grattant la tête, je frappe encore une fois à la porte, dans une ultime tentative d'avoir une réponse de Hanako."


hi "Hanako, c'est juste moi. Mutou m'a demandé de te donner des trucs."


"Pendant un moment, cette tentative semble aussi inutile que les précédentes. Juste avant que je ne glisse les feuilles sous la porte, j'entends la poignée se tourner."

play sound sfx_dooropen
with Pause(1.5)

show hanagown distant:
    xpos 1.0 xanchor 0.75
with charamoveinright


"Alors que la porte s'ouvre à moitié, je fais de mon mieux pour ne pas trop regarder Hanako. C'est une tâche quelque peu difficile à cause de ses cicatrices qui s'étendent autant sur son corps."


"Elle n'a pas l'air malade. Pour être honnête, j'aurais préféré qu'elle soit malade plutôt qu'elle fasse cette tête."


hi "Salut, Hanako. Mutou voulait que je te donne ces feuilles, vu que tu n'étais pas en cours."


"Je lui tends les feuilles, qu'elle prend. La façon dont elle bouge est étrange, sans vie. Cette manière de faire ressemble davantage à un automate mécanique qu'à un être vivant."


hi " Est-ce que... tu vas bien ? Si tu te sens mal ou si ça ne va pas, je peux aller chercher l'infirmier."


"Ça me fait presque pitié de devoir sortir le classique “prends soin de toi”. Je n'arrive pas à savoir ce que je pourrais faire d'autre pour elle."

show hanagown normal:
    xanchor 0.7
with dissolvecharamove


"Elle semble se ressaisir en m'écoutant... mais seulement un peu."

show hanagown distant_blush
with charachange


ha "Je vais bien."


hi "D'accord."

stop music fadeout 6.0

with Pause(2.0)

hide hanagown
with charamoveoutright

play sound sfx_doorclose


"Un étrange silence s'ensuit, finissant par un hochement de tête de sa part en guise d'au revoir, et elle ferme la porte. La scène entière était vraiment étrange."


"Plus qu'un peu troublé, je retourne dans ma chambre en espérant qu'elle ira mieux demain, même si je ne sais pas pourquoi elle ne va pas bien."

scene black
with dissolve



label fr_L11:

show bg school_girlsdormhall at right
with locationchange


"Une fois encore, je me trouve en face de la porte de Hanako après une autre de ses absences inexpliquées de la classe."

play sound sfx_doorknock2

"…"

play sound sfx_doorknock2

"…"


"Rien. Étant donné que c'est le deuxième jour d'affilée que ça arrive, je commence à m'inquiéter."


"M'armant de courage, j'essaye une dernière chose pour la faire répondre."


hi "Hanako, si tu ne dis rien, je vais aller chercher l'infirmier."


ha "...Va-t'en."

play music music_hanako fadein 10.0


"Qu... quoi ? C'est dur de dire si c'est un ton dépressif ou énervé, ou les deux. Qu'est-ce que je peux faire pour elle, si elle ne veut pas être aidée ?"


"Le message est suffisamment clair. Je ne peux pas la laisser comme ça cela dit, à juste rester dans sa chambre pendant des jours entiers."


"Me frottant les tempes pour réfléchir, je retourne dans ma propre chambre pour penser à ce que je peux faire. Je dois rationaliser ; insister pourrait aggraver les choses."

scene bg school_dormhisao
with shorttimeskip


"Tiroir après tiroir de mon bureau, je cherche où j'ai pu mettre cette fichue feuille."


"Avant qu'elle ne parte, Lilly m'a donné le numéro où je pouvais la joindre pendant qu'elle serait en Écosse et je l'ai écrit. Maintenant que j'en ai besoin, je n'arrive pas à—"


"Ah. Ici."


"J'aurais probablement dû l'enregistrer directement dans mon téléphone, en y repensant. Sans tergiverser davantage, j'entre les chiffres et presse anxieusement le bouton vert."

scene bg school_dormhisao_blurred
show phone mobile:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with locationchange
with Pause (0.5)


"Le fait que ça sonne montre au moins que le préfixe pour appeler en Écosse est le bon. C'est la première fois que j'appelle à l'étranger, alors ça me rassure."


"Finalement ça décroche, une voix féminine que je ne connais pas me répond. C'est probablement la mère de Lilly."

$ renpy.music.set_volume(0.5, 0.2, channel="music")


mystery "{image=vfx/garbage.png} {image=vfx/garbage.png} Satou {image=vfx/garbage.png}?"


"De l'anglais ? Me trouvant soudainement pris au dépourvu, je réalise que je ne comprends pas un mot de ce qu'elle dit, à cause de mon vocabulaire limité, ou de son fort accent. J'aurais dû m'y attendre, vu que, d'après Lilly, sa mère est écossaise."


"Je me lance en japonais, avec l'espoir qu'elle le parle un minimum, vu que c'est la langue native de sa fille."


hi "Euh... Je suis Hisao Nakai..."


"Elle semble reconnaitre instantanément la langue. Mon soulagement est immense."


"Mme Satou" "Ah, tu dois être un des amis d'école de Lilly, non ?"


"Même là, son accent me force à me concentrer pour comprendre ce qu'elle dit."


hi "Oui, c'est exact. Enchanté de faire votre connaissance, Mme Satou."


"Mme Satou" "C'est plaisant de trouver quelqu'un d'aussi poli ! Lilly chérie, c'est pour toi !"


"Sa mère semble gentille, même si elle est un peu trop enthousiaste étant donné la situation banale."


"Il y a un petit silence alors que Lilly prend son temps pour arriver au téléphone. Au loin, je peux entendre sa mère lui reprocher gentiment de ne se lever que maintenant."

$ renpy.music.set_volume(1.0, 5.0, channel="music")


li "Bonjour, qui est à l'appareil ?"


hi "Ta voix est épouvantable."


"Sa voix est comme un mélange entre un animal agonisant et un bâillement."


"La seule chose dont je me suis rappelé avant de téléphoner a été de vérifier le décalage horaire. C'est la fin de matinée là-bas, donc elle n'a aucune excuse."


hi "Tu ne te sens pas bien ?"


li "Juste fatiguée. Quelle heure est-il là-bas ?"


hi "Fin d'après-midi. L'école est finie depuis un petit moment."


hi "Tu n'es vraiment pas du matin, n'est-ce pas ?"


li "Je n'ai pas besoin que tu te moques de moi en plus..."


"Il me faut un peu de volonté pour me retenir de rire à son gémissement. Pauvre petite."


hi "Comment ça va là-bas, mis à part le fait que tu aies du mal à te lever ?"


li "C'est bien. Comme je ne les avais pas vus pendant si longtemps, le seul fait de partager un repas avec mes parents est agréable."


li "Bien que j'avoue que la piscine et la taille de la maison aident un peu."


"Même s'ils ne vivent pas au Japon, vu la façon dont Lilly parle de sa famille, ils doivent être plutôt à l'aise financièrement pour vivre aussi luxueusement."


li "Tout va bien pour Hanako et toi ?"

stop music fadeout 0.3


"Merde, j'aurais espéré que le sujet n'arrive pas aussi rapidement."


"Je prends un moment pour réfléchir et trouver comment lui décrire la situation sans trop l'inquiéter, mais elle reparle avant que je n'aie le temps de dire un mot."

play music music_moonlight fadein 2.0


li "Hanako ne va pas bien, n'est-ce pas ?"


hi "Comment le sais-tu ?"


li "Parce qu'aujourd'hui c'est son anniversaire. J'aurais espéré qu'elle aille un peu mieux après avoir fait ta connaissance, mais..."


li "Comment est-ce qu'elle va maintenant ?"


hi "Elle a loupé l'école hier et ne semblait pas dans son assiette quand j'ai été la voir. Aujourd'hui elle a aussi loupé l'école et vient de me dire de m'en aller."


hi "Je ne sais vraiment pas quoi faire. C'est déjà arrivé dans le passé ? C'est lié à ses cicatrices d'une façon ou d'une autre ?"


li "Malheureusement oui. Il s'est passé la même chose l'an dernier quand il y a eu son anniversaire."


li "Pour autant que je puisse dire, c'est parce que ses parents sont morts dans l'accident qui a causé ses cicatrices, et Hanako se blâme de leur mort."


"Ce qu'elle dit concorde. Si elle pense que leur mort est de sa faute, elle peut en venir à regretter d'être née tout court."


"Le fait que Lilly ne semble pas au courant de toute l'histoire non plus est une surprise."


hi "C'est donc pour ça qu'elle vit aux dortoirs aussi. Elle t'a dit quelque chose d'autre sur l'accident ?"


li "Aussi proches que l'on ait pu devenir... elle ne m'a presque rien dit de ce qui s'est passé. Ce que je sais est très vague."


"Elle a l'air déprimée, presque abattue. Prenant en compte le traumatisme qu'a dû vivre Hanako, je ne peux pas reprocher à Lilly de ne pas savoir. Néanmoins, elle semble considérer ça comme une défaite personnelle."


hi "Ne te blâme pas, Lilly. Avec tout ce qu'elle a vécu..."


li "Je sais. Merci, Hisao. Je suis désolée de ne pas pouvoir t'aider davantage."


hi "Ne t'embête pas, je vais y réfléchir un peu. Merci, et passe un moment agréable en Écosse."


li "Hum, je..."


hi "Mmh ?"


li "Ce n'est rien. Merci de prendre soin de Hanako."


hi "...D'accord. À plus."


li "Au revoir."

stop music fadeout 4.0


"Et sur ce, la ligne se coupe."

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


"Maintenant, je me pose de nombreuses questions auxquelles je ne peux répondre, la plus récente étant ce qu'allait dire Lilly au téléphone."


"Oh. Oh non."


"Je suis un idiot. Elle devait penser que j'appelais pour parler avec elle, mais je lui ai juste demandé de l'aide pour Hanako."


"Ce qui est encore plus honteux que la pensée elle-même, c'est le fait qu'elle soit en grande partie vraie."


"Bon... une chose après l'autre. Pour l'instant, je dois m'occuper de Hanako et m'assurer qu'elle mange bien."

show bg school_girlsdormhall
with shorttimeskip


"Les quelques étudiants que je croise regardent, sans se cacher, le plateau de nourriture que j'apporte au dortoir des filles."


"Ce n'est pas un plat dont on peut être fier, ce n'est qu'un plat instantané acheté à l'épicerie puis réchauffé au micro-ondes, mais ça devrait au moins la nourrir."

show bg school_girlsdormhall at right
with charamove


"Finalement j'arrive à sa porte, après avoir pu échapper à deux filles qui essayaient, en rigolant, de me dérober le plat que j'ai mis tant de temps à me procurer."


"Je décide de ne pas frapper, sachant que c'est inutile et que de toute façon c'est difficile en ayant les mains prises."


hi "Hanako, c'est Hisao."


hi "Je sais que tu m'écoutes. J'ai à manger pour toi."


"Silence. Comme je m'y attendais."


hi "Je le laisse devant ta porte. Mange un peu, d'accord ?"


"Voilà, j'ai rempli mon rôle. Maintenant ça ne dépend que d'elle."

show bg school_girlsdormhall at center
with charamove


"Posant le plat au sol, je retourne à ma propre chambre pour prendre mon diner."

with shorttimeskip


"Au moment où je retourne au dortoir des filles, une bonne heure est passée."


"Je suis content de voir qu'il n'y a plus le plat que j'avais mis devant sa porte. Je retourne dans ma chambre, quelque peu content de savoir qu'elle mange."


"Sachant qu'elle essaye de traverser cela toute seule, être capable de l'aider, même si c'est seulement un peu, c'est déjà quelque chose."

scene black
with dissolve



label fr_L12:

scene bg school_library_ss
with locationchange

play music music_pearly


"Je suis en train de lire à la bibliothèque après les cours, tournant page après page, enregistrant à peine les mots écrits, par pur ennui."


"La joue posée sur ma main, je remarque que ma joue est quelque peu rugueuse. Il me faudra bientôt un rasoir."


"Abandonnant la lecture, je laisse ma tête tomber sur le livre."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

nvl clear
nvl show dissolve


n "\n\n\nÇa a été beaucoup plus calme à partir du moment où Hanako a recommencé à venir en cours."


n "Depuis qu'elle est revenue en cours, après plusieurs jours d'absence, rien d'inhabituel n'a été fait ou dit. Aucun de nous deux n'avait envie de reparler de cet incident, donc nous n'avons pas ramené cela sur le tapis."


n "Et ainsi plusieurs jours se sont écoulés, la routine continuant comme avant."


n "Il est normal que mon esprit vagabonde comme ça, vers d'autres endroits, et surtout, d'autres gens. Le vide qu'a laissé Lilly dans ma vie quotidienne et dans celle de Hanako est plus que présent."


n "J'aimerais pouvoir dire qu'au moins ça m'a permis de clarifier ce que je ressens pour elle, mais hélas, ce n'est même pas le cas."


n "Et ce qui n'aide pas, c'est que chaque fois que j'essaye d'y voir plus clair, je finis par dévier sur un autre sujet, comme sur Iwanako."

$ renpy.music.set_volume(1.0, 2.0, channel="music")

nvl clear

nvl hide dissolve

window show


hi "Pourquoi est-ce qu'il a fallu que ça arrive à ce moment-là..."


yu "Hum..."

show yuuko worried_up_ss
with charaenter


"Je me redresse et me tourne pour voir la source de la voix timide venant de derrière."


hi "Ah, désolé. Je ne voulais pas déranger."

show yuuko worried_down_ss
with charachange


yu "Ce n'est... pas ça."


hi "Ah..."


"Je jette un coup d'œil dans la bibliothèque éclairée d'une lueur orangée, réalisant que mon excuse a dû sembler bizarre. Le temps que je réfléchisse et lise à moitié, tout le monde a fini par partir."


hi "La bibliothèque ferme ?"

show yuuko neurotic_down_ss
with charachange


yu "Si tu ne veux pas y aller, je peux rester là un peu plus longtemps, ça ne me gêne pas du tout."


hi "Ne t'inquiète pas, je vais partir de toute façon. Merci."

show yuuko worried_down_ss
with charachange


"Alors que je me lève et me prépare à partir, je sens le regard de Yuuko dans mon dos."


hi "Quelque chose ne va pas ?"

show yuuko worried_up_ss
with charachange


yu "Tu as l'air déprimé. Ça va ?"


"Yuuko se tord nerveusement les doigts en disant cela, n'étant pas sûre de savoir si elle dépasse les limites ou non. Je ne sais pas si elle est inquiète à mon propos ou si elle veut m'embêter."


"En temps normal je me contenterais de hausser les épaules en disant que je vais bien, mais mon humeur mélancolique m'en empêche. Bien qu'elle soit du personnel de l'école, elle n'a pas du tout une présence autoritaire comme les autres."


hi "C'est juste que... je dirais que j'ai quelques problèmes relationnels."

show yuuko worried_down_ss
with charachange


yu "Oh. Je... ne suis pas douée avec ce genre de choses. Ma dernière relation s'est finie un peu brusquement."

show yuuko smile_down_ss
with charachange


yu "Mais si tu veux en parler, je peux t'écouter. Je crois."



"Maintenant je me sens mal d'avoir évoqué cela. Elle n'est pas si vieille, donc au moins elle a une bonne chance de retrouver quelqu'un d'autre."


hi "Ce n'est pas qu'on est en froid en ce moment. On a passé beaucoup de temps ensemble en tant qu'amis, sortant parfois pour faire des courses ou autre... ce genre de choses."


hi "Mais je commence à vouloir faire plus avec elle, en savoir plus sur elle et être plus souvent avec elle. Je ne suis pas sûr de savoir si c'est de l'amour ou non, notre relation actuelle est déjà très bien."

show yuuko panic_up_ss
with charachange


yu "Tu ne devrais pas laisser ça t'arrêter !"

show yuuko worried_down_ss
with charachange


yu "Ah... désolée."

show yuuko worried_up_ss
with charachange


yu "Comment dire ça... euh..."

show yuuko neutral_down_ss
with charachange


yu "Je pense que c'est bien d'être amis, mais l'école finira un jour. Tu crois que ça t'ira de ne pas savoir si ça aurait pu aller plus loin ?"


hi "Je crois que c'est le fond du problème. Je n'ai vraiment aucune idée de la réponse à cette question."

show yuuko worried_down_ss
with charachange


yu "Je ne peux pas t'aider pour cela. Ce que tu ressens est quelque chose que tu dois découvrir par toi-même. Mais je crois que si tu l'aimes, tu devrais faire quelque chose."

show yuuko smile_down_ss
with charachange


yu "Après y avoir pensé, j'ai conclu que même si ma dernière relation n'avait pas bien fini, c'est mieux comme ça que de n'avoir jamais su si ça aurait pu marcher ou pas."


"Je n'aurais jamais cru que Yuuko puisse être aussi avisée. Il est logique qu'avec plus d'expérience dans le domaine, elle ait une meilleure idée que moi sur ce qu'il faut faire."


"Même si rien n'a été élucidé, lui parler m'a aidé à me sortir cela de la tête et je n'ai plus aucun doute sur le fait que si j'aime vraiment Lilly, je dois lui avouer."


"Je soupire, quelque peu frustré."


hi "Si seulement lire autant pouvait aider dans des situations comme ça."

show yuuko closedhappy_up_ss
with charachange


"Ça la fait rire, ce qui renforce mon avis qu'elle est vraiment différente du reste du personnel de l'école."

stop music fadeout 9.0

nvl clear

window hide
nvl show dissolve


n "\n\n\n\n\n\nEn fin de compte, tout revient à ce qui se passera quand l'école finira."


n "En prenant en compte ce qui est arrivé avant que j'arrive à Yamaku, j'ai quelque peu l'impression qu'on me demande de suivre le rythme d'une course, bien que j'aie commencé avec plusieurs tours de retard."


n "C'est une motivation de plus pour avancer. La dernière chose dont j'ai besoin maintenant est de me faire trop devancer et de tomber malade en plus de ça."

nvl clear
nvl hide dissolve

scene bg school_dormhisao_ss
with locationskip
window show


"Une fois de plus, je me retrouve à appeler Lilly. Ma facture de téléphone va être démentielle, vu que c'est de l'international."


"Mais ça en vaut la peine. Je ne veux pas juste rattraper le coup de la dernière fois, je veux vraiment lui parler."

scene bg school_dormhisao_blurred_ss
show phone mobile:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with locationchange
with Pause (0.5)


"Quand ça décroche enfin, je reconnais facilement la voix de l'autre côté."


"Mrs Satou" "{image=vfx/garbage.png} {image=vfx/garbage.png} Satou {image=vfx/garbage.png}?"


hi "Hello, Mrs Satou. May I... euh... speak..."


"Merde. J'ai oublié comment formuler le reste de la phrase. Je ne suis pas fier d'oublier alors qu'il y a si peu de mots, même si je n'ai pas passé longtemps à essayer de les mémoriser."


hi "Pourrais-je parler avec Lilly, s'il vous plaît ?"


"Mme Satou" "Bonjour, Hisao. Tu essayes d'apprendre l'anglais ?"


hi "Juste un peu. Je ne suis pas bon en langue en général."


"Mme Satou" "Oh, ne dis pas ça. Ta prononciation était bonne ! Je vais chercher Lilly pour toi, attends un moment."


"Le temps qu'elle aille trouver Lilly, l'autre côté de la ligne est silencieux."


"Finalement, une Lilly bien plus réveillée que la dernière fois répond, vu qu'il est plus de midi cette fois."

play music music_comfort fadein 12.0


li "Hisao, c'est toi ?"


hi "Ouais, c'est moi. Salut."


li "Bonjour. Désolée d'avoir été aussi longue, j'étais dans le jardin."


hi "Tu faisais du jardinage ?"


li "Malheureusement il s'avère que je suis mauvaise en jardinage, donc je me contente de sentir les fleurs. Mes doigts aussi préfèrent ça."


li "J'en déduis que Hanako va mieux ?"


hi "Oui, un peu. Je me suis assuré qu'elle mangeait et elle a fini par se ressaisir. Merci pour l'aide l'autre jour, au fait."


li "Je ne crois pas que j'ai vraiment aidé. Le principal est qu'elle aille mieux."


hi "Oui. Comment est la vie là-bas, alors ? On dirait que tu vis dans un manoir ou quelque chose dans le genre."


li "Je n'appellerais pas ça un manoir..."


"Elle allait ajouter “mais il est vrai que c'est grand”, mais la modestie l'a arrêtée. Je suis un peu envieux, mais ce sont ses vacances."


li "Mais c'est une belle maison où il fait bon vivre. Il y a une plage pas loin, dont Akira est particulièrement fan."


hi "C'est une nageuse ?"


li "Elle m'emmenait toujours avec elle pour faire des courses de natation. Qu'elle gagne. À chaque fois."


"Lilly ne semble pas être très sportive, le fait qu'elle ne soit pas fan de natation est donc logique."


"Je ne l'ai jamais vue aller plus vite que durant ses marches depuis la ville jusqu'à l'école. Avec ça, il est difficile de l'imaginer nager."


hi "Les plages là-bas doivent être belles à voir. Elles sont sûrement moins peuplées que celles qu'on a ici après tout."


li "Oui, Akira dit que c'est très beau ici, parce que c'est loin de la ville."


"Je ne réalise que maintenant ce que je viens de dire, mais ça n'a pas l'air de la gêner. C'est toujours facile d'oublier qu'elle ne peut pas voir quand elle n'est pas là, même si nous sommes amis."


li "Cela dit, l'accent local rend parfois la communication un peu difficile. Ça me rappelle constamment que je ne suis pas à la maison."


"Le fait qu'elle ne considère pas la maison de ses parents comme étant la sienne est logique mais ça me fait réaliser que je ne suis pas sûr de savoir si c'est la même chose pour moi."


"La fin de l'année scolaire est trop lointaine pour que je puisse l'anticiper et j'ai passé tellement de temps dans cette petite pièce... J'en suis venu à accepter le dortoir comme ma maison assez rapidement."


hi "J'imagine que ça doit être difficile à suivre. Tu t'en sors avec ton niveau d'anglais, non ?"


li "Heureusement. J'ai beau le parler couramment, être dans une situation où je dois l'utiliser souvent aide à effacer mon accent japonais, donc c'est un bon entraînement."


li "J'ai entendu que tu essayais d'apprendre l'anglais ?"


hi "Plutôt mémoriser quelques lignes et sans y arriver en plus de cela. Je ne suis vraiment pas fait pour apprendre une autre langue."


"Ma remarque la fait rire."


li "Je pense qu'il y a des gens qui choisissent leur voie mais pour d'autres, cette voie est innée."


li "Tu peux te rassurer en te disant que tu es toujours meilleur que moi en sciences et en maths, au moins."


hi "Tout ce que ça m'a permis de faire, c'est de devenir l'étudiant préféré de Mutou..."


li "Je ne m'inquièterais pas pour ça, si j'étais toi. Il y a des compétences utiles dans tous les travails, n'est-ce pas ?"


hi "C'est ce qu'il m'a dit. Son visage s'est littéralement illuminé quand j'ai dit que je ferais probablement carrière dans ce domaine."


"Nous partageons un rire chaleureux face aux évènements qui nous ont séparés, chacun d'un côté du monde. C'est bien, cela me rappelle nos discussions qui me manquaient depuis que Lilly est partie."


"Alors que nous attendons tous les deux que l'autre dise quelque chose, je décide de lui dire ce que je pense. Je peux sentir ma gorge se serrer un peu."


hi "Tu nous... hum, tu me... manques."


"Le silence de l'autre côté de la ligne me dit qu'elle a pris en compte le vrai poids de ces mots, mais au fil des secondes, je ne peux pas m'empêcher de me sentir de plus en plus inquiet."


"Heureusement le silence s'arrête, presque aussi rapidement qu'il a commencé."


li "Tu me manques aussi Hisao."


li "Au revoir."


hi "Au revoir, Lilly."

stop music fadeout 6.0


"Encore une fois, elle raccroche, simplement et sans un autre mot."

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


"Cette douce, presque timide voix. Ce ton doux et chaleureux... Je me mentirais si je disais que je ne reconnais pas ce sentiment pour ce qu'il est."


"En pensant à Lilly, je commence à anticiper son retour. Ce fut une bonne journée."

scene black
with dissolve



label fr_L13:

scene bg school_scienceroom
with locationchange


"Je suis en classe à écouter une autre des longues lectures de Mutou, mon esprit vagabondant loin du cours noté sur le tableau."

play music music_tranquil fadein 4.0

nvl clear

window hide
nvl show dissolve


n "\n\nDepuis que j'ai appelé Lilly, je pense à deux choses. Deux choses qui m'amènent à la même conclusion : j'ai commencé à me détacher de ma vie passée."


n "Ça fait seulement un mois et demi que je suis arrivé ici et pourtant l'école est devenue comme une seconde maison. J'ai gagné de nouveaux amis, réussi à m'adapter au style de vie et à la culture de l'école et je me suis habitué aux étrangetés de mes camarades de classe."


n "Cela m'étonne que je me sois habitué à une école où les personnes handicapées sont la norme, au lieu d'être une rare exception. La même école qui est peuplée de brûlés, amputés, aveugles, sourds, et tout autre handicap."


n "Si quelqu'un m'avait décrit cette école avant que je n'y vienne, j'aurais dit qu'il avait trop d'imagination. Pour tout dire, la première fois que je suis venu ici, je me suis senti comme un indigène découvrant un nouveau territoire."


n "C'est incroyable à quelle vitesse quelqu'un peut s'habituer à l'environnement dans lequel il est forcé de vivre. Et maintenant j'ai même trouvé quelqu'un qui m'intéresse beaucoup. Quelle vie étrange."

nvl clear
nvl hide dissolve
window show


"Avant que je ne puisse divaguer plus loin, je vois une petite feuille de papier glisser sur mon bureau. Cette écriture rose et criarde est sans aucun doute celle de Misha."

window hide

show misha hips_grin_close at offscreenleft
with None

show misha hips_grin_close:
    xpos 0.1 xanchor 0.5
show bg school_scienceroom at left
with charamove



$ written_note(u"N'aie pas l'air si ennuyé, Hicchan ! L'école est bientôt finie ! Un week-end de trois jours !", text_args={"color":"#FF2AAA"})

window show


"Oh, c'est vrai, on a samedi et lundi aussi. Je ne vais pas m'en plaindre."


"Je décapuchonne mon stylo et lui réponds avant de lui rendre discrètement la feuille, regardant devant moi de temps en temps. Mutou continue d'enchaîner les équations et formules étranges au tableau."

window hide


$ written_note(u"J'imagine que tu as quelque chose de prévu ?")

show misha perky_smile_close
with charachange

window show


"Misha reprend le papier et réagit de manière comique en lisant son contenu. Même pour elle. Avec sa langue sortant au coin de la bouche. Est-ce qu'elle a mal compris mon expression et croit que je suis déprimé et essaye de me remonter le moral ?"

window hide

show misha sign_smile_close
with charachange


$ written_note(u"Travailler au conseil des étudiants avec Shicchan, bien sûr.", text_args={"color":"#FF2AAA"})


$ written_note(u"Tu ne t'arrêtes jamais avec ça, hein ?")

show misha hips_frown_close
with charachange


$ written_note(u"Mais Hicchan aurait pu nous aider, pauvres petites filles.", text_args={"color":"#FF2AAA"})


$ written_note(u"Je vous aiderais bien aujourd'hui si je n'avais pas quelque chose d'autre à faire.")

show misha hips_grin_close
with charachange


$ written_note(u"Ooh, Hicchan, coquin coquin !", text_args={"color":"#FF2AAA"})


$ written_note(u"Je vais juste retrouver Lilly avec Hanako. Je ne sais pas à quoi tu pensais.")

show misha perky_smile_close
with charachange


$ written_note(u"Donc Lilly est de retour ?", text_args={"color":"#FF2AAA"})



$ written_note(u"Ouais, son avion atterrit ce soir, donc elle reviendra à l'école la semaine prochaine.")

show misha hips_grin_close
with charachange

window show


"Alors qu'elle récupère le papier et commence à répondre, je lève la tête et ce que je vois me déplaît."

stop music fadeout 2.0

show muto irritated behind misha at Alphain(1.0), Slide(0.8, 0.5, 0.6, 0.5, 1.0)
with Pause(0.5)


"Alors que j'essaye d'attirer silencieusement l'attention de Misha, Mutou arrive, passant une table après l'autre, son regard fixé sur elle."

show misha perky_confused_close
with charachange


"Elle s'arrête soudainement d'écrire alors qu'une grande ombre couvre son bureau."

show misha sign_confused_close
with charachange


mi "Ah... je..."


"Il prend silencieusement la feuille de papier de ses mains et commence à lire."


"Transpirant de crainte, je regarde rapidement le reste de classe, remarquant leur silence complet. Bien sûr, je devais être celui qui attirait l'attention durant le cours."

play sound sfx_impact
show misha perky_sad_close
with vpunch


"Après avoir parcouru la feuille plusieurs secondes, il roule la feuille en un petit tube et tapote la tête de Misha avec."

show muto normal
with charachange


mu "Encore une demi-heure jusqu'à ce que tu puisses aller au Conseil des Étudiants. Je crois que tu peux tenir jusque-là."

play music music_ease


"Misha rougit de honte alors que la classe entière explose de rire. Il a beau être quelque peu bizarre, il sait très bien comment gérer Misha."


"Je me sentirais probablement désolé pour elle si je n'étais pas trop occupé à rire."

scene bg hosp_ext at right
show hanako basic_distant_cas at center
with shorttimeskip

play ambient sfx_rooftop fadein 2.0


ha "Hisao, c'est celui-là ?"


hi "Non, je crois que c'est une ligne étrangère."


"Et donc, un troisième avion atterrit, duquel elles ne sortent pas."


"Depuis une demi-heure nous passons le temps en parlant de tout et de rien. Le vol de Lilly et d'Akira a été retardé et à ce rythme il fera nuit avant que leur avion arrive."

show hanako def_worry_cas at twoleft
with shorttimeskip


ha "C'est celui-là ?"


hi "Non, c'est pas le logo de la compagnie."

show hanako basic_distant_cas
with charachange

show hanako basic_normal_cas
with charachange


"Les yeux de Hanako regardent partout, suivant les groupes de gens entrant et sortant par les grandes portes vitrées en face de nous. Heureusement, personne ne fait attention à elle, les gens étant apparemment occupés par d'autres choses."

show hanako emb_timid_cas at tworight
with shorttimeskip


ha "C'est peut-être celui-là ?"


hi "Non, je crois que c'est... attends, je crois que c'est peut-être celui-là en fin de compte."
show hanako cover_distant_cas at center
with shorttimeskip


"Il faut un moment avant que l'affichage change le statut de leur vol en “débarquement”."


"Un grand bâillement monte et je n'ai pas le temps de le retenir. Mon rythme de sommeil a été, encore une fois, complètement chamboulé. C'est probablement dû à mes inquiétudes pour Hanako et aux effets secondaires de mes médicaments."

show hanako emb_smile_cas
with charachange


ha "Hisao, là-bas..."


"Je regarde Hanako, puis suis son regard vers les portes."


aki "Mmh ? Oh, Lilly, ils sont là !"


li "Vraiment ?"

show akira basic_smile:
    xanchor 0.5 xpos -0.3
show lilly basic_cheerful at offscreenleft
with None

show akira basic_smile at left
show lilly basic_cheerful_cas:
    xanchor 0.5 xpos 0.4
show hanako emb_smile_cas at tworight
show bg hosp_ext at center
with charamove


"Nous nous appelons pour nous repérer, nous mettant rapidement sur le côté pour ne pas gêner le passage des autres."


ha "Lilly !"

show hanako emb_downsmile_cas at center
with dissolvecharamove


"Hanako s'avance pour serrer Lilly dans ses bras, un grand sourire sur son visage montrant son bonheur de retrouver Lilly. Lilly sourit simplement en retour, puis parle doucement."

show lilly basic_smileclosed_cas
with charachange


li "Je suis contente que tu sois là, Hanako."

show akira basic_smile at twoleft
show lilly basic_smileclosed_cas:
    xpos 0.6
show hanako emb_downsmile_cas at tworight
show bg hosp_ext:
    xpos 0.55
with charamove


"Pendant qu'elles s'étreignent, ce dont Hanako avait grand besoin après tout ce qui est arrivé pendant l'absence de Lilly, je me tourne vers Akira."

show akira basic_ending
with charachange

aki "Yo."


hi "Vous avez beaucoup de retard."

show akira basic_annoyed
with charachange


aki "Ouais, il y avait une grosse tempête à l'aéroport. On a été trempées rien qu'en marchant de la voiture jusqu'à la porte de l'aéroport."


hi "Tu apprécieras plus le temps ici alors. Bon retour à toi aussi, Lilly."

stop music fadeout 4.0

show hanako basic_smile_cas:
    xpos 0.8
show akira basic_smile
show lilly basic_weaksmile_cas
with dissolvecharamove


"Hanako se décolle de Lilly pendant que je lui parle. Pendant un long moment, aucun de nous deux ne dit quoi que ce soit."


"Contrairement à ce que je croyais, l'atmosphère est étrange, presque étouffante. Nous essayons tous les deux de deviner les sentiments de l'autre, incertains de ce qui devrait être dit."


"Merde. C'est exactement ce que je craignais quand j'envisageais de faire avancer les choses entre nous. Lilly se passe la main dans les cheveux et tourne son doigt autour d'une de ses boucles, essayant de deviner comment il faudrait réagir."


"Et enfin, heureusement, Lilly lâche un petit soupir et rompt le silence."

show lilly basic_smile_cas
with charachange

play music music_lilly fadein 6.0


li "Merci, Hisao. Je suis contente d'être rentrée."

show hanako basic_worry_cas
with charachange


ha "Ça va ? Tu as l'air fatiguée..."


"Apparemment, ne réussissant pas à se ressaisir tout de suite, elle fait signe que non à Hanako, pour éviter qu'elle ne s'inquiète."

show lilly basic_weaksmile_cas
with charachange


li "Je vais bien, vraiment. Juste le décalage horaire."

show akira basic_laugh
with charachange


aki "Faible."


hi "Tu n'en souffres pas ?"

show akira basic_ending
with charachange


"Elle se contente de sourire, gonflant sa modeste poitrine."


aki "Je me sens très bien !"

show lilly basic_sleepy_cas
with charachange


li "C'est pas juste..."

show akira basic_smile
show hanako basic_normal_cas
with charachange


aki "Haha, bah. Ça te passera vite."

show lilly basic_smile_cas
with charachange


li "Ah ! Au fait, Hisao ?"


hi "Ouais ?"

show lilly basic_smileclosed_cas
with charachange


li "On n'a pas des vacances bientôt ?"


hi "J'aurais oublié si Misha ne me l'avait pas rappelé ce matin. On a un week-end de trois jours à partir de demain."

show akira basic_laugh
with charachange


"Akira donne des légers coups de coude à Lilly, souriant."

show akira basic_smile
with charachange


aki "J'te l'avais dit que tu ne les manquerais pas."


hi "Tu as quelque chose de prévu ?"

show lilly basic_smile_cas
with charachange


li "Si Hanako et toi n'êtes pas occupés..."


hi "Je n'ai rien de prévu, donc je suis ouvert à toute proposition. Hanako ?"

show hanako basic_smile_cas
with charachange


ha "Non, rien."

show lilly basic_cheerful_cas
with charachange


li "Tant mieux. Je pensais qu'on pourrait aller à la maison de vacances de ma famille pour se reposer pendant ce long week-end. On l'a rarement utilisée récemment, donc on devra sûrement dépoussiérer les choses un peu."


hi "Oh ? Où est-ce qu'elle est ?"

show akira basic_ending
with charachange


aki "Au nord, à Hokkaido. La zone est pratiquement déserte, donc ça sera bien pour que vous vous reposiez."


hi "Tu ne viens pas ?"

show akira basic_smile
with charachange


aki "Nan. Je prends mes vacances de mon côté avec mon petit copain."


"Je la regarde avec attention, suspicieux sur ses intentions."


hi "On dirait qu'on va devoir nettoyer la maison pour toi."

show lilly basic_displeased_cas
with charachange


li "C'est... bien possible..."


"Akira se contente de regarder ailleurs, nous évitant. On dirait qu'on avait raison."

show akira basic_boo
with charachange


aki "C'est juste un bonus. Vraiment. Mon homme et moi l'avons laissée en bon état la dernière fois, je le promets."

show akira basic_smile
with charachange


aki "Maintenant, je m'en vais."

show lilly basic_reminisce_cas
with charachange


li "Déjà ? Akira..."


"Elle se retourne rapidement et s'en va, la main en l'air en guise d'au revoir."

show akira basic_laugh
with charachange


aki "On se voit dans quelques jours, les gars."

show akira basic_laugh at Alphaout(1.0), offscreenleft
with charamove

hide akira
with None

show lilly basic_reminisce_cas:
    xpos 0.4
show hanako basic_smile_cas:
    xpos 0.6
show bg hosp_ext at bgleft
with charamove


"Lilly et moi nous contentons de soupirer à sa retraite hâtive."

show hanako cover_bashful_cas
with charachange


ha "Ça semble être un endroit agréable."

show lilly basic_smileclosed_cas
with charachange


"Lilly hoche la tête avec enthousiasme, soulevant son sac d'une main et plaçant l'autre sur l'épaule de Hanako pour se guider alors que nous faisons notre chemin jusqu'à la zone des taxis."


"Après les évènements des derniers jours, passer un week-end à la campagne avec Hanako et elle sonne comme un rêve."


"Plus j'y pense et plus j'en suis sûr. Ça sera le bon moment pour lui avouer mes sentiments."

stop music fadeout 2.0
stop ambient fadeout 2.0

scene black
with dissolve



label fr_L14:

scene bg city_station
with locationchange

play music music_daily fadein 7.0


"La froideur du matin enveloppe mon corps frissonnant. Je souffle dans mes mains pour essayer désespérément de chasser le froid alors que nous attendons sur le quai de la gare."


"Lilly est assez peu habillée par rapport à la température qu'il fait. Je ne peux qu'espérer que cela indique qu'il ne fera pas si froid là-bas ..."

show lilly basic_sleepy_cas at twoleft
show hanako basic_distant_cas at tworight
with charaenter


hi "Rah Lilly, pourquoi est-ce qu'on avait besoin d'y aller aussi tôt ?"

show lilly basic_displeased_cas
with charachange


li "Malheureusement, les trains sont contre nous. Le prochain train pour Hokkaido est à quatorze heures."


hi "Génial. Juste génial."


"Je m'arrête un moment pour me frotter les yeux, encore endormi, et Lilly en profite pour me rassurer."

show lilly basic_weaksmile_cas
with charachange


li "Ne t'inquiète pas Hisao. Quand on y sera, il fera plus chaud."


hi "Pourquoi ne pas prendre l'express ? Un train normal va prendre des heures pour y aller, donc autant prendre la ligne Shinkansen vers le nord et changer de ligne à la fin."

show lilly basic_smile_cas
with charachange


li "Les vieux trains ont un certain charme, tu ne penses pas ?"


hi "Je serais d'accord si je n'étais pas en train de me les geler aussi tôt le matin pour en attendre un."

show hanako emb_timid_cas
with charachange


ha "Je suis... désolée, Hisao."


hi "Désolée ? Pourquoi ?"

show hanako emb_downtimid_cas
with charachange


ha "J'ai été... celle qui a suggéré qu'on prenne un train normal."


"Maintenant je me sens coupable. J'en suis réduis à soupirer et me couvrir le visage de la main."


hi "T'inquiète pas, je rouspète juste un peu."

show lilly basic_ara_cas
with charachange


li "Eh bien, eh bien, Hanako, tu ne devrais pas te blâmer pour ça. Même sans ta suggestion, j'aurais quand même opté pour ça."

show hanako emb_smile_cas
with charachange

hide hanako
hide lilly
with charaexit


"Heureusement, Lilly rattrape vite le coup. J'en profite pour regarder autour de moi."


"À part nous, le quai est complètement désert, les sièges n'étant occupés que par la rosée matinale. J'imagine que personne d'autre n'est masochiste au point d'être là à attendre aussi tôt le matin."


"Et si quelqu'un était là, il remarquerait les gros sacs qu'ont amenés Lilly et Hanako."


hi "Mais qu'est-ce que vous avez là-dedans, d'ailleurs ?"

show lilly basic_listen_cas at center
with charaenter


li "Les sacs ? Mmh..."


"Elle s'arrête un moment et penche la tête en réfléchissant."

show lilly basic_smileclosed_cas
with charachange


li "Une veste de rechange, une jupe, un imperméable, des sous-vêtements, un pyjama, quelques livres... et je crois que c'est tout."


hi "Tu dis ça comme si j'étais mal préparé."

show lilly basic_surprised_cas
with charachange


li "Tu as pris quoi toi ?"


hi "Des sous-vêtements et un paquet de cartes. C'est tout."


"Et mes pilules, mais pas besoin de le préciser ça."


li "Pas de pyjama ?"


hi "Zut, je savais que j'oubliais quelque chose."


"Je me frotte les cheveux de frustration, et Lilly soupire."

show lilly basic_weaksmile_cas
with charachange


li "Il y aura des vêtements que tu pourras utiliser là-bas. Akira y va des fois après tout. Et je crois qu'il y a des vêtements de mes parents dans un placard aussi."

show lilly basic_smile_cas
with charachange


li "Je ne pense pas qu'il y ait un problème à ce que tu empruntes un pyjama, si besoin."


hi "Merci. Cependant, ça ne me gêne pas de dormir comme ça."

show lilly basic_surprised_cas
with charachange


li "Pendant deux jours ?"


hi "Pas faux."


"Pas vraiment. Bien que deux jours soient limites, ce qui n'est pas acceptable c'est de passer pour un plouc en présence de deux filles."

hide lilly
with charaexit


"Alors que nous discutons sur le quai, une annonce de la gare prévient bruyamment de l'arrivée de notre train."


"Je regarde derrière Lilly et Hanako, le train n'est pas encore à portée de vue. Regardant ma montre, je vérifie que c'est celui que nous prendrons."


hi "On prend le cinq heures et demie, non ?"

show lilly basic_smileclosed_cas at twoleft
show hanako basic_distant_cas at tworight
with charaenter


li "Oui."


hi "L'une d'entre vous veut que je prenne son sac ? Le mien n'est pas lourd."

show lilly basic_ara_cas
with charachange


li "Eh bien, eh bien. C'est galant de ta part, Hisao."


hi "N'accepte pas à contrecœur, hein."


"Alors que je me penche pour attraper le grand sac de Lilly, je vois Hanako soulever le sien."


hi "Tu t'en sortiras ?"

show hanako basic_normal_cas
with charachange


"Elle me répond avec un hochement de tête. Je commence à croire qu'à la fin du week-end, je pourrai compter sur mes doigts les fois où elle a parlé."


stop music fadeout 5.0
play ambient sfx_trainint fadein 5.0

$ ksgallery_unlock("ev lilly_trainride")
scene train_scenery
show train_scenery_fg
show evfg lilly_trainride at train_shake
with shorttimeskip


"Avec l'horizon matinal par la fenêtre et les bruits occasionnels du train, j'essaye de me concentrer sur les cartes dans mes mains."


hi "Je relance de cinq."


ha "Euh... je..."


"Elle balbutie un peu et se penche vers Lilly d'un air conspiratoire et elles échangent quelques messes basses. Vu le nombre de fois où c'est arrivé, je commence à douter que Hanako sache comment jouer au poker."


"Ça ne semble pas gêner la lecture de Lilly, ses mains glissant sur les lignes, mis à part quand le train secoue un peu."


"Mes pions d'échecs que nous utilisons comme jetons de mise continuent de s'accumuler de mon côté, alors ça ne me gêne pas."


"Regardant autour de nous, je constate que notre wagon est presque aussi vide que le quai sur lequel nous attendions le train. Il y a juste quelques personnes, pour la plupart des touristes ou des couples en vacances."


"Pendant qu'elles continuent leur stratégie clandestine, un petit garçon passe la tête au-dessus de son siège et me regarde. Espérant qu'il ne regarde pas en direction de Hanako, je lui fais un signe et souris."


"Heureusement, il se rassoit après avoir estimé que j'étais trop ennuyeux pour gaspiller son temps."


ha "Je suis et je relance de... cinq."


hi "Zut tu m'as eu. Je me couche."


"Elle a bluffé et je me suis fait avoir. Baissant la tête, je lui donne une grande partie de mes pions."

$ ksgallery_unlock("ev lilly_trainride_smiles")
show evfg lilly_trainride_smiles at train_shake
with charachange


"Hanako a l'air absolument ravie. Et même si Lilly est toujours concentrée sur sa lecture, je peux voir un petit sourire sur son visage. Elles sont toutes les deux très contentes."


"Pendant un moment j'essaye de deviner ce que Lilly lit, mais la couverture est trop effacée. En plus ce sont des lettres romanes. Dommage que je ne puisse pas lire le braille au-dessus du texte."


hi "Qu'est-ce que tu lis, Lilly ? Le titre semble être en anglais."


li "Oui. Ça s'appelle “And Then There Were None”, une vieille histoire anglaise. Je pourrai vous la lire, si vous voulez."


"Elle dit ça avec un petit sourire, un peu pour se moquer."


hi "Je crois que ça ira, merci."

stop ambient fadeout 2.0

scene bg hok_houseext at Fullpan(10.0, dir="left")
with shorttimeskip

play music music_tranquil fadein 3.0
play ambient sfx_parkambience fadein 4.0


"Après ce qui semble avoir été un voyage sans fin, nous arrivons enfin sur la terre promise, où se trouve la maison de vacances des Satou. Même après le voyage en train, la marche semble durer une éternité."


"Malgré tout ça, je n'aurais jamais imaginé la vue qui nous attendait après avoir parcouru cette longue route déserte."


"Ça ressemble plus à une ferme qu'à une maison, petite et entourée par des arbres et des buissons."


"Une grande étendue de champs de blés et de terrains fermiers peuvent être vus alors que nous marchons, les clôtures étant de vieilles barrières en bois."


"Ça me rappelle la maison, mais le fait d'être aussi loin des grandes villes fait que la vue est vraiment différente de l'environnement dans lequel j'ai grandi."


"La seule chose qui ne me surprend pas est le style occidental."

show bg hok_houseext at left
with None


hi "Woaw, c'est beau ici..."

show lilly basic_smileclosed_cas at twoleft
show hanako basic_bashful_cas at tworight
with charaenter


ha "Oui, c'est magnifique."

show lilly basic_smile_cas
with charachange


li "Tant mieux. Même si Akira avait dit que la maison était dans un état correct, j'étais inquiète qu'on ait pu avoir des critères différents pour “correct”."


hi "On dirait qu'il n'y a pas âme qui vive dans les environs. Je pensais qu'Akira serait du genre à préférer la ville."

show lilly basic_listen_cas
with charachange


"Lilly fronce les sourcils, réfléchissant, semblant essayer de se rappeler un souvenir lointain."

show lilly basic_weaksmile_cas
with charachange


li "Mmh, de mémoire il y a une petite ville pas trop loin. Mis à part celle-ci, c'est surtout un territoire fermier."

show lilly basic_smile_cas
with charachange


li "Akira et moi avons vécu pendant un moment dans la maison de nos parents qui était proche d'une ville, mais on a fini par décider de déménager dans une maison plus petite, plus facile à gérer."


hi "Trouver un endroit comme ça au Japon de nos jours... c'est plutôt anachronique."

show lilly basic_smileclosed_cas
with charachange


li "Eh bien, cette ville a un certain passé culturel après tout."


"Je regarde une dernière fois de l'autre bout de la route avant de me remettre à bouger."


hi "On rentre, alors ? Je suis claqué."

show hanako basic_normal_cas
with charachange


ha "C'était une longue marche pour arriver jusqu'ici."

show lilly basic_smile_cas
with charachange


"Lilly hoche la tête, enthousiaste, et nous rentrons dans la maison, nos bagages en main."

stop ambient fadeout 1.0
$ renpy.music.set_volume(0.7, 1.0, channel="music")

scene bg hok_lounge
with locationchange


"Une fois le pied à l'intérieur, Hanako et moi regardons autour de nous attentivement l'endroit dans lequel on va rester les prochains jours."


"Tous les détails montrent une vie en suspens, comme le programme télé sur la table basse ou les casseroles toujours posées sur la cuisinière."


"C'est un sentiment étrange. Comme si nous mettions le pied dans la vie d'Akira pendant un bref moment, avant de repartir dans quelques jours comme nous sommes venus. La réalité, bien moins romantique, est qu'elle n'a pas bien rangé la maison."


hi "Où est-ce qu'on pose nos sacs ?"

show lilly basic_smileclosed_cas at twoleft
show hanako basic_normal_cas at tworight
with charaenter


li "Je vais montrer notre chambre à Hanako. Tu peux poser le tien ici, si tu veux."


hi "Tu veux dire que je ne dors pas dans la même chambre que vous ?"

show hanako emb_blushing_cas
show lilly basic_emb_cas
with charachange


"Hanako rougit beaucoup et Lilly met sa main sur sa joue."

show lilly basic_ara_cas
show hanako emb_emb_cas
with charachange


li "Eh bien, quelle audace."


"Mais..."


hi "Attends, si je laisse mes sacs ici, où est-ce que je vais dormir ?"

show lilly basic_weaksmile_cas
with charachange


li "Vu que nous n'avons pas de chambre d'amis..."


hi "Le futon convertible, hein ?"

show lilly basic_concerned_cas
with charachange


li "Désolée Hisao."


"Je soupire, me lamentant d'être en bas de l'échelle du choix de couchage."


hi "J'imagine qu'il n'y a pas d'autre choix."

hide lilly
hide hanako
with charaexit


"Lilly part avec Hanako pour lui montrer sa chambre, donc je fais un petit tour du propriétaire par moi-même après avoir posé mon sac."

scene bg hok_kitchen
with locationchange


"La cuisine, tout comme le salon, est modeste. La nature rustique du bois des meubles me rappelle à quel point on est loin de la civilisation."

scene bg hok_lounge
with locationchange


"Retournant au salon, je décide de regarder la télévision quelques minutes, le temps qu'elles reviennent. Avec une pression sur la télécommande, la télé prend vie, apparemment réglée sur une chaîne d'information."


"M'effondrant presque de fatigue sur le canapé au lieu de m'asseoir, je m'avachis et regarde."

stop music fadeout 5.0
$ renpy.music.set_volume(1.0, 8.0, channel="music")


"Et regarde."


"Et regarde..."

window hide

scene black
with shuteye

with Pause(4.0)

window show


ha "Hisao..."

play ambient sfx_cicadas fadein 5.0

scene bg hok_lounge_ni
show lilly basic_smileclosed_cas at twoleft
show hanako basic_normal_cas at tworight
with openeye


"Je cligne rapidement des yeux pour me réveiller, Lilly et Hanako étant revenues sans leurs sacs."


"D'après le ciel étoilé d'Hokkaido visible par la fenêtre, on dirait que je me suis endormi. Regardant l'horloge sur le mur, je vois qu'il est déjà dix heures."

show lilly basic_weaksmile_cas
with charachange


li "Je vois que tu as trouvé la télévision."


hi "Ouais. C'est vraiment calme et chaleureux, ici."

show lilly basic_smile_cas
with charachange


li "Je suis contente que tu apprécies."

show lilly basic_giggle_cas
with charachange


li "Tu étais déjà endormi quand nous sommes revenues après avoir déballé nos affaires, donc on n'a pas voulu te réveiller."


"À en juger par son rire, je dois être bizarre quand je dors. Je ne veux pas savoir."

show hanako emb_smile_cas
with charachange


ha "Il y a à manger qui t'attend sur le comptoir de la cuisine..."

show hanako emb_downtimid_cas
with charachange


"Hanako bâille, se rappelant à la dernière seconde de se couvrir la bouche."

show lilly basic_weaksmile_cas
with charachange


li "Eh bien eh bien, tu es fatiguée ?"

show hanako emb_timid_cas
with charachange


ha "Ah, oui. Je n'ai pas beaucoup dormi cette nuit."


hi "Je suis plutôt fatigué aussi. La marche pour venir était longue et il est plutôt tard."

show lilly basic_smileclosed_cas
with charachange


li "Dans ce cas, je pense que l'on va se retirer pour la nuit. Bonne nuit, Hisao."

show hanako basic_smile_cas
with charachange


ha "Bonne nuit."


hi "'Nuit."

hide hanako
hide lilly
with charaexit


"Sur ce, elles retournent en silence dans leur chambre."


"Me frottant les yeux, je soupire. Je me demande si je vais réussir à me rendormir après tout ça."


"Je vais manger quelque chose et regarder un peu la télé avant de me coucher."

stop ambient fadeout 2.0

scene black
with dissolve



label fr_L15:

scene black
with dissolve

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_parkambience fadein 6.0


ha "Il dort toujours ?"


li "Je crois."


"Non. Par contre, je suis vraiment très fatigué."


ha "Il commence à être tard déjà..."


"Je le sais ça."


li "Il est resté réveillé longtemps à regarder la télévision. Je pouvais l'entendre depuis la chambre."


"Seulement parce que je ne pouvais pas dormir."


ha "On le réveille ?"


"Ne fais pas ça, Hanako. S'il te plaît."


li "Non, on devrait le laisser comme ça. Je doute qu'il veuille être réveillé tôt s'il n'a pas beaucoup dormi durant la nuit."


"Merci, Lilly."


li "En plus, il a l'air de bien dormir. Ça serait dommage de le réveiller quand il est comme ça."


"Ne montre aucun signe de ton réveil, Hisao. Ça fait plaisir qu'elle soit aussi attentionnée envers moi, cela dit."


ha "Euh..."


li "Hanako, tu peux aller chercher dans le réfrigérateur ce dont on a besoin pour faire le déjeuner ?"


ha "D'accord. Juste les légumes et le riz ?"


li "Mmh, ça devrait suffire. Quelque chose de simple suffit, on pourra manger en ville plus tard."


"Je peux entendre les pas de Hanako sur la moquette, se dirigeant vers la cuisine. À ce moment, Lilly pose doucement sa main sur ma poitrine."


"Il me faut un effort titanesque pour ne pas réagir, mais quelque chose me dit qu'elle sait que je suis réveillé."


"Un long silence passe."


"La seule pensée dans ma tête est celle de la main de Lilly posée sur ma poitrine. Après un long moment, Lilly retire lentement sa main."


li "Bonjour, Hisao."

$ renpy.music.set_volume(1.0, 3.0, channel="ambient")
play music music_dreamy fadein 8.0

scene bg hok_lounge
show lilly basic_smileclosed_cas at center
with openeye


"M'avouant vaincu, je me redresse et me frotte les yeux."


hi "Comment tu savais ?"

show lilly basic_weaksmile_cas
with charachange


li "À ta respiration."


"Bien que ce soit logique, elle n'avait pas besoin d'autant de temps pour s'en rendre compte. Connaissant son ouïe, elle devait le savoir avant même de poser la main sur moi."

show lilly basic_displeased_cas
with charachange


li "Si tu veux dormir un peu plus, tu devrais aller te coucher plus tôt. J'ai entendu la télévision jusque tard dans la nuit."


hi "Désolé pour ça. Mes médicaments interfèrent avec mon sommeil depuis un moment déjà. Même quand je suis fatigué j'ai du mal à dormir."

show lilly basic_oops_cas
with charachange


li "Je suis... désolée d'avoir abordé ce sujet, Hisao."

label fr_choiceL15:
menu:
    with menueffect
    "Je soupire. C'est exactement le genre de choses que je voudrais que les gens ne fassent pas."
    "En parler.":




        return m1
    "Changer de sujet.":


        return m2


label fr_L15a:


hi "Ne t'embête pas, tu t'inquiètes plus pour moi que je ne le fais moi-même. Ça veut juste dire que je dois dormir un peu plus longtemps, c'est tout."

show lilly basic_reminisce_cas
with charachange



li "Mais..."


hi "Je dirais bien que je me sens tout à fait en forme, mais je suppose que ça ne te suffit pas."

show lilly basic_displeased_cas
with charachange


"Elle soupire de consternation avant de se mettre à rire, amusée par ma remarque, abandonnant le sujet initial."

show lilly basic_weaksmile_cas
with charachange


li "Si tu le dis. Prends soin de toi s'il te plaît, Hisao."


hi "Allez, Hanako a besoin d'aide."

hide lilly
with dissolve


"Elle allait protester, mais finit par se diriger vers la cuisine, en passant sa main le long des murs."

label fr_L15b:


hi "Hanako... pourrait avoir besoin d'aide."

show lilly basic_displeased_cas
with charachange

hide lilly
with dissolve


"Lilly semble être sur le point de protester, mais finit par acquiescer et part en direction de la cuisine."

label fr_L15c:


"Je reste assis un moment, regardant la télévision en attendant d'être mieux réveillé, mais c'est inutile. N'ayant rien d'autre à faire, je me lève donc et rejoins Lilly."

stop ambient fadeout 5.0

scene bg hok_kitchen
with locationchange


"Du coin, je vois Hanako et Lilly, de dos, coupant silencieusement la nourriture sur le bar couleur granit."


"Je regarde un moment Lilly guider le couteau avec ses doigts sur le chou qu'elle est en train de couper, faisant attention, chaque tranche se découpant lentement mais avec précision."


"Elle est un peu lente, mais vu qu'elle ne peut pas voir ce qu'elle fait, c'est déjà énorme qu'elle sache cuisiner tout court, pour Hanako et elle."


hi "Salut Hanako et Lilly. Vous avez besoin d'aide ?"

show lilly back_surprise_cas at twoleft
show hanako basic_normal_cas at tworight
with charaenter

stop music fadeout 0.3


$ doublespeak(li, ha, "C'est toi Hisa— ah !",  "Oh, bonjour, Hisao.")

show lilly basic_oops_cas
with charachange


"Lilly fait un pas en arrière de surprise avant de se retourner. Son petit cri fait que Hanako et moi venons à ses côtés."


hi "Qu'est-ce que... oh."


"Une petite goutte rouge coule de son doigt pâle, le couteau ayant coupé assez profondément pour qu'elle saigne."


"Avec le bruit de la télévision, elle n'a pas dû m'entendre arriver. De plus, pour compenser le fait qu'elle utilise le toucher pour se guider quand elle cuisine, elle doit beaucoup se concentrer."

show hanako defarms_shock_cas
with charachange

play music music_dreamy fadein 8.0


ha "Lilly !"

show lilly basic_weaksmile_cas
with charachange


li "Ne t'inquiète pas, Hanako. C'est juste une petite coupure."


hi "Tu devrais quand même mettre un pansement, au moins jusqu'à ce que ça arrête de saigner. Les trucs de premiers soins sont dans la salle de bains, non ?"

show lilly basic_sleepy_cas
with charachange


li "Je crois. Tu t'en sortiras ici, Hanako ?"

show hanako cover_worry_cas
with charachange


"Je fronce les sourcils en voyant à quel point elle ne se préoccupe pas d'elle-même alors que Hanako hoche la tête."

show hanako basic_worry_cas
with charachange


ha "C'est bon, je peux finir la préparation."

scene bg hok_bath
with locationskip


"Un silence gênant règne alors que je prends la bouteille d'antiseptique et une boîte de pansements sur le côté du lavabo, Lilly tenant son doigt en l'air en attendant que je m'en occupe."


"Le bouchon de la bouteille s'ouvre avec peu de résistance et la petite boule de coton que je trempe se ternit d'un vert léger."


hi "D'accord, ne bouge pas. Ça va peut-être faire un peu mal."

show lilly basic_weaksmile_cas_close at center
with charaenter


"Elle hoche la tête et j'attrape sa main pour la maintenir immobile. Avec autant de tendresse que possible, j'amène lentement le coton sur la petite ligne rouge."

show lilly basic_oops_cas_close
with charachange


li "Ah !"


hi "Quoi ? Je l'ai à peine touché."

show lilly basic_reminisce_cas_close
with charachange


li "Désolée..."


"Je soupire à sa réaction et pour me calmer un peu. Sa tolérance à la douleur est vraiment basse."


hi "Je te dirais bien de te comporter comme un homme, mais je ne peux pas vraiment."

show lilly basic_weaksmile_cas_close
with charachange


"Pendant qu'elle rit, je profite de sa distraction momentanée et presse gentiment plusieurs fois le coton contre son doigt. Heureusement, cela suffit."


"Nous nous calmons tous les deux pendant que j'applique le pansement sur son doigt, couvrant sa plaie."


hi "Voilà, fini. Tu peux bouger maintenant."


"Retirant sa main de l'emprise des miennes, elle bouge pour tester le résultat."

show lilly basic_smileclosed_cas_close
with charachange


li "Merci."


hi "Pas de problème. C'est le moins que je puisse faire après que tu te sois fait mal à cause de moi, après tout."

show lilly basic_emb_cas_close
with charachange


"Elle baisse la tête à mon excuse, se frottant la main dans ce qui semble être de l'embarras."

show lilly basic_weaksmile_cas_close
with charachange


li "Ce n'est vraiment pas grave."

stop music fadeout 5.0


"Sa réponse n'est pas très logique, vu que ce qui est arrivé est clairement de ma faute."


"Je ne peux pas m'empêcher de grimacer légèrement. Bien qu'elle sourie encore, elle ne doit pas aimer se faire rappeler les limites que lui impose son handicap."


"Je ne peux pas lui en vouloir. J'ai déjà ressenti la même chose auparavant, même si ma condition n'est pas aussi restrictive dans la vie de tous les jours."


"Aucun de nous deux n'est à l'aise, nous retournons alors dans la cuisine, d'où diverses odeurs de nourriture émanent."

scene bg hok_lounge
with shorttimeskip

play music music_another fadein 8.0


"Je pose les assiettes, la fumée s'élevant doucement du riz bien cuisiné et des plats au curry, pendant que Hanako dispose les couverts."


"Couteau d'un côté, fourchette de l'autre. Typiquement occidental. Ça convient parfaitement à quelqu'un comme Lilly."


"Alors que nous nous asseyons, faisant attention à la nappe rouge nous arrivant aux genoux, Lilly sort de la cuisine."


"Elle tient dans ses mains trois verres et... une bouteille de vin ?"


"Me rappelant notre dernière expérience avec cette substance, je me cache le visage avec la main."


hi "Alcool ? Sérieusement ?"


show lilly basic_cheerful_cas at center
with charaenter


"Elle s'arrête en atteignant la table, un sourire joyeux sur le visage."

show lilly basic_giggle_cas
with charachange


li "Akira m'a spécifiquement donné la permission de prendre une bouteille de sa collection."


"Non seulement elle donne de l'alcool à des mineurs, mais en plus elle les laisse même se fournir eux-mêmes ? Akira n'est pas le modèle parfait de l'adulte responsable."


"En plus de ça, ce n'est pas un repas qui se marie bien avec l'alcool. Je commence à croire que Lilly est le genre à devenir facilement accro."


hi "Ce n'est pas vraiment le problème. Je n'ai pas vraiment de scrupule avec l'alcool, mais la dernière fois ça ne s'est pas super bien passé, n'est-ce pas ?."

show lilly basic_smileclosed_cas
with charachange


li "La dernière fois nous avions trop bu, là un seul verre ne devrait pas être un problème."

show lilly basic_smile_cas
with charachange


li "Vois ça comme une expérience."


hi "Je ne ne connais pas beaucoup d'expériences qui me rendent malade avant de me coucher, mais d'accord."

show lilly basic_smileclosed_cas
with charachange


"Elle met un de ses doigts dans le verre pour jauger le niveau de vin, touche le bord du verre avec la bouteille et verse."


"Le blanc de ses doigts semble presque briller en reflet à la lumière du soleil, le contour flou se réfléchissant dans le verre."


"Ses doigts sont plus longs que les miens, ils font plus doigts de pianiste que d'enseignant. Elle serait douée si elle en jouait."

hide lilly
with charaexit


"Nous attaquons vite notre repas, couteaux et fourchettes s'entrechoquant avec les assiettes."


"Aucun d'entre nous n'a particulièrement envie de parler en mangeant, Lilly trop réservée pour parler, Hanako probablement trop timide, et moi trop occupé à manger."


"Une activité si commune, manger ensemble autour d'une table. Ça semble tout ce qu'il y a de plus normal, et pourtant ça me fait réaliser que ça fait vraiment très longtemps que je n'avais pas fait quelque chose comme ça."


"Juste nous trois, assis autour d'une table à manger, comme si on était une famille d'handicapés. Peut-être que ce voyage, même s'il s'arrêtait là, vaut le coup."

with shorttimeskip


"Ça prend un long moment, mais nous arrivons tous à finir notre repas, étonnamment copieux. Le vin, heureusement, a eu peu d'effet vu que nous n'avons eu qu'un verre ou deux chacun."


"Je m'adosse à ma chaise et me frotte le ventre de satisfaction."


hi "Je suis plein."

show lilly basic_smileclosed_cas at twoleft
show hanako basic_smile_cas at tworight
with charaenter


"Lilly se tapote la bouche avec une serviette. Deux fois. Seulement deux fois, aussi longtemps à chaque fois. C'est parfois difficile de dire si on assiste à une routine bien huilée ou à un acte bien répété."

show lilly basic_satisfied_cas
with charachange


li "Moi aussi. Tu as aimé, Hanako ?"

show hanako cover_bashful_cas
with charachange


ha "Mm, c'était bon."

show lilly basic_smileclosed_cas
with charachange


li "Maintenant que nous sommes rassasiés, on y va ?"


hi "Aller ? Où ?"

show lilly basic_weaksmile_cas
with charachange


li "Ah, tu n'étais pas là quand j'en ai parlé avec Hanako tout à l'heure."


"J'ai l'impression qu'elle lance une pique discrète à ma grasse matinée."

show hanako basic_bashful_cas
with charachange


ha "On a prévu d'aller en ville."


"J'imagine que j'aurais pu prévoir que deux filles en vacances voudraient aller faire du shopping, peu importe où elles se trouvent sur la planète."


"Ça m'intéresse de savoir ce qu'il y a dans cette région, c'est pas plus mal."


hi "Ça me va. C'est loin ou pas ?"

show lilly basic_smile_cas
with charachange


li "À peu près un kilomètre et demi, peut-être deux."

stop music fadeout 4.0


hi "Pas loin, hein ? Bien."


"Très bien même."

scene bg hok_road at bgright
with shorttimeskip

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_parkambience fadein 6.0
play music music_soothing fadein 0.5


"Alors que nous parcourons le chemin entouré d'arbres et de broussailles, je regarde Lilly et Hanako marcher devant moi."


"La légère brise ne m'empêche pas d'entendre la canne de Lilly taper doucement le sol. Je remarque que Lilly a retiré son pansement, maintenant que le saignement s'est arrêté."


"Une grande respiration d'air frais de la campagne me fait regretter de n'avoir pas grandi avec un air aussi pur que celui-ci."


"On n'a dû faire qu'un seul kilomètre et je transpire déjà. Il fait un peu chaud, je ne devrais pas être aussi dur avec moi."


hi "Hé Lilly, tu connais bien cette ville ?"

show lilly back_smileclosed_cas at center
show lillyprop back_cane
with charaenter


li "Vu que j'ai passé pas mal de mes vacances ici depuis que je suis entrée à Yamaku, je dirais que je la connais plutôt bien. On y allait tous les week-ends en voiture avant."


"J'aimerais bien qu'Akira soit là pour nous y amener."


"Je m'arrête un moment pour me frotter les mains plusieurs fois, histoire de faire partir l'étrange sensation d'engourdissement que j'ai."


hi "Tu t'y plais ?"

show lilly cane_weaksmile_cas
hide lillyprop
with charachange


li "Je dirais que c'est bien durant l'hiver, mais comme tu peux le constater, les étés sont un peu trop chauds pour que ce soit agréable. C'est calme, au moins."


li "La vraie maison de ma famille est encore plus au nord. Quand ils sont partis du Japon, ils nous l'ont donnée, à Akira et moi. Mais seule Akira y vit maintenant, depuis que j'ai déménagé à Yamaku."


hi "Eh bien, calme décrit bien l'endroit."


"Bien que je dirais plus perdu."


"À part la petite ville, il n'y a pas âme qui vive à des kilomètres à la ronde. Je viens d'une maison nichée dans une grande ville, c'est vraiment différent."


"Je crois que si je n'avais pas été à Yamaku, être à la campagne comme ça aurait été un trop grand changement pour que je m'y habitue."


"Après m'être habitué à l'isolement de l'école, l'idée de vivre dans un endroit comme celui-ci est presque agréable. D'être quelque part loin du tohu-bohu de la métropole."

show lilly cane_smile_cas
with charachange


li "Et donc Hisao, tu avais déjà été à Hokkaido ?"


hi "Nan. Je vivais dans le sud et on n'a jamais été aussi loin en vacances."

show lilly cane_cheerful_cas
with charachange


li "Eh bien, c'est une nouvelle expérience pour toi alors."


hi "Ouais, ça c'est sûr. Je suis surpris que ce soit aussi bien par ici."


hi "Et toi, Hanako ?"

show lilly cane_cheerful_cas at twoleft
show bg hok_road at center
with charamove

show hanako emb_smile_cas at tworight
with charaenter


"Elle secoue la tête."

show hanako basic_bashful_cas
with charachange


ha "C'est ma première fois aussi."


"Alors que nous continuons de marcher, je commence à avoir des fourmis dans les jambes. Comme si elles s'engourdissaient. C'est bizarre, étant donné qu'il n'y a pas de raison que ça arrive."

stop ambient fadeout 9.0
stop music fadeout 4.0


hi "Vous pourriez attendre une minute ? J'ai juste besoin de..."

show lilly cane_surprised_cas
with charachange


li "Quelque chose ne va pas ?"


hi "Nan, j'ai juste des fourmis dans..."

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

with Pause(0.05)

play sound sfx_heartstop
show heartattack alpha
with Dissolve (0.1)

show heartattack residual
with Dissolve (0.8)

play music music_tragic fadein 0.5

window show


"Mes cordes vocales se bloquent instantanément alors que ma poitrine se serre. Je place rapidement ma main dessus, essayant de contenir la vague de douleur qui se propage dans mon corps."

show lilly cane_reminisce_cas
show hanako defarms_strain_cas
with charachange


li "Hisao ?"


"Le visage de Lilly n'est que peu inquiet, elle ne sait pas ce qu'est en train de voir Hanako."


hi "Je vais bien, je vais... bien. Juste... fatigué..."


"Je retire mon bras de ma poitrine et me force à marcher de nouveau. C'est juste une petite palpitation comme une autre, elle passera vite, comme les autres."

play sound sfx_heartslow

show heartattack alpha
with Dissolve (0.1)

show heartattack residual
with Dissolve (0.8)


"Il ne me faut que quelques pas pour que mon corps se révolte contre moi, mes jambes commencent à flancher et mes forces semblent s'évaporer."

scene bg hok_road:
    xalign 0.5 yalign 0.52 rotate 0 zoom 1.0
    linear 0.1 rotate -6 zoom 1.2
show lilly cane_reminisce_cas:
    xanchor 0.5 xpos 0.3 yalign 0.52 rotate 0 zoom 1.0
    linear 0.1 xpos 0.25 rotate -6 zoom 1.2
show hanako defarms_strain_cas:
    xanchor 0.5 xpos 0.7 yalign 0.52 rotate 0 zoom 1.0
    linear 0.1 xpos 0.75 rotate -6 zoom 1.2
show heartattack residual
play sound sfx_pillow
with vpunch


"Avant que je ne puisse réagir, elles plient sous mon poids, me laissant à peine assez de temps pour placer mes mains sur le sol, et je me retrouve à genoux."


hi "Ah, merde..."

show hanako defarms_shock_cas
with charachange


ha "Hisa... AAAAH !"


"Alors que je relève la tête pour la voir, je me rends compte que mon visage est toujours tordu de douleur, aggravant son inquiétude."

show lilly cane_oops_cas
with charachange


li "Hisao ?! Hanako, dis-moi ce qui se passe !"


li "Hanako, dis-moi !"

show hanako def_strain_cas_close
with characlose


"Hanako se précipite à mes côtés alors que Lilly panique presque, ne sachant pas à quel point je vais mal. Alors qu'elle se tient là, pétrifiée, je baisse la tête et respire à fond."

scene black
show heartattack alpha
with shuteyefast


"Je me rends compte de quelque chose qui ne fait que m'énerver contre moi-même. Avec tout ça et le fait que je sois content d'être là, j'ai complètement oublié de prendre mes médicaments hier soir ou même ce matin."

stop music fadeout 9.0

hide heartattack
with Dissolve(3.0)


"Respirant une autre fois, la douleur vive dans ma poitrine commence à s'amenuiser aussi vite qu'elle est arrivée."


"Merci mon dieu. Merci, merci, merci, merci mon dieu."

play ambient sfx_parkambience fadein 6.0

scene bg hok_road
show lilly cane_oops_cas at twoleft
show hanako def_strain_cas_close at tworight
with openeye


"En même temps, je deviens conscient de la sueur coulant le long de mon visage et des deux filles effrayées à côté de moi."

show lilly cane_reminisce_cas
with charachange


li "Hisao !"


hi "Je vais bien, Lilly. Je vais... bien."

show hanako defarms_strain_cas_close
play sound sfx_impact
with vpunch


"Je m'appuie sur le sol pour me relever, les bras de Hanako près de moi au cas où je tombe et je titube un peu avant de retrouver mon équilibre."


"Je regarde Lilly et Hanako, toutes deux avec l'inquiétude inscrite sur le visage. Je me sens mal à cause de ça. Vraiment mal."

show lilly cane_sad_cas
with charachange


li "Je crois qu'on devrait rentrer."


hi "Je..."


"Réalisant l'inutilité de protester, je détourne le regard par frustration."


hi "D'accord."

stop ambient fadeout 2.0

$ suppress_window_after_timeskip = True

scene black
with dissolve



label fr_L16:

window hide None

scene black
with dissolve

scene bg hok_lounge_ss
with openeye

window show

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_cicadas fadein 2.0


"J'ouvre les yeux difficilement, complètement dépourvu d'énergie."


"Pendant un moment, je reste juste allongé sans bouger, regardant le plafond en me remémorant les évènements de la matinée pour organiser mes pensées."


"On a été marcher jusqu'à la ville. Mon cœur a failli me lâcher. On est rentrés. J'ai pris mes pilules. J'ai dormi."


"Je peux seulement me rappeler de chaque moment avec des images, mais l'ordre est clair. L'image du visage des filles est particulièrement désagréable, me faisant mal au cœur."


"Si je regarde suffisamment le plafond, je peux imaginer les carreaux et les fissures du plafond de l'hôpital. Ce fait seul suffit à me faire me redresser et à essayer de me ressaisir."


"Je me gratte le derrière de la tête, regardant autour de la pièce. Lilly et Hanako ne sont pas là et la télévision est éteinte."


"L'horloge au dessus de celle-ci dit qu'on est en fin d'après-midi. Le ciel un peu rouge visible par la fenêtre me confirme ce fait."


"Je me tourne et sors du futon, regagnant lentement mon équilibre. Je pense que je ferais mieux de chercher les filles pour voir si elles... vont bien..."


"Alors que je regarde par la fenêtre, je vois quelque chose au loin."


"Me frottant les yeux, je peux discerner la forme d'une personne. Ses longs cheveux blonds, virevoltant dans la légère brise, je les confondrais presque avec le jaune clair du champ de blé."


"Sans y penser, je sors de la pièce et vais à sa rencontre."

stop ambient fadeout 2.0
play music music_innocence fadein 14.0

scene bg hok_wheat_ss at Fullpan(8.0)
with Fade(0.5, 0.2, 3.0, color="#fff")


"La clarté du soleil couchant agresse mes yeux à peine réveillés, me forçant à les plisser jusqu'à ce qu'ils s'habituent."


"Les longs brins de blé jaunes contre mes jambes rendent la progression difficile."


"Néanmoins, mes yeux restent fixés sur l'avant, vers cette forme solitaire. En quelques minutes je l'atteins et reste à quelques mètres dans son dos."


hi "Lilly ?"

scene bg hok_wheat_ss at right
show lilly back_pout_cas_ss at center
with charaenter


"Elle se contente de hocher la tête."


hi "Où est Hanako ?"

show lilly back_listen_cas_ss
with charachange


li "Elle est au lit. Elle est allée dormir après que je l'ai calmée."


"Elle raconte ça avec le moins de mots possible, comme si en parler était rigoureusement interdit."


"Il y a quelque chose de différent. Son expression normalement confiante semble étrangement fragile, son corps n'offre aucune résistance à la brise soufflant sur sa jupe."


"Les brins de blé se balancent d'un côté à l'autre pendant un long moment, le seul son pouvant être entendu étant celui de leurs mouvements."


"Alors que nous nous tenons dans le champ, seuls, je sais ce que je dois demander."


hi "Qu'est-ce qui ne va pas, Lilly ? Tu n'agis pas comme d'habitude."

show lilly back_sad_cas_ss
with charachange


li "Tu te rappelles quand j'ai parlé de ma famille, Hisao ?"


hi "Ta famille..."


"Je baisse la tête en réfléchissant, puisant dans mes souvenirs. Ce souvenir semble être clair dans ma tête."


hi "Après l'anniversaire de Hanako ?"


"Elle hoche simplement la tête."

show lilly back_pout_cas_ss
with charachange


li "C'était bien... à ce moment. Toi et moi, faisant la fête avec Hanako. Partageant des cadeaux, parlant, s'amusant. C'était presque comme si on était une famille. Une petite, étrange famille."

show lilly back_sad_cas_ss
with charachange


li "Je pensais que ça pourrait continuer pour toujours. Juste nous trois, heureux ensemble."


"Elle prend une grande respiration, un léger tremblement dans celle-ci est à peine audible."

show lilly back_pout_cas_ss
with charachange


li "Même si ma famille est si loin... tant que nous sommes ensemble, c'est tout ce dont j'ai besoin. Je ne veux pas te perdre, Hisao."


li "Je n'avais même pas réalisé à quel point j'étais effrayée de perdre quelqu'un d'autre jusqu'à aujourd'hui. Jusqu'à..."


hi "Je suis désolé, Lilly. Je sais que mon corps est faible et là j'ai fait la plus grosse des erreurs."

stop music fadeout 4.0

show lilly back_sad_cas_ss
with charachange


li "Ne t'excuse pas... s'il te plaît ne t'excuse pas..."


hi "Lilly... ?"

show lilly basic_concerned_cas_ss
with charachange


"Elle se tourne vers moi, ses joues pâles couvertes de larmes."

show lilly basic_concerned_cas_close_ss
with characlose


"D'un pas maladroit, elle avance vers moi, son bras tendu à la recherche de ma présence."

play music music_romance fadein 2.0

window hide

scene unlock_ev lilly_wheat_close
show ev lilly_wheat_large:
    yalign 0.5 xalign 0.0 subpixel True
    easein 20.0 xalign 1.0
show ovl lilly_wheat_foreground:
    yalign 0.5 xalign 0.0 subpixel True
    easein 20.0 xalign 1.0
with GenericWhiteout(1.0, 0.0, 4.0)

window show


"Mon cœur ne s'accélère pas alors que j'avance vers Lilly, la prenant doucement dans mes bras alors qu'elle se colle contre moi en sanglotant."


"Avec son visage tremblant sur mon épaule, les prochains mots qui sortent de sa bouche sont ceux que j'attendais le moins."


li "Je t'aime, Hisao. Je t'aime, je t'aime, je t'aime, je t'aime, je t'aime !"


li "Ne pars pas, je t'en supplie. Jamais, ne pars jamais. Je t'aime... alors s'il te plaît... !"


"Donc.. c'est pour ça qu'elle agissait comme ça. Sa tendre voix quand je lui parle, l'inquiétude sincère dès que je souffre de quelque chose..."


"Après avoir été laissée au Japon sans sa famille et avec seulement Akira, Hanako et moi avec elle, elle était effrayée de perdre quelqu'un d'autre proche d'elle. Elle était vraiment inquiète pour moi."


"C'est un étrange sentiment. Un mélange de surprise, de chagrin et aussi la plus grande gratitude que je n'ai jamais ressentie. La seule réaction que j'arrive à sortir de ce tourbillon de sentiments est un léger soupir."


hi "Idiote va."


li "Hi... sao ?"


"Pendant un petit moment, son corps devient rigide, le seul mouvement visible est celui de la légère brise de l'après-midi."


hi "Je l'ai déjà dit avant, nan ? C'est normal de se sentir concernée par ceux qui sont proches de toi."


hi "Je suis toujours là, et je serai toujours là, parce que je veux te voir chaque jour. Pour partager mon bonheur avec toi, pour t'aider dans les moments de peine..."


hi "Mais surtout, je serai toujours là parce que je veux te voir sourire. Je veux voir ton vrai sourire."


"Une rafale de vent fait plier les longs épis de blé et une seconde de silence passe."


hi "Souris quand tu veux sourire. Pleure quand tu veux pleurer. Je t'aime, Lilly. Donc tu n'as plus besoin de te retenir maintenant."


"Sur ce, ses bras se resserrent sur moi aussi fort qu'elle peut et elle cache son visage dans mon cou."

scene ev lilly_wheat_small:
    xalign 0.5 yalign 0.5 zoom 1.1 subpixel True
    ease 16.0 zoom 1.0
with whiteout


"Ses larmes coulent le long de mon cou alors qu'elle pleure sans se retenir, maintenant que sa dernière résistance est tombée."


li "Hisao ! Hisao ! Hisao !"


"Je ferme les yeux et pose ma tête sur son épaule, tenant son corps fort contre moi."


hi "Tout va bien, Lilly. Je ne partirai jamais."


hi "Je te le promets."

stop music fadeout 6.0



label fr_L17:

scene bg hok_lounge_ss
with locationskip


"Nous retournons lentement à la maison, nous tenant l'un contre l'autre alors que nous nous asseyons ensemble. Lilly pose sa tête sur mon épaule tandis que je passe un bras autour de sa taille."


"Aucun d'entre nous n'a envie de briser le silence."


"Avec ses yeux fermés, il est dur de dire si elle s'est endormie ou pas. Pas que cela me gêne : la chaleur de son corps contre le mien, la douceur de sa main délicatement tenue par la mienne..."


"Pendant un long, long moment nous restons l'un contre l'autre, partageant notre chaleur et nos sentiments jusqu'à ce qu'il commence à faire nuit."


"La gentille, douce voix de Lilly brise le silence."

show lilly basic_smileclosed_cas_close_ss at center
with charaenter

play music music_twinkle fadein 6.0


li "Merci, Hisao."


hi "Pourquoi ?"

show lilly basic_smile_cas_close_ss
with charachange


li "De m'aimer aussi."


hi "Tu pensais que ce n'était pas le cas ?"

show lilly basic_weaksmile_cas_close_ss
with charachange


li "C'était une possibilité."


"Je respire profondément en réfléchissant. Ça, c'était de ma faute."


hi "C'est drôle, vraiment. Je pensais t'avouer mes sentiments bientôt."


hi "Je pense que dans un sens, tu m'as économisé cet effort."

show lilly basic_giggle_cas_close_ss
with charachange


"Elle lève la tête et rit un peu. Je souris à l'honnêteté de son rire, si féminin et léger. Elle se redresse un peu après ça, ses cheveux se posant à nouveau sur mon épaule."


hi "Tu te sens mieux ?"

show lilly basic_smileclosed_cas_close_ss
with charachange


"Elle hoche légèrement la tête."

show lilly basic_smile_cas_close_ss
with charachange


li "Tu es attentionné, Hisao. C'est ce que j'aime chez toi."


hi "Je suis désolé d'être comme ça. J'ai beau avoir vraiment voulu que tu ne t'inquiètes pas pour moi, je n'ai pas pu empêcher que cela arrive."

show lilly basic_concerned_cas_close_ss
with charachange


li "Ne t'excuse pas pour ça. S'il te plaît."


hi "Lilly ?"

show lilly basic_reminisce_cas_close_ss
with charachange


li "Est-ce que je me suis déjà excusée d'être aveugle ? Ne serait-ce qu'une fois ? Tu ne peux pas t'excuser de ce que tu es, Hisao. Ça ne sert à rien."


"Étonnamment, elle dit ça avec beaucoup de conviction. En fin de compte, c'était peut-être cette mentalité qui a fait qu'elle m'a pris sous son aile de la sorte, en plus de ses instincts maternels."


"Il me semble qu'elle m'a fait confiance rapidement, mais je ne me suis jamais demandé pourquoi. Maintenant il semble évidement qu'elle voulait m'aider pendant que je traversais un des pires moments de ma vie."


"Je suis sur le point de répondre, mais m'arrête alors que je sens ses doigts parcourir lentement mes cheveux. Je sens ses mouvements doux et délicats descendre pour tracer les contours de mon visage, sa paume s'arrêtant finalement sur ma joue."

show lilly basic_weaksmile_cas_close_ss
with charachange


li "Tu es quelqu'un de génial, Hisao. S'il te plaît, ne t'en excuse pas."


"Pendant un moment, j'en reste sans voix. Je penche lentement ma tête, et pose un léger baiser sur ses cheveux."


hi "On est un couple d'idiots, hein ?"

show lilly basic_cheerful_cas_close_ss
with charachange


li "...Oui."


"Après un long moment, elle rouvre la bouche."

show lilly basic_smile_cas_close_ss
with charachange


li "Hisao ?"


hi "Oui ?"

show lilly basic_smileclosed_cas_close_ss
with charachange


li "Ça..."

stop music fadeout 4.0

show lilly basic_weaksmile_cas_close_ss
with charachange


li "Ça ne me gênerait pas que tu..."


"Je sens sa main se raidir sous la mienne, tremblant légèrement. J'ai la bouche ouverte, essayant comme je peux de formuler une réponse à sa proposition."


hi "Lilly..."


"Avant que je ne puisse dire un autre mot, elle retire sa main de l'emprise de la mienne et attrape mon visage une fois de plus."

show lilly basic_pout_cas_close_ss
with charachange


li "S'il te plaît."


"Je souris paisiblement, tenant sa main contre ma joue en hochant la tête."


hi "D'accord."

play music music_heart fadein 0.5

show lilly basic_smileclosed_cas_close_ss
with charachange


"Pendant que je la regarde dans les yeux, elle se penche vers moi. Ses délicates lèvres touchent les miennes alors qu'elle se guide avec la main."


"Elle se retire moins d'une seconde après, souriant légèrement."

show lilly basic_smile_cas_close_ss
with charachange


li "Je t'aime, Hisao."

show lilly basic_smileclosed_cas_close_ss
with charachange


"Nous nous embrassons à nouveau, cette fois réciproquement."


"Alors que le premier était un baiser d'amour, celui-ci en est un de plaisir, nos langues se rencontrant et nos respirations devenant lourdes. Après de précieuses secondes, nous nous séparons et nous rougissons tous les deux."


"Nous posons tous les deux nos doigts sur nos lèvres, nous rappelant le sentiment fugace, rapidement submergé par nos envies et notre timidité."

show lilly basic_pout_cas_close_ss
with charachange


"Lilly est la première à remuer inconfortablement, cela dit."


hi "Qu'est-ce qu'il y a ?"

show lilly basic_weaksmile_cas_close_ss
with charachange


li "Est-ce qu'on devrait... se mettre plus à l'aise ?"


hi "Mmh ? Ah, d-d'accord..."


"Maintenant qu'elle le mentionne, le futon est un peu trop étroit pour faire quelque chose dessus. Vu ce à quoi on pense tous les deux, c'est normal que l'un de nous prévoie les choses."

show lilly invis:
    ypos 1.2
with dissolvecharamove

hide lilly
with vpunch


"Je prends ses mains et la guide sur le côté, le bref et gênant silence s'arrête à l'instant où nous nous asseyons sur le sol l'un en face de l'autre."


"Alors que je m'avance pour retirer son haut, elle s'arrête après avoir avancé ses mains pour faire la même chose."

show lilly basic_concerned_cas_close_ss:
    center
    ypos 1.17
with charaenter


li "Tu trembles..."


"Je m'arrête un moment et regarde mes mains."


"Effectivement, elles tremblent légèrement. Mais je ne sais pas si c'est de la nervosité ou de l'excitation."


hi "Euh... on dirait bien."

show lilly basic_weaksmile_cas_close_ss
with charachange


li "Donc tu es aussi nerveux que moi ?"


"Je repose mes mains et soupire, essayant de me calmer. On a le temps, alors pas besoin de se dépêcher."


hi "Désolé, c'est ma première fois, alors je suis un peu..."

show lilly basic_cheerfulblush_cas_close_ss
with charachange


"Elle rit nerveusement, confirmant ce que je pensais."

show lilly basic_smile_cas_close_ss
with charachange


li "Pour moi aussi. Je suis contente que... nous puissions partager ça."


"Je souris aussi, me penchant pour la serrer dans mes bras tandis qu'elle m'étreint également."


hi "Je t'aime, Lilly."

show lilly basic_smileclosed_cas_close_ss
with charachange


li "Tu l'as déjà dit."


"Je ne peux pas m'empêcher de sourire. Même dans une telle situation, elle reste telle qu'elle est."

hide lilly
with charaexit


"Nous décidons finalement de retirer nos vêtements nous-mêmes. Même si c'est plus simple comme ça, je pense que c'est juste une façon de faire autre chose, pour nous calmer."


"Avec des mains légèrement raides, je commence à enlever le premier bouton de ma chemise."


"Une fois que nous avons retiré tous nos vêtements qui finissent en pile derrière nous, mon souffle est coupé par la vue qui m'est offerte."

label fr_L17h:

show lilly behind_reminisce_nak_ss
with charaenter


"Ses longues jambes galbées, ses larges hanches et sa poitrine, généreuse mais délicate... son visage légèrement rougi, doux et timide est traversé par une mèche de ses cheveux."


"Ses mains, qu'elle tient serrées derrière elle, ne font qu'accentuer sa poitrine. Son corps nu, grand et pâle, est magnifique."


"Cette fille en face de moi, réservée mais joueuse, rusée mais gentille, est la fille dont je suis tombé amoureux."


"Je m'avance, attrapant délicatement ses épaules avec mes mains."

show lilly behind_listen_nak_close_ss
with charachange


"Alors que je fais ça, elle porte les siennes à ma poitrine. Avec une respiration légèrement lourde, nous nous embrassons langoureusement."


"Je sens une des mains de Lilly monter jusqu'à mon épaule et sa tête se penche légèrement en avant. Comprenant son intention, je m'accoude au sol."


hi "Ah..."

scene evhunlock lilly_handjob_chest_normal_small
show evh lilly_handjob_chest_normal:
    xalign 0.7 yalign 1.0 subpixel True
    ease 8.0 xalign 0.4 yalign 0.2
with whiteout


"Elle se penche sur moi, une main me caressant les cheveux et l'autre qui se dirige vers ma poitrine. Le sentiment de sa poitrine contre la mienne est suffisant pour m'exciter."


"Ça doit être sa façon de voir ce que j'ai déjà vu d'elle. Malgré sa cécité, elle enregistre chaque détail de mon corps et de ma poitrine dans sa mémoire."


"Quand son majeur arrive dans le léger creux de ma cicatrice, une marque persistante de mon opération d'il y a des mois, elle la parcourt doucement sur toute la longueur avec sa main."

show evhunlock lilly_handjob_chest_frown_small
show evh lilly_handjob_chest_frown:
    xalign 0.4 yalign 0.2
with charachange


li "C'est..."


hi "La cicatrice, de mon opération au cœur."


"Pendant un moment, elle semble ne pas savoir quoi dire, l'idée d'une cicatrice si grande ne faisant que l'inquiéter encore plus. Son expression passe de la curiosité à l'appréhension."


li "Est-ce qu'on... devrait vraiment faire ce genre de choses... ?"


"Ces mots me gênent beaucoup. L'expression de Lilly me brise plus le cœur que ses mots le pourraient et je ne connais pas la réponse à sa question."


"Je ne peux laisser ma condition me dominer pour toujours. C'est peut-être déconseillé pour ma santé, mais je refuse de vivre dans une prison."


hi "Ça va, Lilly. Ça ira si ce n'est que ça."

show evh lilly_handjob_chest_normal
with charachange


"Son expression troublée reste un moment, mais elle finit par acquiescer, sa main descend sur mon ventre puis ma cuisse."

show evh lilly_handjob_chest_normal:
    zoom 1.0 xalign 0.4 yalign 0.2
    ease 4.0 zoom 0.667 xalign 0.5 yalign 0.5
with None

show evh lilly_handjob_stroke_normopen:
    zoom 1.0 xalign 0.4 yalign 0.2
    ease 4.0 zoom 0.667 xalign 0.5 yalign 0.5
with charachange


"Avec un air de légère surprise, elle descend doucement ses mains, sa respiration s'accélérant alors qu'elle atteint mes poils pubiens."


"Elle déplace légèrement sa main, touchant délicatement l'endroit le plus intime de mon corps."

show evh lilly_handjob_stroke_normshut_small:
    truecenter
    zoom 1.0
with charachange


li "C... c'est..."


hi "O-ouais."


"Notre nervosité s'agrandit d'autant plus que l'acte commence, sa main bougeant doucement de bas en haut avec énormément de précautions comme si ça pouvait se casser au moindre faux mouvement."


"Je ne sais pas si c'est juste pour me soutenir ou si j'ai envie de la tenir, mais j'utilise ma main libre pour lui tenir le côté du visage. La sensation de ses cheveux et de sa peau douce est agréable et cela semble lui faire plaisir."


"Le simple fait qu'elle me touche est étonnamment érotique. Je sens mon corps se relaxer alors que je m'abandonne au sentiment de plaisir qui me submerge."


"De longues minutes passent dans un silence presque total, notre respiration étant le seul son qui peut être entendu. Les doigts de Lilly s'arrêtent pour me caresser avec affection l'aine, alors qu'elle ouvre la bouche encore une fois."

show evh lilly_handjob_stroke_flustopen_small
with charachange


li "Hisao..."


"J'attends pendant une seconde le reste de sa phrase, qui ne vient pas. Elle a beau être en train d'essayer de prendre l'initiative, elle est toujours très nerveuse."


"Je ne peux pas m'empêcher de sourire alors que je lui enlève les cheveux du visage, la rassurant. Aussi nerveuse qu'elle puisse être, je suis content que Lilly prenne l'initiative. Je serais probablement aussi nerveux qu'elle si ça avait été moi."

show evh lilly_handjob_stroke_normopen_small
with charachange


hi "Oui."


"Elle s'arrête un moment avant de hocher la tête, s'asseyant et mettant ses jambes autour de moi. Encore une fois, mon souffle est coupé par la magnifique vue de son corps au-dessus du mien."

show evh lilly_cowgirl_smile_small
with whiteout


"Je peux seulement la regarder pendant qu'elle s'abaisse délicatement, la bouche encore légèrement ouverte. Elle commence à descendre lentement ses hanches, sa douceur enveloppant complètement mon esprit."

show evh lilly_cowgirl_weaksmile_small
with charachange


"Elle respire profondément pour se ressaisir, son visage restant ferme. Ses mains sont posées sur mon corps pour le sentir, la situation intime permettant de compenser le manque de contact visuel."


"Elle descend doucement sur moi, ses genoux et ses mains la supportant. Son corps entier se raidit tandis que je rentre en elle, son expression exprimant de la douleur."


"Malgré ça, je ne peux pas m'empêcher de savourer la douce, chaude sensation m'enveloppant, la sensation de plaisir surplombant tous mes sens."


"Mon membre en vient à disparaître complètement en elle tandis qu'elle rentre légèrement ses ongles dans ma poitrine dans l'effort de s'empêcher de gémir de douleur. Un gémissement, trop difficile à contenir, s'échappe de ses lèvres."


"Alors que j'ouvre la bouche pour la réconforter, je vois des gouttes rouges à peine visibles couler d'entre ses jambes."


hi "Lilly, si c'est trop..."

scene evh lilly_cowgirl_strain_small
with charachange


"Elle se pince les lèvres fort, secouant la tête rapidement. Après quelques secondes son corps se relaxe légèrement, bien qu'elle soit évidemment loin d'être à l'aise."


li "C... c'est bon... Ça va."

scene evh lilly_cowgirl_frown_small
with charachange


"Elle avale difficilement sa salive, essayant de se ressaisir."


"Se soulevant lentement et se rabaissant, elle se relaxe légèrement alors que la sensation de plaisir commence à surpasser la douleur."

scene evh lilly_cowgirl_strain_small
with charachange


"Sa respiration commence à s'accélérer comme la mienne, son corps bougeant presque trop lentement. Elle a l'air de commencer à lentement apprécier l'acte, mes sensations se joignant aux siennes."


"Je ne sais pas si elle continue à ce rythme pour elle ou pour moi, mais dans tous les cas... à cette vitesse, je crois que je peux... garder mon corps sous contrôle. C'est drôle, d'une certaine façon, que même maintenant je dépende d'elle."


"Que nous soyons aussi proches, comme ça, que nos sensations soient les mêmes... ça me fait plaisir. De partager notre premier moment comme ça ensemble... dans une sensation... presque... irrésistible..."


hi "Je t'aime... Lilly..."

scene evh lilly_cowgirl_cry_small
with charachange


li "Hisao... Hisao... !"


"Je peux sentir son corps se contracter, sa respiration et ses mouvements devenant de moins en moins contrôlés. Je suis content de pouvoir lui faire autant de bien, mais alors que j'y pense, je peux sentir que j'atteins rapidement ma limite."

scene white
with Dissolve(3.0)


"Je perds le contrôle de mon corps et serre fort les dents, un fort gémissement m'échappe alors que j'atteins l'orgasme et que mes hanches rentrent fort en elle. Elle se penche au même moment, sa poitrine se posant sur mon torse."


"Nous restons l'un dans l'autre un moment, dans un sentiment de post-orgasme, mon esprit complètement paralysé par la sensation pendant de précieuses secondes."

scene evh lilly_cowgirl_weaksmile_small
with charachange


"Cette sensation finit bien trop rapidement et nos corps se relâchent d'épuisement avec Lilly tenant à peine au-dessus de moi."


"J'arrive à passer mes bras autour de son corps faible et transpirant et pendant quelques minutes nous restons simplement là, savourant silencieusement le contact de l'autre, nous remettant de l'expérience."


"Aucun d'entre nous n'aurait pu savoir qu'une telle chose allait se produire, de ça je suis certain."


"Complètement épuisé, n'étant pas en état de discuter, je regarde son visage fatigué. On dirait que l'effort, à la fois physique et mental, l'a presque poussée au bord de l'évanouissement."


hi "Je t'aime, Lilly."

scene evh lilly_cowgirl_smile_small
with charachange


"Elle hoche légèrement la tête, me caressant les cheveux de sa main gauche. Si on pouvait rester juste comme ça pour l'éternité, ce serait le paradis."

stop music fadeout 2.0

scene black
with dissolve



label fr_L18:

scene bg hok_lounge_rn
with locationchange

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_rain fadein 1.0


"Après avoir été réveillé par un son, j'ouvre les yeux avec réticence."


"Tournant la tête à gauche, je vois la pluie frapper la vitre bruyamment. Le vent s'attaque au verre, comme s'il faisait de son mieux pour se rattraper de la chaleur d'été de la veille."


"Je m'assois sur le futon, me tenant la nuque à cause de la douleur engendrée par l'étrange position dans laquelle j'ai dormi."


"Je devrais me lamenter du tour que prend la météo, vu que c'est notre dernier jour ici. Cela dit, Les évènements de la veille refusent de quitter mes pensées."


"Le sentiment de tenir Lilly pleurant contre moi. Le mélange de notre luxure et de nos hormones qui nous ont fait passer la nuit ensemble. Ça semble presque futile d'essayer de rationaliser tout ce qui est arrivé."


"Dans une tentative de penser à autre chose, je grogne et me penche pour attraper mon sac sans me lever. Sortant un flacon après un autre, je prends mon régiment journalier de pilules et les avale sans y prêter attention."

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")

window hide
nvl show dissolve

nvl clear


n "\n\n\n\nIl m'a fallu étonnamment peu de temps pour m'habituer à avaler les pilules sans eau. Cela dit, c'est aussi vrai pour m'être habitué à vivre dans une école pour handicapés."


n "Me rappelant Yamaku, je suis encore plus content d'avoir eu une chance de m'échapper, même si ce n'est que pour quelques jours."


n "J'apprécie la chance de passer du temps avec Lilly et Hanako, loin de toute l'activité scolaire, vu les dernières complications."


n "Je n'aurais jamais cru dire ça, mais l'idée de vivre loin de la ville est agréable, une zone tranquille est attirante. C'est une pensée qui, il y a un an, m'aurait paru ridicule."

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")

nvl clear
nvl hide dissolve

window show


"Un éclair rose, qui est sans doute la robe de Hanako, se fait voir. Réalisant que je dois avoir l'air peu présentable vu que je viens de me réveiller, je lance les pilules restante dans ma bouche et passe la main dans mes cheveux."

show hanagown smile_rn at center
with charaenter


ha "Bonjour, Hisao."


hi "Ah, bon— argh !"

$ renpy.music.set_volume(0.0, 0.2, channel="ambient")

with vpunch


"Je lui réponds en oubliant complètement que je suis en train d'avaler une pilule particulièrement large. Toussant et crachotant, je m'étouffe violemment avec."

show hanagown worry_rn
with charachange


ha "Ah, Hisao !"

$ renpy.music.set_volume(0.2, 10.0, channel="ambient")


"Après avoir toussé bruyamment et me tapant la poitrine plusieurs fois, j'arrive à la faire passer."


hi "Je vais bien. Désolé, j'avais oublié que j'étais en train d'avaler."

play music music_happiness fadein 5.0

show hanagown distant_rn
with charachange


ha "Désolée, je ne voulais pas—"


"Je lève la main, faisant signe à Hanako d'arrêter."


hi "Je me suis étouffé, c'est ma faute. Bonjour, Hanako."


"Elle s'arrête un moment, avant de faire une courbette en retour."

show hanagown distant_rn at tworight
show bg hok_lounge_rn at bgright
with charamove

show lilly basic_sleepy_paj_rn at twoleft
with charaenter


"Marchant, non, chancelant derrière Hanako se trouve Lilly, elle aussi habillée en pyjama. Avec ses yeux encore endormis et ses cheveux n'importe comment, elle vaut le détour."


hi "Salut, Lilly."

show lilly basic_weaksmile_paj_rn at twoleft
with charaenter


li "Bonjour... Hisao."


"Pendant un moment, il y a un silence gênant dans l'air, aucun d'entre nous ne sachant quoi faire."


"Étant donné ce qui s'est passé la nuit dernière, nous avons tous les deux suffisamment de raisons pour trouver la situation gênante. Comment sommes-nous censés réagir après quelque chose comme... ça ?"


"La meilleure chose à faire serait de parler seul à seul avec Lilly, pour mettre les choses en ordre."


hi "Hum, je vais... préparer le petit déjeuner."


"Lilly comprend où je veux en venir."

show lilly basic_smileclosed_paj_rn
with charachange


li "Je vais t'aider. Hanako, tu peux mettre la table ?"


"Elle hoche la tête, disparaissant dans un placard, se mettant vite à la tâche qui lui est assignée."

$ renpy.music.set_volume(0.1, 0.5, channel="ambient")

scene bg hok_kitchen_rn
with locationchange


"Je me frotte un peu les yeux alors que je me dirige vers le frigo et en sors du lait, et Lilly attrape plusieurs boîtes de couleurs vives dans un placard à côté d'elle."


"Pendant que nous sommes en train de faire le repas, je chuchote, assez discrètement, sachant que Lilly n'aura pas de problème pour me comprendre."


hi "Est-ce que ça va, Lilly ? Après hier soir..."

show lilly basic_reminisce_paj_rn at center
with charaenter


"Elle hoche délicatement la tête, une expression quelque peu faible sur son visage."


"Bien que sa fatigue ait sûrement un rôle à jouer, elle est déstabilisée par ce qui est arrivé entre nous et ne sait pas comment gérer les choses à partir de maintenant. Je ne peux pas lui en vouloir, vu que je pense la même chose qu'elle."

show lilly basic_sad_paj_rn
with charachange


li "Je suis désolée, Hisao. Je ne pensais pas clairement hier. Je pensais à toi et à Hanako et pourtant j'ai été si loin..."


"Elle se referme sur elle-même. Avec ses mains et sa voix se resserrant, je lui tapote le dos et essaye d'éclaircir la situation."


hi "Tu n'as pas à t'excuser. J'ai dit que je t'aimais aussi, après tout."

show lilly basic_oops_paj_rn
with charachange


li "Mais je..."


"Alors que ça ne s'améliore pas, il devient évident que je n'ai plus qu'une seule option."

show lilly basic_sad_paj_close_rn
with characlose


"Me tournant vers Lilly, je l'embrasse tendrement. Elle ne résiste pas du tout et me rend le baiser."

show lilly basic_sad_paj_close_rn at twoleft
show bg hok_kitchen_rn at bgleft
with charamove

show hanagown normal_rn at tworight
with charaenter


"Bien que ce n'ait duré que quelques secondes, je remarque que Hanako est en train de nous regarder sans un mot. L'assiette dans sa main suspendue au-dessus de la table, son action stoppée par ce qu'elle a vu."

stop music fadeout 2.0

scene bg hok_lounge_rn
show hanagown distant_rn:
    tworight
    ypos 1.15
show lilly basic_sleepy_paj_rn:
    twoleft
    ypos 1.17
with shorttimeskip

$ renpy.music.set_volume(0.2, 0.5, channel="ambient")


"On n'entend plus que le cliquetis des couverts sur les assiettes. Par rapport à avant, où seuls Lilly et moi étions gênés, la situation a complètement changé."


"Après des semaines d'amitié parfaite, à partager des repas ensemble, ou parler de choses sans importance, la relation que j'ai avec Lilly, non, que nous avons tous les trois, a irréversiblement changé."


"Je ne peux pas supporter ça."


hi "Lilly..."

stop ambient fadeout 25.0

show lilly basic_listen_paj_rn
with charachange


"Elle hoche solennellement la tête, posant la cuillère sur le plat en face d'elle. Aucun de nous deux ne sait exactement comment considérer l'autre, et encore moins comment Hanako nous voit."

show lilly basic_weaksmile_paj_rn
with charachange


li "Ça va peut-être te paraître abrupt mais... je me suis déclarée à Hisao."

show hanagown distant_blush_rn
with charachange


"Pendant un moment, Hanako semble un peu confuse. Précisément la réaction que je pensais qu'elle aurait. Elle hoche la tête avec la cuillère toujours dans la bouche."

show hanagown normal_blush_rn
with charachange


ha "Tu as répondu quoi ?"


hi "Oui."

show hanagown smile_rn
with charachange


"Elle affiche un sourire tellement grand, tellement honnête, que j'en viens à rougir. Je crois que c'est le sourire le plus grand que j'ai vu de sa part."

play music music_serene fadein 6.0


ha "Alors je suis contente. Je suis vraiment, vraiment contente."

show lilly basic_sleepy_paj_rn
with charachange


li "Je suis désolée de ne pas te l'avoir dit avant. Les choses ont été..."


"Hanako secoue la tête de droite à gauche, oubliant apparemment que Lilly ne peut pas le remarquer."

show hanagown distant_blush_rn
with charachange


"Elle commence à agiter les mains, ayant l'air un peu plus nerveuse qu'avant."


ha "Pour être honnête, j'ai commencé à croire qu'il y avait quelque chose il y a un moment déjà. Au début je ne savais pas quoi penser... mais je..."

show hanagown smile_rn
with charachange


ha "Je me suis dit qu'en fin de compte... si mes amis sont heureux, alors je suis heureuse."


ha "J'étais vraiment contente d'avoir un autre ami quand j'ai rencontré Hisao, donc que tu trouves l'amour avec lui est encore mieux... non ?"


"Un sentiment de soulagement me submerge maintenant que je sais qu'elle approuve notre relation. Lilly ressent la même chose, à en juger par son expression."

show lilly basic_weaksmile_paj_rn
with charachange


li "Merci, Hanako. J'apprécie vraiment que tu sois aussi compréhensive."

show hanagown distant_rn
with charachange


"La voix de Lilly semble toujours un peu désolée, ou du moins incertaine. Ça n'échappe pas à Hanako qui semble être perdue dans ses pensées un moment avant de se tourner vers moi."

show hanagown smile_rn
with charachange


ha "Hisao, ça te gêne si je sors un moment avec Lilly ?"


hi "Ah, non, vas-y..."

show lilly basic_surprised_paj_rn
with charachange


li "Hanako ?"

show hanagown smile_rn at tworight
with charamove

show lilly basic_surprised_paj_rn at twoleft
with charamove

hide lilly
hide hanagown
with charaexit

stop ambient
$ renpy.music.set_volume(1.0, 0.0, channel="ambient")


"Hanako se lève, prend la main de Lilly et la tire jusqu'à la porte. Vu le rythme typiquement lent et sûr de Lilly, le fait que Hanako soit pressée rend sa marche quelque peu étrange et elle en perd presque l'équilibre plusieurs fois."


"C'est une vision amusante, me laissant sans voix jusqu'à ce qu'elles passent la porte. C'est maintenant que je remarque qu'il ne pleut plus et que la pluie a laissé place à un ciel clair et ensoleillé, comme pour se rattraper du gris de ce matin."


"Pour Hanako, ça doit être une grande révélation. Lilly et moi sommes les seules personnes qu'elle fréquente vraiment, un peu comme si nous étions ses parents."


"Je suppose que ça pourrait être la meilleure façon de décrire la relation que nous partageons. Un père, une mère et une fille, s'amusant dans notre petite famille imaginaire comme si ça pouvait durer toujours."


"C'est peut-être une relation bancale, une qui ne pourrait certainement pas durer longtemps... mais peut-être que juste pour ces petits moments, ça vaut la peine."


"Je me lève et vais rejoindre Lilly et Hanako dans les champs dehors."


"Ce petit moment de bonheur, aussi bref qu'il puisse être, continuera d'exister en moi, en nous tous, pour toujours."

stop music fadeout 2.0

label fr_L19:

scene bg hok_bath
show steam
with shorttimeskip


"Immergé dans l'eau chaude, je soupire profondément. Le sentiment de sentir chaque muscle de mon corps se relaxer est euphorique."


"Je ne sais absolument pas depuis quand je n'avais pas pris un bon bain chaud, mais maintenant je m'en moque complètement."

play music music_dreamy fadein 2.0

nvl clear
window hide

nvl show dissolve


n "Peut-être que c'est parce ce bain implique plus qu'un bain normal que je l'apprécie autant, la chance de me poser, me permettant de me détendre et d'avoir un peu de temps pour moi."


n "Hanako, Lilly et moi nous sommes baladés dehors, explorant la grande étendue de champs entourant la maison. Puis nous avons passé la majeure partie de l'après-midi à nous reposer, regarder la télévision, lire, et jouer aux cartes."


n "Ça n'a peut-être pas été une dernière journée de vacances des plus excitantes, mais la tranquillité est quelque chose à savourer. Même après être retourné à l'école demain, je crois que je me rappellerai de cette petite maison à Hokkaido pendant longtemps."


n "C'est dommage qu'on n'ait plus que quelques heures avant de devoir aller prendre notre train du retour."


n "Je me contente de bâiller en regardant la fumée s'élever lentement de l'eau claire, mes yeux finissant par s'arrêter sur le plafond."


n "Nos examens sont imminents. J'ai à peine révisé."


n "En plus de cela, je ne sais même pas ce que je ferai après avoir eu mon diplôme. Passer les examens est une chose, mais dans quel but ?"


n "Et surtout, maintenant, je suis dans une relation amoureuse."

nvl clear
nvl hide dissolve
window show


hi "Mais qu'est-ce que je fous ?"

"…"


"...Je ne crois pas que je devrais penser comme ça. Ce qui est fait est fait, et peut-être que ça peut être vu comme un autre aspect de la nouvelle vie que je m'efforce de construire."


"J'aime être avec Lilly et il y a plus dans la vie que l'école et le travail, après tout."


"Alors que je suis occupé à rationaliser tout ce qui est arrivé, j'entends une série de coups à la porte. Je me redresse, essayant d'en savoir l'auteur."


"Trois coups, ni plus ni moins. Légers et pourtant sûrs et rythmés comme un métronome. Je serais surpris que ça ne soit pas Lilly."


li "Je peux... entrer ?"


"Ouais, c'est Lilly."


hi "Je suis toujours dans le bain, je sors dans une seconde."


li "...Je sais."

stop music fadeout 3.0


"La réponse venant de l'autre côté de la porte me paralyse. Après y avoir pensé, je me rallonge dans le bain et laisse mes bras posés sur les côtés."


"Bien que j'essaye de ne pas y faire attention, je n'arrive pas à m'empêcher d'imaginer des choses."


hi "P-pas de problème, entre."

show lilly basic_smileclosed_cas at Alphain(1.0), Slide(0.4, 0.5, 0.5, 0.5, 1.0)
with Pause(1.0)


"Sur ce elle ouvre la porte, rentre lentement dans la pièce et referme derrière elle. Elle a l'air étrangement calme, rassurant mon cœur battant la chamade."


hi "Ah... s-salut... Lilly."

play music music_one fadein 9.0

show lilly basic_smile_cas at center
with charachange


li "Ça te gêne si je prends un bain avec toi ?"


hi "Pas du tout. Viens."

show lilly basic_listen_cas at center
with charachange


"Après un petit hochement de tête, elle commence à enlever son haut, découvrant sa poitrine peu à peu."


hi "Je peux t'aider, si tu veux."

show lilly basic_emb_cas at center
with charachange


li "Non."


hi "Pourquoi ?"

show lilly basic_pout_cas at center
with charachange

li "…"


"Son visage montre qu'elle est toujours un peu mal à l'aise à l'idée de me laisser faire ça. Je ne peux pas lui en vouloir."

hide lilly
with charaexit

play sound sfx_rustling


"Elle continue de se déshabiller, sa chemise et sa jupe tombant au sol et la laissant en petite culotte et soutien-gorge. Et enfin, elle se tient nue au centre de la pièce."

label fr_L19h:

show lilly behind_sleepy_nak at center
with charachange


"Comparé à la dernière fois, c'est beaucoup plus facile de la voir entièrement. Vraiment magnifique."


li "Hisao ?"


hi "Mmh ?"

show lilly behind_pout_nak at center
with charaenter


li "Tu penses à des choses perverses, n'est-ce pas ?"


hi "Tu ne peux pas m'en vouloir, tu es en train de te déshabiller en face de moi."

show lilly behind_weaksmile_nak at center
with charachange


"Elle fronce les sourcils."


li "Je crois que c'est quelque peu plus érotique pour toi que pour moi."


hi "Pourquoi ?"


hi "...Ah."

show lilly behind_giggle_nak at center
with charachange


"Elle émet un petit rire amusé, ce qui semble la calmer un peu."

show lilly behind_smile_nak at center
with charachange


li "Si c'est trop pour toi Hisao, je peux revenir plus tard."


hi "Non, non, c'est bon. Je suis juste un peu... eh bien..."


hi "Tu es vraiment belle, tu sais."

show lilly behind_emb_nak at center
with charachange


"Mon commentaire tout ce qu'il y a de plus honnête fait rougir Lilly."


li "Hisao..."


"Je souris un peu. Elle est belle quand elle est surprise comme ça."

show lilly behind_smileclosed_nak at center
with charachange


li "Dans tous les cas, je peux venir ?"


hi "Ah, bien sûr."

hide lilly
with charaexit


"Je me penche en avant et prends sa douce main dans la mienne, l'aidant à rentrer dans le bain."


"Elle tâte le bord de la baignoire puis se baisse lentement, me surprenant quand elle s'assoit et s'adosse à moi, ses jambes à l'intérieur des miennes. Je m'attendais à ce qu'elle s'asseye de l'autre côté."

scene evh lilly_bath_smile_small
with whiteout


"Respirant à fond pour me calmer, je pose mes bras sur les côtés de la baignoire alors que je tente de contrôler mes pulsions."


"Loin d'ignorer la vue de ses... atouts, le sentiment de son corps contre le mien est étonnamment relaxant. Avec Lilly qui est si sensible au toucher, ça doit l'être encore plus pour elle."


li "Tu aimes tes bains plutôt chauds, hein ?"


hi "Un peu. Tu veux que je mette un peu d'eau froide ?"


"Elle secoue un peu la tête."


li "Non, c'est bon."


hi "D'accord."


"La conversation s'arrête brusquement, le silence prenant le dessus."

show evh lilly_bath_emb_small
with charachange


"Un très long et très étrange silence."


li "Peut-être que c'était un peu trop..."


hi "Ne t'inquiète pas, c'est pas grave."


"La situation devient encore plus étrange. Comme pour se distraire, Lilly fait glisser sa main libre le long de ses jambes, tandis que l'autre se tient la poitrine par pudeur."


"Je regarde silencieusement le mur en face de moi et la fumée montante, jetant de temps en temps un coup d'œil à son corps."


"Le blanc de sa peau brille tandis qu'elle fait glisser sa main sur ses jambes, leur longueur et fermeté étant encore plus remarquables."


hi "Tu sais, comparée à Akira, tu as plus l'air étrangère."


li "J'ai pris du côté de ma mère, génétiquement. Akira plutôt du côté de mon père."


hi "Ça se tient. Mais comment est-ce qu'une Écossaise et un businessman japonais en viennent à se rencontrer, d'ailleurs ?"


li "Ma mère était journaliste. Elle a rencontré mon père pendant qu'elle était à une conférence à Inverness."


hi "Ah, je vois. Et ton côté écossais explique ta taille, je présume."


"Je la regarde de bas en haut alors qu'elle hoche la tête et soupire au ridicule de la situation."


hi "C'est vraiment trop, hein ?"

show evh lilly_bath_smile_small
with charachange


li "Avoue que tu apprécies quand même, hein ?"


hi "D'une certaine façon, oui. Ça s'est bien passé, en fin de compte."


hi "Tout s'est bien arrangé, Hanako a approuvé notre relation et on retourne à l'école demain."


li "Oui. C'est dommage qu'on doive y retourner aussi tôt, mais on aura toujours les souvenirs de cet endroit."


hi "Souvenirs, hein ? Je suppose. On devra voir comment les choses se dérouleront quand on rentrera, mais pour l'instant... je suis juste content que tu m'apprécies."


hi "Je me monte la tête à ce sujet depuis des semaines, donc je suis content que les choses se soient passées comme ça."


"Elle hoche la tête et se repose sur moi, partageant la chaleur de nos corps."


"Je ne suis pas sûr qu'elle soit d'accord avec ça, mais mes envies commencent rapidement à prendre le dessus."


hi "Dis, Lilly ?"


li "Oui ?"


hi "Comment c'était ? Hier soir, je veux dire."


"Elle s'arrête un moment avant de baisser légèrement la tête. Un léger sourire se profile sur ses lèvres en même temps qu'elle rougit, son corps se relaxant. C'est plus que suffisant pour répondre à ma question."


"Les évènements de la veille me reviennent en tête. Au vu de la situation, je ne pense pas qu'on puisse me le reprocher."


li "Hisao, ton cœur bat fort..."


"Sa voix est interrompue par ma main se plaçant sur sa hanche. Bien que j'aie résisté auparavant, le souvenir de notre première fois est suffisant pour me faire flancher."


"Elle se laisse faire sans protester, une invitation que j'aurais du mal à ignorer même si je le voulais. Je l'embrasse dans le cou, avant de glisser lentement mes mains sur ses douces jambes."


li "Hisao, s'il te plaît..."


"Même si elle dit ça, sur sa bouche se profile un sourire et son ton est entre l'embarras et le rire."

show evh lilly_bath_open_small
with charachange


"Finalement elle prend une de mes mains dans les siennes et me guide jusqu'à son sein droit. J'apprécie grandement qu'elle veuille me guider."

show evh lilly_bath_grab_small
with charachange


"Tous les signes de tension que montrait son corps disparaissent. Je continue d'apprécier la sensation de sa douce peau, redoublée alors que ma main glisse entre ses jambes."


"Je me demande si la sensation de mes mains est accentuée par son manque de vue, vu que tous ses autres sens sont améliorés."


"Elle semble apprécier cela grandement. Ça me fait une drôle de sensation, en y pensant, mais c'est agréable."

show evh lilly_bath_moan_small
with charachange


"Ça ne prend que quelques minutes pour qu'elle commence à remuer, ses efforts pour contenir ses gémissements devenant visibles alors qu'elle plisse les lèvres. Ses protestations légères, à peine chuchotées, deviennent de plus en plus rares."


"Ça me fait réaliser que le fait qu'elle remue contre mon corps m'excite beaucoup également."


hi "Lilly..."

show evh lilly_bath_smile_small
with charachange


"Je retire mes mains pour lui donner suffisamment de liberté pour répondre. Hochant la tête, elle se redresse et m'offre ses mains pour que je l'aide à sortir de la baignoire."

scene evh lilly_afterbath_open_small
with locationchange


"Elle sort du bain en même temps que moi, ses mains dans les miennes."


"Je m'assois contre le bord de la baignoire, et nous bougeons un peu pour trouver une position confortable. Avec un petit gémissement, difficilement contenu pour éviter qu'il soit audible de l'extérieur, elle s'abaisse sur moi encore une fois."


"La façon dont elle bouge rend évident le fait qu'elle doit toujours être à la limite de l'orgasme."


"Elle commence à bouger lentement de haut en bas, sa langue trouve la mienne dans un baiser langoureux. Je réalise maintenant à quel point lui avoir fait ressentir du plaisir m'a excité."

scene evh lilly_afterbath_shut_small
with locationchange


li "Hisao... Hisao..."


"Bien que ses yeux soient fermés, ses mains serrées sur mes épaules montrent qu'elle est sur le point d'atteindre le point culminant."


"Alors que nos respirations deviennent de plus en plus fortes, je sens rapidement que j'approche ma limite aussi."


"Une série de respirations rapides est le seul avertissement que j'ai avant son gémissement final d'extase, son corps entier devenant tendu et ses ongles me rentrant dans les épaules."


"Mes reins se joignent aux siens, et nous restons tous les deux figés dans notre orgasme."

with Fade(0.5,1.0,4.0, color="#FFF")
stop music fadeout 8.0


"En quelques précieuses secondes, tout est fini, Lilly s'affaisse sur moi alors que j'essaye de retrouver mon calme."


hi "C'était... bien..."


"Elle prend une bouffée d'air avant de répondre, se redressant et hochant la tête."

li "Mm…"


"Elle se baisse pour m'embrasser, ma main lui tenant le visage pour dégager ses cheveux, et nous nous retrouvons encore une fois assis, dans un silence apaisant."

stop music fadeout 2.0

scene black
with dissolve

label fr_L20:

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_trainint fadein 5.0

scene ev lilly_trainride_ni
show train_scenery_ni
show train_scenery_fg_ni
show lilly_trainride_ni norm at train_shake
with locationchange


"Après une ruée chaotique vers la station et trouvant nos sièges dans un train désert, nous sommes enfin assis. Regardant l'heure, presque minuit, ça ne me surprend pas que le train soit presque vide."


"Hanako s'endort rapidement sur l'épaule de Lilly et j'arrive à peine à rester éveillé. Ce que nous avons fait plus tôt n'aidant probablement pas."


"Je serais probablement un peu déprimé de retourner à l'école, si mon cerveau était en état de marche."


"Ceci dit, la vue de nuit depuis la fenêtre du train est vraiment belle."


"Mon long bâillement est presque entièrement étouffé par le cliquetis du train qui circule."


hi "Trop fatigué..."

play music music_comfort fadein 2.0

show lilly_trainride_ni ara at train_shake
with charachange


li "À qui la faute, Hisao ?"


"Elle est vraiment à la limite entre la critique et l'humour, parfois. Mais j'arrive à sourire quand même."


"Je regarde par la fenêtre, mon reflet est à peine visible sur la vitre. Pour dire la vérité, elle a raison. Si on n'avait pas eu ce petit interlude il y a quelques heures, on aurait tous les deux beaucoup plus d'énergie."


"En plus de ça, on a tous les deux dû prendre un autre bain, nous mettant presque en retard pour le départ du train."


hi "Ouais, ouais, c'était ma faute. Mais bon, rentrer dans un bain avec un gars, c'est dangereux."

show lilly_trainride_ni smile at train_shake
with charachange


li "Apparemment."


hi "Désolé, j'ai quelque peu pris avantage de la situation."

show lilly_trainride_ni weaksmile at train_shake
with charachange


li "Eh bien... Ce n'est pas comme si j'avais détesté..."


"Alors qu'elle dit ça, je la regarde. Mes yeux remarquent ses joues légèrement rouges et son petit sourire, ses pensées s'évadant ailleurs."


hi "Dis-le."


li "Je... savais qu'il y avait une possibilité que... ça arrive."


hi "Je le savais. Tu es aussi perverse que moi."


"Elle toussote dans sa main libre, montrant sa désapprobation."

show lilly_trainride_ni pout at train_shake
with charachange


li "C'est une façon un peu grossière de le dire."


hi "Oh ? Et tu dirais quoi toi ?"


li "Que je suis juste une jeune adulte en bonne santé avec une libido tout à fait naturelle."


hi "En d'autres mots, perverse."


"Comme si elle était consciente de la scène, Hanako marmonne doucement avant de placer sa tête sur les jambes de Lilly."

show lilly_trainride_ni opensmile at train_shake
with charachange


"L'expression de désapprobation de Lilly disparaît alors qu'elle sourit et caresse doucement les longs cheveux noirs de Hanako."


"Tout ce que je peux faire, c'est les regarder. Sourire et regarder."


"Si quelqu'un venait à me demander quand je suis tombé amoureux d'elle, je ne saurais pas répondre. La seule chose que je serais capable de dire est : “C'est juste arrivé à un moment, mais je ne m'en suis pas rendu compte.”"


"Si quelqu'un venait à me demander pourquoi je suis tombé amoureux d'elle, alors je pourrais répondre bien plus facilement."


hi "Tu aimes vraiment Hanako, hein ?"

show lilly_trainride_ni smile at train_shake
with charachange


"Elle hoche lentement la tête, toujours avec son sourire chaleureux."

label fr_choiceL20:
menu:
    with menueffect
    li "C'est dommage qu'on doive retourner à l'école. Elle semblait si relaxée pendant ces journées où on n'y était pas."
    "Parler de Hanako.":




        return m1
    "Parler de l'école.":


        return m2


label fr_L20a:


$ renpy.music.set_volume(0.5, 1.0, channel="ambient")


hi "Je ne pense pas qu'il ait matière à s'inquiéter. Hanako a gagné de la confiance grâce à toi, du moins depuis que je vous connais."

show lilly_trainride_ni weaksmile at train_shake
with charachange


"Elle soupire doucement."


li "Je crois que je lui ai à peine apporté de la compagnie et du soutien. Depuis qu'elle te connaît, elle s'est beaucoup plus ouverte, même à moi."


"J'ai le sentiment qu'elle sait l'influence qu'elle a sur Hanako , surtout qu'avant qu'elles ne se connaissent, Hanako n'avait pour ainsi dire, aucun ami."


"Les amis que j'avais dans ma précédente école ont rempli le rôle que j'attendais d'eux, généralement celui de partager simplement des discussions, mais Hanako et Lilly ont une relation bien plus profonde."


"Une part de moi les envie, mais une autre ne peut pas ignorer le fait que l'année scolaire finira dans pas si longtemps. Après ça, je n'ai aucune idée de ce que fera Hanako. Le voyage m'a montré à quel point on dépend tous les uns des autres."


"Forcément, on va tous devoir prendre des décisions. Peut-être que c'est pourquoi, malgré notre retour à l'école signifiant un retour à la vie normale, je ne peux pas m'empêcher de me sentir un peu inquiet."

label fr_L20b:


$ renpy.music.set_volume(0.5, 1.0, channel="ambient")


hi "Oui. Les examens vont bientôt commencer, on devra gérer ça aussi. Tu penses être prête ?"

show lilly_trainride_ni weaksmile at train_shake
with charachange


li "Je crois. Mais ça ne sera sûrement pas une période agréable, non plus."


"Je suis d'accord avec elle. Les examens me sont complètement sortis de la tête et même si je peux m'en sortir pour la plupart des contrôles, je ne suis pas sûr de pouvoir passer si facilement si je ne révise pas un peu."


"Lilly semble bien plus studieuse, ou du moins plus organisée que moi. Cela dit, elle doit gérer le fait d'avoir du mal dans certaines matières malgré son travail."


hi "Au moins cette période ne durera que quelques semaines."

label fr_L20c:



hi "Le bon côté, c'est que les vacances d'été ne sont pas longtemps après nos examens. On pourra retourner à Hokkaido à ce moment-là, si tu veux."


"Pendant un moment elle y réfléchit, son expression devenant quelque peu distante. Je ne peux qu'imaginer qu'elle pense à tout ce qui est arrivé ici."

show lilly_trainride_ni opensmile at train_shake
with charachange


li "Ça serait... bien, je crois."


"Je hoche la tête, lui souriant."


"L'été, ensemble avec Lilly. Ça semble être le meilleur moyen de passer nos vacances."

stop music fadeout 3.0
stop ambient fadeout 3.0

window hide
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
