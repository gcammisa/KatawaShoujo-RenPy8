


label fr_NOP1:
window hide None

scene black
with None

scene bg op_snowywoods
show snow
with Dissolve(2.0)

window show

play music music_serene fadein 2.0


"Une légère brise faisait frissonner les branches dans un léger bruissement."



"Il s'agissait d'un endroit apprécié par les couples durant l'été. Les arbres feuillus formaient un superbe auvent vert, loin de la vue des professeurs et des étudiants."



"Mais là, en cette fin d'hiver, j'avais l'impression d'être en dessous d'une pile de petit bois."


"Je soufflais sur mes mains et les frottais nerveusement pour les empêcher de s'engourdir dans ce froid."


hi "Combien de temps est-ce que je suis censé attendre ici ? Je suis sûr que le message disait 16 heures."


"Ah oui... le message... glissé entre les pages de mon livre de maths pendant que je regardais ailleurs."


"Je préfère encore le cliché de la lettre dans le casier, mais au moins, cette façon de faire montrait un peu d'initiative."


"La neige tombait de plus en plus pendant que je réfléchissais au sens du message."


"Tombant silencieusement du ciel, les flocons de neige étaient le seul signe du temps qui passe."


"Leur lente descente sur la forêt gelée laissait penser que le temps avait ralenti."

play sound sfx_rustling


"Interrompant ce moment de calme, un bruissement de pas sur la neige me fit sursauter. Quelqu'un approchait derrière moi."


mystery "Salut... Hisao ? Tu es venu ?"


"Une question hésitante, presque inaudible."


"Cependant, je reconnus instantanément cette voix délicate."


"Je sentis mon cœur rater un battement."


"C'est une voix que j'avais entendue des centaines de fois, mais jamais autrement qu'en prêtant une oreille indiscrète lors d'une conversation."


"Je me retournais pour faire face à cette voix, celle de mes rêves, et mon cœur commença à s'emballer."

window hide

$ ksgallery_unlock("evul other_iwanako")
scene ev other_iwanako_start
show snow
with GenericWhiteout(0.5,0.0,5.0)

window show


hi "Iwanako ? J'ai reçu un message me disant d'attendre ici... c'était le tien ?"


"Fait chier. J'avais passé tout l'après-midi à essayer de trouver une bonne réplique, et voilà le résultat."


"C'est pathétique."


"Iwanako" "Ah... oui. J'ai demandé à un ami de te donner ce message... Je suis vraiment contente que tu l'aies reçu."


"Son timide mais joyeux sourire me rendait si tendu que même en essayant, je ne pouvais bouger un seul muscle."

stop music fadeout 10.0

window hide

scene bg op_snowywoods
show snow
with GenericWhiteout(0.5,0.0,2.0)

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)

with Pause(0.7)

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)

window show


"À cet instant, mon cœur battait la chamade, comme s'il cherchait à jaillir de ma poitrine et à réclamer cette fille pour lui seul."

window hide

scene ev other_iwanako
show snow
with GenericWhiteout(0.5,0.0,3.0)

window show


hi "Donc... euh... nous y sommes. Dehors dans le froid..."


"Une fois encore, le vent agitait les branches. Le bruit de cette cacophonie était une musique à mes oreilles."


"Iwanako frissonna légèrement à cause de ce même vent."


"À ce moment, elle devint sûre d'elle-même, comme si elle avait été soutenue par une sorte de nouvelle confiance."


"Ses yeux étaient rivés aux miens et elle enroulait nonchalamment ses longs cheveux sombres autour de son doigt."


"Pendant tout ce temps, l'anxiété faisait battre mon cœur plus fort."

window hide

scene bg op_snowywoods
show snow
with GenericWhiteout(0.5,0.0,2.0)

window show


"Ma gorge était serrée ; je doutais de pouvoir réussir à sortir un mot, même si je me forçais."


"Iwanako" "Dis..."

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.4)

window show


"Iwanako" "...Je voudrais savoir..."

stop music fadeout 0.5

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


"Iwanako" "...si tu veux bien sortir avec moi..."



"Je restais là, immobile, seul mon cœur battait."


"Je voulais répondre, mais mes cordes vocales se trouvaient comme au-delà du point de rupture."

play music music_tragic fadein 0.05


"Iwanako" "...Hisao ?"


"Je levai la main pour essayer de me masser la gorge, mais cela ne fit qu'envoyer des pointes de douleur assourdissante le long de mon bras."



"Iwanako" "Hisao ?!"


window hide

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.8)

window show


"Mon corps entier se figea, à l'exception de mes yeux, qui restèrent ouverts sous le coup de la terreur."


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

stop music fadeout 0.3

show heartattack residual
with Dissolve (0.8)

window show


"Iwanako" "HISAO !"



"Le battement dans ma poitrine s'arrêta brusquement, et mes jambes flanchèrent."

window hide

show passoutOP1
with None

nvl show Dissolve(0.2)


n "\n\n\n\n\n\n\nLe monde autour de moi - l'auvent de branches nues, le ciel terne d'hiver, Iwanako courant vers moi - tout vira au noir."


n "\nLes dernières choses dont je me souvienne avant de m'évanouir sont Iwanako criant pour demander de l'aide et le cliquetis incessant des branches au-dessus de moi..."

nvl hide Dissolve(3.0)

nvl clear

with Pause (1.0)

scene black
with None


label fr_NOP2:

window hide None

scene black
with None


centered "Quatre mois se sont écoulés depuis ma crise cardiaque." with dissolve

scene bg hosp_room
show sakura
show hospitalmask
with Dissolve (1.5)

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_rain fadein 4.0

nvl show dissolve


n "Durant cette période, je peux sûrement compter sur mes doigts le nombre de fois où j'ai quitté cette chambre d'hôpital sans surveillance."


n "Quatre mois c'est assez long quand on reste seul avec ses pensées. Donc, j'ai eu bien assez de temps pour m'habituer à ma situation."


n "Arythmie."


n "Un mot étrange, un mot venu d'ailleurs. Un avec qui personne ne voudrait partager sa chambre."


n "Une maladie rare. Elle force le cœur à agir de manière erratique et parfois, à battre trop vite. Elle peut être fatale."


n "Apparemment, je l'ai depuis longtemps. Ils m'ont dit que c'était un miracle que j'aie pu aller bien pendant si longtemps sans que rien ne se passe."


n "Est-ce vraiment un miracle ? Je crois qu'ils ont dit ça pour que je me sente mieux et que je sois reconnaissant d'être en vie."


n "Ça ne me remonte vraiment pas le moral."

nvl clear


n "\n\n\n\n\nMes parents, je crois, ont été plus choqués par la nouvelle que je ne l'ai été. Ils ont pratiquement eu deux infarctus chacun."


n "\nJ'avais déjà eu une journée pour tout digérer. Pour eux c'était tout frais. Ils étaient même prêts à vendre notre maison pour payer un remède."


n "\n\nBien sûr, il n'existe pas de remède."

nvl clear


n "\nEn raison de la découverte tardive de ce... problème, j'ai dû rester à l'hôpital, pour récupérer du traitement."


n "Lors de ma première admission, je me suis senti comme perdu..."


n "Pendant environ une semaine, ma chambre était remplie de fleurs, de ballons et de cartes."


n "Mais les visiteurs et les cadeaux de bon rétablissement ont rapidement diminué jusqu'à finir par disparaître."


n "J'ai réalisé que la seule raison pour laquelle j'avais eu autant de cartes et de fleurs était le fait qu'envoyer leur sympathie avait été transformé en projet de classe."


n "Peut-être que certaines personnes compatissaient vraiment, mais j'en doute. Même au début, j'avais peu de visiteurs. À la fin du premier mois, seuls mes parents venaient régulièrement."


n "Iwanako fut la dernière à arrêter ses visites."


n "Après six semaines, je ne l'ai plus jamais revue. De toute façon, nous n'avions jamais eu grand-chose à nous dire lors de ces visites."


n "Nous n'avions jamais reparlé de ce qu'il s'était passé entre nous en ce jour de neige."

nvl clear


n "\nL'hôpital ?"


