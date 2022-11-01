label fr_S8:

window hide None

scene bg school_dormhisao
with locationchange

with Pause(1.0)

nvl clear

nvl show dissolve

play music music_dreamy fadein 5.0


n "\n\nLe lendemain matin, je me rappelle à quel point la nuit dernière était parfaite. Tellement que je n'arrive pas à arrêter d'y penser."


n "Ce n'est probablement pas le meilleur moment pour ça, vu que j'ai un examen en première heure."


n "Ah, c'est tellement injuste. Comment est-ce qu'ils peuvent faire ça ? Faire un festival, qui est le résultat de ces dernières semaines de travail, un dimanche, et puis enchaîner avec un examen le lendemain matin ?"


n "Ce doit être une mauvaise blague."


n "Ça ne m’inquiète pas trop, mais je me demande s'ils ne pouvaient vraiment pas attendre une semaine pour ça."


n "\n\nBon, au moins il fait assez bon ce matin pour que je puisse étudier dehors avant les cours."

nvl hide dissolve

scene bg school_courtyard
with locationskip

nvl clear

nvl show dissolve


n "\n\nC'est beaucoup plus agréable ici que ça ne le serait en classe. Sans mentionner le silence, je commence à penser que tout le monde se réveillera plutôt tard aujourd'hui."


n "Je pose mes notes pour une seconde et regarde le terrain de l'école, toujours jonché de stands du festival."


n "En les voyant en journée, sans lanternes de papier ou la foule de gens pour me distraire, je remarque quelque chose."


n "Beaucoup des stands que nous avons visités hier s’avèrent être ceux sur lesquels nous avons travaillé."

n "\n…"


n "\nC'est mignon. C'était intentionnel de la part de Shizune ? Ça devait l'être, surtout la connaissant. Est-ce qu'elle voulait que je voie le fruit de notre travail ?"

play sound sfx_footsteps_soft fadein 5.0
stop music fadeout 4.0

nvl hide dissolve

show shizu basic_normal at center
with charaenter

window show


"J’entends des pas dans l'herbe derrière moi et je me retourne. J'ai l'impression d'être légèrement paranoïaque, mais il s’avère que c'est juste Shizune qui se tient là avec un drôle d'air sur le visage."

play music music_shizune fadein 1.0

show shizu adjust_happy
with charachange

shi "…"


hi "Bonjour."


"Pourquoi est-ce que j'oublie toujours qu'elle ne peut pas m'entendre ?"


"C'est probablement parce que je suis habitué à ce que Misha traduise tout, et que je n'ai pas rencontré beaucoup de situations où j'ai été forcé de me confronter au fait que Shizune soit sourde."


"Je crois qu'hier était la première fois."


"Je lui fais quand même un signe. Je peux au moins faire ça, mais je ne vais pas prétendre pouvoir tenir une conversation avec elle, considérant mon ignorance en langage des signes."


"Ça serait malpoli de retourner à mes révisions ? Je ne sais pas vraiment quoi faire d'autre."


hi "Où est Misha ?"

show shizu behind_blank
with charachange

shi "…"


hi "Pas juste parce que je ne te comprends pas. Vous êtes toujours ensemble de toute façon, alors je ne suis pas habitué à vous voir séparées."


"Je sais que c'est idiot, mais pour je ne sais quelle raison, lui parler me rend moins nerveux."

show shizu basic_normal2
with charachange

show shizu adjust_happy
with charachange

show shizu behind_blank
with charachange


"Étonnamment, elle ne s’énerve pas. Elle commence à faire des signes, mais différemment de d'habitude. Les mains de Shizune vont plus doucement et la gestuelle est plus simple."


"Je réalise rapidement que ce n'est pas le langage des signes, mais qu'elle essaye quand même de communiquer avec moi."


hi "Donc c'est l’équivalent du langage des signes pour les non-initiés ?"

show shizu behind_frown
with charachange


"J'ai peur que si j'essaye de lui répondre, j'aie juste l'air d'un complet idiot. L'expression du visage de Shizune me dit qu'elle commence à penser qu'essayer d'avoir une conversation de cette manière n'est pas la meilleure solution possible."


"Il doit y avoir une meilleure façon."


"Écrire sur un cahier ? Bon, j'ai du papier et un crayon. Mais quoi d'autre ?"


"Téléphones ? Je n'en ai pas vraiment besoin ici, donc je l'ai rarement sur moi et je ne sais pas si Shizune en a un de toute façon."

show shizu adjust_happy
with charachange

show shizu basic_normal
with charachange


"Elle prend l'initiative, levant un doigt pour demander une pause avant de sortir un bloc-notes et un stylo de son sac et écrivant un seul mot sur celui-ci :"

window hide


$ written_note("Bonjour.")

show shizu basic_normal2
with charachange

window show

shi "…"


"Je la regarde et reçois un regard intimidant en réponse. Elle tend le bloc-notes dans ma direction avec force, voulant clairement que je réponde."

window hide


$ written_note("Bonjour.")

show shizu behind_smile
with charachange

window show


"Shizune rayonne de bonheur. Elle commence à faire tourner le stylo entre ses doigts d'un air triomphant en pensant à ce qu'elle pourrait dire d'autre."


hi "C'est bon, c'est pas comme si on venait d'inventer l'eau chaude non plus."

show shizu basic_frown
with charachange


"Shizune remonte ses lunettes, comme si elle m'avait entendu et commence à écrire très vite."

window hide


$ written_note("Utilise le bloc-notes ! Écris Écris Écris Écris Écris Écris Écris Écris Écris Écris Écris Écris Écris Écris Écris Écris Écris Écris Écris Écris !")

window show


"Je suis confus. Je suis censé le prendre et écrire “d'accord” ?"


"Ce n'est pas l'exemple d'une conversation fluide. Ça me rend envieux de la capacité qu'a Misha pour discuter avec Shizune."

window hide

show shizu behind_blank
with charachange


$ written_note("Tu révises pour le test ?")

window show


"Je suis presque sûr que je pourrais répondre à des questions comme ça avec de simples hochements de tête."

window hide

show shizu adjust_smug
with charachange


$ written_note("Tu es debout très tôt, la plupart des gens dorment tard après le festival. Ça signifie que tu es anormal.")

window show


"...Ah bon ?"

window hide


$ written_note("Tu es là aussi.")

window show


"Avant de lui rendre le bloc-notes, je me rappelle ce que j'ai remarqué plus tôt, et ajoute :"

window hide


$ written_note("Tu es là aussi.\n\nC'était bien hier. J'ai remarqué aujourd'hui que j'ai construit beaucoup des stands que nous avons été voir. C'est peut-être pour ça qu'ils m'étaient aussi familiers. C'était un autre jeu de ta part ?")

show shizu behind_frown
with charachange

window show


"Elle secoue la tête, indignée."

window hide


$ written_note("Pas un jeu.")

show shizu basic_normal2
with charachange


$ written_note("Je me suis dit que comme tu avais fait ces stands, ils étaient les plus importants. On a dû les visiter, parce que tout le monde devrait être capable d'apprécier le fruit de son labeur. Je voulais que tu sois capable d’apprécier ce que tu as fait.")

window show


"Je suis touché. Cela dit, je me demande pourquoi elle a fait tout ça, et le lui écris."

window hide

show shizu behind_blank
with charachange

stop music fadeout 3.0


$ written_note("Parce que tu étais déprimé.")

window show


"J'ai envie de lui dire que je suis déprimé depuis des jours, mais m’interromps. C'est vrai, je me morfondais pas mal la moitié du temps, donc c'est possible qu'elle s'en soit rendu compte. Tout ce qu'elle a fait, c'était pour me réconforter alors ?"


hi "Merci."


"Je marmonne avant de me rendre compte que j'ai parlé, mais Shizune ne semble pas s'en préoccuper. Je l'écris, et elle hoche la tête une fois."


"Le silence entre nous devient plus pesant à chaque seconde et il n'y a rien que je puisse faire pour le casser. Devoir tout écrire sur le papier détruit un peu toute approche naturelle."

window hide

show shizu adjust_happy
with charachange


$ written_note("Bonne chance pour l'examen.")

window show


"Shizune tend le bloc-notes juste devant mes yeux, brisant ma concentration. Prenant l'initiative, comme toujours."

hide shizu
with charaexit


"Alors qu'elle part en direction du bâtiment scolaire, je me sens un peu triste."

window hide

nvl clear

nvl show dissolve


n "\n\nÇa m'a paru être les vingt minutes les plus longues de ma vie, et tout cela parce que c'est bizarre d'avoir une conversation en face à face avec quelqu'un qui te passe un bloc-notes à chaque fois qu'il veut parler de quelque chose, et en plus je ne sais pas quoi dire la plupart du temps."


n "Ça me donne envie d'apprendre la langue des signes."


n "C'est plus facile à dire qu'à faire. Bien que dans une école comme Yamaku, il doit y avoir une classe de langue des signes. Dans ce cas, il n'y aurait aucune raison de ne pas m'y mettre."


n "La seule personne avec qui je pourrais en parler est Misha."


n "J'ai deux options : Attendre après les cours pour lui parler, ou partir à sa recherche dès maintenant."


n "Je pense y aller maintenant, mais je ne sais pas vraiment où elle est. Le plus plausible serait le dortoir des filles. Après tout, si elle n'est pas avec Shizune, elle doit sûrement être là-bas."

nvl hide dissolve

nvl clear

scene bg school_dormext_full
with locationchange

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_daily fadein 1.0

nvl show dissolve


n "\n\nUn gars se baladant devant le dortoir des filles si tôt le matin est suspect, mais demander à Misha s'il n'y a pas une classe de langue des signes devant Shizune n'est pas envisageable."


n "Elle va bien devoir aller à l'école. Après tout, on est dans la même classe, donc elle doit passer l'examen aussi."


n "Si j’attends là, je serai sûr de la voir passer."


n "J’espère juste qu'elle ne passera pas pendant que je feuillette mes cours."


n "\n\nÇa s’avère être une attente plutôt longue. Alors que les étudiants partent en direction de l'école, je me demande si Misha va être en retard."


n "Finalement je la vois. Elle gambade à travers le terrain, il faudrait que je sois aveugle pour la louper, avec ses cheveux."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear

nvl hide dissolve

show misha hips_grin at center
with charaenter

window show


mi "Salut, Hicchan~ ! Bonjour~ !"


hi "Salut."


"Je n'ai pas beaucoup de temps avant le début des cours, alors je vais direct au but."


hi "Hé, je peux te poser une question ?"

show misha perky_smile
with charachange


mi "Une question ? Mh~... D'accord, Hicchan~ ! Bien sûr~ Bien sûr~ ! J'ai le temps, mais seulement parce que je suis en retard !"


hi "Ça veut dire quoi ça ?"

show misha hips_grin
with charachange


mi "Haha~. J'aurais dû me lever plus tôt, mais j'étais tellement fatiguée~... Si j'avais pu, j'aurais pu réviser, mais j'ai pas pu, pas grave~ ! Qu'y a-t-il, Hicchan ?"


hi "Il y a bien des cours de langue des signes ici, hein ?"

show misha hips_smile
with charachange


mi "Yep~ ! Ils sont optionnels ! Pourquoi tu veux savoir, Hicchan ?"


"Pour je ne sais quelle raison sa question me fait paniquer."


hi "Comme ça. Ça a l'air intéressant, mais j'imagine que c'est trop tard pour m'inscrire maintenant, hein ?"


"Je ne suis pas vraiment subtil, mais Misha ne semble jamais comprendre les sous-entendus de toute façon, donc je fais sûrement plus attention que nécessaire."

show misha sign_smile
with charachange


mi "Mh~ ? Ah, eh bien, Hicchan, j'ai entendu dire qu'il y avait de moins en moins d'étudiants prenant des cours de langue des signes. Alors ! Si tu le veux, je suis sûre qu'ils te laisseront les rejoindre~ !"

show misha hips_grin
with charachange


mi "Tu envisages d'apprendre la langue des signes, Hicchan ?"


hi "...Ouais."

show misha perky_smile
with charachange


mi "Si tu apprenais la langue des signes, ça ferait vraiment plaisir à Shicchan~. Si tu veux, on peut aller à la salle des professeurs après les cours. Ils te laisseront probablement rejoindre le cours."


hi "Ça serait bien."


hi "Ne dis pas à Shizune que je veux faire ça, cela dit."

show misha perky_confused
with charachange


mi "Pourquoi pas ?"


hi "Pour que ça puisse être une surprise. En plus, j'aurais l'air bête si tu lui dis ce matin, et puis que cet après-midi on se rende compte que je ne peux pas rejoindre le cours."

show misha perky_smile
with charachange


mi "Aw~. Tu as raison, Hicchan. Mais, ça va être dur~... C'est une si bonne nouvelle..."


hi "Je suis dans le Conseil des Étudiants, je pourrais tout aussi bien l'apprendre. Même si c'est juste les bases, c'est mieux que rien. En plus, Shizune et moi ne pouvons pas continuer de compter sur toi comme si tu étais un téléphone hein ?"

"…"

with Pause(2.0)

show misha hips_laugh
with charachange


mi "Wahaha~ !"

show misha hips_grin
with charachange


mi "Tu as raison, Hicchan~ !"

"…"

stop music fadeout 4.0
play sound sfx_warningbell


"La cloche résonne pour signaler le début de la première heure, interrompant notre conversation. J'imagine que je demanderai à un prof à la fin des cours."


"Sa réaction était un peu étrange, mais je l'oublie durant la journée."

scene black
with dissolve



label fr_S9:

scene bg school_scienceroom
with locationchange

play sound sfx_normalbell


"La cloche résonne et le professeur fait signe que les cours sont finis pour la journée."

play music music_normal fadein 3.0


"Bien que rentrer dans cette classe ait été étonnamment facile, ça ne fait que quelques jours et je ne suis pas encore habitué. Les signes en eux-mêmes ne sont pas très durs à apprendre, mais la plupart de mes camarades de classe sont durs d'oreille."


"En plus de ça, le professeur favorise l'immersion. Je ne l'ai pas entendue parler depuis que j'ai demandé si je pouvais assister aux cours. C'est un concept étrange et assez troublant."

scene bg school_hallway3
with locationchange


"À l'instant où je sors de la classe, j’entends un rire familier exploser à ma gauche."

show misha hips_grin at center
with charaenter


mi "Salut, Hicchan~ !"


"Misha n'est pas dans ma classe, donc c'est la première fois que je la vois dans ce contexte. Je ne sais toujours pas si le fait qu'elle ne soit pas dans ma classe est une bonne chose ou non."


"Ça serait plus intéressant si elle était là, mais il y aurait plus de situations gênantes."


hi "Salut."

show misha sign_smile
with charachange


mi "C'est une surprise de te voir ici, Hicchan ! ...Ah, c'est vrai ! Tu prends des cours de langue des signes, hein~ ? Hein~ !"

show misha perky_smile
with charachange


mi "Qu'est-ce que tu en penses jusqu’à présent, Hicchan ?"


hi "Ce n'est pas facile d'apprendre une nouvelle langue, mais j'arrive à m'accrocher. Mais même si c'est très différent des autres langues, c'est toujours plus facile que l'anglais."

show misha cross_grin
with charachange


mi "Haha~ ! Vraiment, Hicchan ?"

show misha cross_smile
with charachange


mi "Mh~... J'approuve~ !"


"Je plaisantais juste, mais elle est apparemment très sérieuse."


"Je me demande comment Misha peut me traduire ce qui se dit et avoir en simultané une conversation avec Shizune dans un autre langage."


"Jusqu’à maintenant, je ne réalisais pas à quel point c'est difficile."


"Quelqu'un tape dans mon épaule et s'excuse. Ça devient plutôt bondé par ici, vu que c'est la fin de journée."


hi "Je crois qu'on devrait parler ailleurs que dans le couloir. Allons sur le toit."

show misha sign_smile
with charachange


mi "D'accord~ !"


"Je décide de continuer de parler en chemin. C'est étonnamment assez calme pour qu'on puisse avoir une discussion en même temps."

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 1.0

scene bg school_staircase1
with locationchange

stop music fadeout 5.0


hi "J'ai encore du mal à regarder le professeur constamment. J'imagine que toutes ces années passées à écouter la leçon pendant que je rêvassais font leur effet. Ça rend difficile la prise de notes aussi."


hi "Il n'y a pas grand monde en classe d'introduction et j'ai déjà du retard. J'ai beaucoup à faire."

play sound sfx_door_creak
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene bg school_roof
with locationchange


hi "Voilà, c'est bien mieux."


"Je me tourne et vois Misha en train de me fixer avec les mains sur les hanches et les joues gonflées."

show misha hips_frown
with charaenter

play music music_happiness fadein 4.0


mi "Hicchan, tu es en retard ? C'est pas bon du tout !"


hi "J'ai commencé les cours une semaine après les autres. Ce n'est pas si grave."

show misha sign_smile
with charachange


mi "D'accord, Hicchan, revoyons ce que tu as appris, alors~ ! Je serai ta tutrice, d'accord~ ?"


"C'est la première fois que j’entends “Je serai ta tutrice” en dehors de films cochons. Je ne suis pas autant excité que je l'aurais espéré."


hi "Je ne suis pas sûr d'avoir besoin d'une tutrice."

show misha perky_sad
with charachange

mi "Aw…"


"Elle semble plus déçue que d'habitude. Ça me fait bizarre de la voir avec ce genre d'expression."

show misha hips_frown
with charachange


mi "Je veux devenir professeur de langue des signes, Hicchan ! Et~ ça serait vraiment super si je pouvais essayer de tutorer quelqu'un d'abord. Même si c'est juste un peu, l'expérience serait utile."


hi "Ah, bon, ouais, c'est vrai."


hi "Je ne savais pas que tu voulais devenir professeur de langue des signes."


"C'est difficile de croire qu'elle n'essaye pas intentionnellement de me faire sentir coupable, parce qu'elle est très douée."


"Cela dit, ça se tient. Elle est très douée pour la langue des signes et a certainement la voix pour se faire entendre par ceux qui ont du mal. Je ne l'ai jamais vue comme étant du genre à enseigner, cela dit."

show misha hips_grin
with charachange


mi "Hahaha~ ! C'est la raison pour laquelle je voulais aller dans cette école, Hicchan !"

show misha sign_smile
with charachange


mi "C'est vraiment cher ici, tu sais. Parce que je veux devenir professeur de langue des signes, j'ai reçu un financement. Si je n'avais pas ça, je ne sais pas si je pourrais rester ici."


hi "Je vois. Ce n'est pas que je pense que tu serais mauvaise en tutorat, c'est juste que je ne sais pas si j'en ai besoin pour l'instant."

show misha perky_sad
with charachange


mi "Tu as raison, Hicchan, tu es malin."


hi "Bon, non, ça me donne l'air arrogant."


hi "D'accord, alors s'il te plaît, sois ma tutrice."


show misha cross_laugh
with charachange


mi "Ahahaha~ ! Vraiment ? D'accord~ ! D'accord d'accord d'accord~ ! Yay~ ! Merci, Hicchan~ ! Je ferai de mon mieux !"

show misha sign_smile
with charachange


mi "Commençons dès maintenant~ !"


hi "Trop tôt."

show misha perky_sad
with charachange

"…"


mi "Shicchan me manque~..."


hi "Tu ne l'as pas vue juste ce matin ?"

show misha sign_smile
with charachange


mi "Mais c'est difficile de lui parler en classe, Hicchan ! Et il n'y a pas de réunion du Conseil des Étudiants aujourd'hui, non plus~."


hi "Il y a des examens toute la semaine. Je me sentirais mal si on avait toujours le Conseil des Étudiants. Je serai content quand ils seront finis."

show misha perky_confused
with charachange


mi "Quand on aura de nouveau des réunions, tu ne vas pas sécher, hein, Hicchan ?"


hi "Bien sûr que non. Je suis dans le conseil, après tout."


hi "Ne t’inquiète pas, je ne vais pas arrêter soudainement de venir. Une promesse est une promesse."


"Misha s’arrête pendant une seconde, n'ayant pas l'air très convaincue."

show misha sign_smile
with charachange


mi "Shicchan prend le Conseil des Étudiants très au sérieux, Hicchan. Maintenant que tu l'as rejoint, elle travaille plus dur que jamais pour faire bonne impression."

show misha hips_frown
with charachange


mi "Certaines personnes nous ont rejointes, mais elles ont fini par partir peu après. Shicchan a essayé d’intéresser d’autres personnes dans le Conseil des Étudiants, mais ça n'a pas marché."


show misha perky_sad
with charachange


mi "Même quand une personne voulait nous rejoindre, elle finissait par arrêter de venir. Les gens trouvaient des excuses pour repousser et repousser jusqu’à ce qu'ils finissent par arrêter de venir tout court."

show misha sign_smile
with charachange


mi "Cela dit... Je crois que tu es honnête, Hicchan."


"Mes yeux restent fixés sur ses mains, bougeant presque de manière automatique, traduisant en signes tout ce qu'elle dit."



show misha perky_smile
with charachange


mi "Quand tu as dit que tu nous rejoindrais, elle était vraiment contente."

show misha hips_smile
with charachange


mi "Shicchan pense que tu es intéressant, Hicchan. Une personne inintéressante n'aurait pas l'impulsion nécessaire pour nous rejoindre. Même si ces personnes le faisaient, elles partiraient peu après."


mi "C'est ce qu'a dit Shicchan."

show misha hips_grin
with charachange


mi "Donc~ ! Il est de mon devoir de m'assurer que tu continues~ !"


hi "C'est pour ça que tu veux me tutorer ? Tu es un peu fourbe."

show misha cross_laugh
with charachange


mi "Vraiment, Hicchan ? C'est la première fois que quelqu'un me dit ça~ ! Wahahaha~ !"


"Maintenant il n'est plus possible que je puisse éviter le travail du conseil."


"En repensant à ce qui s'est passé ces derniers jours, je commence à réaliser que la seule raison pour laquelle je les ai rejointes, c'est Shizune. Son sens de la compétition et sa volonté sont ahurissants."


"Je ne peux pas dire ça à Misha cela dit."

show misha sign_smile
with charachange


mi "D'accord, Hicchan, revoyons ce que tu as appris en classe aujourd'hui."


hi "Tu ne sais même pas ce que j'ai appris en classe aujourd'hui."

show misha hips_grin
with charachange


mi "Mh~, tu as raison, Hicchan~ ! D'accord, commençons avec les bases alors~ ! Je vais juste tout t'apprendre depuis le début~ !"


hi "Tu rigoles j’espère ?"

show misha perky_confused
with charachange


mi "Hein~ ?"


hi "Tu es sérieuse ? Ça représente plusieurs jours de cours et on n'apprend même pas au même niveau..."

show misha sign_smile
with charachange


mi "C'est comme le vélo, Hicchan~ ! On n'oublie jamais les bases ! Wahaha~ !"

show misha sign_confused
with charachange


mi "Je ne sais pas comment faire du vélo, cela dit~..."


"Oh non."

show misha hips_grin
with charachange


mi "Bien, bien~. Je vais devenir un professeur un jour, donc bien sûr je sais ce que je fais... D'accord~ ! D'accord d'accord d'accord~ ! On commence~ !"

stop music fadeout 3.0

show misha perky_confused
with charachange


mi "Euh..."

show misha sign_confused
with charachange

mi "…Mmm~…"

show misha perky_sad
with charachange

mi "Ahahaha~…"


"On dirait qu'elle est très concentrée, donc ça pourrait mal tourner. Apprendre une langue est bien différent de l'enseigner et le premier pas est généralement le plus dur. Honnêtement, je n'aurais pas pu faire mieux que ça."


"Cependant..."

show misha sign_confused
with charachange


mi "Hum... La langue des signes a été créée au dix-huitième siècle par un Français nommé... ah... dont je ne n'arrive pas à prononcer le nom, et il a créé la première école pour sourds en 1755, mais l'histoire de la langue des signes est..."

show misha sign_sad
with charachange


mi "Je ne sais pas vraiment où commencer. Désolée~... Bon~, quoi de mieux pour commencer que l'histoire de la langue des signes ? Hein~ ? Hein~ !"

show misha hips_grin
with charachange


mi "Non, attends, peut-être l'alphabet. D'accord~, va pour l'alphabet, alors !"

play music music_another fadein 0.5

show misha sign_smile
with charachange


mi "D'accord, Hicchan~ ! C'est plutôt basique, même si certaines personnes pensent que ça constitue tout le langage et oublient qu'il y a plein de gestes et mots spécifiques."

show misha hips_smile
with charachange


mi "Mais tu ne peux aller nulle part sans les bases ! Ça c'est A. Tu le vois ? Maintenant, essaye !"


hi "Je le sais déjà ça, hein."


"Mais je coopère quand même."

show misha hips_grin
with charachange


mi "Hahaha ! Ouais, c'est ça !"

show misha sign_smile
with charachange


mi "Maintenant, c'est B, et ça c'est C."


"Misha fait un signe avec chaque main, sans spécifier lequel est lequel."

show misha perky_smile
with charachange

show misha sign_smile
with charachange

show misha hips_grin
with charachange


mi "Et maintenant, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, VWXY et Z~ !"


"Ouais, c'est pas bon."


hi "Tu crois que Shizune voudrait quand même faire le travail du conseil ? On pourrait y aller."

show misha sign_smile
with charachange


mi "Bien sûr que non, Hicchan~ !! Allez, on le refait encore une fois ! A, B, C, D, E, F, G, H, I, J, K... À ton tour~ !"


hi "Donc il n'y a pas du tout de travail que le conseil a besoin de faire, ou quelque chose du genre ?"

show misha hips_smile
with charachange


mi "De quoi est-ce que tu parles, Hicchan ? Allez, signe, signe~ !"


hi "Comme ça ?"

show misha sign_smile
with charachange


mi "Non, comme ça !"


hi "Comme..."

show misha perky_smile
with charachange

show misha sign_smile
with charachange


mi "Ça~ !"


