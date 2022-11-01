label fr_R30:

window hide None

scene bg school_scienceroom
with locationchange

window show

play music music_normal fadein 3.0


"J'arrive à temps pour les cours, bien que pas à temps pour le petit déjeuner."


"La salle de classe est baignée dans la douce lumière du soleil."


"Ça signifie qu'il fera intolérablement chaud cet après-midi. Pour l'instant, cela dit, c'est plaisant."


"Je regarde la discussion animée de Misha et Shizune, Hanako regardant par la fenêtre de la classe, Mutou entrant dans la classe quatre minutes en retard et sans savoir ce qu'il est censé enseigner aujourd'hui."


"Je n'aurais jamais pu imaginer décrocher de l'école comme ça, même si c'est juste pour quelques semaines."


"D'un autre côté, Rin ne semble pas avoir de problème avec l'idée, ou même pour le faire vraiment."


"Mais encore, d'une certaine façon, je me suis fait embarquer dans son isolement fou, et on finit par se faire mal mutuellement."


"J'ai un doute. Peut-être qu'il n'y a que moi qui ai souffert."

scene bg school_scienceroom_ss
with shorttimeskip


"Ce n'est que tard dans l'après-midi que je réalise qu'on est lundi. Le club d'art se réunit aujourd'hui."


"Pas seulement ça. À cause des examens, ça sera la dernière réunion du club avec les vacances d’été."




label fr_R30x:


"Je n'ai pas grand-chose à faire ici..."


"Mais je veux parler au professeur."

scene bg school_hallway3
with locationchange


"Donc, je finis par traîner d'un air gêné devant la salle d'art, attendant que la réunion se termine."


no "C'est tout pour ce semestre !"


"Sa voix est suffisamment forte pour que je l'entende à travers la porte, et bien trop enthousiaste pour être honnête."


no "La prochaine réunion aura lieu après les vacances d’été, le mardi de la première semaine du semestre."


no "J’espère tous vous revoir à ce moment-là !"


no "Passez de bonnes vacances !"

play ambient sfx_crowd_indoors fadein 1.0
stop music fadeout 4.0

show crowd
with charaenter


"Il y a en réponse un ensemble de voix loin d'être unanimes, et la porte de la classe s'ouvre, libérant un flux d'étudiants."


"J’attends que tout le monde parte, pour pouvoir parler seul à Nomiya. Il est presque l'heure de dîner, alors je n'ai pas à attendre longtemps."

stop ambient fadeout 2.0

scene bg school_classroomart_ss
with locationchange




label fr_R30y:


"Sans Rin, ça semble presque inutile d'y aller, mais je veux parler avec le professeur."

scene bg school_classroomart_ss
with locationskip


"La réunion en elle-même n'est pas intéressante, tout comme mes talents en aquarelle."


"Nomiya essaye de m’encourager et de me conseiller sans sembler trop condescendant, mais il n'est pas très doué pour ça."


"Dans tout les cas, rejoindre le club d'art m'a appris que j'aime l'art. Ça serait bien si je pouvais faire de l'art dans le club d'art quand même."


"Après que les fruits du labeur de tout le monde se retrouvent posés en une jolie pile sur le bureau du professeur, il se racle la gorge et fait un petit discours."

show nomiya talk at center
with charaenter


no "C'est tout pour ce semestre !"


"Sa voix est très forte et bien trop enthousiaste pour être honnête."

show nomiya smile
with charachange


no "La prochaine réunion aura lieu après les vacances d’été, le mardi de la première semaine du semestre."


no "J’espère tous vous revoir à ce moment-là !"

show nomiya veryhappy
with charachange


no "Passez de bonnes vacances !"

hide nomiya
with charaexit

stop music fadeout 4.0


"Tout le monde lui souhaite également de bonnes vacances tout en se dirigeant vers la porte."


"Je reste en arrière, attendant qu'on soit seuls tous les deux. Il est presque l'heure du dîner, alors je n'ai pas à attendre longtemps."


label fr_R30z:


"Nomiya regarde les peintures, parmi lesquelles certaines sont assez bien."


"Rin pourrait surpasser tout le monde dans le club d'art, mais elle n'est pas la seule avec du talent."


hi "Excusez-moi, monsieur..."

play music music_happiness fadein 2.0

show nomiya smile at center
with charaenter


no "Mmh ? Qu'y a-t-il, Nakai ?"


"Il hausse les sourcils d'un air curieux, souriant à pleines dents."


hi "C'est à propos de Rin..."

show nomiya frown
with charachange


no "Oh ? Quelque chose ne va pas avec Tezuka ?"


hi "Non, mais..."


"J’hésite pendant une fraction de seconde, pas certain de savoir comment je veux dire ça, laissant à Nomiya suffisamment de temps pour marmonner tout seul."

show nomiya smile
with charachange


no "Je l'ai vue il y a quelques jours quand je passais par la galerie de Sae."


no "Elle a dit qu'elle aurait fini une ou deux autres peintures pour l'exposition."

show nomiya talk
with charachange


no "J'ai été agréablement surprise, elle travaille étonnamment dur. J'ai toujours pensé qu'elle était un peu paresseuse, faisant ce qu'elle voulait avec les devoirs..."


"Il semble remarquer mon anxiété et réalise qu'il s’écarte du sujet, se taisant avant de finir sa phrase."

show nomiya smile
with charachange


no "Ah, mais tu avais quelque chose à dire. Qu'y a-t-il ?"


hi "Je ne sais pas... elle semble détachée de tout, comme si elle ne pouvait penser qu'à l'exposition."

show nomiya frown
with charachange


no "Bah, c'est bien non ? Elle est concentrée sur ses peintures, comme elle le devrait."


hi "Ouais, mais c'est différent, c'est comme si elle était obsédée. J'ai été la voir, et..."

show nomiya serious
with charachange


no "Tu as été la gêner ?"


"Il m’interrompt avant que je puisse finir ce que je voulais dire, semblant instantanément énervé."


hi "Non... Je ne... crois pas."


hi "Je suis inquiet parce qu'elle a complètement arrêté de venir à l'école. Je la trouve bizarre, aussi."


hi "Plus que d’habitude, du moins."

show nomiya stern
with charachange


no "Bwah ! C'est bien plus important pour elle qu'un stupide cours de math, de physique, ou quoi que ce soit."


no "C'est exactement pour ça que cette école est aussi flexible, pour donner à tous les étudiants une chance de se réaliser."

show nomiya serious
with charachange


no "Tezuka est une peintre, alors elle devrait peindre, hein ? Et avoir une exposition. C'est ce que font les artistes. Elle devrait être autorisée à se concentrer sur ça, pas sur les autres cours inutiles. Elle devrait être encouragée."


no "Si tu y penses, c'est assez évident."


"Ses contre-arguments ne sont pas très convaincants, mais j'ai du mal à trouver quelque chose à y redire."


"Mon silence mécontent est pris comme un assentiment, et Nomiya se tourne pour rassembler les devoirs rendus par les élèves."

show nomiya smile
with charachange


no "Je dois dire, pendant qu'on parle de l'exposition de Tezuka..."


no "J'ai vraiment hâte de voir comment ça va finir."

show nomiya dreamy
with charachange


no "Elle est encore si jeune, et a tant de talent, et de style !"


"Il parle tout seul, pour détendre l'ambiance sûrement trop négative à son goût."

show nomiya talk
with charachange


no "J'en déduis que tu seras là ?"


hi "Ouais, je pense bien."

show nomiya smile
with charachange


no "Bon, on se verra là-bas alors."

stop music fadeout 3.0

scene bg school_hallway3
with locationchange


"Je comprends qu'il est temps pour moi de partir. Et c'est ce que je fais, sans être satisfait."


"Mon message ne semble pas être passé, c'est rien de le dire."

$ suppress_window_after_timeskip = True

scene black
with dissolve


label fr_R31:

window hide None
nvl clear

scene bg school_scienceroom_bw
with locationchange

nvl show dissolve

play music music_night fadein 1.0


n "\n\n\n\n\n\n\n\n\nLe jour après ça, toutes les opportunités loupées et les choses que j'aurais dû dire reviennent me hanter. Il n'y a rien que je puisse faire à part broyer du noir."

nvl clear
nvl hide dissolve

with shorttimeskip

nvl show dissolve


n "\n\n\n\n\n\n\n\n\nSecond jour. Je commence à me sentir anxieux. Je commence à douter de mes doutes et je me sens idiot, surtout parce que je n'arrive toujours pas à penser à autre chose qu'à Rin."

nvl clear
nvl hide dissolve

with shorttimeskip

nvl show dissolve


n "\n\n\n\n\n\n\n\n\nTroisième jour. Examen de japonais {b}et{/b} d'histoire. Super. La chose que je déteste le plus est qu'elle me fait me sentir aussi mal alors que je devrais me concentrer sur totalement autre chose."

nvl clear
nvl hide dissolve

with shorttimeskip

nvl show dissolve


n "\n\n\n\n\n\n\n\n\nQuatrième jour. Examen de math. On a un examen de math. Ça ira comme ça ira. Je m'en fous."

nvl clear
nvl hide dissolve

with shorttimeskip

nvl show dissolve


n "\n\n\n\n\n\n\n\n\nCinquième jour. Nomiya me demande encore si je compte aller au vernissage de l'exposition. Je ne peux pas lui dire non, même si j'en ai sérieusement envie. Je ne veux pas discuter avec lui de Rin ou quoi que ce soit, alors c'est mieux de n'opposer aucune résistance."

nvl clear
nvl hide dissolve

stop music fadeout 2.0

scene bg school_dormhallway
show rin basic_absent at center
with shorttimeskip

window show


"Le sixième jour, le jour avant le vernissage de l'exposition, je vois Rin dans le couloir, se tenant en face de ma chambre quand je rentre aux dortoirs après le dîner."

play music music_rain fadein 6.0


hi "Qu'est-ce que tu fais là ?"


"Mon ton est plus énervé que je l'aurais voulu.. Je suis un peu déçu de ne pas être capable de me retenir, mais je n'y peux rien."


"Rin se tient juste là, comme si elle s'était retrouvée par coïncidence ici et n'avait aucune raison précise pour être là. La façon dont elle réagit si calmement dans toutes les situations m’énerve maintenant."


"C'est pas bon. Ça fait six jours, et rien que de la voir, je bous. Et elle n'a pas encore ouvert la bouche."

show rin basic_deadpan
with charachange


rin "Fini de peindre."


hi "Tu ne devrais être à la galerie ? À préparer ?"

show rin basic_awayabsent
with charachange


rin "Ils ont dit que non."


"J'imagine que la propriétaire de la galerie s'occupe de ça alors, mettre les peintures sous cadre, les mettre sur les murs et tout."


hi "Alors, pourquoi t'es ici ?"

show rin basic_deadpannormal
with charachange


rin "J'avais envie."


"Le même schéma idiot se répète ; moi posant des questions et elle qui répond avec des réponses qui ne veulent rien dire, parce que c'est la seule façon qu'on a de converser."


"Sauf que j'écoute ses bavardages à propos de je ne sais quoi, ce qui n'est pas vraiment une conversation."



"Est-ce un jeu ? Est-ce qu'il y a des rôles attribués dont je n'ai pas connaissance, dictant les règles de notre relation, nous menant inévitablement à nous blesser mutuellement ?"


"Sa réponse nonchalante accompagnée d'un haussement d'épaules encore plus nonchalant ne m'éclaire pas plus. J'imagine que je devrais être content que les préparations de son exposition soient finies."

play sound sfx_dooropen

scene bg school_dormhisao
with locationchange


"Quand je rentre dans ma chambre, j’entends ses pas me suivre."


"Je ne l'ai pas invitée à rentrer. Je ne vais pas lui demander de partir."

show rin basic_awayabsent:
    center
    alpha 0.0
    ease 0.5 ypos 1.15 alpha 1.0
    parallel:
        ease 0.3 center
    parallel:
        "rin basic_absent" with Dissolve(0.3, alpha=True)
with Pause(0.5)

stop music fadeout 6.0


"Elle se met sur mon lit sans demander la permission, ce qui fait que j'aurais voulu avoir pris le temps de le faire ce matin, puis se rélève comme si elle venait de s'asseoir sur des charbons ardents."


"Je me mets contre le seul coin de mon bureau qui n'est pas encombré avec des trucs, pour reposer un peu mes jambes."

show rin basic_awayabsent:
    center
    alpha 1.0
with charachange


"Rin passe un peu de temps à jeter des coups d’œil curieux dans ma chambre. C'est là que je réalise qu'elle n’était encore jamais venue."


"Pendant un moment, elle semble être concentrée. Essayant de tout analyser. Ça doit être ce regard pour le détail qui fait d'elle une artiste."

show rin basic_absent
with charachange


"Vu que la pièce est petite, elle fait un tour rapide de toutes les choses qu'il y a à voir, mais rien n'en ressort, ce qui fait que le silence reprend le dessus dans la chambre."


"L'ambiance est au mieux froide, nous sommes tous les deux sur nos gardes, attendant que l'autre fasse le premier pas."


"Bien sûr, Rin pourrait jouer à ce jeu pour toujours. Alors ça doit être moi."


hi "Donc..."


"J'abandonne parce qu'elle n'essayerait jamais de commencer la conversation, et parce qu'on dirait qu'elle veut dire quelque chose, et je veux en finir."


"Pour quelle autre raison serait-elle ici si ce n'est pas pour parler ?"


"Je ne sais pas quoi dire moi-même. Je veux être en colère, mais je ne peux pas me résoudre à lui crier dessus ou quelque chose comme ça."


"Ma voix attire son attention, et elle essaye de chercher des mots, mais on dirait qu'elle n'est pas certaine elle-même de savoir pourquoi elle est là"

show rin basic_absent_close:
    center
    ypos 1.05
    easein 0.5 ypos 1.0
with characlose


"Et donc, Rin fait simplement quelques pas en avant pour réduire la distance entre nous, et se met sur la pointe des pieds pour réduire notre différence de taille..."

window hide

show rin basic_lucid_superclose at center
with charachange


centered "“C'était une mauvaise idée.”"


centered "“Peut-être que tu devrais oublier ça et je ferai de même.”"

window show


"C'est un réflexe, et presque comme une arrière-pensée, les mots “non”, “oui” et “peut-être” apparaissent simultanément dans mon esprit."


"Ma main est entre ses lèvres et les miennes, un mur que j'ai élevé pour me protéger de... quelque chose."


"Son souffle est chaud sur mes doigts. L'odeur de sa peau arrive jusqu’à mes narines, une sensation indescriptible me capture et attire mon regard profondément dans le sien."

show rin basic_surprised_close
with charachange

play music music_moonlight fadein 0.5


"L'expression dans ses yeux montre de la surprise, étonnée de la main qui empêche ses avances."


"Ses yeux sont vraiment grands et brillent, humides, fixés directement sur les miens avec un regard doux que j'ai du mal à égaler."


"La bouche mi-ouverte de Rin lui donne l'air encore plus confus, bien que la façon sensuelle avec laquelle ses lèvres se courbent signale quelque chose de complètement différent."

show rin basic_upset_close
with charachange


rin "S'il te plaît."

show rin negative_angry_close
with charachange


rin "J'ai besoin de toi."


"Les mots sortent de sa bouche dans un souffle qui n'est destiné qu'à moi, passant sur sa langue et entre ses dents sans s'interrompre."

show rin negative_angry
with Dissolve(0.15)
with vpunch


"Ils me frappent d'un coup, et je recule un peu maladroitement pour accentuer la distance entre nous, me cognant à mon bureau dans l'action."


"Peut-être que c'est son choix de mots, peut-être la façon dont elle l'a dit, mais quelque chose m'a atteint."


"Quelque chose ne va pas, quelque chose ne va vraiment pas."


hi "Besoin de moi pour quoi ?"


"Alors que le sentiment désagréable monte encore en moi, je sens le battement de mon cœur accélérer grandement."

show rin basic_absent
with charachange


"Le regard de Rin dévie du mien pour revenir alors que son corps se relaxe de son état de tension, et elle se repositionne normalement."

show rin basic_deadpanupset
with charachange


rin "Je ne pense pas que je pensais quoi que ce soit. Pourquoi tu dessines des trucs dans la poussière de ta table de nuit ?"

show rin basic_awayabsent
with charachange


rin "Il y a un mot pour ce genre de choses mais je ne me rappelle pas..."


"Sa remarque me prend par surprise et je regarde par-dessus son épaule sur la table à côté de mon lit, mais je ne vois rien à cette distance."


"Donc elle a besoin de moi pour quelque chose de spécifique ou pas ?"


"Elle est passée juste parce qu'elle pensait que ça me ferait plaisir après m'avoir repoussé sans discussion pendant une semaine."


"Une motivation complètement altruiste ?"


"Elle en avait envie ?"


hi "Conneries. Je peux en deviner moi-même les raisons."


hi "Pour jouer avec moi quand tu le veux, m'embrasser quand tu le veux, m'ignorer quand tu le veux, pour satisfaire tes caprices quand tu le veux ?"


hi "C'est ça ? Pour ça que tu as besoin de moi ?"


"Ma voix semblait très en colère encore une fois, même pour moi."


extend " Bien."

show rin basic_absent
with charachange


"Rin aussi finit par comprendre l'humeur, et son expression curieuse change instantanément en quelque chose de plus compliqué."

show rin negative_sad
with charachange


rin "Non—"


"Elle s’arrête là, le regard passant d'un point à un autre sans arrêt, cherchant dans la pièce comme si les mots qu'elle essayait de trouver étaient écrits sur mes murs."


hi "Alors quoi ?"

show rin negative_confused
with charachange

stop music fadeout 2.0


rin "J'avais besoin de peindre."


"Peindre."


"Bien sûr. C'est ce que font les artistes."


"Les mots rebondissent à l'intérieur de moi, passant dans mon sang avec le sifflement perçant de ma colère."

play music music_tragic fadein 2.0


hi "Ne me sors pas ça, Rin ! Je ne suis pas une fichue muse pour toi, avec qui tu peux jouer dans l’intérêt de la peinture !"


hi "Je ne suis pas un moyen d'obtenir ce que tu veux, je suis moi !"


hi "Ça change quoi que je ne sache rien de mon avenir ?"


hi "Il y a des choses que je veux, et des choses qui sont importantes pour moi ! Même moi je peux rêver d'autres choses que de cauchemars !"


"Je crie, mais j'ai dépassé le point de me soucier de choses comme ça."

show rin negative_sad
with charachange


"Rin regarde ses doigts de pieds et les remue d'un air mélancolique tout en encaissant ma rage sans rien dire pour se défendre."


"Seulement après que j'aie fini elle essaye de répondre quelque chose."

show rin basic_sad
with charachange


rin "Je ne peux rien faire d'autre. Ou je peux faire toutes sortes de choses, mais je... ne peux pas... faire."

show rin basic_upset
with charachange


rin "C'est la seule chose que je fais bien. La plupart du temps."


"Je comprends ça. L'art d'abord, tout en seconde place, ou millième."


hi "Et moi ? Je ne suis rien ? Quand je me suis intéressé à l'art, est-ce que ça t'a donné l'impression que j'étais un peu intéressant, pendant un moment ?"


hi "Dis-moi, je veux vraiment savoir. Tu as déjà pensé à ma perspective, ou est-ce que c'est juste tout pour toi ?"


"Les mots remontent comme de la bile dans ma gorge."

show rin basic_surprised
with charachange


"Elle semble alarmée. Et aussi complètement perdue, comme si elle elle ne comprenait pas pourquoi j'étais en colère."


"Je n'arrive pas à croire qu'elle puisse être aussi stupide."

show rin negative_sad
with charachange


rin "Je ne voulais pas— ?"


"Cette fois c'est Rin qui s’interrompt au milieu de sa phrase."

show rin basic_upset
with charachange


rin "Tu ne comprends pas ? Je ne peux pas."


hi "Peux pas quoi ?"


hi "Tu n'expliques jamais ! Comment est-ce que je suis censé comprendre quoi que ce soit si tu ne dis jamais rien ?"


hi "Pourquoi tu ne parles jamais ?"


hi "Dis quelque chose !"


"Mais elle ne dit rien."


"Défouler ma colère sur elle me fait du bien. Je me sens mal de ressentir ça, mais je ne peux pas m’arrêter."

show rin negative_annoyed
with charachange


"Ne voulant pas faire face à ma colère de plein fouet, Rin se tourne pour regarder par la fenêtre même s'il n'y a rien à voir."


"Le pire de ce que j'ai à dire est sorti, je me tais parce que je ne peux pas continuer de lui crier dessus alors qu'elle est de dos, donc le silence retombe finalement."


"J'essaye de discerner quelques indices de sa réaction à travers ma vision obscurcie par l’adrénaline."


"Mon commentaire n'était pas le meilleur qui soit, mais j’espère que Rin a compris qu'elle ne peut pas juste ignorer tout le reste quand l'envie lui en vient."


"Je voudrais vraiment qu'elle comprenne. Elle n'écoute jamais rien, elle est insensible au monde autour d'elle."


"Pas cette fois, on dirait."


"Son corps est tremblant comme si elle retenait ses larmes, mais je sais déjà que Rin ne pleure pas."


"Son indifférence me rend furieux. Maintenant que c'est sorti, je suis un peu troublé. Je me demande..."


"Est-ce que j'ai été trop loin ?"


hi "Écoute, je—"

show rin negative_angry
with charachange


rin "Va-t'en."


rin "Va-t'en, Hisao."


"Sa voix est faible et fatiguée alors qu'elle dit ça, mais j'entends clairement ses mots."

"…"


"Qu'est-ce que je peux dire de plus ?"


hi "C'est ma chambre."


"Cette remarque crue et vide est une bonne conclusion à la discussion désagréable qui est devenue encore plus désagréable depuis que c'est un concours de cris à sens unique."

show rin basic_lucid
with charachange


"Après un moment pour se ressaisir, Rin abandonne, je peux le voir dans la façon dont elle affaisse les épaules et part."

hide rin
with charaexit


"Même si elle regarde délibérément dans une autre direction, je peux voir comment elle se mord le coin de la lèvre si fort que ça pourrait se mettre à saigner si elle ne s’arrête pas."


"Alors qu'elle fait sa sortie, je réalise qu'elle a laissé la porte ouverte quand elle est entrée et que mes cris ont dû faire écho dans le couloir."


"Je soupire. Maintenant qu'elle est partie, je suis seul avec ma culpabilité."



"Alors que le battement dans ma poitrine se calme, l’anxiété le remplace."


"D'une certaine façon, j'ai l'impression que tout cela reste de ma faute."


"Peu importe à quel point Rin peut être rageante, insupportable et pas possible, elle n'est pas la Rin que je pensais connaître."


"La Rin que j'espérais qu'elle soit."

"…"


"Est-ce que c'est moi qui ai causé tout ça en incitant Rin à tenter sa chance avec l'exposition ?"


n "Est-ce que je suis directement responsable de ce qu'est devenue Rin durant ces dernières semaines ?"


n "Je ne trouve pas d'explication pour son comportement bizarre, autre que l’exposition et toutes les choses qui viennent avec."


n "Peut-être que c'était la seule chose qui aurait pu nous rapprocher, mais tout ce que ça a fait a été de nous éloigner encore plus l'un de l'autre, devenant inatteignables."

play sound sfx_impact2
with vpunch


"Je me frappe fort la tête contre le mur."

play sound sfx_impact2
with vpunch

stop music fadeout 4.0


"Deux fois, pour être sûr que ça fasse mal."

scene black
with dissolve



label fr_R32:

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_traffic fadein 0.5

scene bg gallery_ext
with locationchange


"Un mal de tête bat sans cesse à l’arrière de mon crâne alors que je pousse la porte du 22nd Corner."


"À part ça, je suis parfaitement calme."

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")

window hide
nvl clear
nvl show dissolve


n "\n\nAprès avoir défoulé sur Rin toute la colère que j'avais enfouie en moi, j'ai l'impression que mon cœur a été soulagé d'un grand poids."


n "La tension qui m'a embrouillé le cerveau durant ces dernières semaines s'est évaporée sans même laisser une ombre derrière elle."


n "C'est dans un état d'apaisement presque absolu que je réalise que c'était sans doute une mauvaise idée de lui crier dessus comme ça."


n "\nJe pensais vraiment ce que j'ai dit, mais à quoi ça a servi de faire ça ? À rien."


n "Je ne suis pas comme ça. Je ne crie pas sur les gens normalement. Je ne sais pas pourquoi j'ai dit ça hier."


n "Alors je continue de me sentir vraiment coupable et veux revenir sur ce que j'ai dit."


n "\n\nRin est probablement en colère aussi. Encore plus que mon propre comportement, sa réaction m'a choqué."

nvl clear


n "\nJ'ai toujours pensé qu'elle n'était pas du genre à changer, toujours détachée de ce qui se passe autour d'elle, alors la voir si perturbée que je lui crie dessus... ça m'a fait un drôle d'effet."


n "\nJe me demande si elle comprend comment je me sens ?"


n "Dans le monde de Rin, tout semble être si clair et subjectif... clairement subjectif, comme si elle était dans l'incapacité totale de voir les choses d'un autre point de vue que le sien."


n "Mais en fin de compte, est-ce que n'importe qui peut faire ça ? Peut-être que l'objectivité et l'altruisme sont des illusions pour les gens qui aiment se penser remplis de compassion."



n "Tout comme l'art est une illusion pour les gens qui pensent que la réalité n'est qu'un tremplin pour quelque chose de plus grand."


n "Même quand tu arrêtes de penser que le monde tourne autour de toi ou que tu commences à penser plus loin que le bout de ton nez, tu ne peux pas voir plus loin que là où se portent tes yeux."


n "Peut-être que ça fait d'elle quelqu'un comme nous en fin de compte."


stop ambient fadeout 1.0

nvl clear
nvl hide dissolve

play sound sfx_storebell
$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 0.5

scene bg gallery_int
show crowd
with locationchange

window show

play music music_ease fadein 3.0


"Je franchis la porte et entre dans une galerie remplie de gens illusionnés."


"Malgré les remarques de Sae durant mes précédentes visites, j'ai toujours pensé que c'était très spacieux, mais maintenant qu'il y a beaucoup de monde ça semble vraiment petit."

show sae smile at center behind crowd
with charaenter


"Je remarque immédiatement Sae se tenant au milieu d'une discussion animée, occupée à bavarder avec quelques vieux messieurs."


"Elle est assez grande et classe, alors on la repère vite dans une foule."


"Il y a quelques dizaines de verres de vin posés sur les tables collées au mur du fond, remplis de Bordeaux. Une grande majorité des invités sirotent leurs verres."


"Les mondains et connaisseurs en art se mêlent joyeusement, échangeant leurs opinions sur le travail de Rin qui semble être une priorité secondaire pour pas mal."


"Je me sens distant, exclu des gens ici."


"Je suis loin de pouvoir prétendre être un caméléon social, alors la situation est assez frustrante."


"Puisque je ne m’intègre pas du tout dans la foule, j'essaye de faire semblant et d'avoir l'air aussi cool et à l'aise que possible."


"Je me demande comment Rin supporte tout ça. Si c'était moi, je flipperais sûrement."

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene bg gallery_exhibition
show crowd
with locationchange


"Mettant de côté mon anxiété, je continue de naviguer précautionneusement dans la foule, jetant des coups d’œil aux tableaux accrochés aux murs."

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

scene rin_exhibition_paintings
with locationchange


"L’exposition de Rin prend la moitié de la place de la galerie. Certaines peintures sont moins familières que d'autres, mais j'en reconnais la plupart."


"J'en ai vu certaines en cours de création durant les réunions du club après tout, et j'en ai vu d'autres quand Rin choisissait son portfolio."


"Je remarque que quelques peintures inachevées sont aussi accrochées au mur. Peut-être que c'est ça qu'ils appellent l'art de coïncidence ?"


"Même les échecs de Rin, si on peut appeler ça comme ça, deviennent des exemples de son talent. C'est assez paradoxal."

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene bg gallery_exhibition
show crowd
with locationchange


"Je ne la vois nulle part, ce qui est étrange, parce que même si elle est bondée, la galerie {b}est{/b} assez petite."


"C'est pas grave. Je ne sais pas comment lui faire face après hier, de toute façon. Peut-être que je n'aurais même pas dû venir."


"Mais j'ai promis à plusieurs personnes, dont Rin, que je viendrais, alors..."


