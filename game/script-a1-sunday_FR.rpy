label fr_A38:


window hide None

scene black
with dissolve

scene bg school_dormhisao
with openeye

play music music_daily fadein 4.0

window show


"Le lendemain, je me réveille un peu étourdi. Il est déjà presque midi."

$ renpy.music.set_volume(1.0,0.0, "ambient")


"Ce n'est pas gênant que je dorme tard, puisqu'on est dimanche et qu'il n'y a pas cours."


"Ce n'est pas juste un dimanche d'ailleurs, mais celui du festival aussi."


"Depuis ma fenêtre, je vois déjà certaines des personnes sur le stand de nouilles soba les étaler sur des plaques pour les personnes ayant besoin d'un repas vite fait."


"Je m'enfile une poignée de mes médicaments matinaux et médite sur comment passer la journée."


"Il y aura quelques exams dans la semaine à venir, mais je ne les vois pas autant que les autres comme des menaces, donc je ne suis pas aussi inquiet que je devrais l'être."


"Sans obligation urgente niveau scolaire, je serai libre de passer la journée comme je veux au festival."

scene bg school_dormhallway
with locationchange


"Finissant ma routine matinale, je sors dans le couloir dans l'intention de trouver quelque chose à manger."


"Passant devant sa porte, je décide de voir ce que Kenji a prévu de faire aujourd'hui."


"Je suis curieux de savoir s'il a des projets, puisque tout le monde fait quelque chose."


"Et puis, je peux imaginer qu'il a construit un abri insonorisé dans sa chambre."


"Ou peut-être quelque chose comme un fort, avec une pancarte “Filles Non Admises” dessus."


"...et avec le “Filles” barré et un “personnes” grossièrement griffonné en dessous."

stop music fadeout 2.0

play sound sfx_doorknock2


"Frappant à sa porte, qui est heureusement dépourvue d'une quelconque sorte de pancarte, j'entends encore une fois le cliquetis inquiétant d'au moins dix targettes tirées vers l'arrière. La porte s'ouvre légèrement."

show kenji neutral at Slide(0.0,0.3,0.0,0.2,0.5)
with Dissolve(.5)


ke "Qui est-ce ?"


hi "Tu es supposé demander ça avant d'ouvrir la porte."

show kenji neutral at center
show bg school_dormhallway at bgright
with charamove

play music music_kenji fadein 1.0


ke "Oh, c'est toi. Merde, il est tôt."


hi "Il est pas vraiment si tôt."

show kenji happy
with charachange


ke "Qu'est-ce qu'il y a, mec ?"


hi "Rien, je me demandais juste ce que t'allais faire aujourd'hui."


hi "La moitié de l'école est déjà dehors."

show kenji rage
with charachange


ke "Dehors ? Pourquoi ?"


hi "Quoi ?"


ke "Quoi quoi ? C'est un jour spécial ? Pourquoi est-ce qu'ils sont là ? Qui sont-ils ?"

show kenji tsun
with charachange


ke "Je peux les entendre. C'est bruyant... ne dis rien... L'invasion a commencé ?"


"Il a soudainement l'air plus alarmé."

show kenji neutral
with charachange


ke "On est quel jour, mec ?"


hi "Ouais j'imagine que tu ne peux pas voir les grands stands en bois dehors, et les gens qui vendent des trucs..."


ke "Qu'est-ce que tu racontes ?! J'ai mes rideaux fermés tout le temps pour déjouer les snipers."


hi "Euuh, c'est le festival. Tu le sais... hein ?"

show kenji tsun
with charachange


ke "Oh bordel, c'est aujourd'hui ? Ah, merde. Ah... merde. Merde."


ke "J'arrive pas à croire que j'ai oublié, je n'ai pas encore fini mon fort. C'est pas bon."


ke "Ça va être une très mauvaise journée... C'est bien que tu m'aies dit ça, mec. Ça va être une mauvaise journée."


hi "Pourquoi ?"

show kenji neutral
with charachange


ke "Oh mec, ils vont être partout. Les gens. Derrière ma fenêtre. Socialisant !"


"Kenji se frotte les tempes nerveusement, ayant soudain l'air très malade."

show kenji tsun
with charachange


ke "Ça va faire un bouquant d'enfer. Merde, et j'avais prévu d'aller dehors aujourd'hui, mais maintenant c'est fichu, tout est fichu."


ke "C'est horrible. Ça craint. Ça craint !"


ke "Fait chier, ça craint vraiment. Je ne peux aller nulle part. Il n'y a nulle part où fuir."


"Kenji semble nerveux. On peut même dire qu'il est vraiment en train de paniquer."

show kenji neutral
with charachange


ke "J'arrive pas à le croire. Donc c'était aujourd'hui."


ke "Merde, et je n'ai même pas pu me préparer pour ça."

show kenji tsun
with charachange


ke "Je n'ai même pas pu m'y préparer psychologiquement et maintenant c'est là et je ne peux rien y faire. T'aurais dû me le dire plus tôt, mon gars. Je veux dire, au moins, je sais, mais... j'aurais pu le savoir plus tôt ! Imagine ce que j'aurais pu accomplir..."


hi "Désolé. Je pensais que tu savais."


hi "Donc j'imagine que tu ne vas pas faire quoi que ce soit aujourd'hui ?"


hi "Il fait bon en plus. Y avait beaucoup de vent hier, donc j'ai pensé qu'il ferait froid aujourd'hui. C'est pas le cas pourtant, donc il n'y a pas de raisons de rester à l'intérieur. Ouais, tu devrais aller voir le festival."


"Kenji grogne et couvre son visage avec ses mains."


ke "Argh, non, non ! Je ne peux pas faire ça. Ils me mangeraient vivant dehors, je le sais."


"Ça doit être une blague, mais il l'a dit avec un visage sérieux. Relativement sérieux."

show kenji happy
with charachange


ke "Qu'est-ce que tu vas faire ? On devrait rester ici, tu peux m'aider à construire mon fort. On peut encore y arriver à temps si on travaille ensemble."



label fr_A38a:



hi "Je vais devoir passer la journée avec le Conseil des Étudiants, vu que j'ai perdu le pari."


"Je réalise que nous ne nous somme pas mis d'accord pour quand et où. Je vais juste les attendre ici, plutôt que de risquer qu'on ne se retrouve pas dehors. Elles doivent être occupées à courir dans tous les sens, de toute façon."


"C'est drôle. J'aurais pensé que le gage pour avoir perdu au stupide jeu de Shizune aurait été beaucoup plus sévère. C'est juste un prétexte pour passer du temps avec elle. Dans ce cas, je crois qu'elle veut juste que je m'amuse."


"Même si elle ne peut pas juste mettre ses intentions au clair, elle pourrait avoir de bonnes intentions après tout, et je crois que je commence à plus l'apprécier."


hi "Je pourrais ne pas y aller, mais ça serait du gâchis. Et je veux y aller, aussi. Je veux dire, aujourd'hui va sûrement être une journée palpitante. Quoi qu'il y ait, ça sera intéressant."

show kenji tsun
with charachange

stop music fadeout 1.0


ke "Le conseil des étudiants ? Quoi ? Ils sont toujours par ici ?"


ke "C'était pas genre, deux mecs ?"


hi "C'est deux filles."

play music music_tension

show kenji rage
with charachange


ke "Vraiment ? Elles sont mignonnes ? Merde, non, attends... elles sont mignonnes ?"


ke "Non ! Ça ne compte pas ! J'ai entendu dire que la présidente du conseil des étudiants est folle... qu'elle ne parle jamais et ne fait que donner des ordres via ses larbins."

show kenji tsun
with charachange


ke "Bordel, elles sont pareilles dans toutes les écoles... Ça a l'air d'une salope au cœur de glace. Toutes des salopes."


ke "Si c'est deux filles, elles te surpassent en nombre. C'est une situation dangereuse, mec. Qui sait ce qui peut arriver."


ke "Merde, le conseil des étudiants est juste composé de deux filles, mais elles ont tellement de pouvoir."


ke "Elles doivent être arrêtées."


ke "Je peux les voir, complotant pour imposer leur programme féministe. Je ne peux pas faire confiance à une administration comme ça."


ke "C'est pas cool. Pas cool !"

show kenji rage
with charachange


ke "Merde. Bordel ! Merde !"



label fr_A38b:



hi "Je ne sais pas. J'ai plutôt faim donc je pense que je vais aller chercher à manger d'abord puis regarder les attractions."


hi "Ton projet de classe semble vraiment cool, et j'ai donné un coup de main dessus donc j'ai au moins envie de le voir et de parler avec Lilly, je crois."


hi "En parlant de ça, tu n'as pas d'obligation avec le projet ?"

show kenji rage
with charachange


ke "T'as perdu la tête ?"


ke "Cette perche aveugle mijote quelque chose ; je peux le sentir dans ma rate, mec. Sa présence est comme une ombre ténébreuse qui est dans le chemin de ma superbe vision."


ke "Comme on pourrait s'y attendre d'une aveugle."


hi "...Quoi ?"


hi "D'ailleurs, je pensais que tu étais aussi..."

show kenji neutral
with charachange


"Il lève une main pour m'interrompre."


ke "Seulement légalement."


ke "Métaphoriquement, je peux voir plus loin que n'importe quel homme n'a pu voir avant moi."


"Kenji regarde stoïquement dans une distance métaphorique pour souligner sa déclaration, en avançant son menton pour avoir l'air plus viril. En fait c'est juste le mur du couloir deux mètres plus loin, mais c'est pareil."

show kenji tsun
with charachange


ke "Je peux voir l'avenir de l'humanité, et il est sombre, sauf si la menace de la femme est étouffée."


ke "Elles sont partout."



label fr_A38c:



hi "Eh bien, j'ai rejoint le club d'art donc je pense que je vais aller avec eux."

show kenji rage
with charachange


ke "Tu as fait quoi ?"


hi "J'ai rejoint le club d'art."

show kenji tsun
with charachange


ke "Mec, c'était une mauvaise décision. Vraiment mauvaise. Tu ne sais pas quel genre de filles il y a dans le club d'art. Des filles attirantes, troublées et angoissantes qui t'arracheront le cœur et le mangeront cru."


"Eh bien, j'en connais une du club d'art, et je ne vois vraiment pas Rin devenir soudainement une meurtrière psychotique."


hi "Ça semble peu probable."


ke "Ne dis pas ça. Ne te méprends pas. Tu n'as pas idée de ce à quoi tu as affaire ici, mec. Elles sont de la pire espèce."

show kenji neutral
with charachange


ke "Elles t'attireront avec toutes ces conneries de sous-vêtements frivoles, et quand tu t'y attendras le moins, BAM !"


hi "Bam quoi ?"


"Kenji semble légèrement dérouté par mon scepticisme, mais pas moins loufoque."

show kenji tsun
with charachange


ke "Peu importe."


ke "Avance avec prudence mec, avance avec prudence."



label fr_A38d:



hi "Je me demande... j'ai pas mal faim, mais j'ai passé cet accord où je dois essayer de prendre soin de moi-même. Être en meilleure santé, tu vois."


hi "Je sais pas si je dois éviter les takoyaki, ou foncer dessus."

show kenji tsun
with charachange


ke "Accord ? Ça a l'air inquiétant. Et qu'est-ce que t'as en retour ?"


hi "Rien, je crois ? Ce n'est pas ce genre d'accord."


hi "Tu connais Emi, qui est de la même année que nous ? On s'est mis d'accord sur le fait de prendre mutuellement soin de nous et..."

show kenji rage
with charachange


ke "Aïeeeeeeee !"


"Le cri perçant et l'expression de terreur abjecte sur le visage de Kenji me glace le sang. C'est comme si j'avais dit à un prêtre catholique que j'avais vendu mon âme au diable."


ke "Elle ! Tu as vendu ton âme au diable, et tu n'as rien eu en retour ?"


ke "Qu'est-ce qui va pas chez toi, mec ?"


ke "Tu sais à qui t'as à faire ?"


ke "Elle est un danger pour la santé publique. Tu sais combien de personnes elle envoie à l'hôpital par mois avec ses attaques aériennes méticuleusement préparées ?"

show kenji tsun
with charachange


ke "Elle est l'une d'entre elles ! Un membre clé dans la vaste conspiration qui vise à la complète soumission de tout ce qui est masculin."


ke "Je n'arrive pas à croire ce que j'entends. J'avais confiance en ton jugement, mec. Je pensais qu'on était comme des frères."


ke "Tu dois interrompre tout ça avant qu'il ne soit trop tard."


ke "Le festival aussi ; c'est juste l'un de leurs stratagèmes."



label fr_A38e:


"Il frotte son écharpe nerveusement du bout des doigts, de plus en plus vite comme s'il essayait de faire du feu, puis commence lentement à se calmer après que sa crise d'angoisse se soit finie."

show kenji neutral
with charachange


ke "Je vais devoir trouver un endroit pour me cacher, un havre de paix. Et puis m'assommer pour ne pas avoir à expérimenter ce jour horrible."


ke "J'ai la chose parfaite pour ça. Je dois me préparer maintenant."

show kenji tsun
with charachange


ke "Ne va pas au festival."


hi "D'accord."

show kenji neutral
with charachange


ke "À plus, mec."

stop music fadeout 2.0

hide kenji
with charaexit


"La porte se referme lentement avec un léger crac et je ne sais pas quoi penser à propos de ce que vient de dire Kenji."




label fr_A44:

show bg school_dormhallway at bgright
with None


"Je médite sur ce que je pourrais faire avec Shizune et Misha. Décidant qu'il est mieux d'être préparé, je retourne dans ma chambre pour remplir mon portefeuille."

scene bg school_dormhisao
with locationchange


"Je me demande s'ils ont ce jeu où on doit essayer d'attraper des poissons rouges avec un filet en papier."


"Ça semble beaucoup plus facile qu'ils veulent en donnent l'air. Et puis, si je devais attraper un poisson rouge, je n'aurais aucune bonne raison de le garder."


"Qu'est-ce que je ferais avec un poisson dans ma petite chambre ? Le cuisiner ?"


"Je pourrais le donner à Shizune, ou Misha, mais ça pourrait être mal reçu."


"C'est un vrai problème. Elles sont toutes les deux mignonnes, mais je pense n'avoir de chance avec aucune des deux. J'imagine comment seraient leurs réactions si je devais leur donner un cadeau ce soir, comme un poisson ou une peluche."


"Misha rirait probablement comme elle le fait d'habitude. Shizune pourrait m'envoyer balader."


"Peut-être que ce n'est pas une aussi bonne idée après tout."


"Bien, je crois que je suis prêt."

with shorttimeskip


"Un bon moment plus tard, je me mets à penser que ça pourrait être un autre plan de Shizune pour me tester. Même si ce n'est pas le cas, il commence à se faire tard."



scene bg school_dormhallway
show shizu behind_blank_close at center
with locationchange


"Aussitôt que je mets le pied dehors, je percute presque Shizune."


hi "Salut, Shizune. Où est Misha ?"

show shizu behind_frustrated_close
with locationchange


"J'essaye de le faire en signes autant que je le peux, mais je fais un peu n'importe quoi. Je dois demander à Misha de m'apprendre quelques trucs."


mi "Ici !"

play music music_comedy

show shizu behind_frustrated_close at Slide(0.5,0.5,0.7,0.5,1.0, time_warp=_ease_time_warp)
with None

show misha hips_grin behind shizu at Slide(0.5,0.5,0.3,0.5,1.0)
show shizu behind_frustrated_close at Slide(0.5,0.5,0.7,0.5,1.0,time_warp=_ease_time_warp)
with Dissolve(0.7)


"Misha apparaît derrière Shizune, affichant un large sourire."


mi "On est juste venues pour être sûres que tu viennes avec nous au festival."

show shizu basic_angry_close at tworight
with charachange

shi "…"

show misha sign_smile at twoleft
with charachange


mi "Ne reviens pas sur ta promesse~ !"


hi "Promesse ? Je ne crois pas avoir promis quoi que ce soit."

show shizu cross_angry_close
with charachange

shi "…"

show misha hips_frown
with charachange


mi "N'essaye pas de t'en sortir !"

show misha perky_sad
with charachange


mi "Allez, Hicchan, ça serait fun ! Tu dois le faire, de toute façon, ou tu deviendras une personne bonne à rien !"

show misha perky_smile
with charachange


mi "Tu n'as pas envie de devenir une de ces personnes qui restent juste dans leur chambre toute la journée, devenant paranoïaques, hein ?"


"Je me surprends à regarder par-dessus son épaule vers la porte de Kenji juste à côté de ma chambre."


"J'espère qu'il n'a pas entendu ça, mais je crois que Misha espère l'opposé."


hi "Non, bien sûr que non. Je plaisantais juste un peu, et j'étais d'accord pour y aller de toute façon. Vous n'aviez pas à venir ici."

show misha cross_laugh
with charachange


mi "Vraiment ? Ahahaha ! Shicchan était inquiète que tu puisses essayer de t'échapper !"

show misha hips_grin
with charachange


mi "On a besoin de toi, Hicchan~ !"


hi "Huh ?"


"Je crois que mon cœur vient de sauter un battement."

show misha perky_smile
with charachange


mi "Je n'ai pas la précision pour faire tomber les peluches de leur piédestal dans ce jeu... et Shicchan refuse de jeter des choses."

hi "Oh."


"Shizune me fixe, remarquant immédiatement ma déception. Elle décroise les bras et ajuste ses lunettes."

show shizu adjust_happy_close
with charachange

shi "…"


mi "Qu'est-ce que tu croyais qu'on voulait ? Je refuse de jeter quoi que ce soit."

show misha perky_confused
with charachange


mi "Pourquoi, Shicchan ? C'est bizarre..."

show misha perky_smile
with charachange


mi "Bon, de toute façon, Hicchan, tu as déjà jeté une balle, hein~, hein~ ? Donc ! Tu dois venir avec nous !"


"Je suis bluffé par leur logique. Je ne sais pas si elles plaisantent ou pas."


hi "Heh, je me sentirais offensé si je ne savais pas que vous plaisantez."


hi "Vous plaisantez, hein ?"

show shizu behind_frown_close
with charachange

shi "…"


mi "C'est ce que c'est, Hicchan~ ! C'est ce que c'est ce que c'est ce que c'est ce que c'est !"


hi "Eh bien c'est rassurant."

show shizu basic_normal2_close
with charachange

shi "…"

show misha hips_smile_close at closeleft
with characlose


mi "Allez, on y va ! Le groupe des sourds se met en place dehors."


"Misha m'attrape par la main et fait mine de me tirer jusqu'à la porte, mais il est clair qu'elle n'essaye pas du tout."

hide shizu
with None

show shizu basic_normal2_close behind misha at tworight
with None

show shizu adjust_blush_close
with charachange

stop music fadeout 3.0


"Shizune nous regarde tous les deux, rougissant un peu et triturant ses lunettes avec impatience."


"Je ne suis pas habitué à ce genre de contacts occasionnels, mais je n'ai rien contre. Comment pourrais-je objecter ?"

play ambient sfx_crowd_outdoors fadein 1.0

scene bg school_courtyard
show crowd
with locationskip

play music music_running


"Il fait toujours clair dehors, mais le soleil s'apprête à se coucher derrière les arbres."


"On dirait que la moitié de l'école est dehors, et je peux même voir quelques membres du corps professoral sur le côté, se servant allégrement dans le punch."


"Ils sont sur le point de vider le bol entier, au grand dam de la fille qui travaille au stand."


"Il y a des diseurs de bonne aventure qui discutent avec leurs amis, pendant que les autres sont déjà en train de prédire l'horoscope à quiconque marchant dans l'allée."


"Je trouve que ce genre de tactique est un peu trop agressif, mais ça montre qu'ils sont motivés. C'est agréable à voir, mais je ne sais pas si je serai en mesure de m'y habituer."

show shizu basic_normal2 at tworight
show misha perky_smile at twoleft
with charaenter

shi "…"

show misha sign_smile
with charachange


mi "Eh bien, on devrait prendre quelque chose à manger. Faim, Hicchan ?"


"À y penser, je n'ai pas mangé de la journée."


hi "Je n'ai pas vraiment envie de manger des nouilles frites."

show misha hips_grin
with charachange


mi "C'est pas grave, il y a des autres trucs frits !"


hi "Il y a quelque chose qui n'est pas frit ?"

show shizu adjust_smug
with charachange

shi "…"


mi "Les bonbons. La malbouffe est l'essence de la fête !"

show misha cross_laugh
with charachange


mi "Wahahahaha !"

show shizu behind_smile
with charachange

shi "…"

show misha hips_grin
with charachange


mi "Allez, je — je veux dire, Shicchan — te paye un truc~ !"


mi "Un ?"

show shizu adjust_smug
with charachange


shi "... !"

show misha sign_smile
with charachange


mi "Juste un~ ! Seulement pour avoir de l'énergie pour le jeu du lancer !"

show misha perky_smile
with charachange


mi "Ah, mais il ne semble pas que tous les stands soient montés, donc tu pourrais ne pas avoir ce que tu veux."


"Je jette un œil aux alentours, surpris par le nombre de stands. C'est incroyable, le festival semble plus grand que ceux qu'on peut voir en ville."


"Malgré ce que Misha a dit, il semble que la moitié de l'école soit déjà en train de s'amuser."


"L'air bourdonne avec les bavardages excités d'au moins la moitié du corps étudiant."


"Je peux sentir la cuisson des aliments, et ça ne fait que me donner encore plus faim."

show shizu behind_frustrated
with charachange

shi "…"

show misha perky_confused
with charachange


