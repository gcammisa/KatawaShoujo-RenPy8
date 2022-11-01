label fr_S17:

window hide None

scene bg school_hallway3
with locationchange

nvl clear
nvl show dissolve

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_normal fadein 3.0


n "\n\nLes jours suivants passent sans incident et avec une rapidité surprenante. Je ressens une motivation renouvelée d'apprendre la langue des signes. Il paraît que je suis doué pour ça, alors ça serait dommage de ne pas le faire, et perdre ce que j'ai appris serait encore plus inacceptable."


n "Les vacances d'été arrivent. Même si je croyais que le travail du conseil s'amenuiserait proportionnellement avec la léthargie que contracte ma classe, ça ne se passe pas comme ça. Chaque jour, je me retrouve noyé sous du travail de moins en moins important."


n "Malgré l'envie, je n'ai pas une seconde pour parler à Shizune ces jours-ci. Chaque fois que je la regarde, elle est plongée dans un livre de présence ou sous un tas de papiers qui ont besoin d’être vérifiés."


n "\n\nAujourd'hui, je me réveille tôt pour arriver à l'école avant tout le monde, espérant voir Shizune. Elle a l'habitude d'arriver tôt le matin, pour être plus ponctuelle que les autres. Malheureusement, je crois que je vais arriver plus tôt qu'elle."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

play sound sfx_doorclose

window show


"Entendre la porte du conseil des étudiants coulisser à ma droite m'indique que ce n'est pas le cas. J'imagine que je suis arrivé juste après elle."

play sound sfx_dooropen

scene bg school_council
with locationchange


"J'entre dans la pièce et tape sur l'épaule de Shizune pour avoir son attention."




show shizu behind_smile at center
with charaenter


"Peut-être qu'elle s'attend à une conversation, et que c'est pour ça qu'elle pose la brique de jus d'orange qu'elle tient dans la main."


ssh "Bonjour."


his "Où est ton autre moitié ?"

show shizu adjust_frown
with charachange


ssh "Nous sommes des personnes à part entière."


"En y pensant, c'est le genre de remarque qu'elles doivent souvent entendre. Je ne peux pas expliquer autrement le fait qu'elle m'ait répondu aussi rapidement."

show shizu basic_normal
with charachange


ssh "Tu es là tôt. C'est bien, tu peux m'aider avec certains papiers. Il faut les rendre aujourd'hui."


his "Je suis venu ici tôt spécifiquement pour te voir, sans avoir à travailler."

show shizu behind_smile
with charachange


ssh "Selon Misha, ce n'est pas nouveau le fait que tu viennes tôt."


his "Pour toi non plus."

show shizu adjust_happy
with charachange


ssh "Tu veux qu'on fasse une course pour savoir qui arrivera le plus tôt ?"


"Shizune ajuste ses lunettes nonchalamment, un geste qui montre à quel point elle peut être excitée par l'idée de rendre quelque chose de banal compétitif et sérieux."


his "Ce n'est pas une compétition. Je ne veux pas qu'on fasse la course."


"J'ai presque oublié la dernière partie, qui est la plus importante."

show shizu behind_smile
with charachange


ssh "...Bah, pas grave. Il reste trop de temps avant la fin des cours, ça me fatiguerait."


"Sur ce, Shizune reprend son jus de fruit et le finit. Je me demande si elle va essayer de jeter la brique dans la poubelle, mais elle ne le fait pas. En fait, elle semble se demander pourquoi j'ai l'air si déçu. Je ferais mieux de m'expliquer."


his "Je voulais parler. C'est bientôt les vacances, tu sais."


his "Et on devrait passer plus de temps ensemble de toute façon. Je pensais qu'on pourrait faire ça durant l'été."

show shizu adjust_blush
with charachange


"Le visage de Shizune devient aussi rouge que ce que le mien doit être, et elle ajuste ses lunettes, embarrassée. Elle recycle vraiment ce geste à toutes les sauces. Elle joint les doigts, choisissant ses prochains mots avec précaution."

show shizu basic_normal
with charachange


ssh "Tu veux dire, comme un rendez-vous ?"


his "Juste parce qu'on sort quelque part, ça devient un rendez-vous ?"

show shizu behind_blank
with charachange


ssh "C'est pas le cas ?"

show shizu adjust_frown
with charachange


ssh "Je veux que ce soit un rendez-vous."


his "Alors c'en est un."

show shizu basic_happy
with charachange


"Shizune claque ses mains ensemble, approuvant, avant d'ajouter une phrase :"

show shizu behind_blank
with charachange


ssh "Mais pas aujourd'hui."

show shizu basic_normal2
with charachange


ssh "Je pars une semaine pour rendre visite à ma famille."


"C'est une façon étrangement formelle de dire ça, et pour cette raison, je suis curieux."


"Peut-être que sa famille est du genre traditionnelle, vivant dans un grande et ancienne maison avec un petit cours d'eau et un étang à koï, et où tout le monde porte des kimono tout le temps."


"C'est peu probable, mais par moment, c'est drôle d'imaginer. Je me demande si Shizune apparaît calme et mature comme Lilly quand elle est avec sa famille."


"Je n'arrive pas à me l'imaginer, mais s'il y a une possibilité pour que ce soit vrai, alors je dois la voir."


his "Seulement une semaine ? Ils ne doivent pas être loin, alors."

show shizu behind_frustrated
with charachange


ssh "Bien sûr que non, ma famille est au Japon, après tout."


his "Ah bon..."

show shizu adjust_happy
with charachange


ssh "Ce n'est pas comme si tu pouvais venir avec moi. C'est ce que tu essayais de dire ?"


his "Pourquoi je ne peux pas ?"

show shizu basic_normal2
with charachange


ssh "Ce n'est pas quelque chose que tu apprécierais."


his "Tu ne le sais pas ça. Ça pourrait être fun."


his "Ah, j'ai presque oublié : tu n'as pas répondu à ma question. Tu y vas toute seule, ou Misha vient avec toi ? Ta famille connaît la langue des signes ?"

show shizu behind_blank
with charachange


ssh "Misha vient avec moi."


"La partie de la question à laquelle elle n'a pas répondu est celle qui en dit le plus."


"Si la famille de Shizune ne peut pas communiquer avec elle, je me demande comment a été son enfance. Elle a probablement tout noté sur un bloc-notes comme celui qu'elle transporte tout le temps et dont elle se sert occasionnellement."


"D'habitude, c'est quand Misha et moi ne sommes pas là qu'elle le sort. Je peux voir de loin qu'elle le sort en dernier recours, en grimaçant."


his "Si Misha y va, alors j'y vais aussi."

show shizu basic_normal
with charachange


ssh "Tu aimes Misha ?"


his "C'est pour le principe."


"Je me demande un instant si Shizune pourrait être jalouse, mais j'en doute. Elle affiche d'habitude ses émotions sur son visage, et je ne vois rien qui pourrait confirmer ma théorie."

show shizu adjust_frown
with charachange


ssh "Je crois que tu t'ennuies juste."

show shizu behind_smile
with charachange


ssh "C'est pas grave. D'accord, on ira tous ensemble. C'est ce que j’espérais de toute façon."

show shizu adjust_smug
with charachange


ssh "Tu ne peux pas sécher le Conseil des Étudiants aujourd'hui pour faire tes valises. Même si tu n'es juste prévenu que maintenant, ce n'est pas une excuse !"


his "Pas grave, j'ai pas grand-chose à préparer de toute façon."

show shizu basic_normal
with charachange


"Shizune s’arrête, les doigts immobiles pendant qu'elle réfléchit."

show shizu behind_blank
with charachange


ssh "Tu as dû être prévenu peu de temps avant d'arriver à l'école."




label fr_S17a:


"Elle se rappelle peut-être de la fois où Misha et elle sont rentrées dans ma chambre et ont eu un aperçu de mes flacons de pilules. C'était un moment gênant que j'aimerais oublier, et je n'aime pas m'en souvenir."


"La façon dont elle est hésitante sur le sujet me rend mal à l'aise."


label fr_S17x:


his "Oui. C'était une décision plus ou moins immédiate. Ça s'est passé mieux que ce que je pensais, cela dit."


"J’espère que Shizune ne continuera pas la conversation, et à grand mon soulagement, elle ne le fait pas."

show shizu adjust_happy
with charachange


ssh "Ma maison n'est pas dans un coin particulièrement beau de Saitama."

show shizu behind_smile
with charachange


ssh "Nous partirons tôt dans la matinée, alors sois prêt. On en parlera plus tard, d'accord ? Pour l'instant, ces feuilles ne se feront pas toute seules, et tu vas m'aider."

stop music fadeout 3.0

hide shizu
with charaexit


"Alors que Shizune retourne à son travail, m’entraînant avec elle, je crois qu'elle est presque, mais pas totalement, excitée de partir."

scene black
with dissolve



label fr_S18:

scene bg school_dormhallway
with locationchange

play music music_daily fadein 0.5


"Quand Shizune et Misha arrivent tôt le lendemain matin pour me prendre, elles sont habillées autrement qu'avec l'uniforme scolaire dans lequel j'ai l'habitude de les voir."

show shizu behind_blank_cas at center
with charaenter


"C'est logique, c'est les vacances après tout, mais quand même ; ce que porte Shizune est à la mode, presque trop pour un endroit calme comme Yamaku. Avec ce qu'elle portait à Tanabata, je commence à remarquer une tendance."


"Tous ses choix sont de bons goûts et matures, très bien pensés. Je me demande donc pourquoi elle est si immature."

show bg school_dormhallway at bgright
show shizu behind_blank_cas at tworight
with charamove

show misha perky_smile_cas at twoleft
with charaenter


"Au moins les vêtements de Misha reflètent bien qui elle est."

show shizu adjust_frown_cas
with charachange


ssh "Tu n'emportes pas grand-chose."


hi "Je te l'avais dit. Je n'ai pas grand-chose à prendre."

show shizu basic_frown_cas
with charachange


"Shizune fait la moue et tapote du pied sa pile de sacs comme si elle était embarrassée. Misha a seulement une valise avec elle, mais elle est presque plus grande qu'elle. Elle semble s'en rendre compte aussi."


"Sérieux, cette valise est aussi grosse qu'une voiture compactée. La couleur vert petit pois est troublante aussi. On dirait quelque chose utilisé pour transporter des corps. À les voir comme ça, j'ai envie de les embêter un peu."


hi "Aw, dommage pour Misha et toi, hein ? Devoir porter ces gros sacs. Prenez plus léger la prochaine fois, comme moi. Tout rentre dans une seule petite valise."

show misha hips_grin_cas
with charachange


mi "Comme James Bond~ !"


hi "Oui, exactement comme James Bond."

show shizu adjust_frown_cas
with charachange

shi "…"


"Shizune redresse un peu ses lunettes en se concentrant."

show shizu basic_normal_cas
with charachange


ssh "On devrait diviser ce qu'il y a à porter en trois."

show misha sign_smile_cas
with charachange


mi "Wow~ ! C'est une super idée, Shicchan~ !"


hi "Quoi ? Non."

show shizu adjust_smug_cas
with charachange


ssh "C'est bien pour tout le monde."

show misha cross_laugh_cas
with charachange


mi "Yep~! Wahaha~ !"


hi "Je vais devoir vous dire non."

show shizu cross_angry_cas
with charachange


ssh "Deux contre un !"


"Elle se jette presque en avant en signant ça. Terrifiant."


hi "Bah, je rigolais juste. Ça ne me gêne pas. Je pensais juste que ça serait drôle de vous embêter."


hi "Mais si vous aviez essayé de tout me faire porter, j'aurais descendu la montagne avec la grande valise verte comme luge."

show shizu adjust_smug_cas
with charachange

shi "…"


"Ça semble faire rire Shizune, et elle met une main devant sa bouche pour se retenir. C'est comme si elle le cachait. Je me demande si elle peut rire. Si elle ne peut pas, ça explique peut-être pourquoi elle fait ça. Ça me rend un peu triste."

stop music fadeout 3.0

scene bg city_station
with locationskip


"Ayant fini de nous occuper de ça, nous nous dirigeons vers la gare, et un voyage sans évènement s'ensuit. Shizune et Misha arrivent à s'endormir presque instantanément, mais personnellement, je n'y arrive pas. Peut-être à cause de mes médicaments."

scene bg shizu_houseext
with shorttimeskip

play music music_soothing fadein 0.5


"Quand nous arrivons à la maison de Shizune, c'est bien plus grand que ce que j'aurais imaginé. Je crois que la dire énorme ne serait pas exagéré."


hi "Tu vis dans un manoir ?"

show shizu cross_angry_cas at center
with charaenter


"Shizune, indignée, se met sur la pointe des pieds pour qu'on soit à la même taille et fronce fortement les sourcils après que mon commentaire ait été traduit par Misha. C'est comme pour dire “comment peux-tu dire une telle chose ?”"

show shizu basic_frown_cas
with charachange


ssh "C'est juste une maison normale. Rien d'extravagant comme un manoir."


"Je crois que nos définitions divergent quelque peu, alors."

show bg shizu_houseext at bgright
show shizu basic_frown_cas at tworight
with charamove

show misha hips_grin_cas at twoleft
with charaenter


mi "Wahaha~. Hicchan, tu es surpris ? Tu veux que je te montre où tu seras ?"

show shizu behind_blank_cas
with charachange


ssh "Je crois que nous avons une chambre d'ami, mais je ne sais pas si nous en avons deux. Je vérifierai."

show misha sign_smile_cas
with charachange


mi "Mh~, ce n'est pas un problème, Hicchan~ ! Shicchan et moi pouvons partager une chambre s'il le faut. Bon~ sauf si la sienne est déjà utilisée pour autre chose."

hide shizu
with charaexit

hide misha
with charaexit

stop music fadeout 5.0


" “Je ne sais pas ?” Je commence à croire que Shizune ne passe pas beaucoup de temps chez elle. Avant que je ne puisse faire une blague, Shizune disparaît dans la maison, et Misha part avec elle, me laissant seul dehors."


"Je ne veux pas les suivre à l'intérieur. Je pose mon sac devant la porte et profite de l'opportunité pour voir les alentours, faire juste un tour de la maison."

show hideaki bored at center
with shorttimeskip


"Même si cela ne me prend que quelques minutes, quand je reviens, mon sac a disparu et une petite fille est là à sa place. Elle ressemble beaucoup à Shizune, même si Shizune ne porterait pas un short rouge et des chaussettes comme ça."


hi "Salut ! Tu es la petite sœur de Shizune ou quelque chose comme ça ?"

show hideaki normal
with charachange


hh "Non, je suis son petit frère. Mon nom est Hideaki."

show hideaki thinking
with charachange


hh "Heureux de te rencontrer."

play music music_happiness fadein 2.0


"La voix avec laquelle il me répond est directe, monotone, et définitivement masculine. Je me sens embarrassé au point que je pourrais presque tourner les talons et partir sur le champ, si je pouvais me rappeler le chemin vers la gare."

show hideaki serious
with charachange


hh "Tu es la deuxième personne que ma sœur a emmenée avec elle ?"


hi "“Emmenée avec elle” ? Je ne suis pas une valise."


hi "Bref, je suis Hisao. Tu as pris mon sac ?"

show hideaki triangle
with charachange


hh "Oui, il est de mon droit de garder tout ce que je trouve sur ma propriété."


hi "Non, c'est faux. Ce n'est pas du tout comme ça que ça marche."


"J'imagine que même les enfants qui parlent bien croient en la loi du trouvé-gardé. Même si je dis que c'est un enfant, il ne semble pas beaucoup plus jeune que moi, peut-être deux ou trois ans au mieux."

show hideaki normal
with charachange


hh "Je l'ai donné à Shizune. Il est à l'intérieur. Tu es du Conseil des Étudiants ?"


hi "Oui, comment tu l'as su ? Elle le mentionne souvent ?"


"J'ai failli dire “elle en parle souvent ?” Ça aurait pu mal tourner."

show hideaki bored
with charachange


hh "Oui, tout le temps. Tu t'entends bien avec elle ?"


hi "Bien m'entendre ? C'est une drôle de question. Je ne serais pas dans le Conseil des Étudiants si je ne m'entendais pas avec elle. Et vous deux, vous vous entendez bien ?"


"Même s'il a une voix monotone, son visage est aussi expressif que celui de Shizune, et trahit ce qu'il ressent vraiment. Ça doit être de famille. On dirait qu'il n'apprécie pas ma question, pour je ne sais quelle raison."

show hideaki thinking
with charachange


hh "Je suis désolé, je demandais juste parce que vous agissez de la même manière."


"Je ne sais pas pourquoi, mais j'ai l'impression qu'il me taquine. Malheureusement, ça marche. Je n'aime pas être comparé à Shizune."


hi "Tu ressembles beaucoup à Shizune, mais c'est normal. J'ai même cru que tu étais sa petite sœur. Si tu ne veux pas que les gens se trompent, tu devrais t'habiller de manière plus appropriée."

show hideaki confused
with charachange


hh "Je ne comprends pas, mes vêtements sont parfaitement normaux."


hi "Et les chaussettes ?"

show hideaki angry_up
with charachange


hh "Elles sont cool."

show hideaki disapproves
with charachange


hh "Tu agis comme ma sœur. Au bout d'un moment les gens finiront par te confondre avec elle."


"Je crois que mon commentaire a fait plus de dégâts que je le croyais. Ça expliquerait pourquoi il essaye de regagner l'avantage."


hi "Je déteste être comparé à d'autres personnes."

show hideaki evil
with charachange


hh "Shizune non plus n'aime pas quand elle est comparée."


"Je croyais que Hideaki était un peu plus mature que Shizune, mais ils ont le même esprit de compétitivité et cette manière de provoquer les gens. Je me demande s'il est comme ça à cause de Shizune, ou si c'est l'inverse."


hi "Et toi non plus, hein ? D'accord, j'ai compris. Je ne devrais plus agir comme un gosse."

show hideaki normal
with charachange

stop music fadeout 4.0


"Surtout avec les enfants. Hideaki semble prendre ça comme un aveu de défaite, et je ne peux pas laisser passer ça. Néanmoins, je dois désamorcer cela pendant que j'en ai la chance."

scene bg shizu_living
with locationchange


"Je peux entendre le rire de Misha résonner dans les couloirs dès le moment où je franchis la porte de la maison, et le suit jusqu’à ce que j'arrive dans ce que je crois être le salon. Il y a plus de monde que ce que je pensais."

show lilly basic_displeased_cas:
    center
    ypos 1.17 xpos 0.55
show akira basic_boo:
    tworight
    ypos 1.15 xpos 0.72
show hideaki bored:
    center
    xpos 0.92
    easein 1.0 ypos 1.1
show shizu behind_blank_cas:
    twoleft
    ypos 1.11 xpos 0.27
show misha perky_smile_cas:
    center
    ypos 1.1 xpos 0.08
with charaenter

play music music_another fadein 4.0


"Parmi ces personnes, je remarque une queue de cheval blonde qui m'est familière. Je suis plus confus que surpris de pourquoi Lilly est là. Shizune semble être tout aussi surprise. Lilly ne semble pas ravie non plus de cette situation."


"Assise à côté de Lilly se trouve une grande femme androgyne avec un costume. J'aimerais pouvoir dire que c'est sa grande sœur, mais je ne veux pas prendre ce risque."

show lilly basic_listen_cas
with charachange


li "Je ne m'attendais pas à ce que vous arriviez si tôt."


"Au début je crois qu'elle s'adresse à moi, mais elle parle à Shizune. Je ne crois pas que Lilly ait remarqué ma présence. Je suis apparemment arrivé au milieu d'une conversation, et vu qu'elle est concentrée sur Shizune, elle n'a pas pu m'entendre."

show shizu basic_frown_cas
with charachange


ssh "J'aurais dû réorganiser entièrement mon emploi du temps pour toi."

show misha sign_smile_cas
with charachange


mi "Shicchan dit : J'aurais dû réorganiser mon emploi du temps juste pour toi~ !"

show lilly basic_displeased_cas
with charachange


li "Ça aurait été bien, mais je n'aurais pas espéré que tu fasses une telle chose."

show misha hips_smile_cas
with charachange


mi "Oh, salut Hicchan~ ! Tu es enfin là."


hi "Ouais. Salut Lilly."

show lilly basic_surprised_cas
with charachange


li "Oh, Hisao ? C'est une surprise. Akira, voici Hisao, il est dans mon école. Hisao, voici Akira, ma sœur."

show akira basic_smile
with charachange

aki "Yo."


"Elle lève une main d'un geste bref et décontracté en guise de salutation. Donc elle est bien sa grande sœur après tout."

show akira basic_boo
show lilly basic_weaksmile_cas
with charachange


aki "J’espère que nous ne gênons pas tes plans. Vu que nous ne serons là qu'une journée encore, on s'est dit que Lilly pourrait tout autant venir avec moi."


"Akira se tourne vers moi, comme si elle se sentait obligée d'expliquer. J'en suis reconnaissant."

show akira basic_ending
with charachange


aki "J'imagine qu'on pourrait dire que je joue le rôle de baby-sitter."

show hideaki disapproves
with charachange


"Akira ébouriffe les cheveux de Hideaki tandis qu'il continue de paraître mécontent."


hh "C'est humiliant."

show akira basic_smile
with charachange


aki "Vraiment ? Peut-être que je ne dirai plus ça quand tu auras quelques années de plus. Ou du moins quelques centimètres."


"Elles forment une paire intéressante, bien qu'Akira ressemble plus à un avocat qu'à une baby-sitter. Je ne sais toujours pas vraiment pourquoi Lilly et elle sont là, cela dit."


"Jetant un œil à la pièce, il y a des raquettes de tennis, des clubs de golf, et même quelques cannes et articles de pêche."


"Derrière chaque chaise, dans chaque coin, et sous chaque table il y a un équipement de sport d'extérieur. Je ramasse une des cannes à pêche et joue avec."


hi "C'est une jolie maison."


hi "Shizune, on dirait que ton père a beaucoup de hobbies."

show misha sign_smile_cas
with charachange

show misha perky_smile_cas
with charachange


"Pendant un moment j'oublie de signer ce que je dis, mais Misha interprète ce que je dis pour elle. Je suis toujours impressionné par l'automatisme qu'elle a."

show hideaki normal
with charachange


hh "Tu pêches ?"


hi "Non, je ne sais pas faire. J'aimerais bien apprendre, vu que j'ai du mal à me détendre."

show shizu behind_blank_cas
with charachange


ssh "Il y a une rivière un peu plus loin, toute ma famille sait comment pêcher. Si tu veux, on pourrait y aller un jour."

show akira basic_laugh
with charachange


aki "Hideaki et toi savez pêcher ? Je ne m'attendais pas à ça de la part de gens de votre âge, vu que c'est surtout un hobby pour les vieux."

show akira basic_ending
with charachange


aki "T'sais, Lilly est une bonne cuisinière. Si on avait du poisson frais..."


"Ce n'est pas dur de savoir où Akira veut en venir."

show lilly basic_displeased_cas
with charachange


li "Si tu veux manger du poisson, on peut aller en acheter."


"La voix de Lilly semble légèrement plus autoritaire que d'habitude. Elle ne semble vraiment pas partager l'enthousiasme de sa sœur à cette idée."

show shizu basic_happy_cas
with charachange

shi "…"

show misha hips_grin_cas
with charachange


mi "C'est plus drôle d'aller pêcher ; on pourrait même faire un jeu et voir qui capture le plus gros~ ! Ça serait bien, hein ? Ouais~ ! Hicchan, qu'est-ce que tu en penses ? Ça semble fun, non ?"


hi "Ouais, c'est vrai."

show akira basic_smile
with charachange


aki "Ça me semble bien. Je ne sais pas pêcher non plus, donc c'est une bonne occasion pour apprendre."

show akira basic_boo
with charachange


"Ses yeux partent en direction de Lilly, qui ne bouge pas. Ça affaiblit un peu le sourire d'Akira, et je me demande pourquoi Lilly est si obstinée avec ça."

show hideaki normal
with charachange


hh "Je ne crois pas qu'on ait suffisamment de cannes à pêche pour tout le monde."

show shizu behind_smile_cas
with charachange


ssh "On peut faire chacun son tour. Ça sera un concours par équipe."

show hideaki confused
with charachange


hh "Qu'est-ce qu'elle dit ?"


hi "Qu'on peut pêcher chacun notre tour. Elle veut aussi qu'on fasse une compétition."

show akira basic_laugh
with charachange


aki "Allez Lilly, ça sera drôle."

show akira basic_boo
with charachange


aki "Donc, ce sera le concours de celui qui pêche le plus gros poisson ou le plus grand nombre ?"

show shizu adjust_smug_cas
with charachange


ssh "On dirait que la grande sœur comprend mieux que la petite, comme toujours."

show shizu basic_normal_cas
with charachange

shi "…"

show misha sign_smile_cas
with charachange


mi "Shicchan dit que Lilly préfèrerait aller faire les magasins, hein~ ? C'est beaucoup moins de travail, donc c'est normal qu'elle préfère ! Aller pêcher sera plus amusant cela dit, et économisera de l'argent. Akira, tu as eu une bonne idée~ !"

show akira basic_smile
with charachange


"Akira affiche un sourire gracieux quoique légèrement gêné.  La féliciter n'était pas le but de Shizune, après tout."

show lilly basic_sleepy_cas
with charachange

li "…"

show lilly basic_weaksmile_cas
with charachange


li "La rivière n'est pas un peu loin ?"

show akira basic_ending
with charachange


aki "Je ne crois pas qu'elle soit si loin, et je peux conduire s'il le faut. Ça me va, tant que vous attrapez quelque chose."


hi "Ta voiture peut contenir autant de personnes, et tout un arsenal d'équipements de pêche en plus de ça ?"

show akira basic_boo
with charachange


"Elle plisse les lèvres tandis que son doigt bouge subtilement, comptant le nombre de passagers et la cargaison requise. Si elle doit emmener Shizune, Misha, Lilly, Akira, Hideaki et moi..."

show akira basic_lost
with charachange


aki "Six personnes. Zut, je n'ai que cinq places."

show akira basic_ending
with charachange


aki "En fait, si Hideaki s'assoit sur mes genoux, nous pourrions—"

show hideaki angry_up
with charachange


hh "Je ne m’assiérai pas sur tes genoux."

show akira basic_resigned
with charachange

aki "Aw."

show shizu adjust_happy_cas
with charachange

shi "…"

show misha hips_smile_cas
with charachange


mi "Shicchan dit que la voiture de son père serait suffisamment grande."

show akira basic_lost
with charachange


aki "Quoi, la Fuga ? Si ça ne le gêne pas, alors on n'a pas d'autre choix. C'est dommage quand même qu'on ne prenne pas ma voiture, vu que je ne l'aurai plus pour très longtemps."


"Malgré l'obstination de Lilly et de Hideaki à propos de si nous ne préférons pas manger avant de parier sur des poissons que nous n'attraperons peut-être pas, il est impossible de dissuader Akira et Shizune."

stop music fadeout 5.0

scene ev shizune_car
with shorttimeskip

play ambient sfx_businterior fadein 1.0


"Mes attentes d'une virée quelque peu relaxante dans la campagne sont satisfaites. La conduite de Akira est aussi fluide et calme que les environs, tellement que Misha s'endort durant le trajet."


"J'aurais cru que le voyage serait trop lent pour Shizune, mais elle semble apprécier aussi. Même si Hideaki est bizarrement écrasé entre elle et la porte, elle continue de regarder par la fenêtre et sourire."

stop ambient fadeout 0.5

scene bg shizu_fishing at left
with shorttimeskip

play ambient sfx_parkambience fadein 0.5


"Les environs autour de la rivière sont vraiment beaux. Akira et Shizune se précipitent tellement vite à la rivière que nous n'avons pas d'autre choix que de les poursuivre. Nous serions laissés derrière sinon."

show lilly basic_weaksmile_cas at left
show hideaki bored at center
show misha hips_grin_cas at right
with charaenter


"Je peux voir Hideaki et Lilly en train d'essayer de calmer leurs sœurs respectives. Lilly semble quand même assez enthousiaste. Misha est aussi joyeuse que toujours. On dirait qu'elle a réussi à s'approprier quelque peu l'excitation de Shizune et Akira."


"Quant à moi, je préférerais manger maintenant, mais la pensée de poisson frais préparé par Lilly est attrayante."


"La rivière est plus grande que ce que j'aurais cru et surtout, paisible."


"Outre la petite jetée apparemment construite juste pour pêcher, cet endroit semble épargné par la civilisation. Ça me fait réaliser à quel point j'ai vu beaucoup d'espaces verts récemment."

show shizu invis at offscreenright
show akira invis:
    center
    xpos 1.5
with None

show bg shizu_fishing at right
show lilly invis at Position(xpos=-0.6)
show hideaki invis at offscreenleft
show misha perky_confused_cas at left
show shizu basic_happy_cas:
    center

    xpos 0.37
show akira basic_smile:
    center
    xpos 0.8
with Dissolvemove(1.5)


"Shizune s'écarte un peu avec Misha pour expliquer à Akira comment pêcher. Lilly et Hideaki parlent entre eux, donc je décide de rejoindre le trio enthousiaste."

show akira basic_ending
with charachange


aki "Mmh... donc lequel de ces leurres dois-je utiliser ? Je peux utiliser le petit mignon ?"

show shizu basic_frown_cas
show misha sign_smile_cas
with charachange


mi "Attends, attends~ ! C'est une compétition, on doit choisir les équipes d'abord ! Shicchan et moi serons dans la même équipe, bien sûr. Hicchan, tu seras dans notre équipe, hein ? On peut être l'équipe du Conseil des Étudiants~ !"


hi "D'accord."

show akira basic_laugh
with charachange


aki "Bon alors, ça fait Hideaki, Lilly et moi dans l'autre équipe. Lilly, comment est-ce que nous devrions nous appeler ?"

stop music fadeout 2.0

play sound sfx_flash

show bg shizu_fishing at left
show lilly basic_sleepy_cas at twoleft
show hideaki bored at tworight
show misha invis at Position(xpos=0.85)
show shizu invis at offscreenright
show akira invis:
    center
    xpos 1.5
with Dissolvemove(0.5)


$ doublespeak (li, hh, "Je ne vois pas en quoi c'est important.", "C'est pas important.")

play sound sfx_flash

show bg shizu_fishing at right
show lilly invis at Position(xpos=-0.6)
show hideaki invis at offscreenleft
show misha perky_confused_cas at left
show shizu basic_angry_cas:
    center
    xpos 0.37
show akira basic_ending:
    center
    xpos 0.8
with Dissolvemove(0.5)

show akira basic_lost
with charachange


aki "Alors ça sera l'équipe Sans-Enthousiasme..."

play music music_comedy fadein 0.5


"Encore une fois, les efforts d'Akira sont repoussés. Shizune et Misha, quant à elles, sont tout ce qu'il y a de plus enthousiastes."

show misha hips_smile_cas
show shizu behind_frown_cas
with charachange


ssh "Hisao ! Tu seras notre champion, attrapes-en le plus possible, ou le plus gros."


hi "Pourquoi moi ? Personne ne m'a appris à pêcher encore."

show misha hips_grin_cas
show shizu behind_blank_cas
with charachange


mi "On peut faire ça tout de suite~."


"Après un tutoriel rapide, Shizune essaye immédiatement de nous entraîner dans une discussion sur la stratégie à adopter pour la compétition de pêche."


"Cela dit, la compétition dans un sport qui consiste à rester assis des heures en espérant qu'un poisson morde le ver, ne semble pas particulièrement féroce."

show shizu adjust_happy_cas
with charachange


ssh "On dirait que Hideaki se retrouve avec la canne improvisée. Tu sais que c'est juste un câble enroulé autour d'un bambou, hein ? Tu te retrouveras contre lui alors, Hisao."


hi "Hein, pourquoi moi ?"

show misha sign_smile_cas
with charachange


mi "Tu es celui qui a le moins d'expérience ici, Hicchan~."


hi "Ah ouais ? Donc qui est le meilleur ici ? Shizune ? Hideaki est ton frère, il est probablement aussi bon. Il pêche sûrement tout le temps, vu qu'il vit près d'un lac. Il est peut-être même meilleur."

show akira basic_annoyed
with charachange


aki "Vous voir tous les trois me fait mal à la tête. Tu sais que je n'entends que deux tiers de la conversation, hein ? C'est quoi le sujet ?"


hi "On choisit les équipes."


"Akira semble troublée. Elle devient impatiente, ce qui est compréhensible."

show shizu basic_sparkle_cas
with charachange


ssh "Si tu es impatiente, ça me motive encore plus. Maintenant je veux augmenter les enjeux."

show akira basic_lost
with charachange


aki "Qu'est-ce qu'elle dit ?"


hi "Elle veut augmenter les enjeux."

show akira basic_laugh
with charachange


aki "Ne sois pas si hâtive. Nous avons la chance du débutant fois deux de notre côté, après tout. La seule façon que tu aurais de gagner serait de pêcher un océan entier."

show shizu adjust_happy_cas
with charachange

shi "…"

show misha hips_grin_cas
with charachange


mi "C'est de l'eau douce, espèce de biologiste marine~."


"Une étrange insulte accompagnée d'innocence. Akira ne semble pas embêtée. Elle rit, et Shizune reprend son attitude espiègle. Je suis content qu'elles s'entendent bien."

show akira basic_smile
with charachange


aki "Bon, on pêche ou quoi ? J'ai faim..."

show shizu basic_normal_cas
with charachange


ssh "Hisao, Misha et moi sommes dans une équipe, et Lilly, Hideaki et toi êtes dans l'autre, non ?"

show akira basic_ending
with charachange


aki "J'imagine que c'est le plus logique. Quoique mélanger un peu ne serait-il pas plus amusant ? Hein ?"

show misha perky_smile_cas
with charachange


mi "Mmh~, tu ne veux pas pêcher avec ta propre sœur ?"

show akira basic_boo
with charachange


aki "Bah, aucune de nous deux ne sait pêcher, donc nous mettre ensemble est quelque peu..."


"On dirait que je viens d'entendre une information dangereuse. J'essaye de changer de sujet avant que Shizune puisse s'en servir comme une arme."


hi "Donc, j'imagine que Shizune et toi vous connaissez déjà ?"

show akira basic_smile
with charachange


aki "Bien sûr. Depuis longtemps."

show shizu basic_normal2_cas
with charachange


"Akira sourit à Shizune. Ce n'est qu’après que Misha ait fini de traduire que Shizune affiche une expression troublée."


"Akira est bien différente de Lilly. À part son apparence, elle est beaucoup plus familière et détendue. J'attendais de la part de la famille de Lilly le même niveau de formalité qu'elle, donc c'est une surprise. Mais c'est facile de lui parler."


show akira basic_laugh
with charachange


aki "Même si j'aime beaucoup parler de la pêche, j'aimerais bien m'y mettre un de ces jours."

show shizu behind_blank_cas
with charachange


ssh "Tu suggères qu'on fasse chacun notre tour, comme au baseball ? Ou tous à la fois ? Ou comme dans un tag battle ?"

show shizu basic_sparkle_cas
with charachange


ssh "Est-ce qu'on peut s'asseoir où on veut, ou est-ce que les équipes doivent rester ensemble ? On doit le dire quand on a une touche ? Quelle taille de poisson compte ?"

show akira basic_lost
with charachange


"Voyant Akira faire une grimace après que Misha ait fini de traduire, Shizune tripote ses lunettes, riant silencieusement."

show shizu adjust_happy_cas
with charachange

stop music fadeout 4.0


ssh "Peu importe. Allons juste pêcher."

show shizu behind_smile_cas
with charachange


ssh "Ça peut être une compétition individuelle."

stop ambient fadeout 2.0

scene ev shizu_fishing_ah
with shorttimeskip

play music music_ease


"Je m'assois, prêt à pêcher, bien que je ne me sente pas très confiant. Tout le monde est déjà assis, sauf Akira, qui se met à côté de moi et jette sa ligne après avoir enlevé sa veste et remonté ses manches."


"Misha et Hideaki finissent au bout du lac et pêchent ensemble, comme il n'y a pas assez de place pour tout le monde sur la jetée. Pour dire vrai, je préférerais être assis à côté de Shizune, mais Akira semble sympa aussi."


aki "Fais attention, tu es un peu proche. N'emmêle pas nos lignes, d'accord ?"


hi "Donc, tu as déjà pêché auparavant ?"


aki "Non, mais j'ai déjà vu à la télé. J'ai toujours voulu attraper un de ces gros poissons avec un museau en forme d'épée. Un marlin je crois."


li "Si je me rappelle bien, ils sont dans les océans, poissons d'eau de mer."


aki "Je le sais ça. Pourquoi est-ce que tout le monde agit comme si je ne connaissais pas la différence entre l'eau douce et l'eau salée ?"


li "Si tu ne fais pas attention, tu effrayeras les poissons, eau salée ou non."


"La voix d'Akira est quelque peu forte tandis qu'elle embête Shizune et amuse Lilly à la fois, donc elle a peut-être raison. Ma ligne ne semble pas attirer quoi que ce soit, mais je ne sais pas à quel point Akira en est fautive."