n "Ce n'est pas vraiment un endroit où j'aimerais vivre."


n "Les médecins et les infirmières sont trop froids et impersonnels."


n "Je suppose que c'est parce qu'ils sont pressés et qu'ils ont un million d'autres patients qui les attendent, mais ça me met mal à l'aise."


n "Pendant les deux premiers mois, j'ai demandé au chef de cardiologie, à chaque fois que je le voyais, une estimation approximative du moment où je serais en mesure de partir."


n "Il n'a jamais répondu directement à mes questions. Il me disait d'attendre pour évaluer si le traitement et les chirurgies faisaient effet."


n "\nAinsi, j'observais paresseusement la cicatrice que ces chirurgies avaient laissée sur ma poitrine et qui changeait lentement avec le temps, laissant penser à une sorte de mauvais présage."


n "Je continue de demander ma date de sortie au chef de service, mais je n'y crois plus vraiment ; maintenant je ne suis plus déçu quand je ne reçois pas de réponse."

nvl clear


n "\n\n\n\nÀ un moment j'ai arrêté de regarder la télévision. Je ne sais pas pourquoi, je l'ai juste fait."


n "Peut-être était-ce une mauvaise façon d'échapper à ma situation."


n "\nJ'ai commencé à lire à la place. Il y avait une petite “bibliothèque” à l'hôpital, même si elle ressemble plus à une pièce de stockage pour livres. J'ai commencé à tailler mon chemin à travers elle, une petite pile à la fois. Après les avoir lus, j'y retournais pour en prendre d'autres."


n "Il s'est avéré que j'aimais lire et je pense que je suis devenu un peu accro. J'ai commencé à me sentir nu sans un livre dans les mains."


n "\nMais j'aimais les histoires."

nvl clear


n "C'est à ça que ressemblait ma vie."


n "Ce fut de plus en plus difficile de distinguer les jours les uns des autres, n'ayant pour unique repères que le livre que je lisais et la météo. Le temps passant était comme une sorte de masse visqueuse me retenant prisonnier à l'intérieur."


n "Une semaine pouvait passer sans que je ne m'en aperçoive vraiment."


n "Parfois, je me posais en réalisant que je ne savais pas quel jour de la semaine on était."


n "Mais d'autres fois, toutes ces choses qui m'entouraient venaient s'écraser douloureusement sur ma conscience, malgré la barrière de nonchalance que j'avais mise en place."


n "Les pages de mon livre commençaient à être coupantes et brûlantes, et la lourdeur dans ma poitrine devenait si difficile à porter que je devais poser mon livre et simplement m'allonger pendant un certain temps, en regardant le plafond, comme si j'allais pleurer."


n "Mais cela n'est arrivé que rarement."


n "Et je ne pouvais même pas pleurer."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve

nvl clear

window show


"Aujourd'hui, le médecin arrive en souriant. Il semble excité, mais pas trop. Comme s'il essayait de faire un effort pour être heureux à ma place."


"Mes parents sont là. Je ne les ai pas vus depuis quelques jours. Ils sont tous les deux plutôt bien habillés. Est-ce que c'est censé être une sorte d'occasion spéciale ? Ce n'est pas une fête."


"Le cardiologue a un rituel bien à lui. Il prend son temps, trie ses papiers, puis les met de côté comme pour faire un point sur l'inutilité de ce qu'il vient de faire."


"Puis il s'assoit sur le bord du lit à côté du mien. Il me regarde dans les yeux un instant."


"Docteur" "Bonjour, Hisao. Comment vas-tu aujourd'hui ?"


"Je ne lui réponds pas, mais je lui montre un léger sourire, en réponse au sien."


"Docteur" "Je crois que tu peux rentrer à la maison ; ton cœur est plus fort maintenant, et avec quelques précautions, ça devrait aller."


"Docteur" "Nous avons trouvé le traitement qui te convient. Je vais donner la prescription à ton père."


"Le médecin remet une feuille de papier à mon père, dont le teint devient livide pendant qu'il la parcourt."


"Papa" "Tant que ça..."


"Je la lui prends des mains et y jette un œil par moi-même, me sentant engourdi. Comment je suis supposé réagir face à ça ?"

$ renpy.music.set_volume(0.5, 2.0, channel="music")

scene white
with Dissolve(2.0)

show wallodrugs:
    xalign 0.0 subpixel True
    easein 25.0 xalign 1.0



"La liste ridiculement longue de médicaments qui me fixe depuis la feuille me paraît insurmontable. Ils se mélangent tous dans un océan de lettres."


"C'est insensé."


"Les effets secondaires, effets indérisables, contre-indications et dosages sont énumérés ligne après ligne avec une précision glaciale."


"J'essaie de les lire, mais cela ne sert à rien."


"Je n'y comprends rien. Je me sens encore plus malade en essayant."


"Tout ça... pour le reste de ma vie ? Tous les jours ?"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

scene bg hosp_room
show sakura
show hospitalmask
with fade


"Docteur" "Je crains que ce soit le mieux que nous puissions faire à ce stade."


"Docteur" "Toutefois, de nouveaux médicaments sont constamment mis au point, donc je ne serais pas surpris de voir cette liste se raccourcir au fil des années."


"Années... Il cherchait à me rassurer ? Je me serais senti mieux s'il n'avait rien dit du tout..."


"Docteur" "Aussi, j'ai parlé avec tes parents et nous pensons qu'il serait mieux que tu ne retournes pas à ton ancienne école."


"Quoi ?!"


"Papa" "S'il te plaît, calme-toi, Hisao. Écoute ce que le docteur a à dire..."


"Me calmer ? La façon dont il l'a dit m'indique qu'il savait que je ne voudrais pas. Je vais suivre un enseignement à domicile ?"


"Quelle que soit l'inquiétude que je puisse montrer, elle est ignorée."


"Docteur" "Nous comprenons tous que ton éducation est primordiale, mais je ne pense pas qu'il serait prudent pour toi d'être sans surveillance."


"Docteur" "Du moins tant que nous ne sommes pas sûrs que tes médicaments soient adaptés."


"Docteur" "Alors, j'ai parlé à tes parents de ton transfert dans une autre école."


"Docteur" "C'est une école qui s'appelle l'Académie Yamaku et qui est spécialisée dans le traitement des étudiants handicapés."


"Handicapés ? Quoi ? Je suis..."


"Docteur" "Elle dispose d'un personnel infirmier 24 heures sur 24 et elle est située à seulement quelques minutes d'un hôpital très réputé. La majorité des étudiants vivent sur le campus."


"Docteur" "Pensez-y comme à une sorte d'internat. Il est conçu pour donner de l'indépendance aux étudiants, en maintenant une aide à proximité."


"Indépendance ? C'est une école pour enfants handicapés. Pas la peine d'amenuiser ce fait."


"Si c'était vraiment “libre,” il n'y aurait pas un personnel infirmier 24 heures sur 24 et vous n'utiliseriez pas la proximité de l'hôpital comme un argument de vente."


"Papa" "Bien sûr, c'est uniquement si tu veux y aller. Mais... ta mère et moi ne sommes pas vraiment en mesure de te scolariser à la maison."


"Papa" "Nous y sommes allés il y a quelques semaines ; je pense que tu t'y plairais."


"On dirait que je n'ai pas vraiment le choix."


"Docteur" "Les gens dans ton état ont généralement tendance à vivre une longue vie par rapport aux autres problèmes cardiaques. Tu auras besoin d'un travail un jour, et c'est là une bonne opportunité pour continuer tes études."


"Ce n'est pas une opportunité, n'appelez pas ça une opportunité. N'en parlez pas comme si c'était une foutue opportunité."


"Docteur" "Eh bien, tu dois être excité à l'idée de retourner à l'école. Je me souviens que tu voulais y retourner, et bien que ce ne soit pas la même..."


"Une école spéciale. C'est..."


"Une insulte. C'est ce que je veux dire. C'est un pas en arrière."


"Papa" "Ce n'est pas ce que tu penses. Tous les élèves y sont très actifs, chacun à leur façon."