"Rah, on dirait que je fais les choses parce que c'est la chose convenable à faire, pas parce que ça serait une bonne chose (ou pas) à faire."

scene bg gallery_int at right
show sae smile at center
show crowd at right
with locationchange


"Je m'approche de Sae en attendant un vide dans la conversation pour pouvoir lui parler."


"Même si sa voix est presque entièrement inaudible avec le bruit de fond général, j’entends qu'elle parle de Rin."


sa "Oui, elle est lycéenne dans une école du coin... même si elle sera diplômée l'année prochaine, je suis sûre que diverses écoles d'art seraient intéressées par..."


sa "...Je me disais que ça serait intéressant d'avoir une exposition de quelqu'un qui en est encore aux premiers stades de son développement..."


"C'est bizarre, c'est comme si Rin était un genre de mini-célébrité même si ce n'est rien de plus que l'ouverture d'une petite exposition dans une petite galerie d'art dans une petite ville."


sa "En fait, il y a un ami à moi qui..."

play sound sfx_impact
with vpunch


mystery "C'est Hisao !"


"Mon écoute est interrompue par une voix familière et une claque dans le dos. Je n'ai pas besoin de deviner la source de la voix, ou même de me tourner pour savoir qui c'est."


hi "Salut Emi."

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

show emicas invis:
    center
    xpos 0.15
with None

show bg gallery_int at left
show sae invis:
    xpos 0.75
show crowd at left
show emicas happy at center
with dissolvecharamove

hide sae
with None


emi "Salut ! Tu es là comme un représentant du club d'art ou un truc du genre ? Je ne vois personne d'autre de l'école ici..."


hi "Hum... Je ne sais pas. Ça doit être le cas si je suis le seul."


hi "Et toi ?"

show emicas neutral
with charachange


emi "Ben quoi moi ?"


hi "Euh..."

show emicas angry_up
with charachange


emi "Tu ne penses pas que je suis intéressée par l'art ? C'est ça, Hisao ?"


hi "Non, ce n'est pas ce que j'ai... bon, peut-être un peu, si tu dis ça comme ça."


hi "Je veux dire, même si tu traînes avec Rin, je ne t’ai jamais entendue parler d'art avec elle alors..."

show emicas awayfrown_up
with charachange


"Emi souffle et tourne la tête, semblant mécontente."

show emicas closedsmile
with charachange


emi "C'est vrai, je ne comprends pas du tout, mais elle est venue à ma rencontre d’athlétisme, alors il est normal que je lui retourne la faveur."

show emicas wink_close
with characlose


"Elle s'approche, essayant de donner un air confidentiel à la conversation, mais arrive seulement à avoir l'air suspecte."


emi "Est-ce que tu {b}comprends{/b} l'art ?"


hi "Non. Non, je ne comprends pas."


hi "Du tout."

show emicas closedsmile_close
with charachange


"Mon mouvement de tête pour accentuer mes paroles déclenche un rire et un mouvement de tête de la part d'Emi."

show emicas happy_close
with charachange


emi "Moi non plus !"

show emicas wink_close
with charachange


emi "Hé, allons parler avec Rin ! Je parie que tu ne l'as pas encore fait, parce que je ne l'ai pas fait non plus."

show emicas happy_up_close
with charachange


emi "Allez !"

show nomiya invis behind emicas:
    center
    xpos 0.8
show rin invis:
    center
    xpos 1.1
with None


show bg gallery_int at center
show crowd at center
show emicas neutral_close:
    xpos 0.15
show nomiya smile:
    xpos 0.55
show rin basic_awayabsent:
    xpos 0.85
with dissolvecharamove


"Avant qu'elle ait une chance de me traîner de force jusqu’à Rin, Nomiya apparaît derrière elle avec Rin sur les talons."


"Elle n'est pas habillée pour l'occasion, ayant opté plutôt pour l'uniforme habituel et la coiffure en bataille."


"Peut-être que son look naturel est celui qui lui va le mieux."

show emicas happy_close
with charachange


emi "Bonjour monsieur ! Bonjour Rin !"


"Loin d'être perturbée, Emi salue joyeusement notre professeur, à la suite de quoi il se retourne et la regarde, confus."

show nomiya frown
with charachange


no "Qui es-tu ?"

show emicas frown_up_close
with charachange


emi "Je suis Emi, de l'école, classe 3-4. Vous ne vous rappelez pas ?"


"Elle semble comme choquée qu'il puisse y avoir une personne qui ne la connaît pas."

show nomiya talk
with charachange


no "Oh, désolé. Tu es dans la même classe que Tezuka, non ?"

show emicas wink_close
with charachange


emi "Ouais !"

show nomiya smile
with charachange


no "Il va falloir m'excuser, j'ai du mal à retenir les étudiants qui ne font pas de l'art."

show emicas closedsmile_up_close
with charachange


emi "Pas grave, pas grave !"

show emicas happy_close
with charachange


emi "Salut Rin !"

show rin basic_deadpan
with charachange


rin "Bonjour."

show emicas happy_up_close
with charachange


emi "Félicitations pour ton truc d'art super cool ! Je suis sûre que tu seras une star !"


"Elle lève les bras en l'air pour démontrer ce qu'elle dit, me frappant presque au visage."

show emicas wink_up_close
with charachange


emi "Et regarde, Hisao aussi est venu !"

show rin relaxed_nonchalant
with charachange


"Rin ne me regarde pas, et ne me salue pas non plus."


hi "Félicitations, Rin."


"Elle continue de détourner le regard, regardant ses sandales."

show emicas closedsmile_close
with charachange


"Inconsciente de la tension entre nous et ignorant ce qui est arrivé hier, Emi continue de blablater de tout et de rien face à une Rin qui ne répond pas."


"J'imagine qu'elle est habituée à ce qu'elle ne dise pas grand-chose."

stop music fadeout 5.0
$ renpy.music.set_volume(1.0, 3.0, channel="ambient")



show sae invis behind rin:
    center
    xpos 1.25

with None

show bg gallery_int at right
show crowd at right
show emicas invis:
    xpos -0.35
show nomiya smile:
    xpos 0.25
show rin relaxed_nonchalant:
    xpos 0.55
show sae neutral:
    xpos 0.8
with dissolvecharamove

hide emicas
with None


"Peu après, Nomiya et Sae se tournent vers Rin, la présentant à des invités."


"M'y attendant, je remarque la seconde de confusion quand ils voient ses bras."

show sae smile
with charachange


"Sae est heureusement sur le coup et présente brièvement notre école."


"Les visages confus se changent en curieux."


"Homme" "Tu voudrais bien nous dire quelque chose sur ton art ?"


"Homme" "Je me disais que l'évolution est facile à remarquer, qu'est-ce que tu penses des différences entre les anciennes et les plus récentes œuvres ?"


"Homme" "C'est assez rare pour quelqu'un d'aussi jeune que toi de faire de l'abstraction."


"Femme" "Ça aurait été intéressant de te voir travailler."


"Homme" "Oh, clairement ! J'imagine que tu utilises ton pied ? Ça a dû être difficile d'apprendre, tu devrais être fière."

show rin basic_surprised
with charachange


rin "Je... euh..."

play music music_rain fadein 8.0


"Homme" "Tu poursuivras une carrière d'artiste après l'école ?"


"Elle est bombardée avec tellement de questions qu'elle ne peut pas espérer pouvoir répondre à chacune d'elles."


"Peut-être que ce n'est pas une mauvaise chose, Rin a tendance à dire n'importe quoi assez fréquemment."


"Homme" "D’où est-ce que tu sors tes idées ?"

show rin relaxed_boredom
with charachange


rin "C'est la quatrième, je veux dire la cinquième pire..."


"Rin continue de marmonner, semblant de plus en plus vexée par les demandes incessantes."

show rin negative_annoyed
with charachange

rin "Ah…"


"Tout le monde attend qu'elle dise quelque chose, mais on dirait qu'elle a donné sa langue au chat."


"Chaque question ne fait qu'ajouter à sa détresse."

show rin basic_sad
with charachange


"Je n'entends pas la question qui est celle de trop."


"C'est comme un moteur qui cale."

show rin basic_sad:
    1.2
    parallel:
        easeout 0.5 ypos 1.2
    parallel:
        "rin basic_lucid" with Dissolve(0.3, alpha=True)
with Pause(1.5)

stop ambient fadeout 7.0

scene ev rin_gallery:
    truecenter
    zoom 0.9 subpixel True
    easein 30.0 zoom 1.0
with Dissolve(0.2)
play sound sfx_pillow
with vpunch


"Rin s'immobilise pendant une longue, longue seconde jusqu’à tomber à genoux, s'effondrant sur le sol sans aucune grâce, comme un sac de patates."



"Femme" "Tu vas bien ?"


rin "Je ne sais pas..."


no "Tezuka ? Qu'est-ce qui ne va pas, ma fille ?"


rin "Je ne sais pas ce qui va pas..."


"Un horrible silence s'abat sur les gens autour de Rin."


"Tout le monde est pétrifié, ne sachant pas comment réagir à sa soudaine... crise."


"Elle respire avec de profonds et tremblants soupirs comme si elle manquait d'air, regardant devant elle avec un regard vide."

play sound sfx_rustling
stop music fadeout 1.0

scene bg gallery_int at right
show crowd at right
show nomiya serious:
    center
    xpos 0.25
show rin negative_sad_close:
    center
    xpos 0.55 ypos 1.2
    ease 0.8 ypos 1.0
show sae scowl:
    center
    xpos 0.8
with locationchange


"Voyant que personne ne fait rien, je me force à marcher jusqu’à Rin et la relève, la laissant s'appuyer sur moi pour tenir debout."


hi "Tu veux prendre l'air ? D'accord, viens dehors un moment."


"Je n'attends même pas qu'elle me réponde avant d'attraper son épaule et de la faire traverser le mur constitué de Nomiya, Sae, Emi, et des invités."


hi "Excusez-nous."

play sound sfx_storebell
$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_traffic fadein 1.0

scene bg gallery_ext
with locationchange


"L'air frais du soir me balaye le visage alors que je passe la porte."

show rin negative_sad_close_ni at center
with charaenter


"Je lâche Rin et elle s'adosse contre le mur en pierre, essayant de retrouver son souffle."


hi "Tu vas bien ?"

show rin negative_confused_close_ni
with charachange


rin "Je ne pouvais rien dire..."


"Rin ne me regarde toujours pas, alors je détourne les yeux également."

play music music_dreamy fadein 4.0


"Les lampadaires et néons colorés déforment ma vision jusqu’à me rendre presque aveugle, me forçant à tourner la tête."


"Au moins elle parle, même si ce n'est pas à moi."


hi "Qu'est-ce que tu voulais dire ?"


"Peut-être que nous pouvons tous les deux imaginer parler à un ami invisible."

show rin basic_sad_close_ni
with charachange


rin "Je ne sais pas."

show rin negative_sad_close_ni
with charachange


rin "Quelque chose qui aurait voulu dire quelque chose."

"…"


"Le silence dure un long moment."


"Je ne me sens pas à l'aise en étant seul avec Rin. Je ne suis pas doué pour imaginer que les choses qui n'existent pas existent... ou que les choses qui existent n'existent pas."


hi "On devrait y retourner."


hi "Les invités de Sae sont là, ils veulent probablement te rencontrer et te parler."


hi "Tu sais, te poser des questions et tout. À propos de ces peintures sur lesquelles tu as tant travaillé."

show rin negative_angry_close_ni
with charachange


rin "Je ne veux pas qu'ils posent de questions comme ça. Je ne peux jamais dire les bonnes choses."


hi "Qu'est-ce que tu veux alors ?"

"…"

show rin relaxed_doubt_close_ni
with charachange


label fr_choiceR32:
menu:
    with menueffect
    rin "Que quelqu'un n'ait pas à me poser de questions."
    "T'es pas contente que les gens s’intéressent à tes peintures ?":





        return m1
    "Et qu'est-ce que tu feras si tu trouves quelqu'un comme ça ?":


        return m2

label fr_R32a:

$ renpy.music.set_volume(0.2, 0.2, channel="ambient")


hi "Mais tu n'es pas contente que les gens s’intéressent à tes peintures ?"


hi "Je veux dire, ce n'est pas pour ça que tu as fait ton exposition et tout ?"


hi "Bien sûr qu'ils vont te poser des questions, s'ils pensent que c'est intéressant."

show rin negative_annoyed_close_ni
with charachange


rin "C'est comme avoir un lever de soleil deux fois de suite quand tu veux te baigner nu au clair de lune."

show rin negative_angry_close_ni
with charachange


rin "C'est bien, mais..."


"...c'est pas suffisant, je complète sa phrase pour elle, même si je ne comprends pas totalement sa métaphore."


hi "Je ne comprends pas."


hi "Tu devrais essayer de te réjouir. C'est ta soirée, après tout."


hi "Toutes ces personnes sont là pour voir tes peintures. Je trouve que c'est génial."


"J’attends qu'elle dise quelque chose, que ce soit pour ou contre, mais Rin continue de broyer du noir."


"Elle ne veut pas répondre à mes questions, ou m'expliquer ce qui ne va pas."


"Si elle avait quelque chose à dire, ses mots ne sont pas prononcés."


"Les mots qu'elle ne peut pas dire."


"Je frissonne à cause du vend froid qui souffle dans les rues, et son bruit comble le silence."


hi "On devrait y retourner."


hi "Tout le monde est inquiet."

stop ambient fadeout 0.5
play sound sfx_storebell

scene bg gallery_int
show crowd
show nomiya talk at twoleft
show sae neutral at tworight
with locationchange

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0


no "Ah, te voilà ! Tu te sens mieux ? Il peut faire assez chaud ici, tu peux être prise d'un vertige en un rien de temps."

show nomiya veryhappy
with charachange


"Il rit fortement, presque odieusement."

show nomiya talk
with charachange


no "Tu devrais boire quelque chose si tu te sens faible, Tezuka."

show nomiya talk:
    center
    xpos 0.25
show sae neutral:
    center
    xpos 0.8
with charamove

show rin basic_lucid:
    center
    xpos 0.55
with charaenter


"Rin hoche faiblement la tête, mais ça semble être suffisant pour convaincre Nomiya qu'elle va bien."


"Il pousse un peu Rin en avant pour la présenter à la personne avec qui il discutait."

show nomiya smile
with charachange


no "Donc, à propos de ce que nous disions auparavant..."


"Homme" "Ah oui, je suis très excité de rencontrer..."

stop music fadeout 8.0


"Je suis éjecté de la conversation, et le bruit de fond de dizaines d'autres discussions remplissent mes oreilles en un bourdonnement indistinct."


"Même Emi a disparu quelque part."


"Se tenir au milieu de la foule provoque chez moi un sentiment de solitude étonnant."


"Tout le monde ici, pas uniquement Rin, semble faire partie de quelque chose dont je ne fais pas partie."


"Je suis content pour elle, vraiment, mais ça me donne l'impression de n'avoir rien accompli."


"Rin est la preuve vivante du potentiel d'un être humain. Elle a surmonté son handicap, en a même fait une force."

stop ambient fadeout 4.0


"Elle devrait être heureuse."


"Quel est mon potentiel ?"


"Rin a été aussi loin, mais jusqu’où je peux aller moi ?"

scene black
with dissolve


label fr_R32b:

$ renpy.music.set_volume(0.2, 0.2, channel="ambient")


hi "Et qu'est-ce que tu feras si tu trouves quelqu'un comme ça ?"


hi "Tu penses vraiment que ça serait l'apogée de l'amour à l'infini, amants maudits et heureux pour toujours ?"

show rin basic_absent_close_ni
with charachange


"Ma question se confronte à un regard vide, aux ténèbres dans ses yeux opaques face à l'aigreur de mes paroles."

show rin negative_worried_close_ni
with charachange


rin "Non, je ne pense pas ça."

show rin negative_annoyed_close_ni
with charachange


rin "Mais au moins je ne serais plus toute seule."


"Elle murmure ses paroles aux lumières de la ville mais je les entends quand même."

show rin negative_sad_close_ni
with charachange


rin "Je n'aurais pas dû faire ça. Pas encore."


hi "L'exposition ?"

show rin basic_lucid_close_ni
with charachange


"Elle hoche la tête et ferme les yeux, respirant calmement comme pour prouver qu'elle le peut, puis continue de parler toute seule."


hi "Pourquoi ? Mauvais alignement des planètes ?"

show rin basic_sad_close_ni
with charachange


rin "Non, pas ça. J'ai vérifié deux fois, et je me suis levée du pied droit, je veux dire gauche, et j'ai fait tout le reste gauche, je veux dire droit."

show rin negative_sad_close_ni
with charachange


rin "C'est moi."

show rin negative_worried_close_ni
with charachange


rin "J'avais tort."

hide rin
with charaexit


"Elle se relève et s’étire avant de passer à côté de moi dans la rue."


hi "Attends, où est-ce qu'on va ?"

show rin basic_absent_ni
with charaenter


"Elle s’arrête et se tourne, me regardant d'un air interrogateur."

show rin basic_awayabsent_ni
with charachange


rin "À l'école. Je pars."


hi "Quoi... pourquoi ?"

show rin basic_absent_ni
with charachange


rin "Parce que je veux être moi."

$ renpy.music.set_volume(0.4, 1.0, channel="ambient")

hide rin
with charaexit


"Rin part, me laissant derrière, complètement confus."


hi "Rin !"


"Mais... quelque chose qu'elle a dit m'a vraiment touché, ou peut-être que c'était juste la façon dont elle l'a dit."


"Peut-être que c'était le fait {b}qu'elle{/b} l'ait dit."


"Je veux lui dire quelque chose à mon tour, avant que j'oublie ce sentiment."


"Comme pour réaliser mon souhait, Rin s’arrête. Elle ne se tourne pas, continue juste d'attendre que je dise ce que je veux dire, même si je n'ai pas eu le temps de penser à ce que..."


hi "Rin... écoute. Je... je ne ne pense pas que tu aies besoin d'être seule, même si tu n'as pas rencontré quelqu'un comme ça."


"Je ne sais pas si elle a entendu ce que j'ai dit, mais dans tous les cas, elle ne réagit pas."


"Pour la dernière fois, elle recommence à marcher et s’éloigne de la galerie."

play sound sfx_storebell

stop ambient fadeout 0.5

scene bg gallery_int
show crowd at center
show nomiya frown at twoleft
show sae doubt at tworight
with locationchange

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0


no "Donc ? Où est Tezuka ?"


"Je me contente de secouer la tête, mais puisque ça ne semble pas être une réponse suffisante, j'ouvre la bouche."


hi "Elle a fui."

show nomiya stern
with charachange


no "Quoi ?"


"La terrible prise de conscience se répand sur son visage comme une traînée de poudre."

show nomiya serious
with charachange


no "C'est un fiasco ! Une catastrophe !"


no "Qu'est-ce qu'elle pensait, c'est l’événement le plus important de sa vie, et elle s'enfuit ?"

show nomiya stern
with charachange


no "Et toi ! Pourquoi ne l'as-tu pas arrêtée ? Je vais te tenir personnellement responsable..."

show sae neutral
with charachange


"Sae l’interrompt, les mains calmement levées."


"C'est bien qu'elle soit intervenue, le professeur commençait à attirer l'attention de quelques invités."

show sae smile
with charachange


sa "Shinichi, du calme. Elle a sûrement eu le trac et a paniqué. Je ne la connais pas aussi bien que vous, mais j'ai compris qu'elle est quelque peu particulière."


sa "Ce genre de chose arrive."

show sae neutral
with charachange


sa "Ça ira. J'expliquerai qu'elle est soudainement tombée malade. Les invités comprendront sûrement."

show nomiya frown
with charachange


no "Mais..."

show sae smile
with charachange


sa "Regarde autour de toi, tout le monde semble être content de boire son vin gratuit et de bavarder."

show nomiya serious
with charachange


no "Ça ira pour les invités, mais on loupe des opportunités là ! Entrer dans le réseau, établir des contacts et faire connaissance !"

show emicas invis_close:
    center
    xpos -0.35
with None

show bg gallery_int at left
show crowd at left
show nomiya serious:
    xpos 0.5
show sae smile:
    xpos 0.9
show emicas frown_close:
    xpos 0.15
with dissolvecharamove


"Alors que les adultes continuent de discuter à propos de quelque chose auquel on ne peut rien, Emi tire sur ma manche pour avoir mon attention."


"Elle ne semble pas très contente non plus."

show emicas awayfrown_close
with charachange


emi "Allez."


hi "Quoi ?"

show emicas frown_up_close
with charachange


emi "On va trouver Rin et lui botter les fesses."


hi "Quoi ?"

show emicas angry_close
with charachange


emi "Je n'arrive pas à le croire, elle est si stupide !"


emi "Cette Rin, comment est-ce qu'elle peut faire ça ? Je te le dis, elle n'a pas un gramme de bon sens dans la tête !"


"Emi est sérieusement en colère, il manque juste la fumée sortant de ses oreilles."


"Je crois que je comprends Emi, elle est {b}ce{/b} genre de personne."


"“Abandonner” n'a jamais fait partie de son vocabulaire, et peut-être qu'elle ressent que ça ne devrait faire partie du vocabulaire de personne."


hi "C'est sûrement mieux de la laisser seule ce soir."

show emicas angry_up_close
with charachange


emi "Quoi ? Tu es un expert de Rin maintenant ?"


"Elle se raidit et met ses mains sur ses hanches."


"On dirait qu'elle a envie de se battre avec moi."


hi "Non, je ne pense pas que ce soit possible de toute façon."


hi "Je ne pense juste pas que lui botter les fesses soit une bonne idée."

show emicas frown_close
with charachange


"Ma remarque fonctionne étonnamment, puisque Emi baisse un peu les épaules et soupire."


emi "Je sais."


hi "Ah bon ?"

stop music fadeout 2.0

show emicas awayfrown_close
with charachange


emi "La dernière fois que je l'ai fait, ça n'a rien changé."

stop ambient fadeout 1.0

scene ev busride_ni
with locationskip

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")
play ambient sfx_businterior fadein 2.0


"Le retour à l'école dans le bus vide se fait en silence."


"Nous regardons tous les deux les lumières clignoter devant les fenêtres sans dire un mot."

stop ambient fadeout 1.0

scene bg school_dormext_full_ni
with locationskip

play music music_soothing fadein 0.5


"Les terrains sont calmes de nuit, baignés par la pâle lumière de la lune et des lampadaires jaunes."


"Nous nous souhaitons bonne nuit devant le dortoir."

show emicas awayfrown_up_ni at center
with charaenter


"Emi, se craquant les phalanges par réflexe, m'assure qu'elle n'agressera pas Rin dès que j'aurai tourné le regard."


hi "Tu me promets que tu ne la gronderas pas ?"

show emicas angry_up_ni
with charachange


"Elle relève les yeux, le regard encore flamboyant de colère que je contrecarre avec le mien, aussi calme que possible."


"C'est facile de faire face à une femme en colère seulement quand on n'est pas l'objet de cette colère."


"Après une minute de combat du regard, elle soupire et secoue la tête, défaite."

show emicas closedsmile_ni
with charachange


emi "Tu es trop gentil, Hisao."

show emicas weaksmile_ni
with charachange


emi "Tu le savais ça ?"


"Des bribes de sourire s'affichent au coin de sa bouche alors qu'elle dit ça, et elle semble bien plus relaxée."


"Quel soudain changement d'humeur."


"Peut-être qu'elle n'était pas aussi en colère qu'on l'aurait dit."


"Peut-être qu'elle est d'humeur changeante."


hi "Si je l'étais, je te laisserais faire."

show emicas wink_ni
with charachange


emi "Est-ce que ça veut dire que tu n'es gentil qu'avec Rin ?"


"Nous cachons tous les deux nos préoccupations derrière des blagues, mais au moins ça me met de bonne humeur."


"Emi fronce les sourcils avec un sourire à moitié amusé, essayant de me pousser dans mes retranchements. Ça ne se passera pas comme ça."


hi "Non, ça veut juste dire que je ne suis pas gentil avec toi."

show emicas angry_up_ni
with charachange


emi "HÉ !"

stop music fadeout 2.0


hi "Bonne nuit, Emi."

scene black
with dissolve


label fr_R33:

play music music_daily fadein 0.5

scene bg school_scienceroom
with locationchange


"Le dernier jour avant les vacances d'été se passe lentement."


"La science est l'examen final du trimestre et nous sommes libres."


"L'aspiration collective pour la liberté est presque palpable dans la classe, même si le temps est quelque peu nuageux."


"Il pleuvra peut-être aujourd'hui, qui sait."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene ev rin_doodle
with locationchange


"J'ai déjà fini le test parce qu'il était assez facile, alors je gribouille paresseusement au dos de la feuille, attendant que Mutou m'appelle."


"Ça empêche aussi Misha d'essayer de copier discrètement par-dessus mon épaule."


"Elle arrive peut-être à tromper le professeur inattentif, mais je sais ce qu'elle fait."


"Je pense que c'est sa meilleure chance de réussir le test. Je ne ressens aucune pitié cela dit, alors je l'ignore et regarde autour de moi."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

scene bg school_scienceroom
with locationskip


"C'est calme."


"Les seuls bruits dans la salle de classe sont les bruissements de papier et la toux constante de Mutou."


"Ma conscience glisse doucement et je me mets à divaguer, oubliant le calme de la pièce."






label fr_R34:
scene bg school_scienceroom
with None

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve


n "\nVacances, hein ?"


n "Certaines personnes vont rester à l'école même pendant les vacances, pendant que d'autres retourneront dans leur famille."


n "Je ne sais pas quoi faire. je devrais aller acheter un billet de train pour retourner chez moi, mais je n'arrive pas à m'y résoudre."


n "Je suis sûr que je vais avoir de nouveau un appel de la maison. Maman va encore pester pour savoir quand je reviens, et je ne vais pas savoir quoi lui dire."


n "\nC'est vraiment gênant. Dans l'état actuel des choses avec Rin, j'ai l'impression que je ne peux pas juste m'en aller et prétendre que tout va bien."


n "\nEt aussi, elle a ses propres problèmes. Je pensais que le vernissage de l'exposition lui donnerait un nouveau souffle, mais je me suis complètement trompé."


n "\n\nLe nœud ne semble que se resserrer."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

play sound sfx_doorknock

window show


"Quelqu'un frappant à la porte interrompt l'ambiance calme mais frénétique des 15 dernières minutes de l'examen."

show muto normal at center
with charaenter

$ renpy.music.set_volume(0.2, 0.0, channel="sound")


mu "Entrez."

stop music fadeout 1.0
$ renpy.music.set_volume(1.0, 8.0, channel="sound")
play sound sfx_footsteps_hard

show bg school_scienceroom at bgleft
show muto normal at twoleft
with charamove

show nomiya serious at tworight
with charaenter


"L'ouverture de la porte révèle le professeur d'art, qui rentre dans la classe avec sa veste ondulant autour de lui comme dans une bourrasque."


"Il regarde Mutou, qui le regarde."

play music music_tension

show muto irritated
show nomiya stern
with charachange


"Un froncement de sourcils s'affiche en simultané sur leurs deux visages alors que les hommes se jaugent du regard."


no "Excusez-moi, pourrais-je emprunter M. Nakai pour un moment ?"


mu "Excusez-{b}moi{/b}, M. Nomiya, mais nous sommes au milieu d'un examen là."


"Une ambiance froide se répand dans la classe alors que deux hommes se fixent mutuellement du regard."

show nomiya serious
with charachange


no "C'est urgent, et on dirait que Nakai a déjà fini."


"Les deux hommes se tournent vers moi, me regardant comme deux basilics essayant de pétrifier une proie alléchante."


"Il est vrai que j’attends depuis un bon moment maintenant, alors Nomiya a raison, mais..."

show muto normal
with charachange


mu "Nakai, tu veux te relire encore une fois ?"


"Mutou parle avec une étrange intonation, pesant certains mots comme pour essayer de m'envoyer un message."


"La pression de leurs regards fait que je hoche rapidement la tête, ce qui apparemment est considéré comme une réponse."

stop music fadeout 6.0

show muto irritated
with charachange


mu "Très bien. Nakai, va avec M. Nomiya, s'il te plaît."


mu "Prends ton sac avec toi et pose ta feuille sur mon bureau."

show muto smile
with charachange


mu "Passe de bonnes vacances."


hi "Hum. Euh, vous aussi, monsieur."