"Shizune fait de son mieux pour se relaxer au soleil et semble apprécier, mais je sais qu'elle est légèrement agacée de ne pas savoir ce qui se dit. Ne pas avoir Misha juste à côté peut être gênant."


ssh "Hisao, quel est le score ? On gagne ? J’espère, je te fais confiance pour la victoire de notre équipe."


"J'arrive à faire des signes maladroits en calant ma canne. C'est sûrement plus proche du baragouinage que de vrais termes."


hi "Tu es genre, juste là. Tu ne vois pas ?"


ssh "Décevant. Tu te laisses distraire. Tu dois rester concentré."


hi "J'aurais dû le savoir. Bon, c'est 0-0 dans tous les cas."


"Akira rit, bien qu'il est clair que ça l'a remotivée."


hi "Juste le nombre, ou est-ce qu'on compte la taille aussi ?"


ssh "Les deux, la qualité compte."


hi "Qui va les juger ? Tu es un expert poissonnier certifié ?"


"Shizune secoue la tête pour signifier que non."


ssh "...Mais ça ne semble pas être très dur. Dis à Misha d’arrêter de s'agiter comme ça, ça effraye les poissons. Et demande à Hideaki pourquoi il n'a pas encore lancé sa ligne."


"Je me tourne vers eux et leur crie ce que Shizune a dit."


mi "Shicchan, je crois qu'il est mécontent de se retrouver avec la canne improvisée~ !"


"Vu que Misha est incapable de signer quoi que ce soit de cohérent, elle reçoit un regard interrogateur de Shizune. Shizune soupire juste après que je lui aie traduit."


aki "Hé, même si ça t’embête, tu dois essayer. Tu pourrais attraper le plus gros, pour tout ce que j'en sais. Mais tu n'attraperas rien si tu ne fais rien !"


"J'ai l'impression qu'elle encourage Hideaki surtout parce qu'elle veut être là pour manger son poisson au cas où il attrape le plus gros. Et avoir six personnes qui pêchent, au lieu de cinq, donne plus de chance d'en attraper."


"Les gestes constants que je dois faire pour pouvoir communiquer avec Shizune, sans mentionner le fait qu'elle parle de plus en plus, me font penser que ce serait peut-être une bonne idée de la laisser pêcher à son tour."


hi "Hé les gars, on peut échanger maintenant ?"


aki "Bien sûr. Lilly ?"


li "Non, non, je vous en prie. Je n'ai aucune idée de comment pêcher."


"Je signe ce qu'ils disent, étant donné qu'il semble que j'aie pris la place de Misha en tant qu’interprète de Shizune maintenant."


ssh "C'est vraiment magnanime à toi, Lilly."


"Et voilà, c'est parti. Je ne prends même pas la peine de traduire ce qu'elle dit par peur qu'elle commence une autre dispute."


hi "Shizune dit que tu devrais au moins essayer. Ça pourrait être drôle."


li "Très bien. Akira, comment est-ce qu'on utilise ça ?"


aki "C'est assez simple..."


"Je me demande si c'est éthique de changer complètement ce qu'a dit Shizune. Au moins ça marche."

scene ev shizu_fishing_sl
with shorttimeskip


li "Je crois que je comprends. Quel appât crois-tu que je devrais utiliser ? Je préférerais quelque chose qui ne fasse pas trop mal aux poissons."


aki "Si tu passes un crochet à travers leurs bouches, je ne crois pas que l’appât leur fera beaucoup plus mal."


hi "Et les laisser partir... ? Non, non, ne fais pas ça."


li "Mais s'il n'est pas gros, pas besoin de le tuer..."


"Avec les mains libres, il est plus facile d’interpréter ce que tout le monde dit. Maintenant Shizune est celle qui a les mains pleines mais elle semble s'en accommoder quand même."


ssh "C'est tellement arrogant. D'accord, je vais viser uniquement les plus gros aussi à partir de maintenant."


aki "Qu'est-ce qu'elle dit ?"


"Akira soupire après que je lui aie traduit."


aki "Non, je n'apprécie pas le “uniquement”. Tu sais, un poisson est un poisson, et tu prends ce que tu peux."


"Malheureusement, Shizune ne peut pas l'entendre et Lilly ne semble pas beaucoup prêter attention."


"Lilly a rapidement trouvé de l'intérêt à la pêche. C'est une activité relaxante, après tout."


"Il ne faut pas longtemps pour qu'elles attrapent toutes deux un poisson, et étonnamment, Lilly est aussi intéressée que Shizune pour savoir lequel est le plus gros."

stop music fadeout 3.0


"Et les heures passent, on dirait qu'ils s'amusent."

scene bg shizu_fishing_ss
with shorttimeskip

play ambient sfx_parkambience fadein 4.0
play music music_tranquil fadein 3.0


"À la fin de la journée, nous avons plusieurs poissons de bonne taille. Même Hideaki et Misha ont réussi à en attraper un. Personne ne semble se rappeler que nous étions en compétition. Je ne crois pas que quiconque s'en soucie maintenant."

show akira basic_smile_ss at center
with charaenter


"Shizune et Misha discutent entre elles un peu à l'écart et Lilly et Hideaki font de même. Je décide de prendre avantage du moment de silence pour parler avec Akira."


hi "Lilly et Shizune se sont bien entendues aujourd'hui. Je ne m'y attendais pas vraiment, après avoir vu comment elles agissaient l'une envers l'autre à l'école."

show akira basic_boo_ss
with charachange


"Elle semble amusée. Elle n'a pas l'air de prendre leurs querelles autant au sérieux que moi."


aki "Elles ont leurs raisons. Lilly et moi partons pour un moment à partir de demain, donc on a pensé qu'on pourrait passer."

show akira basic_ending_ss
with charachange


aki "En fin de compte, je suis contente qu'on ait fait ça."


"Après un bref silence, elle s'étire bruyamment puis claque dans les mains pour attirer l'attention de tout le monde."

show akira basic_smile_ss
with charachange


aki "Bon, on dirait qu'on a suffisamment pour nourrir tout le monde. On devrait rentrer maintenant."

show bg shizu_fishing_ss at bgright
show akira basic_smile_ss at tworight
with charamove

show lilly basic_weaksmile_cas_ss at twoleft
with charaenter


"Lilly hoche la tête, puis hésite. Même si elle a le visage encore quelque peu sombre, elle semble de meilleure humeur que ce matin. Akira semble vraiment savoir comment la gérer et désamorcer son agressivité envers Shizune."

show akira basic_ending_ss
with charachange


aki "Les prises d'aujourd'hui semblent délicieuses, j'aimerais avoir de la sauce soja pour pouvoir les manger maintenant."

show lilly basic_surprised_cas_ss
with charachange


li "Je croyais que tu voulais que je les cuisine..."

show akira basic_laugh_ss
with charachange


aki "Ça ne serait pas bien de les manger crues ?"


"Malgré les protestations d'Akira, ou alors ce sont des blagues, je ne sais pas vraiment, nous décidons d'attendre d'avoir au moins cuisiné les poissons avant de les manger."

stop ambient fadeout 2.0

scene bg shizu_houseext_lights
with shorttimeskip

stop music fadeout 3.0


"Il est déjà tard au moment où nous partons, et quand nous arrivons à la maison de Shizune, il est l'heure de dîner."

scene black
with dissolve



label fr_S19:

scene bg shizu_guesthisao
with locationchange

play music music_pearly fadein 5.0


"Certaines de mes pilules sont tombées au fond de mon sac, ce que je n'ai réalisé que la veille, quelques minutes avant d'aller me coucher. J'ai passé un bon moment à toutes les retrouver."



"Au moment où je me lève, je souffre déjà d'une migraine parce que j'ai mal dormi et que je me suis réveillé tard."

scene bg shizu_living
show hideaki normal_up at center
with locationchange


"Quand je rentre dans le salon, Hideaki est en train de finir son petit déjeuner. Sa fourchette est à mi-chemin entre l'assiette et sa bouche, et il ne semble pas savoir s'il doit me saluer ou continuer de manger. Peut-être que je devrais partir."

show hideaki triangle
with charachange


hh "Bonjour."


hi "Bonjour."

show hideaki thinking
with charachange


hh "Qu'est-ce qu'on va prendre comme petit déjeuner ?"


hi "“On ?” Tu n'es pas déjà en train de manger ?"

show hideaki normal
with charachange


hh "Si. Tout le monde a déjà mangé."


"Malgré ça, il répète la question. Il essaye juste d’être gentil. C'est une drôle de façon de le montrer, mais j'apprécie quand même, et je dois avouer que j'ai assez faim."


"J'essaye de faire la conversation avec lui pendant que je me prépare mon petit déjeuner, pour combler le silence."


hi "C'était bien la pêche hier. Les Hakamichi et les Satou sont souvent ensemble comme ça ?"

show hideaki bored
with charachange


hh "Pas vraiment."


hi "Je vois."


"Pas vraiment. Il y a une brève pause avant que Hideaki m'explique."

show hideaki thinking
with charachange


hh "Problèmes de famille. Nos pères sont frères et ne s'apprécient pas."


"Cette information me donne du grain à moudre. Cela me donne une explication sur la manière d'agir de Shizune et Lilly, et cela me rend encore plus prudent sur le sujet."


hi "Ah. Ça peut être compliqué la famille."

show hideaki normal
with charachange


"Hideaki hoche simplement la tête tandis que je m'assieds à table avec mon repas. J'aimerais que ce soit plus facile de communiquer avec lui."


"Pendant que je mange, je remarque que la maison est étrangement silencieuse pour un endroit où se trouve Misha. Si Shizune et Misha ont déjà mangé, elles ne peuvent pas être en train de dormir. Je demande à Hideaki où elles sont."

show hideaki bored
with charachange


hh "Shizune et Misha sont parties faire des courses pour notre père. Les commerçants locaux adorent Misha, alors il a insisté."


hi "Bah, elle est joyeuse et agréable. Je comprends pourquoi ils l'aiment bien. Peut-être que tu devrais apprendre d'elle, tu pourrais te faire de nouveaux contacts professionnels."

show hideaki confused
with charachange


hh "Tu es sérieux ?"


"Il semble sérieux. Je ne sais pas de quel genre de contacts professionnels un enfant aurait besoin. Peut-être qu'il veut détenir la meilleure vente de gâteaux du monde."


"C'est dommage, je vais partir et ne serai pas là pour voir ce qu'il a prévu."


"Je me demande quel genre de personne est le père de Shizune, en dehors du fait qu'il soit sportif. Ce que je sais de lui, c'est qu'il demande à ses partenaires commerciaux et aux amis de sa fille de lui rendre des services."


"Je suppose qu'il est extrêmement timide ou extrêmement flemmard. Peut-être que c'est sévère de dire ça alors que je ne le connais pas, mais ça expliquerait certainement un large panel de la personnalité de Shizune."

show hideaki triangle
with charachange


hh "Tu veux aller quelque part ?"


hi "Pas vraiment. Pourquoi, tu as envie ?"

show hideaki normal
with charachange


hh "Je pensais qu'il pourrait y avoir un endroit où tu voudrais aller. Tu ne veux pas voir quelque chose, ou manger dans un restaurant particulier ?"


hi "Je ne sais pas. Je ne suis jamais venu ici auparavant."

show hideaki thinking
with charachange


hh "Je vois."


"J'étais sur le point de lui demander comment était Shizune quand elle était plus jeune, mais il a réussi à me perturber avec une seule question. La conversation semble être aussi bizarre pour lui qu'elle l'est pour moi."


hi "Tu es drôlement agréable aujourd'hui. Pourquoi est-ce que tu es si gentil ? Tu montres ton bon côté secret quand ta sœur n'est pas là ?"

show hideaki bored
with charachange


hh "Plus ou moins. Shizune voulait que je te tienne compagnie aujourd'hui."


"Je ne veux pas l’embêter et j'essaye de lui faire comprendre, mais Hideaki est aussi têtu que sa sœur et ressent ça comme étant son devoir. Il semble aussi essayer honnêtement d’être gentil."


"Rapidement, je commence à réaliser que ce qui amuse Hideaki c'est de pêcher, collectionner des appareils photos et faire des jeux de mots."


"Pêcher est amusant, mais c'est quelque chose que je ferais plutôt que d'en discuter. Pareil pour les appareils photos."


"Mais Hideaki s'en rend compte tout seul."

show hideaki normal_up
with charachange


hh "Tu t'ennuies ?"


hi "Pas du tout."


"Je bâille presque en disant ça, donc Hideaki ignore totalement mes paroles."

show hideaki sad
with charachange


hh "Tu t'ennuies. Shizune a dit que je devais te divertir, et je crois que je ne sais pas comment faire ça."


hi "Je suis diverti."

show hideaki serious
with charachange


hh "Tu n'en as pas l'air."


hi "Je le suis pourtant !"

show hideaki normal
with charachange


hh "Pourquoi est-ce que tu cries ? J’espère que tu ne cries pas autant avec Shizune."


"Il est difficile de dire s'il blague. Dans tous les cas, je suis un peu surpris. J'essaye de changer de sujet."


hi "Tu collectionnes juste les appareils photos ou tu photographies aussi ?"

show hideaki bored
with charachange


hh "Pas vraiment. Si c'était le cas, il y aurait plus de photos que ça dans la maison. De quoi est-ce qu'on peut prendre des photos ?"


hi "Je sais pas. Des oiseaux ? De l'architecture ? Un des restaurants dont tu parlais ? Je croyais que cette ville avait plein de trucs cool à voir. Comment peux-tu vivre dans un endroit avec tant à faire tout en ne faisant rien ?"

show hideaki triangle
with charachange


hh "Je croyais que tu ne savais pas ce qu'il y avait à faire ici. Soudainement tu as énormément d'idées et sais à quel point c'est intéressant. Tu es comme l'office de tourisme. Tu veux aller voir des oiseaux ou des buildings ?"


hi "D'accord, d'accord, pas besoin de t'énerver."

show hideaki normal
with charachange


hh "...Je ne suis pas énervé. Je pense juste que si tu crois ça, on devrait aller dans un parc d'attractions."


hi "Pourquoi ?"

show hideaki confused
with charachange


hh "Pour que tu puisses t'amuser. Ça sera drôle."


"Est-ce qu'il aurait cette même expression dépressive pendant que nous serions dans un roller coaster ou une tour en chute libre ? Ça gâcherait sûrement pas mal le côté fun de la chose. Cela me fait penser que le voyage ne vaut pas le coup."


hi "Je ne sais pas. J'ai toujours eu l'impression qu'un parc d'attractions se résume plus à faire la queue qu'à faire des attractions. Il faut y aller plus tôt que ça pour éviter la foule."

show hideaki normal
with charachange


hh "Tu n'as jamais été dans un parc d'attractions ?"


hi "Non, mais j'ai l'impression que c'est comme ça."

show hideaki bored
with charachange


hh "...D'accord. Et un parc normal ? Il y en a un pas loin où Shizune aime aller. Peut-être qu'elle sera là-bas, et que je pourrai te débarquer avec elle."


hi "Comment ça “débarquer” ? Je ne suis pas une valise."

show hideaki triangle
with charachange


hh "Tu ne veux pas aller dans un parc d'attractions. Je ne sais pas quoi faire."


"Il agit comme si je l'avais blessé en refusant d'aller avec lui. Je rationalise déjà ma décision. Je n'aime pas faire la queue. Ça ressemblerait trop à un rendez-vous. Je préférerais aller avec Shizune. Ça serait trop fatiguant."


hi "Il n'y a rien de personnel, c'est juste que je voulais que Shizune me montre la ville elle-même."

stop music fadeout 2.0


"Et je ne crois pas qu'aller dans un parc d'attractions avec ma maladie soit une si bonne idée."

scene bg shizu_park
with locationskip

play music music_soothing fadein 0.5


"Le parc est suffisamment proche de leur maison pour qu'on puisse le considérer comme une extension de celle-ci. Le parc et le jardin de Shizune se ressemblent beaucoup, sauf que dans le parc il y a des bancs et plus de gens."


"Cela dit, il est pas mal. Il y a même des gens promenant leurs chiens et des enfants jouant avec des cerfs-volants qui planent au loin. Je pourrais rester assis ici et me relaxer en regardant ce paysage pour toujours."

show hideaki bored at center
with charaenter


"Hideaki, d'un autre côté, semble extrêmement ennuyé. J'ai envie de le remuer pour vérifier qu'il est en vie. Mais est-ce qu'il réagirait de toute façon ?"


hi "Tu t'ennuies ?"

show hideaki normal
with charachange


hh "Non. Tu vas courir ou jouer au frisbee avec des chiens comme tout le monde ? C'est ce que font les gens dans les parcs ?"


hi "Eh bien tu vas dans un parc pour apprécier la nature et l’atmosphère. C'est pour ça que les gens font leur jogging dans le parc au lieu de le faire bêtement sur un trottoir ou autre. On peut courir partout."


hi "Je n'arrive pas à croire que j'ai cette conversation. Comment est-ce que tu peux ne pas savoir ça ? Tu n'aurais pas dû demander ça, c'est trop bizarre. Tu as déjà entendu “Les enfants devraient être vus, pas entendus” ?"

show hideaki bored
with charachange


hh "Oui."

show hideaki triangle
with charachange


hh "J'ai menti. Je m’ennuie. Tu veux jouer à un jeu ?"


"Je grogne suffisamment fort pour lui faire comprendre que je n'ai pas envie. Il s'en moque. En fait, il est déjà en train de jouer avec un paquet de cartes."

show hideaki serious
with charachange


hh "Pourquoi est-ce que tu es si énervé ? C'est pour ça qu'on est là."


hi "Je croyais qu'on était là pour chercher Shizune."

show hideaki happy
with charachange


hh "Exactement. C'est pour ça qu'on devrait jouer. C'est un piège pour Shizune. On peut tout attraper, même les gens."

show hideaki thinking
with charachange


hh "Si nous nous affrontons avec un esprit de compétition, elle sera attirée ici pour affronter le vainqueur, comme un requin. Puis je la vaincrai comme un chasseur de safari. Puis je prendrai une photo de la cérémonie de récompenses."


"Les requins ne se baladent pas en provoquant les gens en duel comme ceux qui défient les dojos."


hi "Et puis quand est-ce que tu as pris cet appareil photo ? Bref, non. Je joue à assez de jeux en traînant avec ta sœur."

show hideaki normal
with charachange


hh "Non, allez, ça sera drôle. On peut jouer aux échecs."


hi "S'il te plaît, non. En plus, jouer aux échecs dans un parc, c'est un truc de vieux, comme la pêche. Tu deviendras vieux trop vite si tu continues d'agir comme ça."

show hideaki darkside
with charachange


"Hideaki s'immobilise comme si j'avais soudainement commencé à parler un langage étranger. Peut-être que je l'ai offensé encore une fois."


"Peut-être qu'il a secrètement 50 ans et qu'il ne fait juste pas du tout son âge. Le fait qu'il soit le frère de Shizune pourrait être une couverture."

show hideaki disapproves
with charachange


hh "Et les dames ? Ou le go ? Ou même le backgammon, même si je n'aime pas trop ça. Si les jeux de plateau ne sont pas trop ton truc, on peut jouer aux cartes. Quoi que ce soit d'autre que le Stud à sept cartes, parce que c'est pour les mauviettes."

show hideaki evil
with charachange


hh "Tu as peur de perdre ? Si tu peux me battre je te donnerai des bonbons."


hi "Hideaki, tu ressembles trop à Shizune. Je commence à croire que c'est juste une excuse pour jouer."

show hideaki thinking
with charachange


hh "Non, ce n'est pas vrai."


hi "Si ! Je parie que cet élan compétitif est génétique. Je vais te vendre à la science."

show hideaki normal
with charachange


hh "Personne ne peut posséder un être humain."


hi "Et si je t'enseignais la langue des signes à la place ?"


hi "Quand Shizune m'a demandé si je voulais venir ici, on a un peu parlé, et apparemment ton père et toi n'utilisez pas le langage des signes. Je suppose juste, mais si c'est le cas, je peux t'apprendre un peu. Je ne suis pas un expert cela dit."


hi "Je crois que ça serait bien que tu apprennes à plus bouger tes bras de toute façon."


"Il bouge à peine ses bras. La plupart du temps ils sont juste collés à ses hanches. C'est agaçant."


"Ça me perturbe que la famille entière de Shizune ne sache pas signer. Je me demande ce qu'elle faisait avant de rencontrer Misha. Est-ce qu'ils engageaient des traducteurs pour elle ? Est-ce qu'elle écrivait tout sur son bloc-notes ?"


"La seconde théorie est la plus plausible. Ça expliquerait pourquoi elle déteste à ce point utiliser le bloc-notes. Aussi triste que ce soit, je comprends pourquoi Hideaki ou son père ne se sont pas embêtés à apprendre la langue des signes."


"C'était probablement trop compliqué à l'époque. C'est facile de penser ça. De ce que j'ai vu cela dit, aucun d'entre eux n'en veut à l'autre ou ne semble affecté. Peut-être que je réfléchis trop."


hi "Allez. Bon, pour être honnête, je suis toujours en train d'apprendre moi-même. J'ai apporté tous mes livres avec moi pour pouvoir suivre, tu sais ? Bref, je peux au moins t'apprendre l'alphabet. C'est assez simple. Ça c'est “cerf-volant.”"


"Je me sens un peu seul là, et encore plus alors que Hideaki me regarde les yeux vides comme si le concept d'apprendre la langue des signes lui était totalement étranger."

show hideaki bored
with charachange


hh "Shizune aimait bien faire du cerf-volant ici aussi."


"C'est une tentative pour relancer la conversation, et j'y adhère avec plaisir."


hi "Pêche et cerfs-volants, hein ? Shizune aimait vraiment les hobbies relaxants ?"

show hideaki thinking
with charachange


hh "Des combats de cerfs-volants. En fait, Shizune est—{w=0.5}{nw}"

stop music fadeout 0.3

show misha cross_grin_cas behind hideaki:
    center
    ypos 1.1 alpha 0.0
    linear 0.2 ypos 1.0 alpha 1.0
show hideaki ohshit
with vpunch


"Hideaki s'immobilise alors que Misha apparaît derrière lui et lui met les mains devant ses yeux."

play music music_comedy fadein 0.5


mi "Hi hi~ ! Devine qui c'est~ !"


"Il semble être quelque peu détendu maintenant, aussi."


hi "Salut Misha. Shizune est avec toi ?"


mi "Hicchan, ne dis rien ! Ne dis rien, ne gâche pas la surprise, d'accord~ ?"

show hideaki thinking
with charachange


hh "Misha."

show bg shizu_park at bgright
show hideaki normal at tworight
show misha perky_confused_cas at twoleft
with dissolvecharamove


mi "Bingo~ ! Tu as raison ! Mais~, c'était trop facile, d'une certaine façon."


"Je ne sais pas ce qu'elle veut dire par “d'une certaine façon”."

show misha hips_frown_cas
with charachange


mi "Trop de personnes se rendent compte que c'est moi ! Je veux surprendre quelqu'un ! Je croyais que je réussirais à avoir Hideaki~. Pourquoi je n'ai pas réussi, hein~ ?"

show hideaki bored
with charachange


hh "Tu es la seule personne qui fait ça. Toi, et les kidnappeurs."

show misha cross_laugh_cas
with charachange


mi "Vraiment ? Wahahah~ !"

show hideaki serious
with charachange


hh "Pourquoi est-ce que tu ris ?"

show shizu invis:
    center
    xpos 0.1
with None

show bg shizu_park at left
show misha cross_laugh_cas at Position(xpos=0.4)
show hideaki serious at Position(xpos=0.8)
show shizu basic_angry_cas at Position(xpos=0.2)
with dissolvecharamove


ssh "Tu embêtes Hisao ? Je t’ai dit de l'emmener dans un endroit plus intéressant que le parc. Ce n'est même pas loin de la maison. Tu es vraiment paresseux."

show misha hips_frown_cas
with charachange


mi "Hideaki, tu embêtes Hisao ? Tu aurais dû l'emmener dans un endroit plus intéressant ! Le parc est trop proche de la maison, Shicchan dit que tu es paresseux~."

show hideaki bored
with charachange


hh "Il voulait venir ici. Pourquoi est-ce que tu es aussi agressive ?"

show shizu behind_frown_cas
with charachange


ssh "Je dois m'assurer que mon petit frère fait bien les choses."

show hideaki triangle
with charachange


hh "Qu'est-ce qu'elle dit ?"


hi "Tu dois bien faire les choses."

show hideaki serious
with charachange


hh "Vraiment..."


"Ils sont prêts à se sauter à la gorge. D'un côté, j'ai entendu que les bagarres entre frères et sœurs ne sont pas rares, et le fait qu'ils se disputent montre qu'il y a au moins de la communication entre eux. C'est bien."

scene bg shizu_houseext
with locationskip

stop music fadeout 4.0


"Ils continuent pendant tout le chemin jusqu’à la maison. Misha traduit pour Shizune, et moi pour Hideaki. Donc on dirait plus qu'on se dispute tous les deux, sauf que pas vraiment. Personne ne peut entendre Misha et croire ça."


"La journée est intéressante jusqu'au bout, au moins."

$ suppress_window_after_timeskip = True

scene black
with dissolve



label fr_S20:

window hide None

scene black
with dissolve

show bg shizu_guesthisao
with openeye

window show


"Bien que je ne sois là que depuis deux jours, j'ai l'impression que ça fait plus longtemps. Je me réveille en me sentant plus fatigué que reposé. Peut-être parce que je n'ai pas arrêté de bouger depuis que je suis ici."


"Quelle que soit la raison, je me réveille tard chaque jour. J'aime bien faire la grasse matinée, mais il ne faudrait pas que ça devienne une habitude."


"Je peux entendre une forte voix masculine crier depuis la chambre. Ça doit être le père de Shizune. Ou peut-être, vu la taille de cette maison, ses créanciers. Sûrement l'ancien créancier, vu que les cris ne semblent pas énervés, juste forts."

scene bg shizu_living
show hideaki normal:
    center
    xpos 0.5
show misha perky_smile_cas:
    center
    xpos 0.3
show shizu basic_normal_cas:
    center
    xpos 0.08
show jigoro smug:
    center
    xpos 0.87
with charaenter

play music music_another fadein 0.5


"Shizune, Misha et Hideaki sont assis dans le salon et ont une conversation à sens unique avec un homme-ours géant qui alterne entre prendre de grandes bouchées du plat en équilibre sur sa jambe et faire tournoyer une épée."


"Connaissant Shizune et Hideaki, j'aurais cru que leur père serait quelqu'un de réservé, propre sur soi, possiblement androgyne, donc je suis surpris. Je suis surpris un moment, jusqu’à ce qu'il commence à me parler."

show jigoro laugh
with charachange


hx_ "Bonjour ! Tu dois être l'autre ami de Shizune. Tu as bien dormi ? Les chambres d'amis sont un peu petites, si tu as besoin de quoi que ce soit, n'hésite pas à me demander."


hi "Merci. Vous devez être le père de Shizune. Heureux de vous rencontrer. Je suis le camarade de classe de Shizune, Hisao Nakai."

show jigoro neutral
with charachange


hx_ "Tout le plaisir est pour moi. Je voulais te rencontrer après avoir entendu que j'aurais un deuxième invité dans la maison. Imprévu."


hx_ "Quand on entend quelque chose comme ça, évidemment qu'on veut voir à quoi ressemble cette personne. Tu veux ma carte de visite ?"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

show jigorocard:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)


"Il sort un porte-cartes et je peux voir que son nom est Jigoro et que ses horaires de bureau sont de huit heures à dix-huit heures. Ça dit aussi qu'il est “consultant”. Quel type bien préparé, pour avoir son porte-cartes sur lui dans sa propre maison."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

show jigorocard:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide jigorocard
with None

show jigoro smug
with charachange


hx "Nous avons un petit déjeuner tardif, tu es là juste à temps pour nous rejoindre. Bien. Prends un siège et je t'apporte une assiette. J’espère que tu n'as rien contre le foie d'ours."


"Je croyais que le foie d'ours était toxique. Dans tous les cas, je n'ai pas d'autre raison d'en manger que de pouvoir dire que je l'ai fait. J'imagine que ça ne ferait pas de mal d'essayer. Mais le père de Shizune se met à rire."

show jigoro laugh
with charachange


hx "Je plaisantais juste. Quoi que ça ne serait pas une si mauvaise idée de donner du foie d'ours aux enfants. Ça vous rendrait fort."

show jigoro neutral
with charachange


hx "Nous mangeons en fait des omelettes. Je t'en fais une tout de suite. C'est rare pour toi d'avoir une omelette pour le petit déjeuner ?"

show hideaki triangle
with charachange


hh "Très rare."


hi "Non, pas du tout."

hide jigoro
with charaexit


"Jigoro disparaît à l'endroit où doit être la cuisine. Je suis surpris que bien qu'il vive dans un endroit comme ça, il ait à cuisiner mon repas. Peut-être qu'il cuisine parce qu'il aime ça."

show jigoro smug:
    center
    xpos 0.87
with shorttimeskip


"Mon assiette fumante est prête en peu de temps. Ça sent vraiment bon."


hx "Tu es dans le Conseil des Étudiants, comme Shizune ? Le Conseil des Étudiants est si occupé que ça pour que Shizune ait à traîner ses amis avec elle partout où elle va ?"

show shizu behind_blank_cas at Position(xpos=0.12)
with charachange


ssh "Parfois des vacances sont juste des vacances."


hi "Vous avez raison pour le conseil des étudiants. Cela dit, je crois qu'on est là juste pour se détendre."

show jigoro neutral
with charachange


hx "Je vois. Quand j'étais jeune, notre conseil des étudiants avait tellement de travail qu'on ne pouvait pas se permettre d'aller en vacances. Ça doit être bien, avoir autant de temps libre. Ça doit donner beaucoup de temps pour penser à votre avenir."


"Je n'aime pas la direction que prend cette conversation, et commence à envisager de l'éviter."


hx "Tu y as déjà pensé ? À ce que tu veux faire ?"


hi "Non. Je n'y ai pas vraiment pensé récemment. Qu'est-ce que vous faites, si je peux me permettre de demander ? Ça doit être plutôt bien, si avez une maison comme celle-ci."

show jigoro angry
with charachange


hx "Pourquoi tu veux savoir ça ? Les enfants ne s'intéressent pas aux affaires. En quoi mes affaires t’intéresseraient ? Suspect. Ne serais-tu pas du fisc, jeune homme ?"


"J'imagine qu'il n'aime pas qu'on lui pose des questions."

show misha hips_grin_cas
with charachange


mi "Hicchan n'est pas du fisc, je crois~. Hicchan, que font tes parents ? Tu nous as jamais dit~ !"


hx "Toi, silence. Ne m’interromps pas. Je déteste être interrompu. Impolie."

show misha perky_sad_cas
with charachange

mi "Aah~…"

show shizu basic_normal2_cas at Position(xpos=0.08)
with charachange


"Shizune ne semble pas très contente de la tournure que prennent les évènements. Même si Misha est incapable de signer ce qui se passe, elle peut sentir l’atmosphère. Son regard se met à fumer alors que Jigoro continue son assaut."


hx "Une dernière chose. Mon équipement de pêche. Je suis rentré et c'était juste un gros tas dans un coin. Les cannes juste déposées en bazar sur les boîtes."

show hideaki thinking
with charachange


hh "C'était moi."


"Je ne suis pas capable de dire si c'était lui ou non. Si ce n'est pas le cas, j'apprécie qu'il veuille prendre une balle pour l'équipe. Mais ça ne sert à rien parce que Jigoro l'ignore complètement sans s’arrêter."

show jigoro smug
with charachange


hx "Bref, je suis content que mon équipement de pêche ait pu divertir les amis de ma fille. Vous ne m'avez même pas dit que vous alliez les utiliser. Ce sont des cannes customisées très chères. Pas pour des dilettantes."


"Je me rends soudainement compte qu'il y a plein de morceaux de coquille d’œuf dans mon omelette. Est-ce qu'il cuisine mal ? Est-ce qu'il les mange pour le calcium ? Est-ce qu'il les a mis volontairement pour me mettre encore plus mal à l'aise ?"


"Bien que confus, je ne suis pas aussi perturbé que j'aurais cru l’être dans une situation comme ça. Ma vie a été bien étrange récemment, et je rencontre beaucoup de personnes différentes. Rien ne me surprend plus désormais."

show jigoro angry
with charachange


hx "Vous ne les avez même pas nettoyées après usage. Épouvantable."


hx "Est-ce que vous savez au moins comment pêcher ? Sûrement pas. Il n'y a même pas assez de cannes. Comment vous avez fait ? Vous avez partagé ? Une personne met l’hameçon et l'autre lance ? Deux personnes pour embobiner ? Incompétents."


hi "Eh bien, on y a été à six, donc on n'a pas pu tous pêcher en même temps. D'abord ce fut Akira, Hideaki, Misha et moi."


hx "Arrête de parler. Tu parles mal. J'en ai assez de ta grossièreté. Vraiment vulgaire. Assure-toi que tes phrases ne soient pas aussi embarrassantes la prochaine fois que tu ouvres la bouche."


hi "Quoi... ?"


hx "“Quoi ?” Tu es si irrespectueux. Incroyable. Tous les délinquants sont comme ça ? Même la façon dont tu t'habilles montre un irrespect total de l'autorité. Sweat-shirt. Honteux..."


hi "Délinquant ? Je suis dans le Conseil des Étudiants."


"Je suis blessé par son commentaire sur mon sweat-shirt, surtout venant d'un gars avec une chemise aussi moulante. J'imagine que je ne peux pas dire grand-chose, cela dit. Il a une épée. Il tue peut-être des ours aussi."

stop music fadeout 0.3
play sound sfx_impact
with vpunch


"Misha pose son assiette avec force sur la table."

show misha hips_smile_cas
with charachange


mi "C'était délicieux~ ! Shicchan et moi avons fini maintenant. Hicchan, toi aussi, hein~ ? On devrait y aller !"


"Quelle stratégie de fuite simple mais efficace."

scene bg shizu_houseext
with locationchange


"J'ai à peine le temps de poser mon assiette avant qu'elles ne me sortent de la pièce, puis finalement à l'extérieur."

show shizu behind_frustrated_cas at tworight
show misha perky_confused_cas at twoleft
with charaenter

shi "…"

show misha sign_confused_cas
with charachange


mi "Incroyable~ ! C'est comme si je regardais un interrogatoire~ ! Ce n'est pas une série policière ! Les invités ont des responsabilités, mais il n'a jamais entendu parler de l'hospitalité ? Vraiment~ !"


"Misha essaye d’interpréter au mieux les mimiques colériques de Shizune. Elle a l'expression assombrie aussi, mais le ton de sa voix reste le même que toujours, et donc manquant de la colère nécessaire pour que tout colle."

show misha hips_smile_cas
with charachange


mi "Wahaha~. Ne le prends pas mal, Hicchan~ ! Le père de Shicchan est pareil avec tout le monde, je crois que c'est comme une plaisanterie~."


hi "C'est la plaisanterie la plus agressive du monde."


"Je ne suis pas du tout convaincu que ce soit une blague, vu la retraite hâtive qu'on a dû faire, mais ce n'est pas le bon moment pour se demander à quel point le père de Shizune peut être un con."

play music music_shizune fadein 4.0

show misha sign_smile_cas
with charachange


mi "Hicchan, allons faire du shopping !"

show shizu adjust_happy_cas
with charachange


ssh "Tu n'as pas encore été en ville, hein ? Ça sera drôle. On peut voir de belles choses, aller dans un parc d'attractions, et même manger dans un bon restaurant."


hi "On vient juste de manger."


"Même si je n'ai pas tant mangé que ça."

show shizu behind_smile_cas
with charachange


ssh "C'est pas grave, dans ce cas, on va s'assurer d'être occupés toute la journée pour que quand on ait fini, il soit l'heure de dîner."

show misha cross_grin_cas
with charachange


mi "Ça marche parfaitement ! Allez, Hicchan~ !"

show shizu behind_smile_cas_close at closeright
show misha cross_smile_cas_close at closeleft
with characlose


"Elles m'encerclent et passent leurs bras autour des miens, Shizune en prenant un et Misha l'autre. Au début, nous en tombons presque. Shizune marche à un rythme soutenu tandis que Misha semble plus rebondir à chaque pas."

scene bg shizu_park
with locationchange


"Nous nous habituons vite et je remarque que nous allons en ville en passant par le parc. Ça ne semble pas le chemin le plus court, donc j'imagine que c'est juste parce que c'est un chemin plaisant."


"Marcher comme ça nous empêche considérablement de communiquer. Je ne peux pas du tout parler à Shizune. Shizune et Misha en sont réduites à une seule main. C'est agréable cela dit, donc ça ne me gêne pas trop."


"Quand je le dis à Misha, elle répond, semblant légèrement confuse."

show misha perky_confused_cas_close at closeleft
with charaenter


mi "Vraiment, Hicchan~ ? Mh... Si tu veux l'attention de Shicchan, tu peux me le dire, et je lui tapoterai l'épaule pour toi."


hi "Tu peux aussi me lâcher et je le ferai moi-même. Et comment tu peux lui taper l'épaule d'ici ?"

show misha hips_grin_cas_close
with charachange


mi "Comme ça~ !"

with vpunch