hi "Euh... euh..."

show misha perky_sad
with charachange


mi "J'aimerais que Shicchan soit là, ça serait tellement plus facile avec elle. Hahaha, c'est comme ça que la langue des signes est apprise la plupart du temps de toute façon, avec deux instructeurs~ ! Tu le savais, Hicchan ?"


hi "Non."


"J'imagine ce que ce serait si Shizune était là."

"…"

show misha hips_frown
with charachange


mi "Hicchan~ ! Tu regardes ?"


hi "Ouais."

show misha sign_smile
with charachange


mi "Shicchan dit que le langage des signes est différent des autres, parce qu'on doit penser à tout avant de dire quoi que ce soit. Ça veut dire que chaque mot a plus de poids, Hicchan. Chaque mot est plus important que s'il est dit normalement."

show misha cross_smile
with charachange


mi "Donc~, fais attention, s'il te plaît."

show misha sign_smile
with charachange


"Elle continue son discours sur les bases du langage des signes. Finalement elle commence à parler de trucs que je pourrais reconnaître."


"À la fin, je suis impressionné. Ça a pris un moment pour en arriver là, mais en tant que professeur, elle est plutôt douée quand elle s'y met sérieusement."

stop music fadeout 4.0

scene bg school_roof_ss
show misha sign_smile_ss at center
with shorttimeskip


"Après un moment je remarque qu'il se fait tard, alors je remercie Misha, je lui dis au revoir, et retourne au dortoir."

stop ambient fadeout 1.0

scene bg school_dormhisao_ss
with locationskip


"J'ai appris beaucoup de choses aujourd'hui."

scene black
with dissolve



label fr_S10:

play sound sfx_doorknock

scene bg school_dormhisao
with vpunch


"Je suis réveillé par des coups de massue contre ma porte."


"Ma première pensée est que ça puisse être Shizune. Après tout, seule une personne sourde frapperait aussi fort à cette heure."


hi "Qui est-ce ?"


"Bien sûr, si c'est Shizune, elle ne sera pas capable de m'entendre ou de me répondre."


"Il n'y a pas de réponse, alors je suis plutôt content. Je n'ai pas vu Shizune depuis un moment."

play sound sfx_dooropen

scene bg school_dormhallway
show kenji tsun at center
with locationchange

play music music_kenji fadein 2.0


"Ouvrant la porte, je trouve Kenji debout dans le couloir, ses yeux jonglant de droite à gauche."


hi "Oh, c'est toi."

show kenji neutral
with charachange


ke "Ouais, c'est moi. C'est quoi cette réaction ?"


hi "J'aurais pu te donner une réponse plus personnalisée si tu avais répondu quand j'ai demandé qui c'était."

show kenji tsun
with charachange


"Kenji fronce les sourcils et remonte ses lunettes exactement comme Shizune."


ke "Pourquoi est-ce que tu fais cette tête bizarre ?"


"Je me demande comment il est capable de me voir faire une tête bizarre, alors qu'il n'en a jamais été capable le million d'autres fois où c'est arrivé. J'aimerais bien savoir, mais suis trop fatigué pour continuer la conversation."


hi "Shizune remonte ses lunettes exactement comme ça. Tu sais, la présidente du Conseil des Étudiants. C'est un peu bizarre."

show kenji rage
with charachange


ke "Hein ? Tu veux dire qu'il y a une fille qui fait la même chose ? Tu veux dire qu'elle touche ses lunettes ? C'est moi qui fais ça, c'est mon truc."


ke "Qui c'est cette pétasse ? Pourquoi est-ce qu'il y a toujours des pétasses sur mon chemin, volant ce que je fais ?"

show kenji tsun
with charachange


"Son caractère passe de la colère à la peur en un clin d’œil."


ke "Est-ce qu'elle essaye de me remplacer ? Avec un clone ? Non, ça serait une copie exacte. Un clone femelle ?"


ke "C'est comme si elles avaient combiné mes deux plus grandes peurs."

show kenji rage
with charachange


ke "Voilà !"


"Je n'arrive pas à croire ce qu'il dit..."

show kenji neutral
with charachange


ke "Hé, tu vas en ville aujourd'hui ?"


hi "Euh, peut-être plus tard."

show kenji happy
with charachange


ke "Ok. Super. J'ai... des trucs que je voudrais que tu prennes pour moi à la poste. Des trucs délicats et secrets."


"Il parle en murmurant, comme si parler de son courrier avec une voix normale allait le mettre en danger."


hi "Tu peux faire envoyer ton courrier directement ici, tu sais."

show kenji neutral
with charachange


ke "Non je peux pas. Tu peux te faire envoyer ton courrier à l'école et puis le Conseil des Étudiants le prendra puis elles te le donneront. Ce n'est pas la même chose que si mon courrier apparaissait dans mes mains."


ke "Je ne fais pas confiance au Conseil des Étudiants. Plein de gars ne reçoivent pas leur courrier, tu sais."

show kenji tsun
with charachange


ke "Elles le volent sûrement ! Elles pensent que juste parce qu'elles le reçoivent, elles ont le droit de le voler ? Je peux les voir, nageant dans le courrier, attrapant ce qui les intéresse. Révoltant."


hi "Où est-ce que je peux trouver ce facteur qui peut transformer l'air en courrier pour toi ?"


ke "Je ne sais pas. J'imagine que le Conseil des Étudiants a décidé de le tuer pour préserver son monopole et tous les trucs des étudiants."


hi "Ça ne marche pas comme ça."


hi "C'est ce que tu voulais, hein ? D'accord, j'irai prendre ton courrier, mais un jour tu me revaudra toutes ces faveurs. Tu me dois déjà de l'argent."

show kenji neutral
with charachange


ke "Merci de me le rappeler. Je te rembourserai une fois que j'aurai mon paquet."


ke "Ouais, désolé, je ne peux pas te payer d'ici là. Je n'ai pas d'argent."


hi "Alors je le fais pour l'argent, comme un job. Pourquoi tu as besoin du paquet en premier ? Il y a de l'argent dedans ?"

show kenji happy
with charachange


ke "Nan."


"Je ne comprends vraiment pas."


hi "Pourquoi tu peux pas aller le chercher toi-même ?"

show kenji neutral
with charachange


ke "Parce que je dois réorganiser ma chambre en salle de guerre."


ke "Alors que les jours passent, je réalise de plus en plus à quel point le féminisme est dangereux. C'est vraiment partout, même dans des endroits comme l'Iran. Tu ne peux pas savoir jusqu’où ça va."

show kenji tsun
with charachange


ke "Quand la guerre commencera, si nous n'avons pas transcendé le concept de nation pour nous battre pour notre genre, ça sera le chaos."


ke "Personne ne saura qui sera de quel côté, et une guerre contre les féministes ne voudra pas seulement dire que ce sera la Troisième Guerre Mondiale, mais aussi la fin de la vie sur terre telle qu'on la connaît."


ke "Si on perd, toutes nos femmes japonaises seront violées et mises en esclavage par une bande de lesbiennes sociopathes suprémacistes."


ke "Pendant ce temps, le peu d'hommes qui ne seront pas morts à la guerre seront castrés et forcés à réparer les toilettes ou construire des immenses monuments commémorant la victoire féministe."


hi "C'est dingue. Tu es dingue. Je crois que tu réfléchis trop."


ke "Alors que les jours passent, je me rends vraiment compte que t'es pas dans le coup."


hi "On a dû parler, genre, quatre fois ensemble."

show kenji neutral
with charachange


ke "Oh, désolé."


hi "Ouais, peu importe, j'irai te chercher ton paquet."

show kenji happy
with charachange


ke "Cool."

play sound sfx_doorslam

stop music fadeout 0.5

scene bg school_dormhisao
with vpunch


"Je ferme la porte et retourne directement dans mon lit."

play ambient sfx_alarmclock


"À la seconde où ma tête atterrit sur l'oreiller, un bruit m'agresse les oreilles et je remarque que c'est mon réveil. L'alarme qui se déclenche signifie que c'est le moment où je suis censé me réveiller à la base."


"En semaine, du moins."

play sound sfx_impact


"Je le ramasse et le jette sans même regarder. Il se retrouve coincé entre le lit et le mur mais le bruit ne s’arrête pas. En fait, il est même encore plus fort."

stop ambient


"Au moment où je suis sur le point de le sortir de là, je sais que je ne serai pas capable de me rendormir. La seule chose que je pense faire maintenant est aller en ville et prendre le fichu colis de Kenji, mais il est trop tôt pour ça."


"Après m'être lavé, je prends mes médicaments. J'ai très faim ce matin vu que je n'ai pas dîné hier soir et qu'avant ça j'ai pris un déjeuner léger."


"Je prends mes pilules, les avalant rapidement. Elles sont incroyablement amères et dégoûtantes."


"Les bons médicaments ont toujours mauvais goût. J'ai toujours faim et j'ai encore du temps à perdre, alors je décide d'aller en ville pour trouver un endroit où déjeuner."


"Je n'arrive pas à me souvenir de la dernière fois où j'ai mangé à l'extérieur. En plus, il fait beau, alors pourquoi pas ?"

scene bg school_road
with locationskip

play music music_soothing fadein 3.0


"La marche jusqu'en ville est plus longue que ce dont je me rappelle, sûrement parce que ça fait un moment et aussi parce que j'y vais rarement seul. Vu qu'il est tôt, il n'y a presque pas de voitures, ce qui rend le trajet inhabituellement silencieux."

scene bg suburb_roadcenter
with locationchange


"La première chose que je fais est chercher un endroit où manger. Je pense immédiatement au Shanghai, mais je veux quelque chose de plus consistant qu'un sandwich ou un gâteau."


"Mais vu qu'il est encore tôt, je décide d'aller chercher le paquet de Kenji d'abord."


"Aller le prendre à la poste n'est pas long en soi, mais au moment où je le vois, je réalise qu'il va être chiant à ramener à l'école et j'enrage."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

show kenjibox:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)


"La boîte est énorme, j'ai besoin de mes deux mains pour la porter. Cela dit, elle est tellement légère que la porter à deux mains en est presque insultant."


"Je pensais me balader un peu, mais avec ce truc, ça va être un gros problème. J'imagine que le Shanghai est ma seule option maintenant."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

show kenjibox:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide kenjibox
with None


"Tous les autres sont fermés et ceux qui ne le sont pas ont tous à peu près le même menu. Ça me donne envie d'aller faire tourner le salon de Yuuko."

stop music fadeout 4.0

scene bg suburb_shanghaiext
with locationchange


"Avant même que je puisse ouvrir la porte, quelqu'un me tape sur l'épaule. Je me tourne et je vois Shizune. Instinctivement, je cherche Misha, mais elle ne semble pas être là."

show shizu adjust_happy at center
with charaenter


ssh "Bonjour."


"On dirait que les cours ont déjà commencé à porter leurs fruits. Je suis tenté de lui répondre avec des signes, mais elle pourrait croire que j'en connais beaucoup plus que ça, ce qui est faux."


"Pour l'instant, je lui fais juste un geste de la main et j'ouvre la porte. Elle est probablement là pour son thé matinal et pas seulement pour me saluer. Il s’avère que j'ai raison, vu que Shizune me suit dans le salon de thé."

play sound sfx_storebell

scene bg suburb_shanghaiint at bgright
with locationchange


"C'est une ville fantôme à l'intérieur. Ça a beau ne pas être une heure de pointe, un autre café aurait déjà au moins quelques clients."


"En fait, le Shanghai est presque vide à chaque fois que j'y passe. Comment cet endroit peut-il encore tourner ?"

show yuukoshang happy_down at center
with charaenter


yu "Bonjour ! Merci d'avoir choisi notre établissement !"

show yuukoshang neurotic_down at Transform(ypos=1.25)
with Dissolvemove(0.2)

play sound sfx_impact
with vpunch

with Pause(0.3)

show yuukoshang neurotic_down at center
with charamove


"Yuuko se penche avec la force d'un coup de hache et se heurte la tête contre la boîte que je tiens, la faisant tomber."

play music music_comedy

show yuukoshang panic_up
with charachange


yu "Oh non, je suis désolée, je suis vraiment désolée, désolée, excuse-moi !"


hi "C'est pas grave, et tu n'as pas besoin de faire ce “Bonjour, bienvenue dans notre établissement !” à chaque fois, vu qu'on se connaît."

show yuukoshang worried_up
with charachange


yu "Mais ça fait partie de mon travail."

show yuukoshang worried_down
with charachange


yu "Vous êtes là tôt, qu'est-ce que je peux vous servir ?"


hi "Je prendrai juste un café pour l'instant."

show shizu invis at right
with None

show yuukoshang worried_down at twoleft
show shizu behind_blank at tworight
show bg suburb_shanghaiint at center
with dissolvecharamove


"Je me demande ce que veut Shizune. Sans Misha, il n'y a pas de façon de savoir, ou même de demander. Je n'ai pas encore appris ça. Elle est là, donc je suis sûr qu'elle veut quelque chose aussi."


hi "Euh, je ne sais pas vraiment ce que veut Shizune. Elle prend quoi d'habitude ?"


hi "Attends, peut-être qu'elle veut quelque chose de différent. Peut-être que tu devrais nous apporter un menu au cas où."


"Je tourne la tête pour en trouver un, mais n'arrive pas à voir où ils sont."

show yuukoshang neurotic_up
with charachange


yu "Menus... Je vais en chercher un."


hi "Hein ?"

show yuukoshang worried_up
with charachange


yu "Hum... il y a des menus. Ils sont juste... rares."


"C'est juste un menu du restaurant, pas une édition collector."

show shizu basic_normal2
with charachange

shi "…"


hi "Bizarre."

show yuukoshang neutral_down
with charachange


yu "C'est ce que dit Shizune ?"


hi "Nan, elle ne peut pas t'entendre. C'est juste bizarre pour un café que tu aies besoin de chercher un menu."

show yuukoshang worried_up
with charachange


yu "Bizarre ?"

show yuukoshang neurotic_down
with charachange


yu "Oui... Tu as raison. C'est illogique. Il y a tant de choses... déjà, pourquoi ça s'appelle le Shanghai ? C'est un salon de type occidental... mais le nom est chinois... et l'architecture est vieille, mais mon uniforme est moderne..."


"On dirait qu'elle est sur le point de s'évanouir. Si elle tombe en avant, elle risque de casser beaucoup de choses."

show yuukoshang panic_up
with charachange


yu "Je ne peux plus travailler ici."


"Son raisonnement s’achève sur une bien sombre pensée."


hi "Non, allez. Ce genre de truc est ce qui rend cet endroit unique. Il y a beaucoup d'autres cafés par ici, tu sais. Je pense que c'est charmant, vraiment. Ne démissionne pas, s'il te plaît. Les affaires vont bien ici, non ?"

show yuukoshang worried_up
with charachange


yu "Pas vraiment..."


hi "Tu sais, je trouve que c'est un bon travail pour toi. Ça te convient bien, tu ne devrais pas démissionner."


"Je n'ai jamais eu à désamorcer ce genre de crise auparavant."

stop music fadeout 2.0





"Finalement, je parviens à la calmer et la convaincre que je suis sûr que Shizune veut juste ce qu'elle prend habituellement."

hide yuukoshang
with charaexit

show shizu basic_normal2 at center
show bg suburb_shanghaiint at bgleft
with charamove

show shizu basic_normal2:
    ypos 1.15
with charamove


"Yuuko part chercher nos boissons et Shizune en profite pour choisir une table."

play music music_dreamy fadein 4.0


"Il n'y a pas d'autres clients et Yuuko n'est pas très bavarde, alors c'est calme."


"Ça ne me gêne pas vraiment, mais j'aimerais qu'on ait un moyen de communiquer. Il y a tellement peu de fois où nous sommes seuls. Shizune et Misha sont presque toujours ensemble et parfois on pourrait croire qu'elles sont la même personne."


"Maintenant, c'est juste elle et moi, et je suis incapable de la comprendre ou de me faire comprendre. C'est terrible."


hi "Tu n'as pas ton petit bloc-notes aujourd'hui ? Je sais que c'est le week-end et tout, mais ça ne te ressemble pas de ne pas être préparée."


hi "Bah, pas grave. Je n'aime pas vraiment m'en servir de toute façon. Ça aurait été pratique cela dit."

show shizu behind_blank
with charachange

shi "…"

show shizu basic_normal
with charachange

shi "… …"


"Shizune commence à faire des signes ponctués par des pauses quand elle boit son thé. C'est bizarre comment elle ne fait aucun effort pour changer sa manière d'agir."


"Je lui parle surtout parce que je ne suis pas habitué aux longs silences. Je me demande si c'est pareil pour elle, d'une certaine façon. Ça m'étonnerait. Je crois qu'elle est plutôt du genre à ne pas changer sa manière d'agir pour les autres."


hi "Hé, on dirait que Misha a rejoint le Conseil des Étudiants à cause de toi. Ça en fait deux, en me comptant. Je suis uniquement là parce que tu m'as forcé."


hi "Bon, pas vraiment forcé, mais si ce n'était pas pour toi, je ne serais pas là."


"Ça fait un peu romantique dit comme ça, et je rougis un peu. Je me sens vraiment bête."


hi "Cela dit, je ne sais toujours pas pourquoi tu as rejoint le conseil. Ça aurait dû être la première chose que j'aurais dû te demander, en y repensant. Il faudra que je me rappelle de le demander à Misha."

show shizu behind_blank
with charachange

shi "…"


hi "C'est agréable de te parler, même si tu ne peux pas me comprendre. Je me demande si c'est pareil pour toi."


hi "Ça serait vraiment... bien."

show shizu adjust_happy
with charachange

shi "…"


hi "Je ne crois pas que je maîtriserai la langue des signes de façon aussi naturelle que Misha un jour, mais c'est déjà un pas en avant par rapport au papier et au crayon, hein ?"

show shizu basic_normal2
with charachange

shi "…"

stop music fadeout 4.0


"On a tous les deux fini nos boissons depuis un moment et les yeux de Shizune dérivent vers le colis posé sur la chaise à côté de moi."

show shizu adjust_happy
with charachange

shi "…"


hi "Je le récupère juste pour quelqu'un, ce n'est pas à moi."


play music music_running fadein 0.5

show shizu basic_sparkle
with charachange


"Shizune le rapproche d'elle, en ayant l'intention de l'ouvrir et je bondis presque. Je passe rapidement ma jambe autour de la chaise pour le garder de mon côté."


hi "Hé, ne l'ouvre pas. Tu ne peux pas ouvrir le courrier des autres, c'est illégal."

show shizu basic_frown
with charachange

shi "…"


hi "Non !"

show shizu cross_angry
with charachange


shi "... !"


"Une fois qu'elle est lancée, il est presque impossible de l’arrêter. Les yeux remplis d'excitation, elle semble prête à se battre contre moi pour ce stupide colis et je réalise rapidement comment ça pourrait devenir une lutte acharnée."

show shizu behind_frown
with charachange


"J'en suis presque debout et agite les bras dans tous les sens comme un contrôleur aérien avant qu'elle ne se calme."

show shizu behind_frown at center
with charamove


"Shizune fait la moue, mécontente de n'avoir pu satisfaire sa curiosité et se lève pour partir."


"Il va être l'heure, j'imagine. On est là depuis un moment. Je prends le colis, protecteur, puis me lève à mon tour."

show shizu basic_happy
with charachange


"Soudainement, elle sort un marqueur de sa poche et commence à écrire sur la boîte de Kenji."


hi "Hé, qu'est-ce que tu fais ? J'ai dit que ce n'était pas à moi !"


hi "Hé !"


"Je ne peux même pas la voir avec le colis qui me bloque la vue."


hi "D'accord, au moins laisse-moi le poser."


"Je dois lire ce qu'elle écrit, de toute façon."

window hide


$ written_note("Je vais t'aider à le porter.", {"background":Frame("vfx/cardboard.jpg",0,0, tile=True)})


show shizu adjust_smug
with charachange

window show


"On ne dirait pas qu'elle a fini et elle fait une grande ligne pour montrer qu'il y a une condition."

window hide


$ written_note("Je vais t'aider à le porter.\n ___________________\n\nMais, on va jouer ! Le premier qui trébuche perd et le perdant doit le porter pour le reste du chemin.", {"background":Frame("vfx/cardboard.jpg",0,0, tile=True)})

window show


hi "C'est stupide, il y a une chance sur deux que je finisse par le porter tout seul de toute façon."


"Je me sens plutôt bête, là. J'ai oublié qu'elle ne pouvait pas m'entendre. J’arrête de parler et secoue la tête."

show shizu behind_blank
with charachange

shi "…"

show shizu cross_angry
with charachange


shi "... !"

show shizu adjust_angry
with charachange


shi "... !"


"Je ne la comprends pas du tout, mais elle fait des signes très enthousiastes. Il est clair qu'elle pense que c'est une très bonne idée."


"Bah, si elle lâche le paquet ou autre, elle devra le porter, ça rendra les choses plus faciles pour moi, évidemment."


"L'enjeu est de 50-50 alors... ce qui est plus que ce qu'elle aurait pu me proposer. D'accord, je suis partant."

show shizu basic_normal_close
with characlose


"En y pensant, je ne sais pas trop comment on devrait faire ça. Alors Shizune attrape un côté de la boîte et la soulève et je décide de prendre l'autre côté. C'est très inconfortable de marcher comme ça."

show bg suburb_shanghaiext
with locationchange


"Nous sortons du café, et je me mets à espérer que les rues soient désertes. Yuuko semble un peu confuse en nous voyant, et j'imagine que ça ne sera pas mieux si d'autres personnes nous voient."

show shizu adjust_happy_close
with charachange

show shizu basic_normal_close
with charachange


"Shizune ne semble pas s'en préoccuper du tout et marche avec son bras sous un angle peu naturel. Elle se contente de sourire, confiante, et fait de temps en temps une sorte de geste bizarre."

show bg suburb_roadcenter
with locationchange


"Il y a des gens qui nous regardent alors que nous marchons et il y a de plus en plus de monde dans la rue au fur et à mesure que le temps passe."


"Je me sens bête, mais je suis sûr que si j'abandonne, Shizune estimera que je me rends. Je ne peux pas accepter ça, parce que je crois que je m'en sors bien jusque-là."

show shizu adjust_happy_close
with charachange

show shizu basic_normal_close
with charachange


"À la base, j'estimais que les petits gestes de la main de Shizune étaient des moqueries, mais je me rends vite compte qu'elle montre en fait les directions où elle souhaite aller."


"Je me rends aussi compte que ce n'est pas une compétition. Ce n'est pas très dur, déjà, et aussi, c'est plus un exercice de travail en équipe. C'est juste que Shizune a mis en place une punition en cas d'échec plutôt qu'une récompense si c'est bien fait."

stop music fadeout 3.0

show shizu adjust_blush_close
with charachange


"Nos doigts se touchent en dessous du paquet et Shizune bouge sa main, faisant presque tomber son côté de la boîte en même temps."


"Bon, game over pour elle."


"Elle ne semble pas très contente. Est-ce qu'elle croit que j'ai fait ça exprès pour qu'elle perde ? Si c'est le cas, elle ne le montre pas. À la guerre comme à la guerre."

show shizu basic_frown
with charadistant


"J'ai l'impression que je devrais le reprendre et le porter moi-même, mais elle me repousse quand j'essaye."

play music music_shizune fadein 1.0


"Elle me regarde comme pour me dire de partir, mais elle ne peut pas. Avec ce paquet dans les mains, elle est comme bâillonnée."

show shizu basic_normal2
with charachange

show shizu basic_normal
with charachange


"Une expression triste s'affiche sur son visage pour une seconde, peut-être en réalisant ça et en voyant qu'il y a des limites auxquelles elle doit faire face, après tout."


"Elle est toujours aussi fière, même si c'est à ses dépens. Elle ne me laisserait pas l'aider à échapper aux conséquences de son pari."


"Tout est valable pendant le jeu, mais le résultat doit être honoré à la lettre dans tous les cas, hein ?"


"Shizune est quelqu'un d’intéressant."

show bg school_dormext_full
with shorttimeskip


"La marche jusqu'au dortoir se passe tranquillement. Shizune passe le temps en bougeant la boîte comme un rubik's cube géant. On dirait que c'est un autre jeu qu'elle a inventé pour s'amuser."


"Ce n'est sûrement pas bon pour ce qui est à l'intérieur, mais je ne m'en préoccupe pas suffisamment pour l’arrêter."


"Peut-être que c'est comme ça qu'elle gère les choses, en faisant de toute situation un jeu, mais il est difficile d'en être sûr, cela dit."


"Il semble futile d'essayer d'analyser Shizune. Depuis le peu de temps qu'on se connaît, j'ai été surpris un bon nombre de fois."

show shizu basic_normal2 at centertremble_nl
with None

stop music fadeout 6.0


"Je remarque que Shizune frissonne. Il y a du vent et l'école est plutôt à une altitude assez haute. C'est normal qu'elle ait froid. Si je lui donnais ma veste, est-ce qu'elle me repousserait ?"

play sound sfx_rustling

show shizu basic_normal2_close at center
with characlose


"Je retire ma veste et la passe autour de ses épaules avant qu'elle ait une chance de protester. Ses épaules sont petites et délicates, tellement que je laisse mes mains se poser dessus."

show shizu adjust_blush_close
with Dissolve(0.2)


"Shizune sursaute alors que mes doigts l'effleurent, visiblement surprise."


hi "Désolé."

show shizu basic_normal_close
with charachange

shi "…"

show shizu adjust_happy_close
with charachange

shi "…"


"Ses doigts glissent un peu sur la surface de la boîte, et j'aimerais l'aider, mais je doute qu'elle me laisserait faire. Shizune fait un signe avec ses mains du mieux qu'elle peut, s’arrêtant un peu après comme si elle voulait en dire plus."


"Je suis sûr qu'elle a voulu dire “merci”. Je suis content d'avoir pu le comprendre."

scene black
with dissolve