"Papa" "Elle est conçue pour les étudiants qui peuvent encore se déplacer et apprendre, mais qui ont juste besoin d'un peu d'aide... d'une manière ou d'une autre."


"Docteur" "Ton père a raison. Et beaucoup de diplômés de l'école ont pu faire des choses étonnantes. Une personne ne doit pas être freinée par son handicap."


"Docteur" "Un de mes collègues dans un autre hôpital en est diplômé."


"Je m'en fous. Une personne ne doit pas être freinée par son handicap ? C'est pourtant la définition même du mot."


"Je déteste vraiment le fait que quelque chose de si important ait été décidé sans moi. Mais qu'est-ce que j'y peux ? Une vie “normale” n'est plus possible maintenant."

stop music fadeout 10.0


"C'est drôle, j'avais toujours pensé que ma vie était plutôt ennuyeuse, mais maintenant, elle me manque."


"J'ai envie de protester. Mettre cette absence de réaction sur le compte du choc ou de la fatigue. Je pourrais facilement crier quelque chose maintenant ; quelque chose sur la façon dont je peux quand même retourner à mon ancienne école. Mais, non."


"Je ne dis rien. Le fait est que maintenant, je sais que c'est inutile."


"Je regarde autour de moi, me sentant très fatigué de tout ça. L'hôpital, les médecins, mon état, tout."


"Il n'y a vraiment aucun choix. Je le sais, mais l'idée d'aller dans une école d'handicapés... en quoi est-ce comparable à une école normale ? J'ai beau essayer de trouver un aspect positif à ce sujet, c'est vraiment très difficile."


"Mais laissez-moi essayer."


"Faire table rase n'est pas une mauvaise chose."


"C'est la seule chose à laquelle je puisse penser pour pouvoir m'en sortir. Au moins, j'ai quelque chose ; même si c'est une “école spéciale,” c'est quelque chose. C'est un nouveau départ, et ma vie n'est pas finie. Ce serait une erreur de penser ça."


"Tout du moins, je vais essayer de voir ce à quoi ma nouvelle vie va ressembler."

window hide




label fr_A1:

window hide None

scene bg school_gate
with Dissolve(3.0)

play music music_happiness

window show


"Le portail semble bien trop pompeux pour ce qu'il est."


"En fait, les portails en général sont comme ça, mais celui-ci l'est particulièrement."


"Briques rouges, fer forgé noir et plâtre gris, assemblés en un tout qui ne donne pas l'impression que l'on est bienvenu."


"Je me demande si une porte d'école doit ressembler à cela, mais je n'arrive pas à savoir. Sans doute que non."


"Bien sûr je ne veux pas rester bloqué à réfléchir sur cette porte pendant trop longtemps, alors je la franchis avec un rythme soutenu, ce qui est étonnamment agréable."


"Aller de l'avant est agréable."

scene bg school_courtyard
with locationchange


"Alors je marche vers le bâtiment principal de l'Académie Yamaku, avec ce rythme soutenu. Je suis seul, mes parents amènent mes affaires aux dortoirs, et il y a quelqu'un censé m'attendre pour m'accueillir."


"La cour est incroyablement luxuriante, remplie de vert."


"Ça ne ressemble pas à une cour d'école, mais plus à un parc, avec un chemin entre les arbres et l'odeur de l'herbe fraîchement coupée et tous les autres trucs qu'on trouve dans un parc."


"Des mots comme “propre” et “hygiénique” surgissent dans ma tête. Ça me fait frémir."


"Je les chasse de mon esprit. Reste ouvert. C'est ta nouvelle vie. Il faut la prendre comme elle vient."


"C'est ce que je me dis."


"Quelques bâtiments apparaissent derrière les arbres. Ils sont trop gros et trop nombreux pour une école."


"Tout ceci est si étrange ; c'est différent de ce que je pensais savoir à propos des écoles."


"C'est une sensation étrange de transition. Même si on m'a dit que c'est ma nouvelle école, au fond de moi, je ne le ressens pas comme tel."


"Je me demande si le sentiment est réel ou s'il est altéré par l'idée que je me fais d'une école pour handicapés."


"En parlant de ça, je ne vois personne d'autre ici. C'est un peu surnaturel."


"Ça me donnerait presque envie que quelqu'un soit là pour qu'il y ait quelque chose de concret auquel je puisse m'accrocher au lieu d'avoir le sentiment d'être arrivé dans une autre dimension."


"Le bruit des arbres dans le vent et les teintes vertes réfléchissantes tout autour de moi attirent mon attention."


"Ça me fait penser aux hôpitaux, ils disent que les salles d'opérations sont peintes en vert parce que le vert est une couleur apaisante."


"Alors, pourquoi suis-je si inquiet, en dépit de toute cette verdure ?"


"..."


"C'est seulement une fois que je suis en face du bâtiment principal que je réalise enfin pourquoi la porte m'avait autant tracassé :"


"C'était la dernière chance que j'avais de faire demi-tour. Même si je n'avais pas de vie, je pouvais repartir."


"Mais toujours est-il que, une fois entré, je ne pouvais plus revenir en arrière."


"C'est rendu nerveux par cette prise de conscience que j'ouvre la porte d'entrée."

scene bg school_lobby
with locationchange


"Un homme plutôt grand et qui se tient mal me remarque alors que j'entre. Nous sommes les seuls dans le hall, donc c'est logique."

show muto normal at center
with charaenter


mu_ "Tu dois être... Ni... Na... Niki ?"



show muto smile
with charachange


mu_ "Donc c'est toi. Excellent. Je suis ton professeur principal et j'enseigne les sciences. Mon nom est Mutou."


mu "Bienvenue."


"Nous échangeons une poignée de main qui n'est ni ferme ni molle, et il regarde sa montre."

show muto irritated
with charachange


mu "Le cadre infirmier t'a demandé pour un bref contrôle, mais on n'a pas le temps pour ça maintenant."


hi "Oh. Je devrai y aller plus tard ?"

show muto normal
with charachange


mu "Oui, durant l'après-midi. Nous ferions mieux de nous dépêcher, on est en retard pour ta présentation devant la classe. Ils attendent déjà."


"Ils m'attendent ? Je n'aime pas vraiment être au centre de l'attention, mais je suppose que c'est inévitable dans une telle situation."


"D'une certaine manière, ne pas savoir ce qui m'attend me rend très nerveux."


"En y pensant, je regrette presque ce que l'enseignant vient de dire."

label fr_choiceA1:
menu:
    with menueffect
    mu "Tu veux te présenter à la classe ?"
    "Pourquoi ?":





        return m1
    "Oui, bien sûr.":


        return m2

label fr_A1a:


hi "Pourquoi ? Je suis obligé de le faire ?"


mu "Bien sûr que non. D'où ma question."


hi "D'accord."


mu "Allons-y alors."


label fr_A1b:


hi "Ouais, bien sûr. Je veux dire, c'est normal, non ?"


mu "Bien sûr. Mais tout le monde n'aime pas être au centre de l'attention."


"Ce qui est mon cas, mais je pense que je c'est à moi de donner la première impression à mon sujet."


hi "Oui, mais ce n'est pas un problème."


mu "Allons-y alors."



label fr_A1c:

scene bg school_staircase2
with locationchange


"Mon cœur bat la chamade ; cela me rappelle ma maladie pendant que je suis le professeur dans l'escalier."

scene bg school_hallway3
show muto normal at center
with locationchange


"La troisième porte du couloir du troisième étage est indiquée comme étant la salle de classe 3-3."

play sound sfx_dooropen


"Mutou ouvre la porte et entre."

show muto normal at Alphaout(0.5), Slide(0.5,0.5,0.4,0.5,0.5,_ease_out_time_warp)
with Pause (0.5)

hide muto
with None


mu "Bonjour tout le monde, désolé, je suis encore en retard."

stop music fadeout 2.0


"J'hésite une fraction de seconde à passer la porte, figé sur place."





label fr_A2:

scene bg school_hallway3
with None


"Ah, ressaisis-toi ! C'est un grand pas, je le sais... Mais il n'y a aucune raison de s'inquiéter autant, du moins pas pour le moment."

scene ev hisao_class_start
with fade

play music music_normal fadein 0.5