mi "Allez, Hicchan, la nourriture se vend déjà rapidement ! Si tu veux des takoyaki, on doit bouger maintenant !"

show misha hips_grin
with charachange


mi "Je serais partante pour des takoyaki~ ! Allez, allons manger ça !"


hi "D'accord, j'ai pas mangé de takoyaki depuis super longtemps. Je suis de la partie."

hide shizu
with charaexit

hide misha
with charaexit


"Shizune part avant que Misha puisse lui traduire en signes, marchant vivement vers le stand de takoyaki pendant que Misha essaye de la rattraper."

scene bg school_stalls1
with locationchange


"Misha rit en sautant vers Shizune, qui commande trois takoyaki en levant trois doigts."


"Je ne l'ai jamais remarqué avant, mais pour quelqu'un qui est tellement obsédée par le thé de grande classe, c'est un peu étrange que Shizune aime autant la malbouffe."


"Je prends la barquette de takoyaki qu'elle me tend et je me demande si je dois commencer à manger. Ça a l'air extrêmement chaud."


"Je peux voir la fumée en sortir et l'huile faire des bulles à la surface."

show misha hips_smile at Slide(0.2,0.5,0.3,0.5,1.0)
show shizu behind_blank at Slide(0.8,0.5,0.7,0.5,1.0)
with Dissolve(1.0)


"Shizune et Misha me regardent toutes les deux, comme si elles attendaient que je mange avant de pouvoir commencer."


"Je ne peux pas me défiler, donc je détache une des petites fourchettes en plastique collée sur un coin de la barquette."

show misha hips_grin at twoleft
show shizu basic_normal at tworight
with charachange

stop music fadeout 12.0


"Toutefois, avant même que je puisse la mettre dans ma bouche, Shizune et Misha ont déjà commencé à manger avidement, Shizune prenant des rapides mais délicates bouchées de takoyaki pendant que Misha se régale comme une enfant."


"Je pense qu'en fin de compte, elles sont toutes deux juste des enfants s'amusant comme les autres étudiants ici."


"C'est plutôt agréable. Je pense que ça fait longtemps que je n'ai pas eu la chance de me balader comme ça avec d'autres personnes et d'apprécier leur compagnie."


"Même avant de venir ici, j'ai traversé une année très chargée. Tellement chargée que je n'ai pas réalisé ce que j'avais manqué jusqu'à maintenant."


"Ici, je me sens en paix."


"C'est une atmosphère apaisante. Je ne savais pas que ce genre de festivals existaient encore."

show misha perky_confused
with charachange


mi "Eh ? Hicchan, tu manges pas ?"


hi "Si, je vais manger."

show shizu adjust_smug
with charachange

shi "…"

show misha sign_smile
with charachange


mi "J'espère que tu chipotes pas parce que c'est trop chaud."


hi "C'est pas pour ça."


"Même leurs piques commencent à devenir attachantes."

$ renpy.music.set_volume(0.6, 2.0, "ambient")

scene bg school_stalls1_ss
with shorttimeskip

play music music_tranquil fadein 1.0


"Je mange rapidement avant que ça refroidisse, pensant que le léger éclairage des lanternes en papier rougeoyantes devant le coucher de soleil fait un beau spectacle."

show shizu behind_smile_close_ss at center
with charaenter


"Avant que je puisse finir ma dernière bouchée de takoyaki, Shizune se met en face de moi, se tenant parfaitement droite avec ses bras dans le dos."


"Je peux voir qu'elle fait de son mieux pour avoir l'air la plus sérieuse possible, mais elle n'arrive pas à totalement cacher sa bonne humeur, car il y a un léger sourire sur son visage."

show bg school_stalls1_ss at bgright
show shizu behind_smile_close_ss at closeright
with charamove

show misha cross_laugh_ss at twoleft
with charaenter


mi "Ahahaha~ ! Allez, Hicchan, allons faire des jeux !"


hi "Ils ont fini d'installer ?"

show shizu adjust_happy_close_ss
with charachange

shi "…"

show misha cross_grin_ss
with charachange


mi "Non, mais c'est pas grave, c'est pas grave~ ! Allez, Hicchan, avant qu'il y ait trop de monde !"

show misha hips_grin_close_ss at closeleft
with characlose


"Misha pose une main sur mon épaule et rit très bruyamment."

show misha perky_smile_close_ss
with characlose


mi "Allez ! Allez ! Les lots ont l'air vraiment super cette année, vraiment vraiment~ ! Tu ne voudrais pas gagner des lots pour deux filles mignonnes comme nous ?"


"Misha prend sa meilleure pose “mignonne”, ce qui est certes très mignon. Je regarde vers Shizune, espérant pareil de sa part, mais elle me regarde juste comme si j'étais fou."

show shizu cross_wut_close_ss
with charachange

shi "…"

show misha hips_grin_close_ss
with characlose


mi "Misha, arrête de faire ça !"

show misha perky_confused_close_ss
with charachange


mi "Attends... Je suis Misha..."

show shizu basic_normal2_close_ss
with charachange

shi "…"

show misha sign_smile_close_ss
with charachange


mi "Hicchan, dépêche, tu tiens ce morceau de takoyaki depuis un millier d'années !"

show misha cross_laugh_close_ss
with charachange


mi "Hahahahaha !"

show misha cross_smile_close_ss
with charachange


hi "J'aime savourer tout ce que je mange. Même ça."

show shizu basic_sparkle_close_ss
with charachange

show shizu adjust_smug_close_ss
with charachange


"Sans me prévenir, Shizune prend le takoyaki de ma main et le met dans sa bouche avec un sourire."


"C'est arrivé si vite que je n'aurais pas pu l'arrêter."

show misha cross_laugh_close_ss
show shizu behind_smile_close_ss
with charachange


"Avant que je puisse comprendre ce qui vient d'arriver, Misha éclate de rire, et Shizune me sourit, probablement le sourire le plus proche d'un rire que j'aie vu de sa part."

show shizu adjust_happy_close_ss
with charachange


shi "... !"


mi "Eh bien, comme ça c'est réglé~ ! Wahaha ! Hahahaha !"

stop music fadeout 6.0


"Shizune attrape ma main droite, et Misha ma main gauche."

show shizu behind_smile_close_ss
with charachange

shi "…"

show misha hips_grin_close_ss
with charachange


mi "Tu viens avec nous ! Il y a plein de trucs à faire ce soir, tu devrais t'amuser et apprécier !"

show misha cross_laugh_close_ss
with charachange


mi "Hahahaha~ !"

$ renpy.music.set_volume(1.0,2.0, "ambient")

scene bg school_courtyard_ss
show crowd_ss
with shorttimeskip

play music music_ease fadein 6.0


"Courant à travers une foule déjà considérable de personnes, on fait jeu après jeu, du lancer d'anneaux au frappe-taupes, en passant par des jeux dont je n'ai jamais entendu parler."


"On gagne rarement, mais c'est quand même amusant."


hi "Hé, ils ont le jeu où il faut attraper les poissons ici ?"

show shizu behind_smile_ss at tworight
show misha hips_smile_ss at twoleft
with charaenter

shi "…"


mi "Bien sûr ! Je ne savais pas que tu aimais ce jeu, Hicchan !"


hi "Eh bien, j'ai toujours voulu essayer. Ça semble pas trop dur."

show misha hips_grin_ss
with charachange


mi "T'es sûr de ça, Hicchan~ ?"

show misha cross_laugh_ss
with charachange


mi "Wahahaha~ ! D'accord, d'accord ! On va voir ! Ça devrait être quelque part par ici !"

show shizu basic_normal_ss
with charachange

shi "…"

show misha perky_smile_ss
with charachange


mi "Mais, tu vas garder le poisson ? T'as un bocal pour ça ?"


hi "En fait, non..."

show misha hips_grin_ss
with charachange


mi "Peut-être qu'il va le manger !"

show shizu adjust_smug_ss
with charachange

shi "…"

show misha cross_laugh_ss
with charachange


mi "Hahahahahaha ! Ahahahahahaha !!"

show misha cross_grin_ss
with charachange


mi "Très bien, Hicchan, si on gagne des poissons, on te les donnera !"


hi "Oh, vraiment ? Un autre jeu ? Bien, alors."

show shizu basic_happy_ss
with charachange


"Shizune me pousse avec énergie vers le stand, essayant de cacher l'enthousiasme dans ses yeux."

scene bg school_stalls2_ss at bgright
with locationchange


"Heureusement, aucune des deux n'a réussi à capturer un poisson, mais je n'ai pas fait mieux."

show bg school_stalls2_ss at bgleft
with charamove

$ renpy.music.set_volume(0.6,2.0, "ambient")

"Je ne peux pas m'empêcher de rire. Immédiatement après, elles commencent à me tirer vers un large stand particulièrement coloré que j'ai aidé à construire."


"Je me rappelle de celui-là ; ça a été vraiment chiant à faire."


"L'exposant, un gars ordinaire avec les cheveux teints couleur châtain, lève la tête quand il nous voit nous approcher. Je remarque deux choses :"


"Premièrement, c'est un de ces jeux où on doit jeter une balle sur une pyramide de boîtes opaques et essayer d'en faire tomber le plus possible."


"Quatre balles pour 50 yen, c'est plutôt bien."


"Deuxièmement, il y a des instructions de jeu en braille. J'ai presque envie de dire quelque chose, et regarde pour savoir si Shizune et Misha voient la même chose."


"Soit ce n'est pas le cas, soit elles ne trouvent pas ça étrange du tout."


"Exposant" "Hé ! C'est cool de te voir, Hakamichi ! Merci d'avoir autant aidé avec ce stand. Tu t'amuses bien ?"


"Shizune regarde vers Misha, qui lui traduit tout en un éclair, puis retourne son attention vers l'exposant."

show shizu behind_smile_ss at Slide(0.8,0.5,0.7,0.5,1.0)
show misha perky_smile_ss at Slide(0.2,0.5,0.3,0.5,1.0)
with Dissolve(1.0)

shi "…"

show misha hips_grin_ss at twoleft
with charachange


mi "Haha~ ! C'était rien, rien du tout, vraiment~ ! Ouais, c'est super, je crois que c'est le meilleur festival qu'on a mis en place !"

show misha perky_smile_ss
with charachange


mi "Shiraki, on voudrait jouer, on peut, hein ?"

show misha hips_grin_ss
with charachange


mi "Bien sûr~, ce serait vraiment super si tu donnais un lot aux mignonnes représentantes du conseil des étudiants pour leur dur travail, pour toutes les heures qu'on a passées à rendre tout ça possible !"

"Shiraki" "Hahaha, haha… Non."


"En tout cas, Shiraki, il en a."


hi "Hé, j'ai construit ce stand, c'était un travail éreintant, aussi. J'ai gaspillé deux heures de ma vie, je crois que je mérite au moins un tour gratuit."

show misha hips_frown_ss
with charachange


mi "Et moi !"

show shizu basic_angry_ss at tworight
with charachange

shi "…"


mi "Moi aussi !"

show misha perky_confused_ss
with charachange

mi "Ah…"


"Après avoir hésité, il abandonne, et nous remet à chacun quatre balles avec un haussement d'épaules."

show misha hips_grin_ss
show shizu behind_blank_ss
with charachange


"À peine une seconde plus tard, Shizune et Misha me les tendent."


hi "Pour quoi faire ?"


hi "Ne me dites pas qu'après avoir fait un aussi gros scandale, vous n'allez même pas jouer ?"


hi "Pas après la façon dont on s'est ligués contre Shiraki."


"Shiraki" "Ouais..."

show shizu basic_frown_ss
with charachange

shi "…"

show misha sign_smile_ss
with charachange


mi "Reste en dehors de ça, s'il te plaît~ !"

show shizu adjust_happy_ss
with charachange


"Shizune se tourne vers moi et commence à agiter sa main dédaigneusement. Misha semble indécise entre lui traduire ou consoler le teneur à changer du stand."

show shizu adjust_smug_ss
with charachange


shi "... !"

show misha hips_grin_ss
with charachange


mi "Ahahaha ! Hicchan, où est ton sens de la chevalerie ? D'ailleurs, je—Shicchan, a une politique contre le jeter de balles !"

show misha hips_smile_ss
with charachange


mi "Ah, désolée, Hicchan. Je ne sais pas si ma précision est si bonne, non plus. Tu dois être plutôt bon à ces trucs, cependant, hein, hein ? Ça ne devrait pas être un problème pour toi !"

stop music fadeout 3.0


"Ça a l'air plutôt simple. Les bouteilles ne sont même pas si loin, le seul défi est que ces balles soient en plastique."

play sound sfx_impact


"J'en jette une fort sur les bouteilles, et elle rebondit sans réaction."

show shizu behind_blank_ss
show misha perky_confused_ss
with charachange


hi "Euh, quoi ?"


"Shiraki" "Ah, ouais, c'est pas aussi facile que ça en a l'air. Il y a de l'eau à l'intérieur des bouteilles. Secret commercial."

show misha hips_frown_ss
with charachange


mi "Ce n'est pas très juste !"


hi "Ça doit être pour ça qu'il y a quatre balles pour 50 yen. Vraiment sournois."

show shizu basic_angry_ss
with charachange

shi "…"

show misha hips_smile_ss
with charachange


mi "Allez, Hicchan, tu peux les faire tomber ! Tu as encore onze chances ! Go !"


hi "Peut-être que tu devrais le faire."


hi "Shizune ? Tu veux essayer ?"

show shizu behind_blank_ss
with charachange


"Shizune secoue énergiquement la tête de droite à gauche."


"Je me mets à rire, c'est vraiment drôle."

play sound sfx_impact
play music music_soothing fadein 3.0


"Après ça, je jette une autre balle vers la pyramide de bouteilles et arrive à les faire bouger légèrement."

show shizu basic_normal_ss
show misha perky_smile_ss
with charachange


"Shizune et Misha jettent des regards insistants vers une peluche en forme de chat."


"Après tout, elles ne sont pas si différentes."


"Des fois je me demande si Shizune aurait le même ton que Misha si elle pouvait parler."


"Non, elles ne sont pas si similaires."

play sound sfx_impact


"Je lance une autre balle, réalisant que c'est en fait plutôt simple. Si je peux frapper deux bouteilles de la rangée du bas en même temps, c'est facile."


"Déjà, une petite foule commence à se rassembler, donc la pression est vraiment sur moi. Encore neuf tirs."

play sound sfx_dropstuff


"M'étirant le bras comme un lanceur de baseball, je lance aussi fort que je peux et les bouteilles s'écroulent."

show shizu behind_blank_ss
show misha cross_laugh_ss
with charachange

show stuffedcat:
    alpha 0.0 yalign 0.5 xanchor 0.5 xpos 0.6 subpixel True
    easein 1.0 xpos 0.5 alpha 1.0
with Pause (1.0)


"Triomphant, je réclame la peluche de chat et Misha rit à gorge déployée comme si c'était elle qui avait gagné."


"Shizune me fixe avec son visage inexpressif habituel. Il est clair qu'elle veut la peluche aussi."

show stuffedcat:
    easeout 1.0 xpos 0.4 alpha 0.0
with Pause (1.0)

hide stuffedcat
with None

show shizu basic_normal2_ss
with charachange

shi "…"

show misha hips_grin_ss
with charachange


mi "Hicchan, félicitations~ ! Qu'est-ce que tu vas faire avec cette peluche ?"


"Il n'y a pas de bonne réponse. Je dois faire preuve de prudence."




hi "Je... ne sais pas."


mi "Eeeeeeeeh bien~ je vais la prendre, si tu n'en veux pas..."

show shizu adjust_smug_ss
with charachange

shi "…"

show misha cross_grin_ss
with charachange


mi "Sauf si tu veux la garder pour toi, Hicchan. Je ne savais pas que tu aimais les peluches. Que c'est délicat."


hi "C'est pas le cas. Elle ne m'intéresse pas."

show misha cross_smile_ss
with charachange


mi "Je peux l'avoir, alors ?"

show shizu behind_blank_ss
with charachange

shi "…"


"Leurs yeux me percent l'âme."


"C'est une décision que je ne veux pas prendre. Je me retourne vers le stand."


hi "Hé, tu as plus d'une peluche comme ça ?"


"Shiraki" "En fait, ouais, juste une autre."


hi "D'accord, remets tout en place, je veux essayer pour celle-là aussi."


"J'ai toujours huit essais."

play sound sfx_pillow


"Aussitôt que les bouteilles sont remises en place, je jette encore une fois aussi fort que je peux, mais loupe."

show misha hips_grin_ss
with charachange


mi "Hahaha ! Essayer d'en gagner une autre ? Tu choisis la solution facile, Hicchan ?"


hi "Si c'est aussi facile, tu peux essayer."


mi "Non merci~ !"

show misha perky_smile_ss
with charachange


mi "Dis, Hicchan, tu peux au moins poser la peluche pendant que tu jettes les balles ?"


hi "Non."

show shizu adjust_smug_ss
with charachange

shi "…"


mi "Il n'en reste qu'une, tu ferais bien de l'avoir ! Si tu échoues, je te tue~ !"

show shizu behind_smile_ss
with charachange

shi "…"


mi "Quelle façon habile d'éviter de me donner la peluche, cependant ! Et par moi, je veux dire moi~ !"

show shizu adjust_happy_ss
with charachange

shi "!"

show misha cross_laugh_ss
with charachange


mi "Ahahahaha~ ! Je plaisante !"


"Je peux voir que Misha n'a pas dit ça pour être méchante, et Shizune semble apprécier sa blague, lui souriant, mais elle semble un peu déprimée après."


"Je décide de lui donner la peluche, au moins pendant que je suis en train d'essayer de gagner l'autre. C'est plutôt dur de viser en tenant un chat géant."

show shizu behind_smile_ss
show misha perky_smile_ss
with charachange

shi "…"


mi "Merci, Hicchan, Shicchan semble contente, Hicchan~ ! Mais, tu vas en gagner une autre pour moi aussi, hein ?"


hi "C'est ce que je suis en train d'essayer de faire."

stop music fadeout 5.0

show shizu behind_smile_ss at Slide(0.7,0.5,0.8,0.5,1.0, time_warp=_ease_out_time_warp)
show misha perky_smile_ss at Slide(0.3,0.5,0.2,0.5,1.0, time_warp=_ease_out_time_warp)
with None

hide shizu
hide misha
with Dissolve(1.0)

play sound sfx_pillow


"Je tire encore une fois, mais ma précision me fait défaut cette fois."


"Mon bras est assez lourd aussi, comme si le sang ne circulait pas correctement."


"Je me gronde mentalement, pensant qu'il est pathétique que je puisse être fatigué après quelque chose comme ça."


"Puis je réalise que c'est peut-être à cause de mon cœur. Si c'est ça, alors je ne sais pas quoi penser."

play sound sfx_impact


"Il est déprimant que quelque chose d'aussi insignifiant que ça soit suffisant pour me faire réaliser ma propre mortalité."


"Je pense qu'il n'y aura plus jamais un moment où je serai en mesure d'oublier tout ça."


"Même aujourd'hui, quand je pensais pouvoir m'amuser, par cette belle soirée dans ce bel endroit, je ne peux pas échapper à la raison pour laquelle je suis ici."


"Je ne me suis jamais senti aussi en paix de ma vie, dans un endroit qui est comme aucun que j'ai pu voir."

play sound sfx_pillow
play music music_sadness fadein 2.0


"Il est dur maintenant de ne pas penser à l'impensable."


"Que j'aie pu être envoyé ici juste pour mourir."


"Ces derniers jours ont été parmi les meilleurs de ma vie. Pour la première fois depuis longtemps, je me suis senti vraiment vivant."


"Mais en fin de compte, je suis quelqu'un à qui il est rappelé, à chaque fois qu'il monte trop d'escaliers ou lance une balle trop fort, qu'il peut mourir à chaque seconde."

play sound sfx_pillow


"Je serai toujours limité par ça."


"Je me sens déprimé à cause de ça, et en colère aussi. En fin de compte, je me soucie de ma vie, et l'apprécie, et maintenant c'est plus transitoire que ça l'était avant."


"Je me demande si c'est ce qui va finalement arriver. Ça pourrait être n'importe quoi, si je suis aussi faible et pathétique : une mauvaise chute, un coup de poing dans la poitrine, une balle de base-ball perdue."


"J'ai maintenant perdu mon envie de continuer de jouer à ce jeu, mais je continue de jouer quand même."

stop music
$ renpy.music.set_volume(0.0,0.0, "ambient")
play sound sfx_heartfast

show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)


"Soudainement, je ressens pendant une fraction de seconde une douleur dans la poitrine. Ça vient et repart instantanément, mais c'est suffisant pour me faire un peu trébucher."

$ renpy.music.set_volume(0.4,10.0, "ambient")

show shizu adjust_blush_close_ss at Slide(0.8,0.5,0.7,0.5,0.5)
show misha perky_confused_close_ss at Slide(0.2,0.5,0.3,0.5,0.5)
with Dissolve(0.5)


"Shizune fait un bon en arrière, surprise. Elle s'approche, me regarde avec inquiétude. Misha pose sa main sur mon épaule."

play music music_pearly


mi "Hé, Hicchan, ça va ?"


hi "Ouais, ça va. Je ne me sens pas vraiment bien là. Je crois que je suis malade. Je ne pense pas pouvoir continuer."

show misha hips_frown_close_ss at twoleft
with charachange


"Misha fronce les sourcils."


mi "Ne te force pas. Si t'es aussi malade, ça aggravera juste les choses."

show shizu basic_normal2_close_ss at tworight
with charachange

shi "…"

show misha hips_smile_close_ss
with charachange