show shizu behind_frustrated_cas_close behind misha at closeright
with charachange


"Elle s’arrête soudainement et essaye d'atteindre l'épaule de Shizune en passant par dessus mes épaules. Elle réussit, mais seulement parce que quand elle s'est arrêtée, j'ai dû m’arrêter aussi pour éviter qu'on ne tombe tous."

show misha hips_laugh_cas_close
with charachange

show shizu adjust_blush_cas_close
with charachange


"Évidemment, Shizune a dû s’arrêter aussi, ce qui fait rire Misha à sa manière habituelle, surprenant les gens autour de nous, et Shizune commence à lui dire avec sa main libre d’arrêter, ce qui la fait bien rire encore plus fort."


"C'est assez drôle de la voir aussi embarrassée, et je commence à rire aussi."

stop music fadeout 2.0

scene black
with dissolve



label fr_S21:

scene bg shizu_guesthisao
with locationchange

play music music_dreamy fadein 2.0


"J'ai négligé mes études de langue des signes ces derniers temps, je devrais probablement passer du temps à rattraper. Cela dit, je crois avoir appris beaucoup par osmose. J'en suis très fier et vais devoir faire attention de ne pas m'en vanter."


"La plupart des livres que j'ai apportés ne sont pas des manuels sur l'apprentissage de la langue des signes, mais sur les différents “dialectes”. Je sais que Shizune a certains signaux secrets avec Misha dont seules elles deux connaissent le sens."


"Après en avoir vu quelques-uns, ce livre a attiré mon attention à la bibliothèque."


"Peut-être que je devrais en utiliser quelques exemples aussi pour les embêter, je suis sûr qu'elles ont commencé à s'en servir plus souvent depuis que j'ai appris la langue des signes. Ça leur apprendra."


"Après une pause rapide pour me doucher, je continue de m'entraîner devant le miroir de la chambre d'ami. Hier, je me suis écrasé les doigts plutôt violemment. Ça me lance toujours et je ne veux pas que ça arrive encore une fois."

play sound sfx_doorknock2

show hideaki normal at center
with charaenter


"J’entends quelqu'un frapper à la porte derrière moi et trouve Hideaki qui me fixe. C'est poli à lui de frapper, mais généralement ça se fait avant d'ouvrir la porte."

show hideaki triangle
with charachange


hh "Qu'est-ce que tu fais ?"


hi "Je m’entraîne à la langue des signes. Tu es là depuis longtemps ?"

show hideaki thinking
with charachange


hh "Je n'ai rien vu."


"Là n'est pas la question. Je ne sais même pas ce qu'il veut dire par là. Ce n'est pas comme si je faisais quelque chose qui aurait été honteux si on m'avait vu."


"Cela dit, le langage des signes doit sembler étrange à la plupart des gens. Je suis seulement habitué à le voir à cause de Shizune et Misha."


hi "J'aiguise mes signes, et m’entraîne à les lire aussi. Et aussi l'histoire des signes, même si on la couvre en cours."

show hideaki normal
with charachange


hh "Ton école a des cours de langue des signes ?"


hi "Ouais. Une des premières choses qu'ils ont dites est que ce n'était pas très courant."

show hideaki serious
with charachange


hh "Ça semble drôle."


hi "Eh bien, je n'appellerais pas ça drôle, mais bon."

show hideaki bored
with charachange


hh "Si tu n'aimes pas ça, ça semble être beaucoup de travail juste pour pouvoir parler à ma sœur."


hi "Pourquoi est-ce que tout le monde dit ça ?"

show hideaki happy
with charachange


"La bouche de Hideaki se tord comme s'il était sur le point de rire, mais s'en empêche. En y pensant, il n'a pas ri une fois depuis que je l'ai rencontré. Je pourrais prendre comme un compliment qu'il ne rie pas de moi, mais je suis curieux."


hi "Ris."

show hideaki thinking
with charachange

stop music fadeout 4.0

hh "…"

show hideaki bored
with charachange


hh "Pourquoi ?"


"C'était la façon la plus rapide et directe que j'ai trouvée pour réaliser mon objectif."


show hideaki normal_up
with charachange


hh "Tu peux m'apprendre la langue des signes ?"


"Il dit ça calmement, mais son corps trahit sa nervosité, montrant qu'il fait clairment des efforts pour demander. Hideaki aime sa sœur après tout. Misha est plus facile à approcher que moi cela dit, je me demande pourquoi il ne lui a pas demandé."


"Secrètement, je crie “yes !” à l'intérieur. J'avais déjà pensé qu'il voulait apprendre la langue des signes et lui en ai même parlé, mais il a évité le sujet. Il s’avère que j'avais raison après tout. Je ne sais pas pourquoi je suis aussi content."


hi "Bien sûr."


"En y pensant, je ne suis pas un professeur de langue des signes. Je ne sais même pas où commencer. En classe, j’apprends peu à peu les choses. Est-ce que Hideaki attend de moi que je lui enseigne tout ce qu'il faut en une seule journée ?"

show hideaki normal
with shorttimeskip

play music music_normal fadein 3.0


"Mon professeur a passé quelques jours à juste expliquer l'histoire de la langue des signes. Je décide de commencer avec ça, pour gagner du temps et trouver une manière de m'attaquer à la pratique. Après cinq minutes, Hideaki lève la main."

show hideaki serious_up
with charachange


hh "Je ne comprends pas ce que tu fais."


hi "Euh... eh bien, je ne peux pas commencer à t'apprendre à faire directement, tu dois y aller doucement. C'est comme quand tu nages, tu ne sautes pas directement dans le lac comme dans les films."

show hideaki triangle
with charachange


hh "Je ne nage pas."


"C'est comme si les scientifiques avaient réussi à extraire toute l'activité et les qualités enfantines d'un jeune enfant et les avaient insufflées à son père, créant un père rageur, et laissant Hideaki."


"Je commence à me sentir claustrophobe, même si la chambre d'ami est trois fois plus grande que ma chambre au dortoir et que nous ne sommes que deux ici."


"Tout ceci est dans ma tête, je le sais, et je m'en moque. Je m'en sers quand même comme excuse pour continuer la leçon à l'extérieur."

scene bg shizu_garden
with locationskip


"C'est beaucoup plus facile de se concentrer ici. Les premières secondes m'ont permis de réorganiser mes pensées. Personne ne dit mot à ce moment-là. Hideaki ne semble pas capable de parler et marcher en même temps."


"Je commence à réaliser que si je veux lui apprendre la langue des signes, il faut que la leçon continue non-stop. À la seconde où il y aura une ouverture, il posera une question, ce qui amènera d'autres questions et je n'en verrai pas le bout."


"La seconde fois, il me demande pourquoi un geste particulier a ce sens-là, et je dois chercher loin dans ma mémoire pour retrouver l’étymologie d'un signe que je ne connais que depuis un mois, et je m'organise une échappatoire."


hi "Hideaki, faisons une pause."

show hideaki bored
with charachange


hh "D'accord."

show hideaki serious
with charachange


hh "Comment est ton école ?"


"Cet enfant est comme un petit journaliste, mais c'est logique à son âge d’être curieux, et c'est une question qui ne me gêne pas."


hi "Comment elle est ? Je n'y ai jamais vraiment pensé. Elle est en haut d'une montagne, donc c'est isolé et même quelque peu triste parfois, même s'il est vrai qu'on a une belle vue."


hi "Les étudiants sont intéressants. En fait, je me sentais un peu mal au début. Tu sais quel genre d'école c'est, hein ?"

show hideaki normal
with charachange


hh "Oui."


hi "Je me sentais mal parce que je ne voulais pas y aller. Je ne me rappelle pas exactement ce que je pensais à l'époque. Probablement que c'était une école pour éclopés et que ça serait déprimant. Comme si on me mettait là-bas pour m'oublier."


hi "Et puis en fait, tout le monde vivait sa vie, en général. Donc je me suis senti encore plus mal. Ce n'était pas bien différent d'une école normale, alors je me suis senti idiot."


hi "Shizune a été la première que j'ai rencontrée. Misha aussi, elles sont toujours ensemble. J'imagine que l'école est fait en sorte qu'elles soient le plus possible ensemble. Et il y a cette fille dans ma classe, Hanako, je me sens mal pour elle."


hi "Elle a ses cicatrices, elle complexe à cause d'elles. Mais pourtant je trouve que ça va, elle est mignonne comme fille. Et amie avec Lilly, aussi. Tu connais Lilly j'imagine ? Elle parle de Hanako des fois ?"

show hideaki thinking
with charachange


hh "Oui, des fois."


hi "J'essaye de me rappeler qui d'autre est intéressant. On a une championne d’athlétisme qui court avec des prothèses."


hi "Il y a cette fille, Rin, qui n'a pas de bras, mais qui est une grande peintre. Tout son art est grotesque et vivant en même temps. Tu as déjà été à Yamaku ? Tu as sûrement déjà vu son mur."


hi "Un peu bizarre des fois, mais j'ai entendu dire que les artistes sont souvent comme ça. Ça me rappelle, le gars qui vit en face de ma chambre est assez bizarre aussi. Mais il est parfois intéressant, au moins."

show hideaki normal
with charachange


hh "Tu es intéressant aussi."


hi "C'est une mauvaise chose ? Et c'est quoi ce ton ? Qu'est-ce que ça veut dire ? Tu dis que je suis bizarre, Hideaki ?"

show hideaki triangle
with charachange


hh "Tu parles beaucoup."


"Mon premier réflexe est de me mettre sur la défensive, mais plus j'y pense, et plus il a raison."


hi "C'est vrai, je parle beaucoup. Ce n'était pas le cas avant."


hi "Je crois... Que c'est probablement la faute de Shizune et Misha. À force de discuter avec elle, j'ai adopté leur logique et leur façon de faire les choses. J'aurais l'impression d’être noyé sous leurs paroles ou mis à part, sinon."

show hideaki confused
with charachange


hh "Ma sœur peut te noyer sous ses paroles ?"


hi "Ce n'est pas comme si elle parlait littéralement plus que moi, bien sûr. C'est difficile à expliquer. Elles ont plus d'énergie que moi. J'ai l'impression de ne pas pouvoir les égaler, mais j'en ai envie. Je crois que ta sœur a cet effet sur les gens."

show hideaki thinking
with charachange

hh "…"


hi "Tu admires ta sœur ?"

show hideaki normal_up
with charachange


"Il me fixe du regard, tendu et confus sur la façon dont il devrait réagir à la question."

show hideaki angry_up
with charachange

stop music fadeout 5.0


hh "Je serai meilleur que Shizune."


hi "Meilleur en quoi ?"

show hideaki angry
with charachange


hh "En... tout."


hi "Comme quoi ?"

show hideaki triangle
with charachange


hh "Je peux faire des tours de magie."


hi "Tu veux dire comme quand tu dis aux gens que tu as leur nez, ou plus le genre de tour de magie où tu sors un lapin de tes fesses ?"


"Il ne semble pas content. Un jour, je verrai Hideaki rire. Je le chatouillerai, s'il le faut."

play sound sfx_doorslam

show hideaki surprise
with vpunch

show hideaki thinking at twoleft
show bg shizu_garden at bgleft
with dissolvecharamove

show jigoro neutral at tworight
with charaenter


"La porte de derrière s'ouvre et Jigoro en sort, gardant son dos droit et faisant de grandes et lentes enjambées, comme s'il était un roi ou un bel idiot."


"J'essaye de me tourner, espérant que si je ne le vois pas, il ne me verra pas. Malheureusement, il ne coopère pas et arrive si vite que c'est comme s'il était apparu directement derrière mon épaule."

show jigoro laugh
with charachange

play music music_happiness fadein 2.0


hx "Oho. Que se passe-t-il ici ? Qu'est-ce que vous faites tous les deux, à faire des gestes dans tous les sens ? Vous jouez au jeu de la ficelle comme des filles ?"


hi "J’apprends un peu la langue des signes à Hideaki. Et vous, M. Hakamichi ?"

show jigoro angry
with charachange


"Il plisse les yeux, soupçonneux, comme s'il n'était pas habitué à ce que les gens soient aussi polis avec lui."


hx "J'écris une autobiographie de ma vie et de mon temps. Et par “écrire” je veux dire que je la dicte à ma biographe. Malheureusement, elle est en retard. Quel manque de professionnalisme."

show jigoro smug
with charachange


hx "Peut-être que tu devrais la lire quand elle sortira plus tard cette année. Je peux te mettre sur liste d'attente. Peut-être que ça te donnera l'indice moral qui semble manquer dans ta vie, et t'inspirer suffisamment pour arrêter d’être un perdant."


"Ça n'est pas normal qu'il insulte tout le monde aussi naturellement que ça."


"Cela dit, Hideaki est sûrement trop détaché pour ne serait-ce que remarquer, Shizune est sourde, et la plupart de ses insultes doivent passer au-dessus de la tête de Misha. Je suis sûr qu'Akira a un avis là-dessus."


"J'essaye de ne pas y penser. S'il fait ça pour me provoquer, alors je dois rester calme ou il gagnera. Il ne doit absolument, définitivement pas gagner. Shizune doit penser comme ça aussi."


hi "Quel âge avez-vous ?"

show jigoro neutral
with charachange


hx "Quarante-six ans."


hi "Ça ne me semble pas suffisant pour justifier une biographie. Je veux dire, ce n'est pas si vieux. La plupart des gens ne commencent pas à écrire leurs mémoires beaucoup plus tard que ça ?"

show jigoro angry
with charachange


hx "La ferme, jeune homme. Je vais te donner un conseil : ne parle pas d'âge à des gens plus âgés que toi. Tu as moins de la moitié de mon âge, tu n'as aucun droit de parler de vieillesse. J'ai un ulcère plus vieux que toi."


"Il devrait se faire examiner pour ça. Il a raison sur un point cela dit, il est bien plus vieux que moi."

show jigoro laugh
with charachange


hx "...De toute façon, même si nous avions le même âge, je n'aurais pas à m'expliquer avec toi, sweat-shirt."

hi "Eugh."

show jigoro angry
with charachange


hx "C'est quoi ce bruit ? Tu es frustré ? Évidemment. Bien. Ton sweat-shirt est horrible, et je veux que tu te sentes mal à cause de ça. Ta réaction me démontre que ça marche."


hi "J'aime mon sweat-shirt."

show jigoro smug
with charachange


hx "Je suis sûr que tu aimes sniffer de la colle, aussi. Ça ne justifie rien."


hi "Je ne sniffe pas de la colle. D’où est-ce que vous avez cette impression ?"

show hideaki normal
with charachange


hh "C'est de la diffamation."


"Je me demande comment Hideaki sait ce qu'est la diffamation. Peut-être que Jigoro est un avocat."


"Ça tiendrait debout, bien que je croyais que des avocats aussi antagonistes ne se voyaient qu'à la télé. Je ne sais pas si je devrais en profiter pour lui demander quel métier il exerce."


hi "Il a raison, c'est de la diffamation. Vous êtes un avocat ?"

show jigoro neutral
with charachange


hx "C'est juste une réflexion basée sur le fait que tu es stupide. C'est comme ta présomption que je suis un avocat qui est sans fondement. Si tu veux le savoir à ce point-là, pourquoi ne précommandes-tu pas mon autobiographie ?"

show jigoro angry
with charachange


hx "Maintenant tu insultes mon livre, et par extension, ma vie entière. Qu'est-ce qui te donne le droit de faire ça ? Arrogant. J'essaye de penser à une manière de te le faire comprendre. Peut-être en te frappant. Avec mon autobiographie."


hx "J’espère que tu en sortiras en ayant appris une bonne leçon, comme ne pas présumer."

show hideaki bored
with charachange


hh "Coups et blessures..."


"Mais il a présumé lui aussi, disant que je sniffais de la colle. J'envisage de lui balancer pour montrer un exemple de son hypocrisie, mais je ne crois pas que ça vaille le coup. Il s'en sortirait sûrement en disant “La ferme, jeune homme”."

show jigoro smug
with charachange


hx "De mon temps, les enfants étaient vus et pas entendus, et être un adulte signifiait avoir expérimenté des moments difficiles."


hx "D'un seul regard, les gens pouvaient juger instantanément le caractère d'un homme. L'enfance n'existait que pour te préparer à l'âge adulte."


hx "Quand tu me regardes, ne peux-tu pas voir mes expériences d'un seul regard ?"


hi "Euh... peut-être. Vous étiez un épéiste ?"


"Il pourrait tout aussi bien être un Hawaïen ou un loup-garou."


hi "Vous ne m'avez pas dit qu'il ne fallait pas présumer ? Maintenant, vous me demandez de le faire. Et vous dites que tout le monde, à votre époque, le faisait. Ça devait être, dans les années 80. C'était il y a même pas si longtemps !"


"Je suis prêt à lui dire ce que je pense, lui qui parle comme s'il avait eu à marcher vingt-cinq kilomètres dans la neige pour prendre un train à charbon, avant de grimper en haut d'une montagne en combattant des ogres, juste pour aller à l'école."


"Mais maintenant que j'ai envie de combattre, Jigoro est content de pouvoir raconter à quel point c'était difficile de grandir il y a une génération, s’arrêtant occasionnellement pour bâiller ou regarder l'heure."


"Le retard de sa biographe est toujours bien présent dans ses pensées. Ça veut dire que tout ce temps où il m'a insulté, il a dû le faire juste pour passer le temps. Et pour ajouter l'injure à l'insulte, sa montre est vraiment très belle."

show jigoro angry
with charachange


hx "...Quand j'avais ton âge, les enfants avaient des responsabilités. Pas comme aujourd'hui. Écœurant."


hx "Personne ne pense aux conséquences de ses actes maintenant. Ils font juste ce qu'ils veulent, pensant que personne ne leur en tiendra rigueur parce qu'ils sont jeunes."


"C'est bizarre, cette description pourrait correspondre à Shizune et Misha. J'ai pensé quelque chose de similaire hier."


hx "Regarde-toi. Un sniffeur de colle amoral et sans but, avec un manque complet de code et aucun sens de la mode. Tu es le Japon de demain. Honteux. C'est ça le futur d'un pays qui était autrefois si grand ?"


hi "Je connais quelqu'un avec qui vous vous entendriez bien."


hx "Ne m’interromps pas ! Qui ? Un de tes amis ? Pourquoi est-ce que je voudrais parler avec un horrible adolescent ? Tu m'as écouté au moins ? Pourquoi es-tu si malpoli, jeune homme ? Ton attitude ne te vaudra pas beaucoup d'amis."


hi "J'aimerais que vous arrêtiez de me donner autant de conseils."


"Ou du moins, j'aimerais qu'il me donne des conseils qu'il ait la décence de respecter lui-même."

show jigoro neutral
with charachange


hx "Où est-ce que tu étais ?"


hi "Hein ?"

show jigoro angry
with charachange

stop music fadeout 3.0


hx "Pas toi, idiot."

show jigoro angry at Position(xpos=0.85)
show hideaki normal at Position(xpos=0.45)
show bg shizu_garden at center
with dissolvecharamove

show shizu behind_blank_cas behind hideaki:
    twoleft
    xpos 0.2
with charaenter

shi "…"


hi "Oups, je ne t'avais pas vue."

show shizu adjust_happy_cas
with charachange


"Shizune sourit et fait un petit signe. Son arrivée rend Jigoro silencieux, je suis content de la voir rien que pour ça."

show shizu basic_normal2_cas
with charachange


ssh "Misha et moi avions décidé de retourner en ville. Hisao, j'ai remarqué que tu regardais des vêtements hier dans une vitrine, et je me suis dit que je pourrais retourner en ville te les acheter. C'était supposé être une surprise cela dit."


"Elle semble déçue que la surprise soit gâchée, bien qu'elle l'ait gâchée elle-même."

show shizu behind_blank_cas
with charachange


ssh "Tiens !"


hi "Merci."

show shizu basic_normal_cas
with charachange


ssh "Misha voulait se couper les cheveux. Je lui ai dit de ne pas le faire, mais elle a insisté, disant qu'il faisait trop chaud l'été."


hi "Ah ouais ? Je sais pas, c'est logique non ? Elle doit avoir vraiment chaud là-dessous. J'ai envie de voir. Où est Misha d'ailleurs ?"


mi "Par ici~ ! Salut, Hicchan~ ! Salut, M. Papa-de-Shicchan~ ! Salut, Hideaki~ !"

show jigoro smug
with charachange

hx "…"

play music music_running

show mishashort hips_grin_cas behind shizu at offscreenleft
with charamoveinright

hide mishashort
with None

show mishashort hips_grin_cas at offscreenleft
with None

show shizu basic_normal_cas:
    xpos 0.3
show jigoro smug:
    xpos 0.95
show hideaki normal:
    xpos 0.55
show mishashort hips_grin_cas:
    center
    xpos 0.1
show bg shizu_garden:
    xpos 0.55
with dissolvecharamove


"Misha court autour de nous en faisant un cercle avant de s’arrêter à côté de Shizune."


"Pour la première fois, elle n'a pas mis ses mains devant mes yeux, et je peux voir qu'elle a des sacs à porter, donc même si elle voulait, elle n'aurait pas pu. Quoiqu'elle en aurait été capable."


"Ses couettes si distinctives ont disparu en faveur d'un style bien plus simple et sportif. Misha semble encore plus joyeuse que d'habitude, probablement parce qu'elle sait qu'elle n'aura pas à se réveiller au petit matin juste pour se coiffer."

show jigoro angry
with charachange


hx "C'est quoi cette coupe ? Tu ressembles à une folle. Ton ancienne coupe te faisait ressembler à un juge avec une perruque. Passer de juge à folle, c'est une belle descente."

show shizu behind_frown_cas
with charachange


ssh "Hisao, est-ce qu'il dit quelque chose d'insultant ? Dis-lui de ne pas insulter mes amis !"


hi "N'insultez pas mes amis."


hx "Lequel de vous est en train de parler ?"


hi "Nous deux. Je suis d'accord avec elle."

show mishashort hips_smile_cas
with charachange


mi "Héhéhé~ ! Qu'est-ce que tu en penses, Hicchan ?"

show shizu adjust_frown_cas
with charachange


ssh "Tu aurais dû rester comme avant."

show mishashort perky_sad_cas
with charachange


mi "Aw~... Hicchan, tu sembles déçu, tu n'aimes pas non plus ?"


hi "Eh bien, ouais, je dois avouer que je préférais ta coupe d'avant, mais je trouve celle-là pas mal aussi. Ça te va bien."

show mishashort hips_grin_cas
with charachange


mi "Aw, merci Hicchan~ !"


hx "Touchant. Si tu l'aimes tant, vous devriez échanger."


hi "On ne peut pas échanger une coupe."


hx "C'est bien dommage. Même son ancienne coiffure irait mieux que celle que tu as, qui est si négligée. Horrible. Quant à toi..."

show jigoro laugh
with charachange


hx "Mmmh... En fait, c'est beaucoup moins criard que l'ancienne. J'aime bien."

show mishashort cross_laugh_cas
with charachange


mi "Ahahahaha~ ! Vraiment ? Merci, M. papa-de-Shizune~ !"

show jigoro angry
with charachange


hx "C'est M. Hakamichi. Parle comme une personne normale."

show mishashort perky_smile_cas
with charachange


mi "Mh~ ? Je ne comprends pas~ ! D'accord, d'accord d'accord~ ! Je vous appellerai M. Hakamichi !"


hx "Arh, c'est comme parler à un sifflet. Méprisable. Où est ma biographe ? Hideaki !"

show jigoro invis
show shizu basic_normal_cas
show hideaki bored
with charaexit


"Il commence à marmonner tout seul en partant. J'imagine qu'un farfelu comme Jigoro est hésitant quand il s'agit de crier sur des filles. Soudainement, il se retourne, incapable de résister à l'envie d'avoir le dernier mot."

show jigoro angry
with charaenter


hx "Et une dernière chose, tu n'as pas à être aussi bruyante. Je n'aime pas les gens qui crient."

show mishashort hips_grin_cas
with charachange


mi "Quoi ? Crier~ ? Je ne crie pas~ !"


"Personne n'est aussi mal placé que lui pour réprimander ceux qui crient sur les autres. C'est comme une parade d'hypocrisie et ça continue encore."


"La situation devient bizarre. Misha semble apparemment trouver Jigoro drôle et rit à chaque fois qu'il dit quelque chose, ce qui le pousse à crier encore plus. Ça, c'est ce qu'on appelle un cercle vicieux."


"La voix de Misha est ponctuée par des explosions de rire qui semblent venir de tous les côtés. En face, Jigoro tire, centré comme un canon. Dans tous les cas, ils sont tous les deux extrêmement bruyants."


"Plus ils parlent et plus le son augmente, d'un niveau à chaque fois."

show mishashort perky_sad_cas
with charachange


mi "Ow~ ! Ça fait mal aux oreilles~ !"


hx "POURQUOI EST-CE QUE TU CRIES ?"

hide shizu
with charaexit

show black
with hands_in


"Shizune, derrière moi, met ses mains devant mes yeux, quelque chose que je croyais que seule Misha faisait, et ça me rend confus, vu que Misha est en face de moi."

show shizu adjust_happy_cas_close at center behind black
show hideaki bored at center
with None

hide black
with hands_out


"Elle me relâche et met un doigt devant ses lèvres."

show shizu behind_smile_cas_close
with charachange


ssh "Profitons-en pendant qu'ils sont occupés ! Partons discrètement."


his "Pourquoi on doit partir discrètement ? On ne peut pas le faire normalement ?"

show shizu adjust_smug_cas_close
with charachange


ssh "Ça ne serait pas aussi drôle."

show shizu basic_happy_cas_close
with charachange


ssh "C'est décidé. C'est une mission secrète. S’échapper sans se faire détecter. Et réussir à extraire Hideaki compte en points bonus."

hide shizu
with charaexit

stop music fadeout 3.0


"Elle a déjà changé la situation en un jeu. Shizune s'éloigne silencieusement et se dirige vers la maison. Je marche en sa direction, normalement."




label fr_S22:

scene bg shizu_living
with locationskip


"Je n'arrive pas à trouver Shizune, mais je la vois finalement dans le salon, sirotant un verre d'eau fraîche et jouant avec ses lunettes de sa main libre. Dès qu'elle me voit, elle les remet."

show shizu basic_normal2_cas at center
with charaenter

play music music_ease fadein 4.0


ssh "Tu n'as pas sauvé Hideaki. Ça veut dire que tu n'auras pas les points bonus. Si tu étais noté sur le style, tu aurais une réduction de points à cause de ton ennuyannnnnnte échappatoire."


his "J'avais l'impression que tu voulais me parler, je ne savais pas qu'il fallait que je le fasse avec style. Tu sais, certains diraient que les gens avec du style sont ceux qui ne s'efforcent pas d'avoir l'air cool."

show shizu cross_wut_cas
with charachange


ssh "Tu es vraiment cool."


"Je me demande comment ça se fait que je comprenne son sarcasme aussi facilement, et comment ça a dû être dur pour elle d'apprendre le concept du sarcasme sans pouvoir entendre. J'ai du mal à imaginer."


his "On dirait que tu es de bonne humeur."


"Bien que je croie que ce n'est pas une vraie bonne humeur. C'est plus qu'elle est très excitée."

show shizu behind_frown_cas
with charachange


ssh "Je suis de mauvaise humeur."

show shizu basic_normal2_cas at Position(ypos=1.1)
with dissolvecharamove


"Posant son verre, Shizune s'assied sur le canapé."

show shizu behind_frown_cas
with charachange


ssh "Je préférais bien plus son ancienne coiffure. C'était si joli. Raffiné et méticuleux. Maintenant ça fait sportif et garçon manqué."


his "Je ne dirais pas que Misha est raffinée et méticuleuse. Ça te ressemble plus. Tu devrais lui donner une chance. Fais pousser tes cheveux et fais les ressembler à des forets."


his "Mh... en fait, non, reste comme ça."

show shizu adjust_frown_cas
with charachange


"Shizune réajuste ses lunettes, visiblement énervée par les implications de mes propos. C'était voulu après tout. Elle s'approche un peu de moi alors que je m'assois."

show shizu basic_angry_cas
with charachange


ssh "Je suis un garçon manqué ?"


his "Eh bien, personne ne dirait ça. ...Basé sur les apparences."


"Shizune me fixe du regard, pas amusée du tout. Je dois lutter pour garder une expression neutre."


his "Peut-être que vous devriez échanger vos coupes."

shi "…"

show shizu behind_frown_cas
with charachange


ssh "Tu parles comme mon père."

show shizu adjust_smug_cas at center
with Dissolvemove(0.2)


"C'est vrai. Shizune rit un peu sans bruit en voyant mon agacement. Se relevant d'un coup, elle fait tourner une épée invisible de sa main gauche tout en se tenant de manière militaire et grimace. Une imitation très bien faite."

show shizu basic_frown_cas
with charachange


ssh "Bref, je ne recevrai pas de conseils de la part de quelqu'un qui porte un sweat-shirt bleu avec un pantalon marron. Où est ton sens de la coordination des couleurs ? Épouvantable."

show shizu adjust_smug_cas
with charachange


ssh "...Mais ça pourrait être fun de changer de coupe. Tu ne penses pas ? Je me demande comment tout le monde réagirait."


his "Tu dois vraiment aimer jouer avec les gens. Des fois, un peu trop même."

show shizu adjust_frown_cas
with charachange


"Pas de réponse. La façon dont elle joue avec ses lunettes, les sourcils froncés, me montrent que j'ai raison."

show shizu behind_blank_cas
with charachange


ssh "C'est fun."



"Puis, avec plus de confiance, elle se rapproche de moi."

show shizu basic_happy_cas
with charachange


ssh "C'est fun d’entraîner de plus en plus de personnes dans ma vie."


his "Oh, je vois."


"Je me demande si je suis inclus dans cette remarque. J'ai envie de demander, mais ne sais pas trop comment le formuler."

show shizu adjust_happy_cas
with charachange


"Shizune agite un doigt, indiquant qu'elle ne répondrait pas à une telle question de toute façon."

stop music fadeout 0.5

show shizu adjust_blush_cas_close
with vpunch


"Elle essaye d'atteindre son verre, mais ne semble pas réaliser qu'elle s'est éloignée de l'endroit où elle l'a posé tout à l'heure. Pour pouvoir se pencher plus, Shizune s'accroche à moi et finit par me faire basculer sur elle."

scene ev shizu_couch
with vpunch

play music music_serene fadein 9.0


"Alors que je me retrouve sur elle, je peux sentir sa chaleur corporelle et réalise à quel point nous sommes proches. Je peux entendre sa légère respiration et le frottement de ses vêtements alors qu'elle remue un peu."


"Ses joues commencent à rougir, mais ses yeux restent rivés aux miens, sombres et immobiles."


"C'est le même regard que quand je l'ai vue pour la première fois, perçant et n'affichant aucune émotion claire. Attendant juste ce qu'il va se passer, comme les yeux d'un chat. Ça me met mal à l'aise d’être regardé d'une telle façon."


"C'est la première fois que je suis aussi proche d'elle pendant aussi longtemps, et l’atmosphère est différente maintenant. La situation n'est pas la même que quand je lui touche passagèrement la main ou quand on joue avec Misha."


"Les doigts de Shizune bougent un peu hasardeusement, mais elle ne signe rien. Son regard veut dire quelque chose, contrairement à ce que je pensais. Elle attend que je fasse quelque chose. Je me demande si j'ai répondu à ses attentes jusque-là."

scene bg shizu_living
with vpunch

show shizu behind_blank_cas_close
with charaenter


"Elle m'attrape doucement par les épaules et me repousse gentiment, mais fermement. Je me recule et me retrouve assis sur le sofa à moins de trente centimètres d'elle. Mais je le ressens comme si elle m'avait repoussé d'un kilomètre."


"Quand j'y pense, c'est peut-être la façon la plus radicale de repousser quelqu'un dans le langage des signes. Shizune dit que le fait qu'on doive signer tout ce qu'on dit oblige l’exécutant à réfléchir avant de parler."


"Mais d'un autre côté, ça veut aussi dire que ce qui serait juste un silence gênant en temps normal est là un mur insurmontable. Je dirais quelque chose, n'importe quoi, pour essayer d'apaiser la tension si je le pouvais, mais je ne peux pas."


"En temps normal, je crois qu'il serait normal de juste s'excuser et peut-être partir. Mais maintenant, je me demande si c'est applicable. Ça serait une action qui avouerait trop ma culpabilité. Comme si je ne voulais pas."


"Bien sûr, ce n'est pas comme si je pouvais faire comme si rien n'était arrivé. Ça serait une insulte pour nous deux. Donc même si je ne veux pas, je m'excuse rapidement, tellement que j'en oublie de le signer et retourne à ma chambre."

window hide None

scene bg shizu_guesthisao_ss
with locationskip

play sound sfx_pillow
with vpunch

$ renpy.music.set_volume(0.5, 1.0, channel="music")

show black
with shuteye

window show


"Soupirant, je me laisse tomber sur le lit. J'aimerais pouvoir me rendormir maintenant, mais je suis trop éveillé."

play sound sfx_doorclose
$ renpy.music.set_volume(1.0, 3.0, channel="music")

with Pause(3.0)

show shizu basic_normal2_cas_close
hide black
with openeye


"Je me redresse quand j’entends la porte se fermer et ouvre les yeux pour voir Shizune assise sur la chaise en face de moi."

show shizu behind_blank_cas_close
with charachange

shi "…"


"Elle pose une question que je ne comprends pas, à cause de l'effet de surprise. Elle le voit, je ne crois pas qu'elle l'ait fait exprès. Quoi qu'elle ait dit, elle le retire et ne redit rien pendant un moment."

show shizu adjust_happy_cas_close
with charachange


ssh "C'est la première fois que je viens dans ta chambre."


"Shizune s'efforce d'afficher un air embarrassé à cette pensée. Je n'arrive pas à apprécier la blague, le fait qu'elle soit là me perturbe un peu."


his "Très drôle. Ce n'est même pas ma chambre, c'est ta chambre d'ami."


label fr_S22a:


his "Et puis de toute façon, tu es déjà entrée dans ma chambre avec Misha, une fois."

show shizu behind_blank_cas_close
with charachange


"On dirait qu'elle s'attend à ce que j'en dise plus. Je me rappelle avoir paniqué quand elles sont entrées dans ma chambre, effrayé de ce qu'elle pourraient penser en voyant l'armée de flacons de pilules. Mais je ne crois pas que Shizune s'en rappelle."

show shizu basic_normal_cas_close
with charachange


ssh "Ça t'a rendu nerveux."


label fr_S22b:


ssh "Tu avais l'air surpris quand je suis entrée."


label fr_S22c:


"La façon dont elle le dit m’embête."


his "Beaucoup de choses me rendent nerveux."


his "Tu es l'une d'entre elles."

show shizu behind_blank_cas_close
with charachange


shi "... ?"


his "Parce que tu inclus trop facilement les gens dans... tout ce que tu fais. Que ce soit rejoindre le Conseil des Étudiants ou même faire une pause. Qu'ils le veuillent ou non."

show shizu basic_angry_cas_close
with charachange

shi "…"

show shizu adjust_happy_cas_close
with charachange

shi "… … … …"

show shizu basic_normal2_cas_close
with charachange

shi "… …"


"Elle signe très rapidement, s’arrêtant bien trop souvent au milieu d'un geste, rendant les mots trop informes pour que je puisse les comprendre. J'essaye de ne pas le laisser transparaître."


"Ça semble marcher, mais elle a l'air un peu triste, et je regrette de n'avoir rien à dire pour enlever l'expression mélancolique et distante qu'elle affiche. Tout ce que je peux faire est attendre qu'elle dise quelque chose."

show shizu behind_sad_cas_close
with charachange


ssh "Tu as raison. Je veux entraîner tout le monde dans ma vie. Mais récemment, je ne suis plus sûre que ce soit la bonne chose à faire."


his "J'ai apprécié que tu m’emmènes à ton restaurant favori l'autre soir."

show shizu basic_normal_cas_close
with charachange


ssh "Ce n'est pas mon restaurant favori... J'en aime d'autres. Je pourrais même les numéroter."


his "Ah bon..."

show shizu adjust_frown_cas_close
with charachange


ssh "Cette chaise est trop inconfortable. Je veux m'asseoir sur le lit."


"Lui faisant signe d'y aller, je m'attends à ce qu'elle se lève et vienne s'asseoir. Elle ne le fait pas et trouve ça amusant."

show shizu behind_smile_cas_close
with charachange

stop music fadeout 5.0


ssh "Ferme les yeux."


his "Pourquoi ?"

show shizu adjust_smug_cas_close
with charachange


ssh "C'est une surprise."

show black
with shuteye


"Je décide de coopérer et les ferme. Je peux sentir qu'elle se penche sur moi et soudainement, quelque chose de doux et humide me touche les lèvres. Mon corps entier se tend à cause de la surprise."


"C'était rapide, et alors que je pense que c'est fini, elle m'embrasse encore une fois, plus fort cette fois. Ses mains glissent sur mes épaules, remontent sur ma nuque avant de redescendre sur mes épaules puis mes bras."


"Je peux sentir le poids de son corps sur mes jambes et l’érotisme de la situation ne m'échappe pas. À ce point, je suis prêt à essayer d'ouvrir un peu les yeux, mais comme si elle s'y attendait, elle passe sa main sur mes yeux."