"Le monde entier... enfin, au moins la salle de classe semble retenir son souffle pour moi, gardant l'examen en attente jusqu’à ce que je me lève, rassemble mes affaires et sorte de la salle."


"Je peux sentir les regards dans mon dos. Mes camarades de classe se demandent sûrement si je suis collé ou quelque chose du genre, pour être emmené comme ça le dernier jour avant les vacances d'été."


"Je ne sais pas ce que me veut le professeur, mais je ne dois pas être collé et ça a sûrement quelque chose à voir avec Rin."

scene bg school_hallway3
with locationchange

play sound sfx_doorslam
with vpunch


"Nomiya ne m’emmène nulle part, se contentant de me parler dans le couloir vide."

show nomiya serious at center
with charaenter

play music music_pearly fadein 1.0


no "Tu sais où est Tezuka ?"


"Donc elle essaye d’éviter le professeur..."


"Je me demande si elle réalise qu'elle ne peut pas faire ça indéfiniment."


hi "Aucune idée."


hi "Vous avez sûrement déjà demandé à sa classe à côté."

show nomiya stern
with charachange


no "Bien sûr ! J'ai cherché dans tous les recoins de cette fichue école et du dortoir pour filles."


no "Tu es le dernier à l'avoir vue depuis hier et tu es son ami."

show nomiya serious
with charachange


no "Sois avec moi là-dessus. Tu n'es pas inquiet ?"


"Je le suis, mais je ne sais pas ce que je peux faire."


"Rin a fait quelque chose d’incompréhensible hier, même pour elle."


"Elle semblait vraiment confuse."


hi "Peut-être qu'elle veut juste du temps pour réfléchir. J'ai le sentiment qu'elle avait des doutes au sujet de cette exposition."


"Ou un truc du genre. Elle ne m'a pas vraiment expliqué ce qui n'allait pas."

show nomiya frown
with charachange


no "Quels doutes ?"


hi "Je sais pas. Je l'ai juste ressenti comme ça."


"Je suis un peu malhonnête avec le professeur, mais je ne devrais pas me mêler de ça."


"Il est venu à moi... oui, pourquoi ? Peut-être qu'il pense que je suis une sorte de confident pour Rin, mais je ne pense pas pouvoir aider à ce sujet."

show nomiya serious
with charachange


"Le professeur souffle et se gratte la tête, confus."


no "C'est quoi son problème ? Elle n'a jamais été comme ça, elle a toujours été sérieuse et directe."


"“Sérieuse et directe ?” Ce ne sont pas les mots que j'aurais utilisés pour décrire Rin."


"Pour moi, elle est obsessionnelle au mieux."


hi "Euh, je ne veux pas être impoli, mais ce n'est pas vous qui avez poussé Rin à faire ça en premier lieu ?"

show nomiya dreamy
with charachange


no "Son but est mon but. C'est le travail d'un mentor."


hi "J'imagine. Je ne sais juste pas si peindre la rend heureuse."

show nomiya stern
with charachange


no "C'est assez ridicule de ta part de dire ça, Nakai."


"Il semble soudainement plutôt en colère. J'ai dit quelque chose de stupide ?"

show nomiya serious
with charachange


no "Tu ne comprends pas, hein ? Ce n'est pas une question de bonheur. Pour chaque gain il y a un sacrifice à faire."

show nomiya stern
with charachange


no "On n'a rien sans rien, mais comment pourrais-je... laisser cette fille gâcher son talent si elle a un moment de doute ? Hors de question !"


no "La peinture est un travail comme un autre. Tezuka peut donner l'impression que c'est un jeu d'enfant, mais elle travaille dur chaque jour pour faire son art."


no "Pour devenir extraordinaire, il faut fournir des efforts extraordinaires."


"Plus le professeur parle, plus j'ai l'impression que Rin ne pense pas comme ça, même si je n'ai aucune idée de comment elle pense."

show nomiya serious
with charachange


no "Je peux tout à fait comprendre pourquoi elle sacrifierait ses vacances d'été pour rattraper les cours loupés et les examens et aussi pour avoir une chance de montrer son art."


no "C'est le chemin qu'elle a pris, et ce n'est pas facile d'aller jusqu'au bout."


no "Je sais qu'elle est jeune, et la vie a été dure avec elle comme avec tous les enfants de cette école, mais ce n'est pas une excuse."


"Il a fini."


hi "Mais—"

show nomiya smile
with charachange


no "Tu as quelque chose, toi, comme Tezuka a son art ?"


hi "Non..."


"C'est vrai. J'ai seulement une vague idée de mon avenir, pas de but auquel m'atteler, pas de rêve vers lequel me diriger."


"J'ai rejoint le club d'art à la recherche de quelque chose qui pourrait m’intéresser, m'inspirer."


"Est-ce que j'ai trouvé quelque chose comme ça ?"


"Tout ce que j'ai trouvé en fin de compte... c'était Rin."


hi "Non, je n'ai pas de passion comme ça."

show nomiya serious
with charachange


no "Alors tu ne peux pas comprendre."


"Sa phrase s'abat d'un coup, rien ne pouvant être dit pour le contredire."


hi "Mais... elle ne se comprend peut-être pas elle-même."


"Pourtant, je continue d'argumenter, par principe plus qu'autre chose."

show nomiya stern
with charachange


no "Comment pourrait-elle ne pas comprendre ? Elle a travaillé si dur ces dernières semaines qu'elle a arrêté de rentrer à l'école, sans même parler d'aller en cours. Ne sois pas ridicule."


"Je ne pense pas être ridicule, mais puisque je n'ai rien à répondre à ça, Nomiya semble considérer ça comme une victoire."

show nomiya smile
with charachange


no "Dans tous les cas, le vernissage de l'expo était un succès malgré la courte présence de Tezuka."


no "Beaucoup de personnes étaient intéressées par son travail et une œuvre a même été vendue pour un prix raisonnable."


hi "C'est bien non ?"

show nomiya veryhappy
with charachange


no "Oui, c'est fantastique ! J'avais espéré que Tezuka reprenne ses esprits après avoir entendu ça, mais..."


"Il soupire et retire ses lunettes, les nettoie avec le bord de sa veste avant de les remettre sur son nez."

show nomiya smile
with charachange


no "Dans tous les cas, je devrais y aller. Il y a ce bazar à régler avec Sae et les autres."


no "Si tu vois Tezuka, demande-lui de venir me voir s'il te plaît. Sinon, passe de bonnes vacances."


hi "Merci..."

stop music fadeout 6.0
play sound sfx_footsteps_hard
$ renpy.music.set_volume(0.0, 4.0, channel="sound")

hide nomiya
with charaexit


"Après qu'il ait disparu au tournant, je me demande où pourrait vraiment être Rin."


"Je suis sûr qu'elle n'a pas un, mais au moins une demi-douzaine de ces “endroits secrets”."


"Je suis partagé entre le désir de résoudre tout ça ou d'abandonner pour de bon."


"La classe abandonnée est seulement à quelques pas de là."


"Que faire ?"

"…"

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_dooropen

scene bg school_room34
with locationchange


"Alors que j'ouvre la porte, seules les ombres m’accueillent de l'intérieur."


hi "Salut toi."



label fr_R35:

scene bg school_scienceroom
with None

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve


n "\n\nVacances, hein ?"


n "Certaines personnes vont rester à l'école même pendant les vacances, pendant que d'autres retourneront dans leur famille."


n "Je devrais probablement retourner à la maison et montrer à mes parents que je suis toujours en vie."


n "\nPas grand-chose à faire à l'école de toute façon."


n "Le prochain trimestre sera stressant. Tout le monde devra penser sérieusement à ce qu'il fera après le diplôme."


n "\n\nCe qui m'inclut..."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

scene ev rin_doodle_all
with silentwhiteout

window show


"Un regard à mes griffonnages me convainc d’arrêter d'insister. C'est un bazar de lignes sans vie, un gâchis de papier si ce n'était pas le dos de ma feuille d'examen."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve


n "\n\n\nPeut-être que c'est parce que je ne m'étais pas décidé à dessiner quelque chose de précis."


n "Je voulais juste passer le temps, alors le dessin s'est fait comme je suis."


n "Sans but précis."


n "\n\nÇa serait plus facile si j'avais un talent spécial, comme Rin."


n "C'est facile pour elle."


n "Ça me rend jaloux."


n "Ça m’énerve qu'elle ne semble pas heureuse de ça."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

scene bg school_scienceroom
show muto smile at center
with locationskip

window show


mu "Eeeeeet... stop !"


"L'annonce par Mutou de la fin de l'examen extirpe des grognements de mécontentement de la part de la moitié de la classe."


"Je ne leur en veux pas, l'examen était assez difficile."


"Mutou attend beaucoup de notre classe, même s'il n'est pas strict du tout. Je pense qu'il aimerait bien qu'on devienne tous des scientifiques."

show muto normal
with charachange


mu "Posez vos crayons et retournez vos feuilles s'il vous plaît."


"La plus grande plainte vient du bureau à côté du mien."

show misha invis_close:
    center
    xpos -0.2
    ypos 1.13
with None

show bg school_scienceroom at bgright
show muto normal at tworight
show misha perky_sad_close:
    xpos 0.15
with dissolvecharamove


"Le désespoir de Misha est presque palpable."


"L'aura ténébreuse du dernier espoir émanant d'elle me terrorise et me donne envie de la plaindre en même temps."

show muto smile
with charachange


mu "Et maintenant, il devrait y avoir vie de classe avant de vous libérer, mais j'ai seulement quelques annonces à faire alors ça devrait aller vite..."


"Ses annonces ne sont jamais importantes, alors je l'écoute d'une oreille."


"Misha semble être trop déprimée pour prétendre écouter."


"Elle pose sa tête sur la table, semblant défaite."


hi "Réjouis-toi, Misha."


hi "C'est les vacances ! Ne t’inquiète pas pour le test."

show misha sign_smile_close
with charachange


mi "Merci, Hicchan."


"Son froncement de sourcils devient un petit sourire, et une étincelle d'excitation s'allume dans ses yeux."

show misha perky_smile_close
with charachange


mi "Qu'est-ce que tu vas faire durant les vacances d'été, Hicchan ?"

show misha hips_smile_close
with charachange


mi "Moi je vais à la maison de Shicchan, ils ont genre un super cool manoir génial ! Je suis trop excitée~ !"

show misha hips_grin_close
with charachange


mi "Je suis sûre que ça sera les meilleures vacances du monde entier~ !"


"Elle semble avoit tout oublié de son désespoir en quelques secondes et bondit, assise sur sa chaise, comme si elle gonflait son excitation."


hi "Je n'ai pas vraiment quelque chose de prévu..."

show misha sign_smile_close
with charachange


mi "Ah bon~ ? Peut-être que tu devrais—"

show misha perky_confused_close
with charachange


"Un doigt tapotant sur l'épaule de Misha détourne son attention."

show muto irritated
with charachange


"Shizune pointe Mutou du doigt, qui les regarde toutes les deux, dans l'expectative."

show misha sign_confused_close
with charachange


mi "Oups ! Désolée, Shicchan, je n'avais pas remarqué que le professeur avait déjà fini, haha~."


"Elle se racle la gorge et prend une grande inspiration..."

show misha hips_grin_close:
    ypos 1.0
with dissolvecharamove


mi "Debout !"


"Je me lève avec tout le monde."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve


n "\n\nDepuis que je suis là, je me suis toujours demandé quelque chose."


n "Qu'est-ce que pensent les élèves en fauteuil roulant de cette routine journalière, mis à part le fait qu'ils sont incapable de la faire “correctement” ?"


n "Est-ce un manque de considération de continuer à avoir cette tradition qui gêne tant de monde dans un endroit comme celui-ci ?"


n "Même si je n'ai jamais demandé à qui que ce soit, durant ces semaines où j'ai été là, j'en suis venu à la conclusion qu'ils ne se sentent en tout cas pas insultés."


n "Ils comprennent."


n "C'est ce que j'aime dans cette école. Personne n'est trop coincé, tout le monde est tellement... prévenant et compréhensif envers les autres."

stop music fadeout 4.0


n "\n\nJ'aimerais que le monde entier soit comme ça."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

scene black
with locationchange

window show


mi "Salutationnnnnn !"

scene bg school_dormhisao
with shorttimeskip

play sound sfx_paper
play music music_tranquil fadein 3.0


"Je tourne lentement la page, écoutant le bruissement du papier lorsque mes doigts le saisissent."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve


n "\nJe n'arrive pas à me détendre."


n "C'est les vacances d'été."


n "Pas de cours, pas de devoirs, pas de réunions du club d'art. Juste du temps libre pour faire ce que je veux."


n "Je n'en ai pas du tout l'impression."


n "J'ai essayé de réconforter Misha, mais je ne me sens pas trop joyeux moi-même."


n "Pour être honnête, le temps libre fait peur. Ça me rappelle l’hôpital et les longues journées sans intérêt qui devaient être remplies d'une façon ou d'une autre."


n "La seule différence, c'est que j'étais limité à l'aile, surveillé par les infirmières-cerbères."


n "Lire était une bonne solution à ce moment-là, mais la pensée de passer mes vacances d'été à lire des livres me fait me sentir un peu... geek."


n "Ça n'a rien à voir avec le fait que je suis en train de lire en ce moment même... Je passe juste le temps et essaye de combattre mon anxiété."


n "En plus, mon esprit vagabonde sur d'autres sujets, s'étirant dans trop de directions pour qu'elles soient toutes logiques."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

window show


"Et donc, l'avancée du livre que je lis depuis mardi est très l{w=0.3}e{w=0.3}n{w=0.3}t{w=0.3}e{w=0.3}."


"J'ai l'impression de mettre plus de temps à lire le livre que l'auteur a mis à l’écrire."


"J'essaye de le poser un moment, puis de recommencer à lire, recommençant depuis le début à chaque fois, lisant deux fois chaque page."


"Rien ne marche, j'ai zéro concentration."


"Le prenant avec moi juste au cas où, je sors pour trouver de l'air et l'inspiration pour savoir quoi faire."

scene bg school_courtyard
with locationskip


"Je me retrouve dans la cour, passant à coté des étudiants se dirigeant vers le portail."


"Les plus pressés repartent déjà chez eux, à en juger par les bagages qu'ils traînent derrière eux."


"J'imagine que même si Yamaku est très hospitalier, la maison reste la maison. Mais j'ai quand même entendu dire que certaines personnes restaient ici durant les vacances."


"La cour est suffisamment grande pour que son centre soit ensoleillé, peu importe à quel point le soleil est haut ou bas dans le ciel."


"Je m’arrête au milieu et baigne dans la chaleur."


"Je plisse les yeux à cause de la lumière en regardant en direction du bâtiment principal."


"Il semble déjà abandonné."


"Yuuko n'était pas au travail aujourd'hui, alors la prochaine fois que je pourrai avoir des livres de la bibliothèque, ce sera après les vacances."


"Il y a une bibliothèque publique quelque part dans le coin, mais je me sens trop mou pour y aller."

scene bg school_lobby
with locationskip


"L'entrée est tout aussi vide de monde alors je me contente de retourner aux dortoirs, finissant ma balade plus rapidement que prévu."


"Encore une fois, je n'étais vraiment pas sûr de ce à quoi m'attendre à la base."

scene bg school_girlsdormhall
with locationskip


"Sur l'impulsion du moment, j'entre dans le dortoir des filles pour voir si Rin ou Emi sont là."


"Aucune des deux n'est là, alors je retourne à ma propre chambre pour méditer sur ma léthargie."

window hide

scene bg school_dormhisao
with locationskip

$ renpy.music.set_volume(0.5, 1.0, channel="music")

nvl clear
nvl show dissolve


n "\n\nJe devrais arranger les choses avec Rin."


n "Elle m'embête vraiment."


n "\n\nDéfiant l’équivalent conceptuel de la gravité, elle tient en équilibre sur une fine ligne, zigzaguant entre la folie, l’incompréhension et l'instabilité."


n "Rin m'affecte aussi. Elle me met au défi d'une manière que je ne connaissais pas... ou plus exactement, je n'espérais pas qu'elle existe."


n "\n\nJ'ai commencé à me demander si ces sentiments étaient vraiment de l'amour, ou si je me trompais."


n "Serait-ce fou de penser ça ?"

nvl clear


n "\n\nPour le reste de la journée, Rin, l’hôpital, Yamaku et les vacances tournent dans ma tête."


n "\nJe n'arrive pas à me concentrer, même en me concentrant."


n "\nMes pensées semblent aller et venir au hasard, fragmentées en de trop petits morceaux pour être logiques."


n "\nJe ramasse le livre et arrive à lire une centaine de pages, mais je suis sûr que demain je ne me rappellerai plus de l'histoire."


n "\nJ'essaye de nettoyer ma chambre, mais même ça s’avère pénible, prenant trop de temps et demandant trop d'attention aux détails."


n "C'est généralement comme ça. Quand on n'a “rien à faire”, on ne fait rien même si on le pouvait."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

scene bg school_dormhisao_blurred_ss
show phone mobile at center
with shorttimeskip

window show


"Comme prévu, ma mère m'a appelé et j'ai fini par promettre de voir si je pouvais obtenir un billet de train pour demain, ou sinon, le lendemain."

window hide
nvl clear

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

$ renpy.music.set_volume(0.5, 1.0, channel="music")

nvl show dissolve


n "\n\nPeut-être que j'irai en ville demain de toute façon. Je pourrais faire du shopping ou un truc du genre."


n "Non pas que j'ai besoin de quoi que ce soit, mais peut-être qu'il y a des soldes d'été, et je pourrais prendre... quelque chose."

stop music fadeout 10.0


n "\n\n... Pourquoi est-ce que j'essaye de me forcer ?"


n "Avant, j’étais content en n'ayant rien à faire, à part taper dans le ballon de temps en temps sur le terrain."


n "Maintenant j'ai l'impression que je ne peux pas me poser du tout."


n "\nC'est parce que j'ai changé, ou parce que mon monde a changé ?"

nvl hide dissolve
nvl clear

scene bg school_dormhisao_ni
with shorttimeskip

window show


"Vers onze heures, les ténèbres m'invitent à dormir."

window hide

show pills:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

window show


"Les bouteilles de médicaments sont innocemment posées sur ma table de nuit, n'attirant pas du tout l'attention, me rappelant juste la réalité comme elle est."


"C'est le soir, alors je dois ouvrir trois bouteilles, extraire une grande pilule large de forme ovale de la première, deux petites rondes de la seconde et une dernière plate de la troisième, qui doit être séparée en deux."

window hide

show pills:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide pills
with None

window show


"L'eau que je prend pour gober mes pilules a un goût de métal sur ma langue."


"Je l'avale quand même avec les pilules et me dirige vers la salle de bain."

scene bg school_dormbathroom
with locationskip


"Le brossage de dents, travail ne nécessitant aucune force de réflexion, est tout à fait approprié pour organiser mes pensées."


"Une d'entre elles émerge de la masse, clairement au-dessus des autres."

window hide
nvl clear

nvl show dissolve


n "\n\n\n\n\n\n\n\n\nJ'ai envie de voir Rin."


n "Je ne peux pas laisser notre dispute et surtout ma colère être la dernière chose qui soit arrivée entre nous avant les vacances."

nvl hide dissolve
nvl clear

scene bg school_dormhisao_ni
with locationskip

nvl show dissolve


n "\n\n\n\n\n\n\n\nJe dois la voir. Demain."


n "Le sommeil triomphe de mon esprit confus avec plus de facilité que prévu."

nvl hide dissolve
nvl clear

$ suppress_window_before_timeskip = True

scene black
with shuteye


label fr_R36:


$ renpy.music.set_volume(1.0, 0.0, channel="music")
$ renpy.music.set_volume(0.7, 0.0, channel="ambient")
play ambient sfx_rain fadein 1.0

scene bg misc_sky_rn
show rain normal
show hisaowindow
with locationchange


"La pluie tombe sur mes vacances d'été comme un nombre incalculable de petits mauvais présages."


"Heureusement je ne suis pas superstitieux, mais le mauvais temps me déprime aussi."


"C'est comme ça depuis ce matin et il n'y a pas de fin en vue."


"Une masse grise impénétrable de nuages obscurcit le ciel tout comme elle obscurcit mon humeur."


"Dans un élan de défi, j'ai fini de nettoyer ce matin, mais après je me suis retrouvé à regarder par la fenêtre, espérant que le temps s’éclaircisse."


"Le battement incessant de la pluie sur le toit et le pavé est hypnotisant, un bruit de fond dans lequel je peux perdre mes pensées."

"…"

"… …"

$ renpy.music.set_volume(0.4, 1.0, channel="ambient")

scene bg school_dormhisao_rn
with locationchange


"Ça n'ira pas. Il faut que je bouge."


"Je devrais faire mes affaires maintenant, ou plus tard ?"

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")

scene bg school_dormhallway
with locationchange


"Je décide de le faire plus tard et sors, m’arrêtant brièvement devant la porte de Kenji pour écouter l’étrange bruit de raclage venant de l'intérieur."

show rain normal behind bg
with None


"Je n'ose pas frapper, de peur de découvrir ce qu'il y fait."

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

show bg school_dormext_full_rn as bg2 behind rain
hide bg
with locationskip


"Affrontant la pluie armé de mon fidèle parapluie, je traverse la cour en direction du dortoir des filles."

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")

scene bg school_girlsdormhall
with locationskip

play sound sfx_doorknock2


"Frapper à la porte de Rin ne me donne aucune réponse, mais la porte derrière moi s'ouvre à la place."

play sound sfx_dooropen

show emicas invis:
    center
    xpos 0.3
with None

show emicas happy at center
with dissolvecharamove

play music music_emi fadein 0.5


emi "Hisao ? Salut !"

show emicas awayfrown
with charachange


emi "Temps de chien. J'ai même loupé mon jogging matinal."


"Elle fronce les sourcils, mais je serais content si j'étais elle. Les courses matinales d'Emi sont tout sauf tranquilles."


hi "Oh, salut, j'étais—"

show emicas neutral
with charachange


emi "Si tu cherches Rin, je ne pense pas qu'elle soit là."


hi "Tu l'as vue récemment ?"

show emicas grin_up
with charachange


emi "Ouais, ce matin quand je l'ai réveillée."


"La mention de se réveiller fait bâiller Emi comme un chat, et ça lui donne l'air bête."


"Bien sûr qu'elle a vu Rin. Emi la réveille et l'aide à s'habiller presque tous les matins, et elle fait même son repas de temps en temps."


"Elles sont comme sœurs, même si elles semblent n'avoir rien en commun."


label fr_R36a:


"Je me demande laquelle des deux est la grande sœur ? Probablement Emi, contrairement à l'avis général."


"Elle est vraiment diligente, même si elle donne l'impression d'être quelqu'un de complètement tête en l'air."


"Pourquoi est-ce que je trouve bizarre qu'elle soit aussi dévouée sous son joyeux sourire ?"



label fr_R36x:

show emicas frown_up
with charachange


emi "Elle est partie pour la galerie il y a quelques heures... hé, tu m'écoutes ?"


"Peut-être que je fais une drôle de tête, puisqu'Emi penche la tête d'un air interrogateur, me regardant avec ses yeux ronds et curieux."

show emicas neutral
with charachange


emi "Mmh ?"


"Son visage innocent semble demander mon attention."


hi "Ouais, j'écoute..."

show emicas weaksmile
with charachange


emi "Je peux te poser une question ?"


hi "Ouais, bien sûr."

show emicas awayfrown
with charachange


"Elle plisse le front et se passe la langue sur les lèvres comme si elle se préparait pour quelque chose."

show emicas frown
with charachange


emi "Pourquoi est-ce que tu tiens tant à Rin ?"

show emicas neutral
with charachange


emi "Je veux dire, tu traînes probablement plus avec elle que moi, et on a même dormi ensemble dans le même lit quelquefois jusque, euh, récemment."


hi "Après qu'elle t’ait bannie pour lui avoir ravagé les cheveux ?"

show emicas blush
with charachange


"Une expression d'horreur sur le visage d'Emi apparaît, et ses yeux s’écarquillent d'au moins deux fois leur taille, donnant encore plus que d'habitude l'impression qu'ils sont des soucoupes, pendant qu'un léger rougissement apparaît sur ses joues et ses oreilles."

show emicas angry_up
with charachange


emi "Elle t'a dit ?! Ohhh… Je vais l'étrangler ou quelque chose de tout aussi horrible…"



"Je retiens un rire, de peur qu'elle s'en prenne à moi."

show emicas closedsmile
with charachange


"Emi oublie rapidement son embarras et semble pardonner à Rin au même moment, se reconcentrant sur moi."

show emicas smile
with charachange


emi "Bref, donc tu es amoureux d'elle, c'est ça ?"


"Oh oh. On dirait vraiment une question digne d'une grande sœur devant un prétendant. Emi est quelque peu fouineuse, et pas dans le bon sens du terme, si ça existe."


"Elle ferait une bonne partenaire avec Misha, pour être honnête. L'horreur."


hi "C'est déjà ta seconde question, alors je ne pense pas que je doive répondre."


"J'essaye d'afficher une expression faite de pur calme cristallin et de détachement."


"Je me demande si je parviens aussi à me tromper moi-même."

show emicas evil
with charachange


"Du moins Emi fronce dangereusement les sourcils, avec un petit sourire narquois sur les lèvres."


emi "C'est un oui ?"


hi "Non, ce n'est pas un oui."

show emicas neutral
with charachange


"Évidemment peu satisfaite de mon refus de répondre à sa question trop personnelle, elle a suffisamment de bon sens pour abandonner."

show emicas wink
with charachange


"Ça ne l’empêche pas de me tirer la langue comme une enfant, et de rire encore."

show emicas closedsmile
with charachange


emi "Si c'est ta réponse, alors je ne pense pas avoir besoin de continuer de parler avec toi."


"C'est facile de voir qu'elle n'est pas vraiment en colère."

show emicas happy
with charachange


emi "En plus, je dois préparer mes affaires maintenant. Maman sera inquiète si je loupe mon bus."


emi "À plus !"


hi "Ouais, à plus."

stop music fadeout 4.0

hide emicas
with charaexit

play sound sfx_doorclose


"Elle retourne dans sa chambre, me laissant seul dans le couloir."


"Ce qui est entre Rin et moi ne la concerne pas, hein ?"


"C'est pour ça que j'ai fini par ne rien dire à Emi à propos de notre dispute. Rin ne doit pas lui avoir dit non plus."


"Je crois... que même si elles sont amies, il y a des choses dont elles ne discutent pas."

"…"


"Donc, si Rin est à la galerie, je vais devoir aller jusque là-bas."


"Maintenant que j'ai réussi à sortir de ma chambre, j'imagine que ce n'est pas si difficile d'aller en ville."


"Je pourrais aller acheter un billet, mais le train devra attendre, au moins jusqu’à demain."

show rain normal behind bg
with None


"Pas question que je porte les bagages jusqu’à la gare sous cette pluie, même s'il n'y en a pas tant."

$ renpy.music.set_volume(1.0, 3.0, channel="ambient")

show bg city_street4_rn as bg2 behind rain
hide bg
with shorttimeskip


"La pluie rend toute vision lointaine très instable, comme si elle s’évanouissait."


"Le paysage urbain se transforme en un amas sans forme de divers tons de gris, au lieu de formes distinctes de bâtiments et de voitures."


"Ces pauvres âmes qui sont forcées à être sous la pluie essayent de se dépêcher autant que possible, s’apitoyant entre elles sur leur sort partagé."

show bg gallery_ext_rn as bg2
with locationchange


"Je prends le dernier tournant, le vingt-deuxième tournant pour ainsi dire, et je me sens immédiatement stupide d'être amusé par mon propre jeu de mots."


"La porte m'invite avec une promesse de chaleur."

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")
play sound sfx_storebell
play music music_soothing fadein 0.5

scene bg gallery_int
with locationchange


"L'eau de pluie ruisselant de mon parapluie fait des formes intéressantes, voire artistiques sur le sol."


"Je ne suis pas mouillé, à part mes chaussures, qui laissent de petites flaques dans mon sillage, complétant l'art à base d'eau de pluie."

show nomiya smile at twoleft
show sae neutral at tworight
with charaenter


"Nomiya est là aussi, discutant avec Sae au fond de la galerie. Je ne vois pas Rin, cela dit."


"Peut-être qu'elle est en haut."