"Je suis le professeur dans la salle de classe et regarde autour de moi, en partie pour ne pas avoir à croiser les regards curieux de mes nouveaux camarades."


"C'est assez spacieux, le plafond est anormalement élevé et il y a beaucoup d'espace autour et entre les tables."


"Le mur entier est utilisé par des tableaux noirs, et les hautes fenêtres anciennes ne lui donnent qu'encore plus l'impression d'être démesuré."


"Les élèves ont pour table un bureau en bois standard avec une case pour les livres. Les chaises quant à elles sont en bois avec un cadre métallique. Simple et efficace."


"J'arrête ma marche en arrivant en face des autres élèves. Ils ont tous l'air normaux, comme des étudiants dans n'importe quelle autre école. Mais si c'était le cas, pourquoi seraient-ils ici ?"

scene ev hisao_class_move
with None


"Ils sont probablement comme moi et ont quelque chose qui ne va pas, simplement, cela ne se remarque pas au premier coup d'œil. Puis, je remarque que l'une des filles semble avoir un pouce manquant à la main droite. Ça brise un peu l'harmonie."


"Malgré la tendance naturelle à écouter quand quelqu'un parle de vous, je finis par ne plus écouter ce que dit le professeur alors qu'il me présente à la classe."


"Du coin de l'œil, je remarque que quelqu'un me regarde. C'est une fille avec des cheveux raides vraiment longs, ce qui attire le regard. Quand elle voit que je la regarde aussi, elle couvre son visage de ses mains comme si ça la rendait invisible."


"Il y a un garçon avec une canne, appuyé contre les casiers à l'arrière de la classe. C'est étrange de voir quelqu'un de si jeune avec une canne."


"Une autre fille semble faire quelques mouvements étranges avec ses mains. Langage des signes ? Elle me lorgne à travers ses lunettes, puis retourne à ce qu'elle faisait."


"Elle est plutôt mignonne. Il en va de même pour la fille toute joyeuse aux cheveux roses assise à côté d'elle. Elle est vraiment dure à louper ; je ne sais pas comment j'ai pu ne pas la remarquer en entrant..."


mu "...souhaitez la bienvenue à votre nouveau camarade."


"Il tape dans ses mains et tout le monde l'imite, exceptée une fille au premier rang qui n'a qu'une seule main. Je recule un peu, mais le cache en m'inclinant en remerciement aux applaudissements que je ne méritais pas."


label fr_A2a:


"Après les applaudissements, il y a un bref silence que personne ne souhaite briser."


"Le professeur se rend vite compte qu'il devrait probablement dire quelque chose. Il commence avec un bruit inintelligible, se tait comme s'il avait perdu son élan, puis commence à me présenter."


"Personne ne semble être vraiment intéressé."


"Peut-être que j'aurais dû dire oui au truc de la présentation."


"Réalisant probablement qu'il ne sait rien à mon sujet, il finit juste en prononçant encore une fois mal mon nom, et me demande de l'écrire au tableau."


"Je le fais, tournant le dos à la classe, me sentant gêné."


label fr_A2b:


"Un silence collectif m'informe que c'est à moi de parler, à présent."


hi "Donc... Je m'appelle Hisao Nakai."


"Et maintenant ?"


hi "Mes hobbies sont le foot et la lecture. J'espère pouvoir bien m'entendre avec tout le monde même si je suis nouveau ici."


"Et maintenant ?"


"Je suis tellement ennuyeux. Cette présentation ressemble à toutes les autres. Je devrais dire quelque chose de plus. Quelque chose de plus intéressant."


"Je finis par ne rien dire, et le professeur reprend à partir de là."


"Tout le monde semble être satisfait, même malgré le peu que j'ai dit. Quelques filles chuchotent entre elles, jetant des regards vers moi. Ça aurait pu être pire."


"..."


label fr_A2c:

scene ev hisao_class_end
with None


"J'écoute le professeur radoter à propos de la bonne entente, me laissant l'occasion de balayer la classe du regard."


"Tout le monde semble l'écouter attentivement et quand il a fini, ils applaudissent encore, ce qui me paraît être une réaction assez étrange."


"La fille du premier rang applaudit aussi, avec sa main contre son autre poignet qui se termine par un moignon bandé."


"Je me sens un peu mal à l'aise en voyant cela."

scene bg school_scienceroom at bgright
show muto normal at center
with fade


mu "Nous allons faire des travaux de groupes aujourd'hui, pour te donner une chance de parler avec tout le monde. Ça te va ?"


hi "Ouais, ça me va très bien."

show muto smile
with charachange


mu "C'est bien, tu peux travailler avec Hakamichi. C'est la déléguée de classe."


mu "Elle pourra répondre aux questions que tu te poses. Et qui d'autre pourrait faire ça mieux qu'elle, après tout ?"

hide muto
with charaexit


"Comment je pourrais le savoir ?"


"Le professeur donne les exercices du jour et annonce que nous allons travailler en groupes de trois."


"Il me vient à l'esprit que je ne sais pas qui est Hakamichi. Je suis lent à la détente. Le professeur semble se rendre compte de mon expression désemparée."


mu "Oh, c'est vrai. Hakamichi est là, Shizune Hakamichi."

show misha perky_smile at center
with charaenter


"Pendant qu'il dit son nom, la belle fille à l'air pétillant avec les cheveux roses et les yeux d'or pose sa main sur moi. Je m'assieds sur un siège à côté d'elle, près de la fenêtre."


hi "Hé, je suppose que tu es Hakamichi, n'est-ce pas ? Content de te rencontrer."

stop music fadeout 1.0

show misha cross_laugh
with charachange


mi_shi "Hahaha~ !"


"Hein ? Son rire me prend de court."

show misha hips_grin
with charachange


mi_shi "Contente de te rencontrer aussi !{w=0.5} Mais~ !"


mi_not_shi "Contente de te rencontrer aussi ! Mais~ !{fast}, je ne suis pas Hakamichi, Je suis Misha ! C'est elle Hakamichi. Shicchan~ !"

play music music_shizune fadein 1.0

show misha hips_grin at twoleft
show bg school_scienceroom at center
with charamove

show shizu basic_normal at tworight
with charaenter


"Riant, Misha pointe du doigt la fille à côté d'elle, celle que j'ai vue utiliser la langue des signes plus tôt. Il semble qu'elle m'ait regardé pendant tout ce temps. Elle hoche la tête avec nonchanlance pour montrer qu'elle m'a vu... mais à peine seulement."



"Elle a des cheveux courts mais bien brossés, une paire de lunettes de forme ovale en équilibre sur le bout de son nez délicat, et des yeux bleu foncé qui semblent alterner toutes les secondes entre l'analyse et l'ennui."


hi "Enchanté de faire ta connaissance."

show shizu behind_blank
with charachange


shi "..."

show misha perky_smile
with charachange

show misha sign_smile
with charachange

show misha perky_smile
with charachange


"Elle se tourne immédiatement vers Misha, qui sourit, et fait quelques gestes rapides avec les mains."

show shizu adjust_happy
with charachange

show shizu behind_smile
with charachange


"Hakamichi hoche la tête et fait quelques gestes à son tour."


"Je commence à me demander si le professeur se moquait de moi en disant des choses comme “tu seras en mesure de parler aux gens” et “qui pourrait mieux t'expliquer les choses”."

show misha hips_smile
with charachange


mi "Je peux voir que tu es un peu confus, hein ?, hein ? Mais, je comprends pourquoi tu croyais que j'étais Shicchan !"


mi "Shicchan est sourde, alors je suis la personne qui traduit les choses dans les deux sens pour elle."

show misha hips_grin
with charachange


mi "Je suis comme une interprète~ ! Elle dit qu'elle est contente de te rencontrer aussi !"

show shizu basic_normal2
with charachange


shi "..."

show misha perky_smile
with charachange


mi "Tu es le nouvel étudiant, n'est-ce pas ? Bah, Shicchan, bien sûr qu'il l'est ! S'il ne l'était pas, il aurait été debout là, sans aucune raison, hein ? Hein~ !"



label fr_A2d:


mi "Il a l'air d'être une personne très intéressante, pas vrai~ !"



label fr_A2e:


"Misha me regarde avec un air bizarre, puis continue."


mi "Nous ne savons pas beaucoup de choses à son propos, mais peut-être que nous en découvrirons plus tard."


"Peut-être que j'aurais dû me présenter, après tout. N'importe quoi d'autre aurait donné une meilleure première impression que le marmonnement du professeur, bafouillant mon nom."



label fr_A2f:


mi "Nous savions qu'il allait y avoir un nouvel élève, mais nous ne savions pas que tu serais ici aujourd'hui. Si rapidement ! Hicchan, hein ?"


"Hicchan... ?"

show misha hips_grin
with charachange


mi "Yup~ ! Ça te va bien, nan ?"


"Je l'ai dit à haute voix ? C'est surprenant. Je n'ai jamais aimé ce surnom."


hi "Je ne suis pas vraiment sûr..."

show misha cross_grin
with charachange


mi "Ça te va bien~ ! Tu es tout à fait comme je l'avais imaginé !"

show shizu adjust_smug
with charachange


shi "..."

show misha cross_laugh
show shizu adjust_happy
with charachange


mi "Hahahaha~ ! Ouais, tu ressembles tout à fait à un Hicchan !"


hi "Je me demande pourquoi tout le monde semble le penser..."


shi "..."


"Hakamichi tape ses doigts sur le bureau pour obtenir l'attention de Misha. Ses signes s'agitent dans tous les sens avec enthousiasme, et ses mains s'embrouillent un peu."

show shizu adjust_happy
with charachange

show misha sign_smile
with charachange

show shizu behind_smile
with charachange

show misha perky_confused
with charachange


"Misha semble un peu débordée."

show misha hips_grin
with charachange


mi "Ahaha~ ! Euh, désolée hein !"

show misha hips_smile
with charachange


mi "Shicchan veut que tu saches qu'elle est la déléguée de classe, donc si t'as besoin de savoir quoi que ce soit, tu peux lui demander sans aucun problème."

show shizu behind_blank
with charachange


shi "..."

show misha sign_smile
with charachange


mi "Tu te plais dans l'école jusqu'à présent ? On peut te faire visiter un peu si tu n'as pas eu le temps de te promener et de te...{w=0.5}{nw}"

show misha perky_smile:
    "misha perky_confused" with Dissolve(0.5, alpha=True)
with None


extend " familiariser ?{w=0.5}{nw}"

show misha perky_confused:
    "misha perky_smile" with Dissolve(0.5, alpha=True)
with None


extend " avec tout ça !"


"Misha trébuche un peu sur un mot compliqué, s'arrangeant tout de même pour que sa traduction reste fluide."


hi "Merci, ça serait plutôt utile. Ouais, je suis venu directement en classe aujourd'hui."


show shizu behind_frown
with charachange


shi "..."

show misha hips_laugh
with charachange


mi "Hahaha~ !"

show misha hips_smile
with charachange


mi "C'est pas bien ! Tu devrais toujours te renseigner le plus possible sur l'endroit où tu vas avant d'y être. Et pas seulement avec l'école, d'ailleurs~ !"

show misha hips_grin
with charachange


mi "Toujours ! Même si c'est une sortie à la supérette ! Hein, Shicchan ? Hahaha~ !"

show misha perky_smile
show shizu behind_smile
with charachange


"Se renseigner au sujet de l'endroit où on va ? J'imagine que je n'ai pas pris la peine de le faire, ou plus simplement, que cela ne m'intéressait pas vraiment."


"Je n'avais pas vraiment hâte d'y être, même si je m'étais décidé à venir en étant un minimum motivé, mais bon."


"Je ne dis rien, et les signes de Misha se terminent avec un haussement d'épaules. C'était quoi ça ? On dirait que c'était à mon propos."


"Je me sens m'affaisser sur mon siège. Toutes les deux sourient, mais ce haussement d'épaules m'a profondément touché, d'une façon inattendue."

show misha perky_sad
with charachange


mi "Tu as l'air déprimé, ça va ?"

show shizu basic_normal
with charachange


shi "..."

show misha perky_smile
with charachange


mi "Ne le prends pas mal, s'il te plaît~ ! Je déteste quand les gens ont peur de poser des questions ! C'est comme ça qu'on apprend, en demandant~ !"


mi "Demander de l'aide est parfaitement normal, tout comme en avoir besoin ! Fais pas cette tête, on dirait que tu viens de rater un examen !"

show misha cross_laugh
with charachange


mi "Wahahaha~ !"


hi "D'accord."

show shizu adjust_happy
with charachange


shi "..."

show misha perky_smile
with charachange


mi "Ah, autre chose, tu n'as pas besoin d'appeler Shicchan d'une façon aussi formelle que “Hakamichi” ou “déléguée” tout le temps ! Appelle-la juste Shicchan~ !"

stop music fadeout 0.5

show shizu adjust_blush
with charachange


shi "..."

show misha hips_smile
with charachange


mi "Ahaha~ ! Bon, c'est peut-être trop décontracté. Peut-être que “Shizune” serait plus approprié ?"

show shizu basic_normal2
with charachange


shi "..."

show misha hips_grin
with charachange

play music music_shizune fadein 5.0


mi "Yep, yep~ ! “Shizune” c'est bien !"


hi "Euh, d'accord, ce serait beaucoup plus facile pour moi."


"Je me sens beaucoup plus à l'aise. Elles sont vraiment amicales toutes les deux, je me sens un peu idiot de m'être autant inquiété plus tôt. Surtout pour Shizune, que je croyais beaucoup plus sérieuse."


"En fait, elle a toujours l'air aussi sérieux. Juste un peu moins que ce que je pensais."

show shizu behind_frown
with charachange


shi "... !"

show misha perky_confused
with charachange


mi "Hein ? Ah, oui, on n'a même pas touché à l'exercice ! On devrait commencer à travailler maintenant, sinon Shicchan va se fâcher."


hi "Il est plutôt long d'ailleurs, on devrait commencer tout de suite si on veut le finir avant la fin du cours."

show misha hips_laugh
with charachange


mi "Wahaha~ ! Ça aussi !"

show shizu basic_frown
with charachange


shi "..."


"Shizune nous fusille tous les deux du regard, impatiente. Je n'ai pas besoin de connaître le langage des signes pour comprendre."


hi "Ok, ok, j'ai compris le message."

show shizu basic_normal
with charachange


shi "..."

show misha perky_smile
with charachange


mi "Après les cours, on peut se promener dans le parc ensemble. Il fait bon aujourd'hui ! Hein~ ?"


"Le devoir est un vrai challenge, réussissant l'exploit d'être à la fois difficile et inutilement long."

stop music fadeout 6.0

scene bg school_scienceroom
with shorttimeskip


"Toutefois, nous le finissons quelques minutes avant tout le monde, en dépit du fait que nous ayons commencé tardivement. Shizune et Misha sont vraiment douées."


"Cependant, elles sont vraiment différentes. La déléguée est aussi calme et professionnelle qu'elle en a l'air, tandis que Misha est beaucoup plus joueuse et enfantine. Sans compter le fait qu'elle est facilement distraite."


"Pour être honnête, ce sont elles qui ont fait la plupart du travail. Je me sens coupable."

play sound sfx_normalbell


"Les cloches sonnent, signalant la fin du cours et l'heure du déjeuner."

scene bg school_hallway3
with locationchange


"Sans savoir ce que je suis censé faire, je suis Misha, qui me fait signe dans le couloir et descend les escaliers."




label fr_A3:

scene bg school_staircase2
with locationchange


"Nous descendons jusqu'au rez-de-chaussée, en dessous du hall où j'ai rencontré Mutou."

play ambient sfx_crowd_indoors fadein 6.0

scene bg school_cafeteria
with locationchange


"Comme tout le reste dans cette école, la cafétéria semble trop spacieuse et étrangement moderne, ce qui contraste avec la façade classique."


"Ses grandes fenêtres cintrées donnent sur la cour et la porte principale."

show misha hips_grin
with charachange

play music music_ease


mi "C'est la cafétéria~ !"