play sound sfx_rustling


"Quelques secondes plus tard, quelque chose m'entrave les mains au niveau des poignets et je panique. Ma première pensée est de demander à Shizune à quoi elle pense. Même si elle ne peut pas m'entendre, je suis sûr qu'elle peut comprendre."


"Elle ne me lâche pas les mains, passant ses doigts dessus, sur ma paume, mes doigts et mes poignets."

scene evh shizune_hcg_tied_stare:
    yalign 0.0 xalign 1.0 subpixel True
    easein 6.0 xalign 0.5 zoom 0.5
    truecenter
    zoom 1.0
    "evh shizune_hcg_tied_stare_small"
with whiteout

play music music_heart fadein 5.0


hi "Hé qu'est-ce que tu fais ? C'est quoi ça ?"


"Bien sûr, avec les mains attachées derrière le dos, je pourrais tout aussi bien être bâillonné. Je me demande si ce n'est pas ce qu'elle voulait."

scene evh shizune_hcg_tied_smile_small
with charachange


"Comme si elle lisait mes pensées, une expression malicieuse s'affiche sur son visage, mais son rougissement ne s'en va pas. En fait, il s'accentue encore plus quand nos regards se rencontrent."


"Embarrassée, elle se penche un peu plus, cachant son visage dans mon cou. Ses cheveux sont doux et me chatouillent, et je laisse échapper un rire sachant qu'elle ne m'entendra pas, et ne sera pas offensée."

label fr_S22h:

scene evh shizune_hcg_tied_blush_small
with charachange


"Les mains de Shizune descendent jusqu’à la braguette de mon pantalon, couverte de sa jupe. Ses mains disparaissent avant de réapparaître, surprise par mon érection. C'est comme si elle ne s'attendait pas à ce qu'elle soit là."


"La naïveté qu'elle montre est en contraste net avec le fait qu'elle ait été directe jusque-là, et je trouve cela amusant. Encore une fois, elle semble très immature. Une lycéenne jouant le rôle d'une femme agressive."

scene evh shizune_hcg_tied_blush:
    yalign 0.0 xalign 0.8
show evh_hi shizune_hcg_tied_hisao2:
    yalign 0.0 xalign 0.8
with flash


"Elle touche curieusement mon pénis du bout de l'index, son visage rougissant alors qu'elle passe ses doigts autour. Ses mouvements sont timides et curieux, et ils s'accordent avec l'air embarrassé qu'elle affiche sur son visage."

show evh shizune_hcg_tied_stare
hide evh_hi
with charachange


"Shizune est sûrement aussi nerveuse que moi, donc je suis un peu soulagé quand elle s’arrête, mais alors je pense à ce qui va venir ensuite."


"Elle voudra peut-être déboutonner ma chemise. Je ne sais pas pas ce qu'elle dira quand elle verra la cicatrice sur ma poitrine. Je peux imaginer l’inquiétude sur son visage quand elle la verra, les doigts immobiles pendant qu'elle réfléchira."



"Heureusement, dans cette position, elle ne pourra pas retirer mon sweat-shirt, à moins de me l'arracher. La peur s’évanouit un peu. Maintenant, j'expérimente un étrange mélange d'anticipation et de nervosité."

show evh shizune_hcg_tied_blush
with charachange


"Une légèreté retrouvée sur mes jambes me force à revenir à la réalité, et je peux voir Shizune se tenir sur la pointe des pieds et faire glisser sa culotte le long de ses jambes. Quand elle me voit la regarder, elle essaye de me couvrir les yeux d'une main."


"Je me demande quand j'ai commencé à être attiré par elle. Pas juste tenté physiquement, mais vraiment attiré par elle. Je me demande pourquoi. Elle est belle, mais aussi très combative. Pas juste ça, mais elle semble aimer être comme ça."

scene evh shizune_hcg_tied_blush_small
with charachange


"La façon dont elle agit maintenant cela dit, et à d'autres moments, ne correspond pas à cette image. Je commence à croire qu'elle m'a peut-être attaché les mains pour des raisons autres que celle qui est évidente."


"Cela dit, cette agressivité qu'elle a tout le temps et qu'elle sort comme une carte de visite est réelle. Je ne sais pas si ce genre d'attitude peut être considérée comme dangereuse. Si elle l'est, je me demande quel genre de personne cela fait de moi."


hi "C'était probablement durant ma première semaine. Une semaine qui ne semble pas si longue quand j'y pense, mais à l'époque elle l'était. Même si je comptais les journées cette semaine-là, ça semblait aller très lentement."


"Même si elle ne peut pas m'entendre, parler me rassure."


hi "J'ai commencé à réaliser que je n'avais pas de raison de me plaindre. Mais pourtant..."


hi "Bah, peu importe."

scene evh shizune_hcg_tied_stare_small
with charachange


"Elle me regarde, simplement parce que je parle. Parce qu'elle ne peut pas comprendre ce que je dis, Shizune devient de plus en plus troublée, mais ne signe rien en réponse."

scene evh shizune_hcg_tied_close_small
show evh_hi shizune_hcg_tied_hisao2_small
with charachange


"Shizune respire brusquement tandis qu'elle s'abaisse sur mon pénis, essayant de rester droite alors qu'elle vacille sur moi."


"La jupe de sa robe couvre nos parties intimes et garde la chaleur de nos corps comme une tente. En dessous, il fait très chaud, et la main de Shizune qui me guide en elle ne fait que faire monter la chaleur."

show evh shizune_hcg_tied_kinky3_small
with flash


"À la seconde où je la pénètre, Shizune grimace et en tombe presque sur moi. La soudaine sensation est engourdissante et je sens plusieurs vagues de plaisir parcourir mon corps dans son intégralité."


"J'ai l'impression que le bas entier de mon corps est enveloppé dans la chaleur et l'humidité du corps de Shizune, capable de sentir chaque mouvement et frisson alors qu'elle commence à bouger."

show evh shizune_hcg_tied_kinky2_small
with charachange


"Shizune commence à bouger ses hanches d'avant en arrière, d'abord doucement, puis son rythme s'intensifie à chaque fois qu'elle se retire presque complètement de moi avant de redescendre à la dernière seconde."

scene evh shizune_hcg_tied_kinky2:
    zoom 1.0 yalign 0.1 xalign 0.7
    acdc_warp 6.0 xalign 0.9
with flash


"Étant si proche d'elle, je peux voir la transpiration perler sur sa peau et la buée qui se forme sur ses lunettes alors qu'elles glissent sur son nez avant qu'elle ne les remette."


"Le bout de ses doigts appuie sur mes épaules, elle me serre fermement pour se tenir, s'appuyant dessus pour se soulever puis abaisse ses mains sur mes bras et tient mes poignets et mes mains tandis qu'elle se rabaisse."

scene evh shizune_hcg_tied_close_small
with flash


"Bouger comme ça est vraiment difficile. Shizune essaye de s'accrocher à moi pendant qu'elle se soulève et se rabaisse avec ses pieds. J'essaye de l'embrasser, mais réussis seulement à cogner mon front contre le sien, au moins pas douloureusement."


"Je me demande brièvement si la porte est verrouillée. Si elle venait à s'ouvrir, j'aurais probablement une crise cardiaque, littéralement. Et encore viendrait la question de qui ouvrirait la porte."


"La sensation de danger n'arrive qu'à rendre les mouvements de Shizune encore plus tortueux, et j'aimerais qu'elle aille plus vite, mais dans cette position ça doit être difficile."

show evh shizune_hcg_tied_kinky1_small
show evh_hi shizune_hcg_tied_hisao2_small
with charachange


"Je commence à bouger mes hanches en rythme avec elle, essayant d'aller plus profondément en elle. Peu importe que mes mouvements fassent bouger la chaise sur laquelle on est, faisant du bruit alors que la chaise frotte contre le sol en bois."

$ ksgallery_unlock("evhul shizune_hcg_tied_hisao2_small")
show evh shizune_hcg_tied_kinky3_small
with charachange


shi "...nn... !"


"Sa respiration se fait plus forte, et des gémissements réprimés s’échappent même de sa bouche. Bien qu'il soit évident qu'elle veut les contenir, ils sont suffisamment bruyants pour être audibles par n'importe qui se tenant hors de la pièce."


"J’arrête de bouger, partiellement parce que c'est de plus en plus dur de continuer en même temps qu'elle tandis qu'elle bouge de plus en plus vite."

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.4)

window show


"Mon cœur commence à s’accélérer et je peux presque entendre le sang dans mes tempes, et plus inquiétant, je peux sentir une pulsation lourde dans ma poitrine. J’arrête de penser à ce que je ressens au bas-ventre, seulement pour un moment."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene white
with whiteout


"Ce moment, cela dit, est suffisant. La sensation d'être serré étroitement à l'intérieur de son corps et sa peau frottant contre la mienne permet d'atteindre ma limite, je me tends et jouis à l'intérieur de Shizune."

label fr_S22x:

$ renpy.music.set_volume(1.0, 2.0, channel="music")
$ renpy.music.play(music_heart, fadein=2.0, if_changed=True)

scene evh shizune_hcg_tied_close:
    yalign 0.1 xalign 0.8
show evh_hi shizune_hcg_tied_hisao2:
    yalign 0.1 xalign 0.8
with Dissolve(2.0)


"Après coup, j'écoute le bruit du battement de mon cœur ralentir jusqu’à ce qu'il atteigne un rythme normal. J'écoute la respiration de Shizune tandis qu'elle fait de même."

hide evh_hi
with charachange


"Ses lunettes sont légèrement de travers et c'est la première fois qu'elle ne les remet pas immédiatement. J'ai envie de les redresser pour elle, mais à la seconde où j'essaye, je me rappelle que je ne peux pas. Shizune semble l'avoir oublié aussi."

stop music fadeout 7.0

scene evh shizune_hcg_tied_close_small:
    truecenter
    subpixel True zoom 1.2
    easein 10.0 zoom 1.0
with Dissolve(2.0)


"Au lieu de se lever, elle se presse contre moi pour pouvoir atteindre mes mains. C'est presque comme si elle n'avait pu penser qu'à cette position pour me détacher. C'est ce que je crois tandis qu'elle me desserre les poignets."


"Cela dit, elle ne s’enlève pas de moi. Ses doigts passent gentiment sur mes mains, glissant sur mes paumes. C'est drôle, je me sens plus connecté à Shizune par cet acte que par ce qu'on a fait jusqu’à maintenant."


"Shizune reste pressée contre moi encore un moment. C'est un peu inconfortable, mais ça me fait plaisir. Comme si je pouvais rester comme ça pendant des heures."

scene black
with dissolve

label fr_S23:

scene bg shizu_guesthisao
with locationchange

play music music_daily fadein 0.5


"Les jours depuis celui-là passent si rapidement que j'ai l'impression que c'est de l'eau entre mes doigts. Chaque fois que j'ai essayé de parler à Shizune, elle était partie faire les courses, ou était avec Misha. J'ai l'impression qu'elle m'évite."


"Je ne suis pas surpris. Bien sûr que ça me gêne, mais je crois que c'est assez naturel comme réaction. Encore une fois, ce n'est pas comme si j'avais été dans cette situation auparavant."

scene bg shizu_living at left
show mishashort perky_smile_cas at center
with locationskip


"À chaque fois que je ne peux pas trouver Shizune, je finis par tomber sur Misha, et quand ça arrive, je lui demande de m'aider pour mes signes. Mais elle finit toujours par s’éclipser. On part demain, je ne vais pas la laisser s'échapper cette fois."


"Une fois qu'on sera retournés à l'école, on aura probablement du travail à faire pour le conseil des étudiants en vue de la reprise des cours. J'ai envie d'affiner mes signes autant que je le peux d'ici là, même si c'est juste pendant une journée."


hi "Allez, c'est comme si on discutait en signant ! Tu fais ça tout le temps. En fait, tu le fais en ce moment même."

show mishashort cross_laugh_cas
with charachange


mi "Wahaha~, vraiment, Hicchan ? C'est drôle !"


"Misha arrête temporairement ses signes automatiques pour pouvoir secouer les mains devant elles pour nier, mais se remet vite à traduire tout ce qui se dit."

show mishashort sign_confused_cas
with charachange


mi "Hicchan, tu es vraiment insistant. Être soudainement aussi intéressé par la langue des signes... se pourrait-il que Hicchan veuille faire carrière là-dedans ? C'est pas juste, c'est moi qui ai eu l'idée la première~ !"

show mishashort cross_frown_cas
with charachange


mi "Mais fais attention, Hicchan. Les temps changent trop vite~... Quand j'ai décidé que je voulais être interprète, ils sortaient des téléphones où on pouvait écrire des paragraphes entiers. Impressionnant~ ! Pas très bon pour moi !"


"Comme si elle savait qu'elle ne pourrait pas reporter cette fois, Misha change de disque assez rapidement pour un ton désolé."

show mishashort perky_sad_cas
with charachange


mi "Je suis désolée, Hicchan, je suis juste si~ fatiguée~ ! Surtout récemment, même si être avec Shicchan est fun, elle a beaucoup plus d'énergie que moi ! Enseigner en plus de ça serait trop~ fatigant. Je n'ai pas autant d'énergie ! Désolée~ !"


"Elle ne semble pas très fatiguée, à crier avec sa vigueur habituelle. Je sais que c'est méchant de ma part d'insister comme ça, cela dit."

show mishashort sign_smile_cas
with charachange


mi "En fait~, Shicchan et moi prévoyions d'aller faire du shopping aujourd'hui ! C'est notre dernière chance de prendre quelques souvenirs."


hi "Souvenirs hein ? J'ai presque oublié qu'on était en vacances."


hi "Je comprends ce que tu veux dire. Enseigner ne semble pas si facile. Hideaki m'a demandé de lui apprendre la langue des signes et j'étais complètement perdu tout le long."


hi "Je me demande comment tu t'en sortiras quand tu seras devenue une enseignante de langue des signes. Ça ne fatigue pas trop comme travail."

show mishashort perky_confused_cas
with charachange


mi "Ouais, c'est vrai, c'est vrai~ ! J’espère pas !"

show mishashort hips_smile_cas
with charachange


mi "Hicchan, maintenant je suis un peu inquiète. Mais~, souvenirs ! Donc~ ! Une prochaine fois, Hicchan. Aha hahaha~. Tu veux qu'on te prenne quelque chose, aussi ?"


"Le fait que je comprenne ne veut pas dire que je ne veux pas qu'elle m'aide. J'imagine que je ne peux pas la forcer de toute façon. Même moi je suis gêné par le fait que ce serait très égoïste. J'abandonne."


hi "Non, ne me prends rien. Je suis sérieux, ne reviens pas avec un t-shirt bizarre ou autre, d'accord ?"

show mishashort cross_grin_cas
with charachange


mi "Heheheh~."


"Je n'aime pas ce ton."

hide misha
with charaexit


"Mettant ses chaussures, elle crie au revoir dans la maison vide mis à part moi, et ouvre la porte pour partir. Une touffe de cheveux foncés de l'autre côté de la porte m'indique que Shizune l'attendait à l'extérieur."


hi "Bonjour."

show mishashort invis:
    center
    xpos 0.8
show shizu invis:
    center
    xpos 1.0
with None

show bg shizu_living at right
show shizu adjust_happy_cas at tworight
show mishashort perky_smile_cas at center
with Dissolvemove(2.0)


"Misha traduit pour moi et Shizune se tourne pour me faire un petit signe."


"Bien que ce soit différent de ses salutations désinvoltes habituelles, il y a une hésitation qu'on ne peut pas manquer. Ça me donne une impression de vide et de distance entre nous."

show shizu behind_blank_cas
with charachange

shi "…"

show mishashort hips_grin_cas
with charachange


mi "Hicchan, tu es là tôt~ ! J’interromps quelque chose ?"


hi "J'essayais de persuader Misha de m'apprendre un peu de langue des signes, mais j’étais impatient, ça peut attendre. Vous avez du shopping de prévu aujourd'hui, après tout."


"Ayant Misha, j'oublie de signer tout ce que je dis, malheureusement, vu que Shizune s'est avancée dans l'encadrement de la porte, Misha est derrière elle. Ce mauvais alignement signifie que tout ce que je dis est perdu."

show shizu basic_angry_cas
with charachange


ssh "Je ne te comprends pas."


"Il y a des choses que je veux dire que je ne serais pas capable de formuler et il y a des conversations entières qu'elle pourrait avoir que je ne comprendrais pas du tout. Je veux lui dire que ça ne sera plus le cas longtemps."

hide shizu
hide mishashort
with charaexit


"À la place je dis juste “peu importe” et leur dis de bien s'amuser, et leur fais un signe d'au revoir."


"On dirait que tout le monde est sorti pour la journée, alors je m'assieds sur la chaise la plus grande et la plus confortable du salon avec un livre. Pas un livre de langue des signes, mais un des romans que j'ai pris à la bibliothèque la première semaine."


"C'était il y a longtemps. Je devrais vraiment m'attaquer à cette pile de livres empruntés, ou au moins les rendre."

stop music fadeout 2.0

show jigoro neutral at center
with charaenter


"Seize pages plus tard, Jigoro entre dans la pièce, une pile de papiers dans une main et son épée qu'il fait tourner dans l'autre, s'ébouriffant occasionnellement les cheveux, mouillés par une douche récente."

show jigoro angry
with charachange

show jigoro angry at Position(ypos=1.15)
with charamove


"Se rendant compte que je le vois faire quelque chose d'incorrect, il s'immobilise comme un lapin pris dans les phares, et se dirige lentement vers la cheminée avec de la colère dans ses pas, avant de s'asseoir sur le sofa."


"C'est seulement la troisième fois que je le vois et je me sens déjà nauséeux quand il apparaît. J'imagine que c'est dû à un certain charisme."


"Je n'ai encore rien dit, qu'il semble déjà mécontent. C'est sûrement une mauvaise idée de le provoquer, et lui parler compte sûrement comme tel. Cependant, je ne peux pas m’empêcher de penser que les alternatives ne seraient guère mieux."


"Disons que je ne dis rien et que je pars, peut-être pour aller lire dans ma chambre ou dehors. Ça serait définitivement une insulte impardonnable. Il me dirait probablement de rester et me détruirait. Dans tous les cas, ce n'est pas poli de ma part."


hi "Qu'est-ce que vous lisez ?"

show jigoro smug
with charachange

play music music_another fadein 6.0


hx "L'ébauche de mon autobiographie. C'est l'histoire d'un homme qui se réveille et trouve un invité indésirable dans son salon, assis dans sa chaise et lisant un dreck littéraire."



"J'ai à peine commencé à lire le livre et n'ai même pas encore d'opinion. Je vois déjà comment la conversation va tourner, donc je pourrais tout autant essayer de la rediriger."


hi "Où est Hideaki ?"

show jigoro angry
with charachange


hx "Tu poses même les questions de manière impolie. Honteux. Cela dit, pourquoi est-ce que tu me poses une question aussi stupide ? Comment est-ce que je saurais ? Suis-je le gardien de mon fils ?"


"“Eh bien, vous êtes son père, et apparemment il vit ici, alors...” Mais je ne peux pas dire ça, même si c'est tentant."


"J'abandonne. J'ai essayé de discuter avec lui et j'ai échoué. C'est comme parler à un mur de brique qui vous déteste. Ça me suffit pour partir, je fouille dans mon portefeuille pour voir si j'ai assez d'argent pour aller voir un film."


"Alors que je suis sur le point de me lever, j'hésite. J'en ai marre d'essayer de solutionner mes problèmes en m'enfuyant."


"C'est hypocrite de ma part d'en vouloir à Misha d'essayer de reporter les choses quand je fuis ma propre petite copine. Quand Jigoro essaye de m’arrêter, je suis presque soulagé, même si je n'ai plus l'intention de partir."

show jigoro neutral
with charachange


hx "Attends."


"Il dit ça avec autorité mais rien d'autre, comme si c'était un ordre à la dernière seconde. Seule une personne très puissante ou très arrogante peut dire à quelqu'un d'attendre d'une telle manière. Je suis un peu impressionné."

show jigoro smug
with charachange


hx "Tu es dans le Conseil des Étudiants avec Shizune, non ? Quel est ton travail exactement ?"


hi "Je ne crois pas qu'on ait des rôles spécifiques, outre la présidente. Shizune essaye toujours d’enrôler les gens pour aider. Généralement, on peut avoir une personne pour aider sur un projet précis, mais sinon on fait tout ce qui doit être fait à trois."


"Je me suis fait la réflexion plusieurs fois quand je l'ai rencontrée, me disant que le regard analytique de Shizune pourrait être dû à sa surdité, mais il s’avère que c'est un trait partagé par tout le monde dans sa famille."

show jigoro neutral
with charachange


hx "Et ça te convient ?"


hi "Pourquoi ça ne serait pas le cas ?"

show jigoro laugh
with charachange


hx "Shizune, toi, et cette fille aux cheveux roses ? C'est vraiment le Conseil des Étudiants dans son intégralité. ?"

show jigoro smug
with charachange


hx "Avec un Conseil des Étudiants aussi petit, ils ne devraient même pas s’embêter à faire des élections. Je parie que tu n'as pas rejoint le Conseil des Étudiants, Shizune t'a enrôlé. Tu as dit que tu ne savais pas quel était ton rôle."


hx "C'est logique. J'imagine que si tu n'as pas été élu, tu ne peux pas savoir. Après tout, si tu n'es pas élu, tu n'es pas grand-chose."

show jigoro laugh
with charachange


hx "Personne ne va respecter un Conseil des Étudiants comme ça. Un corps qui n'a pas été élu et qui est composé de trois personnes essayant de grappiller l’équivalent de travailleurs à temps partiel ?"


hx "Ça doit être une pauvre école si trois enfants buvant le thé peuvent gérer tous les problèmes."


hi "Quelle importance, le nombre de personnes du conseil ? Si le Conseil des Étudiants fait son travail, ça ne suffit pas ?"


hi "Ce n'est pas un jeu, non plus. Peut-être que vous devriez venir à l'école un jour. Si vous venez les bons jours, vous pourrez même voir ce que Shizune est capable de faire."

show jigoro angry
with charachange


hx "Tu crois que j'ai tellement de temps libre que je peux me permettre de passer par ton bled et regarder les exploits d'autosatisfaction de ma fille ? Je n'ai jamais été aussi dégoûté de ma vie."


hi "Ce que vous dites, c'est qu'ils feraient aussi bien de ne pas avoir un Conseil des Étudiants, mais le fait est qu'il y en a un. Et Shizune a été élue pour celui-ci, et pour elle ce n'est pas une position sans intérêt. En fait, elle travaille très dur pour ça."

show jigoro laugh
with charachange


hx "On dirait que tu as voté pour elle."


hi "Non, je n'étais pas là pour ça."

show jigoro neutral
with charachange


hx "Ha. Tu n'as même pas voté pour elle. Bon, à part ça - pourquoi tu ne demandes pas à Hideaki ?"

show jigoro smug
with charachange


hx "Shizune voulait être présidente du Conseil des Étudiants du lycée depuis le collège. Elle lui faisait relire tous les discours d’entraînement, gâchant son temps, pour quelle raison ?"


"Pendant tout ce temps il n'a même pas levé les yeux de son manuscrit. C'est assez énervant."


hi "Parce que ce n'est pas un jeu. Nous ne régnons pas sur l'école, mais ce n'est pas comme si on jouait juste sans prendre ça au sérieux."


"Je me demande si c'est si mal de ne pas être un puriste."

show jigoro angry
with charachange


hx "Je suis allé dans ton école. Vraiment... Les étudiants là-bas..."


"J'imagine déjà un million de choses qu'il pourrait dire, et je me prépare à n'importe laquelle. C'est drôle, mais ça sera probablement des choses auxquelles j'ai déjà pensé."


hx "Ils n'ont pas de corvée de nettoyage."


"Je ne m'y attendais pas du tout. Et il a tort."


hi "Si. Je suis bien placé pour le savoir, je peux éviter la corvée vu que je suis dans le Conseil des Étudiants."

show jigoro neutral
with charachange


"Le principe d'avoir tort rend Jigoro confus. Je devrais profiter de l'opportunité pour attaquer. C'est vraiment bizarre que je réfléchisse comme ça pour une simple conversation."


hi "On dirait que ça fait un moment que vous n'y êtes pas allé."


hi "Si vous pouvez écrire vos mémoires, vous pouvez parler à Shizune de temps en temps. Vous ne pensez pas que c'est le genre de chose dont elle est fière ?"


hi "C'est comme ça que sont les jeunes. On a des choses dont on est fiers. Si vous écrivez une autobiographie, vous devriez le savoir."


"Une si belle opportunité, et je l'ai gâchée. Je ne sais pas à quelle réaction de sa part je m'attendais. Jigoro semble devenir de plus en plus en colère à chaque seconde. Et pourtant, il semble plus calme. Plus sûr de lui et confiant."

show jigoro angry
with charachange


hx "Qui es-tu pour dire que ma vie est si facile ? Tu n'as même pas lu ma biographie, et pourtant tu es capable de me dire comment gérer mes affaires, et comment m'occuper de ma propre fille. Tu ne pourras jamais comprendre."


hx "Même si j'en venais à me lever de ce canapé, marcher jusqu’à toi et te frapper au visage avec un poing américain contenant une édition condensée de ma vie inscrite dessus, laissant ma biographie marquée sur ton visage, tu ne comprendrais pas."


hx "Pendant douze ans, Shizune ne m'a pas parlé, même en ayant engagé de multiples tuteurs et interprètes de toutes sortes pour essayer de la faire devenir normale. Ce n'est pas aussi simple que tu le crois."

show jigoro smug
with charachange


hx "Si elle ne veut pas s’embêter avec moi, alors d'accord. J'estime que c'est normal. C'était quand la dernière fois que tu as parlé à tes parents ?"


"Ça fait un moment et je m'en sens honteux. Plus que ça, il me montre à quel point ça aurait été facile de donner un coup de fil à mes parents ou de leur envoyer un e-mail, ou même une lettre, et je ne l'ai pas fait. Ça me rend vraiment honteux."

show jigoro laugh
with charachange


hx "Je me disais bien."


hi "Si je voulais voir mes parents, je ne pourrais pas. C'est différent. Vous n'êtes pas si éloignés que ça, ce n'est qu'un voyage en train !"

show jigoro neutral
with charachange


hx "Ça suffit. Non signifie non. Tu es très insistant. Si seulement c'était pour quelque chose qui a un intérêt. Je ne vois pas ce que tu as pu apprendre de ma fille à part comment attaquer les gens dans une discussion. C'est ça ?"

stop music fadeout 10.0


"La réponse est oui. Je n'étais pas aussi insistant et prêt à argumenter avant de rencontrer Shizune et Misha. Après tout, avant de les rencontrer, je venais juste d'expérimenter une petite mort."


"Je ne sais même pas pourquoi j'ai refusé de rejoindre le Conseil des Étudiants en premier lieu."


label fr_S23a:


"Il m'a fallu un effort monumental pour juste me présenter le premier jour. J'aurais pu coopérer avec n'importe qui et pour n'importe quelle cause. C'est peut-être juste par chance que le Conseil des Étudiants m'a recruté en premier."



label fr_S23x:


"Il est possible que c'est à force d'essayer d'éviter leur harcèlement que j'ai été capable de récupérer mon énergie. C'est mignon en y pensant."


"Je me demande pourquoi je suis encore là. Discuter avec Jigoro ne sert à rien, mais bizarrement j'en avais presque envie. Et il a raison, je ne peux pas le comprendre. Même si j'y arrivais, il s'en moquerait. Je suis complètement insignifiant pour lui."


"Il a une confiance que je n'ai pas. Shizune l'a, et c'est peut-être pour ça que je suis là maintenant, à presque crier avec son père, parce que sa confiance m'a influencé. Cependant, je n'ai plus de quoi continuer."


"Je le déteste. Je ne sais pas quoi faire. Il y a quelques mois, je crois que je l'aurais frappé et aurais laissé les conséquences s'appliquer. Mais maintenant, je ne peux pas prendre le risque. S'il me frappait en réponse, il me tuerait sûrement."


"Donc en fin de compte, la seule chose que je peux faire est regarder Jigoro en silence, sachant que je n'ai aucune réponse, et que je le déteste ; j'ai complètement perdu. Étrangement, il prend mon silence pour du mépris."

show jigoro angry
with charachange


hx "Hmph. D'accord alors. Amuse-toi bien."

show jigoro invis at center
with dissolvecharamove


"Ramassant son épée et l'utilisant pour se redresser, il se tourne et marche nonchalamment vers la sortie. J'ai envie de lui jeter mon livre, mais je suis content d’être finalement seul, même si je ne suis plus d'humeur à lire."

scene black
with dissolve

label fr_S24:

scene bg city_station
with locationchange


"Le retour jusqu’à l'école n’arrête pas d’être retardé d'une façon ou d'une autre. Shizune et Misha reviennent si tard que ce n'est même pas la peine d'essayer de partir, et nous restons un jour de plus."


"Le matin suivant nous loupons le train d'une minute et les deux suivants n'arrivent pas. Nous loupons le quatrième parce que je m'étais éloigné pour prendre à boire. Shizune n'était pas très contente."

scene bg school_dormhisao
with shorttimeskip

play music music_dreamy fadein 2.0


"À l'instant où je suis enfin de retour dans ma chambre, je me sens très fatigué même si j'ai passé presque l'intégralité du voyage à dormir. Ce n'est pas la première fois que ça arrive."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

scene black
with shuteye

window show


"Si personne ne m'a devancé, je pourrais faire une thèse dessus, peut-être être publié dans une revue médicale. “Le Syndrome du Retour de Voyage.” Pas très créatif. Je m'endors avant de pouvoir penser à un meilleur titre."

window hide

play sound sfx_doorknock
with Pause(1.0)

scene bg school_dormhisao
with openeye

$ renpy.music.set_volume(1.0, 1.0, channel="music")

window show


"Quelqu'un qui frappe à la porte me réveille quelques heures après ma sieste. Ça m’embête parce que j'étais au milieu d'un rêve que je n'arrive pas à me rappeler. Mais je suis sûr qu'il était bien."


"Je me demande brièvement qui ça peut être, mais ce n'est pas comme si j'avais beaucoup de visiteurs, donc je suis sûr que c'est Kenji. J’espère qu'il veut juste me souhaiter bon retour et ne va pas me demander de l'argent encore."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene black
with shuteye


"Pas suffisamment intéressé pour combattre l'envie de me tourner et de me rendormir cela dit."

stop music fadeout 5.0

window hide

with Pause(4.0)

scene bg school_dormhisao
with openeye

window show


"Quelques heures après ça, je me réveille et remarque immédiatement une enveloppe sur le sol."


"Ça doit être quelque chose qui est arrivé dans le courrier pendant que j'étais absent. Ça dépend du département de Shizune et Misha, donc je me demande si elles sont passées me la donner ou si quelqu'un a fait le travail pendant leur absence..."

show letter_insert:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_rain fadein 4.0


"Quand je la ramasse, tout le restant de fatigue s'évanouit instantanément."


"Même si le nom de l'expéditeur n'était pas dessus, j'aurais reconnu en regardant juste l'enveloppe elle-même, realisant pourquoi elle me semble si familière. En reconnaissant la délicate écriture dessus."



"Elle est d'Iwanako. Au début, je n'y crois pas, mais ça ne serait pas trop dur pour elle de me retrouver si elle le voulait."


"Bien sûr, je n'ai pas pensé qu'elle le voudrait. Elle a peut-être été ma petite copine pendant cinq secondes. Après ça, on s'est à peine parlé."

show letter_insert:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide letter_insert
with None


"Ça serait trop facile de ranger la lettre quelque part et de l'oublier. J'ai quelque peu envie de le faire. Ou de la jeter, sans même la lire. Pourquoi est-ce que j'ai envie de faire ça, je ne le sais pas. Ça serait plus facile à faire. Plus facile que de la lire."

scene ev hisao_letter_open
with locationchange


"Ouvrant l'enveloppe avec le bout d'un crayon, je suis surpris par la longueur de la lettre qui en sort."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide


$ written_note("Cher Hisao,\n\nComment vas-tu ? J’espère que tu vas bien et que tu es content dans ta nouvelle école. Tu manques à tout le monde ici. Presque toute la classe de seconde année s'est retrouvée en classe 3-1 pour la dernière année, donc nous sommes plutôt confiants pour le début de l'année. Je suis sûre que tu aurais été assigné à cette classe aussi.")


$ written_note("Pas mal de monde est anxieux parmi les étudiants de troisième année pour les examens finaux, même s'ils ont lieu beaucoup plus tard. Les professeurs nous harcèlent tout le temps avec ça - même M. Tachibana qui est, d'ailleurs, notre professeur principal cette année. Tu y crois à ça ? J'étais sûre qu'il prendrait sa retraite après la deuxième année, mais il est là, embêtant tout le monde pour les examens.\n")


$ written_note("Je crois que des choses comme ça sont la raison principale pour laquelle tout le monde est nerveux en troisième année. Je dois admettre que je perds quelque peu confiance aussi, même si j'ai toujours assez bien géré les examens.\n\n\n\n\n")

$ renpy.music.set_volume(1.0, 1.0, channel="music")

window show


"Ça me rend nostalgique de lire ça. C'est presque comme si j'étais retourné à l’hôpital. De temps en temps, Iwanako passait et me racontait ce qui se passait en classe, et même à l'époque, je me doutais que je n'y retournerais pas."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide


$ written_note("Ça fait bizarre de penser qu'on est déjà des seniors, hein ? Le temps passe vraiment vite. Je me demande où il est passé. Les nouveaux semblent si jeunes et, d'une certaine façon, si innocents. Je me demande si j'étais comme eux en première année. J'ai eu ce sentiment nostalgique pendant tout le premier trimestre.\n\n\n")

show ev hisao_letter_open:
    "ev hisao_letter_open_2" with locationchange
with None
$ ksgallery_unlock("ev hisao_letter_open_2")


$ written_note("Il y a d'autres choses dont je veux te parler. Je t'écris parce que j'ai l'impression que j'aurais dû te dire certaines choses après l'incident de l'hiver. Je regrette vraiment de ne pas avoir été capable de le dire en personne, et je n'ai aucune excuse pour ça.\n\n\n\n\n")


$ written_note("La vérité est que les fois où je t’ai rendu visite à l’hôpital, je me suis inquiétée pour toi. Je ne parle pas de ta santé. Tu semblais plus distant et découragé. C'était naturel après ce qui est arrivé, mais j'avais l'impression que tu avais abandonné quelque chose à ce moment-là. Le bonheur, peut-être ?\n")


$ written_note("Je voulais exprimer mes sentiments, mais les mots ne sortaient pas. Je ne pouvais rien dire pour te réconforter. Je suis vraiment désolée de ne pas avoir pu t'aider quand tu en avais le plus besoin, même si je t’appréciais tant. Au moins maintenant, finalement, je peux être honnête.\n\n\n\n")

$ renpy.music.set_volume(1.0, 1.0, channel="music")

window show


"Quel moment pratique pour elle pour retrouver sa sincérité. Même si je pense ça, je sais qu'elle a raison. “Distant et découragé” est une bonne façon de me décrire à l'époque. Et peut-être que j'avais abandonné, aussi."


"Ça me fait mal au cœur quand je repense à quand j'étais allongé à l’hôpital, si amer quand elle a finalement arrêté de venir."


"Je n'étais pas surpris, et je n'avais aucune raison de l’être. Comment est-ce qu'elle aurait pu ne pas arrêter de venir alors que c'était la seule chose que j'attendais d'elle ?"


"Elle est venue seulement les six semaines après l'incident. Si je me suis éloigné d'elle, c'était parce que je pouvais la sentir déjà éloignée de moi quand elle venait."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide


$ written_note("Si je pouvais revenir à ces jours qu'on passait dans le silence, en février et mars, je te dirais de ne pas abandonner. C'est ce que je dirais. Peut-être que tu n'aurais pas dérivé si loin si j'avais dit quelque chose. J’espère que tu as réussi à te remettre sur pied par toi-même..\n\n\n\n")


$ written_note("Maintenant que la distance entre nous est aussi physique, ça me semble définitif. Je me demande si on se reverra. Peut-être que c'est mieux si on ne se revoit pas. Si tu veux correspondre avec moi, écris-moi par tous les moyens possibles. J'aimerais beaucoup entendre parler de ta nouvelle école et de comment tu vas. Je ne te souhaite que le meilleur.\n\nSincèrement, Iwanako")

$ renpy.music.set_volume(1.0, 1.0, channel="music")

window show


"C'est un étrange sentiment. Je sais que je n'aurai plus jamais de nouvelles d'elle."


"Si elle voulait vraiment qu'on reste en contact, elle n'aurait pas choisi un courrier pour le faire. Ça n'aurait pas été beaucoup plus dur d'avoir mon mail ou téléphone. C'est seulement un au revoir."

stop music fadeout 4.0


"Je souffle, me rendant compte seulement maintenant que j'avais lu sans respirer. Maintenant qui est distant, Iwanako ? Mais peut-être que c'est pour le mieux."