"Il n'y a pas de clients cela dit, ce qui est normal, considérant les seaux d'eau tombant sur la tête de quiconque oserait braver le temps aujourd'hui."

show sae smile
with charachange


sa "Bienvenue."


hi "Bonjour. Pardon de vous déranger..."

show nomiya talk
with charachange


no "Ah, bonjour Nakai."

show nomiya smile
with charachange


no "Tu as fait tout le chemin pour nous rendre visite ?"


hi "Ah... non, je crois que c'était juste une impulsion. J'étais dans le voisinage, faisant des courses, quand j'ai décidé de passer."


"Mon réflexe est un mensonge, ce qui me surprend."


"Peut-être que je n'ai pas envie de dire que je suis venu spécifiquement pour voir Rin, même si ça doit être évident."

show sae doubt
with charachange


sa "Eh bien, tu as choisi une mauvaise journée pour faire les courses. Peut-être voudrais-tu du thé pour te réchauffer ?"


hi "Merci mais je vais bien, vraiment."


hi "Le temps pourrait être meilleur cela dit. De la pluie le premier jour des vacances, c'est un peu déprimant."

show nomiya veryhappy
show sae neutral
with charachange


no "Hahaha ! Bah, je suis sûr que ça s’améliorera."


"Nomiya nous offre son rire franc, plein d’énergie et de bonne humeur."


hi "La pluie ne vous atteint pas, monsieur ?"

show nomiya smile
with charachange


no "Eh bien, il est sûr que je préfère quand il fait beau aussi. J'étais d'ailleurs en train de partir pour aller rejoindre quelqu'un, et je préférerais ne pas avoir ma veste trempée. Elle est vraiment chère."

show nomiya talk
with charachange


no "Mais bien sûr que je suis de bonne humeur !"

show nomiya smile
with charachange


no "Qu'est-ce que tu as pensé de l'exposition ? Superbe, non ?"


hi "Ouais, très bien."


"Ma réponse sans enthousiasme l'encourage seulement à continuer, marchant dans la galerie en parlant sans arrêt du vernissage."


"Il parle plus et plus fort quand il bouge. C'est quelque chose que j'ai remarqué lors des réunions du club aussi."

show nomiya veryhappy
with charachange


no "On a pu parler avec beaucoup de bonnes personnes et se faire des contacts importants."

show nomiya smile
with charachange


no "Une des peintures de Tezuka a même été vendue, à un collectionneur d'Osaka."

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")

show rin_exhibition_sold at center
with locationchange


"Je suis son regard vers un emplacement vide sur le mur, je ne me rappelle pas laquelle était accrochée là."


"Enfin, elle n'est plus là maintenant."

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")

hide rin_exhibition_sold
show nomiya talk
with charachange


no "On a eu de la chance qu'elle aille bien malgré ce petit étourdissement."

show nomiya smile
with charachange


no "Elle est devenue un peu silencieuse cela dit, alors je lui ai dit de se reposer. Mais, encore une fois, elle a toujours été assez timide."


"Timide ? Bah, je me contente d'hocher la tête."

show nomiya talktongue
with charachange


no "La réception s'est bien passée en général. Je pourrais être en mesure de faire en sorte qu'un de mes amis écrive un petit article dans un magazine pour—"


sa "Shinichi, ta réunion. Tu fais attendre M. Takahashi."

show nomiya serious
with charachange


"La remarque de Sae le fait s’arrêter dans son élan et regarder sa montre."


"Nomiya fronce les sourcils de mécontentement à l'interruption de sa tirade."

show nomiya smile
with charachange


no "Oh, c'est vrai. Oui, bon, je ferais mieux d'y aller. Nous nous reverrons en septembre, Nakai."


hi "Au revoir."

hide nomiya
with charaexit

play sound sfx_storebell
stop music fadeout 4.0


"Woaw, le professeur ne lésine vraiment pas quand il s'agit de la future carrière d'artiste de Rin."


"J'imagine qu'il faut beaucoup pour réussir, mais je pense que son travail serait plus facile si Rin était plus coopérative."

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve


n "\nElle est trop indécise même si elle va bien. Comme cet “étourdissement” de la nuit précédente."


n "Elle a juste paniqué ou quelque chose du genre, et je n'ai rien fait pour l'aider."


n "\nJe soupire."


n "J'ai l'impression que le fossé entre Rin et moi ne fait que s’agrandir."


n "Elle va accomplir de grandes choses pendant que je suis toujours embourbé, bien que je me sois promis d'essayer de faire quelque chose de ma vie."


n "En plus de ça, on a eu cette dispute, et plus on passe de temps sans parler, plus les blessures sont longues à guérir."


n "À supposer que c'est ce qu'on veut. Je n'ai jamais découvert ce que ressentait Rin, et maintenant je ne suis pas sûr de ce que je ressens moi-même."


n "J'aimerais pouvoir la comprendre. Mais Rin n'est pas très ouverte à interprétation."


n "Non pas qu'elle cache quoi que ce soit, elle semble juste défier mes tentatives de comprendre de quoi elle parle à chaque fois que je la vois."

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")
$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

show sae smile
with charachange

window show


sa "Quelque chose te perturbe ?"


"Je réalise que je suis en train de rêvasser au milieu de la galerie depuis je ne sais combien de temps."


hi "Ahh... rien de spécial..."


"Je fais semblant d'étudier les tableaux les plus proches pour la distraire."

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
play music music_another fadein 0.5

scene rin_exhibition_c:
    truecenter
    zoom 1.0 subpixel True
    ease 30.0 zoom 1.1
with locationchange


"Je l'ai déjà vu."


"Les couleurs maintenant familières, tournant et se mélangeant les unes aux autres d'une façon qui semblerait aléatoire, donnent toujours l'impression qu'il se passe quelque chose dans les coulisses, pour ainsi dire."


"Le style de Rin est comme elles. Abstrait, incompréhensible, coloré."


"Mystérieux."


"Je me demande si pour comprendre un artiste, on doit comprendre l'art ?"

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")

scene bg gallery_int
with locationchange


hi "Mmh... J'ai peut-être une question."

show sae smile at center
with charaenter


sa "Oh ?"


"Elle relève les yeux du magazine qu'elle feuilletait, semblant ravie de mon intérêt."


hi "Comment vous interprétez l'art ?"

show sae doubt
with charachange


sa "Comment ça ?"


"Elle lève les sourcils, comme si la question était trop compliquée pour commencer à répondre sans plus de précision."


hi "Désolé si je demande quelque chose de stupide."


hi "Je ne pense pas que je puisse comprendre comme le font les pros."

show sae smile
with charachange


sa "Oh, il n'y a rien de compliqué."


"Sae repousse ma question avec un simple geste du poignet."

show sae neutral
with charachange


sa "Tout le monde interprète comme il le veut, et l’interprétation est tout autant dans l’œil de l'observateur que dans les intentions du créateur."


sa "Les “pros” ont leurs propres moyens, parce qu'il y a une chose appelée la théorie de l'art."


sa "Il y a des schémas dans l'art, comme dans tout, et on présume qu'il est possible de trouver des conclusions en observant ces schémas."


"Sa voix est comme celle d'un professeur donnant un cours et apportant de l'emphase aléatoirement aux mots pour garder l'attention du public."

show sae smile
with charachange


sa "En fin de compte, j'imagine que ça ne veut pas dire grand-chose."


"Elle finit par parler apparemment toute seule, marmonnant suffisamment fort pour que je l'entende clairement."


sa "Une bonne œuvre d'art te fera ressentir quelque chose et c'est tout ce qu'il y a à dire."


sa "Les sentiments changent et ils affectent l'art que l'on crée et celui que l'on voit."


hi "Mais..."

show sae neutral
with charachange


sa "Je vais te raconter une histoire."


hi "Vous êtes sûre ? La dernière était déprimante..."


sa "C'est important. Écoute."


sa "Il y a une centaine d'années, un peintre peu connu a reçu la nouvelle que son ami, un homme nommé Casagemas, s'était suicidé."



sa "C'est arrivé pendant qu'il était loin et alors qu'il n'avait pas vu son ami depuis un moment."


sa "Donc évidemment il a dû se sentir encore plus perturbé qu'à la normale quand on entend quelque chose comme ça."


sa "Pendant quatre ans après ça, notre protagoniste n'a rien fait de plus que de la peinture monochrome parce qu'il était profondément affecté par la nouvelle."


sa "Quoi qu'il ait fait, il est toujours retourné à la même couleur jusqu’à ce qu'elle finisse par relâcher sa prise."


"Elle prend une petite pause pour vérifier que je suis toujours."


"C'est le cas, dans une certaine mesure, alors je lui donne l'incitation pour laquelle tous les raconteurs d'histoires semblent vivre."


hi "Donc..."


"C'est difficile de continuer de là, puisque je ne peux trouver les questions qu'elle aimerait que je lui pose."


"Comme un apprenti Socrate, elle pensait présenter tous les outils pour la révélation devant moi."

show sae doubt
with charachange


sa "Tu ne vois pas encore le sens ?"


"Seulement, son élève s'est avéré être trop perdu pour comprendre."

show sae scowl
with charachange


"Elle semble mécontente de ma lenteur."


sa "La Période Bleue de Picasso est une des périodes les plus louées dans l'histoire de l'art, mais qui sait ce qu'il a ressenti quand il travaillait sur ces chefs-d’œuvre ?"


sa "Tristesse ? Nostalgie ? Regret ?"


sa "Personne ne sait."


sa "Si tu vois maintenant une des peintures de la Période Bleue, tu l’interpréterais sûrement différemment d'avant parce que tu as su pour l'ami de Picasso, Casagemas."

show sae neutral
with charachange


sa "Expérimenter l'art est toujours personnel, seulement interactif par hasard ou à cause des circonstances."


sa "Il y a des millions d'explications pour chaque œuvre d'art, mais il est possible qu'aucune d'entre elles ne soit conforme aux intentions de l'artiste."

show sae smile
with charachange


sa "Chaque homme dépend d'un autre, tu sais ?"


"Je hoche la tête sans comprendre ce que sa remarque voulait dire."


"Ce qu'elle a dit semblait clair à part ça, sauf une chose."


"Si l'art est de la communication comme l'a dit Rin, mais que tout le monde parle son propre langage secret comme l'a dit Sae, comment espérer communiquer dans ces conditions ?"


"Ça semble si futile, si inutile."


"L'art n'est vraiment pas une chose pour moi."

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")

scene bg gallery_exhibition
with locationchange


"Sae retourne à son magazine d'art, et je fais un tour de la galerie, essayant de voir ce que Rin peut voir à travers ses propres peintures."


"Une ambiance apaisante prend place dans la galerie assaillie par la pluie, les grandes fenêtres rendant l'isolement plus confortable."

play sound sfx_storebell
stop music fadeout 2.0


"Un bruit de clochette interrompt l'ambiance tranquille."

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")

scene bg gallery_int
with locationchange

show rin relaxed_nonchalant at center
with charaenter


"Rin pousse la porte avec son épaule et entre."


"J'avais presque oublié qu'elle était la raison pour laquelle je suis venu à la galerie en premier lieu."

show rin relaxed_boredom
with charachange


rin "Je crois que je suis prête—{w=0.3}{nw}"

show rin relaxed_surprised
with charachange


"Elle s’arrête au milieu de sa phrase, remarquant ma présence."


"Le même silence que celui qui suit un bris de verre dure pendant exactement une seconde et demie, temps insuffisant pour que Sae ou moi ouvrions la bouche, mais suffisant pour que Rin réagisse."

show rin negative_annoyed
with charachange


rin "Je vais marcher un peu."

hide rin
with charaexit

play sound sfx_storebell


"Retournant à l'extérieur avec un rythme précipité qui est inhabituel de sa part, Rin semble oublier qu'il pleut toujours."

show rain normal behind bg


"Sans vraiment y réfléchir, j'attrape mon parapluie et me précipite derrière elle."

play sound sfx_storebell
$ renpy.music.set_volume(1.0, 2.0, channel="ambient")

hide bg
show bg city_street4_rn as bg2 behind rain
show rin negative_spaciness_close_rn
with locationskip


"Je rattrape Rin au coin de la rue, ouvre mon parapluie et le positionne au-dessus de nous deux, tout en ayant presque à courir pour tenir le rythme avec elle."


"Elle ne me reproche pas de lui avoir couru après ou de la protéger de la pluie, finissant par ralentir un peu pour que je puisse m'adapter à son rythme sans prendre le risque de m'essouffler."


"Je me relaxe, évaluant la situation."


"La dernière fois que j'ai tenu mon parapluie pour nous protéger tous deux de la pluie, je n'y pensais pas trop."


"Mais maintenant, toutes les choses qui sont arrivées depuis ce moment se sont rassemblées, formant une boule glaciale autour de mon estomac."


"Être proche d'elle me met mal à l'aise, et je me sens légèrement troublé."


"C'est difficile de faire sortir les mots de ma bouche, et elle me semble soudainement très, très sèche."


"Cela dit, ce n'est pas comme si je pouvais abandonner."


hi "Pourquoi tu continues de fuir ?"

show rin negative_annoyed_close_rn
with charachange


rin "Je ne veux pas te parler."


hi "Je veux te parler."

show rin negative_confused_close_rn
with charachange


rin "Ça fait mal à chaque fois qu'on parle."


hi "Des fois on n'y peut rien."

show rin negative_sad_close_rn
with charachange


rin "Je ne veux pas faire de mal."


hi "D'accord. Pas besoin de parler."

show rin relaxed_doubt_close_rn
with charachange


rin "Qu'est-ce qu'on fait alors ?"


hi "Continuons juste de marcher."

show rin relaxed_surprised_close_rn
with charachange


rin "Juste marcher ?"


hi "Juste marcher."

show rin basic_absent_close_rn
with charachange


rin "D'accord."


label fr_R37:

play music music_dreamy fadein 2.0
$ renpy.music.set_volume(1.0, 2.0, channel="ambient")
$ renpy.music.play(sfx_rain, fadein=2.0, if_changed=True, channel="ambient")

play sound sfx_whiteout

scene white
with Dissolve(1.0)

show rain normal behind white
with None

hide white
show ev rin_rain_away_close behind rain at Fullpan(20.0,dir="up")
with Dissolve(1.0)


"Nos pas font “splish splash” dans les flaques de la rue alors que nous marchons sous la pluie."


"Rin, marchant maintenant à côté de moi à sa manière calme et relaxée, ne semble pas être perturbée par le fait qu'elle se mouille même si elle peut l’éviter."


"Elle n'est pas totalement protégée par mon parapluie, malgré le fait qu'il soit bien assez grand pour nous deux."


"C'est comme si elle ne remarquait même pas que la pluie mouillait sa chemise."

"…"


"Le comportement de Rin évoque toujours des images mentales de calme méditatif, même si elle peut sembler légèrement tourmentée."


"Mais je ne pense pas que ce soit de la méditation. Elle est juste trempée."


"J'aimerais pouvoir être plus calme aussi."


"Je suis devenu trop impliqué avec Rin pour agir avec ma réserve habituelle."


"J'ai l'impression d'être devenu une de ces personnes qui se trompent en pensant qu'elles sont objectives, mais finissent par se rendre compte qu'elles sont les pires des menteuses."


"L'illusion, nous duper, quelle meilleure façon d'avoir l'impression d'être une bonne personne ?"


"Il est peut-être préférable de perdre cette illusion."

show ev rin_rain_away_close at Position(yalign=0.0)
show ovl rin_rain_hisaotowards_close behind rain at Position(xalign=1.0, yalign=0.0)
with charachange


hi "Je vais rentrer chez moi pendant un moment, alors je me suis dit que j'allais te voir avant ça."


"J'aurais pu trouver un meilleur moyen d'engager la conversation, mais le refus de parler de Rin rend les choses difficiles."


rin "C'est bien. J'aurais pu croire que tu t'étais fait kidnapper sinon."


hi "Tu ne peux pas continuer à tout fuir. Même pas moi qui essaye de te parler sérieusement."


rin "Je suis toujours sérieuse. Et aussi j'ai l'impression de courir très lentement là."


rin "Peut-être que je devrais prendre des cours avec Emi."


"C'est futile. Comme parler à un mur en brique qui te sort aléatoirement des réponses insensées."


hi "Pense au vernissage de l'exposition. Et si tu t'étais enfuie ?"


"Rin ne répond pas, elle continue de marcher. Ou courir lentement, s’échappant dans son silence."


"Elle a le don de pouvoir être seule avec de la compagnie, j'ai remarqué."

show bg city_street3_rn behind rain
hide ev
hide ovl
with locationchange


"Nous descendons la rue, prenons à gauche, trois fois à droite, puis à gauche encore."


"Comme cette nuit-là, il y a quelque temps, nous choisissons les directions au hasard parce qu'il importe peu de savoir où on va."



"Tout ce qui compte sont les pas et le son des gouttes d'eau frappant contre le parapluie."


"L'eau coule des toits des bâtiments dans les caniveaux et se transforme en petites rivières."


"Même si j'essaye de les enjamber, mes pieds se mouillent quand même à travers les chaussures."


"Nous continuons de marcher dans un silence qui ne demande qu'à être brisé encore une fois. Je suis sûr d'être le seul à ressentir ça, cela dit."

hide bg
show ev rin_rain_away behind rain
show ovl rin_rain_hisaotowards at Position(xalign=1.0, yalign=0.0) behind rain
with locationchange


hi "Pourquoi tu as fait cette exposition ?"


"Rin hausse les épaules d'un air morne et regarde dans l'autre direction. J'abandonne ce sujet."

window hide

hide ovl
with charachange

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")
$ renpy.music.set_volume(0.5, 1.0, channel="music")

nvl clear
nvl show dissolve


n "\n\n\nC'est inutile."


n "\nQu'est-ce qu'elle voulait accomplir ? Ce qu'elle a dit le soir du vernissage m'a donné l'impression qu'il y avait quelque chose... quelque chose de spécial qu'elle voulait."


n "J'ai eu l'impression que Rin espérait quelque chose d’inatteignable."


n "Elle a mis la barre haut et elle a perdu toute seule, peu importe à quel le point les gens aimaient ses œuvres."


n "C'est compréhensible de manquer de réalisme. La plupart des gens sont dans ce cas, même si ce n'est pas à un niveau aussi extrême que Rin."


n "\nMais ce n'est pas une raison pour vivre dans un monde qui n'accepte pas de visiteurs."

nvl clear


n "\n\n\nTu ne peux pas modeler le monde pour qu'il convienne à ta cosmologie tordue et mégalomaniaque où tout marche comme tu le veux."


n "\nC'est ce qui me frustre le plus avec Rin."


n "\nElle veut que le monde marche à sa façon, ignorant tout ce qui lui semble non pertinent ou inutile."


n "Je n'arrive pas à croire que qui que ce soit à Yamaku puisse ne pas avoir le minimum de perception pour comprendre que le monde peut parfois être très injuste."


n "Je suis sûr qu'elle n'est pas la seule qui aimerait que certaines choses soient différentes, mais on peut au moins saisir les faits tels qu'ils sont."

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")
$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

hide ev
show bg city_street4_rn behind rain
show rin negative_spaciness_close_rn at center
with locationchange

window show


"Je regarde Rin du coin de l’œil, qui regarde notre protection en forme de dôme. Ça remplace mal le ciel avec sa couleur morne et monochrome."


"La pluie continue de tomber."


"Tout comme les nuages aujourd'hui, Rin ne donne pas vraiment l'impression d'avoir envie d'être regardée."


"Elle est maussade, tout comme le ciel qu'elle aime."


"Je n'aurais pas dû venir. Sa présence me rappelle seulement à quel point je me suis énervé à cause des mêmes raisons, qui ne changeront sans doute jamais."


"Même si je veux dire que je suis désolé, même si je ne veux pas qu'on se sépare, je ne peux pas me résoudre à dire l'une de ces deux choses."
show bg misc_sky_rn
hide rin
with locationchange


"Nous continuons d'avancer dans la rue trempée, un pas à la fois."


"Souvent, quand on marche avec quelqu'un d'autre, nos pas se synchronisent comme s'il y avait une sorte de connexion inconsciente."


"J'ai remarqué que ce n'est jamais notre cas."

window hide

stop music fadeout 5.0
$ renpy.music.set_volume(0.3, 3.0, channel="ambient")

show bg misc_sky_rays
show rain light
with Dissolve(3.0)

window show


"Le temps passe, et l'assaut contre le parapluie s'amenuise alors que les nuages au-dessus de nous se dispersent pour révéler un bleu azur."

show rain light:
    alpha 1.0
    linear 5.0 alpha 0.0
with None

stop ambient fadeout 9.0


"Finalement la pluie s'amenuise suffisamment pour que je ferme mon parapluie, secouant l’excès d'eau avant ça."


"Pendant que je me bats avec le mécanisme, Rin s’arrête si brusquement que c'est seulement quelques mètres plus loin que je me rends compte qu'elle ne suit plus."


"Ce fichu parapluie semble s'être coincé."

play music music_innocence fadein 6.0

scene ev rin_trueend_normal:
    truecenter
    zoom 1.2 rotate -6 subpixel True
    easein 6.0 zoom 1.0 rotate 0
with locationchange


"Quand je me retourne, je la vois en train de me regarder avec une expression impassible."


rin "Je voulais que quelqu'un me dise “Je comprends ce que tu ressens.”"


rin "Ça ne serait pas bien ?"


"C'est une réponse à la question d'avant ? Je ne suis pas sûr."


hi "Ouais... mais pourquoi est-ce si important ?"

scene ev rin_trueend_sad:
    truecenter
    zoom 1.0 rotate 0 subpixel False
with locationchange


rin "Parce que sinon... Je ne sais pas comment je peux supporter ça."


"J'étais en train de refermer mon parapluie alors j'ai juste répondu ça machinalement, mais ce qu'elle dit me glace le sang."

scene ev rin_trueend_closed
with locationchange


rin "Si quelqu'un dit une blague et rit, tu ris avec eux, hein ? Parce qu'une joie doublée est une joie triplée, hein ?"


scene ev rin_trueend_smile
with locationchange


rin "Si quelqu'un a mal et est triste, tu le réconfortes et le prends dans tes bras, hein ? Parce que c'est—"

rin "…"


"Elle s'arrête, la bouche à moitié ouverte, puis se rappelle de la refermer."

scene ev rin_trueend_normal
with locationchange


"Une expression lugubre s'affiche sur son visage et simultanément dans mon cœur."


rin "Je ne sais pas pourquoi les bons mots ne sortent jamais."


rin "Je ne sais pas pourquoi je peux rire seulement quand je me force."


rin "Je ne sais pas pourquoi tout reste uniquement à l'intérieur de moi, même quand j'ai l'impression que je vais exploser."


"Son visage sans expression ne change pas même quand elle dit ça."


"Sa voix habituellement neutre est légèrement plus calme qu'à la normale."


rin "Mais qui... qui voudrait avoir envie de ressentir ça ?"


"Rin me regarde et j'imagine la tristesse se reflétant dans ses yeux, qu'elle soit vraiment là ou non."


rin "Pas moi."


rin "Je ne veux pas ressentir ça."


"Nous restons silencieux un petit moment après ça."


"Rin, parce qu'elle a dit tout ce qu'elle a à dire d'un coup, moi parce que je n'ai aucune idée de comment gérer ce qu'elle vient de dire."


"Je ne comprends pas ce que dit Rin. Ou alors je comprends, mais je ne veux pas."


"Pour la première fois que ces deux choses arrivent, il faut que ce soit simultané."


"L'ironie ne passe pas inaperçue."


hi "Je... crois que tout le monde veut être compris. C'est universel."


hi "Mais... c'est impossible. Pas seulement pour moi, mais pour tout le monde."


hi "Sae l'a dit aussi."


hi "Tu affectes d'autres personnes et tu es affectée par elles, mais en fin de compte, tu vois les choses seulement de la façon dont tu les interprètes."


hi "Tout le monde... est seul. On s'utilise juste les uns les autres pour alléger cette solitude."


"Je me demande pourquoi je raconte ça. J'ai l'impression que ce que m'a dit Sae était vrai, comme si j'avais toujours pensé comme ça sans le savoir."


"J'ai l'impression qu'elle a éclairci mes pensées en des termes simples avec l'aide de cette stupide histoire sur Picasso."

scene ev rin_trueend_closed
with locationchange


"Rin laisse tomber sa tête comme une fleur fanée, laissant ses mèches devant ses yeux pour que je ne puisse pas les voir."


rin "Pourquoi tu dis ça quand tu m'as fait ressentir l'inverse ?"


rin "C'est injuste."


"La voix tremblante qui dit ces mots n'appartient pas à Rin."

scene ev rin_trueend_sad
with locationchange


rin "Je pensais vraiment que tu pouvais être différent. Que je n'aurais pas à être seule."


"C'est une voix aigre de déception, passant par des dents serrées et une poitrine tremblante."


hi "Je suis désolé..."


rin "Si c'est le cas, pourquoi est-ce que tu dis des choses injustes comme ça ?"


"Son ton exigeant ne déclenche aucun sentiment particulier en moi, à part la tristesse qui est présente depuis hier soir."


"Elle ne m'intimide plus du tout. Plus maintenant."


"Rin n'est pas un génie artistique prodigue, ni une savante imprévisible et idiote qui pourrait déchirer en deux le lobe de la logique de mon cerveau à chaque fois qu'elle ouvre la bouche."


"Elle est juste une fille que j'ai pensé aimer, une fille qui voulait être mon amie, une amie que j'ai laissé tomber."


hi "Je dis ça, parce que sinon j'aurais l'impression de mentir."

scene ev rin_trueend_normal
with locationchange


rin "Pourquoi ?"


"Les questions simples sont les plus difficiles. Je dois fermer les yeux et rassembler mes pensées pour pouvoir lui répondre."


hi "Je ne suis pas un artiste. Je ne pourrai jamais être au même niveau que toi."


hi "Il y a un monde que seulement toi peux voir, et pour en faire partie je devrais devenir toi."


hi "C'est quelque chose que je ne peux pas faire, peu importe à quel point tu aimerais que je le fasse."


"Rin encaisse mon explication sans même un battement de cil."


rin "Je ne suis pas une vraie artiste non plus."


rin "Je peins juste parce que ça me donne l'impression de pouvoir vraiment ressentir quelque chose."

scene ev rin_trueend_weaksmile
with locationchange


"Elle retient son souffle pendant un moment avant de le relâcher, lentement, comme un soupir."

scene ev rin_trueend_closed
with locationchange


rin "C'est pour ça que je vais le faire."


rin "J'ai décidé. Je vais le faire. Si même Hisao dit ça, alors je vais le faire."



hi "Faire quoi ?"


"Rin commence à agir comme si elle parlait de nouveau toute seule, mais je suis content de pouvoir la ramener maintenant."

scene ev rin_trueend_normal
with locationchange


rin "Le professeur et Sae ont parlé avec quelqu'un qui est une personne très importante. J'ai une bourse pour une grande école d'art à Tokyo."


rin "Il a dit que je pourrais être transférée là-bas et commencer à la fin de l'été, si je le voulais."


rin "Je ne comprends pas vraiment pourquoi—"

stop music fadeout 10.0


hi "Hein, quoi ? Pourquoi tu ne me l'as pas dit ?"

scene ev rin_trueend_smile
with locationchange


rin "Je viens de le faire. Tu es la première personne à qui je l'ai dit parce que je viens de le décider maintenant."


"Elle garde son calme, semblant seulement légèrement surprise par mon interjection choquée."


"C'est ridicule avec quelle facilité elle peut dire quelque chose de si important."


"Je n'arrive pas à le croire. Après ce qui est arrivé en février, j'ai eu assez de changement pour cette année."


"Même si les choses tournent mal maintenant, je ne veux pas que tout change."


hi "Mais et Yamaku ? Tu ne veux pas avoir ton diplôme avec tout le monde ?"


"Ma plaidoirie ne suscite aucune émotion."


rin "Qui ça tout le monde ?"


hi "Emi, moi, tout le monde !"


"Je sens mon pouls accélérer fortement, et ma respiration devenir courte."


"Je ne veux pas que ça arrive."


rin "Leur vie n'est pas la mienne."


rin "Tu viens de dire que tout le monde est seul."


hi "Je ne voulais pas dire ça comme—"


rin "Tu dis toujours qu'il faut saisir ce que l'on peut et commencer à vivre sa vie."


rin "Je dois vivre ma vie aussi."


"Rin déforme mes paroles pour justifier sa nouvelle fuite. Ça me met en colère."