$ suppress_window_after_timeskip = True



label fr_S11:

window hide None

scene bg school_cafeteria
with locationchange

nvl clear

nvl show dissolve

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_normal fadein 0.5


n "\n\nLe professeur de langue des signes dit que je suis très doué."


n "J'essaye de ne pas trop y penser, mais la vérité est que je suis tellement impliqué récemment que j'y reviens plusieurs fois par jour. J'imagine que je m'y mets plus rapidement que ce que j'aurais cru, mais ce n'est toujours pas suffisant."


n "Je comprends ; comprendre les signes est facile. Bon, faut quand même que je me concentre, mais ça va quand je le fais."


n "Les signes en eux-mêmes sont faisables. J'ai juste besoin d'un peu plus de pratique. Cependant, essayer de faire les deux à la fois, même deux fois plus lentement que Misha ? Impossible."


n "Je suis assez bon par rapport au niveau où j'en suis, mais pour arriver au point où je pourrai vraiment converser avec Shizune, j'ai besoin de travailler plus."


n "\nJe fais de mon mieux pour m'en approcher pas à pas en étudiant du mieux que je peux durant le déjeuner."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear

nvl hide dissolve

window show


"Je relève la tête de mon livre “Introduction à la Langue des Signes Japonaise” pour vérifier que Shizune et Misha ne sont pas là."


"Bien sûr, puisque durant la pause déjeuner, je les évite depuis quelques jours. Et je vais devoir continuer de faire ça si je ne veux pas que Shizune le découvre."


"Adossé à un coin de la salle, jetant un œil toutes les dix minutes, j'ai l'impression d'être une sorte de criminel essayant de ne pas se faire attraper."

"…"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

nvl show dissolve

nvl clear


n "\n\nChaque fois qu'elle en a la possibilité, Misha me demande pourquoi je veux cacher le fait que j’apprends la langue des signes à Shizune."


n "En y repensant, il n'y avait pas vraiment de raison, mais maintenant je crois savoir."


n "Si je veux que Shizune me traite comme un égal, le langage des signes est une étape importante."


n "Si je veux traiter Shizune comme un égal, alors le langage des signes est une étape importante."


n "Une autre étape importante est de s'assurer qu'elle ne le sait pas, et que quand on sera capables d'enfin discuter, je sois complètement prêt, capable de vraiment le faire, pas juste à peu près."


n "Moins que ça serait insultant. Elle le verrait de la même façon."


n "Alors pour moi, c'est la seule option. Surtout maintenant que je suis résolu à le faire."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear

nvl hide dissolve

window show


"Shizune a une forte présence. Il est très facile de la voir arriver, ou même de la sentir arriver. Surtout parce que les cheveux de Misha font d'elle un phare et qu'on peut entendre son rire à des kilomètres à la ronde."


"Cela dit, même si Misha n'était pas avec elle, ce serait pareil. Elle est si directe et efficace que ce ne serait pas surprenant que ça se ressente quand elle marche."


"Grâce à cela, je suis capable de tout ranger et d'afficher ma meilleure expression neutre avant qu'elles ne me voient et me rejoignent."

show shizu behind_smile at tworight
show misha perky_smile at twoleft
with charaenter


hi "Salut."

show shizu adjust_smug
with charachange


ssh "Conseil des Étudiants."

show misha hips_grin
with charachange


mi "Conseil des Étudiants~ !"


"“Conseil des Étudiants” a été la première chose que j'ai demandé à apprendre, j'ai pensé que ça pourrait être pratique."


hi "Ouais, j'évite ça depuis un moment, hein ?"

show misha sign_smile
show shizu behind_smile
with charachange


mi "Yep~ !"

show shizu behind_smile_close at closeright
show misha perky_smile_close at closeleft
with characlose

show shizu behind_smile_close:
    ypos 1.07
show misha perky_smile_close:
    ypos 1.1
with charamove

stop music fadeout 3.0


"Shizune s'assied en face de moi à droite, et Misha à gauche. J'ai fait l'erreur de me mettre dans un coin. Maintenant je suis... coincé."

scene bg school_lobby
with shorttimeskip


"Je me retrouve à être traîné dans la salle du conseil des étudiants, mais ça ne me gêne pas. Elles commençaient à me manquer un peu, de toute façon."


"D'une certaine façon, ça facilite les choses : satisfaite de m'avoir attrapé, Shizune ne demande pas ce que je faisais pendant tout ce temps."


"Une fois que je me tiens devant la porte, je me demande ce qui pouvait être si important pour qu'elles veuillent me ramener à ce point."

scene bg school_council at bgright
with locationchange


hi "Des jeux."

play music music_another fadein 0.5


"Il y a plus de jeux que de livres. Ça explique pourquoi, à chaque fois que je viens ici, il y a plein de livres entassés sur les tables et sur le sol. Elles ont besoin de place pour ranger les jeux."

show misha cross_laugh
with charaenter


mi "Hahaha~ !"

show misha hips_grin
with charachange


mi "C'est ennuyeux de jouer juste à deux, Hicchan. Donc c'est ton tour, d'accord ? D'accord~ ! C'est réglé~ !"


hi "Je n'ai encore rien dit !"

show shizu invis at right behind misha
with None

show misha hips_grin at twoleft
show bg school_council at center
show shizu basic_normal at tworight
with dissolvecharamove

show shizu behind_blank
with charachange

shi "…"

show misha sign_smile
with charachange


mi "Hicchan, c'est l'un des derniers jours où tu pourras te la couler douce avant un moment. Alors~ il est important qu'on en profite le plus possible, tu ne crois pas ?"

show misha cross_smile
with charachange


mi "Il y aura bientôt Tanabata et on va devoir beaucoup travailler."

show misha hips_grin
show shizu behind_smile
with charachange


mi "Alors, pour l'instant, joue avec nous~ !"


"En y pensant, c'est vrai. Je ne m'en suis pas rendu compte parce que j'étais trop occupé à apprendre la langue des signes. Juste après un festival, un plus gros apparaît."


"Je me demande si Shizune essayera d’enrôler quelques autres membres pour nous aider avec celui-là aussi."


hi "Tu as raison."

show misha cross_laugh
with charachange


mi "Hahaha~ ! Yay~ ! Hicchan est d'accord~ ! Ça se fête !"

show shizu basic_happy
with charachange


ssh "On devrait jouer à un jeu."

show misha sign_smile
with charachange


mi "Jouons à quelque chose pour célébrer ça, Hicchan~ !"


hi "Je ne sais pas trop, ce genre de choses finissent généralement mal pour moi."

show misha perky_sad
with charachange


mi "Hicchan est inquiet pour les enjeux~."


"Misha affiche une expression déçue. C'est difficile de dire si elle se moque de moi, vu que ses expressions sont tellement exagérées le reste du temps. Elle est le genre de fille à toujours tout faire à fond."


"Je tourne la tête vers Shizune. Elle, cela dit, se moque clairement de moi."


hi "Hé, c'est bon. Oui, je vais jouer avec vous si vous me dites les enjeux d'abord."

show shizu adjust_smug
with charachange

shi "…"

show misha cross_grin
with charachange


mi "Très japonais, mettre les conséquences devant tout le reste."

show misha sign_smile
with charachange


mi "Hicchan, tu as déjà entendu l'expression “l'arbre qui cache la forêt” ?"


hi "Non."


"C'est un mensonge. Mais j'ai ma fierté qui est actuellement blessée."


hi "D'accord, je joue, mais je choisis le jeu."

show shizu adjust_happy
show misha perky_smile
with charachange


"Misha hoche la tête."


hi "Et aussi, je choisis le gage si vous perdez."

show shizu cross_angry
with charachange


"Shizune fait un X avec ses bras. Soit ça veut dire “non”, ou alors elle est sur le point d'utiliser son attaque spéciale."


hi "Aha, qui a peur des conséquences maintenant ?"

show shizu behind_frown
with charachange


ssh "Tu es vraiment rancunier pour une si petite blague innocente."

show shizu basic_frown
with charachange


ssh "Si un ... te mordait, tu le mordrais probablement aussi."


"Shizune a fait un signe que je n'ai pas compris."

show misha hips_frown
with charachange


mi "Hicchan est vraiment rancunier~ même si c'était juste une petite blague innocente. Si un tatou te mordait, tu le mordrais probablement aussi !"


hi "Tatou ?"

show misha sign_smile
with charachange


mi "C'est méchant de mordre un tatou, Hicchan !"

show shizu behind_blank
with charachange

shi "…"

show misha cross_laugh
with charachange


mi "Mais Hicchan le ferait quand même, hein~ ! Hahaha !"


hi "Je vois."

show shizu adjust_smug
with charachange


"Shizune ajuste ses lunettes avec un petit geste de la main."

show shizu behind_smile
with charachange

shi "…"

show misha sign_smile
with charachange


mi "Hicchan, on n'avait rien prévu en cas de victoire ou de défaite, tu as juste supposé qu'il y aurait quelque chose comme ça~."


hi "Je me demande pourquoi."

show misha hips_grin
with charachange


mi "Mh~, moi aussi~ ! Mais pas grave~ ! Il n'y en a pas. Ça ne te fait pas changer d'avis, Hicchan ?"


hi "Bon... oui."

show misha hips_laugh
with charachange


"Misha secoue les bras à pleine vitesse pour montrer sa joie. Drôle d'habitude. C'est le genre de choses qu'on ne peut voir que dans la salle du conseil des étudiants, là où il n'y a que trois personnes."


"Ailleurs elle aurait fini par taper quelqu'un."

show misha hips_grin
with charachange


mi "Ouais ouais~ ! Commençons~ !"


hi "Pas tout de suite."

show misha hips_smile
with charachange

mi "…"

show shizu behind_blank
with charachange

shi "…"

mi "…"

shi "…"


hi "D'accord, d'accord."


hi "Cependant, on doit tous être capables de jouer. C'est ma condition."


hi "J'aime pas les jeux où dès le début un joueur est clairement dominant, ou les jeux où seulement deux personnes peuvent jouer et que la dernière personne est mise à l'écart. Ça doit être un jeu qui se joue à trois à capacité égale."

show shizu basic_normal
with charachange

shi "…"

show misha sign_smile
with charachange


mi "Les dames ?"


"À l'instant où elle dit ça, Misha sort un jeu de dames et le place sur la table."


hi "On ne peut y jouer qu'à deux. Je t’ai dit—"

show misha hips_grin
with charachange


mi "D'accord d'accord~ ! Hicchan, et... le Monopoly ?"


"Une boîte de Monopoly se dirige lentement vers moi alors je le prends des mains de Misha et le mets sous ma chaise."


hi "Je n'aime pas les jeux qui sont basés sur la chance plutôt que sur le talent. Et puis aussi, arrête de sortir les jeux comme ça !"

show misha perky_confused
with charachange


mi "La chance est un talent aussi, tu sais."


hi "Non, pas du tout !"

show shizu adjust_smug
with charachange

shi "…"

show misha sign_smile
with charachange


mi "Ça peut compter si tu es toujours chanceux~ ! Hein~ ?"


hi "À ce niveau-là, c'est autre chose."

show shizu adjust_happy
show misha hips_grin
with charachange


mi "Mh~, mh~ mh~ mh~~. Baccarat ? Billes ? Destins ? Jeu de l'oie ? Roulette ? Blackjack ? Foot en papier ? Trivial Pursuit ?"


"Misha commence à énumérer des tas de jeux avec excitation comme si elle lisait une liste."


"Après chaque suggestion, une nouvelle boîte, planche ou des pièces apparaissent autour d'elle, des jeux commençant par ceux pour enfants, jusqu’à ceux pour adultes avec des accessoires dignes des casinos qui font tache dans cette pièce."

show misha sign_smile
with charachange


mi "Échecs à trois ?"


hi "C'est possible ça ?"

show shizu behind_smile
with charachange


ssh "Essayons."

show misha cross_laugh
with charachange


mi "Oui oui~, essayons, allons-y~ ! Ahahahaha~ !"

show shizu basic_happy
show misha hips_grin
with charachange


"Elles sortent un jeu d’échecs de derrière elles comme deux jeunes magiciennes. La magie nécessite un habile jeu de main, et ça elles l'ont."


"Je ne suis pas surpris. Néanmoins, c'est toujours un peu perturbant."


hi "Arrêtez de faire ça !"

stop music fadeout 2.0


ha "E-excusez-moi... ?"

show shizu basic_normal
show misha perky_confused
with charachange


"Une voix très timide arrive à attirer mon attention."

show hanako invis at offscreenright
with None

show misha perky_confused at left
show shizu basic_normal at center
show bg school_council at bgleft
show hanako emb_downtimid:
    xanchor 0.7 xpos 1.0
with dissolvecharamove


ha "J'ai p-perdu ma carte étudiante, et quelqu'un m'a dit... que je pourrais en avoir une nouvelle ici. Si j’interromps q-quelque chose, je peux revenir plus tard."

show hanako emb_timid
with charachange


"Les yeux de Hanako parcourent la salle, voyant les livres empilés, les chaises éparpillées et les jeux de société partout."


"J'imagine que ce n'est pas vraiment l'image organisée et sérieuse qu'un Conseil des Étudiants comme le nôtre devrait donner."


hi "Bonjour."


"C'est la seule chose que j'arrive à sortir pour briser la glace. Malheureusement, ça semble juste l'effrayer un peu plus."

show hanako def_worry
with charachange

ha "…"

show hanako def_strain
with charachange


ha "Ah…{w=0.5} ma carte étudiante…{w=0.5} Je…"

show misha sign_smile
with charachange


mi "Tu es dans notre classe, n'est-ce pas ? Hein~ ! Donc~ ! Ne sois pas si timide, d'accord ? Allez !"

show shizu behind_smile
with charachange

shi "…"

show misha hips_grin
with charachange


mi "Yep, même si nous sommes tes aînés, ce n'est pas comme si nous allions te mordre !"


hi "Nous ne sommes pas ses aînés, on est dans la même classe."

play music music_happiness fadein 3.0


"Cela dit, je suis quand même content qu'elles soient intervenues."

show misha hips_smile
with charachange


mi "Qu'est-ce que tu voulais ? Une carte étudiante hein~ ? Hein~ !"

show hanako basic_distant
with charachange


ha "Oui."


"Ses yeux dévient de Misha. Étant timide, ça ne m'étonne pas qu'elle ait du mal à regarder longtemps quelqu'un dans les yeux. Je suis son regard et remarque qu'il s’arrête sur l'échiquier sur la table."

show hanako basic_normal
with charachange

show hanako basic_distant
with charachange


"Les yeux de Hanako s'écarquillent, juste pour une seconde. Shizune le remarque aussi."

show shizu basic_happy
with charachange

shi "…"

show misha perky_smile
with charachange


mi "Tu aimes les échecs ?"

show hanako defarms_strain
with charachange


ha "Eh ?!"

show shizu adjust_smug
with charachange


shi "... !"

show misha hips_smile
with charachange


mi "Tu aimes les échecs, n'est-ce pas~ ? Ouais, tu aimes, c'est clair~ !"

show misha hips_grin
show shizu adjust_happy
with charachange


mi "Est~{w=0.2} ce~{w=0.2} que~{w=0.2} tu~{w=0.2} veux~{w=0.2} jouer~ ?"


"Hésitation. Elle pourrait accepter. Je refuse d'être impliqué dans tout ça, ça va mal finir."

show hanako basic_normal
with charachange


"À mon grand étonnement, Hanako semble envisager l'idée très sérieusement. Elle se touche le bout des doigts, pensive, réfléchissant."


"À ce niveau, c'est plus ou moins un accord."

show misha sign_smile
with charachange


mi "On est en pause déjeuner, tu vas devoir attendre de toute façon. Viens jouer avec nous en attendant~ ! Allez, ça va être fun, vraiment fun~ ! Tu aimes les échecs, hein ? Je peux le dire vraiment, c'est évident~ ! S'il te plaît~."

show hanako cover_distant
with charachange


ha "D'accord..."

show misha cross_laugh
with charachange


mi "Wahaha~ ! Yay~ ! Victoire, victoire, ouais ouais ouais~ ! C'est super~"

scene ev shizu_chess_large:
    subpixel True xanchor 1140 yanchor 1100 xpos 400 ypos 300 zoom 1.0
    easein 10.0 yanchor 1050
with flash




"L'échiquier est mis en place."


"Le premier coup est important."

show ev shizu_chess_large:
    ease 1.0 xpos 400 xanchor 1400 yanchor 400 ypos 300
    acdc_warp 10.0 xanchor 1300


"Cependant, Shizune ne semble pas s'en soucier."

show ev shizu_chess_large:
    ease 0.5 xanchor 800 yanchor 360
    easein 10.0 xanchor 700 yanchor 360


"Hanako prépare ses mouvements avec précaution, glissant les pièces légèrement en avant puis les reculant par incertitude, repensant ses coups plusieurs fois."


"Elle est vraiment à fond dedans, on voit qu'elle est plus qu'une joueuse occasionnelle."


"Shizune ne peut pas se permettre de la prendre à la légère, quoi qu'elle fasse, Hanako a une réponse appropriée."


"Et pourtant il y a quelque chose de bizarre avec le rythme de la partie."

scene ev shizu_chess_base:
    truecenter subpixel True zoom 1.05
    easein 5.0 zoom 1.0
with flash


"Shizune joue trop vite. Non, pas trop vite, mais à une vitesse phénoménale. C'est comme si elle ne pensait pas à son prochain coup. Soit elle a la puissance de calcul d'un superordinateur, soit elle ne prend pas le jeu très au sérieux."


"Ou peut-être que Hanako n'est pas très douée."

scene ev shizu_chess_base
show sc_shiz normal:
    xalign 1.0 yalign 0.0
with charachange


"Shizune force une destruction mutuelle de pions."

scene ev shizu_chess_base3
with charachange


"Les tours de Hanako durent de plus en plus longtemps. Soudainement tout devient clair, Shizune a beaucoup plus de temps pour penser à son tour pendant que Hanako prévoit le sien."


"Malgré ça, ça reste une partie intéressante."

window hide

nvl clear

$ renpy.music.set_volume(0.5, 1.0, channel="music")

nvl show dissolve


n "\n\nCavalier en f6."


n "Fou en d3."


n "Vu qu'elles jouent toutes les deux sérieusement, personne ne prend ça à la rigolade. Il n'y a pas de dominant, du moins pour l'instant. Peut-être que le fait qu'elles ne soient pas très proches aide à ce qu'elles ne se fassent pas de cadeau."


n "Shizune est un adversaire mystérieux pour Hanako, et Hanako est une énigme pour Shizune. Les sourcils froncés de Hanako montrent qu'elle est très concentrée dans la partie. Elle veut gagner, tout comme Shizune."


n "Leur manque de familiarité est un peu déprimant, mais ça donne de la vie au jeu et leur permet d'être compétitives."


n "Peut-être qu'elles pourraient même finir par devenir amies avec ça, ou au moins, rivales. C'est une pensée optimiste."


n "Bien que je me rappelle la partie de Risk que j'ai menée contre Shizune, elle ne veut pas écraser les gens juste pour s'amuser."

nvl clear


n "\n\n\nLe jeu continue."


n "Shizune fait douze mouvements en quatre minutes. Quel adversaire effrayant."


n "Mais Hanako tient bon, même si son roi se fait quelque peu poursuivre."


n "Pion en h6."


n "Cavalier en e6."


n "La fin est proche."


n "\n\n..."

stop music fadeout 3.0


n "Et c'est fini."

nvl clear

nvl hide dissolve

scene bg school_council
show shizu adjust_happy at center
show misha perky_smile at left
show hanako basic_normal at right
with locationchange

window show

shi "…"

show misha sign_smile
with charachange


mi "C'était une très bonne partie~ !"

$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_ease fadein 5.0

show hanako cover_bashful
with charachange


ha "M-merci..."

show shizu behind_smile
with charachange

shi "…"

show misha hips_smile
with charachange


mi "C'était vraiment limite~, j'ai cru que j'allais perdre. Tu es très douée."


"Humble dans sa victoire. Peut-être que c'est parce que Hanako ne prend pas mal sa défaite."

show shizu basic_normal
with charachange

shi "…"

show misha perky_smile
with charachange


mi "C'était fun, mais très long. Presque l'heure entière !"


mi "Les échecs sont trop limités, surtout à ce niveau. Que dirais-tu d'une partie avec des règles avancées~ ?"


hi "Quoi ?"

show hanako cover_worry
with charachange


ha "A... vancées... ?"

show shizu basic_sparkle
with charachange

show shizu adjust_smug
with charachange

show shizu basic_happy
with charachange

shi "… … …"

show misha hips_smile
with charachange


mi "Ouais, ouais~ ! Comme avec du temps limité, ou avec des pièces en plus, avec un ou deux échiquiers, comme tu veux ! Allez allez allez allez, ça sera fun, vraiment, vraiment~ ! Les échecs normaux sont trop lents, trop méthodiques, trop ennuyeux."

show misha hips_grin
with charachange


mi "Je veux jouer à des jeux d'échecs qui récompensent ceux qui réfléchissent vite, et ceux qui osent ! N'importe lequel d'entre eux, comparé aux échecs, est comme comparer les dames et le go, ou le morpion et le shogi, hein ? Hein~ !"

show misha cross_laugh
with charachange


mi "Wahahaha~ ! Même les échecs laser pourraient être plus excitants, choisis quelque chose, choisis~ !"

show hanako defarms_strain
with charachange

ha "Aaaah…"


"Comme un lapin pris dans les phares d'une voiture. Plusieurs émotions émergent en moi alors que je regarde Hanako devant l'échiquier presque sur le point de s'évanouir. Je suis aussi amusé, mais me rapproche un peu au cas où elle basculerait."

scene ev shizu_chess_base2:
    truecenter subpixel True zoom 1.05
    easein 5.0 zoom 1.0
with flash


"L'échiquier est mis en place encore une fois, mais cette fois, le déroulement n'est pas le même."


"Hanako ne peut même pas faire un mouvement de peur que sa main touche celle de Shizune. Elle est partout sur le jeu. C'est un massacre. Partout où Hanako veut mettre une pièce, Shizune est déjà là."


"C'est la partie la plus rapide que je n'ai jamais vue."

scene bg school_council
show shizu basic_sparkle at center
show misha hips_grin at left
show hanako defarms_strain at right
with locationchange


mi "Changeons les règles et jouons encore~ ! Prenons le meilleur des six, comme Kasparov et Deep Blue~ !"

hide hanako
with easeoutright


"Hanako s'excuse et s'enfuit de la pièce."

show shizu basic_normal
show misha perky_confused
with dissolve


mi "Hein ? Attends !"

hide misha
with charaexit


mi "Ah, elle ne voulait pas une nouvelle carte ? Excuse-moi ! Hey oh~ ? Reviens, s'il te plaît ! Attends, attends~ ! Attends~ !"

stop music fadeout 3.0


"Étrangement, plus Misha est loin, plus sa voix semble être forte."

show bg school_council at bgright
show shizu basic_normal at tworight
with charamove

show misha perky_sad at twoleft
with charaenter


mi "Je n'ai pas pu la rattraper."

show shizu adjust_happy
with charachange

play music music_normal fadein 3.0

shi "…"


"Shizune tapote gentiment son épaule pour la rassurer."


hi "Là, là."

show misha hips_smile
with charachange


mi "Là, là~ !"


hi "Tu es plutôt joyeuse pour quelqu'un qui avait besoin d'être rassurée."

show misha cross_laugh
with charachange


mi "Ahahaha~ !"

"…"

show shizu basic_normal2
with charachange

shi "…"

show misha sign_smile
with charachange


mi "Hicchan, tu n'aimes pas les jeux avec de la chance ?"


"Une question sortie de nulle part, mais elle semble vraiment importante."


"Si elle ne l'était pas, pourquoi est-ce que Shizune me regarderait, attendant ma réaction ? Quand je jette un coup d’œil dans sa direction, elle fait semblant d'être occupée à jouer avec une pièce d’échecs."

show misha hips_grin
with charachange


mi "“Je n'aime pas les jeux qui sont basés sur la chance”, n'est-ce pas ? C'est toi qui as dit ça, Hicchan."


hi "Ouais. Mais que le jeu soit basé sur la chance, ce n'est pas pareil qu'un jeu contenant des éléments de chance. Je n'ai rien contre ceux-ci. C'est le cas de la plupart des jeux de toute façon. C'est ce qui rend le jeu intéressant."


hi "Je crois qu'un jeu où tu sais dès le début jusqu’où tu peux aller est ennuyeux. Ce n'est pas un jeu, alors. C'est juste enchaîner des étapes."


hi "Je ne crois pas que je pourrais apprécier un jeu où on n'a presque aucun contrôle sur ce qui se passe."

show shizu behind_smile
with charachange


ssh "Je vois."

show shizu adjust_smug
with charachange

shi "…"

show misha hips_smile
with charachange


mi "Cette fille n'est pas très bonne aux échecs."

show shizu basic_normal
with charachange

shi "…"

show misha sign_smile
with charachange


mi "Les échecs sont un jeu de formules. Donc~ ! Ce n'est pas un jeu qui lui convient... Quelqu'un qui joue aux échecs comme ça, regardant uniquement la prochaine pièce, jouant si superficiellement, n'est pas un joueur sérieux."

show misha perky_smile
with charachange


mi "Quelqu'un qui aime les échecs au point d'avoir les yeux qui brillent comme ça quand il voit un jeu d’échecs, serait le genre de personne qui étudierait le jeu."


mi "Si tu l'étudies, même juste un peu, tu peux apprendre à voir au moins deux coups à l'avance, même contre les pros."

show misha hips_frown
with charachange


mi "Pourquoi quelqu'un qui aime tant ce jeu... avec autant d'enthousiasme... s'y connaît si peu ? Même moins que quelqu'un qui aurait un simple intérêt passager ?"


"Shizune pose la pièce qu'elle a dans la main. C'est une tour."

show shizu behind_frown
with charachange

shi "…"