mi "Regarde, le festival vient juste de commencer, et on a joué à ce jeu pendant un moment. On peut prendre une petite pause si t'es fatigué."

show misha sign_smile_close_ss
with charachange


mi "Bonne idée, Shicchan, je me sens un peu fatiguée aussi ! Je crois qu'on est tous un peu épuisés d'avoir couru dans toute l'école, Hicchan !"


"Je hoche la tête. Elles ne semblent pas remarquer quelque chose d'inhabituel. C'est bien."

scene bg school_courtyard_ni
show crowd_ni
with shorttimeskip

$ renpy.music.set_volume(1.0,2.0, "ambient")


"Nous marchons à travers l'océan de gens, avec Misha qui pointe joyeusement le visage de tous ceux qu'elle connaît. Shizune tient le chat en peluche dans ses bras, le berçant distraitement. On dirait qu'elles s'amusent bien."


"Soudainement, je ressens une pointe de culpabilité."


"À cause de ma santé fragile, on a dû tous s'arrêter."

show shizu behind_smile_ni at tworight
show misha perky_smile_ni at twoleft
with charaenter

shi "…"


mi "Hicchan, on a toutes les deux faim. Et toi ?"


hi "J'ai pas si faim que ça, mais je mangerais bien quelque chose."

show misha hips_smile_ni
with charachange


mi "C'est suffisant, Hicchan~ ! Donc, qu'est-ce qu'on devrait prendre à manger ?"


hi "Peu importe pour moi."

show shizu adjust_happy_ni
with charachange

shi "…"

show misha hips_grin_ni
with charachange


mi "Ah ! Pourquoi pas des sandwiches, alors ? Et on a besoin de boire, aussi ! Misha va tout aller chercher !"

show misha perky_confused_ni
with charachange


mi "Quoi ?"

show shizu behind_smile_ni
with charachange


"Shizune me regarde et sourit, puis je réalise qu'elle essaye de me remonter le moral avec une blague. Je me mets à rire."

show shizu adjust_happy_ni
with charachange

shi "…"

show misha perky_smile_ni
with charachange


mi "Hicchan, c'est plutôt bondé, donc on pourra peut-être pas manger ici. C'est plutôt bruyant, aussi."

show misha sign_smile_ni
with charachange


mi "Peut-être qu'on devrait aller manger sur le toit."


hi "Ça me va. Il doit y avoir une belle vue, et il y aura sûrement une petite brise."

show misha hips_grin_ni
with charachange


mi "Ok alors ! J'imagine que je devrais aller chercher à manger et à boire maintenant... Donc je vous vois après~ !"

hide misha
with charaexit

stop music fadeout 6.0


"Misha fait un petit signe et s'en va."


"Avant, je n'avais pas remarqué à quel point les lanternes en papier brillaient pendant la nuit, mais maintenant que je peux le voir, c'est vraiment un spectacle étonnant."


"Des lucioles volent au-dessus de nos têtes, leur douce lueur donnant l'impression qu'il neige des lumières dans le ciel de la nuit."


"C'est le genre de choses qu'il serait impossible de voir en ville."

show shizu adjust_happy_ni at Slide(0.7,0.5,0.5,0.5,0.5,time_warp=_ease_time_warp)
with None

show shizu cross_angry_close_ni at Slide(0.7,0.5,0.5,0.5,0.5,time_warp=_ease_time_warp)
with Dissolve(0.5)


"Shizune tire sur ma manche avec impatience et croise les bras en fronçant les sourcils comme pour montrer son mécontentement que je sois distrait."

show shizu basic_angry_close_ni at center
with charachange

shi "…"


hi "Tu sais que je ne sais pas lire le langage des signes."

show shizu behind_frown_close_ni
with charachange

shi "…"


"En y pensant, c'est pas stupide de ma part d'avoir dit ça à quelqu'un de sourd ? Elle ne peut pas m'avoir entendu."

show shizu behind_blank_close_ni
with charachange


"Je hausse les épaules, espérant lui montrer que je ne peux pas comprendre. Shizune secoue la tête et me fait signe de la main de laisser tomber."


"Peut-être que je devrais demander à Misha des leçons sur le langage des signes."

$ renpy.music.set_volume(0.3, 1.0, "ambient")

scene bg school_roof_ni
with locationskip


"En montant sur le toit, je me trouve encore une fois terrifié par la taille de cette école. Les terrains sont si vastes que je ne peux pas croire que je ne l'avais pas réalisé avant."


"Pendant que je marche sur le toit, traînant derrière Shizune, je ne peux pas m'empêcher de me perdre dans les étoiles brillant dans le ciel."

show shizu behind_smile_close_ni at center
with charaenter


"Shizune et moi nous asseyons sur un banc. Elle semble être de bonne humeur vu qu'elle sourit doucement tandis que la brise fait remuer ses cheveux."


"Nous regardons le festival en bas qui ressemble à une mer de lanternes lumineuses orange et d'éventails en papier agités par les gens, certains d'entre eux vêtus de yukata."


"En fait, la plupart des filles semblent porter des kimono. Je me demande pourquoi Shizune et Misha n'en portent pas aujourd'hui."


"Elles seraient bien en kimono. Je pense brièvement à quel genre de kimono elles porteraient."


"Shizune serait probablement avec quelque chose de traditionnel. Par contre, il est plus dur de se représenter Misha."


"Misha arrive dans notre direction en haletant, essayant d'empêcher ce qu'il y a dans ses bras de tomber."


"Posant tout par terre, elle se laisse tomber en arrière."

show shizu behind_smile_close_ni at tworight
show bg school_roof_ni at bgright
with charamove

show misha hips_grin_ni behind shizu at twoleft
with charaenter


mi "Ahahahahahahahahaha~ ! Ça a pris longtemps ! Allez, vous ne m'avez pas dit ce que vous vouliez, donc j'ai pris du punch au riz, des sandwiches, et des bonbons aussi ! Un peu de tout !"


hi "C'est super. Bon, commençons."


"Misha prend une bouchée d'un petit sandwich triangulaire."

show misha hips_smile_ni
with charachange


mi "Donc, Hicchan, qu'est-ce que tu penses du festival ? C'est bien, n'est-ce pas ?"


hi "Ouais."

show shizu adjust_happy_close_ni
with charachange

shi "…"


mi "Il y a de belles étoiles ce soir. Ça n'aurait pas pu être un meilleur jour."

play music music_serene fadein 5.0
$ renpy.music.set_volume(0.1, 2.0, "ambient")

scene black
show bg misc_sky_ni at Fullpan(30.0)
with locationchange


"Le son des gens qui parlent en bas est comme une musique de fond à côté du chant des grillons."


"Je prends une gorgée de ma canette et regarde vers Misha, qui a l'air de dormir confortablement, allongée sur le dos avec une brique de jus de fruit à moitié pleine en équilibre sur son ventre."


"Shizune est assise avec ses jambes repliées, se balançant lentement comme un enfant impatient, pendant qu'elle regarde le ciel."


"Elles sont si mignonnes toutes les deux. Je regarde autour et vois plein d'étudiants tenant la main de leur petite amie ou petit ami."


"Pas trop loin de nous sur le toit, il y a des couples qui regardent vers les étoiles ou vers les lumières du festival, se tenant par la main."


"Une partie de moi a envie de ça."


"Regardant vers Shizune et Misha, je me demande si peut-être je devrais en inviter une à sortir un jour. Je me demande si ça vaudrait la peine de prendre le risque."


"Les aiguilles dorées se déplaçant sur le cadran de la montre du délicat poignet de Shizune attirent mon regard, et je remarque qu'il se fait plutôt tard. Mais les festivités battent toujours leur plein."


"Shizune est toujours en train de tenir par la patte le chat en peluche que j'ai gagné. Elle remarque que je le regarde."


shi "... ?"


"Avec désinvolture, elle me le tend. Je souris, voulant lui demander ce que je dois faire avec, mais elle ne pourrait pas me comprendre."


"Je secoue la tête et essaye de mon mieux de lui dire de le garder, espérant qu'elle comprendra."


"Alors que je regarde l'école, je peux voir tant de gens qui semblent tous heureux et joyeux."


"Les regarder m'apaise."


"C'est vraiment quelque chose. Cette journée valait vraiment la peine."


"Mais je n'arrive toujours pas à me détacher des sentiments de culpabilité et de mélancolie de tout à l'heure, ils restent accrochés à moi, et je ne peux pas les laisser partir."


"Shizune me fait des signes, et je ne peux pas la comprendre. Peu importe ce que je dis, elle ne pourra pas m'entendre."


hi "Je ne peux pas comprendre, Shizune."


hi "Bah, peu importe. Je me demande si on ne se considère pas tous les deux comme fautifs pour ça. Quoi qu'il en soit, je suis désolé de ne pas pouvoir comprendre."


hi "Tu sais, je suis presque, presque content que tu m'aies forcé à venir ici. Si je voulais sortir avec toi, cependant, je devrais y réfléchir à deux fois."


hi "Non, en fait... je suis content. C'était bien aujourd'hui."


hi "Tu serais plus mignonne si tu souriais plus, tu as un joli sourire."

stop music fadeout 5.0

show shizu behind_frustrated_close_ni at center
show bg misc_sky_ni at right
with charaenter


"Frustrée, elle se lève, les bras dans le dos, ayant l'air autoritaire et confiante devant le fond étoilé."

stop ambient fadeout 2.0

show shizu out_serious_close_ni
with charachange


"Tout à coup, Shizune tend ses bras en l'air, vers le ciel ouvert, semblant le tenir dans ses mains."


"C'est comme si elle me disait de regarder tout ce qui est en face de moi :"

show shizu epictransition
show cityscape zoom behind shizu
show hill enter behind shizu


"L'école, baignée de lumière avec le festival et les kimono colorés, le toit illuminé par les lucioles, le ciel si vaste qu'il impose le sentiment de crainte."


"Qu'est-ce qu'elle veut ? Ça se révèle doucement à moi. Cette magnifique scène devant moi est la preuve qu'il y a des choses suffisamment merveilleuses pour qu'il soit impardonnable de les gâcher à cause d'une mauvaise humeur."


"Et je peux sentir le poids de la personnalité de Shizune appuyer sur ce fait."


hi "Merci, je suppose."

hide shizu
show hill pairtouch at center
with charachange


"Je regarde au loin, mais Shizune m'attrape par l'épaule, sa montre me frôlant la joue."


"Avec sa main gauche, elle pointe le ciel."

play ambient sfx_fireworks fadein 1.0

show fireworks behind hill
with None
show fw_screen behind fireworks
with Dissolve(5.0)


"Avec de légers pop, des feux d'artifice commencent à éclater dans le ciel, chacun d'entre eux propageant une pluie de couleurs vives qui se fanent lentement dans l'obscurité."


"Je ne peux même pas me rappeler la dernière fois où j'ai vu des feux d'artifice, et encore moins des aussi grands. Sans mentionner qu'on dirait qu'ils sont tirés depuis l'école ; c'est presque impossible à croire."


"Les lumières dans le ciel se mêlent à une deuxième salve depuis la ville d'à côté, et elles semblent être faites de façon à se compléter comme deux parties d'un duo."


"Ça continue pendant presque quinze minutes, et puis ça s'arrête."


"Shizune réalise que sa main est toujours sur mon épaule et la retire avec soin, ayant l'air un peu embarrassée."

stop ambient fadeout 5.0
hide fireworks
hide fw_screen
show hill pairnotouch
with Dissolve(5.0)


"Retrouvant son calme, elle sourit, les mains sur les hanches et le torse bombé."


"C'est dans ces moments-là qu'elle a le plus l'air d'une adolescente normale. Énergique, heureuse et insouciante."


"Je mange avec Shizune, pensif, pendant que nous regardons tous les deux en silence la foule en bas s'amenuisant doucement."


"Elle est assise légèrement penchée en avant, le menton doucement appuyé sur ses mains, et un regard satisfait avec un soupçon de nostalgie sur le visage."


"Depuis tout ce temps, elle tient encore gentiment le chat en peluche par la patte."


"Je commence à me sentir fatigué et lui dis que je les verrai demain, Misha et elle, sans même réaliser qu'elle ne peut pas m'entendre, et je commence à retourner aux dortoirs."


"Je me sens réchauffé et en vie, même par cette nuit glaciale."

stop music fadeout 4.0


"L'image de Shizune se tenant avec force devant les étoiles, et de moi-même refusant de m'apitoyer sur mon sort, ne s'efface pas facilement de mon esprit."


"Si... s'il ne suffisait que d'un seul moment pour aimer quelqu'un, je crois que je pourrais tomber amoureux d'elle."


"Juste un peu."

window hide





label fr_A39:

show bg school_dormhallway at bgright
with None


"C'est un peu déroutant, et maintenant je commence moi-même à avoir des doutes."


"Est-ce que ça vaut la peine que j'y aille ?"


"J'ai un livre que j'ai l'intention de lire."


"Quelque chose à propos d'un système sous-terrain postal qui pourrait, ou pas, exister."


"C'est petit, aussi. Je pourrais le finir en une journée."


"Mais est-ce que ça serait une bonne façon d'utiliser mon temps ?"


"Eh bien, ouais. Ça fera l'affaire."


"Mais je suppose qu'il serait probablement mieux de mettre le nez dehors."


"Voir le festival."


"Essayer de faire les attractions avec les autres."


"Honnêtement, je devrais au moins faire une tentative pour garder l'attitude quelque peu sympathique que j'ai eue cette dernière semaine."


"Peut-être prendre quelque chose à manger, comme mon estomac le suggère."


"Il est presque midi... Je peux au moins prendre quelque chose dans un des stands dehors."

play music music_soothing fadein 1.0
play ambient sfx_crowd_outdoors fadein 1.0

scene bg school_courtyard
show crowd
with locationskip


"Je suis rapidement dehors, entouré par beaucoup d'étudiants et de gens qui sont peut-être leurs parents."


"De temps en temps j'aperçois quelqu'un qui vient clairement de la ville juste pour voir le festival."


"Ils sont faciles à différencier."


"C'est ceux qui n'arrêtent pas de fixer tout le monde, et derrière leurs regards on peut deviner qu'ils se disent “Bon, qu'est-ce qui ne va pas avec {b}celui-là{/b} ?”"


"J'ai presque envie de leur hurler dessus."


"Mais en même temps, est-ce que je peux nier avoir fait pareil toute la semaine ?"


"Une vague de quelque chose proche du dégoût passe en moi ; la culpabilité de ma propre étroitesse d'esprit."

"…"

$ renpy.music.set_volume(0.6,2.0, "ambient")

scene bg school_stalls1
with locationchange


"Je mets ces pensées de côté, me concentrant sur les affres de la faim qui brûlent mes boyaux comme une traînée de poudre."


"L'odeur de quelque chose de frit m'amène à la terre promise, où je peux manger."

stop music fadeout 0.6


"Je suis en train de commander, quand une voix m'interrompt."

show emi basic_annoyed at Slide(0.7,0.5,0.5,0.5,0.5)
with charaenter


emi "Hé, mais qu'est-ce que tu fais ?"

play music music_comedy fadein 0.5


hi "Je prends mon pe—euh, déjeuner."

show emi sad_annoyed at center
with charachange


emi "Petit déjeuner ?"

show emi sad_angry
with charachange


emi "Tu veux dire que tu viens juste de te lever ?"


hi "Euh..."


"Tout à coup j'ai l'impression que faire la grasse matinée est un crime."


hi "Non, je voulais dire déjeuner... vraiment."


"Elle ne me croit pas."


hi "Un pejeuner ?"

show emi basic_annoyed_close
with characlose


emi "C'est pas un petit déjeuner sain du tout !"


"Elle m'arrache la nourriture de la main et me fixe."


"Mais qu'est-ce qu'elle fait elle ?"


hi "Hé, c'est mon petit déjeuner !"

show emi sad_annoyed_close
with charachange


emi "Qu'est-ce qui est arrivé à ton déjeuner ?"


hi "C'est mon... peu importe, c'est ma nourriture !"


"Emi place ses mains sur les hanches et commence à me faire la leçon."

show emi basic_annoyed_close
with charachange


emi "T'as vraiment déjà oublié ton régime alimentaire ?"


emi "Tu as besoin d'être plus consciencieux au sujet de ta santé, Hisao !"

show emi sad_angry_close
with charachange


emi "Et ton cœur alors ?"


hi "Mon cœur est bien comme il est ! La plupart du temps."


"Tout ce que j'ai en réponse est un roulement d'yeux."

show emi basic_annoyed_close
with charachange


emi "J'en doute."

show emi basic_closedgrin_close
with charachange


emi "Tu ne serais pas ici si c'était le cas, hein ?"


"Elle n'a pas tort."


"Mais je ne suis pas près de m'avouer vaincu."


hi "Il est pas si mal que ça !"


hi "Il peut certainement endurer un peu de graisse de temps en temps !"


"Ouais, bien sûr. Et il supporte un peu de course, aussi."

show emi basic_annoyed_close
with charachange


"Emi ne semble pas convaincue."


"Pas étonnant, je n'ai même pas réussi à me convaincre moi-même."


emi "Peut-être, mais pas si tu dors toute la journée !"


"Un regard sournois traverse soudain son visage."

show emi basic_grin_close
with charachange


emi "Bien sûr, si tu avais suivi une routine depuis le début tu ne serais pas dans cette situation..."

stop music fadeout 6.0


hi "Hé, j'ai eu une semaine chargée, tu sais !"


hi "Par exemple, je suis presque mort ! Et j'ai rencontré plein de gens, et j'ai été sur le toit un moment..."

show emi sad_annoyed_close
with charachange


emi "Ce qui n'est pas une excuse pour se relâcher, tu sais."


emi "Une petite expérience de mort imminente n'est pas une excuse pour louper les exercices basiques."

show emi basic_closedgrin_close
with charachange


emi "Comme courir le matin."


"Elle hoche la tête, comme si quelque chose d'important avait été décidé."

show emi basic_happy_close
with charachange

play music music_emi fadein 0.5


emi "Donc c'est fixé, alors !"

show emi excited_proud_close
with charachange


emi "Tu as vu l'erreur que tu as faite et tu as décidé d'adhérer à ma routine, hein ?"


emi "Je te verrai de bonne humeur tous les matins ?"

show emi excited_happy_close
with charachange


emi "On sera partenaires de course ?"


hi "Tu sais, tu m'as déjà convaincu hier que c'était une bonne idée."


hi "Tu n'as pas besoin de me convaincre à nouveau."


"Même si je n'ai pas fait ce qui en découlait normalement."


"Elle a raison à propos de l'alimentation saine, après tout. Et ici je suis en train de commander quelque chose de vraiment pas sain."


"Mais délicieux !"


"Il y a des choses plus importantes que ce qui est délicieux, hein ?"


"Comme rester en vie ?"


"Si Emi n'était pas là pour m'empêcher de prendre les mauvaises décisions, je serais probablement..."


"Hé, attends une seconde."


"Une question me vient soudainement en tête."


hi "Hé, pourquoi est-ce que tu portes un tel intérêt à mon bien-être d'ailleurs ?"

show emi basic_closedgrin_close
with charachange


"Emi hausse les épaules et me fait un sourire."

show emi basic_grin_close
with charachange


emi "T'es le nouveau."


emi "J'ai remarqué que tu n'avais aucun ami encore, hein ?"

show emi sad_grin_close
with charachange


emi "En plus, je t'ai causé des problèmes toute la semaine, hein ?"


emi "Je te dois bien ça."

show emi basic_happy_close
with charachange


emi "Et j'ai dit à l'infirmier que je le ferais, de toute façon."


"Uh... huh. Une petite coureuse un peu folle veut que je sois en bonne santé."


"Bah, j'imagine qu'il y a pire destin."


hi "D'accord, ça m'a l'air... bien."


hi "Merci de te sentir concernée."


hi "Demain matin, alors ?"

stop music fadeout 1.0

hide emi
with charaexit


"Je pense que ça finit la conversation, donc je me tourne pour partir."


emi "Pas si vite !"

play music music_running

with vpunch


"Je sens une main agripper mon col et en une seconde je suis entraîné en arrière."


hi "Hé, pas besoin d'être si brutale !"


hi "Qu'est-ce que tu veux maintenant ?"

show emi sad_shy_close at center
with charaenter


"Emi a presque l'air blessée par mon ton ennuyé."


emi "J'ai pensé que tu voudrais peut-être de la compagnie."

show emi basic_annoyed_close
with charachange


"Ses yeux se plissent."


emi "D'ailleurs, t'as essayé de t'échapper juste pour aller chercher plus de cette merde frite, n'est-ce pas ?"


"Eh bien, ce n'était pas mon but, mais maintenant qu'elle le mentionne, ç'aurait été une très bonne idée."


hi "Bien sûr que non !"

show emi sad_annoyed_close
with charachange


"Un autre regard fixe."


hi "D'accord, peut-être que j'allais en prendre un peu..."


"Le regard continue."


hi "D'accord, beaucoup."


"Mon dieu, je suis un danger pour moi-même et pour les autres, c'est ça ?"


"Je suis d'accord sur le fait que j'ai besoin d'être en meilleure santé, et puis tout de suite après j'envisage le prochain mauvais réflexe que j'ai l'habitude d'avoir."

show emi basic_closedgrin_close
with charachange


emi "Je le savais ! On ne peut pas te faire confiance."

show emi basic_grin_close
with charachange


emi "Maintenant je dois définitivement rester collée à toi."


"La situation entière est ridicule."


"Je peux à peine imaginer ce que doivent se dire les passants qui voient une fille deux fois plus petite que moi me faire la morale."