"Elle doit se sentir coupable de la façon dont se sont terminées les choses pour avoir pris un stylo et écrit cette lettre. Que la façon dont nos vies se sont séparées lui fasse mal, me fait un peu plaisir."


"J'ai presque envie de la remercier, et je ne le fais pas juste parce qu'elle ne veut pas que je lui réponde."

play sound sfx_doorknock

scene bg school_dormhisao
with locationchange


"Quelqu'un frappe à ma porte, et elle s'ouvre de toute façon une milliseconde après. J'ai oublié de la verrouiller, bêtement."


ke "Quoi de neuf mec ? Pourquoi est-ce que ta porte est ouverte ?"


"Je cours jusqu'à la porte, plus rapidement qu'il ne m'est conseillé de le faire dans mon état, pour empêcher Kenji de voir la montagne de pilules qui sont à cinquante centimètres de lui, et que seule la porte l’empêche de voir pour l'instant."



"Et puis il y a la lettre que je tiens. S'il me pose une question, je ne crois pas que je serais capable de trouver quelque chose de convaincant."


"Alors que je suis presque devant lui, je réalise que sa vision est si mauvaise que ce n'est sûrement pas un risque. Il ne me voit pas jusqu’à ce que je lui rentre presque dedans dans l'encadrement de la porte."

scene bg school_dormhallway
show kenji tsun_close at center
with locationchange

play music music_kenji fadein 0.5


ke "Sérieux, c'est quoi ça mec ?"


hi "De quoi tu parles ? Ta porte a genre un million de verrous et pourtant tu entres directement dans la chambre des autres."


hi "Tu n'as même pas attendu une seconde après avoir frappé à la porte, c'était genre, simultané. Tu étais déjà en train d'ouvrir la porte quand tu as frappé."

show kenji happy_close
with charachange


ke "Tu vois ? C'est exactement pour ça que j'ai tous ces verrous. C'est un monde froid et impitoyable dehors, un monde qui te défonce ta porte. Maintenant, toi aussi tu comprends."

show kenji neutral_close
with charachange


ke "Je viens de te donner une précieuse leçon mec. La connaissance c'est le pouvoir. Pourquoi est-ce que tu me cries dessus ? Je suis un héros."

show kenji tsun_close
with charachange


ke "Regarde-toi... tu n'as même pas verrouillé ta porte. Une femme normale aurait pu te tuer un milliard de fois déjà, puis t'aurait remplacé par un clone femelle indistinguable de l'original. Ça m'est presque arrivé."


"Ignorant sa dernière remarque, c'est drôle qu'il dise ça. Il était incapable de m’empêcher de presque lui rentrer dedans et apparemment une femme aurait pu me tuer un milliard de fois. Si cet homme est un héros, nous sommes tous condamnés."

show kenji happy_close
with charachange


ke "Qu'est-ce que tu as là ?"


"D'une certaine façon, il est capable de voir la lettre dans ma main. Vu comment je me suis agité dans tous les sens, ce n'est pas une surprise. Je la cache un peu rapidement, mais ne la mets pas dans mon dos ou autre. Ça serait trop suspect."


"On dirait que je suis plus stressé que je le croyais à propos de la lettre d'Iwanako."


hi "J'ai reçu une lettre."

show kenji neutral_close
with charachange


ke "Oh, ouais, je l'ai mise sous ta porte. J'étais en train de dormir et je me suis réveillé en entendant des explosions."


ke "J'ai mis mon casque et ai jeté un œil dehors pour voir ce qui se passait, et c'était cette femme du Conseil des Étudiants qui frappait à ta porte. C'était celle sans les cheveux roses."

show kenji tsun_close
with charachange


ke "Elle frappait si fort qu'il était évident qu'elle était remplie de rage meurtrière. Contre toi. Elle a réussi à me détecter sans que je sache comment, j'ai essayé de m'échapper, mais elle m'a attrapé et a commencé à pointer ta porte du doigt."


"J'ouvre la bouche pour lui dire qu'elle est sourde, mais j'abandonne. Pour diverses raisons."


ke "Je n'ai pas vraiment compris, et elle s'est énervée de plus en plus, comme un vieil homme essayant d'utiliser un téléphone tactile."

show kenji happy_close
with charachange


ke "Elle allait me tuer. Me tuer et me remplacer par une version femme de moi. Mais soudain la lumière du soleil s'est reflétée sur mes lunettes et l'a aveuglée, me sauvant la vie."

show kenji neutral_close
with charachange


ke "C'était genre un rayon laser. Je ne comprends pas comment quelqu'un avec des lunettes peut se faire blesser par des lunettes. Elle les utilise aussi, elle devrait être immunisée contre les rayons de la mort... mais peu importe."


ke "Elle m'a donné cette enveloppe avec ton nom et est partie."

show kenji happy_close
with charachange


ke "Clairement, elle était à la recherche de sang, alors j'ai menti et dit que tu n'étais pas là. Tu n'étais pas là, hein ? Ça fait une semaine que je veux te demander de m'aider avec mes devoirs, mais je n'avais pas de réponse. ... Bon retour, mec !"


hi "Merci."

show kenji neutral_close
with charachange


ke "Ouais, donc elle m'a donné cette enveloppe avec ton nom dessus. Je ne voulais pas la garder, parce que genre, et si c'était une bombe ? Donc je l'ai juste mise sous ta porte quand elle est partie."


ke "J'allais te le dire, mais tu es revenu avant que je puisse. Au moins c'était pas une bombe."


hi "Erh, merci. Je ne vais pas t'aider avec tes devoirs de maths cela dit, parce que genre, et si ton manuel de maths était une bombe ?"

show kenji tsun_close
with charachange


"Il semble détruit, et envisage aussi que son manuel puisse être une bombe. J'imagine que c'est possible, vu que personne n'utilise vraiment son livre de maths de toute façon."

scene bg school_dormhisao
with locationchange


"Je jette la lettre sur le meuble derrière moi et me tourne pour partir, poussant la porte derrière moi. Elle se cogne et rebondit sur la chaussure de Kenji qui se met à boiter comme si ça lui avait fait vraiment mal."

show kenji neutral at center
with charaenter


"Avant que je le sache, il est déjà dans ma chambre. Je n'arrive pas à l’arrêter avant qu'il ne regarde la lettre, ignorant étrangement la tour de bouteilles de pilules autour d'elle."


hi "Ne lis pas le courrier des autres."

show kenji happy
with charachange


ke "Allez, c'est quoi ? Une lettre d'amour de ta petite copine ? Elle inclut des photos ? Des photos sexy ?"

play sound sfx_dropstuff
stop music fadeout 4.0


"S'adossant au meuble et ne faisant pas attention aux flacons qu'il envoie par terre en faisant ça, Kenji parcourt la lettre d'Iwanako."


"Il semble prendre une éternité, et vu à quel point il a la lettre proche du visage, on dirait qu'il essaye de la manger."

show kenji tsun
with charachange


ke "Qui est “Iwanako” ?"


hi "Mon ex-petite copine."

play music music_night fadein 4.0

show kenji neutral
with charachange


ke "Ex-petite copine, hein ? C'est une lettre de rupture alors. Je croyais que c'était un mythe."


hi "Non. C'en est une, mais vraiment, c'est mon ex-petite copine depuis un moment. Bref, c'est oublié déjà."


"Kenji m'adresse un pouce levé, rassuré que je réagisse bien, même si j'ai presque envie de lui crier dessus, vu que je lui avais dit de ne pas lire."

show kenji happy
with charachange


ke "Ouais, c'est une bonne attitude. C'est pas grave, j'ai déjà eu une rupture aussi, tu ne peux pas laisser ça te détruire. Je veux dire, regarde-moi juste."

hi "Uhhhh…"


ke "Mais, elle a écrit une lettre. Peut-être qu'elle veut que vous vous remettiez ensemble, hein ? C'est écrit, juste là, réponds-lui. Tu devrais le faire. Elle est mignonne ?"


"Pour un gars qui croit que les féministes vont finir par réduire les hommes en esclavage, il est vraiment intéressé par les filles mignonnes."


hi "J'ai une petite copine. Et puis en plus, regarde le contexte, elle ne veut pas que je lui réponde. Elle l'a dit, mais elle ne le veut pas vraiment."

show kenji neutral
with charachange


ke "Mais c'est ce qu'elle a écrit. Cette fille pierre-poisson-enfant te veut encore. C'est dit juste là."


hi "Je l'ai lu, je sais ce que ça dit. Je t’ai dit, tu dois voir le contexte. Elle a dit que je me suis éloigné d'elle, et tout montre qu'elle l'a accepté."


hi "Je pense que la raison pour laquelle elle a écrit, c'est qu'elle veut, je crois, se séparer amicalement. Mais c'est fini, elle ne veut pas qu'on se remette ensemble ou quoi que ce soit."


"Plus j'y pense, plus j'ai l'impression que j'essaye de me trouver des excuses. C'est pas une bonne chose."


"Je suis sûr qu'elle ne veut pas que je lui réponde. Ça me va. Si je lui répondais et que je recevais une réponse indésirable ou pas de réponse, je serais anéanti."


"Peut-être que c'est par peur de cela que j'essaye de justifier ma décision. C'est peut-être ça, mais je ne veux pas y penser. Cette pensée me révulse."


hi "Et puis pourquoi tu t'en préoccupes autant, de toute façon ?"

show kenji happy
with charachange


ke "Parce que tu devrais lui répondre. Elle le veut. Je veux voir ce que sa réponse donnera."

show kenji neutral
with charachange


ke "Y'a même pas besoin que ce soit une belle lettre. C'est bien aussi, mais tu pourrais écrire une lettre de colère et l'accuser. C'est ma nouvelle stratégie d'attaque, je vais continuer d'insulter les femmes. Tu devrais essayer."


hi "Même si elle m'a écrit une lettre, tu dois comprendre ce qu'elle veut dire. Écrire une lettre à quelqu'un, c'est différent de nos jours. Ce n'est pas quelque chose que tu fais. Pas dans ce genre de situation."


hi "Tu peux prendre ton téléphone et appeler n'importe qui de l'autre côté de la terre en un instant, et lui parler presque comme s'il était avec toi. Ou envoyer un mail. Il le saura instantanément et te répondra, c'est aussi simple que ça."


hi "Une lettre peut être quelque chose de personnel, mais elle voulait me garder à distance. Ce n'est pas comme si je pouvais aller lui rendre visite."


hi "Si j'avais son numéro, je pourrais l’appeler, ou si j'avais son adresse mail, je pourrais lui envoyer un mail. Si elle voulait vraiment que je lui réponde, elle m'aurait mis une de ces informations."


"Je me sens bête de me rassurer continuellement avec l'idée que la lettre d'Iwanako ne m'a pas perturbé, alors qu'il est évident que c'est le cas."

show kenji tsun
with charachange


ke "Ça pourrait se faire petit à petit pour elle. Il se peut qu'elle soit trop timide pour t’appeler. Je me rappelle que ma petite copine m'envoyait toujours des textos parce qu'elle était trop timide. C'était super chiant mec."


ke "Je me foutais complètement des téléphones donc je n'en avais pas, et il s’avère que j'ai dû payer pour chaque appel. Mais je n'aime pas les téléphones, donc je ne pouvais même pas l’appeler et lui dire d’arrêter ça."

show kenji neutral
with charachange


ke "J'ai fini par le faire quand même. Je l'ai appelée. J'ai même utilisé un téléphone. C'était littéralement un appel."


hi "Ouais je vois."


"Même s'il a raison, ça veut dire qu'Iwanako veut quand même garder ses distances avec moi. Elle n'est “pas prête” à me parler avec confiance."


"Pourquoi ? Je suis anormal ? Je ne suis pas rassuré par ses actions dans tous les cas. Peut-être que je réfléchis trop, je ne sais pas."


"Kenji ne trouve rien à dire de plus, et le silence qui s'ensuit est si gênant et lourd que je commence à compter les secondes jusqu’à ce qu'il trouve une excuse pour partir."

show kenji tsun
with charachange


ke "Elle me manque..."


hi "Ton ex ?"


ke "Ouais. Même si elle était folle, c'était bien d’être avec elle."


ke "J'ai mal au dos. Si elle était toujours là, je pourrais lui demander de me faire un massage. Je ne sais pas utiliser un four non plus. Ça me manque de manger quelque chose de cuisiné."


ke "On faisait du bowling dans le couloir, des fois. Ça me manque aussi. J'ai dû faire du bowling tout seul durant le dernier festival."


hi "Tu fais du bowling dans le couloir ? Tu vas blesser quelqu'un."


ke "Elle avait l'habitude de dire ça tout le temps."


"Kenji soupire nostalgiquement, ne comprenant clairement pas à quel point quelqu'un peut se faire mal avec une boule de bowling. Apparemment, sa petite copine non plus, vu qu'elle en faisait avec lui."


"C'est une étrange définition de l'amour, mais au moins c'est quelque chose."


hi "Peut-être que tu devrais lui écrire une lettre. Si elle te répond, vous pourriez vous marier."

stop music fadeout 0.3

show kenji rage
with charachange


ke "Se marier ?! Non. Non non non. Non."


hi "D'accord. Pas grave. Mais pourquoi pas ? Tu l'apprécies clairement, même si tu détestes les femmes."

show kenji tsun
with charachange

play music music_kenji fadein 2.0


ke "Les féministes ! Pas les femmes, les féministes. Il y a une différence. Il y a des femmes non-féministes. Merde, ta discrimination est incroyable. La corrélation n'équivaut pas à la cause."


"Même si elle est folle et que c'est une femme, ça ne veut pas dire qu'elle est une femme folle féministe."

show kenji neutral
with charachange


ke "C'est comme la façon dont l'absence de preuve n'est pas la preuve de l'absence. Si c'est vrai, alors par propriété relative, la présence d'éléments de preuve n'est pas égale à la preuve de la présence."


hi "En fait, je crois que si. Et je ne crois pas que ça s'appelle la propriété relative."

show kenji tsun
with charachange


ke "Non, tais-toi, c'est des mathématiques ! Tu dis que les maths se trompent ?"


"Je crois qu'il se trompe."


"Donc même Kenji a quelqu'un qu'il apprécie. Je suis tenté de demander pourquoi ils ont rompu, ou demander plus d'informations, mais je ne devrais pas. Non seulement ça serait indiscret, mais il risquerait de me retourner la question."

stop music fadeout 8.0


"Cette conversation me fait penser à Shizune, bien que la pensée que j'ai n'est vraiment pas claire. Que des questions."


"Je me demande si j'ai ne serait-ce qu’eu l'occasion d'aimer Iwanako, et cette situation avec elle me gêne toujours, comme un mauvais souvenir."


"J'aime beaucoup plus Shizune. Et pourtant j'ai l'impression de devoir la poursuivre, même maintenant. Ça ne me gêne pas, mais je veux réduire la distance entre nous."


"La lettre d'Iwanako est claire, mais je me sens aussi comme ça depuis un moment. Je me suis rapproché, mais pas suffisamment. Je veux réessayer. Tout de suite."

hide kenji
with charaexit


"Je dis à Kenji de sortir pour que je puisse me changer et je me dirige vers la salle du conseil des étudiants."

scene bg school_courtyard
with locationskip


"Les terrains sont déserts aujourd'hui, ce qui est dommage, il fait vraiment bon dehors."

scene bg school_hallway3
with locationskip

play sound sfx_doorknock2


"Personne ne répond quand je frappe. J’essaye de rentrer quand même, mais c'est verrouillé. Quand je retire ma main de la poignée, elle est couverte de poussière. On dirait que personne n'est venu depuis que nous sommes partis."


"Vu que je suis déjà dehors et habillé, je pourrais tout aussi bien manger quelque chose en ville. Mon portefeuille est dans ma chambre, cela dit."

scene ev misha_sad:
    truecenter
    subpixel True zoom 1.05
    easein 10.0 zoom 1.0
with locationskip


"Sur le chemin du retour, je croise Misha assise derrière le bâtiment principal."


"Elle a les yeux fermés et semble dormir. Elle a l'air vraiment tranquille. C'est difficile de l'imaginer autrement qu'en train de rebondir partout ou d'attendre impatiemment en tapant du bout du pied."


"Mon premier réflexe est de l’appeler et de lui demander si elle a vu Shizune, ou si elle veut aller en ville avec moi, mais maintenant que je l'ai vue, je n'ai pas envie de la déranger. Je la laisse seule."

scene black
with dissolve

$ suppress_window_after_timeskip = True

label fr_S25:

window hide None

scene bg school_council_bw
with locationchange

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_pearly

nvl clear
nvl show dissolve


n "\n\nLes premiers jours après mon retour, j'avais presque oublié que j'étais dans le Conseil des Étudiants. J'ai entendu ça et là que le Conseil des Étudiants est généralement débordé de travail vers la fin des vacances, mais ça ne semble pas être le cas."


n "Les premiers temps où j'ai réussi à trouver Shizune ou Misha, elles étaient trop pressées pour me laisser une chance de demander si elles voulaient de l'aide. Quand ce n'était pas le cas, je réussissais juste à trouver Misha."


n "\nShizune disait qu'il y avait du travail, mais pas suffisamment pour impliquer Misha ou moi, ça nous ennuierait juste."


n "\n\nAprès un moment, l'idée d'avoir du temps libre à nouveau a germé en moi, bien qu'à certains moments j'avais vraiment l'impression d'en avoir trop."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

scene bg school_council
show shizu basic_normal2 at center
with locationchange

window show


"Juste quand j'ai commencé à m'y habituer, les choses ont encore changé. Maintenant je me retrouve dans la salle du conseil des étudiants à nouveau, discutant avec Shizune pour savoir si les boîtes de mouchoirs font des bonnes boîtes de votes."


hi "Je te le dis, elles marchent très bien tant qu'on en prend en forme de cubes, pas les rectangulaires."


hi "Misha, tu peux lui signer ? J'ai les mains pleines. ...En fait, laisse tomber."


"Elle est occupée à découper les bulletins de vote, donc si elle fait un mouvement brusque elle enverra sûrement ses ciseaux dans la tête de quelqu'un."


"Je laisse tomber la boîte de gouaches que je porte sur la petite table, et tousse alors qu'une vague de poussière m'arrive au visage. Ça fait vraiment un moment."

show shizu behind_blank
with charachange


ssh "Est-ce que tu crois qu'on devrait changer la taille des bulletins de vote ?"

show bg school_council at bgright
show shizu behind_blank at tworight
with charamove

show mishashort sign_confused at twoleft
with charaenter


mi "Quoi~ ? Mais Shicchan, j'en ai déjà découpé tellement..."

show shizu basic_normal
with charachange


ssh "On peut les faire plus petits. Ça serait plus pratique. On va réduire la police. Comme ça plus de bulletins tiendront dans une seule boîte. On aura besoin de moins de papier aussi."

show shizu behind_smile
with charachange


ssh "Le format pour voter peut être changé. Ça pourrait être comme une vraie élection, et puis on pourrait économiser sur le nombre de boîtes."

show shizu adjust_happy
with charachange


ssh "Avec l'argent restant, on pourrait prendre une pizza, ou peut-être manger chinois, ou un gâteau, ou trois bols du nouveau ramen que j'ai envie d'essayer."


"Shizune passe son doigt sur le bord de ses lunettes, excitée à l'idée d'économiser ne serait-ce qu'un yen sur notre budget."


"Vu que je crois qu'elle est la seule à savoir quel est notre budget, j'ai peur de demander à quel point il est restreint pour qu'elle ait à faire ça."


hi "Et pour les bulletins que Misha a déjà découpés ?"

show shizu basic_happy
with charachange


ssh "Ne t’inquiète pas, ne t’inquiète pas. Je peux les transformer en fiches-mémoire et les vendre dans le magasin de l'école."

show mishashort perky_confused
with charachange


mi "Shicchan, ils ne sont pas très jolis cela dit~..."

show shizu adjust_frown
with charachange


"Shizune semble ne pas être d'accord. Maintenant elles argumentent, ce qui consiste surtout à signer “Si, elles le sont” et “Non, elles ne le sont pas” chacune son tour jusqu’à ce qu'elles se contentent de pointer du doigt."


"C'est étrange, peut-être aussi parce que c'est un peu ridicule, mais je ne les ai jamais vues en désaccord."


"Elles avaient l'air très stressées ces derniers jours."


"Shizune est de plus en plus absorbée par l'élection du conseil des étudiants, bien que ce soit dans plusieurs mois. J'imagine que c'est comme ça qu'agissent les politiciens quand ils réalisent qu'un changement de régime est imminent."


"J'ai du mal à prendre les élections du conseil au sérieux, même maintenant, alors que je suis en train de faire de la calligraphie sur des affiches, mais je comprends pourquoi Shizune les prend au sérieux."


"Après tout, elle a été présidente du Conseil des Étudiants pendant trois ans. D’après son père, elle voulait l’être depuis encore plus longtemps. J'imagine que trois ans est une carrière trop courte pour elle pour partir satisfaite."


hi "Est-ce que l'ancien Conseil des Étudiants a eu à faire tout ça aussi la dernière fois pour organiser l’élection ?"

show shizu behind_frustrated
with charachange


"Shizune affiche une expression chagrinée qui me dit qu'ils n'étaient pas d'une grande aide."


hi "J'imagine que vous faites tout ça pour montrer l'exemple alors ?"

show shizu basic_frown
with charachange

shi "…"

show mishashort hips_frown
with charachange


mi "C'est seulement utile s'ils apprennent quelque chose avec ça, Hicchan~ ! Si ce n'est pas le cas, je serai super énervée~ ! S'ils s’avèrent être du genre à bâcler le travail, je vais être dure avec eux~."


"Ça ne semble pas très menaçant quand c'est Misha qui le dit."


hi "Donc, tu les as déjà rencontrés ?"

show shizu adjust_smug
with charachange

shi "…"

show mishashort hips_grin
with charachange


mi "Ahaha~. Hicchan, il n'y a pas encore de candidats~ !"


hi "Quoi ? Aucun ?"

show shizu behind_smile
show mishashort hips_smile
with charachange


ssh "Même pas pour le statut de président du Conseil des Étudiants. C'est pour ça que j'essaye d'attiser l’intérêt des gens sur le sujet. Qu'est-ce que tu en penses ?"


"Elle tient fièrement, les bras levés, le poster sur lequel elle a travaillé. Ça fait très, euh, militaire."



hi "Tu prends peut-être ça un peu trop au sérieux alors."

show shizu adjust_frown
with charachange


"Shizune fronce les sourcils et joue avec ses lunettes, offensée."


ssh "C'est bizarre ?"


hi "Oui."

show shizu behind_smile
with charachange


"Elle semble étrangement contente que je sois en désaccord avec elle, et je crois que si elle n'était pas vraiment concentrée sur ce qu'elle fait, elle essayerait de débattre avec moi juste parce que ce serait intéressant pour elle."

show shizu basic_normal
with charachange


ssh "Qu'est-ce qui est bizarre ?"

show shizu adjust_smug
with charachange


"On dirait qu'elle va le faire après tout. Mais soudain, Shizune brasse l'air de sa main, comme si elle essayait d'effacer les mots qu'elle vient de prononcer. Au lieu de ça, elle part directement dans les insultes envers ses futurs successeurs."


hi "Eh bien, une chose qui est bizarre, c'est que dans mon ancienne école les élections étaient tous les six mois, vu que, tu sais, nous passons les examens en mars. C'est assez bizarre d'y penser si tôt."

show shizu behind_blank
with charachange


ssh "C'est un peu différent ici."

show shizu adjust_frown
with charachange

shi "…"

show mishashort sign_smile
with charachange


mi "Hicchan, je serai déprimée si nous n'avons pas de remplaçants quand on partira~ ! a dit Shicchan."

show mishashort hips_grin
with charachange


mi "Mais~ ! Ce n'est pas comme si l'école allait arrêter de tourner sans un Conseil des Étudiants. Il sera plus dur pour eux de gérer les formulaires, cela dit~ !"

show mishashort cross_laugh
with charachange


mi "Hahaha~."

show shizu basic_normal2
show mishashort cross_smile
with charachange


"Shizune ne rit pas, cela dit. La blague de Misha la fait se tendre, comme si elle avait été piquée. Bien que Misha n'avait pas l'intention d’être méchante, sa phrase a été cruelle à la fin."

show shizu adjust_frown
with charachange


ssh "Hmph. J'essaye d’inciter des gens à concourir, mais tout le monde est tellement paresseux. Ils croient qu'ils peuvent se la couler douce parce qu'il n'y a pas de deadlines encore. Fainéants, ne profitant pas de l'avantage de commencer tôt."

show shizu cross_angry
with charachange


ssh "“Encore” six mois ? S'ils ne font rien maintenant, ils ne méritent pas un vote !"

show mishashort sign_smile
with charachange


mi "Est-ce qu'ils croient que c'est un travail si facile qu'ils peuvent tout faire à la dernière minute et avoir la place~ ? Insultant~ ! Vraiment~ vraiment~ !"

show mishashort hips_frown
with charachange


mi "Ils se feront manger tout cru quand ils seront assis à ce petit bureau et verront tout le travail qu'il y a à faire~ !"

show shizu behind_frustrated
with charachange


ssh "Si c'était une vraie élection, ils auraient de gros problèmes. Je lisais les lois sur les campagnes japonaises l'autre jour. Seulement les mauvaises, bizarrement."


hi "Bizarrement."


"Pendant une seconde, Shizune a “parlé” comme son père et la voix sortait de la bouche de Misha. Horrible."


hi "Bon déjà, shogun de l'ombre, tu ne peux pas décider ça. Ils seront élus. Deuxièmement, c'est juste une élection scolaire. C'est pas pour être maire ou le Diet. Je ne crois pas que les lois sur les campagnes japonaises s'appliquent."


"Troisièmement, bien que je ne veuille pas le dire, ça me rend nerveux que Shizune soit aussi enthousiaste pour ça, l’élection et les votes."


"D’après son père, elle n'a même pas été élue. En y pensant, je ne me rappelle pas que Shizune ait déjà dit avoir été élue, non plus."


"Alors, est-ce qu'elle a obtenu sa place en étant recrutée dans le Conseil des Étudiants et qu'elle l'a fait s'effondrer jusqu’à ce qu'elle soit la seule restante ? Étrangement, je n'y avais jamais pensé."


"Je ne sais pas quoi en penser, mais ça ne me surprendrait pas. Nous sommes seulement trois maintenant."


"Si les circonstances derrière son accession au poste de présidente sont aussi tristes, je me demande s'il y aura un vote tout court. L’intérêt pourrait être vraiment faible, ou même inexistant. Et toute cette énergie aurait été dépensée pour rien."


"Je claque un point d'exclamation à la fin de l'affiche sur laquelle je travaille. C'est un peu simple, alors en ajouter un n'est pas grave. En fait, c'est toujours un peu trop fade. Je double la grosseur du point d'exclamation."


hi "Je continue de penser que tu devrais ralentir. Ces trucs ne seront pas utilisables avant plusieurs mois, peut-être que tu travailles un peu trop dur là-dessus. C'est ce que je pense. Tu t’inquiètes trop."


"Je ne sais pas comment signer le mot “utilisable”. J'essaye, et réussis juste à envoyer une grande ligne de peinture sur ma feuille. Je n'arriverai pas à arranger ça."


hi "Misha, tu peux lui demander ?"

show mishashort sign_smile
with charachange

show shizu adjust_happy
with charachange


"Shizune rit silencieusement, serrant les dents pour qu'aucun son ne sorte."

show shizu behind_blank
with charachange


ssh "Parce qu'il y a beaucoup à faire."


hi "Comme quoi ?"

show shizu basic_normal
with charachange


ssh "Comme... généralement les boîtes s’avèrent très jolies, alors les gens les prennent. Il faut prévoir ça."

show mishashort hips_grin
with charachange


mi "Wahaha~ ! On pourrait les rendre bizarres cette fois, comme ça personne ne les prendra ! Qu'est-ce que tu en penses, Shicchan~ ?"


hi "On peut dessiner des têtes bizarres dessus. Ou mettre une petite photo de Shizune dessus disant “Voler c'est mal.”"

show shizu behind_frown
with charachange


ssh "Non. Ce n'est pas drôle ! Ce n'est pas votre problème de toute façon. Il y a le taux de participation, aussi..."

show shizu basic_normal2
with charachange


ssh "...Et le pire des cas serait qu'il n'y ait pas de candidats."


"Bien que ce soit fait pour être dit en rigolant, vu la façon dont elle sourit et le signe, ça ne colle pas très bien."

show mishashort cross_laugh
with charachange


"Même Misha comprend que c'est une possibilité, et même si elle essaye de détendre l’atmosphère en ponctuant la phrase de Shizune avec un rire, ça ne marche pas."

show shizu behind_frustrated
with charachange

shi "…"

show shizu basic_angry
with charachange


ssh "Qu'est-ce qui ne va pas vous deux ?"

show shizu adjust_frown
with charachange


ssh "Je faisais une blague. Il y a vraiment des gens intéressés cette année. Si ce n'était pas le cas, pourquoi est-ce que je m’embêterais à faire tout ça ? Ce serait stupide."

show shizu behind_smile
with charachange


ssh "Quand les élections seront finies, j'inviterai tout le monde à dîner. C'est déjà prévu."


hi "Même le nouveau Conseil des Étudiants ?"

show shizu adjust_smug
with charachange


ssh "Non, ils peuvent payer leur propre dîner célébratoire. Ça sera uniquement pour le Conseil des Étudiants actuel. Je serai contente d’être débarrassée de ce travail qui n'apporte aucune reconnaissance."

show mishashort hips_grin
with charachange


mi "Un dîner juste pour nous~ ? Yay~ ! Ça sera comme une petite fête, Shicchan~ !"

stop music fadeout 3.0


"Bien qu'elle force visiblement sa joie, je ne dis rien. Pendant le reste de l'heure, ce qui heureusement est court, nous travaillons en silence."

scene bg school_hallway3
with shorttimeskip

play music music_daily fadein 0.5


"Après les cours, je trouve la porte du conseil verrouillée. C'est étrange, Shizune était tellement occupée tout à l'heure que j'aurais cru qu'elle continuerait de travailler après les cours. C'est ce qu'elle aurait fait normalement."


"Peut-être qu'elle m'a écouté et qu'elle a pris une pause. J’espère que ce n'est que ça."

scene bg school_courtyard_ss
with locationskip


"Me sentant un peu mal à l'aise, je fais un tour rapide de l'école. Je fais ça sans réfléchir, je n'arrive pas à me rappeler quand j'ai commencé à marcher, mais j'ai déjà parcouru la moitié du campus quand je commence à me sentir fatigué."


"Juste une petite balade sur les terrains de l'école et je suis déjà fatigué. Vraiment pathétique."

scene bg school_hallway3
with locationskip


"Avant que je ne le sache, je suis de retour devant la porte du conseil des étudiants. Il y a quelqu'un cette fois-ci."

show mishashort hips_smile at center
with charaenter


mi "Salut Hicchan~ !"


hi "C'est verouillé."


"Voyant dans ses mains une canette de limonade, je regarde autour de moi par réflexe pour voir s'il y a un distributeur. J'ai vraiment soif."

show mishashort sign_smile
with charachange


mi "Je sais, Hicchan~ ! Shicchan est sûrement quelque part ailleurs."


hi "Bizarre."

show mishashort hips_grin
with charachange


mi "Ahahaha~. On n'est pas collées ensemble, tu sais~."


"Misha prend une grande gorgée de sa limonade, jusqu’à la lever complètement pour la finir. J'ai l'impression qu'elle se moque."

show mishashort perky_smile
with charachange


mi "Tu en veux, Hicchan~ ?"


hi "Non, ça va. Je ne peux pas boire dans la canette de quelqu'un d'autre, c'est impoli. En plus, tu te moques de moi, non ? Je viens de te voir tout boire."

show mishashort sign_smile
with charachange


mi "J'en ai une autre dans mon sac~ ! Je suis préparée, hein~, hein~ ? Je suis comme Shicchan~ !"


hi "Elle est un peu trop préparée même. C'est bien que ça déteigne sur toi cela dit. Après quoi, deux ans ?"

show mishashort cross_laugh
with charachange


mi "Wahaha~ !"


"La façon dont elle me regarde pendant que je bois est un peu déconcertant, mais je suis trop reconnaissant pour m'en soucier."


hi "Shizune et toi m'offrez toujours quelque chose. Ça commence à me gêner."

show mishashort hips_smile
with charachange


mi "Vraiment~, Hicchan ? Ahaha~. Paye-moi à manger quelquefois alors, d'accord~ ? Et là~ ! Nous serons quittes."


hi "Eh bien, c'est drôle que tu dises ça. J'allais te proposer d'aller manger en ville..."

show mishashort hips_grin
with charachange


mi "Ouais~ ouais~ ! J'ai super faim aujourd'hui, Hicchan ! Merci !"

show mishashort invis at tworight
with dissolvecharamove

stop music fadeout 3.0


"...Hier. J'allais dire hier. Misha m'a coupé avant que je puisse finir ma phrase, et je ne peux pas me résoudre à lui dire maintenant qu'elle est si contente, riant, bondissant, remuant les bras dans tous les sens."

scene bg suburb_roadcenter_ss
with locationskip

play music music_dreamy fadein 2.0


"J'ai déjà mon portefeuille avec moi, donc je me dirige vers la ville avec Misha juste derrière moi, jouant avec ses mains et se demandant où on devrait aller manger. Du moins je crois. Elle pourrait me demander."


hi "Tu as un endroit précis où tu voudrais aller ?"

show mishashort hips_smile_ss at center
with charaenter


mi "Mmmm~. Je veux aller au salon de thé, ils ont un très gros parfait là-bas."


hi "Je t'ai vu manger un parfait là-bas la dernière fois, il semblait vraiment gros."

show mishashort hips_grin_ss
with charachange


mi "Non non non~ ! Celui-là est vraiment, vraiment~ gros ! Et aussi vraiment cher~ !"


hi "Vraiment, vraiment~ cher ?"

show mishashort cross_laugh_ss
with charachange


mi "Hahaha~ ! Un petit peu~..."


hi "Erh. Bon, Shizune et toi m'avez payé à manger pas mal de fois, alors ça va."

show mishashort perky_confused_ss
with charachange


mi "Hicchan, je ne crois pas avoir déjà fait ça~. Tu es sûr que ce n'est pas juste Shicchan ?"


hi "Tu es vraiment en train d'argumenter contre un repas gratuit ? Ne t’inquiète pas pour ça."

scene bg suburb_shanghaiint
with locationskip


"Nous allons au Shanghai et sommes accueillis par une serveuse qui, étonnamment, n'est pas Yuuko."


"Misha a vraiment hâte de manger ce parfait, parce qu'elle crie sa commande dès qu'elle passe la porte. Quand il arrive, je peux voir qu'il est vraiment gros et a l'air d’être vraiment cher."

show mishashort perky_confused_close at center
with charaenter


mi "Tu vas commander quelque chose, Hicchan~ ? Si tu as faim, on peut partager."


hi "Nan. Je n'aime pas les parfaits. Je n'aime pas le praliné."


show mishashort sign_smile_close
with charachange


mi "Tu peux le retirer~ !"


hi "Tu ne peux pas retirer le praliné, ne sois pas bête."

show mishashort perky_smile_close
with charachange


"Même si je le pouvais, Misha détruit son parfait au point où ce n'est plus possible. C'est un peu dégoûtant même."


"Je me demande si autant de saveurs mélangées peuvent être bonnes. Elle peut vraiment tout différencier là-dedans ? Elle a l'air de trouver ça délicieux en tout cas."

show mishashort hips_grin_close
with charachange


mi "Mh~. C'est si bon les parfaits~, j'ai les dents sensibles, alors adieu les glaces~. Un gâteau c'est trop mou, et s'il y a trop de glaçage, ça m'ennuie. Les parfaits sont intéressants."

show mishashort perky_smile_close
with charachange


mi "Combien de cafés ont des parfaits ici~ ? Dix je crois ! Je les ai tous essayés, et celui-là est mon préféré. Il a un petit flan dedans~ !"


hi "On dirait que tu es une experte en dessert."

show mishashort hips_smile_close
with charachange


mi "Pas juste les desserts~ ! Je veux manger tout plein de choses délicieuses~."

show mishashort hips_grin_close
with charachange


mi "Un jour, j'aurai suffisamment d'argent pour acheter deux kilos de steak de boeuf Matsusaka~ !"


hi "Ça doit coûter 100.000 yen... J'imagine que c'est ton hobby alors, ce genre de nourriture décadente ?"


"Un hobby n'est pas quelque chose que je devrais apprendre après plusieurs mois passés ensemble. J'ai été très impoli en y repensant. Et aussi, c'est un hobby bien cher."

show mishashort perky_confused_close
with charachange


mi "J'imagine~ ! ...Décadente~ ?"


hi "Ouais."

show mishashort hips_grin_close
with charachange


"Misha rit, portant une main à son visage. De la crème glacée s'est accidentellement retrouvée sur son nez. Elle ne le remarque pas. Je ne peux pas m’empêcher de le remarquer. J'aimerais qu'elle la retire. Je vais pour lui dire, mais elle m'interrompt :"

show mishashort perky_confused_close
with charachange


mi "Je ne sais pas ce que ça veut dire."