"Sa facilité et son sérieux pour annoncer ça sont inacceptables."


"Comme si changer de vie était quelque chose de faisable sur un coup de tête ! Non !"


hi "Comment tu peux dire ça ? Pourquoi tu n'essayes même pas de faire partie d'un groupe ?"


"Mon accusation désespérée n'a aucun effet. J'ai l'impression de ne plus avoir d'armes, encore une fois, et que je ne peux pas l'atteindre, peu importe ce que je fais."


"Rin est tellement frustrante en étant aussi tranchante dans sa décision que ça me ferait la détester si je ne l'aimais pas, même si je ne sais plus ce que je ressens maintenant."

scene ev rin_trueend_normal
with locationchange


rin "Peut-être que je suis ce genre de personne. Le genre qui n'appartient qu'à elle."


hi "Je n'accepterai pas ça."


"Son regard nonchalant ne semble pas se préoccuper que j'accepte ou non sa décision."

"…"


"La pause me permet de faire tomber la pression, de retrouver mon calme."


"Pendant ce temps, les nuages qui s'éloignent révèlent un soleil couchant qui a encore le temps de briller pendant un moment avant de finir sa journée."


"Une mosaïque de lumière et d'ombre se propage sur les murs des bâtiments, sur les rues et le grillage autour du parc de l'autre côté de la rue."


"L'ombre de Rin est suffisamment longue pour atteindre mes pieds."


"C'est comme dans l'un de ces westerns où deux cow-boys se regardent, prêts à dégainer leurs revolvers sur l'autre."


"Celui qui perd son calme mangera du plomb."


"Je réalise que je serais désavantagé parce que le soleil est derrière Rin, m'aveuglant."

scene ev rin_trueend_sad
with locationchange


rin "Tu me détestes ?"


"Elle dégaine en premier et je n'ai aucune parade."


hi "Je ne sais pas."


"Ai-je perdu ?"


hi "Même si c'est le cas, est-ce important ?"


"Je cherche des mots, des mots qui pourraient contrer ça. Je n'en trouve aucun."


hi "Tu es mon amie, je te l'ai promis. Je ne suis pas le genre de gars qui oublie ses promesses."


hi "Je crois que c'est la chose la plus importante. On pourrait essayer de—"

scene ev rin_trueend_normal
with locationchange


rin "Ne le dis pas."

scene ev rin_trueend_hug
with locationchange

play music music_friendship fadein 4.0


"Devinant ce que j'allais dire, Rin se jette dans mes bras, pressant son corps contre le mien."


"Je la sens se lever sur la pointe des pieds pour s'accorder à ma taille et se coller encore plus contre moi."


"L'odeur de ses cheveux est celle de la pluie et de la peinture. Son corps est aussi froid que toujours. Sa respiration sur ma nuque est aussi chaude que toujours."


"C'est drôle comme tout ça me semble si familier alors que Rin elle-même ne l'est pas."

scene ev rin_trueend_hugclosed
with locationchange


rin "Tu es sûr que tu ne peux pas me détester ?"


"Rin chuchote tellement près de mon oreille que je peux sentir les mouvements de ses lèvres sur mon lobe."


"C'est taquin, provocateur. Si c'était dans un autre type de situation, je suis sûr que ça me chatouillerait suffisamment pour que je me mette à rire même si je suis un garcon."


rin "Ça serait plus facile si c'était le cas."


hi "Je sais pas. C'est vraiment dur quand tu me fais un câlin comme ça."

scene ev rin_trueend_sad
with locationchange


"Je me demande si c'est à cause de ma voix morne, mais elle fait un pas en arrière, regardant d'un air embêté ses bras raccourcis."


"J'aurais préféré qu'elle ne fasse pas ça."


rin "Je ne peux pas faire de câlins aux gens, Hisao."


rin "Je suis une mauvaise personne."

scene ev rin_trueend_normal
with locationchange


rin "C'est pour ça que je dois partir."


"Elle me désarme complètement avec ces trois simples phrases, me rendant incapable de continuer à argumenter."


"Et puisque je ne peux pas, Rin est libre de continuer comme elle veut, en déplaçant son poids d'un pied sur l'autre."

scene ev rin_trueend_smile
with locationchange


rin "J'apprendrai à faire des câlins aux gens à ma façon."


rin "Je suis sûre de pouvoir devenir une vraie artiste."


rin "Mais si c'est le cas... je pourrais ne plus être moi après."


"Le très léger sourire sur ses lèvres la trahit, un faux signe de confiance en soi dans un avenir que même Rin ne peut pas prévoir."


"Je voudrais interpréter ça comme un signe d'espoir, mais je sais que non."


"Rin continue de rire à sa façon, ce sourire gêné, forcé."


rin "C'est pourquoi... oublie-moi s'il te plaît, et je t'oublierai aussi."


rin "Je suis sûre que—{w=0.5}{nw}"

scene ev rin_trueend_sad
with locationchange


"Elle s'étouffe au milieu de sa phrase que je suis condamné à ne jamais entendre."


"Je ne pense pas que j'aurais voulu l'entendre de toute façon."


"C'est injuste."


"Rin ne plaisante pas. Rin est toujours sérieuse. Mais je ne peux pas l'accepter, je ne peux pas."


"T'oublier ? Comment est-ce que je pourrais... ?"


"C'est ce que j'aimerais dire. Mais je ne sais pas comment je continuerais. Je ne trouve rien de bien à dire, alors je dois la défier."


hi "Comment est-ce que tu peux dire une telle chose ?"

scene ev rin_trueend_normal
with locationchange


"Rin lève les yeux pour rencontrer les miens, ils sont sérieux et profonds, une image parfaite du territoire sauvage que j'ai toujours pensé qu'ils étaient."


"Même maintenant, je ne peux pas lire ses émotions à travers ses impassibles iris couleur jade qui ne reflètent jamais ce qu'ils voient."


rin "C'est facile. Après tout, je suis douée pour oublier les choses."

"…"


"Son injustice me coince la gorge, mais j'arrive à sortir la question qui me torture."


hi "Donc, c'est ça ? C'est un au revoir ?"

"…"


"Rin continue de me regarder gentiment, sans répondre à ma question."


"D'après ses yeux, je peux voir qu'elle n'a même pas besoin de dire quoi que ce soit."


"Il n'y a plus de mots pour nous."

stop music fadeout 12.0

scene ev rin_trueend_gone
with locationchange


"Elle s'est tournée et s'est mise à marcher sans regarder en arrière."


"Tout autour de moi, le monde a continué de changer, peu à peu, mais je suis resté là, debout."

scene ev rin_trueend_gone:
    "ev rin_trueend_gone_ni" with Dissolve(10.0)
with None


"Le soleil a baissé au-dessous de l'horizon, projetant de longues et fines ombres dans la rue."


"Dans la lumière en déclin, le dos de Rin au loin semble être un rêve distant."


"L’écart entre nous grandit lentement."


"Les ondulations dans les flaques où elle a marché s’étendent jusqu’à atteindre les limites de leur courte existence et disparaissent sans laisser de trace."


"Ses mots restent gelés au fond de mon cœur."

window hide


label fr_R38:


scene bg school_room34
with None

show rin negative_spaciness
with charaenter

play music music_drama fadein 6.0


"Elle se tient au milieu de la pièce ensoleillée, regardant entre les rideaux dans le jardin."


"Comme si souvent auparavant, elle ne part ni ne bouge, elle attend juste calmement que je fasse le premier pas."


"C'est comme si elle essayait de devenir une partie intégrante du mobilier."


hi "Le professeur te cherche."


"Un regard vide par-dessus son épaule est tout ce que j'obtiens, accompagné par une expression cryptique sur son visage."


rin "Tu me cherches aussi ?"


hi "Nan, je t’ai déjà trouvée."


rin "Tu penses ?"

show rin negative_annoyed
with charachange


"Elle fronce les sourcils, semblant si perplexe que je me demande si la question était vraiment sérieuse."


"Peut-être qu'elle l'était."


hi "Tu parles métaphoriquement maintenant ?"

show rin negative_spaciness
with charachange


rin "Tu veux dire comme les anguilles, les grottes et les sombres nuits de tempête ?"

show rin negative_sad
with charachange


rin "Je suis pas douée pour les trucs comme ça."

"…"

play sound sfx_doorclose


"Les salutations brusquement finies me donnent une chance de refermer la porte derrière moi et de m'asseoir sur un bureau couvert de poussière."

show rin basic_absent
with charachange


"Rin reste là, mais au moins elle se tourne."


"J'aurais plutôt préféré qu'elle ne le fasse pas, vu à quel point son regard semble attendre de moi."


"C'est chez elle et je suis un intrus, bien que je sois toléré. Malgré ça, elle attend toujours que je dise quelque chose."


"Si seulement je savais quoi."

"…"


"Le silence empli de lumière me pousse à prendre une décision."


"Je suis venu ici sans vraiment penser à ce que je ferais, à part délivrer le court message de Nomiya au cas où Rin serait ici."


"Elle est là, et maintenant je ne sais pas ce que je veux dire d'autre... qu'est-ce que je devrais dire ?"


"Je suis tiraillé entre mes deux options à ce moment."


"Que Rin soit troublée me trouble aussi. C'est une révélation surprenante, presque autant que quand je me suis rendu compte qu'elle était vraiment troublée."


"Rien de ce que je peux faire n'aiderait, et je pourrais être partiellement à blâmer aussi."


"Est-ce que ça veut dire que je ne dois pas m'occuper d'elle ?"


"Je ne pense pas."


hi "Alors... qu'est-ce qui ne va pas ?"

"…"

show rin relaxed_nonchalant
with charachange


rin "Rien."


"Elle commence à se retourner, comme pour essayer de fuir physiquement la conversation qu'elle ne veut pas avoir."


hi "Rin, arrête d'essayer de m’éviter ou je vais partir."

show rin relaxed_boredom
with charachange


rin "D'accord."


hi "Tu veux que je parte ?"

show rin relaxed_doubt
with charachange


rin "Tu es toujours en colère ?"


"Il nous a fallu - ou était-ce juste moi ? - dix secondes pour que la conversation en arrive là."


"J'aimerais pouvoir effacer le passé, ou à défaut, l'oublier."


"J'ai rêvé de ça plus d'une fois ces derniers mois."


hi "Mettons ça de côté pour l'instant, d'accord ?"

show rin basic_absent
with charachange


rin "Si tu le dis."


hi "Oui. Donc... quoi de neuf ?"


hi "Sae et Nomiya n'étaient pas trop contents que tu te sois enfuie hier."


hi "Tu les as laissés à un moment délicat et j'imagine que le professeur voulait une explication."


hi "On dirait que tu as jeté tout ce pour quoi tu as travaillé. Et je ne comprends pas pourquoi."

show rin basic_deadpanupset
with charachange


rin "J'ai fait une erreur ?"


"Ma réprimande et sa réponse plate vont tellement à l'encontre des attentes habituelles lors d'une conversation que ça pourrait tout aussi bien être quelqu'un d'autre en train de parler."


"Aucun de nous n'est comme nous étions au début ; ce sentiment de sécheresse que j'ai à chaque fois que je regarde Rin semble aujourd'hui se refléter dans son propre comportement."


"Je déteste les choses qui tournent mal sans possibilité de se rattraper. Depuis février, j'ai détesté ça."


"Que puis-je dire ?"


"Sa question est suivie par un regard interrogateur, inévitable, qui me fait soupirer et froncer les sourcils."


"Les conversations que personne ne veut sont les pires."


hi "Je ne sais pas. Je veux dire, ce n'est pas la fin du monde mais c'était probablement assez bête."

show rin relaxed_nonchalant
with charachange


"Elle répond avec un soupir à son tour, bien que le sien ne soit pas aussi lourd que le mien l'était."

show rin relaxed_sleepy
with charachange


rin "J'ai juste pas pu."


hi "Mais... pourquoi ? Qu'est-ce qui ne va pas ?"

show rin negative_annoyed
with charachange


"Une pause, un sourcil froncé, une voix calme."


rin "Laisse tomber, Hisao."


rin "Je ne crois pas pouvoir vraiment expliquer d'une façon qui serait compréhensive."


"Ouais, Rin non plus ne veut pas avoir cette conversation. Ça peut-être mieux comme ça."


"Mais c'est rare de sa part, d'admettre qu'elle a des sortes de limites."


"J'ai toujours pensé que Rin était tout sauf ignorante de sa tendance à se laisser distraire, tellement qu'elle obscurcit par inadvertance tout ce qu'elle dit."

"…"


hi "Tu n'expliques jamais {b}rien{/b} d'une façon qui serait compréhensive."

show rin basic_absent
with charachange


rin "Personne d'autre ne m'a jamais demandé de le faire."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve


n "C'est comme ça alors."


n "Mais j'ai toujours voulu te comprendre, découvrir qui tu es."


n "Je le veux toujours, tu ne vois pas ?"

n "…"


n "Je sais que tu ne peux pas."


n "Mais moi si."


n "C'est pour ça que je continue ? Ça te fait aussi mal à toi qu'à moi. Il est peu probable que ce soit utile à l'un de nous deux."


n "Nous avons fait et dit des choses qui ne peuvent plus être retirées."


n "C'est comme si... quand nous sommes proches l'un de l'autre, nous nous faisions mal mutuellement, mais nous continuons quand même de le faire."


n "Ce n'est pas idiot ?"


n "Même maintenant, je peux voir comment tu te forces à répondre, même si tu ne me dois rien."


n "Même si c'est difficile de parler de choses comme ça."


n "Pourquoi ?"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear
window show


hi "Pourquoi est-ce que tu peins ?"

show rin basic_awayabsent
with charachange


rin "Je... parce que je ne sais pas ce que je pourrais faire d'autre."


rin "C'est comme si j'avais l'impression de ne pas avoir le choix, qu'il n'y avait pas d'autre possibilité."

show rin basic_sad
with charachange


rin "Comme quand il n'y a que des sucettes goût pastèque dans le magasin et que tu as besoin de manger une sucette."


"Sa pauvre métaphore mise de côté, elle ne m'a pas vraiment répondu. Ça paraît encore moins logique que de ne pas savoir."


hi "Mais... si tu ne veux pas peindre..."

show rin negative_spaciness
with charachange


rin "Ce n'est pas ça. Tu as dû venir dans cette école même si tu n'as probablement pas voulu avoir une crise cardiaque."

show rin negative_annoyed
with charachange


"Elle s’arrête, fronçant les sourcils comme si quelque chose qu'elle avait dit ne lui avait pas plu."

show rin basic_lucid
with charachange


rin "Du moins je crois que tu n'aurais pas voulu."


"Sa phrase est suivie à son tour par une autre plus courte pause,puis par un plus petit froncement de sourcils."

show rin basic_deadpanupset
with charachange


rin "Tu aimerais avoir une crise cardiaque ?"


hi "Non, je ne voudrais pas et ne voulais pas."

show rin basic_deadpansurprised
with charachange


rin "Mais tu vas bien, non ? Ou tu es toujours triste à cause de ça ?"


"La question de Rin me fait réaliser que je n'ai pas vraiment pensé à ma maladie depuis quelques semaines."


"À part ingurgiter mes médicaments chaque jour, je n'ai pas eu besoin de m’inquiéter de mon cœur endommagé, ce qui est agréable, vraiment."


"Connaître de nouvelles personnes, une nouvelle école, une nouvelle ville... une nouvelle vie, tout ceci m'a occupé et le passé s'est effacé."


hi "Non... bah, j'imagine que je ne peux pas continuer de vivre indéfiniment dans le passé."

show rin basic_awayabsent
with charachange


rin "Tu vois ? Même les pastèques ne sont pas mauvaises si tu dois les manger."


"Sa conclusion à moitié absurde semble mettre un terme au sujet dans l'esprit de Rin, alors je me contente de hocher la tête, incertain."

"…"

"…"


"Il y a deux types de silences : ceux gênants que l'on veut briser, et ceux confortables qui ne dérangent pas."


"Le premier type est mauvais, parce que tes pensées partent de travers. Comme les miennes, en ce moment."


"Regarder Rin me met mal à l'aise."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve


n "\nJe ne veux pas ressentir ça."


n "Regarder Rin me fait me sentir... épuisé. J'ai vraiment essayé de mon mieux, elle a essayé de... je n'en ai aucune idée."


n "Mais on a fini comme ça, et elle a fini par foirer le vernissage de son exposition."


n "J'ai l'impression que c'est sans issue."


n "Il n'y a aucune direction dans laquelle continuer."


n "J'ai essayé de l'atteindre hier, pensant que ça serait la dernière fois."


n "Elle est partie."


n "“Je veux être moi.”"


n "Qu'est-ce que ça veut dire ? Rin, plus que n'importe qui, est elle-même."


n "Je me sens quelque peu rassuré de ne pas être celui à blâmer, mais ça me trotte toujours dans la tête."


n "Pourquoi est-ce qu'elle s'est enfuie ? Ce n'était pas logique hier. Ce n'est pas logique aujourd'hui."


n "Les choses qu'elle a dites semblaient avoir du sens, mais elles n'en ont pas pour moi."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear
window show


hi "Tu sais, à propos de ce que tu viens de dire..."

show rin basic_absent
with charachange


rin "De quoi ?"


hi "Hum... de peindre... Sae m'a dit quelque chose comme ça avant... qu'un vrai artiste ne peint pas parce qu'il le veut, mais parce qu'il le {b}doit{/b}."


hi "Et j'ai réfléchi à ce qu'elle a dit, pourquoi est-ce que les artistes {b}doivent{/b} peindre ?"


"Ma question est probablement assez idiote. Du moins Rin me regarde avec des yeux vides qui semblent l'affirmer."

show rin basic_deadpannormal
with charachange


rin "Je ne sais pas. Je suis une artiste ?"


hi "Eh bien, tu peins des trucs et tu as même eu une exposition. Je dirais que tu es qualifiée."

show rin basic_deadpancontemplation
with charachange


rin "Je crois que je sais toujours pas, mais d'accord."


"La pause qui s'ensuit, durant laquelle elle réfléchit, semble durer une demi-éternité."


"Contrairement à la plupart des gens, Rin ne ponctue pas ses pensées par des mots comme “mmh” ou “euh” ou quoi que ce soit."


"J'ai remarqué que je préfère peut-être comme ça."


"La façon de faire des gens m’énerve, comme si les gens étaient si épris par le son de leur propre voix qu'ils doivent continuer à faire du bruit même quand ils sont juste en train de penser à ce qu'ils pourraient dire ensuite."


"Rin juste... s’arrête complètement quand elle réfléchit. C'est déconcertant, parce que réagir devant les gens qui rêvassent est toujours difficile, mais elle s’avère moins pénible."

show rin basic_lucid
with charachange


rin "Je crois que je veux que quelqu'un voie ce qu'il y a à l'intérieur de moi. Pas à la façon des docteurs et des tueurs en série."

show rin basic_absent
with charachange


rin "La façon qui ne me fait pas sentir seule."

show rin relaxed_boredom
with charachange


rin "C'est ce que tu appelles métaphorique, tu vois."


hi "Ne me fais pas la morale pour des choses évidentes."

show rin basic_deadpansurprised
with charachange


rin "C'est pas évident que c'est évident."


hi "Donc, tu présentes une peinture à quelqu'un et espères qu'il ait, comme par magie, un aperçu de ton âme ?"

show rin negative_angry
with charachange


rin "Ce n'est pas ça. C'est un peu comme ça mais pas vraiment. Tu ne comprends pas ?"


hi "Je comprends... et ne comprends pas."


hi "Tu sais, je me sens un peu désespéré à chaque fois que tu poses cette question."

show rin basic_absent
with charachange


rin "Quelle question ?"


hi "À propos du fait que je te comprenne ou pas."


"Elle semble presque surprise par mes éclaircissements."

show rin basic_lucid
with charachange


rin "Oh, ce n'est pas vraiment une question. C'est une du genre où tu n'as pas besoin de répondre."


hi "Rhétorique."

show rin basic_absent
with charachange


rin "Ouais, c'est le mot, une question qui n'est pas une question est une question rhétorique. C'est cool."


rin "Ça me rappelle, ce n'est pas vraiment logique. Quel genre de question n'est pas une question ?"


hi "Une question rhétorique."


rin "Quel genre de réponse est une réponse qui ne répond à rien ?"


hi "C'est une question rhétorique ?"

show rin basic_deadpanupset
with charachange


rin "Tu n'es pas drôle."

show rin basic_awayabsent
with charachange


rin "Mais si tu n'aimes pas ça, tu ne voudrais pas que je dise quelque chose d'autre à la place ?"

show rin basic_lucid
with charachange


rin "Je n'en ai pas de bonnes cela dit. Tu penses quoi de... “Ton pantalon est en feu” ?"

show rin basic_absent
with charachange


rin "Ça pourrait être notre langage secret."


"Le ridicule sincère de Rin, rendu deux fois plus ridicule par le fait que je sais qu'elle est tout à fait sérieuse, me perturbe comme à chaque fois."


"C'est comme un cran de sûreté pour m'empêcher de devenir un inquiet maladif, gardant les pieds sur terre, là où ils devraient être."


"Je souris maladroitement, mais seulement à l'intérieur."


"Même si les coins de ma bouche n'affichent pas ce sourire, je suis toujours impressionné par la facilité avec laquelle elle détruit toute tentative d'être trop sérieux."


"Pourrait-elle (ou va-t-elle) oublier et ignorer les choses qui la tracassent, les choses qui l’embêtent ?"


"Pourrait-elle être(ou sera-t-elle) libre du fardeau d'être elle-même ?"


"Ou suis-je le seul qui se sent accablé en étant lui-même ?"


hi "Non merci."


hi "Mais pourtant, les fois où j'ai l'impression d'être sur la même longueur d'onde que toi sont rares."


hi "J'ai l'impression... qu'il y a un grand fossé et parfois tu vas de l'autre côté, et je n'ai... pas de moyen de t'atteindre de là où je suis."


hi "C'est comme si tu étais dans un endroit complètement différent parfois."


hi "Même si tu es juste là."


"C'est vrai."


"Il y a une discontinuité insurmontable, un mur de glace imaginaire qui bloque toute compréhension."


"Il peut toujours y avoir un fossé entre deux personnes, mais avec Rin, ça paraît plus tangible."


"Rin ne réagit pas à mes pensées, ni celles que je formule à voix haute ni celles que je garde pour moi."


hi "C'est encore pire avec l'art."


hi "Je ne suis pas très doué en art, je l'admets."


hi "J'ai rejoint le club d'art parce que je pensais que ça pourrait être intéressant."


hi "Et ça l'est, je crois. J'aime l'art, j'aime ton art aussi, mais juste comme avec toi, je ne peux pas le comprendre."


hi "Et je suis assez confiant pour dire que personne ne peut vraiment."

show rin relaxed_doubt
with charachange


"Ça semble l’inquiéter légèrement."


rin "Tu penses ?"


hi "Ouais. J'imagine que l'art est fait pour être interprété, pas compris. C'est comme ça que je le vois."

show rin relaxed_sleepy
with charachange


rin "C'est une pensée triste."


hi "C'est bien possible."


hi "Est-ce que ça te rend triste pour toi-même ?"

show rin basic_lucid
with charachange


"Rin réfléchit pendant un moment, puis secoue la tête avec une énergie surprenante."

show rin basic_deadpannormal
with charachange


"La première chose sur laquelle elle concentre son regard après ça, c'est moi."


"Ces deux choses me font plaisir, et me rassurent."


hi "C'est bien, non ? Bref, tu devrais aller voir le professeur et t'excuser."


hi "Je crois qu'il est inquiet pour toi."


hi "Peux-tu faire ça ?"

show rin basic_absent
with charachange


"Cette fois, elle hoche la tête."

stop music fadeout 4.0


"Seulement, ce n'est pas aussi énergique."


label fr_R39:

scene bg school_hallway3
with locationchange


"Le couloir est vide, presque intimidant."


"Le “bureau” de Nomiya est la classe d'art à l'autre bout du couloir du troisième étage."

show rin basic_absent at center
with charaenter


"Nos pas résonnent d'une façon inquiétante. L’atmosphère est différente d'un après-midi normal. J'ai l'impression que l'école sait que personne ne reviendra pendant un mois, aussi."


"La porte est ouverte, mais pas très accueillante."


hi "Je vais... hum, attendre à l'extérieur."


show rin relaxed_nonchalant
with charachange

with Pause(0.2)

show rin invis at tworight
with dissolvecharamove

hide rin
with None


"Hochant la tête d'une façon à peine visible, Rin avance sans s’arrêter, et naturellement, sans frapper."


"Peut-être que c'est pour ça qu'il faut quelques secondes avant que je puisse entendre la voix du professeur de l'intérieur."


no "Te voilà !"


rin "Bonjour."


"Un conflit s'installe en moi : devrais-je rester là ou aller ailleurs ?"


"Je ne suis pas sûr d'avoir envie de les espionner comme ça."

"…"

show bg school_hallway3 at right
with charamove


"Les bonnes manières perdant face à la curiosité, je reste assez proche pour les écouter."


"Leurs voix résonnent dans le couloir, mais ça importe peu."


"Il n'y a personne d'autre ici à part moi."

play music music_tragic fadein 8.0


no "Ma chère fille, mais à quoi tu pensais, en partant comme ça le grand soir ?"


rin "Je ne pouvais rien dire."


"Comparé au ton de réprimande de Nomiya, Rin semble vraiment silencieuse et renfermée."


"Ses mots semblent s'effacer sous les siens."


no "Je dois dire, je suis très déçu par toi, Tezuka."


rin "C'était pas bon du tout."


no "Sans compter tout ce que j'ai fait pour toi, tu as pensé à Sae ? Et à tous les invités qui voulaient te rencontrer ?"


rin "Il n'y avait personne. Même Hisao..."


no "Tu nous as vraiment embarrassés, Tezuka."


no "La réputation, ça compte énormément, tu le sais j'imagine ?"


rin "C'est pas grave. Je n'en ai pas besoin."


no "“Pas besoin !” D’où est-ce que tu sors ça ?"


"Les réponses de Rin semblent énerver le professeur encore plus, sa voix s’élevant à chaque phrase."


no "Le chemin d'un artiste est tortueux, je te le dis ! Tortueux !"


no "Tu dois voir en grand ! Il y a des bons moments et des mauvais moments !"


rin "Les choses sont comme elles sont. Je m'en sortirai même—"


no "Tu pourrais penser maintenant que c'est beau et facile, mais jusqu’où est-ce que tu aurais été sans moi ?"


no "Je ne serai pas toujours là pour toi !"


no "Quand tu seras allongée sur le sol de ta minuscule chambre, tes trois semaines de loyer en retard, ton esprit vide pour la quatrième semaine d'affilée, alors tu souhaiteras avoir écouté un peu plus le vieux Nomiya."


no "Quand tu continueras de regarder l'ombre de ta chaise s'allonger sur le sol parce que c'est tout ce que permet ta léthargie, peut-être que tu commenceras à t’inquiéter de ta carrière !"


rin "Ça importe peu."


no "Ta volonté ne suffit pas."


rin "Je ne suis pas une personne volontaire."


no "Tu n'es pas une personne volontaire..."

play sound sfx_impact2
with vpunch


no "Alors dis-moi, pourquoi... pourquoi... POURQUOI EST-CE QU'ON A FAIT TOUT ÇA SI C'EST POUR DU PIPI DE CHAT ?"


"Oh mince, le professeur a pété un plomb."


"L'entendre crier sur Rin me fait me sentir coupable d'être resté dehors. Si je l'avais accompagnée, peut-être qu'il ne se serait pas autant énervé."


"Si je ne l'avais pas laissée s’enfuir, il n'aurait pas été aussi en colère en premier lieu."


"Je pourrais toujours y aller et la sauver... Je ne crois pas pouvoir."


"J'ai fait pareil. J'ai crié sur Rin aussi, et je me sens encore plus embarrassé à cause de ça maintenant."


"Je me sentais dans mon droit en lui faisant subir ma colère parce que... juste parce que je sentais que c'était de sa faute si j'étais si frustré."


"Ce n'était pas plus justifié que la colère du professeur."

"…"


"Un terrible silence s'installe dans le couloir."


"Rin n'a rien à dire à Nomiya."


"Qu'elle soit arrivée à court de réponses, ou qu'elle sache qu'argumenter ne ferait que l'énerver encore plus, n'est qu'un détail."