show misha hips_smile
with charachange


mi "Ses sentiments sont réels, mais pas ceux pour le jeu. Tu comprends, Hicchan~ ?"

show misha perky_smile
with charachange


mi "Il n'y a pas de chance aux échecs~ ! Il est très important de le réaliser. La chance dans les jeux, c'est bien pour que tout le monde ait une chance. Juste suffisamment pour que ce soit intéressant, mais pas pour que les compétences soient pénalisées."


mi "Les échecs, ce n'est pas un jeu pour moi, c'est juste des formules."

show misha sign_smile
with charachange


mi "Hanako n'est pas le genre de personne qui aimerait quelque chose comme ça~."

show shizu adjust_angry
with charachange

shi "…"

show misha cross_frown
with charachange


mi "Si tu aimes quelque chose, tu te bats. Se battre est une preuve de préc— préciosité ? Je crois, du moins. Ou~ ! Tu concèdes immédiatement~ ! Vu que c'est tellement précieux que ça t’empêche de réfléchir."


"L'un est un amour passionné. L'autre est un amour gentil."

show shizu basic_normal2
with charachange

shi "…"

show misha hips_smile
with charachange


mi "J'ai essayé de la combattre, en chassant son roi, l’appâtant. Je n'ai pas réussi cela dit, parce qu'elle se limitait seulement aux mouvements viables."


mi "Le moment le plus difficile a été quand elle a agi plus vite. Ça voulait dire qu'elle savait exactement comment gérer la situation."

show misha sign_smile
with charachange


mi "Ça veut dire que quelqu'un lui a appris. Tu comprends, Hicchan~ ?"


hi "Pas vraiment."

show shizu adjust_happy
with charachange

shi "…"

show misha hips_grin
with charachange


mi "Si tu aimes les échecs à ce point-là, mais que tu ne peux pas te donner à fond, c'est parce que tu aimes les souvenirs attachés à ce jeu mais pas le jeu en lui-même, c'est trop précieux pour elle pour être un outil de compétition."

show shizu behind_blank
with charachange

shi "…"

show misha perky_smile
with charachange


mi "À cause de ça, on peut ne pas devenir amies avec ce jeu. Pas sans mots."

stop music fadeout 5.0


"La façon dont tu te fais des amis ne marche pas avec tout le monde, Shizune."


"Elle n'est pas triste, du moins ça ne se voit pas, mais ses mots le sont vraiment."


hi "Hé, jouons à quelque chose."


hi "Pendant que l'échiquier est toujours posé."

play sound sfx_warningbell


"Mais la cloche sonne et m’interrompt."

scene black
with dissolve

$ suppress_window_after_timeskip = True



label fr_S12:

window hide None

scene bg school_council
with locationchange

nvl clear

nvl show dissolve

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_daily fadein 0.5


n "\nLes choses sont revenues à la normale. Certes, j'ai été transféré à un moment inhabituel de l'année et je ne peux pas tellement dire que mes premières semaines ici ont été normales. J'imagine que c'est plus les choses qui se sont calmées et sont devenues normales."



n "Je suis là depuis plus longtemps que je l'aurais cru."


n "C'est difficile de ne pas penser à tout ce que j'ai loupé avant d'arriver dans cette école, ou à ce qui a dû se passer dans mon ancienne école depuis que je suis parti."


n "Je me demande d’où viennent ces sentiments, vu que je n'ai pas laissé grand-chose derrière."


n "Il y a plus de choses que j'aime ici. Si ce n'était pas le cas, je ne me serais pas embêté avec le Conseil des Étudiants. Cela aurait été compliqué de m’intéresser à quoi que ce soit, si cette école était comme j'avais imaginé qu'elle serait."


n "Donc, même ce sentiment de routine journalière me plaît, d'une certaine façon."


n "J'ai peur de la charge de travail qui m'attendra au Conseil des Étudiants après l'école, suffisamment pour envisager de ne pas y aller, juste cette fois. Mais d'un autre côté, c'est agréable qu'il y ait quelque chose que je puisse faire."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

window show

show shizu basic_normal
with charaenter


"Shizune pose une pile de feuilles de présence à côté de moi."

show shizu adjust_happy
with charachange


ssh "Merci encore de nous aider."

show shizu adjust_happy at tworight
show bg school_council at bgright
with charamove

show misha hips_grin at twoleft
with charaenter


mi "Merci encore, Hicchan~ !"


"Il y a beaucoup de travail. J'ai dû louper le cours de langue des signes encore une fois, mais maintenant je suis à un niveau où je peux comprendre la plupart des conversations entre Shizune et Misha, donc ça ne me gêne pas trop."


"Shizune ne le sait toujours pas, cela dit. Je suis déterminé à continuer comme ça jusqu’à ce que je sois sûr de mes compétences. Peut-être que c'est un peu enfantin de ma part."

show shizu behind_frown
with charachange


ssh "Tanabata est dans moins de cinq jours, mais ils commenceront à construire les stands seulement demain."

show misha sign_smile
with charachange


mi "Hicchan, on aura peut-être besoin d'aide pour construire les stands encore."


hi "Pourquoi ? Quel était l’intérêt de les démonter d'ailleurs ? Ça a pris des jours, n'est-ce pas ?"

show misha hips_grin
with charachange


mi "Yep ! C'est vrai~ ! Même si Hicchan n'était pas là pour ça~."


hi "Je vous aurais aidées si vous me l'aviez demandé."

show shizu basic_normal
with charachange


ssh "Ça n'aurait pas eu de sens de t’embêter avec le nettoyage après que tu aies autant apprécié le festival."

show misha hips_smile
with charachange


mi "Ça n'aurait pas eu de sens de t’embêter en te faisant nettoyer juste après le festival, ça aurait ruiné le côté fun du festival."

show shizu behind_smile
with charachange


ssh "D'ailleurs..."

show misha hips_grin
with charachange


mi "Ahahaha~ ! Hicchan est paresseux de toute façon, tu aurais essayé de t'enfuir encore une fois~ ! Shicchan n'aime pas jouer au chat."


hi "Ça fait mal."

show shizu adjust_smug
with charachange


"Shizune se couvre la bouche avec la main et commence à trembler. Il me faut une seconde pour réaliser qu'elle rit, surtout parce qu'elle le fait complètement silencieusement."


"C'est un peu bizarre à voir, mais assez bon esprit, comme Misha, sans le rire perce-tympan."

show misha sign_smile
show shizu adjust_happy
with charachange


mi "Mh~, cela dit, c'est une bonne question, Hicchan."


hi "Hein ?"

show misha hips_grin
with charachange


mi "Stands~ !"

show shizu basic_normal2
with charachange


ssh "C'est un problème de stockage. L'école n'a nul part où stocker autant de stands. Ils ne paieront pas pour stocker non plus, donc c'est ce qu'ils ont décidé de faire. C'est pas pratique, mais c'est pas cher."

show misha sign_smile
with charachange


mi "Parce que~ ! L'école n'a pas d'endroit où entreposer autant de stands, Hicchan."

show shizu behind_frown
with charachange

shi "…"

show misha perky_confused
with charachange


mi "Ah, ouais ouais~, ouais, c'est vrai que si, mais ils ne veulent pas payer~ ! Désolée, Shicchan~..."

show shizu basic_normal2
with charachange


ssh "C'est à cause de la précédente génération."

show shizu behind_frustrated
with charachange


ssh "Le gérant a décidé que le prix des lieux de stockage extérieurs était devenu trop élevé et le Conseil des Étudiants était trop faible pour oser dire que c'est bête d'avoir à construire et désassembler soixante stands deux fois par an."

show shizu adjust_angry
with charachange


shi "... !"

show misha cross_grin
with charachange


mi "D'accord~ !!"

show shizu behind_smile
with charachange

shi "…"

show misha perky_smile
with charachange


mi "Hicchan, allons manger quelque chose~ ! J'ai l'impression qu'on a travaillé toute la journée~..."


hi "C'est le cas. Maintenant que j'y pense, j'ai faim. J'aurais bien pris un déjeuner, mais pour je ne sais quelle raison il y avait plein de monde, alors j'ai décidé que ça ne valait pas le coup."

show misha cross_laugh
with charachange


mi "Ahahaha~ ! C'est sûrement parce qu'aujourd'hui il y avait des choses spécialement intéressantes en vente."


hi "Comme quoi ? Non, ne me dis pas. Ça importe peu, vu que je n'ai pas pu en manger de toute façon."

show shizu adjust_smug
show misha hips_grin
with charachange


"Shizune semble contente d’elle-même. Je me demande pourquoi."

show shizu behind_smile
with charachange


ssh "Je suis préparée à une situation comme celle-ci."


"Rayonnante de fierté, elle sort un grand assortiment de nourriture de son sac. Je peux immédiatement voir que quatre-vingt-dix pour cent de ce qu'il y a vient de la cafétéria de l'école."

stop music fadeout 5.0


"Il y en a vraiment beaucoup. Il n'y a pas une limite d'achats par personne ?"


"Ça signifie qu'elle les a obtenus de façon malhonnête."


hi "Le sandwich à l’escalope de veau est toujours vendu dans la première minute après l'ouverture. Je suis impressionné que tu aies réussi à en avoir un."


hi "Merci."

show misha perky_smile
show shizu basic_sparkle
with charachange


"Je tends le bras pour le prendre dans le panier, mais Shizune fait immédiatement de même."

play music music_another fadein 0.5

show shizu basic_happy_close
with characlose


"Sa prise se ramollit pendant une seconde quand sa main touche la mienne, mais elle y remet immédiatement deux fois plus de force, une flamme de compétitivité étincelant dangereusement dans ses yeux. Ses doigts essayant de déloger les miens."


"Je ne bouge pas d'un pouce, préparé à risquer ma vie pour ce sandwich. Il est possible que je n'aie jamais une autre chance de le manger."


"Je suis parfaitement conscient que si nous continuons comme ça, nous pourrions écraser le sandwich, ce qui réduirait considérablement sa comestibilité."


hi "Misha... Dis-lui que si elle ne lâche pas, le sandwich va être écrasé."

show misha perky_confused
with charachange


mi "Mmmmmh ? Pourquoi tu ne le fais pas toi-même ?"


"Je suis étonné qu'elle laisse glisser aussi facilement le fait que je puisse communiquer sans problème avec Shizune."


"Je pense presque pendant un instant que c'était volontaire, mais je suis sûr qu'elle était juste distraite en se battant avec l'emballage de la paille de son jus de fruit."


hi "C'est pas évident ? Je peux pas lâcher le sandwich."

show misha sign_smile
with charachange


mi "Je ne peux pas dire ça à Shicchan, cela dit."

show misha hips_grin
with charachange


"Elle tourne les paumes vers le ciel et hausse les épaules, un grand sourire sur le visage."


hi "Pourquoi pas ?"

show misha sign_smile
with charachange


mi "Parce que~ ! Tu as un intérêt dans cela, donc je peux pas te faire confiance~ ! Si Shicchan veut répondre, elle devra lâcher le sandwich, et tu gagneras. Qui sait, qui sait, peut-être que c'est ce que tu veux, Hicchan ?"

show misha cross_smile
with charachange


mi "Je ne serai pas injuste, donc je vais être neutre ! Comme la Suisse~ !"


hi "La Suisse ?"

show misha perky_smile
with charachange


mi "Tu connais pas la Suisse ?"


hi "Bien sûr que si... elle est neutre, ils sont neutres."

show shizu basic_sparkle_close
with charachange


"Shizune me fixe du regard avec un air arrogant, le bout de sa langue sortant légèrement d'entre ses dents, tout en continuant de serrer fort le sandwich à l’escalope de veau qui est entre nous."

show shizu adjust_happy
with charadistant


"Soudainement, elle lâche et met les mains en l'air, signe universel de paix."

show shizu behind_blank
with charadistant


ssh "Ça me semble être une triste façon de régler ça, tu ne crois pas ? Et on pourrait écraser le sandwich."

show shizu behind_frown
with charadistant


"Elle me fixe du regard, et son expression passive se change rapidement en une grimace désapprobatrice."

show shizu adjust_angry
with charadistant


shi "... !"

show misha hips_frown
with charachange


mi "Hicchan ! Lâche le sandwich ! On négocie !"


"Je le lâche à l'instant."

show misha perky_smile
show shizu behind_blank
with charachange


"La main de Misha rampe sur la table et attrape le sandwich."

show misha hips_grin_close
with characlose


mi "Ah~ ! Haha~ ! Ne t’embête pas, je n'aime même pas le veau. Je vais juste prendre ce sandwich-là~ ! Et quelque chose à boire, aussi..."

show misha perky_smile
with charadistant


"Prenant avec précaution ce qu'elle veut, elle se retire juste après."


"Elle a la bonne attitude. Je pourrais prendre quelque chose d'autre, il y a plein de bonnes choses, là. Le katsudon au poulet est aussi très populaire, apprécié pour son goût et très demandé. Mais j'en ai déjà mangé un auparavant."

show shizu basic_angry
with charachange


ssh "Tu es si immature, Hisao. Ça ne serait pas un problème si tu prenais quelque chose d'autre. Le katsudon au poulet est délicieux."

show misha hips_smile
with charadistant


mi "Tu es si immature, Hicchan. Pourquoi tu ne prends pas le katsudon au poulet à la place ? C'est délicieux~ !"


hi "Mais j'en ai déjà mangé un une fois."

show shizu behind_frown
with charachange

shi "…"

show misha hips_frown
with charachange


mi "Hicchan~ ! Pourquoi est-ce que tu es si obsédé par le sandwich à l'escalope de veau, spé—ci—fi—que—ment ?"


hi "C'est difficile à avoir en temps normal. Les choses rares sont meilleures."

show shizu basic_frown
with charachange


ssh "Tu agis comme un enfant."

show misha cross_frown
with charachange


mi "Tu agis comme un enfant, Hicchan."


hi "Pourquoi tu ne prends pas celui au poulet ?"

show shizu adjust_blush
with charachange


ssh "Ce n'est pas important."


"Rougissant, elle sourit bizarrement et continue."

stop music fadeout 6.0

show shizu basic_happy
show misha perky_smile
with charachange


ssh "On ne peut pas discuter avec toi. On dirait qu'il n'y a qu'une façon de régler ça : on va le jouer."

show misha sign_smile
with charachange


mi "Ça importe peu : on va jouer pour le sandwich à la place~ !"


"D'une certaine façon, je m'y attendais. C'est la conclusion logique."


"Shizune étudie beaucoup depuis un moment, presque sans s'arrêter jusqu’à maintenant. Avec nos examens terminés, j'imagine que ce surplus d'énergie doit aller quelque part."


hi "Jouer à quoi ?"

hide misha
with None
show misha perky_smile behind shizu at twoleft
with None

show shizu behind_blank_close
with characlose


ssh "Le plus vieux jeu du monde, qui a fixé le destin de nombre de nations : Pierre, Papier, Ciseaux."

show misha sign_smile
with charachange


mi "On va jouer à Pierre, Papier, Ciseaux."

show misha perky_confused
with charachange


mi "Vraiment ? Ça semble très sérieux, Shicchan..."

play music music_shizune fadein 1.0


"Il n'y a pas d'hésitation sur son expression, elle est certaine de son choix."


hi "D'accord, d'accord."

show shizu adjust_happy_close
with charachange


"Elle met la main derrière son dos, et je l'imite."


hi "Go !"

show shizu basic_angry_close
with charachange


"Nous faisons tous les deux pierre. Égalité. Je pensais avoir le plan parfait. La pierre est imbattable. Shizune fronce les sourcils, contrariée par la tournure inattendue des événements."

show shizu adjust_angry_close
with charachange


ssh "Encore !"

show shizu basic_frown_close
with charachange


"Deux papiers."


hi "Zut."

show shizu adjust_angry_close
with charachange


ssh "Encore !!"

show shizu basic_frown_close
with charachange


"Nous faisons tous les deux pierre encore, mais une troisième main apparaît et représente les ciseaux."

show misha hips_grin
with charachange


mi "Ça a l'air fun, je peux jouer ?"

show misha cross_laugh
with charachange


mi "Hahahaha~ !"

show shizu behind_frown_close
with charachange

ssh "… … …"

show misha perky_smile
with charachange


mi "C'est un duel, Shicchan ?"

show shizu adjust_angry_close
with charachange

shi "…"

show misha sign_confused
with charachange


mi "Eh~, un duel ? Mh~... Tu as raison, tu as raison~ ! Je ne sais vraiment pas..."

show shizu cross_angry_close
with charachange

shi "…"

show misha perky_confused
with charachange


"Plus elle signe vite, plus c'est dur de suivre. En fait, on dirait que même Misha a du mal à suivre."


hi "De quoi elle parle ?"

show shizu adjust_angry_close
with charachange


ssh "Encore une fois !"

show shizu basic_frown_close
with charachange


"Nous faisons encore égalité. Chaque fois, Shizune redemande un match et nous finissons même par sauter cette étape en enchaînant directement avec pierre, papier, ou ciseaux."


"Même en jouant complètement au hasard, nous continuons de faire égalité. C'est une aberration mathématique."

stop music fadeout 8.0

show misha hips_grin
with charachange


"Misha regarde, riant à chaque fois que nous avons une égalité. Après seize rounds, Shizune pousse sa chaise et se lève."

show shizu behind_blank_close
with charachange


shi "... !"

show misha hips_smile
with charachange


mi "Ça suffit, Hicchan~ ! Je vois ce que nous faisions mal, ça sera fini au prochain round, alors prépare-toi, d'accord~ ? D'accord~ !"

show misha sign_smile
with charachange


mi "J'ai étudié ta façon de procéder et~ je vois comment tu joues. J'ai anticipé ton prochain mouvement et je vais le contrer."


"Ça m'étonne, vu que je ne sais pas comment je procède moi-même."

show shizu adjust_happy_close
with charachange


"Shizune sourit, confiante, un air d'audace sans peur inscrit sur le visage. Ses yeux jettent des éclairs de pure compétitivité alors qu'elle met sa main dans le dos, me faisant signe de faire de même."


"Sa position est surprenante, comme un joueur de bowling professionnel."

show shizu basic_happy_close
with charachange


"Deux papiers."

play music music_comedy

show shizu cross_stunned_close
with charachange


"Shizune se ramollit immédiatement et se frotte les tempes avec un air d'exaspération sur le visage, laissant échapper un soupir si long qu'on dirait un pneu qui se dégonfle. Je réalise que j'ai encore plus faim qu'avant."


hi "On peut toujours le partager."

show shizu behind_blank_close
with charachange


"Je sépare le sandwich en deux et lui en offre une moitié. Elle la prend."

show shizu adjust_happy_close
with charachange


ssh "Merci."


"Elle regarde le sandwich dans sa main, l'étudiant."

show shizu basic_normal2_close
with charachange


ssh "Mais il me semble fade comme ça."

show shizu basic_normal2_close
with charachange


"Malgré ce qu'elle ressent, elle le mange."


"Soudainement, je vois Misha observer la scène du coin de l’œil."

show misha hips_grin
with charachange


mi "Hicchan~... C'était très romantique, tu sais."


hi "Oh, ça va hein."

show misha cross_laugh
with charachange


mi "Wahahahahaha~ !"

show misha hips_smile
with charachange

stop music fadeout 5.0


"Elle rit et prend une bouchée de son second sandwich."


"Nous mangeons en silence pendant un moment, Shizune et moi parvenons à éviter un autre concours. Et après, nous retournons au travail."

scene bg school_council_ss
with shorttimeskip

play music music_tranquil fadein 3.0


"Alors que je finis de remplir les feuilles du jour, je pense que c'est peut-être la façon qu'a Shizune de commencer la semaine sur une bonne note."


"Après tout, demain il y aura beaucoup plus de travail, et avec les mains littéralement pleines en construisant les stands, elle ne sera pas en mesure de beaucoup “parler”."


"Ça sera sûrement ennuyeux et fatiguant, comme ça l'était la première fois. J'apprécie son effort, dans ce cas. C'est agréable d'avoir des jours comme celui-ci, d’apprécier le temps avant les jours à venir. Je crois que c'était son idée aussi."


"...Je me rappelle aussi que je dois toujours m'occuper du paquet de Kenji. Ce fichu truc est volumineux, et je n'ai pas réussi à localiser Kenji depuis que j'ai été le chercher."

scene bg school_lobby_ss
with locationchange


"Après la fin de la réunion du Conseil des Étudiants, je vais pour prendre quelque chose à boire, me séparant de Shizune et Misha. C'est un court trajet, mais après quelques secondes je commence à avoir le sentiment que je ne suis pas seul."

scene black
with hands_in


"Une paire de mains me couvre les yeux."


mi "Devine qui c'est~ !"


hi "Shizune ?"


mi "Wahahaha~ ! C'est moi, Hicchan~ !"


hi "Ouais, je sais."

scene bg school_lobby_ss
with hands_out

with Pause(0.3)

show misha hips_frown_close_ss at Slide(0.3, 0.5, 0.5, 0.5, 1.0)
with Dissolve(1.0)


mi "Alors pourquoi est-ce que tu as dit que c'était Shicchan~ ? C'est pas grave d'avoir tort parfois, Hicchan~ ! Tu es trop fier."

show misha sign_smile_close_ss at center
with charachange


mi "Bref~, tu n'as rien de prévu après la réunion du Conseil des Étudiants, hein~ ? Donc tu vas directement au dortoir ?"


hi "Où d'autre pourrais-je aller ?"

show misha hips_grin_close_ss
with charachange


mi "D'accord, c'est super~ ! C'est super, Hicchan~ ! Je voulais te parler aujourd'hui, donc ça tombe à pic !"


"Deux lycéens, seuls après les cours, dans un bâtiment vide. Alors que le soleil se couche sur un ciel romantique couleur d'ambre, la jolie fille dit qu'elle veut parler."


"Quelle situation attirante et mystérieuse. Mon imagination s'emballe. Ça ne va sûrement pas s'approcher même de loin, de tout ce que je peux imaginer, mais c'est drôle de penser comme ça."

play sound sfx_can
show misha perky_confused_close_ss
with Dissolve(0.2)


"Le bruit d'ouverture de ma canette de café casse l'ambiance que je me suis inventée, résonnant plus fort que ce que j'aurais pensé. Je soupire à la fois de déception et de soulagement."


hi "Donc, qu'est-ce qu'il y a ?"

show misha perky_smile_close_ss
with charachange


mi "Mh ? Oh ! En fait~... Je suis un peu en retard dans certaines matières, et si je ne rattrape pas, ça pourrait être gênant~ ! Je ne peux pas continuer de repousser ça."

show misha perky_sad_close_ss
with charachange


mi "Les professeurs disent que je dois commencer à prendre les choses au sérieux, donc je devrais les écouter~ parce que c'est la troisième fois."


mi "Désolée~ ! Je suis désolée, Hicchan."


hi "Pourquoi est-ce que tu t'excuses ?"

show misha sign_sad_close_ss
with charachange


mi "Je ne serai pas en mesure de vous aider avec le Conseil des Étudiants pendant quelques jours~. C'est seulement l'affaire de deux ou trois jours, vraiment ! J'essayerai de revenir aussi vite que possible ! Mais~..."


"Je ne peux pas dire que j'en sois content. Cette semaine avait déjà prévu d'être chargée. Ce n'est pas le bon moment. Pendant une seconde j'envisage de demander si Shizune ne peut pas tirer quelques cordes pour sortir Misha de là."


"Mais Misha semble vraiment désolée. Ça serait salaud de ma part de dire quelque chose comme ça."


"En plus, si elle dit qu'elle ne peut pas continuer de le repousser, je la crois, étant donné à quel point elle peut être sérieuse avec le travail du Conseil des Étudiants."


hi "Ouais, je vois, c'est pas grave. Vous avez réussi juste à deux l'année dernière, non ? Donc je suis sûr qu'on y arrivera aussi. Ne t’inquiète pas pour ça."

show misha hips_grin_close_ss
with charachange


mi "Vraiment ? Merci, Hicchan~ ! Vraiment~ ! Ouais ouais~ ! Je ne savais pas que tu le prendrais aussi bien~ ! J'ai pensé que tu serais inquiet, vu qu'il y a tellement~ de travail, avec Tanabata et tout~ !"


"Rah, elle me connaît drôlement bien."

show misha sign_smile_close_ss
with charachange


mi "...Mais~ ! Hicchan est si calme~ ! Je suis contente~..."


hi "Haha, ouais. Tu as raison, j'y pensais, mais ce n'est pas si grave. Je ne vais pas paniquer pour ça."


hi "Ça risque d'être un peu ennuyeux de faire des aller-retour avec le bloc-notes pour parler à Shizune, cela dit."

show misha hips_frown_close_ss
with charachange


mi "Hicchan, dis à Shicchan que tu peux utiliser la langue des signes ! Je ne comprends pas pourquoi tu ne le fais pas."


hi "Pas encore. Je comprends la plupart des choses, mais je veux être vraiment sûr. Bah, en fait, c'est pas grave. Être dans le secret me tue aussi, et ça serait bien qu'on puisse avoir de vraies conversations."


hi "Ne t’inquiète pas, je lui dirai. Je le veux. En fait, j'essaye de trouver une bonne opportunité pour le faire."

show misha hips_smile_close_ss
with charachange


mi "Ça ne sera pas un problème, Hicchan~ !"


hi "Pourquoi pas ?"

stop music fadeout 3.0

show misha sign_smile_close_ss
with charachange


mi "Eh bien~, parce que j'ai... plus ou moins... dit à Shicchan que tu pouvais la comprendre. Elle était inquiète pour la même chose, que vous ne puissiez pas vous comprendre~ ! Donc~ ! J'étais inquiète, mais ça s'est bien passé après tout~ !"

show misha sign_confused_close_ss
with charachange


mi "Hahaha ?"


"..."

play music music_running


hi "AAAAAAAAAAHHH !!"