hi "Oh. C'est un mauvais mot, de toute façon. Ça implique trop de choses. Épicurienne est mieux. Ça veut dire quelqu'un qui apprécie manger de la bonne nourriture. C'est l'adjectif, cela dit. Donc épicurien est le bon mot."

show mishashort cross_laugh_close
with charachange


mi "Wahaha~ !"

show mishashort cross_grin_close
with charachange


mi "Hicchan, tu utilises des mots trop compliqués."


hi "Désolé."

show mishashort perky_smile_close
with charachange


mi "Hahaha~. Je crois que c'est ce que Shicchan aime chez toi."


hi "Que j'utilise des mots compliqués ? Il faut que j’achète de l'acide acétylsalicylique, alors."

show mishashort hips_grin_close
with charachange


mi "Wahaha~ ! Non, pas comme ça, Hicchan~ !"


"Je décide de commander du café après tout, mais il faut un moment pour que la serveuse s'en rende compte, et je crois que le café prendra tout aussi longtemps."


"Le salon de thé se remplit. Pas étonnant, vu que nous sommes là depuis presque une heure, le temps que Misha finisse son dessert."


"Je commande mon café pour partir, mais Misha en commande un aussi, donc on dirait qu'on va rester là encore un peu plus longtemps."


hi "J'aimerais que ce soit si facile. C'est compliqué de lui parler en ce moment."

show mishashort sign_smile_close
with charachange


mi "Shicchan est occupée à cause des élections~ !"


hi "Je sais qu'on ne peut pas s'amuser tout le temps. C'est juste que je veux lui dire beaucoup de choses. Je foire toujours quand c'est le moment cela dit. Et j'ai même pas le temps maintenant. À cause des élections."


hi "Alors même qu'elles sont dans un moment."

show mishashort hips_frown_close
with charachange


mi "Hicchan, tu crois que Shicchan t'évite ?"


"Misha semble énervée. Il fallait s'y attendre, mais je ne le ressens pas comme ça."


hi "Non."

show mishashort perky_sad_close
with charachange


mi "Ah bon~..."


"La façon dont elle le dit me fait penser qu'elle est déçue de ma réponse. Dans ce cas, c'est peut-être le cas. Je me sens mal à l'aise de poser une telle question, mais je crois que la réponse de Misha sera honnête. Sinon, je n'oserais même pas."


hi "Tu crois ça, toi ?"

show mishashort hips_smile_close
with charachange


mi "Non, bien sûr que non, Hicchan~ ! Mais~ ! ...C'est frustrant, parfois~. Shicchan a tant d'énergie, elle essaye toujours d’entraîner les gens dans ce qui l’intéresse elle~."

show mishashort perky_sad_close
with charachange


mi "Mais c'est comme si Shicchan ne savait pas comment gérer les choses quand tout le monde est excité. Ou~ ! Je crois qu'elle veut s'assurer que tout ira bien. Quand je veux aider, Shicchan me repousse toujours."


mi "C'est frustrant."

show mishashort hips_grin_close
with charachange


mi "Je réfléchis sûrement trop~ ! Hein~ ?"


"Misha prend une grande gorgée de son café puis tire la langue."

show mishashort hips_laugh_close
with charachange


mi "Ow~ ! Chaud~ chaud~ chaud~... je croyais qu'il aurait refroidi depuis le temps~ !"


hi "Ça fait vraiment si longtemps ?"


"Je regarde ma montre. Ça ne fait pas longtemps du tout, mais en regardant dehors, le soleil commence déjà à se coucher."


hi "Pas vraiment. Tiens, il fait noir assez tôt aujourd'hui cela dit, donc je peux comprendre pourquoi tu penses ça."

show mishashort perky_sad_close
with charachange


"Après m'avoir entendu, Misha regarde à l'extérieur et bâille presque instantanément. C'est drôle, parce que..."


hi "Tu as sommeil ? Tu étais pleinement éveillée il y a deux secondes."

show mishashort sign_sad_close
with charachange


mi "Je suis fatiguée quand il fait noir, Hicchan~."


hi "Juste comme ça ? Est-ce que tu es un oiseau ?"

show mishashort perky_smile_close
with charachange


mi "Ahahaha~."


"Je prends mon propre café et en bois un peu. Ce n'est pas très chaud, mais très bon. Je le bois aussi vite que possible, parce que maintenant j'ai envie de rentrer aussi. Misha essaye de m'imiter, mais c'est toujours trop chaud pour elle."


"Pendant que j’attends qu'elle finisse, je commence à me demander ce qu'elle disait à propos de ce que Shizune aime chez moi. Soudainement, je suis très curieux, mais en reparler maintenant serait bizarre."

show mishashort hips_grin_close
play sound sfx_impact
with vpunch


"J'essaye de voir mes options encore une fois, mais suis interrompu par Misha claquant presque sa tasse sur la table."

show mishashort cross_grin_close
with charachange


mi "Fini~ !"


"Elle laisse sortir un petit rire, semblant très contente d’elle-même. Un peu comme une enfant. Je me demande si elle avait sa coiffure avec des anglaises quand elle était petite, aussi. Ou si c'était plus comme elle est actuellement ?"


hi "Je pense qu'on pourrait rentrer maintenant. Je n'arrive pas à voir la serveuse. Essaye de ne pas t'endormir pendant que je paie le sunday, d'accord ?"

show mishashort sign_smile_close
with charachange


mi "Pas un sunday, c'est un parfait, Hicchan."

show mishashort cross_laugh_close
with charachange


mi "Wahaha~."


hi "Tu as de la glace sur le nez."

stop music fadeout 2.0

scene black
with dissolve

label fr_S26:

scene bg school_scienceroom at right
with locationchange

play sound sfx_paper
play music music_normal fadein 3.0


"En classe le lendemain après-midi, je suis dans un problème de mathématiques quand une feuille de papier pliée m'atteint à la tête. Je suis sûr de savoir de qui elle vient mais je tourne rapidement la tête quand même, au cas où."

show shizu invis at left
with None

show bg school_scienceroom at left
show shizu behind_blank at center
with dissolvecharamove


"Personne dans cette classe n'est doué pour agir comme si de rien n'était. Je peux voir que tout le monde sait qui me l'a jeté, et en regardant la coupable, il est évident que c'était Shizune. Elle n'essaye même pas de le cacher."


"C'est vraiment différent ici. Dans mon ancienne école je n'aurais eu aucune idée de qui c'était."


"Ouvrant la feuille, je lis :"

window hide


$ written_note("Misha est absente ! Aide-moi après les cours aujourd'hui !")

window show


hi "Je ne comprends pas l’intérêt de la note, pourquoi tu ne le signes pas ?"


"Une grande partie de mon apprentissage en langue des signes s'est faite en imitant le style de Misha qui signe tout ce qu'elle dit, donc je me retrouve à dire à voix haute ce que je signe à Shizune ; un léger rire parcourt la salle. C'est gênant."


his "J'aiderai si je n'ai pas grand-chose à faire."

show shizu basic_angry
with charachange


ssh "C'est idiot. Il est évident que si Misha n'est pas là, tu dois compenser pour deux personnes."


"Je ne sais pas si ça veut vraiment dire quelque chose. Après tout, Misha se plaignait hier que Shizune ne voulait pas la laisser l'aider. Je ne sais pas à quel point, cela dit."


"Faisant semblant d'y réfléchir un peu, je lui réponds sur la feuille que je suis d'accord. Je suis content qu'elle m'ait demandé, parce que je veux lui parler depuis un moment."


"C'est une bonne opportunité, mais j'ai l'impression que je devrais au moins faire un peu de résistance."

hide shizu
with charaexit


"Je retourne à mon devoir et me retrouve immédiatement coincé au troisième problème. Après avoir essayé de le résoudre, j'envoie discrètement la feuille à Shizune. Ça dit :"

window hide


$ written_note("Pourquoi est-ce que Misha n'est pas là ? Et c'est quoi la réponse à la question 3 ?")

show shizu behind_blank at center
with charaenter

window show


ssh "Elle m'a dit qu'elle était malade et qu'elle avait mal au ventre. Misha a souvent mal au ventre, mais j'aurais voulu qu'elle choisisse un meilleur moment pour ça."

show shizu basic_normal2
with charachange


ssh "Utilise les signes."


"Je soupçonne qu'elle a mal au ventre à cause du parfait plus gros que sa tête qu'elle a englouti hier."


"Si ça lui arrive souvent, alors soit c'est une coïncidence, soit elle a l'habitude de manger des choses qui lui infligent ça."


"Je remarque que le professeur nous regarde avec un air désapprobateur. Je ne peux pas lui en vouloir. On “parle” en classe, et avec la langue des signes, d'une façon bien visible et distrayante."


"Je m’éclaircis la gorge pour faire à comprendre à Shizune qu'il faut arrêter, mais elle ne comprend pas."


"Bon, évidemment. Avant que je lui fasse passer le message avec un signe, je peux voir que Shizune a remarqué ce qui se passait, et qu'elle s'en moque juste."

show shizu adjust_smug
with charachange


ssh "Tu veux toujours savoir la réponse à la question 3 ? Je vais te la dire, seulement si tu me donnes la réponse pour la question 25."


his "Hé, je me disais justement qu'un professeur pourrait croire qu'on utilise la langue des signes pour tricher, je n'arrive pas à croire que tu le fasses vraiment ! Et je ne suis pas arrivé à la 25 encore."

show shizu behind_frown
with charachange


ssh "C'est toi le premier qui a demandé la réponse à la question 3. Hypocrite."


his "Tu es la présidente du Conseil des Étudiants, tu ne peux pas tricher."


"Je n'ai pas le temps pour ça, et je pense que j'arrive à la limite de la patience du professeur. J'aimerais continuer à discuter avec elle tout en faisant mes problèmes de maths, mais il me faudrait au moins deux autres mains."

show shizu basic_normal
with charachange


"Shizune est un peu plus créative et s'en sort en utilisant des abréviations de mots. Je prends quelques notes mentales de ses signes tout en étant étourdi par deux équations particulièrement longues."

show shizu adjust_smug
with charachange

play sound sfx_impact2
with vpunch


"Juste avant que la cloche sonne, elle remet le capuchon de son stylo et le claque sur son bureau triomphalement en faisant un bruit qui fait sursauter tout le monde, rapidement oublié par la classe qui va déjeuner."

stop music fadeout 6.0

show shizu basic_normal_close at twoleft
with characlose


"Après quelques rapides étirements, elle se lève et me fait des signes."

show shizu behind_frown_close
with charachange


ssh "Tu n'as toujours pas fini ? J'allais te proposer de rendre la tienne pendant que j'étais levée."


his "Quelqu'un m'a distrait. J'ai dû demander au professeur de m'accorder neuf minutes en plus pour le finir. Ce n'est pas facile de résoudre un problème tout en conversant avec l'autre main, d'ailleurs."


"Il n'était pas content de ma demande, ayant tout autant que moi envie de sortir."


"Vu qu'il ne me reste qu'un problème à finir, on dirait que Shizune ne me croit pas vraiment. À la seconde où je rends ma copie, elle me traîne jusque dans la salle du conseil des étudiants."

scene bg school_council
with locationskip

play music music_happiness fadein 2.0


"C'est étrangement propre. Ce qui ne m'arrange pas. Je n'arrive pas à retrouver ce sur quoi je travaillais hier."


his "Où sont tous les trucs ?"

show shizu behind_blank at center
with charaenter


ssh "J'ai fait du nettoyage."


his "Ça ne me dit pas tout. C'est comme si tu avais oublié où tu avais tout rangé. Bah pas grave, si je ne peux pas trouver les affaires, je vais rentrer."

show shizu basic_normal2
with charachange


ssh "C'est dans le tiroir juste là."


"Shizune boude tandis que je sors les affiches sur lesquelles je travaillais et que je les éparpille un peu, vu qu'elle les avait rangées par couleur. C'est juste que j'ai mon propre système, mais je ne suis pas sûr qu'elle me croirait si je lui disais."


his "J'aime bien quand c'est un peu le bazar. C'est plus naturel. Et ça fait gagner du temps. C'était bien, là où je l'ai laissé, comme ça je n'ai pas besoin d'aller voir dans un placard juste pour trouver ce sur quoi je travaillais la veille."

show shizu adjust_frown
with charachange


ssh "Paresseux."


his "C'est pas vrai, je ne suis pas paresseux, tu en fais juste toujours trop."


"Je jette un coup d’œil à son bureau. Un bloc-notes est dans le coin, à côté se trouve un petit calendrier de bureau avec chaque case remplie par une écriture parfaite. À droite, trois boîtes de stylos, une bleue, une noire, et une rouge."


his "Regarde, tu mets même les stylos dans leurs boîtes d'origine à la fin de la journée, classés par couleur et tout. C'est vraiment un truc de maniaque du rangement."

show shizu behind_frown
with charachange


ssh "Tu en fais quoi toi ? Tu les jettes dans un pot sur ton bureau ?"


his "J'estime que c'est être suffisamment organisé."

show shizu basic_frown
with charachange


ssh "Tu es tellement désorganisé que tu ne te coiffes même pas bien les cheveux."


his "Touché..."


"Ce n'est pas comme si je n'essayais pas, ils refusent juste de rester plats. Je prends une boîte de stylos et l'ouvre pour voir si elle aussi fait en sortee qu'ils soient tous dans le même sens. Elle comprend là où je veux en venir et ne semble pas amusée."

play sound sfx_dropstuff


"Il s'avère que la boîte n'était pas bien fermée de l'autre côté, et aussitôt que je la prends, ils tombent tous en cascade."


his "C'est ma faute, je vais les ramasser, ne t’inquiète pas."

stop music fadeout 4.0
play sound sfx_impact

show shizu adjust_blush_close
with vpunch


"Je me penche pour ramasser les stylos, oubliant que son attention étant dirigée vers eux, elle n'a pas pu me voir. La tête de Shizune se heurte contre ma poitrine. Pas très fort, mais ça me fait perdre l'équilibre et je tombe en arrière."

show shizu adjust_blush
with charadistant


"J'en ris, espérant qu'elle fasse de même. Mais quand elle se raidit et recule, un sentiment de crainte s'empare de moi."


"C'est une étrange réaction. Je commence à me demander pourquoi elle aurait une réaction aussi étrange. C'est assez évident, elle vient se cogner contre quelqu'un qui a un problème au cœur."


label fr_S26a:


"Shizune sait que j'en ai un, ayant vu les rangées de pilules alignées sur mon étagère. Ou du moins, elle sait que j'ai quelque chose d'assez grave pour avoir besoin d'autant de médicaments, tout en n'ayant rien de visible physiquement."


label fr_S26b:


"Shizune sait que j'en ai un, sûrement à cause des fichiers auxquels elle a accès grâce au conseil des étudiants. Ou du moins, elle sait que j'ai quelque chose de suffisamment sévère pour avoir besoin d’être surveillé."


label fr_S26c:


"Donc elle me traite comme si j'étais fait de verre. Pour elle, c'est naturel. Je n'ai pas oublié comment elle a paniqué quand Emi m'est rentrée dedans le premier jour où je suis arrivé. Pourquoi est-ce que ce serait différent pour elle ?"

show shizu basic_normal
with charachange


"Je suis sûr qu'elle s'en rappelle, à cet instant. Je peux le voir sur son visage. Elle semble en colère contre elle-même."


"Ça serait une bonne opportunité pour parler de la fois où elle a vu mes pilules. Même si je n'ai pas spécialement envie d'aborder le sujet, ça serait une bonne chose à faire. Ça mettrait un peu d'ordre."


"Cependant, je suis effrayé, et finis par ne rien dire. En partie parce que je m'imagine devoir attirer son attention et avoir à lui signer quel genre d'éclopé je suis, un geste à la fois ; l'idée me semble de plus en plus déprimante."

hide shizu
with charaexit


"Prenant un siège, je décide de juste finir ces affiches pour penser à autre chose. Il y en a certaines que je ne me rappelle pas avoir faites. D’après le texte aligné et l'écriture très propre, je peux deviner que c'est Shizune qui a fait celles-là."


"Ça veut dire que ce qui reste doit avoir été fait par Misha. Elles sont beaucoup plus visuelles, avec des petites images drôles de nous dessus. Je ne suis pas vraiment très enthousiaste à l'idée d'être une mascotte."

scene bg school_council_ss
with shorttimeskip

play music music_tranquil fadein 3.0


"Le temps passe. Suffisamment pour que le soleil commence à se coucher. J’entends Shizune poser son stylo et se craquer les phalanges, une à la fois. C'est si bruyant que je relève la tête, me demandant si elle essaye d'attirer mon attention."

show shizu behind_blank_ss
with charaenter


"Bien que ce n'était pas le but, quand elle remarque que je la regarde, elle commence à signer l'instant d’après."

show shizu basic_normal_ss
with charachange


ssh "Faisons une pause."


his "Je suis surpris que tu dises ça."

show shizu adjust_happy_ss
with charachange


ssh "J'ai presque fini de toute façon, et j'ai faim. Pas toi ?"


his "Un peu."

show shizu basic_normal2_ss
with charachange


ssh "J'ai vraiment faim."


his "On pourrait commander quelque chose."

show shizu behind_smile_ss
with charachange


ssh "Je pensais à toi. J'ai déjà quelque chose à manger."


his "Où ça ?"

show shizu adjust_smug_ss
with charachange


"Elle sort une brioche à la canelle de sous son bureau, la levant doucement jusqu'au niveau du visage, comme un magicien ferait léviter une pierre."

show shizu behind_smile_ss
with charachange


ssh "Mais !"

show shizu basic_sparkle_ss
with charachange


ssh "Je n'en ai qu'une. Pas suffisant pour nous deux."


"Ah, vraiment dramatique. Je peux voir où elle veut en venir. J'ai un léger sentiment de déjà vu."


his "On pourrait juste la diviser en deux."

show shizu adjust_frown_ss
with charachange


ssh "C'est. Pas. Drôle. Trop ennuyeux. Parions-la au shogi."


"Elle a déjà sorti le plateau. Il y a vraiment de tout dans ce bureau."


his "Pas les échecs ?"

show shizu behind_smile_ss
with charachange


ssh "Les échecs ont des promotions inintéressantes, c'est mieux ça."


his "Je sais pas trop. Bon en fait, je me défends pas trop mal au shogi, alors ça m'ira."

show shizu basic_happy_ss
with charachange


ssh "Ah oui ? D'accord, on peut rendre les choses un peu plus intéressantes alors. Chaque mouvement doit être fait en moins de trente secondes. Tu peux ajouter une règle aussi."


his "Non merci. Tout ce que j'ajouterais ne ferait qu'empirer les choses. Une limite de trente secondes est déjà trop difficile pour moi."


his "Maintenant je regrette de m’être vanté."

scene bg school_council_ss
show shizu basic_normal_close_ss at center
with shorttimeskip


"Dès que que Shizune a gagné le droit de jouer la première après avoir lancé une pièce, elle commence à jouer de façon à faire évoluer ses pièces aussi vite que possible. C'est un style de jeu assez classique mais potentiellement un piège."


"Ce n'en est pas un, pourtant. Le but de Shizune est clairement d'améliorer la position de ses pièces et de voler les miennes. Elle est très douée, mais sa stratégie la rend prévisible. Je m'en sors un peu mieux que je ne l'aurais cru."


"La règle de limite du temps à 30 secondes par coup est difficile, cela dit. La partie se termine sur une égalité. À ce point, je crois qu'on est censés faire une autre partie, ou compter les pièces pour comparer les points."


"Shizune ne veut pas en refaire une parce qu'il se fait tard, mais juste compter les points ne la satisfait clairement pas."

show shizu adjust_frown_close_ss
with charachange

stop music fadeout 4.0


"Elle s'assoit là, faisant passer un général d'argent entre ses doigts en contemplant ses deux options. Ça prend si longtemps que je crois qu'elle a oublié l'enjeu."


"Finalement, elle arrête de jouer avec la pièce de shogi et la pose."

show shizu behind_blank_close_ss
with charachange


ssh "Est-ce que Misha est en colère contre moi ?"


"Ça sort vraiment de nulle part."

play music music_pearly fadein 5.0


"La franchise de Shizune est déconcertante, parce qu'avec elle, un signe de candeur est un signe de manque de sérieux. Il n'y a pas de sourire joueur sur son visage, il y a son masque stoïque de concentration, se demandant si je vais lui dire la vérité."


"Je n'aime pas qu'elle puisse penser que je peux lui dire quoi que ce soit d'autre que la vérité, mais je sais aussi qu'elles se sont probablement disputées récemment, et ça me réchauffe le cœur de savoir qu'elles tiennent autant l'une à l'autre."


his "Non. J'en doute fortement."


his "Tu savais qu'elle croyait que tu étais en colère contre elle ?"

show shizu behind_sad_close_ss
with charachange


"Shizune hoche lentement la tête, mal à l'aise."

show shizu basic_normal2_close_ss
with charachange


ssh "Oui."


his "Elle était moins directe que toi pour poser la question. C'est surprenant, tu es celle qui aime jouer d'habitude."

show shizu behind_blank_close_ss
with charachange


ssh "Pas tout le temps."

"…"


his "Vous vous êtes disputées ou quelque chose ?"

show shizu adjust_frown_close_ss
with charachange


ssh "Non."


"Elle me répond très rapidement, pas très contente de cette remarque. J'ai l'impression d'avoir marché sur un champ de mines."

show shizu behind_sad_close_ss
with charachange


ssh "Désolée. En fait, oui. Juste un peu."

show shizu behind_blank_close_ss
with charachange


ssh "Je sais qu'elle ne s’intéresse pas au Conseil des Étudiants. Elle l'a juste rejoint à cause de moi. Je lui en suis encore reconnaissante. Et je suis vraiment heureuse qu'elle soit mon amie. Mais je ne comprends pas pourquoi elle est contrariée."


his "Pourquoi tu ne lui demandes pas juste ?"

show shizu basic_normal2_close_ss
with charachange


ssh "Elle ne me le dira pas. Je vais le découvrir par moi-même à la place. J'étais sûre que j'étais très perspicace, même si je ne pouvais pas entendre. C'était idiot. Je le sais maintenant."

show shizu behind_sad_close_ss
with charachange


ssh "C'est sûrement de ma faute."

stop music fadeout 8.0


"Shizune n'en dit pas plus. Je suis sûr qu'elle ne comprend pas totalement la situation elle-même."


"C'est étrange de penser que Shizune, qui est habituellement si sûre de tout, puisse être effrayée par une petite dispute avec une amie. Mais plus j'y pense, plus c'est logique."


"Elles sont beaucoup plus proches que des amies normales le seraient, et Shizune est très isolée par rapport aux autres personnes. Le fait qu'elle soit sourde n'y est pas pour rien."


"Mais j'ai le sentiment qu'elle utilise Misha comme une voix entre elle et les autres gens parce qu'elle le veut, pas juste parce qu'elle n'a pas le choix. Elle pourrait très bien communiquer avec son petit bloc-notes. Elle déteste juste ça."


"Après un si long moment à avoir parlé à travers une autre personne, j'imagine qu'on commence à perdre le contact. Ça semble inévitable. Ça ne me semble pas anormal de penser qu'elle n'est pas très douée avec les gens."

hide shizu
with charaexit


"Je retourne au travail, ayant encore plus envie de manger cette brioche à la canelle maintenant que le temps est passé, mais quand je compte les pièces de shogi sur la table de Shizune, je peux voir en un regard qu'elle aurait gagné."


"J'ai aussi trop faim pour me concentrer si jamais il devait y avoir une revanche. Motivé par mon désir de remballer et de manger quelque chose, j'apporte la touche finale à la dernière des affiches."


his "Fini. Je crois que ça suffira. En avoir trop serait mauvais."

play music music_shizune fadein 3.0

show shizu behind_blank_ss at center
with charaenter


ssh "D'accord."


his "C'est tout ? Juste “d'accord” ?"

show shizu adjust_frown_ss
with charachange


shi "... ?"

show shizu behind_blank_ss
with charachange


ssh "...J'en ferai probablement un peu moi-même, après avoir choisi le format de bulletin de vote."


his "Arrggh. Trop d'affiches c'est mauvais, aussi. Tu n'as jamais entendu parler de la saturation ?"


his "Je pense vraiment que tu en fais trop."

show shizu basic_normal_ss
with charachange


"Les doigts en l'air, Shizune semble presque sur le point de l'admettre."

show shizu behind_blank_ss
with charachange


ssh "Peut-être."


his "C'est ce que pense Misha aussi."

show shizu basic_normal2_ss
with charachange


"Je regarde ses doigts continuer de tournoyer entre eux et tirer l'un sur l'autre comme à une épreuve de tir à la corde."


his "Ça ne me gêne pas, mais j'ai demandé dans quelques classes aujourd'hui et l’intérêt est plutôt faible. Comme tu l'avais dit. Donc..."

show shizu adjust_frown_ss
with charachange


ssh "Alors c'est mal ?"


his "Non. Mais... c'est quelque peu inutile."

show shizu basic_angry_ss
with charachange


ssh "Ça ne l'est pas."


"Ouais, mais pour qui ? Je doute que même Shizune le croie vraiment."

show shizu behind_frustrated_ss
with charachange


ssh "Je ne fais pas tout ce travail juste pour mon ego."


his "Ce n'est pas ce que je veux dire."


"La première chance que j'ai d’être seul avec elle depuis plusieurs jours, et je l'ai déjà complètement foirée. Pourtant, elle ne semble pas énervée."


"C'est plus qu'elle est frustrée de ne pas pouvoir s'exprimer suffisamment clairement. Vu qu'elle est une experte en langue des signes, je ne pense pas que ce soit ça."


"Je me demande quel avantage lui conférerait le fait de pouvoir parler, et si elle y a déjà pensé."

show shizu basic_frown_ss
with charachange


ssh "C'est un autre projet à moi. Tout comme les festivals. Je vais le faire, parce que c'est mon travail. C'est juste que l’élection d'un conseil des étudiants n'est pas aussi intéressant qu'un festival, donc tout le monde s'en moque."


"Elle touche brièvement le bout de ses doigts entre eux, comme pour dire “mais, peut-être...” Il y a de la vérité dans ces paroles, mais Shizune ne veut rien dire qui réduirait les élections à quelque chose d'aussi simple."

show shizu behind_frown_ss
with charachange


ssh "Mais je m'en moque. Je veux que les gens s'y intéressent, mais ce n'est pas à propos de moi, je ne veux pas du tout être impliquée."


his "Comment ça ? Tu vas à tous les festivals."

show shizu adjust_frown_ss
with charachange


"Shizune secoue la main comme pour nier."

show shizu behind_blank_ss
with charachange


ssh "Eh bien... Je dois m'amuser aussi. Mais bon, c'est pas la même chose."


"Son humeur semble s’être améliorée, si elle arrive à sortir une blague comme ça."

show shizu basic_normal2_ss
with charachange


ssh "Je ne veux pas que qui que ce soit puisse se servir du fait que je suis impliquée. C'est trop embêtant. Je ne veux pas cette responsabilité."

show shizu adjust_frown_ss
with charachange


ssh "Les choses sont trop compliquées de nos jours. Plus j'essaye d'attirer l’intérêt sur les élections, plus je dois être impliquée. Personne ne veut se lancer pour l'instant, et on ne dirait pas que mon temps est fini, même si c'est le cas."

show shizu behind_frustrated_ss
with charachange


"Croisant les bras et s'adossant, elle grince des dents de frustration."

show shizu cross_angry_ss
with charachange


ssh "Ils sont tous si paresseux. Il est impossible de leur faire faire quoi que ce soit. Ailleurs, les élections seraient un événement excitant. Si seulement il y avait une façon de les punir..."

show shizu adjust_angry_ss
with charachange


ssh "...Comme enchaîner les gens à leurs bureaux. Voter est obligatoire. Si tu ne votes pas, tu te fais fouetter."


"Terrifiant. Je me demande à quel point ça serait hypocrite si j'en venais à rester au lit durant le jour de l’élection. Avec la grippe. Et un rhume. Et une angine. Et avec une entorse à la cheville."


his "Tu devrais te mettre là-dessus aussi."


his "Pas en tant que punition, je parlais de ça."


"Je prends l'une des affiches de Misha."


his "Comme ça. C'est une assez bonne idée. Misha était sur quelque chose d’intéressant. C'est beaucoup plus mignon que du simple texte. Je crois que tu aimerais ça. Avoir des mascottes mignonnes aiderait à la popularité."

show shizu basic_normal_ss
with charachange


ssh "Peut-être, si c'est juste Misha."


his "Pourquoi pas moi aussi ? Quelqu'un m'a dit que l'école avait légèrement plus de filles que de garçons... Tu dois prendre en compte la démographie, aussi."

show shizu adjust_blush_ss
with charachange


"Shizune rit, audiblement cette fois. Je suis surpris, et quand elle voit mon visage, elle aussi. Elle rougit immédiatement, embarrassée d'avoir laissé sortir un son. Ce qui est vraiment troublant."



his "Pourquoi tu ne te dessinerais pas dessus ?"


"Elle écarte ma question."

show shizu basic_angry_ss
with charachange


ssh "C'est pénible."


his "Pourquoi pénible ? Tout le monde sait que tu es dans le Conseil des Étudiants."


"Mon estomac gargouille, me faisant réaliser que je suis plus affamé que je l'aurais cru. Shizune profite de l'occasion pour éviter ma question en changeant de sujet."

show shizu behind_blank_ss
with charachange


ssh "Quelque chose ne va pas ?"


his "Non. Mon estomac a grogné."

show shizu basic_normal_ss
with charachange


ssh "Je vois."


"Elle regarde la pâtisserie oubliée sur le bureau et fronce les sourcils, la trouvant inadéquate pour deux personnes."

show shizu adjust_happy_ss
with charachange


ssh "Allons au Shanghai, si tu as si faim. Il y aura peut-être un peu de monde à cette heure-ci, mais Yuuko travaille aujourd'hui. On aura forcément une table."


"Il y a quelque chose d'inquiétant dans son sourire."


his "Non merci. J'y suis déjà allé deux fois cette semaine, l'une juste après l'autre."


show shizu basic_frown_ss
with charachange


"Shizune fait la moue, s'adosse contre son bureau et reste comme ça en signe de protestation."


his "Quoi ?"

show shizu adjust_frown_ss
with charachange


ssh "Je suis déçue que tu aies refusé."


his "Bah, je ne peux pas être d'accord avec toi sur tout."

show shizu behind_frown_ss
with charachange


ssh "Tu ne donnes pas suffisamment ton opinion. Ça serait plus facile pour moi si c'était toujours comme ça, mais pas très intéressant, tu vois ? Il y a certaines décisions sur lesquelles tu devrais être en désaccord avec moi. Tu en as le devoir."


his "Comment je suis censé savoir quand il faut que je sois en désaccord ?"

show shizu basic_normal_ss
with charachange


ssh "C'est facile."


his "Non ça ne l'est pas. Parfois j'ai du mal à savoir si tu es sérieuse ou si tu plaisantes."

stop music fadeout 9.0


"Vu qu'elle communique entièrement en langue des signes, ça devrait être plutôt évident. Je ne dirais pas que c'est seulement à cause de ça, cela dit."


"Je me rappelle quand j'ai eu ma crise cardiaque, Iwanako n’arrêtait pas de parler au début. J'ai fini par souhaiter qu'elle se taise. Ou je l'aurais voulu, si je n'avais pas été content d'avoir de la compagnie. Finalement, j'ai arrêté d’être reconnaissant."


"Quand on parlait, j'avais l'impression qu'il n'y avait rien de plus que des échanges ritualisés et de la politesse. Iwanako a vraiment essayé de masquer ce qu'elle ressentait, ce qui était vain."


"En fin de compte, son comportement extérieur s'est aligné sur ses sentiments."


"Pour cette raison, j'ai été capable d'accepter le jour où elle a arrêté de venir. Ça n'a pas été une surprise quand c'est arrivé. Même si elle se croyait très forte pour cacher ses sentiments, je n'ai pas été surpris."


"J'ai entendu dire que des jeux comme le shogi ou les échecs peuvent en dire long sur quelqu'un. J'aimerais savoir ce que Shizune a cru en déduire de moi."


"Je suis peut-être plus comme Iwanako que j'aime le croire, si je peux seulement m'attacher à Shizune en reculant. Je suggère qu'on commande à emporter."

scene black
with dissolve



label fr_S27:

scene bg school_hallway2
with locationchange


"Le jour suivant, je vais jusqu’à mon distributeur habituel durant la pause déjeuner, et il est à court de ma boisson favorite. Je l'avais gardée secrète des autres pendant longtemps ; cachée entre un local de stockage et la bibliothèque."


"Je m'attendais à ce qu'une machine aussi proche de la bibliothèque soit toujours très utilisée, mais pourtant, la bibliothèque est vide la plupart du temps, et ceux qui y vont le font seulement pour trouver un document."


"Personne ne reste plus longtemps qu'il n'en a besoin. Durant le dernier mois, cela m'a été favorable, mais le problème avec une machine que personne ne connaît est qu'elle n'est jamais réapprovisionnée."

play sound sfx_can


"Choisissant un soda à l'orange, je décide de le boire ici plutôt que d'attendre d'arriver à la cafétéria, et c'est à ce moment que la porte de la bibliothèque s'ouvre à côté de moi."

show yuuko worried_down at center
with charaenter


yu "Ah..."

show yuuko worried_up
with charachange


yu "Je te cherchais !"

play music music_happiness fadein 2.0


"Yuuko semble être beaucoup plus sûre d'elle que d'habitude aujourd'hui, bien qu'elle retourne à son marmonnement juste après."

show yuuko worried_down
with charachange


yu "R-ramène tes livres, s'il te plaît. Je veux dire... les livres de la bibliothèque. Tu es vraiment en retard pour les rendre. Et certains ont été réclamés..."


hi "Oups. J'ai oublié. Je n’arrête pas d'en prendre des nouveaux et oublie de rendre les anciens."

show yuuko neurotic_up
with charachange


yu "Ça m'arrive tout le temps à la bibliothèque de l'université, c'est vraiment embarrassant."


hi "Ils envoient quelqu'un pour que tu les rendes ?"

show yuuko worried_up
with charachange


yu "Non... La bibliothèque de l'université est plus grande, ils ne se rendent pas compte si quelqu'un emprunte un livre trop longtemps. C'est pratique, leur politique sur les livres en retard est... vraiment stricte, bien plus qu'ici..."


"J'aime bien que, malgré ce qu'elle dit, Yuuko n'ait pas de problème avec le fait d'emprunter les livres plus longtemps qu'elle est supposée le faire. Ça la rend un peu hypocrite sur son retard. Il faut un voleur pour attraper un voleur, j'imagine."


"Comprenant le sens de ses mots au même moment que moi, Yuuko essaye de se rattraper comme elle peut."

show yuuko panic_up
with charachange


yu "...Hum... ah... C'est différent... de cette situation ! C'est totalement différent..."


"Yuuko regarde ses ongles une seconde comme si elle avait vraiment envie de se les ronger, mais en est trop consciente pour le faire."

show yuuko worried_down
with charachange


yu "D'ailleurs, ça fait combien de temps... Tu as emprunté certains des livres il y a des mois, Hisao. Désolée... C'est juste que, d'autres personnes veulent les lire aussi. Si tu es lent à lire, c'est pas grave, cela dit..."


hi "Non, c'est totalement de ma faute. Pour être honnête, il y en a que je n'ai même pas lus. Je ne devrais pas continuer d'emprunter des livres quand je n'en ai pas lu certains."


yu "C'est pas bien..."


hi "Ouais, vraiment pas..."


"Maintenant, je commence à imiter son habitude de devenir silencieuse en fin de phrase. Sa gêne est vraiment contagieuse."


"Cela dit, je suis surpris. Yuuko semble presque normale aujourd'hui, bien que de temps en temps, ses tics nerveux de serveuse reviennent."


"En y pensant, elle n'agissait pas comme ça quand je l'ai rencontrée la première fois. Elle était un peu étourdie et nerveuse, mais ce n'était pas aussi sévère que quand Shizune, Misha et moi l'avons vue au Shanghai."


"Peut-être que Yuuko a un complexe avec le fait que les enfants de l'école la voient en serveuse."


"C'est un peu bizarre aussi de choisir le café le plus proche de l'école comme lieu de travail. Dans ce cas, peut-être que le fait qu'il y ait si peu de clients est considéré comme une pause pour elle."


hi "Bon, j'ai compris. Je les rendrai après les cours."

show yuuko smile_up
with charachange


yu "Aussi vite que possible, s'il te plaît."

show yuuko worried_up
with charachange


yu "Hum... attends, je peux te demander une dernière chose ?"


hi "Bien sûr, quoi donc ?"

show yuuko worried_down
with charachange


yu "Je... Je dois partir pour un petit moment, mais je ne peux pas laisser la bibliothèque sans surveillance... Désolée, ça te gênerait de la surveiller ? Juste pour un petit moment ! Tu es dans le Conseil des Étudiants, je suis sûr que ça ira."


hi "D'accord, je vais le faire, ne t'inqui—"

show yuuko closedhappy_up
with charachange


yu "Merci !"

show yuuko neurotic_up
with vpunch