"Le professeur n'a rien de plus à dire non plus, on dirait, ou peut-être qu'il est juste à bout de souffle."


"Pendant un moment, je les imagine tous les deux en train de se fixer du regard, l'un rouge comme une tomate et l'autre... comment, tiens ?"


"Je ne peux pas dire comment se sent Rin. Ni avant, ni maintenant."


"Le professeur semble attendre que Rin dise quelque chose aussi, mais puisqu'elle ne le fait pas, il recommence à parler avec une voix plus basse, moins énervée."


no "Quel était l’intérêt de faire tout ça s'il n'en ressort... rien ?"


"Là encore, Rin ne dit rien."


no "Je suis désolé. Je n'aurais pas dû m'emporter."


"Il ne semble pas désolé du tout. Au lieu de ça, son ton est froid et sec, comme s'il crachait les mots au lieu de les dire."


no "On dirait que j'attendais trop de toi. Tu n'es pas une artiste après tout."


"Ouais, pas désolé du tout."

show nomiya serious:
    tworight
    alpha 0.0
    parallel:
        linear 1.0 center
    parallel:
        linear 0.4 alpha 1.0
        0.2
        linear 0.4 alpha 0.0
with Pause(1.0)

stop music fadeout 4.0


"Il déferle hors de la salle du club et descend les escaliers sans me remarquer."


"Après qu'il soit parti, je jette un coup d’œil prudent dans la classe."

scene bg school_nomiya at right
show rin basic_awayabsent at center
with locationchange


"Rin se tient debout là, devant le bureau du professeur."

show rin negative_spaciness
with charachange


rin "Je n'ai pas pu dire que j'étais désolée."


"Elle dit ça à l'air humide de la classe, pas à moi."


"Mais puisque la pièce ne semble pas lui répondre, je vais le faire."


hi "C'était injuste de sa part... Il était en colère, mais quand même..."


"Je n'arrive pas à décider comment finir ma phrase. Dédaigner le professeur serait comme dédaigner ma propre attitude d'il y a deux jours."


"Stupide, mais correct quand même."

show rin negative_spaciness_close
with characlose


"Rin ne répond pas, restant pétrifiée sur place, alors je vais jusqu’à elle."


"Elle a tenu sa position. Tant bien que mal. Je ne m'y attendais pas."


"Je n'arrive pas à déterminer si c'est inconvenant ou non, mais dans tous les cas, elle l'a fait."


"Avec moi, elle ne l'a jamais fait."


"J'aurais bien aimé qu'elle le fasse, peut-être que je ne me sentirais pas aussi mal."


"Récemment, je me suis mis à souhaiter ce genre de choses."


hi "Rin ?"

show rin negative_annoyed_close
with charachange


rin "Va-t'en."


label fr_R40:

scene bg school_nomiya at right
show rin negative_annoyed_close at center
with None

play music music_sadness fadein 6.0


hi "Pourquoi... qu'est-ce que tu dis ?"

show rin negative_angry_close
with charachange


rin "Tu es en colère contre moi aussi, hein ?"


rin "Je croyais que tu étais mon ami. Je croyais qu'il l'était, aussi."


"Sa voix est différente de ce que j'ai pu entendre jusque-là, elle est amère, tranchante comme un rasoir, et Rin continue de regarder ses pieds."


hi "Je ne crois pas que ça soit la question."


hi "Il voulait que tu sois quelque chose que tu n'es pas. Et..."

show rin basic_surprised_close
with charachange


"Je prends une grande inspiration et finalement croise son regard, ne le lâchant plus."


hi "...Je suis désolé. Je voulais qu'on soit quelque chose d'autre... plus que des amis."


hi "Peut-être que c'est pour ça que je n'ai pas pu me retenir et que je suis devenu aussi frustré, tout comme le professeur."

show rin relaxed_doubt_close
with charachange


rin "Quoi de plus ? Il n'y a rien de plus de moi que moi, c'est tout ce que je suis. Je ne comprends pas ça."


"Eh bien... la réponse devrait être évidente, non ?"


"Je me rappelle quand je réfléchissais sur le principe de l'amitié. D'être là pour toutes choses à tout moment, d'être là pour son ami."


"Est-ce que j'ai échoué en étant qu'ami, pensant que ça pourrait être une marche vers une autre étape ?"


"Peut-être qu'à cause de ces pensées, je n'ai pas réussi à gérer tout ça, à garder mon calme."


"Aussi outrageuse que Rin puisse être, je n'aurais pas dû me laisser avoir par ça, surtout quand j'ai commencé à ressentir ce que je ressens à son égard."


"Donc, ai-je échoué ?"


"C'est ce que ses yeux semblent demander."

"…"


hi "Je suis désolé, Rin."


hi "Je pourrais ne plus être capable d'être ton ami."


hi "Je ne pense pas que je puisse être un bon ami pour toi."


"Je dis ces choses parce qu'elles sont vraies, pas parce que l'un de nous aimerait les entendre."


"Mais ces choses doivent être dites."


"Le caractère définitif de mes mots crée un silence vibrant, mais qu'est-il possible d'ajouter à ça ?"

"…"

show rin negative_confused_close
with charachange


rin "Pourquoi ? Pourquoi est-ce que tout ça arrive ?"

show rin negative_sad_close
with charachange


rin "Les gens font des choses que je n'ai pas demandées et ne veux pas et tout le monde continue d'être en colère contre moi, je n'ai aucune idée de ce qui se passe maintenant et je ne peux pas m’empêcher de penser que je veux tout fuir..."

show rin basic_lucid_close
with charachange


"Elle ferme les yeux, fort, et respire à fond, calmement."

show rin basic_upset_close
with charachange


"Quand elle rouvre les paupières, tout ce que je peux voir est un désespoir vert foncé."


rin "{b}Je n'ai aucune idée de ce qui cloche chez moi !{/b}"


"Son explosion frénétique me stupéfie pendant un moment, et pendant un battement de cœur nous nous regardons l'un l'autre."


"Voir son regard confus cherchant désespérément des réponses dans le mien me rend triste, parce que je sais que je n'en ai pas."


hi "Je ne sais pas non plus."


hi "Mais tu sais, tu as dit toi-même que les choses ne sont ni bonnes ni mauvaises."


hi "Elles sont, tout simplement."


hi "Soit tu les acceptes, soit tu fais en sorte de les changer, soit tu abandonnes."


hi "Ce n'est pas que je te déteste, ou que Nomiya te déteste."


hi "C'est juste que... je pense que je suis le genre de personne qui abandonne quand il pense qu'il ne peut plus continuer."


hi "Et même si tu détestes ça, c'est... c'est... comme ça que sont les choses."


"Je dis des choses assez cruelles mais je ne peux pas m’arrêter, les mots continuent de glisser sur ma langue avec un ton dur et certain."

show rin basic_surprised_close
with charachange


"Je peux les voir frapper Rin presque comme des vrais coups."


"Alors que l'humidité se rassemble au coin de ses yeux, ils sont toujours écarquillés sous l'effet du choc."

show rin basic_crying_close
with charachange


"Alors que des larmes commencent à rouler sur ses joues pâles, elle ne fait rien pour les arrêter."


"Alors qu'elles tombent au sol une par une, elle se tient debout, me fixant du regard avec les yeux vides, comme si elle n'y croyait pas."

rin "…"


"Mais la réalité reprend le dessus."

show rin negative_crying_superclose
with vpunch


"Rin se laisse aller en avant comme si elle se ramollissait et enfouit son visage dans ma chemise aussi fort que possible."


"Rin est légère comme une plume à soutenir."


"Elle ne sanglote pas vraiment, elle est juste contre moi, laissant ses larmes traverser ma chemise et atteindre ma peau en dessous."


"Et je la laisse, mettant ma main autour de ses épaules dans une étreinte maladroite qui ne sert à rien pour la réconforter."


"Je peux sentir les vertèbres de Rin sous mes doigts, comme un rappel dur et irrégulier que les choses ne vont pas bien."


"Sa mince épaule tremblant contre ma paume est un spectable pitoyable, et le désespoir d'être en partie la cause de la tristesse de Rin me brise le cœur."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve


n "\n\n\n\nFaire pleurer une fille est la chose la plus déplorable qui soit."


n "\nMême Rin. Surtout Rin."


n "\nDerrière ce voile d’étrangeté, Rin est une humaine comme les autres."


n "Tout aussi confuse, effrayée et perdue que n'importe lequel d'entre nous."


n "La plupart du temps on dirait qu'il n'y a ni ordre ni raison dans ce que dit et fait Rin, mais pour une fois, je crois que je comprends vraiment ce qu'elle ressent."


n "\n\nMais aucun mot ne peut l'exprimer, tout comme aucun mot ne peut arranger ça."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear

show bg school_nomiya:
    "bg school_nomiya_ss" with Dissolve(8.0)
show rin negative_crying_superclose:
    "rin negative_crying_superclose_ss" with Dissolve(8.0, alpha=True)
with None

stop music fadeout 5.0


n "\n\n\n\n\nDonc sans dire un mot nous restons là, en silence, à attendre que ses larmes sèchent."


n "Le temps passe lentement à en mourir, même les particules de poussière flottant dans l'air semblent rester immobiles."


n "L'horloge murale obligatoire tique distraitement au-dessus de la porte."


n "Je décide de ne pas compter les secondes, parce que ça ferait paraître le temps plus long."

n "\n\n…"

play music music_serene fadein 9.0

nvl hide dissolve
nvl clear

show rin basic_crying_superclose_ss
with charachange

window show


"Au bout d'un moment, Rin remue un peu et reste blottie contre ma poitrine, murmurant dans ma chemise."


rin "Laisse-moi rester comme ça un moment."

show rin negative_crying_superclose_ss
with charachange


rin "S'il te plaît Hisao."


rin "Laisse-moi un petit moment comme ça."


"Un déluge de pensées se répand dans mon esprit ; le fait de savoir qu'être là pour Rin est tout ce que je peux faire pour elle, que c'est tout ce qu'elle veut en ce moment, malgré ce qu'on a vécu."


hi "Bien sûr."


"Donc elle reste là."


"Mais je n'arrive toujours pas à me résoudre à la coller plus contre moi pour pouvoir la serrer plus convenablement dans mes bras."


"C'est parce que le faire me rendrait tellement triste que je ne sais pas si je pourrais le supporter."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve


n "\n\nLa prise de conscience que nous pourrions ne jamais vraiment être en mesure de devenir ce que nous voulons être pour l'autre se cristallise dans mon esprit comme une découverte dure comme le diamant."


n "Je ressens des pointes au cœur comme un choc électrique."


n "C'est douloureux."


n "La situation claire... me fait mal."


n "Que pouvons-nous faire l'un pour l'autre ? Quel est l'intérêt de nous accrocher si désespérément l'un à l'autre, même si tout ça semble si futile ?"


n "Qu'est-ce que je devrais dire à Rin ? Comment la réconforter ?"


n "Je n'ai aucune de ces réponses, et j'ai peur que les connaître ne me fasse que plus mal."


n "De force, je sors tout cela de mon esprit parce que je ne veux pas penser aux vérités blessantes."


n "Mes pensées calmées, la tristesse se disperse jusqu’à que seuls restent Rin et moi et cette tendre sensation de chaleur et de douceur contre ma poitrine."

nvl clear


n "\n\nQuand est-ce que je suis tombé amoureux d'elle ?"


n "Je n'arrive pas à me rappeler, mais je suis certain que c'était bien avant le contact de ses lèvres sur les miennes, durant cet après-midi orangé où elle était malade et que je suis allé la voir pour des raisons peu claires."


n "Son attitude insouciante, l'impression d’étrangeté autour d'elle, toutes les choses qui font que Rin est Rin... ces choses m'ont capturé avec une force irrésistible."


n "La façon qu'elle a de tout prendre et d'estimer chaque élément à sa manière, pesant toutes les choses de façon juste et sans préjugés, de voir le monde comme elle le veut."


n "C'est quelque chose que je ne pourrais jamais faire, et Rin était probablement plus une muse pour moi que je l'étais pour elle."


n "Elle me semblait si libre, l'esprit toujours au-delà. Pendant que moi, m’inquiétant constamment de tout, je semblais tellement inhibé que ça en était presque embarrassant."


n "Peut-être que c'est pour ça que me suis autant focalisé sur Rin, essayant de rentrer dans son monde qui était tellement différent de ma morne vie."

nvl clear


n "\n\nAvant que je puisse le remarquer, cette irrésistible force m'avait tiré dangereusement près d'elle, mais il s'est avéré que c'était trop différent pour moi."


n "Et j'avais oublié Newton, en plus de ça."


n "La force gravitationnelle est inversement proportionnelle au carré de la distance entre les objets..."


n "Donc si deux personnes ressentent quelque chose l'une pour l'autre..."


n "Bah."


n "Même si les sentiments ne sont pas gouvernés par les constantes de l'univers, je ne peux pas m’empêcher de penser depuis un moment que j'ai été un satellite tournant autour de la planète brillante de Rin."


n "\nPlanète Rin."


n "\nLa pensée me fait presque rire, elle semble vraiment venir d'une autre planète parfois, sauf la peau verte et éventuellement quelques tentacules."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

show rin negative_sad_close_ss
with charadistant

window show


"Peut-être à cause de mon rire étouffé, Rin se recule et je relâche ma prise, ressentant le froid maintenant que sa chaleur est partie, et légèrement embarrassé pour avoir laissé mes pensées s'emballer comme ça."


"Je me dis que c'est juste dû à une mauvaise influence de Rin sur moi, mais je suis quand même content qu'elle ne puisse pas lire dans les pensées pour de vrai."


"Les larmes de Rin ont séché, et elle semble être redevenue un peu elle-même maintenant."

show rin basic_sad_close_ss
with charachange


"Son air perdu est toujours là cela dit. Son regard se promène nerveusement avant de s'arrêter sur moi."


rin "Qu'est-ce qui vient de se passer ?"


rin "Tu peux me dire ?"


hi "Quoi ? Comment ça ?"

show rin basic_upset_close_ss
with charachange


rin "J'ai pleuré."


"Elle dit ça, hésitante, comme si elle n'y croyait pas elle-même."


hi "Oui..."

"…"


"Elle continue de me regarder, comme pour demander des explications pour ne pas se sentir si perdue."

"…"

show rin basic_sad_close_ss
with charachange


rin "Pourquoi ?"


hi "Tu étais triste ?"


hi "C'est ce que tu veux que je te dise ? Mais ce n'est pas évident ?"

show rin negative_confused_close_ss
with charachange


rin "Je ne sais pas. Ça fait bizarre de pleurer."


hi "Quoi ? J'y crois pas. Je veux dire, tout le monde fait ça. C'est nor—"


"Je me mords la langue avant de finir mon argument à propos de la normalité."


"Les normes ne s'appliquent pas pour la personne à qui je parle."

show rin negative_worried_close_ss
with charachange


rin "Ça semble toujours tellement faux, différent de ce qui est en moi. Comme si je ne pouvais pas vraiment dire ce que je ressentais."


rin "Alors j'ai commencé à penser que peut-être je ne savais pas ce que je ressentais. Peut-être que c'était moi qui n'allais pas—"


rin "J'ai pensé ce genre de choses."

show rin negative_sad_close_ss
with charachange


rin "Je pensais... que peindre serait suffisant parce que j'avais l'impression d'au moins bien faire ça."


rin "Que tout ce qui est à l'intérieur de moi pouvait devenir une image si j’essayais vraiment fort. Et c'est le cas."


rin "Mais je n'ai plus l'impression que c'est suffisant maintenant. Parce que si personne d'autre ne peut voir ça comme ça, je serai toujours seule."

show rin basic_absent_close_ss
with charachange


rin "C'était une mauvaise idée d'essayer ? Tout le monde s'est vraiment énervé contre moi pour avoir fait ça."

stop music fadeout 6.0


"J'ai rarement entendu Rin parler autant d'un coup."


"Une fois qu'elle a fini, elle se tait simplement, semblant si normale qu'il est difficile de croire qu'elle a dit ce qu'elle vient de dire."


"Je ne sais pas quoi en penser."

"…"


"Rin voulait désespérément que quelqu'un regarde ses peintures, et en quelque sorte voie son âme à travers elles, pour comprendre ses sentiments..."


"Parce que... elle ressentait qu'elle ne pouvait pas les exprimer d'une autre façon ?"


"Comment quelqu'un pourrait dire si c'est bien ou mauvais ?"


"Se pourrait-il que tout ce temps elle ait cherché un moyen de m'atteindre tout comme j'ai essayé de l'atteindre ?"

"…"


"Je m'assieds sur un bureau pour réfléchir, et pour reposer mes jambes qui nous ont tenus tous deux debout pendant un moment."

play music music_innocence fadein 12.0


hi "Tu sais, quand je lis un bon livre ou regarde un ciel étoilé ou peu importe, quelquefois moi aussi je ressens quelque chose de... profond, comme un... zut, je ne sais pas comment le décrire."


hi "Mais à l'instant où j'essaye de décrire ça avec des mots, j'ai l'impression que je perds quelque chose, ça ne semble pas aussi réel, aussi vrai qu'à l'intérieur de ma tête."


hi "Ça sonne un peu faux. Ha, même ce que je viens de dire sonne un peu faux."


"J'affiche un sourire qui est censé être entre amusant et moqueur, mais Rin ne réagit pas."


hi "Bref..."


hi "C'est peut-être que personne ne peut jamais exprimer ses vrais sentiments face aux autres personnes."


hi "La réalité n'a aucune chance face à ce qu'il peut y avoir dans la tête de quelqu'un."


hi "Rien ne peut changer ça. Pas même tes peintures, sauf peut-être pour toi-même."


hi "Mais j'imagine que tu ne peux pas tout garder à l'intérieur, tu exploserais sinon."


hi "Ce que j'essaye de dire est que... je ne pense pas que ce soit une mauvaise chose d'exprimer ses sentiments, même si tu utilises la peinture comme catalyseur."


hi "Tu ne peux pas juste t'attendre à ce que les gens te comprennent mieux que si tu l'avais fait d'une autre façon."


hi "En fait, tu ne peux pas t'attendre à ce que les gens te comprennent."


hi "C'est parce que tout est vraiment subjectif. Tu vois le monde à ta façon, mais c'est différent pour tout le monde."

show rin basic_sad_close_ss
with charachange


rin "C'est pas horrible ?"


hi "J'imagine que si, d'une certaine façon."

"…"

show rin relaxed_doubt_close_ss
with charachange


"Elle fronce les sourcils, ayant l'air aussi accablée que possible. Ce qui n'est pas beaucoup pour elle, mais suffisamment pour que je comprenne qu'elle n'est pas particulièrement contente."


rin "Je crois que ça me rend triste après tout."


hi "Ouais. Je sais."


hi "J'aimerais pouvoir faire quelque chose pour arranger ça."


"Je ne pense pas sembler amer en parlant comme ça, mais je le suis un peu en vrai."


"C'est mon problème. Je ne peux pas être ce que Rin veut. Et pour la même raison, elle ne peut pas être ce que je veux non plus."

"…"

show rin negative_worried_close_ss
with charachange


"Elle affiche une expression difficile, essayant de choisir soigneusement les mots qu'elle veut dire."


"Donc Rin connaît des moments où il est difficile de dire quelque chose, aussi."

show rin basic_sad_close_ss
with charachange


rin "On n'y peut rien, j'imagine."

show rin basic_absent_close_ss
with charachange


rin "...mais... que tu dises ça..."

show rin basic_awayabsent_close_ss
with charachange


rin "Ça me fait un peu plaisir."

"…"


"C'est drôle comment les choses qui semblent les plus insignifiantes sont parfois les plus importantes à certains moments."


"Comme quand la voix de Rin est très très basse, presque inaudible alors qu'elle dit ça."


"Et comment même ses courtes mèches peuvent couvrir ses yeux quand elle a la tête baissée."

show rin basic_blush_close_ss
with charachange


"Et comment ils ne peuvent pas couvrir le rouge vif sur ses joues et jusqu'au bout de ses oreilles."


"Elles prennent vraiment une nuance très intéressante de rouge."


"Un silence assourdissant s'ensuit."


"C'est très gênant, comme si j'avais vu quelque chose que je n'aurais pas dû voir, même si ce n'était pas volontaire."


"Je ne sais pas quoi dire dans cette situation,mais je continue à me sentir comme si je devais le savoir."


"Elle ne sait pas non plus."


"Pourtant, j'ai l'impression qu'il n'y a pas grand-chose à perdre même si on reste silencieux."


"Comme si on avait une sorte d’étrange connexion qui tiendrait quand même."

show rin relaxed_nonchalant_close_ss
with charachange


"Rin ne cesse de déplacer son poids d'un pied sur l'autre sans arrêt, regardant partout dans la salle, sauf vers moi."


"Elle est celle qui finit par rompre le silence."

show rin basic_deadpan_close_ss
with charachange


rin "On peut y aller ? Je ne veux pas rester là."


hi "Oh, ouais, bien sûr. Où ?"


"Ma réponse couvre ma nervosité aussi difficilement que sa question couvre la sienne."

show rin relaxed_sleepy_close_ss
with charachange


rin "Tu peux aller où tu veux. Je veux dormir. Je n'ai pas vraiment dormi depuis quelques semaines."

show rin basic_lucid_close_ss
with charachange


rin "J'ai l'impression qu'il y a un troupeau de papillons à lumière bleue à l'intérieur de ma tête. Ça fait que j'ai du mal à réfléchir."

show rin basic_deadpannormal_close_ss
with charachange


rin "Le genre qu'on pense trop bleu pour exister, comme la culotte d'Emi ce matin."

show rin negative_spaciness_close_ss
with Dissolve(0.1)

show rin basic_absent_close_ss
with Dissolve(0.1)

show rin negative_spaciness_close_ss
with Dissolve(0.05)

show rin basic_absent_close_ss
with Dissolve(0.05)

show rin negative_spaciness_close_ss
with Dissolve(0.05)

show rin basic_absent_close_ss
with Dissolve(0.05)

show rin negative_spaciness_close_ss
with Dissolve(0.1)

show rin basic_deadpannormal_close_ss
with Dissolve(0.2)


"Elle secoue la tête, et je m'attends presque à ce que quelques papillons Morphos sortent de ses oreilles."

show rin basic_deadpanamused_close_ss
with charachange

"Un léger sourire se dessine aux coins de sa bouche."


rin "Ça me rappelle. Le bleu, pas la culotte."

show rin basic_deadpandelight_close_ss
with charachange


rin "Le mot pour un troupeau de papillons est une nuée. J'ai fait des recherches."


"Je fronce les sourcils d'un air interrogateur."


hi "Pourquoi tu ne l'utilises pas alors ?"

show rin basic_absent_close_ss
with charachange


rin "Je préfère l'autre mot."


"Pourquoi faire des recherches, alors ?"


hi "Pour que tu puisses l'utiliser, non ?"

show rin basic_awayabsent_close_ss
with charachange


"Elle hoche la tête et devient silencieuse, son regard échappant au mien, attiré par l'orange foncé émanant du soleil se reflétant sur les fenêtres."


"Nous restons comme ça pendant un petit moment : moi qui la regarde silencieusement et elle qui regarde silencieusement par la fenêtre."


hi "Hé... tu vas bien maintenant ?"

show rin basic_absent_close_ss
with charachange


"Elle me regarde du coin de l’œil, l'air de nouveau mélancolique. La lumière du soleil dans ses yeux ne trahit plus ses sentiments maintenant."


rin "Je vais avoir besoin d'y penser."


"Je veux continuer cette conversation, continuer de m'accrocher à ces choses dont elle a enfin révélé l'existence."

show rin basic_awayabsent_close_ss
with charachange


"Mais Rin regarde d'un air tellement absent par la fenêtre que je sais qu'elle ne sera pas réceptive de façon cohérente si je continue."


"C'est comme une sorte de mécanisme de défense de sa part, pour éviter d'être sensible."


"Son esprit est comme un papillon, toujours à s'envoler au loin quand il est perturbé."


"Juste quand je pensais que j'arrivais à voir derrière son voile, elle se retrouve hors de ma portée à nouveau."


"Peut-être que c'est juste que Rin est comme ça."


"Peut-être que c'est quelque chose que je devrais accepter pour garder une certaine tranquillité d'esprit."


hi "D'accord."


hi "Je te raccompagne aux dortoirs alors."

show rin basic_absent_close_ss
with charachange


rin "Merci."

show rin basic_lucid_close_ss
with charachange


rin "Vraiment."

stop music fadeout 12.0

scene bg school_hallway3
with locationchange


"Les couloirs vides de l'école me semblent très lugubres."


"Moins d'une heure après le début des vacances d'été, et le bâtiment semble déjà déserté. La seule activité dans l'immobilité des couloirs sont nos pas."


"Le changement est soudain, mais ça montre combien le bâtiment n'est qu'une coquille vide, morte sans ses étudiants et ses professeurs."


"C'est comme si l'école était devenue un monde seulement pour nous deux, un endroit désert, rempli de silence et de poussière de craie."

scene bg school_staircase2_ss
show rin relaxed_sleepy_close_ss at twoleft
with locationchange


rin "Je crois que je dois changer."


"Elle sort ça au milieu de nulle part pendant que nous descendons l'escalier du troisième étage, ayant toujours l'impression qu'elle agit en fonction de ce que je pensais juste avant."


hi "C'est ce que font les gens, parfois."

window hide
nvl clear
nvl show dissolve


n "\n\n\n\n\n\n\n\nC'est la dernière fois que nous nous adressons la parole de la journée, même s'il y avait tant à dire."


n "Et même ces mots s'enlisent dans le lourd silence, disparaissant dans l'air stagnant comme si rien n'avait été dit."

nvl clear
nvl hide dissolve

$ suppress_window_before_timeskip = True

scene black
with dissolve



label fr_R41:

play music music_dreamy fadein 2.0

scene bg school_dormhisao_rn
with charachange

$ renpy.music.set_volume(0.4, 0.0, channel="ambient")
play ambient sfx_rain fadein 1.0


"Le premier jour des vacances d'été est une déception."


"Je me réveille. De l'eau tombe du ciel gris dans des proportions presque bibliques."


"J'étais optimiste à cet instant."


"Une rapide averse d'été, je me suis dit. Des torrents de pluie en quelques minutes, et c'est fini."

show rain normal behind bg
with None


"Pas de chance."

$ renpy.music.set_volume(0.7, 1.0, channel="ambient")

hide bg
show bg misc_sky_rn as bg2 behind rain
show hisaowindow
with locationchange


"La pluie tombe sans arrêt du ciel bleu-gris à l'extérieur, coulant sur ma vitre en formant de petites rivières et ruisseaux qui se rassemblent pour former des lacs miniatures dans la rue."


"Tout comme il l'a fait pendant les deux dernières heures et demie."

$ renpy.music.set_volume(0.4, 1.0, channel="ambient")

scene bg school_dormhisao_rn
with charachange


"Donc je nettoie sans y mettre du cœur, lisant un livre et rangeant mes affaires tour à tour quand l'un des deux m'ennuie."


"Le temps me démoralise pas mal aussi, rendant plus difficile le fait de faire quoi que ce soit convenablement."

play sound sfx_impact2


"Quelque chose frappe assez brutalement contre ma porte, me tirant de mon apathie."


"J’espère que ce n'est pas Kenji et son bowling d'intérieur."

"…"


"Je n'entends plus de bruit venant du couloir jusqu’à ce que j'arrive à la porte et l'ouvre."

play sound sfx_dooropen
$ renpy.music.set_volume(0.2, 1.0, channel="ambient")
stop music fadeout 2.0

scene bg school_dormhallway
show rin basic_absent
with locationchange

"Rin."


"J'aimerais que la voir suscite une certaine émotion en moi, mais de une, je suis trop surpris qu'elle soit venue me voir, et de deux, elle est complètement trempée."


"Sa chemise d'uniforme est trempée et elle est debout dans une flaque qu'elle a créée elle-même."


"Des gouttes d'eau de pluie dégoulinent de ses courtes mèches et glissent le long de son nez jusqu’à tomber depuis le bout."


"Une.{w=0.7} Par.{w=0.7} Une."


hi "Mmh... salut."


hi "Comment tu te sens ?"

show rin basic_deadpannormal
with charachange


rin "Moyen normal."

play music music_rin fadein 2.0


"Le sens relatif de sa phrase mis à part, elle ne semble pas aller très bien."