"Peut-être que je devrais abandonner pour l'instant."


hi "Bien, fais ce que tu veux."


"Je soupire."


"Je peux aussi bien m'en tirer à bon compte."


hi "Qu'est-ce que t'as envie de faire ?"

show emi basic_confused_close
with charachange


"Emi réfléchit pendant une minute."


emi "Eh bien, j'ai promis à Rin que j'irais la voir à son mur..."

show emi basic_grin_close
with charachange


emi "Alors faisons ça !"


"J'avoue que je suis un peu curieux de voir comment son mur a tourné, donc encore une fois je pense qu'il y a pire destin."

$ renpy.music.set_volume(1.0,2.0, "ambient")

scene bg school_courtyard
show crowd
with locationchange


"Je fais un signe d'assentiment et me retrouve presque entraîné à travers la foule pendant qu'Emi court vers notre destination."

stop music fadeout 6.0
stop ambient fadeout 2.0

scene bg school_dormext_full at bgright
with locationchange


"Au moment où nous atteignons les dortoirs, je peux sentir mon cœur en train de s'affoler."


"Mon cœur ne devrait pas s'affoler après seulement ça."


"Je prends quelques respirations profondes, disposé à me calmer."


"Je suis l'une des personnes les plus normales de cette école, mais je dois quand même être ici."


"Parfois même je préfèrerais avoir perdu une main ou un truc du genre."


"Au moins il serait évident que je dois être ici."


"Mais à la place je n'ai même pas l'air malade."


"Même maintenant, essayant de reprendre mon souffle, j'ai juste l'air gêné."


"Emi se retourne et remarque mon état de détresse."

show emi basic_hes at Slide(0.4,0.5,0.5,0.5,0.5)
with charaenter


emi "Tu ne vas pas mourir devant moi, hein ?"

show emi basic_shock at center
with charachange


emi "Évite s'il te plaît !"

show emi sad_depressed
with charachange


emi "Ça serait complètement de ma faute, et je ne veux pas avoir affaire avec ce genre de culpabilité."


emi "D'ailleurs, après la dernière fois, je crois vraiment ne pas avoir besoin de revoir ça, spécialement parce que l'infirmier dirait que c'est tout de ma faute."

play music music_soothing fadein 8.0


hi "N... nan, je vais bien."


hi "Je crois que j'ai besoin de commencer à courir après tout."

show emi basic_closedgrin
with charachange


emi "Et tu voulais continuer de manger ton truc gras... quoi que ce soit."

show emi excited_proud
with charachange


emi "Tu vois ? C'est une bonne chose que je t'aie trouvé, hein ?"


"Oui, c'est sûr."


hi "Peut-être."

show emi basic_grin
with charachange


"Bien sûr, je n'ajoute pas que je ne serais pas dans cet état si elle ne m'avait pas fait traverser le festival comme ça."


"La conversation est interrompue par la soudaine apparition de Rin."

show rin basic_absent at Slide(1.0,0.5,1.0,1.0,1.0)

with Dissolve(1.0)


rin "Oh, c'est toi."

show rin basic_absent at tworight
show emi basic_grin at twoleft
show bg school_dormext_full at center
with charamove

show rin basic_awayabsent
with charachange


rin "Bonjour Emi."

show emi basic_closedhappy
with charachange


emi "Hey Rin ! J'ai amené Hisao avec moi parce qu'il allait se provoquer une crise cardiaque !"

show rin basic_absent
with charachange


hi "Pas du tout !"


"Mon objection passe inaperçue."

show emi basic_grin
with charachange


emi "On est passés voir ce qu'est devenu ton mur !"


"Rin hoche doucement la tête."

show rin basic_awayabsent
with charachange


rin "Eh bien, il est juste là."

show rin basic_deadpan
with charachange


rin "Tu peux le voir plutôt clairement."


"Je me demande combien de temps Rin a passé devant le mur."


"Est-ce qu'au moins quelqu'un s'est arrêté pour le regarder ?"


"On est les premiers ?"


"Évidemment, on n'est pas les premiers à le voir."


"Je veux dire, il est vraiment grand."


"Ça serait difficile de ne pas le voir."


"En même temps, je ne pense pas que quelqu'un en ait discuté avec Rin."


"Personne à part nous."


"Je me sens obligé de dire quelque chose."


hi "Je le trouve plutôt bien."

show rin negative_spaciness
with charachange


rin "Je suis toujours insatisfaite de la façon dont ça a tourné."


rin "Mais je suppose que ça ira."


"Elle semble presque résignée."


"Je ne suis pas sûr de ce qu'elle espérait comme résultat, mais je suppose qu'elle n'a pas dû y arriver."

scene bg mural at Fullpan(100.0, dir="left")
with Dissolve(2.0)


"Nous nous tenons en face de la peinture, la regardant toute entière."


"Je fais de mon mieux pour me concentrer sur la composition de la chose."


"C'est effectivement assez intéressant."


"Les couleurs fondent et se confondent, m'entraînant avec elles."


"Il y a une qualité onirique de la chose qui me donne presque envie de dormir."


"J'essaye de trouver certaines couleurs que j'ai apportées à Emi."


"J'ai beau chercher, je ne trouve pas le bleu de Prusse."


"Bah."


"Je suis sûr qu'il est là quelque part."

scene bg school_dormext_full
show rin basic_awayabsent at tworight
show emi basic_closedgrin at twoleft
with Dissolve(2.0)


"Mes pieds commencent à me faire mal, mais Rin ne semble pas encline à bouger."


"Emi commence à parler."

show emi basic_confused
with charachange


emi "Hé Rin, t'as mangé ?"

show rin basic_deadpan
with charachange


rin "Bien sûr. Je ne pourrais pas survivre sinon."

show emi basic_hes
with charachange


emi "Dans les cinq dernières heures ?"

show rin relaxed_nonchalant
with charachange


rin "Peut-être. Mais j'ai faim, donc peut-être pas."

show emi basic_closedgrin
with charachange


"Emi sourit et joint les mains."

show emi basic_grin
with charachange


emi "Bien ! Viens chercher à manger avec nous !"


"Rin hoche la tête en assentiment."

show rin basic_deadpannormal
with charachange


rin "D'accord, mais on doit se dépêcher avant qu'ils ne se rendent compte que je suis partie."


"Quelque part, je ne pense pas qu'ils s'en préoccupent."


"Qui que ce soit."

stop music fadeout 3.0
$ renpy.music.set_volume(0.6,0.0, "ambient")
play ambient sfx_crowd_outdoors fadein 1.0

scene bg school_stalls1 at Fullpan(8.0)
with locationskip


"Pendant que nous nous dirigeons vers les stands de nourriture, je jette un œil avide sur les aliments frits."


"Non, je ne devrais pas."


"Je suis sûr que Emi ne me laisserait pas faire de toute façon."

stop ambient fadeout 1.0

scene bg school_gardens
show emi basic_closedgrin at twoleft
show rin basic_awayabsent at tworight
with locationchange

play music music_ease fadein 9.0


"Nous trouvons un joli coin dans l'herbe et nous nous asseyons pour manger nos achats."


"Eh bien, mes achats, plutôt. Il s'avère que j'ai payé pour tout."


"Étonnamment, mon repas (non frit) est plutôt bon."


"Le silence tombe pendant qu'Emi et moi mangeons et que Rin regarde vers... un truc ou un autre, prenant occasionnellement une bouchée ou deux."


"Je finis mon repas le premier, et m'allonge sur le gazon."


"Emi lève les yeux de son repas."

show emi basic_confused
with charachange


emi "Fatigué, Hisao ?"


hi "Un peu, je crois."

show emi basic_annoyed
with charachange


emi "Eh bien, ne dors pas trop longtemps demain matin."

show emi excited_proud
with charachange


emi "On commence nos joggings matinaux, tu te rappelles ?"


"En fait, ça m'était sorti de la tête."


"Je ne faisais qu'apprécier le moment."


"Traîner dans le festival avec ces deux-là a effectivement été amusant."


hi "Ouais, je mettrai une alarme."

show emi basic_annoyed
with charachange


emi "T'as intérêt à être là !"

show emi basic_closedgrin
with charachange


emi "Je serais en colère si tu ne venais pas !"


hi "Dieu m'en préserve."

show rin basic_lucid
with charachange


rin "Je ne crois pas que dieu ait quelque chose à voir avec ça."

show rin basic_deadpan
with charachange


rin "À moins qu'il y ait un étrange accident et que ton alarme ne se mette pas en route."

show rin basic_deadpannormal
with charachange


rin "Ce qui pourrait être un acte de dieu."

show emi basic_grin
with charachange


emi "Alors ne fais rien qui puisse provoquer un acte de dieu, hein."


"Un plan se forme dans mon esprit."


"C'est un plan qui me fait me sentir un peu coupable, mais je vais le mettre à exécution quand même."


"Rah, j'ai gagné le droit d'avoir un peu de nourriture frite."


"Et de toute façon, je vais commencer à courir demain, hein ?"


"Donc la routine commencera vraiment demain alors, pas maintenant."


"Donc, le plan alimentaire commence demain aussi, donc je peux avoir un peu de malbouffe aujourd'hui."


"Une sorte de dernier adieu à tous ces trucs que j'avais l'habitude de manger avant de les abandonner brusquement avec l'hôpital."


hi "En fait, je pense que je devrais retourner à ma chambre."


hi "J'ai des devoirs à faire, et si je vais courir demain matin je dois me coucher tôt..."

show emi basic_annoyed
with charachange


"Encore ces yeux plissés."

show emi sad_annoyed
with charachange


emi "T'es sûr que tu ne vas pas juste te faufiler et acheter un peu de ces trucs frits là-bas ?"


hi "Nan, je suis trop plein pour ça maintenant."


"Je me tapote l'estomac pour l'emphase."


hi "De toute façon, vous me l'avez bien fait comprendre."

show emi basic_closedhappy
with charachange


"Emi rit. C'est un son étonnamment agréable."


"Une autre pique de culpabilité."


"Elle sait que je lui mens, c'est ça ?"


"Ou c'est juste qu'elle me fait confiance ?"


"J'ai l'impression d'être un monstre."

show emi excited_proud
with charachange


emi "Ça fait partie de mon plan, Hisao."

show emi basic_closedgrin
with charachange


emi "Bon, j'imagine que je te revois demain matin alors."

show emi basic_grin
with charachange


emi "Merci pour le repas ! Et pour nous avoir tenu compagnie !"


"Et là, j'ai su qu'elle me faisait une faveur."

show rin relaxed_surprised
with charachange


"Rin acquiesce en hochant la tête."


rin "Je ne dirai pas “À demain” parce que ça serait prédire le futur, et je suis sûre de ne pas pouvoir faire ça."

hi "…"


hi "D'accord."


hi "À plus, vous deux."


"Je suis plutôt content d'avoir décidé de quitter ma chambre aujourd'hui."


"Pas une mauvaise façon de commencer ma deuxième semaine ici, j'imagine."

stop music fadeout 9.0
play ambient sfx_crowd_outdoors fadein 1.0

scene bg school_stalls1
with locationchange


"Une fois que je serai sûr d'être sorti de la ligne de mire d'Emi, je ferai une ligne droite vers les stands de nourriture et achèterai un cake."


"Au moins c'est pas frit, hein ?"


"C'est moins pire que ce que je comptais faire."


"Je me sens un peu mal de mentir à Emi, cependant."


"Elle a vraiment l'air inquiète par ma santé."


"Je me rattraperai demain."


"Je ferais bien de me diriger vers ma chambre."


"Hé, j'ai {b}vraiment{/b} du travail à faire."

stop ambient fadeout 1.0

scene bg school_dormhisao
with locationskip


"Mon livre m'attend, et je m'affale sur le lit et lis pendant que les feux d'artifice illuminent le ciel."

$ renpy.music.set_volume(0.1,0.0, "ambient")
play ambient sfx_cicadas fadein 2.0

scene bg school_dormhisao_ni
with Dissolve(2.0)


"Finalement, toutes les balades (ou plus exactement, les courses) me sont dangereuses."


"Je ne suis vraiment pas en forme."


"Qu'Emi me force à courir tous les matins pourrait être une bonne chose après tout."


"C'est ce qu'on peut espérer."

stop ambient fadeout 2.0

window hide






label fr_A40:

play ambient sfx_crowd_outdoors fadein 0.3
play music music_soothing fadein 0.5

scene bg school_dormext_full
show crowd
with locationskip


"Le joyeux brouhaha de la foule m'accueille pendant que je passe par la porte principale et mets un pied dehors."


"Le terrain de l'école a été transformé en un immense festival entre hier et ce matin."


"Il y a des allées de stands colorés de l'entrée jusqu'au bâtiment principal."


"Certaines personnes transportent encore des trucs çà et là, mais derrière la plupart des comptoirs se trouvent des étudiants relaxés qui ont l'air d'être prêts."


"Beaucoup des étudiants se sont levés de bonne heure pour finir les préparatifs."


"Je ressens une once de culpabilité, mais elle disparaît vite."


"Je suis juste un étudiant récemment transféré, après tout."


"Certains visiteurs se baladent déjà sur le terrain."


"Il y a certaines familles avec des parents qui ont du mal à suivre leur progéniture trop enthousiaste..."


"...certains étudiants accompagnés de leurs parents..."


"...et beaucoup de gens qui sont là sans que je puisse savoir pourquoi."

play sound sfx_warningbell


"Les rafales du carillon et la voix de fausset du principal annoncent l'ouverture du festival via les haut-parleurs."


"Tout le monde applaudit poliment avec un peu d'enthousiasme."


"Le festival de l'école... on n'avait pas vraiment de festivals dans mon ancienne école. Ça fait un peu vieux jeu, surtout compte tenu de l'école d'où je viens, mais c'est quand même un peu excitant."


"Un jour de repos est agréable après cette première semaine de dur travail, malgré le fait que je sois resté allongé dans un lit d'hôpital pendant quatre mois avant ça."


"Je me rappelle même avoir souhaité pouvoir aller à des cours de maths durant mon séjour à l'hôpital."


"Je ne me souviens pas du programme du festival, même si Mutou l'a parcouru pendant la classe, l'autre jour."


"Je descends les marches du dortoir, avec l'intention de faire le tour de la cour pour voir tout ce qui est mis en place, mais je reste en bas des escaliers."

stop ambient fadeout 1.0

hide crowd
show rin relaxed_boredom at tworight
with Dissolve(2.0)


"Quelques personnes contemplent la peinture de Rin, tandis que l'artiste elle-même se prélasse sur le côté, appuyée contre le mur et ayant l'air extrêmement ennuyée."


hi "Bonjour."

show rin relaxed_surprised
with charachange


rin "Salut."


hi "Comment ça va ?"

show rin relaxed_nonchalant
with charachange


rin "Nulle part."


rin "Je suis coincée."


hi "Comment ça coincée ?"


rin "Je veux dire que je ne peux pas marcher. Je crois que mes jambes sont hors service à cause d'hier."


hi "Ça te fait mal ?"

show rin relaxed_sleepy
with charachange


rin "Dur à dire. Peut-être."


"L'étendue du travail qu'elle a fait était plus importante qu'elle ne me l'a laissé savoir. Je pensais qu'elle avait juste un peu les muscles fatigués ou un truc du genre. Je veux poser une question, mais Rin change rapidement de sujet."

show rin basic_awayabsent
with charachange


rin "Les amis du prof sont passés."

show rin basic_absent
with charachange


rin "Et ils sont allés en ville pour déjeuner et m'ont demandé d'aller avec eux. Heureusement que mes jambes me faisaient aussi mal."


hi "Mais t'es bloquée, assise ici ? C'est dommage."

show rin basic_lucid
with charachange


rin "Je vais juste attendre jusqu'à ce que je puisse remarcher à nouveau. Ça va arriver tôt ou tard, quand on y pense."


rin "Le prof était content que j'aie fini le mur."


hi "Il peut l'être."

show rin basic_awayabsent
with charachange

stop music fadeout 5.0


rin "Mais je me demande s'il est fini après tout."


hi "Oh ?"

show rin basic_deadpanupset
with charachange


rin "Je croyais hier que j'avais tout fini, mais maintenant je n'en suis plus aussi sûre. Je devrais peindre plein de détails. Peut-être. Probablement. C'est très dur de décider."


"Finie ou non, la peinture murale est vraiment bien au grand jour."

play music music_another fadein 2.0

scene bg mural at Transform(xalign=0.05)
with Dissolve(2.0)


"Diverses parties du corps humain, répétées encore et encore dans une extravagante mutation, pour la plupart déformées, en sont les éléments principaux."


"Ça a l'air anarchique, comme si c'était inconsidérément disposé et rudimentairement peint, mais beaucoup de réflexion et de soin ont été consacrés à chacune d'entre elles."

show bg mural at Transform(xalign=0.25)
with charamove


hi "C'est une grenouille qui sort de la tête de celui-là ?"


rin "C'est un poisson rouge."

show bg mural at Transform(xalign=0.45)
with charamove


hi "C'est quoi ça ?"


rin "Ce n'est rien."

show bg mural at Slide(0.45,0.45,.6,0.6,25.0, time_warp=acdc_warp)
with None


"Bref..."


"Le mur est si long que je dois tourner la tête de chaque côté pour voir la peinture entière."


"C'est dur de considérer ça comme une seule œuvre. Les éléments ne semblent pas s'emboîter, mais j'imagine qu'ils créent une sorte de tout."


"Abstrait comme c'est, je n'ai aucune idée de ce que c'est supposé représenter, mais c'est très joli. C'est suffisant pour moi."


"Je m'installe à côté de Rin, contre le mur comme elle."


"Les bruits joyeux du festival deviennent de plus en plus forts au fur et à mesure que les gens arrivent."


"Les dortoirs sont loin des attractions du bâtiment principal et des stands dans la cour, donc la plupart des visiteurs ne sont pas encore venus jusqu'ici."

show rin negative_spaciness_close at offscreenright
with None

show rin negative_spaciness_close at tworight
show bg mural at Transform(xalign=0.6)
with MoveTransition(3.0, factory=MoveFactory(time_warp=_ease_time_warp))


"Une expression quelque peu ennuyée s'installe sur le visage de Rin, lui donnant l'air d'être détachée de tout ce qui se passe autour d'elle."


"Elle est vraiment silencieuse. Je me demande si elle a mal quelque part."


hi "Donc ils ont dit quoi les autres artistes à propos de ton mur ?"

show rin basic_deadpannormal_close at tworight
with Dissolve(1.5)


"Ma question réveille Rin de sa torpeur. Elle tourne paresseusement la tête vers moi."

show rin basic_deadpan_close
with charachange


rin "Je sais pas trop."

show rin basic_awayabsent_close
with charachange


rin "Je crois qu'ils l'ont aimé ? Peut-être."


hi "Et toi alors ? T'es contente de comment il est ? Parce que j'ai un peu participé, ça serait terrible si tu n'en étais pas contente."


"Rin incline la tête, se mordant la lèvre inférieure."

show rin negative_sad_close
with charachange


rin "Je crois que c'est plutôt satisfaisant. Ce n'est pas mauvais mais pas bon non plus. C'est juste... ça. Je crois que ça me va d'être plutôt incertaine là-dessus."


hi "Je peux demander quelque chose d'autre ? Qu'est-ce que ça représente vraiment ? J'y ai pensé hier, quand tu as dit que ça ne représentait rien de particulier."


hi "Mais c'est un peu illogique, nan ? Tu ne peux pas faire quelque chose venant de nulle part, pas même de l'art."

show rin negative_annoyed_close
with charachange


"Rin fronce les sourcils et penche la tête en arrière pour regarder les nuages."


rin "Je sais pas. Je ne suis pas vraiment bonne pour expliquer les choses. C'est juste une peinture murale ; y a rien de spécial à ça. Je l'ai déjà dit."


"Elle a l'air ennuyée par mes questions."


rin "Je ne savais pas ce que je peindrais, donc j'ai juste décidé de faire une peinture murale."


rin "C'est une peinture murale qui représente une peinture murale."

show rin basic_deadpancontemplation_close
with charachange


rin "Non, attends. Je viens de trouver une meilleure façon de le dire : Elle se représente elle-même."

show rin basic_deadpannormal_close
with charachange


rin "Donc... c'est aussi peinture muralesque que ça peut l'être, du moins autant que je peux le faire, donc si tu crois que ça a une signification, je crois que c'est la même que celle-là."


"Ça ne veut rien dire."


"Signification... Je sens le coin de mes lèvres s'étirer dans un sourire qui est juste un peu tordu."

stop music fadeout 5.0

scene mural all
with flash


"Je n'ai jamais compris l'art dans le sens profond de la chose."


"Je comprends la base, comment l'art est seulement supposé être un moyen pour échanger des idées et des pensées."

scene bg mural at Slide(1.0,1.0,0.6,0.6,40.0, time_warp=acdc_warp)
with flash


"Cependant, je n'ai jamais appris comment je dois interpréter une œuvre d'art, la chose divine que l'artiste a l'intention de dire à travers elle."


"Je sais que ce n'est pas un talent spécial, mais de toute façon, mon cerveau ne peut pas connecter l'art avec ce que je vois. Tout ce que je vois est une peinture murale."


"Je peux admirer l'aspect technique, après tout même moi je peux voir la différence entre une mauvaise œuvre et une bonne."


"Mais je ne peux pas faire plus que ça, donc ne me demande pas de trucs sur les significations, Rin."


"Sa réponse me rend réticent à continuer de poser des questions."


hi "Donc qu'est-ce que tu vas faire quand tu pourras te relever ?"

play music music_happiness fadein 4.0