"Sa déclaration enthousiaste d'un fait évident fait que les gens autour de nous la dévisagent, mais Misha ne semble pas s'en préoccuper."

hide misha
with charaexit


"La liste des menus est assez longue, ce que je trouve bien jusqu'à ce que je me rende compte que beaucoup d'entre eux sont là pour les élèves qui ont besoin de régimes spéciaux."


"Fantastique. Cela me donne presque l'impression d'être de retour à l'hôpital et de manger des portions mesurées avec une précision scientifique pour répondre aux besoins des patients."


"Je prends quelque chose au hasard avant de suivre Shizune à une table et de m'asseoir en face d'elle."

show misha hips_frown at twoleft
show shizu basic_normal at tworight
with charaenter


"Pendant que je grignote indifféremment la nourriture que je préfèrerais ne pas manger, Misha me tapote pour attirer mon attention et pointe Shizune du doigt."

show misha perky_smile
show shizu basic_frown
with charachange


shi "..."


"Je ne comprends pas les signes, alors la raison m'échappe."


"Peut-être que regarder quelqu'un qui vous “parle” est convenable et poli ?"

show misha hips_smile
show shizu behind_blank
with charachange


mi "Tu veux savoir quelque chose ?"


hi "Hein ?"

show misha hips_grin
with charachange


mi "À propos de n'importe quoi ! Nous sommes tes guides alors pose-nous tes questions~ !"

label fr_choiceA3:
menu:
    with menueffect
    hi "Hmmm, je me demande..."
    "Poser des questions sur la bibliothèque.":




        return m1
    "Poser des questions sur la surdité de Shizune.":


        return m2
    "Je pense que je sais tout ce que j'ai besoin de savoir.":


        return m3

label fr_A3a:


hi "Oh, oui. Il y a une bibliothèque dans l'école ? Dernièrement, je lis beaucoup de livres et j'aimerais voir ceux qu'ils ont ici."


"Misha fait le genre de froncement de sourcils qui indique clairement qu'elle ne considère pas la lecture comme un loisir sain, puis reprend son sourire de nouveau."


mi "Il y en a une~ ! Elle est au deuxième étage, on pourra te la montrer plus tard !"


hi "Merci."


"Je retourne à mon repas tandis que les filles parlent entre elles."



label fr_A3b:


"Shizune m'intrigue, et j'ai pas mal envie de demander quelque chose à son sujet."


"Mais je ne peux pas demander quelque chose d'aussi personnel, pas vrai ?"


"Hum..."


"Je ne trouve rien d'autre à demander alors je me concentre sur ma nourriture pendant que les filles parlent entre elles."



label fr_A3c:


hi "Rien ne me vient à l'esprit, vraiment."

show misha sign_smile
with charachange


mi "Ooh ! Ça veut dire qu'on est de bons guides, pas vrai, pas vrai~ ?"


"..."


hi "Euh... on va dire ça."

show misha hips_grin
with charachange

show shizu behind_smile
with charachange


"Misha rayonne de joie, et Shizune aussi après une rapide traduction."


"Je secoue la tête face à leur enthousiasme un peu exagéré, et me concentre sur la nourriture."



label fr_A3d:


"Misha et Shizune font des signes dans tous les sens, en jetant des regards dans ma direction, mais Misha s'abstient de traduire."


"Peut-être qu'elles parlent de trucs de filles ou quelque chose du genre."


"..."

stop music fadeout 3.0
$ renpy.music.set_volume(1.0, .5, channel="ambient")
stop ambient fadeout 3.0


"Je remarque rapidement qu'une conversation en langage des signes n'est pas suffisante pour combler un silence."

scene bg school_scienceroom
with shorttimeskip

play music music_daily fadein 0.5


"Nous arrivons dans la salle de classe tôt, mais nous ne sommes pas les premiers."

show hanako emb_downtimid at Transform(xanchor=0.8, xpos=1.0)
with charaenter


"La fille aux cheveux noirs que j'avais remarquée plus tôt est affaissée sur son bureau au dernier rang."

show hanako defarms_shock
with vpunch

show hanako defarms_shock at Transform(xanchor=0.6, xpos=1.0)
with charamove


"Elle sursaute quand Misha arrive dans la classe avec l'élégance d'un rhinocéros."


"Elle se recroqueville encore plus dans son siège. Je peux sentir sa tension jusqu'ici, comme si elle se transformait lentement en pierre à cause de notre présence."


"Misha et Shizune ne le remarquent pas ou ne s'en occupent pas, elles marchent directement vers leurs chaises et commencent à discuter."

show hanako defarms_shock at offscreenright
with charamove

hide hanako
with None


"Je continue de m'inquiéter à son sujet, même lorsque la salle se remplit doucement avec les autres étudiants et finalement, le professeur."


"Rentrer dans le rythme scolaire est étrange ; c'est comme si mon cerveau se souvient du fonctionnement, mais pas mon corps."


"Vers la fin du cours, je commence à bâiller et à compter les minutes restantes."


"Je ne devrais pas être aussi fatigué dès mon premier jour d'école."


"C'est peut-être le temps passé à l'hôpital qui me fait ça. Je me sens encore sans vie et faible physiquement."

scene bg school_scienceroom
with shorttimeskip

play sound sfx_normalbell


"Après un moment, la cloche finale sonne."


"L'école est enfin terminée pour la journée."


"Près de moi, Misha et Shizune ont une courte conversation. Après délibération, Misha se tourne vers moi."

show shizu behind_blank at tworight
show misha perky_smile at twoleft
with charaenter


shi "..."


mi "Malheureusement, on ne peut pas rester et te faire visiter aujourd'hui, Hicchan. On doit se dépêcher d'ailleurs, il y a beaucoup de travail qui nous attend."

show shizu basic_normal2
with charachange




mi "Tu vas trouver tes aises ici, j'en suis sûre."


hi "Ah, attends ! Le professeur a dit que je devais aller voir l'infirmier. Où est-ce que je dois aller ?"

show shizu behind_smile
show misha hips_grin
with charachange


mi "Ah bon ? On peut te montrer le chemin si c'est juste ça~ !"


mi "Viens, les infirmiers ont leur propre bâtiment, donc on doit passer par l'extérieur."

hide shizu
hide misha
with charaexit

scene bg school_hallway3
with locationchange


"Nous nous mêlons aux étudiants sortant de classe avec, en tête, les filles qui suivent des élèves de classes supérieures qui sont dans le même couloir que nous."

scene bg school_courtyard
with locationskip


"Une fois que nous sommes à l'extérieur, les filles continuent leur chemin vers le plus petit bâtiment juste à côté de celui de l'école."


"Il est construit dans le même style, donc il donne l'impression de faire partie du bâtiment principal."

show shizu behind_smile at tworight
show misha perky_smile at twoleft
with charaenter


shi "..."


mi "C'est le bâtiment secondaire ici. Il y a un paquet de trucs importants et sérieux à l'intérieur, comme le bureau de la Fondation Yamaku et tous les bureaux des infirmiers. Ils ont même une piscine !"


hi "En quoi c'est sérieux ?"

show shizu behind_frustrated
with charachange


shi "..."

show misha hips_grin
with charachange


mi "Ne sois pas idiot Hicchan ! C'est pour la thérapie physique bien sûr."

show misha sign_smile
with charachange


mi "Quoi qu'il en soit, toutes les installations du personnel infirmier sont ici également. Le bureau du cadre infirmier est au premier étage."

show misha hips_smile
show shizu behind_smile
with charachange


mi "Tu t'en sortiras à partir d'ici, hein~ ? Alors on file ! À demain !"


hi "Ouais merci. Au revoir."

stop music fadeout 5.0

hide shizu
hide misha
with charaexit


"Un bâtiment entier pour des trucs qui n'ont rien à voir avec la scolarité ?"


"J'imagine que c'est nécessaire pour un endroit comme celui-ci."

scene bg school_nursehall
with locationchange


"Je rentre dans le bâtiment, espérant que ça ne sera vraiment qu'une visite rapide comme le professeur l'a dit."


"Sur une porte blanche à gauche, il y a une croix verte avec le texte “Infirmier en Chef” et une plaque avec un nom."