hi "Tu es trempée."

show rin basic_absent
with charachange


rin "C'est parce que je viens de dehors. Tu connais ?"


hi "Pourquoi tu irais dehors ? Il pleut des seaux dehors, si tu n'avais pas remarqué."

show rin basic_deadpancontemplation
with charachange


rin "J'avais pas remarqué. Il pleut assez fort cela dit. Je me baladais."


hi "C'est ce qu'on appelle “se vautrer dans son malheur” ?"

show rin basic_deadpanupset
with charachange


rin "Tu penses que je suis malheureuse ?"


hi "Non, j'ai insinué que tu pensais l'être."

show rin basic_awayabsent
with charachange


rin "Je ne le suis pas, et la pluie n'est pas une chose triste."

show rin basic_absent
with charachange


rin "Tu ne marches jamais sous la pluie ?"


hi "Si, mais avec un équipement approprié, comme un parapluie."

show rin basic_lucid
with charachange


rin "Tu as juste besoin d'imaginer avoir un parapluie bleu avec des bandes blanches."


hi "Ça risque d'être difficile quand la pluie te tombe sur la tête."

show rin basic_deadpannormal
with charachange


rin "Imagine plus fort."

"…"


"Ouais, elle est clairement revenue à la normale."


"Ces remarques inconsidérées, à moitié sarcastiques, qui m’exaspèrent vraiment même si elle ne le veut pas, ce regard vide, qui attend toujours plus qu'il ne donne."


"Ça... lui ressemble tellement."

show rin basic_deadpan
with charachange


rin "J'ai peut-être besoin de rentrer. J'ai besoin d'aide avec toute cette eau et les vêtements que je porte."


"Mon cerveau résout rapidement cette équation, et je marmonne mes mots, faisant un contraste frappant avec l'invitation spontanée de Rin."


hi "Mais, Emi..."

show rin basic_lucid
with charachange


"Rin secoue énergiquement la tête, envoyant de l'eau partout."


rin "Elle est partie."

show rin basic_awayabsent
with charachange


rin "Et puis en plus elle ferait que s’inquiéter et s'agiter jusqu’à ce qu'elle ne puisse plus s’inquiéter ou s'agiter, ce qui prend toujours beaucoup de temps."

show rin basic_absent
show rain normal behind bg
with charachange


rin "Elle fait ça pendant plus longtemps que je n'ai envie de l'entendre s'agiter, et je me suis dit que tu n'es sûrement pas du genre à t'agiter."





$ renpy.music.set_volume(0.4, 1.0, channel="ambient")

hide bg
show rin invis_close at center
show bg misc_sky_rn as bg2 behind rain
show hisaowindow behind rin
with locationchange

show rin relaxed_nonchalant_close_rn:
    ypos 1.1
with Dissolvemove(0.5)

stop music fadeout 8.0
play sound sfx_rustling


"Elle se pose sur mon bureau avec un bruit spongieux."


"Ses vêtements trempés mouillent mon bureau et tout ce qui s'y trouve, mais elle ne semble pas s'en préoccuper."

"…"


hi "D'accord. Bien. Je vais t'aider."


hi "J'ai une serviette quelque part. Tu veux des vêtements secs ? Un uniforme, ça te va ? Je suis plus grand que toi, mais..."

show rin basic_lucid_close_rn
with charachange


rin "Peu importe."

show bg school_dormhisao_rn
with locationchange


"Après avoir cherché un peu, je trouve un uniforme sec et une serviette au fond de mon armoire."

hide bg
with locationchange


"La serviette dans une main et l’uniforme dans l'autre, je me tourne pour faire de nouveau face à Rin, pas sûr de la prochaine étape."


"Il y a un truc qui ne va pas chez moi, un gars normal serait juste—{w=1.0}{nw}"

show rin basic_absent_close_rn
with charachange


rin "Arrête de t’inquiéter. Ce n'est pas un problème."


"Elle a probablement dû comprendre en me voyant si hésitant."


"Comme si j'étais totalement transparent pour elle."


"Je mets mon anxiété de côté et me concentre sur les huit boutons alignés sur sa chemise, tout comme les miens."


"Seul le premier bouton est un obstacle, et après m'en être occupé, j’enlève les autres avec des mains légèrement moins tremblantes."

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")
play music music_heart fadein 0.5

scene ev rin_wet_pan_down:
    center
    yalign 1.0 subpixel True
    easein 20.0 yalign 0.0
with whiteout


"Jetant la chemise trempée sur le sol, je révèle le corps pâle de Rin, vêtu seulement de son soutien-gorge bleu clair, ce qui me rappelle immédiatement le fait qu'elle m'ait dit que c'est sa couleur préférée."


"J'essaye de ne pas trop penser à... ça, mais c'est difficile de ne pas regarder son corps avec ce qui me vient à l'esprit."


"Je ne sais pas quoi en penser, alors je la regarde juste. Rin semble... fragile."


"Elle est comme une coquille, une coquille fragile qui tient à peine toute seule."


"Ses côtes, toutes visibles sous la peau pâle, montent et descendent en rythme avec sa respiration."


"Rin m'a toujours paru assez mince, mais je réalise maintenant que la période d'activité frénétique avant le vernissage de l'exposition a dû lui faire perdre du poids."


"Est-ce qu'elle mange suffisamment et correctement ? Certainement pas et probablement pas."


"Ce corps laid, et pourtant magnifique, fournissant le minimum nécessaire pour un corps humain, et qui appartient à quelqu'un d'important pour moi, est une contradiction esthétique en lui-même, ce qui est étrange venant d'elle."


"Mes yeux suivent sa clavicule jusqu’à son épaule et au bout de son bras qui s'arrête brusquement."


"Non, c'est moins que le minimum, et je ressens un pincement de tristesse et une certaine culpabilité de penser ça."

scene ev rin_wet_arms:
    center
    xalign 0.0 subpixel True
    linear 20.0 xalign 1.0
with flash


"Ses bras, qui ne sont presque plus que de la peau et des os à cause du manque d'utilisation, semblent vraiment courts maintenant qu'il n'y a plus les longues manches de son uniforme pour les couvrir."


"Mon absence de réaction négative me fait penser que j'ai fini par m'habituer aux diverses anomalies physiques de mes camarades."





"Je me suis toujours demandé pourquoi Rin gardait ses manches longues, ne faisant qu'un simple nœud là où le coude devrait être."


"Ça semble assez peu pratique, mais encore une fois, elle n'est pas la définition de la praticité."


"Peut-être qu'elle aime ça, peut-être que c'est quelque peu important pour elle. Peut-être qu'elle ne s'est juste jamais posé la question."


"J'ai envie de lui demander, et je le fais presque, mais l’état actuel de Rin nécessite d'avoir mon attention en priorité."

scene ev rin_wet_face_down:
    center
    yalign 0.0
with flash


"Elle a arrêté de parler aussi, après qu'on en ait fini des formalités."


"J'imagine qu'il n'y a pas besoin de discutailler dans cette situation."

scene ev rin_wet_towel_down
with charachange


"Je ramasse la serviette sur le lit et l'enroule autour de sa tête, lui frottant les cheveux jusqu’à ce que la grande partie de l'eau de pluie soit absorbée par le tissu."

scene ev rin_wet_towel_up
with charachange


"Elle me regarde par-dessus la serviette, avec ses yeux impassibles."


"On dirait qu'elle a envie de dire quelque chose sans le faire."


"C'est ce genre de regard."


"Mais je ne peux pas lire ce qu'elle pense sur son visage, alors je continue de frotter ses épaules et ses cheveux avec la serviette."


"Le silence est oppressant, terrifiant."


"La communication entre nous a soudainement été réduite aux mouvements de mes mains et de la serviette, et Rin bougeant son corps avec mes gestes."


"Ma respiration irrégulière et ses souffles courts, essayant de trouver un rythme commun qui n'existe pas."


"Je crois que je peux entendre ses battements de cœur, ou peut-être que ce sont simplement les miens qui redoublent."


"Alors que je repousse une mèche de cheveux coquine derrière son oreille, Rin presse soudainement sa joue sur le dos de ma main."


"Le contact est électrique, un coup de jus me passant à travers le corps."

scene ev rin_wet_towel_touch
with charachange


"Qu'elle soit en train de rechercher du réconfort, de la chaleur ou juste mon toucher, je ne saurais pas dire, mais je ne peux pas m’empêcher de la toucher en retour, caressant sa douce joue avec ma main."


"Et avec les yeux fermés, elle me fait des petits baisers sur les doigts, comptant les phalanges avec ses lèvres..."


"Je suis attristé au-delà de ce qu'il est possible d'exprimer."


"Nous sommes là, un garçon et une fille, tous les deux amoureux l'un de l'autre ou quelque chose de proche, ou peut-être pas... et pourtant..."

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve


n "\nQuelque chose ne va pas, je peux le sentir en Rin et en moi ; dans la façon dont nos regards se rencontrent à peine, évitant timidement tout contact ; dans sa posture timide, renfermée, et dans ma façon de la toucher comme si elle était une poupée de porcelaine, de peur de briser sa constitution délicate."


n "Nous sommes plus proches que nous ne l'avons jamais été, et pourtant je ne me sens pas heureux. C'est comme hier."


n "Depuis quand tendresse et tristesse sont devenues le même mot, actes d'affection n'invoquant que le désir ? ...Comment, pourquoi est-ce qu'on a fini comme ça ?"


n "“Non, ne dis pas ça”, j'ai envie de me dire à moi-même, mais combattre l'omniscience de la conscience est une cause perdue."


n "Pourtant, je suis là, et Rin est là, et j'ai l'impression qu'elle serait capable de résoudre tous les problèmes qu'elle a."


n "Et si elle peut, pourquoi je ne pourrais pas moi ? Pourquoi nous ne pourrions pas ?"


n "J'ai l'impression que cette étape est de trop, trop difficile, trop incertaine."


n "Donc pour maintenant, tout ce que je peux faire est la sécher pour qu'elle n'ait pas à nouveau un rhume."

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")
$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

scene ev rin_wet_face_up
with charachange

window show


"Je lui caresse la tête, essayant de coiffer ses cheveux qui refusent de s'ordonner même en étant mouillés."


"Une paire d'yeux foncés suit chacun de mes mouvements."


hi "Le pantalon aussi ?"

scene ev rin_wet_face_down
with charachange


"Elle hoche la tête, s'adosse et tend les jambes, avec un geste d'invitation qui me provoque une sensation désagréable remontant le long de ma colonne vertébrale comme un mauvais pressentiment."


"Ce n'est pas suffisant pour me dissuader cela dit, et le silence commence à me donner l'impression d'être détaché de moi-même."


"Je fais des mouvements automatiques, sans penser, même si je devrais ; je devrais lui en parler, ou au moins parler de quelque chose."


"Le silence est un sort, un pacte qui nous a liés à ce monde privé fait de bruit de pluie et de la sensation de sa douce peau sous mes doigts."


"Le bouton de son pantalon est fortement serré, mais il s'ouvre étonnamment facilement."


"Le faire glisser est difficile, surtout parce qu'elle est assise dessus sans intention de se lever pour me faciliter la tâche."

scene unlock_evh rin_h2_pan_surprise
show evh rin_h2_pan_surprise:
    xalign 0.5 yalign 0.0
with whiteout


"Je me mets à genoux inconfortablement entre ses jambes pour pouvoir rapidement sécher ses pieds nus, me rappelant qu'ils sont aussi importants pour elle que des mains pour moi."


"Alors que je passe la serviette sur ses jambes, Rin frôle ma joue avec sa cuisse et me pousse dans le dos avec ses talons pour me faire venir plus près."


"Je relève la tête pour croiser son regard silencieux qui attendait le mien."


"Son regard modeste, dans l'expectative, semble me dire que la balle est dans mon camp."

"…"


"Je caresse furtivement l’intérieur de sa cuisse avec ma main."

show unlock_evh rin_h2_pan_away
show evh rin_h2_pan_away
with charachange


"Le toucher la fait inspirer brusquement, comme si elle essayait de retenir son souffle."


"Et si je fais ça, alors ?"

show unlock_evh rin_h2_pan_closed
show evh rin_h2_pan_closed
with charachange


"Le léger baiser que je pose sur sa cuisse est suffisant pour que Rin perde son calme, ferme les yeux et gémisse d'une voix à peine audible."


"...C'est ce que tu veux aussi ? Ça t'irait de le faire ? De franchir cette étape ?"

show evh rin_h2_pan_closed:
    subpixel True
    acdc_warp 8.0 yalign 1.0
with None


"...Et si ? Peut-être que si..."


"Des pensées brumeuses flottent quelque part à l’arrière de mon esprit confus."


"D'une certaine manière, cette situation fait que j'ai du mal à réfléchir, comme si ma tête était pleine de coton."


"Mais ce n'est pas grave. Je ne pense pas que réfléchir soit quelque chose dont on ait besoin à ce moment précis."

label fr_R41h:
show evh rin_h2_nopan_closed:
    yalign 1.0
with Dissolvemove(0.5)

$ renpy.music.play(music_heart, fadein=0.5, if_changed=True)


"Par la grâce d'un morceau de tissu beaucoup plus petit, enlever la culotte de Rin est bien plus facile que son pantalon."




"Elle disparaît au-delà de mon champ de vision, glissant quelque part loin de ses jambes."


"On dirait que je n'ai pas fait un bon travail avec la serviette, puisque les jambes de Rin sont toujours mouillées par la pluie."


"Bah, peu importe."

show evh rin_h2_hisao_closed
with charachange


"Guidé par l'instinct plus que par la rationalité, je me rapproche et goûte un différent type d'humidité."


"Elle répond aux lents mouvements de ma langue sur sa peau, à mes baisers sur sa chair."


"Ses muscles se tendent et se relaxent en rythme, comme si je faisais quelque chose de désagréable."


"Entendre Rin essayer ne de pas faire de bruit pendant que je l'embrasse à cet endroit est... irréel."


"Toute cette matinée m'a semblé irréelle, comme l'intangibilité surréaliste d'un rêve éveillé."


"Je n'arrive pas à croire que je fasse ça, pour elle, à ce moment."


"En plus, le point de non-retour était il y a un million de kilomètres."


"J'explore, essaye de faire des choses pour elle, de trouver des endroits où réside sa faiblesse, pour la taquiner, la rendre folle de plaisir parce que je veux, je veux faire ça pour elle."


"Mais elle ne gémit pas, elle ne se tortille pas, peut-être parce que je ne peux pas rendre Rin plus folle qu'elle ne l'est déjà, quoi que je fasse."


"Sa lourde respiration est mixée avec des gémissements inintelligibles qui sont ceux d'une démente, mais je ne les cause pas."


"Je les libère juste d'elle."


"Elle devient de plus en plus humide, et je bois d'elle, sentant une chaleur grandir à l'intérieur de moi."


"J'essaye d'atteindre ses endroits les plus profonds, pour pouvoir la ressentir le plus possible."


"Chacune de mes actions entraîne une réaction différente, mais aucune n'est guidée par la luxure."

show evh rin_h2_hisao_closed:
    subpixel True
    acdc_warp 16.0 yalign 0.0
with None


"Rin est perdue dans le désir, prête à accepter que je fasse n'importe quoi si je le fais tout de suite."


"Elle se rapproche de plus en plus du moment final, mais ce chemin passe par la folie."


"Pourtant, elle va dans cette direction."


"Les muscles ne se relaxent plus maintenant entre les vagues de spasmes d'extase."


"Rin devient juste de plus en plus tendue, se contractant tellement que ça doit être douloureux physiquement, mais je ne m’arrête pas."


"Je continue, et je sais qu'elle a envie aussi, elle veut désespérément que je fasse ça pour elle."


"Une jambe s'enroule autour de mes épaules et me rapproche d'elle, tellement proche que je crois que je vais étouffer."


"Je continue parce que c'est la seule possibilité."

stop music fadeout 8.0
stop ambient fadeout 12.0


"Alors que je pousse le bouton qui l’amène à manquer d'air, elle coince sa jambe dans mon dos, perdant son esprit dans la sensation, et à ce moment précis je semble oublier tout ce qui aurait dû se passer, et tout ce qui devrait se passer."


"Tout ce que je sais c'est que je suis venu ici et... je crois qu'il y avait une serviette à un moment donné aussi."


"Rien de tout cela n'a d'importance, tout ce qui importe c'est ce que nous avons maintenant."


"Son orgasme passe aussi à travers moi, m'excitant d'une façon totalement nouvelle."


"Ça me rend anxieux, nerveux. Gêné."

show evh rin_h2_hisao_away:
    yalign 0.0
with Dissolvemove(0.5)


"Alors que son corps se relaxe, j'essaye de l'embrasser de nouveau en bas, mais ça la surprend, la faisant sursauter."

show evh rin_h2_hisao_surprise
with charachange


rin "Non... Hisao... Ça suffit."


rin "Viens là."

scene bg school_dormhisao_rn
with locationchange


"Je me lève pour retirer le dernier vêtement que porte Rin."


"Elle se penche sur moi pour reprendre son souffle, me chatouillant avec son souffle chaud à travers mon t-shirt."


"Aveuglément, je passe ma main dans son dos pour trouver l’agrafe qui tient son soutien-gorge."


"Il s'ouvre plus facilement que ce que je pensais, tombant quelque part sur le sol."

play music music_romance fadein 10.0

scene ev rin_pair_base_clothes
show rp_hisao normal at truecenter
show rp_rin normal at truecenter
with whiteout


"Sa peau nue contre moi est une sensation si fantastique que j'en veux plus, et je l'obtiens, en la serrant dans mes bras."


"L'odeur des cheveux de Rin est celle de la pluie, et je réalise que je n'entends plus le bruit de celle-ci maintenant."


"Ça nous fait revenir à la réalité. L’atmosphère qui nous enveloppait dans une réalité qui était la nôtre a maintenant disparu, et je réalise maintenant plus clairement ce qui se passe."

show rp_hisao frown
with charachange


hi "Tu sais, ce n'est vraiment pas ce que devraient faire des amis."


"Je chuchote, remarquant encore une fois à quel point un fait aussi simple que parler peut être extrêmement difficile des fois."

show rp_rin talk
with charachange


rin "Tu vas arrêter d'être mon ami ?"




"Ce n'était pas ce que je voulais dire, mais son ton sérieux et les connotations derrière la question de Rin me font réfléchir."

show rp_hisao smile
with charachange


hi "Nan."

show rp_rin smile
with charachange


rin "Je... crois que ça irait. Même si tu arrêtais."


"Je la serre dans mes bras et souris dans ses cheveux, comprenant parfaitement Rin pour une fois."

show rp_rin frown
with charachange


rin "Tu es mouillé."


"L'humidité qu'il restait sur sa peau est maintenant sur ma chemise."


"D'une certaine façon, même ses remarques évidentes me font plaisir maintenant."

show rp_hisao normal
with charachange


hi "C'est vrai. Je suis mouillé. Mais c'est ta faute."

show rp_rin normal
with charachange


rin "Je veux te voir."

play sound sfx_rustling

scene ev rin_pair_base
with charachange


"J'acquiesce, me redresse et défais les boutons de ma chemise, bien plus rapidement que lorsque j'ai défait les boutons de Rin."


"Une soudaine sensation de hâte me prend, me poussant à me dépêcher."


"Chaque seconde où je ne touche pas Rin est une seconde gâchée, une chance perdue."


"Ma boucle de ceinture s’avère être un obstacle malgré ma capacité à l'ouvrir en un battement de paupière dans des circonstances normales."

show rp_rin closed
with charachange


"Pendant que je me débats avec, je ne remarque pas le pied de Rin se lever entre nous jusqu’à ce qu'elle commence à passer sur ma poitrine avec son orteil."

show rp_hisao frown
with charachange


"Je baisse le regard pour voir ce qu'elle regarde..."


hi "Mon cœur..."


"Par réflexe je me recule légèrement, couvrant de ma main la cicatrice au milieu de ma poitrine."


"La marque profonde qu'a laissée la chirurgie sur mon corps après ma crise cardiaque a guéri depuis, mais... eh bien, ce n'est pas particulièrement beau sans pourtant être repoussant."


"C'est à peine visible, mais elle a vraiment un œil pour le détail. C'est pour ça qu'elle a dit qu'elle voulait me voir ?"


"J'avais quelque peu oublié ça à cause de tout ce bazar avec Rin, mais maintenant toutes les choses désagréables liées à ma condition refont surface au même moment, déferlant dans mon esprit comme un tsunami."


"Mon dieu, et ces histoires de vieux qui ont des crises cardiaques en faisant l'amour, et si..."

show rp_rin talk
with charachange

rin "Hisao."

"…"


"Me rendant compte que je pourrais avoir gâché l'ambiance, je peine à m'expliquer."

show rp_hisao normal
with charachange


hi "Ah... désolé, c'est juste que..."

show rp_rin smile
with charachange


rin "Laisse-moi te toucher."


"Ses yeux sont sensuels, engageants, alors qu'elle est là, nue, sans un soupçon de honte. Je n'aurais jamais cru que Rin puisse être comme ça."

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve


n "\n\nOuais, je sais que ce n'est pas comme ça que ça devrait se passer."


n "Même si Rin est là, même s'il ne devrait pas y avoir d'autres questions, d'autres obstacles, pas cet horrible sentiment que quelque chose ne va pas..."


n "Le même sentiment qui m'a serré le cœur hier refait son apparition."


n "Nous sommes ensemble. D'une façon qu'il est difficile de définir, ça échappe à la description aussi farouchement que ça évite le changement."


n "\nEst-ce qu'une relation comme ça irait ? Est-ce qu'on pourrait changer pour devenir plus proches ?"


n "Même si on restait ensemble toute une éternité, il est possible qu'on ne trouve jamais de compréhension mutuelle."


n "Mais l'éternité n'est pas une chose de ce monde. Ça pourrait tout autant dire qu'on ne resterait pas ensemble pour toujours."


n "Si ce n'est pas nos différences, alors le flot du temps nous séparera avec sa force irrésistible."

nvl clear


n "\n\nRin est une créature de l'instant, de fantaisie et d'impulsion."


n "\nJe ne suis rien de la sorte."


n "\nC'est un fait que je comprends très clairement."


n "Sans besoin d'autre raison, je devrais saisir ce moment. Même si c'est le seul moment qu'on aura ensemble, je ne devrais pas me laisser le gâcher."


n "Même si je ne peux pas m'enfuir. Rin ne peut pas non plus, je le sais maintenant."


n "\nNous avons tous deux des choses que nous ne pouvons pas laisser tomber, choses auxquelles nous ne pouvons pas ne pas penser."


n "Des sentiments que nous ne pouvons pas ne pas ressentir."


n "Mais elle se permet de me vouloir sans aucune retenue. Ici et maintenant."

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")
$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

show rp_hisao frown
with charachange

window show


hi "Je suis désolé, tu sais..."

show rp_rin closed
with charachange


rin "Hisao, tu dois vraiment arrêter de t’inquiéter."


"Rin m’interrompt avant que je puisse aller plus loin, ce qui est bien parce que je ne sais pas ce que j'aurais pu dire."


"Sa voix, vide de tout calme habituel, me gronde gentiment, sans être sèche."

show rp_rin smile
with charachange


rin "Tu dois vraiment apprendre à te laisser aller."


"Elle me scanne calmement, presque d'un air calculateur."


"Je me demande de quoi j'ai l'air à travers ses yeux."


"La vache. Ils sont tellement verts que ça fait presque mal de les regarder."


"J'ai toujours été tellement enchanté par ses yeux, ces yeux mystérieux, captivants qui étaient toujours trop actifs dans leur propre intérêt."


"Mais j'ai aussi toujours été intimidé par eux."


"Ouais. Rin est intimidante, sur plus d'un point à ce moment précis."


"Elle est très lucide, c'en est effrayant, et la chair de poule sur sa peau trahit le fait qu'elle a froid, ou peur."


"Dans tous les cas, je me redresse et me rapproche de Rin, la serrant dans mes bras pour la sentir contre moi et bannir tous mes doutes."


"La vue de ses yeux aimants et doux semble faire fondre ces doutes, comme a fondu la dernière neige de l'hiver."

scene evh rin_h_closed
with whiteout


"Elle presse sa tête sur mon épaule, cherchant une position pour se reposer, s'appuyant sur moi comme je m'appuie sur elle."


rin "Allons-y."


"Oui."

scene evh rin_h_left
with charachange


rin "Tu devrais oublier les choses comme le futur et le passé, ce n'est pas comme si tu pouvais changer ce genre de choses."


"Je voulais lui dire quelque chose, mais j'ai perdu ma voix alors je lui marmonne juste quelque chose d'inintelligible."


rin "Tu devrais être juste avec moi maintenant."


"Peut-être qu'elle a compris ce que je voulais dire même si ce n'est pas mon cas."


rin "Viens là."


hi "Je suis là."

scene evh rin_h_normal
with charachange


rin "Viens plus près."


"Mon corps entier n'a que des pensées positives, alors je le fais, la serrant plus fort contre moi."

scene evh rin_h_right
with charachange


rin "Plus près."


"J'appuie le bas de mon corps contre le sien."


"Elle se tend un peu. Juste un peu."

scene evh rin_h_closed_close
with characlose


rin "Plus près."


"Sa demande finale ressemble plus à une prière."


"Il n'y a qu'une seule façon d'être plus proche que ça."


"Je baisse une main et me guide, me plongeant en elle."

scene evh rin_h_strain_close
with charachange


"Chaque muscle dans le corps de Rin se tend au même moment."

scene evh rin_h_strain
with charadistant


"Elle ne dit rien, ne tressaille même pas, alors je pousse plus loin, finissant par bouger d'avant en arrière."


"Et encore. Et elle bouge avec moi."


"Nos mouvements se confondent en une chaîne continue de va-et-vient, dedans et dehors."


"Toutes mes sensations deviennent plus vives, amplifiées dix fois."


"Mon cerveau a renoncé depuis bien longtemps à interpréter toute cette stimulation, et maintenant je n'ai aucun autre choix que de ressentir tout ça avec tout mon corps."


"C'est comme ça pour Rin aussi, je le sais. Je peux le voir. Je peux le ressentir."


"Elle respire rapidement, perdant tout son calme et sa grâce, son souffle chaud sur mon épaule."


"Entre ses respirations fragiles, elle m'embrasse quelques fois tendrement, gentiment, comme si elle ne savait pas comment bien le faire."


"Mais il n'y a pas d'hésitation."


"Se tenant désespérément à moi, me serrant plus près pour que je puisse être plus profondément en elle, elle bouge contre moi, de sorte qu'il est difficile de dire où je m’arrête et où elle commence."


"Nous y allons lentement, atrocement lentement, comme si nous avions tout le temps du monde même si nous avons seulement ce moment et rien au-delà."


"Ce sentiment est—{w=0.7}{nw}"

scene evh rin_h_normal_close
with characlose


rin "Attends..."


"Je m’arrête de bouger, légèrement alarmé."


"Peut-être que ça fait mal, ou..."

scene evh rin_h_right_close
with charachange


"Elle me regarde d'une façon que je n'arrive pas vraiment à interpréter."


rin "C'est ça ?"


hi "Hein ?"


rin "Tu as dit que je n'avais pas à être seule."

scene evh rin_h_left_close
with charachange


"Ses yeux sont remplis d'une confusion innocente et maladroite qui me fait un peu rire et lui caresser l’arrière de la tête."


hi "Ouais. C'est ce que je voulais dire."


hi "Que tu as quelqu'un que tu peux aller voir quand tu es trempée par la pluie."


hi "Ça veut dire que tu n'es pas seule."


hi "Si tu as quelqu'un comme ça pour toi."

scene evh rin_h_closed_close
with charachange


"Elle me répond en m'embrassant, me rappelant que nous nous sommes arrêtés sans vraie raison."


"Alors nous recommençons, presque en même temps, synchronisant chacun le rythme de l'autre."


"Je bouge plus vite, plus vite à l'extérieur et plus vite à l'intérieur d'elle, ma transpiration se mélangeant à la sienne et scintillant sur nos peaux comme des diamants et des perles."

scene evh rin_h_strain:
    truecenter
    zoom 1.2 subpixel True
    easein 20.0 zoom 1.0
with charadistant


"Elle bouge plus vite, remuant contre moi dans les affres de notre désir."


"Le parfum enivrant de son désir, le sentiment aliénant qui relie nos corps, la sensation de toute pensée rationnelle s'écoulant de mon esprit."