scene bg mural at Transform(xalign=0.6)
show rin negative_spaciness_close at tworight
with flash


rin "Rien."


hi "Rien ? Mais c'est le festival, t'as pas envie d'aller t'amuser ?"

show rin basic_absent_close
with charachange


rin "Je suis bien comme ça."


hi "Tu ne socialises pas beaucoup, hein ?"


"Je crois que je demande plus pour elle que pour moi à ce moment. C'est pas comme si j'étais particulièrement excité à propos du festival non plus ; juste un peu curieux de voir de quoi ça a l'air, et c'est tout."


"Sa réponse n'est pas surprenante."

show rin basic_awayabsent_close
with charachange


rin "Non, pas trop."


hi "Je crois... que moi non plus, en fait."

show rin basic_deadpan_close
with charachange


rin "Tu devrais y aller si t'en as envie."


hi "Je sais, mais je peux te tenir compagnie. Je ne suis pas encore habitué à tout ça, donc ça me va si je reste au calme."


hi "Je peux partir cependant, si tu veux être seule."

show rin basic_deadpannormal_close
with charachange


rin "J'aime bien quand t'es là."


"On tourne autour du pot avec des mots, mais on finit par s'accorder finalement. Ses paroles me font me sentir étrangement heureux, donc je reste."


"Sa présence est quelque chose que j'aime aussi. Cette étrange aura de sérénité qui semble émaner d'elle rend le silence confortable. J'apprécie vraiment ça."


"Nous regardons les gens passer, tous les deux silencieux, pendant que tous les autres parlent joyeusement entre eux."


"Les étudiants dirigent leurs familles vers les dortoirs pour montrer leurs chambres. Ils passent devant nous et devant le mur, en lançant un regard ou deux."


"Je leur porte moins d'attention, et plus à ma camarade, essayant de tracer mon chemin à travers son visage illisible et énigmatique."

show rin basic_awayabsent_close
with charachange

show rin basic_absent_close
with charachange

show rin basic_awayabsent_close
with charachange


"Les yeux de Rin s'agitent d'une personne à une autre alors qu'ils passent."


"Est-ce qu'elle s'attend à ce que les gens s'arrêtent devant le mur, peut-être espérant secrètement que quelqu'un fasse un commentaire ?"


"Je ne crois pas que qui que ce soit puisse présumer que c'est elle l'artiste. On est juste assis là comme deux vagabonds après tout, et elle n'a même pas de mains."


"Je me demande si c'est le genre de Rin de vouloir des compliments. Elle semble tellement à l'écart."


"Plus de gens passent, certains d'entre eux pointent la peinture du doigt, échangeant des paroles que je ne distingue pas. Quelqu'un fait tomber une boule de glace sur sa chaussure. Dommage pour lui."



hi "Tout le monde semble l'apprécier."


"Je suggère ça hasardeusement, jetant un sujet dans l'air vicié qui nous sépare."


"Rin ne répond pas tout de suite, mais maintenant je suis habitué à la lenteur avec laquelle elle parle. C'est comme si elle prenait grand soin de choisir ses mots, ce qui est dur à croire quand on considère le fouillis de mots qu'elle sort."

show rin basic_lucid_close
with charachange


rin "Je voulais faire ça pour que les gens puissent le regarder sans penser. Puis j'ai réalisé que ça n'avait aucun sens. Donc c'est devenu un mélange de ceci et de cela."

show rin negative_spaciness_close
with charachange


rin "De loin, on dirait que quelqu'un a vomi un troupeau de papillons sur le mur. Ce qui est exactement ce que cette odieuse présidente ne voulait pas. C'est ce mot-là ?"


hi "Quel mot ?"

show rin basic_deadpannormal_close
with charachange


rin "Ça. C'est quoi le mot pour plus d'un papillon ?"


hi "Des papillons ?"

show rin basic_deadpanupset_close
with charachange


rin "Non, comme un troupeau, ou une école, ou un tas."


hi "Oh. Je sais pas. Un essaim peut-être ?"


rin "Peut-être que les gens aiment le vomi de papillon."

show rin negative_confused_close
with charachange


"Rin regarde son mur, ayant l'air étonnamment mécontente."


rin "Le milieu pourrait être mieux."

show rin negative_annoyed_close
with charachange


rin "D'habitude j'aime les intermédiaires, mais là, ça m'a fait mal aux fesses. Pas littéralement, bien sûr... et puis j'ai eu ça. Je suppose que c'était littéral après tout."


hi "Ne sois pas aussi critique avec toi-même."

show rin basic_deadpannormal_close
with charachange


"Elle me regarde d'un air amusé, mais ne dit rien."

scene bg school_dormext_full at bgright
with locationchange


"À ce moment je commence à me demander si je ne devrais pas vraiment partir et faire quelque chose de plus constructif de mon dimanche."


"C'est le summum de l'échec social. Une journée entière de libre, un festival juste derrière ma porte, et qu'est-ce que je fais ?"


"Je reste assis ici avec Rin ; deux spectateurs avec rien à faire sauf penser à quel point il est dommage de n'être qu'un spectateur."


"Même en réalisant à quel point c'est dommage, je ne fais rien. Je ne me lève pas pour partir passer une journée agréable."

stop music fadeout 5.0

play sound sfx_rustling


centered "*gigote gigote*"

"…"


centered "*tortille*"

play sound sfx_rustling


centered "*gigote*"

"…"

scene bg mural at Transform(xalign=0.6)
show rin negative_annoyed_close at tworight
with locationchange


"Rin est agitée, balançant constamment une jambe par dessus l'autre et recommençant."


"Elle a l'air vraiment irritée."


hi "Quelque chose ne va pas ?"

show rin basic_deadpanupset_close
with charachange


rin "Oui. Non. Oui."

scene bg school_dormext_full at bgright
show rin basic_deadpanupset:
    xpos 0.7 ypos 1.0 xanchor 0.5 yanchor 0.8
    easein 0.5 yanchor 1.0
with locationchange


"Elle bondit soudainement sur ses pieds. C'est surprenant, je croyais qu'elle en était toujours incapable, mais apparemment ce n'est pas le cas."

show rin negative_confused at tworight
with charachange


rin "Je dois trouver Emi ou quelqu'un, j'ai besoin d'aide pour quelque chose."


hi "Je peux t'aider."

show rin relaxed_nonchalant
with charachange


rin "Non, ça va. L'un d'entre nous doit rester au cas où quelque chose arrive."


hi "Ne sois pas ridicule. Rien d'intéressant n'est arrivé depuis que je suis là, sauf un gars qui a fait tomber sa boule de glace sur son pied. Laisse-moi t'aider, je m'ennuie."


hi "Donc qu'est-ce qu'il y a ?"

show rin negative_annoyed
with charachange


"Les lèvres de Rin s'aplatissent l'une contre l'autre pour former une ligne presque parfaitement horizontale."

show rin basic_lucid
with charachange


"Elle ferme les yeux et prend une profonde respiration."


"Quand elle rouvre les paupières et laisse apparaître ses yeux noirs d'un aspect terriblement sérieux, ça me prend au dépourvu."

play music music_rin fadein 0.5

show rin negative_angry
with charachange


rin "Hisao, tu pourrais ne pas vouloir entendre ça ou peut-être que si, je ne sais pas, mais ça ne compte pas et même si c'est le cas tu ne me laisses pas le choix."


rin "J'ai mes règles et j'ai besoin de l'aide de quelqu'un. Cependant, je ne crois pas que notre relation soit arrivée au niveau où je peux t'autoriser à retirer mes sous-vêtements dans les toilettes des filles, même si tu me le proposais."


rin "C'est pourquoi tu devrais rester ici pendant que je vais chercher Emi."


"Pendant que le sang me monte aux joues, mon cerveau essaye désespérément de trouver une réponse. Mais en fait c'est la chose la plus cohérente que j'ai entendue de la part de Rin depuis les quatre jours où je la connais."


hi "Oui."

hide rin
with charaexit

stop music fadeout 4.0


"Ne voulant pas croiser Rin du regard, je tourne la tête, prétendant regarder les parents de quelqu'un."


"Du coin de l'œil je vois Rin tourner les talons pour s'en aller sans plus tarder."


"J'ai envie d'aller me cacher six pieds sous terre."


"Je me demande combien de temps Rin va partir... ou si elle va revenir."

scene bg mural at Transform(xalign=0.6)
with shorttimeskip

play music music_dreamy fadein 3.0


"Elle revient finalement, apparaissant de nulle part, et elle se rassied là où elle était, à côté de moi."

show rin basic_deadpannormal_close at Slide(0.8,0.5,0.7,0.5,1.0)
with Dissolve(1.0)


rin "Je suis revenue."


"Elle dit ça calmement, comme si mon erreur n'avait jamais été faite. Je préfère oublier toute la chose, donc je reste silencieux."

scene bg mural_ss at Transform(xalign=0.6)
show rin basic_deadpannormal_close_ss at tworight
show rin_shadow basic behind rin:
    xpos 0.7 ypos 1.0 xanchor 0.5 yanchor 0.85
    easein 3.0 xpos 0.8 yanchor 0.9
with Dissolve(3.0)


"Le temps passe en statu quo, le soleil brille juste au-dessus du bâtiment principal. Il me frappe directement dans les yeux, mais je me contente de les plisser au lieu de bouger."


"En peu de temps, il devient douloureux de garder les yeux ne serait-ce qu'un peu ouverts, et mes tempes commencent à me faire mal."


hi "J'ai mal à la tête. Je crois que cette journée m'a donné une migraine, tu peux le croire ?"

show rin basic_deadpan_close_ss
with charachange


rin "T'as faim ?"


hi "Quel rapport avec le mal de tête ?"

show rin basic_deadpansurprised_close_ss
with charachange


rin "Y en n'a pas. Je demande parce que j'ai faim."

"…"


"Sa gravité face à la situation mélange mon irritation et son ridicule, et je me retrouve encore une fois avec le coin des lèvres qui s'étire."


hi "Tu sais quoi ? Moi aussi."


hi "Je vais aller nous chercher à manger. Qu'est-ce que tu veux ? C'est moi qui paye."

show rin basic_lucid_close_ss
with charachange


rin "Peu importe."

show rin basic_deadpannormal_close_ss
with shorttimeskip


"Revenant avec à manger, je donne une portion à Rin, prenant l'autre pour moi, et on commence à manger sans un mot."

show rin negative_spaciness_close_ss
show rin_shadow negative at Transform(xpos=0.8,ypos=1.0,xanchor=0.5,yanchor=0.9)
with charachange


"Rin regarde vers le ciel, la fourchette suspendue au bout de ses lèvres."


rin "Que sont les nuages ? J'ai toujours pensé qu'ils étaient les pensées du ciel ou quelque chose comme ça. Parce que tu peux pas les toucher."


hi "Tu pensais ça quand t'étais enfant ?"


rin "Non, la semaine dernière."


rin "Peut-être parce que parfois mes pensées sont comme des nuages. Brumeuses, blanches et lentes."


rin "Comme si le ciel était dans mon esprit. Comme si mon esprit était le ciel."


hi "Le ciel de ton esprit ?"


rin "Ferme les yeux et pense au ciel. Tu ne seras pas capable de penser à autre chose jusqu'au moment où tu arrêteras."

scene black
with shuteye


"J'essaye. Ça marche. Magique ?"

scene bg mural_ss at Transform(xalign=0.6)
show rin basic_deadpannormal_close_ss at tworight
show rin_shadow basic behind rin at Transform(xpos=0.8,ypos=1.0,xanchor=0.5,yanchor=0.9)
with openeye


"Ouvrant les yeux, je vois Rin m'étudier du regard. Ça me met mal à l'aise parce qu'elle ne dit rien. Je me tourne."

scene bg misc_sky_ss at Fullpan(20.0)
with locationchange


hi "Les nuages sont de l'eau. De l'eau évaporée."


hi "Tu sais, ils disent que presque toute l'eau du monde sera, à un certain moment de son existence, une partie d'un nuage."


hi "Chaque larme ou goutte de sang ou de sueur qui sort de toi, sera un nuage. Toute l'eau de ton corps aussi, elle s'en va après ton décès. Ça peut prendre un certain temps cependant."


rin "Ton explication est meilleure que n'importe laquelle des miennes."


hi "Parce qu'elle est vraie."


rin "Ça doit être pour ça."


"Je me remets à manger avant que ça devienne froid."


"Le mur offre un peu d'ombre divine pendant que le soleil frappe depuis le dôme qu'est le ciel."


"Mais l'après-midi laisse déjà lentement place au soir donc notre déjeuner devient plus un dîner. Ou quel que soit le mot pour un repas décalé comme ça."


"Malgré la façon dont je décide de l'appeler, il est là au bon moment. Je n'avais pas mangé depuis genre super longtemps."

"…"


"Mon appétit étant calmé, je laisse échapper un soupir satisfait. Rin n'a pas tout mangé mais semble en avoir fini avec son repas aussi."


"Je me penche en arrière, m'imprégnant de l'atmosphère. La foule s'est déjà amincie, mais les activités sont toujours en cours. Tout le monde semble s'amuser."


"C'est normal après tout. Il fait bon, le genre de parfait jour d'été où il fait chaud mais pas trop."


"Le soleil va bientôt se coucher. Le temps est vraiment passé vite."

scene bg mural_ss at Transform(xalign=0.6)
show rin basic_deadpannormal_close_ss at tworight
show rin_shadow basic behind rin at Transform(xpos=0.8,ypos=1.0,xanchor=0.5,yanchor=0.9)
with locationchange


hi "On est assis là depuis six heures."

show rin basic_deadpansurprised_close_ss
with charachange


rin "C'est pas faux."

show rin basic_deadpancontemplation_close_ss
with charachange


rin "Tu veux faire quelque chose d'autre maintenant ?"


hi "Non, pas vraiment."

show rin basic_deadpannormal_close_ss
with charachange


rin "Moi non plus."

show rin basic_lucid_close_ss
with charachange


"Elle ajuste sa position et s'adosse contre le mur, et je suis son exemple, me relaxant."


"Pendant quelques minutes, on est assis là, sans dire un mot."


"J'essaye de ressentir l'humeur de Rin à son attitude, la tension de ses muscles, les petites expressions fugaces sur son visage. C'est en vain. Elle est illisible, comme toujours."

$ renpy.music.set_volume(0.5, 0.0, "ambient")
play music sfx_crowd_outdoors channel 6 fadein 1.0

scene bg school_dormext_full_ss
show crowd_ss
with locationchange


"La foule gonfle çà et là, les gens bavardent joyeusement entre eux. Très peu de gens prêtent attention au mur, et encore moins à nous."


"Je joue avec quelques cailloux distraitement."


"L'acte de faire quelque chose juste pour le principe de faire quelque chose, le summum de la paresse."


"Centimètre par centimètre, le soleil se glisse de plus en plus bas, changeant la couleur du ciel proche de l'horizon de jaune doré à orange et à rouge au moment où le coucher est proche."


"J'ai l'impression que mon estomac est rempli de plomb après avoir mangé si lourdement, mais le mur de briques est étonnamment agréable contre mon dos."


"J'essaye de lutter contre la somnolence qui m'écrase, mais en vain."

scene black
with shuteye

stop music fadeout 4.0
$ renpy.music.stop(channel=6,fadeout=2.0)

with Pause(4)
$ renpy.music.set_volume(1.0, 0.2, "ambient")
play ambient sfx_fireworks fadein 1.0

scene bg misc_sky_ni
with openeye


"Je me réveille en sursaut."


"Un léger boum rebondit à travers le terrain de l'école. Des étincelles lumineuses clignotent dans mon champ de vision comme des étoiles."


"Quelque chose monte vers le ciel en direction du terrain de sport."


"Une traînée de feu le suit jusqu'à ce qu'une explosion de flammes rouges et jaunes éclairent le ciel au-dessus de l'école avec un gros boum."

show fireworks
with dissolve


"Feux d'artifice."


"L'éclair de lumière soudain sur la toile du ciel étoilé me permet de me rendre compte qu'il fait déjà nuit."


"J'ai dormi pendant combien de temps ? Je me sens faible et je ne peux pas sentir mon bras droit."


"Alors que j'essaye de le bouger, je réalise pourquoi."

play music music_twinkle fadein 1.0

show rin basic_lucid_close_ni:
    xpos 1.0 ypos 1.1 xanchor 0.5 yanchor 1.0
    easein 1.0 xpos 0.9
with Dissolve(1.0)


"Rin est lourdement appuyée contre mon épaule, près de tomber sur mes genoux."


"Elle dort profondément, même pas dérangée par les feux d'artifice."


"Sa bouche est légèrement entrouverte et ses yeux sont fermés avec quiétude. Le visage d'un enfant qui dort du sommeil de l'innocence."


"Je secoue gentiment Rin avec mon bras libre, essayant de la réveiller, ou, à défaut, la bouger pour que mon autre bras soit libéré de son écrasement."


"Rin réagit aux secousses en plissant fort les yeux, comme pour résister au réveil."

show rin basic_deadpanupset_close_ni at Transform(xpos=0.9, xanchor=0.5, ypos=1.1)
with charachange


"Elle ouvre progressivement les yeux, mais les garde à demi-fermés, laissant la lumière des feux d'artifice s'immiscer dans ses yeux verts qui reflètent les éclairs lumineux des explosions, puis me regarde et fronce les sourcils."

show rin basic_deadpan_close_ni
with charachange


rin "Juste un peu plus longtemps, d'accord ?"


"La voix de Rin est somnolente et ralentie, laissant ses mots presque inintelligibles suspendus paresseusement dans l'air."


"On dirait qu'elle n'est pas tout à fait consciente de la situation."

show rin basic_lucid_close_ni
with charachange


"La tête de Rin retombe sur mon épaule, et elle se penche sur moi de tout son poids."


"Elle se blottit contre moi, essayant de trouver une position agréable, mais me met très mal à l'aise en même temps."


"Je deviens intensément, presque douloureusement conscient du corps chaud de Rin, et du léger soulèvement de sa poitrine contre mon bras, sa respiration revenant rapidement au même rythme."


"Je ne peux pas m'empêcher d'admirer son don pour dormir, ou la facilité qu'a son esprit d'utiliser quelqu'un qu'elle connaît depuis moins d'une semaine comme oreiller."


"Les fusées s'élèvent une à la fois dans le ciel, explosant en fleurs rouges, vertes et dorées, accompagnées par les ooh et les aah du public."


"J'essaye de me sortir de la tête la proximité déconcertante de Rin, qu'est-ce que je peux y faire après tout ? J'espère juste que son 'un peu plus longtemps' n'est vraiment que ça."


"Un par un, les éclats scintillants naissent et meurent en un clin d'œil, colorant le ciel sombre de la nuit dans une constante peinture abstraite."


"J'écoute les légers boums des explosions et la respiration calme de Rin, essayant de sortir de la torpeur de mon réveil."


"Heureusement, juste un peu a vraiment duré juste un peu, puisque Rin remue dans son sommeil et se réveille à nouveau avant que les feux d'artifice soient finis."

show rin relaxed_sleepy_close_ni
with charachange


rin "Je me suis endormie."

show rin basic_awayabsent_close_ni
with charachange

show rin basic_lucid_close_ni
with charachange

show rin basic_awayabsent_close_ni
with charachange


"Elle ouvre finalement complètement les yeux et les cligne plusieurs fois."


hi "Tu t'es endormie sur moi. Deux fois."

show rin basic_absent_close_ni
with charachange


rin "Tu n'as pas aimé ça ?"


hi "Euh..., eh bien..."

show rin basic_absent_close_ni:
    ease 1.0 ypos 1.0


"Malgré le bégaiement peu concluant, Rin se redresse, se décalant de moi."


hi "Ben, t'es lourde."


"C'est un mensonge, elle ne pèse presque rien, mais je dois me venger, même si c'est en dessous de la ceinture. Ma moquerie ne parvient pas à provoquer une réaction chez Rin dont l'attention s'est tournée vers le ciel, aux lueurs des feux d'artifice."

show rin negative_spaciness_close_ni at Transform(xpos=0.9, xanchor=0.5)
with charachange


"Elle semble hypnotisée par le jeu de couleurs des explosions."


"Une sensation de picotement me parcourt le bras pendant que le sang recommence à circuler. C'est désagréable, mais ça m'aide à me débarrasser de mon état de torpeur."


"De plus en plus de fusées s'envolent vers le ciel, les couleurs vives de leurs explosions sont réfléchies par les nuages."


"Nous regardons tous les deux fixement les feux d'artifice à travers la canopée des arbres, captivés par le spectacle."


"Nous aurions une meilleure vue du ciel si nous bougions de quelques mètres, mais aucun de nous deux ne le suggère."

show rin negative_worried_close_ni
with charachange


rin "J'aime vraiment les feux d'artifice, même si les regarder me rend un peu triste, je crois. C'est comme s'ils voulaient tellement que tu voies à quel point ils sont bruyants et brillants, mais quand quelqu'un regarde, ils sont déjà partis."

show rin negative_sad_close_ni
with charachange


rin "C'est comme s'ils n'étaient même pas réels."

"…"


hi "Ils sont réels, je peux te le dire."


hi "Tout ça est... réel, tu sais ?"


hi "Quand tu y penses, rien ne dure vraiment longtemps. Même quelque chose comme ma vie ou la tienne dure juste le temps d'un clignement d'œil dans l'histoire du monde, comme l'une de ces fusées. Pouf, et on est partis."


hi "Mais on est là, n'est-ce pas ?"