hi "Tu sais à quel point j'ai l'air stupide maintenant ? Je suis resté assis là-bas durant la moitié de la journée à agir comme si je ne pouvais pas comprendre la langue des signes, et tu me dis sérieusement qu'elle savait pendant tout ce temps ?"


hi "Elle pensait probablement “ce gars est un con, à prétendre qu'il ne peut pas me comprendre.” Je passe pour un salaud."


hi "Comment as-tu pu me laisser faire ça ?!"

show misha hips_frown_close_ss
with charachange


"Misha fronce les sourcils, semblant ne pas savoir quoi dire en réalisant que je ne prends pas aussi bien cela que ce qu'elle aurait espéré. Elle ne parle pas avant que je me sois calmé."

show misha hips_smile_close_ss
with charachange


mi "...Mais, Hicchan, je crois que c'est une bonne chose~ !"


"Elle dit ça sans bouger un cil, ayant attendu patiemment que je redescende."


"Le ton joyeux de sa voix donne l'impression qu'il y a eu une rupture dans le temps entre le moment où elle a lâché la bombe et maintenant. C'est assez drôle, d'une certaine façon."


hi "Tu es vraiment unique, tu le sais ça ?"

show misha hips_grin_close_ss
with charachange


mi "Oui~ !"

stop music fadeout 4.0


"Les dégâts sont faits. Si Misha croit que tout ira bien avec autant de certitude, alors peut-être que ça vaut le coup de lui donner sa chance."


"Et si les choses tournent mal, je courrai aussi vite que je le peux..."


"Pour essayer de se rattraper au cas où, elle offre de m'acheter une autre boisson au distributeur. C'est pas grand-chose, mais j'imagine que c'est l'intention qui compte, et les siennes sont sincères."


"Et puis ça fait une boisson gratuite, alors j'accepte."

scene black
with dissolve


label fr_S13:

scene bg school_dormhisao
with locationchange


"Je bois d'un coup ma fournée de pilules journalière avec un verre d'eau."


"Après huit bonnes heures de sommeil, je ne sais pas de quoi j'avais si peur la nuit dernière. Alors que je fais passer une pilule particulièrement grosse, je continue de rationaliser mes inquiétudes."

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_dreamy fadein 2.0

window hide

nvl clear

nvl show dissolve


n "\nShizune savait que je prenais des cours de langue des signes hier, et n'en a pas fait toute une histoire."


n "Elle a beau être muette, ça ne veut pas dire qu'elle ne peut pas faire connaître ce qu'elle ressent. Non, en fait, on dirait que ça la rend encore plus directe."


n "Elle ne tourne pas autour du pot, pas plus qu'elle ne se retient, elle met toujours tout à plat pour qu'il n'y ait pas d'erreur."


n "Donc, si elle n'était pas énervée hier, elle ne le sera probablement pas aujourd'hui. Et puis en plus, je n'ai rien fait de mal de toute façon."


n "Mais alors que ma peur s'atténue, la pensée de passer plusieurs jours avec Shizune sans Misha s’imprègne en moi. Je n'y avais pas pensé hier, mais l'idée devient de plus en plus intimidante. Il est vrai que je comprends plutôt bien la langue des signes, mais..."


n "J’hésiterais à dire que je la comprends au-delà d'un niveau basique, et si elle accélérait ses mouvements, ce qu'elle fait plutôt souvent, je ne crois pas que j'y arriverais."


n "Faire des signes, aussi, n'est pas mon point fort. Faire les deux en même temps comme Misha est toujours un rêve lointain."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

scene bg school_scienceroom
show misha hips_grin at twoleft
show shizu behind_smile at tworight
with shorttimeskip

window show


mi "Hicchan~ !"


hi "Quoi ?"

show misha sign_smile
with charachange


mi "N'oublie pas, tu as dit que tu aiderais à construire les stands aujourd'hui~ ! Derrière l'école après la fin des cours, d'accord~ ?"


hi "Je sais, je sais."

show shizu adjust_happy
with charachange

shi "…"

show misha hips_smile
with charachange


mi "La dernière fois que tu nous as aidées, Hicchan, on a vraiment apprécié~ ! Cette fois, c'est encore plus important, alors hors de question de sécher, d'accord ?"


"Je veux demander pourquoi, mais je n'en ai pas l'opportunité. En plus, Misha est en retard en cours, donc ça semble être une mauvaise idée de la distraire. Je peux toujours lui demander au déjeuner, ce que je finis par faire."

scene bg school_cafeteria
show misha sign_smile at twoleft
show shizu behind_blank at tworight
with shorttimeskip


mi "Parce que, Hicchan, un festival qui célèbre une ville est là pour célébrer ta maison et son histoire."

show misha hips_grin
with charachange


mi "Tanabata est différent, c'est pour les souhaits et les amoureux~ ! C'est plus important, tu ne crois pas ? Ouais~, évidemment que ça l'est~."


hi "C'est vraiment pour ça ?"

show shizu basic_frown
with charachange

shi "…"

show misha cross_frown
with charachange


mi "Hicchan, t'es pas fun..."


"Elle gonfle les joues pour montrer son mécontentement avant de sortir l'air comme un ballon qui se dégonfle."

show misha hips_frown
with charachange


mi "Il faut apprécier les choses comme ça, même si c'est juste une excuse pour manger des bons trucs et bien s'habiller~ !"

show misha sign_smile
with charachange


mi "Je serai déçue si tu n'apprécies pas, d'accord ?"

stop music fadeout 5.0


"Avant que je puisse dire quelque chose, elle se tourne pour renifler une croquette."

scene bg school_gardens2
with shorttimeskip


"Après les cours, je retrouve Shizune derrière l'école, où on dirait qu'elle a déjà commencé à tout installer hier."

show shizu adjust_happy at center
with charaenter


"Elle m'accueille avec un petit signe et un marteau dans la main, tend le bras pour me montrer les stands derrière elle, certains déjà à moitié faits, d’autres encore sous la forme d'une pile de planches attachées ensemble par une corde."

hide shizu
with charaexit

show bg school_gardens2_ss as overlay at Alphain(20.0), center
with None

play ambient sfx_stallbuilding fadein 8.0


"Alors que le temps passe, je réalise que les pilules ont leurs limites. Je suis toujours plus fatigué que je devrais l'être normalement. Heureusement, Shizune est de dos, alors je peux me permettre de me reposer sans qu'elle s’inquiète de la raison."


"Quand j'y pense, je me sens un peu mal de profiter du fait qu'elle ne peut pas entendre que je n'utilise plus mon marteau. C'est mal d'en être content."


"Son éthique de travail est admirable. Il est évident que ça l'ennuie, ou même l’énerve, mais elle ne ralentit pas le rythme. Quand elle est fatiguée de frapper avec un bras, elle utilise l'autre."

hi "Shizune—"


"Je me sens bête d'avoir dit son nom."


"Je ne peux pas lui dire ce que je pense. Il y a un marteau dans ma main aussi, et en fin de compte, j'ai l'impression de devoir faire comme elle."


"Je ne peux pas négliger mon travail non plus, surtout vu qu'on n'est que deux. On n'a pas le temps de faire de signes, pas d'opportunité. Même pas pour un compliment pour un travail bien fait."


"Même quelque chose d'aussi banal que ça nécessiterait que je pose mon marteau, aie son attention, et lui fasse les signes."


"Une simple formalité est devenue inutilement complexe, comme un pas qui prendrait deux fois plus de temps que prévu."


"Je la connais depuis suffisamment longtemps pour savoir ça, et continue de l'oublier."


"Le bruit des frappes rythmées des marteaux enfonçant des clous dans le bois remplit l'air."


"C'est agréable après un moment. Pour ignorer la monotonie de la tâche, j'essaye de synchroniser ma frappe avec celle de Shizune, puis l'alterne pour faire un rythme. Bien sûr, elle ne s'en rend pas compte."


"Je me demande, est-ce que l'absence de bruit rend la tâche encore plus ennuyeuse pour elle ?"

stop ambient fadeout 3.0


"Ça doit être bizarre, être incapable d'entendre les résultats de ses actions alors même qu'elle ressent les vibrations à travers les doigts. Ou alors, n'ayant aucune notion du son, ça ne la gêne pas ?"


"Distrait, je ne remarque pas Shizune se faufilant jusqu’à moi jusqu’à ce que je vois sa tête apparaître."

scene bg school_gardens2_ss
show shizu adjust_happy_ss at center
with charaenter

play music music_soothing fadein 5.0


ssh "Tu prends une pause ?"


his "Ouais, on va dire ça."

show shizu behind_smile_ss
with charachange


ssh "D'accord, faisons ça."

show shizu basic_normal_ss
with charachange


ssh "Tu peux comprendre la langue des signes."

show shizu behind_blank_ss
with charachange


ssh "C'est plus pratique pour nous deux. Même si tu me l'as caché."


hi "Hahaha..."

show shizu basic_normal2_ss
with charachange


ssh "Pourquoi ?"


his "Pourquoi quoi ?"

show shizu behind_blank_ss
with charachange


ssh "Pourquoi est-ce que tu as décidé de prendre des cours de langue des signes ?"


"Ses yeux ne dérivent pas des miens même pour une seconde ; si elle a besoin de voir ma réponse, sa vision périphérique est suffisante. Une fois qu'elle a quelque chose en vue, elle ne détourne pas le regard."


"C'est étrange à quel point ses yeux sont perçants, sombres comme un lac la nuit."


his "Parce que je le voulais. Je me disais que ça serait pratique. Et c'est le cas, non ?"

show shizu adjust_happy_ss
with charachange


ssh "Oui."

show shizu basic_normal_ss
with charachange

shi "…"


his "Désolé, je n'ai rien compris de ce que tu as dit."


his "Tu vois ? Ce genre de choses continue d'arriver de temps en temps. J'aimerais que Misha soit là."

show shizu behind_blank_ss
with charachange


ssh "Elle a du travail à faire après tout. Ça pourrait être partiellement ma faute."


ssh "Misha n'a pas besoin de cours supplémentaires. Ses notes ne sont pas excellentes, mais elle comprend que ses décisions affectent les autres. Ça la met devant beaucoup d’autres personnes."

show shizu basic_angry_ss
with charachange


ssh "Surtout certaines blondes."


hi "Ah..."


"Elle n'oublie pas facilement."

show shizu behind_smile_ss
with charachange


ssh "Tes signes sont vraiment bons. Tu apprends étrangement vite."


his "Je prends des cours depuis un moment déjà. C'est facile à suivre après un moment, avec l'immersion, l'osmose, ce genre de choses. C'est pas si mal."


his "Et si je suis vraiment coincé, Misha est là, aussi."

show shizu adjust_smug_ss
with charachange

shi "…"

show shizu behind_smile_ss
with charachange

shi "…"


"J'imagine que j'ai parlé trop tôt. Je n'ai rien compris. Je vais reformuler."


his "Ouais, non, en fait c'est pas si facile. C'est super dur. Comme ramasser du verre brisé."


his "Mais d'une certaine façon, c'est intéressant. Comme une aventure. Euh, non..."

show shizu basic_normal2_ss
with charachange


ssh "Ramasser du verre cassé n'est pas une aventure."


his "Bien sûr que si. C'est un challenge."

show shizu behind_blank_ss
with charachange


ssh "Pas si tu utilises une pelle et une balayette."


"Je me sens frustré et triste."


"Quand je lève la tête, je remarque qu'elle a une canette de soda dans la main."


hi "Où est-ce que tu as eu ça ?"

show shizu adjust_happy_ss
with charachange


"J'oublie de le signer, mais elle comprend quand même, suit mon regard, et en sort une autre de son dos. Elle la jette dans ma direction et je l'attrape à deux mains."

show shizu behind_smile_ss
with charachange


ssh "J'en ai acheté une autre pour toi."

play sound sfx_can


"Elle s’arrête pour passer son ongle en dessous de l'opercule de sa canette et l'ouvre avant de la mettre sur le côté un moment."

show shizu basic_normal_ss
with charachange


ssh "Si tu m'aides autant, alors je dois veiller sur toi aussi. C'est normal."

show shizu behind_blank_ss
with charachange


ssh "Si tu apprends la langue des signes, c'est entièrement différent. Je serai bien évidemment impressionnée. Ce qui différencie les deux actions est l'obligation."

show shizu adjust_happy_ss
with charachange

stop music fadeout 8.0


ssh "Je suis très contente."

show shizu behind_smile_ss
with charachange


"Elle descend la canette entière en une fois, s'étire les bras et se relève d'un bond."

show shizu adjust_smug_ss
with charachange


ssh "Ok ! Retour au travail !"

hide shizu
with charaexit


"Et sur ce, c'est fini. Shizune retourne à son travail avec la même énergie qu'avant, un léger sourire sur son visage étant la seule preuve qu'elle a pris une pause."

show bg school_gardens2_ni as overlay at Alphain(10.0), center
with None


"Alors que je fais de même, je crois que Misha avait raison en disant que ça se passerait bien. Jusqu’à maintenant, tout va dans cette direction."


"Misha passe nous voir alors qu'il commence à faire noir, ayant l'air aussi fatiguée que moi, et Shizune décide d’arrêter pour la journée."


"Alors que nous couvrons notre travail de la journée et nous séparons, je regarde à quel point leur discussion est fluide, et avec quelle facilité elles rient ensemble en partant vers le dortoir."


"Ça me donne encore plus envie d'atteindre le niveau de compétence de Misha. Je me demande si j'atteindrai ce niveau un jour, ou si j'en aurai le temps."

scene black
with dissolve


label fr_S14:

scene black
with None

play sound sfx_impact

scene bg school_dormhisao
with vpunch


"La première chose que je fais ce matin est trébucher encore une fois sur le paquet de Kenji en sortant du lit, me retrouvant la tête sur le sol avant même d'être complètement réveillé."

show kenjibox:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)


"J'ai envie de frapper ce truc avec le premier objet contondant que je peux trouver, comme si je faisais un home run, mais je n'ai pas l’énergie de faire ça si tôt le matin... et ça endommagerait sûrement ce qui est à l'intérieur. Ce serait méchant."

show kenjibox:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide kenjibox
with None

scene bg school_dormhallway
with locationchange


"Je le pousse dans le couloir. Il glisse sur le sol lisse jusqu’à heurter avec un très léger bruit la porte de Kenji. Immédiatement, une douzaine de loquets et verrous se déclenchent en succession comme une symphonie."

play music music_kenji fadein 0.5

show kenji tsun at Slide(0.4, 0.5, 0.5, 0.5, 0.5)
with charaenter


ke "Qui est-ce ?"


"Il dit ça, avançant d'un pas incertain dans le couloir, passant au-dessus de la boîte d'une façon qui aurait été considérée impressionnante si elle n'avait pas été accidentelle."


hi "C'est moi, j'ai ton courrier. Tu es au-dessus."

show kenji happy at center
with charachange


ke "Je sais. Merci, mec."


hi "...Ouais, peu importe."


hi "Donc, qu'est-ce qu'il y a dedans ?"

show kenji tsun
with charachange


"Il fait une grimace, devenant instantanément sur la défensive et agité."


ke "Ce n'est rien."


hi "Allez, dis-moi, je suis curieux."


hi "Et tu sais, je me suis presque brisé la nuque en trébuchant dessus, et avant ça j'ai eu à transporter ce fichu paquet et traverser la rue alors qu'il me bloquait la vue... Je crois que tu me dois au moins la vérité sur ce qu'il y a à l'intérieur en retour."


ke "C'est secret. Je ne peux pas te le dire, parce que ça ne serait plus très secret et tout. C'est rien d'important."


hi "Eh bien, si ce n'est rien d'important, tu peux me le dire."


ke "Si ce n'est rien d'important, pourquoi est-ce que tu veux savoir ?"


hi "En quoi ça gêne ?"


ke "Pourquoi tu veux savoir ?"


hi "Pourquoi je ne peux pas ?"

show kenji neutral
with charachange


ke "Pourquoi tu réponds à mes questions avec des questions ?"


hi "Pourquoi tu ne réponds pas à ma première question ?"


ke "Pourquoi tu ne réponds pas à ma dernière question ?"


"Je réalise que nos voix deviennent de plus en plus fortes à chaque réponse. Plus loin dans le couloir, une porte s'ouvre et quelqu'un passe la tête pour voir ce qui se passe."


"On doit avoir l'air de deux idiots, mais je suis sûr d'être le seul à avoir suffisamment de honte pour le réaliser."


hi "D'accord, tu peux l'emporter dans ta tombe. Je dois me préparer pour aller en cours de toute façon."

show kenji tsun
with charachange


ke "Roh, non. Pourquoi est-ce que tu es si pressé de partir ? Reste un peu. Tu veux du café ? Ça fait un moment. Tu sais, je pensais que tu étais mort vu le temps que tu as mis à m'apporter le colis."


hi "Tu es chanceux que j'aie bien voulu aller le chercher ton colis en premier lieu, gros malin !"

show kenji neutral
with charachange


ke "Woaw, du calme. Tu es vraiment dans la confrontation mec. C'est à cause du Conseil des Étudiants ? J'ai entendu dire que tu traînais avec eux maintenant."


hi "C'est moi qui te l'ai dit."


ke "Vraiment ?"


ke "Ouais, bref, peu importe mec. Le fait est qu'elles sont terribles."

show kenji tsun
with charachange


ke "Tu es le nouveau, donc bien sûr tu ne le sais pas, mais elle est motif à polémique. Avant que tu n'arrives, elle a essayé d'instituer une politique de badge. C'est une longue histoire, donc peut-être que tu devrais t'asseoir."


"Je cherche une chaise du regard, mais n'en trouve pas parce qu'on est dans un fichu couloir. Je lève un doigt et commence à penser que peut-être je devrais lui dire, mais il a déjà commencé à parler."


"Ne voulant pas gâcher le mouvement de bras que je viens de faire, je regarde ma montre à la place."


ke "Cela aurait été un vrai règne de terreur si c'était arrivé."


hi "Attends, tu la juges sur la base de quelque chose qui n'est même pas arrivé ?"

stop music fadeout 8.0


ke "Oui. Bref, son idée était d'avoir des badges de mérite, mais il y aurait eu aussi des badges de démérite."


hi "Qu'est-ce qu'ils font ?"

show kenji neutral
with charachange


ke "Je ne sais pas, c'est jamais arrivé. Ça semblait horrible cela dit, donc quand j'ai entendu ça, je n'ai pas quitté ma chambre pendant quelques semaines."


hi "Donc tu as entendu qu'il allait y avoir un gros changement et tu t'es caché dans ta chambre, essayant d'éviter d'être affecté ?"

show kenji tsun
with charachange


ke "Nan, j'ai décidé de faire quelque chose pour contrer ça. Je me suis rendu au bureau du conseil des étudiants avec une liste de demandes et avec des gens que j'avais pris au passage pour faire croire que j'avais des supporters."


hi "Attends, donc en plus que ce ne soit pas arrivé, tout le monde s'en fichait ?"

show kenji rage
with charachange

play music music_tension


"Kenji ne m'entend pas, il est parti dans son histoire. Complètement dans sa déclamation, il commence à débloquer et balance ses bras en avant, comme s'il voulait faire des signes de gang."


ke "J'ai été jusqu’à son bureau et lui ai dit “Eh toi, femme fasciste ! C'est quoi cette idée de badge ? Pour qui tu te prends ici, dans ta tour d'ivoire, à nous regarder de haut comme si nous étions une bande d'idiots ?”"


ke "“Ton niveau d'élitisme est honteux, tu es probablement une de ces riches qui demandent à leur chauffeur de les conduire vers des taudis pour qu'ils puissent pointer du doigt et rire...”"


ke "“...et ne boire que du café provenant de grains de luxe chiés par le dernier dinosaure vivant et brassé dans un crâne en or massif."


ke "“Et comment peux-tu ? Va ouvrir un livre d'histoire, tu ne sais pas que la bourgeoisie a toujours déclenché des révolutions sanglantes pour des merdes comme ça ? Stupide ! Tu es une idiote !”"


ke "“D'accord, les révolutionnaires finissent généralement par foutre la merde partout au bout d'un moment, mais seul un maniaque pourrait créer une politique comme ça...”"


ke "“...c'est comme si c'était quelque chose qui était créé pour faire souffrir les gens, sauf que c'est réel et que tu veux l'institutionnaliser ! Quand finira la désacralisation de nos droits ? Nous sommes des gens ! Ce n'est pas une justice !”"

show kenji neutral
with charachange


ke "C'est ce que j'ai dit."

show kenji rage
with charachange


ke "Et puis j'ai crié “Ils peuvent bien prendre nos biens, mais ils ne prendront jamais notre liiiiiiiibertéééééé !” pour attiser les masses comme dans ce film sur la vie de William Wallace où ils ont pris ses biens, mais pas sa liberté, et l'ont tué."

stop music fadeout 5.0

show kenji tsun
with charachange


ke "...Mais elle m'a juste ignoré et n'a même pas levé la tête de sa fichue feuille."


ke "Peut-être que je l'ai tellement écrasée avec ma logique qu'elle est tombée dans le déni. Peut-être que c'est juste une pétasse. Dans tous les cas, elle n'a pas répondu, et le futur n'a pas changé."


ke "En plus, sur le chemin du retour je me suis rendu compte que j'avais perdu ma carte d'étudiant. C'est l'histoire de ma vie. Une lutte constante et parfois futile. Comme essayer d'escalader un mur avec des éponges à la place des mains."


hi "Hé, tu as dit que rien n'a changé, mais elle n'a pas fait porter un tas de stupides badges aux gens, donc ça a changé."

play music music_kenji fadein 0.5

show kenji happy
with charachange


ke "Ouais, c'est vrai. D'accord, peut-être qu'ils ne sont pas si horribles alors."


"J'imagine que ça compte pour quelque chose, si je peux faire admettre à Kenji que deux filles ne sont peut-être pas si mal après tout. C'est déjà ça. Surtout si ça me permet de clôturer la conversation, je n'avais pas réalisé le temps qu'il s'est passé."

stop music fadeout 2.0

scene bg school_dormext_full
with locationchange


"J'essaye de faire ma routine matinale aussi vite que possible. Je regarde ma montre encore une fois en sortant du dortoir et vois que je suis déjà en retard."

scene bg school_scienceroom
with shorttimeskip

play music music_daily fadein 1.0


"Heureusement, le reste de la journée se passe plus calmement, et après la fin des classes, je vais à la rencontre de Shizune."

scene bg school_gardens2
with locationskip


"Derrière l'école, je la vois adossée à un stand terminé sur lequel il y a du papier et du ruban adhésif, trace de la dernière fois où il a été utilisé. Faisant tourner un clou sans y penser entre ses doigts, elle ne m'a pas encore remarqué."


"C'est difficile de résister à la tentation de me faufiler jusqu’à elle. Après avoir vu autant de documents animaliers, je suis préparé. Je suis face au vent, les conditions sont favorables. Cela dit, plus j'y pense, plus ça me semble une mauvaise idée."


"Si je me fais surprendre, j'aurais l'air d'un idiot, et si elle ne sait pas que c'est moi, je pourrais finir blessé. Dans les deux cas, ça serait un peu méchant de ma part. Donc il vaut mieux ne rien faire... même si c'est dommage."

show shizu adjust_blush at center
with charaenter


"Je marche face à elle, la surprenant un peu."


his "Qu'est-ce qu'il y a ? Je t’ai surprise pendant que tu ne faisais rien ?"

show shizu behind_blank
with charachange


ssh "Non, je prenais une pause."


his "Tu n'as pas l'air d'être fatiguée. C'est une sacrée pause, présidente."

show shizu behind_frustrated
with charachange


"Les yeux de Shizune s'agitent un moment, je crois l'avoir embarrassée."


"Elle est exaspérée, et quelque peu tendue, mais elle ne peut pas déclarer forfait, c'est impensable pour elle. Ses doigts gigotent d'impatience."

show shizu basic_normal2
with charachange


ssh "Tu es compétitif aujourd'hui. Tu essayes de me provoquer ? Tu veux qu'on fasse une compétition ? On fait une course pour voir qui arrive à faire le plus de stands jusqu'à la tombée de la nuit."


his "Non, non ! Je t’embête juste. Ce n'est pas un vrai Conseil des Étudiants si je ne peux pas embêter un peu la présidente. Tu n'es pas d'accord ?"

show shizu behind_frown
with charachange


ssh "Ça n'est pas dans la charte du conseil des étudiants, donc non."


his "Il n'y a pas de charte !"


"Du moins, je ne crois pas qu'il y en ait. La seule chose sur laquelle on prête serment sont des menus pour des repas à emporter."

show shizu adjust_smug
with charachange


ssh "Bref, c'est bien que tu sois là, même si tu aurais pu arriver plus tôt. Ramasse un marteau et on va continuer là où on s'est arrêtés."

hide shizu
with charaexit

play ambient sfx_stallbuilding fadein 0.5


"Alors que nous travaillons encore une fois sur les stands, je réalise que c'est moins de travail que ce que j'aurais cru. En fait, d’après Shizune, ça pourrait être terminé pour la fin de la journée avec un peu de chance."


"La dernière fois que je les ai aidées, ça nous a pris, Misha, Shizune et moi, presque quatre jours pour tout faire. Ça ne peut pas être juste mon imagination."

stop ambient fadeout 2.0


his "Tu sais, ça ne semble pas être tant de travail que ça."

show shizu behind_blank at center
with charaenter


ssh "Parce que ça ne l'est pas."

play ambient sfx_parkambience fadein 10.0


"Sa réponse me laisse sur ma faim. Sachant cela, Shizune pose son marteau pour développer."

show shizu basic_happy
with charachange


ssh "Ça aurait été impossible de faire ce travail en moins d'une semaine pour deux personnes. La vérité est que je ne démonte que la moitié des stands, et j'entrepose les autres ailleurs. En fait, je les ai plus cachés à la vue de tous."

show shizu adjust_smug
with charachange


"Elle remue un doigt de manière malicieuse."

show shizu adjust_happy
with charachange