"Yuuko s'avance rapidement comme si elle était si reconnaissance qu'elle était sur le point de me serrer dans ses bras, mais s’arrête deux centimètres avant, ce qui rend le geste extrêmement confus."


"Je suis surpris qu'elle réussisse à se contrôler aussi brusquement, vu qu'elle est quelque peu maladroite."

hide yuuko
with charaexit

stop music fadeout 6.0


"Avant que je puisse dire “De rien”, elle est déjà en train de courir jusqu’à la sortie comme si elle était en retard à un rendez-vous."


"C'est peut-être le cas, mais je n'en suis pas sûr. C'est Yuuko, elle semble être le genre de personne à tout traiter de cette façon."

scene bg school_library
with locationchange


"Maintenant que je suis dans la bibliothèque, je me sens un peu bête. Je ne sais pas vraiment ce que je suis censé faire. Est-ce que je dois m'asseoir et lire normalement comme je le ferais ? Ce n'est pas ce que ferait Yuuko."


"Peut-être que je devrais m'asseoir au bureau de la bibliothécaire, et adresser à tout le monde un regard sévère et analytique. J'utilise celui de Shizune comme référence et m’entraîne sur la surface miroir d'un stylo."


"Je trouve que ça rend plutôt pas mal. Ce qui est frustrant, c'est que personne ne rentre, donc j'abandonne vite l'idée et décide de chercher Hanako à la place."


"C'est désert. Je crois voir quelqu'un, mais à la seconde où je cligne des yeux, ce quelqu'un a disparu. Au moment où j'ouvre un livre qui me semble intéressant, une personne familière apparaît devant le bureau comme un fantôme."

show kenji invis:
    center
    xpos 0.4
with None

show kenji tsun at center
with dissolvecharamove

play music music_kenji fadein 0.5


ke "Yo bibliothécaire, je vous ai cherché pendant genre dix minutes. Quoi ?! C'est toi ? Mec, tu dois vraiment t'ennuyer, ou le Conseil des Étudiants doit te forcer. Ces pétasses ! Comment osent-elles ?"

show kenji rage
with charachange


ke "Esclavagistes !"


"Il doit exagérer, parce que ça m'a pris trente secondes à faire le tour de l'endroit en marchant lentement. Cette pensée est dominée par ma surprise de le voir."


hi "D’où est-ce que tu viens ? Qu'est-ce que tu fais là ?"

show kenji tsun
with charachange


ke "Quoi, un homme ne peut plus aller à la bibliothèque, maintenant ? Je ne peux même pas aller à la bibliothèque sans qu'un mec comme toi me tombe dessus. Je vois une fille venir ici tout le temps, mais personne ne lui demande jamais rien à elle."


ke "C'est parce qu'elle lit et moi non ?"


"Il doit parler de Hanako. Bien qu'ils évitent tous deux les gens, j'ai bien envie de lui dire que lire est ce qui se fait généralement dans une bibliothèque. Donc s'il ne lit pas, quoi qu'il fasse ici le rend plus suspect qu'elle."


"En fin de compte, je suis surtout surpris parce qu'il est apparu de nulle part."


hi "Ça— ça ne me dit pas ce que tu fais là."

show kenji neutral
with charachange


ke "Je suis là à cause de toi."


"Sa réponse me perturbe un peu. Peut-être que je me suis endormi et que tout ça n'est qu'un rêve bizarre, et que Kenji n'est pas réel, mais juste mon subconscient. Est-ce qu'il va me donner des conseils profonds et vagues maintenant ?"

show kenji tsun
with charachange


ke "À cause de toi, je me suis fait chasser des dortoirs par des féministes. Maintenant, j’erre dans la bibliothèque, comme un soldat sans patrie, ou un fantôme. Je devrais te hanter, pour m'avoir fait ça."


"Dommage, ça aurait été un rêve intéressant, mais apparemment c'est réel."


ke "Ouais, il a fallu que tu travailles avec des femmes, et ça les a amenées à ma chambre. Tu te rappelles ? Tu devrais, vu que tu étais là. Après ce jour, j'ai su qu'elles étaient après moi. J'aurais dû suivre mon instinct, mais j'étais jeune et stupide."


hi "C'était il n'y a même pas une semaine."


ke "Puis, mon père m'a appelé et m'a dit qu'une de mes lettres ne leur était pas parvenue. La poste n'aurait pas pu la perdre, donc elle a dû être interceptée. Guerre des renseignements !"

show kenji neutral
with charachange


ke "C'est là que j'ai su que ma cachette secrète avait été compromise. Maintenant je suis en cavale, comme un fugitif. Code rouge."


hi "Les chambres ne sont pas secrètes, ils mettent ton nom et numéro de chambre sur un tableau à l'entrée."

show kenji rage
with charachange


ke "Je sais, j'ai vu. Elles sont diaboliques. Pourquoi ne pas mettre un grand avis de recherche comme dans le Far West, quitte à faire ça ?! “Recherché : Mort ou Vif !” Probablement vif, pour qu'elles puissent me cloner ou me transformer en sauterelle."

show kenji tsun at Position(ypos=1.15)
with Dissolvemove(0.5)


"Se précipitant sans prévenir sur la chaise vide en face de moi, Kenji sort une cigarette et commence à la faire tourner entre ses doigts. Je ne l'ai jamais vu fumer auparavant, donc ça doit être pour le genre que ça donne."


ke "Je ne peux même plus vivre où je veux maintenant. C'est là que tout commence."


ke "Quelle brillante tactique ... Je veux dire, une fois qu'elles sont dans ta chambre, c'est fini, comme des termites. C'est là que COMMENCE le plan féministe. Où est-ce que je peux aller maintenant ?"

show kenji happy
with charachange


ke "La seule question maintenant est comment est-ce qu'elles peuvent agir comme des termites quand elles sont naturellement repoussées par le bois."


hi "“Tu ne pourras plus jamais rentrer chez toi.” C'est ça ?"

show kenji neutral
with charachange


ke "Mec, je sais pas trop. Je vivais là. Je ne sais pas où d'autre je pourrais me laver ou avoir de nouveaux vêtements. Et manger. Et utiliser les toilettes. Et regarder la télé. Je dois continuer de regarder les informations, pour me tenir informé."


"Pour quelqu'un expulsé de sa chambre et vivant comme un fugitif, il n'a pas de problème à l'idée d'y retourner plusieurs fois par jour."


"Mais là, il s'est légèrement détourné de moi et parle avec un air à résoudre des crimes. Ça ne sert à rien de l’interrompre maintenant."

play sound sfx_can_clatter


"Je finis mon soda et le jette dans la poubelle proche de la porte. La canette se cogne contre le bord, mais rentre quand même. Je suis fier de moi."

show kenji neutral at center
with dissolvecharamove


"Kenji se lève rapidement et se dirige vers la porte. Je ne faisais pas vraiment attention. J’espère qu'il ne m'a pas vu faire une drôle de tête."


hi "Où est-ce que tu vas ?"

show kenji tsun
with charachange


ke "Tu n’arrêtais pas de t'enfiler ton jus de fruit."


hi "Et alors ? Ce n'était même pas du jus de fruit, c'était un soda. Et j'ai fini maintenant. Et comment ça “enfiler” ? J'ai dû boire deux gorgées."


ke "Ouais, bien sûr, tu as bu genre cinquante millions de gorgées."


hi "C'est impossible."

show kenji neutral
with charachange


ke "Peut-être pour toi ; je vais tout le temps au delà de l'impossible. Bon, peu importe, maintenant j'ai soif aussi. Je vais me prendre mon propre jus de fruit, je reviens tout de suite."

show kenji invis at Position(xpos=0.4)
with dissolvecharamove

with Pause(0.5)

show kenji neutral at center
with dissolvecharamove


"Il revient effectivement tout de suite, si rapidement que je le suspecte de connaître mon distributeur secret."


ke "Je t'en ai pris une aussi. J’espère que tu aimes le jus de raisin. On est quitte pour la pizza maintenant."


hi "Merci."

show kenji neutral at Position(ypos=1.15)
with charamove


"J'ai envie de lui dire que ce que je lui ai prêté coûtait au moins dix fois le prix d'une canette, mais ça ferait un peu radin. Kenji s'assoit et commence à boire son jus de raisin comme un homme furieux faisant une vendetta contre le raisin."

show kenji happy
with charachange


ke "Tu sais, c'est cool que je t’aie trouvé ici, mec. J'ai besoin que tu me rendes un service."


"Bien que ce soit cynique, je me demande s'il m'a pris un jus de fruit pour pouvoir me demander sa faveur. Si c'est le cas, c'est assez flagrant. Je doute que Kenji pense à mal à ce point, cela dit. Demander les choses directement lui ressemble plus."


ke "J'ai besoin que tu me recommandes quelques livres."


hi "Mais je croyais que tu ne lisais pas ?"

show kenji neutral
with charachange


ke "Comment tu sais ?"


hi "Tu me l'as dit. Tu as dit que tu pensais que les gens avaient un comportement discriminatoire avec toi parce que tu ne lisais pas."

show kenji happy
with charachange


ke "C'est le cas. Et je lis. Je lis des livres audio, parce qu'ils sont la manière de faire du futur."

show kenji neutral
with charachange


ke "Je dois lire un livre par mois pour le cours de littérature, et j'ai découvert que l'école n'avait pas de classiques tels que “La Cryptographie Avancée.” Si je ne lis pas un tas de bouquins, ils me feront échouer."

show kenji tsun
with charachange


ke "Je ne peux pas échouer en littérature... ça voudrait dire que je suis illettré. Ça voudrait dire que ma mère avait raison. Ma mère ne peut pas avoir raison. Je dois étudier la littérature autant que possible."


hi "Et si tu faisais en sorte d'avoir des crédits supplémentaires ?"


ke "Non merci. C'est déjà assez dur comme ça maintenant que j'ai à porter ces trucs stupides."


"Il ramasse un dictionnaire, le feuillette et le place sur l’étagère des meurtres mystérieux derrière lui."


ke "Je n'arrive pas à croire que c'était le média que nos ancêtres utilisaient pour regarder du porno."


"Je renverse ma boisson sur le livre que je suis en train de tenir, l'endommageant bien trop pour pouvoir l'arranger. Je regarde au dos du livre et vois que le prix de vente conseillé est 7900 yen. Je crois que je vais avoir une crise cardiaque."


show kenji happy
with charachange


ke "Woaw, détruit. Tu n'aurais pas dû faire ça, ils prennent le vandalisme super au sérieux ici. Tu vas prendre des coups de canne."


"Il rit un peu, amusé, avant de prendre une extrêmement longue et bruyante gorgée de son jus de fruit."


hi "Ce n'est pas du vandalisme, je n'ai pas fait exprès. Tu m'as fait faire ça, avec tes mots."


hi "Et c'est quoi cette histoire de coups de canne ? Je ne veux pas prendre de coups de canne."

show kenji neutral
with charachange


ke "Attends, calme-toi, ils ne le feront pas vraiment. Ils vont juste te faire payer et te crier dessus vraiment, vraiment fort. C'est comme s'ils allaient t'étriper. Pas grand-chose."


hi "Je m'en fous si c'est pas vraiment vrai, je ne veux pas me prendre de coups de canne, ou me faire étriper, ou quoi que ce soit, espèce de... d'idiot."


hi "Qu'est-ce que je vais faire ? Je suis la seule personne ici. Qu'elle sache, du moins. Je ne peux même pas jeter le livre dans la poubelle, il sera retrouvé, et elle le saura."

show kenji tsun
with charachange


ke "Sérieux, mec, arrête d’être aussi bizarre."


hi "En quoi c'est bizarre de ne pas vouloir d'amende ?"


ke "Mec, arrête de flipper, mec."


hi "Je ne flippe pas, j'essaye de garder mon argent."


ke "Radin."

show kenji invis at center
with Dissolvemove(0.5)

hide kenji
with None

stop music fadeout 1.0


"Je suis sur le point de l'étrangler quand j’entends le “wahaha” de Misha venant du couloir. Apparemment, Kenji l'entend aussi et profite de l’opportunité pour disparaître rapidement dans la section autobiographie. Comme le vent."

show mishashort hips_grin at center
with charaenter

play music music_comedy fadein 0.5


mi "Salut, Hicchan~ !"

show bg school_library at bgleft
show mishashort hips_grin at twoleft
with charamove

show yuuko neurotic_down at tworight
with charaenter


"Misha crie avec exubérance, traînant une Yuuko embarrassée derrière elle."

show mishashort sign_confused
with charachange


mi "Hicchan~ ! Tu parlais tout seul ?"


"D'un côté, dire oui me ferait passer pour un fou. D'un autre côté, si je dévoile la présence de Kenji, il pourrait sortir et me faire passer pour un fou."


hi "Oui."

show mishashort cross_grin
with charachange


mi "Ahaha~ ! C'est pas grave~ ! Ne sois pas embarrassé, Hicchan. Ça m'arrive aussi, des fois, quand je suis seule ! La~ la~ la~."

show yuuko worried_up
with charachange


yu "Hum... rien n'est arrivé pendant que j'étais partie ?"


hi "Absolument rien."

show yuuko worried_down
with charachange


yu "Ça sent le... raisin."


hi "Je porte de l'eau de cologne odeur raisin."


"Je mens éhontément. D’après sa réaction, je vais finir par penser qu'elle sait que je mens, ou qu'elle croit que j'ai un goût horrible pour l'eau de cologne."


"Vu que la brique de jus de fruit que j'ai bu est encore là, elle sait sûrement. Heureusement, elle ne cherche pas plus loin."


hi "Qu'est-ce que vous faites à deux ?"

show mishashort sign_smile
with charachange


mi "On a déjeuné ensemble~ ! Strictement professionnel, un déjeuner professionnel~ !"


"J'essaye d'imaginer Misha dans un costume, faisant un déjeuner professionnel avec quelqu'un. J'ai vraiment du mal."


hi "Pour quelle raison ?"

show yuuko panic_up
with charachange


yu "Tu ne sais pas ?"

show mishashort hips_grin
with charachange


mi "Ahaha~ ! Ce n'est rien~, rien~. C'est normal pour un membre du Conseil des Étudiants de ne pas savoir tout ce que le conseil fait~ !"


hi "Hé, ne dis pas “rien, rien” pour quelque chose comme ça. Ce n'est pas normal du tout. En fait, c'est vraiment pas bon. On est seulement trois."

show yuuko neurotic_up
with charachange


"Yuuko rit nerveusement. Elle doit être terrifiée."

show yuuko worried_down
with charachange


yu "Misha dit que tu veux mettre des affiches dans la bibliothèque... pour les élections. Hum... même si c'est dans vraiment longtemps, je pense que ce n'est pas un problème. Je ne savais même pas que je pouvais décider ce genre de choses..."

show mishashort cross_laugh
with charachange


mi "Tu peux~ ! Ce n'est pas super~ ? Ahaha~ ! Tu n'es pas contente ? Ouais~ ouais~ !"

show yuuko panic_up
with vpunch


"Misha attrape les mains de Yuuko et la force à applaudir joyeusement. Yuuko ne semble pas très joyeuse de savoir qu'elle a plus de pouvoir et de responsabilités qu'elle pensait à l'origine."

show mishashort sign_smile
with charachange


mi "Hicchan~ ! Vu que tu es là, tu peux m'aider à les mettre !"


"Sortant une pile géante d'affiches de son sac, elle en prend la moitié et me passe la moitié légèrement chiffonnée."

show mishashort hips_smile
with charachange


mi "Shicchan a eu une très bonne idée~ ! On pourrait mettre des flyers dans les livres aussi~ ! Comme ça, même si les gens essayent de nous ignorer, ils ne le pourront pas ! Ça pourrait même être des flyers à ressort !"


"Misha fait de son mieux pour imiter le ton de Shizune, c'est assez proche, et un peu menaçant."


hi "Elle plaisantait sûrement."

show mishashort perky_confused
with charachange


mi "J'ai bien aimé moi~."

show yuuko cry_up
with charachange


yu "N-non... s'il te plaît... pas ça..."

show mishashort cross_smile
with charachange


mi "Une super ultra agressive forme de marketing blitz~ ! On pourrait faire du porte à porte, aussi~ !"


hi "C'est une terrible idée."

show mishashort cross_frown
with charachange


"Misha fait la moue comme le fait Shizune, entrechoquant ses doigts d'énervement."


mi "Hicchan~ ! Tu trouves que chaque idée est terrible..."


hi "Ouais, mais cette idée est trop terrible, trop terrible pour être ignorée. Je ne peux pas faire ça."

show mishashort hips_smile
with charachange


mi "Wahaha~ ! Hicchan, on dirait presque un challenge. Mutinerie~, mutinerie~ !"

show yuuko cry_down
with charachange


yu "La m-mutinerie est une mauvaise chose... Ne vous battez pas."

show mishashort hips_grin
with charachange


mi "Wahaha~ ! Je plaisantais juste~ !"

show yuuko worried_down
with charachange


yu "D'accord..."

show yuuko worried_up
with charachange


yu "Ne vous battez pas."

show mishashort cross_laugh
with charachange


mi "Aha~ ha~ ha~."


"La façon qu'a Yuuko d’être ferme me rappelle un peu un professeur de maternelle. Je suppose que ça la rend très persuasive à sa façon."

hide mishashort
hide yuuko
with charaexit

stop music fadeout 5.0


"Accrocher les affiches est étonnamment dur, parce qu'il y a déjà beaucoup d'affiches et de flyers tous les quelques mètres, certains à des endroits tellement improbables que je ne les avais jamais remarqués auparavant."

play sound sfx_warningbell


"Décider lesquels d'entre eux je vais retirer pour mettre les nôtres n'est pas difficile mais prend beaucoup de temps. Au moment où la cloche sonne, signalant la fin de la pause déjeuner, Misha et moi avons encore pas mal d'affiches."


"Alors que nous partons, je décide d'en mettre une juste à la porte. Elle a dû être faite par Misha, elle a un petit dessin de Shizune dessus."

scene black
with dissolve

label fr_S28:

scene bg school_scienceroom
with locationchange


"Quelques jours plus tard, Shizune part manger toute seule et ne revient pas. Elle a dû être submergée de travail par le conseil, et je sais qu'elle va probablement faire presque tout ce travail toute seule."

scene bg school_hallway3
with shorttimeskip


"Quand j'arrive à la salle du conseil des étudiants, la porte est déverrouillée. Avant de l'ouvrir, j’attends une seconde, pour voir si j’entends le rire de Misha. Rien."


"Je pourrais presque penser qu'il n'y a personne, mais Shizune n'aurait pas laissé la porte déverrouillée."

play sound sfx_dooropen

scene bg school_council
with locationchange


"Elle est à son bureau, dormant assise sur sa chaise avec les bras croisés. C'est une drôle de position. Si elle n'avait pas les yeux fermés, je ne saurais même pas qu'elle dort. En fait, je ne suis même pas sûr qu'elle soit endormie."


"Normalement je taperais sur un bureau pour réveiller quelqu'un d'autre, mais ça ne marcherait pas pour elle. Je commence à imaginer tout ce que je pourrais faire si elle dort. C'est décevant que je pense directement à ça."

show shizu basic_normal at center
with charaenter


ssh "Bonjour. Salut."


play music music_shizune fadein 3.0


"Elle me salue une fois avec chaque main, c'est troublant."


his "Hé, qu'est-ce que tu fais ? Tu négliges secrètement ton travail ?"

show shizu behind_smile
with charachange


"Shizune sourit, mais baisse la tête pour l'avouer, et essaye de son mieux d'avoir l'air énervé à la place."

show shizu adjust_frown
with charachange


ssh "Ne reste pas là, ça me rend nerveuse si je suis assise et que tu ne l'es pas."


"Je m'assieds sur la chaise la plus proche pendant que Shizune ajuste ses lunettes comme si elle accordait un instrument."

show shizu adjust_angry
with charachange


ssh "Pourquoi est-ce que tu es aussi loin ?"


his "Ça te rend nerveuse aussi ?"


"Plissant les lèvres, Shizune ne semble pas trop amusée par ma moquerie."


his "J'avais du temps libre, alors je me suis dit que je pourrais passer voir si tu es toujours occupée."

show shizu behind_blank
with charachange


ssh "Tu veux m'aider ?"


his "Ouais."

show shizu adjust_smug
with charachange


ssh "Tant pis."

show shizu behind_smile
with charachange


ssh "Je t'en suis reconnaissante, mais ce n'est pas nécessaire. Je viens juste de finir, et maintenant tout ce qui devait être fait est terminé."


his "Tellement formelle. Misha était tout aussi sérieuse hier. Vous êtes toutes deux aussi sérieuses quand ça concerne officiellement le conseil des étudiants ?"

show shizu basic_normal2
with charachange


ssh "Je suis toujours sérieuse. Comme devraient l’être les candidats au conseil."


"Il ne lui a pas fallu longtemps. Critique immédiate des gens qui ne sont même pas encore ses collègues, alors que je n'ai même pas eu le temps d’étendre mes jambes en dessous de la table."

show shizu behind_frown
with charachange


ssh "Du moins les présidents. Ils doivent savoir faire preuve d'initiative, alors là peut-être qu'ils pourront motiver tous les autres, ou au moins les faire rester. Mais même s'il y en a pas mal, ils sont tous tellement inefficaces."

show shizu basic_angry
with charachange


ssh "Il n'y a personne qui concourt pour le poste de vice-président. Ils veulent tous le gros lot, mais aucun d'entre eux n'a ce qu'il faut pour ça. Et puis les trésoriers sont toujours si paresseux, j'ai décidé d'user de mon pouvoir pour éliminer ce poste."


his "Attends une seconde. Tu peux faire ça ? Je ne crois pas que ça marche comme ça."

show shizu adjust_frown
with charachange


ssh "C'est comme ça pourtant."


"Sur ce, Shizune regarde sinistrement vers l'horizon, frottant le bord de ses lunettes. Ça ne répond pas à ma question, futur dictateur."

show shizu behind_frown
with charachange


ssh "Je suis déçue. Ils devraient vouloir me faire partir pour avoir le job, ou au moins se battre contre moi pour l'avoir. Si je ne peux pas mobiliser quelques personnes pour le conseil des étudiants, alors tout mon travail aura été vain."

show shizu adjust_angry
with charachange


ssh "S'ils prévoient d’être aussi lents que ça, je tiendrai mon poste aussi longtemps que possible !"

play sound sfx_snap


"Shizune ponctue sa sentence d'un claquement de doigts, créant un son aussi tranchant qu'un coup de feu. Je me demande si elle sait à quel point c'est bruyant."


"C'est définitivement pour attirer l'attention, ce qui est inestimable pour une muette. Elle s'est peut-être entraînée rien que pour ça."


his "“Tout ton travail” ? Tu es trop sévère."

show shizu behind_blank
with charachange


ssh "J'ai toujours pensé que c'était le but final. Laisser une marque est important. C'est pour ça que je ne construis pas de château de sable, ils s'effondrent quand tu pars."


his "Peut-être, mais si j'en vois un qui est spécialement beau, je trouve ça impressionnant. Je dirais que c'est impressionnant."


his "Je t'admire pour ça. Donc, pour moi, ce n'était pas pour rien."

show shizu adjust_happy
with charachange


"Elle attrape ses lunettes comme si elle voulait les retirer, et sourit un peu."

show shizu basic_normal
with charachange


ssh "Désolée."

show shizu behind_blank
with charachange


ssh "J'ai pas fait attention et j'ai dit quelque chose d’égoïste."

show shizu basic_normal
with charachange


ssh "J'ai toujours voulu être au sommet. Peu importe le domaine, il fallait que je sois la meilleure, et que je comprenne tout, jusqu'à me l'approprier."

show shizu adjust_happy
with charachange


ssh "Comme quand tu entends une musique et rêves d’être un musicien, ou vois un avion et aimerais être un pilote. Tu as déjà eu un rêve comme ça ?"


his "Ouais."


"La première fois que j'ai joué au foot, je me demandais si je pourrais devenir assez bon pour que les gens m'admirent. Une fois que je vois la différence entre moi et les gens qui ont un vrai talent, je mets ces rêves de côté."


"Bah, avec mon cœur étant ce qu'il est, je ne peux plus jouer au football maintenant, de toute façon."


his "Tu as encore des rêves comme ça ?"

show shizu basic_normal2
with charachange


ssh "Non, ils sont irréalisables. Je m'en suis rendu compte assez vite. Il y a toujours quelqu'un de meilleur."


"Une expression nostalgique s'affiche sur son visage. Elle semble étrangement mature à cet instant, comme si les jours où elle combattait vigoureusement les autres pour la suprématie étaient loin derrière elle."


"Bien sûr, je sais que c'est loin d’être vrai. Rien que la semaine dernière, elle voulait voir qui de nous deux pourrait faire la plus grosse bulle avec un chewing-gum. Ça devait être encore pire quand elle était plus jeune, une terrifiante pensée."

show shizu behind_smile
with charachange


ssh "J'aimais ça. Qu'il y ait toujours quelqu'un de meilleur. Quand quelqu'un de meilleur que moi apparaît, ça m'excite. Je veux le défier."

show shizu adjust_frown
with charachange


ssh "Même si en fin de compte il s’avère meilleur, je serai en admiration. Il y a des gens qui sont à un niveau tout autre, complètement. Après un moment, je deviens jalouse, je veux quelque chose comme ça aussi."


his "Et c'est ce qu'est le Conseil des Étudiants ? La chose juste pour toi ?"

show shizu basic_normal
with charachange


ssh "Non, non. Même si je le ressens parfois, ce n'est pas pour ça que j'ai décidé de le faire. C'est une tout autre histoire."

show shizu adjust_happy
with charachange


ssh "Mais... J'aime être la présidente du Conseil des Étudiants. Même si le travail est dur et que je vois toujours tros grand, ça qui continue de m’intéresser. Les gens au sommet ne devraient pas pouvoir être confortablement assis à leur place."


his "Tu parles comme une fermière."


"Bien que ça ne lui irait pas, Shizune serait mignonne avec une salopette et un chapeau de paille."


his "Donc, si ce n'était pas cette raison-là, pourquoi tu as voulu le poste ?"

show shizu behind_frown
with charachange


ssh "Ce n'était pas le cas au début, mais j'ai décidé de le faire quand même. Je voulais être la présidente du Conseil des Étudiants parce que l'ancien Conseil des Étudiants était stupide."

show shizu basic_normal
with charachange


ssh "Et je veux remuer les gens, pour qu'ils puissent dire : “C'était intéressant. Aujourd'hui était une journée où j'ai fait des choses intéressantes.” Ce genre de choses. Des expériences mémorables."

show shizu behind_smile
with charachange


ssh "Je suis contente, parce que je crois qu'on a réussi. Toi, Misha, et moi."

show shizu basic_normal2
with charachange


ssh "J'ai un souhait égoïste aussi. Au début je pensais que c'était quelque chose qui pourrait être un joli bonus, mais je suis devenue gourmande."

show shizu behind_blank
with charachange


ssh "C'est pour ça que ça me rendrait heureuse si les élections se passaient bien. Ça serait la seule façon possible que mon souhait se réalise."


his "C'est quoi ce souhait ?"

show shizu adjust_blush
with charachange


ssh "C'est un secret."


"Sentant que je ne lâcherai pas le sujet aussi facilement, Shizune fait un signe de la main pour changer de sujet, rougissant d'embarras. C'est quelque chose qu'elle veut garder pour elle seule parce que c'est trop bête autrement."


"Je commence à avoir un peu faim, et regarde ma montre. Il est plus tôt que je croyais. Trop tôt pour dîner."


his "Tu as à manger dans ton bureau ?"

show shizu cross_wut
with charachange


"Pendant une seconde, on dirait que la question l'étonne."

show shizu behind_frustrated
with charachange


ssh "Les bureaux sont faits pour les fournitures et les provisions."


his "La nourriture, c'est des provisions."

show shizu basic_normal
with charachange


ssh "Tu aurais dû déjeuner."


his "Je ne pensais pas que ce serait un problème. Si j'avais travaillé, je n'aurais pas eu à y penser. J'aurais été trop occupé pour avoir faim."

show shizu adjust_happy
with charachange


"Elle lève une main jusqu’à sa bouche dans une tentative ratée de cacher un rire, et essaye de masquer ça en prétendant remonter ses lunettes."


his "Tu ne dois pas avoir faim toi, vu que tu as déjà mangé."


"Je ne sais pas signer ces mots donc je me contente de pointer du doigt l'emballage de nourriture chinoise qui se trouve au sommet de sa corbeille."

show shizu basic_normal
with charachange


ssh "Cela date d'hier."


his "Alors nous avons tous les deux faim. Allons prendre quelque chose à manger."


his "Pas à la cafétéria. Il n'y avait rien de bon ce midi, donc je doute vraiment qu'il reste quelque chose de bon ce soir. Tu veux commander quelque chose ?"

show shizu behind_frown
with charachange


ssh "Commander deux jours de suite est anormal. Seulement en cas d'urgence. C'est ma politique personnelle."


"C'est pour ça qu'on devrait penser à mettre à manger dans son bureau, ça serait plus facile de se débrouiller en cas d'“urgence”. J'ai envie de lui dire, mais signer au moins cinq fois à quel point je suis affamé m'a trop fatigué pour que je fasse le malin."


"Je suis grandement tenté, cela dit."


mi "Salut~ ! Salut, salut !"


"La voix distinctive de Misha se fait entendre depuis le couloir. Elle arrive la seconde d’après."

show shizu behind_blank at tworight
show bg school_council at bgright
with dissolvecharamove

show mishashort perky_confused at twoleft
with charaenter

mi "…"

show mishashort perky_smile
with charachange


mi "Hicchan~ ! Tu es là aussi~ !"


hi "“Aussi ?” Comment est-ce que tu savais qu'il y avait déjà quelqu'un ?"

show mishashort sign_smile
with charachange


mi "Si c'est ouvert, c'est qu'il y a quelqu'un~."

show mishashort cross_laugh
with charachange


mi "Wahaha~ !"

show mishashort hips_grin
with charachange


mi "J’interromps quelque chose~ ?"

show shizu basic_normal
with charachange


"Shizune secoue la tête."

show mishashort hips_smile
with charachange


mi "Génial~ ! C'est vraiment génial~ ! Mais~ ! J'étais sûre que ça serait le cas. Vous êtes en pause ?"


hi "C'est ce que je croyais aussi, mais il s’avère que le travail a déjà été fait, pour l'instant. C'est pour ça que tu es venue ?"

show mishashort perky_smile
with charachange


mi "Wahaha~ ! Ouais~ ! C'est exact, Hicchan !"


ssh "Désolée de te décevoir. On discutait juste pour savoir si on devait commander à manger ou non."

show mishashort hips_grin
with charachange


mi "Ça semble fun~."


hi "Shizune n'est pas très fun pour ça. Elle dit qu'elle ne peut pas commander à manger deux jours de suite. Tu as faim, aussi ? Parce que si c'est le cas, ça ferait deux voix contre une."

show mishashort hips_smile
with charachange


mi "Mh~ mh~, ça semble fun, Hicchan ! Et j'ai un peu faim aussi..."


hi "Je pensais que tu aurais fait passer ça pour une mutinerie."

show shizu adjust_frown
with charachange


"Shizune tient une branche de ses lunettes, pensant clairement que c'est une mutinerie, mais étant battue par un vote de 2 contre 1, il n'y a rien qu'elle puisse faire. Misha a déjà sorti son téléphone. Il est vraiment criard."

show mishashort sign_smile
with charachange


mi "Shicchan, tu nous avais promis qu'on aurait un truc de conseil des étudiants, juste pour nous, hein ? Hein, hein~ ! Ça peut aussi être ça~ !"

show shizu behind_frown
with charachange


"Shizune secoue lentement la tête. La dernière fête qu'elle pourra faire en tant que présidente du Conseil des Étudiants de Yamaku est trop spéciale pour elle pour qu'elle puisse l'associer à une envie spontanée d'un dîner."

stop music fadeout 3.0


"Même si je sais que la fête sera aussi quelque chose comme ça : un repas comme un autre, avec juste nous trois."

scene bg school_dormext_full_ss
with shorttimeskip


"Après qu'on ait fini de manger et de ranger, je leur dis au revoir et me dirige vers le dortoir. Même si je ne me sens pas particulièrement fatigué, je crois que je vais aller dormir directement ce soir."


"Si j'étais à la maison, ma mère me dirait de ne pas aller au lit juste après avoir mangé, mais ce qu'elle ne sait pas ne peut pas lui causer de tort."

scene bg school_dormhisao_ss
with locationskip


"Je regarde l'heure dès que je rentre dans ma chambre, et réalise qu'il est bien plus tard que ce que je croyais."


"Je me sens un peu bête de regarder l'horloge alors que j'ai un téléphone et une montre. Je retire ma montre et la tiens dans ma main, tout en tenant mon téléphone dans l'autre. Je me sens puissant. Et stupide."

play sound sfx_doorknock


"Je me prépare à aller me coucher sans entrain, et suis content quand quelqu'un frappe à ma porte après quelques minutes. Je me dis que ça ne pourrait pas être quelqu'un d'autre de Kenji, et je suis surpris quand il s’avère que c'est Misha."

play sound sfx_dooropen

scene bg school_dormhallway
show mishashort hips_smile at center
with locationchange


mi "Salut Hicchan~ !"

show mishashort perky_sad
with charachange


mi "Tu ne sembles pas content de me voir~..."


hi "Non, je suis juste un peu surpris. Est-ce que Shizune s'est rappelée qu'elle voulait que je fasse quelque chose après tout ?"


hi "Il est tard mais... peu importe. Heureusement que je ne me suis pas changé."

show mishashort sign_smile
with charachange


mi "Nope~. Je me suis juste dit que j'allais te rejoindre, Hicchan~ !"


hi "Pour t'amuser ?"


"Non, bien sûr que non. C'est parce qu'elle veut parler. Ça doit être quelque chose d'important, et quelque chose qu'elle ne veut pas que Shizune sache."


hi "Tu veux entrer ?"

show mishashort hips_grin
with charachange


mi "Ouais~ merci Hicchan !"

scene bg school_dormhisao_ss
show mishashort invis at center
with locationchange

show mishashort perky_smile_ss at Position(ypos=1.13)
with dissolvecharamove

play sound sfx_doorclose


"Elle rentre et s'assoit immédiatement sur la chaise. Ce qui est normal, mais je m'attendais à ce qu'elle s'assoie sur le lit."

show mishashort cross_frown_ss
with charachange


mi "Hicchan..."


"Misha fronce sévèrement les sourcils, les bras croisés. C'est comme si elle voulait jouer un rôle d'interrogateur effrayant. Tout ce qui manque est une moustache et une lampe se baladant et vacillant le long d'un fil."


mi "Tu as fait de la peine à Shicchan ?"

play music music_drama fadein 6.0


hi "Comment ça ?"

show mishashort hips_frown_ss
with charachange


mi "Quand j'ai été au bureau aujourd'hui, Shicchan ne pouvait pas m'entendre arriver. C'est pourquoi~ quand j'ai ouvert la porte, j'ai vu une expression vraiment confuse sur son visage. Shicchan semblait contente et triste, et~ je voulais savoir pourquoi."


hi "Ce n'était pas à cause de moi, je ne l'ai même pas vu, ça."


hi "Je crois qu'elle est déprimée parce qu'elle ne sera plus présidente du Conseil des Étudiants dans quelques mois."

show mishashort perky_confused_ss
with charachange


mi "Mh~... Quand j'ai demandé à Shicchan, elle a dit que ça allait~ !"


hi "C'est inutile. Shizune a beau dire ça, il est impossible qu'elle lâche le morceau aussi facilement."


hi "Je veux dire, il y a des fois où elle veut se battre contre moi pour la dernière pomme, ou du chocolat au lait, ou autre chose. Et pourtant ce n'est pas important."

show mishashort hips_frown_ss
with charachange


mi "Le chocolat au lait c'est important."


hi "D'accord, d'accord. Ne t’énerve pas. Mais pas autant que l'est le Conseil des Étudiants pour elle. Elle ne l'abandonnerait pas aussi facilement."

show mishashort hips_grin_ss
with charachange


mi "Wahaha~. Tu as raison~."


"Je croyais que c'était supposé être un interrogatoire, mais on dirait que Misha a déjà oublié."

show mishashort sign_smile_ss
with charachange


mi "Mais~ ! Je ne veux pas que Shicchan me mente pour se sentir mieux."

show mishashort hips_grin_ss
with charachange


mi "Hahaha~ ! La plupart des gens ne savent pas à quel point Shicchan est sérieuse et ils pensent qu'elle joue juste un rôle. Je suis contente que tu puisses la comprendre, Hicchan."


hi "C'est évident. Surtout vu comment elle en a parlé aujourd'hui."


"Misha se penche, visiblement intéressée, et pose sa tête entre ses mains."

show mishashort cross_smile_ss
with charachange


mi "Vraiment~ ? Qu'est-ce qu'elle a dit ?"


"Elles sont suffisamment proches pour que sa curiosité ne m’inquiète pas."


hi "Pourquoi elle a rejoint le Conseil des Étudiants. En quelque sorte. Elle a commencé à me raconter, mais a décidé que certains trucs devaient rester top secret. Elle a dit “C'est un secret.” Alors j'imagine que c'est ça. Un secret."