"Ouais, c'est la réalité. Rin, assise à côté de moi, les explosions bruyantes des feux d'artifice, le vaste ciel illimité. Ces choses sont définitivement réelles, même si elles ne le seront pas éternellement."


"Je me sens chaud à l'intérieur, et je me demande si c'est parce que Rin est si proche de moi ou si c'est le sentiment d'être en vie."

show rin negative_spaciness_close_ni
with charachange


rin "Je ne sais pas vraiment ce que je devrais dire après ça."


hi "C'est pas grave... peut-être que je ne parlais qu'à moi-même."


hi "Mais tu sais, les feux d'artifice sont beaux... mais en fait, n'est-ce pas quelque chose d'idiot de dépenser autant d'argent dans une seconde de belles étincelles ?"

show rin negative_sad_close_ni at Slide(0.9,0.5,0.7,0.5,1.0)
with None

show rin relaxed_doubt_close_ni at Slide(0.9,0.5,0.7,0.5,1.0)
with Dissolve(1.0)


"Rin détache son regard du spectacle en cours et se penche en arrière, me regardant avec un visage renfrogné."


rin "Woaw, je ne me serais jamais attendue à ce que tu sois aussi cynique."


hi "Cynique est une appellation plutôt barbare. Au lieu de ça, je me considère comme un réaliste."

show rin relaxed_surprised_close_ni at tworight
with charachange


rin "Réalistes n'est pas la façon dont les cyniques s'appellent eux-mêmes ?"

stop ambient fadeout 1.0
hide fireworks
with dissolve


"La fusée finale explose dans un bang d'argent et de bleu, laissant le terrain étrangement silencieux pendant un moment jusqu'à ce que la foule commence à se diriger vers l'entrée comme un troupeau de bovins."


"La fumée grise des feux se dirige vers les dortoirs depuis le terrain de sport. La piquante odeur de poudre qu'elle transporte se colle à mes vêtements et à mes cheveux."


hi "C'est tout ?"

show rin negative_spaciness_close_ni
with charachange


rin "Je crois bien."

scene bg school_dormext_full_ni
with locationchange


"Je me relève et m'étire. Dormir contre un mur de briques n'était pas une si bonne idée après tout."

show rin negative_spaciness_ni:
    xpos 0.7 ypos 1.0 xanchor 0.5 yanchor 0.8
    easein 1.0 yanchor 1.0
with Dissolve(1.0)

show rin basic_absent_ni at tworight
with charachange


"Rin se lève aussi et se tourne vers moi, avec une lueur d'attente dans son regard fatigué."


"Même si elle semble avoir du mal à fixer son regard, elle me regarde directement, quelque chose qui ne s'est pas vraiment produit durant cette semaine."


hi "Hum... donc..."


"Je réalise soudainement qu'on était presque en rendez-vous là, même par accident. Même si on n'a rien fait."


"Mais ce n'était pas... alors pourquoi est-ce que mon sang se précipite dans mes joues et que je balbutie ?"


"Je ne sais pas ce que je devrais dire, d'autant plus qu'il semble que Rin attende que je dise quelque chose, mais heureusement, elle résout le problème pour moi."

show rin basic_deadpannormal_ni
with charachange


rin "Bonne nuit, Hisao."

hide rin
with charaexit


"Elle me regarde encore pendant un moment, me fixant de la tête aux pieds, tourne les talons et s'en va, disparaissant dans la foule."

stop music fadeout 7.0

"…"


hi "D'accord... Bonne nuit."


"Je reste là, donnant ma réponse à l'air froid de la nuit."


"Soupir."


"Le festival s'est avéré n'être rien de ce à quoi je m'attendais."


"J'ai fini par passer toute la journée à un seul endroit avec Rin, même si aucun de nous ne l'avait proposé ou n'a suggéré qu'on fasse autre chose."


"Je n'avais juste rien de mieux à faire et évidemment, elle non plus."


"La chaleur de Rin s'attarde sur moi pendant encore un petit moment, avant de disparaître dans la nuit tombante."

window hide





label fr_A41b:


scene bg school_gardens
with shorttimeskip

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_crowd_outdoors fadein 0.5
play music music_soothing fadein 0.5


"Après avoir acheté une assiette de takoyaki dans un stand appartenant à une classe voisine de la nôtre, je m'assieds dans les jardins de l'école et regarde les gens passer en grignotant mon repas plutôt fade."


"Je ne devrais pas me plaindre. C'est mieux que rien et c'est pas cher."


"Alors que je regarde en direction de l'école, je me rends compte que regarder les gens aller et venir est étonnamment divertissant pour passer le temps en mangeant."

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

show bg school_courtyard
show crowd
with locationchange


"Des enfants accompagnés par leurs parents ou grands-parents trottinent vers le centre de l'évènement, une main tenant celle d'un parent et une gourmandise surdimensionnée dans l'autre."


"Je ne peux pas m'empêcher de remarquer que la tranche d'âge ici est plutôt élevée, quelque chose que j'avais déjà remarqué en allant marcher en ville."



"Ça doit être une de ces villes où les seuls gens restants sont ceux qui y ont vécu toute leur vie et qui refusent catégoriquement de partir, et ceux qui veulent passer leurs vieux jours dans un endroit calme."


"J'imagine que c'est aussi une façon d'expliquer pourquoi la culture de Yamaku semble aussi conservatrice."

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

scene bg school_gardens at Fullpan(8.0)
with locationchange


"Non pas que ça me gêne. J'apprécie le calme de Yamaku et de ses environs."


"La chaleur, cependant, c'est autre chose. Être assis au même endroit pendant si longtemps a fini par me faire penser au fait qu'il fait désagréablement humide, maintenant que le plus chaud moment de la journée est là."


"Je ferais mieux de bouger si-{w=.5}{nw}"

play sound sfx_warningbell


"Gah !"


"Le son des cloches du carillon me prend complètement par surprise et je me lève, une réaction partagée par quelques personnes non loin de moi."


"Le système de sonorisation crachotte après la fin de la cacophonie des cloches. Le principal annonce d'une voix presque inintelligible l'ouverture du festival qui est déjà en plein essor."


"Il est plutôt amusant de comparer les sourires enjoués des plus vieux avec l'alternative peinée et douloureuse des grimaces des plus jeunes. Les étudiants, de l'autre côté, semblent y porter peu attention."


"Néanmoins, avec l'annonce qui finit, tous à l'unisson et poliment — si ce n'est pas avec trop d'enthousiasme — applaudissent, et puis tout redevient comme avant."


"Glissant une main dans ma poche pour avoir l'air le plus relaxé possible, je jette négligemment un regard autour de moi pour trouver quelque chose à faire."


"...C'est un peu difficile de voir au loin avec tous ces gens autour."


"Je décide de me rabattre sur une technique essayée et approuvée : aller là où tous les autres se rendent. Et tout de suite, c'est la cour d'école et ses environs."

play sound sfx_can_clatter


"Lançant l'assiette vide dans une poubelle, je fais mon chemin vers le bâtiment de l'école."

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene bg school_courtyard
show crowd
with locationchange


"Le nombre de stands autour du périmètre du bâtiment de l'école me surprend. Un bon nombre de classes doivent avoir opté pour des stands multiples."


"En décidant lequel faire en premier, j'aperçois une bannière familière avec une bordure à motifs bleus et du texte rouge."


"Le stand de Lilly est un bon endroit pour commencer. Je suis curieux de savoir comment ça a tourné, après tout le travail que sa classe et elle ont fourni."

$ renpy.music.set_volume(0.5, 2.0, channel="ambient")

scene bg school_stalls2 at Fullpan(8.0, dir="left")
with locationchange


"En arrivant, je commence à comprendre pourquoi la classe a mis si longtemps à tout organiser."


"Facilement deux fois plus large que la plupart des autres stands et jonché d'équipements pour cuisiner éparpillés partout, c'est plus proche d'un restaurant en plein air que d'un évènement de festival."


"Pendant qu'un étudiant devant moi prend un bol de nouilles et s'en va, je marche vers le comptoir."


"La fille derrière semble plutôt exaspérée, et me demande d'attendre un moment avant de disparaître sous le comptoir."


"Je profite du moment pour jeter un œil autour."


"De la vapeur semble s'élever de partout, et des casseroles fument sur les tables. La plupart des étudiants aveugles s'occupent du déballage des ingrédients en étant aidés par quelqu'un qui est probablement le professeur de la 3-2."


"Il ne faut pas longtemps pour que je remarque Lilly parmi eux, parlant avec le professeur pendant qu'elle compte rapidement des boîtes et paquets avec ses doigts."


"D'après son expression et le fait que le professeur et elle semblent tous deux être dans un état de légère confusion, il semble qu'il y ait un problème de coordination."


"Avant que je puisse regarder plus longtemps, la fille derrière le comptoir apparaît à nouveau, seulement pour se retourner et demander où est la caisse de rechange."


"Lilly s'arrête un moment avant que la fille et elle échangent leur place et que le professeur s'en aille rapidement ailleurs."

stop music fadeout 2.0

show bg school_stalls2 at left
show lilly basic_smileclosed at center
with charaenter


li "Désolée pour cela, nous avons quelques problèmes. Que puis-je pour vous ?"


"Il me faut une seconde pour me rappeler pourquoi je suis venu. Mes yeux se tournent rapidement sur le côté pour lire le menu sur le comptoir."


hi "Oh, euh, pourquoi pas... une soupe miso ?"

show lilly basic_surprised
with charachange


li "Ah, serait-ce Hisao ?"


hi "Yep. On dirait que t'es pas mal occupée."

play music music_ease fadein 6.0

show lilly basic_weaksmile
with charachange


"Son visage le confirme au fur et à mesure qu'elle abandonne son masque de serveuse."


li "Quelque part dans la chaîne, notre commande s'est mélangée. On essaye de réparer ça, mais on dirait qu'on a juste la moitié de ce dont nous avons besoin."


hi "Vous ne devriez pas servir des plus petites portions pour pallier à ce problème ?"

show lilly basic_sad
with charachange


li "Il semble que c'est ce qu'on devrait faire, bien que je ne préfèrerais pas. Le fait qu'une bonne moitié de notre classe soit partie n'aide pas, non plus."


"Je regarde derrière elle pour voir combien de gens sont en train de travailler dans le stand."


"Ça ne dépasse pas les huit personnes."


hi "J'imagine que c'est pour ça que le professeur est parti ?"

show lilly basic_weaksmile
with charachange


li "C'est exact. Elle est partie pour essayer de ramener quelques autres de nos camarades de classe pour aider."


"Entendant des bruits de pas derrière moi, je lance furtivement un regard en arrière pour voir un couple de personnes âgées prendre place dans la queue. Je suppose que je ferais mieux d'arrêter de discuter."


hi "Voilà l'argent pour la soupe."

show lilly basic_smile
with charachange


li "Soupe... oh, oui, elle arrive."


"Lilly se tourne et demande un bol de soupe miso pendant que je tends la monnaie."

show lilly basic_reminisce
with charachange


"Prenant les pièces dans sa paume, je ne peux pas m'empêcher de remarquer avec quelle efficacité elle compte l'argent avec ses longs doigts pâles. Satisfaite que j'aie remis le montant exact, elle le met dans un petit plateau métallique."

show lilly basic_smileclosed
with charachange


"Il ne faut pas longtemps avant que la soupe soit faite et placée doucement dans ses mains, après quoi elle se retourne et me la passe."


hi "Merci. Je reviendrai pour rendre le bol."

show lilly basic_smile
with charachange


li "Merci, Hisao. Oh, autre chose. Tu as vu Hanako ?"


hi "Hanako... non, pas aujourd'hui. Pourquoi ?"

show lilly basic_sad
with charachange


"Elle soupire, visiblement déçue."


li "Ce n'est pas grave. Je me demandais juste ce qu'elle faisait pour le festival."

show lilly basic_weaksmile
with charachange


li "Tu reviendras quand tu auras fini, alors ?"


hi "Bien sûr. Je te ferai signe si je vois Hanako, aussi."


li "Je te remercie, Hisao."

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene bg school_courtyard
show crowd
with locationchange


"Je m'éloigne du stand et cherche une place pour m'asseoir, tenant soigneusement mon bol en bois fumant des deux mains."


"Par rapport aux boulettes d'avant, c'est très bon. Un peu tiède comparé à ce que ça devrait probablement être, peut-être, mais la saveur est suffisante pour couvrir ça raisonnablement bien."


"Pendant que je bois, je ne peux pas m'empêcher de ressentir un peu de culpabilité de ne pas m'être impliqué dans le festival comme les autres."


"Je ne peux pas y faire grand-chose, considérant que je suis arrivé dans l'école il n'y a qu'une semaine, mais ça me pèse toujours."


"Ça, et le fait que quelques étudiants ne semblent pas profiter du festival autant que les visiteurs."


"Finalement je finis mon bol et pars en direction du stand, pour le rendre."


"Considérant qu'il ne semble pas y avoir de queue du tout, je prends mon temps pour marcher."

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

scene bg school_stalls2
with locationchange


"Il semble que la mission du professeur ait porté ses fruits : il y a maintenant plus d'une douzaine d'étudiants en train d'aider, et une grande partie du déballage des cartons a été faite."


"Bien que la plupart d'entre eux aient l'air plutôt détendus pendant qu'ils travaillent, Lilly semble toujours quelque peu stressée."





label fr_A41a:


stop music fadeout 4.0


"...Bien. Je sais ce que je dois faire. Même si c'est juste pour une personne, je vais rendre le festival plus agréable pour elle."


"Alors que je pose le bol sur le comptoir, j'appelle Lilly."

show lilly basic_smile at center
with charaenter


li "Ah, Hisao. Tu l'as ramené ?"


hi "Ouais, ici."

hide lilly
with charaexit


"Je le glisse dans ses mains, et elle le donne à quelqu'un qui est apparemment chargé du nettoyage. Considérant que c'est quelqu'un que je n'ai pas vu avant, c'est probablement une pénalité pour son retard."


hi "Hé, Lilly ?"

show lilly basic_smileclosed at center
with charaenter


"Elle lève la tête et revient au comptoir en entendant ma voix, réalisant que je suis encore là."


hi "Tu veux venir voir le reste du festival ?"

play music music_another fadein 0.5

show lilly basic_pout
with charachange


"Elle gonfle les joues avec un air désapprobateur. C'est plutôt mignon, mais en complète contradiction avec sa nature habituellement réservée."


"Il me faut quelques secondes pour que je comprenne ce qu'elle met en cause. Oups."


hi "Ah... euh, je ne voulais pas dire..."

show lilly basic_giggle
with charachange


"Lilly rit doucement, montrant sa taquinerie pour ce qu'elle est."


li "Tu n'es toujours pas habitué à l'école, hein ?"


"Elle m'a eu."

show lilly basic_reminisce
with charachange


li "Toujours est-il que... j'ai besoin de rester au stand. Il a fallu jusqu'à maintenant pour que tout soit déballé."


"Je suppose que sa réticence ne devrait pas trop me surprendre, compte tenu de la quantité de travail qu'elle a fourni dans ce projet."


hi "Tout semble fonctionner très bien maintenant, cela dit. D'ailleurs, tu as des gens en plus pour aider maintenant."

show lilly basic_surprised
with charachange


"Un garçon qui est au milieu de la préparation de nouilles soba se tourne vers nous, souriant."


"Étudiant" "Vas-y Lils, tu as mérité une pause. On peut tenir le fort, pour l'instant."

show lilly basic_displeased
with charachange


li "Si tu dis que c'est bon, alors je suppose que ça va..."

show lilly basic_reminisce
with charachange


li "Mais, si vous avez besoin d'aide-"


"Étudiant" "Alors on t'appellera. Vas-y, on s'en sortira."

hide lilly
with charaexit


"Lilly arrête finalement de résister alors qu'il remue une spatule dans sa direction. Elle fait le tour le stand, et prend sa canne en chemin."


"Je suppose que la première chose qu'on devrait faire est chercher Hanako. Lilly semble s'inquiéter pour elle, et je doute qu'elle soit le genre de personne à profiter de la foule comme ça, toute seule."


hi "Bon, je suppose qu'on devrait chercher Hanako. On va où en premier ?"

show lilly cane_reminisce at center
with charaenter

li "Hmm…"


"Nous restons tous les deux silencieux un moment pour réfléchir."


hi "Peut-être qu'elle est dans sa chambre ?"


li "J'en doute. Elle ne garde pas grand-chose dedans, donc elle n'aurait rien à faire."

show lilly cane_satisfied
with charachange


li "...Ah ! La bibliothèque ?"


"Un bon endroit pour chercher une lectrice avide, je suppose."


hi "La bibliothèque donc. Allons vérifier en premier."

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")

scene bg school_lobby
with locationskip


"Mis à part les bruits de la foule à l'extérieur, l'intérieur de l'école semble presque désert."


"Afin de s'assurer que tout le monde ait assez de place, je suppose que tous les évènements ont été organisés pour être à l'extérieur, sur les terrains de l'école. Ils sont vraiment très grands, par rapport aux normes de tout autre école."

show lilly cane_smileclosed at center
with charaenter


li "C'est tranquille et silencieux ici, n'est-ce pas ?"


hi "Ouais. Bien mieux que toute l'agitation extérieur."

stop ambient fadeout 3.0

scene bg school_staircase2
with locationchange


"Nous prenons notre temps et marchons doucement à travers le premier étage de l'école, atteignant finalement l'escalier du deuxième étage."

scene bg school_hallway2
show lilly cane_smileclosed
with locationchange


"Je ne peux pas m'empêcher de remarquer que Lilly anticipe toutes les portes et obstacles, sa canne restant fixe et sa main touchant constamment sur le mur du couloir."


hi "Tu connais vraiment bien l'école, hein ?"

show lilly cane_smile at center
with charaenter


"Elle sourit et hoche la tête."


li "Je suis ici depuis quelques années déjà, donc je sais où tout se trouve."

show lilly cane_sad
with charachange


li "Le dortoir me joue toujours des tours parfois. Je n'y suis pas depuis longtemps, et il n'est pas aussi bien aménagé que le bâtiment principal."


li "Si je me souviens bien, c'était un bâtiment inutilisé avant d'être rénové et de devenir un dortoir."


"Ça explique pourquoi le dortoir des garçons et celui des filles ont l'air différents de l'extérieur, et pourquoi leurs pièces semblent un peu bizarres pour des chambres à coucher."


"Je croyais qu'elle vivait dans les dortoirs depuis qu'elle était arrivée dans l'école, mais maintenant je me rappelle ce qu'elle a dit hier."


"Elle a dû emménager au milieu de sa scolarité. Pas étonnant qu'elle ne soit pas si familière avec les lieux."


hi "C'est vrai, tu m'en avais déjà parlé."


hi "Je suppose que la plupart des étudiants ici vivent dans les dortoirs dès qu'ils arrivent. Un grand nombre d'entre eux en ont l'air, en tout cas."

show lilly cane_reminisce
with charachange


"L'expression de Lilly devient un peu difficile à lire, mes questions touchant à l'évidence un point délicat."


li "Eh bien... Comment pourrais-je dire..."

show lilly cane_weaksmile
with charachange


li "Tout le monde... a ses raisons."


"Quelque chose me dit que l'une de ces personnes avec des “raisons” est Hanako, d'où son hésitation face à la réponse. Ma propre situation est encore un autre cas."


"Je suppose que c'est un choix que tout le monde ici doit avoir fait de lui-même... ou, pour mon cas, qui a été fait pour lui."


hi "J'y peux rien, je suppose. Au moins Yamaku en soi semble être un endroit agréable."

show lilly cane_smile
with charachange


li "C'est bon de t'entendre dire ça. Je pensais que tu en étais venu à la détester."


hi "Et toi, alors ?"

show lilly cane_surprised
with charachange


"Mon retournement de question prend Lilly par surprise."


li "Je suis ici depuis longtemps, alors..."


hi "Ce n'est pas ça. Tu semblais pas mal déprimée à propos d'Akira."

show lilly cane_smileclosed
with charachange

li "Hmm~"


hi "Quoi ?"

show lilly cane_smile
with charachange


li "Akira est prise. Désolée, Hisao."


"Lilly ne verra jamais avec quelle rapidité la paume de ma main a atteint mon visage à cause de son accusation sournoise."


hi "Hé, je m'inquiète pour toi. Ce n'est pas une façon de répondre à ça."

show lilly cane_cheerful
with charachange


"Pendant qu'elle affiche un sourire amusé, nous arrivons à l'angle d'un couloir et entrons dans la bibliothèque."

scene ev hana_library_read_std
with locationskip


"Cela fait, il n'est pas dur de repérer Hanako, considérant que la pièce est complètement vide d'autre présence humaine."

scene bg school_library
with locationchange


"Étant donné qu'il n'y a pas de personnel, je suppose qu'il n'y a pas besoin de tenir compte des règles de la bibliothèque. Je l'appelle à haute voix."


hi "Hé, Hanako."

show lilly cane_surprised at center
with charaenter


li "Hanako est là ?"


"Pendant qu'elle cherche d'où viennent nos voix, Hanako sort la tête de derrière son livre, probablement le même que celui qu'elle lisait vendredi."

show lilly cane_surprised at twoleft
show bg school_library at bgleft
with charamove
show lilly cane_smile at twoleft
show hanako basic_normal at tworight
with charaenter


ha "Hisao... Lilly ?"


hi "On a pensé qu'on pourrait passer. Lilly a réussi à s'échapper du stand de nouilles, avec un peu d'aide."

show lilly cane_pout
with charachange


li "Ce n'était pas vraiment s'échapper.."

show hanako emb_downsmile
show lilly cane_surprised
with charachange