ssh "Mais c'est un secret, donc je ne peux pas te révéler le truc."


his "Tu n'es pas une magicienne."

show shizu behind_smile
with charachange


"Clignant d'un œil, elle sort deux sacs plastique de son sac puis les pause sur une planche avant de lever les mains comme pour dire “ta-da !”"

show shizu adjust_happy
with charachange


ssh "J'ai fait à manger pour nous deux."

show shizu behind_smile
with charachange


ssh "Tu peux avoir celui-là. Le sac a remué et ça s'est mélangé."


"Elle me tend une des boîtes. Je l'ouvre. Ça a l'air délicieux, même si c'est un peu simple. Elle me tend une paire de baguettes, comme si elle venait de s'en rappeler, et je mange ce qui semble être du bœuf grillé."


his "C'est très bon."


his "Tu n'aimes pas que la nourriture se mélange ?"

show shizu basic_normal
with charachange


ssh "En effet."


his "Tu es difficile."

show shizu behind_blank
with charachange


ssh "Des fois je mélange moi-même, mais pas toujours, et pas tout. Je n'aime pas quand c'est fait pour moi. Ce qui est important, c'est le choix."

show shizu basic_normal
with charachange


"Elle pointe du doigt pour ajouter à son argumentaire, puis sépare ses baguettes pour manger."


"Alors que je continue de manger, je remarque deux choses. La première est que tout, à part le riz, est frit. Même les légumes."


"Et il y a beaucoup de viande. Est-ce qu'elle mange souvent comme ça ? Je me demande comment elle réussit à rester aussi fine malgré ça."


"La seconde chose que je remarque est que je ne peux pas lui parler pendant que je mange. Parler la bouche pleine est malpoli, mais avec bols et baguettes dans nos mains, la communication entre nous est impossible. Tout comme hier."


"Même si on passe du temps ensemble, même si j'ai pris le temps d'apprendre la langue des signes, j'ai l'impression de moins lui parler qu'avant. Malgré ça, j'ai aussi l'impression de mieux la comprendre qu'avant."

stop music fadeout 4.0

show shizu basic_normal at tworight
show bg school_gardens2 at bgright
with charamove

show lilly cane_smileclosed at twoleft
with charaenter


"J’entends le bruit de quelque chose tapant sur un des stands et lève les yeux pour voir Lilly, se frayant un chemin avec sa canne."


hi "Salut."


"Je m’arrête avant de dire : “je ne t'avais pas vue.”"

show lilly cane_surprised
with charachange


li "Oh, Hisao, est-ce toi ? J'ai senti une odeur de nourriture qui semblait bonne, et me suis demandée qui ça pourrait être."

show shizu behind_frustrated
with charachange


ssh "Qu'est-ce qu'elle dit ?"

play music music_happiness fadein 6.0


"C'est difficile de bouger les mains tout en disant quelque chose de complètement différent à Lilly. Ça doit être pour ça que Misha traduit tout, tout le temps. Un peu bête, mais ça simplifierait beaucoup les choses."

show shizu basic_happy
with charachange


"Shizune semble contente de ma traduction, comme si elle avait entendu une blague."

show shizu adjust_smug
with charachange


ssh "Tout ceci a été cuisiné il y à des heures, mais pour quelqu'un d'aussi lent que toi, qui ne peut pas rendre une feuille sans une semaine de retard, j'imagine que ta perception du temps doit être un peu différente !"


hi "Ce... n'est pas très gentil."

show lilly cane_displeased
with charachange


"Lilly fronce les sourcils à la réponse de quelque chose qu'elle n'a pas entendu."


hi "Ah, désolé. Je prends juste mon déjeuner. La présidente du Conseil des Étudiants a tout cuisiné."

show lilly cane_reminisce
with charachange


li "Est-ce que la présidente est là aussi ?"


hi "Oui, juste là."

show lilly cane_listen
with charachange


li "Je m'excuse, je n'avais pas remarqué. Normalement sa présence se fait ressentir. Je n'étais pas consciente que le Conseil des Étudiants faisait des repas en extérieur, pourquoi n'ai-je pas été invitée ? C'est bien, cela dit, d'avoir autant de temps libre."

show shizu behind_frustrated
with charachange


ssh "Qu'est-ce qu'elle dit ?"

"…"

show shizu basic_angry
with charachange


ssh "Si je devais t'inviter à faire quoi que ce soit, tu arriverais en retard."


"Mais les mots de Shizune ne sont pas perceptibles par Lilly, un fait qui l'énerve immédiatement."

show shizu behind_frown
with charachange


ssh "Traduis pour moi, complètement, s'il te plaît."


"Elle est bien polie. Dommage qu'elle me demande de lâcher les chiens. Cela dit, je ne peux pas me contenter de ne rien faire. Le sentiment d'être incapable de répondre et incompris est vraiment déprimant. Elle ne me pardonnerait jamais."


"Je vais essayer d'adoucir ses mots un peu."


hi "Eh bien, en fait, tout ceci a été cuisiné il y a un moment déjà."

show lilly cane_weaksmile
with charachange


li "Vraiment ? C'est bien."

show shizu cross_angry
with charachange


ssh "Tourne-toi par ici, c'est très irrespectueux de ne pas regarder la personne avec qui tu parles. Ce n'est pas la façon dont une dame devrait se conduire."


hi "La moitié de ce que je dis est ce que dit Shizune. Elle n'aime pas que les gens ne regardent pas dans sa direction quand elle essaye de dire quelque chose. Elle est, euh, à la droite de ma voix."


"Bien que dans ce cas, je peux comprendre pourquoi Lilly ne le faisait pas. C'est une situation très bizarre, et c'est intimidant d'être le seul lien entre elles deux."


"J'avais oublié ce qui était arrivé la dernière fois qu'elles se sont pris le bec comme ça. Il est clair que Shizune s'en rappelle, et Lilly est plutôt hostile aussi, à sa façon."

show lilly cane_displeased
with charachange


li "Je suis désolée, j'avais complètement oublié de telles formalités. Il est vrai que la présidente du Conseil des Étudiants est le type de personne à demander un tel respect et une attention aux règles à tout moment."

show lilly cane_listen
with charachange


li "J'imagine que gouverner les étudiants t'oblige à rester ferme. Cela dit, elle a certainement le temps de s'amuser aussi, donc ça ne doit pas être entièrement vrai."

show shizu adjust_angry
with charachange


ssh "Le Conseil des Étudiants n'est ni une dictature, ni un jeu à somme nulle !"

play sound sfx_snap


"Shizune pointe le doigt vers Lilly comme un pistolet et claque des doigts, ce qui fait sursauter Lilly, visiblement énervée."

show lilly back_listen
show lillyprop back_cane at twoleft
with charachange


li "C'est donc ça ? Alors cela rend encore plus impressionnant le fait que tu en fasses partie depuis si longtemps, jouant comme si c'en était un. J'adore le fait que tu sois aussi tenace. Pour faire tout ça, tu dois être aussi très responsable."

show shizu behind_frown
with charachange


ssh "Pas autant que je voudrais l'être. Tu ne peux pas te plaindre toi, hein ?"

show shizu cross_rage
with charachange


ssh "Tu es très responsable, à demander de repousser une deadline et faire ce qui doit être fait au dernier moment ? C'est la définition même de la responsabilité !"


hi "Shizune est contente d'entendre ça. Mais, apparemment tu es très responsable aussi, de ce qu'elle dit."

show lilly cane_surprised
hide lillyprop
with charachange


li "Elle dit vraiment ça ?"


hi "Plus ou moins..."


"Lilly ne semble pas très contente."


hi "Nous ne faisons pas un barbecue, juste une simple pause déjeuner. On est à l'extérieur pour construire les stands du festival."

show shizu behind_frown
with charachange


ssh "Je ne vois pas comment tu pourrais savoir, vu que tu ne sors jamais. Tu es à court de thé ?"


hi "Tu vas en ville ? Faire les courses ?"

show lilly back_devious
show lillyprop back_cane at twoleft
with charachange


li "Non. Comme je l'ai dit, je passais juste, au cas où tu n’aies pas entendu. Je détesterais interrompre la présidente du Conseil des Étudiants. Tu ne fais rien actuellement, mais vous devez être très occupés."


show lilly cane_listen
hide lillyprop
with charachange


li "Dans tous les cas, Hisao, je suis sûre que la présidente sera capable de trouver ou inventer du travail à faire pour vous deux, s'il le faut."

show shizu cross_rageclosed
with charachange


ssh "Je vais te dévorer !"


hi "Ouais, très occupés."


"“Dévorer” est un mot compliqué. Je suis content de pouvoir le lire. Ce n'est pas le bon moment pour célébrer ça, cela dit. Au lieu de ça, on dirait qu'elles ont fini de se chamailler. Ça, ça se fête."

show lilly cane_listen
with charachange


li "Passe une bonne journée, Hisao. Au revoir, présidente du Conseil des Étudiants."


hi "Merci, toi aussi."

show shizu basic_frown
with charachange


ssh "N'en fais pas trop surtout."

hide lilly
with charaexit

show shizu basic_normal2 at center
show bg school_gardens2 at center
with dissolvecharamove

stop music fadeout 4.0


"Dès que Lilly part, Shizune repart à l'attaque de son déjeuner aussi vite que possible, comme si elle oubliait ce qui venait d'arriver à chaque bouchée."

hide shizu
with charaexit


"Quand elle a fini, elle retourne marteler avec le même esprit. C'est bien de voir qu'elle évacue sa frustration, mais maintenant elle ne semble plus être d'humeur à discuter."

show bg school_gardens2_ss
with shorttimeskip

play music music_tranquil fadein 3.0


"À peu près deux heures plus tard, elle s’arrête, ayant monté des stands non-stop depuis tout ce temps."


"Elle est toujours difficile à approcher, et je me dis qu'une conversation peut vite se tarir. Après qu'il ait fallu si longtemps pour qu'on ait une occasion seuls tous les deux pour parler en face à face, ça fait presque mal."

show shizu basic_normal_ss at center
with charaenter


ssh "Ta traduction était bonne."



his "Vraiment ?"

show shizu adjust_happy_ss
with charachange


ssh "De première classe !"


"Elle ponctue sa remarque avec un pouce levé."

show shizu behind_blank_ss
with charachange


ssh "...Pour ton niveau."

show shizu basic_normal_ss
with charachange


ssh "Il n'y a pas tant de sourds que ça dans l'école, et la classe de langue des signes est sur le point d'être arrêtée depuis un moment déjà. Je suis sûre que tu n'as pas beaucoup de camarades en classe, j'ai raison ?"

show shizu behind_blank_ss
with charachange


ssh "Si tu apprends la langue des signes seulement maintenant, ta vitesse d'apprentissage va être limitée. C'est pour ça que l’intérêt réduit, parce qu'il faut faire des efforts, juste pour communiquer. C'est pareil avec toutes les langues."

show shizu basic_normal2_ss
with charachange


ssh "Dans une telle situation, une conversation en langue des signes est moins ... qu'elle ne l'aurait été normalement."


his "Je n'ai pas compris un mot. Moins quoi ?"

show shizu behind_blank_ss
with charachange

show shizu basic_normal2_ss
with charachange


ssh "Sp—{w=0.2}on—{w=0.2}ta—{w=0.2}née."

show shizu behind_blank_ss
with charachange


ssh "Misha est la seule personne qui y arrive bien."


his "Ouais, ça c'est sûr."

show shizu behind_sad_ss
with charachange

show shizu behind_blank_ss
with charachange


"Son expression change pour une seconde, et revient à la normale trop vite pour que je l’interprète, mais j'ai le sentiment que je ne devrais pas l'interroger là-dessus de toute façon."


"Ce que je veux vraiment savoir est..."


his "Pourquoi vous vous disputez autant Lilly et toi ?"

show shizu basic_frown_ss
with charachange


"Se tendant un peu et fronçant les sourcils, Shizune tend les doigts et les entrelace à répétition comme si elle mélangeait un paquet de cartes invisible."

show shizu behind_frustrated_ss
with charachange


ssh "Tu ne peux pas dire “autant” avec les deux disputes dont tu es au courant. Si tu avait été là l'année dernière, tu pourrais dire ça."


his "J'ai entendu dire que ce fut une année difficile. Et quelque chose à propos d'instituer une politique de badges aussi."

show shizu cross_wut_ss
with charachange


his "Ha ha, surprise ? Eh bien, je voudrais aussi qu'on parle de ça plus tard, mais... tu n'aimes pas beaucoup Lilly, hein ? N'évite pas ma question."

show shizu behind_frustrated_ss
with charachange


ssh "Je n'évite rien."

show shizu basic_angry_ss
with charachange


ssh "Elle faisait partie du Conseil des Étudiants jusqu’à cette année. On ne s'entendait pas très bien. Elle voulait continuer les choses comme l'ancien Conseil des Étudiants. L'ancien Conseil des Étudiants était vraiment inefficace. C'était idiot, et insultant."

show shizu behind_frown_ss
with charachange


ssh "Je voulais faire plus, et on s'est disputées."

show shizu basic_frown_ss
with charachange


ssh "Beaucoup disputées."

show shizu adjust_angry_ss
with charachange


ssh "Elle ne pouvait rien faire dans les temps."

show shizu behind_frustrated_ss
with charachange


ssh "Et puis elle a dit que ce que je voulais faire était inutile, juste du travail supplémentaire. Ça te semble être du travail inutile tout ça ?"


"Shizune fait des gestes pour montrer autour de nous."

show shizu basic_frown_ss
with charachange


ssh "Ce qui est vraiment inutile est un Conseil des Étudiants qui ne fait rien. Faible, paresseux, et ennuyeux. Surtout ennuyeux !"

show shizu adjust_angry_ss
with charachange


ssh "C'est pas interessant de rester dans une pièce en ne faisant rien, c'est juste une perte de temps. Quel intérêt d'être là ? Mon sang se refroidissait à force de ne rien faire, au moins en me disputant avec elle, il repart !"

show shizu behind_blank_ss
with charachange


ssh "Si elle avait pu être aussi motivée avant, elle n'aurait pas eu à devenir ma rivale. Mais si elle montre autant d'énergie que ça, même si c'est pour se disputer, au moins c'est quelque chose ! C'est toujours excitant."


his "Je vois."


his "Et pour cette histoire de badge ?"

show shizu adjust_happy_ss
with charachange

stop music fadeout 4.0


"Elle rit, couvrant sa bouche avec sa main comme pour le cacher. Son rire est la seule chose qu'elle cache généralement."

show shizu behind_smile_ss
with charachange


ssh "C'était juste une blague."

show shizu adjust_happy_ss
with charachange


ssh "S'amuser un peu est important, aussi."

stop ambient fadeout 0.5

scene black
with dissolve



label fr_S15:

scene bg school_dormext_full
with locationchange

play music music_normal fadein 0.5


"Le jour suivant, je me retrouve à devoir chercher un peu au début de la pause déjeuner, après m'être retrouvé devant mon distributeur habituel avec ma canette de café favorite en rupture de stock. Le détour prend plus longtemps que prévu."

scene bg school_gardens
with locationchange


"Les choses ont été tellement trépidantes récemment, qu'il me faut un moment pour comprendre pourquoi l'odeur est différente alors que je parcours les jardins en direction de la cafétéria. L'herbe a été récemment coupée."


"Je m’arrête et regarde un peu après avoir réalisé cela. Le groupe occasionnel d'étudiants discutant ou jouant dans l'herbe et les quelques professeurs parlant entre eux sur le chemin rendent la scène très idyllique."

stop music fadeout 2.0


"Malheureusement, un sentiment de crainte monte en moi depuis un moment. Le sentiment que je ne suis pas seul."

play music music_kenji fadein 0.5

show kenji neutral at center
with charaenter


ke "Hé, Hisao, c'est toi ?"


hi "Ouais c'est moi."


"Je suis content que ce soit lui plutôt que quelqu'un avec un couteau et un masque. Kenji commence à parler comme s'il avait une discussion avec quelqu'un d'autre que moi."

show kenji happy
with charachange


ke "Je le savais. Cette coiffure est inconfondable. Une personne de normal n'aurait pas de coiffure comme ça."


"Inconsciemment, je commence à me toucher la tête. Une fois que je réalise ce que je fais, je me sens insulté, et pourtant trop surpris pour être indigné."


hi "Ouais... Qu'est-ce que tu fais là ?"

show kenji neutral
with charachange


ke "Je jauge la température."

show kenji happy
with charachange


ke "L'hiver arrivera bientôt. Il fera trop froid pour que les femmes sortent et fassent leurs déjeuners à la Sex and the City suivies de leurs patrouilles en formation obstructive dans des zones urbaines peuplées."



ke "Quand ça arrivera, les hommes seront en mesure de marcher librement dans les rues à nouveau, et réclamer ce qui leur revient de droit."

show kenji neutral
with charachange


ke "Et pour me préparer en vue de ce jour, je n'ai fait que manger des pizzas durant la dernière semaine, pour stocker de l'énergie."


hi "D'accord."


hi "C'est ce que font les ours."

show kenji happy
with charachange


ke "Et alors ? On a beaucoup à apprendre des ours."


"Kenji hoche la tête, visiblement d'accord avec lui-même."

show kenji neutral
with charachange


ke "D'accord, écoute ça : J'étais en ville aujourd'hui, j'achetais du lait. Il y avait une nouvelle employée, une pouffe qui avait une casquette de baseball avec deux manches de hockey dessus. Je vais l’appeler fille pouffe hipster casquette hockey baseball."


ke "J'ai remarqué que le lait n'avait pas de prix dessus, donc je lui ai dit d'aller mettre l'étiquette sur le lait, pour les générations futures."


"Il était en ville aujourd'hui ? Il a dû louper les cours du matin. J'ai bien envie de lui reprocher, mais son flux verbal m’empêche de placer un mot."

show kenji tsun
with charachange


ke "Elle m'a dit de ne pas l’embêter parce qu'elle était malade. Malade ? Malade ?! On vit dans une société. Tu ne peux pas négliger les interactions humaines parce que tu es malade. Tu sais quel effort il me faut pour me lever le matin ?"

show kenji rage
with charachange


ke "Je le fais toujours pourtant, et je me suis levé ce matin pour aller acheter du lait, pas pour que mes remarques vitales soient ignorées par une pouffe hipster étudiante idiote qui porte une {b}casquette de hockey baseball{/b} au travail. {b}À l'intérieur{/b}."

show kenji tsun
with charachange


ke "J'essayais juste de maintenir l'intégrité des produits. Un carton de lait sans une étiquette de prix ? Quand je vois quelque chose comme ça, ça entraîne des questions. D'importantes questions. Et c'est son travail d'y répondre, merde."


ke "C'est ça le problème avec les femmes, elles n'ont aucun sens du devoir."

show kenji neutral
with charachange


ke "J'ai souvent la diarrhée, mais tu ne me vois pas m'en plaindre. Je relève la tête et fais ce que j'ai à faire quand même, parce que c'est ça être un homme. Même si tu as la diarrhée, tu continues d'avancer, dans l'espoir d'un meilleur lendemain."


hi "Tu sais, avoir fréquemment la diarrhée c'est pas bon signe."


hi "Peut-être que tu devrais arrêter de boire autant de lait."


ke "Je ne peux pas faire ça, c'est ce qui me permet de maintenir ma super force. Et dans ce monde... la force d'un homme est la seule chose qui ne peut pas être affectée par la gonzessification de la société."

show kenji happy
with charachange


ke "C'est pour ça que je laisse des bocaux d'olives ouverts partout. Des fois juste pour montrer que je le peux."


hi "Tu les mets au frigo après ouverture ?"

show kenji tsun
with charachange


ke "Quoi ? Je sais pas mec, c'est pas important."


hi "Tu dois les mettre au frigo après ouverture. Même en primaire les enfants savent ça."

show kenji neutral
with charachange


ke "Ils ne peuvent pas ouvrir les bocaux pour commencer, donc ça importe peu."


hi "Ah, c'est vrai."

show kenji happy
with charachange


ke "Je suis un génie."


"Il se frotte le menton, fier. Je croyais que seuls les scientifiques faisaient ça, puis j'ai rencontré Mutou et ai été déçu."

show kenji neutral
with charachange


ke "Bref, je ne peux plus retourner à ce magasin, vu qu'il est compromis par les pétasses. Sauf... si je me déguise. Peut-être en mettant une autre paire de lunettes."


hi "Pire déguisement du monde."

show kenji tsun
with charachange


ke "Pffff, ça marche sans faille depuis des années. Je n'ai même pas besoin de lunettes pour voir. Elles sont là pour faire semblant. Et pour protéger mon identité. Je suis comme Superman."


hi "Pire déguisement du monde."

show kenji happy
with charachange


ke "Je te le dis, quand les gens voient ma carte d'identité, ils ne me reconnaissent même pas."


hi "Vraiment ? Laisse-moi voir."

show kenji neutral
with charachange


ke "Je ne peux pas faire ça. Je ne peux pas me balader et montrer ma carte d'identité à tout le monde. Je l'ai fait faire il y a longtemps. À une différente époque. J'avais une coiffure de hippie."

stop music fadeout 2.0


"Alors que j'essaye d'imaginer de quoi il pourrait avoir l'air, Kenji retire ses lunettes."

$ ksgallery_unlock("evul kenji_glasses_closed")
scene evbg kenji_glasses:
    truecenter
    subpixel True zoom 0.82
    acdc_warp 20.0 zoom 0.8
show evmg kenji_glasses_closed at kenji_mg_out
show evfg kenji_glasses:
    truecenter
    subpixel True zoom 1.0
    acdc_warp 20.0 zoom 0.8
with whiteout

play music music_friendship



"Il plisse les yeux dès qu'il a retiré ses lunettes, ce qui lui donne l'air encore plus fatigué. Il a raison, il a l'air très différent. Comme s'il n'avait pas dormi depuis des années. Pas suffisamment différent pour que ce soit un bon déguisement, cela dit."


hi "Tu as besoin de plus de sommeil."

$ ksgallery_unlock("evul kenji_glasses_frown")
show evmg kenji_glasses_frown at kenji_mg_out
with charachange


ke "Nan."


hi "On dirait que tu en as besoin."

$ ksgallery_unlock("evul kenji_glasses_normal")
show evmg kenji_glasses_normal at kenji_mg_out
with charachange


ke "Pas du tout. Ce sont juste les yeux d'un homme qui a vu des choses. Les yeux d'un shaman. De terribles choses, que tu ne peux pas imaginer."



ke "Comme quand j'ai fait un bateau dans une bouteille et que ma mère s'est assise dessus. Il y avait du sang et des lambeaux aux motifs floraux partout. C'est ça l'expérience de la vie."


"Kenji ne semble pas horrifié, même si c'est, je crois, la première chose qu'il me dit sur sa vie qui aurait pu être légitimement traumatisant."


"Il parle aussi à trente degrés à ma gauche, donc j'imagine que sa cécité est réelle. Je bouge ma main devant lui, sans réaction de sa part."


ke "Mec, j’espère que tu as réalisé que je rigolais."


"Je ris, prétendant avoir compris. D'une certaine façon, le regarder dans les yeux est plus difficile que d'habitude."

show evmg kenji_glasses_closed at kenji_mg_out
with charachange


ke "Tu veux savoir un fait ? Les gens avec des petits yeux portent de grandes lunettes."


hi "J'ai lu ça quelque part. C'est parce que ça rend les yeux moins petits."


ke "Vraiment ? Je ne savais pas ça."

stop music
$ renpy.music.set_volume(0.5, 0.0, channel="sound")
play sound sfx_scratch


scene bg school_gardens
show kenji tsun at center
with locationchange

$ renpy.music.set_volume(1.0, 2.0, channel="sound")


"Il remet ses lunettes et je me sens étrangement soulagé pendant un moment, jusqu’à ce que je me rappelle qu'il est toujours là, avec lunettes ou sans."

play music music_kenji fadein 2.0


ke "Bon, bref... Il y a cette artiste qui a voulu peindre mon portrait une fois, je crois. J'ai dû lui parler cinq fois pour qu'elle commence à comprendre."


"Ça devait être Rin, j'imagine."


hi "Elle ressemblait à quoi ?"

show kenji neutral
with charachange


ke "Je ne sais pas. Une femme avec des sandales."


"J’espérais qu'il serait un peu plus précis, du genre “elle a pas de bras”. Il est vrai que Rin porte des sandales, mais je crois qu'il est aussi bien possible qu'il y ait d’autres étudiantes artistes qui se sentent assez à l'aise pour porter des sandales."

show kenji happy
with charachange


ke "Je me disais qu'un jour, après que j'aie brûlé toutes les preuves écrites que j'ai existé, ça serait bien de laisser un portrait derrière, pour que les gens puissent le voir et se rappeler le sauveur de l'humanité. Ils en auront besoin pour faire la statue."

show kenji neutral
with charachange


ke "Puis j'y ai plus réfléchi et ai dû refuser sa proposition. C'était tentant, mais elle le voulait pour un truc de l'école. Ça aurait été diffusé."

show kenji tsun
with charachange


ke "Les gens auraient demandé qui c'était, sauf que je n'aurais pas encore sauvé la société, donc ça aurait été inutile. Et puis si quelqu'un m'avait reconnu, j'aurais eu à m'expliquer."


ke "C'est quelque chose que je ne veux pas expérimenter. Je ne veux pas me retrouver dans une situation bizarre, ça arrive tout le temps. Se différencier est une manière certaine de finir inscrit sur une liste."

show kenji neutral
with charachange


ke "C'est pour ça que je fais des efforts pour me fondre dans la masse dans ma vie de tous les jours. Jusqu’à ce qu'il soit temps d'agir."


hi "Bien sûr."


hi "Quelle liste ?"


ke "Il y a beaucoup de listes."

show kenji happy
with charachange


ke "Qu'est-ce que tu fais ici de toute façon ?"


hi "Rien. Je suis arrivé là par accident."