show mishashort sign_smile_ss
with charachange


mi "Eh bien~, si quelqu'un te dit qu'il a un secret, c'est en soi un secret aussi, Hicchan~ !"


hi "Tout comme selon toi, la chance est un talent ?"

show mishashort hips_grin_ss
with charachange


mi "Ça peut l’être !"

show mishashort cross_laugh_ss
with charachange


mi "Wahaha~ !"


hi "Fais attention, ne fais pas trop de bruit."

show mishashort perky_confused_ss
with charachange


mi "Pourquoi, Hicchan ?"


hi "Tu vas réveiller la moitié des gens dans le bâtiment, et en plus de ça, les dortoirs ne sont pas mixtes."

show mishashort hips_frown_ss
with charachange


mi "Hicchan, est-ce que tu penses à quelque chose de pervers ?"


hi "Arrête d'être bizarre."

show mishashort hips_grin_ss
with charachange


mi "Ahahaha~."

show mishashort hips_smile_ss
with charachange


mi "Si c'est le cas, c'est pas grave."


"Entendre ça me fait réaliser à quel point ça a été facile de parler à Misha tout ce temps, que j'ai pu être avec elle aussi longtemps sans ressentir le besoin d’être sur mes gardes. C'est la première fois que ça m'arrive."

show mishashort perky_sad_ss
with charachange


mi "Je me sens triste, Hicchan."


mi "C'est drôle, plus Shicchan est contente, et plus je suis déprimée. Même si je devrais être contente pour Shicchan. Je le suis... mais~, je ne peux pas parler de mes problèmes avec elle."


hi "Pourquoi pas ?"

show mishashort sign_sad_ss
with charachange


mi "Tout comme Shicchan ne peut pas parler de ses problèmes avec moi. C'est la même chose, Hicchan. Si on a ce genre de problèmes, alors je ne sais pas ce que je devrais faire. Je me demande... si je suis une mauvaise amie."






show mishashort perky_sad_close_ss at center
with characlose

stop music fadeout 2.0


"Misha se met sur le lit, et nous sommes maintenant à une dizaine de centimètres l'un de l'autre. Quelques secondes plus tard, elle avance sa tête et me fait un petit baiser. Elle a loupé mes lèvres, plus parce qu'elle a mal visé qu'à cause de moi."


hi "Qu'est-ce que tu fais ?"


"C'est juste une formalité. Je serais stupide si je ne comprenais pas où elle veut en venir, c'est juste que ça semble si peu plausible que j’espère qu'il existe un moyen pour que je n'aie pas à m'occuper de ça."


show mishashort hips_grin_close_ss
with charachange


"Maintenant elle décide d’être timide, et rit un peu, embarrassée."

mi "…"

show mishashort perky_smile_close_ss
with charachange


mi "Tu m'aimes bien, Hicchan ?"


hi "Ouais."


"Sa tête est enfouie dans ma poitrine. J'ai l'impression qu'elle parle à ma cicatrice. Elle pourrait être capable de la frotter avec sa joue."


"J'ai essayé trop longtemps de leur cacher. En y pensant, je me sens bête de m'en être autant inquiété."

show mishashort perky_sad_close_ss
with charachange



label fr_choiceS28:
menu:
    with menueffect
    mi "Réconforte-moi s'il te plaît, Hicchan. Juste pour ce soir."
    "Réconforter Misha.":





        return m1
    "Refuser.":


        return m2


label fr_S28a:

play music music_moonlight fadein 4.0


"Même si je prétends protester, j'ai autorisé les choses à en venir là. Même si je savais dès le début qu'elle voulait en venir à ça."


"Du moins, j'étais d'accord avec les conséquences. Je le sais, sinon je l'aurais repoussée."


"J'aurais pu n'importe quand, et c'était mal de ma part de ne pas le faire plus tôt, mais maintenant, ne rien faire signifie plus qu'un manque d’intérêt."

show mishashort perky_sad_close_ss:
    linear 0.2 alpha 0 ypos 1.1
with vpunch

hide mishashort
with None


"Misha prend mon silence comme un consentement, et se colle contre moi. Mes bras sont enveloppés par la douceur de sa peau et la chaleur de son corps. Je me penche presque par réflexe et finis sur elle."


"Elle me regarde, comme si elle s'attendait à ce que je mène la danse et ferme les yeux nerveusement la seconde d'après. N'ayant pas le choix, je commence à la déshabiller maladroitement, quelque chose que je n'ai jamais fait."

label fr_S28h:

scene evh misha_naked:
    xalign 1.0 ypos 0.0 subpixel True
    easein 12.0 xalign 0.0
with whiteout


"Après tout, je n'ai fait l'amour qu'une seule fois auparavant, et j'étais attaché à une chaise. Cette fois, je contrôle, comme je l'aurais voulu avant. Mais c'est un peu effrayant maintenant. Je commence par déboutonner sa blouse, et l’enlève."


"Son corps a plus de formes que je ne l'aurais cru, et cela s'accorde bien avec son visage mignon."


"Son soutien-gorge s'ouvre par derrière, et j'ai du mal à le retirer, partiellement parce que Misha semble honteuse de sa poitrine, et continue de la cacher en partie une fois que j'ai retiré le soutien-gorge."


"Quand je décroche sa jupe et commence à enlever sa culotte, elle offre un moment de faible fausse résistance. C'est juste une formalité."


"Je réalise maintenant que les formalités sont très importantes pour Misha. C'est pour ça qu'elle salue toujours tout le monde avec autant de joie, même quand elle n'est pas contente de les voir."


"Elle a les yeux ouverts maintenant, et je glisse ma main entre ses cuisses, me mettant presque à rire quand elle frissonne et m'écrase la main quand elle referme les jambes. Une réaction naturelle, assez mignonne."


"Shizune était plus douée pour masquer son inexpérience, même si elle était tout aussi embarrassée."


hi "Tu es prête ?"


"Elle hoche la tête sans même me regarder."

scene evh misha_sex_aside:
    truecenter
    subpixel True zoom 1.05
    easein 6.0 zoom 1.0
with locationchange


"Alors que je rentre en elle, je peux sentir qu'elle se raidit, nerveuse, ce que je commence à ressentir aussi quand je rencontre une résistance en elle. Je me sens si tendu que chaque fois que je bouge, c'est presque automatique."


"Je me demande si je devrais aller plus vite, comme Shizune. Mais Shizune est assez directe. C'est une situation différente maintenant, dans laquelle je regrette de m'être engagé. Je commence à m'avancer lentement, et Misha grimace de douleur."


mi "Fais ça vite s'il te plaît..."

scene evh misha_sex_closed:
    zoom 1.0
with locationchange


mi "Aie..."


"Je m'arrête."

scene evh misha_sex_aside
with locationchange


mi "Non, ça va."


"Et alors que je rentre de plus en plus loin en elle, Misha m'attrape les bras et les ressaisit un peu plus haut, comme si elle essayait de les escalader."


"M'attrapant les épaules, elle me serre contre elle, nous joignant encore plus profondément, et je ne peux rien faire pour la repousser."

scene evh misha_sex_closed
with locationchange


mi "Ah~... aaah..."


"Entendant ses gémissements, j’accélère et trouve un rythme. Elle s'agrippe à mon dos, et je sens ses coudes se caler en dessous de mes côtes tandis que je continue mes mouvements en elle."


"Mon sang bat dans mes tempes, je peux à peine l'entendre."


mi "Hnn~..."

scene evh misha_sex_aside
with locationchange


mi "C'est ma première fois avec un homme. C'est bizarre."


"J'aimerais qu'elle arrête de parler. Sa voix est si faible et saccadée par sa respiration que j'ai du mal à l'entendre, mais le ton de tristesse qui ponctue sa voix est immanquable, et je me sens encore plus coupable."


"Je suis censé la réconforter, mais c'est entièrement physique, et si ça lui fait du bien, elle ne le montre pas en tout cas. Ce qui remet en cause ma décision. Je commence vraiment à douter."

scene evh misha_sex_closed
with locationchange


"Malgré ça, ses doux gémissements à mon oreille me font continuer, tout comme l’étreinte chaude et glissante autour de mon membre. Au bout d'un moment, elle passe ses jambes autour des miennes et se tend dans un orgasme."

scene evh misha_naked
with whiteout

stop music fadeout 6.0


"Il lui faut une minute pour qu'elle se sépare de moi. Ça me donne l'opportunité de voir son corps entier nu, sa peau quelque peu rougie et parsemée de sueur. J'ai froid."


mi "...Hicchan ?"


"Je n'entends rien à part le tic-tac de l'horloge et le son de ma propre respiration."


mi "...Peu importe, Hicchan."


"Je cherche la main de Misha avec la mienne, et la caresse. Elle semble si légère et délicate, même lorsqu'elle m'attrape fermement le poignet. Le sentiment m'est familier."

scene black
with dissolve




label fr_S28b:

show mishashort perky_sad_close_ss:
    linear 0.2 alpha 0 ypos 1.1
with vpunch

hide mishashort
with None

play sound sfx_pillow


"Avant que je ne puisse répondre, elle se pousse contre moi de tout son poids, et ça suffit pour nous faire tomber tous deux sur le lit. Si je ne réponds pas rapidement, alors la situation ne fera qu'empirer."


"Je sais que je n'aurais pas dû laisser les choses en arriver à ce point-là."


"Donc, même si ce n'est pas la manière la plus délicate de lui répondre, je la repousse. Misha tombe en arrière sur les draps, si légèrement qu'on dirait qu'elle est à peine dessus. Elle reste comme ça pendant un moment, avant de se lever et de rire, gênée."

show mishashort invis:
    center
    ypos 1.2
with None

show mishashort perky_sad_ss at center
with dissolvecharamove

play music music_moonlight fadein 6.0


mi "Tu as raison, Hicchan. Je suis désolée."

scene black
with shuteye


"Je ne sais pas vraiment comment je me sens. Je regrette, légèrement. Triste, pour une multitude de raisons. Je suis aussi un peu énervé, à la fois contre elle et contre moi. Et d'un autre côté, j'ai l'impression de ne rien ressentir du tout."


hi "Ne le sois pas."


mi "Non, Hicchan. C'est pas grave~. Je le suis, vraiment, vraiment~."


mi "Juste... demander m'a suffit, je crois."


mi "Je suis contente que tu aies dit non."


hi "C'est vrai ? Bon, tant mieux."


mi "Ouais~, c'est vrai. Merci, Hicchan."


"Elle se redresse et s'adosse au mur. Du moins je crois. J'ai tellement mal à la tête que je n'ouvre pas les yeux. Je reste allongé sur le lit, écoutant le bruit de mes cheveux bougeant sur les draps et le vent faisant onduler l'herbe à l'extérieur."


"Je pourrais peut-être dire quelque chose de plus pour la rassurer, mais je me demande si ça aiderait vraiment. Peut-être qu'il serait mieux de ne rien dire. Je ne sais pas, dans cette situation, il n'y a pas grand-chose que je puisse faire."


mi "Bonne nuit, Hicchan."

play sound sfx_doorclose

stop music fadeout 4.0


"Sur ce, elle part, la porte se refermant derrière elle comme un chuchotement coupable."


"Peut-être que c'est parce que j'ai envie de mettre ça derrière moi, mais après que Misha soit partie, je m'endors facilement. Presque instantanément."

scene black
with dissolve




label fr_S29:

scene bg school_dormhisao
with locationchange

play music music_night fadein 4.0


"Le matin suivant, je me réveille pensant que je vais passer la plupart de mon temps à éviter Shizune et Misha."


"Ce qui est arrivé hier soir me met toujours mal à l'aise. J'aurais cru que dormir m'aurait aidé à alléger ce sentiment. Je me sens comme un idiot d'avoir cru que ça serait aussi facile."


"Je me demande si Misha se sent pareille. Si c'est le cas, elle ne viendra sûrement pas à l'école aujourd'hui. J'envisage de faire de même, mais ça serait plutôt suspect, et rester enfermé toute la journée juste par peur ne m’intéresse pas."

scene bg school_scienceroom
with locationskip


"Comme je le pensais, Misha n'est pas en classe ce matin. Shizune est là, mais c'est une grosse journée, alors elle se concentre en classe, ce qui signifie qu'elle n'a pas vraiment le temps de commencer une conversation avec moi."


label fr_S29a:


"C'est étrange que je doive éviter d'avoir une conversation avec Shizune alors que j'ai essayé pendant longtemps d'en avoir justement une, mais je ne sais pas quoi faire d'autre. J'ai couché avec sa meilleure amie."


"Si je me sens comme ça, je me demande comment se sent Misha. Tout aussi pleine de regrets que moi ? Quand elle est venue me voir, elle était plus déprimée qu'excitée. Je n'imagine même pas à quel point elle doit se sentir mal."


"En y pensant comme ça, j'ai envie de la revoir. Mais seulement un peu. Une partie de moi est toujours terrifiée, même si je déteste utiliser ce mot."


"Je me sens honteux, et je suis sûr que c'est la seule façon valable de me décrire. Ce n'est pas un bon sentiment."


label fr_S29b:


"J'ai été tellement habitué à voir Shizune et Misha ensemble que je n'avais pas remarqué jusqu’à hier à quel point ce n'était plus le cas récemment."


"Et c'est dommage, parce que le siège vide à côté de moi me rappelle qu'elles vont de pair. Il serait mieux que j'emporte dans ma tombe ce qu'il s'est passé hier soir."


"Si je me sens comme ça, je me demande comment se sent Misha. Tout aussi pleine de regrets que moi ? Quand elle est venue me voir, elle était plus déprimée qu'excitée. Je n'imagine même pas à quel point elle doit se sentir mal."


"En y pensant comme ça, j'ai envie de la revoir. Mais seulement un peu. Une partie de moi est toujours terrifié, même si je déteste utiliser ce mot."


"Je me sens honteux, et je suis sûr que c'est la seule façon valable de me décrire. Ce n'est pas un bon sentiment."


label fr_S29x:

scene bg school_library
with shorttimeskip


"J'ai passé les heures suivantes à la bibliothèque, pas d'humeur à m’asseoir en classe pour le reste de la journée, mais n'ayant pas envie de retourner aux dortoirs."

show shizu invis at center
with None

show shizu behind_frown at Position(ypos=1.14)
with dissolvecharamove


"Pendant que je feuillette sans conviction les pages d'un roman historique inintéressant, Shizune s'assied sur la chaise en face de moi, faisant la moue."

show shizu adjust_frown
with charachange


ssh "Je crois que ça ne sert pas à grand-chose de venir à l'école puis de sauter les cours."


his "Désolé."

show shizu behind_frustrated
with charachange


ssh "Au moins dis à tout le monde que tu es malade."


his "Je ne le sentais juste pas aujourd'hui. Ça allait hier, demain ça ira sûrement. Être malade juste une journée au milieu de la semaine est trop suspect. L'histoire de la “grippe de 24 heures” ne passera pas."

show shizu adjust_frown
with charachange


ssh "Ce n'est pas suspect."


his "Si ça l'est."

show shizu basic_angry
with charachange


"Je retourne à mon livre, mais Shizune le met gentiment de côté, ce qui contraste avec son expression, qui varie entre inquiétude et colère."

show shizu behind_blank
with charachange


ssh "Quelque chose ne va pas ?"


his "Quoi ?"

show shizu basic_normal2
with charachange


ssh "Est-ce qu'il y a quelque chose qui t’embête ? Parce que tu agis de façon un peu suspecte aujourd'hui, d'une manière différente."

show shizu behind_blank
with charachange


ssh "Si c'est le cas, dis-le-moi, ou alors je serai en colère. Je ne suis pas douée pour deviner ce que pensent les gens."


"C'est bizarre de dire ça, alors qu'elle a deviné comment je me sentais si facilement."


"Elle plaisante à moitié, mais il y a du vrai dans ce qu'elle dit. Après tout, elle ne peut pas entendre mon ton, et doit lire des signes pour communiquer."


"C'est comme si tu parlais à quelqu'un via des textos. Ça ne facilite pas les choses."


"C'est probablement pour ça qu'elle fixe si intensément les gens, pour jauger leurs réactions. Ou peut-être que c'est pour ça qu'elle pousse souvent les gens, pour les faire réagir."


"J'y ai déjà pensé auparavant, mais il est trop difficile de savoir à coup sûr quelles sont les exactes motivations de Shizune."


"Donc, je me demande si elle plaisantait vraiment. Même si ce n'était pas le cas, je ne peux pas lui dire. Vu que c'est en langue des signes, j'ai suffisamment de temps pour réfléchir et mentir efficacement."


his "Rien."

show shizu cross_wut
with charachange

shi "…"


his "Je pensais beaucoup à l'avenir du Conseil des Étudiants, récemment. Je crois que c'est pareil pour Misha... enfin, à sa façon."

show shizu behind_frustrated
with charachange


ssh "Tout comme moi, mais elle n'est pas là aujourd'hui. J'aurais aimé qu'elle me dise quelque chose, j'aurai sûrement besoin de son aide tout à l'heure. De la tienne aussi, sauf si tu es occupé."


his "Non ça va..."

show shizu basic_normal
with charachange


ssh "Merci."

show shizu behind_sad
with charachange


ssh "J'ai l'impression de perdre beaucoup de gens proches de moi, récemment."


"Je ne sais pas quoi répondre à cela. Quelque chose de rassurant et intime, lui disant de ne pas s’inquiéter. “Je suis là pour toi, je ne fais pas partie de ces gens.”"


"Alors, de qui elle parle ? Et ça ferait trop forcé de lui dire ça. Je fais un signe de la main qui fait un peu antipathique."


his "Tu ne devrais pas penser ça."

show shizu basic_normal2
with charachange

shi "…"


his "Je suis peut-être juste un peu malade, pas suffisamment pour m’embêter à rendre ça officiel. C'est plus facile pour moi comme ça."

show shizu behind_frown
with charachange


ssh "C'est pas la bonne chose à faire."


"J'ai entendu que la façon la plus dure est souvent la meilleure, l'inverse doit être vrai aussi."

show shizu basic_normal
with charachange


ssh "Bon, d'accord. Si tu dis que tu vas bien, alors ça me va."


his "Attends."

show shizu behind_blank
with charachange


shi "… ?"


his "Tu me l'as demandé, alors je te retourne la question. Tu vas bien toi ?"

show shizu basic_normal2
with charachange


ssh "Oui."

stop music fadeout 3.0


"Elle le signe sans un moment d’hésitation. Après ça, Shizune attend pour voir si je vais ajouter quelque chose."

show shizu invis at center
with dissolvecharamove

hide shizu
with None


"Je ne dis rien, et elle part. Je me sens comme un idiot de ne pas avoir continué, même si je pense que c'est mieux de n'avoir rien fait."


"Je suis à la bibliothèque depuis un moment, et décide d'aller sur le toit pour changer d'air."

play sound sfx_door_creak
play ambient sfx_rooftop fadein 1.0

scene bg school_roof_ss
with locationskip


"Une brise fraîche m’accueille à la seconde où j'ouvre la porte. C'est vraiment mon endroit préféré de l'école. Je vois que je ne suis pas le seul là. Je peux voir une fille avec les cheveux couleur chewing-gum devant moi."


"Elle est de dos, mais je n'ai pas besoin de voir son visage pour savoir qui c'est. Je suis sûr que Misha est la seule personne au monde à avoir les cheveux comme ça."


"J'ai le sentiment que je la surprends à un mauvais moment. Elle voulait évidemment être seule, et je me demande si elle ne m'a pas remarqué. Si c'est le cas, je vais partir. Mais elle se tourne face à moi."

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

scene ev misha_roof_normal:
    yalign 1.0 xalign 0.5 subpixel True
    easein 12.0 yalign 0.0
with whiteout

play music music_sadness fadein 8.0


mi "Oh, Hicchan, je pensais bien qu'il y avait quelqu'un derrière moi, mais je ne m'attendais pas à ce que ce soit toi. Cette fois, c'est toi qui m'as surprise."


"Si elle fait référence à son habitude d'arriver derrière moi et de demander qui c'est... Ça ne m'a jamais surpris."


hi "Je suis surpris, aussi. Mais tant mieux, je voulais te parler de quelque chose de toute façon."

mi "…"


hi "Pas de ça..."


hi "Qu'est-ce qui se passe entre Shizune et toi ? Elle ne veut pas me dire, alors je te demande."


"“Parce que c'est plus facile d'avoir une réponse de ta part, vu que la même latence qui me donne le temps de mentir lui donne le temps d'éviter mes questions.” Alors que je vois qu'elle hésite, je la pousse un peu."


hi "Donne-moi une réponse honnête, s'il te plaît."


mi "C'est compliqué, Hicchan... C'est à cause de quelque chose qui est arrivé il y a longtemps. Je croyais pouvoir oublier, mais~... c'est vraiment dur. Donc~, entre ça et les examens, je voulais passer plus de temps avec Shicchan~ !"

scene ev misha_roof_sad
with charachange


mi "Mais Shicchan est toujours occupée maintenant. Donc~ ! On s'est disputées. Mais j'en ai marre maintenant."


mi "Parce que~... J'aime Shicchan."


hi "Tout comme moi."

scene ev misha_roof_normal
with charachange


mi "Wahaha~. Non, non~. Je sais que tu l'aimes, Hicchan. Je voulais dire que j'aimais Shicchan de la même façon que toi."

scene ev misha_roof_closed
with charachange


mi "Je veux qu'elle soit ma petite amie."


"Misha ferme les yeux, comme un criminel condamné à confesser ses crimes en face d'un bourreau. J'ai du mal à trouver une réponse, et je sais que je dois en faire une."


hi "Je vois. Je ne savais pas."

scene ev misha_roof_normal
with charachange


mi "Je ne voulais pas vraiment venir dans cette école, Hicchan~. Mais ça semblait intéressant, et même si tout le monde me détestait, au moins ils me laisseraient tranquille. J'apprenais la langue des signes, mais je n'étais pas très douée~."


mi "Shicchan était en train d'essayer de recruter des gens au Conseil des Étudiants, parce qu'il n'y avait que Lilly et elle. Puis, elle est venue me voir. Je ne pouvais pas la comprendre du tout~."

scene ev misha_roof_angry
with charachange


mi "Mais~ ! Shicchan ne voulait pas utiliser de crayon. Elle savait que je prenais des cours. Elle s'est rendu compte que je n'étais pas douée~... Alors j'ai travaillé plus dur, et j'ai détesté Shicchan et cru qu'elle se moquait de moi."

scene ev misha_roof_normal
with charachange


mi "Ce n'était pas ça la raison pourtant~..."





mi "Donc~ ! Je suis lentement tombée amoureuse de Shicchan, et lui ai dit... que je l'aimais."

scene ev shizu_flashback:
    truecenter
    zoom 1.15 subpixel True
    easein 30.0 zoom 1.0
with whiteout


mi "C'était dans la salle du conseil, tu sais. Quand on était juste deux."


mi "J'avais cette image de Shicchan assise seule dans la salle du conseil, essayant de tout faire toute seule. Ça me semblait si triste~. Je pense que je voulais que ce soit comme ça~."


mi "Comme ça, je pourrais être là pour Shicchan, et peut-être que Shicchan m'aimerait. Même s'il n'y avait pas de raison pour que je croie ça, c'était quand même le cas. Je voulais que ce soit vrai, alors je me laissais imaginer ça."


mi "Cette journée était vraiment, vraiment~ magnifique Hicchan~. On avait tout fini, et je regardais par la fenêtre. Même par la fenêtre, le soleil était si chaud~... Je voulais rester comme ça pour toujours, à côté de Shicchan."


mi "Mais~ ! Quand j'ai regardé Shicchan, elle tournait le dos à la fenêtre et travaillait encore sur quelque chose, s'isolant du reste du monde. Le soleil était sur ses épaules, comme quand on me mettait une couverture sur les épaules quand j'étais petite."


"Misha s’arrête pendant une seconde comme si elle essayait d'immobiliser la vision de Shizune dans son esprit."


mi "Shicchan semblait... mh~... C'était comme si Shicchan était d'une façon qui me donnait envie d’être avec elle... Mais je ressentais que ça serait difficile."


mi "Wahaha~. C'était il y a~ un vraiment~ long~ moment. Mes cheveux étaient différents à l'époque aussi. Un peu en bataille~. Je les ai coupés parce que Shicchan m'en parlait tout le temps."


mi "Bref~ ! Je lui ai dit, à ce moment-là, je lui ai avoué mes sentiments."

scene ev misha_roof_sad
with whiteout


mi "Et j'ai été repoussée~."


mi "Donc~, je me suis dit que c'était fini, Hicchan. Mais Shicchan continuait de me parler, et je l'ai encore détestée pour ça. Et quand je lui ai demandé pourquoi elle faisait ça, elle m'a dit que c'était parce que j'étais son amie."


"Ses joues sont légèrement rosées. Je me demande si elle a beaucoup pleuré pour pouvoir se retenir comme ça. Si elle ne s’était pas arrêtée pour s'essuyer les yeux, je n'aurais jamais remarqué."

scene ev misha_roof_closed
with charachange


mi "Que Shicchan me dise ça m'a fait plaisir, mais m'a aussi rendue triste, même si elle ne voulait pas me faire de mal, ça faisait quand même mal. Même maintenant..."


mi "Shicchan a une façon de manipuler les gens, Hicchan. Des fois elle fait exprès, et des fois pas vraiment, mais ça arrive quand même~. Et des fois je ne sais pas... et je doute..."


mi "Je souhaiterais juste que Shicchan m'aime, plutôt que toi. Je me suis demandée si je n'avais pas commencé à vous détester Shicchan et toi... juste un petit peu... Je... n'aime pas ça."


hi "Donc tu t'es dit que peut-être ça serait mieux si je n'étais pas là ?"

scene ev misha_roof_normal
with charachange


"Elle semble confuse. Cette pensée ne lui a jamais traversé l'esprit."


mi "Ce n'est pas ça, Hicchan."

scene ev misha_roof_sad
with charachange


mi "J'y ai beaucoup pensé ces derniers jours, et je ne veux plus détester qui que ce soit. Shicchan ou toi. C'est nul que j'aie ressenti ça comme ça, hein, Hicchan ? Je ne veux plus jamais penser à ce genre de choses."


mi "Et que les gens me manquent, et qu'ils soient séparés de moi. Je suis fatiguée de tout ça, je ne veux plus jamais y penser."


mi "Et pourtant je l'ai fait. Donc~ !... Je suis vraiment la pire. Je ne pensais pas que ce serait mieux si Hicchan n'était jamais venu ici. Je pensais... si ça n'aurait pas été mieux si j'étais juste morte ?"


label fr_S29xa:


scene ev misha_roof_closed
with charachange


mi "Après tout, j'ai fait quelque chose de vraiment horrible. Impardonnablement horrible."


"Misha s'appuie encore plus contre le grillage, comme si elle espérait passer à travers."


hi "Ne sois pas stupide."


"Je suis surpris par le ton de ma voix."


hi "Désolé."


hi "J'ai réalisé que je déteste quand je regrette quelque chose. Et pourtant, ça continue d'arriver."


hi "Hier, j'ai fait quelque chose de stupide. C'est probablement partiellement à cause de ça que je suis là maintenant, pour que je puisse trouver comment... arranger ça, sûrement."


hi "Tu as déjà ressenti ça ? Tu as dit que tu avais fait des choses terribles. Tu peux essayer de les réparer."

scene ev misha_roof_normal
with charachange


mi "Hicchan~, est-ce que..."


"Je sais qu'elle croit que je dis ça plus pour moi que pour elle."


hi "Non. Ce n'est pas ça."


hi "Je crois juste que te suicider se définit comme le plus grand des regrets qu'une personne puisse avoir."

mi "…"


mi "Hicchan, tu es vraiment dramatique."

scene ev misha_roof_closed
with charachange


"Qu'elle ait été sérieuse ou non, je ne le saurai jamais. Je n'essaye pas de le découvrir, elle laisse échapper un soupir et ferme les yeux comme si elle allait s'endormir. Je pense que l'humeur dangereuse dans laquelle elle était est passée."


label fr_S29xb:

stop music fadeout 0.5
$ renpy.music.set_volume(0.0, 0.5, channel="ambient")


"Misha s'appuie encore plus contre le grillage, comme si elle espérait passer à travers."

scene bg school_roof_ss
show mishashort perky_confused_close_ss at center
with vpunch

$ renpy.music.set_volume(1.0, 6.0, channel="ambient")


"Sans vraiment y penser, je lui attrape la main. Mes réflexes sont mauvais, et je n'arrive qu'à agripper quelques-uns de ses doigts, mais ce n'est pas important."

play music music_rain fadein 6.0


hi "Désolé. C'est juste que tu as dit quelque chose d'assez bizarre."

show mishashort perky_sad_close_ss
with charachange


mi "Hahaha~. Ouais~, c'est vrai, Hicchan."


hi "Ouais."


hi "Tu veux savoir ce que je pense ?"


hi "Shizune est le type de personne qui ne laissera personne s'approcher sauf à ses conditions. C'est frustrant, parfois même exaspérant."


hi "Ça m'aurait probablement embêté quand j'étais à l’hôpital et que je refusais d'entendre parler de tous ceux qui m'abandonnaient. J'avais tout oublié jusqu’à récemment. J'ai reçu une lettre, et c'était tout."


hi "J'étais furieux. Je me suis dit “Comment est-ce qu'elle peut m'accuser de me renfermer et d'abandonner ? Ce n'est pas ce que tout le monde a fait pour moi ? Qu'est-ce que je suis censé faire ? Qu'est-ce que je peux faire ?”"


hi "Ouais, même maintenant, je sais que c'est comme ça que c'est arrivé, mais... elle avait raison, aussi. Je me suis renfermé."


hi "Donc, j'ai décidé que je ne laisserais pas cela se reproduire."

show mishashort perky_confused_close_ss
with charachange


label fr_S29xba:


mi "L’hôpital ? Hicchan... ces pilules sont là pour ça ?"


label fr_S29xbb:


mi "L’hôpital ? Hicchan... qu'est ce que..."


label fr_S29xbc:


hi "Écoute-moi s'il te plaît."


hi "Shizune est l'opposé de ce que j'étais. Elle a toujours voulu attirer les gens dans sa vie. C'est la seule raison pour laquelle Shizune s'est intéressée à moi à la base, je crois."


hi "Je crois que j'étais déterminé à ne pas laisser ça arriver, d'une certaine façon."


"Misha baisse les yeux, comprenant parfaitement ce que je veux dire."


hi "Je n'ai jamais réalisé à quel point ça pouvait être dur."


hi "Et maintenant, je crois que je veux lui retourner la faveur, même si ça prend deux fois plus longtemps. J'ai déjà appris une seconde langue jusque-là."


hi "Ce n'était pas aussi dur que je le croyais, mais c'était quand même dur. Des fois, j'avais l'impression d'escalader une montagne tellement mes mains me faisaient mal."


hi "Et tu as fait la même chose. Et c'était pour la même raison, n'est-ce pas ? C'est vraiment impressionnant. C'est aussi pour ça que ça me rend triste, et un peu en colère, que tu dises une chose stupide comme ça."

mi "…"


hi "C'est juste ce que je crois, du moins."

show mishashort perky_sad_close_ss
with charachange


"Elle se ramollit et glisse presque sur le sol, comme si elle avait été drainée de son énergie."


mi "Tu es trop dramatique, Hicchan."


"Elle dit ça tout en détournant le regard, comme si elle voulait regarder en contrebas, mais ne le fait pas."


mi "Wahaha~."


label fr_S29y:

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene bg school_roof_ss
show mishashort perky_confused_close_ss at center
with locationchange

stop music fadeout 0.5
$ renpy.music.set_volume(0.2, 0.0, channel="sound")
play sound sfx_door_creak


"La porte derrière nous s'ouvre, se faisant à peine entendre par-dessus la brise ambiante."

scene bg school_roof_ss at bgleft
show mishashort perky_confused_close_ss at closeleft
with charamove

show shizu behind_blank_ss at tworight
with charaenter


ssh "Je vous cherchais partout. C'est une réunion secrète ?"


"Elle s'approche de nous, s'adosse au grillage à côté de Misha comme si elle avait besoin de s’arrêter pour reprendre son souffle, avant de s'en retirer et de continuer."

show shizu basic_normal_ss
with charachange


ssh "Je suis fatiguée d’être au conseil des étudiants chaque jour sans que vous veniez. Prendre du temps libre est une bonne chose, mais là c'est trop."


"En temps normal, Misha et moi trouverions des excuses en plaisantant. Cette fois, il n'y a que le silence. Shizune, s'attendant à une résistance, est perturbée par l'absence d'une telle chose."

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_snap
show shizu adjust_happy_ss
with Dissolve(0.3)


"Quelques secondes passent dans un lourd silence, que Shizune rompt avec un claquement sec des doigts, souriant comme pour dire “eurêka.”"

show shizu basic_happy_ss
with charachange


ssh "Faisons quelque chose ensemble."


hi "Comme quoi ?"

show shizu behind_smile_ss
with charachange


ssh "N'importe quoi ! On devrait aller au bureau du conseil d'abord, et puis décider là-bas."


hi "Ça ressemble beaucoup à un piège pour nous amener à travailler."

show shizu basic_normal2_ss
with charachange


ssh "Très drôle."


label fr_S29ya:

show shizu behind_smile_ss
with charachange


ssh "Ce n'est pas un piège. Je le promets. Ça sera quelque chose d'amusant."

show mishashort perky_sad_close_ss
with charachange

play music music_rain fadein 4.0


"Misha contraste le sourire de Shizune avec une expression triste."


"Si Misha est vraiment jalouse de moi pour lui avoir volé Shizune, alors ça ne fait qu'empirer quand nous sommes tous les trois. J'imagine que c'est comme mettre du sel sur une blessure ouverte. Donc j'ai dans l'idée de les laisser toutes les deux."


"Je ne suis pas naïf au point de croire qu'un seul après-midi à deux résoudra tout, mais ça peut aider. Ça me semble une meilleure option que d'aller avec elles, parce que ma présence n'aidera vraiment pas du tout."


hi "Allez vous amuser toutes les deux alors. Je vais me coucher tôt."

show shizu basic_normal_ss
with charachange


ssh "Tu es sûr ? On vient de manger."


hi "Je te l'ai dit, je ne me sens pas très bien aujourd'hui, je crois que je couve quelque chose."


show shizu adjust_frown_ss
with charachange


ssh "Je pensais t'avoir dit que des excuses comme ça ne marchent pas."


"Elle m'a eu sur ce coup."

show shizu basic_normal2_ss
with charachange


ssh "C'est pas grave. Par contre refuser l'invitation de quelqu'un est impoli. J’espère que tu te rattraperas."

show shizu adjust_happy_ss
with charachange


"Shizune se tourne et sourit à Misha, et commence à signer quelque chose que je ne peux pas voir. J'imagine que c'est quelque chose du genre “on dirait qu'on ne va être que nous deux.”"

stop music fadeout 3.0


"C'est bien."

stop ambient fadeout 2.0

window hide



label fr_S29yb:

show mishashort hips_grin_close_ss
with charachange

play music music_comfort fadein 5.0


"Misha rit, réussissant à laisser sortir un “wahaha” forcé. Le fait que Shizune ne puisse pas le voir me fait plaisir. Ça veut dire que ce n'était pas juste pour elle."

show shizu behind_smile_ss
with charachange


ssh "Je pensais que vous pourriez m'aider pour quelque chose. On ne peut pas manger à l'extérieur. On a déjà commandé hier et rompu mon principe, trois jours de suite ce serait impardonnable."

show mishashort perky_smile_close_ss
with charachange


mi "Mais~ ! C'était une livraison, Shicchan~ ! Manger dehors est différent."


hi "Ouais, rien à voir."

show shizu adjust_frown_ss
with charachange


ssh "Vous plaisantez."

show shizu basic_normal_close_ss at closeright
with characlose


"Avant que je ne puisse répondre, Shizune me prend la main, m’empêchant de le faire. Mes options sont tellement bridées que je n'ai aucun autre choix que de faire une grimace. Elle m'en fait une aussi, et tend sa main à Misha."


"Alors que Misha est réticente à la prendre, je m'approche d'elle autant que je peux tandis que Shizune me tient toujours, et j'attrape moi-même la main de Misha."

show mishashort hips_smile_close_ss
with charachange


mi "...Hahaha."


"Elle n'a qu'une seconde pour sourire avant que Shizune ne nous entraîne impatiemment vers la porte, nous reliant ensemble, comme une chaîne humaine."

stop ambient fadeout 1.0

scene ev shizu_hands
with locationskip


"Bien que ce soit dangereux, aucun d'entre nous ne semble envisager de lâcher prise tandis que nous parcourons l'école et les terrains."


"Ça me semble familier, comme si on avait déjà marché comme ça. Nous trois, main dans la main. Bien sûr, l'ambiance était tout autre."


"Je peux voir la tristesse persistante sur leurs visages, et je me demande si quoi que ce soit a vraiment changé. Si tout ceci n'est qu'une distraction. Mais je crois que je redeviens juste cynique à cause de l'instant. C'est déjà ça, après tout."

stop music fadeout 3.0

window hide
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