"Hanako laisse échapper un petit rire, nous surprenant tous les deux."

show hanako basic_bashful
with charachange


ha "Je croyais juste que... Lilly pourrait ne pas apprécier le festival."


hi "Eh bien, maintenant on peut en profiter ensemble, hein ?"

show lilly cane_smileclosed
with charachange


"Elles hochent toutes deux la tête avant qu'on sorte de la bibliothèque pour nous diriger vers les festivités."

stop music fadeout 2.0

scene bg school_stalls1_ni
with shorttimeskip

$ renpy.music.set_volume(0.5,0.0, "ambient")

play ambient sfx_cicadas fadein 0.3


"Je donne quelques pièces à la fille derrière le comptoir, et prends deux gobelets de thé. J'essaye d'accentuer ma salutation en me penchant un peu plus pour compenser le fait qu'elle est de toute évidence sourde."


"Maintenant que j'y pense, j'aurais probablement dû demander de l'aide au lieu de les laisser toutes les deux dans le jardin pendant que j'achetais les boissons."


"Essayer de jongler avec deux tasses de thé chaud (pour elles) et une canette de café (pour moi, d'un distributeur) n'est pas très facile."


"Avec quelques manœuvres prudentes, je réussis à tout garder stable et vertical pendant que je marche vers le banc où Lilly et Hanako sont assises et bavardent."

scene bg school_gardens2_ni
show lilly basic_smileclosed_ni at twoleft
show hanako basic_distant_ni at tworight
with locationchange


"C'est un endroit vraiment agréable. Uniquement éclairé par la lune, il est un peu éloigné des évènements principaux."


"Comparé à la chaleur qu'il a fait pendant la journée, cet endroit est agréablement frais maintenant."


"Pas que ça importe tant que ça. La plupart des visiteurs sont partis vers les zones qui sont soit plus proches des feux d'artifice, ou plus hautes sur la colline pour voir le spectacle."

show lilly basic_smile_ni
with charachange


li "Oh, tu es revenu, Hisao."

show hanako basic_normal_ni
with charachange


"Ses oreilles sont bonnes. Je ne suis même pas à proximité et Hanako ne m'avait pas remarqué."


hi "Voilà. Désolé, c'est du thé instantané, mais c'est tout ce qu'il leur restait."


"Hanako prend délicatement sa tasse de la main droite, et je place doucement l'autre dans les mains tendues de Lilly."

show hanako basic_smile_ni
show lilly basic_smileclosed_ni
with charachange


li "Tu as apprécié le festival alors, Hisao ?"


hi "Ouais, c'est plutôt fun."


"Une réponse honnête. La nourriture n'était en général pas super, mais je me suis bien amusé en fin de compte, spécialement avec Hanako et Lilly."


"En fait, je crois qu'elles ont encore plus apprécié que moi. Avec Lilly et moi à côté, Hanako a réussi à être suffisamment à l'aise pour pouvoir apprécier le festival."

stop ambient fadeout 1.0

$ renpy.music.set_volume(1.0,0.0, "ambient")

play ambient sfx_fireworks
play music music_twinkle fadein 12.0

scene bg misc_sky_ni
show fireworks
with dissolve


"Pendant qu'on est assis à boire, les sifflements des premiers feux d'artifice se font entendre avant qu'ils explosent dans une douche vibrante de bleu dans le ciel de la nuit, annonçant le début de la fin pour le festival."


"Des cris enthousiastes peuvent être entendus dans la foule dispersée sur le terrain de l'école pour célébrer ça."


"Pendant quelques minutes sur la fin, Hanako et moi regardons les feux d'artifice alors que Lilly écoute béatement avec les yeux fermés."


"Rouge, vert, jaune, en forme d'étoile, de rond ou autre, toutes les formes et toutes les couleurs remplissent l'air, une après l'autre, et dansent dans le ciel."


"Aucun endroit près d'où j'ai vécu n'a jamais eu d'exhibition aussi grandiose. Les festivals comme ça sont une chose qui appartient au passé, dans une zone aussi métropolitaine."


"Voir un tel spectacle avec elles deux... c'est probablement le moment le plus agréable que j'ai eu depuis longtemps."

scene bg school_gardens2_ni
show lilly basic_weaksmile_ni at twoleft
show hanako basic_distant_ni at tworight
show fireshine
with charachange


li "Donc... voilà. Le festival est finalement terminé."


hi "Ouais."


"Elle laisse échapper un délicat soupir."

show lilly basic_concerned_ni
with charachange


li "Autant je pourrais me plaindre à propos de tout ce qu'on a dû faire, mais je suis toujours triste de constater que je serai diplômée avant le prochain festival de Yamaku."

show lilly basic_concerned_close_ni
with characlose


"Je m'avance et me tiens à côté de Lilly, posant doucement une main sur son épaule."


hi "T'inquiète pas. On a toujours Tanabata plus tard dans l'année, hein ?"

show lilly basic_smile_close_ni
with charachange


li "Tu as raison. Ça serait bien d'y aller quand ça arrivera."


"Plusieurs minutes passent en silence, avec seulement les explosions des feux d'artifice se faisant entendre."


"Les voir toutes les deux me rappelle le conseil que m'avait donné Lilly quand on avait été en ville ensemble."


"“Chérir l'opportunité de se faire de nouveaux amis”, hein ?"


hi "Dis, Lilly ?"

show lilly basic_smileclosed_close_ni
with charachange


"Elle tourne légèrement la tête vers moi pour me montrer qu'elle écoute, le regard d'Hanako est encore fixé sur les explosions d'artifice multicolores."


hi "Ça te gêne si je vous rejoins de temps en temps toutes les deux pour boire le thé ?"


"Le sourire sur son visage est plus que suffisant pour voir sa réponse."

show lilly behind_cheerful_close_ni
with charachange


li "Ça serait un plaisir, Hisao."

stop music fadeout 2.0
stop ambient fadeout 2.0
window hide




label fr_A42:





scene bg school_stalls2
with None

show lilly basic_reminisce at center
with charaenter


"Lilly ne semble pas rassurée du tout, et je ne peux pas l'en blâmer."


"En plus de ses problèmes avec son stand, elle semble toujours s'inquiéter pour Hanako."


"Je ne peux pas vraiment l'aider avec sa classe, donc je suppose que la seule façon de lui venir en aide est d'essayer de la rassurer pour notre amie timide en commun."


"Plaçant le bol sur le comptoir, j'appelle Lilly."


hi "Hé, Lilly, ne t'inquiète pas pour Hanako, je vais la trouver et rester avec elle, d'accord ?"

show lilly basic_weaksmile
with charachange


"Je peux voir l'apaisement de Lilly clairement écrit sur son visage."


li "Merci Hisao. Et si tu vois les élèves de ma classe, tu peux leur dire de revenir ici s'il te plaît ?"


hi "Je le ferai. Amuse-toi bien. Et assure-toi de prendre une pause, hein ?"

show lilly basic_smile
with charachange


li "Je le ferai si je le peux. À plus tard, Hisao."

stop music fadeout 10.0
$ renpy.music.set_volume(1.0,1.0, "ambient")

scene bg school_courtyard
show crowd
with locationchange


"Je laisse Lilly à son stand et pars à la recherche d'Hanako."


"D'une certaine manière, je me sens mal de la laisser avec toute cette foule, mais même si elle était clairement sous pression, je ne peux pas m'empêcher de penser que ça lui plaisait."

stop ambient fadeout 0.5

scene bg school_hallway2
show crowd
with locationskip

play ambient sfx_crowd_indoors fadein 0.5


"Les halls sont remplis de gens se baladant au festival."


"S'il y a une chose que je sais à propos d'Hanako, c'est qu'elle ne s'approcherait pas de foules comme ça."


"Et avec les étudiants montrant leurs amis et leur chambre à leur famille, je doute qu'elle soit là aussi."


"Suivant une intuition aveugle, je vais à l'encontre de la foule."


"Heureusement, cette foule semble être moins festive que dans un festival normal ; j'imagine que c'est par considération pour le corps étudiant."

stop ambient fadeout 5.0


"Pendant que je me fraye un chemin à travers la masse, il ne faut pas longtemps pour que je me retrouve dans un endroit vide de monde."

hide crowd
with Dissolve(2.0)


"Ce n'est pas surprenant, vu que je suis devant la bibliothèque."


"Même les plus ardents étudiants n'ont pas pris la peine de montrer cette section de l'école."

play music music_happiness fadein 2.0
scene bg school_library
with locationchange


"Pendant que j'entre dans la bibliothèque, le vacarme du festival se transforme en bruit de fond, et bientôt je me retrouve dans la zone de lecture à l'arrière de la salle."


"Derrière l'un des bureaux, je vois le haut d'une tête, avec des longs cheveux noirs."


hi "Salut Hanako. Je me doutais que j'allais te trouver ici..."

show hanako def_shock:
    xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 0.9
    easein 0.5 yanchor 1.0
with charaenter


"Elle sursaute un peu avec le choc, avant de me regarder lentement par-dessus le bureau."


ha "H-Hisao ?"


hi "Yep. Lilly est plutôt occupée, alors elle m'a envoyé te trouver."

show hanako basic_normal at center
with charachange


ha "O-oh. Tu veux t'asseoir ?"


hi "En fait, j'ai un peu faim. Tu veux qu'on aille chercher quelque chose à l'un des stands ?"

show hanako defarms_worry
with charachange


ha "Um... Je... j'ai amené à manger alors..."


"J'aurais dû m'en douter, mais j'aurais essayé. Espérer d'elle qu'elle sorte aujourd'hui était peut-être un peu trop."


hi "Que dirais-tu d'aller manger dans la salle de thé ? Je suis passé devant en venant ici, et il n'y avait personne aux alentours."


hi "On peut toujours manger ici, mais ça serait un peu moins confortable. Qu'est-ce que t'en dis ?"

show hanako cover_distant
with charachange


ha "D-d'accord. Allons-y."

show hanako basic_distant
with charachange


"Hanako ferme son livre et le pose d'une manière délicate."


hi "On y va ?"

show hanako basic_normal
with charachange


ha "O... oui."

stop music fadeout 2.0

scene bg school_hallway2
with locationchange


"Nous marchons côte à côte depuis la bibliothèque jusqu'au salon de thé."


"Comme prévu, il n'y a quasiment personne ici."


"S'il n'y avait pas ces murmures à travers les murs, il serait impossible de dire qu'il y a un énorme festival à l'extérieur."

show hanako emb_downtimid at tworight
with charaenter


"Hanako porte son sac avec ses deux mains et fixe le sol devant elle."

show hanako emb_downsmile
with charaenter

show hanako emb_downtimid
with charaenter


"De temps en temps, elle semble briser son rythme et marche en faisant de plus petits pas."


"La première fois que c'est arrivé, je n'y ai pas prêté attention, mais je remarque vite qu'elle le fait régulièrement."


hi "Ça va ?"

show hanako defarms_worry
with charachange


"Elle s'arrête net."


ha "Q-quoi ?"


hi "Je sais pas... on dirait que tu étais en train de trébucher ou un truc comme ça..."

play music music_another fadein 0.5

show hanako emb_blushing
with charachange


"Ses joues se teintent de rose alors que son regard se reconcentre sur le sol."

show hanako emb_downtimid
with charachange


ha "C'est... ce n'est rien."


hi "Tu sais, quand tu dis “rien” comme ça, les gens ont envie de continuer à poser des questions."


"Pendant une seconde, j'ai cru qu'elle n'allait pas répondre."


"Prêt à repartir, je recommence presque à marcher, quand..."

show hanako emb_emb
with charachange


ha "C'est un... un jeu."


hi "Un jeu ?"

show hanako emb_downsmile
with charachange


ha "Tu... vois le sol là ?"


"Quelle question bizarre. Le sol ressemble à celui de n'importe quel autre étage ; couvert de planches faites avec des carrés de linoléum."


"Rien de spécial."


hi "Ben, oui. Et donc ?"

show hanako emb_downtimid
with charachange


ha "Des fois... quand il n'y a personne... je ne marche que sur les planches foncées..."


"La voix d'Hanako s'affaisse au fur et à mesure que son explication continue, jusqu'au stade où je peux à peine entendre sa voix dans le silence hurlant de la salle vide."


hi "Les plus foncées ?"


"Remuant les pieds, Hanako pointe du bout de sa chaussure une latte qui est à peine plus foncée que les autres."

show hanako emb_downsmile
with charachange


ha "C-comme celles-là."


hi "Oh, d'accord, donc celles-là ne sont pas bonnes ?"


"Je pointe une planche à proximité."

show hanako emb_emb
with charachange


ha "O-oui. Quelque chose... quelque chose comme ça."


hi "Oh, je vois. Tu joues souvent à ce jeu ?"

show hanako emb_downsad
with charachange


"Hanako secoue la tête."


hi "Juste quand le couloir est vide ?"

show hanako emb_emb
with charachange


"Elle hoche la tête."


hi "Bon eh bien, inutile de s'arrêter, je commence à avoir vraiment faim."

show hanako emb_smile
with charachange


"Elle hoche la tête encore une fois, cette fois avec un peu plus d'enthousiasme."


hi "Bien, allons-y."

hide hanako
with charaexit

stop music fadeout 5.0


"Nous arrivons au bout du couloir, et cette fois je remarque qu'Hanako porte un peu moins d'attention au sol."


"Je me demande ; à quel point est-ce qu'il faut se sentir seul pour jouer à un jeu comme ça ?"


"Mais, avant que je réalise ce que je suis en train de faire, je me surprends à essayer de viser chaque pas pour marcher sur les bonnes planches."

play music music_dreamy fadein 2.0

scene bg school_miyagi
with locationchange


"Le bruit du festival est un peu plus fort dans la salle de thé, mais avec la brise qui vient de la fenêtre, ça en vaut la peine."


"Sans réfléchir, je marche jusqu'à la fenêtre et respire profondément. J'oublie parfois à quel point l'air est pur ici comparé à chez moi."

show hanako basic_bashful at center
with charaenter


ha "Je... te sers du thé ?"


hi "Je veux bien, merci."

hide hanako
with charaexit


"Il me semble que c'est la première fois que je suis seul avec Hanako sans qu'elle veuille être ailleurs."


"Me tournant, je la regarde faire un simple pot de thé et organiser quelques sandwichs sur un plat."


"Je l'ai vue faire ça plusieurs fois auparavant, mais cette fois semble légèrement différente."



"C'est comme si elle était...{w} calme."


"Finalement, elle place le petit plateau sur la table et remplit les tasses de thé."


"Le parfum frais du thé infusé est mêlé à la brise, et pendant une seconde je me sens comme si j'étais seul au monde."


hi "Je crois que maintenant je sais pourquoi tu aimes cet endroit."

show hanako defarms_worry at center
with charaenter


ha "Um... Je ne comprends pas ce que tu veux dire."


hi "Eh bien, y a pas mal de gens dehors, mais ici c'est comme un autre monde."


hi "Tu pourrais prétendre qu'il n'y a personne à des kilomètres à la ronde."

show hanako emb_downtimid
with charachange


ha "C-c'est vrai."


ha "C'est comme si le monde avait oublié cette pièce."

show hanako emb_emb
with charachange


ha "Et a-avec ça, tu peux oublier le monde extérieur."


"Ça doit être attirant dans certains cas."


"Pour autant que je sache, il n'y pas d'élèves qui en martyrisent d'autres dans cette école."


"Mais là encore, je n'ai pas vu une seule personne parler à Hanako mise à part Lilly."


"Si on est ignoré par le monde, un endroit où on peut oublier son existence doit être vraiment attirant."


hi "C'est bien. J'aime les pièces qui donnent cette impression de totale liberté."

show hanako emb_smile
with charachange


ha "O-ouais."

show hanako basic_bashful
with charachange


ha "Dis... tu joues aux échecs ?"


hi "Les échecs ? Un peu, j'imagine."


hi "J'en déduis que t'y joues ?"

show hanako basic_distant
with charachange


ha "Un peu..."

hide hanako
with charaexit


"Sans dire un mot de plus, Hanako va vers l'une des armoires et en sort un petit jeu d'échecs."


ha "Tu... tu veux..."


hi "Bien sûr, pourquoi pas ?"


"Je lui coupe la parole, mais elle ne semble pas y faire attention."

scene bg school_miyagi
show hanako basic_normal_close at center
with shorttimeskip


"On met les pièces en place, et il ne faut pas longtemps pour que nous avancions les pions pour une charge vers leur destin inévitable."


"Je prends mon temps et examine attentivement chaque mouvement et ses conséquences, la nostalgie pour le jeu prend une place secondaire face à ma concentration."


"Pendant un moment, le jeu reste une longue bataille d'usure, mais je remarque une ouverture et perce sa défense."

show hanako basic_worry_close
with charachange


"Quelques mouvements plus tard, son roi est entouré par plusieurs de mes pièces."


hi "Échec et mat."


hi "T'es pas mauvaise à ça, hein ?"


"Une évaluation honnête. Sa technique est plutôt bonne, mais plusieurs fois j'ai été en mesure d'exploiter son manque de prévision."


"Je ramasse une pièce et l'examine. Elle semble relativement nouvelle, mais usée pour son âge."

show hanako basic_smile_close
with charachange


ha "Je... j'imagine que oui."


hi "Lilly y joue ?"

show hanako def_worry_close
with charachange


"L'absence de réponse de la part d'Hanako me fait reconsidérer ma question."


ha "Un... Un peu..."


ha "C-c'est la première fois que je joue contre quelqu'un... d'autre qu'elle, ou..."

show hanako emb_downsad_close
with charachange


"Ou... ?"


"Elle s'arrête brusquement, laissant la réponse suspendue dans l'air. Quelqu'un qu'elle connaissait avant de venir à Yamaku, peut-être."


hi "Eh bien, je suis honoré d'avoir joué contre toi."

show hanako emb_smile_close
with charachange


ha "Hum... on peut rejouer ?"


"Elle le prononce comme si elle me demandait de me couper les mains. L'esprit de la compétition s'est emparé d'elle ?"


hi "Bien sûr. Mais ne t'attends pas à ce que je sois tendre avec toi cette fois..."


"Pas que je l'étais avant, de toute façon. Elle semble apprécier le ton compétitif."

show hanako emb_downsmile_close
with charachange


ha "T... toi non plus..."

stop music fadeout 2.0








label fr_A43:


scene bg school_dormhallway at bgright
show kenji happy at center
with None

stop music fadeout 2.0


"Qu'est-ce que je vais faire ? Je n'ai rien de prévu. Avec le recul, c'est vraiment stupide."


"Peut-être que je devrais demander à une fille de me tenir compagnie pendant la journée ? Mais encore, tout bien considéré, je ne pense pas pouvoir faire quelque chose comme ça. C'est seulement ma première semaine."


"Une semaine que j'ai gâchée à être gêné avec presque tout le monde, trébuchant sans arrêt en essayant de m'habituer à cet endroit."


"À bien y penser, qu'est-ce que j'ai accompli ?"


"À qui est-ce que j'aurais dû proposer de venir au festival avec moi ?"


"Merde, on dirait que Kenji est ma seule option réaliste pour une sortie aujourd'hui."


"C'est la chose la plus déprimante qui me soit arrivée depuis la fois où j'ai eu une crise cardiaque parce qu'une fille a avoué son amour pour moi."


"Je suis sans espoir."

play music music_kenji fadein 0.5


hi "Je ne sais franchement pas. Je n'ai pas grand-chose à faire, mais un fort semble un peu excessif."


hi "T'es sûr que tu ne veux pas sortir ? C'est pas comme si les visiteurs n'allaient pas venir aux dortoirs aujourd'hui."

show kenji tsun
with charachange


"Il semble atterré par la révélation."


ke "Merde, tu marques un point. Cet endroit n'est pas sûr aujourd'hui."


ke "On doit trouver quelque part où se cacher."


"Il reste silencieux un moment, réfléchissant."

show kenji neutral
with charachange


ke "Le toit."


hi "Quoi le toit ?"

show kenji happy
with charachange


ke "On va aller se cacher sur le toit aujourd'hui."


ke "C'est l'endroit parfait, personne ne monte là-haut."

show kenji neutral
with charachange


ke "Retrouves-y moi dans une heure. Je dois me préparer."

stop music fadeout 1.0

show kenji neutral at Slide(0.5,0.5,0.4,0.5,0.5, time_warp=_ease_out_time_warp)
with None

hide kenji
with charaexit

play sound sfx_doorslam
with vpunch


"Il claque la porte et la verrouille."


"La vache, qu'est-ce qui ne va pas avec Kenji ?"


"Et dire que maintenant je fais partie de sa folie. Ça me déprime vraiment."


"J'ai l'impression d'être un échec."

play ambient sfx_crowd_outdoors fadein 0.3

scene bg school_courtyard
show crowd
with locationskip


"Dès que je mets un pied dehors, le vacarme de la foule me salue."


"Toute l'école est en pleine activité."


"Il y a des stands partout, et la foule grouillante entre eux est considérable."


"Je ne m'attendais pas à ce que le festival attire tant de visiteurs."


"Je dois admettre que les gens en charge de la décoration ont fait beaucoup d'efforts, et ça se voit."


"Les gens semblent bien s'amuser, l'atmosphère est colorée et joyeuse."

play music music_rain fadein 1.0


"Ça serait bien, si je n'étais pas de si mauvaise humeur."


"À ce moment, c'est plus ennuyeux qu'autre chose."


"Bah, je n'y peux rien. Je décide de m'en tenir à mon plan et de manger, puis je suppose que j'irai au moins voir ce que Kenji fait sur le toit."

"…"