ke "Ça m'arrive tout le temps. J’espère que tu t'en sortiras. Je crois que je vais retourner dans ma chambre. J'ai besoin de programmer un enregistrement sur la télé."


hi "Tu as une télé ?"


ke "Oui, tu devrais passer un de ces quatre, on pourra voir la partie. En haute définition."

stop music fadeout 4.0

hide kenji
with charaexit


"Avant que je puisse lui demander de quoi il parle, il est parti. Il est parti comme il est venu, sans aucun respect envers les gens. Assez impressionnant."


"Maintenant que Kenji est parti, je regarde de nouveau les jardins de l'école dans leur splendeur d'été. C'est pas la peine, il a gâché l'instant."

scene bg school_cafeteria
with locationchange

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 1.0


"Quand je retourne à la cafétéria, épuisé mais en vie, je pense déjeuner avec Shizune encore une fois, mais la trouve assise à une table avec Misha."


"Si c'était n'importe qui d'autre, je penserais être trop loin pour les entendre. Cela dit, c'est Shizune et Misha."


"Si je le voulais, je pourrais espionner facilement leur conversation. C'est mal d'y penser, mais c'est là. ...Je n'ai pas envie, cela dit."


"Elles doivent avoir beaucoup à se raconter, même si ça ne fait que quelques jours. Je suis enclin à les laisser seules pour qu'elles soient tranquilles."


"Cependant, à l'instant où elles me voient, elles me font un signe."

show misha hips_grin at twoleft
show shizu basic_normal at tworight
with charaenter

stop ambient fadeout 5.0
play music music_shizune fadein 1.0


mi "Salut, Hicchan~ !"


"Entendre sa voix, même après si peu de temps sans la voir, est discordant, et je grimace."


"Ces derniers jours, j'avais oublié qu'on ne pouvait communiquer avec Shizune que dans le silence, et en me concentrant pour bien faire, je n'entendais même plus le son ambiant."


"Bah, je me réhabituerai. Je suis content que Misha soit revenue."

show misha sign_smile
with charachange


mi "J'ai fini de rattraper mon travail~ ! Juste à temps~, je n'aurais pas à louper le festival. Wahaha~."

show shizu adjust_smug
with charachange


ssh "Je t'aurais requise pour les affaires du conseil pour empêcher ça d'arriver."

show misha perky_confused
with charachange


mi "Tu m'aurais requise pour les affaires du conseil pour empêcher ça d'arriver~ ?"


hi "C'est de l'abus de pouvoir."

show shizu behind_frown
with charachange

shi "…"

show misha hips_frown
with charachange


mi "Pas du tout, Hicchan~ !"

show misha sign_smile
with charachange


mi "Shicchan dit que s'il n'y avait eu que deux membres du Conseil des Étudiants pour surveiller le festival, ça aurait été un problème, n'est-ce pas ? Ouais~, forcément. On doit être au moins trois ! C'est pour le bien de tous, c'est nécessaire~ !"

show shizu adjust_happy
show misha perky_smile
with charachange


"Shizune se tient en diagonale de la table alors que Misha traduit ses justifications un peu perturbantes et militaires avec une manière enfantine et joyeuse, sur un ton criard."


"Shizune semble vraiment contente, les doigts tendus et essayant de retenir un rire alors que Misha finit l’interprétation."


hi "Si tu le dis."


"Je suis content qu'on puisse parler si facilement ensemble. Tous les trois."


"Au début je croyais m'être retrouvé dans une mauvaise situation. J'étais sûr que Shizune détesterait devoir faire faire un tour des environs au nouveau."


"Je ne voulais pas être ce genre de fardeau, non plus. Ça aurait été gênant même si elle n'était pas sourde et muette, en plus de ça."


"Juste que maintenant, elle a dit qu'on devra tous être au festival, le Conseil des Étudiants en entier."


"Je ne crois pas que le Conseil des Étudiants ait une vraie juridiction sur Tanabata. C'est juste la façon qu'a Shizune de dire qu'elle veut qu'on passe du temps ensemble."


"C'est bien d'avoir des amis."


"C'est une simple pensée, mais elle me fait vraiment plaisir, l'idée qu'on puisse être ensemble et à l'aise aussi facilement. Malgré la façon détournée dont Shizune l'a dit, je suis content qu'elle le pense suffisamment fort pour l'exprimer."

show shizu basic_normal
with charachange


ssh "Pourquoi est-ce que tu as attendu qu'on te fasse signe pour venir t'asseoir avec nous ?"


"Une question sortie de nulle part. Les yeux de Shizune montrent qu'elle attend une réponse tandis que Misha répète le message. J'ai l'impression de la taquiner."


hi "Tu veux que je m'asseye avec vous à ce point ?"

show shizu behind_blank
with charachange


ssh "Nous sommes le Conseil des Étudiants. Nous devrions nous asseoir ensemble autant que possible. C'est logique."

show shizu adjust_happy
with charachange


ssh "Tout le monde voudrait profiter de la chance de s'asseoir avec deux jolies filles de toute façon."


"Elle s’arrête, au cas où je voudrais dire quelque chose du genre “Mais vous n'êtes pas si jolies !” et me met instantanément dans une position de défaite inévitable. Alors que je ne mords pas à l’appât, Shizune continue."

show shizu basic_happy
with charachange


ssh "Tu es anormal."


"Bon, je ne m'attendais pas à ça."


hi "Tu dis trop vite que les gens sont anormaux. C'est arrogant."

show shizu adjust_smug
with charachange


ssh "Tu dis trop vite que les gens sont arrogants. Ça te rend arrogant, et l'arrogance est aussi anormale. Tu es double-anormal."


hi "Ça ne marche pas comme ça."

show misha hips_grin
with charachange


mi "Hahaha~."


"Se reposant sur son bras, Misha ferme les yeux et rit lentement."


hi "Ne ris pas..."

show shizu behind_blank
with charachange


ssh "Ne ris pas dans ce genre de situation."


"Je remarque que Misha signe tout ce que je dis à Shizune, même si je le signe déjà. C'est un peu redondant, mais elle le fait inconsciemment. D'un autre côté je ne peux pas me permettre d’arrêter."


"Si je me laisse aller et laisse Misha faire les signes pour moi, alors quel était l’intérêt ? Je ne veux pas risquer de perdre ma familiarité avec les signes non plus. Mes mains sont assez lentes comme ça."

show misha sign_smile
with charachange


mi "Hicchan, Shicchan et toi parlez beaucoup plus ensemble qu'avant~ ! Vous vous renvoyez la balle, c'est drôle ! Comme un vieux couple, hein~ hein~ ?"


"Quel commentaire épineux, de tant de façons. Cela dit, vu que c'est Misha, ça ne peut pas être exprès."


hi "Ce n'est pas un compliment."


"Shizune ne réagit pas à la tentative de Misha de nous assimiler en tant que couple. Peut-être qu'elle ne l'a pas vue. Ça arrive des fois. Je me demande toujours pourquoi j'y accorde tant d'importance, mais je ne veux pas trop y penser."


"Je veux partir. Je continue de penser que j’empiète sur le temps de Misha avec Shizune et c'est peut-être pour ça que Misha nous a interrompus. Je doute qu'elles me laissent partir de toute façon. D'un côté, elles sont trop gentilles."


hi "Bref, Shizune, si tu veux vraiment savoir, je ne voulais pas m'asseoir ici parce que je voulais pas m’incruster."


hi "Je pensais que parce que Misha était absente depuis quelques jours, vous auriez envie de parler, et que je devais vous laisser seules. C'est pour ça que je ne suis pas venu d'emblée."


hi "Ne t’inquiète pas Misha, je n'essaye pas de monopoliser Shizune."

show misha cross_laugh
with charachange


mi "Wahaha~ ! Hicchan ! C'est pas ça~."

show shizu basic_normal
with charachange

shi "…"

show misha hips_smile
with charachange


mi "Tu es vraiment attentionné, Hicchan ! Shicchan est désolée~ et s'excuse."


hi "Il n'y a pas vraiment de raison de s'excuser, donc ne t’embête pas. Hé, maintenant que Misha est revenue, et si on fêtait ça ? Ça serait bien."

show misha cross_frown
with charachange


mi "Hicchan~ ! En général, rattraper du travail n'est pas quelque chose qui se fête."

show shizu adjust_happy
with charachange


ssh "Non, c'est une bonne idée."


hi "Le timing est parfait, et Shizune a dit que le Conseil des Étudiants doit s'amuser aussi de temps en temps. Tu as probablement entendu ça aussi, hein Misha ? Ça ne devrait pas être un problème."

show shizu behind_blank
with charachange

shi "…"


hi "En fait, attends une seconde. Tu n'as pas dû rattraper parce que tu as loupé plein de cours ? Alors louper des cours pour fêter ça serait un peu stupide. Peut-être que le timing n'est pas si parfait après tout, mais on peut le faire après les cours."

show misha sign_smile
with charachange


mi "Où est-ce qu'on devrait aller ?"


"Misha répète la question de Shizune à voix haute avant même d'y réfléchir, m'ignorant complètement."


hi "Hé, écoutez-moi, Conseil des Étudiants qui ne pensez à rien !"

show shizu adjust_smug
with charachange

shi "…"

show misha hips_grin
with charachange


mi "Wahaha~ ! Hicchan, toi aussi tu fais partie du conseil !"


hi "Ah, ouais. C'est vrai."

show misha hips_smile
with charachange


mi "Ouais ouais~ ! C'est vrai, Hicchan !"

show shizu behind_smile
with charachange


ssh "Petite tête et à problèmes. Je suis désolée pour la fille qui tombera amoureuse de toi."

show misha sign_smile
with charachange


mi "Donc~ ! Où est-ce que tu crois qu'on devrait aller ?"


"Je ris à mes dépens, voulant montrer que Misha est vraiment enthousiaste maintenant, alors qu'elle est celle qui avait le plus d'appréhension. Pour je ne sais quelle raison, je n'arrive pas à me résoudre à parler. Mais ce n'est pas grave."

stop music fadeout 4.0


"Après une courte discussion sur où aller, le seul endroit sur lequel nous sommes tous d'accord se trouve être le Shanghai."


"Une maison de thé n'est pas un mauvais endroit pour célébrer quelque chose, surtout que je suis sûr qu'ils vendent des gâteaux, et les gâteaux sont la célébration incarnée sous forme de nourriture."

scene bg suburb_shanghaiext
with shorttimeskip


"Je n'ai pas vu Yuuko depuis un moment non plus, et c'est aussi le cas des filles. Pour toutes ces raisons, en plus du fait que c'est proche, je finis par me tenir devant le petit salon de thé avec Shizune et Misha avant même de m'en rendre compte."

play sound sfx_storebell

scene bg suburb_shanghaiint
with locationchange

show yuukoshang neutral_down at center
with charaenter


yu "Bienvenue !"

play music music_dreamy fadein 2.0


"Ça faisait un moment que je n'avais pas entendu la voix de Yuuko, et je suis encore surpris par l'énergie qu'elle met dans sa salutation. Comme si elle était une Misha super nerveuse."

show yuukoshang neutral_down at tworight
show bg suburb_shanghaiint at bgright
with charamove

show misha perky_smile at twoleft
with charaenter


mi "Salut~ ! Mais~ ! Tu n'as pas à faire ça à chaque fois si c'est juste nous."

show yuukoshang worried_up
with charachange


yu "Mais si..."

show misha sign_confused
with charachange


mi "Mais—"

show misha cross_laugh
with charachange


mi "D'accord~ ! D'accord~ ! Si tu le dis, Yuuko ! Hahahahaha~ !"


"Je profite de ce moment pour jeter un coup d’œil à l'intérieur et remarque que c'est aussi vide que d'habitude. C'est l'heure de déjeuner. Et pourtant, toujours aussi désert. Je ne comprends pas. Il doit y avoir une raison."

show yuukoshang worried_up at center
show misha hips_smile at left
show bg suburb_shanghaiint at center
with dissolvecharamove

show shizu behind_blank_close:
    yalign 1.0 xpos 1.0 xanchor 0.8
with charaenter


"Shizune tapote mon bras pour attirer mon attention."

show shizu adjust_happy_close
with charachange


ssh "Qu'est-ce que tu veux prendre ?"

show yuukoshang neurotic_up
with charachange


"Yuuko semble un peu agitée après que Misha ait relayé automatiquement la question."


yu "N-non, c'est moi qui suis censée... demander ça... Il y a quelque chose que je peux te servir ?"


show shizu behind_smile_close:
    ypos 1.1
show misha perky_smile:
    ypos 1.14
with dissolvecharamove



hi "Juste du café pour l'instant. Merci."

show yuukoshang neutral_down
with charachange


"Le dévouement qu'a Yuuko pour son devoir de serveuse est admirable. Tout comme la vitesse avec laquelle elle apporte des parts de gâteau et nos boissons à notre table."

hide yuukoshang
with charachange

show shizu behind_smile_close:
    closeright
    ypos 1.1
show misha perky_smile:
    twoleft
    ypos 1.14
with charamove


"Encore une fois, nous sommes les seuls clients ici. Qui sait ce que ça serait s'il y avait du monde."


"Shizune et Misha attaquent immédiatement leur gâteau avec appétit, probablement parce qu'elles ne peuvent pas parler avec la fourchette à la main."


"L’intérêt de partager un repas avec des amis, c'est d'être en mesure de discuter en même temps. Ça serait logique que ce soit pareil avec elles."


"Je suis seulement à la moitié de ma part quand j’entends leurs fourchettes faire du bruit alors qu'elles les reposent sur leur plat vide."


hi "Ce n'est pas sain de manger aussi vite."

show misha hips_grin
with charachange


mi "Hahaha~ ! Hicchan parle comme un vieux~ !"


"Je fais une grimace et ai l'impression de m'être pris un coup."

show shizu adjust_happy_close
with charachange

shi "…"

show misha sign_smile
with charachange


mi "Tu vas porter un yukata demain, Hicchan ?"


hi "Non, je n'en ai pas. Bon, même si j'en avais un, je ne suis pas le genre de gars qui porte des trucs comme ça."


hi "Et vous ? Vous allez en mettre un ?"

show shizu behind_blank_close
show misha perky_smile
with charachange


ssh "Bien sûr."


hi "Comment ça “bien sûr” ? Tu n'en as pas mis un la dernière fois."

show shizu basic_normal2_close
with charachange


ssh "Une fois n'est pas une généralité ! C'est complètement différent de toute façon. Déjà ce n'était pas Tanabata, et le festival était sur le terrain de l'école ; les étudiants devraient porter leur uniforme à l'école."


"C'est clairement une blague, mais elle ne dit pas ça différemment de d'habitude. Ce n'est pas normal, mais elle n'a jamais eu un sens de l'humour normal, et j'y suis habitué."


"J'imagine que sa façon de dire des choses outrageuses sérieusement est mieux que si elle disait des choses sérieuses outrageusement."


"Ce qui est le plus troublant est que j'ai commencé à associer une voix à ses signes et ça rentre en conflit avec Misha qui dit à voix haute tout ce que Shizune signe. Ça me désoriente."

show shizu behind_smile_close
with charachange


ssh "J'en mettrai un cette fois !"

show misha sign_smile
with charachange


mi "J'en mettrais un cette fois~ ! Tu verras, Hicchan !"

show misha hips_smile
with charachange


mi "Pas juste Shicchan, mais moi aussi~ !"

show misha hips_grin
with charachange


mi "Peut-être que~ je changerai ma coiffure, aussi."


hi "Ne fais pas ça, je n'arrive pas à t'imaginer différemment de comme tu es maintenant."

show shizu adjust_happy_close
with charachange


"Shizune fait un signe du doigt et sourit."

show shizu adjust_smug_close
with charachange


ssh "Tu es vraiment sûr de toi. Et si je changeais de coiffure moi ?"


hi "Peut-être que tu devrais te laisser pousser les cheveux et te faire des anglaises."

show shizu behind_blank_close:
    xpos 1.0 xanchor 0.8
show misha hips_smile:
    left
    ypos 1.14
with dissolvecharamove

show yuukoshang neutral_up at center behind misha
with charaenter


"Elle ne semble pas amusée. Heureusement, je vois Yuuko s'approcher, apparemment pour prendre nos assiettes ou demander si on a envie de quelque chose d'autre."


hi "Yuuko, tu fais quelque chose pour Tanabata ?"

show yuukoshang panic_up
with charachange


yu "Hein ?"


"C'est comme si elle s’entraînait dans sa tête à me demander si je voulais à nouveau du café en arrivant, mais elle n'a aucune idée de quoi faire si je pose une question en premier. Je me sens mal."

show yuukoshang worried_down
with charachange


yu "Oui, je... travaille..."

show misha perky_sad
with charachange


mi "Yuuko~, ils te font travailler pendant les vacances ? Awwww..."

show yuukoshang neutral_down
with charachange


yu "O-on a beaucoup de clientèle durant les vacances, et parfois des touristes. Ça ne me gêne pas. Je dois faire de mon mieux."

show shizu adjust_happy_close
show misha perky_smile
with charachange


ssh "Je comprends bien. Vraiment admirable."


"Shizune hoche la tête par solidarité, ressentant une sorte de lien dans leur détermination partagée de faire au mieux, bien que pour elle c'est de la fierté là où Yuuko a vraiment, vraiment besoin de ce travail et même d'une augmentation."


hi "Beaucoup de clientèle, hein ? Combien de personnes il y a en moyenne pendant les vacances ?"

show yuukoshang neurotic_up
with charachange


yu "Ah, euh..."

show yuukoshang worried_up
with charachange

yu "…"

hide yuukoshang
with charaexit

show shizu behind_smile_close:
    closeright
    ypos 1.1
show misha perky_smile:
    twoleft
    ypos 1.14
with dissolvecharamove


"Yuuko s'en va et commence à nettoyer un pot contenant des touillettes. Ce n'est pas poli. Ce n'est pas ce qu'une serveuse digne de ce nom devrait faire. Néanmoins, j'ai plus ou moins ma réponse. Clairement, il y a assez peu de monde."


"Je me demande encore comment le Shanghai fait pour rester ouvert. Peut-être que ce style de salon de thé était un grand succès avant que j'arrive et qu'il ne l'est plus maintenant, et qu'ils restent ouverts en attendant de le refaire."


"Peut-être que le gérant est riche et a fait un pari fou pour voir qui peut perdre le plus d'argent. Peut-être que je loupe les foules de clients à chaque fois que je viens."


"Ou peut-être que cet endroit est juste une couverture pour des revendeurs d'armes."


hi "Vu qu'il n'y a personne d'autre, pourquoi tu ne viens pas t'asseoir avec nous ?"


"On peut parler d'infaisabilité économique. ...Mais Yuuko ne mord pas à l’hameçon, secoue la tête de droite à gauche."

show misha hips_grin
with charachange


mi "Je n'ai jamais célébré Tanabata auparavant, et je ne me suis jamais habillée spécialement pour quelque chose comme ça~ ! Je pourrai enfin porter mon yukata. Ouais ouais~ !"


hi "Comment ça jamais ? Et l'année dernière ?"

show misha sign_smile
with charachange


mi "Mh~... l'année dernière, Shicchan, la déléguée aveugle de la classe 3-2 et moi tenions un stand pour le festival ! C'était un stand de soba, je crois~ ? Ouais, c'était ça~ ! Yep !"

show shizu adjust_blush_close
with charachange


"La déléguée de la classe 3-2 doit être Lilly. Je suis surpris qu'elles aient pu travailler ensemble sur quoi que ce soit, mais Misha serait sûrement la plus à même de rendre ce genre de choses possible, vu à quel point elle est innocente."

show misha hips_grin
with charachange


mi "Shicchan a cuisiné, Lilly a pris les commandes, et je traduisais pour elles~ !"

show misha hips_smile
with charachange


mi "Shicchan n’arrêtait pas de dire : “C'est inefficace~ ! Misha~ ! Pourquoi est-ce que tu es entre nous deux ? Comme pour dire~ Ça marcherait bien si je faisais à manger et que tu prenais les commandes ! Ce n'est pas logique !”"

show misha sign_smile
with charachange


mi "Mais~ ! Je crois que tout le monde s'est amusé en fin de compte. Hein, Shicchan~ ?"

show shizu behind_frustrated_close
with charachange

shi "… … …"


"Shizune ajuste ses lunettes avec un air renfrogné et Misha éclate de rire."

show misha hips_grin
with charachange


mi "C'était l'idée de l'ancien Conseil des Étudiants~ ! C'est pour ça~ !"


hi "Et donc, comment était l'ancien Conseil des Étudiants ?"


"Shizune décide enfin de revenir dans la conversation, ou du moins n'arrive pas à s'en empêcher."

show shizu basic_angry_close
with charachange


ssh "Terrible."


"C'est clair au moins. Elle finit avec un signe de rupture, comme si le jugement était décisif. J’espère qu'elle va développer un peu."

show shizu adjust_angry_close
with charachange


shi "…"

show misha sign_confused
with charachange


mi "Dans les universités et certaines écoles privées, les conseils des étudiants peuvent brasser des millions de ye ! Wow~ ! Vraiment ? Des millions ? Ah, d'accord~ ! Et ils sont beaucoup plus impliqués dans les activités scolaires aussi, Hicchan."


"D’après le ton de Misha, on dirait que c'est tout aussi nouveau pour elle que pour moi."

show misha hips_frown
with charachange


mi "Le Conseil des Étudiants de cette école était une blague en comparaison~ ! Ne donne pas des positions de pouvoir aux gens s'ils n'ont pas de pouvoir du tout ! Quel intérêt~ ?"

show shizu behind_blank_close
with charachange


ssh "Donc..."

show misha sign_smile
with charachange


mi "...Je voulais qu'on ait plus de travail~ ! Ça a été dur de convaincre l'école et les autres membres du Conseil des Étudiants d'accepter ça. En fait~ beaucoup du travail que tu nous as vu faire est le travail que j'ai récupéré, et c'est ce dont Lilly parlait."

show misha hips_grin
with charachange


mi "Si ce n'était pas pour Shicchan, le Conseil des Étudiants s'occuperait juste des présences journalières~ !"

show misha cross_laugh
with charachange


mi "Hahaha~ ! Tu préférerais ça, Hicchan ?"

show misha sign_smile
with charachange


mi "Bien sûr, Hicchan, aussitôt que la quantité de travail a commencé à augmenter, la plupart des membres du conseil ont arrêté de venir."

show misha hips_laugh
with charachange


mi "Wahahaha~ !"

show shizu basic_normal2_close
show misha hips_smile
with charachange

shi "…"


"Shizune joint les doigts avec précaution. Comme si elle voulait ajouter quelque chose, mais n'arrive pas à s'y résoudre."


"Comme elle a dit, le langage des signes donne un peu plus le temps de penser à ce qu'on “dit”. J'imagine qu'elle a l'impression de ne pas pouvoir en parler."

show shizu behind_blank_close
with charachange


ssh "C'était avant, et là c'est maintenant. Amusons-nous juste demain."


"C'est ce sur quoi elle conclut son histoire."


hi "Ouais."

show shizu adjust_happy_close
with charachange

shi "…"

show misha perky_smile
with charachange

stop music fadeout 5.0


mi "D'accord~ ! Alors, la réunion du Conseil des Étudiants est a—jour—née pour aujourd'hui~ !"

show misha hips_grin
with charachange


mi "Il faut ajourner de bonne humeur, parce qu'aujourd'hui était une bonne journée."

show misha cross_laugh
with charachange


mi "Ahahaha~ !"

scene bg school_road_ss
with shorttimeskip


"Les cours semblent être finis au moment où nous partons du salon de thé, et je peux voir les étudiants venant de l'école lorsque nous montons la route en direction de celle-ci."


"Quelques personnes portant notre uniforme regardent Shizune alors que nous les croisons, et je me demande s'ils la reconnaissent en tant que présidente du Conseil des Étudiants ou si leur regard est juste attiré par la tête de Misha."


"Il est impossible de ne pas entendre les discussions des étudiants, et le sujet le plus récurrent est Tanabata. Je me demande combien d'entre eux vont utiliser les stands que j'ai réassemblés."


"Je me sens quelque peu fier, une émotion que je n'avais jamais ressentie en faisant quelque chose à l'école."


"Peut-être que Shizune se sent comme ça aussi. J'ai presque envie de lui demander, mais ça me semble stupide."

scene bg school_courtyard_ss
with locationskip


"Je continue avec cette pensée en tête alors que nous marchons jusqu'au campus et que nous nous séparons ; Shizune en direction du bureau du conseil, et Misha et moi en direction de nos dortoirs respectifs."


"C'est seulement après qu'elles sont parties que je réalise que je ne leur ai pas demandé où et quand elles voulaient qu'on se rejoigne demain."

$ suppress_window_after_timeskip = True

scene black
with dissolve


label fr_S16:

window hide None

scene black
with dissolve

scene bg school_dormhisao
with openeye

window show


"Même si c'est les vacances, je me lève à la même heure que d'habitude, un jour où tout le monde dormira sûrement encore six heures."

play music music_pearly fadein 3.0


"Je prends mon régiment matinal de pilules pour la première fois en quelques jours. Je dois l'admettre, ça m'était sorti de la tête. En voyant les rangées de flacons en face de moi, je ne sais pas comment j'ai fait."


"Dix-sept médicaments différents. J'ai l'impression d'avoir suffisamment mangé pour ne pas avoir à prendre un petit-déjeuner."


"Je suis déjà debout, donc autant aller me balader."

scene bg school_dormext_full
with locationskip


"Il fait bon dehors, ce qui donne à l’atmosphère un air idyllique dont j'ai souvent rêvé."


"Ça m'a toujours semblé romantique de me balader comme ça dans la nature, respirant l'air frais."


"Maintenant que j'en ai l'opportunité ici, je ne peux pas résister, même si je sais que je dois avoir l'air idiot."

scene bg school_courtyard
with locationchange


"Je m’arrête au bâtiment principal pour prendre une boisson, puis décide d'y entrer et éventuellement d'aller sur le toit."