play sound sfx_doorknock2


"Une voix à l'intérieur me répond presque immédiatement après que j'aie frappé à la porte, mais je ne comprends pas ce qu'elle dit."


"Ça sonnait un peu comme une invitation à ouvrir la porte, alors je choisis d'entrer."

play sound sfx_dooropen

scene bg school_nurseoffice
with locationchange


"La pièce n'est pas grande et il y a une odeur bizarre, mais un homme qui semble amical se retourne sur sa chaise pour me faire face à l'instant où j'entre."


"Son bureau est propre et bien rangé, mais la poubelle sous la table déborde de matériel médical usagé et il y a au moins une douzaine de cercles de tasses de café éparpillés sur son bureau."

play music music_nurse fadein 0.5

show nurse neutral at center
with charaenter


nk_ "Bien le bonjour. Que puis-je faire pour toi aujourd'hui ?"


"Il semble jeune et sérieux, mais les fossettes de ses joues repoussent au loin cette impression quand il sourit."


hi "Hum, vous êtes l'infirmier ?"

show nurse grin
with charachange


"Il sourit comme une personne qui a entendu cette même question des centaines de fois."


nk_ "Mais oui, c'est moi. C'est écrit sur la porte, non ?"


nk_ "Tu peux m'appeler par mon nom ou juste “l'infirmier” comme tout le monde."


"Bien sûr. Je sors de ma confusion, réalisant que je devrais probablement saisir sa main tendue.{w} Sa poignée de main est plutôt ferme et amicale."


hi "Bien... euh, je suis le nouvel étudiant et mon professeur principal m'a dit de venir vous voir. Je m'appelle Hisao Nakai."

play sound sfx_snap


"Ses yeux s'illuminent à la révélation et il claque des doigts."

show nurse fabulous
with charachange


nk "Oh tu es CE Nakai. Je lisais justement ton dossier ce matin."


nk "Une forme d'arythmie chronique et une anomalie congénitales du muscle cardiaque, c'est ça ?"


"Il me fait signe de m'asseoir dans un fauteuil libre en face de son bureau."


hi "Euh, oui."

show nurse neutral
with charachange


nk "Bon. Eh bien, tu as probablement été suffisamment informé sur l'école, alors je vais être rapide."


nk "Nous avons toutes sortes d'installations disponibles, la plupart sont là pour des thérapies physiques, entre autres."


nk "Il y a toujours quelqu'un de mon équipe pas loin, même la nuit, alors n'hésite pas à nous appeler en cas de problème."


"La fameuse équipe d'infirmiers 24/24."


hi "Woaw, c'est comme un hôpital."


nk "Eh bien, pas exactement. Par exemple, nous ne faisons pas de neurochirurgie ici."


"Son rire semble tellement hors de propos que j'en reste à me demander pourquoi il a dit ça."


hi "Ouais... juste que c'est vraiment bizarre d'avoir autant de personnel médical dans une école."


nk "Tu vas t'y habituer."


"Je n'en suis pas aussi sûr moi-même, mais je vais laisser l'infirmier le croire."


nk "Maintenant, laisse-moi juste le temps de retrouver ton dossier..."


"Pendant qu'il cherche quelque chose sur son ordinateur et dans les piles de papiers mélangées, je laisse mon regard errer dans la pièce."


"C'est la quintessence de l'ordinaire, pourrais-je dire."


"Murs et plafond beiges, revêtement de sol stratifié gris foncé, et tous les équipements qu'on pourrait attendre d'un bureau d'infirmier scolaire."


"Même les ridicules posters éducatifs sont accrochés sur les quatre murs, me rappelant de manger correctement - trois fois par jour et de façon équilibrée."

show nurse grin
with charachange


"Souriant, l'infirmier tire un épais dossier à partir d'une pile de dossiers de même épaisseur et l'ouvre."


nk "Alors, tu as déjà des médicaments contre l'arythmie, n'oublie pas de prendre tes pilules matin et soir ou ça ne servira pas à grand-chose."

show nurse fabulous
with charachange


nk "À part ça... tu fais du sport ? Violent comme... je sais pas, la boxe ?"


"Il sourit à sa propre plaisanterie, mais pas moi."


hi "Euh, en fait, je jouais au foot de temps en temps avec quelques camarades de classe."


nk "Bon, je crains de devoir te recommander de t'abstenir d'en faire. Au moins pour le moment."




"Mon manque de réaction lui fait lever un sourcil, mais honnêtement, je ne suis pas trop dérangé par son interdiction de frapper dans un ballon."


"Je suppose que je n'ai jamais fait ça par grande passion pour le sport. Juste pour avoir quelque chose à faire."


nk "Tout type de choc peut être très dangereux pour ton cœur et prendre le risque d'avoir une autre attaque n'est pas une bonne idée."


nk "C'était la raison de ta première attaque ? Il n'y a aucune mention de la cause dans tes papiers."


hi "Euh... pas exactement."

show nurse concern
with charachange


"J'évite la question de manière habile, et il lance un regard sur ses papiers, avec une expression plus sérieuse sur son visage."


nk "Pour autant, tu as besoin de garder ton corps en bonne santé, donc faire un peu d'exercice te ferait du bien."


nk "Comme je l'ai dit, nous faisons de la thérapie physique ici, mais je ne pense pas que tu aies besoin de quelque chose d'aussi lourd."


nk "Juste quelques petits exercices régulièrement."


nk "De la marche rapide ou même un peu de jogging, du saut à la corde, ce genre de choses. La natation peut-être ? Il y a une piscine ici."


hi "On me l'a déjà dit."

show nurse neutral
with charachange


nk "Tu le savais ? Parfait."


nk "En tout cas, et je suis sûr qu'on t'a déjà dit tout cela auparavant, tu as juste besoin de faire attention à ne pas trop pousser."


"Il agite son doigt pour souligner ce point. Ce n'est pas très utile, j'ai déjà entendu ça des centaines de fois."

show nurse concern
with charachange


nk "Aucun risque inutile. Prends soin de toi."


hi "D'accord."


"Il passe le regard sur mes papiers une fois de plus, et les met sur le bureau, apparemment satisfait."

show nurse neutral
with charachange


nk "Bien. Ce sera tout, alors. Reviens me voir si tu as besoin de quelque chose."

scene bg school_nursehall
with locationchange

stop music fadeout 2.0


"Je suis ressorti avant même de m'en rendre compte. Une visite rapide, en effet."




label fr_A4:

scene bg school_courtyard
with locationchange

play music music_pearly fadein 4.0


"Je me tiens devant le bâtiment principal et le bâtiment auxiliaire même si, à mes yeux, ils semblent toujours être un seul et même."


"C'est le premier vrai regard que j'ai sur les autres étudiants, alors je regarde les gens sortir de l'école, en train de se diriger vers le portail ou les dortoirs."


"Chacun semble savoir où il doit aller."


"Et je continue de penser que la plupart d'entre eux n'ont pas l'air spécial pour des étudiants d'une école spéciale. De toute façon, moi non plus."


"Est-ce que ça fait de moi l'un d'entre eux ?{w} L'un d'entre nous ?"


"..."


"Je devrais aller quelque part aussi, pour éviter de me perdre."


"Il est presque l'heure de dîner, mais je me sens plus fatigué qu'affamé."


"La lassitude en moi ne fait que grandir alors que je m'avance lentement vers le dortoir, un peu à l'écart du complexe principal."

scene bg school_gardens
with locationchange


"Il y a une sorte de jardin entre l'école et le dortoir ; on y trouve des arbustes, des fleurs et cette odeur omniprésente de l'herbe fraîchement coupée qui emplit l'atmosphère."


"Dans la fatigue, il me vient à l'esprit que l'odeur me paraît aussi forte parce que je n'étais pas du tout sorti à l'extérieur depuis très longtemps."

scene bg school_dormext_start at bgleft
with locationchange


"Le bâtiment du dortoir est grand et fait de briques rouges. Il semble bien trop pompeux pour ce qu'il est, mais j'avance, me rendant à l'intérieur."

scene bg school_dormhallground
with locationchange