"Tout ça brûle ma conscience tout comme le sentiment irrésistible de mon corps brûle mes instincts."


"Alors que ces sensations montent en moi, Rin ne montre aucun signe de vouloir s'arrêter."


"Elle croise ses pieds dans mon dos, me forçant à m'enfoncer aussi profondément en elle que nos corps le permettent, chaque millimètre envoyant des signaux de plaisir dans ma colonne vertébrale."


"Mon esprit s’éteint alors que le monde se change en un flash de lumière aveuglante."

stop music fadeout 2.0
stop ambient fadeout 2.0

window hide

scene white
with Dissolve(2.0)

$ suppress_window_after_timeskip = True

with Pause(4.0)


label fr_R42:

window hide None

scene white
with None

$ renpy.music.set_volume(0.1, 0.0, channel="music")
play music music_timeskip fadein 4.0

centered_b "Present{fast}" with Dissolve(4.0)


nb "“Présent” est un concept vague et fugace au mieux.\n"


extend "Le moment entre le passé et le futur ?\n"


extend "Ça ne veut pas dire grand-chose.\n"


extend "Trop penser à des choses qui ne veulent pas dire grand-chose est une perte de temps.\n"


extend "C'est pour ça que vivre dans le présent est toujours la meilleure option.\n"


extend "En plus, pour nous qui ne pouvons pas voir le futur et qui oublions le passé trop facilement, le présent est vraiment la seule preuve de notre existence.\n"


extend "Même si cette existence continuera même si on l'oublie pendant un moment, il est bon de vivre le jour au moins une fois de temps en temps.\n"



centered_alive "De cette façon... tu peux confirmer que tu es, vraiment..."


show alivetext "That way… you can confirm that you are, in fact…"
show alivetext "De cette façon... tu peux confirmer que tu es, vraiment..."
with None


show alivetext "That way… you can confirm that you are, in fact… alive."
show alivetext "De cette façon... tu peux confirmer que tu es, vraiment... en vie."
with Dissolve(3.0)

$ renpy.pause()

stop music fadeout 4.0

scene bg school_dormhisao
with Dissolve(4.0)

window show Dissolve(2.0)

$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_dreamy fadein 4.0


"Je suis sûr que la fille qui se tient là à moitié nue, regardant par la fenêtre de ma chambre, a une bien meilleure notion du “présent” que moi."


"Quant à moi... eh bien, à cet instant je suis quelque peu désorienté par mon état présent, puisque je devrais essayer de trouver ma chemise au lieu de regarder les fesses de Rin."


"Mais je ne peux pas m’empêcher de la regarder."

scene bg misc_sky
show hisaowindow
show rinpan relaxed_nonchalant_close at center
with locationchange


"Elle est tellement proche de la vitre que son nez va probablement laisser une marque."


"Du moins sa respiration le fait, quand elle se condense sur la fenêtre rafraîchie par la pluie avant de rapidement disparaître de nouveau."


"Le fait que je m'agite dans tous les sens pour trouver mes vêtements et m'habiller ne semble pas perturber Rin dans sa contemplation, ce qui n'est pas gênant, vraiment. Ça ne m’embête plus autant qu'avant, ces silences."


"Seulement après que j'aie presque fini de boutonner ma chemise, Rin dit quelque chose, toujours sans se tourner pour me regarder."

show rinpan relaxed_boredom_close
with charachange


rin "Allons quelque part."


hi "Où ?"


"Je peux seulement présumer qu'elle m'invite moi et pas la fenêtre, mais c'est une simple supposition."

show rinpan basic_lucid_close
with charachange


rin "Je sais."


hi "Quoi ?"

show rinpan basic_deadpan_close
with charachange


rin "Aide-moi à m'habiller."

show rinpan basic_awayabsent_close
with charachange


rin "Je crois qu'aujourd'hui c'est le jour."

show rinpan basic_deadpanupset_close
with charachange


rin "Allez, vêtements."


"Vêtements, vêtements... quel ton impatient."


"Je m'accroupis pour ramasser son soutien-gorge qui est tombé sur le sol, jeté là dans ma hâte de la déshabiller et oublié là."


"Le tenant par le bout des doigts comme un poisson mort, la même hésitation qui m'a prise quand je déshabillais Rin s'empare de moi à nouveau."


"Est-ce que l'intimité est une chose aussi difficile que ça pour moi ?"

show rinpan basic_deadpancontemplation_close
with charachange


rin "Allez, tu l'as retiré sans souci. C'est pareil mais dans l'autre sens. Comme parler à l'envers."

show rinpan basic_deadpan_close
with charachange


rin "Elicaf tse'c siam, eliciffid elbmes."


"Perplexe devant sa soudaine démonstration de processus mental prodigieux, j'en oublie d'inverser son charabia."


"Je suis assez sûr que je ne pourrais pas parler à l'envers avec autant de fluidité, même si je m’entraînais."


hi "Euuh, tu pourrais répéter ?"

show rinpan basic_lucid_close
with charachange


rin "Elicaf tse'c siam, eliciffid elbmes."

"…"


hi "Compris. Bien, je vais essayer."


"Rin avait raison, le système de verrouillage est assez simple, et j'accroche le petit morceau de plastique au bout du troisième essai."


hi "Voilà."

show rinpan basic_deadpandelight_close
with charachange


rin "Retsuja'l siod ut tnanetniam."


hi "Quoi ? Arrête ça s'il te plaît, je ne parle pas l'enverlien."

show rinpan basic_lucid_close
with charachange


"Elle secoue la tête comme si elle devait se remettre à l'endroit avec un geste physique."


"Je connais quelques personnes qui pourraient trouver un intérêt à ce genre d'aptitude."

show rinpan relaxed_nonchalant_close
with charachange


rin "Je suis coincée. Maintenant, tu dois l'ajuster."


hi "Ajuster ?"

show rinpan basic_deadpan_close
with charachange


rin "C'est ce que j'ai dit."


hi "Non, j'ai demandé ce que tu voulais dire."

show rinpan basic_lucid_close
with charachange


rin "Tu sais, qu'ils soient... bien."


"Oh. Bien tu dis ?"

"…"


"Comme je n'ai aucune idée de comment sont censés être ses seins pour être “bien”, je finis par remuer sa poitrine pendant un bon moment sans arriver nulle part."


"Pas que je me plaigne, mais Rin le fait."

show rinpan basic_deadpanupset_close
with charachange


rin "Emi est meilleure que toi pour ça."


"Son ton impatient m'agace un peu, même si je ne peux pas vraiment la contredire. Rin semble soudainement être terriblement pressée."


hi "Ouais ben excuse-moi, se pourrait-il que le fait qu'elle soit une {b}fille{/b} fasse la différence ?"

show rinpan basic_deadpanamused_close
with charachange


rin "Je ne pense pas, elle a à peu près autant de poitrine que toi."

"…"

stop music fadeout 5.0

hide rinpan
show rin basic_absent_close
with shorttimeskip


"Avec son soutien-gorge et sa poitrine finalement “bien” comme il se doit, le reste de ses vêtements sont bien plus faciles à mettre."

hide rin
with charaexit


"Rin se dirige précipitamment vers la porte même si sa chemise n'est pas entièrement boutonnée."


"Ne me laissant que peu de choix, je la suis."

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_soothing fadein 2.0
play ambient sfx_parkambience fadein 0.5

scene bg school_gardens
with locationskip


"Aussitôt que je réalise que nous nous dirigeons vers l'entrée de derrière menant à la forêt, je pense savoir où veut aller Rin, même si je ne peux pas dire pourquoi elle a envie d'aller là-bas.."


"Encore une fois, je ne peux pas assurer quoi que ce soit quand il s'agit de Rin, même pas si on en arrive à utiliser le mot “probablement”."

$ renpy.music.set_volume(0.6, 0.5, channel="ambient")
$ renpy.music.set_volume(0.8, 0.5, channel="music")

scene bg school_forest1
with locationskip


"La forêt derrière les murs a une odeur de pluie, les dernières gouttes glissent toujours des arbres sur le sol malgré le fait qu'il ait fini de pleuvoir depuis un moment déjà."


"Nous avançons à un rythme tranquille qu'impose Rin, me laissant le temps d’apprécier l’atmosphère calme."


"Je crois que je peux entendre Rin dire bonjour à au moins trois arbres différents alors qu'elle passe à côté d'eux, mais je les ignore, les arbres m'ignorent également."


"Elle me conduit jusqu’à ce chemin étroit menant à la colline, comme je m'en doutais."

scene bg worrytree:
    truecenter
    yalign 1.0
with locationchange


"Je regarde à travers la canopée, cherchant un arc-en-ciel, mais on dirait qu'il n'y en a pas."


"C'est un temps parfait pour les arcs-en-ciel. Le ciel brille bas et la pluie s'est arrêtée depuis peu de temps."


"Bah, peu importe."

$ renpy.music.set_volume(0.7, 0.5, channel="ambient")
$ renpy.music.set_volume(0.6, 0.5, channel="music")

scene bg school_forest2
with locationchange


"Je baisse les yeux de la cime des arbres pour voir le dos décharné de la fille qui ne cesse de grimper lentement sur la colline, sans perdre l'équilibre."


"Quelques pas devant moi sur le chemin, mais toujours hors d'atteinte."


"Je ne crois pas que je pourrais atteindre un arc-en-ciel, mais atteindre Rin... ça semble moins impossible que c'était le cas à une époque."

$ renpy.music.set_volume(1.0, 0.5, channel="ambient")
$ renpy.music.set_volume(0.4, 0.5, channel="music")

scene bg school_hilltop_border_summer
with locationchange


"Le ciel clair qui nous salue au-dessus de la prairie est vaste et beau."


"Un vent fort repousse les nuages de la ville, de l'autre côté des montagnes au loin."


"La vue est belle, mais..."

"…"

stop music fadeout 6.0

show dandelionsbg thin
show dandelionsfg thin
with None


"Une tache de blanc passe au coin de ma vision, mais quand je me tourne pour la regarder, elle est déjà partie."


"Une autre suit, puis une troisième."


"Avant que je puisse le réaliser, des douzaines de petites touffes de blanc presque invisibles volent tout autour de nous."

show rin basic_delight behind dandelionsfg at center
with charaenter


rin "Regarde, les fleurs."


"Ah, je vois maintenant."

$ renpy.music.set_volume(1.5, 0.5, channel="ambient")
$ renpy.music.set_volume(1.0, 0.0, channel="music")

scene bg school_hilltop_summer
show dandelionsbg dense
show dandelionsfg dense
with locationchange

play music music_comfort fadein 0.5


"La mer de pissenlits qui couvraient le haut de la colline lors de notre dernière visite a changé au fil des jours."


"Eux qui étaient jaune brillant la fois dernière sont maintenant blanc coton."


"Certaines des fleurs ont déjà relâché leurs graines, mais beaucoup attendent toujours un meilleur vent."


"Aujourd'hui ces vents ne se font pas attendre, de temps en temps ils font plier sans difficulté l'herbe, et peu après l'air se retrouve avec plein de graines de pissenlits."


"Une par une, les graines se séparent des fleurs et s'envolent."


"Un événement commun, mais qui semble fasciner Rin pour je ne sais quelle raison."

$ renpy.music.set_volume(1.0, 0.5, channel="ambient")

show rin negative_spaciness behind dandelionsfg at center
with charaenter


"Elle tourne la tête de tous les côtés, émerveillée par le changement qui se passe tout autour d'elle alors que les graines s'envolent."


"Je les regarde aussi, suivant les touffes blanches qui flottent au vent vers l'horizon, et j'imagine que je peux les voir même après qu'elles aient disparu de ma vue."

"…"

show rin basic_awayabsent
with charachange


rin "Hisao ?"


hi "Oui ?"

show rin basic_absent
with charachange


rin "Est-ce que tu m'aimes ?"


"Je redeviens immédiatement attentif, vois son expression très sérieuse qui ne regarde maintenant plus seulement les fleurs."


"Quelle question difficile, posée juste comme ça, au milieu de nulle part."


"Pourtant son ton vif me force à répondre rapidement."


hi "Je ne sais pas. Peut-être que oui."


"Peut-être trop rapidement."

show rin basic_deadpannormal
with charachange


rin "Qu'est-ce que ça veut dire ?"


hi "...Je ne sais pas."

show rin basic_lucid
with charachange


"Rin soupire, peut-être insatisfaite de ma réponse incertaine. Je le serais aussi."

show rin relaxed_nonchalant
with charachange


rin "Moi non plus."

show rin relaxed_boredom
with charachange


rin "Je ne pense pas savoir grand-chose sur l'amour."

hi "…"


hi "C'est pas grave, hein ?"

show rin basic_lucid
with charachange


"“Qu'est-ce que j'en sais moi ?” semble dire son haussement d'épaules, hésitant à donner une réponse précise."


"Elle reste silencieuse pendant une seconde de trop, mais même cette seconde n'est pas assez longue pour réfléchir..."

show rin basic_absent
with charachange


rin "Je t'aime."


"Ces deux mots me paralysent comme un lapin pris dans les phares, mais je ne suis pas un lapin et je ne regarde que les yeux de Rin qui semblent bien, bien trop sereins pour ce qui vient de sortir de sa bouche."

show rin basic_deadpanupset
with charachange


"Rin semble assez sérieuse cela dit, jusqu’à ce qu'elle tire la langue, fronce un peu les sourcils et me rende encore plus confus que ce qu'ont pu faire ses mots."


"Pourquoi est-ce qu'elle semble légèrement mécontente ?"


"Était-ce une confession de ses sentiments les plus profonds, un test pour voir comment je réagirais, un test pour voir comment elle réagirait ?"

show rin basic_awayabsent
with charachange


rin "Ça a un drôle de goût."


hi "...Goût ?"

show rin basic_lucid
with charachange


rin "Ouais. Trop bizarre."


"Elle rit, peut-être nerveusement, du moins c'est ce que je choisis de croire, mais elle s’arrête peu après quand elle remarque à quel point ça semble étrange."

show rin negative_spaciness
with charachange


rin "Comme... Je ne sais pas quoi, je... ne pense pas qu'il y ait un mot pour ça."


"Rin continue de parler comme s'il n'y avait pas de sens derrière ses mots, des mots insouciants qui passent par la même langue qui a formé les mots plus importants."

show rin negative_worried
with charachange


rin "Un mot pour... humm..."


"Sauf que."

show rin negative_annoyed
with charachange


rin "...c'est comme..."


"Elle ne peut pas."

show rin basic_deadpanupset
with charachange

rin "…"


"Trouver les mots."

show rin basic_sad
with charachange

rin "…"


"Rin continue de me regarder, cherchant ses mots comme si son cerveau cessait de fonctionner."


"Elle semble horriblement confuse, un peu comme moi alors que j’attends qu'elle m'explique."


"Mais elle ne le fait pas, clignant juste plusieurs fois des yeux, le battement de ses longs cils me rassurant sur le fait qu'elle n'est pas totalement pétrifiée."


"Jusqu’à ce que je réalise ce contre quoi ils se battaient."

show rin basic_crying
with charachange


"C'est encore ces étranges larmes, pas associées à la tristesse ou au bonheur, pas de pitoyables sanglots ou de rires de joie."


"Juste des larmes, spontanées et sans avertissement, comme cette fois dans la salle de classe."


rin "Ah."


"Juste quelques-unes, pas suffisamment pour en faire toute une histoire, alors Rin ne fait pas un geste pour les cacher après avoir remarqué leur présence."


"Rin pleure, semblant ne pas savoir pourquoi, et un grand mal-être s’immerge dans ma poitrine quand je vois ses yeux mouillés me fixer."


"Ça me pétrifie aussi, choqué du caractère incompréhensible de cette situation."


"Je ne comprends plus ce qui se passe."


hi "Rin ? Qu'est-ce qui ne va pas ?"


rin "Je..."

show rin negative_crying
with charachange


"Elle secoue la tête, confuse, ayant du mal à sortir les mots de sa bouche."

show rin basic_crying
with charachange


rin "Désolée..."


rin "Il se peut que j'aie un peu peur de toi..."


"Les mots sont lentement marmonnés, avec une petite voix qui semble croire aussi peu ce qu'elle dit que moi."


hi "Quoi ? Pourquoi ?"

show rin basic_sad
with charachange


rin "Je ne sais pas. Dire ça m'a donné cette impression."

show rin basic_absent
with charachange


rin "Les gens pleurent quand ils ont peur, hein ?"

show rin basic_awayabsent
with charachange


rin "Tu vois ? Je peux le faire aussi."


"Elle détourne le regard maintenant, faisant exprès de ne pas me regarder. Ça me trouble, au moins autant que ce qu'elle m'a dit."

show rin negative_annoyed
with charachange


rin "J'ai... j'ai envie parfois, avec toi, de m'enfuir à un point que je ne peux pas bouger c'est comme si mes jambes se transformaient en pudding panna cotta au citron et mon cœur est comme sur le point d'exploser et..."

show rin negative_sad
with charachange


"Elle affaisse les épaules d'un air mélancolique."


rin "Est-ce que quelque chose comme ça t'est déjà arrivé ?"


"...Je me rappelle le ciel de plomb au-dessus de la forêt gelée et le son des branches sans feuilles s'entrechoquant."


"C'est comme le souvenir d'une autre vie."


hi "Ouais. Une fois."


hi "Mon cœur me faisait très mal à l'époque, aussi."

show rin basic_surprised
with charachange


rin "Mais je croyais que ton truc n'était pas contagieux."


"Je secoue la tête et un petit sourire légèrement forcé trouve le chemin jusqu’à mes lèvres."


"L'autre affliction de mon cœur pourrait très bien être contagieuse que ça ne me gênerait pas du tout."


hi "De quoi est-ce que tu as peur ? Je n'ai jamais trouvé ça effrayant."

show rin negative_confused
with charachange


"Rin secoue désespérément la tête, comme si elle savait que le nœud dans sa tête n'allait pas se défaire juste comme ça."


rin "Tu me donnes l'impression que je devrais être quelqu'un d'autre que moi."

show rin negative_sad
with charachange


rin "C'est une chose effrayante."

show rin negative_worried
with charachange


rin "Ça arrive quand tu es gentil avec moi. Comme hier."


rin "Je ne sais jamais quoi faire dans des moments comme ça. C'est difficile."


"Sa voix est à peine audible, un aveu murmuré de quelque chose qui est trop gênant pour même y penser, sans parler de le dire à voix haute."


"Rin n'a jamais été du genre à être embarrassée alors elle dit ça en parlant, mais timidement, comme par instinct."

show rin basic_upset
with charachange


rin "Mais je veux faire quelque chose. Mais je ne sais pas si ce moi le peut."


"Pendant un moment, nous nous regardons tous les deux comme pour attendre que l'autre dise quelque chose."

"…"

hide rin
show rin basic_upset_close as rin2
with characlose


hi "Tu es bête."

hide rin2
show rin relaxed_surprised_superclose at center
with characlose


"Les lèvres de Rin ont un goût salé et de peur contre les miennes."

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack
with Dissolve (0.4)

window show


"Alors que je la serre dans mes bras, je sens mon cœur frapper douloureusement dans ma poitrine."

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack
with Dissolve (0.4)

$ renpy.music.set_volume(0.5, 1.0, channel="music")
$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

nvl clear
nvl show dissolve


n "\n\nMême si je suis content qu'elle ait pu dire des choses comme ça, ça me rend triste après tout."


n "L'esprit de Rin, sa passion, sa force. Toutes ces choses qui me sont chères sont celles que je ne veux pas changer."


n "Comment est-ce que je devrais prendre ça ? Où tout cela se dirige-t-il ? Son avenir est-il irrévocablement différent du mien ?"


n "Cette anxiété ne perdra jamais l'emprise qu'elle a sur mon cœur, mais je pense que je peux apprendre à vivre avec."


n "Lentement, la douleur dans mon cœur s'apaise, et il s'aligne au même rythme que celui de Rin."


n "\n\nNous écoutons ce son pendant un petit moment."

n "…"

$ renpy.music.set_volume(1.0, 1.0, channel="music")
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")
stop music fadeout 8.0

nvl hide dissolve
nvl clear

hide rin2
show rin basic_blush_close behind dandelionsfg at center
with charadistant

window show


"Après que nos lèvres se séparent, il nous faut un moment pour réaliser qu'on peut dire quelque chose maintenant."

"…"

show rin basic_sad_close
with charachange


rin "Tu vois ?"

show rin relaxed_doubt_close
with charachange


rin "Tu es quelqu'un de très gentil, même quand tu ne l'es pas."


rin "C'est la chose la plus effrayante au monde."

show rin relaxed_sleepy_close
with charachange


rin "Je crois... que tout ce qui me faisait peur était ta gentillesse."

"…"


hi "C'est pas bon alors, si tu as peur ?"

show rin basic_lucid_close
with charachange


"Elle réfléchit pendant un moment, plissant le front comme si c'était un problème de math difficile."

show rin basic_deadpanamused_close
with charachange


rin "Non. Ça me va. Ça va, si c'est toi."


"Comme un poids enlevé de ma poitrine, ses mots soulagent mon cœur, le remplissant de... je ne sais pas, bonheur ?"


"Qu'est-ce que ça pourrait être d'autre ?"


"Cette fois mon sourire est honnête."

hide rin
show rin basic_deadpanamused as rin2 behind dandelionsfg
with charadistant


"Rin recule, me souriant gentiment comme je lui souris."

show dandelion full:
    alpha 0.0 xalign 0.5 yanchor 1.0 ypos 1.2 subpixel True
    easein 1.0 ypos 1.0 alpha 1.0
with None
show dandelionbg behind dandelion
show dandelions_blurbg behind dandelion
show dandelions_blurfg behind dandelion
hide dandelionsfg
hide dandelionsbg
with Dissolve(1.0)

hide rin2
show rin basic_deadpanamused behind dandelionbg
with None


"Pendant qu'elle essuie son visage avec son épaule, je ramasse un pissenlit jaune et l'apporte à mes lèvres."

show dandelion gone
with Dissolve(1.0)

"Pfff…"


"Les graines s'éparpillent au vent qui les emmène dans un autre lieu."


"En y pensant, tout était si différent il y a seulement quelques semaines."


"C'est le changement."

"…"

show dandelion gone:
    easeout 1.0 alpha 0.0 yanchor 1.0 ypos 1.2
with None

hide dandelionbg
hide dandelions_blurbg
hide dandelions_blurfg
show dandelionsbg dense behind rin
show dandelionsfg dense
with Dissolve(1.0)


hi "Dis, les fleurs sont devenues ce qu'elles étaient destinées à devenir, comme tu l'as dit la dernière fois."


hi "Et toi ? Tu es devenue une vraie artiste ? Ou pas, parce que tu t'es enfuie ?"

show rin basic_deadpancontemplation
with charachange


"Elle réfléchit un moment à ma question..."

show rin relaxed_nonchalant
with charachange


"...puis hausse les épaules."


"Ça me fait presque rire."


"Son attitude insouciante est adorable, un signe de la façon dont Rin peut, et vraiment, sans aucune contrainte que ce soit, faire glisser le poids du monde entier de ses épaules, si elle le veut."


"Elle est, par tous les moyens possibles et impossibles... libre."


"Et je crois que je l'aime pour ça."

show rin basic_absent
with charachange


rin "Je crois pas que c'est important."

show rin basic_deadpandelight
with charachange


rin "Regardons juste les nuages aujourd'hui."

play music music_twinkle fadein 2.0

scene ev rin_goodend_1
show evbg rin_goodend_base:
    center
    subpixel True xalign 0.0
    1.0
    easein 20.0 xalign 1.0
show dandelionsbg dense
show rin goodend_1:
    center
    subpixel True xalign -0.5
    1.0
    easein 20.0 xalign 1.0
show dandelionsfg dense
show evfg rin_goodend:
    center
    subpixel True xalign -1.0
    1.0
    easein 20.0 xalign 1.0
with whiteout


"Elle fait cinq pas et se retrouve sur une grande pierre pour pouvoir être le plus haut possible, et se tient sur la pointe des pieds."


"Quand tu essayes d'atteindre les nuages, chaque centimètre compte."


hi "Ouais, regardons les nuages. C'est bien de faire quelque chose qu'on a vraiment envie de faire, de temps en temps."


rin "Ouais. Tu as sûrement raison."


"Je regarde vers le ciel bleu au-dessus de nous."


"C'est une grande étendue azurée qui s'étend au-delà de mon champ de vision."


"Et pourtant Rin reste sur sa pierre, regardant l'horizon là où les nuages s'éloignent de plus en plus de nous."


rin "J'ai décidé quelque chose."


"Sa voix rêveuse, adressée au vent qui la porte à mes oreilles, manque d'intensité dans le ton mais est pleine de sens."


rin "Ça va d’être moi en fin de compte."

$ renpy.music.set_volume(0.5, 1.0, channel="music")
$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

window hide
nvl clear
nvl show dissolve


n "\n\n\nÇa va aussi ? Ses décisions semblent toujours être très... recherchées."


n "Bah, j'imagine que ça reste important de réaliser ça."


n "Être en paix avec soi-même, s'accepter, être bien avec ce qu'on est."


n "Un simple état d'esprit qui est incroyablement dur à avoir pour certaines personnes, si ce n'est impossible."


n "Je réalise tout à fait que je peux faire partie de ces personnes-là."


n "Rin aussi..."


n "Peut-être que nous ne sommes pas si différents après tout."


n "Peut-être que pour accepter quelqu'un d'autre, tu dois déjà t'accepter toi-même."


n "Peut-être que c'est une étape nécessaire, que nous n'avions pas franchie jusqu’à maintenant."

$ renpy.music.set_volume(1.0, 1.0, channel="music")
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

nvl hide dissolve
nvl clear
window show


"La regardant, debout sur sa pierre, je crois qu'elle peut trouver ce qu'elle cherche."


"Et moi aussi."

show ev rin_goodend_1b
show evbg rin_goodend_base:
    subpixel False xalign 1.0
show rin goodend_1b:
    subpixel False xalign 1.0
show evfg rin_goodend:
    subpixel False xalign 1.0
with charachange


"Le vent balaye ses cheveux et ses vêtements, et Rin écarte ses courts bras dans une étreinte qui est très petite, mais aussi grande qu'il lui est possible de faire."


"Pendant un moment on dirait qu'elle est sur le point de s'envoler, et je dois me retenir de ne pas l'attraper par l'épaule, la ramener vers moi."


"Mais ce moment est quelque chose que je ne peux qu'observer, quelque chose dont je vais me souvenir."


"Les manches de Rin virevoltent librement au vent, ses cheveux ébouriffés, sa peau touchée par le soleil couchant."


"Sa forme élégante que j'ai appris à adorer se fait balayer par le vent qui transporte les petites graines blanches autour d'elle, chacune le début d'une nouvelle fleur."


"Tout ceci est gravé dans mon cœur."


"Comme ces petites graines éparpillées au vent, je suis sûr que Rin aussi peut trouver sa place dans ce monde sans ressentir le besoin de créer le sien à l’intérieur de celui-ci."


"Peut-être qu'elle le croit aussi, et se tenant aussi proche du paradis que possible, elle offre un énorme câlin au monde entier."


"Pour moi on dirait que le monde entier pourrait tenir là, entre ses petits bras, à l’intérieur de son étreinte géante."

show ev rin_goodend_2
show rin goodend_2
with charachange


rin "Hisao ?"


"Elle me regarde de la même façon qu'elle appelle mon nom, d'un air insouciant par-dessus son épaule avec un étrange bonheur dans sa voix et ses yeux."

show evbg rin_goodend_base:
    subpixel True yalign 0.0
    acdc_warp 12.0 zoom 1.15
show rin goodend_2_hires:
    subpixel True yalign 0.0 xalign 1.0 zoom 0.769
    acdc_warp 12.0 zoom 1.0
    subpixel False
show evfg rin_goodend:
    subpixel True yalign 0.0
    acdc_warp 12.0 zoom 1.45
with None


"Je sonde ces yeux sombres, mystérieux qui scintillent de curiosité entre ses cheveux auburn."


"Bien que je sois trop loin pour le voir, je suis sûr qu'ils reflètent mon image."


hi "Qu'y a-t-il ?"


rin "C'est quoi le mot quand on ressent à l’intérieur de son cœur que tout va bien dans le monde ?"

stop music fadeout 4.0
stop ambient fadeout 4.0

window hide

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