"La vue devrait être plutôt belle à ce moment-là, et je suis sûr que personne d'autre ne sera là-haut. Je n'y ai jamais été, en plus."

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 1.0

scene bg school_staircase1
with locationchange


"L'école est silencieuse aujourd'hui. Déserte. Mes pas résonnant dans l'escalier vers le toit me semblent vraiment bruyants."


"Ça ne devrait pas m’embêter vu tout le temps que j'ai passé en classe de langue des signes dans un silence presque total, ou travaillant autant avec Shizune récemment, mais pourtant, ça me gêne toujours."


"Mes pas font des bruits que je n'aurais même pas remarqués avant. J'ai l'impression d'aller dans un endroit où je ne devrais pas être. Je me demande pourquoi. Peut-être que l'école est hantée ou quelque chose du genre."

play sound sfx_door_creak
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")
stop music fadeout 3.0

scene bg school_roof at left
with locationchange


"Quand j'ouvre la porte du toit, je vois que je ne suis pas seul. Misha est contre la grille, regardant en contrebas, et semble ne pas m'avoir remarqué."


"Instantanément, je sais ce que j'ai à faire : couvrir ses yeux et dire “Qui c'est ?”. C'est la seule option."


"En m'approchant, je commence à imaginer à quel point ça pourrait mal tourner pour moi si Shizune arrivait soudainement, étant partie une seconde pour aller chercher des sandwiches, et me voyait en train de m'approcher sournoisement de Misha."


"Je prie silencieusement pour qu'une telle coïncidence n'arrive pas."

show bg school_roof at right
with charamove


hi "C'est qui ?"


mi "Hicchan !"


"Elle répond, sans hésiter une seconde, sans dévier ne serait-ce qu'un peu de sa voix normale. C'est pas drôle."

play music music_soothing fadein 1.0

show misha hips_grin_close at Slide(0.6, 0.5, 0.5, 0.5, 0.5)
with charaenter


mi "Salut Hicchan ! Bonjour~ !"

show misha sign_confused_close at center
with charachange


"Elle essaye par réflexe de bouger ses mains pour signer un bonjour et les coince dans le grillage."


hi "Bonjour. Je ne m'attendais pas à te trouver là. Qu'est-ce que tu fais debout si tôt ?"

show misha perky_smile_close
with charachange


mi "Je pourrais te demander la même chose, Hicchan ! Qu'est-ce que tu fais debout si tôt ? Je ne m'attendais pas à te trouver là~ !"


hi "J'ai demandé en premier."

show misha hips_grin_close
with charachange


mi "Mh~... C'est vrai. Wahaha~ !"

show misha sign_smile_close
with charachange


mi "Tu parles comme Shicchan."


hi "Non, c'est faux."


"...Je dis ça, à peine convaincu moi-même. Heureusement, Misha ne semble pas remarquer quel mauvais acteur je suis."


hi "Tu as hâte d'être ce soir ?"

show misha hips_smile_close
with charachange


mi "Bien sûr, Hicchan~ ! Je n'aime pas les fêtes, ou du moins pas autant que Shicchan, mais Tanabata a l'avantage de toujours avoir des bons trucs à manger. Et~ ! Je vais porter un yukata~ !"


"Ce qu'elle dit est bizarre. On dirait qu'elle dit qu'elle n'aime pas les fêtes, mais aime faire tout ce qu'elles impliquent. Je ne sais pas si ça vaut le coup d'en parler, j'ai peut-être mal compris."

show misha perky_smile_close
with charachange


mi "Et toi, Hicchan~ ?"


hi "Pareil, sinon je serais resté dans ma chambre, hein ? C'est logique."

show misha hips_grin_close
with charachange


mi "Ahaha~ ! Hicchan, tu n'es pas si logique~ ! Donc~ ! C'est vraiment surprenant ! Mh, d'accord. Je m'assurais juste, parce que tu n'avais pas l'air de tant t'amuser la dernière fois. Shicchan et moi étions un peu inquiètes."


hi "Si, je me suis amusé, même plus que ce à quoi je m'attendais."

show misha perky_smile_close
with charachange


mi "Vraiment, Hicchan~ ? Wahahaha~ ! Quelle partie ? Dis-moi~ !"


hi "Euh, il y avait les feux d'artifice à la fin. Ils étaient... vraiment bien."


hi "Je crois que tu t'es endormie avant."

show misha hips_smile_close
with charachange


mi "Aw~... Je m'endors toujours tôt. Mais~ ! Je ne m'endormirai pas cette année ! Je resterai éveillée !"


hi "Je ne crois pas qu'il y ait de feux d'artifice durant Tanabata. C'est pas du tout la même ambiance."



hi "Peut-être que tu peux faire en sorte que Shizune fasse une pétition pour qu'il y en ait. Et qu'ils soient plus tôt."

show misha cross_laugh_close
with charachange


mi "Hahahahahaha~ ! Peut-être que je ferai ça~ ! C'est une super idée, Hicchan !"


hi "Ah, non, non pas du tout ! Ne fais pas ça. Je n'étais pas sérieux."


hi "Et puis... peut-être que ça embêterait Shicc— Shizune."

show misha hips_grin_close
with charachange


mi "Wahaha~. On dirait que tu aimerais bien ça, Hicchan."

show misha cross_smile_close
with charachange


mi "Hicchan~ ! Est-ce que tu aimes Shicchan ?"


"Je ne peux pas dire oui ou non, et assis comme je suis, je ne peux même pas partir."


hi "Ne sois pas bête. Celle que j'aime, c'est toi."

show misha perky_smile_close
with charachange


mi "Ahahaha~ ! Vraiment, Hicchan ? Mh~ ! Non, tu plaisantes, hein ? Tu dois aimer Shicchan plus."


hi "Misha, tu fais trop vite des conclusions."

show misha sign_smile_close
with charachange


mi "Mais tu l'as presque appelée Shicchan ! Donc~ ! J'ai raison, hein~ ?"


hi "C'est parce que tu l'appelles Shicchan tout le temps. C'est sorti comme ça. C'est des choses qui arrivent. En plus, je m'en suis rendu compte avant de finir. Et selon ta logique, tu dois l'aimer plus que moi. Et... tu te moquerais pas de moi par hasard ?"

show misha cross_laugh_close
with charachange


mi "Wahaha~ !"

show misha perky_smile_close
with charachange


mi "Peut-être~."

show misha hips_smile_close
with charachange


mi "J'ai faim. Tu as pris un petit déjeuner, Hicchan ?"


hi "Non. Juste mes médicaments."

show misha sign_confused_close
with charachange


mi "Mh..."


"Misha joue avec ses cheveux pour faire quelque chose de ses mains pendant qu'elle réfléchit."

show misha hips_grin_close
with charachange


mi "On devrait aller manger quelque chose, alors~ ! Tu crois qu'ils serviront un petit déjeuner aujourd'hui ?"


"C'est vraiment le genre de choses qu'un membre du Conseil des Étudiants devrait savoir. Je ne peux pas lui dire, cela dit. Je suis dans le Conseil des Étudiants et je ne sais pas."


hi "Je n'ai vu personne travailler en cuisine quand je suis arrivé, mais je ne sais pas vraiment."

show misha perky_smile_close
with charachange


mi "Hé, Hicchan, tu as déjà entendu parler de ces distributeurs où on peut acheter à manger, comme des hamburgers, de la soupe, ou même de la pizza ? Ça ne serait pas super si on en avait un à l'école~ ?"


hi "Je ne sais pas, j'ai toujours pensé que ces machines étaient bizarres."

show misha hips_smile_close
with charachange


mi "Imagine à quel point ça serait cool d'avoir une machine comme ça ici, Hicchan~ ! Ça serait presque magique, hein ?"


mi "Un plat chaud sortant d'un distributeur, c'est si génial, j'aurais jamais pu imaginer ça. Voir une de ces machines serait comme un rêve !"

show misha perky_sad_close
with charachange


mi "Mh~... On n'a pas de machines comme ça en ville, cela dit~. Et il est trop tôt pour aller en ville en plus~ ! Je ne pourrai pas prendre de petit déjeuner, Hicchan, c'est le repas le plus important de la journée. Tout le monde le dit~ ! Ah, je veux manger !"


hi "Tu es un peu bête. Si ça t’embête autant que ça, je t’achèterai un soda."

show misha hips_frown_close
with charachange


"Misha gonfle les joues et affiche une expression sérieuse."


mi "Hicchan, un soda n'est pas un petit déjeuner. C'est comme de l'eau."


hi "Ce n'est pas comme de l'eau, c'est un liquide. De l'eau n'est pas de la nourriture. Un liquide peut être de la nourriture."


"“Maintenant qui parle comme Shizune, Misha ?” J'ai envie de lui dire. Même son ton me rappelle la façon qu'a Shizune de dire avec confiance des choses ridicules. Mais si j'avais dit ça, j'aurais été celui qui parle comme Shizune encore une fois."


"C'est terrible, sa compétitivité déteint vraiment sur moi."


hi "Allons chercher quelque chose à manger, alors."

show misha cross_frown_close
with charachange

mi "…"

show misha cross_laugh_close
with charachange


mi "D'accord. Ahahahaha~ !"

stop music fadeout 3.0
stop ambient fadeout 1.0

scene bg school_lobby
with locationskip


"Comme on aurait pu s'y attendre, notre quête pour trouver à manger dans une école vide, si tôt le matin, mène à un échec."


"Misha décide de partir de son côté pour trouver à manger, même si on est déjà en fin de matinée."

scene bg school_dormhisao
with locationskip


"Je retourne au dortoir. Les heures qui suivent s'écoulent lentement, et je passe le temps à lire."

show bg school_dormhisao_ni as overlay at Alphain(6.0), center
with None

play music music_dreamy fadein 6.0


"Je n'avais pas touché certains de ces livres depuis que j’étais à l’hôpital. En y repensant, c'était il n'y a pas si longtemps, même si j'en ai l'impression."


"Une journée de libre, et je ne trouve rien à faire. Je fais une courte sieste et alors que je me change pour une seconde fois aujourd'hui, je réalise que je n'ai jamais confirmé avec Shizune et Misha où et quand nous devrions nous rejoindre."


"J'imagine qu'elles finiront par venir me chercher, mais j'aurais l'air plutôt bête si on devait en arriver là."

scene bg school_dormhisao_ni
with None


"Il est déjà le soir, alors je devrais au moins faire un effort pour les trouver en premier."

scene bg school_courtyard_ni
with locationskip


"Même si le terrain n'est pas si rempli de monde que ça et qu'il serait impossible de louper les cheveux roses de Misha même s'il y avait foule, j'ai beaucoup de mal à les trouver."

scene bg school_gate_ni
with locationchange


"Finalement, je les croise au portail principal, qui était le premier endroit où je les ai cherchées."

show shizuyu basic_happy_ni at center
with charaenter


ssh "Bonjour !"


"Elle ponctue sa salutation habituelle avec un grand geste."

show shizuyu basic_happy_ni at tworight
show bg school_gate_ni at bgright
with charamove

show misha sign_smile_yuk_ni at twoleft
with charaenter


mi "Hicchan~ ! Comment vas-tu ?"


"C'est bizarre de les voir en yukata, même si j'ai vu des yukata toute la soirée."


"Celui de Shizune est simple et élégant, ce qui est normal pour elle en y pensant."


"Ce qui attire mon regard est l'épingle à cheveux qu'elle a, une fleur qui rayonne un peu à la lumière de la lune."


"C'est beau sur elle, mais d'une certaine façon aussi quelque peu bizarre. Comme si c'était trop élaboré pour une lycéenne, ou peut-être pour quelqu'un d'aussi secrètement enfantin que Shizune."


"Le yukata de Misha est ce à quoi je m'attendais, donc ça lui va un peu trop bien. Avec ses cheveux couleur chewing gum, elle est mignonne, mais un peu anachronique."


hi "Ça vous va bien."

show misha perky_smile_yuk_ni
with charachange


mi "Merci, Hicchan~ !"

show shizuyu cross_angry_ni
with charachange

shi "…"


mi "Hicchan, tu es un peu en retard. On t'attendait ici depuis un moment, tu avais oublié l'heure ou l'emplacement ?"


mi "Pas grave~ ! Allons-y, Hicchan~ !"

show shizuyu cross_happy_ni
with charachange

shi "…"


"Le fait que Misha abandonne la conversation m'évite une situation potentiellement embarrassante, leur dire que je les cherche depuis au moins une heure."


"Voyant Shizune et Misha si joyeuses, c'est difficile de ne pas succomber à l’atmosphère et de ne pas apprécier la soirée."


"Ce qui m’embête est que j'ai du mal à comprendre ce que signe Shizune ce soir. Je n'ai pas été en cours de langue des signes depuis presque une semaine. J'imagine que comme je n'ai pas pratiqué depuis un moment, j'en perds l'habitude."


hi "Attends, où vous allez ? En ville ?"

show shizuyu basic_happy_ni
with charachange


ssh "Oui."


hi "C'est pas logique. On n'a même pas regardé ce qu'il y avait à l'école. Sauf si vous vous êtes amusées sans moi."

show shizuyu cross_happy_ni
with charachange


ssh "On reviendra, on fait juste le parcours dans l'autre sens."

show misha sign_smile_yuk_ni
with charachange


mi "Hahaha~ ! Dans tous les cas, Hicchan, on devra revenir après avoir été en ville si on veut tout voir. Donc~ ! De cette manière, après avoir fini, on ira directement nous coucher quand on sera fatigués. Comme ça c'est parfait~ !"

show shizuyu basic_happy_close_ni at closeright
with characlose

stop music fadeout 2.0


"C'est effectivement logique. Shizune ne me donne pas l'occasion de lui répondre de toute façon, m'attrapant par le bras et m’entraînant avec elle."

scene ev shizutanabata:
    truecenter zoom 8.0 rotate 45.0 subpixel True
    easein 1.0 zoom 1.1 rotate 0.0
    easein 8.0 zoom 1.0
with locationskip

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_crowd_outdoors fadein 2.0
play music music_ease


"Les rues illuminées par la lumière de la lune et les lanternes en papier sont belles à voir."


"Maintenant que nous sommes en ville, Shizune avance un peu plus lentement pour voir autour d'elle."


"Je décide de marcher un peu plus vivement pour l’embêter, mais elle réajuste rapidement son rythme pour coller au mien, laissant échapper un rire silencieux avant de signer à Misha avec sa main libre."

shi "…"


mi "Qu'est-ce que tu veux faire en premier, Hicchan~ ?"


hi "Pourquoi pas des jeux, s'il y en a ?"


mi "Je croyais que tu n'aimais pas les jeux, Hicchan."


hi "Ça me va."


"Pour la seconde fois aujourd'hui, je sens ses doigts fins s'enrouler autour des miens. J'ai l'impression que ça a toujours été comme ça, que j'ai toujours été entraîné par la volonté de Shizune. Généralement, je ne déteste pas ça."


"C'est juste que certaines personnes ont le talent d'attirer les gens dans leurs vies, comme une tornade. Ce mot correspond à Shizune des fois. Même si je n'ai pas voulu le dire à Misha ce matin, je l'aime bien."


mi "Hicchan, tu vas gagner une poupée pour moi aussi cette fois, hein~ ?"


hi "Tu penses toujours à ça ? D'accord, je t'en gagnerai une."

$ renpy.music.set_volume(1.0, 2.0, channel="ambient")

scene bg suburb_tanabata_ni at bgright
show nightwash
with shorttimeskip


"Le temps passe plus vite que je ne l'aurais cru alors que nous courons dans tous les sens, essayant de faire le plus de choses possible."

show misha perky_smile_yuk at center behind nightwash
with charaenter


mi "De la glace pilée ! Hicchan, tu en veux une~ ?"


"Misha court en direction du stand sans même attendre ma réponse."

show misha perky_smile_yuk at twoleft
show bg suburb_tanabata_ni at center
with charamove

show shizuyu cross_happy_close at closeright behind nightwash
with charachange


ssh "Elles ont l'air bonnes, j'en veux une aussi. On jouera à pierre papier ciseaux pour voir qui paiera pour tout le monde."


hi "Ou... on pourrait aussi payer chacun notre part."

show misha sign_smile_yuk
with charachange


mi "Hicchan~ tu prends quelle saveur ?"


hi "Celle qui est bleue."

show shizuyu basic_angry_close
with charachange


ssh "Bleue n'est pas une saveur."


hi "Je sais..."


ssh "Commander quelque chose en fonction de la couleur est enfantin."


hi "C'est toi qui es enfantine. Qu'est-ce que tu vas prendre ? Fraise ? Ha ! C'est tellement enfantin, seuls les enfants mangent de la fraise."

show shizuyu cross_angry_close
with charachange


ssh "Tu devrais prendre nature, c'est tellement adulte comme saveur !"


"Je veux savoir d’où vient sa personnalité. Je me demande si je penserais comme ça si elle n'avait pas été la première ici avec qui j'ai eu une conversation."


"Il est possible que j'aurais loupé la partie d'elle qui m’attire tant."


"Si je n'avais pas su qu'elle ne pouvait pas m'entendre, qu'elle était si compétitive, si envieuse de me faire entrer dans le Conseil des Étudiants, et si joyeuse et sévère à la fois..."


"Sans ces nouvelles facettes, est-ce que j'aurais fini par autant l'apprécier ?"


"Je réfléchis sûrement trop."


hi "Tu ne vas pas faire un vœu ?"

show misha perky_confused_yuk
with charachange


mi "Shicchan ne fait jamais de vœux, Hicchan !"


hi "Oh vraiment ? Même pas pour le nouvel an ? Pourquoi ça ?"

show shizuyu basic_happy_close
with charachange

shi "…"


"Shizune tend un doigt et sourit, mais ne répond pas."


ssh "C'est un secret."

show misha sign_smile_yuk
with charachange


mi "Moi je sais~ !"


mi "Hicchan, tu veux que je te le dise ?"

show shizuyu cross_blush_close
with charachange


shi "... !"


hi "Oui."

show shizuyu basic_angry_close
with charachange


"Shizune réitère plusieurs fois fortement le mot “non”."

show misha perky_smile_yuk
with charachange


mi "Wahaha~ ! Je te le dirai plus tard, d'accord ?"

show misha perky_sad_yuk
with charachange

stop music fadeout 5.0


mi "En fait, je me sens fatiguée. Je crois que j'irai tôt au lit~."

show shizuyu cross_blush_close
with charachange


ssh "Vraiment ?"


hi "Ça ne fait pas si longtemps."


"Le temps passe plus vite quand on s'amuse."

show misha sign_smile_yuk
with charachange


mi "Et bien~ ! Pourtant si, Hicchan. Peut-être que je rendrai visite à Yuuko d'abord, puis je reviendrai ? Ou~... Je ne sais pas~."

show misha perky_smile_yuk
with charachange


mi "Bah, c'est pas important. Amusez-vous sans moi, d'accord~ ?"


hi "On retournera bientôt à l'école de toute façon, Misha."

hide misha
with charaexit

show shizuyu cross_blush_close at center
show bg suburb_tanabata_ni at bgleft
with charamove


"Misha ne m'écoute pas et part quand même. Shizune se demande pourquoi tout comme moi, et le signe, semblant vouloir en discuter."

scene bg suburb_tanabata_ni at bgleft
show nightwash
with shorttimeskip


"Après que nous ayons vu tout ce qu'il y a à voir, je vérifie l'heure, et me rends compte qu'il est assez tard. Je commence à fatiguer, c'est un miracle que j'aie réussi à en faire autant d'ailleurs."


"Même Shizune commence à avoir l'air un peu fatiguée. Nous repartons en direction de l'école."

stop ambient fadeout 0.5

scene bg school_courtyard_ni
with locationskip

play ambient sfx_cicadas fadein 0.5


"Shizune semble déçue en voyant l'école et la foule d'étudiants à l'intérieur."


his "Un problème ?"

show shizuyu basic_aside_ni at center
with charaenter


ssh "Je voulais aller sur le toit, mais maintenant il y a trop de monde. Je suis fatiguée, donc c'est pas grave."


his "Il y a probablement des couples sur le toit, c'est le genre de fête qui va bien avec ça après tout."


his "Mais encore une fois, je ne sais pas. C'est vraiment ça ou juste un cliché ? Je n'ai jamais vraiment fait de festival avant de venir ici."

shi "…"


his "Je suis déçu, tu avais dit vouloir voir ce que faisait l'école en dernier, garder le meilleur pour la fin. Maintenant tu me dis que tu n'as pas envie ? Même pas un peu ? Je croyais que tu aurais plus d'énergie que ça. Je ne suis pas fatigué moi."

show shizuyu basic_happy_ni
with charachange


"Ça semble déclencher son esprit compétitif, et Shizune se remet d'aplomb immédiatement, même si je viens de réaliser que je n'ai aucune idée de où aller, et je n'ai pas envie d'aller dans le bâtiment principal non plus."

scene bg school_gardens_ni at Fullpan(4.0, dir="right")
with locationchange


"Heureusement, la zone derrière l'école est déserte et aussi assez belle aujourd'hui. Je n'ai jamais remarqué à quel point elle était belle et bien entretenue avant de la voir la nuit. Elle semble presque s'étendre à l'infini dans la lumière de la lune."

show shizuyu basic_happy_ni at center
show bg school_gardens_ni at right
with charaenter


ssh "C'est très beau, même si ce n'est qu'une piste."


"J'ai pensé plus tôt qu'elle était trop immature pour porter une tenue comme ça, mais là, elle est vraiment belle."


"Ça me rappelle quand j'ai fait l'autre festival avec elle, elle était pareil."

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")
$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_serene fadein 1.0

window hide

nvl clear

nvl show dissolve


n "\nJe veux lui dire que je l'apprécie. Mais même y penser est bizarre."


n "Et plus je l'apprécie, plus je suis gêné et effrayé, et j'ai peur de lui dire ce que je ressens. Même maintenant, alors que je pourrais lui dire sans devoir utiliser quelqu'un comme relai."


n "Sans mentionner que si quelque chose comme la dernière fois arrive encore, je ne m'en sortirai peut-être pas aussi simplement qu'avec quelques mois à l’hôpital. Je ne veux même pas y penser."


n "J'essaye d’éloigner ces pensées. J'essaye de les classer en tant que peurs irrationnelles."


n "Mais quand bien même..."


n "La première fois que j'ai vu toutes mes pilules, je les imaginais tomber indéfiniment sur moi, suffisamment pour m'étouffer."


n "J'y pense toujours de temps en temps. Je ne peux pas dire que ce n'est pas une inquiétude légitime. Mais j'apprécie les moments comme ça qui me permettent d'oublier."

nvl clear
nvl hide dissolve

$ renpy.music.set_volume(1.0, 1.0, channel="music")
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene ev shizuconfess_normal
with flash

window show


ssh "Ce que je préfère dans cette école, c'est qu'elle est en haut d'une montagne."


his "Parce qu'elle est plus proche du ciel ?"


ssh "Oui."


his "J'aime aussi, surtout pour l'air frais."


his "Tu es tellement compétitive. Trop compétitive. Si une baleine te mordait, tu la mordrais aussi."

scene ev shizuconfess_smile
with charachange

shi "…"


"Ça la fait rire, et elle me fait un clin d’œil."


ssh "Ça serait si mal ?"


"Son sourire est contagieux."


his "Oui."

shi "…"

scene ev shizuconfess_closed
with charachange


ssh "C'est vrai. Je suis méchante. Un peu."

scene ev shizuconfess_smile
with locationchange


ssh "Mais si je peux rendre les gens heureux, je ne suis pas si méchante, hein ? Alors ça va. J'ai beaucoup d'exemples pour ma défense."


"Peut-être que même ce moment est un jeu pour elle."


his "C'est vrai."

stop music fadeout 2.0


"C'est un moment romantique. Je ne sais pas si une telle chance se reproduira, et je me sens contraint de dire quelque chose de bizarre et stupide. Si je pense trop, je doute que mes mains veuillent m'obéir."


his "Tu veux devenir ma petite amie ?"

scene bg school_gardens_ni at right
show shizuyu cross_blush_ni
with locationchange

shi "…"


"J'espère que je l'ai bien signé."


"Je me sens nerveux, comme si je voulais m'enfuir en courant, et pourtant je suis figé. Je ne pouvais pas entendre ce qui se passait autour de moi, et maintenant j’entends chaque bruit d'ambiance. Je suis vraiment nerveux, ça se voit sûrement."


"Avant, les heures passaient comme des secondes. Maintenant, les secondes passent comme des siècles."

show shizuyu basic_blush_ni
with charachange


"Les mains de Shizune sont devant elle ; elle est presque immobile, comme quelqu'un cherchant ses mots."


"Comme elle a dit, la langue des signes te donne l'opportunité de réfléchir à tes paroles, et elle est en train de faire exactement ça."


"Une situation à laquelle elle ne sait pas réagir. C'est rare. Aussi stoïque que Shizune essaye d'être, elle ne peut pas cacher ses joues rouges, et elle est très mignonne et féminine comme ça. Ça me rassure de savoir qu'elle est aussi nerveuse que moi."

show shizuyu cross_happy_ni
with charachange


ssh "D'accord."

play music music_romance fadein 1.0

show shizuyu basic_happy_close_ni
with characlose


"C'est une réponse simple. Mais aussitôt, Shizune fait un pas en avant et me serre dans ses bras."

stop ambient fadeout 3.0

window hide

nvl clear

nvl show dissolve


n "\n\n\n\n\n\n\n\n\nUne étreinte prudente, comme si j'étais en porcelaine, et comme si elle ne savait pas comment prendre quelqu'un dans ses bras. Bien que pour être honnête, je suis pas particulièrement familier avec ça."


n "Son yukata est doux sous mes doigts, mais je peux aussi sentir la chaleur de Shizune."


n "En fin de compte, elle a pensé que c'était la meilleure façon de me montrer ce qu'elle ressentait."

stop music fadeout 3.0

nvl hide dissolve
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