"Je prends plus de temps que nécessaire pour retrouver la clé que j'avais mise dans ma poche."


hi "Chambre cent dix-neuf..."


"Contrairement à son apparence extérieure, l'intérieur du dortoir est plutôt récent, fonctionnel, et quelconque."


"Tout comme le bâtiment principal, les halls et les portes sont assez larges pour les fauteuils roulants. Et cela est aussi valable pour les ascenseurs au bout des couloirs."


"Je passe ma tête par l'ouverture de la porte de la salle commune."


"À l'intérieur quelques étudiants regardent la télévision."


"L'un d'entre eux hoche la tête et me salue rapidement avant de reprendre son visionnage."


"On dirait que seules les filles sont sociables ici. Ça me convient parfaitement."


"Je prends l'escalier vers l'étage supérieur."

scene bg school_dormhallway
with locationchange


"Ici, le couloir principal se prolonge en plusieurs couloirs plus petits."


"Chacun de ces halls secondaires semble avoir des toilettes, des douches, ainsi que quatre chambres."


"À mi-chemin dans le hall, je trouve la chambre 119."


"Il n'y a pas de noms sur les plaques des chambres adjacentes à la mienne. J'imagine que nous sommes juste deux ici."

play sound sfx_doorknock2
stop music fadeout 3.0


"Il y a de la lumière sous la porte de la chambre 117, alors je frappe légèrement."


hi "Bonjour, il y a quelqu'un ?"


"De l'intérieur, j'entends un peu de mouvement, puis le cliquetis de plusieurs serrures ; je ne pensais pas que les portes en avaient autant. Après un moment, la porte s'ouvre en grinçant."

show kenji tsun at Slide(0.4,0.5,0.5,0.5,0.5)
with charaenter

play music music_kenji fadein 0.5


"Un garçon à lunettes est debout dans l'embrasure. Il me regarde très attentivement à travers ses lunettes très épaisses."


ke_ "Qui est-ce ?"


"Aveugle ? Non, du moins pas complètement, pourquoi porterait-il des lunettes s'il l'était ?"

show kenji tsun_close at center
with characlose


"Il se penche plus près de moi jusqu'à ce que nos nez se touchent presque. Son haleine pue l'ail."


hi "Hisao Nakai... J'emménage dans la chambre d'à côté. J'ai pensé que je devais me présenter..."

show kenji happy
with charadistant


"Son visage s'illumine tout à coup, et il se tient debout, revenant à une position normale, tendant sa main dans un salut souriant, presque directement à mon diaphragme."


ke_ "Oh, salut mec, j'suis Kenji."


hi "Ah, salut."


"Je prends la main moite de Kenji et la serre, toujours un peu ébranlé par le brusque changement d'attitude et son salut véhément."


ke "Il y a eu quelques personnes louches entrant et sortant de ta chambre tout à l'heure."


hi "C'était probablement mes parents."

show kenji tsun
with charachange


ke "Tes parents ? T'es sûr ? Parce qu'il aurait pu y avoir d'autres personnes, aussi. Tu ne peux pas juger un livre à sa couverture."


"Son proverbe, mal placé, est laissé maladroitement en suspens entre nous alors que j'essaye de trouver une autre façon de lui répondre."


hi "Je dirais que les chances sont assez élevées."


"Il frémit et fait quelques gestes exagérés."

show kenji neutral
with charachange


ke "T'es un mec brave, Hisao."

show kenji tsun
with charachange


ke "Moi, je ne pense pas que je pourrais me fier à la chance."


ke "Le seul en qui j'ai confiance, c'est moi."


hi "Est-ce que ça veut dire que je ne devrais pas te faire confiance non plus ?"


"Il réfléchit à ce sujet pendant un certain temps."

show kenji neutral
with charachange


ke "Une sage décision."

show kenji happy
with charachange


ke "Mince, tu es plus intelligent que tu ne le parais."


ke "Probablement."


ke "De quoi t'as l'air ? Pas intelligent, j'espère."

show kenji neutral_close
with characlose


"Il plisse les yeux et se penche plus près encore, mais je me penche en arrière pour l'esquiver."

show kenji tsun
with charadistant


ke "Tant pis, c'est pas grave."

hide kenji
with charaexit

stop music fadeout 3.0


"Après ça, il se tourne, tâtonne un moment à la recherche de la poignée de porte,{w=0.3}{nw}"

play sound sfx_doorslam


extend " et ferme la porte derrière lui."


"Je glisse la clé dans la serrure de la chambre 119."

scene bg school_dormhisao_ss
with locationchange

play music music_night fadein 1.0


"Sombres murs beiges, draps blancs, un bureau fait de bois léger. Des rideaux laids."


"Ça n'est la chambre de personne ; elle est impersonnelle, comme ma chambre d'hôpital l'était."


"Mes valises sont posées au pied du lit, et semblent plus vides qu'elles ne l'étaient ce matin."


"L'armoire est encore ouverte, remplie de mes vêtements."


"D'ailleurs, il semble qu'il y a un certain nombre d'uniformes scolaires, suspendus là aussi."


"Une note est épinglée sur la poche de l'une des chemises."

window hide


$ written_note("Salut Hicchan. Nous avons déballé tes affaires et fait ton lit.\nIls nous ont dit que si celles-ci ne vont pas, alors tu devras aller à l'accueil demain.\nSi tu as le moindre problème, tu peux toujours nous appeler.\n\nBisous, Maman et Papa")

window show


"Eh bien, au moins je n'ai pas à m'inquiéter à propos du déballage."


"J'aurais limite espéré devoir le faire moi-même, au moins ça m'aurait occupé."


"Il est encore trop tôt."


"Je pose la note sur le bureau et m'allonge sur le lit, me sentant vide."


"Être allongé ici me donne envie de lire quelque chose, mais je n'ai rien avec moi."


"Je me demande si l'hôpital m'a conditionné pour me donner envie de lire dès que je n'ai rien à faire."


"L'envie de lire m'angoisse jusqu'à ce que je me lève."


"Peut-être que c'est le stress ou un truc du genre."


"J'étais vraiment nerveux avant de venir, ainsi que toute la journée. Je le suis encore, je crois."


"Merde, j'ai besoin de me distraire d'une manière ou d'une autre, ça ne sera pas aussi anormal tout le temps."


"Demain, j'irai emprunter des livres à la bibliothèque."


"Ouais, je vais faire ça."


"Mais pour le moment..."

show pills:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)


"Les flacons de médicaments bien alignés sur ma table de nuit attirent mon regard."


"J'en choisis un et le secoue juste pour entendre le contenu, puis je lis l'étiquette de la pharmacie dessus."

window hide

show pills:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide pills
with None


$ written_note("Hisao Nakai\n\nDeux comprimés par jour pour rester en vie", quiet=True)

window show


"Ça ne dit pas vraiment ça, mais ça pourrait tout aussi bien."


"C'est un peu tordu, avoir une vie dépendant de produits chimiques comme ça. Ça me contrarie un peu, mais est-ce que j'ai le choix ?"


"Soupirant, je commence mon rituel quotidien : prendre le bon nombre de pilules de chaque flacon, en prenant soin de vérifier la posologie."


"..."


"Je m'allonge à nouveau, me sentant vide et incertain, et après ça je continue de regarder le blanc de ce plafond inconnu, pendant un long moment."

stop music fadeout 8.0

scene bg school_dormhisao_ni
with Dissolve(3.0)


"Il ne me semble pas plus familier, pas même après la tombée de la nuit et que de longues ombres s'étirent à travers ma chambre comme des doigts."


"Les draps me semblent un peu plus confortables et chaleureux, et sont comme un nid contre le froid ambiant."


"Bientôt, l'ombre ténébreuse du plafond lui donne le même aspect que tous les plafonds ont la nuit, et il devient la seule chose que je reconnais encore."


"La nuit me fait signe de dormir, et je sens la froideur de l'inconnu et la peur rampant le long de ma colonne vertébrale, une fois de plus."


"Je continue de dériver loin du monde que j'ai connu."

$ suppress_window_after_timeskip = True

scene black
with shuteye


return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