scene bg school_stalls2 at Fullpan(8.0)
with locationchange


"Je fais un tour des terrains pour tuer le temps, regardant les stands, mais ne me sentant pas d'humeur à jouer à un des jeux."


"Les couleurs criardes m'éreintent les yeux et je me sens de plus en plus mal au fur et à mesure que le temps passe."


"Je n'arrive même pas à décider quoi manger, et la large sélection combinée à la masse de visiteurs énergiques ne va pas m'aider."

scene bg school_stalls1 at bgright
with locationchange


"Je me dirige vers le stand le plus proche qui semble offrir quelque chose de plutôt comestible et me mets dans la file."


"Il s'avère que c'est des nouilles."


"Il s'avère aussi que ce n'est pas très bon."


"Eh bien, au moins c'est nourrissant. Ce n'est pas comme si je demandais autre chose, à ce moment."

scene bg misc_sky at Fullpan(25.0)
with locationchange


"Pendant que je mélange mes nouilles peu appétissantes, je me demande ce que font les autres en ce moment même."


"Shizune et Misha sont forcément quelque part en train d'organiser des choses."


"Je ferais mieux de me tenir à distance d'elles. Je ne pense pas qu'elles me pardonneraient de les avoir laissées seules pour tout gérer."


"Je suppose qu'Emi est en train de bourdonner dans tous les sens, étant dépressivement gaie."


"J'ai n'ai aucune chance de la trouver, mais aucune chance de l'éviter non plus, donc ce n'est pas important."


"Lilly est probablement en train d'aider au stand avec sa classe, et trop occupée pour moi."


"Hanako ne voudrait parler à personne de toute façon, et elle doit être seule dans un coin ou en train d'aider Lilly."


"Rin doit être à son mur et ne serait probablement d'aucune aide pour faire quelque chose d'intéressant."


"Aller là-bas pour être en paix semble l'option la plus agréable qui se présente, mais là encore, je ne pense pas que me forcer à voir de l'art puisse me remettre de bonne humeur, donc j'abandonne l'idée."

scene bg school_stalls1 at bgright
with locationchange


"Alors que j'étais perdu dans mes pensées, mes nouilles semblent avoir disparu, et donc ma faim aussi."


"Je pense que j'ai bloqué mentalement l'expérience de la nourriture, ce qui est probablement une bonne chose."


"Rassasié mais insatisfait, je me dirige vers le bâtiment principal. Une heure est déjà presque passée."

play ambient sfx_crowd_indoors fadein 0.3

scene bg school_lobby
show crowd
with locationskip


"La foule est encore plus dense ici qu'à l'extérieur."

scene bg school_hallway3
show crowd
with locationchange


"Les couloirs sont presque impraticables, et je n'ose même pas penser à l'intérieur des classes."

stop ambient fadeout 1.0

scene bg school_staircase1
with locationchange


"Je monte les escaliers vers ma destination."


"Le toit."


"Heureusement, la porte en haut n'est pas verrouillée, mais maintenant il y a un écriteau dessus."

window hide


$ written_note("{size=55}{b}ACCÈS INTERDIT{/b}{/size}", quiet=True)

window show


"Ça ne me gêne pas."

scene bg school_roof at bgright
with locationchange


"Les bruits du festival sont étonnamment atténués ici, et le toit semble désert, comme prévu."


"Près d'un endroit où la clôture s'est effondrée, il y a un tas de couvertures qui n'ont pas grand-chose à faire là."

stop music fadeout 3.0


"Attends."

play sound sfx_rustling


"Est-ce que le tas vient de bouger ?"


"Ça serait étrange, parce qu'il n'y a pas de vent du tout."


"Je lève prudemment la main et donne une petite poussée."

play sound sfx_impact
show kenji rage_close:
    alpha 0.0 xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 0.7
    easein 0.2 yanchor 1.0 alpha 1.0

with vpunch


$ doublespeak(ke, hi, "AHHHHHHHHHHHHH !")

play music music_comedy fadein 2.0

show kenji rage:
    center alpha 1.0
with charadistant


"Surpris, je saute en arrière."


ke "Qui est là ?"


hi "Bordel, Kenji. C'est moi."

show kenji tsun at center
with charachange


ke "Oh merde, tu m'as fait peur mec."


hi "Alors, qu'est-ce qu'on fait ici ?"

show kenji neutral
with charachange


ke "On pique-nique."


hi "Quoi ?"

show kenji happy
with charachange


ke "Ouais. J'ai des couvertures, des bretzels et du whisky. C'est la configuration ultime, mec."


hi "Whisky ?"


hi "T'es pas trop jeune pour boire de l'alcool ?"

show kenji tsun
with charachange


ke "J'ai 20 ans, tu sais."


hi "...je crois pas, non."

show kenji neutral
with charachange


ke "J'ai 20 ans et toi aussi."


hi "Quoi ? C'est absurde."

show kenji tsun
with charachange


ke "Hé, au moins TU as eu quelque chose de tout ça, tout ce que j'ai eu c'est cette bouteille de whisky..."


"Il marmonne de façon incohérente, mais je décide de m'en accommoder."


hi "Donc pourquoi tu as une bouteille de whisky ?"

show kenji happy
with charachange


ke "Ma mère n'a pas pu venir me voir pour le festival, donc elle m'a envoyé une bouteille de Single Malt à la place."


hi "Une histoire touchante."


ke "T'en veux ?"

hi "…"


"C'est pas comme si j'avais quoi que ce soit à perdre. Cette journée peut difficilement être pire."


hi "...pourquoi pas."

hide kenji
with charaexit

show bg school_roof at center
with charamove_accel

show kenji happy_close at offscreenleft
with None

show kenji happy_close at twoleft
show bg school_roof at bgleft
with charamove_decel


"On s'assied sur le tas de couvertures que Kenji a apparemment apportées."


"Il sort une bouteille de whisky presque pleine et me la passe."


hi "Tu n'as même pas pris de verres ?"

show kenji tsun_close
with charachange


ke "Non, c'est pas un pique-nique romantique pour princesses. Tu crois quoi, mec ?"

show kenji neutral_close
with charachange


ke "C'est un pique-nique viril."


ke "Pas de verres."


ke "Pas de serviettes."


ke "Que du whisky. La boisson des vrais hommes."


hi "Peu importe."

show kenji happy_close

with charachange


ke "Et des bretzels."


"Je regarde la bouteille de plus près."


"Whisky single malt, 12 ans d'âge."


"Haussant les épaules, j'en prends une gorgée. Ça me brûle la gorge comme de l'acide, mais le goût n'est pas désagréable."


"Je sens l'effet aller directement dans ma tête, et l'arrière-goût persiste dans ma bouche, réclamant une autre gorgée."

show kenji neutral_close
with charachange


ke "On devrait mettre au point notre contre-offensive et médire sur les femmes ici, là où elles ne peuvent pas nous entendre."

show kenji tsun_close
with charachange


ke "Merde, j'ai oublié d'amener mes graphiques."


"Je décide de jouer à un jeu d'alcool tout seul. Chaque fois que Kenji mentionne “conspiration féminine”, je bois une gorgée."

$ wdt_off(False)

stop music fadeout 2.0

scene black
with delayblinds


centered "Quatre ou cinq heures, ou peut-être quelques jours plus tard :\n{w}(J'ai perdu le fil)"

play music music_kenji fadein 0.5

scene ev kenji_rooftop
with delayblinds

window show


ke "Tu devrais pas te sentir mal, mec ! Prends ça à la légère, putain ! Sérieusement, sérieusement !"


hi "Je suis relaxé là, bordel !"


ke "Je te le dis comme je le vois !"

scene ev kenji_rooftop_kenji
with flash


ke "Penses-y. Quand est-ce que les logements et les terrains sont devenus plus chers ? Quand les femmes ont commencé à rentrer sur le marché du travail, à cause de ça, ça a créé des familles nucléaires à deux revenus."


ke "Ouais j'ai oublié mes graphiques, mais, et tu dois me croire sur parole, les femmes sont liées à la décadence de toute notre société."

show ev kenji_rooftop_large:
    crop (288, 376, 800, 600)
    ease 1.0 crop (1024, 260, 800, 600)


hi "Je vois. C'est un peu difficile à croire."


"Même si je dis ça, quelque part, tout ce que dit Kenji semble avoir plus de sens maintenant."


"Tout concorde, mais je ne sais pas si c'est parce qu'il explique mieux les choses quand il est ivre, ou parce que je comprends tout mieux quand je suis ivre."

show ev kenji_rooftop_large:
    ease 1.0 crop (288, 376, 800, 600)


ke "Nan mec, réfléchis. Réfléchis ! Réfléchis aux implications plus profondes !"


ke "Les gens pouvaient se permettre de commencer à dire “Oh, vu qu'il y a deux membres de la famille qui gagnent de l'argent maintenant au lieu d'un, ils peuvent certainement se permettre une augmentation des coûts de propriété.”"

show ev kenji_rooftop_large:
    ease 1.0 crop (1024, 260, 800, 600)


hi "Je vois où tu veux en venir. Mais le terrain au Japon a toujours été cher."

show ev kenji_rooftop_large:
    ease 1.0 crop (288, 376, 800, 600)


ke "...Et le prix des terrains gonfle généralement quand un pays commence à s'industrialiser. ...Mais non ! C'est la faute des femmes ! La corrélation est égale à la causalité, tu sais."

show ev kenji_rooftop_large:
    ease 1.0 crop (1024, 260, 800, 600)


hi "Je pensais que la corrélation n'était pas égale à la causalité. Bah, peu importe, t'as peut-être raison."

show ev kenji_rooftop_large:
    ease 1.0 crop (288, 376, 800, 600)


ke "J'ai toujours raison. Ouais, je parie que les femmes ont créé l'industrialisation, aussi, pour couvrir leurs traces."


ke "Vraiment diabolique."


ke "Donc ouais, tout le monde peut aller se faire foutre !"

scene bg school_roof_ni
show kenji rage_ni:
    xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 0.9
    easein 1.0 yanchor 1.0
with locationchange


"Il se lève, m'impressionnant parce que je suis presque sûr de ne pas pouvoir le faire même si je le voulais. Il hurle très fort comme s'il avait perdu la notion du volume. Je grimace et ai presque envie de me boucher les oreilles."

stop music fadeout 2.0


ke "Aaagh, ç'aurait été bien si j'avais été en bas... Mais non. Tu vois, penser comme ça est un piège, tu penses que tu loupes quelque chose, mais à la fin de la route, il n'y a rien à part le désespoir..."

show kenji tsun_ni at center
with charachange

play music music_sadness fadein 1.5


"Kenji attrape la bouteille et penche la tête en arrière, essayant de verser l'alcool dans sa bouche, mais n'arrivant qu'à le verser sur lui."

show kenji rage_ni
with charachange


ke "Merde ! Tu vois, ma précision est terrible, et la mauvaise chose avec l'alcool est que plus tu bois, et pire c'est !"

show kenji tsun_ni
with charachange


ke "Aujourd'hui est le jour du désespoir."


"Sa voix baisse immédiatement jusqu'à devenir presque un murmure, mais il commence à parler beaucoup plus vite qu'avant, avec une voix un peu pâteuse à cause du whisky."


"Pendant qu'il parle, il remue la bouteille, en renversant un peu çà et là."


ke "Ouais, tu sais ce qui a été l'évènement le plus choquant de ma vie ?"


"J'ai un souvenir brumeux de lui en train de raconter que le deuxième évènement le plus choquant de sa vie est quand un oiseau lui a déféqué sur la tête."


"Je n'ai pas particulièrement de grands espoirs mais je lui fais signe de continuer quand même."

show kenji neutral_ni
with charachange


ke "Tu ne vas pas le croire, mais j'avais une petite copine ici, je crois que c'était l'année dernière."


ke "Ouais, ça t'a courcicuité le cerveau, hein ? Tu sais, je ne l'avais jamais dit à personne."


"C'est vrai, la pensée m'a effectivement fait courcicuiter le cerveau. Soudainement, je veux la bouteille. Je la reprends et la descends autant que je le peux."

show kenji tsun_ni
with charachange


ke "J'étais plus innocent à l'époque, et je pensais qu'elle était saine d'esprit, contrairement aux autres femmes. Mais un jour, on a eu des... rapports sexuels."


ke "C'était pas mal, mais juste après l'évènement culminant, quelque chose d'étrange et d'effrayant s'est produit."

show kenji tsun_ni at tworight
show bg school_roof_ni at bgleft
with charamove


"Il se jette contre la clôture, s'appuyant contre elle, les yeux plissés."


ke "J'ai commencé à me sentir très fatigué et endormi ! C'est pas normal, mec ! C'est quoi ce bordel ?"


ke "Je veux dire, normalement, ça devrait faire monter la tension, pomper l'adrénaline de quiconque, mais mon niveau d'énergie tombait comme une brique !"


ke "Quelque chose de sinistre avait lieu, je pouvais le sentir."


ke "C'est là que j'ai su... les femmes sont dangereuses, sapant la force vitale de tous les hommes en utilisant la seule chose qui est presque exclusivement sous leur contrôle !"


ke "Écœurant."

show kenji neutral_ni
with charachange


ke "Ouais, tu ferais mieux de t'abstenir, mec..."


"Kenji avait raison, c'est vraiment le jour du désespoir. Je bois encore plus pour éviter de réfléchir à ce qu'il vient de dire."


ke "Maintenant je suis le dernier homme sain d'esprit dans un monde de fous... quand les autres gens s'en rendront compte, il y aura une guerre, une grande guerre entre les hommes et les forces féministes."


ke "Mais le problème est que tous les hommes ne se battront pas à mes côtés... c'est la merde. Je peux mettre la barre plutôt bas, tous les hommes sont bons à prendre. Mais pas les gars élevés par leur mère ou leur sœur, ça c'est sûr."

show kenji tsun_ni
with charachange


ke "Et personne aimant le porno où il y a des filles avec des bites."


hi "Ha... Cette situation me semble peu probable, comme si ça ne pouvait pas arriver, comme... comme si ce n'était pas très probable."


"L'alcool doit faire effet."


"Peu importe, je me sens toujours déprimé d'être ici aujourd'hui."


"Je n'avais pas vraiment autant hâte d'être au festival que le reste de l'école, mais quand même."


"Ça aurait été bien d'être avec quelqu'un. Vu d'ici, on dirait que tout le monde s'amuse bien. Peut-être que je manque quelque chose."


"C'est juste qu'il n'y a personne avec qui j'aurais pu y aller."


"Ou peut-être qu'il y avait. Tant d'occasions, en y réfléchissant, je dois en avoir gâché beaucoup."


ke "Merde, c'est le vrai désespoir... Le pire c'est que parfois j'ai l'impression de n'avoir pas de choix dans ma vie, tu sais ?"


ke "Comme si je n'avais jamais la chance de prendre une décision, que les merdes arrivent juste."


ke "Comme si c'était préprogrammé. Comme le destin... ou un truc du genre. Comme s'il n'y avait aucun moyen que je puisse avoir mon mot à dire sur ce que je fais."

stop music fadeout 0.2

show kenji rage_ni
with vpunch


ke "Vite, pose-moi une question !"

hi "Uh…"


ke "Maintenant !"


hi "Je ne peux pas vraiment..."

show kenji tsun_ni
with charachange


ke "Tu vois ? C'est juste un autre exemple ! Merde ! Putain ! Merde ! Tu vois, hein ? Maintenant, quand j'essaye d'aller contre ma destinée et de prendre en charge ma vie, l'opportunité n'est même pas là."


ke "Merde, mec, tu m'as laissé tomber. Laissé tomber pour la dernière fois. Salaud."

show kenji tsun_ni:
    xpos 0.7 ypos 1.0 xanchor 0.5 yanchor 1.0
    easeout 0.7 ypos 0.9 yanchor 0.5
with Pause(0.8)

show kenji tsun_ni:
    rotate 0
    easeout 0.7 rotate 90 ypos 1.0 yanchor 0.3

with Pause(.7)


play sound sfx_impact
with vpunch

hide kenji
with None


"Il tombe à genoux et s'effondre sur le côté, gisant sur le gravier du toit."


hi "Hé, ça va ?"


ke "Non, ça ne va pas, tu ne peux pas voir que je suis désespéré ?"


"Il parle sur un ton sarcastique."

show kenji neutral_ni:
    xpos 0.7 ypos 1.0 xanchor 0.5 yanchor 0.0
    easein 0.5 ypos 1.0 yanchor 0.7
with Pause(0.5)


"Tout à coup, Kenji se redresse, se tapote maladroitement pour se nettoyer, et tend la main vers moi pour attraper la bouteille. Je lui mets dans la main."

show kenji tsun_ni at Transform(xpos=0.7, xanchor=0.5, ypos=1.0, yanchor=0.7)
with charachange


ke "Ah bah merde ? Bordel, tu as descendu presque toute la bouteille. Tu vois, c'est comme si je n'avais pas d'option dans la vie..."


ke "C'est comme ça que ça va être jusqu'à la fin des temps ?"


hi "Bah, je suis plutôt sûr que ça ne va pas être comme ça jusqu'à la fin des temps."


"Quoi que ce soit dont il parle. Ma tête tourne. Je me lève et m'appuie contre la clôture, espérant que ça m'aidera à me concentrer un peu."

show kenji tsun_ni at center
show bg school_roof_ni at center
with charamove


ke "Ouais, je sais. On doit lutter contre le pouvoir avec tout ce qu'on a. C'est le seul moyen de vivre."

play music music_one fadein 6.0

show kenji neutral_ni
with charachange


ke "T'es un mec bien."

show kenji happy_ni
with charachange


ke "Ce lien fraternel est ce qui me motive en ces temps sombres."

show kenji neutral_ni
with charachange


ke "On devrait aller troller les femmes."


hi "Toller les femmes ? Quoi ?"

show kenji neutral_close_ni
with characlose


ke "Troller les femmes. Du troll à femmes. Mais on doit le faire maintenant, avant que je perde le courage lié à l'alcool."


"Il gesticule vigoureusement. Violemment, même."

show bg school_roof_ni at Slide(0.5,0.5,0.75,0.75,0.5, time_warp=_ease_time_warp)
show kenji neutral_close_ni at Slide(0.5,0.5,0.3,0.5,0.5, time_warp=_ease_time_warp)
with None

show kenji neutral_ni at Slide(0.5,0.5,0.3,0.5,0.5, time_warp=_ease_time_warp)
show bg school_roof_ni at Slide(0.5,0.5,0.75,0.75,0.5, time_warp=_ease_time_warp)
with charadistant


"Je fais un pas en arrière."

show kenji neutral_ni at Slide(0.3,0.5,0.5,0.5,0.5, time_warp=_ease_time_warp)
with None

show kenji neutral_close_ni at Slide(0.3,0.5,0.5,0.5,0.5, time_warp=_ease_time_warp)
with characlose


"Il fait un pas en avant."

show kenji happy_close_ni
with charachange


ke "Qu'est-ce qui t'arrive ? Pas d'humeur pour l'amour ?"


hi "Pour être franc... non."

show bg school_roof_ni at Slide(0.75,0.75,1.0,1.0,0.5, time_warp=_ease_time_warp)
show kenji happy_close_ni at Slide(0.5,0.5,0.3,0.5,0.5, time_warp=_ease_time_warp)
with None

show kenji happy_ni at Slide(0.5,0.5,0.3,0.5,0.5)
show bg school_roof_ni at Slide(0.75,0.75,1.0,1.0,0.5, time_warp=_ease_time_warp)
with charadistant


"Je fais un autre pas en arrière."

show kenji happy_ni at Slide(0.3,0.5,0.5,0.5,0.5, time_warp=_ease_time_warp)
with None

show kenji happy_close_ni at Slide(0.3,0.5,0.5,0.5,0.5, time_warp=_ease_time_warp)
with characlose



"Il fait un autre pas en avant."


"Il se penche très, trop proche."


hi "Bordel, arrête de te pencher comme ça, ça me perturbe."


ke "Penché comme quoi ? Hé, tu ne devrais pas t'appuyer sur la barrière comme ça, c'est dangereux."


"J'essaye de m'éloigner de Kenji, mais mon équilibre n'est pas bon."


"À cause de mon vertige, j'attrape un des piquets de la clôture, mais je sens qu'il cède dès que je mets mon poids dessus."


"...C'est pas bon. Même si mon cerveau embrouillé par l'alcool ne semble pas être capable d'enregistrer pourquoi."

show black behind bg
with None

show n_vignette:
    xalign 0.5 yalign 0.5 zoom 4.0
    linear 0.2 zoom 1.2
with Pause(0.2)

show n_vignette:
    zoom 1.2
    linear 8.0 zoom 0.001
show kenji happy_close_ni:
    xalign 0.5 yalign 0.5
    linear 8.0 zoom 0.001
show bg school_roof_ni_crop:
    xalign 0.5 yalign 0.5
    linear 8.0 zoom 0.001


"Le visage de Kenji semble devenir plus petit, ce qui est un peu un soulagement."


"Beaucoup plus petit, en fait. Et rapidement aussi."

show nightsky rotation
with None


"On dirait qu'il y a du vent maintenant. D'une certaine façon je me sens presque en apesanteur."


"Je me sens étourdi, comme si mon esprit était vide."


hi "Je suis en train de... tomber... ?"


"Je peux voir le ciel pendant que je tourne dans les airs. La bouteille s'envole du bout de mes doigts et disparaît dans les airs pendant que je tombe."


"Je réalise que c'est la fin d'une très, très mauvaise journée."

window hide

stop music fadeout 0.1
play sound sfx_crunchydeath

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
